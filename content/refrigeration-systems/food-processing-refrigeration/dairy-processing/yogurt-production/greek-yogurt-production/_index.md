---
title: "Greek Yogurt Production"
aliases: ["Greek Yogurt Production"]
description: "HVAC and refrigeration requirements for Greek yogurt manufacturing including straining processes, whey separation, acid whey cooling, and process room environmental control for concentrated dairy products"
weight: 3
---

Greek yogurt production requires specialized refrigeration systems to manage the straining process, handle large volumes of acid whey byproduct, and maintain product quality during concentration. The higher protein content (typically 9-10% compared to 3-4% in regular yogurt) results from removing approximately 50-60% of the liquid volume as whey, creating unique thermal management challenges.

## Straining Process Fundamentals

### Mechanical Separation Methods

Greek yogurt straining removes liquid whey to concentrate proteins and solids. Three primary separation technologies are employed:

| Separation Method | Whey Removal Rate | Protein Retention | Energy Use | Capital Cost |
|-------------------|-------------------|-------------------|------------|--------------|
| Centrifugal Separation | 1000-3000 L/hr per unit | 98-99% | 15-25 kW per separator | High |
| Membrane Filtration (UF) | 500-2000 L/hr per module | 99.5%+ | 8-12 kW per module | Very High |
| Gravity Drainage (Batch) | 50-150 L/hr per vat | 95-97% | Minimal | Low |

**Centrifugal separators** use rotational force (3000-7000 RPM) to partition whey from concentrated yogurt based on density differences. Bowl temperatures must remain between 4-10°C to maintain product viscosity while preventing microbial growth.

**Ultrafiltration systems** employ membrane pores of 0.01-0.1 μm to retain proteins while allowing water, lactose, and minerals to pass. Transmembrane pressure typically operates at 200-400 kPa.

### Temperature Control During Straining

The straining process generates frictional heat that must be removed to maintain product quality and prevent acid development:

**Temperature Rise from Mechanical Work:**

ΔT = W / (m × cp)

Where:
- W = mechanical work input (kJ)
- m = product mass flow rate (kg/s)
- cp = specific heat capacity of yogurt ≈ 3.8 kJ/(kg·K)

For a centrifugal separator processing 2000 kg/hr with 20 kW power input:

ΔT = (20 kJ/s × 3600 s/hr) / (2000 kg/hr × 3.8 kJ/(kg·K)) = 9.5°C/hr

**Cooling Requirements:**

Pre-straining yogurt temperature: 4-8°C
Maximum allowable product temperature: 10°C
Post-straining target temperature: 4-6°C

Continuous cooling during straining prevents:
- Excessive acid development (target pH 4.4-4.6)
- Culture over-activity
- Protein denaturation
- Texture degradation

### Process Cooling Integration

**Jacketed Separator Bowls:**

Cooling glycol at -2 to 2°C circulates through separator jackets at 20-30 L/min. Heat removal capacity:

Q = ṁ × cp × ΔT

For glycol flow:
Q = (25 kg/min × 60 min/hr) × 3.5 kJ/(kg·K) × 8°C = 42,000 kJ/hr = 11.7 kW

**Plate Heat Exchangers (Post-Straining):**

Greek yogurt viscosity (8,000-15,000 cP at 5°C) requires specialized plate designs:
- Wide gap plates (6-12 mm spacing)
- Low shear rate flow (< 50 s⁻¹)
- Surface area: 2-4 m² per 1000 kg/hr capacity
- Approach temperature: 2-3°C

Refrigerant side: R-507A or ammonia at -5 to 0°C
Product side: cooling from 8-10°C to 4-6°C

## Whey Management Systems

### Acid Whey Production Volumes

Greek yogurt straining generates substantial acid whey volumes:

**Mass Balance:**

For 1000 kg finished Greek yogurt:
- Starting regular yogurt required: 2200-2500 kg
- Whey removed: 1200-1500 kg (54-60% of initial mass)
- Typical composition: 93-94% water, 0.8-1.0% protein, 4-5% lactose, pH 4.3-4.5

### Immediate Cooling Requirements

Acid whey exits straining operations at 6-12°C but must be cooled rapidly to prevent spoilage and control odor:

**Target Storage Temperature:** 2-4°C
**Cooling Time Requirement:** Within 2 hours of separation

**Cooling Load Calculation:**

Q = m × cp × ΔT + Qrespiration

For 10,000 kg/day whey production cooled from 10°C to 3°C:

Q = (10,000 kg × 3.9 kJ/(kg·K) × 7°C) / (2 hr × 3600 s/hr)
Q = 273,000 kJ / 7200 s = 37.9 kW cooling capacity required

Add 15-20% safety factor: **45 kW refrigeration capacity**

### Whey Cooling System Design

**Option 1: Direct Expansion Tank Cooling**

Insulated storage tanks (5,000-20,000 L capacity) with:
- Internal DX coils (stainless steel 316L)
- Evaporator temperature: -3 to 0°C
- Surface area: 0.8-1.2 m² per 1000 L
- Agitation: 30-50 RPM slow-speed mixers
- Insulation: 100-150 mm polyurethane foam (R-30 to R-45)

**Option 2: Plate Heat Exchanger with Glycol Loop**

Pre-cooling system upstream of storage:
- Plate PHE: 50-80 m² surface area for 10,000 kg/day
- Glycol temperature: -2 to 1°C
- Flow rate: whey 8-12 m³/hr, glycol 10-15 m³/hr
- Pressure drop: < 100 kPa product side
- CIP capability: 85°C hot water circulation

**Option 3: Falling Film Chiller**

For large operations (>50,000 kg whey/day):
- Vertical shell-and-tube design
- Ammonia evaporator at -5°C
- Whey film thickness: 0.5-1.5 mm
- Heat transfer coefficient: 1500-2500 W/(m²·K)
- Minimal fouling due to turbulent film flow

### Acid Whey Storage Refrigeration

**Short-Term Storage (1-7 days):**

Refrigerated tanks maintain 2-4°C:
- Tank volume: 1.5-3 days production capacity
- Heat infiltration: 8-12 W/m² through insulation
- Agitation heat: 0.5-1.0 kW per 10,000 L
- Pump circulation heat: 2-4 kW per transfer event

**Total cooling load per 20,000 L tank:**

Qtank = Qinfiltration + Qagitation + Qproduct

- Qinfiltration = 10 W/m² × 40 m² = 400 W
- Qagitation = 0.75 kW = 750 W
- Qproduct = 37.9 kW (during filling only)

Continuous load: 1.15 kW per tank
Peak load during filling: 39 kW

### Whey Processing Alternatives

**Concentration for Transport:**

Reverse osmosis (RO) systems concentrate acid whey to 18-25% solids:
- Reduces transport volume by 70-80%
- Operating temperature: 4-10°C (chilled feed required)
- Membrane cooling: 15-25 kW per 5000 L/hr capacity
- Permeate can be discharged (lower BOD)

**Spray Drying:**

Convert liquid whey to powder:
- Feed temperature: 45-60°C (heating required)
- Outlet temperature: 80-95°C
- Substantial energy input: 4000-5500 kJ/kg water removed
- Requires large cooling water systems for exhaust condensers

## Protein Concentration Impact on Refrigeration

### Higher Thermal Mass

Greek yogurt's increased solids content (23-26% vs. 12-15% regular) affects thermal properties:

| Property | Regular Yogurt | Greek Yogurt | Impact |
|----------|---------------|--------------|---------|
| Specific Heat | 3.85 kJ/(kg·K) | 3.65 kJ/(kg·K) | 5% less cooling energy |
| Thermal Conductivity | 0.54 W/(m·K) | 0.48 W/(m·K) | Slower heat transfer |
| Density | 1030 kg/m³ | 1060 kg/m³ | More mass per volume |
| Freezing Point | -0.5°C | -0.8°C | Lower crystallization risk |

**Cooling Time Implications:**

For equal volume cooling in storage cups (150 mL):

τ = (ρ × V × cp) / (h × A × ΔT)

Where:
- τ = cooling time constant (seconds)
- ρ = product density (kg/m³)
- V = volume (m³)
- h = heat transfer coefficient (W/(m²·K))
- A = surface area (m²)

Greek yogurt requires 8-12% longer cooling time due to higher density and lower thermal conductivity.

### Increased Viscosity Effects

Greek yogurt viscosity (8,000-15,000 cP) is 5-8× higher than regular yogurt (1,500-2,500 cP):

**Pumping Power Requirements:**

ΔP = (32 × μ × L × v) / D²

For laminar flow (Re < 2100):
- μ = dynamic viscosity (Pa·s)
- L = pipe length (m)
- v = velocity (m/s)
- D = pipe diameter (m)

A 50 mm pipe carrying Greek yogurt at 0.5 m/s over 20 m:

ΔP = (32 × 12 Pa·s × 20 m × 0.5 m/s) / (0.05 m)² = 1,536,000 Pa = 15.4 bar

High pressure drop generates heat: Qpump = ṁ × ΔP / ρ

This heat must be removed by downstream cooling.

### Cold Chain Maintenance

Greek yogurt's higher protein concentration makes it more susceptible to temperature abuse:

**Shelf Life vs. Storage Temperature:**

| Storage Temperature | Expected Shelf Life | Microbial Risk Level |
|---------------------|---------------------|---------------------|
| 2-3°C | 50-60 days | Very Low |
| 4-5°C | 40-45 days | Low |
| 6-7°C | 28-35 days | Moderate |
| 8-10°C | 14-21 days | High |
| >10°C | <14 days | Very High |

Distribution refrigeration must maintain ≤4°C continuously.

## Post-Straining Cooling Systems

### Filled Cup Cooling Tunnels

After filling and sealing, Greek yogurt cups pass through cooling tunnels:

**Spiral Conveyor Tunnels:**

- Retention time: 60-90 minutes
- Air temperature: 0-2°C
- Air velocity: 2.5-3.5 m/s across product
- Relative humidity: 85-90% (prevents condensation)
- Temperature reduction: 22-25°C down to 6-8°C

**Cooling Load Calculation:**

For 10,000 cups/hour (150 g per cup):

Qproduct = ṁ × cp × ΔT
Qproduct = (10,000 cups/hr × 0.15 kg/cup) × 3.65 kJ/(kg·K) × 18°C
Qproduct = 9,855 kJ/hr = 2.74 kW

Total tunnel cooling requirement with infiltration, conveyors, fans:
**Qtotal = 12-15 kW for 10,000 cups/hr**

### Blast Cooling Rooms

Batch cooling in palletized configuration:

- Room temperature: 0-2°C
- Air changes: 30-50 per hour
- Cooling time: 12-18 hours (pallet load to core)
- Evaporator ΔT: 8-10°C
- Coil face velocity: 2.5-3.0 m/s

**Room sizing:** 0.15-0.20 m³ per kg daily production

For 20,000 kg/day production: 3,000-4,000 m³ blast room

Refrigeration load: 60-80 kW (including product, infiltration, lighting, fans)

### Cold Storage Warehousing

Finished Greek yogurt storage at 2-4°C:

**Storage Density:**

- Pallet dimensions: 1.2 m × 1.0 m × 1.4 m high
- Weight per pallet: 600-800 kg product
- Storage height: 5-7 pallet levels (rack system)
- Aisle width: 3.0-3.5 m (forklift access)

**Heat Load Components:**

| Load Source | Specific Load | Calculation Basis |
|-------------|---------------|-------------------|
| Transmission | 8-12 W/m² | Wall/ceiling/floor area |
| Infiltration | 3-5 W/m² | Door openings, traffic |
| Product cooling | 0.5-0.8 W/kg | Daily throughput |
| Lighting | 5-8 W/m² | Floor area |
| People/equipment | 250 W per person | Occupancy |
| Fans | 15-20% | Of total cooling load |

Typical cold storage: **12-18 W/m³** total refrigeration load

## Process Room HVAC Design

### Environmental Requirements

Greek yogurt straining and filling areas require controlled environments:

| Parameter | Specification | Rationale |
|-----------|---------------|-----------|
| Temperature | 10-15°C | Prevent product warming, reduce microbial growth |
| Relative Humidity | 50-60% | Minimize condensation, mold control |
| Air Changes | 15-20 per hour | Odor control, heat removal |
| Pressurization | +5 to +15 Pa | Prevent contamination ingress |
| Filtration | MERV 13-14 minimum | Particulate control |
| Air Velocity | <0.25 m/s at workstations | Prevent draughts, no product surface drying |

### Space Heat Load Analysis

**Heat Sources in Straining Room:**

1. **Equipment Heat Dissipation:**
   - Centrifugal separators: 15-25 kW per unit
   - UF membrane pumps: 8-12 kW per system
   - Conveyors/agitators: 3-8 kW total
   - Control panels: 1-2 kW

2. **Product Heat Release:**
   - Warm yogurt entering: Q = ṁ × cp × (Tproduct - Troom)
   - For 5000 kg/hr at 8°C in 12°C room: 5.1 kW

3. **Personnel Load:**
   - 120-150 W per person (light work)
   - 8-12 operators typical: 1.0-1.8 kW

4. **Lighting:**
   - LED fixtures: 8-12 W/m²
   - 500 m² process area: 4-6 kW

**Total Cooling Load:** 50-75 kW for typical straining operation

### Air Distribution Systems

**Overhead Laminar Flow:**

- Supply diffusers: perforated ceiling panels
- Supply temperature: 8-10°C
- Throw pattern: vertical downward at 0.3-0.5 m/s
- Return: low wall grilles at 0.5 m above floor
- Ductwork: stainless steel 304L, fully welded seams

**Displacement Ventilation Alternative:**

- Low-velocity wall-mounted diffusers (0.15-0.25 m/s)
- Supply temperature: 10-12°C (higher than conventional)
- Temperature stratification maintained
- Contaminants rise to high-level exhaust
- Better energy efficiency (15-25% reduction vs. mixing)

### Humidity Control Systems

**Dehumidification Load:**

Process rooms gain moisture from:
- Product evaporation: minimal (covered vessels)
- Personnel: 50-80 g/hr per person
- Infiltration: dependent on door traffic
- Washing operations: 200-500 g/hr per wash station

**Target moisture removal:** 10-20 kg/day for 500 m² room

**Dehumidification Methods:**

1. **Chilled Water Coils:**
   - Apparatus dewpoint: 6-8°C
   - Requires reheat to avoid overcooling
   - Energy penalty: 20-30%

2. **Desiccant Dehumidification:**
   - Silica gel or molecular sieve wheels
   - Regeneration at 80-120°C
   - Isothermal moisture removal
   - Higher energy use but better control

3. **Hybrid Systems:**
   - Chilled coils for sensible cooling
   - Desiccant for latent load
   - Optimized energy consumption
   - Precise humidity control (±3% RH)

## Refrigeration Equipment Specifications

### Compressor Selection

**Load Profile Considerations:**

Greek yogurt production has varying refrigeration demands:

| Time Period | Process Load | Whey Cooling | Storage | Total |
|-------------|--------------|--------------|---------|-------|
| Production (16 hr) | 80-100 kW | 35-45 kW | 60 kW | 175-205 kW |
| Non-production (8 hr) | 0 kW | 5-10 kW | 60 kW | 65-70 kW |

**Capacity Control Requirements:**

Variable load requires modulating capacity:
- Reciprocating: 100-75-50-25% unloading
- Screw: continuous 10-100% slide valve
- Scroll: staged multiple compressors
- Centrifugal: variable speed drive (VSD)

**Recommended Configuration:**

- Base load: 70 kW screw compressor (continuous operation)
- Peak load: 2 × 60 kW reciprocating (production hours only)
- Redundancy: N+1 design (one spare compressor)

### Evaporator Systems

**Glycol Secondary Loop:**

Advantages for dairy processing:
- Single refrigeration plant location
- No ammonia in process areas
- Temperature stability (thermal mass)
- Simplified equipment cleaning

**System Design:**

- Glycol concentration: 30-35% propylene glycol
- Operating temperature: -5 to 0°C
- Flow rate: 0.02-0.03 L/s per kW cooling
- Piping: Schedule 40 carbon steel with glycol-compatible inhibitors
- Pump redundancy: 2 × 100% capacity

**Evaporator Sizing:**

For 150 kW total load at -2°C glycol:

LMTD = (ΔT₁ - ΔT₂) / ln(ΔT₁/ΔT₂)

Where:
- ΔT₁ = Tglycol,in - Trefrigerant = (-2°C) - (-10°C) = 8°C
- ΔT₂ = Tglycol,out - Trefrigerant = (-5°C) - (-10°C) = 5°C

LMTD = (8 - 5) / ln(8/5) = 6.4°C

Required UA: Q / LMTD = 150 kW / 6.4 K = 23.4 kW/K

For U = 800 W/(m²·K): A = 23,400 / 800 = 29.3 m² evaporator surface area

### Condensing Systems

**Heat Rejection Options:**

| System Type | Approach Temp | Water Usage | Energy Use | Capital Cost |
|-------------|---------------|-------------|------------|--------------|
| Evaporative Condenser | 8-10°C | 2-3 L/hr per kW | Lowest | Medium |
| Air-Cooled Condenser | 12-15°C | None | Highest | Low |
| Cooling Tower + Shell-Tube | 6-8°C | 4-5 L/hr per kW | Low | Highest |

**Selection Criteria:**

For 200 kW refrigeration load:
- Heat rejection: 200 kW × 1.25 (compressor heat) = 250 kW
- Evaporative condenser: 1-1.2 kW fan power
- Air-cooled: 6-8 kW fan power

**Energy analysis favors evaporative condensing in most climates.**

### Refrigerant Selection

**Options for Dairy Processing:**

| Refrigerant | Advantages | Disadvantages | Application |
|-------------|-----------|---------------|-------------|
| R-717 (Ammonia) | Excellent efficiency, low cost, natural | Toxic, code restrictions in process areas | Central plant only |
| R-507A | Good capacity, non-flammable | High GWP (3985), phasing out | Legacy systems |
| R-134a | Low toxicity, established use | Lower efficiency, moderate GWP | Small DX systems |
| R-744 (CO₂) | Natural, non-toxic, low GWP | High pressures, complex controls | Cascade systems |

**Current best practice:** Ammonia central plant with glycol distribution

## Energy Efficiency Strategies

### Heat Recovery Systems

**Compressor Heat Recovery:**

Refrigeration compressors reject heat at 60-90°C (discharge gas) and 30-45°C (oil cooling):

**Application: Hot Water Generation**

Recovered heat warms water for CIP (Clean-in-Place) operations:
- CIP water requirement: 60-85°C
- Preheat from 15°C to 45-50°C using compressor heat
- Heat recovery potential: 30-40% of refrigeration energy

**Calculation:**

For 150 kW refrigeration load at COP 3.5:
- Compressor power: 150 / 3.5 = 42.9 kW
- Total heat rejection: 150 + 42.9 = 192.9 kW
- Recoverable heat (70%): 135 kW

If CIP uses 5000 L/day heated 30°C:
Energy needed: 5000 kg × 4.18 kJ/(kg·K) × 30°C = 627,000 kJ/day = 7.26 kW average

**Heat recovery covers 100% of preheat demand with excess available.**

### Variable Speed Drives

**VSD Applications:**

1. **Compressors:** Match capacity to actual load
   - Energy savings: 20-35% vs. on/off control
   - Reduced cycling wear
   - Better temperature stability

2. **Glycol Pumps:** Flow matches heat load
   - Energy savings: 30-50% (pump laws: power ∝ flow³)
   - Reduced pressure drop
   - Lower noise

3. **Evaporator Fans:** Modulate airflow to load
   - Energy savings: 40-60%
   - Better humidity control
   - Reduced frosting

**Example Energy Savings:**

Baseline: 200 kW refrigeration with constant-speed equipment
- Compressors: 60 kW average
- Pumps: 12 kW
- Fans: 18 kW
- Total: 90 kW average auxiliary power

With VSD optimization:
- Compressors: 42 kW (30% reduction)
- Pumps: 7 kW (42% reduction)
- Fans: 9 kW (50% reduction)
- Total: 58 kW (36% reduction)

**Annual savings:** (90 - 58) kW × 6000 hr/yr × $0.12/kWh = $23,040/year

### Free Cooling Integration

**Ambient Conditions Utilization:**

When outdoor temperature <5°C, use ambient air for cooling:

**Glycol Free Cooling:**

Dry cooler directly cools glycol loop:
- Effective when Tambient < (Tglycol,setpoint - 3°C)
- Example: Cool glycol to 0°C when Tambient < -3°C
- Compressor energy eliminated during these periods

**Climate Analysis (Example: Midwest US):**

| Month | Hours <-3°C | Potential Free Cooling Hours | Energy Savings |
|-------|-------------|------------------------------|----------------|
| January | 180 | 150 | 9,000 kWh |
| February | 160 | 130 | 7,800 kWh |
| March | 80 | 60 | 3,600 kWh |
| November | 45 | 35 | 2,100 kWh |
| December | 140 | 115 | 6,900 kWh |
| **Annual Total** | **605** | **490** | **29,400 kWh** |

At $0.12/kWh: **$3,528 annual savings**

### Thermal Storage

**Ice Bank Systems:**

Build ice during off-peak hours (lower electric rates):
- Ice builds at night: 8-10 hour charging
- Ice melts during production: 12-16 hour discharge
- Glycol circulation through ice tank
- Tank volume: 0.08-0.12 m³ per kW·hr stored

**Economic Analysis:**

Peak demand charge: $15/kW per month
Off-peak energy: $0.08/kWh
On-peak energy: $0.14/kWh

For 150 kW peak refrigeration load reduced to 50 kW (100 kW from storage):
- Demand savings: 100 kW × $15/kW × 12 months = $18,000/year
- Energy cost increase: 100 kW × 8 hr/day × 250 days × ($0.08 - $0.14) = -$12,000/year

**Net annual savings: $6,000**

Payback period on $80,000 ice storage system: 13.3 years (marginal project)

### Process Optimization

**Straining Temperature Optimization:**

Lower straining temperature reduces culture activity and improves yield:

| Straining Temperature | Protein Retention | Whey Volume | Energy Penalty |
|-----------------------|-------------------|-------------|----------------|
| 4°C | 99.2% | Reference | Baseline |
| 7°C | 98.7% | -2% | -15% cooling |
| 10°C | 97.8% | -4% | -30% cooling |

**Energy vs. Yield Trade-off:**

Extra cooling cost at 4°C: 15-20% higher refrigeration
Value of retained protein: $3-5/kg finished product
At 2% yield improvement: 20 kg more product per 1000 kg batch

**Benefit:** 20 kg × $4/kg = $80 per batch
**Cost:** 5 kW additional × 3 hr × $0.12/kWh = $1.80 per batch

**ROI: 4400% - low temperature straining is economically optimal**

---

Greek yogurt production requires integrated refrigeration design accounting for high-volume whey handling, increased product viscosity, and precise temperature control during straining. Energy recovery, variable capacity equipment, and optimized process temperatures provide significant operational savings while maintaining premium product quality. Proper HVAC design for process rooms ensures food safety compliance and efficient thermal management throughout the manufacturing facility.
