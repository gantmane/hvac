---
title: "Chiller Performance Analysis for HVAC Engineers"
description: "Efficiency metrics (kW/ton, COP, IPLV), part-load performance, condenser water optimization, and free cooling integration for chilled water systems."
keywords: ["chiller efficiency", "kW per ton", "IPLV", "chiller COP", "condenser water", "free cooling", "chiller performance"]
author: "Evgeniy Gantman"
date: 2026-01-04
weight: 14
---

# Chiller Performance Analysis for HVAC Engineers

Chiller efficiency determines 40-60% of total HVAC energy consumption. Understanding performance metrics and optimization strategies enables equipment selection and operation for minimum life cycle cost.

## Efficiency Metrics

**kW/ton:**

$$kW/ton = \frac{Compressor\ kW}{Tons\ Cooling}$$

Lower is better. Typical values:
- Air-cooled chiller: 0.9-1.2 kW/ton
- Water-cooled centrifugal: 0.50-0.65 kW/ton
- Magnetic bearing centrifugal: 0.45-0.55 kW/ton

**COP (Coefficient of Performance):**

$$COP = \frac{12,000 \times Tons}{3,413 \times kW} = \frac{12}{3.413 \times kW/ton} = \frac{3.516}{kW/ton}$$

Higher is better. Typical: COP 4.0-6.5

**EER (Energy Efficiency Ratio):**

$$EER = \frac{Cooling\ Capacity\ (Btu/h)}{Power\ Input\ (Watts)} = 12 \times COP$$

## Part-Load Performance

**Integrated Part Load Value (IPLV):**

Weighted efficiency at four load points:
- 100% load: 1% weight
- 75% load: 42% weight
- 50% load: 45% weight
- 25% load: 12% weight

$$IPLV = 0.01A + 0.42B + 0.45C + 0.12D$$

Where A, B, C, D are kW/ton at respective load points.

**Significance:** Chillers rarely operate at full load; IPLV better predicts annual energy.

## Temperature Lift Effect

Chiller efficiency degrades with increased temperature lift:

$$Lift = T_{leaving,cond} - T_{leaving,evap}$$

**Every 1°F lift increase:** ~0.015-0.025 kW/ton efficiency penalty

**Optimization strategies:**
1. Lower chilled water temperature only when needed (reset based on load)
2. Maximize condenser water temperature in winter (free cooling)
3. Keep condenser clean (fouling increases lift)

## Condenser Water Optimization

**Cooling tower approach:**

$$Approach = T_{leaving,tower} - T_{wetbulb,outdoor}$$

**Tower range:**

$$Range = T_{entering,tower} - T_{leaving,tower}$$

Typical: 10°F range, 7-10°F approach

**Energy tradeoff:**
- Lower condenser water temp: Better chiller efficiency, more tower fan power
- Optimal condenser water temp: 65-75°F (varies by climate, equipment)

## Free Cooling

**Waterside economizer:** Uses cooling tower to cool chilled water directly (bypasses chiller)

**Conditions:** Outdoor wet bulb < 45-50°F

**Energy savings:** 50-90% when active (winter months in most climates)

## Practical Applications

1. **Equipment selection:** Specify IPLV > 15.0 EER for ASHRAE 90.1 compliance
2. **Sequencing:** Load most efficient chiller first at part load
3. **Condenser water reset:** Raise leaving temperature in cool weather
4. **Chilled water reset:** Raise leaving temperature when loads decrease

---

**Related Technical Guides:**
- [Thermodynamic Cycles](/technical-guides/thermodynamic-cycles/)
- [Cooling Tower Performance](/technical-guides/cooling-tower-performance/)
- [Variable Flow System Design](/technical-guides/variable-flow-system-design/)

**References:**
- ASHRAE Handbook of HVAC Systems and Equipment, Chapter 38: Compressors
- ASHRAE Handbook of HVAC Systems and Equipment, Chapter 43: Liquid Chillers
- AHRI Standard 550/590: Performance Rating of Water-Chilling and Heat Pump Water-Heating Packages
