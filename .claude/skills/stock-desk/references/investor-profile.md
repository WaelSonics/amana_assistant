# Investor profile — Wael

Last updated: 2026-10-01. Update this file when any number below changes.

## Capital structure
- Core savings: **cash and physical gold** (the safety base — not part of the stock sleeve).
- Stock sleeve contributions: **≈ $200 / month** (confirmed from statement: $200 deposits on
  2026-07-01 and 2026-09-01; earlier months ranged $100–$450). The sleeve is ~13% of total
  monthly savings; the other ~87% goes to cash and gold.
- Sleeve size (statement 2026-09-29): **equity $3,666.25**; net contributed $3,200.15 since
  2025-11-02; lifetime realized +$208.94 (pre-reset) + post-reset fills; fees so far $84 (clearing
  $1/trade + CFD overnight). Statement archive: `portfolio/statements/`.
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
- **The AI race** — infrastructure and enablers (see `ai-race-map.md`). Current sleeve (2026-09-29): ARM, BE, EWY, WDC (storage),
  TTWO (non-AI, GTA VI), QUBT (off-plan, desk says sell), VOO (core anchor), 8.7% cash. AMD fully sold 2026-09-21, INTC 2026-09-08.

## History that matters
- Account start → **2026-08-12**: experimentation, no clear strategy. Treat pre-Aug-12 trades as
  noise for performance evaluation, but useful for behavioral lessons.
- **2026-08-12**: portfolio cleanup; intentional AI-race positioning begins. Performance
  measurement starts here.
- **2026-09-08**: sold all INTC (+10.2%, +$40.88) and half of BE (+35.4%, +$70.79) to lock in gains, citing
  recent volatility and frequent sharp drawdowns. Interpretation: client values realized gains and
  a positive running return; recommendations should respect that (trim into strength, re-enter on
  defined pullbacks) rather than push maximum exposure.

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
