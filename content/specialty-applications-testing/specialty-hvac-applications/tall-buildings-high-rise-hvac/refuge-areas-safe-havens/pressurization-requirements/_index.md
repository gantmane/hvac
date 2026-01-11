---
title: "Refuge Area Pressurization Requirements"
description: "HVAC pressurization system design for high-rise refuge areas including positive pressure maintenance, makeup air supply, pressure monitoring, and emergency power requirements per IBC and NFPA 92."
weight: 2
---

Refuge areas and areas of refuge in high-rise buildings require dedicated mechanical pressurization systems to maintain tenable conditions during fire emergencies. These systems prevent smoke infiltration by creating positive pressure differentials relative to adjacent spaces, ensuring occupants awaiting evacuation or rescue remain in breathable atmosphere. Pressurization requirements derive from International Building Code provisions and NFPA 92 smoke control standards.

## Code-Required Positive Pressure

IBC Section 1009.6 and NFPA 92 establish minimum pressure differentials for refuge areas. The fundamental requirement mandates positive pressure of at least 0.05 inches water column (12.5 Pa) with respect to adjacent spaces under two conditions:

1. All communicating doors closed
2. Any single door open to adjacent space

The dual requirement ensures smoke exclusion during normal refuge area operation (doors closed) and during entry/exit events when doors open momentarily. Maintaining pressure with doors open requires substantially higher air supply volume than closed-door conditions due to airflow through the door opening.

Design pressure differential typically ranges from 0.10 to 0.30 inches w.c. (25-75 Pa) with doors closed, providing margin above code minimum and compensating for leakage variation, wind effects, and system degradation. Excessive pressure (>0.35 inches w.c.) creates door-opening force challenges, potentially preventing entry by weak or injured occupants.

## Makeup Air Supply System Design

Refuge area pressurization requires dedicated air supply from mechanical equipment located outside the smoke zone. Supply fan configurations include:

**Dedicated Refuge Area Fan**: Individual fan serving single refuge area or group of refuge areas on common fire-rated shaft. Sizing based on leakage area calculation plus door-open makeup air requirement. Typical supply rates: 0.5-2.0 cfm/ft² of refuge area floor area with doors closed; 3000-5000 cfm per door opening when any door opens.

**Staged Pressurization from Building HVAC**: Building air handling system provides refuge area supply through fire/smoke dampers that close in non-refuge zones while remaining open to refuge areas. Requires complex control sequencing and may not provide adequate volume for large door openings.

**Stairwell Pressurization Integration**: Refuge areas adjacent to pressurized stairwells may share supply air infrastructure if stairwell system capacity accounts for additional refuge area volume. Careful analysis prevents undermining stairwell pressure when refuge area doors open.

Supply air volume calculation methodology per NFPA 92:

**Closed Door Condition**:
Q = AL√(2ΔP/ρ)

Where:
- Q = volumetric flow rate (cfm)
- A = total leakage area (ft²)
- L = leakage coefficient (typically 0.65)
- ΔP = pressure differential (lbf/ft²)
- ρ = air density (lbm/ft³)

**Door Open Condition**:
Q = 2610 × Aᵈ × W × √ΔP

Where:
- Aᵈ = door area (ft²)
- W = effective flow width
- ΔP = pressure differential (inches w.c.)

Design requires calculating both conditions and selecting supply volume meeting the more demanding scenario, typically door-open condition.

## Pressure Monitoring and Control

Automated pressure monitoring ensures pressurization system effectiveness throughout the emergency event. Differential pressure sensors measure refuge area pressure relative to adjacent corridor or floor area. Typical sensor specifications:

- Measurement range: 0-0.50 inches w.c. (0-125 Pa)
- Accuracy: ±2% of reading or ±0.005 inches w.c., whichever is greater
- Response time: <5 seconds
- Output: 4-20 mA or digital protocol (BACnet, Modbus)

Control strategies for maintaining target pressure:

**Variable Speed Fan Control**: Supply fan speed modulates based on measured pressure differential. VFD adjusts airflow to compensate for door position, wind effects, and leakage variation. Provides most stable pressure control but requires continuous power to VFD during emergency operation.

**Staged Barometric Dampers**: Multiple relief dampers weighted to open at different pressure thresholds relieve excess pressure without fan speed modulation. Passive system continues functioning if control power fails. Less precise than VFD control.

**Multiple Fixed-Speed Fans**: Staging multiple constant-speed fans provides coarse pressure adjustment. Energizing additional fans increases flow when doors open; de-energizing fans prevents over-pressurization. Simple and reliable but limited resolution.

Control panel location requires accessibility for fire department override while remaining outside potential smoke exposure areas. Many installations locate control panels in building fire command center with status indication on fire alarm annunciator panel.

## Emergency Power Requirements

IBC Section 1009.6.3 mandates refuge area pressurization systems connect to emergency power supply in accordance with Section 2702. Emergency power must activate automatically upon normal power failure and provide operation for minimum 2 hours (4 hours for Group I-2 occupancies). NFPA 70 (NEC) Article 700 establishes installation requirements for emergency power circuits.

Emergency power source options:

**Generator**: Standby or emergency generator with automatic transfer switch (ATS). Generator must achieve rated speed and voltage within 10 seconds of power failure for emergency systems. Refuge area pressurization loads typically connect to life safety branch of emergency distribution.

**Battery/Inverter Systems**: UPS systems or battery-powered fans provide immediate backup without transfer delay. Limited run time (typically 90-120 minutes) may fall short of code requirements unless substantial battery capacity provided. Advantageous for smaller refuge areas with modest flow requirements.

Electrical circuit design considerations:
- Wiring methods per NEC Article 700 (emergency systems) or Article 701 (legally required standby)
- Dedicated transfer switch or section of main fire pump/life safety transfer switch
- Circuit breaker or fused disconnect accessible to fire department
- Status monitoring integrated with building fire alarm system
- Emergency lighting in equipment rooms for maintenance access during power failure

## Makeup Air Intake Location

Supply air source for refuge area pressurization must originate from location unlikely to become smoke-contaminated during building fire. Intake placement strategies:

1. **Rooftop Intake**: Most common approach, utilizing building rooftop location remote from fire floors. Requires evaluation of wind effects that may draw smoke upward along building exterior. Minimum 20 feet horizontal separation from potential smoke sources (exhaust fans, relief openings, elevator machine room vents).

2. **Mid-Level Intake with Smoke Detection**: Exterior wall intake serving refuge areas on adjacent floors. Smoke detection in intake duct shuts down supply if smoke-contaminated outdoor air threatens system. Requires alternate air source or manual fire service operation.

3. **Ground Level Intake**: Acceptable for low-rise applications but problematic for tall buildings where ground-level intake may be distant from refuge areas requiring longest duct runs and highest fan pressure.

Intake design includes:
- Weather louvers with low pressure drop (<0.10 inches w.c.)
- Bird screen (1/2 inch mesh)
- Smoke detection in duct downstream of intake
- Isolation damper closing upon smoke detection
- Intake location documented on fire service access panel

## Interface with Building Smoke Control

Refuge area pressurization often forms one component of comprehensive building smoke control system. Integration requirements include:

- Coordination with stairwell pressurization preventing pressure reversal
- Elevator lobby smoke control interaction (shared or separate systems)
- Sequence ensuring refuge area achieves pressure before occupants enter
- Override provisions permitting fire department manual control
- Status reporting to fire alarm control panel and fire command center

Design approach must analyze all combinations of system activation to verify refuge areas maintain required pressure under worst-case scenarios including multiple door openings, adverse wind conditions, and partial system failure.

## Testing and Commissioning

Functional performance testing validates refuge area pressurization system compliance with design intent. Testing protocol per NFPA 92:

1. Measure pressure differential with all doors closed (shall meet or exceed 0.05 inches w.c.)
2. Open each door individually, measure pressure differential (shall meet or exceed 0.05 inches w.c.)
3. Verify control system response to simulated pressure variations
4. Confirm emergency power transfer and system operation on emergency power
5. Test smoke detection interlocks and verify proper response
6. Document supply airflow rates, fan speeds, and damper positions
7. Verify fire department control panel override functions

Annual testing requirements per local jurisdiction typically include pressure measurement, visual inspection, and emergency power transfer test. Documentation provides evidence of ongoing code compliance and system readiness.
