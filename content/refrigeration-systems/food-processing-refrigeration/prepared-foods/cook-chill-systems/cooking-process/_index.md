---
title: "Cooking Process in Cook-Chill Systems"
description: "Comprehensive analysis of cooking processes in industrial cook-chill food production including time-temperature requirements, equipment specifications, HACCP control points, heat rejection calculations, and kitchen ventilation design for HVAC integration."
weight: 1
---

## Overview

The cooking phase in cook-chill systems represents the critical thermal processing step where raw or partially prepared food products are heated to pathogen destruction temperatures while simultaneously creating substantial heat loads on building HVAC systems. This process demands precise temperature control, comprehensive monitoring, and coordinated HVAC design to manage sensible and latent heat gains.

The cooking process serves three primary functions: pathogen elimination, food quality development, and enzymatic inactivation. From an HVAC perspective, cooking equipment generates the largest thermal loads in food processing facilities, requiring robust kitchen ventilation systems and refrigeration capacity to handle subsequent cooling operations.

## Critical Temperature Requirements

### Minimum Safe Cooking Temperatures

Food safety regulations mandate minimum internal temperatures for pathogen destruction. The fundamental requirement establishes 74°C (165°F) as the universal safe temperature, though time-temperature combinations allow flexibility.

**Minimum Internal Temperatures by Product Type:**

| Product Category | Minimum Temperature | Hold Time | Target Pathogen |
|------------------|---------------------|-----------|-----------------|
| Poultry (whole/ground) | 74°C (165°F) | Instantaneous | Salmonella spp. |
| Ground meats (beef, pork) | 71°C (160°F) | Instantaneous | E. coli O157:H7 |
| Whole muscle meats | 63°C (145°F) | 15 seconds | Trichinella spiralis |
| Fish/seafood | 63°C (145°F) | 15 seconds | Parasites/bacteria |
| Eggs (held hot) | 68°C (155°F) | 15 seconds | Salmonella Enteritidis |
| Casseroles/stuffing | 74°C (165°F) | Instantaneous | Mixed pathogens |
| Reheated foods | 74°C (165°F) | 2 minutes | Vegetative cells/spores |
| Vegetables (to hold) | 60°C (140°F) | Continuous | Quality maintenance |

### Time-Temperature Equivalency

The D-value concept allows equivalent lethality through extended time at lower temperatures. The fundamental relationship:

**Pathogen Destruction Equation:**

```
log₁₀(N/N₀) = -t/D
```

Where:
- N = final microbial population
- N₀ = initial microbial population
- t = exposure time at temperature (minutes)
- D = decimal reduction time (time to reduce population by 90%)

**Equivalent Pathogen Lethality Combinations:**

| Temperature | Time Required | Log Reduction | Application |
|-------------|---------------|---------------|-------------|
| 63°C (145°F) | 3 minutes | 6.5-log | Whole muscle meats |
| 65°C (149°F) | 1 minute | 6.5-log | Sous vide processing |
| 68°C (154°F) | 16 seconds | 6.5-log | Rapid cook processes |
| 71°C (160°F) | 5 seconds | 6.5-log | Ground meat patties |
| 74°C (165°F) | Instantaneous | 7-log | Standard safety margin |
| 80°C (176°F) | Instantaneous | >10-log | High-risk products |

The z-value (temperature change for 10-fold D-value change) for most foodborne pathogens ranges from 4.5°C to 6.0°C, allowing calculation of equivalent processes.

## Equipment Types and Specifications

### Steam Jacketed Kettles

Tilting and stationary steam kettles provide batch cooking for soups, sauces, stews, and semi-liquid products.

**Design Parameters:**

| Specification | Range | Typical Application |
|---------------|-------|---------------------|
| Capacity | 20-500 L (5-130 gal) | Batch size dependent |
| Steam pressure | 50-100 psig (345-690 kPa) | Indirect heating |
| Heat input | 15-80 kW (51,000-273,000 BTU/hr) | Size dependent |
| Heat flux | 30,000-50,000 W/m² | Through jacket |
| Temperature control | ±2°C | PID controllers |
| Heating time | 15-45 min to 100°C | Product dependent |
| Sensible heat output | 70-85% of input | To kitchen space |
| Latent heat output | 15-30% of input | Evaporation/steam |

**Heat Rejection Calculation:**

```
Q_sensible = A × U × (T_steam - T_ambient)
Q_latent = m_evap × h_fg
Q_total = Q_sensible + Q_latent + Q_radiation
```

Where:
- A = external surface area (m²)
- U = overall heat transfer coefficient (15-25 W/m²·K for insulated kettles)
- T_steam = steam temperature (typically 115-125°C at operating pressure)
- T_ambient = kitchen ambient temperature (typically 25-30°C)
- m_evap = mass evaporation rate (kg/h)
- h_fg = latent heat of vaporization (2260 kJ/kg at 100°C)

For a typical 200 L kettle operating continuously:
- Heat input: 40 kW
- Sensible radiation: 10 kW (25%)
- Latent heat (steam/evaporation): 8 kW (20%)
- Product heating: 22 kW (55%)
- **Total HVAC load: 18 kW per kettle**

### Combination Ovens (Combi-Ovens)

Multi-mode convection ovens with steam injection provide versatile cooking capabilities.

**Operating Modes:**

| Mode | Temperature Range | Humidity Control | Heat Load Characteristics |
|------|-------------------|------------------|---------------------------|
| Dry convection | 100-300°C | <10% RH | High radiant, moderate convective |
| Steam cooking | 100-130°C | 100% RH | High latent, moderate sensible |
| Combination | 100-250°C | 30-80% RH | Mixed sensible/latent |
| Low-temperature cook | 60-95°C | 50-100% RH | Extended time, lower instantaneous load |

**Heat Rejection Profile:**

```
Q_oven = (P_electric × η_loss) + (m_steam × h_fg × f_vent)
```

For a 10-pan electric combi-oven (20 kW rated):
- Electrical input: 20 kW
- Insulation efficiency: 75% (5 kW loss)
- Steam generation: 15 kg/h at 100% steam mode
- Steam venting: 12 kg/h to exhaust hood
- Radiant losses: 3 kW
- Latent heat release (condensation on surfaces): 2 kW
- **Total HVAC load: 5 kW continuous**
- **Peak steam mode load: 8 kW** (includes latent release)

### Continuous Inline Cooking Systems

High-capacity tunnel ovens, continuous fryers, and conveyor cooking systems for large-scale production.

**Continuous Oven Specifications:**

| Parameter | Specification | Heat Load Impact |
|-----------|---------------|------------------|
| Conveyor speed | 0.5-3.0 m/min | Affects dwell time |
| Chamber length | 5-20 m | Continuous radiation |
| Temperature zones | 3-6 zones | 150-250°C per zone |
| Heat input per zone | 50-150 kW | Zone-specific control |
| Air velocity | 2-5 m/s | Convective transfer |
| Opening losses | 15-30% of input | Direct exhaust |
| Surface radiation | 20-35% of input | To kitchen space |
| **Total heat rejection** | **40-60% of rated input** | **HVAC cooling required** |

For a 3-zone continuous oven (300 kW total input):
- Product heating: 150 kW (50%)
- Exhaust losses: 75 kW (25%)
- Radiation to space: 60 kW (20%)
- Structural heat storage: 15 kW (5%)
- **HVAC sensible load: 60 kW**
- **Exhaust hood requirement: 135 kW capture**

### Steam Cooking Equipment

Atmospheric and pressurized steamers for vegetables, proteins, and delicate products.

**Steamer Types:**

| Equipment Type | Operating Pressure | Temperature | Heat Load (per compartment) |
|----------------|-------------------|-------------|---------------------------|
| Atmospheric pressure | 0 psig (gauge) | 100°C | 15-25 kW |
| Low-pressure | 5 psig (34 kPa) | 109°C | 20-30 kW |
| High-pressure | 15 psig (103 kPa) | 121°C | 30-45 kW |
| Pressureless convection | 0 psig | 100°C | 12-18 kW |

**Steam Consumption and Condensate:**

```
Steam_required = (m_product × c_p × ΔT) / (η × h_fg)
Condensate_rate = Steam_required × (1 - losses)
```

For 100 kg/h product throughput (20°C to 95°C):
- Specific heat: 3.5 kJ/kg·K (average food)
- Temperature rise: 75 K
- Efficiency: 80%
- Steam required: 14.5 kg/h
- Condensate generated: 13 kg/h (at 95°C)
- Condensate sensible heat available: 1.3 kW
- **Net heat to space: 18 kW** (after accounting for condensate recovery)

## Heat Rejection to HVAC Systems

### Total Kitchen Heat Load Calculation

Comprehensive heat load assessment requires equipment-specific calculations summed across all cooking units.

**Heat Load Components:**

| Source | Calculation Method | Typical Magnitude |
|--------|-------------------|-------------------|
| Equipment radiation | Surface area × U-value × ΔT | 20-35% of rated input |
| Steam/moisture release | Mass flow × latent heat | 15-30% of rated input |
| Exhaust hood capture failure | 5-15% of convective load | Variable with hood design |
| Personnel | 75 W sensible + 75 W latent per person | 150 W total per worker |
| Lighting | 10-20 W/m² LED, 40-60 W/m² fluorescent | Facility dependent |
| Product heat | Minimal (product leaves quickly) | Usually negligible |

**Aggregate Kitchen Load Equation:**

```
Q_kitchen_total = Σ(Q_equipment × RF) + Q_personnel + Q_lighting + Q_infiltration
```

Where RF = radiation factor (equipment-specific, typically 0.25-0.35)

**Example Large Cook-Chill Kitchen:**

Equipment inventory:
- 4× 200L steam kettles @ 40 kW each: 160 kW input
- 3× combi-ovens @ 20 kW each: 60 kW input
- 2× continuous ovens @ 150 kW each: 300 kW input
- 6× atmospheric steamers @ 18 kW each: 108 kW input
- Personnel: 25 workers
- Lighting: 500 m² × 15 W/m²: 7.5 kW

Heat load summary:
- Kettles: 160 kW × 0.30 RF = 48 kW
- Combi-ovens: 60 kW × 0.25 RF = 15 kW
- Continuous ovens: 300 kW × 0.20 RF = 60 kW
- Steamers: 108 kW × 0.28 RF = 30 kW
- Personnel: 25 × 150 W = 3.75 kW
- Lighting: 7.5 kW
- **Total sensible cooling load: 164 kW**
- **Latent load estimate: 45 kW** (moisture release)
- **Total HVAC requirement: 209 kW (59 tons refrigeration)**

### Hood Capture Efficiency Impact

Exhaust hood effectiveness directly impacts HVAC cooling loads.

**Hood Performance Metrics:**

| Hood Type | Capture Efficiency | Spillage to Space |
|-----------|-------------------|-------------------|
| Type I backshelf hood | 92-96% | 4-8% of convective load |
| Type I canopy hood (wall-mounted) | 85-92% | 8-15% of convective load |
| Type I single-island canopy | 80-88% | 12-20% of convective load |
| Type I double-island canopy | 75-85% | 15-25% of convective load |
| Proximity hood (low-clearance) | 95-98% | 2-5% of convective load |

Poor hood performance increases HVAC load proportionally to spillage percentage.

## Kitchen Ventilation Requirements

### Exhaust Hood Design

Type I hoods (grease-producing) required for most cooking operations.

**Exhaust Flow Rate Calculation:**

```
CFM = L × W × Exhaust_Rate
```

**Recommended Exhaust Rates:**

| Appliance Type | Light Duty | Medium Duty | Heavy Duty | Extra-Heavy Duty |
|----------------|------------|-------------|------------|------------------|
| CFM per ft² hood | 200 | 300 | 400 | 500+ |
| L/s per m² hood | 10.2 | 15.2 | 20.3 | 25.4+ |
| Application | Ovens, steamers | Ranges, griddles | Fryers, broilers | Char-broilers, woks |

**Hood Air Balance:**

For proper containment, maintain:
- Front face velocity: 75-125 fpm (0.38-0.64 m/s)
- Minimum overhang: 6 inches (150 mm) beyond appliance edge on all open sides
- Hood height: 4-7 feet (1.2-2.1 m) above floor for canopy, 3-4 feet (0.9-1.2 m) for backshelf

### Makeup Air Requirements

Replace exhaust air to prevent negative pressure problems.

**Makeup Air Design:**

| Parameter | Specification | Rationale |
|-----------|---------------|-----------|
| Supply vs. exhaust ratio | 85-95% | Slight negative pressure for odor control |
| Makeup air temperature | 15-20°C (winter), 22-26°C (summer) | Worker comfort at perimeter |
| Makeup air velocity at personnel | <50 fpm (0.25 m/s) | Avoid drafts |
| Tempered vs. untempered | Tempered required <10°C outdoor | Code compliance |
| Heated makeup air capacity | 50-100% of exhaust CFM | Climate dependent |

**Makeup Air Heating Load (Winter):**

```
Q_heating = CFM × 1.08 × (T_supply - T_outdoor)
```

For 10,000 CFM exhaust (4,720 L/s):
- Makeup air: 9,000 CFM (90% ratio)
- Outdoor temperature: -10°C (14°F)
- Supply temperature: 18°C (64°F)
- **Heating requirement: 272 kW (927,000 BTU/hr)**

**Makeup Air Cooling Load (Summer):**

```
Q_sensible = CFM × 1.08 × (T_outdoor - T_supply)
Q_latent = CFM × 0.68 × (W_outdoor - W_supply)
```

For 10,000 CFM exhaust in hot/humid climate:
- Outdoor: 35°C (95°F), 60% RH (0.021 kg H₂O/kg dry air)
- Supply: 24°C (75°F), 50% RH (0.009 kg H₂O/kg dry air)
- Sensible: 119 kW (406,000 BTU/hr)
- Latent: 46 kW (157,000 BTU/hr)
- **Total cooling: 165 kW (47 tons), 46 tons refrigeration**

## HACCP Critical Control Points

### Temperature Monitoring CCPs

**Critical Control Point Identification:**

| CCP Number | Control Point | Critical Limit | Monitoring Frequency | Corrective Action |
|------------|---------------|----------------|---------------------|-------------------|
| CCP-1 | Initial product temperature | ≤4°C at start | Every batch | Reject product >4°C |
| CCP-2 | Cooking temperature | ≥74°C for 2 min | Continuous probe | Extend cook time or discard |
| CCP-3 | Temperature distribution | ±2°C across batch | Every 50 batches | Recalibrate equipment |
| CCP-4 | Equipment calibration | ±0.5°C accuracy | Daily verification | Recalibrate before use |
| CCP-5 | Hold time verification | Per time-temp table | Every batch | Extend to meet requirement |

### Temperature Monitoring Systems

**Sensor Specifications:**

| Sensor Type | Range | Accuracy | Response Time | Application |
|-------------|-------|----------|---------------|-------------|
| Type K thermocouple | -40 to 260°C | ±1.1°C or 0.4% | 1-2 seconds | General purpose |
| Type T thermocouple | -40 to 260°C | ±0.5°C or 0.4% | 1-2 seconds | High accuracy |
| Pt100 RTD | -50 to 260°C | ±0.15°C at 0°C | 3-5 seconds | Calibration standard |
| Infrared sensor | -30 to 500°C | ±2°C or 2% | <1 second | Surface temperature |
| Wireless data logger | -40 to 140°C | ±0.3°C | 10-60 seconds | Automated recording |

**Placement Requirements:**

- Minimum 3 sensors per batch: geometric center + 2 coldest spots
- Sensor insertion depth: minimum 2 inches (50 mm) into thickest portion
- Avoid contact with metal surfaces or fat pockets
- Continuous recording at 30-60 second intervals

### Process Validation

**Heat Penetration Studies:**

Establish worst-case cooking profiles through systematic testing:

1. Identify slowest-heating product configuration (largest, densest, coldest)
2. Map temperature distribution using 9-12 sensors throughout batch
3. Record continuous time-temperature data throughout cook cycle
4. Calculate accumulated lethality (F-value) for each sensor location
5. Establish minimum process time ensuring all locations achieve target lethality

**F-Value Calculation:**

```
F₀ = Σ 10^((T - T_ref) / z) × Δt
```

Where:
- F₀ = equivalent minutes at reference temperature
- T = actual temperature at time interval (°C)
- T_ref = reference temperature (typically 74°C)
- z = z-value (typically 5-6°C for pathogens)
- Δt = time interval (minutes)

Target F₀ ≥ 2 minutes at 74°C for 7-log reduction of pathogens.

## Process Control and Automation

### Temperature Control Strategies

**PID Control Parameters:**

| Control Loop | Proportional (Kp) | Integral (Ki) | Derivative (Kd) | Application |
|--------------|------------------|---------------|-----------------|-------------|
| Steam kettle heating | 3-6 | 0.1-0.3 | 0.05-0.2 | Moderate lag |
| Oven zone control | 5-10 | 0.2-0.5 | 0.1-0.3 | Fast response |
| Steam pressure control | 2-4 | 0.05-0.15 | 0.02-0.08 | Stability critical |
| Conveyor speed | 1-3 | 0.5-1.0 | 0 | Disturbance rejection |

### Data Acquisition and Recording

Automated systems capture and store process data for HACCP compliance:

- Recording interval: 30-60 seconds maximum
- Data retention: Minimum 2 years (regulatory requirement)
- Alarm limits: ±2°C from setpoint triggers operator alert
- Critical deviation: >2°C below minimum safe temperature requires automatic process hold
- Network integration: OPC-UA or Modbus connectivity to facility SCADA

## Energy Efficiency Optimization

### Heat Recovery Opportunities

**Condensate Recovery:**

High-temperature condensate from steam cooking equipment contains significant recoverable energy.

```
Q_recoverable = m_condensate × c_p × (T_condensate - T_ambient)
```

For 500 kg/h condensate at 95°C:
- Sensible heat content: 58 kW (198,000 BTU/hr)
- Potential applications: Makeup air preheating, water preheating, radiant heating
- Recovery efficiency: 60-75% with heat exchanger
- **Recoverable energy: 35-44 kW**

**Exhaust Air Heat Recovery:**

Kitchen exhaust contains substantial thermal energy, though grease content complicates recovery.

For 10,000 CFM exhaust at 45°C (113°F) in winter (-10°C outdoor):
- Sensible heat: 353 kW (1.2 million BTU/hr)
- Practical recovery (run-around loop with coil protection): 40-50%
- **Recoverable: 140-175 kW**

### Equipment Efficiency Measures

| Measure | Energy Savings | Implementation Cost | Payback Period |
|---------|----------------|---------------------|----------------|
| High-efficiency burners | 10-15% gas reduction | Moderate | 2-3 years |
| Improved insulation | 8-12% heat loss reduction | Low-moderate | 1-2 years |
| Steam pressure optimization | 5-8% energy reduction | Low | <1 year |
| Exhaust hood demand control | 20-30% fan energy | Moderate-high | 2-4 years |
| Variable speed drives (fans) | 30-50% fan energy | Moderate | 1-3 years |
| LED kitchen lighting | 50-70% lighting energy | Low | <1 year |
| Heat recovery systems | 30-50% heating energy offset | High | 3-7 years |

### Load Management Strategies

**Equipment Staging:**

Sequence cooking equipment operation to minimize simultaneous peak demand:

- Stagger start times for large continuous ovens (15-30 minute intervals)
- Operate steam kettles in alternating banks
- Schedule high-load processes during off-peak HVAC hours when possible
- Implement demand-limiting controls to cap total electrical draw

**Peak Demand Reduction:**

For a facility with 600 kW connected cooking equipment load:
- Diversity factor: 0.70 (not all equipment at full load simultaneously)
- Actual peak demand: 420 kW
- With staging and load management: 350 kW
- **Demand reduction: 70 kW (17% reduction)**
- **Annual cost savings: $8,000-15,000** (depending on demand charges)

## Safety Considerations

### Burn Prevention

High-temperature cooking equipment poses significant burn hazards:

- Install barriers or guards on exposed hot surfaces >60°C
- Provide insulated handles on all kettles and tilting equipment
- Ensure steam valve locations prevent operator exposure to discharge
- Maintain clearances per NFPA 96: minimum 18 inches from combustibles
- Post warning signage on all surfaces exceeding 50°C

### Fire Protection

Cooking operations create grease accumulation and ignition risks:

- Install automatic fire suppression (wet chemical systems per NFPA 17A)
- Maintain fusible link temperature ratings: 74-165°C depending on location
- Clean exhaust hoods and ductwork quarterly minimum
- Provide Class K fire extinguishers at 30-foot maximum travel distance
- Integrate suppression system with gas/electric shutoff and exhaust fan shutdown

## Equipment Specifications Summary

**Standard Procurement Requirements:**

All cooking equipment for cook-chill operations shall meet:

- NSF/ANSI 4 certification (commercial food equipment)
- UL listing for electrical equipment or comparable international standard
- ENERGY STAR certification where applicable
- Minimum 3-inch (75 mm) fiberglass insulation on all heated surfaces >65°C
- Digital temperature controls with ±1°C accuracy and 0.1°C resolution
- Stainless steel construction (type 304 minimum, type 316 for high-acid products)
- Automated data logging capability (4-20 mA output or digital protocol)
- Seismic restraint provision per IBC/ASCE 7 (seismic design categories D-F)

---

**References:**
- FDA Food Code (current edition): Time-temperature requirements for food safety
- ASHRAE Handbook - HVAC Applications: Chapter on Commercial Kitchens
- NFPA 96: Standard for Ventilation Control and Fire Protection of Commercial Cooking Operations
- HACCP Principles & Application Guidelines (FDA/USDA)
- ASTM F2861: Standard Practice for Heat Recovery from Commercial Kitchen Exhaust Systems
