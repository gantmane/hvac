---
title: "Specific Heat of Air"
description: "Comprehensive analysis of air specific heat properties including cp and cv values, temperature dependencies, thermodynamic relationships, and application to HVAC load calculations and system design"
weight: 3
---

## Technical Overview

Specific heat represents the amount of thermal energy required to raise the temperature of a unit mass of air by one degree. For HVAC applications, air exhibits two distinct specific heat values depending on the thermodynamic process:

**Specific heat at constant pressure (cp)**: Energy required to raise air temperature when pressure remains constant, as occurs in most HVAC air handling processes.

**Specific heat at constant volume (cv)**: Energy required to raise air temperature in a rigid container where volume cannot change.

The distinction between these values arises from the work energy required during expansion. When air is heated at constant pressure, it expands and performs work against atmospheric pressure. This expansion work requires additional energy beyond that needed to raise the internal temperature, making cp larger than cv.

## Standard Values for Dry Air

At standard HVAC reference conditions (20°C, 101.325 kPa):

| Property | Value (SI) | Value (I-P) | Notes |
|----------|-----------|-------------|-------|
| cp | 1.006 kJ/(kg·K) | 0.240 Btu/(lbm·°F) | Constant pressure |
| cv | 0.718 kJ/(kg·K) | 0.171 Btu/(lbm·°F) | Constant volume |
| cp - cv | 0.287 kJ/(kg·K) | 0.069 Btu/(lbm·°F) | Equals R/M |
| Specific heat ratio (γ) | 1.400 | 1.400 | cp/cv |

The difference between cp and cv equals the specific gas constant for air (R/M = 0.287 kJ/(kg·K)), a relationship derived from fundamental thermodynamic principles.

## Thermodynamic Relationships

### Specific Heat Ratio

The ratio of specific heats (γ = cp/cv) appears in numerous HVAC calculations:

γ = cp/cv = 1.400 (for dry air near standard conditions)

This ratio governs:
- Isentropic compression and expansion processes in compressors
- Sound speed in air: c = √(γRT)
- Pressure-temperature relationships during adiabatic processes
- Acoustic performance of duct systems

### Mayer's Relation

For ideal gases, the relationship between the two specific heats is:

cp - cv = R

Where R is the specific gas constant for air (287 J/(kg·K) or 53.35 ft·lbf/(lbm·°R)).

This relationship confirms that cp must always exceed cv by a fixed amount for ideal gas behavior.

### Enthalpy and Internal Energy

The two specific heat values relate to different thermodynamic properties:

- cp relates to enthalpy change: Δh = cp·ΔT
- cv relates to internal energy change: Δu = cv·ΔT

For HVAC applications at constant atmospheric pressure, enthalpy-based calculations using cp are standard practice.

## Temperature Dependence

While often treated as constant, specific heat values exhibit slight temperature dependence:

### Dry Air Specific Heat vs. Temperature

| Temperature | cp | cv | γ |
|-------------|-------|-------|-------|
| °C (°F) | kJ/(kg·K) | kJ/(kg·K) | - |
| -40 (-40) | 1.0045 | 0.7175 | 1.401 |
| -20 (-4) | 1.0049 | 0.7179 | 1.400 |
| 0 (32) | 1.0054 | 0.7184 | 1.400 |
| 20 (68) | 1.0061 | 0.7191 | 1.399 |
| 40 (104) | 1.0068 | 0.7198 | 1.399 |
| 60 (140) | 1.0076 | 0.7206 | 1.398 |
| 80 (176) | 1.0084 | 0.7214 | 1.398 |
| 100 (212) | 1.0093 | 0.7223 | 1.397 |
| 150 (302) | 1.0119 | 0.7249 | 1.396 |
| 200 (392) | 1.0146 | 0.7276 | 1.394 |

For standard HVAC temperature ranges (-20°C to 50°C or -4°F to 122°F), the variation in cp is less than 0.2%, justifying the use of constant values in most calculations.

### Temperature Correction Factors

When extreme accuracy is required across wide temperature ranges, use polynomial approximations:

**SI Units (T in K):**
```
cp(T) = 1.045356 - 3.161783×10⁻⁴·T + 7.083814×10⁻⁷·T² - 2.705209×10⁻¹⁰·T³
```

**I-P Units (T in °R):**
```
cp(T) = 0.2196 + 1.25×10⁻⁵·T - 1.47×10⁻⁹·T²
```

These equations provide accuracy within 0.1% from -50°C to 300°C (-58°F to 572°F).

## Moist Air Considerations

Real HVAC systems handle moist air, requiring adjustment of specific heat values:

### Moist Air Specific Heat

cp,ma = cp,da + W·cp,v

Where:
- cp,ma = specific heat of moist air mixture [kJ/(kg·K)]
- cp,da = specific heat of dry air = 1.006 kJ/(kg·K)
- W = humidity ratio [kg water/kg dry air]
- cp,v = specific heat of water vapor = 1.86 kJ/(kg·K)

### Typical Moist Air Values

| Condition | Humidity Ratio | cp,ma | Difference |
|-----------|----------------|--------|-----------|
|  | kg/kg | kJ/(kg·K) | % increase |
| Dry air | 0.0000 | 1.006 | 0.0% |
| 30% RH at 20°C | 0.0044 | 1.014 | 0.8% |
| 50% RH at 20°C | 0.0073 | 1.021 | 1.5% |
| 70% RH at 20°C | 0.0103 | 1.028 | 2.2% |
| 90% RH at 20°C | 0.0132 | 1.035 | 2.9% |
| Saturated at 30°C | 0.0273 | 1.057 | 5.1% |

The moisture content increases effective specific heat, impacting sensible heat calculations by 1-3% under typical conditions and up to 5% in hot, humid environments.

## HVAC Load Calculation Applications

### Sensible Heat Transfer

The fundamental equation for sensible heating or cooling:

**Mass flow basis:**
Q = ṁ·cp·ΔT

**Volumetric flow basis:**
Q = ρ·V̇·cp·ΔT

Where:
- Q = sensible heat transfer rate [kW or Btu/hr]
- ṁ = mass flow rate [kg/s or lbm/hr]
- V̇ = volumetric flow rate [m³/s or cfm]
- ρ = air density [kg/m³ or lbm/ft³]
- cp = specific heat at constant pressure
- ΔT = temperature difference [K or °F]

### Practical HVAC Equations

**SI Units:**
```
Q (kW) = ṁ (kg/s) × 1.006 (kJ/(kg·K)) × ΔT (K)
Q (kW) = V̇ (m³/s) × 1.20 (kg/m³) × 1.006 (kJ/(kg·K)) × ΔT (K)
Q (kW) = 1.21 × V̇ (m³/s) × ΔT (K)
```

**I-P Units:**
```
Q (Btu/hr) = ṁ (lbm/hr) × 0.240 (Btu/(lbm·°F)) × ΔT (°F)
Q (Btu/hr) = V̇ (cfm) × 60 × 0.075 (lbm/ft³) × 0.240 (Btu/(lbm·°F)) × ΔT (°F)
Q (Btu/hr) = 1.08 × V̇ (cfm) × ΔT (°F)
```

The factor 1.08 in I-P units and 1.21 in SI units incorporates standard air density and specific heat.

### Adjustment for Altitude and Temperature

Standard factors (1.08 Btu/(hr·cfm·°F) and 1.21 kW/(m³/s·K)) assume:
- Sea level pressure (101.325 kPa or 14.696 psia)
- Standard air density (1.20 kg/m³ or 0.075 lbm/ft³)

**Altitude correction:**
The actual factor at elevation:

Factor(z) = Factor(sea level) × (ρ(z)/ρ(sea level))

| Elevation | Pressure Ratio | Factor (I-P) | Factor (SI) |
|-----------|----------------|--------------|-------------|
| ft (m) | - | Btu/(hr·cfm·°F) | kW/(m³/s·K) |
| 0 (0) | 1.000 | 1.080 | 1.210 |
| 2500 (762) | 0.917 | 0.991 | 1.110 |
| 5000 (1524) | 0.843 | 0.910 | 1.020 |
| 7500 (2286) | 0.776 | 0.838 | 0.939 |
| 10000 (3048) | 0.716 | 0.773 | 0.866 |

Failure to correct for altitude results in oversized equipment and excessive energy consumption.

## Design Considerations

### Constant Pressure Assumption

HVAC air-side calculations universally employ cp because:

1. Air handling occurs at approximately constant atmospheric pressure
2. Pressure variations in ductwork (typically 500-2500 Pa or 2-10 in. w.g.) represent less than 3% of absolute pressure
3. The thermodynamic process follows an isobaric path on a psychrometric chart

The constant volume specific heat (cv) applies primarily to theoretical thermodynamic analysis and rigid container scenarios rarely encountered in HVAC practice.

### Accuracy Requirements

**Standard calculations (±5% accuracy):**
- Use cp = 1.006 kJ/(kg·K) or 0.24 Btu/(lbm·°F)
- Apply standard density factors (1.08 or 1.21)
- Acceptable for typical comfort HVAC and general load estimates

**Precision calculations (±1% accuracy):**
- Account for moist air effects using actual humidity ratio
- Apply altitude corrections for elevations above 500 m (1500 ft)
- Consider temperature-dependent specific heat for processes exceeding 50 K (90°F) temperature change
- Required for critical applications, calibration standards, and energy modeling

### Heat Exchanger Performance

In air-to-air heat recovery and heat exchanger analysis:

**Effectiveness calculations:**
ε = (ṁc·cp)min × ΔTactual / (ṁc·cp)min × ΔTmax

The (ṁc·cp) term represents heat capacity rate, fundamental to heat exchanger effectiveness-NTU methods.

**NTU (Number of Transfer Units):**
NTU = UA / (ṁc·cp)min

Where UA is the overall heat transfer coefficient times area.

Specific heat appears in both effectiveness and NTU, making accurate values essential for heat recovery equipment sizing.

### Stratification and Mixing

In large spaces, specific heat governs the energy required to overcome thermal stratification:

Q_mixing = ṁ_recirculation × cp × (T_ceiling - T_occupied)

Destratification fan sizing requires accurate specific heat values combined with measured temperature differentials.

## Psychrometric Process Applications

### Sensible Heating

Pure sensible heating (horizontal line on psychrometric chart):

ΔH_sensible = cp × ΔT = 1.006 × ΔT (kJ/kg dry air)

The specific heat determines the slope of the sensible heating process line and the energy input required.

### Bypass Factor Calculations

When cooling coils provide both sensible and latent cooling, the apparatus dew point and bypass factor relate through specific heat:

SHR = cp × (T_entering - T_leaving) / Δh_total

Where SHR is the sensible heat ratio and Δh_total includes both sensible and latent components.

### Mixed Air Calculations

Mixing outdoor and return air:

T_mixed = (ṁ_oa × T_oa + ṁ_ra × T_ra) / (ṁ_oa + ṁ_ra)

This assumes constant specific heat across the temperature range, valid for HVAC temperature differences.

## Enthalpy-Based Calculations

Since h = cp × T for ideal gases (zero reference), specific heat provides direct conversion between temperature and enthalpy:

**Dry air enthalpy:**
h_da = cp × T = 1.006 × T (kJ/kg) [T in °C above 0°C reference]

**Moist air enthalpy:**
h_ma = (1.006 × T) + W × (2501 + 1.86 × T)

The 1.86 coefficient represents water vapor specific heat, appearing in the sensible heat component of moisture.

## Computational Considerations

### Software Implementation

Building energy simulation software (EnergyPlus, TRNSYS, eQuest) implements specific heat as:

- Constant value for rapid calculations in typical ranges
- Temperature-dependent polynomial for detailed annual simulations
- Pressure-corrected values for high-altitude projects
- Moist air mixture properties for coupled heat-mass transfer

### Precision and Rounding

Engineering calculations balance precision with practicality:

**Load calculations:** 3 significant figures (cp = 1.01 kJ/(kg·K))
**Energy modeling:** 4 significant figures (cp = 1.006 kJ/(kg·K))
**Research/calibration:** 5+ significant figures with temperature dependence

Excessive precision in specific heat provides no benefit when other inputs (flow rates, temperatures) carry larger uncertainties.

## Code and Standard References

### ASHRAE Fundamentals

**ASHRAE Handbook - Fundamentals (2021):**
- Chapter 1: Psychrometrics - Provides moist air specific heat equations
- Chapter 33: Physical Properties of Materials - Tables of thermophysical properties
- Chapter 19: Energy Estimating and Modeling Methods - Application to loads

**Reference values:**
- Table 1 (Chapter 1): Thermodynamic properties of moist air
- Equation 27: cp,ma = cp,da + W × cp,v

### Industry Standards

**AHRI Standard 210/240:**
Specifies standard air properties for rating calculations:
- Standard air: 20°C (68°F), 101.325 kPa
- cp = 1.006 kJ/(kg·K) or 0.240 Btu/(lbm·°F)

**ISO 13790:**
Energy performance of buildings:
- Default specific heat: 1.0 kJ/(kg·K) for simplified calculations
- Temperature-dependent values for detailed dynamic simulation

## Common Errors and Misconceptions

### Using cv Instead of cp

Incorrect application of constant volume specific heat to open systems leads to 29% underestimation of energy requirements (since cv/cp = 0.714).

**Correct:** Q = ṁ × 1.006 × ΔT
**Incorrect:** Q = ṁ × 0.718 × ΔT

### Ignoring Moisture Content

For humid climates, dry air specific heat underestimates moist air heat capacity:

**Error at 80% RH, 30°C:**
- Dry air assumption: cp = 1.006 kJ/(kg·K)
- Actual moist air: cp = 1.044 kJ/(kg·K)
- Undersizing error: 3.8%

### Altitude Neglect

Using sea-level factors at elevation:

**Denver example (1600 m / 5280 ft):**
- Sea level factor: 1.08 Btu/(hr·cfm·°F)
- Actual factor: 0.91 Btu/(hr·cfm·°F)
- Oversizing: 19% if uncorrected

## Advanced Applications

### Compressible Flow

In high-velocity duct systems approaching Mach 0.3, specific heat ratio affects pressure recovery:

Stagnation pressure: P₀ = P × (1 + ((γ-1)/2) × M²)^(γ/(γ-1))

For air with γ = 1.4, pressure recovery becomes significant above 30 m/s (6000 fpm).

### Acoustic Analysis

Sound propagation speed in ducts:

c = √(γ × R × T) = √(1.4 × 287 × T)

At 20°C: c = 343 m/s (1125 ft/s)

Specific heat ratio directly determines acoustic velocity, affecting duct noise attenuation calculations.

### Refrigeration Cycles

In air-source heat pumps and chillers, the specific heat ratio governs isentropic compression efficiency:

Isentropic work: W_s = (cp × T₁) × [(P₂/P₁)^((γ-1)/γ) - 1]

Compressor performance maps depend on accurate γ values for refrigerant and air-side calculations.

## Measurement and Verification

Direct measurement of specific heat requires calorimetry, impractical for field verification. Instead, HVAC professionals verify proper application through:

**Energy balance verification:**
Q_measured = ṁ_measured × cp_assumed × ΔT_measured

If measured power disagrees with calculated values by more than 5%, investigate flow measurement, temperature sensors, or heat losses rather than specific heat values.

**Psychrometric verification:**
Compare measured temperature changes against psychrometric chart predictions using standard specific heat. Agreement within instrument accuracy (±0.5°F or ±0.3°C) confirms proper values.

## Summary

Specific heat of air represents a fundamental thermophysical property governing all HVAC sensible heat calculations. The constant pressure value (cp = 1.006 kJ/(kg·K) or 0.240 Btu/(lbm·°F)) applies to standard air handling processes, while the constant volume value (cv = 0.718 kJ/(kg·K)) serves theoretical analysis.

**Key engineering values:**
- Standard factor (I-P): 1.08 Btu/(hr·cfm·°F)
- Standard factor (SI): 1.21 kW/(m³/s·K)
- Specific heat ratio: γ = 1.40
- Temperature dependence: <0.2% variation in HVAC range

Proper application requires consideration of moisture content in humid conditions, altitude correction above 500 m (1500 ft), and recognition that the constant pressure process assumption underlies all HVAC air-side thermal calculations.
