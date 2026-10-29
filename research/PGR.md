# PGR — Progressive Corp — research log

One file per ticker; newest entry first. Each entry is dated; numbers are as of that date.

Entries:
- 2026-10-28 (deep dive, watch only, levels.py-checked; October-report preview)
- 2026-10-23 (deep dive, non-AI diversifier screen)

---

## PGR — Progressive Corp — deep dive 2026-10-28

**Verdict:** WATCH, watch only. PGR is an alternate in the v5 compounder bucket and cannot be bought under v3. The board level
is **$213.50** (zone $213.00–213.50). It applies **only after the 11/18 October report**, and must be re-derived on that day's
close. · **Conviction:** Low, for three reasons:
- the zone passes only under the desk's T1 convention, and fails on the strict reading;
- the band is 50 cents wide;
- the business is past its margin peak: consensus 2027 EPS is 11.8% below 2026.

| | |
|---|---|
| Price | **$225.66**, from levels.py at 2026-10-28 10:52 ET ($226.30 at 11:07 ET). Last close $225.60 (10/27, −1.6%). 52-week high **$239.38** (7/7) |
| Entry zone | **$213.00–213.50**. Set the alert at $213.50, then buy with a market order. It rests on the levels.py swing low of $212.63 (9/9) and the 10/15 low of $212.71 (Yahoo bar), 1.9% above the falling 200-DMA ($209.01). **It is valid only if all of these hold:** (1) the date is 11/19 or later, after the October report; (2) the price is still above the 200-DMA; (3) the plan allows the buy. At 50 cents wide the zone is thin: buy only if the session holds $213.00 at the fill |
| Invalidation (stop) | **$205.40**, under the levels.py swing low of $205.90 (8/4) and under the 200-DMA. That is 1.52–1.62 ATR and 3.6–3.8% under the zone. For events, see the thesis-break exits. **Dividend trap:** last year's annual variable dividend was $13.50 (record date 1/2/2026, paid 1/8/2026), about 6% of the price. A stop 3.6–3.8% under the entry would fire on the ex-date, so a position must be closed or its stop reset before then. The 2026 amount and dates are unverified |
| Target 1 / 2 | **$229.73**: the 10/26 high, which with $229.81 (10/22) and $230.28 (10/23) forms a three-session cap; it is not yet a levels.py swing / **$232.2–235.0**: the July 2–13 closes and the 7/13 high, then **$239.38** (levels.py resistance and the 52-week high) |
| Reward/risk (T1) | **2.20 / 2.10 / 2.00 : 1** at the zone's low / mid / high (levels.py ✓; the top edge is exactly 2.00). On the strict reading, T1 is the old range top at $222.50, made of the levels.py swing highs $223.10 (7/29), $223.78 (10/13), $224.73 (8/24) and $225.45 (9/3); a fall to $213 re-enters that range. That gives **1.25 / 1.18 / 1.11 ✘**. Buying today pays 0.46–0.70:1 ✘ |
| Size | **$190** in one fill ≈ 0.89 sh. Risk to the stop is **$6.99 = 0.2%** (cap $69) |
| Timeframe | Weeks. The position must be gone, or its stop reset, before the annual dividend's ex-date |
| Next earnings | **The October results come Wed 11/18 before the open** (company, in the 10/14 8-K fetched 10/28), so no buys on 11/13, 11/16 or 11/17. **The Q3 call is Tue 11/3 at 09:30 ET** (same 8-K). The Q3 10-Q is due ≈ 11/2 (10/23 entry; not re-verified). November results ≈ mid-December (unverified). levels.py prints "not in the 3-month calendar": it cannot see monthly reports |
| Earliest buy date | **None under v3.** Under the rules, 11/19 at the earliest. A fill between 11/2 and 11/12 would sit inside 10 sessions of a report, and in two of the last four report days the gap was larger than this stop distance (preview below). As a v5 alternate compounder, PGR would instead be bought in a January or February tranche, with thesis-break exits and no price stop (PLAN §11). This zone is a trading-board level only |

T1 convention: as in the 10/28 PM entry. T1 is the nearest real resistance above today's price (PLAN §3b), and the strict
reading is shown beside it. The 10/23 PGR entry used the strict reading, which is why it found no zone.

**levels.py, 2026-10-28 10:52 ET** (the only source of technicals in this entry)
```
PGR  $225.66 (2026-10-28 10:52 ET); last daily bar 2026-10-28 close $225.66
  20/50/200-DMA  219.28 / 217.22 (rising) / 209.01 (falling)   price vs 50 +3.9%, vs 200 +8.0%
  RSI(14) 59.0   ATR(14) $4.97 = 2.2% a day   52-wk 189.20–239.38 (-6% from the high)
  Trend: above a falling 200-DMA
  Chase guard: ok
  Next report: not in the 3-month calendar (ETF, or more than 3 months away)
  Swing support below: 215.98, 212.63, 205.90   resistance above: 239.38
```
**Zone checks, 11:07 ET** (price $226.30, ATR $5.00)
```
$ levels.py PGR --zone 213.00-213.50 --stop 205.40 --target 229.73 --size 190 --sleeve 3426
  Setup: zone 213.00–213.50, stop 205.40, T1 229.73
    at low     213.00: R/R 2.20:1, stop 1.52 ATR (3.6%)   ✓
    at mid     213.25: R/R 2.10:1, stop 1.57 ATR (3.7%)   ✓
    at high    213.50: R/R 2.00:1, stop 1.62 ATR (3.8%)   ✓
    size $190 ≈ 0.8910 sh at the mid; risk to stop $6.99 = 0.2% of $3,426   ✓ ≤ 2%
    price 226.30 is +6.0% above the zone — wait for the alert at 213.50

$ levels.py PGR --zone 213.00-213.50 --stop 205.40 --target 222.50 ...    (strict reading)
    at low 1.25:1 ✘ · at mid 1.18:1 ✘ · at high 1.11:1 ✘
$ levels.py PGR --zone 224.50-225.70 --stop 217.00 --target 229.73 ...    (buying today)
    at low 0.70:1 ✘ (stop 1.50 ATR, flagged) · at mid 0.57:1 ✘ · at high 0.46:1 ✘
```
At 10:52 ET (ATR $4.97) the zone's floor could reach $212.90. At 11:07 ET, with ATR at $5.00, $212.90 sits exactly 1.50 ATR from
the stop, so the floor was raised to $213.00. Re-run the check on the day: the margin is cents.

Chart: `levels.py PGR --chart` (10/28, scratchpad). It shows the $201–225 range from July to October inside a falling 200-DMA,
the 10/22 break above the range top, the 229.7–230.3 cap, and the zone in the middle of the old range. It agrees with the
computed levels.

## What changed since the 10/23 entry
- **Price:** $229.62 (10/22), then $228.07 (10/23, high $230.28), $229.25 (10/26), $225.60 (10/27, −1.6%) and $225.66 now. The
  10/22 break above the $222.5–225.5 range top is holding so far: the lows were $223.83 on 10/27 and $224.47 today.
- **Indicators:**
  - ATR $5.57 → **$4.97** ($5.00 at 11:07): the 10/14 gap is fading out of the average. RSI 66.3 → 59.0.
  - 20-DMA $215.49 → $219.28. 50-DMA $215.63 → $217.22, rising.
  - 200-DMA $208.74 → $209.01. levels.py calls it falling: it was $209.42 twenty sessions ago.
- **T1 moved** from $232.20 (the nearest resistance from $229.62 on 10/23) to the new cap at **$229.73**. Under the PLAN §3b
  convention that creates the $213.00–213.50 zone. Under the strict reading the 10/23 entry used, there is still no zone.
- **Analysts:**
  - BofA Buy, target **$266 → $262** (10/23, stockanalysis). This places the 10/23 entry's unverified "BofA $314 → $266": $266
    was BofA's prior target. The $314 is still unverified.
  - Consensus Hold from 25 analysts. Average target $230.38, median $232, range $196–262 (stockanalysis, updated 10/23).
- **Dates confirmed** from the company's 10/14 8-K: October results 11/18 before the open, and the Q3 call 11/3 at 09:30 ET.
- **Q3 EPS conflict:** consensus was $4.35 (MarketBeat, search summary) or $4.41–4.42 (Tickeron, 10/23 entry). The $4.37 actual
  was therefore in line or a narrow miss, depending on the source.

## Thesis
**Why it is on the list:**
- Auto insurance has nothing to do with AI capex.
- PGR's 60-day correlation with the SOX was −0.48 (10/23 screen, data to 10/22; not re-measured).
- It is cheap on trailing earnings: P/E 11.4 (stockanalysis, 10/28).
- ROE is 33% (stockanalysis, 10/28).

**Why not:**
- **Those earnings are expected to fall.** Consensus EPS goes from $18.46 in 2026 to $16.29 in 2027 (stockanalysis).
- **Growth is slowing while rates are cut.** Premiums written grew only +2% in September, and personal-auto policies fell month
  on month for the first time since November 2023 (10/23 entry).
- **The chart is a range inside a falling 200-DMA.** The only rule-compliant level sits back in the middle of that range.

**What would make it a better candidate:** the 11/18 report showing personal-auto policies growing again with a monthly combined
ratio at or under 90, and the 200-DMA turning up.

## Earnings preview: October results, Wed 11/18 before the open (section A)
1. **Date and time:** 11/18 before the open (company). The last decision point is the 11/17 close. The buy blackout covers 11/13,
   11/16 and 11/17; levels.py does not flag it (see the flags).
2. **Consensus:** there is no published consensus for a monthly report; none was found (unverified). What moves the stock:
   - personal-auto policies in force, month on month: −27K in September, the first drop since November 2023 (10/23 entry);
   - premiums written: +2% in September;
   - the monthly combined ratio: 90.0 in September, against 100.4 a year earlier (8-K, 10/14). The October 2025 comparison was
     not fetched (unverified).
   - The 11/3 call may give colour on rate cuts and advertising first.
3. **Implied move:** not found (unverified). Report-day history comes from the Yahoo bars (below).
   - The average absolute close-to-close move over the last four reports is **4.9%** (my arithmetic).
   - That is larger than the **3.6–3.8% distance to the stop**. Two of the last four opening gaps (−8.2% and −7.1%) would have
     skipped this stop.
   - On a $190 position, 4.9% is about $9 at stake.
4. **Scenarios:**

   | Scenario | What has to happen | Likely reaction | Action written now |
   |---|---|---|---|
   | Bull | Personal-auto policies grow month on month again, premiums written ≥ +4%, combined ratio ≤ 90 | +4–5% (the 8/19 pattern), toward $232–235 | No chase. Re-derive T1 from the new high. The zone stands only if a structure with ≥ 3 ATR of room exists |
   | Base | Policies flat, combined ratio 89–91 | ±1–2% | Re-derive on the 11/18 close. The alert is valid from 11/19 |
   | Bear | A second month-on-month policy drop, or combined ratio > 92 | −4% to −9% (the 7/15 and 10/14 pattern); it may gap into or through the zone | **No buy on the gap.** Two policy drops in a row is thesis-break exit #1. Cancel the alert and re-assess at the December report |

5. **History** (Yahoo bars; report dates from the company releases cited in the 10/23 entry):

   | Report | Opening gap | Close to close | Note |
   |---|---|---|---|
   | 7/15 (Q2) | −8.2% | −9.4% | low $203.58 |
   | 8/19 (July) | +0.2% | +4.8% | |
   | 9/18 (August) | −1.0% | −1.3% | slid to $200.96 by 9/24 |
   | 10/14 (Q3 / September) | −7.1% | −4.2% | intraday low $201.02 (−9.8%) |

6. **Decision, written now:** no position and no buy before the report. Re-run levels.py on the 11/18 close. Carry the alert from
   11/19 only if personal-auto policies did not fall again and the price is still above the 200-DMA.

## Thesis scorecard
| Pillar (falsifiable) | What was expected | Status (dated) | Trend |
|---|---|---|---|
| Premiums keep growing | net premiums written ≥ +5% a year | September +2%; Q3 +4% ($22,301M) (10/14) | weakening |
| Policy count grows month on month | personal-auto policies up month on month | Total 40,489K at 9/30 (+6% y/y), but personal auto −27K against 8/31 (10/14; month-on-month figure per the 10/23 entry) | weakening |
| Underwriting margin holds | monthly combined ratio ≤ 90 | September 90.0; Q3 88.7, against 89.5 (10/14) | stable at the edge |
| Book value holds | no large bond-mark losses | BVPS $59.51; unrealized losses −$3,455M, of which −$1,656M in September alone (10/14). The 10-year yield is now 5.02% (desk) | weakening |
| Earnings path | 2027 EPS ≥ 2026 | 2026 $18.46, 2027 $16.29, −11.8% (stockanalysis, updated 10/23) | weakening |

**Thesis-break exits.** For a v5 compounder these replace the price stop (PLAN §11):
1. Personal-auto policies in force fall month on month again in the October report (11/18), which would be two in a row, or in
   any two of three consecutive monthly reports.
2. The monthly combined ratio goes above 92 in two consecutive months, or the year-to-date ratio goes above 96. The 96 is
   believed to be the company's long-run ceiling, but it was not fetched this session: **unverified**. Confirm it on the 11/3
   call.
3. The annual variable dividend (declared ≈ December) is cut by more than half or skipped. Or book value per share falls below
   $55 on bond marks.

**Disconfirming evidence (the bull side, logged too):**
- September's combined ratio of 90.0 was 10.4 points better than a year earlier.
- Net income doubled in September ($630M against $305M).
- 969,262 shares were bought back at $207.92 in September (8-K, 10/14).

**Conviction:** Low. It rises with one month of personal-auto policy growth. It ends with a second month-on-month drop.

## Chart & technicals
Source: levels.py, 10/28 10:52 ET.
- **Trend:** above a rising 50-DMA ($217.22) and a rising 20-DMA ($219.28). Above a **falling** 200-DMA ($209.01), +8.0% over
  it. The protocol allows fresh longs above a falling 200-DMA but not under it, and the zone sits 1.9% above it.
- **Momentum and volatility:** RSI 59.0, chase guard ok. ATR **$4.97 = 2.2%**, so 1.5 ATR = $7.46. 52-week range $189.20–239.38.
- **Swing lows (levels.py):** 5/8 $191.75 · 5/29 $189.20 · 7/16 $203.08 · 8/4 $205.90 · 8/17 $203.18 · 8/27 $215.98 · 9/9
  $212.63 · 9/24 $200.96 · 10/14 $201.02.
- **Swing highs:** 5/19 $206.84 · 7/7 $239.38 · 7/29 $223.10 · 8/10 $215.99 · 8/24 $224.73 · 9/3 $225.45 · 10/13 $223.78.
  - levels.py lists only $239.38 above the price. The 10/22–10/26 cap ($229.73–230.28) and the July closes ($229.5–234.5) are
    not swings in its five-bar window.
- **Volume** (Yahoo bars): 1.8–2.3M a day since the 10/22 breakout, under the 2.87M 20-day average quoted on 10/23. That is
  thin sponsorship, as on 10/22.

## Fundamentals
**September and Q3** (8-K Ex. 99, 10/14, fetched 10/28):

| | September | Q3 |
|---|---|---|
| Net premiums written | $7,255M (+2%) | $22,301M (+4%) |
| Net premiums earned | $7,160M (+5%) | $21,869M (+5%) |
| Net income | $630M (against $305M) | $2,542M (−3%) |
| EPS | $1.08 | **$4.37** (against $4.45) |
| Combined ratio | **90.0** (100.4 a year earlier) | **88.7** (89.5) |

**Policies in force at 9/30** (thousands, with year-on-year growth):
- Agency auto 11,347 (+7%) · direct auto 16,848 (+8%) · special lines 7,390 (+6%) · property 3,652 (0%) · commercial 1,252 (+5%).
- Total **40,489 (+6%)**.

**Capital:**
- Book value per share **$59.51**.
- Net unrealized losses on fixed maturities **−$3,455M**, of which −$1,656M came in the month.
- September buyback: 969,262 shares at $207.92.

**Valuation** (stockanalysis, 10/28):
- Market cap $131.04B. P/E 11.39 trailing and 14.05 forward. P/B 3.79. ROE 33.24%.
- Debt $8.39B. Shares outstanding −0.43% year on year. Beta 0.24.
- The 0.18% yield counts only the $0.10 quarterly dividend, not the annual variable one.

**Consensus** (stockanalysis, updated 10/23): EPS 2026 $18.46 (range $17.37–19.46) and 2027 $16.29. Revenue 2026 $87.1B and
2027 $91.72B. On those, the price is **12.2× 2026 and 13.9× 2027 EPS** (my arithmetic).

**Dividend:** $0.10 a quarter plus the annual variable dividend. Last year's was $13.50, declared 12/5/2025, record date
1/2/2026, paid 1/8/2026 (company release, fetched 10/28). The 2026 amount is unknown.

## News & catalysts
**Last 30 days**
- **10/14:** Q3 and September results. EPS $4.37, combined ratio 88.7, September premiums written +2%, and the first
  month-on-month drop in personal-auto policies since November 2023. The stock closed −4.2%. *Breaking (growth).*
- 10/15–10/19: Evercore $227, KBW $246, Wells Fargo $196 (Underweight), Goldman Buy $233, Morgan Stanley Hold $210, UBS Hold
  $238 (10/23 entry and stockanalysis). Raymond James $245 reiterated around 10/19–20 (search summary). *Neutral.*
- 10/22: +3.7% in the defensive rotation, with no company news (10/23 entry). *Neutral.*
- **10/23:** BofA Buy, target $266 → $262. *Neutral.*
- 10/27: −1.6%, with no company news found. *Neutral.*

**Next 90 days**
- 10/28: FOMC (desk). The 10-year yield is 5.02%, and higher yields cut book value.
- ≈ 11/2: the 10-Q (unverified).
- **11/3:** Q3 call at 09:30 ET, and the midterms.
- 11/4: Allstate Q3 after the close, a peer read (Alpha Vantage calendar in levels.py's cache).
- **11/18: October results.**
- 11/30: end of the hurricane season.
- ≈ early December: the annual dividend is declared (unverified; last year 12/5).
- ≈ mid-December: November results (unverified).
- ≈ early January: the record or ex-date of the annual dividend (unverified).

## Positioning & sentiment
- **Analysts** (stockanalysis): consensus **Hold**, 25 analysts. Average target $230.38, median $232, range $196–262: +2.1% to the
  average from $225.66.
- **Short interest:** 6.81M shares = 1.18% of float, 2.48 days to cover (stockanalysis, 10/28). It matches the 10/23 entry's
  figure, so it may be stale.
- **Insiders:** not re-checked. The 10/23 entry found only sellers: the CEO sold $8.2M on 9/1, and the CIO files monthly Form 144s.
- **Crowding:** insurers are part of the defensive rotation the 10/23 screen flagged. PGR's own RSI (59) is not extended.

## What would make me wrong
- **A re-rating without a pullback.** A strong October report plus a large December dividend could carry PGR through $230 and
  $239 without ever returning to $213. That is the cost of the rule.
- **A deeper soft market.** More rate cuts and higher advertising spend. A close under the $200.96–201.02 double bottom opens
  $189.
- **Bond marks.** At a 5% 10-year yield, book value keeps eroding.
- **Gaps through the stop.** Report-day gaps of −7% to −8% are normal for this stock, and the dividend ex-date drop is about 6%.
  Both are larger than the stop distance.
- **The T1 convention itself.** If the desk adopts the strict reading, this zone fails (1.1–1.25:1) and PGR goes back to
  "no level".

## Sources
- levels.py (Yahoo chart API; Alpha Vantage calendar). Runs: PGR at 10:52 ET; zone checks and `--chart` at 11:07 ET
  (2026-10-28). The report-day gaps come from the same cached Yahoo bars.
- Progressive 8-K Ex. 99, September and Q3 results, fetched 2026-10-28 — https://www.sec.gov/Archives/edgar/data/80661/000008066126000367/pgr202609ex99earningsrelea.htm (2026-10-14)
- Progressive dividend release, fetched 2026-10-28 — https://investors.progressive.com/financials/financial-news-releases/news-details/2025/Progressive-Announces-Dividend-Information-And-2026-Annual-Meeting-Record-Date/default.aspx (2025-12-08)
- stockanalysis PGR forecast (updated 2026-10-23) — https://stockanalysis.com/stocks/pgr/forecast/
- stockanalysis PGR statistics, 2026-10-28 — https://stockanalysis.com/stocks/pgr/statistics/
- MarketBeat, the Q3 date and the $4.35 consensus (search summary) — https://www.marketbeat.com/earnings/reports/2026-10-14-the-progressive-co-stock/
- ad-hoc-news, Raymond James $245 and Wells Fargo $196 (search summary) — https://www.ad-hoc-news.de/boerse/news/corporate-news/progressive-files-september-results-as-progressive-corp-stock-trades-at-eur-203-50/70410193
- 10/23 entry below, for values marked as such.

---

## PGR — Progressive Corp — deep dive 2026-10-23 (non-AI diversifier screen)

**Verdict:** AVOID for now · re-check after the October report (Wed 11/18) · **Conviction:** Med. On paper it is a good
diversifier: its 60-day correlation with the SOX is −0.48. But the rules leave no entry. From $229.62 the next resistance is
1–2% away. The only band in the chart that passes 2:1 ($203.8–204.3) is 50 cents wide and sits under a flat-to-falling
200-DMA. The business is past its margin peak: growth is slowing, rates are being cut, and 2027 EPS is expected 12% lower.

Data: the latest completed session is Thu 2026-10-22. Yahoo bars were fetched 2026-10-22 22:13 UTC (01:13 EEST Friday),
before Friday's session opened. Prices are raw: the $13.60 January dividend shows in the chart as a gap.

| | |
|---|---|
| Price (date) | **$229.62** (2026-10-22 close, +3.7%, closing at the day's high of $229.81). It was a sector move: Allstate +3.2%, Chubb +2.5%, Travelers +1.6% the same day. No Progressive news was found |
| Entry zone | **None that passes the rules.** The only 2:1 band is **$203.8–204.3** (stop $195.40, T1 $222.10). At a 50-cent width it is too thin to catch with an alert and a market order. It also sits under the 200-DMA ($208.7, −0.5% over 20 sessions), which the house protocol treats as no-fresh-longs ground |
| Invalidation (stop) | None: no position. For reference, the range floor is **$200.96–201.02** (the 9/24 and 10/14 lows). A close under it opens $196.15 (4/30) and $189.20 (the 52-week low, 5/29) |
| Target 1 / 2 | Resistance: **$232.2–235.0** (the 7/2–7/13 closes and the 7/13 high) / **$239.38** (52-week high, 7/7). Above that, the 2025 highs at $248–255 |
| Reward/risk (T1) | **0.25 : 1** from $229.62, with the stop at $219.30 (under the 10/21 low of $219.59, 1.85 ATR) and T1 at $232.20. It needs ≥ 2 |
| Size | **$0.** If a setup appears: one fill ≤ $270 (8% of $3,387), about 1.2 sh at $225; risk ≤ $68 |
| Timeframe | None now. Re-check on 11/18–11/19 |
| Next earnings | **October results on Wed 11/18 before the open** (confirmed by the company on 10/14), so no buys on 11/13, 11/16 or 11/17. The Q3 10-Q comes Mon 11/2 and the Q3 call is **Tue 11/3 at 09:30 ET** (confirmed, "subject to change"). Annual variable dividend: last year's $13.50 was declared 12/5/2025, ex-date 1/2/2026. The 2026 amount and dates are unverified |

## Thesis
**Why it is on the list.** Auto insurance has nothing to do with AI capex.
- **Low correlation:** over the 60 sessions to 10/22, PGR's daily correlation with the SOX was **−0.48** (−0.43 over 250
  sessions), and its beta to the S&P was **−0.35** (−0.50 over 250).
- **Chip-crash days:** it netted +1.7% across the three days. On 10/14 it fell 4.2% on its own Q3 report, then gained 2.2%
  on 10/16 and 3.7% on 10/22.
- **Gasoline:** expensive gasoline usually means fewer miles driven and fewer claims. That link is not measured here, so
  treat it as unverified.
- **Quality:** a trailing P/E of 11.6, a 34.4% ROE and a combined ratio of 88.7 make this one of the best underwriters in
  the US.

**Why not.**
1. **The cycle has turned.** Progressive is cutting rates to keep growing, and growth is slowing anyway.
   - Net premiums written grew 5%, 6% and **2%** in July, August and September. September personal auto was +1%.
   - Policies in force grew 6.3% y/y in September, down from 11.2% in February (Piper Sandler, as quoted in 10/14–10/15
     coverage).
   - September brought the first month-on-month drop in personal auto policies since November 2023 (−27K).
   - The monthly combined ratio drifted from 86.8 to 89.3 to 90.0 over July–September.
   - Consensus EPS falls from **$18.40 (2026) to $16.24 (2027), −11.7%**. The stock is cheap on trailing earnings because
     those earnings are expected to fall.
2. **The chart is a range inside a downtrend.**
   - Since January it has traded between $189 and $239, inside a decline from the March 2025 high of $292.99.
   - The 10/22 close cleared the three-month range top ($222–225.5) on a sector rotation day, with no news and on light
     volume.
   - With ATR at 2.4% a day and the next resistance at $232–235, there is no room for a 2:1 trade with a structural stop
     1.5 ATR away.
3. **The Street sees no upside.** The consensus is Hold, and the average target ($230–234) is about the current price.

**What would turn it into a WATCH with a level:**
- **The fundamentals:** the 11/18 October report shows personal auto policies growing again month on month, with the
  monthly combined ratio at or under 90.
- **The chart:** a structure with room, meaning a base above a rising 200-DMA with at least 3 ATR between the entry and the
  next resistance.
- Re-run the levels on 11/18–11/19 with a fresh ATR. Today's ATR is inflated by the 10/14 gap. At a normal ATR (≈ $4.7) the
  2:1 band would only widen to ≈ $202.5–204.3, still under the 200-DMA.

## Chart & technicals
Source: Yahoo 1y/2y daily bars, close 2026-10-22.
- **Averages:** 20-DMA $215.49 (−0.2% over 20 sessions), 50-DMA $215.63 (+0.7%), 200-DMA **$208.74** (−0.5% over 20
  sessions, +0.04% over the last 5), so flat to falling. Price is +6.6%, **+6.5%** and **+10.0%** above them.
- **RSI(14):** **66.3**, up from 58.1 the day before. That passes the chase guard, but it rose 8 points in one day.
- **ATR(14):** **$5.57 = 2.43%** a day, inflated by the 10/14 results gap (a $21.86 true range). Excluding 10/14, the last 14
  true ranges average $4.72 (2.06%).
- **52-week range:** high **$239.38** (7/7/2026), low $189.20 (5/29/2026). Price is −4.1% from the high. The all-time high
  is $292.99 (March 2025).
- **Returns:** 5 days +7.4%, 1 month +13.0%, 3 months +7.4%, 6 months +11.8%, 1 year +3.6%. YTD +0.8% on price, about +6.8%
  including the $13.60 January dividend (not reinvested).
- **Volume:** the 10/22 breakout came on 2.35M shares, 0.8× the 20-day average (2.87M). That is weak sponsorship. The
  10/14 results day traded 7.2M.
- **Support:**
  - $222.5–225.5: the old range top (the 10/22 low $222.46, and the 8/24 $224.73, 9/3 $225.45 and 10/13 $223.78 highs).
  - $218.7–219.6: the 10/20–10/21 lows.
  - $215.5: the 20/50-DMA.
  - $212.7–213.8: the 10/15–10/16 lows.
  - $208.7: the 200-DMA.
  - **$200.96–201.02**: the double bottom of 9/24 and 10/14.
  - $196.15 (4/30), then $189.20.
- **Resistance:**
  - $229.81: the 10/22 high, a close at the high rather than a rejection.
  - **$232.2–235.0**: the July 2–13 closes and the 7/13 high.
  - **$239.38**: the 52-week high.
  - $248–255: the August–October 2025 highs.
- **Report-day moves:**
  - Quarterly reports: 7/15 −9.4% (Q2) and 10/14 −4.2% (Q3, with an intraday low of −9.8% at $201.02).
  - Monthly reports move it too: 8/19 +4.8% (July results). On 9/18 (August results) it fell 1.3%, then slid 7.1% from the
    9/17 close to the $200.96 low on 9/24.

## Fundamentals
Source: company releases of 8/19, 9/18 and 10/14/2026, unless noted.
- **Q3 2026** (reported 10/14 before the open):
  - Net premiums written $22.30B (+4%); net premiums earned $21.87B (+5%).
  - Net income $2.54B (−3%); EPS **$4.37** against $4.45 a year ago. The consensus was about $4.41–4.42 (Tickeron; search
    coverage), a narrow miss. Evercore put September operating EPS at $1.39, a beat.
  - Pre-tax realized losses −$170M.
  - Combined ratio **88.7**, against 89.5. The 2025 year-to-date line includes a **$950M policyholder credit expense**
    (Florida), worth about 4.6 points on Q3'25 premiums of $20.85B. A secondary source puts it in Q3'25, and September 2025's
    combined ratio of 100.4 fits. Without it, last year's quarter ran ≈ 84.9, so 2026 is ≈ 3.8 points worse underneath.
- **Monthly results:**

  | Month | Premiums written | Combined ratio (a year earlier) |
  |---|---|---|
  | July | +5% | 86.8 (85.3) |
  | August | +6% | 89.3 (83.1) |
  | September | **+2%** (agency auto +1%, direct auto +1%) | 90.0 (100.4) |
- **Policies in force on 9/30:** 40.489M (+6% y/y).
  - Agency auto 11.347M (+7%), direct auto 16.848M (+8%), special lines 7.390M (+6%), property 3.652M (0%), commercial
    1.252M (+5%).
  - **Against 8/31:** total −3K. Personal auto −27K: direct −31K, agency +4K.
- **Year to date, 9 months:** premiums written $67.0B (+5%), combined ratio 87.5, favorable prior-year reserve development
  $1.54B, net income $8.67B, EPS $14.83. Property is only 3.6% of premiums written.
- **Balance sheet, 9/30:**
  - Book value per share **$59.51**, down from $60.92 on 8/31 because of bond marks. Unrealized losses on fixed maturities
    are **−$3.46B**, of which −$1.66B came in September alone.
  - Duration 3.6 years, credit quality AA−. Debt/capital 19.6%. Investment book yield 4.3%.
  - Trailing ROE 34.4% on net income, 25.7% on comprehensive income.
  - Shares outstanding 579.5M. Buybacks: 969,262 shares in September at $207.92.
- **Pricing:**
  - Rate cuts are spreading: Louisiana approved −6.6% (1/7/2026); Texas lists Progressive filings down, including one at
    −6% (TDI, 10/8/2026); Florida's five largest auto writers are at about −8% for 2026 (state release, 3/5/2026).
  - The Q2 10-Q (as quoted in search coverage) reports personal auto policy life expectancy −8% y/y, meaning more customers
    shop and switch.
- **Valuation (10/22):**
  - P/E **11.6** trailing (EPS TTM $19.85) and **14.3** forward.
  - P/B **3.86** on 9/30 book. Market cap $133B.
  - The 5-year median P/E of 19.4 comes from a GuruFocus snippet: unverified. The historical P/B range is unverified.
- **Consensus EPS:** 2026 $18.40, 2027 **$16.24** (−11.7%) (Stockanalysis, 10/22).
- **Dividend policy:** $0.10 a quarter plus an annual variable dividend set in December from the capital position. The last
  one was $13.50, declared 12/5/2025, ex-date 1/2/2026, paid 1/8/2026. The 2026 amount is unknown.
  - **Practical note:** an ex-date drop of $13.50 is about 6% of the price (≈ 2.4 ATR).
  - A broker stop sitting close under the price in late December would fire on the dividend, not on news.
  - Any future position must plan the stop around the ex-date.

## News & catalysts
**Last 30 days**
- **9/1** — CEO Tricia Griffith sold 37,338 shares at $219.50 (≈ $8.2M; Form 4). — *neutral*
- **9/18** — August results: premiums written +6%, combined ratio 89.3, policies +7%. The stock then fell to $200.96 by
  9/24. — *neutral*
- **10/14** — Q3 and September results: EPS $4.37 (a small miss), combined ratio 88.7 (better), September premiums written
  only +2%, and the first month-on-month drop in personal auto policies since November 2023. The stock closed −4.2%, with an
  intraday low of −9.8%. — *breaking* (growth)
- **10/14–10/19 — analyst target changes:**
  - Evercore ISI $230 → $227, In Line (10/14): "a step back", EPS trimmed 2%.
  - KBW $252 → $246, Outperform (10/15).
  - Wells Fargo $201 → $196, Underweight (10/15).
  - Roth Buy $245 (10/15).
  - Goldman Buy, $233–235 (the two sources give conflicting dates).
  - Morgan Stanley Hold $210 (10/16).
  - UBS $234 → $238, Neutral (10/19).
  - BofA $314 → $266: one search summary only, not confirmed — **unverified**.
  - Overall: *breaking/neutral*.
- **10/22** — +3.7%, alongside other insurers and utilities (XLU +2.1%) on the chip-crash day. That is rotation, not company
  news. — *neutral*
  - The same day, CIO Steven Broz filed a Form 144 to sell 1,225 shares (≈ $274K), the fourth monthly sale of that size
    (7/23, 8/20, 9/24, 10/22).

**Next 90 days**
- 10/27–28 — FOMC.
- 11/2 — 10-Q.
- 11/3 — Q3 call (questions to the CEO and CFO) and the midterms.
- **11/18 — October results.**
- ≈ Mid-December — November results (unverified).
- ≈ Early December — annual dividend declared (unverified).
- 11/30 — the hurricane season ends.
- December — FOMC (date unverified).

## Positioning & sentiment
- **Analysts:** consensus **Hold**.
  - Stockanalysis: 24 analysts, average target **$230.38** (range $196–266).
  - MarketBeat: 23 analysts (2 Sell / 12 Hold / 9 Buy), average **$234.45** (range $196–314).
  - Both are as of 10/22. The average target is 0–2% above the price.
- **Short interest:** 6.81M shares = **1.18% of float**, 2.5 days to cover (Stockanalysis; the settlement date is not
  shown). Nobody is leaning against it.
- **Insiders:** sellers only — the CEO's $8.2M on 9/1 and the CIO's monthly lots of about $0.25M. GuruFocus counts $30.6M of
  insider sales over 12 months (not opened in full: unverified). No insider buys were found.
- **Crowding:** insurers are part of the defensive rotation the 10/23 screen flagged. On 10/22 Travelers' RSI was 77.3 and
  Chubb's 70.5. PGR's RSI of 66.3 is under the guard, but buying it now is chasing the same rotation.
- **Beta (5-year):** 0.24 (Stockanalysis).

## What would make me wrong
- **A rerating without a pullback.** An October report on 11/18 with policies growing again and a combined ratio under 90,
  plus a December annual dividend near last year's $13.50 (about 5.9% of today's price), could carry the stock through $239
  toward the 2025 levels ($248–255) without ever offering a 2:1 entry. That is the cost of the rule.
- **A deeper soft market.** If rate cuts keep spreading and advertising keeps rising, the 2027 EPS decline could be worse
  than −12%. A close under **$200.96** would confirm it and open $189.
- **Bond marks.** Higher yields keep cutting book value (−$1.66B in September alone).
- **One bad month.** Catastrophes or reserve charges can swing a monthly report by several points. Property is small
  (3.6% of premiums), but the July and October 2026 report days show 4–10% gaps are normal for this stock.
- **Plan constraint.** Even with a setup, PLAN §1 allows only one non-AI satellite, and TTWO holds it. A buy needs plan change
  (a), and no buys are allowed before 11/2 (the circuit breaker fired 10/22).

## Sources
- Yahoo chart API: PGR, ^SOX, ^GSPC (2y daily) and ALL, TRV, CB, XLF, XLU (10d), fetched 2026-10-22 22:13 UTC (latest bar
  10/22)
- Q3 and September results, 8-K 2026-10-14 — https://www.sec.gov/Archives/edgar/data/80661/000008066126000367/pgr202609ex99earningsrelea.htm
- August results, 8-K 2026-09-18 — https://www.sec.gov/Archives/edgar/data/80661/000008066126000322/pgr202608ex99earningsrelea.htm
- July results, 8-K 2026-08-19 — https://www.sec.gov/Archives/edgar/data/80661/000008066126000315/pgr202607ex99earningsrelea.htm
- Form 144, S. Broz, 2026-10-22 — https://www.sec.gov/Archives/edgar/data/80661/000195917326007447/primary_doc.xml
- Form 4, T. Griffith, sale 2026-09-01 — https://www.sec.gov/Archives/edgar/data/80661/000008066126000319/form4.xml
- Q2 10-Q, filed 2026-08-03 (quoted via search coverage) — https://www.sec.gov/Archives/edgar/data/0000080661/000008066126000308/pgr-20260630.htm
- Tickeron Q3 review, 2026-10 — https://tickeron.com/blogs/progressive-pgr-q3-2026-earnings-underwriting-strength-meets-growth-slowdown-19377/
- The Insurer, 2026-10-15 (headline only; paywalled) — https://www.theinsurer.com/ti/news/progressive-shares-fall-4-after-drop-in-month-over-month-pif-2026-10-15/
- Colby (Substack) Q3 review, 2026-10-15 — https://investwithcolby.substack.com/p/progressive-pgr-q3-fy2026-earnings
- GuruFocus, Evercore cut, 2026-10-14 — https://www.gurufocus.com/news/9123720/evercore-isi-lowers-progressive-pgr-price-target-amid-policy-decline-concerns
- Stockanalysis forecast and statistics, 2026-10-22 — https://stockanalysis.com/stocks/pgr/forecast/ · https://stockanalysis.com/stocks/pgr/statistics/
- MarketBeat forecast, 2026-10-22 — https://www.marketbeat.com/stocks/NYSE/PGR/forecast/
- Dividend declaration, 2025-12-08 — https://investors.progressive.com/financials/financial-news-releases/news-details/2025/Progressive-Announces-Dividend-Information-And-2026-Annual-Meeting-Record-Date/default.aspx
- Louisiana rate decrease, 2026-01-07 — https://ldi.la.gov/news/press-releases/1-7-26-progressive-approved-for-personal-auto-rate-decreases
- Texas rate filings, 2026-10-08 — https://www.tdi.texas.gov/news/2026/tdi10082026.html
- Florida auto rate decreases, 2026-03-05 — https://myfloridacfo.com/news/pressreleases/press-release-details/2026/03/05/icymi--commissioner-mike-yaworsky-announces-more-significant-auto-rate-decreases-for-florida's-top-5-auto-insurance-groups
- Screen that put PGR on the list: `journal/2026-10-23-diversifier-screen.md`
