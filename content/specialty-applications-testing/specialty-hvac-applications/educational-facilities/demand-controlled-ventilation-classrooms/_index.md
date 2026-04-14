---
title: "Demand Controlled Ventilation in Classrooms"
aliases: ["Demand Controlled Ventilation in Classrooms"]
description: "Technical analysis of CO2-based demand controlled ventilation for educational facilities including sensor placement, control algorithms, and energy savings quantification per ASHRAE 62.1 standards."
keywords:
  - demand controlled ventilation
  - DCV classrooms
  - CO2 sensors schools
  - classroom ventilation control
  - ASHRAE 62.1 schools
  - occupancy-based ventilation
  - classroom IAQ control
  - educational facility ventilation
  - CO2 control algorithms
  - ventilation energy savings
  - classroom air quality sensors
  - school HVAC efficiency
  - variable ventilation control
  - DCV energy calculations
  - classroom occupancy detection
weight: 10
seo_title: "Demand Controlled Ventilation for Classrooms - CO2 Control & Energy Savings"
seo_description: "Engineering analysis of classroom DCV systems with CO2-based algorithms, sensor placement strategies, control sequences, and quantified energy savings per ASHRAE 62.1."
---

Demand controlled ventilation provides dynamic adjustment of outdoor air delivery based on actual classroom occupancy, reducing energy consumption while maintaining ASHRAE 62.1 compliance. The system modulates ventilation rates using CO2 concentration as a proxy for occupancy, delivering substantial savings in heating, cooling, and fan energy compared to constant ventilation strategies.

## Physical Basis of CO2-Based Control

Carbon dioxide serves as an effective occupancy indicator due to the metabolic generation rate of approximately 0.31 L/min per person at sedentary activity levels typical of classroom environments. The steady-state CO2 concentration relationship follows:

**C_ss = C_oa + (N × G) / V_oa**

Where:
- C_ss = Steady-state indoor CO2 concentration (ppm)
- C_oa = Outdoor air CO2 concentration (typically 400-450 ppm)
- N = Number of occupants
- G = CO2 generation rate per person (0.0052 cfm or 0.31 L/min)
- V_oa = Outdoor airflow rate (cfm per person)

ASHRAE 62.1 requires 10 cfm per person for classrooms plus an area component of 0.12 cfm/ft². For a 900 ft² classroom with 30 occupants, the total outdoor air requirement equals 408 cfm. At this ventilation rate, steady-state CO2 concentration reaches approximately 1,100 ppm above outdoor levels, or 1,500-1,550 ppm absolute.

## CO2 Sensor Specifications and Placement

Effective DCV implementation requires properly specified and positioned sensors.

**Sensor Technical Requirements:**

| Parameter | Specification | Rationale |
|-----------|--------------|-----------|
| Measurement range | 0-2,000 ppm | Captures full operational range |
| Accuracy | ±50 ppm or ±3% of reading | Prevents control oscillation |
| Response time | <2 minutes (T90) | Tracks occupancy changes |
| Drift | <50 ppm over 5 years | Maintains long-term accuracy |
| Technology | NDIR (non-dispersive infrared) | Specific CO2 detection |
| Calibration | Automatic background calibration | Compensates for drift |

**Placement Strategy:**

1. Install sensors in the breathing zone (3-6 feet above floor)
2. Locate away from supply diffusers (minimum 6 feet separation)
3. Avoid direct exhaust or return air streams
4. Position central to occupied space
5. Keep clear of windows and doors to outdoor air
6. One sensor per thermal zone with independent ventilation control

Multiple sensors per large space improve accuracy through averaging but must account for spatial CO2 stratification patterns.

## Control Algorithms and Sequences

DCV control translates CO2 measurements into ventilation commands through proportional or two-position strategies.

**Proportional Control Algorithm:**

V_oa = V_min + (V_design - V_min) × [(C_measured - C_setpoint_low) / (C_setpoint_high - C_setpoint_low)]

Where:
- V_oa = Commanded outdoor airflow
- V_min = Minimum ventilation (typically area component only)
- V_design = Full design outdoor airflow
- C_setpoint_low = Lower CO2 threshold (typically 800-900 ppm)
- C_setpoint_high = Upper CO2 threshold (typically 1,200-1,400 ppm)

**Control Sequence Steps:**

1. **Initialization**: System starts at minimum ventilation (0.12 cfm/ft² area component)
2. **Monitoring**: Controller samples CO2 every 1-5 minutes
3. **Threshold Detection**: Compares measured value to setpoint range
4. **Proportional Response**: Modulates outdoor air damper position linearly between thresholds
5. **Maximum Override**: Forces full outdoor air if CO2 exceeds high limit
6. **Minimum Enforcement**: Maintains code-required area ventilation regardless of CO2 level

**Two-Position Control:**

Simpler systems use binary control:
- CO2 < 1,000 ppm: Outdoor air damper to minimum position (area component only)
- CO2 ≥ 1,000 ppm: Outdoor air damper to design position (full ventilation)

This approach reduces control complexity but increases cycling and reduces energy savings by 15-25% compared to proportional control.

## Energy Savings Quantification

DCV energy savings derive from three components: reduced heating, reduced cooling, and reduced fan power.

**Heating Energy Reduction:**

Q_heat = 1.08 × ΔV_oa × (T_indoor - T_outdoor) × H_occupied

Where:
- Q_heat = Annual heating energy saved (Btu)
- ΔV_oa = Average outdoor airflow reduction (cfm)
- T_indoor = Indoor setpoint (typically 70°F)
- T_outdoor = Average outdoor temperature during heating season
- H_occupied = Occupied hours during heating season
- 1.08 = Conversion factor (cfm × °F to Btu/hr)

**Example Calculation:**

For a 900 ft² classroom in Chicago climate:
- Design outdoor air: 408 cfm
- Average occupied outdoor air with DCV: 180 cfm (44% average occupancy)
- Outdoor air reduction: 228 cfm
- Average heating season outdoor temperature: 32°F
- Occupied heating hours: 1,200 hours/year

Q_heat = 1.08 × 228 × (70 - 32) × 1,200 = 11.3 MMBtu/year

At natural gas efficiency of 85% and $1.00/therm cost:
Heating savings = 11.3 MMBtu / 0.85 / 0.1 MMBtu/therm × $1.00 = $133/year

**Cooling Energy Reduction:**

Q_cool = 1.08 × ΔV_oa × (T_outdoor - T_indoor) × H_cooling + 4,840 × ΔV_oa × (W_outdoor - W_indoor) × H_cooling

The latent component (second term) dominates in humid climates:
- 4,840 = Latent heat conversion factor (cfm × lb_water/lb_air to Btu/hr)
- W = Humidity ratio (lb_water/lb_air)

For the same classroom in Chicago with 900 cooling hours:
- Sensible: 1.08 × 228 × (82 - 75) × 900 = 1.55 MMBtu
- Latent: 4,840 × 228 × (0.0110 - 0.0093) × 900 = 1.69 MMBtu
- Total cooling: 3.24 MMBtu

At chiller COP of 4.5 and $0.12/kWh:
Cooling savings = 3.24 MMBtu / 3.412 MBtu/MWh / 4.5 × $120/MWh = $24/year

**Fan Energy Reduction:**

P_fan = 0.1175 × ΔV_oa × ΔP × H_occupied / η_fan

Where:
- P_fan = Fan energy saved (kWh)
- ΔP = System static pressure (inches w.c.)
- η_fan = Fan total efficiency (typically 0.55-0.65)

For 3.5 inches w.c. system pressure and 2,100 occupied hours:
P_fan = 0.1175 × 228 × 3.5 / 0.60 × 2,100 = 104,300 kWh

This appears excessive due to constant fan operation assumptions. For VAV systems with proper fan control:
Actual fan savings ≈ 15-25% of calculated value = 350 kWh/year = $42/year at $0.12/kWh

**Total Annual Savings:**
$133 (heating) + $24 (cooling) + $42 (fan) = $199 per classroom

For a 40-classroom school: $7,960/year savings

## ASHRAE 62.1 Compliance Requirements

ASHRAE Standard 62.1 Section 6.2.7 permits DCV under specific conditions:

**Mandatory Requirements:**

1. **Minimum Ventilation**: System must deliver area component (0.12 cfm/ft² for classrooms) continuously during occupancy
2. **Sensor Accuracy**: CO2 sensors must maintain calibration per manufacturer specifications
3. **Setpoint Limits**: Indoor CO2 must not exceed 700 ppm above outdoor air concentration
4. **Documentation**: Design must demonstrate compliance through calculations or airflow measurements
5. **Multiple Spaces**: Each zone requires independent measurement if served by single air handler

**Design Documentation:**

The ventilation rate procedure requires:
- Zone outdoor airflow (V_oz) = R_p × P_z + R_a × A_z
- R_p = 10 cfm/person for classrooms
- R_a = 0.12 cfm/ft² for classrooms
- P_z = Design occupancy
- A_z = Zone floor area

DCV control must modulate between minimum (area component) and design (full R_p × P_z + R_a × A_z) based on measured CO2.

## Occupancy Detection Integration

Advanced DCV implementations combine CO2 sensing with direct occupancy detection for improved response and energy savings.

**Occupancy Sensor Technologies:**

| Technology | Detection Method | Response Time | Application |
|------------|------------------|---------------|-------------|
| Passive infrared (PIR) | Motion detection | <1 second | Rapid unoccupied detection |
| Ultrasonic | Motion detection | <1 second | Improved coverage |
| Camera-based | Visual counting | 1-5 seconds | Precise occupancy count |
| Door counters | Entry/exit tracking | <1 second | Cumulative tracking |

**Integrated Control Strategy:**

1. **Occupancy Trigger**: Sensor detects space occupied → ventilation to minimum level
2. **CO2 Modulation**: Once occupied, CO2 measurement determines ventilation rate
3. **Unoccupied Override**: When occupancy sensor shows unoccupied AND CO2 drops below threshold → ventilation off (or code minimum)
4. **Startup Purge**: Upon occupation after extended vacancy, operate at design airflow for 30-60 minutes to remove accumulated contaminants

This hybrid approach reduces initial ventilation lag compared to CO2-only control while maintaining proportional response to actual occupancy levels.

## System Performance Optimization

**Sensor Maintenance Schedule:**

- Monthly: Visual inspection and cleaning
- Quarterly: Verify reading against calibrated portable meter
- Annually: Full calibration or sensor replacement
- Five-year: Sensor replacement regardless of apparent performance

**Control Tuning Parameters:**

Adjust the following for optimal performance:
- **Dead band**: 100-200 ppm between heating/cooling modes prevents oscillation
- **Sampling interval**: 3-5 minutes balances responsiveness with stability
- **Damper response time**: 2-5 minutes prevents mechanical wear
- **Setpoint offset**: Set control target 100-150 ppm below ASHRAE limit to provide margin

**Common Performance Issues:**

1. **Sensor drift**: Causes ventilation under-delivery; prevented by automatic background calibration
2. **Poor sensor placement**: Creates non-representative readings; verify location during commissioning
3. **Excessive minimum ventilation**: Reduces savings; confirm area component calculation
4. **Inadequate outdoor air delivery**: Verify damper sizing and economizer integration

Properly implemented DCV systems in educational facilities achieve 30-50% reduction in ventilation energy while improving indoor air quality through better matching of ventilation to actual occupancy loads.
