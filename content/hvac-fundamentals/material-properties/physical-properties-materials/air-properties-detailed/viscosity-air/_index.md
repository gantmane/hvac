---
title: "Viscosity of Air"
description: "Comprehensive analysis of air viscosity including dynamic and kinematic viscosity, Sutherland's law, temperature relationships, and engineering applications in HVAC system design and analysis."
weight: 2
---

## Overview

Air viscosity represents the internal resistance to flow within the fluid, quantifying the momentum transfer between adjacent layers moving at different velocities. This transport property fundamentally affects pressure drop calculations, fan power requirements, heat transfer coefficients, and flow regime determination in all HVAC applications.

Unlike liquids, gas viscosity increases with temperature due to enhanced molecular activity and momentum exchange at elevated kinetic energy levels. This behavior directly impacts duct design, filter performance, and energy consumption across operating temperature ranges.

## Molecular Basis of Gas Viscosity

Air viscosity arises from momentum transfer between gas molecules moving in different velocity layers. When faster-moving molecules diffuse into slower layers, they impart momentum, creating resistance to the velocity gradient.

**Key molecular mechanisms:**

- Momentum exchange through molecular collisions increases with temperature
- Mean free path between collisions affects viscous shear stress
- Molecular mass and diameter influence collision frequency
- Gas composition determines mixture viscosity properties

The kinetic theory of gases predicts viscosity proportional to the square root of absolute temperature, though empirical corrections improve accuracy at HVAC operating conditions.

## Dynamic (Absolute) Viscosity

Dynamic viscosity μ quantifies the relationship between shear stress τ and velocity gradient du/dy in fluid flow:

```
τ = μ (du/dy)
```

Where:
- τ = shear stress (Pa)
- μ = dynamic viscosity (Pa·s or kg/m·s)
- du/dy = velocity gradient perpendicular to flow (1/s)

### Standard Reference Values

**At 20°C (68°F), 101.325 kPa:**
- Dynamic viscosity: μ = 1.825 × 10⁻⁵ Pa·s
- Commonly approximated: μ ≈ 1.81 × 10⁻⁵ Pa·s

This reference value appears throughout ASHRAE handbooks and engineering calculations as the baseline for standard air properties.

### Dynamic Viscosity vs Temperature

| Temperature (°C) | Temperature (°F) | Dynamic Viscosity (Pa·s × 10⁻⁵) | Dynamic Viscosity (lbm/ft·s × 10⁻⁵) |
|------------------|------------------|----------------------------------|--------------------------------------|
| -40 | -40 | 1.514 | 1.017 |
| -20 | -4 | 1.632 | 1.096 |
| 0 | 32 | 1.716 | 1.153 |
| 10 | 50 | 1.778 | 1.194 |
| 20 | 68 | 1.825 | 1.226 |
| 30 | 86 | 1.872 | 1.258 |
| 40 | 104 | 1.918 | 1.289 |
| 50 | 122 | 1.963 | 1.319 |
| 60 | 140 | 2.008 | 1.349 |
| 70 | 158 | 2.052 | 1.379 |
| 80 | 176 | 2.096 | 1.408 |
| 90 | 194 | 2.139 | 1.437 |
| 100 | 212 | 2.181 | 1.466 |
| 150 | 302 | 2.420 | 1.626 |
| 200 | 392 | 2.640 | 1.774 |
| 250 | 482 | 2.849 | 1.914 |
| 300 | 572 | 3.047 | 2.047 |

**Data source:** ASHRAE Handbook - Fundamentals, Chapter 1

## Kinematic Viscosity

Kinematic viscosity ν represents the ratio of dynamic viscosity to density, eliminating mass units and simplifying many flow calculations:

```
ν = μ / ρ
```

Where:
- ν = kinematic viscosity (m²/s)
- μ = dynamic viscosity (Pa·s)
- ρ = density (kg/m³)

### Kinematic Viscosity vs Temperature

| Temperature (°C) | Temperature (°F) | Kinematic Viscosity (m²/s × 10⁻⁶) | Kinematic Viscosity (ft²/s × 10⁻⁴) |
|------------------|------------------|-------------------------------------|--------------------------------------|
| -40 | -40 | 8.86 | 9.54 |
| -20 | -4 | 11.76 | 12.66 |
| 0 | 32 | 13.28 | 14.29 |
| 10 | 50 | 14.16 | 15.24 |
| 20 | 68 | 15.06 | 16.21 |
| 30 | 86 | 15.98 | 17.20 |
| 40 | 104 | 16.92 | 18.21 |
| 50 | 122 | 17.88 | 19.24 |
| 60 | 140 | 18.86 | 20.30 |
| 70 | 158 | 19.84 | 21.36 |
| 80 | 176 | 20.84 | 22.43 |
| 90 | 194 | 21.86 | 23.52 |
| 100 | 212 | 22.88 | 24.63 |
| 150 | 302 | 28.93 | 31.14 |
| 200 | 392 | 35.32 | 38.02 |
| 250 | 482 | 42.06 | 45.28 |
| 300 | 572 | 49.08 | 52.83 |

Kinematic viscosity increases more rapidly with temperature than dynamic viscosity because air density decreases as temperature rises, amplifying the ratio effect.

## Sutherland's Law for Air Viscosity

Sutherland's law provides accurate viscosity predictions across the temperature range encountered in HVAC applications, accounting for intermolecular forces through an empirical constant.

### General Sutherland Equation

```
μ = μ₀ × (T/T₀)^(3/2) × (T₀ + S)/(T + S)
```

Where:
- μ = dynamic viscosity at temperature T (Pa·s)
- μ₀ = reference dynamic viscosity (Pa·s)
- T = absolute temperature (K)
- T₀ = reference absolute temperature (K)
- S = Sutherland's constant (K)

### Air-Specific Constants

**Standard reference state:**
- T₀ = 273.15 K (0°C)
- μ₀ = 1.716 × 10⁻⁵ Pa·s
- S = 110.4 K (Sutherland's constant for air)

**Alternative reference (ASHRAE preference):**
- T₀ = 293.15 K (20°C)
- μ₀ = 1.825 × 10⁻⁵ Pa·s
- S = 110.4 K

### Simplified Engineering Form

For temperatures between 0°C and 200°C with acceptable accuracy (±2%):

```
μ = 1.458 × 10⁻⁶ × T^(3/2) / (T + 110.4)
```

Where:
- μ = dynamic viscosity (Pa·s)
- T = absolute temperature (K)

### Imperial Units Form

```
μ = 1.8463 × 10⁻⁷ × T^(3/2) / (T + 198.72)
```

Where:
- μ = dynamic viscosity (lbm/ft·s)
- T = absolute temperature (°R)

## Temperature Dependence Characteristics

### Viscosity-Temperature Relationship

Gas viscosity increases with temperature following power-law behavior modified by intermolecular attraction terms. The physical mechanism differs fundamentally from liquid viscosity, which decreases with temperature.

**Temperature coefficient:**

```
dμ/dT ≈ 7.0 × 10⁻⁸ Pa·s/K (at 20°C)
```

This represents approximately 0.38% increase per degree Celsius near room temperature.

### Comparison with Power Law Approximation

Simple power law approximation for limited temperature ranges:

```
μ ≈ C × T^n
```

Where:
- C = constant determined by reference conditions
- n ≈ 0.7 to 0.8 (depending on temperature range)

Sutherland's law provides superior accuracy across wide temperature ranges by incorporating the S term representing intermolecular forces.

## Pressure Effects on Viscosity

Air viscosity remains essentially independent of pressure across the range encountered in HVAC systems (0.5 to 3.0 atmospheres). Measurable pressure effects only occur at:

- Very high pressures (>10 atmospheres)
- Very low pressures (<0.01 atmospheres)
- Near critical conditions (not applicable to air)

**Design implication:** Standard viscosity values apply for all normal HVAC pressurization levels, including fan discharge conditions, tall building static pressure variations, and altitude effects.

## Humidity Effects on Air Viscosity

Water vapor slightly reduces air viscosity because water molecules (molecular weight 18) are lighter than average air molecules (effective molecular weight 28.97). The effect remains small for typical HVAC humidity levels.

**Approximate correction:**

```
μ_humid ≈ μ_dry × (1 - 0.00012 × RH)
```

Where RH = relative humidity (%)

For engineering calculations, humidity effects on viscosity are typically negligible (<1% error) and can be ignored except in precision psychrometric research.

## Reynolds Number Calculations

Reynolds number Re characterizes flow regime transitions from laminar to turbulent flow, directly depending on kinematic viscosity:

```
Re = ρ × V × D / μ = V × D / ν
```

Where:
- Re = Reynolds number (dimensionless)
- ρ = density (kg/m³)
- V = velocity (m/s)
- D = characteristic dimension (m)
- μ = dynamic viscosity (Pa·s)
- ν = kinematic viscosity (m²/s)

### Critical Reynolds Numbers in HVAC

**Duct flow:**
- Re < 2,300: Laminar flow (rare in HVAC)
- 2,300 < Re < 4,000: Transitional flow
- Re > 4,000: Turbulent flow (typical HVAC operation)

**Flow over tubes (heat exchangers):**
- Re < 40: Creeping flow
- 40 < Re < 1,000: Vortex shedding region
- Re > 1,000: Fully turbulent

### Temperature Impact on Flow Regime

Higher air temperatures increase kinematic viscosity, reducing Reynolds number at constant velocity. This shifts flow toward laminar regime, affecting:

- Pressure drop coefficients
- Heat transfer correlations
- Mixing and entrainment characteristics
- Acoustic generation mechanisms

## Engineering Applications

### Pressure Drop Calculations

Friction factor f in the Darcy-Weisbach equation depends on Reynolds number, which directly incorporates viscosity:

```
ΔP = f × (L/D) × (ρ × V²/2)
```

For turbulent flow in smooth ducts (Blasius correlation):

```
f = 0.316 / Re^0.25
```

Temperature variations affecting viscosity change friction factors by 5-10% across typical HVAC operating ranges.

### Fan Performance Corrections

Fan laws assume constant air properties. When temperature changes significantly from rated conditions, viscosity effects require correction through Reynolds number adjustments affecting efficiency and power:

```
η_actual / η_rated ≈ 1 - 0.2 × (1 - (Re_actual / Re_rated)^0.1)
```

This correction becomes significant for temperature differences exceeding 30°C from rated conditions.

### Filter Pressure Drop

Filter media pressure drop varies inversely with viscosity at constant mass flow rate. Temperature increases reduce viscosity-dependent resistance:

```
ΔP_filter ∝ μ / ρ = ν
```

A 40°C temperature rise from 20°C to 60°C increases kinematic viscosity by approximately 25%, increasing clean filter pressure drop proportionally.

### Heat Transfer Coefficients

Viscosity appears in dimensionless correlations governing convective heat transfer. The Prandtl number Pr relates momentum and thermal diffusion:

```
Pr = ν / α = μ × cp / k
```

Where:
- α = thermal diffusivity (m²/s)
- cp = specific heat (J/kg·K)
- k = thermal conductivity (W/m·K)

For air, Pr ≈ 0.71 across HVAC temperature ranges, varying less than 2% from -20°C to 100°C.

## Design Considerations

### Standard Air vs Actual Conditions

AMCA fan ratings use standard air (20°C, 101.325 kPa, 1.204 kg/m³). Field conditions require corrections accounting for viscosity changes through Reynolds number effects on fan efficiency.

**Reynolds number correction factor:**

```
Re_field / Re_standard = (T_standard / T_field)^0.5 × (P_field / P_standard)
```

### Altitude Effects

Atmospheric pressure decreases with altitude, reducing air density but not significantly affecting dynamic viscosity. Kinematic viscosity increases with altitude:

```
ν_altitude = ν_sea_level × (ρ_sea_level / ρ_altitude)
```

At 1,500 m (5,000 ft) elevation, kinematic viscosity increases approximately 18% compared to sea level at the same temperature.

### Economizer Operation

Wide temperature variations between outdoor air (-20°C) and return air (24°C) during economizer operation create viscosity differences affecting mixed air properties. The mixture viscosity follows mole-fraction weighting:

```
μ_mix = Σ(y_i × μ_i)
```

Where y_i represents mole fraction of each stream.

### High-Temperature Applications

Industrial HVAC systems handling process exhaust at elevated temperatures (150-300°C) experience viscosity increases of 40-75% compared to standard conditions, significantly affecting:

- Exhaust fan power requirements
- Duct pressure drop calculations
- Heat recovery effectiveness
- Thermal expansion compensation

## ASHRAE Standards and References

**ASHRAE Handbook - Fundamentals, Chapter 1:** Psychrometrics
- Table 1: Thermophysical properties of air
- Figure 15: Viscosity of air vs temperature

**ASHRAE Handbook - Fundamentals, Chapter 3:** Fluid Flow
- Section on Reynolds number and friction factors
- Viscosity applications in pressure drop calculations

**ASHRAE Standard 41.6:** Standard Method for Measurement of Moist Air Properties
- Specifies viscosity measurement procedures
- Defines standard reference conditions

**AMCA 210:** Laboratory Methods of Testing Fans for Certified Aerodynamic Performance Rating
- Standard air definition incorporating viscosity
- Reynolds number corrections for non-standard conditions

## Measurement Methods

**Capillary viscometers:** Measure time for air to flow through precision capillary tubes under pressure differential.

**Rotating cylinder viscometers:** Determine viscosity from torque required to rotate cylinder in air gap.

**Oscillating disk viscometers:** Calculate viscosity from damping of oscillating element in gas.

Laboratory measurements typically achieve accuracy of ±0.5% for dynamic viscosity at controlled temperature and pressure conditions.

## Components

- Dynamic Viscosity Air Vs Temperature
- Viscosity 20c 1 81e 5 Pa S
- Kinematic Viscosity Air
- Sutherland Equation Air
- Temperature Dependence Gases
