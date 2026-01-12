---
title: "Evaporators"
weight: 3
description: "Comprehensive technical guide to refrigeration evaporators including DX and flooded types, heat transfer analysis, superheat control, fin configurations, defrost methods, and capacity calculations using LMTD and effectiveness-NTU methods."
---

Evaporators absorb heat from the refrigerated space or fluid by evaporating liquid refrigerant at low pressure and temperature. The evaporator represents the heat absorption component in the refrigeration cycle, where the refrigerant undergoes a phase change from liquid to vapor while extracting thermal energy from the load.

## Evaporator Classification

### Direct Expansion (DX) Evaporators

DX evaporators feed liquid refrigerant through an expansion device (TXV or electronic expansion valve) where the refrigerant evaporates as it flows through the coil. The refrigerant exits as superheated vapor. DX evaporators are characterized by:

- Refrigerant-side pressure drop throughout the coil
- Superheat control at the coil outlet (typically 8-12°F)
- High heat transfer coefficients in the two-phase region
- Reduced charge compared to flooded designs
- Sensitivity to refrigerant distribution in multi-circuit coils

The heat transfer in DX evaporators occurs in three distinct zones: subcooled liquid entry, two-phase evaporation (where most heat transfer occurs), and superheated vapor exit.

### Flooded Evaporators

Flooded evaporators maintain liquid refrigerant level using a float valve or liquid level control. The refrigerant boils at nearly constant temperature and pressure throughout the evaporator. Key characteristics:

- Uniform heat transfer coefficient across the heat exchange surface
- Refrigerant exits as saturated or slightly superheated vapor
- Requires liquid-vapor separator after the evaporator
- Higher refrigerant charge than DX systems
- Excellent for large-capacity applications with multiple evaporators
- Temperature glide is minimized with zeotropic refrigerants

Flooded evaporators provide superior heat transfer performance because the entire surface remains wetted with liquid refrigerant, maintaining high boiling heat transfer coefficients.

### Falling-Film Evaporators

Falling-film evaporators distribute liquid refrigerant over the top of vertical or horizontal tubes, where it flows as a thin film while evaporating. This configuration provides:

- Very high heat transfer coefficients (thin film reduces thermal resistance)
- Low refrigerant charge
- Minimal pressure drop on refrigerant side
- Excellent oil return characteristics
- Common in large-tonnage chillers and industrial refrigeration

The film thickness typically ranges from 0.5 to 2 mm, requiring precise distribution to ensure complete wetting without flooding.

## Heat Transfer Fundamentals

The overall heat transfer rate in an evaporator is expressed as:

Q = UA × LMTD

Where:
- Q = heat transfer rate (Btu/hr or kW)
- U = overall heat transfer coefficient (Btu/hr·ft²·°F or W/m²·K)
- A = heat transfer surface area (ft² or m²)
- LMTD = log mean temperature difference (°F or K)

The overall heat transfer coefficient is determined by:

1/U = 1/h_i + R_f,i + t_w/k_w + R_f,o + 1/(η_o × h_o)

Where:
- h_i = inside (refrigerant-side) heat transfer coefficient
- R_f,i = inside fouling resistance
- t_w = tube wall thickness
- k_w = tube wall thermal conductivity
- R_f,o = outside fouling resistance
- η_o = outside surface efficiency (accounts for fin effectiveness)
- h_o = outside (air or fluid-side) heat transfer coefficient

### Refrigerant-Side Heat Transfer

Boiling heat transfer in evaporators occurs through two mechanisms:

**Nucleate boiling** dominates at low vapor qualities, where bubbles form at nucleation sites on the tube surface. The heat transfer coefficient is:

h_nb ∝ q^0.7

Where q is the heat flux. This relationship shows that nucleate boiling coefficient increases with heat flux.

**Convective evaporation** dominates at high vapor qualities, where heat transfer depends on the two-phase flow regime (annular flow provides highest coefficients).

### Log Mean Temperature Difference (LMTD)

For counterflow or parallel flow arrangements:

LMTD = (ΔT_1 - ΔT_2) / ln(ΔT_1 / ΔT_2)

For evaporators with constant refrigerant temperature (flooded type):

LMTD = (T_in - T_out) / ln[(T_in - T_evap) / (T_out - T_evap)]

Where T_in and T_out are the inlet and outlet temperatures of the cooled fluid or air.

### Effectiveness-NTU Method

The effectiveness-NTU method is particularly useful when outlet temperatures are unknown:

ε = Q / Q_max = (T_in - T_out) / (T_in - T_evap)

NTU = UA / C_min

Where C_min is the minimum heat capacity rate (ṁ × cp). For evaporators with constant refrigerant temperature, the refrigerant side has infinite heat capacity, making the cooled fluid side C_min.

For this configuration:
ε = 1 - exp(-NTU)

## Superheat Control

Superheat is the temperature difference between the actual refrigerant vapor temperature and the saturation temperature at the evaporator pressure:

ΔT_sh = T_vapor - T_sat

Proper superheat control ensures:

- Complete evaporation before the compressor (prevents liquid slugging)
- Maximum utilization of heat transfer surface
- Stable system operation
- Protection of compressor from liquid floodback

**Thermostatic expansion valves (TXV)** maintain superheat by modulating refrigerant flow based on the difference between evaporator outlet temperature and evaporator pressure (converted to saturation temperature). Typical superheat settings:

- Air conditioning: 8-12°F
- Medium-temperature refrigeration: 6-10°F
- Low-temperature refrigeration: 4-8°F
- Suction line length affects required superheat

**Electronic expansion valves (EEV)** use temperature and pressure sensors with PID control algorithms to maintain precise superheat, providing better stability and efficiency, especially during load variations.

## Air-Cooling vs Liquid-Cooling Evaporators

### Air-Cooling Evaporators

Air-cooling evaporators (finned coils) cool air directly and are characterized by:

- Low air-side heat transfer coefficient (2-5 Btu/hr·ft²·°F for natural convection, 5-15 for forced convection)
- Extended surface (fins) required to compensate for low h_o
- Face velocities typically 300-600 fpm for comfort cooling, 200-400 fpm for refrigeration
- Fin spacing affects frost accumulation and pressure drop
- Temperature difference (TD) between air inlet and refrigerant saturation: 10-20°F for comfort cooling, 8-15°F for medium-temp refrigeration

### Liquid-Cooling Evaporators

Liquid-cooling evaporators (shell-and-tube, plate heat exchangers) provide:

- High liquid-side heat transfer coefficient (200-1000+ Btu/hr·ft²·°F for water)
- Compact design due to efficient heat transfer
- Lower approach temperatures possible (3-5°F)
- Typical water velocity: 3-10 fps (prevents settling, limits erosion)
- Minimum water temperature must remain above freezing (glycol solutions for temperatures below 40°F)

## Fin Configurations

Fin geometry significantly affects evaporator performance:

**Fin spacing:**
- 8-10 FPI (fins per inch): low-temperature applications, frequent defrost
- 10-14 FPI: medium-temperature refrigeration
- 14-18 FPI: air conditioning (no frost conditions)

**Fin types:**
- Plate fins (flat): simplest, lowest cost
- Wavy fins: enhanced air-side heat transfer (15-25% improvement)
- Louvered fins: highest performance, increased pressure drop
- Spine fins: used in low-frost applications

**Fin efficiency** reduces with increasing fin height and decreasing thermal conductivity:

η_f = tanh(mL) / (mL)

Where m = √(2h/kt) and L is the fin height from base to tip.

Aluminum fins (k = 130 Btu/hr·ft·°F) provide 90-95% efficiency for typical geometries. Copper fins offer marginal improvement at higher cost.

## Defrost Methods

Frost accumulation on air-cooling evaporators operating below 32°F reduces airflow and heat transfer capacity. Defrost methods include:

**Electric defrost:**
- Electric resistance heaters energized during defrost cycle
- Defrost termination at 45-55°F coil temperature
- Power consumption: 15-25% of refrigeration capacity
- Simple control, predictable duration

**Hot gas defrost:**
- Hot refrigerant gas from compressor discharge bypasses condenser
- Fastest defrost method (15-30 minutes)
- Energy efficient (captures heat from discharge gas)
- Requires additional piping and controls
- Pan heaters still required for drain system

**Off-cycle defrost (air defrost):**
- Refrigeration stops, fans continue or ambient air circulates
- Only effective for spaces above 40°F
- Slowest method (1-2 hours)
- Zero energy cost for defrost

**Water defrost:**
- Spray water over coil surface
- Very fast (10-15 minutes)
- High water and energy consumption for heating water
- Rarely used except in industrial applications

Defrost frequency depends on operating conditions (coil temperature, humidity, airflow). Typical intervals: 4-6 times per 24 hours for low-temperature applications.

## Capacity Calculations and Selection

Evaporator capacity must account for all heat loads:

**Product load:**
Q_product = ṁ × cp × ΔT + ṁ × h_fg (if phase change occurs)

**Transmission load:**
Q_transmission = U × A × ΔT (through walls, floor, ceiling)

**Infiltration load:**
Q_infiltration = ṁ_air × Δh (sensible and latent)

**Internal loads:**
Q_internal = lighting + equipment + occupants

**Total capacity:**
Q_total = Q_product + Q_transmission + Q_infiltration + Q_internal

**Safety factor:** 10-20% typically applied to account for future expansion and uncertainty in load calculations.

Evaporator selection considers:

1. Required capacity at design conditions
2. Allowable temperature difference (affects product quality, dehumidification)
3. Available space and airflow patterns
4. Defrost requirements and method
5. Refrigerant pressure drop (affects system efficiency)
6. First cost vs operating cost optimization

## Application-Specific Considerations

**Comfort cooling:**
- Coil entering air: 75-80°F DB, 50-65% RH
- Refrigerant temperature: 38-45°F (DX systems)
- Emphasis on dehumidification (sensible heat ratio 0.70-0.80)
- Face velocity: 300-500 fpm

**Medium-temperature refrigeration (28-50°F):**
- High relative humidity maintenance (85-95%) to minimize product moisture loss
- Unit cooler capacity includes defrost heat load
- Low air velocity across products (prevents desiccation)
- Temperature difference: 8-12°F

**Low-temperature refrigeration (-20 to 0°F):**
- Frequent defrost required
- Large fin spacing (6-8 FPI) to accommodate frost
- Hot gas defrost preferred for efficiency
- Multiple circuits for reliable operation

**Process cooling:**
- Precise temperature control (±1-2°F)
- May require glycol secondary loop for freeze protection
- Shell-and-tube or plate evaporators common
- Fouling factors critical in selection

ASHRAE Refrigeration Handbook provides detailed selection procedures, performance data, and application guidelines for all evaporator types.

## Performance Degradation Factors

Evaporator capacity decreases due to:

- Frost accumulation (up to 50% capacity loss before defrost)
- Reduced airflow (dirty filters, blocked coils): 2-3% per 10% airflow reduction
- Oil accumulation in tubes (flooded systems): 5-15% capacity loss with 1-2% oil concentration
- Refrigerant maldistribution (DX coils): some circuits starved, others flooded
- Non-condensables in system: increases evaporator pressure, reduces capacity

Regular maintenance and proper system design minimize these degradation factors and maintain design capacity throughout the equipment life.
