# Pre-reset period 2025-11-02 → 2026-08-12 — what the statement says

Written 2026-09-09 from the Amana statement. This period is excluded from performance measurement
but it is the best behavioral data we have.

## Account structure (the biggest change)
Pre-reset the account was **leveraged/CFD**: open losses reduced usable equity, so spare cash was
frozen exactly when it was needed, and shorting/2× buying were available (see ARM). On 2026-08-12 it
was converted to a **cash account** — positions fully paid, side cash always deployable, no shorts,
no leverage, no overnight financing fees. The 8/12 $3,022 withdrawal / 8/18 re-deposit was the switch.

## Numbers
- Realized gross +$208.94 (lifetime to 2026-09-08, of which ≈ +$97 came after the reset) → pre-reset
  realized ≈ +$97 net of $84 fees. On ~$3,000 of capital over 9 months: roughly flat.
- 62 clearing fees ($62) + $22 CFD overnight fees = **$84, ~30% of gross realized profit**.

## What made money (≈ +$525)
ANET +$155 · TSM +$106 · MU +$83 · TTWO +$81 · LITE +$77 (4 short swings) · NVDA +$71 · EWY +$32 ·
MRVL +$29 · SIVR +$27. **Every meaningful winner was a long in AI infrastructure**, held days to months.

## What lost money (≈ −$430)
- **ARM short via CFD −$242** (2026-04-22 short @195.75 covered 205.21; 2026-05-20 short @256.84
  covered 402–410 during the run to the $439 ATH). Largest loss by far. Lesson: never short momentum,
  never CFD on this sleeve.
- SNDK −$80 (bought 2026-06-30 @ $2,199 after a 2.4× run; sold 8/12 @ $1,319). BE −$63 (bought
  6/29 @ $274.5 at the local top). Lesson: chasing after vertical moves; the fix — waiting and
  re-entering BE at $207.70 in August — is exactly what worked.
- Speculative/non-thesis: SLV −$48, SPCX −$41, CHZUSD −$39, GLD −$22, QUBT −$18. Lesson: outside the
  thesis and outside your edge; gold exposure belongs in the physical gold, not in a leveraged CFD.
- Small fills ($20–$100) with a $1 fee = 1–5% drag before the trade starts.

## Rules that came out of this (now in `risk-rules.md`)
No shorts/CFDs/leverage · no buying >20% above the 50-DMA · few positions, fewer trades · enter in
halves · defined invalidation before entry · lock gains into strength with a re-entry plan.
