---
title: "Exhaust Requirements for Plywood & Particleboard Plants"
aliases: ["Exhaust Requirements for Plywood & Particleboard Plants"]
description: "Technical guidance on local exhaust ventilation, general ventilation, and capture hood design for plywood and particleboard manufacturing facilities."
date: 2025-01-05
keywords:
  - local exhaust ventilation
  - formaldehyde control
  - VOC capture systems
  - particleboard exhaust
  - plywood plant ventilation
  - industrial hood design
  - ACGIH ventilation
  - wood composite manufacturing
weight: 4
draft: false
---

## Overview

Plywood and particleboard manufacturing facilities require sophisticated exhaust systems to control wood dust, formaldehyde emissions, volatile organic compounds (VOCs), and thermal loads from press operations. Proper ventilation design protects worker health, ensures regulatory compliance, and maintains product quality throughout the manufacturing process.

## Exhaust Volume Calculation Methods

### Local Exhaust Ventilation (LEV)

For point-source capture at sanding, trimming, and cutting operations, calculate exhaust volume using the hood face velocity method:

$$Q = V_f \cdot A_f$$

Where:
- $Q$ = Required exhaust volume (cfm)
- $V_f$ = Hood face velocity (fpm)
- $A_f$ = Hood face area (ft²)

The ACGIH Industrial Ventilation Manual recommends face velocities of 100-200 fpm for fully enclosed hoods and 200-500 fpm for canopy or side-draft hoods capturing wood dust.

### Capture Hood Design

For non-enclosed sources, calculate the volumetric flow rate based on capture velocity at the contaminant source:

$$Q = V_c \cdot (10X^2 + A)$$

Where:
- $Q$ = Required airflow (cfm)
- $V_c$ = Capture velocity (fpm), typically 100-150 fpm for wood dust
- $X$ = Distance from hood face to contaminant source (ft)
- $A$ = Hood face area (ft²)

This relationship accounts for the expansion of the capture envelope with distance from the hood opening.

### General Ventilation Requirements

For process areas with diffuse emissions from hot presses, dryers, and resin application zones, calculate dilution ventilation:

$$Q_{dil} = \frac{G \cdot K \cdot 10^6}{C_{permissible} - C_{makeup}}$$

Where:
- $Q_{dil}$ = Dilution airflow (cfm)
- $G$ = Contaminant generation rate (lb/min)
- $K$ = Safety factor (typically 3-10 depending on toxicity and mixing)
- $C_{permissible}$ = Permissible exposure limit (ppm)
- $C_{makeup}$ = Makeup air contaminant concentration (ppm)

## Formaldehyde Control Strategies

### Press Exhaust Systems

Hot press operations represent the primary formaldehyde emission source. Design considerations include:

**Press Opening Hoods:** Position high-velocity hoods (300-500 fpm face velocity) at press opening locations to capture the thermal plume and formaldehyde surge released when presses open.

**Continuous Press Exhaust:** For continuous laminating and pressing lines, provide lateral slot hoods along both sides of the press with minimum 200 fpm slot velocity:

$$Q_{slot} = 2 \cdot V_{slot} \cdot W \cdot L_{press}$$

Where:
- $Q_{slot}$ = Total slot exhaust (cfm)
- $V_{slot}$ = Slot velocity (fpm)
- $W$ = Slot width (ft), typically 0.25-0.5 ft
- $L_{press}$ = Press length (ft)
- Factor of 2 accounts for hoods on both sides

**Enclosure Ventilation:** Where feasible, enclose press areas and maintain negative pressure of 0.05-0.10 inches w.c. relative to adjacent occupied spaces. Provide 6-12 air changes per hour based on emission rates.

### Resin Application Zones

Resin blending, spraying, and curtain coating operations require dedicated LEV:

- **Spray booths:** Minimum 100 fpm face velocity across booth opening
- **Mixing tanks:** Rim exhaust or close-capture canopy hoods with 150-200 fpm capture velocity
- **Curtain coaters:** Lateral slot exhaust at both edges of the coating line

## VOC Control Strategies

### Source Capture

Implement high-efficiency capture systems at primary VOC sources:

**Dryer Exhaust:** Direct connection from rotary dryers, conveyor dryers, and UV curing systems. Calculate based on manufacturer specifications plus safety margin:

$$Q_{dryer} = Q_{process} \cdot 1.15$$

**Adhesive Application:** For solvent-based adhesives (less common in modern facilities), provide enclosed booths with minimum 150 fpm cross-draft velocity.

### Secondary Treatment

High VOC concentrations may require treatment before atmospheric discharge:

- **Thermal oxidizers:** For exhaust streams exceeding 500 ppm total VOCs
- **Regenerative thermal oxidizers (RTOs):** Energy-efficient option for continuous high-volume applications
- **Biofilters:** Lower capital cost alternative for moderate VOC concentrations (50-500 ppm) in facilities with space availability

## Dust Collection Integration

Coordinate formaldehyde and VOC exhaust with dust collection systems:

**Separate Systems:** Never combine high-temperature press exhaust with wood dust collection systems due to fire and explosion hazards.

**Filtration Requirements:** Wood dust exhaust requires baghouse or cartridge collectors with minimum 99% efficiency on particles ≥5 microns. Formaldehyde exhaust may use wet scrubbers or activated carbon adsorption.

**Airflow Distribution:** Size branch ducts to maintain minimum transport velocity:

$$V_{transport} = 4000-4500 \text{ fpm (wood dust)}$$

Design ductwork pressure drop using the Darcy-Weisbach equation, accounting for wood dust loading and potential buildup.

## Makeup Air Considerations

Provide conditioned makeup air equal to 90-100% of exhaust volume. Locate makeup air diffusers to:

- Avoid short-circuiting to exhaust points
- Prevent drafts across press openings that disrupt capture
- Supply fresh air to occupied zones before migrating to exhaust locations

For cold climates, makeup air heating can represent 40-60% of facility energy consumption. Consider heat recovery from dryer exhaust where formaldehyde concentrations permit.

## Regulatory Compliance

**OSHA PEL:** Formaldehyde 0.75 ppm (TWA), 2 ppm (STEL)
**NIOSH REL:** Formaldehyde lowest feasible concentration
**ACGIH TLV:** Formaldehyde 0.1 ppm (Ceiling)

Design exhaust systems to maintain exposures below 50% of applicable limits, with continuous monitoring in high-risk areas. The ACGIH Industrial Ventilation Manual Chapter 10 provides comprehensive design guidance specific to wood products manufacturing.

## Performance Verification

Commission all exhaust systems with documented testing:

- Hood face velocity measurements at representative points
- Capture efficiency smoke testing at maximum distance from hood
- Formaldehyde area monitoring in breathing zones
- Static pressure verification throughout duct network
- Filter pressure drop trending to establish replacement schedules

Maintain detailed maintenance logs and retest systems after any process modifications or equipment additions.
