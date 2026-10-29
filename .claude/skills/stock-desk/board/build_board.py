#!/usr/bin/env python3
"""Build the plan-v6 Flag Board page.

    python3 .claude/skills/stock-desk/board/build_board.py OUT.html

Numbers come from the repo (portfolio/*.csv, cash.txt, peak.txt), live Yahoo bars (levels.py) and the Alpha Vantage
earnings calendar. The desk's words (next steps, calendar, watchlist themes, the eight rules) come from board/notes.json:
edit that file, then rebuild. The page is flag-board.template.html with the data injected.
"""
import datetime as dt
import importlib.util
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True   # keep the imported scripts from writing __pycache__ into the repo
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


lv = load("levels", HERE.parent / "scripts" / "levels.py")
pr = load("portfolio_report", HERE.parent / "scripts" / "portfolio_report.py")
lv.FRESH = True


def main(out):
    notes = json.loads((HERE / "notes.json").read_text())
    holdings = pr.read_csv(ROOT / "portfolio" / "holdings.csv")
    levels = {r["ticker"].upper(): r for r in pr.read_csv(ROOT / "portfolio" / "levels.csv")}
    cash = pr.read_cash(ROOT / "portfolio" / "cash.txt")
    peak_line = next(ln for ln in (ROOT / "portfolio" / "peak.txt").read_text().splitlines() if ln and not ln.startswith("#"))
    peak, peak_date = float(peak_line.split()[0]), peak_line.split()[1]
    dip_closed = pr.dip_realized(pr.read_csv(ROOT / "portfolio" / "transactions.csv"))
    cal = lv.earnings_calendar()
    nbd = notes["next_buy_day"]
    stamps = set()

    lines = []
    for h in holdings:
        t = h["ticker"].upper()
        a = lv.analyse(t)
        stamps.add(a["quote"]["time"])
        lvl = levels.get(t, {})
        num = lambda k: float(lvl[k]) if (lvl.get(k) or "").strip() else None
        sh, avg, px = float(h["shares"]), float(h["avg_cost"]), a["px"]
        lines.append({"t": t, "kind": lvl.get("kind", ""), "theme": lvl.get("theme", ""), "sh": sh, "avg": avg, "px": px,
                      "value": sh * px, "pnl": sh * (px - avg), "stop": num("stop"), "tp": num("tp"),
                      "exit_by": lvl.get("exit_by", ""), "report": cal.get(t, [None])[0]})
    total = cash + sum(x["value"] for x in lines)
    held = {x["t"] for x in lines}
    dips_open = sum(1 for x in lines if x["kind"] == "dip")
    fits = 0
    while dips_open + fits < pr.DIP_SLOTS and cash - pr.DIP_SIZE * (fits + 1) >= pr.CASH_FLOOR:
        fits += 1
    theme_count = {}
    for x in lines:
        if x["kind"] != "core":
            theme_count[x["theme"]] = theme_count.get(x["theme"], 0) + 1

    scan = []
    for theme, names in notes["watchlist"].items():
        for t in names:
            try:
                a = lv.analyse(t)
            except Exception as e:  # one bad quote never blocks the board
                scan.append({"t": t, "theme": theme, "error": str(e)})
                continue
            stamps.add(a["quote"]["time"])
            dd = a["close"] / a["hi20c"] - 1
            up = bool(a["close"] > a["sma200"] and a["sma200_20ago"] and a["sma200"] > a["sma200_20ago"])
            rep = cal.get(t, [None, ""])
            blocked = bool(rep[0] and lv.sessions_back(rep[0], 3) <= nbd <= rep[0])
            before = bool(rep[0] and rep[0] < nbd)
            if t in held:
                status = "held"
            elif dd <= -lv.DIP_DRAWDOWN and up:
                status = "blackout" if blocked else "signal"
            elif up and dd <= -0.12:
                status = "near"
            else:
                status = "none"
            scan.append({"t": t, "theme": theme, "px": a["px"], "dd": dd, "up": up, "vs200": a["close"] / a["sma200"] - 1,
                         "report": rep[0], "when": {"pre-market": "BMO", "post-market": "AMC"}.get(rep[1], ""),
                         "before_buy_day": before, "status": status, "live": a["quote"]["live"]})

    data = {
        "asof": max(stamps), "plan": notes["plan"], "next_buy_day": nbd,
        "total": total, "cash": cash, "peak": peak, "peak_date": peak_date,
        "brake": peak * (1 - pr.ACCOUNT_BRAKE_DD), "dip_closed": dip_closed, "dip_brake": pr.DIP_BRAKE,
        "slots": pr.DIP_SLOTS, "dips_open": dips_open, "fits": fits, "size": pr.DIP_SIZE, "floor": pr.CASH_FLOOR,
        "core_target": pr.CORE_TARGET, "core_value": sum(x["value"] for x in lines if x["kind"] == "core"),
        "theme_max": pr.THEME_MAX_OPEN, "theme_count": theme_count,
        "lines": lines, "scan": scan, "steps": notes["steps"], "calendar": notes["calendar"], "rules": notes["rules"],
    }
    page = (HERE / "flag-board.template.html").read_text()
    Path(out).write_text(page.replace("/*DATA*/null", json.dumps(data, ensure_ascii=False)))
    print(f"{out}: account ${total:,.2f} · brake ${data['brake']:,.2f} · {fits} buys fit · "
          f"signals: {', '.join(s['t'] for s in scan if s.get('status') == 'signal') or 'none'} · as of {data['asof']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
