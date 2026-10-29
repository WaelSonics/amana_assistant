# Risk rules — plan v6 (from 2026-10-29)

`PLAN.md` is the source. This file is the checklist the desk runs before every recommendation. `portfolio_report.py`
enforces the numeric ones. Change them there and here together. v3's rules are in `archive/PLAN-v3-2026-10-29.md`.

## Structure
- VOO = 35% of the account, never sold, no stop. The monthly $200 goes to VOO while it is under 35%, else to cash.
- Dip book: at most **5 open dip trades**, **$400 each**. A buy happens only if cash stays **≥ $150** after it.
- Legacy lines (AMD, TTWO): they keep their stops and get a +25% TP; no adds; they do not use dip slots.

## Entry: every buy must pass all of these
- [ ] **A dip signal on a daily close** (`levels.py` "Dip rule (v6)"):
  - ≥ 15% under the 20-session high close;
  - above the 200-DMA;
  - the 200-DMA higher than 20 sessions ago.
- [ ] **A study is written first** (5 lines, `output-templates.md`).
- [ ] **Not in the 3 sessions before the name's earnings, and not an FOMC day.**
- [ ] **≤ 2 open lines in its theme** (PLAN §6; legacy lines count).
- [ ] **$400, a free slot (≤ 5), and cash ≥ $150 after the fill.**
- [ ] **No brake is on** (below).
- [ ] **Not a re-buy in the session the name's stop fired.**
- [ ] **Not a story stock** (no revenue, or a market cap under $5B). No leverage, shorts, options, CFDs, crypto or SPACs.

## Exits
- SL at fill −25% and TP at fill +25%, **set in the app at the fill**. Never a line without both.
- Time exit at the close of the 30th session after the buy.
- Thesis break, as named in the study: sell at the next open.
- **Never lower or remove a stop.**

## Brakes
- Closed dip trades net −$400 → new buys pause until a desk review.
- A close under $3,212.87 (−15% from the $3,779.85 peak) → new buys pause for two weeks. Nothing is force-sold.
- Brakes are never reset or moved.

## Never
Sell VOO for a stock idea · touch the physical vault · lower a stop · buy without the desk.
