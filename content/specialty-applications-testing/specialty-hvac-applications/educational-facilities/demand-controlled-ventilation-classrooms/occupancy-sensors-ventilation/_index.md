---
title: "Occupancy Sensors for Classroom Ventilation Control"
description: "Technical analysis of PIR, ultrasonic, and hybrid occupancy sensors for demand-controlled ventilation in educational facilities including integration strategies."
date: 2025-01-05
weight: 2
keywords:
  - occupancy sensors ventilation
  - PIR sensors HVAC
  - ultrasonic occupancy detection
  - demand controlled ventilation sensors
  - classroom occupancy sensing
  - HVAC sensor integration
  - ventilation control sensors
  - educational facility sensors
---

# Occupancy Sensors for Classroom Ventilation Control

Occupancy sensors provide real-time detection of room occupancy for demand-controlled ventilation (DCV) systems in educational facilities. Proper sensor selection, placement, and integration directly affect ventilation effectiveness, energy efficiency, and indoor air quality in classroom environments.

## Sensor Technology Types

### Passive Infrared (PIR) Sensors

PIR sensors detect infrared radiation emitted by occupants. The sensor responds to temperature differentials caused by human body heat moving across detection zones.

**Operating principles:**
- Detect thermal radiation in 8-12 μm wavelength range
- Require motion for detection (static occupants may not be detected)
- Multiple detection zones increase coverage reliability
- Temperature differences between occupants and background affect sensitivity

**Typical specifications:**
- Detection range: 20-40 feet radius
- Field of view: 90-180 degrees
- Response time: 1-2 seconds
- Operating temperature: 32-120°F

**Application considerations:**
- Effective in spaces with moderate occupant movement
- Less reliable for seated classrooms during testing
- Performance degrades when room temperature approaches body temperature
- Line-of-sight required to detection zones

### Ultrasonic Sensors

Ultrasonic sensors emit high-frequency sound waves (typically 25-40 kHz) and detect frequency shifts caused by moving objects using the Doppler effect.

**Operating principles:**
- Emit ultrasonic waves that reflect off surfaces and occupants
- Detect frequency changes from moving objects
- Sound waves propagate around obstacles
- More sensitive to minor movements than PIR

**Typical specifications:**
- Detection range: 30-50 feet radius
- Coverage pattern: omnidirectional
- Frequency: 25-40 kHz
- Response time: 2-5 seconds

**Application considerations:**
- Detect occupants through partitions and obstacles
- May false-trigger from air movement, HVAC operation
- Require careful gain adjustment to prevent false positives
- Effective for spaces with minimal occupant movement

### Hybrid (Dual-Technology) Sensors

Hybrid sensors combine PIR and ultrasonic technologies, requiring both technologies to confirm occupancy before triggering. This configuration significantly reduces false positives and false negatives.

**Operating logic:**
- Both sensors must detect presence for "occupied" status
- Either sensor can maintain "occupied" status once established
- Provides redundancy for reliable detection
- Optimizes detection while minimizing false triggers

## Sensor Type Comparison

| Parameter | PIR | Ultrasonic | Hybrid |
|-----------|-----|------------|--------|
| Detection method | Thermal radiation | Sound reflection | Both combined |
| Minor motion sensitivity | Low | High | High |
| False positive rate | Low | Moderate | Very low |
| False negative rate | Moderate | Low | Very low |
| Coverage through obstacles | No | Yes | Yes |
| Relative cost | $ | $$ | $$$ |
| Classroom suitability | Moderate | Good | Excellent |
| Maintenance requirements | Low | Low | Low |
| Typical lifespan | 10-15 years | 10-15 years | 10-15 years |

## Integration with HVAC Controls

### Control Strategies

**Binary occupancy control:**
- Occupied: Full ventilation rate per ASHRAE 62.1 or IMC Section 403
- Unoccupied: Reduced ventilation (typically 0.06 cfm/ft² or complete shutoff where permitted)
- Simple two-position control logic
- Most common implementation

**Time-delay settings:**
- On-delay: 30-60 seconds (prevents short-duration false triggers)
- Off-delay: 15-30 minutes (accounts for brief departures, sensor blind spots)
- Longer off-delays recommended for classrooms to prevent unnecessary cycling

**Gradual setback:**
- Progressive reduction in ventilation rate after occupancy loss
- Maintains minimum ventilation for contaminant dilution
- Reduces thermal shock and acoustic disturbances from equipment cycling

### BAS Integration

Occupancy sensors integrate with building automation systems through multiple protocols:

**Communication methods:**
- Hardwired relay contacts (24 VAC common)
- 0-10 VDC analog signal
- BACnet MS/TP or BACnet IP
- Modbus RTU or Modbus TCP
- Proprietary protocols (manufacturer-specific)

**Data points transmitted:**
- Occupancy status (binary or analog)
- Sensor diagnostics
- Battery status (wireless sensors)
- Configuration parameters

### Control Sequence Coordination

Occupancy-based ventilation control must coordinate with other HVAC functions:

1. **Temperature control:** Maintain setpoint during occupied periods; implement setback during unoccupied periods
2. **CO₂ monitoring:** Occupancy sensors provide supplementary control when CO₂ sensors are primary
3. **Scheduling:** Override schedule-based control when occupancy detected outside scheduled hours
4. **Demand reset:** Adjust outdoor air damper positions based on actual occupancy versus design occupancy

## Sensor Placement Requirements

**Optimal mounting locations:**
- Ceiling-mounted: 8-12 feet height for standard classrooms
- Wall-mounted: 6-8 feet height when ceiling mounting not feasible
- Corner placement maximizes coverage area
- Avoid mounting near supply air diffusers (air movement causes false triggers)

**Coverage patterns:**
- Single sensor typically covers 400-600 ft² classroom
- Multiple sensors required for irregular room geometries
- Overlap coverage zones 10-15% to eliminate detection gaps
- Consider furniture layout and potential obstructions

**Code-compliant installation:**
- Sensors must detect occupancy in all normally occupied areas
- Comply with ASHRAE 62.1 Section 6.2.7 (demand-controlled ventilation)
- Meet International Mechanical Code Section 403.3.1.1 (ventilation controls)
- Coordinate with IECC Section C403.2.7 (demand control ventilation requirements)

## Accuracy and Reliability Factors

**Environmental conditions affecting performance:**
- Extreme temperatures reduce PIR sensitivity
- High air velocities cause ultrasonic false triggers
- Lighting changes affect some optical sensors
- Electromagnetic interference from equipment

**Calibration and commissioning:**
- Verify detection coverage through walk tests
- Adjust sensitivity and time delays for application
- Document sensor placement and detection zones
- Test under various occupancy scenarios (standing, seated, minimal movement)

**Maintenance requirements:**
- Inspect lenses quarterly for dust, debris, damage
- Verify operation during normal occupancy patterns
- Recalibrate after room layout changes
- Replace batteries annually (wireless sensors)

## Best Practices

- Specify hybrid sensors for critical classroom applications requiring high reliability
- Implement minimum 15-minute off-delay to account for brief absences and sensor limitations
- Coordinate occupancy-based control with CO₂-based DCV for optimal performance
- Commission sensors under actual occupancy conditions, not just empty rooms
- Provide override switches for manual control during sensor failures
- Document sensor locations and coverage patterns in building automation system
- Train facility staff on occupancy sensor operation and troubleshooting
- Review actual vs. design occupancy patterns after first year of operation

Properly selected and integrated occupancy sensors enable significant energy savings in educational facilities while maintaining code-compliant ventilation rates and acceptable indoor air quality during occupied periods.
