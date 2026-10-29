# AMD — Advanced Micro Devices — research log

One file per ticker; newest entry first. Each entry is dated; numbers are as of that date.

Entries:
- 2026-10-28 (deep dive + 11/3 earnings preview + thesis scorecard)
- 2026-10-19 (update)
- 2026-10-16 (position opened 10/15)

---

## AMD — Advanced Micro Devices — deep dive 2026-10-28

**Verdict:** HOLD with the $498 stop · no adds · **apply the 11/2 rule below** · **Conviction:** Med. The business is
beating: Data Center +107% in Q2, and Helios racks are now installed at Meta. The position is not: from here it pays
**0.94:1** to the sell zone, the report is a ±9.7% coin, and the account is $24 above its circuit breaker.

| | |
|---|---|
| Price (date) | **$565.87** (levels.py, 2026-10-28 11:07 ET); close $560.26 (10/27, +5.45%) |
| Entry zone | **None.** Adds are blocked: the line is 15.0% of the sleeve, at the cap. The §6b zone $530–541 also fails levels.py (below) |
| Invalidation (stop) | **$498** broker stop: 12.0% / 2.59 ATR below, under the 7/8 swing low $498.15 and the 10/22 low $502.60 · event: any thesis-break exit in the scorecard |
| Target 1 / 2 | Sell zone **$630–658** (⅓ = 0.30 sh) / ladder +25% $683.17 (stop to breakeven), +40% $765.16 (sell ⅓) |
| Reward/risk (T1) | **0.94:1** from $565.87 to $630 (levels.py). This is a hold, not a buy |
| Size | 0.91477917 sh ≈ **$518 = 15.0%** of $3,426 (cap 15%) |
| Timeframe | Quarters |
| Next earnings | **Tue 11/3 after the close** (AMD IR, 10/6; levels.py: 4 sessions). Buy blackout 10/29–11/3. **Decision session: Mon 11/2** |

**What changed since 10/19** ($546.93 then):
- **10/22:** −8.1% to $507.93 in the SOX −6.7% day (Meta FCF/capex, Lam supply warning). The low of $502.60 was $4.60 above
  the stop. The circuit breaker fired on that close, and the halving (0.4574 sh) was skipped, an OVERRIDE (journal 10/27).
- **10/27:** +5.45% to $560.26. AMD said it will put **$1B into Meta's equity offering**, and that the first Helios racks are
  installed and being tested at Meta.
- **Moving averages:** the 20-DMA rolled over (607.0 → 578.7) while the 50-DMA kept rising (538.4 → 545.3). Price is back
  above the 50 and under the 20.
- **New in this entry:** the implied move (±9.7%), consensus (sources conflict), the last 4 reactions, a mechanical 11/2
  rule and a thesis scorecard.
- **Two plan items found:**
  1. The §6b buy zone $530–541 fails the 1.5-ATR stop rule at its low and mid.
  2. The note "AMD add ≤ $150 from 11/4" cannot be filled under the 15% cap (see Fundamentals → sizing).

### Thesis scorecard (earnings-and-thesis.md §B)
| Pillar (falsifiable) | What was expected | Status (dated) | Trend |
|---|---|---|---|
| Data Center revenue grows > 50% y/y | Management: server revenue > 80% y/y in H2 2026 | Q2: **$6.718B, +107%** (8-K, 8/4) | improving |
| Helios / MI450 ships on time | Initial shipments in Q3, ramp through Q4 into 2027 | 10/27: "installed and being tested" at Meta; broader deployment "in the near future", no date (AMD release) | stable, still unproven in revenue |
| Non-GAAP gross margin ≥ 55% through the ramp | ≈ 56% | Q2 56% · Q3 guide ≈ 56% (8/4) | stable |
| Guide at or above consensus | Q3 guide vs consensus | Q3 guide $13.0B vs $12.52B LSEG (8/4). The stock still fell 7.0% the next day | stable |
| Customer financing stays arm's-length, dilution contained | No circular funding; flat share count | $5B equity into Anthropic (7/22) · $1B into Meta's offering (10/27) · OpenAI and Meta warrants for up to 160M sh each at $0.01 (none vested at 6/27) · World Labs $8.2B in stock (9/28) | **weakening** |

- **Thesis-break exits (whatever the price):**
  1. A Q4 guide below Q3's actual revenue, or Helios volume pushed into 2027.
  2. Meta, OpenAI or Anthropic cuts or delays its gigawatt commitment.
  3. Non-GAAP gross margin guided below 54%.
- **Disconfirming evidence:**
  - A beat-and-raise on 8/4 still fell 7.0%.
  - Insiders: 31 sells and 0 buys in 3 months (Nasdaq).
  - AMD is now a buyer of its customers' equity.
  - The 10/22 low sat $4.60 above the stop.
- **Conviction: Med.** It goes to High if the Q4 guide quantifies Helios at or above consensus, and to Low on a Q4 guide below
  consensus.

### Earnings preview — Q3, Tue 11/3 after the close (priority deliverable)
1. **Date and time.** Tue **11/3 after the close**, call 5:00 pm ET (AMD IR release of 10/6). levels.py: "2026-11-03 after the
   close (4 sessions)". The last decision point is the **11/2 close**. Never decide on report night.
2. **Consensus (sources conflict):**
   - **MarketBeat** (fetched 10/28): EPS **$1.94**, revenue **$13.08B**. **Theta** (data as of 10/27): **$1.93 / $13.08B**.
   - **Zacks via Nasdaq** (10/28): **$1.68** (13 estimates, range $1.46–1.84). levels.py shows the same $1.68 from Alpha Vantage.
   - The $1.68 is barely above Q2's actual $1.66 on a guide 13% higher, so it is likely GAAP-basis or stale. ARM's
     equivalent ($0.22) matches Hudson Labs' GAAP consensus ($0.23). **Use $1.93–1.94 for the non-GAAP print.**
   - **Guide:** ≈ $13.0B ± $0.3B and ≈ 56% non-GAAP gross margin (8/4).
   - **Q4:** EPS consensus $2.29 (Zacks, basis unclear). Q4 revenue consensus is **unverified**: no dated source found.
   - **What moves the stock:** the Q4 guide; the first Helios/MI450 revenue and how it is ramping; Data Center revenue.
     Hyperscaler capex is a read-across: MSFT and GOOGL report 10/28 after the close, AMZN 10/29, AAPL 11/2 (StockTitan,
     10/26).
3. **Implied move: ±9.7%.** The Nov 6 at-the-money straddle (562.50 strike) was $28.15 call + $26.60 put = **$54.75** on a
   $563.39 price (Nasdaq option chain, 10/28 10:58 ET).
   - It includes ≈ 6 ordinary sessions; the Oct 30 straddle alone is ±4.4%. So the earnings gap priced is somewhat less
     than ±9.7%. The desk uses the full figure.
   - **Versus the stop:** the stop is **12.0%** away ($67.87). The implied range is **$510.87–620.87**. A move of that size
     reaches neither the stop nor the sell zone ($630, +11.3%). A move about **1.2×** the implied one reaches either. In 2
     of the last 4 reports the next close went that far: February down (−17.3%) and May up (+18.6%).
   - **Versus the size:** ±9.7% × $518 = **± $50** on the line, **twice the $24 cushion** over the breaker. Losses if the
     move goes against the line:

     | Case | Price | Loss vs now | Loss vs cost |
     |---|---|---|---|
     | Stop fills at $498 | $498 | **$62** | $44 |
     | A repeat of February's −17.3% | ≈ $468 | **$90** | — |
4. **Scenarios** (actions written now, 10/28):

   | Scenario | What has to happen | Likely reaction | Action written now |
   |---|---|---|---|
   | Bull | Q3 ≥ $13.3B (top of the guide), gross margin ≥ 56%, a Q4 guide clearly above consensus that puts a number on Helios | +10% to +19% (May analog +18.6%) → $620–670 | Alert at **$630**. At ≥ $630, sell **0.30 sh** (⅓) by hand on 11/4, never on the night. Keep the rest on the 498 stop until a close ≥ $683.17, then move the stop to $546.54 |
   | Base | In line, Q4 guide ≈ consensus, Helios "on track" with no numbers (the 8/4 pattern) | −7% to +5% → $525–595 | Hold with the 498 stop. No add (cap). Levels re-derived 11/4 from the new bars |
   | Bear | Q3 miss or Q4 guide below consensus, Helios slips, gross margin < 55%, or the financing loop questioned | −11% to −18% (February analog) → $465–505 | **The stop decides.** If it gaps under $498, the fill at the open is the result. No re-buy that session (§4a), no add for 2 sessions, re-entry only after a higher low with a new stop |
5. **History** (Yahoo daily bars via the levels.py cache; report-day close → next session):

   | Report (after the close) | Next open (gap) | Next close (close to close) |
   |---|---|---|
   | 2025-11-04 (Q3'25) | −2.7% | **+2.5%** |
   | 2026-02-03 (Q4'25) | −11.2% | **−17.3%** |
   | 2026-05-05 (Q1'26) | +15.3% | **+18.6%** |
   | 2026-08-04 (Q2'26) | −6.6% | **−7.0%** |

   The average absolute move was **11.4%**, above the ±9.7% priced. Two of four went past it, one each way (February and
   May). August was a beat-and-raise (EPS $1.66 vs $1.62; guide above consensus) and still fell 7.0%.
6. **Decision rule for Mon 11/2.** Read two numbers at 15:30 ET: AMD's price and the account value in the app.
   - **AMD ≥ $630** (the sell zone): **sell 0.30 sh (⅓)** under the §3 catalyst rule. The rest keeps the 498 stop.
   - **AMD $498–630 and the account ≥ $3,452** (the $3,401.87 breaker plus the ≈ $50 implied move on the line):
     **hold the full line through the report with the 498 stop.**
   - **AMD $498–630 and the account < $3,452:** **sell 0.4574 sh**, the circuit-breaker half still owed since 10/22. Hold the
     rest with the 498 stop. This halves the $ at stake to ≈ ±$25.

   The rule only applies the desk's position of 10/27 (the halving is owed) mechanically. It is not a forecast. On today's
   numbers ($3,426) the third branch applies.
   **levels.py quirk for 11/2:** its ET is hard-coded as UTC−4. After DST ends on 11/1, its quote times read one hour
   late, so check the app clock.

### Thesis
AMD is the second source of AI accelerators and the share gainer in server CPUs. It has signed gigawatt-scale GPU
commitments with OpenAI and Meta, and up to 2 GW of MI450 with Anthropic (7/22). Agentic AI is pulling server-CPU demand up
on top of that. The market already prices much of it: ≈ 40× FY27 consensus EPS and ≈ $915B of market cap (10/27).

What is under-weighted is the **funding loop**. Two customers hold warrants for up to 160M AMD shares each. AMD is buying
equity in Anthropic ($5B) and now Meta ($1B), while those customers raise equity to pay for capex: Meta priced a $25B
common offering plus a mandatory convertible, settling 10/29 (Meta FWP). Q3–Q4 is the first test of Helios in revenue.

### Chart & technicals (levels.py, 2026-10-28 11:07 ET)
```
AMD  $565.87 (2026-10-28 11:07 ET); last daily bar 2026-10-28 close $565.87
  20/50/200-DMA  578.73 / 545.33 (rising) / 407.29 (rising)   price vs 50 +3.8%, vs 200 +38.9%
  RSI(14) 51.1   ATR(14) $26.25 = 4.6% a day   52-wk 188.22–658.52 (-14% from the high)
  Trend: above a rising 200-DMA
  Chase guard: ok
  Next report: 2026-11-03 after the close (4 sessions; EPS est. 1.68)   ✓ outside the buy blackout
  Swing support below: 498.15, 495.35, 463.21   resistance above: 574.20, 584.73, 658.52
```
- **Structure.** Lower highs from the 10/6 high of $658.52 ($606.20 on 10/13, $556.79 on 10/21). Since the 10/22 low of
  $502.60 the lows are higher ($508.36, $514.01, $538.50). Today's high of $573.96 stalled at the 7/14 pivot of $574.20, under
  the 20-DMA.
  - Overhead: $574.2 / $578.7 (20-DMA) / $584.7 / $591.9–606.2 (the 10/13–10/14 highs; not levels.py pivots) / $630.8–639
    (9/24–9/25) / $658.5.
- **Volume.** The 10/22 drop came on 28.0M shares. The 10/27 rally came on 20.5M, about average (30-day 21.3M per Gotrade).
  The bounce is not a conviction move yet.
- **"Buy blackout ✓" is not a buy signal.** levels.py does not know about FOMC day (today), the client's no-trade commitment
  to 11/2, or the 15% cap.
- **Zone checks** (`levels.py AMD --zone … --stop 498 --size … --sleeve 3426`, run 11:06–11:10 ET; ATR $26.25 in both runs):
```
  Setup: zone 530.00–541.00, stop 498.00, T1 562.99          # §6b buy zone, T1 = nearest real resistance
    at low     530.00: R/R 1.03:1, stop 1.22 ATR (6.0%)   ✘ R/R < 2; stop < 1.5 ATR
    at mid     535.50: R/R 0.73:1, stop 1.43 ATR (7.0%)   ✘ R/R < 2; stop < 1.5 ATR
    at high    541.00: R/R 0.51:1, stop 1.64 ATR (7.9%)   ✘ R/R < 2
  Setup: zone 530.00–541.00, stop 498.00, T1 630.00          # same zone, T1 = sell-zone bottom
    at low     530.00: R/R 3.12:1, stop 1.22 ATR (6.0%)   ✘ stop < 1.5 ATR
    at mid     535.50: R/R 2.52:1, stop 1.43 ATR (7.0%)   ✘ stop < 1.5 ATR
    at high    541.00: R/R 2.07:1, stop 1.64 ATR (7.9%)   ✓
  Setup: zone 565.87–565.87, stop 498.00, T1 630.00          # holding from here
    at mid     565.87: R/R 0.94:1, stop 2.59 ATR (12.0%)   ✘ R/R < 2
    size $518 ≈ 0.9154 sh at the mid; risk to stop $62.13 = 1.8% of $3,426   ✓ ≤ 2%
```
  **No passing AMD buy zone.** The §6b zone fails at its low and mid with either T1, so it should come off the Flag Board. A
  post-report add zone is written from 11/4 bars only.
- Chart: `/tmp/claude-1000/-home-waelas-wael-amana-amana-assistant/cf7235bd-03e5-456e-8948-a8c2229a57bd/scratchpad/charts/AMD.png`
  (stop 498, T1 630). Visual check: price is back over the rising 50-DMA, the 20-DMA has rolled over, and the RSI has
  recovered from ≈ 35 to 51.

### Fundamentals
- **Q2 2026** (8-K, 8/4):
  - Revenue **$11.536B, +50%**. Non-GAAP gross margin 56% (GAAP 54%). Non-GAAP EPS **$1.66** (GAAP $1.38) vs $1.62 consensus.
  - Segments: Data Center **$6.718B (+107%)** · Client $3.062B (+23%) · Gaming $779M (−31%) · Embedded $977M (+19%).
  - FCF **$1.558B** (14% margin). Cash and short-term investments **$13.11B**, total debt **$3.23B**: net cash.
- **Q3 guide:** ≈ $13.0B ± $0.3B (≈ +41% y/y, +13% q/q), ≈ 56% non-GAAP gross margin.
  - After the print the stock fell 9% after hours. Futurum's Daniel Newman: the market "wanted a blowout guide driven by
    Helios". Others pointed to higher capex (implicator.ai, 8/5).
- **Valuation:** ≈ 87× FY26 / **40×** FY27 consensus EPS ($6.50 / $14.14, Zacks via Nasdaq 10/28; basis unclear). Market cap
  ≈ $914.6B at $560.26 (Gotrade, 10/27). The story is priced. The stock needs Helios numbers, not adjectives.
- **Dilution items** (reported, dated above): the World Labs all-stock deal of ≈ $8.2B is ≈ 14.5M shares at today's price
  (desk arithmetic). Vesting terms of the OpenAI and Meta warrants are **unverified** this session.
- **Sizing under the cap** (desk arithmetic, sleeve $3,426, 10:52 ET):
  - At $565.87 there is **$0** of room under 15%. A $50 add fits only at **≤ $497**, which is under the stop.
  - With the $200 November contribution deposited, $50 fits at ≤ $536 and $150 at ≤ $407.
  - **So the PLAN note "AMD add ≤ $150 from 11/4" cannot be done above the stop.** Only the halving, a sleeve rise or a
    contribution reopens room.

### News & catalysts (last 30d / next 90d)
- 9/28 — AMD to buy World Labs for ≈ $8.2B in stock; closing expected by end-2026 — **neutral** (dilution; no product link)
- 10/15 — EVP Forrest Norrod sold 17,262 sh at $535.15 (automatic plan sale; Nasdaq Form 4 table) — **neutral**
- 10/22 — −8.1% with the SOX (−6.7%): Meta FCF/capex and Lam's supply warning. Nothing AMD-specific — **neutral** (sector)
- 10/27 — AMD release, 9:20 ET: $1B into Meta's equity offering; first Helios racks installed and in test at Meta; EPYC
  behind Meta's Muse agent. The stock rose +5.45% — **confirming** on Helios, **caution** on the financing loop
- 10/27 — GF Securities raised its target to $720 (GuruFocus). Its analyst Jeff Pu also cautioned that current-quarter
  forecasts may fall short (Gotrade) — **neutral**
- **Next:** FOMC today 2:00 pm ET · MSFT and GOOGL 10/28 after the close · AMZN and PCE 10/29 · Meta offering settles 10/29 ·
  AAPL 11/2 · **AMD 11/3 after the close** · ANET 11/3 · ARM 11/4 · World Labs close by year-end

### Positioning & sentiment
- **Short interest:** 38.1M shares (10/15) vs 39.3M (9/30); 1.98 days to cover (Nasdaq). No squeeze fuel, no crowded short.
- **Insiders:** 31 sells and **0 open-market buys** in 3 months; net −711k shares (Nasdaq).
- **Analysts:** 29 Buy / 6 Hold / 0 Sell; mean target **$664.31** (range $465–1,250) (Nasdaq, 10/28). MarketBeat's mean is
  $606.76.
- **Crowding:** a crowded AI trade. The SOX is −21% from its high and under its 50-DMA (desk, 10/28). That is the setup
  protocol §4 warns about: crowded, a report in 4 sessions, and an account with no cushion.

### What would make me wrong
- **Price:** a close under $527 (the September breakout) weakens the line. **$498 is the exit**, and a gap through it fills
  lower.
- **Events:** a Q4 guide below consensus or Helios slipping to 2027. A hyperscaler capex cut in this week's prints
  (MSFT, GOOGL, AMZN). Gross margin guided under 54%.
- **Against my caution:** if Q4 is guided well above consensus with Helios dollars, the "sell half" branch costs upside. The
  sell zone and the +25% ratchet still capture the bulk.

### Sources
- `levels.py AMD` (Yahoo chart API daily bars; Alpha Vantage earnings calendar), runs 2026-10-28 10:52–11:10 ET; chart PNG
  above
- Nasdaq option chain, AMD Nov 6 and Oct 30 expiries, 10/28 10:58 ET — https://api.nasdaq.com/api/quote/AMD/option-chain
- Nasdaq earnings-forecast / earnings-date / targetprice / ratings / short-interest / insider-trades APIs for AMD, fetched
  10/28 — https://api.nasdaq.com/api/analyst/AMD/earnings-forecast
- [AMD Q2 2026 results, 8-K exhibit 99.1](https://www.sec.gov/Archives/edgar/data/0000002488/000000248826000121/q22026991.htm) — 2026-08-04
- [AMD to report fiscal Q3 2026 results](https://ir.amd.com/news-events/press-releases/detail/1300/amd-to-report-fiscal-third-quarter-2026-financial-results) — 2026-10-06
- [MarketBeat: AMD Q3 2026 estimates](https://www.marketbeat.com/earnings/reports/2026-11-3-advanced-micro-devices-inc-stock/) — fetched 2026-10-28
- [Theta: AMD Q3 FY2026](https://www.theta.md/earnings/amd/q3-2026) — data as of 2026-10-27
- [Hudson Labs: AMD Q3 2026 preview](https://www.hudson-labs.com/research/amd-q3-2026-earnings-preview-revenue-guidance-key-drivers) — 2026-10-07 (internal inconsistencies noted; used only for the guide)
- [implicator.ai: Data Center +107%, shares slide after hours](https://www.implicator.ai/amd-data-center-sales-jump-107-to-6-7-billion-as-shares-slide-after-hours/) — 2026-08-05
- [AMD and Meta advance strategic partnership (release via StockTitan)](https://www.stocktitan.net/news/AMD/amd-and-meta-advance-strategic-partnership-to-power-meta-s-w7j6r9jk2soy.html) — 2026-10-27 09:20 ET
- [Gotrade: AMD rises 5.5% to $560.26](https://www.heygotrade.com/en/news/amd-amd-stock-news-october-28-2026/) — 2026-10-28
- [GuruFocus: GF Securities target $720](https://www.gurufocus.com/news/9144486/amd-shares-rise-15-premarket-after-gf-securities-raises-price-target-to-720) — 2026-10-27
- [Axios: AMD to acquire World Labs for $8.2B in stock](https://www.axios.com/pro/all-deals/2026/09/28/amd-world-labs-ai-8-billion) — 2026-09-28
- [AMD and Anthropic: up to 2 GW of MI450](https://ir.amd.com/news-events/press-releases/detail/1292) — 2026-07-22
- [Meta pricing term sheet (FWP)](https://www.sec.gov/Archives/edgar/data/0001326801/000119312526432549/d382225dfwp.htm) — October 2026
- [StockTitan: earnings calendar, week of Oct 26](https://www.stocktitan.net/articles/earnings-calendar-week-of-october-26-2026) — 2026-10-23, updated 10-26

---

## AMD — update 2026-10-19

**Verdict:** HOLD with the $498 stop · no adds (15% cap) · **Conviction:** Med. Nothing company-specific since 10/16. The
10/16 drop was the sector (8th straight SOX down day; 24/7 Wall St tied part of it to the Qualcomm–Arm verdict), and
10/19 is a sector bounce. The 50-DMA held on a close.

| | |
|---|---|
| Price | **$546.93** (2026-10-19, 10:35 ET, +3.4%); close $528.75 (10/16, −6.0%); 10/16 low **$526.83**, just under the $527 September breakout, but the close held above it |
| 20 / 50 / 200-DMA | $607.0 / **$538.4** (rising) / $395.9 — price +1.6% over the 50, −9.9% under the 20 |
| RSI(14) · ATR(14) | 42.8 · **$27.10 = 5.0% a day** · −16.9% from the 10/6 high of $658.52 |
| Stop | **$498** (broker, confirmed live 10/19): 8.9% below, 1.8 ATR. Risk ≈ $45 = 1.3% of the sleeve |
| Sell zone (⅓) | **$630–658** → 0.30 sh. R/R from today: **1.7:1** to $630 |
| Weight | 14.5% of the sleeve → adds blocked (15% cap) |
| Next earnings | **Tue 11/3** after the close (confirmed 10/14). Buy blackout 10/29–11/3. Decide 11/2: hold through with the stop, or sell ⅓ only if in $630–658 |

**What changed:** nothing in the thesis. The open question is still hyperscaler funding (CoreWeave bonds at 15%, the
Broadcom CEO's "casino" remark 10/12). TSMC's 10/15 print and Q4 guide argue demand is intact. A close under **$527**
would mean the breakout retest failed; the stop at $498 stays the hard line.

**Sources:** Yahoo chart API AMD 1y daily, fetched 2026-10-19 10:35 ET · [24/7 Wall St, 10/16: Arm and AMD fall 5% as Qualcomm verdict adds to chip selloff](https://247wallst.com/investing/2026/10/16/arm-and-amd-fall-5-as-qualcomm-verdict-adds-to-chip-selloff-taiwan-semiconductor-slips) · [simpletechtrend, wk 42: optical sell-off is funding, not supply](https://www.simpletechtrend.com/en/post/optical-selloff-funding-vs-supply-2026-w42-en) · news sweep 10/19 found no AMD-specific item since 10/10.

---

## AMD — position card 2026-10-16

**Verdict:** HOLD with the stop · **Conviction:** Med. Bought 10/15 at $546.54 for $499.96 (0.91477917 sh), at 11:29 ET
and 2.5× the size the desk proposed. Zone and stop come from the 10/14 desk note (`journal/2026-10-14-check.md`). The full
research-protocol deep dive is still owed and is due before the 11/2 pre-report decision.

| | |
|---|---|
| Price | **$544.97** (2026-10-16, 09:44 ET); close $562.23 (10/15); 10/15 low **$530.09** |
| 20 / 50 / 200-DMA | $611.2 / **$537.5** (rising) / $394.3 — price 1.4% over the 50-DMA, 10.8% under the 20 |
| 52-wk high · RSI(14) · ATR(14) | $658.52 · 40.8 · **$26.28 = 4.8% a day** |
| Stop | **$498**, under the September breakout (> $527) and the 50-DMA. That is −8.9% from cost and 1.8 ATR. Risk ≈ $43 = 1.2% of the sleeve |
| Sell zone (⅓) | **$630–658** (the September highs up to the 52-week high) → ⅓ = 0.30 sh |
| Reward/risk at the fill | **1.7:1 to $630**, 2.3:1 to $658. The 2:1 zone top is **$541**, not $545 (desk error in the 10/14 zone) |
| Ladder | +25% $683.17 (stop to breakeven) · +40% $765.16 (sell ⅓) · +75% $956.44 · hard exit −15% $464.56 (the stop is above it) |
| Adds | **Blocked.** At 14.3% of the sleeve, a $150 add would pass the 15% cap |
| Next earnings | **Tue 11/3** after the close (confirmed). Blackout for buys 10/29–11/3. Decide on 11/2: hold through with the stop, or sell ⅓ if it is in the sell zone |

## Why it held on 10/15
TSMC's Q3 (10/15): revenue **$46.72B, +41.2%**, above its $44.6–45.8B guide; gross margin 66.4%; Q4 guide **$52.3–54.3B**.
On the same morning AMD tested the 10/15 low of $530.09 and closed at $562.23. The chip sell-off (10/9–10/15) was sector-wide
and came with no AMD-specific news (journal 10/14–10/15).

## What would make me wrong
- A close under $527 (the September breakout): the retest failed. The $498 stop is the hard line.
- A hyperscaler capex cut, or a Q3 print on 11/3 with an MI-series data-center guide below what the market expects.
- Another sector-wide de-rating day (10/14: AMD −5.7%). The account is $73 above its circuit breaker, so AMD is the line
  that moves the account most.

## Sources
- Yahoo chart API AMD 1y daily and 5-day 5-min bars, fetched 2026-10-16 09:44 ET (fill check: the 11:30 ET bar on 10/15 was
  544.84–547.20)
- TSMC Q3'26 6-K https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000726/a3q26e_withguidancexfinal.htm — 2026-10-15
- Amana statement 2026-10-15 (`portfolio/statements/amana-statement-2026-10-15_2026-10-15.pdf`)
