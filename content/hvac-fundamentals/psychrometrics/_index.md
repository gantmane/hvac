---
title: "Psychrometrics"
aliases: ["Psychrometrics"]
weight: 4
description: "Comprehensive guide to psychrometrics in HVAC systems, including moist air properties, psychrometric chart usage, humidity ratio calculations, and air conditioning process analysis."
---

Psychrometrics is the study of thermodynamic properties of moist air and the analysis of processes involving air-water vapor mixtures. This discipline forms the foundation for air conditioning system design, enabling engineers to quantify thermal and moisture conditions throughout HVAC processes.

## Fundamental Properties

Moist air consists of dry air and water vapor. The mixture behaves as an ideal gas under typical HVAC conditions (atmospheric pressure, temperatures from -10°C to 50°C). Seven independent properties characterize the state of moist air:

**Dry-bulb temperature (Tdb)** is the temperature measured by a standard thermometer, representing the sensible heat content of air. This is the primary temperature reference in psychrometric analysis.

**Wet-bulb temperature (Twb)** is the temperature indicated by a thermometer with its bulb covered by a water-saturated wick exposed to moving air. The wet-bulb temperature accounts for both sensible and latent heat effects through evaporative cooling. At saturation (100% RH), dry-bulb and wet-bulb temperatures are equal.

**Dew point temperature (Tdp)** is the temperature at which water vapor begins to condense when air is cooled at constant pressure and humidity ratio. The dew point provides a direct indicator of moisture content—higher dew points correspond to higher absolute humidity.

**Humidity ratio (W)**, also called specific humidity or mixing ratio, represents the mass of water vapor per unit mass of dry air:

W = mw / ma (lb water vapor / lb dry air or kg/kg)

This property is critical for mass balance calculations in HVAC processes.

**Relative humidity (φ or RH)** is the ratio of actual water vapor pressure to saturation vapor pressure at the same dry-bulb temperature:

φ = pw / pws × 100%

Relative humidity indicates how close the air is to saturation but does not directly indicate absolute moisture content.

**Enthalpy (h)** represents the total heat content of moist air per unit mass of dry air:

h = cpa·Tdb + W(hfg + cpw·Tdb)

where cpa = specific heat of dry air (≈ 0.24 Btu/lb·°F or 1.006 kJ/kg·K), hfg = latent heat of vaporization at 0°F or 0°C (≈ 1061 Btu/lb or 2501 kJ/kg), and cpw = specific heat of water vapor (≈ 0.444 Btu/lb·°F or 1.86 kJ/kg·K). Enthalpy is essential for energy balance calculations.

**Specific volume (v)** is the volume of moist air per unit mass of dry air, required for air flow rate calculations and duct sizing.

## Psychrometric Chart

The psychrometric chart graphically represents these properties, enabling rapid determination of air states and process visualization. ASHRAE publishes standard charts for sea level and various elevations, as barometric pressure significantly affects moist air properties.

Chart construction places dry-bulb temperature on the horizontal axis and humidity ratio on the vertical axis. Constant relative humidity curves arc upward from left to right, with the saturation curve (100% RH) forming the upper boundary. Wet-bulb temperature lines slope downward from upper left to lower right, while enthalpy lines run nearly parallel to wet-bulb lines. Specific volume lines slope upward from lower left to upper right.

Two independent properties define a unique point on the chart, from which all other properties can be determined. For example, knowing dry-bulb temperature and relative humidity allows reading humidity ratio, enthalpy, wet-bulb temperature, dew point, and specific volume directly from the chart.

## Key Calculations

**Humidity ratio** from partial pressures:

W = 0.622 × pw / (p - pw)

where p = total barometric pressure and pw = partial pressure of water vapor.

**Sensible heat ratio (SHR)** quantifies the proportion of sensible to total heat:

SHR = qs / qtotal = qs / (qs + ql)

where qs = sensible heat and ql = latent heat. SHR determines the slope of process lines on the psychrometric chart during simultaneous heating/cooling and humidification/dehumidification.

**Degree of saturation (μ)** relates humidity ratio to saturation humidity ratio at the same temperature:

μ = W / Ws

This differs from relative humidity but provides useful information about the air's moisture-holding capacity utilization.

## Psychrometric Processes

**Sensible heating** increases dry-bulb temperature while maintaining constant humidity ratio, moving horizontally to the right on the chart. Heating coils, furnaces, and electric resistance heaters perform this process. Enthalpy increases proportionally to temperature rise.

**Sensible cooling** reduces dry-bulb temperature at constant humidity ratio, moving horizontally to the left. This occurs when cooling coil surface temperature exceeds the air dew point, preventing condensation.

**Cooling and dehumidification** occurs when air contacts surfaces below its dew point temperature, as in typical air conditioning cooling coils. The process line slopes downward and left, reducing both temperature and humidity ratio. The actual process follows a straight line from the initial state toward the apparatus dew point (ADP), which represents the effective surface temperature of the coil.

**Humidification** adds moisture to air, increasing humidity ratio. Steam injection provides nearly pure humidification (vertical line upward), as high-pressure steam adds minimal sensible heat. Evaporative humidification follows the wet-bulb line, with decreasing dry-bulb temperature as water evaporates (adiabatic saturation process).

**Dehumidification** without cooling typically requires chemical desiccants or refrigerant-based systems with reheat. The process removes moisture while adding sensible heat.

**Mixing processes** combine two airstreams, with the resulting state lying on a straight line connecting the two initial states. The mixture point divides this line in inverse proportion to the mass flow rates. Mixing calculations are fundamental to analyzing outdoor air and return air combination in air handling units.

## Air Conditioning System Design Applications

Psychrometric analysis enables precise calculation of:

- **Cooling coil loads**: Determining required cooling capacity from inlet and outlet conditions and airflow rate
- **Required airflow rates**: Calculating supply air quantity from space load and supply-to-room temperature difference
- **Outdoor air ventilation effects**: Quantifying the load imposed by introducing outdoor air
- **Reheat requirements**: Sizing reheat coils to achieve desired supply air conditions after dehumidification
- **Economizer operation**: Identifying conditions when outdoor air provides free cooling
- **Energy recovery effectiveness**: Evaluating sensible and latent heat transfer in air-to-air heat exchangers

## Comfort Zone and ASHRAE Standard 55

ASHRAE Standard 55 defines thermal comfort conditions based on extensive research correlating environmental parameters with human comfort perception. The comfort zone on the psychrometric chart typically encompasses:

- Operative temperature: 68-76°F (20-24°C) winter, 73-79°F (23-26°C) summer
- Humidity: 30-60% relative humidity recommended
- Dew point: Below 62°F (17°C) for thermal comfort; above 55°F (13°C) to prevent excessive dryness

The standard accounts for clothing insulation (clo), metabolic rate (met), air velocity, mean radiant temperature, and humidity. Understanding psychrometric relationships allows designers to specify conditions that satisfy comfort requirements while optimizing energy consumption.

ASHRAE Fundamentals Handbook provides detailed psychrometric equations, tabular data, and charts at various elevations. Engineers should consult Chapter 1 (Psychrometrics) for precise calculation methods, especially when conditions fall outside chart boundaries or when computer-based calculations are required for iterative design processes.

Proficiency with psychrometric analysis distinguishes competent HVAC engineers, enabling rapid problem-solving, accurate system sizing, and effective troubleshooting of air conditioning systems. The psychrometric chart remains an indispensable tool despite advances in computational methods, providing immediate visualization of air conditioning processes and system performance.
