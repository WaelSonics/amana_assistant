# LITE — Lumentum Holdings — research log

One file per ticker; newest entry first. Each entry is dated; numbers are as of that date.

Entries:
- 2026-10-28 (deep dive)
- 2026-10-19 (update)
- 2026-10-15

---

## LITE — Lumentum Holdings — deep dive 2026-10-28

**Verdict:** WATCH, no passing zone · **Conviction:** Med on the business, Low on the setup. Same answer as 10/15 and
10/19, now measured by `levels.py`. At a 7.6% daily ATR a 2:1 trade needs **≈ $203 of clear air** above support, and
the nearest swing high is only $10–113 away. The $784–800 support from the last entry **broke on 10/22–10/23**, and so
did the 200-DMA on a closing basis, before a +17% V-rebound. Earliest buy is **11/6 afternoon, realistically 11/9**,
after the 11/5 report.

| | |
|---|---|
| Price (date) | **$887.35** (levels.py, 2026-10-28 10:52 ET; high 897.99). Cross-check $895.00 (stockanalysis, 11:04 ET) |
| Entry zone | **None passes.** Three zones tested (below) |
| Invalidation (stop) | n/a, no position. Thesis-level: FQ1 revenue < $1.225B guide low, a FQ2 guide that flattens, a weekly close under the 200-DMA, a change to the NVIDIA commitment |
| Target 1 / 2 | n/a. Swing highs above: 897.00 / 970.32 / 998.50 / 1,002 / 1,026.76 / 1,143 (record). Fundamental: analyst average $1,166.28 (stockanalysis 10/28) |
| Reward/risk (T1) | Best tested: **1.14:1** (zone 845–855, stop 735, T1 970.32, skipping 897). ✘ |
| Size | n/a. When a zone passes: ≈ $190 starter (5.5%). Hold at most **one optical name** (LITE / AXTI / AAOI) |
| Timeframe | Months (the InP laser / OCS / CPO ramp, 2026–28) |
| Next earnings | **2026-11-05 after the close** (Lumentum IR 10/5; webcast 5:00 ET; levels.py: 6 sessions). Blackout **11/2–11/5** |

### What changed since the 10/19 update
- **The support failed.** 10/22 close **$752.54 (−11.5%)**, 10/23 low **$736.01**, close $756.17. Both closes were
  under the 200-DMA (≈ $784–787 those days). The $784–800 shelf that the 10/15 and 10/19 entries called "best real
  support" gave way by $48. The hypothetical $680 stop was not reached.
- **Then a V.** 10/26 **+8.2%** to $818.10 on a StoneX initiation (Buy, $1,200; 24/7 Wall St 10/26). 10/27 +5.9% to
  $866.18. Today $887.35, which is **+17.3% from the 10/23 close** and **+20.6% from the low**. It is testing the 7/23
  swing high (897.00) and the 9/28 low (881.23), and today's high was 897.99.
- **The 50-DMA has turned down** ($921.30 vs $931.07 ten sessions ago). ATR is $67.52 = 7.6% (it was $69.26 = 8.1%).
- Consensus is firm at **$1.25B / $4.21–4.22** (MarketBeat 10/28), against Alpha Vantage's stale 3.82. Implied move
  **±13.33%** for the report week (optionslam 10/28).

### Thesis
Lumentum makes the indium-phosphide laser chips (EMLs, CW lasers for silicon photonics, CPO light sources) and the
optical circuit switches inside AI clusters. It guided FQ1'27 to **$1.225–1.275B revenue, a 39.5–40.5% non-GAAP
operating margin and $4.05–4.35 non-GAAP EPS** (8/11 release). Coverage on 10/26 again cites the CEO's "sold out through
early 2029" (24/7 Wall St). It has **$1.07B of net cash** and $300M of TTM FCF (stockanalysis 10/28). The price is the
catch: **41× forward earnings, 26× trailing sales**, $81B market cap. The stock trades as a high-beta proxy for
AI-capex *funding* (it fell −11.5% on 10/22 with no company news). It is the best business of the three optical names
and the hardest to buy under the 2:1 / 1.5-ATR rule.

### Chart & technicals — `levels.py LITE` (quote 2026-10-28 10:52 ET)
```
LITE  $887.35 (2026-10-28 10:52 ET); last daily bar 2026-10-28 close $887.35
  20/50/200-DMA  939.04 / 921.30 (falling) / 795.70 (rising)   price vs 50 -3.7%, vs 200 +11.5%
  RSI(14) 48.7   ATR(14) $67.52 = 7.6% a day   52-wk 184.20–1,143.00 (-22% from the high)
  Trend: above a rising 200-DMA
  Chase guard: ok
  Next report: 2026-11-05 after the close (6 sessions; EPS est. 3.82)   ✓ outside the buy blackout
  Swing support below: 881.23, 854.62, 845.00   resistance above: 897.00, 970.32, 998.50
```
- **Trend:** above a 200-DMA that rises ≈ $2.9 a day, and below a falling 50-DMA. The two-session close under the
  200-DMA (10/22–10/23) was reclaimed in one day. That is a shakeout, but not yet a higher-low structure: the last swing
  low (736) is far below the prior one (881, 9/28).
- **levels.py blind spot:** the **10/22–10/23 lows ($746.23 / $736.01)** are not listed because the swing finder needs
  5 bars on each side. They are the real nearest major support under the 845–855 May lows.
- **Levels:** support 881.23 · 854.62 · 845.00 · 818.89 · 795.7 (200-DMA) · 787/784 (8/11, 8/24, now broken) ·
  **736.01** · 680.43 · 650.82 · 594.84. Resistance **897.00** · 921 (50-DMA) · 939 (20-DMA) · 970.32 · 998.50–1,002 ·
  1,026.76 · 1,049.53 · 1,085.68 · 1,143.00.
- **Volume:** 10/22 down 6.16M, 10/26 up 6.06M, 10/27 up 5.56M. The bounce had real volume, unlike the 10/15 entry's
  "distribution".
- Chart: `/tmp/claude-1000/-home-waelas-wael-amana-amana-assistant/cf7235bd-03e5-456e-8948-a8c2229a57bd/scratchpad/charts/LITE.png`.
  It shows the wick through the 200-DMA and the V back into the 881–897 band, under a rolling 20/50.

### Zone checks — `levels.py LITE --zone … --size 190 --sleeve 3426` (10:52 ET data)
```
# 1. 200-DMA + 8/11–8/24 lows (the old "best support"), stop under the 7/7 low, T1 = 7/23 swing high
  Setup: zone 784.00–800.00, stop 680.00, T1 897.00
    at low     784.00: R/R 1.09:1, stop 1.54 ATR (13.3%)   ✘ R/R < 2
    at mid     792.00: R/R 0.94:1, stop 1.66 ATR (14.1%)   ✘ R/R < 2
    at high    800.00: R/R 0.81:1, stop 1.78 ATR (15.0%)   ✘ R/R < 2
    size $190 ≈ 0.2399 sh at the mid; risk to stop $26.87 = 0.8% of $3,426   ✓ ≤ 2%
# 2. May lows 845–855, stop under the 10/23 low
  Setup: zone 845.00–855.00, stop 735.00, T1 897.00
    at low     845.00: R/R 0.47:1, stop 1.63 ATR (13.0%)   ✘ R/R < 2
    at mid     850.00: R/R 0.41:1, stop 1.70 ATR (13.5%)   ✘ R/R < 2
    at high    855.00: R/R 0.35:1, stop 1.78 ATR (14.0%)   ✘ R/R < 2
# 3. Same, generous T1 (skips 897 and both falling MAs)
  Setup: zone 845.00–855.00, stop 735.00, T1 970.32
    at low     845.00: R/R 1.14:1, stop 1.63 ATR (13.0%)   ✘ R/R < 2
    at high    855.00: R/R 0.96:1, stop 1.78 ATR (14.0%)   ✘ R/R < 2
```
**No zone passes.** The arithmetic: 1.5 ATR = **$101**, so T1 must sit **≥ $203 (3 ATR)** above the zone top. Below
**$675** even the stop band is empty, because 1.5 ATR would exceed the 15% hard exit.

**What would create a zone:**
- **(a)** A post-report close above **$1,143** (the record; no overhead swing high), with a measured-move T1 written
  first and the chase guard passing.
- **(b)** ATR falls to ≈ 4% (≈ $35) and a new base forms with ≥ 3 ATR to the next swing high.

Neither is likely before mid-November.

### Earnings preview (section A) — not held
1. **Date/time:** Thu **11/5 after the close**, webcast 5:00 ET (Lumentum IR, 10/5). COHR reports 11/4 AMC (24/7 Wall St
   via search, unverified), which gives a read-across the day before.
2. **Consensus:** **$1.25B revenue / $4.22 EPS** (MarketBeat, fetched 10/28; search summary $4.21). That is the guide
   midpoint: revenue $1.225–1.275B, non-GAAP op margin 39.5–40.5%, EPS $4.05–4.35 (8/11). It has beaten EPS in 6 of the
   last 8 quarters (MarketBeat). The metrics that move it are the FQ2 revenue guide, OCS revenue (≥ $100M was expected
   for FQ1 per the 10/15 entry, not re-fetched) and CPO timing. Alpha Vantage's 3.82 is stale.
3. **Implied move:** **±13.33%** (weekly, 11/6 expiry; monthly ±17.25%; optionslam 10/28) ≈ **±$118 → $769–1,006**. On
   a $190 starter that is ≈ $25. In August the implied move was 14.16% and the close-to-close +13.63%.
4. **Scenarios:**

   | Scenario | What has to happen | Likely reaction | Action written now |
   |---|---|---|---|
   | Bull | FQ1 > $1.275B, FQ2 guide clearly up, OCS/CPO pulled in | Gap +10–15% into $998–1,027 | No buy into the gap. A zone needs a close > $1,143 or a base with ≥ 3 ATR to T1 |
   | Base | In line, guide ≈ +10% q/q | ±7%, chop $820–950 | No zone; stays WATCH |
   | Bear | Miss, or a flat FQ2 guide | Gap −13% or worse, under the 200-DMA (≈ $815 by 11/6) toward 736/680 | Under the 200-DMA there are no fresh longs. Wait for a base and a reclaim |

5. **History** (close-to-close / opening gap, levels.py Yahoo bars): 11/5/25 **+23.6% / +16.0%** · 2/4/26 **+7.0% /
   +8.7%** · 5/6/26 **−5.1% / +0.1%** · 8/12/26 **+13.6% / +9.6%**. Three of four were up. (The 11/4/25 and 2/3/26
   report dates are inferred from the gaps.)
6. **Decision:** not held. No pre-report day is open: the client freeze runs to 11/2 and the blackout covers 11/2–11/5.
   Run `levels.py LITE` after the **11/6 close**. 11/6 is a jobs-report morning, so the earliest buy is the 11/6
   afternoon, realistically **11/9**.

### Thesis scorecard (section B)
| Pillar (falsifiable) | Expected | Status (dated) | Trend |
|---|---|---|---|
| FQ1 revenue ≥ guide low | ≥ $1.225B | consensus $1.25B (MarketBeat 10/28); report 11/5 | pending |
| Non-GAAP op margin in the 39.5–40.5% guide | ≥ 39.5% | FQ4 36.6% (10/15 entry); test 11/5 | improving (guided) |
| Demand sold out into 2029 | CEO 10/8–10/9 | restated in 24/7 coverage 10/26 | stable |
| No new equity; net cash ≥ $1B | yes | net cash $1.07B, shares +7.2% y/y (stockanalysis 10/28); no 8-K/S-3 since 10/6 (EDGAR) | stable |
| Multiple holds while growth delivers | ≈ 39× FY27 (10/15) | forward P/E 41.1 (10/28) | richer |

**Thesis-break exits:** FQ1 revenue under $1.225B · a FQ2 guide flat or down q/q · a change to the NVIDIA purchase
commitment. **Conviction:** Med. Up if FQ2 guides ≥ +10% q/q with margins in range; down on a guide that only flattens.

### Fundamentals (stockanalysis statistics, 2026-10-28 11:04 ET, unless noted)
- Market cap **$81.07B**, EV $80.00B. **Forward P/E 41.1**, P/S 26.5, forward P/S 12.6.
- TTM revenue $3.01B, GM 44.2%, GAAP op margin 17.8%, FCF $300.1M. **Net cash $1.07B** (cash $2.74B, debt $1.67B).
  Shares 90.58M, **+7.18% y/y**.
- **Data oddity:** stockanalysis shows a **TTM net loss of −$6.94B (EPS −$92.96)**. The page does not explain it.
  Probably a non-cash mark on the converts or the NVIDIA preferred, but this is **unverified**. GAAP P/E is not
  meaningful.
- FQ1'27 guide (8/11 release, via Stocktitan): revenue $1.225–1.275B, non-GAAP op margin 39.5–40.5%, EPS $4.05–4.35.

### News & catalysts (last 30d / next 90d)
- 2026-10-28 — neutral — +2.4% to $887; today's high 897.99 is at the 7/23 swing high (897.00).
- 2026-10-26 — confirming (sentiment) — **StoneX initiates Buy, PT $1,200**. LITE +8% intraday, AAOI and COHR +6%
  (24/7 Wall St, 10/26). The article blames the prior slide on "questions about how customers will fund large AI
  infrastructure projects".
- 2026-10-22 — neutral (sector) — optics sell-off "as tech selloff deepens": COHR −12%, AAOI −10%, LITE −9% intraday
  (24/7 Wall St headline, 10/22); LITE closed **−11.5%**. It followed Meta's 10/21 print (Q3 capex $34.9B > operating
  cash flow; FY26 capex $135–145B).
- 2026-10-05 — neutral — report date set: 11/5 AMC.
- **Next:** 10/28 FOMC + MSFT/GOOGL · 10/29 PCE + AMZN · 11/4 COHR · **11/5 LITE** · 11/6 jobs.

### Positioning & sentiment
- Short interest **7.45M = 8.26% of float** (up from 6.51M), 1.66 days (stockanalysis 10/28; settlement date not shown).
- Analysts **Buy (28)**, average PT **$1,166.28** (stockanalysis 10/28). StoneX $1,200 (10/26).
- Insiders: a run of Form 144s and Form 4s from 9/15 to 10/2, none since (EDGAR 10/28).
- Crowded, high-beta AI optics. A ±13% implied move on an $81B name is the crash profile the client wants to avoid.

### What would make me wrong
- A clean beat-and-raise that never pulls back. Acceptable: missing a winner costs less than a 2-ATR stop-out.
- A weekly close under the 200-DMA after the report, or a FQ2 guide that flattens, ends the thesis for this cycle.
- The 10/22–10/23 shakeout could prove to be the low. Even then, the rule needs a base and room to T1, not a hope.

### Sources
- `levels.py LITE` and zone checks, Yahoo chart API, quote 2026-10-28 10:52 ET. Chart PNG above
- [Lumentum IR: FQ1'27 reporting date](https://investor.lumentum.com/financial-news-releases/news-details/2026/Lumentum-Announces-Reporting-Date-for-Fiscal-First-Quarter-2027-Financial-Results/default.aspx) — 2026-10-05 (via search, fetched 10/28)
- [Stocktitan: FQ4'26 results and FQ1'27 outlook](https://www.stocktitan.net/news/LITE/lumentum-announces-fourth-quarter-and-full-fiscal-year-2026-k3q8m0wxnl6c.html) — 2026-08-11 (via search)
- [MarketBeat: LITE Q1 2027 earnings estimates](https://www.marketbeat.com/earnings/reports/2026-11-5-lumentum-holdings-inc-stock/) — fetched 10/28
- [optionslam LITE](https://www.optionslam.com/earnings/straddle/LITE) — fetched 10/28
- [stockanalysis LITE statistics](https://stockanalysis.com/stocks/lite/statistics/) — 10/28 11:04 ET
- [24/7 Wall St, 10/26: Lumentum jumps 8% as StoneX starts coverage](https://247wallst.com/investing/2026/10/26/lumentum-jumps-8-as-stonex-starts-coverage-with-1200-target-applied-optoelectronics-and-coherent-climb-6/)
- 24/7 Wall St, 10/22: "Optics Stocks Tumble as Tech Selloff Deepens Ahead of Earnings" (headline/teaser only; URL https://247wallst.com/investing/2026/10/22/optics-stocks-tumble-as-tech-selloff-deepens-ahead-of-earnings-coherent-tumbles-12-applied-optoelectronics-drops-10-lumentum-falls-9)
- EDGAR filing list, CIK 1633978 — fetched 10/28
- [Gotrade, 10/23: Meta Q3 capex/FCF](https://www.heygotrade.com/en/news/meta-meta-stock-news-october-23-2026/) (via search summary)

---

## LITE — update 2026-10-19

**Verdict:** WATCH, no zone · **Conviction:** Med on the business, Low on the setup. Unchanged from 10/15: at an 8% daily
range, no support pays 2:1 to the next resistance. Earliest buy **11/6**, after the **11/5** report.

| | |
|---|---|
| Price | **$853.19** (2026-10-19, 10:35 ET, +3.5%); close $824.13 (10/16); 10/15 low **$800.00** |
| 20 / 50 / 200-DMA | $983.3 / $930.9 (rising) / **$779.9** (rising) — price −8.3% under the 50, +9.4% over the 200 |
| RSI(14) · ATR(14) | 40.6 · **$69.26 = 8.1% a day** · −25.4% from the 10/9 high of $1,143 |
| Support / resistance | $784–800 (8/24, 8/11 and 10/15 lows; 200-DMA $780) / $876–894 gap, then $1,000–1,027 |
| R/R | At $790 with the $680 stop: 0.8:1 to $876 ✘, 2.0:1 to $1,000 (too far to be T1). At today's price ✘ |

**News (dated):** −9.8% on 10/12 to $995.41 (the Nasdaq-100's worst that day) and −7% intraday on 10/14, with no company
news: the Broadcom CEO's AI-funding remark and CoreWeave's bond stress. The FQ1 guide ($1.225–1.275B, 8/11) is the bar
for 11/5. LITE and AXTI are one indium-phosphide trade: hold at most one.

**Sources:** Yahoo chart API LITE 1y daily, fetched 2026-10-19 10:35 ET · [simpletechtrend, wk 42](https://www.simpletechtrend.com/en/post/optical-selloff-funding-vs-supply-2026-w42-en) · [24/7 Wall St, 10/14](https://247wallst.com/investing/2026/10/14/applied-optoelectronics-dives-9-as-ai-funding-fears-hit-optical-stocks-coherent-slides-7-lumentum-drops-7/) · [CMC Markets: FQ4 beat and FQ1 guide](https://www.cmcmarkets.com/en-au/opto/lite-stock-is-lumentums-q4-beat-enough-to-wow-investors) · earnings date per the 10/15 entry (Lumentum IR 10/5).

---

## LITE — Lumentum Holdings — deep dive 2026-10-15

**Verdict:** WATCH (no buy) · **Conviction:** Med on the business, Low on the setup. It is the best business of the three optical names, but this is the worst trade of the three. At this volatility there is **no zone at real support that pays 2:1** to the nearest resistance. Separately, the earnings blackout means no buy is allowed before **11/6**.

| | |
|---|---|
| Price | **$858.42** (2026-10-15, 11:10 ET, **−4.2%**; opened $845.00 on a −5.7% gap, low **$800.00**, high $859.97); close **$896.33** (2026-10-14, −9.3%) |
| 50-DMA / 200-DMA | **$931.7** rising (+$19.6 in 5 sessions) / **$775.2** rising (+$14.6 in 5 sessions). Price is **−7.9% under the 50-DMA**, **−2.0% under the 100-DMA ($875.7)**, −13.6% under the 20-DMA ($993.1) and **+10.7% above the 200-DMA** |
| 52-wk high / low | **$1,143.00 (2026-10-09)** / $152.54 (2025-10-22). Price is **−24.9% from the high** and **+463% from the low** |
| RSI(14) · MACD · ATR(14) | **39.8** (Wilder; was 62.6 on 10/9) · **bearish**: crossed under the signal line on 10/13, histogram −22.0 and widening · **$72.67 = 8.5% a day** |
| Entry zone | **None tradable.** The best real support is **$784–800**: the 8/24 low $784.47, the 8/11 low $787.01 and today's low $800.00. The rising 200-DMA is $775 today and ≈ $818 by 11/9 if the price stays flat. This zone **fails 2:1** (see R/R) |
| Invalidation (stop) | **$680**, at/under the 7/7 swing low $680.43. That is 1.43–1.65 ATR under the zone and −13.3% to −15.0% from it / or event: FQ1'27 revenue under the **$1.225B** guide low, a FQ2 guide that only flattens, a weekly close under the 200-DMA, or a cut to NVIDIA's purchase commitment |
| Target 1 / 2 | **$876–894 sell zone**: 100-DMA $875.7, 9/28 swing low $881.2, today's **open gap $860–894** and the 10/14 low $893.9 / **$1,000–1,027**: 9/22 high $1,002, 9/9 high $1,026.8, 20-DMA $993 |
| Reward/risk (T1) | **0.88:1 at $784 · 0.63:1 at $800 ✘**. At today's price: **0.14:1 ✘** (stop at −15%, $730). Even to T2: 2.1:1 at $784, 1.7:1 at $800, 0.8:1 today ✘ |
| Size | Would be a starter of **$190 ≈ 5%** of the sleeve. That is **0.221 sh** at $858 and 0.238–0.242 sh at $784–800. Risk to the $680 stop ≈ **$25–29 = 0.7–0.8%** of the sleeve. Size is not the problem. The R/R is |
| Timeframe | Months (the thesis runs on the 2026–28 InP laser, OCS and CPO ramp). **No action before the 11/5 report.** Re-derive the levels from fresh bars after it |
| Next earnings | **2026-11-05 after the close (confirmed, Lumentum IR 10/5)**, **15 sessions** away. Blackout **11/2–11/5**, so the 11/2 window is closed for LITE. Earliest buy is **11/6** (the reaction day), realistically the week of 11/9. Last 4 reactions, close-to-close: **+23.6%** (11/5/25) / **+7.0%** (2/4/26) / **−5.1%** (5/6/26) / **+13.6%** (8/12/26). Opening gaps: +16.0 / +8.7 / +0.1 / +9.6% |

### Thesis
Lumentum makes the **indium-phosphide (InP) laser chips** inside AI optical links: EMLs, CW lasers for silicon photonics, ultra-high-power lasers for co-packaged optics (CPO) and pump lasers. It also makes the **optical circuit switches (OCS)** used in AI clusters, plus transceivers (it bought CloudLight). It sits upstream of the module assemblers and buys its wafers from AXT.

- **Demand is not the question.** On 10/8–10/9 the CEO told Bloomberg TV that its optoelectronic parts are "effectively sold out through **early 2029**" (TIKR 10/9). Six months earlier he had said 2028. The Motley Fool (10/12) quotes it as "almost sold out" for 2029. He says the company cannot meet **≈ 70% of demand** for some products through next year, nor ≈ 30% for others through 2028. New laser capacity takes about **3 years** to reach customers.
- **Growth and margins are real.** FQ4'26 (Jun) revenue was **$1,006M, +109% YoY**. Non-GAAP gross margin was **50.4%** and non-GAAP operating margin **36.6%**. The FQ1'27 guide is **$1.225–1.275B (+134% YoY at the midpoint)** with a **39.5–40.5%** non-GAAP operating margin and **$4.05–4.35** EPS (8/11 release). OCS should pass **$100M in a quarter for the first time in FQ1**. CPO lasers ramp in **H2 CY2027**, with the first external light source (ELS) module order for delivery in H2 CY2027 (Zacks/MarketBeat call summaries, 8/11).
- **NVIDIA is inside the cap table.** It paid **$2.0B for 2.88M Series A preferred shares at $695.31** on 3/2/2026. They convert 1:1 and come with a multi-year purchase commitment and capacity rights (10-K, 8/17).
- **Why it fell 25% in 4 sessions:** there is **no company news** (24/7 Wall St, 10/14 and 10/15). It is a sector unwind:
  - 10/8: profit-taking.
  - 10/12: Broadcom's Hock Tan warned on AI funding and called parts of the market a "casino" (Fool 10/12).
  - 10/14: the Broadcom and Intel CEOs pointed to capital access and borrowing costs.
  - 10/15: rotation into defensives.

  LITE fell hardest because it had run hardest: the 10/9 all-time high came after a **+$300 run from the 9/28 low**.
- **The catch is the price.** The stock trades at **≈ 39× FY27 consensus EPS ($21.79)** and **≈ 24× FY28 ($36.02)**. Consensus needs FY27 revenue of **$6.3B (+110%)** and FY28 of **$9.95B**. The stock is priced for delivery and moves as a high-beta proxy for AI capex funding.

### Where it sits vs AXTI and AAOI
| | **LITE** | **AXTI** | **AAOI** |
|---|---|---|---|
| Place in the chain | InP **laser chips** + OCS + modules. Buys wafers from AXT | InP **wafers**, the bottleneck input (3 real suppliers) | Transceiver **assembler** in a crowded field |
| Gross margin | **47.4% GAAP / 50.4% non-GAAP** (FQ4'26) | 44.9% (Q2'26) | 27.7% GAAP (Q2'26) |
| Profit / cash | Non-GAAP operating margin 36.6%. FCF **$196M** in FQ4, **$300M TTM**. ≈ **$1.1B net cash** after $1.55B of converts at par | Profitable, ≈ $616M net cash | Operating margin −11%, burning cash |
| Funding | NVIDIA $2B preferred at $695 (3/26). Converts equitized in FY26. **No new equity or converts in the last 90 days** (EDGAR) | One raise at $64.25 (Apr) | Serial ATMs, ≈ $1.65B in 2026 |
| Customers | **Customer A 26.6%, B 15.0%** of FY26 revenue (not named). One customer = **30.4% of receivables** | None > 10% (Q2) | Top 3 = 92% |
| Valuation | **39× FY27 / 24× FY28 EPS** | ≈ 30× FY27 EPS (10/9) | ≈ 24× FY27 EPS (10/9) |
| What breaks it | De-rating of a 39× multiple on an AI-funding scare, a miss against a sold-out story, Chinese InP laser fabs | Beijing's export permits | Dilution, margins, execution |
| Desk status | **WATCH: no 2:1 zone, blocked until 11/6** | **Setup failed 10/15**: the low was $53.31, under the $54 stop level (journal 10/15). Re-derive after the 10/29 report | WATCH: zone failed |

**Ranking:** for the trade, none of the three has a live 2:1 entry on 10/15 (AXTI's broke this morning). For business quality, LITE ≥ AXTI > AAOI. **Owning AXTI and LITE together is one trade, not two.** Lumentum is an AXT customer paying $87M in deposits, and both names move on the same InP and AI-funding headlines. If AXTI is bought under the exception, LITE would be added optical concentration, not diversification.

### Chart & technicals (source: Yahoo v8 daily bars, 2y, pulled 10/15 11:10 ET; computed by the desk)
- **Structure.** From May to September the stock ranged **$595–1,085**. From the **7/29 low ($594.84)** it made higher lows: $787 (8/11), $784 (8/24), $819 (9/3), $832 (9/15), $881 (9/28). It then broke out to **$1,143 on 10/9**.
- **The breakout failed in one session.** Today's $800 low **broke the 9/28, 9/15 and 9/3 lows**, so the higher-low sequence is over. The first level that held is the 8/11–8/24 shelf ($784–787).
- **Momentum.** RSI is 39.8, not oversold. MACD crossed bearish on 10/13 and the histogram is still widening. Price is under the 20-, 50- and 100-DMA and above a fast-rising 200-DMA. The 200-DMA climbs ≈ $2.5 a day because the close 200 sessions ago was $372.61 (12/29/25).
- **Volume.** Down days ran heavier than the 50-day average (4.74M): **10/12 at 1.36×**, 10/14 at 1.20×, 10/8 at 1.03×. The 10/9 up day ran 1.11×. Today printed **3.60M by 11:10 ET**, already 0.76× a full day, so it is on pace for heavy volume. This is distribution, not capitulation yet.
- **Volatility.** In the last 250 sessions there were **17 days of +10% or more and 7 days of −10% or more**. ATR is 8.5%. Beta is 1.54 (5-yr). A 1.5-ATR stop is $109. For 2:1, the target has to sit **$218 or more above entry**, while the nearest resistance (gap $860–894) is only $60–110 above support. That gap is why no zone qualifies.
- **Supports.** $800 (today's low, round number) · **$784–787** (8/11, 8/24 lows) · $775 (200-DMA, rising) · $680–698 (7/7 low, the late-July gap/high) · $651 (7/17 low) · **$595** (7/29 low).
- **Resistances.** **$860–894** (today's open gap) · $876 (100-DMA) · $881 (9/28 low) · $932 (50-DMA) · $993–1,027 (20-DMA, 9/9 and 9/22 highs) · $1,085 (5/12 high) · $1,143 (10/9 all-time high).
- **Client rules.** The chase guard passes (RSI < 70, below the 50-DMA). The **falling-knife rule fails**: there is no higher low yet, and there is no close back above the broken $881–894 level.

### Fundamentals (company releases; FCF from stockanalysis cash-flow, 10/15)
| Quarter (end) | Revenue | YoY | GM GAAP / non-GAAP | Op margin GAAP / non-GAAP | Non-GAAP EPS | FCF |
|---|---|---|---|---|---|---|
| FQ1'26 (9/27/25) | $533.8M | +58% | 34.0% / 39.4% | 1.3% / 18.7% | $1.10 | −$18.3M |
| FQ2'26 (12/27/25) | $665.5M | +65% | 36.1% / 42.5% | 9.7% / 25.2% | $1.67 | $43.1M |
| FQ3'26 (3/28/26) | $808.4M | +90% | 44.2% / 47.9% | 21.6% / 32.2% | $2.37 | $79.1M |
| FQ4'26 (6/27/26) | **$1,006.3M** | **+109%** | **47.4% / 50.4%** | **27.8% / 36.6%** | **$3.23** | **$196.2M** |
| **FQ1'27 guide** | **$1.225–1.275B** | ≈ +134% | — | non-GAAP 39.5–40.5% | $4.05–4.35 | — |

- **Consensus** (stockanalysis, 10/12): FY27 revenue **$6.3B** (range $5.6–7.2B) and EPS **$21.79**. FY28 revenue **$9.95B** and EPS **$36.02**. FQ1'27 consensus is unverified.
- **Valuation now** (stockanalysis, 10/15):
  - Forward P/E **39.8**, against its own **22–60** range at quarter-ends since 9/2023. That is mid-range. It peaked at 60.0 in 12/2025.
  - Trailing EV/sales is **24.4**, the **top of its 3-year range** (2.5–24.4). Forward P/S is 11.9.
- **Peers** (stockanalysis, 10/15):

  | Peer | Forward P/E | Trailing EV/sales | Gross margin | Balance sheet |
  |---|---|---|---|---|
  | COHR | 26.3 | 7.5 | 37.5% | Net debt $1.56B |
  | CIEN | 33.4 | 8.0 | 44.1% | Net debt $0.44B |
  | FN | 20.9 | 2.9 | 12.0% | Net cash $0.87B |
  | AAOI | 36.2 | 12.8 | 28.9% | Operating margin −11% |

  LITE is the **most expensive name in the group** on both P/E and EV/sales. It also has the best margins.
- **Balance sheet (6/27/26).** Cash and short-term investments are **$2,738M**. Convertible principal is **$1,554M** and must be settled in cash: 2032 notes $1,265M, convertible at $187.77, with a capped call to $268.24; 2026 notes $54.8M due 12/15/26 at $99.29; the 2028 notes ($131.03) and 2029 notes ($69.54) are the rest. There are small yen term loans. **Net cash after converts at par ≈ $1.1B** (stockanalysis: $1.07B).
- **Dilution.** All converts are **deep in the money**. Above the cap, the 2032 notes alone add ≈ 4.6M net shares at $858. NVIDIA's preferred adds 2.88M.
  - Shares outstanding are **90.58M** (+7.2% YoY).
  - **Non-GAAP diluted shares were 101.1M** in FQ4, up from 72.2M in FQ3'25.
  - The **FQ4 GAAP net loss was −$7.16B**, driven by a $7.8B non-cash loss from equitizing converts. FY26 GAAP EPS was −$92.96 and non-GAAP EPS **$8.67**.
- **SBC** (including payroll taxes) was $50.1M in FQ4, **5.0% of revenue**, and $191.3M in FY26, **6.3%**. FY26 also had **$281M** of withholding-tax cash for net share settlement.

### News & catalysts
**Last 30 days**
| Date | Item | Tag |
|---|---|---|
| 9/28 | Citi raised its PT to $1,400 from $1,200 (Buy) | confirming |
| 9/30 | Bernstein initiated at Outperform, PT $1,220 | confirming |
| 10/5 | FQ1'27 report date set for **11/5 after the close** | neutral |
| 10/5 | Stifel PT to $1,232 from $1,100. Rosenblatt Buy, $1,300 | confirming |
| 10/6 | Proxy and annual report filed (DEF 14A / ARS) | neutral |
| 10/8 | Optics fell on profit-taking. LITE −5.6%. No company news | neutral |
| 10/8–9 | CEO on Bloomberg TV: **sold out through early 2029**; Greensboro fab added, 2nd Japan fab expanding. LITE +5.2%, all-time high $1,143 | confirming (demand) / breaking (it marked the top) |
| 10/12 | Broadcom's Hock Tan: AI funding / "casino" remarks. LITE **−9.8%**. Zacks cut to Hold | breaking (sentiment) |
| 10/14 | Broadcom and Intel CEOs on capital access and borrowing costs. LITE **−9.3%** | breaking (sentiment) |
| 10/15 | Rotation to defensives. LITE −4–5%, low $800 | neutral to breaking |
| 8/18–10/1 | Daily insider sales (Form 144s nearly every session) | breaking (supply) |

**Next 90 days**
| Date | Item | Tag |
|---|---|---|
| 10/28 | FOMC. No buys | neutral |
| 10/29 | PCE. AXTI reports (InP supply read-through) | read-through |
| ≈ 11/4–11/11 | Coherent FQ1 (date unconfirmed: Nasdaq 11/4, Earnings Whispers 11/11) | read-through |
| **11/5 after close** | **LITE FQ1'27**. Must land ≥ $1.25B and guide FQ2 up. The OCS > $100M quarter, CPO order book and capacity timing are the tells | binary |
| ≈ 11/5 | AAOI report (estimate) | read-through |
| ≈ 11/18 | NVIDIA FQ3 (estimate, unconfirmed). The AI-capex mood setter | read-through |
| 12/15 | 2026 notes mature ($54.8M, cash) | neutral |
| Open | Draft FCC ban on Chinese transceivers (Reuters via Dow Jones, 8/2026) helps US/Japan laser supply. Chinese InP laser fabs entering (risk flagged on the 8/11 call) | ± |

### Positioning & sentiment
- **Short interest:** **7.45M shares = 8.3% of float, 1.5 days to cover** (settlement 9/30, published 10/9; MarketBeat). That is **+14.3%** from 6.51M on 9/15. Benzinga showed ≈ 13% in June, so shorts have come down since then. Squeeze fuel is low.
- **Insiders:** in the last 6 months (4/15–10/15) there were **31 sales worth $96.8M and zero purchases** (OpenInsider):
  - EVP Retort sold $41.0M; he is retiring in October 2026 (8-K, 7/30).
  - Pres. Yuen sold $16.4M, in near-daily 500–2,000 sh sales from 8/20 to 9/28.
  - GC Kim sold $16.2M.
  - Directors sold ≈ $20M.
  - The CEO sold only $0.5M (8/27).

  This is steady distribution into strength. It is not a thesis signal on its own.
- **Analysts:**
  - MarketBeat: 23 ratings (16 Buy, 6 Hold, 1 Sell), **average PT $1,078.75**.
  - stockanalysis: 26 analysts, Buy, **average PT $1,179**, low $820, high $1,500 (10/12).
  - In the last 30 days PTs were **raised** (Citi, Stifel, Bernstein, Rosenblatt). There was **one downgrade** (Zacks to Hold, 10/12). No broker has cut since the sell-off began.
- **Crowdedness: high.** The stock is **+463% in a year**. It is a top holding of the photonics ETF (LYTE), carries the sector's highest multiple and trades in a group that falls together (COHR −7%, AAOI −6% today). Positioning is the reason the drop is fast. Today's drop is not information about the business.

### Potential — the honest range (12 months, from $858)
- **Bear $550–600 (−30% to −36%).** An AI-funding scare de-rates it to COHR's multiple: 26× FY27 $21.79 = **$567**. The **7/29 low is $595**. It has already done −45% (the June high to the 7/29 low) inside this bull run.
- **Base $900–1,080 (+5% to +26%).** It delivers the guide and the multiple drifts to 25–30× FY28 $36. That is in line with the MarketBeat average PT ($1,079).
- **Bull $1,300–1,400 (+50% to +63%).** A FY28 beat plus a CPO pull-forward, at ≈ 38× FY28. That matches the Citi and Loop PTs of $1,400.
- **The skew from here is roughly symmetric** (−$280 vs +$220 to +$540). After a −25% drop that is not a bargain; it is still priced for delivery. "It's on sale" is the client's known bias. The stock is still 10.7% above its 200-DMA and at 39× forward earnings.

### What would make me wrong
- **Missing a cheap entry.** If the 11/5 report beats ($1.3B+, FQ2 guide ≥ $1.5B) and the stock gaps back above $894 to $1,000, WATCH misses a +15–20% move. That is acceptable: the rules forbid holding a $190 starter through a ±10–25% binary 3 sessions after entry anyway.
- **A V-bottom.** $800 could be the low (a round number on a heavy flush). If it holds and the price closes back above **$894** with a higher low above $800, the falling-knife rule clears. But T1 then moves to $1,000–1,027 and the stop to ≈ $780–800, which still gives **< 2:1** from $900.
- **The other direction.** This is a de-rating of the whole group, not a pause. A weekly close under the rising 200-DMA (≈ $800–818 by early November) opens **$680 → $595**.
- **What would make the thesis wrong** (not the trade):
  - Customer A or B (41.6% of FY26 revenue) cuts or delays orders.
  - Chinese InP laser fabs win EML or CW share.
  - The FQ1 gross margin stalls near 50% while capex climbs.

### Sources
- Yahoo Finance chart API, LITE 2y daily + 1d intraday — https://query1.finance.yahoo.com/v8/finance/chart/LITE?range=2y&interval=1d — pulled 2026-10-15 11:10 ET
- Lumentum IR, FQ1'27 report date (11/5 after the close) — https://investor.lumentum.com/financial-news-releases/news-details/2026/Lumentum-Announces-Reporting-Date-for-Fiscal-First-Quarter-2027-Financial-Results/default.aspx — 2026-10-05
- FQ4/FY26 results + FQ1'27 guide — https://seekingalpha.com/pr/20615640 — 2026-08-11
- FQ3'26 results (8-K ex99.1) — https://www.sec.gov/Archives/edgar/data/0001633978/000162828026030530/lite_ex991xq3fy26.htm — 2026-05-05
- FQ1'26 results — https://www.businesswire.com/news/home/20251104859713/en/Lumentum-Announces-First-Quarter-of-Fiscal-Year-2026-Financial-Results/ — 2025-11-04
- FQ2'26 results / reaction — https://www.itiger.com/news/1147150881 and https://www.nasdaq.com/articles/why-lumentum-lite-462-last-earnings-report — 2026-02-03/04
- FY26 10-K (customers, converts, NVIDIA preferred, capped call, shares) — https://www.sec.gov/Archives/edgar/data/0001633978/000162828026057358/lite-20260627.htm — 2026-08-17
- 8-K Item 5.02 (Retort retirement) — https://www.sec.gov/Archives/edgar/data/1633978/000162828026051078/lite-20260727.htm — 2026-07-30
- EDGAR filing index (no equity/convert 8-K in last 90 days) — https://data.sec.gov/submissions/CIK0001633978.json — pulled 2026-10-15
- 2032 notes pricing — https://www.businesswire.com/news/home/20250903825830/en/Lumentum-Announces-Pricing-of-1.1-Billion-Convertible-Notes-Offering/ — 2025-09-03
- stockanalysis statistics (valuation, SI, PT) — https://stockanalysis.com/stocks/lite/statistics/ — 2026-10-15
- stockanalysis quarterly financials / cash flow / ratios — https://stockanalysis.com/stocks/lite/financials/?p=quarterly · https://stockanalysis.com/stocks/lite/financials/cash-flow-statement/?p=quarterly · https://stockanalysis.com/stocks/lite/financials/ratios/?p=quarterly — 2026-10-15
- stockanalysis forecast (FY27/FY28 consensus) — https://stockanalysis.com/stocks/lite/forecast/ — 2026-10-12
- Peers: https://stockanalysis.com/stocks/cohr/statistics/ · https://stockanalysis.com/stocks/cien/statistics/ · https://stockanalysis.com/stocks/fn/statistics/ · https://stockanalysis.com/stocks/aaoi/statistics/ — 2026-10-15
- MarketBeat short interest — https://www.marketbeat.com/stocks/NASDAQ/LITE/short-interest/ — settlement 2026-09-30, published 2026-10-09
- MarketBeat analyst actions — https://www.marketbeat.com/stocks/NASDAQ/LITE/forecast/ — pulled 2026-10-15
- OpenInsider LITE — http://openinsider.com/screener?s=LITE — pulled 2026-10-15
- TIKR, CEO "sold out through early 2029" — https://www.tikr.com/blog/lumentum-stock-jumps-ai-optical-components-sold-out-2029 — 2026-10-09
- Motley Fool, "Why Lumentum sank today" — https://www.fool.com/investing/2026/10/12/why-lumentum-sank-today/ — 2026-10-12
- 24/7 Wall St, optics 10/8 — https://247wallst.com/investing/2026/10/08/optics-stocks-tumble-as-profit-taking-cuts-into-big-yearly-gains-applied-optoelectronics-drops-9-coherent-falls-5-lumentum-slides-4/ — 2026-10-08
- 24/7 Wall St, optics 10/12 — https://247wallst.com/investing/2026/10/12/lumentum-falls-10-as-optics-selloff-hits-hardest-where-capacity-is-sold-out-applied-optoelectronics-drops-7-coherent-slides-7/ — 2026-10-12
- 24/7 Wall St, AI funding fears 10/14 — https://247wallst.com/investing/2026/10/14/applied-optoelectronics-dives-9-as-ai-funding-fears-hit-optical-stocks-coherent-slides-7-lumentum-drops-7/ — 2026-10-14
- 24/7 Wall St, rotation 10/15 — https://247wallst.com/investing/2026/10/15/optical-stocks-extend-slide-as-money-rotates-into-defensives-applied-optoelectronics-falls-6-coherent-drops-7-lumentum-slips-5/ — 2026-10-15 10:58 ET
- FQ4 call summaries (OCS > $100M, CPO H2 CY27, ELS order, "way behind" on lasers, Chinese InP fabs) — https://www.zacks.com/stock/news/2973530/lumentum-q4-earnings-call-focuses-on-ai-optics-ocs-npo-ramps · https://www.marketbeat.com/instant-alerts/lumentum-q4-earnings-call-highlights-2026-08-11/ — 2026-08-11/12
- InP / China / FCC draft (Dow Jones via iTiger) — https://www.itiger.com/news/2657610870 — 2026-08
- NVIDIA $2B preferred (8-K summary) — https://www.stocktitan.net/sec-filings/LITE/8-k-lumentum-holdings-inc-reports-material-event-c842dcf0e631.html — 2026-03-02
- COHR date — https://chartrow.com/quote/cohr/earnings · https://beta.earningswhispers.com/go/w/COHR ; NVDA estimate — https://www.wallstreethorizon.com/nvidia-earnings-calendar — pulled 2026-10-15 (unconfirmed)
- Desk files: research/AXTI.md (2026-10-14), research/AAOI.md (2026-10-09), PLAN.md v3

**Unverified:** FQ1'27 consensus EPS and revenue · options-implied earnings move · the names behind Customer A and B (NVIDIA and Google are not named in the 10-K) · the exact 2028 vs 2029 note split (≈ $234M combined) · Coherent and NVIDIA report dates · the annual meeting date · any CPO or OCS revenue split.
