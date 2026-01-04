---
title: "Variable Flow System Design for HVAC Engineers"
description: "VFD sizing, minimum flow requirements, pressure-independent control, diversity factors, and energy optimization for variable flow HVAC systems."
keywords: ["variable flow", "VFD", "VAV systems", "diversity factor", "pressure independent", "variable speed drives"]
author: "Evgeniy Gantman"
date: 2026-01-04
weight: 26
---

# Variable Flow System Design for HVAC Engineers

Variable flow systems modulate airflow or water flow to match actual loads, reducing fan and pump energy by 30-60% compared to constant-volume systems. Proper design requires understanding minimum flow limits, diversity factors, and control strategies.

## Fan Energy Savings

**Fan affinity laws:**

$$\frac{CFM_2}{CFM_1} = \frac{RPM_2}{RPM_1}$$

$$\frac{Power_2}{Power_1} = \left(\frac{RPM_2}{RPM_1}\right)^3$$

**At 50% airflow:**

$$Power_{50\%} = 0.5^3 = 0.125 = 12.5\%$$ of full power

**Energy savings:** 87.5% reduction at half flow

<div class="worked-example">
<h3>Worked Example 1: VAV Energy Savings</h3>

**Given:**
- Design airflow: 20,000 CFM
- Full-load fan power: 15 hp
- Average operating airflow: 60% of design
- Operating hours: 4,000 hours/year
- Electricity cost: $0.12/kWh

**Find:** Annual energy savings vs. constant volume

**Solution:**

Variable speed power at 60% flow:

$$Power_{60\%} = 15 \times 0.6^3 = 15 \times 0.216 = 3.24 \text{ hp}$$

Energy savings per hour:

$$\Delta E = (15 - 3.24) \times 0.746 = 8.76 \text{ kW}$$

Annual savings:

$$Savings = 8.76 \times 4000 \times 0.12 = \$4,205$$

**Answer:** $4,205/year energy savings (76% reduction)
</div>

## VAV System Design

### Minimum Airflow

**Reasons for minimum flow:**
1. Meet ventilation requirements (ASHRAE 62.1)
2. Maintain air circulation
3. Prevent stratification
4. Ensure diffuser performance

**Typical minimum:** 30-50% of design airflow

**Calculation:**

$$CFM_{min} = \max\left(CFM_{ventilation}, 0.3 \times CFM_{design}\right)$$

### Diversity Factor

**Not all zones at peak load simultaneously**

**System diversity:**

$$Diversity = \frac{\sum CFM_{design,zones}}{CFM_{AHU,actual}}$$

**Typical values:**
- Office buildings: 1.2-1.4
- Schools: 1.1-1.3
- Hospitals: 1.0-1.1 (less diversity)

**Impact:** Allows smaller AHU and ductwork sizing

### Static Pressure Control

**Setpoint location:** 2/3 distance from fan to furthest terminal

**Control strategy:**

$$SP_{setpoint} = SP_{design} \times \left(\frac{CFM_{actual}}{CFM_{design}}\right)^2$$

**Static pressure reset:**
- Monitors all VAV damper positions
- If all dampers < 90% open, reduce static pressure setpoint
- Saves fan energy without sacrificing control

```mermaid
graph TD
    A[Measure all VAV damper positions] --> B{Any damper > 90% open?}
    B -->|Yes| C[Increase SP setpoint by 0.1 \"w.g.]
    B -->|No| D{All dampers < 50% open?}
    D -->|Yes| E[Decrease SP setpoint by 0.1 \"w.g.]
    D -->|No| F[Maintain current SP setpoint]
    C --> G[Limit: SP_min to SP_max]
    E --> G
    F --> G
    G --> H[Modulate fan speed to maintain SP]
```

## Pressure-Independent VAV Terminals

**Advantages:**
- Maintains design airflow regardless of duct pressure variations
- Simplified balancing
- Better control stability

**Components:**
- Airflow sensor (pressure grid or hot-wire anemometer)
- Controller with airflow setpoint
- Modulating damper with actuator

**Control:**

$$Damper\% = f\left(CFM_{setpoint} - CFM_{measured}\right)$$

## Variable Primary Flow Chilled Water

**Replaces constant primary / variable secondary** with single variable loop

**Benefits:**
- Eliminates primary pumps
- Reduces piping complexity
- Lower first cost and energy

**Requirements:**
1. **Minimum flow through chillers:** Use bypass valve or 3-way valve
2. **Chiller isolation:** Two-way valves at each chiller
3. **Differential pressure control:** Maintain 15-20 psi across system

**Minimum flow calculation:**

$$GPM_{min,chiller} = 2-3 \text{ ft/s} \times A_{evaporator}$$

Typically 30-50% of design flow

## Pump Energy Savings

**Pump affinity laws:**

$$\frac{GPM_2}{GPM_1} = \frac{RPM_2}{RPM_1}$$

$$\frac{Head_2}{Head_1} = \left(\frac{RPM_2}{RPM_1}\right)^2$$

$$\frac{Power_2}{Power_1} = \left(\frac{RPM_2}{RPM_1}\right)^3$$

**Variable vs. constant speed:**

<div class="worked-example">
<h3>Worked Example 2: Pump Energy at Part Load</h3>

**Given:**
- Design flow: 500 GPM at 60 ft head
- Part-load flow: 250 GPM (50%)
- Pump efficiency: 75%

**Find:** Power savings with VFD vs. throttling valve

**Solution:**

**Constant speed with throttle valve:**

Power unchanged (still pumping against 60 ft head)

$$Power_{constant} = \frac{500 \times 60}{3960 \times 0.75} = 10.1 \text{ hp}$$

**Variable speed:**

Speed ratio: 50%

Head at 50% flow:

$$Head_{50\%} = 60 \times 0.5^2 = 15 \text{ ft}$$

$$Power_{variable} = \frac{250 \times 15}{3960 \times 0.75} = 1.26 \text{ hp}$$

**Savings:** $(10.1 - 1.26) / 10.1 = 87.5\%$

**Answer:** 87.5% energy savings with VFD at 50% flow
</div>

## VFD Sizing and Selection

**VFD must match motor:**
- Voltage (230V, 460V, etc.)
- Current (nameplate FLA)
- Horsepower rating

**Typical efficiency:**
- 95-97% at full load
- 92-95% at 50% load

**Harmonics mitigation:**
- Use line reactors (3-5% impedance)
- Or passive harmonic filters

## Practical Design Considerations

1. **Duct design:** Size for actual diversity, not sum of peaks
2. **Minimum flow:** Verify ventilation requirements at all loads
3. **Bypass dampers:** Avoid—waste energy
4. **Pressure sensors:** Place at representative location (2/3 point)
5. **Commissioning:** Verify minimum flow, diversity factors, reset strategies

---

**Related Technical Guides:**
- [HVAC Control Strategies](/technical-guides/hvac-control-strategies/)
- [Fan Selection & Performance](/technical-guides/fan-selection-performance/)
- [Duct Static Pressure Calculations](/technical-guides/duct-static-pressure-calculations/)

**References:**
- ASHRAE Handbook of HVAC Systems and Equipment, Chapter 48: Variable-Flow Systems
- ASHRAE Guideline 36: High-Performance Sequences of Operation for HVAC Systems
- Taylor Engineering: "Optimizing Design & Control of Chilled Water Plants"
