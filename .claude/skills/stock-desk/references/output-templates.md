# Output templates

## Dip study (plan v6) → new entry at the top of `research/TICKER.md`, before every buy (PLAN rule 8)

```markdown
## TICKER — dip study YYYY-MM-DD (plan v6)
1. **What it is:** one line.
2. **Why it fell:** the cause, dated and sourced, and whether it touches the business or only the price.
3. **Next earnings:** YYYY-MM-DD (N sessions; blackout?), with the source.
4. **Sell whatever the price if:** the 1–2 events that break the thesis (guidance withdrawn, a lost key customer, fraud…).
5. **Signal (levels.py, date time):** close −x.x% from the 20-session high close; 200-DMA filter pass.
**Order:** $400 at the next open → SL fill −25%, TP fill +25% in the app · exit by YYYY-MM-DD (30 sessions) ·
slots n/5 and cash $x after it · theme count n/2.
```

## Ticker deep dive → new entry at the top of `research/TICKER.md` (one file per ticker; create it with a `# TICKER — Company — research log` title if it does not exist)

```markdown
## TICKER — Company name — deep dive YYYY-MM-DD

**Verdict:** BUY / ADD / HOLD / TRIM / EXIT / WATCH · **Conviction:** High/Med/Low — one-line why

| | |
|---|---|
| Price (date) | $xx.xx (YYYY-MM-DD close) |
| Entry zone | $xx–$xx |
| Invalidation (stop) | $xx — below <level> / or event: <event> |
| Target 1 / 2 | $xx (technical) / $xx (fundamental) |
| Reward/risk (T1) | x.x : 1 |
| Size | x% of sleeve (starter/half/full) — half now, half on <confirmation> |
| Timeframe | weeks / months / quarters |
| Next earnings | YYYY-MM-DD (N trading days) |

## Thesis
2–5 sentences.

## Chart & technicals
Trend, MAs, levels, RSI, volume, ATR. Sources + dates.

## Fundamentals
Growth, margins, valuation vs range/peers, balance sheet.

## News & catalysts (last 30d / next 90d)
- date — item — confirming/neutral/breaking

## Positioning & sentiment
Short interest, insiders, analysts, crowdedness.

## What would make me wrong
Bullet list — price level and fundamental events.

## Sources
- [title](url) — date
```

## Portfolio review → `journal/YYYY-MM-DD-review.md`

```markdown
# Portfolio review YYYY-MM-DD

## Macro backdrop (dated)
SPX/NDX trend, VIX, 10Y, calendar this week, AI/semis headlines.

## Positions
| Ticker | Layer | Weight | P&L % | Action | Level that changes the call |
|---|---|---|---|---|---|

## Rule check
- breaches / clean (from portfolio_report.py + judgment rules)

## Recommendations (ranked)
1. Action — ticker — size — why (2 lines) — invalidation

## Monthly contribution plan
Where the next $ goes, or "cash until <level>".

## Watchlist
| Ticker | Layer | Trigger level | Why |

## Open questions for the client
```

## Trade log → append to `portfolio/transactions.csv`, then `journal/YYYY-MM-DD-trade-TICKER.md`

```markdown
# Trade — TICKER — BUY/SELL — YYYY-MM-DD
- Qty / price / total
- Why now (thesis + technical trigger)
- Invalidation set at
- What would have made this wrong
- Lesson (if closing a position)
```
