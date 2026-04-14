---
title: "Plank Equation"
aliases: ["Plank Equation"]
description: "Comprehensive analysis of Plank's equation for food freezing time calculation including shape factors, assumptions, limitations, Cleland-Earle modifications, and practical engineering applications for industrial refrigeration systems."
weight: 1
---

## Introduction

Plank's equation provides the fundamental analytical method for predicting freezing times of foods and other materials. Developed by R. Plank in 1913, this equation remains the basis for most freezing time calculations in industrial refrigeration despite its simplifying assumptions. The equation balances heat removal rate with the latent heat of fusion, accounting for conductive resistance through the frozen layer and convective resistance at the surface.

The classical Plank equation applies to regular-shaped foods (infinite slabs, infinite cylinders, spheres) freezing from an initial uniform temperature above the freezing point to a final center temperature below the freezing point.

## Classical Plank Equation

### Basic Form

The freezing time **t_f** is given by:

```
t_f = (ρ L / (T_f - T_m)) × (P a / h + R a² / k)
```

Where:
- **t_f** = Freezing time (s)
- **ρ** = Density of frozen product (kg/m³)
- **L** = Latent heat of fusion (J/kg)
- **T_f** = Initial freezing temperature of product (°C)
- **T_m** = Temperature of cooling medium (°C)
- **a** = Thickness (for slab) or diameter (for cylinder/sphere) (m)
- **h** = Surface heat transfer coefficient (W/m²·K)
- **k** = Thermal conductivity of frozen product (W/m·K)
- **P** = Dimensionless shape factor for surface convection
- **R** = Dimensionless shape factor for internal conduction

### Shape Factors

The P and R factors account for geometry and determine the relative importance of surface convection and internal conduction:

| Geometry | P | R | Application |
|----------|---|---|-------------|
| Infinite slab | 1/2 | 1/8 | Thin products, layered materials |
| Infinite cylinder | 1/4 | 1/16 | Sausages, pipes, cylindrical containers |
| Sphere | 1/6 | 1/24 | Fruits, meatballs, spherical products |
| Finite cylinder (L/D = 1) | 1/4 | 1/16 | Short cylinders, cans |
| Finite cylinder (L/D = 2) | 1/4 | 1/16 | Standard cans |
| Finite cylinder (L/D = 4) | 1/6 | 1/24 | Long cylinders approaching infinite |
| Rectangular brick (2a×2a×4a) | 1/8 | 1/32 | Packaged products |

For finite cylinders and rectangular bricks, the characteristic dimension **a** represents:
- Finite cylinder: **a** = radius or half-diameter
- Rectangular brick: **a** = shortest half-dimension

### Derivation from First Principles

Plank's equation derives from a heat balance during phase change. Consider an infinite slab of thickness 2a:

**Heat removed from product:**
```
Q_total = ρ × V × L = ρ × (2a × A) × L
```

**Heat flow through frozen layer:**

The frozen layer thickness increases from the surface toward the center. At time t, the frozen layer extends distance x from the surface. The temperature gradient through this layer is approximately linear:

```
q = k × A × (T_f - T_m) / x
```

**Heat flow through surface film:**
```
q = h × A × (T_s - T_m)
```

Where **T_s** is the surface temperature. For steady-state through the composite resistance:

```
q = (T_f - T_m) / (x/k + 1/h)
```

**Heat balance:**

The heat conducted through the frozen layer equals the latent heat released at the freezing front:

```
ρ × L × A × dx/dt = k × A × (T_f - T_m) / x + h × A × (T_f - T_m)
```

Separating variables and integrating from x = 0 to x = a over time 0 to t_f:

```
∫[0 to a] ρ L x dx = ∫[0 to t_f] [k(T_f - T_m) + h(T_f - T_m)x] dt
```

This integration yields:

```
ρ L a²/2 = (T_f - T_m) × [ka/h + a²/2k] × t_f
```

Rearranging:

```
t_f = (ρ L / (T_f - T_m)) × (a/2h + a²/2k)
```

For a slab with half-thickness a, comparing to the general form identifies **P = 1/2** and **R = 1/8** (the factor of 2 accounts for heat removal from both sides).

## Assumptions and Limitations

### Primary Assumptions

1. **Single freezing point**: Product freezes at a single temperature T_f (no freezing range)
2. **Negligible sensible heat**: Heat removal above and below freezing point is small compared to latent heat
3. **Constant properties**: Thermal conductivity, density, and heat transfer coefficient remain constant
4. **Uniform initial temperature**: Product starts at freezing temperature T_f throughout
5. **Constant medium temperature**: Cooling medium temperature T_m is constant
6. **Regular geometry**: Product has simple geometric shape
7. **One-dimensional heat transfer**: Edge effects are negligible
8. **No volume change**: Product dimensions remain constant during freezing

### Practical Limitations

**Overprediction of freezing time:**
- Plank's equation typically **overpredicts** freezing time by 10-30%
- Assumes product starts at freezing temperature (neglects precooling sensible heat)
- Assumes freezing ends when center reaches freezing point (actual target is lower)

**Property variations:**
- Thermal conductivity of frozen food typically 3-4 times higher than unfrozen
- Density changes 5-10% during freezing
- Heat transfer coefficient varies with air velocity, temperature difference, and frost formation

**Freezing range effects:**
- Most foods freeze over a temperature range (typically -1°C to -5°C)
- Latent heat releases gradually, not at a single temperature
- Bound water freezes at lower temperatures

**Temperature distribution:**
- Assumes linear temperature profile in frozen layer
- Actual profile is more complex due to varying thermal conductivity

## Modified Plank Equations

### Accounting for Sensible Heat

The complete freezing process includes three phases:
1. **Precooling**: Cooling from initial temperature T_i to freezing point T_f
2. **Phase change**: Freezing at temperature range around T_f
3. **Tempering**: Cooling from T_f to final center temperature T_c

**Modified equation including sensible heat:**

```
t_f = (ρ / (T_f - T_m)) × [ΔH_1(a/h) + ΔH_2(a²/k)]
```

Where:
```
ΔH_1 = P × [L + c_u(T_i - T_f) + c_f(T_f - T_c)]
ΔH_2 = R × [L + 0.5 × c_u(T_i - T_f) + 0.2 × c_f(T_f - T_c)]
```

- **c_u** = Specific heat of unfrozen product (J/kg·K)
- **c_f** = Specific heat of frozen product (J/kg·K)
- **T_i** = Initial product temperature (°C)
- **T_c** = Final center temperature (°C)

The coefficients 0.5 and 0.2 account for the temperature distribution during sensible heat removal.

### Equivalent Freezing Temperature Method

For foods with a freezing range, use an **equivalent freezing temperature**:

```
T_f,eq = (T_i + T_c) / 2
```

This approximates the mean temperature during the freezing process and provides better accuracy than using the initial freezing point.

### Equivalent Heat Transfer Dimension

For irregular shapes, calculate an **equivalent heat transfer dimension**:

```
a_eq = (V / A) × β
```

Where:
- **V** = Product volume (m³)
- **A** = Surface area (m²)
- **β** = Shape factor (1 for slab, 2 for cylinder, 3 for sphere)

Then use shape factors corresponding to the assumed geometry in the Plank equation.

## Cleland-Earle Modifications

Cleland and Earle (1977, 1982) developed empirical modifications to Plank's equation that significantly improve accuracy for practical food freezing applications. These modifications account for sensible heat, freezing range, and temperature-dependent properties.

### Cleland-Earle Equation Form

```
t_f = (ρ_u × a / (T_f - T_m)) × [P × ΔH_1 / E_1 + R × ΔH_2 / E_2]
```

Where:
- **ρ_u** = Density of unfrozen product (kg/m³)
- **E_1** = Mean surface heat transfer coefficient during freezing (W/m²·K)
- **E_2** = Mean thermal conductivity during freezing (W/m·K)

### Enthalpy Terms

**ΔH_1 (surface resistance enthalpy):**

```
ΔH_1 = c_u(T_i - T_f) + L + c_f(T_f - T_c)
```

**ΔH_2 (internal resistance enthalpy):**

```
ΔH_2 = (1 + 0.008 Pk_s) × c_u(T_i - T_f) + L + (1 - 0.10 Pk_s) × c_f(T_f - T_c)
```

Where **Pk_s** is the Plank number for sensible heat:

```
Pk_s = c_f(T_f - T_c) / L
```

### Mean Heat Transfer Coefficient

The mean surface heat transfer coefficient accounts for varying conditions:

```
E_1 = 1 / [(T_f - T_m) / ((T_i - T_m) × h_0 + (T_f - T_m) × h_f)]
```

Simplified for most applications:

```
E_1 ≈ h × [(T_i - T_m) / (T_f - T_m)]^0.25
```

Where:
- **h_0** = Initial heat transfer coefficient (W/m²·K)
- **h_f** = Final heat transfer coefficient (W/m²·K)
- **h** = Average heat transfer coefficient (W/m²·K)

### Mean Thermal Conductivity

The mean thermal conductivity during freezing:

```
E_2 = (2 × k_u × k_f) / (k_u + k_f)
```

Where:
- **k_u** = Thermal conductivity of unfrozen product (W/m·K)
- **k_f** = Thermal conductivity of frozen product (W/m·K)

This harmonic mean accounts for the changing conductivity as the frozen layer propagates.

### Modified Shape Factors

Cleland and Earle introduced modified shape factors based on extensive numerical analysis:

| Geometry | P (Cleland) | R (Cleland) | Biot Number Range |
|----------|-------------|-------------|-------------------|
| Infinite slab | 0.5072 | 0.1684 | 0.1 < Bi < 100 |
| Infinite cylinder | 0.2482 | 0.0528 | 0.1 < Bi < 100 |
| Sphere | 0.1684 | 0.0235 | 0.1 < Bi < 100 |

**Biot number:**

```
Bi = h × a / k_f
```

The Biot number indicates the relative importance of internal conduction resistance to surface convection resistance.

## Practical Calculation Examples

### Example 1: Freezing Beef Patties (Infinite Slab)

**Given data:**
- Thickness: 2a = 19 mm (a = 0.0095 m)
- Initial temperature: T_i = 20°C
- Initial freezing point: T_f = -2°C
- Final center temperature: T_c = -18°C
- Cooling medium temperature: T_m = -35°C
- Air velocity: 5 m/s
- Heat transfer coefficient: h = 40 W/m²·K

**Product properties (beef, 75% moisture):**
- Density unfrozen: ρ_u = 1050 kg/m³
- Density frozen: ρ_f = 970 kg/m³
- Specific heat unfrozen: c_u = 3500 J/kg·K
- Specific heat frozen: c_f = 1900 J/kg·K
- Latent heat: L = 250,000 J/kg
- Thermal conductivity unfrozen: k_u = 0.45 W/m·K
- Thermal conductivity frozen: k_f = 1.60 W/m·K

**Classical Plank calculation:**

Using P = 1/2, R = 1/8 for infinite slab:

```
t_f = (970 × 250,000 / (-2 - (-35))) × (0.5 × 0.0095 / 40 + 0.125 × 0.0095² / 1.60)
t_f = (242,500,000 / 33) × (0.000119 + 0.000007)
t_f = 7,348,485 × 0.000126
t_f = 926 seconds = 15.4 minutes
```

**Cleland-Earle calculation:**

Step 1 - Calculate Plank number:
```
Pk_s = 1900 × (-2 - (-18)) / 250,000 = 1900 × 16 / 250,000 = 0.122
```

Step 2 - Calculate enthalpy terms:
```
ΔH_1 = 3500 × (20 - (-2)) + 250,000 + 1900 × (-2 - (-18))
ΔH_1 = 77,000 + 250,000 + 30,400 = 357,400 J/kg

ΔH_2 = (1 + 0.008 × 0.5 × 0.122) × 77,000 + 250,000 + (1 - 0.10 × 0.5 × 0.122) × 30,400
ΔH_2 = 1.00049 × 77,000 + 250,000 + 0.9939 × 30,400
ΔH_2 = 77,037 + 250,000 + 30,214 = 357,251 J/kg
```

Step 3 - Calculate mean thermal conductivity:
```
E_2 = (2 × 0.45 × 1.60) / (0.45 + 1.60) = 1.44 / 2.05 = 0.702 W/m·K
```

Step 4 - Use E_1 ≈ h (simplified):
```
E_1 = 40 W/m²·K
```

Step 5 - Calculate freezing time:
```
t_f = (1050 × 0.0095 / (-2 - (-35))) × (0.5072 × 357,400 / 40 + 0.1684 × 357,251 / 0.702)
t_f = (9.975 / 33) × (4,536 + 85,731)
t_f = 0.3023 × 90,267
t_f = 27,290 seconds = 7.6 hours
```

**Analysis:**

The Cleland-Earle method gives approximately **30 times longer** than classical Plank because it accounts for:
- Sensible heat removal (cooling from 20°C to -2°C, then -2°C to -18°C)
- Lower mean thermal conductivity during the initial unfrozen phase
- More accurate representation of the temperature distribution

The classical Plank equation assumes the product starts at the freezing point, which drastically underestimates actual freezing time.

### Example 2: Freezing Fish Fillets (Irregular Shape)

**Given data:**
- Volume: V = 0.0003 m³ (300 cm³)
- Surface area: A = 0.025 m² (250 cm²)
- Initial temperature: T_i = 5°C
- Freezing point: T_f = -1.5°C
- Final center temperature: T_c = -20°C
- Blast freezer air: T_m = -40°C
- Heat transfer coefficient: h = 50 W/m²·K

**Product properties (fish, 80% moisture):**
- Density: ρ = 1040 kg/m³
- Specific heat unfrozen: c_u = 3800 J/kg·K
- Specific heat frozen: c_f = 2000 J/kg·K
- Latent heat: L = 268,000 J/kg
- Thermal conductivity unfrozen: k_u = 0.50 W/m·K
- Thermal conductivity frozen: k_f = 1.80 W/m·K

**Step 1 - Determine equivalent dimension:**

Volume-to-area ratio:
```
V/A = 0.0003 / 0.025 = 0.012 m
```

Assume slab geometry (β = 1):
```
a_eq = 0.012 × 1 = 0.012 m
```

**Step 2 - Use Cleland-Earle equation:**

Calculate Pk_s:
```
Pk_s = 2000 × 18.5 / 268,000 = 0.138
```

Calculate ΔH_1:
```
ΔH_1 = 3800 × 6.5 + 268,000 + 2000 × 18.5
ΔH_1 = 24,700 + 268,000 + 37,000 = 329,700 J/kg
```

Calculate ΔH_2:
```
ΔH_2 = (1 + 0.008 × 0.5072 × 0.138) × 24,700 + 268,000 + (1 - 0.10 × 0.5072 × 0.138) × 37,000
ΔH_2 = 1.00056 × 24,700 + 268,000 + 0.9930 × 37,000
ΔH_2 = 24,714 + 268,000 + 36,741 = 329,455 J/kg
```

Calculate E_2:
```
E_2 = (2 × 0.50 × 1.80) / (0.50 + 1.80) = 1.80 / 2.30 = 0.783 W/m·K
```

Calculate freezing time:
```
t_f = (1040 × 0.012 / 38.5) × (0.5072 × 329,700 / 50 + 0.1684 × 329,455 / 0.783)
t_f = 0.324 × (3,344 + 70,871)
t_f = 0.324 × 74,215
t_f = 24,046 seconds = 6.68 hours
```

### Example 3: Freezing Spherical Meatballs

**Given data:**
- Diameter: 2a = 40 mm (a = 0.020 m)
- Initial temperature: T_i = 15°C
- Freezing point: T_f = -2.5°C
- Final center temperature: T_c = -15°C
- Air temperature: T_m = -30°C
- Heat transfer coefficient: h = 35 W/m²·K

**Product properties (meat, 70% moisture):**
- Density: ρ = 1060 kg/m³
- Specific heat unfrozen: c_u = 3400 J/kg·K
- Specific heat frozen: c_f = 1850 J/kg·K
- Latent heat: L = 235,000 J/kg
- Thermal conductivity unfrozen: k_u = 0.43 W/m·K
- Thermal conductivity frozen: k_f = 1.50 W/m·K

**Using sphere factors (P = 0.1684, R = 0.0235):**

Calculate Pk_s:
```
Pk_s = 1850 × 12.5 / 235,000 = 0.098
```

Calculate ΔH_1:
```
ΔH_1 = 3400 × 17.5 + 235,000 + 1850 × 12.5
ΔH_1 = 59,500 + 235,000 + 23,125 = 317,625 J/kg
```

Calculate ΔH_2:
```
ΔH_2 = (1 + 0.008 × 0.1684 × 0.098) × 59,500 + 235,000 + (1 - 0.10 × 0.1684 × 0.098) × 23,125
ΔH_2 = 1.00013 × 59,500 + 235,000 + 0.9984 × 23,125
ΔH_2 = 59,508 + 235,000 + 23,088 = 317,596 J/kg
```

Calculate E_2:
```
E_2 = (2 × 0.43 × 1.50) / (0.43 + 1.50) = 1.29 / 1.93 = 0.668 W/m·K
```

Calculate freezing time:
```
t_f = (1060 × 0.020 / 27.5) × (0.1684 × 317,625 / 35 + 0.0235 × 317,596 / 0.668)
t_f = 0.771 × (1,530 + 11,169)
t_f = 0.771 × 12,699
t_f = 9,791 seconds = 2.72 hours
```

## Selection of Heat Transfer Coefficients

Accurate freezing time prediction requires appropriate heat transfer coefficient values for the specific freezing method:

| Freezing Method | Air Velocity | Heat Transfer Coefficient h (W/m²·K) |
|----------------|--------------|--------------------------------------|
| Still air freezer | Natural convection | 5 - 10 |
| Blast freezer | 1 - 2 m/s | 15 - 25 |
| Blast freezer | 3 - 5 m/s | 30 - 50 |
| Blast freezer | 5 - 10 m/s | 50 - 80 |
| Fluidized bed | High velocity | 100 - 200 |
| Immersion freezing | Brine/glycol | 200 - 500 |
| Plate freezer | Contact freezing | 100 - 300 |
| Cryogenic (CO₂) | Liquid contact | 400 - 800 |
| Cryogenic (N₂) | Liquid spray | 500 - 1000 |

**Factors affecting heat transfer coefficient:**
- Air or fluid velocity
- Temperature difference between product and medium
- Product surface characteristics (smooth, rough, frost formation)
- Packaging (wrapped products have lower h values)
- Product orientation and spacing

For packaged products, reduce the heat transfer coefficient by 20-40% to account for packaging resistance.

## Property Data for Common Foods

### Thermal Conductivity

**Unfrozen (above freezing):**

| Product | Moisture (%) | k_u (W/m·K) |
|---------|--------------|-------------|
| Beef | 70-75 | 0.41 - 0.48 |
| Pork | 65-72 | 0.40 - 0.46 |
| Chicken | 70-75 | 0.42 - 0.49 |
| Fish (lean) | 78-82 | 0.48 - 0.54 |
| Fish (fatty) | 60-70 | 0.38 - 0.45 |
| Vegetables | 85-95 | 0.50 - 0.60 |
| Fruits | 80-90 | 0.45 - 0.58 |
| Ice cream | 60-65 | 0.35 - 0.42 |

**Frozen (below freezing):**

| Product | Moisture (%) | k_f (W/m·K) |
|---------|--------------|-------------|
| Beef | 70-75 | 1.50 - 1.75 |
| Pork | 65-72 | 1.40 - 1.65 |
| Chicken | 70-75 | 1.55 - 1.80 |
| Fish (lean) | 78-82 | 1.75 - 2.00 |
| Fish (fatty) | 60-70 | 1.30 - 1.55 |
| Vegetables | 85-95 | 1.85 - 2.20 |
| Fruits | 80-90 | 1.65 - 2.05 |
| Ice cream | 60-65 | 1.25 - 1.50 |

### Latent Heat of Fusion

Latent heat depends primarily on moisture content:

```
L = w × L_water
```

Where:
- **w** = Mass fraction of water (decimal)
- **L_water** = Latent heat of water = 334,000 J/kg

For foods, account for bound water and dissolved solids:

```
L ≈ w × 334,000 × (0.95 - 0.85) J/kg
```

Typical range: **0.85 to 0.95 times theoretical** based on water content.

| Moisture Content (%) | Effective L (kJ/kg) |
|---------------------|---------------------|
| 50 | 140 - 160 |
| 60 | 170 - 190 |
| 70 | 200 - 220 |
| 75 | 215 - 235 |
| 80 | 230 - 250 |
| 85 | 240 - 265 |
| 90 | 255 - 280 |
| 95 | 270 - 295 |

## Numerical Methods and Software

For complex geometries, non-uniform initial conditions, or variable properties, numerical methods provide more accurate predictions:

### Finite Difference Method

Discretize the heat conduction equation:

```
∂T/∂t = α × ∇²T
```

Where **α = k / (ρ × c)** is thermal diffusivity.

### Finite Element Analysis

Commercial software packages used in food freezing analysis:
- COMSOL Multiphysics
- ANSYS Fluent
- MATLAB with PDE Toolbox
- Specialized food engineering software (FreezeCalc, ColdSim)

### When to Use Numerical Methods

- Irregular product shapes
- Layered or composite products
- Time-varying boundary conditions
- Spatially varying initial temperatures
- Need for detailed internal temperature profiles
- Multiple products in contact
- Accuracy requirements within ±5%

## ASHRAE Handbook References

**ASHRAE Handbook - Refrigeration (2022):**
- Chapter 19: Thermal Properties of Foods
- Chapter 20: Cooling and Freezing Times of Foods
- Table 1: Thermal properties of foods
- Table 3: Shape factors for Plank's equation
- Equations 15-22: Modified Plank equations

**Key equations from ASHRAE:**
- Equation 20.15: Classical Plank equation
- Equation 20.18: Cleland-Earle modification
- Equation 20.21: Enthalpy calculation methods
- Figure 20.3: Heat transfer coefficients for various freezing methods

## Accuracy and Validation

**Expected accuracy of Plank-based methods:**

| Method | Typical Accuracy | Application Range |
|--------|-----------------|-------------------|
| Classical Plank | ±30-50% (overpredicts) | Limited, educational only |
| Modified Plank (sensible heat) | ±20-30% | Regular shapes, known properties |
| Cleland-Earle | ±10-15% | Most food freezing applications |
| Numerical methods | ±5-10% | Complex cases, research applications |

**Factors affecting prediction accuracy:**
- Property data uncertainty (±10-20%)
- Heat transfer coefficient estimation (±20-30%)
- Product variability (composition, initial temperature)
- Actual freezing process conditions
- Frost buildup on product surface
- Non-uniform air distribution in freezer

## Engineering Applications

### Freezer Capacity Calculations

Total refrigeration load includes:

1. **Product freezing load:**
```
Q_product = m × (c_u × ΔT_precool + L + c_f × ΔT_temper) / t_f
```

2. **Packaging:**
```
Q_package = m_package × c_package × ΔT / t_f
```

3. **Air infiltration, fan heat, transmission losses**

### Process Optimization

Use freezing time calculations to:
- Select appropriate freezing equipment
- Determine optimum air velocity (balance energy cost vs. throughput)
- Size refrigeration systems
- Optimize product dimensions for rapid freezing
- Schedule production runs
- Compare freezing methods (blast, plate, immersion, cryogenic)

### Quality Considerations

Freezing rate affects product quality:

**Slow freezing (low h, high a):**
- Large ice crystals
- Cell damage
- Drip loss upon thawing
- Texture degradation

**Fast freezing (high h, low a):**
- Small ice crystals
- Minimal cell damage
- Better quality retention
- Higher operating cost

Target freezing rates:
- Individual quick frozen (IQF): Complete freezing in 15-30 minutes
- Standard blast freezing: 2-4 hours
- Plate freezing: 1-3 hours
- Cryogenic: 5-15 minutes

## Conclusion

Plank's equation provides the fundamental framework for freezing time calculations in industrial refrigeration. While the classical equation has significant limitations, modern modifications (particularly Cleland-Earle) offer practical accuracy for engineering design and analysis.

**Key engineering considerations:**

1. Always use modified Plank equations that account for sensible heat
2. Select appropriate shape factors based on actual product geometry
3. Use validated property data from ASHRAE or experimental measurement
4. Estimate heat transfer coefficients conservatively for design calculations
5. Consider using numerical methods for critical applications
6. Validate predictions with trial runs during commissioning

The equation remains an essential tool for refrigeration engineers, providing rapid estimates for feasibility studies, preliminary design, and process optimization. For final design verification, combine analytical predictions with experimental validation or detailed numerical simulation.

