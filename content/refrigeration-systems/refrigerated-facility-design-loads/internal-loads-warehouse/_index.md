---
title: "Internal Loads Warehouse"
description: "Comprehensive technical analysis of internal heat loads in refrigerated warehouses including lighting, forklift equipment, personnel, electric motors, and defrost systems with ASHRAE calculation methods and design values"
weight: 5
---

Internal heat loads constitute a significant portion of the total refrigeration load in cold storage facilities. Unlike transmission and infiltration loads, internal loads are directly controllable through operational practices and equipment selection. Accurate calculation of these loads is essential for proper refrigeration system sizing and energy cost projection.

## Lighting Heat Gain

Lighting represents a continuous internal load in refrigerated warehouses, with magnitude dependent on fixture type, layout, and operational schedule.

### Heat Release from Lighting Systems

The total heat gain from lighting is:

**Q_light = W × F_u × F_sa**

Where:
- Q_light = Heat gain from lighting (W)
- W = Total installed lighting power (W)
- F_u = Usage factor (fraction of lights operating)
- F_sa = Special allowance factor (typically 1.0)

### Lighting Power Density Values

| Application Area | Lighting Power Density | Typical Fixture Type |
|-----------------|----------------------|---------------------|
| High-bay storage (-20°F to 35°F) | 5-8 W/ft² | LED high-bay |
| Low-bay storage | 8-12 W/ft² | LED or T8 fluorescent |
| Shipping/receiving docks | 15-20 W/ft² | High-output LED |
| Freezer aisles (-20°F to 0°F) | 6-10 W/ft² | Cold-rated LED |
| Processing areas | 20-30 W/ft² | LED panel/troffer |

### Temperature-Dependent Lighting Efficiency

Fluorescent fixture efficiency decreases at low temperatures. LED fixtures maintain performance but require cold-temperature ratings:

| Space Temperature | Fluorescent Output | LED Output | Ballast Heat Factor |
|------------------|-------------------|-----------|-------------------|
| 70°F | 100% | 100% | 1.0 |
| 35°F | 85-90% | 98-100% | 1.15 |
| 0°F | 60-70% | 95-98% | 1.25 |
| -20°F | 40-50% | 90-95% | 1.35 |

The ballast/driver heat factor accounts for additional heat release to the space from inefficient operation at low temperatures.

### Usage Factors

Lighting usage factors depend on operational practices:

- **Motion sensor control**: F_u = 0.20 to 0.40
- **Scheduled operation (8 hr/day)**: F_u = 0.33
- **Scheduled operation (16 hr/day)**: F_u = 0.67
- **Continuous operation**: F_u = 1.0
- **High-bay with occupancy sensing**: F_u = 0.25 to 0.35

ASHRAE Handbook - Refrigeration recommends motion sensor control for cold storage facilities operating below 35°F to minimize lighting loads.

## Forklift and Material Handling Equipment

Material handling equipment generates substantial heat through engine combustion, electric motor inefficiency, and battery charging. Equipment type significantly impacts refrigeration load.

### Electric Forklift Heat Release

Electric forklifts release heat from motor inefficiency and resistance heating:

**Q_forklift = (P_motor / η_motor) × t_op × N**

Where:
- Q_forklift = Heat release (Btu/hr)
- P_motor = Motor power rating (hp)
- η_motor = Motor efficiency (typically 0.85-0.90)
- t_op = Operating time fraction
- N = Number of units

| Forklift Capacity | Motor Power | Heat Release (Operating) | Heat Release (Standby) |
|------------------|------------|------------------------|---------------------|
| 3,000 lb | 15-20 hp | 15,000-18,000 Btu/hr | 2,000-3,000 Btu/hr |
| 4,000 lb | 20-25 hp | 18,000-22,000 Btu/hr | 2,500-3,500 Btu/hr |
| 5,000 lb | 25-30 hp | 22,000-27,000 Btu/hr | 3,000-4,000 Btu/hr |
| 6,000 lb | 30-36 hp | 27,000-32,000 Btu/hr | 3,500-5,000 Btu/hr |

### Internal Combustion Equipment

Propane or natural gas forklifts release all fuel combustion energy to the space:

**Q_IC = N × m_fuel × HHV × t_op**

Where:
- Q_IC = Heat from internal combustion (Btu/hr)
- N = Number of units
- m_fuel = Fuel consumption rate (lb/hr or ft³/hr)
- HHV = Higher heating value of fuel (Btu/lb or Btu/ft³)
- t_op = Operating time fraction

| Fuel Type | HHV | Typical Consumption | Heat Release per Unit |
|-----------|-----|-------------------|---------------------|
| Propane | 21,500 Btu/lb | 2-4 lb/hr | 43,000-86,000 Btu/hr |
| Natural gas | 1,050 Btu/ft³ | 40-80 ft³/hr | 42,000-84,000 Btu/hr |
| Diesel | 19,000 Btu/lb | 3-6 lb/hr | 57,000-114,000 Btu/hr |

**Internal combustion equipment should not operate in refrigerated spaces below 35°F due to excessive heat release and exhaust contamination.**

### Battery Charging Heat

Battery charging releases heat to the space through charging inefficiency:

**Q_charge = (V × I × t_charge) / η_charge**

Where:
- Q_charge = Charging heat (Btu)
- V = Charging voltage (typically 36-80 V)
- I = Charging current (A)
- t_charge = Charging duration (hr)
- η_charge = Charging efficiency (0.80-0.85)

Typical charging heat: 5,000-8,000 Btu per charge cycle. For facilities with in-space charging:

**Q_charge_avg = (N_units × Q_per_charge × charges_per_day) / 24**

### Equipment Operating Time Factors

| Operation Type | Time Factor (t_op) | Basis |
|---------------|------------------|-------|
| Continuous shift operation | 0.60-0.75 | Active time during shift |
| Intermittent operation | 0.40-0.60 | Multiple short tasks |
| Peak period operation | 0.80-0.90 | Loading/unloading periods |
| Standby/idle | 0.10-0.20 | Parked in space |

Conservative design assumes 0.70 operating time factor for high-activity warehouses.

## Personnel Heat Gain

Occupants release sensible and latent heat through metabolic activity. In cold environments, latent heat from respiration becomes more significant relative to sensible heat.

### Metabolic Heat Release Rates

**q_person = q_sensible + q_latent**

| Activity Level | Sensible Heat (Btu/hr) | Latent Heat (Btu/hr) | Total Heat (Btu/hr) | Application |
|---------------|----------------------|-------------------|------------------|-------------|
| Seated, light work | 245 | 155 | 400 | Office, control room |
| Standing, light work | 250 | 200 | 450 | Inspection, supervision |
| Walking slowly (2 mph) | 305 | 245 | 550 | General warehouse work |
| Medium work | 345 | 405 | 750 | Order picking, stocking |
| Heavy work | 425 | 575 | 1,000 | Manual material handling |

### Cold Space Personnel Heat Adjustment

In spaces below 50°F, personnel wear insulated clothing that reduces sensible heat transfer to the space:

| Space Temperature | Clothing Insulation | Sensible Heat Factor |
|------------------|-------------------|-------------------|
| 35°F to 50°F | Light jacket | 0.85 |
| 0°F to 35°F | Insulated coat | 0.70 |
| -20°F to 0°F | Heavy insulated suit | 0.55 |

**Q_personnel = N_people × (q_sensible × F_clothing + q_latent) × F_occupancy**

Where F_clothing accounts for reduced sensible heat transfer through insulated clothing.

### Occupancy Factors

| Warehouse Type | Peak Occupancy | Average Occupancy Factor | Design Occupancy |
|---------------|---------------|----------------------|-----------------|
| Automated high-bay | 0.001-0.002 people/1000 ft² | 0.60 | Very low |
| Conventional pallet storage | 0.005-0.01 people/1000 ft² | 0.70 | Low |
| Order picking facility | 0.02-0.04 people/1000 ft² | 0.75 | Medium |
| Processing/distribution | 0.05-0.10 people/1000 ft² | 0.80 | High |

### Respiration Moisture Load

In freezer applications, exhaled moisture immediately condenses and contributes to frost accumulation on evaporator coils:

**W_respiration = N_people × 0.5 lb_H2O/hr × t_occupancy**

This moisture load (approximately 500 Btu/lb latent heat plus heat of crystallization at 169 Btu/lb) requires additional defrost energy.

## Electric Motor Heat Gain

Electric motors driving pumps, conveyors, and other equipment release heat based on motor location relative to the refrigerated space.

### Motor Heat Release Configuration

Three configurations exist:

1. **Motor and driven equipment in space**: All motor inefficiency and equipment friction heat released to space
2. **Motor in space, driven equipment outside**: Only motor inefficiency heat released to space
3. **Motor outside, driven equipment in space**: Only equipment friction/inefficiency heat released to space

### Heat Release Equations

**Motor and equipment in space:**

**Q_motor_total = (P_rated × LF) / η_motor**

**Motor in space only:**

**Q_motor_only = P_rated × LF × (1 - η_motor) / η_motor**

**Equipment in space only:**

**Q_equipment_only = P_rated × LF × (1 - η_equipment)**

Where:
- P_rated = Motor nameplate power (hp or kW)
- LF = Load factor (fraction of rated power)
- η_motor = Motor efficiency
- η_equipment = Driven equipment efficiency

### Motor Efficiency Values

| Motor Size | Standard Efficiency | Premium Efficiency (NEMA Premium) |
|-----------|-------------------|--------------------------------|
| 1-5 hp | 0.80-0.85 | 0.86-0.88 |
| 5-20 hp | 0.85-0.89 | 0.89-0.92 |
| 20-50 hp | 0.89-0.92 | 0.92-0.94 |
| 50-100 hp | 0.92-0.94 | 0.94-0.95 |
| 100-200 hp | 0.93-0.95 | 0.95-0.96 |

### Typical Warehouse Equipment Loads

| Equipment Type | Motor Size | Load Factor | Operating Hours | Heat Release |
|---------------|-----------|------------|----------------|-------------|
| Conveyor system (100 ft) | 5-10 hp | 0.60-0.80 | Intermittent | 3,000-6,000 Btu/hr |
| Pallet wrapper | 2-3 hp | 0.50-0.70 | Intermittent | 1,500-2,500 Btu/hr |
| Dock leveler (hydraulic) | 3-5 hp | 0.40-0.60 | Intermittent | 2,000-3,500 Btu/hr |
| Vertical reciprocating conveyor | 10-15 hp | 0.70-0.85 | Continuous | 7,000-11,000 Btu/hr |
| AGV charging station | 15-25 hp | Variable | Intermittent | 10,000-18,000 Btu/hr |

### Conveyor System Load Calculation

For belt conveyors operating in refrigerated spaces:

**Q_conveyor = (P_motor / η_motor) × LF × t_op + Q_friction**

Where Q_friction represents bearing and belt friction heat (typically 10-15% of motor power).

**Design Recommendation**: Locate motor drives outside refrigerated spaces when possible. Use cold-rated motors (rated for -20°F or lower) for in-space applications.

## Defrost Heat Load

Evaporator defrost is a major internal load in low-temperature applications. Defrost heat removes frost accumulation and warms the coil to prevent ice bridging.

### Defrost Methods and Heat Input

| Defrost Method | Heat Input Rate | Typical Duration | Energy per Cycle | Applications |
|---------------|----------------|-----------------|-----------------|--------------|
| Electric resistance | 1.5-2.5 W/ft² coil | 20-45 min | High | Freezers, low-temp |
| Hot gas bypass | 1.0-1.8 W/ft² coil | 15-30 min | Medium | Medium/low-temp |
| Reverse cycle | 0.8-1.5 W/ft² coil | 15-25 min | Low | Medium-temp only |
| Off-cycle (air) | 0 (ambient heat) | 2-8 hr | Very low | Above 32°F only |

### Electric Defrost Heat Load Calculation

**Q_defrost = A_coil × q_defrost × N_cycles × t_defrost / 24**

Where:
- Q_defrost = Average defrost heat load (Btu/hr)
- A_coil = Total evaporator coil face area (ft²)
- q_defrost = Defrost heat flux (Btu/hr-ft²)
- N_cycles = Defrost cycles per day
- t_defrost = Defrost duration (hr)

### Defrost Frequency Requirements

| Space Temperature | Humidity Load | Defrost Cycles/Day | Basis |
|------------------|--------------|-------------------|-------|
| 32°F to 40°F | Low | 1-2 | Minimal frost |
| 0°F to 32°F | Medium | 2-3 | Moderate frost |
| -20°F to 0°F | Medium | 3-4 | Significant frost |
| Below -20°F | High | 4-6 | Heavy frost |

Defrost frequency increases with:
- Higher infiltration rates
- Increased door traffic
- Personnel occupancy
- Forklift exhaust (if IC equipment used)
- Product loading frequency

### Hot Gas Defrost Calculations

Hot gas defrost uses refrigerant system heat:

**Q_hotgas = m_ref × (h_gas_in - h_liquid_out) × N_cycles × t_defrost / 24**

Where:
- m_ref = Refrigerant mass flow rate (lb/hr)
- h_gas_in = Enthalpy of hot gas entering coil (Btu/lb)
- h_liquid_out = Enthalpy of liquid leaving coil (Btu/lb)

Typical hot gas defrost heat flux: 3,500-6,000 Btu/hr per ft² of coil face area.

### Defrost Termination Methods

| Termination Method | Set Point | Advantages | Disadvantages |
|-------------------|-----------|-----------|---------------|
| Time | 20-45 min | Simple, predictable | May over/under defrost |
| Temperature | 45-55°F coil temp | Efficient | Requires sensor |
| Pressure | Saturated suction pressure | Responsive | Complex control |
| Adaptive | Algorithm-based | Optimal efficiency | Requires sophisticated control |

**Design Practice**: Use temperature-initiated, temperature-terminated defrost control for maximum efficiency. Terminate defrost at 45-50°F coil surface temperature.

### Defrost Drip Pan Heating

Electric heaters in drip pans prevent refreezing of condensate:

**Q_pan = L_pan × W_pan × 10-15 W/ft²**

Typical drip pan heater power: 100-300 W per evaporator unit. Operates continuously in freezer applications.

## Product Heat Load

While product-specific, internal product heat manifests when product enters at above-space temperature or when product is processed in the space.

### Product Cooling Load

**Q_product = m_product × c_p × (T_in - T_final) / t_cool**

Where:
- m_product = Product mass flow rate (lb/hr)
- c_p = Specific heat of product (Btu/lb-°F)
- T_in = Product temperature entering space (°F)
- T_final = Final product temperature (°F)
- t_cool = Time to reach final temperature (hr)

### Respiration Heat (Produce)

Fresh fruits and vegetables release metabolic heat:

| Product | Respiration at 32°F | Respiration at 40°F | Respiration at 50°F |
|---------|-------------------|-------------------|-------------------|
| Apples | 400-600 Btu/ton-day | 800-1,200 Btu/ton-day | 1,600-2,400 Btu/ton-day |
| Lettuce | 2,000-3,000 Btu/ton-day | 4,000-6,000 Btu/ton-day | 8,000-12,000 Btu/ton-day |
| Potatoes | 600-900 Btu/ton-day | 1,200-1,800 Btu/ton-day | 2,400-3,600 Btu/ton-day |
| Strawberries | 2,500-3,500 Btu/ton-day | 5,000-7,000 Btu/ton-day | 10,000-14,000 Btu/ton-day |
| Tomatoes | 800-1,200 Btu/ton-day | 1,600-2,400 Btu/ton-day | 3,200-4,800 Btu/ton-day |

**Q_respiration = (m_stored / 2000) × q_respiration**

Where m_stored is total stored mass (lb) and q_respiration is rate per ton from tables.

## Safety Factor and Design Margins

Internal loads should include appropriate safety factors:

| Load Component | Typical Safety Factor | Conservative Design Factor |
|---------------|---------------------|--------------------------|
| Lighting | 1.0 | 1.0 (known exactly) |
| Forklifts | 1.10-1.15 | 1.20 (usage uncertainty) |
| Personnel | 1.0 | 1.0 (if count verified) |
| Electric motors | 1.10 | 1.15 (load factor variation) |
| Defrost | 1.0 | 1.0 (calculated directly) |
| Product | 1.15-1.25 | 1.25 (throughput variation) |

**Total internal load = Σ(Individual loads × Safety factors)**

Apply safety factors to individual components rather than total load to avoid compounding conservatism.

## Load Calculation Example

**Warehouse Specifications:**
- Size: 50,000 ft² footprint, 30 ft height
- Temperature: 0°F
- Operation: 16 hr/day, 5 days/week
- Equipment: 6 electric forklifts, 3 conveyors
- Personnel: 12 workers during operation
- Evaporator coils: 2,000 ft² total face area

**Lighting Load:**
- Installed power: 50,000 ft² × 8 W/ft² = 400,000 W
- Usage factor: 0.67 (16 hr operation)
- Q_light = 400,000 × 0.67 = 268,000 W = 914,400 Btu/hr

**Forklift Load:**
- 6 units × 25 hp average × 2,545 Btu/hr-hp / 0.88 efficiency × 0.70 operating factor
- Q_forklift = 6 × 25 × 2,545 / 0.88 × 0.70 = 306,700 Btu/hr

**Personnel Load:**
- 12 people × (345 Btu/hr sensible × 0.70 clothing + 405 Btu/hr latent) × 0.75 occupancy
- Q_personnel = 12 × (241.5 + 405) × 0.75 = 5,819 Btu/hr

**Motor Load (conveyors):**
- 3 conveyors × 7.5 hp × 2,545 Btu/hr-hp / 0.87 × 0.75 LF × 0.67 time factor
- Q_motors = 3 × 7.5 × 2,545 / 0.87 × 0.75 × 0.67 = 37,000 Btu/hr

**Defrost Load:**
- 2,000 ft² coil × 2.0 W/ft² × 3.412 Btu/hr-W × 4 cycles/day × 0.5 hr / 24 hr
- Q_defrost = 2,000 × 2.0 × 3.412 × 4 × 0.5 / 24 = 2,275 Btu/hr average

**Total Internal Load:**
- Total = 914,400 + 306,700 + 5,819 + 37,000 + 2,275 = 1,266,194 Btu/hr
- With 10% overall safety factor = 1,392,813 Btu/hr = 116 tons refrigeration

This example demonstrates lighting as the dominant internal load, followed by material handling equipment.

## Load Reduction Strategies

Minimizing internal loads reduces operating cost and capital investment:

**Lighting:**
- LED fixtures with occupancy sensing (50-75% reduction)
- High-reflectance surfaces to reduce required lighting levels
- Task lighting instead of area lighting
- Fixtures located outside space with light pipes (specialized applications)

**Material Handling:**
- Electric equipment exclusively (eliminate IC equipment heat)
- Battery charging outside refrigerated space
- Automated systems to reduce equipment operating time
- Equipment sizing optimization to prevent oversized motors

**Personnel:**
- Automated or semi-automated systems to reduce occupancy
- Acclimatization rooms to minimize time in coldest zones
- Efficient workflow to reduce dwell time

**Motors:**
- Premium efficiency motors for continuous operation
- Variable frequency drives for variable loads
- Equipment location outside space when feasible

**Defrost:**
- Demand defrost initiation based on actual frost accumulation
- Temperature termination to prevent over-defrost
- Hot gas defrost instead of electric resistance
- Coil design with wider fin spacing to reduce frost accumulation rate

## References

**ASHRAE Handbook - Refrigeration**, Chapter 24: Refrigerated-Facility Design
- Section on internal loads and heat gains
- Tables for equipment heat release rates
- Personnel metabolic rates at various activity levels

**ASHRAE Handbook - Refrigeration**, Chapter 51: Evaporative Air Cooling
- Evaporator defrost methods and heat requirements

**ASHRAE Handbook - Fundamentals**, Chapter 18: Nonresidential Cooling and Heating Load Calculations
- Motor heat gain calculations
- Lighting heat gain methodology

**ANSI/ASHRAE Standard 15-2022**: Safety Standard for Refrigeration Systems
- Requirements for equipment operating in refrigerated spaces

Design internal loads with detailed operational knowledge. Monitor actual loads during commissioning to verify design assumptions and refine future projects.
