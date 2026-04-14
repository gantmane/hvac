---
title: "Demand-Controlled Ventilation (DCV)"
aliases: ["Demand-Controlled Ventilation (DCV)"]
description: "Demand-controlled ventilation strategies for educational facilities including CO2-based control, occupancy sensing, and energy optimization."
keywords: ["demand-controlled ventilation", "DCV", "CO2 sensing", "school ventilation", "educational facilities", "energy efficiency"]
tags: ["demand-controlled ventilation", "DCV", "CO2 sensing", "school ventilation", "educational facilities", "energy efficiency"]
weight: 5
---

Demand-controlled ventilation (DCV) adjusts outdoor air supply based on actual occupancy, providing energy savings while maintaining indoor air quality in educational facilities with highly variable occupancy patterns.

## DCV Fundamentals

### Operating Principle

DCV modulates ventilation based on occupancy indicators:

$$\dot{V}_{OA} = \dot{V}_{min} + K \times (Indicator - Baseline)$$

Where:
- $\dot{V}_{OA}$ = outdoor air flow rate
- $\dot{V}_{min}$ = minimum (unoccupied) ventilation
- K = proportional gain
- Indicator = CO₂, occupancy count, or other

### Occupancy Detection Methods

| Method | Technology | Response Time | Accuracy |
|--------|------------|---------------|----------|
| CO₂ sensing | NDIR sensors | Minutes | Good for groups |
| Occupancy counting | Video, infrared | Immediate | Very accurate |
| Schedule-based | Time clock | Pre-programmed | Variable |
| Motion detection | PIR sensors | Immediate | Presence only |

### CO₂ as Proxy

CO₂ concentration indicates occupancy:

$$CO_2 = CO_{2,outdoor} + \frac{N \times G}{Q}$$

Where:
- N = number of occupants
- G = CO₂ generation rate (~0.31 L/min for adults)
- Q = ventilation rate

**ASHRAE 62.1 Basis**:
- 1,000 ppm indoor = approximately 15 CFM/person
- 800 ppm differential above outdoor

## Educational Facility Applications

### Classroom Implementation

Classrooms experience predictable but variable occupancy:

**Typical Pattern**:
- Empty: Before school, after hours
- Partial: Study halls, small groups
- Full: Standard class periods
- Peak: Special events

**DCV Benefits**:
- 30-50% ventilation energy savings
- Automatic response to actual occupancy
- Maintained IAQ regardless of schedule changes

### Assembly Spaces

Gyms, auditoriums, cafeterias with highly variable loads:

**Characteristics**:
- Very low to maximum occupancy
- Short notice events
- Extended vacancy periods

**DCV Essential**: Fixed ventilation would be grossly oversized or undersized.

### Laboratory Spaces

Science labs with fume hood requirements:
- DCV for general area when hoods satisfy minimum OA
- Coordinate with exhaust requirements
- Maintain proper pressure relationships

## System Design

### CO₂ Sensor Placement

Proper sensor location critical:

**Recommended Locations**:
- 3-6 ft above floor (breathing zone)
- Away from supply diffusers
- Away from doors and windows
- Minimum 3 ft from occupants
- Representative of space conditions

**Avoid**:
- Direct sunlight
- Near HVAC equipment
- Stagnant areas
- High traffic paths

### Control Strategies

**Single-Zone DCV**:
- One sensor controls one zone
- Simplest implementation
- Common for classrooms

**Multi-Zone DCV**:
- Multiple zones share AHU
- Critical zone reset
- System-level optimization

$$\dot{V}_{OA,system} = \frac{\sum \dot{V}_{OA,zone}}{E_v}$$

Where $E_v$ = system ventilation effectiveness

### Setpoint Selection

| Space Type | Target CO₂ | Minimum OA |
|------------|------------|------------|
| Classrooms | 800-1,000 ppm | 5 CFM/person + 0.06 CFM/ft² |
| Gymnasium | 800-1,000 ppm | 7.5 CFM/person + 0.06 CFM/ft² |
| Cafeteria | 800-1,000 ppm | 7.5 CFM/person + 0.18 CFM/ft² |
| Library | 800-1,000 ppm | 5 CFM/person + 0.06 CFM/ft² |

## Equipment Requirements

### CO₂ Sensors

**Sensor Specifications**:
- Technology: NDIR (non-dispersive infrared)
- Range: 0-2,000 ppm minimum
- Accuracy: ±50 ppm or ±3%
- Output: 4-20 mA or BACnet

**Calibration**:
- Factory calibration
- Annual verification
- Automatic baseline correction (ABC)
- Fresh air calibration option

### Damper Actuators

Outdoor air dampers for DCV:
- Modulating capability (0-100%)
- Characterized for linear flow
- Fast response (<60 seconds)
- Reliable positioning feedback

### Control Integration

BAS programming requirements:
- PID control loops
- Minimum/maximum limits
- Alarm generation
- Trend logging
- Override capability

## Energy Savings

### Savings Calculation

$$Savings = \sum_{hours} (\dot{V}_{OA,design} - \dot{V}_{OA,actual}) \times \Delta h \times Cost$$

Where:
- $\Delta h$ = enthalpy difference
- Cost = energy cost per unit

### Typical Savings

| Climate | Occupancy Variation | Typical Savings |
|---------|-------------------|-----------------|
| Heating-dominated | High | 20-40% |
| Cooling-dominated | High | 15-30% |
| Mild | Moderate | 10-20% |

### Payback Analysis

Simple payback typically 1-3 years:

$$Payback = \frac{Sensor + Installation + Commissioning}{Annual\ Energy\ Savings}$$

## Code Compliance

### ASHRAE 62.1

DCV explicitly permitted:
- Section 6.2.7 Dynamic Reset
- Allows reduced OA when occupancy reduced
- Must maintain minimum rates
- Requires OA monitoring

### Building Energy Codes

ASHRAE 90.1 and IECC require DCV for:
- High occupancy spaces (>25 people/1,000 ft²)
- Systems >3,000 CFM
- Specific climate zones

### Educational Codes

State education department requirements:
- Minimum ventilation rates
- CO₂ monitoring often required
- Documentation and reporting

## Commissioning and Maintenance

### Commissioning Requirements

Verify DCV performance:
- Sensor calibration verification
- Control sequence testing
- Response time verification
- Minimum OA verification
- Alarm testing

### Ongoing Maintenance

| Frequency | Activity |
|-----------|----------|
| Monthly | Verify sensor readings |
| Quarterly | Check damper operation |
| Annual | Sensor calibration |
| Annual | Review trend data |

### Performance Monitoring

Track key indicators:
- CO₂ levels during occupancy
- Outdoor air delivery
- Energy consumption
- Occupant complaints

Demand-controlled ventilation provides educational facilities with optimized indoor air quality while significantly reducing energy consumption, particularly valuable in spaces with variable occupancy patterns.
