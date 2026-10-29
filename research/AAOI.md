# AAOI — Applied Optoelectronics — research log

One file per ticker; newest entry first. Each entry is dated; numbers are as of that date.

Entries:
- 2026-10-28 (deep dive)
- 2026-10-19 (update)
- 2026-10-09

---

## AAOI — Applied Optoelectronics — deep dive 2026-10-28

**Verdict:** WATCH, off the buy list for this cycle · **Conviction:** Low. Two rules block it before any zone math:
- **It is 31.6% under a rising 200-DMA**, so no fresh longs.
- **Its ATR is 10.1%.** At any price under **$78.60**, 1.5 ATR exceeds the 15% hard exit, so no stop can satisfy both rules.

The 10/9 zone is long gone. The **$82 invalidation broke on 10/16**, the levels.py "support" of $76.01 broke on 10/22
(low $66.28), and the 50-DMA has crossed under the 200-DMA. The business still burns cash: **TTM FCF −$900M**, with
shares **+49% y/y**.

| | |
|---|---|
| Price (date) | **$77.78** (levels.py, 2026-10-28 10:52 ET). Cross-check $78.75 (stockanalysis, 11:05 ET) |
| Entry zone | **None passes**: below the 200-DMA, and the stop band is empty at 10% ATR (checks below) |
| Invalidation (stop) | n/a, no position. Thesis-level: a 4th ATM / equity filing, 1.6T qualification still unconfirmed at the Q3 report, a GM guide < 29% |
| Target 1 / 2 | n/a. Nearest real resistance: 81.32 (10/21 high) · 83.7–85.0 (10/15) · 91.5–97 (broken Jul/Sep lows) · 100.7 (50-DMA) · 110.74 (levels.py's first swing high) · 113.8 (200-DMA) |
| Reward/risk (T1) | Not computable inside the rules. The best-looking test (T1 110.74) shows 3.7–4.4:1, but the stop fails 1.5 ATR and 15% at every edge |
| Size | n/a. If it ever qualifies: optical slot (one of LITE/AXTI/AAOI); high-beta name → ≤ $190 |
| Timeframe | Quarters (the 800G/1.6T ramp) |
| Next earnings | **2026-11-05 after the close**, call 4:30 ET (**company PR 10/15**: now confirmed; levels.py 6 sessions). Blackout **11/2–11/5** |

### What changed since the 10/19 update
- **A new low.** 10/22 **−12.0%** to $68.07 (14.1M shares), low **$66.28**. 10/26 low $66.51, a near-double low. Then
  10/26 +6.6% and 10/27 +7.0%, so today's $77.78 is **+15% from the 10/23 close**. It has not made a higher high: the
  10/21 high of $81.32 is untouched.
- **The death cross happened.** 50-DMA **$100.73** (falling fast: $112.86 ten sessions ago) is now under the 200-DMA
  **$113.76** (rising). The 20-DMA ($92.56) is below both, a fully bearish stack.
- **Report date confirmed by the company:** Thu 11/5 AMC (PR, 10/15 4:10 PM). The 10/19 entry had it as an estimate.
- **Analysts:** Needham cut its PT **$190 → $170** (Buy, reported 10/27). B. Riley **$109 → $92** (Neutral, 10/15).
- **No new ATM since the 10/5 completion:** no 424B5 or S-3 since 9/1 (EDGAR, fetched 10/28). Five **Form 4s filed
  10/26** were not parsed. A 13G/A was filed 10/27.
- ATR fell slightly, from $9.07 (11.8%) to $7.86 (10.1%), but is still above the 10% line that makes the stop band
  impossible.

### Thesis (unchanged, weaker)
AOI builds the transceivers (400G/800G now, 1.6T starting) that link AI servers, plus CATV amplifiers, mostly in Texas.
Q2'26 revenue was **$191.9M, +86.3%** (MarketBeat via DailyPolitical, 10/27). It guides Q3 to **$255–290M** with EPS
**$0.11–0.26**. On the Q2 call it said it would be the **fourth 1.6T supplier qualified** at a major hyperscaler
"in 2–3 weeks", with **> $70M** of 1.6T revenue in Q4 (Yahoo Q2 call highlights, via search). **No October confirmation
of that qualification was found.** The funding model is the problem. TTM free cash flow is **−$900.5M** on $768.6M of
capex. Net cash is only **$199.6M** after ≈ $1.65B of 2026 ATMs, and shares are **+49.3% y/y** (stockanalysis 10/28).
Another raise is more likely than not before FCF turns.

### Chart & technicals — `levels.py AAOI` (quote 2026-10-28 10:52 ET)
```
AAOI  $77.78 (2026-10-28 10:52 ET); last daily bar 2026-10-28 close $77.79
  20/50/200-DMA  92.56 / 100.73 (falling) / 113.76 (rising)   price vs 50 -22.8%, vs 200 -31.6%
  RSI(14) 40.1   ATR(14) $7.86 = 10.1% a day   52-wk 18.50–233.67 (-67% from the high)
  Trend: BELOW a rising 200-DMA  → protocol: no fresh longs until it reclaims it
  Chase guard: ok
  Next report: 2026-11-05 after the close (6 sessions; EPS est. 0.08)   ✓ outside the buy blackout
  Swing support below: 76.01   resistance above: 110.74, 116.90, 128.35
```
- **levels.py blind spot, and it matters here:** "Swing support below: 76.01" (the 7/29 low) is **already broken**. The
  10/22 low of **$66.28** and the 10/26 low of **$66.51** are not listed, because the swing finder needs 5 bars on each
  side. The resistance list (first entry 110.74) also skips the nearer real levels: 81.32 (10/21 high), 85.02 (10/15
  high), 91.5 (7/17 low), 93.6–96.96 (Sept lows) and the 50-DMA at 100.7.
- **Structure:** lower highs since May (233.7 → 161.0 → 131.2) and lower lows (76.0 in July → 66.3 in October). The
  bounce is +17% from the low on falling volume (14.1M on 10/22 down; 11.3M and 9.4M on the 10/26–10/27 up days).
- Chart: `/tmp/claude-1000/-home-waelas-wael-amana-amana-assistant/cf7235bd-03e5-456e-8948-a8c2229a57bd/scratchpad/charts/AAOI.png`.
  It shows a fully bearish MA stack and price far under all three averages.

### Zone checks — `levels.py AAOI --zone … --size 190 --sleeve 3426` (10:52 ET data)
```
# 1. The October double low 66.28/66.51, stop ≈ 1.3–1.5 ATR under, T1 = 10/21 high
  Setup: zone 66.50–68.00, stop 56.50, T1 81.32
    at low      66.50: R/R 1.48:1, stop 1.27 ATR (15.0%)   ✘ R/R < 2; stop < 1.5 ATR; stop > 15% (hard exit)
    at mid      67.25: R/R 1.31:1, stop 1.37 ATR (16.0%)   ✘ R/R < 2; stop < 1.5 ATR; stop > 15% (hard exit)
    at high     68.00: R/R 1.16:1, stop 1.46 ATR (16.9%)   ✘ R/R < 2; stop < 1.5 ATR; stop > 15% (hard exit)
    size $190 ≈ 2.8253 sh at the mid; risk to stop $30.37 = 0.9% of $3,426   ✓ ≤ 2%
# 2. Same zone, T1 = levels.py's first swing high (generous; skips five nearer levels)
  Setup: zone 66.50–68.00, stop 56.50, T1 110.74
    at low      66.50: R/R 4.42:1, stop 1.27 ATR (15.0%)   ✘ stop < 1.5 ATR; stop > 15% (hard exit)
    at mid      67.25: R/R 4.05:1, stop 1.37 ATR (16.0%)   ✘ stop < 1.5 ATR; stop > 15% (hard exit)
    at high     68.00: R/R 3.72:1, stop 1.46 ATR (16.9%)   ✘ stop < 1.5 ATR; stop > 15% (hard exit)
```
**No zone passes, and none can at this volatility.** 1.5 ATR = $11.79, which is more than 15% of any entry under
$78.60. Even a far T1 does not rescue the stop.

**What would create a zone (all three are needed):**
- **(1)** A close back above the **200-DMA (≈ $116 by 11/6)**, +49% from here.
- **(2)** ATR under ≈ 9% of price.
- **(3)** A base with ≥ 3 ATR (≈ $24 today) to the next resistance.

That is not a realistic November setup. It is a 2027 question.

### Earnings preview (section A) — not held
1. **Date/time:** Thu **11/5 AMC**, call 4:30 ET (company PR 10/15; levels.py agrees).
2. **Consensus, and it conflicts:** revenue **$268.1M / EPS $0.14** (MarketBeat) vs **$270.3M / $0.28** (Earnings
   Whispers), both via search on 10/28. Guide $255–290M / EPS $0.11–0.26. Alpha Vantage's 0.08 matches neither. The
   metrics that move it: **1.6T shipments and the Q4 1.6T number (> $70M)**, GM vs 29%, and any word on funding or an ATM.
3. **Implied move:** **±19.10%** (weekly, 11/6 expiry; monthly ±22.94%; optionslam 10/28) ≈ **±$14.9 → $63–93**. On a
   $190 starter that is ≈ $36 at stake. That is half the account's $69 risk budget on one gap, and larger than any stop
   distance the rules allow.
4. **Scenarios:**

   | Scenario | What has to happen | Likely reaction | Action written now |
   |---|---|---|---|
   | Bull | Q3 ≈ $290M, 1.6T shipping and the Q4 1.6T ≥ $70M reaffirmed, GM ≥ 30%, no new ATM | Gap +20–30% into $91.5–97 (broken Sept lows), still under the 50- and 200-DMA | No buy: still below the 200-DMA. Re-run weekly; a qualifying base is weeks away |
   | Base | Mid-range revenue, vague 1.6T timing | ±10%, chop $66–85 | Nothing |
   | Bear | Miss, 1.6T slip, or an ATM/equity filing | Break of $66.28 toward the $50s | Nothing. A new ATM is a thesis break: drop it from the watchlist |

5. **History** (close-to-close / opening gap, levels.py Yahoo bars): 11/7/25 **−1.8% / −14.1%** · 2/27/26 **+56.9% /
   +22.8%** · 5/8/26 **−5.5% / +10.3%** · 8/7/26 **+9.2% / +14.7%**. Opening gaps of −14% to +23%. Two of four reversed
   intraday by 12–16 points. (11/6/25 and 2/26/26 report dates inferred from the gaps.)
6. **Decision:** not held, nothing to decide. Run `levels.py AAOI` after the **11/6 close**. Even if a level appears,
   it must first clear the 200-DMA rule and the one-optical-name rule.

### Thesis scorecard (section B)
| Pillar (falsifiable) | Expected | Status (dated) | Trend |
|---|---|---|---|
| 1.6T qualified and shipping; Q4 1.6T > $70M | Q2 call (8/6): "2–3 weeks" | **no confirmation found** by 10/28 | weakening |
| Non-GAAP GM ≥ 29% | 29–30.5% guide | TTM GAAP 28.9% (stockanalysis 10/28); Q3 test 11/5 | flat |
| No new equity before FCF turns | none | no 424B5/S-3 since 9/1 (EDGAR 10/28); TTM FCF −$900M, net cash $199.6M | weakening |
| Q3 revenue inside $255–290M | ≥ $255M | test 11/5 | pending |
| US-made premium vs Chinese transceivers | policy tailwind | no new policy news this session | unverified |

**Thesis-break exits:** a 4th ATM or any equity/convert filing · the 1.6T qualification not confirmed at Q3 · a GM guide
< 29%. **Conviction:** Low. Up only on confirmed 1.6T revenue *and* a funding plan that is not new shares.

### Fundamentals (stockanalysis statistics, 2026-10-28 11:05 ET, unless noted)
- Market cap **$7.13B**, EV $6.94B. Forward P/E 34.2, P/S 11.7, **forward P/S 3.8**.
- TTM revenue $596.0M, GM 28.9%, op margin **−11.3%**. Operating cash flow −$131.8M, capex −$768.6M, **FCF −$900.5M**.
- **Net cash $199.6M** (cash $499.7M, debt $300.1M). Shares 90.60M: **+49.3% y/y, +7.35% q/q**.
- Q2'26: revenue $191.92M (+86.3%), EPS $0.06 vs $0.02 consensus. Analysts expect $0.55 FY EPS (MarketBeat via
  DailyPolitical, 10/27).

### News & catalysts (last 30d / next 90d)
- 2026-10-27 — breaking (sentiment) — **Needham cuts PT to $170 from $190**, keeps Buy (DailyPolitical/MarketBeat,
  10/27).
- 2026-10-26 — neutral — +6.6% with the optics rebound after StoneX's LITE initiation (24/7 Wall St, 10/26). Five Form 4s
  filed (EDGAR).
- 2026-10-22 — neutral (sector) — **−12.0%** close, new low $66.28, in the post-Meta optics sell-off (24/7 Wall St
  headline 10/22: AAOI −10% intraday).
- 2026-10-15 — confirming (date) — company sets the Q3 call for 11/5, 4:30 ET. B. Riley cuts PT to $92.
- 2026-10-12 — neutral — CFO Murry sold 4,000 shares at $102.87 (10b5-1). 56,887 insider shares ($6.58M) sold in 90
  days, no buys reported (DailyPolitical, 10/27).
- **Next:** 11/4 COHR · **11/5 AAOI** · any ATM/S-3 filing (watch EDGAR).

### Positioning & sentiment
- Short interest **13.87M = 16.0% of float**, 2.07 days (stockanalysis 10/28; settlement date not shown).
- Analysts conflict: **Buy (6), PT $156** (stockanalysis 10/28) vs **Hold, PT $143** (3 Buy / 2 Hold / 1 Sell; MarketBeat
  via DailyPolitical 10/27). Weiss "sell (d−)" (10/21).
- Beta 3.85 (MarketBeat). One of the most crowded, highest-beta optical names, with leveraged single-stock ETFs (10/9
  entry). The profile behind the −67% drawdown from May.

### What would make me wrong
- 1.6T confirmed with a big Q4 number and no ATM could squeeze a 16%-short stock +30% in a day. The rules would still miss
  it, and that is acceptable for a cash-burning, diluting name.
- The thesis is wrong outright if another equity raise lands before FCF turns, or 1.6T slips again.

### Sources
- `levels.py AAOI` and zone checks, Yahoo chart API, quote 2026-10-28 10:52 ET. Chart PNG above
- [Finviz/PR Newswire, 10/15: AOI announces date of Q3 2026 call](https://finviz.com/news/403299/applied-optoelectronics-announces-date-of-third-quarter-2026-financial-results-conference-call) — fetched 10/28
- [DailyPolitical, 10/27: Needham lowers AAOI target](https://www.dailypolitical.com/2026/10/27/applied-optoelectronics-nasdaqaaoi-stock-price-target-lowered-at-needham-company-llc.html) — fetched 10/28
- [stockanalysis AAOI statistics](https://stockanalysis.com/stocks/aaoi/statistics/) — 10/28 11:05 ET
- [optionslam AAOI](https://www.optionslam.com/earnings/straddle/AAOI) — fetched 10/28
- [MarketBeat AAOI Q3 estimates](https://www.marketbeat.com/earnings/reports/2026-11-5-applied-optoelectronics-inc-stock/) and [Earnings Whispers AAOI](https://www.earningswhispers.com/epsdetails/AAOI) — via search 10/28 (conflicting consensus)
- [Yahoo: AAOI Q2 2026 call highlights](https://finance.yahoo.com/markets/stocks/articles/applied-optoelectronics-inc-aaoi-q2-050943160.html) — 1.6T qualification language (via search)
- [24/7 Wall St, 10/26](https://247wallst.com/investing/2026/10/26/lumentum-jumps-8-as-stonex-starts-coverage-with-1200-target-applied-optoelectronics-and-coherent-climb-6/) · 24/7 Wall St 10/22 headline (see LITE entry)
- EDGAR filing list, CIK 1158114 — fetched 10/28

---

## AAOI — update 2026-10-19

**Verdict:** WATCH, setup invalid · re-derive only after the ≈ **11/5** report and a confirmed 1.6T qualification ·
**Conviction:** Low. The 10/9 zone ($94–96.50) broke and the price is **under the $82 invalidation**. All three
moving averages are falling.

| | |
|---|---|
| Price | **$77.09** (2026-10-19, 10:35 ET, +2.0%); close $75.57 (10/16); 10-day low **$75.43** |
| 20 / 50 / 200-DMA | $102.1 / $109.8 / $112.4 — all falling; price −30% under the 50 and −31% under the 200 |
| RSI(14) · ATR(14) | 34.1 · **$9.07 = 11.8% a day** · −67% from the 5/13 high of $233.67 |

**News (dated):** the **$600M ATM program was reported completed** (≈ 10/5): more dilution, on top of ≈ $1.65B of ATMs
in 2026. −9% intraday on 10/14 and a 10/15 close of $83.73 (−23.6% from 10/9), harder hit than LITE and COHR.
**B. Riley cut its target to $92 from $109** (week of 10/16). The 1.6T case rests on the 8/6 call: shipments late Q3,
ramp in Q4, > $200M of 1.6T orders. No October confirmation. Q3 guide $255–290M; top 10 customers = 99% of revenue.

**Sources:** Yahoo chart API AAOI 1y daily, fetched 2026-10-19 10:35 ET · [Motley Fool, 10/16: why AAOI plummeted this week](https://www.fool.com/coverage/market-movers/2026/10/16/why-applied-optoelectronics-stock-plummeted-this-week/) · [24/7 Wall St, 10/14](https://247wallst.com/investing/2026/10/14/applied-optoelectronics-dives-9-as-ai-funding-fears-hit-optical-stocks-coherent-slides-7-lumentum-drops-7/) · [MarketBeat: Q2 call highlights, 8/6](https://www.marketbeat.com/instant-alerts/applied-optoelectronics-q2-earnings-call-highlights-2026-08-06/) · earnings date unconfirmed by the company.

---

## AAOI — Applied Optoelectronics — deep dive 2026-10-09

**Verdict:** WATCH (not BUY today; second choice after AXTI) · **Conviction:** Low–Med — the demand is real and the
policy wind favours a Texas manufacturer. But the business makes a 28–30% gross margin, burns cash, and pays for its
build-out by selling new shares: **≈ $1.65B of ATM offerings in 2026 alone**. At $111.58 the reward/risk is 1.0:1.

| | |
|---|---|
| Price | **$111.58** (2026-10-09, 12:43 ET, +5.4%); close **$105.90** (2026-10-08, −13.6% on 19.2M shares) |
| 50-DMA / 200-DMA | **$113.9** / **$111.0** (10/9 incl. intraday) — price at the 200, under the 50; **death cross in ≈ 6 sessions if flat** |
| 52-wk high / low | $233.67 (2026-05-13) / $18.50 (2025-11-21) · **−52% from the high, +229% in a year** |
| RSI(14) · MACD · ATR(14) | 50.9 · bullish but fading (histogram peaked 10/6) · **$9.52 = 8.6% a day** |
| Entry zone | **$94.00–96.50** (Sep double bottom $93.6–94.0; Sep 30/Oct 1 lows $96.4–97.8) |
| Invalidation (stop) | **$82** (1.4 ATR under the zone; −15.0% from $96.50) / or event: 1.6T qualification still unconfirmed at the Q3 report, a new ATM, GM guide < 29% |
| Target 1 / 2 | **$128–131** sell zone (Oct 7 high $127.9, Oct 6 swing high $131.15, falling 100-DMA ≈ $130) / $149–161 (Aug highs) |
| Reward/risk (T1) | **2.2:1 at $96.50 · 2.8:1 at $94** ✓ — at today's price **1.0:1** ✘ |
| Size | **starter $190 ≈ 5% of the sleeve** in one fill. Risk to the stop ≈ $27 = 0.7% |
| Timeframe | months (thesis = the 2026–27 800G/1.6T ramp) |
| Next earnings | **≈ 2026-11-05 (estimate, not confirmed)** — 19 sessions. Last 4 reactions: −1.8% / **+56.9%** / −5.5% / +9.2% close-to-close; opening gaps −14% to +23% |

### Thesis
AOI builds the optical transceivers that connect AI servers (400G/800G now, 1.6T starting) and amplifiers for cable
networks (DOCSIS 4.0). Revenue is accelerating: Q2 2026 was $191.9M, +86% YoY. Datacenter was $107.7M (+140%) and CATV
$80.6M (+44%). Q3 guide is **$255–290M** and FY26 ≈ $1.1B. Consensus has FY27 at **$2.66B**. In March it won a >$200M
first 1.6T volume order from a hyperscaler. Amazon holds a warrant over 7.95M shares that vests with up to $4B of
purchases. Its edge is **US manufacturing**: lasers are made in Sugar Land, and Houston capacity is growing toward
> 1.6M sq ft. Policy is moving against Chinese transceivers: a Senate bill (9/28) would bar InnoLight/Eoptolink from
national-security systems, and an FCC/White House draft ban was reported (8/4). **At $10.1B the bull case is priced as
delivered**: 9.5× FY26 sales, 3.7× FY27, ≈ 24× FY27 EPS ($4.60). That is cheap only if the 4.5× revenue ramp from TTM
$596M to $2.66B happens and margins rise to 35–40%.

### Why it ranks below AXTI
| | AXTI | AAOI |
|---|---|---|
| Place in the chain | **Bottleneck input** (InP wafers), 3 real suppliers | Assembler, in a crowded field (InnoLight ≈ 27% share, Eoptolink, COHR, FN) |
| Gross margin | **44.9%** and rising (pricing power) | **27.7% GAAP**, guided 29–30.5% (half of LITE's 44%) |
| Profit / cash | Profitable in Q2; **≈ $616M net cash** | Op margin −11%; Q2 FCF **−$265M** ex-prepayments |
| How growth is funded | One large raise at $64.25 (Apr) | **Serial ATMs: $500M + $550M + $600M in 2026**; shares +182% since Aug 2023 |
| Customers | No customer > 10% in Q2 | **Top 3 = 92% of Q2 revenue**; one distributor owes 67% of receivables |
| What breaks it | Beijing (binary, outside the fundamentals) | Execution, margins, dilution (gradual, inside them) |
Management credibility: on 8/18 the CFO said raising "everything on the back of equity … is not our plan." The $600M
ATM was filed **three days later** (8/21) and finished on 10/5 at an average of $105.36.

### Chart & technicals (Yahoo daily bars computed by the desk; matches stockanalysis/finviz 10/9)
- **Structure**: $223 close (5/13), then **−66% to $76.52 (7/29)**, then +70% to $130.16 (10/6), now $111. Since
  August: lower highs ($161 → $149 → $131), with a double bottom at $93.6–94 in September.
- **Trend is mixed and turning down**: the 100-DMA is falling, and the 50-DMA is about to cross under the 200-DMA. The
  heaviest volume of the month came on the down day (10/8, 19.2M).
- **Volatility**: 27 days of −10% or worse and 35 of +10% or better in the last 251 sessions. Beta ≈ 3.9.
- **Supports**: $104.9–106.1 (10/8 low/close, 20-DMA, ATM average $105.36) · $102.1 · $96.4–97.8 · **$93.6–94.0** ·
  $91.5 · $76.0.
- **Resistances**: $111 (200-DMA) · $113.5–113.9 (50-DMA) · $116.9–117.7 · $119.9–121.9 · **$127.9–131.2** · $133.7 ·
  $149.4 / $161.0 · $233.67.

### Fundamentals
| Quarter | Revenue (YoY) | Datacenter | CATV | Non-GAAP GM | Op margin | GAAP NI | FCF |
|---|---|---|---|---|---|---|---|
| Q3'25 | $118.6M (+82%) | $43.9M | $70.6M | 31.0% | −15.3% | −$17.9M | −$78.7M |
| Q4'25 | $134.3M (+34%) | $74.9M | $54.0M | 31.4% | −8.6% | −$2.0M | −$104.6M |
| Q1'26 | $151.1M (+51%) | $81.4M | $66.8M | 29.2% | −8.6% | −$14.3M | −$143.6M |
| **Q2'26** | **$191.9M (+86%)** | **$107.7M** | **$80.6M** | **29.8%** | **−12.9%** | **−$22.8M** | **−$265M** (ex-prepayments) |
- Earnings quality: Q2's +$5.5M non-GAAP profit includes a +$14.3M tax add-back. H1 operating cash flow was helped by a
  +$142M rise in payables.
- Balance sheet (6/30): cash $500M, debt ≈ $222M (incl. $125M converts at $43.31). Pro forma for the 10/5 ATM, net cash
  is ≈ $866M before Q3 burn. H1 capex was $335M plus $290M of prepayments, and H2 is expected to be at least as heavy.
- Share count: 32.1M (8/2023) → 62.4M (8/2025) → **≈ 90.6M now**, +32% in a year. Overhang: 7.95M Amazon warrant
  shares, 2.9M from the converts, ≈ 2.5M RSUs. Authorized: 120M.

### News & catalysts
- 2026-10-09 — confirming (sector) — +5% after Lumentum's CEO said optical parts are sold out through early 2029.
- 2026-10-08 — neutral/breaking — −13.6% in a sector sell-off; ATM dilution and an insider sale were cited.
- 2026-10-05 — **breaking (dilution)** — the third 2026 ATM completed: 5.69M shares at $105.36, $588M net.
- 2026-10-05/07 — neutral — SVP sold 6,000 shares at $120.03 (10b5-1).
- 2026-09-28 — confirming — Senate bill against InnoLight/Eoptolink in national-security systems.
- 2026-09-15 — **mixed** — a new 10-year factory lease in **Ningbo, China**. That is exposed to the same FCC draft ban
  that is AOI's bull case.
- 2026-09-10 / 09-01 — confirming — Houston building bought ($26.8M); two Houston leases signed.
- **Next 90 days**: ≈ 11/5 Q3 report (guide $255–290M, GM 29–30.5%; first 1.6T revenue; the Q4 1.6T $70–80M "committed")
  · FCC ban decision (timing unknown) · whether a fourth ATM is filed.

### Positioning & sentiment
- Short interest 12.3M = **≈ 15% of float**, 2.0 days to cover (9/15).
- **Insiders: $94.8M sold in 6 months, zero buys.** The CEO sold ≈ $19.9M at $166–173 in May–June.
- Consensus Buy, average PT **$163.40** (6 analysts; stockanalysis/TipRanks, data from mid-August). MarketBeat has
  Hold / $139.40. No rating or PT changes in the last 30 days.
- **Crowded**: 2× long ETFs (AAOX, AAOG) and a 2× short; "meme stock" and "crowded trade" labels (24/7, 7/15).

### Potential — the honest range
- **Upside** if 1.6T ramps and margins reach the 30s: $149–161 (+34–44%); the $234 high is +109%.
- **Downside** on a margin miss, a failed qualification or another ATM: $76 (−32%). It fell −66% in 11 weeks this year.

### What would make me wrong
- A daily close **under $82**.
- 1.6T qualification not confirmed at the Q3 report, or the Q4 1.6T $70–80M cut.
- **A fourth ATM / equity filing** before free cash flow turns: exit, no debate. The dilution is the thesis risk.
- A non-GAAP gross margin guide under 29%.
- An FCC ban that catches its Ningbo output with no US offset.

### Sources
- Yahoo chart API AAOI 5y daily bars (fetched 2026-10-09 12:22 ET); https://stockanalysis.com/stocks/aaoi/ (10/9 12:43 ET)
- https://stockanalysis.com/stocks/aaoi/statistics/ · /forecast/ · /financials/ · /transcripts/662748-q2-2026/ — 2026-10-09
- Rosenblatt summit transcript https://stockanalysis.com/stocks/aaoi/transcripts/726607-rosenblatt-s-6th-annual-technology-summit-the-age-of-ai-part-ii/ — 2026-08-18
- Q2 10-Q https://www.sec.gov/Archives/edgar/data/1158114/000143774926026278/aaoi20260630_10q.htm
- Q2 release https://www.sec.gov/Archives/edgar/data/1158114/000168316826006055/aaoi_ex9901.htm — 2026-08-06
- ATM 8-K https://www.sec.gov/Archives/edgar/data/1158114/000110465926099688/tm2623389d2_8k.htm — 2026-08-21
- ATM completion https://finviz.com/news/398520/applied-optoelectronics-announces-completion-of-previously-announced-at-the-market-offering — 2026-10-05
- Ningbo lease 8-K https://www.sec.gov/Archives/edgar/data/1158114/000168316826007160/aaoi_8k.htm — 2026-09-15
- 1.6T order https://www.globenewswire.com/news-release/2026/03/09/3251675/0/en/aoi-receives-first-volume-order-of-1-6t-data-center-transceivers-from-major-hyperscale-customer.html — 2026-03-09
- https://finance.yahoo.com/markets/stocks/articles/optics-stocks-tumble-profit-taking-160031296.html — 2026-10-08
- https://www.tipranks.com/news/why-applied-optoelectronics-stock-is-surging-today-as-ast-spacemobile-falls-and-what-wall-street-expects-next — 2026-10-09
- https://www.executivegov.com/articles/senate-bill-chinese-optical-transceivers-national-security-systems — 2026-09-28
- https://gvwire.com/2026/08/04/trump-administration-drafting-ban-on-chinese-data-center-devices-sources-say/ — 2026-08-04
- https://www.marketbeat.com/stocks/NASDAQ/AAOI/short-interest/ · https://api.nasdaq.com/api/quote/AAOI/short-interest — 9/15 settlement
- http://openinsider.com/screener?s=AAOI — fetched 2026-10-09
