#!/usr/bin/env python3
"""Portfolio snapshot + mechanical risk-rule check for the stock sleeve.

Reads portfolio/holdings.csv, portfolio/transactions.csv, portfolio/cash.txt and portfolio/levels.csv
(stops, buy/sell zones) relative to the project root (found by walking up from this script). Prices must be supplied because there is no
live feed:

    portfolio_report.py --prices BE=23.10 INTC=24.85 [--peak 1234.56] [--json]

Rule thresholds mirror references/risk-rules.md; change them there and here together.
"""
import argparse
import csv
import json
import sys
from collections import defaultdict
from pathlib import Path

NAME_NO_ADD = 0.15              # PLAN §4: no add may take a name past 15%
NAME_TRIM = 0.20                # PLAN §3: above 20% at market → trim back to 15%
CORE_TICKERS = {"VOO"}          # Tier 1 core has its own 30–35% band (PLAN §1), not the single-name cap
THEME_CAP = 0.60
AI_CAP = 0.80
MIN_CASH = 0.075                # v3 floor for discretionary buys (index ladder may go to 5%)
MAX_POSITIONS = 7
CIRCUIT_BREAKER_DD = 0.10
OPEN_RISK_CAP = 0.08            # v3: all satellite stops hit at once must cost < 8% of the sleeve
PER_BUY_RISK = 0.02             # v3: one buy may risk ≤ 2% of the sleeve to its stop
TIER_BANDS = {"Core": (0.30, 0.35), "Satellites": (0.45, 0.60), "Reserve": (0.075, 0.25)}
NON_AI_THEMES = {"non-ai", "cash", "other"}


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


def parse_zone(text):
    lo, _, hi = (text or "").partition("-")
    try:
        return float(lo), float(hi)
    except ValueError:
        return None


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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prices", nargs="*", help="TICKER=PRICE ...")
    ap.add_argument("--peak", type=float, help="peak sleeve value, for the drawdown circuit breaker")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    root = find_root(Path(__file__).resolve().parent)
    holdings = read_csv(root / "portfolio" / "holdings.csv")
    transactions = read_csv(root / "portfolio" / "transactions.csv")
    cash = read_cash(root / "portfolio" / "cash.txt")
    levels = {r["ticker"].upper(): r for r in read_csv(root / "portfolio" / "levels.csv")}
    prices = parse_prices(args.prices)

    rows, missing = [], []
    for h in holdings:
        t = h["ticker"].upper()
        sh = float(h["shares"])
        avg = float(h["avg_cost"])
        px = prices.get(t)
        if px is None:
            missing.append(t)
            px = avg
        lvl = levels.get(t, {})
        stop = float(lvl["stop"]) if (lvl.get("stop") or "").strip() else None
        buy, sell = parse_zone(lvl.get("buy_zone")), parse_zone(lvl.get("sell_zone"))
        if buy and buy[0] <= px <= buy[1]:
            zone = f"IN BUY ZONE {buy[0]:g}-{buy[1]:g}"
        elif sell and px >= sell[0]:
            zone = f"IN SELL ZONE {sell[0]:g}-{sell[1]:g}: trade-around 1/3 allowed"
        else:
            zone = ""
        rows.append({
            "ticker": t, "theme": h.get("theme", "").strip() or "Unclassified",
            "shares": sh, "avg_cost": avg, "price": px,
            "cost": sh * avg, "value": sh * px,
            "pnl": sh * (px - avg), "pnl_pct": (px / avg - 1) if avg else 0.0,
            "stop": stop, "stop_risk": sh * max(0.0, px - stop) if stop else 0.0, "zone": zone,
        })

    invested = sum(r["value"] for r in rows)
    total = invested + cash
    for r in rows:
        r["weight"] = r["value"] / total if total else 0.0
        r["weight_cost"] = r["cost"] / total if total else 0.0

    by_theme = defaultdict(float)
    for r in rows:
        by_theme[r["theme"]] += r["weight"]
    ai_weight = sum(w for th, w in by_theme.items() if th.lower() not in NON_AI_THEMES)
    cash_weight = cash / total if total else 1.0

    satellites = [r for r in rows if r["ticker"] not in CORE_TICKERS]
    open_risk = sum(r["stop_risk"] for r in satellites)
    tiers = {"Core": sum(r["weight"] for r in rows if r["ticker"] in CORE_TICKERS),
             "Satellites": sum(r["weight"] for r in satellites), "Reserve": cash_weight}

    breaches, notes = [], []
    for r in satellites:
        if r["weight"] > NAME_TRIM:
            breaches.append(f"{r['ticker']}: {r['weight']:.0%} of sleeve at market > {NAME_TRIM:.0%} — trim back to {NAME_NO_ADD:.0%}")
        elif r["weight"] > NAME_NO_ADD:
            notes.append(f"{r['ticker']}: {r['weight']:.0%} > {NAME_NO_ADD:.0%} — no adds")
        if r["stop"] is None:
            notes.append(f"{r['ticker']}: no stop in levels.csv — open risk unknown")
    if total and open_risk / total > OPEN_RISK_CAP:
        breaches.append(f"open stop-risk ${open_risk:,.0f} = {open_risk / total:.1%} > {OPEN_RISK_CAP:.0%} — no buys until a trim or a stop raise")
    for name, (lo, hi) in TIER_BANDS.items():
        if rows and not lo <= tiers[name] <= hi:
            notes.append(f"{name} {tiers[name]:.1%} outside its {lo:.1%}–{hi:.0%} band")
    for th, w in by_theme.items():
        if w > THEME_CAP:
            breaches.append(f"theme '{th}': {w:.0%} > {THEME_CAP:.0%} cap")
    if ai_weight > AI_CAP:
        breaches.append(f"AI race total: {ai_weight:.0%} > {AI_CAP:.0%} cap")
    if cash_weight < MIN_CASH and rows:
        breaches.append(f"cash {cash_weight:.1%} < {MIN_CASH:.1%} floor — no discretionary buys")
    if len(rows) > MAX_POSITIONS:
        breaches.append(f"{len(rows)} positions > {MAX_POSITIONS} max")
    if args.peak and total < args.peak * (1 - CIRCUIT_BREAKER_DD):
        breaches.append(f"CIRCUIT BREAKER: sleeve {total:,.2f} is {1 - total / args.peak:.1%} below peak {args.peak:,.2f}")

    realized = realized_pnl(transactions)
    out = {
        "total": total, "cash": cash, "cash_weight": cash_weight, "invested": invested,
        "unrealized_pnl": sum(r["pnl"] for r in rows),
        "realized_pnl": realized, "realized_total": sum(realized.values()),
        "positions": rows, "by_theme": dict(by_theme), "ai_weight": ai_weight,
        "open_risk": open_risk, "open_risk_weight": open_risk / total if total else 0.0,
        "max_risk_per_buy": PER_BUY_RISK * total, "tiers": tiers,
        "breaches": breaches, "notes": notes, "missing_prices": missing,
    }
    if args.json:
        print(json.dumps(out, indent=2))
        return

    print(f"Sleeve total: ${total:,.2f}   invested ${invested:,.2f}   cash ${cash:,.2f} ({cash_weight:.0%})")
    print(f"Unrealized P&L: ${out['unrealized_pnl']:+,.2f}   Realized (from log): ${out['realized_total']:+,.2f}")
    if rows:
        print()
        print(f"{'Ticker':<7}{'Theme':<20}{'Shares':>9}{'Avg':>10}{'Price':>10}{'Value':>11}{'P&L%':>8}{'Wt':>7}"
              f"{'Stop':>9}{'Risk$':>8}  Zone")
        for r in sorted(rows, key=lambda r: -r["value"]):
            stop = f"{r['stop']:>9.2f}{r['stop_risk']:>8.0f}" if r["stop"] else f"{'—':>9}{'—':>8}"
            print(f"{r['ticker']:<7}{r['theme'][:19]:<20}{r['shares']:>9.3f}{r['avg_cost']:>10.2f}{r['price']:>10.2f}"
                  f"{r['value']:>11,.2f}{r['pnl_pct']:>8.1%}{r['weight']:>7.0%}{stop}  {r['zone']}")
        print()
        print("By theme: " + ", ".join(f"{th} {w:.0%}" for th, w in sorted(by_theme.items(), key=lambda x: -x[1]))
              + f"  |  AI total {ai_weight:.0%}")
        print("Tiers: " + " · ".join(f"{n} {tiers[n]:.1%} ({lo:.1%}–{hi:.0%})" for n, (lo, hi) in TIER_BANDS.items()))
        print(f"Open stop-risk ${open_risk:,.0f} = {out['open_risk_weight']:.1%} of sleeve (cap {OPEN_RISK_CAP:.0%})"
              f"  |  max risk per new buy ${out['max_risk_per_buy']:,.0f} ({PER_BUY_RISK:.0%})")
    if missing:
        print(f"\nNo price supplied for {', '.join(missing)} — valued at cost. Fetch and pass --prices.")
    print("\nRule check: " + ("CLEAN" if not breaches else ""))
    for b in breaches:
        print("  ⚠ " + b)
    for n in notes:
        print("  · " + n)


if __name__ == "__main__":
    main()
