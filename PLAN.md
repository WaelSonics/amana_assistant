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

Current fit (2026-10-02 closes): Core 31.8% ✓ · Satellites 62.9% (TTWO 12.6, EWY 11.9, BE 11.4, WDC 10.8, ARM 10.7,
QUBT 5.5) ✘ above 60% · Reserve **5.3% ✘ below the 7.5% floor**. Six satellites = the max.
Fix: sell-zone trims (EWY is at its zone) and the October $200 → Reserve. No discretionary buys until the Reserve ≥ 7.5%.

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

## 6b. Flags — when to call the desk (`/stock-desk`), levels as of 2026-10-06 closes
Live version with news and statuses: **Amana Flag Board** (https://claude.ai/artifact/HjfHpid7GbLvP5VQUSYZmF).
Check prices **once a week** (Friday after the close). Between checks, act only if a flag fires — and **ask the desk
before every trade** (client commitment, 2026-10-07).
Averages are the broker's blended costs from the 2026-10-06 statement. MAs/RSI are 10/7 (stockanalysis.com);
10/7 prices are early-session. Earnings dates: stockanalysis/Yahoo, fetched 2026-10-07 ("est" = not confirmed).

**Price and ratchet flags (closing prices).** Ladder from avg cost.
| Ticker | Avg cost | ⚠ Exit (close below) | +25% → stop to BE | +40% → sell ⅓ | +75% → sell ⅓ | Catalyst trim |
|---|---|---|---|---|---|---|
| EWY | 171.04 | **172** | 213.80 | 239.46 | 299.32 | none |
| ARM | 259.17 | **280** (client raised, ~10/6) | 323.97 | 362.84 | 453.55 | none (earnings 11/4) |
| BE | 239.26 | **260** (client raised) | 299.07 | 334.96 | 418.70 | **> 299 before 10/27 earnings → sell ⅓ of what is left** |
| TTWO | 213.11 | **190** (broker, hard) | 266.39 | 298.35 | 372.94 | launch week 11/16–20 > **270** → sell ⅓ |
| WDC | 404.48 | **360** (hard exit −15% = 343.81) | 505.60 | 566.27 | 707.84 | none (earnings 11/5) |
| STX | 807.43 | **760** | 1,009.29 | 1,130.40 | 1,413.00 | none (earnings 10/27); broker TP 1000 sells all |
| QUBT | 7.92 | **8.00 → EXIT CALLED** (7.86 on 10/6); broker stop was lowered to 7 | — | — | — | — |
| VOO | 705.79 | none (core) | never | never | never | none |
| Any satellite | — | — | — | — | — | market value > 20% of sleeve → trim to 15% |

**Trade ranges (plan v3).** Buy zone above the stop with R/R ≥ 2:1 to the sell zone; sell zone ≤ ⅓ of the line.
All buys are locked while the Reserve is below 7.5% (today 5.8%). Each add ≤ $150 and never past 15% of the sleeve.
No buys in the 3 trading sessions before earnings or on 10/28 (FOMC). 5–10 buys a month (5 normal, 10 cap): October 3 so far.
| Ticker | Buy zone | Sell zone (≤ ⅓) | Stop | R/R | Max add | Adds used | Buy window | 10/6 close |
|---|---|---|---|---|---|---|---|---|
| VOO | ≈ $688 (SPX −4%) · ≈ $666 (−7%) · ≈ $609 (−15%) | never sold | none | — | ¼ · ½ · rest of Reserve (5% floor) | — | any time | 716.20 |
| ARM | **$285–292** (9/28 close 283.3, above the 280 stop) | **$325–337** (under the 9/23 high 336.98) | 280 | 4.3:1 | $100 (stop < 1 ATR under) | 1 of 2 | until 10/29 | 302.56 |
| EWY | **$176–180** (9/28 low 180.4, 9/18 low 178.2) | **$192–196** (9/22 high 193.0, 10/2 high 192.9) | 172 | 2.3:1 | $150 | 0 of 2 | after Samsung's prelim (10/8 KST) | 186.40 |
| BE | **$265–272** (9/18 close 265.6) | **$299–305** (+25% mark, 9/29 high 302.35) | 260 | 3.6:1 | $100 | 0 of 2 (reset 10/6) | until 10/21 | 295.78 |
| TTWO | **$193–198** | **$222–228** (50/200-DMA ≈ 224, 9/14 high 224.3) | 190 | 4.8:1 | **blocked** — 2 of 2 used | 2 of 2 | until 11/3 | 202.53 |
| WDC | **$384–396** (10/2 low 396.6) | **$455–465** (gap fill 462.56; 50-DMA 461.5) | 360 | 2.2:1 | $150 | 0 of 2 | **locked until STX reports 10/27**, then 10/29–10/30 | 411.04 |
| STX | **$770–785** (9/17 low 783, 10/7 low 782) | **$845–860** (10/2 close 849; 50-DMA 856) | 760 | 3.9:1 | $100 | 0 of 2 | **locked until its own 10/27 report**, then 10/29–10/30 | 805.63 |
| QUBT | none — exit called | none | 8.00 | — | blocked | — | — | 7.86 |
| GOOGL (watch) | $315–328 | — | 305 | 2.6:1 to 364 | needs a free slot | — | after ~10/28 earnings | 347.68 |
| INTC (watch) | $100–105 | — | 94 | 2.9:1 to 127 | needs a free slot | — | after ~10/22 earnings | 112.50 |

**Market flags** (S&P 500 record close **7,818.93 on 2026-10-06**; 7,775 early 10/7)
- ☐ SPX **−4%** (≈ 7,506) → up to a quarter of the Reserve into VOO.
- ⚠ SPX **−7%** (≈ 7,272) → deploy up to half the Reserve (VOO first). Use `/market-move`.
- ⚠ SPX **−15%** (≈ 6,646) → deploy the second half, keep the 5% floor.
- ⚠ Sleeve equity **< $3,402** (−10% from the $3,779.85 peak of 10/2) → circuit breaker.
- ⚠ Open stop-risk **> 8%** of the sleeve (today 4.8%) → no buys until a trim or a stop raise.
- ⚠ VIX spike or any holding gaps > 8% on news → `/market-move` **before** touching anything (WDC and STX both −10% on 10/2, STX −9% again 10/6).
- Rates: US 10-year above 5.3% (10/7), highest since 2002. Long-duration growth is the exposed end of this sleeve.

**Calendar flags**
| Date | Event | Action |
|---|---|---|
| October | $200 contribution (not on the 10/6 statement) | → Reserve (5.8% < 10%) |
| 2026-10-08 | Samsung Q3 prelim (LSEG ≈ ₩106.1T OP, estimate cut 7.7% since Aug) | EWY buy zone opens after the print |
| 2026-10-14 | CPI 8:30 ET | no trades that morning |
| 2026-10-21 | last day for BE adds | |
| ~2026-10-22 | INTC earnings (est) | watch zone after |
| 2026-10-27 | **STX earnings** (confirmed) · BE earnings (est) | decides the WDC and STX add locks; BE ⅓ trim beforehand if > 299 |
| 2026-10-28 | FOMC · GOOGL earnings (est) | no trades that day |
| 2026-10-29 | PCE 8:30 ET · last day for ARM adds | no trades that morning |
| 2026-10-30 | last day for WDC / STX adds (if Seagate held up) | |
| 2026-11-01 | $200 contribution | VOO if Reserve ≥ 10%, else Reserve |
| 2026-11-04 / 11-05 | ARM / WDC earnings | hold with stops |
| 2026-11-09 | TTWO earnings (confirmed 10/3; one source says ~11/6) | hold; gap risk accepted |
| 2026-11-16→20 | GTA VI launch week (11/19) | TTWO > 270 → sell ⅓ |
| 2026-12-19 | TTWO review | exit or re-underwrite |
| 2026-12-31 | v3 review | score active fills and `TA` round trips net of fees |

**Anything else** (a headline that scares or excites you, an urge to buy something new): write it down, bring it to the
desk **before** trading. A new name needs a filed research note and must beat the weakest holding.

## 7. Scorecard (measured from 2026-08-18)
- Satellite sleeve vs VOO, rolling 6 months — the only test of whether the satellite layer earns its risk.
- Max drawdown of the whole sleeve: **target < 15%**. Circuit breaker at −10% from peak (halve every satellite, pause buys, write the post-mortem).
- Profit ratcheted into Tiers 1+3 per year (dollars). Win rate matters less than this number.
- Fills: 5–10 buys a month under v3 (5 normal pace, 10 hard cap); sells uncounted. Trade-around round trips scored separately. Fees tracked; review 2026-12-31.

## 8. Current application (2026-10-06 closes; see journal/2026-10-07-review.md)
| Ticker | Avg cost | Now | P&L | Stop | Zone status | Notes |
|---|---|---|---|---|---|---|
| VOO | 705.79 | 716.20 | +1.5% | — | core (32.3%) | never trimmed |
| TTWO | 213.11 | 202.53 | −5.0% | 190 | between zones | adds 2/2 used; hold to launch; review 12/19 |
| EWY | 171.04 | 186.40 | +9.0% | 172 | between zones | Samsung prelim 10/8; 181 early 10/7 |
| WDC | 404.48 | 411.04 | +1.6% | 360 | above the buy zone; adds locked | 399.5 early 10/7, under the 200-DMA |
| ARM | 259.17 | 302.56 | +16.7% | 280 | between zones | stop raised by client; 293.5 early 10/7 |
| BE | 239.26 | 295.78 | +23.6% | 260 | 1% under the sell zone | half sold 10/6 @295.02 |
| STX | 807.43 | 805.63 | −0.2% | 760 | between zones; adds locked | 10/6 buy = OVERRIDE (7th satellite, Reserve below floor) |
| QUBT | 7.92 | 7.86 | −0.8% | 8.00 (plan) / 7 (broker) | **EXIT** | under the plan stop; broker stop lowered = OVERRIDE |

Reserve $217 (5.8%) — below the 7.5% floor, and 8 lines > 7 max. Fix: sell QUBT (≈ +$190 → ≈ 11%), October $200 →
Reserve (≈ 16%). Open stop-risk $181 = 4.8% of $3,770.

## 9. Override protocol
If Wael wants to do something the plan or the desk objects to: the desk states the objection, the
data, and the rule it breaks — once, plainly. If Wael still wants it, it is executed and logged in
`journal/` as an **OVERRIDE** with the reasoning. Overrides are reviewed quarterly: if they are
beating the rules, the rules change; if not, they stop.

## Changelog
- 2026-10-07 — 10/6 statement: BE half sold @295.02 (+$41.59); STX bought @807.43 (OVERRIDE: 7th satellite, Reserve 5.8% < 7.5%); QUBT broker stop lowered 8 → 7 (OVERRIDE; exit called); stops raised ARM 280, BE 260, TTWO 190. S&P record re-pinned 7,798.99 → 7,818.93 (10/6); index ladder 7,506 / 7,272 / 6,646. Client committed to ask the desk before every trade.
- 2026-10-07 — client set the monthly buy range to **5–10**: 5 is the normal pace, 10 stays the hard cap, no minimum. Buys past the 5th are flagged in each recommendation. Sells still uncounted.
- 2026-10-03 v3 — client asked to loosen buying and selling again (sleeve ≈ 10% of savings; ≈ 70% physical, ≈ 20% cash outside). Loosened: buys ≤ 10/month and sells uncounted (was 8 fills), Reserve floor 10% → 7.5%, trade-around ⅓ between written buy/sell zones (§3b), one-fill entries up to 8%, earnings blackout 5 → 3 sessions, banked profit refills the Reserve to 15% first, satellite band 45–60%, §4a re-entry wait one week → next session (moved from the Flag Board into the plan). Added: risk per buy ≤ 2%, open stop-risk ≤ 8%, $50 minimum buy, `TA` tagging, headline add-lock. Kept: stops + R/R ≥ 2:1, chase guard, 15/20% name caps, ratchet, circuit breaker, 6 satellites, spec slot, 2 adds, no leverage/shorts/options/CFDs/crypto. Review 2026-12-31.
- 2026-10-03 — 10/2 statement: WDC stopped out at 418.20 (−$21.91) and re-bought 0.986 sh @404.48 (stop 360); TTWO add 0.497 sh @202.40; ARM stop 250 → 260; +$100 referral; Reserve 5.3%. WDC re-entry and TTWO add logged as OVERRIDES. Earnings dates corrected: TTWO 11/9, WDC 11/5.
- 2026-10-01 v2 — client asked to trade more (vault outside the account is the safety layer). Loosened: fills 2 → 8/month, Reserve floor 15% → 10%, satellites 5 → 6, one speculative slot (≤ 6% at cost), 2 adds per name (reset after profit-banking sale), earnings blackout 10 → 5 trading days, VOO −4% rung. Every holding always carries a dip zone. Kept: stops + R/R ≥ 2:1 first, 15% name cap, ladder, circuit breaker, no leverage/shorts/options/CFDs/crypto. Review 2026-12-31. QUBT no longer a forced sale.
- 2026-10-01 v1.2 — 9/29 statement review: logged 11 fills (9/15–9/29); Reserve 8.7% and 6 satellites breach the plan → sell QUBT, Oct $200 to Reserve, buy freeze until ≥ 15%, one dip fill in October. New dip zones (ARM 262–268, EWY 176–178, WDC 410–420 with stop 395), BE pre-earnings trim > 299, GOOGL 315–328 / INTC 100–105 watch zones. Overrides logged: WDC 6th satellite, BE double average-down.
- 2026-09-24 — (back-filled from the pre-v2 copy) weekly check vs the 9/23 statement: SPX high corrected 7,765 → 7,798.99 (8/13 ATH); EWY stop set 172, QUBT stop raised to 8.00 (above cost); BE securities class action filed 9/22; GOOGL researched → WATCH, not bought (below 50-DMA, R/R 1.33:1); broker TPs flagged as full-line exits that pre-empt the ⅓ ladder. Added §4a (stop vs dip-buy). See `journal/2026-09-24-check-and-googl.md`, `research/GOOGL-2026-09-24.md`.
- 2026-09-22 — (back-filled) 9/21 statement review: AMD closed +27.1%, ARM trimmed ~40% at +25.9%, TTWO add 9/15 against the 9/9 decision, QUBT opened 9/15 against §2 (OVERRIDE logged). Peak $3,670.02. See `journal/2026-09-22-review.md`, `journal/2026-09-22-qubt-override.md`.
- 2026-09-09 — §6b: added per-name trim ladder table.
- 2026-09-09 — §6b: added per-name dip-buy zones (client asked why only exits were listed).
- 2026-09-09 — TTWO: client requested $400 now + hold through launch; challenged per §9; client then decided NOT to add at all. Existing position held through launch to 12/19 (⅓ trim in launch week if >$271). Stop $195 → $185. Added §6b flag list.
- 2026-09-09 v1 — initial plan after the cash-account switch and first review.
- 2026-09-09 v1.1 — added `/market-move` shock playbook; per-name levels moved to `portfolio/levels.csv`.
