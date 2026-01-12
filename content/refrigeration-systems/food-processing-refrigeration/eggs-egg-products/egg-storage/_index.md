---
title: "Egg Storage"
description: "Technical requirements for shell egg refrigerated storage including temperature control, humidity management, CO2 atmosphere effects, and quality preservation in commercial egg storage facilities."
weight: 1
---

Shell egg storage requires precise environmental control to maintain product quality and extend shelf life. The storage environment directly affects albumen quality, yolk condition, and overall egg grade retention through temperature-dependent biochemical reactions and moisture transfer mechanisms.

## Storage Temperature Requirements

Shell eggs respond to temperature control according to well-established degradation kinetics. The primary quality metric, Haugh unit (albumen quality), degrades following first-order reaction kinetics with a temperature-dependent rate constant.

**Recommended storage temperatures:**

| Storage Duration | Temperature Range | Expected Quality Retention |
|------------------|-------------------|---------------------------|
| Short-term (≤30 days) | 7-10°C (45-50°F) | AA to A grade maintenance |
| Medium-term (30-90 days) | 0-4°C (32-39°F) | A grade maintenance |
| Long-term (90-180 days) | -1 to 0°C (30-32°F) | B grade acceptable |

The lower temperature limit approaches -2°C (28°F), below which shell eggs begin to freeze. Ice crystal formation damages membranes and causes quality defects upon thawing.

Temperature uniformity throughout the storage space maintains consistent quality. Temperature stratification creates zones of accelerated degradation in warmer areas. Air circulation systems must prevent local temperature variations exceeding ±1°C.

## Relative Humidity Control

Moisture loss through the porous eggshell constitutes the primary physical change during storage. The shell contains 7,000-17,000 pores that permit water vapor transmission and gas exchange.

**Humidity specifications:**

| Parameter | Value | Basis |
|-----------|-------|-------|
| Target RH | 70-80% | Minimum moisture loss |
| Maximum RH | 85% | Mold growth prevention |
| Minimum RH | 65% | Excessive shrinkage limit |

At 70% RH and 7°C, shell eggs lose approximately 0.2% mass per week through evaporation. This moisture loss increases air cell size and reduces egg grade. At 60% RH, moisture loss doubles to 0.4% per week.

Higher humidity (80-85%) reduces moisture loss but increases surface mold risk, particularly with Pseudomonas and Penicillium species. Surface condensation occurs when eggs move from cold storage to warmer environments, promoting microbial growth on shells.

The vapor pressure difference between egg contents (100% RH equivalent) and ambient air drives moisture transfer. The mass transfer coefficient depends on air velocity across the shell surface and shell permeability, which varies by hen age, genetics, and nutrition.

## Carbon Dioxide Atmosphere Effects

Controlled atmosphere storage with elevated CO2 concentrations extends egg storage life by slowing albumen pH increase. Fresh egg albumen contains 3000-4000 ppm CO2 dissolved in the aqueous phase, creating pH 7.6-7.9. As CO2 diffuses through the shell pores, albumen pH rises to 9.0-9.5, degrading ovomucin-lysozyme complexes that maintain thick albumen structure.

**CO2 atmosphere parameters:**

| CO2 Concentration | Storage Temperature | Quality Extension | Application |
|-------------------|---------------------|-------------------|-------------|
| 0.5-2.0% | 7°C (45°F) | 50% longer AA grade | Standard CA storage |
| 2.0-5.0% | 2°C (36°F) | 100% longer AA grade | Extended storage |
| 10-15% | 0°C (32°F) | 200% longer AA grade | Research applications |

Enriched CO2 atmosphere maintains higher dissolved CO2 in albumen, preventing pH drift. The equilibrium CO2 concentration in albumen follows Henry's Law, with temperature-dependent solubility coefficients.

At 2% ambient CO2 and 7°C, albumen pH stabilizes near 8.0 rather than rising to 9.2, preserving thick albumen consistency measured by Haugh units. The Haugh unit equation:

**HU = 100 log(H - 1.7W^0.37 + 7.6)**

where H = albumen height (mm) and W = egg weight (g).

CA storage systems require gas mixing equipment, sealed rooms, and CO2 monitoring. The storage room air change rate must balance CO2 loss through leakage against CO2 injection to maintain setpoint concentration.

## Storage Life Determinants

Multiple factors beyond temperature determine achievable storage duration:

**Initial egg quality** sets the baseline for storage potential. Eggs collected within 2-4 hours and cooled rapidly to storage temperature maintain higher quality than eggs held at ambient conditions before refrigeration. The pre-cooling delay affects initial Haugh unit by approximately 2-3 units per hour at 20°C.

**Eggshell quality** determines moisture loss rate and microbial penetration resistance. Thicker shells with lower porosity maintain quality longer. Shell thickness averages 0.33-0.38 mm with conductance (gas and vapor transmission) inversely proportional to thickness.

**Air circulation patterns** affect both temperature uniformity and moisture loss. High-velocity air (>2 m/s) over shells increases evaporative moisture loss by 30-50% compared to low-velocity systems (<0.5 m/s). Packaging in fiberboard or plastic cases reduces shell exposure to airflow.

**Loading patterns** impact air distribution effectiveness. Solid stacking blocks airflow and creates warm zones. Palletized storage with gaps between cases permits air circulation. Minimum recommended spacing: 50 mm between pallets, 150 mm from walls.

**Egg age at receipt** matters for commercial storage. Eggs entering storage at 7-10 days post-lay have already degraded 5-10 Haugh units from fresh values of 90-100. Storage extends useful life but cannot recover lost quality.

## Quality Grade Maintenance

USDA shell egg grades (AA, A, B) depend on albumen height, yolk appearance, and air cell depth. Storage time systematically downgrades eggs through biochemical and physical changes.

**Expected grade transitions at optimal storage:**

| Initial Grade | Storage Conditions | Time to Downgrade | Final Grade |
|---------------|-------------------|-------------------|-------------|
| AA | 7°C, 75% RH | 30-45 days | A |
| A | 7°C, 75% RH | 60-90 days | B |
| AA | 2°C, 80% RH, 2% CO2 | 60-90 days | A |
| A | 2°C, 80% RH, 2% CO2 | 120-180 days | B |

Downgrading rate follows temperature-dependent kinetics. The Q10 value (rate increase per 10°C temperature rise) for Haugh unit degradation approximates 2.5-3.0. Storage at 15°C degrades eggs 2.5-3.0 times faster than storage at 5°C.

## Refrigeration System Design Considerations

Egg storage refrigeration systems must provide precise temperature control with minimal temperature swing and adequate dehumidification capacity matched to refrigeration load.

**Cooling load components:**

1. **Product heat removal**: Eggs enter storage at 15-25°C requiring cooling to storage temperature. Specific heat of whole eggs: 3.18 kJ/kg·K. For 10,000 kg daily throughput cooled from 20°C to 5°C: Q = 10,000 × 3.18 × 15 = 477 MJ (132 kWh).

2. **Respiration heat**: Shell eggs generate minimal metabolic heat, approximately 0.8-1.2 mW per egg at 5°C storage.

3. **Infiltration load**: Air leakage through doors and room envelope introduces warm, humid outside air. For rooms near loading docks, infiltration can exceed 20% of total cooling load.

4. **Equipment heat gains**: Motors, lights, and personnel contribute sensible heat loads.

Evaporator selection prioritizes high RH operation to minimize shell moisture loss. Large-face-area evaporators with low air velocity across coils (2-3 m/s) reduce dehumidification. Coil TD (temperature difference between refrigerant and air) should not exceed 4-6°C to prevent excessive moisture removal.

Defrost cycles must be minimized and carefully controlled. Hot gas defrost or electric defrost introduces heat requiring subsequent removal. Demand defrost based on coil pressure drop or temperature sensors reduces unnecessary defrost cycles.

## Monitoring and Control Requirements

Continuous temperature monitoring at multiple locations throughout the storage space detects thermal gradients and equipment malfunctions. Sensor placement includes:

- Warmest zone (typically upper corners, door areas)
- Coldest zone (often near evaporator discharge)
- Representative mid-space locations
- Product core temperature (sample cases)

Alarm setpoints trigger at ±1.5°C from setpoint to alert operators before significant quality degradation occurs. Temperature excursions above 10°C for more than 4 hours cause measurable quality loss.

Humidity sensors should be capacitive or chilled-mirror type calibrated regularly. Resistive humidity sensors drift in accuracy and require frequent recalibration or replacement.

Data logging systems record temperature and humidity at 15-minute intervals minimum, providing quality assurance documentation and identifying equipment degradation trends before failure occurs.

## Room Construction Features

Insulation requirements exceed standard cold storage due to the narrow temperature range specification. Wall, floor, and ceiling R-values typically reach R-30 to R-40 (metric: 5.3-7.0 m²·K/W) to minimize heat gain and maintain uniform temperatures.

Vapor barriers on the warm side of insulation prevent moisture migration into insulation, which degrades thermal performance. In cooler rooms operating near 0°C, vapor barrier integrity becomes critical.

Floor heating prevents ground freezing and frost heaving in facilities with below-grade floors or cold climates. Electric resistance cables or glycol piping beneath floor insulation maintain ground temperature above 5°C.

Air distribution requires multiple small evaporators distributed throughout large rooms rather than single large units. This arrangement improves temperature uniformity and reduces local high-velocity zones that accelerate moisture loss from product.

Door traffic management includes air curtains, plastic strip curtains, or vestibules to reduce infiltration during product movement. High-speed doors minimize open time during forklift traffic.
