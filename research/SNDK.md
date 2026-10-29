# SNDK — Sandisk Corp — research log

One file per ticker; newest entry first. Each entry is dated; numbers are as of that date.

Entries:
- 2026-10-28 (deep dive + earnings preview; not held; in blackout)
- 2026-10-19 (update)
- 2026-10-14 (check)
- 2026-10-13

---

## SNDK — Sandisk Corp — deep dive 2026-10-28

**Verdict:** WATCH. It reports tomorrow (10/29, after the close), so it is inside the 3-session blackout. No zone passes before
the print. Re-derive from the post-report bars on 11/2. · **Conviction:** Med on the business, Low on the setup. **Third** for the
single memory slot, behind MU and EWY. SNDK carries a 6.7% ATR, sits 13% under a falling 50-DMA, and faces a consensus that
already sits above the top of its own guidance.

| | |
|---|---|
| Price | **$1,360.78** (2026-10-28 10:52 ET, `levels.py`). +4.3% on the 10/27 close of $1,304.84; +10.7% off the 10/23 low of $1,228.89 |
| Entry zone | **None passes** (checks below). None can be written before the print, because the report resets ATR and structure |
| Invalidation (stop) | For any future buy: under the post-report low. Event: gross margin < 83% or a FQ2 guide flat or down q/q |
| Target 1 / 2 | $1,446.62 (8/4 swing high) / $1,600 (5/11 high; 50-DMA 1,570.80). Fundamental: mean target $2,144 (S&P via stockanalysis, 10/26) |
| Reward/risk (T1) | ✘ 0.78–1.48:1 across the candidate zones |
| Size | $0. When a zone passes: ≈ $190–250, risk ≤ $68 |
| Timeframe | months |
| Next earnings | **2026-10-29 after the close** (`levels.py`: 1 session, ✘ blackout). Call 4:30 pm ET (FinanceFeeds 10/24: 1:30 pm PT) |

### What changed since the 10/19 entry
- The fall did not end on 10/19. It made a **lower low at $1,228.89** (10/23) on top of the 200-DMA (≈ 1,250), then bounced
  10.7%. §4a: a close above the broken level ($1,310 stop) would count. The 10/27 close of $1,304.84 fell short; today's close is
  pending. There is no higher low yet.
- The 50-DMA turned from rising ($1,596.6 on 10/19) to **falling ($1,570.80)**. ATR eased from $98 to $90.55.
- **The bar went up.** Consensus EPS rose to $46.22–46.67 against a guide of $44–46. Wedbush lifted its FQ1 numbers to
  $11.45B / $49.04 (10/26).
- **The options price less.** The ATM straddle implies ≈ ±8.4% today, against ±11–13% on 10/13–10/19.
- MU is no longer held, so the "one memory name" block on SNDK has lifted. SNDK still ranks behind MU and EWY.

### Earnings preview, 10/29 after the close (section A)
1. **Date and time:** Thu 2026-10-29 after the close (`levels.py` / Alpha Vantage; stockanalysis "confirmed"). 10/29 is a PCE
   morning and 10/28 is FOMC day, so for this account the last decision point was before today. Nothing is held, so nothing has
   to be decided.
2. **Consensus:** revenue **$10.64B** (TradingKey 10/28) / $10.72B (TipRanks 10/28); EPS **$45.22** (Alpha Vantage via `levels.py`)
   / $46.22 (TradingKey) / $46.67 (TipRanks). Company guide (8-K 8/5): revenue $10.30–10.80B, non-GAAP gross margin **83–85%**,
   EPS $44–46. The metrics that move the stock: gross margin, data-center revenue (≈ ⅓ of revenue in FQ4), and the **FQ2 guide**
   (FinanceFeeds 10/24).
3. **Implied move:** Oct-30 ATM $1,360 straddle, call 57.90/58.70 + put 56.40/57.20 ≈ **$115 ≈ ±8.4%** (Nasdaq option chain,
   10/28 11:00 ET, last $1,362.83). Implied band ≈ $1,248–1,478. That band contains both the 200-DMA (1,250) and the first
   resistance (1,446.62). Other reads: Optionslam weekly 9.31% (undated), TipRanks 12.1% (10/23), Earnings-Watcher 13.7% (10/16).
   **Stop distance and $ at stake:** not held, so $0.
4. **Scenarios:**

   | Scenario | What has to happen | Likely reaction | Action written now |
   |---|---|---|---|
   | Bull | Revenue ≥ $11B, gross margin ≥ 85%, FQ2 guide midpoint ≥ +15% q/q | gap +10–15% into 1,446.62–1,600 | No chase. From 11/2, re-derive. A gap into a falling 50-DMA is resistance, not a zone |
   | Base | Revenue $10.6–10.8B, gross margin 83–85%, FQ2 guide +5–15% q/q | ± the implied ≈ 8% | Nothing. Re-run `levels.py` 11/2 and look for a higher low above 1,228.89 |
   | Bear | Gross margin < 83% **or** FQ2 guide flat or down q/q | gap −10–15% under the 200-DMA toward 1,100 / 998.19 | No buy. Pillar 1 or 2 breaks, and SNDK drops off the memory ranking until the next print |
5. **History** (Yahoo daily bars via `levels.py`, report-day close to next session):

   | Report | Opening gap | Close-to-close |
   |---|---|---|
   | 2025-11-06 AMC | +0.4% | **+15.3%** |
   | 2026-01-29 AMC | +20.8% | +6.9% |
   | 2026-04-30 AMC | −3.4% | +8.3% |
   | 2026-08-05 AMC | **−13.1%** | −6.8% (it beat by 16.7%) |

   Three of four closed up. The last one gapped −13% on a beat.
6. **Decision (written 10/28, the session before):** not held, so no hold, trim or exit decision. **No buy on 10/29 or 10/30**
   (blackout, PCE morning, and the client's no-trade commitment to 11/2). The earliest new decision is 11/2, on post-report levels.

### Thesis scorecard (section B)
| Pillar (falsifiable) | Expected | Status (dated) | Trend |
|---|---|---|---|
| Gross margin holds | ≥ 83% (guide 83–85%) | FQ4 84.6% (8-K 8/5). FQ1 prints 10/29 | stable; tested tomorrow |
| Sequential growth stops decelerating | FQ2 guide ≥ +10% q/q | +97% → +51% (FQ4) → +15–20% guided for FQ1 | **weakening** |
| NAND contract prices rise | +15–20% in 4Q26 | TrendForce 9/30: NAND +15–20%. Enterprise SSD is the only accelerating category; client SSD and eMMC/UFS are soft | stable |
| Data center becomes the core | DC ≥ ⅓ of revenue | FQ4 DC $2.98B, +103% q/q = 33% of revenue (8-K 8/5) | improving |
| Balance sheet / returns | net cash, buyback | Cash $4.76B, no long-term debt (7/3). $15.5B authorization (8-K 8/5). Shares **+6.90% y/y** (stockanalysis 10/28) | stable; dilution noted |

- **Thesis-break exits:** gross margin < 83%; a FQ2 guide down q/q; a flat or negative 1Q27 NAND contract forecast.
- **Disconfirming evidence:** the consensus sits above the top of guidance (TradingKey 10/28). The last report gapped −13% on a
  16.7% beat. The SK hynix CFO sees 2027 NAND demand only +high-teens % and PC/mobile units falling (10/28).
- **Conviction: Med.** It goes Low on any of the break events. It rises if the FQ2 guide re-accelerates.

## Thesis
Sandisk is the purest listed NAND/enterprise-SSD name. Revenue is growing 4–5× y/y at 84% gross margins, with zero debt. AI
inference is pulling enterprise SSD demand, the one NAND category still accelerating (TrendForce 9/30). The market prices it at
6.3× FY27 EPS because it sees a cyclical peak. The stock peaked on 6/22 while estimates kept rising. Tomorrow's guide is the test.

## Chart & technicals
`levels.py SNDK`, quote 2026-10-28 10:52 ET:
```
SNDK  $1,360.78 (2026-10-28 10:52 ET); last daily bar 2026-10-28 close $1,360.78
  20/50/200-DMA  1,467.90 / 1,570.80 (falling) / 1,250.43 (rising)   price vs 50 -13.4%, vs 200 +8.8%
  RSI(14) 42.0   ATR(14) $90.55 = 6.7% a day   52-wk 164.56–2,354.39 (-42% from the high)
  Trend: above a rising 200-DMA
  Chase guard: ok
  Next report: 2026-10-29 after the close (1 sessions; EPS est. 45.22)   ✘ inside the 3-session buy blackout
  Swing support below: 1,325.03, 1,277.33, 998.19   resistance above: 1,446.62, 1,600.00, 1,696.37
```
- **Structure:** lower highs since June (2,354 → 1,909 → …). The 10/23–10/26 double low at $1,228.89 / $1,229.00 sits on the rising
  200-DMA. It is not yet in the script's support list, which needs 5 bars after a low. Today opened a gap from the 10/27 high of
  $1,315.98 to today's low of $1,343.85.
- **Volume:** 3.3M by 10:52 ET, against 7.0M on 10/27 (Yahoo bars).
- **Chart:** `/tmp/claude-1000/-home-waelas-wael-amana-amana-assistant/cf7235bd-03e5-456e-8948-a8c2229a57bd/scratchpad/charts/SNDK.png`.
  It shows the price sitting on the 200-DMA with the 20- and 50-DMA falling above it.

**Zone checks** (`levels.py SNDK --zone … --size 250 --sleeve 3426`, 10/28 10:52 ET data):
```
# 7/17-low pullback 1,300-1,330 / 1,180 / 1,446.62
    at low   1,300.00: R/R 1.22:1, stop 1.33 ATR (9.2%)   ✘ R/R < 2; stop < 1.5 ATR
    at mid   1,315.00: R/R 0.97:1, stop 1.49 ATR (10.3%)   ✘ R/R < 2; stop < 1.5 ATR
    at high  1,330.00: R/R 0.78:1, stop 1.66 ATR (11.3%)   ✘ R/R < 2
# 200-DMA / double low 1,240-1,260 / 1,100 / 1,446.62
    at low   1,240.00: R/R 1.48:1, stop 1.55 ATR (11.3%)   ✘ R/R < 2
    at mid   1,250.00: R/R 1.31:1, stop 1.66 ATR (12.0%)   ✘ R/R < 2
    at high  1,260.00: R/R 1.17:1, stop 1.77 ATR (12.7%)   ✘ R/R < 2
    size $250 ≈ 0.2000 sh at the mid; risk to stop $30.00 = 0.9% of $3,426   ✓ ≤ 2%
# breakout retest 1,450-1,470 / 1,310 / 1,600
    at low   1,450.00: R/R 1.07:1 ✘ · at mid 1,460.00: R/R 0.93:1 ✘ · at high 1,470.00: R/R 0.81:1 ✘
```
**No passing zone.** At a $90.55 ATR, 2:1 needs ≈ **$272 of open air** above the entry. The widest pocket on this chart, from
$1,228.89 to $1,446.62, is $218.

**The condition that would create a zone:** after the print, ATR(14) at **≤ ≈ $70** and a higher low above $1,228.89. Then
≈ $1,235–1,240 with a stop ≈ $1,130 pays 2:1 to $1,446.62. Alternatively, a post-report close above $1,600 that holds, re-derived
against $1,696–1,909. A gap day usually raises ATR, so expect no SNDK zone in the first half of November.

## Fundamentals
- **FQ4 FY26** (8-K 2026-08-05): revenue **$8,965M**, +51% q/q and +372% y/y; data center $2,977M, +103% q/q; non-GAAP gross margin
  **84.6%**; non-GAAP EPS **$39.25**; FCF $7,083M (FY26 $11,494M). Cash $4,762M, no long-term debt (7/3).
- **Valuation** (stockanalysis, 10/28 10:58 ET, price $1,361.88): market cap **$199.4B**, EV $193.1B, forward P/E **6.34**, trailing
  18.46, EV/sales 9.12. Consensus EPS FY27 **$214.82**, FY28 $266.30, so 6.3× / 5.1× at $1,360.78.
- Margins (TTM): gross 71.47%, operating 61.58%; FCF $11.49B (stockanalysis).

## News & catalysts (last 30d / next 90d)
- 10/28: SNDK +4.4% premarket to $1,362.24 on SK hynix's record Q3 (TipRanks). **Confirming** read-across, though SK hynix is
  mostly DRAM.
- 10/26: Bernstein Buy $3,000 (HBF could use ≈ 6.5× the NAND wafer of conventional products); Wedbush Buy $2,000, FQ1 estimates
  raised to $11.45B / $49.04 (TipRanks 10/28; stockanalysis). **Confirming**, and it raises the bar.
- 10/22–10/24: WDC sold off on rising NAND/DRAM input costs (FinanceFeeds 10/24). SNDK's selling price is WDC's input cost.
  **Confirming** for SNDK pricing.
- 10/18: Mizuho Buy $2,050 (stockanalysis). **Neutral.**
- 9/30: TrendForce 4Q26 NAND +15–20%, retail channels struggling to absorb record wafer prices. **Neutral.**
- Next: **10/29 AMC report** · 11/2 first possible decision · 11/6 jobs report, 08:30 ET (calendar sites, not confirmed on bls.gov).

## Positioning & sentiment
- **Short interest** 4.70M shares at the 10/15 settlement (Nasdaq), 3.26% of float, 0.47–1.0 days to cover. No squeeze fuel.
- **Analysts:** 25, Buy; mean **$2,144**, median $2,150, range $1,000–3,600 (S&P via stockanalysis, 10/26). TipRanks: 15 Buy / 2 Hold,
  mean $2,205.59 (10/28).
- **Crowding:** +673% over 52 weeks (stockanalysis 10/28), and the consensus sits above the guide. That is the setup that gapped
  −13% on 8/5.

## What would make me wrong
- A beat-and-raise that gaps SNDK +15% and keeps going. The cost of being out is ≈ $30–40 on a $250 line. Not buying a binary
  event inside a blackout is the plan, not an error.
- NAND re-accelerates in 1Q27 (TrendForce) while the group re-rates. Then SNDK's operating leverage beats MU's, and the ranking
  should flip.

## Sources
- `levels.py SNDK` (Yahoo chart API + Alpha Vantage), 10/28 10:52 ET data, with the zone checks above. Earnings reactions are from
  the same Yahoo bars.
- [Sandisk FQ4 FY26 8-K](https://www.sec.gov/Archives/edgar/data/0002023554/000162828026053346/sndkq4-26ex991xpressrelease.htm) — 2026-08-05
- [stockanalysis SNDK statistics](https://stockanalysis.com/stocks/sndk/statistics/) · [forecast](https://stockanalysis.com/stocks/sndk/forecast/) — fetched 2026-10-28
- [TipRanks: what analysts expect ahead of Q1](https://www.tipranks.com/news/sandisk-stock-forecast-what-financial-analysts-expect-ahead-of-q1-earnings) — 2026-10-28
- [TradingKey: SanDisk earnings preview](https://www.tradingkey.com/analysis/stocks/us-stocks/262247048-sandisk-earnings-preview-nand-data-center-demand-sndk-tradingkey) — 2026-10-28
- [TipRanks: MU, SNDK, SK hynix premarket 10/28](https://www.tipranks.com/news/why-are-micron-sandisk-and-sk-hynix-stocks-extending-gains-in-premarket-today-october-28) — 2026-10-28
- [FinanceFeeds: WDC falls 3% after the beat; Sandisk 10/29](https://financefeeds.com/western-digital-stock-falls-3-after-the-4-64-beat-what-shares-are-saying-before-sandisk-reports-on-29-october/) — 2026-10-24
- [Optionslam SNDK earnings history](https://www.optionslam.com/earnings/swim/SNDK) — fetched 2026-10-28
- Nasdaq API: SNDK Oct-30 option chain (11:00 ET), short interest (10/15), earnings-surprise history — fetched 2026-10-28
- [TrendForce 4Q26 contract prices](https://www.trendforce.com/presscenter/news/20260930-13258.html) — 2026-09-30

---

## SNDK — update 2026-10-19 (not held: stopped 10/15 at $1,300.39)

**Verdict:** WATCH · no buy while MU is held (one memory name) · re-check after the **10/29** report · **Conviction:**
Med on the business, Low on the setup. The 10/15 stop sold at $1,300.39; it closed 10/16 at $1,299.30, so the stop was
right on the day. It is +6.9% since on the bounce, which changes nothing about the rules.

| | |
|---|---|
| Price | **$1,388.37** (2026-10-19, 10:35 ET, +6.9%); close $1,299.30 (10/16, −6.9%; 7th straight lower close); 10-day low **$1,276** |
| 20 / 50 / 200-DMA | $1,631.5 / $1,596.6 (rising) / **$1,216.5** — price −13% under the 50, +14% over the 200 |
| RSI(14) · ATR(14) | 37.5 · **$98 = 7.1% a day** · −41% from the 6/22 high of $2,354.39 |
| Report | **10/29** after the close (Unusual Whales, FXLeaders; not seen on Sandisk IR). Consensus EPS ≈ $45.22, revenue ≈ $10.7B; implied move ≈ ±11%. Last quarter's non-GAAP gross margin 84.6% |

**News (dated):** the 10/16–10/19 fear is CXMT ("4F²" density, a product before year-end). CXMT makes DRAM, not NAND;
Goldman calls the fear overstated (≈ 50% of China's local demand by 2028). Morgan Stanley's 10/13 note was on Samsung and
SK hynix: memory stocks have peaked 4–8 months before earnings did. KeyBanc expects NAND prices +≈ 20% q/q in Q4 2026.
Targets since 10/1: Mizuho $2,050 (10/5), Goldman $2,200 (10/12), Bernstein $3,000; no downgrade found. September
insider sales (CEO ≈ $53M on 9/17) were 10b5-1 plan sales.

**When it could be a buy again:** only if MU is sold or the client wants a second memory line (which the plan does not
allow), after 11/2, on a higher low after the print with gross margin ≥ 83% and a stop within 1.5 ATR.

**Sources:** Yahoo chart API SNDK 1y daily, fetched 2026-10-19 10:35 ET · [FXLeaders, 10/19: Sandisk forecast, CXMT, earnings](https://www.fxleaders.com/news/2026/10/19/sandisk-stock-forecast-sndk-cxmt-earnings/) · [KuCoin: Samsung/SK hynix valuation trap (Morgan Stanley 10/13)](https://www.kucoin.com/blog/samsung-sk-hynix-valuation-trap) · [Unusual Whales: SNDK earnings](https://unusualwhales.com/stock/SNDK/earnings) · [ad-hoc-news: Goldman $2,200](https://www.ad-hoc-news.de/boerse/news/corporate-news/goldman-sets-usd-2-200-target-for-sandisk-stock/70359204) · [SEC Form 4, CEO 9/17](https://www.sec.gov/Archives/edgar/data/0002023554/000124264826000032/edgardoc.xml).

---

## SNDK — Sandisk Corp — check 2026-10-14 (client: "it's on sale, isn't it an opportunity?")

**Verdict:** HOLD the existing 0.135 sh **only with the broker stop at $1,310** · **NO ADD** · sell before the 10/29
report if it is still under the 50-DMA (≈ $1,590) on 10/28 · **Conviction:** Med.

| | |
|---|---|
| Price | **$1,436.55** (2026-10-14, 10:00 ET, −3.1%); close $1,482.33 (10/13, reversed from a 1,401.01 low) |
| 50-DMA / 200-DMA | $1,592 / $1,200 · SMA20 $1,688 falling · RSI 35.9 · ATR ≈ $96 (6.7%) |
| Add at today's price | stop 1,310 → R/R **1.2:1** to $1,590 ✘ |
| An add with R/R ≥ 2:1 | would need an entry ≤ $1,393, only 0.9 ATR above the stop, so noise would hit it. **There is no valid add before 10/29.** |
| Next earnings | **10/29** after close (Oct-30 straddle ≈ ±12.7%; average move 9.3%) |

**Why "cheap" is not a level:** the five memory dip-buys made in October (WDC ×2, EWY, STX, SNDK) are **−$91.87 together
with fees** at 10/14 prices. SNDK fell from 1,952 to 998 (−49%) in three weeks in July. Supports below: 1,401 (10/13 low),
1,325 (7/17), ≈ 1,200 (200-DMA + Aug gap 1,163–1,212), 998.

**When it becomes a buy (from 11/2, after the report):** the 10/29 print holds the gross margin ≥ 83% and the guide does
not slow again, **and** price closes back above the 50-DMA (≈ $1,590) or makes a higher low after the report. Write
the stop under the post-report low, R/R ≥ 2:1, ≈ $200. If the 1,310 stop fires first, §4a applies: no re-buy without a
higher low (the 200-DMA ≈ $1,200 is where that base would most likely form).

Sources: Yahoo chart API SNDK 1y daily + 1d 5-min bars, fetched 2026-10-14 ≈ 10:00 ET; earlier entry below.

---

## SNDK — Sandisk Corp — deep dive 2026-10-13

**Verdict:** **EXIT today** (sell at market before the close) · re-entry only on the WATCH trigger below ·
**Conviction:** Med — the company is extraordinary, but the trade is not. At $1,452 the reward/risk is 0.9:1. The
memory group is in a 4-month downtrend in which every one of the client's memory stops just fired. The 6.7× P/E is what
the market pays for peak earnings, not a discount. The position was bought with no stop and no research, 17 minutes
after the STX stop fired.

| | |
|---|---|
| Price | **$1,451.97** (2026-10-13, 10:30 ET); close $1,487.33 (10/12, −6.0%); today's open/low 1,405.75/1,403.16 |
| Position | 0.1353 sh @ $1,477.05 = ≈ $196 (5.6%), **no broker stop** |
| 50-DMA / 200-DMA | **$1,591** (rising) / **$1,194** — price under the 20 (1,690, falling) and the 50 |
| 52-wk high / low | $2,354.39 (2026-06-22) / $120.96 (2025-10-14) · **−38% from the high**, still +512% YTD |
| RSI(14) · ATR(14) | 36.8 · **$95.8 = 6.6%** |
| If held, the stop | **$1,310** (under the 7/17 low 1,325; 1.5 ATR; −11.3% from cost). Risk ≈ $19 |
| First target | $1,580–1,600 (10/9 close 1,582, 50-DMA 1,591) |
| Reward/risk | **0.9:1** ✘ (plan minimum 2:1) |
| Next earnings | **Thu 2026-10-29** after close (confirmed). Last 4 reactions +15.3 / +6.9 / +8.3 / **−6.8%** (the last one gapped −13% on a beat); Oct-30 straddle ≈ ±12.7% |

### The business (company 8-Ks)
| | Q2 FY26 (Jan) | Q3 FY26 (Apr) | Q4 FY26 (Jul) | Q1 FY27 guide |
|---|---|---|---|---|
| Revenue | $3.03B | $5.95B | **$8.97B** | $10.3–10.8B |
| Sequential growth | +31% | +97% | +51% | **≈ +18%** |
| Gross margin | 50.9% | 78.4% | **84.6%** | 83–85% |
| Free cash flow | $0.98B | $2.99B | **$7.08B** | — |
- Zero debt, $4.76B cash (7/3). **$15.5B of buyback authorization** left. Shares 149M → 146.4M.
- **$93.9B of minimum contracted revenue** at floor prices (8 customers, more than 4 years). It covers more than half of
  FY27 bits and ≈ ⅔ of FY28.
- Valuation: $211.6B market cap, **6.7× forward P/E**, 10.4× EV/sales (TTM). FY27 consensus EPS $214.82. Analysts:
  Buy, average PT $2,173 (range $1,000–3,600). Recent: Bernstein $3,000 (10/5), Mizuho $2,050 (10/6), Citi $2,100 (10/9).
- Western Digital's stake is fully sold (no overhang). Short interest is only 3.3% of float, so there is little squeeze fuel.

### Why it is not a buy (or a hold) here
1. **Cycle math.** Morgan Stanley (10/13, relayed): memory stocks have peaked ≈ 4–8 months *before* earnings did
   (2008, 2012, 2018). Samsung and SK hynix trade at 3–4× forward for that reason. SNDK's price peaked on 6/22 while its
   EPS is still rising, which is exactly that pattern.
2. **The rate of change is turning.** Sequential growth went +97% → +51% → ≈ +18% guided. TrendForce's 3Q NAND forecast
   was +10–15% ("slower than previous quarters", 7/3). 4Q is +15–20%, but only enterprise SSD is accelerating. NAND
   wafer spot fell 2.9% in the week to 10/5.
3. **Supply response.** SK hynix lifted 2026 capex 50% to ≥ $31B (7/29). YMTC has 14% NAND share and new fabs. CXMT's
   4F² DRAM news (10/10) set off this week's sell-off.
4. **The whole group is in a downtrend.** From the June peaks: SNDK −38%, WDC −54%, STX −37%, MU −25%, EWY −25%. On
   10/12–10/13: KOSPI −5%, Samsung and SK hynix ≈ −8%. The client's EWY, WDC and STX stops fired in two sessions.
5. **The chart.** Lower highs (2,354 → 1,953 → 1,909 → 1,802). Price is under the 50-DMA, and today it is testing the
   1,390–1,436 support zone. The next supports are 1,325, then 1,163–1,212 (August gap / 200-DMA), then 998.
6. **The entry broke §2 and §4a.** No research, no stop, R/R 0.9:1, and the same memory bet re-bought in the session its
   STX stop fired. SNDK is also the name of the pre-reset −$80 chase.

### WATCH — what would make it a buy again (after 10/29)
All three:
- The 10/29 report holds the gross margin at ≥ 83%, **and** the FQ2 guide shows sequential growth that is not falling
  again.
- Price forms a higher low above $1,390 **or** closes back above the 50-DMA (≈ $1,590).
- A written stop and R/R ≥ 2:1 at that point, inside the plan's sizing. One memory position at a time.

### What would make me wrong
- A 10/29 beat-and-raise (the last three beat the top of guidance by 8–24%) re-rates the group. The cost of being out is
  missing a +10–15% gap on a ≈ $196 line, roughly $20–30.
- TrendForce's 1Q27 forecast reaccelerates NAND contract prices.

### Sources
- Yahoo chart API SNDK 2y daily + 1d 5-min bars, fetched 2026-10-13 ≈ 10:30 ET
- Q4 FY26 8-K https://www.sec.gov/Archives/edgar/data/0002023554/000162828026053346/sndkq4-26ex991xpressrelease.htm — 2026-08-05
- Q3 FY26 8-K https://www.sec.gov/Archives/edgar/data/0002023554/000162828026028879/sndkq3-26ex991xpressrelease.htm — 2026-04-30
- https://stockanalysis.com/stocks/sndk/statistics/ · /forecast/ · /financials/ratios/ — 2026-10-09/13
- https://www.trendforce.com/presscenter/news/20260703-13134.html — 2026-07-03
- https://www.trendforce.com/presscenter/news/20260930-13258.html — 2026-09-30
- https://www.trendforce.com/news/2026/10/07/insights-memory-spot-price-update-dram-spot-largely-sideways-as-holidays-month-end-effects-weigh — 2026-10-07
- https://www.kucoin.com/news/flash/morgan-stanley-low-valuation-of-memory-stocks-hides-high-risk-amid-cycle-peak — 2026-10-13 (secondary)
- https://www.fool.com/investing/2026/10/12/why-sandisk-stock-dropped-on-monday/ — 2026-10-12
- https://247wallst.com/investing/2026/07/13/micron-sandisk-western-digital-fall-6-as-sk-hynixs-weak-outlook-rattles-memory-stocks/ — 2026-07-13
- https://247wallst.com/investing/2026/07/29/sandisk-sinks-7-micron-slides-6-as-memory-selloff-intensifies-seagate-bucks-the-trend/ — 2026-07-29
- https://cryptobriefing.com/sandisk-94-billion-contract-revenue/ — 2026-08-13
- https://api.nasdaq.com/api/quote/SNDK/short-interest · /company/SNDK/earnings-surprise · option chain — 2026-10-13
- https://www.sec.gov/cgi-bin/own-disp?action=getissuer&CIK=0002023554 — insider sales 8/25–10/1
