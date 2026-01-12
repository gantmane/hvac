---
title: "Liquid Egg Products"
description: "Refrigeration and HVAC requirements for liquid egg product processing including immediate chilling, cold chain maintenance, processing room environmental control, and regulatory temperature compliance for whole eggs, whites, and yolks"
weight: 2
---

Liquid egg products require stringent temperature control from breaking through processing, storage, and distribution to prevent microbial growth and maintain functional properties. HVAC and refrigeration system design must account for high heat loads from processing equipment, frequent sanitation cycles, and critical time-temperature requirements mandated by FDA and USDA regulations.

## Liquid Egg Product Types

### Whole Liquid Eggs

Whole liquid eggs contain both albumen and yolk in natural proportions, providing a complete egg product for food service and manufacturing applications.

**Composition characteristics:**
- Solids content: 23-25%
- Protein: 12-13%
- Fat: 10-11%
- pH: 7.0-7.6
- Freezing point: -0.45°C (31.2°F)

**Critical temperature requirements:**
- Breaking temperature: Maximum 7°C (45°F) within 2 hours
- Processing temperature: 4-7°C (39-45°F)
- Storage temperature: 2-4°C (36-39°F)
- Distribution temperature: ≤4°C (≤39°F)

### Egg Whites (Albumen)

Egg whites represent approximately 67% of egg content by weight and are used for angel food cakes, meringues, confections, and high-protein applications.

**Composition characteristics:**
- Solids content: 11-12%
- Protein: 10-11%
- pH: 9.0-9.5 (increases with storage)
- Freezing point: -0.45°C (31.2°F)
- Heat-sensitive proteins (conalbumin, lysozyme)

**Temperature control parameters:**
| Processing Stage | Temperature Range | Maximum Duration | Critical Factor |
|-----------------|-------------------|------------------|-----------------|
| Separation | 4-7°C (39-45°F) | Continuous | Protein stability |
| Filtration | 4-7°C (39-45°F) | 30 minutes | Foaming prevention |
| Storage holding | 2-4°C (36-39°F) | 48 hours | Microbial control |
| Pre-pasteurization | 4-7°C (39-45°F) | 24 hours | Quality retention |

### Egg Yolks

Egg yolks constitute approximately 33% of egg content by weight and serve as emulsifiers in mayonnaise, salad dressings, and baking applications.

**Composition characteristics:**
- Solids content: 43-45%
- Protein: 16-17%
- Fat: 32-35%
- Lecithin: 8-9%
- pH: 6.0-6.4
- Freezing point: -0.58°C (30.9°F)

**Gelation prevention requirements:**
- Plain yolks gel irreversibly when frozen
- Sugar addition: 10% w/w prevents gelation
- Salt addition: 10% w/w prevents gelation
- Processing temperature: 4-7°C (39-45°F) before additive incorporation

### Blended Products

Blended liquid egg products combine eggs with dairy, seasonings, or other ingredients for specific food service applications.

**Common formulations:**
- Scrambled egg mix: whole eggs + milk + butter
- Omelet mix: whole eggs + cheese + seasonings
- French toast batter: whole eggs + milk + sugar + spices
- Extended products: eggs + milk proteins or starches

**Temperature control challenges:**
- Multiple ingredient temperature histories
- Increased water activity from dairy additions
- Enhanced microbial growth potential
- Shorter shelf life than plain liquid eggs

## Immediate Chilling Requirements

### Breaking to Chilling Time-Temperature Limits

FDA Egg Safety Rule (21 CFR 118) and Pasteurized Milk Ordinance guidelines establish maximum time-temperature exposure limits.

**Regulatory compliance parameters:**
| Product Type | Maximum Chilling Time | Target Temperature | Enforcement Level |
|--------------|----------------------|-------------------|-------------------|
| Whole eggs | 2 hours | ≤7°C (≤45°F) | FDA mandatory |
| Egg whites | 2 hours | ≤7°C (≤45°F) | FDA mandatory |
| Egg yolks | 2 hours | ≤7°C (≤45°F) | FDA mandatory |
| Blended products | 1 hour | ≤4°C (≤39°F) | USDA/FDA |

### Chilling System Design

Immediate chilling systems must rapidly reduce product temperature while maintaining product quality and preventing freeze damage.

**Plate heat exchanger sizing:**

Heat load calculation:

Q = ṁ × cp × ΔT

Where:
- Q = heat removal rate (kW)
- ṁ = mass flow rate (kg/s)
- cp = specific heat capacity (kJ/kg·K)
- ΔT = temperature difference (K)

**Specific heat values for liquid egg products:**
| Product | Specific Heat (kJ/kg·K) | Thermal Conductivity (W/m·K) |
|---------|------------------------|------------------------------|
| Whole eggs | 3.52 | 0.56 |
| Egg whites | 3.89 | 0.58 |
| Egg yolks | 2.85 | 0.42 |

**Example calculation for whole egg chilling:**

Processing rate: 5,000 kg/hr (1.39 kg/s)
Inlet temperature: 18°C (breaking room temperature)
Outlet temperature: 4°C
ΔT = 14 K

Q = 1.39 kg/s × 3.52 kJ/kg·K × 14 K = 68.5 kW (19.5 tons refrigeration)

Add 25% safety factor: 85.6 kW (24.4 tons refrigeration)

### Chilled Storage Buffer Tanks

Liquid egg products require immediate refrigerated storage between breaking/chilling and pasteurization operations.

**Storage tank refrigeration design:**
- Jacketed tanks with glycol circulation: -2 to 2°C glycol temperature
- Direct expansion coils in tank space: evaporator temperature -5 to 0°C
- Agitation heat input: 0.5-1.5 kW per 1,000 liters
- Heat infiltration through insulation: 2-3 W/m²
- Tank capacity: 4-8 hours of breaking production

**Tank cooling load calculation:**

Q_total = Q_product + Q_agitation + Q_infiltration + Q_ambient

For a 10,000-liter insulated tank:
- Product heat removal: 68.5 kW (calculated above)
- Agitation heat: 1.2 kW/1,000 L × 10 = 12 kW
- Infiltration (200 m² surface): 2.5 W/m² × 200 = 0.5 kW
- Ambient losses: 5-8 kW

Total cooling requirement: 86-89 kW (24.5-25.3 tons)

## Cold Chain Maintenance

### Pre-Pasteurization Cold Chain

Liquid egg products must maintain continuous refrigeration from breaking through pasteurization to prevent microbial growth, particularly Salmonella enteritidis.

**Critical control points:**
1. Breaking room to chiller: insulated pipes, maximum 5 minutes
2. Chiller to storage tank: jacketed transfer lines, ≤4°C
3. Storage tank holding: continuous refrigeration, 2-4°C
4. Tank to pasteurizer feed: jacketed lines, maximum 10 minutes transfer time

**Cold chain failure consequences:**

Microbial growth rate doubles approximately every 10°C temperature increase above 4°C.

Log reduction required to compensate for temperature abuse:

log N = (T - 4) × t / D_value

Where:
- N = microbial population increase
- T = abuse temperature (°C)
- t = time at abuse temperature (hours)
- D_value = decimal reduction time at reference temperature

### Post-Pasteurization Cold Chain

Pasteurized liquid egg products require immediate cooling and continuous refrigeration to prevent recontamination and growth of psychrotrophic bacteria.

**Post-pasteurization cooling requirements:**
| Product | Pasteurization Temp | Cooling Target | Maximum Cooling Time |
|---------|--------------------|-----------------|--------------------|
| Whole eggs | 60°C (140°F) | 4°C (39°F) | 90 minutes |
| Egg whites | 57°C (134°F) | 4°C (39°F) | 60 minutes |
| Egg yolks | 61°C (142°F) | 4°C (39°F) | 120 minutes |
| Sugar yolks | 63°C (145°F) | 4°C (39°F) | 120 minutes |
| Salt whole eggs | 63°C (145°F) | 4°C (39°F) | 90 minutes |

**Cooling system configuration:**
- Primary stage: plate heat exchanger with chilled water (1-2°C)
- Secondary stage: glycol-cooled surge tank (-1 to 1°C glycol)
- Final holding: refrigerated storage tanks (2-4°C product)

### Distribution Cold Chain

Pasteurized liquid egg products require continuous refrigeration during filling, storage, and distribution.

**Temperature monitoring requirements:**
- Continuous temperature recording in storage coolers
- Temperature sensors in tanker trucks every 2 meters
- Maximum temperature excursion: 7°C for 2 hours
- Alarm activation at 5°C
- Reject product if >7°C for >2 hours or >10°C at any time

## Processing Room HVAC Design

### Breaking Room Environmental Control

The egg breaking area requires strict environmental control to minimize microbial contamination and maintain worker comfort in a cold, wet environment.

**Breaking room design parameters:**
| Parameter | Target Value | Tolerance | Monitoring Frequency |
|-----------|-------------|-----------|---------------------|
| Air temperature | 10-13°C (50-55°F) | ±2°C | Continuous |
| Relative humidity | 60-70% | ±10% | Continuous |
| Air changes per hour | 15-20 ACH | Minimum 15 | Commissioning |
| Outside air | 15-20% | Minimum 15% | Continuous |
| Room pressure | +15 Pa | +10 to +25 Pa | Continuous |
| Air velocity | 0.15-0.25 m/s | Non-drafting | Annual verification |

**HVAC system configuration:**
- 100% outside air system with energy recovery
- Chilled water cooling coils (4-6°C supply water)
- Reheat coils for humidity control
- MERV 13-14 filtration minimum
- Supply air temperature: 8-10°C after reheat
- Separate exhaust for odor and moisture removal

**Sensible and latent load calculation:**

Sensible heat gain sources:
- Personnel: 75 W sensible per person × number of workers
- Lighting: 10-15 W/m² (LED industrial lighting)
- Equipment: conveyors, breakers, pumps (measured or manufacturer data)
- Transmission: U-value × area × ΔT
- Ventilation: ṁ_air × cp_air × (T_outside - T_inside)

Latent heat gain sources:
- Personnel: 55 W latent per person
- Product evaporation from open vessels: significant in breaking area
- Wet floor evaporation: 20-40 W/m² of wet surface
- Ventilation: ṁ_air × h_fg × (ω_outside - ω_inside)

### Separation and Filtration Room

Dedicated rooms for egg separation and filtration require lower temperatures and tighter humidity control than breaking rooms.

**Environmental parameters:**
- Air temperature: 7-10°C (45-50°F)
- Relative humidity: 55-65%
- Air changes: 20-25 ACH
- Positive pressure: +20 Pa relative to breaking room
- HEPA filtration in critical zones

### Ingredient Addition and Blending Room

Rooms where sugar, salt, or other ingredients are added to egg products require temperature control to prevent premature gelation or microbial growth.

**Design conditions:**
- Air temperature: 4-7°C (39-45°F) for yolk products
- Air temperature: 10-13°C (50-55°F) for whole egg products
- Humidity control: 60-70% RH to prevent ingredient clumping
- Positive pressure relative to adjacent spaces
- Separate HVAC zone with independent control

## Equipment Heat Loads

### Breaking Machine Heat Generation

Automated egg breaking machines generate substantial heat from motors, hydraulics, and mechanical friction.

**Typical heat generation rates:**
| Machine Type | Capacity | Electrical Load | Heat to Space | Heat to Product |
|--------------|----------|----------------|---------------|-----------------|
| Inline breaker | 120,000 eggs/hr | 15-25 kW | 12-20 kW | 3-5 kW |
| Rotary breaker | 180,000 eggs/hr | 25-40 kW | 20-32 kW | 5-8 kW |
| High-speed line | 240,000 eggs/hr | 40-60 kW | 32-48 kW | 8-12 kW |

Heat to space includes:
- Motor inefficiency (typically 85-92% efficient)
- Hydraulic system heat rejection
- Bearing and drive friction
- Control panel heat dissipation

Heat to product includes:
- Mechanical agitation of egg mass
- Friction during shell separation
- Pump work on liquid product

### Separation Equipment Loads

Centrifugal separators and membrane filtration systems generate heat that must be removed to maintain product temperature.

**Centrifuge heat loads:**
- Motor heat: P_motor × (1 - η_motor)
- Friction heat: function of rotational speed and product viscosity
- Typical total heat generation: 5-15 kW per separator unit

### Pumping System Heat Loads

Positive displacement pumps and centrifugal pumps add heat to liquid egg products through mechanical work and friction.

**Pump heat addition calculation:**

ΔT_pump = (P_pump / ṁ × cp) × (1 - η_pump)

Where:
- ΔT_pump = temperature rise through pump (K)
- P_pump = pump power input (kW)
- ṁ = mass flow rate (kg/s)
- cp = specific heat capacity (kJ/kg·K)
- η_pump = pump efficiency (typically 0.65-0.85 for positive displacement)

**Example:**
Pump power: 7.5 kW
Flow rate: 1.39 kg/s (5,000 kg/hr)
Efficiency: 0.75
Specific heat: 3.52 kJ/kg·K (whole eggs)

ΔT_pump = (7.5 / 1.39 × 3.52) × (1 - 0.75) = 0.38 K

Temperature rise: 0.38°C per pumping stage

Multiple pumping stages compound this effect, requiring additional refrigeration capacity to compensate.

## Sanitation Temperature Requirements

### Hot Water Sanitation Systems

Liquid egg processing equipment requires daily hot water sanitation at elevated temperatures to ensure microbial destruction.

**Sanitation water temperatures:**
| Sanitation Type | Water Temperature | Contact Time | Application Method |
|----------------|------------------|--------------|-------------------|
| Pre-rinse | 40-50°C (104-122°F) | 5-10 minutes | Flood/spray |
| Detergent wash | 60-70°C (140-158°F) | 15-20 minutes | Circulation |
| Post-rinse | 40-50°C (104-122°F) | 5-10 minutes | Flood/spray |
| Sanitizer rinse | 75-85°C (167-185°F) | 10-15 minutes | Circulation |
| Final rinse | Cold (≤10°C) | 5 minutes | Flush |

**HVAC impact during sanitation:**

Hot water sanitation creates substantial moisture and heat loads in processing rooms:

- Latent heat from evaporation: 2,260 kJ/kg water evaporated
- Sensible heat from hot surfaces: equipment surface area × h × ΔT
- Humidity increase: can reach 90-95% RH during sanitation
- Temperature increase: 5-10°C above normal operating temperature

**Sanitation load management:**
- Increase exhaust air volume during sanitation: 200-300% of normal
- Activate supplemental dehumidification if installed
- Allow 2-4 hours cool-down time before production restart
- Target post-sanitation conditions: ≤10°C, ≤75% RH

### Equipment Cool-Down Requirements

After hot sanitation, all product-contact surfaces must be cooled to ≤10°C before introducing liquid egg products.

**Cool-down methods:**
1. Cold water circulation: 2-4°C water through cleaned systems
2. Refrigerated air circulation in enclosed equipment
3. Chilled glycol through jacketed vessels
4. Room air cooling for external surfaces

**Cool-down time estimation:**

t = (m × cp × ΔT) / (Q_cooling)

Typical cool-down times:
- Stainless steel tanks: 1-2 hours
- Pipe systems: 30-60 minutes
- Heat exchangers: 45-90 minutes
- Breaking machines: 2-3 hours

## Quality Control Temperatures

### Protein Functionality Preservation

Liquid egg proteins have specific temperature sensitivities that affect functional properties critical for end-use applications.

**Temperature-sensitive functional properties:**
| Property | Critical Temperature | Measurement | Application Impact |
|----------|---------------------|-------------|-------------------|
| Foaming (whites) | >10°C degradation begins | Foam volume, stability | Meringue, angel food cake |
| Emulsification (yolks) | >7°C lecithin damage | Emulsion stability | Mayonnaise, dressings |
| Gelation (whole eggs) | <-2°C ice crystal damage | Gel strength | Custards, baked goods |
| Coagulation temperature | Product-specific | Differential scanning calorimetry | All applications |

**Foaming property preservation for egg whites:**

Egg whites must maintain foaming capacity for meringue and angel food cake applications. Temperature abuse above 7°C for extended periods reduces foam volume and stability.

Foam volume reduction rate:
- Storage at 4°C: <5% loss per week
- Storage at 7°C: 10-15% loss per week
- Storage at 10°C: 25-35% loss per week

### Color Stability

Egg yolk color intensity (measured in Roche yolk color fan units) degrades with temperature abuse and oxidation.

**Color preservation requirements:**
- Storage temperature: ≤4°C
- Minimize oxygen exposure: <2% headspace oxygen
- Light protection: opaque containers or dark storage
- Antioxidant addition: optional for extended shelf life

### Viscosity Control

Liquid egg product viscosity increases with storage time and temperature abuse due to protein aggregation.

**Viscosity specifications:**
| Product | Fresh Viscosity (mPa·s at 20°C) | Maximum Acceptable | Storage Impact |
|---------|--------------------------------|-------------------|----------------|
| Whole eggs | 5-8 | 12 | Increases with storage |
| Egg whites | 2-4 | 6 | pH-dependent increase |
| Egg yolks | 80-150 | 250 | Temperature-sensitive |

Temperature control minimizes viscosity increase by reducing protein-protein interactions and preventing aggregation.

## Regulatory Temperature Requirements

### FDA Egg Safety Rule (21 CFR 118)

The FDA Egg Safety Rule establishes mandatory temperature controls for egg products to prevent Salmonella enteritidis growth.

**Key regulatory requirements:**
1. Shell eggs must be held at ≤7°C (≤45°F) during breaking
2. Liquid egg products must be cooled to ≤7°C within 2 hours of breaking
3. Storage temperature must be maintained at ≤7°C until pasteurization
4. Post-pasteurization storage at ≤7°C (≤45°F) or frozen
5. Distribution temperature ≤7°C for refrigerated products

**Regulatory compliance documentation:**
- Continuous temperature monitoring and recording
- Automated alarm systems at critical control points
- Standard operating procedures for temperature deviations
- Corrective action procedures for non-conforming product
- Validation studies demonstrating temperature control efficacy

### USDA FSIS Requirements for Egg Products

USDA Food Safety and Inspection Service (FSIS) regulates egg products used in further processed foods.

**FSIS temperature requirements (9 CFR 590):**
| Requirement | Temperature | Application |
|-------------|-------------|-------------|
| Breaking operations | ≤7°C (≤45°F) | All liquid egg products |
| Storage before pasteurization | ≤7°C (≤45°F) | Maximum 72 hours |
| Pasteurized product storage | ≤4°C (≤39°F) | Recommended |
| Frozen egg products | ≤-18°C (≤0°F) | Mandatory |
| Thawing frozen eggs | ≤7°C (≤45°F) | Under refrigeration only |

### Pasteurized Milk Ordinance (PMO) Application

Some jurisdictions apply PMO temperature requirements to liquid egg products due to similar microbial risk profiles.

**PMO-based temperature limits:**
- Refrigerated storage: ≤4°C (≤39°F)
- Distribution: ≤4°C (≤39°F)
- Retail display: ≤4°C (≤39°F)
- Consumer guidance: refrigerate at ≤4°C

## Refrigeration System Sizing

### Total Plant Refrigeration Load

Comprehensive refrigeration load calculation includes product cooling, process equipment heat rejection, environmental conditioning, and safety factors.

**Load categories and typical percentages:**
| Load Source | Percentage of Total | Calculation Method |
|-------------|--------------------|--------------------|
| Product chilling | 35-45% | ṁ × cp × ΔT |
| Process equipment heat | 15-25% | Equipment power × inefficiency |
| Room cooling sensible | 10-15% | Transmission + ventilation + occupancy |
| Room cooling latent | 5-10% | Evaporation + occupancy + ventilation |
| Tank and vessel cooling | 10-15% | Product holding + agitation |
| Sanitation cool-down | 5-8% | Post-cleaning equipment cooling |
| Safety factor | 15-20% | Applied to sum of above |

**Example refrigeration load summary for 10,000 kg/hr liquid egg plant:**

Product chilling load:
- Q_product = 1.39 kg/s × 3.52 kJ/kg·K × 14 K = 68.5 kW

Process equipment:
- Breaking machines: 20 kW
- Separators: 10 kW
- Pumps: 8 kW
- Conveyors: 5 kW
- Total equipment: 43 kW

Breaking room cooling:
- Sensible: 35 kW
- Latent: 18 kW
- Total room: 53 kW

Storage tank cooling:
- Four tanks at 12 kW each: 48 kW

Subtotal: 68.5 + 43 + 53 + 48 = 212.5 kW

Safety factor (20%): 42.5 kW

**Total refrigeration capacity required: 255 kW (72.5 tons)**

### Refrigeration System Architecture

Liquid egg processing plants typically employ centralized ammonia or cascade CO2/ammonia systems with secondary glycol loops to processing areas.

**System configuration options:**

**Option 1: Centralized ammonia with glycol secondary**
- Engine room: ammonia chillers producing -5 to 0°C glycol
- Distribution: insulated glycol piping to process areas
- End use: plate heat exchangers, jacketed tanks, air handling units
- Advantages: ammonia isolation from food areas, good efficiency
- Disadvantages: glycol pumping energy, approach temperature losses

**Option 2: Distributed packaged refrigeration**
- Multiple packaged R-448A or R-449A systems
- Direct expansion cooling of process equipment
- Individual system capacities: 10-50 kW
- Advantages: system redundancy, simplified installation
- Disadvantages: higher refrigerant charge, lower efficiency

**Option 3: CO2 cascade with ammonia primary**
- Ammonia primary loop: -10 to -5°C CO2 condensing
- CO2 secondary: -8 to 0°C process cooling
- Transcritical CO2 capability for flexibility
- Advantages: natural refrigerants, excellent efficiency
- Disadvantages: higher capital cost, complexity

### Glycol System Design

Propylene glycol secondary loops are common in liquid egg processing to isolate ammonia refrigerant from food contact zones.

**Glycol system parameters:**
| Parameter | Typical Value | Design Consideration |
|-----------|--------------|----------------------|
| Glycol concentration | 25-30% by weight | Freeze protection to -10°C |
| Supply temperature | -2 to 2°C | Process requirement dependent |
| Return temperature | 5 to 10°C | Δ T = 5-8 K typical |
| Flow rate | Based on load/ΔT | Q = ṁ × cp × ΔT |
| Pump head | 20-40 m (200-400 kPa) | Piping friction + equipment ΔP |
| Expansion tank | 10-15% system volume | Thermal expansion accommodation |

**Glycol flow rate calculation:**

ṁ_glycol = Q / (cp_glycol × ΔT)

For 255 kW cooling load with 30% propylene glycol:
- cp_glycol = 3.85 kJ/kg·K
- ΔT = 6 K
- ṁ_glycol = 255 / (3.85 × 6) = 11.04 kg/s

Glycol density at 0°C: 1,025 kg/m³
Volume flow: 11.04 / 1,025 = 0.0108 m³/s = 38.8 m³/hr = 171 GPM

### Heat Rejection Systems

Liquid egg processing refrigeration systems require adequate heat rejection capacity accounting for compressor heat of compression.

**Heat rejection calculation:**

Q_rejection = Q_refrigeration × (COP + 1) / COP

For ammonia system with COP = 3.5:
Q_rejection = 255 × (3.5 + 1) / 3.5 = 328 kW

Add 10% for hot gas defrost (if applicable): 361 kW

**Heat rejection options:**
- Evaporative condensers: most efficient, water consumption
- Adiabatic coolers: reduced water use, good efficiency
- Air-cooled condensers: no water use, lower efficiency, larger footprint
- Cooling towers with shell-and-tube condensers: flexible, scalable

**Condenser capacity selection:**
- Size for peak ambient conditions (95-100°F dry bulb)
- Ammonia condensing temperature: 35-40°C (95-104°F)
- Approach to wet bulb: 5-7°C for evaporative systems
- Approach to dry bulb: 10-15°C for air-cooled systems

---

**File location:** `/Users/evgenygantman/Documents/github/gantmane/hvac/content/refrigeration-systems/food-processing-refrigeration/eggs-egg-products/egg-breaking-processing/liquid-egg-products/_index.md`

This enhanced content provides HVAC professionals with comprehensive technical guidance on refrigeration and environmental control requirements for liquid egg product processing facilities, including detailed load calculations, system sizing methodology, regulatory compliance requirements, and practical design parameters.
