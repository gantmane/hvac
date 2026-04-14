---
title: "Composition Effects"
aliases: ["Composition Effects"]
description: "Comprehensive analysis of how food composition affects thermal properties for refrigeration load calculations. Includes predictive equations, component property values, and calculation methods for water, fat, protein, carbohydrate, fiber, and ash content based on ASHRAE methodology."
weight: 10
---

Food thermal properties depend directly on chemical composition. Since foods are mixtures of water, fat, protein, carbohydrates, fiber, and ash, their thermophysical properties can be predicted from the mass fractions and properties of individual components.

## Component Mass Fractions

The composition of any food satisfies the mass balance:

**X_w + X_f + X_p + X_c + X_a = 1.0**

Where:
- X_w = mass fraction of water (dimensionless)
- X_f = mass fraction of fat (dimensionless)
- X_p = mass fraction of protein (dimensionless)
- X_c = mass fraction of carbohydrate (dimensionless)
- X_a = mass fraction of ash (dimensionless)

For ASHRAE calculations, fiber is typically grouped with carbohydrates. Some sources report total solids content, where:

**X_s = X_f + X_p + X_c + X_a = 1 - X_w**

## Thermal Property Prediction Models

### Specific Heat Above Freezing

For unfrozen foods (T > T_f), specific heat is calculated using the mass-weighted average:

**c_p = 4.19X_w + 1.55X_p + 1.68X_c + 1.42X_f + 0.84X_a**

Where c_p is in kJ/(kg·K) at temperatures above the initial freezing point.

This equation assumes:
- Water contributes 4.19 kJ/(kg·K)
- Protein contributes 1.55 kJ/(kg·K)
- Carbohydrate contributes 1.68 kJ/(kg·K)
- Fat contributes 1.42 kJ/(kg·K)
- Ash contributes 0.84 kJ/(kg·K)

### Specific Heat Below Freezing

For frozen foods (T < T_f), the specific heat includes the effect of bound water that remains unfrozen:

**c_p = 1.55X_p + 1.68X_c + 1.42X_f + 0.84X_a + 2.05X_ice + 4.19X_uw**

Where:
- X_ice = mass fraction of ice (frozen water)
- X_uw = mass fraction of unfrozen water (bound water)
- X_ice + X_uw = X_w

The specific heat of ice is 2.05 kJ/(kg·K), significantly lower than liquid water's 4.19 kJ/(kg·K).

### Enthalpy Above Freezing

The enthalpy of unfrozen food relative to -40°C reference:

**H = 9.79 + 405X_w + c_p(T - T_ref)**

Where:
- H = enthalpy (kJ/kg)
- T = food temperature (°C)
- T_ref = -40°C (reference temperature)
- 9.79 = enthalpy contribution from solids at -40°C
- 405 = enthalpy of water at 0°C relative to -40°C

For practical applications with 0°C reference:

**H = c_p × T**

### Enthalpy Below Freezing

For frozen foods, enthalpy includes latent heat of fusion:

**H = c_pf(T - T_f) - 335X_ice**

Where:
- c_pf = specific heat of frozen food
- T_f = initial freezing point (°C)
- 335 = latent heat of fusion for water (kJ/kg)
- X_ice = fraction of water frozen at temperature T

## Component Property Values

| Component | Specific Heat (kJ/kg·K) | Thermal Conductivity (W/m·K) | Density (kg/m³) |
|-----------|-------------------------|-------------------------------|-----------------|
| Water (liquid) | 4.19 | 0.60 | 998 |
| Ice | 2.05 | 2.22 | 917 |
| Protein | 1.55 | 0.18 | 1320 |
| Fat | 1.42 | 0.18 | 925 |
| Carbohydrate | 1.68 | 0.20 | 1550 |
| Fiber | 1.84 | 0.18 | 1300 |
| Ash (minerals) | 0.84 | 0.33 | 2420 |

## Thermal Conductivity Prediction

### Parallel Model (Upper Bound)

**k = k_wX_w + k_pX_p + k_cX_c + k_fX_f + k_aX_a**

This model assumes heat flow parallel to layers of components.

### Series Model (Lower Bound)

**1/k = X_w/k_w + X_p/k_p + X_c/k_c + X_f/k_f + X_a/k_a**

This model assumes heat flow perpendicular to layers of components.

### Effective Medium Model

For most foods, the parallel model overpredicts and series model underpredicts. ASHRAE recommends empirical models:

**Unfrozen foods:**
**k = 0.25 + 0.40X_w + 0.16X_f + 0.19X_p + 0.17X_c + 0.33X_a**

**Frozen foods:**
**k = 0.25 + 1.23X_ice + 0.40X_uw + 0.16X_f + 0.19X_p + 0.17X_c + 0.33X_a**

Note the dramatic increase in thermal conductivity when water freezes (ice conductivity = 2.22 W/m·K vs. water = 0.60 W/m·K).

## Density Prediction

The density of food can be estimated from component densities using the volumetric relationship:

**1/ρ = X_w/ρ_w + X_p/ρ_p + X_c/ρ_c + X_f/ρ_f + X_a/ρ_a**

Where ρ is bulk density in kg/m³.

For frozen foods, substitute ice density (917 kg/m³) for the frozen water fraction:

**1/ρ_f = X_ice/ρ_ice + X_uw/ρ_w + X_p/ρ_p + X_c/ρ_c + X_f/ρ_f + X_a/ρ_a**

Porosity must be considered for cellular foods with air spaces:

**ρ_apparent = (1 - ε)ρ_solid**

Where ε = porosity (volume fraction of air).

## Thermal Diffusivity

Thermal diffusivity affects the rate of temperature change during cooling or freezing:

**α = k/(ρc_p)**

Where:
- α = thermal diffusivity (m²/s)
- k = thermal conductivity (W/m·K)
- ρ = density (kg/m³)
- c_p = specific heat (J/kg·K)

Typical values for foods:
- High moisture foods (unfrozen): 1.2-1.5 × 10⁻⁷ m²/s
- High moisture foods (frozen): 8-10 × 10⁻⁷ m²/s
- Low moisture foods: 1.0-1.2 × 10⁻⁷ m²/s
- High fat foods: 0.8-1.0 × 10⁻⁷ m²/s

## Water Content Effects

Water content is the dominant factor affecting food thermal properties:

### High Water Content (>70% moisture)
- High specific heat (>3.5 kJ/kg·K)
- Moderate thermal conductivity (0.45-0.55 W/m·K)
- Dramatic property changes upon freezing
- Large latent heat requirement
- Examples: lettuce, cucumbers, tomatoes, lean fish

### Moderate Water Content (40-70% moisture)
- Moderate specific heat (2.5-3.5 kJ/kg·K)
- Variable thermal conductivity depending on other components
- Significant freezing effects
- Examples: meats, potatoes, apples, carrots

### Low Water Content (<40% moisture)
- Low specific heat (<2.5 kJ/kg·K)
- Low thermal conductivity (<0.40 W/m·K)
- Minimal freezing effects
- Examples: nuts, dried fruits, cheese, bakery products

## Fat Content Effects

Fat has distinct thermal characteristics:

1. **Lower specific heat**: 1.42 kJ/(kg·K) vs. 4.19 for water
2. **Lower thermal conductivity**: 0.18 W/m·K
3. **No phase change** in normal refrigeration range
4. **Lower density**: 925 kg/m³

High fat foods (>20% fat):
- Reduced cooling requirements
- Lower thermal conductivity
- More uniform properties across temperature range
- Examples: butter, cheese, fatty meats, nuts

## Carbohydrate and Protein Effects

These components have intermediate properties:

**Protein:**
- Specific heat: 1.55 kJ/(kg·K)
- Thermal conductivity: 0.18 W/m·K
- Common in meats (15-25%), fish (15-20%)

**Carbohydrate:**
- Specific heat: 1.68 kJ/(kg·K)
- Thermal conductivity: 0.20 W/m·K
- Dominant in grains, fruits, vegetables

The ratio of protein to carbohydrate affects the initial freezing point depression through colligative properties.

## Ash Content Effects

Mineral content (ash) has minimal direct thermal effect:

- Typically <5% by mass in most foods
- Specific heat: 0.84 kJ/(kg·K)
- Higher thermal conductivity: 0.33 W/m·K
- Very high density: 2420 kg/m³

Primary importance is in freezing point depression and bound water calculation.

## Calculation Procedure

For refrigeration load calculations using composition data:

**Step 1: Obtain Composition Data**

From USDA database, product specifications, or laboratory analysis:
- X_w (water fraction)
- X_f (fat fraction)
- X_p (protein fraction)
- X_c (carbohydrate fraction)
- X_a (ash fraction)

Verify: X_w + X_f + X_p + X_c + X_a = 1.0

**Step 2: Calculate Specific Heat**

For unfrozen product:
c_p = 4.19X_w + 1.55X_p + 1.68X_c + 1.42X_f + 0.84X_a

**Step 3: Calculate Thermal Conductivity**

k = 0.25 + 0.40X_w + 0.16X_f + 0.19X_p + 0.17X_c + 0.33X_a

**Step 4: Calculate Density**

1/ρ = X_w/998 + X_p/1320 + X_c/1550 + X_f/925 + X_a/2420

**Step 5: Calculate Thermal Diffusivity**

α = k/(ρc_p)

**Step 6: For Frozen Products**

Calculate initial freezing point:
T_f = -0.5X_s / X_w (simplified equation)

Determine ice fraction at storage temperature T:
X_ice ≈ X_w × (T_f - T) / (T_f + 1.8)

Recalculate properties using ice and unfrozen water fractions.

## Example Calculation: Ground Beef

Given composition (mass fractions):
- X_w = 0.60 (60% water)
- X_p = 0.19 (19% protein)
- X_f = 0.20 (20% fat)
- X_c = 0.00 (0% carbohydrate)
- X_a = 0.01 (1% ash)

**Specific heat (unfrozen):**
c_p = 4.19(0.60) + 1.55(0.19) + 1.68(0.00) + 1.42(0.20) + 0.84(0.01)
c_p = 2.514 + 0.295 + 0 + 0.284 + 0.008
**c_p = 3.10 kJ/(kg·K)**

**Thermal conductivity (unfrozen):**
k = 0.25 + 0.40(0.60) + 0.16(0.20) + 0.19(0.19) + 0.17(0.00) + 0.33(0.01)
k = 0.25 + 0.24 + 0.032 + 0.036 + 0 + 0.003
**k = 0.561 W/(m·K)**

**Density:**
1/ρ = 0.60/998 + 0.19/1320 + 0.00/1550 + 0.20/925 + 0.01/2420
1/ρ = 0.000601 + 0.000144 + 0 + 0.000216 + 0.000004
1/ρ = 0.000965
**ρ = 1036 kg/m³**

**Thermal diffusivity:**
α = 0.561 / (1036 × 3100)
**α = 1.75 × 10⁻⁷ m²/s**

For refrigeration load from 20°C to 2°C:
Q = m × c_p × ΔT = m × 3.10 × 18 = 55.8m kJ

Where m is mass in kg.

## Accuracy and Limitations

**Prediction accuracy:**
- Specific heat: ±5% for most foods
- Thermal conductivity: ±10-15% (structure dependent)
- Density: ±2-3%
- Enthalpy: ±5%

**Limitations:**
1. Models assume homogeneous mixtures
2. Actual foods have cellular structure and anisotropy
3. Air content (porosity) not included in basic models
4. Temperature dependence of component properties simplified
5. Bound water effects require additional correlations

**Improved accuracy requires:**
- Experimental measurement for critical applications
- Accounting for food structure and porosity
- Temperature-dependent property correlations
- Consideration of processing history (freezing damage, dehydration)

## Applications in Refrigeration Design

Understanding composition effects enables:

1. **Product-specific load calculations** without extensive property data
2. **Prediction of cooling/freezing time** using thermal diffusivity
3. **Optimization of storage conditions** based on property sensitivity
4. **Energy analysis** for different product mixes
5. **Quality control** through property verification

## References

ASHRAE Handbook—Refrigeration (2022), Chapter 19: Thermal Properties of Foods
- Table 1: Thermal properties of foods and beverages
- Table 3: Composition data for common foods
- Equations for predictive models

ASHRAE Handbook—Fundamentals (2021), Chapter 9: Thermal Properties of Foods
- Detailed composition effects
- Experimental data compilation
- Validation studies

## Related Topics

- Initial freezing point determination
- Latent heat of fusion calculation
- Freezing time estimation methods
- Respiration heat generation
- Moisture migration in storage
