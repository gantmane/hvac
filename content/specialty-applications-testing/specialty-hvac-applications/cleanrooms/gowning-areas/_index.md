---
title: "Gowning Areas"
description: "HVAC design requirements for cleanroom gowning rooms including air change rates, pressure relationships, and contamination control strategies."
keywords: ["gowning room", "cleanroom", "contamination control", "airlock", "pressure cascade", "personnel flow"]
weight: 5
---

Gowning areas serve as critical transition zones between general environments and cleanrooms, providing space for personnel to don protective garments while preventing contamination transfer. Proper HVAC design ensures these airlocks effectively protect cleanroom integrity.

## Gowning Area Functions

### Contamination Control

Gowning rooms minimize particle introduction by:

- Providing transition between cleanliness levels
- Allowing personnel to don clean garments
- Establishing pressure barriers
- Capturing contamination before cleanroom entry
- Supporting garment storage

### Zone Classification

Gowning areas typically maintain intermediate cleanliness:

| Adjacent Cleanroom | Gowning Room Class | Reasoning |
|-------------------|-------------------|-----------|
| ISO Class 5 | ISO Class 7-8 | Significant step change |
| ISO Class 6 | ISO Class 7-8 | Moderate transition |
| ISO Class 7 | ISO Class 8 | One class step |
| ISO Class 8 | Controlled | Basic separation |

## Pressure Relationships

### Cascade Design

Establish pressure gradient from cleanest to dirtiest:

```
Cleanroom → Gowning → Corridor/Anteroom → General
(Highest)    (Mid)         (Low)          (Lowest)
```

**Typical Pressure Differentials**:
- Cleanroom to gowning: +0.03 to +0.05" w.g.
- Gowning to anteroom: +0.02 to +0.03" w.g.
- Anteroom to corridor: +0.01 to +0.02" w.g.

### Airlock Configuration

**Single-Stage Gowning**:
- One room between corridor and cleanroom
- Suitable for ISO Class 7-8 cleanrooms
- Lower construction cost

**Two-Stage Gowning**:
- Anteroom + gowning room
- Required for ISO Class 5-6 cleanrooms
- Better contamination control
- Personnel flow management

### Door Interlocks

Prevent simultaneous door opening:

- Magnetic locks with indicators
- PLC-controlled interlocking
- Emergency override capability
- Visual status indication

## Airflow Design

### Air Change Rates

| Gowning Room Class | Minimum ACH | Recommended ACH |
|-------------------|-------------|-----------------|
| ISO Class 7 | 60 | 70-80 |
| ISO Class 8 | 20 | 25-40 |
| Controlled | 10-15 | 15-20 |

### Air Distribution

**Ceiling Supply**:
- Non-unidirectional for most gowning rooms
- HEPA filtered terminal units
- 2-4 ft/s face velocity at diffusers

**Low-Level Return**:
- Located near floor level
- Captures particles generated during gowning
- Multiple locations for uniform flow

### Special Considerations

**Bench Placement**:
- Dirty side / clean side separation
- Airflow direction supports separation
- Particle control at seated position

**Mirror Locations**:
- Full-length for garment inspection
- Lighting for visual verification
- Away from supply air paths

## Temperature and Humidity

### Comfort Requirements

Gowning involves physical activity and garment insulation:

**Temperature**: 66-72°F (19-22°C)
- Lower than office due to gowning activity
- Account for garment insulation

**Relative Humidity**: 30-60%
- Static control (minimum 30%)
- Comfort (maximum 60%)
- Material compatibility

### Pharmaceutical Requirements

GMP environments may specify:
- 68°F ± 2°F during gowning operations
- 45% ± 5% RH
- Continuous monitoring and alarming

## Filtration Requirements

### Supply Air Filtration

**Terminal HEPA**:
- Required for ISO Class 7 and cleaner
- 99.99% minimum efficiency
- Ceiling-mounted terminal units

**Pre-filtration**:
- MERV 14-16 at AHU
- Extends HEPA life
- Reduces maintenance frequency

### Return Air Considerations

- Filter return air before recirculation
- MERV 8-13 typical
- Prevents cross-contamination

## Garment Storage

### Clean Garment Storage

HVAC considerations for storage:
- Positive pressure relative to gowning
- HEPA-filtered supply
- Minimize dust accumulation
- Temperature/humidity control

### Soiled Garment Collection

- Negative pressure or neutral
- Adequate exhaust
- Sealed containers
- Separate from clean garments

## Monitoring and Control

### Environmental Monitoring

**Continuous Monitoring**:
- Differential pressure (all rooms)
- Temperature and humidity
- Airflow verification

**Periodic Testing**:
- Particle counts (classification)
- HEPA filter integrity
- Air balance verification

### Alarm Systems

Critical parameter alarming:
- Pressure differential deviation
- Door position status
- Temperature/humidity excursions
- HEPA filter loading

## Design Considerations

### Personnel Flow

Design to support logical gowning sequence:
1. Enter anteroom, remove street clothes
2. Cross to gowning room
3. Don cleanroom garments
4. Inspect in mirror
5. Enter cleanroom

### Traffic Patterns

- Minimize backtracking
- Separate entry and exit when possible
- Accommodate peak traffic
- Emergency egress provisions

### Sizing

Allow adequate space:
- Minimum 50 ft² per gowning station
- Clear floor area for movement
- Storage for garment supplies
- Mirror and inspection area

Properly designed gowning area HVAC systems support personnel transition while maintaining the pressure cascades and air cleanliness essential for cleanroom contamination control.
