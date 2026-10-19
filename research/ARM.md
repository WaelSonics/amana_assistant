# ARM — Arm Holdings plc (ADR) — research log

One file per ticker; newest entry first. Each entry is dated; numbers are as of that date.

Entries:
- 2026-10-19 (update)
- 2026-10-13

---

## ARM — update 2026-10-19 (royalty ruling: closing arguments 10/20)

**Verdict:** HOLD with the $220 stop · no adds · **sell at market if Judge Noreika lets Qualcomm suspend royalties** ·
**Conviction:** Low. The binary is now dated: the bench-trial closing arguments are **Tue 10/20, 10:00 ET** (court
minute entry, 90 minutes split). The ruling can come any day after that; there is no deadline.

| | |
|---|---|
| Price | **$230.25** (2026-10-19, 10:35 ET, +1.1%); close $227.80 (10/16, −6.9%); 10/15–10/16 lows **$226.54 / $226.65** |
| 20 / 50 / 200-DMA | $282.1 / $266.8 (rising) / **$224.0** — price −13.7% under the 50, +2.8% over the 200 |
| RSI(14) · ATR(14) | 35.6 · **$16.85 = 7.3% a day** · −49% from the 6/18 high of $452.70 |
| Position | 1.5668 sh @ $255.87 = ≈ $361, 10.5% of the sleeve, **−10.0%** |
| Stop | **$220** (broker, confirmed live 10/19): only **4.4% / 0.6 ATR** below, just under the 200-DMA. Risk ≈ $16. Never lowered |
| Sell zone (⅓) | $275–281 → 0.52 sh (above cost) |
| Buy zone | $225–233 — **locked** until after the 11/4 report *and* the ruling. `portfolio_report.py` flags "IN BUY ZONE"; ignore it |
| Next events | **10/20 closing arguments** · ruling date unknown · earnings **Wed 11/4** after the close (implied ≈ ±8.8%) |

### The ruling (dated)
- **10/13 jury:** Arm breached its Architecture License Agreement and interfered with Qualcomm's Meta relationship;
  **$2** in damages ($1 per claim). Arm won the Technology License Agreement claims.
- **With the judge:** (1) whether the clause letting Qualcomm **suspend royalties for 5 years** after a material breach
  is enforceable — Qualcomm says it applies automatically, Arm says it is unenforceable; Arm itself puts it at
  "billions"; (2) whether Arm negotiated next-generation pricing in good faith. Noreika declined to decide (1) before trial.
- Rule (unchanged since 10/13): **a ruling that grants the suspension = thesis break → sell the whole line at market.**
  A ruling that voids the clause is a relief catalyst, but the adds stay locked until after 11/4.

### Gap risk, stated plainly
On a suspension ruling ARM would likely **gap through $220**. A −20 to −25% gap from $230 costs ≈ **$70–90** on this line,
about the account's whole **$56 cushion** over the $3,402 breaker (10:28 ET). The stop does not protect against a gap.
The plan does not require a sale before the ruling, and the desk does not recommend one: selling now locks ≈ −$40 and
pays the same for a coin flip in the other direction. It is the client's call. A sale is always allowed without the
desk; a re-buy is not.

**Sources:** Yahoo chart API ARM 1y daily, fetched 2026-10-19 10:35 ET · [Insurance Journal, 10/15: jury verdict and the open bench issues](https://www.insurancejournal.com/news/east/2026/10/15/889003.htm) · [Tech Times, 10/14: $2 verdict unlocks the royalty-suspension fight](https://www.techtimes.com/articles/329023/20261014/qualcomm-jury-finds-arm-breach-2-verdict-unlocks-billion-dollar-royalty-suspension-fight.htm) · [Forbes/Tirias, 10/15: who came out on top](https://www.forbes.com/sites/tiriasresearch/2026/10/15/qualcomm-vs-arm-the-jury-verdict-is-in-who-came-out-on-top/) · [24/7 Wall St, 10/16](https://247wallst.com/investing/2026/10/16/arm-and-amd-fall-5-as-qualcomm-verdict-adds-to-chip-selloff-taiwan-semiconductor-slips) · closing-argument date and time from the court minute entry as quoted in search results 10/19 (docket not fetched directly).

---

## ARM — Arm Holdings plc (ADR) — deep dive 2026-10-13

**Verdict:** HOLD with the 220 stop · no adds · **exit at market if the Qualcomm case goes against Arm on royalties** ·
**Conviction:** Low–Med — the business is intact (royalty + licensing +22%, AGI CPU demand > $2B), but the re-buy broke
§4a, the chart is still making lower lows, and a jury verdict that can cut royalties is due today.

| | |
|---|---|
| Price | **$251.74** (2026-10-13, 10:29 ET); close $255.24 (10/12); today's open/low 245.32/243.60 |
| Position | 1.5668 sh @ $255.87 = ≈ $393, **11.2%** of the sleeve (re-bought 10/12 in one $400 fill > the 8% one-fill max) |
| 50-DMA / 200-DMA | **$270.4** (rising) / **$221.5** — price is under the 20 and 50, above the 200 |
| 52-wk high / low | $452.70 (2026-06-18) / $100.02 (2026-02-05) · −25.3% from the 9/23 high of 336.98 |
| RSI(14) · ATR(14) | 39.6 · **$16.89 = 6.7%** a day |
| Stop | **$220** (broker): under the 200-DMA $221.5, just above the 8/3 swing low $219.39 — 1.9 ATR. Risk ≈ $48 = 1.4% |
| Sell zone | **$275–281** (10/8 close 275.3, 9/28 low 279.2, 50% retracement 278.2) → ⅓ = 0.52 sh. Above the avg 255.87 ✓ |
| Buy zone | $225–233 (9/3 low 225.46, 8/24 low 233.29), R/R 3.2:1+ to 275 — **locked**: October buying closed, and after the 11/4 report only |
| Reward/risk at today's price | 0.6:1 to the 50-DMA $270 · 0.9:1 to $280 ✘ — the desk would not buy here |
| Next events | **Qualcomm jury verdict (deliberations resume 10/13)** · earnings **Wed 11/4** after close (implied ≈ ±8.8%) |

### Thesis
Arm collects a royalty on almost every phone chip and a fast-growing share of data-center CPUs, and now sells its own
"AGI CPU" (Meta lead partner; OpenAI, ByteDance, Oracle, Cloudflare, Cerebras named). Q1 FY27 (Jun-26) revenue was
$1.289B, +22%: royalty $715M (+22%) and licensing $574M (+23%). Non-GAAP operating margin was 41%, and TTM FCF $1.51B.
Q2 guide: $1.38B ±$50M, EPS $0.47 ±$0.04. AGI CPU demand is > $2B across FY27–28, but only $1B of capacity is secured.
**Price:** 107× forward earnings and ≈ 51× sales (StockAnalysis 10/13), against a peer forward P/E of ≈ 67×. The price
already assumes the AGI CPU works and royalties keep compounding. Any doubt costs a lot, and beta is ≈ 3.8.

### Why it fell 25% in three weeks (dated)
- **9/21 +17% spike** on Meta's "Muse" agent, which was *assumed* (not confirmed) to run on Arm's AGI CPU. Fully retraced
  since: the 275.8–293.1 gap is filled.
- **9/18** SoftBank upsized its Arm-backed margin loan to $25B. 72% of all Arm shares are pledged. It is a loan, not a sale.
  Loan-to-value is ≈ 13% at today's price, so a forced sale would need a much deeper fall.
- **9/28** chip sell-off on oil and inflation (−8.7%). **10/8** −6.5% on an FT report that OpenAI's annualized revenue was
  ≈ $50B, not ≈ $70B. **10/12** −4.1% in the memory/CXMT sell-off.
- **10/5–10/9 Qualcomm v. Arm jury trial** (Delaware). Qualcomm alleges Arm withheld tools and broke a pricing clause, and
  asks for a ruling that lets it **stop paying royalties for 5 years**. The judge has not ruled on that clause; Arm says it
  is unenforceable. The jury had no verdict after ≈ 4 hours and resumes today. A bench ruling on good-faith negotiation
  comes later. **This is the one item that can break the thesis.**
- ARM is −24% since 9/23 against SMH −3% and NVDA 0%. Most of the fall is specific to Arm and SoftBank.

### Chart & technicals (Yahoo daily bars, computed by the desk and the agent; 10/13 10:30 ET)
- Lower highs (339 → 337 → 318) and, since 10/2, lower lows every session to 243.6 today. That is ≈ the 78.6%
  retracement (244.6) of the 219.4 → 337.0 swing. A bounce from here is possible. A higher low has **not** formed yet.
- Supports: 243.6 · 238.0 · 233.3 · 225.5 · **221.5 / 219.4 (200-DMA + Aug low)** · 200.9–193.9.
- Resistances: 252.8–256 · 263.2 · **266.3–270.4 (50-DMA)** · 275.3–281.5 · 290.2 · 318.4 · 337–339.

### Positioning & sentiment
- Short interest 16.2M = ≈ 11.4% of the 142.6M float, 2.3 days to cover (9/30). Insiders: 34 sales and no buys in 12
  months (the CFO sold at $300 on 9/21).
- Analysts: 17 Buy / 5 Hold / 0 Sell; average PT ≈ $299 (Nasdaq, 10/13; range $150–480). No downgrades or target cuts
  since 8/1.
- Earnings reactions: −1.2% / +5.7% / −10.1% / +7.4% (last 4). Options imply ≈ ±8.8% for 11/4.
- The float is only ≈ 13% of the shares (SoftBank owns 86.4%), and 2× single-stock ETFs exist. Moves get amplified.

### Calls
1. **Hold with the broker stop at 220. Never lower it.** Risk ≈ $48 = 1.4% of the sleeve, inside the 2% budget.
2. **Qualcomm rule:** a verdict for Qualcomm that comes with a royalty holiday (or the judge signalling it is
   enforceable) is a **thesis break → sell at market, whatever the price**. A verdict for Arm or a narrow damages award
   → hold, and expect a relief bounce toward $263–270.
3. **Sell zone $275–281:** price alert at 275; when it fires, sell 0.52 sh (⅓).
4. **No adds.** The buy zone of $225–233 opens only after the 11/4 report.
5. The 10/12 re-buy is logged as an OVERRIDE: §4a needs a close back above $280 or a higher low first. Neither happened,
   and price made two lower lows after the fill.

### What would make me wrong
- A daily close under $220 (the 200-DMA and the August low give way).
- A Qualcomm royalty holiday, or licensees publicly moving designs to RISC-V because of the AGI CPU or fee rises.
- An 11/4 guide that cuts royalty growth further (the CFO already moved the FY outlook toward the high teens).
- SoftBank stress forcing share sales.

### Sources
- Yahoo chart API ARM 1y daily + 1d 5-min bars, fetched 2026-10-13 10:26–10:30 ET
- https://stockanalysis.com/stocks/arm/statistics/ — 2026-10-13
- https://newsroom.arm.com/news/arm-q1-fye27-results — 2026-07-29
- https://whtc.com/2026/10/09/qualcomm-and-arm-set-for-jury-verdict-in-contract-breach-feud/ — 2026-10-09 (Reuters)
- https://finance.yahoo.com/markets/stocks/articles/qualcomm-arm-trial-ends-hung-130049760.html — 2026-10-12
- https://theedgemalaysia.com/node/818515 — 2026-09-18 (SoftBank margin loan)
- https://www.tikr.com/blog/arm-holdings-stock-fell-6-in-a-day-as-an-openai-revenue-report-hit-chip-stocks-heres-where-openai-touches-arms-business — 2026-10-09
- https://247wallst.com/investing/2026/09/28/arm-sinks-9-as-chip-selloff-deepens-qualcomm-drops-6-marvell-slides-5/ — 2026-09-28
- https://www.tradingkey.com/news/market-movers/262211846-market-movers-arm-20261012 — 2026-10-12
- https://api.nasdaq.com/api/quote/ARM/short-interest · /analyst/ARM/targetprice · /company/ARM/insider-trades · /quote/ARM/option-chain — 2026-10-13
- https://www.sec.gov/Archives/edgar/data/0001973239/000197323926000097/arm-20260331.htm — 20-F (SoftBank stake, pledge)
- https://www.ad-hoc-news.de/boerse/news/corporate-news/arm-holdings-stock-falls-2-14-percent-as-arm-sets-results-date/70235028 — 2026-10-05
