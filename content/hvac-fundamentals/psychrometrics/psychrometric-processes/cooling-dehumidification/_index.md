---
title: "Cooling and Dehumidification"
description: "Comprehensive analysis of simultaneous cooling and moisture removal processes in HVAC systems, including wet cooling coil performance, sensible heat ratio calculations, apparatus dew point theory, and practical design considerations"
weight: 3
---

## Overview

Cooling and dehumidification represents the most common psychrometric process in air conditioning systems, occurring when moist air passes over a cooling coil with a surface temperature below the air's dew point. This process simultaneously reduces both dry-bulb temperature (sensible cooling) and humidity ratio (latent cooling through condensation).

The process follows a curved path on the psychrometric chart, not a straight line, because the proportions of sensible and latent cooling vary continuously as air progresses through the coil. Understanding this process is fundamental to proper cooling coil selection, system design, and performance prediction.

## Physical Process Description

### Mechanism of Simultaneous Cooling and Dehumidification

When air contacts a cooling coil surface below its dew point temperature:

1. **Initial contact**: Air near the coil surface cools to saturation
2. **Condensation begins**: Water vapor condenses on the cold surface
3. **Mass transfer**: Moisture migrates from the airstream to the wetted coil surface
4. **Heat transfer**: Both sensible heat (temperature reduction) and latent heat (condensation) transfer to the cooling medium
5. **Progressive process**: As air moves through the coil, temperature and humidity ratio continuously decrease

The process line curves toward the saturation curve because:
- Early coil sections remove proportionally more sensible heat
- Later sections, with colder surfaces, remove proportionally more latent heat
- The local sensible heat ratio varies along the coil length

### Energy Balance

Total cooling consists of two components:

**Sensible Cooling (q_s)**:
- Temperature reduction from entering to leaving conditions
- Heat transferred: q_s = ṁ_da × c_p × (t_1 - t_2)
- Where ṁ_da = dry air mass flow rate, c_p = specific heat of air

**Latent Cooling (q_l)**:
- Moisture removal from air
- Heat transferred: q_l = ṁ_da × h_fg × (W_1 - W_2)
- Where h_fg = latent heat of vaporization, W = humidity ratio

**Total Cooling**:
q_t = q_s + q_l = ṁ_da × (h_1 - h_2)

Where h is specific enthalpy, directly readable from psychrometric charts.

## Sensible Heat Ratio (SHR)

### Definition and Significance

The Sensible Heat Ratio quantifies the proportion of total cooling devoted to temperature reduction versus moisture removal:

**SHR = q_s / q_t = (h_1 - h_2) / (h_1 - h_2) at constant W / (h_1 - h_2) total**

Alternatively:
**SHR = (t_1 - t_2) × c_p / (h_1 - h_2)**

**Typical SHR Values by Application**:

| Application Type | Typical SHR | Characteristics |
|------------------|-------------|-----------------|
| Auditoriums, theaters | 0.65 - 0.75 | High occupant density, high latent load |
| Office buildings | 0.75 - 0.85 | Moderate occupancy, standard ventilation |
| Retail spaces | 0.70 - 0.80 | Variable occupancy, door infiltration |
| Hospitals, operating rooms | 0.80 - 0.90 | Low occupancy density, high ventilation rates |
| Computer rooms, data centers | 0.90 - 1.00 | Equipment loads, minimal moisture generation |
| Natatoriums | 0.40 - 0.60 | Very high moisture loads from pool evaporation |
| Kitchens | 0.60 - 0.75 | High latent loads from cooking processes |
| Laboratories | 0.75 - 0.90 | High ventilation rates, equipment loads |

### Process Line Construction Using SHR

On a psychrometric chart, the cooling and dehumidification process line can be approximated by:

1. Plot entering air condition (point 1)
2. Determine SHR from load calculations
3. Draw a line from point 1 through the SHR protractor at the calculated SHR value
4. Extend this line toward saturation curve
5. The intersection approximates the apparatus dew point (ADP)
6. Actual leaving condition (point 2) lies on this line between point 1 and ADP

**Note**: The actual process follows a curved path, but the straight-line approximation is sufficiently accurate for most design purposes.

## Grand Sensible Heat Ratio (GSHF)

### Definition and Application

The Grand Sensible Heat Ratio includes both space loads and outdoor air loads in a single ratio:

**GSHF = (Space Sensible Load + OA Sensible Load) / (Space Total Load + OA Total Load)**

Where:
- OA = Outdoor air ventilation
- Space loads = Room loads only
- OA loads = Enthalpy difference between outdoor and space conditions

### Significance in System Design

GSHF determines the required apparatus dew point for the entire air handling system, accounting for:
- Return air from conditioned space
- Outdoor ventilation air (typically at different conditions)
- Mixed air conditions entering the cooling coil

**Procedure**:
1. Calculate space sensible and latent loads
2. Calculate outdoor air sensible and latent loads
3. Determine GSHF
4. Plot mixed air condition on psychrometric chart
5. Draw process line from mixed air through GSHF protractor
6. Determine required ADP and supply air conditions

## Apparatus Dew Point (ADP)

### Theoretical Basis

The apparatus dew point represents the theoretical surface temperature at which all air passing through the coil would be saturated if perfect contact occurred. In reality:

- Actual coil surfaces have varying temperatures
- Air contact with surfaces is imperfect
- Not all air reaches saturation

ADP is a **hypothetical construct** that simplifies complex heat and mass transfer into a single reference point.

### ADP and Coil Performance

**Definition**:
The ADP lies on the saturation curve where the process line (extended from entering conditions through the SHR point) intersects it.

**Mathematical relationship**:
For a straight-line approximation, the leaving air condition satisfies:

**(h_1 - h_2) / (h_1 - h_ADP) = Bypass Factor (BF)**

Where:
- h_1 = Entering air enthalpy
- h_2 = Leaving air enthalpy
- h_ADP = Enthalpy at apparatus dew point (on saturation curve)

### Bypass Factor and Contact Factor

**Bypass Factor (BF)**:
The fraction of air that "bypasses" the coil without being cooled to the ADP.

**BF = (t_2 - t_ADP) / (t_1 - t_ADP)**

Or using humidity ratios:
**BF = (W_2 - W_ADP) / (W_1 - W_ADP)**

**Contact Factor (CF)**:
The fraction of air effectively treated to ADP conditions.

**CF = 1 - BF**

**Typical Bypass Factors**:

| Coil Configuration | Rows Deep | Fins/inch | Typical BF | Contact Factor |
|--------------------|-----------|-----------|------------|----------------|
| Low performance | 3-4 | 8-10 | 0.30 - 0.50 | 0.50 - 0.70 |
| Standard performance | 4-6 | 10-12 | 0.15 - 0.30 | 0.70 - 0.85 |
| High performance | 6-8 | 12-14 | 0.05 - 0.15 | 0.85 - 0.95 |
| Ultra-high performance | 8-12 | 14-16 | 0.02 - 0.05 | 0.95 - 0.98 |

Lower bypass factors indicate better dehumidification performance but higher pressure drop and cost.

## Effective Surface Temperature

### Definition

The effective surface temperature (t_s) represents a weighted-mean temperature of the wetted coil surface that produces the observed cooling and dehumidification effect.

Unlike ADP (which lies on the saturation curve), the effective surface temperature accounts for:
- Non-uniform surface temperatures across coil depth
- Partial wetting of surfaces
- Temperature gradients through fin surfaces

### Relationship to Performance

For wet cooling coils, the effective surface temperature can be approximated by:

**t_s ≈ t_ADP + correction factor**

The correction depends on:
- Coil circuitry (direct expansion vs. chilled water)
- Face velocity
- Fin spacing and efficiency
- Refrigerant or water temperature profile

In practical terms, effective surface temperature is used in detailed coil simulation programs that solve simultaneous heat and mass transfer equations row-by-row through the coil.

## Mean Surface Temperature

### Distinction from ADP and Effective Temperature

Mean surface temperature represents the arithmetic or area-weighted average temperature of all coil surfaces (tubes and fins):

**t_mean = (Σ A_i × t_i) / Σ A_i**

Where:
- A_i = Surface area of element i
- t_i = Temperature of element i

### Practical Application

Mean surface temperature is relevant for:
- Condensate formation rate estimation
- Coil frosting prediction
- Corrosion assessment on wetted surfaces

For chilled water coils:
**t_mean ≈ (t_water,in + t_water,out) / 2 + tube wall resistance effect**

For DX coils, temperature varies more significantly due to refrigerant phase change and superheat region.

## Wet Cooling Coil Calculations

### Enthalpy-Based Method

This method provides the most direct calculation approach using psychrometric chart or properties:

**Step 1**: Determine entering air conditions (t_1, W_1, h_1)

**Step 2**: Calculate total cooling load:
q_total = ṁ_da × (h_1 - h_2)

**Step 3**: Determine sensible cooling load:
q_sensible = ṁ_da × c_p × (t_1 - t_2)

**Step 4**: Calculate latent cooling load:
q_latent = q_total - q_sensible = ṁ_da × h_fg × (W_1 - W_2)

**Step 5**: Find SHR:
SHR = q_sensible / q_total

**Step 6**: Determine apparatus dew point by extending line from point 1 through SHR point to saturation curve

**Step 7**: Calculate bypass factor (if coil is selected):
BF = (h_2 - h_ADP) / (h_1 - h_ADP)

### Condensate Removal Rate

The mass of water condensed from the airstream equals the change in moisture content:

**ṁ_condensate = ṁ_da × (W_1 - W_2)**

In practical units:
- **ṁ_condensate [lb/hr] = CFM × 4.5 × ρ_air × (W_1 - W_2)**
- Where CFM = airflow rate, ρ_air ≈ 0.075 lb/ft³ at standard conditions
- W in lb_water/lb_dry air

**Simplified**:
**ṁ_condensate [lb/hr] ≈ CFM × 0.34 × (W_1 - W_2)**

**In SI units**:
**ṁ_condensate [kg/s] = ṁ_da [kg/s] × (W_1 - W_2)**

### Example Calculation

**Given**:
- Airflow: 10,000 CFM
- Entering conditions: 80°F DB, 67°F WB (h_1 = 31.4 Btu/lb, W_1 = 0.0112 lb/lb)
- Leaving conditions: 55°F DB, 54°F WB (h_2 = 22.1 Btu/lb, W_2 = 0.0084 lb/lb)

**Solution**:

Dry air mass flow rate:
ṁ_da = 10,000 CFM × 60 min/hr × 0.075 lb/ft³ / (1 + 0.0112) = 44,505 lb/hr

Total cooling:
q_t = 44,505 × (31.4 - 22.1) = 413,900 Btu/hr = 34.5 tons

Sensible cooling:
q_s = 44,505 × 0.24 × (80 - 55) = 266,880 Btu/hr

Latent cooling:
q_l = 413,900 - 266,880 = 147,020 Btu/hr

SHR = 266,880 / 413,900 = 0.645

Condensate:
ṁ_condensate = 44,505 × (0.0112 - 0.0084) = 124.6 lb/hr = 14.96 gal/hr

## Coil Selection Considerations

### Required Parameters

For proper wet cooling coil selection, specify:

1. **Air-side conditions**:
   - Entering DB and WB (or RH)
   - Leaving DB and WB (or RH, or ADP and BF)
   - Airflow rate (CFM or m³/s)

2. **Cooling medium**:
   - Chilled water: entering/leaving temperatures, flow rate
   - DX refrigerant: saturated suction temperature, superheat

3. **Physical constraints**:
   - Maximum face velocity (typically 300-600 fpm)
   - Allowable pressure drop (typically 0.3-0.8 in. w.g.)
   - Available face area dimensions

4. **Performance requirements**:
   - Total capacity
   - Sensible capacity
   - SHR or required dehumidification

### Face Velocity Effects

Face velocity significantly impacts coil performance:

| Face Velocity (fpm) | Typical Application | Pressure Drop | Dehumidification | Carryover Risk |
|---------------------|---------------------|---------------|------------------|----------------|
| 200 - 300 | Critical dehumidification | Low | Excellent | Minimal |
| 300 - 450 | Standard comfort cooling | Moderate | Good | Low |
| 450 - 550 | High-capacity systems | Higher | Fair | Moderate |
| 550 - 650 | Maximum capacity | High | Reduced | Significant |
| > 650 | Avoid (moisture carryover) | Very high | Poor | Severe |

**Note**: At face velocities above 550 fpm, moisture entrainment becomes significant, requiring drain pans or eliminators downstream.

### Rows and Fins Selection

**Coil depth (rows)**:
- More rows = lower ADP, better dehumidification, higher cost
- Typical range: 3-8 rows for chilled water, 2-6 rows for DX

**Fin spacing**:
- More fins/inch = greater surface area, better heat transfer, higher pressure drop
- Typical range: 8-14 fins/inch
- Closer spacing (>12 fpi) increases fouling susceptibility

**Trade-offs**:
- 4-row, 10 fpi coil: General purpose, balanced performance
- 6-row, 12 fpi coil: High dehumidification, high humidity climates
- 3-row, 8 fpi coil: Low first cost, sensible cooling dominant

## Design Considerations

### Supply Air Temperature Selection

The required supply air temperature depends on:

1. **Sensible cooling requirement**:
   - Lower supply temperature = reduced airflow for same sensible capacity
   - Typical range: 52-58°F for comfort cooling

2. **Dehumidification requirement**:
   - Lower supply temperature and humidity = better moisture control
   - May require reheat if supply air too cold for sensible load

3. **Distribution system**:
   - Lower temperature allows smaller ductwork
   - Risk of condensation on cold ducts if vapor barriers inadequate

4. **Comfort and air quality**:
   - Very cold supply (< 50°F) may cause drafts and discomfort
   - Excessively cold surfaces risk condensation and mold

**Guideline**: Select the highest supply temperature that satisfies both sensible and latent loads to minimize energy consumption and reheat requirements.

### Apparatus Dew Point Selection

ADP must be low enough to achieve required leaving humidity while accounting for bypass factor:

**Required ADP** ≤ **Desired leaving DB** - **(Entering DB - Desired leaving DB) × BF**

Lower ADP requires:
- Colder chilled water or lower refrigerant temperature
- Deeper coils (more rows)
- Lower face velocity
- Higher energy consumption

**Design principle**: Select ADP 2-5°F below desired leaving dry-bulb temperature for adequate dehumidification with standard coils (BF ≈ 0.1-0.2).

### Reheat Considerations

Reheat becomes necessary when:
- Latent load is high relative to sensible load (low space SHR)
- Supply air cooled below temperature needed for sensible load
- Simultaneous temperature and humidity control required

**Reheat strategies**:
1. **Terminal reheat**: Individual zone control, highest energy use
2. **Hot gas reheat (DX systems)**: Energy recovery from compressor
3. **Heat recovery from other sources**: Condensers, exhaust air
4. **Desiccant systems**: Alternative to mechanical cooling for extreme latent loads

**Energy code compliance**: ASHRAE 90.1 and local energy codes restrict reheat. Verify compliance when using reheat strategies.

### Part-Load Performance

Wet cooling coil performance changes at part-load:

**Reduced airflow**:
- Lower face velocity increases contact time
- Bypass factor decreases (more effective cooling)
- Supply air temperature drops
- May improve dehumidification

**Reduced cooling capacity**:
- Chilled water or refrigerant temperature may rise
- ADP increases
- Bypass factor may increase
- Dehumidification performance degrades

**Critical**: At very low loads, coil surface temperature may rise above entering air dew point, eliminating dehumidification entirely. This is common in oversized systems cycling on/off frequently.

## ASHRAE and Code References

### ASHRAE Handbook References

**ASHRAE Fundamentals (2021)**:
- Chapter 1: Psychrometrics - fundamental properties and processes
- Chapter 6: Mass Transfer - condensation on coil surfaces
- Chapter 23: Thermal and Water Vapor Transmission Data

**ASHRAE HVAC Systems and Equipment (2020)**:
- Chapter 23: Air-Cooling and Dehumidifying Coils - detailed coil selection and rating
- Chapter 2: Decentralized Cooling and Heating - unitary equipment

**ASHRAE Applications (2019)**:
- Application-specific requirements for various building types
- Humidity control strategies

### Standards

**ASHRAE Standard 62.1**: Ventilation for Acceptable Indoor Air Quality
- Outdoor air requirements affect mixed air conditions and GSHF

**ASHRAE Standard 90.1**: Energy Standard for Buildings
- Minimum efficiency requirements for cooling equipment
- Restrictions on simultaneous heating and cooling (reheat)

**ASHRAE Standard 55**: Thermal Environmental Conditions for Human Occupancy
- Acceptable temperature and humidity ranges
- Influences supply conditions and load calculations

**ARI Standard 410**: Forced-Circulation Air-Cooling and Air-Heating Coils
- Standardized rating conditions and test procedures
- Published coil performance data format

### Psychrometric Chart Usage

All cooling and dehumidification calculations reference psychrometric charts at the applicable altitude:

- **Sea level**: Standard barometric pressure 29.92 in. Hg
- **High altitude**: Corrected charts or calculation programs required
- Every 1000 ft elevation reduces barometric pressure ~3.5%

Altitude affects:
- Humidity ratio at saturation (dewpoint temperature relationship)
- Enthalpy values
- Required cooling capacity

## Best Practices

### System Design

1. **Accurate load calculations**: Use ASHRAE load calculation methods (RTS, CLTD/CLF) to determine sensible and latent loads separately

2. **Conservative coil selection**: Select coils with 10-15% margin to account for:
   - Fouling over time
   - Slight load underestimation
   - Off-design conditions

3. **Adequate condensate drainage**: Provide properly sized and trapped drain lines to prevent water accumulation and microbial growth

4. **Coil access**: Ensure maintenance access for cleaning and inspection

5. **Filtration upstream**: Install appropriate filters to minimize coil fouling and maintain performance

### Control Strategies

1. **Maintain dewpoint control**: Monitor leaving air dewpoint or humidity ratio, not just dry-bulb temperature

2. **Avoid short cycling**: Minimum run times ensure adequate dehumidification

3. **Staged or modulating capacity**: Variable capacity systems maintain better humidity control than single-stage on/off

4. **Dewpoint reset**: In variable air volume (VAV) systems, reset supply air dewpoint based on zone with highest latent load

### Moisture Control

1. **Prevent coil blow-off**: Keep face velocity below 550 fpm or install eliminators

2. **Drain pan design**: Slope pans minimum 1/8 in. per foot toward drain, provide adequate depth

3. **Trap drainage properly**: Install traps with seal depth exceeding maximum negative pressure in drain pan area

4. **UV lights or treatments**: Consider for coil and drain pan microbial control in high-humidity applications

5. **Insulation**: Insulate all surfaces below dewpoint temperature to prevent condensation

### Troubleshooting High Humidity

If conditioned space humidity exceeds design conditions:

1. **Check entering conditions**: Verify actual outdoor air quantity and conditions

2. **Verify coil performance**:
   - Measure entering and leaving DB/WB
   - Calculate actual SHR and compare to design
   - Check for fouling, reduced airflow, or inadequate cooling capacity

3. **Assess infiltration**: Uncontrolled outdoor air infiltration adds latent load

4. **Review internal loads**: Verify actual occupancy and moisture-generating processes match design assumptions

5. **Control system**: Confirm proper operation of outdoor air dampers, cooling valves/compressors

6. **Part-load operation**: Verify adequate dehumidification at part-load (may need reduced airflow or dedicated dehumidification)

## Summary

Cooling and dehumidification is the fundamental air conditioning process that simultaneously reduces air temperature and moisture content. Key principles:

- **Process path**: Curved line from entering condition toward apparatus dew point on saturation curve
- **SHR and GSHF**: Define proportion of sensible to total cooling, determine required ADP
- **Bypass factor**: Quantifies coil effectiveness, lower BF provides better dehumidification
- **Condensate removal**: Equals mass of moisture extracted from airstream, requires proper drainage
- **Coil selection**: Balance between capacity, dehumidification performance, pressure drop, and cost
- **Control**: Maintaining dewpoint control is essential for humidity management

Proper application of these principles ensures effective cooling and humidity control while optimizing energy performance and occupant comfort.

## Related Topics

- Sensible Cooling (dry coil operation)
- Humidification Processes
- Air Mixing and Ventilation
- Psychrometric Chart Construction and Use
- Cooling Coil Performance and Selection
- Dehumidification Equipment and Strategies
