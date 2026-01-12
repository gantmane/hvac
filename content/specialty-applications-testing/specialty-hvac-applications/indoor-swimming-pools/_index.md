---
title: "Indoor Swimming Pools"
description: "HVAC design for indoor swimming pool facilities including humidity control, air quality, and corrosion prevention strategies."
keywords: ["indoor pool", "natatorium", "pool HVAC", "humidity control", "chloramine control", "pool dehumidification"]
weight: 10
---

Indoor swimming pool facilities, or natatoriums, present unique HVAC challenges including extreme humidity loads, corrosive atmospheres, and stringent air quality requirements for swimmer health and building protection.

## Design Challenges

### Humidity Generation

Pool evaporation generates substantial moisture:

$$W_{evap} = A \times (p_{sat,water} - p_{air}) \times K_{activity}$$

Where:
- A = pool surface area
- p = vapor pressure
- K = activity factor (0.5-1.0)

**Evaporation Rates**:
| Activity Level | Evaporation (lb/h/ft²) |
|----------------|------------------------|
| Quiescent pool | 0.04-0.06 |
| Residential use | 0.06-0.08 |
| Public swimming | 0.10-0.12 |
| Competition | 0.12-0.15 |
| Wave pools | 0.30-0.40 |

### Chloramine Concerns

Chloramines (combined chlorine) form when chlorine reacts with organic compounds:

**Health Effects**:
- Eye and respiratory irritation
- Asthma triggers
- Reduced air quality

**Control Strategies**:
- Adequate ventilation
- Source-level exhaust
- UV treatment of pool water
- Proper water chemistry

### Corrosion Environment

Warm, humid, chlorinated air attacks:
- Steel structures
- Electrical equipment
- Ductwork
- Building finishes

## Ventilation Requirements

### Air Change Rates

ASHRAE recommendations:

| Space | Minimum ACH | Outdoor Air |
|-------|-------------|-------------|
| Pool area | 4-6 | 0.48 CFM/ft² |
| Spectator areas | 4-8 | 15 CFM/person |
| Locker rooms | 4-6 | 0.5 CFM/ft² |
| Showers | 10-15 | 50 CFM/head |

### Outdoor Air

Minimum outdoor air for natatoriums:
- ASHRAE 62.1: 0.48 CFM/ft² pool deck
- Capture chloramines near source
- Prevent recirculation of contaminants

### Air Distribution

**Supply Air**:
- High on walls or ceiling
- Directed across pool surface
- 25-50 fpm at pool surface (minimizes evaporation)

**Return/Exhaust**:
- Low on walls (near deck level)
- Captures heavy chloramine compounds
- Multiple points around perimeter

## Temperature and Humidity

### Design Conditions

| Parameter | Pool Area | Spectator |
|-----------|-----------|-----------|
| Dry bulb | 82-86°F | 75-78°F |
| Relative humidity | 50-60% | 50-60% |
| Deck temperature | 84-88°F | N/A |

### Water-to-Air Relationship

Maintain air temperature 2-5°F above water temperature:
- Reduces evaporation rate
- Improves swimmer comfort
- Prevents fog formation

$$T_{air} = T_{water} + (2°F\ to\ 5°F)$$

### Humidity Control

Target 50-60% RH for balance:
- <50%: Excessive evaporation, swimmer discomfort
- >60%: Condensation risk, comfort issues

## Dehumidification Systems

### Refrigerant-Based Dehumidifiers

Mechanical dehumidification with heat recovery:

**Operating Cycle**:
1. Air passes over evaporator (cools below dew point)
2. Moisture condenses and drains
3. Air reheated over condenser
4. Some heat returned to pool water

**Efficiency**:
- COP: 4-6 for dehumidification
- Heat recovery to pool: 50-80% of removed latent

### Outdoor Air Systems

Use outdoor air for dehumidification when favorable:

$$m_{OA} = \frac{m_{moisture}}{W_{return} - W_{OA}}$$

**Effective When**:
- Outdoor humidity ratio < indoor
- Typically 50°F and below outdoor temperature

### Desiccant Systems

Desiccant wheels for specialized applications:
- Very low humidity requirements
- Heat recovery from exhaust
- Combined with refrigerant systems

### Hybrid Approaches

Combine methods for optimization:
- Outdoor air when effective
- Mechanical dehumidification when needed
- Heat pump heat recovery
- Energy recovery from exhaust

## HVAC System Components

### Air Handling Units

Specialized natatorium AHUs:
- Corrosion-resistant construction (stainless, aluminum, coated)
- Large OA/exhaust capacity
- Integrated dehumidification
- High-quality filtration

### Ductwork

**Material Selection**:
| Material | Application | Notes |
|----------|-------------|-------|
| Aluminum | Preferred | Corrosion resistant |
| Stainless steel | High corrosion | Higher cost |
| Fiberglass | Supply ducts | No condensation areas |
| PVC | Exhaust | Certain applications |

**Avoid**: Galvanized steel in pool area atmosphere

### Exhaust Systems

Dedicated pool exhaust:
- Corrosion-resistant fans
- Low-level pickup points
- Roof discharge
- Separate from general HVAC

## Energy Efficiency

### Heat Recovery

Multiple heat recovery opportunities:

| Source | Recovery Method | Application |
|--------|-----------------|-------------|
| Exhaust air | Air-to-air HX | Preheat outdoor air |
| Condenser heat | Desuperheater | Pool water heating |
| Dehumidifier | Heat recovery | Space/pool heating |

### Pool Covers

Reduce evaporation during unoccupied periods:
- 50-70% evaporation reduction
- Automatic covers for convenience
- Ventilation reduction possible with cover deployed

### Control Strategies

- Setback when unoccupied
- Pool cover integration
- OA economizer when effective
- Demand-controlled ventilation

## Special Considerations

### Condensation Prevention

Prevent surface condensation:
- Maintain wall temperatures above dew point
- Insulate exterior walls well
- Warm window frames/glazing
- Air movement over surfaces

### Structural Protection

Design for durability:
- Vapor barriers on warm side
- Stainless fasteners
- Protective coatings
- Material selection throughout

### Acoustics

Swimming pools amplify sound:
- Sound-absorbing materials
- Duct silencers
- Equipment isolation
- Background noise consideration

Indoor swimming pool HVAC systems require specialized design addressing extreme humidity, air quality, and corrosion challenges while providing energy-efficient operation for these demanding facilities.
