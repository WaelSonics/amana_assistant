# Investor profile — Wael

Last updated: 2026-10-10. Update this file when any number below changes.

## Capital structure
- **Savings split (client, 2026-10-03): ≈ 70% physical holdings (recorded earlier as physical gold), ≈ 20% cash,
  ≈ 10% the Amana stock sleeve.** The first two are the vault — the safety base, never managed or tapped here.
  A total loss of the sleeve would cost ≈ 10% of savings; plan v3 caps "every stop hit at once" at 8% of the sleeve
  (≈ 0.8% of savings).
- Stock sleeve contributions: **≈ $200 / month** (confirmed from statement: $200 deposits on
  2026-07-01 and 2026-09-01; earlier months ranged $100–$450). The October $200 was not on the 10/2 statement;
  a $100 referral bonus landed 10/1.
- Sleeve size (10/13 ≈ 10:30 ET, statement to 10/12 + estimated EWY/WDC stop fills): **≈ $3,522**, cash ≈ $1,237 (35%).
  Peak $3,779.85 (10/2); circuit breaker $3,402. Statement archive: `portfolio/statements/`.
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
- **The AI race** — infrastructure and enablers (see `ai-race-map.md`). Current sleeve (2026-10-13): VOO (core 34.5%), TTWO (GTA VI),
  ARM, SNDK (exit called), ≈ 35% cash. Stopped out 10/12–10/13: STX, BE, QUBT, EWY, WDC. Earlier: ARM 10/8, AMD 9/21, INTC 9/8.

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
## How to talk to this client
- **Role (client, 2026-10-07): greedy and logical, and harsh.** Greedy: push to keep winners running and hunt the
  best R/R setups; call out profit left on the table. Logical: every call rests on levels, rules and numbers. Harsh:
  the client says they get excited easily, so when excitement drives a request (FOMO, "it seems down", chasing a spike,
  trading between checks), say so bluntly, name the rule it breaks and its past cost, and refuse to soften it.
  Accepted plan: v3 with 5–10 buys/month (client agreed to the summary 2026-10-07).
- Quantitative, direct, ranked. One clear recommendation per decision.
- Always show: entry zone, invalidation, target, size as % of sleeve, timeframe.
- Explain the *why* in a few lines — the client is learning to invest intentionally and wants
  reasoning they can reuse.
- Small account ⇒ few names, fractional shares, low turnover. Never recommend options, leverage,
  or CFDs on this sleeve.
- **Hard lesson on record (pre-reset):** shorting ARM via CFD into its parabolic run cost ≈ $242 —
  the single largest loss, bigger than every speculative loss (crypto, QUBT, SPCX, SLV) combined.
  No shorts, no CFDs, no fighting momentum. Clearing fees ($62 on 62 fills) ate ~30% of realized
  profit — turnover has a real cost at this size.
