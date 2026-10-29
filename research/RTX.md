# RTX — RTX Corp — research log

One file per ticker; newest entry first. Each entry is dated; numbers are as of that date.

Entries:
- 2026-10-28 (deep dive, watch only, levels.py-checked: no passing zone)
- 2026-10-23 (deep dive, non-AI diversifier screen)

---

## RTX — RTX Corp — deep dive 2026-10-28

**Verdict:** WATCH, watch only. It is neither a v5 compounder nor a trading-pot candidate, and it cannot be bought under v3. **No
zone passes the rules, so there is no board alert.** · **Conviction:** Low on timing; the business itself rates Med to High.
- The price sits on both its 50-DMA and its 200-DMA, and the 50-DMA is about to cross under the 200-DMA.
- Three fresh highs at $197.00–198.19 cap it.
- Every gap between its support and resistance shelves is about 2 ATR or less. A passing setup needs at least 3 ATR of clear air.

| | |
|---|---|
| Price | **$195.38**, from levels.py at 2026-10-28 10:52 ET ($195.82 at 11:07 ET). Last close $194.60 (10/27, −1.5%). Record **$226.88** (8/10); the low of the fall was **$179.02** (10/8) |
| Entry zone | **None passes** (the levels.py checks are below). (a) The post-earnings floor at **$188.00–189.30**, with the stop at $180.60 and T1 at $197.00, fails: **1.22 / 1.04 / 0.89 ✘**. The floor is made of the lows of 10/16 ($188.00), 10/20 ($188.08), 10/21 ($189.20) and 10/23 ($189.28); the stop sits under the 10/13 higher low of $181.15. (b) A retest of the 10/8 low at **$178.80–180.30**, with the stop at $172.00 (under the 6/3 swing low of $172.55) and T1 at $197.00, passes on R/R and ATR (2.68 / 2.31 / 2.01 ✓). But a fill there sits about 8% under the 200-DMA and under a falling 50-DMA, where levels.py's trend line says "no fresh longs". On the strict reading (the $188–189 floor becomes resistance) it pays about 1.1:1, so it is **not carried**. (c) Buying at today's price pays 0.19–0.36:1 ✘ |
| Invalidation | No position. For the thesis: a daily close under **$179.02** (the 10/8 low) means the decline has resumed |
| Overhead (T1 candidates) | **$197.00–198.19**: the 10/20, 10/26 and 10/27 highs, not yet levels.py swings · $196.3–202.7: the September shelf (the 9/2–9/11 bars) · **$203.94**: the 7/7 high, levels.py's first listed resistance · $205.4–207.8 and $213.5–214.5 (10/23 entry) · $221.34 / $226.41 / $226.88 (levels.py swing highs and the record) |
| Reward/risk (T1) | Fails above the 200-DMA on both readings (checks below) |
| Size | $0. If a setup appears: $190 in one fill, risk ≤ $69 |
| Timeframe | Re-check after the 11/3 midterms and again at the Q4 report |
| Next earnings | **≈ late January 2027, unverified.** levels.py: "not in the 3-month calendar". Q4'25 was reported on 2026-01-27 (10/23 entry). Peer: General Dynamics reports Q3 on 10/30 before the open (Alpha Vantage calendar in levels.py's cache) |
| Earliest buy date | **None.** There is no zone, and the name cannot be bought under v3 |
| What would create a zone | At least **3 ATR (≈ $13.50) of clear air** between a structural support and the next overhead high, above a rising 200-DMA. Today the largest gap between RTX's shelves is about $9 (≈ 2 ATR). Any of these would change that: (1) a daily close above the **$226.88** record, followed by a T1 the desk writes as a measured move, since the plan defines none; (2) the Q4 report and the 2027 guide redrawing the chart; (3) ATR falling under ≈ $2.8 while the $188–189 floor and the $197–198 cap both hold (it was $3.6–3.7 before earnings week, per the 10/23 entry, so this is unlikely soon) |

T1 convention: as in the 10/28 PM entry. T1 is the nearest real resistance above today's price (PLAN §3b), and the strict
reading is shown beside it. RTX fails on both.

**levels.py, 2026-10-28 10:52 ET** (the only source of technicals in this entry)
```
RTX  $195.38 (2026-10-28 10:52 ET); last daily bar 2026-10-28 close $195.38
  20/50/200-DMA  188.76 / 195.45 (falling) / 195.27 (rising)   price vs 50 -0.0%, vs 200 +0.1%
  RSI(14) 55.3   ATR(14) $4.50 = 2.3% a day   52-wk 166.74–226.88 (-14% from the high)
  Trend: above a rising 200-DMA
  Chase guard: ok
  Next report: not in the 3-month calendar (ETF, or more than 3 months away)
  Swing support below: 192.59, 190.02, 180.97   resistance above: 203.94, 221.34, 226.41
```
**Zone checks, 11:07 ET** (price $195.82, ATR $4.53)
```
$ levels.py RTX --zone 188.00-189.30 --stop 180.60 --target 197.00 --size 190 --sleeve 3426
  Setup: zone 188.00–189.30, stop 180.60, T1 197.00
    at low     188.00: R/R 1.22:1, stop 1.63 ATR (3.9%)   ✘ R/R < 2
    at mid     188.65: R/R 1.04:1, stop 1.78 ATR (4.3%)   ✘ R/R < 2
    at high    189.30: R/R 0.89:1, stop 1.92 ATR (4.6%)   ✘ R/R < 2
    size $190 ≈ 1.0072 sh at the mid; risk to stop $8.11 = 0.2% of $3,426   ✓ ≤ 2%

$ levels.py RTX --zone 178.80-180.30 --stop 172.00 --target 197.00 --size 190 --sleeve 3426
  Setup: zone 178.80–180.30, stop 172.00, T1 197.00
    at low     178.80: R/R 2.68:1, stop 1.50 ATR (3.8%)   ✓
    at mid     179.55: R/R 2.31:1, stop 1.67 ATR (4.2%)   ✓
    at high    180.30: R/R 2.01:1, stop 1.83 ATR (4.6%)   ✓
    size $190 ≈ 1.0582 sh at the mid; risk to stop $7.99 = 0.2% of $3,426   ✓ ≤ 2%
    → rejected on trend: ≈ 8% under the 200-DMA (195.27) and a falling 50-DMA; strict reading ≈ 1.1:1

$ levels.py RTX --zone 194.50-195.50 --stop 187.50 --target 197.00 ...     (buying today)
    at low 0.36:1 ✘ · at mid 0.27:1 ✘ · at high 0.19:1 ✘
```
For reference: even against levels.py's first listed resistance ($203.94), which would mean skipping the three fresh highs at
$197–198 (a fudged T1), the floor zone fails at its mid (1.90:1) and top (1.68:1).

Chart: `levels.py RTX --chart` (10/28, scratchpad). It shows the August–October fall, the double bottom at $179–181, the
bounce into the 50/200-DMA knot, and the falling 50-DMA about to cross under the flat 200-DMA. It agrees with the computed levels.

## What changed since the 10/23 entry
- **Price:** $194.71 (10/22), then:
  - $191.01 (10/23, −1.9%; the low of $189.28 retested the floor);
  - $197.48 (10/26, +3.4%; high $197.91);
  - $194.60 (10/27, −1.5%, after a high of $198.19; Boeing weakened on its results that day, per the desk);
  - $195.38 now.
- **The cross:** the 50-DMA fell from $197.70 to **$195.45** and is now $0.18 above the 200-DMA ($195.27, which levels.py calls
  rising). The cross the 10/23 entry projected for about 10/29 is imminent.
- **Other indicators:** 20-DMA $187.31 → $188.76; RSI 56.6 → 55.3; ATR $4.49 → $4.50.
- **New caps:** $197.91 and $198.19. Together with $197.00 they are now T1 for any entry below.
- **Analysts** (stockanalysis; consensus updated 10/26), all reiterations:
  - BofA Buy $235 (10/26), JPMorgan Buy $240 (10/22), Citi Buy $240 (10/21), Susquehanna Buy $245 (10/21).
  - Average target $229.17 across 24 analysts (10 Strong Buy, 6 Buy, 8 Hold), against $229.22 (Yahoo, 10/22).
  - EPS: 2026 $7.65 and 2027 $8.05, against $7.55 and $8.02 (Yahoo, 10/22).
- **Contracts new to this file** (mid-October):
  - An Air Force sole-source IDIQ for strategic communications terminals worth up to **$8B**, running through 10/12/2036. Only
    $0.8M was obligated at the award. Sources date the announcement 10/13 or 10/15 (search summaries of GovConWire and Virginia
    Business).
  - A **$729M** counter-drone export deal (search summary; date unverified).

## Thesis
RTX is the higher-quality business of the two non-staple names in the screen:
- the 2026 guide has been raised three times;
- the backlog is a record $340B (8-K, 10/20);
- management expects the munitions multiyears to add revenue from 2027 (10/23 entry).

Two things keep it from being a trade:
- **The hedge is weak.** Its SOX correlation was only −0.28 over 60 days and −0.02 over 250 (data to 10/22; not re-measured).
- **The chart offers no defined-risk entry.** The August–October fall left a shelf every $4–9 from $188 to $227.

VOO already holds RTX. Exposure without a swing setup would be a core decision, not a satellite trade.

## Q3 report (10/20): a summary, since there is no report before 11/10
**Results** (8-K Ex. 99, fetched 10/28):
- Sales **$25.0B** ($24,965M), +11% reported and +12% organic.
- Adjusted EPS **$2.26** (+33%), including **$0.25 of IEEPA tariff recovery**. GAAP EPS $1.89.
- Q3 free cash flow $2.12B, against $4.03B a year earlier.
- Backlog **$340B**: $176B commercial and $164B defense.

**Segments:**

| Segment | Sales | Growth | Adjusted margin (a year earlier) |
|---|---|---|---|
| Collins | $8,382M | +10% | 21.3% (15.7%) |
| Pratt & Whitney | $9,231M | +10% | 10.5% (8.9%) |
| Raytheon | $8,031M | +14% | 14.1% (12.2%) |

**2026 guide, raised:**

| | Prior | New |
|---|---|---|
| Sales | $95.0–96.0B | **$97.0–97.5B** |
| Organic growth | 8–9% | 10–11% |
| Adjusted EPS | $7.10–7.25 | **$7.65–7.75** |
| Free cash flow | $8.50–8.75B | $9.0–9.2B |

**Reaction** (Yahoo bars): opened +0.6%, traded $188.08–197.00, closed +0.6%. The stock is +1.1% since.

## Thesis scorecard
| Pillar (falsifiable) | What was expected | Status (dated) | Trend |
|---|---|---|---|
| The guide keeps rising | 2026 adjusted EPS raised each quarter | $7.65–7.75, up from $7.10–7.25 (10/20): the third raise | improving |
| The backlog converts | backlog grows faster than sales | $340B (10/20); sales +11% | improving |
| Cash conversion | the full-year FCF guide is met | Q3 FCF $2.12B against $4.03B; FY guide raised to $9.0–9.2B (10/20) | mixed |
| Earnings without one-offs | growth excluding IEEPA | Q3 includes $0.25 of IEEPA. Consensus 2027 EPS is only +5.2% over 2026 ($7.65 → $8.05, stockanalysis 10/28) | weakening |
| Defense funding | the munitions multiyears are funded | SM-6 and SM-3 multiyears awarded (10/1, 10/8; 10/23 entry). FY27 appropriations unverified | pending |

**Thesis-break exits.** Any one ends a position whatever the price:
1. The 2027 guide (≈ late January) implies flat or lower adjusted EPS once the IEEPA recovery drops out.
2. A new GTF powder-metal charge, or a wider fleet-inspection programme.
3. FY27 appropriations leave the munitions multiyears unfunded, or action under the January 2026 executive order on contractor
   payouts hits RTX.

**Disconfirming evidence:**
- Q3 free cash flow fell 47%.
- No buybacks in 2026 (10/23 entry).
- A Motley Fool author puts fair value at about $186, below the price (10/27).
- Insiders only sold in July and August (10/23 entry).

**Conviction:** Low on timing, Med on the business. A clean 2027 guide that excludes IEEPA would raise it. A guide with flat EPS
would end the case.

## Chart & technicals
Source: levels.py, 10/28 10:52 ET.
- **Trend:**
  - The price ($195.38) sits on the 50-DMA ($195.45, falling: it was $201.43 ten sessions ago) and the 200-DMA ($195.27, rising:
    it was $194.87 twenty sessions ago).
  - The 20-DMA ($188.76) is turning up.
  - This is not a "trend long" (rising 50 and 200) under the protocol.
- **Momentum and volatility:** RSI 55.3, chase guard ok. ATR **$4.50 = 2.3%**, so 1.5 ATR = $6.75 and 3 ATR = $13.50.
  52-week range $166.74–226.88.
- **Swing lows (levels.py):** 4/24 $171.63 · 5/5 $171.20 · 5/15 $170.78 · 6/3 $172.55 · 6/22 $180.97 · 7/10 $192.59 · 7/21
  $190.02 · 10/8 $179.02.
  - **The July lows levels.py lists as "support" ($192.59, $190.02) were broken in August and September.** They are not live
    support.
  - The live floor is $188.0–189.3 (October lows that are not yet swings) and $181.15 / $179.02.
- **Swing highs:** 5/11 $179.93 · 5/28 $181.55 · 6/18 $194.17 · 7/7 $203.94 · 7/28 $221.34 · 8/10 $226.88 · 8/19 $226.41.
  - Below $203.94 there are the September shelf (bars from 9/2 to 9/11, $196.3–202.7) and the three October highs ($197.00–198.19).
- **Volume** (Yahoo bars): 4.4–5.6M a day since 10/23, against 7.7–9.9M on the 10/16 bounce and the 10/20 earnings day. The
  push into the averages came on lighter volume.

## Fundamentals
- **Market and valuation** (stockanalysis, 10/28):
  - Market cap $264.41B. P/E 31.85 trailing and 25.24 forward. EV/EBITDA 17.23.
  - Yield 1.49% ($2.92 a year). Beta 0.31.
- **Balance sheet and cash** (stockanalysis, 10/28):
  - Debt $38.87B and cash $9.17B, so net debt is $29.70B. The 10/23 entry put net debt at ≈ $28.2B from the 10-Q; the
    definitions differ, likely leases.
  - Free cash flow over the last 12 months: $9.50B.
- **Consensus** (stockanalysis): EPS 2026 $7.65 (range $7.25–7.86) and 2027 $8.05. Revenue 2026 $97.41B and 2027 $104.91B.
- **On consensus** (my arithmetic): **24.3× 2027 EPS** and 25.4× the 2026 guide midpoint ($7.70).
- **Peers:**
  - FY27 P/E for Lockheed, General Dynamics and Northrop was 18–19× (10/23 entry; not re-fetched).
  - Motley Fool (10/27), on 2027 EV/operating income: Lockheed 13.8× and GE Aerospace 25.1×. The author blends them to 19.2×
    for RTX.

## News & catalysts
**Last 30 days**
- 10/1 and 10/8: SM-6 (up to $24.4B) and SM-3 IB (up to $6.3B) multiyear awards (10/23 entry). *Confirming.*
- Mid-October: the up-to-$8B strategic-communications IDIQ and the $729M counter-drone export deal. *Confirming*, though the IDIQ
  is a ceiling, not funded revenue.
- **10/20, Q3:** beat and raise, record backlog. *Confirming.*
- 10/21–10/26: target moves only up or reiterated (Barclays $235, UBS $212, Citi $240, Susquehanna $245, JPMorgan $240, BofA
  $235). *Confirming.*
- 10/26: +3.4% on defense strength. 10/27: −1.5% on the day Boeing weakened on its results (desk). *Neutral.*

**Next 90 days**
- 10/28: FOMC (desk).
- 10/29 or so: the 50/200-DMA cross, a likely "death cross" headline.
- 10/30: General Dynamics Q3 (peer read).
- **11/3: midterms.** Defense-budget headline risk.
- FY27 appropriations or a stopgap bill: status unverified.
- **≈ late January 2027: Q4 and the 2027 guide (unverified).** This is the thesis-break check.

## Positioning & sentiment
- **Analysts** (stockanalysis): 24 ratings (10 Strong Buy, 6 Buy, 8 Hold, 0 Sell). Average target **$229.17**, median $235,
  range $200–250: +17% to the average. MarketBeat shows "Moderate Buy" with $228.32 (search summary).
- **Short interest:** 13.65M shares = 1.09% of float, 3.44 days to cover (stockanalysis, 10/28). It is the same share count as
  the 9/30 figure in the 10/23 entry, so it may be stale.
- **Insiders:** not re-checked. The 10/23 entry found only sales, at $210–224, in July and August.
- **Not crowded:** defense was out of favour in the 10/23 screen (ITA −19% from its high).

## What would make me wrong
- **Upside.** Rising estimates plus a defense bid carry RTX through $198 and the September shelf toward $204–214 without a usable
  pullback. The 2:1 rule then keeps the account out of a 5–10% move. That is the accepted cost.
- **Downside:** a close under $179.02; a weak commercial-aerospace read-through from Boeing; budget headlines after the
  election; a 2027 guide with flat EPS excluding IEEPA.
- **Process risk:** the deep retest zone passes the arithmetic. If the desk decides that "under a still-rising 200-DMA" is allowed
  (the protocol blocks only a falling one), it could be carried, but on the strict reading it is a 1.1:1 trade.

## Sources
- levels.py (Yahoo chart API; Alpha Vantage calendar). Runs: RTX at 10:52 ET; zone checks and `--chart` at 11:07 ET (2026-10-28).
- RTX Q3'26 8-K Ex. 99, fetched 2026-10-28 — https://www.sec.gov/Archives/edgar/data/0000101829/000010182926000030/a2026-10x208xkerexhibit99.htm (2026-10-20)
- stockanalysis RTX forecast (consensus updated 2026-10-26) — https://stockanalysis.com/stocks/rtx/forecast/
- stockanalysis RTX statistics, 2026-10-28 — https://stockanalysis.com/stocks/rtx/statistics/
- Motley Fool, "RTX has a $340 billion backlog…", 2026-10-27 — https://www.fool.com/investing/2026/10/27/rtx-340-billion-backlog-trades-at-32-earnings/
- GovConWire, the $8B Air Force terminal contract (search summary) — https://www.govconwire.com/articles/raytheon-8b-air-force-strategic-communications-terminal-contract
- Virginia Business, the $8B award (search summary) — https://virginiabusiness.com/rtx-subsidiary-raytheon-8b-air-force-contract/
- Foreign Policy Journal, $8.7B combined with the counter-drone deal (search summary) — https://www.foreignpolicyjournal.com/2026/10/18/rtx-nyse-rtx-secures-8-7-billion-in-defense-contracts-strengthening-long-term-revenue-outlook/ (2026-10-18)
- heygotrade, the 10/27 close $194.60 (search summary) — https://www.heygotrade.com/en/us-stock/rtx/
- MarketBeat RTX (search summary) — https://www.marketbeat.com/stocks/NYSE/RTX/
- 10/23 entry below, for values marked as such.

---

## RTX — RTX Corp — deep dive 2026-10-23 (non-AI diversifier screen)

**Verdict:** WATCH, with no buy level that passes the rules on the 10/22 chart · **Conviction:** Low (on timing). The business is the
stronger of the two names in this screen: the guide has been raised three times this year and the backlog is a record $340B. The
chart is the problem. The August–October fall left a resistance shelf every $4–8 between $195 and $227. A structural stop at least 1.5
ATR away therefore never pays 2:1 to the next shelf; the best entry anywhere from $170 to $226 pays about 1.1:1.

| | |
|---|---|
| Price | **$194.71**, close Thu 2026-10-22 (+1.6%). Record high **$226.88** (8/10). Low of the fall **$179.02** (10/8). No Friday 10/23 bar yet |
| Entry zone | **None qualifies.** The obvious spot is the bottom of the post-earnings range, **$188.0–189.2** (lows of 10/16, 10/20 and 10/21). With a stop under the 10/13 higher low ($180.60), it pays **0.84:1** to the $195.2–197.7 shelf. I tested every entry from $170 to $226: the best is ≈ 1.1:1 |
| Invalidation (stop) | There is no position, so this invalidates the thesis rather than a trade: a daily close under **$179.02** (10/8 low) means the decline has resumed. If a setup appears later, the structural stop is **$180.60** (under the 10/13 low of $181.15), which is 1.76 ATR under $188.50 |
| Target 1 / 2 | These are resistance shelves, not targets: **$195.2–197.7** (200-DMA, the 10/20 high of $197.00, 50-DMA) · **$199.0–202.7** (the 9/2–9/8 shelf) · **$205.4–207.8** (February and April highs, late-August lows) · $213.5–214.5 · $221.3–226.9 |
| Reward/risk (T1) | **Fails.** At most ≈ 1.1:1 at any entry with a structural stop ≥ 1.5 ATR away. The plan needs ≥ 2:1 |
| Size | **$0.** If a level qualifies later, the first fill is ≤ $250 (7.4% of $3,387), or 1.32 sh at $190; the full position is ≤ $500 (14.8%) in halves |
| Timeframe | Re-check after the 11/3 elections. The next report (≈ late January) redraws the chart. Trigger below |
| Next earnings | **≈ late January 2027, not confirmed.** Q4'25 was reported 2026-01-27 and the date was announced on 1/6. The 2027 guide comes with it |
| Trigger | **A daily close above $226.88**, a new record with no shelves overhead, then re-derive. Even then T1 would have to come from a measured move, which the plan does not define: the desk must decide that before any buy. There is no buy trigger below that level on the current chart |

## Thesis
- **As a diversifier it is weaker than PM.** I correlated daily returns with the SOX on Yahoo bars to 10/22: **−0.28 over 60 days**,
  −0.19 over 120 and **−0.02 over 250**. The negative link is recent; over a year RTX is simply uncorrelated with chips. On the three
  chip-crash days it gained +1.89% (10/14), +3.73% (10/16) and +1.62% (10/22), **+7.24% in total**. On the chip up days of 10/19 and
  10/21 it fell 0.93% and 0.90%.
- **A real hedge mechanism the market may be missing:** management says printed circuit boards, capacitors and resistors are in short
  supply, partly because AI data centres are buying them (Q3 call, 10/20). Slower AI capex would ease RTX's supply chain, so the
  hedge rests on an operating link, not just on rotation flows.
- **Estimates rose while the stock fell.**
  - The midpoint of the 2026 EPS guide went from $6.70 (January) to $7.18 (July) to **$7.70 (October)**, +15%.
  - Consensus FY26 EPS rose from $7.08 to $7.55 in 90 days, and FY27 from $7.70 to $8.02 (Yahoo).
  - The stock is still −14% from its high. That de-rating came from the sector: fading Iran-war premium, tariff costs and
    midterm-election risk. RTX itself has not missed.
  - Multi-year munitions contracts worth about $70B (management) start adding revenue in 2027.
- **The bear case:**
  - 2026 EPS includes **$0.25 of one-off IEEPA tariff recovery**, so FY27 consensus growth is only +6.2%.
  - The stock trades at **24.3× FY27**, against 18–19× for Lockheed, General Dynamics and Northrop.
  - Q3 free cash flow fell 47% year on year.
  - There are no buybacks in 2026, and a January 2026 executive order may limit payouts by contractors the government judges to be
    underperforming.
  - Congress has not yet appropriated the money for the multi-year munitions deals (Defense News, 10/1).
- VOO is already in the account and holds RTX.

## Chart & technicals
All values are as of the 10/22 close (Yahoo daily bars).
- **Trend:**
  - RTX fell from the **$226.88** record (8/10) to **$179.02** (10/8), −21.1% in 42 sessions, then bounced 8.8% to $194.71.
  - The **20-DMA is $187.31** and turning up ($187.04 five sessions ago). The **50-DMA is $197.70** and falling (−3.0% in 10
    sessions). The **200-DMA is $195.16** and flat. Price is +3.9%, −1.5% and −0.2% from them.
  - If the price stays flat, the 50-DMA crosses under the 200-DMA around 10/29 (my projection). Expect "death cross" headlines just
    before 11/2.
- **Momentum and volatility:** RSI(14) is **56.6**, up from 19.1 on 10/7. ATR(14) is **$4.49 = 2.31%**, raised by earnings week; it was
  $3.6–3.7 before. The 120-day median is 2.31%. 1.5 ATR = $6.74.
- **Chase guard passes:** RSI is under 70 and the price is 1.5% under the 50-DMA.
- **52 weeks:** high **$226.88** (2026-08-10), low **$166.74** (2025-12-03). Price is −14.2% from the high and +6.2% YTD, against
  +11.9% for the S&P 500.
- **Volume:** buyers came in on the bounce. 10/16 (+3.7%) traded 7.7M shares and 10/20 (earnings) 9.9M, against a 50-day average
  of 4.4M.
- **Swing highs (6 months):** 5/11 $179.93 · 5/28 $181.55 · 6/18 $194.17 · 7/7 $203.94 · 7/28 $221.34 · 8/10 $226.88 · 8/19 $226.41 ·
  10/20 $197.00.
- **Swing lows (6 months):** 4/24 $171.63 · 5/5 $171.20 · 5/15 $170.78 · 6/3 $172.55 · 6/22 $180.97 · 7/10 $192.59 · 7/21 $190.02 ·
  10/8 $179.02 · 10/13 $181.15 (a higher low).
- **Support:** $188.0–189.2 · $187.3 (20-DMA) · $181.15 / $179.02 · $170.8–172.6.
- **Resistance:** $195.2–197.7 · $199.0–202.7 · $205.4–207.8 · $213.5–214.5 · $221.3–226.9.
- **Why no level qualifies:** the shelves are $4–8 apart, which is 1–1.8 ATR. A structural stop at least $6.74 away means risking
  $7–11, while the next shelf is $6–8 away, so the trade pays about 1:1. Clearing $197.7 does not fix it: the next shelves are at $199
  and $205. From a $190–194 entry, the stop under $188 would be too close for the 1.5 ATR rule, and one far enough away would sit
  under $181.

## Fundamentals
- **Q3'26 (reported 10/20, before the open):**
  - Sales **$24.97B, +11%** (+12% organic), against ≈ $24.0–24.2B expected.
  - Adjusted EPS **$2.26, +33%**, against $1.78 expected. That includes **$0.25 of IEEPA tariff recovery**. GAAP EPS was $1.89.
- **Segments (Q3):**

  | Segment | Sales | Growth | Adjusted margin | Notes |
  |---|---|---|---|---|
  | Collins | $8.38B | +10% | 21.3% | ≈ 3 points of the margin came from IEEPA |
  | Pratt & Whitney | $9.23B | +10% | 10.5% | Aftermarket +21%; reported operating profit $608M after a $363M charge for a customer bankruptcy |
  | Raytheon | $8.03B | +14% | 14.1% | |

- **Backlog:** **$340B**, +36% year on year ($176B commercial, $164B defense), up from $289B in Q2. Q3 awards were above $81B, including
  ≈ $23B for Tomahawk and more than $14B for AMRAAM.
- **Free cash flow:** Q3 $2.12B (against $4.03B a year earlier); year to date $6.31B (against $4.75B).
- **2026 guide, raised for the third time:**

  | | January | July | October |
  |---|---|---|---|
  | Sales | $92–93B | $95–96B | $97.0–97.5B (+10–11% organic) |
  | Adjusted EPS | $6.60–6.80 | $7.10–7.25 | **$7.65–7.75** |
  | Free cash flow | $8.25–8.75B | $8.50–8.75B | $9.0–9.2B |

  The 2027 guide comes in January. Management expects growth and wider margins but flagged the IEEPA comparison.
- **Valuation at $194.71:** **25.3×** the FY26 guide midpoint and **24.3×** FY27 consensus ($8.02). Trailing P/E 31.7×, EV/EBITDA
  17.4×. Free-cash-flow yield ≈ 3.5% (guide midpoint over a $262.7B market cap).
  - FY27 P/E of peers (Yahoo): Lockheed 18.0×, General Dynamics 18.8×, Northrop 18.3×, GE Aerospace 29.5×.
  - Against its own history: no five-year P/E series was fetched (**unverified**). As a proxy, the 1.50% yield is below its
    five-year average of 1.98% (Yahoo).
- **Balance sheet (9/30, 10-Q):** debt ≈ $37.4B and cash $9.17B, so net debt is ≈ $28.2B, ≈ 1.7× TTM EBITDA of $16.7B (Yahoo).
  1,349.4M shares outstanding.
- **Dividend and buybacks:** **$0.73 a quarter** ($2.92 a year = 1.50% yield). **No buybacks in 2026** (10-Q).
- **Not disclosed:** no new GTF powder-metal cost appeared in the Q3 release.

## News & catalysts
**Last 30 days**
- 9/23: Bernstein cut its target from $232 to $223 (Market Perform). *Neutral.*
- 9/24 (Yahoo): the stock was −15% from its high, blamed on ≈ $850M of tariff costs and a fading Iran-war premium as a ceasefire
  looked possible. *Breaking (sector).*
- 10/1: Navy SM-6 multi-year award worth up to $24.4B; quantities not disclosed, and Congress has not yet appropriated the funding.
  *Confirming.*
- 10/8: SM-3 Block IB multi-year award worth up to $6.3B. The stock bottomed at $179.02 the same day. *Confirming.*
- 10/9: TD Cowen cut its target from $240 to $225 (Buy); Barclays started coverage at Overweight with $223. *Neutral.*
- 10/15: RBC cut from $250 to $235 (Outperform) and Bernstein from $223 to $214. Bloomberg (headline and snippet only, paywalled):
  the aerospace & defense index is down ≈ 19% from its early-August high, and dip buyers are looking past the election. *Neutral.*
- 10/16: +3.7% on 7.7M shares as defense bounced; European defense stocks rose on Ukraine tensions. *Confirming.*
- **10/20, Q3 results:** a beat and a raise, with a record backlog. The stock traded from $188.08 to $197.00 and closed +0.6%
  (Benzinga showed it lower intraday despite the beat). *Confirming.*
- 10/21: Barclays raised from $223 to $235 (Overweight); UBS from $209 to $212 (Neutral). *Confirming.*
- 10/22: Lockheed rose 7.0% on a Q3 beat-and-raise and an F-35 framework deal; RTX +1.6%. *Confirming (sector).*

**Next 90 days**
- 11/3: U.S. midterm elections, which bring defense-budget headline risk.
- FY27 defense appropriations or a stopgap funding bill: status unverified.
- The likely 50/200-DMA cross around 10/29 (projection): a technical headline.
- Q4 results and the 2027 guide ≈ late January 2027 (not confirmed). The market will focus on the IEEPA comparison, cash conversion,
  and when Pratt & Whitney's new-engine sales grow again (Trefis, 10/19).

## Positioning & sentiment
All data is from 10/22 unless stated.
- **Analysts (Yahoo):** 24 ratings: 6 Strong Buy (up from 4 two months ago), 10 Buy, 8 Hold, 0 Sell. 23 price targets: mean
  **$229.22**, median $235, range $200–250, so **+17.7%** to the mean. October target moves were mixed: four cuts between 10/9 and
  10/15 before the report, two raises after it.
- **Short interest:** 13.65M shares = **1.01% of float** (9/30), up from 12.34M (8/31). 3.4 days to cover.
- **Insiders:** only sales, all at higher prices, and no open-market buys:
  - the general counsel sold 13.65k shares at $223.92 ($3.06M) on 8/18;
  - the treasurer sold 7.0k shares at $213.62–216.93 ($1.5M) on 7/28;
  - a director sold 2.29k shares at $218.05 on 7/27;
  - an officer sold 8.56k shares at about $210 on 7/24.
- **Crowded defensive rotation? No.** Defense is out of favour: ITA is 19.2% below its 52-week high and −4.8% YTD (10/22), and RTX
  is +6.2% YTD against 11.9% for the S&P. Beta is 0.31 (Yahoo). This is the uncrowded half of the screen, but the chart does not
  offer a defined-risk entry.

## What would make me wrong
- **Upside:** rising estimates plus a defense rotation could carry RTX through $197.7 and the shelves to $205–214 without a usable
  pullback. The 2:1 rule then keeps the account out of a 6–10% move. That is the known cost of the rule, and it is acceptable at
  this account size.
- **Downside:**
  - a daily close under $179.02;
  - election or budget headlines;
  - a 2027 guide with flat EPS once the IEEPA recovery drops out;
  - new GTF powder-metal costs;
  - action under the executive order on payouts.
- **Desk call needed:** if the client wants RTX exposure without a swing setup, that is a core decision outside the satellite rules.
  VOO already provides some of it.

## Sources
- Yahoo chart API, RTX, ^SOX, LMT, GD, NOC, GE, ITA and ^GSPC 2y/1y daily bars, fetched 2026-10-23 01:12 EEST (18:12 ET on 10/22,
  after the close). RSI, ATR, moving averages, the moving-average projection, correlations and the entry scan are my calculations.
- Yahoo quoteSummary for RTX and its peers: estimates and revisions, targets, ratings, short interest (9/30), insiders and dividend.
  Fetched 2026-10-23 01:15 EEST.
- RTX Q3'26 8-K, Ex. 99: https://www.sec.gov/Archives/edgar/data/0000101829/000010182926000030/a2026-10x208xkerexhibit99.htm (2026-10-20)
- RTX Q3'26 10-Q: https://www.sec.gov/Archives/edgar/data/0000101829/000010182926000031/rtx-20260930.htm (October 2026)
- Yahoo/Zacks, Q3 call highlights: https://finance.yahoo.com/markets/stocks/articles/rtx-q3-earnings-call-highlights-130000639.html (2026-10-21)
- Reuters via Investing.com, RTX raises its forecasts: https://www.investing.com/news/stock-market-news/rtx-lifts-2026-forecasts-as-aerospace-defense-demand-drives-record-backlog-4959691 (2026-10-20)
- Benzinga, the stock lower despite the beat: https://www.benzinga.com/markets/earnings/26/10/62473062/rtx-order-backlog-hits-record-340-billion (2026-10-20, search summary)
- Yahoo, the $4.3B cash hurdle: https://finance.yahoo.com/markets/stocks/articles/rtx-stocks-move-lower-ahead-171033429.html (2026-10-20)
- Yahoo, "why is the stock down 15%": https://finance.yahoo.com/markets/stocks/articles/rtx-289-billion-backlog-just-190645312.html (2026-09-24)
- Trefis, the P&W new-engine question: https://www.trefis.com/stock/rtx/articles/619187/rtx-stock-is-waiting-on-one-answer/2026-10-19 (2026-10-19)
- Defense News, SM-6 award: https://www.defensenews.com/industry/techwatch/2026/10/01/us-navy-awards-rtxs-raytheon-244b-for-sm-6-missiles-amid-stockpile-concerns/ (2026-10-01)
- RTX, SM-3 IB award: https://www.rtx.com/news/news-center/2026/10/08/rtxs-raytheon-awarded-6-3-billion-multi-year-contract-for-sm-3-ib-interceptors (2026-10-08)
- Bloomberg, the defense rout (headline only): https://www.bloomberg.com/news/articles/2026-10-15/defense-stock-rout-lures-dip-buyers-looking-past-election-risk (2026-10-15)
- 24/7 Wall St, Lockheed +9% and RTX +2%: https://247wallst.com/investing/2026/10/22/lockheed-martin-rises-9-as-record-backlog-lifts-outlook-rtx-gains-2-northrop-grumman-advances-3/ (2026-10-22)
- Fortune, the executive order on contractor buybacks: https://fortune.com/2026/01/13/trump-executive-order-defense-contractors-rtx-general-dynamics-lockheed-martin-boeing-northrop-grumman-l3-harris/ (2026-01-13)
- PR Newswire, the $0.73 dividend: https://www.prnewswire.com/news-releases/rtx-board-of-directors-declares-quarterly-cash-dividend-302812108.html (2026-06-26)
- RTX, Q4'25 date: https://www.rtx.com/news/news-center/2026/01/06/rtx-to-release-fourth-quarter-earnings-results-on-january-27-2026 (2026-01-06) · Nasdaq/Zacks, Q4'25 and the first 2026 guide: https://www.nasdaq.com/articles/rtx-q4-earnings-surpass-estimates-revenues-increase-y-y (2026-01-27)
