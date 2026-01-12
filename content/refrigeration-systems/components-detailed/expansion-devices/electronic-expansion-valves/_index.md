---
title: "Electronic Expansion Valves"
description: "Advanced technical guide to electronic expansion valves (EEV) in refrigeration systems covering stepper motor technology, PWM control, superheat algorithms, and controller integration for precision refrigerant metering"
weight: 2
---

## Technical Overview

Electronic expansion valves (EEV) represent the evolution of refrigerant metering technology, replacing mechanical thermostatic expansion valves with electronically-controlled actuators. EEVs utilize electric motors to modulate valve position based on real-time system feedback, enabling precise superheat control across varying load conditions.

The fundamental advantage of EEV technology lies in its ability to maintain optimal superheat independently of thermal bulb response time and charge migration issues inherent to TXVs. This results in improved evaporator utilization, enhanced system efficiency, and superior transient response.

## Actuator Technologies

### Stepper Motor Valves

Stepper motors provide discrete positioning control through incremental angular steps, typically ranging from 100 to 500 steps for full valve travel. Each electrical pulse rotates the motor shaft a fixed angle, translating to predictable valve stem movement.

**Operating Characteristics:**

- Step resolution: 0.9° to 3.6° per step
- Holding torque: 0.5 to 2.0 Nm
- Response time: 50 to 200 ms per step
- Power consumption: 2 to 8 W continuous
- Position accuracy: ±1 step without feedback

The absence of position feedback in most stepper implementations necessitates periodic homing cycles to establish valve position reference. Stepper motors excel in applications requiring precise, repeatable positioning and tolerance to power interruption without position loss.

**Advantages:**

- Absolute position control without sensors
- High holding torque at zero speed
- Excellent low-speed stability
- No position drift during holding

**Limitations:**

- Potential for step loss under high load
- Audible noise from stepping motion
- Higher power consumption than PWM alternatives
- Limited response speed for rapid load changes

### Pulse Width Modulation (PWM)

PWM-controlled EEVs utilize DC motors with proportional valve positioning achieved through duty cycle modulation. The controller varies the ratio of on-time to off-time within a fixed cycle period, typically 1 to 10 Hz, to achieve intermediate valve positions.

**Control Parameters:**

| Parameter | Typical Range | Effect |
|-----------|--------------|--------|
| PWM Frequency | 1-10 Hz | Affects response smoothness |
| Duty Cycle | 0-100% | Determines valve opening |
| Dead Band | 2-5% | Prevents hunting |
| Minimum Pulse Width | 50-100 ms | Ensures motor response |

PWM systems require position feedback from hall effect sensors or potentiometers to achieve closed-loop control. This feedback enables compensation for refrigerant pressure forces acting on the valve mechanism.

**Advantages:**

- Smooth, continuous modulation
- Lower power consumption
- Quieter operation
- Faster response to setpoint changes

**Limitations:**

- Requires position feedback sensor
- More complex control algorithm
- Potential for electromagnetic interference
- Position loss during power failure

## Superheat Control Algorithms

EEV controllers implement various algorithms to maintain target superheat while optimizing evaporator performance and preventing compressor flooding.

### Proportional-Integral-Derivative (PID) Control

PID algorithms form the foundation of most EEV control strategies, calculating valve position based on three terms:

**Proportional Term (P):**
- Responds to current superheat error magnitude
- Gain typically 5-20 steps per degree F
- Provides immediate correction to deviations

**Integral Term (I):**
- Eliminates steady-state offset
- Integration time constant: 30-120 seconds
- Prevents sustained superheat error

**Derivative Term (D):**
- Anticipates trend direction
- Derivative time constant: 5-20 seconds
- Dampens oscillations and overshoot

| PID Parameter | Low Load | High Load | Rationale |
|--------------|----------|-----------|-----------|
| Proportional Gain | 8-12 | 15-25 | Higher gain needed at high load |
| Integral Time | 60-120 s | 30-60 s | Faster integration at high load |
| Derivative Time | 10-20 s | 5-10 s | Reduced at high load for stability |

### Adaptive Control Strategies

Advanced EEV controllers employ adaptive algorithms that modify control parameters based on operating conditions:

**Load-Based Adaptation:**
- Monitors evaporator capacity through suction pressure
- Adjusts PID gains proportionally to load
- Prevents hunting at low loads
- Maintains responsiveness at peak conditions

**Rate-of-Change Limiting:**
- Restricts maximum valve movement per time interval
- Typical limit: 5-15 steps per second
- Prevents refrigerant hammering
- Reduces compressor liquid slugging risk

**Fuzzy Logic Control:**
- Implements rule-based decision making
- Evaluates multiple inputs simultaneously
- Superheat error, rate of change, suction pressure
- Provides superior performance during transients
- Reduces tuning complexity

### Anti-Hunt Algorithms

Hunting prevention requires implementing dead bands and time delays:

- Dead band: ±1-2°F around setpoint
- Minimum dwell time: 10-30 seconds between adjustments
- Differential setpoints: open at +3°F, close at -1°F
- Prevents oscillation from measurement noise

## Controller Integration

### Sensor Inputs

EEV controllers require multiple temperature and pressure inputs for comprehensive system monitoring:

**Required Sensors:**

| Sensor | Location | Type | Accuracy |
|--------|----------|------|----------|
| Suction Temperature | Compressor inlet | Thermistor/RTD | ±0.5°F |
| Suction Pressure | Suction line | Transducer | ±1% FS |
| Liquid Temperature | TXV inlet | Thermistor | ±1°F |
| Liquid Pressure | Liquid line | Transducer | ±1% FS |

**Optional Sensors:**

- Discharge temperature for compressor protection
- Outdoor ambient for load anticipation
- Supply air temperature for capacity verification
- Return air temperature for demand calculation

### Communication Protocols

Modern EEV controllers integrate with building management systems through standard protocols:

- Modbus RTU/TCP for industrial applications
- BACnet MS/TP or IP for commercial HVAC
- LonWorks for legacy system integration
- Proprietary protocols for manufacturer-specific systems

Data points typically exposed:

- Current superheat value
- Target superheat setpoint
- Valve position (percentage or steps)
- Alarm status codes
- Operating hours
- Sensor readings

## Advantages Over Thermostatic Expansion Valves

### Performance Comparison

| Parameter | TXV | EEV | Improvement |
|-----------|-----|-----|-------------|
| Superheat Stability | ±3-5°F | ±1-2°F | 50-60% |
| Response Time | 30-90 s | 5-15 s | 70-85% |
| Evaporator Utilization | 85-90% | 92-97% | 5-8% |
| Part-Load Efficiency | Baseline | +8-15% | Significant |
| Flooded Start Protection | Limited | Excellent | Superior |

### Operational Benefits

**Enhanced System Efficiency:**
- Maintains lower superheat at all loads
- Increases evaporator capacity 5-12%
- Reduces compressor work through lower suction superheat
- Enables economizer operation optimization

**Superior Load Following:**
- Rapid response to thermal load changes
- No thermal bulb lag time
- Accurate control during pull-down
- Stable operation at low ambient conditions

**Diagnostic Capabilities:**
- Real-time performance monitoring
- Alarm generation for abnormal conditions
- Trending data for predictive maintenance
- Remote adjustment capability

**Expanded Operating Range:**
- Functions across full refrigerant charge range
- Accommodates multiple evaporator circuits
- Operates reliably at extreme ambient conditions
- Compatible with all refrigerant types

## Multiple Evaporator Control

EEV technology enables sophisticated control of systems with multiple evaporators served by a single condensing unit.

### Individual Circuit Control

Each evaporator circuit receives independent EEV and sensor set:

- Maintains optimal superheat per circuit
- Compensates for varying load distribution
- Prevents refrigerant migration between circuits
- Enables circuit-specific setpoints

### Capacity Balancing

Controller algorithms distribute refrigerant to match thermal loads:

- Monitors superheat across all circuits
- Adjusts individual EEVs to equalize utilization
- Prevents one circuit from starving others
- Maximizes total system capacity

### Circuit Staging

Sequential activation of evaporator circuits based on demand:

- Primary circuit operates continuously
- Secondary circuits stage on increasing load
- EEVs close on inactive circuits
- Prevents refrigerant accumulation in offline coils

## EEV Selection Specifications

### Capacity Rating

EEV capacity must match refrigeration system tonnage with appropriate safety margin:

| System Capacity | EEV Orifice Size | Flow Coefficient (Cv) |
|-----------------|------------------|----------------------|
| 1-3 ton | 0.040-0.060 in | 0.15-0.30 |
| 3-7 ton | 0.060-0.080 in | 0.30-0.60 |
| 7-15 ton | 0.080-0.120 in | 0.60-1.20 |
| 15-25 ton | 0.120-0.180 in | 1.20-2.50 |
| 25+ ton | 0.180+ in | 2.50+ |

### Connection Specifications

- Flare fittings: 3/8" to 7/8" SAE standard
- Sweat connections: 3/8" to 1-1/8" copper
- ODF connections for field brazing
- Body material: Brass or stainless steel
- Maximum operating pressure: 400-600 psig
- Operating temperature range: -40°F to +150°F

### Electrical Requirements

- Supply voltage: 12-24 VDC or 24 VAC
- Current draw: 0.1-0.5 A nominal
- Inrush current: 1-2 A maximum
- Signal input: 4-20 mA or 0-10 VDC
- Cable length limit: 300-1000 ft depending on signal type
- Environmental rating: NEMA 1 to NEMA 4X

## Installation Considerations

**Mounting Orientation:**
- Install in horizontal liquid line preferred
- Vertical mounting acceptable with flow upward
- Avoid low points that trap liquid refrigerant
- Provide service access to actuator

**Location Requirements:**
- Minimum 12 inches from distributor inlet
- After liquid line filter-drier
- Before evaporator distributor
- Adequate clearance for actuator removal

**Electrical Installation:**
- Shielded cable for sensor inputs
- Separate power and signal conduits
- Proper grounding to prevent noise
- Controller within 200 feet of valve preferred

## Commissioning and Tuning

### Initial Setup Procedure

1. Verify sensor installation and wiring
2. Confirm valve full-stroke operation
3. Set initial superheat target: 8-12°F
4. Configure PID parameters per manufacturer
5. Run system through load range
6. Monitor superheat stability
7. Adjust parameters as needed

### Performance Verification

- Superheat stability within ±2°F over 10 minutes
- No hunting or oscillation at steady-state
- Valve position responds to load changes
- No compressor flooding events
- Evaporator outlet temperature profile uniform

### Common Tuning Issues

| Symptom | Likely Cause | Correction |
|---------|--------------|------------|
| Hunting at low load | Proportional gain too high | Reduce P gain 20-30% |
| Sustained offset | Insufficient integral | Reduce integral time constant |
| Slow response | Proportional gain too low | Increase P gain 10-20% |
| Overshoot | Excessive derivative | Reduce derivative gain |
| Erratic behavior | Sensor noise | Add filtering, check wiring |

## Maintenance Requirements

**Routine Inspection:**
- Verify sensor readings quarterly
- Check valve position indication
- Monitor superheat trends
- Inspect electrical connections
- Clean sensor mounting surfaces

**Annual Service:**
- Verify sensor calibration
- Test valve full-stroke operation
- Review alarm history
- Update controller firmware if available
- Document performance parameters

**Troubleshooting:**
- Loss of communication: Check wiring, power supply
- Erratic superheat: Verify sensor mounting, check for leaks
- Valve stuck: Inspect for contaminants, verify power
- Hunting: Review PID parameters, check dead band settings
