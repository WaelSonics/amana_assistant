# Risk rules

**Account model: cash account (since 2026-08-12).** No margin, no shorts, no leverage — never
recommend them, they are not available and the client does not want them. Cash on the side is
fully deployable regardless of open P&L, so the cash reserve is a real dip-buying option, not a
margin buffer. Size it as such.

All limits are % of the **stock sleeve** (total money in the stock account, cash included), so
they hold regardless of the sleeve's dollar size. The script `scripts/portfolio_report.py` checks
the mechanical ones; the judgment ones are on you.

## Position sizing
- **Single-name cap: 30%** of sleeve at cost, 35% at market (let winners run a little, then trim).
- **Full position = 20–25%**, half = 10–12%, starter = 5%. Enter in halves: half at the level,
  half on confirmation (break of resistance or successful retest) — never all at once into strength.
- **Theme cap: 60%** in any one theme (e.g. "AI power" or "AI compute"), 80% in the AI race
  overall. The remaining 20%+ is cash or an uncorrelated holding.
- **Minimum 10% cash for discretionary buys** (v2, 2026-10-01; was 15%). The index-dip ladder may go to 5%. In a cash account this
  reserve stays usable no matter how open positions move, so it *is* the option to buy the crash.
  Deploy at most half of it on any single dip; keep the rest for a second leg down.
- **Max 7 lines** (VOO + 6 satellites, one of which may be the speculative slot: ≤ 6% at cost, stop ≤ 12% under entry).
- **Fills: ≤ 8 a month.** Over 8 → no new buys for the rest of the month; sells are always allowed.

## Entry discipline
- No new buy with RSI(14) > 70 or price > 20% above its 50-DMA. Put it on WATCH with the level.
- No new buy or add within 5 trading days of earnings unless the position is a starter (≤5%).
- Reward/risk ≥ 2:1 on the first target, or skip.
- No averaging down into a position whose *fundamental* thesis is impaired. Adding on a
  purely technical pullback with intact thesis is allowed twice per holding period (each ≤ 4% of the sleeve, inside a
  dip zone above the stop, never past the 15% cap); the count resets after a sale that banks a profit.

## Exit and profit-taking
- **Hard invalidation** at the set level: exit, no debate. Re-entry is always possible later.
- **Portfolio-level circuit breaker**: if the sleeve draws down **10% from its peak**, cut every
  position to half and stop new buys until a journal review explains what happened.
- **Profit ladder** (default, override per name): **trim ⅓ when a position is up 40%+ and
  RSI > 70**, trim another ⅓ if it later exceeds the single-name cap, let the rest run with a
  trailing stop at the 50-DMA (weekly close). Kept deliberately simple for a small account.
- Time stop: a thesis that has not started working in 2 earnings cycles is reviewed for exit.

## Monthly contribution
- Default: contribution goes to cash. Deploy when a WATCH level is hit or a review says ADD.
  Small contributions ≠ obligation to buy every month.
- Prefer adding to an existing winner within caps over opening a 6th name.

## Behavioral guards (from the client's own history)
- The pre-2026-08-12 period was experimentation. Do not let anchoring to those prices drive today's
  decisions ("I was up X before" is not a level).
- Locking in gains during volatility is the client's stated preference. Respect it: propose trims
  into strength with a re-entry plan rather than arguing for max exposure.
- Any recommendation to hold through earnings must state the expected move (implied or historical)
  and confirm the client accepts a gap of that size.
