# RKLB — Rocket Lab — research log

One file per ticker; newest entry first. Each entry is dated; numbers are as of that date.

Entries:
- 2026-10-28 (deep dive + 11/9 earnings preview)
- 2026-10-19 (update)
- 2026-10-15

---

## RKLB — Rocket Lab — deep dive 2026-10-28

**Verdict:** WATCH, no setup · speculative slot only · **Conviction:** Low. It bounced +16.5% off the 10/20 low on the Neutron
stage-2 shipment, but it is still 28% under a **falling 200-DMA**: the protocol allows no fresh longs. No zone passes
levels.py, and the report (11/9) puts a ±15% option-implied move in the way.

| | |
|---|---|
| Price | **$57.37** (2026-10-28 10:52 ET, levels.py; refresh $57.52 at 11:11 ET); close $58.31 (10/27, +8.3%, high **$59.18**); 10/20 low **$49.25** |
| 20 / 50 / 200-DMA | $61.27 / $64.90 (falling) / **$80.16 (falling)**: −11.6% under the 50, −28.4% under the 200 |
| RSI(14) · ATR(14) | 43.7 · **$3.90 = 6.8% a day** · 52-wk $37.57–151.00 (−62% from the 5/27 high) |
| Trend (levels.py) | "BELOW a falling 200-DMA → protocol: no fresh longs until it reclaims it" |
| Entry zone | **none.** The best base zone fails levels.py (below) |
| What would qualify | (1) a **close above the 200-DMA (≈ $80)**, which is the rule; and (2) a zone with a ≥ 1.5-ATR stop under a held higher low, ≤ 12% (speculative slot), with T1 ≥ 2× the stop distance away |
| Next earnings | **Mon 11/9 after the close** (company PR 10/20; call 5:00 pm ET). levels.py: 8 sessions; blackout from 11/4 |
| Earliest buy | in practice **not before 11/10** (the 11/2–11/3 window is open by date, but the 200-DMA rule blocks it). Speculative slot ≤ 6% at cost (≈ $205) |

### What changed since the 10/19 entry
- **The 10/15 setup's first leg broke on 10/20:** a lower low at **$49.25**, under $49.69. Since then the lows were $49.96
  (10/22) and $49.52 (10/23): a three-touch base at **$49.25–49.96**.
- **The second leg (a close above $59.18) is not met.** On 10/27 it tagged $59.18 intraday, exactly the 10/14 close, and closed
  at $58.31. Today: $57.37.
- **Momentum repaired:** RSI 27.8 → 43.7, ATR 8.1% → 6.8%. The 200-DMA keeps falling ($81.2 → $80.16).
- **Report confirmed** for Mon 11/9 after the close (company PR, 10/20). It was "≈ 11/10, unconfirmed".
- **News:**
  - **Neutron:** the second stage and thrust module shipped by barge to LC-3, Wallops (10/26). Cantor kept Overweight at $122
    and models the first Neutron launch in **Q2 2027** (10/27).
  - **Electron:** 98th launch on 10/23, the 19th of 2026.
  - **SDA:** 8 of the 18 spacecraft are in production on the **$515M** Space Development Agency program.
  - **The rally:** +2.0% on 10/26, +8.3% on 10/27.

### levels.py zone checks (2026-10-28 10:52 ET, `--size 190 --sleeve 3426`)
**Base zone above the $49.25 low. Stop under it. T1 = nearest real resistance ($59.18: the 10/27 high and 10/14 close):**
```
  Setup: zone 53.00–55.00, stop 48.50, T1 59.18
    at low      53.00: R/R 1.37:1, stop 1.15 ATR (8.5%)   ✘ R/R < 2; stop < 1.5 ATR
    at mid      54.00: R/R 0.94:1, stop 1.41 ATR (10.2%)   ✘ R/R < 2; stop < 1.5 ATR
    at high     55.00: R/R 0.64:1, stop 1.67 ATR (11.8%)   ✘ R/R < 2
    size $190 ≈ 3.5185 sh at the mid; risk to stop $19.35 = 0.6% of $3,426   ✓ ≤ 2%
    price 57.37 is +4.3% above the zone — wait for the alert at 55.00
```
**Same zone, with levels.py's listed resistance $67.70 (9/9 high).** That T1 skips the 20-DMA ($61.27), the 10/14 high ($63.56)
and the 50-DMA ($64.90). It still fails:
```
  Setup: zone 53.00–55.00, stop 48.50, T1 67.70
    at low      53.00: R/R 3.27:1, stop 1.15 ATR (8.5%)   ✘ stop < 1.5 ATR
    at mid      54.00: R/R 2.49:1, stop 1.41 ATR (10.2%)   ✘ stop < 1.5 ATR
    at high     55.00: R/R 1.95:1, stop 1.67 ATR (11.8%)   ✘ R/R < 2
```
**No passing zone. What would create one:**
- **The squeeze.** The speculative slot's ≤ 12% stop and the ≥ 1.5-ATR rule ($5.85) leave a 10.2–12% stop band. With the
  nearest resistance 3–10% overhead, nothing fits.
- **What has to happen:**
  1. RKLB **closes above $59.18**.
  2. It holds a higher low above $49.25.
  3. It reclaims the falling 200-DMA (≈ $80). That is the protocol line and is today 40% away.

  Until then it is a falling knife with a bounce.

### Earnings preview — Q3 2026, Mon 2026-11-09 after the close (not held)
1. **Date and time:** 11/9 after the close; call 2:00 pm PT / 5:00 pm ET (company PR 10/20). levels.py: 8 sessions. Its
   blackout starts 11/4.
2. **Consensus and guide:**
   - **Consensus:** revenue **$257.19M**, EPS **−$0.0674** (MarketBeat, 10/27; Alpha Vantage −$0.05).
   - **Company Q3 guide (8-K, 8/10):**
     - revenue **$250–265M**;
     - GAAP gross margin **29–31%** (Q2: 36.1%);
     - non-GAAP gross margin 35–37%;
     - adjusted EBITDA **−$17M to −$23M** (Q2: −$8.8M).
   - **What moves the stock:** backlog ($2.36B at Q2), the Neutron schedule (the 8/10 release still said "Neutron to the launch
     pad in Q4 2026", since slipped to 2027), and cash burn / ATM use.
3. **Implied move:** **±15.1%** to the 11/13 weekly and ±16.6% to 11/20, reference $58.31 (OptionSlam, fetched 10/28). Not
   held, so no $ at stake. For a future buyer, that is ≈ 1.5× a 1.5-ATR stop distance ($5.85 = 10.2%): a gap can skip any compliant stop.
4. **Scenarios:**

   | Scenario | What has to happen | Likely reaction | Action written now |
   |---|---|---|---|
   | Bull | Revenue ≥ $265M, backlog > $2.5B, a firm Neutron date (H1 2027), no new raise | +10–20% → $63–69, into the falling 50-DMA | No chase. Still under the 200-DMA. Re-run levels.py 11/10 |
   | Base | Revenue in the guide, margins as guided, Neutron "2027" | ±5–10% | WATCH |
   | Bear | Q4 guide-down, another Neutron slip, or a new ATM | −10–15% → $49–52, at or through the $49.25 base | No knife. A new low resets the base count |

5. **History** (levels.py bars; reaction day vs the prior close):

   | Report | Opening gap | Close |
   |---|---|---|
   | 11/10/25 | +7.9% | −1.3% |
   | 2/26/26 | −7.0% | −4.9% |
   | 5/7/26 | +9.5% | **+34.2%** |
   | 8/10/26 | −4.7% | −0.0% |

   The 8/10 implied move was 16.38%; the realized close was −0.03% (OptionSlam).
6. **Decision:** not held. No buy in the blackout (11/4–11/9). Levels re-derived 11/10+.

### Thesis
Rocket Lab is the only scaled US small-launch provider (Electron, 19 launches in 2026). Its growth engine is Space Systems:
Q2 revenue $234.1M (+62%) on a record **$2.36B backlog** (8-K, 8/10). The equity story still runs through **Neutron**. The
first launch slipped from Q4 2026 to 2027 (10/14; voids in a carbon-composite tank dome), and management ties cash-flow
breakeven to it. Two pressures hang on the stock:
- the market cap is ≈ $34.9B (MarketBeat, 10/27), about **45× trailing sales** (desk arithmetic on ≈ $769M TTM, 10/15 entry);
- ≈ $2.7B of ATM sales since January 2025 (10/15 entry).

The stock is −62% from the high for good reasons. It fits only the speculative slot, and only once the trend turns.

### Chart & technicals (levels.py, 10/28 10:52 ET; chart `scratchpad/charts/RKLB.png`)
- **Trend:** under all three averages, all falling. Lower highs: $86.83 (8/10) → $78.28 (10/6) → $59.18 (10/27).
- **Base:** $49.25–49.96 (10/20–10/23).
- **Resistance:** $59.13–59.18 (10/27–10/28), $61.27 (20-DMA), $63.56 (10/14 high), $64.90 (50-DMA), $67.70 (9/9).
- **Volume:** 10/27's +8.3% came on 21.2M shares, *below* the ≈ 22.9M average (MarketBeat). That is not a high-conviction
  reversal. The capitulation was 48.6M on 10/15.
- **RSI** 43.7.

### Fundamentals (Q2 8-K, 2026-08-10; re-fetched 10/28)
- **Revenue:** $234.1M (+62%): product $181.3M, service $52.7M.
- **Gross margin:** GAAP 36.1%, non-GAAP 41.5%. Q3 guide: GAAP 29–31%, non-GAAP 35–37%. **Margins are guided down.**
- **Profitability:** adjusted EBITDA −$8.8M; net loss −$49.3M.
- **Backlog:** $2.36B (record). Cash $2.13B; ≈ $2.39B with marketable securities.
- **Debt:** debt-to-equity 0.01, current ratio 5.48 (MarketBeat, 10/27).

### News & catalysts (last 30 days / next 90)
- **10/14:** Neutron first launch slips to 2027. Target cuts followed (KeyBanc $135 → $100 on 10/15; others per the 10/19
  entry). *Breaking* (timing).
- **10/16:** Needham reiterates Buy at $120; Citigroup reiterates (MarketBeat). *Neutral.*
- **10/20:** Q3 date set for 11/9. *Neutral.*
- **10/23:** Electron's 98th launch (HawkEye 360). *Confirming* (execution).
- **10/26–10/27:** Neutron stage 2 shipped to Wallops; Cantor Overweight $122, Neutron in Q2 2027; SDA 8 of 18 in production.
  *Confirming.*
- **Next:** **11/9 report**. Neutron stage-1 dome production and inspection is targeted before Q1 2027 (Stocktwits via
  Yahoo, 10/27). The Iridium deal status was not re-verified this session.

### Positioning & sentiment
- **Short interest:** 45.3M shares = **8.26% of float**, 2.0 days to cover, +1.9% (MarketBeat, 10/15 record).
- **Analysts:** consensus "Moderate Buy", **target $102.05** (3 Strong Buy, 14 Buy, 5 Hold, 1 Sell; MarketBeat, 10/27).
- **Insiders:** sold 400,749 shares ≈ $26.96M in 90 days, including CFO Adam Spice's 140,157 shares at $70.82 on 10/1
  (10b5-1).
- **Retail sentiment:** Stocktwits turned "bearish" on a 285% message spike (10/27). A crowded retail name.

### Thesis scorecard
| Pillar (falsifiable) | Expected | Status (dated) | Trend |
|---|---|---|---|
| Neutron first launch | Q4 2026 (8/10 release) | Slipped to 2027 (10/14); stage 2 shipped (10/26); Cantor: Q2 2027 (10/27) | **weakening** (stabilising) |
| Space Systems-led growth | > 50% y/y | Q2 +62% (8/10); Q3 guide $250–265M | stable |
| Gross margin holds | GAAP ≥ 33% | Q3 guide 29–31% (vs 36.1%) | **weakening** |
| Backlog grows | > $2.36B | $2.36B at Q2; Q3 due 11/9 | improving (untested) |
| Dilution slows | no new ATM | ≈ $2.7B ATM since 1/2025; shares +10% in 7 months (10/15 entry) | **weakening** |

- **Thesis-break (if ever held):** a second Neutron slip past mid-2027; a new ATM or raise below $60; a Q4 revenue guide-down.
- **Conviction:** Low. A close above the 200-DMA with Neutron on its Q2 2027 path would lift it.

### What would make me wrong
- **A short squeeze.** 8.3% of float is short and retail is engaged. A strong 11/9 print could run it +20–30% without ever
  offering a 2:1 entry. That is acceptable: it is a speculative-slot name.
- **The $49.25 base breaks**, especially after the report. Then the 52-week low of $37.57 is the next reference.
- **Another Neutron slip or a fresh ATM.** Either is a thesis break.

### Sources
- levels.py (Yahoo chart API daily bars; Alpha Vantage calendar), run 2026-10-28, quotes 10:52 ET; zone checks the same
  session; reaction history computed from the same bars
- [Rocket Lab Q2 2026 results, 8-K ex. 99.1](https://www.sec.gov/Archives/edgar/data/0001819994/000181999426000061/rklb-08102026ex991.htm): 2026-08-10
- [StockTitan: Rocket Lab sets Nov. 9 date for Q3 2026 results](https://www.stocktitan.net/news/RKLB/rocket-lab-announces-date-of-third-quarter-2026-financial-61vtha3ophyg.html): PR 2026-10-20
- [MarketBeat: Rocket Lab shares climb 8.3%](https://www.marketbeat.com/instant-alerts/price-rocket-lab-nasdaq-rklb-shares-climb-83-heres-why-2026-10-27/): 2026-10-27
- [Yahoo/Stocktwits: Neutron's second stage heads to launch site](https://finance.yahoo.com/markets/stocks/articles/rklb-stock-edges-overnight-neutron-035945858.html): 2026-10-27
- [OptionSlam: RKLB earnings straddle](https://www.optionslam.com/earnings/straddle/RKLB): fetched 2026-10-28
- [MarketBeat: RKLB short interest](https://www.marketbeat.com/stocks/NASDAQ/RKLB/short-interest/): 10/15 record
- [MarketBeat: RKLB Q3 2026 estimates](https://www.marketbeat.com/earnings/reports/2026-11-9-rocketlab-stock/): via search, 10/28

---

## RKLB — update 2026-10-19

**Verdict:** WATCH, no setup · speculative slot only · **Conviction:** Low. The 10/15 setup conditions are not met: no higher
low has formed and it has not closed back above **$59.18**. RSI is under 30 with all three averages falling.

| | |
|---|---|
| Price | **$51.89** (2026-10-19, 10:35 ET, +2.1%); close $50.84 (10/16); 10/15 low **$49.69** |
| 20 / 50 / 200-DMA | $67.5 / $68.6 / $81.2 — all falling; price −24% under the 50, −36% under the 200 |
| RSI(14) · ATR(14) | **27.8** · $4.19 = **8.1% a day** · −66% from the 5/27 high of $151 |
| Setup that would qualify | a higher low above $49.69 **and** a close above $59.18; stop under the higher low, within 12%; ≤ 6% of the sleeve at cost |
| Report | ≈ 11/10 (not confirmed) |

**News (dated):** 10/14 — Neutron's first launch slips from Q4 2026 to 2027 (a forward propellant dome on the stage-1 tank).
Management ties cash-flow breakeven to Neutron's first successful launch. Target cuts 10/14–10/16: KeyBanc $135 → $100,
Citizens $130 → $90, Clear Street $129 → $105, Goldman $75 → $67; Cantor $122 and Needham $120 kept; average ≈ $104.
Q2 backlog was a record $2.36B. Funding: a $1B ATM (March 2026) after an earlier $750M one; no October raise found, but a
Neutron slip makes one more likely. The Iridium deal is still pending (closing reportedly mid-2027; unverified).

**Sources:** Yahoo chart API RKLB 1y daily, fetched 2026-10-19 10:35 ET · [Tiger, 10/15: Neutron delay](https://www.itiger.com/news/1119004903) · [Yahoo Finance: Neutron delay](https://finance.yahoo.com/markets/stocks/articles/rocket-labs-neutron-delay-leaves-160500684.html) · [TipRanks: analysts after the delay](https://tipranks.com/news/rocket-lab-stock-rklb-falls-on-neutron-launch-delay-heres-what-analysts-expect-next) · [Investing.com: KeyBanc cut](https://www.investing.com/news/analyst-ratings/keybanc-cuts-rocket-lab-stock-price-target-on-neutron-delay-93CH-4951940) · [Investing.com: Citizens cut](https://www.investing.com/news/analyst-ratings/citizens-cuts-rocket-lab-stock-price-target-on-neutron-delay-to-2027-93CH-4953465).

---

## RKLB — Rocket Lab — deep dive 2026-10-15

**Verdict:** WATCH, no setup · **Conviction:** Low. A falling knife on fresh bad news (Neutron slips to 2027), at ≈ 40×
sales, funded by constant share sales. It would only ever fit the speculative slot (≤ 6% at cost, stop ≤ 12% under the
entry), and no level gives that today.

| | |
|---|---|
| Price | **$53.01** (2026-10-15, 11:35 ET, −10.4%); range today $49.69–55.21; close $59.18 (10/14, −7.9%) |
| 20 / 50 / 200-DMA | $68.95 / $69.68 / **$81.34** — price 24% under the 50 and 35% under the 200 |
| 52-wk high / low | $151.00 (2026-05-27) / $37.57 (2025-11-21) · **−65% from the high** |
| RSI(14) · ATR(14) | **27.3** (oversold) · $4.31 = **8.1% a day** |
| Entry | **none today.** Re-check after Q3 earnings (≈ 11/10, unconfirmed) |
| What would make it a setup | a higher low above today's $49.69 **and** a close back above $59.18 (the 10/14 close / 7/29 low $58.20); stop under the higher low, within 12% |
| Size if it ever qualifies | speculative slot: ≤ 6% at cost (≈ $200) |

## Business
- **Revenue:** Q2'26 **$234.1M, +62%**. Growth is all Space Systems ($189.5M); Launch is flat (−4%). TTM ≈ $769M.
- **Guidance:** Q3 guide $250–265M, but the gross margin is guided **down** to 29–31% GAAP (36.1% in Q2), and adjusted
  EBITDA worsens to −$17–23M.
- **Backlog:** **$2.36B** (+137%). Contracts: SDA Tracking Layer $816M, Space Force SB-AMTI $397M (Neutron-dependent),
  suborbital $266M.
- **Cash and dilution:** free cash flow ≈ −$187M in H1'26. Cash and securities $2.39B. **ATM share sales ≈ $2.7B since
  January 2025**; common shares 543.6M → 598.4M in seven months (+10%).
- **Iridium:** ≈ $8B deal (6/28), $27 cash + $27 RKLB stock per share, a $3.6B bridge loan, closing in 2027. The collar's
  $67.50 floor is now above the price.
- **Valuation:** market cap ≈ $33.9B (including the preferred), EV ≈ $31.5B ≈ **41× trailing sales**.

## News
- **10/14 after the close: Neutron's first launch slips from Q4 2026 into 2027.** Voids were found in the composite dome of
  the Stage 1 tank; it must be rebuilt, inspected and tested through Q1'27. This is the **fifth slip** (2024 → mid-2025 →
  H2 2025 → 2026 → Q4 2026 → 2027).
- 10/15: KeyBanc cut its target $135 → $100 (Overweight). TD Cowen ($90), Cantor ($122) and Roth ($110) kept Buy ratings.
  Consensus is Moderate Buy, average $104 (range $60–150).
- The space group fell together: ASTS −25%, Planet −19%, Firefly −16% over 5 sessions.
- The CFO sold ≈ $9.9M on 10/1 and ≈ $8.8M on 9/2 (10b5-1 plans). There were no insider buys.
- Short interest 44.4M = ≈ 7.4% of shares (9/30). 2× ETFs exist (RKLX, RKLZ).

## Levels
- **Support:** $49.69 (10/15 low) · $47.7–49.2 (December 2025 lows) · ≈ $45 (November 2025 base) · $37.6–40.0 (52-week low).
- **Resistance:** $55.2 · **$58.2–59.2** (7/29 low, 10/14 close) · $60.5–61.5 (broken September lows) · $64–66 ·
  $69–70 (20/50-DMA) · $81.3 (200-DMA).
- Earnings reactions: −1.3% / −4.9% / **+34.2%** / 0.0%.

## Why not now
1. **Bad news on the day.** The thesis event (Neutron) just broke again. Plan §4: a headline that questions the thesis
   locks entries until the next hard data point (Q3 earnings).
2. **No defined risk.** Below $49.69 the next real floor is $45–47.7, then $37.6. A stop within the speculative slot's 12%
   would sit inside one or two days of normal noise (ATR 8%).
3. **Supply of shares.** Rocket Lab sells stock steadily, and the Iridium deal needs > $3B of cash. Rallies tend to meet
   new share sales.
4. **The account:** about $77 above the circuit breaker, and the October buy budget is already spoken for (AMD, MU).

## What would make me wrong
A quick Neutron test success, a large funded contract, or a Q3 beat with the margin holding could reverse the slide the way
Q1 did (+34% in a day). That is the risk of waiting. The cost of guessing early is the next leg to $45 or $38.

## Sources
- Yahoo chart API RKLB 2y daily bars, fetched 2026-10-15 11:35 ET
- Q2'26 8-K https://www.sec.gov/Archives/edgar/data/0001819994/000181999426000061/rklb-08102026ex991.htm · 10-Q https://www.sec.gov/Archives/edgar/data/0001819994/000181999426000062/rklb-20260630.htm
- https://finance.yahoo.com/markets/stocks/articles/rocket-lab-shares-slide-15-102958258.html — 2026-10-15
- https://aviationweek.com/space/operations-safety/rocket-lab-tank-design-flaw-formally-pushes-neutron-debut-2027
- https://ng.investing.com/news/stock-market-news/keybanc-cuts-rocket-lab-stock-price-target-on-neutron-delay-93CH-2738649 — 2026-10-15
- https://www.marketbeat.com/stocks/NASDAQ/RKLB/forecast/ — 2026-10-15 · https://equibles.com/stocks/rklb/shortinterest — 9/30
- https://www.datacenterdynamics.com/en/news/launcher-rocket-lab-acquires-satellite-operator-iridium-in-8bn-deal/
