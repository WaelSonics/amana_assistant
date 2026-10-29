# EWY — iShares MSCI South Korea ETF — research log

One file per ticker; newest entry first. Each entry is dated; numbers are as of that date.

Entries:
- 2026-10-28 (deep dive; not held; §4a not met)

---

## EWY — iShares MSCI South Korea ETF — deep dive 2026-10-28

**Verdict:** WATCH. **Second** for the single memory slot, behind MU. No zone passes, and §4a is not met: there is no close back
above the $165 stop, and the 10/22 low was a lower low. · **Conviction:** Med on the holdings, Low on the setup. 45% of the fund
is Samsung plus SK hynix, the two cleanest prints of this cycle, and its ATR is the lowest in the group (3.8%). Against that: it
is a won, Korean-rates and index-rule bet as well as a memory bet.

| | |
|---|---|
| Price | **$163.75** (2026-10-28 10:52 ET, `levels.py`). +4.0% on the 10/27 close of $157.46; +0.3% on the 10/13 stop fill of $163.23; +10.4% off the 10/22 low of $148.30 |
| Entry zone | **None passes** (checks below) |
| Invalidation (stop) | For any future buy: under the 10/22 low of $148.30, or the next higher low. Event: Samsung or SK hynix guides memory prices or HBM volume down |
| Target 1 / 2 | $166.82–166.90 (10/13 high / 20-DMA), then $172.62–176.08 (8/4 and 7/23 swing highs, 50-DMA) / $190.11–193.93 (8/17, 9/9 highs) |
| Reward/risk (T1) | ✘ 0.88–1.73:1 across the candidate zones |
| Size | $0 |
| Timeframe | months |
| Next earnings | n/a (ETF; `levels.py`: not in the calendar). Holding events: **Samsung detailed Q3 + call 10/29 (KST)** · index change ≈ **11/9** · Bank of Korea **11/26** |

### What changed (no earlier research file; desk history)
- **Account history:** the 10/8 add at $178.09 was an OVERRIDE ($200 > $150, and it took EWY to 16.6%). The stop was lowered
  172 → 165, also an OVERRIDE, and gapped through: **stopped 10/13 at $163.23, −$34.93**. Lowering the stop cost ≈ $30.51 (journal
  10/10, 10/13; PLAN §6b). The 10/27 check said: EWY only after Samsung's 10/29 print, only as the one memory name, MU first.
- **Since then:** SK hynix's record Q3 and a **KOSPI +6.63%** day (10/28) put EWY back above its 200-DMA. The 10/28 open left a
  gap: 10/27 high $158.15 to today's low $162.74.
- **§4a:** not met. The fall made a **lower** low ($148.30 on 10/22, under 10/15's $149.71), and the last close ($157.46) is under the
  broken $165 level. Today's $163.75 is intraday and still under 165.

### Thesis scorecard (section B)
| Pillar (falsifiable) | Expected | Status (dated) | Trend |
|---|---|---|---|
| Top-2 holdings' memory profits keep rising | beats, no guide-down | SK hynix Q3 OP ₩83.33T, +37.6% q/q, beat by 9.7% (10/28). Samsung prelim Q3 OP ₩107.4T, +20.1% q/q, beat by 1.3%, but revenue missed by 2.6% (10/8) | improving |
| Foreign money returns to Korea | net foreign buying | 10/28: foreigners +₩815.83B, institutions +₩960.79B, retail −₩1.8T (Korea JoongAng Daily; Asia Business Daily reports +₩1.152T foreign) | improving (one day) |
| The won holds | no sharp weakening | 1,337.7/$ on 10/28, 10.7 won weaker on the day (KJD) | stable; watch |
| Concentration stays below a 2-stock bet | Samsung + SK hynix ≤ 50% | **22.81% + 22.34% = 45.15%** (Schwab, 10/28 10:44 ET). The index changes to MSCI Korea 25/50 **Daily** 25 Capped ≈ 11/9 (iShares, announced 10/23); the weight effect is unverified | stable; event risk |
| Korean rates don't choke the rally | BOK on hold | BOK held at 3.00% on 10/22 after two hikes; inflation 2.9% (Sep). The next meeting is **11/26** and experts expect another hike (QNA 10/22) | **weakening** |

- **Thesis-break exits:** a memory guide-down from Samsung or SK hynix; the index change lifting the two names above 50% (EWY
  becomes a 2-stock memory bet, which MU does better without the FX risk); a BOK hike plus foreign selling that takes the KOSPI back
  under 5,700 (the 10/27 level).
- **Disconfirming evidence:** Samsung's Q3 revenue missed (10/8). SK hynix's net profit missed on a ₩11.6T FX loss and ₩22.9T of
  investment losses (24/7 Wall St, 10/28): the won cuts both ways. Retail sold ₩1.8T into the 10/28 rally. KOSPI buy-side
  sidecars fired two sessions in a row (programs chasing).
- **Conviction: Med.** It rises on a Samsung shareholder-return plan on 10/29 and an index change that does not raise the memory
  weight. It falls on a BOK hike on 11/26.

### Samsung detailed Q3, 10/29 KST (the holding's catalyst; EWY itself does not report)
- **Expected:** the chip division's (DS) operating profit at ≈ the whole-company ₩107.4T or above. Chosun estimate ≈ ₩110T (via
  search, not verified). Memory margin estimates range from 76% to > 80% (via search, not verified). Hopes are building for a
  stronger shareholder-return plan on the call (KJD and Asia Business Daily coverage, 10/28).
- **Already priced:** Samsung +9.01% on 10/28 to ₩242,000.
- **Decision written now:** nothing is held. No buy on 10/29 (PCE morning, and the client's commitment to 11/2). Re-run
  `levels.py EWY` on 11/2.

## Thesis
EWY is the cheapest way to own Samsung and SK hynix together: 45% of the fund (10/28), the two largest DRAM/HBM makers, which
printed the strongest numbers of the cycle (SK hynix 79.7% operating margin, "sold out through 2029"). The other 55% is Korean
banks, autos, biotech and Samsung affiliates. That makes it less of a pure memory bet than MU, SNDK or WDC. It also carries the
lowest volatility of the four (ATR 3.8%). Fund P/E 17.55, P/B 1.92 (iShares, 10/27). What you also buy: the won, BOK hikes, retail
leverage (sidecars both ways), and an index-rule change on 11/9. MarketVector's capitulation indicator hit 97.9 in the week before
10/23. EWY was higher one month later in 8 of 10 past signals, median +6% at one month and +16% at three (one analyst, 10 cases
since 2010).

## Chart & technicals
`levels.py EWY`, quote 2026-10-28 10:52 ET:
```
EWY  $163.75 (2026-10-28 10:52 ET); last daily bar 2026-10-28 close $163.74
  20/50/200-DMA  166.90 / 176.08 (falling) / 162.17 (rising)   price vs 50 -7.0%, vs 200 +1.0%
  RSI(14) 47.4   ATR(14) $6.15 = 3.8% a day   52-wk 86.90–220.89 (-26% from the high)
  Trend: above a rising 200-DMA
  Chase guard: ok
  Next report: not in the 3-month calendar (ETF, or more than 3 months away)
  Swing support below: 154.20, 142.64   resistance above: 172.62, 175.08, 190.11
```
- **Structure:** lower highs from $220.89 (6/18) to $193.93, $193.00 and $192.87 (9/9, 9/22, 10/2). October broke the 50- and
  200-DMA. The low was $148.30 (10/22). Today's gap puts it **1% back above the 200-DMA**, right under the falling 20-DMA (166.90).
- **Not in the script's lists:** the 10/22 low of $148.30 (the §4a reference) and the 20-DMA / 10/13 high at ≈ $166.8–166.9
  (resistance below its "nearest" $172.62). The unfilled gap at $158.15–162.74 is the first pullback target.
- **Volume:** 6.5M by 10:52 ET, against 14.2M on 10/27 and 33.1M on the 10/15 flush (Yahoo bars).
- **Chart:** `/tmp/claude-1000/-home-waelas-wael-amana-amana-assistant/cf7235bd-03e5-456e-8948-a8c2229a57bd/scratchpad/charts/EWY.png`.
  It shows the price just back over the 200-DMA, with the 20- and 50-DMA falling above.

**Zone checks** (`levels.py EWY --zone … --size 250 --sleeve 3426`, 10/28 10:52 ET data):
```
# 7/17 swing-low zone 154-156 / 144.80 / 172.62 (script's T1)
    at low     154.00: R/R 2.02:1, stop 1.50 ATR (6.0%)   ✘ stop < 1.5 ATR
    at mid     155.00: R/R 1.73:1, stop 1.66 ATR (6.6%)   ✘ R/R < 2
    at high    156.00: R/R 1.48:1, stop 1.82 ATR (7.2%)   ✘ R/R < 2
    size $250 ≈ 1.6129 sh at the mid; risk to stop $16.45 = 0.5% of $3,426   ✓ ≤ 2%
# same zone, honest T1 = 166.82 (10/13 high; 20-DMA 166.90)
    at low     154.00: R/R 1.39:1 ✘ · at mid 155.00: R/R 1.16:1 ✘ · at high 156.00: R/R 0.97:1 ✘
# 200-DMA / gap retest 160-162.50 / 151 / 172.62
    at low     160.00: R/R 1.40:1, stop 1.46 ATR (5.6%)   ✘ R/R < 2; stop < 1.5 ATR
    at mid     161.25: R/R 1.11:1, stop 1.67 ATR (6.4%)   ✘ R/R < 2
    at high    162.50: R/R 0.88:1, stop 1.87 ATR (7.1%)   ✘ R/R < 2
# breakout retest over the 50-DMA 175-177 / 165.50 / 190.11
    at low     175.00: R/R 1.59:1 ✘ · at mid 176.00: R/R 1.34:1 ✘ · at high 177.00: R/R 1.14:1 ✘
```
**No passing zone.** At a $6.15 ATR, 2:1 needs **$18.45 of open air** above the entry. The only pocket wide enough is
$148.30 → $166.82, and an entry with a 1.5-ATR stop inside it pays < 2:1 to 166.82.

**The conditions that would create a zone:**
- **(a)** ATR(14) at **≤ ≈ $5.5** and a higher low above $148.30. Then ≈ $150 with a stop at $142 (under the 7/29 low of $142.64)
  pays 2:1 to ≈ $166.8.
- **(b)** A daily close above the 50-DMA (≈ $176) and ATR at **≤ ≈ $4.7**. Then a retest of ≈ $176 with a stop at ≈ $169 pays 2:1
  to $190.11.

Either way, §4a also needs the close above $165 or the higher low first.

## Fundamentals (fund level)
- iShares (10/27): NAV **$158.0952**, net assets **$23.17B**, 76 holdings, expense ratio 0.59%, IT sector 51.57%, P/E 17.55,
  P/B 1.92, NAV total return YTD **+56.41%** (10/26). 12-month trailing yield 1.11% (9/30).
- **Top holdings** (Schwab, 10/28 10:44 ET): Samsung Electronics 22.81%, SK hynix 22.34%, SK Square 2.64%, Samsung
  Electro-Mechanics 2.53%, KB Financial 2.17%, Shinhan 1.61%, Hyundai Motor 1.56%, Hana Financial 1.44%, Celltrion 1.42%,
  Samsung SDI 1.36%. Memory-linked, counting SK Square (SK hynix's parent), is ≈ 47.8%.
- **SK hynix Q3** (10/28): revenue ₩104.62T, operating profit ₩83.33T (79.7%), net income ₩39.78T (missed on FX and investment
  losses), ≈ 4× forward earnings and ≈ ₩99T of net cash (24/7 Wall St; Seoul Economic Daily).
- **Samsung preliminary Q3** (10/8): revenue ₩195T (+127% y/y), operating profit **₩107.4T** (+783% y/y, 55.1% margin) (Seoul Economic Daily).

## News & catalysts (last 30d / next 90d)
- 10/28: **KOSPI +6.63% to 6,012.44**, its first close above 6,000 in 10 sessions. Samsung +9.01%, SK hynix +10.89%, buy-side
  sidecar for the second session running; won 1,337.7 (Korea JoongAng Daily). **Confirming.**
- 10/28: SK hynix record Q3: sold out through 2029, LTAs cover > 50% of 2027–28 capacity, ≈ ₩100T of 2026 returns, 2027 capex up
  significantly (24/7 Wall St; Seoul Economic Daily). **Confirming**, with a supply caveat.
- 10/23: iShares announces the index change to MSCI Korea 25/50 Daily 25 Capped, effective ≈ 11/9 (iShares fund page).
  **Neutral**: event risk around rebalancing.
- 10/23: MarketVector capitulation indicator at 97.9 (threshold 95) with EWY at $149.06 (KuCoin repost of Benzinga). **Neutral**:
  a sentiment extreme, not a level.
- 10/22: BOK holds at 3.00% after two hikes; next meeting 11/26, a hike expected (QNA). **Breaking-risk.**
- Next: **10/29 KST** Samsung detailed Q3 + call · 10/29 PCE (US) · ≈ 11/9 index change · 11/26 BOK.

## Positioning & sentiment
- **Short interest:** not available (the Nasdaq API returned nothing for EWY). Unverified.
- **Flows:** foreign and institutional buying returned on 10/28 while retail sold ₩1.8T (KJD). Program buying tripped sidecars on
  10/27 and 10/28. EWY net assets $23.17B (10/27).
- **Crowding:** the memory-driven KOSPI went from a 9,410 record in June to ≈ 5,817 at one point (Yahoo/24/7, undated snapshot;
  not verified), then 6,012 today. The market is retail-leveraged and moves in sidecars both ways.

## What would make me wrong
- Samsung's call (10/29) adds a large buyback, and the KOSPI keeps running. EWY clears 166.9 and 176 without a pullback, and the
  desk misses +7–10% on a $250 line (≈ $20–25).
- The won strengthens sharply and adds a currency tailwind on top of memory. That is the reverse of the FX loss that hit SK hynix's
  Q3 net income.

## Sources
- `levels.py EWY` (Yahoo chart API), 10/28 10:52 ET data, with the zone checks above
- [iShares MSCI South Korea ETF fund page](https://www.ishares.com/us/products/239681/ishares-msci-south-korea-capped-etf) — data as of 10/26–10/27, fetched 2026-10-28
- [Schwab EWY holdings](https://www.schwab.wallst.com/schwab/Prospect/research/etfs/schwabETF/index.asp?type=holdings&symbol=EWY) — 2026-10-28 10:44 ET
- [Korea JoongAng Daily: Kospi surges past 6,000](https://koreajoongangdaily.com/business/kospi-surges-past-6000-as-sk-hynix-record-earnings-reignite-ai-rally/12943596) — 2026-10-28
- [Seoul Economic Daily: SK hynix 79.7% operating margin](https://en.sedaily.com/finance/2026/10/28/sk-hynix-posts-record-797-percent-operating-margin-in-third) — 2026-10-28
- [24/7 Wall St: SK Hynix's profit jumped 632%](https://247wallst.com/investing/2026/10/28/sk-hynixs-profit-jumped-632-as-ai-eats-the-worlds-memory/) — 2026-10-28
- [Seoul Economic Daily: Samsung Q3 prelim ₩107.4T](https://en.sedaily.com/finance/2026/10/08/samsung-electronics-posts-record-107-trillion-won-quarterly) — 2026-10-08
- [KuCoin (Benzinga repost): Korea capitulation signal](https://www.kucoin.com/news/flash/korea-capitulation-signal-flashes-ahead-of-sk-hynix-earnings) — 2026-10-23
- [QNA: Bank of Korea holds key rate at 3%](https://qna.org.qa/en/News-Area/News/2026-10/22/bank-of-korea-holds-key-rate-steady-at-3) — 2026-10-22
- [CoinDesk: KOSPI surges as SK hynix earnings fuel AI rebound](https://www.coindesk.com/markets/2026/10/28/kospi-surges-7-as-sk-hynix-earnings-fuel-ai-stock-rebound) — 2026-10-28 05:59 ET
