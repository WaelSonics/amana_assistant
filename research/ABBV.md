# ABBV — AbbVie — research log

One file per ticker; newest entry first. Each entry is dated; numbers are as of that date.

Entries:
- 2026-10-28 (deep dive, pre-report; v5-candidate refresh with levels.py checks)
- 2026-10-23 (deep dive, non-AI diversifier screen)

---

## ABBV — AbbVie — deep dive 2026-10-28

**Verdict:** WATCH. **v5 candidate, not buyable under v3.** Board alert **$266.30** (zone $265.00–266.30). It holds only if
the 10/30 report keeps the thesis, and only after the zone is re-run with the post-report ATR on 11/2.

**Conviction:** Low:
- **For:** strong execution and three positive pipeline events in a week.
- **Against:** at $287.95 it sits just under its record with RSI 67, and the average analyst target ($283.19) is below the
  price.
- **Against:** it tends to fall on its reports. Three of the last four closed down, and all four opened down.

| | |
|---|---|
| Price (date) | **$287.95** (levels.py, 2026-10-28 11:07 ET; intraday high $288.80). Close 10/27: $286.39 |
| Entry zone | **$265.00–266.30. Alert at $266.30** (unchanged from 10/23), then a market order. It is the old July–September ceiling ($266.97–269.39), just under the rising 50-DMA ($268.17; +$7.29 in ten sessions, ≈ $270 by 11/2) |
| Invalidation (stop) | **$255.00**, under the 10/2 swing low $257.87. That is 1.60–1.81 ATR, or 3.8–4.2%. Hard exit at −15% ≈ $226 (the stop comes first). **Event:** the thesis-break exits below |
| Target 1 / 2 | **T1 $289.00**: the 10/21 high, the bottom of the $289.00–291.40 band (10/26 $289.59, 10/20 $290.98, 10/15 record $291.40). **T2 $325**: a measured move, equal to the highest Street target (Barclays; 10/23 entry) |
| Reward/risk (T1) | **2.40 / 2.19 / 2.01 : 1** at the low / mid / high (levels.py, pasted below) |
| Size | One fill of **$190 = 5.5%** ≈ 0.72 sh. **Risk to the stop $7.62 = 0.2%** (cap $69) |
| Timeframe | weeks to months |
| Next earnings | **2026-10-30, before the open.** levels.py: 2 sessions away, ✘ inside the blackout. The webcast is at 8:00 am CT (search summary; company release of 10/1 per the 10/23 entry). The report after that is ≈ late January / early February 2027 (not confirmed) |

**levels.py ABBV** (2026-10-28 11:07 ET):
```
ABBV  $287.95 (2026-10-28 11:07 ET); last daily bar 2026-10-28 close $287.95
  20/50/200-DMA  278.59 / 268.17 (rising) / 236.39 (rising)   price vs 50 +7.4%, vs 200 +21.8%
  RSI(14) 67.1   ATR(14) $6.25 = 2.2% a day   52-wk 190.75–291.40 (-1% from the high)
  Trend: above a rising 200-DMA
  Chase guard: ok
  Next report: 2026-10-30 before the open (2 sessions; EPS est. 3.76)   ✘ inside the 3-session buy blackout
  Swing support below: 257.87, 246.77, 243.07   resistance above: 291.40
```
**Zone check:** `levels.py ABBV --zone 265.00-266.30 --stop 255 --target 289.00 --size 190 --sleeve 3426`
```
  Setup: zone 265.00–266.30, stop 255.00, T1 289.00
    at low     265.00: R/R 2.40:1, stop 1.60 ATR (3.8%)   ✓
    at mid     265.65: R/R 2.19:1, stop 1.70 ATR (4.0%)   ✓
    at high    266.30: R/R 2.01:1, stop 1.81 ATR (4.2%)   ✓
    size $190 ≈ 0.7152 sh at the mid; risk to stop $7.62 = 0.2% of $3,426   ✓ ≤ 2%
    price 287.95 is +8.1% above the zone — wait for the alert at 266.30
```
**Rule check at the zone:**
- Chase guard ✓: RSI 67.1 today, close to the 70 line; it will be lower in the zone. The 50-DMA will be ≈ 0–2% above the
  zone.
- Price is above a rising 200-DMA ✓.
- The stop is ≥ 1.5 ATR and ≤ 15% away ✓.
- R/R ≥ 2:1 at the low, mid and high ✓.
- Risk ≤ 2% of the sleeve ✓.
- ✘ **Today it is inside the blackout.** A buy is possible only after the 10/30 report, and the client's pause runs to 11/2.

**Re-run on 11/2:**
- The zone floor is $255 + 1.5 × ATR(14). $265.00 passes while ATR(14) ≤ $6.67, and $266.30 passes while ATR(14) ≤ $7.53.
- The zone top is (T1 + 2 × 255) / 3 = $266.33 with T1 at $289.00.
- **A gap down to a new low** leaves a new, lower rejection high, which becomes T1 and moves the zone down.
- **A gap up through $291.40** means there is no resistance left above: re-derive the zone, and do not chase the breakout.

**Plan status:**
- **v3:** not buyable (≤ 1 non-AI satellite, TTWO), and the client's pause runs to 11/2.
- **v5:** ABBV is **not** on the §11 list, and JNJ holds the one health-care slot. ABBV could only replace JNJ at a quarterly
  review. It passes the ≤ 35× gate (20.6× 2026, 17.8× 2027 EPS).
- **XLV:** do not own ABBV and XLV together. XLV is 7.78% ABBV (SSGA 10/27).

### What changed since 10/23
- **Price:** $285.19 → $287.95 (+1.0%). It is testing the band again (today's high $288.80).
- **Indicators:** RSI 64.7 → 67.1; ATR $6.59 → $6.25. The 50-DMA rose from $265.43 to $268.17.
- **The zone is unchanged and still passes.** The lower ATR leaves more room: the stop is 1.60 ATR from the zone's low,
  against 1.52 on 10/23.
- **Pipeline news was positive** (AbbVie newsroom):
  - 10/22: lutikizumab hit its goals in the phase 3 INTREPID trial in hidradenitis suppurativa.
  - 10/23: the FDA approved Skyrizi's subcutaneous induction regimen in Crohn's disease.
  - 10/27: AbbVie submitted the etentamig BLA in multiple myeloma.
- **The bar for Q3 is lower.** Consensus EPS is $3.76–3.78 after eight downward revisions in 30 days (247wallst 10/26).
  That is below the company's own Q3 guide of $3.84–3.88, which excludes IPR&D.
- **Targets still trail the price:** average $283.19 (StockAnalysis 10/26), against $278.07–282.61 on 10/22.
- **Implied move for the print:** ±5.3% (EarningsWatcher, 10/27).
- **No rotation unwind on the chip rebound:** ABBV was +0.4% on 10/26 and −0.1% on 10/27, while the SOX rose 2.8% and 3.6%.

### Earnings preview: Q3 2026, 10/30 before the open
1. **Date and time.** 10/30, before the open (levels.py/Alpha Vantage; 247wallst 10/26; company release of 10/1). The last
   decision point is the 10/29 close.
2. **Consensus.**
   - **EPS: $3.76** (Alpha Vantage) or **$3.7788** (247wallst 10/26). That is +103% y/y, because the Q3 2025 base carried a
     $1.50 IPR&D charge.
   - **Revenue: $17.35B**, +10.0% (247wallst), or $17.307B (Hudson Labs 10/6).
   - **Company guide for Q3:** $3.84–3.88 excluding IPR&D (247wallst). The 10/5 8-K's IPR&D charge ($216M, −$0.11) puts it
     at ≈ $3.73–3.77 including IPR&D (10/23 entry). Consensus is therefore sitting at the guide.
   - **Full year:** guide $13.87–14.07 (7/31); consensus $13.95–13.96.
   - **The metrics that move the stock:**
     - Skyrizi (FY guide $21.7B);
     - Rinvoq (≈ $2.73B expected for Q3, 247wallst);
     - neuroscience (Q2 +20.3%);
     - Humira erosion;
     - Apogee dilution and any 2027 colour;
     - **the dividend.** It was raised from $1.64 to $1.73 (+5.5%) with the Q3 2025 report (8-K exhibit, search summary)
       and has been $1.73 since.
3. **Implied move: ±5.3% ≈ ±$15.3** (EarningsWatcher 10/27; ≈ 5% per 247wallst 10/26).
   - The average peak earnings-day move is ±5.7% over 10 years and ±6.1% over 2.
   - The peak move exceeded the implied move in 14 of the last 17 reports.
   - A −5.3% gap lands at ≈ $272.7, still 2.4% above the zone top. Reaching the zone takes ≈ −7.5%, an open like 2/4/26
     (−7.0%).
4. **Scenarios:**

   | Scenario | What has to happen | Likely reaction | Action written now |
   |---|---|---|---|
   | Bull | Skyrizi + Rinvoq ≥ +20%, the FY guide raised, a clean Apogee update, a dividend raise ≥ 5% | a gap through $291.40 to a record | No buy (no chase; RSI likely > 70). Without resistance there is no 2:1 setup: re-derive after a base forms |
   | Base | in line; guide held; dividend raised | a $275–292 range; this stock usually fades after reports | Re-run the zone on 11/2 with the new ATR. The $266.30 alert stays if the check passes |
   | Bear | an EPS miss, a guide cut beyond IPR&D, Skyrizi + Rinvoq < +20%, or no dividend raise | a −5 to −8% open (the 2/4/26 pattern) | If a pillar breaks, the zone is void (§4 lock until the next data point). If not, re-derive with the new rejection high as T1 |

5. **History** (levels.py bars, opening gap / close-to-close / next day):

   | Report | Open | Close | Next day |
   |---|---|---|---|
   | 7/31/26 | −1.9% | −2.5% | −2.3% |
   | 4/29/26 | −2.9% | +3.1% | |
   | 2/4/26 | −7.0% | −3.8% | |
   | 10/31/25 | −2.3% | −4.5% | −2.8% |

   **All four opened down.**
6. **Decision, written 10/28:** no position, and no buy until 11/2. Re-derive on 11/2 from closed bars; nothing is decided
   on report night.

### Thesis scorecard (v5 candidate; not on the §11 list)
| Pillar (falsifiable) | What was expected | Status (dated) | Trend |
|---|---|---|---|
| Skyrizi + Rinvoq grow ≥ 20% y/y | ≥ +20% | Q2: Skyrizi +24.4%, Rinvoq +24.5% (7/31) | stable; Q3 due 10/30 |
| The adjusted-EPS guide is held or raised, excluding IPR&D | ≥ $13.87–14.07 | trimmed 7/31 for Apogee (−$0.14); IPR&D −$0.11 (8-K 10/5) | weakening (mechanical) |
| Neuroscience grows ≥ 15% | ≥ +15% | Q2 +20.3% | stable |
| The dividend is raised each year with Q3 | a raise on 10/30 | $1.64 → $1.73 (+5.5%) with Q3 2025; $1.73 since | due 10/30 |
| Labels keep expanding | approvals and filings | Skyrizi SC induction in Crohn's approved (10/23); lutikizumab phase 3 positive (10/22); etentamig BLA (10/27) | improving |

**Thesis-break exits (under v5 these replace the price stop):**
1. Skyrizi + Rinvoq combined growth below 15% y/y for two quarters, or a cut to their multi-year sales guidance.
2. Two cuts in a row to the adjusted-EPS guide that acquired IPR&D does not explain.
3. The dividend is cut, or not raised.

**Disconfirming evidence:**
- Consensus Q3 EPS was revised down 8 times in 30 days.
- The average target is below the price.
- Bernstein is at Hold, $230 (10/26).
- Insiders only sold (10/23 entry).
- Net debt is $64.32B.

**Conviction: Low.** It moves to Med after a clean beat and raise with a dividend raise, followed by a pullback that resets
the RSI.

## Thesis
Unchanged from 10/23: a high-margin immunology compounder whose growth comes from Skyrizi and Rinvoq. The week added
evidence that the franchise keeps widening: new labels, and a second immunology mechanism in hidradenitis suppurativa.

The problem is the price, not the business:
- +42% in six months (10/23 entry);
- 20.6× 2026 EPS;
- Street targets below the price;
- a habit of selling off on its reports.

Most of its value as a diversifier is sector behaviour that XLV provides with less single-name risk. It is a buy only after
a pullback that resets the risk.

## Chart & technicals
Source: levels.py, 2026-10-28 11:07 ET. Daily bars come from levels.py's Yahoo cache.

**Trend:** clean and up.
- Above a rising 20-DMA ($278.59).
- Above a rising 50-DMA: $268.17 now vs $260.88 ten sessions ago.
- Above a rising 200-DMA: $236.39 now vs $231.16 twenty sessions ago.
- Price is +7.4% over the 50-DMA and +21.8% over the 200-DMA.

**Momentum and volatility:** RSI(14) 67.1, near the 70 chase line; ATR(14) $6.25 = 2.2% a day.

**Range:** the 52-week range is $190.75–291.40, and price is 1% under the record.

**Last week (closes):** 10/23 $285.64, 10/26 $286.74 (high $289.59), 10/27 $286.39. Volume was 4.6M, 4.5M and 3.3M shares,
against a 20-day average of 5.27M. This is a quiet drift into the report.

**Support:**
- $278.0 (10/22 low) and the 20-DMA ($278.6).
- $266.97–269.39 (old ceiling) and the 50-DMA: **the zone.**
- $257.87, the 10/2 swing low; stop $255.
- $246.77 (9/9) and $243.07 (7/15).

**Resistance:** $289.00 / $289.59 / $290.98 / $291.40.

**levels.py oddity:** levels.py shows only $291.40. The other three highs sit within 5 bars of a higher high, so its swing
finder never lists them. T1 at $289.00 is set by hand, as the bottom of the band.

## Fundamentals
**Market data** (StockAnalysis, 10/28 10:56 ET, price $288.31):
- Market cap $509.48B; EV $573.79B.
- Forward P/E 19.15. My calculations at $287.95: 20.6× the 2026 consensus and 17.8× the 2027 consensus.
- Trailing P/E 81.45; PEG 1.41; EV/EBITDA 18.54.

**Dividend and cash flow:**
- Dividend $6.92 a year = 2.40%.
- FCF (TTM) $18.21B = a 3.60% yield.

**Balance sheet:** debt $70.89B, cash $6.57B → **net debt $64.32B**. Share count +0.03% y/y.

**Margins (TTM):** gross 72.79%, operating 35.56%, net 9.80%.

**Consensus** (StockAnalysis, 10/26):

| | 2026 | 2027 |
|---|---|---|
| Revenue | $67.6B (+10.6%) | $73.58B (+8.8%) |
| EPS | $13.95 | $16.20 (+16.1%) |

**Q2 2026 base** (10/23 entry; not re-fetched): revenue $16.99B (+10.2%); Skyrizi $5.505B; Rinvoq $2.525B; Humira $756M
(−35.9%).

**v5 gate (≤ 35×):** passes.

## News & catalysts (last 30d / next 90d)
Items new since 10/23 are marked ★. Releases are from the AbbVie newsroom unless noted.

**Last 30 days:**
- ★ 10/28 — Botox Cosmetic Day returns on 11/18. *Neutral.*
- ★ 10/27 — **Etentamig BLA** submitted to the FDA for relapsed/refractory multiple myeloma. *Confirming.*
- ★ 10/26 — **Analyst maintains** (StockAnalysis). *Neutral.*
  - Piper Sandler $303 Buy.
  - **Bernstein $230 Hold.**
  - Scotiabank $320 Buy.
- ★ 10/23 — **The FDA approved Skyrizi's subcutaneous induction regimen** in moderate-to-severe Crohn's disease.
  *Confirming.*
- ★ 10/23 — **Analyst maintains** (StockAnalysis): Morgan Stanley $310 Buy, BofA $305 Buy. *Neutral.*
- ★ 10/22 — **Lutikizumab** phase 3 INTREPID topline: it improved the signs and symptoms of hidradenitis suppurativa.
  *Confirming:* a new immunology asset.
- 10/19 — **ABBV-466** in Crohn's: higher endoscopic remission than either monotherapy. *Confirming (early).*
- 10/18 — ESMO solid-tumour programme. *Neutral.*
- 10/5 — **8-K:** a Q3 IPR&D charge of −$0.11. *Neutral* (10/23 entry).

**Next 90 days:**
- **10/30** — Q3 results and the likely dividend decision.
- **11/3** — US midterm elections.
- **11/16** — the $1.73 dividend is paid (record date 10/15; AbbVie release of 9/10, search summary).
- **Rinvoq decisions** — vitiligo "later this year", alopecia areata "early next year" (search summary; unverified).
- **≈ late January / early February 2027** — Q4 results and the 2027 guide.

## Positioning & sentiment
- **Analysts** (StockAnalysis, 10/26): consensus Buy. 16 Strong Buy, 7 Buy, 5 Hold, 1 Sell. Average target **$283.19
  (−1.8%)**, median $288, range $200–325.
- **Options:** the put/call ratio for the 10/30 expiry is 0.59 (247wallst 10/26), so positioning into the print is bullish.
  That is crowded.
- **Short interest:** 16.28M shares = 0.92% of float (StockAnalysis; date not shown).
- **Crowding:** a top-3 XLV weight (7.78%) that receives the sector flows. Bullish options and targets that trail the
  price, ahead of a stock that usually falls on its reports: that is the crowded + extended + earnings-soon setup the
  protocol warns about.

## What would make me wrong
- **Bull:** a beat, a raise and a dividend raise gap it through $291.40, and it never comes back to $266. We miss it. That
  is acceptable, because buying a record with RSI > 70 is a chase.
- **Bear:** a close under $255 breaks the 10/2 low. The thesis is hit by:
  - Skyrizi + Rinvoq growth under 20%;
  - a guide cut beyond IPR&D;
  - no dividend raise.
- **Rotation:** so far the healthcare bid has survived a +7.6% chip rebound, but a longer chip rally could still drain it.

## Sources
**Price and technicals**
- levels.py ABBV (Yahoo chart API): output and setup check at 2026-10-28 11:07 ET; chart
  `/tmp/claude-1000/-home-waelas-wael-amana-amana-assistant/cf7235bd-03e5-456e-8948-a8c2229a57bd/scratchpad/charts/ABBV.png`.
  Earnings date and the $3.76 estimate from Alpha Vantage (demo key; cached 10/27).

**Earnings preview**
- https://247wallst.com/investing/2026/10/26/abbvie-options-price-in-a-sudden-5-swing-what-investors-must-know-before-oct-30/
  — 2026-10-26.
- https://www.hudson-labs.com/research/abbvie-q3-2026-earnings-preview-abbv-results-and-outlook — 2026-10-06.
- https://earnings-watcher.com/wiki/abbv-implied-move — implied move and history, as of 2026-10-27.
- https://tradersunion.com/news/companies/show/3990119-abbvie-stock-is-little-changed/ — webcast time (search summary).

**Company and fundamentals**
- https://stockanalysis.com/stocks/abbv/statistics/ — 2026-10-28 10:56 ET.
- https://stockanalysis.com/stocks/abbv/forecast/ — as of 2026-10-26.
- https://news.abbvie.com/ — releases 10/18–10/28, fetched 2026-10-28.

**Dividend**
- https://www.sec.gov/Archives/edgar/data/1551152/000155115225000047/abbv-20250930xexhibit991.htm — the Q3 2025 release
  with the raise to $1.73 (search summary).
- https://news.abbvie.com/2026-09-10-AbbVie-Declares-Quarterly-Dividend — 2026-09-10 (search summary).

**XLV weight**
- https://www.ssga.com/us/en/intermediary/etfs/state-street-health-care-select-sector-spdr-etf-xlv — ABBV at 7.78%, as of
  2026-10-27.

**Unverified:**
- the webcast time;
- the timing of the Rinvoq decisions;
- whether the dividend raise will come on 10/30;
- the dates of the short-interest figures.

---

## ABBV — AbbVie — deep dive 2026-10-23 (non-AI diversifier screen)

**Verdict:** WATCH. Buy from 11/2 only in **$265.0–266.3** (alert $266.3), and only if the 10/30 report keeps the
guidance. · **Conviction:** Low. AbbVie executes very well, but it has run +42% in six months. Its forward P/E is at the
top of its range, the average analyst target is below the price, and it fell after 3 of its last 4 reports. Two drugs
(Skyrizi + Rinvoq) are 47% of sales, so a single-name position swaps the AI concentration for a smaller version of the
same mistake.

| | |
|---|---|
| Price (date) | **$285.19** (2026-10-22 close, +0.1%; low $278.01, a hammer on the day the SOX fell 6.7%). Friday 10/23 bars did not exist at fetch time (22:12 UTC 10/22) |
| Entry zone | **$265.0–266.3**, alert at **$266.3** (market order on the alert). This is the old July–September ceiling ($266.97 / $267.47 / $269.39) plus the rising 50-DMA (≈ $266.7–269.3 on 11/2). It is 6.6–7.1% under the 10/22 close |
| Invalidation (stop) | **$255**, under the 10/2 swing low $257.87. That is $10.65 = **1.62 × ATR** below the zone mid (−4.0%). Event: the 10/30 report cuts FY26 adjusted EPS below $13.76, or Skyrizi + Rinvoq growth drops under 20% (Q2: +24%) |
| Target 1 / 2 | **$289** (technical: bottom of the $289.0–291.4 record cluster, rejected 10/15, 10/20, 10/21) / **$325** (measured move 291.40 + (291.40 − 257.87); equals the highest Street target). The fundamental target is *lower*: the consensus average ($278–283) is already under the price |
| Reward/risk (T1) | **2.19 : 1** at the $265.65 mid (2.40 at $265.0, 2.01 at $266.3). 5.6 : 1 to T2 |
| Size | One fill: **1.0 sh ≈ $266 = 7.9%** of the $3,387 sleeve. Risk 1.0 × $10.65 = **$10.7 (0.31%)**, far under the $68 cap. The fill size cap binds, not the risk cap. A second half (to 10–15%) only from a new written zone. No adds above $289: there is no resistance-based target above the record |
| Timeframe | weeks to months: to the Q4 report (≈ late Jan / early Feb 2027, unverified; last year 2/4) |
| Next earnings | **Fri 2026-10-30, before the open (confirmed, company PR 10/1).** Blackout 10/27–10/29. The report comes *before* the 11/2 buy window, so re-run every level on 11/2 with the post-report ATR. The zone works while ATR(14) ≤ $7.56; its floor is $255 + 1.5 × ATR |

**Rules check (at the zone mid):** RSI will be well under 70 in the zone (64.7 today) ✓ · ≈ 0% over the 50-DMA (+7.4% today) ✓ ·
stop structural and ≥ 1.5 ATR ✓ · R/R ≥ 2:1 ✓ · one fill ≤ 8% ✓ · risk ≤ $68 ✓ · hard exit −15% from cost ≈ $226 (the
stop comes first) ✓ · after earnings and after 11/2 ✓. **Plan §1: at most one non-AI satellite.** ABBV and XLV compete
for the same slot, and XLV already holds 7.75% ABBV.

## Thesis
AbbVie is a high-margin immunology compounder (adjusted operating margin 48.3% in Q2). Skyrizi and Rinvoq grew 24% in
Q2 and have more than replaced Humira. As a diversifier it has behaved well: 60-day correlation to the SOX −0.48, and
+4.2% across the three chip-crash days (10/14, 10/16, 10/22) while the SOX fell 14.2%. But most of that behaviour belongs
to the sector, not the name: ABBV's 60-day correlation to XLV is 0.77, and XLV's own SOX correlation is −0.44. Over 250
days the SOX correlation is only −0.21, so the hedge is a recent rotation effect, not a law. The case for owning ABBV
over XLV is extra return from best-in-class execution. The price for that is drug-specific, policy and earnings-gap risk.
At $285, after +42% in six months and with the Street's average target below the price, that extra return is mostly
already paid for. It is a buy only on a pullback that resets the risk.

## Chart & technicals
Yahoo chart API, 2y daily bars, fetched 2026-10-22 22:12 UTC; last bar 10/22.
- **Trend:** up and clean. Price $285.19 is above a rising 20-DMA **$274.02** (+3.7% over 10 sessions), 50-DMA **$265.43**
  (+2.7%) and 200-DMA **$235.14** (+1.2%). It sits +4.1% / **+7.4%** / **+21.3%** above them.
- **Momentum:** RSI(14) **64.7** (Wilder). Returns: 1 month +7.5%, 3 months +11.0%, **6 months +41.9%**, 1 year +24.7%.
- **Volatility:** ATR(14) **$6.59 = 2.31%** a day; over the past year it ranged 1.69–3.02% (median 2.47%). Realized vol:
  21.8% (60 days), 25.9% (250 days). Worst day in the year −5.2% (3/18); 18 days moved more than 3%.
- **52-week:** high **$291.40** (10/15, an all-time high) / low **$190.75** (4/29, the Q1 report day). Price is −2.1% from
  the high. Max drawdown on closes: −16.5% over 1 year (11/21/25 → 4/27/26), −21.5% over 2 years.
- **Swing structure, last 6 months:** lows 200.0 (5/8) → 209.0 (6/2) → 215.4 (6/18) → 243.1 (7/15) → 241.2 (8/6) →
  246.8 (9/9) → **257.9 (10/2)**. Highs 220.0 → 230.5 → 261.6 → 267.5 (7/29) → 267.0 (8/19) → 269.4 (9/23) →
  **291.4 (10/15)**. The July–September ceiling at $267–269 broke on 10/7–10/9, on higher volume (5–7.6M shares a day
  against 2.5–4.4M in late September).
- **Resistance:** **$289.0–291.4** (rejected 10/15: high 291.40, close 283.40; 10/20: high 290.98; 10/21: high 289.00).
  There is nothing above it, so T2 is a measured move. I have been conservative: T1 is the bottom of that cluster.
- **Support:** $278.0 (10/22 low) · $273.7 (10/13 low) / 20-DMA $274 · **$267–269 (old ceiling) + 50-DMA** · **$257.87
  (10/2 swing low)** · $246.8 (9/9) · $235 (200-DMA).
- **Earnings reactions (close-to-close):** 10/31/25 **−4.45%** · 2/4/26 **−3.79%** (opened −7.04%, intraday −9.5%) ·
  4/29/26 +3.14% (opened −2.88%) · 7/31/26 **−2.51%**, then −2.33% the next session. Three of four were down.
- **Why no entry now:** from $285.19, 2:1 to $289 needs a stop no lower than $283.3. That is $1.90 away, under a third
  of one ATR. The first structural stop at least 1.5 ATR away is the 10/2 low, and it only pays 2:1 from about $266 or
  lower.

## Fundamentals
Q2 2026 results (8-K, 7/31/2026), the 10/5/2026 8-K, and StockAnalysis (10/22 close).
- **Revenue:** Q2 **$16.990B, +10.2%** (+9.5% operational); H1 $31.992B, +11.2%. Immunology $8.786B (+15.1%):
  **Skyrizi $5.505B (+24.4%)**, **Rinvoq $2.525B (+24.5%)**, Humira $756M (**−35.9%**). Neuroscience $3.228B (+20.3%;
  Vraylar $1.071B, Botox Therapeutic $1.042B). Oncology $1.650B (−1.5%; Imbruvica −29.4%). Aesthetics $1.282B (+0.3%).
  **Skyrizi + Rinvoq = 47% of Q2 revenue.**
- **Margins:** adjusted gross 84.7% (GAAP 74.7%); adjusted operating **48.3%** (GAAP 37.9%). GAAP EPS $2.03 against
  adjusted $3.65 (+22.9%). The gap is amortization ($0.81) and contingent-consideration changes ($0.83).
- **Guidance:** FY26 adjusted EPS $13.91–14.11 → **$13.87–14.07** (7/31, including $0.14 Apogee dilution) → **$13.76–13.96**
  once the Q3 IPR&D charge is included (8-K 10/5: $216M pre-tax, −$0.11). Q3 adjusted EPS guide **$3.73–3.77**; consensus
  ≈ $3.74–3.76 on ≈ $17.3B revenue (MarketBeat/Barchart, via search). FY revenue guide ≈ $67.6B, raised $300M on the Q2
  call (call coverage, **unverified** against the release).
- **Cash flow and balance sheet (StockAnalysis, 10/22):** FCF (TTM) **$18.21B** (3.6% FCF yield). Total debt $70.89B,
  cash $6.57B, **net debt $64.3B**, debt/EBITDA 2.28. Book equity negative (−$5.89B). Diluted shares 1.771B, flat on the
  year. Apogee (≈ $10.9B equity value) closed **9/3/2026**; 2027 dilution ≈ $0.46 a share (search summary of the 8-K,
  **unverified**).
- **Dividend:** $1.73 a quarter ($6.92 a year) = **2.43%** yield; FCF payout ≈ 67%. Last ex-date 10/15 (paid 11/16). The
  annual raise usually comes with the Q3 report (10/31/2025: +5.5%, $1.64 → $1.73).
- **Valuation:** forward P/E **18.9** (StockAnalysis, 10/22); **20.6×** the FY26 guidance midpoint ($13.86). Yahoo's
  quarter-end history: 15.3 (6/30/25), 16.5 (9/30/25), 16.3 (12/31/25), **15.0** (3/31/26), **17.7** (6/30/26). Today is
  at or above the top of that range (no 5- or 10-year average found: **unverified**). Peers' forward P/E at the 10/22
  close: BMY 10.3, MRK 17.7, **ABBV 18.9**, JNJ 24.0, LLY 33.8. EV/EBITDA 18.5; PEG 1.4 (StockAnalysis).

## News & catalysts
**Last 30 days**
- 9/3 — Apogee deal closed (IL-13 for eczema, IL-13/TSLP for asthma); dilutive this year and next — *neutral*.
- 9/28 — FDA approved **Juvmo (tavapadon)** for Parkinson's; launch October 2026 — *confirming*.
- 10/1 — Q3 date set: Fri 10/30, before the open — *neutral*.
- 10/5 (8-K) — Q3 IPR&D charge of $216M (−$0.11); FY26 EPS guide incl. the charge $13.76–13.96 — *neutral* (mechanical,
  but it trims the number).
- 10/6–10/21 — target raises: Scotiabank 280 → **320** (10/6), UBS 260 → 275 Neutral (10/6), Morgan Stanley 296 → 310
  (10/7), JPMorgan 285 → 300 and Cantor 285 → 290 (10/8), RBC 260 → 280 Buy (10/13), Barclays 300 → **325** (10/21) —
  *confirming, but a sign of crowding*.
- 10/15 — ex-dividend $1.73 — *neutral*.
- 10/18 — ESMO program (Madrid, 10/23–10/27); Temab-A colorectal oral on 10/24 — *neutral* (small oncology swing factor).
- 10/20–10/22 — healthcare rotation: XLV record closes, the AI/chip sell-off on 10/22 — *confirming for price, bad for
  entry*.
- Policy background: the MFN deal (1/12/2026) brought a 3-year tariff exemption and a $100B US investment pledge. The
  Section 232 100% tariff on patented drugs took effect 9/29, and MFN-deal companies are at 0% through 1/20/2029 (Zacks via
  Yahoo, 10/6; the article gives no year for 9/29). Tariff risk is largely removed — *confirming*. **Botox** was picked for
  Medicare negotiation, with prices effective 2028 (CMS, 1/27/2026); AbbVie is suing HHS over the program — *breaking-lite,
  long-dated*.

**Next 90 days**
- 10/24 ESMO data · 10/28 FOMC · 10/29 LLY and MRK reports (read-across for the sector) ·
  **10/30 ABBV Q3 + likely dividend raise + first 2027 colour** · 11/3 US midterms (healthcare-policy headlines) · Rinvoq US
  decisions in vitiligo and alopecia areata (filed Feb/Apr 2026; timing **unverified**) · Q4 report ≈ late Jan / early
  Feb 2027 with the 2027 guide (**unverified**).

## Positioning & sentiment
- **Analysts:** MarketBeat (10/22): Moderate Buy. 23 Buy, 1 Strong Buy, 6 Hold, 0 Sell. Average target **$278.07** (range
  $225–325); StockAnalysis average **$282.61**. **Both are below the $285.19 price.** The rally ran ahead of the targets,
  and the October raises are chasing it. Citi reportedly kept a Hold on 10/20 (search summary, **unverified**).
- **Short interest:** 16.28M shares ≈ 0.9–1.0% of the float (9/30; StockAnalysis 0.92%, Yahoo 1.02%), 4.1 days to cover.
  No squeeze fuel and no bear camp.
- **Insiders:** sellers only. EVP Nicholas Donoghoe sold 32,710 sh at $250 (≈ $8.2M) on 8/14/2026; GC Perry Siatis and SVP
  David Purdue sold in Feb–Mar 2026. No open-market buys in about 13 months (Chartrow via search, **unverified** in total).
- **Crowding:** healthcare is now the market's "defensive rotation". XLV is at a record with RSI ≈ 70, 77% of its stocks
  are above their 50-DMA (ETF Action, 10/21), and the sector's forward P/E (19.3) is above the S&P's (19.0) (FactSet,
  10/16). ABBV is a top-3 XLV weight, so it receives the sector flows. When that money leaves, it leaves together. On the
  chip-rebound days 10/19 and 10/21, ABBV fell 0.96% and 1.48%.

## What would make me wrong
- **Price:** a daily close under **$255** (the 10/2 low $257.87 gives way). The trend structure is broken there; exit and
  re-derive from a new base. Below that the next supports are $246.8 and the 200-DMA (≈ $237 on 11/2).
- **Event (bearish):** the 10/30 report cuts FY26 EPS under $13.76, Skyrizi + Rinvoq growth slows below 20%, or the 2027
  commentary flags Apogee dilution plus Botox pricing as heavier than expected. Any of these voids the zone: a headline
  that questions the thesis locks entries until the next hard data point (plan §4).
- **Event (bullish, the cost of waiting):** a clean beat and raise, plus a dividend raise, could gap it through $291 to a
  new record with no pullback. Then there is no rule-compliant entry, and that is acceptable. Buying a breakout above the
  record means a measured-move target, a stop ≥ 1.5 ATR under it, RSI likely > 70, and a valuation already at the top of
  its range.
- **Rotation reversal:** if the AI/chip trade rebounds hard, the defensive bid can fade for weeks, as on 10/19 and 10/21.

## Sources
- Yahoo chart API ABBV, XLV, ^SOX, SPY, LLY, JNJ, MRK — 1y and 2y daily bars, fetched 2026-10-22 22:12 UTC (01:12 EEST 10/23); last bar 10/22
- AbbVie Q2 2026 release (8-K Ex. 99.1), 2026-07-31 — https://www.sec.gov/Archives/edgar/data/1551152/000155115226000023/abbv-20260630xexhibit991.htm
- AbbVie 8-K (Q3 IPR&D, updated guidance), 2026-10-05 — https://www.sec.gov/Archives/edgar/data/1551152/000155115226000030/abbv-20261005.htm
- AbbVie PR "to Host Third-Quarter 2026 Earnings Conference Call", 2026-10-01 — https://www.nasdaq.com/press-release/abbvie-host-third-quarter-2026-earnings-conference-call-2026-10-01
- Yahoo Finance, Q2 call highlights (revenue guide ≈ $67.6B; search summary, not opened) — https://finance.yahoo.com/healthcare/articles/abbvie-q2-earnings-call-highlights-150428675.html
- StockAnalysis ABBV statistics, 2026-10-22 — https://stockanalysis.com/stocks/abbv/statistics/ · peers: /jnj/, /mrk/, /lly/, /bmy/ statistics, 2026-10-22
- Yahoo key statistics ABBV (quarter-end forward P/E), fetched 2026-10-23 — https://finance.yahoo.com/quote/ABBV/key-statistics
- MarketBeat ABBV forecast, 2026-10-22 — https://www.marketbeat.com/stocks/NYSE/ABBV/forecast/
- ad-hoc-news: RBC 10/13 (article 10/21) — https://www.ad-hoc-news.de/boerse/news/corporate-news/abbvie-stock-rbc-keeps-buy-rating-for-abbvie-stock-at-usd-280-00/70385929 · Scotiabank 10/6 — https://www.ad-hoc-news.de/boerse/news/corporate-news/scotiabank-lifts-target-for-abbvie-stock-from-usd-280-00-to-usd-320-00/70340323
- Short interest 9/30 (search summary) — https://curvedtrading.com/stocks/abbv/short-interest/
- Insider sale 8/14 (search summary) — https://www.insidertrades.com/alerts/nyse-abbv-insider-buying-and-selling-2026-08-20/
- Apogee close 9/3/2026 (search summary) — https://www.nasdaq.com/articles/abbvie-completes-109-bln-acquisition-apogee-therapeutics
- Juvmo approval, 2026-09-28 — https://news.abbvie.com/2026-09-28-U-S-FDA-Approves-AbbVies-JUVMO-TM-tavapadon-for-Parkinsons-Disease
- ESMO program, 2026-10-18 — https://news.abbvie.com/2026-10-18-AbbVie-to-Present-Data-at-the-2026-European-Society-for-Medical-Oncology-ESMO-Congress-Highlighting-Progress-Across-its-Expanding-Solid-Tumor-Portfolio
- Dividend raise 2025-10-31 — https://www.tipranks.com/news/the-fly/abbvie-raises-quarterly-dividend-5-5-to-1-73-from-1-64-per-share-thefly
- MFN deal, 2026-01-12 — https://www.cnn.com/2026/01/12/politics/drug-prices-abbvie-trump · https://www.fiercepharma.com/pharma/abbvie-inks-latest-white-house-drug-pricing-deal-scoring-tariff-reprieve-it-makes-100b-us
- Pharma tariffs (Zacks via Yahoo), 2026-10-06 — https://finance.yahoo.com/economy/policy/articles/execution-pharma-tariffs-brings-etfs-132200925.html
- CMS IPAY 2028 selected drugs (Botox), 2026-01-27 — https://www.cms.gov/files/document/factsheet-medicare-negotiation-selected-drug-list-ipay-2028.pdf
- FactSet Earnings Insight, 2026-10-16 — https://advantage.factset.com/hubfs/Website/Resources%20Section/Research%20Desk/Earnings%20Insight/EarningsInsight_101626.pdf
- ETF Action, 2026-10-21 — https://www.etfaction.com/small-caps-and-health-care-lead-a-defensive-rotation/
- SSGA XLV daily holdings (ABBV 7.75%), as of 2026-10-21 — https://www.ssga.com/us/en/intermediary/etfs/state-street-health-care-select-sector-spdr-etf-xlv
