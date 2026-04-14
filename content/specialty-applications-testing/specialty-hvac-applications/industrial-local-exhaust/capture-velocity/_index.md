---
title: "Capture Velocity for Industrial Local Exhaust"
aliases: ["Capture Velocity for Industrial Local Exhaust"]
weight: 2
description: "Technical analysis of capture velocity ranges, contaminant generation conditions, velocity decay relationships, and distance effects for local exhaust ventilation hood design"
keywords: ["capture velocity", "local exhaust ventilation", "hood design", "velocity decay", "ACGIH", "industrial ventilation", "contaminant capture", "fpm ranges"]
tags: ["capture velocity", "local exhaust ventilation", "hood design", "velocity decay", "ACGIH", "industrial ventilation", "contaminant capture", "fpm ranges"]
---

Capture velocity represents the air velocity at any point in front of a hood or opening necessary to overcome opposing air currents and capture contaminated air at that point by drawing it into the exhaust system. This fundamental parameter determines the effectiveness of local exhaust ventilation in controlling airborne contaminants at the source.

## Velocity Requirements by Contaminant Condition

The required capture velocity depends on the conditions under which contaminants are released into the workroom air. ACGIH Industrial Ventilation Manual establishes four distinct categories based on contaminant dispersion energy.

### Released with Minimal Velocity (50-100 FPM)

Applied when contaminants are released into essentially still air with minimal kinetic energy:

- Evaporation from degreasing tanks
- Evaporation from open surface tanks
- Gas evolution from plating baths
- Booths for spray painting (large enclosed volume)
- Welding with minimal air movement

The low energy release allows relatively low capture velocities to maintain control. Air currents from general ventilation or personnel movement often exceed the release energy.

### Released at Low Velocity (100-200 FPM)

Applied when contaminants are released with low kinetic energy into moderately still air:

- Spray booths with controlled air patterns
- Intermittent container filling
- Low-speed conveyor transfers
- Bench-scale mixing operations
- Crushers and grinders with minimal product velocity
- Barrel filling with controlled pour rates

The moderate release energy requires higher capture velocities to counteract the initial momentum of the contaminant stream.

### Active Generation (200-500 FPM)

Applied when contaminants are released with significant initial velocity or in zones with substantial cross-drafts:

- Grinding operations
- Abrasive blasting
- Barrel filling with free-fall discharge
- High-speed conveyor transfer points
- Crushers with significant particle ejection
- Tumbling and shaking operations
- Active hand-grinding and polishing

The substantial release energy demands capture velocities sufficient to overcome both the initial contaminant momentum and competing air currents.

### High-Energy Release (500-2000 FPM)

Applied to processes generating high-velocity contaminant dispersal:

- Abrasive blasting in open areas
- Heavy grinding with significant sparks
- High-energy crushing operations
- Processes with explosive release characteristics

These extreme conditions require exceptionally high capture velocities, often necessitating enclosing hoods or containment strategies rather than relying solely on induced airflow.

## Velocity Decay Relationships

The air velocity induced by a hood decreases rapidly with distance from the hood face. This decay relationship determines the effective capture zone and influences hood placement relative to contaminant sources.

### Plain Opening (Unflanged)

For a plain rectangular or circular opening without flanges, the centerline velocity follows:

**V<sub>x</sub> = V<sub>f</sub> × (A / [10X² + A])**

Where:
- V<sub>x</sub> = velocity at distance X from hood face (FPM)
- V<sub>f</sub> = face velocity at hood opening (FPM)
- A = hood face area (ft²)
- X = distance from hood face (ft)

This relationship demonstrates the rapid decay in capture velocity. At a distance equal to one hood diameter (or equivalent diameter for rectangular openings), velocity drops to approximately 10% of face velocity.

### Flanged Opening

Adding a flange to the hood perimeter improves velocity projection:

**V<sub>x</sub> = V<sub>f</sub> × (A / [10X² + A]) × 1.4**

The flange factor of 1.4 reflects the elimination of flow from the rear hemisphere, concentrating airflow in the capture direction. This 40% improvement in velocity projection justifies flanging most exterior hoods.

### Slot Hood

For slot hoods with aspect ratio (length to width) greater than 5:1:

**V<sub>x</sub> = V<sub>s</sub> × (W / [5X + W])**

Where:
- V<sub>s</sub> = slot velocity (FPM)
- W = slot width (ft)
- X = distance from slot face (ft)

Slot hoods exhibit less dramatic velocity decay due to their two-dimensional flow characteristics, making them effective for capturing contaminants along extended line sources.

## Distance Effects on System Performance

The relationship between capture velocity and distance creates critical design constraints for local exhaust systems.

### Practical Capture Distance

The maximum effective capture distance rarely exceeds 1.5 hood diameters for plain openings or 2.0 hood diameters for flanged openings. Beyond these distances, required volumetric flow rates become excessive and the hood loses effectiveness against cross-drafts.

**Example Calculation:**

A 12-inch diameter flanged hood requiring 200 FPM capture velocity at the source:

At X = 0.5 ft (6 inches, 0.5 hood diameters):
- V<sub>0.5</sub> = V<sub>f</sub> × (0.785 / [10(0.5)² + 0.785]) × 1.4
- V<sub>0.5</sub> = V<sub>f</sub> × (0.785 / 3.285) × 1.4
- V<sub>0.5</sub> = V<sub>f</sub> × 0.334

To achieve 200 FPM at 6 inches requires:
- V<sub>f</sub> = 200 / 0.334 = 599 FPM
- Q = 599 FPM × 0.785 ft² = 470 CFM

At X = 1.0 ft (12 inches, 1.0 hood diameter):
- V<sub>1.0</sub> = V<sub>f</sub> × (0.785 / [10(1.0)² + 0.785]) × 1.4
- V<sub>1.0</sub> = V<sub>f</sub> × 0.102

To achieve 200 FPM at 12 inches requires:
- V<sub>f</sub> = 200 / 0.102 = 1,961 FPM
- Q = 1,961 FPM × 0.785 ft² = 1,539 CFM

Doubling the distance increases the required flow rate by more than 300%, illustrating why minimizing capture distance is the most effective design strategy.

### Cross-Draft Sensitivity

As distance from the hood increases, sensitivity to cross-drafts increases exponentially. A 50 FPM cross-draft may be negligible at 0.25 hood diameters but completely disrupts capture at 1.5 diameters. This sensitivity necessitates:

- Positioning hoods as close to sources as operationally feasible
- Evaluating room air patterns during hood placement
- Installing baffles or enclosures in high-traffic or high-air-movement areas
- Increasing design capture velocity margins in critical applications

## Design Application Strategy

Select capture velocity based on the highest energy release condition encountered during operation. A process alternating between low and active generation requires designing for the 200-500 FPM range to ensure continuous control.

Minimize capture distance through process analysis and hood placement optimization before increasing volumetric flow rates. The inverse square relationship in velocity decay equations makes distance reduction far more efficient than flow rate increases.

Verify actual capture velocities during commissioning using measurements at multiple points within the intended capture zone. Theoretical calculations assume ideal conditions; field measurements confirm performance under actual operating conditions including cross-drafts and thermal effects.

