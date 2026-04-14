---
title: "Mixing"
aliases: ["Mixing"]
description: "Engineering analysis of adiabatic mixing processes for air streams, including mass and energy balance equations, graphical methods, and HVAC design applications"
weight: 6
---

## Overview

Mixing of two or more air streams represents one of the most common psychrometric processes in HVAC systems. This adiabatic process occurs whenever return air combines with outdoor air in economizer cycles, exhaust air mixes with outdoor air in energy recovery systems, or zone air streams merge in return plenums. The analysis of mixing processes relies on fundamental conservation principles—mass balance and energy balance—applied to the moisture and dry air constituents.

The mixed air state point lies on a straight line connecting the two inlet air states on the psychrometric chart. The exact location along this line depends on the mass flow rate ratio of the two streams. Understanding mixing processes is essential for economizer control strategies, minimum outdoor air calculations, freeze protection, and energy recovery system design.

## Fundamental Principles

### Conservation Laws

The mixing process follows two fundamental conservation principles:

**Mass Conservation:**
- Total dry air mass flow rate is conserved
- Total moisture mass flow rate is conserved
- Volume flow rates do not add linearly (density varies with state)

**Energy Conservation:**
- Total enthalpy flow rate is conserved for adiabatic mixing
- No heat transfer occurs with surroundings
- Kinetic and potential energy changes are negligible

### Graphical Representation

On the psychrometric chart, the mixed air state point lies on the straight line connecting the two inlet states. This linear relationship results from the fact that both dry-bulb temperature and humidity ratio are extensive properties when considering mass flow rates.

The position along the mixing line is determined by the **lever rule**, which states that the ratio of distances from the mixed point to each inlet point is inversely proportional to the mass flow rate ratio.

## Engineering Equations

### Two-Stream Mixing Analysis

For two air streams mixing adiabatically:

**Mass Balance - Dry Air:**

```
ṁ₃ = ṁ₁ + ṁ₂
```

Where:
- ṁ₃ = mixed air mass flow rate (lb/min or kg/s)
- ṁ₁ = stream 1 mass flow rate (lb/min or kg/s)
- ṁ₂ = stream 2 mass flow rate (lb/min or kg/s)

**Mass Balance - Moisture:**

```
ṁ₃ · W₃ = ṁ₁ · W₁ + ṁ₂ · W₂

W₃ = (ṁ₁ · W₁ + ṁ₂ · W₂) / (ṁ₁ + ṁ₂)
```

Where:
- W = humidity ratio (lb_w/lb_da or kg_w/kg_da)

**Energy Balance - Enthalpy:**

```
ṁ₃ · h₃ = ṁ₁ · h₁ + ṁ₂ · h₂

h₃ = (ṁ₁ · h₁ + ṁ₂ · h₂) / (ṁ₁ + ṁ₂)
```

Where:
- h = specific enthalpy (Btu/lb_da or kJ/kg_da)

**Dry-Bulb Temperature:**

```
T₃ = (ṁ₁ · T₁ + ṁ₂ · T₂) / (ṁ₁ + ṁ₂)
```

Where:
- T = dry-bulb temperature (°F or °C)

### Bypass Factor Formulation

When mixing return air with outdoor air, the equation can be expressed using bypass factor (X):

```
X = ṁ_oa / ṁ_total

T_ma = (1 - X) · T_ra + X · T_oa
W_ma = (1 - X) · W_ra + X · W_oa
h_ma = (1 - X) · h_ra + X · h_oa
```

Where:
- X = outdoor air fraction (dimensionless)
- ma = mixed air
- ra = return air
- oa = outdoor air

### Volumetric Flow Rate Considerations

**Volume flow rates do not add linearly** because air density changes with temperature and moisture content:

```
V̇₃ ≠ V̇₁ + V̇₂  (generally not equal)
```

To convert between mass and volume flow rates:

```
ṁ = ρ · V̇ = V̇ / v

V̇ = ṁ · v
```

Where:
- ρ = air density (lb/ft³ or kg/m³)
- v = specific volume (ft³/lb or m³/kg)
- V̇ = volume flow rate (cfm or m³/s)

**Corrected Mixed Volume Flow Rate:**

```
V̇₃ = ṁ₃ · v₃ = (ṁ₁ + ṁ₂) · v₃
```

The specific volume v₃ must be evaluated at the mixed air conditions.

## Mixing Line Properties

### Linear Relationship

For any property φ that is extensive with respect to dry air mass:

```
φ₃ = (ṁ₁ · φ₁ + ṁ₂ · φ₂) / (ṁ₁ + ṁ₂)
```

This applies to:
- Dry-bulb temperature (T)
- Humidity ratio (W)
- Enthalpy (h)
- Dew-point temperature (T_dp)

### Lever Rule Application

The position of the mixed point divides the mixing line such that:

```
Distance from point 1 to mixed point     ṁ₂
─────────────────────────────────────  = ────
Distance from point 2 to mixed point     ṁ₁
```

This graphical relationship provides a quick check of calculations and enables visual estimation of mixed conditions.

### Non-Linear Properties

**Relative humidity and wet-bulb temperature do NOT follow linear relationships** during mixing. The mixed air relative humidity typically falls below both inlet stream relative humidities in the middle portion of the mixing line. This phenomenon occurs because saturation vapor pressure is an exponential function of temperature.

## HVAC System Applications

### Economizer Mixing

Air-side economizers mix outdoor air with return air to provide "free cooling" when outdoor conditions are favorable.

**Control Strategies:**

1. **Dry-bulb economizer:** Compares outdoor and return air temperatures
2. **Enthalpy economizer:** Compares outdoor and return air enthalpies
3. **Differential enthalpy:** Uses both temperature and humidity measurements

**Minimum Position:**
- Code-required minimum outdoor air must always be maintained
- IMC Section 403.3: Minimum 0.06 cfm/ft² or 15 cfm/person
- ASHRAE 62.1: Ventilation rate procedure or IAQ procedure

**Maximum Position:**
- Limited by design outdoor air damper capacity
- Typically 60-100% outdoor air depending on system design
- Must consider freeze protection for cooling coils

### Makeup Air Systems

In applications with exhaust requirements (kitchens, laboratories, industrial processes), makeup air must be provided:

```
V̇_ma = V̇_exhaust - V̇_relief

Mixed condition depends on:
- Building air temperature and humidity
- Outdoor air conditions
- Infiltration characteristics
```

### Return Air Plenum Mixing

Multiple zones with different conditions merge in return plenums:

```
T_mixed = Σ(ṁᵢ · Tᵢ) / Σ(ṁᵢ)
W_mixed = Σ(ṁᵢ · Wᵢ) / Σ(ṁᵢ)
```

This mixed return air then combines with outdoor air at the air handling unit.

### Energy Recovery Systems

Air-to-air energy recovery devices create effective mixing processes:

**Run-around loops:**
- Precondition outdoor air using energy from exhaust air
- Mixing calculation determines entering coil conditions

**Heat wheels and plate exchangers:**
- Transfer both sensible and latent energy
- Effectiveness determines degree of preconditioning

## Design Considerations

### Freeze Protection

Mixing outdoor air with return air reduces the risk of freezing coil damage, but careful analysis is required:

**Critical Conditions:**
- Outdoor air temperature < 32°F (0°C)
- Mixed air temperature < 35-40°F (2-4°C) at coil face
- Low load conditions with high outdoor air percentage

**Protection Strategies:**
1. Minimum mixed air temperature setpoint (typically 40-45°F)
2. Preheat coil upstream of mixing plenum
3. Face and bypass damper arrangements
4. Glycol addition to chilled water systems

### Damper Control Sequences

**Typical economizer sequence:**

1. **Full mechanical cooling:** Minimum outdoor air position
2. **Economizer transition:** Modulate outdoor air damper open
3. **Full economizer:** Maximum outdoor air position
4. **Integrated economizer:** Modulate outdoor air with mechanical cooling

**Damper sizing considerations:**
- Velocity through outdoor air damper: 500-800 fpm typical
- Pressure drop across dampers: 0.2-0.5 in. w.g.
- Leakage class per AMCA 500-D

### Stratification Prevention

Incomplete mixing creates temperature stratification in ducts and plenums:

**Factors promoting good mixing:**
- High velocity differential between streams (> 500 fpm difference)
- Turbulent flow conditions (Re > 4000)
- Adequate mixing length (minimum 5-7 equivalent diameters)
- Baffles or turning vanes to create turbulence

**Consequences of poor mixing:**
- Inaccurate temperature sensor readings
- Freezing damage to coil tubes in cold outdoor air streams
- Comfort complaints from non-uniform air delivery

### Sensor Placement

Temperature and humidity sensors measuring mixed air must be located where complete mixing has occurred:

- Minimum distance: 5 duct diameters downstream of mixing point
- Prefer locations after fans or coils (enhanced turbulence)
- Use averaging sensors or multiple sensors for large ducts
- Avoid locations near plenum walls or dead zones

## Calculation Methods

### Tabular Method

For hand calculations, organize data in tabular format:

| Parameter | Stream 1 (OA) | Stream 2 (RA) | Mixed Air |
|-----------|---------------|---------------|-----------|
| Mass flow rate, ṁ (lb/min) | 850 | 3,400 | 4,250 |
| Dry-bulb temp, T (°F) | 35.0 | 75.0 | - |
| Humidity ratio, W (lb/lb) | 0.0025 | 0.0095 | - |
| Enthalpy, h (Btu/lb) | 11.2 | 28.8 | - |

Calculate mixed properties using mass-weighted averages.

### Psychrometric Chart Method

1. Plot both inlet states on psychrometric chart
2. Draw straight line connecting the two points
3. Calculate mass flow rate ratio: r = ṁ₁/(ṁ₁ + ṁ₂)
4. Locate mixed point at fractional distance r along line from point 2 toward point 1
5. Read mixed air properties from chart

### Computer Methods

**Psychrometric calculation libraries:**
- ASHRAE RP-1485 psychrometric libraries
- PsychroLib (open source, multiple languages)
- Engineering Equation Solver (EES)
- MATLAB/Python psychrometric packages

**Building energy simulation:**
- EnergyPlus
- TRACE 3D Plus
- Carrier HAP
- Trane TRACE 700

## Standards and References

### ASHRAE Standards

**ASHRAE Fundamentals Handbook:**
- Chapter 1: Psychrometrics
- Equations 32-34: Moist air property calculations
- Figure 1: ASHRAE Psychrometric Chart No. 1

**ASHRAE 62.1 Ventilation for Acceptable Indoor Air Quality:**
- Section 5: Systems and Equipment
- Section 6.2: Outdoor Air Intake
- Appendix A: Mass Balance Method for multiple zones

**ASHRAE 90.1 Energy Standard:**
- Section 6.4.3.8: Economizer Requirements
- Section 6.5.1: Outdoor air damper controls
- Table 6.5.1: Economizer high-limit shutoff temperatures

### Code Requirements

**International Mechanical Code (IMC):**
- Section 403.3: Minimum ventilation rates
- Section 403.3.1: Outdoor air delivery monitoring
- Section 606.2: Air economizers

**International Energy Conservation Code (IECC):**
- Section C403.5: Economizers (commercial buildings)
- Table C403.3.1: Minimum equipment efficiencies

## Worked Examples

### Example 1: Economizer Mixed Air Calculation

**Given:**
- Outdoor air: T₁ = 55°F, W₁ = 0.0045 lb_w/lb_da
- Return air: T₂ = 75°F, W₂ = 0.0095 lb_w/lb_da
- Total supply air flow: 10,000 cfm at mixed conditions
- Outdoor air fraction: 40%

**Find:** Mixed air dry-bulb temperature, humidity ratio, and enthalpy

**Solution:**

For 40% outdoor air fraction:
```
X = 0.40

T_ma = (1 - 0.40) × 75 + 0.40 × 55
T_ma = 0.60 × 75 + 0.40 × 55
T_ma = 45 + 22 = 67°F

W_ma = (1 - 0.40) × 0.0095 + 0.40 × 0.0045
W_ma = 0.60 × 0.0095 + 0.40 × 0.0045
W_ma = 0.0057 + 0.0018 = 0.0075 lb_w/lb_da
```

From psychrometric chart at T = 67°F, W = 0.0075 lb_w/lb_da:
```
h_ma ≈ 25.8 Btu/lb_da
φ_ma ≈ 52% RH
```

Alternatively, calculate enthalpy directly:
```
h₁ = 0.240 × 55 + 0.0045(1061 + 0.444 × 55) = 18.1 Btu/lb
h₂ = 0.240 × 75 + 0.0095(1061 + 0.444 × 75) = 28.4 Btu/lb

h_ma = 0.60 × 28.4 + 0.40 × 18.1
h_ma = 17.0 + 7.2 = 24.2 Btu/lb
```

(Note: Direct calculation shows slight difference from chart reading due to chart resolution)

### Example 2: Minimum Outdoor Air with Variable Flow

**Given:**
- Design outdoor air requirement: 2,000 cfm at 75°F
- Current return air conditions: 72°F, 13.5 ft³/lb specific volume
- Current outdoor air conditions: 45°F, 12.9 ft³/lb specific volume
- Minimum outdoor air damper position maintains constant volume OA

**Find:** Mixed air temperature when system operates at 75% of design airflow

**Solution:**

Design outdoor air mass flow rate:
```
ṁ_oa,design = 2,000 cfm ÷ 13.5 ft³/lb = 148 lb/min
```

At 75% flow, if outdoor air volume remains constant (damper position fixed):
```
V̇_oa = 2,000 cfm (constant)
ṁ_oa = 2,000 ÷ 12.9 = 155 lb/min (varies with density)

V̇_total = 0.75 × V̇_design
V̇_design = V̇_oa,design ÷ X_design
```

Assuming design OA fraction was 20%:
```
V̇_design = 2,000 ÷ 0.20 = 10,000 cfm
V̇_total,current = 0.75 × 10,000 = 7,500 cfm

X_current = 2,000 ÷ 7,500 = 26.7% (increased OA fraction)

T_ma = 0.733 × 72 + 0.267 × 45
T_ma = 52.8 + 12.0 = 64.8°F
```

This demonstrates that outdoor air fraction increases at reduced flow when dampers maintain constant position.

### Example 3: Three-Stream Mixing

**Given:**
Three zone return air streams merge in return plenum:
- Zone 1: 1,500 cfm at 73°F, 50% RH
- Zone 2: 2,200 cfm at 68°F, 45% RH
- Zone 3: 1,800 cfm at 77°F, 55% RH

Standard air density: 0.075 lb/ft³

**Find:** Mixed return air temperature and humidity ratio

**Solution:**

Convert volume flows to mass flows (assuming v ≈ 13.33 ft³/lb for all):
```
ṁ₁ = 1,500 ÷ 13.33 = 113 lb/min
ṁ₂ = 2,200 ÷ 13.33 = 165 lb/min
ṁ₃ = 1,800 ÷ 13.33 = 135 lb/min
ṁ_total = 413 lb/min
```

From psychrometric chart:
- Zone 1 (73°F, 50% RH): W₁ = 0.0082 lb_w/lb_da
- Zone 2 (68°F, 45% RH): W₂ = 0.0065 lb_w/lb_da
- Zone 3 (77°F, 55% RH): W₃ = 0.0106 lb_w/lb_da

Mixed temperature:
```
T_mixed = (113 × 73 + 165 × 68 + 135 × 77) ÷ 413
T_mixed = (8,249 + 11,220 + 10,395) ÷ 413
T_mixed = 29,864 ÷ 413 = 72.3°F
```

Mixed humidity ratio:
```
W_mixed = (113 × 0.0082 + 165 × 0.0065 + 135 × 0.0106) ÷ 413
W_mixed = (0.927 + 1.073 + 1.431) ÷ 413
W_mixed = 3.431 ÷ 413 = 0.0083 lb_w/lb_da
```

Result: Mixed return air is 72.3°F, 0.0083 lb_w/lb_da (approximately 54% RH)

## Common Design Errors

### Volume Flow Assumption

**Error:** Assuming V̇₃ = V̇₁ + V̇₂

**Impact:** Can result in 5-15% error in airflow calculations, affecting fan sizing and energy consumption.

**Correction:** Always use mass flow rates for mixing calculations, then convert to volume using mixed air specific volume.

### Sensor Location

**Error:** Placing mixed air temperature sensor immediately downstream of mixing dampers

**Impact:** Sensor reads stratified air, not true mixed temperature, causing control instability and potential freeze damage.

**Correction:** Locate sensor minimum 5 duct diameters downstream or after fan/coil where turbulence ensures mixing.

### Minimum OA at Low Flow

**Error:** Using constant volume outdoor air damper with variable flow systems

**Impact:** Outdoor air percentage increases at low flow, causing overcooling, comfort issues, and energy waste.

**Correction:** Implement airflow tracking or mass balance control to maintain constant OA fraction across operating range.

### Freeze Protection Setpoint

**Error:** Using mixed air temperature setpoint below 40°F

**Impact:** Risk of coil freezing in coldest portions of non-uniform air stream.

**Correction:** Maintain minimum 40-45°F mixed air temperature; add preheat if necessary for economizer operation.

## Advanced Topics

### Psychrometric Mixing with Altitude

At elevations above sea level, use altitude-corrected psychrometric charts or adjust equations for barometric pressure:

```
W = 0.62198 × (p_w) / (p_atm - p_w)
```

Where p_atm varies with altitude per standard atmosphere equations.

### Mixing with Condensation

If mixed air conditions result in relative humidity > 100%, condensation occurs. The final state lies on the saturation line at mixed air enthalpy:

```
If φ_calculated > 100%, then:
- Final state: φ = 100% (saturated)
- T_final found at h_mixed on saturation curve
- Condensate mass = ṁ_total × (W_mixed,calculated - W_saturated)
```

### Energy Recovery Effectiveness

For energy recovery devices, the effective mixing considers heat exchanger effectiveness (ε):

```
T_oa,entering_coil = T_oa + ε × (T_ea - T_oa)
W_oa,entering_coil = W_oa + ε_latent × (W_ea - W_oa)
```

Where ε_latent may differ from sensible effectiveness.

## Summary

Psychrometric mixing analysis forms the foundation for:
- Economizer control and optimization
- Minimum outdoor air ventilation compliance
- Freeze protection strategies
- Energy recovery system design
- Multi-zone return air management

Proper application of mass and energy balance equations ensures accurate prediction of mixed air conditions, enabling precise HVAC system control and energy-efficient operation. Understanding the graphical representation on psychrometric charts provides intuitive verification of calculations and aids in troubleshooting control issues.

The linear relationship of mixing processes on the psychrometric chart—combined with the lever rule for locating mixed states—makes this one of the most straightforward psychrometric processes to analyze. However, careful attention to mass flow rates versus volume flow rates, proper sensor placement, and stratification prevention remains essential for successful implementation in real HVAC systems.
