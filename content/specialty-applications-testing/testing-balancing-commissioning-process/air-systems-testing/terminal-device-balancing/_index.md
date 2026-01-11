---
title: "Terminal Device Balancing Procedures"
description: "Comprehensive guide to balancing diffusers, registers, and grilles using Ak factors, capture hoods, and flow traverse methods per AABC and NEBB standards."
date: 2025-01-05
weight: 3
tags: ["terminal device balancing", "Ak factor", "capture hood", "flow traverse", "diffuser balancing", "register balancing", "air balancing procedures", "AABC standards"]
---

# Terminal Device Balancing

Terminal device balancing represents the final stage of air system balancing, ensuring that each supply and return outlet delivers design airflow rates. This process requires precise measurement techniques, proper application of correction factors, and systematic adjustment procedures to achieve specified performance.

## Terminal Device Classification

Terminal devices are classified by function and measurement characteristics:

**Supply devices:**
- Ceiling diffusers (round, square, linear slot)
- Sidewall grilles and registers
- Floor registers
- High-induction diffusers
- Low-induction diffusers

**Return and exhaust devices:**
- Return air grilles
- Exhaust grilles
- Transfer grilles
- Door louvers

## Measurement Methods

### Capture Hood Method

Capture hoods provide direct volumetric flow measurement by capturing the entire terminal device discharge. The method offers rapid measurements but requires correction for device effects.

**Advantages:**
- Quick field measurements
- No interference with occupied spaces
- Suitable for most ceiling diffusers
- Direct reading in CFM

**Limitations:**
- Accuracy dependent on device type
- Manufacturer-specific correction factors required
- Hood size constraints
- Limited accuracy for high-velocity devices (>500 FPM face velocity)

**Procedure:**
1. Ensure hood capture area encompasses entire device discharge pattern
2. Maintain firm seal against ceiling surface
3. Record stabilized reading (minimum 15 seconds)
4. Apply manufacturer correction factors
5. Document device model and orientation

### Flow Traverse Method

Flow traverse measurements determine average velocity through the device by sampling velocity at multiple points across the face area.

**Traverse point determination:**

For rectangular grilles, the minimum number of traverse points follows ASHRAE guidelines:

$$N_{points} = \frac{A_{face}}{144}$$

where $N_{points}$ is rounded to the nearest equal-area grid pattern (minimum 9 points) and $A_{face}$ is face area in square inches.

**Calculated airflow:**

$$Q = V_{avg} \times A_{free} \times 60$$

where:
- $Q$ = airflow (CFM)
- $V_{avg}$ = arithmetic average velocity from all traverse points (FPM)
- $A_{free}$ = free area (square feet)

## Ak Factor Application

The Ak factor relates terminal device pressure drop to airflow, providing a device-specific characteristic used for field measurements with manometers.

### Ak Factor Definition

$$Q = A_k \times \sqrt{\Delta P}$$

where:
- $Q$ = airflow (CFM)
- $A_k$ = Ak factor (manufacturer-supplied constant)
- $\Delta P$ = pressure drop across device (inches w.g.)

### Determining Ak Factors

**From manufacturer data:**

Most manufacturers provide Ak factors for standard devices at specified blade or vane positions. Ak factors typically range from 50 to 500 depending on device size and geometry.

**Field calibration:**

When manufacturer data is unavailable, field calibration establishes Ak factors:

1. Measure actual airflow using calibrated flow traverse
2. Simultaneously measure pressure drop across device
3. Calculate Ak factor:

$$A_k = \frac{Q_{measured}}{\sqrt{\Delta P_{measured}}}$$

**Pressure tap placement:**

- Supply devices: static pressure between duct and device inlet
- Return/exhaust devices: static pressure between device and duct connection
- Maintain minimum 2.5 duct diameters upstream of measurement
- Install taps perpendicular to airflow

### Ak Factor Application Ranges

Ak factors remain constant only within specific operational ranges:

| Device Type | Valid Reynolds Number Range | Typical Ak Range |
|-------------|----------------------------|------------------|
| Ceiling diffusers | Re > 10,000 | 80-250 |
| Registers (opposed blade) | Re > 8,000 | 100-400 |
| Grilles (fixed blade) | Re > 12,000 | 150-500 |
| Slot diffusers | Re > 15,000 | 60-180 |

Below minimum Reynolds numbers, compressibility effects and laminar flow components invalidate Ak factors.

## Balancing Procedures

### Supply Diffuser Balancing

**Step-by-step procedure:**

1. **Initial survey:**
   - Measure airflow at each diffuser using capture hood or flow traverse
   - Document existing damper positions
   - Calculate total branch airflow
   - Identify terminal devices farthest from air handler (index terminals)

2. **Proportional balancing:**
   - Begin with all balancing dampers fully open
   - Adjust main branch damper to achieve design flow at index diffuser
   - Balance remaining diffusers proportionally by restricting dampers
   - Work from terminals farthest from source toward air handler

3. **Final adjustment:**
   - Re-measure all terminal flows after initial balance
   - Make fine adjustments to achieve design flows ±10%
   - Verify minimum system pressure drop
   - Document final damper positions

4. **Verification:**
   - Confirm total branch flow matches design within ±5%
   - Check that no individual terminal exceeds ±10% tolerance
   - Measure sound levels at critical locations
   - Lock dampers in final positions

### Register and Grille Balancing

Sidewall registers and return grilles require additional considerations due to asymmetric flow patterns.

**Measurement protocol:**

For sidewall registers, position measuring hood or traverse grid perpendicular to primary air jet direction. Flow traverse measurements should sample the core region where velocity exceeds 50% of maximum.

**Damper adjustment sequence:**

1. Adjust volume dampers (if provided) before face dampers
2. Use opposed-blade dampers for flow control
3. Avoid extreme damper positions (<20% open or >90% open)
4. Maintain minimum 100 FPM face velocity for proper air distribution

## Field Measurement Accuracy

### Error Sources and Mitigation

**Capture hood errors:**
- Device geometry effects: ±5-15% depending on diffuser type
- Seal leakage: ±3-8%
- Hood flow sensor calibration: ±3%

**Mitigation strategies:**
- Use manufacturer-specific correction factors
- Verify capture hood calibration annually
- Ensure complete sealing against ceiling
- Cross-check critical measurements with traverse methods

**Flow traverse errors:**
- Point sampling resolution: ±4-10%
- Velocity sensor accuracy: ±2-5%
- Free area uncertainty: ±3-6%

**Mitigation strategies:**
- Increase traverse points for large devices
- Use calibrated velocity probes
- Verify manufacturer free area data

## Standards and Tolerances

### AABC and NEBB Requirements

**AABC (Associated Air Balance Council) tolerances:**
- Individual terminals: ±10% of design
- System totals: ±5% of design
- Measurement accuracy: ±5% of reading

**NEBB (National Environmental Balancing Bureau) tolerances:**
- Supply terminals: ±10% of design (minimum 50 CFM)
- Return/exhaust terminals: ±10% of design
- Total system flow: ±10% of design

**Documentation requirements:**

Both organizations mandate comprehensive reporting including:
- Device location and identification
- Design versus measured airflow
- Damper positions (percentage or turns from closed)
- Measurement method and instrumentation
- Correction factors applied
- Final system performance summary

### Manufacturer Specifications

Terminal device performance depends on installation conditions matching manufacturer test parameters:

- Static pressure range: devices perform per catalog data only within specified inlet pressure ranges (typically 0.05-0.50 inches w.g.)
- Duct connection: flexible duct connections reduce diffuser performance by 10-25%
- Clearance requirements: minimum clearance above ceiling diffusers (typically 12-24 inches)
- Mounting orientation: sidewall devices require proper alignment with airflow patterns

## Special Considerations

### High-Velocity Devices

Terminal devices operating above 2,000 FPM face velocity require specialized measurement approaches:

- Capture hood measurements become unreliable above 500 FPM hood face velocity
- Use Pitot-static traverse with minimum 16 measurement points
- Apply compressibility corrections for velocities exceeding 10,000 FPM
- Verify sound power levels against NC/RC criteria

### Variable Air Volume Terminals

VAV terminal balancing requires measurements at multiple flow conditions:

- Maximum cooling airflow (design condition)
- Minimum cooling airflow (turndown condition, typically 30-50% of maximum)
- Heating airflow (if applicable)
- Verify controls response and damper authority at each condition

Ak factors may vary with VAV damper position; establish calibration curves across the operational range for precision balancing.
