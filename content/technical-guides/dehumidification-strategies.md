---
title: "Dehumidification Strategies for HVAC Engineers"
description: "Cooling-based dehumidification, desiccant systems, subcooling coils, and humidity control sequences for maintaining comfort and IAQ."
keywords: ["dehumidification", "desiccant", "subcooling", "humidity control", "latent cooling", "moisture removal"]
author: "Evgeniy Gantman"
date: 2026-01-04
weight: 18
---

# Dehumidification Strategies for HVAC Engineers

Humidity control affects comfort, indoor air quality, and mold prevention. Different strategies suit different applications based on latent load magnitude, cost constraints, and control precision requirements.

## Cooling-Based Dehumidification

**Principle:** Cool air below dew point to condense moisture

**Sensible Heat Ratio (SHR):**

$$SHR = \frac{q_{sensible}}{q_{total}}$$

**Dehumidification capability:**
- High SHR (0.85-1.0): Poor dehumidification
- Medium SHR (0.70-0.85): Adequate for most spaces
- Low SHR (0.50-0.70): Good dehumidification (kitchens, pools)

**Coil design for dehumidification:**
- Lower air velocity (300-400 FPM) improves contact time
- More rows (6-8 rows better than 4)
- Lower leaving air temperature (52-54°F)

**Limitations:** Energy penalty for overcooling then reheating

## Subcooling with Reheat

**Process:**
1. Overcool to remove moisture
2. Reheat to desired supply temperature

**Energy penalty:** Inefficient (cooling then heating same air)

**Applications:** Critical humidity control (hospitals, museums, data centers)

**Reheat sources:**
- Hot water coil
- Electric resistance
- Heat recovery (most efficient)
- Hot gas reheat (uses compressor discharge)

## Desiccant Dehumidification

**Principle:** Chemical absorption of moisture

**Types:**
1. **Solid desiccant wheel:** Rotating wheel coated with silica gel or molecular sieve
2. **Liquid desiccant:** Spray lithium chloride solution

**Process:**
- **Process air:** Desiccant absorbs moisture (also heats air due to adsorption heat)
- **Regeneration air:** Heated air drives moisture off desiccant

**Advantages:**
- Handles high latent loads
- No overcooling needed
- Low dew points achievable (< 40°F)

**Disadvantages:**
- High energy for regeneration
- Adds sensible heat to space
- Requires heat source

**Applications:** Indoor pools, ice rinks, pharmaceutical manufacturing

## Dedicated Outdoor Air Systems (DOAS)

**Strategy:** Separate outdoor air conditioning from space conditioning

**Benefits:**
- Optimized for latent load (outdoor air typically high humidity)
- Space systems handle sensible only
- Prevents overcooling of spaces

**Typical DOAS:**
- Deep cooling coil (45-50°F leaving)
- Heat recovery
- Optional desiccant
- Neutral supply temperature (65-75°F after reheat)

## Humidity Control Sequences

**Two-stage dehumidification:**
1. Stage 1: Normal cooling
2. Stage 2 (if RH > 55%): Enable dehumidification mode
   - Lower supply air temperature
   - Activate reheat
   - Reduce airflow (lower SHR)

**Variable speed compressor:**
- Slow compressor at light loads
- Lower evaporator temperature
- Better moisture removal

## Practical Applications

1. **Humid climates:** Design for SHR 0.70-0.75, consider DOAS
2. **Natatoriums:** Desiccant + pool cover (50-60% RH target)
3. **Museums:** Tight control (±5% RH): subcooling + reheat
4. **Warehouses:** Desiccant for product protection

---

**Related Technical Guides:**
- [Psychrometric Processes](/technical-guides/psychrometric-processes/)
- [Cooling Load Calculations](/technical-guides/cooling-load-calculations/)
- [Air Conditioning System Selection](/technical-guides/air-conditioning-system-selection/)

**References:**
- ASHRAE Handbook of HVAC Systems and Equipment, Chapter 24: Desiccant Dehumidification and Pressure Drying Equipment
- ASHRAE Standard 62.1: Ventilation for Acceptable Indoor Air Quality
