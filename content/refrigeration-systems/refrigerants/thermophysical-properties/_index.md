---
title: "Thermophysical Properties"
description: "Comprehensive analysis of refrigerant thermophysical properties including critical point data, saturation properties, transport properties, and property relationships for refrigeration cycle design and analysis"
weight: 2
---

Thermophysical properties define the fundamental behavior of refrigerants across the full range of operating conditions. These properties govern heat transfer rates, pressure drops, compressor work requirements, and system efficiency. Accurate property data is essential for refrigeration cycle calculations, heat exchanger design, and system performance prediction.

## Critical Point Properties

The critical point represents the highest temperature and pressure at which distinct liquid and vapor phases can coexist. Above the critical point, the substance exists as a supercritical fluid with properties intermediate between liquid and gas.

### Critical Temperature

Critical temperature (T_c) defines the maximum temperature at which a substance can exist as a liquid regardless of pressure applied. This property fundamentally limits the high-side operating conditions in refrigeration cycles.

**Common Refrigerants:**

| Refrigerant | Critical Temperature (°C) | Critical Temperature (°F) | Critical Temperature (K) |
|-------------|---------------------------|---------------------------|--------------------------|
| R-22        | 96.1                      | 205.0                     | 369.3                    |
| R-134a      | 101.1                     | 214.0                     | 374.2                    |
| R-410A      | 72.1                      | 161.8                     | 345.3                    |
| R-32        | 78.1                      | 172.6                     | 351.3                    |
| R-290 (Propane) | 96.7                  | 206.1                     | 369.8                    |
| R-600a (Isobutane) | 134.7              | 274.5                     | 407.8                    |
| R-717 (Ammonia) | 132.3                 | 270.1                     | 405.4                    |
| R-744 (CO₂) | 31.0                      | 87.8                      | 304.1                    |

### Critical Pressure

Critical pressure (P_c) is the vapor pressure at the critical temperature. This represents the minimum pressure required to liquefy a gas at its critical temperature.

| Refrigerant | Critical Pressure (kPa) | Critical Pressure (psia) | Critical Pressure (bar) |
|-------------|-------------------------|--------------------------|-------------------------|
| R-22        | 4,990                   | 723.8                    | 49.9                    |
| R-134a      | 4,059                   | 588.7                    | 40.6                    |
| R-410A      | 4,902                   | 711.0                    | 49.0                    |
| R-32        | 5,782                   | 838.6                    | 57.8                    |
| R-290       | 4,251                   | 616.5                    | 42.5                    |
| R-600a      | 3,629                   | 526.3                    | 36.3                    |
| R-717       | 11,333                  | 1,644                    | 113.3                   |
| R-744       | 7,377                   | 1,070                    | 73.8                    |

### Critical Density and Volume

Critical density (ρ_c) represents the density at the critical point where liquid and vapor densities converge. Critical specific volume (v_c) is the reciprocal of critical density.

| Refrigerant | Critical Density (kg/m³) | Critical Specific Volume (m³/kg) |
|-------------|--------------------------|----------------------------------|
| R-22        | 523.8                    | 0.00191                          |
| R-134a      | 511.9                    | 0.00195                          |
| R-410A      | 489.0                    | 0.00205                          |
| R-32        | 424.0                    | 0.00236                          |
| R-717       | 225.0                    | 0.00444                          |
| R-744       | 467.6                    | 0.00214                          |

## Reference State Properties

### Triple Point

The triple point defines the unique temperature and pressure at which solid, liquid, and vapor phases coexist in thermodynamic equilibrium.

| Refrigerant | Triple Point Temperature (°C) | Triple Point Pressure (kPa) |
|-------------|-------------------------------|----------------------------|
| R-134a      | -103.3                        | 0.39                       |
| R-32        | -136.8                        | 0.048                      |
| R-717       | -77.7                         | 6.08                       |
| R-744       | -56.6 (sublimation point)     | 518.0                      |

### Normal Boiling Point

Normal boiling point (NBP) is the saturation temperature at standard atmospheric pressure (101.325 kPa). This property indicates the temperature level at which the refrigerant operates in atmospheric conditions.

| Refrigerant | NBP at 101.325 kPa (°C) | NBP at 101.325 kPa (°F) |
|-------------|-------------------------|-------------------------|
| R-22        | -40.8                   | -41.4                   |
| R-134a      | -26.1                   | -15.0                   |
| R-410A      | -51.4                   | -60.5                   |
| R-32        | -51.7                   | -61.1                   |
| R-290       | -42.1                   | -43.8                   |
| R-717       | -33.3                   | -28.0                   |
| R-744       | -78.4 (sublimation)     | -109.1                  |

## Saturation Properties

Saturation properties define the relationship between temperature and pressure along the phase equilibrium boundary. These properties are fundamental to refrigeration cycle analysis.

### Vapor Pressure Relationship

Vapor pressure as a function of temperature follows the Clausius-Clapeyron relationship:

**ln(P) = A - B/(T + C)**

Where:
- P = vapor pressure (kPa)
- T = temperature (°C)
- A, B, C = refrigerant-specific constants

More accurate representations use the extended Antoine equation or REFPROP correlations with multiple terms.

### Pressure-Temperature Tables

Representative saturation data for R-134a:

| Temperature (°C) | Pressure (kPa) | Pressure (psia) | Liquid Density (kg/m³) | Vapor Density (kg/m³) |
|------------------|----------------|-----------------|------------------------|----------------------|
| -40              | 51.2           | 7.43            | 1418.0                 | 2.773                |
| -30              | 84.4           | 12.24           | 1394.0                 | 4.394                |
| -20              | 133.7          | 19.39           | 1371.0                 | 6.753                |
| -10              | 201.7          | 29.25           | 1347.0                 | 10.07                |
| 0                | 293.0          | 42.50           | 1322.0                 | 14.61                |
| 10               | 414.9          | 60.17           | 1296.0                 | 20.77                |
| 20               | 572.1          | 82.97           | 1269.0                 | 28.98                |
| 30               | 770.6          | 111.8           | 1240.0                 | 39.77                |
| 40               | 1017.0         | 147.5           | 1208.0                 | 53.84                |
| 50               | 1318.0         | 191.2           | 1173.0                 | 72.15                |

### Latent Heat of Vaporization

Latent heat of vaporization (h_fg) represents the energy required to convert liquid to vapor at constant temperature and pressure. This property directly affects refrigeration system capacity.

**h_fg = h_g - h_f**

Where:
- h_fg = latent heat of vaporization (kJ/kg)
- h_g = enthalpy of saturated vapor (kJ/kg)
- h_f = enthalpy of saturated liquid (kJ/kg)

Latent heat decreases with increasing temperature and becomes zero at the critical point.

**R-134a Latent Heat Data:**

| Temperature (°C) | Latent Heat (kJ/kg) | Latent Heat (Btu/lb) |
|------------------|---------------------|----------------------|
| -40              | 216.7               | 93.2                 |
| -20              | 207.4               | 89.2                 |
| 0                | 198.0               | 85.1                 |
| 20               | 187.5               | 80.6                 |
| 40               | 175.6               | 75.5                 |
| 60               | 161.5               | 69.4                 |
| 80               | 144.1               | 62.0                 |
| 100              | 120.3               | 51.7                 |

**Temperature dependence approximation:**

h_fg ≈ h_fg,0 × (1 - T_r)^n

Where:
- T_r = reduced temperature = T/T_c
- n ≈ 0.38 for many refrigerants
- h_fg,0 = latent heat at reference condition

## Specific Heat Capacities

Specific heat capacity quantifies the energy required to change the temperature of a substance by one degree.

### Liquid Specific Heat (c_p,f)

Liquid specific heat remains relatively constant over moderate temperature ranges and increases slightly with temperature.

| Refrigerant | c_p,f at 25°C (kJ/kg·K) | c_p,f at 25°C (Btu/lb·°F) |
|-------------|-------------------------|---------------------------|
| R-22        | 1.267                   | 0.303                     |
| R-134a      | 1.434                   | 0.343                     |
| R-410A      | 1.845                   | 0.441                     |
| R-32        | 2.010                   | 0.480                     |
| R-717       | 4.700                   | 1.123                     |
| R-744       | 3.140                   | 0.750                     |

### Vapor Specific Heat (c_p,g)

Vapor specific heat varies significantly with temperature and pressure. At low pressures, ideal gas behavior approximates vapor properties.

**Ideal gas specific heat correlation:**

c_p = A + BT + CT² + DT³

Where T is absolute temperature and A, B, C, D are refrigerant-specific constants.

| Refrigerant | c_p,g at 25°C, 101.325 kPa (kJ/kg·K) | c_p,g at 25°C (Btu/lb·°F) |
|-------------|--------------------------------------|---------------------------|
| R-22        | 0.658                                | 0.157                     |
| R-134a      | 0.852                                | 0.204                     |
| R-410A      | 0.901                                | 0.215                     |
| R-32        | 0.823                                | 0.197                     |
| R-717       | 2.177                                | 0.520                     |
| R-744       | 0.846                                | 0.202                     |

### Specific Heat Ratio

The specific heat ratio (γ = c_p/c_v) affects compression processes and sound velocity.

**For ideal gas:**

c_p - c_v = R

Where R is the specific gas constant.

| Refrigerant | γ at 25°C, low pressure |
|-------------|-------------------------|
| R-134a      | 1.127                   |
| R-410A      | 1.175                   |
| R-717       | 1.310                   |
| R-744       | 1.289                   |

## Thermal Conductivity

Thermal conductivity (k) governs conductive heat transfer rates and affects heat exchanger performance.

### Liquid Thermal Conductivity

Liquid thermal conductivity decreases with increasing temperature as molecular spacing increases.

| Refrigerant | k_f at 25°C (W/m·K) | k_f at 25°C (Btu/h·ft·°F) |
|-------------|---------------------|---------------------------|
| R-22        | 0.0829              | 0.0479                    |
| R-134a      | 0.0808              | 0.0467                    |
| R-410A      | 0.0923              | 0.0533                    |
| R-32        | 0.1350              | 0.0780                    |
| R-717       | 0.5230              | 0.3022                    |
| R-744       | 0.1090              | 0.0630                    |

**Temperature correlation for liquids:**

k_f = k_f,0 × (1 - T_r)^0.38

Where T_r is reduced temperature (T/T_c).

### Vapor Thermal Conductivity

Vapor thermal conductivity increases with temperature due to increased molecular activity.

| Refrigerant | k_g at 25°C, 101.325 kPa (W/m·K) | k_g at 25°C (Btu/h·ft·°F) |
|-------------|----------------------------------|---------------------------|
| R-22        | 0.01095                          | 0.00633                   |
| R-134a      | 0.01327                          | 0.00767                   |
| R-410A      | 0.01431                          | 0.00827                   |
| R-32        | 0.01488                          | 0.00860                   |
| R-717       | 0.02542                          | 0.01469                   |
| R-744       | 0.01677                          | 0.00969                   |

**Vapor thermal conductivity increases with pressure and approaches liquid values near the critical point.**

## Viscosity Properties

Viscosity quantifies flow resistance and determines pressure drops in piping and heat exchangers.

### Dynamic Viscosity

Dynamic (absolute) viscosity (μ) relates shear stress to velocity gradient in flowing fluids.

**Liquid Dynamic Viscosity:**

| Refrigerant | μ_f at 25°C (μPa·s) | μ_f at 25°C (cP) | μ_f at 25°C (lb/ft·h) |
|-------------|---------------------|------------------|-----------------------|
| R-22        | 166                 | 0.166            | 0.401                 |
| R-134a      | 196                 | 0.196            | 0.473                 |
| R-410A      | 139                 | 0.139            | 0.336                 |
| R-32        | 110                 | 0.110            | 0.266                 |
| R-717       | 152                 | 0.152            | 0.367                 |
| R-744       | 75                  | 0.075            | 0.181                 |

Liquid viscosity decreases exponentially with temperature:

μ_f = A × exp(B/T)

**Vapor Dynamic Viscosity:**

| Refrigerant | μ_g at 25°C, 101.325 kPa (μPa·s) | μ_g at 25°C (cP) |
|-------------|----------------------------------|------------------|
| R-22        | 12.3                             | 0.0123           |
| R-134a      | 11.8                             | 0.0118           |
| R-410A      | 12.6                             | 0.0126           |
| R-32        | 12.9                             | 0.0129           |
| R-717       | 10.2                             | 0.0102           |
| R-744       | 15.0                             | 0.0150           |

Vapor viscosity increases with temperature following power law relationships.

### Kinematic Viscosity

Kinematic viscosity (ν = μ/ρ) represents the ratio of dynamic viscosity to density and appears in Reynolds number calculations.

ν = μ/ρ

Units: m²/s, cSt (centistokes), ft²/h

## Density Relationships

Density varies significantly with temperature and pressure, particularly for vapors.

### Liquid Density Temperature Dependence

Liquid density decreases linearly with temperature over moderate ranges:

ρ_f = ρ_f,0 × [1 - β(T - T_0)]

Where β is the volumetric thermal expansion coefficient (typically 0.002-0.003 K⁻¹ for refrigerants).

**More accurate correlation:**

ρ_f = ρ_c × (A + B×T_r^(1/3) + C×T_r^(2/3) + D×T_r)

Where T_r is reduced temperature.

### Vapor Density

At low pressures, vapor density approximates ideal gas behavior:

ρ_g = P/(R×T)

Where:
- P = absolute pressure
- R = specific gas constant
- T = absolute temperature

At higher pressures, compressibility factor (Z) corrections are required:

ρ_g = P/(Z×R×T)

### Two-Phase Density

In two-phase flow regions, effective density depends on vapor quality (x) and flow pattern:

**Homogeneous model:**

ρ_tp = 1/[(x/ρ_g) + ((1-x)/ρ_f)]

**Separated flow:**

ρ_tp = α×ρ_g + (1-α)×ρ_f

Where α is void fraction (volume fraction occupied by vapor).

## Surface Tension

Surface tension (σ) affects bubble formation, droplet behavior, and two-phase flow patterns.

| Refrigerant | σ at 25°C (mN/m) | σ at 25°C (dyn/cm) |
|-------------|------------------|---------------------|
| R-22        | 7.80             | 7.80                |
| R-134a      | 8.05             | 8.05                |
| R-410A      | 6.12             | 6.12                |
| R-32        | 9.45             | 9.45                |
| R-717       | 23.4             | 23.4                |
| R-744       | 2.47             | 2.47                |

Surface tension decreases linearly with temperature and becomes zero at the critical point:

σ = σ_0 × (1 - T_r)^n

Where n ≈ 1.26 for most refrigerants.

## Pressure-Enthalpy Diagrams

Pressure-enthalpy (P-h) diagrams provide graphical representation of refrigerant properties and enable visualization of refrigeration cycles.

### Diagram Features

**Key regions:**
- Subcooled liquid region (left of saturated liquid line)
- Two-phase region (between saturated liquid and saturated vapor lines)
- Superheated vapor region (right of saturated vapor line)
- Supercritical region (above critical point)

**Constant property lines:**
- Isotherms (constant temperature)
- Isentropes (constant entropy)
- Isochores (constant specific volume)
- Constant quality lines (in two-phase region)

### Refrigeration Cycle on P-h Diagram

Standard vapor-compression cycle states:

1. **Evaporator inlet:** Low pressure, low quality two-phase mixture
2. **Evaporator outlet:** Low pressure, saturated or superheated vapor
3. **Compressor outlet:** High pressure, superheated vapor
4. **Condenser outlet:** High pressure, saturated or subcooled liquid
5. **Expansion device outlet:** Low pressure, low quality two-phase mixture (returns to state 1)

### Using P-h Diagrams for Calculations

**Refrigeration capacity:**

Q_evap = m × (h_2 - h_1)

Where:
- m = mass flow rate
- h_2 = enthalpy at evaporator outlet
- h_1 = enthalpy at evaporator inlet

**Compressor work:**

W_comp = m × (h_3 - h_2)

**Coefficient of Performance:**

COP = Q_evap / W_comp = (h_2 - h_1) / (h_3 - h_2)

## Property Tables and Data Sources

### ASHRAE Fundamentals

ASHRAE Fundamentals Handbook provides comprehensive refrigerant property tables including:
- Saturation properties (temperature and pressure tables)
- Superheated vapor properties
- Compressed liquid properties
- Transport properties

### REFPROP Database

NIST REFPROP (Reference Fluid Thermodynamic and Transport Properties Database) offers the most accurate property calculations using:
- High-accuracy equations of state
- Helmholtz energy formulations
- Validated experimental data correlations

### Property Calculation Methods

**Equations of State:**

Complex multi-parameter equations relate pressure, temperature, and density:

P = f(ρ, T)

Common formulations:
- Modified Benedict-Webb-Rubin (MBWR) equation
- Helmholtz energy explicit in temperature and density
- Peng-Robinson equation (simplified, lower accuracy)

**Transport Property Correlations:**

Thermal conductivity and viscosity require separate correlation frameworks based on kinetic theory and experimental data.

## Temperature and Pressure Effects

### Pressure Effects on Properties

**Liquid properties:** Relatively insensitive to pressure changes
- Density increases slightly with pressure (typically <1% per 1000 kPa)
- Thermal conductivity essentially independent of pressure
- Viscosity slightly increases with pressure

**Vapor properties:** Strongly pressure-dependent
- Density proportional to pressure (ideal gas approximation)
- Thermal conductivity increases with pressure
- Viscosity increases with pressure
- Specific heat increases significantly near critical pressure

### Temperature Effects on Properties

**General trends with increasing temperature:**
- Liquid density decreases
- Vapor density decreases (at constant pressure)
- Liquid viscosity decreases
- Vapor viscosity increases
- Latent heat decreases
- Surface tension decreases
- Specific heat of vapor increases

## Engineering Applications

### Heat Transfer Calculations

Convective heat transfer coefficients depend on thermal conductivity, specific heat, density, and viscosity through dimensionless groups:

**Nusselt number:**

Nu = h×L/k

**Reynolds number:**

Re = ρ×V×L/μ

**Prandtl number:**

Pr = (μ×c_p)/k

### Pressure Drop Calculations

Pressure drop in piping depends on density and viscosity:

**Darcy-Weisbach equation:**

ΔP = f × (L/D) × (ρ×V²/2)

Where f is the friction factor dependent on Reynolds number and relative roughness.

### Compressor Performance

Isentropic compression work depends on specific heat ratio and pressure ratio:

**For ideal gas:**

W_s = (c_p×T_1) × [(P_2/P_1)^((γ-1)/γ) - 1]

Real refrigerant properties deviate from ideal gas behavior, requiring property table lookups or equation of state calculations.

## Property Uncertainty and Accuracy

### Measurement Uncertainty

Typical uncertainties in experimental property measurements:
- Temperature: ±0.01 to ±0.05 K
- Pressure: ±0.1% to ±0.5%
- Density: ±0.1% to ±0.5%
- Thermal conductivity: ±2% to ±5%
- Viscosity: ±2% to ±5%

### Correlation Accuracy

Modern equations of state (REFPROP) achieve:
- Vapor pressure: ±0.1% to ±0.5%
- Liquid density: ±0.1% to ±0.2%
- Vapor density: ±0.2% to ±1%
- Heat capacity: ±1% to ±2%
- Sound velocity: ±0.1% to ±0.5%

Transport property correlations typically achieve ±3% to ±5% accuracy compared to experimental data.
