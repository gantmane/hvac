---
title: "Product Loads"
aliases: ["Product Loads"]
description: "Advanced technical analysis of product cooling loads in refrigerated facilities including sensible heat removal above and below freezing, latent heat of fusion, respiration heat loads, and product pulldown calculations for refrigeration system design using ASHRAE methods and thermodynamic principles"
weight: 4
---

Product loads represent the thermal energy that must be removed from stored commodities to reduce their temperature to storage conditions and maintain that temperature during the storage period. These loads constitute a significant portion of the total refrigeration load in cold storage facilities, distribution centers, and food processing operations.

## Fundamental Heat Transfer Components

Product cooling involves multiple heat transfer mechanisms that occur sequentially or simultaneously depending on the initial and final product temperatures relative to the freezing point.

### Sensible Heat Above Freezing

Sensible heat removal above the freezing point reduces product temperature without phase change. The heat removal rate is calculated using:

**Q_s1 = m × c_p1 × (T_initial - T_freeze)**

Where:
- Q_s1 = Sensible heat above freezing (Btu or kJ)
- m = Product mass (lb or kg)
- c_p1 = Specific heat above freezing (Btu/lb·°F or kJ/kg·°C)
- T_initial = Initial product temperature (°F or °C)
- T_freeze = Freezing point temperature (°F or °C)

The specific heat capacity above freezing varies with product composition, particularly water content. For most food products, the specific heat above freezing ranges from 0.70 to 0.95 Btu/lb·°F (2.93 to 3.98 kJ/kg·°C), with higher values corresponding to higher moisture content.

### Latent Heat of Fusion

When products are frozen, the latent heat of fusion must be removed to convert water within the product from liquid to solid phase. This represents the largest single heat load component during freezing operations.

**Q_L = m × w × h_if**

Where:
- Q_L = Latent heat of fusion (Btu or kJ)
- m = Product mass (lb or kg)
- w = Water content (decimal fraction of total mass)
- h_if = Latent heat of fusion of water = 144 Btu/lb (335 kJ/kg)

Not all water in food products freezes at 32°F (0°C) due to dissolved solids and bound water. The initial freezing point is depressed, and complete crystallization occurs over a temperature range. For practical calculations, 95% of freezable water is assumed to crystallize by 0°F (-18°C).

### Sensible Heat Below Freezing

After the phase change, additional sensible heat must be removed to reduce the frozen product temperature to final storage conditions.

**Q_s2 = m × c_p2 × (T_freeze - T_final)**

Where:
- Q_s2 = Sensible heat below freezing (Btu or kJ)
- c_p2 = Specific heat below freezing (Btu/lb·°F or kJ/kg·°C)
- T_final = Final storage temperature (°F or °C)

The specific heat of frozen products is significantly lower than unfrozen products, typically ranging from 0.35 to 0.50 Btu/lb·°F (1.47 to 2.09 kJ/kg·°C), depending on composition.

### Total Product Heat Load

For products cooled from above freezing to frozen storage conditions:

**Q_total = Q_s1 + Q_L + Q_s2**

**Q_total = m × [c_p1(T_initial - T_freeze) + w × h_if + c_p2(T_freeze - T_final)]**

## Thermophysical Properties of Common Products

Representative values for refrigeration load calculations:

| Product | Water Content (%) | c_p Above Freezing (Btu/lb·°F) | c_p Below Freezing (Btu/lb·°F) | Freezing Point (°F) |
|---------|-------------------|--------------------------------|-------------------------------|---------------------|
| Beef | 70-75 | 0.77 | 0.40 | 28 to 29 |
| Pork | 60-68 | 0.70 | 0.38 | 28 to 30 |
| Chicken | 74-76 | 0.79 | 0.41 | 27 to 29 |
| Fish (lean) | 75-82 | 0.82 | 0.42 | 28 to 30 |
| Apples | 84-88 | 0.87 | 0.45 | 29 to 30 |
| Oranges | 86-88 | 0.89 | 0.46 | 30 to 31 |
| Lettuce | 94-96 | 0.96 | 0.48 | 31 to 32 |
| Potatoes | 77-80 | 0.82 | 0.43 | 30 to 31 |
| Milk | 87-88 | 0.93 | 0.46 | 31 |
| Eggs | 74-76 | 0.76 | 0.40 | 30 to 31 |
| Butter | 15-16 | 0.64 | 0.34 | 34 to 36 |
| Ice cream | 60-65 | 0.70 | 0.38 | 22 to 28 |

Reference: ASHRAE Handbook - Refrigeration, Chapter 19, Thermal Properties of Foods.

## Respiration Heat Loads

Living products (fruits, vegetables, flowers) continue metabolic activity after harvest, generating heat through respiration. This heat must be continuously removed throughout the storage period.

### Respiration Heat Generation

Respiration converts carbohydrates, proteins, and fats to carbon dioxide, water, and heat. The rate of heat generation depends on:

- Product type and variety
- Temperature
- Oxygen and carbon dioxide concentrations
- Product maturity and condition
- Time since harvest

The respiration rate follows an exponential relationship with temperature, approximately doubling for every 18°F (10°C) increase in temperature. This relationship is expressed by the temperature coefficient Q_10:

**r_2 = r_1 × Q_10^[(T_2 - T_1)/18]**

Where:
- r_1, r_2 = Respiration rates at temperatures T_1 and T_2
- Q_10 = Temperature coefficient (typically 2.0 to 3.5 for most products)
- T_1, T_2 = Temperatures (°F)

### Heat of Respiration Data

Heat generation rates at specific temperatures for selected products:

| Product | Heat of Respiration (Btu/ton·day) |  |  |
|---------|-----------------------------------|---|---|
|         | 32°F (0°C) | 41°F (5°C) | 50°F (10°C) |
| Apples (mature) | 1,000-1,500 | 1,800-2,700 | 3,200-5,000 |
| Asparagus | 14,000-18,000 | 26,000-35,000 | 50,000-70,000 |
| Bananas (green) | 2,500-3,500 | 4,500-6,500 | 9,000-13,000 |
| Broccoli | 8,000-12,000 | 15,000-22,000 | 28,000-42,000 |
| Carrots (topped) | 2,200-3,000 | 3,800-5,200 | 7,000-10,000 |
| Grapes | 600-900 | 1,100-1,600 | 2,000-3,000 |
| Lettuce (head) | 2,400-3,200 | 4,200-5,800 | 7,800-11,400 |
| Mushrooms | 14,000-20,000 | 26,000-38,000 | 50,000-75,000 |
| Onions (dry) | 600-900 | 1,000-1,500 | 1,800-2,700 |
| Oranges | 1,200-1,800 | 2,100-3,200 | 3,900-6,000 |
| Peaches | 1,200-1,800 | 2,200-3,300 | 4,200-6,500 |
| Potatoes | 1,000-1,400 | 1,800-2,500 | 3,200-4,700 |
| Strawberries | 4,000-6,000 | 7,500-11,500 | 14,000-22,000 |
| Tomatoes (mature green) | 1,600-2,400 | 2,900-4,400 | 5,500-8,500 |
| Tomatoes (ripe) | 2,400-3,600 | 4,400-6,600 | 8,500-13,000 |

Reference: ASHRAE Handbook - Refrigeration, Chapter 21, Cargo of Fruits and Vegetables, Tables 2-5.

The respiration heat load for a storage facility is calculated as:

**Q_resp = (m/2000) × r × SF**

Where:
- Q_resp = Respiration heat load (Btu/day or Btu/h)
- m = Product mass (lb)
- r = Heat of respiration (Btu/ton·day)
- SF = Safety factor (1.1 to 1.3 to account for variation)

For hourly load calculations:

**Q_resp(hourly) = Q_resp(daily) / 24**

## Product Pulldown Calculations

Product pulldown refers to the initial cooling of product from receiving temperature to storage temperature. This calculation determines the peak refrigeration capacity required and cooling time.

### Average Cooling Load Method

The average cooling load during pulldown is calculated using the total heat removal divided by the pulldown time:

**Q_avg = Q_total / t_pulldown**

Where:
- Q_avg = Average cooling load (Btu/h or kW)
- Q_total = Total heat to be removed (Btu or kJ)
- t_pulldown = Desired pulldown time (h)

### Design Pulldown Times

Typical design pulldown times for various applications:

| Application | Product Type | Pulldown Time |
|-------------|--------------|---------------|
| Cold storage warehouse | General commodities | 12-24 hours |
| Blast freezer | Packaged meat products | 4-8 hours |
| Quick freeze tunnel | Individually quick frozen (IQF) | 0.5-2 hours |
| Cooler receiving dock | Fresh produce | 4-12 hours |
| Precooling room | Fruits and vegetables | 6-18 hours |
| Chill room | Meat carcasses | 24-48 hours |
| Milk cooling | Bulk milk in tank | 2-3 hours |

### Peak Load Factor

The instantaneous peak load during initial pulldown typically exceeds the average load due to the temperature difference being maximum at the start. A peak load factor accounts for this:

**Q_peak = Q_avg × PLF**

Where:
- Q_peak = Peak instantaneous load (Btu/h or kW)
- PLF = Peak load factor (typically 1.3 to 1.8)

For systems with continuous product flow (such as conveyor freezers), the load is steady-state and PLF = 1.0.

### Transient Cooling Analysis

For accurate pulldown calculations, the cooling process follows a first-order exponential decay when the product is exposed to constant air temperature:

**(T_product - T_air) / (T_initial - T_air) = e^(-t/τ)**

Where:
- T_product = Product temperature at time t (°F or °C)
- T_air = Refrigerated air temperature (°F or °C)
- T_initial = Initial product temperature (°F or °C)
- t = Time (h)
- τ = Time constant (h)

The time constant depends on product mass, specific heat, surface area, and heat transfer coefficient:

**τ = (m × c_p) / (h × A)**

Where:
- h = Surface heat transfer coefficient (Btu/h·ft²·°F or W/m²·K)
- A = Product surface area (ft² or m²)

### Heat Transfer Coefficients

Surface heat transfer coefficients for product cooling:

| Condition | Heat Transfer Coefficient h |
|-----------|------------------------------|
| | Btu/h·ft²·°F | W/m²·K |
| Still air (natural convection) | 1.0-1.5 | 5-8 |
| Low velocity forced air (100-200 fpm) | 2-4 | 11-23 |
| Moderate velocity forced air (400-600 fpm) | 5-9 | 28-51 |
| High velocity forced air (1000-2000 fpm) | 10-20 | 57-114 |
| Immersion cooling (water or brine) | 50-200 | 284-1135 |
| Package-to-package contact | 0.3-0.8 | 1.7-4.5 |

Reference: ASHRAE Handbook - Refrigeration, Chapter 20, Cooling and Freezing Times of Foods.

## Equivalent Heat Per Unit Volume

For facility design, product loads are often expressed as heat per unit volume of storage space:

**q_v = (Q_total × ρ_apparent) / (V × t_pulldown)**

Where:
- q_v = Heat load per unit volume (Btu/h·ft³ or W/m³)
- ρ_apparent = Apparent product density including packaging and air spaces (lb/ft³ or kg/m³)
- V = Storage volume (ft³ or m³)

Typical apparent densities for storage facilities:

| Product Category | Apparent Density (lb/ft³) |
|------------------|---------------------------|
| Boxed beef | 35-45 |
| Hanging beef carcasses | 18-25 |
| Boxed poultry | 30-40 |
| Frozen fish | 30-38 |
| Packaged vegetables | 25-35 |
| Apples in bins | 32-40 |
| Citrus in bins | 35-42 |
| Dairy products (mixed) | 28-36 |
| Ice cream | 18-24 |

## Load Calculation Example

Calculate the refrigeration load to freeze 20,000 lb of beef from 38°F to -10°F storage temperature in 12 hours.

Given data:
- m = 20,000 lb
- T_initial = 38°F
- T_final = -10°F
- T_freeze = 28°F
- c_p1 = 0.77 Btu/lb·°F
- c_p2 = 0.40 Btu/lb·°F
- w = 0.72 (72% water content)
- h_if = 144 Btu/lb
- t_pulldown = 12 h

**Step 1: Sensible heat above freezing**

Q_s1 = 20,000 × 0.77 × (38 - 28) = 154,000 Btu

**Step 2: Latent heat of fusion**

Q_L = 20,000 × 0.72 × 144 = 2,073,600 Btu

**Step 3: Sensible heat below freezing**

Q_s2 = 20,000 × 0.40 × (28 - (-10)) = 304,000 Btu

**Step 4: Total heat removal**

Q_total = 154,000 + 2,073,600 + 304,000 = 2,531,600 Btu

**Step 5: Average cooling load**

Q_avg = 2,531,600 / 12 = 210,967 Btu/h = 17.6 tons

**Step 6: Peak load (using PLF = 1.5)**

Q_peak = 210,967 × 1.5 = 316,450 Btu/h = 26.4 tons

Note that the latent heat of fusion represents 82% of the total heat load, illustrating the dominant energy requirement for freezing operations.

## Product Loading Patterns

The timing and rate of product loading significantly affect refrigeration system sizing and operation.

### Continuous Loading

Products enter and leave storage continuously, maintaining relatively constant refrigeration load. Common in distribution centers and cross-dock facilities.

**Q_design = Q_avg × 1.1 to 1.2**

The factor accounts for minor fluctuations but assumes steady-state operation.

### Batch Loading

Products are loaded periodically in discrete batches. Common in cold storage warehouses and seasonal processing facilities.

**Q_design = Q_peak × Simultaneous Load Factor**

The simultaneous load factor (0.6 to 0.8) accounts for the probability that not all storage zones reach peak load simultaneously.

### Seasonal Loading

Product intake varies significantly by season. Refrigeration capacity must accommodate peak season while operating efficiently during low-demand periods.

Design capacity: Based on maximum anticipated load during peak season with sufficient margin for above-average harvest years (1.15 to 1.25 factor).

## Product Packaging Effects

Packaging material and configuration impact heat transfer rates and total product load.

### Packaging Material Heat Load

The sensible heat of packaging materials must be included:

**Q_pkg = m_pkg × c_pkg × ΔT**

Where:
- m_pkg = Packaging mass (lb or kg)
- c_pkg = Specific heat of packaging material (Btu/lb·°F or kJ/kg·°C)

Typical packaging material specific heats:

| Material | Specific Heat (Btu/lb·°F) |
|----------|---------------------------|
| Corrugated cardboard | 0.33 |
| Wood (pallets, crates) | 0.45 |
| Polyethylene (film, bags) | 0.55 |
| Polystyrene (foam) | 0.32 |
| Aluminum | 0.22 |
| Steel | 0.12 |

For typical commercial packaging, packaging mass ranges from 3% to 8% of product mass.

### Packaging Thermal Resistance

Insulating packaging reduces heat transfer rate, extending pulldown time. The thermal resistance of packaging must be included in transient cooling calculations:

**R_pkg = t_pkg / k_pkg**

Where:
- R_pkg = Thermal resistance (h·ft²·°F/Btu or m²·K/W)
- t_pkg = Packaging thickness (ft or m)
- k_pkg = Thermal conductivity (Btu/h·ft·°F or W/m·K)

## Design Considerations

Key factors for product load calculations in refrigeration system design:

1. **Accurate product data**: Obtain specific thermophysical properties, initial temperatures, and loading rates from facility operators or historical records.

2. **Safety factors**: Apply appropriate factors (1.1 to 1.3) to calculated loads to account for uncertainties and variations in product properties, ambient conditions, and operational practices.

3. **Diversity**: In large facilities with multiple storage zones, apply diversity factors (0.7 to 0.9) recognizing that not all zones reach peak load simultaneously.

4. **Respiration loads**: For produce facilities, respiration heat can represent 10% to 30% of total load and must not be neglected.

5. **Product turnover rate**: Higher turnover rates increase average product load as pulldown operations occur more frequently.

6. **Load profile**: Document hourly and seasonal load profiles to optimize equipment selection, staging, and energy management strategies.

7. **Measurement verification**: Where possible, verify calculated loads against measured data from similar existing facilities or pilot operations.

Product loads, while calculable from first principles, benefit significantly from experience with specific products and operating conditions. Collaboration between refrigeration engineers and facility operators ensures realistic load estimates and successful system performance.

## References

- ASHRAE Handbook - Refrigeration, Chapter 19: Thermal Properties of Foods
- ASHRAE Handbook - Refrigeration, Chapter 20: Cooling and Freezing Times of Foods
- ASHRAE Handbook - Refrigeration, Chapter 21: Cargo of Fruits and Vegetables
- ASHRAE Handbook - Refrigeration, Chapter 24: Refrigeration Load Calculations
