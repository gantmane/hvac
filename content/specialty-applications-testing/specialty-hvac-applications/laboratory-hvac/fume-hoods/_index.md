---
title: "Fume Hoods"
aliases: ["Fume Hoods"]
description: "HVAC design for laboratory fume hood systems including face velocity requirements, exhaust configurations, and control strategies."
keywords: ["fume hood", "chemical fume hood", "laboratory exhaust", "face velocity", "VAV fume hood", "containment"]
tags: ["fume hood", "chemical fume hood", "laboratory exhaust", "face velocity", "VAV fume hood", "containment"]
weight: 3
---

Laboratory fume hoods provide critical containment for chemical vapors, gases, and particulates. HVAC system design must ensure proper exhaust rates, face velocities, and room air balance while optimizing energy consumption.

## Fume Hood Types

### Conventional (Constant Air Volume)

Fixed exhaust rate regardless of sash position:
- Simple operation
- Higher energy consumption
- Face velocity varies with sash position
- Suitable for teaching labs, limited budgets

### Variable Air Volume (VAV)

Exhaust modulates with sash position:
- Maintains constant face velocity
- Significant energy savings (40-60%)
- More complex controls
- Standard for research laboratories

### Auxiliary Air (Add-Air)

Supplemental air supply at hood face:
- Reduces conditioned air consumption
- Not recommended (containment concerns)
- Prohibited by many institutions
- Legacy installations only

### Ductless (Filtered)

Carbon filter recirculation to room:
- No duct connection required
- Limited chemical compatibility
- Filter saturation monitoring critical
- Not appropriate for all applications

## Face Velocity Requirements

### Design Face Velocity

ASHRAE and AIHA recommendations:

| Application | Face Velocity | Notes |
|-------------|---------------|-------|
| Standard chemicals | 80-100 fpm | Most common |
| High hazard | 100-120 fpm | Highly toxic materials |
| Low hazard | 60-80 fpm | Nuisance materials |
| Perchloric acid | 100-120 fpm | Dedicated system |
| Radioisotope | 100-125 fpm | Specialized requirements |

### Sash Position Considerations

Face velocity calculated at working opening:

$$V_{face} = \frac{Q_{exhaust}}{A_{opening}}$$

**Full Open Sash**: Maximum exhaust, design face velocity
**Partially Closed**: Reduced exhaust (VAV), maintained face velocity
**Fully Closed**: Minimum exhaust (bypass air or slot)

## Exhaust System Design

### Individual Exhaust

One fan per hood:
- No cross-contamination
- Independent operation
- Higher capital cost
- More roof penetrations

### Manifold Exhaust

Multiple hoods share exhaust system:
- Lower cost
- Fewer penetrations
- Dilution of concentrated vapors
- Requires careful design

### System Configurations

**Constant Volume Manifold**:
- Bypass dampers at each hood
- Central fan runs constant
- Individual hood VAV possible

**Variable Volume Manifold**:
- Total exhaust varies with demand
- Variable speed fan(s)
- Significant energy savings
- Complex controls

### Exhaust Fan Selection

| Criteria | Specification |
|----------|---------------|
| Material | Corrosion-resistant |
| Location | Roof preferred (negative duct) |
| Redundancy | Consider backup fan |
| Capacity | All hoods at maximum |

### Stack Design

Discharge above roof:
- 10 ft minimum above roof
- 2 ft above adjacent air intakes
- Adequate exit velocity (3,000+ fpm)
- Rain protection

## Room Air Balance

### Makeup Air

Supply air must balance exhaust:

$$\dot{V}_{supply} = \dot{V}_{fume\ hoods} + \dot{V}_{general\ exhaust} - \dot{V}_{infiltration}$$

Maintain slight negative pressure relative to corridor.

### Air Change Rates

Laboratory air changes (total supply):

| Risk Level | Minimum ACH |
|------------|-------------|
| General chemistry | 6-10 |
| Organic chemistry | 8-12 |
| High hazard | 10-15 |
| Teaching lab | 6-8 |

### Supply Air Distribution

Position supply to avoid disrupting hoods:
- Maintain <50 fpm at hood face
- No supply directly opposing hood
- Perforated ceiling or high sidewall

## Control Systems

### VAV Hood Controls

Monitor and modulate:
- Sash position sensor
- Face velocity measurement
- Exhaust damper/valve
- Alarm on low face velocity

### Room Pressure Control

Track supply with exhaust changes:
- Direct pressure control
- Offset tracking
- Cascade control
- Response time matching

### Building Automation

BAS integration requirements:
- Hood status monitoring
- Alarm management
- Energy monitoring
- Occupancy scheduling

## Performance Testing

### ASHRAE 110 Method

Standard test protocol:
- **Face Velocity Test**: Measure velocity uniformity
- **Flow Visualization**: Observe smoke patterns
- **Tracer Gas Test**: Quantify containment (as manufactured: <0.05 ppm; as installed: <0.10 ppm)

### Periodic Verification

Annual testing minimum:
- Face velocity measurement
- Visual inspection
- Alarm verification
- Sash sensor calibration

### Continuous Monitoring

Real-time parameters:
- Face velocity or exhaust flow
- Sash position
- Room pressure differential
- Alarm status

## Energy Efficiency

### VAV Hood Benefits

Energy savings from VAV:

$$Savings = \sum hours \times (Q_{CV} - Q_{VAV}) \times \Delta h \times Cost$$

Typical 40-60% reduction in hood-related energy.

### Occupancy-Based Control

Further reduction when labs unoccupied:
- Setback face velocity (50-60 fpm)
- Maintain minimum air changes
- Rapid return to normal on entry

### Sash Management

Operator behavior programs:
- Close sashes when not in use
- Alarm on extended full-open
- Training and awareness
- Significant savings potential

### Heat Recovery

For high exhaust volumes:
- Runaround coils (no cross-contamination)
- Heat pipe systems
- Energy wheels (careful with contaminants)
- Return on investment analysis

## Special Hood Types

### Perchloric Acid Hoods

Dedicated system with:
- Stainless steel construction
- Wash-down system
- No manifold connection
- Direct exhaust

### Radioisotope Hoods

HEPA filtration with:
- Bag-in/bag-out filter
- Higher face velocity
- Glove box option
- Special waste handling

### Walk-In Hoods

Large equipment accommodation:
- Higher exhaust volumes
- Multiple sash options
- Floor-level exhaust

Effective fume hood HVAC integration ensures occupant safety while managing the substantial energy requirements of these critical containment devices through appropriate system design and control strategies.
