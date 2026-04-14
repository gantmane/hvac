---
title: "Laboratory Exhaust Systems"
aliases: ["Laboratory Exhaust Systems"]
description: "Comprehensive guide to laboratory exhaust systems including fume hood exhaust design, manifolded systems, stack height calculations, wind effects, and re-entrainment prevention per ANSI Z9.5 standards."
keywords: ["laboratory exhaust", "fume hood exhaust", "stack design", "ANSI Z9.5", "manifolded exhaust", "re-entrainment prevention", "laboratory ventilation", "exhaust stack height", "bypass air", "wind effects"]
tags: ["laboratory exhaust", "fume hood exhaust", "stack design", "ANSI Z9.5", "manifolded exhaust", "re-entrainment prevention", "laboratory ventilation", "exhaust stack height", "bypass air", "wind effects"]
date: 2026-01-05
draft: false
weight: 2
---

Laboratory exhaust systems provide critical life safety functions by capturing and removing hazardous contaminants generated during research and analytical procedures. Unlike general building exhaust, laboratory systems must operate continuously with precise control to maintain containment while preventing re-entrainment of exhausted contaminants into building air intakes.

## Fume Hood Exhaust Requirements

Fume hoods represent the primary containment device in most laboratories. The exhaust system must maintain consistent face velocity across the hood opening regardless of sash position or building pressure fluctuations.

**Face Velocity Standards:**
- Typical range: 80-120 fpm (ANSI Z9.5)
- Research facilities: 100 fpm average
- High-hazard applications: up to 150 fpm
- Measurement grid: 6-inch spacing across opening

Face velocity alone does not ensure containment. The system must minimize cross-drafts at the hood face (below 50 fpm perpendicular to face) and maintain turbulence-free airflow within the hood interior. Supply air diffusers should be positioned at least 10 feet from hood faces or oriented away to prevent disruption of capture velocity.

## Bypass Air Configuration

Constant volume fume hoods without bypass dampers create significant challenges when sash position changes. As the sash closes, face velocity increases dramatically, potentially creating turbulence that compromises containment.

**Bypass Air Design:**
- Opens when sash closes to maintain constant exhaust volume
- Bypass opening area typically 50-60% of sash opening area
- Activation occurs when sash reaches 50% closed position
- Prevents face velocity from exceeding 150 fpm at minimum sash opening

Modern variable air volume (VAV) systems eliminate bypass requirements by modulating exhaust fan speed based on sash position sensors. VAV systems reduce energy consumption by 50-70% compared to constant volume bypass designs while maintaining equivalent containment performance.

## Manifolded Exhaust Systems

Individual exhaust fans for each fume hood create excessive noise, maintenance requirements, and roof penetrations. Manifolded systems combine multiple hoods onto common ductwork serving a central exhaust fan.

**Manifold Design Criteria:**
- Minimum duct velocity: 2000 fpm (prevents particulate settling)
- Maximum velocity: 3500 fpm (limits pressure drop and noise)
- Duct material: PVC, stainless steel, or coated carbon steel based on chemical exposure
- Slope: 0.25 inch per foot toward collection points for condensate drainage

Chemical compatibility determines manifold configuration. Incompatible chemicals (acids with bases, oxidizers with organics) must use separate exhaust systems to prevent reactions in ductwork. ANSI Z9.5 provides chemical compatibility matrices for manifold design.

Manifolded systems require careful balancing. Each hood must maintain design face velocity regardless of other hoods operating or idle. VAV systems with pressure-independent control at each hood eliminate rebalancing requirements when hoods are added or removed from service.

## Stack Design and Height Determination

The exhaust stack must discharge contaminants at sufficient height and velocity to prevent re-entrainment into building air intakes, occupied areas, or adjacent buildings.

**Discharge Velocity:**
- Minimum: 3000 fpm (prevents downdrafts)
- Optimal: 4000-5000 fpm (ensures plume rise)
- Stack diameter sized to achieve velocity at maximum exhaust volume

**Stack Height Calculation (ANSI Z9.5 Method):**

For stacks on flat roofs:
```
H = h + 1.5L
```
Where:
- H = stack height above roof
- h = height of nearby building wake zone (0.5 × building height)
- L = lesser of building height or maximum building width

Minimum stack height: 10 feet above roof line for low-toxicity applications. High-toxicity exhausts require atmospheric dispersion modeling per EPA guidelines to ensure ground-level concentrations remain below permissible exposure limits (PELs).

## Wind Effects and Re-entrainment Prevention

Wind creates positive and negative pressure zones on building surfaces. Exhaust stacks in negative pressure zones experience flow reversal, while those in positive zones achieve enhanced dispersion.

**Critical Separation Distances:**
- Stack to air intake: minimum 20 feet horizontal + 10 feet vertical
- Stack to operable window: minimum 10 feet any direction
- Stack to adjacent building: atmospheric modeling required

Architectural features (penthouses, mechanical rooms, parapet walls) create recirculation zones extending 3-5 times the feature height downwind. Stacks must penetrate above these zones or relocate upwind of obstacles.

**Rain Cap Selection:**

Traditional rain caps (mushroom, cone) reduce effective discharge velocity by 50% and create turbulence that promotes re-entrainment. Preferred alternatives:
- Vertical discharge with no cap (self-draining design)
- Tapered stack tip (increases exit velocity)
- Horizontal discharge for corrosive exhausts (prevents drainage into ductwork)

## Exhaust Fan Selection

Laboratory exhaust fans must overcome system pressure drop while maintaining stable operation across variable flow conditions.

**Performance Requirements:**

| Parameter | Specification |
|-----------|---------------|
| Fan type | Backward-inclined centrifugal or vaneaxial |
| Pressure capability | 4-8 inches w.g. typical |
| Turndown ratio | 10:1 minimum (VAV systems) |
| Control response | 2-second maximum lag |
| Redundancy | N+1 for critical facilities |

Fans handling corrosive exhausts require coated or non-metallic construction (FRP, PVC). Direct-drive fans eliminate belt maintenance and reduce energy consumption by 15% compared to belt-driven designs.

Backup power (emergency generator or UPS) must support exhaust systems in facilities handling highly toxic materials. Loss of exhaust ventilation in these spaces creates immediate life safety hazards requiring building evacuation.

## System Monitoring and Control

Laboratory exhaust systems require continuous monitoring to ensure containment performance and energy efficiency.

**Critical Parameters:**
- Face velocity (±20% of setpoint triggers alarm)
- Exhaust airflow (±10% of design)
- Duct static pressure (indicates filter loading or system degradation)
- Stack discharge velocity (verified during TAB and annually)

Building automation systems must maintain exhaust volume at least 10% greater than supply volume to ensure negative pressure in laboratory spaces. Differential pressure transmitters with local displays provide immediate feedback on space pressurization status.

Annual testing per ANSI Z9.5 includes face velocity surveys, tracer gas containment testing (sulfur hexafluoride or titanium tetrachloride smoke), and alarm verification. Documentation demonstrates regulatory compliance and identifies degradation requiring corrective action.
