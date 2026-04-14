---
title: "Stack Effect Pressure Differentials"
aliases: ["Stack Effect Pressure Differentials"]
description: "Pressure differential calculation and analysis for tall building stack effect including neutral plane location, hydrostatic pressure differences, and building height impact on HVAC system performance."
weight: 1
---

Stack effect pressure differentials in tall buildings create significant forces affecting HVAC system operation, building envelope performance, and occupant comfort. These pressure differences result from density variations between interior and exterior air columns, generating vertical air movement through shafts, stairwells, and elevator cores. Quantifying stack effect pressures enables proper design of mechanical systems, determination of door-opening forces, and prediction of infiltration/exfiltration rates.

## Fundamental Stack Effect Equation

Stack effect pressure differential derives from hydrostatic pressure differences between interior and exterior air columns at different temperatures. The governing equation:

ΔP = Cₛ × ρₒ × g × H × (Tᵢ - Tₒ) / Tᵢ

Where:
- ΔP = pressure differential (Pa or inches w.c.)
- Cₛ = stack coefficient (dimensionless)
- ρₒ = outdoor air density (kg/m³ or lbm/ft³)
- g = gravitational acceleration (9.81 m/s² or 32.2 ft/s²)
- H = height above neutral plane (m or ft)
- Tᵢ = interior absolute temperature (K or °R)
- Tₒ = outdoor absolute temperature (K or °R)

Simplified engineering form in I-P units:

ΔP = 0.0188 × H × (1/Tₒ - 1/Tᵢ)

Where:
- ΔP = pressure differential (inches w.c.)
- H = height from neutral plane (ft)
- Tₒ, Tᵢ = outdoor and indoor absolute temperatures (°R = °F + 460)

This equation reveals that pressure differential increases linearly with height above or below the neutral plane and increases with greater temperature difference between interior and exterior.

## Pressure Distribution in Tall Buildings

Stack effect creates characteristic pressure distribution along building height:

**Above Neutral Plane**:
- Interior pressure exceeds exterior pressure (positive pressure)
- Air flows outward through envelope openings (exfiltration)
- Magnitude increases linearly with height above neutral plane
- Maximum pressure at building top

**Below Neutral Plane**:
- Exterior pressure exceeds interior pressure (negative pressure)
- Air flows inward through envelope openings (infiltration)
- Magnitude increases linearly with depth below neutral plane
- Maximum negative pressure at building base

**At Neutral Plane**:
- Interior pressure equals exterior pressure (zero differential)
- No net airflow through envelope openings
- Location varies based on building characteristics and HVAC operation

## Example Calculation

Consider a 40-story office building (600 feet tall) with neutral plane at 20th floor (300 feet). Winter conditions: interior 70°F, exterior -10°F.

At building top (300 feet above neutral plane):
Tᵢ = 70 + 460 = 530°R
Tₒ = -10 + 460 = 450°R
ΔP = 0.0188 × 300 × (1/450 - 1/530)
ΔP = 0.0188 × 300 × (0.002222 - 0.001887)
ΔP = 0.0188 × 300 × 0.000335
ΔP = 0.189 inches w.c. (47 Pa)

This positive pressure drives air outward through top floors. At building base (300 feet below neutral plane), equal magnitude negative pressure drives infiltration.

## Temperature Differential Impact

Stack effect pressure varies directly with temperature difference between interior and exterior. Winter conditions with large temperature differentials generate maximum stack pressures. Summer conditions with smaller differentials produce reduced stack effect.

Temperature differential scenarios for 300-foot height above neutral plane:

| Interior Temp | Outdoor Temp | Temp Diff | Pressure Diff (inches w.c.) |
|--------------|--------------|-----------|---------------------------|
| 70°F | -10°F | 80°F | 0.189 |
| 70°F | 0°F | 70°F | 0.165 |
| 70°F | 20°F | 50°F | 0.118 |
| 70°F | 40°F | 30°F | 0.071 |
| 70°F | 60°F | 10°F | 0.024 |

This demonstrates winter stack effect typically dominates design considerations in cold climates. Summer reverse stack effect (cooling occupied space below ambient temperature) produces lower pressure differentials due to smaller temperature differences.

## Building Height Impact

Stack effect pressure increases linearly with distance from neutral plane. Taller buildings experience proportionally greater pressure differentials. This relationship makes stack effect management increasingly critical as building height increases.

Pressure differential at various heights (winter, 70°F interior, 0°F exterior):

| Height from Neutral Plane | Pressure Differential |
|--------------------------|---------------------|
| 50 ft (5 floors) | 0.028 inches w.c. (7 Pa) |
| 100 ft (10 floors) | 0.055 inches w.c. (14 Pa) |
| 200 ft (20 floors) | 0.110 inches w.c. (27 Pa) |
| 300 ft (30 floors) | 0.165 inches w.c. (41 Pa) |
| 400 ft (40 floors) | 0.220 inches w.c. (55 Pa) |

Buildings exceeding 300 feet height experience stack pressures significantly affecting HVAC system operation, elevator door performance, and vestibule effectiveness.

## Airflow Through Envelope Openings

Stack effect pressure differentials drive airflow through building envelope openings following orifice flow equations:

Q = C × A × √(2ΔP/ρ)

Where:
- Q = volumetric airflow (cfm)
- C = discharge coefficient (typically 0.6-0.7)
- A = flow area (ft²)
- ΔP = pressure differential (lbf/ft²)
- ρ = air density (lbm/ft³)

For engineering calculations in I-P units:

Q = 2610 × C × A × √ΔP

Where ΔP is in inches w.c.

This demonstrates that doubling pressure differential increases airflow by factor of √2 = 1.41. Quadrupling pressure increases airflow by factor of 2.

## Impact on HVAC System Design

Stack effect pressure differentials impose requirements on HVAC system design:

**Supply/Return Fan Pressure**: Mechanical systems must overcome stack effect pressures in addition to duct friction losses and terminal device pressure drops. Top floor supply systems may require reduced fan pressure (stack assists supply flow). Bottom floor systems require increased fan pressure (stack opposes supply flow).

**Shaft Pressurization Systems**: Stairwell and elevator shaft pressurization systems must overcome or utilize stack effect depending on season. Winter stack effect assists stairwell pressurization on upper floors but opposes it on lower floors. System design requires adequate pressure capability at worst-case locations.

**Vestibule Performance**: Building entrance vestibules at base experience maximum negative pressure during winter. Stack-induced infiltration through entrance doors creates cold drafts and door-opening force problems. Vestibule heating and revolving doors mitigate these effects.

**Elevator Performance**: Pressure differentials across elevator doors affect door operation. Excessive pressure (>0.30 inches w.c.) may prevent normal door opening. Elevator shaft venting or mechanical pressurization controls these pressures.

**Zone Pressure Control**: Building HVAC zones on different floors experience different stack effect pressures relative to corridors and vertical shafts. Supply/return air balancing must account for these pressure biases to maintain intended zone pressurization.

## Transient Stack Effect

Rapidly changing outdoor temperature creates transient stack effect as building interior temperature distribution adjusts. Morning warm-up following night setback generates temporary enhanced stack effect. These transient conditions may exceed steady-state predictions.

Thermal mass in building structure delays interior temperature response to outdoor conditions. Lightweight construction responds quickly (hours), while massive concrete structures respond slowly (days). HVAC control strategies should account for these thermal lag effects when managing stack-induced pressures.

## Wind Interaction with Stack Effect

Wind pressure on building exterior modifies stack effect pressure distribution. Windward facade experiences positive pressure; leeward facade experiences negative pressure. These wind pressures combine algebraically with stack pressures, creating complex three-dimensional pressure fields.

At windward facade, wind pressure adds to stack pressure above neutral plane, increasing exfiltration. Wind pressure opposes stack pressure below neutral plane, potentially reversing flow direction. At leeward facade, negative wind pressure enhances infiltration below neutral plane and may reverse flow above neutral plane.

Wind effects typically dominate stack effect for wind speeds exceeding 15-20 mph. Combined analysis requires computational fluid dynamics (CFD) modeling or wind tunnel testing for critical applications.

## Measurement and Verification

Measuring stack effect pressure differentials requires differential pressure instrumentation with resolution of 0.001 inches w.c. (0.25 Pa) and accuracy of ±0.005 inches w.c. Measurement locations:

- Exterior wall at multiple floors (measure envelope pressure difference)
- Elevator shaft relative to occupied floors
- Stairwell relative to floor lobbies
- Mechanical shafts relative to occupied spaces

Measurements should span multiple outdoor temperature conditions to validate pressure predictions across full operating range. Winter measurements during extreme cold provide maximum stack pressure conditions. Summer measurements verify reverse stack effect magnitude.

Recorded pressure data correlates with outdoor temperature following theoretical relationships. Deviations from predicted pressure indicate unaccounted leakage paths, mechanical system impacts, or wind effects requiring investigation.

## Mitigation Strategies

Several approaches mitigate problematic stack effect:

**Compartmentalization**: Separating building into multiple vertical zones with sealed horizontal barriers at mid-height. Each zone develops independent neutral plane at mid-height, reducing maximum pressure differential by factor of 2.

**Shaft Sealing**: Minimizing leakage in stairwells, elevator shafts, and mechanical shafts reduces stack-driven airflow. Fire/smoke dampers at shaft penetrations limit vertical air movement.

**Mechanical Pressurization**: Active pressurization or depressurization of vertical shafts counteracts stack effect. Elevator shaft fans can maintain shaft pressure equal to average building pressure, eliminating differential across elevator doors.

**Vestibule Design**: Multiple vestibules at building entrances (double vestibule) reduce infiltration impact. Revolving doors eliminate open door area. Vestibule heating prevents cold drafts in occupied spaces.

**Building Envelope Tightening**: Reducing envelope leakage area decreases airflow for given pressure differential. Achieving 0.25 cfm/ft² envelope leakage at 0.30 inches w.c. test pressure represents good practice for tall buildings.
