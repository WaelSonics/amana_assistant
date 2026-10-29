# BE — Bloom Energy — research log

One file per ticker; newest entry first. Each entry is dated; numbers are as of that date.

Entries:
- 2026-10-28 (deep dive; first entry in this file. Earlier BE context: PLAN.md §4a/§6b, journal/2026-10-24-check.md, journal/2026-10-27-check.md)

---

## BE — Bloom Energy — deep dive 2026-10-28

**Verdict:** WATCH · **no zone passes** (levels.py, below) · no buy before 11/2 · **Conviction:** Low on the setup, Med on
the business. The Q3 print was strong. At an 8.7% daily ATR, though, the plan's stop rule (≥ 1.5 ATR, ≤ 15%) and its 2:1 rule
cannot both be met with the $240–253 resistance band only 8–14% overhead.

| | |
|---|---|
| Price | **$222.42** (2026-10-28 10:52 ET, levels.py; refresh $224.31 at 11:11 ET, RSI 44.5, which changes no check); close $218.50 (10/27); 10/23 close $193.30, low **$189.00** |
| Position | not held. Stopped 10/12 at $260.20 (+$8.04 on the line) |
| 20 / 50 / 200-DMA | $247.99 / $247.78 (falling) / **$220.55 (rising)**: price +0.8% over the 200, −10.2% under the 50 |
| RSI(14) · ATR(14) | 43.8 · **$19.42 = 8.7% a day** · 52-wk $75.70–351.28 (−37% from the high) |
| Chase guard | ok (RSI 43.8; under the 50-DMA) |
| Entry zone | **none passes**. Checks A–C below |
| Invalidation (any future setup) | price: a close under **$189.00** (the 10/23 low); stop ≈ $186, under the 8/24 low $185.93 · event: Q4 FCF negative again, or a FY26 guide cut |
| Target 1 / 2 | **$239.85–241.37** (10/15 and 10/21 highs) / $253.31 (8/13 high; the 20/50-DMAs sit at ≈ $248) |
| Reward/risk (T1) | 0.65–0.87 : 1 from $214–218 ✘ |
| Size if one ever passes | ≈ $190 (5.5% of the sleeve), one fill; risk well under the $69 cap |
| Timeframe | weeks to months |
| Next earnings | ≈ late Feb 2027 (est.; not announced, and not in Alpha Vantage's 3-month calendar) |
| Earliest buy | **11/2** (client commitment), and only on a zone that passes levels.py. None exists today |

### What changed since the last BE note (journal 10/24 "BE: no", 10/27 check; PLAN §6b "invalid")
- **Price:** $193.30 (10/23 close) → $203.92 (10/26) → $218.50 (10/27) → $222.42 now. That is **+17.7% off the $189.00 low in
  three sessions**, back on the rising 200-DMA.
- **The §4a evidence, both readings:**
  - **10/24 wording** ("a higher low above $186, then a daily close above $218"): **literally met.** The 10/23 low ($189.00) held
    above the 8/24 low ($185.93), and 10/27 closed at $218.50. Both margins are thin: $3.07 and $0.50.
  - **10/27 desk reading** ("a pullback that holds above $189, then a close above $218"): **not met.** There has been no
    pullback. Each low since 10/23 is higher ($192.15, $211.29, $217.90 today). That is a V-rebound, not a tested higher low.
  - **Neither reading unlocks a buy.** §4a also needs a new stop written first and R/R ≥ 2:1, plus every §2 rule. No zone
    passes (checks below).
- **The client wanted to buy on 10/24 and 10/27.** What the rules cost this time:
  - $190 at the 10/26 open ($193.00) would be **≈ +$29 (+15%)** now.
  - $190 at the 10/27 open ($214.12) would be ≈ +$7 (+3.9%).
  - On 10/26 no compliant stop existed. 1.5 ATR under $193 is $163, which is 15.5% away, past the 15% hard exit. The client's
    instinct made money. Under v3 it was still a buy with no valid stop, in a name that fell 19% in the two sessions before.

### levels.py zone checks (2026-10-28 10:52 ET, `--size 190 --sleeve 3426`)
**A. Buy the 200-DMA / 10/27 close. Stop under the 8/24 low. T1 = nearest real resistance (10/15–10/21 highs ≈ $240):**
```
  Setup: zone 214.00–218.00, stop 184.00, T1 240.00
    at low     214.00: R/R 0.87:1, stop 1.54 ATR (14.0%)   ✘ R/R < 2
    at mid     216.00: R/R 0.75:1, stop 1.65 ATR (14.8%)   ✘ R/R < 2
    at high    218.00: R/R 0.65:1, stop 1.75 ATR (15.6%)   ✘ R/R < 2; stop > 15% (hard exit)
    size $190 ≈ 0.8796 sh at the mid; risk to stop $28.15 = 0.8% of $3,426   ✓ ≤ 2%
    price 222.42 is +2.0% above the zone — wait for the alert at 218.00
```
**B. Same zone, with levels.py's listed resistance $253.31 as T1.** This T1 is too generous: it skips the $240 highs. It still fails.
```
  Setup: zone 214.00–218.00, stop 184.00, T1 253.31
    at low     214.00: R/R 1.31:1, stop 1.54 ATR (14.0%)   ✘ R/R < 2
    at mid     216.00: R/R 1.17:1, stop 1.65 ATR (14.8%)   ✘ R/R < 2
    at high    218.00: R/R 1.04:1, stop 1.75 ATR (15.6%)   ✘ R/R < 2; stop > 15% (hard exit)
```
**C. A higher-low zone: stop under the $189 low, T1 $241.37:**
```
  Setup: zone 200.00–204.50, stop 186.00, T1 241.37
    at low     200.00: R/R 2.96:1, stop 0.72 ATR (7.0%)   ✘ stop < 1.5 ATR
    at mid     202.25: R/R 2.41:1, stop 0.84 ATR (8.0%)   ✘ stop < 1.5 ATR
    at high    204.50: R/R 1.99:1, stop 0.95 ATR (9.0%)   ✘ R/R < 2; stop < 1.5 ATR
    size $190 ≈ 0.9394 sh at the mid; risk to stop $15.27 = 0.4% of $3,426   ✓ ≤ 2%
    price 222.42 is +8.8% above the zone — wait for the alert at 204.50
```
**No passing zone. What would create one:**
- **The arithmetic.** A 1.5-ATR stop at 2:1 needs T1 at least **3 ATR (≈ $58) above the entry**, and the stop must stay within 15%.
  The $240–253 resistance is far closer than that.
- **Path 1 (the realistic one): zone C, narrowed to $200–204** (stop $186, T1 $241.37: R/R 2.1–3.0). It becomes valid only when
  both happen:
  1. BE pulls back and **holds above $189**. That would be the real higher low.
  2. The **ATR(14) falls to about $9–12** (≈ 5–6%), so the stop clears 1.5 ATR.
  The lowest of 26 ten-session ATR samples in the last 12 months (levels.py bars) was **6.7% (4/23/26)**. Expect no
  v3-compliant BE buy soon.
- **Path 2: clearing $253.31 does not fix it.** T1 then becomes $283.83 (9/8 high), and a retest entry near $253 with a
  1.5-ATR stop pays only ≈ 1:1.

### Thesis
Bloom sells solid-oxide fuel-cell power servers. They put power into data centers faster than a grid connection can. Q3 was a
beat and raise: revenue +138%, product +179%, the third FY26 guide raise this year, and a 23% non-GAAP operating margin. The
market is pricing the cash. Q3 free cash flow was ≈ −$181M (working capital plus $153.5M of capex for capacity), shares are up
5.5% this year, and the stock trades at ≈ 15× sales. Morgan Stanley's 38 GW US AI power-gap estimate (10/27) is the bull case.
FCF and dilution are the bear case. Under v3 it would be an AI satellite that behaves like a speculative name (8.7% ATR).

### Chart & technicals (levels.py, 10/28 10:52 ET; chart `scratchpad/charts/BE.png`)
- **Trend:** above a rising 200-DMA ($220.55, up from $205.51 twenty sessions ago), but under a falling 50 ($247.78) and 20
  ($247.99). It made a lower high at $302.35 on 9/29 against $351.28 on 6/25. This is a broken uptrend testing its 200.
- **Levels:**
  - Support: $218.50 (10/27 close, ≈ the 200-DMA), then $211.29 (10/27 low), $197.50 (9/1), **$189.00 (10/23)**, $185.93
    (8/24) and $157.33 (7/29).
  - Resistance: today's high $227.55, then $233.5–239.85 (10/15–10/19), $241.37 (10/21), the $248 MAs, and $253.31 (8/13).
- **Volume:** the 10/23 capitulation came on 36.0M shares (≈ 2.5× normal). The rebound volume is fading: 21.1M on 10/26,
  15.7M on 10/27, 5.0M by 10:52 ET today.
- **RSI** 43.8 (rising from the mid-30s). **ATR** $19.42 = 8.7%.
- **levels.py caveat:** its support list starts at $216.04, a 4/28 swing low six months old. It cannot see the 10/23 low,
  because a swing needs 5 bars on each side. Its first resistance, $253.31, skips the $240 highs for the same reason.

### Fundamentals (Q3 8-K, 2026-10-22)
- **Revenue** $1,235.8M (+138.1% y/y, +16% q/q). Product $1,073.6M (+179.4%), service $67.6M.
- **Margins:** non-GAAP gross margin 34.5% (+412 bp), GAAP 33.8%. Non-GAAP operating income $285.7M (23.1%), GAAP $225.4M.
  Non-GAAP EPS $0.94 vs ≈ $0.69 expected (Trefis, 10/27); GAAP EPS $0.78.
- **Cash:** operating cash flow −$27.1M, capex $153.5M, **free cash flow ≈ −$180.6M** (year to date ≈ +$42M). CFO: "not the
  beginning of a trend". Backlog was not disclosed; the CEO said it is "continuing to expand faster than our revenue".
- **FY26 guide, raised for the third time:**
  - revenue $4.4–4.6B (≈ +122%);
  - non-GAAP gross margin ≈ 34%;
  - non-GAAP operating income $960M–1,030M;
  - non-GAAP EPS $3.10–3.40.
- **Balance sheet (9/30):** cash $2,486.7M against recourse debt $2,473.5M, so roughly net-neutral. Basic shares 295.5M vs
  280.0M at 12/31/25 (**+5.5%**); diluted weighted average 324.3M.
- **Valuation** (desk arithmetic at $222.42): ≈ $65.7B basic market cap (≈ $72B diluted). That is ≈ 68× the FY26 non-GAAP EPS
  midpoint and ≈ 14.6× FY26 revenue (Trefis: 15.7× sales, 10/27).

### News & catalysts (last 30 days / next 90)
- **10/22:** Q3 beat and raise, S&P 500 inclusion noted in the release. *Confirming* for the business.
- **10/22–10/23:** −8.7%, then −11.2% (close $193.30) on the cash flow. *Breaking* for the chart, *neutral* for the thesis.
- **10/26–10/27:** +5.5% and +7.1% on analyst support.
  - Evercore ISI kept Outperform at $350 ("overreaction").
  - Target raises: Barclays $308 → $316, Bernstein $306, Wells Fargo to $182.
  - Morgan Stanley raised its 2026–28 US AI data-center power-gap estimate to **38 GW** and named Bloom (Investing.com, 10/27).
  - Also reported: Morgan Stanley target $335; JPMorgan cut to $292 and BTIG to $250 (search summary, 10/28; unverified).
  - *Confirming.*
- **Next:**
  - 10/28 FOMC: a 10-year yield at 5.02% matters for a capex-funded name.
  - Q4 report ≈ late Feb 2027: the free-cash-flow test.

### Positioning & sentiment
- **Short interest:** 17.19M shares = 6.02% of float, 1.3 days to cover, −18.1% vs 9/30 (MarketBeat, 10/15 record).
- **Analysts:** consensus "Moderate Buy", target ≈ $259 (MarketBeat via search, 10/28).
- **Insiders:** selling only for six months (MarketBeat); CCO Aman Joshi sold 8,437 shares at $277.17 on 10/1 (StockTitan, via
  search; unverified).
- **Crowding:** an AI-power momentum name sold with the AI-capex basket on 10/22–10/23. Not extended now (RSI 43.8).

### Thesis scorecard
| Pillar (falsifiable) | Expected | Status (dated) | Trend |
|---|---|---|---|
| Revenue grows > 100% y/y | ≥ 100% | Q3 +138.1% (10/22) | improving |
| Non-GAAP gross margin ≈ 34% | ≥ 33% | 34.5% (10/22) | stable |
| FCF positive for the year | > 0 | Q3 ≈ −$181M; YTD ≈ +$42M (10/22) | **weakening** |
| Guide raised, not cut | ≥ $4.4B | raised to $4.4–4.6B, third raise (10/22) | improving |
| Dilution contained | < 5% a year | +5.5% in 9 months (280.0M → 295.5M) | **weakening** |

- **Thesis-break exits (if re-entered):** Q4 FCF negative again with no inventory release; any guide cut; a close under $189.
- **Conviction:** Low on the setup. It rises if a higher low holds above $189 while the ATR contracts. It falls on a close
  under $189.

### What would make me wrong
- **BE runs through $248–253 without a pullback.** The rules will have missed it, as they did on 10/26–10/28. That is the cost
  of a stop rule on an 8.7%-ATR name.
- **A close under $189.00** means the rebound failed. Next supports: $185.93, then $157.33.
- **Q4 FCF negative again**, a guide cut, or new dilution (convertible or ATM).
- **Hyperscaler order delays:** a repeat of the 10/22 capex/financing scare.

### Sources
- levels.py (Yahoo chart API daily bars; Alpha Vantage calendar), run 2026-10-28, quotes 10:52 ET; zone checks A–C the same
  session; ATR history computed from the same bars
- [Bloom Energy Q3 2026 results, 8-K ex. 99.1](https://www.sec.gov/Archives/edgar/data/0001664703/000162828026066890/ex991_q326financialresults.htm): 2026-10-22
- [Investing.com: Why is Bloom Energy stock surging today?](https://www.investing.com/news/stock-market-news/why-is-bloom-energy-stock-surging-today-93CH-4975912): 2026-10-27 09:46
- [Trefis: Why did Bloom Energy stock jump?](https://www.trefis.com/stock/be/articles/620854/why-did-bloom-energy-stock-jump/2026-10-27): 2026-10-27
- [24/7 Wall St: fuel-cell stocks rally as post-earnings selloff keeps unwinding](https://247wallst.com/investing/2026/10/27/fuel-cell-stocks-rally-as-post-earnings-selloff-keeps-unwinding-bloom-energy-jumps-6-fuelcell-climbs-5-plug-power-gains-3/): 2026-10-27
- [Benzinga: What's going on with Bloom Energy stock on Monday?](https://www.benzinga.com/trading-ideas/movers/26/10/62587503/whats-going-on-with-bloom-energy-stock-on-monday): 2026-10-26
- [MarketBeat: BE short interest](https://www.marketbeat.com/stocks/NYSE/BE/short-interest/): 10/15 record, published 10/26
- [StockTitan: BE SEC filings (insider Form 4s)](https://www.stocktitan.net/sec-filings/BE/): via search, 10/28
