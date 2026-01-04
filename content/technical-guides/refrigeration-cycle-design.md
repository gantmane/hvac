---
title: "Refrigeration Cycle Design for HVAC Engineers"
description: "Compressor selection, evaporator and condenser sizing, superheat and subcooling control, and capacity modulation strategies for refrigeration systems."
keywords: ["refrigeration cycle", "compressor selection", "superheat", "subcooling", "evaporator sizing", "condenser sizing"]
author: "Evgeniy Gantman"
date: 2026-01-04
weight: 15
---

# Refrigeration Cycle Design for HVAC Engineers

Refrigeration system design balances capacity, efficiency, and reliability. Proper component sizing and control ensures optimal performance across varying load and ambient conditions.

## Vapor Compression Cycle Components

1. **Evaporator:** Absorbs heat, evaporates liquid refrigerant
2. **Compressor:** Increases pressure and temperature
3. **Condenser:** Rejects heat, condenses vapor to liquid
4. **Expansion device:** Reduces pressure, controls flow

## Compressor Selection

**Types:**
- **Reciprocating:** 1-100 tons, high efficiency, good part-load
- **Scroll:** 2-60 tons, quiet, reliable
- **Screw:** 20-500 tons, good part-load, industrial
- **Centrifugal:** 100-10,000 tons, highest efficiency at full load

**Displacement:**

$$V_{displacement} = \frac{Capacity \times v_1}{\eta_v}$$

Where:
- $v_1$ = specific volume at compressor suction (ft³/lb)
- $\eta_v$ = volumetric efficiency (0.65-0.85)

## Superheat Control

**Superheat:** Temperature above saturation at evaporator outlet

$$SH = T_{suction} - T_{sat,evap}$$

**Target:** 10-15°F

**Too low:** Liquid slugging risk, compressor damage
**Too high:** Reduced capacity, higher discharge temperature

**Control:** Thermostatic expansion valve (TXV) or electronic expansion valve (EEV)

## Subcooling

**Subcooling:** Temperature below saturation at condenser outlet

$$SC = T_{sat,cond} - T_{liquid}$$

**Target:** 10-20°F

**Benefits:**
- Prevents flash gas in liquid line
- Increases capacity (~0.5% per °F)
- Improves efficiency

## Evaporator Sizing

**Heat transfer:**

$$Q = UA_{evap} \times LMTD$$

**Log mean temperature difference:**

$$LMTD = \frac{(T_{in} - T_{evap}) - (T_{out} - T_{evap})}{\ln\frac{T_{in} - T_{evap}}{T_{out} - T_{evap}}}$$

**Typical approach:** 8-15°F (difference between evaporating temperature and leaving chilled water)

## Condenser Sizing

Similar to evaporator:

$$Q_{cond} = Q_{evap} + W_{comp}$$

**Approach:** 10-15°F (condensing temperature above entering condenser water)

## Capacity Modulation

**Methods:**
1. **On-off:** Simple, cycling losses
2. **Cylinder unloading:** 25/50/75/100% steps
3. **Variable speed:** Continuous modulation, highest efficiency
4. **Hot gas bypass:** Inefficient, use only for critical control

## Practical Applications

1. **R-410A residential AC:** 13-21 SEER
2. **R-134a chiller:** 0.50-0.65 kW/ton
3. **Ammonia industrial:** Highest efficiency, toxic
4. **CO₂ transcritical:** Low GWP, high pressure

---

**Related Technical Guides:**
- [Thermodynamic Cycles](/technical-guides/thermodynamic-cycles/)
- [Chiller Performance Analysis](/technical-guides/chiller-performance-analysis/)
- [Heat Transfer Fundamentals](/technical-guides/heat-transfer-fundamentals/)

**References:**
- ASHRAE Handbook of HVAC Systems and Equipment, Chapter 38: Compressors
- ASHRAE Handbook of Fundamentals, Chapter 30: Thermophysical Properties of Refrigerants
