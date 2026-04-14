---
title: "Liquid Recirculation Principles"
aliases: ["Liquid Recirculation Principles"]
description: "Thermodynamic principles of liquid overfeed refrigeration systems including wet evaporator operation, heat transfer enhancement, recirculation ratios, and efficiency advantages over direct expansion systems"
weight: 1
---

## Overview

Liquid recirculation represents a fundamental departure from direct expansion refrigeration system operation. Instead of complete evaporation of refrigerant within the evaporator coil, liquid overfeed systems deliberately maintain liquid refrigerant presence throughout the entire evaporator surface. This approach requires circulating 2 to 6 times more liquid refrigerant through the evaporator than the actual refrigeration capacity demands, returning the unevaporated liquid to a low-pressure receiver for separation and recirculation.

The thermodynamic advantage stems from maintaining nucleate boiling heat transfer throughout the evaporator rather than transitioning to convective vapor cooling in superheated regions. This operational principle fundamentally changes evaporator heat transfer characteristics, pressure drop behavior, and overall system efficiency.

## Recirculation Ratio Fundamentals

The recirculation ratio (n) defines the relationship between total mass flow through the evaporator and the actual evaporated mass:

n = ṁ_total / ṁ_evaporated

Where:
- ṁ_total = total refrigerant mass flow through evaporator (lb/min or kg/min)
- ṁ_evaporated = mass of refrigerant evaporated (lb/min or kg/min)

The quality (x) at the evaporator outlet relates inversely to recirculation ratio:

x_outlet = 1 / n

For a system with recirculation ratio of 4:1, outlet quality equals 0.25, meaning 75% of refrigerant leaving the evaporator remains liquid.

### Typical Recirculation Ratios by Application

| Application Type | Recirculation Ratio | Outlet Quality | Operating Characteristics |
|-----------------|--------------------|-----------------|-----------------------------|
| Cold Storage Rooms | 2:1 to 3:1 | 0.33 to 0.50 | Lower ratios reduce pump power |
| Process Cooling | 3:1 to 4:1 | 0.25 to 0.33 | Balanced performance and cost |
| Ice Rink Systems | 4:1 to 5:1 | 0.20 to 0.25 | High ratio ensures complete wetting |
| Blast Freezers | 3:1 to 4:1 | 0.25 to 0.33 | Moderate ratio for rapid cooling |
| Flooded Chillers | 5:1 to 6:1 | 0.17 to 0.20 | Highest ratios for optimal heat transfer |

## Thermodynamic Advantages

### Complete Evaporator Wetting

Liquid overfeed systems maintain liquid refrigerant contact with 100% of the evaporator internal surface area. Direct expansion systems typically achieve complete liquid wetting only in the first 60-75% of coil length, with the remaining surface area handling superheated vapor at significantly reduced heat transfer coefficients.

The heat transfer coefficient for nucleate boiling (h_nb) exceeds that of vapor convection (h_v) by factors of 5 to 15:

h_nb / h_v = 5 to 15

This disparity means that maintaining liquid presence throughout the evaporator directly translates to enhanced overall heat transfer performance.

### Enhanced Heat Transfer Performance

Nucleate boiling heat transfer coefficients for typical refrigerants range from 800 to 2500 Btu/(hr·ft²·°F) [4500 to 14,000 W/(m²·K)], while single-phase vapor convection yields only 50 to 200 Btu/(hr·ft²·°F) [280 to 1100 W/(m²·K)].

The overall evaporator heat transfer coefficient (U_overall) improves significantly:

1/U_overall = 1/h_refrigerant + t_wall/k_wall + 1/h_air

When h_refrigerant increases from 150 Btu/(hr·ft²·°F) for superheated vapor to 1200 Btu/(hr·ft²·°F) for nucleate boiling, the refrigerant-side thermal resistance drops from 0.0067 to 0.0008 hr·ft²·°F/Btu, reducing overall thermal resistance by approximately 15-25% depending on air-side and wall resistances.

### Heat Transfer Coefficient Comparison

| Evaporator Region | DX System h [Btu/(hr·ft²·°F)] | Overfeed System h [Btu/(hr·ft²·°F)] | Improvement Factor |
|-------------------|-------------------------------|-------------------------------------|-------------------|
| Inlet (two-phase) | 1000-1500 | 1200-1800 | 1.2-1.3 |
| Mid-section (two-phase) | 800-1200 | 1200-1800 | 1.3-1.6 |
| Outlet (two-phase) | 200-400 (superheated) | 1000-1500 | 4.0-6.0 |
| Overall Weighted Average | 650-900 | 1200-1700 | 1.6-2.0 |

## Reduced Superheat Requirements

Direct expansion systems require 8-15°F [4-8°C] of superheat at the evaporator outlet to ensure no liquid refrigerant returns to the compressor. This superheat represents pure sensible heat transfer at low heat transfer coefficients, reducing effective evaporator capacity.

Liquid overfeed systems eliminate superheat requirements within the evaporator. The low-pressure receiver provides liquid-vapor separation, allowing saturated vapor or slightly superheated vapor to return to the compressor while liquid recirculates. This eliminates 10-20% of evaporator surface area previously dedicated to superheat production.

The capacity gain from eliminating superheat penalties can be expressed:

Q_gain = ṁ × c_p,vapor × ΔT_superheat

For a 100-ton [352 kW] ammonia system operating at 20°F [-6.7°C] evaporating temperature requiring 10°F [5.6°C] superheat:

Q_superheat_penalty = 137.5 lb/min × 0.523 Btu/(lb·°F) × 10°F = 719 Btu/min = 0.6 tons

Eliminating this superheat requirement recovers 0.6% of system capacity while improving evaporator temperature uniformity.

## Uniform Temperature Distribution

Pressure drop through evaporator coils creates corresponding saturation temperature reduction from inlet to outlet. In direct expansion systems, this temperature glide combines with superheat to create significant temperature stratification:

ΔT_total,DX = ΔT_saturation + ΔT_superheat

Overfeed systems experience only saturation temperature change:

ΔT_total,overfeed = ΔT_saturation

### Temperature Profile Comparison

| System Type | Inlet Temperature | Mid-point Temperature | Outlet Temperature | Total Temperature Range |
|-------------|-------------------|------------------------|---------------------|------------------------|
| DX System (R-717, 20°F evap) | 20°F [-6.7°C] | 18°F [-7.8°C] | 30°F [-1.1°C] | 10°F [5.6°C] |
| Overfeed System (R-717, 20°F evap) | 20°F [-6.7°C] | 19°F [-7.2°C] | 18°F [-7.8°C] | 2°F [1.1°C] |
| Temperature Uniformity Improvement | - | - | - | 80% reduction |

This improved temperature uniformity provides more consistent product temperatures in cold storage applications and reduces the average temperature difference driving moisture migration and product dehydration.

## System Efficiency Benefits

### Reduced Compressor Discharge Temperature

Liquid overfeed systems return saturated or slightly superheated vapor to compressors rather than highly superheated vapor typical of direct expansion systems. Lower suction superheat directly reduces compressor discharge temperature:

T_discharge = T_suction × (P_discharge/P_suction)^[(k-1)/k] + Motor heat

For reciprocating ammonia compressors:
- DX system with 20°F suction superheat: discharge temperature ≈ 220-240°F [104-116°C]
- Overfeed system with 5°F suction superheat: discharge temperature ≈ 200-220°F [93-104°C]

This 20-40°F [11-22°C] reduction in discharge temperature extends compressor valve life, reduces oil degradation, and improves volumetric efficiency.

### Improved Oil Return Characteristics

Maintaining liquid refrigerant throughout evaporators ensures positive oil entrainment back to the low-pressure receiver. The high mass flux in overfeed systems (typically 50-150 lb/(ft²·s) [244-732 kg/(m²·s)]) provides sufficient velocity to transport oil even at low qualities.

Direct expansion systems must maintain minimum vapor velocities to entrain oil, particularly in the final superheated section where mass flux drops significantly. This constraint often requires oversized suction line sizing or vertical risers with velocity requirements:

v_min,oil = 700 to 1000 ft/min [3.6 to 5.1 m/s] for horizontal lines
v_min,oil = 1000 to 1500 ft/min [5.1 to 7.6 m/s] for vertical risers

Overfeed systems naturally exceed these velocities throughout the evaporator, improving oil return reliability.

## Pressure Drop Considerations

### Two-Phase Pressure Drop

Overfeed systems maintain two-phase flow throughout the evaporator, experiencing pressure drop characteristics dominated by acceleration and frictional components:

ΔP_total = ΔP_friction + ΔP_acceleration + ΔP_static

The acceleration pressure drop component results from vapor generation increasing volumetric flow rate:

ΔP_acceleration = G² × [x²/(ρ_v × α) + (1-x)²/(ρ_l × (1-α))]_outlet - [similar term]_inlet

Where:
- G = mass flux [lb/(ft²·s) or kg/(m²·s)]
- x = quality (mass fraction)
- α = void fraction
- ρ_v, ρ_l = vapor and liquid densities

### Pressure Drop Comparison

| Evaporator Type | Inlet Pressure | Outlet Pressure | Pressure Drop | Equivalent ΔT_sat |
|-----------------|----------------|-----------------|---------------|-------------------|
| DX Coil (R-717, 20°F) | 34.3 psia | 32.8 psia | 1.5 psi | 1.8°F [1.0°C] |
| Overfeed Coil (R-717, 20°F, n=4) | 34.3 psia | 33.5 psia | 0.8 psi | 1.0°F [0.5°C] |
| Pressure Drop Reduction | - | - | 47% | 44% |

Lower pressure drop in overfeed systems results from reduced vapor velocity (due to incomplete evaporation) and shorter effective flow length for complete vapor generation.

## Part Load Performance

Liquid overfeed systems demonstrate superior part-load performance compared to direct expansion systems. As cooling load decreases, the recirculation pump continues to supply liquid refrigerant throughout the evaporator, maintaining complete surface wetting even at reduced evaporation rates.

Direct expansion systems at part load experience:
- Reduced refrigerant mass flow
- Decreased evaporator occupancy
- Earlier transition to superheated vapor
- Reduced effective heat transfer area
- Lower overall heat transfer coefficient

Overfeed systems maintain:
- Consistent liquid distribution
- Complete surface wetting
- High heat transfer coefficients
- Full evaporator utilization
- Stable suction temperature

### Part Load Efficiency Comparison

| Load Condition | DX System Efficiency | Overfeed System Efficiency | Efficiency Advantage |
|----------------|----------------------|----------------------------|----------------------|
| 100% Load | 100% (baseline) | 103% | +3% |
| 75% Load | 96% | 102% | +6% |
| 50% Load | 91% | 100% | +9% |
| 25% Load | 83% | 96% | +13% |

The widening efficiency advantage at reduced loads results from overfeed systems maintaining consistent heat transfer performance while direct expansion systems experience degraded evaporator effectiveness.

## Advantages Over Direct Expansion Systems

### Capacity Enhancement

Liquid overfeed evaporators deliver 10-20% greater capacity than equivalent direct expansion coils due to:
1. Complete surface area utilization for boiling heat transfer
2. Elimination of low-efficiency superheated regions
3. Reduced pressure drop maintaining higher average saturation temperature
4. Improved heat transfer coefficients throughout

### Reduced Refrigerant Charge Variability

Direct expansion systems experience significant refrigerant charge migration based on load conditions, ambient temperature, and operating mode. Liquid overfeed systems concentrate refrigerant inventory in the low-pressure receiver, providing:
- Stable evaporator refrigerant charge
- Consistent system performance
- Simplified charge management
- Reduced sensitivity to ambient conditions

### System Control Simplicity

Overfeed systems eliminate the need for precise superheat control at each evaporator. The low-pressure receiver provides:
- Centralized liquid level control
- Simplified evaporator valve control
- Reduced sensor requirements
- Improved reliability

## Design Considerations

### Recirculation Ratio Selection

Higher recirculation ratios provide:
- More complete evaporator wetting
- Higher heat transfer coefficients
- Better temperature uniformity
- Improved part-load performance

But require:
- Larger recirculation pumps
- Higher pump power consumption
- Larger diameter evaporator connections
- Increased low-pressure receiver size

Optimal recirculation ratio balances heat transfer performance against parasitic pump power:

COP_net = (Q_evaporator - W_pump) / W_compressor

### Minimum Recirculation Ratios

| Evaporator Configuration | Minimum Ratio | Recommended Ratio | Justification |
|--------------------------|---------------|-------------------|---------------|
| Horizontal Shell-and-Tube | 2.5:1 | 3:1 to 4:1 | Ensure tube flooding |
| Vertical Shell-and-Tube | 2:1 | 2.5:1 to 3:1 | Gravity aids distribution |
| Plate Heat Exchanger | 3:1 | 4:1 to 5:1 | Ensure channel flooding |
| Air Coils (horizontal) | 3:1 | 4:1 to 5:1 | Overcome stratification |
| Air Coils (vertical) | 2.5:1 | 3:1 to 4:1 | Gravity-assisted flow |

## Summary

Liquid recirculation principles fundamentally enhance refrigeration system performance by maintaining nucleate boiling heat transfer throughout evaporators. The thermodynamic advantages include 60-100% improvement in local heat transfer coefficients, 10-20% system capacity enhancement, improved temperature uniformity, and superior part-load efficiency.

Proper recirculation ratio selection balances heat transfer enhancement against pump parasitic power consumption, with typical ratios ranging from 2:1 for simple applications to 6:1 for critical heat transfer applications. The operational benefits of reduced superheat requirements, improved oil return, and simplified control justify liquid overfeed system complexity for industrial refrigeration applications above 20-25 tons capacity.
