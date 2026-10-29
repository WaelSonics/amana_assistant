#!/usr/bin/env python3
"""Technicals, swing levels, setup check and chart for one or more tickers, from Yahoo daily bars.

Replaces the ad-hoc Python the desk rewrote for every check. Standard library only.

    levels.py MU NVDA                         # technicals + nearest support/resistance
    levels.py MU --zone 855-870 --stop 790 --target 1010 --size 270
                                              # plan checks for a written setup (R/R, ATR distance, chase guard)
    levels.py AMD --chart amd.svg             # candlestick chart with 20/50/200-DMA, RSI, swing levels, zone/stop/target
    levels.py --report                        # live prices for every holding → portfolio_report.py (v6 checks)

Next earnings dates come from Alpha Vantage's EARNINGS_CALENDAR (one call a day, cached). Put a free key in
$ALPHAVANTAGE_API_KEY or ~/.config/amana-desk/alphavantage.key (https://www.alphavantage.co/support/#api-key);
without one the public "demo" key is used, which Alpha Vantage intends for testing only.

Numbers come from Yahoo's unofficial chart API (no key); every output line carries the bar date or quote time.
Bars are cached for 15 minutes in ~/.cache/amana-desk/ (--fresh skips the cache). During the session the last bar is
still open, so the MAs, RSI and ATR move until the close; the output says so.

Levels: swing turns need 3 bars each side; a turn in the last few sessions (2+ bars after it) is listed as provisional
(*). Supports that a later close broke are dropped. The 20/50/200-DMA and the 52-week high are listed with the swings,
so "nearest resistance" includes them.
"""
import argparse
import datetime as dt
import json
import math
import subprocess
import sys
import time
import urllib.request
from pathlib import Path
from zoneinfo import ZoneInfo

CACHE = Path.home() / ".cache" / "amana-desk"
ET = ZoneInfo("America/New_York")
UA = {"User-Agent": "Mozilla/5.0"}
FRESH = False  # --fresh

# NYSE full-day closures, so session counts skip them. Extend every December.
NYSE_HOLIDAYS = {"2026-11-26", "2026-12-25", "2027-01-01", "2027-01-18", "2027-02-15", "2027-03-26", "2027-05-31",
                 "2027-06-18", "2027-07-05", "2027-09-06", "2027-11-25", "2027-12-24"}

# Setup-check thresholds from plan v3 (archive/PLAN-v3-2026-10-29.md). Under v6 the zone check is information only;
# the entry is the dip rule below.
MIN_RR = 2.0
MIN_STOP_ATR = 1.5
CHASE_RSI = 70
CHASE_ABOVE_50 = 0.20
DIP_DRAWDOWN = 0.15  # PLAN v6 §2 dip rule: close this far under the 20-session high close, above a rising 200-DMA
DIP_STOP = 0.25
DIP_TARGET = 0.25
SWING_WINDOW = 3     # 5 hid lower highs that sat next to a higher one (ABBV 289.00 under 291.40)
SWING_MIN_RIGHT = 2  # bars a recent turn needs after it to be listed (as provisional)


def fetch(ticker, rng="2y"):
    CACHE.mkdir(parents=True, exist_ok=True)
    f = CACHE / f"{ticker.replace('^', '_')}-{rng}.json"
    if not FRESH and f.exists() and time.time() - f.stat().st_mtime < 900:
        return json.loads(f.read_text())
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?range={rng}&interval=1d"
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=20) as r:
        data = json.load(r)
    f.write_text(json.dumps(data))
    return data


def bars(ticker):
    res = fetch(ticker)["chart"]["result"][0]
    q = res["indicators"]["quote"][0]
    out = []
    for i, ts in enumerate(res["timestamp"]):
        o, h, l, c, v = (q[k][i] for k in ("open", "high", "low", "close", "volume"))
        if None in (o, h, l, c):
            continue
        out.append({"d": dt.datetime.fromtimestamp(ts, ET).strftime("%Y-%m-%d"), "o": o, "h": h, "l": l, "c": c, "v": v or 0})
    meta = res["meta"]
    now = dt.datetime.now(ET)
    quote = {"price": meta.get("regularMarketPrice"),
             "time": dt.datetime.fromtimestamp(meta["regularMarketTime"], ET).strftime("%Y-%m-%d %H:%M ET"),
             "live": out[-1]["d"] == now.strftime("%Y-%m-%d") and now.hour < 16 and is_session(now.date())}
    return out, quote


def earnings_calendar():
    """{ticker: (reportDate, timeOfTheDay, estimate)} for the next 3 months; cached for a day."""
    import csv, io, os
    f = CACHE / "earnings-calendar.csv"
    CACHE.mkdir(parents=True, exist_ok=True)
    if not f.exists() or time.time() - f.stat().st_mtime > 86400:
        key = os.environ.get("ALPHAVANTAGE_API_KEY")
        kf = Path.home() / ".config" / "amana-desk" / "alphavantage.key"
        if not key and kf.exists():
            key = kf.read_text().strip()
        url = f"https://www.alphavantage.co/query?function=EARNINGS_CALENDAR&horizon=3month&apikey={key or 'demo'}"
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
                text = r.read().decode()
            if text.startswith("symbol,"):
                f.write_text(text)
        except Exception as e:  # the calendar is a convenience; never block the analysis on it
            print(f"  (earnings calendar unavailable: {e})", file=sys.stderr)
    if not f.exists():
        return {}
    out = {}
    for row in csv.DictReader(io.StringIO(f.read_text())):
        if row["symbol"] not in out or row["reportDate"] < out[row["symbol"]][0]:
            out[row["symbol"]] = (row["reportDate"], row.get("timeOfTheDay") or "", row.get("estimate") or "")
    return out


def is_session(d):
    return d.weekday() < 5 and d.isoformat() not in NYSE_HOLIDAYS


def sessions_until(date_str):
    """Sessions from today (exclusive) to the report date (inclusive)."""
    d0 = dt.datetime.now(ET).date()
    d1 = dt.date.fromisoformat(date_str)
    n, d = 0, d0
    while d < d1:
        d += dt.timedelta(days=1)
        if is_session(d):
            n += 1
    return n


def sessions_back(date_str, k):
    """The k-th session before a date."""
    d, m = dt.date.fromisoformat(date_str), 0
    while m < k:
        d -= dt.timedelta(days=1)
        if is_session(d):
            m += 1
    return d.isoformat()


def sma(xs, n, end=None):
    end = len(xs) if end is None else end
    return sum(xs[end - n:end]) / n if end >= n else None


def wilder_rsi(c, n=14):
    g = l = 0.0
    for i in range(1, n + 1):
        d = c[i] - c[i - 1]; g += max(d, 0); l += max(-d, 0)
    g /= n; l /= n
    for i in range(n + 1, len(c)):
        d = c[i] - c[i - 1]; g = (g * (n - 1) + max(d, 0)) / n; l = (l * (n - 1) + max(-d, 0)) / n
    return 100.0 if l == 0 else 100 - 100 / (1 + g / l)


def wilder_atr(b, n=14):
    tr = [max(b[i]["h"] - b[i]["l"], abs(b[i]["h"] - b[i - 1]["c"]), abs(b[i]["l"] - b[i - 1]["c"])) for i in range(1, len(b))]
    a = sum(tr[:n]) / n
    for x in tr[n:]:
        a = (a * (n - 1) + x) / n
    return a


def swings(b, lookback=130, w=SWING_WINDOW):
    """Swing lows and highs as (date, price, provisional). A turn with fewer than w bars after it is provisional."""
    lo, hi = [], []
    n = len(b)
    for i in range(max(w, n - lookback), n - SWING_MIN_RIGHT):
        win = b[i - w:i + w + 1]
        prov = i + w >= n
        if b[i]["l"] == min(x["l"] for x in win):
            lo.append((b[i]["d"], b[i]["l"], prov))
        if b[i]["h"] == max(x["h"] for x in win):
            hi.append((b[i]["d"], b[i]["h"], prov))
    return lo, hi


def dedupe(levels):
    """Drop a level within 0.1% of the one before it (keeps the first label)."""
    out = []
    for p, lab in levels:
        if not out or abs(p / out[-1][0] - 1) > 0.001:
            out.append((p, lab))
    return out


def analyse(ticker):
    b, quote = bars(ticker)
    c = [x["c"] for x in b]
    last = b[-1]
    a = {"ticker": ticker, "bar_date": last["d"], "close": last["c"], "quote": quote,
         "sma20": sma(c, 20), "sma50": sma(c, 50), "sma200": sma(c, 200),
         "sma50_prev": sma(c, 50, len(c) - 10), "sma200_prev": sma(c, 200, len(c) - 20),
         "rsi": wilder_rsi(c), "atr": wilder_atr(b),
         "hi52": max(x["h"] for x in b[-252:]), "lo52": min(x["l"] for x in b[-252:]),
         "hi20c": max(c[-20:]), "sma200_20ago": sma(c, 200, len(c) - 20)}
    px = a["px"] = quote["price"] or last["c"]
    a["swing_lo"], a["swing_hi"] = swings(b)
    sup, res = [], []
    for d, p, prov in a["swing_lo"]:
        # a low that a later close went under is broken, not support
        if p < px and min((x["c"] for x in b if x["d"] > d), default=p) >= p:
            sup.append((p, d[5:] + ("*" if prov else "")))
    for d, p, prov in a["swing_hi"]:
        if p > px:
            res.append((p, d[5:] + ("*" if prov else "")))
    for k in ("sma20", "sma50", "sma200"):
        if a[k]:
            (sup if a[k] < px else res).append((a[k], k[3:] + "-DMA"))
    if a["hi52"] > px:
        res.append((a["hi52"], "52-wk high"))
    a["sup_all"] = dedupe(sorted(sup, reverse=True))
    a["res_all"] = dedupe(sorted(res))
    a["support"], a["resistance"] = a["sup_all"][:4], a["res_all"][:4]
    a["bars"] = b
    return a


def pct(x, y):
    return (x / y - 1) * 100 if y else float("nan")


def down2(x):
    """Round down for display, so a failing 1.496 prints as 1.49, not as a passing-looking 1.50."""
    return math.floor(x * 100) / 100


def slope(now, prev):
    if not (now and prev):
        return "n/a"
    ch = now / prev - 1
    return "flat" if abs(ch) < 0.0025 else "rising" if ch > 0 else "falling"


def print_analysis(a):
    px = a["px"]
    t50, t200 = slope(a["sma50"], a["sma50_prev"]), slope(a["sma200"], a["sma200_prev"])
    print(f"\n{a['ticker']}  ${px:,.2f} ({a['quote']['time']}); last daily bar {a['bar_date']} close ${a['close']:,.2f}")
    if a["quote"]["live"]:
        print("  (today's bar is still open: the MAs, RSI, ATR and 52-wk range move until the close)")
    print(f"  20/50/200-DMA  {a['sma20']:,.2f} / {a['sma50']:,.2f} ({t50}) / {a['sma200']:,.2f} ({t200})"
          f"   price vs 50 {pct(px, a['sma50']):+.1f}%, vs 200 {pct(px, a['sma200']):+.1f}%")
    print(f"  RSI(14) {a['rsi']:.1f}   ATR(14) ${a['atr']:,.2f} = {a['atr'] / px * 100:.1f}% a day"
          f"   52-wk {a['lo52']:,.2f}–{a['hi52']:,.2f} ({pct(px, a['hi52']):+.0f}% from the high)")
    if px > a["sma200"]:
        print(f"  Trend: above a {t200} 200-DMA")
    elif t200 == "falling":
        print("  Trend: BELOW a falling 200-DMA  → protocol §1: no fresh longs, only mean-reversion trims")
    else:
        print(f"  Trend: BELOW a {t200} 200-DMA  → not a trend long (the protocol bans only a falling one; desk 10/24: wait for a reclaim)")
    chase = []
    if a["rsi"] > CHASE_RSI: chase.append(f"RSI {a['rsi']:.0f} > {CHASE_RSI}")
    if px > a["sma50"] * (1 + CHASE_ABOVE_50): chase.append(f"{pct(px, a['sma50']):.0f}% above the 50-DMA")
    print("  Chase guard: " + ("FAIL — " + ", ".join(chase) if chase else "ok"))
    # PLAN v6 §2: the signal is a daily close; during the session it is provisional
    dd = a["close"] / a["hi20c"] - 1
    up200 = a["close"] > a["sma200"] and a["sma200_20ago"] and a["sma200"] > a["sma200_20ago"]
    sig = dd <= -DIP_DRAWDOWN and up200
    print(f"  Dip rule (v6): close {dd * 100:+.1f}% from the 20-session high close ({a['hi20c']:,.2f}); "
          f"200-DMA filter {'pass' if up200 else 'FAIL'} → "
          + (f"SIGNAL{' (provisional: bar still open)' if a['quote']['live'] else ''}: buy at the next open, stop −{DIP_STOP:.0%}, "
             f"take profit +{DIP_TARGET:.0%} or exit after 30 sessions" if sig else "no signal"))
    cal = earnings_calendar().get(a["ticker"])
    if cal:
        n = sessions_until(cal[0])
        when = {"pre-market": "before the open", "post-market": "after the close"}.get(cal[1], "time n/a")
        est = f"Alpha Vantage EPS est. {cal[2]}, often GAAP: check the consensus" if cal[2] else "no EPS est."
        print(f"  Next report: {cal[0]} {when} ({n} session{'' if n == 1 else 's'}; {est})")
        # PLAN §1b: no buy in the 3 sessions before the report, nor on its day (the desk's 10/29–11/3 AMD window)
        print(f"  Earnings blackout {sessions_back(cal[0], 3)} to {cal[0]}: " + ("✘ inside it, no buys" if n <= 3 else "✓ outside it")
              + " (FOMC days, data mornings, client freezes and caps are not checked here)")
    else:
        print("  Next report: not in Alpha Vantage's 3-month calendar (ETFs, monthly reporters such as PGR and some ADRs"
              " are missing: check the company's IR page)")
    fmt = lambda xs: ", ".join(f"{p:,.2f} ({lab})" for p, lab in xs) or "none"
    print(f"  Support below: {fmt(a['support'])}")
    print(f"  Resistance above: {fmt(a['resistance'])}"
          + ("   (* = recent turn, provisional)" if any("*" in lab for _, lab in a["support"] + a["resistance"]) else ""))


def check_setup(a, zlo, zhi, stop, target, size, sleeve):
    atr, px = a["atr"], a["px"]
    print(f"  Setup: zone {zlo:,.2f}–{zhi:,.2f}, stop {stop:,.2f}, T1 {target:,.2f}")
    for name, e in (("low", zlo), ("mid", (zlo + zhi) / 2), ("high", zhi)):
        if e <= stop:
            print(f"    at {name:4} {e:9,.2f}: ✘ entry at or below the stop")
            continue
        rr = (target - e) / (e - stop)
        dist = (e - stop) / atr
        flags = []
        if rr < MIN_RR: flags.append(f"R/R < {MIN_RR:g}")
        if dist < MIN_STOP_ATR: flags.append(f"stop < {MIN_STOP_ATR:g} ATR")
        if (e - stop) / e > 0.15: flags.append("stop > 15% (hard exit)")
        print(f"    at {name:4} {e:9,.2f}: R/R {down2(rr):4.2f}:1, stop {down2(dist):.2f} ATR ({(e - stop) / e * 100:.1f}%)"
              + ("   ✘ " + "; ".join(flags) if flags else "   ✓"))
    # PLAN §3b: T1 is the nearest real resistance above the price (or above the zone, for a zone over the price)
    skipped = [(p, lab) for p, lab in a["res_all"] if max(px, zhi) < p < target * 0.999]
    if skipped and zhi > stop:
        p, lab = skipped[0]
        print(f"    ⚠ T1 skips nearer resistance at {p:,.2f} ({lab}): R/R to it at the high edge {down2((p - zhi) / (zhi - stop)):.2f}:1")
    between = [(p, lab) for p, lab in a["sup_all"] if zhi < p < px]
    if between:
        print("    levels between the zone and the price (a rebound must clear them): "
              + ", ".join(f"{p:,.2f} ({lab})" for p, lab in between[::-1][:3]))
    if size and zhi > stop:
        sh = size / zhi   # a fixed $ size risks most at the zone's high edge
        risk = sh * (zhi - stop)
        print(f"    size ${size:,.0f} ≈ {sh:.4f} sh at the high edge; risk to stop ${risk:,.2f} = {risk / sleeve * 100:.1f}% of ${sleeve:,.0f}"
              + ("   ✘ > 2%" if risk > 0.02 * sleeve else "   ✓ ≤ 2%"))
    if px > zhi:
        print(f"    price {px:,.2f} is {pct(px, zhi):+.1f}% above the zone — wait for the alert at {zhi:,.2f}")
    elif px < zlo:
        print(f"    price {px:,.2f} is {pct(px, zlo):+.1f}% below the zone: as a reclaim zone, buy only after a close back"
              " inside it; as a pullback zone, it broke and needs re-deriving (a lower price is not evidence)")
    else:
        print("    price is IN the zone")


def svg_chart(a, path, days=130, zone=None, stop=None, target=None):
    b = a["bars"][-days:]
    c_all = [x["c"] for x in a["bars"]]
    n0 = len(a["bars"]) - len(b)
    ma = {k: [sma(c_all, k, n0 + i + 1) for i in range(len(b))] for k in (20, 50, 200)}
    # RSI series for the panel
    rsis = []
    for i in range(len(b)):
        end = n0 + i + 1
        rsis.append(wilder_rsi(c_all[:end]) if end > 30 else None)
    W, H, L, R, T = 1100, 640, 70, 90, 40
    PH, RH, GAP = 400, 110, 40
    vals = [x["h"] for x in b] + [x["l"] for x in b] + [v for k in ma for v in ma[k] if v]
    for v in (stop, target, *(zone or ())):
        if v: vals.append(v)
    ymin, ymax = min(vals) * 0.98, max(vals) * 1.02
    cw = (W - L - R) / len(b)
    X = lambda i: L + cw * (i + 0.5)
    Y = lambda p: T + (ymax - p) / (ymax - ymin) * PH
    RY = lambda r: T + PH + GAP + (100 - r) / 100 * RH
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Helvetica,Arial,sans-serif" font-size="12">',
         f'<rect width="{W}" height="{H}" fill="#ffffff"/>',
         f'<text x="{L}" y="24" font-size="16" font-weight="700" fill="#1c1e24">{a["ticker"]} · daily · last bar {a["bar_date"]} · ${a["px"]:,.2f}</text>']
    # grid + price labels
    step = (ymax - ymin) / 6
    for k in range(7):
        p = ymin + k * step
        s.append(f'<line x1="{L}" x2="{W - R}" y1="{Y(p):.1f}" y2="{Y(p):.1f}" stroke="#eceae4"/>')
        s.append(f'<text x="{W - R + 6}" y="{Y(p) + 4:.1f}" fill="#8b8f99">{p:,.2f}</text>')
    # zone / stop / target
    if zone:
        s.append(f'<rect x="{L}" y="{Y(zone[1]):.1f}" width="{W - L - R}" height="{Y(zone[0]) - Y(zone[1]):.1f}" fill="#1f7a4d" fill-opacity="0.12" stroke="#1f7a4d" stroke-opacity="0.5"/>')
        s.append(f'<text x="{L + 6}" y="{Y(zone[1]) - 4:.1f}" fill="#1f7a4d" font-weight="600">buy zone {zone[0]:,.2f}–{zone[1]:,.2f}</text>')
    for v, col, lab in ((stop, "#b3261e", "stop"), (target, "#a5700a", "T1")):
        if v:
            s.append(f'<line x1="{L}" x2="{W - R}" y1="{Y(v):.1f}" y2="{Y(v):.1f}" stroke="{col}" stroke-dasharray="6 4" stroke-width="1.5"/>')
            s.append(f'<text x="{L + 6}" y="{Y(v) - 4:.1f}" fill="{col}" font-weight="600">{lab} {v:,.2f}</text>')
    # recent swing levels as ticks on the right: green below the price (support), red above it (resistance)
    for _, p, _ in a["swing_lo"][-6:] + a["swing_hi"][-6:]:
        col = "#1f7a4d" if p < a["px"] else "#b3261e"
        s.append(f'<line x1="{W - R - 40}" x2="{W - R}" y1="{Y(p):.1f}" y2="{Y(p):.1f}" stroke="{col}" stroke-width="2"/>')
    # candles
    for i, x in enumerate(b):
        up = x["c"] >= x["o"]
        col = "#1f7a4d" if up else "#b3261e"
        s.append(f'<line x1="{X(i):.1f}" x2="{X(i):.1f}" y1="{Y(x["h"]):.1f}" y2="{Y(x["l"]):.1f}" stroke="{col}"/>')
        top, bot = Y(max(x["o"], x["c"])), Y(min(x["o"], x["c"]))
        s.append(f'<rect x="{X(i) - cw * 0.35:.1f}" y="{top:.1f}" width="{cw * 0.7:.1f}" height="{max(bot - top, 1):.1f}" fill="{col}"/>')
    # moving averages
    for k, col in ((20, "#2f5f9e"), (50, "#b8651a"), (200, "#6b5ca5")):
        pts = " ".join(f"{X(i):.1f},{Y(v):.1f}" for i, v in enumerate(ma[k]) if v)
        if pts:
            s.append(f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="1.8"/>')
    lx = L + 6
    for k, col in ((20, "#2f5f9e"), (50, "#b8651a"), (200, "#6b5ca5")):
        s.append(f'<text x="{lx}" y="{T + 14}" fill="{col}" font-weight="600">{k}-DMA</text>'); lx += 64
    # RSI panel
    s.append(f'<text x="{L}" y="{T + PH + GAP - 8}" fill="#5a5e69">RSI(14) {a["rsi"]:.1f}</text>')
    for r, col in ((70, "#b3261e"), (50, "#d6d2c8"), (30, "#1f7a4d")):
        s.append(f'<line x1="{L}" x2="{W - R}" y1="{RY(r):.1f}" y2="{RY(r):.1f}" stroke="{col}" stroke-dasharray="3 3"/>')
        s.append(f'<text x="{W - R + 6}" y="{RY(r) + 4:.1f}" fill="#8b8f99">{r}</text>')
    pts = " ".join(f"{X(i):.1f},{RY(r):.1f}" for i, r in enumerate(rsis) if r is not None)
    s.append(f'<polyline points="{pts}" fill="none" stroke="#1c1e24" stroke-width="1.4"/>')
    # date labels
    for i in range(0, len(b), max(1, len(b) // 8)):
        s.append(f'<text x="{X(i):.1f}" y="{H - 8}" text-anchor="middle" fill="#8b8f99">{b[i]["d"][5:]}</text>')
    s.append("</svg>")
    svg = Path(path).with_suffix(".svg")
    svg.write_text("\n".join(s))
    if str(path).endswith(".png"):
        chrome = next((c for c in ("google-chrome", "chromium", "chromium-browser") if subprocess.run(["which", c], capture_output=True).returncode == 0), None)
        if not chrome:
            print(f"  chart → {svg} (no Chrome for PNG)")
            return
        subprocess.run([chrome, "--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
                        f"--window-size={W},{H + 100}", f"--screenshot={Path(path).resolve()}", f"file://{svg.resolve()}"],
                       capture_output=True, timeout=60)
    print(f"  chart → {path}")


def report():
    root = Path(__file__).resolve()
    while not (root / "portfolio" / "holdings.csv").exists():
        if root.parent == root:
            sys.exit("portfolio/holdings.csv not found")
        root = root.parent
    import csv
    tickers = [r["ticker"] for r in csv.DictReader(open(root / "portfolio" / "holdings.csv"))]
    prices, when = [], set()
    for t in tickers:
        _, q = bars(t)
        prices.append(f"{t}={q['price']}"); when.add(q["time"])
    print("Quotes:", " ".join(prices), "·", ", ".join(sorted(when)), flush=True)
    peak = (root / "portfolio" / "peak.txt").read_text().split("\n")
    peak_v = next((ln.split()[0] for ln in peak if ln and not ln.startswith("#")), None)
    cmd = [sys.executable, str(Path(__file__).with_name("portfolio_report.py")), "--prices", *prices]
    if peak_v:
        cmd += ["--peak", peak_v]
    subprocess.run(cmd, check=False)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("tickers", nargs="*")
    ap.add_argument("--zone", help="LO-HI buy zone")
    ap.add_argument("--stop", type=float)
    ap.add_argument("--target", type=float, help="T1 = nearest real resistance")
    ap.add_argument("--size", type=float, help="planned $ for one fill")
    ap.add_argument("--sleeve", type=float, default=3400.0, help="sleeve value for the 2%% risk check")
    ap.add_argument("--chart", help="write an SVG chart (one ticker) to this path")
    ap.add_argument("--days", type=int, default=130)
    ap.add_argument("--report", action="store_true", help="price every holding and run portfolio_report.py")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--fresh", action="store_true", help="skip the 15-minute bar cache")
    args = ap.parse_args()
    global FRESH
    FRESH = args.fresh
    if args.report:
        return report()
    if not args.tickers:
        ap.error("give at least one ticker, or --report")
    zone = tuple(float(x) for x in args.zone.split("-")) if args.zone else None
    if zone and len(args.tickers) > 1:
        ap.error("--zone/--stop/--target describe one setup: give one ticker")
    for t in args.tickers:
        a = analyse(t)
        if args.json:
            print(json.dumps({k: v for k, v in a.items() if k != "bars"}, default=str))
            continue
        print_analysis(a)
        if zone and args.stop and args.target:
            check_setup(a, zone[0], zone[1], args.stop, args.target, args.size, args.sleeve)
        if args.chart:
            svg_chart(a, args.chart if len(args.tickers) == 1 else f"{Path(args.chart).stem}-{t}.svg",
                      args.days, zone, args.stop, args.target)


if __name__ == "__main__":
    main()
