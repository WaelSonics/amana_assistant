# Risk rules

**Account model: cash account (since 2026-08-12).** No margin, no shorts, no leverage — never
recommend them, they are not available and the client does not want them. Cash on the side is
fully deployable regardless of open P&L, so the cash reserve is a real dip-buying option, not a
margin buffer. Size it as such.

All limits are % of the **stock sleeve** (total money in the stock account, cash included), so
they hold regardless of the sleeve's dollar size. The script `scripts/portfolio_report.py` checks
the mechanical ones; the judgment ones are on you.

## Position sizing (PLAN.md is the authority; v3 2026-10-03)
- **Single-name cap**: no add may take a satellite past **15%** of the sleeve; above **20%** at market, trim back to 15%.
  VOO (core) has its own 30–35% band instead.
- **Full position = 10–15%**, half = 5–8%, starter ≤ 5%. Up to 8% of the sleeve may go in one fill; above 8%, enter
  in halves: half at the level, half on confirmation (break of resistance or successful retest) — never all at once
  into strength.
- **Risk per buy ≤ 2% of the sleeve** (shares × distance to the stop). **Open stop-risk ≤ 8%**: every satellite stop
  hit on the same day must cost less than 8% of the sleeve, which keeps it under the 10% circuit breaker. Above 8% →
  no buys until a trim or a stop raise. `portfolio_report.py` computes both from `portfolio/levels.csv`.
- **Minimum buy $50** — the $1 clearing fee must stay ≤ 2% of the fill.
- **Theme cap: 60%** in any one theme (e.g. "AI power" or "AI compute"), 80% in the AI race
  overall. The remaining 20%+ is cash or an uncorrelated holding.
- **Minimum 7.5% cash after any discretionary buy** (v3, 2026-10-03; v2 10%, v1 15%). Contributions refill it toward
  10%; the index-dip ladder may go to 5%. In a cash account this
  reserve stays usable no matter how open positions move, so it *is* the option to buy the crash.
  Deploy at most half of it on any single dip; keep the rest for a second leg down.
- **Max 7 lines** (VOO + 6 satellites, one of which may be the speculative slot: ≤ 6% at cost, stop ≤ 12% under entry).
- **Buys: 5–10 a month** (client, 2026-10-07): 5 is the normal pace, 10 the hard cap. Past the 5th buy, say
  "buy #N of the month, above the normal 5" in the recommendation. It is a ceiling, not a quota. Sells never count and are always allowed.

## Entry discipline
- No new buy with RSI(14) > 70 or price > 20% above its 50-DMA. Put it on WATCH with the level.
- No new buy or add in the 3 trading sessions before earnings (v3), nor on FOMC day or a data morning.
- Reward/risk ≥ 2:1 on the first target (the bottom of the name's sell zone), or skip.
- No averaging down into a position whose *fundamental* thesis is impaired. Adding on a
  purely technical pullback with intact thesis is allowed twice per holding period (each ≤ 4% of the sleeve, inside a
  buy zone above the stop, never past the 15% cap); the count resets after a sale that banks a profit.
- A headline that questions the thesis locks adds on that name until the next hard data point (its own or a close
  peer's earnings) answers it.

## Exit and profit-taking
- **Hard invalidation** at the set level: exit, no debate. Re-entry (PLAN §4a): never the same session the stop
  fired; after that only with evidence the fall ended (higher low or a close back above the broken level), a new stop
  written first, and R/R ≥ 2:1.
- **Portfolio-level circuit breaker**: if the sleeve draws down **10% from its peak**, cut every
  position to half and stop new buys until a journal review explains what happened.
- **Profit ratchet** (PLAN §3, the minimum selling): +25% → stop to breakeven; +40% → sell ⅓; +75% → sell another ⅓;
  the rest trails on a weekly close below the 50-DMA. Trim into a known catalyst's run-up, not after.
- **Broker take-profits sell 100% of the line**, not ⅓. A TP parked at the +40% rung silently replaces the ratchet
  with a full exit. When the stop is already at breakeven, raising the TP costs nothing: put it at or above the +75%
  rung and do the ⅓ trims by hand: a price alert at the level, then a market sell of the ⅓ when it fires. Always say in a review which rung each broker TP actually hits.
- **Trade-around (v3, PLAN §3b)**: every satellite has a sell zone (first target / resistance, above avg cost) and a
  buy zone (support above the stop, R/R ≥ 2:1 to the sell zone). Up to ⅓ of the line may be sold in the sell zone and
  bought back in the buy zone, repeatedly. Optional, never forced; the other ⅔ follow the ratchet. Tag fills `TA`.
- Banked profit refills the Reserve to 15% first, then splits 50/50 Reserve/VOO.
- Time stop: a thesis that has not started working in 2 earnings cycles is reviewed for exit.

## Monthly contribution
- Default (PLAN §5): $200 → VOO while Core < 35% and the Reserve is ≥ 10%; otherwise → Reserve.
  Small contributions ≠ obligation to buy a satellite every month.
- Prefer adding to an existing winner within caps over opening a 7th line.

## Behavioral guards (from the client's own history)
- The pre-2026-08-12 period was experimentation. Do not let anchoring to those prices drive today's
  decisions ("I was up X before" is not a level).
- Locking in gains during volatility is the client's stated preference. Respect it: propose trims
  into strength with a re-entry plan rather than arguing for max exposure.
- Any recommendation to hold through earnings must state the expected move (implied or historical)
  and confirm the client accepts a gap of that size.
