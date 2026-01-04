---
title: "Energy Recovery Systems for HVAC Engineers"
description: "Sensible and enthalpy wheels, effectiveness analysis, frost control strategies, and energy savings calculations for ventilation energy recovery."
keywords: ["energy recovery", "heat recovery", "ERV", "HRV", "enthalpy wheel", "heat wheel", "energy recovery effectiveness"]
author: "Evgeniy Gantman"
date: 2026-01-04
weight: 24
---

# Energy Recovery Systems for HVAC Engineers

Energy recovery reduces ventilation loads by transferring energy between exhaust and outdoor air streams. Proper selection and sizing can reduce HVAC energy consumption by 20-40% in high-ventilation applications.

## Energy Recovery Types

### Heat Recovery Ventilator (HRV)

**Transfers:** Sensible heat only

**Applications:** Cold/dry climates (avoid over-humidification in winter)

**Effectiveness:** 60-80% sensible

### Energy Recovery Ventilator (ERV)

**Transfers:** Sensible + latent heat (total energy)

**Applications:** Hot/humid climates, high latent loads

**Effectiveness:** 60-80% total, 50-70% latent

## Technology Types

### Rotary Wheel (Air-to-Air Exchanger)

**Characteristics:**
- Rotating desiccant-coated wheel
- Transfers sensible + latent (ERV)
- High effectiveness (70-85%)
- Cross-contamination: 1-5% (purge sector reduces)

**Advantages:** Highest effectiveness, lowest pressure drop
**Disadvantages:** Moving parts, cross-contamination, requires maintenance

### Plate Heat Exchanger

**Characteristics:**
- Stationary plates separate airstreams
- Transfers sensible only (unless with permeable membrane)
- Effectiveness: 50-75%
- Zero cross-contamination

**Advantages:** No moving parts, reliable, no cross-contamination
**Disadvantages:** Lower effectiveness, higher pressure drop

### Heat Pipe

**Characteristics:**
- Refrigerant-filled pipes transfer heat
- Sensible only
- Effectiveness: 45-65%
- Zero cross-contamination

**Advantages:** Passive (no power), no moving parts
**Disadvantages:** Limited effectiveness, orientation-sensitive

### Run-Around Loop

**Characteristics:**
- Glycol loop connects coils in exhaust and supply ducts
- Allows separated air handlers
- Effectiveness: 45-65%

**Advantages:** Flexible placement, no cross-contamination
**Disadvantages:** Pump energy, glycol maintenance

## Effectiveness

**Sensible effectiveness:**

$$\epsilon_s = \frac{T_{supply,leaving} - T_{OA}}{T_{exhaust} - T_{OA}}$$

**Total effectiveness:**

$$\epsilon_t = \frac{h_{supply,leaving} - h_{OA}}{h_{exhaust} - h_{OA}}$$

## Energy Savings

**Annual heating energy recovery:**

$$Q_{recover} = 1.08 \times CFM \times \epsilon_s \times HDD \times 24$$

**Annual cooling energy recovery:**

$$Q_{recover} = 4.5 \times CFM \times \epsilon_t \times CDD \times 24$$

**Typical payback:** 3-8 years depending on climate, utility rates, ventilation rates

## Frost Control

**Problem:** When exhaust air moisture freezes on cold wheel/plates

**Occurs:** Outdoor air < 15-25°F with high indoor humidity

**Strategies:**
1. **Preheat outdoor air:** Electric or hot water coil before wheel
2. **Bypass outdoor air:** Route some OA around wheel
3. **Wheel rotation modulation:** Slow or stop rotation
4. **Exhaust air recirculation:** Reduce exhaust airflow (warms wheel)

## Pressure Drop

**Typical:**
- Rotary wheel: 0.4-0.8 "w.g. (each side)
- Plate exchanger: 0.6-1.2 "w.g.
- Heat pipe: 0.3-0.6 "w.g.

**Fan power penalty must be considered in energy analysis**

## Applications

**High-benefit applications:**
- High outdoor air rates (100% OA systems, DOAS)
- Long operating hours (24/7 facilities)
- Extreme climates (very cold winters or hot/humid summers)
- Healthcare (high ventilation codes)
- Schools (high occupant density)

**Low-benefit applications:**
- Low outdoor air rates (< 20%)
- Mild climates
- Short operating hours
- Where cross-contamination unacceptable (unless using plate/run-around)

## Practical Design

1. **Sizing:** Match outdoor air CFM to ensure balanced flows
2. **Effectiveness:** Select 65-75% for cost/performance balance
3. **Frost control:** Required in climates with winter design < 20°F
4. **Maintenance:** Plan filter access, wheel cleaning (annually)

---

**Related Technical Guides:**
- [Ventilation Rate Calculations](/technical-guides/ventilation-rate-calculations/)
- [Psychrometric Processes](/technical-guides/psychrometric-processes/)
- [Heat Transfer Fundamentals](/technical-guides/heat-transfer-fundamentals/)

**References:**
- ASHRAE Handbook of HVAC Systems and Equipment, Chapter 26: Air-to-Air Energy Recovery Equipment
- ASHRAE Standard 84: Method of Testing Air-to-Air Heat/Energy Exchangers
- AHRI Standard 1060: Performance Rating of Air-to-Air Heat Exchangers for Energy Recovery Ventilation Equipment
