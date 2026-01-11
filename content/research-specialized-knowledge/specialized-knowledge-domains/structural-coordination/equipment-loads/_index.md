---
title: "Equipment Loads"
description: "Static and dynamic load calculations, seismic restraint requirements, wind and snow load effects on rooftop equipment for structural coordination"
weight: 1
---

## Overview

Equipment loads transmitted to building structures include static weight forces, dynamic operating forces, seismic inertial forces, wind pressures, and snow accumulation. Structural engineers require accurate load information for member sizing, foundation design, and connection detailing. HVAC engineers provide equipment weights, dimensions, and support point locations enabling proper structural integration.

##Static Load Calculations

Static loads represent equipment weight plus operating fluids, refrigerant charge, and piping connections acting continuously on supporting structure. Equipment manufacturers provide shipping weights and operating weights in product data. Operating weight exceeds shipping weight due to refrigerant charge, oil, and water content in heat exchangers and coils.

For equipment not yet selected, use estimated weights based on similar equipment:

| Equipment Type | Weight Estimate |
|----------------|-----------------|
| Rooftop units | 10-15 lb/ton cooling |
| Air handling units | 0.5-1.5 lb/cfm |
| Chillers (air-cooled) | 40-60 lb/ton |
| Chillers (water-cooled) | 20-30 lb/ton |
| Cooling towers | 15-25 lb/ton |
| Boilers (fire tube) | 50-100 lb/hp |

Add weight of isolated piping, ductwork, and platforms supported by equipment frame. Distribution of loads to support points depends on equipment configuration and center of gravity location. Manufacturers provide support point locations and maximum/minimum loads per point.

## Dynamic Load Considerations

Dynamic loads result from equipment operation including unbalanced rotating forces, reciprocating compressor impulses, and impact forces from sudden starts/stops. Dynamic forces are periodic at equipment operating frequency and harmonics, exciting structural vibration.

Rotating equipment generates centrifugal force from residual imbalance:
F = m × e × ω²

Where:
- m = rotor mass
- e = eccentricity (imbalance)
- ω = angular velocity (rad/s)

Balanced equipment exhibits imbalance 0.1-0.5 oz-in per pound of rotor weight. Cooling tower fans with 10-foot diameter generate forces of 100-500 pounds at operating speed. Centrifugal chillers with precisely balanced rotors produce minimal dynamic forces.

Reciprocating compressors create first-order and second-order forces and moments requiring inertia bases and spring isolation. First-order forces occur at compressor speed; second-order forces at twice compressor speed. Inertia base mass should exceed compressor mass by factor of 1.5 to 3.0 depending on compressor type and operating conditions.

Variable frequency drives alter operating speed and dynamic force magnitude. Forces increase proportional to speed squared (F ∝ ω²). VFD operation at 60 Hz produces four times dynamic force compared to 30 Hz operation. Consider full-speed operation for structural design despite part-load operation dominating annual hours.

## Seismic Restraint Requirements

Seismic restraints prevent equipment overturning, sliding, and structural damage during earthquakes. International Building Code (IBC) and ASCE 7 establish seismic design requirements based on building seismic design category, equipment location, and component importance factor.

Seismic force on equipment:
F_p = 0.4 × a_p × S_DS × W_p × (1 + 2z/h) / (R_p/I_p)

Where:
- a_p = component amplification factor (1.0-2.5)
- S_DS = design spectral acceleration
- W_p = component weight
- z = height above base
- h = building height
- R_p = component response modification factor (1.5-2.5)
- I_p = component importance factor (1.0-1.5)

Rooftop equipment experiences higher seismic forces due to elevation term (1 + 2z/h). Top floor rooftop equipment sees forces 3 times greater than ground-level equipment of equal weight. Life safety and fire suppression systems require I_p = 1.5, increasing design forces 50%.

Seismic restraints include:

- Spring isolators with lateral snubbers limiting displacement to 0.25-0.5 inches
- Equipment anchorage bolts sized for combined tension from overturning and shear from lateral forces
- Flexible piping connections permitting seismic motion without piping damage
- Anchored housekeeping pads providing equipment mounting surface

OSHPD seismic requirements for California hospitals impose additional testing and certification requirements demonstrating seismic performance through shake table testing.

## Wind Load Calculations for Rooftop Equipment

Rooftop equipment experiences wind pressure on projected area normal to wind direction. Wind pressure increases with height and exposure category. ASCE 7 establishes design wind pressures based on:

- Basic wind speed (mph) from wind speed maps
- Exposure category (B, C, or D) based on surrounding terrain
- Equipment height above ground
- Component and cladding pressure coefficients

Design wind pressure:
p = q_z × G × C_p

Where:
- q_z = velocity pressure at height z
- G = gust effect factor (0.85 typical)
- C_p = pressure coefficient (0.8-1.5 depending on shape)

For rooftop unit 10 feet tall on 40-foot building in 115 mph wind zone, design pressure approximates 30-40 psf. Total force equals pressure times projected area. Large chillers and cooling towers require substantial anchorage resisting overturning moments.

Equipment screens and penthouses reduce wind loads on equipment but create additional loads on screen/penthouse structure. Account for wind loads on screens in structural design. Porous screens reduce wind pressure compared to solid walls; use appropriate pressure coefficients.

Flexible piping and duct connections accommodate wind-induced movement without imposing loads on connected systems. Rigid connections can damage piping or equipment during high wind events. Spring vibration isolators permit limited lateral movement acceptable for wind loads.

## Snow Load Effects on Equipment

Snow accumulation on rooftop equipment reduces heat rejection capacity and imposes additional structural loads. Flat roofs accumulate snow depth equal to ground snow load divided by snow density. Sloped roofs and equipment surfaces shed snow partially depending on roof slope and surface characteristics.

Ground snow load (psf) varies geographically from 0 psf in southern locations to 100+ psf in mountainous regions. Flat roof snow load:
p_f = 0.7 × C_e × C_t × I_s × p_g

Where:
- C_e = exposure factor (0.7-1.2)
- C_t = thermal factor (1.0-1.2)
- I_s = importance factor (0.8-1.2)
- p_g = ground snow load

Drifting snow accumulates on low portions of roofs adjacent to higher sections or rooftop equipment. Drift height:
h_d = 0.43 × (L_u)^(1/3) × (p_g + 10)^(1/4) - 1.5

Where L_u is upwind fetch distance. Drifts create non-uniform loads requiring structural analysis considering both balanced and unbalanced snow conditions.

Equipment curbs and platforms elevate equipment above anticipated snow accumulation. Minimum curb height equals 1.5 times design snow depth. Provide drainage preventing water ponding from snow melt. Sloped surfaces shed snow more readily than flat surfaces.

Air intake louvers require protection from snow blockage. Elevated louvers above snow line, sloped or vertical louvers shedding snow, and interior louver locations prevent snow infiltration. Snow infiltration causes coil freezing, reduced airflow, and equipment damage.

## Concentrated Load Distribution

Point loads from equipment supports must distribute to structural framing through adequate curbs, platforms, or housekeeping pads. Concentrated loads exceeding structural element capacity require reinforcement or load distribution over larger area.

Steel frame structures permit concentrated loads at beam intersections where columns provide support. Loads between beam supports require verification that beam can support additional concentrated load plus distributed loads. Composite metal deck may require supplementary framing distributing equipment point loads to multiple beams.

Concrete structures distribute loads through slab action. Post-tensioned slabs handle concentrated loads better than conventionally reinforced slabs. Elevated equipment platforms using structural steel or reinforced concrete transfer loads to columns, avoiding loading on slab beyond design capacity.

Rooftop curbs for package units typically use 14-18 gauge galvanized steel with internal bracing at 24-inch centers. Curb must support equipment weight plus wind loads without excessive deflection. Curb anchorage to structure uses expansion anchors or embedded sleeves with sufficient edge distance and spacing preventing concrete breakout.

## Load Path and Connection Design

Complete load path from equipment support points through structure to foundation ensures proper force transfer. Missing elements in load path create weak links allowing excessive deflection or failure. Load path includes:

1. Equipment support points and internal framing
2. Vibration isolation mounts (if used)
3. Equipment curb or platform
4. Curb-to-structure anchors
5. Roof structure (joists, beams, deck)
6. Columns and walls
7. Foundations and soil

Each element must carry loads from above without exceeding capacity. Coordination between disciplines ensures consistent assumptions about load magnitude, distribution, and path. Document equipment loads, support requirements, and special conditions on drawings facilitating contractor understanding and proper installation.
