---
title: "Offshore Platform HVAC Systems"
description: "HVAC design for offshore oil and gas platforms, drilling rigs, and FPSOs including hazardous area classifications, accommodation comfort, pressurization requirements, and compliance with offshore standards."
date: "2026-01-05"
weight: 4
tags: ["offshore platforms", "oil rigs", "FPSO", "hazardous areas", "API standards", "pressurization", "accommodation HVAC", "marine environments"]
categories: ["Specialty Applications", "Marine HVAC"]
---

## Offshore Platform Environment

Offshore platforms present extreme HVAC design challenges combining hazardous industrial processes with residential-style living quarters in corrosive marine environments. Systems must maintain personnel comfort and safety while operating continuously in salt spray, high winds, temperature extremes, and potentially explosive atmospheres.

Platform types requiring specialized HVAC:
- Fixed production platforms (jackets, gravity-based structures)
- Compliant towers and tension leg platforms
- Floating production storage and offloading vessels (FPSOs)
- Semi-submersible drilling rigs
- Jack-up drilling platforms
- Subsea production facilities with topside modules

Operating conditions create unique requirements:
- Continuous 24/7 operation with no shutdown windows
- Personnel accommodation for 50-300 workers
- Hazardous area classifications requiring explosion-proof equipment
- Salt-laden atmosphere causing accelerated corrosion
- Structural weight and space constraints
- Limited maintenance access and long supply chains
- Integration with fire and gas detection systems

## Hazardous Area Classification

Area classification determines HVAC equipment selection and installation requirements based on probability of explosive atmosphere formation.

### Classification Zones

**Zone 0** (API Division 1 equivalent):
- Explosive atmosphere present continuously or for long periods
- Rare in HVAC applications
- Interior of process vessels, wellheads, storage tanks
- HVAC equipment generally excluded from Zone 0 areas

**Zone 1** (API Division 1):
- Explosive atmosphere likely during normal operations
- Occurs around process equipment, pump seals, compressor seals
- Drilling floor areas during well operations
- Requires HVAC equipment certified for Zone 1 (Ex d or Ex p)
- Positive pressure ventilation maintains classification boundaries

**Zone 2** (API Division 2):
- Explosive atmosphere unlikely during normal operations but possible during abnormal conditions
- Areas adjacent to Zone 1 locations
- Enclosed equipment rooms containing hydrocarbon piping
- Standard industrial equipment acceptable with restrictions
- Most offshore HVAC equipment operates in Zone 2 or safe areas

### Gas Group Classification

Hydrocarbon atmospheres classified by ignition characteristics:

| Gas Group | Representative Gas | Maximum Experimental Safe Gap (mm) | Minimum Ignition Current Ratio |
|-----------|-------------------|-----------------------------------|-------------------------------|
| IIA | Propane | 0.9 | 0.8 |
| IIB | Ethylene | 0.5-0.9 | 0.45-0.8 |
| IIC | Hydrogen, Acetylene | < 0.5 | < 0.45 |

Offshore oil and gas facilities typically design for Group IIA (propane/methane) or IIB (ethylene) depending on process fluids.

### Temperature Classification

Equipment surface temperature must remain below autoignition temperature of gases present:

- T1: 450°C maximum surface temperature
- T2: 300°C maximum
- T3: 200°C maximum (most offshore applications)
- T4: 135°C maximum
- T5: 100°C maximum
- T6: 85°C maximum

HVAC equipment in hazardous areas typically rated T3 (200°C) or cooler.

## Equipment Requirements for Hazardous Areas

### Explosion-Proof Construction

**Flameproof Enclosures (Ex d)**: Contains internal explosion:
- Motor housings, control panels, junction boxes
- Flanged joints with specified gap dimensions prevent flame transmission
- Heavy cast construction adds weight to equipment
- Common for fans, actuators, electrical components

**Increased Safety (Ex e)**: Prevents ignition sources:
- Enhanced insulation, terminal spacing
- Temperature monitoring prevents overheating
- Lower weight than flameproof construction
- Used for motors, lighting fixtures

**Purged and Pressurized (Ex p)**: Maintains positive pressure with inert gas or clean air:
- Analyzer shelters, control rooms, motor control centers
- Requires continuous airflow and pressure monitoring
- Interlocks prevent operation if pressure lost
- Reduces weight compared to explosion-proof construction

### Ventilation System Design

Hazardous area ventilation prevents explosive atmosphere accumulation:

**Air Change Rates**:
- Zone 1 areas: 12-20 air changes per hour minimum
- Zone 2 areas: 8-12 air changes per hour
- Enclosed process areas: 15-30 ACH during gas release scenarios
- Continuously operating systems with backup capability

**Airflow Patterns**: Designed to sweep gas release points:
- Low-level air intakes remove heavier-than-air hydrocarbons (propane, butane)
- High-level exhaust removes lighter-than-air gases (methane)
- Directed airflow from safe areas toward hazardous areas prevents gas migration
- CFD modeling validates ventilation effectiveness for complex geometries

**Gas Detection Integration**: HVAC responds to gas detection system:
- Normal operation: continuous ventilation at design rates
- Gas detected: increased ventilation to maximum capacity
- High gas concentration: emergency shutdown and area evacuation
- Ventilation interlock with process equipment startup

## Pressurization Systems

Positive pressure systems protect critical spaces from hazardous atmosphere intrusion.

### Control Room Pressurization

Control rooms house personnel and critical instrumentation requiring explosion-free environment:

**Design Pressure Differential**:
- Minimum: 0.05 in. w.c. (12 Pa) relative to exterior
- Typical: 0.10-0.15 in. w.c. (25-37 Pa)
- Maximum: 0.30 in. w.c. (75 Pa) to limit door forces

**Supply Air Requirements**:

$$Q_{supply} = Q_{leakage} + Q_{pressurization}$$

Where leakage calculated as:

$$Q_{leakage} = A_{leak} \times 2610 \times \sqrt{\Delta P}$$

For typical control room (1,500 ft², 4 doors, construction leakage):
- Door leakage area: 0.15 ft² per door = 0.60 ft² total
- Construction leakage: 0.002 ft²/ft² wall area = 0.20 ft² for 100 ft² walls
- Total leakage area: 0.80 ft²
- At 0.10 in. w.c. differential:

$$Q_{supply} = 0.80 \times 2610 \times \sqrt{0.10} = 660 \text{ cfm}$$

Add 25% safety factor: 825 cfm minimum supply.

**System Features**:
- Dedicated supply fan with backup (auto-switchover on failure)
- HEPA filtration removes particulates
- Activated carbon removes hydrocarbon vapors (optional)
- Differential pressure monitoring with low-pressure alarm
- Automatic dampers seal room on high gas detection outside control room
- Emergency override allows depressurization for firefighting access

### Accommodation Module Pressurization

Living quarters maintained at positive pressure relative to industrial areas:

**Pressure Staging**:
1. Living quarters: +0.10 in. w.c. relative to exterior/industrial
2. Corridors/common areas: +0.05 in. w.c.
3. Industrial areas: 0.00 in. w.c. (reference)
4. Hazardous process areas: 0.00 to -0.05 in. w.c.

Pressure gradient prevents hydrocarbon migration toward occupied spaces.

**Vestibule Design**: Transition spaces between pressure zones:
- Two doors in series with intermediate space
- Pressurized vestibule reduces airflow loss during personnel passage
- Self-closing doors maintain pressure boundary
- Volume: 50-100 ft³ per vestibule typical

## Accommodation HVAC Systems

Living quarters require comfort conditions for personnel working multi-week shifts.

### Design Conditions

**Exterior Conditions** (basis for load calculations):
- Summer: 95°F dry bulb, 80°F wet bulb typical (region dependent)
- Winter: -10°F to +20°F (cold climate offshore)
- Solar radiation: increased due to low latitude (equatorial platforms) or continuous daylight (Arctic)
- Wind: 50-100 mph design wind, affects infiltration and equipment mounting
- Salt spray: continuous exposure requires corrosion-resistant construction

**Interior Conditions**:
- Cabins/sleeping quarters: 72-76°F, 40-60% RH
- Common areas: 74-78°F, 40-60% RH
- Galley/dining: 76-80°F, 50-60% RH
- Gym/recreation: 72-76°F, 40-50% RH
- Medical facilities: 72-76°F, 40-60% RH, positive pressure

### System Configurations

**Central Chilled Water System**: Most common for larger platforms:
- Water-cooled screw or centrifugal chillers (500-2,000 ton capacity)
- Seawater-cooled condenser bundles (titanium tubes)
- Primary-secondary chilled water distribution (42°F/54°F)
- Air handling units serve zones (cabins, common areas, galley)
- Fan coil units in individual cabins for occupant control
- Redundancy: N+1 chiller configuration for continuous operation

**Packaged DX Systems**: Smaller platforms or retrofit applications:
- Rooftop or split-system air conditioners
- Air-cooled condensers with corrosion-resistant coil coatings
- Independent systems per zone reduce single-point failure risk
- Higher energy consumption than central systems
- Easier maintenance with modular component replacement

**Hybrid Systems**: Combine central and distributed equipment:
- Central air handling for ventilation air (pre-conditioned)
- Local fan coils or VRF systems for sensible cooling
- Separates ventilation (code-driven) from comfort (occupant-driven)
- Energy recovery between exhaust and supply air streams

### Ventilation Requirements

Accommodation spaces require continuous outdoor air per API RP 14C and local regulations:

| Space Type | Outdoor Air (cfm/person) | Air Changes per Hour |
|------------|-------------------------|---------------------|
| Sleeping quarters | 20-25 | 6-8 |
| Office spaces | 15-20 | 6-10 |
| Dining/galley | 20-25 | 15-20 |
| Recreation areas | 20-25 | 6-8 |
| Locker rooms | 15-20 | 10-15 |
| Bathrooms | N/A | 10-15 (exhaust) |
| Laundry | N/A | 20-30 (exhaust) |

Positive building pressure requires supply airflow 5-10% greater than exhaust airflow.

### Heating Systems

Cold-climate platforms require space heating for accommodation and freeze protection:

**Heat Sources**:
- Waste heat recovery from gas turbines or diesel generators
- Hot water boilers (fired or waste heat recovery boilers)
- Electric heating (locations with abundant generator capacity)

**Distribution**:
- Hydronic heating via perimeter convectors or radiant panels
- Hot water coils in central air handlers
- Ceiling-mounted unit heaters for industrial spaces
- Heat tracing for freeze protection of piping and equipment

## Corrosion Protection

Marine atmosphere requires comprehensive corrosion prevention:

**Materials Selection**:
- Stainless steel (316 grade minimum) for seawater-exposed components
- Aluminum 5xxx or 6xxx series with anodized coating for ductwork and louvers
- Titanium tubes for seawater heat exchangers
- Galvanized steel with epoxy coating for sheltered applications
- Non-metallic (FRP, PVC) for low-pressure applications

**Protective Coatings**:
- Phenolic or epoxy coatings on aluminum and steel surfaces
- Powder coat finishes on electrical enclosures
- Continuous coating inspection and touch-up programs
- Multi-coat systems (primer + intermediate + finish) for long service life

**Design Features**:
- Enclosed equipment rooms protect from direct spray
- Drainage provisions prevent water accumulation
- Continuous cathodic protection for seawater systems
- Sacrificial anodes on seawater-cooled equipment
- Regular freshwater washdown of exposed equipment

## Applicable Standards

Offshore platform HVAC design follows multiple international standards:

**API Recommended Practices**:
- API RP 14C: Analysis, Design, Installation, and Testing of Basic Surface Safety Systems for Offshore Production Platforms
- API RP 14F: Design and Installation of Electrical Systems for Fixed and Floating Offshore Petroleum Facilities for Unclassified and Class I, Division 1 and Division 2 Locations
- API RP 500: Recommended Practice for Classification of Locations for Electrical Installations at Petroleum Facilities Classified as Class I, Division 1 and Division 2

**International Standards**:
- IEC 60079 series: Explosive atmospheres equipment standards
- ISO 13702: Petroleum and natural gas industries - Control and mitigation of fires and explosions on offshore production installations
- NORSOK S-002: Working environment (Norwegian offshore standards)
- DNVGL standards: Classification society rules for marine and offshore units

**HVAC-Specific Requirements**:
- ASHRAE Applications Handbook, Chapter 27: Industrial applications
- ASHRAE 62.1: Ventilation for acceptable indoor air quality (accommodation basis)
- IMO MODU Code: Mobile Offshore Drilling Units Code (for drilling rigs)

Offshore platform HVAC systems balance personnel safety, comfort, and operational reliability in hazardous and corrosive environments. Proper hazardous area classification, robust pressurization systems, redundant equipment configurations, and comprehensive corrosion protection enable these systems to protect personnel and support continuous operations under extreme conditions.
