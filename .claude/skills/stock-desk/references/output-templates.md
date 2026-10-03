# Output templates

## Ticker deep dive → `research/TICKER-YYYY-MM-DD.md`

```markdown
# TICKER — Company name — deep dive YYYY-MM-DD

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
