---
title: "Hood Design Principles for Industrial Local Exhaust Ventilation"
description: "Comprehensive guide to industrial exhaust hood design including exterior hoods, enclosing hoods, receiving hoods, capture velocity, face velocity, and slot velocity principles per ACGIH standards."
keywords:
  - industrial exhaust hood design
  - capture velocity calculations
  - face velocity requirements
  - enclosing hood design
  - exterior hood ventilation
  - receiving hood principles
  - slot velocity optimization
  - ACGIH industrial ventilation
  - hood containment design
  - local exhaust ventilation
weight: 1
---

## Hood Classification and Selection

Industrial exhaust hoods are classified into three fundamental categories based on their relationship to the contaminant source and the physical principles governing contaminant capture. Proper classification determines the airflow requirements and design parameters.

### Exterior Hoods

Exterior hoods (also termed capturing hoods) are positioned outside the contaminant generation zone and rely on induced airflow to capture and transport contaminants into the hood opening. These hoods must overcome ambient air currents and the initial velocity of contaminant release.

**Critical design factors:**
- Hood placement distance from source directly affects required airflow
- Capture velocity must exceed contaminant dispersion velocity
- Airflow increases with the square of distance from hood face
- Cross-drafts significantly reduce capture efficiency

**Typical applications:**
- Welding stations with flexible positioning requirements
- Open surface tanks (plating, degreasing, etching)
- Grinding and buffing operations
- Material transfer points

### Enclosing Hoods

Enclosing hoods (including canopy hoods and booth-type designs) partially or fully surround the contaminant source, restricting contaminant dispersion paths and reducing required airflow. The degree of enclosure directly correlates with ventilation efficiency.

**Design hierarchy (most to least efficient):**
1. Total enclosure with minimal openings (laboratory hoods, glove boxes)
2. Booth-type enclosures with one open face (spray booths, downdraft tables)
3. Partial enclosures with multiple open sides (three-sided bench hoods)
4. Canopy hoods positioned above heat or buoyant contaminant sources

**Face velocity** becomes the primary design parameter for enclosing hoods. Face velocity is the average air velocity measured across the hood face opening and provides the control metric for adequate capture.

| Hood Type | Typical Face Velocity | Application |
|-----------|----------------------|-------------|
| Laboratory fume hood | 80-120 fpm | General chemical handling |
| Walk-in spray booth | 100 fpm | Large equipment painting |
| Bench-mounted booth | 100-150 fpm | Small parts finishing |
| Downdraft table | 150-200 fpm | Grinding, sanding operations |

### Receiving Hoods

Receiving hoods capture contaminants possessing inherent momentum or thermal buoyancy directed toward the hood opening. These hoods receive rather than capture contaminants, resulting in the lowest airflow requirements among hood types.

**Applicable conditions:**
- Heat sources producing strong thermal plumes (furnaces, ladles, melting operations)
- Processes with directed contaminant velocity (abrasive blasting, material discharge chutes)
- Vertically-directed releases into overhead canopy hoods

**Design considerations:**
- Hood face area must exceed the contaminant plume cross-section
- Capture distance limited to zone of plume stability
- Cross-drafts exceeding plume velocity will defeat capture
- Thermal stratification in receiving canopy hoods

## Capture Velocity Principles

Capture velocity represents the air velocity at the contaminant generation point required to overcome opposing air currents and direct contaminant movement into the hood. This velocity must be sufficient at the farthest point of contaminant generation.

**Velocity decay relationship:**

For an unflanged circular opening:
V_x = V_hood × (A / (10X² + A))

Where:
- V_x = velocity at distance X from hood face (fpm)
- V_hood = velocity at hood face (fpm)
- A = hood face area (ft²)
- X = distance from hood face (ft)

**Key principle:** Velocity decreases rapidly with distance from the hood opening. Doubling the capture distance requires approximately four times the airflow.

### ACGIH Recommended Capture Velocities

| Contaminant Release Condition | Capture Velocity Range |
|-------------------------------|------------------------|
| Released with no velocity into quiet air | 50-100 fpm |
| Released at low velocity into moderately still air | 100-200 fpm |
| Active generation into zone of rapid air motion | 200-500 fpm |
| Released at high velocity into very rapid air motion | 500-2000 fpm |

These values assume minimal cross-drafts. Cross-draft velocity exceeding 50% of capture velocity significantly reduces hood effectiveness.

## Slot Velocity and Hood Pressurization

For hoods incorporating slot openings (common in booth-type and lateral exhaust designs), slot velocity determines airflow distribution uniformity and hood static pressure requirements.

**Slot velocity** is the air velocity through the slot opening, typically 1000-2000 fpm for effective performance:
- Lower slot velocities (< 1000 fpm) result in poor airflow distribution
- Higher slot velocities (> 2500 fpm) create excessive static pressure loss and noise
- Plenum design behind slots must provide uniform pressure distribution

**Plenum sizing criterion:**
Plenum velocity should not exceed 50% of slot velocity to ensure uniform slot discharge. This relationship maintains pressure uniformity across the slot length.

## Containment Principles

Hood containment effectiveness depends on maintaining controlled airflow patterns that prevent contaminant escape. The fundamental principle requires that induced airflow velocity exceeds the maximum expected contaminant dispersion velocity at all potential escape points.

**Containment factors:**

1. **Geometric containment:** Physical barriers reduce open area and required airflow
2. **Velocity containment:** Sufficient face or capture velocity prevents escape
3. **Pressure containment:** Negative pressure relative to surroundings prevents outward migration

**Flanges and baffles:** Adding flanges to hood openings increases capture effectiveness by 25-40% for equivalent airflow. Flanges should extend at least the hood diameter (or equivalent diameter for rectangular openings) beyond the hood face.

**Airflow uniformity:** Face velocity variation should not exceed 20% across the hood opening. Non-uniform airflow creates dead zones allowing contaminant escape.

## Design Integration

Effective hood design requires integrating multiple velocity parameters:

1. **Determine hood classification** based on source characteristics and process constraints
2. **Calculate required capture velocity** using ACGIH guidelines for release conditions
3. **Establish hood-to-source distance** minimizing this distance reduces required airflow
4. **Compute required airflow** using appropriate velocity equations for hood type
5. **Design slot geometry** (if applicable) for uniform distribution and acceptable pressure loss
6. **Verify face velocity** for enclosing hoods meets minimum requirements
7. **Account for cross-drafts** increase design airflow by 50-100% in high-draft environments

The ACGIH Industrial Ventilation Manual provides detailed design procedures, coefficient values, and specific hood designs for hundreds of industrial processes. These standardized designs incorporate decades of empirical validation and represent best practice for common applications.

## Performance Verification

After installation, hood performance must be verified through direct measurement:
- Capture velocity measured at design control points using anemometer or velometer
- Face velocity measured at multiple points across hood opening (9-point grid minimum)
- Smoke tube testing to visualize airflow patterns and identify escape paths
- Static pressure measurements to verify fan performance and system balance

Measured values should meet or exceed design criteria under actual operating conditions including cross-drafts, thermal effects, and process variations.
