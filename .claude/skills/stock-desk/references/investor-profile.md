# Investor profile — Wael

Last updated: 2026-10-03. Update this file when any number below changes.

## Capital structure
- **Savings split (client, 2026-10-03): ≈ 70% physical holdings (recorded earlier as physical gold), ≈ 20% cash,
  ≈ 10% the Amana stock sleeve.** The first two are the vault — the safety base, never managed or tapped here.
  A total loss of the sleeve would cost ≈ 10% of savings; plan v3 caps "every stop hit at once" at 8% of the sleeve
  (≈ 0.8% of savings).
- Stock sleeve contributions: **≈ $200 / month** (confirmed from statement: $200 deposits on
  2026-07-01 and 2026-09-01; earlier months ranged $100–$450). The October $200 was not on the 10/2 statement;
  a $100 referral bonus landed 10/1.
- Sleeve size (statement 2026-10-02): **equity $3,779.85**, cash $199.07 (5.3%); money in $6,345.26, out $3,042
  since 2025-11-02; lifetime realized +$392.65; fees so far $98.19 ($76 clearing at $1/trade + $22.19 CFD overnight).
  Statement archive: `portfolio/statements/`.
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
- **The AI race** — infrastructure and enablers (see `ai-race-map.md`). Current sleeve (2026-10-02): ARM, BE, EWY, WDC (storage),
  TTWO (non-AI, GTA VI), QUBT (speculative slot), VOO (core anchor), 5.3% cash. AMD fully sold 2026-09-21, INTC 2026-09-08.

## History that matters
- Account start → **2026-08-12**: experimentation, no clear strategy. Treat pre-Aug-12 trades as
  noise for performance evaluation, but useful for behavioral lessons.
- **2026-08-12**: portfolio cleanup; intentional AI-race positioning begins. Performance
  measurement starts here.
- **2026-09-08**: sold all INTC (+10.2%, +$40.88) and half of BE (+35.4%, +$70.79) to lock in gains, citing
  recent volatility and frequent sharp drawdowns. Interpretation: client values realized gains and
  a positive running return; recommendations should respect that (trim into strength, re-enter on
  defined pullbacks) rather than push maximum exposure.
- **2026-10-01 → 10-03**: asked twice in three days to loosen the trading rules (plan v2, then v3), citing the vault.
  Between the two, traded without the desk: WDC re-bought full size the same day its stop fired, TTWO added above
  its zone, Reserve to 5.3% (both logged as OVERRIDES). Pattern to watch: activity rises when cash is lowest.
  The client trades from the Amana app when Claude is unavailable — written levels in `PLAN.md` §6b and broker
  stops are what actually govern those moments, so keep them current.

## How to talk to this client
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
