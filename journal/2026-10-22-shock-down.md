# Shock (down) — Thursday 2026-10-22 close, reviewed 17:30 ET · CIRCUIT BREAKER FIRED

Client: "MU just hit the SL. The market is closed. I am below the circuit breaker. Fuck this shit we lost all the profits
we did in the last two months. The market is in crash massive crash now btw."

## The move (Yahoo daily bars, 10/22 close)
| | Close | Day |
|---|---|---|
| S&P 500 | 7,663.43 | −1.21% · **−2.0% from the 7,818.93 record** |
| Nasdaq-100 | 28,958.69 | −2.90% |
| Dow | 52,867.98 | +0.02% |
| SOX | 10,731.98 | **−6.72%** (chips' worst day since 6/23) |
| VIX | 19.03 | +14% |
| 10-year | 4.95% | −20 bp (flight to Treasuries) |
| Brent | ≈ $113 | +4% (Houthi attacks on Saudi energy infrastructure) |

**This is not a market crash.** The S&P is 2% off its record and the Dow was flat. It was a **chip and AI crash**: AMD −8.1%,
LITE −11.5%, CRWV −10%, SNDK −8.5%, META −7.0%, MU −6.3%. The account was 30%+ in AI chips.

**Cause** (two independent sources):
- **AI capex and financing.** Meta reported negative free cash flow on ≈ $35B of quarterly capex, ≈ $356B of off-balance-sheet
  leases and a proposed non-voting share class to raise capital. Jones Trading: "the most widespread selling of the AI trade
  we have seen all year."
- **Chip equipment.** Lam Research's CFO said guidance "would have been a bit higher if not for some near-term supply chain
  constraints", and those constraints run into 2027. LRCX fell 11.75% on record revenue; AMD and Marvell ≈ −8%, Intel ≈ −7%.
- **Backdrop:** oil (Brent ≈ $113), rate-hike risk at the FOMC on 10/28, and CoreWeave's debt (10/16).

After the close, **WDC** beat and guided above (Q2 revenue $5.0–5.2B vs $4.57B consensus), first +4%, then reported ≈ −8%
after hours on input costs and capex; the reaction is unconfirmed. **BE** beat and raised; ≈ −3 to −5% after hours.
No ARM ruling found.

## Fills
- **MU: the broker stop at $850 fired at ≈ 15:40–15:45 ET** (5-min lows 850.60 / 849.25; closed 856.49). The fill is
  estimated at **$850.00 → ≈ −$16.45 + $1 fee**. Confirm on the next statement. The plan's one memory name is gone.

## Account (10/22 close)
| | Close | Day | vs cost | Value | Stop | Above stop |
|---|---|---|---|---|---|---|
| VOO | 702.30 | −1.2% | −0.5% | $1,193.82 | — | — |
| AMD | 507.93 | −8.1% | −7.1% | $464.64 | 498 | **2.0%** |
| TTWO | 207.81 | +0.8% | −2.5% | $488.70 | 190 | 9.4% |
| Cash | | | | $1,239.72 (est.) | | |
| **Total** | | | | **$3,386.88** | | |

- **−10.4% from the $3,779.85 peak, $14.98 under the $3,402 breaker. The circuit breaker fired (PLAN §7).**
- Against money put in: **+$83.62 (+2.5%)** on $3,303.26. At the peak it was +$476.59, so 82% of the gain is gone.
  The capital is intact.
- §10 test 2 (beat VOO from the 10/16 close): VOO-equivalent $3,421.28. The account is $34 behind.

## Engine (`shock_playbook.py`)
- **Class:** NOISE for the index (−1.2%, −2.0% from the high, VIX 19).
- **Mechanical action: CIRCUIT BREAKER.** Halve every satellite, pause buys, write the post-mortem.
- The reserve tranche is suspended.
- AMD's stop is CLOSE (2.0%).

## Macro or mine?
**Mine.** The cause (whether AI capex is financeable and earns a return) is the question under AMD, ARM and MU. All three
fell together on 10/14, 10/16 and 10/22, and two of them are now gone on their stops. It is not yet a thesis break: Meta is
still spending $35B a quarter, and nobody cut capex. The fear is about funding and returns, not orders. TTWO was the
diversifier and it worked: +0.8% on the day.

## Decision card
1. **Friday 10/23, the circuit breaker: sell half of each satellite at market**, between 10:00 and 10:30 ET (17:00–17:30
   Amana time), after the opening 30 minutes.
   - **AMD 0.4574 sh** (≈ $232 at the close)
   - **TTWO 1.1758 sh** (≈ $244)

   If AMD opens under $498, its stop sells the whole line. Then only the TTWO half is left to sell.
2. **Keep VOO.** Keep the stops on the remaining halves: AMD $498, TTWO $190. Stops never move down.
3. **No buys.** Not the VOO rung, not "cheap" chips, not MU or ARM back. All buys are paused until the post-mortem is agreed,
   and not before 11/2 in any case.
4. **This weekend: the post-mortem decision** (below). It includes the v4 question.
5. After the halving, satellites are ≈ $477 (14%), open stop-risk is ≈ $25, and cash is ≈ $1,714 (≈ 51%).

## Do NOT
- Sell everything at Friday's open. The breaker says *half* of the satellites, and **never VOO**.
- Skip the halving because "it will bounce". The rule is written for exactly this moment.
- Buy back MU or ARM, or any chip "on sale". Two stops fired this week; the plan treats that as information.
- Lower the AMD stop to avoid a fill.

## Post-mortem (PLAN §7) — peak $3,779.85 (10/2) → $3,386.88 (10/22): −$392.97
| Source | $ | Share |
|---|---|---|
| **Overrides** (ledger, marked against the plan's alternative) | **−$258.32** | **66%** |
| Everything else (the market, desk-approved trades, fees) | ≈ −$135 | 34% |

Overrides in the ledger:
- WDC re-buy 10/2 −$44.85
- STX 10/6 −$11.81
- EWY add and lowered stop −$37.34
- BE buy-back −$7.59
- WDC locked add −$8.00
- QUBT lowered stop −$25.28
- SNDK 10/12 −$23.90
- ARM re-buy 10/12 −$55.87
- AMD 10/15 $500 fill −$35.32 (open)
- fees −$9
- TTWO add +$0.65

**What went wrong, in order of cost:**
1. **Trades without the desk: two-thirds of the loss.** The pattern is the same each time: re-buying the session a stop fired,
   oversized fills (AMD $500 = 14.6% in one fill; ARM $400 = 11%), and lowered stops. None has happened since 10/19.
2. **One trade in five tickers.** AMD, ARM, MU (plus WDC, STX, SNDK and EWY before them) are all "AI capex keeps rising". On 10/14,
   10/16 and 10/22 they fell 5–8% together. The plan caps a name at 15% but has **no theme cap**, so 30–45% of the account
   rode one question.
3. **Entries next to their stops.** ARM's re-buy left the stop 0.6 ATR away. MU was bought at R/R 1.4 (a desk error: no
   ceiling in the trigger). Both stops fired on ordinary intraday dips, ARM at the open and MU at 15:40 ET, and both closed
   above the stop.
4. **Desk errors**, logged: the MU trigger without a ceiling (10/15), two buys in one day (10/15), and the AMD zone 4 points too
   wide (10/14).

**Proposed rule changes (client decides):**
- **(a) Theme cap:** AI semis and memory (AMD, ARM, MU, NVDA, AVGO, SNDK, WDC, STX, LITE, AXTI, AAOI, ANET, INTC) **≤ 25% of the
  sleeve** combined, and at most 2 such names at once.
- **(b) Stop distance at entry ≥ 1.5 ATR, or no buy.** The research protocol already says this. It becomes a hard check.
- **(c) The v4 question.** On 10/18 the desk recommended v4 (VOO 80%, a 20% trading pot) and the client chose v3 to 12/31.
  The breaker firing is the event v4 was built for. **Desk recommendation: switch to v4 now**, using the halving's cash
  plus the existing cash to move toward VOO on the plan's schedule. The client decides. If v3 continues, the §10 test
  stands as written: a breaker fire does not fail test 1.

## Client's instinct
"We lost all the profits": the account is still **+$84** on money put in, but 82% of the peak gain is gone. "Massive crash":
the S&P is −2.0% from its record. The crash is in the one theme the account was concentrated in. That is lesson 2, and it
is fixable.

## Client proposal (10/23, before the halving): remove the AMD stop, hold it as a "long-term investment"
Client: "What about removing the SL and holding AMD, so we segregate the account further: SL/TP for trading, long
investments with no SL. Is it good practice according to history?"

**Desk: no. Keep the $498 stop and halve AMD tomorrow as written.**

1. **Plan.** Removing a stop is lowering it to zero, which makes it an OVERRIDE. It fails §10 test 1 ("no stop is lowered"),
   which moves the account to v4 from 1/4. It does not cancel the breaker either: half of AMD is sold on 10/23 whatever the
   stop.
2. **Motive and timing.** The proposal arrived with AMD −7% from cost and 2% above its stop. It would turn a losing trade
   into an "investment" to avoid the loss (the disposition effect). Together with the recorded habit of selling winners early
   (AMD at +27% on 9/21, ARM at the first rung), the result is: cut winners, keep losers. Lowered stops cost $56 in October
   (QUBT, EWY); SNDK was held without a stop.
3. **History** (Yahoo monthly closes, fetched 10/23):
   - **AMD:** 2000-03 $40.88 → 2015-06 $1.81, **−96%, back above the peak in 2019-12**, almost 20 years later. Drawdowns of
     48% or more six times since 1984, two of them in the last five years: −51% (2021–22) and −48% (2023–24).
   - **CSCO:** −86% from 2000, back in 2026-01, 26 years later. **INTC:** −83% from 2000, back in 2026-03, 26 years later.
   - **SOX:** −83% from 2000, back in 2017-10. **S&P 500:** −45% (2000–02) and −52% (2007–09), each back in 6–7 years.
   - **Bessembinder (2018, JFE):** ≈ 57% of US stocks since 1926 returned less than one-month T-bills over their lifetime;
     ≈ 4% of firms account for all of the market's net wealth creation. A single stock held without a stop is a bet that
     you picked one of the 4%.
4. **What is right in the idea.** Splitting the account into a trading part and a hold-forever part is sound, and the
   hold-forever part already exists: **VOO** (Tier 1, never sold, no stop). An index has no single-company failure mode. v4
   is this idea taken seriously (VOO 80%).

**If the client still wants a long-term single-stock bucket, it needs rules decided in advance:**
- fresh buys only, never a conversion of an open trade;
- ≤ 5% of the sleeve per name and ≤ 10% in total;
- exits written as thesis events and reviewed each report;
- no name enters it within 30 days of leaving the trading bucket;
- every buy decided with the desk on a weekend.

Client decision: pending.
