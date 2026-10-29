# Investor profile — Wael

Last updated: 2026-10-29 (plan v6). Update this file when any number below changes.

## Capital structure
- **Savings split (client, 2026-10-03): ≈ 70% physical holdings (recorded earlier as physical gold), ≈ 20% cash,
  ≈ 10% the Amana stock sleeve.** The first two are the vault — the safety base, never managed or tapped here.
  A total loss of the sleeve would cost ≈ 10% of savings. Under plan v6 (10/29) a full stop on one $400 dip trade costs
  ≈ $102 (≈ 3% of the sleeve); the client accepted that risk for faster profits.
- Stock sleeve contributions: **≈ $200 / month** (confirmed from statement: $200 deposits on
  2026-07-01 and 2026-09-01; earlier months ranged $100–$450). The October $200 was not on the 10/2 statement;
  a $100 referral bonus landed 10/1.
- Sleeve size (10/29 11:43 ET, statement to 10/26): **$3,426**, cash $1,239.59 (36%). Peak $3,779.85 (10/2); the v6
  account brake is $3,212.87 (−15%). Statement archive: `portfolio/statements/`.
- **Order types (client, 2026-10-07): no limit orders as far as the client knows.** Each position carries one broker
  SL and one TP, and both close the WHOLE line. So partial trims (⅓ ladder, trade-around) and buys at a level are
  done as: price alert at the level → manual market order when it fires. Never write "limit order" in a
  recommendation; give the alert price and the share count. Adds and buy-backs work the same way.
- **Account type: CASH account** (switched at the 2026-08-12 reset; the $3,022 withdrawal on 8/12
  and re-deposit on 8/18 was the migration). Consequences that shape every recommendation:
  - Positions are fully paid. An open loss cannot eat into the cash set aside — unlike the old
    leveraged/CFD account, where $1,000 invested falling to $700 left the account at −$200 and
    froze the spare $100. Cash on the side is now *always* deployable — it is the buy-the-dip reserve.
  - No shorting, no 2× leveraged buying, no CFD financing/overnight fees. This is structurally
    what removed the ARM-short failure mode.
  - Fractional shares still available (statement shows fractional fills post-switch).
- Broker: Amana (Amana Capital) — MT4/MT5 plus the Amana app. No live API access from this
  machine; positions come from the client or exported statements.

## Goals and risk posture
- Primary: **maximize returns while avoiding significant losses and unnecessary risk.**
- Accepts that losses happen; wants **capital preservation and good risk/reward** prioritized over
  chasing. Prefers locking in gains when the tape is volatile.
- Practically: asymmetric setups, defined invalidation, willingness to sit in cash.

## Thematic focus
- **The AI race** — infrastructure and enablers (see `ai-race-map.md`). Current sleeve (2026-10-16): VOO (core 34.7%), AMD, TTWO (GTA VI),
  ARM, MU, ≈ 20% cash. Stopped out 10/12–10/15: STX, BE, QUBT, EWY, WDC, SNDK. Earlier: ARM 10/8, AMD 9/21, INTC 9/8.

## History that matters
- Account start → **2026-08-12**: experimentation, no clear strategy. Treat pre-Aug-12 trades as
  noise for performance evaluation, but useful for behavioral lessons.
- **2026-08-12**: portfolio cleanup; intentional AI-race positioning begins. Performance
  measurement starts here.
- **2026-09-08**: sold all INTC (+10.2%, +$40.88) and half of BE (+35.4%, +$70.79) to lock in gains, citing
  recent volatility and frequent sharp drawdowns. Interpretation: client values realized gains and
  a positive running return; recommendations should respect that (trim into strength, re-enter on
  defined pullbacks) rather than push maximum exposure.
- **2026-09-15**: between weekly checks, re-bought QUBT ($200, a name the §2 rule cited as a lesson) and added TTWO
  above its watch zone against the 9/9 "no add" decision, both without the desk (`journal/2026-09-22-qubt-override.md`).
- **2026-09-21**: sold all of AMD at +27% and ~40% of ARM at +26%, i.e. at the stop-to-breakeven rung, not the ⅓ trim
  rung. Two of two winners closed early, and the broker TPs were set to sell whole lines at the first rung. Pattern:
  **exits winners too early**. Point out when a sale skips the ratchet.
- **GOOGL impulse pattern**: three round trips in June 2026 (avg hold 3 days, +$10.31 on six fills); asked to buy
  "$400 because it seems down" on 2026-09-24 with no level or horizon. Answer dip-feel requests with written
  triggers and R/R (`research/GOOGL.md`, entry 2026-09-24), not a yes/no.
- **2026-10-01 → 10-03**: asked twice in three days to loosen the trading rules (plan v2, then v3), citing the vault.
  Between the two, traded without the desk: WDC re-bought full size the same day its stop fired, TTWO added above
  its zone, Reserve to 5.3% (both logged as OVERRIDES). Pattern to watch: activity rises when cash is lowest.
  The client trades from the Amana app when Claude is unavailable — written levels in `PLAN.md` §6b and broker
  stops are what actually govern those moments, so keep them current.

- **2026-10-06**: three moves from the app without the desk: STX bought (7th satellite, Reserve below floor), BE half sold
  below its zone, and the QUBT stop **lowered** 8 → 7 to dodge an exit the desk had called. On 2026-10-07 the client
  committed to ask the desk before every trade. Hold them to it: any fill without a desk note is an OVERRIDE.
- **2026-10-08 → 10-09** (one day after the commitment): ARM's raised stop fired (+$27, right). Then three buys from the app
  in 24 hours, citing "no internet": EWY, BE, WDC — all at desk-written zone prices, all oversized or locked. The EWY stop was
  **lowered** 172 → 165. Cash went from $585 to $30 (0.8%). Client called it "very smart". The override ledger since 10/2 is
  −$15.43 at 10/9 closes (PLAN §7). Pattern: the client follows the desk's *prices* but not its *sizes, locks or cash floor*,
  and moves stops down to avoid exits. Answer with the ledger, not with opinion.
- **2026-10-12 → 10-13**: STX's stop fired and SNDK (no stop, no research) was bought 17 minutes later. ARM was re-bought
  for $400 below its own stop. Then EWY (lowered stop) and WDC gapped through their stops. Five stop-outs in two sessions.
  The override ledger reached −$154 (−4.1% of the sleeve in 11 days). Client: "I fucked up again." Asked for research on
  every holding and **one research file per ticker** (`research/TICKER.md`). Watch for the next trigger: ≈ 35–40% cash after
  a string of stop-outs is the exact setup where the client has redeployed within hours.
- **2026-10-14 → 10-16**: pushed back hard on the caution ("paranoid", "different this time") and raised the October cap
  10 → 12. Then followed the desk on MU (close trigger, $200 vs $150) but bought AMD **$500 at 11:29 ET**, before a
  close-based trigger that then failed (closed 562 vs ≤ 545). Same pattern as 10/9: the desk's price, not its size or its
  timing. SNDK stopped at 1,300 (the stop held). Override ledger −$197 (−5.2%). The account sits $73 above the circuit
  breaker. Desk lesson: write triggers as bands ("close in $X–Y"), never one-sided.
- **Scored 2026-10-17:** the client's unprompted *protective* acts helped (ARM stop raised to 280 and BE to 260: ≈ +$43.5
  saved; BE half sold at 295.02: +$41.59 banked; SNDK stop 1,300 ≈ even). Every unprompted *buy* lost except a +$0.65 TTWO add
  (−$227 total). Trust their sells and stop raises; route every buy through the desk.
- **2026-10-18**: after the −9.6% slide, asked whether indexing beats trading. Backtests showed v3 followed perfectly still
  trails the S&P (20 yrs: $230–240k vs $251k; v4 $248–254k; 50/50 $151–169k). The desk recommended v4; the client chose
  **v3 to 12/31, then decide** (PLAN §10: zero overrides and beating VOO from 10/16, or v4 on 2027-01-04). Every override
  from 10/19 now counts against v3 itself: name it as such when one is proposed.
- **2026-10-22 → 10-23**: the circuit breaker fired (MU stopped, account $3,386.88). The night before the halving, the client
  proposed removing the AMD stop and calling the position a "long-term investment" (−7%, 2% above its stop). Desk: no. That is a
  stop lowered to zero, an OVERRIDE that fails §10 test 1, and the disposition effect: sell winners early, keep losers. The
  hold-forever bucket is VOO. Watch for: rule-softening proposals arriving at the point of maximum pain.
- **2026-10-29**: pushed again for looser rules ("lower the stop, ride the upswings"; "BE and Intel bought on 10/24 would
  have made money"). This time the desk tested the claim in two regimes, not just refused it. The client adopted a written
  dip rule (PLAN §3c), live from 11/2 against the desk's 11/10. Pattern: rule pressure follows a week when skipped trades
  bounced. Answer with tests and written rules, and keep the line on lowering existing stops.
- **2026-10-29 (later)**: the desk showed that v3's entry gate would have blocked all 7 post-reset winners. The client
  dropped v3 and adopted **plan v6**: VOO 35%, the dip rule as the only entry, 5 slots × $400 (above the desk's 4 × $200),
  SL −25% / TP +25% / 30 sessions, and eight October rules he called "the fruits of learning" (no lowered stops, no
  same-session re-buys, SL+TP always set, signal-only dips, ≤ 2 per theme, size/slot/cash caps, earnings blackout, a study
  first). Hold him to the eight rules. The size is his accepted risk; don't re-argue it.

## How to talk to this client
- **Role (client, 2026-10-07): greedy and logical, and harsh.** Greedy: push to keep winners running and hunt the
  best R/R setups; call out profit left on the table. Logical: every call rests on levels, rules and numbers. Harsh:
  the client says they get excited easily, so when excitement drives a request (FOMO, "it seems down", chasing a spike,
  trading between checks), say so bluntly, name the rule it breaks and its past cost, and refuse to soften it.
  Accepted plan: **v6** (2026-10-29): the dip rule, 5 × $400, the eight October rules (PLAN.md).
- Quantitative, direct, ranked. One clear recommendation per decision.
- Always show (v6): the signal line, the $400 size, SL −25% and TP +25% prices, the 30-session exit date, slots and cash
  after the buy.
- Explain the *why* in a few lines — the client is learning to invest intentionally and wants
  reasoning they can reuse.
- Small account ⇒ few names, fractional shares, low turnover. Never recommend options, leverage,
  or CFDs on this sleeve.
- **Hard lesson on record (pre-reset):** shorting ARM via CFD into its parabolic run cost ≈ $242 —
  the single largest loss, bigger than every speculative loss (crypto, QUBT, SPCX, SLV) combined.
  No shorts, no CFDs, no fighting momentum. Clearing fees ($62 on 62 fills) ate ~30% of realized
  profit — turnover has a real cost at this size.
