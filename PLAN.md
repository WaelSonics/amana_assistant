# Investment plan — v6 (adopted 2026-10-29)

Owner: Wael. Maintained with `/stock-desk`. Every change gets a dated line in "Changelog".
**v6 replaces every v3 rule.** v3 and its full history: `archive/PLAN-v3-2026-10-29.md`.
Evidence: `journal/2026-10-29-dip-rule-test.md`. Decision: `journal/2026-10-29-v6-switch.md`.

## 0. The idea in four lines
1. **VOO is 35% of the account and is never sold.** The physical savings outside Amana are the safe base. This account is
   for growth.
2. **Buy only one kind of dip:** a ≥ 15% drop in a stock that is still in an uptrend. Each buy is $400 at the next open, after
   a 5-line study.
3. **Every trade carries a −25% stop and a +25% take-profit, set in the app at the fill.** After 30 sessions, sell if neither
   has hit.
4. **The eight rules in §4 are the fruits of October.** Each one has a price tag. They are not negotiable trade by trade.

## 1. Structure
| Part | Rule |
|---|---|
| **VOO (core)** | 35% of the account, never sold, no stop. The monthly $200 goes to VOO while it is under 35%; otherwise it goes to cash |
| **Dip book** | up to **5 trades of $400** each (client, 10/29). A buy happens only if cash stays **≥ $150** after it |
| **Legacy lines** | AMD and TTWO, from v3. They keep their stops, get a +25% take-profit and no adds. They do not use dip slots |
| **Cash** | whatever is left, never below $150 |

At today's cash ($1,239.59) only **2 dip trades fit** ($800 → $439.59 left). Slots 3–5 open as the legacy lines exit, as
dip trades close, and as contributions arrive.

## 2. The only way in: the dip rule
1. **Signal on a daily close.** All three must hold:
   - the close is **≥ 15% under the highest close of the last 20 sessions**;
   - the close is **above the 200-DMA**;
   - the **200-DMA is higher than it was 20 sessions ago**.

   `levels.py TICKER …` prints the line "Dip rule (v6)". During the session the signal is provisional.
2. **The study, before the buy** (template in `references/output-templates.md`), saved at the top of `research/TICKER.md`.
   It is the desk note, 5 lines:
   - what the company is;
   - why it fell;
   - the next earnings date;
   - what would make it a sell whatever the price;
   - the signal line.
3. **Buy $400 at the next open, at market.** Then set the **SL at fill −25% and the TP at fill +25%** in the app straight away.
- **Universe:** the watchlist (§6), plus any name the client brings with a study. No story stocks: no revenue, or a market cap
  under $5B.
- **If more names signal than there are free slots or cash:** the strongest trend goes first (the highest close relative to
  its 200-DMA).

## 3. The only ways out
- **The SL (−25%) or the TP (+25%) fires in the app.** Each closes the whole line.
- **Time exit:** at the close of the **30th session** after the buy, if neither has fired. The desk writes the date in
  `portfolio/levels.csv` (`exit_by`).
- **Thesis break:** the "sell whatever the price" event named in the study (guidance withdrawn, fraud, a lost key customer).
  Sell at the next open.

## 4. The eight rules: fruits of October (no exceptions, no "just this once")
| # | Rule | What it cost when broken |
|---|---|---|
| 1 | **Never lower a stop**, and never remove one | EWY 172 → 165 and QUBT 8 → 7: −$55.79 |
| 2 | **Never re-buy a name in the session its stop fired.** It needs a fresh signal on a later close | WDC 10/2 and SNDK 10/12: −$68.75 |
| 3 | **Never hold a line without its SL and TP in the app** | SNDK 10/12 had no stop |
| 4 | **Never buy a dip without a signal.** Below the 200-DMA, or "it's down", is not a signal | In the bust test, the instinct lost 3–5× more than the rule |
| 5 | **At most 2 open lines per theme** (§6; legacy lines count) | Memory in October: WDC, STX, SNDK, EWY and MU bought, ≈ −$160 |
| 6 | **Never more than $400 in one buy, never a 6th dip slot, never cash under $150** | AMD $500 in one fill; Reserve at 0.8% on 10/9 |
| 7 | **No buy in the 3 sessions before the name's earnings**, nor on FOMC days | Untested either way; kept because it is cheap |
| 8 | **Every buy has a study first.** When the desk can't be reached: sells and stops only | October's overrides were all buys without the desk |

## 5. Brakes
- **Dip brake:** closed dip trades net **−$400** (four full stops) → new buys pause until a desk review.
- **Account brake:** a close **under $3,212.87**, which is −15% from the $3,779.85 peak of 10/2 → new buys pause for two weeks.
  Nothing is force-sold, and VOO is never sold.
- **Neither brake is ever reset or moved to make room.** That would be rule 1 at the account level.

## 6. Watchlist and themes
| Theme | Names |
|---|---|
| Compute and chips | AMD (legacy), NVDA, ARM, INTC, TSM |
| Memory and storage | MU, SNDK, WDC, STX, EWY |
| Networking and optical | ANET, LITE, AAOI, AXTI |
| AI power | BE |
| Platforms | GOOGL |
| Space | RKLB |
| Games | TTWO (legacy) |
| Healthcare | JNJ, ABBV, MRK, XLV |
| Each its own theme | PM (staples), XLE (energy), RTX (defense), PGR (insurance) |

## 7. Cadence
- **After each close:** the desk runs `levels.py` on the watchlist and writes a study for each signal. The client buys at the
  next open and sends the fill.
- **The desk logs every fill:**
  - `portfolio/transactions.csv`, with `DIP` in the note for dip trades;
  - `portfolio/holdings.csv`;
  - `portfolio/levels.csv` (stop, tp, exit_by).
- **Weekly:** `levels.py --report`, which shows the slots, cash floor, brakes, theme count and time exits.
- **Monthly:** the dip-book P&L against VOO from 11/2.
- **Review on 2027-03-31:** keep, resize, or put everything into VOO.

## 8. Positions at the switch (Yahoo, 10/29 09:44 ET)
| Line | Shares | Avg | Now | SL (in the app) | TP (set it now) | Note |
|---|---|---|---|---|---|---|
| VOO | 1.69987894 | 705.79 | 706.54 | none | none | core, 35.1% |
| AMD (legacy) | 0.91477917 | 546.54 | 570.49 | 498 | **683.18** | reports 11/3 after the close; the stop and the TP decide |
| TTWO (legacy) | 2.35163202 | 213.11 | 193.44 | 190 | **266.39** | 1.8% above the stop; GTA VI 11/19; an official delay → exit |
| Cash | | | $1,239.59 | | | 2 dip slots fundable |

Account $3,417.39, $204.52 above the account brake. **No trades until Mon 11/2** (client commitment of 10/27). The first scan
is the **10/30 close**.

## Changelog
- 2026-10-29 — **v6 adopted** (client): VOO 35%, the dip rule as the only entry, 5 slots × $400 (client's numbers; the desk
  drafted 4 × $200), SL −25% / TP +25% / 30 sessions, the eight October rules, and brakes at −$400 net on dip trades and
  $3,212.87 on the account. Dropped from v3:
  - the R/R gate and the 1.5-ATR minimum stop (they blocked all 7 post-reset winners);
  - zones, trade-around and the ratchet;
  - buy caps and tier bands;
  - §4a;
  - the −10% breaker and its halving;
  - the §10/§11 year-end test.

  The test at 5 × $400: +$2,437 in the 2024–26 AI-winners window and −$460 in the 2021–23 bust window (both hindsight).
  VOO with $800: +$262 and +$64. Full v3 history in `archive/PLAN-v3-2026-10-29.md`.
