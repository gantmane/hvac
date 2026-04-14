---
title: "Psychrometric Calculations"
aliases: ["Psychrometric Calculations"]
description: "Comprehensive analysis of psychrometric calculation methods including perfect gas theory, partial pressure laws, and practical engineering equations for moist air properties"
weight: 5
---

## Overview

Psychrometric calculations quantify the thermodynamic properties of moist air using fundamental gas laws and empirical correlations. These calculations form the foundation for HVAC load analysis, equipment sizing, and system design. Accurate psychrometric calculations require understanding the behavior of dry air and water vapor as a binary gas mixture.

The complexity of psychrometric calculations ranges from simplified perfect gas approximations suitable for most HVAC applications (elevation < 6000 ft, temperature range 0-120°F) to high-precision formulations required for laboratory environments, specialized industrial processes, and rigorous research applications.

## Fundamental Gas Laws for Moist Air

### Perfect Gas Mixture Theory

Atmospheric air behaves as an ideal gas mixture within the temperature and pressure ranges encountered in HVAC applications. The perfect gas law applies to both the dry air component and the water vapor component:

**Dry Air:**
```
pₐV = nₐRₐT
```

**Water Vapor:**
```
pᵥV = nᵥRᵥT
```

Where:
- p = partial pressure (psi or Pa)
- V = volume (ft³ or m³)
- n = number of moles (lbmol or kmol)
- R = specific gas constant (ft·lbf/lbm·°R or J/kg·K)
- T = absolute temperature (°R or K)

**Gas Constants:**

| Component | IP Units | SI Units |
|-----------|----------|----------|
| Dry Air (Rₐ) | 53.352 ft·lbf/lbm·°R | 287.042 J/kg·K |
| Water Vapor (Rᵥ) | 85.778 ft·lbf/lbm·°R | 461.520 J/kg·K |
| Universal Gas Constant (R̄) | 1545.35 ft·lbf/lbmol·°R | 8314.472 J/kmol·K |

The ratio of molecular masses determines the relationship between dry air and water vapor properties:

```
Rₐ/Rᵥ = Mᵥ/Mₐ = 18.015/28.966 = 0.62198
```

This ratio appears throughout psychrometric equations as the constant 0.622.

### Dalton's Law of Partial Pressures

Dalton's Law states that the total pressure of a gas mixture equals the sum of the partial pressures of the constituent gases:

```
p = pₐ + pᵥ
```

Where:
- p = total atmospheric pressure (barometric pressure)
- pₐ = partial pressure of dry air
- pᵥ = partial pressure of water vapor

At standard atmospheric conditions (sea level):
- p = 14.696 psia (101.325 kPa)
- pᵥ typically ranges from 0.09 to 0.95 psia (0.6 to 6.5 kPa)
- pₐ = p - pᵥ ≈ 13.7 to 14.6 psia (95 to 100.7 kPa)

**Altitude Correction:**

Atmospheric pressure decreases with elevation according to:

```
p = 14.696 × [1 - 6.8754×10⁻⁶ × h]⁵·²⁵⁵⁹  (IP units, h in feet)
p = 101.325 × [1 - 2.25577×10⁻⁵ × h]⁵·²⁵⁵⁹  (SI units, h in meters)
```

| Elevation (ft) | Pressure (psia) | Elevation (m) | Pressure (kPa) |
|----------------|-----------------|---------------|----------------|
| 0 (Sea Level) | 14.696 | 0 | 101.325 |
| 1000 | 14.175 | 305 | 97.717 |
| 2500 | 13.429 | 762 | 92.592 |
| 5000 | 12.228 | 1524 | 84.330 |
| 7500 | 11.104 | 2286 | 76.564 |
| 10000 | 10.108 | 3048 | 69.682 |

### Gibbs-Dalton Law

The Gibbs-Dalton Law states that each component of a gas mixture behaves as if it alone occupies the entire volume at the mixture temperature. This principle allows calculation of individual component properties:

**Internal Energy:**
```
U = Uₐ + Uᵥ
```

**Enthalpy:**
```
H = Hₐ + Hᵥ
```

**Entropy:**
```
S = Sₐ + Sᵥ
```

For psychrometric calculations, the specific enthalpy of moist air per unit mass of dry air:

```
h = hₐ + W × hᵥ
```

Where:
- h = specific enthalpy of moist air (Btu/lbₐ or kJ/kgₐ)
- hₐ = specific enthalpy of dry air (Btu/lbₐ or kJ/kgₐ)
- W = humidity ratio (lbᵥ/lbₐ or kgᵥ/kgₐ)
- hᵥ = specific enthalpy of water vapor (Btu/lbᵥ or kJ/kgᵥ)

### Amagat's Law (Additive Volumes)

Amagat's Law states that the total volume of a gas mixture equals the sum of the partial volumes at constant temperature and pressure:

```
V = Vₐ + Vᵥ
```

This law is particularly useful for calculating specific volume of moist air:

```
v = Vₐ/mₐ = RₐT/pₐ
```

For practical calculations at atmospheric pressure:

```
v = 0.370486 × T/pₐ  (IP units: ft³/lbₐ, T in °R, pₐ in psia)
v = 0.287042 × T/pₐ  (SI units: m³/kgₐ, T in K, pₐ in kPa)
```

## Water Vapor Saturation Relationships

### Saturation Pressure Equations

The saturation pressure of water vapor is the maximum partial pressure that can exist at a given temperature. Exceeding this pressure results in condensation.

#### Carrier Equation (1911)

The Carrier equation provides reasonable accuracy for HVAC applications from -40°F to 250°F:

**For water (above 32°F):**
```
pws = exp[C₁/T + C₂ + C₃T + C₄T² + C₅T³ + C₆ln(T)]
```

**For ice (below 32°F):**
```
pwsi = exp[C₇/T + C₈ + C₉T + C₁₀T² + C₁₁T³ + C₁₂ln(T)]
```

Where T is in absolute temperature (°R or K).

**Simplified Carrier Equation (Traditional HVAC Use):**

For temperatures above freezing in IP units:

```
pws = exp[23.7093 - 4111/(tdb + 459.67)]  (tdb in °F, pws in psia)
```

This simplified form is accurate within ±2% from 32°F to 100°F.

#### Hyland-Wexler Equations (1983)

The Hyland-Wexler equations, adopted by ASHRAE, provide high accuracy (±0.01%) from -148°F to 392°F:

**For water (above 32°F/0°C):**
```
ln(pws) = C₁/T + C₂ + C₃T + C₄T² + C₅T³ + C₆ln(T)
```

**SI Units Coefficients:**
- C₁ = -5.8002206×10³
- C₂ = 1.3914993
- C₃ = -4.8640239×10⁻²
- C₄ = 4.1764768×10⁻⁵
- C₅ = -1.4452093×10⁻⁸
- C₆ = 6.5459673

Valid range: 273.15 K to 473.15 K (0°C to 200°C)

**For ice (below 32°F/0°C):**
```
ln(pwsi) = C₇/T + C₈ + C₉T + C₁₀T² + C₁₁T³ + C₁₂ln(T)
```

**SI Units Coefficients:**
- C₇ = -5.6745359×10³
- C₈ = 6.3925247
- C₉ = -9.6778430×10⁻³
- C₁₀ = 6.2215701×10⁻⁷
- C₁₁ = 2.0747825×10⁻⁹
- C₁₂ = -9.4840240×10⁻¹³
- C₁₃ = 4.1635019

Valid range: 173.15 K to 273.15 K (-100°C to 0°C)

The Hyland-Wexler equations are recommended for:
- High-precision laboratory applications
- Computer-based psychrometric calculations
- Research and development work
- Specialized industrial processes

#### Ferrel Equation (Empirical)

An empirical correlation useful for quick manual calculations:

```
log₁₀(pws) = A - B/(tdb + C)
```

**IP Units (tdb in °F, pws in in. Hg):**
- A = 6.1155
- B = 814.35
- C = 329.94

**Accuracy:** ±5% from 32°F to 100°F

**Example calculation at 75°F:**
```
log₁₀(pws) = 6.1155 - 814.35/(75 + 329.94)
log₁₀(pws) = 6.1155 - 2.0103 = 4.1052
pws = 10⁴·¹⁰⁵² = 12,751
pws = 0.8805 in. Hg = 0.433 psia
```

### Degree of Saturation

Degree of saturation (μ) represents the ratio of actual humidity ratio to saturation humidity ratio:

```
μ = W/Ws = (pᵥ/pws) × [(p - pws)/(p - pᵥ)]
```

For most HVAC applications where pᵥ << p:

```
μ ≈ pᵥ/pws = φ (relative humidity)
```

However, at high humidity levels or reduced pressures, the full equation provides more accurate results.

## Psychrometric Property Calculations

### Humidity Ratio

Humidity ratio (W) is the mass of water vapor per unit mass of dry air:

```
W = 0.62198 × pᵥ/(p - pᵥ)  (lbᵥ/lbₐ or kgᵥ/kgₐ)
```

**Alternative form:**
```
W = 0.62198 × φ × pws/(p - φ × pws)
```

**Typical ranges:**

| Condition | W (grains/lbₐ) | W (lbᵥ/lbₐ) | W (g/kgₐ) |
|-----------|-----------------|-------------|-----------|
| Very dry (desert) | 20-30 | 0.0029-0.0043 | 2.9-4.3 |
| Comfortable indoor | 50-70 | 0.0071-0.0100 | 7.1-10.0 |
| Humid (coastal) | 90-120 | 0.0129-0.0171 | 12.9-17.1 |
| Tropical | 130-180 | 0.0186-0.0257 | 18.6-25.7 |

Note: 7000 grains = 1 lbₐ

### Relative Humidity

Relative humidity (φ) is the ratio of actual water vapor pressure to saturation pressure:

```
φ = pᵥ/pws = (W/Ws) × [(p - pws)/(p - W × pws/0.62198)]
```

**Simplified (for most HVAC applications):**
```
φ = W/Ws × (p - pws)/p
```

**From dry-bulb and wet-bulb temperatures:**
```
φ = (Ws' - (p/(0.62198 × pws)) × (W - W'))/Ws

Where:
W = [(1093 - 0.556 × twb) × W' - 0.240 × (tdb - twb)]/(1093 + 0.444 × tdb - twb)  (IP)
```

For practical psychrometric chart use, the simpler approximation:

```
W ≈ Ws' - (tdb - twb)/[2800 - 1.3 × twb]  (IP units, approximate)
```

### Dew Point Temperature

Dew point temperature (tdp) is the temperature at which condensation begins when air is cooled at constant pressure and humidity ratio.

At dew point: pᵥ = pws(tdp)

**Calculation procedure:**
1. Calculate pᵥ from W or φ
2. Use inverse saturation equation to find tdp

**Approximate inverse equation:**
```
tdp = C - D/[ln(pᵥ) - A]  (°F)

Where:
A = 23.7093
C = 459.67
D = 4111
```

**Example for W = 0.010 lbᵥ/lbₐ at p = 14.696 psia:**
```
pᵥ = W × p/(0.62198 + W)
pᵥ = 0.010 × 14.696/(0.62198 + 0.010) = 0.2326 psia

tdp = 459.67 - 4111/[ln(0.2326) - 23.7093]
tdp = 459.67 - 4111/(-1.456 - 23.709)
tdp = 459.67 - 163.5 = 54.5°F
```

### Wet-Bulb Temperature

Wet-bulb temperature (twb) is the equilibrium temperature achieved by a water surface evaporating into moving air. It requires iterative solution of the energy balance equation.

**Psychrometric wet-bulb equation:**
```
W = [(hfg)s' × W' - cp(tdb - twb)]/(hfg)

Where:
(hfg)s' = enthalpy of vaporization at twb
W' = humidity ratio at saturation at twb
cp = specific heat of moist air
```

**Simplified iteration method:**

Starting with twb guess = tdb - 5°F:

1. Calculate W' at twb: W' = 0.62198 × pws(twb)/(p - pws(twb))
2. Calculate W from: W = W' - (tdb - twb)/(1220 - twb)
3. Compare to known W; adjust twb and repeat

Convergence typically achieved in 3-5 iterations with ±0.1°F tolerance.

**Wet-bulb depression:**
The difference (tdb - twb) increases with decreasing relative humidity:

| RH (%) | Typical Depression at 75°F |
|--------|---------------------------|
| 90 | 1-2°F |
| 70 | 3-5°F |
| 50 | 6-9°F |
| 30 | 11-15°F |
| 10 | 20-25°F |

### Specific Enthalpy

Specific enthalpy of moist air per unit mass of dry air:

```
h = cpₐ × tdb + W × (hfg0 + cpᵥ × tdb)
```

Where:
- cpₐ = 0.240 Btu/lbₐ·°F (1.006 kJ/kgₐ·K) - specific heat of dry air
- cpᵥ = 0.444 Btu/lbᵥ·°F (1.86 kJ/kgᵥ·K) - specific heat of water vapor
- hfg0 = 1061 Btu/lbₐ (2501 kJ/kgₐ) - latent heat at 0°F (0°C)

**Simplified form (IP units, tdb in °F, h in Btu/lbₐ):**
```
h = 0.240 × tdb + W × (1061 + 0.444 × tdb)
```

**SI units (tdb in °C, h in kJ/kgₐ):**
```
h = 1.006 × tdb + W × (2501 + 1.86 × tdb)
```

**Sensible and latent components:**
```
hsensible = 0.240 × tdb
hlatent = W × (1061 + 0.444 × tdb)
```

### Specific Volume

Specific volume of moist air per unit mass of dry air:

```
v = Rₐ × T/(p - pᵥ) = Rₐ × T × (1 + 1.6078 × W)/p
```

**IP units (v in ft³/lbₐ, T in °R, p in psia):**
```
v = 0.370486 × T × (1 + 1.6078 × W)/p
```

**SI units (v in m³/kgₐ, T in K, p in kPa):**
```
v = 0.287042 × T × (1 + 1.6078 × W)/p
```

**Standard conditions (70°F, 50% RH, sea level):**
```
v ≈ 13.33 ft³/lbₐ (0.832 m³/kgₐ)
```

**Temperature effect on density:**

For constant W and p, density changes approximately 0.2% per °F (0.36% per °C).

| Temperature | Specific Volume (ft³/lbₐ) | Density (lbₐ/ft³) |
|-------------|---------------------------|-------------------|
| 0°F | 11.86 | 0.0843 |
| 32°F | 12.65 | 0.0791 |
| 70°F | 13.33 | 0.0750 |
| 100°F | 14.42 | 0.0694 |
| 130°F | 15.18 | 0.0659 |

## Engineering Calculation Examples

### Example 1: Complete Psychrometric State

Given: tdb = 75°F, φ = 60%, p = 14.696 psia

**Step 1: Saturation pressure at 75°F**
```
pws = exp[23.7093 - 4111/(75 + 459.67)]
pws = exp[23.7093 - 7.6886] = exp[16.0207]
pws = 0.4306 psia
```

**Step 2: Vapor pressure**
```
pᵥ = φ × pws = 0.60 × 0.4306 = 0.2584 psia
```

**Step 3: Humidity ratio**
```
W = 0.62198 × 0.2584/(14.696 - 0.2584)
W = 0.62198 × 0.01790 = 0.01114 lbᵥ/lbₐ
W = 77.98 grains/lbₐ
```

**Step 4: Specific enthalpy**
```
h = 0.240 × 75 + 0.01114 × (1061 + 0.444 × 75)
h = 18.0 + 0.01114 × 1094.3
h = 18.0 + 12.19 = 30.19 Btu/lbₐ
```

**Step 5: Specific volume**
```
v = 0.370486 × 534.67 × (1 + 1.6078 × 0.01114)/14.696
v = 0.370486 × 534.67 × 1.0179/14.696
v = 13.73 ft³/lbₐ
```

**Step 6: Dew point temperature**
```
tdp = 459.67 - 4111/[ln(0.2584) - 23.7093]
tdp = 459.67 - 4111/(-1.354 - 23.709)
tdp = 459.67 - 164.0 = 59.1°F
```

### Example 2: Cooling Coil Process

Given:
- Entering air: tdb1 = 85°F, twb1 = 68°F
- Leaving air: tdb2 = 55°F, φ2 = 90%
- Airflow: 10,000 cfm at entering conditions
- Atmospheric pressure: 14.696 psia

**Entering air properties:**

From entering conditions, determine W1 (requires iteration or chart):
```
W1 ≈ 0.0138 lbᵥ/lbₐ (from psychrometric chart)
h1 = 0.240 × 85 + 0.0138 × (1061 + 0.444 × 85)
h1 = 20.4 + 15.1 = 35.5 Btu/lbₐ
v1 = 0.370486 × 544.67 × 1.0222/14.696 = 14.09 ft³/lbₐ
```

**Leaving air properties:**

Saturation at 55°F:
```
pws = exp[23.7093 - 4111/(55 + 459.67)] = 0.2141 psia
pᵥ2 = 0.90 × 0.2141 = 0.1927 psia
W2 = 0.62198 × 0.1927/(14.696 - 0.1927) = 0.00826 lbᵥ/lbₐ
h2 = 0.240 × 55 + 0.00826 × (1061 + 0.444 × 55)
h2 = 13.2 + 9.0 = 22.2 Btu/lbₐ
```

**Mass flow rate:**
```
ṁₐ = Q/v1 = 10,000/14.09 = 709.8 lbₐ/min = 42,588 lbₐ/hr
```

**Total cooling capacity:**
```
Q̇total = ṁₐ × (h1 - h2)
Q̇total = 42,588 × (35.5 - 22.2) = 566,420 Btu/hr
Q̇total = 47.2 tons
```

**Sensible cooling:**
```
Q̇sensible = ṁₐ × cpₐ × (tdb1 - tdb2)
Q̇sensible = 42,588 × 0.240 × (85 - 55) = 306,634 Btu/hr
Q̇sensible = 25.6 tons
```

**Latent cooling:**
```
Q̇latent = ṁₐ × hfg × (W1 - W2)
Q̇latent = 42,588 × 1061 × (0.0138 - 0.00826)
Q̇latent = 42,588 × 1061 × 0.00554 = 250,406 Btu/hr
Q̇latent = 20.9 tons
```

**Sensible heat ratio:**
```
SHR = Q̇sensible/Q̇total = 306,634/566,420 = 0.541
```

**Condensate removal rate:**
```
ṁcondensate = ṁₐ × (W1 - W2)
ṁcondensate = 42,588 × (0.0138 - 0.00826)
ṁcondensate = 235.9 lbᵥ/hr = 28.3 gallons/hr
```

### Example 3: Mixing of Two Airstreams

Given:
- Stream 1 (outdoor air): 10,000 cfm at 95°F DB, 75°F WB
- Stream 2 (return air): 30,000 cfm at 75°F DB, 62°F WB
- Pressure: 14.696 psia

**Stream 1 properties:**
```
W1 = 0.0153 lbᵥ/lbₐ (from chart or calculation)
h1 = 0.240 × 95 + 0.0153 × (1061 + 0.444 × 95) = 39.6 Btu/lbₐ
v1 = 14.35 ft³/lbₐ
ṁ1 = 10,000/14.35 = 697 lbₐ/min
```

**Stream 2 properties:**
```
W2 = 0.0091 lbᵥ/lbₐ
h2 = 0.240 × 75 + 0.0091 × (1061 + 0.444 × 75) = 27.9 Btu/lbₐ
v2 = 13.68 ft³/lbₐ
ṁ2 = 30,000/13.68 = 2193 lbₐ/min
```

**Mixed air properties:**
```
ṁ3 = ṁ1 + ṁ2 = 697 + 2193 = 2890 lbₐ/min

Mass fraction: x1 = 697/2890 = 0.241

h3 = x1 × h1 + (1 - x1) × h2
h3 = 0.241 × 39.6 + 0.759 × 27.9 = 30.7 Btu/lbₐ

W3 = x1 × W1 + (1 - x1) × W2
W3 = 0.241 × 0.0153 + 0.759 × 0.0091 = 0.0106 lbᵥ/lbₐ

tdb3 = (h3 - W3 × 1061)/(0.240 + W3 × 0.444)
tdb3 = (30.7 - 0.0106 × 1061)/(0.240 + 0.0106 × 0.444)
tdb3 = 19.46/0.245 = 79.4°F
```

## Design Considerations

### Calculation Accuracy Requirements

| Application | Required Accuracy | Recommended Method |
|-------------|------------------|-------------------|
| Comfort cooling/heating | ±2% | Simplified Carrier equation |
| Laboratory HVAC | ±0.5% | Hyland-Wexler equations |
| Industrial process | ±1% | ASHRAE algorithms |
| Energy modeling | ±2-3% | Psychrometric chart |
| Research | ±0.1% | High-precision formulations |

### Software Implementation

Modern psychrometric calculations are typically performed using:

1. **ASHRAE Psychrometric Chart Software** - Based on Hyland-Wexler equations
2. **EES (Engineering Equation Solver)** - High-precision property database
3. **Custom spreadsheets** - Using simplified equations for specific applications
4. **Building simulation software** - Integrated psychrometric routines

### Iterative Solution Techniques

Several psychrometric properties require iterative solution:

**Wet-bulb temperature calculation:**
- Newton-Raphson method: typically 3-5 iterations
- Bisection method: 8-12 iterations but guaranteed convergence
- Convergence criterion: |twb,n+1 - twb,n| < 0.05°F

**Relative humidity from enthalpy and dry-bulb:**
- Requires simultaneous solution of h and W equations
- Successive substitution or Newton's method
- Convergence criterion: |φn+1 - φn| < 0.001

### ASHRAE Standard References

**ASHRAE Handbook - Fundamentals:**
- Chapter 1: Psychrometrics (comprehensive equations and properties)
- Table 2: Thermodynamic properties of moist air (extensive tabulations)
- Chapter 18: Load calculation principles

**ASHRAE Standards:**
- ASHRAE Standard 55: Thermal comfort conditions
- ASHRAE Standard 62.1: Ventilation rate calculations require psychrometric analysis
- ASHRAE Standard 90.1: Energy calculations use psychrometric processes

### Common Calculation Errors

1. **Mixing atmospheric and gauge pressure** - Always use absolute pressure
2. **Incorrect temperature scale** - Verify °F vs °R or °C vs K
3. **Altitude neglect** - Pressure correction essential above 2000 ft
4. **Saturation assumptions** - Air leaving cooling coils may not be saturated
5. **Condensate energy** - Often neglected in coil capacity calculations
6. **Fan heat addition** - Typically 0.5-1.5°F temperature rise

### Practical Calculation Tips

**Quick estimate of humidity ratio from RH:**
```
W ≈ φ × Ws (accurate within 5% for φ < 80%)
```

**Approximate wet-bulb depression:**
```
tdb - twb ≈ (100 - RH)/3  (°F, rough estimate)
```

**Sensible heat factor (SHF) line slope on chart:**
```
Slope = Δh/ΔW = Q̇sensible/Q̇latent × 4840  (IP units)
```

**Coil apparatus dew point (ADP):**
```
ADP ≈ twb,leaving - 2 to 5°F (depending on coil bypass factor)
```

## Advanced Computational Methods

### Enthalpy-Humidity Chart Calculations

The h-W (Mollier) diagram provides direct visualization of HVAC processes:

**Chart characteristics:**
- Horizontal axis: Humidity ratio (W)
- Vertical axis: Enthalpy (h)
- Constant dry-bulb lines: slope = cpₐ + W × cpᵥ
- Constant relative humidity curves
- Constant wet-bulb lines: approximately straight at 45° angle

**Process line equations:**

Sensible heating/cooling (W = constant):
```
Δh/Δtdb = 0.240 + W × 0.444
```

Humidification at constant dry-bulb:
```
Δh/ΔW = hfg + cpᵥ × tdb
```

### Numerical Integration for Complex Processes

For non-linear processes (e.g., evaporative cooling with varying effectiveness):

```
h(x) = h₀ + ∫₀ˣ [q̇sens(ξ) + q̇lat(ξ)] dξ
```

Numerical methods:
- Trapezoidal rule for moderate accuracy
- Simpson's rule for higher precision
- Runge-Kutta for coupled differential equations

## Conclusion

Psychrometric calculations form the quantitative foundation for HVAC system analysis and design. Selection of appropriate calculation methods depends on required accuracy, application constraints, and available computational tools. For routine design work, simplified equations provide adequate precision. Critical applications require high-accuracy formulations such as Hyland-Wexler equations.

Proper application of psychrometric principles ensures accurate load calculations, appropriate equipment selection, and verification of system performance. Understanding the underlying physics and mathematical relationships enables engineers to troubleshoot complex problems and optimize HVAC system designs.
