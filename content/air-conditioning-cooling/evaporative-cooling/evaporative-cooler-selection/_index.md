---
title: "Evaporative Cooler Selection"
aliases: ["Evaporative Cooler Selection"]
description: "Guidelines for selecting evaporative cooling equipment including system sizing, type selection, and performance verification methods."
keywords: ["evaporative cooler selection", "sizing", "equipment selection", "cooling capacity", "HVAC design", "swamp cooler"]
tags: ["evaporative cooler selection", "sizing", "equipment selection", "cooling capacity", "HVAC design", "swamp cooler"]
weight: 4
---

Proper evaporative cooler selection ensures systems deliver required cooling capacity efficiently across expected operating conditions. This guide covers system sizing, equipment type selection, and performance verification for successful installations.

## Climate Analysis

### Wet-Bulb Frequency Analysis

Before selecting evaporative cooling, analyze local climate data:

**Bin Data Analysis**:
- Compile hourly wet-bulb temperatures
- Determine hours in each temperature bin
- Calculate cooling degree-hours
- Identify percentage hours evaporative cooling viable

**Selection Criteria**:
| Climate Category | Design WB | Hours > 65°F WB | Suitability |
|------------------|-----------|-----------------|-------------|
| Excellent | <62°F | <100 | Direct or Two-Stage |
| Good | 62-67°F | 100-300 | Two-Stage or Hybrid |
| Marginal | 67-72°F | 300-600 | Indirect or Hybrid |
| Poor | >72°F | >600 | Pre-cooling only |

### Design Point Selection

Select design conditions for sizing:

**Conservative Approach**: 1% annual wet-bulb
**Standard Approach**: 2.5% annual wet-bulb
**Economy Approach**: 5% annual wet-bulb

More conservative selection provides more hours of comfort but increases equipment size.

## Capacity Calculation

### Sensible Cooling Load

Determine space sensible cooling requirement:

$$Q_{sensible} = Q_{transmission} + Q_{solar} + Q_{internal} + Q_{infiltration}$$

Note: Evaporative cooling primarily addresses sensible loads; latent removal is limited.

### Airflow Calculation

Required airflow for sensible cooling:

$$CFM = \frac{Q_{sensible}}{1.08 \times (T_{room} - T_{supply})}$$

Where:
- $T_{room}$ = design indoor temperature
- $T_{supply}$ = achievable supply temperature

### Supply Temperature Estimation

Estimate achievable supply temperature:

**Direct Evaporative**:
$$T_{supply} = T_{db,OA} - \epsilon_{DEC}(T_{db,OA} - T_{wb,OA})$$

**Two-Stage**:
$$T_{supply} = T_{db,OA} - [\epsilon_{IEC} + \epsilon_{DEC}(1-\epsilon_{IEC})](T_{db,OA} - T_{wb,OA})$$

## Equipment Type Selection

### Direct Evaporative Coolers

**Select When**:
- Design wet-bulb <65°F
- Humidity addition acceptable
- Lowest first cost required
- Simple installation preferred

**Typical Effectiveness**: 70-90%

### Indirect Evaporative Coolers

**Select When**:
- Supply humidity must be controlled
- Moderate humidity climates
- Humidity-sensitive applications
- Higher first cost acceptable

**Typical Effectiveness**: 50-75% (wet-bulb)

### Two-Stage Systems

**Select When**:
- Maximum cooling required
- Moderate humidity acceptable
- Climate supports both stages
- Energy savings justify cost

**Typical Effectiveness**: 90-115% (wet-bulb)

### Hybrid Systems

**Select When**:
- Evaporative cooling marginal
- Backup cooling required
- Variable climate conditions
- Peak load beyond evaporative capacity

## Equipment Sizing

### Face Area Sizing

Media face area determines capacity:

$$A_{face} = \frac{CFM}{V_{face}}$$

**Recommended Face Velocities**:
| Media Type | Velocity Range | Optimal |
|------------|----------------|---------|
| Rigid cellulose | 400-600 fpm | 500 fpm |
| Aspen pad | 250-400 fpm | 300 fpm |
| IEC plate | 400-600 fpm | 500 fpm |

### Media Depth Selection

Deeper media increases effectiveness and pressure drop:

| Depth | Effectiveness | ΔP | Application |
|-------|---------------|-----|-------------|
| 6" | 70-75% | 0.1" | Residential, economy |
| 8" | 80-85% | 0.15" | Light commercial |
| 12" | 85-90% | 0.25" | Commercial standard |
| 18" | 90-95% | 0.35" | High performance |

### Fan Sizing

Fan must overcome total static pressure:

$$\Delta P_{total} = \Delta P_{media} + \Delta P_{intake} + \Delta P_{duct} + \Delta P_{outlet}$$

Select fan for design CFM at total static, with margin for loaded media.

## Water System Sizing

### Evaporation Rate

Water consumption for cooling:

$$\dot{m}_{evap} = \frac{Q_{sensible}}{h_{fg}} ≈ 3\ gal/ton \cdot hr$$

### Bleed-Off Requirements

Prevent mineral concentration:

$$Bleed\ Rate = \frac{Evap\ Rate}{Cycles - 1}$$

Where cycles of concentration = 3-5 typical

**Total Water**: 4-5 gal/ton·hr including bleed

### Sump Sizing

Sump capacity for adequate reserve:
- Minimum: 5-10 gallons per ft² face area
- Or: 3-5 minutes pump flow capacity

## Performance Verification

### Commissioning Tests

Verify installed performance:

1. **Airflow measurement**: Compare to design CFM
2. **Temperature drop**: Verify effectiveness
3. **Pressure drop**: Check fan operating point
4. **Water distribution**: Confirm media wetting

### Effectiveness Verification

Calculate actual effectiveness:

$$\epsilon_{actual} = \frac{T_{in} - T_{out}}{T_{in} - T_{wb,in}}$$

Compare to published performance curves.

### Energy Performance

Measure EER or kW/ton:

$$EER = \frac{Q_{cooling}}{W_{total}}$$

Compare to design values and alternatives.

## Selection Documentation

### Equipment Schedule

Document selections:

| Item | Value |
|------|-------|
| Model/Manufacturer | |
| Airflow (CFM) | |
| Effectiveness (%) | |
| Supply air temp (design) | |
| Fan HP | |
| Pump GPM | |
| Water consumption | |
| Electrical (V/Ph/Hz) | |

### Operating Limits

Specify operating parameters:

- Maximum wet-bulb for evaporative mode
- Changeover points for hybrid systems
- Maintenance schedules
- Media replacement criteria

Careful evaporative cooler selection, matched to climate conditions and application requirements, ensures systems deliver expected performance while maximizing energy savings.
