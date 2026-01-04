---
title: "Fan Selection & Performance for HVAC Engineers"
description: "Fan laws, system curves, operating point determination, and variable speed drive application for energy optimization and proper fan sizing."
keywords: ["fan selection", "fan laws", "system curve", "fan performance", "VFD", "fan efficiency"]
author: "Evgeniy Gantman"
date: 2026-01-04
weight: 22
---

# Fan Selection & Performance for HVAC Engineers

Proper fan selection matches airflow and pressure requirements at maximum efficiency. Understanding fan laws and system curves enables VFD sizing and troubleshooting.

## Fan Laws

**At constant speed and size:**

Law 1 (Flow proportional to speed):

$$\frac{CFM_2}{CFM_1} = \frac{RPM_2}{RPM_1}$$

Law 2 (Pressure proportional to speed squared):

$$\frac{SP_2}{SP_1} = \left(\frac{RPM_2}{RPM_1}\right)^2$$

Law 3 (Power proportional to speed cubed):

$$\frac{hp_2}{hp_1} = \left(\frac{RPM_2}{RPM_1}\right)^3$$

**Significance:** Reducing speed by 20% cuts power by 49%

## Fan Types

### Centrifugal Fans

**Forward-curved (FC):**
- Efficiency: 50-65%
- Applications: Residential furnaces, low-pressure
- Characteristics: Compact, low cost, overloading power curve

**Backward-inclined (BI):**
- Efficiency: 70-80%
- Applications: Commercial AHUs, return fans
- Characteristics: Non-overloading power curve, efficient

**Airfoil:**
- Efficiency: 80-85%
- Applications: Large systems, energy-critical
- Characteristics: Highest efficiency, most expensive

### Axial Fans

**Propeller:**
- Efficiency: 40-60%
- Applications: Exhaust fans, cooling towers
- Characteristics: High flow, low pressure

**Tube-axial:**
- Efficiency: 55-70%
- Applications: Duct-mounted exhaust

**Vane-axial:**
- Efficiency: 70-85%
- Applications: High-capacity, moderate pressure

## System Curve

**Parabolic relationship:**

$$SP = K \times CFM^2$$

Where $K$ depends on duct system resistance

**Operating point:** Intersection of fan curve and system curve

## Fan Sizing

**Total Pressure Rise:**

$$TP = SP_{discharge} - SP_{suction} + P_{v,discharge}$$

**Power:**

$$hp = \frac{CFM \times TP}{6,356 \times \eta_{total}}$$

Where $\eta_{total}$ includes fan, drive, and motor efficiencies

**Safety factor:** 10-15% on pressure (do NOT apply to flow)

## Variable Frequency Drives (VFDs)

**Energy savings at 60% speed:**

$$Power_{60\%} = 0.6^3 = 0.216 = 21.6\%$$ of full speed power

**Savings = 78% power reduction**

**Applications:**
- VAV systems (modulate fan to maintain duct static pressure)
- CO₂-based demand control ventilation
- Seasonal airflow variation

**VFD efficiency:** 95-97% at full load, 92-95% at 50% load

## Practical Applications

1. **System design:** Select fan at 85-95% of peak efficiency
2. **VFD control:** Maintain duct static pressure at 2/3 point from fan
3. **Troubleshooting:** If airflow low, check speed, dampers, filters

---

**Related Technical Guides:**
- [Fluid Mechanics for HVAC](/technical-guides/fluid-mechanics-hvac/)
- [Duct Static Pressure Calculations](/technical-guides/duct-static-pressure-calculations/)
- [Variable Flow System Design](/technical-guides/variable-flow-system-design/)

**References:**
- ASHRAE Handbook of HVAC Systems and Equipment, Chapter 21: Fans
- AMCA Publication 201: Fans and Systems
- Air Movement and Control Association (AMCA) Standards
