---
title: "Water Viscosity"
description: "Comprehensive analysis of dynamic and kinematic viscosity of water including temperature relationships, empirical correlations, property tables, and applications to pressure drop calculations in HVAC hydronic systems"
weight: 2
---

## Technical Overview

Water viscosity quantifies the internal resistance to flow and shear deformation in liquid water. This transport property directly impacts pressure drop calculations, pump sizing, heat exchanger performance, and flow regime transitions in all hydronic HVAC systems. Viscosity decreases exponentially with temperature, creating significant design implications across the operating range of heating and cooling systems.

Two forms of viscosity characterize fluid behavior:

**Dynamic (Absolute) Viscosity (μ):** The fundamental property representing the ratio of shear stress to velocity gradient in a flowing fluid. Units: Pa·s, cP (centipoise), or mPa·s.

**Kinematic Viscosity (ν):** The ratio of dynamic viscosity to fluid density, representing momentum diffusivity. Units: m²/s, cSt (centistokes), or mm²/s.

The relationship between dynamic and kinematic viscosity:

ν = μ / ρ

Where:
- ν = kinematic viscosity (m²/s)
- μ = dynamic viscosity (Pa·s)
- ρ = density (kg/m³)

## Temperature Dependence

Water viscosity exhibits strong inverse exponential dependence on temperature. As temperature increases, intermolecular forces weaken, molecular kinetic energy increases, and resistance to flow decreases substantially. This temperature sensitivity exceeds that of most other thermophysical properties.

### Quantitative Temperature Effect

From 0°C to 100°C at atmospheric pressure, dynamic viscosity decreases by approximately 84%, from 1.79 mPa·s to 0.28 mPa·s. This reduction directly translates to decreased pumping power requirements in heating systems compared to chilled water systems operating at identical flow rates.

### Design Implications

- Chilled water systems (4-7°C) operate with viscosities 1.6-1.7 times higher than hot water systems (60-80°C)
- Pressure drop in chilled water piping approximately 60-70% higher than equivalent hot water systems at same volumetric flow
- Pump power requirements scale proportionally with pressure drop differences
- Reynolds numbers in heating systems substantially higher, promoting turbulent flow at lower velocities

## Empirical Correlations

### Vogel-Fulcher-Tammann Equation

The most accurate correlation for water dynamic viscosity over the liquid range:

μ(T) = A × exp[B / (T - C)]

Where:
- μ = dynamic viscosity (mPa·s)
- T = temperature (K)
- A = 0.02939 mPa·s
- B = 507.88 K
- C = 149.3 K

Applicable range: 0°C to 370°C
Accuracy: ±1% deviation from experimental data

### Andrade Equation

Simplified form suitable for HVAC temperature ranges:

μ(T) = A × exp(B / T)

Where:
- μ = dynamic viscosity (Pa·s)
- T = absolute temperature (K)
- A, B = empirical constants

For water: A ≈ 2.414 × 10⁻⁵ Pa·s, B ≈ 247.8 K (approximate values)

### Polynomial Approximation

For computational applications in HVAC software:

ln(μ) = a₀ + a₁T + a₂T² + a₃T³

Where T is in °C and coefficients fitted over specific ranges.

## Dynamic Viscosity Data

### Standard Temperature Points

Critical reference values for HVAC calculations:

| Temperature | Dynamic Viscosity | Relative to 20°C |
|-------------|------------------|------------------|
| 0°C | 1.79 mPa·s | 1.79× |
| 4°C | 1.57 mPa·s | 1.57× |
| 10°C | 1.31 mPa·s | 1.31× |
| 20°C | 1.00 mPa·s | 1.00× |
| 40°C | 0.653 mPa·s | 0.653× |
| 60°C | 0.467 mPa·s | 0.467× |
| 80°C | 0.355 mPa·s | 0.355× |
| 100°C | 0.282 mPa·s | 0.282× |

### Extended Temperature Range

Comprehensive data for specialized applications:

| Temperature (°C) | Dynamic Viscosity (mPa·s) | Temperature (°C) | Dynamic Viscosity (mPa·s) |
|-----------------|---------------------------|-----------------|---------------------------|
| 0 | 1.787 | 55 | 0.504 |
| 5 | 1.519 | 60 | 0.467 |
| 10 | 1.307 | 65 | 0.434 |
| 15 | 1.139 | 70 | 0.404 |
| 20 | 1.002 | 75 | 0.378 |
| 25 | 0.890 | 80 | 0.355 |
| 30 | 0.798 | 85 | 0.334 |
| 35 | 0.719 | 90 | 0.315 |
| 40 | 0.653 | 95 | 0.297 |
| 45 | 0.596 | 100 | 0.282 |
| 50 | 0.547 | | |

### Pressure Effects

Water viscosity increases slightly with pressure. For typical HVAC hydronic systems (gauge pressures below 1500 kPa), pressure effects remain negligible (<2% deviation). High-pressure applications require correction factors:

μ(P,T) = μ(P₀,T) × [1 + αP]

Where α ≈ 2-3 × 10⁻⁹ Pa⁻¹ for water near 20°C.

## Kinematic Viscosity Data

Kinematic viscosity accounts for density variation with temperature, providing the parameter directly used in Reynolds number calculations.

### Standard Conditions

| Temperature | Kinematic Viscosity | Dynamic Viscosity | Density |
|-------------|---------------------|-------------------|---------|
| 0°C | 1.787 mm²/s | 1.787 mPa·s | 1000.0 kg/m³ |
| 4°C | 1.568 mm²/s | 1.567 mPa·s | 1000.0 kg/m³ |
| 10°C | 1.306 mm²/s | 1.307 mPa·s | 999.7 kg/m³ |
| 20°C | 1.004 mm²/s | 1.002 mPa·s | 998.2 kg/m³ |
| 40°C | 0.658 mm²/s | 0.653 mPa·s | 992.2 kg/m³ |
| 60°C | 0.475 mm²/s | 0.467 mPa·s | 983.2 kg/m³ |
| 80°C | 0.365 mm²/s | 0.355 mPa·s | 971.8 kg/m³ |
| 100°C | 0.294 mm²/s | 0.282 mPa·s | 958.4 kg/m³ |

### Conversion Relations

Standard unit conversions for viscosity:

**Dynamic Viscosity:**
- 1 Pa·s = 1000 mPa·s = 1000 cP
- 1 mPa·s = 1 cP
- 1 lbf·s/ft² = 47.88 Pa·s

**Kinematic Viscosity:**
- 1 m²/s = 10⁶ mm²/s = 10⁶ cSt
- 1 mm²/s = 1 cSt
- 1 ft²/s = 0.0929 m²/s

## Applications to Pressure Drop Calculations

### Reynolds Number

Viscosity directly determines flow regime through the Reynolds number:

Re = ρVD / μ = VD / ν

Where:
- Re = Reynolds number (dimensionless)
- ρ = density (kg/m³)
- V = velocity (m/s)
- D = pipe diameter (m)
- μ = dynamic viscosity (Pa·s)
- ν = kinematic viscosity (m²/s)

Flow regime classification:
- Re < 2300: Laminar flow
- 2300 < Re < 4000: Transition region
- Re > 4000: Turbulent flow (typical HVAC systems)

### Darcy-Weisbach Equation

Pressure drop in piping systems depends on friction factor, which varies with Reynolds number and thus viscosity:

ΔP = f × (L/D) × (ρV²/2)

For laminar flow (Re < 2300):
f = 64 / Re

Viscosity appears directly in friction factor, creating strong temperature dependence.

For turbulent flow, friction factor depends weakly on Reynolds number through implicit equations (Colebrook, Swamee-Jain), but viscosity remains influential.

### Hagen-Poiseuille Equation

For laminar flow in circular pipes:

ΔP = (128μLQ) / (πD⁴)

Where:
- ΔP = pressure drop (Pa)
- μ = dynamic viscosity (Pa·s)
- L = pipe length (m)
- Q = volumetric flow rate (m³/s)
- D = pipe diameter (m)

Pressure drop scales linearly with viscosity in laminar conditions.

### Practical Design Calculations

**Example: Chilled Water vs. Hot Water Comparison**

Consider identical piping systems with turbulent flow (Re > 10,000):

Chilled water at 7°C: μ = 1.42 mPa·s
Hot water at 70°C: μ = 0.404 mPa·s

Viscosity ratio = 1.42 / 0.404 = 3.51

For turbulent flow in smooth pipes where f ∝ Re⁻⁰·²:

Pressure drop ratio ≈ (μ_cold / μ_hot)⁰·² = (3.51)⁰·² ≈ 1.29

Chilled water systems experience approximately 29% higher pressure drop than hot water systems at equivalent flow velocities.

## Glycol Solutions

Adding ethylene glycol or propylene glycol for freeze protection substantially increases viscosity:

| Temperature | Water | 30% EG | 50% EG |
|-------------|-------|--------|--------|
| 0°C | 1.79 mPa·s | 4.87 mPa·s | 15.6 mPa·s |
| 20°C | 1.00 mPa·s | 2.50 mPa·s | 6.00 mPa·s |
| 40°C | 0.653 mPa·s | 1.57 mPa·s | 3.16 mPa·s |

Glycol concentration must be minimized to reduce pumping penalties while maintaining adequate freeze protection.

## ASHRAE References

**ASHRAE Handbook—Fundamentals (2021):**
- Chapter 33: Physical Properties of Secondary Coolants (Brines)
  - Table 1: Physical properties of water
  - Viscosity data from 0°C to 100°C at saturation
  - Glycol solution viscosity correlations

**ASHRAE Handbook—HVAC Systems and Equipment (2020):**
- Chapter 13: Hydronic Heating and Cooling System Design
  - Pressure drop calculation methodologies incorporating viscosity
  - Pipe sizing procedures accounting for temperature-dependent properties

## Design Considerations

### Pump Selection

Account for viscosity variation across operating range:

1. Calculate pressure drop at maximum viscosity condition (lowest temperature)
2. Verify pump operates within acceptable performance curve range
3. Account for increased power consumption in cold-start conditions
4. Consider variable-speed drives to optimize efficiency as temperature rises

### Pipe Sizing

Select pipe diameters ensuring:

1. Velocities maintain turbulent flow (Re > 4000) for optimal heat transfer
2. Pressure drop remains within acceptable limits at maximum viscosity
3. Erosion velocity limits not exceeded at minimum viscosity
4. Economic balance between pipe cost and pumping cost

Typical HVAC velocity range: 0.6-2.4 m/s (2-8 ft/s)

### System Fill and Startup

During initial fill with cold water:

1. Viscosity 50-80% higher than design operating conditions
2. Increased pressure drop may trigger pump overload protection
3. Air elimination more difficult due to reduced turbulence
4. Chemical treatment dispersion slower

Recommend gradual temperature increase during commissioning.

### Heat Transfer Impact

While viscosity primarily affects pressure drop, secondary impacts on heat transfer occur through:

1. Prandtl number variation: Pr = μc_p / k
2. Boundary layer thickness in heat exchangers
3. Convective heat transfer coefficients in forced convection

Higher viscosity reduces convective coefficients by 10-15% in chilled water applications compared to hot water.

### Flow Measurement

Viscosity affects certain flowmeter types:

- **Differential pressure meters:** Require Reynolds number corrections
- **Turbine meters:** Viscosity drag on rotor affects accuracy below Re = 10,000
- **Magnetic flowmeters:** Unaffected by viscosity (conductivity-based)
- **Ultrasonic flowmeters:** Minimal viscosity dependence

Select flowmeter technology appropriate for expected viscosity range.

### Control Valve Sizing

Valve flow coefficients (C_v) derived assuming water at 60°F (15.6°C). For significantly different temperatures:

C_v,corrected = C_v,catalog × √(SG × (1 + f_v))

Where f_v represents viscosity correction factor from manufacturer data.

### Energy Efficiency Implications

Lower viscosity in heating systems provides inherent efficiency advantages:

1. Reduced pumping power (proportional to pressure drop)
2. Higher Reynolds numbers improve heat transfer
3. Lower parasitic losses in distribution
4. Improved control valve authority

Conversely, chilled water systems face viscosity penalties requiring larger pumps and higher operating costs.

## Measurement Methods

### Capillary Viscometers

Glass capillary viscometers (Ubbelohde, Cannon-Fenske) measure kinematic viscosity based on timed efflux through calibrated tubes. Accuracy: ±0.5% for water.

### Rotational Viscometers

Concentric cylinder or cone-plate geometries measure dynamic viscosity through torque-rotational speed relationships. Suitable for quality control and non-Newtonian fluids.

### Industrial Standards

- **ASTM D445:** Standard test method for kinematic viscosity
- **ASTM D2161:** Standard practice for conversion of kinematic viscosity to Saybolt Universal viscosity
- **ISO 3104:** Petroleum products—Transparent and opaque liquids—Determination of kinematic viscosity

## Summary

Water viscosity represents a critical transport property for HVAC hydronic system design. The strong temperature dependence, spanning nearly an order of magnitude across typical operating ranges, creates significant differences in pressure drop, pumping power, and heat transfer between heating and cooling applications. Accurate viscosity data enables proper pipe sizing, pump selection, and energy consumption predictions. Engineers must account for worst-case viscosity conditions (coldest temperatures) when designing system components while recognizing efficiency benefits at elevated temperatures. The addition of glycol for freeze protection dramatically increases viscosity, requiring careful concentration selection balancing freeze protection requirements against pumping penalties.
