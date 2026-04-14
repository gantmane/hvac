---
title: "Industrial Local Exhaust Ventilation"
aliases: ["Industrial Local Exhaust Ventilation"]
description: "Comprehensive guide to industrial local exhaust systems including hood design, capture velocity calculations, duct system design, air cleaning equipment, and contaminant control strategies for workplace safety."
keywords: "industrial exhaust, local exhaust ventilation, LEV, capture velocity, hood design, ACGIH, contaminant control, industrial ventilation, fume hood, dust collection"
tags: ["industrial exhaust", "local exhaust ventilation", "LEV", "capture velocity", "hood design", "ACGIH", "contaminant control", "industrial ventilation", "fume hood", "dust collection"]
weight: 14
---

## Overview

Industrial local exhaust ventilation (LEV) systems capture contaminants at their source before they enter the worker's breathing zone or general workspace. Unlike dilution ventilation, which reduces contaminant concentration throughout an entire space, LEV provides targeted control where emissions occur, making it the preferred method for toxic, flammable, or nuisance particulates and gases.

Proper LEV design requires understanding contaminant characteristics, process operations, and fundamental fluid mechanics. The American Conference of Governmental Industrial Hygienists (ACGIH) *Industrial Ventilation: A Manual of Recommended Practice* serves as the authoritative reference for LEV system design and performance verification.

## System Components

A complete LEV system consists of four primary elements:

**Hood**: The capture device positioned at or near the contaminant source. Hood effectiveness depends on geometry, placement relative to the source, and airflow rate.

**Ductwork**: Conveys contaminated air from hoods to air cleaning equipment or discharge points. Duct sizing must maintain minimum transport velocities to prevent particle settling.

**Air Cleaner**: Removes contaminants before air discharge to atmosphere or recirculation. Selection depends on contaminant type, concentration, particle size distribution, and regulatory requirements.

**Fan**: Provides motive force to overcome system resistance and maintain required airflow rates. Fan selection requires accurate static pressure and volumetric flow calculations.

## Capture Velocity Principles

Capture velocity is the air velocity at any point in front of a hood necessary to overcome opposing air currents and capture contaminated air. This velocity depends on contaminant generation characteristics and external disturbances.

### Capture Velocity Categories

ACGIH provides recommended capture velocity ranges based on contaminant release conditions:

| Release Condition | Capture Velocity Range |
|-------------------|------------------------|
| Released with no velocity into quiet air | 50-100 fpm |
| Released at low velocity into moderately still air | 100-200 fpm |
| Active generation into zone of rapid air motion | 200-500 fpm |
| Released at high velocity into very rapid air motion | 500-2000 fpm |

These values represent minimum face velocities for hood openings or velocities at specified distances for exterior hoods.

### Velocity Decay

Air velocity decreases rapidly with distance from a hood opening. For an unflanged plain opening, velocity at a point along the centerline follows:

**V_x = V_face × (10 × A)/(10 × A + x²)**

Where:
- V_x = velocity at distance x from hood face (fpm)
- V_face = face velocity at hood opening (fpm)
- A = hood face area (ft²)
- x = distance from hood face (ft)

This relationship demonstrates why hoods must be positioned as close as practical to contaminant sources. Doubling the distance reduces capture effectiveness dramatically.

## Hood Design Basics

Hood selection and design represent the most critical decisions in LEV system performance.

### Hood Classifications

**Enclosing Hoods**: Partially or fully enclose the contaminant source, requiring minimal airflow since the hood physically contains emissions. Examples include laboratory fume hoods, spray booths, and abrasive blasting cabinets.

**Exterior Hoods**: Positioned adjacent to but not enclosing the source, relying on airflow to capture and transport contaminants. Categories include canopy hoods, side-draft hoods, downdraft tables, and receiving hoods.

**Design Considerations**

Effective hood design requires:

- **Minimize hood face area** while maintaining adequate access for process operations. Smaller openings require less airflow for equivalent face velocity.

- **Position for natural contaminant trajectory**. Place hoods to intercept contaminants moving due to thermal buoyancy, process momentum, or material handling patterns.

- **Add flanges or baffles** to improve directional airflow. A properly designed flange can reduce required airflow by 25% compared to unflanged openings.

- **Avoid cross-drafts**. Position hoods away from doors, windows, HVAC supply diffusers, and traffic patterns that create competing air currents.

- **Provide uniform face velocity**. Incorporate plenums, perforated plates, or slot designs to distribute airflow evenly across the hood opening.

## Duct System Design

Duct transport velocity must exceed the minimum velocity required to prevent particle settling. ACGIH recommendations based on contaminant characteristics:

| Contaminant Nature | Minimum Transport Velocity |
|--------------------|---------------------------|
| Gases, vapors, smoke | 1000-2000 fpm |
| Fumes | 2000-2500 fpm |
| Light dust | 2500-3000 fpm |
| Dry dust and powders | 3000-3500 fpm |
| Average industrial dust | 3500-4000 fpm |
| Heavy dust, metal chips | 4000-4500 fpm |

### Pressure Loss Calculations

Total system static pressure equals the sum of:

- Hood entry losses (function of hood geometry and velocity pressure)
- Straight duct friction losses (function of velocity, duct diameter, length, and surface roughness)
- Fitting losses (elbows, transitions, branches expressed as velocity pressure multiples)
- Air cleaner pressure drop (manufacturer data at specified airflow)
- Discharge losses at stack or return

Accurate pressure calculations ensure proper fan selection and system balancing.

## Air Cleaning Equipment

Air cleaner selection depends on contaminant physical state, particle size, concentration, collection efficiency requirements, and disposal considerations.

**Particulate Control**:
- Cyclones: 5-100 micron particles, moderate efficiency
- Fabric filters (baghouses): 0.5+ micron particles, high efficiency
- Wet scrubbers: wide particle range, simultaneous gas absorption
- Electrostatic precipitators: submicron capability, low pressure drop

**Gaseous Contaminant Control**:
- Activated carbon adsorption: organic vapors
- Chemical scrubbers: acid gases, alkaline compounds
- Oxidizers: thermal or catalytic destruction

## Performance Verification

ACGIH standards require periodic testing to verify system performance:

- **Hood static pressure**: Verify adequate suction using manometers at designated test ports
- **Face velocity measurements**: Grid measurements across hood openings
- **Duct velocity**: Pitot tube traverses to confirm transport velocity
- **Qualitative smoke testing**: Visual verification of capture patterns

Maintain test records documenting airflow rates, static pressures, and any corrective actions taken to maintain design performance.

## Conclusion

Industrial local exhaust ventilation provides essential worker protection when designed and maintained according to established engineering principles. Successful systems balance hood effectiveness, energy efficiency, and operational practicality while meeting occupational exposure limits and regulatory requirements. The ACGIH *Industrial Ventilation Manual* remains the definitive resource for calculation methods, design standards, and performance criteria in this specialized HVAC discipline.
