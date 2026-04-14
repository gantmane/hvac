---
title: "Mold Growth Control"
aliases: ["Mold Growth Control"]
description: "HVAC design strategies for controlled mold cultivation in surface-ripened cheeses and prevention of unwanted mold contamination in cheese manufacturing facilities, including filtration systems, environmental control parameters, and air distribution requirements."
weight: 4
---

Cheese manufacturing facilities require precise control of airborne mold spores to simultaneously cultivate beneficial surface molds on specific cheese varieties while preventing unwanted mold contamination on other products. HVAC system design must accommodate these competing objectives through zoning, filtration, pressurization, and environmental control strategies.

## Mold Growth Fundamentals

### Beneficial Mold Requirements

Surface-ripened and blue-veined cheeses depend on specific mold strains for flavor development, texture modification, and rind formation. The HVAC system must maintain conditions that promote desired mold growth.

**Primary Beneficial Mold Species:**

| Mold Species | Cheese Type | Temperature Range | Relative Humidity | Growth Rate |
|--------------|-------------|-------------------|-------------------|-------------|
| *Penicillium roqueforti* | Blue cheese, Roquefort, Gorgonzola | 50-55°F (10-13°C) | 90-95% | 0.5-1 mm/day |
| *Penicillium camemberti* | Camembert, Brie | 50-54°F (10-12°C) | 90-95% | 0.8-1.2 mm/day |
| *Geotrichum candidum* | Saint-Nectaire, Reblochon | 50-55°F (10-13°C) | 92-96% | 1-2 mm/day |
| *Brevibacterium linens* | Limburger, Munster | 54-59°F (12-15°C) | 93-97% | 0.6-1 mm/day |

### Spore Concentration Requirements

Desired mold development requires specific airborne spore concentrations:

- **Blue cheese caves:** 10³-10⁵ spores/m³ of *P. roqueforti*
- **Surface-ripened rooms:** 10²-10⁴ spores/m³ of *P. camemberti*
- **Mixed-rind environments:** 10²-10³ spores/m³ combined species

Spore concentration is controlled through:
- Natural accumulation from inoculated cheeses
- Mechanical atomization of spore suspensions
- Air filtration efficiency and bypass ratios
- Air change rates and recirculation percentages

### Growth Kinetics

Mold growth rate follows the modified Arrhenius relationship:

**μ = μ_max × f(T) × f(RH) × f(O₂) × f(CO₂)**

Where:
- μ = specific growth rate (mm/day)
- μ_max = maximum growth rate at optimal conditions
- f(T) = temperature function
- f(RH) = relative humidity function
- f(O₂) = oxygen availability function
- f(CO₂) = carbon dioxide inhibition function

Temperature effect on mold growth:

**f(T) = exp[-((T - T_opt)² / (2σ²))]**

Where:
- T = actual temperature (°C)
- T_opt = optimal temperature (typically 10-13°C for cheese molds)
- σ = standard deviation (typically 3-5°C)

## Unwanted Mold Prevention

### Contamination Sources

Undesired mold species (*Aspergillus*, *Cladosporium*, *Mucor*) must be controlled to prevent:
- Off-flavors and discoloration
- Mycotoxin production
- Product rejection and economic loss
- Cross-contamination between aging rooms

**Critical Control Points:**

1. **Outdoor air intake:** Primary source of environmental mold spores
2. **Personnel movement:** Transfer on clothing, equipment, hands
3. **Raw materials:** Milk, packaging materials, salt
4. **Room surfaces:** Walls, ceilings, drains, cooling coils
5. **HVAC components:** Ductwork, filters, humidifiers, condensate pans

### Prevention Strategies by Zone

| Zone Classification | Mold Control Level | Filtration | Pressurization | ACH |
|---------------------|-------------------|------------|----------------|-----|
| Processing rooms | High control | MERV 14-16 | +15-25 Pa | 15-20 |
| Packaging areas | Very high control | HEPA (H13) | +20-30 Pa | 20-25 |
| Blue cheese caves | Selective control | MERV 8-10 | 0 to +5 Pa | 4-8 |
| Surface-ripened rooms | Selective control | MERV 10-12 | 0 to +10 Pa | 6-10 |
| Hard cheese aging | High control | MERV 13-15 | +10-20 Pa | 8-12 |
| Corridors | Moderate control | MERV 11-13 | +5-15 Pa | 10-15 |

## Air Filtration Systems

### Filtration Design for Dual Objectives

HVAC systems serving cheese facilities must provide:
- **High-efficiency filtration** for clean zones (processing, packaging)
- **Selective filtration** for mold-ripening zones
- **Isolation** between incompatible zones

**Multi-Stage Filtration Configuration:**

**Outdoor Air Intake:**
1. **Pre-filter:** MERV 8 (45% efficiency per ASHRAE 52.2)
2. **Secondary filter:** MERV 11-13 (70-85% efficiency)
3. **Final filter:** MERV 14-16 or HEPA (per zone requirements)

**Recirculation Air:**
- Blue cheese caves: MERV 8-10 (retain *P. roqueforti* spores)
- Surface-ripened: MERV 10-12 (partial spore retention)
- Clean zones: MERV 14 minimum

### Filter Selection Criteria

Filter efficiency must account for particle size distribution of mold spores:

| Mold Species | Spore Size Range | MERV 13 Efficiency | MERV 15 Efficiency | HEPA H13 Efficiency |
|--------------|------------------|-------------------|-------------------|---------------------|
| *Penicillium* spp. | 2.5-4.5 μm | 65-75% | 85-92% | >99.95% |
| *Aspergillus* spp. | 2-3.5 μm | 60-70% | 82-90% | >99.95% |
| *Cladosporium* spp. | 3-10 μm | 75-85% | 90-95% | >99.97% |
| *Mucor* spp. | 4-8 μm | 70-80% | 88-94% | >99.96% |

**Pressure Drop Considerations:**

Initial and final filter pressure drops impact fan energy:

**ΔP_total = ΔP_filter1 + ΔP_filter2 + ΔP_filter3 + ΔP_system**

Typical pressure drops:
- MERV 8: 0.15-0.35 in. w.g. (clean to loaded)
- MERV 13: 0.25-0.60 in. w.g.
- MERV 15: 0.35-0.80 in. w.g.
- HEPA H13: 0.80-1.50 in. w.g.

### Filter Maintenance Protocols

**Replacement Frequency by Zone:**

| Zone Type | Filter Rating | Replacement Interval | Monitoring Method |
|-----------|---------------|---------------------|-------------------|
| Processing | MERV 14-16 | 3-6 months | Pressure differential |
| Packaging | HEPA H13 | 6-12 months | DOP test + pressure |
| Blue caves | MERV 8-10 | 6-9 months | Visual + pressure |
| Surface rooms | MERV 10-12 | 4-8 months | Pressure differential |
| Corridors | MERV 11-13 | 4-6 months | Pressure differential |

Filters should be replaced when:
- Pressure drop exceeds final rating by 0.2 in. w.g.
- HEPA efficiency drops below 99.95% (annual DOP test)
- Visual contamination observed on room-side surface
- Microbial testing shows contamination breakthrough

## Temperature and Humidity Control

### Psychrometric Requirements

Mold growth requires free water on cheese surfaces, governed by:

**a_w = RH_air / 100**

Where:
- a_w = water activity at cheese surface
- RH_air = relative humidity of surrounding air (%)

Beneficial mold species require:
- a_w > 0.90 (equivalent to RH > 90%)
- Minimum a_w of 0.85 for slow growth

### Dew Point Control

Surface condensation must be prevented on walls, ceilings, and cooling coils while maintaining high relative humidity in cheese aging spaces.

**Critical temperature relationship:**

**T_surface > T_dewpoint + 2°F (1.1°C)**

For aging room at 52°F (11°C) and 95% RH:
- Dew point = 50.7°F (10.4°C)
- Minimum wall surface temperature = 52.7°F (11.5°C)
- Required insulation = R-19 minimum (cold climate)

### Humidity Control Strategies

**Humidification Methods:**

| Method | Capacity Range | Control Accuracy | Microbial Risk | Application |
|--------|----------------|------------------|----------------|-------------|
| Steam injection | 50-5000 lb/hr | ±2% RH | Low (140°F+) | Large facilities |
| Evaporative media | 20-500 lb/hr | ±3% RH | Moderate | Medium facilities |
| Ultrasonic atomization | 5-200 lb/hr | ±2% RH | High (cold water) | Small rooms |
| Compressed air atomization | 10-300 lb/hr | ±3% RH | Moderate | Cave environments |

**Steam Humidification Design:**

For aging room requiring 90-95% RH:

**ṁ_steam = (Q_air × ρ_air × (ω_supply - ω_return)) / h_fg**

Where:
- ṁ_steam = steam mass flow rate (lb/hr)
- Q_air = air volume flow rate (CFM)
- ρ_air = air density (0.075 lb/ft³ at standard conditions)
- ω_supply = supply air humidity ratio (lb_water/lb_dry air)
- ω_return = return air humidity ratio
- h_fg = latent heat of vaporization (970 BTU/lb at 212°F)

**Example Calculation:**

Aging room: 5,000 ft³, 52°F, target 94% RH, 6 ACH
- Air flow = (5,000 ft³ × 6 ACH) / 60 min = 500 CFM
- Outdoor air fraction = 10% (50 CFM at 70°F, 50% RH)
- ω_outdoor = 0.0078 lb/lb (from psychrometric chart)
- ω_room = 0.0086 lb/lb (52°F, 94% RH)
- ṁ_steam = (500 × 0.075 × (0.0086 - 0.0078)) / (970/60) = 0.037 lb/min = 2.2 lb/hr

**Dehumidification Requirements:**

Blue cheese caves generate moisture from:
- Cheese surface evaporation: 0.2-0.4 lb/hr per 1000 lb cheese
- Air infiltration: depends on pressurization and door traffic
- Washing operations: intermittent peak loads

Dehumidification capacity:

**Q_dehumid = (ṁ_evap + ṁ_infiltration - ṁ_absorption) × h_fg**

Where:
- ṁ_evap = evaporation rate from cheese surfaces
- ṁ_infiltration = moisture from infiltration air
- ṁ_absorption = moisture absorbed by cheese rinds

## Air Distribution Design

### Air Change Rates

Air change rates balance multiple objectives:
- Spore distribution for beneficial mold
- Contaminant dilution
- Temperature uniformity
- Humidity control
- Energy efficiency

**Recommended ACH by Cheese Type:**

| Cheese Type | Aging Duration | ACH Range | Air Velocity at Cheese | Recirculation % |
|-------------|----------------|-----------|------------------------|-----------------|
| Blue cheese | 60-120 days | 4-8 | 20-40 fpm | 85-95% |
| Camembert/Brie | 21-35 days | 6-10 | 30-50 fpm | 80-90% |
| Washed rind | 30-90 days | 8-12 | 40-60 fpm | 75-85% |
| Hard cheese | 6-24 months | 8-15 | 30-50 fpm | 70-85% |
| Fresh cheese | 1-14 days | 15-20 | 50-80 fpm | 60-75% |

### Airflow Patterns

**Laminar Flow Considerations:**

Surface-ripened cheese requires uniform mold growth, achieved through:
- Low-velocity laminar airflow (Re < 2300)
- Perforated duct distribution
- Displacement ventilation strategies

**Reynolds number check:**

**Re = (V × D) / ν**

Where:
- V = air velocity (ft/s)
- D = hydraulic diameter (ft)
- ν = kinematic viscosity (1.6 × 10⁻⁴ ft²/s at 50°F)

For laminar flow at cheese surface:
- V_max = 0.8 ft/s (50 fpm)
- Turbulent mixing above Re = 2300 causes uneven spore deposition

**Supply Air Distribution:**

Perforated duct design for uniform spore distribution:

**A_total = Q / V_face**

Where:
- A_total = total perforation area (ft²)
- Q = air volume flow rate (CFM)
- V_face = face velocity through perforations (typically 400-800 fpm)

Perforation spacing for uniform flow:
- Hole diameter: 0.5-1.0 inches
- Spacing: 6-12 inches on center
- Open area ratio: 5-15% of duct surface

## Surface Mold for Rind Development

### Controlled Mold Application

Surface-ripened cheeses require precise mold inoculation and environmental control for rind development.

**Application Methods:**

1. **Spray Inoculation:**
   - Spore suspension: 10⁶-10⁷ spores/ml
   - Application rate: 0.5-1.0 ml per cheese surface
   - Spray pressure: 15-30 psi
   - Droplet size: 50-150 μm

2. **Aerosol Dispersion:**
   - Spore concentration: 10⁴-10⁵ spores/m³
   - Distribution time: 15-30 minutes
   - Air mixing required for uniformity

3. **Direct Transfer:**
   - Contact with colonized surfaces
   - Natural spore accumulation in aging rooms

### Rind Development Timeline

**Camembert/Brie Rind Formation:**

| Day | Surface Coverage | Mycelium Depth | Environmental Requirements |
|-----|------------------|----------------|----------------------------|
| 0-3 | Spore germination | Surface only | 52-54°F, 92-94% RH, 0.5-1 ACH |
| 4-7 | 20-40% white growth | 0.5-1 mm | 50-52°F, 93-95% RH, 2-4 ACH |
| 8-14 | 80-100% coverage | 1-2 mm | 50-52°F, 92-94% RH, 4-6 ACH |
| 15-21 | Dense mat formation | 2-4 mm | 52-54°F, 90-92% RH, 6-8 ACH |
| 22-35 | Proteolysis begins | 4-6 mm penetration | 50-52°F, 88-90% RH, 6-8 ACH |

**Blue Cheese Vein Development:**

Blue cheese requires internal mold growth through mechanical piercing:

- **Piercing timing:** Day 7-14 after molding
- **Hole diameter:** 2-3 mm
- **Hole spacing:** 1-2 inches on center
- **Oxygen penetration:** Critical for *P. roqueforti* growth
- **Cave conditions:** 50-52°F, 90-95% RH, air circulation 20-30 fpm

### Enzymatic Activity and HVAC Response

Mold proteolysis and lipolysis generate:
- Volatile organic compounds (VOCs): aldehydes, ketones, alcohols
- Ammonia from protein breakdown
- Heat from metabolic activity (minor, ~0.5 BTU/hr per lb cheese)

**VOC Removal Requirements:**

Activated carbon filtration for odor control:
- Carbon bed depth: 2-4 inches
- Face velocity: 200-400 fpm
- Replacement: annually or when breakthrough detected
- Capacity: 10-25% by weight for cheese VOCs

## UV Sterilization Systems

### UV-C Germicidal Irradiation

UV-C light (254 nm wavelength) inactivates mold spores in air streams and on surfaces.

**UV Dose Requirements:**

| Organism | D90 Dose (μJ/cm²) | 99% Kill Dose (μJ/cm²) | 99.9% Kill Dose (μJ/cm²) |
|----------|------------------|----------------------|-------------------------|
| *Aspergillus niger* spores | 66,000-132,000 | 132,000-264,000 | 198,000-396,000 |
| *Penicillium* spores | 44,000-88,000 | 88,000-176,000 | 132,000-264,000 |
| *Cladosporium* spores | 30,000-60,000 | 60,000-120,000 | 90,000-180,000 |
| Vegetative bacteria | 2,000-6,000 | 4,000-12,000 | 6,000-18,000 |

**UV System Design:**

In-duct UV-C systems for supply air:

**D = (I × t) / A**

Where:
- D = UV dose (μJ/cm²)
- I = lamp intensity (μW/cm²)
- t = exposure time (seconds)
- A = cross-sectional area factor

Exposure time calculation:

**t = L / V**

Where:
- L = lamp zone length (ft)
- V = air velocity through UV zone (ft/s)

**Example Design:**

AHU serving 2,000 CFM:
- Duct size: 24" × 20" (3.33 ft²)
- Air velocity: 2,000 CFM / 3.33 ft² = 600 fpm = 10 ft/s
- Target dose: 150,000 μJ/cm² (99% kill of *Penicillium*)
- Required intensity × time product: 150,000 μJ/cm²

For lamp zone length = 3 ft:
- Exposure time = 3 ft / 10 ft/s = 0.3 seconds
- Required intensity = 150,000 / 0.3 = 500,000 μW/cm² = 500 mW/cm²

Lamp selection:
- UV-C output: 30-100 watts per lamp
- Lamp configuration: 4-8 lamps in 3-foot section
- Maintenance: annual cleaning, lamp replacement every 9,000-12,000 hours

### Surface UV Treatment

UV-C treatment of aging room surfaces reduces unwanted mold accumulation:

**Surface Dose Calculation:**

**D_surface = (I × t × CF)**

Where:
- D_surface = delivered dose (mJ/cm²)
- I = intensity at surface (mW/cm²)
- t = exposure time (seconds)
- CF = configuration factor (0.5-0.9 for typical geometries)

Intensity varies with distance:

**I = P / (4π × r²)**

Where:
- P = lamp power (watts)
- r = distance from lamp to surface (meters)

**Application Protocols:**

| Surface Type | UV Dose Required | Treatment Frequency | Safety Considerations |
|--------------|------------------|---------------------|----------------------|
| Walls/ceilings | 50-100 mJ/cm² | Weekly | Occupancy prohibited |
| Equipment | 100-200 mJ/cm² | After cleaning | Eye/skin protection |
| Drains | 200-400 mJ/cm² | Daily | Remote activation |
| Floors | 50-150 mJ/cm² | Daily | Automated systems |

## Equipment Specifications

### Dedicated Cheese Aging HVAC Units

**Typical Unit Configuration:**

**Capacity Range:** 5,000-50,000 CFM per unit

**Component Specifications:**

| Component | Specification | Design Criteria |
|-----------|--------------|-----------------|
| Supply fan | Plenum, FC, VFD | 2-4 in. w.g. TSP, 30-50% turndown |
| Cooling coil | 6-8 rows, circuited for 52-54°F LAT | Approach 1-2°F, chilled water 40-42°F |
| Heating coil | Hot water or electric | Capacity for 40°F to 54°F rise |
| Humidifier | Steam grid or evaporative | 10-50 lb/hr, ±2% RH control |
| Filter bank | Multi-stage, 12-24 in. deep | MERV 8-16 per zone requirements |
| Controls | DDC with +/-0.5°F, ±1% RH accuracy | Networked, remote monitoring |

**Cooling Coil Design:**

For cheese aging at 52°F supply air temperature:

**Q_sensible = 1.08 × CFM × ΔT**

**Q_latent = 4.5 × CFM × Δω (gr/lb)**

Where:
- CFM = air volume flow rate
- ΔT = temperature difference (°F)
- Δω = humidity ratio difference (grains/lb)

**Example Sizing:**

Room: 20,000 ft³, 10 ACH, 52°F, 94% RH
- Supply air: 3,333 CFM
- Internal load: 15,000 BTU/hr sensible, 5,000 BTU/hr latent
- Ventilation: 10% outdoor air at 75°F, 60% RH

Coil capacity required:
- Sensible: 15,000 BTU/hr
- Latent: 5,000 BTU/hr
- Total: 20,000 BTU/hr (1.67 tons)

Coil selection:
- Rows: 6-8 (for dehumidification at 52°F LAT)
- Face velocity: 400-500 fpm
- Face area: 3,333 CFM / 450 fpm = 7.4 ft²
- Chilled water: 40°F supply, 48°F return, 8 GPM

### Refrigeration System Requirements

Cheese aging facilities require precise refrigeration:

**System Types:**

1. **Chilled Water System (Preferred for Large Facilities):**
   - Chiller capacity: 50-500 tons
   - Supply temperature: 38-42°F
   - Return temperature: 46-50°F
   - Pumping: Primary-secondary or variable primary flow
   - Backup: 100% redundancy for critical aging rooms

2. **Direct Expansion (Small Facilities):**
   - Scroll or rotary compressors
   - Evaporator temperature: 34-38°F
   - Superheat control: 8-12°F
   - Hot gas bypass for capacity modulation

**Load Calculations:**

Total refrigeration load:

**Q_total = Q_transmission + Q_product + Q_infiltration + Q_equipment + Q_personnel**

**Transmission Load:**

**Q_transmission = U × A × (T_outside - T_inside)**

Where:
- U = overall heat transfer coefficient (BTU/hr·ft²·°F)
- A = surface area (ft²)
- T_outside, T_inside = temperatures (°F)

Typical U-values for insulated aging rooms:
- Walls: 0.05-0.08 BTU/hr·ft²·°F (R-13 to R-20)
- Ceiling: 0.04-0.06 BTU/hr·ft²·°F (R-17 to R-25)
- Floor: 0.06-0.10 BTU/hr·ft²·°F (R-10 to R-17)

**Product Load:**

Cheese heat generation (respiration and mold metabolism):
- Fresh cheese: 0.5-1.0 BTU/hr per 100 lb
- Blue cheese: 0.3-0.6 BTU/hr per 100 lb (active mold growth)
- Hard cheese: 0.1-0.3 BTU/hr per 100 lb (minimal activity)

### Pressurization Control Equipment

Maintaining proper pressure relationships requires:

**Pressure Control Methods:**

| Method | Accuracy | Response Time | Application | Typical Cost |
|--------|----------|---------------|-------------|--------------|
| Relief dampers (barometric) | ±5 Pa | Passive | Simple applications | $ |
| Modulating relief dampers | ±2-3 Pa | 10-30 seconds | Medium complexity | $$ |
| Variable speed exhaust fans | ±1-2 Pa | 5-15 seconds | Critical areas | $$$ |
| Direct pressure control (DPC) | ±0.5-1 Pa | 2-5 seconds | Pharmaceutical-grade | $$$$ |

**Pressure Measurement:**

Differential pressure sensors:
- Range: 0-50 Pa (0-0.2 in. w.g.)
- Accuracy: ±0.5 Pa or ±2% of reading
- Response time: <1 second
- Calibration: annually

**Airflow Balancing:**

**Q_supply - Q_exhaust = Q_leak**

Where:
- Q_supply = supply airflow (CFM)
- Q_exhaust = exhaust airflow (CFM)
- Q_leak = infiltration/exfiltration through building envelope (CFM)

Leakage airflow estimation:

**Q_leak = C × A × √(ΔP)**

Where:
- C = leakage coefficient (CFM/ft² at 1 in. w.g.), typically 0.1-0.4
- A = leakage area (ft²)
- ΔP = pressure differential (in. w.g.)

**Example:**

Aging room: 20 Pa positive pressure, 1,000 ft² envelope area, C = 0.2
- Convert pressure: 20 Pa = 0.08 in. w.g.
- Q_leak = 0.2 × 1,000 × √(0.08) = 57 CFM
- Supply air must exceed exhaust by 57 CFM to maintain pressure

## HVAC Design Considerations

### System Zoning Strategy

Cheese facilities require rigorous zoning to prevent cross-contamination:

**Zone Hierarchy (High to Low Pressure):**

1. **Packaging areas:** +25 to +30 Pa (highest pressure)
2. **Processing rooms:** +20 to +25 Pa
3. **Hard cheese aging:** +15 to +20 Pa
4. **Corridors:** +10 to +15 Pa
5. **Surface-ripened rooms:** +5 to +10 Pa
6. **Blue cheese caves:** 0 to +5 Pa
7. **Wash rooms:** -5 to -10 Pa (negative pressure)

**Airflow Direction:**

Clean → Less Clean → Contaminated

Airflow should never reverse from mold-ripening areas into clean processing zones.

### Energy Recovery Limitations

Energy recovery systems must be evaluated carefully:

**Acceptable Technologies:**

- **Runaround loops:** Glycol coil systems with no air cross-contamination
- **Plate heat exchangers:** Only if 100% separation between airstreams
- **Sensible wheels:** Not recommended due to carryover risk

**Prohibited Technologies:**

- **Enthalpy wheels:** Cross-contamination of mold spores between airstreams
- **Heat pipes:** Only if isolation verified through commissioning

**Energy Recovery Effectiveness:**

For runaround loop system:

**ε = (T_supply - T_outdoor) / (T_exhaust - T_outdoor)**

Where:
- ε = effectiveness (typically 0.45-0.65 for runaround loops)
- T_supply = supply air temperature after heat recovery (°F)
- T_outdoor = outdoor air temperature (°F)
- T_exhaust = exhaust air temperature (°F)

### Control Sequences

**Aging Room Environmental Control:**

1. **Temperature Control:**
   - Primary: Chilled water valve modulation
   - Heating: Hot water valve or electric heat staging
   - Deadband: 1°F between heating and cooling
   - Setpoint accuracy: ±0.5°F

2. **Humidity Control:**
   - RH < setpoint - 2%: Enable humidifier, stage to 100%
   - RH > setpoint + 2%: Increase cooling, reduce humidification
   - RH > setpoint + 4%: Enable dehumidification mode

3. **Pressurization Control:**
   - Supply fan on constant volume or pressure-controlled VFD
   - Relief dampers modulate to maintain setpoint ±2 Pa
   - Low pressure alarm at setpoint -5 Pa

**Interlocks and Safeties:**

- Loss of refrigeration: Alarm and notification
- High humidity alarm: >98% RH for >30 minutes
- Low pressure alarm: Pressurization failure
- Filter high pressure alarm: Scheduled replacement required
- UV lamp failure: Maintenance notification

### Material Selection

Equipment and ductwork materials must withstand high humidity and chemical cleaning:

**Acceptable Materials:**

| Component | Material Options | Corrosion Resistance | Cost Factor |
|-----------|------------------|---------------------|-------------|
| Ductwork | 316 SS, FRP, PVC-coated galv. | Excellent / Excellent / Good | 3-4× / 2-3× / 1.5× |
| AHU casing | 304/316 SS, FRP | Excellent / Excellent | 2-3× / 2× |
| Coils | Copper-nickel, 316 SS | Excellent / Excellent | 2× / 3× |
| Drain pans | 316 SS, antimicrobial coating | Excellent / Good | 2× / 1.5× |
| Insulation | Closed-cell elastomeric, XPS | Good / Excellent | 1.5× / 1.2× |

**Surface Finishes:**

- Smooth, non-porous surfaces for easy cleaning
- Minimum crevices to prevent mold accumulation
- Sloped surfaces for drainage (1/4 in. per foot minimum)
- Removable panels for access and cleaning

### Maintenance Access

Design for routine maintenance and sanitation:

- **Filter access:** Front-loading filter racks with service corridors
- **Coil cleaning:** Removable coil sections or hinged access doors
- **Drain pan access:** Full-length access panels, 18-inch minimum clearance
- **UV lamp service:** External access doors, lamp monitoring systems
- **Humidifier maintenance:** Quick-disconnect fittings, isolated drainage

### Commissioning Requirements

Functional testing for cheese aging HVAC systems:

**Critical Tests:**

1. **Pressure relationships:** Verify all zones meet design pressures under all operating modes
2. **Temperature control:** ±0.5°F accuracy at all setpoints (45-65°F range)
3. **Humidity control:** ±2% RH accuracy at 90-95% RH setpoints
4. **Air change rates:** Verify actual ACH matches design (±10%)
5. **Filter efficiency:** HEPA leak test with DOP, others with pressure verification
6. **UV system output:** Measure intensity with calibrated radiometer
7. **Interlock verification:** Test all alarm sequences and safeties

**Seasonal Testing:**

Commission during peak summer and winter conditions to verify:
- Dehumidification capacity
- Humidification capacity during cold, dry weather
- Temperature control under extreme outdoor conditions

## Integration with Cheese Production

### Coordination with Process Equipment

HVAC systems must coordinate with:

**Cheese Production Schedule:**
- Molding operations: increased humidity loads
- Turning/washing: door openings, equipment heat gain
- Packaging: transition from high humidity to low humidity environment

**HVAC Response:**
- Pre-cooling/humidification before cheese placement
- Demand-controlled ventilation based on occupancy sensors
- Setback during unoccupied periods (limited for aging rooms)

### Monitoring and Alarming

Critical parameter monitoring:

**24/7 Continuous Monitoring:**
- Temperature (all zones): ±0.5°F accuracy
- Relative humidity (aging rooms): ±1% accuracy
- Differential pressure (all zones): ±1 Pa accuracy
- Filter pressure drop: ±0.05 in. w.g. accuracy

**Alarm Thresholds:**

| Parameter | Warning Level | Critical Level | Response Time |
|-----------|--------------|----------------|---------------|
| Temperature | ±2°F from setpoint | ±4°F from setpoint | <15 minutes |
| Humidity | ±5% from setpoint | ±8% from setpoint | <15 minutes |
| Pressure | ±5 Pa from setpoint | ±10 Pa from setpoint | <5 minutes |
| Power failure | Immediate | Immediate | <1 minute |

**Data Logging:**

Maintain continuous records for:
- Regulatory compliance (FDA, USDA)
- Quality assurance and troubleshooting
- Energy management and optimization
- Equipment performance trending

Standard logging interval: 5-15 minutes
Retention period: Minimum 3 years (per FDA recommendations)

---

**References:**
- ASHRAE Handbook - HVAC Applications, Chapter 21: Food Processing Facilities
- CFR Title 21, Part 117: Current Good Manufacturing Practice
- International Dairy Foods Association (IDFA) guidelines
- Academic research on *Penicillium* growth kinetics in controlled environments
