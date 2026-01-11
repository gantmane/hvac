---
title: "Equipment Performance Tests"
description: "Comprehensive testing procedures for verifying HVAC equipment performance against design specifications, including chillers, boilers, air handlers, and terminal units."
date: 2025-01-05
keywords:
  - equipment performance testing
  - chiller capacity verification
  - boiler efficiency testing
  - air handler performance
  - fan coil testing
  - commissioning measurements
  - performance data comparison
  - ASHRAE 90.1 testing
weight: 1
---

Equipment performance testing validates that installed HVAC equipment operates according to manufacturer specifications and design intent. These tests form the quantitative foundation of the commissioning process, providing objective evidence that capacity, efficiency, and control performance meet project requirements.

## Performance Testing Objectives

Equipment performance tests verify:

- **Capacity delivery** at design conditions
- **Energy efficiency** compared to rated values
- **Part-load performance** across operating range
- **Control response** to varying loads
- **Safety interlock** functionality
- **Manufacturer data correlation** with field measurements

Performance testing differs from functional testing by emphasizing quantitative measurement rather than qualitative sequence verification.

## Chiller Performance Testing

Chiller performance tests measure cooling capacity and efficiency under controlled conditions.

### Capacity Verification

Measure chiller capacity using the water-side energy balance:

$$Q_{ch} = \dot{m}_{chw} c_{p,w} (T_{chwr} - T_{chws})$$

Where:
- $Q_{ch}$ = chiller cooling capacity (Btu/hr or kW)
- $\dot{m}_{chw}$ = chilled water mass flow rate (lb/hr or kg/s)
- $c_{p,w}$ = specific heat of water (1.0 Btu/lb·°F or 4.186 kJ/kg·K)
- $T_{chwr}$ = chilled water return temperature (°F or °C)
- $T_{chws}$ = chilled water supply temperature (°F or °C)

### Efficiency Measurement

Calculate chiller efficiency as coefficient of performance (COP) or kW/ton:

$$\text{COP} = \frac{Q_{ch}}{P_{comp} + P_{aux}}$$

$$\text{kW/ton} = \frac{P_{comp} + P_{aux}}{Q_{ch} / 12{,}000}$$

Where:
- $P_{comp}$ = compressor power consumption (kW)
- $P_{aux}$ = auxiliary equipment power (pumps, controls) (kW)

### Test Conditions

Conduct chiller tests at:
- **Design conditions**: Full load, design temperatures
- **AHRI conditions**: 44°F leaving chilled water, 85°F entering condenser water
- **Part-load conditions**: 75%, 50%, 25% of design capacity

Record entering and leaving water temperatures, flow rates, and power consumption at each test point. Compare measured performance to manufacturer's certified data at equivalent conditions.

## Boiler Performance Testing

Boiler performance testing quantifies thermal output and combustion efficiency.

### Thermal Output Measurement

Calculate boiler capacity from water-side measurements:

$$Q_{b} = \dot{m}_{hw} c_{p,w} (T_{hws} - T_{hwr})$$

Where:
- $Q_{b}$ = boiler heating capacity (Btu/hr or kW)
- $\dot{m}_{hw}$ = hot water mass flow rate (lb/hr or kg/s)
- $T_{hws}$ = hot water supply temperature (°F or °C)
- $T_{hwr}$ = hot water return temperature (°F or °C)

### Combustion Efficiency

Determine combustion efficiency from flue gas analysis:

$$\eta_{c} = 100 - \left[\frac{K \cdot (T_{fg} - T_{a})}{CO_2 \%}\right] - L_{m}$$

Where:
- $\eta_{c}$ = combustion efficiency (%)
- $K$ = fuel-dependent constant (natural gas: 0.535)
- $T_{fg}$ = flue gas temperature (°F)
- $T_{a}$ = ambient air temperature (°F)
- $CO_2 \%$ = carbon dioxide percentage in flue gas
- $L_{m}$ = manufacturer's radiation and convection losses (typically 1-2%)

### Testing Protocol

Boiler performance tests include:
- Full-load steady-state capacity measurement
- Combustion analysis at multiple firing rates
- Modulation range verification
- Low-fire hold stability
- Safety shutdown response
- Thermal efficiency calculation

Test at stable operating conditions after minimum 30-minute warm-up period.

## Air Handling Unit Testing

AHU performance testing verifies airflow delivery, temperature control, and pressure performance.

### Airflow Verification

Measure total airflow using:
- **Traverse measurements** in duct cross-sections
- **Fan inlet flow stations** with calibrated averaging arrays
- **Pressure-flow calculations** from fan curves

Calculate delivered airflow from traverse data:

$$Q = A \cdot V_{avg} \cdot 60$$

Where:
- $Q$ = volumetric flow rate (cfm)
- $A$ = duct cross-sectional area (ft²)
- $V_{avg}$ = average velocity from traverse (ft/min)

### Cooling/Heating Capacity

Determine AHU capacity from air-side energy balance:

$$Q_{AHU} = 1.08 \cdot Q \cdot (T_{ea} - T_{sa})$$

Where:
- $Q_{AHU}$ = sensible capacity (Btu/hr)
- $Q$ = airflow rate (cfm)
- $T_{ea}$ = entering air temperature (°F)
- $T_{sa}$ = supply air temperature (°F)

### Performance Metrics

Evaluate AHU performance against:
- **Design airflow** at rated external static pressure
- **Temperature difference** across coils at design conditions
- **Fan power consumption** compared to nameplate data
- **Filter pressure drop** at design airflow

## Fan Coil and Terminal Unit Testing

Terminal equipment testing verifies local zone conditioning capacity.

### Fan Coil Performance

Test fan coil units by measuring:
- Airflow at each speed setting
- Entering and leaving air temperatures
- Water-side temperature difference and estimated flow
- Sound levels in occupied space

Calculate approximate capacity:

$$Q_{fc} = 1.08 \cdot Q_{fc,air} \cdot \Delta T_{air}$$

### VAV Box Testing

VAV terminal unit tests include:
- Minimum and maximum airflow set points
- Flow tracking accuracy across modulating range
- Reheat coil capacity (if applicable)
- Damper response time
- Controller accuracy

## Manufacturer Data Comparison

Compare field measurements to manufacturer's certified performance data:

1. **Normalize conditions**: Adjust field measurements to manufacturer's test conditions using correction factors
2. **Tolerance evaluation**: Apply ASHRAE Guideline 0 tolerances (typically ±5% for capacity, ±10% for efficiency)
3. **Trending analysis**: Plot multiple test points against performance curves
4. **Deficiency documentation**: Record and report equipment not meeting specifications

## Standards and References

Equipment performance testing follows:

- **ASHRAE Guideline 0**: The Commissioning Process (testing tolerances)
- **ASHRAE Standard 90.1**: Energy Standard for Buildings (minimum efficiency requirements)
- **ASHRAE Guideline 1.1**: HVAC&R Technical Requirements for The Commissioning Process
- **NEBB Procedural Standards**: Testing and balancing measurement protocols
- **AHRI Standards**: Equipment performance rating conditions

Performance test results provide verification that equipment installations meet both design intent and minimum code requirements, forming essential documentation for project acceptance and building operation.
