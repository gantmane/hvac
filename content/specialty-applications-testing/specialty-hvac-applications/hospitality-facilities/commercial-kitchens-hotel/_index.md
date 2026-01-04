---
title: "Hotel Commercial Kitchens"
description: "Kitchen exhaust hood design, makeup air systems, grease capture, NFPA 96 requirements, and dining room conditioning for hotel restaurants."
date: "2026-01-04"
weight: 6
tags: ["kitchen exhaust", "makeup air", "NFPA 96", "Type I hood", "restaurant HVAC"]
categories: ["Specialty Applications"]
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
