---
title: "Condensation Analysis"
weight: 4
description: "Quantitative methods for predicting surface and interstitial condensation in building assemblies including dewpoint calculations, Glaser method steady-state analysis, and dynamic hygrothermal modeling approaches."
---

# Condensation Analysis

Condensation occurs when moist air contacts surfaces below the dewpoint temperature or when vapor pressure exceeds saturation pressure within building assemblies. Condensation analysis predicts moisture accumulation locations, quantifies condensation rates, and verifies adequate drying potential to prevent long-term moisture damage.

## Dewpoint Temperature Fundamentals

The dewpoint temperature Td represents the temperature at which air becomes saturated (100% RH) at constant pressure. When surfaces drop below dewpoint, water vapor condenses on those surfaces.

### Dewpoint Calculation Methods

**Method 1: Psychrometric Chart**
Read dewpoint directly from chart at intersection of dry-bulb temperature and relative humidity lines.

**Method 2: Magnus-Tetens Formula** (accurate for -40°C to 50°C):

```
Td = (b × α(T,RH))/(a - α(T,RH))

where:
α(T,RH) = (a × T)/(b + T) + ln(RH/100)
a = 17.27
b = 237.7°C (for Td in °C)

For T in °F:
a = 17.27
b = 427.86°F
```

**Method 3: Partial Vapor Pressure Approach**:

```
First, calculate partial vapor pressure:
pv = RH × psat(T)

Then find dewpoint from inverse saturation equation:
Td = C2/(ln(C1/pv) + C3)

where:
C1 = 0.0866 (imperial units, psi)
C2 = 4030.18
C3 = 235
```

### Example Dewpoint Calculation

Interior conditions: 70°F, 40% RH

```
Step 1: Find saturation pressure at 70°F
psat(70°F) = 0.3631 psi (from steam tables)

Step 2: Calculate partial vapor pressure
pv = 0.40 × 0.3631 = 0.1452 psi

Step 3: Calculate dewpoint
Td = 4030.18/(ln(0.0866/0.1452) + 235)
Td = 4030.18/(−0.517 + 235) = 17.2°C = 45.0°F
```

Any surface below 45°F experiences condensation with these interior conditions.

## Surface Condensation

Surface condensation occurs on interior surfaces when surface temperature falls below dewpoint. High humidity, cold outdoor temperatures, and poor insulation create condensation risk.

### Surface Temperature Calculation

Interior surface temperature follows from heat transfer analysis:

```
Tsi = Ti - Q × Rsi

where:
Tsi = interior surface temperature (°F)
Ti = interior air temperature (°F)
Q = heat flux through assembly (Btu/hr·ft²)
Rsi = interior surface resistance (typically 0.68 hr·ft²·°F/Btu)
```

Heat flux through assembly:

```
Q = (Ti - To)/(Rtotal)

where:
To = outdoor temperature (°F)
Rtotal = total assembly R-value including surface resistances
```

Combining equations:

```
Tsi = Ti - ((Ti - To)/(Rtotal)) × Rsi
Tsi = Ti - (Ti - To) × (Rsi/Rtotal)
```

### Condensation Risk Factor

Temperature ratio TR quantifies condensation risk:

```
TR = (Tsi - To)/(Ti - To)

Higher TR indicates better performance (warmer interior surface)
TR > 0.70 generally prevents condensation for typical interior conditions
```

### Example Surface Condensation Analysis

Wall assembly:
- R-value: R-20 total (includes Rsi = 0.68, Rso = 0.17)
- Interior: 70°F, 40% RH (dewpoint = 45°F)
- Exterior: 10°F

```
Tsi = 70 - (70 - 10) × (0.68/20)
Tsi = 70 - 60 × 0.034 = 67.96°F
```

Surface temperature (67.96°F) exceeds dewpoint (45°F) - no condensation occurs.

For poorly insulated wall (R-5):
```
Tsi = 70 - (70 - 10) × (0.68/5)
Tsi = 70 - 8.16 = 61.84°F
```

Still no condensation, but closer to dewpoint with less safety margin.

### Thermal Bridge Condensation

Thermal bridges (studs, joists, shelf angles) locally reduce R-value, creating cold spots prone to condensation. 2D/3D heat transfer analysis or infrared thermography identifies bridge locations.

Temperature at thermal bridge:

```
Tbridge = Ti - (Ti - To) × (Rsi/Rbridge)

where Rbridge accounts for reduced insulation at framing member
```

Steel studs create severe thermal bridges (R-value ≈ R-5 at stud vs. R-20 at cavity), requiring thermal breaks or exterior insulation.

## Interstitial Condensation

Interstitial condensation occurs within building assemblies when vapor pressure exceeds saturation pressure at a given temperature plane. This hidden condensation accumulates in insulation cavities, degrading thermal performance and causing material decay.

### Temperature Profile Calculation

Temperature distribution through multilayer assembly follows from thermal resistance ratio:

```
T(x) = Ti - (Ti - To) × (ΣR(x)/Rtotal)

where:
T(x) = temperature at position x
ΣR(x) = cumulative R-value from interior to position x
Rtotal = total assembly R-value
```

For discrete layers:

```
Tn = Ti - (Ti - To) × ((Rsi + R1 + R2 + ... + Rn)/(Rtotal))
```

### Vapor Pressure Profile

Vapor pressure profile depends on boundary conditions and material permeances:

**Steady-state vapor flow**:
```
ṁ = (pv,i - pv,o)/(ΣZ)

where:
Z = vapor resistance = 1/μ (reperm)
ΣZ = Z1 + Z2 + ... + Zn
```

Vapor pressure at interface n:

```
pv,n = pv,i - ṁ × (Z1 + Z2 + ... + Zn)
```

### Condensation Location

Condensation occurs where vapor pressure exceeds saturation pressure:

```
If pv(x) > psat(T(x)) → condensation at location x
```

Condensation plane typically occurs:
- **Cold climates**: Within or at exterior face of insulation
- **Hot-humid climates**: At interior face of insulation
- **Mixed climates**: Seasonally variable location

### Example Interstitial Condensation Analysis

2×6 wall assembly (interior to exterior):
1. Gypsum board: 1/2 in., R-0.45, μ = 50 perm
2. Polyethylene vapor retarder: 6 mil, R-0, μ = 0.05 perm
3. Fiberglass insulation: 5-1/2 in., R-19, μ = 100 perm (air-permeable)
4. OSB sheathing: 1/2 in., R-0.62, μ = 2 perm
5. Housewrap: R-0, μ = 50 perm

Conditions:
- Interior: 70°F, 40% RH → pv,i = 0.145 psi
- Exterior: 20°F, 70% RH → pv,o = 0.021 psi

Total vapor resistance:
```
ΣZ = 1/50 + 1/0.05 + 1/100 + 1/2 + 1/50
ΣZ = 0.02 + 20.0 + 0.01 + 0.5 + 0.02 = 20.55 reperm
```

Vapor flow rate:
```
ṁ = (0.145 - 0.021)/20.55 = 0.00604 grain/(hr·ft²)
```

Vapor pressure at OSB interior face (after poly and insulation):
```
pv,osb = 0.145 - 0.00604 × (20.0 + 0.01) = 0.024 psi
```

Temperature at OSB interior face:
```
Rtotal = 0.68 + 0.45 + 19 + 0.62 + 0.17 = 20.92
R to OSB interior = 0.68 + 0.45 + 19 = 20.13

T_osb = 70 - (70 - 20) × (20.13/20.92) = 22.1°F
psat(22.1°F) = 0.046 psi
```

Since pv (0.024 psi) < psat (0.046 psi), **no condensation occurs** in this assembly despite the cold sheathing temperature.

The polyethylene vapor retarder (0.05 perm) effectively limits vapor flow to the cold sheathing.

## Glaser Method

The Glaser method provides simplified steady-state interstitial condensation analysis, comparing vapor pressure and saturation pressure profiles through assemblies.

### Glaser Procedure

1. **Calculate temperature profile** through assembly layers
2. **Calculate saturation vapor pressure** at each interface using psat(T)
3. **Calculate actual vapor pressure profile** based on boundary conditions and vapor resistances
4. **Identify condensation zones** where pv > psat
5. **Quantify condensation rate** in affected zones
6. **Calculate monthly accumulation/drying** to verify annual moisture balance

### Monthly Condensation Analysis

Condensation rate in affected layer:

```
ṁcond = A × [(pv,1 - psat) × μ1 + (psat - pv,2) × μ2]

where:
A = wall area (ft²)
pv,1 = vapor pressure entering layer
pv,2 = vapor pressure exiting layer
psat = saturation pressure at condensing plane
μ1, μ2 = permeances before and after condensing plane
```

Monthly accumulation:

```
Mmonth = ṁcond × hours_per_month
```

Annual moisture balance requires:

```
Σ(Mdrying months) ≥ Σ(Mwetting months)
```

### Glaser Method Limitations

The Glaser method assumes:
- Steady-state conditions (actual assemblies experience transient behavior)
- One-dimensional moisture flow (ignores lateral redistribution)
- No moisture storage in materials
- No air leakage
- No solar radiation effects
- No wind-driven rain

These limitations produce conservative predictions for vapor diffusion-driven condensation but miss dynamic phenomena captured by advanced hygrothermal modeling.

## Dynamic Hygrothermal Modeling

Advanced simulation tools (WUFI, MOISTURE-EXPERT, hygIRC) solve coupled heat and moisture transport equations with transient boundary conditions.

### Governing Equations

**Heat transfer**:
```
ρ × c × (∂T/∂t) = ∇·(λ∇T) + hv × ∇·(δp∇(φ × psat))

where:
ρ = density
c = specific heat
λ = thermal conductivity
hv = latent heat of evaporation
δp = vapor permeability
φ = relative humidity
```

**Moisture transfer**:
```
∂w/∂t = ∇·(Dw∇w + δp∇(φ × psat))

where:
w = moisture content
Dw = liquid diffusivity
```

### Model Inputs

**Material properties**:
- Thermal conductivity λ(w,T)
- Vapor permeability δ(w,T)
- Liquid diffusivity Dw(w)
- Moisture storage function w(φ)
- Sorption isotherms

**Boundary conditions**:
- Hourly weather data (temperature, RH, solar radiation, wind-driven rain)
- Interior temperature and humidity schedules
- Surface transfer coefficients

### Model Outputs

- Temperature and moisture content at each node over time
- Relative humidity profiles
- Condensation/evaporation rates
- Mold growth risk indicators
- Annual moisture balance

### Validation Requirements

ASHRAE Standard 160 specifies acceptance criteria:
- 30-day running average surface RH ≤ 80% at T > 41°F
- No sustained elevated moisture content in materials
- Adequate drying between wetting events

## Condensation Prevention Strategies

### Cold Climates

**Interior vapor retarder** (Class I or II) on warm side of insulation:
- Limits vapor flow to cold surfaces
- Prevents interstitial condensation in insulation
- Allows outward drying during summer

**Exterior insulation**:
- Warms sheathing temperature
- Reduces condensation risk
- Increases temperature ratio TR

### Hot-Humid Climates

**Avoid interior vapor retarders**:
- Interior cooling surfaces require inward drying capability
- Vapor-impermeable interior finishes trap moisture

**Exterior vapor control**:
- Low-perm exterior insulation (foil-faced polyiso)
- Limits inward vapor drive
- Interior must remain above dewpoint

### Mixed Climates

**Semi-permeable assemblies** (Class III vapor retarders):
- Allow bidirectional drying
- Avoid vapor-impermeable layers on either side
- Variable-permeance membranes adapt to seasonal conditions

## Measurement and Monitoring

**Surface temperature**: Infrared thermography identifies cold surfaces below dewpoint

**Interstitial conditions**: In-situ RH/temperature sensors monitor assembly performance

**Moisture content**: Pin-type or capacitance moisture meters detect elevated moisture in materials

**Mold inspection**: Visual examination during construction or renovation

## Related Topics

- [Dewpoint Temperature](./dew-point-temperature/) - Calculation methods and psychrometric relationships
- [Surface Condensation](./surface-condensation/) - Interior surface temperature analysis
- [Interstitial Condensation](./interstitial-condensation/) - Within-assembly moisture accumulation
- [Drying Potential](../drying-potential/) - Moisture removal capacity of assemblies

---

*Condensation analysis requires integrated thermal and moisture analysis to predict surface and interstitial condensation risk across seasonal operating conditions.*
