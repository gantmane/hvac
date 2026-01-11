---
title: "Refuge Areas and Safe Havens HVAC"
description: "HVAC system design for high-rise refuge areas, areas of refuge, safe havens, and fire service access elevator lobbies. Pressurization requirements, smoke control, emergency power, and IBC compliance for protected spaces in tall buildings."
weight: 8
---

Refuge areas and safe havens in high-rise buildings provide protected spaces where occupants unable to immediately evacuate can await assistance or firefighter-assisted evacuation during fire emergencies. These spaces require dedicated HVAC systems maintaining tenable conditions through smoke exclusion, adequate ventilation, and environmental control. The design of refuge area mechanical systems represents critical life safety infrastructure subject to stringent code requirements and rigorous performance criteria.

## Refuge Area Classification and Requirements

Building codes distinguish several types of protected spaces in tall buildings, each with specific HVAC requirements:

**Areas of Refuge** (IBC Section 1009.6): Accessible spaces where occupants unable to use stairs can await assistance. Required in multi-story buildings lacking complete sprinkler protection. Each area of refuge must accommodate wheelchair spaces based on occupant load and connect to accessible means of egress. HVAC requirements include protection from smoke infiltration through pressurization or other approved smoke control methods.

**Refuge Areas** (IBC Section 412, High-Rise Buildings): Protected floor areas designated for occupant staging during phased evacuation. High-rise buildings may incorporate refuge areas at intervals within the vertical evacuation path, reducing evacuation time and providing rest locations for mobility-impaired occupants. Mechanical ventilation and smoke control systems maintain safe conditions for extended occupancy periods.

**Fire Service Access Elevator Lobbies** (IBC Section 3007): Two-hour fire-rated lobbies serving fire department elevators in buildings exceeding 120 feet height. These lobbies provide firefighter staging areas and protected elevator access to upper floors. Smoke protection systems prevent smoke infiltration during fire department operations.

**Smoke-Protected Seating Areas** (IBC Section 1029): Stadium and arena seating areas where occupants await evacuation. Mechanical smoke control maintains visibility and tenable conditions during evacuation from large assembly spaces.

All refuge area types share fundamental HVAC design requirements: smoke exclusion, breathable atmosphere maintenance, emergency power supply, and reliable operation under fire conditions.

## Smoke Control System Design Approaches

Refuge areas employ pressurization as the primary smoke control strategy. Positive pressure differential relative to adjacent spaces prevents smoke infiltration through door openings, construction gaps, and penetrations. Alternative approaches include natural ventilation (limited applicability) and dedicated smoke exhaust (less common for refuge areas).

**Positive Pressure Differential**: Refuge area maintained at minimum 0.05 inches water column (12.5 Pa) positive pressure relative to adjacent spaces per IBC and NFPA 92. This differential exceeds forces driving smoke movement through typical leakage paths. Design pressure typically ranges from 0.10 to 0.30 inches w.c. providing margin for uncertainty in leakage area, wind effects, and system performance variation.

Pressure must be maintained under two distinct conditions:
1. All doors closed (baseline pressurization)
2. Any single door open to adjacent space (door-open makeup air)

Door-open condition requires substantially higher airflow, often 10-20 times the closed-door requirement. Supply fan sizing, control strategy, and pressure relief design must accommodate this range.

**Supply Airflow Calculation**: NFPA 92 provides calculation methodology for determining supply airflow based on leakage area and pressure requirements. Leakage area derives from construction tightness class (typical range: 0.3-1.0 cfm/ft² at 0.30 inches w.c.), door undercut area, and construction penetrations.

For closed-door condition:
Q = AL√(2ΔP/ρ)

For door-open condition:
Q = 2610 × Aᵈ × W × √ΔP

Where design must satisfy both conditions simultaneously through variable volume supply or pressure relief.

**Control Strategies**: Refuge area pressurization control systems must respond to changing conditions while maintaining required pressure differential. Control approaches include:

- Variable speed drive (VFD) modulating supply fan airflow based on pressure feedback
- Staged barometric relief dampers opening at preset pressure thresholds
- Multiple fixed-speed fans staging based on pressure measurement
- Combined VFD and relief damper systems providing primary control and backup relief

Pressure sensors measuring differential pressure between refuge area and adjacent corridor provide feedback for closed-loop control. Sensor accuracy (±0.005 inches w.c. or better) and rapid response time (<5 seconds) ensure stable control.

## Ventilation and Air Quality Requirements

Beyond smoke exclusion, refuge areas require adequate ventilation maintaining oxygen levels and limiting carbon dioxide accumulation during occupancy. Occupant density in refuge areas may exceed normal building areas as evacuees congregate awaiting assistance.

Ventilation rate calculation based on occupant load:
- Minimum outdoor air: 15-20 cfm per person
- Occupant density: per IBC assembly occupancy load factors or higher
- Makeup air volume for pressurization often exceeds ventilation requirement
- 100% outdoor air supply eliminates recirculation of potential contamination

For refuge area accommodating 50 occupants:
Q_ventilation = 50 persons × 20 cfm/person = 1000 cfm minimum

Pressurization makeup air requirement typically exceeds ventilation requirement, making dedicated ventilation calculation secondary to smoke control analysis. However, control sequences should verify minimum ventilation during normal operation.

## Air Supply Source and Quality

Supply air for refuge areas must originate from location unlikely to become smoke-contaminated during building fire. Intake strategies include:

**Dedicated Rooftop Intake**: Most reliable approach for tall buildings. Rooftop location remains above fire floor discharge in typical scenarios. Minimum 20-foot separation from potential contamination sources (exhaust fans, relief openings, cooling tower discharge).

**Smoke Detection in Supply Duct**: Duct smoke detectors provide additional protection against contaminated supply air. Detection triggers alarm, system shutdown, or switchover to alternate air source depending on design philosophy. Detector location: downstream of intake, upstream of supply fan.

**Filtration**: Supply air filtration protects occupants from particulate contamination. Minimum MERV 13 particulate filtration recommended. Activated carbon filtration (gaseous filtration) provides additional protection against toxic fire gases in supply air but requires substantial installation space and ongoing maintenance.

## Emergency Power Requirements

IBC mandates refuge area HVAC systems connect to emergency power, ensuring operation continues following normal power failure. Emergency power specifications:

- Automatic transfer to emergency power source
- Transfer time: maximum 60 seconds (10 seconds typical for life safety loads)
- Minimum run time: 2 hours (4 hours for healthcare occupancies)
- Emergency power source: standby generator or battery system
- Power connection per NFPA 70 (NEC) Article 700 (Emergency Systems)

Emergency power load calculation must include:
- Supply fan full-load amperage
- Control system and monitoring equipment
- Pressure monitoring sensors and alarms
- Emergency lighting in refuge area
- Communication system power

Generator-based emergency power requires fuel supply, automatic starting system, and load transfer switch. Battery/UPS systems provide instantaneous backup but limited run time may necessitate larger battery banks to achieve code-required duration.

## System Integration and Control

Refuge area HVAC systems integrate with building fire alarm, smoke control, and emergency communication systems. Integration points include:

**Fire Alarm System**: Fire alarm activation triggers refuge area pressurization system startup. Specific floor or zone fire detection may activate only affected refuge areas or activate entire building complement depending on evacuation strategy.

**Building Automation System (BAS)**: Refuge area HVAC monitoring integrates with BAS for status indication, trending, and maintenance alerts during non-emergency operation. Emergency operation typically bypasses BAS control, operating through dedicated hardwired controls.

**Fire Command Center**: Manual control provisions in fire command center permit fire department override of automatic sequences. Status indication displays system operation, pressure differential, and alarm conditions.

**Stairwell Pressurization**: Refuge areas adjacent to pressurized stairwells require pressure relationship analysis preventing backflow or pressure imbalance. Design approach maintains compatible pressure gradients: stairwell pressure > refuge area pressure > building floor pressure.

## Testing, Commissioning, and Maintenance

Refuge area HVAC systems require comprehensive acceptance testing demonstrating compliance with design intent and code requirements. Testing protocol per NFPA 92 includes:

**Pressure Differential Testing**:
- Measure pressure with all doors closed (verify ≥0.05 inches w.c.)
- Open each door individually, measure maintained pressure (verify ≥0.05 inches w.c.)
- Document pressure at design conditions

**Airflow Verification**:
- Measure supply airflow at fan outlet
- Compare to design calculations
- Verify adequate volume for both closed and open-door conditions

**Control System Testing**:
- Simulate pressure variations, verify control response
- Test emergency power transfer and system operation on emergency power
- Verify alarm annunciation and status indication
- Test manual override controls in fire command center

**Integration Testing**:
- Verify fire alarm system activation triggers pressurization startup
- Test smoke detection interlocks
- Confirm proper sequencing with building smoke control systems

Ongoing maintenance requirements include quarterly pressure testing, annual emergency power transfer test, and filter replacement per manufacturer recommendations. Documentation of testing and maintenance provides evidence of code compliance and system readiness.

## Design Considerations and Best Practices

Successful refuge area HVAC design requires consideration of factors beyond minimum code compliance:

- Acoustic design: high supply airflow generates noise; silencers may be required
- Door opening forces: excessive pressure (>0.35 inches w.c.) creates accessibility problems
- Multiple refuge areas: dedicated systems versus shared infrastructure
- Phased evacuation compatibility: staging activation with evacuation sequence
- Firefighter operations: system supports fire department access, not just occupant refuge
- Building stack effect: tall building pressure distributions interact with refuge area pressurization
- Wind effects: exterior pressure variations affect achievable interior differential

Refuge area locations within building floor plan affect HVAC system effectiveness. Locations adjacent to building core (near stairwells and elevators) minimize exposure to exterior wind pressure. Locations with minimal perimeter exposure reduce construction complexity for achieving required tightness.
