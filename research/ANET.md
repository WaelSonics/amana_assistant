# ANET — Arista Networks — research log

One file per ticker; newest entry first. Each entry is dated; numbers are as of that date.

Entries:
- 2026-10-28 (deep dive)
- 2026-10-19 (update)
- 2026-10-16 (update)
- 2026-10-15

---

## ANET — Arista Networks — deep dive 2026-10-28

**Verdict:** WATCH, no passing zone · **Conviction:** Med on the business, Low on the setup. A top-quality AI-networking
franchise, but at an $8.53 ATR in a chart with a swing level every $5–12, no support pays 2:1 to the next resistance with
a stop ≥ 1.5 ATR. **The standing PLAN zone B ($156–160, stop 150, T1 181) fails the 1.5-ATR stop test at every edge.**
No buy is possible before the 11/3 report. Re-run the levels after the 11/4 close.

| | |
|---|---|
| Price (date) | **$185.24** (levels.py, 2026-10-28 10:52 ET; open 190.17, high 191.11). Cross-check $185.80 (stockanalysis, 11:04 ET) |
| Entry zone | **None passes.** Five zones tested with `levels.py --zone` (below). Zone B as written in PLAN §6b fails |
| Invalidation (stop) | n/a, no position. Thesis-level: a Q4 guide below Q3 actual, a top-2 customer capex cut, a non-GAAP op-margin guide < 45% |
| Target 1 / 2 | n/a without a zone. Swing highs above: 189.82 / 200.68 / 206.13 / 212.00 / 214.89 / 217.41. Fundamental: analyst average $243.59 (stockanalysis, 10/28) |
| Reward/risk (T1) | Best tested: **1.51:1** (zone 181–183, stop 168, T1 200.68, skipping the nearer 189.82). ✘ |
| Size | n/a. When a zone passes: ≈ $190 starter (5.5% of $3,426), risk to stop ≤ $69 (2%) |
| Timeframe | Months (hyperscaler capex cycle) |
| Next earnings | **2026-11-03 after the close** (Arista PR 10/6; levels.py: 4 sessions). Blackout **10/29–11/3** |

### What changed since the 10/19 update
- **The floor broke, then was retaken.** 10/22 close $171.07 (**−7.2%**, 8.3M shares) in the sector sell-off after Meta's
  print. 10/23 low **$168.24**, which held ≈ 3% above the rising 200-DMA (≈ $163.4 that day). Then 10/26 $177.24 and
  **10/27 $187.00 (+5.5%)**, exactly the top of the old $181–187 floor, not above it. Today it opened $190.17, failed at
  $191.11 (the 7/9 swing high is 189.82) and trades $185.24. The 10/19 condition ("a daily close *above* $187") has
  **not** been met.
- **The 50-DMA has turned down** ($195.53 vs $198.97 ten sessions ago). The 20-DMA ($194.62) is now under the 50-DMA.
- **ATR rose** from $8.19 to **$8.53**. The new `levels.py --zone` check shows zone B was never valid: at $160 the $150
  stop is 1.17 ATR (it was 1.22 ATR on 10/19; the 10/19 entry did not test the ATR distance).
- Consensus for Q3 is now **$3.33B / $1.08 EPS** (Yahoo via Motley Fool, 10/19). The options imply ±10.35% for the
  report week (optionslam, 10/28).
- Insiders keep selling: **four Form 144s on 10/20** and a Form 4 on 10/22 (EDGAR, fetched 10/28).

### Thesis
Arista sells the Ethernet switches that connect AI clusters at the big cloud builders. Q2'26 revenue was **$3.036B,
+37.7% y/y**, with a 63.4% non-GAAP gross margin and a 49.9% non-GAAP operating margin (8-K, 8/4). It has **$13.34B of
net cash, no debt and $5.16B of TTM free cash flow** (stockanalysis, 10/28). The stock is a proxy for hyperscaler capex,
and two customers (Meta and Microsoft, per TradingKey 10/27) are over 40% of revenue. So this week's MSFT/GOOGL (10/28)
and AMZN (10/29) capex numbers matter as much as the 11/3 print. At **40× forward earnings and 22.7× trailing sales**
(stockanalysis, 10/28) the business is priced for delivery. The problem today is the setup, not the business.

### Chart & technicals — `levels.py ANET` (Yahoo daily bars, quote 2026-10-28 10:52 ET)
```
ANET  $185.24 (2026-10-28 10:52 ET); last daily bar 2026-10-28 close $185.24
  20/50/200-DMA  194.62 / 195.53 (falling) / 164.67 (rising)   price vs 50 -5.3%, vs 200 +12.5%
  RSI(14) 45.3   ATR(14) $8.53 = 4.6% a day   52-wk 114.52–217.41 (-15% from the high)
  Trend: above a rising 200-DMA
  Chase guard: ok
  Next report: 2026-11-03 after the close (4 sessions; EPS est. 0.99)   ✓ outside the buy blackout
  Swing support below: 182.83, 181.27, 162.25   resistance above: 189.82, 200.68, 206.13
```
- **Trend:** above a rising 200-DMA, below a falling 50-DMA. That makes it a pullback inside an uptrend, not a fresh long
  signal. RSI 45 is neutral and the chase guard passes.
- **What levels.py cannot see:** its swing finder needs 5 bars on each side, so the **10/22–10/23 lows ($169.87 /
  $168.24)** are not listed yet. They come from the same Yahoo bars levels.py cached. 182.83/181.27 are no longer
  untested support: they broke on 10/22 and were retaken on 10/27.
- **Levels (all from levels.py's 6-month swing list, plus the 10/23 low):** support 182.83 · 181.27 · **168.24** · 164.7
  (200-DMA) · 162.25 · 157.13/156.84 · 154.74. Resistance **189.82** (7/9 high; today's 191.11 rejection) · 195.5
  (50-DMA) · 200.68 · 206.13 · 212.00 · 214.89 · 217.41 (record).
- **Volume:** the 10/22 down day ran 8.3M and the 10/27 up day 5.65M. The sell-off had more conviction than the bounce.
- Chart: `/tmp/claude-1000/-home-waelas-wael-amana-amana-assistant/cf7235bd-03e5-456e-8948-a8c2229a57bd/scratchpad/charts/ANET.png`.
  It shows a 10/22–10/23 wick to the 168 shelf, above the 200-DMA, a V back to 187, and the 20-DMA rolling under the 50.

### Zone checks — `levels.py ANET --zone … --size 190 --sleeve 3426` (10:52 ET data)
```
# 1. PLAN §6b zone B as written
  Setup: zone 156.00–160.00, stop 150.00, T1 181.00
    at low     156.00: R/R 4.17:1, stop 0.70 ATR (3.8%)   ✘ stop < 1.5 ATR
    at mid     158.00: R/R 2.88:1, stop 0.94 ATR (5.1%)   ✘ stop < 1.5 ATR
    at high    160.00: R/R 2.10:1, stop 1.17 ATR (6.2%)   ✘ stop < 1.5 ATR
# 2. The retaken Aug–Sep floor, stop under the 10/23 low, T1 = nearest swing high
  Setup: zone 181.00–183.00, stop 168.00, T1 189.82
    at low     181.00: R/R 0.68:1, stop 1.52 ATR (7.2%)   ✘ R/R < 2
    at mid     182.00: R/R 0.56:1, stop 1.64 ATR (7.7%)   ✘ R/R < 2
    at high    183.00: R/R 0.45:1, stop 1.76 ATR (8.2%)   ✘ R/R < 2
# 3. Same, generous T1 (skips 189.82 and the 50-DMA)
  Setup: zone 181.00–183.00, stop 168.00, T1 200.68
    at low     181.00: R/R 1.51:1, stop 1.52 ATR (7.2%)   ✘ R/R < 2
    at high    183.00: R/R 1.18:1, stop 1.76 ATR (8.2%)   ✘ R/R < 2
# 4. 200-DMA shelf (4/28 low 162.25), T1 = 6/22 swing high
  Setup: zone 162.00–165.00, stop 149.00, T1 175.20
    at low     162.00: R/R 1.02:1, stop 1.52 ATR (8.0%)   ✘ R/R < 2
    at high    165.00: R/R 0.64:1, stop 1.88 ATR (9.7%)   ✘ R/R < 2
# 5. Same, generous T1 = the broken floor
  Setup: zone 162.00–165.00, stop 149.00, T1 181.27
    at low     162.00: R/R 1.48:1, stop 1.52 ATR (8.0%)   ✘ R/R < 2
    at high    165.00: R/R 1.02:1, stop 1.88 ATR (9.7%)   ✘ R/R < 2
    (every size line: risk $9.62–16.85 = 0.3–0.5% of $3,426 ✓ ≤ 2%)
```
**No zone passes.** To fix zone B's stop you must move it to ≤ $147 (1.5 ATR under $160), and then R/R to $181 drops to
1.6:1. Under these rules, a stop ≥ 1.5 ATR with R/R ≥ 2 needs **T1 ≥ 3 ATR (≈ $26) above the zone top**. Today the
nearest swing high sits only $7–13 above every support.

**What would create a zone:**
- **(a)** The 11/3 report resets the structure. Either a close above **$217.41**, which leaves no overhead swing high
  (T1 then has to be a measured move written *before* the buy, and the chase guard re-checked), or a flush that builds a
  new base with ≥ $26 of clear air to the next swing high.
- **(b)** ATR compresses toward ≈ $4–5, so the $181–183 floor can pay 2:1 to 200.68 with a stop around $174. That is
  unlikely in the two weeks after a report.

### Earnings preview (section A) — not held: the job is to define the post-report buyable level
1. **Date/time:** Tue **11/3 after the close**, call 4:30 ET (Arista PR 10/6; levels.py/Alpha Vantage agree). The
   last decision point is the 11/2 close, and the client freeze plus the blackout already close every pre-report day.
2. **Consensus:** Q3 revenue **$3.33B**, EPS **$1.08**. Q4 is $3.6B / $1.15 (Yahoo via Motley Fool, 10/19). Company
   guide: revenue ≈ $3.3B and a non-GAAP operating margin of 48–49% (Q2 8-K, 8/4). An EPS guide of $1.06–1.08 is
   **unverified**: one fetch of the 8-K shows it, while Motley Fool says Arista does not guide EPS. The metrics that move
   it are the Q4 revenue guide, gross margin (≈ 63%) and AI/cloud commentary on 2027. Alpha Vantage's 0.99 estimate is
   stale.
3. **Implied move:** **±10.35%** (weekly, Nov 6 expiry; monthly ±12.81%; optionslam, fetched 10/28) ≈ **±$19 → $166–204**.
   That whole range sits inside the dense 168–206 structure. On a $190 starter it is ≈ $20 at stake. The August implied
   move was 14.11% and the close-to-close was +3.6%.
4. **Scenarios:**

   | Scenario | What has to happen | Likely reaction | Action written now |
   |---|---|---|---|
   | Bull | Q3 > $3.4B, Q4 guide ≥ $3.7B, GM ≥ 63%, 2027 growth framed ≥ 25% | Gap +8–12% into the 200.7/206.1/212 ladder | No buy into the gap. Buyable only after a **close > $217.41** with a written measured-move T1, or a pullback base with ≥ 3 ATR to T1 |
   | Base | In line ($3.30–3.35B; Q4 ≈ $3.6B) | ±5%, stays 168–200 | No zone (structure too dense). Re-check weekly |
   | Bear | Miss, Q4 guide < $3.5B, GM < 62%, or "sell the beat" (−13.6% on 5/6) | Gap to 160–170, onto the 200-DMA (≈ $166 by 11/4) | No catch. Wait ≥ 2 sessions for a base. Under the 200-DMA there are no fresh longs |

5. **History** (close-to-close / opening gap, from levels.py's Yahoo bars): 11/5/25 **−8.6% / −7.1%** · 2/13/26
   **+4.8% / +7.9%** · 5/6/26 **−13.6% / −10.1%** · 8/5/26 **+3.6% / +10.3%**. Two of four fell, and two gap-ups faded
   intraday. (2/12/26 report date not re-verified.)
6. **Decision:** not held, so nothing to decide on 11/2. **No buy before the report.** Run `levels.py ANET` after the
   **11/4 close**. PLAN allows 11/4; the desk recommends 11/5, after one full post-report bar. 11/6 is a jobs-report
   morning, so afternoon only.

### Thesis scorecard (section B)
| Pillar (falsifiable) | Expected | Status (dated) | Trend |
|---|---|---|---|
| Revenue growth ≥ 30% y/y | ≥ 30% | Q2 +37.7% (8-K 8/4); Q3 guide ≈ $3.3B, consensus $3.33B (10/19) | stable |
| Non-GAAP op margin ≥ 47% | 48–49% guide | Q2 49.9% (8/4) | stable |
| Gross margin ≥ 62% | ≈ 63% | Q2 63.4% non-GAAP; TTM 63.0% (stockanalysis 10/28) | slowly weakening |
| Top customers keep raising capex | up | Meta FY26 capex **$135–145B** (low end raised), but Q3 FCF **−$2.12B** (Meta 10/21, via Gotrade 10/23); MSFT/GOOGL 10/28, AMZN 10/29 pending | mixed |
| Insider selling not a signal of a top | 10b5-1 only | four 144s on 10/20, a Form 4 on 10/22 (EDGAR 10/28) | unchanged |

**Thesis-break exits** (for a future position): a Q4 guide below Q3 actual, or a FY cut · a Meta or Microsoft capex cut
· a non-GAAP op-margin guide < 45%. **Conviction:** Med. It goes up on a Q4 guide ≥ $3.7B with GM ≥ 63%, and down on a
top-2 customer capex cut.

### Fundamentals (stockanalysis statistics, fetched 2026-10-28 11:04 ET, unless noted)
- Market cap **$234.3B**, EV $221.0B. Trailing P/E 58.8, **forward P/E 39.95**. P/S 22.7, forward P/S 16.5, EV/S 21.5.
- TTM revenue $10.54B, GM 63.0%, GAAP operating margin 43.1%, FCF **$5.16B**. **Net cash $13.34B**, no debt. Shares
  1.26B (−0.26% y/y; no dilution).
- Q2'26 (8-K, 8/4): revenue $3.036B (+37.7%), non-GAAP GM 63.4%, op margin 49.9%, EPS $1.02. It has beaten EPS
  consensus 8 quarters running (search summary of MarketBeat, 10/28).
- Risks: $9.7B of non-cancellable purchase commitments, $9.4B of them due within 12 months; > 40% of revenue from two
  hyperscalers (TradingKey, 10/27).

### News & catalysts (last 30d / next 90d)
- 2026-10-28 — neutral — opened +1.7% at $190.17 and was rejected at $191.11. FOMC at 2:00 ET; MSFT and GOOGL report
  tonight (AMC).
- 2026-10-27 — confirming (sentiment) — +5.5% to $187.00 into the report. TradingKey cites pre-earnings positioning; no
  company news.
- 2026-10-22 — neutral/sector — **−7.2%** to $171.07 in the AI-infrastructure sell-off after Meta's 10/21 print (capex
  over operating cash flow). Tickeron also cites 10b5-1 sales by the CEO and CFO.
- 2026-10-20/22 — neutral — four Form 144s (10/20) and a Form 4 (10/22) (EDGAR).
- 2026-10-06 — neutral — Q3 date set: 11/3 AMC.
- **Next:** 10/28 FOMC + MSFT/GOOGL · 10/29 PCE + AMZN · **11/3 ANET Q3** (and US midterms) · 11/6 jobs report.

### Positioning & sentiment
- Short interest 11.93M = **1.14% of float**, 2.49 days to cover (stockanalysis 10/28, settlement date not shown). Not a
  squeeze candidate.
- Analysts: **Strong Buy (32)**, average PT **$243.59** (stockanalysis 10/28). TradingKey has $240.33 (range $140–290).
- Crowding: a high-beta AI-capex proxy (β ≈ 2.1 per one aggregator, unverified). Extended + crowded + report in 4
  sessions is the setup the client wants to avoid. It is not extended now, but the report is binary for it.

### What would make me wrong
- Being too strict: a clean Q3 beat and a close above $217.41 runs away without a pullback. That is acceptable; the rules
  are built to miss some winners.
- On the business: the Q4 guide disappoints or GM slips under 62% (NVIDIA Spectrum-X / white-box share), or MSFT/GOOGL
  cut capex tonight.
- On the chart: a close under **$168.24** (10/23 low) puts the 200-DMA (≈ $165) in play. A close under the 200-DMA ends
  the uptrend case.

### Sources
- `levels.py ANET` and zone checks, Yahoo chart API, quote 2026-10-28 10:52 ET (cache written 10:52 ET). Chart PNG above
- Q2'26 8-K (8/4): https://www.sec.gov/Archives/edgar/data/0001596532/000159653226000174/ex991q226-earningsrelease.htm — fetched 10/28
- Q3 date: https://www.arista.com/company/news/press-release/24817-pr-20261006 — 2026-10-06, fetched 10/28
- [Motley Fool, 10/19: Arista heads for a big test on Nov 3](https://www.fool.com/investing/2026/10/19/arista-networks-is-heading-for-a-big-test-on-nov-3/) — consensus $3.33B / $1.08
- [optionslam ANET](https://www.optionslam.com/earnings/straddle/ANET) — implied move, fetched 10/28
- [stockanalysis ANET statistics](https://stockanalysis.com/stocks/anet/statistics/) — 10/28 11:04 ET
- [TradingKey, 10/27](https://www.tradingkey.com/news/market-movers/262242630-market-movers-anet-20261027) · [Tickeron, 10/22](https://tickeron.com/blogs/why-is-arista-networks-anet-stock-down-6-61-today-20632/)
- EDGAR filing list, CIK 1596532 — fetched 10/28
- [Stocktitan earnings calendar, week of 10/26](https://www.stocktitan.net/articles/earnings-calendar-week-of-october-26-2026) — upd. 10/26
- [Gotrade, 10/23: Meta falls 7%](https://www.heygotrade.com/en/news/meta-meta-stock-news-october-23-2026/) — Meta capex/FCF figures (via search summary)
- [Guggenheim 2026 economic calendar](https://www.guggenheiminvestments.com/services/advisor-resources/us-economic-calendar) — jobs report 11/6 (via search summary)

---

## ANET — update 2026-10-19

**Verdict:** WATCH · zone B only (**≤ $160**, stop $150) · no buy before the **11/3** report · **Conviction:** Med on the
business, Low on the setup. Zone A failed on the 10/16 close ($176.98 < $178). The 10/19 bounce to $181 is a test of the
broken floor from below, not a reclaim.

| | |
|---|---|
| Price | **$181.15** (2026-10-19, 10:35 ET, +2.4%); close $176.98 (10/16, −4.6%); 10/16 low **$176.77** |
| 20 / 50 / 200-DMA | $203.2 / $198.3 (rising) / **$162.9** (rising) — price −8.6% under the 50, +11% over the 200 |
| RSI(14) · ATR(14) | 35.8 · **$8.19 = 4.5% a day** · −16.7% from the 10/9 high of $217.41 |
| Zone B | **$156–160** (the 200-DMA and the 7/17–7/29 lows $156.8–157.1), stop $150, sell zone $181–187 → **2.1:1 at $160** |
| Timing | October buying is closed; buys resume 11/2, but ANET reports **11/3** after the close (blackout 10/29–11/3). So: re-run the levels on 11/4 |

**Why it fell (dated):** no Arista-specific news 10/10–10/19. The group de-rated on funding, not orders: Broadcom CEO
Hock Tan (10/12) said capital may limit the AI build-out more than chips; CoreWeave's 2032 bonds hit 15% and CRWV fell
15.5% (10/14). TrendForce (10/14) still sees 2027 hyperscaler capex above $1.5T.

**What would change it:** a daily close back above **$187** (the top of the old floor) would be evidence the break
failed, worth a fresh zone after the report. A close under the 200-DMA (≈ $163) moves zone B into play.

**Sources:** Yahoo chart API ANET 1y daily, fetched 2026-10-19 10:35 ET · [simpletechtrend, wk 42](https://www.simpletechtrend.com/en/post/optical-selloff-funding-vs-supply-2026-w42-en) · [24/7 Wall St, 10/14: AI funding fears hit optical stocks](https://247wallst.com/investing/2026/10/14/applied-optoelectronics-dives-9-as-ai-funding-fears-hit-optical-stocks-coherent-slides-7-lumentum-drops-7/) · earnings date per the 10/15 entry (confirmed).

---

## ANET — update 2026-10-16

Two desk runs on 10/15 gave two zones; they are now one plan (PLAN §6b):
- **Zone A, $178–181 on a daily close** (stop 170, sell zone 205–212, 2.2–2.7:1). It needs the August–September floor
  ($181–183) to hold. On 10/15 it did: low $178.47, close $185.58.
- **Zone B, ≤ $160, used only after a close under $178** (stop 150, sell zone 181–187 = the broken floor, 2.1:1 at 160).
  This came from the 11:19 ET run (`journal/2026-10-15-anet-lite.md`). It sits at the rising 200-DMA ($162.7) and the
  7/17–7/29 lows ($156.8–157.1).

Price $181.13 (2026-10-16, 09:44 ET; open 187.97, low 180.38), at the top of zone A. RSI 33.6, ATR $8.11.
**Not a buy today.** 10/15 already had two stock buys (AMD, MU), and the plan allows one a week. ANET would also be a third
AI-hardware line next to AMD and ARM, and the account is only $73 above its breaker. Window: **10/19–10/27**, on a close in
zone A, and only while the account is ≥ $3,500.

---

## ANET — Arista Networks — deep dive 2026-10-15

**Verdict:** WATCH → BUY in **$178–181** on a close, until **10/28** (it reports 11/3) · **Conviction:** Med-High. A
top-quality AI-networking business in a live uptrend, pulled back 16% to its August–September floor. It is not cheap
(21× sales, the top of its own range), and insiders are selling heavily.

| | |
|---|---|
| Price | **$182.66** (2026-10-15, 11:35 ET, −6.5%); today's low $178.47; 4 down days from the $217.41 record (10/9) |
| 20 / 50 / 200-DMA | $205.4 / **$198.7** / **$162.4** — all three rising; price −8% under the 50, +12.5% over the 200 |
| RSI(14) · ATR(14) | 34.6 · $8.33 = **4.6% a day** |
| Entry zone | **$178–181** (8/20 low 182.8, 9/3 low 181.3, today's low 178.5) |
| Stop | **$170** (under the zone and today's low by ≈ 1 ATR; −5.6% from $180) |
| Sell zone (⅓) | **$205–212** (20-DMA 205.4, 8/27 high 206.1, 9/25 high 212.0) |
| Reward/risk | **2.2:1 at $181 · 2.7:1 at $178** ✓ — at today's $182.66: 1.8:1 ✘ |
| Size | ≈ $200 (≈ 5.7%), risk to the stop ≈ $12 |
| Next earnings | **Tue 11/3** after the close (company, 10/6). Last 4 reactions −8.6% / +4.8% / −13.6% / +3.6% |

## Business (8-K / 10-Q)
- **Revenue:** Q2'26 **$3.04B, +37.7%**. Non-GAAP gross margin 63.4%, operating margin 49.9%, EPS $1.02.
- **Guidance:** Q3 guide ≈ $3.3B (+43%). FY26 guide ≈ **$12.6B (+40%)**, raised from $10.5B. AI-fabric revenue target
  ≥ $3.5B, from 100+ AI customers.
- **Visibility:** deferred revenue **$6.87B** and purchase commitments $9.7B.
- **Cash:** TTM free cash flow $5.16B. **$13.3B net cash**, no debt. Buyback room left: $818M.
- **Risks:** two customers were 42% of FY25 revenue (26% + 16%, likely Meta and Microsoft). Gross margin is drifting down
  (65.6% → 62–63%) as the mix shifts to big AI customers.
- **Valuation:** market cap $231B, EV $217.5B. **42× forward P/E**, 35× 2027. **21× trailing sales, the top of its 5-year
  range.** Peers: CSCO 7×, CIEN 8×, CRDO 21×.

## News
- **Sector:** this week's drop is sector-wide (COHR −6.8%, LITE −4.9%, CSCO −4.3% on 10/15). No ANET-specific bad news was
  found.
- **Analysts are raising targets into the drop:** Citi $248 (10/8), BNP $290 (10/14), Bernstein $250 (10/15), Melius
  $275. Consensus is Strong Buy, average $245 (range $190–290).
- **Product:** on 10/12 Arista launched Etherlink SU-144 scale-up Ethernet against NVIDIA's NVLink. No orders were
  disclosed.
- **Insiders:** ≈ **$853M sold in 3 months** (CEO Ullal $510M, co-founder Bechtolsheim $315M), all under 10b5-1 plans, with
  Form 144s through 10/9. Short interest is only 1.1% of float.
- **Competition:** NVIDIA Spectrum-X (co-packaged optics in production) and white-box vendors (Celestica leads AI Ethernet
  switch sales per Dell'Oro).

## Levels
- **Support:** **$181.3–182.8** (Aug/Sep lows, being tested) · $178.5 (10/15 low) · $162.2–162.4 (200-DMA + 4/28 low) ·
  $154.7–157.1.
- **Resistance:** $186.1 · **$198.7** (50-DMA) · $205.4–206.1 · $212.0 / 214.9 · $217.4 (record, a triple top 10/7–10/9).

## Rules for the buy
- Only on a **daily close inside $178–181**. A close under $178 means today's low gave way: wait for $162–165 (the 200-DMA)
  instead.
- Not on 10/28 (FOMC), and not after 10/28 (3 sessions before the 11/3 report).
- One buy with a written stop; it counts toward the October cap of 12. AMD's zone comes first (a compute name in its zone
  now). ANET is the second choice in AI hardware. Do not buy both on the same day.

## What would make me wrong
- A close under $170: the August–September floor has broken. The next stop is $162 (the 200-DMA).
- A hyperscaler capex cut (Meta or Microsoft), or a Q3 guide that shows margin pressure from NVIDIA or white-box share gains.
- The pattern of selling off after beats (−8.6%, −13.6%) repeats on 11/3. That is why the window closes 10/28.

## Sources
- Yahoo chart API ANET 2y daily bars, fetched 2026-10-15 11:35 ET
- Q2'26 8-K https://www.sec.gov/Archives/edgar/data/0001596532/000159653226000174/ex991q226-earningsrelease.htm · 10-Q https://www.sec.gov/Archives/edgar/data/1596532/000159653226000175/anet-20260630.htm
- Q3 date https://www.arista.com/company/news/press-release/24817-pr-20261006 — 2026-10-06
- https://stockanalysis.com/stocks/anet/statistics/ · /forecast/ · /financials/ratios/?p=quarterly — 2026-10-15
- https://www.marketbeat.com/instant-alerts/price-arista-networks-nyse-anet-stock-falls-46-on-insider-selling-2026-10-14/
- https://finance.yahoo.com/markets/stocks/articles/bnp-paribas-adjusts-price-target-094426545.html
- https://www.tradingview.com/news/gurufocus:15341790b094b:0-arista-stocks-fall-2-7-as-ethernet-invades-nvidia-s-rack/
- https://www.delloro.com/news/ethernet-extends-lead-in-ai-scale-out-networks-despite-strong-infiniband-rebound/
- SEC Form 4s (36 filings since 7/14), parsed 2026-10-15
