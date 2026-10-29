# Tools review — Claude MCP servers, plugins and skills for market data and charts (2026-10-27)

Client: "Search for Claude MCPs or skills related to the stock market and graph study that we can benefit from in this
repo. I saw many Instagram reels hinting that new Claude features help."

## What is installed now
- **MCP:** about 20 claude.ai connectors, all for work tools. The only finance one is CB Insights (private companies,
  needs auth). The repo has no `.mcp.json`.
- **Plugins:** none installed. The Anthropic directory is configured and lists about 150 finance-related plugins.
- **Python:** no matplotlib or pandas. Charts would be SVG/HTML or need a venv.

## What is real (official docs; Claude Code guide agent)
- **MCP servers:** `claude mcp add --transport http|stdio …`, with scopes local, project (`.mcp.json`) or user.
  Put keys in env vars as `${VAR}`, never literally in a committed file.
  Source: https://code.claude.com/docs/en/mcp.md
- **Anthropic finance plugins (official, Apache-2.0):** github.com/anthropics/financial-services
  - Plugins: `financial-analysis` (DCF, comps), `equity-research`, `earnings-reviewer`, `market-researcher`.
  - Install: `claude plugin marketplace add anthropics/financial-services`, then
    `claude plugin install earnings-reviewer@claude-for-financial-services`.
  - The skills are free. Their data connectors (FactSet, S&P, Morningstar…) need paid vendor licences.
- **Claude for Financial Services connectors:** an Enterprise offering with institutional data licences. Not viable here.
- **Reading chart images:** works for qualitative reads (trend, zones, patterns), not for exact prices or RSI. Computed
  numbers stay the source of truth.
- **Desktop scheduled tasks** run locally on this machine, so a daily check is possible without GitHub.
  Source: https://code.claude.com/docs/en/scheduled-tasks.md

## Market-data MCP servers (sonnet sweep; free-tier figures partly unverified)
| Server | Publisher | Free tier | Fit |
|---|---|---|---|
| **Alpha Vantage** (remote OAuth `mcp.alphavantage.co/mcp`, or local) | official | 25 requests/day | Earnings calendar and history, news sentiment, macro, fundamentals. Too few calls for bulk prices |
| **EODHD v2** (OAuth) | official | ≈ 20 calls/day (unverified) | 72 read-only tools; cheap paid plans |
| **Massive (ex-Polygon)** | official | unverified | High-quality bars and options; 3 generic tools |
| **SEC EDGAR** (stefanoamorelli, ≈ 378★) | community | free, no key (needs a User-Agent email) | Filings, financials, **insider trades**. Run as local stdio only |
| **FRED** (stefanoamorelli) | community | free key | Macro series; optional, since VOO/^TNX cover most of it |
| FMP | official MCP unconfirmed | 250 calls/day | Best free fundamentals and estimates, if an official server exists |
| **Alpaca** | official | — | **Can place real trades. Never on this account.** |
| Yahoo (yfinance) community MCPs | community | free | The same fragile source we already curl |
| TradingView cookie MCPs | unknown | — | Hand over your session. Never |

## Desk view
- **Cost.** The sleeve is ≈ $3,400. A $30–50/month data plan is 10–18% of the account a year, so free tiers only.
- **What tools can and cannot fix.** They fix **data quality and speed**: unverified earnings dates, insider data, fragile
  Yahoo calls, levels rewritten by hand. They do not fix returns. October's −$393 was 66% overrides, and no MCP fixes that.
- **Safety:**
  - read-only servers only;
  - official publishers preferred;
  - community servers as local stdio, version pinned;
  - **no trade-capable integration, ever** (with the override record, an AI trade button is the worst possible tool).

## Evaluation (same day): kept, borrowed, dropped
1. **Chart-and-levels script: KEPT.** It is `.claude/skills/stock-desk/scripts/levels.py` (standard library only).
   - Technicals, swing levels, the chase guard and the trend verdict.
   - A setup checker (R/R at the zone low, mid and high; stop ≥ 1.5 ATR; risk ≤ 2%).
   - A PNG/SVG chart via headless Chrome.
   - `--report` for every holding.
   - **First run caught a desk error:** the MU zone of 10/24 ($855–870) failed the rules at both edges, so it was tightened
     to $859–863 (alert $863).
2. **SEC EDGAR MCP: DROPPED (client, 2026-10-28: no email).** The Docker image `stefanoamorelli/sec-edgar-mcp` (v1.30.0,
   AGPL, 21 tools including insider summaries and Form 4) works, but **www.sec.gov returns 403 unless the User-Agent has a
   real contact email.** data.sec.gov (company facts) works without one, but filings and insider data do not. The client
   declined to give an email.
   - It was never registered as an MCP server; only the image was pulled. The desk's permission check blocked deleting
     it, so the client removes it: `docker rmi stefanoamorelli/sec-edgar-mcp:latest` (335 MB).
   - Insider trades and filings stay a web-search item in the research protocol, cited by their sec.gov link, as the
     research files already do.
3. **Alpha Vantage: KEPT as a direct call, not as an MCP.**
   - EARNINGS_CALENDAR returns every report date, time and consensus EPS in one call. It matched all the hand-confirmed
     dates and is now built into `levels.py` with the 3-session blackout flag.
   - Not installed as an MCP: ≈ 120 tools in context and an OAuth setup, for one call a day.
   - Needs the client's free key in `~/.config/amana-desk/alphavantage.key`. Until then the public demo key is used,
     which is meant for testing only.
4. **Anthropic finance plugins: DROPPED as an install; two templates borrowed.**
   - Not installed: `equity-research` duplicates stock-desk, and `financial-analysis` ships 10+ paid connectors.
   - Borrowed into `references/earnings-and-thesis.md` (Apache-2.0): the earnings-preview scenario table and the
     thesis-tracker scorecard. The scorecard is the format for v5's written thesis-break exits.
5. **Daily automatic check: DROPPED.**
   - Desktop scheduled tasks need the Claude desktop app (Mac/Windows; this machine runs Linux).
   - The client turned off the automated alert routine on 10/14.
   - `levels.py --report` gives the same status on demand in one command.
