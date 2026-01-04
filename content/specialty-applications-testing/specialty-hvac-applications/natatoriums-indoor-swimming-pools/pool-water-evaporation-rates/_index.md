---
title: "Pool Water Evaporation Rate Calculations"
weight: 1
description: "Detailed analysis of pool water evaporation calculation methods including Carrier, Shah, and ASHRAE formulas, activity factors, and latent load determination for natatorium HVAC design."
keywords: "pool evaporation calculation, Carrier equation, Shah method, ASHRAE evaporation formula, latent load calculation, natatorium moisture load"
---

Accurate determination of pool water evaporation rates is fundamental to natatorium HVAC system design. The evaporation rate directly determines the dehumidification equipment capacity, ventilation requirements, pool heating load, and energy consumption. Underestimating evaporation leads to inadequate humidity control and potential condensation damage; overestimating results in oversized, inefficient equipment.

## Physical Principles of Evaporation

Pool water evaporation is a mass transfer process governed by the vapor pressure difference between the water surface and surrounding air. The driving force for evaporation is the difference between the saturation vapor pressure at the water surface temperature and the partial pressure of water vapor in the air above the surface.

The rate of moisture transfer depends on:

1. **Temperature difference** between water and air (affects saturation pressure)
2. **Humidity of air** (affects vapor pressure gradient)
3. **Air velocity** across water surface (affects boundary layer resistance)
4. **Water surface area** exposed to air
5. **Activity level** (agitation increases effective surface area and disrupts boundary layer)
6. **Barometric pressure** (affects absolute vapor pressures)

Heat transfer accompanies mass transfer, as each pound of water evaporated requires approximately 1,040 Btu of latent heat of vaporization. This energy is extracted from the pool water, representing a major component of pool heating load.

## Carrier Equation

The Carrier equation, developed empirically for swimming pool applications, is widely used for preliminary calculations:

**W = A × F × (P_w - P_a)**

Where:
- W = Evaporation rate (lb/h)
- A = Pool water surface area (ft²)
- F = Activity factor (dimensionless)
- P_w = Saturation vapor pressure at pool water temperature (in. Hg)
- P_a = Partial pressure of water vapor in room air (in. Hg)

**Activity Factors (F)**:
- Unoccupied pool: 0.5
- Residential pool, light use: 0.65
- Public pool, moderate use: 0.8
- Public pool, heavy use: 1.0
- Wave pools, water slides: 1.5
- Whirlpools, spas: 1.0-2.0

The vapor pressure difference (P_w - P_a) represents the thermodynamic driving force. Saturation vapor pressure increases exponentially with temperature following the Clausius-Clapeyron relationship. At 80°F water temperature, saturation pressure is approximately 1.03 in. Hg. If room air is maintained at 82°F and 50% RH, the partial pressure of water vapor is approximately 0.52 in. Hg, yielding a pressure difference of 0.51 in. Hg.

**Example Calculation**:

For a 1,500 ft² competitive pool:
- Water temperature: 80°F (P_w = 1.03 in. Hg)
- Air temperature: 82°F, 50% RH (P_a = 0.52 in. Hg)
- Activity factor: 0.8 (moderate use)

W = 1,500 × 0.8 × (1.03 - 0.52) = 1,500 × 0.8 × 0.51 = 612 lb/h

Latent load = 612 lb/h × 1,040 Btu/lb = 636,480 Btu/h = 53.0 tons

This represents the dehumidification capacity required under design conditions.

## Shah Equation

The Shah equation incorporates air velocity effects and provides more detailed physics-based calculation:

**W = (95 + 0.425 × V_air) × A × (P_w - P_a) / Y**

Where:
- W = Evaporation rate (lb/h)
- V_air = Air velocity at water surface (fpm)
- A = Pool water surface area (ft²)
- P_w = Saturation vapor pressure at water surface temperature (in. Hg)
- P_a = Partial pressure of water vapor in air (in. Hg)
- Y = Latent heat of vaporization (approximately 1,040 Btu/lb at typical temperatures)

The coefficient (95 + 0.425 × V_air) represents the combined effects of natural convection and forced convection. At low air velocities (<30 fpm recommended for unoccupied pools), natural convection dominates. Higher velocities increase evaporation significantly—a key reason for maintaining low air movement across pool surfaces.

**Example Calculation**:

Same pool as above, with air velocity = 25 fpm:

W = (95 + 0.425 × 25) × 1,500 × (1.03 - 0.52) / 1,040

W = (95 + 10.625) × 1,500 × 0.51 / 1,040

W = 105.625 × 1,500 × 0.51 / 1,040 = 77.7 lb/h (unoccupied)

For occupied conditions, multiply by activity factor (~1.5-2.0 for moderate activity), yielding approximately 116-155 lb/h. The Shah equation typically produces lower baseline evaporation rates than Carrier but requires modification for activity.

## ASHRAE Method

The ASHRAE Handbook provides a comprehensive approach combining empirical data with theoretical models:

**W = 0.1 × A × F_a × (P_w - P_a)**

Where:
- W = Evaporation rate (lb/h)
- A = Pool water surface area (ft²)
- F_a = Activity factor
- P_w = Saturation pressure at water temperature (lb/ft²)
- P_a = Vapor pressure in air (lb/ft²)

Note: When using lb/ft² for pressure units, the constant is 0.1. When using in. Hg, constants range from 0.5 to 1.0 depending on activity.

**ASHRAE Activity Factors**:
- Unoccupied, still air: 0.5-0.6
- Residential, light use: 0.65-0.75
- Public, moderate use: 0.8-0.9
- Public, heavy use: 1.0-1.1
- Wavy, agitated: 1.5-2.0

ASHRAE recommends using higher activity factors for sizing dehumidification equipment to ensure adequate capacity during peak use. Conservative design typically uses F_a = 1.0 for public pools even if typical use is moderate.

## Design Recommendations

| Calculation Method | Best Application | Typical Result |
|-------------------|------------------|----------------|
| Carrier Equation | Preliminary sizing, public pools | Higher evaporation rates |
| Shah Equation | Detailed design, velocity-sensitive | Lower baseline, requires activity multiplier |
| ASHRAE Method | General design, conservative | Mid-range, well-validated |

**Design Practice**:

1. Calculate evaporation using all three methods
2. Use highest result for equipment sizing to ensure adequate capacity
3. Verify air velocity assumptions (should be <30 fpm at water surface when unoccupied)
4. Consider transient conditions: pool covers reduce evaporation by 90-95% when in place
5. Account for splash-out, which can add 10-20% to moisture load in heavy-use facilities
6. Include safety factor of 10-20% for equipment selection

## Load Calculation Procedure

**Step 1: Determine Design Conditions**

- Pool water temperature (typically 78-84°F depending on use)
- Indoor air temperature (typically T_water + 2-4°F)
- Design relative humidity (typically 50-60%)
- Pool surface area (exclude area covered by lane lines, diving boards, etc.)
- Expected activity level (peak use scenario)

**Step 2: Calculate Vapor Pressures**

Use psychrometric relationships or steam tables:

P_w = saturation pressure at water temperature

P_a = RH × (saturation pressure at air temperature)

**Step 3: Apply Evaporation Equation**

Use selected method(s) with appropriate activity factor.

**Step 4: Calculate Latent Load**

Q_latent = W × h_fg

Where h_fg ≈ 1,040 Btu/lb (or use exact value from steam tables at water temperature)

**Step 5: Calculate Pool Heat Loss**

Pool heating must replace:
- Evaporative heat loss (from Step 4)
- Convective heat loss to air (if air is cooler than water)
- Conductive heat loss through pool walls/floor
- Radiation heat loss to cool surfaces
- Fresh water makeup heating
- Conductive heat loss through plumbing

Evaporation typically represents 60-80% of total pool heat loss in indoor facilities.

## Humidity Ratio Calculations

For dehumidification system sizing, calculate the moisture removal rate in terms of humidity ratio change:

Δω = W / (ρ_air × Q_air)

Where:
- Δω = Change in humidity ratio (lb_water/lb_dry air)
- W = Evaporation rate (lb/h)
- ρ_air = Air density (approximately 0.075 lb/ft³ at standard conditions)
- Q_air = Air circulation rate (cfm)

This determines the required apparatus dewpoint temperature for the cooling/dehumidification coil.

## Verification and Monitoring

After installation, verify design assumptions:

- Measure actual pool water evaporation by tracking makeup water addition over extended periods
- Monitor relative humidity during various occupancy and weather conditions
- Verify air velocities across pool surface
- Adjust dehumidification setpoints based on actual performance

Actual evaporation rates may vary ±30% from calculated values due to variations in activity, air movement patterns, and water chemistry effects. Proper system design includes capacity modulation to accommodate this variability while maintaining energy efficiency.

## Summary

Evaporation rate calculation is the foundation of natatorium HVAC design. Use conservative assumptions for equipment sizing while providing adequate turndown for part-load operation. The Carrier equation with appropriate activity factors provides reliable results for most applications. Complex facilities with unusual geometry, high occupancy variability, or special features (wave pools, waterslides) may warrant CFD analysis or specialized consulting to refine evaporation estimates.
