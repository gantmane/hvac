---
title: "Refrigerant Property Tables"
description: "Comprehensive refrigerant property tables for saturation, superheat, and subcooled conditions. Essential thermodynamic data for HVAC system design, refrigeration cycle analysis, and equipment performance calculations."
weight: 1
---

Refrigerant property tables provide tabulated thermodynamic and transport properties essential for vapor compression cycle analysis, system design, and performance evaluation. These tables eliminate the need for complex equation-of-state calculations by presenting pre-calculated property values at standard conditions.

## Table Organization and Structure

Property tables organize refrigerant data into three primary categories based on thermodynamic state:

**Saturation Tables** present properties at the liquid-vapor phase boundary where temperature and pressure are dependent variables. Each saturation table lists properties for both saturated liquid (subscript f) and saturated vapor (subscript g) states.

**Superheated Vapor Tables** provide properties for vapor at temperatures exceeding the saturation temperature for a given pressure. These tables organize data by pressure, with temperature as the secondary variable.

**Subcooled Liquid Tables** contain properties for liquid below the saturation temperature at a given pressure. Many applications approximate subcooled liquid properties using saturated liquid values at the actual liquid temperature due to minimal variation.

## Saturation Property Tables

Saturation tables present properties along the phase dome where liquid and vapor coexist in equilibrium. Tables may be organized by either temperature or pressure as the independent variable.

### Temperature-Based Saturation Tables

Temperature-based tables list saturation pressure and properties at specified temperatures:

| Temperature (°C) | Pressure (kPa) | vf (m³/kg) | vg (m³/kg) | hf (kJ/kg) | hfg (kJ/kg) | hg (kJ/kg) | sf (kJ/kg·K) | sg (kJ/kg·K) |
|-----------------|----------------|------------|------------|------------|-------------|------------|--------------|--------------|
| -40 | 51.2 | 0.000708 | 0.3569 | 144.0 | 246.2 | 390.2 | 0.7532 | 1.7395 |
| -20 | 132.8 | 0.000732 | 0.1409 | 172.8 | 232.4 | 405.2 | 0.8759 | 1.7153 |
| 0 | 293.0 | 0.000758 | 0.0672 | 200.0 | 218.0 | 418.0 | 0.9876 | 1.6984 |
| 20 | 572.1 | 0.000787 | 0.0354 | 227.5 | 202.5 | 430.0 | 1.0927 | 1.6872 |
| 40 | 1017.0 | 0.000820 | 0.0198 | 255.8 | 185.2 | 441.0 | 1.1935 | 1.6803 |

Properties listed include:
- **vf, vg**: Specific volume of saturated liquid and vapor (m³/kg)
- **hf, hfg, hg**: Enthalpy of saturated liquid, enthalpy of vaporization, and enthalpy of saturated vapor (kJ/kg)
- **sf, sg**: Entropy of saturated liquid and vapor (kJ/kg·K)

The enthalpy of vaporization (hfg) represents the latent heat required for phase change and decreases with increasing temperature, reaching zero at the critical point.

### Pressure-Based Saturation Tables

Pressure-based tables provide saturation temperature and properties at specified pressures, particularly useful for analyzing components where pressure is the known variable:

| Pressure (kPa) | Temp (°C) | vf (m³/kg) | vg (m³/kg) | hf (kJ/kg) | hg (kJ/kg) | sf (kJ/kg·K) | sg (kJ/kg·K) |
|----------------|-----------|------------|------------|------------|------------|--------------|--------------|
| 100 | -26.4 | 0.000722 | 0.1928 | 165.4 | 400.8 | 0.8422 | 1.7249 |
| 200 | -12.7 | 0.000744 | 0.0993 | 184.5 | 410.9 | 0.9281 | 1.7089 |
| 500 | 15.7 | 0.000781 | 0.0407 | 222.1 | 428.0 | 1.0753 | 1.6908 |
| 1000 | 39.4 | 0.000819 | 0.0200 | 254.5 | 440.4 | 1.1903 | 1.6814 |
| 2000 | 67.5 | 0.000880 | 0.0095 | 293.2 | 451.8 | 1.3254 | 1.6713 |

## Superheated Vapor Tables

Superheated vapor exists at temperatures above saturation for a given pressure. Tables organize data by pressure sections, with temperature increments within each section.

### Table Structure

For each pressure level, properties are listed at various superheat temperatures:

**At P = 200 kPa (Tsat = -12.7°C):**

| Temperature (°C) | v (m³/kg) | h (kJ/kg) | s (kJ/kg·K) | cp (kJ/kg·K) | μ (μPa·s) | k (mW/m·K) |
|-----------------|-----------|-----------|-------------|-------------|----------|------------|
| -10 (2.7 K SH) | 0.1012 | 412.3 | 1.7149 | 0.788 | 11.2 | 10.8 |
| 0 | 0.1065 | 420.5 | 1.7488 | 0.802 | 11.6 | 11.3 |
| 20 | 0.1166 | 437.2 | 1.8145 | 0.828 | 12.4 | 12.3 |
| 40 | 0.1264 | 454.5 | 1.8773 | 0.856 | 13.2 | 13.4 |
| 60 | 0.1360 | 472.3 | 1.9377 | 0.886 | 14.0 | 14.5 |

**At P = 500 kPa (Tsat = 15.7°C):**

| Temperature (°C) | v (m³/kg) | h (kJ/kg) | s (kJ/kg·K) | cp (kJ/kg·K) |
|-----------------|-----------|-----------|-------------|-------------|
| 20 (4.3 K SH) | 0.0415 | 429.8 | 1.6993 | 0.812 |
| 40 | 0.0456 | 449.1 | 1.7639 | 0.848 |
| 60 | 0.0495 | 468.2 | 1.8252 | 0.882 |
| 80 | 0.0533 | 487.6 | 1.8838 | 0.916 |

Transport properties (viscosity μ, thermal conductivity k) enable heat transfer and pressure drop calculations for heat exchangers and piping systems.

## Subcooled Liquid Properties

Subcooled liquid tables provide properties below saturation temperature at elevated pressures. Liquid properties vary minimally with pressure, so compressed liquid data is often limited.

### Approximation Methods

For most HVAC applications, subcooled liquid properties are approximated using saturated liquid values at the actual liquid temperature:

**Method 1: Temperature-Based Approximation**
```
h_subcooled(T, P) ≈ hf(T)
v_subcooled(T, P) ≈ vf(T)
s_subcooled(T, P) ≈ sf(T)
```

**Method 2: Pressure Correction**

For higher accuracy when significant subcooling exists:
```
h_subcooled = hf(T) + vf(T) × [P - Psat(T)]
```

This correction accounts for compression work, typically negligible for liquids but relevant at high pressure differences exceeding 1000 kPa.

### Example Subcooled Liquid Table

**At T = 20°C (Psat = 572.1 kPa):**

| Pressure (kPa) | v (m³/kg) | h (kJ/kg) | s (kJ/kg·K) |
|----------------|-----------|-----------|-------------|
| 600 | 0.000787 | 227.5 | 1.0927 |
| 1000 | 0.000787 | 227.8 | 1.0925 |
| 2000 | 0.000786 | 228.6 | 1.0921 |
| 5000 | 0.000784 | 230.5 | 1.0911 |

The minimal variation demonstrates why simplified approximations are acceptable for most refrigeration calculations.

## Table Interpolation Methods

Refrigerant properties at conditions between tabulated values require interpolation. Linear interpolation provides sufficient accuracy for most engineering calculations.

### Linear Interpolation

For a property y at value x between tabulated points (x₁, y₁) and (x₂, y₂):

```
y = y₁ + (y₂ - y₁) × [(x - x₁) / (x₂ - x₁)]
```

**Example: R-134a at P = 350 kPa**

Find saturation temperature between tabulated values at 300 kPa (0.7°C) and 400 kPa (8.9°C):

```
Tsat = 0.7 + (8.9 - 0.7) × [(350 - 300) / (400 - 300)]
Tsat = 0.7 + 8.2 × 0.5 = 4.8°C
```

### Double Interpolation

Superheated vapor properties require interpolation in both pressure and temperature dimensions.

**Step 1:** Interpolate at bounding pressures for the desired temperature.
**Step 2:** Interpolate between the results from Step 1 for the desired pressure.

**Example: R-134a enthalpy at P = 350 kPa, T = 30°C**

At P = 300 kPa, interpolate between T = 20°C (h = 433.8 kJ/kg) and T = 40°C (h = 451.2 kJ/kg):
```
h₁ = 433.8 + (451.2 - 433.8) × [(30 - 20) / (40 - 20)] = 442.5 kJ/kg
```

At P = 400 kPa, interpolate between T = 20°C (h = 432.1 kJ/kg) and T = 40°C (h = 449.8 kJ/kg):
```
h₂ = 432.1 + (449.8 - 432.1) × [(30 - 20) / (40 - 20)] = 440.95 kJ/kg
```

Final interpolation between pressures:
```
h = 442.5 + (440.95 - 442.5) × [(350 - 300) / (400 - 300)] = 441.73 kJ/kg
```

### Entropy Interpolation Considerations

Entropy interpolation requires care near the saturation dome where property gradients are steep. For states close to saturation (within 5 K superheat), use smaller interpolation intervals or refer to detailed property tables with finer resolution.

## Common Refrigerant Property Examples

### R-134a (HFC-134a, Tetrafluoroethane)

Most widely used refrigerant in automotive air conditioning and medium-temperature commercial refrigeration. Critical temperature: 101.1°C, Critical pressure: 4059 kPa.

**Key saturation points:**
- Evaporator condition: -20°C, 133 kPa, hfg = 232.4 kJ/kg
- Condenser condition: 40°C, 1017 kPa, hfg = 185.2 kJ/kg

### R-410A (HFC Blend: R-32/R-125)

Zeotropic blend for residential and light commercial air conditioning. Critical temperature: 72.8°C, Critical pressure: 4902 kPa.

**Saturation properties at 25°C:**
- Pressure: 1729 kPa
- hf: 93.4 kJ/kg
- hg: 422.2 kJ/kg
- Temperature glide: 0.1 K (near-azeotropic)

### R-22 (HCFC-22, Chlorodifluoromethane)

Legacy refrigerant being phased out under Montreal Protocol. Critical temperature: 96.1°C, Critical pressure: 4990 kPa.

**Standard rating conditions (ARI 550/590):**
- Evaporator: 4.4°C (40°F), 621 kPa
- Condenser: 54.4°C (130°F), 2088 kPa

### R-717 (Ammonia, NH₃)

Industrial refrigerant for cold storage and food processing. Critical temperature: 132.3°C, Critical pressure: 11333 kPa.

**Properties at -10°C:**
- Saturation pressure: 291 kPa
- hfg: 1319.2 kJ/kg (high latent heat)
- Specific volume ratio (vg/vf): 535:1

## Property Table Applications

### Refrigeration Cycle Analysis

Property tables enable calculation of cycle performance parameters:

**Coefficient of Performance (COP):**
```
COP = (h₁ - h₄) / (h₂ - h₁)
```
where subscripts denote cycle state points requiring table lookups.

**Compressor Work:**
```
w_comp = h₂ - h₁
```
Enthalpy values obtained from tables at compressor inlet (superheated vapor) and outlet (superheated vapor at elevated pressure).

**Evaporator Capacity:**
```
q_evap = ṁ × (h₁ - h₄)
```
Mass flow rate multiplied by enthalpy difference between evaporator inlet (low-quality mixture or subcooled liquid) and outlet (saturated or superheated vapor).

### Heat Exchanger Design

Property tables provide temperature-enthalpy relationships for LMTD (Log Mean Temperature Difference) and ε-NTU (Effectiveness-Number of Transfer Units) heat exchanger calculations.

Transport properties (thermal conductivity, viscosity) enable convection coefficient determination through dimensionless correlations (Nusselt, Reynolds, Prandtl numbers).

### System Charge Calculation

Refrigerant charge determination requires density (inverse of specific volume) at various system components:

**Total charge:**
```
m_total = V_liquid/vf + V_vapor/vg + m_receiver + m_piping
```

Tables provide specific volumes for liquid and vapor phases at operating conditions throughout the system.

## Digital Property Resources

Modern HVAC analysis increasingly relies on digital property databases accessed through:

**REFPROP (NIST Reference Fluid Properties):** Comprehensive database with equation-of-state calculations validated against experimental data for 147+ pure fluids and mixtures.

**CoolProp:** Open-source thermophysical property library with Python, MATLAB, and Excel interfaces. Implements high-accuracy equations of state for 122 pure and pseudo-pure fluids.

**EES (Engineering Equation Solver):** Integrated property database with built-in refrigerant functions enabling parametric studies and optimization.

Despite digital resources, printed tables remain valuable for field calculations, preliminary design, troubleshooting, and educational purposes where computational tools are unavailable or impractical.

## Table Usage Best Practices

**Verify Reference State:** Refrigerant property tables use different reference states (IIR, ASHRAE, NBP). Ensure consistent reference state when comparing values or combining data sources.

**Check Temperature Scale:** Confirm whether tables use Celsius or Fahrenheit. Many North American publications use dual-scale tables.

**Interpolation Limits:** Avoid extrapolation beyond tabulated ranges. Property equations lose accuracy outside experimental data boundaries.

**Mixture Considerations:** For zeotropic blends (R-407C, R-404A), account for temperature glide during phase change. Saturation tables list bubble point and dew point temperatures.

**Quality Region:** Properties in the two-phase region (0 < x < 1) are determined using quality:
```
h = hf + x × hfg
v = vf + x × vfg
s = sf + x × sfg
```

Accurate quality determination is essential for evaporator modeling and system simulation.
