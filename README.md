# amana — stock desk

Working folder for the Amana stock sleeve. The Claude skill lives in `.claude/skills/stock-desk/`
and is invoked with `/stock-desk` (or automatically when a request is about a stock or the portfolio).

```
.claude/skills/stock-desk/   research/review skill: SKILL.md + references/ + scripts/
.claude/skills/market-move/  shock playbook: /market-move on a big up/down day → decision card
PLAN.md                      the investment plan, v6 (2026-10-29): VOO 35% + dip rule + eight October rules
archive/                     retired plans (v3 with its full history)
portfolio/holdings.csv       open positions: ticker,shares,avg_cost,theme,opened,notes
portfolio/transactions.csv   every fill: date,ticker,side,shares,price,fees,note (dip trades tagged DIP)
portfolio/cash.txt           free cash in the account
portfolio/levels.csv         per line: kind (core/legacy/dip), stop, tp, opened, exit_by, theme
portfolio/peak.txt           high-water mark for the account brake (−15%)
research/                    one file per ticker, TICKER.md (dated entries and dip studies, newest first)
journal/                     dated reviews, trade logs, lessons
```

Daily scan and weekly report (Yahoo prices; the earnings calendar from Alpha Vantage, key in
`~/.config/amana-desk/alphavantage.key`):

```
python3 .claude/skills/stock-desk/scripts/levels.py MU AMD BE ...   # technicals + the "Dip rule (v6)" line
python3 .claude/skills/stock-desk/scripts/levels.py --report        # v6 checks: SL/TP, slots, cash floor, themes, brakes
```

Shock day: `/market-move` (or just "market is down 4%, what do I do"). Its v3 engine `shock_playbook.py` is retired.
