---
title: "External Flow"
aliases: ["External Flow"]
weight: 1
---

External forced convection involves fluid flow over surfaces where the boundary layer develops without confinement. This regime governs heat transfer from building exteriors, HVAC equipment in outdoor installations, and heat exchangers with flow across tube bundles.

## Flat Plate Correlations

### Laminar Boundary Layer (Re_x < 5×10⁵)

The local Nusselt number for laminar flow over a flat plate:

Nu_x = 0.332 Re_x^(1/2) Pr^(1/3)

where:
- Re_x = ρVx/μ = local Reynolds number
- x = distance from leading edge
- Valid for Pr ≥ 0.6

The average Nusselt number over length L:

Nu_L = 0.664 Re_L^(1/2) Pr^(1/3)

For liquid metals (Pr < 0.05):

Nu_x = 0.565 (Re_x Pr)^(1/2)

### Turbulent Boundary Layer (Re_x > 5×10⁵)

Local Nusselt number for turbulent flow:

Nu_x = 0.0296 Re_x^(4/5) Pr^(1/3)

Valid for:
- 5×10⁵ < Re_x < 10⁷
- 0.6 ≤ Pr ≤ 60

For higher Reynolds numbers (10⁷ < Re_x < 10⁹):

Nu_x = 0.0296 Re_x^(4/5) Pr^(0.4)

Average Nusselt number (turbulent from leading edge):

Nu_L = 0.037 Re_L^(4/5) Pr^(1/3)

### Mixed Boundary Layer

When transition occurs on the plate (Re_crit = 5×10⁵):

Nu_L = (0.037 Re_L^(4/5) - 871) Pr^(1/3)

This accounts for the laminar region before transition.

### Colburn Analogy

Relates heat transfer to friction:

St Pr^(2/3) = C_f/2

where St = Nu/(Re Pr) is the Stanton number.

## Cylinder in Crossflow

### Flow Regimes

Flow over cylinders exhibits distinct regimes:

| Re Range | Flow Characteristics |
|----------|---------------------|
| Re < 4 | Creeping flow, no separation |
| 4 < Re < 40 | Separation bubble forms |
| 40 < Re < 150 | Vortex shedding begins |
| 150 < Re < 3×10⁵ | Laminar boundary layer, vortex street |
| 3×10⁵ < Re < 3×10⁶ | Transition, drag crisis |
| Re > 3×10⁶ | Turbulent boundary layer |

### Churchill-Bernstein Correlation

Comprehensive correlation for cylinders:

Nu_D = 0.3 + [0.62 Re_D^(1/2) Pr^(1/3)] / [1 + (0.4/Pr)^(2/3)]^(1/4) × [1 + (Re_D/282000)^(5/8)]^(4/5)

Valid for:
- Re Pr > 0.2
- All Reynolds numbers

### Simplified Correlations

For specific Reynolds ranges:

| Re Range | Nu_D Correlation | Applicability |
|----------|-----------------|---------------|
| 0.4 - 4 | 0.989 Re^0.330 Pr^(1/3) | Stagnant flow |
| 4 - 40 | 0.911 Re^0.385 Pr^(1/3) | Separation forming |
| 40 - 4000 | 0.683 Re^0.466 Pr^(1/3) | Vortex shedding |
| 4000 - 40000 | 0.193 Re^0.618 Pr^(1/3) | Subcritical |
| 40000 - 400000 | 0.027 Re^0.805 Pr^(1/3) | Critical transition |

Properties evaluated at film temperature: T_f = (T_s + T_∞)/2

### Vortex Shedding

Strouhal number relates shedding frequency to flow:

St = fD/V = 0.21 (for 250 < Re < 2×10⁵)

where f is the vortex shedding frequency (Hz).

## Tube Banks

### Configuration Parameters

Tube bank geometry defined by:

| Parameter | Definition |
|-----------|-----------|
| S_T | Transverse pitch (perpendicular to flow) |
| S_L | Longitudinal pitch (parallel to flow) |
| S_D | Diagonal pitch = √(S_L² + (S_T/2)²) |
| D | Tube outer diameter |

Arrangement types:
- **Inline**: Tubes aligned in flow direction
- **Staggered**: Offset rows for enhanced mixing

### Maximum Velocity

For inline arrays:

V_max = (S_T/(S_T - D)) V

For staggered arrays, use minimum of:

V_max = (S_T/(S_T - D)) V  or  V_max = (S_T/(2(S_D - D))) V

### Žukauskas Correlation

For tube banks with N_L ≥ 20 rows:

Nu_D = C Re_D,max^m Pr^0.36 (Pr/Pr_s)^(1/4)

Constants C and m depend on arrangement and Re:

**Inline Arrays:**
| Re_D,max | C | m |
|----------|---|---|
| 10-100 | 0.80 | 0.40 |
| 100-1000 | 0.51 | 0.50 |
| 1000-2×10⁵ | 0.27 | 0.63 |
| 2×10⁵-2×10⁶ | 0.021 | 0.84 |

**Staggered Arrays:**
| Re_D,max | C | m |
|----------|---|---|
| 10-100 | 0.90 | 0.40 |
| 100-1000 | 0.51 | 0.50 |
| 1000-2×10⁵ | 0.35 (S_T/S_L < 2) | 0.60 |
| 1000-2×10⁵ | 0.40 (S_T/S_L > 2) | 0.60 |
| 2×10⁵-2×10⁶ | 0.022 | 0.84 |

For N_L < 20, apply correction factor:

Nu_D,N = F Nu_D

where F ranges from 0.70 (N_L = 1) to 1.0 (N_L ≥ 20).

### Pressure Drop

Pressure drop across tube bank:

ΔP = N_L χ (ρV_max²/2) f

where:
- χ = correction factor for entrance/exit effects
- f = friction factor (function of Re and geometry)

## Building Exterior Convection

### Wind-Driven Heat Transfer

Heat loss from building envelopes:

q = h_o A (T_s - T_amb)

where h_o is the exterior convective coefficient.

### Correlations for Vertical Walls

**Forced Convection (wind-dominated):**

h_o = 5.7 + 3.8V (SI units: W/m²·K, V in m/s)

h_o = 1.0 + 0.67V (Imperial: Btu/hr·ft²·°F, V in mph)

**McAdams correlation:**

Nu = 0.037 Re^0.8 Pr^(1/3) (for Re > 5×10⁵)

Properties evaluated at film temperature.

### ASHRAE Winter Design Conditions

For outdoor design calculations:

h_o = 34 W/m²·K (6.0 Btu/hr·ft²·°F) at 6.7 m/s (15 mph)

Conservative value for peak load calculations.

### Wind Direction Effects

Local heat transfer varies with position:

| Location | h/h_avg |
|----------|---------|
| Windward face | 1.3-1.5 |
| Side faces | 0.8-1.0 |
| Leeward face | 0.5-0.7 |
| Roof windward | 1.5-2.0 |
| Roof leeward | 0.6-0.8 |

### Combined Natural and Forced Convection

Total heat transfer:

h_total = (h_forced^n + h_natural^n)^(1/n)

where n = 3 for most building applications.

## Condensing Unit Heat Rejection

### Air-Cooled Condensers

Heat transfer from finned coil:

q = U_o A_o LMTD

External convection coefficient:

h_o = ε_f η_f h_bare

where:
- ε_f = fin effectiveness factor
- η_f = fin efficiency
- h_bare = bare tube convection coefficient

### Fin Efficiency Consideration

For rectangular fins:

η_f = tanh(mL)/(mL)

where m = √(2h/kt) and L is fin height.

Overall surface effectiveness:

ε_o = 1 - (A_f/A_o)(1 - η_f)

## Reynolds Number Effects

Critical Reynolds numbers for transition:

| Geometry | Re_crit | Transition Behavior |
|----------|---------|-------------------|
| Flat plate | 5×10⁵ | Laminar to turbulent BL |
| Cylinder | 2×10⁵ | Drag crisis, BL separation delay |
| Sphere | 2.5×10⁵ | Similar to cylinder |

## Property Evaluation

Temperature for evaluating properties:

**Film temperature method:**
T_f = (T_s + T_∞)/2

**Property ratio method:**
Evaluate at T_∞, apply (Pr/Pr_s)^0.25 correction

For gases, property variation is minor. For liquids, correction is essential.

## HVAC Applications

**Outdoor equipment:**
- Condensing units exposed to wind
- Cooling towers with crossflow
- Rooftop unit heat rejection
- Heat pump outdoor coils

**Heat exchanger design:**
- Shell-and-tube with crossflow over tubes
- Finned coil banks in air handlers
- Economizer outdoor air heat exchangers

**Building envelope:**
- Exterior wall and roof heat loss
- Window surface temperatures
- Thermal bridge analysis at projections

## Components

- Flat Plate Laminar
- Flat Plate Turbulent
- Flat Plate Mixed
- Cylinder Crossflow
- Sphere Flow
- Tube Banks
- Noncircular Cylinders
- Impinging Jets
- Boundary Layer Development
- Reynolds Analogy
- Colburn Analogy
