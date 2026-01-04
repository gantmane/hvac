---
title: "Heating Load Calculations for HVAC Engineers"
description: "Heat loss methodology, envelope analysis, infiltration calculations, and degree-day methods per ASHRAE Handbook for accurate heating system sizing."
keywords: ["heating load", "heat loss calculation", "infiltration", "transmission losses", "degree days", "Manual J"]
author: "Evgeniy Gantman"
date: 2026-01-04
weight: 12
---

# Heating Load Calculations for HVAC Engineers

Accurate heating load calculations prevent undersizing (inadequate comfort) and oversizing (cycling, inefficiency). This guide presents ASHRAE methodology for residential and commercial heating load determination.

## Heat Loss Components

$$Q_{total} = Q_{transmission} + Q_{infiltration} + Q_{ventilation}$$

## Transmission Heat Loss

**Through envelope:**

$$Q = U \times A \times (T_{in} - T_{out})$$

Where:
- $U$ = overall heat transfer coefficient (Btu/(h·ft²·°F))
- $A$ = surface area (ft²)
- $T_{in}$ = indoor design temperature (typically 68-72°F)
- $T_{out}$ = outdoor 99% or 99.6% design temperature

**Below-grade losses:**
- Basement walls: Use F-factor method
- Slab-on-grade: Use F-factor or C-factor

## Infiltration Heat Loss

**Air change method:**

$$Q_{inf} = 0.018 \times V \times ACH \times (T_{in} - T_{out})$$

Where:
- $V$ = building volume (ft³)
- $ACH$ = air changes per hour

**CFM method:**

$$Q_{inf} = 1.08 \times CFM \times \Delta T$$

**Typical ACH values:**
- Tight construction (ICF, SIPs): 0.15-0.25 ACH
- Average construction: 0.35-0.50 ACH
- Loose construction: 0.60-1.00 ACH

## Design Temperatures

**Indoor:** 68-72°F heating

**Outdoor (ASHRAE 99.6%):**
- Chicago, IL: -7°F
- Denver, CO: -2°F
- Atlanta, GA: 17°F
- Phoenix, AZ: 34°F

## Degree Days

**Heating degree days (base 65°F):**

$$HDD = \sum (65 - T_{avg,daily})$$ for days when $T_{avg} < 65$°F

**Annual energy:**

$$Energy = \frac{24 \times HDD \times UA_{building}}{\eta_{equipment}}$$

## Practical Applications

1. **Residential:** Use Manual J (ACCA)
2. **Commercial:** Room-by-room or block load
3. **Safety factor:** Design equipment capacity, do NOT add to calculated load

---

**Related Technical Guides:**
- [Heat Transfer Fundamentals](/technical-guides/heat-transfer-fundamentals/)
- [Load Calculation Methodology](/technical-guides/load-calculation-methodology/)
- [Boiler Selection & Sizing](/technical-guides/boiler-selection-sizing/)

**References:**
- ASHRAE Handbook of Fundamentals, Chapter 18: Residential Cooling and Heating Load Calculations
- ACCA Manual J, 8th Edition
