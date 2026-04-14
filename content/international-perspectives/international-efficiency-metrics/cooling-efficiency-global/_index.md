---
title: "Global Cooling Efficiency Metrics and Standards"
aliases: ["Global Cooling Efficiency Metrics and Standards"]
description: "Technical analysis of worldwide cooling efficiency metrics including SEER, EER, SCOP, CSPF, and regional testing standards. Compare calculation methods, testing conditions, and labeling programs."
keywords:
  - SEER calculation
  - EER efficiency
  - SCOP cooling
  - CSPF China
  - ISEER India
  - cooling efficiency standards
  - ISO 5151
  - AHRI 210/240
  - EN 14511
  - global efficiency metrics
  - seasonal cooling efficiency
  - energy efficiency ratio
  - coefficient of performance
  - HVAC testing standards
  - efficiency labeling programs
weight: 1
---

## Global Cooling Efficiency Metrics and Standards

Cooling efficiency metrics vary significantly across global markets, reflecting different climate patterns, testing methodologies, and regulatory frameworks. Understanding these metrics enables accurate equipment comparison, proper system selection, and compliance with regional energy standards.

## Fundamental Efficiency Metrics

### Energy Efficiency Ratio (EER)

EER represents instantaneous cooling efficiency at specific test conditions:

**EER = Q_cooling / W_input**

Where:
- Q_cooling = Cooling capacity (Btu/h or W)
- W_input = Electrical power input (W or Wh)

**Standard Test Conditions:**

| Region | Indoor Conditions | Outdoor Conditions | Standard |
|--------|------------------|-------------------|----------|
| USA | 80°F DB / 67°F WB | 95°F DB | AHRI 210/240 |
| Europe | 27°C DB / 19°C WB | 35°C DB | EN 14511 |
| ISO | 27°C DB / 19°C WB | 35°C DB | ISO 5151 |
| China | 27°C DB / 19.5°C WB | 35°C DB | GB/T 7725 |

EER provides single-point efficiency but does not capture part-load or seasonal performance variations.

### Coefficient of Performance (COP)

COP uses consistent units for both cooling output and power input:

**COP = Q_cooling(W) / W_input(W)**

**Conversion Relationship:**

EER(Btu/Wh) = COP × 3.412

COP is the international standard for efficiency expression, used in ISO standards and most global markets outside North America.

## Seasonal Efficiency Metrics

### Seasonal Energy Efficiency Ratio (SEER)

SEER accounts for varying load conditions throughout the cooling season:

**SEER = ΣQ_cooling(i) / ΣW_input(i)**

Where summation occurs across weighted temperature bins representing typical seasonal conditions.

**SEER2 Calculation (2023 US Standard):**

Uses outdoor temperatures from 65°F to 104°F in 5°F increments, weighted by frequency:

| Temperature Bin | Weight Factor | Compressor State |
|----------------|---------------|------------------|
| 82°F | 0.214 | Cycling |
| 87°F | 0.231 | Cycling/Continuous |
| 92°F | 0.216 | Continuous |
| 97°F | 0.161 | Continuous |
| 102°F | 0.094 | Continuous |

SEER2 (AHRI 210/240-2023) replaced SEER (2008 standard) with more realistic testing including external static pressure requirements.

### European Seasonal Coefficient of Performance (SCOP)

SCOP for cooling (sometimes designated SEER_ON or ηs,c) follows EN 14825:

**SCOP_cooling = Q_cooling,annual / E_annual**

**Calculation incorporates:**
- Four temperature bins: 20°C, 25°C, 30°C, 35°C
- Part-load ratios: 100%, 74%, 47%, 21%
- Standby and off-mode losses
- Degradation coefficient for cycling

**Climate Zones:**

| Zone | Designation | Reference City | Design Temp |
|------|-------------|----------------|-------------|
| Average | A | Strasbourg | 35°C |
| Warmer | W | Athens | 35°C |
| Colder | C | Helsinki | 35°C |

### China Seasonal Performance Factor (CSPF)

CSPF applies to air conditioners under GB 21455:

**CSPF = Total_cooling_output(Wh) / Total_energy_input(Wh)**

**Test Points:**

| Outdoor Temp | Indoor Temp | Load % | Weight |
|-------------|-------------|--------|--------|
| 27°C | 27°C/19°C WB | 50% | 42% |
| 32°C | 27°C/19°C WB | 75% | 27% |
| 35°C | 27°C/19°C WB | 100% | 21% |
| 40°C | 27°C/19°C WB | 125% | 10% |

China's testing methodology emphasizes high-temperature performance relevant to southern climate zones.

### Indian Seasonal Energy Efficiency Ratio (ISEER)

ISEER under IS 1391 (Part 1):

**ISEER = Total_annual_cooling / Total_annual_energy**

**Weighted Bins:**

Based on 1600 hours annual operation:
- 24°C outdoor: 45% weight
- 28°C outdoor: 30% weight
- 32°C outdoor: 20% weight
- 37°C outdoor: 5% weight

Indoor conditions fixed at 27°C DB / 19°C WB.

### Annual Energy Efficiency Ratio (AEER) - Japan

Japan's JIS C 9612 defines AEER:

**AEER = Annual_cooling_output(MJ) / Annual_power_consumption(kWh)**

Uses regional climate data for Tokyo, with intermediate and minimum capacity operation weighted by occurrence frequency.

## Global Standards Comparison

### Testing Standard Frameworks

| Standard | Region | Scope | Key Features |
|----------|--------|-------|--------------|
| AHRI 210/240 | USA/Canada | Unitary AC & HP | SEER2, EER2, external static pressure |
| EN 14511 | Europe | AC & chillers | Part 1-4: terms, testing, marking, requirements |
| EN 14825 | Europe | Heat pumps | Seasonal calculation, climate zones |
| ISO 5151 | International | AC & HP | Reference standard, widely adopted |
| GB/T 7725 | China | Room AC | Fixed and variable speed units |
| GB 21455 | China | Minimum efficiency | CSPF requirements, energy grades |
| JIS C 9612 | Japan | Room AC | APF (heating), AEER (cooling) |
| IS 1391 | India | Room AC | ISEER, star rating program |
| AS/NZS 3823 | Australia/NZ | AC performance | EER, AEER for labeling |

### Efficiency Metric Conversion

Approximate conversions between seasonal metrics:

**SEER2 ≈ SEER × 0.95**

**SCOP_cooling ≈ SEER ÷ 3.6**

**CSPF ≈ SEER × 1.05** (rough approximation)

**Note:** Direct conversion is imprecise due to different climate assumptions, test procedures, and weighting factors.

## Minimum Efficiency Requirements

### Regional Minimum Standards (2024)

| Region | Metric | Minimum Split AC | Effective Date |
|--------|--------|------------------|----------------|
| USA | SEER2 | 13.4-14.3 (regional) | Jan 2023 |
| Canada | SEER | 13.0-14.0 (regional) | Jan 2017 |
| EU | SCOP | Class D minimum | Mar 2021 |
| China | CSPF | 3.2 (Grade 3) | Jul 2020 |
| India | ISEER | 3.1 (2-star) | Jan 2018 |
| Japan | APF | 5.8 (cooling 4.0kW) | Apr 2027 |
| Australia | AEER | Various by capacity | Multiple phases |

## Energy Labeling Programs

### Label Format Comparison

**USA - EnergyGuide:** Yellow label showing estimated annual energy cost, SEER2 rating, and comparison range.

**Europe - EU Energy Label:** A-G scale (revised 2021), annual energy consumption in kWh, cooling capacity, sound power.

**China - CEL:** 5-grade scale (Grade 1 highest), CSPF value, cooling capacity, power input.

**India - BEE Star Rating:** 1-5 star scale, ISEER value, annual energy consumption estimate.

**Japan - Unified Energy Label:** Multi-year targets (up to 4 stars), annual energy consumption, market position indicator.

## Physical Principles and Measurement

Seasonal metrics capture two critical thermodynamic realities:

**Part-Load Degradation:** Compressor cycling introduces losses from refrigerant migration, repeated startup transients, and control system inefficiencies. The degradation coefficient (C_D) quantifies efficiency reduction:

**COP_cyclic = COP_steady × (1 - C_D × (1 - PLR))**

Where PLR = part load ratio.

**Temperature Dependence:** Carnot efficiency establishes theoretical limits:

**COP_Carnot = T_indoor / (T_outdoor - T_indoor)**

Real systems achieve 40-60% of Carnot efficiency, with the ratio improving at lower lift conditions.

## Testing Procedure Variations

Key procedural differences affecting measured efficiency:

**Air Flow Measurement:** Nozzle chamber (ISO 5151), pitot traverse (AHRI), or air enthalpy method (EN 14511).

**Psychrometric Control:** Indoor/outdoor chamber tolerances range from ±0.3°C (ISO) to ±0.5°F (AHRI).

**Refrigerant Charge:** Subcooling method, superheat method, or manufacturer specification.

**Defrost Credit:** European standards provide energy credit for reverse-cycle defrost losses; US standards do not.

## System Selection Implications

Higher seasonal efficiency metrics indicate:
- Superior part-load performance through variable-capacity compressors
- Optimized refrigerant circuit design for varying conditions
- Advanced controls minimizing cycling losses
- Efficient fan and pump systems

When comparing equipment across regions, verify test standard alignment and climate suitability rather than relying solely on metric values.
