---
title: "Tunnel Ventilation"
description: "HVAC design for tunnel ventilation systems including road tunnels, transit tunnels, and emergency smoke control requirements."
keywords: ["tunnel ventilation", "road tunnel", "transit tunnel", "smoke control", "jet fans", "longitudinal ventilation"]
weight: 5
---

Tunnel ventilation systems maintain air quality during normal operation and provide critical life safety functions during fire emergencies. Design requirements vary significantly based on tunnel type, length, traffic characteristics, and fire safety objectives.

## Ventilation Objectives

### Normal Operation

During routine use, ventilation provides:

- **Contaminant Dilution**: Reduce vehicle emissions to acceptable levels
- **Visibility**: Maintain adequate sight distance
- **Thermal Control**: Remove heat from vehicles and systems
- **Comfort**: Acceptable conditions for occupants and workers

### Emergency Operation

During fire or incident:

- **Smoke Control**: Clear evacuation paths
- **Tenable Conditions**: Support safe egress
- **Firefighting Access**: Enable emergency response
- **Structural Protection**: Limit fire-induced temperatures

## Ventilation System Types

### Longitudinal Ventilation

Air moves along tunnel length in one direction:

**Components**:
- Jet fans mounted in tunnel
- Portal fans (optional)
- Control systems

**Advantages**:
- Lower construction cost
- No transverse ducts
- Flexible operation
- Common for road tunnels <2 km

**Limitations**:
- Requires unidirectional traffic for fire mode
- Limited effectiveness for very long tunnels
- Back-layering concern during fires

### Transverse Ventilation

Supply and exhaust through separate duct systems:

**Full Transverse**:
- Supply duct along tunnel
- Exhaust duct along tunnel
- Uniform distribution
- High construction cost

**Semi-Transverse**:
- Either supply or exhaust ducted
- Other through portals
- Reduced cost vs. full transverse

**Advantages**:
- Better contaminant control
- Bidirectional traffic compatible
- Enhanced fire control

### Hybrid Systems

Combine longitudinal and transverse elements:
- Point extraction for fire emergencies
- Longitudinal normal operation
- Flexibility for varying conditions

## Design Parameters

### Air Quality Standards

**Carbon Monoxide (CO)**:
| Duration | Limit | Application |
|----------|-------|-------------|
| 15 min | 120 ppm | Short tunnel exposure |
| 1 hour | 35 ppm | Extended exposure |
| 8 hour | 25 ppm | Worker exposure |

**Nitrogen Dioxide (NO₂)**:
- Short-term: 1.0 ppm
- Long-term: 0.25 ppm

**Visibility**:
- Extinction coefficient: K < 0.005-0.012 m⁻¹
- Sight distance: >100 m typical

### Emission Factors

Vehicle emission rates depend on:
- Fleet composition (cars, trucks, buses)
- Traffic speed
- Grade (upgrade produces more emissions)
- Vehicle age and emission standards

**Typical Values** (modern fleet):
| Pollutant | Light Duty | Heavy Duty |
|-----------|------------|------------|
| CO | 5-15 g/km | 10-30 g/km |
| NOx | 0.5-2 g/km | 5-15 g/km |
| PM | 0.01-0.05 g/km | 0.1-0.5 g/km |

### Airflow Requirements

**Dilution Ventilation**:
$$Q = \frac{N \times E \times L}{C_{max} - C_{ambient}}$$

Where:
- N = number of vehicles
- E = emission rate
- L = tunnel length
- C = concentration limit

**Typical Ranges**:
- Road tunnels: 100-400 CFM per vehicle
- Transit tunnels: Based on train schedules

## Jet Fan Systems

### Operating Principle

Jet fans transfer momentum to tunnel air:

$$F_{thrust} = \dot{m} \times (V_{jet} - V_{tunnel})$$

**Typical Specifications**:
- Diameter: 800-1,400 mm
- Thrust: 500-2,000 N
- Jet velocity: 25-35 m/s
- Reversible operation

### Sizing Considerations

Account for:
- Pressure losses (friction, obstacles)
- Traffic drag (piston effect)
- Meteorological effects (wind, buoyancy)
- Grade effects
- Fire scenario requirements

### Installation

**Mounting**:
- Ceiling mounted in pairs
- Staggered arrangement
- Minimum spacing for thrust development
- Structural support for thrust loads

**Fire Protection**:
- High-temperature rated for fire zones
- Redundant units
- Rated for 250-400°C for 2 hours

## Fire Emergency Ventilation

### Design Fire Size

| Tunnel Type | Design Fire | Heat Release |
|-------------|-------------|--------------|
| Car tunnel | 2-3 cars | 8-15 MW |
| Heavy truck | Single truck | 20-30 MW |
| HGV/Tanker | Dangerous goods | 100-200 MW |
| Transit | Rail car | 10-30 MW |

### Smoke Control Strategies

**Longitudinal Control**:
- Push smoke downstream of fire
- Critical velocity: 2.5-3.5 m/s
- Requires one-way traffic

$$V_{critical} = K \times \left(\frac{g \times H \times Q}{c_p \times \rho \times T_{ambient} \times A}\right)^{1/3}$$

**Point Extraction**:
- Extract smoke at fire location
- Damper-controlled extraction points
- Maintains tenable conditions both directions

### Emergency Operating Modes

| Scenario | System Response |
|----------|-----------------|
| Fire detected | Stop normal ventilation |
| Location confirmed | Activate smoke control mode |
| Evacuation phase | Maintain tenable egress |
| Firefighting | Support emergency access |

## Controls and Monitoring

### Detection Systems

**Air Quality Monitoring**:
- CO sensors at regular intervals
- Visibility (opacity) meters
- NOx monitoring (some applications)

**Fire Detection**:
- Linear heat detection
- Video analytics
- Flame detectors
- Smoke detection (challenging)

### SCADA Integration

Supervisory control includes:
- Automatic mode selection
- Manual override capability
- Sensor data trending
- Alarm management
- Emergency coordination

### Operational Modes

- **Normal**: Maintains air quality
- **Congested**: Enhanced ventilation
- **Emergency**: Smoke control protocol
- **Maintenance**: Safe access conditions

## Standards and Guidelines

### Design Standards

- **NFPA 502**: Road Tunnels, Bridges, and Other Limited Access Highways
- **ASHRAE Applications Handbook**: Chapter on Enclosed Vehicular Facilities
- **PIARC**: World Road Association guidelines
- **European Directive 2004/54/EC**: Trans-European road tunnels

### Testing Requirements

- Hot smoke tests
- Jet fan thrust verification
- Control system commissioning
- Emergency drill exercises

Tunnel ventilation design requires careful balance between normal operational requirements, emergency capabilities, and lifecycle cost considerations unique to these critical infrastructure systems.
