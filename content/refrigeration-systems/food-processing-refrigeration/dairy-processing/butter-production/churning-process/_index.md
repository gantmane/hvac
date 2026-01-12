---
title: "Churning Process"
description: "HVAC requirements for butter churning operations including temperature control, equipment heat loads, process room design, and cooling system specifications for batch and continuous churning systems"
weight: 2
---

## Process Overview

Butter churning converts cream into butter through mechanical agitation that inverts the fat-water emulsion. The process transforms cream (fat droplets dispersed in water) into butter (water droplets dispersed in fat). Temperature control during churning directly affects butter yield, texture, moisture content, and production efficiency.

The churning operation generates significant heat through mechanical work while requiring precise temperature maintenance. HVAC systems must remove equipment heat loads, maintain optimal working temperatures, and control humidity to prevent condensation on cold surfaces.

## Critical Temperature Parameters

### Churning Temperature Range

Optimal churning temperature depends on cream fat composition and desired butter characteristics:

| Parameter | Temperature Range | Purpose |
|-----------|------------------|---------|
| Summer cream churning | 8-10°C | Higher melting point fat requires lower temperature |
| Winter cream churning | 12-14°C | Lower melting point fat churns at higher temperature |
| Optimal general range | 10-12°C | Balances churning time with butter quality |
| Cream feed temperature | 8-13°C | Pre-cooled before entering churn |
| Buttermilk discharge | 10-15°C | Should exit at or above churning temperature |

Temperature control precision: ±0.5°C for consistent butter quality.

The churning temperature affects fat crystal structure. Too cold: excessive butter losses in buttermilk. Too warm: extended churning time, soft butter, poor texture.

### Temperature Control During Process Stages

**Phase 1: Agitation and Fat Destabilization**
- Duration: 15-45 minutes (batch), continuous (continuous systems)
- Temperature rise: 1-2°C from mechanical work
- Cooling requirement: Active temperature maintenance

**Phase 2: Butter Grain Formation**
- Critical temperature maintenance: ±0.5°C
- Heat generation: 0.8-1.2 kW per 1000 L cream capacity
- Temperature uniformity: Essential for consistent grain size

**Phase 3: Buttermilk Drainage**
- Buttermilk temperature: 10-15°C at discharge
- Drainage time: 2-5 minutes
- No active cooling typically required

**Phase 4: Washing (Optional)**
- Wash water temperature: 2-4°C below churning temperature
- Volume: 20-40% of cream volume
- Purpose: Remove residual buttermilk, lactose, proteins

**Phase 5: Working and Salting**
- Working temperature: 12-15°C
- Temperature rise: 2-4°C from mechanical work
- Active cooling: Required for continuous systems

## Batch Churning Systems

### Equipment Configuration

Traditional batch churns operate with intermittent production cycles:

**Barrel Churns**
- Capacity: 500-5000 L cream
- Rotation speed: 20-35 rpm
- Churning time: 30-60 minutes
- Fill ratio: 35-45% of total volume

**End-Over-End Churns**
- Capacity: 1000-3000 L cream
- Rotation speed: 25-40 rpm
- Churning time: 20-40 minutes
- More efficient agitation pattern

### Heat Load Calculations

Mechanical work converted to heat during batch churning:

Q_mech = P × η_heat × t

Where:
- Q_mech = Heat generated (kJ)
- P = Motor power (kW)
- η_heat = Fraction converted to heat (0.85-0.95)
- t = Churning time (seconds)

**Typical batch churn heat loads:**

| Churn Capacity | Motor Power | Heat Generation Rate | Total Heat Per Batch |
|----------------|-------------|---------------------|---------------------|
| 1000 L cream | 7.5 kW | 6.4 kW thermal | 460 kJ (30 min) |
| 2000 L cream | 11 kW | 9.4 kW thermal | 680 kJ (30 min) |
| 3000 L cream | 15 kW | 12.8 kW thermal | 920 kJ (30 min) |
| 5000 L cream | 22 kW | 18.7 kW thermal | 1345 kJ (30 min) |

### Batch Churn Cooling Methods

**External Jacket Cooling**
- Glycol/brine circulation through churn jacket
- Coolant temperature: 2-6°C
- Heat transfer coefficient: 250-400 W/m²·K
- Jacket surface area: 1.5-3.0 m² per 1000 L capacity

Required cooling capacity:

Q_cooling = Q_mech + Q_cream

Q_cream = m_cream × cp_cream × ΔT

Where:
- m_cream = Cream mass (kg)
- cp_cream = Specific heat (3.8-4.0 kJ/kg·K for 35-40% fat cream)
- ΔT = Temperature change (K)

**Internal Cooling Coils**
- Stainless steel coils submerged in cream
- Coolant: Chilled water or glycol (1-4°C)
- Surface area: 0.8-1.5 m² per 1000 L capacity
- Higher heat transfer effectiveness than external jacket

**Combined Cooling Systems**
- Both jacket and internal coils
- Used for large capacity churns (>3000 L)
- Faster temperature recovery between batches
- Better temperature uniformity

### Batch Process Room Temperature Control

Room conditions for batch churning operations:

| Parameter | Specification | Reason |
|-----------|--------------|---------|
| Air temperature | 12-16°C | Prevent butter softening during handling |
| Relative humidity | 60-75% | Minimize condensation risk |
| Air changes | 15-20 ACH | Remove moisture, control odors |
| Air velocity at equipment | <0.3 m/s | Prevent surface drying |
| Temperature stability | ±1°C | Consistent processing conditions |

## Continuous Churning Systems

### Fritz Continuous Churn

Modern high-capacity butter production uses continuous churning systems:

**Process Configuration**
- Continuous cream feed
- Cylindrical churning chamber with internal beaters
- Integrated buttermilk separation
- Continuous butter discharge to working section
- Production rate: 500-5000 kg butter/hour

**Temperature Control Zones**

| Zone | Function | Temperature | Cooling Method |
|------|----------|-------------|----------------|
| Cream feed | Pre-conditioning | 8-12°C | Plate heat exchanger upstream |
| Churning section | Phase inversion | 10-13°C | Jacketed cooling, internal coils |
| First working | Initial consolidation | 12-14°C | Jacketed cooling |
| Second working | Final texture | 13-15°C | Jacketed cooling |
| Extrusion | Butter discharge | 12-14°C | Minimal cooling |

### Continuous System Heat Loads

Heat generation in continuous churning is constant during operation:

**Churning Section Heat Load**

Q_churn = P_motor × η_heat + Q_friction

Where:
- P_motor = Churning motor power (kW)
- η_heat = Heat conversion efficiency (0.85-0.92)
- Q_friction = Bearing and seal friction heat (5-10% of motor power)

**Working Section Heat Load**

Q_work = P_work × η_heat

Where P_work = working section motor power (typically 30-50% of churning power)

**Total continuous system heat loads:**

| Production Capacity | Churning Power | Working Power | Total Heat Load |
|---------------------|----------------|---------------|-----------------|
| 500 kg/h butter | 15 kW | 7 kW | 19 kW thermal |
| 1000 kg/h butter | 25 kW | 11 kW | 31 kW thermal |
| 2000 kg/h butter | 45 kW | 18 kW | 54 kW thermal |
| 3000 kg/h butter | 60 kW | 25 kW | 73 kW thermal |
| 5000 kg/h butter | 90 kW | 38 kW | 110 kW thermal |

### Continuous Churn Cooling System Design

**Jacket Cooling Circuit**

Required coolant flow rate:

m_coolant = Q_remove / (cp_coolant × ΔT_coolant)

Where:
- Q_remove = Heat removal rate (kW)
- cp_coolant = Coolant specific heat (3.4 kJ/kg·K for 30% glycol)
- ΔT_coolant = Temperature rise through jacket (3-6°C)

**Design specifications:**

| Parameter | Value | Notes |
|-----------|-------|-------|
| Coolant supply temperature | 2-5°C | Below churning temperature |
| Coolant return temperature | 6-10°C | Limited rise for effectiveness |
| Flow velocity | 0.5-1.2 m/s | Turbulent flow in jacket |
| Jacket gap | 25-50 mm | Uniform coolant distribution |
| Material | 316 stainless steel | Dairy-grade corrosion resistance |

**Refrigeration System Requirements**

For continuous churning operation, dedicated refrigeration capacity:

Q_refrig = Q_churn + Q_work + Q_transmission + Q_cream_cooling

Q_transmission = U × A × ΔT

Where:
- U = Overall heat transfer coefficient (0.8-1.2 W/m²·K for insulated equipment)
- A = External surface area (m²)
- ΔT = Temperature difference to ambient (K)

Safety factor: 1.15-1.25 for capacity sizing

## Buttermilk Temperature Management

### Buttermilk Characteristics

Buttermilk discharged from churning contains:
- 0.4-0.7% fat (represents butter losses)
- 3.5-4.0% protein
- 4.5-5.0% lactose
- Temperature: 10-15°C at discharge

### Buttermilk Heat Recovery

The sensible heat in buttermilk can be recovered:

Q_buttermilk = m_buttermilk × cp_buttermilk × (T_buttermilk - T_ref)

Where:
- m_buttermilk = Mass flow rate (kg/s)
- cp_buttermilk = 3.9 kJ/kg·K (approximates skim milk)
- T_buttermilk = Discharge temperature (°C)
- T_ref = Reference temperature, typically 4°C storage

**Heat Recovery System Design**

Plate heat exchanger for buttermilk-to-cream heat exchange:
- Hot side: Buttermilk at 12-15°C → cooled to 4-6°C
- Cold side: Incoming cream warmed by 3-5°C
- Heat transfer effectiveness: 0.6-0.75
- Energy savings: 15-25% of cream cooling load

| Production Rate | Buttermilk Flow | Available Heat Recovery | Energy Value |
|-----------------|-----------------|------------------------|--------------|
| 500 kg/h butter | 450 L/h | 4.5 kW | 4 GJ/month |
| 1000 kg/h butter | 900 L/h | 9.0 kW | 8 GJ/month |
| 2000 kg/h butter | 1800 L/h | 18.0 kW | 16 GJ/month |
| 5000 kg/h butter | 4500 L/h | 45.0 kW | 40 GJ/month |

Assumes 20 hours/day operation, 22 days/month.

## Process Room HVAC Design

### Design Conditions

**Summer Design Conditions**
- Outdoor: 32°C DB, 24°C WB
- Indoor: 14°C, 70% RH
- Refrigeration load: Maximum

**Winter Design Conditions**
- Outdoor: -10°C
- Indoor: 14°C, 65% RH
- Heating load: Minimal due to equipment heat

### Cooling Load Components

**1. Equipment Heat Gain**

Sum of all churning and working equipment as calculated above.

**2. Transmission Load**

Q_transmission = U_wall × A_wall × (T_outdoor - T_indoor) + U_roof × A_roof × (T_outdoor - T_indoor + ΔT_solar)

Where:
- U_wall = 0.25-0.35 W/m²·K (insulated wall)
- U_roof = 0.20-0.28 W/m²·K (insulated roof)
- ΔT_solar = 10-15°C (solar load on roof)

**3. Infiltration Load**

Q_infiltration = n × V × ρ_air × (h_outdoor - h_indoor)

Where:
- n = Air change rate from infiltration (0.5-1.0 ACH)
- V = Room volume (m³)
- ρ_air = Air density (1.2 kg/m³)
- h = Enthalpy from psychrometric chart (kJ/kg)

**4. Lighting Load**

Q_lighting = W_lighting × A_floor × f_use

Where:
- W_lighting = 8-12 W/m² (LED lighting)
- A_floor = Floor area (m²)
- f_use = Usage factor (0.8-1.0)

**5. Occupancy Load**

Q_occupancy = n_people × (Q_sensible + Q_latent)

Where:
- n_people = Number of operators
- Q_sensible = 75 W/person (light work at 14°C)
- Q_latent = 55 W/person

**6. Product Load**

Negligible for churning, as cream enters near room temperature.

### Total Cooling Load Summary

For a typical continuous butter production facility (2000 kg/h capacity):

| Load Component | Heat Gain (kW) | Percentage |
|----------------|----------------|------------|
| Equipment (churning + working) | 54.0 | 68% |
| Transmission (walls, roof) | 8.5 | 11% |
| Infiltration | 6.2 | 8% |
| Lighting (200 m² floor) | 2.0 | 3% |
| Occupancy (4 operators) | 0.5 | 1% |
| Ventilation air (makeup) | 7.8 | 10% |
| **Total** | **79.0** | **100%** |

Design capacity with safety factor (1.15): 91 kW

### HVAC System Configuration

**Recommended System: Ducted Direct Expansion with Reheat**

**Air Handling Unit Specifications**
- Supply air volume: 8000-12000 m³/h (15-20 ACH)
- Supply air temperature: 8-10°C
- Return air temperature: 14-15°C
- Mixed air: 70% return, 30% outdoor (minimum ventilation)
- Cooling coil: DX evaporator, 3-5°C evaporating temperature
- Reheat coil: Hot gas or electric, for humidity control
- Supply air filter: MERV 8 (minimum), MERV 11 (recommended)

**Refrigeration System**
- Type: Direct expansion or glycol loop from central plant
- Refrigerant: R-404A, R-507A, or R-448A (HFO alternatives)
- Evaporating temperature: 0 to -5°C
- Condensing temperature: 35-45°C (air-cooled), 30-38°C (water-cooled)
- Compressor type: Screw or scroll for continuous operation

**Humidity Control Strategy**

Churning rooms require dehumidification to prevent condensation on cold equipment surfaces.

Moisture removal rate:

m_moisture = ρ_air × Q_air × (ω_outdoor - ω_indoor)

Where:
- ρ_air = 1.2 kg/m³
- Q_air = Outdoor air volume flow (m³/s)
- ω = Humidity ratio from psychrometric chart (kg moisture/kg dry air)

Cooling coil dehumidification:
- Coil surface temperature: 2-4°C (below dew point)
- Condensate removal: 2-5 L/h per 1000 m³/h outdoor air
- Reheat requirement: 1.5-3 kW per 1000 m³/h to reach supply temperature

### Air Distribution Design

**Supply Air Delivery**
- High sidewall diffusers or perforated duct
- Throw distance: 10-15 m
- Discharge velocity: 3-5 m/s
- Terminal velocity at work zone: <0.3 m/s
- Temperature differential: 4-6°C below room

**Return Air Collection**
- Low sidewall or floor-level returns
- Location: Away from supply air to ensure circulation
- Return velocity: <2.5 m/s at grilles
- Return air path: Minimum 3 m from supply discharge

**Ventilation Air Requirements**

Minimum outdoor air for odor control and pressurization:
- 0.5 L/s per m² floor area (minimum)
- Or 20-30% of supply air volume
- Positive pressure: 5-10 Pa relative to adjacent spaces

## Equipment Specifications

### Batch Churn Cooling Requirements

**Small Batch Churn (1000-2000 L)**
- Jacket cooling capacity: 8-12 kW
- Coolant flow rate: 15-25 L/min
- Coolant temperature: 2-4°C
- Control valve: Modulating, 0-10 VDC signal
- Temperature sensor: RTD, ±0.2°C accuracy

**Large Batch Churn (3000-5000 L)**
- Jacket cooling capacity: 18-28 kW
- Internal coil capacity: 10-15 kW (if used)
- Total coolant flow: 40-70 L/min
- Coolant temperature: 2-4°C
- Control: Cascade control, inner loop on coolant valve, outer loop on cream temperature

### Continuous Churn Cooling Requirements

**Medium Capacity (1000-2000 kg/h butter)**
- Churning section cooling: 25-35 kW
- Working section cooling: 15-20 kW
- Total coolant flow: 60-90 L/min
- Coolant supply temperature: 2-5°C
- Coolant return temperature: 6-10°C
- Temperature control: PID with feedforward compensation

**High Capacity (3000-5000 kg/h butter)**
- Churning section cooling: 50-75 kW
- Working section cooling: 30-45 kW
- Total coolant flow: 140-200 L/min
- Multiple cooling zones with independent control
- Redundant cooling circuits for production continuity

### Refrigeration Plant Sizing

Total refrigeration capacity for churning facility:

Q_refrig_total = Q_equipment + Q_room + Q_buttermilk_cooling + Q_misc

**Equipment refrigeration:**
- Churn jacket/coil cooling
- Temperature: -2 to +5°C glycol supply
- Immediate response required

**Room HVAC refrigeration:**
- Air conditioning system
- Temperature: 0 to -5°C evaporating
- Continuous operation

**Buttermilk cooling refrigeration:**
- Storage tank cooling
- Temperature: 0 to +2°C glycol supply
- Scheduled operation

Design approach: Separate refrigeration circuits for equipment cooling and space conditioning to allow independent control and maintenance.

## Energy Efficiency Considerations

### Heat Recovery Opportunities

**1. Buttermilk Heat Recovery**
- Preheat incoming cream
- Energy recovery: 15-25% of cream cooling load
- Payback period: 1-2 years

**2. Compressor Heat Recovery**
- Hot gas desuperheater for hot water generation
- Water heating to 50-60°C for CIP systems
- Energy recovery: 20-30% of compressor power
- Payback period: 2-3 years

**3. Exhaust Air Heat Recovery**
- Run-around glycol loop or heat pipe
- Preheat ventilation air in winter
- Energy recovery effectiveness: 50-65%
- Payback period: 3-5 years (climate dependent)

### Variable Speed Drive Applications

**Refrigeration Compressors**
- Load variation: 40-100% during batch operation, 70-100% continuous
- Energy savings: 15-25% compared to stepped control
- Required turndown: 3:1 minimum

**Air Handling Unit Fans**
- Variable air volume for load-following
- Night setback capability
- Energy savings: 20-35% compared to constant volume

**Coolant Circulation Pumps**
- Flow modulation based on temperature control demand
- Energy savings: 10-20% compared to constant flow

### Operational Energy Optimization

**Temperature Setpoint Optimization**
- Churning at upper end of acceptable range (12-13°C vs 8-10°C)
- Reduces refrigeration load by 20-30%
- Must balance against butter quality requirements

**Batch Schedule Optimization**
- Align peak churning loads with off-peak electricity rates
- Cold storage of cream to allow flexible scheduling
- Potential cost savings: 15-30% in time-of-use markets

**Load Shedding Strategies**
- Pre-cool equipment during off-peak hours
- Thermal mass utilization
- Demand response participation

## Control System Design

### Temperature Control Architecture

**Batch Churn Control**
- PID control on cream temperature
- Manipulated variable: Coolant valve position
- Setpoint: 10-13°C (product dependent)
- Control precision: ±0.5°C
- Tuning: Conservative (minimize overshoot)

**Continuous Churn Control**
- Multi-zone cascade control
- Inner loop: Coolant temperature (fast response)
- Outer loop: Product temperature (slow response)
- Feedforward: Cream flow rate and temperature
- Control precision: ±0.3°C

### HVAC Control Integration

**Room Temperature Control**
- Modulating cooling via refrigerant flow or coolant valve
- Reheat for humidity control
- Setpoint: 14°C ±1°C
- Night setback: 16-18°C (unoccupied periods)

**Humidity Control**
- Target: 65-70% RH
- Method: Overcool and reheat
- Dehumidification active when RH > 72%
- Humidification not typically required

**Ventilation Control**
- CO2-based demand control ventilation (if occupancy varies)
- Minimum outdoor air damper position: 30%
- Maximum outdoor air: 100% (free cooling when available)

## Maintenance Requirements

### Cooling System Maintenance

**Weekly Tasks**
- Inspect coolant levels and pressures
- Check for leaks at connections
- Verify temperature control performance
- Clean coolant strainers

**Monthly Tasks**
- Test coolant concentration (if glycol)
- Inspect coolant pump operation
- Check control valve operation
- Review temperature trend data

**Quarterly Tasks**
- Clean cooling coils and jackets
- Inspect insulation condition
- Verify control sensor calibration
- Analyze coolant for contamination

**Annual Tasks**
- Complete cooling system CIP (clean-in-place)
- Replace coolant (if required)
- Recalibrate all temperature sensors
- Test emergency shutdown systems

### HVAC System Maintenance

**Monthly Tasks**
- Replace/clean air filters
- Inspect refrigerant levels and pressures
- Check condensate drainage
- Verify control sequences

**Quarterly Tasks**
- Clean evaporator and condenser coils
- Inspect fan belts and bearings
- Test humidity control operation
- Review energy consumption trends

**Annual Tasks**
- Complete refrigeration system service
- Duct cleaning and inspection
- Control system calibration
- Airflow measurements and balancing

## Safety Considerations

### Temperature Safety

**High Temperature Alarm**
- Setpoint: 16°C (churning process)
- Action: Alert operator, reduce production rate
- Consequence of failure: Soft butter, quality issues

**Low Temperature Alarm**
- Setpoint: 7°C (churning process)
- Action: Alert operator, reduce cooling
- Consequence of failure: Extended churning time, butter losses

### Refrigerant Safety

**Refrigerant Detection**
- Sensors in equipment rooms and occupied spaces
- Alarm level: 25% of TLV-TWA
- Emergency ventilation activation: 50% of TLV-TWA

**Emergency Procedures**
- Refrigerant leak response plan
- Evacuation thresholds
- Emergency ventilation capacity: 0.3 m³/s per kg refrigerant charge

### Personnel Safety

**Cold Surface Protection**
- Guard rails around cold equipment
- Warning signage on sub-ambient surfaces
- Personal protective equipment requirements

**Electrical Safety**
- Equipment in wet areas: IP67 minimum
- GFCI protection for 120V circuits
- Lockout/tagout procedures for maintenance

---

**Related Topics:**
- Cream Aging and Cooling
- Butter Working and Texturization
- CIP Systems for Churning Equipment
- Refrigerant System Design for Dairy Processing
