# WDC — Western Digital — research log

One file per ticker; newest entry first. Each entry is dated; numbers are as of that date.

Entries:
- 2026-10-28 (deep dive; not held; below the 200-DMA)

---

## WDC — Western Digital — deep dive 2026-10-28

**Verdict:** WATCH, with **no fresh longs**: WDC is below its 200-DMA (`levels.py`), and even after a reclaim no zone passes.
**Last of four** for the single memory slot. · **Conviction:** Low on the setup, Med on the business. The 10/22 beat-and-raise is
real, but the stock has fallen after each of its last four reports. The market is selling the input-cost and capex story, not
buying the earnings.

| | |
|---|---|
| Price | **$385.91** (2026-10-28 10:52 ET, `levels.py`). +1.3% on the 10/27 close of $380.88; +7.0% on the 10/13 stop fill of $360.62; −52% from the 6/18 high of $799.87 |
| Entry zone | **None.** Below the rising 200-DMA (417.27), so no fresh longs per `levels.py`, and no candidate zone passes R/R (checks below) |
| Invalidation (stop) | For any future buy: under the 10/16 low of $331.81 or the post-reclaim swing low. Event: a FQ2 gross margin < 60% or a guide cut; HDD $/TB falling q/q |
| Target 1 / 2 | $398.28 (10/9 high), then $417–425 (200- and 50-DMA) / $475.66–495.49 (9/23, 8/27, 9/9 swing highs). Fundamental: mean target $613.38 (S&P via stockanalysis, 10/27) |
| Reward/risk (T1) | ✘ 0.86–1.52:1 across the candidate zones |
| Size | $0 |
| Timeframe | months |
| Next earnings | ≈ **2027-02-03** (Investing.com 10/23, "tentative"; not in the `levels.py` 3-month calendar). Dividend record 12/4, paid 12/17 |

### What changed (no earlier research file; desk history)
- **Account history:** re-bought 10/2 and added 10/9 (an OVERRIDE: adds were locked). **Stopped 10/13 at $360.62, −$50.85**
  (PLAN §6b, journal 10/10 and 10/13). The client has since called the WDC/STX/SNDK buys greed.
- **Since the stop:** a low of $331.81 on 10/16, then the 10/22 report beat and raised. The stock still fell **−6.4%** on report day,
  before the release, in the AI-capex scare, and **−3.0%** on 10/23 to $343.67. It made a **higher low at $339.55** (10/23) and has
  rallied 13.6%. §4a evidence is met: that higher low, plus closes back above the broken $360 level (10/27 $380.88). The 200-DMA
  rule still blocks.
- **The 50-DMA (424.64, falling) is about to cross under the 200-DMA (417.27, rising).** A death cross is days away.

### Thesis scorecard (section B)
| Pillar (falsifiable) | Expected | Status (dated) | Trend |
|---|---|---|---|
| HDD pricing power | blended $/TB up y/y | **+28% y/y** in FQ1 (Investing.com 10/23). Evercore: investors will "struggle" with its durability | stable, questioned |
| Revenue growth | FQ2 guide ≥ +50% y/y | FQ2 guide **$5.1B ± $0.1B** (+66–72% y/y, +16% q/q) (press release 10/22) | improving |
| Margin expansion | gross margin ≥ 58% | FQ1 non-GAAP **58.1%**, FQ2 guide **60–61%** (press release 10/22) | improving |
| Cost and capex discipline | capex 4–6% of revenue; cost/TB −10% y/y | Capex "modestly higher" than 4–6% for two years (Investing.com 10/23). Input costs rising. On cost/TB, Investing.com 10/23 has it "on track" for ≈ −10% y/y, while FinanceFeeds 10/24 has near-term cuts below the ≈ 10% target (**the two conflict**) | **weakening** |
| The market pays for beats | positive reaction | It fell after the last 4 reports, close to close: **−10.1%** (1/29), −0.7% (4/30), **−13.0%** (8/5), −3.0% (10/22) (Yahoo bars) | **weakening** |

- **Thesis-break exits:** a FQ2 gross margin < 60% or a guide cut (≈ 2/3); HDD $/TB down q/q; a hyperscaler long-term deal renewed
  at lower prices.
- **Disconfirming evidence logged:** price-target cuts after the beat (TD Cowen $540 → 430, Citi $740 → 660, Morgan Stanley
  $676 → 643). STX also beat-and-raised on 10/27 and fell ≈ 5–7% after hours.
- **Conviction: Med** on the business. It rises if the FQ2 margin lands ≥ 61% with $/TB still rising. It falls on any capex raise.

## Thesis
Since the Sandisk separation, WDC is a pure hard-drive company: 88% of sales go to cloud (Investing.com 10/23). Exabyte demand
from AI data storage is giving it pricing power it has never had: $/TB +28% y/y, gross margin 43.9% → 58.1% in a year. At
$385.91 it trades at 15.6× FY27 consensus EPS ($24.72) and 9.6× FY28 ($40.40). That is dearer than MU or SNDK on earnings, because
HDD is seen as less cyclical. The problem is the tape. Four straight beats were sold, input costs and capex are rising, and the
price is under a 200-DMA that the 50-DMA is about to cross. The protocol answer is: wait for the reclaim.

## Chart & technicals
`levels.py WDC`, quote 2026-10-28 10:52 ET:
```
WDC  $385.91 (2026-10-28 10:52 ET); last daily bar 2026-10-28 close $385.91
  20/50/200-DMA  383.13 / 424.64 (falling) / 417.27 (rising)   price vs 50 -9.1%, vs 200 -7.5%
  RSI(14) 48.0   ATR(14) $24.46 = 6.3% a day   52-wk 121.85–799.87 (-52% from the high)
  Trend: BELOW a rising 200-DMA  → protocol: no fresh longs until it reclaims it
  Chase guard: ok
  Next report: not in the 3-month calendar (ETF, or more than 3 months away)
  Swing support below: 331.81   resistance above: 475.66, 479.85, 495.49
```
- **Structure:** lower highs since June: 799.87 → 602.54 → 580 → 548.60 → 495.49 → 475.66. It broke the 200-DMA in October. Low
  $331.81 (10/16), higher low $339.55 (10/23), a bounce to $389.27 (today's high) just over the 20-DMA.
- **Missing from the script's resistance list:** the $398.28 high (10/9) and the 200- and 50-DMAs at $417–425. All three sit
  between the price and the script's "nearest" $475.66.
- **Volume:** 14.0M on the post-report sell day (10/23), against a ≈ 9.7M 10-day average (FinanceFeeds 10/24). 2.4M by 10:52 ET today.
- **Chart:** `/tmp/claude-1000/-home-waelas-wael-amana-amana-assistant/cf7235bd-03e5-456e-8948-a8c2229a57bd/scratchpad/charts/WDC.png`.
  It shows the price under the converging 50- and 200-DMA.

**Zone checks** (`levels.py WDC --zone … --size 250 --sleeve 3426`, 10/28 10:52 ET data):
```
# pullback to the post-report closes 355-362 / 320 / 398.28
    at low     355.00: R/R 1.24:1, stop 1.43 ATR (9.9%)   ✘ R/R < 2; stop < 1.5 ATR
    at mid     358.50: R/R 1.03:1, stop 1.57 ATR (10.7%)   ✘ R/R < 2
    at high    362.00: R/R 0.86:1, stop 1.72 ATR (11.6%)   ✘ R/R < 2
    size $250 ≈ 0.6974 sh at the mid; risk to stop $26.85 = 0.8% of $3,426   ✓ ≤ 2%
# after a 200-DMA reclaim, retest 418-425 / 380 / 475.66
    at low     418.00: R/R 1.52:1, stop 1.55 ATR (9.1%)   ✘ R/R < 2
    at mid     421.50: R/R 1.31:1, stop 1.70 ATR (9.8%)   ✘ R/R < 2
    at high    425.00: R/R 1.13:1, stop 1.84 ATR (10.6%)   ✘ R/R < 2
    size $250 ≈ 0.5931 sh at the mid; risk to stop $24.61 = 0.7% of $3,426   ✓ ≤ 2%
```
**No passing zone.** At a $24.46 ATR, 2:1 needs **$73 of open air**. The pockets on this chart are $339.55 → $398.28 ($59) and
$417 → $475.66 ($58).

**The condition that would create a zone:** first, a daily close above the 200-DMA (≈ $417). Then ATR(14) has to fall to
**≤ ≈ $18.5** (≈ 4.5%). At that point a retest of ≈ $418–420 with a stop ≈ $391 pays 2:1 to $475.66. Both must hold, and on or
after 11/2.

## Fundamentals
- **FQ1 FY27** (press release, 2026-10-22; quarter ended 10/2):
  - Revenue **$4.38B**, +55% y/y and +17% q/q.
  - Non-GAAP gross margin **58.1%** (GAAP 57.8%); non-GAAP operating margin 49.1%.
  - Non-GAAP EPS **$4.64**, against a $4.08 consensus (Investing.com 10/23).
  - Operating cash flow $1.60B, FCF **$1.38B**. Exabytes shipped 248 EB, +22% y/y (Investing.com 10/23).
  - Dividend +17% to $0.175.
- **FQ2 guide:** revenue **$5.1B ± $0.1B**, gross margin **60–61%**, EPS **$5.80 ± $0.20**, opex $400–410M, ≈ 380M diluted shares.
- **Valuation** (stockanalysis, 10/28 10:58 ET, price $387.49): market cap **$145.05B**, forward P/E **13.40**, trailing 15.04,
  EV/sales 9.82. Consensus EPS FY27 **$24.72**, FY28 $40.40 (stockanalysis 10/27).
- **Balance sheet** (stockanalysis): cash $1.31B, debt $0.92B, net cash $0.39B. Shares 374.32M: +5.84% y/y, −1.29% q/q.
- **Quality of earnings:** TTM profit margin 69.2% against a 40.9% operating margin (stockanalysis). Net income is inflated by
  non-operating items, presumably the Sandisk-stake sale gains (not verified). Use operating figures.

## News & catalysts (last 30d / next 90d)
- 10/22: **FQ1 beat and FQ2 guide above consensus**, dividend +17% ([WD press release](https://westerndigital.com/company/newsroom/press-releases/2026/2026-10-22-wd-reports-fiscal-first-quarter-2027-financial-results)).
  **Confirming** for the business.
- 10/23: the stock fell −3.0% to $343.67 after the call. Capex runs "modestly higher" than the 4–6% target for two years, input
  costs are rising, and Evercore doubts the durability of the price gains (Investing.com 10/23; FinanceFeeds 10/24). **Breaking**
  for the trade, **neutral** for the thesis.
- 10/20–10/27: price targets reset lower while ratings stay Buy:
  - Morgan Stanley $676 → $643 (10/20): an "overly punitive cycle-end" is priced in.
  - TD Cowen $540 → $430 and Wedbush $650 (10/23).
  - Citi $740 → $660 and Bernstein $600 (10/26).
  - Evercore $575 (10/27).
  - Sources: stockanalysis; Investing.com. **Neutral to negative.**
- 10/27: Seagate FQ1, revenue $4.2B (+61%), EPS $7.68; guide $4.8B / $9.20. It fell ≈ 5–7% after hours (24/7 Wall St; Chartmill).
  **Confirming** the pattern that HDD beats are not being paid.
- 10/21: Chief Legal Officer sold 807 sh at $380 under a 10b5-1 plan (SEC Form 4). **Neutral.**
- Next: nothing company-specific before ≈ 2/3/2027. Read-across from SNDK on 10/29: NAND pricing is a WDC input cost.

## Positioning & sentiment
- **Short interest** 19.45M shares at the 10/15 settlement, up from 17.28M on 9/15. 1.9 days to cover (Nasdaq), 5.23% of float
  (stockanalysis). The highest short interest of the four memory names.
- **Analysts:** 26, Buy (17 Strong Buy, 4 Buy, 5 Hold). Mean **$613.38**, median $622.50, range $405–900 (S&P via stockanalysis,
  10/27). Targets are being cut while ratings hold. That is late-cycle behaviour.
- **Insiders:** sellers only. July–September sales by the CEO and directors at ≈ $440–470. A July analysis counted 125 open-market
  sales in 6 months and no purchases (Kavout, via search; not verified).

## What would make me wrong
- WDC reclaims the 200-DMA within days on HDD pricing, and the post-report sellers are exhausted (higher low $339.55 holds). Then
  the desk is late, but a reclaim plus a contracting ATR is exactly the condition above.
- The FQ2 margin prints ≥ 61% in February with $/TB still rising, and the "cycle-end" discount (MS 10/20) unwinds.

## Sources
- `levels.py WDC` (Yahoo chart API), 10/28 10:52 ET data, with the zone checks above. Earnings reactions are from the same Yahoo bars.
- [WD Reports Fiscal First Quarter 2027 Financial Results](https://westerndigital.com/company/newsroom/press-releases/2026/2026-10-22-wd-reports-fiscal-first-quarter-2027-financial-results) — 2026-10-22
- [Investing.com: WDC earnings analysis and next catalysts](https://www.investing.com/news/stock-market-news/western-digital-earnings-analysis-questions-answered-and-next-catalysts-93CH-4970089) — 2026-10-23 12:02
- [Investing.com: WDC shares drop as cost pressures, higher capex overshadow earnings](https://www.investing.com/news/stock-market-news/western-digital-surges-on-earnings-beat-upbeat-guidance-as-ai-stocks-slump-4967303) — 2026-10-22/23
- [FinanceFeeds: WDC falls 3% after the $4.64 beat](https://financefeeds.com/western-digital-stock-falls-3-after-the-4-64-beat-what-shares-are-saying-before-sandisk-reports-on-29-october/) — 2026-10-24
- [stockanalysis WDC statistics](https://stockanalysis.com/stocks/wdc/statistics/) · [forecast](https://stockanalysis.com/stocks/wdc/forecast/) — fetched 2026-10-28
- [Chartmill: Seagate strong margins, after-hours slide](https://www.chartmill.com/news/STX/Chartmill-56965-Seagate-Technology-Holdings-NASDAQSTX-Posts-Strong-Margins-and-Above-Consensus-Guidance-Despite-After-Hours-Slide) · [24/7 Wall St: Seagate Q1 2027](https://247wallst.com/cards/seagate-technology-q1-2027-earnings-stx-01m5zg90mk29dvmt5zgqe2kcj1) — 2026-10-27
- [SEC Form 4, C. Tregillis 10/21 sale](https://www.sec.gov/Archives/edgar/data/0000106040/000126682426000217/edgardoc.xml) — signed 2026-10-22, fetched 2026-10-28
- Nasdaq API: WDC short interest (10/15) and earnings-surprise history. Nasdaq lists FQ1 EPS as $4.43 against $3.99, while the
  company's non-GAAP figure is $4.64 against Investing.com's $4.08 consensus. Fetched 2026-10-28.
