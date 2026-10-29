# TTWO — Take-Two Interactive — research log

One file per ticker; newest entry first. Each entry is dated; numbers are as of that date.

Entries:
- 2026-10-28 (deep dive + 11/9 earnings preview + thesis scorecard)
- 2026-10-19 (update)
- 2026-10-13
- 2026-09-09

---

## TTWO — Take-Two Interactive — deep dive 2026-10-28

**Verdict:** HOLD through the 11/9 report with the **$190 broker stop** · no adds (2 of 2 used) · sell ⅓ only in $222–228, or
above $270 in launch week · **Conviction:** Med on the launch, **Low on the report**. Three of the last four reports traded
≥ 6.9% below the prior close intraday. Two brokers trimmed into it. The price sits 4.6% above the stop, and options imply ≈ 10%.

| | |
|---|---|
| Price | **$199.06** (2026-10-28 10:52 ET, levels.py; refresh $199.82 at 11:06 ET, 5.0% above the stop); close $201.28 (10/27); 10/13 low **$196.30** |
| Position | 2.35163202 sh @ $213.11 = **$468.13**, 13.7% of the $3,426 sleeve, **−6.6% (−$33.03)** |
| 20 / 50 / 200-DMA | $204.86 / $212.44 (falling) / $220.39 (falling): −6.3% under the 50, −9.7% under the 200 |
| RSI(14) · ATR(14) | 39.3 · **$5.69 = 2.9% a day** · 52-wk $187.63–265.94 (−25% from the high) |
| Stop | **$190** (broker, hard; never lowered): $9.06 = **4.55% = 1.59 ATR** below. Risk from here **$21.31**; from cost −$54.35 (−10.8%). Hard exit −15% from cost = $181.14 |
| Sell zone (⅓ = 0.78 sh) | **$222–228** = the falling 200-DMA ($220.39) and the 9/14 high ($224.26); 11.5% above. Banks ≈ +$6.93 at $222. The 50-DMA ($212.44) has dropped out of the zone; first resistance is $204.9–212.0 (20-DMA, 9/30 high $210.15, 10/22 high $212.00) |
| Buy zone | **none**: 2 of 2 adds used, and price is below a falling 200-DMA |
| Next events | **Earnings Mon 11/9 after the close** (company PR 10/13; levels.py/Alpha Vantage: 8 sessions) · decision confirmed Fri 11/6 · pre-load 11/12 · reviews 11/18 (reported, unconfirmed) · **GTA VI 11/19** · review 12/19 |
| Override note | Circuit-breaker halving (1.1758 sh) skipped 10/23–10/27: an OVERRIDE on the §7 ledger. Not re-argued here |

### What changed since the 10/19 entry
- **Price** $205.14 → $199.06 (−3.0%):
  - a lower high at $212.00 (10/22), then closes of $203.69, $203.35 and $201.28;
  - the 50-DMA fell $218.3 → $212.44 and the 200-DMA $222.1 → $220.39;
  - RSI 45.7 → 39.3, ATR $6.73 → $5.69.
- **BofA** kept Buy but cut its target **$368 → $330**: FY28 EPS cut to $13.03 from $14.13; "be long TTWO through the GTA 6
  launch". Reported 10/28 (tech-insider). Single source; the note's date is not given.
- **GTA VI review codes** are reportedly out with an **11/18 embargo** (insider NateTheHate, 10/26; via GTABoom and Insider
  Gaming; not confirmed by Rockstar). The official page still lists 11/19 (10/27). Pre-load starts 11/12 (Rockstar). No delay
  reports.
- **Short interest** 9.63M shares = **5.21% of float**, 3.8 days to cover, +3.5% (MarketBeat, 10/15 record). It was 5.0% at 9/30.
- **Implied move** now ≈ ±10.2% to the 11/13 expiry and ±12.7% to 11/20 (OptionSlam). The 10/13 entry had ±14% / ±17% from
  another source.

### levels.py check (informational: an add is blocked anyway)
"If this were a buy today": stop $190, T1 = the nearest real resistance ($210.15):
```
  Setup: zone 198.90–201.50, stop 190.00, T1 210.15
    at low     198.90: R/R 1.26:1, stop 1.56 ATR (4.5%)   ✘ R/R < 2
    at mid     200.20: R/R 0.98:1, stop 1.79 ATR (5.1%)   ✘ R/R < 2
    at high    201.50: R/R 0.75:1, stop 2.02 ATR (5.7%)   ✘ R/R < 2
    size $190 ≈ 0.9491 sh at the mid; risk to stop $9.68 = 0.3% of $3,426   ✓ ≤ 2%
    price is IN the zone
```
The same line, using the sell-zone bottom ($222) as T1, gives 2.60 / 2.14 / 1.78 : 1 (✘ at the high edge). The hold is a
catalyst bet to 11/19, not a technical setup. No add would pass even if one were left.

### Earnings preview — Q2 FY27, Mon 2026-11-09 after the close
1. **Date and time:** 11/9 after the close (company PR 10/13). levels.py: "2026-11-09 after the close (8 sessions)".
   - Last decision session: Fri 11/6. The decision is written now and confirmed after the 11/6 close.
   - Client commitment: no trades until 11/2. A stop fill is not a breach.
2. **Consensus and guide:**
   - **Q2 guide (8-K, 8/7):** net bookings **$1,620–1,670M**; GAAP revenue $1,420–1,470M; GAAP EPS −$0.84 to −$0.75.
   - **Consensus EPS is unreliable:** MarketBeat $0.97 (basis unclear), Alpha Vantage $0.49, against a GAAP guide that is
     negative. The stock trades on bookings and the guide.
   - **FY27 guide (reiterated 8/7):** net bookings **$8.0–8.2B**; GAAP revenue $7.9–8.1B; GAAP EPS $0.55–0.75; operating cash
     flow > $1.0B.
   - **The number that moves the stock:** the first launch-quarter (Oct–Dec) bookings guide. Wells Fargo expects
     **$3,350–3,400M vs $3,446M consensus**, and adjusted EBITDA $876–900M vs $926M (10/12).
   - **Also watch:** GTA VI pre-order and sell-through commentary; NBA 2K (Wells Fargo: units −10% y/y); mobile (top-20 daily
     users −22% y/y in Q2); recurrent consumer spending (84% of Q1 bookings, −1% y/y).
3. **Implied move:** **±10.16%** to the 11/13 weekly. It covers the report plus the 11/12 pre-load ($25.60 on a $201.28
   reference). It is ±12.72% to 11/20, which includes the launch (OptionSlam, fetched 10/28). The earnings-only part is
   smaller; the 10/13 entry estimated ≈ ±6.5%.
   - **vs the stop:** 4.55% away, so the implied move is **2.2× the distance**. A gap can skip the $190 stop.
   - **$ at stake:** ±10.16% × $468.13 = **±$47.56** (±$30.43 at ±6.5%).
   - **Gap math:** a −10.16% gap opens near **$178.84**, under both the stop and the −15% hard exit ($181.14). The broker sells
     there: **−$47.56 from now, −$80.59 from cost (2.4% of the sleeve)**. A gap is how the 2% risk cap gets broken. With
     everything else flat, the account would be ≈ $3,378 against the $3,401.87 breaker. Even a clean fill at $190 (−$21.31)
     would leave ≈ $3,405, a cushion of ≈ $3.
4. **Scenarios:**

   | Scenario | What has to happen | Likely reaction | Action written now |
   |---|---|---|---|
   | Bull | Q2 bookings ≥ $1.67B; FY27 $8.0–8.2B reiterated or raised; launch-quarter guide ≥ $3.45B; firm pre-order color | +6 to +10% → $211–219, into the $210–216 resistance and the 50-DMA | Hold. No add (2 of 2). Sell ⅓ (0.78 sh) only if it trades in **$222–228**. Launch week 11/16–20 above **$270** → sell ⅓ |
   | Base | Q2 in range; FY27 reiterated; launch-quarter guide $3.35–3.45B | ±3–5% → $189–209 | Hold with the $190 stop. If it fills, that is the plan |
   | Bear | FY27 cut, launch-quarter guide < $3.35B, or any GTA VI timing wobble | −8 to −12% gap → $175–183 | The broker stop sells at the open. No re-buy that session (§4a). A FY27 cut or a GTA VI delay is a thesis break: no re-entry before the 12/19 review |

5. **History** (levels.py bars; reaction day vs the prior close):

   | Report | Opening gap | Close | Intraday low |
   |---|---|---|---|
   | 11/6/25 after the close | −8.1% | −8.1% | −10.0% |
   | 2/3/26 after the close | −2.1% | −5.4% | −6.9% |
   | 5/21/26 after the close | +2.4% | −4.4% | −7.4% |
   | 8/7/26 before the open | +0.4% | +6.0% | −0.6% |

   **A stop 4.55% below the pre-report close would have filled in 3 of the 4**: at the open once, intraday twice.
6. **Decision (written 10/28; confirm after the 11/6 close):** **hold through the report with the $190 broker stop.** Never
   lower it, and no adds. Sell ⅓ (0.78 sh) only if it trades in $222–228 before the report. Exit before 11/9 only on a thesis
   break, such as an official GTA VI date change. Why not trim or exit now:
   - **(a)** The line is held for the 11/19 launch, eight sessions after the report.
   - **(b)** Below cost there is no sell zone (PLAN §3b). The stop decides (§4).
   - **(c)** The gap risk is the price of the thesis.

   The plan's tool for cutting that exposure was the breaker halving, and it was skipped (an OVERRIDE). Said plainly: **the
   stop is more likely than not to be tested on 11/10.** Never decide on report night.

### Thesis
GTA VI (PS5, Xbox Series X|S; $79.99 / $99.99) is still dated **11/19/2026**. The official page shows it as of 10/27, and
review codes are reportedly out. FY27 bookings guidance of $8.0–8.2B rests on it. Wells Fargo models ≈ 50M units at a $90
gross price; the guidance implies ≈ 33M at $80 (10/12). At $199 the stock carries no launch premium: −25% from the 7/7 high
and −20% YTD (Investing.com, 10/19). The risk is the 11/9 launch-quarter guide, not the launch. This is a catalyst hold to
11/19 and the 12/19 review, not a compounder.

### Chart & technicals (levels.py, 10/28 10:52 ET; chart `scratchpad/charts/TTWO.png` with the stop and $222)
- **Trend:** below a falling 50 and 200. Lower highs: $224.26 (9/14) → $215.66 (10/9) → $212.00 (10/22). Lows: $196.30
  (10/13), then $199.60–199.90 (10/26–10/27) and $198.90 today.
- **Support:** $196.30, then the Feb–Mar shelf $187.6–189.5. Under it, the stop.
- **Momentum and volume:** RSI 39.3, falling. Volume is quiet (1.3–2.4M a day since 10/14, against 5.2M on the 10/13 flush).
- **Distance from the 50-DMA:** −6.3%, so the chase guard is not relevant.

### Fundamentals (8-K, 2026-08-07)
- **Q1 FY27:** net bookings $1,385.9M (−3% y/y, above the $1.32–1.37B guide); GAAP revenue $1,533.9M; GAAP EPS −$0.18.
- **FY27 guide:** see the preview above. Capex ≈ $290M.
- **Balance sheet and earnings (Investing.com, 10/19, data as of 6/30):** debt $2.94B, levered FCF $298.7M. Consensus EPS
  $6.99 for FY27 and $10.25 for FY28.

### News & catalysts (last 30 days / next 90)
- **10/12:** Wells Fargo kept Overweight at $300 and cut its Q2 estimates. Launch-quarter bookings $3.35–3.40B vs $3.446B
  consensus. *Weakening.*
- **10/13:** closed −4.1% (low $196.30, −6.0% intraday) on a PC-port timing rumor (TipRanks headline via search). *Neutral.*
- **BofA:** target $368 → $330, Buy kept. Reported 10/28; the note's date is unverified. *Weakening.*
- **10/26:** review codes reportedly out, 11/18 embargo. Unconfirmed. *Confirming.*
- **Next:**
  - **11/9 report**;
  - 11/12 pre-load;
  - 11/18 reviews (reported);
  - **11/19 launch**;
  - 12/19 desk review.

### Positioning & sentiment
- **Short interest:** 5.21% of float, rising (10/15).
- **Analysts:**
  - BofA Buy $330 (the cut above);
  - Wells Fargo Overweight $300 (10/12);
  - Investing.com's fair-value model shows 8.3% downside (10/19).
- **Insiders:** zero buys in 2026, ≈ $12.9M sold in 90 days (10/13 entry; not re-fetched).
- **Crowding:** not crowded or extended. It is a single-event stock into a binary report.

### Thesis scorecard
| Pillar (falsifiable) | Expected | Status (dated) | Trend |
|---|---|---|---|
| GTA VI ships 11/19/2026 | on date | Official page 11/19 (10/27); pre-load 11/12; review codes reportedly out (10/26) | stable / improving |
| FY27 net bookings guide held | $8.0–8.2B | Reiterated 8/7; next test 11/9 | stable (untested) |
| Launch-quarter guide ≥ consensus | ≥ $3.35B (WF low), ideally ≥ $3.446B | Wells Fargo expects $3.35–3.40B (10/12); BofA FY28 EPS cut (reported 10/28) | **weakening** |
| Core business stable (NBA 2K, mobile) | Q2 bookings in $1.62–1.67B | NBA 2K units −10%, mobile daily users −22% (Wells Fargo, 10/12); Q1 above guide | **weakening** |
| Price holds the stop shelf | closes > $190 | $199.06; lower highs; −9.7% under a falling 200-DMA | **weakening** |

- **Thesis-break exits (whatever the price):**
  1. Any official GTA VI date change.
  2. A FY27 net bookings guide cut below $8.0B on 11/9.
  3. A daily close under $190, which the broker stop executes.
- **Disconfirming evidence logged:** two broker cuts into the print, a 3-of-4 down-reaction history, and rising short interest.
- **Conviction:** Med on the launch, Low on the report. A launch-quarter guide ≥ $3.45B lifts it to Med. A FY27 cut ends the
  position.

### What would make me wrong
- **On the hold:** the 11/9 guide is weak and the stock gaps through $190. The fill could land near $179–183, which costs
  $38–48 from here.
- **On the patience:** a strong guide and a launch run past $222 in days. Then the call is to sell ⅓ in the zone, not to chase
  the add.
- **On the launch:** a delay. That is the one event that ends the position outright.

### Sources
- levels.py (Yahoo chart API daily bars; Alpha Vantage calendar), run 2026-10-28, quotes 10:52 ET; reaction history computed
  from the same bars
- [Take-Two Q1 FY27 results, 8-K](https://www.sec.gov/Archives/edgar/data/0000946581/000162828026054580/ttwo1q27earningsrelease.htm): 2026-08-07
- [OptionSlam: TTWO earnings straddle](https://www.optionslam.com/earnings/straddle/TTWO): fetched 2026-10-28 (reference $201.28)
- [tech-insider: BofA Buy, $330 target](https://tech-insider.org/take-two-bofa-buy-330-target-gta-6-earnings-2026/): 2026-10-28
- [Investing.com: Wells Fargo reiterates Overweight at $300](https://investing.com/news/analyst-ratings/wells-fargo-reiterates-taketwo-stock-overweight-rating-at-300-target-93CH-4943909): 2026-10-12 (re-fetched 10/28)
- [Investing.com: TTWO stock analysis into GTA VI release](https://www.investing.com/news/stock-market-news/taketwo-interactive-ttwo-stock-analysis-into-gta-vi-release-93CH-4956738): 2026-10-19
- [GTABoom: review codes going out, 11/18 embargo](https://www.gtaboom.com/trusted-insider-says-gta-6-review-codes-are-going-out-right-now-4d27): 2026-10-26 (via search)
- [MarketBeat: TTWO short interest](https://www.marketbeat.com/stocks/NASDAQ/TTWO/short-interest/): 10/15 record, published 10/26
- [MarketBeat: TTWO Q2 2027 estimates](https://www.marketbeat.com/earnings/reports/2026-11-9-take-two-interactive-software-inc-stock/): via search, 10/28

---

## TTWO — update 2026-10-19

**Verdict:** HOLD to the launch with the $190 stop · no adds (2 of 2) · sell ⅓ in $222–228, or > $270 in launch week ·
**Conviction:** Med. Quiet: no new dated news since the 10/13 entry. GTA VI is still **11/19**; no delay reports.

| | |
|---|---|
| Price | **$205.14** (2026-10-19, 10:35 ET, −0.1%); close $205.28 (10/16); 10/13 low **$196.30** |
| 20 / 50 / 200-DMA | **$204.9** / $218.3 (falling) / $222.1 — price on the 20, −6.0% under the 50 |
| RSI(14) · ATR(14) | 45.7 · **$6.73 = 3.3% a day** · −23% from the 7/7 high of $265.94 |
| Position | 2.3516 sh @ $213.11 = ≈ $482, 14.0% of the sleeve, −3.7% |
| Stop | **$190** (broker, confirmed live 10/19): 7.4% / 2.3 ATR below, above the Feb–Mar shelf $187.6–189.5. Risk ≈ $35 |
| Sell zone (⅓) | **$222–228** = the 50 and 200-DMAs plus the 9/14 high → 0.78 sh; it is 8% above today's price |
| Next events | **Earnings Mon 11/9** after the close (company PR 10/13) · pre-load 11/12 · **launch 11/19** · review 12/19 |

The chip sell-off did not touch TTWO (−2.0% on 10/16 vs SOX −3.8%). It is the one satellite that does not move with
AMD, ARM and MU, and that is why it stays. The risk is the 11/9 guide: Wells Fargo (10/12) expects $3.35–3.40B for
the launch quarter vs $3.446B consensus.

**Sources:** Yahoo chart API TTWO 1y daily, fetched 2026-10-19 10:35 ET · news sweep 10/19: no TTWO item dated 10/10–10/19 · launch date per the 10/13 entry sources.

---

## TTWO — Take-Two Interactive — deep dive 2026-10-13 (update of the 2026-09-09 entry below)

**Verdict:** HOLD to the GTA VI launch with the 190 stop · no adds (2 of 2 used) · sell ⅓ in $222–228 or > $270 in
launch week · **Conviction:** Med — the launch is still 11/19 and the stock carries no pre-launch premium (−23% from July).
Against that: the core business is soft, and Wells Fargo expects a launch-quarter guide below consensus on 11/9.

| | |
|---|---|
| Price | **$203.72** (2026-10-13, 10:29 ET); close $208.82 (10/12); today's low 198.72 |
| Position | 2.3516 sh @ $213.11 = ≈ $479, **13.6%** of the sleeve, −4.4% |
| 50-DMA / 200-DMA | **$221.0** (falling) / **$223.2** — price under both |
| 52-wk high / low | $265.94 (2026-07-07) / $187.63 (2026-03-27) · −20.4% YTD |
| RSI(14) · ATR(14) | 41.9 · **$6.62 = 3.3%** |
| Stop | **$190** (broker, hard): 2.1 ATR under; just above the Feb–Mar shelf of $187.6–189.5. Risk ≈ $32 = 0.9% |
| Sell zone | **$222–228** (50-DMA 221.0, 200-DMA 223.2, 9/14 high 224.26) → ⅓ = 0.78 sh · launch week > **$270** → ⅓ |
| Buy zone | $193–198 shown, **blocked**: 2 of 2 adds used until a profit-banking sale |
| Next events | **Earnings Mon 11/9 after close (confirmed, company PR 10/13)** · pre-load 11/12 · **GTA VI 11/19** (PS5, Xbox Series X\|S) |
| Expected moves | options ≈ ±14% to the 11/13 expiry, ≈ ±17% to 11/20 (≈ ±6.5% for earnings, ≈ ±6% for launch week); last 4 earnings −8.1 / −5.4 / −4.4 / +6.0% |

### Thesis
GTA VI is the largest entertainment launch on the calendar: $79.99 standard and $99.99 Ultimate, pre-orders open since
6/25. Management called pre-orders "unprecedented and astonishing" (Q1 call, 8/7). Third-party estimates (Sensor
Tower) are ≈ 4.4–5M pre-order units; there is no official count. FY27 guidance is net bookings **$8.0–8.2B** (reiterated
8/7). Wells Fargo models ≈ 50M units at a $90 average price (10/12, PT $300). Morningstar models 60–70M. **At $204 the
stock is priced below its pre-launch levels**: ≈ 25× forward earnings, ≈ 4.8× FY27 bookings guidance. This is a
catalyst hold, not a compounder. The plan's rule: trim into the run-up, not after the launch.

### What has gone wrong since July
- Pricing at $79.99 disappointed the $90–100 bulls. The physical edition is only a download code, and the game is
  single-player at launch (6/24–26).
- Gameplay leaks ("Cyberleek", 8/18–8/21 and 8/31: −6.7%) and rumors that GTA Online slips to 2027 (mid-September).
- Guidance was not raised despite record pre-orders. The $400 Collector's Edition (without the game) drew backlash.
- **10/12 Wells Fargo:** NBA 2K units −10%, mobile daily users −22%. Q2 estimates cut to the low end of guidance. It
  expects a Q3 (launch-quarter) bookings guide of **$3.35–3.40B against $3.446B consensus**.
- Short interest is up ≈ 42% since mid-August, to 9.3M = 5.0% of float (9/30). Insiders: zero buys in 2026, ≈ $12.9M sold
  in 90 days.

### Analogue: GTA V (launched 9/17/2013)
The stock ran +34% into August 2013, then fell −11% into launch day. It was +4% a week later and −7.7% at the November
low, then +17.6% five months out: buy the rumor, sell the news, recover on results. **2026 is different**: there was no
run-up, and the stock goes into launch −23% from its high. The usual sell-the-news risk is smaller. The risk now is a
weak 11/9 guide.

### Calls
1. **Hold with the broker stop at 190. Never lower it.** Under 190 the Feb–Mar shelf ($187.6–189.5) has failed. That is
   information, not a discount.
2. **Price alert $222** → sell 0.78 sh (⅓) by hand. That banks ≈ +$7, resets the add count, and puts proceeds in the Reserve.
3. **Hold through 11/9 earnings** with the stop. Expected move ≈ ±6.5%. Three of the last four reactions were down.
   Accept a gap of that size, or trim beforehand.
4. **Launch week 11/16–11/20 above $270** → sell ⅓ (the ratchet's +25% rung is $266.39).
5. Review on 12/19: exit or re-underwrite on launch data.

### What would make me wrong
- A daily close under $190.
- An official delay of GTA VI, or launch-week reviews or sales that badly miss (< 30M units implied by the guide).
- An 11/9 launch-quarter guide well below $3.35B.

### Sources
- Yahoo chart API TTWO 1y daily bars, fetched 2026-10-13 10:29 ET; GTA V 2013 bars
- https://www.take2games.com/ir — Q2 FY27 date PR, 2026-10-13
- https://www.take2games.com/ir/news/take-two-interactive-software-inc-reports-results-fiscal-first-6 — 2026-08-07
- https://www.engadget.com/2200483/rockstar-reveals-gta-6-pricing-launch/ — 2026-06-24
- https://finance.yahoo.com/markets/stocks/articles/gta-6-pre-orders-send-212404392.html — 2026-06-26
- https://finance.yahoo.com/markets/stocks/articles/two-shed-2-83-billion-104851645.html — 2026-08-21
- https://investing.com/news/analyst-ratings/wells-fargo-reiterates-taketwo-stock-overweight-rating-at-300-target-93CH-4943909 — 2026-10-12
- https://tech4gamers.com/take-two-shares-decline-gta-6/ — 2026-09-27
- https://stockanalysis.com/stocks/ttwo/statistics/ · /forecast/ — 2026-10-12/13
- https://www.marketbeat.com/stocks/NASDAQ/TTWO/short-interest/ — 9/30 settlement
- https://www.optionsanalysissuite.com/stocks/ttwo/expected-move — 2026-10-12

---

## TTWO — Take-Two Interactive — deep dive 2026-09-09 (add + hold-through-launch request)

**Verdict:** ADD is *allowed* under PLAN §4 (one technical average-down, thesis intact) but the desk's call is
**ADD IN HALVES, not all at $211** · hold-through-launch = **OVERRIDE of PLAN §3/§8** · **Conviction: Medium**
— thesis (GTA VI 2026-11-19, reaffirmed Aug 2026) is intact; timing and the post-launch hold are the weak parts.

| | |
|---|---|
| Price (date) | $210.71 intraday 2026-09-09 (other feed $213.29; day range $210.15–216.26) |
| 52-week range | $187.63 – $265.94 |
| 50-day EMA / RSI(14) | ~$227.6 / ~43 (TipRanks, Sep 2026) — price ~7.5% *below* the 50-EMA; MA consensus "Strong Sell" |
| 30-day move | ≈ −17% (ad-hoc-news, 2026-09-09); −6.7% on 2026-08-31 alone (GTA Online delay speculation) |
| Entry zone | Desk: $200–205 (set 2026-09-09 review). Client: $211 now |
| Invalidation (stop) | **$185 weekly close** — below the $187.63 52-wk low; −13.6% from blended cost $214.0 |
| Target 1 / 2 | $265 (52-wk high, pre-launch run-up) / $290 (analyst median, 29 analysts) |
| Reward/risk (T1) | 2.1 : 1 from $211 with $185 stop (3.5 : 1 with the old $195 stop, but $195 sits above the 52-wk low) |
| Size | Client target $400 = 11.5% of sleeve (full satellite, inside the 10–15% cap) |
| Timeframe | Client: through 2026-11-19 launch + 1 month (≈ 2026-12-19) |
| Next earnings | **2026-11-05** (Q2 FY27; inside the hold window). Prior moves: Feb-2026 −18.3% vs 5.6% implied; May-2026 +0.2% vs 9.4% implied |

### Thesis
GTA VI ships 2026-11-19 (date reaffirmed by Rockstar with the Aug-2026 Extended Look). FY27 net bookings
guided $8.0–8.2B (~+20%); Street models ~37M launch-window units at $80. Stock has given back the summer
run (−21% from the July high) on execution worries (QA crunch, GTA Online timing, no PC date, digital-only).
Add thesis = buy the pre-launch dip; Morgan Stanley: publisher stocks average +18% in the 6 months before a
major release.

### Chart & technicals
Downtrend since July high $265.94. Below 20- and 50-day EMAs; RSI 43 (one feed says 32 on the EU listing =
near oversold). No confirmed support until the $200–205 area and the 52-wk low $187.63. Falling-knife shape:
the plan's "half at level, half on confirmation" applies.

### Fundamentals
FY27 EPS consensus $6.60, FY28 $10.51 → ~32x FY27 / ~20x FY28 at $211. Forward P/E 36.6x quoted 2026-08-14 at $242.
Q1 FY27 net bookings $1.39B beat. Valuation already embeds a successful launch; upside requires a *beat* on units.

### News & catalysts
- 2026-08-31 — Forbes speculation GTA Online may lag the 11/19 launch; Benchmark (Hickey) calls it speculation — **neutral/negative**
- 2026-08 — Rockstar Extended Look; date reaffirmed 11/19 — **confirming**
- 2026-09-17 — FOMC (binary; three hawkish dissents last meeting) — **macro risk**
- 2026-11-05 — Q2 FY27 earnings (no GTA VI sales in it) — **binary**
- 2026-11-19 — launch; Rockstar 3-day sales headline likely within a week (GTA V: $1B/3 days; RDR2: $725M/3 days)
- ~2027-02 — Q3 FY27 earnings = first quarter with GTA VI sales. **Falls AFTER the client's 12/19 exit window.**

### Positioning & sentiment
29 analysts: 28 Buy / 0 Hold / 1 Sell; median PT $290, range $170–368; BofA $320. Consensus is one-sided —
crowded long. Everyone knows the launch date; the "hype" is the consensus, not an edge.

### History of the trade the client wants (sell-the-news evidence)
- RDR2 (2018-10-26): 17M units in 8 days, record — stock still fell ~14% after the Nov-2018 print because Street
  numbers were higher. Buzz ≠ beat.
- GTA V (2013-09-17): $1B in 3 days; shares dipped on the buggy GTA Online launch weeks later; the *long-term*
  hold (years) was the winner, "the launch-day trade was a coin flip" (Yahoo/AOL, 2026-06-28).

### What would make me wrong
- Bull: pre-launch rally resumes above the 50-EMA (~$228) — then the $200–205 limit never fills and the client's
  "now" entry was right.
- Bear: weekly close < $185, another launch slip, GTA Online officially decoupled from launch, Nov-5 guidance cut.

### Sources
- TipRanks TTWO technicals (Sep 2026); Investing.com quote 2026-09-09; TIKR 2026-08-31 drop note; Investing.com
  analyst piece 2026-08-14; MarketBeat/Nasdaq earnings date 2026-11-05; Investing.com implied-move notes (Feb/May 2026);
  Yahoo/AOL "how blockbuster launches move stocks" 2026-06-28; ad-hoc-news 2026-09-09; Forbes 2019-02-06 (RDR2 drop).
