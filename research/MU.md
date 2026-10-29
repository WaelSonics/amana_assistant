# MU — Micron Technology — research log

One file per ticker; newest entry first. Each entry is dated; numbers are as of that date.

Entries:
- 2026-10-28 (deep dive, not held; no zone passes)
- 2026-10-22 (stopped out)
- 2026-10-19 (update)
- 2026-10-16 (position opened 10/15)
- 2026-10-14

---

## MU — Micron Technology — deep dive 2026-10-28

**Verdict:** WATCH. No buy zone passes the plan today, so the $859–863 re-entry alert is **retired**. · **Conviction:** Med on
the business, Low on the setup. MU is first in line for the single memory slot. But this chart has no 2:1 entry at a $46 ATR,
and the desk does not invent one.

| | |
|---|---|
| Price | **$969.18** (2026-10-28 10:52 ET, `levels.py`). +4.4% on the 10/27 close of $928.76; +13.2% on the 10/22 close of $856.49 |
| Entry zone | **None passes.** The script passes $860–863 with stop 790 and T1 1,011.77. **Rejected:** that T1 skips the falling 50-DMA (980.28) and today's high (979.80), which sit under it. To ≈ 980 the same window pays 1.60–1.71:1 ✘ |
| Invalidation (stop) | For any future buy: **$790**, under the 7/17 swing low of 804.00. Event on ≈ 12/16: FQ1 revenue under the $61.5B guide, a FQ2 guide down q/q, or a gross margin under 85%. Also a flat or negative 1Q27 DRAM contract forecast |
| Target 1 / 2 | **≈ $980** (50-DMA plus the 10/28 high) / $1,011.77–1,042.40 (7/23, 8/17, 9/9 swing highs). Fundamental: mean target $1,562 (S&P via stockanalysis, 10/26) |
| Reward/risk (T1) | ✘ 1.60–1.71:1 at $860–863 to 980. **No price above the 10/22 low ($849.25) pays 2:1 to 980 at today's ATR** (see the check below) |
| Size | **$0 now.** When a zone passes: ≤ $270 (7.9% of $3,426); risk ≈ $22 to a 790 stop (0.7%). With the account $24 above the breaker, that one stop-out uses almost all of the cushion |
| Timeframe | months |
| Next earnings | **2026-12-16**: `levels.py` (Alpha Vantage, time n/a), 35 sessions; stockanalysis has it as "estimated, after close". The last buy day before the blackout is 12/10 |

### What changed since the 10/22 entry (stopped out at $849.35)
- **§4a evidence is half there.** MU has closed above the broken $850 level every session since 10/23 (877.55, 903.70, 928.76),
  so "a close back above the broken level" is met. There has been no pullback yet, so there is no higher low.
- **The first memory print is in, and it confirmed.** SK hynix Q3 (10/28 KST) beat FnGuide's operating-profit consensus by 9.7%.
  It said DRAM/HBM is "effectively sold out through 2029". Samsung's detailed Q3 and SNDK report 10/29.
- **The old zone is stale.** ATR(14) is now $46.44, so $859 is only 1.49 ATR above the 790 stop and fails. T1 at 1,010 is
  also no longer the nearest resistance for a pullback buyer: the 50-DMA (980.28, falling) and today's 979.80 high sit under it.
- The 10/13 gap ($953.6–978.5) filled today (high $979.80). Today opened a new gap: 10/27 high $935.87 to 10/28 low $959.34.

### Thesis scorecard (section B)
| Pillar (falsifiable) | Expected | Status (dated) | Trend |
|---|---|---|---|
| DRAM contract prices still rise q/q | ≥ +10% in 4Q26 | TrendForce 9/30: conventional DRAM +10–15%, "pace … expected to moderate". Commercial Times via TrendForce 10/20: ≈ +20% after +80% (2Q) and +40% (3Q) | rising, **rate slowing** |
| Gross margin holds near peak | ≥ 85% | FQ4 87.0% (8-K 9/30). FQ1 guide ≈ 86.25%, the first decline of the cycle | slightly weakening |
| Peers confirm demand, no guide-down | peer beats | SK hynix Q3 OP ₩83.33T, +632% y/y, beat by 9.7% (10/28). Samsung prelim OP ₩107.4T, beat by 1.3% (10/8) | improving |
| Long-term contracts cover demand | LTAs > half of 2027–28 | SK hynix: LTAs with 14 customers cover > 50% of 2027–28 capacity. The "sold out" claim includes demand still under discussion (24/7 Wall St, 10/28) | stable |
| Supply discipline | no capex race | SK hynix: 2027 capex up "significantly" vs 2026 (10/28). MU's own FY27 capex > $50B is from the 10/14 entry, not re-verified today | **weakening** (disconfirming) |

- **Thesis-break exits:** (1) the FQ1 report (≈ 12/16) guides FQ2 revenue down q/q, or the gross margin under 85%; (2) TrendForce
  or a Korean maker guides 1Q27 DRAM contract prices flat or down; (3) a top-4 hyperscaler cuts 2027 capex.
- **Disconfirming evidence logged:** rising 2027 capex across the group; PC and mobile unit declines (SK hynix CFO, 10/28); LTA
  price ceilings starting to cap gains (TrendForce 10/20); MU still −23% from its 6/25 high while EPS keeps rising, the
  peak-cycle pattern of the 10/14 entry.
- **Conviction: Med.** It rises if the 1Q27 contract forecast re-accelerates. It falls on any 2027 capex raise by Micron itself.

## Thesis
Micron is the US DRAM/HBM leader and the cheapest large-cap on the AI build-out: 5.5× FY27 consensus EPS ($176.58) at $969.18.
SK hynix's 10/28 print (₩104.6T revenue, 79.7% operating margin, sold out through 2029) confirms the pricing Micron reported on
9/30. What the market keeps pricing is not this year's earnings but the 2028 down-cycle: rate-of-change slowing and capex
rising. The business case is intact. The trade needs a level, and there isn't one today.

## Chart & technicals
`levels.py MU`, Yahoo daily bars, quote 2026-10-28 10:52 ET:
```
MU  $969.18 (2026-10-28 10:52 ET); last daily bar 2026-10-28 close $969.18
  20/50/200-DMA  967.57 / 980.28 (falling) / 741.02 (rising)   price vs 50 -1.1%, vs 200 +30.8%
  RSI(14) 51.5   ATR(14) $46.44 = 4.8% a day   52-wk 192.59–1,255.00 (-23% from the high)
  Trend: above a rising 200-DMA
  Chase guard: ok
  Next report: 2026-12-16 time n/a (35 sessions; EPS est. 37.93)   ✓ outside the buy blackout
  Swing support below: 902.60, 891.66, 887.61   resistance above: 1,011.77, 1,036.13, 1,042.40
```
- **Structure.** Range-bound since July between $737.88 (7/29 low) and $1,108.72 (9/25 high). October made a lower low at
  **$849.25** (10/22) and is bouncing into the falling 50-DMA. The 20-DMA has rolled over to price. This is a test of
  resistance, not a breakout.
- **Not in the script's lists:** the 10/22 low of $849.25, which is the §4a reference (it needs 5 bars on each side to count as a
  swing), and the 50-DMA/10-28 high at ≈ 980 as resistance.
- **Volume:** 10.5M by 10:52 ET on 10/28, against 22.9M for all of 10/27 (Yahoo bars). That pace is normal, not a capitulation or
  a breakout day.
- **Chart:** `/tmp/claude-1000/-home-waelas-wael-amana-amana-assistant/cf7235bd-03e5-456e-8948-a8c2229a57bd/scratchpad/charts/MU.png`
  (drawn with the rejected 860–863 / 790 / 1,011.77 window). It shows the 50-DMA sitting between that zone and its T1.

**Zone checks** (`levels.py MU --zone … --stop … --target … --size 270 --sleeve 3426`, 10/28 10:52 ET data):
```
# old desk zone 859-863 / 790 / 1,010
    at low     859.00: R/R 2.19:1, stop 1.49 ATR (8.0%)   ✘ stop < 1.5 ATR
    at mid     861.00: R/R 2.10:1, stop 1.53 ATR (8.2%)   ✓
    at high    863.00: R/R 2.01:1, stop 1.57 ATR (8.5%)   ✓
# script-passing window 860-863 / 790 / 1,011.77 (passes; rejected: T1 skips the 50-DMA)
    at low     860.00: R/R 2.17:1, stop 1.51 ATR (8.1%)   ✓
    at mid     861.50: R/R 2.10:1, stop 1.54 ATR (8.3%)   ✓
    at high    863.00: R/R 2.04:1, stop 1.57 ATR (8.5%)   ✓
    size $270 ≈ 0.3134 sh at the mid; risk to stop $22.41 = 0.7% of $3,426   ✓ ≤ 2%
# same window, honest T1 = 980 (50-DMA 980.28 / 10-28 high 979.80)
    at low     860.00: R/R 1.71:1, stop 1.51 ATR (8.1%)   ✘ R/R < 2
    at mid     861.50: R/R 1.66:1, stop 1.54 ATR (8.3%)   ✘ R/R < 2
    at high    863.00: R/R 1.60:1, stop 1.57 ATR (8.5%)   ✘ R/R < 2
# just above the 10/22 low, 851-855 / 790 / 980
    at low     851.00: R/R 2.11:1, stop 1.31 ATR (7.2%)   ✘ stop < 1.5 ATR
    at mid     853.00: R/R 2.02:1, stop 1.36 ATR (7.4%)   ✘ stop < 1.5 ATR
    at high    855.00: R/R 1.92:1, stop 1.40 ATR (7.6%)   ✘ R/R < 2; stop < 1.5 ATR
# 9/14-low zone 900-910 / 835 / 1,011.77
    at low     900.00: R/R 1.72:1 ✘ · at mid 905.00: R/R 1.53:1 ✘ · at high 910.00: R/R 1.36:1 ✘
# breakout retest 1,012-1,020 / 940 / 1,108.72
    at low   1,012.00: R/R 1.34:1 ✘ · at mid 1,016.00: R/R 1.22:1 ✘ · at high 1,020.00: R/R 1.11:1 ✘
```
**Why nothing passes.** With a 1.5-ATR stop, 2:1 needs **3 ATR ($139) of open air** between the entry and the first resistance.
The entry also has to sit above $849.25 (§4a: a lower low is not evidence). The air from $849.25 to ≈ $980 is $131. Above
980, resistance comes every $25–70 up to $1,108.72.

**The condition that would create a zone:**
- **(a)** ATR(14) falls to **≤ $40** while MU pulls back and holds above $849.25. Then **$850–853 with a $790 stop pays 2:1 to
  ≈ 980.** Re-run `levels.py`, because the window is only $3 wide.
- **(b)** A weekly close above **$1,108.72** (9/25 high). Then re-derive against the $1,255 June high.

Until then, cash is the position.

## Fundamentals
- **FQ4 FY26** (8-K, 2026-09-30): revenue **$54.23B**, non-GAAP gross margin **87.0%**, EPS $33.42, operating cash flow $43.97B,
  adjusted FCF **$33.20B**. FY26 revenue $133.19B.
- **FQ1 FY27 guide:** revenue **$61.5B ± $1.5B** (+13% q/q), gross margin ≈ **86.25%**, EPS **$38.15 ± $1.00**. Alpha Vantage
  shows an EPS estimate of $37.93 (`levels.py`, 10/28).
- **Valuation** (stockanalysis, 10/28 10:58 ET, price $967.50): market cap **$1.09T**, EV $1.03T, forward P/E **5.48**,
  trailing 13.02, EV/sales 7.71. Consensus FY27 EPS **$176.58** (+134%) and FY28 **$206.89** (+17%), so the stock trades at 5.5× /
  4.7× at $969.18.
- **Balance sheet** (stockanalysis, latest quarter): cash $43.43B, debt $5.18B. The page also states "net cash $68.27B", which
  does not reconcile with cash minus debt ($38.25B); the gap is presumably long-term investments. Shares +1.60% y/y.
- **Margins (TTM):** gross 80.72%, operating 74.59%, FCF $58.96B.

## News & catalysts (last 30d / next 90d)
- 10/28: **SK hynix Q3**: revenue ₩104.62T (+31.9% q/q), operating profit **₩83.33T** (79.7% margin), 9.7% over FnGuide.
  "Effectively sold out through 2029". 2027 demand growth seen at mid-20s% for DRAM and high-teens for NAND (24/7 Wall St).
  Investing.com reports "mid-20%" as Q4 DRAM bit-shipment growth instead; the two conflict. 2027 capex up significantly.
  ≈ ₩100T of 2026 shareholder returns. **Confirming**, with a supply caveat.
- 10/28: MU +4.1% premarket to $967 (TipRanks 09:41 UTC). KOSPI +6.63%, SK hynix +10.89%, Samsung +9.01% (Korea JoongAng Daily). **Confirming.**
- 10/22–10/26: analysts reiterated, no downgrades: RBC Buy $1,500 and Needham Buy $1,650 (10/22), Wedbush $1,400 (10/23), BofA Buy
  $1,550 (10/26) (stockanalysis). **Neutral**, since this is already the consensus.
- 10/20: TrendForce news digest. 4Q26 DRAM ≈ +20% q/q "despite slower gains". LTA price ceilings are starting to bind. CXMT's
  4F² is "generally expected" to commercialize after 2028. **Neutral**: the rate of change is slowing, and the CXMT fear is pushed out.
- 9/30: TrendForce, 4Q26 conventional DRAM +10–15%, NAND +15–20%, consumer demand weak. **Neutral.**
- Next: **10/28 14:00 ET FOMC** (no trades today) · **10/29** Samsung detailed Q3 + call, SNDK report (AMC), PCE 08:30 ET ·
  11/6 October jobs report, 08:30 ET (calendar sites, not confirmed on bls.gov) · **≈ 12/16** FQ1 report.

## Positioning & sentiment
- **Short interest** 22.53M shares at the 10/15 settlement, down from 26.02M on 9/30. 1.0 day to cover (Nasdaq). 2.00% of float
  (stockanalysis). No squeeze fuel, and no crowded short either.
- **Analysts:** 49, Strong Buy. Mean **$1,562**, median $1,550, low $361, high $3,000 (S&P via stockanalysis, 10/26). TipRanks: 29
  analysts, mean $1,621.67 (10/28).
- **Crowding:** MU trades as SK hynix's US proxy (+340.5% over 52 weeks, stockanalysis 10/28). The "linkage" cuts both ways: KOSPI
  sidecars fired two sessions running (10/27–10/28) on the way up.
- **Insiders:** Investing.com (10/28) mentions Form 4 activity on 10/27; details not verified. The 10/14 entry logged ≈ $259M of
  10b5-1 sales in 6 months and zero buys.

## What would make me wrong
- MU never pulls back. A close above 1,011.77 and then 1,108.72 leaves the desk in cash through a re-rate. The cost of being wrong
  is ≈ +10–15% on a ≤ $270 line, about $27–40. That is the price of not buying a 1.6:1 setup.
- A hawkish FOMC today or a soft Samsung call on 10/29 sends MU back under $900 without a higher low. In that case the old zone
  would have been a falling knife anyway.
- The rate of change turns up: a 1Q27 contract forecast above +10% would shrink the peak-cycle discount the stock is paying.

## Sources
- `levels.py MU` (Yahoo chart API daily bars + Alpha Vantage calendar), run 2026-10-28 at 10:52 ET data, with the zone checks above
- [Micron FQ4 FY26 8-K press release](https://www.sec.gov/Archives/edgar/data/723125/000072312526000018/a2026q4ex991-pressrelease.htm) — 2026-09-30
- [stockanalysis MU statistics](https://stockanalysis.com/stocks/mu/statistics/) · [forecast](https://stockanalysis.com/stocks/mu/forecast/) — fetched 2026-10-28
- [24/7 Wall St: SK Hynix's profit jumped 632%](https://247wallst.com/investing/2026/10/28/sk-hynixs-profit-jumped-632-as-ai-eats-the-worlds-memory/) — 2026-10-28 07:16 ET
- [Seoul Economic Daily: SK hynix 79.7% operating margin](https://en.sedaily.com/finance/2026/10/28/sk-hynix-posts-record-797-percent-operating-margin-in-third) — 2026-10-28 08:39 KST
- [Investing.com: why is Micron rallying today](https://www.investing.com/news/stock-market-news/why-is-micron-technology-stock-rallying-today-93CH-4978112) — 2026-10-28
- [TipRanks: MU, SNDK, SK hynix premarket 10/28](https://www.tipranks.com/news/why-are-micron-sandisk-and-sk-hynix-stocks-extending-gains-in-premarket-today-october-28) — 2026-10-28
- [Korea JoongAng Daily: Kospi surges past 6,000](https://koreajoongangdaily.com/business/kospi-surges-past-6000-as-sk-hynix-record-earnings-reignite-ai-rally/12943596) — 2026-10-28
- [TrendForce news: DRAM ≈ +20% q/q in 4Q26 despite slower gains](https://www.trendforce.com/news/2026/10/20/news-dram-prices-seen-rising-20-qoq-in-4q26-despite-slower-gains-ai-demand-tight-supply-support-outlook/) — 2026-10-20
- [TrendForce press release: 4Q26 contract prices](https://www.trendforce.com/presscenter/news/20260930-13258.html) — 2026-09-30
- Nasdaq API: MU short interest (10/15 settlement) and earnings-surprise history, fetched 2026-10-28
- Unverified this session: the macro brief's "DRAM ASP +high-20s% q/q" for SK hynix Q3 (CNBC returned 403; no other source gave Q3 ASPs)

---

## MU — stopped out 2026-10-22 (not held)

**Verdict:** WATCH · no re-entry before the memory prints (SK hynix ≈ 10/27, Samsung and SNDK 10/29) *and* the post-mortem
(circuit breaker fired 10/22) · **Conviction:** Low on the setup.

| | |
|---|---|
| Exit | Broker stop $850 fired at ≈ 15:40–15:45 ET (5-min lows $850.60 / $849.25). **Fill estimated at $850.00** → ≈ −$16.45 + $1 fee; confirm on the next statement |
| The day | Open $880.08, low $849.25, close **$856.49** (−6.3%); SOX −6.7% |
| Cause | Not MU-specific: the AI-capex and financing scare (Meta's negative FCF on $35B of capex; Lam's supply constraints into 2027) |
| After the close | WDC beat and guided above (Q2 revenue $5.0–5.2B vs $4.57B), then reportedly ≈ −8% after hours on input costs and capex |
| Line result | Bought 10/15 at $926.20 on the desk trigger (desk error: R/R 1.4:1 at the fill, no ceiling). Ends ≈ −$18.45 with both fees |

**Lesson:** the entry was at the wrong price, not the stop at the wrong level. At $926 the $850 stop was 1.6 ATR away. That is
just wide enough for normal days, but not for a −6% sector day. A buy at ≤ $910 (the 2:1 price) would have left room.

**Sources:** Yahoo chart API MU daily and 5-min bars, fetched 2026-10-22 17:30 ET ·
[investinglive, 10/22: Nasdaq sinks as chip stocks tumble](https://investinglive.com/stocks/nasdaq-sinks-as-chip-stocks-tumble/) ·
[24/7 Wall St, 10/22: chip stocks fall as supply warning deepens AI selloff](https://247wallst.com/investing/2026/10/22/chip-stocks-fall-as-supply-warning-deepens-ai-selloff-marvell-and-amd-sink-8-intel-drops-7/) ·
[Investing.com, 10/22: Western Digital earnings](https://www.investing.com/news/stock-market-news/western-digital-surges-on-earnings-beat-upbeat-guidance-as-ai-stocks-slump-4967303)

---

## MU — update 2026-10-19

**Verdict:** HOLD with the $850 stop · adds locked to the 10/29 prints · **Conviction:** Med. Back above the $880–895
zone on the sector bounce. No new dated MU or CXMT news since 10/16 (sweep 10/19); the peak-cycle question is still
answered only by the memory prints.

| | |
|---|---|
| Price | **$914.32** (2026-10-19, 10:35 ET, +4.0%); close $878.84 (10/16, −5.6%); 10/15 flush low **$858.00** |
| 20 / 50 / 200-DMA | $1,026.5 / **$983.9** (rising) / $721.0 — price −7.1% under the 50 |
| RSI(14) · ATR(14) | 39.8 · **$48.69 = 5.3% a day** · −27% from the 6/25 high of $1,255 |
| Position | 0.2159 sh @ $926.20 = ≈ $197, 5.7% of the sleeve, −1.3% |
| Stop | **$850** (broker, confirmed live 10/19): 7.0% / 1.3 ATR below. Risk ≈ $14 |
| Sell zone (⅓) | $1,030–1,045 → 0.07 sh · target 2 $1,090–1,109. R/R from today: 1.8:1 to $1,030 |
| Adds | 0 of 2, **locked** until WDC (10/22), SK hynix (≈ 10/27) and Samsung/SNDK (10/29) report; then only in $880–895, ≤ $150 |
| Next earnings | ≈ mid-December (not announced) |

**Analysts (dated):** 10/5–10/6, Morgan Stanley kept Overweight ($1,200) and Susquehanna Positive ($2,000); mean target
≈ $1,581. Morgan Stanley's view after the FQ4 report: 2027–28 supply/demand tighter than 2026, but estimate raises may
lag earlier quarters. **CXMT** is the #4 DRAM maker, within ≈ 1 point of Micron's share (Counterpoint, Q2 2026), and still
behind in HBM. That is the bear case the 10/29 prints have to answer.

**Sources:** Yahoo chart API MU 1y daily, fetched 2026-10-19 10:35 ET · [parameter.io, 10/6: analysts stick with bullish calls](https://parameter.io/analysts-stick-with-bullish-micron-mu-calls-despite-minor-dip-following-banner-fiscal-year/) · [Stocktwits: Morgan Stanley flags estimate raises may lag](https://stocktwits.com/news-articles/markets/equity/micron-s-post-earnings-estimate-hikes-may-lag-previous-quarters-flags-morgan-stanley/cZMSCqhRBQx) (undated) · [PCGH: CXMT DRAM share, Counterpoint Q2](https://www.pcgameshardware.de/RAM-Hardware-154108/News/CMXT-Speicher-DRAM-Marktanteil-1550368/).

---

## MU — position card 2026-10-16

**Verdict:** HOLD with the stop · **Conviction:** Med. Bought 10/15 at 15:40 ET, $926.20 × 0.2158615 sh = $199.93, on the
desk's close trigger (a close ≥ $895 after the $858 flush; it closed at $931.24). The desk proposed ≈ $150. It is the one
memory name; SNDK was stopped out on 10/15.

| | |
|---|---|
| Price | **$902.52** (2026-10-16, 09:44 ET; low $894.31); close $931.24 (10/15); 10/15 low **$858.00** |
| 20 / 50 / 200-DMA | $1,034.2 / $983.6 / $718.0 · RSI 36.2 · ATR $47.81 = 5.3% a day |
| Stop | **$850**, under the 10/15 flush low. That is −8.2% from cost. Risk ≈ $11 at today's price |
| Sell zone (⅓) | **$1,030–1,045** → ⅓ = 0.07 sh · target 2 **$1,090–1,109** |
| Reward/risk at the fill | **1.4:1 to $1,030 ✘**, 2.1:1 to $1,090. **Desk error:** the trigger had a floor ($895) and no ceiling. For 2:1 to $1,030 the fill needed to be ≤ $910 |
| Ladder | +25% $1,157.75 · +40% $1,296.68 · +75% $1,620.85 · hard exit −15% $787.27 |
| Adds | 0 of 2. **Locked** until the memory prints (WDC 10/22, SK hynix 10/27, Samsung and SNDK 10/29) answer the peak-cycle question. Then only in $880–895, ≤ $150 |
| Next earnings | ≈ 12/16 (not announced). Buyback usable from 12/9 |

The 10/14 thesis and risks below still stand. What changes: MU is now held, so the stop is the decision, and the 10/29 memory
prints decide whether it gets an add.

## Sources
- Yahoo chart API MU 1y daily and 5-day 5-min bars, fetched 2026-10-16 09:44 ET (fill check: the 15:40 ET bar on 10/15 was
  925.05–927.90)
- Amana statement 2026-10-15 (`portfolio/statements/amana-statement-2026-10-15_2026-10-15.pdf`)

---

## MU — Micron Technology — deep dive 2026-10-14 (client: "I am hearing it might double on X posts")

**Verdict:** WATCH — buy zone **$880–895 from 11/2**, after the memory prints of 10/27–10/29 · **Conviction:** Med — the
best business in memory and cheap on this year's earnings, but the stock is behaving like a cycle peak. A doubling needs the
market to stop pricing the downturn, not better earnings.

| | |
|---|---|
| Price | **$922.01** (2026-10-14, 13:43 ET, −3.3%); close $953.19 (10/13); −10.4% since 10/9 |
| 50-DMA / 200-DMA | **$982.6** (rising) / **$711.8** (rising) — price under the 20 (1,042.6) and 50, above the 200 |
| 52-wk high / low | $1,255.00 (2026-06-25; closing high 1,213.56) / $187.42 · **−26.5% from the high**, +379% in a year |
| RSI(14) · ATR(14) | 37 intraday (40.4 at the 10/13 close) · **$46.30 = 5.0%** |
| Entry zone | **$880–895** (8/24 low 887.6, 7/7 low 891.7, 9/14 low 902.6) |
| Invalidation (stop) | **$830** (under the 6/9 low 854.4; 1.2–1.4 ATR) / or event: memory contract prices guided flat or down, a second gross-margin cut |
| Target 1 / 2 | **$1,030–1,045** sell zone (10/9 close 1,029, 20-DMA 1,042.6, 9/9 high 1,042.4) / $1,090–1,109 (10/7 and 9/25 highs) |
| Reward/risk (T1) | **2.1:1 at $895 · 3.0:1 at $880** ✓ — at today's $922 with the same stop: 1.2:1 ✘ |
| Size | ≈ $200 (≈ 5.7% of the sleeve), risk to the stop ≈ $14 |
| Timeframe | months |
| Next earnings | ≈ **12/15–16** (not announced; FQ1 ends ≈ 12/3) · buyback ($35.16B) usable from **12/9** |

## Thesis
Micron is the US memory leader: DRAM (76% of FY26 revenue), HBM for AI accelerators, and NAND (24%). The AI build-out has
turned memory into the tightest part of the chain.
- **Results** (8-K, 9/30): FY26 revenue **$133.2B** (FY25 $37.4B). FQ4 revenue **$54.2B**, 87% gross margin, EPS $33.42,
  adjusted FCF $33.2B in the quarter. FQ1 FY27 guide **$61.5B ± $1.5B**, EPS $38.15.
- **Balance sheet and buyback:** net cash ≈ $68B. A **$35.2B buyback** opens on 12/9.
- **Contracts:** $134B of contracted backlog. The "vast majority" of 2027 HBM supply is sold at higher prices, including a
  custom HBM4E with NVIDIA.
- **Valuation:** **5.2× FY27 consensus EPS** ($176) and 4.5× FY28 ($206). Analysts: 49, average PT **$1,561 (+69%)**, high
  $3,000 (D.A. Davidson, 10/7), low $361. Wall Street has never been more bullish on the numbers.

## Why it is not a buy today
1. **The cycle pattern.** Morgan Stanley (10/13): memory stocks peaked ≈ 4 months before earnings in 2008 and 2012, and
   ≈ 8 months before in 2018. MU's price peaked on **6/25 at $1,255**, and its earnings have kept rising since. That is the
   pattern. 5× earnings is the multiple the market pays for a peak, the same 3–4× it pays Samsung and SK hynix.
2. **The rate of change has turned.** Revenue growth quarter on quarter: +75% → +74% → +31% → +13% (guide). The FQ1 gross
   margin guide is the **first decline of the cycle** (87.0% → 86.25%). TrendForce: 4Q DRAM contract prices +10–15%, "increases
   moderating".
3. **Supply is coming.** Micron's own FY27 capex is **> $50B** (FY26: $27.4B). SK hynix raised capex ≈ 50%. Morgan Stanley
   sees new supply from 2H27. China's CXMT claims server DRAM by end-2026 (the 10/10 trigger of this sell-off).
4. **HBM share.** Counterpoint Q2-26: Micron 21% → **18%**, Samsung 21% → 33% (snippet-sourced).
5. **The chart.** Price is under the 20- and 50-DMA, and the 10/13 gap ($953.6–978.5) is unfilled. Price is testing today's
   low ($919.6) and the 9/14 low ($902.6). KOSPI fell 5.5% on 10/13; SK hynix −10% and Samsung −7.4%.
6. **Insiders:** ≈ $259M sold in 6 months and **zero bought**. The CEO alone sold $182M at $512–1,192 (10b5-1).
7. **Your account:** you already hold SNDK (memory), and the plan says one memory name at a time. The headline lock (§4)
   applies: the peak-cycle and CXMT news question the memory thesis. Nothing new in memory until the hard data of
   10/27–10/29 (SK hynix Q3, Samsung final Q3, SNDK).

## "Could it double?" — the arithmetic
From $922, a double is **$1,844 = a $2.09T market cap = 10.5× FY27 consensus EPS** (8.9× FY28). The earnings already exist
in the forecasts. What is missing is the multiple: the market would have to stop pricing a 2028–29 downturn and pay about
twice today's multiple. That is the bull case (D.A. Davidson's $3,000 uses ≈ 19×). The same arithmetic in reverse: the
July-crash low of $737.9 is −20% from here, and Morningstar's fair value is $455. "Might double" and "might fall 20%" are
both true of a stock with a 5% daily range. Neither is a level.

## If you want memory in this account, MU beats SNDK
MU has more data-center exposure (63% of FQ4), DRAM and HBM instead of NAND, $68B of net cash, and a $35B buyback starting
12/9. If the 10/28 rule sells SNDK (still under its ≈ $1,590 50-DMA), MU is the memory name to take its place, at its level,
from 11/2.

## Levels
- Supports: 919.6 (10/14 low) · **902.6** (9/14) · **887.6–891.7** (8/24, 7/7) · 854.4 (6/9) · 804.0 (7/17) · **737.9**
  (7/29 crash low) · 711.8 (200-DMA, rising).
- Resistances: **953.6–978.5** (10/13 gap) · 982.6 (50-DMA) · 1,017–1,029 · **1,042** (20-DMA + 9/9 high) ·
  1,089–1,109 · 1,213.6 / 1,255.0.
- Earnings reactions (last 4): +10.2% / −3.8% / +15.7% / +3.0%.

## What would make me wrong
- SK hynix (10/27–28) and Samsung (10/29) guide memory prices up again → the cycle fear eases and MU re-rates without dipping
  to the zone. Then the entry becomes a close back above the 50-DMA (≈ $985), written fresh.
- A close under $830 → the August–September base has failed; the next stop is the July low ($738).
- TrendForce's 1Q27 contract forecast flat or negative; a second gross-margin cut on ≈ 12/16; CXMT shipping server DRAM.

## Sources
- Yahoo chart API MU 2y daily bars, fetched 2026-10-14 13:43 ET
- FQ4 FY26 8-K https://www.sec.gov/Archives/edgar/data/723125/000072312526000018/a2026q4ex991-pressrelease.htm — 2026-09-30
- FQ3 / FQ2 / FQ1 8-Ks (6/24, 3/18, 12/17) — sec.gov/Archives/edgar/data/723125/
- FY26 10-K https://www.sec.gov/Archives/edgar/data/723125/000072312526000023/mu-20260903.htm — filed 2026-10-09
- https://stockanalysis.com/stocks/mu/statistics/ · /forecast/ — 2026-10-08/14
- https://investinglive.com/stocks/micron-could-triple-to-3-000-says-d-a-davidson-as-stock-trades-at-six-times-earnings/ — 2026-10-07
- https://www.kucoin.com/news/flash/morgan-stanley-low-valuation-of-memory-stocks-hides-high-risk-amid-cycle-peak — 2026-10-13 (secondary)
- https://www.morningstar.com.au/stocks/this-us-ai-winner-has-been-unstoppable-is-it-time-sell — 2026-06-05
- https://finance.yahoo.com/markets/stocks/articles/sk-hynix-plunges-9-china-061401801.html — 2026-10-13
- https://www.heygotrade.com/en/news/micron-blowout-quarter-ai-memory-supercycle-mu-sk-hynix-hbm/ — 2026-10-01
- https://api.nasdaq.com/api/quote/MU/short-interest — 9/30 settlement · SEC Form 4s (EDGAR submissions, 4/14–10/14)
