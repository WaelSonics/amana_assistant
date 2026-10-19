# Shock (down) — Friday 2026-10-16 close, reviewed Saturday 10/17

Client: "Holly shit man, fuck this shit. The market closed down." Then: "I have lost most of what we worked for. How should
we fucking proceed. I will not do anything stupid from now on."

## The move (Yahoo daily bars, 10/16 close)
- **Indexes:** S&P 500 7,659.44, −1.09% on the day and −2.0% from the 7,818.93 record. Nasdaq-100 −2.50%.
- **Semiconductors:** SOX −3.83%, its 8th straight down day, the longest streak since 2008.
- **Volatility and rates:** VIX 19.99 (+21%); 10-year 5.10%.
- **Cause** (Quartz, Kotak, TradingKey, 10/16):
  - doubts that debt-funded AI infrastructure earns enough to repay its borrowing (CoreWeave −12%, ≈ −25% in five sessions);
  - CXMT memory progress (MU ≈ −10% on the week);
  - higher oil and inflation worries.
  The Nasdaq-100 had its worst week in about 18 months.

| | Close | Day | vs cost | Stop | Distance |
|---|---|---|---|---|---|
| AMD | 528.75 | −6.0% | −3.3% | 498 | 6.2% |
| ARM | 227.80 | −6.9% | −11.0% | 220 | 3.5% |
| MU | 878.84 | −5.6% | −5.1% | 850 | 3.4% |
| TTWO | 205.28 | −2.0% | −3.7% | 190 | 8.0% |
| VOO | 701.61 | −1.1% | −0.6% | — | — |

- **Account:** **$3,417.92**, −9.6% from the $3,779.85 peak and **$16 above the $3,402 circuit breaker**. Cash $712.20 (20.8%).
- **Last two days:** −$91.49 on 10/16. AMD −$30.63, ARM −$26.62, VOO −$13.29, MU −$11.31, TTWO −$9.64.
- **Against money put in:** **+$114.66 (+3.5%)** on $3,303.26. At the peak it was +$476.59. About ¾ of the gain is
  given back, and no capital is lost.
- **Override ledger** at the 10/16 close: **−$227.38**. That is ≈ 63% of the $362 fall from the peak.

## Engine (`shock_playbook.py`)
- **Class:** NOISE for the index (−1.1% on the day, −2.0% from the high, VIX 20). No VOO tranche, because §5 needs −4%.
- **Mechanical actions:** none.
- **Flags:** ARM and MU stops are CLOSE (≈ 3.5%), so do not add.
- **Engine bug:** it printed ARM "BUY ZONE 225–233" but did not apply the lock in `levels.csv`, which keeps ARM locked
  until after 11/4 and the royalty ruling. The engine does not read the `lock` text, so this has to be fixed in the
  script.

## Macro or mine?
Mine. The causes (AI financing doubts, CXMT) are the same question that drives AMD, ARM and MU: 30% of the account, and the
three names fell 5.6–6.9% together. It is a fear, not yet a thesis break: no capex cut and no guidance cut. The answers are
dated:
- SK hynix 10/27.
- Samsung and SNDK 10/29.
- Hyperscaler reports, late October (dates unverified).
- AMD 11/3 and ARM 11/4.
Until then: no adds to any AI-chip name. The stops decide.

## Decision card
1. **Weekend: nothing.** Confirm in the app that four stops are live: AMD 498, ARM 220, MU 850, TTWO 190.
2. **Monday 10/19, one check at 15:45 ET.** Look at the account value in the app.
   - **$3,402 or above:** do nothing.
   - **Below $3,402:** the circuit breaker fires (PLAN §7). Sell **half of each satellite at market** before the close:
     - AMD 0.4574 sh (≈ $242)
     - ARM 0.7834 sh (≈ $178)
     - MU 0.1079 sh (≈ $95)
     - TTWO 1.1758 sh (≈ $241)

     Keep VOO, make no buys (not even the VOO rung), and write the post-mortem with the desk.
3. **A stop that fires is final.** No re-buy that session; §4a applies after. Stops never move down.
4. **October buying is closed.** No buys until 11/2, after the memory and hyperscaler prints. Buys #11–12 are not used.
5. **Watch levels:** S&P closes ≤ 7,506 → the VOO rung (¼ of cash), unless the breaker has fired. ANET: zone A failed
   (closed 176.98), so ≤ $160 only.

## Do NOT
- Sell everything at Monday's open out of anger. The plan has a written level for each line.
- "Buy the dip" with the $712. October is closed, and the breaker is $16 away.
- Lower a stop to avoid a sale (QUBT 8 → 7 cost $25; EWY 172 → 165 cost $31).
- Touch VOO or the vault.

## Lesson
The drawdown has two parts:
- **The sector** (8 straight down days in chips): the plan's stops and breaker exist for this.
- **The overrides** (−$227): the client's part, which comes down to size, timing and same-day re-buys.

"I will not do anything stupid" becomes concrete as one rule: no order without a written level, size and stop from the desk.

## Artifacts refreshed (10/17)
- Flag Board v17: priced at the 10/16 close. Monday's breaker check is step 1, with exact half-sizes. ANET is zone B only.
  October buying is shown as closed.
- Account Ledger v12: priced at the 10/16 close. Equity $3,417.92, +$114.66 (+3.5%) on money in, open −$95.99.
- Client asked whether the desk can trade and check for them. I found no public Amana trading API (search 10/17; to confirm
  with Amana support). The desk cannot place orders. Offered: a scheduled Monday 15:45 ET breaker check that messages the
  exact action. The broker stops are already the automatic part.
