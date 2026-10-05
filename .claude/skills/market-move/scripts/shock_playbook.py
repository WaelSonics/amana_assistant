#!/usr/bin/env python3
"""Mechanical playbook for a sharp market move, derived from PLAN.md.

Reads portfolio/holdings.csv, portfolio/cash.txt, portfolio/levels.csv, portfolio/peak.txt.
Prices and index context are passed in (no live feed):

  shock_playbook.py --prices AMD=470 ARM=240 ... --spx-now 6100 --spx-high 6600 \
                    --day-move -3.2 [--vix 31] [--json]

Outputs: shock classification, per-holding rule hits (stop / ladder stage / cap), reserve tranche
that PLAN.md §5 allows to deploy, circuit-breaker status, and a do-not list. Thresholds mirror
PLAN.md §3–§7; change both together.
"""
import argparse, csv, json, sys
from pathlib import Path

# PLAN.md §3 ratchet
LADDER = [(0.25, "move stop to breakeven"), (0.40, "sell 1/3"), (0.75, "sell 1/3 (cost fully recovered)")]
NAME_CAP_MKT = 0.20          # trim back to TRIM_TO
TRIM_TO = 0.15
HARD_LOSS = -0.15            # §4
# §5 reserve ladder (S&P drawdown from high)
TRANCHE_0_DD = -0.04            # v2: quarter of reserve, VOO only
TRANCHE_1_DD = -0.07
TRANCHE_2_DD = -0.15
CASH_FLOOR = 0.05
RESERVE_TARGET = 0.075         # v3 floor for discretionary buys
# §7 circuit breaker (sleeve drawdown from peak)
CIRCUIT_BREAKER = -0.10
# up-shock guards (§2 entry rules)
BIG_DAY = 0.03
CHASE_ABOVE_50DMA = 0.20


def root():
    for p in [Path(__file__).resolve(), *Path(__file__).resolve().parents]:
        if (p / "portfolio" / "holdings.csv").exists():
            return p
    sys.exit("portfolio/holdings.csv not found above script")


def rows(path):
    if not path.exists():
        return []
    with path.open(newline="") as f:
        return [r for r in csv.DictReader(f) if any((v or "").strip() for v in r.values())]


def first_number(path):
    for line in path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            return float(line.split()[0].replace(",", ""))
    return 0.0


def kv(items):
    out = {}
    for it in items or []:
        k, _, v = it.partition("=")
        if not v:
            sys.exit(f"bad item {it!r}, expected TICKER=VALUE")
        out[k.upper()] = float(v)
    return out


def zone(text):
    lo, _, hi = (text or "").partition("-")
    try:
        return float(lo), float(hi)
    except ValueError:
        return None


def classify(day_move, spx_dd, vix):
    mag = abs(day_move)
    if day_move <= -0.05 or spx_dd <= TRANCHE_2_DD:
        cls = "CRASH"
    elif day_move <= -0.03 or spx_dd <= TRANCHE_1_DD:
        cls = "SELL-OFF"
    elif day_move <= -0.015:
        cls = "RED DAY"
    elif day_move >= 0.05:
        cls = "MELT-UP"
    elif day_move >= BIG_DAY:
        cls = "BIG GREEN DAY"
    elif day_move >= 0.015:
        cls = "GREEN DAY"
    else:
        cls = "NOISE"
    if vix is not None and vix >= 30 and day_move < 0:
        cls += " / VIX≥30"
    return cls


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prices", nargs="+", required=True)
    ap.add_argument("--day-move", type=float, required=True, help="index move today in %% (e.g. -3.2)")
    ap.add_argument("--spx-now", type=float, required=True)
    ap.add_argument("--spx-high", type=float, required=True, help="S&P 500 recent closing high")
    ap.add_argument("--vix", type=float)
    ap.add_argument("--dma50", nargs="*", help="optional TICKER=50DMA for chase check")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    R = root()
    prices, dma50 = kv(a.prices), kv(a.dma50)
    holdings = rows(R / "portfolio" / "holdings.csv")
    levels = {r["ticker"].upper(): r for r in rows(R / "portfolio" / "levels.csv")}
    cash = first_number(R / "portfolio" / "cash.txt")
    peak = first_number(R / "portfolio" / "peak.txt") if (R / "portfolio" / "peak.txt").exists() else None

    missing = [h["ticker"] for h in holdings if h["ticker"].upper() not in prices]
    if missing:
        sys.exit("missing --prices for: " + ", ".join(missing))

    day = a.day_move / 100.0
    spx_dd = a.spx_now / a.spx_high - 1.0
    cls = classify(day, spx_dd, a.vix)
    down = day < 0 or spx_dd <= TRANCHE_1_DD

    pos = []
    for h in holdings:
        t = h["ticker"].upper(); sh = float(h["shares"]); ac = float(h["avg_cost"]); px = prices[t]
        pos.append(dict(ticker=t, shares=sh, avg_cost=ac, price=px, value=sh * px, pnl=px / ac - 1.0,
                        theme=h["theme"], lvl=levels.get(t, {})))
    invested = sum(p["value"] for p in pos)
    equity = invested + cash
    cash_w = cash / equity if equity else 0

    actions, watch, donts = [], [], []
    for p in pos:
        p["weight"] = p["value"] / equity if equity else 0
        L = p["lvl"]; t = p["ticker"]; core = (L.get("stop_type") == "none")
        stop = float(L["stop"]) if L.get("stop") else None
        done = int(L.get("ladder_done") or 0)
        p["signals"] = []

        if core:
            p["signals"].append("CORE — never trimmed; first target for reserve deployment")
            continue
        # stops / hard loss
        if stop and p["price"] <= stop:
            p["signals"].append(f"STOP HIT {stop:.2f} ({L.get('stop_type')}) → EXIT unless a weekly-close rule applies; re-entry allowed later")
            actions.append(f"{t}: EXIT — {L.get('stop_type')} stop {stop:.2f} breached at {p['price']:.2f}")
        elif p["pnl"] <= HARD_LOSS:
            p["signals"].append(f"HARD LOSS {p['pnl']:+.1%} ≤ −15% → EXIT")
            actions.append(f"{t}: EXIT — hard loss rule {p['pnl']:+.1%}")
        elif stop:
            room = p["price"] / stop - 1.0
            p["signals"].append(f"stop {stop:.2f} is {room:.1%} below" + (" — CLOSE; do not add" if room < 0.05 else ""))
        # ladder — a gap through several stages fires them together as one trim
        fired = [(i, thr, act) for i, (thr, act) in enumerate(LADDER) if p["pnl"] >= thr and done < i + 1]
        sell_stages = [(i, thr) for i, thr, _ in fired if i > 0]
        for i, thr, act in fired:
            p["signals"].append(f"LADDER stage {i+1} (+{thr:.0%}) reached at {p['pnl']:+.1%} → {act}")
        if any(i == 0 for i, _, _ in fired) and not sell_stages:
            watch.append(f"{t}: stop → breakeven {p['avg_cost']:.2f}")
        if sell_stages:
            frac = len(sell_stages) / 3.0
            sh_sell = p["shares"] * frac
            stages = "+".join(f"{thr:.0%}" for _, thr in sell_stages)
            actions.append(f"{t}: SELL {len(sell_stages)}/3 ≈ {sh_sell:.4f} sh ≈ ${sh_sell*p['price']:,.0f} — ratchet {stages}"
                           + (" (cost fully recovered)" if sell_stages[-1][0] == 2 else "")
                           + f" → set ladder_done={sell_stages[-1][0]+1}; banked → reserve until 15%, then 50% VOO / 50% reserve")
        # cap
        if p["weight"] > NAME_CAP_MKT:
            excess = (p["weight"] - TRIM_TO) * equity
            p["signals"].append(f"CAP {p['weight']:.1%} > 20% → trim ${excess:,.0f} back to 15%")
            actions.append(f"{t}: TRIM ${excess:,.0f} — concentration cap")
        # v3 trade-around zones (PLAN §3b): optional, never forced
        buy, sell = zone(L.get("buy_zone")), zone(L.get("sell_zone"))
        if sell and p["price"] >= sell[0] and not sell_stages:
            p["signals"].append(f"SELL ZONE {sell[0]:g}-{sell[1]:g} → trade-around: may sell up to 1/3 (proceeds → reserve)")
            watch.append(f"{t}: optional trade-around sell of up to 1/3 ≈ {p['shares']/3:.4f} sh in {sell[0]:g}-{sell[1]:g}")
        elif buy and buy[0] <= p["price"] <= buy[1]:
            p["signals"].append(f"BUY ZONE {buy[0]:g}-{buy[1]:g} → add only if cash stays ≥ {RESERVE_TARGET:.1%} after it, "
                                f"adds remain ({L.get('adds_used') or 0} of 2 used), outside the 3-session earnings blackout; index rungs first")
        # catalyst proximity
        if L.get("catalyst_date"):
            p["signals"].append(f"catalyst: {L.get('catalyst')} {L.get('catalyst_date')} — trim INTO run-up, not after")
        # up-shock chase guard
        if t in dma50 and dma50[t] and p["price"] / dma50[t] - 1.0 > CHASE_ABOVE_50DMA:
            p["signals"].append(f"{p['price']/dma50[t]-1.0:+.0%} above 50-DMA → NO ADD (chase guard)")
            donts.append(f"do not add {t} ({p['price']/dma50[t]-1.0:+.0%} vs 50-DMA)")

    # reserve logic (§5)
    reserve = {"cash": cash, "weight": cash_w, "deployable_now": 0.0, "tranche": None}
    floor_cash = CASH_FLOOR * equity
    if down:
        if spx_dd <= TRANCHE_2_DD:
            reserve["tranche"] = "2 — deploy remaining reserve down to the 5% floor"
            reserve["deployable_now"] = max(0.0, cash - floor_cash)
        elif spx_dd <= TRANCHE_1_DD:
            reserve["tranche"] = "1 — deploy up to HALF of reserve (VOO first, then best-rated satellite at its 50-DMA)"
            reserve["deployable_now"] = max(0.0, min(cash / 2.0, cash - floor_cash))
        elif spx_dd <= TRANCHE_0_DD:
            reserve["tranche"] = "0 — deploy up to a QUARTER of reserve, VOO only"
            reserve["deployable_now"] = max(0.0, min(cash / 4.0, cash - floor_cash))
        else:
            reserve["tranche"] = f"none — S&P only {spx_dd:.1%} from high; §5 needs −4%. Sit."
    else:
        reserve["tranche"] = "none — up-move. Reserve is not deployed on green days."
        if cash_w < RESERVE_TARGET:
            donts.append(f"reserve {cash_w:.1%} < {RESERVE_TARGET:.1%} floor → no discretionary buys; next contribution to cash")
    if reserve["deployable_now"] > 0:
        actions.append(f"DEPLOY up to ${reserve['deployable_now']:,.0f} of reserve — VOO first, then best-rated satellite at/near its 50-DMA with thesis intact; limit orders, not market (§5 tranche {reserve['tranche'][0]})")
    if day >= BIG_DAY:
        donts.append("no buys on a ≥+3% index day — chase guard (§2); ladder, cap and trade-around trims are allowed")
    if day <= -0.03 and reserve["deployable_now"] == 0:
        donts.append("do not 'buy the dip' on a red day the ladder hasn't unlocked — that is exactly the pre-reset pattern")
    donts.append("no shorts / leverage / options (cash account, PLAN §2)")
    donts.append("never touch VOO or the gold/cash vault to fund a satellite")

    # circuit breaker (§7)
    cb = None
    if peak:
        sleeve_dd = equity / peak - 1.0
        cb = {"peak": peak, "equity": equity, "drawdown": sleeve_dd, "tripped": sleeve_dd <= CIRCUIT_BREAKER}
        if cb["tripped"]:
            actions.insert(0, f"CIRCUIT BREAKER: sleeve {sleeve_dd:.1%} from peak ${peak:,.0f} → halve every satellite, pause buys, write post-mortem (overrides reserve deployment)")
            reserve["deployable_now"] = 0.0
            reserve["tranche"] = "SUSPENDED — circuit breaker"
            actions[:] = [x for x in actions if not x.startswith("DEPLOY")]
            donts.insert(0, "no reserve deployment while the circuit breaker is tripped — even though the S&P tranche is unlocked")

    out = dict(classification=cls, day_move=day, spx_drawdown=spx_dd, vix=a.vix, equity=equity,
               invested=invested, positions=pos, reserve=reserve, circuit_breaker=cb,
               actions=actions, watch=watch, donts=donts)
    if a.json:
        print(json.dumps(out, indent=2, default=str)); return

    print(f"== SHOCK CLASS: {cls}  | index today {day:+.1%} | S&P {spx_dd:+.1%} from high"
          + (f" | VIX {a.vix:.0f}" if a.vix else ""))
    print(f"   sleeve ${equity:,.0f} (invested ${invested:,.0f}, cash ${cash:,.0f} = {cash_w:.1%})"
          + (f" | vs peak {cb['drawdown']:+.1%}" if cb else ""))
    print("\n-- positions")
    for p in pos:
        print(f"{p['ticker']:5} {p['price']:>9.2f}  {p['pnl']:+6.1%}  w={p['weight']:5.1%}  rating={p['lvl'].get('rating','?')}")
        for s in p["signals"]:
            print(f"        - {s}")
    print("\n-- reserve (PLAN §5)")
    print(f"   tranche: {reserve['tranche']}")
    if reserve["deployable_now"]:
        print(f"   deployable now: ${reserve['deployable_now']:,.0f} (cash floor ${floor_cash:,.0f})")
    print("\n-- MECHANICAL ACTIONS" + ("" if actions else " (none — the rules say do nothing)"))
    for x in actions: print("   * " + x)
    if watch:
        print("\n-- adjust")
        for x in watch: print("   * " + x)
    print("\n-- DO NOT")
    for x in donts: print("   x " + x)


if __name__ == "__main__":
    main()
