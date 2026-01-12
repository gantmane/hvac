---
title: "Sweet Potato Storage"
description: "Technical specifications for sweet potato curing and storage refrigeration systems including wound healing requirements, chilling injury prevention, humidity control, and specialized equipment design for 4-7 month storage periods"
weight: 5
---

## Overview

Sweet potato storage requires two distinct environmental phases: initial curing for wound healing and subsequent long-term storage. The curing process is critical for developing protective suberized layers over harvest wounds, while proper storage conditions prevent chilling injury and maintain quality. Unlike other root crops, sweet potatoes are highly sensitive to low temperatures and require precise control above 13°C.

## Curing Phase Requirements

### Temperature and Humidity Specifications

Sweet potato curing establishes wound healing through suberization, requiring elevated temperature and humidity:

| Parameter | Specification | Tolerance | Purpose |
|-----------|--------------|-----------|---------|
| Temperature | 29-32°C | ±0.5°C | Optimal enzyme activity |
| Relative Humidity | 85-90% | ±2% | Prevent moisture loss |
| Duration | 4-7 days | Varies by damage | Complete wound healing |
| Air Velocity | 0.1-0.3 m/s | Maximum | Uniform conditions |

### Curing Process Physics

The curing process involves enzymatic suberization where periderm cells at wound sites develop protective corky layers. The rate of suberization follows temperature-dependent kinetics:

**Suberization Rate Equation:**

```
R_sub = A × e^(-E_a/(R×T))
```

Where:
- R_sub = Suberization rate (μm/day)
- A = Pre-exponential factor (1.8 × 10^8 μm/day)
- E_a = Activation energy (62 kJ/mol)
- R = Universal gas constant (8.314 J/(mol·K))
- T = Absolute temperature (K)

At 30°C (303 K), suberization proceeds at approximately 40-50 μm/day, achieving protective layers of 150-200 μm within 4-5 days.

### Curing Room Design

#### Heating System Requirements

Curing rooms require substantial heating capacity to maintain 29-32°C:

**Heating Load Calculation:**

```
Q_heat = Q_product + Q_transmission + Q_ventilation + Q_evaporation
```

**Product Heating Load:**

```
Q_product = (m_product × c_p × ΔT) / t_heat
```

For 20,000 kg sweet potatoes heated from 15°C to 30°C over 8 hours:
- m_product = 20,000 kg
- c_p = 3.6 kJ/(kg·K) (sweet potato specific heat)
- ΔT = 15 K
- t_heat = 28,800 s

```
Q_product = (20,000 × 3.6 × 15) / 28,800 = 37.5 kW
```

**Transmission Load:**

```
Q_transmission = U × A × (T_inside - T_ambient)
```

For 200 m² surface area, U = 0.25 W/(m²·K), T_inside = 30°C, T_ambient = 20°C:

```
Q_transmission = 0.25 × 200 × 10 = 0.5 kW
```

**Evaporative Load:**

Sweet potatoes lose moisture during curing at approximately 0.5-1.0% mass loss:

```
Q_evaporation = (m_loss × h_fg) / t_cure
```

For 1% mass loss (200 kg water) over 5 days:
- m_loss = 200 kg
- h_fg = 2,450 kJ/kg (latent heat of vaporization)
- t_cure = 432,000 s

```
Q_evaporation = (200 × 2,450) / 432,000 = 1.13 kW
```

**Total Heating Capacity:**

```
Q_total = 37.5 + 0.5 + 1.13 + Q_ventilation ≈ 45-50 kW
```

#### Humidification System

Maintaining 85-90% RH at 30°C requires continuous moisture addition:

**Required Humidification Rate:**

```
m_humidification = V × ρ_air × ACH × (ω_target - ω_supply)
```

For 500 m³ curing room, 2 ACH, at 30°C:
- ω_target = 0.024 kg_water/kg_dry air (85% RH at 30°C)
- ω_supply = 0.015 kg_water/kg_dry air (outdoor air at 20°C, 60% RH)
- ρ_air = 1.15 kg/m³

```
m_humidification = 500 × 1.15 × 2 × (0.024 - 0.015) = 10.4 kg/h
```

**Equipment Selection:**

- Steam humidifiers: 10-15 kg/h capacity
- Atomizing nozzles: 20-30 μm droplet size
- Distribution: Perforated ducting or overhead manifold

### Curing Room Control Strategy

**Temperature Control:**
- Modulating hot water or steam coils
- PID control with ±0.5°C setpoint
- Supply air temperature 32-35°C
- Return air temperature 29-31°C

**Humidity Control:**
- Continuous RH measurement (capacitive sensors)
- Proportional humidifier control
- High-limit safety at 92% RH
- Low-limit alarm at 83% RH

**Air Distribution:**
- Horizontal airflow across product bins
- Supply air velocity 0.2-0.3 m/s at product surface
- Return air plenum below floor or overhead
- Minimum mixing to maintain uniformity

## Long-Term Storage Phase

### Storage Temperature Requirements

Following curing, sweet potatoes transition to long-term storage with precise temperature control:

| Storage Duration | Temperature Range | Optimal Setpoint | Maximum Deviation |
|-----------------|-------------------|------------------|-------------------|
| 0-2 months | 13-16°C | 15°C | ±1.0°C |
| 2-4 months | 13-15°C | 14°C | ±0.5°C |
| 4-7 months | 13-14°C | 13.5°C | ±0.5°C |

### Chilling Injury Mechanisms

Sweet potatoes suffer irreversible chilling injury below 13°C due to membrane phase transitions and metabolic disruption:

**Critical Temperature Thresholds:**

| Temperature | Duration | Injury Symptoms | Mechanism |
|-------------|----------|-----------------|-----------|
| 10-13°C | >7 days | Pitting, internal discoloration | Membrane lipid crystallization |
| 7-10°C | >3 days | Hard core, off-flavor | Enzymatic browning activation |
| <7°C | >24 hours | Severe decay, total loss | Cell membrane rupture |

**Membrane Phase Transition:**

Chilling injury correlates with lipid phase transition temperature (T_m):

```
T_m = f(fatty acid composition)
```

Sweet potato membrane lipids have T_m ≈ 12-14°C. Below this temperature, membranes transition from liquid-crystalline to gel phase, losing selective permeability and causing:
- Electrolyte leakage
- Enzyme compartmentation loss
- Oxidative stress
- Phenolic compound oxidation (browning)

### Storage Humidity Control

Maintaining 85-90% RH prevents moisture loss while avoiding surface condensation:

**Vapor Pressure Deficit (VPD):**

```
VPD = P_sat(T_product) - P_vapor(T_air, RH)
```

At 14°C storage, 87.5% RH (midpoint):
- P_sat(14°C) = 1.598 kPa
- P_vapor = 0.875 × 1.598 = 1.398 kPa
- VPD = 1.598 - 1.398 = 0.200 kPa

This VPD maintains transpiration rate at approximately 0.5-0.8 mg/(kg·h), resulting in:
- Total moisture loss: 3-5% over 6 months
- No visible shriveling
- Maintained turgor pressure

**Condensation Prevention:**

Surface condensation occurs when product surface temperature drops below dew point. For 14°C storage at 90% RH:
- T_dew = 12.6°C

Evaporator coil temperature must remain above 10°C to prevent excessive dehumidification. Coil approach temperature:

```
ΔT_approach = T_storage - T_coil ≥ 4 K
```

Maximum coil temperature differential: 4-5 K

### Storage Duration and Quality Degradation

Sweet potato storage life depends on temperature, humidity, and variety:

**Respiration Rate:**

```
R_resp = R_0 × Q_10^((T - T_ref)/10)
```

Where:
- R_0 = 5 mg CO₂/(kg·h) at 0°C
- Q_10 = 2.5 for sweet potatoes
- T_ref = 0°C

At 14°C storage:

```
R_resp = 5 × 2.5^(14/10) = 5 × 3.52 = 17.6 mg CO₂/(kg·h)
```

**Respiratory Heat Generation:**

```
Q_resp = (R_resp × m_product × H_comb) / (44 g/mol)
```

Where H_comb = 479 kJ/mol CO₂ produced:

For 50,000 kg stored sweet potatoes:

```
Q_resp = (17.6 mg/(kg·h) × 50,000 kg × 479 kJ/mol) / (44,000 mg/mol)
Q_resp = 9.55 kJ/h = 2.65 kW
```

**Storage Life Prediction:**

Quality degradation rate follows first-order kinetics:

```
Q(t) = Q_0 × e^(-k×t)
```

Where k = rate constant dependent on temperature:

| Temperature | Rate Constant k (month⁻¹) | Half-Life (months) |
|-------------|---------------------------|---------------------|
| 13°C | 0.10 | 6.9 |
| 14°C | 0.12 | 5.8 |
| 15°C | 0.15 | 4.6 |
| 16°C | 0.20 | 3.5 |

Practical storage duration at 14°C: 5-6 months to maintain >80% of initial quality.

## Refrigeration System Design

### Cooling Load Components

**Total Refrigeration Load:**

```
Q_total = Q_product + Q_resp + Q_transmission + Q_infiltration + Q_equipment + Q_people
```

#### Product Cooling Load

Minimal after curing, as product enters storage at 14-15°C:

```
Q_product = (m_product × c_p × ΔT) / 24 hours
```

For 1°C temperature pulldown:

```
Q_product = (50,000 kg × 3.6 kJ/(kg·K) × 1 K) / 86,400 s = 2.08 kW
```

#### Respiratory Heat Load

As calculated previously: Q_resp = 2.65 kW

#### Transmission Load

```
Q_transmission = U × A × (T_ambient - T_storage)
```

For 1,000 m² envelope, U = 0.20 W/(m²·K), summer ambient 30°C:

```
Q_transmission = 0.20 × 1,000 × (30 - 14) = 3.2 kW
```

#### Infiltration Load

```
Q_infiltration = V_inf × ρ_air × c_p × ΔT + V_inf × ρ_air × Δω × h_fg
```

For 2,000 m³ storage, 0.5 air changes per day:

**Sensible component:**

```
Q_sensible = (2,000 × 0.5 / 24) × 1.2 × 1.005 × (30 - 14) = 0.67 kW
```

**Latent component:**

```
Q_latent = (2,000 × 0.5 / 24) × 1.2 × (0.024 - 0.009) × 2,450 = 1.53 kW
```

```
Q_infiltration = 0.67 + 1.53 = 2.20 kW
```

#### Equipment and Occupancy

- Evaporator fans: 0.8-1.2 kW
- Lighting (LED, minimal): 0.2 kW
- Occupancy (occasional): 0.3 kW average

**Total Design Load:**

```
Q_design = 2.08 + 2.65 + 3.2 + 2.20 + 1.2 + 0.3 = 11.63 kW
```

**With 20% safety factor:**

```
Q_design = 11.63 × 1.20 = 14.0 kW (4.0 tons)
```

### Refrigeration System Configuration

#### System Type Selection

**Unit Cooler System:**
- Direct expansion (DX) with R-404A, R-448A, or R-449A
- Low temperature differential evaporators
- Electronic expansion valve (EEV) control
- Multiple circuits for capacity modulation

**System Schematic:**

```
Compressor → Condenser → Receiver → Filter/Drier → EEV → Evaporator → Compressor
              ↓
         Subcooling (3-5 K)
```

#### Evaporator Specifications

Critical parameters for sweet potato storage:

| Parameter | Specification | Justification |
|-----------|--------------|---------------|
| Coil TD | 4-5 K | Prevent excessive dehumidification |
| Face Velocity | 1.5-2.0 m/s | Low air velocity across product |
| Fin Spacing | 6-8 mm | Adequate for high humidity |
| Defrost Type | Electric or hot gas | Minimal temperature fluctuation |
| Defrost Frequency | Every 8-12 hours | High humidity operation |
| Fan Motor | ECM or VFD | Variable speed for precise control |

**Evaporator Coil Temperature:**

```
T_coil = T_storage - TD = 14 - 5 = 9°C
```

Corresponding saturation pressure for R-404A: 4.5 bar (absolute)

#### Capacity Modulation

Sweet potato storage requires precise capacity control due to low cooling load variation:

**Modulation Methods:**

1. **Variable Speed Compressor:**
   - 25-100% capacity range
   - Inverter-driven scroll or screw compressor
   - High efficiency at part load

2. **Multiple Circuits:**
   - 2-3 independent refrigeration circuits
   - Step capacity control (50%, 75%, 100%)
   - Redundancy for critical storage

3. **Evaporator Fan Control:**
   - VFD or multi-speed motors
   - 30-100% airflow range
   - Coordinated with compressor capacity

**Control Strategy:**

```
Compressor Speed = f(T_storage - T_setpoint, RH_storage)
```

PID control with:
- P = 20% per K deviation
- I = 0.1 repeats/minute
- D = 2 minutes

### Humidity Control Integration

Maintaining 85-90% RH in refrigerated storage requires careful balance:

**Dehumidification Control:**

Evaporator operation inherently dehumidifies. To maintain high RH:

1. **Large Coil Surface Area:**
   - Low face velocity reduces moisture removal
   - Coil TD minimum 4 K

2. **Humidification System:**
   - Ultrasonic or centrifugal atomizers
   - 2-5 kg/h capacity
   - Activated when RH < 85%

3. **Air Circulation:**
   - Continuous low-velocity circulation (0.3-0.5 m/s)
   - Prevents localized dry zones
   - ECM fans at 40-60% speed during steady-state

**Humidity Control Logic:**

```
IF RH < 85%:
    Activate humidifier
    Reduce evaporator fan speed 10%
ELSE IF RH > 90%:
    Increase evaporator fan speed 10%
    Reduce humidifier output 50%
ELSE:
    Maintain current settings
```

## Equipment Specifications

### Compressor Selection

**Reciprocating Compressor (Small Systems <20 kW):**

| Specification | Value | Notes |
|--------------|-------|-------|
| Type | Semi-hermetic reciprocating | Serviceable |
| Displacement | 25-35 m³/h | At 1,450 rpm |
| Capacity Control | Cylinder unloading (50%, 100%) | Step control |
| Evaporating Temperature | 5-10°C | Matches coil temperature |
| Condensing Temperature | 35-40°C | Air-cooled condenser |
| Power Input | 3-5 kW | At design conditions |
| Oil Type | POE (polyolester) | HFC refrigerant compatible |

**Scroll Compressor with Inverter (Medium Systems 20-50 kW):**

| Specification | Value | Notes |
|--------------|-------|-------|
| Type | Variable speed scroll | Continuous modulation |
| Speed Range | 30-120 Hz | 25-100% capacity |
| Capacity | 15-40 kW | At design conditions |
| Oil Management | Internal separator | >99% efficiency |
| Sound Level | 65-70 dB(A) | At 1 meter |
| COP | 3.5-4.2 | At part load conditions |

### Evaporator Unit Specifications

**Low TD Unit Cooler:**

| Component | Specification | Purpose |
|-----------|--------------|---------|
| Coil Material | Copper tubes, aluminum fins | Standard construction |
| Tube Diameter | 12-16 mm | Low pressure drop |
| Fin Spacing | 6-8 mm | High humidity operation |
| Circuits | 4-6 independent | Uniform distribution |
| Face Area | 6-10 m² | Low face velocity |
| Air Throw | 15-20 meters | Uniform distribution |
| Fan Type | Axial, backward curved | High efficiency |
| Fan Motors | ECM, 0.5-1.0 kW each | Variable speed |
| Drain Pan | Stainless steel, heated | Prevent freezing |
| Defrost | Electric (6 kW) or hot gas | 20-30 minute cycle |

### Condenser Specifications

**Air-Cooled Condenser:**

| Parameter | Specification | Notes |
|-----------|--------------|-------|
| Type | Forced draft, V-bank | Compact footprint |
| Approach Temperature | 8-12 K | Above ambient |
| Face Velocity | 2.0-2.5 m/s | Low noise |
| Fan Control | VFD or cycling | Floating head pressure |
| Minimum Capacity | 25% of design | Head pressure control |
| Coil Material | Copper tubes, aluminum fins | Corrosion resistant coating |

**Evaporative Condenser (Alternative):**

- 30-40% higher efficiency than air-cooled
- Water consumption: 3-5 L/kW·h
- Requires water treatment system
- Not recommended for freezing climates without winterization

### Control System Architecture

**Programmable Logic Controller (PLC) System:**

**Input Signals:**
- Temperature sensors (4-20 mA RTD): 6-8 locations
- Humidity sensors (4-20 mA): 3-4 locations
- Refrigerant pressure transducers: 4 (suction, discharge, liquid, economizer)
- Door switches: Digital inputs
- Current transducers: Compressor, fans

**Output Signals:**
- Compressor speed control (0-10 VDC or 4-20 mA)
- Evaporator fan VFDs (Modbus RTU)
- EEV control (pulse width modulation)
- Defrost heaters (relay outputs)
- Humidifier control (4-20 mA)
- Alarm outputs (relay, dry contact)

**Control Functions:**
- PID temperature control (±0.5°C)
- Humidity control with deadband (±2% RH)
- Adaptive defrost initiation (pressure or time-based)
- Compressor capacity optimization
- Energy management and load shedding
- Alarm annunciation and logging

### Monitoring and Data Logging

**Critical Parameters to Monitor:**

| Parameter | Frequency | Alarm Limits | Action |
|-----------|-----------|--------------|--------|
| Storage Temperature | 1 minute | 12.5°C / 16.5°C | Email + text alert |
| Storage Humidity | 5 minutes | 80% / 92% | Local alarm |
| Compressor Discharge Temp | 1 minute | >110°C | Shutdown |
| Suction Pressure | 1 minute | <3.5 bar / >6.0 bar | Capacity adjust |
| Defrost Termination Temp | Per defrost | >20°C | Extended defrost |
| Door Open Time | Continuous | >5 minutes | Alert operator |

**Data Retention:**
- 1-minute intervals: 7 days
- 15-minute averages: 6 months
- Daily averages: 5 years
- Alarm events: Permanent

## Quality Parameters and Inspection

### Incoming Product Assessment

Pre-storage quality inspection ensures optimal storage outcomes:

**Physical Parameters:**

| Parameter | Acceptable Range | Rejection Criteria |
|-----------|------------------|-------------------|
| Skin integrity | >95% intact | Cuts >10 mm deep |
| Size uniformity | 50-100 mm diameter | <40 mm or >120 mm |
| Dry matter content | 25-35% | <20% (immature) |
| Field heat temperature | 15-25°C | >30°C requires cooling |
| Visible decay | None | Any soft rot present |

**Pre-Storage Procedures:**
1. Sort and grade within 24 hours of harvest
2. Remove damaged, diseased, or undersized roots
3. Allow field heat dissipation to 20°C before curing
4. Load into bins with 70-80% fill ratio for air circulation

### In-Storage Monitoring

**Weekly Inspection Protocol:**

1. **Temperature Mapping:**
   - Measure at 12 locations throughout storage
   - Record warmest and coldest zones
   - Maximum variation <2°C acceptable

2. **Product Sampling:**
   - Inspect 20 sweet potatoes per 10,000 kg stored
   - Check for sprout development, shrivel, decay
   - Document defects by type and location

3. **Environmental Verification:**
   - Verify RH sensors with calibrated hygrometer
   - Check air circulation patterns (smoke test)
   - Inspect drain pans for ice accumulation

**Quality Degradation Indicators:**

| Defect | Cause | Corrective Action |
|--------|-------|-------------------|
| Sprouting | Temperature >16°C, high RH | Lower setpoint 1°C |
| Shriveling | RH <80%, excessive air velocity | Increase humidity, reduce airflow |
| Pitting | Temperature fluctuation, chilling | Stabilize at 14°C |
| Internal discoloration | Exposure to <13°C | Discard affected, verify controls |
| Surface mold | RH >92%, poor circulation | Increase air movement, reduce RH |
| Soft rot | Disease entry, warm zones | Remove affected, inspect cooling |

### Post-Storage Conditioning

Sweet potatoes removed from 13-14°C storage require temperature conditioning before processing or shipment:

**Warming Protocol:**

| Destination | Target Temperature | Warming Rate | Duration |
|-------------|-------------------|--------------|----------|
| Fresh market | 18-20°C | 2°C per day | 3-4 days |
| Processing | 20-24°C | 3°C per day | 2-3 days |
| Retail distribution | 16-18°C | 2°C per day | 2-3 days |

Gradual warming prevents condensation and allows metabolic adjustment.

## Energy Efficiency Optimization

### Operating Cost Analysis

**Annual Energy Consumption:**

For 2,000 m³ storage facility (500 tonnes capacity):

```
E_annual = (Q_avg × h_operation × COP^-1) + E_aux
```

Where:
- Q_avg = 8 kW (average load)
- h_operation = 6,000 hours (7 months × 720 h/month + curing)
- COP = 3.8 (seasonal average)
- E_aux = 7,200 kWh (fans, controls, humidifiers)

```
E_annual = (8 × 6,000 / 3.8) + 7,200 = 12,632 + 7,200 = 19,832 kWh
```

At $0.12/kWh: Annual energy cost = $2,380

**Cost per Tonne Stored:**

```
Energy cost = $2,380 / 500 tonnes = $4.76/tonne
```

### Efficiency Improvement Measures

**High-Efficiency Equipment:**

| Upgrade | Energy Savings | Payback Period | Investment |
|---------|----------------|----------------|------------|
| Variable speed compressor | 20-30% | 3-4 years | $8,000-12,000 |
| ECM evaporator fans | 40-50% fan energy | 2-3 years | $2,000-3,000 |
| Advanced controls (PLC) | 10-15% overall | 4-5 years | $5,000-8,000 |
| LED lighting | 60-70% lighting | 1-2 years | $1,000-1,500 |

**Operational Optimization:**

1. **Night Cooling:**
   - Utilize cool ambient temperatures during night hours
   - Increase ventilation when T_ambient < T_storage + 2°C
   - Potential savings: 5-10% during spring/fall storage

2. **Demand Response:**
   - Pre-cool storage 1-2°C before peak demand periods
   - Thermal mass maintains conditions during 2-4 hour curtailment
   - Utility incentives: $100-300/kW·year

3. **Defrost Optimization:**
   - Demand-based defrost initiation (pressure differential >50 Pa)
   - Reduce frequency from fixed 12h to actual need
   - Savings: 15-20% of defrost energy

## System Commissioning and Startup

### Pre-Startup Checklist

**Mechanical Systems:**
- [ ] Refrigerant charge verified (superheat/subcool method)
- [ ] All valves, dampers positioned correctly and operational
- [ ] Belt tensions checked, sheaves aligned
- [ ] Bearing lubrication completed
- [ ] Electrical connections torqued to specification
- [ ] Safety devices tested (high/low pressure cutouts)

**Control Systems:**
- [ ] Sensor calibration verified against standards
- [ ] Control sequences programmed and logic verified
- [ ] Alarm setpoints configured
- [ ] Trending and data logging operational
- [ ] Remote monitoring connectivity established

**Structural:**
- [ ] Insulation complete, no thermal bridges
- [ ] Vapor barriers intact and sealed
- [ ] Floor drainage operational
- [ ] Door seals and hardware adjusted
- [ ] Lighting and electrical outlets functional

### Performance Verification

**Refrigeration System Tests:**

1. **Capacity Verification:**
   - Operate at design conditions (14°C storage, 30°C ambient)
   - Measure compressor power input
   - Calculate actual capacity vs. design
   - Acceptance: ±10% of design capacity

2. **Temperature Uniformity:**
   - Place 12 temperature sensors throughout space
   - Record temperatures every 5 minutes for 24 hours
   - Maximum deviation: <2°C from setpoint
   - No location below 13°C for more than 1 hour

3. **Humidity Control:**
   - Verify RH maintenance at 87.5% setpoint
   - Test humidifier response time (<30 minutes to setpoint)
   - Verify high-limit cutoff at 92% RH

**Documentation Requirements:**
- Equipment nameplate data
- Refrigerant charge quantity and type
- Control system programming (backup)
- Sensor calibration certificates
- Performance test results
- Operating and maintenance manuals

## Maintenance Schedule

### Daily Checks (Automated/Operator)

- Storage temperature and humidity readings
- Compressor operating hours and cycles
- Evaporator frost accumulation visual inspection
- Door operation and seal condition
- Unusual sounds or vibrations

### Weekly Maintenance

- Clean or replace air filters
- Check evaporator drain pan operation
- Inspect product for quality issues
- Verify control system operation
- Review alarm logs

### Monthly Maintenance

- Check refrigerant pressures and temperatures
- Inspect electrical connections for heat/corrosion
- Lubricate fan bearings if required
- Test defrost cycle completion
- Calibrate humidity sensors (quarterly minimum)

### Annual Maintenance

- Compressor oil analysis and potential change
- Refrigerant leak detection (electronic and bubble test)
- Electrical contact inspection and cleaning
- Control system programming backup
- Comprehensive system performance evaluation
- Replace worn belts, gaskets, seals preventatively

## Troubleshooting Guide

### Temperature Control Issues

**Problem: Storage temperature exceeds 16°C**

**Possible Causes:**
1. Inadequate refrigeration capacity
   - Verify compressor operation and capacity
   - Check for refrigerant undercharge (superheat >12 K)
   - Inspect condenser airflow and cleanliness

2. Excessive heat load
   - Check for air infiltration (door seals, structural gaps)
   - Verify insulation integrity (thermal imaging)
   - Measure actual product respiratory heat

3. Control system malfunction
   - Verify temperature sensor accuracy
   - Check EEV operation and superheat control
   - Review control logic and setpoints

**Problem: Temperature drops below 13°C causing chilling injury**

**Possible Causes:**
1. Control system overcooling
   - Increase proportional band or decrease gain
   - Add deadband to prevent short cycling
   - Implement minimum off-time (5-10 minutes)

2. Improper sensor location
   - Sensor in cold air stream from evaporator
   - Not measuring representative product temperature
   - Relocate to product mass center

### Humidity Control Issues

**Problem: RH drops below 85% causing shriveling**

**Possible Causes:**
1. Excessive dehumidification
   - Reduce evaporator fan speed
   - Increase coil TD (raise evaporating temperature)
   - Reduce defrost frequency

2. Air infiltration
   - Inspect and repair door seals
   - Check for structural air leaks
   - Install air curtain at frequently used doors

3. Insufficient humidification
   - Verify humidifier operation and output
   - Check water supply and quality
   - Clean or replace atomizer nozzles

**Problem: RH exceeds 92% causing surface mold**

**Possible Causes:**
1. Inadequate air circulation
   - Increase evaporator fan speed
   - Verify no blocked air pathways
   - Rearrange product bins for better airflow

2. Poor defrost control
   - Water accumulation in drain pan
   - Excessive moisture input during defrost
   - Ensure drain heaters operational

## Conclusion

Sweet potato storage requires specialized HVAC design integrating precise temperature control above chilling injury thresholds, high humidity maintenance, and initial curing phases. The two-phase approach of 30°C/85% RH curing for 4-7 days followed by 13-15°C/85-90% RH storage for 4-7 months demands sophisticated refrigeration systems with low temperature differential evaporators, capacity modulation, and integrated humidity control.

Proper system design accounts for respiratory heat loads, maintains temperature uniformity within ±1°C, and prevents both chilling injury from low temperatures and quality degradation from excessive temperatures. Energy-efficient operation through variable capacity compressors, ECM fans, and optimized control strategies reduces operating costs while maintaining product quality throughout extended storage periods.
