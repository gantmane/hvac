---
title: "Fan Performance"
aliases: ["Fan Performance"]
description: "Understanding fan performance curves, efficiency, and operating characteristics for optimal HVAC system design and operation."
keywords: ["fan performance", "fan curves", "static pressure", "total pressure", "fan efficiency", "operating point"]
tags: ["fan performance", "fan curves", "static pressure", "total pressure", "fan efficiency", "operating point"]
weight: 3
---

Fan performance characteristics determine how effectively fans move air through HVAC systems. Understanding performance curves, efficiency factors, and operating behavior enables optimal fan selection and system operation.

## Fan Performance Curves

### Fan Curve Components

A complete fan performance curve includes:

1. **Pressure-Volume Curve**: Static or total pressure vs. CFM
2. **Power Curve**: BHP vs. CFM
3. **Efficiency Curve**: Mechanical efficiency vs. CFM
4. **Operating Region**: Stable operation zone

### Static Pressure vs. Total Pressure

**Total Pressure**:
$$P_T = P_S + P_V$$

**Velocity Pressure**:
$$P_V = \frac{\rho V^2}{2g} = \left(\frac{V}{4005}\right)^2$$ (inches w.g., standard air)

**Fan Total Pressure (FTP)**:
$$FTP = TP_{outlet} - TP_{inlet}$$

**Fan Static Pressure (FSP)**:
$$FSP = FTP - VP_{outlet}$$

### Curve Shapes by Fan Type

| Fan Type | Curve Shape | Characteristics |
|----------|-------------|-----------------|
| Forward-curved | Steep, S-shaped | Peak pressure left of peak CFM |
| Backward-curved | Flatter, smoother | Gradual pressure drop |
| Axial | Dip in middle | Stall region visible |
| Radial | Relatively flat | High shutoff pressure |

## Operating Point

### System Curve

The system resistance curve represents duct and component losses:

$$\Delta P_{sys} = K_{sys} \times Q^2$$

Where $K_{sys}$ is the system resistance coefficient.

### Finding Operating Point

The fan operates where fan curve intersects system curve:

$$P_{fan}(Q) = P_{sys}(Q)$$

This intersection point defines:
- Delivered airflow (CFM)
- Developed pressure
- Required power
- Operating efficiency

### Operating Point Shifts

**Increased System Resistance**:
- System curve steepens
- Operating point moves left on fan curve
- Airflow decreases
- Pressure increases

**Decreased System Resistance**:
- System curve flattens
- Operating point moves right
- Airflow increases
- Pressure decreases

## Fan Efficiency

### Definitions

**Total Efficiency**:
$$\eta_T = \frac{Q \times P_T}{6356 \times BHP}$$ (Q in CFM, P in in. w.g.)

**Static Efficiency**:
$$\eta_S = \frac{Q \times P_S}{6356 \times BHP}$$

### Peak Efficiency Point

Maximum efficiency occurs at specific flow rate:
- Design near peak efficiency
- Avoid operation far from peak
- Efficiency drops at extremes

**Typical Peak Efficiencies**:
| Fan Type | Peak Total Efficiency |
|----------|----------------------|
| BC Airfoil | 80-88% |
| BC Inclined | 75-82% |
| Vane-Axial | 70-82% |
| FC Centrifugal | 65-75% |
| Radial | 55-70% |
| Propeller | 40-60% |

### Brake Horsepower

Power at the fan shaft:

$$BHP = \frac{Q \times P_T}{6356 \times \eta_T}$$

Include motor efficiency for electrical input:

$$kW_{input} = \frac{BHP \times 0.746}{\eta_{motor}}$$

## Surge and Stall

### Centrifugal Fan Surge

Surge occurs when operating left of peak pressure:
- Periodic flow reversal
- Noise and vibration
- Potential damage
- Unstable operation

**Avoid** operation in surge region (typically left 1/3 of curve).

### Axial Fan Stall

Stall occurs at high pressure/low flow:
- Blade flow separation
- Sharp efficiency drop
- Noise increase
- Performance instability

Stall region visible as curve "dip" on axial fan performance.

### Selection Guidelines

**Safe Operating Range**:
- Centrifugal: Right of peak pressure
- Axial: Right of stall dip
- Allow margin for system variations

## Performance at Non-Standard Conditions

### Altitude Effects

At elevation, air density decreases:

$$\rho_{alt} = \rho_{std} \times \frac{P_{baro}}{P_{std}}$$

Fan delivers same CFM but:
- Reduced pressure capability
- Reduced power consumption
- Same mass flow requires higher CFM

### Temperature Effects

Hot air is less dense:

$$\rho_T = \rho_{std} \times \frac{T_{std}}{T_{actual}}$$ (absolute temps)

Correct published curves for actual density.

### Correction Example

Given: Fan curve at standard conditions
Need: Performance at 5,000 ft, 120°F

Density ratio:
$$\frac{\rho_{actual}}{\rho_{std}} = 0.83 \times \frac{530}{580} = 0.76$$

Corrected pressure: Published × 0.76
Corrected power: Published × 0.76

## Multiple Fan Operation

### Fans in Parallel

Same pressure, combined flow:

$$Q_{total} = Q_1 + Q_2$$
$$P_{total} = P_{individual}$$

**Requirements**:
- Similar fans recommended
- System curve determines actual split
- Ensure both operate in stable region

### Fans in Series

Same flow, combined pressure:

$$P_{total} = P_1 + P_2$$
$$Q_{total} = Q_{individual}$$

**Considerations**:
- Second fan handles heated air
- Derate second fan for temperature
- Used for high-pressure systems

## Performance Testing

### AMCA Standard Testing

AMCA 210/ASHRAE 51 specifies test methods:
- Multi-nozzle chamber
- Pitot traverse
- Various configurations

Test conditions:
- Standard air: 0.075 lb/ft³
- Sea level pressure
- 70°F temperature

### Field Testing

Verify installed performance:
- Pitot traverse in duct
- Measure motor amps
- Calculate actual CFM and BHP
- Compare to published curves

### Performance Verification

$$CFM = V_{avg} \times A_{duct}$$

$$BHP = \frac{V \times I \times PF \times \eta_{motor}}{746}$$ (single phase)

Compare actual to design, accounting for system effect.

## Specification Considerations

### Selecting Operating Point

1. Calculate system CFM requirement
2. Determine system static pressure
3. Add safety factor (10-20%)
4. Plot on fan curve
5. Verify efficiency and power
6. Ensure stable operation region

### Rating Tolerances

AMCA certified fans meet tolerance requirements:
- Airflow: ±10% at rated pressure
- Pressure: ±10% at rated flow
- Peak efficiency: -5%

Understanding fan performance characteristics enables selection of fans that efficiently deliver required airflow at design pressure while operating reliably within their stable performance range.
