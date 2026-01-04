---
title: "Cooling Tower Performance for HVAC Engineers"  
description: "Approach, range, and effectiveness calculations, fan and pump power optimization, and water treatment considerations for evaporative cooling systems."
keywords: ["cooling tower", "approach temperature", "range", "tower effectiveness", "evaporative cooling", "tower performance"]
author: "Evgeniy Gantman"
date: 2026-01-04
weight: 16
---

# Cooling Tower Performance for HVAC Engineers

Cooling towers reject heat via evaporative cooling. Performance depends on ambient wet bulb temperature, water flow, and airflow. Proper sizing and control optimize chiller efficiency and minimize water/energy consumption.

## Performance Parameters

**Range:**

$$Range = T_{in} - T_{out}$$

Typically 10°F for HVAC applications

**Approach:**

$$Approach = T_{out} - T_{wb}$$

Typically 7-10°F (lower approach requires larger/more expensive tower)

**Effectiveness:**

$$\epsilon = \frac{Range}{Range + Approach} = \frac{T_{in} - T_{out}}{T_{in} - T_{wb}}$$

Typical: 0.65-0.75

## Heat Rejection

$$Q = \dot{m}_{water} \times c_p \times Range$$

$$Q = GPM \times 500 \times \Delta T$$

Where 500 = 8.33 lb/gal × 60 min/h × 1.0 Btu/(lb·°F)

**Water evaporation rate:**

$$GPM_{evap} = \frac{Q}{8.33 \times 1,000}$$

Approximately 0.3% of water circulation rate per °F range

## Fan Power

**Mechanical draft towers:**

$$hp_{fan} = \frac{CFM_{air} \times \Delta P_{tower}}{6,356 \times \eta}$$

**Energy tradeoff:**
- More airflow: Lower leaving water temp, better chiller efficiency
- Less airflow: Lower fan power, higher leaving water temp

**Optimal:** Balance chiller and tower fan energy (typically leaving water temp 70-80°F)

## Water Treatment

**Makeup water:**

$$GPM_{makeup} = GPM_{evap} + GPM_{blowdown} + GPM_{drift}$$

**Cycles of concentration:**

$$COC = \frac{TDS_{circulating}}{TDS_{makeup}}$$

Higher COC reduces water consumption but requires better treatment

**Typical COC:** 3-6 (limited by scaling, corrosion, biological growth)

## Practical Applications

1. **Chiller condenser:** 85°F entering, 95°F leaving, 78°F wet bulb design
2. **Free cooling:** Tower alone when wet bulb < 45-50°F
3. **VFD fans:** Modulate to maintain leaving water setpoint

---

**Related Technical Guides:**
- [Chiller Performance Analysis](/technical-guides/chiller-performance-analysis/)
- [Psychrometric Processes](/technical-guides/psychrometric-processes/)
- [Variable Flow System Design](/technical-guides/variable-flow-system-design/)

**References:**
- ASHRAE Handbook of HVAC Systems and Equipment, Chapter 40: Cooling Towers
- CTI Code Tower STD-201: Standard for Certification of Water Cooling Towers
