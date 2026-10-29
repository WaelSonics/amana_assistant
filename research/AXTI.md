# AXTI — AXT Inc. — research log

One file per ticker; newest entry first. Each entry is dated; numbers are as of that date.

Entries:
- 2026-10-28 (deep dive)
- 2026-10-19 (update)
- 2026-10-14 (check)
- 2026-10-09

---

## AXTI — AXT Inc. — deep dive 2026-10-28

**Verdict:** WATCH, no passing zone · **Conviction:** Low on the setup, Med on the business. **There was no
rule-compliant AXTI buy on 10/27, and there is none today.** The PLAN's "fresh level ≈ $190 after the 10/29 report"
cannot be built at a 10% ATR. Today's 8-K (a **$285–545M private financing at the Tongmei subsidiary**) funds the InP
capacity without a parent share sale, but it gives away up to ≈ 26.6% of the operating company and adds 8% redemption
claims that AXT may settle in its own stock. Next steps: re-run the levels after the **10/30 close**; earliest buy
**11/2** (client freeze). The 11/27 China date remains the kill switch.

| | |
|---|---|
| Price (date) | **$61.29** (levels.py, 2026-10-28 10:52 ET; +5.3%, high 62.10). Cross-check $61.85 (stockanalysis, 11:03 ET) |
| Entry zone | **None passes.** Four zones tested, including the client's 10/27 "dip" (below) |
| Invalidation (stop) | n/a, no position. Thesis-level: China halts or slows InP permits, or the 11/27 Ga/Ge suspension lapses with new limits; Q3 < $60M or a Q4 guide that blames permits; a parent equity raise |
| Target 1 / 2 | n/a. Resistance: 64.49 (200-DMA) · 64.96–65.35 (10/13–10/14 highs) · 65.42 (20-DMA) · 66.81 (50-DMA) · 73.94 · 81.50 · 88.36. Fundamental: analyst average $91.60 (stale, July data) |
| Reward/risk (T1) | Best tested: **1.72:1** (hypothetical reclaim zone 65.5–66, stop 56.2, T1 81.5, skipping 73.94). ✘ |
| Size | n/a. When a zone passes: ≈ $190 (5.5%) as the one optical name. **Not as the speculative slot:** that slot needs a stop ≤ 12% under entry, and 1.5 ATR is 15% |
| Timeframe | Months, cut short by the 11/27 policy date |
| Next earnings | **2026-10-29 after the close** (Business Wire 10/1; levels.py: 1 session, **✘ inside the blackout**, which began 10/26) |

### The client's 10/27 "dip" — was there a rule-compliant setup? No, on five counts
1. **Earnings blackout.** From 10/26 the report was ≤ 3 sessions away (PLAN §1b). levels.py flags it today.
2. **Trend filter.** The price is under the 200-DMA ($64.49). levels.py prints "no fresh longs until it reclaims it",
   and the 10/24 desk check listed AXTI as "broken … not fresh longs until they base and reclaim the 200-DMA".
3. **The zone math fails all three tests at once:**
   ```
   levels.py AXTI --zone 56-58 --stop 49 --target 64.5 --size 190 --sleeve 3426   (10:52 ET data)
     Setup: zone 56.00–58.00, stop 49.00, T1 64.50
       at low      56.00: R/R 1.21:1, stop 1.14 ATR (12.5%)   ✘ R/R < 2; stop < 1.5 ATR
       at mid      57.00: R/R 0.94:1, stop 1.30 ATR (14.0%)   ✘ R/R < 2; stop < 1.5 ATR
       at high     58.00: R/R 0.72:1, stop 1.47 ATR (15.5%)   ✘ R/R < 2; stop < 1.5 ATR; stop > 15% (hard exit)
       size $190 ≈ 3.3333 sh at the mid; risk to stop $26.67 = 0.8% of $3,426   ✓ ≤ 2%
   ```
   At a 10.0% ATR, **no stop can be both ≥ 1.5 ATR and ≤ 15% below any entry under $61.40**. The rule set makes it
   mechanically impossible, so no stop placement could have rescued the dip.
4. **Client commitment:** no buys or sells until 11/2.
5. **Evidence:** "it will go back, look at MU and WDC" is cherry-picking (journal 10/27). The only real evidence since
   then is the 10/22 higher low ($51.00 vs $50.57). That is necessary but not sufficient.

The stock is +5% since the 10/27 close. That does not prove the dip-buy right: it is +18.9% into a ±15% binary.

### What changed since the 10/19 update
- **First higher low:** 10/22 low **$51.00** (close $51.56, **−13.0%** on the sector sell-off) held above the 10/16 low
  of $50.57. Then **+18.9%** in four sessions (10/26 +8.0%, 10/27 +3.5%, today +5.3%), on thin news (StocksToTrade,
  10/26: "without new fundamental headlines").
- **Still under the 200-DMA** ($64.49, rising ≈ $0.24 a day; it was $63.2 on 10/19). The 50-DMA ($66.81) is falling
  (it was $71.49 ten sessions ago). The 20, 50 and 200 have converged at $64.5–66.8 directly overhead.
- **ATR eased** from $6.69 (11.8%) to **$6.14 (10.0%)**, still at the line where the stop band disappears.
- **10/28 8-K (accepted 06:10 ET): Tongmei private equity financing**, signed 10/27. Investors put in **RMB 1.91–3.67B
  (≈ $285–545M)**, led by BNK-B3 HK Holdings (managed by "a leading Asia asset manager"), together with an affiliate of
  an existing customer. AXT recapitalizes Tongmei with **$400M** and keeps ≈ **73.4%** at the maximum. Investors can
  demand **redemption at cost + 8% a year** if there is no qualified IPO within 3 years. AXT may pay that in cash, an
  unsecured note or **AXT shares at the 90-day VWAP**. Closing needs Chinese government filings and is expected in
  **December 2026**; the deal terminates if the minimum has not closed by 12/20. Use of proceeds: InP capacity, capex,
  working capital and raw-material affiliates.
- **Trade policy:** the US-China truce was **extended to 2027-01-10** (Bessent, 9/23–24; CNBC/Rare Earth Exchanges
  9/24). **Whether the separate Ga/Ge/Sb export-ban suspension (to 11/27/2026) was extended with it is unverified.** No
  source fetched this session says so. The 11/27 kill-switch date stands.
- Short interest is **17.5% of float** (stockanalysis 10/28) vs 14.3% (9/15, per the 10/9 entry). Implied move for the
  report: **±15.46%** (optionslam 10/28).

### Thesis
AXT makes **indium-phosphide wafers**, the substrate under the lasers in AI optical links, and is one of three real
suppliers. Q2'26 revenue was **$47.6M (+164% y/y)**, including **$30.7M of InP**, a **45% non-GAAP gross margin** and net
income of $11.9M ($0.19). Q3 is guided to **≥ $66M "realizable"** (already permitted or permit-exempt) and EPS
$0.30–0.32, with InP capacity at **$35–40M a quarter in Q3, $60M by end-2026 and $130M by end-2027** (Semiconductor Today,
8/4). The bull case is a supply-constrained input with pricing power. The bear case is that **all production is in
Beijing** and every export needs a Chinese permit. Today's financing confirms the capacity plan, and that a customer
affiliate is willing to fund it, but it moves more of the value into a Chinese subsidiary with outside claims ahead of
AXT's common stock. At **$3.97B market cap, 38.7× forward earnings and 11.1× forward sales** (stockanalysis 10/28), the
ramp is priced in.

### Chart & technicals — `levels.py AXTI` (quote 2026-10-28 10:52 ET)
```
AXTI  $61.29 (2026-10-28 10:52 ET); last daily bar 2026-10-28 close $61.29
  20/50/200-DMA  65.42 / 66.81 (falling) / 64.49 (rising)   price vs 50 -8.3%, vs 200 -5.0%
  RSI(14) 47.5   ATR(14) $6.14 = 10.0% a day   52-wk 6.04–143.16 (-57% from the high)
  Trend: BELOW a rising 200-DMA  → protocol: no fresh longs until it reclaims it
  Chase guard: ok
  Next report: 2026-10-29 after the close (1 sessions; EPS est. 0.3)   ✘ inside the 3-session buy blackout
  Swing support below: 53.36, 52.76, 50.57   resistance above: 73.94, 81.50, 88.36
```
- **levels.py blind spot:** the **10/22 low of $51.00**, the higher low, is not listed (it needs 5 bars on each side).
  The resistance list starts at 73.94 and skips the 200/20/50-DMA cluster at $64.5–66.8 and the 10/13–10/14 highs
  ($64.96–65.35), which is the real first resistance.
- **Structure:** a contracting range since July: 36.73 (7/29) → 52.76 (9/3) → 50.57 (10/16) → 51.00 (10/22) on the
  lows, and 97.79 (8/17) → 88.36 (10/6) → 65.35 (10/14) → 62.10 (today) on the highs. Price is coiling under the MA
  cluster into the report.
- Chart: `/tmp/claude-1000/-home-waelas-wael-amana-amana-assistant/cf7235bd-03e5-456e-8948-a8c2229a57bd/scratchpad/charts/AXTI.png`.
  It shows price just under the converged 20/50/200 cluster.

### Zone checks — `levels.py AXTI --zone … --size 190 --sleeve 3426` (10:52 ET data)
```
# 1. Client's 10/27 dip — see above: fails R/R, 1.5 ATR and 15% at every edge
# 2. Today's price, stop under the 10/22 and 10/16 lows, T1 = the MA cluster
  Setup: zone 61.00–62.00, stop 50.50, T1 64.50
    at low      61.00: R/R 0.33:1, stop 1.71 ATR (17.2%)   ✘ R/R < 2; stop > 15% (hard exit)
    at mid      61.50: R/R 0.27:1, stop 1.79 ATR (17.9%)   ✘ R/R < 2; stop > 15% (hard exit)
    at high     62.00: R/R 0.22:1, stop 1.87 ATR (18.5%)   ✘ R/R < 2; stop > 15% (hard exit)
    size $190 ≈ 3.0894 sh at the mid; risk to stop $33.98 = 1.0% of $3,426   ✓ ≤ 2%
    price is IN the zone
# 3. Hypothetical post-report reclaim of the 200/50-DMA, T1 = 9/9 swing high (today's ATR)
  Setup: zone 65.50–66.00, stop 56.20, T1 73.94
    at low      65.50: R/R 0.91:1, stop 1.51 ATR (14.2%)   ✘ R/R < 2
    at mid      65.75: R/R 0.86:1, stop 1.55 ATR (14.5%)   ✘ R/R < 2
    at high     66.00: R/R 0.81:1, stop 1.60 ATR (14.8%)   ✘ R/R < 2
# 4. Same, generous T1 (skips 73.94)
  Setup: zone 65.50–66.00, stop 56.20, T1 81.50
    at low      65.50: R/R 1.72:1, stop 1.51 ATR (14.2%)   ✘ R/R < 2
    at high     66.00: R/R 1.58:1, stop 1.60 ATR (14.8%)   ✘ R/R < 2
    (levels.py prints "price is BELOW the zone — needs re-deriving" for #3–4: that message assumes a dip zone; here the zone is a reclaim above price)
```
**No zone passes.** Even a clean reclaim fails, because the swing highs above (73.94 / 81.50 / 88.36 / 97.79) are spaced
1.1–1.5 ATR apart, while the rule needs **3 ATR (≈ $18) of clear air to T1**.

**What would create a zone (all three are needed):**
- **(1)** A post-report **close above the 200-DMA (≈ $65.0 on 10/30)** that holds the $51.00 higher low.
- **(2)** ATR down to ≈ 8% or less, so a stop band exists with some zone width.
- **(3)** A base whose nearest swing high is ≥ 3 ATR above.

Realistically, (2) cannot happen in the 2–3 weeks after a ±15% gap, and **11/27 arrives 18 sessions after 11/2**.
**The desk's "≈ $190 after the report" line should be withdrawn until a check passes.**

### Earnings preview (section A) — not held
1. **Date/time:** Thu **10/29 after the close** (confirmed; Business Wire 10/1, MarketChameleon, Stocktitan calendar). PCE
   prints at 8:30 the same morning, and AMZN, INTC and SNDK report the same evening.
2. **Consensus:** revenue **$66.11M (+136.5% y/y)**, EPS **$0.31** (Zacks via TradingView, fetched 10/28). Wedbush
   $66.1M / $0.32 (Proactive, via search, date unknown). Guide ≥ $66M realizable, upside "depending on additional export
   permit approvals". The metrics that move it: **InP revenue vs the $35–40M capacity**, GM vs 45%, the **Q4 guide** (one
   source has Q4 consensus ≈ $77.45M, unverified), and any word on US-bound permits or the Tongmei deal.
3. **Implied move:** **±15.46%** (weekly, 10/30 expiry; monthly ±24.30%; optionslam 10/28) ≈ **±$9.5 → $51.8–70.8**.
   The bottom of that range is the 10/22 higher low ($51.00). On a $190 starter that is ≈ $29 at stake. In July the
   implied move was 32.3%, the realized close-to-close +28.7% and the open gap +42%.
4. **Scenarios:**

   | Scenario | What has to happen | Likely reaction | Action written now |
   |---|---|---|---|
   | Bull | Q3 ≥ $70M (permit upside), GM ≥ 45%, Q4 guide ≥ $77M, InP capacity on track | Gap +15–30% to $70–80, through the 200/50-DMA | No buy into the gap. Re-run 10/30. A zone needs a base above the 200-DMA and ≥ 3 ATR to T1, which is unlikely before 11/27 |
   | Base | ≈ $66M, in line, cautious Q4 | ±10%, chop $55–68 under or at the MA cluster | Nothing; still under the 200-DMA |
   | Bear | < $60M, permit language, Q4 below Q3, or the Tongmei deal read as dilution | Gap through $51.00/$50.57 toward $42–37 | The higher low is gone. No level until a new base forms |

5. **History** (close-to-close / opening gap, levels.py Yahoo bars): 10/31/25 **+8.6% / +12.7%** · 2/20/26 **+24.7% /
   +8.5%** · 5/1/26 **+21.2% / −0.5%** · 7/31/26 **+28.7% / +42.1%**. Four for four up. This time the stock ran +18.9%
   in the four sessions before the print, so part of a beat is already in the price. (The 10/30/25 report date is
   inferred; 2/19, 4/30 and 7/30 are confirmed.)
6. **Decision:** not held; no pre-report decision. Run `levels.py AXTI` after the **10/30 close**, the first full
   post-report bar. Earliest buy **11/2** (client freeze), and only if a `--zone` check passes. 11/2 has ISM at 10:00 ET,
   which is not on PLAN's data-morning list. Any AXTI position held past **11/27** carries the policy binary, which no
   stop protects against.

### Thesis scorecard (section B)
| Pillar (falsifiable) | Expected | Status (dated) | Trend |
|---|---|---|---|
| Q3 revenue ≥ $66M realizable | ≥ $66M | consensus $66.11M (Zacks, 10/28); report 10/29 | pending |
| Non-GAAP GM ≥ 40% (pricing power) | ≥ 45% | Q2 45% (8/4); TTM 32.2% (stockanalysis 10/28) lags | improving |
| InP capacity: $60M a quarter by end-2026 | on plan | Q2 commentary "ahead of schedule" (Zacks 10/28); **Tongmei financing $285–545M for capacity (8-K 10/28)** | improving |
| Chinese export permits flow; 11/27 Ga/Ge suspension extended | extended | truce to 1/10/27 (9/24); **Ga/Ge piece unverified** | unknown |
| No parent equity raise before FCF turns | none | no 424B5/S-3 among the 20 filings since 6/17 (EDGAR 10/28); **subsidiary financing with 8% redemption claims payable in AXT stock** (10/28) | mixed |

**Thesis-break exits:** China halts or slows InP permits, or 11/27 passes with new restrictions (exit at market) · Q3 <
$60M or a Q4 guide that blames permits · a parent equity raise, or redemptions settled in AXT shares. **Conviction:** Low
for a trade. Up if Q4 guides ≥ $77M with permits unchanged and 11/27 is extended in writing.

### Fundamentals (stockanalysis statistics, 2026-10-28 11:03 ET, unless noted)
- Market cap **$3.97B**, EV $3.65B. **Forward P/E 38.7**, P/S 29.8, forward P/S 11.1 (Zacks: TTM P/S 28.5× vs an
  industry 13.0×).
- TTM revenue $125.5M, GM 32.2%, op margin 3.1%, **FCF −$19.6M**. Shares 64.20M, **+19.5% y/y**.
- **Cash: data conflict.** stockanalysis shows **net cash $315.7M ($4.92/share)**. The Q2 release had **cash, equivalents
  and investments of $749M** at 6/30 (Semiconductor Today, 8/4), and the 10/9 entry had ≈ $616M net cash (10-Q). The
  difference probably comes from how long-term investments are counted. Not resolved this session.
- Q2 (8/4): revenue $47.6M, InP $30.7M, non-GAAP GM 45%, net income $11.9M ($0.19). Q3 opex ≈ $10.5M.

### News & catalysts (last 30d / next 90d)
- **2026-10-28 — mixed — 8-K: Tongmei private financing, RMB 1.91–3.67B (≈ $285–545M)** to expand InP capacity, closing
  expected in December. It is confirming on capacity and customer support, and a cost on minority leakage (≈ 26.6% at the
  max), 8% redemption claims and possible AXT-share settlement. Stock +5–6% today.
- 2026-10-26 — neutral — +8% intraday "without new fundamental headlines" (StocksToTrade, updated 10/26).
- 2026-10-22 — neutral (sector) — **−13.0%** close in the post-Meta optics/AI sell-off; low $51.00 (the higher low).
- 2026-10-05 — neutral — BlackRock 13G/A (EDGAR). No insider Form 4/144 since 8/19.
- 2026-09-24 — confirming (policy) — US-China truce extended to 1/10/2027. The Ga/Ge suspension date (11/27) is not
  confirmed as extended.
- **Next:** **10/29 Q3** · 12/20 Tongmei deal minimum-close deadline · **11/27 Ga/Ge suspension expiry** · 1/10/27 truce
  expiry.

### Positioning & sentiment
- Short interest **10.79M = 17.5% of float**, 1.25 days to cover (stockanalysis 10/28; settlement date not shown). That
  is squeeze fuel either way on the print.
- Analysts **Buy (5), PT $91.60** (stockanalysis 10/28, unchanged since July: stale). Zacks Rank #3 (Hold).
- Crowded: 2× long/short single-stock ETFs (10/9 entry), up 244% YTD (Zacks).

### What would make me wrong
- A blowout Q3 with permit upside and a written 11/27 extension could re-rate it toward $80–90 without a pullback. The
  rules would miss it. That is the cost of not owning a Beijing-permit binary on a $3.4k account.
- A close back under **$51.00** after the report ends the higher-low case.
- Any sign that the Tongmei investors' redemption claims are being met with AXT stock means dilution at the parent.

### Sources
- `levels.py AXTI` and zone checks, Yahoo chart API, quote 2026-10-28 10:52 ET. Chart PNG above
- AXT 8-K, 10/28/2026 (accession 0001213900-26-113058): https://www.sec.gov/Archives/edgar/data/1051627/000121390026113058/0001213900-26-113058-index.htm · press release https://www.sec.gov/Archives/edgar/data/1051627/000121390026113058/ea030977401ex99-1.htm — fetched 10/28
- [Zacks via TradingView: AXTI before Q3](https://www.tradingview.com/news/zacks:dc7ce6b80094b:0-axti-stock-before-q3-earnings-release-to-buy-or-not-to-buy/) — fetched 10/28
- [Semiconductor Today, 8/4: AXT returns to profit](https://www.semiconductor-today.com/news_items/2026/aug/axt-040826.shtml) — fetched 10/28
- [stockanalysis AXTI statistics](https://stockanalysis.com/stocks/axti/statistics/) — 10/28 11:03 ET
- [optionslam AXTI](https://www.optionslam.com/earnings/straddle/AXTI) — fetched 10/28
- [StocksToTrade, 10/26](https://stockstotrade.com/news/axt-inc-axti-news-2026_10_26/) — fetched 10/28
- [Rare Earth Exchanges, 9/24: truce extended to 1/10/2027](https://rareearthexchanges.com/news/us-china-trade-truce-rare-earth-chokepoints/) · [CNBC, 9/24](https://www.cnbc.com/2026/09/24/us-china-trade-truce-bessent-trump-xi.html) (403 on fetch; headline via search)
- [CNBC, 11/9/2025: China suspends Ga/Ge/Sb ban to 11/27/2026](https://www.cnbc.com/2025/11/09/china-suspends-ban-on-exports-of-gallium-germanium-antimony-to-us.html) (via search)
- [AXT Q4'25 results, 2/19/2026](https://investors.axt.com/Investors/news/news-details/2026/AXT-Inc--Announces-Fourth-Quarter-and-Fiscal-Year-2025-Financial-Results/default.aspx) (via search, report date)
- EDGAR filing list, CIK 1051627 — fetched 10/28

---

## AXTI — update 2026-10-19

**Verdict:** WATCH, setup failed · re-derive after the **10/29** report · **Conviction:** Low on the setup. The 10/14
zone ($62–63.50, stop $54) broke on 10/15 (low $53.31) and again on 10/16 (close $51.47). It is now **under the 200-DMA**.

| | |
|---|---|
| Price | **$56.63** (2026-10-19, 10:35 ET, +10.0%); close $51.47 (10/16, −11.1%); 10-day low **$50.57** |
| 20 / 50 / 200-DMA | $72.4 / $70.2 / **$63.2** — price −19.3% under the 50, −10.5% under the 200 |
| RSI(14) · ATR(14) | 39.4 · **$6.69 = 11.8% a day** · −60% from the 5/26 high of $143.16 |
| Report | **10/29** after the close (set 10/1); ≈ ±20% typical move |
| China | The Ga/Ge/Sb export-ban suspension to the US runs **to 11/27/2026**; licences and the military end-user ban still apply. No extension news yet. InP substrates were not in the original controls; Tongmei got InP export permits in Aug 2025 |

A +10% day at an 11.8% ATR is one normal move, not evidence. Under the 200-DMA there is no trend to buy into. After the
report, a fresh zone needs a higher low above $50.57 and a stop within 1.5 ATR. Analysts' 2027 revenue estimates rose
from ≈ $222M to ≈ $461M between 6/30 and 9/30 (TIKR), so the business case is intact; the chart is not.

**Sources:** Yahoo chart API AXTI 1y daily, fetched 2026-10-19 10:35 ET · [TIKR, 10/8: AXT fell 10% as estimates doubled](https://www.tikr.com/de/blog/axt-stock-fell-10-in-a-day-even-as-analysts-more-than-doubled-their-2027-revenue-estimates-heres-where-the-stock-could-go) · [Mining Technology: China suspends export ban to the US](https://www.mining-technology.com/news/china-suspends-ban-exports-us/) · [TipRanks: export controls and AXT](https://www.tipranks.com/news/could-chinas-new-export-controls-impact-axt-nasdaqaxti).

---

## AXTI — AXT Inc. — check 2026-10-14 (price reached the zone)

**Verdict:** BUY allowed, through the desk, on a daily close ≥ $62 (October exception, buy #9) · **Conviction:** Med.
$62.09 at 12:45 ET (Yahoo). −28% in 7 sessions (86.66 on 10/5 → 61.98 on 10/12), in the optical and memory sell-off.
It is sitting on the 200-DMA (≈ $62.7). Today's low of $61.00 held above the 10/13 low of $60.05, and the 10/13 session
reversed from 60.05 to close 64.63. 50-DMA $71.5, RSI 41, ATR $6.51 (10.5%).
Zone $62–63.50, stop $54 (under the Sep 1–3 lows; 1.2 ATR, so noise can reach it), sell zone $84–88 → **R/R 2.7:1 at $62**.
Size ≈ $190 (≈ 5%), risk to the stop ≈ $25 (0.7%). Holding into the **10/29 report means a ±20%+ gap** (≈ ±$38 on $190).
Pre-report buys stop on 10/23. China's Ga/Ge pause lapses 11/27. The thesis checks from 10/9 below still apply.

---

## AXTI — AXT Inc. — deep dive 2026-10-09

**Verdict:** WATCH (not BUY today) · **Conviction:** Med — the best business of the two optical names asked about
(an upstream bottleneck with pricing power, profits and net cash), but at $68.85 the reward/risk is 1.0:1. It reports
in 14 sessions, and one government in Beijing can switch its exports off.

| | |
|---|---|
| Price | **$68.85** (2026-10-09, 12:37 ET, −3.9%); close **$71.66** (2026-10-08, −10.2%) |
| 50-DMA / 200-DMA | **$71.61** rising / **$61.94** rising (10/9) — price under the 20 and 50, above the 200 |
| 52-wk high / low | $143.16 (2026-05-26) / $4.00 (2025-10-10) · **−52% from the high, +1,209% in a year** |
| RSI(14) · MACD · ATR(14) | 44.9 · bearish cross at the 10/8 close · **$6.82 = 10.0% a day** |
| Entry zone | **$62.00–63.50** (rising 200-DMA $61.9–62.3 + Sep 8 low; April offering price $64.25) |
| Invalidation (stop) | **$54** (under the Sep 1–3 lows; −15.0% from $63.50) / or event: China halts InP permits, Q3 < $60M, a new equity raise |
| Target 1 / 2 | **$84–88** sell zone (Oct 7 gap $83–84, Oct 2–6 swing high $87.5–88.4) / $96–98 (Aug 17 high) |
| Reward/risk (T1) | **2.2:1 at $63.50 · 2.75:1 at $62** ✓ — at today's price **1.0:1** ✘ (and the stop would sit 21.6% under cost, past the −15% hard exit) |
| Size | **starter $190 ≈ 5% of the sleeve** in one fill. Risk to the stop ≈ $27 = 0.7% |
| Timeframe | months (thesis runs on the 2026–27 InP capacity ramp) |
| Next earnings | **2026-10-29 after the close (confirmed, Business Wire 10/1)** — 14 sessions. Blackout 10/26–10/29 |

### Thesis
AXT makes the indium-phosphide (InP) wafers that the lasers in AI optical transceivers are built on. In 2026 InP
became a bottleneck: Lumentum's CEO said the InP shortage "has surpassed that of DRAM and NAND" (TrendForce 8/6), and on
10/8–10/9 that optical parts are sold out into early 2029. AXT is one of three real suppliers (with Sumitomo and JX), and
the customers are paying in advance: Coherent prepaid $22.3M (7/2 8-K), Lumentum is putting down 2 × $43.5M deposits for
a 6-year reservation (7/29 8-K), and Casela committed RMB 173M for 2027, half prepaid. Q2 revenue was $47.6M, +165% YoY,
with InP alone at $30.7M (it was $3.6M a year earlier). Gross margin is 44.9% and the company made a profit. Q3 guide is
$66M. InP capacity is planned to reach ≈ $60M a quarter by end-2026 and ≈ $130M by end-2027. Backlog is "well over" $100M.
Balance sheet: ≈ $616M net cash (6/30 10-Q), ≈ $9.40 a share. **The market prices this in already**: EV ≈ $3.9B is 31×
trailing sales, 17.8× FY26 consensus ($218M) and 8.4× FY27 ($461M); FY27 EPS consensus $2.25 puts it at ≈ 30×. If the
2027 ramp is delivered it is fair to cheap. If it is not, it is expensive.

### The risk that matters: China
- **All production is in Beijing** (subsidiary Tongmei), and no capacity outside China is planned.
- Every substrate it sells abroad (InP, GaAs, Ge) needs a Ministry of Commerce export permit, and AXT can only apply
  once an order is in hand. InP was added to the list on 2025-02-04, and revenue bottomed in Q2 2025 at $18M with an
  8% gross margin.
- **Shipments of InP to the US are still blocked.** The 10-Q (8/13) says AXT is "unable to estimate when" permits will
  come. North America was $161K of Q2 revenue. China itself was more than 50% of Q2 revenue.
- China's suspension of its gallium/germanium export ban to the US **lapses on 2026-11-27** (Nov 2025 truce; one
  source says 11/10). Indium is not covered by it. China's revised Foreign Trade Law (in force 2026-03-01) widens
  Beijing's power to restrict exports.
- This is a kill switch that sits outside the fundamentals. No stop protects against a gap through it.

### Chart & technicals (Yahoo daily bars computed by the desk; matches stockanalysis 10/9)
- **Structure**: peak $143 (5/26), then −74% to $36.73 (7/29). Since then: a higher low at $52.8–54.8 (9/1–3), a lower
  high at $88.4 (10/6), and now $68.85. That is a contracting range of **$53–97** inside a long-term uptrend (rising
  200-DMA).
- **Short term it is weak**: 4 down sessions, a bearish MACD cross, a −10.2% day on 10.05M shares (above the 20-day
  average of 8.31M, i.e. distribution), and **−3.9% on 10/9 while LITE was +6.5%, AAOI +6.1% and COHR +2.4%**. That
  relative weakness is a warning, not a discount.
- **Volatility**: ATR is 10% a day, and 13 of the last 50 sessions moved ±10%. The plan's hard exit (−15% from cost) is
  only 1.5 days of normal noise. That is why the zone sits on support and the size is a starter.
- **Supports**: $64.25–65.2 (offering price, Sep 10–17 lows) · **$61.9–62.3 (200-DMA + Sep 8 low)** · $56.9–57.2 ·
  $52.8–54.8 · $48.7–52.8 (Jul 31 earnings gap) · $36.73.
- **Resistances**: $71.2–71.7 (50-DMA) · $74.3–75.5 (20-DMA) · $77.25–78.70 (open 10/8 gap) · **$83.2–84.0** ·
  **$87.5–88.4** · $96–97.8 · $143.16.

### Fundamentals
| Quarter | Revenue | YoY | GAAP GM | Op margin | Net income | FCF |
|---|---|---|---|---|---|---|
| Q3'25 | $27.96M | +18% | 22.3% | −4.0% | −$1.95M | −$11.3M |
| Q4'25 | $23.04M | −8% | 21.0% | −16.6% | −$3.59M | +$1.3M |
| Q1'26 | $26.92M | +39% | 29.6% | −5.9% | −$1.66M | −$13.1M |
| **Q2'26** | **$47.59M** | **+165%** | **44.9%** | **+21.9%** | **+$11.1M** | +$3.6M |
- TTM free cash flow is still **−$19.6M**. The InP pricing tailwind: 2-inch wafers went from 550 to 880 yuan (+60%) in H1
  2026 and 3-inch from 1,800 to 3,200 yuan (+78%) (Nomura via Yahoo, 8/17).
- **Dilution: shares +41% in 9 months** (46.6M on 11/1/25 → 65.6M on 8/3/26). Two raises: Dec 2025 at $12.25 ($100M)
  and **Apr 2026 at $64.25 ($632.5M)**. The automatic shelf is still effective, and authorized shares were raised to 120M.
- Tongmei withdrew its STAR-market IPO (7/8). Funds can redeem ≈ $49M at cost. A Hong Kong listing would take ≈ 1 year.
- Competition is coming: JX plans 7–10× its InP capacity by FY2030 and Sumitomo 3.1× by FY2028 (TrendForce, weakly
  sourced). The shortage, and the pricing with it, probably eases in 2028.

### News & catalysts
- 2026-10-08 — neutral — −10.2% in a sector-wide optics sell-off (COHR −9.6%, AAOI −13.6%), no company news.
- 2026-10-05 — confirming — BlackRock 13G/A at 14.3%, up from 7.1% (index buying after the S&P 600 add).
- 2026-10-01 — confirming — Q3 report set for **10/29** after the close.
- 2026-09-29 — neutral — Zacks Strong Buy → Hold.
- 2026-09-21 — confirming — joined the S&P SmallCap 600 (+11.4% on the announcement, +14.1% on the day).
- ~2026-09-16 — confirming — Needham names AXT a co-packaged-optics beneficiary, PT $90.
- 2026-09-15 — **breaking risk** — US-bound export approvals still unresolved (NTD).
- **Next 90 days**: 10/29 Q3 (guide $66M, EPS $0.30–0.32) · **11/27 China Ga/Ge truce expiry** · Q4 guide and any
  InP-to-US permit.

### Positioning & sentiment
- Short interest 8.81M = **14.3% of float**, 1.1 days to cover (9/15).
- **Insiders: ≈ $73M sold since February, zero buys.** The CEO sold $22.3M at ≈ $112–113 on 6/1–2, the CFO $21.3M in
  March, and a director at $96.07 on 8/17.
- Consensus Buy, average PT **$91.60** (5 analysts; stockanalysis, data from 7/31 — stale). MarketBeat has Hold / $77.
- **Crowded**: 2× long and 2× short single-stock ETFs (AXTX/AXTQ since 8/18; AXTU), "short-squeeze dynamics"
  headlines, and daily volume ≈ 13% of the float.
- The quorum for shareholder meetings was cut to 33⅓% (7/26) after the 2026 meeting barely made quorum. A governance yellow flag.

### Potential — the honest range
- **Upside** if the ramp and permits deliver: $96–98 (+40%), with the $143 high (+108%) possible in 2027.
- **Downside** if Beijing slows permits or Q3 misses: the July gap $48.7 (−29%) or the July low $36.7 (−47%). Net cash
  (≈ $9.40/share) is the only hard floor.
- It can do either in a quarter. "High potential" is true, and the potential runs in both directions.

### What would make me wrong
- A daily close **under $54** (the Sep 1–3 higher low fails, and the range breaks down).
- China halts or slows InP export permits, or the 11/27 truce lapses with new restrictions → **exit at market**
  whatever the price.
- Q3 revenue under $60M, or a Q4 guide that blames permits.
- A new equity raise off the open shelf before FCF turns positive.
- Gross margin falling back under 40% (would mean pricing power is fading as Japan adds capacity).

### Sources
- Yahoo chart API AXTI 5y daily bars (fetched 2026-10-09 12:21 ET); https://stockanalysis.com/stocks/axti/ (10/9 12:37 ET)
- https://stockanalysis.com/stocks/axti/history/ · /statistics/ · /financials/?p=quarterly · /forecast/ · /ratings/ — 2026-10-09
- Q2 10-Q https://www.sec.gov/Archives/edgar/data/1051627/000143774926027677/axti20260630_10q.htm — filed 2026-08-13
- Tongmei 8-K https://www.sec.gov/Archives/edgar/data/1051627/000143774926022984/axti20260629_8k.htm — 2026-06-29
- Offering 8-K https://www.sec.gov/Archives/edgar/data/0001051627/000121390026045867/ea0286957-8k_axt.htm — 2026-04
- Q3 date https://www.businesswire.com/news/home/20261001072530/en/ — 2026-10-01
- Q2 call https://www.fool.com/earnings/call-transcripts/2026/07/30/axt-axti-q2-2026-earnings-call-transcript/ — 2026-07-30
- https://www.semiconductor-today.com/news_items/2026/aug/axt-040826.shtml — 2026-08-04
- https://www.trendforce.com/news/2026/08/06/news-inp-shortage-emerges-as-ai-optical-interconnect-bottleneck/ — 2026-08-06
- https://finance.yahoo.com/markets/stocks/articles/axt-inc-axti-soars-19-185832685.html — 2026-08-17
- https://finance.yahoo.com/markets/stocks/articles/bull-day-axt-axti-092000532.html — 2026-09-18
- https://www.marketbeat.com/stocks/NASDAQ/AXTI/short-interest/ — 9/15 settlement
- https://fastmarkets.com/insights/china-suspends-export-prohibition-on-superhard-materials-us — Nov 2025
- https://247wallst.com/investing/2026/10/01/coherent-jumps-10-on-photonlink-push-and-bernsteins-outperform-start-lumentum-rises-9-corning-advances-3/ — 2026-10-01
