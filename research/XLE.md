# XLE — Energy Select Sector SPDR ETF — research log

One file per ticker; newest entry first. Each entry is dated; numbers are as of that date.

Entries:
- 2026-10-28 (deep dive, v5 trading-pot candidate, levels.py-checked; XOM/CVX preview)
- 2026-10-23 (deep dive, non-AI diversifier screen)

---

## XLE — Energy Select Sector SPDR ETF — deep dive 2026-10-28

**Verdict:** WATCH (conditional). **This is a v5 trading-pot candidate and cannot be bought under v3**: PLAN §1 allows at most one
non-AI satellite, and TTWO holds it. The client has also committed to no buys or sells before 11/2. The board alert is **$63.60**
(zone $62.80–63.60). It counts only if Brent's front month is at or above $100 that day and the drop is not a peace headline.

**Conviction:** Low.
- The 10/23 target ($68.78) was taken out on 10/23, and the zone never printed.
- XLE set an all-time high of $69.86 on 10/26 and sits 2% under it.
- The next ten days turn on Iran. Strikes after the midterms (WSJ, via The National 10/28) would lift the oil premium. No strikes,
  or a Qatar-brokered deal, would unwind it (ING, 10/28).
- That unwind is the likeliest way the zone prints, and it voids the zone.

| | |
|---|---|
| Price | **$68.47**, from levels.py at 2026-10-28 10:52 ET ($68.50 at 11:07 ET). Last close $68.21 (10/27, −2.1%). All-time high **$69.86** (10/26 intraday; the levels.py 52-week high). Prices are split-adjusted |
| Entry zone | **$62.80–63.60**. Set the alert at $63.60, then buy with a market order. This is the early-October base the leg started from: closes of $62.82 (10/2), $63.45 (10/5) and $63.36 (10/7), and lows of $62.93 (10/6) and $63.04 (10/7) (Yahoo bars). It sits above levels.py swing support at $61.31 (8/26) and $60.95 (9/29). **The zone is valid only if all of these hold:** (1) Brent's ICE front month is at or above $100 that day (use the ICE front month, not Yahoo BZ=F in a roll week: see the flags); (2) the drop is not a ceasefire, deal, Hormuz-reopening or blockade-lifting headline; (3) the plan allows the buy (v5 adopted, or v3 changed); (4) it is not an FOMC day or a data morning. Re-derive it at every weekly check, since zones go stale after two weeks, and on any new high |
| Invalidation (stop) | **$60.70**, under the levels.py swing lows of $61.31 (8/26) and $60.95 (9/29). That is 1.53–2.12 ATR and 3.3–4.6% under the zone. For events, see the thesis-break exits: exit at the next open |
| Target 1 / 2 | **$69.70**: the 10/27 high, which with $69.72 (10/23) and $69.86 (10/26) forms a three-session cap. levels.py prints "resistance above: none in 6 months" only because the cap is too recent to count as a swing; its 52-week high is $69.86 / **none**: there is no resistance above the all-time high, so any T2 needs a measured move written by the desk |
| Reward/risk (T1) | **3.29 / 2.60 / 2.10 : 1** at the zone's low / mid / high (levels.py ✓). On the strict reading, T1 is $66.17: the 9/10 swing high plus the 10/15–10/22 lows, which a fall to $63 would break. That gives **1.60 / 1.19 / 0.89 ✘**. Buying today pays 0.50–0.64:1 ✘ |
| Size | **$190** in one fill = 5.5% of $3,426, ≈ 3.0 sh at the mid. Risk to the stop is **$7.52 = 0.2%** (cap $69). A −4% ceasefire gap from $63.20 would open at ≈ $60.67, right at the stop, a loss of ≈ $7.6 |
| Timeframe | Weeks to about 3 months, and only while the war premium lasts |
| Next earnings | ETF: no buy blackout. Holdings, from the Alpha Vantage calendar in levels.py's cache unless noted: **XOM (23.98%) and CVX (18.21%) report Fri 10/30 before the open** (levels.py: "2 sessions … inside the 3-session buy blackout"). Also MPC 11/3 before the open, WMB 11/2 after the close, COP (7.18%) 11/5 before the open and EOG 11/5 after the close. PSX reported 10/28 before the open |
| Earliest buy date | **None under v3**, and never before 11/2. If v5 is adopted, the first session the trading pot opens, after the zone is re-derived and the Brent and ceasefire conditions are met |

T1 convention: as in the 10/28 PM entry. T1 is the nearest real resistance above today's price (PLAN §3b), and the strict
reading is shown beside it.

**levels.py, 2026-10-28** (the only source of technicals in this entry)
```
XLE  $68.47 (2026-10-28 10:52 ET); last daily bar 2026-10-28 close $68.47
  20/50/200-DMA  66.46 / 64.70 (rising) / 58.51 (rising)   price vs 50 +5.8%, vs 200 +17.0%
  RSI(14) 61.9   ATR(14) $1.37 = 2.0% a day   52-wk 43.19–69.86 (-2% from the high)
  Trend: above a rising 200-DMA
  Chase guard: ok
  Next report: not in the 3-month calendar (ETF, or more than 3 months away)
  Swing support below: 61.31, 60.95, 57.11   resistance above: none in 6 months

BZ=F  $112.07 (2026-10-28 10:51 ET); last daily bar 2026-10-28 close $112.07
  20/50/200-DMA  107.38 / 102.26 (rising) / 91.94 (rising)   price vs 50 +9.6%, vs 200 +21.9%
  RSI(14) 60.7   ATR(14) $4.18 = 3.7% a day   52-wk 58.72–126.10 (-11% from the high)
  Swing support below: 97.36, 96.56, 96.07   resistance above: 112.69, 126.10
CL=F  $102.68 (2026-10-28 10:51 ET) · RSI 60.1 · ATR $4.30 = 4.2% · 50/200-DMA 93.98 / 85.93 (rising)
XOM   $182.03 (11:01 ET) · RSI 67.2 · 52-wk high 184.88 · Next report 2026-10-30 before the open (2 sessions; EPS est. 3.9) ✘ blackout
CVX   $230.09 (11:01 ET) · RSI 67.8 · 52-wk high 234.08 · Next report 2026-10-30 before the open (2 sessions; EPS est. 4.78) ✘ blackout
```
**Zone checks, 11:07 ET**
```
$ levels.py XLE --zone 62.80-63.60 --stop 60.70 --target 69.70 --size 190 --sleeve 3426
  Setup: zone 62.80–63.60, stop 60.70, T1 69.70
    at low      62.80: R/R 3.29:1, stop 1.53 ATR (3.3%)   ✓
    at mid      63.20: R/R 2.60:1, stop 1.82 ATR (4.0%)   ✓
    at high     63.60: R/R 2.10:1, stop 2.12 ATR (4.6%)   ✓
    size $190 ≈ 3.0063 sh at the mid; risk to stop $7.52 = 0.2% of $3,426   ✓ ≤ 2%
    price 68.50 is +7.7% above the zone — wait for the alert at 63.60

$ levels.py XLE --zone 62.80-63.60 --stop 60.70 --target 66.17 ...      (strict reading)
    at low 1.60:1 ✘ · at mid 1.19:1 ✘ · at high 0.89:1 ✘
$ levels.py XLE --zone 68.30-68.50 --stop 66.10 --target 69.70 ...      (buying today)
    at low 0.64:1 ✘ · at mid 0.57:1 ✘ · at high 0.50:1 ✘
$ levels.py XLE --zone 64.95-65.20 --stop 62.90 --target 69.70 ...      (50-DMA retest, rejected)
    at low 2.32:1 but stop 1.50 ATR ✘ (rounds up; 1.496) · at mid 2.13:1 ✓ · at high 1.96:1 ✘
```
The 50-DMA retest fails at both edges and is 25 cents wide, so it is not carried.

Chart: `levels.py XLE --chart` (10/28, scratchpad). It shows the leg up from the early-October base to the 69.7–69.9 cap, the
zone sitting on that base just under the 50-DMA ($64.70), the stop under the September lows, and the rising 200-DMA far below.
It agrees with the computed levels.

## What changed since the 10/23 entry
**XLE:**
- Closes: $67.57 (10/22), $69.33 (10/23, +2.6%), $69.64 (10/26), then $68.21 (10/27, −2.1%) and $68.47 now.
  - The 10/23 high of $69.72 took out the old T1 ($68.78), and 10/26 set the all-time high of $69.86.
  - Energy shares fell more than 2% on 10/27 (desk backdrop; CNBC and AP closing reports).
  - The old zone ($62.80–63.35) never printed. The setup is re-derived with T1 at $69.70: the zone top rises to $63.60 and the
    stop is unchanged.
- Indicators: ATR from $1.382 to $1.37, RSI 63.1 to 61.9. 20-DMA $65.04 to $66.46, 50-DMA $64.17 to $64.70, 200-DMA $58.06 to
  $58.51.

**Brent:**
- $112.76 on 10/22 (10/23 entry).
- **$116.72 settlement on 10/23, the highest since 4/29** (CNBC via search summary; the Yahoo bar agrees).
- $115.81 on 10/26, then $113.88 on 10/27, about −1.6% (The National).
- On 10/28: $114.87 (+0.87%) at 2 pm UAE (The National), $115.48 at 09:00 GMT (Engine), and $112.07 on Yahoo BZ=F at 10:51 ET.
  The last one looks like a contract roll (see the flags).

**Iran:**
- No ceasefire. The U.S. blockade stays: Ambassador Waltz said on 10/23 it can hold "for the foreseeable future" (CBS).
- Iran offers to reopen Hormuz if the blockade is lifted (10/24, CBS).
- Trump framed it as "deal or finish them off" (10/23–10/25), and said strikes would wait until after 11/3 (10/24) (CBS).
- The WSJ reported that the U.S. told Gulf states to prepare for a possible campaign after the midterms (The National, 10/28).
- Qatar gave Iran a new draft: a seven-day timeline of daily confidence-building steps. Iran is expected to reply by the end of
  the week (Reuters, via Engine and The National, 10/28).
- Saudi, Pakistani and Turkish officials met Iranian officials in Tehran on 10/26 (CBS).

**Houthi attacks:**
- Claims of strikes on Ras Tanura (550,000 b/d; not confirmed by Saudi Arabia) and on Abha airport.
- A missile aimed at Taif was intercepted on 10/28 (The National, Engine).

**Forecasts:**
- UBS raised its oil forecasts and expects Brent near $110 through year-end (The National, 10/28).
- ING says the premium can unwind without a deal if there are no strikes after 11/3 (Tradingpedia, 10/28).

**Fund:** XOM plus CVX are 42.19% of the fund (SSGA, 10/27), up from 41.9% (10/21).

## Thesis
**What XLE hedges:** the shock that hurts the rest of this account, oil-driven inflation that keeps the Fed hiking.
- The Fed hiked in September, and markets price about a 75% chance of a December hike (desk backdrop, 10/28). The 10-year
  Treasury yield is 5.02%.
- XLE moved against chips in the 10/23 screen: −0.24 correlation with the SOX over 60 days (data to 10/22; not re-measured).

**What the price carries:** a war premium.
- Brent was ≈ $72 before the war (10/23 entry) and is ≈ $115 now.
- Both 2026 ceasefires cut XLE by 15–16% (10/23 entry).

**The rule-compliant trade:** buy a pullback to the October base that peace did not cause, with the stop under the September lows.
- If peace causes the pullback, the thesis has broken and the zone does not count.
- If war resumes after 11/3, XLE likely breaks above $69.86, where there is no 2:1 buy until the desk writes a target.

## Earnings preview: XOM and CVX, Fri 10/30 before the open (section A; 42.2% of the fund)
1. **Date and time:** both report 2026-10-30 before the open (levels.py and the Alpha Vantage calendar). Nothing is held, and no
   buy is allowed before 11/2, so there is no pre-report decision to make.
2. **Consensus:**

   | | XOM | CVX |
   |---|---|---|
   | EPS (Zacks, 10/27) | **$3.90** (+107.5% y/y). Two revisions up and one down in 7 days | **$4.78** (+158.4% y/y), revised up 0.8% in 7 days |
   | EPS (other sources) | AlphaStreet $4.03, 18 analysts (search summary). Range $3.00–4.20 (search summary) | AlphaStreet $4.83, 21 analysts (search summary) |
   | Revenue (Zacks) | $102.98B | $60.5B (+21.6%) |
   | Metric that moves the stock | Refining (Energy Products) margins: **+$4.5B** vs Q2 in the 10/16 8-K, against liquids prices −$1.3B and **timing effects −$2.5B** (upstream −0.7, Energy Products −1.9). Q2 adjusted earnings were $14.7B | Downstream earnings: consensus **$5.1B** vs $1.1B a year ago. Turnaround costs guided at $175–225M (Zacks) |
   | Track record | Beat in 3 of the last 4 quarters, average surprise 2.43% (Zacks) | Beat in 4 of the last 4, average 18.7% (Zacks) |

3. **Implied move:** XOM **±5.0%**, CVX **±4.6%** (EarningsWatcher, as of 10/27).
   - Earlier readings were ±5.4% for XOM (10/23) and ±6.3% for CVX (10/10) (search summary), so the implied moves have come in.
   - Weighted by fund share, the two imply ≈ ±2.0% for XLE (≈ $1.40, ≈ 1.0 ATR) if both move the same way (my arithmetic).
   - The zone is 7.7% below the price, so the reports alone are unlikely to reach it.
   - Nothing is held. A $190 position would have ≈ $4 at stake.
4. **Scenarios:**

   | Scenario | What has to happen | Likely reaction | Action written now |
   |---|---|---|---|
   | Bull | Refining windfall above the 8-K's +$4.5B, a buyback raised, and Brent holds above $110 | XLE clears $69.86 | No buy: there is no resistance for a T1. The desk writes a measured move or waits for a pullback |
   | Base | In line, with timing effects as guided | XLE follows Brent and the Iran headlines | Alert unchanged. Re-run levels.py on the 10/30 close |
   | Bear | A miss on timing effects or upstream, or weak Q4 commentary | XLE −1 to −2%, still well above the zone | Alert unchanged. A falling price is not a reason to move the zone up |

5. **History** (close to close on report day, from EarningsWatcher 10/27; gaps not listed):
   - XOM: −1.0% (7/31/26), −1.0% (5/1/26), +0.6% (1/30/26), −0.3% (10/31/25).
   - CVX: +2.4%, −1.4%, +3.3%, +2.7% on the same dates.
6. **Decision:** no position, so nothing to decide on report night. The alert stands with its conditions. After 10/30, re-check
   T1 if XLE prints a new high.

## Thesis scorecard
| Pillar (falsifiable) | What was expected | Status (dated) | Trend |
|---|---|---|---|
| Brent front month ≥ $100 | ≥ $100 | **$114.87** (The National, 10/28 2 pm UAE). Yahoo BZ=F $112.07 (10:51 ET, likely rolled) | stable (−1.6% on 10/27, +0.9% on 10/28) |
| No ceasefire, Hormuz reopening or blockade lift | none | None as of 10/28. Qatar's draft is with Iran, with a reply due ≈ 10/30. Tehran meeting on 10/26. The WSJ reports strikes planned after the midterms | at risk |
| Supply stays disrupted | Gulf flows below normal | UBS says flows "have not yet fully normalised" (10/28). A 10/21 headline says non-Iran Middle East exports are back to pre-war levels using Hormuz alternatives (The National; headline only). Houthi claims on Saudi sites (10/27–28) | weakening |
| Sector earnings deliver | XOM ≥ $3.90, CVX ≥ $4.78 (Zacks, 10/27) | Reports on 10/30. FactSet (10/23): energy EPS estimates revised up since 9/30 | pending |
| Moves against chips | negative correlation with the SOX | −0.24 over 60 days to 10/22 (screen). Not re-measured | unknown |

**Thesis-break exits.** Any one ends a position at the next open, or cancels the alert:
1. A signed U.S.–Iran ceasefire or deal, Hormuz reopened, or the U.S. blockade lifted.
2. Iran formally accepts the Qatari draft, or a U.S.–Iran framework is announced.
3. Brent's front month settles under $100.

**Disconfirming evidence:**
- Non-Iran Gulf exports are reportedly back to pre-war levels through bypass routes (10/21 headline).
- Russia lifted its diesel export ban earlier in October, and the ICE gasoil crack is at its lowest since early October (Tradingpedia, 10/28).
- XLE fell 2.1% on 10/27 while Brent fell only about 1.6%.

**Conviction:** Low. It rises if the midterms pass, the premium holds, and XLE pulls back to the base on chip strength instead.
It goes to zero on any of the break events.

## Chart & technicals
Source: levels.py, 10/28 10:52 ET.
- **Trend:** above a rising 20-DMA ($66.46), 50-DMA ($64.70) and 200-DMA ($58.51): +5.8% and +17.0% over the 50- and 200-DMA.
  Higher highs since the 7/1 low ($52.62, levels.py swing low).
- **Momentum and volatility:** RSI 61.9, chase guard ok. ATR **$1.37 = 2.0%**, so 1.5 ATR = $2.06.
- **Swing lows (levels.py):** 5/7 $55.13 · 5/29 $55.99 · 7/1 $52.62 · 8/7 $57.11 · 8/26 $61.31 · 9/29 $60.95.
- **Swing highs:** 4/30 $59.84 · 5/20 $61.70 · 6/3 $59.38 · 7/24 $60.45 · 8/20 $64.70 · 9/10 $66.17. All are below the price.
- **Resistance:** none listed. The 69.70–69.86 cap (10/23–10/27) is not a swing yet, because a swing needs five bars after it.
- **Leaders are near their highs:** XOM (RSI 67.2, 52-week high $184.88) and CVX (RSI 67.8, $234.08) both pass the chase guard.
- **Brent (levels.py BZ=F):** RSI 60.7, ATR $4.18 = 3.7% a day. 50-DMA $102.26 and 200-DMA $91.94, both rising. Swing support at
  $97.36, $96.56 and $96.07.
  - A full unwind toward the swing lows would breach the $100 condition, which ties the price and event exits together.

## Fundamentals
- **Fund** (SSGA, 10/27): AUM $45.24B. Expense ratio 0.08%. 21 holdings: oil, gas and consumable fuels 91.87%, equipment and
  services 8.13%.
- **Top 10 holdings** (SSGA, 10/27): XOM 23.98 · CVX 18.21 · COP 7.18 · MPC 4.67 · PSX 4.41 · VLO 4.27 · WMB 4.22 · EOG 4.07 ·
  SLB 3.86 · KMI 3.19 (%).
- **Valuation and yield** (SSGA, 10/27):
  - P/E 18.47 trailing (index) and **12.28 forward**. P/B 2.75. Price/cash flow 9.49.
  - Index yield 2.31%. 30-day SEC yield 2.22% (10/26).
  - Estimated 3–5-year EPS growth 12.96%.
- **stockanalysis (10/28, 11:02 ET):**
  - $68.51. AUM $45.85B. P/E 18.07, forward 11.23.
  - Yield 2.22% ($1.52 a year). The last ex-dividend date was 9/21/2026.
  - One-year total return 59.5%. Beta 0.50.
  - It lists 24 holdings against SSGA's 21: a conflict between sources.
- **Earnings path:**
  - FactSet (10/23): S&P 500 Q3 blended growth 29.5%. Energy is among the leaders, with estimates revised up since 9/30 (no
    sector figure given).
  - FactSet (10/12, per the 10/23 entry; not re-fetched): sector EPS growth turns negative in Q2 and Q3 2027 (−21.3% and −19.5%).
    The market already models the war earnings fading.

## News & catalysts
**Last 30 days**
- 10/5: Houthi strike on Saudi Arabia's East-West pipeline (10/23 entry). *Confirming.*
- 10/16: XOM 8-K shows refining margins +$4.5B against Q2 (fetched 10/28). *Confirming.*
- 10/20–22: U.S.–Iran deal claims called "inaccurate". Brent $108.79 on 10/20, then $112.76 on 10/22 (10/23 entry). *Neutral.*
- **10/23:** Brent settles at $116.72, the highest since 4/29. Trump says "finish it off or let it wither". *Confirming.*
- **10/24–25:** Trump says strikes wait until after 11/3. Iran offers to reopen Hormuz if the blockade lifts (CBS). *Breaking risk.*
- 10/26: Saudi, Pakistani and Turkish officials meet Iranian officials in Tehran (CBS). *Breaking risk.*
- 10/27: Brent −1.6% and energy shares down more than 2% (The National; desk). *Neutral.*
- **10/28:** the WSJ reports post-midterm strike preparations, which is *confirming*. Qatar's draft goes to Iran, with a reply due
  ≈ 10/30, which is *breaking risk*. Houthi attacks (Abha; Taif missile intercepted). UBS sees Brent ≈ $110 to year-end. *Mixed.*

**Next 90 days**
- **10/28:** FOMC at 2:00 ET (desk).
- **10/30:** XOM and CVX Q3.
- ≈ 10/30: Iran's reply to Qatar.
- 11/1: OPEC+ meeting (10/23 entry; not re-verified).
- 11/2–11/5: WMB, MPC, COP and EOG report.
- **11/3: U.S. midterms**, the pivot for the war premium.
- Early November: the U.S. force is fully in place, per one report (search summary).
- Wednesdays: EIA inventory data. The API showed crude −2.03M bbl in the week to 10/23 (Engine).
- December FOMC: date unverified.

## Positioning & sentiment
- **Flows:** no October XLE flow figure was found (unverified).
- **Futures and fund managers** (10/23 entry; not re-fetched): CTAs were 100% long Brent and WTI (Kpler, 10/20), and fund managers
  were not crowded in oil (BofA FMS, October).
- **The holdings are stretched but pass the guard:** XOM and CVX have RSI near 67, within 2% of their highs (levels.py).
- **Read:** the futures side is crowded and the equity side is not. A peace headline hits futures first.

## What would make me wrong
- **Escalation after 11/3.** XLE leaves $69.86 behind and never returns to $63. The plan has no 2:1 trade at an all-time high;
  that is the cost of the rule.
- **No strikes and no deal.** The premium bleeds out slowly (ING). XLE drifts into the zone while Brent is still above $100, the
  zone fires, and the decline continues. The stop at $60.70 handles that.
- **A deal or ceasefire:** a fast fall of 15–16%, as in April and June (10/23 entry). Do not buy it.
- **Demand and supply:** Gulf flows normalising, Russian diesel returning, and a Fed hiking into a slowdown.

## Sources
- levels.py (Yahoo chart API; Alpha Vantage calendar). Runs: XLE, BZ=F and CL=F at 10:52 ET; XOM and CVX at 11:01 ET; zone
  checks and `--chart` at 11:07 ET (2026-10-28).
- The National, oil up on Houthi strikes and the U.S. threat to renew the war, 2026-10-28 — https://www.thenationalnews.com/business/energy/2026/10/28/oil-prices-up-due-to-houthi-strikes-and-us-threat-to-renew-iran-war/
- Engine, Brent and the Qatar draft, 2026-10-28 — https://www.engine.online/news/brent-inches-lower-as-qatar-presents-iran-with-new-peace-deal-8354
- Tradingpedia, ING on the premium, 2026-10-28 — https://www.tradingpedia.com/2026/10/28/brent-crude-holds-premium-as-markets-await-iran-policy/
- CBS live updates, 10/23–10/26 entries, fetched 2026-10-28 — https://www.cbsnews.com/live-updates/iran-war-trump-us-oil-gas-prices-strait-of-hormuz-midterms/
- CNBC, 10/23 and 10/28 oil reports (search summaries; the pages returned 403) — https://www.cnbc.com/2026/10/23/oil-price-brent-wti-iran-war-saudi-arabia.html · https://www.cnbc.com/2026/10/28/oil-price-today-wti-brent-hormuz.html
- SSGA XLE fund page, data 2026-10-26/27 — https://www.ssga.com/us/en/intermediary/etfs/state-street-energy-select-sector-spdr-etf-xle
- stockanalysis XLE and holdings, 2026-10-28 — https://stockanalysis.com/etf/xle/ · https://stockanalysis.com/etf/xle/holdings/
- XOM 8-K, 3Q26 factors, 2026-10-16, fetched 2026-10-28 — https://www.sec.gov/Archives/edgar/data/2115436/000211543626000013/f8k3q991101626.htm
- Zacks via The Globe and Mail, XOM Q3 preview, 2026-10-27 — https://www.theglobeandmail.com/investing/markets/stocks/CVX/pressreleases/8479008/exxonmobils-q3-earnings-on-deck-should-you-bet-on-the-stock/
- Zacks via Yahoo, CVX Q3 preview, 2026-10-27 — https://finance.yahoo.com/markets/stocks/articles/chevron-eyes-q3-earnings-beat-111100910.html
- AlphaStreet XOM and CVX previews (search summary; the pages returned 403) — https://news.alphastreet.com/exxon-mobil-xom-q3-2026-preview-eps-est-4-03-reports-october-30/ · https://news.alphastreet.com/chevron-cvx-q3-2026-preview-eps-est-4-83-reports-october-30/
- EarningsWatcher implied moves, as of 2026-10-27 — https://earnings-watcher.com/wiki/xom-implied-move · https://earnings-watcher.com/wiki/cvx-implied-move
- FactSet earnings season update, 2026-10-23 — https://insight.factset.com/sp-500-earnings-season-update-october-23-2026
- 10/23 entry below, for values marked as such.

---

## XLE — Energy Select Sector SPDR ETF — deep dive 2026-10-23 (non-AI diversifier screen)

**Verdict:** WATCH · alert at **$63.35** · **Conviction:** Low. The hedge is real: XLE moves against the S&P and the chips.
But at $67.57 it is 1.8% under its all-time high, so no entry gives 2:1 today. The price also carries a war premium that
both 2026 ceasefires erased (−15.8% and −14.7%). The likeliest route down to the buy zone is the peace headline that breaks
the thesis, so the zone only counts on a dip that has nothing to do with peace.

Data: the latest completed session is Thu 2026-10-22. Yahoo bars were fetched 2026-10-22 22:13 UTC (01:13 EEST Friday),
before Friday's session opened. The fund's current name is "State Street Energy Select Sector SPDR ETF" (SSGA, 10/21).
Prices are split-adjusted (2-for-1 on 2025-12-05).

| | |
|---|---|
| Price (date) | **$67.57** (2026-10-22 close, −0.9%). Same day: all-time high **$68.78**, low $66.29, volume 41.6M (1.3× the 20-day average). Brent rose 3.6% that day |
| Entry zone | **$62.80–63.35**, from 11/2. Alert at $63.35, then a market order. Valid only if all three hold: (1) the drop is not a US–Iran ceasefire, Hormuz-reopening or blockade-lifting headline; (2) Brent's front month is ≥ $100 that day; (3) the client has agreed plan change (a), because TTWO holds the one non-AI slot (PLAN §1). Not on FOMC day or a data morning. The zone expires at the 11/6 weekly check; recompute it if XLE makes a new high first |
| Invalidation (stop) | **$60.70**, under the 9/29–10/1 swing lows ($60.95 / $61.04) that the October leg started from. That is $2.38 under the zone mid = **1.72 ATR** (1.52 ATR from the zone bottom). **Event:** a signed ceasefire, Hormuz reopening, or the US blockade lifted → exit at the next open, at any price. Hard exit −15% from cost = $53.62 at a $63.08 fill (the stop is above it) |
| Target 1 / 2 | **$68.78** (the 10/22 all-time high, a high-volume reversal bar) / **$70.70** (equal-leg projection: the 10/1→10/22 leg of +$7.74 added to a $63 low. A projection, not a resistance) |
| Reward/risk (T1) | **2.39 : 1** at the zone mid $63.08 (5.70 / 2.38). 2.05 at $63.35, 2.85 at $62.80. From today's $67.57 it is **0.45 : 1** (stop $64.90 under the 20-DMA), so no buy at today's price |
| Size | **$270 = 8.0% of the $3,387 sleeve, one fill → 4.28 sh at $63.08.** Risk to the stop **$10.2** (0.3% of the sleeve; the cap is $68). A −4% ceasefire gap from $63.08 opens at ≈ $60.56, a loss of ≈ $10.8. No second half: an add "on confirmation" above $66.30 would be 0.4:1 to $68.78 |
| Timeframe | Weeks to ≈ 3 months. The hedge lasts only as long as the war premium |
| Next earnings | ETF: none, so the 3-session blackout does not apply. Holdings: **XOM and CVX (41.9% of the fund) report Fri 10/30**, before the 11/2 window (XOM confirmed by the company; CVX per an aggregator, not checked on Chevron's site). **COP (7.1%) reports Thu 11/5** (company release 9/24). Next distribution ≈ late December (pattern from past dates, unverified) |

## Thesis
**Why it is on the list.** The October losses came from one factor, AI capex. XLE behaves close to the opposite. Over the
60 sessions to 10/22, its daily correlation with the SOX was **−0.24** and its beta to the S&P 500 **−0.56**. Over 250
sessions the figures were −0.19 and −0.42. On the three chip-crash days it returned +0.6% (10/14), +2.5% (10/16) and −0.9%
(10/22), while the SOX fell 4.3%, 3.8% and 6.7%. It protects against the shock that hurts everything else: oil-driven
inflation and a Fed forced to tighten. September CPI was 3.7% with gasoline up 34.2% y/y (10/14), and, per 10/14 CPI coverage, the
Fed hiked in September for the first time since 2023 (not checked against the Fed's own statement: unverified).

**Why not now.** The price embeds a war premium. Brent closed at **$72.48 on 2/27/2026**, the last close before the
war, and at **$112.76 on 10/22** (+56%). Twice this year a ceasefire took most of that premium out, and both times XLE fell
15–16% from its high:

| Episode | Brent | XLE |
|---|---|---|
| 4/8/2026: two-week US–Iran ceasefire | $109.27 → $94.75 (**−13.3% in one day**) | **−3.5%** that day, while the S&P rose 2.5% |
| 3/30 → 4/17/2026: the April ceasefire, Hormuz partly reopened | — | high $63.46 → low $53.41, **−15.8%** in under three weeks |
| 5/20 → 7/1/2026: talks, the 6/17 MOU, oil back at pre-war levels by early July | weekly close $103.54 (5/22) → $71.80 (7/2) (front month, includes contract rolls) | high $61.70 → low $52.62, **−14.7%** in six weeks |
| 5/6/2026 (cause not checked) | −7.8% | −4.1%, S&P +1.5% |

**Applied to today:**
- **One headline day:** −3.5% to −4.1%, which is 1.7–2.0 ATR, takes $67.57 to about $64.8–65.2.
- **A full unwind like April or June:** −15% to −16% from the high, which is **$57.9–58.7**. That is where the rising 200-DMA
  ($58.06) sits.
- **All the way back to pre-war oil:** XLE closed at $53.22 on 7/2 and $55.92 on 2/27 with Brent near $72. That is
  **$53–56**, or −17% to −21% from here, unless sector earnings have re-rated it since.
- **Motive and timing:** the White House has a gasoline motive before the **11/3 midterms**, and Iran's seven-day ceasefire
  proposal is still "on the table" (Iran, 10/21–22).

**The trade that fits the rules.** Buy a pullback into the October pivot at $62.8–63.4 that peace did not cause, with
the stop under the September lows. That is 2.4:1 for about $10 of risk. If peace causes the pullback, it is not a dip but the
thesis breaking, and the 2026 record says the fall continues to the high $50s.

## Chart & technicals
Source: Yahoo 1y/2y daily bars, close 2026-10-22.
- **Trend:** up on every timeframe. The 20-DMA is $65.04 (+1.6% over 20 sessions), the 50-DMA $64.17 (+4.1%) and the
  200-DMA $58.06 (+3.6%). Price is +3.9%, **+5.3%** and **+16.4%** above them. Higher highs and higher lows since the
  6/24–7/1 low ($52.62–52.94).
- **Momentum and volatility:** RSI(14) **63.1** (67.4 on 10/21), which passes the chase guard. ATR(14) **$1.382 = 2.05%**
  a day.
- **52-week range:** $43.19 (2025-11-04) to **$68.78** (2026-10-22), an all-time high on split-adjusted prices.
- **Returns:** 5 days +1.5%, 1 month +8.3%, 3 months +13.3%, 6 months +18.6%, 1 year +55.9%. YTD +51.1% (2025 close $44.71).
- **Swing lows (6 months):** 7/1 $52.62, 8/7 $57.11, 8/26 $61.31, 9/22 $61.42, **9/29 $60.95**, 10/5 $62.05, 10/7 $63.04,
  10/15 $66.17, 10/22 $66.29.
- **Swing highs:** 5/20 $61.70, 8/20 $64.70, 9/10 $66.17, **10/22 $68.78**.
- **Support:**
  - $66.17–66.29: the 10/15 and 10/22 lows, and the 9/10 high, which broke on 10/13.
  - $65.0: the 20-DMA.
  - $64.2: the 50-DMA, about $65 by early November if the price holds.
  - **$62.9–63.5**: the 10/6–10/7 lows and the 10/2–10/5 closes, where the October leg started.
  - **$60.95–61.42**: the September lows.
  - $58.1 (200-DMA), then $57.1 (8/7 low).
- **Resistance:** **$68.78** only. It is an all-time high, with nothing above it. A breakout buy above it cannot be sized
  under the plan, because there is no real resistance to set a 2:1 first target against.
- **Warning bar on 10/22:** XLE opened at its high and closed −0.9%. Volume was the heaviest since 10/8, and Brent rose
  3.6% the same day. It was the first day this month that energy shares did not follow oil. The defensive money went to
  utilities (XLU +2.1%) and insurers (PGR +3.7%, ALL +3.2%, CB +2.5%) instead.
- **Top holdings stretched (10/22):** XOM RSI 70.3, CVX 71.5, COP 71.1, together 49% of the fund. Each would fail the
  chase guard on its own.
- **Brent (BZ=F):** $112.76 (10/22, +3.6%), RSI 69.2, 50-DMA $100.2, 200-DMA $90.9. Its 52-week range is $58.72
  (2025-12-16) to $126.10 intraday (4/30/2026). WTI was $99.14. Front-month rolls distort single days at month ends.

## Fundamentals
Source: SSGA fund page, data as of 2026-10-21 unless noted.
- **Fund:** AUM **$45.2B**. Expense ratio **0.08%**. 21 holdings: oil, gas & consumable fuels 92.3%, equipment & services
  7.7%.
- **Top 10 = 78.6% of the fund:** XOM 23.77% · CVX 18.12% · COP 7.08% · MPC 5.02% · VLO 4.82% · PSX 4.77% · WMB 4.15% ·
  EOG 3.99% · SLB 3.66% · KMI 3.21%.
  - XOM and CVX alone are 41.9%.
  - Refiners (MPC, VLO, PSX) are 14.6% and pipelines (WMB, KMI) 7.4%. Both damp the fund's sensitivity to the oil price.
- **Valuation:**
  - P/E 19.26 trailing, **12.38 forward (FY1)**. Index estimate of 3–5-year EPS growth: 13.07%.
  - P/B 2.76.
  - Price/cash flow 9.48, about a 10.5% operating-cash-flow yield. This is operating cash flow, not free cash flow.
  - **Free-cash-flow yield: unverified.** No dated source was found.
  - Yields: index dividend yield 2.36%, 30-day SEC yield 2.27%. Stockanalysis (10/22) shows a 2.25% yield, $1.52 a year.
- **Earnings (FactSet, 10/12):**
  - Q3 2026 energy-sector EPS growth is **+121.1% y/y**, up from 79.3% expected on 6/30. By sub-industry: refiners +462%,
    integrated +113%, E&P +60%, pipelines +8%, services −9%.
  - WTI averaged $85.68 in Q3, +32% y/y.
  - Projections: Q4 +117.1%, Q1'27 +86.7%, then **Q2'27 −21.3% and Q3'27 −19.5%**. Analysts already model the war earnings
    fading by mid-2027.
- **XOM's 10/16 8-K (Q3 versus Q2 factors):**
  - Refining margins **+$4.5B**, liquids prices −$1.3B, gas +$0.3B, timing effects −$2.5B. Q2 adjusted earnings were $14.7B.
  - So the war money is landing in refining margins more than in crude realizations.
- **Sensitivity to oil:** XLE's daily beta to Brent is 0.25 over 250 sessions and 0.28 over 60, with correlations of 0.61
  and 0.52. On an ordinary day a 10% Brent move is worth about 2.5–2.8% in XLE. The ceasefire day (−13.3% Brent, −3.5% XLE)
  fits that ratio.

## News & catalysts
**Last 30 days**
- **9/26** — Trump rejected Iran's seven-day proposal. Iran offered to reopen Hormuz within seven days if the US lifts its
  naval blockade, eases oil sanctions and frees Iranian assets. — *confirming* (the premium stays)
- **Early October** — the G7 agreed to release up to 100M barrels from strategic reserves (CBS, via search; exact date not
  checked). — *breaking* (bearish for oil)
- **10/4** — OPEC+ kept November targets unchanged. — *neutral*
  - Gulf exports are running at 60–80% of normal.
  - The seven core members pumped 25M bpd in August, about 5M bpd below pre-war.
  - Next meeting: **11/1**.
- **10/5** — a Houthi strike halted Saudi Arabia's East-West pipeline (≈ 7M bpd capacity), the route that bypasses Hormuz.
  Flows were reportedly 5.8M bpd on 10/6. — *confirming*
- **10/14** — September CPI. — *confirming* (the macro hedge)
  - Headline 3.7% y/y (3.4% prior); core 2.6%.
  - Gasoline +9.1% m/m and +34.2% y/y.
- **10/16** — XOM's 8-K showed refining margins +$4.5B quarter on quarter. — *confirming*
- **10/20** — Bloomberg called claims of a near US–Iran deal "inaccurate", and Brent settled at $108.79. — *neutral, fragile*
  - CTAs were 100% max long Brent and WTI (Kpler).
  - The US Energy Secretary put Gulf crude flows at about 80% of pre-war levels.
- **10/21** — mixed signals on talks. — *breaking risk* (talks exist, and both sides have a timetable)
  - Trump: "we're not negotiating", but the war will "end very soon", and there will be no strike on Iran before the
    **11/3 midterms**.
  - Iran (Araghchi): indirect talks continue through Pakistan and Qatar. The US has accepted the seven-day framework but
    wants more (the US has not confirmed). Hormuz stays closed until the terms are met.
  - Reuters: Tehran may be dragging out the stalemate to hurt Trump before the midterms.
- **10/21–22** — Houthi strikes. — *confirming*
  - A drone near Saudi Arabia's Shaybah field (≈ 1M bpd) killed 2; operations were unaffected.
  - An attack on Dammam airport.
  - The US ordered non-emergency staff out of Saudi Arabia.
  - Brent $112.76, a five-month high.

**Next 90 days**
- 10/27–28 — FOMC (before the window).
- **10/30** — XOM and CVX Q3.
- **11/1** — OPEC+ meeting.
- **11/3 — US midterms.** The pivot date for the war premium.
- 11/5 — COP Q3.
- Wednesdays — EIA inventory reports.
- Mid-November — October CPI (date unverified).
- December — FOMC (date unverified).
- Any day — a US reply to Iran's terms, a Hormuz incident, or another Saudi infrastructure hit.

## Positioning & sentiment
- **Fund managers are not crowded in oil.** In BofA's October Global FMS (fielded 10/2–10/8), "long global semiconductors" was
  the most crowded trade (45%), and long oil was named by only 3%.
- **Futures are one-sided.** CTAs were at **100% max long** Brent and WTI (Kpler, via Rigzone 10/20). A peace headline would
  hit a crowded futures market, which is why the April and June drops were fast.
- **The top three holdings are overbought.** XOM, CVX and COP all had RSI above 70 on 10/22.
- **Flows:** no dated October XLE flow figure was found (unverified). The last dated figure is stale: energy ETFs lost about
  $4B in the 65 days to mid-August, after record March inflows (Crypto Briefing, August).
- **Short interest and analysts:** not checked, since they mean little for a sector ETF.

## What would make me wrong
- **Waiting can cost the hedge.** If the war escalates (Hormuz shut through the winter, more hits on Saudi infrastructure),
  XLE could clear $68.78 and never come back to $63. The plan has no 2:1 trade at an all-time high, and that is the price of
  discipline.
- **Price:** a daily close under **$60.70** after a fill.
- **Event:** a signed ceasefire, Hormuz reopening, or the US blockade lifted. Exit at the next open, and do not re-buy that
  drop (April and June: −15% to −16%).
- **A deal around the midterms:** the White House wants lower gasoline, and Iran's seven-day framework is still open.
- **Demand side:** G7 reserve releases (up to 100M bbl), a Fed that keeps hiking into a slowdown, and the sector earnings path
  that FactSet already shows turning negative in Q2'27.
- **Risk-on rotation:** if money rotates back into chips and XLE drifts into the zone, the hedge may keep lagging even
  without a ceasefire. The stop handles that.

## Sources
- Yahoo chart API: XLE, BZ=F, CL=F, ^GSPC, ^SOX, XOM, CVX, COP (2y daily) and XLU, ALL, CB, TRV (10d), fetched
  2026-10-22 22:13 UTC (latest bar 10/22)
- SSGA fund page, data 2026-10-21 — https://www.ssga.com/us/en/intermediary/etfs/state-street-energy-select-sector-spdr-etf-xle
- Stockanalysis XLE, 2026-10-22 — https://stockanalysis.com/etf/xle/
- FactSet energy Q3 preview, 2026-10-12 — https://insight.factset.com/sp-500-energy-sector-earnings-preview-q3-2026
- ExxonMobil 8-K, 3Q26 market and planned impacts, 2026-10-16 — https://www.sec.gov/Archives/edgar/data/2115436/000211543626000013/f8k3q991101626.htm
- XOM Q3 date (company) — https://investor.exxonmobil.com/company-information/press-releases/detail/1212/exxonmobil-to-release-third-quarter-2026-financial-results
- CVX Q3 10/30 (aggregator) — https://www.money365.market/news/latest/chevron-schedules-q3-earnings-call-for-october-30-34c9bacf
- COP Q3 11/5 (release 2026-09-24) — https://finviz.com/news/395338/conocophillips-to-hold-third-quarter-earnings-conference-call-on-thursday-nov-5
- The National, 2026-10-22 (Shaybah, Dammam, East-West pipeline) — https://www.thenationalnews.com/business/energy/2026/10/22/oil-tops-110-as-houthi-drone-strike-near-saudi-shaybah-field-rattles-markets/
- Rigzone, 2026-10-20 (deal report denied, CTAs 100% long) — https://rigzone.com/news/oil_slips_as_iran_talks_fuel_volatility-20-oct-2026-184889-article
- Outlook India, 2026-10-22 (Trump and Araghchi, midterms) — https://www.outlookindia.com/international/no-talks-but-an-end-very-soon-trumps-iran-war-claims-face-tehrans-account
- OPEC+ 10/4 — https://www.thenationalnews.com/business/energy/2026/10/04/opec-keeps-oil-output-targets-unchanged-for-november/ (via search summary)
- G7 reserves and talks, CBS live updates (via search summary) — https://www.cbsnews.com/live-updates/iran-war-us-trump-talks-russia-strait-of-hormuz/
- Al Jazeera, 2026-07-08 (6/17 MOU; oil back at pre-war levels) — https://www.aljazeera.com/news/2026/7/8/oil-prices-surge-as-us-strikes-iran-reversing-fall-to-pre-war-levels
- Axios, 2026-04-07 (ceasefire, Brent −13%, pre-war ≈ $73; page blocked, read via search summary) — https://axios.com/2026/04/07/oil-prices-plunge-us-iran-war-ceasefire-trump
- September CPI, 2026-10-14 — https://tradingeconomics.com/united-states/inflation-cpi/news/591934
- BofA FMS October 2026 — https://investinglive.com/news/long-global-semiconductors-remains-the-most-crowded-trade-followed-by-short-us-treasuries-according-to-bank-of-america/
- Energy ETF flows (August, stale) — https://cryptobriefing.com/us-energy-etf-outflows-4-billion
- Screen that put XLE on the list: `journal/2026-10-23-diversifier-screen.md`
