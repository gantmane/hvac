---
title: "Radiant Heating Design for HVAC Engineers"
description: "Floor, wall, and ceiling radiant systems with panel output calculations, tube spacing methods, and manifold design for comfort and efficiency."
keywords: ["radiant heating", "radiant floor", "hydronic radiant", "radiant panel", "floor heating design", "tube spacing"]
author: "Evgeniy Gantman"
date: 2026-01-04
weight: 10
---

# Radiant Heating Design for HVAC Engineers

Radiant heating delivers comfort via infrared radiation and minimal air movement. Proper design ensures uniform temperatures, adequate capacity, and system responsiveness while preventing floor surface overheating.

## Radiant Panel Output

**Heat flux from radiant panel:**

$$q = C \times (T_s - T_r)^n$$

Where:
- $q$ = heat flux (Btu/(h·ft²))
- $C$ = empirical constant
- $T_s$ = surface temperature (°F)
- $T_r$ = room temperature (°F)
- $n$ = 1.0 to 1.3 (depending on system type)

**Floor panel output:** 15-30 Btu/(h·ft²) typical

**Limitations:**
- Floor surface: < 85°F (comfort limit for occupied areas)
- Ceiling surface: < 120°F (prevents discomfort from overhead radiation)

## Tube Spacing Design

**Heat transfer per unit length:**

$$q' = \frac{k_{effective} \times W \times (T_{avg} - T_{floor,bottom})}{thickness}$$

Where:
- $k_{effective}$ = effective thermal conductivity including tube influence
- $W$ = panel width per tube
- Spacing: typically 6-12 inches

**Serpentine vs. Counterflow:**
- **Serpentine:** Simple, temperature gradient along length
- **Counterflow:** More uniform, requires more circuits

## System Design Procedure

1. Calculate room heat loss
2. Determine available floor area (exclude furniture)
3. Select supply water temperature (typically 95-120°F)
4. Calculate required surface temperature
5. Size tube spacing and circuit length
6. Design manifold and controls

## Water Temperature and Flow

**Supply temperature:** 95-140°F (lower for floor, higher for ceiling)

**Temperature drop:** 10-20°F per circuit

**Flow rate per circuit:**

$$GPM = \frac{q}{500 \times \Delta T}$$

**Circuit length:** Maximum 300-400 ft (pressure drop limit)

## Practical Applications

1. **Slab-on-grade:** Tubes in concrete slab (high thermal mass, slow response)
2. **Suspended floor:** Tubes in subfloor or joist space (faster response)
3. **Ceiling panels:** Higher temperatures, faster response
4. **Snowmelt:** Driveway/walkway heating (higher capacity, 150-250 Btu/(h·ft²))

---

**Related Technical Guides:**
- [Heat Transfer Fundamentals](/technical-guides/heat-transfer-fundamentals/)
- [Hydronic System Fundamentals](/technical-guides/hydronic-system-fundamentals/)
- [Heating Load Calculations](/technical-guides/heating-load-calculations/)

**References:**
- ASHRAE Handbook of HVAC Systems and Equipment, Chapter 6: Radiant Heating and Cooling
- Radiant Professionals Alliance Design Guidelines
