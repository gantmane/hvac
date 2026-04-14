---
title: "Properties"
aliases: ["Properties"]
weight: 3
---

Thermodynamic properties define the state of a substance and govern energy transfer processes in HVAC systems. Understanding property classification, measurement, and calculation enables accurate system design and performance analysis.

## Property Classification

### Intensive Properties

Intensive properties are independent of system mass or extent. These properties remain constant when a system is divided:

**Common Intensive Properties:**
- Temperature (T)
- Pressure (P)
- Specific volume (v = V/m)
- Specific enthalpy (h = H/m)
- Specific entropy (s = S/m)
- Specific internal energy (u = U/m)
- Density (ρ = 1/v)
- Quality (x)

### Extensive Properties

Extensive properties scale proportionally with system mass or extent:

**Common Extensive Properties:**
- Mass (m)
- Volume (V)
- Total enthalpy (H)
- Total entropy (S)
- Total internal energy (U)

**Conversion Relationship:**
```
Specific Property = Extensive Property / Mass
v = V/m
h = H/m
s = S/m
```

## State Postulate

The state of a simple compressible substance is completely specified by two independent intensive properties. This fundamental principle enables property determination:

**Requirements:**
1. System must be in equilibrium
2. Properties must be independent
3. System must be simple compressible (no magnetic, electric, or surface tension effects)

**Common Property Pairs:**
- Temperature and pressure (T, P)
- Pressure and specific enthalpy (P, h)
- Temperature and specific entropy (T, s)
- Pressure and quality (P, x) for two-phase states

## Primary Thermodynamic Properties

### Internal Energy (u)

Molecular-scale energy of a substance, including kinetic and potential energy of molecules.

**Units:** kJ/kg, Btu/lbm

### Enthalpy (h)

Combined property representing total energy content:

```
h = u + Pv
```

Where:
- h = specific enthalpy (kJ/kg)
- u = specific internal energy (kJ/kg)
- P = absolute pressure (kPa)
- v = specific volume (m³/kg)

**Physical Meaning:** Enthalpy represents the energy required to create the substance and make room for it by displacing the environment.

### Entropy (s)

Measure of molecular disorder or energy dispersal.

**Units:** kJ/(kg·K), Btu/(lbm·°R)

**Second Law Relationship:**
```
ds ≥ δq/T
```

For reversible processes: ds = δq/T

### Specific Heats

**Constant Pressure (cp):**
```
cp = (∂h/∂T)P
```

**Constant Volume (cv):**
```
cv = (∂u/∂T)v
```

**Heat Capacity Ratio (k):**
```
k = cp/cv
```

| Substance | cp (kJ/kg·K) | cv (kJ/kg·K) | k |
|-----------|-------------|-------------|-----|
| Air (300 K) | 1.005 | 0.718 | 1.40 |
| R-134a vapor | 0.852 | 0.762 | 1.12 |
| Water vapor | 2.010 | 1.520 | 1.32 |
| Nitrogen | 1.039 | 0.743 | 1.40 |

## Equations of State

Equations relating pressure, temperature, and specific volume.

### Ideal Gas Law

```
Pv = RT
```

Where:
- P = absolute pressure (kPa)
- v = specific volume (m³/kg)
- R = specific gas constant (kJ/kg·K)
- T = absolute temperature (K)

**Gas Constant:**
```
R = R̄/M
```

R̄ = universal gas constant = 8.314 kJ/(kmol·K)
M = molar mass (kg/kmol)

**Valid When:**
- Low pressure (P < 1 MPa for most gases)
- High temperature (T > 2Tcritical)
- Gases far from saturation

### Van der Waals Equation

Corrects ideal gas law for molecular size and intermolecular forces:

```
(P + a/v²)(v - b) = RT
```

Where:
- a = attraction parameter
- b = molecular volume parameter

### Compressibility Factor (Z)

Measures deviation from ideal gas behavior:

```
Z = Pv/RT
```

- Z = 1: ideal gas behavior
- Z < 1: attractive forces dominate (common at moderate pressures)
- Z > 1: repulsive forces dominate (common at high pressures)

## Property Tables and Data Sources

### Saturated Property Tables

Organize properties along the saturation curve where liquid and vapor coexist.

**Table Entry Format:**

| T (°C) | Psat (kPa) | vf (m³/kg) | vg (m³/kg) | hf (kJ/kg) | hfg (kJ/kg) | hg (kJ/kg) | sf (kJ/kg·K) | sg (kJ/kg·K) |
|--------|-----------|-----------|-----------|-----------|------------|-----------|-------------|-------------|
| 0 | 0.6113 | 0.001000 | 206.14 | 0.00 | 2501.3 | 2501.3 | 0.0000 | 9.1562 |
| 20 | 2.339 | 0.001002 | 57.79 | 83.95 | 2454.1 | 2538.1 | 0.2966 | 8.6672 |
| 100 | 101.35 | 0.001044 | 1.6729 | 419.04 | 2257.0 | 2676.1 | 1.3069 | 7.3549 |

**Subscripts:**
- f = saturated liquid
- g = saturated vapor
- fg = difference (evaporation)

### Superheated Vapor Tables

Properties of vapor above saturation temperature at given pressure.

**Example: Superheated R-134a**

| P (kPa) | T (°C) | v (m³/kg) | h (kJ/kg) | s (kJ/kg·K) |
|---------|--------|----------|----------|-------------|
| 200 | 0 | 0.1080 | 398.8 | 1.7506 |
| 200 | 20 | 0.1151 | 412.2 | 1.8020 |
| 200 | 40 | 0.1220 | 425.9 | 1.8517 |
| 400 | 20 | 0.05641 | 407.5 | 1.7268 |
| 400 | 40 | 0.06009 | 421.6 | 1.7770 |

### Compressed Liquid Tables

Properties of liquid below saturation temperature at given pressure. Often approximated using saturated liquid properties at the same temperature.

## Refrigerant Properties

### Critical Properties

Properties at the critical point where liquid-vapor distinction vanishes.

| Refrigerant | Tcrit (°C) | Pcrit (kPa) | vcrit (m³/kg) | ODP | GWP |
|-------------|-----------|------------|--------------|-----|-----|
| R-134a | 101.06 | 4059 | 0.001970 | 0 | 1430 |
| R-410A | 71.34 | 4901 | 0.001790 | 0 | 2088 |
| R-32 | 78.11 | 5782 | 0.001890 | 0 | 675 |
| R-290 (Propane) | 96.74 | 4251 | 0.00456 | 0 | 3 |
| R-744 (CO₂) | 30.98 | 7377 | 0.002140 | 0 | 1 |
| R-717 (Ammonia) | 132.25 | 11333 | 0.00426 | 0 | 0 |

### Normal Boiling Points

| Refrigerant | Boiling Point (°C at 101.325 kPa) |
|-------------|----------------------------------|
| R-134a | -26.1 |
| R-410A | -51.6 |
| R-32 | -51.7 |
| R-290 | -42.1 |
| R-744 | -78.4 (sublimation) |
| R-717 | -33.3 |

### Property Calculation in Two-Phase Region

When quality (x) is known:

```
v = vf + x·vfg = vf + x(vg - vf)
h = hf + x·hfg
s = sf + x·sfg
u = uf + x·ufg
```

Where x = mass fraction of vapor (0 ≤ x ≤ 1)

**Quality Determination:**
```
x = (v - vf)/(vg - vf)
x = (h - hf)/(hg - hf)
x = (s - sf)/(sg - sf)
```

## Property Relationships

### Maxwell Relations

Derived from exactness of thermodynamic properties:

```
(∂T/∂v)s = -(∂P/∂s)v
(∂T/∂P)s = (∂v/∂s)P
(∂P/∂T)v = (∂s/∂v)T
(∂v/∂T)P = -(∂s/∂P)T
```

### Clapeyron Equation

Relates saturation pressure and temperature:

```
dPsat/dT = hfg/(T·vfg)
```

This equation governs the slope of phase boundaries on property diagrams.

## Property Diagrams

### Temperature-Entropy (T-s) Diagram

- X-axis: specific entropy (s)
- Y-axis: temperature (T)
- Shows constant pressure lines
- Area under process curve = heat transfer for reversible process
- Useful for analyzing Carnot cycles and heat engines

### Pressure-Enthalpy (P-h) Diagram

- X-axis: specific enthalpy (h)
- Y-axis: pressure (P, logarithmic scale)
- Standard diagram for refrigeration cycle analysis
- Horizontal lines = constant pressure processes
- Vertical lines = constant enthalpy (throttling) processes
- Quality lines radiate from critical point

### Pressure-Volume (P-v) Diagram

- X-axis: specific volume (v)
- Y-axis: pressure (P)
- Area under process curve = boundary work
- Shows isothermal and isentropic processes clearly

### Mollier Diagram (h-s)

- X-axis: specific entropy (s)
- Y-axis: specific enthalpy (h)
- Useful for steam turbine and compressor analysis
- Constant pressure lines slope upward
- Constant temperature lines horizontal in two-phase region

## Components

- Enthalpy Calculations
- Entropy Calculations
- Internal Energy
- Specific Heat Constant Pressure
- Specific Heat Constant Volume
- Heat Capacity Ratio
- Compressibility Factor
- Reduced Properties
- Corresponding States
- Virial Equations
- Equations Of State
- Ideal Gas Law
- Van Der Waals Equation
- Redlich Kwong Equation
- Peng Robinson Equation
- Benedict Webb Rubin Equation
- Property Tables Charts
- Mollier Diagrams
- Ts Diagrams
- Ph Diagrams
- Pv Diagrams
