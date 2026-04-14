---
title: "Apple Juice Processing"
aliases: ["Apple Juice Processing"]
description: "Refrigeration system design for apple juice production including pressing room conditions, pasteurization cooling, concentrate evaporation, and cold storage requirements for fresh and frozen juice products"
weight: 3
---

Apple juice processing requires precise temperature control throughout multiple production stages, from receiving and pressing through pasteurization, concentration, and final product storage. Refrigeration systems must handle variable heat loads from equipment, provide rapid cooling for thermal stability, and maintain cold storage conditions that preserve juice quality while preventing microbial growth.

## Process Overview and Thermal Requirements

Apple juice production follows a temperature-controlled sequence that alternates between heating and cooling operations, requiring refrigeration systems to remove heat from pasteurization, support evaporative concentration, and maintain cold storage zones.

### Production Flow Temperature Profile

| Process Stage | Temperature Range | Heat Load Type | Refrigeration Requirement |
|---------------|-------------------|----------------|---------------------------|
| Fruit receiving | 10-15°C | Ambient cooling | Space conditioning |
| Washing/sorting | 5-10°C | Equipment heat | Process cooling |
| Grinding/milling | 8-12°C | Mechanical heat | Equipment cooling |
| Pressing | 10-15°C | Hydraulic heat | Space and equipment cooling |
| Raw juice holding | 0-4°C | Product cooling | Direct refrigeration |
| Pasteurization | 77-85°C | Heating (upstream) | N/A |
| Post-pasteurization cooling | 4-10°C | Rapid cooling | High-capacity plate cooling |
| Cold filling | 2-6°C | Product cooling | Refrigerated environment |
| Cold storage | 0-4°C | Product storage | Refrigerated warehouse |
| Concentrate evaporation | 50-65°C | Evaporator cooling | Vacuum condenser cooling |
| Frozen concentrate | -18 to -23°C | Blast freezing | Low-temperature refrigeration |

## Receiving and Preparation Areas

### Fruit Receiving Bay Conditions

Apples arriving at processing facilities generate heat from respiration and must be cooled to slow deterioration before processing.

**Temperature control requirements:**
- Ambient air temperature: 10-15°C
- Relative humidity: 85-90%
- Air velocity: 0.5-1.0 m/s maximum to prevent dehydration
- Holding time: 24-72 hours typical

**Refrigeration load calculation:**

Heat of respiration for apples at 10°C:
```
Q_respiration = m × q_r
```

Where:
- m = mass of apples (kg)
- q_r = respiration heat (0.25-0.35 W/kg at 10°C)

For 50,000 kg holding capacity:
```
Q_respiration = 50,000 kg × 0.30 W/kg = 15,000 W = 15 kW
```

Total receiving bay load includes:
- Respiration heat: 15 kW
- Infiltration (doors, traffic): 8-12 kW
- Equipment (conveyors, forklifts): 5-8 kW
- Lighting and people: 3-5 kW
- **Total design load: 35-45 kW**

### Washing and Sorting Area

Water-based washing systems operate at controlled temperatures to optimize cleaning effectiveness while minimizing thermal shock to fruit.

**Design parameters:**
- Wash water temperature: 5-10°C
- Room temperature: 12-16°C
- Water flow rate: 1,500-2,500 L/hr per tonne of fruit
- Heat rejection from pumps: 1.5-2.5 kW per 10 HP motor

**Cooling load components:**

Make-up water cooling:
```
Q_water = ṁ_water × c_p × ΔT
Q_water = (2,000 kg/hr) × (4.18 kJ/kg·K) × (20°C - 7°C) / 3,600
Q_water = 30.2 kW
```

Pump heat rejection for 30 HP total pumping:
```
Q_pumps = 30 HP × 0.746 kW/HP × 0.85 (heat to water)
Q_pumps = 19.0 kW
```

Total washing system cooling: **50-55 kW**

## Grinding and Milling Operations

Mechanical size reduction generates substantial heat from friction and motor inefficiency. Temperature control prevents enzymatic browning and maintains juice quality.

### Grinding Room Conditions

**Design criteria:**
- Room temperature: 8-12°C
- Product temperature increase limit: 2-3°C maximum
- Ventilation rate: 15-20 air changes per hour
- Relative humidity: 80-85%

### Equipment Heat Generation

Hammer mills and graters generate heat proportional to motor loading:

**Heat load from grinding equipment:**

For 100 HP grinding system:
```
Q_grinder = P_motor × (1 - η_motor) / η_motor
Q_grinder = (100 HP × 0.746 kW/HP) × (1 - 0.92) / 0.92
Q_grinder = 6.5 kW heat to product

Q_motor = 100 HP × 0.746 kW/HP × 0.92 × 0.15 (to space)
Q_motor = 10.3 kW heat to space
```

**Total grinding area refrigeration load:**
- Equipment heat to space: 10-12 kW
- Product heat removal: 6-8 kW
- Ventilation load: 8-10 kW
- Miscellaneous: 3-5 kW
- **Total: 30-40 kW**

## Pressing Room Refrigeration

Press operations extract juice while generating hydraulic and mechanical heat. Temperature control during pressing affects juice yield, clarity, and oxidation rates.

### Pressing Room Design Conditions

| Parameter | Rack-Cloth Press | Belt Press | Screw Press |
|-----------|------------------|------------|-------------|
| Room temperature | 10-15°C | 12-16°C | 12-18°C |
| Relative humidity | 75-85% | 70-80% | 70-80% |
| Product temperature rise | 1-2°C | 2-3°C | 3-5°C |
| Hydraulic heat load | 8-12 kW | 5-8 kW | 3-5 kW |
| Motor heat load | 5-8 kW | 10-15 kW | 12-18 kW |

### Hydraulic Press Cooling Requirements

Hydraulic presses generate heat in fluid circuits that must be removed to prevent temperature rise in pressing chambers.

**Hydraulic oil cooler sizing:**

For 150 HP hydraulic power unit:
```
Q_hydraulic = P_pump × (1 - η_system)
Q_hydraulic = (150 HP × 0.746 kW/HP) × 0.25
Q_hydraulic = 28.0 kW
```

Oil-to-water heat exchanger requirements:
- Heat rejection: 28-35 kW
- Oil flow rate: 200-250 L/min
- Oil temperature in: 55-65°C
- Oil temperature out: 40-50°C
- Cooling water supply: 20-25°C
- Cooling water return: 30-35°C

### Press Room Total Cooling Load

For a pressing room with multiple press lines:
- Hydraulic system heat rejection: 25-35 kW
- Motor heat to space: 15-20 kW
- Product heat removal: 8-12 kW
- Room conditioning (infiltration, lights): 10-15 kW
- **Total pressing room load: 60-80 kW**

## Raw Juice Holding and Cold Stabilization

Extracted juice requires immediate cooling to 0-4°C to prevent fermentation, enzymatic browning, and microbial growth before pasteurization.

### Cold Holding Tank Requirements

**Design parameters:**
- Storage temperature: 0-4°C
- Holding time: 2-24 hours
- Tank insulation: 100-150 mm polyurethane foam
- Agitation: Slow paddle, 10-15 RPM
- Heat ingress through walls: 0.3-0.5 W/m²

### Juice Cooling Load Calculation

**Product cooling from pressing to cold storage:**

For 10,000 L/hr juice production:
```
Q_juice = ṁ × c_p × ΔT
Q_juice = (10,000 kg/hr) × (3.9 kJ/kg·K) × (14°C - 2°C) / 3,600
Q_juice = 130 kW
```

**Agitator heat input:**

For 5 HP agitator motor:
```
Q_agitator = 5 HP × 0.746 kW/HP × 0.92 = 3.4 kW
```

**Tank heat ingress:**

For 50 m³ tank with 80 m² surface area:
```
Q_tank = A × U × ΔT
Q_tank = 80 m² × 0.35 W/m²·K × (20°C - 2°C)
Q_tank = 504 W = 0.5 kW
```

**Total cold holding refrigeration load:**
- Product cooling: 130 kW
- Agitation heat: 3-4 kW
- Tank heat ingress: 0.5-1.0 kW
- **Total: 135-140 kW per 10,000 L/hr line**

### Plate Heat Exchanger Configuration

Juice cooling typically uses multi-stage plate heat exchangers for efficiency:

| Stage | Function | Temperature Change | Coolant |
|-------|----------|-------------------|---------|
| 1 | Pre-cooling | 14°C → 10°C | Chilled water (5-7°C) |
| 2 | Final cooling | 10°C → 2°C | Glycol solution (-2 to 0°C) |

**Heat transfer area calculation:**

Using overall heat transfer coefficient U = 2,500 W/m²·K:
```
A = Q / (U × LMTD)

For stage 1:
LMTD = [(14-7) - (10-5)] / ln[(14-7)/(10-5)] = 5.93°C
A₁ = 52,000 W / (2,500 W/m²·K × 5.93 K) = 3.5 m²

For stage 2:
LMTD = [(10-0) - (2-(-2))] / ln[(10-0)/(2-(-2))] = 6.93°C
A₂ = 78,000 W / (2,500 W/m²·K × 6.93 K) = 4.5 m²

Total plate area required: 8.0 m²
```

## Pasteurization and Rapid Cooling

Flash pasteurization heats juice to 77-85°C for 15-30 seconds, followed by immediate cooling to 4-10°C to preserve flavor and nutritional quality.

### Pasteurization System Design

**Thermal treatment parameters:**
- Pasteurization temperature: 77-85°C (typically 79°C)
- Holding time: 15-30 seconds
- Heating medium: Hot water or steam (85-95°C)
- Target pathogen reduction: 5-log reduction

### Post-Pasteurization Cooling Load

Rapid cooling after pasteurization represents the highest instantaneous refrigeration demand in juice processing.

**Cooling load calculation:**

For 10,000 L/hr production rate:
```
Q_cooling = ṁ × c_p × ΔT
Q_cooling = (10,000 kg/hr) × (3.85 kJ/kg·K) × (79°C - 6°C) / 3,600
Q_cooling = 779 kW
```

This substantial load is typically handled through regeneration and staged cooling:

### Regenerative Heat Exchange

Incoming cold juice pre-cools outgoing hot pasteurized juice, reducing net refrigeration load by 60-75%.

**Regeneration efficiency:**

For 70% regeneration efficiency:
```
Energy recovered = 779 kW × 0.70 = 545 kW
Net refrigeration required = 779 - 545 = 234 kW
```

### Multi-Stage Cooling Configuration

| Stage | Temperature Range | Cooling Medium | Heat Removed |
|-------|-------------------|----------------|--------------|
| Regeneration | 79°C → 25°C | Incoming cold juice | 545 kW |
| Water cooling | 25°C → 12°C | Chilled water (7-10°C) | 131 kW |
| Final cooling | 12°C → 6°C | Glycol (-1 to 2°C) | 60 kW |
| Trim cooling | 6°C → 4°C | Direct expansion | 20 kW |

**Total refrigeration plant capacity required: 250-280 kW**

### Plate Heat Exchanger Selection

**Regeneration section:**
- Heat duty: 545 kW
- Flow rate: 10,000 kg/hr both sides
- Temperature approach: 3-5°C
- Overall U-value: 2,800 W/m²·K
- Estimated area: 45-50 m²

**Cooling section:**
- Heat duty: 234 kW
- Overall U-value: 2,500 W/m²·K
- Estimated area: 20-25 m²

## Cold Filling and Packaging

Aseptic or cold-fill packaging maintains product temperature at 2-6°C during filling operations to ensure microbial stability.

### Filling Room Environmental Control

**Design conditions:**
- Room temperature: 4-8°C
- Relative humidity: 60-70% (condensation control)
- Air cleanliness: ISO Class 7 or 8
- Air changes: 25-30 per hour
- Positive pressure: 10-15 Pa relative to adjacent spaces

### Filling Room Refrigeration Load

**Sensible cooling load components:**

Equipment heat:
- Filling machines (motors, pumps): 15-20 kW
- Conveyors and ancillary equipment: 8-12 kW
- Lighting (LED): 3-5 kW

Infiltration and ventilation:
```
Q_ventilation = ṁ_air × c_p × ΔT
Q_ventilation = (12,000 kg/hr) × (1.006 kJ/kg·K) × (20°C - 6°C) / 3,600
Q_ventilation = 47 kW
```

Personnel (10 workers at 150 W sensible each):
```
Q_people = 10 × 0.15 kW = 1.5 kW
```

**Total filling room sensible load: 75-90 kW**

**Latent cooling load:**

Latent heat from personnel and infiltration:
```
Q_latent = n × q_latent + ṁ_infiltration × Δω × h_fg
Q_latent = (10 × 75 W) + infiltration component
Q_latent = 5-10 kW
```

**Total filling room load: 85-100 kW**

### Aseptic Processing Requirements

Aseptic processing systems require ultra-clean environments with enhanced environmental control.

**Aseptic room conditions:**
- Temperature: 18-22°C (higher than cold fill)
- Relative humidity: 40-50%
- Air cleanliness: ISO Class 5-6
- HEPA filtration: 99.97% at 0.3 μm
- Laminar flow velocity: 0.3-0.5 m/s in critical zones

**Refrigeration implications:**

Aseptic rooms operate at near-ambient temperature but require dehumidification:
- Sensible cooling: 30-40 kW
- Latent cooling (dehumidification): 20-30 kW
- **Total: 50-70 kW**

## Cold Storage of Finished Juice

Pasteurized juice requires continuous refrigeration to maintain quality and extend shelf life.

### Cold Storage Design Parameters

| Storage Type | Temperature | Relative Humidity | Storage Duration | Refrigeration Intensity |
|--------------|-------------|-------------------|------------------|-------------------------|
| Short-term | 2-4°C | 85-90% | 7-14 days | 60-80 W/m³ |
| Medium-term | 0-2°C | 85-90% | 30-60 days | 80-100 W/m³ |
| Long-term | -1 to 0°C | 90-95% | 90-180 days | 100-120 W/m³ |

### Cold Storage Load Calculation

For 1,000 m³ cold storage room (200 tonnes capacity):

**Transmission load:**

Wall area = 1,200 m² (including floor and ceiling)
U-value = 0.25 W/m²·K (150 mm insulation)
```
Q_transmission = A × U × ΔT
Q_transmission = 1,200 m² × 0.25 W/m²·K × (25°C - 2°C)
Q_transmission = 6,900 W = 6.9 kW
```

**Product load:**

Daily throughput: 20 tonnes/day
```
Q_product = ṁ × c_p × ΔT
Q_product = (20,000 kg/24 hr) × (3.9 kJ/kg·K) × (20°C - 2°C) / 3,600
Q_product = 16.3 kW
```

**Infiltration load:**

For 2 door openings per hour, 3 m × 3 m door:
```
Q_infiltration = n × V_exchange × ρ × Δh
Q_infiltration = 2/hr × 100 m³ × 1.2 kg/m³ × 30 kJ/kg / 3,600
Q_infiltration = 2.0 kW
```

**Equipment and lighting:**
- Forklift operation: 8-10 kW
- Lighting: 2-3 kW
- Evaporator fans: 3-4 kW

**Total cold storage refrigeration load:**
- Transmission: 6.9 kW
- Product cooling: 16.3 kW
- Infiltration: 2.0 kW
- Equipment: 15.0 kW
- Safety factor (15%): 6.0 kW
- **Design capacity: 50 kW**

## Concentrate Production by Evaporation

Apple juice concentrate (typically 70-72°Brix) requires vacuum evaporation with substantial refrigeration for condenser cooling.

### Evaporation System Configuration

Multiple-effect evaporators operate under vacuum to minimize thermal degradation:

| Effect | Operating Pressure | Evaporation Temperature | Purpose |
|--------|-------------------|------------------------|---------|
| 1st effect | 60-70 kPa absolute | 85-90°C | Primary evaporation |
| 2nd effect | 40-50 kPa absolute | 75-80°C | Secondary evaporation |
| 3rd effect | 20-30 kPa absolute | 60-65°C | Final concentration |
| Vapor condenser | 4-8 kPa absolute | 30-35°C | Vapor condensation |

### Evaporator Cooling Requirements

**Water evaporation rate:**

To concentrate 10,000 kg/hr of single-strength juice (12°Brix) to 70°Brix:

Concentration ratio:
```
CR = Brix_concentrate / Brix_feed = 70 / 12 = 5.83

Mass of concentrate = 10,000 kg/hr / 5.83 = 1,716 kg/hr
Water evaporated = 10,000 - 1,716 = 8,284 kg/hr
```

**Heat of evaporation:**

Average latent heat at vacuum conditions ≈ 2,300 kJ/kg
```
Q_evaporation = ṁ_water × h_fg
Q_evaporation = (8,284 kg/hr) × (2,300 kJ/kg) / 3,600
Q_evaporation = 5,290 kW
```

### Vacuum Condenser Refrigeration Load

Final effect vapors must be condensed to maintain vacuum. This represents the major refrigeration load in concentrate production.

**Condenser duty:**

Vapor to be condensed: 8,284 kg/hr at 30-35°C
```
Q_condenser = ṁ_vapor × h_fg_vacuum
Q_condenser = (8,284 kg/hr) × (2,400 kJ/kg) / 3,600
Q_condenser = 5,523 kW ≈ 5.5 MW
```

**Cooling water requirements:**

Using cooling water with 10°C temperature rise:
```
ṁ_cooling_water = Q / (c_p × ΔT)
ṁ_cooling_water = 5,523 kW / (4.18 kJ/kg·K × 10 K)
ṁ_cooling_water = 132 kg/s = 475 m³/hr
```

### Refrigerated Condenser Design

For locations without adequate cooling water, mechanical refrigeration provides condenser cooling:

**Chiller capacity:**
- Heat rejection: 5,500-6,000 kW
- Chilled water supply: 8-12°C
- Chilled water return: 18-22°C
- Flow rate: 450-500 m³/hr
- **Refrigeration plant: 1,570 kW cooling (assuming 3.5 kW/kW refrigeration)**

### Concentrate Cooling After Evaporation

Hot concentrate (60-70°C) must be rapidly cooled to preserve flavor compounds.

**Concentrate cooling load:**

For 1,716 kg/hr concentrate production:
```
Q_concentrate = ṁ × c_p × ΔT
Q_concentrate = (1,716 kg/hr) × (2.8 kJ/kg·K) × (65°C - 5°C) / 3,600
Q_concentrate = 80 kW
```

Tubular or plate heat exchangers provide cooling in two stages:
- Stage 1: 65°C → 25°C using chilled water (70°C approach)
- Stage 2: 25°C → 5°C using glycol solution (-2°C supply)

## Frozen Concentrate Storage

Apple juice concentrate stored frozen (-18 to -23°C) maintains quality for 12-24 months.

### Freezing System Requirements

**Blast freezing of concentrate drums:**

For 200 L drums (240 kg concentrate each):

Freezing load per drum:
```
Q_freeze = m × [c_p_unfrozen × ΔT₁ + L_f + c_p_frozen × ΔT₂]

Where:
c_p_unfrozen = 2.8 kJ/kg·K
Latent heat L_f = 180 kJ/kg (70°Brix)
c_p_frozen = 1.6 kJ/kg·K

Q_freeze = 240 kg × [(2.8 × 15) + 180 + (1.6 × 13)]
Q_freeze = 240 kg × [42 + 180 + 20.8]
Q_freeze = 240 kg × 242.8 kJ/kg = 58,272 kJ per drum
```

**Freezing time:**

Target freezing time: 24 hours per drum

Average cooling rate:
```
Q_avg = 58,272 kJ / (24 hr × 3,600 s/hr) = 0.67 kW per drum
```

For blast freezer with 100 drum capacity:
**Freezer refrigeration load: 65-75 kW**

### Frozen Storage Warehouse

**Design parameters:**
- Storage temperature: -20 to -23°C
- Warehouse volume: 2,000 m³ (400 tonnes capacity)
- Insulation: 200-250 mm polyurethane
- Evaporator ΔT: 8-10°C
- Defrost cycle: Electric or hot gas, 2-3 times daily

**Frozen storage load calculation:**

Transmission load (wall area = 1,800 m²):
```
Q_transmission = 1,800 m² × 0.15 W/m²·K × [25°C - (-22°C)]
Q_transmission = 12,690 W = 12.7 kW
```

Product load (30 tonnes/day throughput):
```
Q_product = (30,000 kg/24 hr) × (1.6 kJ/kg·K) × [5°C - (-22°C)] / 3,600
Q_product = 15.0 kW
```

Infiltration (calculated for -20°C storage):
```
Q_infiltration = 4-6 kW
```

Equipment:
- Forklifts: 10-12 kW
- Lighting: 2-3 kW
- Evaporator fans: 5-6 kW

**Total frozen storage design load:**
- Transmission: 12.7 kW
- Product: 15.0 kW
- Infiltration: 5.0 kW
- Equipment: 18.0 kW
- Safety factor: 7.5 kW
- **Design capacity: 60 kW at -22°C**

## Refrigeration System Architecture

### Primary Refrigeration Plant Configuration

Apple juice processing requires multiple refrigeration temperature levels, typically served by separate systems or a cascade arrangement.

**Temperature zones:**

| Zone | Evaporating Temperature | Refrigerant | Application |
|------|------------------------|-------------|-------------|
| High-temp | 0 to +5°C | R-134a, R-513A | Cold storage, filling room |
| Medium-temp | -5 to -8°C | R-404A, R-449A | Juice cooling, glycol |
| Low-temp | -28 to -30°C | R-404A, R-507A | Frozen storage |
| Ultra-low | -35 to -40°C | NH₃, cascade | Blast freezing |

### Chiller Plant for Process Cooling

Central chiller plants provide chilled water and glycol for process cooling throughout the facility.

**Chilled water system (7-12°C):**
- Supply temperature: 7°C
- Return temperature: 12°C
- Design flow rate: Based on total load
- Secondary pumping: Variable speed

**Glycol system (-2 to +2°C):**
- Glycol concentration: 25-30% propylene glycol
- Supply temperature: -2°C
- Return temperature: +2°C
- Freeze protection to: -15°C

### System Capacity Summary

For a complete 10,000 L/hr juice processing plant:

| System Component | Refrigeration Load | Temperature Level |
|------------------|-------------------|-------------------|
| Receiving bay | 40 kW | 10°C |
| Washing area | 55 kW | 12°C |
| Grinding/pressing | 70 kW | 10°C |
| Raw juice cooling | 140 kW | 2°C |
| Post-pasteurization | 280 kW | 6°C |
| Filling room | 100 kW | 6°C |
| Cold storage (juice) | 50 kW | 2°C |
| Evaporator condenser | 1,570 kW | 10°C |
| Concentrate cooling | 80 kW | 5°C |
| Blast freezing | 75 kW | -40°C |
| Frozen storage | 60 kW | -22°C |

**Total connected load: 2,520 kW**

**Installed capacity with diversity (0.75 factor): 1,900 kW**

## Energy Efficiency Strategies

### Heat Recovery Opportunities

**Condenser heat recovery:**

Evaporator condenser heat (5,500 kW) can be recovered for:
- Juice pre-heating before pasteurization
- Facility space heating
- Hot water generation
- First-effect evaporator heating

Theoretical heat recovery potential: 3,500-4,000 kW

**Pasteurizer regeneration:**

Regenerative heat exchange reduces cooling load by 60-75%, saving:
```
Energy saved = 779 kW × 0.70 = 545 kW refrigeration capacity
Annual savings = 545 kW × 4,000 hr/yr × $0.12/kWh = $262,000/yr
```

### Variable Speed Drive Applications

**Compressor VFD benefits:**

Compressor capacity modulation to match variable loads:
- Part-load operation: 40-60% of design capacity during low production
- Energy savings: 25-35% compared to on-off control
- Reduced starting current and mechanical wear

**Pump and fan VFDs:**

Chilled water and glycol pumps with VFDs:
- Flow matching to instantaneous demand
- Energy savings: 30-50% at part load
- Improved process control

### Floating Head Pressure Control

Allow condensing temperature to decrease with ambient conditions:

**Energy savings calculation:**

For 500 kW refrigeration load, reducing head pressure by 5°C:
```
COP improvement ≈ 8-12%
Energy savings = 500 kW × 0.10 / 2.5 (COP) = 20 kW compressor power
Annual savings = 20 kW × 6,000 hr/yr × $0.12/kWh = $14,400/yr
```

### Thermal Storage Integration

Ice or chilled water storage reduces peak demand and enables load shifting:

**Ice storage for peak shaving:**

Daily cooling load profile shows peaks during pasteurization and concentrate production. Ice storage built during off-peak hours (night) provides:
- Peak demand reduction: 30-40%
- Time-of-use rate savings: $30,000-50,000/yr
- Reduced installed chiller capacity
- Emergency cooling backup

**Storage tank sizing:**

For 4-hour peak shaving at 400 kW average load:
```
Energy storage required = 400 kW × 4 hr = 1,600 kWh

Ice storage mass:
m_ice = (1,600 kWh × 3,600 kJ/kWh) / 334 kJ/kg = 17,246 kg ice
Ice storage volume ≈ 20-25 m³ (including water)
```

### Ammonia Refrigeration Efficiency

Large juice processing facilities often use ammonia (R-717) for environmental and efficiency benefits:

**Ammonia system advantages:**
- Higher latent heat: 1,370 kJ/kg vs. 217 kJ/kg (R-134a)
- Better heat transfer properties
- Lower refrigerant charge per kW
- Zero GWP and ODP
- Lower operating costs: 15-25% vs. HFC systems

**Typical ammonia system efficiency:**

For large cold storage (500 kW at -20°C):
```
COP_ammonia = 2.8-3.2
Compressor power = 500 kW / 3.0 = 167 kW

COP_R-404A = 2.2-2.5
Compressor power = 500 kW / 2.35 = 213 kW

Power savings = 213 - 167 = 46 kW (22% reduction)
```

## Defrost Strategies for Low-Temperature Systems

### Evaporator Coil Frosting

Frozen storage and blast freezer evaporators accumulate frost from air moisture and product moisture release.

**Frost accumulation rate:**

For -22°C storage with 2% infiltration air (at 20°C, 60% RH):
```
Moisture removal = ṁ_air × (ω_ambient - ω_storage)
ω_ambient ≈ 0.0087 kg_water/kg_air
ω_storage ≈ 0.0006 kg_water/kg_air

Moisture = 1,500 kg_air/hr × (0.0087 - 0.0006) = 12.2 kg/hr
Daily frost accumulation ≈ 290 kg/day
```

### Defrost Methods and Energy Consumption

| Defrost Method | Application | Duration | Energy Input | Efficiency |
|----------------|-------------|----------|--------------|------------|
| Off-cycle (air) | High-temp only | 2-4 hr | None (fans only) | Poor below -5°C |
| Electric | All temps | 20-40 min | 8-12 kW per coil | Good control |
| Hot gas | Medium/low-temp | 15-30 min | Compressor heat | Most efficient |
| Water spray | Low-temp blast | 10-15 min | 5-8 kW + water | Fast, water disposal |

**Hot gas defrost energy balance:**

For 60 kW evaporator coil at -22°C:
```
Frost mass = 15 kg (typical per coil)
Heating from -22°C to 0°C: Q₁ = 15 kg × 2.1 kJ/kg·K × 22°C = 693 kJ
Melting: Q₂ = 15 kg × 334 kJ/kg = 5,010 kJ
Draining: Q₃ = 15 kg × 4.18 kJ/kg·K × 5°C = 314 kJ
Total heat required = 6,017 kJ

Hot gas heat available = 80-100 kW (compressor discharge)
Defrost time = 6,017 kJ / (90 kW × 0.7 efficiency) = 95 seconds ≈ 90-100 seconds
```

Practical defrost time includes coil warm-up and draining: 15-20 minutes total.

## Refrigerant Leak Detection and Safety

Processing facilities handling food products require robust refrigerant safety systems, particularly for ammonia installations.

### Ammonia Safety Systems

**Detection thresholds:**
- OSHA PEL (8-hour TWA): 25 ppm
- OSHA STEL (15-minute): 35 ppm
- IDLH (Immediately Dangerous): 300 ppm
- Detection setpoint: 10-15 ppm (alarm)
- Emergency ventilation activation: 25 ppm

**Ventilation requirements:**

Machinery room ventilation for ammonia:
- Normal ventilation: 30 cfm per 1,000 BTU/hr compressor capacity
- Emergency ventilation: 150 cfm per 1,000 BTU/hr
- Discharge location: 25 ft minimum from air intakes

For 600 kW (2,047,000 BTU/hr) refrigeration capacity:
```
Normal ventilation = 30 cfm × 2,047 = 61,410 cfm
Emergency ventilation = 150 cfm × 2,047 = 307,050 cfm
```

### HFC Refrigerant Detection

Lower-toxicity HFC refrigerants still require monitoring for:
- Oxygen displacement (confined spaces)
- Leak prevention (environmental regulations)
- Cost control (refrigerant expense)

**Monitoring strategy:**
- Fixed sensors in machinery rooms: Every 300-500 ft²
- Portable detectors for maintenance
- Alarm setpoints: 10% LEL or 1,000 ppm (whichever lower)

## Instrumentation and Control Integration

### Critical Temperature Monitoring Points

| Location | Sensor Type | Range | Accuracy | Alarm |
|----------|-------------|-------|----------|-------|
| Raw juice tanks | RTD Pt-100 | -5 to +50°C | ±0.2°C | >5°C |
| Pasteurizer inlet | RTD Pt-100 | 0 to +100°C | ±0.15°C | <1°C |
| Pasteurizer outlet | RTD Pt-100 | 50 to +100°C | ±0.15°C | <75°C |
| Post-cooling outlet | RTD Pt-100 | 0 to +50°C | ±0.2°C | >8°C |
| Cold storage rooms | RTD Pt-100 | -5 to +15°C | ±0.3°C | >6°C |
| Frozen storage | Type T thermocouple | -40 to +20°C | ±0.5°C | >-18°C |
| Glycol supply | RTD Pt-100 | -10 to +10°C | ±0.2°C | >3°C |
| Evaporator vacuum | Vacuum transducer | 0-100 kPa abs | ±0.5 kPa | >10 kPa |

### Automated Control Sequences

**Pasteurization cooling control:**

PLC-based control sequence:
1. Monitor pasteurizer outlet temperature (79°C setpoint)
2. Modulate cooling valve to maintain 6°C outlet temperature
3. Adjust glycol flow based on product flow rate (ratio control)
4. Alarm if outlet temperature exceeds 10°C for >30 seconds
5. Divert product to rework tank on cooling failure

**Cold storage temperature control:**

Cascade control strategy:
- Primary loop: Room air temperature (2°C setpoint)
- Secondary loop: Evaporator superheat (5°C setpoint)
- Compressor capacity modulation via slide valve or VFD
- Defrost initiation on pressure differential or time

**Energy management system integration:**

BAS monitors and optimizes:
- Chiller sequencing based on load
- Floating head pressure control
- Thermal storage charge/discharge cycles
- Heat recovery activation
- Demand limiting during peak periods

Target metrics:
- kW per tonne of juice processed: 0.35-0.45 kW/tonne
- Refrigeration COP system-wide: 2.5-3.2
- Heat recovery utilization: >60% of available

---

**File location:** `/Users/evgenygantman/Documents/github/gantmane/hvac/content/refrigeration-systems/food-processing-refrigeration/fruit-processing/apple-processing/apple-juice-processing/_index.md`

This comprehensive technical reference covers refrigeration system design for apple juice processing from receiving through frozen concentrate storage, with detailed load calculations, equipment specifications, and energy efficiency strategies for HVAC professionals designing food processing facilities.
