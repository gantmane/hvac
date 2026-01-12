---
title: "Thermodynamic Tables Detailed"
description: "Comprehensive guide to refrigerant thermodynamic property tables including saturation, superheated vapor, and subcooled liquid tables with interpolation methods and digital database applications for HVAC system analysis"
weight: 10
---

Thermodynamic property tables constitute the primary reference tool for refrigeration cycle analysis, equipment selection, and performance evaluation. These tables provide experimentally verified thermophysical data for refrigerants across operating ranges encountered in HVAC applications.

## Table Categories and Structure

Refrigerant property tables organize data into three fundamental categories based on thermodynamic state:

**Saturation Tables**

Saturation tables present properties at liquid-vapor equilibrium conditions. Two organizational formats exist:

- Temperature-based tables list properties at specified saturation temperatures with corresponding saturation pressures
- Pressure-based tables list properties at specified saturation pressures with corresponding saturation temperatures

Each entry provides:
- Saturation temperature (T_sat) and pressure (P_sat)
- Specific volume of saturated liquid (v_f) and saturated vapor (v_g)
- Specific enthalpy of saturated liquid (h_f) and saturated vapor (h_g)
- Specific entropy of saturated liquid (s_f) and saturated vapor (s_g)
- Enthalpy of vaporization (h_fg = h_g - h_f)
- Entropy of vaporization (s_fg = s_g - s_f)

**Superheated Vapor Tables**

Superheated vapor tables present properties for vapor at temperatures exceeding saturation temperature for a given pressure. Tables organize data by pressure, with temperature as the secondary parameter. Properties listed include:

- Temperature (T)
- Specific volume (v)
- Specific enthalpy (h)
- Specific entropy (s)

**Subcooled Liquid Tables**

Subcooled (compressed) liquid tables provide properties for liquid below saturation temperature at specified pressures. Due to minimal pressure effects on liquid properties, subcooled liquid data often approximates saturated liquid properties at the same temperature.

## Property Table Application

### Cycle State Point Analysis

Refrigeration cycle analysis requires determining thermodynamic properties at four key state points:

1. **Evaporator outlet (compressor inlet):** Typically saturated or slightly superheated vapor
2. **Compressor discharge:** Superheated vapor at elevated pressure and temperature
3. **Condenser outlet (expansion device inlet):** Subcooled liquid at condensing pressure
4. **Evaporator inlet:** Two-phase mixture after isenthalpic expansion

For two-phase mixtures, properties calculate using quality (x):

Property = (1-x) × property_f + x × property_g

Where x represents vapor mass fraction (dryness fraction).

### Performance Calculations

Property tables enable quantitative analysis of refrigeration system performance:

**Refrigeration Effect:**
q_e = h_1 - h_4

Where h_1 is evaporator outlet enthalpy and h_4 is evaporator inlet enthalpy.

**Compressor Work:**
w_c = h_2 - h_1

Where h_2 is compressor discharge enthalpy and h_1 is compressor inlet enthalpy.

**Coefficient of Performance:**
COP = q_e / w_c

## Interpolation Techniques

Property values between tabulated points require interpolation. Linear interpolation provides acceptable accuracy for most HVAC applications.

### Single Variable Interpolation

For property P at intermediate value x between tabulated points x_1 and x_2:

P = P_1 + (P_2 - P_1) × (x - x_1) / (x_2 - x_1)

### Double Interpolation

Superheated vapor properties often require double interpolation when both pressure and temperature fall between tabulated values. Perform interpolation in two stages:

1. Interpolate at constant pressure for both bounding pressures
2. Interpolate between results at constant temperature

This sequential approach maintains thermodynamic consistency.

## Sample Property Data - R-134a

### Saturation Table (Temperature Basis)

| T (°C) | P_sat (kPa) | v_f (m³/kg) | v_g (m³/kg) | h_f (kJ/kg) | h_fg (kJ/kg) | h_g (kJ/kg) | s_f (kJ/kg·K) | s_g (kJ/kg·K) |
|--------|-------------|-------------|-------------|-------------|--------------|-------------|---------------|---------------|
| -40    | 51.25       | 0.0007055   | 0.3569      | 154.77      | 224.50       | 379.27      | 0.7937        | 1.7665        |
| -20    | 132.82      | 0.0007363   | 0.1424      | 173.75      | 213.22       | 386.97      | 0.8980        | 1.7395        |
| 0      | 292.82      | 0.0007703   | 0.0693      | 200.00      | 198.63       | 398.63      | 1.0000        | 1.7150        |
| 20     | 572.07      | 0.0008122   | 0.0361      | 227.03      | 181.12       | 408.15      | 1.1013        | 1.6923        |
| 40     | 1017.0      | 0.0008697   | 0.0199      | 256.54      | 159.85       | 416.39      | 1.2042        | 1.6695        |

### Superheated Vapor Table - R-134a at 200 kPa

| T (°C) | v (m³/kg) | h (kJ/kg) | s (kJ/kg·K) |
|--------|-----------|-----------|-------------|
| -10    | 0.0993    | 392.01    | 1.7506      |
| 0      | 0.1032    | 400.96    | 1.7805      |
| 10     | 0.1070    | 410.12    | 1.8095      |
| 20     | 0.1107    | 419.47    | 1.8377      |
| 30     | 0.1144    | 429.00    | 1.8652      |
| 40     | 0.1181    | 438.71    | 1.8920      |

### Superheated Vapor Table - R-134a at 800 kPa

| T (°C) | v (m³/kg) | h (kJ/kg) | s (kJ/kg·K) |
|--------|-----------|-----------|-------------|
| 40     | 0.0263    | 425.56    | 1.7207      |
| 50     | 0.0275    | 435.15    | 1.7479      |
| 60     | 0.0286    | 444.89    | 1.7741      |
| 70     | 0.0298    | 454.79    | 1.7996      |
| 80     | 0.0309    | 464.86    | 1.8244      |
| 90     | 0.0320    | 475.09    | 1.8486      |

## Digital Property Databases

Modern refrigerant property determination increasingly relies on digital databases and calculation engines rather than printed tables.

### REFPROP (Reference Fluid Thermodynamic and Transport Properties)

NIST REFPROP represents the industry-standard reference for refrigerant properties. The database implements high-accuracy equations of state and provides:

- Properties for pure refrigerants and mixtures
- Extended property ranges including metastable regions
- Transport properties (viscosity, thermal conductivity)
- Surface tension and dielectric constant
- Uncertainty estimates for calculated values

### CoolProp

CoolProp provides open-source thermophysical property calculations with accuracy approaching REFPROP. Integration capabilities include:

- Python, MATLAB, Excel, and C++ interfaces
- Web-based calculation tools
- EES (Engineering Equation Solver) compatibility
- Mobile applications for field use

### Equation of State Implementation

Digital databases calculate properties from fundamental equations of state rather than storing tabulated values. The Helmholtz energy equation of state provides the foundation:

α(τ,δ) = α⁰(τ,δ) + α^r(τ,δ)

Where:
- τ = T_c/T (inverse reduced temperature)
- δ = ρ/ρ_c (reduced density)
- α⁰ represents ideal gas contribution
- α^r represents residual contribution

All thermodynamic properties derive from this fundamental relation through partial derivatives, ensuring thermodynamic consistency.

## Table Accuracy and Uncertainty

Property table accuracy depends on experimental measurement precision and equation of state fitting quality.

### Uncertainty Levels

Typical uncertainties for well-characterized refrigerants:

| Property | Saturated Liquid | Saturated Vapor | Superheated Vapor |
|----------|------------------|-----------------|-------------------|
| Pressure | ±0.1%           | ±0.1%          | ±0.1%            |
| Density  | ±0.1%           | ±0.2%          | ±0.3%            |
| Enthalpy | ±0.5%           | ±0.5%          | ±1.0%            |
| Entropy  | ±0.5%           | ±0.5%          | ±1.0%            |

These uncertainties compound in cycle calculations, particularly for small temperature differences.

## Practical Application Guidelines

**State Point Identification:**
Determine whether the state is compressed liquid, saturated mixture, or superheated vapor before selecting the appropriate table.

**Pressure-Temperature Consistency:**
For saturated states, pressure and temperature are dependent properties. Specifying both independently may lead to thermodynamic inconsistencies.

**Quality Calculation:**
For two-phase regions, calculate quality from:
x = (h - h_f) / h_fg  or  x = (s - s_f) / s_fg

Quality must fall between 0 (saturated liquid) and 1 (saturated vapor).

**Unit Consistency:**
Verify unit consistency throughout calculations. Property tables use SI units (kPa, kJ/kg, m³/kg), but field measurements often use alternative units requiring conversion.

**Reference State:**
Enthalpy and entropy values are relative to an arbitrary reference state. Different table sources may use different reference states, affecting absolute values but not differences used in cycle calculations.
