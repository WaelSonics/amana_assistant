# Earnings preview and thesis scorecard

Adapted from Anthropic's `equity-research` plugin (github.com/anthropics/financial-services, Apache-2.0: skills
`earnings-preview` and `thesis-tracker`), cut down to this account's rules. The desk evaluated the full plugin on
2026-10-27 and did not install it: it duplicates this skill and ships paid-data connectors (`journal/2026-10-27-tools-review.md`).

## A. Earnings preview — for every holding, written before the pre-report decision day
Run `levels.py TICKER` first: it gives the report date and time, the sessions left, and the blackout flag.

1. **Date and time.** Taken from `levels.py`, which reads the Alpha Vantage calendar. Before the open or after the close
   sets which session's close is the last decision point.
2. **Consensus.** Revenue, EPS and the 1–2 sector metrics that move the stock (data-center revenue, bookings, combined
   ratio…). Each figure carries its source and date.
3. **Implied move.** From the options straddle (web search "TICKER implied move earnings"), compared with:
   - **the distance to the stop:** if the implied move exceeds it, a gap can skip the stop;
   - **the position's size:** implied move × position value is the $ at stake.
4. **Scenarios:**

   | Scenario | What has to happen | Likely reaction | Action written now |
   |---|---|---|---|
   | Bull | | | e.g. sell ⅓ only if it reaches the sell zone |
   | Base | | | hold with the stop |
   | Bear | | | the stop decides; no add for 2 sessions |

5. **History.** The last 4 reactions, close to close and opening gap.
6. **Decision, written the session before the report:**
   - hold through with the stop;
   - trim into the run-up (PLAN §3 catalyst rule); or
   - exit.

   No buys inside the 3-session blackout. Never decide on report night.

## B. Thesis scorecard — one per holding (and per v5 compounder)
Keep it at the top of `research/TICKER.md`. Update it after every report and every thesis-relevant headline.

| Pillar (falsifiable) | What was expected | Status (dated) | Trend |
|---|---|---|---|
| e.g. data-center revenue grows > 30% y/y | ≥ 30% | Q3: +x% (date) | stable / improving / weakening |

- **Thesis-break exits:** 2–3 events that end the position whatever the price. Examples: two guidance cuts in a row, a
  ruling that cuts the core economics, a dividend cut. For v5 compounders these replace the price stop (PLAN §11).
- **Disconfirming evidence** is logged as carefully as confirming evidence.
- **Conviction** is High, Med or Low, with one line on what would change it.
