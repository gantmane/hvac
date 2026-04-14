---
title: "Interstitial Condensation"
aliases: ["Interstitial Condensation"]
description: "Analysis of moisture condensation within building envelope assemblies using vapor pressure profiles, dew point calculations, and transient moisture transport modeling for preventing moisture damage in wall and roof systems"
weight: 3
---

Interstitial condensation occurs when water vapor migrates through a building assembly and condenses at an interface or within a layer where the local temperature drops below the dew point of the air-vapor mixture. Unlike surface condensation, this phenomenon occurs within the concealed portions of wall, roof, and floor assemblies, making detection difficult until significant damage accumulates.

## Fundamental Physics of Interstitial Condensation

Vapor diffusion through building assemblies follows Fick's first law, where moisture flux depends on vapor pressure gradient and material permeance:

**Vapor Diffusion Rate:**
```
g = M × ΔP
```

Where:
- g = vapor flux (grains/h·ft² or kg/s·m²)
- M = permeance (perms or ng/Pa·s·m²)
- ΔP = vapor pressure difference (in. Hg or Pa)

**Permeability Relationship:**
```
M = μ / d
```

Where:
- μ = permeability (perm-inch or ng/Pa·s·m)
- d = material thickness (inches or m)

Condensation occurs at any location where:
```
P_actual ≥ P_sat(T)
```

Where:
- P_actual = actual vapor pressure at the location
- P_sat(T) = saturation vapor pressure at local temperature

## Temperature Profile Analysis

The temperature at any point within a multi-layer assembly is determined by the thermal resistance distribution. For steady-state conditions:

**Temperature at Interface n:**
```
T_n = T_i - [(T_i - T_o) × Σ(R_1 to R_n)] / R_total
```

Where:
- T_n = temperature at interface n (°F or °C)
- T_i = interior temperature (°F or °C)
- T_o = exterior temperature (°F or °C)
- R_1 to R_n = R-values from interior to interface n (ft²·h·°F/BTU or m²·K/W)
- R_total = total assembly R-value (ft²·h·°F/BTU or m²·K/W)

**Example Temperature Distribution:**

| Location | R-Value (cumulative) | Temperature at 70°F inside, 20°F outside |
|----------|---------------------|------------------------------------------|
| Interior surface | 0.68 | 70°F |
| Gypsum board (1/2") | 1.13 | 68°F |
| Fiberglass batt (5.5") | 20.13 | 29°F |
| Sheathing (1/2") | 20.76 | 28°F |
| Air film exterior | 21.01 | 20°F |

## Vapor Pressure Profile Analysis

The vapor pressure profile through an assembly depends on the permeance distribution and boundary conditions.

**Vapor Pressure at Interface n:**
```
P_n = P_i - [(P_i - P_o) × Σ(1/M_1 to 1/M_n)] / Σ(1/M_total)
```

Where:
- P_n = vapor pressure at interface n (in. Hg or Pa)
- P_i = interior vapor pressure (in. Hg or Pa)
- P_o = exterior vapor pressure (in. Hg or Pa)
- M_1 to M_n = permeance from interior to interface n (perms)
- M_total = inverse sum of all layer vapor resistances

**Saturation Vapor Pressure:**

The Antoine equation provides saturation vapor pressure as a function of temperature:

```
log₁₀(P_sat) = A - B / (C + T)
```

For water vapor (°C and kPa):
- A = 8.07131
- B = 1730.63
- C = 233.426

For IP units (°F and psi):
```
P_sat = exp[77.3450 + 0.0057(T) - 7235/(T + 459.67)] / (T + 459.67)^8.2
```

Simplified approximation for typical temperatures:
```
P_sat (in. Hg) ≈ 0.00126 × exp[0.0688 × T(°F)]
```

## Dew Point Method

The dew point method compares the actual temperature at each interface with the dew point temperature corresponding to the local vapor pressure.

**Procedure:**

1. Calculate temperature profile through assembly
2. Calculate vapor pressure profile through assembly
3. Determine dew point at each interface using inverse saturation relationship
4. Compare actual temperature to dew point temperature
5. Condensation occurs where T_actual < T_dewpoint

**Dew Point Temperature:**

From vapor pressure, the dew point can be determined:

```
T_dp = 100.45 + 33.193 × ln(P_v) + 2.319 × [ln(P_v)]² + 0.17074 × [ln(P_v)]³ + 1.2063 × [P_v]^0.1984
```

Where:
- T_dp = dew point temperature (°F)
- P_v = vapor pressure (psia)

For SI units (P in kPa, T in °C):
```
T_dp = 234.175 × ln(P_v/0.6105) / [17.08085 - ln(P_v/0.6105)]
```

## Glaser Method

The Glaser method is a simplified steady-state approach standardized in ISO 13788 for predicting interstitial condensation. It assumes one-dimensional vapor diffusion and steady-state conditions.

**Monthly Calculation Procedure:**

1. Define monthly average interior and exterior conditions
2. Calculate temperature profile for each month
3. Calculate vapor pressure profile for each month
4. Identify condensation plane (where vapor pressure line intersects saturation line)
5. Calculate monthly condensation accumulation
6. Calculate monthly evaporation
7. Sum annual moisture balance

**Condensation Rate:**

When condensation occurs at a plane:

```
g_c = (P_i - P_sat,c) / Σ(Z_i to c) = (P_sat,c - P_o) / Σ(Z_c to o)
```

Where:
- g_c = condensation rate (grains/h·ft²)
- P_sat,c = saturation vapor pressure at condensation plane
- Z = vapor resistance (1/perm)

**Critical Design Criteria:**

Per ISO 13788, a construction is acceptable if:
- Maximum moisture content remains below critical levels
- Accumulated moisture evaporates during drying season
- No water accumulation at interfaces with low permeability

## Material Vapor Permeability Properties

Material vapor permeability governs diffusion rates and condensation potential.

| Material | Permeability (perm-inch) | Vapor Retarder Class |
|----------|--------------------------|---------------------|
| Polyethylene (6 mil) | 0.06 | Class I (impermeable) |
| Aluminum foil (1 mil) | 0.01 | Class I (impermeable) |
| OSB sheathing (7/16") | 0.70 | Class III (permeable) |
| Plywood (1/2") | 0.80 | Class III (permeable) |
| Gypsum board (1/2") | 50 | Not a vapor retarder |
| Kraft paper facing | 1.0 | Class II (semi-impermeable) |
| Extruded polystyrene | 1.2 | Class II (semi-impermeable) |
| Expanded polystyrene | 2.0-5.6 | Class III (permeable) |
| Closed-cell spray foam (1") | 0.4-1.6 | Class II (semi-impermeable) |
| Open-cell spray foam (1") | 8.0-11.0 | Not a vapor retarder |
| Mineral fiber batt | 100+ | Not a vapor retarder |

**Vapor Retarder Classifications (per 2021 IRC/IBC):**

- Class I: ≤ 0.1 perm
- Class II: > 0.1 and ≤ 1.0 perm
- Class III: > 1.0 and ≤ 10 perm

## Condensation Plane Identification

The condensation plane location depends on the relative vapor resistance distribution and thermal resistance distribution.

**Graphical Method:**

1. Plot temperature profile through assembly on psychrometric chart
2. Plot saturation curve on same chart
3. Plot vapor pressure profile
4. Intersection of vapor pressure line with saturation curve indicates condensation plane

**Analytical Method:**

For a two-layer system (interior vapor retarder and permeable insulation):

```
R_c / R_total = (P_i - P_sat,c) × M_total / (P_i - P_o)
```

Where:
- R_c = thermal resistance from interior to condensation plane
- This establishes the temperature at condensation plane

Solve iteratively since P_sat,c depends on T_c which depends on R_c.

## Moisture Accumulation Rate

The rate of moisture accumulation within an assembly determines the severity of the condensation problem.

**Steady-State Accumulation:**

```
M_acc = g_c × A × t
```

Where:
- M_acc = accumulated moisture mass (lb or kg)
- g_c = condensation rate (lb/h·ft² or kg/s·m²)
- A = area (ft² or m²)
- t = time duration (hours or seconds)

**Critical Moisture Content:**

Different materials have critical moisture content levels above which performance degrades:

| Material | Critical Moisture Content (% by weight) | Consequence |
|----------|----------------------------------------|-------------|
| Wood framing | 20% | Decay fungi growth |
| OSB sheathing | 18% | Strength reduction, swelling |
| Mineral fiber insulation | 1% | Thermal performance reduction |
| Cellulose insulation | 15% | Settling, thermal degradation |
| Gypsum board | 1% | Mold growth potential |

**Moisture Storage Capacity:**

The amount of moisture a material can store affects transient behavior:

```
W_s = ρ × δ × V × φ
```

Where:
- W_s = stored moisture (lb or kg)
- ρ = material density (lb/ft³ or kg/m³)
- δ = moisture content change (dimensionless)
- V = material volume (ft³ or m³)
- φ = porosity (dimensionless)

## Seasonal Analysis

Interstitial condensation risk varies seasonally based on temperature gradients and interior humidity levels.

**Heating Season Analysis:**

- Vapor drive typically from warm interior to cold exterior
- Greatest condensation risk in coldest months
- Critical parameters: interior humidity, outdoor temperature, assembly design

**Cooling Season Analysis:**

- Vapor drive can reverse in air-conditioned buildings
- Moisture can condense on interior vapor retarders in humid climates
- Critical concern for exterior insulation and low-permeability cladding

**Monthly Moisture Balance:**

Track accumulation and drying:

```
M_net = Σ(M_acc,monthly - M_evap,monthly)
```

Design requirement: M_net ≤ M_critical at end of condensation season

**Climate-Specific Considerations:**

| Climate Zone | Primary Condensation Season | Vapor Retarder Location |
|--------------|----------------------------|------------------------|
| Cold (Zone 5-8) | Heating season | Interior (warm side) |
| Hot-Humid (Zone 1-2) | Cooling season | Not required or exterior |
| Mixed-Humid (Zone 3-4) | Both seasons | Class III or "smart" retarder |
| Marine (Zone 3-4C) | Heating season | Interior or Class III |

## Freeze-Thaw Cycles

When condensation occurs at temperatures below freezing, ice formation creates additional complications.

**Ice Formation Impacts:**

- Volume expansion (9% increase) causing physical damage
- Reduced drying potential (vapor pressure over ice is lower)
- Repeated freeze-thaw cycling accelerates material degradation

**Vapor Pressure Over Ice:**

Below freezing, use saturation pressure over ice rather than water:

```
P_sat,ice = P_sat,water × 0.95 (approximate at 25°F)
```

More precise relationship from Murphy-Koop equation:

```
ln(P_sat,ice) = 9.550426 - 5723.265/T + 3.53068 × ln(T) - 0.00728332 × T
```

Where T is in Kelvin and P is in Pa.

**Frost Plane Analysis:**

The frost plane location within an assembly:

```
d_frost = L × (T_i - T_freeze) / (T_i - T_o)
```

Where:
- d_frost = depth to frost plane from interior
- L = total assembly thickness
- T_freeze = 32°F (0°C)

This assumes linear temperature distribution (valid for homogeneous assemblies).

## Advanced Analysis Methods

### Transient Hygrothermal Modeling

For more accurate analysis, transient models account for:

- Moisture storage in materials
- Temperature-dependent properties
- Liquid and vapor transport
- Solar radiation effects
- Wind-driven rain

**Governing Equations:**

Heat transfer with moisture effects:

```
ρ_m × c_p × ∂T/∂t = ∇(k × ∇T) + L_v × ∂(ρ_v)/∂t
```

Moisture transfer:

```
∂w/∂t = ∇(D_w × ∇w) + δ_p × ∇(P_v)
```

Where:
- w = moisture content (kg/m³)
- D_w = liquid diffusivity (m²/s)
- δ_p = vapor permeability (kg/m·s·Pa)
- L_v = latent heat of vaporization

**Software Tools:**

- WUFI (Fraunhofer IBP)
- DELPHIN
- HygIRC (NRC Canada)
- BSim
- EnergyPlus with moisture modeling

### Moisture Reference Years

Analysis should use appropriate climate data:

- ASHRAE moisture design values (Chapter 14, Handbook of Fundamentals)
- Typical Meteorological Year (TMY3) data
- Moisture Reference Years (MoistRY) developed specifically for hygrothermal analysis

## Design Strategies for Prevention

### Vapor Retarder Placement

**Cold Climate Strategy:**

Place Class I or II vapor retarder on warm (interior) side:

- Reduces vapor drive into assembly
- Located where temperature remains above dew point
- Typical: polyethylene sheeting or vapor retarder paint

**Hot-Humid Climate Strategy:**

- Avoid interior vapor retarders
- Use permeable interior finishes
- May use exterior vapor retarders in some configurations

**Mixed Climate Strategy:**

- Use "smart" vapor retarders that adjust permeability with humidity
- Class III vapor retarders (1-10 perms)
- Vapor-permeable exterior sheathing and cladding

### Ventilation and Drainage

**Vented Assemblies:**

Roof and wall assemblies with ventilation cavities:

```
Q_vent = C_d × A × √(2 × ΔP / ρ)
```

Where:
- Q_vent = ventilation airflow (ft³/min)
- C_d = discharge coefficient (typically 0.6-0.65)
- A = vent opening area (ft²)
- ΔP = pressure difference (lbf/ft²)
- ρ = air density (lb/ft³)

Ventilation air must have adequate capacity to remove moisture:

```
g_removal = Q_vent × Δω × ρ
```

Where:
- Δω = humidity ratio difference between inlet and saturated air

### Thermal Bridging Mitigation

Thermal bridges create local cold spots where condensation risk increases:

**Linear Thermal Bridge:**

```
Ψ = Q / ΔT - Σ(U_i × A_i)
```

Where:
- Ψ = linear thermal transmittance (BTU/h·ft·°F)
- Q = total heat flow through assembly
- U_i, A_i = U-factor and area of clear-field sections

Continuous exterior insulation reduces thermal bridging and raises sheathing temperatures.

## Quality Control and Verification

### Construction Quality Requirements

Critical factors for preventing interstitial condensation:

1. **Vapor Retarder Continuity**
   - Seal all penetrations
   - Overlap joints minimum 6"
   - Seal to framing at perimeter

2. **Air Barrier Continuity**
   - More critical than vapor retarder
   - Test with blower door (≤ 3 ACH50 for residential)
   - Seal electrical boxes, plumbing penetrations

3. **Insulation Installation**
   - Fill all cavities completely
   - No gaps or voids
   - Contact with sheathing on exterior side

### Field Verification Methods

**Non-Destructive Testing:**

- Infrared thermography to identify thermal anomalies
- Moisture meters for spot checks
- Relative humidity sensors installed in assemblies
- Temperature sensors at critical interfaces

**Performance Monitoring:**

Install sensors at condensation-prone locations:

- Temperature: thermocouples or RTDs
- Relative humidity: capacitive RH sensors
- Moisture content: resistance-based wood moisture sensors

**Acceptance Criteria:**

- RH at condensation plane < 80% for extended periods
- No increasing moisture content trend over season
- Complete drying during evaporation season

## ASHRAE and Code References

**ASHRAE Standards:**

- **ASHRAE 160**: Criteria for Moisture-Control Design Analysis in Buildings
  - Establishes failure criteria based on surface RH and temperature
  - 30-day running average RH < 80% at surface T > 41°F
  - 7-day running average RH < 98% at surface T > 41°F

- **ASHRAE Handbook - Fundamentals, Chapter 25**: Heat, Air, and Moisture Control in Building Assemblies
  - Vapor retarder design
  - Material properties
  - Analysis procedures

- **ASHRAE Handbook - Fundamentals, Chapter 26**: Climatic Design Information
  - Design conditions including humidity
  - Climate classifications

**Building Codes:**

- **2021 IRC Section R702.7**: Vapor retarders
  - Class I, II, or III requirements by climate zone
  - Exceptions for specific assemblies

- **2021 IBC Section 1405.3**: Weather protection
  - Water-resistive barriers
  - Drainage requirements

**Other Standards:**

- **ISO 13788**: Hygrothermal performance of building components and building elements - Internal surface temperature to avoid critical surface humidity and interstitial condensation

- **ASTM E96**: Standard Test Methods for Water Vapor Transmission of Materials

- **ASTM C1371**: Standard Test Method for Determination of Emittance of Materials Near Room Temperature Using Portable Emissometers

## Example Calculation

**Given Wall Assembly (interior to exterior):**

1. Interior air film: R = 0.68
2. Gypsum board 1/2": R = 0.45, M = 50 perms
3. Polyethylene 6 mil: R = 0, M = 0.06 perms
4. Fiberglass batt 5.5": R = 19, M = 100 perms
5. OSB sheathing 1/2": R = 0.62, M = 0.7 perms
6. Exterior air film: R = 0.17

**Design Conditions:**

- Interior: 70°F, 40% RH
- Exterior: 0°F, 70% RH

**Step 1: Calculate Temperatures**

R_total = 20.92 ft²·h·°F/BTU

Temperature at interface 3 (behind polyethylene):
T₃ = 70 - (70 × 1.13 / 20.92) = 66.2°F

Temperature at interface 4 (behind insulation):
T₄ = 70 - (70 × 20.13 / 20.92) = 2.6°F

**Step 2: Calculate Vapor Pressures**

Interior: P_i = 0.40 × 0.363 = 0.145 psi (70°F, 40% RH)
Exterior: P_o = 0.70 × 0.038 = 0.027 psi (0°F, 70% RH)

Z_total = 1/50 + 1/0.06 + 1/100 + 1/0.7 = 18.12 perm⁻¹

Vapor pressure at interface 3:
P₃ = 0.145 - [(0.145 - 0.027) × (1/50) / 18.12] = 0.145 psi

Vapor pressure at interface 4:
P₄ = 0.145 - [(0.145 - 0.027) × (1/50 + 1/0.06) / 18.12] = 0.034 psi

**Step 3: Check for Condensation**

Saturation pressure at T₄ = 2.6°F: P_sat = 0.041 psi
Actual pressure at interface 4: P₄ = 0.034 psi

Since P₄ < P_sat, no condensation predicted at this interface under steady-state conditions.

**Conclusion:** The interior vapor retarder (polyethylene) is effective in preventing interstitial condensation in this cold climate application.

## Summary

Interstitial condensation analysis requires understanding vapor diffusion physics, temperature and vapor pressure profiles, and material properties. The dew point method and Glaser method provide steady-state approximations, while advanced hygrothermal modeling captures transient effects. Proper vapor retarder placement, construction quality, and seasonal analysis are essential for preventing moisture damage in building envelopes. Design strategies must account for climate zone, assembly configuration, and anticipated interior conditions to ensure long-term durability and performance.
