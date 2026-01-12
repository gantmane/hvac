---
title: "Yogurt Manufacture"
description: "Comprehensive thermal control requirements for yogurt production including incubation temperature control, fermentation monitoring, post-fermentation cooling, and process room HVAC specifications"
weight: 1
---

## Manufacturing Process Overview

Yogurt production requires precise thermal control throughout multiple process stages. Temperature deviations of ±1°C during incubation can significantly affect fermentation kinetics, final pH, texture development, and product consistency.

The manufacturing sequence integrates heating operations (pasteurization), controlled fermentation (incubation), and rapid cooling systems. Each stage imposes specific HVAC loads and requires dedicated refrigeration capacity.

## Heat Treatment Requirements

### Pasteurization Parameters

High-temperature pasteurization destroys vegetative microorganisms, denatures whey proteins for improved gel structure, and reduces dissolved oxygen content.

**Standard Pasteurization Conditions:**

| Process Type | Temperature | Time | Purpose |
|--------------|-------------|------|---------|
| Low Temperature Long Time (LTLT) | 85°C | 30 min | Traditional batch processing |
| High Temperature Short Time (HTST) | 90-95°C | 5-10 min | Continuous processing |
| Ultra-High Temperature (UHT) | 135-140°C | 2-4 sec | Extended shelf life products |

Heat treatment affects yogurt texture through whey protein denaturation. β-lactoglobulin unfolds at temperatures above 70°C, exposing reactive sulfhydryl groups that interact with κ-casein to form a stronger protein network.

### Heating System Capacity

Heat requirement for pasteurization:

**Q = m × cp × ΔT + Q_losses**

Where:
- Q = heating load (kW)
- m = mass flow rate (kg/s)
- cp = specific heat of milk ≈ 3.93 kJ/(kg·K)
- ΔT = temperature rise (K)
- Q_losses = heat losses to environment (typically 5-10%)

For 10,000 L/hr milk flow from 4°C to 90°C:
- m = 10,000 kg/hr × 1.032 kg/L ÷ 3600 = 2.87 kg/s
- ΔT = 90 - 4 = 86 K
- Q = 2.87 × 3.93 × 86 = 970 kW
- With 8% losses: Q_total = 970 × 1.08 = 1,048 kW

## Cooling to Incubation Temperature

### Primary Cooling Stage

Following pasteurization, milk must be cooled rapidly to incubation temperature (42-45°C) to prevent thermal damage and prepare for culture inoculation.

**Cooling Load Calculation:**

For the same 10,000 L/hr flow cooled from 90°C to 43°C:
- ΔT = 90 - 43 = 47 K
- Q_cooling = 2.87 × 3.93 × 47 = 530 kW (152 TR)

### Cooling Equipment Options

| Equipment Type | Cooling Rate | Temperature Control | Application |
|----------------|--------------|---------------------|-------------|
| Plate heat exchanger | ±2-4°C/min | ±0.5°C | Most common, high efficiency |
| Tubular heat exchanger | ±1-2°C/min | ±1.0°C | High viscosity products |
| Scraped surface | ±3-5°C/min | ±0.3°C | Fruit-on-bottom yogurt |

Chilled water supply temperature: 2-4°C
Return water temperature: 8-12°C
Approach temperature: 2-3°C minimum

## Incubation Temperature Control

### Set Yogurt Process

Set yogurt ferments in final retail containers placed in temperature-controlled incubation rooms or cabinets.

**Critical Control Parameters:**

| Parameter | Specification | Tolerance | Impact of Deviation |
|-----------|--------------|-----------|---------------------|
| Temperature | 42-45°C | ±0.5°C | Fermentation rate, texture consistency |
| Relative humidity | 70-80% | ±5% | Container condensation prevention |
| Air velocity | 0.15-0.25 m/s | ±0.05 m/s | Temperature uniformity |
| Incubation time | 4-6 hours | ±15 min | pH endpoint control |

**Fermentation Kinetics:**

Acid production rate follows modified Gompertz equation:

**pH(t) = pH₀ - A × exp[-exp((μ_max × e / A) × (λ - t) + 1)]**

Where:
- pH₀ = initial pH (≈6.7)
- A = pH reduction amplitude (≈2.1 units)
- μ_max = maximum acidification rate (pH units/hr)
- λ = lag time (hr)
- t = time (hr)

At 43°C, typical μ_max = 0.4-0.6 pH units/hr
At 45°C, typical μ_max = 0.6-0.8 pH units/hr

Temperature increases of 2°C can reduce fermentation time by 25-35%.

### Stirred Yogurt Process

Stirred yogurt ferments in bulk tanks (5,000-50,000 L capacity) with integrated temperature control.

**Tank Design Requirements:**

- Jacketed vessel with cooling/heating capability
- Glycol or chilled water circulation
- Temperature sensors (minimum 3 locations):
  - Bottom third
  - Middle section
  - Top third
- Vertical temperature gradient: ≤0.5°C

**Heat Generation During Fermentation:**

Bacterial metabolism generates heat:

Q_fermentation = 1.5-2.5 W/m³ of milk

For 10,000 L tank:
- Heat output = 2.0 W/m³ × 10 m³ = 20 W (negligible)
- Primary heat gain from ambient conditions

### Incubation Room HVAC Design

**Heating Capacity:**

Room heat loss calculation:
- Wall/ceiling/floor transmission losses
- Infiltration losses through door openings
- Cold product thermal mass

For 200 m² incubation room (4 m height):
- Product thermal mass: 20,000 kg milk at 4°C heated to 43°C
- Q_product = 20,000 × 3.93 × (43-4) / 3600 = 849 kW·hr
- If heating over 2 hours: P_heating = 425 kW

**Temperature Control System:**

- Steam or hot water heating coils
- Circulation fans (0.5-0.8 air changes per minute)
- Modulating control valves
- Multiple zone control for large rooms
- Temperature uniformity: ±1°C throughout room

**Air Distribution:**

- Low velocity diffusers to prevent surface drying
- Perforated duct distribution
- Return air grilles at floor level
- Horizontal airflow patterns preferred

## Fermentation Monitoring

### pH Measurement

In-line pH monitoring for bulk fermentation:
- Glass electrode sensors
- Automatic temperature compensation
- Measurement range: pH 4.0-7.0
- Accuracy: ±0.05 pH units
- Response time: <30 seconds

Target endpoint pH: 4.4-4.6 (varies by product type)

**pH-Temperature Relationship:**

pH electrode readings are temperature-dependent:

pH_corrected = pH_measured + α(T - T_ref)

Where α = temperature coefficient (≈0.003 pH units/°C for milk)

### Titratable Acidity

Backup measurement method:
- Lactic acid concentration (% w/v)
- Typical endpoint: 0.8-1.0% lactic acid
- Measured by titration with 0.1 N NaOH

Relationship: 1% lactic acid ≈ pH 4.3-4.5

### Viscosity Development

For stirred yogurt, viscosity monitoring indicates gel strength:
- Brookfield viscometer measurements
- Target: 1,500-3,000 cP at 10°C
- Shear rate: 50-100 s⁻¹

## Post-Fermentation Cooling

### Cooling Requirement

Immediate cooling upon reaching target pH arrests fermentation and prevents over-acidification.

**Set Yogurt Cooling:**

Transfer to cold storage room:
- Room temperature: 2-4°C
- Cooling time to 10°C center temperature: 8-12 hours
- Container geometry affects cooling rate

Heat removal rate (Biot number analysis):

**Bi = h × L_c / k**

Where:
- h = convective heat transfer coefficient (W/(m²·K))
- L_c = characteristic length (volume/surface area) (m)
- k = thermal conductivity of yogurt ≈ 0.55 W/(m·K)

For 200 mL container (Bi < 0.1), lumped capacitance method applies:

**T(t) = T_∞ + (T₀ - T_∞) × exp(-t/τ)**

Where τ = ρ × V × cp / (h × A)

**Stirred Yogurt Cooling:**

Rapid cooling in plate heat exchanger:
- Initial temperature: 42-45°C
- Final temperature: 15-20°C (break gel strength)
- Cooling rate: 2-3°C/min
- Further cooling to 4-7°C after fruit addition

### Cooling System Capacity

For 10,000 L/hr stirred yogurt cooled from 43°C to 7°C:

Q_cooling = m × cp × ΔT
- m = 2.87 kg/s
- cp = 3.85 kJ/(kg·K) (fermented product)
- ΔT = 43 - 7 = 36 K
- Q = 2.87 × 3.85 × 36 = 398 kW (113 TR)

**Refrigeration Equipment:**

| System Component | Specification | Notes |
|------------------|---------------|-------|
| Compressor capacity | 450-500 kW | Includes safety factor |
| Evaporator temperature | -5 to -2°C | Glycol system |
| Glycol supply temperature | -2 to 0°C | Prevents freezing |
| Glycol return temperature | 4-6°C | Temperature rise in PHE |
| Glycol concentration | 25-30% propylene glycol | Food-grade required |

### Cooling Curve Specifications

**Critical Cooling Parameters:**

For set yogurt in cold room:

| Time (hours) | Center Temperature (°C) | Cooling Rate (°C/hr) |
|--------------|-------------------------|----------------------|
| 0 | 43 | - |
| 2 | 32 | 5.5 |
| 4 | 22 | 5.0 |
| 6 | 15 | 3.5 |
| 8 | 10 | 2.5 |
| 10 | 7 | 1.5 |
| 12 | 5 | 1.0 |

Maximum cooling rate: 6°C/hr (prevents excessive syneresis)

For stirred yogurt (continuous cooling):

**Stage 1:** 43°C → 20°C in 8-10 minutes
- Purpose: Break gel structure under controlled shear
- Cooling rate: ≈2.5°C/min

**Stage 2:** 20°C → 7°C in 5-7 minutes
- Purpose: Final product temperature
- Cooling rate: ≈2.0°C/min

## Set vs Stirred Yogurt Thermal Differences

### Comparison Table

| Aspect | Set Yogurt | Stirred Yogurt |
|--------|------------|----------------|
| Fermentation location | Retail containers | Bulk tanks (5,000-50,000 L) |
| Incubation method | Static room/cabinet | Jacketed tank with agitation |
| Temperature uniformity | ±1-2°C variation | ±0.3-0.5°C variation |
| Cooling method | Ambient air in cold room | Plate heat exchanger |
| Cooling time | 8-12 hours | 15-20 minutes |
| Post-fermentation handling | No mechanical agitation | Pumping, mixing with fruit |
| Gel structure | Undisturbed network | Broken then re-set |
| HVAC complexity | Cold room design critical | Process cooling capacity critical |

### Energy Consumption Comparison

**Set Yogurt (per 1000 kg product):**
- Incubation heating: 35-45 kWh
- Cold room cooling: 15-20 kWh (refrigeration)
- Cold room fan power: 2-3 kWh
- Total: 52-68 kWh per tonne

**Stirred Yogurt (per 1000 kg product):**
- Tank heating/maintaining: 25-30 kWh
- PHE cooling: 12-15 kWh (refrigeration)
- Pumping/mixing: 1-2 kWh
- Total: 38-47 kWh per tonne

Stirred yogurt systems typically 25-30% more energy efficient due to faster heat transfer in continuous cooling.

## Process Room HVAC Requirements

### Fermentation Room Specifications

**Environmental Conditions:**

| Parameter | Specification | Control Method |
|-----------|--------------|----------------|
| Air temperature | 42-45°C | Steam/hot water heating |
| Room temperature uniformity | ±0.5°C | Multi-point sensing, modulating control |
| Relative humidity | 70-80% | Humidification if needed |
| Air cleanliness | ISO Class 8 | HEPA filtration, positive pressure |
| Pressurization | +10-15 Pa | Supply > exhaust |
| Air changes | 5-8 ACH | Minimum for temperature control |
| Room recovery time | <30 min to setpoint | After door opening |

**Heating Load Components:**

1. **Transmission losses:** Q_trans = U × A × ΔT
   - U = 0.2-0.3 W/(m²·K) for insulated construction
   - A = total surface area (m²)
   - ΔT = (T_room - T_ambient)

2. **Infiltration losses:** Q_inf = ρ × V_inf × cp × ΔT
   - V_inf = infiltration rate (m³/s)
   - Depends on door opening frequency

3. **Product thermal mass:** Q_product (see earlier calculation)

4. **Equipment heat gain:** Minimal for set yogurt (lighting only)

### Cooling Room Specifications

Post-fermentation cold storage:

**Environmental Conditions:**

| Parameter | Specification |
|-----------|--------------|
| Air temperature | 2-4°C |
| Temperature uniformity | ±1°C |
| Relative humidity | 85-90% |
| Air velocity at product | <0.5 m/s |
| Air changes | 10-15 ACH |
| Defrost cycle | Automatic, 2-4 times daily |

**Refrigeration Load:**

1. **Product cooling load:** Major component (calculated previously)
2. **Transmission gain:** Through walls, ceiling, floor
3. **Infiltration load:** Door openings, personnel entry
4. **Equipment load:** Fans, lighting
5. **People load:** Warehouse activities

Total cooling capacity typically 1.5-2.0 times product cooling load to account for other gains and pull-down requirements.

### Processing Room HVAC

Packaging and handling areas:

**Temperature:** 10-15°C (reduces condensation, controls microbial growth)
**Relative humidity:** 60-70% (prevents mold, condensation)
**Pressure relationship:** Positive relative to external areas
**Air cleanliness:** ISO Class 8 or better
**HEPA filtration:** 99.97% at 0.3 μm

## Equipment Specifications

### Incubation Cabinets

For smaller operations (set yogurt):

**Capacity:** 500-2,000 cups per cabinet
**Temperature range:** 30-50°C
**Temperature uniformity:** ±0.3°C
**Control system:** PID controller with RTD sensors
**Heating method:** Electric heating elements or hot water coils
**Air circulation:** Internal fans, horizontal airflow
**Insulation:** 75-100 mm polyurethane foam
**Construction:** Stainless steel 304 interior/exterior

### Bulk Fermentation Tanks

For stirred yogurt production:

**Capacity range:** 5,000-50,000 liters
**Aspect ratio:** Height:diameter = 1.2-1.5:1
**Jacket design:**
- Dimple jacket or conventional jacket
- Glycol or chilled water circulation
- Heat transfer coefficient: 300-500 W/(m²·K)

**Agitation:**
- Slow-speed mixers (10-30 rpm) for culture blending
- No agitation during fermentation
- Gentle mixing after fermentation

**Temperature control:**
- Multiple RTD sensors (3-5 locations)
- Modulating valve control
- Heating and cooling capability
- Control accuracy: ±0.2°C

### Heat Exchangers

**Plate Heat Exchangers (PHE):**

Configuration for yogurt cooling:
- Product passages: 3-5 mm gap
- Chevron angle: 30-60° (lower for yogurt to reduce pressure drop)
- Material: 316L stainless steel
- Surface area: 0.3-0.5 m²/(tonne·hr)
- Pressure drop: <100 kPa on product side

**Tubular Heat Exchangers:**

Used for high-viscosity fruit yogurt:
- Tube diameter: 50-75 mm
- Double-tube or shell-and-tube design
- Lower heat transfer efficiency but reduced fouling
- Easier cleaning (CIP compatible)

## Quality Control Parameters

### Temperature Monitoring Requirements

**Critical Control Points (CCPs):**

1. **Pasteurization temperature:** Continuous recording
   - Legal requirement for FSMA compliance
   - Chart recorders or electronic data logging
   - Minimum 3-year record retention

2. **Incubation temperature:** Every 30 minutes
   - Multiple location monitoring
   - Alarm limits: ±1°C from setpoint

3. **Cooling temperature:** Continuous for stirred, periodic for set
   - Final product temperature verification
   - Center temperature measurement for set yogurt

### Product Quality Metrics

**Fermentation endpoint criteria:**

| Parameter | Target Range | Test Method |
|-----------|--------------|-------------|
| pH | 4.4-4.6 | pH meter, ±0.02 accuracy |
| Titratable acidity | 0.85-0.95% lactic acid | NaOH titration |
| Temperature | 42-45°C | RTD sensor |
| Fermentation time | 4-6 hours | Process timer |
| Syneresis | <2% whey separation | Centrifuge method |
| Viscosity (stirred) | 1,500-3,000 cP | Brookfield, Spindle 3, 50 rpm |

**Post-cooling verification:**

- Final product temperature: ≤7°C within specification time
- Cold chain maintenance: ≤4°C throughout storage/distribution
- Temperature abuse indicators on retail containers

## Safety and Sanitation Considerations

### Clean-in-Place (CIP) Systems

Process equipment requires thermal sanitization:

**CIP Temperature Requirements:**

| Phase | Temperature | Duration | Purpose |
|-------|-------------|----------|---------|
| Pre-rinse | 40-50°C | 5-10 min | Loose soil removal |
| Caustic wash | 75-85°C | 15-30 min | Protein/fat removal |
| Intermediate rinse | 40-50°C | 5-10 min | Caustic removal |
| Acid wash | 60-70°C | 10-20 min | Mineral scale removal |
| Final rinse | Ambient | 5-10 min | Neutralization |
| Sanitization | 85-95°C | 10-15 min | Thermal kill step |

**Heating capacity for CIP:**

For 10,000 L CIP solution heated from 20°C to 80°C:
- Q = 10,000 kg × 4.18 kJ/(kg·K) × 60 K = 2,508 MJ
- Power over 30 min: P = 2,508,000 / 1,800 = 1,393 kW

### Personnel Safety

Hot water and steam systems present burn hazards:
- Insulation on all hot surfaces >60°C
- Warning signage on incubation rooms
- Pressure relief valves on steam systems
- Emergency stops on all mechanical equipment

## Energy Efficiency Optimization

### Heat Recovery Opportunities

**Pasteurization-to-cooling regeneration:**

Plate heat exchanger with regeneration section:
- Hot pasteurized milk (90°C) preheats incoming cold milk (4°C)
- Regeneration efficiency: 70-85%
- Reduces heating load by 65-75%
- Reduces cooling load by 65-75%

Energy savings calculation:
- Without regeneration: 1,048 kW heating + 530 kW cooling = 1,578 kW total
- With 75% regeneration: 262 kW heating + 133 kW cooling = 395 kW total
- Savings: 75% reduction in thermal energy demand

**Refrigeration heat recovery:**

Compressor discharge heat (condenser duty) available at 40-50°C:
- Use for CIP water heating
- Use for building heating (winter)
- Typical heat recovery: 20-30% of compressor input power

### Control Strategies

**Variable speed drives (VSD):**
- Glycol circulation pumps
- Refrigeration compressors
- HVAC fans

Energy savings: 20-40% compared to constant speed operation

**Thermal storage:**

Ice bank or chilled water storage:
- Shift refrigeration load to off-peak hours
- Reduces demand charges
- Provides peak load capacity

**Process optimization:**

- Batch scheduling to minimize idle heating/cooling
- Temperature setback during non-production hours
- Optimized incubation times (pH-based endpoints vs. time-based)
