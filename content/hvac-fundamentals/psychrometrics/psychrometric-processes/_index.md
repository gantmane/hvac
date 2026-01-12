---
title: "Psychrometric Processes"
description: "Detailed analysis of psychrometric processes including sensible heating, cooling, humidification, dehumidification, evaporative cooling, and mixed air calculations with process plotting methods for HVAC system design"
weight: 3
---

Psychrometric processes represent the thermodynamic transformations that air undergoes as it moves through HVAC systems. Understanding these processes is fundamental to system design, control strategy development, and energy analysis. Each process follows a specific path on the psychrometric chart, defined by the physical mechanisms driving the change in air properties.

## Sensible Heating Process

Sensible heating adds thermal energy to air without changing its moisture content. The process follows a horizontal line on the psychrometric chart, moving from left to right at constant humidity ratio.

**Process Characteristics:**
- Dry-bulb temperature increases
- Humidity ratio remains constant (ω = constant)
- Relative humidity decreases
- Enthalpy increases
- Dew point temperature remains constant

The sensible heating equation:

Q_sensible = ṁ_da × c_p × ΔT = ṁ_da × c_p × (T_2 - T_1)

where:
- Q_sensible = sensible heating rate (Btu/hr or W)
- ṁ_da = dry air mass flow rate (lb_da/hr or kg_da/s)
- c_p = specific heat of air at constant pressure (0.24 Btu/lb_da·°F or 1.006 kJ/kg_da·K)
- T_1, T_2 = initial and final dry-bulb temperatures

**Common Applications:**
- Heating coils using hot water or steam
- Electric resistance heaters
- Gas-fired furnaces
- Heat recovery devices

## Sensible Cooling Process

Sensible cooling removes thermal energy without condensation. The process follows a horizontal line on the psychrometric chart, moving from right to left at constant humidity ratio.

**Process Characteristics:**
- Dry-bulb temperature decreases
- Humidity ratio remains constant (ω = constant)
- Relative humidity increases
- Enthalpy decreases
- Dew point temperature remains constant

The process continues as sensible cooling only if the cooling coil surface temperature remains above the dew point of the air. Once the coil surface temperature drops below the dew point, the process transitions to cooling with dehumidification.

| Parameter | Initial State | Final State | Change |
|-----------|---------------|-------------|---------|
| Dry-bulb temperature | T_1 | T_2 | Decreases |
| Humidity ratio | ω | ω | Constant |
| Relative humidity | φ_1 | φ_2 | Increases |
| Enthalpy | h_1 | h_2 | Decreases |

## Cooling with Dehumidification

Cooling with dehumidification occurs when air contacts a surface below its dew point temperature, causing simultaneous sensible and latent cooling. The process line slopes downward and to the left on the psychrometric chart.

**Process Characteristics:**
- Dry-bulb temperature decreases
- Humidity ratio decreases
- Relative humidity increases initially, reaches saturation at coil surface
- Enthalpy decreases (both sensible and latent components)
- Dew point temperature decreases

**Total Cooling Equation:**

Q_total = Q_sensible + Q_latent = ṁ_da × (h_1 - h_2)

Q_sensible = ṁ_da × c_p × (T_1 - T_2)

Q_latent = ṁ_da × h_fg × (ω_1 - ω_2)

where:
- h_fg = latent heat of vaporization (approximately 1061 Btu/lb or 2465 kJ/kg at standard conditions)
- ω_1, ω_2 = initial and final humidity ratios

**Apparatus Dew Point (ADP):**
The apparatus dew point represents the effective surface temperature of the cooling coil. The process line extends from the entering air condition toward the ADP. The bypass factor determines how closely the leaving air condition approaches the ADP:

BF = (T_leaving - T_ADP) / (T_entering - T_ADP)

Contact factor: CF = 1 - BF

Lower bypass factors indicate better coil performance and closer approach to the ADP.

| Coil Configuration | Typical Bypass Factor | Rows Deep |
|-------------------|----------------------|-----------|
| 3-row coil, 8 fins/inch | 0.30 - 0.50 | 3 |
| 4-row coil, 8 fins/inch | 0.20 - 0.30 | 4 |
| 6-row coil, 12 fins/inch | 0.10 - 0.20 | 6 |
| 8-row coil, 14 fins/inch | 0.05 - 0.10 | 8 |

## Humidification Processes

Humidification increases the moisture content of air through several methods, each following a distinct path on the psychrometric chart.

**Steam Humidification:**
Injecting steam into an airstream adds both moisture and thermal energy. The process line slopes upward and to the right, approximately following a line of constant wet-bulb temperature.

- Dry-bulb temperature increases slightly (due to sensible heat from steam)
- Humidity ratio increases significantly
- Relative humidity increases
- Enthalpy increases substantially

Steam addition rate:

ṁ_steam = ṁ_da × (ω_2 - ω_1)

**Water Spray Humidification (Adiabatic):**
Spraying water into an airstream causes evaporative humidification. If the water is at the wet-bulb temperature of the entering air, the process is adiabatic, following a line of constant wet-bulb temperature (constant enthalpy on standard psychrometric charts).

- Dry-bulb temperature decreases
- Humidity ratio increases
- Wet-bulb temperature remains approximately constant
- Enthalpy remains approximately constant
- Process approaches saturation

**Efficiency of Adiabatic Humidification:**

η = (ω_2 - ω_1) / (ω_sat@WBT - ω_1)

where ω_sat@WBT is the humidity ratio at saturation at the entering wet-bulb temperature.

## Dehumidification Processes

**Cooling Dehumidification:**
Covered above under cooling with dehumidification. Most common method in air conditioning systems.

**Chemical Dehumidification (Desiccant):**
Solid or liquid desiccants absorb moisture from air through chemical affinity. The process removes moisture while adding sensible heat (heat of adsorption).

- Dry-bulb temperature increases (due to heat of adsorption)
- Humidity ratio decreases
- Dew point temperature decreases
- Process line slopes upward and to the left

Heat of adsorption is approximately 1.2 to 1.3 times the latent heat of vaporization.

| Desiccant Type | Temperature Rise | Dehumidification Capacity | Regeneration Temp |
|----------------|------------------|---------------------------|-------------------|
| Silica gel | 15-25°F | Moderate | 250-350°F |
| Activated alumina | 20-30°F | Moderate | 350-450°F |
| Molecular sieve | 25-35°F | High | 400-600°F |
| Lithium chloride | 30-45°F | Very high | 200-300°F |

## Evaporative Cooling

Evaporative cooling uses water evaporation to cool air in an approximately adiabatic process. The air follows a line of constant wet-bulb temperature toward saturation.

**Direct Evaporative Cooling:**
Air passes through a wetted medium or spray chamber, directly contacting water.

- Dry-bulb temperature decreases
- Humidity ratio increases
- Wet-bulb temperature remains approximately constant
- Relative humidity increases significantly
- Process approaches saturation line

**Effectiveness:**

ε = (T_db1 - T_db2) / (T_db1 - T_wb1)

Typical effectiveness ranges:
- Simple wetted pad: 50-70%
- Rigid media (4-6 inches): 70-85%
- Rigid media (8-12 inches): 85-95%

**Indirect Evaporative Cooling:**
Air is cooled through a heat exchanger by secondary air that undergoes direct evaporative cooling. The primary airstream experiences sensible cooling without moisture addition.

- Dry-bulb temperature decreases
- Humidity ratio remains constant (horizontal line)
- No latent load added to space

## Adiabatic Mixing of Air Streams

Mixing two airstreams at different conditions produces a final condition that lies on a straight line connecting the two initial states on the psychrometric chart. The location on this line is determined by mass flow rate ratios.

**Mixing Equation for Any Property:**

x_mix = (ṁ_da1 × x_1 + ṁ_da2 × x_2) / (ṁ_da1 + ṁ_da2)

where x represents any property (T, ω, h, etc.)

**Mass Ratio Location:**

ṁ_da1 / ṁ_da2 = (x_2 - x_mix) / (x_mix - x_1)

This relationship shows that the mixed condition divides the line connecting states 1 and 2 inversely proportional to the mass flow rates. If equal mass flows mix, the result is the midpoint between the two conditions.

**Practical Applications:**
- Return air mixing with outdoor air
- Bypass air mixing with conditioned air
- Multiple zone discharge air mixing
- Economizer cycle mixing

**Mixed Air Temperature Example:**

For 1000 cfm outdoor air at 95°F and 3000 cfm return air at 75°F:

T_mix = (Q_oa × T_oa + Q_ra × T_ra) / (Q_oa + Q_ra)
T_mix = (1000 × 95 + 3000 × 75) / (1000 + 3000)
T_mix = 80°F

## Process Plotting on Psychrometric Chart

Accurate process plotting requires identifying the nature of the transformation and the appropriate path on the chart.

**Step-by-Step Plotting Procedure:**

1. **Locate Initial State:** Plot the entering air condition using two independent properties (typically dry-bulb temperature and relative humidity, or dry-bulb and wet-bulb)

2. **Identify Process Type:** Determine which process is occurring based on equipment and operating conditions

3. **Determine Process Direction:** Establish whether properties increase or decrease

4. **Plot Process Line:**
   - Sensible heating/cooling: horizontal line (constant ω)
   - Cooling with dehumidification: line toward ADP
   - Adiabatic humidification: line following constant wet-bulb
   - Steam humidification: line upward and to right
   - Mixing: straight line between two states

5. **Locate Final State:** Use energy balance or equipment performance data to determine exit condition

6. **Verify Results:** Check that calculated values are consistent with process physics

**Example Process Series - Typical Air Conditioning:**

1. **Point O:** Outdoor air at 95°F DB, 75°F WB
2. **Point R:** Return air at 75°F DB, 50% RH
3. **Point M:** Mixed air (O + R mixing)
4. **Point C:** Leaving cooling coil at 55°F DB, 90% RH (cooling + dehumidification from M to C)
5. **Point S:** Supply air after fan heat gain at 58°F DB (sensible heating from C to S)
6. **Point R:** Room condition after space loads applied (sensible + latent gains from S to R)

## Sensible Heat Ratio (SHR)

The sensible heat ratio defines the relationship between sensible and total cooling, determining the slope of the process line from supply air to room conditions.

**Definition:**

SHR = Q_sensible / Q_total = Q_sensible / (Q_sensible + Q_latent)

The SHR line on the psychrometric chart, drawn through the room condition at the calculated SHR, represents the path from supply air to room air as space loads are applied. The supply air condition must lie on this line.

| Application | Typical SHR | Latent Load Character |
|-------------|-------------|-----------------------|
| Office space | 0.85 - 0.95 | Low occupancy density |
| Retail store | 0.75 - 0.85 | Moderate occupancy |
| Restaurant | 0.65 - 0.75 | High occupancy, kitchen |
| Natatorium | 0.40 - 0.60 | High evaporation load |
| Ice rink | 0.30 - 0.45 | Very high dehumidification |

**Supply Air Calculation Using SHR:**

Q_sensible = ṁ_da × c_p × (T_room - T_supply)

Solving for required supply airflow:

ṁ_da = Q_sensible / [c_p × (T_room - T_supply)]

Once ṁ_da is known, the required supply humidity ratio is:

ω_supply = ω_room - Q_latent / (ṁ_da × h_fg)

## Chemical Reactions and Moisture Generation

Certain processes generate moisture through chemical reactions, requiring psychrometric analysis:

**Combustion Processes:**
Complete combustion of hydrocarbon fuels produces water vapor. For natural gas (primarily methane):

CH₄ + 2O₂ → CO₂ + 2H₂O

Each cubic foot of natural gas combusted produces approximately 2 cubic feet of water vapor, adding latent load to spaces with unvented combustion.

**Human Metabolism:**
Occupants generate both sensible and latent heat. The ratio shifts with activity level and ambient temperature. At higher activity levels and temperatures, latent heat generation dominates.

These processes must be accurately represented on the psychrometric chart to properly size dehumidification equipment and ensure adequate moisture control.
