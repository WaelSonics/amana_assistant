# XLV — Health Care Select Sector SPDR ETF — research log

One file per ticker; newest entry first. Each entry is dated; numbers are as of that date.

Entries:
- 2026-10-28 (deep dive, holdings-report week; v5-candidate refresh with levels.py checks)
- 2026-10-23 (deep dive, non-AI diversifier screen)

---

## XLV — Health Care Select Sector SPDR ETF — deep dive 2026-10-28

**Verdict:** WATCH. **v5 candidate, not buyable under v3.** Board alert **$170.35** (zone $169.30–170.35).

**Conviction:** Med:
- **For:** it is still the right tool for the diversifier job: 60 stocks, ATR 1.6% a day, and it held flat through a +7.6%
  chip rebound.
- **Against:** at $180.66 it is 0.4% under its record close, with RSI 66.
- **Against:** the sector's Q3 earnings are still falling (−1.2%).
- **Against:** 32% of the fund reports in the next two sessions.

| | |
|---|---|
| Price (date) | **$180.66** (levels.py, 2026-10-28 11:07 ET; intraday high $181.27). Close 10/27: $179.18. Record close $181.30 (10/22) |
| Entry zone | **$169.30–170.35. Alert at $170.35**, then a market order. It is the 10/13 higher low ($169.48), ≈ 1% under the rising 50-DMA ($171.82). It **replaces** the 10/23 zone ($171.0–172.6 with a floating stop at "fill − $4.35"): levels.py checks one fixed stop, and no single fixed stop lets that zone pass (check below) |
| Invalidation (stop) | **$165.00**, under the 9/11–10/8 double bottom ($165.11 / $165.19, levels.py's first two supports). That is 1.50–1.87 ATR, or 2.5–3.1%. Hard exit at −15% ≈ $145. **Event:** the thesis-break exits below |
| Target 1 / 2 | **T1 $181.17**: the 10/26 rejection high (closed $179.28). It is the bottom of the record band, $181.17–182.25, which also holds the 10/22 record close ($181.30) and the record high ($182.25). **levels.py prints "resistance above: none in 6 months", so T1 is set by hand.** **T2 $188.1**: a measured move (10/23 entry) |
| Reward/risk (T1) | **2.76 / 2.35 / 2.02 : 1** at the low / mid / high (levels.py, pasted below) |
| Size | One fill of **$190 = 5.5%** ≈ 1.12 sh. **Risk to the stop $5.40 = 0.2%** (cap $69). Cost: 0.08% a year |
| Timeframe | weeks to months; years if held as a v5 core-sector line |
| Next earnings | An ETF has no report of its own. **31.96% of the fund reports on 10/29–10/30** (table below) |

**levels.py XLV** (2026-10-28 11:07 ET):
```
XLV  $180.66 (2026-10-28 11:07 ET); last daily bar 2026-10-28 close $180.66
  20/50/200-DMA  173.91 / 171.82 (rising) / 158.40 (rising)   price vs 50 +5.1%, vs 200 +14.1%
  RSI(14) 66.3   ATR(14) $2.86 = 1.6% a day   52-wk 141.97–182.25 (-1% from the high)
  Trend: above a rising 200-DMA
  Chase guard: ok
  Next report: not in the 3-month calendar (ETF, or more than 3 months away)
  Swing support below: 165.19, 165.11, 160.73   resistance above: none in 6 months
```
**Zone check:** `levels.py XLV --zone 169.30-170.35 --stop 165.00 --target 181.17 --size 190 --sleeve 3426`
```
  Setup: zone 169.30–170.35, stop 165.00, T1 181.17
    at low     169.30: R/R 2.76:1, stop 1.50 ATR (2.5%)   ✓
    at mid     169.82: R/R 2.35:1, stop 1.69 ATR (2.8%)   ✓
    at high    170.35: R/R 2.02:1, stop 1.87 ATR (3.1%)   ✓
    size $190 ≈ 1.1188 sh at the mid; risk to stop $5.40 = 0.2% of $3,426   ✓ ≤ 2%
    price 180.66 is +6.1% above the zone — wait for the alert at 170.35
```
**The 10/23 zone with a fixed stop fails.** `--zone 171.00-172.60 --stop 167.45 --target 181.30`:
```
    at low     171.00: R/R 2.90:1, stop 1.24 ATR (2.1%)   ✘ stop < 1.5 ATR
    at mid     171.80: R/R 2.18:1, stop 1.52 ATR (2.5%)   ✓
    at high    172.60: R/R 1.69:1, stop 1.80 ATR (3.0%)   ✘ R/R < 2
```
Here is why. For the zone's low to have 1.5 ATR, the stop must be ≤ $166.71. For its top to pay 2:1, the stop must be
≥ $168.25. Both cannot hold, and neither stop sits on structure. The structural stop is under the double bottom, and with
it the zone is the 10/13 higher low.

**How T1 and the zone move from here** (needed because levels.py has no resistance at new highs):
- **T1** = the lowest rejection high in the record band.
- **Zone top** = (T1 + 2 × 165) / 3.
- **Zone floor** = 165 + 1.5 × ATR(14).
- If XLV closes above $182.25 and makes a new record before it pulls back, T1 becomes the new record close. Each $1 added to
  T1 lifts the zone top by $0.33.
- At ATR > $2.90, the $169.30 floor breaks the 1.5-ATR rule.

**Plan status:**
- **v3:** not buyable (≤ 1 non-AI satellite, TTWO), and the client's pause runs to 11/2.
- **v5:** XLV is **not** on the §11 compounder list, which is six single names, one per sector. It is the low-volatility
  alternative to JNJ for the health-care slot, not an addition to it: JNJ is 9.96% of XLV.
- **Valuation gate:** the index forward P/E is 21.61 (SSGA 10/27), under 35× ✓.
- **One line only:** never hold XLV with ABBV or JNJ (10/23 rule: one health-care line).

### Holdings that report this week and next (weights: SSGA, as of 10/27)
| Holding | Weight | Report | Source |
|---|---|---|---|
| **LLY** | **15.77%** | **10/29 before the open**, call 10:00 ET | Lilly release of 10/15 (search summary; 10/23 entry); Alpha Vantage |
| MRK | 5.38% | 10/29 before the open | Merck release of 10/1; Alpha Vantage |
| GILD | 3.03% | 10/29 after the close, webcast 4:30 pm ET | Gilead release (BioPharmaWatch, search summary); Alpha Vantage |
| BMY | outside the top 10 | 10/29 before the open | Alpha Vantage; third-party calendar "confirmed" (search summary) |
| **ABBV** | **7.78%** | **10/30 before the open** | AbbVie release of 10/1; Alpha Vantage |
| REGN | outside the top 10 | 10/30 before the open | Alpha Vantage only |
| AMGN | 3.72% | 11/3 after the close | Alpha Vantage only (**unverified**) |
| PFE | 2.61% | 11/3 before the open | Alpha Vantage only (**unverified**) |

**Already reported:**
- **JNJ** (9.96%): 10/13.
- **UNH** (5.66%): 10/13. Adjusted EPS $4.69 vs ≈ $4.14 expected; 2026 guide raised to ≥ $20.50; the stock closed −0.2% that
  day, then rose ≈ 4.5% over two days (XTB/Trefis via search).
- **TMO** (3.94%): 10/21. Revenue $12.14B (+9%); adjusted EPS $6.68 (+15%) (SEC 8-K, search summary).

**LLY is the swing factor.** Its Q3 consensus is muddied by IPR&D accounting:
- revenue $22.11B / EPS $5.38 (Zacks, search summary);
- revenue $22.62B / normalized EPS $6.67 (247wallst 10/25);
- mean EPS $5.70, down from $9.92, as most analysts now include IPR&D (FactSet 10/23).

Read LLY's print on revenue and guidance, not on headline EPS. A ±10% LLY move is about ±1.6% for XLV through its weight
alone.

### What changed since 10/23
- **Price:** $181.30 → $180.66 (−0.4%). Three flat-to-down closes (10/23 $179.28, 10/26 $179.28, 10/27 $179.18), then +0.8%
  today.
- **Indicators:** RSI 69.9 → 66.3, off the chase line. ATR unchanged at $2.86. The 50-DMA rose from $170.90 to $171.82.
- **The setup was re-derived:**
  - zone $171.0–172.6 → $169.30–170.35;
  - stop "fill − $4.35" → a fixed $165.00;
  - T1 $181.30 → $181.17, the 10/26 rejection high.
- **The rotation did not unwind on a chip rebound.** The SOX rose 7.6% from the 10/22 close (+2.8% on 10/26, +3.6% on
  10/27) while XLV moved 0.0% and −0.1%. On 10/19 and 10/21, XLV had fallen ≈ 0.5% on chip up-days (10/23 entry).
- **Sector earnings (FactSet, 10/23):**
  - Q3 health-care EPS −1.2% y/y, improved from −2.6% on 10/16.
  - Pharma is −17%; without pharma the sector would be +9.4%.
  - The bottom-up 12-month target is +6.5%, the second-smallest of the 11 sectors.
  - 61% of ratings are Buy.
- **Fund (SSGA, 10/27):**
  - AUM $47.04B, against $47.46B on 10/21–22.
  - Index forward P/E 21.61, against 21.6.
  - LLY 15.77%, against 15.66%.
  - JNJ 9.96%, against 9.57%.
- **Week to 10/23:** XLV +1.5% vs SPY −0.4%; IBB +2.9%, XBI +3.6% (Stocktwits via Yahoo, 10/26).

### Thesis scorecard (v5 candidate; not on the §11 list)
| Pillar (falsifiable) | What was expected | Status (dated) | Trend |
|---|---|---|---|
| It diversifies the chip risk: it rises on chip sell-offs and does not unwind on rebounds | up on chip-crash days, ≈ flat on chip rallies | +3.6% across 10/14, 10/16 and 10/22 (10/23 entry). On 10/26–10/27 (SOX +2.8%, +3.6%), XLV 0.0% and −0.1% (levels.py bars) | stable |
| Sector earnings return to growth | Q3 y/y ≥ 0% | −1.2% (FactSet 10/23; −2.6% on 10/16); ex-pharma +9.4% | improving |
| The valuation premium stops expanding | index FY1 P/E ≤ ≈ 22 | 21.61 (SSGA 10/27), against 21.6 (10/21) | stable |
| Drug pricing stays contained by the MFN/tariff deals | no MFN extension to Medicare or commercial | no new policy found this week | stable |
| It stays diversified | LLY ≤ 20% of the fund | 15.77% (SSGA 10/27) | stable, drifting up |

**Thesis-break exits (under v5 these replace the price stop):**
1. Federal action that extends MFN pricing to Medicare or commercial insurance: a price cut across the whole sector.
2. Forward EPS estimates for the sector fall for two quarters in a row (FactSet).
3. LLY goes above 20% of the fund, which makes XLV a single-stock bet.

**Disconfirming evidence:**
- The sector's forward P/E is above its 5- and 10-year averages (FactSet 10/16, in the 10/23 entry).
- The bottom-up upside is only +6.5%.
- Over 250 days the correlation with the SOX was only −0.17 (10/23 entry).

**Conviction: Med.**
- **Up to High** if LLY and ABBV print cleanly and the sector's Q3 growth turns positive.
- **Down to Low** if XLV breaks $165.

## Thesis
Unchanged. The account's risk is one theme (AI semis and memory). XLV gives the opposite behaviour without a new single
point of failure: 60 stocks, a 1.6% daily ATR, and a 0.08% fee.

This week answered the 10/23 entry's main worry. A +7.6% chip rebound did not pull money back out of health care. That is
one week, not a law.

The cost is the same as on 10/23:
- the sector is no longer cheap (FY1 P/E 21.6);
- its earnings are still slightly negative;
- a third of the fund reports in two days, with Lilly alone at a sixth of it.

So own it as insurance bought on a pullback, not by chasing a record.

## Chart & technicals
Source: levels.py, 2026-10-28 11:07 ET. Daily bars come from levels.py's Yahoo cache.

**Trend:** up.
- Above a rising 20-DMA ($173.91).
- Above a rising 50-DMA: $171.82 now vs $169.49 ten sessions ago, ≈ +$0.23 a session.
- Above a rising 200-DMA: $158.40 now vs $156.59 twenty sessions ago.
- Price is +5.1% over the 50-DMA and +14.1% over the 200-DMA.

**Momentum and volatility:** RSI(14) 66.3; ATR(14) $2.86 = 1.6% a day. The chase guard passes.

**Range:** the 52-week range is $141.97–182.25, and price is 1% under the record.

**Last week:** 10/23–10/27 was a three-day pause at $179.2 on 7.7–7.8M shares a day, against an 8.7M 20-day average. Today
it reached $181.27 intraday and fell back to $180.66 by 11:07.

**Support:**
- $176.2–176.6: the 10/15 gap and the old August record.
- $174.0–175.3: the unfilled 10/14–10/15 gap.
- $171.8: the 50-DMA.
- **$169.48: the 10/13 higher low (the zone).**
- **$165.11 / $165.19: the double bottom; stop $165.00.**
- $160.73 (7/31) and the 200-DMA (≈ $158.4).

**Resistance:** $181.17 (10/26), $181.30 (record close), $182.25 (record high).

**levels.py oddities:**
- levels.py lists no resistance, because the 10/22 record sits inside the last 5 bars and nothing above it exists.
- Its supports are the two halves of the double bottom ($165.19, $165.11) and $160.73. It does not list $169.48, because
  that low is within 5 bars of the lower 10/8 low.

**Where the zone sits:** by 11/2 the 50-DMA will be ≈ $172.5. The zone is therefore a break of the 50-DMA down to the
10/13 higher low, not a test of the 50-DMA. That is a deeper pullback than on 10/23 (−5.7% from today). It is the price of a
structural stop.

## Fundamentals
**Fund data** (SSGA fund page, as of 10/27 unless noted):
- NAV $179.17; AUM $47.04B; gross expense ratio 0.08% (10/28).
- 30-day SEC yield 1.41%; distribution yield 1.42% (10/26).
- Index P/E: 33.10 trailing, **21.61 forward (FY1)**.
- 61 holdings (60 in the index).

**Top 10 = 60.6%:**

| Holding | Weight |
|---|---|
| LLY | 15.77% |
| JNJ | 9.96% |
| ABBV | 7.78% |
| UNH | 5.66% |
| MRK | 5.38% |
| TMO | 3.94% |
| AMGN | 3.72% |
| GILD | 3.03% |
| ABT | 2.74% |
| PFE | 2.61% |

**Industries:** pharma 36.58%, biotech 19.92%, providers and services 17.18%, equipment and supplies 14.91%, life-science
tools 10.68%, health-care technology 0.72%.

**Sector earnings** (FactSet, 10/23):
- Q3 EPS −1.2% y/y: the only S&P sector declining.
- By industry: pharma −17%; health-care technology +13%; tools +13%; biotech +13%; providers +8%; equipment +6%.
- The net margin is 7.5%, against a 5-year average of 8.7%.
- For comparison, the S&P 500's forward P/E is 18.7 (5-year average 19.8).

## News & catalysts (last 30d / next 90d)
Items new since 10/23 are marked ★.

**Last 30 days:**
- ★ 10/23–10/27 — **Holdings' pipeline news.** *Confirming.*
  - ABBV: Skyrizi subcutaneous induction approved in Crohn's (10/23); etentamig BLA (10/27).
  - JNJ: ESMO prostate and head-and-neck data (10/24–10/25).
  - MRK: endometrial phase 3 wins (10/26); MRK still fell 3.2%.
- ★ 10/23 — **FactSet:** sector Q3 EPS −1.2%, from −2.6%. Elevance's beat helped. *Improving.*
- ★ 10/26 — **Stocktwits weekly:** XLV +1.5% in the week to 10/23 vs SPY −0.4%. *Confirming* (and evidence of crowding).
- 10/20 and 10/22 — record closes (10/23 entry). *Confirming.*
- 10/13 and 10/21 — UNH and TMO beats (above). *Confirming.*

**Next 90 days:**
- **10/28** — FOMC decision at 2:00 pm ET (desk: ≈ 94% hold).
- **10/29** — LLY, MRK and BMY before the open; GILD after the close.
- **10/30** — ABBV and REGN before the open.
- **11/2** — VRTX after the close (Alpha Vantage).
- **11/3** — AMGN and PFE (Alpha Vantage), and the US midterm elections.
- **Late 2026** — Medicare's negotiated prices for the 2028 drug list (10/23 entry; timing unverified).
- **January** — the JPM Healthcare conference and the 2027 guides.

## Positioning & sentiment
- **Crowding:** moderate, and lower than on 10/23. RSI is off 70; three quiet sessions came on below-average volume; it held
  through a chip rally.
- **Analysts** (FactSet 10/23): 61% of the sector's ratings are Buy; the bottom-up target is only +6.5%.
- **Flows:** AUM fell $0.42B from 10/21–22 to 10/27 (SSGA). That is not a clean flow figure, because it mixes price moves
  and creations. Short interest was not checked: not material for a $47B sector ETF.

## What would make me wrong
- **Price:** a close under $165 breaks the double bottom and ends the uptrend that started in July. Re-derive from a new base.
- **Events:**
  - LLY (15.8%) disappoints on revenue or guidance on 10/29.
  - A drug-pricing push after the 11/3 midterms.
  - A longer chip rally that finally pulls the rotation money out.
- **The cost of waiting:** XLV breaks out above $182.25 and never pulls back 6%. That is acceptable. A record with RSI ≈ 70
  is the same excitement trade that built the AI concentration, in a different sector.

## Sources
**Price and technicals**
- levels.py XLV (Yahoo chart API): output and setup checks at 2026-10-28 11:07 ET; chart
  `/tmp/claude-1000/-home-waelas-wael-amana-amana-assistant/cf7235bd-03e5-456e-8948-a8c2229a57bd/scratchpad/charts/XLV.png`.
  SOX and S&P closes from levels.py's cache, the same fetch.

**Fund and sector data**
- https://www.ssga.com/us/en/intermediary/etfs/state-street-health-care-select-sector-spdr-etf-xlv — NAV, AUM, P/E, top 10,
  industries; as of 2026-10-26/27/28.
- FactSet Earnings Insight, 2026-10-23 —
  https://advantage.factset.com/hubfs/Website/Resources%20Section/Research%20Desk/Earnings%20Insight/EarningsInsight_102326.pdf
- https://finance.yahoo.com/healthcare/articles/stocktwits-pharma-pulse-big-pharma-022829910.html — 2026-10-26 (weekly
  performance and the catalyst calendar).

**Holdings' reports**
- Earnings dates: Alpha Vantage earnings calendar via levels.py's cache (demo key; fetched 2026-10-27).
- https://247wallst.com/investing/2026/10/25/3-massive-catalysts-that-could-ignite-an-eli-lilly-stock-rally-on-oct-29/ —
  2026-10-25 (LLY consensus).
- https://lilly.gcs-web.com/news-releases/news-release-details/lilly-confirms-date-and-conference-call-third-quarter-2026 —
  2026-10-15 (via the 10/23 entry; the date is re-confirmed in a 10/28 search summary).
- https://www.biopharmawatch.com/news/GILD/gilead-sciences-q3-2026-financial-results — GILD date (search summary).
- https://www.xtb.com/en/market-analysis/unitedhealth-group-shares-gain-3-after-stronger-than-expected-earnings-and-guidance
  — 2026-10-13 (search summary).
- https://www.sec.gov/Archives/edgar/data/0000097745/000009774526000173/q32026earnings8kex99_1.htm — TMO Q3, 2026-10-21
  (search summary).
- Merck and AbbVie report dates: their 10/1 releases (10/23 entry); the AbbVie and Merck newsrooms were fetched 2026-10-28.

**Unverified:**
- the AMGN and PFE dates;
- the BMY and REGN weights;
- LLY's consensus basis;
- the timing of Medicare's 2028 prices.

---

## XLV — Health Care Select Sector SPDR ETF — deep dive 2026-10-23 (non-AI diversifier screen)

**Verdict:** WATCH. Buy from 11/2 only in **$171.0–172.6** (alert $172.6), a test of the rising 50-DMA. ·
**Conviction:** Med. It is the right tool for the job: 60 stocks, ≈ 90% of ABBV's anti-chip behaviour at about two-thirds
of its volatility. But today it is at a record close with RSI 69.9 (on the chase-guard line) in a crowded defensive rotation.
With ATR 1.6% and the record 0.5% away, it only pays 2:1 after a ≈ 5% pullback.

| | |
|---|---|
| Price (date) | **$181.30** (2026-10-22 close, +1.32%, a record close; intraday record **$182.24**) while the SOX fell 6.72%. Friday 10/23 bars did not exist at fetch time (22:12 UTC 10/22) |
| Entry zone | **$171.0–172.6**, alert at **$172.6** (market order on the alert). This is the rising 50-DMA (≈ $171.5–172.4 on 11/2), under the unfilled 10/14–10/15 gap ($174.0–175.3). It is 4.8–5.7% under the 10/22 close |
| Invalidation (stop) | **Fill − $4.35** (= 1.52 × ATR $2.86): **$167.45** at the $171.8 mid; $166.65–168.25 across the zone. Every value is under the 10/13 swing low **$169.48** and the 50-DMA. That is −2.5%. A close under **$165.1** (the 9/11–10/8 double bottom) ends the uptrend. Event: a bad LLY report (15.7% of the fund) or a drug-pricing shock after the 11/3 midterms |
| Target 1 / 2 | **$181.3** (technical: the 10/22 record close, the bottom of the $181.3–182.2 sell zone) / **$188.1** (measured move: the Aug–Oct base $165.1–176.6 = $11.5, added to the $176.6 breakout). Fundamental cross-check: FactSet's bottom-up health care target is +8.3% from the 10/16 close ≈ $191 (sector proxy, not XLV itself) |
| Reward/risk (T1) | **2.18 : 1** at the $171.8 mid (2.00 at $172.6, 2.37 at $171.0). 3.75 : 1 to T2 |
| Size | One fill: **1.5 sh ≈ $258 = 7.6%** of the $3,387 sleeve. Risk 1.5 × $4.35 = **$6.5 (0.19%)**, far under the $68 cap. A second half (to ≈ 13–14%) only from a new written zone |
| Timeframe | weeks to months |
| Next earnings | ETF, no report of its own. **≈ 33% of the fund reports 10/28–10/30, before the buy window:** LLY 15.66% (10/29 before the open, confirmed 10/15), ABBV 7.75% (10/30 before the open, confirmed 10/1), MRK 5.69% (10/29, call 9:00 ET, confirmed 10/1), TMO 3.95% (10/28, TipRanks, **unverified**). AMGN 3.65% ≈ 11/3 after the close (estimate, **unverified**). JNJ 9.57% and UNH 5.76% reported 10/13 |

**Rules check (at the zone mid):** RSI well under 70 in the zone (69.9 today: at the line) ✓ · ≈ 0% over the 50-DMA
(+6.1% today) ✓ · stop under a swing low and the 50-DMA, ≥ 1.5 ATR ✓ · R/R ≥ 2:1 ✓ · one fill ≤ 8% ✓ · risk ≤ $68 ✓ ·
hard exit −15% ≈ $146 (the stop comes first) ✓ · after 11/2 ✓. **On the alert day, recompute:** zone top = $181.3 −
3.04 × ATR(14), stop = fill − 1.52 × ATR(14). If XLV sets a new record before pulling back, T1 becomes that record close.
**Plan §1: at most one non-AI satellite.** XLV and ABBV compete for the slot; this file recommends XLV first.

## Thesis
The account's problem is one theme: AMD, ARM, MU and the memory names fell together on 10/14, 10/16 and 10/22. The fix
is exposure that does something different on those days, without bringing in a new single point of failure. XLV did that:
+3.6% across the three chip-crash days while the SOX fell 14.2%. Its 60-day correlation to the SOX is −0.44. On the 10
worst SOX days of the past year it averaged +1.07%, against −0.99% for SPY. Because it holds 60 stocks, a failed trial or
a pricing ruling at one company costs a fraction of a percent, not 5–7%. Two cautions. First, the negative correlation is
a recent rotation effect: over 250 days it is only −0.17, and on the chip-rebound days (10/19, 10/21) XLV fell. Second,
the sector is no longer cheap: its forward P/E is 19.3 against a 5-year average of 17.4 and an S&P of 19.0, while Q3
earnings fall 2.6%. So own it as insurance bought on a pullback, not as a momentum chase at a record.

### ETF or single name for this account? (1y daily data to 10/22 unless noted)

| | **XLV** | **ABBV** |
|---|---|---|
| ATR(14) today · 1-year range | **1.58%** · 1.01–1.78% | 2.31% · 1.69–3.02% |
| Realized vol, 60 / 250 days | **17.3% / 16.2%** | 21.8% / 25.9% |
| Max drawdown on closes, 1y / 2y | **−10.8% / −14.4%** | −16.5% / −21.5% |
| Worst day · worst 5 days · days beyond ±3% | **−2.5% · −4.7% · 3** | −5.2% · −8.5% · 18 |
| Own earnings gap risk | none (largest holding LLY 15.7%) | opened −7.0% on 2/4/26; 3 of last 4 reports down |
| SOX correlation, 60 / 250 days | −0.44 / −0.17 | −0.48 / −0.21 |
| Three chip-crash days (10/14, 10/16, 10/22) | +3.6% | +4.2% |
| Stop distance at zone mid | **2.5%** (1.52 ATR) | 4.0% (1.62 ATR) |
| R/R to T1 at zone mid | 2.18 | 2.19 |
| Per ≈ $260 fill: planned risk / T1 reward | $6.5 / $14.3 | $10.7 / $23.4 |
| Would the −15% hard exit have fired in the last year? | **no** | **yes** |
| Concentration inside | 60 stocks; top 10 = 60.3% | Skyrizi + Rinvoq = 47% of revenue |
| Cost · yield | 0.08% a year (≈ $0.21 on $260) · 1.43% | none · 2.43% |

**Reading it:** the 2% risk cap ($68) never binds here. A rule-compliant fill risks 0.2–0.3% of the sleeve in either
name, because the 8%-per-fill size cap binds first. So the choice is not about planned risk. It is about **unplanned**
risk and about whether the tool fixes the problem. ABBV adds ≈ $9 more upside per fill, and pays for it with an earnings
gap history: a repeat of the 2/4 −7% open from the zone loses ≈ $18.6 on one share, not $10.7. It also brings drug,
policy and patent risk, and a drawdown last year (−16.5%) that would have tripped the hard exit. XLV gives about 90% of
the anti-chip behaviour (−0.44 vs −0.48) with about two-thirds of the volatility (ATR 0.68×, 250-day vol 0.63×, 1-year drawdown 0.65×) and a sixth of the 3% days. For an account that
just learned it held one theme, **XLV is the better tool.** ABBV is a pharma bet, not a hedge. Do not own both: XLV
already holds 7.75% ABBV, and the plan allows one non-AI satellite.

## Chart & technicals
Yahoo chart API, 2y daily bars, fetched 2026-10-22 22:12 UTC; last bar 10/22.
- **Trend:** up. Price $181.30 is above a rising 20-DMA **$172.05** (+2.2% over 10 sessions), 50-DMA **$170.90** (+1.3%)
  and 200-DMA **$157.97** (+0.6%). It sits +5.4% / **+6.1%** / **+14.8%** above them.
- **Momentum:** RSI(14) **69.9** (Wilder), at the chase-guard line. Returns: 1 month +6.7%, 3 months +12.3%,
  6 months +24.0%, 1 year +24.2%.
- **Volatility:** ATR(14) **$2.86 = 1.58%** a day (1-year median 1.45%). Worst day in the year −2.52%; worst 5 days
  −4.68%.
- **52-week:** high **$182.24** (10/22, an all-time high) / low **$141.97** (4/29). Price is −0.5% from the high. Max
  drawdown on closes: −10.8% (2/27 → 4/29/26).
- **Swing structure, last 6 months:** lows 142.7 (5/11) → 145.3 (6/2) → 148.8 (6/18) → 157.2 (7/21) → 160.7 (7/31) →
  **165.1 (9/11)** → **165.2 (10/8)** (a double bottom) → **169.5 (10/13)** → 175.3 (10/19). Highs 146.6 → 155.2 →
  165.6 → 168.5 → **176.6 (8/19)** → 171.9 (9/28) → **182.2 (10/22)**. On 10/15 it gapped over the August record (10/14
  high $173.99 → 10/15 low $176.22); 10/19 filled part of the gap, down to $175.27.
- **Pullbacks inside this uptrend:** −5.1% (7/7 → 7/21), −4.6% (7/28 → 7/31), −6.5% (8/19 → 9/11), −3.9% (9/28 → 10/8).
  A ≈ 5% pullback to the 50-DMA is normal for this trend, not a crash scenario.
- **Resistance:** none above $182.24 (record). T2 is a measured move, and T1 conservatively uses the record close.
- **Support:** $176.2–176.6 (gap top / old record) · **$174.0–175.3** (unfilled gap) · **50-DMA ≈ $171–172** · **$169.48**
  (10/13 higher low) · **$165.1–165.2** (double bottom) · 200-DMA ≈ $158.6 on 11/2.
- **Why no entry now:** at $181.30 even a measured-move T1 ($188.1) fails. The nearest structural stop at least 1.5 ATR
  away is under the 10/19 low (≈ $175.0): $6.30 of risk for $6.80 of reward = 1.1 : 1.
- **The gap above the zone:** between the zone and T1, the $174.0–176.6 gap/old-record band can slow a rebound. R/R to
  $176.6 from the mid is only 1.1 : 1. The setup is a trend-continuation bet that the record is retaken.

## Fundamentals
SSGA fund page and daily holdings (as of 10/21–10/22); FactSet Earnings Insight (10/16).
- **Fund:** gross expense ratio **0.08%**; AUM **$47.46B**; NAV $178.89 (10/21); 60 index stocks (61 holdings incl.
  futures). 30-day SEC yield 1.41%, distribution yield 1.43%.
- **Top 10 = 60.3%:** LLY **15.66%** · JNJ 9.57% · ABBV 7.75% · UNH 5.76% · MRK 5.69% · TMO 3.95% · AMGN 3.65% · GILD
  2.93% · ABT 2.68% · PFE 2.62%. Industries: pharma **36.4%**, biotech 19.9%, providers & services 17.6%, equipment &
  supplies 14.6%, life-science tools 10.7%, health care tech 0.7%. In practice it is a pharma fund with a large Lilly bet:
  one stock is ≈ 1/6 of it.
- **Valuation:** S&P 500 Health Care forward 12-month P/E **19.3** vs its **5-year average 17.4** and **10-year average
  16.5**; the S&P 500 is at 19.0 (FactSet, 10/16). Health care now trades at a premium to the market and about 11–17%
  above its own history. SSGA's index figures (10/21): forward P/E (FY1) **21.6**, trailing P/E 33.2, P/B 5.0.
- **Earnings:** health care is the only S&P sector with falling Q3 earnings, **−2.6% y/y**. Pharma is at −18%, partly
  because analysts now include IPR&D charges (LLY's Q3 estimate cut from $10.03 to $5.60). Without pharma: +7.4%. Since
  9/30, the sector's price is up ≈ 5% while its forward EPS is roughly flat (read off FactSet's scatter chart, approximate):
  the October rally is a re-rating, not new earnings. The bottom-up 12-month target is **+8.3%**, the third-lowest
  of the 11 sectors.

## News & catalysts
**Last 30 days**
- 10/13 — JNJ and UNH Q3. JNJ −5.7% on the day (a talc charge per coverage; it raised its FY guide per search summary,
  **unverified**); XLV −1.35% — *neutral*.
- 10/14–10/15 — XLV +2.5% and +1.9% while the SOX fell; gapped over the August record $176.60 — *confirming (rotation)*.
- 10/16 — FactSet: health care is the only sector with falling Q3 EPS; the sector's forward P/E is above its 5- and
  10-year averages — *a valuation warning*.
- 10/20 — record close $179.82 (+2.37%); ETF Action: +7.2% in a month, 77% of constituents above their 50-DMA, RSI 69 —
  *confirming, and the crowding evidence*.
- 10/22 — record close $181.30 (+1.32%) as the SOX fell 6.72% (Meta capex/FCF, Lam supply warning) — *confirming*.
- Policy background: MFN deals plus the Section 232 tariff. Companies with deals pay 0% through 1/20/2029; others face up
  to 100% on patented drugs (Zacks via Yahoo, 10/6). Per Health Affairs (search summary, **unverified**), 17 companies
  covering 86% of branded sales have signed. Tariff risk for the big XLV names is mostly settled — *confirming*.

**Next 90 days**
- 10/28 FOMC · TMO (est.) · **10/29 LLY and MRK** (21.4% of the fund) · **10/30 ABBV** (7.75%) · ≈ 11/3 AMGN (est.) ·
  **11/3 US midterms.** Healthcare is policy-sensitive; one paywalled report (MM+M, 10/20) links the sector's ≈ 9%
  three-month gain to bets on a Democratic Congress (**unverified**). Medicare's negotiated prices for the 2028 drug list
  (Botox, Entyvio, Cosentyx, Trulicity, Biktarvy and others) are due late 2026 (statutory timing, **unverified**) ·
  JPM Healthcare conference and 2027 guidance in January.

## Positioning & sentiment
- **Crowding:** yes, moderately. Records on 10/20 and 10/22, RSI ≈ 70, 77% of members above their 50-DMA, a P/E premium
  to the S&P, and a narrative ("defensive rotation out of tech") that every outlet now repeats. That narrative fuelled the
  rally, and it also means the bid can reverse quickly if the SOX bounces (10/19: SOX +1.6%, XLV −0.6%; 10/21: SOX
  +2.0%, XLV −0.5%).
- **Analysts:** 61% of health care ratings are Buy (FactSet, 10/16), mid-pack among sectors. The bottom-up upside (+8.3%)
  is among the smallest.
- **Flows / short interest:** no total XLV flow figure found for October (**unverified**). Yahoo headlines from 10/15
  and 10/16 report the fund buying ≈ $20–25M of LLY a day (and JNJ on 10/15), which fits new money arriving (headlines
  only, not opened). Short interest not checked (not material for a $47B sector ETF).
- **Lilly drift:** LLY is already 15.66% and rose 7.0% across the three chip-crash days, so the fund's single-stock
  concentration grows as LLY outperforms.

## What would make me wrong
- **Price:** a close under the stop (≈ $167.5; under the 10/13 higher low). Exit. A close under **$165.1** breaks the
  double bottom and ends the October uptrend; re-derive from a new base. Below that is the 200-DMA ≈ $158.6.
- **Event:** LLY (15.7%) misses or cuts guidance on 10/29; a drug-pricing push after the 11/3 midterms; or an AI/chip
  rebound that pulls the rotation money back out. Any of these can turn a "test of the 50-DMA" into a break of it.
- **Valuation:** a premium P/E on falling sector earnings. If Q3 confirms the decline without better 2027 numbers, the
  re-rating can unwind even without bad news.
- **The cost of waiting:** XLV keeps grinding higher with no 5% pullback, and the entry never comes. That is acceptable:
  buying at an RSI-70 record is the same excitement trade that built the AI concentration, just in a different sector.

## Sources
- Yahoo chart API XLV, ABBV, ^SOX, SPY, LLY, JNJ, MRK — 1y and 2y daily bars, fetched 2026-10-22 22:12 UTC (01:12 EEST 10/23); last bar 10/22
- SSGA XLV fund page (expense ratio, AUM, yields, P/E, industry weights), as of 2026-10-21/22 — https://www.ssga.com/us/en/intermediary/etfs/state-street-health-care-select-sector-spdr-etf-xlv
- SSGA XLV daily holdings file, as of 2026-10-21 — https://www.ssga.com/us/en/intermediary/library-content/products/fund-data/etfs/us/holdings-daily-us-en-xlv.xlsx
- FactSet Earnings Insight, 2026-10-16 (sector forward P/E chart p. 32; health care EPS; targets) — https://advantage.factset.com/hubfs/Website/Resources%20Section/Research%20Desk/Earnings%20Insight/EarningsInsight_101626.pdf
- ETF Action, "Small-Caps and Health Care Lead a Defensive Rotation", 2026-10-21 — https://www.etfaction.com/small-caps-and-health-care-lead-a-defensive-rotation/
- Yahoo Finance headlines on XLV purchases (titles only, not opened): 10/16 — https://finance.yahoo.com/healthcare/articles/state-street-health-care-spdr-110529619.html · 10/15 — https://finance.yahoo.com/healthcare/articles/state-street-health-care-spdr-110350557.html
- GuruFocus, XLV new high, 2026-10-20 — https://www.gurufocus.com/news/9132305/health-care-select-sector-spdr-etf-xlv-hits-new-high-at-17986-on-strong-momentum
- Lilly PR: Q3 date confirmed, 2026-10-15 — https://lilly.gcs-web.com/news-releases/news-release-details/lilly-confirms-date-and-conference-call-third-quarter-2026
- Merck PR: Q3 call 10/29, 2026-10-01 — https://www.merck.com/news/merck-to-hold-third-quarter-2026-sales-and-earnings-conference-call-oct-29/
- AbbVie PR: Q3 on 10/30, 2026-10-01 — https://www.nasdaq.com/press-release/abbvie-host-third-quarter-2026-earnings-conference-call-2026-10-01
- TipRanks TMO earnings (10/28, unverified) — https://www.tipranks.com/stocks/mx:tmo/earnings · MarketBeat AMGN (≈ 11/3 estimate) via search
- JNJ Q3 reaction (search summary) — https://www.rttnews.com/3698614/johnson-johnson-stock-falls-5-after-q3-profit-plunges.aspx
- Pharma tariffs (Zacks via Yahoo), 2026-10-06 — https://finance.yahoo.com/economy/policy/articles/execution-pharma-tariffs-brings-etfs-132200925.html
- Health Affairs on the pharma deals (search summary) — https://www.healthaffairs.org/content/forefront/trump-administration-s-deals-pharma-policy-progress-political-theater
- CMS IPAY 2028 selected drugs, 2026-01-27 — https://www.cms.gov/files/document/factsheet-medicare-negotiation-selected-drug-list-ipay-2028.pdf
- MM+M, 2026-10-20 (paywalled, search summary only) — https://www.mmm-online.com/news/five-things-for-pharma-marketers-to-know-for-tuesday-october-20-2026
