---
title: "Surimi Production"
description: "Temperature control requirements for surimi production including washing water temperature management, dewatering operations, cryoprotectant addition, and block freezing refrigeration loads"
weight: 4
---

Surimi production requires precise temperature control throughout multiple processing stages to preserve myofibrillar proteins, remove impurities, and maintain gel-forming ability. The refrigeration system must manage washing water temperatures, dewatering operations, cryoprotectant addition, and rapid block freezing while handling substantial thermal loads from raw material cooling and mechanical dewatering processes.

## Surimi Production Process Overview

Surimi is refined fish myofibrillar protein concentrate produced from deboned, minced lean whitefish through repeated washing cycles that remove sarcoplasmic proteins, fat, and undesirable compounds. The process transforms raw fish into a stable intermediate product with superior gel-forming properties.

### Process Stages

| Stage | Purpose | Temperature Range | Duration |
|-------|---------|-------------------|----------|
| Raw material reception | Fish intake and sorting | 0-4°C | 15-30 min |
| Deboning/mincing | Mechanical separation | 2-5°C | Continuous |
| Washing cycles | Protein purification | 5-10°C | 20-40 min |
| Dewatering | Moisture reduction | 4-8°C | 5-15 min |
| Refining | Texture improvement | 3-7°C | 2-5 min |
| Cryoprotectant addition | Freeze stability | 5-10°C | 3-8 min |
| Forming | Block shaping | 5-8°C | 1-3 min |
| Freezing | Preservation | -35 to -40°C | 2-4 hours |
| Frozen storage | Long-term holding | -18 to -25°C | Months |

### Process Flow

1. **Heading/gutting**: Remove head, viscera, and scales
2. **Deboning**: Mechanical separation of meat from bones and skin
3. **Mincing**: Size reduction to 3-5 mm particles
4. **Washing**: 2-4 cycles with cold water (water:fish ratio 3:1 to 10:1)
5. **Dewatering**: Centrifugal or screw press moisture removal
6. **Refining**: Final texture development
7. **Cryoprotectant mixing**: Freeze protectant addition (4-8% by weight)
8. **Forming**: Block or log shaping
9. **Plate freezing**: Rapid freezing to -18°C core temperature
10. **Packaging and storage**: -18°C or lower

## Temperature Control Requirements by Stage

### Raw Material Reception and Holding

Fish quality deteriorates rapidly above 4°C. Refrigeration requirements:

**Cooling load for raw material:**
```
Q_raw = m_fish × cp_fish × ΔT + Q_respiration
```

Where:
- Q_raw = cooling load (kW)
- m_fish = fish mass flow rate (kg/s)
- cp_fish = specific heat of fish ≈ 3.5 kJ/(kg·K)
- ΔT = temperature reduction (K)
- Q_respiration = metabolic heat ≈ 0.15 W/kg

**Design parameters:**
- Reception temperature: 5-15°C (depending on harvest method)
- Target holding temperature: 0-2°C
- Holding time: < 6 hours before processing
- Ice:fish ratio: 1:1 to 1:2 for supplemental cooling
- Room temperature: 4-7°C
- Relative humidity: 90-95%

### Deboning and Mincing Operations

Mechanical processing generates heat that must be removed to prevent protein denaturation.

**Heat generation from mechanical work:**
```
Q_mech = P_input × (1 - η) + m_fish × cp_fish × ΔT_friction
```

Where:
- P_input = mechanical power input (kW)
- η = mechanical efficiency (0.60-0.75)
- ΔT_friction = temperature rise from friction (2-4°C)

**Typical refrigeration loads:**
- Deboner/separator: 15-25 kW per 1000 kg/h capacity
- Mincer/grinder: 8-15 kW per 1000 kg/h capacity
- Ambient temperature control: 8-12°C in processing area
- Product temperature after mincing: < 7°C
- Maximum allowable product temperature: 10°C

**Equipment considerations:**
- Chilled water jackets on mincers
- Pre-cooling of equipment
- Insulated product conveyors
- Rapid transfer to washing operations

## Washing Water Temperature Management

Washing water temperature critically affects protein extraction, fat removal, and gel strength development. Temperature must be precisely controlled across multiple wash cycles.

### Washing Cycle Temperature Requirements

| Cycle | Water Temperature | Water:Fish Ratio | Duration | Purpose |
|-------|-------------------|------------------|----------|---------|
| First wash | 8-12°C | 5:1 to 10:1 | 10-15 min | Fat and blood removal |
| Second wash | 5-8°C | 3:1 to 5:1 | 8-12 min | Sarcoplasmic protein removal |
| Third wash | 5-7°C | 2:1 to 3:1 | 5-10 min | Final purification |
| Optional fourth | 3-5°C | 2:1 to 3:1 | 5-8 min | Enhanced whiteness |

### Washing Water Refrigeration System

**Cooling load calculation:**
```
Q_wash = m_water × cp_water × ΔT + Q_product + Q_mixing
```

Where:
- m_water = water flow rate (kg/s)
- cp_water = 4.18 kJ/(kg·K)
- ΔT = temperature rise during washing (3-6°C typical)
- Q_product = heat transfer from fish
- Q_mixing = mechanical mixing heat (5-10% of mixing power)

**Design parameters for 1000 kg/h surimi production:**
- Total water flow: 3000-8000 kg/h (depending on wash cycle)
- Water supply temperature: 3-8°C
- Water return temperature: 8-15°C
- Refrigeration capacity: 40-80 kW
- Chilled water storage: 5000-10000 L at 2-4°C
- Water recirculation rate: 30-50% (after screening and filtration)

### Chilled Water System Configuration

**Primary refrigeration:**
- Ammonia or R-507A screw compressor package
- Plate-and-frame heat exchangers for water chilling
- Evaporating temperature: -5 to -2°C
- Glycol secondary loop for freeze protection
- Variable speed pumping for demand matching

**Water distribution:**
- Insulated distribution headers (50-100 mm diameter)
- Temperature sensors at each wash tank
- Modulating control valves for temperature regulation
- Mixing nozzles for uniform temperature distribution
- Overflow and drainage systems

**Temperature control strategy:**
- Feed-forward control based on fish flow rate
- Cascade control: water temperature master, valve position slave
- Wash cycle sequencing with temperature verification
- Alarm at ±2°C from setpoint

## Dewatering and Refining Temperature Needs

Dewatering reduces moisture content from 85-90% to 75-82% while maintaining low temperature to prevent protein denaturation and bacterial growth.

### Dewatering Operations

**Centrifugal dewatering:**
- Feed temperature: 5-8°C
- Discharge temperature: < 10°C
- G-force: 1000-3000 × g
- Residence time: 1-3 minutes
- Heat generation: 8-12 kW per 1000 kg/h
- Final moisture: 78-82%

**Screw press dewatering:**
- Feed temperature: 4-7°C
- Discharge temperature: < 9°C
- Pressure: 200-400 kPa
- Heat generation: 5-8 kW per 1000 kg/h
- Final moisture: 75-80%

### Refrigeration Requirements

**Cooling load for dewatering:**
```
Q_dewater = Q_mechanical + Q_friction + m_surimi × cp × ΔT
```

Typical values per 1000 kg/h:
- Mechanical heat: 8-12 kW
- Friction heat: 3-5 kW
- Product temperature rise: 2-4°C
- Total refrigeration: 15-20 kW
- Room cooling: 10-15 kW

**Temperature control methods:**
- Chilled water jacketing on dewatering equipment
- Direct expansion coils in processing room
- Cooled air circulation (8-12°C)
- Chilled discharge conveyors
- Rapid transfer to refining operations

### Refining Operations

Refining improves texture and removes remaining impurities through mechanical working.

**Temperature management:**
- Feed temperature: 5-8°C
- Target discharge temperature: < 10°C
- Mechanical heat input: 10-15 kW per 1000 kg/h
- Refrigeration requirement: 12-18 kW per 1000 kg/h
- Ambient temperature: 10-14°C

**Quality indicators affected by temperature:**
- Gel strength: Maximum at 5-8°C processing
- Whiteness: Improved at lower temperatures
- Water holding capacity: Optimal at 4-7°C
- Texture: Finer at controlled temperatures < 10°C

## Cryoprotectant Addition Temperature

Cryoprotectants (sugar, sorbitol, polyphosphates) protect myofibrillar proteins during frozen storage by preventing protein denaturation and moisture migration.

### Cryoprotectant Formulations

| Component | Concentration | Function | Temperature Impact |
|-----------|---------------|----------|-------------------|
| Sucrose | 2-4% | Protein protection | Dissolves readily at 5-15°C |
| Sorbitol | 2-4% | Texture improvement | Viscosity increases < 5°C |
| Polyphosphates | 0.2-0.3% | Water binding | Activity optimized at 8-12°C |
| Salt | 0-0.3% | Taste and texture | Soluble at all process temps |

### Mixing Requirements

**Temperature control during mixing:**
- Surimi temperature before mixing: 5-8°C
- Cryoprotectant solution temperature: 10-15°C
- Mixed product temperature: 7-10°C
- Mixing time: 3-8 minutes
- Mechanical heat generation: 3-5 kW per 1000 kg/h

**Thermal balance:**
```
T_final = (m_surimi × cp_surimi × T_surimi + m_cryo × cp_cryo × T_cryo) / (m_surimi × cp_surimi + m_cryo × cp_cryo)
```

**Design considerations:**
- Vacuum mixing to reduce air incorporation
- Jacketed mixer with chilled water circulation (5-10°C)
- Temperature monitoring and control
- Batch time minimization (< 10 minutes total)
- Rapid transfer to forming operations

## Freezing Requirements for Surimi Blocks

Rapid freezing preserves protein functionality and prevents large ice crystal formation that damages protein structure.

### Plate Freezer Systems

**Design parameters:**
- Plate surface temperature: -35 to -40°C
- Product core temperature: -18°C minimum (-25°C preferred)
- Block thickness: 50-75 mm typical
- Freezing time: 2-4 hours
- Plate pressure: 50-100 kPa

**Heat transfer calculation:**
```
Q_freezing = m × [cp_unfrozen × (T_initial - T_freezing) + L_f + cp_frozen × (T_freezing - T_final)]
```

Where:
- L_f = latent heat of fusion ≈ 280 kJ/kg for surimi (80% moisture)
- cp_unfrozen ≈ 3.5 kJ/(kg·K)
- cp_frozen ≈ 1.9 kJ/(kg·K)
- T_freezing ≈ -1.5°C (depression due to solutes)

**Example calculation for 10 kg block:**
- Sensible cooling (8°C to -1.5°C): 10 × 3.5 × 9.5 = 333 kJ
- Latent heat: 10 × 280 = 2800 kJ
- Subcooling (-1.5°C to -20°C): 10 × 1.9 × 18.5 = 352 kJ
- Total heat removal: 3485 kJ
- Average freezing rate: 3485 kJ / (3 h × 3600 s/h) = 0.32 kW per block

**Plate freezer refrigeration load (20 blocks capacity):**
- Product load: 20 × 0.32 = 6.4 kW average (12-15 kW peak)
- Equipment thermal mass: 8-12 kW
- Infiltration and door openings: 3-5 kW
- Safety factor: 1.15-1.25
- **Total design load: 25-35 kW**

### Contact Freezing Heat Transfer

**Heat flux through surimi block:**
```
q = (T_plate - T_core) / (R_contact + R_product + R_package)
```

Where:
- R_contact = contact resistance ≈ 0.0001-0.0003 m²·K/W
- R_product = x / k_surimi (k ≈ 1.2-1.8 W/(m·K) depending on temperature)
- R_package = plastic film resistance ≈ 0.00005 m²·K/W

**Thermal conductivity of surimi:**
- Unfrozen (0 to 10°C): k = 0.45-0.55 W/(m·K)
- Partially frozen (-5 to 0°C): k = 0.8-1.2 W/(m·K)
- Frozen (< -10°C): k = 1.5-2.0 W/(m·K)

### Alternative Freezing Methods

**Air blast freezing:**
- Air temperature: -35 to -40°C
- Air velocity: 3-5 m/s
- Freezing time: 4-8 hours (slower than plate)
- Load: 1.5-2× plate freezer for same capacity
- Lower capital cost, higher operating cost

**Cryogenic freezing:**
- Liquid nitrogen or CO₂
- Surface temperature: -50 to -100°C
- Freezing time: 20-40 minutes
- Very high operating cost
- Used for premium products or rapid startup needs

## Frozen Storage Requirements

Frozen surimi storage maintains product quality during distribution and before secondary processing into seafood analogs.

### Storage Conditions

| Parameter | Standard Grade | Premium Grade | Ultra-Premium |
|-----------|----------------|---------------|---------------|
| Temperature | -18 to -20°C | -20 to -25°C | -25 to -30°C |
| Temperature tolerance | ±2°C | ±1°C | ±0.5°C |
| Storage duration | 6-9 months | 9-12 months | 12-18 months |
| Gel strength retention | 85-90% | 90-95% | > 95% |

**Refrigeration load for 500 tonne capacity:**
- Product respiration: Negligible
- Air infiltration: 15-25 kW
- Transmission load: 25-40 kW
- Internal lighting: 2-5 kW
- Forklift operation: 8-15 kW
- Door openings: 5-10 kW
- Evaporator fans: 8-12 kW
- **Total design load: 75-120 kW**

### Temperature Cycling Effects

Temperature fluctuations cause quality degradation through ice recrystallization and protein denaturation.

**Gel strength loss rate:**
```
ΔGS/Δt = k × f(T,ΔT,t_cycle)
```

Where:
- ΔGS = gel strength loss (g·cm)
- k = rate constant (species-dependent)
- f(T,ΔT,t_cycle) = function of average temperature, temperature swing, cycle frequency

**Typical degradation rates:**
- At -18°C steady: 1-2% gel strength loss per month
- With ±3°C cycling weekly: 3-5% loss per month
- At -25°C steady: 0.5-1% loss per month

### Storage Room Design

**Configuration:**
- Ceiling height: 8-12 m for racked storage
- Aisle width: 3.5-4.5 m for forklift access
- Floor loading: 15-25 kPa
- Insulation thickness: 200-300 mm polyurethane (U = 0.12-0.18 W/(m²·K))
- Vapor barrier: Continuous on warm side
- Refrigeration: Ammonia or low-GWP refrigerant evaporators
- Evaporator TD: 8-12°C (wider = more economical, narrower = better control)
- Defrost: Hot gas or electric, 2-4 cycles per day

## Equipment Refrigeration Loads

Complete refrigeration system must handle all processing areas and cold storage simultaneously.

### Load Summary by Area

| Processing Area | Refrigeration Capacity | Temperature | Equipment Type |
|-----------------|------------------------|-------------|----------------|
| Raw material holding | 15-25 kW | 0-4°C | DX or secondary glycol |
| Processing room cooling | 40-60 kW | 8-12°C | Chilled air or glycol |
| Wash water system | 50-80 kW | 3-8°C supply | Chilled water, plate HX |
| Dewatering/refining | 25-35 kW | 5-10°C product | Jacketed equipment |
| Plate freezers | 30-50 kW | -35°C plates | Direct ammonia or cascade |
| Frozen storage | 80-120 kW | -20 to -25°C | Ammonia evaporators |
| **Total design load** | **240-370 kW** | Multiple temps | Centralized plant |

### Central Refrigeration Plant Sizing

**Compressor selection for multi-stage plant:**

1. **High-stage (processing areas, -5 to +5°C):**
   - Load: 150-220 kW
   - Evaporating temperature: -2 to 0°C
   - Condensing temperature: 35-40°C
   - Compressor type: Screw or reciprocating
   - Refrigerant: Ammonia or R-507A

2. **Low-stage (freezing and frozen storage, -40 to -25°C):**
   - Load: 110-170 kW
   - Evaporating temperature: -40 to -35°C
   - Suction from low-temp evaporators
   - Discharge to inter-cooler or high-stage suction
   - Two-stage compression or cascade system

**System COP by configuration:**
- Single-stage to -40°C: COP = 0.8-1.2
- Two-stage compound: COP = 1.4-1.8
- Cascade with CO₂ low stage: COP = 1.2-1.6
- Two-stage with economizer: COP = 1.6-2.0

## Energy Optimization Strategies

### Heat Recovery Opportunities

**Condenser heat recovery:**
```
Q_recovery = m_refrigerant × (h_discharge - h_condensed)
```

**Applications:**
- Space heating for administrative areas (20-30% of condenser heat)
- Process water preheating (limited application due to water temperature requirements)
- Floor heating in frozen storage entrance areas
- Defrost heat for evaporators (hot gas defrost)

**Typical recovery potential:**
- Compressor heat rejection: 1.3-1.5 × refrigeration load
- Recoverable fraction: 30-50% under favorable conditions
- Payback period: 2-4 years for integrated system

### Variable Load Management

Surimi production operates in batch modes with varying refrigeration demands.

**Load profiles:**
- Washing cycles: Intermittent, high flow rate
- Dewatering/refining: Continuous during production shift
- Plate freezing: Batch loading, continuous cooling
- Frozen storage: Constant base load

**Optimization strategies:**
1. **Thermal storage for wash water:**
   - Ice bank or chilled water tank (5000-10000 L)
   - Build reserve during low-load periods
   - Reduce peak compressor capacity by 20-30%
   - Improve energy efficiency through load shifting

2. **Variable speed compressors:**
   - Match capacity to instantaneous load
   - Reduce cycling losses
   - Energy savings: 15-25% vs. step control
   - Better temperature control

3. **Floating condensing pressure:**
   - Lower condensing temperature with ambient
   - Each 1°C reduction → 2-3% COP improvement
   - Control limits: oil return, pressure ratio
   - Savings: 10-20% annually in moderate climates

4. **Evaporator optimization:**
   - Variable speed fans (30-50% fan energy savings)
   - Scheduled defrost based on coil performance
   - Maintain clean coils (annual cleaning)
   - TD optimization: 8-10°C typical for storage

### Process Integration

**Coordinated operation:**
- Sequence washing cycles to minimize peak demand
- Stagger plate freezer loading
- Schedule defrost during low-load periods
- Pre-cooling strategies using frozen storage capacity

**Energy monitoring:**
- Specific energy consumption (SEC): kWh per kg surimi produced
- Target SEC: 0.4-0.6 kWh/kg for modern plants
- Benchmark components: refrigeration 60-70%, processing 20-25%, auxiliary 10-15%
- Continuous monitoring and optimization

## Quality Parameters and Temperature Impact

### Gel Strength Development

Gel strength is the primary quality indicator for surimi, measured in g·cm (gel breaking force × penetration depth).

**Temperature effects on gel strength:**

| Processing Temperature | Relative Gel Strength | Protein Denaturation |
|------------------------|----------------------|----------------------|
| 0-5°C | 100% (optimal) | Minimal |
| 5-10°C | 95-100% | Very low |
| 10-15°C | 85-95% | Low to moderate |
| 15-20°C | 70-85% | Moderate |
| > 20°C | < 70% | High |

**Mechanisms:**
- Myosin denaturation begins above 15°C
- Actomyosin complex stability decreases with temperature
- Enzymatic degradation accelerates above 10°C
- Oxidation reactions increase exponentially with temperature

### Whiteness Retention

Whiteness is critical for visual appeal and marketability.

**L* value targets:**
- Fresh surimi: L* = 75-82
- Frozen surimi (6 months, -20°C): L* > 72
- Processing temperature impact: +1°C average → -0.5 to -1.0 L* units

**Contributing factors:**
- Lipid oxidation (temperature-dependent)
- Myoglobin oxidation to metmyoglobin
- Maillard reactions (minimal at low temperatures)
- Melanin formation from enzymatic browning

### Moisture Content and Water Holding Capacity

**Target moisture content:**
- Standard grade: 75-78%
- Premium grade: 78-82%
- Control tolerance: ±1%

**Temperature influence:**
- Dewatering efficiency decreases below 3°C (high viscosity)
- Optimal dewatering: 5-8°C
- Water holding capacity (WHC) maximized at 4-7°C processing
- Freeze-thaw cycles reduce WHC by 10-20%

### Microbial Control

Temperature control is the primary barrier against microbial growth and toxin production.

**Critical control points:**
- Reception: < 4°C (< 2 hours above 7°C)
- Processing: < 10°C throughout (< 1 hour above 15°C)
- Post-cryoprotectant: < 10°C (freeze within 2 hours)
- Frozen storage: < -18°C (no thawing events)

**Microbial growth rates:**
- Psychrotrophic bacteria double time at 4°C: 10-15 hours
- At 10°C: 4-6 hours
- At 15°C: 2-3 hours
- Freezing: Growth essentially stops, but survival continues

### Protein Functionality

**Critical functional properties:**
1. **Gel-forming ability**: Maintained at < 10°C processing
2. **Emulsifying capacity**: Optimal at 5-8°C
3. **Water binding**: Maximum at 4-7°C
4. **Texture development**: Best at controlled temperatures

**Temperature-time integration:**
```
TTI = Σ(t_i × e^(T_i / T_ref))
```

Where:
- TTI = temperature-time indicator
- t_i = time interval
- T_i = temperature during interval
- T_ref = reference temperature (often 0°C)

Target: TTI < 150°C·minutes from reception to freezing

## Process Monitoring and Control

### Critical Measurement Points

**Temperature monitoring:**
- Raw material holding: 3-5 sensors per holding area
- Wash water supply and return: Each cycle monitored
- Product temperature: After each processing stage
- Plate freezer: Core temperature verification (sample basis)
- Storage rooms: Multi-point monitoring (ceiling, mid-level, floor)

**Data logging requirements:**
- Sampling frequency: 1-5 minutes for process areas
- Retention period: Minimum 1 year
- Alarm levels: ±2°C from setpoint for critical areas
- HACCP documentation compliance

### Automation and Control Systems

**Process control hierarchy:**
1. **Equipment level**: PLC control of individual machines
2. **Production line**: Coordinated sequencing of process stages
3. **Plant level**: Central SCADA monitoring and optimization
4. **Enterprise level**: Quality data integration and analysis

**Advanced control strategies:**
- Model predictive control for refrigeration plant
- Feed-forward wash water temperature control
- Adaptive defrost scheduling
- Energy optimization algorithms

---

**File:** `/Users/evgenygantman/Documents/github/gantmane/hvac/content/refrigeration-systems/food-processing-refrigeration/fishery-products/seafood-processing-operations/surimi-production/_index.md`

This enhanced content provides HVAC professionals with comprehensive technical guidance on refrigeration requirements for surimi production, including detailed temperature control parameters, equipment sizing calculations, energy optimization strategies, and quality control considerations.
