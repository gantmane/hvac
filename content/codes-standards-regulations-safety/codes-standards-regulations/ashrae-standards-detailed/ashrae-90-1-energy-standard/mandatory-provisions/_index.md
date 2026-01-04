---
title: "Mandatory Provisions of ASHRAE 90.1"
description: "Non-tradeable minimum requirements applicable to all compliance paths including equipment efficiency floors, mandatory controls, envelope performance minimums, and system design features."
date: 2026-01-04
weight: 1
---

Mandatory provisions in ASHRAE 90.1 represent non-negotiable minimum requirements that apply regardless of which compliance path a project follows. These provisions establish performance floors preventing unreasonable tradeoffs that might satisfy whole-building energy targets while incorporating inefficient individual components or poor design practices. Every building complying with ASHRAE 90.1 must satisfy all applicable mandatory provisions in addition to meeting prescriptive requirements, performance rating method criteria, or energy cost budget method targets. Understanding mandatory provisions is crucial because they constrain design options even when using flexible performance-based compliance approaches.

## Purpose and Philosophy of Mandatory Provisions

The fundamental purpose of mandatory provisions is preventing poor design decisions that might technically comply with performance targets while creating long-term operational problems. Performance-based compliance paths allow trading efficiency improvements across systems—for example, exceptional envelope performance might mathematically offset inefficient mechanical equipment. Without mandatory minimums, such tradeoffs could result in buildings with excellent simulation results but problematic actual performance.

Mandatory provisions also address market transformation goals by ensuring minimum technology adoption. As equipment efficiency improves and costs decrease, mandatory minimums are periodically raised to reflect current market offerings. This prevents installation of obsolete, inefficient equipment even in projects where other systems compensate in performance calculations.

The mandatory requirements cover four primary categories: equipment and system minimum efficiency, controls and scheduling, envelope components and assemblies, and verification and documentation. Each category establishes baseline performance that all buildings must achieve before considering compliance path-specific requirements.

## Equipment Efficiency Mandatory Minimums

Section 6.4 establishes mandatory minimum efficiency requirements for HVAC equipment and components. These minimums apply to all equipment regardless of whether the project uses prescriptive compliance or performance-based compliance. The prescriptive path equipment efficiency tables (Section 6.8) typically list higher minimums than the mandatory minimums, but performance-based methods must still respect mandatory floors even when making system tradeoffs.

For unitary air conditioners and condensing units, mandatory minimums specify EER (Energy Efficiency Ratio) and SEER (Seasonal Energy Efficiency Ratio) or IEER (Integrated Energy Efficiency Ratio) values depending on equipment type and capacity. Air-cooled equipment serving <65,000 Btu/h must meet minimum SEER values. Equipment serving ≥65,000 Btu/h and <135,000 Btu/h must meet minimum EER and IEER. Equipment ≥135,000 Btu/h and <240,000 Btu/h requires minimum EER and IEER values. Larger equipment categories have progressively higher minimums.

Packaged terminal air conditioners (PTACs) and packaged terminal heat pumps (PTHPs) follow the relationship:

$$EER = 14.0 - (0.300 \times Cap_{Btu/h}/1000)$$

Where $Cap_{Btu/h}$ represents cooling capacity in Btu/h. This sliding scale recognizes that smaller capacity equipment typically achieves higher efficiency ratios than larger capacity equipment in this category.

Water-chilling packages (chillers) must meet minimum efficiency expressed as kW/ton at specified rating conditions. Air-cooled chillers have different minimums than water-cooled chillers. Centrifugal chillers maintain separate minimums from positive displacement types. Path A efficiency represents full-load performance while Path B represents IPLV (Integrated Part Load Value) accounting for part-load operation. Equipment must meet both Path A and Path B minimums.

Boilers require minimum combustion efficiency or thermal efficiency depending on fuel type and capacity. Gas-fired boilers <300,000 Btu/h input must achieve minimum AFUE (Annual Fuel Utilization Efficiency). Larger gas boilers require minimum combustion efficiency at specified conditions. Oil-fired boilers follow similar structure with capacities and minimums adjusted for fuel characteristics.

Heat rejection equipment including cooling towers and evaporative condensers must achieve minimum performance measured in gpm/hp for cooling towers or Btu/h per hp for evaporative condensers. Open-circuit cooling towers have different minimums than closed-circuit fluid coolers.

## Mandatory HVAC Controls Requirements

Section 6.4 establishes extensive mandatory controls requirements ensuring proper system operation, appropriate setback during unoccupied periods, and prevention of simultaneous heating and cooling. These controls requirements often receive less attention than equipment efficiency but significantly impact actual building energy consumption.

**Thermostatic controls:** Each zone must have individual thermostatic control capable of responding to temperature changes within that zone. Exception: spaces with similar occupancy patterns and thermal characteristics can share a thermostat if located within the same zone and not separated by partitions. This requirement prevents a single thermostat in a large open area from inadequately controlling comfort in distinct zones.

**Setpoint overlap restriction:** The cooling setpoint cannot be more than 5°F below the heating setpoint for the same zone and same operational mode (occupied or unoccupied). This deadband requirement prevents simultaneous heating and cooling:

$$T_{cool,setpoint} \geq T_{heat,setpoint} + 5°F$$

Some systems can achieve even tighter deadbands (as little as 1-2°F) but 5°F represents the mandatory minimum separation preventing gross energy waste from fighting systems.

**Off-hour controls:** HVAC systems must have the capability to automatically reduce energy use during unoccupied periods through one of several methods: automatic shutdown, setback to unoccupied temperature setpoints, cycling to maintain unoccupied setpoints, or reduction of outdoor air ventilation to minimum required for health and safety.

**Shutoff damper controls:** Air economizers must include both motorized dampers and automatic controls configured to provide outdoor air cooling when appropriate. The control system must close outdoor air dampers when economizer operation would increase energy consumption—typically when outdoor conditions are unsuitable for cooling and minimum ventilation requirements are satisfied.

**Zone isolation:** Systems serving multiple zones must have controls and devices capable of shutting off heating and cooling to individual zones in response to zone thermostatic control. This prevents conditioned air delivery to unoccupied zones. VAV systems inherently provide this through terminal unit dampers. Constant volume systems require zone-level dampers or valves.

**Ventilation fan controls:** Systems supplying outdoor air through fans >25 hp must have automatic controls configured to shut off fans when spaces served are unoccupied except when ventilation must continue for health, safety, or process requirements. Return and exhaust fans must also shut off unless continued operation is required.

**Hydronic system controls:** Hydronic systems distributing heating or cooling through water must include automatic controls maintaining supply water temperature through modulation or staging of heat input/rejection. Individual zone control must be provided through two-way valves, on-off control of individual pumps, or thermostatic radiator valves. Continuous circulation with three-way bypass mixing is prohibited except in specific applications where it is essential for system operation.

## Building Envelope Mandatory Requirements

Section 5.4 establishes mandatory envelope provisions preventing grossly deficient envelope assemblies even when using performance-based compliance. These requirements address insulation, fenestration, air leakage, and moisture control.

**Minimum insulation R-values:** All opaque envelope assemblies separating conditioned space from unconditioned space or outdoors must contain insulation meeting minimum R-value requirements. While these minimums are climate-zone specific and lower than prescriptive values, they prevent completely uninsulated assemblies. For example, even in the mildest climates, walls require minimum R-3 insulation, roofs require minimum R-5, and floors over outdoor air require minimum R-10.

**Fenestration U-factor limits:** Vertical fenestration (windows) and skylights must meet maximum U-factor requirements preventing single-pane uninsulated glazing. Mandatory U-factor limits range from 1.20 Btu/h·ft²·°F in mild climates to 0.40 Btu/h·ft²·°F in severe climates. These values are significantly less stringent than prescriptive requirements but ensure minimum performance floors.

**Continuous insulation:** Metal building walls and roofs must include continuous insulation in addition to cavity insulation to address thermal bridging through structural members. The continuous insulation R-value depends on climate zone and assembly type but typically represents 40-60% of total required R-value for the assembly.

**Air leakage requirements:** Building envelope assemblies must comply with air leakage provisions including sealed envelope, continuous air barrier, air barrier testing, and loading dock door seals. The air barrier system must be continuous across all envelope assemblies, sealed at transitions and penetrations, and capable of withstanding specified pressure differences.

Envelope assemblies must be tested to verify air leakage rates not exceeding maximum values:

- Fenestration: 0.4 cfm/ft² at 1.57 psf (75 Pa)
- Curtain walls: 0.06 cfm/ft² at 1.57 psf (75 Pa)
- Doors: 1.0 cfm/ft² at 1.57 psf (75 Pa)

Whole-building air leakage must not exceed 0.40 cfm/ft² of above-grade envelope area at 0.3 inches water column (75 Pa) when verified through testing.

## Lighting and Power Mandatory Requirements

Section 9.4 establishes mandatory lighting controls requirements ensuring appropriate shutoff, dimming, and scheduling. Unlike the equipment efficiency sections where mandatory minimums are typically less stringent than prescriptive requirements, lighting controls mandatory requirements often represent the most stringent provisions in the standard.

**Automatic lighting shutoff:** Interior lighting in buildings larger than 5,000 ft² must include automatic controls capable of shutting off lighting in all spaces. Acceptable shutoff methods include:

- Scheduled shutoff using time-of-day scheduling with manual override limited to 2 hours
- Occupancy sensors shutting off lights within 20 minutes of space vacancy
- Signal from another control or alarm system indicating unoccupied status

**Space control:** Each space enclosed by ceiling-height partitions must have at least one independent lighting control device. This requirement prevents large areas controlled by a single switch, enabling occupants to shut off lighting in unoccupied portions without affecting occupied areas.

**Exterior lighting control:** Lighting for building exteriors, parking areas, and site illumination must include automatic controls turning off lighting when sufficient daylight is available or during periods when lighting is not needed. Astronomical time switches or photocell controls satisfy this requirement.

**Tandem wiring:** Linear fluorescent lamps ≥30 watts and ≤100 watts must be installed with tandem wiring where feasible, allowing one ballast to drive two lamps and reducing ballast losses. LED lighting has largely superseded fluorescent technology, making this provision less relevant in current construction.

## Service Water Heating Mandatory Provisions

Section 7.4 establishes mandatory requirements for service water heating systems addressing equipment efficiency, pipe insulation, and controls.

**Temperature controls:** Service water heating equipment must include controls maintaining desired outlet temperature through modulation or staged operation. This prevents continuous full-fire operation when lower heat input would maintain setpoint.

**Pipe insulation:** Piping serving service water heating systems must include insulation meeting minimum requirements based on pipe size and fluid temperature. For recirculating systems and piping between water heater and first draw location >50 feet, insulation R-value must be:

$$R = 3.0 \text{ h·ft²·°F/Btu for pipes} < 1.5 \text{ in. diameter}$$
$$R = 4.0 \text{ h·ft²·°F/Btu for pipes} \geq 1.5 \text{ in. diameter}$$

**Pool heating:** Pools must include pool covers reducing evaporative heat loss when pools are not in use. Pool heating systems must include controls allowing shutoff and temperature adjustment. Heat recovery from building systems can substitute for conventional pool heating where feasible.

## Verification and Documentation Requirements

Mandatory provisions include requirements for verification testing and documentation ensuring proper installation and operation of systems and components.

**Equipment efficiency verification:** Equipment nameplates must document rated efficiency for comparison against minimum requirements. For custom-built or field-assembled equipment, certification must be provided documenting compliance with efficiency minimums.

**Controls verification:** Control sequences must be documented, programmed as documented, and demonstrated to function as intended during commissioning. This requirement ensures mandatory controls provisions are implemented in actual operation, not just on paper.

**Envelope assembly verification:** For air barrier compliance, testing must verify that envelope assemblies meet maximum air leakage rates. Continuous insulation installation must be verified through inspection confirming continuous coverage without thermal bypasses.

**Training and documentation:** Operating and maintenance manuals must be provided covering all equipment and systems. Building operators must receive training on system operation, control sequences, and efficiency optimization strategies.

Understanding and applying mandatory provisions correctly ensures code-compliant designs while preventing common pitfalls. Even when using performance-based compliance methods offering system tradeoff flexibility, mandatory provisions establish non-negotiable minimums protecting building performance and occupant comfort. Designers must verify mandatory provision compliance before proceeding with compliance path-specific requirements, ensuring all projects achieve baseline performance standards regardless of optimization strategies employed.
