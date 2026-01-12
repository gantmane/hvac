---
title: "Clarification and Separation"
description: "HVAC design for milk clarification and cream separation operations including centrifugal separator heat loads, temperature control requirements, and process room environmental conditions"
weight: 2
---

## Process Overview

Clarification and separation represent critical thermal-mechanical operations in dairy processing where centrifugal force removes sediment and separates cream from milk. These processes generate substantial heat loads while requiring precise temperature control for optimal separation efficiency and product quality.

### Primary Operations

**Clarification**: Removes solid impurities, somatic cells, and bacteria through centrifugal force (5,000-10,000 × g). The process operates continuously at 32-38°C to maintain optimal milk viscosity for sediment removal.

**Separation**: Divides whole milk into cream (35-45% fat) and skim milk (0.05-0.10% fat) using density differential under centrifugal force (6,000-9,000 × g). Temperature control directly affects fat globule stability and separation efficiency.

**Standardization**: Blends cream and skim milk to achieve target fat content products ranging from skim milk (0.1% fat) to whole milk (3.25% fat) to cream (18-40% fat).

## Centrifugal Separation Principles

### Physical Principles

The separation process exploits density differences between milk plasma (ρ ≈ 1.036 g/cm³) and fat globules (ρ ≈ 0.93 g/cm³).

**Stokes' Law Application**:

```
v = (2r²g(ρ_p - ρ_f)) / (9η)
```

Where:
- v = settling velocity (m/s)
- r = particle radius (m)
- g = gravitational acceleration or centrifugal force (m/s²)
- ρ_p = plasma density (kg/m³)
- ρ_f = fat globule density (kg/m³)
- η = dynamic viscosity (Pa·s)

**Centrifugal Force**:

```
F_c = m × ω² × r = m × (2πN/60)² × r
```

Where:
- F_c = centrifugal force (N)
- m = particle mass (kg)
- ω = angular velocity (rad/s)
- N = rotational speed (rpm)
- r = radius from rotation axis (m)

### Temperature-Viscosity Relationship

Milk viscosity significantly affects separation efficiency:

| Temperature (°C) | Dynamic Viscosity (mPa·s) | Relative Separation Efficiency |
|------------------|---------------------------|--------------------------------|
| 25 | 2.10 | 75% |
| 30 | 1.85 | 88% |
| 35 | 1.65 | 100% |
| 40 | 1.50 | 105% |
| 45 | 1.38 | 108% |
| 50 | 1.28 | 110% |

**Viscosity Temperature Relationship**:

```
η(T) = η_0 × e^(E_a/R × (1/T - 1/T_0))
```

Where:
- η(T) = viscosity at temperature T
- η_0 = reference viscosity
- E_a = activation energy (≈ 15 kJ/mol for milk)
- R = gas constant (8.314 J/mol·K)
- T = absolute temperature (K)

## Separator Equipment Specifications

### High-Speed Centrifugal Separators

Modern hermetic separators operate under specific thermal and mechanical conditions:

| Parameter | Clarifier | Separator | Combination Unit |
|-----------|-----------|-----------|------------------|
| Bowl speed | 6,000-8,000 rpm | 7,000-9,500 rpm | 6,500-9,000 rpm |
| Centrifugal force | 5,000-8,000 × g | 6,000-9,000 × g | 5,500-8,500 × g |
| Capacity | 10,000-40,000 L/hr | 15,000-50,000 L/hr | 12,000-45,000 L/hr |
| Motor power | 15-55 kW | 22-75 kW | 18-65 kW |
| Operating temperature | 32-38°C | 35-40°C | 32-38°C |
| Heat generation | 12-48 kW | 18-65 kW | 15-55 kW |

### Equipment Heat Loads

**Total Heat Generation**:

```
Q_total = Q_mechanical + Q_friction + Q_milk
```

Where:
- Q_mechanical = motor inefficiency losses
- Q_friction = bearing and seal friction
- Q_milk = milk temperature rise from friction

**Mechanical Heat Load**:

```
Q_mech = P_motor × (1 - η_motor) / η_motor
```

For a typical 45 kW separator with 92% motor efficiency:

```
Q_mech = 45 kW × (1 - 0.92) / 0.92 = 3.91 kW
```

**Friction Heat Load**:

```
Q_friction = 0.25 × P_motor
```

For 45 kW separator:

```
Q_friction = 0.25 × 45 kW = 11.25 kW
```

**Milk Temperature Rise**:

```
ΔT_milk = Q_absorbed / (ṁ × c_p)
```

Where:
- ΔT_milk = temperature rise (°C)
- Q_absorbed = heat absorbed by milk (kW)
- ṁ = milk mass flow rate (kg/s)
- c_p = specific heat of milk (3.93 kJ/kg·K)

For 30,000 L/hr (8.61 kg/s) with 8 kW absorbed:

```
ΔT_milk = 8 kW / (8.61 kg/s × 3.93 kJ/kg·K) = 0.24°C
```

### Separator Room Heat Load Summary

**Total heat load for typical separation room** (4 separators, 45 kW each):

| Heat Source | Load per Unit (kW) | Quantity | Total Load (kW) |
|-------------|-------------------|----------|-----------------|
| Motor losses | 3.9 | 4 | 15.6 |
| Friction heat | 11.3 | 4 | 45.2 |
| Bearing heat | 2.5 | 4 | 10.0 |
| Milk warming | 8.0 | 4 | 32.0 |
| Lighting (LED) | 15 W/m² | 200 m² | 3.0 |
| Personnel | 130 W/person | 4 | 0.52 |
| **Total** | | | **106.3 kW** |

## Temperature Requirements for Separation

### Optimal Temperature Ranges

Process temperatures balance separation efficiency, microbial control, and energy consumption:

| Product Stream | Temperature Range (°C) | Target Temperature (°C) | Critical Control Point |
|----------------|------------------------|-------------------------|------------------------|
| Raw milk inlet | 4-6 | 5 | Yes - microbial growth |
| Preheated milk | 32-38 | 35 | Yes - separation efficiency |
| Separator discharge | 36-42 | 38 | No - expected rise |
| Cream discharge | 35-40 | 37 | Yes - fat stability |
| Skim milk discharge | 36-42 | 38 | No - cooling follows |
| Post-separation cooling | 2-4 | 3 | Yes - microbial control |

### Temperature Control Strategies

**Preheating System**:

```
Q_preheat = ṁ × c_p × (T_sep - T_storage)
```

For 30,000 L/hr (31,050 kg/hr) heating from 5°C to 35°C:

```
Q_preheat = 31,050 kg/hr × 3.93 kJ/kg·K × (35 - 5)K
         = 3,663,435 kJ/hr = 1,018 kW
```

**Regenerative Heat Exchange**:

Modern installations use plate heat exchangers with 90-95% thermal efficiency:

```
Q_recovered = ṁ × c_p × (T_hot - T_cold) × η_HX
```

For 95% efficiency:

```
Q_recovered = 31,050 kg/hr × 3.93 kJ/kg·K × 30K × 0.95
            = 3,480,263 kJ/hr = 967 kW
```

Net heating required: 1,018 - 967 = 51 kW

## Cream and Skim Milk Handling

### Product Stream Characteristics

| Property | Whole Milk | Cream (40%) | Skim Milk |
|----------|------------|-------------|-----------|
| Fat content | 3.5% | 40.0% | 0.05% |
| Density (kg/m³) | 1,032 | 994 | 1,036 |
| Specific heat (kJ/kg·K) | 3.93 | 3.35 | 3.98 |
| Viscosity at 35°C (mPa·s) | 1.65 | 8.5 | 1.55 |
| Thermal conductivity (W/m·K) | 0.58 | 0.42 | 0.60 |

### Cream Cooling Requirements

Cream requires rapid cooling to prevent fat destabilization and microbial growth:

**Cooling Load Calculation**:

```
Q_cream = ṁ_cream × c_p,cream × (T_sep - T_storage)
```

For 3,000 L/hr cream (2,982 kg/hr) cooling from 37°C to 4°C:

```
Q_cream = 2,982 kg/hr × 3.35 kJ/kg·K × (37 - 4)K
        = 329,663 kJ/hr = 91.6 kW
```

### Skim Milk Cooling Requirements

Skim milk volume is substantially larger than cream:

**Cooling Load Calculation**:

```
Q_skim = ṁ_skim × c_p,skim × (T_sep - T_storage)
```

For 27,000 L/hr skim milk (27,972 kg/hr) cooling from 38°C to 4°C:

```
Q_skim = 27,972 kg/hr × 3.98 kJ/kg·K × (38 - 4)K
       = 3,783,470 kJ/hr = 1,051 kW
```

### Buffer Tank Requirements

**Temperature Stratification Prevention**:

Tank agitation prevents temperature gradients:

| Tank Volume (L) | Agitator Power (kW) | Heat Generation (kW) | Mixing Time (min) |
|-----------------|---------------------|----------------------|-------------------|
| 5,000 | 2.2 | 1.8 | 8-12 |
| 10,000 | 3.7 | 3.1 | 10-15 |
| 20,000 | 5.5 | 4.6 | 12-18 |
| 30,000 | 7.5 | 6.3 | 15-20 |

## Clean-in-Place (CIP) Temperature Requirements

### CIP Cycle Specifications

| CIP Stage | Temperature (°C) | Duration (min) | Flow Rate (L/min) | Heat Load (kW) |
|-----------|------------------|----------------|-------------------|----------------|
| Pre-rinse | 40-50 | 5-10 | 200-300 | 35-50 |
| Alkaline wash | 75-85 | 15-25 | 200-300 | 140-180 |
| Intermediate rinse | 50-60 | 5-10 | 200-300 | 45-60 |
| Acid wash | 65-75 | 10-15 | 200-300 | 95-120 |
| Final rinse | 20-25 | 5-10 | 200-300 | 0 (ambient) |

### CIP Heat Load Calculation

**Alkaline Wash Heating**:

```
Q_CIP = (V_tank × ρ × c_p × ΔT) / t_heat + Q_losses
```

For 1,500 L tank heated from 20°C to 80°C in 20 minutes:

```
Q_CIP = (1,500 L × 1.02 kg/L × 4.18 kJ/kg·K × 60K) / (20 min × 60 s/min) + 5 kW
      = 318 kW + 5 kW = 323 kW peak demand
```

Continuous heating during circulation:

```
Q_maintain = ṁ_CIP × c_p × ΔT_target + Q_losses
```

For 250 L/min (4.25 kg/s) maintaining 80°C with 8 kW losses:

```
Q_maintain = 4.25 kg/s × 4.18 kJ/kg·K × 60K + 8 kW
           = 1,066 kW + 8 kW = 1,074 kW
```

**Note**: Heat recovery from hot rinse water can reduce loads by 40-60%.

### CIP Room Environmental Impact

During CIP operations, process rooms experience:

- Steam release from open vents: 15-30 kg/hr
- Elevated ambient temperature: +5-8°C
- Increased humidity: +15-25% RH
- Chemical vapor release (NaOH, HNO₃ trace amounts)

## Process Room HVAC Design

### Environmental Specifications

| Parameter | Requirement | Critical Control |
|-----------|-------------|------------------|
| Temperature | 10-15°C | Yes - product safety |
| Relative humidity | 50-60% | Yes - condensation control |
| Air changes | 15-25 ACH | Yes - heat removal |
| Pressurization | +15 to +25 Pa | Yes - contamination control |
| Air velocity (occupied) | 0.15-0.30 m/s | No - comfort |
| Filtration | MERV 13 minimum | Yes - airborne contamination |

### Cooling Load Components

**Total Cooling Load**:

```
Q_total = Q_equipment + Q_lights + Q_people + Q_envelope + Q_ventilation + Q_safety
```

**Equipment Heat Load**: 106.3 kW (from separator analysis)

**Lighting Load**:

```
Q_lights = A_floor × W_lighting × BF
```

For 200 m² with 15 W/m² LED lighting (BF = 1.0):

```
Q_lights = 200 m² × 15 W/m² × 1.0 = 3.0 kW
```

**Occupancy Load**:

```
Q_people = N × (Q_sensible + Q_latent)
```

For 4 people in cool environment (moderate activity):

```
Q_people = 4 × (100 W + 30 W) = 0.52 kW
```

**Envelope Load**:

For insulated walls (U = 0.25 W/m²·K), 400 m² surface, ΔT = 20K:

```
Q_envelope = U × A × ΔT = 0.25 × 400 × 20 = 2.0 kW
```

**Ventilation Load**:

For 20 ACH, room volume 1,200 m³:

```
V̇ = ACH × V_room = 20 × 1,200 m³/hr = 24,000 m³/hr = 6.67 m³/s
```

Sensible load (ΔT = 20K):

```
Q_sensible = ρ × c_p × V̇ × ΔT = 1.2 kg/m³ × 1.005 kJ/kg·K × 6.67 m³/s × 20K
           = 160.8 kW
```

Latent load (Δω = 0.004 kg/kg, 25°C outdoor, 15°C indoor):

```
Q_latent = ρ × h_fg × V̇ × Δω = 1.2 × 2,465 kJ/kg × 6.67 × 0.004
         = 79.2 kW
```

**Safety Factor**: 10-15% for future equipment and peak conditions

```
Q_safety = Q_subtotal × 0.125
```

### Total Cooling Load Summary

| Component | Sensible (kW) | Latent (kW) | Total (kW) |
|-----------|---------------|-------------|------------|
| Separators | 106.3 | 0 | 106.3 |
| Lighting | 3.0 | 0 | 3.0 |
| Occupancy | 0.40 | 0.12 | 0.52 |
| Envelope | 2.0 | 0 | 2.0 |
| Ventilation | 160.8 | 79.2 | 240.0 |
| **Subtotal** | **272.5** | **79.3** | **351.8** |
| Safety factor (12.5%) | 34.1 | 9.9 | 44.0 |
| **Total Design Load** | **306.6** | **89.2** | **395.8 kW** |

### Air Distribution Design

**Supply Air Calculation**:

```
ṁ_supply = Q_sensible / (c_p × ΔT_supply)
```

For ΔT = 8K:

```
ṁ_supply = 306.6 kW / (1.005 kJ/kg·K × 8K) = 38.2 kg/s
```

Volume flow rate:

```
V̇_supply = ṁ_supply / ρ = 38.2 kg/s / 1.2 kg/m³ = 31.8 m³/s = 114,480 m³/hr
```

**Air Changes per Hour**:

```
ACH = V̇_supply / V_room = 114,480 m³/hr / 1,200 m³ = 95.4 ACH
```

This high ACH is typical for high-heat-load process rooms.

### Ductwork Design Considerations

**Supply Air Distribution**:

- High-induction diffusers mounted 4.0-5.0 m above floor
- Discharge velocity: 4-6 m/s at diffuser face
- Throw distance: 8-12 m to reach equipment zones
- Pattern: Perimeter supply with central returns above equipment

**Return Air Design**:

- Low-velocity returns (2.5-3.5 m/s) to minimize noise
- Located above heat sources (separators)
- Minimum 2.5 m above floor to avoid product contamination
- Return grilles with removable/washable filters

**Duct Velocities**:

| Duct Type | Velocity (m/s) | Pressure Drop (Pa/m) |
|-----------|----------------|----------------------|
| Main supply | 8-12 | 0.8-1.2 |
| Branch supply | 5-8 | 0.6-1.0 |
| Supply runouts | 4-6 | 0.8-1.2 |
| Return mains | 6-9 | 0.6-0.9 |
| Return branches | 4-6 | 0.5-0.8 |

## Refrigeration System Design

### Chilled Water System

For moderate cooling loads (200-600 kW), chilled water systems offer flexibility:

| Parameter | Specification |
|-----------|---------------|
| Supply temperature | 2-4°C |
| Return temperature | 10-12°C |
| Flow rate | 14.3 kg/s (51.5 m³/hr) |
| ΔT | 8K |
| Pump head | 250-350 kPa |
| Pipe velocity | 1.5-2.5 m/s |

**Chiller Capacity**:

```
Q_chiller = Q_cooling / COP = 395.8 kW / 3.2 = 123.7 kW compressor power
```

### Direct Expansion System

For smaller installations or backup systems:

| Component | Specification |
|-----------|---------------|
| Refrigerant | R-134a, R-404A, R-513A |
| Evaporator temperature | -2 to +2°C |
| Condensing temperature | 40-45°C |
| Superheat | 5-8K |
| Subcooling | 3-5K |
| COP | 2.8-3.5 (at design conditions) |

## Control Sequences

### Temperature Control Hierarchy

**Level 1 - Product Temperature**:
- Primary control: Preheat temperature to separator (35°C ± 1K)
- Secondary control: Post-separation cooling (4°C ± 0.5K)
- Response time: < 30 seconds

**Level 2 - Room Temperature**:
- Supply air temperature: 12°C ± 1K
- Room temperature: 15°C ± 2K
- Response time: 2-5 minutes

**Level 3 - Equipment Protection**:
- Separator bearing temperature: < 75°C alarm
- Motor winding temperature: < 120°C trip
- Response time: Immediate

### Automation Sequences

**Normal Operation**:

1. Milk preheating to 35°C via PHE
2. Separator startup and temperature stabilization (10-15 min)
3. Room HVAC modulates to maintain 15°C ± 2K
4. Product cooling via regenerative heat exchange
5. Final cooling to 4°C storage temperature

**CIP Mode**:

1. Room HVAC switches to high ventilation (30 ACH)
2. Exhaust fans activate for steam/chemical vapor removal
3. Supply air temperature increases to 18°C (reduced cooling)
4. Post-CIP purge: 30 minutes high ventilation
5. Return to normal operation setpoints

**Emergency Shutdown**:

1. Separators coast down (5-10 min)
2. Product diversion to waste if temperature > 10°C
3. Room cooling continues at 100% capacity
4. Ventilation maintains minimum 15 ACH
5. Alarm notification to operators

## Energy Efficiency Measures

### Heat Recovery Opportunities

| System | Recovery Potential (kW) | Capital Cost Factor | Payback (years) |
|--------|-------------------------|---------------------|-----------------|
| Separator bearing cooling | 40-60 | Medium | 2-4 |
| CIP hot water | 150-250 | High | 1-3 |
| Refrigeration condenser | 200-300 | High | 2-5 |
| Compressor cooling | 30-50 | Low | 3-6 |

### Variable Speed Drive Applications

**AHU Supply Fan**:

Energy savings from load variation:

```
P_fan = P_design × (V̇_actual / V̇_design)³
```

At 60% cooling load (60% airflow):

```
P_fan = 45 kW × 0.60³ = 9.72 kW (78% energy reduction)
```

**Cooling Water Pump**:

```
P_pump = P_design × (Q_actual / Q_design)³
```

At 70% load:

```
P_pump = 15 kW × 0.70³ = 5.15 kW (66% reduction)
```

## Commissioning and Validation

### Functional Performance Tests

| Test Parameter | Acceptance Criteria | Test Method |
|----------------|---------------------|-------------|
| Room temperature | 15°C ± 2K at all locations | 24-hour monitoring, 16 points |
| Temperature uniformity | < 2K variation | Simultaneous measurement grid |
| Separator discharge temp | 37-39°C continuous | Inline RTD, 1-minute logging |
| Product cooling rate | 35°C to 4°C in < 20 min | Time-temperature profile |
| Room pressurization | +20 Pa ± 5 Pa | Differential pressure gauge |
| Air changes | 95 ± 5 ACH | Tracer gas decay method |
| CIP temperature | 80°C ± 2K during alkaline wash | Inline RTD verification |

### Operational Qualification

**System capacity verification**:

1. Full production load test (8-hour run)
2. Peak summer condition simulation
3. CIP cycle during production (worst case)
4. Emergency shutdown and recovery
5. Instrument calibration verification

**Energy performance verification**:

- kW/ton refrigeration efficiency
- Fan energy per CFM delivered
- Overall process energy intensity (kWh/L milk processed)
- Heat recovery system effectiveness

## Maintenance Requirements

### HVAC System Maintenance

| Component | Frequency | Critical Tasks |
|-----------|-----------|----------------|
| AHU filters | Weekly inspection | Replace at 2× design pressure drop |
| Cooling coils | Monthly | Inspect fins, check ΔT, clean if needed |
| Refrigeration system | Quarterly | Refrigerant charge, oil analysis, leak check |
| VSD drives | Quarterly | Thermal scan, connection torque check |
| Control sensors | Semi-annually | Calibration verification against reference |
| Ductwork | Annually | Internal inspection, joint integrity |

### Separator System Coordination

HVAC maintenance must coordinate with separator maintenance:

- **Daily CIP**: 2-3 hours per separator, staggered schedule
- **Weekly inspection**: 30 minutes downtime, no HVAC impact
- **Monthly deep clean**: 4-6 hours, coordinate with HVAC CIP mode
- **Annual overhaul**: 2-5 days, reduce HVAC capacity accordingly

## Safety Considerations

### Personnel Safety

**Slip hazards**: Condensate from high-humidity CIP operations requires floor drains and anti-slip surfaces.

**Noise exposure**: Separators generate 80-90 dBA at 1 m distance. HVAC design must not add > 5 dBA to background noise.

**Chemical vapor exposure**: CIP operations release NaOH and HNO₃ vapors. Exhaust ventilation must maintain < 0.5 ppm exposure limits.

### Product Safety

**Temperature excursions**: Alarm setpoints at 38°C (preheat) and 6°C (storage) with 30-second delay.

**Cross-contamination**: Positive pressure prevents airborne contamination. Pressure loss alarm at +10 Pa.

**Power failure**: Emergency generator powers refrigeration and control systems within 10 seconds. UPS maintains separator coast-down control.

## Regulatory Compliance

### FDA Pasteurized Milk Ordinance (PMO)

- Room temperature during processing: < 10°C preferred, < 15°C maximum
- Product temperature limits: < 7°C for storage, > 72°C for pasteurization
- Cleaning validation: ATP testing < 250 RLU after CIP

### ASHRAE Standards

- **ASHRAE 15**: Refrigeration system safety, ventilation for machinery rooms
- **ASHRAE 55**: Thermal comfort for occupied spaces (control room, offices)
- **ASHRAE 62.1**: Ventilation rates for process areas (15-25 ACH typical)

### Energy Codes

- **ASHRAE 90.1**: Insulation requirements, equipment efficiency minimums
- **IECC**: Building envelope performance, lighting power density
- State-specific energy codes may impose additional requirements

---

**Design Summary**: Clarification and separation operations impose substantial HVAC loads (400+ kW cooling) due to high-speed centrifugal equipment. Precise temperature control (±1-2K) is essential for separation efficiency and product safety. Integration of heat recovery systems and variable-speed drives significantly reduces operating costs while maintaining process performance.
