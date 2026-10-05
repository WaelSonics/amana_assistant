---
name: market-move
description: Emergency desk for a sharp market move — up or down. When Wael says the market crashed / sold off / ripped / is up or down big, VIX spiked, "what do I do now", or a holding gapped on news, fetch live index, VIX and cause, run the PLAN.md rules mechanically against every holding and the cash reserve, and return one decision card — exact actions, exact do-nots, and a challenge if his instinct breaks the plan.
---

# Market Move — shock playbook

One job: turn a scary (or euphoric) tape into a short list of pre-agreed actions, fast, without
improvising. The rules live in `PLAN.md`; this skill applies them. Read `PLAN.md` §3–§7 and
`../stock-desk/references/investor-profile.md` first. The stock-desk non-negotiables apply
(fresh dated numbers only; capital preservation first; client decides; challenge once; log it).

## Workflow — target: decision card in one pass

### 1. Measure the move (live, dated) — subagent `sonnet`, one sweep
- S&P 500 and Nasdaq-100: today's % move, current level, most recent closing high (for drawdown).
- VIX level and change. 10Y yield change. Dollar/gold if the move is macro.
- **Cause**, in one line, from ≥2 sources: macro (rates/FOMC/CPI/jobs), geopolitical, credit event,
  AI/semis-specific (capex cut, export rule, hyperscaler guidance), or a single-name event.
- Current price for **every ticker in `portfolio/holdings.csv`**, plus 50-DMA if quickly available.
- For any holding moving >2× the index: the headline behind it.
State the timestamp of every number.

### 2. Run the engine
```
python3 .claude/skills/market-move/scripts/shock_playbook.py \
  --prices AMD=.. ARM=.. BE=.. EWY=.. TTWO=.. VOO=.. \
  --day-move -3.2 --spx-now 6100 --spx-high 6600 --vix 31 [--dma50 AMD=..]
```
It classifies the shock, checks every holding against stop / ladder / cap, computes the reserve
tranche PLAN §5 allows, checks the §7 circuit breaker, and prints the do-not list. Its output is
the skeleton of the answer — do not contradict it without saying which rule you are overriding
and why.

### 3. Judgment layer (Fable) — the only part that is not mechanical
Answer three questions, each in ≤2 sentences, with the data:
1. **Is this macro or is it mine?** A broad, rates- or headline-driven drop with theses intact is a
   *dip* → reserve rules. A drop caused by something inside a holding's thesis (AI capex cut,
   export ban on its product, guidance cut) is a *thesis event* → treat that name under §4, not §5,
   even if the tranche is unlocked.
2. **Where does the unlocked reserve go, in order?** VOO first (§5). Then the satellite with the best
   `rating` in `portfolio/levels.csv` that is at/near its 50-DMA with thesis intact. Give the exact
   dollar amount per name and a limit price, never "buy some".
3. **On an up-shock: what does the ladder let us bank?** List trims the engine fired, then the optional
   trade-around sells it lists under "adjust" (names in their sell zone, ≤ ⅓). If nothing fired, the answer is
   "hold; do not add", and say so.

### 4. Deliver the decision card (template in `references/decision-card.md`)
Verdict line → mechanical actions with sizes and limits → reserve decision → do-nots → what would
change the call in the next 48h → the one lesson if the client's stated instinct differed.

### 5. Challenge and log
If the client's message contains an instinct ("should I sell everything", "let's go all in", "buy
more TTWO it's cheap now"), test it against the plan **first** and lead with the challenge if it
fails. Then write `journal/YYYY-MM-DD-shock-<down|up>.md` with the card, the engine output, and
the client's decision. If fills happen, record them per stock-desk workflow D and update
`portfolio/levels.csv` (`ladder_done`) and `portfolio/peak.txt` if a new high was set.

## Hard rules for this skill
- Never recommend selling VOO or touching the gold/cash vault, whatever the tape.
- Never deploy more than the engine's `deployable_now`; never all at once.
- A stop is a stop. "It'll bounce" is not a rule.
- On a ≥+3% index day, the only allowed trades are ladder trims, cap trims and trade-around sells in a sell zone
  (PLAN §3b, ≤ ⅓ of the line).
- If data is stale or missing, say "unverified" and give the rule-based answer conditionally —
  do not delay the card waiting for perfect data; a shock is time-sensitive.
- Delegation: `sonnet` for the data sweep, `opus` if a thesis-event deep dive is needed. Never `fable`.

## Files
- `scripts/shock_playbook.py` — engine (thresholds mirror PLAN.md; change both together)
- `portfolio/levels.csv` — per-name stops, ladder state, catalysts, rating (client-editable)
- `portfolio/peak.txt` — sleeve high-water mark for the circuit breaker
- `references/decision-card.md` — output template
