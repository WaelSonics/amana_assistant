# Investment plan — living document

Owner: Wael. Maintained with `/stock-desk`. Edit freely; every change gets a dated line in "Changelog".
Version 2 — 2026-10-01 (active-trading rules, §1b). Numbers reflect the 2026-09-29 statement (sleeve $3,666; 9/30 closes ≈ $3,635).

## 0. What this plan is for
Grow the stock sleeve meaningfully faster than the index **without ever putting the safe layers at
risk**. Safety comes from structure (tiers, caps, a cash reserve that is always deployable in a cash
account), not from predicting the market. There is no "perfect" plan — this one is built so that being
wrong on any single stock costs a bounded, pre-agreed amount.

## 1. The tiers

| Tier | What | Target | Profit-taking? | Role |
|---|---|---|---|---|
| **0 · Vault** | Physical gold + cash savings (outside Amana, ~87% of monthly savings) | not managed here | never | The reason the sleeve can take equity risk at all |
| **1 · Core** | VOO | **30–35%** of sleeve | **never sold for profit** | Compounding anchor; default home for contributions and for banked profits |
| **2 · Satellites** | 3–5 individual stocks/ETFs, mostly AI-race layers, ≤1 non-AI | **45–55%**, each 8–15% at entry | **yes — this is the only tier we trade** | Where the excess return is earned and locked in |
| **3 · Reserve** | Cash inside the account | **10–25%**, never below 5% | n/a | Buys the dip. In a cash account it is never frozen by open losses |

Current fit (2026-09-30 closes): Core 32.8% · Satellites 58% (EWY 12, BE 11, TTWO 11, ARM 11, WDC 8, QUBT 6) · Reserve **8.8% ✘ below the 10% floor**. Six satellites = the v2 max. Fix: Oct 1 $200 to Reserve → ≈ 13.6%. Optional: selling QUBT adds ≈ $213 of dry powder.

## 1b. Active-trading rules (v2, from 2026-10-01)
Client asked to trade more, citing the physical gold + cash vault outside the account as the real safety layer.
The guard rails that protect capital stay; the ones that only limited activity are loosened.

| Rule | v1 | **v2** |
|---|---|---|
| Fills per month | ≤ 2 | **≤ 8** (≈ 2 a week). Over 8 → no new buys for the rest of the month; sells always allowed |
| Reserve floor for stock buys | 15% (band 15–25%) | **10%** (band 10–25%); the index ladder may still go to 5% |
| Satellites | ≤ 5 | **≤ 6** (7 lines with VOO) |
| Speculative names | banned | **one slot**, ≤ 6% of the sleeve at cost, stop written first and ≤ 12% under entry |
| Adds per name | 1 average-down | **2 adds per holding period**, each ≤ 4% of the sleeve (≈ $150); count resets after a sale that banks a profit |
| Earnings blackout for adds | 10 trading days | **5 trading days** |
| Dip zones | some retired | **every holding always has one** (client instruction) |
| VOO index ladder | −7% / −15% | **−4% → ¼ Reserve**, −7% → ½, −15% → rest to the 5% floor |

**Unchanged (strict):** stop and reward/risk ≥ 2:1 written before every buy; dip zones always sit above the stop;
hard exit at the stop and at −15% from cost; single name ≤ 15% after adds, trim at 20%; trim ladder +25/+40/+75;
circuit breaker at −10% from peak; no leverage, shorts, CFDs, options, crypto or SPACs; banked profit 50/50 Reserve/VOO.

**Cost:** 8 fills a month at $1 is up to $96 a year, ≈ 2.6% of the sleeve. **Review 2026-12-31:** if fills beyond the old
2-a-month pace lose money net of fees over the quarter, revert to v1 numbers (§9).

## 2. Satellite rules — entry
- Passes the full research protocol; verdict table filed in `research/`.
- Not >20% above its 50-DMA, RSI(14) < 70, no earnings inside 5 trading days (else starter size only).
- Reward/risk ≥ 2:1 to the first target. Invalidation level written down *before* the buy.
- **Enter in halves**: half at the level, half on confirmation. Full size = 10–15% of sleeve.
- 6 satellites max (v2). A 7th idea must be better than the weakest holding, which gets sold to fund it.
- Never: shorts, leverage, CFDs, options, crypto, SPACs.
- **One speculative slot** (story / micro-cap, e.g. QUBT): ≤ 6% of the sleeve at cost, stop written first and ≤ 12%
  under entry, one at a time. SPCX/CHZ on the statement are the reason for the cap.

## 3. Satellite rules — profit ratchet (the core of the plan)
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

**Where banked profit goes:** 50% → Reserve (Tier 3), 50% → VOO (Tier 1). Redeploying it into
another satellite is allowed only via the entry rules above, never automatically.

## 4. Satellite rules — losses
- **Hard exit at −15% from avg cost** or on a fundamental thesis break, whichever first. No debate,
  no averaging down into a broken thesis. Re-entry later is always allowed.
- Up to **two adds** per name per holding period (v2), only on a technical pullback with the thesis intact,
  only inside a dip zone above the stop, each ≤ 4% of the sleeve, never past the 15% cap, and only from cash above
  the 10% floor. The count resets after any sale from the line that banks a profit.
- Time stop: a satellite that has not moved in your favor after two earnings cycles is reviewed for replacement.

## 5. Reserve and contributions
- **Monthly $200 → VOO by default** while Core < 35% and the Reserve is ≥ 10%; otherwise → Reserve.
- Reserve deployment ladder (S&P 500 from its high, or a satellite at its 50-DMA with thesis intact):
  - **−4%** (v2): deploy up to **a quarter** of the Reserve, VOO only.
  - **−7%**: deploy up to **half** of the Reserve — into VOO first, then the best-rated satellite.
  - **−15%**: deploy the second half, keeping the 5% floor.
  - Never all at once; never below the 5% floor.
- After a deployment, rebuild the Reserve to 10% from contributions before any new satellite buy.

## 6. Cadence
- **Weekly (10 min)**: prices vs ladder triggers and stops; any thesis-relevant headline. `/stock-desk check`.
- **Monthly**: fresh statement PDF → `portfolio/statements/`; full review; contribution decision. `/stock-desk review`.
- **Event-driven**: holdings' earnings, FOMC, index changes, anything that hits an invalidation.
- **Shock (index ±3% day, VIX spike, or a holding gapping)**: `/market-move` — applies §3–§7 mechanically
  via `portfolio/levels.csv` and returns a decision card. No improvising in the moment.

## 6b. Flags — when to call the desk (`/stock-desk`), levels as of 2026-10-01
Live version with news and statuses: **Amana Flag Board** (https://claude.ai/artifact/HjfHpid7GbLvP5VQUSYZmF).
Check prices **once a week** (Friday after the close). Between checks, act only if a flag fires.
Averages are the broker's blended costs from the 2026-09-29 statement. MAs are 9/30 daily (Yahoo closes).

**Price and trim flags (closing prices).** Ladder from avg cost; banked profit 50% Reserve / 50% VOO.
| Ticker | Avg cost | ⚠ Exit (close below) | +25% → stop to BE | +40% → sell ⅓ | +75% → sell ⅓ | Catalyst trim |
|---|---|---|---|---|---|---|
| EWY | 171.04 | **172** | 213.80 | 239.46 | 299.32 | none |
| ARM | 259.17 | **250** | 323.97 | 362.84 | 453.55 | none (earnings 11/4) |
| BE | 239.26 | **250** | 299.07 | 334.96 | 418.70 | **> 299 before 10/27 earnings → sell ⅓** |
| TTWO | 215.98 | **185 weekly close** | 269.97 | 302.37 | 377.96 | launch week 11/16–20 > **270** → sell ⅓ |
| WDC | 451.14 | **395** (move broker stop from 420) | 563.93 | 631.60 | 789.50 | none (earnings ~10/29) |
| QUBT | 7.92 | **8.00** | — | — | — | speculative slot (≤ 6% at cost); broker TP 10 |
| VOO | 705.79 | none (core) | never | never | never | none |
| Any satellite | — | — | — | — | — | market value > 20% of sleeve → trim to 15% |

**Dip-buy flags (plan v2).** Every holding always has a zone (client instruction 2026-10-01). Locked while the Reserve
is below 10%. Up to two adds per name per holding period (count resets after a profit-banking sale), each ≤ $150 and
never past 15% of the sleeve, only from cash above the 10% floor, never within 5 trading days of earnings, 8 fills a
month in all. The VOO index rungs come first on an index dip. R/R measured from the zone midpoint.
| Ticker | Dip-buy zone | Anchor | Stop | R/R | Max add | Adds used | Window |
|---|---|---|---|---|---|---|---|
| VOO | ≈ $686 (SPX −4%) · ≈ $664 (−7%) · ≈ $607 (−15%) | Sep 16 low 689; 200-DMA 662 | none | — | ¼ · ½ · rest of Reserve (5% floor) | — | any time |
| ARM | **$262–268** | 50-DMA 265.12 | 250 | 4.5:1 to 333 | $150 | 1 of 2 | until 10/27 |
| EWY | **$176–178** | 50-DMA 175.98, Sep low 173.90 | 172 | 3.4:1 to 194 | $145 | 0 of 2 | after Samsung Q3 preview (~10/7) |
| BE | **$256–262** | 9/24 + 9/28 entries; 9/28 close 262.87 | 250 | 4.8:1 to 302 | $100 (tight stop) | 0 of 2 | until 10/19 |
| TTWO | **$188–196** | March low 187.63 → 9/28 low 199.46 | 185 wk | 5.1:1 to 227 | $150 | 1 of 2 | until 10/28 |
| WDC | **$410–420** ($425–435 if the stop stays 420) | double bottom 407 | 395 | 2.8:1 to 471 | $150 | 0 of 2 | until 10/21 |
| QUBT | **$8.10–8.30** | just above the $8 stop; 50-DMA 8.41 | 8.00 | 4.8:1 to 9.16 | ≈ $30 (6% spec cap) | 0 of 2 | until 11/5 |
| GOOGL (watch) | $315–328 | 7/23 low 314.90, 9/10 low 327.74 | 305 | 2.6:1 to 364 | needs a free slot | — | after 10/28 earnings |
| INTC (watch) | $100–105 | 50-DMA 100.15, 7/15 low 99.20 | 94 | 2.9:1 to 127 | needs a free slot | — | after ~10/22 earnings |

**Market flags** (S&P 500 record close 7,798.99 on 2026-08-13; 7,651.54 on 9/30 = −1.9%)
- ☐ SPX **−4%** (≈ 7,487) → up to a quarter of the Reserve into VOO (v2).
- ⚠ SPX **−7%** (≈ 7,253) → deploy up to half the Reserve (VOO first). Use `/market-move`.
- ⚠ SPX **−15%** (≈ 6,629) → deploy the second half, keep the 5% floor.
- ⚠ Sleeve equity **< $3,303** (−10% from the $3,670 peak of 9/21) → circuit breaker.
- ⚠ VIX spike or any holding gaps > 8% on news → `/market-move` before touching anything.

**Calendar flags**
| Date | Event | Action |
|---|---|---|
| 2026-10-01 | $200 contribution · sell QUBT | contribution → Reserve |
| 2026-10-02 | Jobs report | no trades that morning |
| ~2026-10-07 | Samsung Q3 preview (unverified) | EWY dip zone opens after |
| 2026-10-14 | CPI · last day for WDC adds | no trades that morning |
| 2026-10-20 | last day for ARM adds | 11/4 earnings |
| ~2026-10-27 | BE earnings | ⅓ trim beforehand if > 299 |
| 2026-10-28 | FOMC (hold vs hike) · GOOGL earnings | no trades that day |
| ~2026-10-29 | WDC earnings · Samsung full Q3 | hold with stops |
| 2026-11-01 | $200 contribution | VOO if Reserve ≥ 15%, else Reserve |
| 2026-11-04 / 11-05 | ARM / TTWO earnings | hold; TTWO ±10–18% gap accepted |
| 2026-11-16→20 | GTA VI launch week (11/19) | TTWO > 270 → sell ⅓ |
| 2026-12-19 | TTWO review | exit or re-underwrite |

**Anything else** (a headline that scares or excites you, an urge to buy something new): write it down, bring it to the
weekly check. A new name needs a filed research note and must beat the weakest holding.

## 7. Scorecard (measured from 2026-08-18)
- Satellite sleeve vs VOO, rolling 6 months — the only test of whether the satellite layer earns its risk.
- Max drawdown of the whole sleeve: **target < 15%**. Circuit breaker at −10% from peak (halve every satellite, pause buys, write the post-mortem).
- Profit ratcheted into Tiers 1+3 per year (dollars). Win rate matters less than this number.
- Fills: ≤ 8 a month under v2 (was 2). Fees tracked; v2 review 2026-12-31.

## 8. Current application (2026-09-30 closes; see journal/2026-10-01-review.md)
| Ticker | Avg cost | Now | P&L | Hard exit | Notes |
|---|---|---|---|---|---|
| EWY | 171.04 | 182.78 | +6.9% | 172 | memory 20% with WDC; dip 176–178 after Samsung preview |
| BE | 239.26 | 276.98 | +15.8% | 250 | avg-down used ×2 (override); sell ⅓ > 299 before 10/27 |
| TTWO | 215.98 | 207.50 | −3.9% | 185 weekly | hold to launch; avg-down used; review 12/19 |
| ARM | 259.17 | 289.66 | +11.8% | 250 | dip 262–268 until 10/20 |
| WDC | 451.14 | 454.46 | +0.7% | 395 (move from 420) | opened 9/24 as 6th satellite (override); research note owed |
| QUBT | 7.92 | 8.45 | +6.7% | 8 | speculative slot under v2; dip 8.10–8.30, max ≈ $30 |
| VOO | 705.79 | 700.86 | −0.7% | — | core; never trimmed |

Reserve $320 (8.8%) → ≈ $520 (13.6%) after the Oct 1 $200, ≈ $135 above the 10% floor to spend. Selling QUBT would add ≈ $213.

## 9. Override protocol
If Wael wants to do something the plan or the desk objects to: the desk states the objection, the
data, and the rule it breaks — once, plainly. If Wael still wants it, it is executed and logged in
`journal/` as an **OVERRIDE** with the reasoning. Overrides are reviewed quarterly: if they are
beating the rules, the rules change; if not, they stop.

## Changelog
- 2026-10-01 v2 — client asked to trade more (vault outside the account is the safety layer). Loosened: fills 2 → 8/month, Reserve floor 15% → 10%, satellites 5 → 6, one speculative slot (≤ 6% at cost), 2 adds per name (reset after profit-banking sale), earnings blackout 10 → 5 trading days, VOO −4% rung. Every holding always carries a dip zone. Kept: stops + R/R ≥ 2:1 first, 15% name cap, ladder, circuit breaker, no leverage/shorts/options/CFDs/crypto. Review 2026-12-31. QUBT no longer a forced sale.
- 2026-10-01 v1.2 — 9/29 statement review: logged 11 fills (9/15–9/29); Reserve 8.7% and 6 satellites breach the plan → sell QUBT, Oct $200 to Reserve, buy freeze until ≥ 15%, one dip fill in October. New dip zones (ARM 262–268, EWY 176–178, WDC 410–420 with stop 395), BE pre-earnings trim > 299, GOOGL 315–328 / INTC 100–105 watch zones. Overrides logged: WDC 6th satellite, BE double average-down.
- 2026-09-09 — §6b: added per-name trim ladder table.
- 2026-09-09 — §6b: added per-name dip-buy zones (client asked why only exits were listed).
- 2026-09-09 — TTWO: client requested $400 now + hold through launch; challenged per §9; client then decided NOT to add at all. Existing position held through launch to 12/19 (⅓ trim in launch week if >$271). Stop $195 → $185. Added §6b flag list.
- 2026-09-09 v1 — initial plan after the cash-account switch and first review.
- 2026-09-09 v1.1 — added `/market-move` shock playbook; per-name levels moved to `portfolio/levels.csv`.
