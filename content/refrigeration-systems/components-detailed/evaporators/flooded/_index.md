---
title: "Flooded Evaporators"
aliases: ["Flooded Evaporators"]
description: "Comprehensive technical guide to flooded evaporator design, shell-and-tube construction, liquid level control methods, oil return strategies, and heat transfer enhancement for industrial refrigeration systems"
weight: 2
---

## Overview

Flooded evaporators operate with refrigerant liquid maintained at a specific level inside the evaporator shell or tubes. Unlike direct expansion (DX) systems where refrigerant fully evaporates within the heat exchanger, flooded evaporators maintain wetted heat transfer surfaces throughout operation. This design provides superior heat transfer coefficients and stable operation in large-capacity refrigeration systems.

The fundamental operating principle involves liquid refrigerant boiling on the heat transfer surface while vapor separates and exits to the compressor. Liquid level control mechanisms ensure adequate refrigerant inventory without flooding the suction line. Flooded evaporators are predominantly used in industrial refrigeration, process cooling, and large HVAC chiller applications where efficiency and reliability are critical.

## Shell-and-Tube Flooded Design

Shell-and-tube flooded evaporators represent the most common configuration in industrial refrigeration. The design consists of a cylindrical shell containing a tube bundle through which the process fluid flows. Refrigerant boils on the external tube surfaces, with liquid maintained in the lower portion and vapor occupying the upper region.

### Construction Features

**Shell Design:**
- ASME Section VIII pressure vessel construction
- Carbon steel or stainless steel materials
- Internal diameter: 12 to 96 inches typical
- Design pressure: 150 to 300 psig depending on refrigerant
- Hemispherical, ellipsoidal, or flanged-and-dished heads
- Minimum shell thickness per ASME calculations plus corrosion allowance

**Tube Bundle:**
- Copper, stainless steel, or copper-nickel alloys
- Standard diameters: 5/8", 3/4", 7/8", 1" OD
- Wall thickness: 0.035" to 0.065" (BWG 18 to 14)
- Tube lengths: 8 to 20 feet typical
- Fixed tubesheet, U-tube, or floating head configurations
- Triangular or square pitch arrangements

**Separation Space:**
The vapor space above the liquid level provides critical separation:
- Minimum height: 12 to 18 inches above liquid level
- Prevents liquid carryover to suction line
- Accommodates refrigerant circulation rate variations
- Contains mist eliminators or demisters in high-velocity applications

### Flow Arrangements

**Single-Pass Configuration:**
- Process fluid makes one traverse through evaporator
- Simplest design with lowest pressure drop
- Used for large temperature differences (>15°F)
- Velocity: 3 to 8 ft/s typical

**Multi-Pass Configuration:**
- Fluid redirected through multiple passes via baffles
- Increases velocity and heat transfer coefficient
- Applied when single-pass velocity insufficient
- Common: 2-pass, 4-pass, 6-pass designs
- Velocity: 5 to 12 ft/s typical

**Refrigerant-Side Enhancement:**
- Enhanced tube surfaces (low-fin, turbo-B, corrugated)
- Nucleate boiling enhancement
- Heat transfer improvement: 1.5 to 3.0x smooth tube
- Pressure drop penalty minimal in pool boiling

## Liquid Level Control Methods

Precise liquid level control is essential for flooded evaporator performance. Three primary control methods are employed:

### Float Control

**Mechanical Float Systems:**
- Float chamber connected to evaporator shell
- Float actuates refrigerant feed valve
- Direct mechanical linkage or pilot-operated valve
- Response time: 1 to 5 seconds
- Accuracy: ±1 to 2 inches liquid level
- Maximum capacity: Limited by valve size
- Applications: Small to medium evaporators (<100 tons)

**Electronic Float Controls:**
- Capacitance or conductivity level sensors
- Electronic signal to modulating valve
- Continuous level measurement
- Response time: <1 second
- Accuracy: ±0.5 inches
- Suitable for all capacities
- Allows remote monitoring and trending

### High-Side/Low-Side Float Control

**High-Side Float:**
- Float chamber on high-pressure (condenser) side
- Float opens valve when liquid accumulates
- Maintains constant liquid level in evaporator
- Self-equalizing system pressure
- Used in specific industrial applications
- Requires careful refrigerant charge management

**Low-Side Float:**
- Float in evaporator shell or separate chamber
- Opens feed valve when level drops
- Common in flooded shell-and-tube chillers
- Prevents suction line flooding
- Responsive to load variations

### Thermostatic Expansion Valve (TEV) with Liquid Level

Some flooded systems use modified TEV control:
- Oversized TEV maintains liquid seal
- Bulb location critical (vapor space)
- Superheat setting: 2 to 5°F
- Combined with high liquid level alarm
- Less common than float control
- Applied in retrofit situations

## Liquid Recirculation Systems

Recirculation systems circulate refrigerant at rates exceeding evaporation rate, ensuring complete tube wetting and enhanced heat transfer.

### Overfeed Ratio

The overfeed ratio (OR) defines the relationship between circulated liquid and evaporated vapor:

**OR = Mass Flow Circulated / Mass Flow Evaporated**

Typical overfeed ratios:
- Low overfeed: 1.5:1 to 2:1
- Medium overfeed: 2:1 to 4:1
- High overfeed: 4:1 to 6:1
- Ultra-high: 6:1 to 10:1

Higher overfeed ratios provide:
- Improved heat transfer (up to 20% increase)
- Better oil return to separator
- More uniform tube wetting
- Reduced fouling tendency
- Increased pumping energy requirement

### Pump Recirculation

**Mechanical Liquid Pumps:**
- Centrifugal or positive displacement
- Located in liquid return from evaporator
- Pump refrigerant from separator to evaporator
- Design pressure differential: 5 to 30 psi
- NPSH requirements critical
- Materials: Cast iron, stainless steel, or specialty alloys
- Hermetic or semi-hermetic construction for volatile refrigerants

**System Components:**
- Low-pressure receiver/separator
- Refrigerant liquid pump
- Distribution headers
- Return piping to separator
- Liquid level controls
- Pump discharge pressure control

**Operating Characteristics:**

| Parameter | Typical Range | Notes |
|-----------|---------------|-------|
| Pump flow rate | 1.5 to 6× evaporator capacity | Based on overfeed ratio |
| Discharge pressure | 5 to 30 psig above suction | Overcome piping/distributor losses |
| NPSH available | 3 to 10 ft minimum | Prevent cavitation |
| Motor efficiency | 70 to 85% | Hermetic pump-motor assembly |
| Temperature rise | 2 to 5°F | Heat of compression in liquid |

### Gravity Recirculation

Gravity systems rely on density differences to circulate refrigerant:

**Vertical Configuration:**
- Evaporator elevated above separator
- Two-phase mixture returns via gravity
- Liquid-vapor separation in low-pressure receiver
- Liquid returns to evaporator via liquid leg
- No mechanical pump required
- Elevation difference: 10 to 40 feet typical

**Operating Principles:**
- Hydrostatic head provides circulation driving force
- Driving force (psi) = 0.433 × height (ft) × specific gravity difference
- Vapor quality in return line: 10 to 30%
- Return line sizing critical (two-phase flow)
- Liquid leg must remain sealed

### Thermosyphon Systems

Thermosyphon evaporators use heat input to drive circulation:

**Configuration:**
- Evaporator tubes oriented vertically or inclined
- Liquid refrigerant in lower region
- Heat input creates vapor bubbles
- Bubble-induced circulation drives flow
- Natural convection enhancement
- No external pump required

**Design Considerations:**
- Tube inclination: 5 to 15 degrees from vertical
- Heat flux: 2,000 to 8,000 Btu/hr-ft²
- Circulation rate: Function of heat input
- Limited to specific geometries
- Excellent for direct immersion applications

## Oil Return Considerations

Oil management is critical in flooded evaporator systems due to oil-refrigerant miscibility characteristics and the large refrigerant inventory.

### Oil Accumulation Issues

**Oil in Evaporator:**
- Reduces heat transfer coefficient (5 to 25% degradation)
- Forms insulating film on heat transfer surfaces
- Concentration increases in low-temperature zones
- Viscosity increases at low temperatures
- Eventually fouls tubes requiring cleaning

**Oil Concentration Effects:**

| Oil Concentration | Heat Transfer Impact | Mitigation Strategy |
|-------------------|----------------------|---------------------|
| 0-1% | Negligible (<3% reduction) | Normal operation |
| 1-3% | Moderate (3-10% reduction) | Increase oil return frequency |
| 3-5% | Significant (10-20% reduction) | Implement continuous removal |
| >5% | Severe (>20% reduction) | Requires system shutdown/cleaning |

### Oil Return Mechanisms

**Refrigerant Velocity Method:**
- Maintain sufficient vapor velocity to entrain oil
- Minimum velocity: 500 to 1000 fpm in horizontal suction
- Vertical suction: 1000 to 1500 fpm minimum
- Effective for miscible oil-refrigerant pairs
- Less effective with immiscible combinations

**Continuous Oil Return:**
- Dedicated oil drain from evaporator low point
- Solenoid valve controlled by timer or level sensor
- Returns oil to compressor crankcase or separator
- Cycle frequency: Every 15 to 60 minutes
- Duration: 30 to 120 seconds per cycle

**Oil Separator Integration:**
- High-efficiency oil separator on compressor discharge
- Removes >95% of oil before condenser
- Reduces oil circulation rate through system
- Direct oil return to compressor
- Essential for ammonia and CO₂ systems

**Oil Still/Distillation:**
- Heats oil-refrigerant mixture
- Evaporates refrigerant, concentrates oil
- Returns clean refrigerant to system
- Drains concentrated oil to waste or compressor
- Used in large industrial systems (>500 tons)

## Heat Transfer Enhancement

Maximizing heat transfer performance in flooded evaporators involves both passive and active enhancement techniques.

### Enhanced Tube Surfaces

**Low-Fin Tubes:**
- Integral fins on external surface
- Fin density: 19, 26, or 40 fpi (fins per inch)
- Fin height: 0.031" to 0.062"
- Heat transfer enhancement: 1.5 to 2.0× smooth tube
- Nucleate boiling improved by increased surface area
- Standard in modern chiller design

**High-Flux Surfaces:**
- Porous or structured surface coating
- Subsurface tunnels promote nucleation
- Heat transfer enhancement: 2.5 to 3.5× smooth tube
- Examples: Turbo-B, Gewa, Thermoexcel
- Higher cost justified in premium applications
- Reduced fouling tendency in some designs

**Internally Enhanced Tubes:**
- Rifled, corrugated, or micro-fin internal surface
- Increases fluid-side heat transfer coefficient
- Enhancement: 1.3 to 1.8× smooth tube
- Combined with external enhancement
- Total enhancement: 2.0 to 4.0× plain tube performance

### Surface Maintenance

**Fouling Mitigation:**
- Water treatment critical (calcium/magnesium control)
- Fouling factor design allowance: 0.0001 to 0.0005 hr-ft²-°F/Btu
- Regular cleaning schedules (chemical or mechanical)
- Monitoring via log mean temperature difference trending
- Performance degradation indicator: 10-15% capacity loss

**Cleaning Methods:**
- Chemical cleaning: Acid wash, scale inhibitors
- Mechanical brushing: Manual or automated systems
- Online cleaning systems: Continuous ball recirculation
- Frequency: Quarterly to annually depending on water quality

## Surge Drum and Liquid Management

The surge drum (low-pressure receiver) serves multiple functions in recirculated flooded systems:

**Primary Functions:**
- Liquid-vapor separation
- Liquid refrigerant storage
- Surge capacity for load variations
- Oil collection point
- Pump suction source

**Design Parameters:**

| Parameter | Specification | Basis |
|-----------|---------------|-------|
| Volume | 2 to 5× evaporator liquid volume | Load change accommodation |
| Vapor velocity | <2 ft/s at maximum load | Prevent mist carryover |
| Liquid residence time | 1 to 3 minutes minimum | Separation efficiency |
| NPSH margin | 5 to 10 ft above required | Pump performance |
| Operating level | 40 to 60% of height | Normal operating range |

**Internal Components:**
- Mist eliminator pads (vapor outlet)
- Baffle plates (inlet distribution)
- Oil drain connection (lowest point)
- Level sight glass or sensors
- Pressure relief valve
- Liquid pump suction connection

## Liquid Refrigerant Pumps

Refrigerant liquid pumps in recirculation systems require specialized design:

### Pump Selection Criteria

**Centrifugal Pumps:**
- Flow rate: 100 to 5,000 gpm typical
- Head: 20 to 100 feet
- Efficiency: 60 to 80%
- Hermetic or sealed construction
- Single or multi-stage
- NPSH critical consideration

**Positive Displacement Pumps:**
- Flow rate: 10 to 500 gpm
- Discharge pressure: 30 to 150 psi
- Efficiency: 70 to 85%
- Screw, gear, or vane type
- Hermetic construction
- Less NPSH sensitive
- Higher discharge pressure capability

### NPSH Requirements

Net Positive Suction Head Available (NPSHa) must exceed NPSHr:

**NPSHa = P_static + P_atmospheric - P_vapor - P_friction**

Where:
- P_static = Static head from liquid level to pump centerline
- P_atmospheric = Separator pressure (gauge + atmospheric)
- P_vapor = Refrigerant vapor pressure at pump inlet temperature
- P_friction = Friction losses in suction piping

**Design Guidelines:**
- NPSHa > NPSHr + 3 to 5 ft safety margin
- Minimize suction line length and fittings
- Subcool liquid when possible (1 to 3°F)
- Locate pump below separator liquid level
- Increase separator pressure if necessary

## System Performance Specifications

### Typical Flooded Evaporator Performance

| Refrigerant | Evaporator Temp (°F) | Overall U-Factor (Btu/hr-ft²-°F) | LMTD (°F) | Notes |
|-------------|----------------------|-----------------------------------|-----------|-------|
| R-134a | 40 | 180-220 | 8-12 | Water chiller, enhanced tubes |
| R-404A | 20 | 150-190 | 10-15 | Low-temp process cooling |
| Ammonia | 25 | 200-250 | 8-12 | Industrial refrigeration |
| Ammonia | -20 | 150-200 | 12-18 | Freeze protection |
| CO₂ | -10 | 180-230 | 10-14 | Cascade system evaporator |

### Capacity Calculation

Evaporator capacity is determined by:

**Q = U × A × LMTD**

Where:
- Q = Cooling capacity (Btu/hr)
- U = Overall heat transfer coefficient (Btu/hr-ft²-°F)
- A = Heat transfer surface area (ft²)
- LMTD = Log mean temperature difference (°F)

**LMTD Calculation:**

LMTD = (ΔT₁ - ΔT₂) / ln(ΔT₁/ΔT₂)

For counterflow arrangement with constant evaporator temperature:
- ΔT₁ = Entering fluid temp - Evaporator temp
- ΔT₂ = Leaving fluid temp - Evaporator temp

## Applications and Selection Criteria

Flooded evaporators are preferred when:

- Large refrigeration capacity required (>50 tons)
- High efficiency demanded (low approach temperatures)
- Stable evaporator temperature critical
- Multiple evaporators fed from common system
- Oil return challenging (ammonia, CO₂ systems)
- Process requires precise temperature control
- Long-term reliability essential

Limitations include:
- Higher refrigerant charge compared to DX systems
- Increased system complexity
- Liquid pump energy requirement
- More sophisticated controls
- Higher initial cost
- Larger equipment footprint

## Safety and Code Compliance

Flooded evaporator systems must comply with:

**ASME Section VIII:**
- Pressure vessel design and fabrication
- Material specifications
- Welding procedures and inspection
- Hydrostatic testing requirements

**ASHRAE 15:**
- Refrigerant safety classification
- Maximum allowable charge limits
- Machinery room requirements
- Ventilation and detection systems

**IIAR Standards (Ammonia):**
- IIAR 2: Equipment, design, and installation
- IIAR 3: Ammonia refrigeration valves
- IIAR 5: Start-up and commissioning
- IIAR 6: Inspection, testing, and maintenance

**Pressure Relief:**
- Relief valve sizing per ASME/IIAR standards
- Discharge to safe location
- Capacity based on fire exposure scenario
- Annual inspection and testing required

## Conclusion

Flooded evaporators provide superior performance in large-scale refrigeration applications through maximized heat transfer surface utilization and stable operating characteristics. Proper design requires careful attention to liquid level control, oil management, refrigerant circulation, and heat transfer enhancement. When correctly applied and maintained, flooded evaporators deliver exceptional efficiency and reliability for decades of service in industrial refrigeration and large HVAC systems.
