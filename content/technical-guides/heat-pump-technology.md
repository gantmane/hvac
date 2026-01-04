---
title: "Heat Pump Technology for HVAC Engineers"
description: "Air-source and ground-source heat pumps, COP and HSPF metrics, balance point analysis, and supplemental heating requirements for efficient space conditioning."
keywords: ["heat pump", "COP", "HSPF", "geothermal heat pump", "air source heat pump", "balance point", "supplemental heat"]
author: "Evgeniy Gantman"
date: 2026-01-04
weight: 9
---

# Heat Pump Technology for HVAC Engineers

Heat pumps transfer heat from cold sources to warm spaces, providing heating with COP of 2.5-4.5 (250-450% efficiency). Understanding performance degradation at low temperatures enables proper sizing and supplemental heat integration.

## Heat Pump Types

### Air-Source Heat Pumps (ASHP)

Extract heat from outdoor air.

**Advantages:**
- Lower first cost
- Easy installation
- No ground loop required

**Disadvantages:**
- Capacity degrades at low outdoor temperatures
- Requires defrost cycle
- COP drops significantly below 32°F

### Ground-Source Heat Pumps (GSHP)

Extract heat from ground via buried loops.

**Advantages:**
- Stable ground temperature (50-60°F year-round)
- Higher COP (3.0-5.0)
- No defrost cycle
- Longer life (25+ years)

**Disadvantages:**
- High first cost ($6,000-$12,000/ton installed)
- Requires land area or deep bores
- Complex ground loop design

## Performance Metrics

**Heating COP:**

$$COP_h = \frac{Q_h}{W_{comp}} = \frac{h_2 - h_3}{h_2 - h_1}$$

**Cooling EER:**

$$EER = \frac{Q_c \text{ (Btu/h)}}{W_{comp} \text{ (W)}}$$

**HSPF** (Heating Seasonal Performance Factor):
Seasonal heating efficiency including defrost and cycling losses.

$$HSPF = \frac{\sum Q_h}{\sum W_{total}}$$

Units: Btu/W·h (higher is better)

**Minimum standards:**
- Federal minimum: HSPF 8.2 (Northern), 8.8 (Southern)
- ENERGY STAR: HSPF 9.0+

## Balance Point Analysis

Balance point: outdoor temperature where heat pump capacity equals building heat loss.

$$T_{balance} = T_{indoor} - \frac{Q_{design}}{UA_{building}}$$

**Below balance point:** Supplemental heat required

**Sizing strategies:**
1. **Size for balance point:** No supplemental heat above balance point (common for ASHP)
2. **Size for full load:** Heat pump handles entire load (expensive for ASHP, typical for GSHP)
3. **Dual fuel:** Switch to gas furnace below economic balance point

## Defrost Control

**Frost formation:** When evaporator coil < 32°F and humid outdoor air

**Defrost methods:**
- **Reverse cycle:** Switches to cooling mode, hot gas melts frost (most common)
- **Hot gas bypass:** Diverts compressor discharge to outdoor coil
- **Electric resistance:** Heats outdoor coil (inefficient)

**Defrost initiation:**
- Time-temperature: Every 30-90 min if coil < 32°F
- Demand: Pressure differential or coil temperature triggers

**Energy penalty:** 5-15% capacity loss during heating season

## Practical Applications

1. **Cold climates:** Consider GSHP or dual-fuel ASHP
2. **Moderate climates:** ASHP cost-effective
3. **Cooling-dominant:** Heat pump ideal (high cooling efficiency)

---

**Related Technical Guides:**
- [Thermodynamic Cycles](/technical-guides/thermodynamic-cycles/)
- [Heating Load Calculations](/technical-guides/heating-load-calculations/)
- [Refrigeration Cycle Design](/technical-guides/refrigeration-cycle-design/)

**References:**
- ASHRAE Handbook of HVAC Systems and Equipment, Chapter 9: Air-Source Heat Pumps
- IGSHPA Design and Installation Standards
