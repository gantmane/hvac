---
title: "Demand Controlled Ventilation"
aliases: ["Demand Controlled Ventilation"]
weight: 5
---

Demand controlled ventilation (DCV) modulates outdoor air delivery based on actual occupancy or indoor air quality conditions rather than design occupancy. This strategy reduces energy consumption by eliminating unnecessary ventilation during periods of low or variable occupancy.

## Fundamental Principles

DCV operates on the premise that ventilation requirements are directly proportional to occupant density and metabolic activity. By continuously monitoring space conditions, the system adjusts outdoor air intake to maintain acceptable indoor air quality while minimizing conditioning energy.

**Primary control parameters:**
- CO2 concentration (occupancy indicator)
- Direct occupancy counts
- VOC levels
- Particulate matter concentration
- Time-based schedules

## CO2-Based Control

Carbon dioxide serves as a reliable surrogate for occupancy because humans exhale CO2 at predictable rates. The CO2 generation rate for sedentary adults averages 0.3 L/min (0.011 cfm) at standard metabolic rates.

### CO2 Concentration Relationships

The steady-state CO2 concentration follows:

**C_ss = C_oa + (N × G) / V_ot**

Where:
- C_ss = Steady-state indoor CO2 concentration (ppm)
- C_oa = Outdoor air CO2 concentration (typically 400-450 ppm)
- N = Number of occupants
- G = CO2 generation rate per person (L/s or cfm)
- V_ot = Total outdoor air ventilation rate (L/s or cfm)

### Outdoor Air CO2 Concentration

Baseline outdoor CO2 levels vary by location and have increased over time:

| Environment | Typical CO2 (ppm) |
|-------------|-------------------|
| Rural areas | 400-420 |
| Suburban areas | 420-450 |
| Urban areas | 450-500 |
| Near roadways | 500-600 |

Design calculations should use locally measured values or conservative estimates of 450 ppm for general applications.

### CO2 Setpoint Selection

ASHRAE 62.1 does not mandate specific CO2 setpoints but provides guidance based on ventilation rate per person. For typical applications:

**Target setpoint calculation:**
- At 15 cfm/person outdoor air rate: approximately 1000-1100 ppm
- At 10 cfm/person outdoor air rate: approximately 1400-1500 ppm
- At 20 cfm/person outdoor air rate: approximately 800-900 ppm

**Common setpoints by application:**

| Space Type | CO2 Setpoint (ppm) | Basis |
|------------|-------------------|-------|
| Office areas | 1000 | 17 cfm/person + 0.12 cfm/ft² |
| Classrooms | 1100 | High density, 15 cfm/person minimum |
| Conference rooms | 1000 | Variable occupancy |
| Retail | 850 | Lower density, public space |

### Indoor Generation Rate

CO2 generation depends on metabolic activity level:

| Activity Level | CO2 Generation Rate |
|----------------|---------------------|
| Sedentary (office work) | 0.31 L/min (0.011 cfm) |
| Light activity (shopping) | 0.48 L/min (0.017 cfm) |
| Moderate activity (warehouse) | 0.63 L/min (0.022 cfm) |
| Heavy activity (gymnasium) | 1.15 L/min (0.041 cfm) |

## ASHRAE 62.1 Ventilation Rates

ASHRAE 62.1 specifies ventilation rates using the Ventilation Rate Procedure, which combines people-based and area-based components.

### Breathing Zone Outdoor Airflow

**V_bz = R_p × P_z + R_a × A_z**

Where:
- V_bz = Breathing zone outdoor airflow (cfm)
- R_p = People outdoor air rate (cfm/person)
- P_z = Zone population (design or actual with DCV)
- R_a = Area outdoor air rate (cfm/ft²)
- A_z = Zone floor area (ft²)

### People Outdoor Air Rate

Standard rates from ASHRAE 62.1 Table 6.2.2.1:

| Occupancy Category | R_p (cfm/person) | R_a (cfm/ft²) |
|-------------------|------------------|---------------|
| Office space | 5 | 0.06 |
| Conference/meeting | 5 | 0.06 |
| Classrooms (ages 9+) | 10 | 0.12 |
| Lecture classroom | 7.5 | 0.06 |
| Retail sales | 7.5 | 0.12 |
| Lobbies/prefunction | 7.5 | 0.06 |

### Minimum Ventilation Rate

DCV systems must maintain minimum ventilation based on the area component:

**V_min = R_a × A_z**

This ensures baseline dilution of non-occupant-related contaminants including:
- Building material emissions
- Cleaning product residuals
- Furniture off-gassing
- Outdoor pollutant infiltration

## Occupancy Sensing Technologies

### Direct Occupancy Sensors

**Passive infrared (PIR) sensors:**
- Detect thermal motion
- Binary output (occupied/unoccupied)
- Limited accuracy for occupant counting
- Cost: $50-$150 per sensor

**Ultrasonic sensors:**
- Detect motion via Doppler shift
- Better coverage in obstructed spaces
- Cannot count occupants
- Cost: $75-$200 per sensor

**Computer vision systems:**
- Camera-based counting
- High accuracy (±5%)
- Privacy concerns require consideration
- Cost: $500-$2000 per camera

**WiFi/Bluetooth tracking:**
- Device-based occupancy estimation
- Building-wide integration potential
- Undercounts non-device users
- Cost: $200-$500 per access point

### CO2 Sensors

**Non-dispersive infrared (NDIR) sensors:**
- Industry standard for HVAC applications
- Accuracy: ±50 ppm typical
- Require periodic calibration
- Lifespan: 10-15 years
- Cost: $200-$600 per sensor

**Sensor placement requirements:**
- Mount at breathing zone height (3-6 ft above floor)
- Avoid locations near supply air diffusers
- Minimum 3 ft from exhaust grilles
- Representative of occupied zone
- Multiple sensors for large or irregular spaces

## Control Algorithms

### Proportional Control

The outdoor air damper position modulates proportionally to the difference between measured and setpoint CO2:

**OA_damper = OA_min + K_p × (CO2_measured - CO2_setpoint)**

Where:
- OA_damper = Outdoor air damper position (%)
- OA_min = Minimum damper position (%)
- K_p = Proportional gain
- CO2_measured = Current sensor reading (ppm)
- CO2_setpoint = Target concentration (ppm)

Typical gain values range from 0.05 to 0.20 %/ppm depending on system responsiveness requirements.

### Reset Logic

**Proportional-integral (PI) control:**
Adds integral term to eliminate steady-state offset:

**OA_damper = OA_min + K_p × e + K_i × ∫e dt**

Where:
- e = Error (CO2_measured - CO2_setpoint)
- K_i = Integral gain

**Setpoint reset:**
Adjusts CO2 setpoint based on outdoor air temperature or enthalpy to maximize free cooling opportunities when outdoor conditions are favorable.

### Response Time Considerations

CO2 concentration responds slowly to occupancy changes due to space volume and air change rates:

**Time constant (τ) = V_space / V_ot**

For a 10,000 ft³ space with 1000 cfm outdoor air:
τ = 10,000 / 1000 = 10 minutes

The space reaches 63% of final concentration change in one time constant, 95% in three time constants (30 minutes in this example).

## Energy Savings Potential

DCV energy savings derive from reduced outdoor air heating, cooling, dehumidification, and fan energy.

### Heating Energy Savings

**Q_heating = 1.08 × ΔV_oa × Δt × hours**

Where:
- Q_heating = Annual heating energy reduction (Btu)
- 1.08 = Constant (Btu/cfm·°F·hr)
- ΔV_oa = Reduction in outdoor air volume (cfm)
- Δt = Temperature difference indoor-outdoor (°F)
- hours = Annual operating hours with reduced airflow

### Cooling Energy Savings

**Q_cooling = 4.5 × ΔV_oa × Δh × hours / COP**

Where:
- Q_cooling = Annual cooling energy reduction (kWh)
- 4.5 = Constant (Btu/cfm·h/Btu/lb)
- Δh = Enthalpy difference indoor-outdoor (Btu/lb)
- COP = Chiller coefficient of performance

### Example Calculation

**Project parameters:**
- Space: 5000 ft² classroom
- Design occupancy: 125 people
- Average occupancy: 50 people (40% utilization)
- Operating hours: 2500 hours/year
- Climate: Mixed humid (heating and cooling)

**Ventilation rates:**
- R_p = 10 cfm/person
- R_a = 0.12 cfm/ft²
- Minimum OA = 0.12 × 5000 = 600 cfm
- Design OA = (10 × 125) + 600 = 1850 cfm
- Average DCV OA = (10 × 50) + 600 = 1100 cfm
- Airflow reduction = 1850 - 1100 = 750 cfm

**Annual heating savings:**
- Average Δt = 35°F
- Q_heating = 1.08 × 750 × 35 × 2500 = 70,875,000 Btu
- At $12/MMBtu natural gas, 80% efficiency: $1063/year

**Annual cooling savings:**
- Average Δh = 8 Btu/lb
- COP = 3.5
- Q_cooling = 4.5 × 750 × 8 × 2500 / 3.5 = 19,286 kWh
- At $0.12/kWh: $2314/year

**Total annual savings: $3377**

### Savings Factors

Energy savings magnitude depends on:

| Factor | High Savings | Low Savings |
|--------|-------------|-------------|
| Occupancy variability | >50% variation | <20% variation |
| Climate severity | Extreme heating/cooling | Mild year-round |
| Occupancy density | High (>7 people/1000 ft²) | Low (<3 people/1000 ft²) |
| Operating hours | >4000 hours/year | <2000 hours/year |
| Baseline ventilation | Fixed at design | Already modulated |

## VOC Sensors

Volatile organic compound sensors detect chemical contaminants not correlated with occupancy, including cleaning products, building materials, and outdoor pollutants.

**Metal oxide semiconductor (MOS) sensors:**
- Detect total VOCs
- Response to hydrogen-containing compounds
- Subject to drift and cross-sensitivity
- Require frequent calibration
- Cost: $150-$400

**Photoionization detectors (PID):**
- Measure specific VOC compounds
- Higher accuracy than MOS
- More expensive and complex
- Laboratory-grade applications
- Cost: $1000-$3000

## Particulate Sensors

Optical particle counters measure PM2.5 and PM10 concentrations to control filtration and outdoor air intake based on particulate pollution.

**Laser scattering sensors:**
- Real-time PM2.5 measurement
- Accuracy ±10 μg/m³
- Used for wildfire smoke response
- Cost: $200-$800

## Applications and Limitations

**Ideal applications:**
- Spaces with highly variable occupancy (conference rooms, auditoriums, classrooms)
- Dense occupancy with significant people-based ventilation component
- Climates with substantial heating or cooling loads
- Buildings with extended operating hours

**Limitations:**
- Not suitable for constant high-density occupancy
- Slow response to rapid occupancy changes
- Requires commissioning and ongoing calibration
- Ineffective when area component dominates ventilation requirement
- May not address all contaminant sources

## Integration with Building Systems

DCV integrates with:
- Building automation systems (BACnet, LonWorks protocols)
- Energy management platforms
- Fault detection and diagnostics systems
- Occupancy scheduling systems
- Indoor air quality dashboards

Proper integration enables advanced strategies including predictive ventilation based on scheduled events and multi-zone optimization balancing energy use with air quality across entire buildings.
