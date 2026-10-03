# amana — stock desk

Working folder for the Amana stock sleeve. The Claude skill lives in `.claude/skills/stock-desk/`
and is invoked with `/stock-desk` (or automatically when a request is about a stock or the portfolio).

```
.claude/skills/stock-desk/   research/review skill: SKILL.md + references/ + scripts/
.claude/skills/market-move/  shock playbook: /market-move on a big up/down day → decision card
PLAN.md                      the living investment plan (tiers, profit ratchet, reserve ladder)
portfolio/holdings.csv       open positions: ticker,shares,avg_cost,theme,opened,notes
portfolio/transactions.csv   every fill: date,ticker,side,shares,price,fees,note
portfolio/cash.txt           free cash in the account
portfolio/levels.csv         per-name stop, ladder stage done, catalyst, rating (edit freely)
portfolio/peak.txt           sleeve high-water mark for the circuit breaker
research/                    per-ticker deep dives, TICKER-YYYY-MM-DD.md
journal/                     dated reviews, trade logs, lessons
```

`theme` in holdings.csv uses the layer names from `references/ai-race-map.md`
(e.g. `Compute`, `Power generation`, `Foundry`, `Platforms`) or `Non-AI` for anything else.

Quick report (prices are passed in because there is no live feed):

```
python3 .claude/skills/stock-desk/scripts/portfolio_report.py --prices BE=xx.xx INTC=xx.xx
```

Shock day:

```
/market-move            # or just: "market is down 4%, what do I do"
python3 .claude/skills/market-move/scripts/shock_playbook.py --prices ... --day-move -4 --spx-now .. --spx-high .. --vix ..
```
