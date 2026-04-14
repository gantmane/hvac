---
title: "Design Conditions"
aliases: ["Design Conditions"]
description: "Selection of outdoor and indoor design conditions for HVAC cooling load calculations including weather data, temperature, humidity, and solar radiation."
keywords: ["design conditions", "outdoor design temperature", "indoor conditions", "weather data", "ASHRAE climatic data", "cooling design"]
tags: ["design conditions", "outdoor design temperature", "indoor conditions", "weather data", "ASHRAE climatic data", "cooling design"]
weight: 1
---

Design conditions establish the basis for HVAC system sizing, representing the outdoor environmental extremes and indoor requirements that define peak cooling loads. Proper selection ensures systems meet occupant comfort needs while avoiding excessive oversizing.

## Outdoor Design Conditions

### ASHRAE Climatic Design Data

ASHRAE publishes comprehensive climatic data for thousands of worldwide locations, updated periodically in the Fundamentals Handbook and online ASHRAE Weather Data Viewer.

**Key Design Values**:

| Parameter | Description | Typical Use |
|-----------|-------------|-------------|
| 0.4% DB/MCWB | Dry-bulb exceeded 35 hours/year with mean coincident wet-bulb | Critical applications |
| 1% DB/MCWB | Dry-bulb exceeded 88 hours/year | Standard commercial design |
| 2% DB/MCWB | Dry-bulb exceeded 175 hours/year | Residential, non-critical |

### Dry-Bulb Temperature Selection

The design dry-bulb temperature directly impacts sensible cooling load calculations:

$$Q_{sensible} = 1.1 \times CFM \times (T_{outdoor} - T_{supply})$$

**Selection Guidelines**:
- **Critical facilities** (hospitals, data centers): 0.4% values
- **Commercial buildings**: 1% values
- **Residential**: 1-2% values
- **Industrial**: Application-dependent

### Wet-Bulb Temperature and Humidity

Wet-bulb or dew-point conditions determine latent cooling requirements:

$$Q_{latent} = 0.68 \times CFM \times (W_{outdoor} - W_{supply})$$

**Mean Coincident Values**: Use MCWB coinciding with design dry-bulb rather than peak wet-bulb, as extreme temperature and humidity rarely occur simultaneously.

### Solar Radiation Data

Solar heat gain calculations require:

- **Direct normal irradiance**: Beam radiation on perpendicular surface
- **Diffuse horizontal**: Scattered sky radiation
- **Global horizontal**: Total radiation on horizontal surface

ASHRAE clear-sky model or TMY (Typical Meteorological Year) data provide design solar values.

## Indoor Design Conditions

### Thermal Comfort Parameters

ASHRAE Standard 55 defines acceptable thermal environmental conditions:

**Summer Cooling Design**:
| Parameter | Typical Range | Notes |
|-----------|---------------|-------|
| Temperature | 74-78°F (23-26°C) | Higher setpoints reduce energy |
| Relative Humidity | 40-60% | Maximum 65% for comfort |
| Air Movement | 20-50 fpm | Higher velocity allows higher temperature |
| Clothing | 0.5 clo (summer) | Light office attire |
| Activity | 1.0-1.2 met | Seated office work |

### Space-Specific Requirements

Different space types require specific conditions:

**Offices and Commercial**:
- 75°F DB, 50% RH typical
- Uniform conditions expected

**Retail and Public Spaces**:
- 75-78°F acceptable
- Higher transient occupancy tolerates wider range

**Healthcare**:
- ASHRAE 170 mandates specific requirements
- Operating rooms: 66-68°F, 30-60% RH
- Patient rooms: 70-75°F

**Data Centers**:
- ASHRAE TC 9.9 guidelines
- Recommended: 64.4-80.6°F supply
- Allowable: 59-90°F (A1 class)

### Humidity Considerations

Design relative humidity affects:

$$h_{indoor} = f(T_{db}, RH)$$

- **Comfort**: 40-60% RH preferred
- **Health**: <65% RH reduces mold growth
- **Static electricity**: >30% RH prevents discharge
- **Energy**: Lower RH reduces latent load but may require reheat

## Temperature Differential (ΔT)

### Outdoor-Indoor Differential

The design temperature differential determines peak load:

$$\Delta T_{design} = T_{outdoor,design} - T_{indoor,setpoint}$$

**Example**:
- Outdoor: 95°F (1% design)
- Indoor: 75°F setpoint
- ΔT = 20°F

### Coil Temperature Differential

Supply air temperature affects airflow requirements:

$$\Delta T_{coil} = T_{return} - T_{supply}$$

**Typical Values**:
- Conventional VAV: 18-22°F
- High-efficiency: 15-18°F
- Chilled beams: 10-14°F

Lower coil ΔT requires higher airflow but provides better humidity control.

## Altitude and Pressure Corrections

### Density Correction

Standard calculations assume sea-level air density. At elevation:

$$\rho_{altitude} = \rho_{SL} \times \frac{P_{altitude}}{P_{SL}}$$

**Approximate Correction**:
$$CF = 1 - 0.0000036 \times altitude(ft)$$

### Impact on System Sizing

At 5,000 ft elevation:
- Air density approximately 17% lower
- Fan airflow must increase for same mass flow
- Cooling capacity may derate

## Coincident Design Conditions

### Peak Load Timing

Different load components peak at different times:

**Solar Loads**: Vary hourly and seasonally
- East exposure: Morning peak
- West exposure: Afternoon peak
- Roof: Midday peak

**Transmission Loads**: Follow temperature profile
- Typically peak mid-afternoon
- Thermal mass causes time delay

**Internal Loads**: Follow occupancy
- May peak before outdoor maximum
- Diversity reduces simultaneous peak

### Block Load vs. Peak Load

**Block Load**: Simultaneous sum of all zones
$$Q_{block} = \sum_{zones} Q_{zone}(t_{peak,block})$$

**Peak Load Sum**: Sum of individual zone peaks
$$Q_{peak,sum} = \sum_{zones} Q_{zone,peak}$$

Block load is always less than or equal to peak sum due to non-coincident peaks.

## Climate Change Considerations

### Shifting Design Conditions

Historical weather data may not represent future conditions:

- **Temperature trends**: Warming observed in most locations
- **Extreme events**: Increasing frequency and intensity
- **Humidity patterns**: Varying by region

### Design Approach Options

1. **Future weather files**: Use projected TMY data
2. **Safety factors**: Add margin to historical design
3. **Adaptive design**: Plan for future equipment additions
4. **Resilience planning**: Consider extended operation beyond design

## Documentation Requirements

### Design Basis Documentation

Record design condition selections:

- Design condition values and source
- Percentile/frequency basis for outdoor conditions
- Indoor temperature and humidity setpoints
- Justification for any deviations from standard practice

### Code Compliance

Energy codes may specify:

- Maximum indoor design temperature (ASHRAE 90.1)
- Humidity control requirements
- Equipment sizing limitations

Proper selection and documentation of design conditions establishes the foundation for accurate cooling load calculations and appropriate HVAC system sizing.
