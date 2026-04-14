---
title: "Humidity Control"
aliases: ["Humidity Control"]
description: "Humidity control strategies for natatoriums including dehumidification systems, condensation prevention, and energy-efficient operation."
keywords: ["natatorium humidity", "pool dehumidification", "humidity control", "condensation prevention", "swimming pool HVAC"]
tags: ["natatorium humidity", "pool dehumidification", "humidity control", "condensation prevention", "swimming pool HVAC"]
weight: 3
---

Natatorium humidity control is critical for occupant comfort, building protection, and energy management. The substantial moisture load from pool evaporation requires specialized dehumidification systems and careful design to prevent condensation damage.

## Humidity Load Calculation

### Evaporation Rate Estimation

Pool evaporation depends on multiple factors:

$$W = A \times (p_w - p_a) \times F_a$$

Where:
- W = evaporation rate (lb/h)
- A = pool surface area (ft²)
- p_w = saturation pressure at water temperature
- p_a = partial pressure of water vapor in air
- F_a = activity factor

### Activity Factors

| Activity Level | Factor | Description |
|----------------|--------|-------------|
| Unoccupied (with cover) | 0.1-0.2 | Covered pool |
| Unoccupied (no cover) | 0.5 | Quiet water surface |
| Residential use | 0.5-0.7 | Light activity |
| Public swimming | 0.8-1.0 | Moderate activity |
| Competition/training | 1.0-1.2 | High activity |
| Wave pools | 1.5-2.0 | Aggressive surface |
| Waterslides/features | 1.5-2.5 | High agitation |

### Example Calculation

**Pool**: 25m × 25m (6,700 ft²), 82°F water, 84°F air at 55% RH

$$p_w = 0.533\ psia\ (at\ 82°F)$$
$$p_a = 0.55 \times 0.596 = 0.328\ psia$$
$$W = 6,700 \times (0.533 - 0.328) \times 0.8 = 1,100\ lb/h$$

## Humidity Setpoints

### Design Targets

| Parameter | Recommended | Notes |
|-----------|-------------|-------|
| Relative humidity | 50-60% | Balance comfort and evaporation |
| Air temperature | 82-86°F | 2-5°F above water temperature |
| Dew point | 62-68°F | Condensation prevention |

### Temperature-Humidity Relationship

Higher air temperature and lower humidity reduce evaporation:

$$\Delta p = p_{sat,water} - p_{air}$$

Reducing this vapor pressure difference reduces evaporation rate and humidity load.

### Comfort Considerations

**Low Humidity (<50%)**:
- Increased evaporation
- Higher energy consumption
- Swimmer discomfort (skin drying)

**High Humidity (>60%)**:
- Condensation risk
- Uncomfortable "muggy" feeling
- Mold/mildew potential

## Dehumidification Methods

### Mechanical Refrigeration

Refrigerant-based dehumidification systems:

**Operating Cycle**:
1. Warm, humid air crosses evaporator coil
2. Air cools below dew point
3. Moisture condenses on coil
4. Condensate drains away
5. Cool, dry air reheated over condenser

**Capacity**: 50-500 lb/h moisture removal typical

**Heat Recovery Options**:
- Air reheat (condenser in airstream)
- Pool water heating (desuperheater)
- Combined approach

### Outdoor Air Ventilation

Use outdoor air when favorable:

$$Effective\ when: W_{outdoor} < W_{return}$$

**Typical Conditions**:
- Outdoor temperature <55°F
- Low outdoor humidity

**Control Strategy**:
- Enthalpy economizer operation
- Transition smoothly between modes
- Minimum outdoor air always maintained

### Desiccant Systems

Solid or liquid desiccant absorption:

**Applications**:
- Very low humidity requirements
- Heat recovery from exhaust
- Combined with mechanical cooling

**Considerations**:
- Higher first cost
- Regeneration energy required
- Specialized maintenance

### Hybrid Systems

Combine multiple methods:
- Outdoor air when effective (free dehumidification)
- Mechanical dehumidification when needed
- Heat pump heat recovery
- Optimize for conditions

## Condensation Prevention

### Critical Surfaces

Surfaces at risk:
- Windows and skylights
- Exterior walls
- Roof structure
- Cold water pipes
- Metal framework

### Surface Temperature Requirement

Maintain surface temperature above dew point:

$$T_{surface} > T_{dewpoint,air}$$

**Example**: 60% RH, 84°F air → Dew point = 68°F
Surface must be >68°F to prevent condensation.

### Prevention Strategies

**Windows/Glazing**:
- High-performance glazing (low U-factor)
- Warm-edge spacers
- Thermally broken frames
- Air directed over glass surfaces

**Exterior Walls**:
- Continuous insulation
- Vapor barriers on warm side
- Thermal bridge elimination

**Roof Structure**:
- Insulate above deck
- Vapor barrier below insulation
- Warm air circulation at underside

### Air Movement

Prevent condensation through air circulation:
- 15-25 fpm over glazing
- No stagnant air pockets
- Directed supply at vulnerable surfaces

## Energy Efficiency

### Pool Covers

Reduce evaporation when unoccupied:
- 50-70% reduction in evaporation
- Automatic covers for convenience
- Allow ventilation reduction
- Significant energy savings

$$Savings = Cover\ hours \times (1 - Factor_{cover}/Factor_{no\ cover}) \times Load$$

### Heat Recovery

Recover energy from dehumidification:

| Recovery Method | Efficiency | Application |
|-----------------|------------|-------------|
| Air reheat | 100% sensible | Space heating |
| Pool heating | 50-80% | Water temperature |
| Hot water | 30-50% | DHW preheat |

### Control Optimization

- Setback when unoccupied
- Cover interlock
- Economizer when conditions allow
- Demand-based ventilation

### Energy Benchmarks

Typical natatorium energy intensity:
- 150-300 kBtu/ft²·year (without optimization)
- 80-150 kBtu/ft²·year (with best practices)

## Equipment Selection

### Packaged Dehumidification Units

Purpose-built natatorium units:
- Corrosion-resistant construction
- Integrated controls
- Heat recovery options
- Outdoor air capability

### Custom Air Handling

Large facilities may use:
- Built-up AHU with DX cooling
- Chilled water systems
- Separate dehumidifier integration
- Energy recovery equipment

### Capacity Sizing

Design for peak conditions:
- Maximum activity level
- Design outdoor conditions
- No pool cover (operating)
- Safety factor (10-15%)

## Control Systems

### Primary Control

Humidity control loop:
- Humidity sensor (space)
- Setpoint (50-60% RH)
- Modulate dehumidification
- Coordinate outdoor air

### Mode Selection

Automatic mode transitions:
- Outdoor air mode (economizer favorable)
- Mechanical dehumidification (economizer unfavorable)
- Combined mode (transitional)

### Monitoring

Track and trend:
- Space temperature and humidity
- Pool water temperature
- Outdoor conditions
- Energy consumption
- Equipment operation

Effective humidity control in natatoriums protects building structures from moisture damage while maintaining comfortable conditions and optimizing energy consumption through appropriate system selection and control.
