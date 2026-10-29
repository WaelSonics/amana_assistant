---
name: market-move
description: Emergency desk for a sharp market move — up or down. When Wael says the market crashed / sold off / ripped / is up or down big, VIX spiked, "what do I do now", or a holding gapped on news, fetch live index, VIX and cause, run the PLAN.md rules mechanically against every holding and the cash reserve, and return one decision card — exact actions, exact do-nots, and a challenge if his instinct breaks the plan.
---

# Market Move — shock playbook (plan v6)

One job: turn a scary (or euphoric) tape into a short list of pre-agreed actions, fast, without improvising. The rules live
in `PLAN.md` (v6, adopted 2026-10-29); this skill applies them. Read `PLAN.md` and
`../stock-desk/references/investor-profile.md` first. The stock-desk non-negotiables apply (fresh dated numbers only;
client decides; challenge once; log it).

## What v6 means on a shock day
- **Nothing is decided intraday.** The app's SLs and TPs act on their own. Dip signals are read on the **close**, and buys
  happen at the next open. A shock day is the input to tonight's scan, not a reason to trade now.
- **VOO is never sold** and has no stop. There is no cash-tranche ladder in v6. VOO grows only through the monthly $200
  (while under 35%).
- **Brakes:** a close under $3,212.87 (−15% from the $3,779.85 peak) pauses new buys for two weeks; closed dip trades net
  −$400 pause them until a review. Nothing is force-sold.

## Workflow — target: decision card in one pass
### 1. Measure the move (live, dated): subagent `sonnet`, one sweep
- S&P 500 and Nasdaq-100: % move, level, the record close. VIX, the 10-year, and the cause in one line from ≥ 2 sources
  (macro, geopolitical, credit, AI/semis-specific, single-name).
- For any holding moving > 2× the index: the headline behind it.

### 2. Run the tools
```
python3 .claude/skills/stock-desk/scripts/levels.py --report             # stops/TPs, slots, cash, brakes, themes
python3 .claude/skills/stock-desk/scripts/levels.py <PLAN §6 watchlist>  # the "Dip rule (v6)" line per name
```

### 3. Judgment layer: three questions, ≤ 2 sentences each, with the data
1. **Is it macro, or a thesis break?** A thesis break named in a holding's study is a sell at the next open, whatever the
   price. Anything else: the SL and TP decide.
2. **Which names may signal at tonight's close, and which would we take?** Apply slots, cash ≥ $150, ≤ 2 per theme, the
   earnings blackout, and the brakes. Rank by trend strength. Give $400 per name and the study list. No buy before the close.
3. **On an up-shock:** which TPs fired or are close. There is no other selling in v6.

### 4. Deliver the decision card (template in `references/decision-card.md`)
Verdict line → what the stops and TPs did → tonight's possible signals → do-nots → what would change the call in 48h → the
lesson if the client's instinct differed.

### 5. Challenge and log
Test the client's instinct ("sell everything", "buy it now, it's down") against PLAN v6 §4 **first**, and lead with the
challenge if it fails. Write `journal/YYYY-MM-DD-shock-<down|up>.md`. Record fills per stock-desk workflow D and update
`portfolio/levels.csv`.

## Hard rules for this skill
- Never sell VOO; never touch the physical vault.
- Never an intraday buy on a shock. Signals come from closes.
- A stop is a stop: never lowered, never removed, and no re-buy in the session it fired.
- If data is stale or missing, say "unverified" and answer conditionally. A shock is time-sensitive.
- Delegation: `sonnet` for the data sweep, `opus` for a thesis-break deep dive. Never `fable`.

## Files
- `scripts/shock_playbook.py`: **retired with plan v3** (reserve tranches, ladder, −10% breaker). Do not run it under v6.
- `portfolio/levels.csv`: per-line kind, stop, tp, exit_by, theme.
- `portfolio/peak.txt`: the high-water mark for the account brake. Never reset it to make room.
- `references/decision-card.md`: output template.
