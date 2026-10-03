#!/usr/bin/env python3
"""Portfolio snapshot + mechanical risk-rule check for the stock sleeve.

Reads portfolio/holdings.csv, portfolio/transactions.csv and portfolio/cash.txt relative to the
project root (found by walking up from this script). Prices must be supplied because there is no
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

SINGLE_NAME_CAP_COST = 0.30
SINGLE_NAME_CAP_MKT = 0.35
CORE_TICKERS = {"VOO"}          # Tier 1 core has its own 30–35% band (PLAN §1), not the single-name cap
THEME_CAP = 0.60
AI_CAP = 0.80
MIN_CASH = 0.10
MAX_POSITIONS = 7
CIRCUIT_BREAKER_DD = 0.10
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
        rows.append({
            "ticker": t, "theme": h.get("theme", "").strip() or "Unclassified",
            "shares": sh, "avg_cost": avg, "price": px,
            "cost": sh * avg, "value": sh * px,
            "pnl": sh * (px - avg), "pnl_pct": (px / avg - 1) if avg else 0.0,
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

    breaches = []
    for r in rows:
        if r["ticker"].upper() in CORE_TICKERS:
            continue
        if r["weight_cost"] > SINGLE_NAME_CAP_COST:
            breaches.append(f"{r['ticker']}: {r['weight_cost']:.0%} of sleeve at cost > {SINGLE_NAME_CAP_COST:.0%} cap")
        if r["weight"] > SINGLE_NAME_CAP_MKT:
            breaches.append(f"{r['ticker']}: {r['weight']:.0%} of sleeve at market > {SINGLE_NAME_CAP_MKT:.0%} cap — trim candidate")
    for th, w in by_theme.items():
        if w > THEME_CAP:
            breaches.append(f"theme '{th}': {w:.0%} > {THEME_CAP:.0%} cap")
    if ai_weight > AI_CAP:
        breaches.append(f"AI race total: {ai_weight:.0%} > {AI_CAP:.0%} cap")
    if cash_weight < MIN_CASH and rows:
        breaches.append(f"cash {cash_weight:.0%} < {MIN_CASH:.0%} minimum")
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
        "breaches": breaches, "missing_prices": missing,
    }
    if args.json:
        print(json.dumps(out, indent=2))
        return

    print(f"Sleeve total: ${total:,.2f}   invested ${invested:,.2f}   cash ${cash:,.2f} ({cash_weight:.0%})")
    print(f"Unrealized P&L: ${out['unrealized_pnl']:+,.2f}   Realized (from log): ${out['realized_total']:+,.2f}")
    if rows:
        print()
        print(f"{'Ticker':<7}{'Theme':<20}{'Shares':>9}{'Avg':>10}{'Price':>10}{'Value':>11}{'P&L%':>8}{'Wt':>7}")
        for r in sorted(rows, key=lambda r: -r["value"]):
            print(f"{r['ticker']:<7}{r['theme'][:19]:<20}{r['shares']:>9.3f}{r['avg_cost']:>10.2f}{r['price']:>10.2f}"
                  f"{r['value']:>11,.2f}{r['pnl_pct']:>8.1%}{r['weight']:>7.0%}")
        print()
        print("By theme: " + ", ".join(f"{th} {w:.0%}" for th, w in sorted(by_theme.items(), key=lambda x: -x[1]))
              + f"  |  AI total {ai_weight:.0%}")
    if missing:
        print(f"\nNo price supplied for {', '.join(missing)} — valued at cost. Fetch and pass --prices.")
    print("\nRule check: " + ("CLEAN" if not breaches else ""))
    for b in breaches:
        print("  ⚠ " + b)


if __name__ == "__main__":
    main()
