---
title: "Design Considerations"
weight: 3
description: "Engineering design methodology for infrared radiant heating systems including mounting height calculations, spacing optimization, pattern factor analysis, thermal comfort criteria, mean radiant temperature (MRT), energy effectiveness analysis, and application-specific design strategies for warehouses, hangars, and outdoor heating."
keywords: "infrared design, radiant heating design, mounting height, pattern factor, mean radiant temperature, MRT, operative temperature, energy effectiveness, radiant comfort, heater spacing"
---

# Design Considerations for Infrared Radiant Heating

Successful infrared radiant heating system design requires systematic analysis of mounting geometry, thermal comfort parameters, and energy effectiveness to deliver adequate floor-level radiant intensity while maintaining acceptable pattern uniformity and occupant comfort. Unlike convective heating where air temperature alone determines comfort, radiant systems create thermal environments where mean radiant temperature (MRT) and operative temperature govern occupant sensation, enabling lower air temperatures (4-6°F reduction) while maintaining equal comfort through direct radiant heat transfer to surfaces and occupants.

## Design Process Overview

**Systematic design methodology:**

1. **Application analysis:** Building type, ceiling height, occupancy patterns, comfort requirements
2. **Heat load calculation:** Design heat loss, pickup load, infiltration
3. **System selection:** High-intensity vs. low-intensity, gas vs. electric
4. **Mounting height determination:** Balance coverage area and floor-level intensity
5. **Heater spacing calculation:** Uniform pattern or acceptable variation
6. **Capacity sizing:** Energy effectiveness-based capacity determination
7. **Comfort verification:** MRT, operative temperature, radiant asymmetry
8. **Control strategy:** Staging, setback, zone control optimization
9. **Economic analysis:** Life-cycle cost, payback period

## Mounting Height Analysis

### Coverage vs. Intensity Trade-Off

Floor-level radiant intensity decreases with mounting height following inverse square law:

$$I_{floor} = \frac{I_0 \cos^3(\alpha)}{r^2}$$

Simultaneously, coverage diameter increases linearly with height:

$$D_{coverage} = 2H \tan(\theta/2)$$

**Optimization objective:** Maximize coverage while maintaining minimum required floor intensity.

### Optimal Height Calculation

For uniform heating applications, optimal mounting height:

$$H_{opt} = \sqrt{\frac{Q_{radiant}}{I_{required,min} \times \pi \times \tan^2(\theta/2)}}$$

Where:
- $Q_{radiant}$ = Heater radiant output (Btu/h)
- $I_{required,min}$ = Minimum acceptable floor intensity (Btu/h·ft²)
- $\theta$ = Reflector beam angle

**Example:**
- Low-intensity tube: 80,000 Btu/h input, 50% radiant fraction = 40,000 Btu/h radiant
- Required intensity: 25 Btu/h·ft² minimum
- Beam angle: 70°
- $H_{opt} = \sqrt{40,000 / (25 \times \pi \times \tan^2(35°))} = \sqrt{40,000 / (25 \times 1.54)} = 32$ ft

### Practical Height Constraints

**Minimum heights:**
- Safety (prevent excessive radiant asymmetry): 8-10 ft occupied areas
- Code requirements: Vary by jurisdiction
- Thermal comfort: Avoid >15°F vertical asymmetry

**Maximum heights:**
- High-intensity gas: 30 ft practical limit
- Low-intensity gas: 40 ft practical limit
- Beyond limits: Intensity becomes inadequate

**Typical ranges:**

| Application | Ceiling Height | Mounting Height |
|-------------|----------------|-----------------|
| Loading dock | 14-20 ft | 12-18 ft |
| Warehouse | 24-32 ft | 20-28 ft |
| Manufacturing | 20-30 ft | 18-26 ft |
| Aircraft hangar | 40-80 ft | 35-40 ft (low-int.), supplement with high-int. spot |

## Heater Spacing Design

### Uniform Coverage Criterion

Pattern factor at midpoint between adjacent heaters determines uniformity:

$$P_f = \frac{I_{max}}{I_{avg}}$$

**Design targets:**
- Uniform heating (warehouses, manufacturing): $P_f$ < 1.5
- Moderate uniformity (storage areas): $P_f$ < 2.0
- Spot heating acceptable: $P_f$ = 3.0-5.0

### Spacing Calculation

For overlapping patterns maintaining uniformity:

$$S = 2H \tan(\theta/2) \times C_o$$

Where:
- $S$ = Center-to-center spacing
- $H$ = Mounting height
- $\theta$ = Effective beam angle
- $C_o$ = Overlap coefficient (0.80-0.90 for smooth transitions)

**Verification:** Calculate intensity at midpoint:

$$I_{midpoint} = 2 \times I_0 \frac{\cos^3(\alpha_{edge})}{r_{edge}^2}$$

Where $\alpha_{edge}$ and $r_{edge}$ are angle and distance from heater to midpoint.

**Example:**
- $H$ = 24 ft
- $\theta$ = 70° (low-intensity tube with semi-cylindrical reflector)
- $C_o$ = 0.85

$$S = 2 \times 24 \times \tan(35°) \times 0.85 = 28.6 \text{ ft spacing}$$

### Array Layout Strategies

**Parallel tube arrays:**
- Long straight runs for rectangular buildings
- Tubes parallel to long dimension (minimize end losses)
- Perpendicular to primary airflow (if significant)

**Grid patterns:**
- U-tube configurations in grid
- Suitable for square or irregular spaces
- Individual heater control for zoning

**Perimeter + interior:**
- Higher density perimeter zones (greater heat loss)
- Lower density interior zones
- Separate control for load matching

## Pattern Factor and Uniformity

### Pattern Factor Calculation

For single heater, pattern factor:

$$P_f = \frac{I(0,H)}{I_{avg}}$$

Where:
- $I(0,H)$ = Intensity directly below heater at height $H$
- $I_{avg}$ = Average intensity over coverage area

**High-intensity heaters:**
- Narrow beam (60°): $P_f$ = 4.0-5.5
- Medium beam (75°): $P_f$ = 2.8-3.8
- Wide beam (90°): $P_f$ = 2.0-2.8

**Low-intensity tube heaters:**
- Semi-cylindrical reflector: $P_f$ = 1.5-2.0
- V-reflector: $P_f$ = 2.0-2.8

### Overlapping Patterns

Multiple heaters with overlapping coverage reduce pattern factor:

$$P_{f,array} = P_{f,single} \times R_{overlap}$$

Where $R_{overlap}$ = 0.6-0.8 for proper spacing.

**Example:** Low-intensity tube with $P_{f,single}$ = 1.8, proper spacing
- $P_{f,array} = 1.8 \times 0.70 = 1.26$ (excellent uniformity)

### Acceptable Variation

**Comfort applications:**
- Intensity variation: ±25% maximum
- Temperature variation: ±3°F floor-level air
- MRT variation: ±5°F across occupied zone

**Process applications:**
- May require tighter control (±10-15%)
- Multiple zones with independent control
- Continuous monitoring and adjustment

## Browse Subtopics

- **[Thermal Comfort and MRT](./comfort-radiant/)** - Mean radiant temperature calculations, operative temperature, ASHRAE 55 comfort criteria, radiant asymmetry limits, and occupant thermal sensation in radiant-heated spaces
- **[Performance Factors and Energy Effectiveness](./performance-factors/)** - Energy effectiveness methodology, radiant fraction analysis, absorption efficiency, stratification reduction, comparative performance metrics
- **[Application-Specific Design](./application-specific/)** - Warehouses, aircraft hangars, loading docks, manufacturing facilities, outdoor heating areas, and agricultural buildings

## Key Design Parameters Summary

**Mounting height:**
- Determined by ceiling height, coverage requirements, intensity needs
- Typical: 0.85-0.95× ceiling height
- Verify minimum 18-24 in clearance to ceiling

**Heater spacing:**
- Calculate based on beam angle and overlap factor
- Typical: 1.1-1.4× mounting height for low-intensity
- Verify acceptable pattern factor

**Capacity:**
- Size for design heat loss ÷ energy effectiveness
- Energy effectiveness: 50-70% (gas infrared), 60-90% (electric infrared)
- Compare to 20-40% for forced-air in high-bay

**Comfort criteria:**
- Maintain operative temperature 68-72°F
- Air temperature may be 4-6°F lower than conventional
- Limit radiant asymmetry to <15°F vertical, <10°F horizontal

**Control:**
- Zone by use pattern (perimeter/interior, occupied/storage)
- Implement setback for unoccupied periods (20-30% savings)
- Consider outdoor reset for modulating systems

---

*Effective infrared radiant heating design integrates mounting geometry, thermal comfort physics, and energy effectiveness analysis to deliver efficient, comfortable heating while maximizing economic performance through proper system sizing, spacing, and control strategies.*
