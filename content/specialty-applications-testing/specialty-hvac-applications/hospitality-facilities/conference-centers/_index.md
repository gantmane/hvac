---
title: "Conference Centers and Ballrooms"
description: "High-density occupancy HVAC design, flexible space requirements, VAV systems, demand-controlled ventilation, and AV system integration."
date: "2026-01-04"
weight: 7
tags: ["conference center HVAC", "ballroom ventilation", "VAV systems", "demand-controlled ventilation", "high occupancy"]
categories: ["Specialty Applications"]
---

## High Occupancy Density Characteristics

Conference centers and ballrooms experience extreme occupancy density variations from empty (setup/teardown) to peak events at 7-10 ft²/person. A 10,000 ft² ballroom transitions from zero occupants during setup to 1,000+ attendees during banquets, conferences, or receptions. This 100:1 load variation requires flexible HVAC systems capable of efficient operation across the entire range.

### Load Analysis

Peak occupancy drives design cooling loads through metabolic heat generation and required ventilation air conditioning. Calculate occupant sensible and latent loads:

**Sensible Load per Person**:
- Seated at rest (theater): 250 Btu/hr
- Seated moderate activity (banquet): 300 Btu/hr
- Standing/light activity (reception): 350 Btu/hr

**Latent Load per Person**:
- Seated at rest: 150 Btu/hr
- Seated moderate activity: 200 Btu/hr
- Standing/light activity: 250 Btu/hr

For 10,000 ft² ballroom with 1,000 seated attendees at moderate activity:
$$Q_{sensible} = 1,000 \times 300 = 300,000 \text{ Btu/hr}$$
$$Q_{latent} = 1,000 \times 200 = 200,000 \text{ Btu/hr}$$

Total occupant load: 500,000 Btu/hr (42 tons) from people alone, before accounting for lighting, audio/visual equipment, envelope gains, and outdoor air loads.

Lighting contributes 1.5-2.5 W/ft² depending on fixture type and event requirements. Audio/visual equipment adds 5-15 kW for typical installations, increasing to 50-100 kW for major events with extensive video walls, sound systems, and theatrical lighting.

### Ventilation Loads

Outdoor air ventilation often dominates conference center cooling loads, particularly in humid climates. ASHRAE 62.1 requires 5 cfm/person for conference/multipurpose spaces, increasing to 7.5 cfm/person without operable windows. For 1,000-person occupancy:

$$OA = 7.5 \times 1,000 = 7,500 \text{ CFM}$$

In humid summer conditions (90°F/70% RH outdoor, 75°F/50% RH indoor), conditioning this outdoor air requires approximately:
$$Q_{OA} = 7,500 \times 4.5 \times \Delta h \approx 400,000 \text{ Btu/hr (33 \text{ tons})}$$

This outdoor air load exceeds internal gains, explaining why proper outdoor air control through demand-controlled ventilation provides greatest energy savings in conference spaces.

## Flexible Space Requirements

Hotel ballrooms and conference centers reconfigure frequently through movable partitions subdividing large spaces into breakout rooms or combining small rooms for larger events. HVAC systems must accommodate these reconfigurations without significant operator intervention or guest comfort compromise.

### Zoning Strategy

Provide independent HVAC zones aligned with partition wall locations. A 15,000 ft² divisible ballroom requires 3-6 zones allowing operation as single space, two halves, or three thirds. Each zone needs:

- Dedicated VAV terminal unit with controls
- Separate thermostat and occupancy sensing
- Outdoor air damper control coordinating with DCV system
- Override capability for event scheduling

Zone sizing balances flexibility against equipment cost. Excessive zones (10+ zones for 15,000 ft²) provide maximum flexibility but increase first cost and control complexity. Insufficient zones (2 zones) limit operational flexibility when partial space use occurs.

### Supply Air Distribution

Fixed ceiling diffusers serve all partition configurations, with airflow patterns designed to avoid short-circuiting regardless of partition position. Space diffusers on 8-12 foot centers using high-induction diffusers (4-6:1 induction ratio) to promote mixing and prevent stratification in high-ceiling ballrooms (12-18 feet).

Return air design accommodates partitions through:
- **Over-partition return**: Partitions stop 12-18 inches below ceiling allowing return air flow over top; simplest approach but transmits sound between adjacent spaces
- **Ducted returns**: Separate return ducts serve each zone with motorized dampers closing when zone is unoccupied; better sound isolation but higher first cost
- **Perimeter low returns**: Wall-mounted returns below partition track; excellent sound control, requires coordination with partition system

## VAV System Design

Variable air volume systems provide optimal performance for conference spaces through capacity modulation matching actual loads. System components include:

### Primary AHU Configuration

Dedicated air-handling units serve conference areas separately from guest rooms due to vastly different operating schedules and load profiles. Unit sizing accounts for peak occupancy diversity—a hotel hosting multiple simultaneous events rarely sees all conference spaces at maximum occupancy.

AHU components for conference center service:
- **Supply fans**: Variable speed with 30-100% turndown; size for 0.8-1.0 CFM/ft² at peak occupancy
- **Cooling coils**: 10-12°F approach temperature, 52-55°F leaving air temperature for humidity control
- **Heating coils**: Hot water or electric, sized for morning warm-up and perimeter heat
- **Economizer**: Air-side economizer with integrated control for free cooling during mild weather
- **Filtration**: MERV 11-13 to protect coils and maintain air quality for close-packed occupants

Calculate required supply airflow for 10,000 ft² ballroom:
$$CFM_{supply} = \frac{Q_{sensible}}{1.08 \times (T_{room} - T_{supply})} + CFM_{ventilation}$$

With 500,000 Btu/hr total sensible load, 75°F room temperature, 55°F supply temperature:
$$CFM_{supply} = \frac{500,000}{1.08 \times 20} + 7,500 = 23,148 + 7,500 = 30,648 \text{ CFM}$$

This represents 3.1 CFM/ft² at peak occupancy, reducing to 0.3-0.5 CFM/ft² during unoccupied or light-occupancy periods.

### VAV Terminal Units

Each zone employs pressure-independent VAV boxes with hot water reheat coils or electric heat. Box minimum airflow settings account for ventilation requirements:

$$CFM_{min} = \frac{OA_{zone}}{1 - \% OA_{primary}}$$

For zone requiring 2,500 CFM outdoor air with primary AHU at 30% outdoor air:
$$CFM_{min} = \frac{2,500}{1-0.30} = 3,571 \text{ CFM minimum}$$

This ensures adequate outdoor air delivery even when zone cooling loads are minimal. During unoccupied periods, minimum airflow reduces to zero (box closes) with outdoor air damper also closing to eliminate conditioning cost for vacant spaces.

### Static Pressure Control

VAV system static pressure resets based on zone demand, maintaining pressure sufficient to satisfy most-demanding zone while minimizing fan energy. Reset strategies include:

**Zone-Request Reset**: System pressure resets downward until one zone damper reaches 90-95% open, indicating need for more pressure. This demand-based approach minimizes average static pressure and fan energy.

**Trim-and-Respond**: Pressure incrementally reduces (trims) every few minutes until zone requests increase, then responds with small pressure increase. Iterative process finds optimal pressure setpoint balancing zone needs against fan power.

Typical operating static pressure ranges from 1.0-2.5 in. wc at design, resetting to 0.6-1.2 in. wc during light-load conditions. Fan power varies with cube of speed, so reducing static pressure from 2.0 to 1.0 in. wc cuts fan power approximately 65%.

## Demand-Controlled Ventilation

DCV systems modulate outdoor air based on measured CO₂ concentration, providing outdoor air proportional to actual occupancy rather than design maximum. This approach saves 30-60% of conference center HVAC energy by avoiding over-ventilation during low-occupancy periods.

### CO₂ Sensor Placement

Wall-mounted sensors install in each conference zone at 4-5 feet height (breathing zone). Multiple sensors per zone improve accuracy in large spaces—provide one sensor per 2,500-3,500 ft² of floor area. Sensors must locate away from doors, outdoor air intakes, and exhaust grilles to measure representative space CO₂.

Sensor accuracy specification requires ±50 ppm at concentrations below 2,000 ppm. This precision permits reliable control without excessive ventilation or inadequate fresh air. Automatic baseline calibration (ABC) compensates for sensor drift over time by assuming periodic exposure to outdoor CO₂ levels (approximately 400-450 ppm).

### Control Algorithm

DCV controllers modulate outdoor air damper position to maintain space CO₂ below target setpoint, typically 1,000-1,100 ppm. Control equation relates CO₂ concentration to required ventilation:

$$CFM_{OA} = \frac{N \times G}{(C_s - C_o) \times 0.075}$$

where:
- $N$ = number of occupants
- $G$ = CO₂ generation rate per person (0.3-0.4 CFM/person)
- $C_s$ = space CO₂ concentration (ppm)
- $C_o$ = outdoor CO₂ concentration (ppm)

For space at 1,000 ppm with 400 ppm outdoor and 0.35 CFM/person generation:
$$N = \frac{CFM_{OA} \times (1,000-400) \times 0.075}{0.35} \approx CFM_{OA} \times 12.9$$

This relationship allows real-time calculation of required outdoor air based on measured CO₂ levels, implementing proportional control that ramps ventilation as occupancy increases.

### Energy Savings Calculation

Calculate annual DCV energy savings by comparing constant outdoor air versus demand-controlled operation. For conference space operating 2,500 hours annually with average 35% occupancy:

**Baseline (constant OA)**: 7,500 CFM × 2,500 hours = 18.75 million CFM-hours

**DCV (proportional to occupancy)**: 7,500 CFM × 0.35 × 2,500 hours = 6.56 million CFM-hours

Outdoor air reduction: 65% fewer CFM-hours requiring conditioning. At $0.15/kWh electricity and 1.0 kW per 1,000 CFM cooling energy use:

$$Savings = \frac{(18.75-6.56) \times 10^6 \times 1.0}{1,000} \times \$0.15 = \$1,828/year$$

For 30,000 ft² of conference space, annual savings reach $5,500-$8,000 justifying $15,000-$25,000 DCV system first cost with 2-4 year payback.

## Audio/Visual System Integration

Modern conference centers integrate HVAC controls with audio/visual and room scheduling systems for coordinated operation. Integration objectives include:

### Noise Control

AV presentations require quiet HVAC operation, typically NC 30-35 in conference rooms and NC 35-40 in ballrooms. Achieve this through:

- VAV box selection for low-speed operation (200-400 FPM duct velocity at design)
- Sound-lined ductwork (1-inch liner minimum, 2-inch for critical spaces)
- Flexible duct connections at terminals preventing vibration transmission
- Supply diffuser velocity limitation (400-600 FPM)

During presentations, HVAC controls reduce supply airflow to minimum (eliminating reheat noise) and slow fan speeds to reduce air noise. Brief periods of minimal cooling prove acceptable given large space thermal mass moderating temperature drift.

### Equipment Heat Loads

Projection equipment, sound systems, and video walls generate substantial sensible loads. A typical major conference room might include:
- Laser projector: 2,000-3,000 Btu/hr
- Sound system amplifiers: 3,000-5,000 Btu/hr
- Video processing equipment: 1,500-2,500 Btu/hr
- Theatrical lighting: 10,000-30,000 Btu/hr (if used)

Total AV heat load: 15,000-40,000 Btu/hr depending on installation. This load operates intermittently, creating dynamic load conditions that VAV systems handle through capacity modulation. Equipment rooms housing AV components require dedicated cooling operating continuously to prevent temperature-sensitive electronics damage.

### Control Integration

Building automation system integrates with room scheduling software and AV control systems:

1. **Pre-event conditioning**: HVAC ramps up 1-2 hours before scheduled event based on calendar
2. **Occupancy coordination**: Lights-on signal from AV system confirms occupancy, preventing premature setback
3. **Presentation mode**: AV system signals HVAC to minimize noise during presentations
4. **Post-event shutdown**: Lights-off or AV system power-down triggers HVAC setback within 15-30 minutes

This integration reduces energy consumption 20-35% compared to constant-volume operation while maintaining comfort during actual event periods.

## System Efficiency Optimization

Conference center HVAC represents 35-45% of hotel energy consumption despite comprising only 15-25% of conditioned floor area. Optimization strategies include:

- **Schedules**: Operate systems only during scheduled events plus pre/post conditioning periods
- **Setback**: Maintain 80-85°F cooling setback and 55-60°F heating setback when unoccupied
- **Economizer**: Maximize free cooling during mild weather (50-60°F outdoor temperature)
- **Heat recovery**: Capture exhaust energy during peak ventilation periods for makeup air preheating
- **Chilled water reset**: Increase chilled water temperature to 50-55°F during low-humidity periods reducing chiller energy

Combined optimization reduces conference center HVAC energy by 40-55% compared to constant-volume, always-on operation at fixed setpoints.
