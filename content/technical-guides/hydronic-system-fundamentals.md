---
title: "Hydronic System Fundamentals for HVAC Engineers"
description: "Primary-secondary pumping, variable flow systems, differential pressure control, and hydraulic separation principles for chilled and hot water distribution."
keywords: ["hydronic systems", "primary-secondary pumping", "variable flow", "chilled water", "hot water", "differential pressure control"]
author: "Evgeniy Gantman"
date: 2026-01-04
weight: 7
---

# Hydronic System Fundamentals for HVAC Engineers

Hydronic systems distribute thermal energy via water circulation. Proper hydraulic design ensures adequate flow to all loads while minimizing pump energy and maintaining control stability.

## System Configurations

### Primary-Secondary Pumping

Decouples production (chillers/boilers) from distribution (building loads).

**Components:**
- **Primary loop:** Constant flow through production equipment
- **Secondary loop:** Variable flow to building loads
- **Common pipe:** Hydraulic separator (low pressure drop connection)

**Benefits:**
- Chillers/boilers see constant flow (manufacturer requirement)
- Variable speed secondary pumps save energy
- Easy to add/remove production equipment

### Variable Primary Flow

Eliminates secondary pumps; single variable speed pumps serve both production and distribution.

**Requirements:**
- Minimum flow through chiller (typically 30-50% of design)
- Bypass valve or dedicated minimum flow loop
- Advanced controls to prevent low flow

**Benefits:** Eliminates secondary pumps, reduces complexity, lower first cost

## Pump Sizing

**Flow rate:**

$$GPM = \frac{Q}{500 \times \Delta T}$$

Where:
- $Q$ = heat transfer rate (Btu/h or tons × 12,000)
- $\Delta T$ = temperature difference (typically 10-20°F for chilled water, 20-40°F for hot water)
- 500 = constant for water (8.33 lb/gal × 60 min/h × 1.0 Btu/(lb·°F))

**Head requirement:**

$$H_{total} = H_{static} + H_{friction} + H_{equipment} + H_{control}$$

**Pump power:**

$$hp = \frac{GPM \times H_{ft}}{3,960 \times \eta}$$

## Differential Pressure Control

Maintains system $\Delta P$ at remote sensor location.

**Control strategies:**
- **Fixed $\Delta P$:** Simple but energy waste at part load
- **Reset $\Delta P$:** Reduces setpoint as valves open (saves 20-40% pump energy)

## Practical Applications

1. **Chilled water:** 10-12°F $\Delta T$, 40-45°F supply
2. **Hot water:** 20-40°F $\Delta T$, 140-180°F supply  
3. **Condenser water:** 10°F $\Delta T$, 85°F design leaving

---

**Related Technical Guides:**
- [Fluid Mechanics for HVAC](/technical-guides/fluid-mechanics-hvac/)
- [Pump Selection & Performance](/technical-guides/pump-selection-performance/)
- [Variable Flow Control Design](/technical-guides/variable-flow-system-design/)

**References:**
- ASHRAE Handbook of HVAC Systems and Equipment, Chapter 13: Hydronic Heating and Cooling System Design
- ASHRAE Design Guide: Variable Primary Flow Chilled Water Systems
