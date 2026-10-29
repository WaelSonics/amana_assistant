# 2026-10-29 — "Lower the stop and ride the upswings": tested

Client: "We need to make trades that make money; waiting forever for the perfect chance is being very safe. We can make the
stop loss lower and benefit from the up swings. If I had bought BE and Intel on 10/24 I would have made good money by now."

## The claim, checked
- 10/24 was a Saturday, so the first possible fill was the 10/26 open: BE $193.00, INTC $87.94.
- At the 10/28 close: BE $228.08 (+18.2%) and INTC $95.53 (+8.6%).
- **$190 in each = +$48.91 after fees, open.** True, but not banked: INTC reports tonight (±9.4% implied).

## Two different ideas inside "lower the stop"
1. **Lowering an existing stop** to avoid being stopped out. October measured this:
   - EWY 172 → 165: −$30.51.
   - QUBT 8 → 7: −$25.28.
   - Together −$55.79. It also fails §10 test 1 (client clarification, 10/27). **Not on the table.**
2. **Setting a wider stop at entry**, with the size fixed so the $ risk is known. Tested below.

## Test (scratchpad `dipstop_test.py`; Yahoo daily bars; $200 a trade, $1 a fill)
**The rule:**
- **Signal:** a close ≥ 15% below the highest close of the last 20 sessions.
- **Entry:** buy at the next open.
- **Exit:** the stop (intraday; a gap through it fills at the open), +25% take profit, or the close after 30 sessions.
- One position per name at a time. Concurrency is not capped, and the test does not avoid earnings.

**The universes** are both chosen with hindsight, on purpose, to bracket the answer:
- **A** — the desk's 16 AI watchlist names, 10/2024 to 10/2026. They are on the list *because* they went up.
- **B** — approximately ARKK's top holdings of early 2021 (TSLA, ROKU, TDOC, XYZ, ZM, SHOP, SPOT, BIDU, TWLO; the list is from
  memory), 2/2021 to 2/2023.

| | Stop | A: 2026 AI winners | B: 2021 hot list in the bust |
|---|---|---|---|
| No filter | −8% | +$1,557 · 360 trades · win 37% · worst run −$253 | −$1,689 · win 21% · worst run −$1,828 |
| No filter | −15% | +$2,152 · win 52% · worst run −$261 | −$1,552 · win 31% · worst run −$1,596 |
| No filter | −25% | +$2,433 · win 64% · worst run −$206 | −$1,711 · win 36% · worst run −$1,740 |
| **Trend filter** | −8% | +$330 · win 32% · worst run −$361 | −$201 · 35 trades · worst run −$273 |
| **Trend filter** | −15% | +$1,060 · win 49% · worst run −$245 | −$287 · worst run −$381 |
| **Trend filter** | **−25%** | **+$1,755 · 140 trades · win 64% · worst run −$208** | **−$315 · 21 trades · worst run −$394** |

The trend filter: buy only while the close is above a 200-DMA that is rising over 20 sessions.

**What it says:**
1. **The client's instinct is right in a winners' market.** Wider stops made more money (A), because they ride out noise.
2. **The regime decides, not the stop.** In the bust (B), every stop width lost ≈ half the account. A wider stop amplifies
   whichever regime you are in.
3. **The 200-DMA trend filter is the useful part.** It keeps ≈ 70% of A's gains at a −25% stop and cuts B's losses by ≈ 80%.
   It still loses in a bust, but survivably.
4. **The client's two picks:**
   - **INTC 10/23:** −27.7% from its 20-day high close, above a rising 200-DMA ($85.81) → **the rule buys it.**
   - **BE:** −34.6%, but under its 200-DMA ($219.29) → **the rule skips it.**

**Caveats:**
- Both lists are hindsight.
- B has only 21 filtered trades.
- With TP +25% and stop −25%, the payoff is 1:1, so the edge is the 64% win rate in A. That fell to 38% in B.
- Concurrency is not capped, so the dollar totals overstate what $1,240 of cash can do.
- Earnings are not avoided.
- Even A's best case has a −$208 losing run, while the account sits $30 above the breaker.

## Desk view
- **This is a better answer than v3's zone rule for these names.** v3 produced zero entries on 10/28. The trend-filtered dip
  rule trades, and it was tested in both regimes.
- **It is a rule change, decided by the client in writing**, not an override. As tested it breaks two v3 rules:
  - the 15% hard exit;
  - R/R ≥ 2:1 to the nearest resistance.
- The client chose how to use it: see below.

## Client decision (10/29): live from 11/2
- **The options offered were:**
  - live from 11/10, small (desk recommendation: after the AMD 11/3 and TTWO 11/9 reports);
  - live from 11/2;
  - paper-trade to 12/31;
  - keep v3.
- **The client chose live from 11/2.** It is written as PLAN §3c: $150 a trade, at most 2 open, stop −25%, TP +25%,
  30-session exit, desk note first, earnings blackout for entries, breaker still governs.
- **The kill switch at −$75 net is a desk addition.** The client may strike it.
- **Desk caution, said once:** the first week holds two binaries on held names, with the account ≈ $30 above the breaker.
  One full dip stop (−$37.50) plus a weak AMD print would put the account under it, and that pauses new dip trades.

## First scan (`levels.py`, 10/29 09:39 ET, provisional: the bar is open)
- **Provisional signals:**
  - BE −23.6% from its 20-session high close, above a rising 200-DMA. Note that it qualifies now, at ≈ $226, not at the $193
    low: on 10/23 it was under the 200-DMA.
  - INTC −22.7%: reports tonight.
  - SNDK −21.1%: reports tonight.
  - ANET −15.1%: blackout to 11/3.
  - LITE −16.8%: blackout 11/2–11/5.
- **No signal:**
  - under the 15% dip line: AMD (held), MU, WDC, NVDA, TSM;
  - failing the 200-DMA filter: ARM, AAOI, AXTI, EWY, RKLB, GOOGL.
  - GOOGL opened ≈ −13% after its 10/28 report (≈ $281.53); the cause is not yet confirmed.
- **The buy list for Mon 11/2 comes from the 10/30 close.** Likely candidates: BE, plus INTC and SNDK if their signals survive
  the reports. One memory name only. ANET and LITE are blocked by their blackouts.

## Morning check (Yahoo, 10/29 09:44 ET)
- **Account $3,417.39, $15.52 above the breaker.**
- **TTWO $193.44 (≈ −3%), 1.8% above its $190 stop.** No confirmed cause. Claims of a 2027 GTA VI delay circulated on 10/28;
  IBT and the Xbox listing (11/19, preload 11/12) contradict them.
  - The thesis breaks only on an official Rockstar date change, and then the line exits. Otherwise the stop decides.
  - A $190 fill is ≈ −$8 from here and −$54.35 from cost; the account would stay ≈ $7 above the breaker.
- **Other moves:**
  - GOOGL ≈ −13% after its report ($283.57); cause unconfirmed (the Q2 pattern was capex and free cash flow).
  - MRK +4.8% after its report ($148.64): above $147, the condition for a zone. Re-run from the 10/30 close.
  - XLV made a new high ($183.84).
- **The 10/28 Fed decision is not yet confirmed by the desk** (search returned previews only).
- Flag Board v32 published.

## "Would v3 have blocked the post-reset winners?" Yes: all seven (client question, 10/29)
The check used bars up to the night before each buy, the closest stop v3 allows (1.5 ATR), and T1 = the nearest resistance.

| Buy | ATR | 1.5-ATR stop | T1 | R/R | v3 | §3c | Next 30 sessions |
|---|---|---|---|---|---|---|---|
| AMD 8/18 @478.80 | 6.5% | −9.7% | 494.36 | 0.34 | BLOCK | no | best +31.7%, worst −8.0% |
| ARM 8/18 @250.00 | 8.8% | −13.2% | 266.75 | 0.51 | BLOCK | no | best +33.3%, worst −9.8% |
| BE 8/18 @207.70 | 12.2% | −18.2% | 213.24 | 0.15 | BLOCK (also > 15%) | no | best +40.2%, worst −10.5% |
| INTC 8/18 @95.82 | 7.3% | −10.9% | 97.15 | 0.13 | BLOCK | no | best +32.9%, worst −11.1% |
| BE 9/24 @256.29 | 7.0% | −10.6% | 283.83 | 1.02 | BLOCK | no | best +15.4%, worst −26.3% |
| BE 9/28 @261.66 | 7.3% | −11.0% | 283.83 | 0.77 | BLOCK | no | best +13.0%, worst −27.8% |
| ARM 9/28 @284.38 | 6.7% | −10.0% | 290.21 | 0.20 | BLOCK | no | best +8.1%, worst −26.8% |

- All four 8/18 builds:
  - were above the 200-DMA;
  - sat 6–19% under the 50-DMA, with RSI ≈ 50 (a pullback in an uptrend);
  - never came near a 1.5-ATR stop;
  - gained 32–40% within 30 sessions.
- **The binding constraint is structural.** A 1.5-ATR stop plus 2:1 needs T1 ≥ 3 ATR above the entry, which is 20–37% at these
  ATRs. Generous T1s (prior highs) fail too.
- **Which rule caught what.** The losers of October (WDC, STX, SNDK, EWY, QUBT, the ARM re-buy) broke the *behaviour* rules:
  - no desk note;
  - same-session re-buys;
  - lowered stops;
  - caps.

  Those rules cost nothing on the winners. The R/R gate blocked winners and losers alike.
- **Desk conclusion:** the client's suspicion is right about one gate. "R/R ≥ 2:1 to the nearest resistance with a ≥ 1.5-ATR
  stop" filters out the whole high-volatility AI universe. The behaviour rules, the stop and the breaker are the parts that
  earned their keep.
- **Proposed next step:** test a "pullback in an uptrend" entry with the two-regime harness used for §3c. Above a rising
  200-DMA, below the 50-DMA, RSI 40–55, 1.5-ATR stop ≤ 15%, risk ≤ 2%. Decide in writing.

## Pullback test, and the client's "completely new plan" (10/29)
Script: scratchpad `pullback_test.py`. Same universes. 4 slots × $200 is the realistic case.

| Rule | A: AI winners 10/24–10/26 | B: 2021 bust 2/21–2/23 |
|---|---|---|
| Pullback ≥ 5% under the 50-DMA, above a rising 200-DMA | +$61 to +$445 | −$172 to −$344 |
| **§3c dip rule** (−25% / +25% / 30 sessions) | **+$853 · 61% wins · worst run −$317** | **−$235** |
| No trend filter, ≥ 5% under the 50-DMA (the instinct) | +$531 to +$813 | −$792 to −$1,180 |
| VOO with the same $800 | +$262 (+32.7%) | +$64 (+8.0%) |

- **The desk's pullback proposal failed.** The 8/18 pattern does not generalise.
- The §3c dip rule is the best entry tested: ≈ 3× VOO in the winners' market, −$235 in the bust.
- The client wants every rule dropped and a new plan around 35% VOO, the October lessons and dip-buying.
- **Drafted as `PLAN-v6-draft.md`.** It keeps the behaviour rules (each priced from October) and the dip rule, and drops the v3
  gate, zones, ratchet and breaker. Awaiting the client's go before it replaces PLAN.md.
