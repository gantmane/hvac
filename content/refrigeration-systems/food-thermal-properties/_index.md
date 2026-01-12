---
title: "Food Thermal Properties"
weight: 10
---

## Overview

Thermal properties of food products govern heat transfer rates during refrigeration, freezing, thawing, and storage processes. Accurate knowledge of specific heat, thermal conductivity, enthalpy, and density is essential for calculating cooling loads, determining refrigeration equipment capacity, and predicting temperature change rates. These properties vary significantly with temperature, composition, and phase state (above or below freezing point).

## Composition and Water Content

Water content is the dominant factor affecting thermal properties of food products. Most fresh foods contain 60-95% water by mass, which determines their behavior during cooling and freezing. The remaining composition includes proteins, fats, carbohydrates, and minerals, each contributing distinct thermal characteristics.

**Key relationships:**
- High water content increases specific heat and latent heat of freezing
- Fat content reduces specific heat but increases thermal resistance
- Fiber and carbohydrates contribute intermediate thermal properties
- Air voids in porous foods reduce effective thermal conductivity

## Specific Heat Capacity

Specific heat represents the energy required to raise the temperature of a unit mass by one degree. Food products exhibit different specific heat values above and below their initial freezing point due to phase change effects.

### Above Freezing Temperature

**Empirical correlation (Siebel equation):**

c = 0.837 + 3.349·X_w

Where:
- c = specific heat, Btu/(lb·°F) or kJ/(kg·K)
- X_w = mass fraction of water (decimal)

**Typical values above freezing:**

| Food Category | Water Content (%) | Specific Heat Btu/(lb·°F) | Specific Heat kJ/(kg·K) |
|---------------|-------------------|---------------------------|-------------------------|
| Leafy vegetables | 90-95 | 0.95-0.97 | 3.98-4.06 |
| Fruits | 80-90 | 0.90-0.95 | 3.77-3.98 |
| Fish | 70-80 | 0.82-0.90 | 3.43-3.77 |
| Meat (lean) | 68-75 | 0.77-0.85 | 3.22-3.56 |
| Poultry | 65-75 | 0.75-0.85 | 3.14-3.56 |
| Bread products | 35-40 | 0.55-0.60 | 2.30-2.51 |
| Cheese | 35-50 | 0.55-0.65 | 2.30-2.72 |
| Butter | 15-16 | 0.40-0.42 | 1.67-1.76 |

### Below Freezing Temperature

Once ice formation begins, apparent specific heat decreases significantly. Below the initial freezing point, residual unfrozen water continues to freeze gradually over a temperature range.

**Empirical correlation (frozen foods):**

c_f = 0.200 + 2.008·X_w

Where c_f applies to temperatures well below freezing (< 0°F or -18°C).

## Thermal Conductivity

Thermal conductivity determines the rate of heat flow through food materials. This property varies with temperature, composition, structure (cellular vs. homogeneous), and freezing state.

### Unfrozen Foods

**Thermal conductivity ranges above freezing:**

| Food Category | Thermal Conductivity Btu/(h·ft·°F) | Thermal Conductivity W/(m·K) |
|---------------|-------------------------------------|------------------------------|
| Water (reference) | 0.345 | 0.597 |
| Lean meat | 0.25-0.30 | 0.43-0.52 |
| Fat tissue | 0.11-0.14 | 0.19-0.24 |
| Fruits (dense) | 0.22-0.26 | 0.38-0.45 |
| Vegetables (dense) | 0.24-0.30 | 0.42-0.52 |
| Bread (porous) | 0.03-0.05 | 0.05-0.09 |
| Cheese | 0.20-0.25 | 0.35-0.43 |
| Liquid foods | 0.30-0.35 | 0.52-0.61 |

### Frozen Foods

Ice has thermal conductivity approximately four times higher than liquid water (k_ice = 1.28 Btu/(h·ft·°F) or 2.22 W/(m·K)). Consequently, frozen foods conduct heat more rapidly than unfrozen equivalents.

**Typical frozen food conductivity:**

k_frozen ≈ 2 to 2.5 × k_unfrozen

This increased conductivity accelerates heat transfer during frozen storage but reduces temperature gradients within the product.

## Enthalpy and Freezing

Enthalpy represents the total heat content of a food product relative to a reference temperature. Freezing enthalpy includes sensible cooling above the freezing point, latent heat of fusion during ice formation, and sensible cooling of the frozen product.

### Initial Freezing Point

Pure water freezes at 32°F (0°C), but food products freeze at lower temperatures due to dissolved solids (freezing point depression). Initial freezing points typically range from 28-31°F (-2 to -1°C) for most foods.

**Representative initial freezing points:**

| Food Product | Initial Freezing Point °F | Initial Freezing Point °C |
|--------------|---------------------------|---------------------------|
| Beef | 28-30 | -2.2 to -1.1 |
| Pork | 28-29 | -2.2 to -1.7 |
| Poultry | 27-29 | -2.8 to -1.7 |
| Fish | 28-31 | -2.2 to -0.6 |
| Eggs (whole) | 30-31 | -1.1 to -0.6 |
| Apples | 29-30 | -1.7 to -1.1 |
| Strawberries | 30-31 | -1.1 to -0.6 |
| Lettuce | 31-32 | -0.6 to 0 |

### Latent Heat of Fusion

The latent heat required to freeze water in food products is approximately 144 Btu/lb (335 kJ/kg). Total latent heat depends on water content:

Q_latent = 144 × X_w × m

Where:
- Q_latent = latent heat, Btu
- X_w = mass fraction of water
- m = mass of product, lb

**Example:** 100 lb of beef (70% water content) requires:
Q_latent = 144 × 0.70 × 100 = 10,080 Btu to freeze

### Total Enthalpy Change

Complete enthalpy change from initial temperature to frozen storage temperature:

ΔH_total = c_above × (T_initial - T_freeze) + ΔH_fusion + c_below × (T_freeze - T_final)

This three-term expression accounts for:
1. Sensible cooling to freezing point
2. Latent heat extraction during phase change
3. Sensible cooling of frozen product

## Density

Density affects heat capacity per unit volume and packaging efficiency. Frozen foods exhibit lower density than unfrozen equivalents due to ice expansion (approximately 9% volume increase upon freezing).

**Density ranges:**

| Food Category | Unfrozen lb/ft³ | Unfrozen kg/m³ | Frozen lb/ft³ | Frozen kg/m³ |
|---------------|-----------------|----------------|---------------|--------------|
| Meat (lean) | 66-68 | 1060-1090 | 60-63 | 960-1010 |
| Fish | 64-66 | 1025-1060 | 58-61 | 930-980 |
| Fruits | 50-65 | 800-1040 | 46-60 | 740-960 |
| Vegetables | 50-70 | 800-1120 | 46-64 | 740-1025 |
| Ice cream | 33-37 | 530-590 | 30-34 | 480-545 |

## Application to Load Calculations

Thermal properties directly determine cooling and freezing loads:

**Product load equation:**

Q = m × c × ΔT + m × ΔH_fusion (if freezing)

Where accurate values of c and ΔH_fusion based on composition are essential for equipment sizing. Underestimating thermal properties results in undersized refrigeration systems, excessive temperature pull-down times, and potential product quality degradation.

**Design considerations:**
- Use conservative (high) estimates of specific heat for safety factors
- Account for packaging materials adding thermal mass
- Consider product respiration heat for fresh produce
- Factor in moisture migration affecting local thermal properties during storage

## Temperature Dependence

All thermal properties vary with temperature. Specific heat and thermal conductivity increase with temperature above freezing and decrease below freezing (excluding the phase change region). Property correlations must account for the operating temperature range encountered during refrigeration processes.

For precision calculations, temperature-dependent correlations from ASHRAE Refrigeration Handbook or food engineering databases provide superior accuracy compared to single-point average values.
