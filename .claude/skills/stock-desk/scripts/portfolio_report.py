#!/usr/bin/env python3
"""Portfolio snapshot + mechanical risk-rule check for the stock sleeve.

Reads portfolio/holdings.csv, portfolio/transactions.csv, portfolio/cash.txt and portfolio/levels.csv
(kind, stop, tp, exit_by, theme) relative to the project root (found by walking up from this script). Prices must be supplied because there is no
live feed:

    portfolio_report.py --prices BE=23.10 INTC=24.85 [--peak 1234.56] [--json]

Rule thresholds mirror PLAN.md v6 and references/risk-rules.md; change them there and here together.
"""
import argparse
import csv
import json
import sys
from collections import defaultdict
from pathlib import Path

# Plan v6 (PLAN.md §1, §4, §5; references/risk-rules.md). Change them there and here together.
CORE_TICKERS = {"VOO"}
CORE_TARGET = 0.35              # VOO share of the account; contributions go to VOO while it is under this
DIP_SLOTS = 5                   # open dip trades at most
DIP_SIZE = 400.0                # $ per dip buy
CASH_FLOOR = 150.0              # $ left after any buy
THEME_MAX_OPEN = 2              # open lines per theme, legacy lines included
ACCOUNT_BRAKE_DD = 0.15         # a close this far under the peak pauses new buys for two weeks
DIP_BRAKE = -400.0              # closed dip trades net this → new buys pause until a desk review


def find_root(start: Path) -> Path:
    for p in [start, *start.parents]:
        if (p / "portfolio" / "holdings.csv").exists():
            return p
    sys.exit("could not find portfolio/holdings.csv above %s" % start)


def read_csv(path: Path):
    if not path.exists():
        return []
    with path.open(newline="") as f:
        return [r for r in csv.DictReader(f) if any(v.strip() for v in r.values() if v)]


def read_cash(path: Path) -> float:
    if not path.exists():
        return 0.0
    for line in path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            return float(line.replace(",", ""))
    return 0.0


def parse_prices(items):
    prices = {}
    for it in items or []:
        t, _, p = it.partition("=")
        if not p:
            sys.exit("bad --prices item %r, expected TICKER=PRICE" % it)
        prices[t.upper()] = float(p)
    return prices


def realized_pnl(transactions):
    """Average-cost realized P&L per ticker from the transaction log."""
    lots = defaultdict(lambda: {"shares": 0.0, "cost": 0.0})
    realized = defaultdict(float)
    for tx in sorted(transactions, key=lambda r: r["date"]):
        t = tx["ticker"].upper()
        side = tx["side"].strip().lower()
        sh = float(tx["shares"])
        px = float(tx["price"])
        fee = float(tx.get("fees") or 0)
        lot = lots[t]
        if side == "buy":
            lot["shares"] += sh
            lot["cost"] += sh * px + fee
        elif side == "sell":
            if lot["shares"] <= 0:
                continue
            avg = lot["cost"] / lot["shares"]
            realized[t] += sh * (px - avg) - fee
            lot["cost"] -= sh * avg
            lot["shares"] -= sh
    return dict(realized)


def dip_realized(transactions):
    """Realized P&L of sells tagged DIP in the note (PLAN v6 dip brake)."""
    lots = defaultdict(lambda: {"shares": 0.0, "cost": 0.0})
    total = 0.0
    for tx in sorted(transactions, key=lambda r: r["date"]):
        t, side = tx["ticker"].upper(), tx["side"].strip().lower()
        sh, px, fee = float(tx["shares"]), float(tx["price"]), float(tx.get("fees") or 0)
        lot = lots[t]
        if side == "buy":
            lot["shares"] += sh; lot["cost"] += sh * px + fee
        elif side == "sell" and lot["shares"] > 0:
            avg = lot["cost"] / lot["shares"]
            if "DIP" in (tx.get("note") or ""):
                total += sh * (px - avg) - fee
            lot["cost"] -= sh * avg; lot["shares"] -= sh
    return total


def main():
    import datetime as dt
    ap = argparse.ArgumentParser()
    ap.add_argument("--prices", nargs="*", help="TICKER=PRICE ...")
    ap.add_argument("--peak", type=float, help="peak account value, for the account brake")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    root = find_root(Path(__file__).resolve().parent)
    holdings = read_csv(root / "portfolio" / "holdings.csv")
    transactions = read_csv(root / "portfolio" / "transactions.csv")
    cash = read_cash(root / "portfolio" / "cash.txt")
    levels = {r["ticker"].upper(): r for r in read_csv(root / "portfolio" / "levels.csv")}
    prices = parse_prices(args.prices)
    today = dt.date.today().isoformat()

    num = lambda v: float(v) if (v or "").strip() else None
    rows, missing = [], []
    for h in holdings:
        t = h["ticker"].upper()
        sh, avg = float(h["shares"]), float(h["avg_cost"])
        px = prices.get(t)
        if px is None:
            missing.append(t)
            px = avg
        lvl = levels.get(t, {})
        kind = (lvl.get("kind") or ("core" if t in CORE_TICKERS else "dip")).strip()
        stop, tp = num(lvl.get("stop")), num(lvl.get("tp"))
        rows.append({
            "ticker": t, "kind": kind, "theme": (lvl.get("theme") or h.get("theme") or "Unclassified").strip(),
            "shares": sh, "avg_cost": avg, "price": px, "cost": sh * avg, "value": sh * px,
            "pnl": sh * (px - avg), "pnl_pct": (px / avg - 1) if avg else 0.0,
            "stop": stop, "tp": tp, "exit_by": (lvl.get("exit_by") or "").strip(),
            "stop_risk": sh * max(0.0, px - stop) if stop else 0.0,
        })

    invested = sum(r["value"] for r in rows)
    total = invested + cash
    for r in rows:
        r["weight"] = r["value"] / total if total else 0.0
    core_w = sum(r["weight"] for r in rows if r["kind"] == "core")
    dips = [r for r in rows if r["kind"] == "dip"]
    themes = defaultdict(list)
    for r in rows:
        if r["kind"] != "core":
            themes[r["theme"]].append(r["ticker"])
    fits = 0
    while len(dips) + fits < DIP_SLOTS and cash - DIP_SIZE * (fits + 1) >= CASH_FLOOR:
        fits += 1
    dip_closed = dip_realized(transactions)
    brake_line = args.peak * (1 - ACCOUNT_BRAKE_DD) if args.peak else None

    breaches, notes = [], []
    for r in rows:
        if r["kind"] == "core":
            continue
        if r["stop"] is None or r["tp"] is None:
            breaches.append(f"{r['ticker']}: no {'stop' if r['stop'] is None else 'take-profit'} recorded — rule 3: set SL and TP in the app")
        if r["exit_by"] and r["exit_by"] <= today:
            breaches.append(f"{r['ticker']}: time exit due ({r['exit_by']}) — sell at the close")
    if len(dips) > DIP_SLOTS:
        breaches.append(f"{len(dips)} dip trades open > {DIP_SLOTS} slots")
    if cash < CASH_FLOOR:
        breaches.append(f"cash ${cash:,.2f} < ${CASH_FLOOR:,.0f} floor — no buys")
    for th, names in themes.items():
        if len(names) > THEME_MAX_OPEN:
            breaches.append(f"theme '{th}': {len(names)} open lines ({', '.join(names)}) > {THEME_MAX_OPEN}")
    if brake_line and total < brake_line:
        breaches.append(f"ACCOUNT BRAKE: ${total:,.2f} < ${brake_line:,.2f} (−{ACCOUNT_BRAKE_DD:.0%} from the ${args.peak:,.2f} peak) — on a close, new buys pause two weeks")
    if dip_closed <= DIP_BRAKE:
        breaches.append(f"DIP BRAKE: closed dip trades net ${dip_closed:+,.2f} ≤ ${DIP_BRAKE:,.0f} — new buys pause until a desk review")
    if rows and core_w < CORE_TARGET:
        notes.append(f"VOO {core_w:.1%} < {CORE_TARGET:.0%}: the monthly $200 goes to VOO")

    realized = realized_pnl(transactions)
    out = {
        "total": total, "cash": cash, "invested": invested, "core_weight": core_w,
        "unrealized_pnl": sum(r["pnl"] for r in rows), "realized_pnl": realized, "realized_total": sum(realized.values()),
        "positions": rows, "dip_open": len(dips), "dip_buys_that_fit": fits, "themes": dict(themes),
        "dip_closed_pnl": dip_closed, "account_brake": brake_line, "breaches": breaches, "notes": notes,
        "missing_prices": missing,
    }
    if args.json:
        print(json.dumps(out, indent=2))
        return

    print(f"Account ${total:,.2f}   VOO {core_w:.1%} (target {CORE_TARGET:.0%})   cash ${cash:,.2f} ({cash / total:.0%})")
    print(f"Unrealized P&L ${out['unrealized_pnl']:+,.2f}   Realized (from log) ${out['realized_total']:+,.2f}")
    if rows:
        print()
        print(f"{'Ticker':<7}{'Kind':<8}{'Theme':<20}{'Shares':>9}{'Avg':>9}{'Price':>9}{'Value':>10}{'P&L%':>8}{'Wt':>6}"
              f"{'Stop':>9}{'TP':>9}{'Risk$':>7}  Exit by")
        for r in sorted(rows, key=lambda r: -r["value"]):
            f = lambda v: f"{v:>9.2f}" if v else f"{'—':>9}"
            print(f"{r['ticker']:<7}{r['kind']:<8}{r['theme'][:19]:<20}{r['shares']:>9.3f}{r['avg_cost']:>9.2f}{r['price']:>9.2f}"
                  f"{r['value']:>10,.2f}{r['pnl_pct']:>8.1%}{r['weight']:>6.0%}{f(r['stop'])}{f(r['tp'])}{r['stop_risk']:>7.0f}  {r['exit_by']}")
        print()
    print(f"Dip slots {len(dips)}/{DIP_SLOTS} · ${DIP_SIZE:,.0f} buys that fit now with ≥ ${CASH_FLOOR:,.0f} cash left: {fits}")
    print("Themes (max " + str(THEME_MAX_OPEN) + " open): " + (", ".join(f"{th} {len(n)}" for th, n in themes.items()) or "none"))
    if brake_line:
        print(f"Account brake ${brake_line:,.2f}: ${total - brake_line:+,.2f} away · dip brake: closed dip trades net "
              f"${dip_closed:+,.2f} (pause at ${DIP_BRAKE:,.0f})")
    if missing:
        print(f"\nNo price supplied for {', '.join(missing)} — valued at cost. Fetch and pass --prices.")
    print("\nRule check: " + ("CLEAN" if not breaches else ""))
    for b in breaches:
        print("  ⚠ " + b)
    for n in notes:
        print("  · " + n)


if __name__ == "__main__":
    main()
