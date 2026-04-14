---
title: "Hotel Commercial Kitchen HVAC Systems: Exhaust Hood Design and Makeup Air"
aliases: ["Hotel Commercial Kitchen HVAC Systems: Exhaust Hood Design and Makeup Air"]
description: "Complete technical guide to hotel commercial kitchen HVAC: Type I/II exhaust hood design, grease removal efficiency, makeup air systems, NFPA 96 compliance, fire suppression coordination, and worker comfort solutions."
date: "2026-01-05"
weight: 6
tags: ["kitchen exhaust", "makeup air", "NFPA 96", "Type I hood", "restaurant HVAC", "grease removal", "fire suppression", "UL 300", "commercial kitchen", "hotel kitchen", "hood design", "kitchen ventilation", "worker comfort"]
categories: ["Specialty Applications", "Hospitality HVAC", "Commercial Kitchen"]
keywords: ["commercial kitchen exhaust", "Type I hood", "Type II hood", "makeup air", "grease filters", "NFPA 96 compliance", "UL 300 fire suppression", "kitchen ventilation design", "hotel restaurant HVAC", "grease duct", "kitchen worker comfort", "spot cooling", "dining room conditioning"]
---

## Kitchen Exhaust Hood Design

Commercial kitchen exhaust hoods remove heat, smoke, grease, and combustion products from cooking appliances while preventing their dispersion into dining areas. Hood design follows NFPA 96 requirements distinguishing between Type I (grease-producing) and Type II (heat/moisture only) exhaust systems.

### Type I Grease Hoods

Type I hoods cover appliances producing grease-laden vapors including ranges, griddles, fryers, and charbroilers. Construction requires 18-gauge stainless steel or 18-gauge carbon steel with listed grease filters capturing particulates before entering ductwork. Hood extends minimum 6 inches beyond appliance footprint on all open sides to contain thermal plume.

Exhaust airflow rates depend on appliance type, duty cycle (light/medium/heavy), and hood configuration (wall-mounted canopy versus island/peninsula). ASHRAE recommendations provide:

**Wall-Mounted Canopy Hoods**:
- Light duty: 200 CFM per linear foot
- Medium duty: 300 CFM per linear foot
- Heavy duty: 400 CFM per linear foot

**Island/Peninsula Hoods** (50% higher than wall-mounted):
- Light duty: 300 CFM per linear foot
- Medium duty: 450 CFM per linear foot
- Heavy duty: 600 CFM per linear foot

Calculate total exhaust for 12-foot wall-mounted heavy-duty hood:
$$CFM_{exhaust} = 12 \text{ ft} \times 400 \text{ CFM/ft} = 4,800 \text{ CFM}$$

Alternative calculation methods base airflow on hood face area and capture velocity. Maintain minimum 50-100 FPM face velocity (measured 6 inches below hood) to prevent spillage during normal operation. For 12 ft × 4 ft hood face:

$$CFM = A_{face} \times V_{face} = (12 \times 4) \times 75 = 3,600 \text{ CFM}$$

Use larger value between per-linear-foot calculation and face velocity method.

### Grease Filters and Removal Efficiency

UL-listed baffle or mesh filters mount in hood at 45-60° angle directing grease to collection troughs. Baffle filters achieve 60-80% grease removal efficiency through impaction and direction changes forcing grease dropout. Spacing between baffles maintains 1.5-2.0 inches for optimal performance.

Filter face velocity should remain below 500 FPM to prevent grease re-entrainment. For 4,800 CFM hood with 48 ft² filter area:
$$V_{filter} = \frac{4,800}{48} = 100 \text{ FPM}$$

This low velocity permits effective grease capture. Undersized filter areas with velocities exceeding 500 FPM allow grease passage into ductwork creating fire hazard through accumulation.

### Type II Heat/Moisture Hoods

Type II hoods handle non-grease appliances including steamers, ovens, dishwashers, and kettles. Construction permits lighter materials and relaxed clearances since grease fire risk is absent. Exhaust rates follow heat removal requirements:

$$CFM = \frac{Q_{sensible}}{1.08 \times (T_{hood} - T_{room})}$$

where $Q_{sensible}$ is appliance heat output (typically 40-60% of nameplate rating) and hood temperature runs 120-140°F.

For a 60 kW steamer releasing 60% of energy as space heat:
$$CFM = \frac{60 \times 3,412 \times 0.60}{1.08 \times (130-75)} = 3,455 \text{ CFM}$$

## Makeup Air Requirements

Kitchen exhaust creates substantial building depressurization requiring dedicated makeup air. Exhausting 5,000-15,000 CFM without makeup air generates -0.10 to -0.30 in. wc building pressure, causing door operation difficulty, backdrafting of atmospheric-vented equipment, and uncontrolled infiltration.

### Makeup Air Volume

Provide makeup air equal to 80-100% of exhaust volume. The remaining 0-20% comes from transfer air from dining room and hotel corridors. Complete makeup air replacement (100%) maintains neutral kitchen pressure relative to dining room, preventing odor migration while allowing comfortable door operation.

For 8,000 CFM total kitchen exhaust:
- Dedicated makeup air: $8,000 \times 0.85 = 6,800$ CFM
- Transfer from dining/adjacent spaces: $8,000 \times 0.15 = 1,200$ CFM

Makeup air systems must be listed for use in commercial kitchen applications with grease-resistant construction and approved for installation proximity to cooking surfaces.

### Makeup Air Tempering

Untempered outdoor air discharged near cooking surfaces creates drafts affecting hood capture and worker discomfort. NFPA 96 permits unheated makeup air discharge at minimum 10 feet from hood and workers, but most installations provide heating for worker comfort and improved hood performance.

**Heating Requirements**: Winter makeup air heating represents substantial load. Calculate heating capacity:

$$Q_{heating} = CFM \times 1.08 \times (T_{supply} - T_{outdoor})$$

For 6,800 CFM raised from 0°F to 60°F:
$$Q_{heating} = 6,800 \times 1.08 \times 60 = 440,640 \text{ Btu/hr}$$

This 440 MBH heating load runs continuously during kitchen operation in cold weather, significantly impacting boiler capacity and fuel consumption.

**Cooling Option**: Hot climates benefit from makeup air cooling preventing excessive kitchen temperatures. Direct-expansion cooling or evaporative cooling reduces 95°F outdoor air to 75-80°F supply. Cooling capacity:

$$Q_{cooling} = CFM \times 1.08 \times (T_{outdoor} - T_{supply})$$

For same 6,800 CFM cooled from 95°F to 75°F:
$$Q_{cooling} = 6,800 \times 1.08 \times 20 = 146,880 \text{ Btu/hr (12.2 \text{ tons})}$$

Economic analysis compares cooling cost against improved kitchen comfort and potential labor productivity gains from better working conditions.

### Makeup Air Distribution

Three primary distribution methods exist:

**Front Face (Proximity) Ventilation**: Makeup air discharges immediately adjacent to hood face, flowing across appliances before capture by exhaust. This efficient approach uses 30-50% less makeup air volume than ceiling discharge methods. Installation requires careful coordination to prevent cross-drafts disrupting hood capture.

**Ceiling Diffusers**: Makeup air discharges through ceiling diffusers 8-12 feet from cooking line. Lower velocity discharge (300-500 FPM) prevents hood disruption while providing gentle air mixing. Requires greater makeup air volume since much air mixes with kitchen environment rather than directly feeding exhaust.

**Short-Circuit Hood**: Makeup air discharges from perimeter of hood face through dedicated plenum. Air path flows directly from supply to exhaust minimizing mixing with kitchen. Most efficient method achieving makeup volumes 40-60% of exhaust while maintaining proper hood operation. Higher first cost ($20-30/CFM versus $10-15/CFM for conventional) limits adoption to high-performance installations.

## Exhaust System Design

### Ductwork Requirements

Kitchen exhaust ductwork requires 16-gauge welded or continuously brazed carbon steel construction for grease duct service per NFPA 96. Minimum duct velocity maintains 500 FPM preventing grease settling while avoiding excessive pressure drop. Calculate duct diameter:

$$D = \sqrt{\frac{4 \times CFM}{60 \times \pi \times V}}$$

For 4,800 CFM at 1,500 FPM velocity:
$$D = \sqrt{\frac{4 \times 4,800}{60 \times 3.14 \times 1,500}} = 0.80 \text{ ft = 9.6 inches}$$

Use next standard size: 10-inch diameter round duct.

Ductwork runs independently for each hood, sloping minimum 1/4 inch per foot toward hood for grease drainage. Horizontal runs minimize to reduce grease accumulation points. All penetrations through fire-rated construction use listed grease duct assemblies.

### Exhaust Fan Selection

Upblast centrifugal fans designed for grease-laden vapor service mount on roof above duct termination. Fan construction features:
- Grease drainage provisions returning to duct
- Grease-resistant motor and drive components
- Spark-resistant construction (aluminum, stainless steel)
- Hinged or removable panels for cleaning access

Fan capacity accounts for system pressure drop including duct friction, hood entry loss, filters, and discharge stack. Total static pressure typically ranges 1.5-3.0 in. wc for properly designed systems. Size fan for design CFM at total system static pressure plus 20% margin for filter loading.

Variable speed drives modulate exhaust based on cooking activity, reducing fan energy 30-50% during low-production periods. Drive must be listed for use in kitchen exhaust application with grease-resistant construction.

## Dining Room Conditioning

Restaurant dining areas require 70-75°F temperature control with humidity maintained 40-55% RH for guest comfort. Loads include envelope gains, lighting (1.0-1.5 W/ft²), occupancy (7-15 ft²/person), and infiltration from entrance doors.

### Ventilation Requirements

ASHRAE 62.1 mandates 7.5 cfm/person for restaurants with additional 0.18 cfm/ft² area component. For 2,000 ft² dining room with 150-person capacity:

$$OA = (7.5 \times 150) + (0.18 \times 2,000) = 1,125 + 360 = 1,485 \text{ CFM}$$

Demand-controlled ventilation using CO₂ sensors reduces outdoor air during low occupancy. During 50% occupancy:
$$OA_{reduced} = (7.5 \times 75) + (0.18 \times 2,000) = 923 \text{ CFM (38% reduction)}$$

Annual energy savings from DCV range 15-30% of dining room HVAC costs depending on occupancy patterns and climate.

### System Integration

Dining room HVAC systems maintain slight positive pressure (0.02-0.05 in. wc) relative to kitchen preventing odor migration. Transfer air from dining to kitchen through door undercuts and transfer grilles provides portion of kitchen makeup air while maintaining pressure relationship.

Air distribution uses low-velocity ceiling diffusers (400-600 FPM) for draft-free comfort. Returns locate away from kitchen entrance to prevent short-circuiting of supply air and maintain proper air flow patterns.

## Fire Suppression System Coordination

### UL 300 Wet Chemical Systems

Type I hoods require automatic fire suppression systems protecting both hood interior and cooking surfaces. UL 300 wet chemical systems replaced older dry chemical systems (UL 300A) effective in 1994 due to improved performance on high-temperature cooking oil fires reaching 650-700°F.

Wet chemical agent (potassium carbonate or acetate solution) discharges through nozzles positioned above appliances, providing:
- Chemical reaction with cooking oil creating saponification (soap layer)
- Cooling effect reducing oil temperature below auto-ignition point (600-700°F)
- Vapor suppression blanket preventing re-ignition

### System Integration Requirements

**Exhaust Fan Shutdown**: Fire suppression system activation immediately stops exhaust fan through hardwired interlock. Continued fan operation during discharge would pull suppression agent up through duct reducing effectiveness at cooking surface. Time-delay relay permits 30-60 second fan overrun after manual system reset for smoke clearance.

**Fuel and Power Cutoff**: Gas solenoid valves and electrical contactors automatically shut off energy to cooking appliances when suppression activates. Cutoff occurs at main supply point serving hood, not individual appliances, ensuring complete energy isolation. Manual reset required before restoring fuel/power after discharge event.

**Makeup Air Coordination**: Most designs maintain makeup air operation during fire event. Continuing makeup air prevents building depressurization that could backdraft smoke through ductwork or create difficulty opening exit doors. Alternative approach shuts makeup simultaneously with exhaust in small installations where building pressure change is minimal.

**HVAC Integration**: Dining room HVAC continues operation during kitchen fire suppression. Fire/smoke dampers in transfer air openings between kitchen and dining room close on system activation preventing smoke migration. BMS receives alarm signal from suppression panel for occupant notification and emergency response coordination.

### Detection and Actuation

Fusible link detection mounts in hood at 10-12 inch spacing along appliance line. Link temperature rating (360-500°F) selected based on normal cooking temperatures plus margin. High-temperature cooking like wok stations or charbroilers use 500°F links; standard ranges use 360-400°F links.

Manual pull stations locate at kitchen exits within 10-20 feet of protected equipment and clearly visible. Illuminated signage marks pull station location. Hotel kitchens typically require 2-3 manual pulls depending on kitchen size and exit configuration.

System discharge initiates when any fusible link melts or manual pull activates. All nozzles discharge simultaneously providing complete coverage of cooking surfaces and hood interior. Discharge duration ranges 5-20 seconds depending on system size and protected area.

### Maintenance and Testing

Fire suppression systems require semi-annual inspection by certified technician verifying:
- Nozzle caps intact and properly oriented
- Fusible links free of grease buildup and within expiration date
- Agent cylinder pressure within acceptable range (factory-charged systems) or weight verification (bladder tanks)
- Detection and actuation components operational
- Fuel shutoff valves functioning properly

Annual testing includes simulated discharge (water test) verifying proper nozzle spray pattern and coverage. Full agent discharge requires complete system recharge at significant cost ($1,500-3,000 for typical hotel kitchen hood).

## Kitchen Worker Comfort

### Temperature Control Challenges

Commercial kitchens generate 50,000-150,000 Btu/hr heat gain from cooking appliances creating uncomfortable working environment without proper HVAC design. Appliance radiant heat creates local hot spots reaching 120-140°F within 3 feet of cooking surfaces while kitchen perimeter areas remain 85-95°F.

**Heat Gain Components**:
- Appliance radiation: 30-40% of nameplate rating
- Convective plume: 40-50% of nameplate rating (captured by hood)
- Lighting and equipment: 1.5-2.5 W/ft²
- Occupancy: 250-400 Btu/hr per worker

For typical hotel kitchen with 200 kW cooking equipment:
$$Q_{total} = (200 \times 3,412 \times 0.35) + (2,000 \times 2.0 \times 3.412) + (8 \times 300) = 238,840 + 13,648 + 2,400 = 254,888 \text{ Btu/hr}$$

Hood capture removes 60-70% of total appliance heat, leaving 75,000-100,000 Btu/hr released to kitchen space.

### Spot Cooling Solutions

Direct makeup air at workers provides localized cooling without attempting full kitchen conditioning. Supply air 10-20°F cooler than ambient discharged at low velocity (300-500 FPM) near worker positions creates comfort improvement through convective cooling.

Ceiling-mounted spot coolers discharge conditioned air in focused pattern covering 50-75 ft² work zones. Small air-cooled direct expansion units (2-3 tons) serve individual stations with dedicated supply diffuser. Installation at 8-10 feet above floor provides effective cooling while avoiding interference with hood capture.

Personal cooling fans mounted on adjustable arms permit worker-directed airflow. Low-velocity fans (200-300 FPM) provide evaporative cooling effect without creating hood disruption. Coordinate fan placement to avoid direct airflow toward hood face.

### Air Quality Management

Kitchen air quality depends on effective capture of cooking effluent and adequate dilution ventilation. Poor air quality manifests as eye irritation, breathing difficulty, and excessive heat stress reducing worker productivity and increasing turnover.

**Recommended Conditions**:
- Temperature: 75-85°F (difficult to achieve; 80-90°F more realistic)
- Relative humidity: 50-60% RH
- Air changes: 15-30 ACH based on kitchen volume
- CO₂ concentration: Below 1,000 ppm
- Particulate matter: Maintain PM2.5 below 35 μg/m³

Supplemental kitchen conditioning beyond makeup air requires 5-10 tons per 1,000 ft² kitchen area. Direct expansion split systems or dedicated outdoor air units supply conditioned air through ceiling diffusers positioned away from hood face. Energy recovery from exhaust heat offsets conditioning cost in installations justifying capital investment.

### Noise Control

Kitchen exhaust systems generate 70-85 dBA sound levels from fan operation creating communication difficulty and hearing protection requirements. Upblast exhaust fans mounted directly on roof transmit noise into kitchen through ductwork.

**Noise Reduction Methods**:
- In-line silencers in exhaust duct (10-15 dB reduction)
- Flexible duct connectors isolating fan vibration
- Fan speed reduction during low cooking periods
- Sound-insulated fan housings
- Distance separation between fan and occupied areas

Target kitchen ambient noise below 70 dBA for acceptable working environment. Areas exceeding 85 dBA require hearing protection per OSHA requirements.

## NFPA 96 Compliance Summary

Key NFPA 96 requirements for commercial kitchen exhaust systems:

- **Hood Construction**: Listed Type I or II construction, 18-gauge minimum, welded corners, grease collection with removable catch trough
- **Ductwork**: 16-gauge welded/brazed steel, independent ducts per hood, 1/4 in/ft slope, accessible for cleaning
- **Fans**: Listed for grease service, hinged/removable for inspection, upblast discharge, minimum 40 in. from property line
- **Clearances**: 18 inches minimum from unprotected combustibles, reduced with approved protection systems
- **Fire Suppression**: UL 300 listed wet chemical system required for Type I hoods, manual pull station, fuel/power shutoff
- **Cleaning**: Professional cleaning frequency based on accumulation (daily to annually), with documentation
- **Access Panels**: Provided every 12 feet of horizontal run and changes of direction, minimum 12×12 inch opening

Compliance verification occurs through plan review, installation inspection, and ongoing maintenance documentation. Fire marshal approval required before kitchen operation begins.
