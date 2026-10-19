# Investment plan — living document

Owner: Wael. Maintained with `/stock-desk`. Edit freely; every change gets a dated line in "Changelog".
Version 3 — 2026-10-03 (trade-around + risk budget, §1b). Numbers reflect the 2026-10-02 statement (sleeve $3,779.85)
and Yahoo daily closes of 2026-10-02.

## 0. What this plan is for
Grow the stock sleeve meaningfully faster than the index **without ever putting the safe layers at
risk**. Safety comes from structure (tiers, caps, a cash reserve that is always deployable in a cash
account), not from predicting the market. There is no "perfect" plan — this one is built so that being
wrong on any single stock costs a bounded, pre-agreed amount.

The sleeve is **≈ 10% of total savings** (client, 2026-10-03: ≈ 70% physical holdings, ≈ 20% cash, ≈ 10% Amana).
The open-risk cap (§1b) keeps "every stop hit on the same day" under 8% of the sleeve ≈ **0.8% of total savings**.

## 1. The tiers

| Tier | What | Target | Profit-taking? | Role |
|---|---|---|---|---|
| **0 · Vault** | Physical holdings (≈ 70% of savings) + cash (≈ 20%), outside Amana | ≈ 90% of savings, not managed here | never | The reason the sleeve can take equity risk at all. Never funds a stock idea |
| **1 · Core** | VOO | **30–35%** of sleeve | **never sold for profit** | Compounding anchor; default home for contributions and for banked profits |
| **2 · Satellites** | Up to 6 individual stocks/ETFs, mostly AI-race layers, ≤1 non-AI + 1 speculative slot | **45–60%**, each 8–15% at entry | **yes — this is the only tier we trade** | Where the excess return is earned and locked in |
| **3 · Reserve** | Cash inside the account | **7.5–25%**, never below 5% | n/a | Buys the dip. In a cash account it is never frozen by open losses |

Current fit (2026-10-16, 09:44 ET): Core 34.7% ✓ · Satellites 44.8% (AMD 14.3, TTWO 14.1, ARM 10.7, MU 5.6) — just under
the band · Reserve **20.5%** ✓. Rebuild satellites only through written levels (one new position at a time, each with a
research entry), never by "redeploying the cash".

## 1b. Trading rules (v3, from 2026-10-03)
Client asked again to loosen buying and selling, citing the vault outside the account. v3 loosens how often and how
freely the satellites are traded. It adds an explicit risk budget so every trade still has a defined, capped loss.

| Rule | v2 (2026-10-01) | **v3** |
|---|---|---|
| Fill budget | ≤ 8 fills a month (sells allowed beyond) | **5–10 buys a month** (client, 2026-10-07): 5 is the normal pace, 10 the hard cap; buys 6–10 are named as such by the desk. Not a quota: zero is fine if nothing is in a zone. Sells never count |
| Reserve floor for discretionary buys | 10% | **7.5%**; contributions refill toward 10%; the index ladder may still go to 5% |
| Selling | ratchet (+25/+40/+75) and catalyst trims only | **+ trade-around (§3b)**: up to ⅓ of any satellite sold in its sell zone, bought back in its buy zone, repeatable |
| Entry size | always in halves | **one fill up to 8% of the sleeve**; halves above that |
| Earnings blackout for buys | 5 trading sessions | **3 trading sessions** before the report |
| Banked profit | 50% Reserve / 50% VOO | **Reserve first until it is back to 15%**, then 50/50 |
| Satellite band | 45–55% | **45–60%** (fits 6 names at ≈ 10%) |
| Re-entry after a stop (§4a) | never the same week (Flag Board) | **never the same session**; then evidence the fall ended + a new stop + R/R ≥ 2:1 |

**New guard rails (the price of the loosening):**
| Guard | Rule |
|---|---|
| Risk per buy | size × distance to stop **≤ 2% of the sleeve** (≈ $76 today) |
| Open stop-risk | all satellite stops hit at once **≤ 8% of the sleeve** (today $268 = 7.1%). Above 8% → no buys until a trim or a stop raise. Sits under the 10% circuit breaker by design |
| Minimum buy | **$50**, so the $1 fee stays ≤ 2% (pre-reset: $20–$100 fills cost 1–5% before the trade started) |
| Tagging | trade-around fills carry `TA` in the `transactions.csv` note so they can be scored on their own |

**Unchanged (strict) — these are what keep trading from being random:** a stop and reward/risk ≥ 2:1 to the first
target (the bottom of the sell zone) written before every buy · buy zones always sit above the stop · hard exit at the
stop and at −15% from cost · no add past 15% of the sleeve, trim at 20% · the ratchet +25/+40/+75 is the *minimum*
selling · circuit breaker at −10% from peak · chase guard: no buy with RSI(14) > 70 or > 20% above the 50-DMA (your
SNDK −$80 and BE −$63 buys were both this shape) · max 6 satellites, one speculative slot ≤ 6% at cost · 2 adds per
holding period, each ≤ 4% (≈ $150), count reset by a profit-banking sale · no trades on FOMC day or data mornings ·
no leverage, shorts, CFDs, options, crypto or SPACs · the vault is never touched.

**Cost:** worst case 10 buys plus sells ≈ $15 a month ≈ 4.8% of the sleeve a year; a realistic 6–8 fills ≈ 2.2%.
**Review 2026-12-31:** score (a) every fill beyond the old 2-a-month pace and (b) every `TA` round trip, net of fees.
If either is negative over the quarter, revert to v2 numbers (§9).

## 2. Satellite rules — entry
- Passes the full research protocol; verdict table filed in `research/`.
- Not >20% above its 50-DMA, RSI(14) < 70, no earnings inside 3 trading sessions (v3).
- Reward/risk ≥ 2:1 to the first target. Invalidation level written down *before* the buy.
- Risk to the stop ≤ 2% of the sleeve; open stop-risk stays ≤ 8% after the fill; buy ≥ $50 (v3).
- **Size**: full position = 10–15% of sleeve. Up to 8% may go in one fill (v3); above 8%, enter in halves: half at the
  level, half on confirmation.
- 6 satellites max. A 7th idea must be better than the weakest holding, which gets sold to fund it.
- Never: shorts, leverage, CFDs, options, crypto, SPACs.
- **One speculative slot** (story / micro-cap, e.g. QUBT): ≤ 6% of the sleeve at cost, stop written first and ≤ 12%
  under entry, one at a time. SPCX/CHZ on the statement are the reason for the cap.

## 3. Satellite rules — profit ratchet (the minimum selling)
Gains are locked in stages, and **banked profit migrates to the safe tiers** so the sleeve gets
structurally safer as it wins.

| Trigger (from avg cost) | Action | Effect |
|---|---|---|
| **+25%** | Stop/alert moves to breakeven | Position can no longer lose money |
| **+40%** | **Sell ⅓** | Recovers ~47% of original cost |
| **+75%** | **Sell another ⅓** | Cost fully recovered (~105%) — remaining ⅓ is house money |
| Remainder | Trail: exit on a **weekly close below the 50-DMA** | Lets the winner run, no ceiling |
| Any satellite **>20%** of sleeve by market value | Trim back to 15% regardless of the ladder | Concentration cap |
| Known binary catalyst (product launch, index inclusion, earnings) | Trim *into* the run-up, not after | Sell the news before the crowd |

Ratchet stages are measured on the shares held at the time (after any trade-around sale).

**Where banked profit goes (v3):** 100% → Reserve until the Reserve is back to 15%; beyond that 50% → Reserve,
50% → VOO. Redeploying it into a satellite is allowed only via the entry rules above, never automatically.

## 3b. Trade-around (v3) — sell strength, rebuy weakness, on written levels
Every satellite carries **two zones**, kept in §6b and `portfolio/levels.csv` (`buy_zone`, `sell_zone`):
- **Sell zone**: the first target / nearest resistance, always above the average cost. In it you *may* sell **up to ⅓**
  of the position: set a price alert at the zone edge, and when it fires sell the ⅓ by hand at market (Amana has no
  partial limit orders; its SL/TP close the whole line). Optional, never forced. Proceeds go to the Reserve.
- **Buy zone**: support above the stop, with R/R ≥ 2:1 to the bottom of the sell zone. In it you may buy back up to
  what was sold. That buy-back counts as an add (the sale already reset the add count because it banked a profit).
- The other ⅔ follow only the ratchet and the stop.
- Below average cost there is no sell zone — the stop rules (§4) apply instead.
- Zones are refreshed at the weekly check from dated closes; a stale zone (> 2 weeks) is not tradable.
`portfolio_report.py` prints `IN BUY ZONE` / `IN SELL ZONE` per line; `/market-move` lists trade-around sells as optional.

## 4. Satellite rules — losses
- **Hard exit at −15% from avg cost** or on a fundamental thesis break, whichever first. No debate,
  no averaging down into a broken thesis. Re-entry later is allowed under §4a.
- **§4a Re-entry after a stop (v3)**: never in the same session the stop fired. After that it needs all three:
  evidence the fall ended (a higher low, or a close back above the broken level — a lower price is not evidence),
  a new stop written first, and R/R ≥ 2:1 — plus every §2 entry rule. Buy zones always sit above the stop.
  *Why (from v1.2, 2026-09-24):* the stop and the dip-buy are opposite conclusions about the same fall — above the
  stop a drop is a discount (thesis holds), at the stop it is information (thesis broke); exactly one can be right at
  any price. Stopping out and re-buying as the price keeps falling keeps the realized loss *and* removes the cap, plus
  a second round of fees — a stop that is undone the moment it fires is theatre; size smaller instead. Worked example:
  BE sold 8/12 at $243.92 (−$63), *not* re-bought that afternoon at $235; re-entered 8/18 at $207.70 with a new size
  and stop → +32% by 9/23. What worked was the pause and the new decision, not the lower price.
- Up to **two adds** per name per holding period, only on a technical pullback with the thesis intact,
  only inside the buy zone above the stop, each ≤ 4% of the sleeve, never past the 15% cap, only while the Reserve stays
  ≥ 7.5% after the fill, never within 3 trading sessions of earnings. The count resets after any sale from the line
  that banks a profit.
- A headline that questions the thesis (e.g. WDC 10/2: Toshiba doubling HDD capacity) **locks adds** until the next
  hard data point (a peer's or the company's earnings) answers it.
- Time stop: a satellite that has not moved in your favor after two earnings cycles is reviewed for replacement.

## 5. Reserve and contributions
- **Monthly $200 → VOO by default** while Core < 35% and the Reserve is ≥ 10%; otherwise → Reserve.
- Floor for discretionary buys (adds, buy-backs, new names): **7.5%** after the fill (v3).
- Reserve deployment ladder (S&P 500 from its high, or a satellite at its 50-DMA with thesis intact):
  - **−4%**: deploy up to **a quarter** of the Reserve, VOO only.
  - **−7%**: deploy up to **half** of the Reserve — into VOO first, then the best-rated satellite.
  - **−15%**: deploy the second half, keeping the 5% floor.
  - Never all at once; never below the 5% floor.
- After a deployment, rebuild the Reserve to 10% from contributions and trade-around proceeds.

## 6. Cadence
- **Weekly (10 min)**: prices vs zones, ladder triggers and stops; any thesis-relevant headline. `/stock-desk check`
  (`portfolio_report.py` shows zone status and open stop-risk).
- **Monthly**: fresh statement PDF → `portfolio/statements/`; full review; contribution decision. `/stock-desk review`.
- **Event-driven**: holdings' earnings, FOMC, index changes, anything that hits an invalidation.
- **Shock (index ±3% day, VIX spike, or a holding gapping)**: `/market-move` — applies §3–§7 mechanically
  via `portfolio/levels.csv` and returns a decision card. No improvising in the moment.

## 6b. Flags — when to call the desk (`/stock-desk`), levels as of 2026-10-16 (09:44 ET)
Live version with news and statuses: **Amana Flag Board** (https://claude.ai/artifact/HjfHpid7GbLvP5VQUSYZmF) — refreshed
2026-10-14 12:45 ET (before the AMD/MU buys). History: **Amana Account Ledger** (https://claude.ai/artifact/88jFMg2Jbrqe3peDpDUDv5), to the 10/14 close.
Check prices **once a week** (Friday after the close). Price alerts are set by the client in the Amana app (suggested
10/16: AMD $630, MU $1,030, ARM $275, TTWO $222 for the sell zones; ANET $178; VOO $688). Between checks, act only if a flag fires — and **ask the desk
before every trade** (client commitment, 2026-10-07; broken 10/8–10/9 and 10/12).
**If the desk cannot be reached: sells at written levels and stop-outs are allowed; buys are not. Stops never move down.**
Averages are the broker's blended costs (statement 2026-10-15). Prices, MAs, RSI, ATR: Yahoo bars 10/16 09:44 ET.
Research: `research/TICKER.md` (one file per ticker, newest entry first).

**Price and ratchet flags (closing prices).** Ladder from avg cost.
| Ticker | Avg cost | ⚠ Exit | +25% → stop to BE | +40% → sell ⅓ | +75% → sell ⅓ | Catalyst trim |
|---|---|---|---|---|---|---|
| AMD | 546.54 | **498** (set it in the app as SL) | 683.17 | 765.16 | 956.44 | 11/3 report: decide 11/2 (sell ⅓ only if in the sell zone) |
| ARM | 255.87 | **220** (broker) · or a court ruling granting Qualcomm the 5-year royalty suspension → sell at market | 319.84 | 358.22 | 447.77 | none (earnings 11/4) |
| MU | 926.20 | **850** (set it in the app as SL) | 1,157.75 | 1,296.68 | 1,620.85 | none (earnings ≈ 12/16) |
| TTWO | 213.11 | **190** (broker, hard) | 266.39 | 298.35 | 372.94 | launch week 11/16–20 > **270** → sell ⅓ |
| VOO | 705.79 | none (core) | never | never | never | none |
| Any satellite | — | — | — | — | — | market value > 20% of sleeve → trim to 15% |
Closed by stops: STX 10/12 759.71 (−$11.81) · BE 10/12 260.20 (+$8.04) · QUBT 10/12 7.00 (−$23.26, lowered stop) · EWY 10/13
163.23 (−$34.93) · WDC 10/13 360.62 (−$50.85) · SNDK 10/15 1,300.39 (−$23.90; 1,350.85 on 10/16 09:44 ET).

**Trade ranges (plan v3).** Buy zone above the stop with R/R ≥ 2:1 to the sell zone; sell zone ≤ ⅓ of the line.
**October buys: 10 of 12** (cap raised 10 → 12 for October only, client OVERRIDE 10/15): WDC, TTWO, STX, EWY, BE, WDC, SNDK,
ARM, **AMD (#9), MU (#10)**. Two left, and the desk gate below applies to both. Sells always allowed.
No buys in the 3 trading sessions before earnings, on 10/28 (FOMC) or on data mornings (10/29 PCE).
| Ticker | Buy zone | Sell zone (≤ ⅓) | Stop | R/R | Max add | Adds used | Buy window | 10/16 price |
|---|---|---|---|---|---|---|---|---|
| VOO | ≈ $688 (SPX −4%) · ≈ $666 (−7%) · ≈ $609 (−15%) | never sold | none | — | ¼ · ½ · rest of Reserve (5% floor) | — | any time | 709.40 |
| AMD | $530–541 (10/15 low 530.1, rising 50-DMA 537.5) — **blocked**: 14.3% of the sleeve, an add passes the 15% cap | **$630–658** → ⅓ = 0.30 sh | 498 | 2.1:1 at 541 | blocked | 0 of 2 | — | 544.97 |
| ARM | $225–233 (9/3 low 225.5, 8/24 low 233.3) — **locked** | **$275–281** → ⅓ = 0.52 sh | 220 | 3.2:1+ | $150 | 0 of 2 | after the 11/4 report and the royalty ruling | 237.62 |
| MU | $880–895 (8/24 887.6, 7/7 891.7 lows) — **locked** until the 10/29 memory prints | **$1,030–1,045** → ⅓ = 0.07 sh · target 2 $1,090–1,109 | 850 | 3.0:1 at 895 | $150 | 0 of 2 | from 11/2 | 902.52 |
| TTWO | $193–198 — **blocked** (2 of 2 adds used) | **$222–228** → ⅓ = 0.78 sh | 190 | — | blocked | 2 of 2 | — | 208.83 |

**10/17: October buying is closed (desk).** The account closed 10/16 $16 above the breaker. No buys until 11/2, after the
memory and hyperscaler prints. **Desk gate for buys #11–12 (judgment, 10/16, superseded):** a new satellite only while the account is **≥ $3,500**, i.e. more than one
10/14-style day (−$72.5 at today's weights) above the $3,402 circuit breaker. At 09:44 ET on 10/16: $3,475 ✘. If every stop
fired today the account would be ≈ $3,349, under the breaker — no new risk on top of that until the gap widens.

**The cash plan ($712 on 10/16) — the only ways it gets spent:**
| When | Trigger | Buy | Amount |
|---|---|---|---|
| Any day | S&P 500 closes ≤ **7,506** (−4% from the record) | VOO | ¼ of cash ≈ $180 |
| Any day | S&P 500 closes ≤ **7,272** (−7%) | VOO first, then the best-rated satellite | up to ½ of cash |
| From **11/2** | AXTI after its 10/29 report, at a fresh level | AXTI | ≈ $190 |
| From **11/2** | MU add in $880–895 after the 10/29 prints (margins hold) | MU add | ≤ $150 |
| From **11/5** | ARM after its 11/4 report, in $225–233, royalty question resolved | ARM add | ≤ $150 |
| Never | "it's on sale", "it seems low", "the market may go up" | — | — |
One stock buy per week at most, each after a desk note (10/15 had two — AMD and MU — so the next is 10/19 at the earliest).
Everything else stays in cash. In a cash account, cash cannot be frozen by losses: it *is* the opportunity.

**Watchlist** (each needs a written stop and R/R ≥ 2:1 at the time; one new position at a time). Prices 10/16 09:44 ET.
| Ticker | Zone | Stop | Target | R/R | Report | Earliest | 10/16 |
|---|---|---|---|---|---|---|---|
| ANET | **≤ $160 only** (zone A failed: closed 176.98 on 10/16, under 178); 200-DMA 162.6, 7/17–7/29 lows 156.8–157.1 | 150 | 181–187 | 2.1:1 at 160 | **11/3 (confirmed)** | not before 11/2 (October buying closed 10/17); re-run 11/4 | 176.98 (10/16 close) |
| AXTI | failed: closed 57.91 on 10/15 after a 53.31 low (under the 54 stop level) | — | — | — | 10/29 (≈ ±20%) | re-derive after the report | 55.71 |
| BE | $210–218 (200-DMA 216, 8/10 low 210) | 195 | 260 | 2.4:1 at 214 | **10/22 (confirmed)** | after the report, with a higher low (§4a: stopped 10/12) | 231.73 |
| INTC | broke its $95–98 zone (10/15 low 90.02) | — | — | — | **10/29 (confirmed)** | re-derive after the report | 93.70 |
| SNDK / WDC / EWY | not while MU is held (one memory name) | — | — | — | 10/22, 10/29 | — | SNDK 1,350.85 |
| RKLB | none — Neutron slipped to 2027 (10/14); falling knife | — | — | — | ≈ 11/10 | re-check after Q3; speculative slot only | 54.35 |
| AAOI | zone failed (Sept double bottom 93.6 broke) | 82 | — | — | ≈ 11/5 | re-derive after the report | — |
| LITE | **none**: support $784–800 pays 0.6–0.9:1 to the $876–894 gap (ATR 8%) | (680) | (876–894) | ✘ | **11/5 (confirmed)** AMC | re-derive after the report (blackout 11/2–11/5); one optical name with AXTI | 858.86 |
| GOOGL | stale (9/24 levels) | — | — | — | ≈ 10/28 | re-research after the report | — |

**Market flags** (S&P 500 record close **7,818.93 on 2026-10-06**; 7,744.55 on 10/16 09:44 ET = −1.0%; VIX 15.9)
- ☐ SPX **−4%** (≈ 7,506) → up to a quarter of the Reserve into VOO.
- ⚠ SPX **−7%** (≈ 7,272) → deploy up to half the Reserve (VOO first). Use `/market-move`.
- ⚠ SPX **−15%** (≈ 6,646) → deploy the second half, keep the 5% floor.
- ⚠ Sleeve equity **< $3,402** (−10% from the $3,779.85 peak of 10/2) → circuit breaker: halve every satellite, no buys,
  post-mortem. **10/16 close: $3,417.92 (−9.6%), $16 away. 10/19 10:28 ET: $3,457.81 (−8.5%), $56 away.** Monday 10/19, 15:45 ET: if the app shows the account below
  $3,402, sell half of each satellite (AMD 0.457 sh, ARM 0.783 sh, MU 0.108 sh, TTWO 1.176 sh); keep VOO; no buys.
- ⚠ Open stop-risk **> 8%** (10/16: $126 = 3.6%) → no buys.
- ⚠ VIX spike or any holding gaps > 8% on news → `/market-move` **before** touching anything.
- Rates and memory: 10-year 5.22%, the Fed hiked in September. Memory stocks are in a 4-month downtrend (SNDK −38%,
  WDC −54%, STX −37%, EWY −25% from June); Morgan Stanley's peak-cycle note 10/13.

**Calendar flags**
| Date | Event | Action |
|---|---|---|
| **2026-10-13** | Qualcomm v. Arm jury deliberations resume · bank earnings | ARM: verdict rule above · **sell SNDK** |
| October | $200 contribution (still not deposited) | → Reserve (Core is at 34.5%) |
| 2026-10-14 | CPI 8:30 ET (≈ +0.6% m/m headline) · BAC, MS, ASML earnings | no trades that morning |
| 2026-10-15 | PPI + retail sales 8:30 ET · Warsh fireside chat | no trades that morning |
| 2026-10-16 | Monthly options expiry · weekly check after the close | no new buy (two on 10/15) |
| **2026-10-20** | **Arm v. Qualcomm bench-trial closing arguments** (10:00 ET); ruling any day after | royalty suspension granted → sell ARM at market |
| 2026-10-22 | **WDC and BE earnings** (both confirmed, AMC) | memory read-across for MU · BE re-entry zone after |
| 2026-10-27 | STX earnings (est) · SK hynix Q3 (after the US close) · last ANET buy day before the FOMC/blackout | memory read-across for MU |
| 2026-10-28 | FOMC · GOOGL earnings (est) | no trades that day |
| 2026-10-29 | PCE 8:30 ET · **SNDK, AXTI, INTC earnings** (AMC, confirmed) · Samsung final Q3 | no trades that morning |
| 2026-11-01 | $200 contribution | Reserve (unless Core < 35% and a rung fires) |
| 2026-11-02 | AMD pre-report decision | hold with the 498 stop, or sell ⅓ if in $630–658 |
| 2026-11-03 | **AMD earnings** (confirmed, AMC; held) · **ANET earnings** (confirmed, AMC) | AMD levels re-derived after · ANET levels re-run 11/4 |
| 2026-11-04 | **ARM earnings** (confirmed, AMC; implied ≈ ±8.8%) | hold with the 220 stop |
| ≈ 2026-11-05 | AAOI earnings (est) · **LITE earnings** (confirmed, AMC) | LITE levels re-derived 11/6+ |
| **2026-11-09** | **TTWO earnings** (confirmed AMC, PR 10/13; expected ≈ ±6.5%) | hold with the 190 stop |
| 2026-11-12 / 11-19 | GTA VI pre-load / **launch** | launch week > 270 → TTWO sell ⅓ |
| 2026-11-27 | China's Ga/Ge export-ban suspension to the US lapses | AXTI kill-switch date |
| 2026-12-19 | TTWO review | exit or re-underwrite |
| 2026-12-31 | v3 review · **v3 or v4 decision (§10)** | score fills, `TA` round trips and the override ledger; run the §10 test and re-run the backtest to 12/31 |
| 2027-01-04 | v4 start if §10 fails | sell half of each satellite, cash to VOO |

**Anything else** (a headline that scares or excites you, an urge to buy something new): write it down, bring it to the
desk **before** trading. A new name needs a research entry and must beat the weakest holding.

## 7. Scorecard (measured from 2026-08-18)
- Satellite sleeve vs VOO, rolling 6 months — the only test of whether the satellite layer earns its risk.
- Max drawdown of the whole sleeve: **target < 15%**. Circuit breaker at −10% from peak (halve every satellite, pause buys, write the post-mortem).
- Profit ratcheted into Tiers 1+3 per year (dollars). Win rate matters less than this number.
- Fills: 5–10 buys a month under v3 (5 normal pace, 10 hard cap); sells uncounted. Trade-around round trips scored separately. Fees tracked; review 2026-12-31.
- **Override ledger** (trades made without the desk, marked against the plan's alternative), 10/16 close:
  WDC re-buy 10/2 −$44.85 · TTWO add 10/2 +$0.65 · STX 10/6 −$11.81 · EWY add 10/8 −$6.83 · EWY stop lowered 172 → 165
  −$30.51 · BE buy-back 10/8 −$7.59 · WDC locked add 10/9 −$8.00 · QUBT stop lowered 8 → 7 −$25.28 · SNDK 10/12 **−$23.90
  (closed)** · ARM re-buy 10/12 **−$43.98** (open) · AMD 10/15 $500 at 11:29 ET before its close trigger, which failed
  (closed 562.23) **−$16.27** (open) · fees on 9 buys −$9 → **net −$227.38 = −6.0% of the peak sleeve in 15 days**, about 63% of the
  $362 fall from the peak.
  Stops, by contrast, saved: ARM 10/8 +$38.52 · STX +$9.09 · BE +$5.02 (vs 10/13 prices); SNDK 10/15 cost −$6.83 (vs 10/16).

## 8. Current application (2026-10-16, 09:44 ET; see journal/2026-10-16-check.md)
| Ticker | Avg cost | Now | P&L | Stop | Weight | Status | Notes |
|---|---|---|---|---|---|---|---|
| VOO | 705.79 | 709.40 | +0.5% | — | 34.7% (core) | hold | never trimmed |
| AMD | 546.54 | 544.97 | −0.3% | 498 | 14.3% | hold, no adds | 10/15 $500 one fill = OVERRIDE; earnings 11/3 |
| TTWO | 213.11 | 208.83 | −2.0% | 190 | 14.1% | hold | earnings 11/9, launch 11/19 |
| ARM | 255.87 | 237.62 | −7.1% | 220 | 10.7% | hold | royalty ruling pending; 10/12 re-buy = OVERRIDE |
| MU | 926.20 | 902.52 | −2.6% | 850 | 5.6% | hold | desk buy 10/15; adds locked until the 10/29 prints |

Reserve **$712.20 (20.5%)** (statement 10/15 book value less open cost). Lines 5 (max 7). Sleeve $3,474.75, −8.1% from peak; the circuit breaker is
at $3,402 ($73 away). Open stop-risk $126 = 3.6%. Broker statement "account value" $3,413.91 is book value (beginning +
realized + fees), not the mark-to-market used for the breaker.

## 9. Override protocol
If Wael wants to do something the plan or the desk objects to: the desk states the objection, the
data, and the rule it breaks — once, plainly. If Wael still wants it, it is executed and logged in
`journal/` as an **OVERRIDE** with the reasoning. Overrides are reviewed quarterly: if they are
beating the rules, the rules change; if not, they stop.

## 10. Year-end decision: v3 or v4 (written 2026-10-18, before the results)
Client decision 2026-10-18: run v3 unchanged to 2026-12-31, then choose between v3 and v4. The desk recommended
switching to v4 now (backtest below); the client chose to test v3 first. The test is fixed here so December's
numbers cannot pick the conclusion.

**v3 continues into 2027 only if both hold at the 2026-12-31 close:**
1. **Zero OVERRIDES from 10/19 to 12/31**: every buy has a desk note, no stop is lowered, no re-buy in the session a stop fired.
2. **The account beats VOO from the 10/16 close**: account value ≥ $3,417.92 plus every deposit after 10/16, each deposit
   put into VOO on its date at VOO's close (start: $3,417.92 in VOO at $701.61).

**Either fails → v4 from Monday 2027-01-04** (first trading day): sell half of each satellite, cash to VOO, then the v4
rules below. A circuit-breaker fire (§7) is market, not behavior: it does not fail test 1 by itself.

**What ten weeks cannot show:** whether the rules have an edge. The 20-year backtest already answered that. Test 1 measures
discipline, and test 2 is mostly noise.

**v4 (if it applies):** VOO 80%, never sold; $200 to VOO on the 1st of each month. Trading pot 20%, at most 3 names, same
entry/stop/ratchet rules, never refilled, swept into VOO above 25% of the account, closed if it loses half its starting
value. One buy without the desk → pot cut to 10%; a second → closed. Review 2027-04-18 against VOO.

**Backtest (2026-10-18, rules followed perfectly, $3,300 + $200/month, $1 a fill, Yahoo adjusted closes).**
Dashboard: https://claude.ai/artifact/65WKhZpiLah9vjcn9vRXmM. Journal: `journal/2026-10-18-v3-vs-v4-study.md`.
| Oct 2006 → Oct 2026 ($51,300 in) | AI list | 2006 hot list | Worst drop | Beat S&P, 300 random lists |
|---|---|---|---|---|
| 100% S&P 500 | $251,182 | — | −55% | — |
| v4 (80/20) | $247,707 | $254,219 | −49 to −52% | 58 / 300 |
| v3 | $230,183 | $239,908 | −46 to −47% | 18 / 300 |
| v3 at the Aug–Oct 2026 fill pace | $225,616 | — | −51% | — |
| 50/50 | $150,572 | $168,953 | −31 to −33% | 0 / 300 |

## Changelog
- 2026-10-19 — statement 10/1–10/18 (`portfolio/statements/amana-statement-2026-10-01_2026-10-18.pdf`): no fills after 10/15; cash $712.20 confirmed (book value $3,513.91); October fees $19, realized −$89.72; the October $200 is still not deposited. 10:28 ET: chips bounce (SOX +2.6%, S&P +0.7%, VIX 18.0); account $3,457.81, $56 above the breaker. No ARM royalty ruling yet. 15:45 ET breaker check unchanged. Flag Board v18 and Account Ledger v13 refreshed. Research: a 10/19 update entry in all 12 `research/TICKER.md` files; verdicts unchanged. ARM bench-trial closing arguments set for 10/20 (calendar).
- 2026-10-18 — v3 vs v4 study (5-year and 20-year backtests, 50/50 added). Desk recommended v4 now; **client chose v3 to
  2026-12-31, then decide** (§10). Year-end test written in advance: zero overrides from 10/19 and the account beats VOO
  from the 10/16 close, or v4 from 2027-01-04. Monday 10/19 15:45 ET circuit-breaker check unchanged.
- 2026-10-17 — 10/16 close: S&P −1.1%, NDX −2.5%, SOX −3.8% (8th straight down day, the longest since 2008), VIX 20.0. Causes: AI-debt and returns fears (CoreWeave −12%), CXMT memory progress, oil. AMD −6.0% (528.75), ARM −6.9% (227.80), MU −5.6% (878.84), TTWO −2.0%, VOO −1.1%. Account $3,417.92 (−9.6% from peak), **$16 above the breaker**; still +$114.66 on $3,303.26 put in. Shock engine: NOISE for the index, no mechanical action, no VOO tranche (S&P −2.0%). Monday rule written: below $3,402 at 15:45 ET → halve every satellite. October buying closed; no buys until 11/2. ANET zone A failed (176.98) → ≤ $160 only. Override ledger −$227.38.
- 2026-10-16 — statement 10/15: SNDK stopped 1,300.39 (−$23.90); **AMD bought $499.96 @546.54 at 11:29 ET** (OVERRIDE: 2.5× the ≈ $200 proposal, 14.6% in one fill > 8%, before its close trigger, which failed at 562.23); **MU bought $199.93 @926.20 at 15:40 ET** on the desk's close trigger (≈ $150 proposed; desk error: no price ceiling, R/R 1.4:1 at the fill, 2:1 needed ≤ 910). Cash $712.11. Buys 10 of 12. Stops AMD 498, MU 850. AMD adds blocked (15% cap); MU adds locked to the 10/29 prints. Desk gate for buys #11–12: account ≥ $3,500. ANET rows merged (A $178–181 / B ≤ $160); AXTI and INTC zones failed on 10/15; ARM jury verdict 10/13 ($2; royalty suspension with the judge). Override ledger −$197.16.
- 2026-10-15 — researched ANET (WATCH → buy $178–181 on a close until 10/28, stop 170) and RKLB (WATCH, no setup after the Neutron delay).
- 2026-10-15 — ANET and LITE added to the research study (`research/ANET.md`, `research/LITE.md`), both **WATCH**. Both are −16% / −22% from the 10/9 highs in an optics/networking unwind with no company news (Broadcom CEO AI-funding remarks 10/12). ANET: 2:1 only at ≤ $160 (stop 150, sell zone 181–187); reports 11/3. LITE: no 2:1 zone at ATR 8.5%; reports 11/5. LITE and AXTI are one InP trade, so only one of them can be held.
- 2026-10-15 — OVERRIDE (client): October buy cap raised 10 → **12** for October only; back to 10 on 11/1. Statement to 10/14: EWY filled 163.23 (−$34.93), WDC 360.62 (−$50.85). SNDK stopped at 1,300 on 10/15 (≈ −$23.95). Cash $1,414. Proposals: AMD in $530–545 (stop 498), MU on a close ≥ $895 after the 858 flush (stop 850).
- 2026-10-14 (pm) — price-alert cloud routine disabled at the client's request; the client sets the alerts manually in the Amana app.
- 2026-10-14 (pm) — MU researched ("might double" on X): WATCH, zone $880–895 from 11/2, stop 830, sell zone 1,030–1,045 (2.1–3.0:1). A double = $2.09T = 10.5× FY27 EPS. One memory name: MU replaces SNDK if SNDK is sold on 10/28. Price-alert routine created (cloud, 15:45 ET, 10/15–10/27): AXTI ≥ 62, AMD 530–545, SPX ≤ 7,506.
- 2026-10-14 (pm) — client: "missing out on the dips" in BE, ARM, SNDK, AMD, INTC. None is at a level (all report 10/22–11/4; ARM/SNDK adds R/R 1.5 and 1.4). One October exception through the desk: AXTI (in its zone, 2.7:1) or AMD ($530–545). New watch zones: BE $210–218 / 195, INTC $95–98 / 89, AMD $530–545 / 498. Confirmed dates: BE 10/22, INTC 10/29, AMD 11/3. SNDK stop 1,300 (client). Flag Board and Account Ledger artifacts refreshed.
- 2026-10-14 — client kept SNDK and asked whether it is a buy "on sale" with $1,239 cash: no add (R/R 1.2:1; a 2:1 add sits inside the stop's noise). SNDK held only with SL 1,310 and a 10/28 sell rule. Added the cash plan to §6b: VOO ladder any day; stock buys from 11/2 after the reports. October memory dip-buys scored at −$91.87.
- 2026-10-13 — statement to 10/12 + 10/13 stops: STX, BE, QUBT stopped 10/12; EWY and WDC gapped under their stops at the 10/13 open (≈ 163.18 / ≈ 359.01, to confirm). Two buys without the desk on 10/12 (OVERRIDES): SNDK with no stop, 17 min after STX's stop; ARM $400 below its 10/8 stop with no higher low. Research refreshed for ARM, SNDK, TTWO, VOO: SNDK EXIT, ARM HOLD (Qualcomm verdict rule), TTWO HOLD, VOO HOLD. October buying closed at 8. §6b: without the desk, sells/stops only. Dates fixed: WDC 10/22, TTWO 11/9, SNDK 10/29 (all confirmed). Research files merged to one per ticker (`research/TICKER.md`). Override ledger −$154.14.
- 2026-10-10 — 10/9 statement: ARM stopped out 10/8 @279.88 (+$27.31; saved ≈ $18 vs the 10/9 close). Three buys without the desk, all inside written zones but each breaking a rule (OVERRIDES): EWY $200 (> $150 max, past the 15% cap), BE $250 TA buy-back (> $100 max; Reserve 3.6% after), WDC $102 (adds locked). EWY broker stop lowered 172 → 165 (§4). Reserve $30 = 0.8%. QUBT still open (exit called 3×). WDC earnings date moved from 11/5 to ≈ 10/22–10/29 (unconfirmed); TTWO 11/5–11/9 unconfirmed. Override ledger added to §7 (net −$15.43 at 10/9 closes). §6b: "if the desk cannot be reached, these rules are the desk". October buying closed at 6.
- 2026-10-09 — AXTI and AAOI researched (asked before trading). Both WATCH: R/R 1.0:1 at 10/9 prices. AXTI first (buy zone $62–63.50, stop 54, sell zone 84–88), AAOI second ($94–96.50, stop 82, sell zone 128–131). Both need a free satellite slot (QUBT sold, then STX after its 10/27 report) and the Reserve ≥ 7.5%. Calendar: AXTI 10/29, AAOI ≈ 11/5, China Ga/Ge truce lapses 11/27. See `journal/2026-10-09-axti-aaoi.md`.
- 2026-10-07 — 10/6 statement: BE half sold @295.02 (+$41.59); STX bought @807.43 (OVERRIDE: 7th satellite, Reserve 5.8% < 7.5%); QUBT broker stop lowered 8 → 7 (OVERRIDE; exit called); stops raised ARM 280, BE 260, TTWO 190. S&P record re-pinned 7,798.99 → 7,818.93 (10/6); index ladder 7,506 / 7,272 / 6,646. Client committed to ask the desk before every trade.
- 2026-10-07 — client set the monthly buy range to **5–10**: 5 is the normal pace, 10 stays the hard cap, no minimum. Buys past the 5th are flagged in each recommendation. Sells still uncounted.
- 2026-10-03 v3 — client asked to loosen buying and selling again (sleeve ≈ 10% of savings; ≈ 70% physical, ≈ 20% cash outside). Loosened: buys ≤ 10/month and sells uncounted (was 8 fills), Reserve floor 10% → 7.5%, trade-around ⅓ between written buy/sell zones (§3b), one-fill entries up to 8%, earnings blackout 5 → 3 sessions, banked profit refills the Reserve to 15% first, satellite band 45–60%, §4a re-entry wait one week → next session (moved from the Flag Board into the plan). Added: risk per buy ≤ 2%, open stop-risk ≤ 8%, $50 minimum buy, `TA` tagging, headline add-lock. Kept: stops + R/R ≥ 2:1, chase guard, 15/20% name caps, ratchet, circuit breaker, 6 satellites, spec slot, 2 adds, no leverage/shorts/options/CFDs/crypto. Review 2026-12-31.
- 2026-10-03 — 10/2 statement: WDC stopped out at 418.20 (−$21.91) and re-bought 0.986 sh @404.48 (stop 360); TTWO add 0.497 sh @202.40; ARM stop 250 → 260; +$100 referral; Reserve 5.3%. WDC re-entry and TTWO add logged as OVERRIDES. Earnings dates corrected: TTWO 11/9, WDC 11/5.
- 2026-10-01 v2 — client asked to trade more (vault outside the account is the safety layer). Loosened: fills 2 → 8/month, Reserve floor 15% → 10%, satellites 5 → 6, one speculative slot (≤ 6% at cost), 2 adds per name (reset after profit-banking sale), earnings blackout 10 → 5 trading days, VOO −4% rung. Every holding always carries a dip zone. Kept: stops + R/R ≥ 2:1 first, 15% name cap, ladder, circuit breaker, no leverage/shorts/options/CFDs/crypto. Review 2026-12-31. QUBT no longer a forced sale.
- 2026-10-01 v1.2 — 9/29 statement review: logged 11 fills (9/15–9/29); Reserve 8.7% and 6 satellites breach the plan → sell QUBT, Oct $200 to Reserve, buy freeze until ≥ 15%, one dip fill in October. New dip zones (ARM 262–268, EWY 176–178, WDC 410–420 with stop 395), BE pre-earnings trim > 299, GOOGL 315–328 / INTC 100–105 watch zones. Overrides logged: WDC 6th satellite, BE double average-down.
- 2026-09-24 — (back-filled from the pre-v2 copy) weekly check vs the 9/23 statement: SPX high corrected 7,765 → 7,798.99 (8/13 ATH); EWY stop set 172, QUBT stop raised to 8.00 (above cost); BE securities class action filed 9/22; GOOGL researched → WATCH, not bought (below 50-DMA, R/R 1.33:1); broker TPs flagged as full-line exits that pre-empt the ⅓ ladder. Added §4a (stop vs dip-buy). See `journal/2026-09-24-check-and-googl.md`, `research/GOOGL.md`.
- 2026-09-22 — (back-filled) 9/21 statement review: AMD closed +27.1%, ARM trimmed ~40% at +25.9%, TTWO add 9/15 against the 9/9 decision, QUBT opened 9/15 against §2 (OVERRIDE logged). Peak $3,670.02. See `journal/2026-09-22-review.md`, `journal/2026-09-22-qubt-override.md`.
- 2026-09-09 — §6b: added per-name trim ladder table.
- 2026-09-09 — §6b: added per-name dip-buy zones (client asked why only exits were listed).
- 2026-09-09 — TTWO: client requested $400 now + hold through launch; challenged per §9; client then decided NOT to add at all. Existing position held through launch to 12/19 (⅓ trim in launch week if >$271). Stop $195 → $185. Added §6b flag list.
- 2026-09-09 v1 — initial plan after the cash-account switch and first review.
- 2026-09-09 v1.1 — added `/market-move` shock playbook; per-name levels moved to `portfolio/levels.csv`.
