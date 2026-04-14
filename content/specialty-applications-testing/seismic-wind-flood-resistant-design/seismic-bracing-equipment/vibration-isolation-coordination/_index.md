---
title: "Vibration Isolation and Seismic Restraint Coordination"
aliases: ["Vibration Isolation and Seismic Restraint Coordination"]
description: "Technical guidance on coordinating vibration isolation systems with seismic restraints, including isolator selection, gap sizing, and restraint placement calculations."
date: 2025-01-05
weight: 4
keywords:
  - vibration isolation
  - seismic restraints
  - restrained spring isolators
  - snubber design
  - clearance gaps
  - isolation coordination
  - seismic bracing equipment
  - vibration control seismic
---

## Fundamental Conflict Between Isolation and Restraint

Vibration isolation systems permit equipment movement to reduce transmission of operational vibrations (typically 5-50 Hz) to the building structure. Seismic restraint systems prevent excessive equipment displacement during seismic events (typically 0.5-5 Hz). These opposing requirements create a design conflict that demands careful coordination.

The isolation system must allow controlled movement under normal operating conditions while the seismic restraint system must limit movement during earthquake loading. Improper coordination results in either compromised vibration isolation performance or inadequate seismic protection.

## Restrained vs Unrestrained Isolator Selection

**Restrained Spring Isolators**

Restrained isolators incorporate built-in limit stops that restrict vertical displacement to a predetermined value, typically 0.25 to 0.50 inches. The restraint housing engages when displacement exceeds normal operating deflection.

Selection criteria:
- Equipment with moderate vibration isolation requirements (85-95% efficiency)
- Installations where external seismic restraints are impractical
- Rooftop equipment with limited clearance
- Locations with moderate seismic design parameters (SDS < 1.0g)

The restrained isolator displacement limit must satisfy:

$$\delta_{limit} \geq \delta_{static} + \delta_{dynamic}$$

where $\delta_{static}$ is static deflection under dead load and $\delta_{dynamic}$ is maximum dynamic displacement during operation.

**Unrestrained Isolators with External Restraints**

Unrestrained isolators provide superior vibration isolation (95-99% efficiency) but require separate seismic restraint systems. This configuration allows independent optimization of both isolation and restraint performance.

Selection criteria:
- Critical vibration isolation applications (precision equipment, sensitive occupancies)
- Large equipment with significant seismic mass
- High seismic design parameters (SDS ≥ 1.0g)
- Multi-story buildings where relative displacement must be controlled

## Gap Sizing and Clearance Requirements

The clearance gap between equipment and seismic restraint is critical. Insufficient gap causes restraint engagement during normal operation, compromising isolation. Excessive gap permits uncontrolled displacement before restraint engagement.

**Minimum Gap Calculation**

The minimum required gap accommodates static deflection plus dynamic operating displacement:

$$G_{min} = \delta_{static} + A_{operating} + C_{tolerance}$$

where:
- $\delta_{static}$ = static deflection of isolation system (inches)
- $A_{operating}$ = maximum amplitude of operating vibration (inches)
- $C_{tolerance}$ = installation tolerance (typically 0.125 inches)

For typical installations with 1-inch static deflection:

$$G_{min} = 1.0 + 0.25 + 0.125 = 1.375 \text{ inches}$$

**Maximum Gap Calculation**

The maximum gap ensures restraint engagement before unacceptable equipment displacement:

$$G_{max} = \min\left(\frac{D_{seismic}}{2}, D_{clearance}\right)$$

where:
- $D_{seismic}$ = seismic design displacement from dynamic analysis
- $D_{clearance}$ = physical clearance to adjacent equipment or building elements

**Design Gap Recommendation**

The design gap typically falls between minimum and maximum values:

$$G_{design} = G_{min} + 0.5(G_{max} - G_{min})$$

This provides operating clearance while ensuring timely restraint engagement. ASHRAE Applications Handbook recommends gaps between 1.0 and 2.0 inches for most commercial HVAC equipment.

## Restraint Placement and Load Path

**Horizontal Restraint Configuration**

Horizontal restraints should engage isolators near equipment center of gravity to minimize eccentric loading. The restraint force is distributed among multiple attachment points:

$$F_{restraint} = \frac{F_p}{N \cdot \cos(\theta)}$$

where:
- $F_p$ = seismic design force per ASCE 7
- $N$ = number of restraint points
- $\theta$ = angle between restraint and horizontal plane

**Vertical Restraint Requirements**

Vertical seismic restraints prevent equipment uplift during combined vertical and horizontal seismic loading. The required vertical restraint capacity is:

$$T_{vertical} = 0.7 \cdot S_{DS} \cdot I_p \cdot W_p - W_p$$

where $S_{DS}$ is design spectral acceleration, $I_p$ is component importance factor, and $W_p$ is equipment operating weight.

## Snubber Design Considerations

Snubbers are passive restraint devices that permit slow thermal movement while restricting rapid seismic displacement. Snubber selection requires matching device characteristics to system requirements.

**Snubber Velocity Threshold**

The activation velocity must distinguish between thermal expansion and seismic motion:

$$v_{threshold} = \frac{\alpha \cdot L \cdot \Delta T}{t_{thermal}} < \frac{D_{seismic}}{t_{seismic}}$$

where $\alpha$ is thermal expansion coefficient, $L$ is piping length, and $t$ represents characteristic time for thermal vs seismic movement.

## Coordination with Building Structure

Seismic restraints transfer forces to the building structure. Structural attachment point capacity must exceed restraint loading:

$$\phi \cdot R_n \geq 1.3 \cdot F_{restraint}$$

where $\phi$ is strength reduction factor and $R_n$ is nominal attachment strength. The 1.3 factor accounts for variability in seismic response and component overstrength.

## Testing and Verification

Verify isolation/restraint coordination through:

1. **Static load testing** - Confirm isolation system deflection and gap dimensions
2. **Dynamic testing** - Verify isolator does not contact restraints during operation
3. **Restraint engagement testing** - Apply displacement to verify restraint activates within design gap
4. **Structural attachment testing** - Confirm attachment capacity through pull testing

## Design Integration Standards

ASHRAE Applications Handbook Chapter 48 provides guidance on vibration isolation selection. ASCE 7 Chapter 13 establishes seismic design forces. ICC-ES AC156 defines acceptance criteria for seismic qualification testing of nonstructural components. SMACNA Seismic Restraint Manual presents installation details for coordinated isolation and restraint systems.

Successful coordination requires simultaneous consideration of operational vibration control and seismic life safety requirements throughout the design process.
