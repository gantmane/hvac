---
title: "Cream Preparation"
aliases: ["Cream Preparation"]
description: "Comprehensive technical guidance on HVAC and refrigeration systems for cream preparation in butter production, including pasteurization heat loads, cooling requirements, crystallization temperature control, and process room environmental management."
weight: 1
---

## Overview

Cream preparation represents the critical first stage in butter production, requiring precise thermal control across multiple process steps. The HVAC and refrigeration systems must manage substantial heat loads from pasteurization (95°C) while providing accurate cooling to churning temperature (8-14°C) and maintaining crystallization conditions. Process room environmental control ensures product quality and worker safety during these temperature-intensive operations.

## Cream Receiving and Storage

### Reception Temperature Control

Raw cream arrives at processing facilities at temperatures between 4-10°C depending on farm cooling systems and transport duration. Reception areas require refrigeration capacity to prevent temperature rise during off-loading and initial storage.

**Reception dock specifications:**
- Ambient temperature: 10-15°C
- Air changes: 15-20 ACH
- Relative humidity: 70-80%
- Positive pressure: 12-25 Pa to minimize contamination ingress

### Storage Tank Refrigeration

Cream storage tanks maintain product at 4-6°C prior to processing. Refrigeration load calculations must account for:

**Heat gain components:**

| Source | Load (W/m³) | Notes |
|--------|-------------|-------|
| Transmission through walls | 8-12 | Insulated tank assumption |
| Agitator motor heat | 15-25 | Continuous gentle mixing |
| Product heat of respiration | 2-4 | Bacterial activity |
| Ambient infiltration | 3-6 | Tank openings, sampling |
| **Total specific load** | **28-47** | **Per cubic meter of cream** |

For a 10,000 L storage tank, total refrigeration load:

Q_storage = V × ρ × q_specific

Where:
- V = 10 m³
- ρ = 1.01 (cream density relative to water)
- q_specific = 37.5 W/m³ (average)

Q_storage = 10 × 1.01 × 37.5 = 379 W ≈ 1,300 BTU/hr

### Storage Room Environmental Control

Storage areas housing multiple tanks require environmental management:

- Temperature: 4-8°C
- Humidity control: 75-85% RH to prevent condensation on cold surfaces
- Air distribution: Low-velocity diffusers (0.15-0.25 m/s) to minimize surface drying
- Refrigeration system: Direct expansion or glycol loop with 3-5 TD

## Pasteurization Heat Load

### High-Temperature Short-Time (HTST) Pasteurization

Cream undergoes HTST pasteurization at 95°C for 15-30 seconds to eliminate pathogenic bacteria and deactivate enzymes that cause off-flavors. This process generates significant heating and subsequent cooling loads.

**Heating requirements:**

Q_heat = ṁ × c_p × ΔT

For 5,000 kg/hr cream flow:
- ṁ = 5,000 kg/hr = 1.389 kg/s
- c_p = 3.35 kJ/(kg·K) for 35% fat cream
- ΔT = 95 - 5 = 90 K (from storage temp to pasteurization)

Q_heat = 1.389 × 3.35 × 90 = 419 kW = 1,430,000 BTU/hr

### Heat Recovery Systems

Regenerative heat exchangers recover 85-95% of pasteurization heat, pre-warming incoming cold cream with outgoing hot pasteurized cream. This reduces net heating and cooling loads dramatically.

**With 90% regeneration efficiency:**

Net heating load = 419 kW × (1 - 0.90) = 41.9 kW

Net cooling load (to remove heat after regeneration):

Q_cool_regenerated = 419 kW × 0.90 = 377 kW

This regenerated heat must still be removed but enters the cooling section at higher temperature, improving refrigeration system efficiency.

### Pasteurizer Room HVAC

Pasteurization equipment generates substantial radiant and convective heat that elevates room temperature:

**Room heat load components:**

| Source | Heat gain (kW) | Calculation basis |
|--------|----------------|-------------------|
| Equipment radiation | 12-18 | 3-4% of process heat |
| Motor heat (pumps) | 8-12 | 15 kW motor @ 80% efficiency |
| Hot water system losses | 5-8 | Piping, valves, connections |
| Lighting | 3-5 | LED fixtures, 10 W/m² |
| Personnel | 4-6 | 4 operators @ 120 W sensible each |
| Ventilation load | 15-25 | Makeup air conditioning |
| **Total room load** | **47-74** | **Average 60 kW** |

Room design conditions:
- Temperature setpoint: 18-22°C
- Humidity: 50-60% RH
- Air changes: 12-15 ACH (heat and steam removal)
- Exhaust: Local capture hoods over steam sources

## Cooling to Churning Temperature

### Primary Cooling Stage

After pasteurization, cream requires rapid cooling to arrest bacterial growth and prepare for temperature-controlled aging. Target temperature: 8-14°C depending on butter type and season.

**Cooling load calculation:**

Q_cool_primary = ṁ × c_p × ΔT

For 5,000 kg/hr production rate:
- ṁ = 1.389 kg/s
- c_p = 3.35 kJ/(kg·K)
- ΔT = 95 - 11°C = 84 K (to average churning prep temp)

Q_cool_primary = 1.389 × 3.35 × 84 = 391 kW = 1,333,000 BTU/hr

With regenerative heat exchange removing 90% of sensible heat:

Net cooling load = 391 kW × 0.10 = 39.1 kW = 133,400 BTU/hr

### Cooling System Configuration

Plate heat exchangers (PHE) provide efficient heat transfer for cream cooling:

**PHE specifications:**

| Parameter | Value | Notes |
|-----------|-------|-------|
| Heat transfer area | 45-65 m² | For 400 kW duty |
| Overall U-value | 2,800-3,200 W/(m²·K) | Cream to glycol/ammonia |
| Approach temperature | 2-3°C | Temperature difference at cold end |
| Pressure drop (cream side) | 50-80 kPa | Impacts pump sizing |
| Pressure drop (refrigerant side) | 30-50 kPa | Direct expansion systems |

**Heat exchanger effectiveness:**

ε = (T_in - T_out) / (T_in - T_refrigerant)

For cream cooling from 95°C to 11°C with -2°C glycol:

ε = (95 - 11) / (95 - (-2)) = 84 / 97 = 0.866 (86.6%)

This represents excellent heat exchanger performance for liquid-liquid applications.

### Refrigeration System Selection

**Option 1: Direct expansion ammonia**
- Evaporating temperature: -5°C to -8°C
- Suction superheat: 5-8 K
- Suitable for large installations (>200 kW)
- Requires skilled operators and safety systems

**Option 2: Glycol loop with central chiller**
- Glycol supply: -2°C to 0°C
- Return temperature: 6-8°C
- Glycol concentration: 30-35% propylene glycol
- Preferred for moderate capacity, simpler operation

**Chiller sizing for glycol system:**

Q_chiller = Q_cool_primary + Q_aging + Q_distribution_losses

Q_chiller = 39.1 + 15 + 5.9 = 60 kW = 17 tons refrigeration

### Cooling Rate Control

Cooling rate affects fat crystallization and butter texture. Controlled cooling prevents excessive crystal formation:

- Fast cooling (>10°C/min): Small crystals, firmer butter
- Slow cooling (<5°C/min): Large crystals, softer spreadable butter
- Modulating control: Variable-speed pumps adjust flow rates

## Aging and Ripening Temperature Control

### Physical Aging Process

After cooling, cream undergoes physical aging at 8-14°C for 2-15 hours to allow fat crystallization. Temperature precision directly impacts butter yield and texture characteristics.

**Aging vessel refrigeration load:**

| Component | Heat gain (W/m³) | Description |
|-----------|------------------|-------------|
| Transmission losses | 4-8 | Through insulated walls |
| Crystallization heat | 12-18 | Exothermic fat solidification |
| Agitator work input | 8-12 | Gentle slow-speed mixing |
| Ambient infiltration | 2-4 | Minimal in closed vessels |
| **Total specific load** | **26-42** | **Average 34 W/m³** |

For 20,000 L aging vessel:

Q_aging = 20 m³ × 34 W/m³ = 680 W ≈ 2,320 BTU/hr

### Temperature Stability Requirements

Fat crystallization requires temperature stability within ±0.5°C to produce consistent butter texture:

**Control strategies:**
1. Jacketed vessel cooling with PID temperature control
2. Glycol flow modulation via control valve
3. Temperature sensors: RTD Pt100 with ±0.1°C accuracy
4. Control loop: 30-60 second update rate

**Jacket heat transfer:**

Q = U × A × LMTD

Where:
- U = 300-400 W/(m²·K) for jacketed vessel with agitation
- A = Jacket surface area (m²)
- LMTD = Log mean temperature difference between glycol and cream

For a 20 m³ vessel (approximately 3.5 m³ jacket area):

Q = 350 × 3.5 × 4.5 = 5,513 W = 5.5 kW

This provides adequate capacity for the 680 W continuous load plus temperature pull-down capability.

### Cultured Butter Ripening

Cultured butter production adds biological aging with starter culture addition. Ripening occurs at 12-16°C for 12-20 hours to develop diacetyl (buttery flavor compound).

**Modified refrigeration requirements:**
- Higher setpoint reduces cooling load by 30-40%
- Tighter temperature control: ±0.3°C for optimal culture activity
- CO₂ production from culture requires headspace venting
- Room temperature control prevents condensation on vessel exteriors

## Crystallization Temperature Management

### Fat Crystal Formation Physics

Milk fat crystallizes in multiple polymorphic forms depending on cooling rate and temperature. The β' crystal form (intermediate melting point) provides optimal spreadability.

**Crystal development temperatures:**

| Temperature (°C) | Crystal type | Characteristics |
|------------------|--------------|-----------------|
| 4-8 | α (alpha) | Unstable, small crystals |
| 8-12 | β' (beta-prime) | Stable, optimal texture |
| 12-16 | β (beta) | Very stable, grainy texture |

Target temperature range: 8-12°C to maximize β' crystal formation.

### Crystallization Heat of Fusion

Fat crystallization releases latent heat that must be removed to maintain temperature:

Q_crystallization = m_fat × x_crystallized × L_f

Where:
- m_fat = Mass of milk fat in cream
- x_crystallized = Fraction crystallized (typically 0.25-0.35 at aging temp)
- L_f = Latent heat of fusion = 120-140 kJ/kg for milk fat

For 1,000 kg cream at 35% fat with 30% crystallization:

Q_crystallization = 1,000 × 0.35 × 0.30 × 130 = 13,650 kJ

Released over 8 hours aging period:

q_crystallization = 13,650 kJ / (8 × 3600 s) = 0.475 kW = 475 W

This represents a significant portion of the aging vessel cooling load and cannot be neglected in refrigeration system sizing.

### Temperature Cycling Strategy

Some butter manufacturers employ temperature cycling to optimize crystal structure:

**Cycle parameters:**
1. Initial cooling: 95°C → 5°C in 30 minutes
2. Warm-up: 5°C → 15°C over 2 hours
3. Hold: 15°C for 4 hours (partial melting)
4. Re-cool: 15°C → 10°C over 2 hours (controlled crystallization)
5. Final aging: 10°C for 8-12 hours

This strategy requires refrigeration systems with both heating and cooling capability, typically implemented with hot water and chilled glycol supplies to the same jacket.

## Heat Transfer Equipment Specifications

### Plate Heat Exchangers

Plate heat exchangers dominate cream processing due to high thermal efficiency and cleanability:

**Design parameters:**

| Specification | Value | Design notes |
|---------------|-------|--------------|
| Plate material | 316L stainless steel | Dairy-grade, corrosion resistant |
| Gasket material | EPDM or NBR | Temperature rating to 140°C |
| Plate pattern | Herringbone, 60° chevron | Turbulence generation |
| Plate spacing | 3-5 mm | Viscous product accommodation |
| Connection size | DN50-DN100 | Flow rate dependent |
| Design pressure | 10 bar (145 psi) | Product and cleaning sides |
| CIP compatibility | Full counterflow capability | 80°C caustic, 70°C acid |

**Heat transfer correlation for PHE:**

Nu = 0.724 × Re^0.583 × Pr^0.33 × (μ/μ_wall)^0.14

Where:
- Nu = Nusselt number = h × D_h / k
- Re = Reynolds number = ρ × v × D_h / μ
- Pr = Prandtl number = c_p × μ / k
- D_h = Hydraulic diameter (2× plate spacing)

For cream at 50°C in a PHE with 4 mm spacing at 0.3 m/s velocity:
- Re = 1,010 × 0.3 × 0.004 / 0.012 = 101 (laminar flow)
- Pr = 3,350 × 0.012 / 0.52 = 77.3
- Nu = 0.724 × 101^0.583 × 77.3^0.33 × 1.0 = 58.9

Heat transfer coefficient:
h = Nu × k / D_h = 58.9 × 0.52 / 0.004 = 7,657 W/(m²·K)

### Scraped Surface Heat Exchangers

For high-fat cream (>45%) or cultured cream with increased viscosity, scraped surface heat exchangers prevent fouling:

**SSHE specifications:**
- Rotating blade speed: 200-400 rpm
- Clearance: 0.5-1.5 mm from wall
- Heat transfer coefficient: 1,500-3,000 W/(m²·K)
- Power consumption: 8-15 kW per m² of surface
- Applications: Viscous products, crystallization control

## Process Room HVAC Design

### Environmental Control Requirements

Cream preparation rooms demand precise environmental control for product quality, equipment performance, and worker comfort:

**Design conditions:**

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Dry bulb temperature | 16-20°C | Equipment heat dissipation, worker comfort |
| Relative humidity | 60-70% | Prevent condensation, minimize drying |
| Air changes per hour | 15-20 | Heat and moisture removal |
| Pressurization | +15 Pa | Contamination prevention |
| Supply air filtration | MERV 13-14 | Particulate control |
| Temperature uniformity | ±1.5°C | Consistent conditions throughout space |

### Sensible and Latent Load Calculation

**Sensible heat sources:**

| Source | Load (kW) | Calculation method |
|--------|-----------|-------------------|
| Equipment radiation | 18-25 | 3-5% of process heat |
| Motor heat | 12-18 | Pump and agitator motors |
| Lighting | 4-6 | LED, 8-10 W/m² |
| Personnel | 5-8 | 10 workers @ 120 W sensible each |
| Transmission | 8-12 | Through walls, ceiling, floor |
| Solar gain | 2-4 | Minimal with proper insulation |
| Infiltration sensible | 6-10 | Door openings, building leakage |
| **Total sensible** | **55-83** | **Average 69 kW** |

**Latent heat sources:**

| Source | Load (kW) | Moisture source |
|--------|-----------|-----------------|
| Personnel | 6-9 | 10 workers @ 75 W latent each |
| Process evaporation | 8-15 | Open vessels, cleaning operations |
| Infiltration latent | 4-8 | Humid outdoor air ingress |
| **Total latent** | **18-32** | **Average 25 kW** |

**Total cooling load:**

Q_total = Q_sensible + Q_latent = 69 + 25 = 94 kW = 26.7 tons

**Sensible heat ratio (SHR):**

SHR = Q_sensible / Q_total = 69 / 94 = 0.73

This moderate SHR indicates both sensible cooling and dehumidification are required.

### Air Distribution System Design

**Supply air calculations:**

Sensible cooling airflow:

ṁ_air = Q_sensible / (c_p × ΔT) = 69,000 / (1.006 × 8) = 8,580 kg/hr = 7,250 m³/hr

For ΔT = 8°C supply air temperature differential.

**Air changes verification:**

For a 500 m² room with 4 m height (2,000 m³ volume):

ACH = 7,250 / 2,000 = 3.6 air changes per hour

This is insufficient. Increase to 15 ACH for adequate heat removal:

Required airflow = 2,000 × 15 = 30,000 m³/hr

This higher airflow provides:
- Superior heat removal from localized hot spots
- Faster temperature recovery after door openings
- Better air quality through increased ventilation

### Ductwork and Diffuser Layout

**Supply air distribution:**
- Low-velocity ceiling diffusers: 4-way throw, 0.2-0.3 m/s terminal velocity
- Spacing: 3-4 m centers
- Throw distance: 70% of spacing distance
- Supply temperature: 10-12°C (avoid excessive ΔT causing condensation)

**Return/exhaust air:**
- High-level return grilles above heat-generating equipment
- Low-level returns for floor cleaning water vapor pickup
- 60% high-level, 40% low-level split
- Exhaust fans with VFD control to maintain room pressure

## Energy Efficiency Strategies

### Heat Recovery Implementation

**Regenerative heat exchange:**

The single most effective energy conservation measure captures 85-95% of pasteurization heat:

Annual energy savings calculation:

E_saved = Q_heat × η_recovery × t_operation

For 5,000 kg/hr production, 6,000 hours/year operation:
- Q_heat = 419 kW (calculated earlier)
- η_recovery = 0.90
- t_operation = 6,000 hrs/yr

E_saved = 419 × 0.90 × 6,000 = 2.26 million kWh/yr

At $0.08/kWh electricity cost:

Cost savings = $181,000/year

**Payback analysis:**

Regenerative PHE capital cost: $85,000-$120,000

Simple payback = $100,000 / $181,000 = 0.55 years (6-7 months)

This represents exceptional return on investment.

### Variable Speed Drive Applications

VFD implementation on refrigeration system compressors and pumps:

**Energy savings mechanisms:**
1. Compressor capacity modulation eliminates hot gas bypass losses
2. Pump flow matching to actual process demand reduces throttling losses
3. Fan speed reduction follows the cubic power relationship (50% speed = 12.5% power)

**Typical savings:**
- Refrigeration compressors: 15-25% annual energy
- Glycol circulation pumps: 20-35% annual energy
- HVAC fans: 30-45% annual energy

### Evaporative Cooling for Condenser Heat Rejection

In dry climates, evaporative condensers or cooling towers provide superior efficiency compared to air-cooled condensers:

**Comparison for 100 kW refrigeration system:**

| System type | Condensing temp | COP | Power (kW) | Annual energy (kWh) |
|-------------|----------------|-----|------------|---------------------|
| Air-cooled | 45°C | 2.8 | 35.7 | 214,200 |
| Evaporative | 32°C | 3.9 | 25.6 | 153,600 |
| **Savings** | **-13°C** | **+39%** | **-10.1** | **60,600 kWh/yr** |

At $0.08/kWh: $4,850 annual savings

Water consumption: 60,600 kWh × 3 L/kWh = 182 m³/yr at $3/m³ = $545/yr

Net annual savings: $4,850 - $545 = $4,305/year

### Insulation Optimization

Proper insulation on cold cream piping, storage vessels, and aging tanks prevents heat gain and condensation:

**Economic insulation thickness:**

The optimal thickness balances insulation cost against energy savings. For -2°C glycol piping in 20°C ambient:

| Thickness (mm) | Heat loss (W/m) | Annual energy cost | Insulation cost ($/m) | Total 10-yr cost |
|----------------|-----------------|--------------------|-----------------------|------------------|
| 25 | 18.5 | $12.60 | $15 | $141 |
| 50 | 10.8 | $7.35 | $24 | $97.50 |
| 75 | 7.9 | $5.38 | $35 | $88.80 |
| 100 | 6.2 | $4.22 | $48 | $90.20 |

Optimal thickness: 75 mm (minimum total cost over lifecycle)

Standard specification: 50-75 mm closed-cell elastomeric foam for -10°C to +10°C service.

## Control System Integration

### Temperature Control Architecture

Multi-stage cream processing requires coordinated temperature control across all process steps:

**Control hierarchy:**
1. Plant supervisory control (SCADA)
2. Process line controller (PLC)
3. Local loop controllers (dedicated temperature controllers)

**Critical control loops:**
- Pasteurization temperature: PID control with steam valve modulation
- Cooling water temperature: Cascade control with chiller capacity staging
- Aging vessel temperature: PID control with glycol valve positioning
- Room temperature: VAV control with heating/cooling sequencing

### Sensor Specifications

| Measurement | Sensor type | Accuracy | Location |
|-------------|-------------|----------|----------|
| Pasteurization temp | RTD Pt100 | ±0.1°C | Holding tube outlet |
| Cooling temp | RTD Pt100 | ±0.2°C | PHE cream outlet |
| Aging vessel temp | RTD Pt100 | ±0.1°C | Immersion in product |
| Glycol supply temp | RTD Pt100 | ±0.3°C | Main header |
| Room air temp | Thermistor | ±0.5°C | Return air plenum |
| Humidity | Capacitive RH | ±3% RH | Room return air |

### Alarm and Safety Systems

**Critical alarms:**
- Pasteurization temperature low: Product safety risk
- Cooling system failure: Product quality degradation
- Aging temperature deviation: Off-specification butter texture
- Room temperature high: Equipment overheating risk
- Refrigerant leak detection: Safety and environmental protection

**Response protocols:**
- Automatic process shutdown on pasteurization temperature deviation >1°C
- Diversion valve activation to waste tank for under-pasteurized product
- Backup glycol chiller auto-start on primary unit failure
- Operator notification via text/email for non-critical alarms

## Maintenance and Cleaning Requirements

### CIP (Clean-in-Place) System Integration

All cream contact surfaces require daily cleaning. CIP systems circulate hot caustic (80°C) and acid (70°C) solutions through process equipment:

**CIP thermal impact on refrigeration:**

During caustic circulation, equipment heats to 80°C. Post-cleaning, rapid cool-down to process temperature (10°C) creates significant refrigeration demand:

Q_cooldown = m_equipment × c_p_steel × ΔT + m_residual × c_p_water × ΔT

For a plate heat exchanger (300 kg stainless steel, 50 L water residual):

Q_cooldown = 300 × 0.5 × 70 + 50 × 4.18 × 70 = 10,500 + 14,630 = 25,130 kJ

Over 30-minute cooldown period:

q_cooldown = 25,130 kJ / 1,800 s = 14 kW

**Refrigeration system sizing consideration:**

CIP cooldown loads occur simultaneously across multiple equipment items during shift changes. Size refrigeration systems for:

Q_refrigeration = Q_process_maximum + 0.6 × Q_CIP_total

The 0.6 diversity factor accounts for staggered cleaning schedules.

### Preventive Maintenance Schedule

| Equipment | Task | Frequency | Impact on refrigeration |
|-----------|------|-----------|-------------------------|
| Plate heat exchangers | Gasket inspection | Monthly | Leakage reduces efficiency |
| Refrigeration compressors | Oil analysis | Quarterly | Wear indicates loss of capacity |
| Glycol concentration | Testing | Quarterly | Low concentration = poor heat transfer |
| Insulation condition | Visual inspection | Quarterly | Damage increases heat gain |
| Control valve calibration | Testing | Semi-annually | Poor control = energy waste |

## Summary

Cream preparation for butter production requires sophisticated thermal management across pasteurization (95°C), cooling (8-14°C), and crystallization temperature control. Key HVAC considerations:

1. **Heat recovery**: 85-95% regenerative heat exchange provides 6-7 month payback
2. **Refrigeration capacity**: Size for process loads plus CIP cooldown demands
3. **Temperature precision**: ±0.5°C control for consistent fat crystallization
4. **Process room HVAC**: 15-20 ACH with 60-70% RH maintains equipment performance
5. **Energy efficiency**: VFD controls, evaporative cooling, and optimized insulation reduce operating costs by 25-40%

Proper integration of refrigeration and HVAC systems ensures production efficiency, product quality, and energy performance in cream preparation operations.

