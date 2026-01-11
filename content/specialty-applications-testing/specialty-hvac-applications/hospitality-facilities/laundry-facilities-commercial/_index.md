---
title: "Commercial Laundry Facilities HVAC Design"
description: "Engineering guidelines for HVAC systems in commercial laundries including heat load calculations, humidity control, makeup air requirements, and lint filtration strategies for high-heat production environments."
date: "2026-01-05"
weight: 5
tags: ["commercial laundry", "industrial HVAC", "humidity control", "makeup air", "heat load", "ventilation design", "lint control", "worker comfort", "dryer exhaust", "heat recovery"]
categories: ["Specialty Applications", "Hospitality Facilities"]
keywords: ["commercial laundry HVAC", "laundry facility ventilation", "dryer exhaust makeup air", "laundry heat load", "humidity control commercial laundry", "lint filtration HVAC", "industrial laundry climate control", "commercial laundry design"]
---

Commercial laundry facilities present extreme HVAC challenges due to massive heat generation, continuous moisture release, and airborne particulate contamination. Proper climate control directly impacts worker safety, equipment longevity, and operational efficiency in these demanding industrial environments.

## Heat Load Characteristics

Commercial laundries generate exceptional sensible heat loads requiring careful analysis for adequate capacity sizing. Unlike typical commercial spaces, equipment heat dominates over envelope and occupant loads by factors of 10:1 or greater.

### Primary Heat Sources

Equipment heat release constitutes 85-95% of total facility sensible load.

**Dryers** contribute 50-70% of total facility heat gain:
- Gas-fired units: 3,000-5,000 BTU/hr per pound of rated capacity
- Electric resistance: 2,500-4,000 BTU/hr per pound of rated capacity
- Typical 50-pound commercial dryer: 150,000-250,000 BTU/hr input, 90,000-175,000 BTU/hr rejected to space

**Ironers and presses** generate concentrated heat loads:
- Flatwork ironers (chest or roller): 15,000-25,000 BTU/hr per unit depending on width and speed
- Steam presses: 8,000-12,000 BTU/hr per press head
- Form finishers: 10,000-18,000 BTU/hr per unit

**Washers** contribute during extraction and motor operation:
- Extract motors: 2,000-4,000 BTU/hr per machine during spin cycles
- Hot water carryover: minimal contribution to space load, most heat contained in water

**Finishing equipment** adds supplemental loads:
- Folder motors and conveyors: 500-1,500 BTU/hr per horsepower
- Steam tunnels: 20,000-40,000 BTU/hr depending on length and throughput
- Lint collection systems: 1,000-2,000 BTU/hr per motor

**Lighting** in industrial laundry facilities:
- High-bay LED or fluorescent: 1.0-1.5 W/ft²
- 1,000 ft² facility: 3,400-5,100 BTU/hr

Total sensible heat loads commonly reach 100-150 BTU/hr per square foot in production areas, with localized zones near dryers and ironers exceeding 300 BTU/hr per square foot. Equipment manufacturer data sheets provide exact input ratings essential for accurate load calculations.

### Occupant Load Contribution

Worker metabolic heat contributes secondary but significant load:
- Heavy work activity (lifting, sorting, folding): 600-800 BTU/hr per person
- Moderate activity (machine operation): 450-550 BTU/hr per person
- Typical staff density: 200-300 ft² per worker in production areas
- Occupant contribution: 2-4 BTU/hr per square foot

For 1,000 ft² laundry with 4 workers at heavy activity: 2,800 BTU/hr total occupant load, representing less than 1% of total facility heat gain.

## Humidity Control Requirements

Moisture release creates persistent high-humidity conditions requiring aggressive latent cooling capacity and ventilation to maintain acceptable working environments.

### Moisture Generation Sources

**Evaporation from wet textiles** during transfer between operations:
- Washer to dryer transfer: 0.5-1.0 lb moisture/hr per washer depending on extract efficiency
- Poor extract efficiency (below 50% moisture removal): doubles evaporative load

**Dryer exhaust leakage** through poor seals and duct connections:
- Well-maintained equipment: 5-10% of exhaust volume leaks to space
- Poorly maintained systems: 15-25% leakage contributing 30-60 lb/hr moisture per dryer

**Ironer steam release** from chest ironers and steam presses:
- Small chest ironers (60" wide): 15-20 lb/hr steam release
- Large production ironers (110-150" wide): 25-35 lb/hr steam release
- Steam presses: 5-10 lb/hr per press depending on usage intensity

**Floor cleaning and spills** contribute variable moisture:
- Continuous mop-up operations: 5-10 lb/hr facility-wide
- End-of-shift washdown: temporary 20-40 lb/hr for 30-60 minutes

### Total Latent Load Calculation

For typical 1,000 ft² hotel laundry processing 800-1,200 lb/day:
- Washer evaporation (3 washers × 0.7 lb/hr): 2.1 lb/hr
- Dryer leakage (4 dryers × 40 lb/hr × 0.15): 24 lb/hr
- Ironer steam release (1 ironer): 18 lb/hr
- Floor cleaning baseline: 6 lb/hr
- **Total moisture generation: 50 lb/hr**

Convert to latent heat using heat of vaporization (1,050 BTU/lb at typical conditions):

$$Q_{latent} = 50 \text{ lb/hr} \times 1,050 \text{ BTU/lb} = 52,500 \text{ BTU/hr}$$

This represents 40-60 BTU/hr per square foot latent load. Combined with sensible loads, total cooling requirement reaches 140-210 BTU/hr per square foot.

### Design Conditions and Equipment Selection

**Target space conditions:**
- Dry-bulb temperature: 75-78°F (worker comfort acceptable up to 82°F)
- Relative humidity: 50-60% maximum (55% preferred)
- Dewpoint temperature: 58-62°F maximum

Higher humidity promotes mold growth on textiles, accelerates equipment corrosion, and creates unsafe working conditions. ASHRAE Standard 55 recommends upper humidity limits of 65% for thermal comfort, but laundry operations benefit from tighter control.

**Sensible heat ratio (SHR) considerations:**

$$SHR = \frac{Q_{sensible}}{Q_{sensible} + Q_{latent}} = \frac{120,000}{120,000 + 52,500} = 0.70$$

This low SHR (compared to 0.80-0.85 typical commercial) requires enhanced dehumidification capability:

- Oversized evaporator coils with reduced face velocity (300-350 FPM vs. 400-500 FPM standard)
- Lower evaporator temperatures (38-42°F coil surface vs. 45-50°F standard)
- Subcooling reheat or hot gas reheat to maintain space temperature while operating extended dehumidification cycles
- Multiple compressor stages for capacity modulation matching varying loads

## Ventilation and Makeup Air Requirements

Massive exhaust requirements from dryers create substantial makeup air demands critical to system performance and building pressure control.

### Exhaust Volume Requirements

**Dryer exhaust** constitutes primary exhaust load:
- Commercial dryers exhaust 150-250 CFM per pound of rated capacity
- Typical 50-pound dryer: 7,500-12,500 CFM exhaust at full operation
- Multiple dryer installations: 30,000-100,000 CFM total exhaust not uncommon

**General space ventilation** removes heat and moisture beyond dryer exhaust:
- ASHRAE recommends 15-25 air changes per hour for industrial laundry spaces
- 1,000 ft² space with 12-foot ceiling height: 12,000 ft³ volume
- At 20 ACH: 4,000 CFM general exhaust requirement
- Combined dryer + general exhaust for mid-size facility: 15,000-25,000 CFM total

### Makeup Air System Design

Provide makeup air equal to 100-110% of total exhaust to maintain slight positive pressure (0.02-0.05 in. w.c.) preventing infiltration of unconditioned outdoor air through building envelope.

**Makeup air volume calculation:**

For laundry exhausting 18,000 CFM total (dryers + general ventilation):
- Design makeup air: 18,000 CFM × 1.05 = 18,900 CFM
- Slight positive pressure prevents uncontrolled infiltration while avoiding excessive pressurization

International Mechanical Code (IMC) Section 508.1 requires makeup air for commercial cooking and industrial exhaust systems exceeding 2,000 CFM. Makeup air must be provided through dedicated systems, not borrowed from adjacent building spaces.

### Makeup Air Unit Specifications

Dedicated makeup air units (MAU) should incorporate:

**Heating capacity** for winter operation:
- Size for design winter outdoor temperature to minimum 55-60°F discharge
- Cold climate (0°F design): 60°F temperature rise × 18,900 CFM × 1.08 = 1,224,720 BTU/hr (1.2 million BTU/hr)
- Moderate climate (20°F design): 40°F rise × 18,900 CFM × 1.08 = 816,480 BTU/hr

**Cooling capacity** for summer (optional but beneficial):
- Partial cooling to 80-85°F supply temperature reduces extreme space loads
- Full dehumidification to 55°F dewpoint often economically unjustifiable
- Evaporative cooling provides economical alternative in dry climates: 15-25°F temperature reduction at 10-20% capital cost of mechanical cooling

**Filtration systems:**
- MERV 8-11 minimum to prevent outdoor contaminant introduction
- Upstream bird screens and weather louvers
- Accessible filter sections with pressure drop monitoring

**Distribution design:**
- Discharge near dryer locations to provide direct path for replacement air
- High-velocity discharge (1,200-1,800 FPM) allows longer throw distances
- Multiple diffuser locations prevent short-circuiting from supply to exhaust

### Energy Impact of Makeup Air Temperature

Makeup air supply temperature directly affects supplemental space conditioning load. Each 10°F reduction in MAU supply temperature decreases cooling requirements:

$$\Delta Q_{cooling} = CFM \times 1.08 \times \Delta T = 18,900 \times 1.08 \times 10 = 204,120 \text{ BTU/hr}$$

Cooling makeup air from 95°F outdoor to 75°F discharge (20°F reduction) saves 408,240 BTU/hr (34 tons) supplemental space cooling capacity, offsetting MAU cooling equipment cost through reduced air handler sizing.

## Lint Control and Air Filtration

Airborne lint concentration threatens HVAC equipment reliability, indoor air quality, and creates fire hazards requiring comprehensive filtration strategies.

### Filtration Strategy

**Return air filtration** provides primary defense:
- MERV 11-13 pleated filters capture textile fibers before reaching cooling coils
- 4-inch deep pleated media preferred over 1-2 inch throwaway filters
- Filter face velocity: 300-400 FPM maximum to maintain MERV rating efficiency

**Filter replacement frequency:**
- Visual inspection: monthly minimum
- Pressure drop monitoring: replace when exceeding 0.5 in. w.c. or per manufacturer specification
- Typical replacement interval: 60-90 days depending on lint generation rate

**Coil protection:**
- Upstream filtration prevents lint accumulation reducing heat transfer efficiency
- Lint-fouled coils lose 20-40% capacity over 6-12 months without adequate filtration
- Annual coil cleaning required even with proper filtration

### Ductwork Design for Lint Management

**Duct configuration:**
- Avoid horizontal duct runs where lint settles and accumulates
- Slope all horizontal sections minimum 1/4 inch per foot toward drain points
- Install cleanout access panels at all elbows, transitions, and every 10-15 feet of straight run

**Drain provisions:**
- Low-point drains at duct low points prevent moisture accumulation
- Minimum 1-inch diameter drain connections with trap seals
- Condensate pumps where gravity drainage unavailable

**Access requirements:**
- Bolted access panels (minimum 12" × 12") at all direction changes
- Annual or semi-annual duct cleaning depending on lint accumulation rate
- Document cleaning schedules for fire marshal inspection compliance

### Equipment Selection for Lint-Heavy Environments

Specify HVAC units with lint-resistant features:
- Removable coil sections for periodic cleaning access
- Sloped drain pans with large-diameter connections (minimum 1" diameter)
- Easily accessible filter racks accommodating 4-inch pleated media
- Stainless steel or epoxy-coated drain pans resisting corrosion from moisture and detergent residues
- Sealed electrical compartments preventing lint infiltration to controls

## System Design Strategy

### Zoning and Separation

**Production area zoning:**
- Separate dryer areas requiring 100% outdoor air makeup from general production requiring partial recirculation
- Washing and sorting areas tolerate recirculated air with adequate filtration
- Dryer and ironer zones require dedicated once-through ventilation

**Support space separation:**
- Offices, break rooms, and employee areas operate with conventional recirculated systems
- Maintain positive pressure in support spaces relative to production preventing migration of heat, humidity, and lint
- Dedicated HVAC systems for non-production areas: 72-75°F, 45-50% RH for occupant recovery during breaks

### Equipment Location

**Air handler placement:**
- Locate condensing units and air handlers outdoors or in mechanical rooms isolated from lint-laden production environments
- Outdoor installation eliminates lint exposure but increases refrigerant line lengths
- Indoor mechanical room requires dedicated ventilation and lint filtration

**Duct routing:**
- Route return air through dedicated shafts with accessible filtration
- Avoid passing supply or return ducts through non-production areas preventing noise and heat transfer
- Insulate all supply ductwork in unconditioned spaces preventing condensation

### Control Strategies

**Demand-based ventilation:**
- Monitor dryer operation status via current sensors or equipment interlocks
- Reduce makeup air volumes during off-peak periods proportionally to active exhaust loads
- Variable frequency drives (VFD) on makeup air fans save 30-50% fan energy during partial load operation

**Space condition monitoring:**
- Temperature sensors in multiple production zones (dryers, washers, ironers)
- Humidity sensors monitoring space dewpoint for dehumidification control
- Building automation system (BAS) integration for optimal sequencing

**Equipment sequencing:**
- Stage cooling compressors based on space temperature deviation from setpoint
- Enable dehumidification reheat when space humidity exceeds 60% RH regardless of temperature
- Lead/lag equipment rotation for even runtime distribution

## Worker Comfort in High-Heat Environments

High heat and humidity environments require engineered solutions beyond standard comfort cooling to maintain productive, safe working conditions.

### Spot Cooling Systems

**High-velocity air circulators:**
- Deploy 18-24 inch diameter pedestal or ceiling-mounted fans
- Position to provide 200-400 FPM airflow at worker positions near dryers and ironers
- Air movement increases evaporative cooling from skin surfaces, improving thermal comfort by 3-5°F effective temperature
- Energy cost: 100-200 watts per fan location vs. thousands of watts for mechanical cooling

**Evaporative cooling in dry climates:**
- Portable or installed evaporative coolers provide 15-25°F temperature reduction
- Effective in climates below 40% outdoor relative humidity
- Operating cost: $0.20-0.40/hour vs. $2-4/hour for equivalent mechanical cooling

### Radiant Heat Barriers

**Equipment shielding:**
- Install reflective barriers or insulated panels between workers and equipment surfaces exceeding 140°F
- Polished aluminum shields reflect 80-90% of radiant heat
- Reduce radiant heat transfer by 40-60% improving comfort in close-proximity work areas

**Ceiling radiant barriers:**
- Reflective insulation in ceiling assemblies prevents downward radiant heat transfer from overhead ductwork and roof solar gain
- Reduces effective radiant temperature by 5-8°F in production areas

### Break Area Conditioning

**Enhanced comfort zones:**
- Aggressively conditioned break rooms at 72-74°F, 45-50% RH
- Physiological recovery during 10-15 minute rest periods
- Improved overall worker well-being despite challenging production floor conditions

**Transition zone design:**
- Vestibules between production and break areas prevent thermal shock
- Gradual temperature transition improves comfort and reduces HVAC load from door infiltration

Proper HVAC design transforms commercial laundries from oppressive heat zones into productive, safe work environments while protecting equipment investments and ensuring consistent textile processing quality.
