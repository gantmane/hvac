---
title: "Wind Exposure Categories for HVAC Equipment Design"
aliases: ["Wind Exposure Categories for HVAC Equipment Design"]
description: "Comprehensive guide to ASCE 7 wind exposure categories B, C, and D for HVAC equipment design, including terrain roughness, velocity pressure coefficients, and determination procedures."
date: 2025-01-05
weight: 2
draft: false
tags: ["wind load design", "exposure categories", "ASCE 7", "velocity pressure", "terrain roughness", "rooftop equipment", "wind resistant design", "structural design"]
keywords: ["wind exposure categories", "ASCE 7 exposure", "exposure coefficient", "terrain roughness", "velocity pressure coefficient", "rooftop HVAC wind loads", "exposure B C D", "surface roughness length"]
---

## Overview

Wind exposure categories represent the influence of terrain roughness on wind velocity profiles. ASCE 7 defines three exposure categories (B, C, D) that fundamentally affect the calculation of design wind pressures on HVAC equipment. The exposure category determines the velocity pressure exposure coefficient (Kz), which accounts for the increase in wind speed with height above ground and varies based on surrounding terrain characteristics.

Selection of the correct exposure category is critical for accurate wind load determination on rooftop HVAC units, cooling towers, air-cooled condensers, and outdoor mechanical equipment.

## Exposure Category Definitions

### Exposure B: Urban and Suburban Terrain

Exposure B represents urban and suburban areas with numerous closely spaced obstructions having the size of single-family dwellings or larger.

**Terrain characteristics:**
- Buildings, forest, or surface irregularities covering at least 20% of the ground surface
- Obstructions present for at least 2,600 ft (792 m) or 20 times the building height upwind
- Average height of obstructions exceeds 30 ft (9.1 m)

**Typical environments:**
- Residential neighborhoods with dense housing
- Urban areas with multi-story buildings
- Forested areas with mature tree canopy
- Industrial parks with large structures

Surface roughness length: $z_0 = 1.0$ m

### Exposure C: Open Terrain

Exposure C represents open terrain with scattered obstructions having heights generally less than 30 ft (9.1 m).

**Terrain characteristics:**
- Flat, open country and grasslands
- Scattered obstructions with separations of at least 40 times obstacle height
- Open water surfaces within hurricane-prone regions (not frozen)
- Smooth mud flats, salt flats, and unbroken ice

**Typical environments:**
- Agricultural areas with minimal structures
- Airports and airfields
- Coastal regions without development
- Prairie and grassland areas

Surface roughness length: $z_0 = 0.15$ m

### Exposure D: Flat Unobstructed Coastal Areas

Exposure D represents flat, unobstructed areas exposed to wind flowing over open water for a distance of at least 5,000 ft (1,524 m) or 20 times the building height.

**Terrain characteristics:**
- Located within 600 ft (183 m) or 20 times building height from shoreline
- Open water upwind for minimum 1 mile (1.61 km)
- Smooth surfaces with essentially no obstructions
- Surf zone and immediate coastal areas

**Typical environments:**
- Beachfront properties
- Offshore platforms
- Coastal piers and wharfs
- Low-lying barrier islands

Surface roughness length: $z_0 = 0.03$ m

## Exposure Category Comparison

| Parameter | Exposure B | Exposure C | Exposure D |
|-----------|------------|------------|------------|
| Surface Roughness ($z_0$) | 1.0 m | 0.15 m | 0.03 m |
| Gradient Height ($z_g$) | 1,200 ft (365.8 m) | 900 ft (274.3 m) | 700 ft (213.4 m) |
| Power Law Exponent ($\alpha$) | 7.0 | 9.5 | 11.5 |
| Minimum Design Height | 30 ft (9.1 m) | 15 ft (4.6 m) | 15 ft (4.6 m) |
| Typical Kz at 30 ft | 0.70 | 0.85 | 0.90 |
| Typical Kz at 60 ft | 0.85 | 1.03 | 1.10 |
| Wind Speed Increase Rate | Gradual | Moderate | Rapid |

## Velocity Pressure Exposure Coefficient (Kz)

The velocity pressure exposure coefficient varies with height and exposure category according to the power law relationship:

For heights 15 ft ≤ z ≤ $z_g$:

$$K_z = 2.01 \left(\frac{z}{z_g}\right)^{2/\alpha}$$

Where:
- $z$ = height above ground level (ft)
- $z_g$ = gradient height (ft), see table above
- $\alpha$ = power law exponent, see table above

For heights z < 15 ft:

$$K_z = 2.01 \left(\frac{15}{z_g}\right)^{2/\alpha}$$

### Simplified Calculation for Typical Heights

**At 30 ft above ground:**

- Exposure B: $K_z = 2.01 \times (30/1200)^{2/7.0} = 0.70$
- Exposure C: $K_z = 2.01 \times (30/900)^{2/9.5} = 0.85$
- Exposure D: $K_z = 2.01 \times (30/700)^{2/11.5} = 0.90$

**At 60 ft above ground:**

- Exposure B: $K_z = 2.01 \times (60/1200)^{2/7.0} = 0.85$
- Exposure C: $K_z = 2.01 \times (60/900)^{2/9.5} = 1.03$
- Exposure D: $K_z = 2.01 \times (60/700)^{2/11.5} = 1.10$

## Exposure Determination Procedures

### ASCE 7 Section 26.7 Methodology

**Step 1: Identify Site Location**
- Determine distance from shoreline for coastal sites
- Map surrounding terrain within 45-degree sectors radiating from structure

**Step 2: Evaluate Upwind Terrain**
- Assess terrain for a distance of 20 times building height or 2,600 ft minimum
- Consider all directions that contribute to design wind loads
- Document surface roughness characteristics

**Step 3: Apply Directional Assessment**
- Evaluate exposure for each cardinal and intercardinal direction
- Use most conservative exposure when loads are direction-dependent
- Consider surrounding development that may change over structure lifetime

**Step 4: Special Provisions**
- For sites in transition zones, use Exposure C unless Exposure B terrain extends upwind for required distance
- Exposure D applies only within specified distance from open water shoreline
- Elevated structures (on stilts/piers) typically use Exposure C minimum

### HVAC Equipment Considerations

**Rooftop Equipment:**
- Equipment height above roof level must be added to building height
- Parapet effects may reduce effective exposure height
- Equipment mounted on screens or platforms requires height adjustment

**Grade-Level Equipment:**
- Large equipment may create its own wake effects
- Screening and fencing can modify local exposure
- Equipment height determines applicable Kz value

**Elevated Platforms:**
- Use actual equipment centerline height above grade
- Consider platform structure in total height calculation
- Lattice platforms may have reduced wind blocking effects

## Impact on HVAC Design Wind Pressures

The velocity pressure at height z is calculated as:

$$q_z = 0.00256 K_z K_{zt} K_d V^2$$

Where:
- $q_z$ = velocity pressure (psf)
- $K_z$ = velocity pressure exposure coefficient
- $K_{zt}$ = topographic factor
- $K_d$ = wind directionality factor
- $V$ = basic wind speed (mph)

**Example calculation** for 100 mph basic wind speed at 30 ft height:

- Exposure B: $q_z = 0.00256 \times 0.70 \times 1.0 \times 0.85 \times 100^2 = 15.2$ psf
- Exposure C: $q_z = 0.00256 \times 0.85 \times 1.0 \times 0.85 \times 100^2 = 18.5$ psf
- Exposure D: $q_z = 0.00256 \times 0.90 \times 1.0 \times 0.85 \times 100^2 = 19.6$ psf

The difference between Exposure B and D represents a 29% increase in velocity pressure, resulting in significantly higher design loads on HVAC equipment.

## Common Design Errors

**Inappropriate Exposure Selection:**
- Assuming Exposure B for all urban locations without verifying terrain characteristics
- Failing to account for cleared areas upwind of structure
- Not considering future development that may alter exposure

**Height Determination Issues:**
- Using building height instead of equipment centerline height
- Neglecting equipment mounted above rooftop on platforms
- Incorrectly applying minimum height provisions

**Directional Considerations:**
- Using single exposure for all wind directions
- Not accounting for asymmetric terrain conditions
- Failing to identify critical wind direction for equipment orientation

## Documentation Requirements

**Design Documentation:**
- Site plan showing surrounding terrain features
- Photographs or aerial imagery of upwind terrain
- Calculation of distances to surface roughness transitions
- Justification for exposure category selection by direction

**Submittal Information:**
- Exposure category used for each wind direction
- Equipment height above grade
- Velocity pressure calculations with all coefficients
- Reference to applicable ASCE 7 edition

## Summary

Proper determination of wind exposure category is essential for accurate HVAC equipment wind load calculations. The exposure coefficient Kz can vary by up to 29% between Exposure B and D at typical equipment heights, directly impacting structural requirements for equipment anchorage, support structures, and vibration isolation systems. Engineers must carefully evaluate terrain characteristics following ASCE 7 procedures and document exposure determination to ensure code-compliant, safe installations.
