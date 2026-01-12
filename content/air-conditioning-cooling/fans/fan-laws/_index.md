---
title: "Fan Laws"
description: "Application of fan affinity laws for predicting HVAC fan performance changes with speed, size, and density variations."
keywords: ["fan laws", "affinity laws", "fan performance", "fan speed", "system curve", "HVAC design"]
weight: 2
---

Fan laws, also known as affinity laws, describe the mathematical relationships between fan performance variables. These fundamental relationships enable engineers to predict how changes in speed, size, or air density affect airflow, pressure, and power consumption.

## The Three Fan Laws

### Law 1: Flow is Proportional to Speed

$$\frac{Q_2}{Q_1} = \frac{N_2}{N_1}$$

Airflow (CFM) varies directly with rotational speed (RPM).

**Example**: 10% speed increase → 10% flow increase

### Law 2: Pressure is Proportional to Speed Squared

$$\frac{P_2}{P_1} = \left(\frac{N_2}{N_1}\right)^2$$

Static or total pressure varies with the square of speed.

**Example**: 10% speed increase → 21% pressure increase

### Law 3: Power is Proportional to Speed Cubed

$$\frac{W_2}{W_1} = \left(\frac{N_2}{N_1}\right)^3$$

Fan power (HP or kW) varies with the cube of speed.

**Example**: 10% speed increase → 33% power increase

## Combined Relationships

### Speed Change Summary

For any speed ratio:

| Variable | Relationship | 10% Speed ↑ | 20% Speed ↓ |
|----------|--------------|-------------|-------------|
| Flow | Linear | +10% | -20% |
| Pressure | Squared | +21% | -36% |
| Power | Cubed | +33% | -49% |

### Practical Formula

$$\frac{W_2}{W_1} = \left(\frac{Q_2}{Q_1}\right)^3$$

Power varies as the cube of flow ratio.

## Size Scaling Laws

When geometrically similar fans operate at the same tip speed:

### Diameter Relationships

$$\frac{Q_2}{Q_1} = \left(\frac{D_2}{D_1}\right)^3$$

$$\frac{P_2}{P_1} = \left(\frac{D_2}{D_1}\right)^2$$

$$\frac{W_2}{W_1} = \left(\frac{D_2}{D_1}\right)^5$$

### Combined Speed and Size

For both speed and diameter changes:

$$Q_2 = Q_1 \left(\frac{N_2}{N_1}\right) \left(\frac{D_2}{D_1}\right)^3$$

$$P_2 = P_1 \left(\frac{N_2}{N_1}\right)^2 \left(\frac{D_2}{D_1}\right)^2$$

$$W_2 = W_1 \left(\frac{N_2}{N_1}\right)^3 \left(\frac{D_2}{D_1}\right)^5$$

## Air Density Effects

### Density Correction

Fan curves are published at standard conditions (0.075 lb/ft³ or sea level). Actual density affects pressure and power:

$$\frac{P_2}{P_1} = \frac{\rho_2}{\rho_1}$$

$$\frac{W_2}{W_1} = \frac{\rho_2}{\rho_1}$$

**Note**: Volumetric flow (CFM) remains unchanged; mass flow changes with density.

### Altitude Effects

Density decreases with altitude:

$$\rho_{alt} = \rho_{SL} \times \frac{P_{alt}}{P_{SL}}$$

| Altitude | Density Ratio | Pressure/Power Factor |
|----------|---------------|----------------------|
| Sea level | 1.00 | 1.00 |
| 2,000 ft | 0.93 | 0.93 |
| 5,000 ft | 0.83 | 0.83 |
| 10,000 ft | 0.69 | 0.69 |

### Temperature Effects

Higher temperature reduces density:

$$\rho_2 = \rho_1 \times \frac{T_1}{T_2}$$ (absolute temperature)

**Example**: 70°F to 120°F
$$\frac{\rho_2}{\rho_1} = \frac{530}{580} = 0.91$$

## System Curve Interaction

### System Curve Equation

System resistance follows a parabolic relationship:

$$\Delta P_{sys} = K \times Q^2$$

Where K = system resistance constant

### Fan/System Operating Point

The operating point occurs where fan curve intersects system curve:

$$P_{fan}(Q) = P_{sys}(Q)$$

### Speed Change on System

When fan speed changes, the new operating point follows the system curve:

$$\frac{Q_2}{Q_1} = \sqrt{\frac{P_2}{P_1}}$$ (on same system curve)

This matches the fan law relationship, confirming the operating point.

## Practical Applications

### Variable Speed Energy Savings

Reducing flow from 100% to 80% with VFD:

| Flow | Speed | Pressure | Power |
|------|-------|----------|-------|
| 100% | 100% | 100% | 100% |
| 80% | 80% | 64% | 51% |
| 60% | 60% | 36% | 22% |
| 40% | 40% | 16% | 6% |

**Substantial energy savings** at reduced flow!

### Comparison: Speed vs. Damper Control

At 60% airflow:

**VFD Control**: 22% power (per fan laws)
**Discharge Damper**: 70-80% power (throttling losses)
**Inlet Vane**: 55-65% power (pre-rotation)

VFD provides best energy savings.

### System Changes

Fan laws apply to fan changes, not system changes:

**Correct**: Changing fan speed
**Not Applicable**: Adding system resistance

When system resistance increases, use fan curve to find new operating point.

## Limitations

### Geometrically Similar Fans Only

Size laws require geometric similarity:
- Same blade angles
- Same hub ratio
- Same proportions

Scaling between dissimilar fans requires testing.

### Stable Operating Range

Fan laws assume operation in stable region:
- Right of surge/stall
- Away from shutoff
- On published curve region

### Efficiency Changes

Fan laws assume constant efficiency. In reality:
- Peak efficiency at one point
- Efficiency drops at off-design
- VFD may affect motor efficiency

### System Effect Not Included

Fan laws describe fan-only behavior:
- System effect losses add separately
- Installation conditions matter
- Actual performance may differ

## Example Calculations

### Speed Change

Given: 10,000 CFM at 4" w.g., 8 HP at 1,000 RPM

Find performance at 800 RPM:

$$Q_2 = 10,000 \times \frac{800}{1000} = 8,000\ CFM$$

$$P_2 = 4 \times \left(\frac{800}{1000}\right)^2 = 2.56"\ w.g.$$

$$W_2 = 8 \times \left(\frac{800}{1000}\right)^3 = 4.1\ HP$$

### Required Speed for Target Flow

Given: Need 12,000 CFM from 10,000 CFM fan at 1,000 RPM

$$N_2 = 1000 \times \frac{12,000}{10,000} = 1,200\ RPM$$

Verify motor and fan can handle increased speed, pressure, and power.

Fan laws provide essential tools for analyzing fan performance changes, enabling accurate prediction of airflow, pressure, and power across operating conditions for optimized HVAC system design and operation.
