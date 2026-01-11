---
title: "ERV Performance Factors and Testing Standards"
description: "Technical analysis of energy recovery ventilator effectiveness, pressure drop, cross-contamination, and performance degradation per ASHRAE Standard 84 testing protocols."
date: 2025-01-05
keywords:
  - ERV effectiveness
  - ASHRAE Standard 84
  - energy recovery performance
  - pressure drop calculations
  - cross-contamination testing
  - sensible effectiveness
  - latent effectiveness
  - heat exchanger performance
weight: 6
draft: false
---

## Effectiveness Fundamentals

Energy recovery ventilator performance is quantified through effectiveness metrics that describe the device's ability to transfer sensible and latent energy between airstreams. These metrics form the foundation for system sizing and energy analysis.

### Sensible Effectiveness

Sensible effectiveness measures temperature change effectiveness:

$$\epsilon_s = \frac{T_{supply} - T_{outdoor}}{T_{exhaust} - T_{outdoor}}$$

Where:
- $\epsilon_s$ = sensible effectiveness (dimensionless)
- $T_{supply}$ = supply air temperature leaving ERV (°F)
- $T_{outdoor}$ = outdoor air temperature entering ERV (°F)
- $T_{exhaust}$ = exhaust air temperature entering ERV (°F)

For heating mode, the equation reverses to:

$$\epsilon_s = \frac{T_{outdoor} - T_{supply}}{T_{outdoor} - T_{exhaust}}$$

### Latent Effectiveness

Latent effectiveness quantifies moisture transfer capability:

$$\epsilon_l = \frac{W_{supply} - W_{outdoor}}{W_{exhaust} - W_{outdoor}}$$

Where:
- $\epsilon_l$ = latent effectiveness (dimensionless)
- $W_{supply}$ = supply air humidity ratio leaving ERV (lb/lb)
- $W_{outdoor}$ = outdoor air humidity ratio entering ERV (lb/lb)
- $W_{exhaust}$ = exhaust air humidity ratio entering ERV (lb/lb)

### Total Effectiveness

Total effectiveness accounts for both sensible and latent energy transfer:

$$\epsilon_t = \frac{h_{supply} - h_{outdoor}}{h_{exhaust} - h_{outdoor}}$$

Where:
- $\epsilon_t$ = total effectiveness (dimensionless)
- $h_{supply}$ = supply air enthalpy leaving ERV (Btu/lb)
- $h_{outdoor}$ = outdoor air enthalpy entering ERV (Btu/lb)
- $h_{exhaust}$ = exhaust air enthalpy entering ERV (Btu/lb)

## ASHRAE Standard 84 Testing Protocol

ASHRAE Standard 84-2020 establishes standardized test procedures for air-to-air heat exchangers. This standard ensures consistent performance reporting across manufacturers.

### Test Conditions

Standard rating conditions per ASHRAE 84:

| Parameter | Summer Condition | Winter Condition |
|-----------|------------------|------------------|
| Outdoor Temp | 95°F | 5°F |
| Outdoor RH | 40% | Not specified |
| Exhaust Temp | 75°F | 75°F |
| Exhaust RH | 50% | 50% |
| Face Velocity | 600 fpm | 600 fpm |
| Airflow Balance | 1:1 ratio | 1:1 ratio |

### Performance Metrics Measured

ASHRAE 84 requires measurement and reporting of:

- Sensible effectiveness at multiple airflow rates
- Latent effectiveness (for enthalpy exchangers only)
- Pressure drop on both airstreams
- Exhaust air transfer ratio (EATR) for cross-contamination
- Power consumption (if motorized)

## Comparative Performance Data

ERV device type significantly impacts performance characteristics:

| Device Type | Sensible Eff. | Latent Eff. | Pressure Drop | Cross-Contamination |
|-------------|---------------|-------------|---------------|---------------------|
| Rotary wheel | 75-85% | 70-80% | 0.4-0.8 in. w.g. | 1-5% EATR |
| Fixed plate | 55-75% | 50-70% | 0.3-0.6 in. w.g. | <1% EATR |
| Heat pipe | 45-65% | N/A | 0.2-0.5 in. w.g. | 0% EATR |
| Run-around coil | 50-65% | N/A | 0.5-1.0 in. w.g. | 0% EATR |
| Membrane | 70-80% | 65-75% | 0.4-0.7 in. w.g. | <0.5% EATR |

Performance values at nominal design airflow with balanced flows.

## Pressure Drop Relationships

Pressure drop through ERV cores follows aerodynamic principles with relationship to airflow:

$$\Delta P = K \cdot \left(\frac{\dot{V}}{A}\right)^n$$

Where:
- $\Delta P$ = pressure drop (in. w.g.)
- $K$ = device constant (manufacturer-specific)
- $\dot{V}$ = volumetric airflow (cfm)
- $A$ = face area (ft²)
- $n$ = flow exponent (typically 1.8-2.0 for turbulent flow)

### Pressure Drop Impact on Effectiveness

Higher face velocities reduce effectiveness:

$$\epsilon_{actual} = \epsilon_{rated} \cdot \left(\frac{V_{rated}}{V_{actual}}\right)^{0.22}$$

This relationship demonstrates the 22% power law degradation typical of heat exchanger performance.

## Cross-Contamination Analysis

Exhaust air transfer ratio (EATR) quantifies unintended mixing:

$$EATR = \frac{C_{supply} - C_{outdoor}}{C_{exhaust} - C_{outdoor}}$$

Where:
- $C$ = tracer gas concentration (ppm)
- Subscripts indicate measurement location

ASHRAE 62.1 limits EATR to 10% maximum for general ventilation applications. Critical environments require EATR < 1%.

### Cross-Contamination by Device Type

Physical separation mechanisms reduce contamination:

| Separation Method | Typical EATR | Application Suitability |
|-------------------|--------------|-------------------------|
| Fixed plate | <0.5% | Healthcare, labs |
| Membrane | <0.5% | Healthcare, general |
| Heat pipe | 0% | Critical spaces |
| Run-around coil | 0% | Labs, isolation |
| Rotary wheel (purge) | 1-3% | Commercial, institutional |
| Rotary wheel (no purge) | 3-5% | General commercial |

## Performance Degradation Factors

ERV effectiveness degrades over time and with operating conditions:

### Fouling and Contamination

Particulate accumulation reduces heat transfer surface effectiveness. The fouling factor relationship:

$$\frac{1}{U_{actual}} = \frac{1}{U_{clean}} + R_f$$

Where:
- $U$ = overall heat transfer coefficient (Btu/hr·ft²·°F)
- $R_f$ = fouling resistance (hr·ft²·°F/Btu)

Typical fouling rates: 0.0005-0.002 (hr·ft²·°F/Btu) per year depending on filtration.

### Airflow Imbalance Effects

Unbalanced airflows reduce effectiveness:

$$\epsilon_{imbalanced} = \epsilon_{balanced} \cdot \left(\frac{\dot{m}_{min}}{\dot{m}_{max}}\right)^{0.78}$$

Where:
- $\dot{m}_{min}$ = lower mass flow rate (lb/min)
- $\dot{m}_{max}$ = higher mass flow rate (lb/min)

Maintain airflow balance within 10% for optimal performance.

### Frost Formation

Winter operation below 25°F outdoor temperature risks frost accumulation on cold surfaces. Frost reduces airflow area and effectiveness. Prevention strategies:

- Pre-heating outdoor air to 25°F minimum
- Recirculation bypass during defrost cycles
- Wheel speed modulation (rotary devices)
- Supply air temperature limiting

### Seal Degradation

Gasket and seal deterioration increases leakage, raising EATR and reducing effectiveness. Annual inspection recommended for gasket compression and integrity.

## Operating Point Performance

Effectiveness varies with operating conditions beyond rated points. The correction factor for non-standard conditions:

$$\epsilon_{op} = \epsilon_{std} \cdot \left(\frac{NTU_{op}}{NTU_{std}}\right)^{0.78}$$

Where NTU (Number of Transfer Units) represents the heat exchanger capacity:

$$NTU = \frac{UA}{\dot{m} \cdot c_p}$$

This relationship allows performance prediction across the operating envelope using manufacturer-provided rated data.

## Practical Application Considerations

Specify ERV performance requirements based on:

- Minimum acceptable effectiveness at design airflow
- Maximum allowable pressure drop for fan energy budget
- EATR limits per application code requirements
- Seasonal performance range for climate-specific operation
- Maintenance access for periodic cleaning and seal inspection

ASHRAE Standard 84 certified performance data ensures consistent comparison between manufacturers and devices for informed selection.
