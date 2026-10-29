# GOOGL — Alphabet Inc. — research log

One file per ticker; newest entry first. Each entry is dated; numbers are as of that date.

Entries:
- 2026-10-28 (deep dive + Q3 earnings preview, written before tonight's report)
- 2026-10-19 (update)
- 2026-09-24

---

## GOOGL — Alphabet Inc. — deep dive 2026-10-28

**Verdict:** WATCH · no zone before the report · **levels re-derived 10/29+** from the post-report bars · no buy before 11/2 ·
**Conviction:** Med on the business, Low on the timing. It reports tonight, sits 5% under its 200-DMA, and the 9/24 trigger is dead.

| | |
|---|---|
| Price | **$323.86** (2026-10-28 10:52 ET, levels.py; refresh $323.54 at 11:11 ET); close $320.58 (10/27); $316.80 (10/26), the lowest close since 7/23 |
| 20 / 50 / 200-DMA | $339.76 / $341.49 (falling) / **$341.19 (rising)**: −5.2% under the 50, −5.1% under the 200 |
| RSI(14) · ATR(14) | 37.6 · $8.07 = 2.5% a day · 52-wk $266.50–408.61 (−21% from the 5/18 high) |
| Trend (levels.py) | "BELOW a rising 200-DMA → protocol: no fresh longs until it reclaims it" |
| Report | **Tonight, 10/28 after the close**, call 4:30 pm ET (TradingKey, 10/24). levels.py: "0 sessions ✘ inside the 3-session buy blackout" |
| Entry zone | **none.** The 9/24 Trigger A (close > $345, stop $330) is retired: check below |
| Support / resistance | **$314.90** (7/23 low), then ≈ $300 (OANDA channel $300.44; TradingKey $297.45) / the 200-DMA $341.19, then $351.60 (8/24), $359.40 (10/14), $364.17 (9/22) |
| Earliest buy | **11/2** (client commitment; 10/28 is FOMC day and 10/29 the PCE morning). Only after a close back above the 200-DMA and a zone that passes levels.py |

### What changed since the 10/19 entry
- **Price** $344.87 → $323.86 (−6.1%).
  - It lost all three averages on 10/21–10/22 (10/22 close $324.22, −3.1%) with the AI-capex and financing sell-off.
  - It then made lower closes through 10/26 ($316.80).
  - The 50-DMA turned down ($344.4 → $341.49). The 9/24 levels are obsolete.
- **Report date confirmed** for 10/28 after the close (was "≈ 10/27–10/28, not confirmed").
- **New dated items:**
  - J.P. Morgan raised its target $420 → $425 and expects Cloud revenue to roughly double (OANDA, 10/22).
  - Michael Burry said he may cut or sell his stake (MarketBeat, 10/26; comment undated).
  - A securities class action was filed over Gemini 3.5 Pro statements: class period 5/19–7/16/2026, lead-plaintiff deadline
    12/1 (BFA Law press release, 10/28; details via search and MarketBeat).

### levels.py check — the 9/24 Trigger A, retired
```
  Setup: zone 341.00–346.00, stop 330.00, T1 351.60
    at low     341.00: R/R 0.96:1, stop 1.36 ATR (3.2%)   ✘ R/R < 2; stop < 1.5 ATR
    at mid     343.50: R/R 0.60:1, stop 1.67 ATR (3.9%)   ✘ R/R < 2
    at high    346.00: R/R 0.35:1, stop 1.98 ATR (4.6%)   ✘ R/R < 2
    size $190 ≈ 0.5531 sh at the mid; risk to stop $7.47 = 0.2% of $3,426   ✓ ≤ 2%
    price 323.86 is BELOW the zone — the setup needs re-deriving (a lower price is not evidence)
```
With T1 at the 10/14 high ($359.40), R/R is 1.67 / 1.18 / 0.84 : 1, still ✘. Its old T1 of $380 is no longer the nearest
resistance: $351.60 and $359.40 sit in the way. **No passing zone today.**

**The condition that creates one** (re-derived from 10/29):
- **Bullish gap:** a daily close back above the 200-DMA ($341.19) that holds. Then a pullback zone near the 200-DMA, a stop
  under the post-report low (≥ 1.5 ATR away), and T1 at $359.40 or $364.17. T1 must sit ≥ 2× the stop distance above, and the
  zone is checked with levels.py before it is written.
- **Bearish gap:** a break of $314.90. No buy until a higher low forms above the ≈ $297–300 band, plus a reclaim.

### Earnings preview — Q3 2026, Wed 2026-10-28 after the close (result not out while this was written)
1. **Date and time:** tonight after the close (Alpha Vantage via levels.py; TradingKey). The last decision point is today's
   close. **No position, so nothing to decide.** No buy today (FOMC, blackout) or on the 10/29 PCE morning.
2. **Consensus:**
   - Revenue ≈ **$127.4–127.9B** (≈ +25% y/y; TradingKey 10/24, MarketBeat via OANDA 10/22).
   - EPS ≈ **$3.02–3.04** (Alpha Vantage: $2.94).
   - **Google Cloud ≈ $29.16B** (+92%; Zacks via search, 10/28).
   - What moves the stock:
     - Cloud revenue and backlog ($514B at Q2);
     - the 2026 capex guide ($195–205B, raised 7/22) and the 2027 framing;
     - **the free-cash-flow sign** (Q2 ≈ **−$5.9B**, the first negative in its public history per TradingKey);
     - Search growth (Q2 +17%).
3. **Implied move:** **±6.0%** to the 10/30 weekly (OptionSlam, fetched 10/28, reference ≈ $320); ±6.4% (EarningsWatcher via
   OANDA, 10/21). That puts the range at ≈ **$304–343**. The top of the range is the 200-DMA ($341.19). No position, so no $ at
   stake.
4. **Scenarios:**

   | Scenario | What has to happen | Likely reaction | Action written now |
   |---|---|---|---|
   | Bull | Cloud ≥ $29.2B with backlog > $514B; Search ≥ +15%; capex held at $195–205B; FCF back positive | +6–10% → $343–356, through the 200-DMA | No chase (and no buy before 11/2). Re-run levels.py 10/29–10/30. A zone needs a close > $341.19 that holds |
   | Base | In line; capex nudged up; FCF ≈ flat | ±3% → $314–334 | WATCH. Still under the 200-DMA: no fresh long |
   | Bear | Capex raised again with FCF negative a second time; Cloud margin squeeze; heavy 2027 capex language | −6–8% → $298–304, through $314.90 | No knife. Wait for a higher low above ≈ $297–300 and a reclaim |

5. **History** (levels.py bars; reaction day vs the prior close):

   | Report | Opening gap | Close |
   |---|---|---|
   | 10/29/25 | +6.2% | +2.5% |
   | 2/4/26 | −6.3% | −0.5% |
   | 4/29/26 | +6.9% | +10.0% |
   | 7/22/26 | −6.1% | −7.1% |

   All four gapped ≥ 6%. The 6% implied move is not generous.
6. **Decision:** none needed (not held). Write levels from the 10/29 and 10/30 bars, not from tonight's after-hours print.

### Thesis
Alphabet is the AI platform with its own chips (TPU), its own models (Gemini), and a cloud growing **+82% (Q2: $24.8B)** on a
**$514B backlog**. It earned a 34% operating margin in Q2 (TradingKey, OANDA). The bear case has moved since 9/24, from "AI
disintermediates search" to **"AI capex eats the cash"**:
- Q2 capex was $44.9B against $39.1B of operating cash flow;
- 2026 capex is guided at $195–205B;
- an **$80B equity raise** was announced 6/1: $30B public (half mandatory convertible preferred), a $40B ATM from Q3 (≈ $30B
  of it for employee-vesting taxes), and **$10B to Berkshire at $351.81 (A) / $348.20 (C)**;
- long-term debt was $98.2B at 6/30, up from $46.5B (TradingKey, 10/24).

At ≈ 24× forward earnings (TradingKey, 10/24) it is not expensive. But it is now a capital-hungry compounder, and the price is
below Berkshire's placement price. Under v3 it would be a third AI-capex line next to AMD (held) and any re-entry. It has to
beat the weakest holding to earn a slot.

### Chart & technicals (levels.py, 10/28 10:52 ET; chart `scratchpad/charts/GOOGL.png`)
- **Trend:** under all three averages. The 50 is falling and the 200 is still rising ($338.60 twenty sessions ago →
  $341.19). Lower highs: $364.17 (9/22) → $359.40 (10/14). The **$314.90** 7/23 low is the line; 10/26 held $316.60.
- **RSI** 37.6, bouncing from ≈ 30 on 10/26. **ATR** $8.07 (2.5%). Volume rose into the slide: 27.7–29.2M on 10/21–10/22 and
  28.5M on 10/27.
- **Data conflict:** MarketBeat (10/26) shows a 50/200-DMA of $342.79 / $353.19. levels.py shows $341.49 / $341.19 (Yahoo
  closes). levels.py is the desk's source.

### Fundamentals
- **Q2 2026 (reported 7/22):**
  - revenue $119.8B (+24%);
  - Cloud $24.8B (+82%), Cloud operating income $8.8B;
  - Search +17%, YouTube ads +13%;
  - operating margin 34%;
  - EPS $9.11 including a ≈ $99B equity-securities gain (≈ $2.85 without it, vs $2.89 expected);
  - capex $44.9B, FCF ≈ −$5.9B (TradingKey, 10/24; OANDA, 10/22).
- **Valuation:** ≈ 24× forward (TradingKey). MarketBeat's 15.9× trailing P/E is distorted by the equity gain.
- **Balance sheet:** the June equity raise, plus long-term debt doubling to $98.2B.

### News & catalysts (last 30 days / next 90)
- **10/21–10/22:** AI-capex sell-off (Meta FCF, Lam supply warnings); GOOGL −1.6% and −3.1%. *Neutral to weakening.*
- **10/22:** J.P. Morgan target $420 → $425, Cloud expected to ≈ double. *Confirming.*
- **10/26:** Burry may cut his stake; −1.1%. *Neutral* (sentiment).
- **10/28:** securities class action over Gemini 3.5 Pro statements (class 5/19–7/16). *Neutral* (litigation noise; Q2's
  Gemini 3.5 Pro delay is the substance).
- **Undated:** Anthropic's IPO filing lists ≈ $114.5B of compute commitments with Google Cloud (MarketBeat, 10/26).
  *Confirming*, if it is confirmed.
- **Next:** **tonight's report**; ad-tech and search remedy appeals (no dates found in this sweep).

### Positioning & sentiment
- **Analysts:**
  - consensus Buy (5 Strong Buy, 47 Buy, 4 Hold), **average target $425.04** (MarketBeat, 10/26);
  - StockAnalysis: $430.51 from 62 analysts (via TradingKey, 10/24);
  - Needham Buy $450 (10/8).
- **Insiders:** ≈ $2.47M sold in 90 days (small).
- **Crowding:** part of the AI-capex basket that sold off 10/22; options price a ≈ 6% move. Not extended (RSI 37.6).

### Thesis scorecard
| Pillar (falsifiable) | Expected | Status (dated) | Trend |
|---|---|---|---|
| Google Cloud grows ≥ 80% y/y | ≥ 80% | Q2 +82% ($24.8B); Q3 consensus $29.16B (+92%) | improving (tested tonight) |
| Search & other ≥ +15% | ≥ 15% | Q2 +17% | stable |
| Operating margin ≥ 33% | ≥ 33% | Q2 34% | stable |
| Free cash flow positive | > 0 | Q2 ≈ −$5.9B, the first negative | **weakening** |
| Funding without heavy dilution | equity ≤ a few % | $80B equity raise (6/1); long-term debt $46.5B → $98.2B | **weakening** |

- **Thesis-break exits (if ever held):**
  1. A second negative-FCF quarter together with a higher capex guide and no Cloud acceleration.
  2. A court-ordered structural remedy in search or ad-tech.
  3. Search revenue declining y/y.
- **Conviction:** Med on the business. FCF positive tonight with Cloud ≥ +90% would raise it. A higher capex guide with
  negative FCF would cut it to Low.

### What would make me wrong
- **A clean beat** gaps it through the 200-DMA and it never looks back. Waiting for a 2:1 retest costs the move.
- **A capex-and-dilution spiral:** FCF stays negative into 2027, more equity is issued, and $314.90 and ≈ $300 give way.
- **AI agents measurably eating Search.** Q3 Search growth below 12% would be the first data point.

### Sources
- levels.py (Yahoo chart API daily bars; Alpha Vantage calendar), run 2026-10-28, quotes 10:52 ET; zone check the same
  session; reaction history computed from the same bars
- [TradingKey: Alphabet Q3 preview, $315 support](https://www.tradingkey.com/analysis/stocks/us-stocks/262235520-alphabet-stock-forecast-q3-earnings-preview-cloud-capex-315-support-october-24-2026-tradingkey): 2026-10-24
- [OANDA: Alphabet Q3 2026 earnings preview](https://www.oanda.com/bvi-en/skills-and-insights/education/trading-asset-classes/shares/22102026-alphabet-q3-2026-earnings-preview-google-cloud-ai-capex-outlook/): 2026-10-22
- [OptionSlam: GOOGL earnings straddle](https://www.optionslam.com/earnings/straddle/GOOGL): fetched 2026-10-28
- [MarketBeat: Alphabet stock down 1.1%](https://www.marketbeat.com/instant-alerts/price-alphabet-nasdaq-googl-stock-price-down-11-heres-why-2026-10-26/): 2026-10-26
- [Alphabet: June 2026 equity capital raise press release (PDF)](https://s206.q4cdn.com/479360582/files/doc_news/2026/Jun/01/attachments/2026-June-Alphabet-Equity-Capital-Raise-Press-Release-PDF.pdf): 2026-06-01 (terms via search, 10/28)
- [GlobeNewswire / BFA Law: Alphabet securities class action](https://www.globenewswire.com/news-release/2026/10/28/3389972/0/en/goog-and-googl-stock-market-alert-alphabet-sued-for-securities-fraud-after-ai-issues-lead-to-4-stock-drop-contact-bfa-law-if-you-lost-money.html): 2026-10-28 (page returned 403; details via search)
- Zacks Cloud consensus $29.16B: web-search summary, 10/28 (exact page not pinned; treat as indicative)

---

## GOOGL — update 2026-10-19

**Verdict:** WATCH · the 9/24 levels are stale · re-research after the Q3 report (**≈ 10/27–10/28**, not confirmed) ·
**Conviction:** Med on the business, Low on the timing. The price is pinned to its moving averages, with a report
in about 7 sessions and October buying closed.

| | |
|---|---|
| Price | **$344.87** (2026-10-19, 10:35 ET, +1.3%); close $340.59 (10/16) |
| 20 / 50 / 200-DMA | $345.9 / **$344.4** (falling) / $341.1 — price is on all three |
| RSI(14) · ATR(14) | 48.8 · **$8.67 = 2.5% a day** · −15.6% from the 5/18 high of $408.61 |
| 9/24 Trigger A | "close > $345, stop $330, T1 $380": the price has crossed $345 several times since without follow-through. It is not a buy before the report anyway |
| Report | **≈ 10/28** after the close (Admiral Markets; Investing.com says 10/27 tentatively) · consensus EPS ≈ $3.04, revenue ≈ $127.4B |

**What the report has to answer (dated):** Q2 (July) raised 2026 capex to **$195–205B** from $180–190B and said 2027 will
"rise significantly". Q2 free cash flow was ≈ **−$5.9B**, it issued **$25B** of notes, and Gemini 3.5 Pro was delayed. The
stock fell 8.5% after that print. Positives: multi-GW TPU agreements with revenue mostly in 2027 (10-Q). The court did not
order an ad-exchange sale; appeals and EU/UK cases remain. Cantor and HSBC kept Buy at $420 (10/12).

**Fit:** it would be a third AI-capex-driven line next to AMD and ARM. It needs to beat the weakest holding to get a slot.

**Sources:** Yahoo chart API GOOGL 1y daily, fetched 2026-10-19 10:35 ET · [Investing.com, 10/16: stalled near the 200-day before Q3](https://www.investing.com/news/stock-market-news/alphabet-stock-analysis-stalled-near-200day-average-ahead-of-q3-earnings-93CH-4954685) · [Admiral Markets: Q3 2026 preview](https://admiralmarkets.com/education/articles/shares/alphabet-stock-q3-2026-earnings-preview) · [Finbold, 10/12: analyst targets](https://finbold.com/wall-street-analysts-update-google-googl-stock-price-target-for-12-months/).

---

## GOOGL — Alphabet Inc. — deep dive 2026-09-24

**Verdict:** WATCH (not BUY today) · **Conviction:** Med — right company, wrong entry. Price is *below* its
50-DMA and sitting *on* its 200-DMA, and the reason it fell is a thesis question, not noise. Reward/risk to
the first real resistance is ~1.3:1, under the 2:1 minimum.

| | |
|---|---|
| Price | **$337.83** (2026-09-23 close, −3.80% on the day); $336.00 pre-market 2026-09-24 |
| 50-DMA / 200-DMA | **$345.07** / **$337.95** — price is below the 50 and *at* the 200 |
| 52-wk high / low | $408.61 / $235.84 · ATH close $402.12 (2026-05-13) |
| Off the high | **−17.3%** |
| RSI(14) | **unverified** — sources conflict (43.8 vs 56.0); no primary confirmation |
| Entry zone | **none today.** Trigger A: close > $345 (50-DMA reclaim). Trigger B: $300–310 flush |
| Invalidation (stop) | $318 for a buy at spot — but see R/R below |
| Target 1 / 2 | $360 (failed resistance 9/22) / $428 (consensus 12-mo PT) |
| Reward/risk (T1, at spot) | **1.33 : 1** ✘ — below the 2:1 floor |
| Reward/risk (Trigger A) | entry ~$346, stop $330, T1 $380 → **2.1 : 1** ✓ |
| Size if triggered | $400 = 10.9% of sleeve (within PLAN §1's 8–15%), **half now / half on confirmation** |
| Timeframe | months (not days) |
| Next earnings | **2026-10-27** after close (~24 trading days out — *outside* the 10-day blackout) |

### Thesis
Alphabet is the cheapest high-quality name in the AI platform layer: 24% revenue growth, 34% operating
margin, and a cloud business compounding at 82% — at ~25x forward earnings, roughly its own 5-year average
and in line with MSFT. The bear case is not valuation, it is that AI agents disintermediate the ad auction
that funds everything. That is a real, live question, and it is why the stock is down 17%, not a mispricing
to be scooped up on a hunch.

### Chart & technicals
The setup contradicts "it seems down, it might come up shortly":
- **Below the 50-DMA ($345.07)** — the plan's own dip-buy rule is "a satellite *at* its 50-DMA with the
  thesis intact". Below it is the opposite setup.
- **Sitting on the 200-DMA ($337.95)** — the last major support. It either holds here or the next visible
  reference is far lower; there is no well-defined support between here and the $235.84 52-week low.
- **Failed at ~$360 on 2026-09-22**, then −3.8% on 9/23. That is a lower high followed by distribution.
- 20-DMA and RSI(14) could not be verified from a consistent source — flagged, not guessed.

### Fundamentals (Q2 2026, reported 2026-07-22)
- Revenue **$119.8B, +24% YoY** — 12th straight quarter of double-digit growth
- Operating margin **34%** (+2pp YoY); operating income +30%
- Google Cloud **$24.8B, +82% YoY**; cloud operating income $8.8B vs $2.8B a year earlier
- Non-GAAP EPS **$2.85** (GAAP $9.11 is inflated by a one-time $99B equity gain — ignore it)
- Forward P/E **~25.2x**; trailing **16.95x**. 5-yr average trailing P/E ~25x, so it is not expensive
- **Capex guided up to $195–205B** for FY26 (from $180–190B) on the Q2 call — the standing overhang

### News & catalysts
- **2026-09-23 — breaking** — GOOGL −3.8% as Meta's "Muse" AI agent hit ~2.8M downloads in 12 days, the
  fastest adoption since ChatGPT. The fear is direct: agents that complete tasks bypass the ad auction.
- 2026-09-22 — neutral/breaking — failed at $360 resistance on Gemini-spend-vs-growth concerns
- 2026-09-03 — **confirming** — judge rejected DOJ's push to force an AdX divestiture. A genuine win, and
  notably the stock did *not* hold the gain
- 2026-07-22 — breaking — capex guide raised; stock fell on the print
- Search antitrust remedies remain on appeal (both sides); no decision date
- **2026-10-27** — Q3 earnings, the next real catalyst

### Positioning & sentiment
Consensus **Strong Buy**, average 12-month target **~$428** (range $340–515) across ~62 analysts. No analyst
target changes could be confirmed in the September window — the most recent dated moves are from the July
earnings reaction (Morgan Stanley cut to $400, Wedbush held $445). So the Street has not yet re-rated for
the Muse narrative; that cuts both ways.

### What would make me wrong
- A close back above **$345** (50-DMA) on volume — the downtrend is over and I was too cautious (this is
  Trigger A; I buy it there)
- Muse adoption stalls, or Q3 on 10/27 shows Search revenue accelerating anyway
- Conversely: a **close below $330** with the 200-DMA lost puts $300–310 in play quickly, and below that
  there is very little structure

### The behavioural note
The client has traded GOOGL three times before, all in June 2026: 6/3→6/5, 6/15→6/16, 6/22→6/29. Average
hold **3 days**, total profit **+$10.31** on six fills. This request has the same shape — no level, no
horizon, "might come up shortly." That pattern is what the 8/12 reset was meant to end.

### Sources
- [stockanalysis.com/stocks/googl](https://stockanalysis.com/stocks/googl/) — price, MAs, P/E, 2026-09-23/24
- [Alphabet Q2 2026 results](https://abc.xyz/investor/news/news-details/2026/Alphabet-Announces-Second-Quarter-2026-Results-2026-Y3uQ6H4ZJa/default.aspx) — 2026-07-22
- [Invezz — Alphabet falls 3% as Meta's Muse raises competition](https://invezz.com/ca/news/2026/09/23/alphabet-stock-falls-3percent-as-metas-muse-ai-raises-competition/) — 2026-09-23
- [Bloomberg — Meta's Muse drags down stocks that depend on consumer inertia](https://www.bloomberg.com/news/articles/2026-09-22/meta-s-muse-drags-down-stocks-that-depend-on-consumer-inertia) — 2026-09-22
- [Motley Fool — Google's latest antitrust ruling is a big win](https://www.fool.com/investing/2026/09/03/opinion-googles-latest-antitrust-ruling-is-a-big-win-for-alphabet-investors/) — 2026-09-03
- [CNBC — GOOGL sinks on 2026 capex hike](https://www.cnbc.com/2026/07/22/google-earnings-q2-goog-live-updates.html) — 2026-07-22

**Unverified / carried caveats:** RSI(14); 20-DMA; the 10/27 earnings date is from secondary calendars, not
Alphabet's own IR page; peer forward P/Es were inconsistent across sources and are not used above.
