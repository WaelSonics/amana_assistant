# PM — Philip Morris International — research log

One file per ticker; newest entry first. Each entry is dated; numbers are as of that date.

Entries:
- 2026-10-28 (deep dive, v5 trading-pot candidate, levels.py-checked)
- 2026-10-23 (deep dive, non-AI diversifier screen)

---

## PM — Philip Morris International — deep dive 2026-10-28

**Verdict:** WATCH. **This is a v5 trading-pot candidate and cannot be bought under v3**: PLAN §1 allows at most one non-AI
satellite, and TTWO holds it. The client has also committed to no buys or sells before 11/2. The board alert is **$184.90**
(zone $183.80–184.90). · **Conviction:** Med. The $184 band has held four times since August and Q3 beat. Against that, at
$203 PM is a crowded defensive trading at ≈ 22× next year's earnings, and no entry within 9% of the price pays 2:1.

| | |
|---|---|
| Price | **$203.04**, from levels.py at 2026-10-28 10:52 ET and still $203.04 at 11:07 ET (today's bar is partial). Last close $202.62 (10/27). The record is $210.45 (10/15) |
| Entry zone | **$183.80–184.90**. Set the board alert at **$184.90**, then buy with a market order. The band is made of levels.py swing lows: $184.36 (8/4), $184.11 (10/5), $184.00 (10/21) and $185.84 (9/21). Do not buy below $183.80: below that the band has broken. On 10/23 the zone was $183.80–185.30; the top is 40 cents lower now because T1 is the lower 10/27 high (checks below) |
| Invalidation (stop) | **$175.40**, under the 7/15 swing low of $175.76 (levels.py). That is 1.69–1.91 ATR and 4.6–5.1% under the zone. The thesis-break events are listed in the scorecard |
| Target 1 / 2 | **$204.00**: the 10/27 high, which with $203.71 on 10/26 forms the cap the price is sitting under now / **$205.20–210.45**: the 10/14–10/16 closes and highs, plus levels.py resistance at $207.76 (7/28) and $210.45 (the 10/15 record). Sell zone for ⅓: $204.00–210.45 |
| Reward/risk (T1) | **2.40 / 2.20 / 2.01 : 1** at the zone's low / mid / high (levels.py ✓). On the strict reading, T1 is the August–September range top at $195.22, which a fall to $184 would break back through. That gives **1.36 / 1.21 / 1.09 ✘** |
| Size | **$190** in one fill = 5.5% of the $3,426 sleeve, ≈ 1.03 sh at the mid. Risk to the stop is **$9.22 = 0.3%** (cap $69). It fits inside a v5 trading pot of 15% (≈ $514, at most 3 names) |
| Timeframe | Weeks to 3 months after a fill. The zone may never print |
| Next earnings | **≈ early February 2027, unverified.** levels.py: "not in the 3-month calendar". Q4'25 was reported on 2026-02-06 (10/23 entry). No buy in the 3 sessions before it |
| Earliest buy date | **None under v3**, and never before 11/2. If v5 is adopted on 12/31, the first session the trading pot opens (start date unverified), after the zone is re-derived: a zone older than two weeks is not tradable (PLAN §3b) |

**T1 convention (the same in all four 10/28 entries):** T1 is the bottom of the sell zone, which is the nearest real resistance
above today's price (PLAN §3b). The 10/23 PM and XLE alerts used the same rule. Each entry also shows the strict reading,
where T1 is the first shelf between the entry and today's price. On the strict reading, no zone passes for PM, XLE, RTX or PGR.

**levels.py, 2026-10-28 10:52 ET** (the only source of technicals in this entry)
```
PM  $203.04 (2026-10-28 10:52 ET); last daily bar 2026-10-28 close $203.04
  20/50/200-DMA  198.45 / 193.43 (rising) / 181.48 (rising)   price vs 50 +5.0%, vs 200 +11.9%
  RSI(14) 58.2   ATR(14) $4.97 = 2.4% a day   52-wk 142.11–210.45 (-4% from the high)
  Trend: above a rising 200-DMA
  Chase guard: ok
  Next report: not in the 3-month calendar (ETF, or more than 3 months away)
  Swing support below: 185.84, 184.36, 184.11   resistance above: 207.76, 210.45
```
**Zone checks, 11:07 ET**
```
$ levels.py PM --zone 183.80-184.90 --stop 175.40 --target 204.00 --size 190 --sleeve 3426
  Setup: zone 183.80–184.90, stop 175.40, T1 204.00
    at low     183.80: R/R 2.40:1, stop 1.69 ATR (4.6%)   ✓
    at mid     184.35: R/R 2.20:1, stop 1.80 ATR (4.9%)   ✓
    at high    184.90: R/R 2.01:1, stop 1.91 ATR (5.1%)   ✓
    size $190 ≈ 1.0306 sh at the mid; risk to stop $9.22 = 0.3% of $3,426   ✓ ≤ 2%
    price 203.04 is +9.8% above the zone — wait for the alert at 184.90

$ levels.py PM --zone 183.80-184.90 --stop 175.40 --target 195.22 ...     (strict reading)
    at low 1.36:1 ✘ · at mid 1.21:1 ✘ · at high 1.09:1 ✘

$ levels.py PM --zone 202.50-203.50 --stop 195.50 --target 204.00 ...     (buying today)
    at low 0.21:1 ✘ (stop 1.41 ATR) · at mid 0.13:1 ✘ · at high 0.06:1 ✘
```
For reference, the 10/23 zone ($183.80–185.30) still passes against T1 $205.20 (2.55 / 2.26 / 2.01). Against T1 $204.00, its
top fails at 1.89:1.

Chart: `levels.py PM --chart` (10/28, kept in the scratchpad, not the repo). It shows the 199–204 box under the 10/15
reversal bar, the zone sitting on the August–October lows just above the rising 200-DMA, and RSI in mid-range. It agrees with
the computed levels.

## What changed since the 10/23 entry
- **Price:** 10/22 close $201.74, then $199.47 (10/23), $201.87 (10/26), $202.62 (10/27) and $203.04 now. It has traded in a
  $199.3–204.0 box with no new high. Volume was 3.6–5.0M a day, below the 10/15 reversal's 8.0M. (Yahoo bars, levels.py cache.)
- **Volatility and averages:** ATR fell from $5.60 to **$4.97**: the 10/21 earnings bar is fading out of the average. RSI moved
  from 57.3 to 58.2. The 50-DMA rose from $192.32 to $193.43 and the 200-DMA from $180.66 to $181.48. (10/22 values come from
  the 10/23 entry.)
- **A new cap:** the 10/26–10/27 highs at $203.71–204.00. Using it as T1 trims the zone top by 40 cents. Everything else is
  unchanged: the same band, the same stop.
- **Analysts:** all moves were up or reiterations (dates and firms under News).
- **Consensus EPS:** $8.37 for 2026 and $9.09 for 2027 (stockanalysis, 10/28), against $8.40 and $9.14 (Yahoo, 10/22). The
  providers differ; the drift is small and downward.
- **Company news:** none found from 10/23 to 10/28.

## Thesis
None of PM's earnings depend on AI capex. Cigarette pricing (+8.9% in Q3) pays for the move into smoke-free products (IQOS, ZYN
and VEEV), which made up more than 40% of Q3 revenue (8-K, 10/21).

**The hedge:** in the 10/23 screen, PM rose on all three chip-crash days (+8.0% in total). Its 60-day correlation with the SOX
was −0.58 (data to 10/22; not re-measured today).

**The price:** the market already pays for this story, at ≈ 24× 2026 and 22× 2027 consensus EPS (my arithmetic on the 10/28
stockanalysis estimates).

**The trade:** the $184 band. The 10/21 earnings flush tested it and buyers defended it. The likeliest way back there is a chip
rebound that unwinds the defensive rotation, which is the scenario in which the hedge earns its keep.

## Q3 report (10/21): a summary, since there is no report before 11/10
**Results** (8-K Ex. 99.1, fetched 10/28):
- Net revenues **$11.4B**, +5.5% reported and +7.1% organic.
- Adjusted EPS **$2.36** (+5.4%). Reported EPS $2.12 (−4.9%).
- Smoke-free products were more than 40% of revenue, +6.3% organic.
- Combustible pricing +8.9%. Cigarette volume was flat at 158.0B units.
- Heated-tobacco units (HTU) were 41.5B (+1.5%). U.S. ZYN shipped 3.2B pouches (+4.2%).

**2026 guide:**
- Adjusted EPS **$8.29–8.44**, or $8.11–8.26 excluding currency (+7.5% to +9.5%).
- Organic operating-income growth of 7–9%, "middle or lower half" of the range.
- Operating cash flow ≈ $13.5B. Capex $1.4–1.6B.
- Dividend +8.8%, to $1.60 a quarter.

**Against expectations:** a beat of ≈ $0.04 per GuruFocus (search summary, 10/21). The 10/23 entry had ≈ $2.29–2.30 expected,
which is a small conflict between sources.

**Reaction** (Yahoo bars): the stock opened −6.4% at $187.14, touched $184.00 and closed −1.2% at $197.46. It is +2.8% since.

**Already known from the call** (10/23 entry, not re-fetched):
- Q4 U.S. operating income is guided to about zero.
- The ZYN 20-pouch can sells at the same price, ≈ 25% less revenue per pouch.
- The 2027 guide comes in February.

**Peer read:** Altria reports Q3 on 10/29 before the open (Alpha Vantage calendar in levels.py's cache; EPS estimate $1.51).

## Thesis scorecard
| Pillar (falsifiable) | What was expected | Status (dated) | Trend |
|---|---|---|---|
| Smoke-free products keep growing | ≥ 6% organic; the 2026–28 target for total organic revenue is +6% to +8% | Q3: smoke-free +6.3%, total +7.1% (10/21) | stable |
| U.S. ZYN volume grows | volume up year on year | Q3: 3.2B pouches, +4.2% (10/21). Q4 U.S. operating income guided to ≈ 0 (call, per the 10/23 entry) | weakening |
| Cigarette pricing funds the shift | pricing ≥ 5% with volume about flat | Q3: pricing +8.9%, volume flat at 158.0B (10/21) | stable |
| EPS growth excluding currency | +9% to +11% a year (2026–28 target) | 2026 guide: +7.5% to +9.5% excluding currency (10/21), below the multi-year target | weakening |
| Dividend growth | raised every year | +8.8% to $1.60 (10/21) | stable |

**Thesis-break exits.** Any one of these ends a position whatever the price; in the trading pot they sit next to the $175.40 stop.
1. The February 2027 guide puts 2027 EPS growth excluding currency below 9%, or the 2026–28 targets are withdrawn.
2. U.S. ZYN shipments fall year on year in Q4 2026 or Q1 2027.
3. A federal or FDA action removes ZYN authorizations or flavours, or PM cuts the dividend.

**Disconfirming evidence:**
- The 2026 guide has been trimmed twice for currency.
- The Q4 EPS estimate slid from $1.96 to $1.90 (10/23 entry).
- 4 of the 16 analysts rate it Hold, and the low target is $175 (stockanalysis, 10/28).
- GuruFocus's GF Value is $170.25, which it calls overvalued (search summary, undated; it quotes a price of $201.48).

**Conviction:** Med. A 2027 guide at or above 9% excluding currency, with ZYN growing, would raise it. A Q4 ZYN volume decline
would cut it to Low.

## Chart & technicals
Source: levels.py, 10/28 10:52 ET. Recent bars come from the Yahoo daily bars levels.py caches.
- **Trend:** the price is above a rising 50-DMA ($193.43) and a rising 200-DMA ($181.48), and above the 20-DMA ($198.45). It is
  +5.0% over the 50-DMA and +11.9% over the 200-DMA.
- **Chase guard:** passes (RSI 58.2, +5.0% over the 50-DMA). Today's price is blocked by reward/risk, not by the chase guard:
  0.13:1 at $203 (check above).
- **Volatility:** ATR **$4.97 = 2.4%** a day, so 1.5 ATR = $7.46. The 52-week range is $142.11–210.45, and the price is 4% under
  the high.
- **Swing lows (levels.py, 6 months):** 6/2 $170.00 · 6/22 $172.29 · 7/15 $175.76 · 8/4 $184.36 · 8/12 $184.02 · 9/8 $181.01 ·
  9/21 $185.84 · 10/5 $184.11 · 10/21 $184.00.
- **Swing highs:** 5/19 $193.05 · 6/16 $186.22 · 7/7 $189.70 · 7/28 $207.76 · 8/26 $196.66 · 9/16 $195.49 · 9/30 $195.22 · 10/15
  $210.45.
  - The 8/26, 9/16 and 9/30 highs ($195.2–196.7) are the August–September range top. They broke on 10/8, and those levels are
    the strict-reading T1.
  - levels.py does not yet list the 10/26–10/27 highs ($203.71 / $204.00): a swing needs five bars after it.
- **The 200-DMA is closing in.** It rises about $0.19 a session (from $177.59 twenty sessions ago, levels.py JSON), which puts it
  near $184 by mid-November (projection).
  - If the zone fires after that, the fill sits under a rising 200-DMA. levels.py would then print "no fresh longs"; the
    protocol blocks only a falling 200-DMA.
  - This needs a desk call before any buy.

## Fundamentals
- **Valuation** (stockanalysis, 10/28):
  - Market cap $316.19B. P/E 29.61 trailing and 23.18 forward; EV/EBITDA 17.74.
  - Yield 3.16% ($6.40 a year). The payout is 93.42% of GAAP EPS.
  - Free cash flow over the last 12 months: $13.60B.
- **Balance sheet** (stockanalysis, 10/28):
  - Debt $47.73B and cash $6.69B, so net debt is $41.04B.
  - Shares outstanding +0.13% year on year (no buybacks).
- **Consensus** (stockanalysis, 10/28):
  - EPS: 2026 $8.37 (range $8.29–8.59) and 2027 $9.09.
  - Revenue: 2026 $43.58B and 2027 $45.63B.
- **On consensus EPS** (my arithmetic): **24.3× 2026 and 22.3× 2027**. The 10/23 entry put PM's five-year mean at 17.9×
  next-12-month EPS (TIKR; not re-fetched).

## News & catalysts
**Last 30 days**
- 10/2: ex-dividend date (10/23 entry). *Confirming.*
- 10/15: key reversal from the $210.45 record (10/23 entry). *Breaking (technical).*
- **10/21:** Q3 beat, Q4 guided soft, guide trimmed for currency. *Neutral.*
- 10/22: UBS Hold, target $193 → $201. Stifel Buy, $205 maintained (stockanalysis). *Neutral.*
- 10/23 or 10/26: Argus Buy, target $210 → $220. stockanalysis dates it 10/23; a GuruFocus/Defense World search summary dates
  it 10/26. *Confirming.*
- 10/28: Barclays Buy $225 and Goldman Sachs Buy $222, both reiterated (stockanalysis). *Confirming.*

**Next 90 days**
- 10/28: FOMC decision at 2:00 ET (desk). No trades today.
- 10/29: Altria Q3 (peer read on U.S. nicotine pouches and pricing).
- 11/3: U.S. midterm elections.
- Next dividend declaration and ex-date: unverified. The quarterly pattern points to late December.
- **Q4 results and the 2027 guide: ≈ early February 2027, unverified.** This is the thesis-break check.
- Background, already in the price: the FDA granted ZYN modified-risk orders for 20 products on 6/30/2026 (Moodie Davitt,
  7/1). IQOS ILUMA is still awaiting U.S. authorization (not re-checked this session).

## Positioning & sentiment
- **Analysts** (stockanalysis, 10/28): 16 analysts, consensus Buy. Price targets: average **$210.47**, median $215, range
  $175–230, which is +3.7% to the average. MarketBeat shows "Moderate Buy" with an average of $209.70 (search summary, undated).
- **Short interest:** 17.75M shares = 1.14% of float, 4.04 days to cover (stockanalysis, 10/28). No settlement date is given, and
  the figure matches the 9/30 data in the 10/23 entry, so it may be stale.
- **Insiders:** not re-checked. The 10/23 entry found no open-market trades in six months.
- **Crowding** sits in the valuation, not the momentum: RSI 58, but 22× next year's earnings in a defensive rotation (10/23 screen).

## What would make me wrong
- **The rotation lasts.** PM never returns to $184. The cost is small to T1 ($204.00 is +0.5% from here). A breakout over $210.45
  has no resistance above it, so the desk would have to write a T1 before any buy.
- **Chips rebound hard and PM gaps through the band.** If a fill at or above $183.80 is not available, skip it and re-derive. Do
  not move the stop.
- **A bounce from $184 stalls at $195–197,** the strict-reading T1, which pays only 1.1–1.4:1. The plan holds for T1 with the
  stop, but this is the realistic failure mode.
- **The 200-DMA rises into the zone by mid-November** (see Chart).
- **Events:**
  - ZYN loses share after the per-pouch price cut.
  - FDA or state action on pouch flavours.
  - A European tax on pouches or heated tobacco.
  - A February guide below 9% excluding currency.

## Sources
- levels.py (Yahoo chart API bars and quote; Alpha Vantage calendar). Runs: `levels.py PM` 2026-10-28 10:52 ET, zone checks and
  `--chart` 11:07 ET.
- PM Q3'26 8-K Ex. 99.1, fetched 2026-10-28 — https://www.sec.gov/Archives/edgar/data/0001413329/000162828026066596/earningsreleasepm-ex991xq3.htm (2026-10-21)
- stockanalysis PM forecast, 2026-10-28 — https://stockanalysis.com/stocks/pm/forecast/
- stockanalysis PM statistics, 2026-10-28 — https://stockanalysis.com/stocks/pm/statistics/
- GuruFocus, Q3 results (search summary) — https://www.gurufocus.com/news/9134194/philip-morris-international-pm-posts-strong-q3-results-but-shares-slip-on-us-sales-and-cost-concerns (2026-10-21)
- GuruFocus, Argus $220 (search summary; page 403) — https://gurufocus.com/news/9142464/pm-maintained-by-argus-research-price-target-raised-to-220
- Defense World, Argus (search summary; page 403) — https://www.defenseworld.net/2026/10/27/argus-issues-positive-forecast-for-philip-morris-international-nysepm-stock-price.html (2026-10-27)
- Moodie Davitt, ZYN MRTP orders — https://moodiedavittreport.com/?p=478087 (2026-07-01)
- 10/23 entry below, for the 10/22 values, the call notes and the screen statistics marked as such.

---

## PM — Philip Morris International — deep dive 2026-10-23 (non-AI diversifier screen)

**Verdict:** WATCH. From 11/2, buy only in **$183.80–185.30**, with an alert at **$185.30**. · **Conviction:** Med. The $184 band has held
four times since August, most recently when buyers absorbed the 10/21 earnings flush at $184.00. At $201.74, though, PM is a crowded
defensive trade near its highest multiple in five years, and the best rule-compliant buy today pays 0.3:1.

| | |
|---|---|
| Price | **$201.74**, close Thu 2026-10-22 (+2.2%). Record high **$210.45** intraday on 10/15. Earnings-day low **$184.00** on 10/21. No Friday 10/23 bar yet |
| Entry zone | **$183.80–185.30** from 11/2. This is the $184–186 support band: lows of $184.36 (8/4), $184.02 (8/12), $184.11 (10/5) and $184.00 (10/21). **Alert at $185.30**, then a market order. Do not buy below $183.80, because the stop would then sit less than 1.5 ATR away. The zone is 8.5% below the 10/22 close |
| Invalidation (stop) | **$175.40**, under the 7/15 swing low ($175.76) and the 200-DMA ($180.66 on 10/22, ≈ $182 by 11/2 if the price stays flat). At the zone mid that is $9.15 = **1.63 ATR** = 5.0% below the entry. The −15% hard exit (≈ $157) is below the stop. Event: Q4 U.S. ZYN shipments fall quarter on quarter, or the February 2027 guide comes in below the 9–11% ex-currency EPS growth target |
| Target 1 / 2 | **$205.20** (bottom of the sell zone: closes of $205.58 on 10/14 and $205.20 on 10/16, highs of $205.79–205.86) / **$210.45** (record, 10/15). Sell zone (⅓) is $205.20–210.45. There is no overhead resistance above it |
| Reward/risk (T1) | **2.26:1 at the zone mid of $184.55** ($20.65 / $9.15). It is 2.55:1 at $183.80 and 2.01:1 at $185.30. To T2 it is 2.83:1 at the mid |
| Size | First half: **$250 = 7.4%** of the $3,387 sleeve, or **1.35 sh** at $184.55. Risk is **$12.40** (0.37%). A full position is $500 (14.8%) = 2.71 sh, bought in two halves inside the zone on different sessions, for about $24.80 of risk (0.73%). The $68 risk cap would allow 7.4 sh, so the 8% and 15% weight rules are what limit the size |
| Timeframe | 1–3 months to T1 after a fill. The zone may never print |
| Next earnings | **≈ early February 2027, not confirmed.** Q4'25 was reported 2026-02-06, and management said 2027 guidance comes "in February". No buys in the 3 sessions before it |

## Thesis
- **Why it diversifies an AI-chip account:** none of PM's earnings depend on AI capex. They come from cigarette pricing (+8.9% in Q3)
  and from smoke-free products (IQOS, ZYN, VEEV), which are now more than 40% of revenue. I correlated daily returns with the SOX on
  Yahoo bars to 10/22: **−0.58 over 60 days**, −0.46 over 120 and −0.28 over 250. On the three chip-crash days PM gained +3.16% (10/14),
  +2.65% (10/16) and +2.17% (10/22), **+7.98% in total**. The hedge works both ways: on the SOX up days of 10/19 (+1.6%) and 10/21
  (+2.0%), PM fell 2.0% and 1.2%.
- **What the market may be missing:** Q4 is designed to be the low point for U.S. profit. PM is moving flagship ZYN from 15-pouch to
  20-pouch cans at the same price (about 25% less revenue per pouch), and Q4 U.S. operating income is guided to about zero. Meanwhile
  U.S. ZYN shipments rose 10% from Q2 to Q3, and management puts ZYN's offtake share up about 1.4 points from June to September. If
  those share gains hold, the 2027 comparisons are easy. Cigarette pricing is still paying for the investment.
- **Why only at $184:** the stock already prices that story. It trades at **22.0× next-12-month EPS against a five-year mean of 17.9×
  and a high of 23.8×** (TIKR, 10/22). The 3.17% yield is well below its five-year average of 4.25% (Yahoo). Staples are where money
  is hiding right now. The stock pays the plan's 2:1 only at the support band, and the most likely way it gets there is a rebound in
  chips (the negative correlation).
- VOO is already in the account and holds PM. A satellite position adds weight; it does not add a new exposure.

## Chart & technicals
All values are as of the 10/22 close (Yahoo daily bars).
- **Trend:** all three averages are rising. The 20-DMA is **$196.55** (+2.7% over 10 sessions), the 50-DMA **$192.32** (+1.4%) and
  the 200-DMA **$180.66** (+1.1%). Price is +2.6%, +4.9% and +11.7% above them. If the price stays flat, by 11/2 the averages are
  ≈ $200.5 / $194.1 / $182.0.
- **Momentum and volatility:** RSI(14) is **57.3**; it reached 68.7 on 10/14, the day before the record. ATR(14) is **$5.60 = 2.78%**,
  inflated by the 10/21 earnings bar (true range $15.90). It was $4.87 on 10/20, and its 120-day median is 2.66%. 1.5 ATR = $8.40.
- **Chase guard passes today:** RSI is under 70, and the price is 4.9% above the 50-DMA (under 20%).
- **52 weeks:** high **$210.45** (2026-10-15), low **$142.11** (2025-11-03). Price is −4.1% from the high and +25.8% YTD, against
  +11.9% for the S&P 500.
- **Key bars:**
  - **10/15, key reversal:** PM opened at a record $210.00 (+2.2%), touched $210.45, then closed at $199.90 (−2.8%) on 8.0M shares,
    1.7× the 50-day average of 4.5M. MO (+1.0%) and XLP (+0.7%) both rose that day, so the reversal was PM-specific. I found no
    company news that explains it.
  - **10/21, earnings:** a gap to $187.14 and a low of $184.00, then a close at $197.46 (−1.2%). The $184 band was bought hard.
- **Swing highs (6 months):** 5/19 $193.05 · 6/16 $186.22 · 7/7 $189.70 · 7/28 $207.76 · 8/26 $196.66 · 9/16 $195.49 · 9/30 $195.22 ·
  10/15 $210.45.
- **Swing lows (6 months):** 6/2 $170.00 · 6/22 $172.29 · 7/15 $175.76 · 8/4 $184.36 · 8/12 $184.02 · 9/8 $181.01 · 9/21 $185.84 ·
  10/5 $184.11 · 10/21 $184.00.
- **Support:** $199.3–199.9 (lows on 10/13, 10/15 and 10/20) · $196.6 (20-DMA) · $192.3 (50-DMA) · **$184.0–186.0** · $181.0 (9/8 low)
  and the 200-DMA · $175.8 (7/15 low).
- **Resistance:** **$205.2–205.9** (10/14 and 10/16) · $207.8 (7/28) · **$210.45** (record).
- **Why not buy at the averages:**
  - At $201.74 the stop has to sit at least $8.40 below, under the 50-DMA at $191.30. That pays $3.46 against $10.44 of risk, or 0.3:1.
  - At the 50-DMA (≈ $194 on 11/2) the stop goes under the $184 band at $183.40. That pays $11.20 against $10.60, or 1.1:1.
  - I tested every entry from $170 to $205 against these stops and T1 = $205.20. Only $183.80–185.30 (stop $175.40) and a sliver at
    $188.30–188.45 (stop $179.90) reach 2:1 at today's ATR. If ATR falls toward $5.10 by 11/2 (projection), the zone bottom
    extends to about $183.05.

## Fundamentals
- **Q3'26 (reported 10/21, before the open):**
  - Revenue **$11.44B, +5.5%** (+7.1% organic), against ≈ $11.32B expected.
  - Adjusted EPS **$2.36, +5.4%**, against $2.29–2.30 expected. Reported EPS was $2.12 (−4.9%), dragged by a non-cash fair-value
    hit on equity investments.
  - Adjusted operating income was $5.12B, a 44.7% margin.
  - Smoke-free products were more than 40% of revenue, up 6.3% organic. Combustibles were up 7.7% organic, with **pricing +8.9%**,
    on flat cigarette volume of 158.0B units.
  - IQOS HTU volume was 41.5B units (+1.5%). U.S. ZYN shipped 3.2B pouches (+4.2%, or +13% excluding the September 2025
    promotion). VEEV was up 61.6%.
- **U.S. segment (Q3):** revenue $845M and operating income $171M. SG&A was ≈ $370M and is guided about 10% higher in Q4. Q4 U.S.
  operating income is guided to "around zero or slightly negative" (TIKR and Investing.com call notes, 10/21–22).
- **2026 guide:**
  - Adjusted EPS is now **$8.29–8.44**, down from $8.35–8.50. The first guide in February was $8.38–8.53. Both cuts are
    currency-only; excluding currency the range is still $8.11–8.26 (+7.5–9.5%).
  - Organic operating income growth of 7–9% is now expected in the "middle or lower half" of the range.
  - Operating cash flow ≈ $13.5B and capex $1.4–1.6B, so free cash flow is ≈ $12B (my derivation).
  - The February 2026–28 targets: organic revenue +6–8% a year, operating income +8–10%, adjusted EPS excluding currency +9–11%,
    all with no buybacks.
- **Consensus (Yahoo, 10/22):** FY26 EPS $8.40 (15 analysts); FY27 $9.14 (+8.8%). The Q4'26 estimate is $1.90, down from $1.96
  30 days ago.
- **Valuation at $201.74:** **24.0× FY26 and 22.1× FY27** EPS, against Altria at 13.0× FY27 (Yahoo). EV/EBITDA 17.2×. Market cap
  ≈ $314B.
- **Balance sheet (Yahoo, most recent quarter):** debt $47.6B and cash $6.7B, so net debt is ≈ $40.9B, ≈ 2.0× TTM EBITDA of $20.5B.
  The target is "close to 2.0×" by the end of 2026. Book equity is negative.
- **Dividend:** **$1.60 a quarter** after an 8.8% raise ($6.40 a year = 3.17% yield). That is ≈ 76% of the FY26 adjusted EPS
  midpoint. The 10/2 ex-date has passed; the next one is unverified. No buybacks.

## News & catalysts
**Last 30 days**
- 9/23: UBS raised its target from $182 to $193 (Neutral). *Neutral.*
- 10/2: ex-dividend for the raised $1.60 dividend (+8.8%). *Confirming.*
- 10/8 (+4.1%) and 10/14 (+3.2%, a record close of $205.58): no company news; staples were bid in the rotation out of AI.
  *Neutral (crowding).*
- ≈ 10/10, NACS trade show: IQOS is sold only in Florida, Texas and Mississippi, and IQOS ILUMA is still under FDA review (2Firsts).
  *Neutral.*
- 10/15: key reversal from the $210.45 record. I found no PM-specific cause; PM published an EU economic-footprint study that day.
  *Breaking (technical).*
- 10/19: Goldman Sachs Buy, $222 target (secondary source, ad-hoc-news). *Confirming.*
- **10/21, Q3 results:** a beat, but the guide was trimmed for currency, operating-income growth was tilted to the lower half, the
  ZYN 20-pouch can cuts revenue per pouch by about 25%, Q4 is called a "unique quarter of investment", and there is no 2027 guide
  until February. The stock gapped down 6.4% and recovered to close −1.2%. *Neutral (a beat with a softer Q4).*
- 10/22: Needham raised its target from $215 to $220 (Buy); UBS from $193 to $201 (Neutral). *Confirming.*

**Next 90 days**
- The ZYN 20-pouch switch should be "largely complete" in Q4, with Q4 U.S. profit near zero. Already known.
- FDA decision on IQOS ILUMA: timing unverified. A U.S. ILUMA authorization would be a positive surprise.
- Macro: FOMC on 10/28; U.S. midterm elections on 11/3.
- Q4 results and the 2027 guide ≈ early February 2027 (not confirmed), just outside this window. Investor Day is in Q2 2027.

## Positioning & sentiment
All data is from 10/22 unless stated.
- **Analysts (Yahoo):** 16 ratings: 3 Strong Buy, 9 Buy, 4 Hold, 0 Sell, unchanged for three months. 15 price targets: mean
  **$210.13**, median $215, range $175–230, so **+4.2%** to the mean. MarketBeat shows 9 Buy / 2 Hold with an average of $207.56
  (search summary only).
- **Short interest:** 17.75M shares = **1.14% of float** (9/30), up from 16.59M (8/31). 4.0 days to cover. Not a crowded short.
- **Insiders:** no open-market buys or sales in six months. The only filings are director stock grants on 5/6 at $169.93.
- **Crowded defensive rotation? Yes, moderately.**
  - XLP is up 9.2% in a month to a 52-week high, including +3.3% on 10/22 alone.
  - PM is up 25.8% YTD against 11.9% for the S&P.
  - RSI was 68.7 the day before the record, and the multiple is near the top of its five-year range.
  - The "AI out, staples in" trade is the trade of the moment, so it is also the one that reverses when chips bounce.

## What would make me wrong
- **The rotation lasts:** if the market keeps selling AI capex for months, PM may break above $210.45 and never return to $184. The cost
  of waiting is small to T1 ($205.20 is +1.7% from the 10/22 close). A breakout has no overhead resistance, but it needs a desk decision
  on a target, because the 2:1 rule cannot be checked without one.
- **A gap through the zone:** chips rebound hard, the rotation unwinds, and PM gaps through $184 toward the 200-DMA (≈ $182) and the 7/15
  low ($175.76). If a fill at or above $183.80 is not available, skip the buy and re-derive the levels; do not move the stop.
- **Events:**
  - ZYN loses share after the per-pouch price cut.
  - FDA or state action on pouch flavours or strengths. A 2Firsts review flagged ZYN products shown at the NACS booth that are
    not on the FDA's authorized list.
  - A European tax on pouches or heated tobacco (timing unverified).
  - A 2027 guide in February below the 9–11% EPS growth target.

## Sources
- Yahoo chart API, PM, ^SOX, MO, BTI, XLP and ^GSPC 2y/1y daily bars, fetched 2026-10-23 01:12 EEST (18:12 ET on 10/22, after the
  close). RSI, ATR, moving averages, correlations and the entry scan are my calculations.
- Yahoo quoteSummary for PM and MO: estimates, targets, ratings, short interest (9/30), insider data and dividend. Fetched
  2026-10-23 01:15 EEST.
- PM Q3'26 8-K, Ex. 99.1: https://www.sec.gov/Archives/edgar/data/0001413329/000162828026066596/earningsreleasepm-ex991xq3.htm (2026-10-21)
- PM Q4'25 8-K, Ex. 99.1 (2026–28 targets, first 2026 guide): https://www.sec.gov/Archives/edgar/data/1413329/000162828026005932/earningsreleasepm-ex991xq4.htm (2026-02-06)
- Investing.com, Q3 call transcript: https://www.investing.com/news/transcripts/earnings-call-transcript-philip-morris-tops-q3-2026-estimates-shares-fall-93CH-4963512 (2026-10-21)
- TIKR, Q3 and the ZYN per-pouch cut, plus the P/E history: https://www.tikr.com/blog/philip-morris-beat-q3-then-handed-it-back-zyns-25-price-cut-explained (2026-10-22)
- Investing.com, UBS target $201: https://www.investing.com/news/analyst-ratings/ubs-raises-philip-morris-stock-price-target-to-201-on-earnings-beat-93CH-4966782 (2026-10-22)
- GuruFocus, Needham target $220: https://www.gurufocus.com/news/9136703/pm-maintained-by-needham-price-target-raised-to-220 (2026-10-22)
- ad-hoc-news, Goldman $222: https://www.ad-hoc-news.de/boerse/news/corporate-news/philip-morris-stock-goldman-sachs-sets-usd-222-00-target/70374652 (2026-10-19)
- Global Banking & Finance, the 10/15 drop: https://www.globalbankingandfinance.com/philip-morris-international-pm-falls-2026-10-15/ (2026-10-15)
- 2Firsts, PMI at the NACS show: https://www.2firsts.com/news/pmi-showcases-zyn-iqos-and-us-investments-at-nacs-show-2026 (≈ 2026-10-10)
- Business Wire, Q4'25 webcast date: https://www.businesswire.com/news/home/20260130069518/en/Philip-Morris-International-to-Host-Webcast-of-2025-Fourth-Quarter-and-Full-Year-Results (2026-01-30)
