---
title: "Enthalpy of Foods"
aliases: ["Enthalpy of Foods"]
description: "Comprehensive technical guide to food enthalpy calculations for refrigeration load determination including specific enthalpy values, phase change effects, freezing point depression, and ASHRAE calculation methods for HVAC refrigeration systems"
weight: 3
---

Enthalpy represents the total heat content of a food product and is essential for calculating refrigeration loads in storage, processing, and transportation applications. The enthalpy of foods varies with temperature, composition, and phase state, requiring accurate determination for proper equipment sizing and energy analysis.

## Fundamental Enthalpy Relationships

The specific enthalpy of a food product is the sum of sensible and latent heat components:

**h = h_ref + ∫c_p dT + L**

Where:
- h = specific enthalpy (kJ/kg or Btu/lbm)
- h_ref = reference enthalpy at reference temperature
- c_p = specific heat (kJ/kg·K or Btu/lbm·°F)
- T = temperature (K or °F)
- L = latent heat of phase change (kJ/kg or Btu/lbm)

For refrigeration calculations, the reference temperature is typically set at -40°C (-40°F) where h_ref = 0, or at the initial freezing point of the product.

## Enthalpy Above Freezing Point

For unfrozen foods, the enthalpy calculation simplifies to sensible heat only:

**h_unfrozen = c_p,unfrozen × (T - T_ref)**

The specific heat of unfrozen foods can be estimated from composition:

**c_p,unfrozen = 4.19x_w + 1.55x_p + 1.68x_f + 1.26x_c + 0.84x_a (kJ/kg·K)**

**c_p,unfrozen = 1.00x_w + 0.37x_p + 0.40x_f + 0.30x_c + 0.20x_a (Btu/lbm·°F)**

Where x represents mass fraction of:
- x_w = water
- x_p = protein
- x_f = fat
- x_c = carbohydrate
- x_a = ash

## Enthalpy Below Freezing Point

Below the initial freezing point, foods contain both ice and unfrozen water. The enthalpy calculation must account for:

1. Sensible heat removal from initial temperature to freezing point
2. Latent heat of fusion for water that freezes
3. Sensible heat removal of frozen product

**h_frozen = c_p,unfrozen(T_f - T_ref) - x_w × L_f × f_ice - c_p,frozen(T_f - T)**

Where:
- T_f = initial freezing point (°C or °F)
- L_f = latent heat of fusion of water (334 kJ/kg or 144 Btu/lbm)
- f_ice = fraction of water frozen at temperature T

The specific heat of frozen foods:

**c_p,frozen = 1.55x_p + 1.68x_f + 1.26x_c + 0.84x_a + 2.05x_ice + 4.19x_uw (kJ/kg·K)**

**c_p,frozen = 0.37x_p + 0.40x_f + 0.30x_c + 0.20x_a + 0.49x_ice + 1.00x_uw (Btu/lbm·°F)**

Where:
- x_ice = mass fraction of ice
- x_uw = mass fraction of unfrozen water

## Fraction of Water Frozen

The fraction of water frozen depends on temperature and follows the freezing point depression relationship. For most foods, an empirical equation applies:

**f_ice = (T_f - T)/(T_f - T_f')**

Where T_f' is an apparent final freezing temperature, typically -55°C to -60°C (-67°F to -76°F) for high-moisture foods.

More accurately, using the Chen model:

**x_uw = x_w × [1.105 + 0.7138 ln(T_f - T)]** for T < T_f

This accounts for bound water and solute effects.

## Specific Enthalpy Values for Common Foods

### Meats and Poultry (Reference T_ref = -40°C)

| Food Product | Moisture % | T_f (°C) | h at 4°C (kJ/kg) | h at -18°C (kJ/kg) | h at -29°C (kJ/kg) |
|--------------|------------|----------|------------------|--------------------|--------------------|
| Beef, lean | 74 | -1.7 | 311 | -174 | -195 |
| Beef, fatty | 55 | -2.2 | 231 | -106 | -123 |
| Pork, lean | 72 | -2.2 | 303 | -164 | -185 |
| Chicken, whole | 69 | -2.8 | 290 | -152 | -172 |
| Turkey, whole | 68 | -2.5 | 286 | -147 | -167 |
| Lamb | 73 | -2.0 | 307 | -169 | -190 |
| Fish, lean | 80 | -2.2 | 336 | -202 | -224 |
| Fish, fatty | 65 | -2.7 | 273 | -135 | -155 |

### Fruits (Reference T_ref = -40°C)

| Food Product | Moisture % | T_f (°C) | h at 10°C (kJ/kg) | h at -18°C (kJ/kg) | h at -23°C (kJ/kg) |
|--------------|------------|----------|-------------------|--------------------|--------------------|
| Apples | 84 | -1.5 | 385 | -238 | -257 |
| Oranges | 87 | -1.3 | 399 | -252 | -272 |
| Strawberries | 90 | -0.8 | 413 | -267 | -288 |
| Bananas | 75 | -1.0 | 344 | -196 | -215 |
| Grapes | 81 | -1.6 | 372 | -222 | -242 |
| Peaches | 89 | -0.9 | 408 | -262 | -283 |
| Blueberries | 84 | -1.2 | 385 | -238 | -258 |

### Vegetables (Reference T_ref = -40°C)

| Food Product | Moisture % | T_f (°C) | h at 10°C (kJ/kg) | h at -18°C (kJ/kg) | h at -23°C (kJ/kg) |
|--------------|------------|----------|-------------------|--------------------|--------------------|
| Potatoes | 78 | -0.6 | 358 | -209 | -228 |
| Carrots | 88 | -1.4 | 404 | -256 | -277 |
| Lettuce | 95 | -0.2 | 436 | -290 | -312 |
| Tomatoes | 94 | -0.6 | 431 | -284 | -306 |
| Broccoli | 91 | -0.6 | 417 | -272 | -293 |
| Corn, sweet | 76 | -0.6 | 349 | -200 | -219 |
| Peas | 79 | -0.6 | 362 | -214 | -233 |

### Dairy Products (Reference T_ref = -40°C)

| Food Product | Moisture % | T_f (°C) | h at 4°C (kJ/kg) | h at -18°C (kJ/kg) | h at -29°C (kJ/kg) |
|--------------|------------|----------|------------------|--------------------|--------------------|
| Milk, whole | 88 | -0.5 | 369 | -256 | -276 |
| Butter | 16 | -15.0 | 67 | 10 | 3 |
| Cheese, cheddar | 37 | -13.0 | 155 | -26 | -38 |
| Ice cream | 63 | -5.6 | 264 | -114 | -133 |
| Yogurt | 88 | -1.0 | 369 | -255 | -276 |
| Cream, heavy | 58 | -8.0 | 243 | -81 | -98 |

## ASHRAE Enthalpy Calculation Methods

ASHRAE Handbook - Refrigeration provides empirical equations for calculating food enthalpy based on composition and temperature.

### Method 1: Siebel's Equations (Historical)

For temperatures above freezing:
**h = c_p,unfrozen × (T - T_ref)**

For temperatures below freezing:
**h = c_p,unfrozen × (T_f - T_ref) - L_f - c_p,frozen × (T_f - T)**

Where Siebel's constants:
- c_p,unfrozen = 3.35 kJ/kg·K (0.80 Btu/lbm·°F) for foods above freezing
- c_p,frozen = 1.68 kJ/kg·K (0.40 Btu/lbm·°F) for frozen foods
- L_f = 334 kJ/kg (144 Btu/lbm) latent heat

This method is simplified and less accurate than modern composition-based methods.

### Method 2: Composition-Based Calculation

Current ASHRAE method uses component mass fractions:

**Step 1:** Determine initial freezing point
**T_f = -40.9 × m_s / m_w (°C)**

Where:
- m_s = mass of dissolved solids (kg)
- m_w = mass of water (kg)

**Step 2:** Calculate enthalpy above freezing (T > T_f)
**h = c_p,unfrozen × (T - T_ref)**

With c_p,unfrozen from composition equation provided earlier.

**Step 3:** Calculate enthalpy below freezing (T < T_f)

**h = h_f - ΔH_latent - ∫c_p,frozen dT**

Where:
- h_f = enthalpy at freezing point
- ΔH_latent = latent heat released during freezing
- Integral from T_f to T

### Method 3: Empirical Regression Equations

For specific food categories, ASHRAE provides regression equations:

**Fruits and vegetables:**
**h = A + B×T + C×T²**

**Meats:**
**h = D×(T - T_f) + E×x_w×(T - T_f)²** for T < T_f

Coefficients are tabulated in ASHRAE Handbook - Refrigeration, Chapter 19.

## Latent Heat Effects During Freezing

The latent heat release during freezing is not instantaneous but occurs over a temperature range due to:

1. Freezing point depression by dissolved solutes
2. Bound water effects
3. Progressive ice crystal formation

The latent heat release rate is:

**dQ/dT = m × L_f × df_ice/dT**

Where df_ice/dT represents the rate of ice formation with temperature decrease.

For a food product with 80% moisture content:

| Temperature (°C) | Ice Fraction | Remaining Latent Heat (kJ/kg) |
|------------------|--------------|-------------------------------|
| -1 | 0.10 | 241 |
| -2 | 0.25 | 201 |
| -5 | 0.60 | 107 |
| -10 | 0.82 | 48 |
| -15 | 0.91 | 24 |
| -20 | 0.96 | 11 |
| -30 | 0.99 | 3 |

This progressive freezing affects refrigeration system capacity requirements, as the effective load is higher in the initial freezing zone (-1°C to -5°C) than at lower temperatures.

## Refrigeration Load Calculations Using Enthalpy

The refrigeration load for cooling or freezing food products:

**Q = m × Δh**

Where:
- Q = heat removal rate (kW or Btu/hr)
- m = mass flow rate (kg/s or lbm/hr)
- Δh = specific enthalpy change (kJ/kg or Btu/lbm)

### Example Calculation: Beef Cooling and Freezing

Calculate the refrigeration load to cool 1000 kg of lean beef from 20°C to -25°C in 24 hours.

Given:
- Moisture content: 74%
- Initial freezing point: -1.7°C
- Mass: 1000 kg
- Time: 24 hours = 86,400 s

**Step 1:** Calculate enthalpy at 20°C (above freezing)
Using c_p,unfrozen = 3.48 kJ/kg·K (from composition):
**h₁ = 3.48 × (20 - (-40)) = 209 kJ/kg**

**Step 2:** Calculate enthalpy at -1.7°C (freezing point)
**h₂ = 3.48 × (-1.7 - (-40)) = 133 kJ/kg**

**Step 3:** Calculate enthalpy at -25°C (frozen)
Using empirical data or calculation:
**h₃ = -208 kJ/kg** (includes latent heat and sensible cooling of frozen product)

**Step 4:** Total enthalpy change
**Δh = h₃ - h₁ = -208 - 209 = -417 kJ/kg**

**Step 5:** Refrigeration load
**Q = (1000 kg × 417 kJ/kg) / 86,400 s = 4.83 kW**

**Step 6:** Apply safety factor for peak load
With 25% safety factor for peak conditions:
**Q_design = 4.83 × 1.25 = 6.0 kW refrigeration capacity**

## Enthalpy Change Components

Breaking down the beef freezing example into components:

| Process Stage | Temperature Range | Enthalpy Change (kJ/kg) | Percentage |
|---------------|-------------------|-------------------------|------------|
| Cooling to freezing point | 20°C to -1.7°C | -76 | 18.2% |
| Latent heat of fusion | -1.7°C | -247 | 59.2% |
| Cooling frozen product | -1.7°C to -25°C | -94 | 22.6% |
| **Total** | **20°C to -25°C** | **-417** | **100%** |

This distribution shows that approximately 60% of the refrigeration load occurs during the phase change, with the freezing zone requiring the highest instantaneous capacity.

## Effect of Freezing Point Depression

Solutes in food products depress the freezing point and reduce the fraction of water that freezes at any given temperature below 0°C.

The freezing point depression follows:

**ΔT_f = K_f × m_solute**

Where:
- ΔT_f = freezing point depression (K)
- K_f = cryoscopic constant for water (1.86 K·kg/mol)
- m_solute = molal concentration of solutes

For foods with high sugar or salt content:

| Food Type | Dissolved Solids (%) | T_f (°C) | Water Frozen at -18°C (%) |
|-----------|----------------------|----------|---------------------------|
| Fresh fish | 4 | -2.2 | 97 |
| Fruit juice concentrate | 40 | -15.0 | 75 |
| Sugar solution (50%) | 50 | -20.0 | 40 |
| Salted fish | 15 | -10.0 | 85 |
| Jam/preserves | 35 | -12.0 | 80 |

This affects the latent heat release and the final specific heat of the frozen product, as unfrozen water has much higher specific heat than ice.

## Practical Considerations for HVAC Design

1. **Residence Time in Freezing Zone**: Products spend considerable time in the -1°C to -10°C range where most ice formation occurs. Refrigeration equipment must handle the peak latent heat load in this zone.

2. **Product Temperature Uniformity**: Surface layers freeze first, creating thermal resistance. Center temperature lags surface temperature, requiring extended cooling time.

3. **Respiration Heat**: Fresh fruits and vegetables continue respiration above freezing, adding 10-50 W/tonne to the refrigeration load depending on product and temperature.

4. **Packaging Effects**: Packaging materials add sensible heat load and thermal resistance:
   - Cardboard boxes: add 2-5% to enthalpy change
   - Plastic trays: add 1-3% to enthalpy change
   - Thermal resistance increases cooling time by 15-40%

5. **Air Film Resistance**: Surface heat transfer coefficient significantly affects cooling rate:
   - Natural convection: h = 5-10 W/m²·K
   - Forced air: h = 25-50 W/m²·K
   - High-velocity air: h = 50-100 W/m²·K

## Enthalpy Charts and Psychrometric Applications

For foods stored in refrigerated spaces, the enthalpy of both the product and the surrounding air must be considered. The total refrigeration load includes:

**Q_total = Q_product + Q_air + Q_transmission + Q_infiltration + Q_equipment + Q_personnel**

The product load dominates initial cooling, while air enthalpy changes affect steady-state storage load.

For a cold storage room at -20°C with outdoor air at 30°C, 50% RH:
- Outdoor air enthalpy: 64 kJ/kg_da
- Storage air enthalpy: -19 kJ/kg_da
- Enthalpy difference per air change: 83 kJ/kg_da

## ASHRAE Handbook References

Detailed enthalpy data, calculation procedures, and product-specific values are found in:

- **ASHRAE Handbook - Refrigeration, Chapter 19**: "Thermal Properties of Foods"
  - Tables R1-R9: Enthalpy values for various foods
  - Equations for composition-based calculations
  - Freezing point data

- **ASHRAE Handbook - Refrigeration, Chapter 28**: "Methods of Precooling Fruits, Vegetables, and Cut Flowers"
  - Cooling load calculations using enthalpy methods
  - Product-specific cooling requirements

- **ASHRAE Handbook - Refrigeration, Chapter 29**: "Industrial Food Freezing Systems"
  - Freezing time calculations incorporating enthalpy
  - Equipment sizing based on enthalpy removal rates

## Advanced Calculation Tools

Modern refrigeration load calculations use computational tools that integrate:

1. Transient heat transfer analysis with time-dependent boundary conditions
2. Variable specific heat and thermal conductivity with temperature
3. Ice crystal formation kinetics and supercooling effects
4. Multi-dimensional geometry for irregular product shapes

These tools solve the coupled heat and mass transfer equations numerically, providing more accurate results than simplified enthalpy methods for complex freezing scenarios.

However, enthalpy-based calculations remain essential for preliminary sizing, energy analysis, and understanding fundamental heat transfer requirements in refrigeration systems.

## Quality and Safety Implications

Enthalpy calculations inform critical temperature control decisions:

- **Freezing Rate**: Fast freezing (high enthalpy removal rate) produces small ice crystals, better preserving product quality
- **Thawing**: Controlled enthalpy addition prevents surface cooking while center remains frozen
- **Temperature Abuse**: Enthalpy changes during storage temperature fluctuations cause freeze-thaw damage
- **Cold Chain Management**: Cumulative enthalpy gain indicates product temperature history and remaining shelf life

Proper application of enthalpy principles ensures both energy-efficient refrigeration system design and maintenance of food product quality and safety throughout the cold chain.
