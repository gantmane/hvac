---
title: "Natural Ventilation Design"
description: "Physics-based design guidance for natural ventilation systems including stack effect calculations, wind-driven airflow, opening sizing methodology, and hybrid system integration strategies."
keywords:
  - natural ventilation design
  - stack effect calculation
  - wind-driven ventilation
  - buoyancy ventilation
  - thermal chimney
  - opening sizing
  - cross ventilation
  - hybrid ventilation
  - passive cooling
  - CIBSE AM10
weight: 2
---

# Natural Ventilation Design

Natural ventilation harnesses pressure differentials created by thermal buoyancy and wind forces to provide fresh air without mechanical energy. Proper design requires quantitative analysis of driving forces, airflow paths, and thermal comfort boundaries.

## Stack Effect Principles

Stack effect (thermal buoyancy) generates airflow through vertical pressure differentials caused by indoor-outdoor temperature differences.

### Stack Effect Airflow Calculation

The volumetric airflow rate driven by stack effect:

**Q = C<sub>d</sub> × A × √(2 × g × H × ΔT / T<sub>avg</sub>)**

Where:
- Q = volumetric airflow rate (m³/s)
- C<sub>d</sub> = discharge coefficient (0.60-0.65 for sharp-edged openings)
- A = effective opening area (m²)
- g = gravitational acceleration (9.81 m/s²)
- H = vertical distance between inlet and outlet (m)
- ΔT = indoor-outdoor temperature difference (K)
- T<sub>avg</sub> = average absolute temperature (K)

### Neutral Pressure Level

The neutral pressure level (NPL) occurs where indoor and outdoor pressures equalize. For two openings:

**H<sub>NPL</sub> = (A<sub>upper</sub>² × H) / (A<sub>lower</sub>² + A<sub>upper</sub>²)**

Optimal design places the NPL near the mid-height to balance inlet and outlet velocities.

### Stack Pressure Differential

Pressure difference at height h above NPL:

**ΔP = ρ<sub>o</sub> × g × h × (ΔT / T<sub>avg</sub>)**

Where:
- ΔP = pressure differential (Pa)
- ρ<sub>o</sub> = outdoor air density (kg/m³)
- h = height above NPL (m)

## Wind-Driven Ventilation

Wind creates pressure distributions on building facades based on geometry and orientation. Surface pressures drive cross-ventilation through the building envelope.

### Wind Pressure Coefficients

Surface pressure relative to dynamic wind pressure:

**P<sub>surface</sub> = C<sub>p</sub> × (ρ × V² / 2)**

Where:
- P<sub>surface</sub> = gauge pressure on surface (Pa)
- C<sub>p</sub> = wind pressure coefficient (-0.7 to +0.7 typical)
- ρ = air density (1.2 kg/m³ at sea level)
- V = wind velocity at building height (m/s)

Windward faces: C<sub>p</sub> = +0.5 to +0.8
Leeward faces: C<sub>p</sub> = -0.3 to -0.5
Side faces: C<sub>p</sub> = -0.6 to -0.7

### Wind-Driven Airflow

Flow rate through openings with pressure differential:

**Q = C<sub>d</sub> × A × √(ΔP / (ρ/2))**

For cross-ventilation with inlet and outlet:

**Q = C<sub>d</sub> × A<sub>eff</sub> × V<sub>ref</sub> × √(C<sub>p,inlet</sub> - C<sub>p,outlet</sub>)**

Where:
- A<sub>eff</sub> = 1 / √(1/A<sub>inlet</sub>² + 1/A<sub>outlet</sub>²)
- V<sub>ref</sub> = reference wind velocity (m/s)

## Opening Sizing Methodology

Effective opening area must satisfy both ventilation rate requirements and velocity constraints for thermal comfort.

### Free Area Calculation

Required free area for specified ventilation rate:

**A<sub>required</sub> = Q<sub>design</sub> / (C<sub>d</sub> × v<sub>design</sub>)**

Where:
- Q<sub>design</sub> = required ventilation rate (m³/s)
- v<sub>design</sub> = design air velocity through opening (m/s)

### Opening Ratio Guidelines

| Configuration | Inlet:Outlet Ratio | Performance |
|--------------|-------------------|-------------|
| Balanced | 1:1 | Maximum airflow |
| Inlet-limited | 1:2 | Reduced flow, lower inlet velocity |
| Outlet-limited | 2:1 | Reduced flow, higher indoor velocity |

CIBSE AM10 recommends inlet areas equal to or greater than outlet areas for occupied spaces.

### Effective Opening Height

For vertical displacement ventilation, minimum opening separation:

**H<sub>min</sub> = Q² × T<sub>avg</sub> / (C<sub>d</sub>² × A² × 2 × g × ΔT)**

Typical effective heights: 2-4 m for single-story, 6-12 m for multi-story atria.

## Thermal Comfort Limits

Natural ventilation operates within narrower comfort boundaries than mechanical systems.

### Acceptable Temperature Range

CIBSE TM52 adaptive comfort model defines acceptable indoor operative temperature:

**T<sub>comf</sub> = 0.33 × T<sub>rm</sub> + 18.8°C**

Where:
- T<sub>comf</sub> = comfort temperature (°C)
- T<sub>rm</sub> = running mean outdoor temperature (°C)

Acceptable range: T<sub>comf</sub> ± 3K for 90% acceptability

### Air Velocity Constraints

| Condition | Maximum Velocity | Application |
|-----------|-----------------|-------------|
| Sedentary work | 0.15-0.25 m/s | Offices, classrooms |
| Light activity | 0.25-0.40 m/s | Retail, circulation |
| Elevated air movement | 0.80-1.50 m/s | Cooling effect in warm conditions |

Elevated velocities acceptable when T<sub>op</sub> > 25°C with occupant control.

### Cooling Capacity Limitations

Natural ventilation cooling capacity:

**Q<sub>cooling</sub> = ρ × c<sub>p</sub> × V<sub>flow</sub> × ΔT**

Practical cooling: 15-30 W/m² in temperate climates
Peak capacity: 40-50 W/m² with night cooling

## Hybrid Integration Strategies

Hybrid (mixed-mode) systems combine natural and mechanical ventilation to extend operational range.

### Mode Transition Criteria

**Changeover Logic:**

```
IF (T_outdoor < T_lower OR T_outdoor > T_upper) THEN
    Mechanical_Mode
ELSE IF (Wind_velocity > V_min AND ΔT > ΔT_min) THEN
    Natural_Mode
ELSE
    Mechanical_Mode
END IF
```

Typical thresholds:
- T<sub>lower</sub> = 12-15°C
- T<sub>upper</sub> = 25-28°C
- V<sub>min</sub> = 1.0-2.0 m/s
- ΔT<sub>min</sub> = 2-3K

### System Configurations

**Zoned Hybrid:** Core zones mechanically ventilated, perimeter zones naturally ventilated

**Changeover Hybrid:** Building switches between natural and mechanical modes

**Concurrent Hybrid:** Natural ventilation supplements mechanical system continuously

### Integration Requirements

- Automated window/damper actuators with BMS integration
- Temperature and wind velocity sensors
- Interlocked mechanical system shutdown during natural mode
- Minimum mechanical backup: 0.3-0.4 L/s/m² for IAQ maintenance
- Night purge capability: 5-10 air changes per hour

## Design Process Summary

1. **Establish Requirements:** Determine ventilation rates per ASHRAE 62.1 or local codes
2. **Analyze Climate:** Assess temperature, wind speed, and humidity profiles
3. **Calculate Driving Forces:** Quantify stack and wind pressures for design conditions
4. **Size Openings:** Determine inlet/outlet areas using effective area calculations
5. **Verify Comfort:** Confirm air velocities and temperatures within acceptable limits
6. **Plan Hybrid Modes:** Define transition criteria and mechanical backup capacity
7. **Model Performance:** Use CFD or multizone analysis for complex geometries

Natural ventilation provides energy-efficient air delivery when outdoor conditions align with comfort requirements. Accurate prediction of airflow requires careful analysis of buoyancy and wind forces, proper opening design, and realistic assessment of thermal comfort boundaries.

---

**References:**
CIBSE AM10: Natural Ventilation in Non-Domestic Buildings
CIBSE TM52: The Limits of Thermal Comfort
ASHRAE Fundamentals Handbook, Chapter 16: Ventilation and Infiltration
