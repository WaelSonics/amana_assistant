# ARM — Arm Holdings plc (ADR) — research log

One file per ticker; newest entry first. Each entry is dated; numbers are as of that date.

Entries:
- 2026-10-28 (deep dive + 11/4 earnings preview + thesis scorecard; not held)
- 2026-10-21 (stopped out 10/20)
- 2026-10-19 (update)
- 2026-10-13

---

## ARM — Arm Holdings plc (ADR) — deep dive 2026-10-28

**Verdict:** WATCH · not held · **no passing zone** · earliest buy **11/5**, and only after the 11/4 report *and* the Qualcomm
royalty ruling · **Conviction:** Low on the setup. The business is intact, but at a 6.1% daily ATR every real level is
closer than the 3 ATR a 2:1 trade needs. The binary ruling is still open.

| | |
|---|---|
| Price (date) | **$233.35** (levels.py, 2026-10-28 11:07 ET); close $226.60 (10/27); 10/22–10/23 lows **$208.30 / $208.50** |
| Entry zone | **None passes** (checks below) |
| Invalidation (stop) | n/a (not held). For any future setup, structure says under the $208.30 double low (≈ $205) · event: a royalty-suspension ruling |
| Target 1 / 2 | Nearest real resistance **$233.29 → $236.59–239.50** · then $245.87 / $250.20 / the falling 50-DMA $259.98 / $267.69 |
| Reward/risk (T1) | **0.17–0.63:1** for the old $225–233 zone with a $205 stop to $237.68 (levels.py) ✘ |
| Size | 0 now. Plan placeholder ≈ $190 from 11/5 (PLAN §6b) |
| Timeframe | Weeks to quarters |
| Next earnings | **Wed 11/4 after the close**, call 17:00 ET (Arm newsroom, 10/5). levels.py: 5 sessions; the buy blackout starts 10/30 |

**What changed since 10/21** ($226.94 then):
- **10/22:** −7.3% to $210.10 in the Lam/SOX sell-off. The low of $208.30 was 5.7% under the 10/20 stop fill ($220.85).
  10/23 made a matching low at $208.50.
- **Bounce:** +12% from that low (10/26 +6.2% close to close, Yahoo bars; TradingKey: "oversold", brokers reiterating), to $233.35 now.
  At the low, the stop had saved ≈ $20; at this price it has cost ≈ $20 (1.5668 sh × $12.50).
- **The 50-DMA turned down** (it was rising on 10/19; now $259.98, falling).
- **Implied move ±12.3%**, up from ≈ ±8.8% on 10/13.
- **Short interest rose** to 17.7M (10/15) from 16.2M.
- **Still no ruling.** Futurum (10/27): expected "before the end of the calendar year".
- **New soft negative.** AMD's 10/27 release says AMD EPYC processors "support the computing environments" behind Meta's
  Muse agent. The 9/21 +17% ARM spike was built on the *assumption* that Muse runs on Arm's AGI CPU.
- **§4a evidence is forming:** a higher low (10/26 $210.82 > $208.30) and today's high of $233.55 above $233. If today
  closes above $233, the "close > $233" leg is met. **It still does not open a buy:** the report and ruling gates come first,
  and no zone passes the R/R test.

### Thesis scorecard (earnings-and-thesis.md §B; not held — kept for the re-entry decision)
| Pillar (falsifiable) | What was expected | Status (dated) | Trend |
|---|---|---|---|
| Royalty revenue growth ≥ low-teens % y/y | Q2 FY27 guide: low teens | Q1 FY27 total revenue $1.29B, +22% (Yahoo, 10/25). The royalty guide for Q2 is down to low teens; smartphone royalty growth seen at high teens for FY27, from 20%+ (Hudson Labs, 10/7) | **weakening** |
| Data-center royalties > 2× y/y | > 2× | Q1: "more than doubled" (Yahoo, 10/25) | stable |
| AGI CPU demand converts into revenue | > $2B demand, $1B capacity secured | No update since 7/29. A fuller revenue and margin update was promised for later (Yahoo, 10/25). The AMD/Meta Muse release is a soft negative (above) | stable to weakening |
| The Qualcomm remedy does not suspend royalties | No suspension | 10/13 jury: breach and $2 in damages. The remedy is pending, expected by year-end (Futurum, 10/27). Qualcomm ≈ $443M of last FY's revenue (≈ 9%) (Yahoo, 10/25). Futurum's estimate of a suspension: ≈ $300M a year, ≈ $1.5B in total | **open (binary)** |
| Valuation supported by growth | — | ≈ 105× FY27 normalized EPS ($2.23; Yahoo, 10/25; desk arithmetic at $233.35) | — |

- **Thesis-break exits** (each keeps ARM off the re-entry list, whatever the price):
  1. The royalty suspension is granted.
  2. The royalty growth guide is cut again on 11/4.
  3. A major licensee publicly moves designs to RISC-V.
- **Disconfirming evidence:**
  - The CFO's automatic sales at $300 (9/21) and $255.33 (8/27).
  - The Muse/EPYC read-across.
  - Short interest rising into the report.
- **Conviction: Low.** It goes to Med on a ruling that voids the clause *and* a royalty guide at or above low teens.

### Earnings preview — Q2 FY27, Wed 11/4 after the close (§A)
1. **Date and time.** 11/4 after the close, call 14:00 PT / 17:00 ET (Arm newsroom, 10/5). Last decision point: none needed,
   since ARM is not held.
2. **Consensus:**
   - Revenue **$1,376M** (Hudson Labs, 10/7) vs guide **$1.38B ± $50M** (+22% y/y).
   - Non-GAAP EPS guide **$0.47 ± $0.04**. The GAAP consensus is $0.23 (Hudson Labs); levels.py/Zacks shows **$0.22**, a GAAP
     basis, so don't compare it to the non-GAAP print.
   - **Metrics that move it:** royalty growth (guided low teens), licensing (guided ≈ +30%), data-center royalties, the AGI
     CPU capacity line, and any Qualcomm remedy comment.
3. **Implied move: ±12.3%.** The Nov 6 at-the-money straddle (232.50 strike) was $14.22 + $14.43 = **$28.65** on $232.34
   (Nasdaq, 10/28 10:59 ET); the Oct 30 straddle alone is ±5.3%. That is ≈ $204–261.
   - **$ at stake: $0** (not held). For the plan's ≈ $190 re-entry it would be ±$23 on one night. That is why the re-entry
     waits until 11/5.
4. **Scenarios** (written 10/28):

   | Scenario | What has to happen | Likely reaction | Action written now |
   |---|---|---|---|
   | Bull | Revenue ≥ $1.43B, royalty growth above low teens, AGI CPU capacity raised; ideally a ruling that voids the clause | +10% to +15% (July analog: +14.7% gap) → $255–270, into the falling 50-DMA | **No chase.** Re-derive 11/5 from the new bars; a gap into the 50-DMA is resistance, not an entry |
   | Base | In line, royalty low teens, no AGI CPU numbers | ±5–10% (May −10.1%, February +5.7%) | Re-derive 11/5. A buy needs the ruling out, §4a evidence, and a zone that passes levels.py |
   | Bear | Royalty guide cut again, AGI CPU supply-limited, or a suspension ruling | −10% to −25% | A close under **$208.30** breaks the base: off the list until a new one forms. A suspension ruling is a thesis break: off the list |
5. **History** (Yahoo daily bars via levels.py; report-day close → next session):

   | Report (after the close) | Next open (gap) | Next close |
   |---|---|---|
   | 2025-11-05 (Q2 FY26) | +4.3% | **−1.2%** |
   | 2026-02-04 (Q3 FY26) | −0.4% | **+5.7%** |
   | 2026-05-06 (Q4 FY26) | −6.3% | **−10.1%** |
   | 2026-07-29 (Q1 FY27) | +14.7% | **+7.4%** |

   Same series as the 10/13 entry. The 5/6 date is inferred from it and was not re-fetched this session.
6. **Decision:** none on 11/3 or 11/4 (not held). The re-entry plan is unchanged: **from 11/5**, after the report *and* the
   ruling, with a zone that passes all three points.

### Thesis
Arm takes a royalty on nearly every smartphone chip and a fast-growing share of data-center CPUs. Data-center royalties more
than doubled in Q1. It now also sells its own AGI CPU, with demand above $2B and $1B of capacity secured.

The market is paying ≈ 105× FY27 earnings for that. It is not paying for a Qualcomm royalty holiday (≈ 9% of revenue) or a
second guide-down in royalty growth. Both are live into 11/4. The float is ≈ 13% of the shares (SoftBank owns ≈ 86%; 10/13
entry), so moves get amplified.

### Chart & technicals (levels.py, 2026-10-28 11:07 ET)
```
ARM  $233.35 (2026-10-28 11:07 ET); last daily bar 2026-10-28 close $233.35
  20/50/200-DMA  252.09 / 259.98 (falling) / 227.80 (rising)   price vs 50 -10.2%, vs 200 +2.4%
  RSI(14) 43.1   ATR(14) $14.20 = 6.1% a day   52-wk 100.02–452.70 (-48% from the high)
  Trend: above a rising 200-DMA
  Chase guard: ok
  Next report: 2026-11-04 after the close (5 sessions; EPS est. 0.22)   ✓ outside the buy blackout
  Swing support below: 233.29, 225.46, 219.39   resistance above: 237.68, 239.50, 267.69
```
- **Structure.** Lower highs from $336.98 (9/23): $318.36 (10/2), $260.15 (10/13), $245.87 (10/15), $239.42 (10/16), $236.59
  (10/19), $228.95 (10/21).
  - Then a double low at $208.30 / $208.50 (10/22–10/23), under the 200-DMA, and a reclaim. Today's high of $233.55 is the
    first higher high since September.
  - The bounce volume (4.7M, 3.7M) is below the 5.7M of the 10/22 drop. That is fading, not conviction.
- **levels.py's support list misses the actual low.** At 10:52 ET it listed $225.46 / $219.39 / $200.89 and skipped the 10/22
  low of $208.30: a pivot needs 5 bars after it, and there are only 4.
- **Real resistance, from the bars:** $233.29 (8/24 low, broken support) · $236.59–239.50 (10/19 and 10/16 highs; 4/24 and
  5/6 pivots) · $245.87 · $250.20 · $252.09 (20-DMA) · $255–260 (10/12–10/13 highs and the falling 50-DMA) · $267.69.
- **Zone checks** (`levels.py ARM --zone … --size 190 --sleeve 3426`, 11:06–11:07 ET, ATR $14.20):
```
  Setup: zone 225.00–233.00, stop 205.00, T1 237.68     # the old re-entry zone; stop under the double low
    at low     225.00: R/R 0.63:1, stop 1.41 ATR (8.9%)   ✘ R/R < 2; stop < 1.5 ATR
    at mid     229.00: R/R 0.36:1, stop 1.69 ATR (10.5%)   ✘ R/R < 2
    at high    233.00: R/R 0.17:1, stop 1.97 ATR (12.0%)   ✘ R/R < 2
  Setup: zone 222.00–225.00, stop 205.00, T1 267.69     # generous T1: skips 237.7–260 (only legitimate after a reclaim)
    at low     222.00: R/R 2.69:1, stop 1.20 ATR (7.7%)   ✘ stop < 1.5 ATR
    at mid     223.50: R/R 2.39:1, stop 1.30 ATR (8.3%)   ✘ stop < 1.5 ATR
    at high    225.00: R/R 2.13:1, stop 1.41 ATR (8.9%)   ✘ stop < 1.5 ATR
  Setup: zone 222.00–225.00, stop 200.00, T1 267.69     # wider stop under the 5/12 low
    at low     222.00: R/R 2.08:1, stop 1.55 ATR (9.9%)   ✓
    at mid     223.50: R/R 1.88:1, stop 1.66 ATR (10.5%)   ✘ R/R < 2
    at high    225.00: R/R 1.71:1, stop 1.76 ATR (11.1%)   ✘ R/R < 2
  Setup: zone 222.00–225.00, stop 200.00, T1 245.87     # honest T1 after a reclaim of 239.50
    at low     222.00: R/R 1.09:1, stop 1.55 ATR (9.9%)   ✘ R/R < 2
    at mid     223.50: R/R 0.95:1, stop 1.66 ATR (10.5%)   ✘ R/R < 2
    at high    225.00: R/R 0.83:1, stop 1.76 ATR (11.1%)   ✘ R/R < 2
```
- **No passing zone, even with a T1 the chart does not justify.**
  - **Why:** a 2:1 trade with a 1.5-ATR stop needs ≥ 3 ATR = **$42.60** of clear air to T1. Between $208 and $260, ARM's
    real levels are $4–12 apart.
  - **Condition that would create a zone** (from 11/5, after the report and the ruling):
    - ATR(14) contracts to **≤ ≈ $7** (≈ 3% a day), and
    - a higher low holds above $208.30.
    - Then a ≈ $213–216 zone with a ≈ $205 stop pays 2:1 to $237.68.
  - A breakout alone does not fix it: above the 50-DMA the next levels ($267.69 / $274.80 / $279.20) are also < 3 ATR apart.
  - Expect no ARM buy in the first half of November. The plan's "≈ $190 from 11/5" is a placeholder, not a trade.
- Chart: `/tmp/claude-1000/-home-waelas-wael-amana-amana-assistant/cf7235bd-03e5-456e-8948-a8c2229a57bd/scratchpad/charts/ARM.png`
  (stop 205, T1 267.69 drawn for reference). Visual check: lower highs under falling 20/50-DMAs, sitting on a rising
  200-DMA. Cosmetic: the stop label overlaps the candles.

### Fundamentals
- **Q1 FY27** (reported 7/29): revenue **$1.29B, +22%**; non-GAAP EPS **$0.45, +29%**, above the top of the guide;
  data-center royalties more than doubled (Yahoo, 10/25).
  - The royalty / licensing split ($715M / $574M) and TTM FCF $1.51B are from the 10/13 entry (Arm newsroom, 7/29), not
    re-fetched.
- **FY27:** revenue estimate $6.06B (+23.2% on FY26's $4.92B); normalized EPS $2.23 (Yahoo, 10/25). Zacks via Nasdaq: FY (Mar
  2027) EPS $1.15, GAAP basis.
- **Valuation:** ≈ 105× FY27 normalized EPS and ≈ 68× FY28 at $210 (Yahoo, 10/25), higher now. Beta is high, and the float
  is small.
- **Balance sheet:** net cash and no dilution concern (10/13 entry; not re-fetched). The SoftBank margin loan (9/18) is the
  overhang, not Arm's own balance sheet.

### News & catalysts (last 30d / next 90d)
- 10/13 — Delaware jury: Arm breached the Architecture License Agreement and interfered with Qualcomm's Meta relationship; $2
  in damages; Arm won the TLA claims — **breaking-risk** (it unlocks the remedy)
- 10/20 — Bench-trial closing arguments; ARM stopped at $220.85 — **neutral**
- 10/22 — −7.3% to $210.10 in the Lam supply-warning sell-off (SOX −6.7%); "nothing in Lam's warning was about Arm"
  (Yahoo, 10/25) — **neutral** (sector)
- 10/26 — +6.2% close to close (Yahoo bars; TradingKey: oversold, brokers reiterate) — **neutral**
- 10/27 — Futurum: no ruling yet; remedy "expected before the end of the calendar year"; the loser is expected to appeal —
  **open binary**
- 10/27 — AMD/Meta release: AMD EPYC behind Meta's Muse — **soft disconfirming** for the AGI CPU story
- **Next:** MSFT and GOOGL 10/28 · AMZN 10/29 · AMD 11/3 (read-across) · **ARM 11/4 after the close** · **royalty ruling: any
  day to ≈ year-end** · AGI CPU update promised with a later report

### Positioning & sentiment
- **Short interest:** 17.70M (10/15) vs 16.19M (9/30); **3.75 days to cover** (Nasdaq). Rising into the binary.
- **Analysts:** 17 Buy / 5 Hold / 0 Sell; mean target **$299.47** (range $150–480) (Nasdaq, 10/28). Unchanged since 10/13.
- **Insiders:**
  - CFO Jason Child: automatic sales of 10,400 sh at $300.00 (9/21) and $255.33 (8/27).
  - No open-market buys: Nasdaq's 12-month "buys" include a 64-share non-open-market acquisition (Haas, 8/31).
- **SoftBank:** owns ≈ 86% and has a margin loan (10/13 entry). No SoftBank-specific news found 10/23–10/27.
- **Crowded and extended?** Not extended (RSI 43, −10% under the 50-DMA). It is crowded by beta, binary-exposed and
  small-float: the protocol §4 crash setup is present around 11/4.

### What would make me wrong
- **The ruling voids the clause and 11/4 reaccelerates royalties.** ARM could gap through the 50-DMA and never offer a 2:1
  zone. That is acceptable: missing a trade costs $0.
- **Price:** a daily close under $208.30 means the base failed.
- **Events:** the suspension is granted (a thesis break); the royalty guide is cut again; RISC-V defections.

### Sources
- `levels.py ARM` (Yahoo daily bars; Alpha Vantage calendar), runs 2026-10-28 10:52–11:07 ET; chart PNG above
- Nasdaq option chain, ARM Nov 6 and Oct 30 expiries, 10/28 10:59 ET — https://api.nasdaq.com/api/quote/ARM/option-chain
- Nasdaq earnings-forecast / targetprice / short-interest / insider-trades APIs for ARM, fetched 10/28 — https://api.nasdaq.com/api/analyst/ARM/targetprice
- [Arm announces earnings release date for Q2 FYE27](https://newsroom.arm.com/news/arm-announces-earnings-release-date-for-second-quarter-fiscal-year-ending-2027) — 2026-10-05
- [Hudson Labs: ARM Q2 FY27 preview](https://www.hudson-labs.com/research/arm-q2-2027-earnings-preview-arm-revenue-and-outlook) — 2026-10-07
- [Yahoo Finance: Arm stock is down 8% last week. What does Lam Research have to do with it?](https://finance.yahoo.com/markets/stocks/articles/arm-stock-down-8-last-154101616.html) — 2026-10-25
- [Futurum: Qualcomm wins liability verdict, royalty suspension ruling to follow](https://futurumgroup.com/insights/qualcomm-wins-liability-verdict-against-arm-with-royalty-suspension-ruling-to-follow/) — 2026-10-27
- [TradingKey: ARM up 5.69% on Oct 26](https://www.tradingkey.com/news/market-movers/262239732-market-movers-arm-20261026) — 2026-10-26
- [TradingKey: ARM down 6.69% on Oct 22](https://www.tradingkey.com/news/market-movers/262232913-market-movers-arm-20261022) — 2026-10-22
- [AMD and Meta release (Muse / EPYC)](https://www.stocktitan.net/news/AMD/amd-and-meta-advance-strategic-partnership-to-power-meta-s-w7j6r9jk2soy.html) — 2026-10-27

---

## ARM — stopped out 2026-10-20 (not held)

**Verdict:** WATCH · no re-entry before the **11/4** report *and* the royalty ruling · **Conviction:** Low on the setup.

| | |
|---|---|
| Exit | Broker stop $220 → **sold 1.56684554 sh @ $220.85 at 09:36 ET on 10/20**, −$54.87 + $1 fee (statement 10/20) |
| The day | Open $224.66, low **$217.26** (09:50 ET), close **$221.06**; the hearing started at 10:00 ET |
| Since | **$226.94** (10/21, 15:44 ET), +$9.54 against the fill |
| Line result | The 10/12 re-buy (OVERRIDE, §4a) ends **−$56.87** with both fees. ARM since 8/18: +$13.46 realized |
| Ruling | Closing arguments heard 10/20. Bloomberg (10/20): the judge is reluctant to step into the next-generation licensing talks. **No ruling on the 5-year royalty-suspension clause yet** |

**Was the stop wrong?** It was flagged on 10/19: $220 sat only 0.6 ATR ($16.85) under the price, so a normal opening dip
could take it. That happened. But the stop itself was right by the plan (under the 200-DMA and the 8/3 swing low, set
before the re-buy's loss grew). The cause was the entry: the 10/12 re-buy at $255.87 had no higher low under §4a, and by
10/19 the price had fallen to within one day's range of the stop. The client held and did not lower the stop (10/19). That
part was right. A stop that is never moved down costs a small known amount. Lowering stops (QUBT, EWY) cost $56 in October.

**Re-entry (§4a), from 11/5 at the earliest:** the ruling must be out, and not a royalty suspension. Then a higher low, or a
close back above **$233** (the 8/24 low and the broken zone top), a new stop written first, and R/R ≥ 2:1. 50-DMA ≈ $265
(the sell zone $275–281 sits above it), 200-DMA ≈ $224.

**Sources:** Amana statement 2026-10-01 → 10-20 (`portfolio/statements/amana-statement-2026-10-01_2026-10-20.pdf`) ·
Yahoo chart API ARM 5-min bars 10/20 and daily bars, fetched 2026-10-21 15:44 ET ·
[Bloomberg, 10/20: Judge reluctant to intervene in Qualcomm-Arm licensing talks](https://www.bloomberg.com/news/articles/2026-10-20/judge-reluctant-to-intervene-in-qualcomm-arm-licensing-talks) ·
[Notebookcheck: Arm's v10 royalty demand, trial figures](https://www.notebookcheck.net/Arm-s-v10-royalty-demand-equals-up-to-30-of-a-220-Snapdragon-chip-s-price-trial-figures-suggest.1429935.0.html)

---

## ARM — update 2026-10-19 (royalty ruling: closing arguments 10/20)

**Verdict:** HOLD with the $220 stop · no adds · **sell at market if Judge Noreika lets Qualcomm suspend royalties** ·
**Conviction:** Low. The binary is now dated: the bench-trial closing arguments are **Tue 10/20, 10:00 ET** (court
minute entry, 90 minutes split). The ruling can come any day after that; there is no deadline.

| | |
|---|---|
| Price | **$230.25** (2026-10-19, 10:35 ET, +1.1%); close $227.80 (10/16, −6.9%); 10/15–10/16 lows **$226.54 / $226.65** |
| 20 / 50 / 200-DMA | $282.1 / $266.8 (rising) / **$224.0** — price −13.7% under the 50, +2.8% over the 200 |
| RSI(14) · ATR(14) | 35.6 · **$16.85 = 7.3% a day** · −49% from the 6/18 high of $452.70 |
| Position | 1.5668 sh @ $255.87 = ≈ $361, 10.5% of the sleeve, **−10.0%** |
| Stop | **$220** (broker, confirmed live 10/19): only **4.4% / 0.6 ATR** below, just under the 200-DMA. Risk ≈ $16. Never lowered |
| Sell zone (⅓) | $275–281 → 0.52 sh (above cost) |
| Buy zone | $225–233 — **locked** until after the 11/4 report *and* the ruling. `portfolio_report.py` flags "IN BUY ZONE"; ignore it |
| Next events | **10/20 closing arguments** · ruling date unknown · earnings **Wed 11/4** after the close (implied ≈ ±8.8%) |

### The ruling (dated)
- **10/13 jury:** Arm breached its Architecture License Agreement and interfered with Qualcomm's Meta relationship;
  **$2** in damages ($1 per claim). Arm won the Technology License Agreement claims.
- **With the judge:** (1) whether the clause letting Qualcomm **suspend royalties for 5 years** after a material breach
  is enforceable — Qualcomm says it applies automatically, Arm says it is unenforceable; Arm itself puts it at
  "billions"; (2) whether Arm negotiated next-generation pricing in good faith. Noreika declined to decide (1) before trial.
- Rule (unchanged since 10/13): **a ruling that grants the suspension = thesis break → sell the whole line at market.**
  A ruling that voids the clause is a relief catalyst, but the adds stay locked until after 11/4.

### Gap risk, stated plainly
On a suspension ruling ARM would likely **gap through $220**. A −20 to −25% gap from $230 costs ≈ **$70–90** on this line,
about the account's whole **$56 cushion** over the $3,402 breaker (10:28 ET). The stop does not protect against a gap.
The plan does not require a sale before the ruling, and the desk does not recommend one: selling now locks ≈ −$40 and
pays the same for a coin flip in the other direction. It is the client's call. A sale is always allowed without the
desk; a re-buy is not.

**Sources:** Yahoo chart API ARM 1y daily, fetched 2026-10-19 10:35 ET · [Insurance Journal, 10/15: jury verdict and the open bench issues](https://www.insurancejournal.com/news/east/2026/10/15/889003.htm) · [Tech Times, 10/14: $2 verdict unlocks the royalty-suspension fight](https://www.techtimes.com/articles/329023/20261014/qualcomm-jury-finds-arm-breach-2-verdict-unlocks-billion-dollar-royalty-suspension-fight.htm) · [Forbes/Tirias, 10/15: who came out on top](https://www.forbes.com/sites/tiriasresearch/2026/10/15/qualcomm-vs-arm-the-jury-verdict-is-in-who-came-out-on-top/) · [24/7 Wall St, 10/16](https://247wallst.com/investing/2026/10/16/arm-and-amd-fall-5-as-qualcomm-verdict-adds-to-chip-selloff-taiwan-semiconductor-slips) · closing-argument date and time from the court minute entry as quoted in search results 10/19 (docket not fetched directly).

---

## ARM — Arm Holdings plc (ADR) — deep dive 2026-10-13

**Verdict:** HOLD with the 220 stop · no adds · **exit at market if the Qualcomm case goes against Arm on royalties** ·
**Conviction:** Low–Med — the business is intact (royalty + licensing +22%, AGI CPU demand > $2B), but the re-buy broke
§4a, the chart is still making lower lows, and a jury verdict that can cut royalties is due today.

| | |
|---|---|
| Price | **$251.74** (2026-10-13, 10:29 ET); close $255.24 (10/12); today's open/low 245.32/243.60 |
| Position | 1.5668 sh @ $255.87 = ≈ $393, **11.2%** of the sleeve (re-bought 10/12 in one $400 fill > the 8% one-fill max) |
| 50-DMA / 200-DMA | **$270.4** (rising) / **$221.5** — price is under the 20 and 50, above the 200 |
| 52-wk high / low | $452.70 (2026-06-18) / $100.02 (2026-02-05) · −25.3% from the 9/23 high of 336.98 |
| RSI(14) · ATR(14) | 39.6 · **$16.89 = 6.7%** a day |
| Stop | **$220** (broker): under the 200-DMA $221.5, just above the 8/3 swing low $219.39 — 1.9 ATR. Risk ≈ $48 = 1.4% |
| Sell zone | **$275–281** (10/8 close 275.3, 9/28 low 279.2, 50% retracement 278.2) → ⅓ = 0.52 sh. Above the avg 255.87 ✓ |
| Buy zone | $225–233 (9/3 low 225.46, 8/24 low 233.29), R/R 3.2:1+ to 275 — **locked**: October buying closed, and after the 11/4 report only |
| Reward/risk at today's price | 0.6:1 to the 50-DMA $270 · 0.9:1 to $280 ✘ — the desk would not buy here |
| Next events | **Qualcomm jury verdict (deliberations resume 10/13)** · earnings **Wed 11/4** after close (implied ≈ ±8.8%) |

### Thesis
Arm collects a royalty on almost every phone chip and a fast-growing share of data-center CPUs, and now sells its own
"AGI CPU" (Meta lead partner; OpenAI, ByteDance, Oracle, Cloudflare, Cerebras named). Q1 FY27 (Jun-26) revenue was
$1.289B, +22%: royalty $715M (+22%) and licensing $574M (+23%). Non-GAAP operating margin was 41%, and TTM FCF $1.51B.
Q2 guide: $1.38B ±$50M, EPS $0.47 ±$0.04. AGI CPU demand is > $2B across FY27–28, but only $1B of capacity is secured.
**Price:** 107× forward earnings and ≈ 51× sales (StockAnalysis 10/13), against a peer forward P/E of ≈ 67×. The price
already assumes the AGI CPU works and royalties keep compounding. Any doubt costs a lot, and beta is ≈ 3.8.

### Why it fell 25% in three weeks (dated)
- **9/21 +17% spike** on Meta's "Muse" agent, which was *assumed* (not confirmed) to run on Arm's AGI CPU. Fully retraced
  since: the 275.8–293.1 gap is filled.
- **9/18** SoftBank upsized its Arm-backed margin loan to $25B. 72% of all Arm shares are pledged. It is a loan, not a sale.
  Loan-to-value is ≈ 13% at today's price, so a forced sale would need a much deeper fall.
- **9/28** chip sell-off on oil and inflation (−8.7%). **10/8** −6.5% on an FT report that OpenAI's annualized revenue was
  ≈ $50B, not ≈ $70B. **10/12** −4.1% in the memory/CXMT sell-off.
- **10/5–10/9 Qualcomm v. Arm jury trial** (Delaware). Qualcomm alleges Arm withheld tools and broke a pricing clause, and
  asks for a ruling that lets it **stop paying royalties for 5 years**. The judge has not ruled on that clause; Arm says it
  is unenforceable. The jury had no verdict after ≈ 4 hours and resumes today. A bench ruling on good-faith negotiation
  comes later. **This is the one item that can break the thesis.**
- ARM is −24% since 9/23 against SMH −3% and NVDA 0%. Most of the fall is specific to Arm and SoftBank.

### Chart & technicals (Yahoo daily bars, computed by the desk and the agent; 10/13 10:30 ET)
- Lower highs (339 → 337 → 318) and, since 10/2, lower lows every session to 243.6 today. That is ≈ the 78.6%
  retracement (244.6) of the 219.4 → 337.0 swing. A bounce from here is possible. A higher low has **not** formed yet.
- Supports: 243.6 · 238.0 · 233.3 · 225.5 · **221.5 / 219.4 (200-DMA + Aug low)** · 200.9–193.9.
- Resistances: 252.8–256 · 263.2 · **266.3–270.4 (50-DMA)** · 275.3–281.5 · 290.2 · 318.4 · 337–339.

### Positioning & sentiment
- Short interest 16.2M = ≈ 11.4% of the 142.6M float, 2.3 days to cover (9/30). Insiders: 34 sales and no buys in 12
  months (the CFO sold at $300 on 9/21).
- Analysts: 17 Buy / 5 Hold / 0 Sell; average PT ≈ $299 (Nasdaq, 10/13; range $150–480). No downgrades or target cuts
  since 8/1.
- Earnings reactions: −1.2% / +5.7% / −10.1% / +7.4% (last 4). Options imply ≈ ±8.8% for 11/4.
- The float is only ≈ 13% of the shares (SoftBank owns 86.4%), and 2× single-stock ETFs exist. Moves get amplified.

### Calls
1. **Hold with the broker stop at 220. Never lower it.** Risk ≈ $48 = 1.4% of the sleeve, inside the 2% budget.
2. **Qualcomm rule:** a verdict for Qualcomm that comes with a royalty holiday (or the judge signalling it is
   enforceable) is a **thesis break → sell at market, whatever the price**. A verdict for Arm or a narrow damages award
   → hold, and expect a relief bounce toward $263–270.
3. **Sell zone $275–281:** price alert at 275; when it fires, sell 0.52 sh (⅓).
4. **No adds.** The buy zone of $225–233 opens only after the 11/4 report.
5. The 10/12 re-buy is logged as an OVERRIDE: §4a needs a close back above $280 or a higher low first. Neither happened,
   and price made two lower lows after the fill.

### What would make me wrong
- A daily close under $220 (the 200-DMA and the August low give way).
- A Qualcomm royalty holiday, or licensees publicly moving designs to RISC-V because of the AGI CPU or fee rises.
- An 11/4 guide that cuts royalty growth further (the CFO already moved the FY outlook toward the high teens).
- SoftBank stress forcing share sales.

### Sources
- Yahoo chart API ARM 1y daily + 1d 5-min bars, fetched 2026-10-13 10:26–10:30 ET
- https://stockanalysis.com/stocks/arm/statistics/ — 2026-10-13
- https://newsroom.arm.com/news/arm-q1-fye27-results — 2026-07-29
- https://whtc.com/2026/10/09/qualcomm-and-arm-set-for-jury-verdict-in-contract-breach-feud/ — 2026-10-09 (Reuters)
- https://finance.yahoo.com/markets/stocks/articles/qualcomm-arm-trial-ends-hung-130049760.html — 2026-10-12
- https://theedgemalaysia.com/node/818515 — 2026-09-18 (SoftBank margin loan)
- https://www.tikr.com/blog/arm-holdings-stock-fell-6-in-a-day-as-an-openai-revenue-report-hit-chip-stocks-heres-where-openai-touches-arms-business — 2026-10-09
- https://247wallst.com/investing/2026/09/28/arm-sinks-9-as-chip-selloff-deepens-qualcomm-drops-6-marvell-slides-5/ — 2026-09-28
- https://www.tradingkey.com/news/market-movers/262211846-market-movers-arm-20261012 — 2026-10-12
- https://api.nasdaq.com/api/quote/ARM/short-interest · /analyst/ARM/targetprice · /company/ARM/insider-trades · /quote/ARM/option-chain — 2026-10-13
- https://www.sec.gov/Archives/edgar/data/0001973239/000197323926000097/arm-20260331.htm — 20-F (SoftBank stake, pledge)
- https://www.ad-hoc-news.de/boerse/news/corporate-news/arm-holdings-stock-falls-2-14-percent-as-arm-sets-results-date/70235028 — 2026-10-05
