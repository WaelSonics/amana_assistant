# JNJ — Johnson & Johnson — research log

One file per ticker; newest entry first. Each entry is dated; numbers are as of that date.

Entries:
- 2026-10-28 (deep dive, v5-candidate refresh with levels.py checks)
- 2026-10-23 (deep dive, non-AI diversifier screen)

---

## JNJ — Johnson & Johnson — deep dive 2026-10-28

**Verdict:** WATCH. **v5 candidate, not buyable under v3**: §1 allows ≤ 1 non-AI satellite, and TTWO holds it. Board alert
**$250.75** (zone $250.00–250.75). · **Conviction:** Med. It is the best-behaved diversifier of the four, and it is the only
one on the §11 compounder list. But at $271.98 it is back in the top quarter of its $245–281 range, at 23.4× 2027 EPS. A
rule-checked entry is still ≈ 8% lower.

| | |
|---|---|
| Price (date) | **$271.98** (levels.py, 2026-10-28 11:07 ET; intraday high $272.42). Close 10/27: $268.73 |
| Entry zone | **$250.00–250.75. Alert at $250.75**, then a market order. It can be bought from 11/2 only after a plan change (see "Plan status"). The zone is the 10/13–10/19 post-earnings base (closes $248.61–253.91) and the 8/4 swing low $250.44, above the rising 200-DMA ($246.41). On 10/23 it was $250.00–251.50. The top is $0.75 lower because T1 is now the 10/26 rejection high |
| Invalidation (stop) | **$240.00**, under the 10/13 low $245.17, the 7/21 low $245.49 and the 200-DMA. That is 1.54–1.66 ATR, or 4.0–4.3%. Hard exit at −15% ≈ $213 (the stop comes first). **Event:** the thesis-break exits below |
| Target 1 / 2 | **T1 $272.36**: the 10/26 high, which closed at $266.30. It is the lowest rejection high in the $272.4–276.5 band, and today's high ($272.42) tested it. **T2 $281.07**: the record high (9/2). levels.py's first swing resistance is $274.90 (7/28) |
| Reward/risk (T1) | **2.24 / 2.12 / 2.01 : 1** at the low / mid / high of the zone (levels.py, pasted below). At today's price, no stop ≥ 1.5 ATR away gives 2:1 to either $272.36 or $274.90 |
| Size | One fill of **$190 = 5.5%** of $3,426 ≈ 0.76 sh. **Risk to the stop $7.87 = 0.2%** (cap $69) |
| Timeframe | Months, as a v3 trade to T1. Years, if it is held as a v5 compounder |
| Next earnings | **≈ 2027-01-25/26, not confirmed.** MarketScreener projects 1/25 and Investing.com lists 1/26; the Q4 2025 report was on 1/21/2026. levels.py says "not in the 3-month calendar". At ≈ 60 sessions away, the blackout is not an issue |

**levels.py JNJ** (2026-10-28 11:07 ET, Yahoo daily bars):
```
JNJ  $271.98 (2026-10-28 11:07 ET); last daily bar 2026-10-28 close $271.98
  20/50/200-DMA  259.16 / 265.47 (rising) / 246.41 (rising)   price vs 50 +2.5%, vs 200 +10.4%
  RSI(14) 60.3   ATR(14) $6.48 = 2.4% a day   52-wk 184.66–281.07 (-3% from the high)
  Trend: above a rising 200-DMA
  Chase guard: ok
  Next report: not in the 3-month calendar (ETF, or more than 3 months away)
  Swing support below: 263.83, 260.68, 250.44   resistance above: 274.90, 275.23, 276.47
```
**Zone check:** `levels.py JNJ --zone 250.00-250.75 --stop 240 --target 272.36 --size 190 --sleeve 3426`
```
  Setup: zone 250.00–250.75, stop 240.00, T1 272.36
    at low     250.00: R/R 2.24:1, stop 1.54 ATR (4.0%)   ✓
    at mid     250.38: R/R 2.12:1, stop 1.60 ATR (4.1%)   ✓
    at high    250.75: R/R 2.01:1, stop 1.66 ATR (4.3%)   ✓
    size $190 ≈ 0.7589 sh at the mid; risk to stop $7.87 = 0.2% of $3,426   ✓ ≤ 2%
    price 271.98 is +8.5% above the zone — wait for the alert at 250.75
```
The 10/23 zone fails at its top against the new T1. With `--zone 250.00-251.50 --stop 240 --target 272.36`, the result is
`at high 251.50: R/R 1.81:1, stop 1.77 ATR (4.6%)   ✘ R/R < 2`. Against levels.py's own first resistance, $274.90, it
still passes: 2.49 / 2.25 / 2.03. The alert moves to $250.75 so that it passes under either reading of T1.

**Rule check at the zone:**
- Chase guard ✓: today RSI 60.3 and +2.5% over the 50-DMA; both will be lower in the zone.
- Price is above a rising 200-DMA ✓.
- The stop is ≥ 1.5 ATR and ≤ 15% away ✓.
- R/R ≥ 2:1 at the low, mid and high ✓.
- Risk ≤ 2% of the sleeve ✓.
- No report within 3 sessions ✓. The ex-dividend date (11/24) does not block a buy.

**Re-check on the alert day:** the zone floor is $240 + 1.5 × ATR(14). If ATR(14) is above $6.67, a fill at $250.00 breaks
the 1.5-ATR rule.

**Plan status:**
- **v3 as written:** cannot be bought (≤ 1 non-AI satellite; TTWO holds the slot). The client's pause also blocks every buy
  until 11/2.
- **v5 (§11, decided on 12/31):** JNJ is one of the six named compounders.
  - Bought in fixed-date tranches on the first trading day of January (2027-01-04) and of February.
  - Each tranche ≈ 5% of the sleeve (≈ $171 today).
  - Only while ≤ 35× forward earnings: now 24.5× 2026 and 23.4× 2027 EPS ✓.
  - **No price stop.** The thesis-break exits below replace it.
- **The $250.75 alert** is a v3-rule setup for the board to carry. It is not how v5 would buy.

### What changed since 10/23
- **Price:** $267.61 (10/22 close) → $271.98 (+1.6%). The rally took back the 50-DMA and tested the 10/26 high. RSI 57.2 →
  60.3; ATR $6.44 → $6.48.
- **T1 is lower.** On 10/26 JNJ printed a rejection high at $272.36 and closed at $266.30. Counting that high as the first
  resistance cuts the zone top from $251.50 to $250.75. The $240 stop is unchanged.
- **Chips bounced and JNJ held its gains.** From the 10/22 close to 11:07 ET today the SOX rose 7.6% (+2.8% on 10/26,
  +3.6% on 10/27), and JNJ rose 0.9% on each of those days. The 10/23 caveat (the rotation reverses when chips rebound) has
  not happened yet.
- **Talc:** about 87.5% of the remaining ovarian claims have signed up to the deal (66,500 claimants through 313 firms;
  Law.com, 10/19). It needs 95%. On 10/23 J&J also won an Ohio mesothelioma trial (Law360, search summary).
- **ESMO data:**
  - 10/24: perioperative ERLEADA cut the risk of recurrence or death by 62% in high-risk prostate cancer (PROTEUS sub-study).
  - 10/25: a RYBREVANT FASPRO combination showed a 77% response rate in first-line head-and-neck cancer.
- **Analysts:** every action on 10/26–10/28 was a maintain (Goldman $280, UBS $320, Scotiabank $305, RBC $280, Leerink
  $272). The average target is $279.41, +2.7% from here (StockAnalysis, 10/28).
- **Valuation is a little richer:** 23.0× → 23.4× 2027 EPS. The $11.62 consensus is unchanged.

### Thesis scorecard (v5 compounder candidate)
| Pillar (falsifiable) | What was expected | Status (dated) | Trend |
|---|---|---|---|
| Innovative Medicine grows ≥ 5% operationally while Stelara erodes | ≥ +5% | Q3 +7.9% op. (10/13; 10/23 entry) | stable |
| MedTech grows ≥ 4% operationally | ≥ +4% | Q3 +2.5%, the second miss in a row (10/13) | **weakening** |
| The adjusted-EPS guide is held or raised | 2026 ≥ $11.05–11.15 | raised 10/13; consensus $11.12 (StockAnalysis 10/28) | stable |
| 2027 EPS absorbs the deal dilution | consensus ≥ $11.5 | $11.62 (StockAnalysis 10/28); it was $12.83 ≈ 90 days before 10/22 | stable since 10/22 |
| The ovarian talc deal reaches 95% | ≥ 95% sign-up | ≈ 87.5% (Law.com 10/19) | improving, still open |
| The dividend is kept | no cut | $1.34 a quarter, declared 10/13; ex-dividend 11/24 | stable |

**Thesis-break exits (under v5 these replace the price stop):**
1. The ovarian talc settlement fails: 95% is not reached and J&J walks away, so ≈ 66,000+ claims go back to trial.
2. Two cuts in a row to the adjusted-EPS guide that acquisitions do not explain. Or a 2027 guide (at the 12/8 review or the
   January report) that implies lower EPS than in 2026.
3. The dividend is cut or frozen.

**Disconfirming evidence:** two MedTech misses in a row. 2027 EPS fell from $12.83 to $11.62 in about 90 days. Insiders only
sold through September (10/23 entry). Erste cut it to Hold on valuation (10/21).

**Conviction: Med.**
- **Up to High** if the talc deal closes at ≥ 95% and the 12/8 review shows 2027 EPS growth of ≥ 5%.
- **Down to Low** on a third MedTech miss.

## Thesis
The 10/23 thesis stands. This week supported its diversifier half. On the two biggest chip-rebound days JNJ still rose, so
it is not simply the other side of the semis trade.

**For it:**
- Innovative Medicine grows ≈ 8% now that most of the Stelara cliff is in the base.
- The talc overhang is closer to capped than at any time in years (87.5% signed up).
- The 12/8 Enterprise Business Review is the next re-rating event: the 2027 outlook and the orthopaedics separation.

**Against it:**
- 23.4× 2027 EPS for ≈ 4.5% EPS growth.
- A sector the market has just crowded into.
- Analyst targets only 2.7% above the price.

So the entry still has to be low. The v5 tranches remove the timing question, but not the valuation question.

## Chart & technicals
Source: levels.py, 2026-10-28 11:07 ET. Daily closes come from levels.py's Yahoo cache.

**Trend**
- Above a rising 20-DMA ($259.16).
- Above a flat 50-DMA: $265.47 now vs $265.35 ten sessions ago; levels.py calls that "rising".
- Above a rising 200-DMA: $246.41 now vs $241.26 twenty sessions ago.
- Price is +2.5% over the 50-DMA and +10.4% over the 200-DMA.

**Momentum and volatility:** RSI(14) 60.3; ATR(14) $6.48 = 2.4% a day. The chase guard passes.

**Range:** the 52-week range is $184.66–281.07, and price is 3% under the record. Since July the range has been $245–281,
and price is in its top quarter.

**Last week (closes):**

| Date | Close | Change | Note |
|---|---|---|---|
| 10/23 | $263.81 | −1.4% | |
| 10/26 | $266.30 | +0.9% | high $272.36 |
| 10/27 | $268.73 | +0.9% | |
| 10/28 | $271.98 (11:07 ET) | | high $272.42 |

Volume on 10/23–10/27 was 5.3–5.8M shares a day, against a 20-day average of 7.8M. The push came on light volume.

**Support** (levels.py swing lows):
- $263.83 (8/27).
- $260.68 (9/15).
- **$250.44 (8/4): the zone.**
- $245.17 / $245.49 (10/13, 7/21) and the 200-DMA.
- Stop $240.

**Resistance:**
- $272.36–272.42: the 10/26 high and today's high. levels.py cannot see them yet, because its swing finder needs 5 bars
  after a pivot.
- levels.py's swing highs: $274.90 (7/28), $275.23 (9/24), $276.47 (8/19).
- $281.07: the record.

**Why the zone sits this low:** with ATR at $6.48, a 2:1 trade with a stop ≥ 1.5 ATR away needs ≥ 3 ATR ($19.4) of room to
T1. So nothing above ≈ $252.9 qualifies. With the stop at $240, under the double bottom with room to spare, the window that
qualifies is $249.72–250.79. Each $1 lower on the stop widens that window by $0.33.

## Fundamentals
**Q3 2026 and guidance** (reported 10/13; from the 10/23 entry, not re-fetched):
- Sales $25.4B (+5.9%); adjusted EPS $2.59.
- Innovative Medicine +7.9% operationally; MedTech +2.5%, a miss.
- 2026 guidance raised: sales $101.0–101.4B, adjusted EPS $11.05–11.15.

**Consensus** (StockAnalysis, 10/28):

| | 2026 | 2027 |
|---|---|---|
| EPS | $11.12 (+3.1%) | **$11.62 (+4.5%)** |
| Revenue | $101.22B (+7.5%) | $107.75B (+6.5%) |

**Valuation** (StockAnalysis, 10/28 10:58 ET, price $272.24):
- Forward P/E 24.47; trailing P/E 41.35 (depressed by the talc charge).
- PEG 3.28; EV/EBITDA 19.61.
- My calculation: 23.4× 2027 EPS at $271.98.
- Dividend yield 1.97%.

**Cash flow and balance sheet** (StockAnalysis, 10/28):
- FCF (TTM) $20.59B = a 3.17% yield.
- Debt $44.65B, cash $17.23B → **net debt $27.42B**.
- The 10/23 entry, using the 9/27 balance sheet, had debt $49.0B and cash & securities $20.8B (net $28.3B). The two sources
  define debt and cash differently; their net-debt figures differ by only $0.9B.
- Share count +0.80% year on year.

**Margins (TTM):** gross 67.77%, operating 26.59%, net 16.20%.

**v5 valuation gate (≤ 35× forward):** passes at 24.5×.

## News & catalysts (last 30d / next 90d)
Items new since 10/23 are marked ★.

**Last 30 days:**
- ★ 10/27 — **Investor "investigation".** Pomerantz announced an investigation on behalf of JNJ investors (GlobeNewswire).
  The page returned 403, so what it concerns is unverified. Law firms routinely announce these after a drop. *Neutral*
  unless a suit is filed.
- ★ 10/26–10/28 — **Analyst maintains** (StockAnalysis). *Neutral.*
  - 10/26: Goldman $280, UBS $320, Scotiabank $305.
  - 10/28: RBC $280, Leerink $272.
- ★ 10/25 — **RYBREVANT FASPRO** combination: 77% overall response rate in first-line advanced head-and-neck cancer (J&J
  release). *Confirming.* The 10/23 entry noted that an FDA decision in head-and-neck cancer is expected by year-end.
- ★ 10/24 — **PROTEUS sub-study** (ESMO LBA53): perioperative ERLEADA + ADT cut the risk of recurrence or death by 62% vs
  surgery alone in high-risk prostate cancer (Urology Times, CancerNetwork, 10/24). *Confirming.* The drug is still
  investigational in this setting.
- ★ 10/23 — **Talc:** an Ohio jury found for J&J in a mesothelioma wrongful-death trial (Law360, search summary).
  *Confirming.*
- ★ 10/19 — **Talc:** Law.com reports that 313 firms representing ≈ 66,500 ovarian claimants (≈ 87.5%) have signed. A
  Massachusetts mesothelioma trial opened; mesothelioma is not covered by the deal. Law.com calls it a $5.8B settlement;
  other sources say $5.5B. *Confirming, pending.*
- 10/22 — **ACR and APHRS:** 43 presentations at ACR, including late-breaking ICOTYDE psoriatic-arthritis data; real-world
  pulsed-field-ablation data at APHRS (J&J releases). JNJ rose 3.8% that day while the SOX fell 6.7%. *Confirming.*
- 10/13 — **Q3:** a beat and a raise, a MedTech miss and a talc charge; the stock fell 5.7%. *Neutral.*

**Next 90 days:**
- **11/3** — US midterm elections; drug-pricing headlines.
- **11/24** — ex-dividend, $1.34 (Yahoo, via search 10/28).
- **12/8** — Enterprise Business Review: the 2027 outlook and the pipeline. The date was set in J&J's Q1 release and
  repeated on the Q3 call (search summaries); J&J's newsroom listed "J&J will host an enterprise business review" on 10/27.
- **Date unknown** — whether the talc deal reaches 95%. This is binary.
- **≈ 1/25–1/26/2027** — Q4 results and the 2027 guide. Not confirmed.

## Positioning & sentiment
- **Analysts** (StockAnalysis, 10/28): consensus Buy. 11 Strong Buy, 5 Buy, 6 Hold, 0 Sell, 1 Strong Sell. Average target
  $279.41 (+2.7%), median $280.50, range $190–320.
- **Short interest:** 22.07M shares = 0.92% of float (StockAnalysis 10/28; settlement date not shown). Not a factor.
- **Insiders:** sales only, through September (10/23 entry; not re-checked).
- **Crowding:**
  - Health care is still the rotation trade.
  - JNJ's past week was a steady climb of +0.9% a day on below-average volume, not a squeeze.
  - XLV holds 9.96% JNJ (SSGA 10/27), so sector flows reach it directly.

## What would make me wrong
- **Up and away:** JNJ closes above $272.4, then above the $274.9–276.5 band, and runs to the $281 record without pulling
  back.
  - The zone never fires. That is acceptable.
  - At a new record there is no resistance to measure 2:1 against: re-derive, don't chase.
  - Under v5 it would not matter: the January tranche buys at market if the stock is ≤ 35× forward earnings.
- **Through the zone:** a close under $240 breaks the post-earnings double bottom and the 200-DMA together. Likely causes:
  - the talc deal fails;
  - a third MedTech miss;
  - a weak 2027 outlook at the 12/8 review.
- **De-rating:** at 23.4× for ≈ 4.5% EPS growth, a soft 2027 guide could cost 10% even without bad news.

## Sources
**Price and technicals**
- levels.py JNJ (Yahoo chart API): output and setup check at 2026-10-28 11:07 ET; chart
  `/tmp/claude-1000/-home-waelas-wael-amana-amana-assistant/cf7235bd-03e5-456e-8948-a8c2229a57bd/scratchpad/charts/JNJ.png`.
  Earnings calendar from Alpha Vantage (demo key; cached 10/27).
- https://www.heygotrade.com/en/us-stock/jnj/ — 10/27 close and ex-dividend date (search summary), fetched 2026-10-28.

**Company and fundamentals**
- https://stockanalysis.com/stocks/jnj/statistics/ — 2026-10-28 10:58 ET.
- https://stockanalysis.com/stocks/jnj/forecast/ — 2026-10-28.
- https://www.jnj.com/media-center/press-releases — release headlines 10/19–10/27, fetched 2026-10-28.
- https://www.jnj.com/media-center/press-releases/johnson-johnson-to-host-enterprise-business-review — the 12/8 review
  (search summary).
- https://www.ssga.com/us/en/intermediary/etfs/state-street-health-care-select-sector-spdr-etf-xlv — JNJ at 9.96% of XLV,
  as of 2026-10-27.

**Talc**
- https://www.law.com/2026/10/19/another-talc-trial-opens-as-jj-gets-support-for-58b-settlement/ — 2026-10-19.
- https://www.law360.com/articles/2542050/j-j-wins-ohio-talc-mesothelioma-trial — 10/23 verdict (search summary).
- https://www.globenewswire.com/news-release/2026/10/27/3389777/1087/en/investor-alert-pomerantz-law-firm-investigates-claims-on-behalf-of-investors-of-johnson-johnson-jnj.html
  — 2026-10-27 (403; title only).

**ESMO data**
- https://www.urologytimes.com/view/proteus-substudy-perioperative-apalutamide-plus-adt-improves-efs-vs-surgery-alone —
  2026-10-24.
- https://www.cancernetwork.com/view/apalutamide-adt-improves-efs-vs-surgery-alone-in-high-risk-prostate-cancer — 2026-10-24.

**Next report date (projections)**
- https://www.marketscreener.com/quote/stock/JOHNSON-JOHNSON-4832/calendar/ — search summary.
- https://uk.investing.com/equities/johnson-johnson-earnings — search summary.

**Sector**
- https://finance.yahoo.com/healthcare/articles/stocktwits-pharma-pulse-big-pharma-022829910.html — 2026-10-26.

**Unverified:**
- the Q4 report date;
- what the Pomerantz notice concerns;
- whether the 95% talc threshold has been met, and its deadline;
- the deal size ($5.5B vs $5.8B);
- the Ohio verdict details (search summary only).

---

## JNJ — Johnson & Johnson — deep dive 2026-10-23 (non-AI diversifier screen)

**Verdict:** WATCH. Buy from 11/2 only in the zone · **alert at $251.50** · **Conviction:** Med. It is the best
diversifier on the screen: 60-day correlation with the SOX is −0.50 and the ATR is 2.4% a day. But at $267.61 it is
only 3% under real resistance and trades at 23× next year's earnings. From here the best structural stop pays about
0.5:1. It only qualifies on a pullback into the post-earnings base.

| | |
|---|---|
| Price | **$267.61** (close 2026-10-22, +3.8%, high $269.67, 10.1M shares vs a 7.8M 20-day average). No 10/23 bar yet: data fetched 10/22 18:12 ET |
| Entry zone | **$250.00–251.50, from 11/2 — alert at $251.50**, then a market order. This is the 10/13–10/19 post-earnings base (closes $248.61–253.91, 10/19 low $251.50), just above the rising 200-DMA (≈ $247 by 11/2) |
| Invalidation (stop) | **$240.00**, under the 10/13 gap low $245.17, the 7/21 low $245.49 and the 200-DMA. That is $10.75 under the zone mid = **1.67 × ATR** (1.55× at $250, 1.79× at $251.50). Hard exit −15% from cost ≈ $213 (the stop comes first). **Event:** the ovarian-talc deal fails its 95% sign-up, or a second MedTech miss comes with a guidance cut |
| Target 1 / 2 | **T1 $275** (bottom of the sell zone $275–281: the 9/24 lower high $275.23 and the 9/3 record close $278.43) / **T2 $281** (record high $281.07, 9/2). First hurdle on the way: $264–270 (50-DMA, 10/12 and 10/22 highs) |
| Reward/risk (T1) | **2.26:1 at the zone mid $250.75** (+$24.25 / −$10.75) · 2.04:1 at $251.50 · 2.5:1 at $250 · 2.8:1 to T2. **At today's $267.61: about 0.5:1** (stop $254 under the 10/21 low → −$13.6 vs +$7.4) → no buy at this price |
| Size | One fill of **$270 = 8.0% of $3,387** → **≈ 1.07 sh** at $251.50 (1.08 at $250). **Risk to the stop ≈ $12** (0.4% of the sleeve; cap $68). Full 10–15%: one later add ≤ 4% (≈ $135), only after a close back above the 50-DMA (≈ $264) |
| Timeframe | 1–3 months: T1 before the January report |
| Next earnings | **≈ 1/19–1/21/2027, not confirmed** (Quartr lists 1/19, but that page is stale). Last report: **10/13/2026** (confirmed) → −5.7% that day |

**Rule check at the zone:** the zone is ≈ 5% under the 50-DMA and RSI is well under 70, so the chase guard passes ✓ · the
stop is ≥ 1.5 ATR away ✓ · R/R ≥ 2:1 across the whole zone ✓ · no earnings within 3 sessions ✓ · ex-dividend 11/24 is not
a blocker. **If the ATR(14) on the alert day is above $6.67**, a fill at $250 breaks the 1.5-ATR rule: re-check it on the day.
**Plan flag (§1):** satellites are "≤ 1 non-AI" and TTWO appears to fill that slot. Owning JNJ needs that line changed (the
10/22 post-mortem's AI-semis cap points the same way) or TTWO replaced. That is the client's call.

## Thesis
- **Why it fits the account.** From 7/23 to 10/22, the 60-day correlation of daily returns with the SOX was **−0.50**
  (20-day −0.55, 120-day −0.45), and its 60-day beta to the S&P 500 was −0.43. On the three chip-crash days JNJ rose
  **+2.13% (10/14), +0.90% (10/16) and +3.81% (10/22) = +6.8%**, while the SOX fell −4.30%, −3.83% and −6.72%. Its 60-day
  annualized volatility is 24% and its ATR 2.4% a day, so it is a calm line next to AMD/MU.
- **The business is not just "defensive".** Innovative Medicine grew **+7.9% operationally in Q3** even with Stelara
  **−54%**. Most of the Stelara cliff is already in the base. The growth comes from Tremfya (+68%), Darzalex (+16%),
  Carvykti (+35%), Rybrevant (+64%) and the Icotyde pill (approved March 2026; more than 20,000 patients started).
- **What the market may be missing (my reading, not a fact):** the 2027 EPS consensus fell **$12.83 → $11.62 in 90
  days**, mostly from the Sail deal ($1.28 of the $1.36 2027 dilution). J&J's 7/29 8-K says that figure *assumes Sail hits
  milestones and J&J exercises its option*. If the option is not exercised, the 2027 bar is too low. Also, the ovarian-talc
  overhang is closer to being capped than at any time in years ($5.5B deal; the MDL court ordered plaintiffs on 7/22 to show
  cause after they withdrew experts).
- **Against it:** 23× forward earnings for ≈ 4–5% EPS growth, a sector that has just had a fast rotation into it, and only
  +4% to the analysts' average target. That is why the entry has to be low.

## Chart & technicals
(Yahoo daily bars to the 10/22 close; Wilder RSI/ATR.)
| | |
|---|---|
| 20 / 50 / 100 / 200-DMA | $259.39 (falling, −2.1% over 10 sessions) / **$265.17** (flat) / $257.48 (rising) / **$245.19** (rising, +1.05% over 10 sessions) |
| Price vs averages | **+0.9% over the 50**, +9.1% over the 200. 10/22 was the **first close above the 50-DMA since 9/29** (16 sessions under) |
| RSI(14) · ATR(14) | **57.2** · **$6.44 = 2.41% a day** |
| 52-wk high / low | **$281.07 (2026-09-02)** / $184.66 (2025-10-29) · −4.8% from the high · record close $278.43 (9/3) |
| Returns | 5d +5.7% · 20d −1.1% · 60d +0.8% · 120d +17.8% · 250d +39.0% |
| Earnings-day moves | **10/13/2026 −5.7%** · 4/14/2026 +0.9% · 1/21/2026 −0.1% · 10/14/2025 0.0% |

- **Structure:** after the 9/2 record ($281.07) it made lower highs ($275.23 on 9/24, $264.39 on 10/12). The 10/13 report
  gapped it to $245.17, a double bottom with the 7/21 low ($245.49) and right on the 200-DMA. Five sessions of base
  followed ($248.61–255.56 closes), then a +3.8% day on 10/22 took out the 10/12 high. The short-term trend has turned
  up. The bigger picture is still a **$245–281 range since July**, with price in its upper third.
- **Swing points (6 months):** highs 7/7 $269.43 · 7/28 $274.90 · 8/19 $276.47 · 9/2 $281.07 · 9/24 $275.23 · 10/12
  $264.39 · 10/22 $269.67. Lows 6/22 $227.50 · 7/21 $245.49 · 8/4 $250.44 · 8/27 $263.83 · 9/15 $260.68 · **10/13 $245.17**.
- **Support:** $264.4–265.2 (10/12 high, 50-DMA) · $259.4–260.7 (20-DMA, 9/15 low) · $257.5 (100-DMA) ·
  **$248.6–253.9 (post-earnings base) = buy zone** · $245.2–245.5 + 200-DMA · stop $240 · then $227.5 (6/22 low).
- **Resistance:** $269.7 (10/22 high) · **$275.2** (9/24) · $278.4 (record close) · **$281.1** (record).
- **Why the zone is so low:** with an ATR of $6.44, a 2:1 trade with a stop ≥ 1.5 ATR away needs ≥ 3 ATR ($19.3) of room
  to T1 $275. No entry above ≈ $255.7 can qualify.

## Fundamentals
- **Q3 2026 (reported 10/13):** sales **$25.4B, +5.9%** reported / +6.0% operational vs ≈ $25.37–25.38B expected. Adjusted
  EPS **$2.59** vs $2.52–2.53 (−6.8% y/y; it includes ≈ $1B of Firefly in-process R&D). GAAP EPS $0.09 after ≈ $7B of
  special items, **including the $5.5B ovarian-talc charge**. Innovative Medicine $16.8B (+7.9% op.). **MedTech $8.6B (+2.5%)
  vs ≈ $8.71B expected: a second straight miss**, weak outside the US (Abiomed −1.5%, Shockwave +17%). Stelara $716M (−54%),
  Tremfya $2.4B, Darzalex $4.24B (vs ≈ $4.4B expected).
- **2026 guidance (10/13):** sales **$101.0–101.4B** (+7.2–7.6%) and adjusted EPS **$11.05–11.15**, both raised. The EPS
  guide had been cut on 7/29 for the Firefly/Sail deals. Deal dilution: 2026 −$0.64, **2027 −$1.36** (7/29 8-K).
  Operating margin is guided ≈ 60 bp lower; the adjusted pre-tax margin was 30.2% in Q3 (35.2% a year ago).
- **Consensus (Yahoo, 10/22):** 2026 EPS $11.12 (+3.0%), **2027 $11.62 (+4.5%)**, 2027 sales $107.8B. Both were cut in the
  last 90 days.
- **Margins (TTM):** gross 67.8% · operating 25.1% · net 16.2% (after the talc charge).
- **Cash flow:** FCF TTM **$22.2B** (StockAnalysis); 2026 ≈ $21B guided; Q3 > $6B → FCF yield ≈ 3.4% on a $645B market cap.
- **Balance sheet (9/27/2026):** debt $49.0B, cash & securities $20.8B → **net debt ≈ $28.3B**, EV/EBITDA 19.0. Talc cash:
  first payment ≤ $3B in 2027, nothing more before 2028.
- **Dividend:** $1.34 a quarter = $5.36 a year, **2.0% yield** (10/22). Ex-dividend **11/24**, paid 12/8 (declared 10/13).
  Payout ≈ 48% of adjusted 2026 EPS. **Buybacks:** none to speak of (the share count is slightly up; buyback yield −0.8%).
- **Valuation (10/22):** **23.0× 2027 EPS** (24.1× 2026), PEG 2.85, trailing GAAP P/E 40.6 (talc). Peers' forward P/E (Yahoo,
  10/22): LLY 27.7 · **JNJ 23.0** · AMGN 18.3 · ABBV 17.6 · ABT 17.2 · MRK 15.9 · NVS 15.9 · AZN 15.2 · MDT 15.1 · PFE 10.6 ·
  GSK 10.4 · BMY 9.5. Only Lilly is dearer. Against its own history: the yield is 2.08% vs a 5-year average of 2.68% (Yahoo),
  i.e. ≈ 29% richer. Intellectia puts the forward P/E at 22.6 vs a 5-year average of 16.3 (method unverified).
- **Patent cliffs:** Stelara is mostly done. Darzalex is the next big LOE (date unverified). There is no single-drug cliff the
  size of Keytruda's inside 3 years.
- **Policy:** MFN pricing deal with the administration in **January 2026**: Medicaid at MFN prices, some drugs on TrumpRx
  (Xarelto, Invokana), and a time-limited tariff exemption tied to two new US plants.

## News & catalysts
Last 30 days:
- **10/22 — confirming.** First real-world pulsed-field-ablation data at APHRS (Busan): VARIPURE, 225+ patients, 100% acute
  success, 0.4% primary adverse events; Omny-IRE, 82.5% free of AF at 12 months. The stock rose +3.8% while the S&P fell
  −1.2% and the SOX −6.7%. That is the diversifier behaviour the account wants.
- **10/13 — neutral.** The Q3 beat and the guidance raise were outweighed by the MedTech miss and the talc charge: −5.7% to
  $248.61. Same day: dividend $1.34 declared, and an Enterprise Business Review set for **12/8**. The DePuy Synthes ortho
  separation is planned for mid-2027, with a spin now the leading option.
- **10/14–10/21 analyst moves — neutral.** Raises: Wells Fargo $275 → $287 (OW, 10/15–16) and Bernstein $261 → $270
  (Market Perform). Cuts: RBC $290 → $280 (OP), BofA $282 → $275, Leerink $276 → $272 (Buy, 10/15) and Morgan Stanley
  $294 → $292. Reiterations: Scotiabank $305 (10/14) and TD Cowen $300 (10/20). Downgrades: **Erste to Hold on valuation
  (10/21)** and JLPascual to Sell at $110 (10/17).
- **Talc — confirming, pending.** The $5.5B ovarian settlement (announced 7/27) needs **95% of claimants** to sign. J&J says
  sign-ups are trending to meet it; no completion report found as of 10/22. Mesothelioma cases sit outside the deal: the
  $966M LA verdict was cut to $16M compensatory on 3/13/2026 (appeals continue), and a $45M Illinois verdict was upheld on 7/13.
  No new October verdict was found.

Next 90 days:
- **11/3** — US midterm elections; drug-pricing politics.
- **11/24** — ex-dividend.
- **12/8** — Enterprise Business Review: the ortho spin and the 2027 framing.
- **By year-end** — FDA decision on Rybrevant Faspro in head and neck cancer, expected by the company.
- **Date unknown** — whether the 95% talc threshold is met. This is binary.
- **≈ 1/19–1/21/2027** — Q4 plus the first 2027 guide with the deal dilution. Not confirmed.

## Positioning & sentiment
- **Analysts:** consensus Buy. Yahoo (October): 5 Strong Buy / 11 Buy / 6 Hold / 1 Sell. StockAnalysis (23 analysts): average
  target **$279.41 (+4.4%)**, median $280.50, range $190–320. There is not much upside left in the targets.
- **Estimates are falling:** 2027 EPS was $12.83 90 days ago and is $11.62 now, with 2 cuts in the last 30 days.
- **Short interest:** 22.07M shares = **1.0% of float** (9/30), up from 21.67M (8/31). 3.5 days to cover. Not a factor.
- **Insiders:** sales only, after option exercises. CEO Duato sold 48.5k shares at ≈ $258 (8/5) and 123.3k at $261–262
  (8/13), ≈ $44.7M in total. T. Schmid sold 33.6k at $274.74 (9/2). No open-market buys were found.
- **Crowding:** health care *is* the rotation trade right now. XLV is **+7.6% since 9/30 vs the S&P +0.2% and the SOX
  −15.0%**, and the S&P health-care index hit a record on 10/20 (secondary source). JNJ itself is only +1.1% since 9/30
  because of its report, but it is +39% over 52 weeks. If chips bounce, the rotation can unwind and JNJ can lag. That is
  the hedge working, but it means the line can sit flat or red in a chip rally.

## What would make me wrong
- **Up and away:** the rotation keeps going and JNJ breaks $281 without pulling back to $251. Then we miss it. A breakout
  above the record is not a plan setup, because there is no resistance to measure 2:1 against. Re-derive it then; don't chase.
- **The zone fails:** a close under $240 would break the post-earnings double bottom and the 200-DMA together. Likely
  causes: the talc deal missing 95% (with litigation back on the table), a third MedTech miss, or a Medicare-wide MFN push
  after the midterms.
- **Valuation de-rating:** at 23× with ≈ 4–5% EPS growth, a soft 2027 guide in January could cost 10%+ even with no bad
  news. The stop at $240 caps that at ≈ $12 on this size.

## Sources
- Yahoo chart API JNJ, 2y daily bars, and quoteSummary (estimates, targets, short interest 9/30, insiders, dividend dates):
  fetched 2026-10-23 01:12 EEST (10/22 18:12 ET). SOX, S&P 500, XLV and peer bars the same time.
- https://www.investing.com/news/transcripts/earnings-call-transcript-johnson--johnson-tops-q3-2026-eps-forecast-shares-fall-93CH-4946987 — 2026-10-13
- https://www.tikr.com/blog/johnson-and-johnson-stock-falls-medtech-miss-q3-2026 — 2026-10-13
- https://www.jnj.com/latest-news/what-you-need-to-know-about-johnson-johnsons-2026-third-quarter-earnings — 2026-10-13
- https://www.nasdaq.com/press-release/johnson-johnson-announces-quarterly-dividend-fourth-quarter-2026-2026-10-13 — 2026-10-13
- https://www.sec.gov/Archives/edgar/data/0000200406/000020040626000163/jnj-20260729.htm — 8-K 2026-07-29 (Firefly/Sail, dilution)
- https://www.investing.com/news/stock-market-news/why-is-johnson--johnson-stock-rallying-today-93CH-4966908 — 2026-10-22
- https://247wallst.com/investing/2026/10/22/procter-gamble-jumps-6-as-earnings-beat-draws-defensive-buyers-johnson-johnson-rises-3-coca-cola-ticks-up/ — 2026-10-22
- https://stockanalysis.com/stocks/jnj/statistics/ and https://stockanalysis.com/stocks/jnj/forecast/ — 2026-10-21/22
- https://www.investing.com/news/analyst-ratings/bernstein-raises-johnson--johnson-stock-price-target-on-solid-q3-93CH-4951860 — 2026-10-14
- https://www.gurufocus.com/news/9128006/jnj-maintained-by-wells-fargo-price-target-raised-to-287 — 2026-10-16
- https://www.insurancejournal.com/news/national/2026/07/28/879253.htm — 2026-07-28 (talc deal)
- https://www.legalexaminer.com/all/legal/j-js-5-5-billion-talc-settlement-has-a-catch-95-of-plaintiffs-must-say-yes/ — 2026 (95% condition)
- https://www.sokolovelaw.com/product-liability/talcum-powder/settlements/ — September 2026 (verdict list; a law-firm site)
- https://www.fiercepharma.com/pharma/jj-strikes-mfn-deal-trump-reveals-plan-build-2-us-manufacturing-sites — January 2026
- https://www.cnbc.com/2026/03/18/icotyde-psoriasis-pill-from-jj-to-rival-tremfya-skyrizi-il-23-shots.html — 2026-03-18
- https://quartr.com/companies/johnson-johnson_5162 — next-report date (stale page, unconfirmed)
- https://intellectia.ai/stock/JNJ/valuation — forward P/E vs 5-year average (undated, unverified)
- https://www.ebc.com/forex/why-are-healthcare-stocks-hitting-record-highs-in-october-2026 — October 2026 (search summary only; the page returned 403)

**Unverified:** the next report date · the Darzalex LOE date · whether the 95% talc threshold has been met · the 5-year
forward-P/E average · the sector "record high" (secondary source).
