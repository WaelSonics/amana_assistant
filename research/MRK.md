# MRK — Merck & Co. — research log

One file per ticker; newest entry first. Each entry is dated; numbers are as of that date.

Entries:
- 2026-10-28 (deep dive, pre-report; v5-candidate refresh with levels.py checks)
- 2026-10-23 (deep dive, non-AI diversifier screen)

---

## MRK — Merck & Co. — deep dive 2026-10-28

**Verdict:** WATCH. **v5 candidate, not buyable under v3.** **No alert filed: there is no tradeable zone.**
**Conviction:** Low:
- MRK reports tomorrow (10/29, before the open) and is inside the blackout.
- It is down 3.8% since 10/22 on its own news, not on chips, and trades below its 50-DMA.
- Against the real overhead (the $146.61 high left by the reversal), the only zone that passes is $0.75 wide. The ATR after
  the report will probably close it.

| | |
|---|---|
| Price (date) | **$141.59** (levels.py, 2026-10-28 11:07 ET). Closes: 10/22 $147.24; 10/26 $140.61 (−3.2%) |
| Entry zone | **None filed.** Only **$131.45–132.20** passes against T1 $146.61 (check below). It is under $1 wide and would be re-derived after the report anyway. **The 10/23 provisional zone ($132–134, alert $134) is withdrawn:** its top fails against the new T1 |
| Invalidation (stop) | **$125.00** for any re-derived zone: under the 8/4 low $126.22 and the rising 200-DMA ($126.33). Hard exit at −15% ≈ $112. **Event:** the thesis-break exits below |
| Target 1 / 2 | **T1 $146.61**: the 10/26 rejection high. With the 50-DMA ($146.98) and the top of the 8/19 gap ($144.90), it forms the band any rebound has to clear. **T2 $152.80–154.02**: the 9/3 high and the 10/22 reversal high. levels.py lists $152.80 as its first resistance; it cannot see $154.02 yet |
| Reward/risk (T1) | **2.35 / 2.00 : 1** at the low / high of the sliver. The 10/23-style $131.50–133.50 zone **fails at its mid and high (1.88 and 1.54)** |
| Size | One fill of $190 = 5.5% of the sleeve ≈ 1.44 sh. Risk to the stop $9.84 = 0.3% |
| Timeframe | months |
| Next earnings | **2026-10-29, before the open.** levels.py: 1 session away, ✘ inside the 3-session blackout. The call is at 9:00 ET (company release of 10/1, per the 10/23 entry). The report after that is ≈ early February 2027 (not confirmed) |

**What would create a zone** (re-run levels.py on 10/30 with the post-report ATR):
- **(a) A daily close above $147.00**, the 50-DMA and the 10/26 high. The nearest resistance then becomes $152.80–154.02,
  and the $131.50–133.50 zone with a $125 stop passes (check below: 3.28 / 2.71 / 2.27).
- **(b) A post-report base with a new swing low.** It has to allow a stop ≥ 1.5 ATR under an entry that sits ≥ 3 ATR below
  the $146.6 band.

A report that breaks a thesis pillar voids both routes: plan §4 locks entries until the next hard data point.

**levels.py MRK** (2026-10-28 11:07 ET):
```
MRK  $141.59 (2026-10-28 11:07 ET); last daily bar 2026-10-28 close $141.59
  20/50/200-DMA  144.23 / 146.98 (rising) / 126.33 (rising)   price vs 50 -3.7%, vs 200 +12.1%
  RSI(14) 44.3   ATR(14) $4.29 = 3.0% a day   52-wk 82.01–156.92 (-10% from the high)
  Trend: above a rising 200-DMA
  Chase guard: ok
  Next report: 2026-10-29 before the open (1 sessions; EPS est. 2.12)   ✘ inside the 3-session buy blackout
  Swing support below: 138.80, 126.22, 120.16   resistance above: 152.80, 153.57, 156.92
```
**Zone checks** (all with `--stop 125 --size 190 --sleeve 3426`):
```
--zone 131.45-132.20 --target 146.61   (the only passing zone vs the real T1; not filed: < $1 wide)
    at low     131.45: R/R 2.35:1, stop 1.50 ATR (4.9%)   ✓
    at mid     131.82: R/R 2.17:1, stop 1.59 ATR (5.2%)   ✓
    at high    132.20: R/R 2.00:1, stop 1.68 ATR (5.4%)   ✓
    size $190 ≈ 1.4413 sh at the mid; risk to stop $9.84 = 0.3% of $3,426   ✓ ≤ 2%
--zone 131.50-133.50 --target 146.61   (the 10/23-style zone vs the real T1)
    at low     131.50: R/R 2.32:1, stop 1.52 ATR (4.9%)   ✓
    at mid     132.50: R/R 1.88:1, stop 1.75 ATR (5.7%)   ✘ R/R < 2
    at high    133.50: R/R 1.54:1, stop 1.98 ATR (6.4%)   ✘ R/R < 2
--zone 131.50-133.50 --target 152.80   (valid only after a close > $147.00, condition (a))
    at low     131.50: R/R 3.28:1, stop 1.52 ATR (4.9%)   ✓
    at mid     132.50: R/R 2.71:1, stop 1.75 ATR (5.7%)   ✓
    at high    133.50: R/R 2.27:1, stop 1.98 ATR (6.4%)   ✓
```
**Plan status:**
- **v3:** not buyable (≤ 1 non-AI satellite, TTWO), and the client's pause runs to 11/2.
- **v5:** MRK is **not** on the §11 compounder list. That list allows one name per sector, and JNJ holds health care. MRK
  could only enter by replacing JNJ at a quarterly review. It passes the ≤ 35× gate (15.3× 2027 EPS).

### What changed since 10/23
- **Price:** $147.24 → $141.59 (−3.8%). It lost the 20- and 50-DMA and is now 3.7% under the 50-DMA. The 10/22 bearish
  outside reversal followed through: 10/26 fell 3.2% on 13.1M shares (1.3× the 10.0M 20-day average), to a low of $139.93,
  just above the 10/5 swing low ($138.80).
- **The rotation did not cause this.** The SOX rose 2.8% and 3.6% on 10/26–10/27 while XLV was flat. MRK fell on 10/26, the
  day of its ESMO endometrial data and its 2:30 pm ET oncology investor event.
  - I found no article explaining the fall.
  - The data was positive: TroFuse-005 cut the risk of death by 32%, and KEYNOTE-C93 cut progression-or-death by 43%.
  - My reading: "sell the news" on high pipeline expectations, as on 10/22.
- **T1 dropped from $153 to $146.61:** the reversal left a lower high under the old sell zone.
- **Indicators:** ATR $4.36 → $4.29; RSI 52.9 → 44.3.
- **Consensus edged lower again:** 2027 EPS $9.26 → $9.23. The average target rose from $158.44 to $159.76 (StockAnalysis).
- **The 10/24 ESMO presentation and the 10/26 event have passed.** Three binary events were pending on 10/23; only the
  report is left.

### Earnings preview: Q3 2026, 10/29 before the open
1. **Date and time.** 10/29, before the open (levels.py/Alpha Vantage; 247wallst 10/25). The last decision point is today's
   close. We hold none, and both the blackout and the client's pause block buys.
2. **Consensus.**
   - **EPS: $2.09** (247wallst, 10/25: $2.0947, down from $2.2810 90 days earlier; $2.58 a year ago) or **$2.12** (Alpha
     Vantage, via levels.py).
   - **Revenue: $17.35B**, +0.4% y/y (247wallst, 10/25), or $17.33B (Hudson Labs, 10/6).
   - Full-year consensus: EPS $2.66, revenue $67.05B (247wallst). Company guide (8/4): sales $66.3–67.3B, non-GAAP EPS
     $2.66–2.76.
   - The metrics that move the stock:
     - **Keytruda + Qlex.** Q2 was $7.904B for Keytruda plus $463M for Qlex. Zacks puts the Q3 Keytruda consensus at
       $7.45B (search summary; unclear whether that includes Qlex).
     - **Gardasil.** I found no Q3 consensus. Q2 was $1.169B, and the 2026 guide assumes no shipments to China (search
       summary).
     - **Winrevair.** Q2 was $588M, +75%.
     - **Any 2027 framing.**
   - The year-ago quarter had ≈ $250M of wholesaler timing that will not repeat (247wallst).
3. **Implied move: ±4.8% ≈ ±$6.80** (EarningsWatcher, as of 10/27). The average peak earnings-day move is ±5.3% over 2
   years and ±4.3% over 10.
   - A −4.8% gap lands at ≈ $134.8, still above the sliver.
   - Reaching $132.20 takes ≈ 1.4× the implied move.
   - We hold no position, so no money is at stake.
4. **Scenarios:**

   | Scenario | What has to happen | Likely reaction | Action written now |
   |---|---|---|---|
   | Bull | Keytruda + Qlex ≥ $8.4B with Qlex share up, the FY guide raised, a 2027 framing ≥ the $9.23 consensus | a gap toward $146–147 | No buy: blackout, and the pause runs to 11/2. A close above $147.00 → re-derive with T1 $152.80–154.02 (condition a) |
   | Base | in line; guide held | chop at $137–146 | Re-derive on 10/30 with the post-report ATR; expect no zone |
   | Bear | Keytruda below the estimate (after the specialty-pharmacy unwind), weaker Gardasil, or a cut to the guide or the 2027 framing | a gap to $133–136 or lower | The zone is void if a pillar breaks (§4 lock). If the pillars hold, the only route is a stop ≥ 1.5 ATR under a new swing low |

5. **History** (levels.py bars, opening gap and close-to-close):

   | Report | Open | Close |
   |---|---|---|
   | 8/4/26 | +0.5% | +0.2% |
   | 4/30/26 | −1.5% | −1.6% |
   | 2/3/26 | −1.5% | +2.2% |
   | 10/30/25 | −2.3% | −0.3% |

   All four stayed inside the implied move. EarningsWatcher's peak intraday moves were +1.7%, −2.1%, +4.5% and −3.8%.
6. **Decision, written 10/28:** no position, and no buy before or on report day. Re-derive the levels on 10/30 from closed
   bars. Nothing is decided on report night.

### Thesis scorecard (v5 candidate; not on the §11 list)
| Pillar (falsifiable) | What was expected | Status (dated) | Trend |
|---|---|---|---|
| The Keytruda franchise (IV + Qlex) grows y/y until the 2028 LOE | ≥ 0% y/y | Q2 $8.37B, +5% (8/4); Q3 due 10/29 | at risk (estimates falling) |
| Qlex conversion protects the franchise | US share rising; access in the EU | Q2 $463M vs $128M in Q1. The EU SC version is enjoined in 8 countries (Dutch court, 10/7); the German appeal hearing is set for 11/19 (search summary) | mixed |
| Growth outside Keytruda | Winrevair ≥ +50% y/y; Lipfendra launch | Winrevair Q2 $588M, +75% | improving (Q3 due) |
| The late-stage pipeline delivers | positive phase 3 data | INTerpath-001 HR 0.58 (10/22). TroFuse-005: OS −32%, PFS −41%. KEYNOTE-C93: PFS −43% (Merck, 10/26) | improving |
| 2027 EPS consensus holds | ≥ $9.0 | $9.23 (StockAnalysis 10/28) vs $9.26 (10/22) vs $9.66 (≈ late July) | weakening |

**Thesis-break exits (under v5 these replace the price stop):**
1. A US ruling or injunction against Keytruda Qlex in Halozyme's New Jersey patent case.
2. The Keytruda revenue outlook is cut at two reports in a row, or a settlement or ruling allows a US biosimilar before 2028.
3. A dividend cut (now $0.85 a quarter).

**Disconfirming evidence:**
- Analysts cut full-year EPS estimates 10 times in 30 days, with no raises (247wallst 10/25).
- The stock fell on good data twice (10/22, 10/26).
- Net debt is $46.77B (StockAnalysis 10/28).

**Conviction: Low.** It moves to Med on a clean Q3, a close back above $147 and a credible floor under 2027 EPS.

## Thesis
On 10/23 the case was "cheap pharma with a non-Keytruda engine, uncorrelated with chips." The week made the pipeline half
stronger and the stock weaker. Three phase 3 programmes posted positive data, and the stock fell anyway. That means
expectations are already in the price, and that the 2028 Keytruda cliff caps what the market will pay.

At 15.3× 2027 EPS it is not expensive. But the chart is a series of lower highs since August ($156.92 → $154.02 →
$146.61), and estimates keep falling. A buy needs either a report that stops the estimate cuts, or a price low enough to
pay 2:1 under the new lower high. Neither exists today.

## Chart & technicals
Source: levels.py, 2026-10-28 11:07 ET. Daily bars come from levels.py's Yahoo cache.

**Trend:** under the 20-DMA ($144.23) and the 50-DMA ($146.98; it was $144.43 ten sessions ago, still rising). Above a
rising 200-DMA: $126.33 now vs $122.42 twenty sessions ago. Price is −3.7% vs the 50-DMA and +12.1% vs the 200-DMA. The
long trend is intact; the short trend has turned down.

**Momentum and volatility:** RSI(14) 44.3; ATR(14) $4.29 = 3.0% a day. The chase guard passes.

**Range:** the 52-week range is $82.01–156.92, and price is 10% under the high.

**Last week (closes):**

| Date | Close | Change | Range / volume |
|---|---|---|---|
| 10/23 | $145.27 | −1.3% | |
| 10/26 | $140.61 | −3.2% | high $146.61, low $139.93; 13.1M shares |
| 10/27 | $141.82 | +0.9% | |
| 10/28 | $141.59 (11:07 ET) | | low $139.21 |

**Support:**
- $138.80, the 10/5 swing low (and the bottom of the 8/19 gap).
- $133.1–136.0, the 8/13–8/18 pre-gap shelf.
- $126.22 / $126.33: the 8/4 low and the 200-DMA.
- $120.16 (7/14).

**Resistance:**
- $144.9–147.0: the top of the 8/19 gap, the 10/23 high ($145.44), the 10/26 high ($146.61) and the 50-DMA.
- $152.80 / $153.57 / $154.02: 9/3, 9/22 and 10/22.
- $156.92: the record.

**levels.py oddity:** levels.py lists $152.80 as the first resistance. It cannot see $154.02, which is inside the last 5
bars. And it will never list $146.61, because that high sits within 5 bars of the higher $154.02. Its "resistance above"
therefore overstates the room to T1 right after a reversal.

## Fundamentals
**Market data** (StockAnalysis, 10/28 10:58 ET, price $142.17):
- Market cap $350.76B; EV $397.53B.
- Forward P/E 17.09; my calculation is 15.3× the 2027 consensus of $9.23 at $141.59.
- Trailing P/E 111.7, inflated by acquired-IPR&D charges.
- PEG 3.13; EV/EBITDA 13.74.

**Dividend and cash flow:**
- Dividend $3.40 a year = 2.40%.
- FCF (TTM) $16.06B = a 4.59% yield.

**Balance sheet:** debt $53.91B, cash $7.14B → **net debt $46.77B**. Share count −1.92% y/y.

**Margins (TTM):** gross 75.90%, operating 35.28%, net 4.77%.

**Consensus** (StockAnalysis, 10/28):

| | 2026 | 2027 |
|---|---|---|
| EPS | $2.65 (after the Cidara/Terns charges) | $9.23 |
| Revenue | $67.05B (+3.1%) | $69.94B (+4.3%) |

**Keytruda:** US exclusivity ends ≈ 2028. The first US biosimilar BLA was accepted on 10/13 (10/23 entry).

**v5 gate:** passes.

## News & catalysts (last 30d / next 90d)
Items new since 10/23 are marked ★.

**Last 30 days:**
- ★ 10/28 and 10/27 — **Analyst maintains** (StockAnalysis). Targets cluster near the price on the Hold side. *Neutral.*
  - 10/28: Guggenheim $170 Buy, Barclays $180 Buy.
  - 10/27: Cantor $145 Hold, RBC $145 Hold, Scotiabank $180 Buy.
- ★ 10/26 — **ESMO endometrial data** (Merck newsroom). *Confirming for the pipeline. The stock fell 3.2% that day.*
  - TroFuse-005: sac-TMT cut the risk of death by 32% and of progression or death by 41% vs chemotherapy in previously
    treated endometrial cancer.
  - KEYNOTE-C93: Keytruda alone cut the risk of progression or death by 43% vs chemotherapy in dMMR endometrial cancer.
  - The FDA granted priority review to the sac-TMT BLA (search summary; no target date found).
- ★ 10/26 — **Oncology investor event** in Madrid at 2:30 pm ET (BioPharmaWatch). No coverage found. *Neutral, unknown.*
- 10/22 — **INTerpath-001:** data leaked before ESMO (HR 0.58). Merck's 10/22 release confirms the Presidential Symposium
  slot. *Breaking for the stock (10/23 entry).*
- 10/21 — **EU approval** of Keytruda + Padcev around surgery in muscle-invasive bladder cancer (Merck newsroom).
  *Confirming.*
- 10/13 — **The FDA accepted the first Keytruda biosimilar BLA.** *Breaking, long term.*
- 10/7 — **Dutch court** blocks Keytruda SC in 8 European countries (Halozyme release). *Breaking for the Qlex defence.*

**Next 90 days:**
- **10/29** — Q3 results, before the open.
- **11/3** — US midterm elections.
- **11/19** — German appeal hearing on the Keytruda SC injunction (search summary).
- **No date** — Halozyme's US case in New Jersey.
- **≈ early February 2027** — Q4 results and the 2027 guide (not confirmed).

## Positioning & sentiment
- **Analysts** (StockAnalysis, 10/28): consensus Buy. 14 Strong Buy, 5 Buy, 8 Hold, 0 Sell. Average target $159.76
  (+12.4%), median $165, range $105–186.
- **Short interest:** 28.27M shares = 1.15% of float (StockAnalysis; date not shown). Not a factor.
- **Crowding:** low. MRK is not the vehicle of the sector rotation (XLV weight 5.38%, SSGA 10/27). This week's weakness is
  specific to the stock: pipeline hopes were priced, and each readout has been sold.

## What would make me wrong
- **Up:** a clean print and a close above $147 lead back to $152.8–157 without a pullback. The answer is a re-derived
  setup, not a chase.
- **Down:** misses on Keytruda or Gardasil gap it to the shelf or the 200-DMA. A close under $125 means the August gap move
  has fully failed.
- **Structural:**
  - Qlex is blocked in the US.
  - Biosimilars enter early.
  - More debt-funded deals.

## Sources
**Price and technicals**
- levels.py MRK (Yahoo chart API): output and setup checks at 2026-10-28 11:07 ET; chart
  `/tmp/claude-1000/-home-waelas-wael-amana-amana-assistant/cf7235bd-03e5-456e-8948-a8c2229a57bd/scratchpad/charts/MRK.png`.
  Earnings date and the $2.12 estimate from Alpha Vantage (demo key; cached 10/27).

**Earnings preview**
- https://247wallst.com/investing/2026/10/25/beyond-keytruda-the-critical-pipeline-metrics-to-watch-in-mercks-q3-results-on-oct-29/
  — 2026-10-25.
- https://www.hudson-labs.com/research/merck-q3-2026-earnings-preview-mrk-results-and-guidance — 2026-10-06.
- https://earnings-watcher.com/wiki/mrk-implied-move — implied move and history, as of 2026-10-27.
- https://www.nasdaq.com/articles/will-keytruda-continue-aid-mercks-top-line-q3-earnings — Zacks Keytruda estimate (search
  summary; date unclear).

**Company and fundamentals**
- https://stockanalysis.com/stocks/mrk/statistics/ — 2026-10-28 10:58 ET.
- https://stockanalysis.com/stocks/mrk/forecast/ — 2026-10-28.

**News**
- https://www.merck.com/media/news/ — 10/21, 10/22 and 10/26 releases, fetched 2026-10-28.
- https://www.biopharmawatch.com/news/MRK/merck-esmo-2026-oncology-results — ESMO programme and the investor-event time.
- https://www.benzinga.com/news/health-care/26/10/62599012/merck-endometrial-cancer-studies-show-significant-survival-gains
  — 2026-10-26 (403; search summary, including the priority review).
- https://www.placera.se/pressmeddelanden/halozyme-therapeutics-halozyme-wins-injunction-stopping-manufacture-and-sale-of-merck-s-keytruda-sc-in-multiple-european-markets-20261007
  — 2026-10-07 (search summary, including the 11/19 German hearing).

**Sector**
- https://finance.yahoo.com/healthcare/articles/stocktwits-pharma-pulse-big-pharma-022829910.html — 2026-10-26.

**Unverified:**
- the cause of the 10/26 drop;
- the basis of the Zacks Keytruda estimate;
- the 11/19 German hearing;
- the sac-TMT PDUFA date;
- the February report date.

---

## MRK — Merck & Co. — deep dive 2026-10-23 (non-AI diversifier screen)

**Verdict:** WATCH. The levels below are **provisional**. Re-derive them on 10/30, after the 10/29 report, and buy only
from 11/2 · provisional **alert at $134.00** · **Conviction:** Low. Three binary events land before the buy window opens:
full ESMO data (10/24), the oncology investor event (10/26) and Q3 (10/29). Its 60-day correlation with the SOX is about
zero (−0.07), so it does not hedge chips; it is only uncorrelated, with 36% volatility. The Keytruda cliff (≈ 2028) caps
the multiple.

| | |
|---|---|
| Price | **$147.24** (close 2026-10-22, −1.8%). It reversed from **$154.02** after the cancer-vaccine data leaked: low $144.07, 19.0M shares = 2.0× the 20-day average. No 10/23 bar yet: data fetched 10/22 18:12 ET |
| Entry zone | **$132.00–134.00, from 11/2 — alert at $134.00**, then a market order. This fills the 8/19 gap down to the pre-gap shelf of 8/13–8/18 (lows $133.06–134.88, closes $135.17–135.97), just under the 100-DMA (≈ $137 by 11/2) |
| Invalidation (stop) | **$125.00**, under the 8/4 swing low $126.22 and the 200-DMA ($125.68 now, ≈ $127 by 11/2). That is $8.00 under the zone mid = **1.83 × ATR** (1.61× at $132, 2.06× at $134). Hard exit −15% from cost ≈ $113 (the stop comes first). **Event:** the 10/29 report cuts the Keytruda or 2027 outlook, or a US court blocks Keytruda Qlex |
| Target 1 / 2 | **T1 $153** (bottom of the sell zone $153–157: highs 9/3 $152.80, 9/22 $153.57, 10/22 $154.02) / **T2 $157** (record high $156.92, 8/25). Hurdle on the way: $144.9–147 (top of the 8/19 gap, 20/50-DMA) |
| Reward/risk (T1) | **2.5:1 at the zone mid $133** (+$20 / −$8) · 2.1:1 at $134 · 3.0:1 at $132 · 3.0:1 to T2. **At today's $147.24: about 0.6:1** (stop $138 under the 10/5 low → −$9.2 vs +$5.8) → no buy at this price |
| Size | One fill of **$270 = 8.0% of $3,387** → **≈ 2.01 sh** at $134 (2.03 at $133). **Risk to the stop ≈ $16–18** (0.5% of the sleeve; cap $68). Full 10–15%: one later add ≤ 4% (≈ $135), only after a close back above the 50-DMA |
| Timeframe | 1–3 months: T1 before the early-February report |
| Next earnings | **2026-10-29, before the open: confirmed** (company release 10/1; call 9:00 ET). Consensus EPS $2.09, revenue $17.35B (Yahoo). This is before the buy window, so the earnings blackout does not bind, but **every level here must be re-derived on 10/30**. The report after that is ≈ early February 2027 (not confirmed) |

**Rule check at the zone:** the zone is ≈ 9% under the 50-DMA, so the chase guard passes ✓ · the stop is ≥ 1.5 ATR away ✓ ·
R/R ≥ 2:1 across the whole zone ✓. **The ATR will probably rise after the 10/29 report.** If the ATR(14) is above $4.67, a
fill at $132 breaks the 1.5-ATR rule. **The zone is void if the price gets there *because* the report broke the thesis**
(a Keytruda or 2027 guide cut): plan §4 locks entries until the next hard data point. **Plan flag (§1):** satellites are
"≤ 1 non-AI" and TTWO appears to fill that slot. That is the client's call.

## Thesis
- **Why it might fit:** it is independent of the AI trade. The 60-day correlation with the SOX is **−0.07** (120-day
  −0.16) and the 60-day beta to the S&P is 0.38. On the chip-crash days it moved **+3.80% (10/14), +0.52% (10/16) and
  −1.76% (10/22) = +2.6%**, but the 10/22 loss came from its own news while chips fell 6.7%. It is not a hedge the way JNJ
  is (−0.50).
- **The bull case:** at **15.9× 2027 EPS ($9.26)** it is mid-pack among big pharma. FCF is ≈ $15–16B a year (≈ 4.3% yield),
  and a non-Keytruda engine is growing: Winrevair +75%, Welireg +67%, Capvaxive +42%, the oral PCSK9 Lipfendra (approved
  July 2026), sac-TMT (TroFuse-005 positive), and the acquired Cidara (flu) and Terns (CML) assets. If 2027 is ≈ $9.3 of EPS
  and the cliff proves "more of a hill" (the CEO's phrase), $153–157 is reachable.
- **What the market may be missing (my reading):** expectations for the pipeline are now high. The 10/22 leak (HR 0.58 vs
  hopes of 0.50–0.59) sold off despite a clearly positive phase 3. The stock re-rated from ≈ 9× FY2025 EPS ($8.98) at the
  11/4/2025 low ($82.01) to ≈ 16× now, a move of **+80% from the low**. The easy re-rating is done; what is left is execution
  against the 2028 cliff.
- **Against it:** Keytruda is ≈ half of sales and loses US exclusivity around 2028. The first US biosimilar was accepted for
  FDA review on 10/13. The Qlex defence is being fought in European courts. Net debt nearly doubled in a year. 2027 EPS
  estimates are falling.

## Chart & technicals
(Yahoo daily bars to the 10/22 close; Wilder RSI/ATR.)
| | |
|---|---|
| 20 / 50 / 100 / 200-DMA | $145.37 (flat, −0.25% over 10 sessions) / **$146.45** (rising, +2.3%) / $135.55 (rising) / **$125.68** (rising, +1.6%) |
| Price vs averages | **+0.5% over the 50**, +17.2% over the 200. It has crossed the 50-DMA 6 times in 3 weeks: a chop, not a trend |
| RSI(14) · ATR(14) | **52.9** · **$4.36 = 2.96% a day** (60-day volatility 35.7% annualized vs JNJ 24.2%) |
| 52-wk high / low | **$156.92 (2026-08-25)** / $82.01 (2025-11-04) · −6.2% from the high |
| Returns | 5d +1.4% · 20d −0.5% · 60d +12.9% · 120d +31.3% · 250d +68.9% |
| Earnings-day moves | **8/4/2026 +0.2%** · 4/30/2026 −1.6% · 2/3/2026 +2.2% · 10/30/2025 −0.3% (the last three dates are inferred from volume spikes) |

- **Structure:** on 8/19 the stock gapped +12.6% (from $135.17 to an open of $146.94) on the INTerpath-001 topline, and it
  has ranged **$138.8–156.9** since. The highs are flat ($156.92 → $153.57 → $154.02). The lows fell from $145.75 (8/28)
  to $142.32 (9/15) to **$138.80 (10/5)**, then made a higher low at $143.53 (10/19). **10/22 was a bearish outside reversal
  on 2× volume**: it opened at $151.05, ran to $154.02 and closed at $147.24.
- **The gap:** 8/18 high $137.98 → 8/19 low $144.90. The 10/5 low ($138.80) filled all of it except the bottom $0.82.
- **Swing points (6 months):** highs 6/30 $130.29 · 7/28 $135.05 · 8/25 $156.92 · 9/3 $152.80 · 9/22 $153.57 · 10/22
  $154.02. Lows 6/18 $111.57 · 7/14 $120.16 · **8/4 $126.22** · 8/28 $145.75 · 9/15 $142.32 · **10/5 $138.80**.
- **Support:** $145.4–146.5 (20/50-DMA, 10/20 low) · $142.3–143.5 · **$138.0–138.8** (gap bottom, 10/5 low) · ≈ $137
  (100-DMA by 11/2) · **$133.1–136.0 (pre-gap shelf) = buy zone** · $125.7–126.2 (200-DMA, 8/4 low) · stop $125 · then
  $120.2.
- **Resistance:** $149.4–150.0 · **$152.8–154.0** · $156.9 (record).
- **Why no zone closer to today's price:** with an ATR of $4.36, a 2:1 trade with a stop ≥ 1.5 ATR away needs ≥ 3 ATR
  ($13.1) of room to T1 $153, so nothing above ≈ $139.9 qualifies. At the 10/5 low area ($138.8–139.9), the stop would have
  to sit at ≈ $132–133. That leaves a window under $1 wide, which is not tradeable. The first workable zone is the shelf.

## Fundamentals
- **Q2 2026 (reported 8/4; Q3 is due 10/29):** sales **$16.6B, +5%** (+4% ex-FX) vs ≈ $16.4B expected. Keytruda + Qlex
  **$8.4B (+5%)**, of which Qlex was $463M (Q1: $128M). Winrevair $588M (+75%) · Gardasil $1.17B (+4%; −9% YTD) ·
  Januvia/Janumet $429M (−31%) · Animal Health $1.8B (+8%) · Ohtuvayre (Verona) +$204M. GAAP loss $0.54/sh; non-GAAP loss
  $0.13/sh vs −$0.27 expected, after a **$2.31/sh Terns charge**. Management flagged that the unwind of Q2
  specialty-pharmacy buying will hit Q3 sales (Trefis).
- **2026 guidance (8/4):** sales **$66.3–67.3B** (raised from $65.8–67.0B). Non-GAAP EPS **$2.66–2.76** (from $5.04–5.16),
  after one-time charges of $3.62/sh (Cidara, $9.2B, closed in January) and $2.31/sh (Terns, $6.7B, closed in Q2) plus
  ≈ $0.12. Excluding those, EPS is ≈ $8.7–8.8 (my addition).
- **Consensus (Yahoo, 10/22):** Q3 EPS $2.09 (it was $2.28 90 days ago) on $17.35B of revenue; 2026 $2.66; **2027 $9.26**
  ($9.66 90 days ago, with 10 cuts in 30 days); 2027 revenue $69.9B (+4.3%). Merck beat EPS in each of the last 4 quarters.
- **Keytruda and the cliff:** 2025 sales were **$31.7B** including Qlex, ≈ half of revenue. US exclusivity ends **≈ 2028**
  (one source says the main US compound patent expires December 2028, with related patents into 2029 and EU exclusivity to
  2031; the exact dates are unverified). **10/13: the FDA accepted the first publicly announced Keytruda biosimilar BLA**
  (Formycon/Zydus FYB206), with a decision ≈ Q3 2027. Analysts (Evaluate consensus) see IV Keytruda falling from ≈ $32.7B
  (2026) to ≈ $7.2B (2032). Qlex is the defence: the CFO targets 30–40% US adoption by the end of 2027 (secondary source).
- **Margins (TTM):** gross 75.9% · operating 35.3% before acquired-R&D charges (StockAnalysis), ≈ 0% GAAP in the latest
  quarter · net 4.8%.
- **Cash flow:** FCF TTM to 6/30 **$15.2B** (Yahoo) / $16.1B (Trefis), against $8.3B of dividends paid.
- **Balance sheet (6/30/2026):** debt **$53.9B (up from $35.4B a year earlier)**, cash $7.1B → **net debt ≈ $46.8B**.
  Interest cover 4.0× (Trefis); EV/EBITDA 14.4. Three deals in 12 months (Verona, Cidara, Terns) were bought with debt.
- **Dividend:** $0.85 a quarter = $3.40 a year, **2.3% yield** (10/22); last paid 10/7. Payout ≈ 39% of underlying EPS.
  **Buybacks:** buyback yield 1.9% (StockAnalysis).
- **Valuation (10/22):** **15.9× 2027 EPS**; trailing GAAP P/E 117 (meaningless after the charges); PEG 2.8. Peers' forward
  P/E (Yahoo, 10/22): LLY 27.7 · JNJ 23.0 · AMGN 18.3 · ABBV 17.6 · **MRK 15.9** · NVS 15.9 · AZN 15.2 · PFE 10.6 · GSK 10.4 ·
  BMY 9.5. Against its own history: the yield is 2.27% vs a 5-year average of 2.88% (Yahoo), ≈ 27% richer, and the stock is
  ≈ 9× → 16× since the November 2025 low.
- **Policy:** MFN deal on **12/19/2025** (one of nine companies): Medicaid at MFN prices, Januvia/Janumet on TrumpRx, and a
  3-year tariff exemption tied to US manufacturing investment.

## News & catalysts
Last 30 days:
- **10/22 — breaking (for the stock, not the drug).** INTerpath-001 data (the mRNA vaccine intismeran + Keytruda in
  melanoma) **leaked before ESMO**: recurrence-free survival HR **0.58** (−42%), 2-year RFS 82.2% vs ≈ 70%, distant
  metastasis −38%, overall survival not yet mature. Investors had hoped for 0.50–0.59 (RBC), and the phase 2 HR was 0.51.
  BMO: "not enough … amidst elevated expectations". RBC expects approval in 2027 but questions the commercial case. MRK
  reversed from $154.02 to $147.24; Moderna fell −21%.
- **10/21 — confirming.** EU approval of Keytruda + Padcev around surgery in muscle-invasive bladder cancer.
- **10/13 — breaking (long term).** FDA accepted Formycon/Zydus's Keytruda biosimilar BLA. The LOE clock is now visible.
- **10/7 — breaking (for the defence).** A Dutch court found Halozyme's EP622 patent valid and infringed by Keytruda SC,
  with a ban in 8 European countries. A German injunction has been in place since 12/4/2025. Halozyme's US suit (15 patents,
  New Jersey) is pending, though the PTAB has voided some Halozyme US claims. Merck calls the patent invalid and is appealing.
- **10/12–10/17 analyst moves — neutral.** BMO $170 Buy (10/12) · Wells Fargo $165 Buy (10/15) · **Goldman $160 → $155**
  Buy (10/16) · Citi $145 Hold (10/16) · **RBC $150 → $145** Hold (10/17) · JPMorgan raised to $165 OW (≈ 10/5). Targets
  are clustering near the price.
- **10/22 — unverified.** FDA traditional approval of Keytruda for TMB-high tumours (single source, GuruFocus).

Next 90 days:
- **10/24** — full INTerpath-001 data at ESMO (Saturday). The market reacts Monday 10/26.
- **10/26** — oncology investor event in Madrid.
- **10/29 (before the open)** — Q3. Watch the Keytruda/Qlex mix, Gardasil and the specialty-pharmacy unwind, and any 2027
  framing.
- **11/3** — US midterm elections; drug-pricing politics.
- **Ongoing** — Halozyme appeals in Europe, the US case, and Qlex adoption.
- **≈ early February 2027** — Q4 plus the 2027 guide. Not confirmed.

## Positioning & sentiment
- **Analysts:** consensus Buy. StockAnalysis (27 analysts): 14 Strong Buy / 5 Buy / 8 Hold / 0 Sell; average target
  **$158.44 (+7.6%)**, median $163, range $105–186. Yahoo: $158.56 average from 25 analysts. Recent target moves are
  mostly cuts or holds, not raises.
- **Estimates are falling:** 2027 EPS is down from $9.66 to $9.26 in 90 days (10 cuts in 30 days), and Q3 EPS from $2.28 to
  $2.09.
- **Short interest:** 28.27M shares = **1.15% of float** (9/30), down from 30.29M (8/31). 2.9 days to cover. Not a factor.
- **Insiders:** sales only, in August at $128.7–135: General Counsel Zachary 80.3k shares at $133.46 (8/12), CTO Williams
  52.9k at $128.77 (8/5), and others. No open-market buys were found.
- **Crowding:** the sector is crowded (XLV +7.6% since 9/30 vs the S&P +0.2%), but **MRK has not been the vehicle**: it is
  only +1.3% since 9/30, against LLY +12.9%, ABBV +9.0% and PFE +6.7%. Its crowding is the pipeline-hope kind (+80% from the
  low on the August gap), and the 10/22 reversal shows that hope is fully priced.

## What would make me wrong
- **Up and away:** a clean ESMO/Q3 sequence takes it through $157 and it never comes back to $134. We miss a move, but
  that is a better outcome than buying the 10/22-style reversal at $150. A breakout above the record is not a plan setup
  (there is no resistance to measure against); re-derive it then.
- **Down through the zone:** a Q3 Keytruda miss, a weak 2027 framing, or a US ruling against Qlex could take it through the
  shelf to the 200-DMA. A close under $125 means the August gap move has fully failed.
- **Structural:** a Keytruda patent settlement that lets biosimilars in before 2028, or more debt-funded deals, would take
  away the "cheap at 16×" argument.

## Sources
- Yahoo chart API MRK, 2y daily bars, and quoteSummary (estimates, targets, short interest 9/30, insiders, calendar): fetched
  2026-10-23 01:12 EEST (10/22 18:12 ET). SOX, S&P 500, XLV and peer bars the same time.
- https://www.biopharmawatch.com/news/MRK/merck-third-quarter-2026-conference-call — 2026-10-01 (Q3 date/time)
- https://www.sec.gov/Archives/edgar/data/310158/000110465926090045/tm2621496d1_ex99-1.htm — Q2 release, 2026-08-04
- https://www.biospace.com/drug-development/esmo-2026-merck-moderna-shares-fall-as-cancer-vaccine-disappoints-after-data-leak — 2026-10-22
- https://www.biopharmadive.com/news/moderna-merck-esmo-intismeran-melanoma-vaccine-results/833765/ — 2026-10-22
- https://www.fxleaders.com/news/2026/10/20/merck-stock-forecast-mrk-50-day-ema-esmo-q3-earnings/ — 2026-10-20
- https://stockanalysis.com/stocks/mrk/statistics/ and https://stockanalysis.com/stocks/mrk/forecast/ — 2026-10-17/22
- https://finance.yahoo.com/healthcare/articles/heres-expect-merck-co-next-140409871.html — 2026-10-13 (Q3 preview)
- https://trefis.com/stock/mrk/articles/619419/what-happens-to-merck-stock-if-keytruda-sales-stop-growing/2026-10-20 — 2026-10-20
- https://www.fiercepharma.com/pharma/halozyme-stymies-subq-keytruda-launch-select-european-countries-merck-vows-fight-patent — 2026-10-07
- https://www.targetedonc.com/view/fda-accepts-bla-pembrolizumab-biosimilar-fyb206 — 2026-10-15
- https://ad-hoc-news.de/boerse/news/corporate-news/goldman-sachs-cut-target-for-merck-und-co-stock-to-usd-155-00/70382362 — 2026-10-16
- https://www.ad-hoc-news.de/boerse/news/corporate-news/merck-wins-eu-cancer-approval-merck-und-co-stock-gains-1-37-percent/70393036 — 2026-10-21
- https://finance.yahoo.com/sectors/healthcare/articles/merck-buy-oncology-firm-terns-112132385.html — 2026-03-25 (Terns)
- https://www.fiercepharma.com/pharma/top-drugmakers-reach-us-drug-price-deal-trump-administration — 2025-12-19 (MFN)
- https://bju.proactrx.com/resource/news/fda-approved-keytruda-qlex-to-offset-original-drugs-patent-expiration-in-2028/500/ — LOE timing (weak source)
- https://www.gurufocus.com/news/9137597/fda-grants-traditional-approval-to-mercks-keytruda-for-tmbh-tumors-boosting-mrks-growth-prospects — 2026-10-22 (single source)

**Unverified:** the exact Keytruda US LOE date · the Qlex adoption target · the TMB-H approval · the 2026 earnings dates
other than 8/4 · the February report date.
