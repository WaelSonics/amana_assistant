# Non-AI diversifier screen — 2026-10-23 (data: 10/22 close)

Client: "If we stay at v3, what do you think the other stocks other than AI and chips would be? Our research was mainly there.
Please do a research to prepare for new buys outside these 2 that failed drastically this month." The client acknowledged that
the WDC/STX/SNDK buys were greed, expecting the old swings to repeat.

## Desk challenge (once)
"They used to swing back" is not a level. It is how WDC, STX, SNDK and EWY were bought after their stops, and those dip-buys
cost $91.87 by 10/14 and more after. §4a exists because a falling price is information, not a discount.

## Plan constraints before any buy
- **PLAN §1 allows "≤ 1 non-AI" satellite, and TTWO holds it.** Buying any name below needs post-mortem change (a):
  replace "≤ 1 non-AI" with "AI semis and memory ≤ 25% of the sleeve, at most 2 names". The client decides.
- The circuit breaker fired on 10/22: no buys until the post-mortem is agreed, and not before 11/2.
- No gold names: the vault is ≈ 70% physical gold.
- Chase guard: RSI(14) ≤ 70 and ≤ 20% above the 50-DMA. Proposed (b): stop ≥ 1.5 ATR under the entry.

## Method
- Universe: 52 liquid US large caps and sector ETFs outside AI, semis, AI power and gold.
- Data: Yahoo 1y daily bars to the 10/22 close.
- Measures:
  - % vs the 50- and 200-DMA, with their slopes
  - Wilder RSI(14) and ATR(14) %
  - % off the 52-week high
  - 60-day correlation of daily returns with the SOX, and beta to the S&P
  - **"3shock"**: the summed return on the three chip-crash days 10/14, 10/16 and 10/22 (SOX −14.9%, S&P −3.4%)
  - 3- and 6-month returns

## Finding
**The defensive rotation has already happened.** PG, KO, COST, CME, V, MA, BRK-B, LMT, RSG, WM and TRV all have RSI > 70, most
within 1–7% of their highs. Buying them now is a chase in a different sector, and the chase guard blocks them.

**Shortlist for deep dives** (positive on the chip-crash days, negative SOX correlation, RSI < 70, uptrend):

| Ticker | 10/22 | vs 50d | vs 200d | RSI | ATR% | cSOX | 3shock | 6m |
|---|---|---|---|---|---|---|---|---|
| PM | 201.74 | +4.9 ↑ | +11.7 ↑ | 57.3 | 2.8 | −0.58 | +8.0 | +19.2 |
| RTX | 194.71 | −1.5 ↓ | −0.2 ↑ | 56.6 | 2.3 | −0.28 | +7.2 | +8.6 |
| JNJ | 267.61 | +0.9 ↓ | +9.1 ↑ | 57.2 | 2.4 | −0.50 | +6.8 | +16.0 |
| MRK | 147.24 | +0.5 ↑ | +17.2 ↑ | 52.9 | 3.0 | −0.07 | +2.6 | +28.5 |
| ABBV | 285.19 | +7.4 ↑ | +21.3 ↑ | 64.7 | 2.3 | −0.48 | +4.2 | +41.9 |
| XLV | 181.30 | +6.1 ↑ | +14.8 ↑ | 69.9 | 1.6 | −0.44 | +3.6 | +24.0 |
| XLE | 67.57 | +5.3 ↑ | +16.4 ↑ | 63.1 | 2.0 | −0.24 | +2.3 | +18.6 |
| PGR | 229.62 | +6.5 ↑ | +10.0 ↓ | 66.3 | 2.4 | −0.48 | +1.7 | +11.8 |

**Alternates:** AMGN (RSI 66.6, +20.5% vs the 200-DMA) and VRTX (RSI 61.5).

**Excluded:**
- Downtrends: TMUS, LHX, NFLX, GE, GS, ITA, BSX, MCD, GD.
- Extended (RSI > 70): LLY, UNH, CB, COST, KO, PG, V, MA, BRK-B, CME, LMT.

## Full screen (sorted by 3shock)
```
tkr        last   vs50 50  vs200 200   RSI  ATR%  offHi  cSOX  beta 3shock     3m     6m
LMT      589.91   +9.2 dn   +4.3 up  75.2   2.6  -14.8 -0.35 -0.40  +14.2   +1.3  +11.3
NOC      552.35   +5.6 dn   -6.8 dn  68.2   2.5  -28.6 -0.38 -0.27   +9.4   +1.9   -6.0
PG       165.59  +11.9 up  +11.6 up  74.5   1.8   -1.0 -0.46 -0.31   +9.3  +12.3  +13.6
PM       201.74   +4.9 up  +11.7 up  57.3   2.8   -4.1 -0.58 -0.99   +8.0   +4.5  +19.2
RSG      241.90  +10.0 up  +12.0 up  75.6   1.8   -0.2 -0.65 -0.61   +7.9  +11.5  +13.0
CBOE     327.72  +12.9 up  +12.8 up  69.0   3.4  -11.7 -0.30 -1.03   +7.8  +15.0   +9.2
CME      305.98  +10.6 up   +9.6 up  78.3   2.1   -7.0 -0.41 -0.38   +7.7  +19.8   +7.2
TMUS     158.79   -7.2 dn  -15.7 dn  45.5   3.4  -29.7 -0.38 -0.85   +7.2  -11.8  -18.2
RTX      194.71   -1.5 dn   -0.2 up  56.6   2.3  -14.2 -0.28 -0.20   +7.2   -8.5   +8.6
LHX      254.23   +1.0 dn  -17.1 dn  61.5   2.1  -33.0 -0.47 -0.44   +7.2  -15.3  -23.0
WM       239.10  +10.4 dn   +6.4 dn  78.1   1.8   -3.6 -0.63 -0.69   +7.2   +0.1   +2.7
WMT      121.12  +10.8 up   +2.3 dn  74.4   2.0  -10.4 -0.35 -0.07   +7.1  +10.6   -8.3
PEP      138.83   +3.4 dn   -5.0 dn  68.7   2.0  -19.0 -0.50 -0.46   +7.0   +1.6  -10.8
LLY     1306.69  +10.2 up  +20.5 up  70.7   2.9   -1.1 -0.48 -0.54   +6.9   +9.3  +42.4
JNJ      267.61   +0.9 dn   +9.1 up  57.2   2.4   -4.8 -0.50 -0.43   +6.8   +1.6  +16.0
KO        95.34   +7.1 up  +17.0 up  73.6   1.6   -0.0 -0.59 -0.44   +6.8  +15.9  +25.0
XLP       89.99   +6.7 up   +6.9 up  74.3   1.4   -0.2 -0.63 -0.35   +6.6   +7.0   +7.8
COST    1018.21   +8.5 up   +5.1 up  78.7   1.6   -7.1 -0.47 -0.23   +6.0   +8.9   +0.4
CB       363.95   +6.6 up   +9.5 up  70.5   1.7   -0.5 -0.63 -0.56   +5.7   +1.2   +9.3
UNH      424.98   +9.5 dn  +17.8 up  72.2   2.7   -7.9 -0.25 -0.09   +5.4   +1.0  +19.9
UNP      298.09   +3.7 dn  +11.1 up  71.8   1.9   -5.7 -0.23 -0.21   +5.1   -3.0   +9.9
ICE      163.84   +4.4 up   +6.0 dn  64.3   2.1   -6.9 -0.35 -0.09   +5.1  +12.4   +4.0
AMGN     447.28   +7.3 up  +20.5 up  66.6   2.4   -0.8 -0.13  0.35   +4.9  +18.9  +28.3
GD       350.79   -1.3 dn   -1.1 dn  59.8   1.7  -12.3 -0.30  0.02   +4.6   -9.3  +10.1
CVX      226.68   +8.1 up  +18.5 up  71.5   2.0   -0.9 -0.36 -0.80   +4.5  +16.4  +20.8
COP      145.63   +9.0 up  +21.7 up  71.1   2.3   -1.3 -0.29 -0.86   +4.4  +21.1  +17.1
TRV      405.44   +9.3 up  +24.3 up  77.3   1.9   -0.6 -0.43 -0.28   +4.3   +4.7  +31.9
XOM      178.23   +7.8 up  +16.6 up  70.3   2.1   -1.2 -0.38 -0.97   +4.2  +13.6  +18.4
ABBV     285.19   +7.4 up  +21.3 up  64.7   2.3   -2.1 -0.48 -0.51   +4.2  +10.0  +41.9
TJX      147.38   +7.9 dn   -2.8 dn  70.7   1.8  -13.3 -0.13  0.16   +4.1   -4.4   -6.9
MCD      252.63   +0.9 dn  -11.3 dn  65.9   1.8  -26.1 -0.34 -0.14   +3.8   -4.6  -16.5
BRK-B    546.97   +7.2 up  +10.6 up  81.5   1.2   -0.5 -0.44 -0.22   +3.8  +10.5  +16.2
XLV      181.30   +6.1 up  +14.8 up  69.9   1.6   -0.5 -0.44 -0.05   +3.6  +11.5  +24.0
BSX       46.01   +0.8 dn  -20.8 dn  59.2   2.8  -56.5 -0.13  0.38   +3.2   +4.0  -30.0
SPGI     453.10   +8.5 up   +8.2 dn  74.7   2.2  -13.3 -0.39  0.22   +3.0   +6.3   +9.1
VRTX     535.17   +2.4 up  +12.2 up  61.5   2.5   -4.5 -0.20  0.18   +3.0  +12.1  +23.0
ISRG     443.85  +12.4 up   +1.6 dn  67.9   2.9  -26.5 -0.23  0.48   +3.0  +31.5   -7.3
JPM      336.54   -2.7 dn   +4.4 up  47.6   1.9   -8.2  0.04  0.41   +2.8   -4.7   +8.0
MRK      147.24   +0.5 up  +17.2 up  52.9   3.0   -6.2 -0.07  0.38   +2.6  +12.3  +28.5
ABT      102.51   -2.7 dn   +0.2 dn  50.5   2.8  -22.4 -0.38 -0.19   +2.5   -0.5  +10.8
XLE       67.57   +5.3 up  +16.4 up  63.1   2.0   -1.8 -0.24 -0.56   +2.3  +13.3  +18.6
IHI       54.87   +3.3 dn   +2.0 dn  64.9   1.8  -15.2 -0.34  0.20   +2.3   +9.2   +3.5
HCA      467.31   +8.6 up   +5.1 dn  63.9   2.5  -16.0 -0.24 -0.19   +1.8  +22.3   -1.4
PGR      229.62   +6.5 up  +10.0 dn  66.3   2.4   -4.1 -0.48 -0.35   +1.7   +7.4  +11.8
MA       633.21   +9.1 up  +18.6 up  79.5   1.6   -0.0 -0.25  0.19   +1.6  +17.3  +26.0
V        414.34  +10.1 up  +21.8 up  79.1   1.6   -0.1 -0.31  0.21   +1.1  +16.5  +34.1
XLF       56.65   +0.9 dn   +5.5 dn  63.2   1.3   -3.3 -0.11  0.45   +1.0   +0.6   +9.4
ITA      204.48   -6.9 dn  -11.0 dn  35.6   1.9  -20.3  0.21  0.74   +0.5  -14.8   -6.7
NFLX      67.05  -10.0 dn  -18.6 dn  39.6   3.2  -42.6 -0.37  0.34   +0.4   -4.3  -27.8
GE       293.54   -9.7 dn   -9.2 up  30.2   3.0  -24.5  0.20  0.74   -0.4  -17.0   +4.0
AXP      325.17   +1.7 dn   -0.7 dn  65.3   1.8  -16.1  0.01  0.79   -0.5   -0.3   +2.1
GS       891.30   -7.5 dn   -7.0 dn  41.6   2.8  -22.8  0.55  1.66   -4.1  -16.0   -4.3
```

## Deep dives
Four opus analysts, 10/23, data to the 10/22 close. Files: `research/{JNJ,MRK,PM,RTX,ABBV,XLV,XLE,PGR}.md`. The desk checked
every stop and target anchor against the Yahoo bars.

**Nothing is a buy at today's price.** Every name that passes the rules does so only 5–9% lower, at real support. The
rotation into defensives has already paid the people who were early.

| Rank | Ticker | Verdict | Alert (zone) | Stop | T1 | R/R | Size | Next report |
|---|---|---|---|---|---|---|---|---|
| 1 | **JNJ** | WATCH · Med | **$251.50** ($250.00–251.50) | $240 (1.67 ATR) | $275 | 2.26 | $270 = 1.07 sh, risk ≈ $12 | ≈ late Jan |
| 2 | **PM** | WATCH · Med | **$185.30** ($183.80–185.30) | $175.40 (1.63 ATR) | $205.20 | 2.26 | $250 = 1.35 sh, risk ≈ $12 | ≈ early Feb |
| 3 | **XLV** (instead of JNJ, not with it) | WATCH · Med | **$172.60** ($171.0–172.6) | fill − $4.35 (≈ $167.45, 1.52 ATR) | $181.30 | 2.18 | $258 = 1.5 sh, risk ≈ $6.5 | 33% of the fund reports 10/28–10/30 |
| 4 | **XLE** (conditional) | WATCH · Low | **$63.35** ($62.80–63.35) | $60.70 (1.72 ATR) | $68.78 | 2.39 | $270 = 4.28 sh, risk ≈ $10 | XOM/CVX 10/30 |
| — | MRK | WATCH · Low | provisional $134 | $125 | $153 | 2.5 | re-derive after the 10/29 report | 10/29 |
| — | ABBV | WATCH · Low | $266.3 (not with XLV) | $255 | $289 | 2.19 | 1 sh | 10/30 |
| — | RTX | WATCH · Low | none (resistance every 1–1.8 ATR) | — | — | ≤ 1.1 | — | ≈ late Jan |
| — | PGR | AVOID to 11/18 | only $203.8–204.3, under a falling 200-DMA | — | — | — | — | 11/18 (Oct results) |

**Rules for this list:**
- At most one healthcare line (JNJ or XLV, whichever fires first), PM, and XLE only if Brent is ≥ $100 and the drop is not a
  ceasefire.
- That makes up to 3 new names, ≈ $790 (≈ 23%). With the halved AMD and TTWO (≈ 14%), satellites would be ≈ 37%.
- Every alert needs plan change (a), the post-mortem agreed, and a date of 11/2 or later. Each buy is one fill with its stop
  written first.
- Re-check each zone on the day it fires: zones go stale after two weeks, and ATR moves.

**Caveats:**
- The negative chip link is recent. Over 250 days the SOX correlation of these names is only about −0.2 (ABBV/XLV analyst).
  If chips rebound, this rotation reverses, and that hits exactly the names bought as a hedge.
- These are lower-octane trades: T1 is +8–10%. The cleanest diversifier the account already owns is VOO.

