# AI race — value-chain map

A classification and idea-sourcing map. **Not a buy list.** Every name must pass the full
`research-protocol.md` on live data before it is recommended. Tickers are US listings; check
which are available on Amana before proposing. Last reviewed: 2026-09-09 — refresh when the
narrative shifts.

| Layer | What it is | Representative names | Cycle character |
|---|---|---|---|
| Compute (GPUs/accelerators) | The picks and shovels; capex-driven | NVDA, AMD, AVGO (custom ASICs), MRVL | Highest quality, most crowded; moves on hyperscaler capex guidance |
| Foundry / manufacturing | Who fabs the chips | TSM, INTC (turnaround + US policy), ASML, AMAT, LRCX, KLAC | TSM = quality; INTC = policy/turnaround, headline-driven, high beta |
| Memory | HBM/DRAM bottleneck | MU, (Samsung, SK Hynix — non-US) | Cyclical; pricing-driven; big swings both ways |
| Networking & interconnect | Moving data between chips | ANET, CRDO, ALAB, CIEN, COHR | Second-derivative of GPU demand; can lead or lag |
| Power generation & fuel cells | Data centers need electrons now | BE (fuel cells), GEV (turbines), VST, CEG, TLN, NRG, OKLO/SMR (nuclear, speculative) | Ran hard 2025–26; thesis intact but valuations demand execution; crowded-trade risk |
| Power equipment & cooling | Grid, transformers, thermal | VRT, ETN, PWR, HUBB, MOD | Backlog-driven; less headline-volatile than fuel cells |
| Data-center real estate | Land, shells, leases | EQIX, DLR | Rate-sensitive; lower beta |
| Platforms / hyperscalers | Buyers of all the above; sell the models | MSFT, GOOGL, AMZN, META, ORCL | Fund the whole chain; their capex guidance is the master signal |
| Software / applications | Monetizing models | PLTR, CRM, NOW, SNOW, DDOG | Most disputed layer: "AI eats software" vs "software wins"; be selective |
| Edge / devices | On-device AI | AAPL, QCOM, ARM | Slower, consumer-cycle dependent |
| Second-order commodities | Inputs the buildout consumes | Copper (FCX), uranium (CCJ), natural gas (EQT) | Diversifiers within the theme; different drivers |

## How to use the map
- **Classify each holding by layer** so `portfolio_report.py` can compute theme concentration.
  Use the layer name as the `theme` column in `portfolio/holdings.csv`.
- **Rotation awareness**: within the AI race, leadership rotates (compute → power → memory →
  networking…). When a layer is > 20% above its 50-DMA on aggregate, look for the next layer that
  hasn't moved rather than chasing.
- **Master signals** to check every review: hyperscaler capex guidance (MSFT/GOOGL/AMZN/META
  earnings), NVDA earnings and data-center revenue, TSMC monthly sales, US export-control and
  CHIPS/tariff policy headlines, power-purchase-agreement announcements.
- **What breaks the theme**: capex cuts from two or more hyperscalers, a demonstrated collapse in
  inference pricing power, or credit stress in data-center financing. Any of these → move the sleeve
  toward the 80% AI cap floor immediately.
