---
title: "Prandtl Number for Water"
aliases: ["Prandtl Number for Water"]
description: "Prandtl number for water in HVAC applications including temperature dependence, comparison with glycol solutions, impact on convective heat transfer coefficient calculations, and heat exchanger design implications for hydronic systems"
weight: 6
---

The Prandtl number (Pr) for water is a dimensionless parameter that characterizes the relative thickness of velocity and thermal boundary layers in convective heat transfer. In HVAC hydronic systems, accurate Prandtl number values are essential for calculating convective heat transfer coefficients and designing efficient heat exchangers.

## Definition and Physical Significance

The Prandtl number represents the ratio of momentum diffusivity to thermal diffusivity:

**Pr = ν/α = (μ/ρ)/(k/ρcp) = μcp/k**

Where:
- ν = kinematic viscosity (m²/s)
- α = thermal diffusivity (m²/s)
- μ = dynamic viscosity (Pa·s)
- ρ = density (kg/m³)
- cp = specific heat capacity (J/kg·K)
- k = thermal conductivity (W/m·K)

For water, the Prandtl number indicates that momentum diffuses approximately 7 times faster than heat at typical HVAC operating temperatures. This relationship fundamentally affects boundary layer development and heat transfer performance in hydronic equipment.

## Temperature Dependence of Prandtl Number

Water exhibits significant Prandtl number variation with temperature, primarily driven by the strong temperature dependence of dynamic viscosity. The following table provides Prandtl number values across the HVAC operating range:

| Temperature (°C) | Temperature (°F) | Prandtl Number | Deviation from 20°C |
|------------------|------------------|----------------|---------------------|
| 0                | 32               | 13.44          | +91.4%              |
| 10               | 50               | 9.40           | +33.9%              |
| 20               | 68               | 7.02           | Reference           |
| 30               | 86               | 5.49           | -21.8%              |
| 40               | 104              | 4.49           | -36.0%              |
| 50               | 122              | 3.77           | -46.3%              |
| 60               | 140              | 3.25           | -53.7%              |
| 70               | 158              | 2.86           | -59.3%              |
| 80               | 176              | 2.55           | -63.7%              |
| 90               | 194              | 2.29           | -67.4%              |
| 100              | 212              | 2.07           | -70.5%              |

The Prandtl number decreases approximately 70% as temperature increases from 0°C to 100°C. This reduction results from the rapid decrease in viscosity with increasing temperature, which dominates the more modest changes in thermal conductivity and specific heat.

## Engineering Correlations

For preliminary calculations in the HVAC operating range (5-95°C), the following approximation provides Prandtl number estimates within ±5%:

**Pr ≈ 13.5 - 0.11T + 0.00025T²**

Where T is temperature in °C. For more precise calculations requiring accuracy within ±1%, use property tables or established correlations such as IAPWS-IF97 formulations.

## Impact on Heat Transfer Calculations

The Prandtl number appears in virtually all convective heat transfer correlations used for HVAC equipment design:

**Turbulent Flow (Re > 10,000):**
Nu = 0.023Re^0.8·Pr^0.4 (Dittus-Boelter equation)

**Transitional Flow (2,300 < Re < 10,000):**
Nu = 0.116(Re^2/3 - 125)Pr^1/3[1 + (d/L)^2/3] (Hausen equation)

**Laminar Flow (Re < 2,300):**
Nu = 3.66 + (0.065(d/L)RePr)/(1 + 0.04[(d/L)RePr]^2/3) (Sieder-Tate type)

The exponent on Prandtl number varies from 0.3 to 0.4 in most turbulent flow correlations, indicating that heat transfer coefficient changes by approximately 2-3% for each 10% change in Prandtl number. This sensitivity necessitates using Prandtl values at the actual bulk fluid temperature rather than default values.

## Comparison with Other HVAC Fluids

Understanding how water compares to other heat transfer fluids clarifies design considerations:

| Fluid (20°C) | Prandtl Number | Thermal Boundary Layer | Design Implications |
|--------------|----------------|------------------------|---------------------|
| Water | 7.0 | Thin relative to velocity | High heat transfer coefficients |
| Ethylene glycol 30% | 15.5 | Thicker | 10-15% lower heat transfer |
| Ethylene glycol 50% | 27.0 | Much thicker | 20-30% lower heat transfer |
| Propylene glycol 30% | 18.5 | Thicker | 12-18% lower heat transfer |
| Propylene glycol 50% | 35.0 | Much thicker | 25-35% lower heat transfer |
| Engine oil | 1,050 | Very thick | Poor heat transfer fluid |
| Liquid metals | 0.01 | Very thin | Thermal resistance dominates |

Water's moderate Prandtl number (approximately 7) makes it an excellent heat transfer fluid. The thermal boundary layer is thin enough to provide good convective heat transfer while the fluid remains easy to pump due to low viscosity.

## Glycol Solution Effects

Adding freeze protection glycol significantly increases Prandtl number and reduces heat transfer performance:

**30% Ethylene Glycol Solution:**
- Prandtl number increases to approximately 15.5 at 20°C (121% increase)
- Heat transfer coefficient decreases by approximately 10-15%
- Required heat exchanger surface area increases by 12-18%

**50% Ethylene Glycol Solution:**
- Prandtl number increases to approximately 27 at 20°C (285% increase)
- Heat transfer coefficient decreases by approximately 25-30%
- Required heat exchanger surface area increases by 35-45%

The degradation is non-linear because the Pr^0.4 relationship in the Nusselt number correlation partially mitigates the effect. However, the simultaneous reduction in thermal conductivity and increase in viscosity create compounding effects on overall system performance.

## Design Implications for Heat Exchangers

The Prandtl number influences multiple aspects of heat exchanger selection and sizing:

**Surface Area Requirements:**
Systems using glycol solutions require 15-45% more heat transfer surface area than pure water systems at equivalent flow rates and temperature differentials. This impacts both equipment first cost and physical space requirements.

**Flow Velocity Selection:**
Higher Prandtl number fluids benefit more from increased flow velocity because the exponent on Reynolds number (0.8) exceeds the Prandtl exponent (0.4). Operating glycol systems at higher velocities partially compensates for reduced thermal performance, though at the cost of increased pumping power.

**Temperature-Dependent Performance:**
Heat exchangers operating with large temperature changes experience varying local Prandtl numbers along the flow path. The logarithmic mean temperature difference (LMTD) method assumes constant properties, which can introduce 5-10% error in sizing calculations when temperature spans exceed 30°C. The effectiveness-NTU method with property evaluation at multiple points provides more accurate results.

**Film Temperature Evaluation:**
For accurate heat transfer coefficient calculations, evaluate properties including Prandtl number at the film temperature (average of bulk fluid and surface temperatures) rather than bulk temperature alone. This correction becomes significant when wall-to-fluid temperature differences exceed 10°C.

## Boundary Layer Development

The Prandtl number directly determines the relative thickness of thermal and velocity boundary layers:

**δt/δv ≈ Pr^(-1/3)**

Where:
- δt = thermal boundary layer thickness
- δv = velocity boundary layer thickness

For water at 20°C (Pr = 7), the thermal boundary layer is approximately 52% of the velocity boundary layer thickness. This means heat transfer resistance concentrates in a relatively thin region near the surface, making water an efficient heat transfer fluid.

For 50% glycol solutions (Pr ≈ 27), the thermal boundary layer thickness drops to approximately 33% of the velocity boundary layer. The thicker thermal resistance layer reduces heat transfer effectiveness and requires more aggressive mixing or enhanced surfaces to maintain performance.

## Practical Application Guidelines

**Chilled Water Systems (4-10°C):**
Use Pr = 9-11 for heat transfer calculations. The elevated Prandtl number at low temperatures reduces convective coefficients by approximately 8-12% compared to calculations using room temperature properties.

**Hot Water Systems (70-90°C):**
Use Pr = 2.3-2.9 for heat transfer calculations. The reduced Prandtl number increases convective coefficients by approximately 15-20% compared to room temperature values.

**Glycol Systems:**
Always account for both temperature and concentration effects on Prandtl number. Calculate properties at the lowest expected operating temperature to ensure adequate heat transfer surface area under worst-case conditions.

**Condensing Systems:**
For condensers where water is the cooling medium, evaluate Prandtl number at the average water temperature (inlet plus outlet divided by 2) for overall heat transfer coefficient calculations. The condensate film resistance typically dominates, making water-side calculations less sensitive to property variations.

## Measurement and Verification

The Prandtl number cannot be measured directly but is calculated from measured thermophysical properties. For field verification of heat exchanger performance:

1. Measure actual fluid temperatures and flow rates
2. Determine fluid properties including Prandtl number at measured bulk temperature
3. Calculate actual heat transfer rate from Q = ṁcp∆T
4. Compare to design predictions using proper Prandtl correlations
5. Deviations exceeding 10-15% indicate fouling, air binding, or flow distribution issues

Apparent Prandtl number discrepancies often stem from incorrect fluid concentration measurements in glycol systems or failure to account for degraded glycol that has absorbed water or oxidized during service.

## Advanced Considerations

**Variable Property Effects:**
In high-temperature-difference applications (∆T > 30°C), the Prandtl number variation along the flow path requires integration of local heat transfer coefficients rather than using a single mean value. This approach can change heat exchanger effectiveness calculations by 3-8%.

**Enhanced Surfaces:**
Turbulators, fins, and enhanced surfaces increase the exponent on Prandtl number in heat transfer correlations from approximately 0.4 to 0.6-0.7. This makes enhanced surfaces particularly beneficial for high-Prandtl-number fluids like glycol solutions.

**Non-Newtonian Fluids:**
Severely degraded or contaminated glycol solutions may exhibit non-Newtonian behavior where apparent Prandtl number varies with shear rate. Replace any glycol solution showing viscosity increases exceeding 50% of fresh fluid values.

Understanding Prandtl number behavior enables accurate heat exchanger sizing, proper fluid selection, and realistic performance predictions across the full range of HVAC operating conditions. The 70% reduction in Prandtl number from 0°C to 100°C represents one of the largest temperature-dependent property variations affecting HVAC system design.
