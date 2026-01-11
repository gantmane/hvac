---
title: "Energy Savings from Demand-Controlled Ventilation"
description: "Quantify DCV energy savings in classrooms including heating, cooling, and fan power reductions. Analysis of 20-40% ventilation energy savings with calculation methods."
date: 2025-01-05
keywords:
  - demand-controlled ventilation energy savings
  - DCV cost reduction
  - classroom ventilation efficiency
  - CO2-based ventilation control
  - HVAC energy consumption
  - outdoor air reduction benefits
  - ventilation load calculations
  - energy recovery with DCV
weight: 3
---

Demand-controlled ventilation (DCV) in educational facilities delivers substantial energy savings by reducing unnecessary outdoor air ventilation during periods of low or partial occupancy. Field studies and simulation analyses consistently demonstrate ventilation energy reductions of 20-40% in typical classroom applications, with specific savings dependent on climate, occupancy patterns, and baseline ventilation rates.

## Energy Savings Mechanisms

DCV reduces energy consumption through three primary mechanisms: reduced heating energy for outdoor air, reduced cooling energy for outdoor air, and reduced fan power from lower airflow rates.

**Heating Energy Reduction**

During heating season, introducing outdoor air requires sensible heating to raise the air temperature to the supply air setpoint. The heating energy required per unit time is:

$$Q_{\text{heat}} = \dot{m} \cdot c_p \cdot (T_{\text{supply}} - T_{\text{outdoor}})$$

where $\dot{m}$ is the mass flow rate of outdoor air (kg/s), $c_p$ is the specific heat of air (approximately 1.006 kJ/kg·K), $T_{\text{supply}}$ is the supply air temperature (°C), and $T_{\text{outdoor}}$ is the outdoor air temperature (°C).

For volumetric flow calculations:

$$Q_{\text{heat}} = \dot{V} \cdot \rho \cdot c_p \cdot \Delta T = 1.23 \cdot \dot{V} \cdot \Delta T \text{ (W)}$$

where $\dot{V}$ is the outdoor air volumetric flow rate (m³/s), $\rho$ is air density (approximately 1.225 kg/m³ at sea level), and $\Delta T$ is the temperature difference (K or °C).

DCV reduces $\dot{V}$ in proportion to the reduction in occupancy, directly decreasing heating energy. A classroom designed for 30 students at 7.5 L/s per person (15 cfm) requires 225 L/s (475 cfm) at full occupancy but only 75 L/s (160 cfm) with 10 students present—a 67% reduction in outdoor air.

**Cooling Energy Reduction**

Outdoor air imposes both sensible and latent cooling loads. The total cooling energy is:

$$Q_{\text{cool}} = \dot{m} \cdot [(h_{\text{outdoor}} - h_{\text{supply}})]$$

where $h_{\text{outdoor}}$ and $h_{\text{supply}}$ are the enthalpies of outdoor air and supply air respectively (kJ/kg).

Separating sensible and latent components:

$$Q_{\text{sensible}} = \dot{m} \cdot c_p \cdot (T_{\text{outdoor}} - T_{\text{supply}})$$

$$Q_{\text{latent}} = \dot{m} \cdot h_{fg} \cdot (\omega_{\text{outdoor}} - \omega_{\text{supply}})$$

where $h_{fg}$ is the latent heat of vaporization for water (approximately 2501 kJ/kg at 0°C), and $\omega$ represents humidity ratio (kg water/kg dry air).

In humid climates, latent cooling loads from outdoor air can exceed sensible loads. DCV provides proportionally greater savings in these conditions by reducing moisture introduction.

**Fan Energy Reduction**

Fan power consumption relates to airflow rate and pressure rise:

$$P_{\text{fan}} = \frac{\dot{V} \cdot \Delta p}{\eta_{\text{fan}}}$$

where $\Delta p$ is the total pressure rise across the fan (Pa), and $\eta_{\text{fan}}$ is the fan total efficiency (typically 0.50-0.70 for classroom systems).

For variable air volume systems with variable frequency drives, fan power varies approximately with the cube of flow rate due to the fan affinity laws:

$$\frac{P_2}{P_1} = \left(\frac{\dot{V}_2}{\dot{V}_1}\right)^3$$

Reducing outdoor air from 225 L/s to 75 L/s (67% reduction) in a VAV system potentially reduces fan power by:

$$\frac{P_2}{P_1} = (0.33)^3 = 0.036$$

This represents a 96% reduction in fan power for the outdoor air component. However, total system fan power reduction is less dramatic since return air and minimum flow requirements limit the overall flow reduction.

## Typical Energy Savings Ranges

ASHRAE research and field studies provide the following savings ranges:

**By Climate Zone**

- Cold climates (heating-dominated): 25-45% ventilation energy reduction
- Mixed climates: 20-35% ventilation energy reduction
- Hot-humid climates: 30-50% ventilation energy reduction (higher latent savings)
- Hot-dry climates: 15-30% ventilation energy reduction

**By System Type**

- Constant air volume (CAV) systems: 20-30% savings (outdoor air damper modulation only)
- Variable air volume (VAV) systems: 30-45% savings (airflow reduction plus fan power)
- Dedicated outdoor air systems (DOAS): 35-50% savings (entire DOAS unit modulates)

**By Occupancy Pattern**

Schools with highly variable occupancy (frequent transitions, empty periods) achieve greater savings than continuously occupied spaces. Typical K-12 classrooms experience:

- 40-60% average occupancy during school hours
- 0% occupancy during lunch, recess, assemblies (15-25% of school day)
- Weekends, holidays, summer (significant periods at minimum ventilation)

## Energy Savings Calculation Methodology

Annual energy savings estimation requires bin analysis or hourly simulation accounting for:

1. **Occupancy schedule** - Percentage of time at various occupancy levels
2. **Climate data** - Temperature and humidity bin hours
3. **Baseline ventilation** - Fixed outdoor air rate (L/s or cfm)
4. **DCV-modulated ventilation** - Occupancy-based outdoor air rate
5. **HVAC system characteristics** - Efficiency, fan power, economizer operation

Simplified annual heating energy savings:

$$E_{\text{heat,saved}} = \sum_{i} (\dot{V}_{\text{baseline}} - \dot{V}_{\text{DCV},i}) \cdot \rho \cdot c_p \cdot \Delta T_i \cdot h_i \cdot \frac{1}{\eta_{\text{heat}}}$$

where $i$ represents each occupancy/temperature bin, $h_i$ is hours in bin $i$, and $\eta_{\text{heat}}$ is heating system efficiency.

## Energy Recovery Integration

DCV provides reduced but still significant savings when combined with energy recovery ventilation (ERV). The ERV effectiveness reduces the temperature and humidity difference between outdoor air and supply air:

$$\Delta T_{\text{effective}} = \Delta T_{\text{gross}} \cdot (1 - \epsilon_{\text{sensible}})$$

where $\epsilon_{\text{sensible}}$ is the sensible effectiveness (typically 0.60-0.80).

Even with 70% energy recovery, DCV modulation reduces the remaining 30% load proportionally, yielding 6-12% total HVAC energy savings in typical applications.

## Documented Savings Studies

ASHRAE Research Project RP-1547 examined DCV performance in educational facilities, documenting average ventilation energy savings of 32% across multiple climate zones. California Energy Commission studies of Title 24 DCV requirements showed median savings of 28% in classrooms.

The National Renewable Energy Laboratory (NREL) analysis of school DCV retrofits measured 25-40% reduction in ventilation-related energy consumption, with payback periods of 2-5 years depending on installation complexity and energy costs.

## Economic Considerations

Energy cost savings must be evaluated against DCV implementation costs including CO₂ sensors ($300-600 per classroom), control system integration ($1,000-3,000 per air handler), and commissioning ($2,000-5,000 per building). Typical installed costs range from $1,500-4,000 per classroom.

At $0.10/kWh electricity and $0.80/therm natural gas, a typical 75 m² (800 ft²) classroom can save $200-500 annually, providing simple payback of 3-8 years. Higher energy costs, extreme climates, and larger classrooms improve economics significantly.

## Implementation Best Practices

Maximize energy savings by:

- Setting minimum outdoor air to code-required unoccupied levels (not design occupancy)
- Commissioning CO₂ sensor calibration and control sequences
- Integrating DCV with economizer control to prevent conflicts
- Monitoring actual savings through submetering or building automation trending
- Educating facility staff on proper DCV operation and maintenance

DCV represents one of the most cost-effective energy conservation measures for educational facilities, particularly in climates with significant heating or dehumidification loads and buildings with variable occupancy patterns.
