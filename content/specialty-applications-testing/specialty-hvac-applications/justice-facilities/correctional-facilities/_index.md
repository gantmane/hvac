---
title: "Correctional Facilities HVAC Systems Design"
aliases: ["Correctional Facilities HVAC Systems Design"]
description: "Technical overview of HVAC design for correctional facilities including security-level classifications, airflow control, and system redundancy requirements."
keywords: ["correctional HVAC", "prison ventilation", "security level HVAC", "detention facility climate control", "ACA standards", "correctional airflow", "prison temperature control", "secure facility HVAC"]
tags: ["correctional HVAC", "prison ventilation", "security level HVAC", "detention facility climate control", "ACA standards", "correctional airflow", "prison temperature control", "secure facility HVAC"]
weight: 2
---

# Correctional Facilities HVAC Systems

Correctional facility HVAC systems must balance environmental control, security requirements, operational safety, and energy efficiency. Design considerations vary significantly based on security classification, occupancy patterns, and facility mission.

## Security Classification Impact on HVAC Design

Security level determines ventilation strategy, equipment accessibility, and control methodology.

### Security Level Requirements

| Security Level | Minimum ACH | Temperature Range | Individual Control | Equipment Location |
|----------------|-------------|-------------------|-------------------|-------------------|
| Maximum | 10-15 | 68-78°F | None | Remote secure areas |
| Medium | 8-12 | 68-76°F | Limited zone | Controlled access |
| Minimum | 6-10 | 65-78°F | Zone level | Standard locations |
| Administrative | 4-8 | 70-74°F | Individual space | Standard access |

## Primary Space Types and Ventilation Criteria

Correctional facilities contain diverse space types with conflicting HVAC requirements.

### Housing Unit Design Parameters

**Cell Block Ventilation:**
- Supply air: 15-20 CFM per occupant minimum
- Exhaust locations: toilet/shower areas
- Pressure relationship: slightly negative to corridors
- Temperature setpoint: 72°F ± 4°F (non-adjustable by occupants)

The airflow rate per housing unit is calculated:

$$Q_{\text{cell}} = N_{\text{occ}} \times 20 + A_{\text{floor}} \times 0.06$$

Where:
- $Q_{\text{cell}}$ = required airflow (CFM)
- $N_{\text{occ}}$ = maximum occupant count
- $A_{\text{floor}}$ = floor area (ft²)
- 0.06 = area-based ventilation rate (CFM/ft²)

**Dayroom/Common Areas:**
- Minimum 10 ACH or 25 CFM per occupant (whichever is greater)
- Direct exhaust preferred
- Positive pressure relative to cells
- Enhanced filtration (MERV 13 minimum)

### Support and Service Spaces

**Kitchen and Food Service:**
- Kitchen hood exhaust: 150-400 CFM per linear foot
- Makeup air: 80-100% of exhaust
- Positive pressure in serving areas
- Negative pressure in dishwashing areas

**Medical Units:**
- Outpatient: 6 ACH supply, positive pressure
- Isolation rooms: 12 ACH supply, negative pressure (-0.01" WC minimum)
- Exam rooms: positive pressure, individual exhaust

**Visitation Areas:**
- Contact: 10 ACH minimum, positive pressure
- Non-contact: standard comfort conditioning
- Attorney rooms: acoustic and environmental isolation

## Pressure Control and Airflow Strategies

Maintaining pressure differentials prevents migration of odors, contaminants, and smoke between security zones.

```mermaid
graph LR
    A[Outdoor Air] --> B[AHU with Filtration]
    B --> C[Administrative +0.05" WC]
    B --> D[Corridors +0.02" WC]
    D --> E[Housing Units 0.00" WC]
    E --> F[Cell Toilets -0.02" WC]
    B --> G[Medical Positive +0.03" WC]
    B --> H[Medical Isolation -0.01" WC]
    F --> I[Exhaust to Atmosphere]
    H --> I
```

### Pressure Cascade Design

The pressure differential between adjacent zones is maintained:

$$\Delta P_{\text{zone}} = 0.02 \text{ to } 0.05 \text{ inches WC}$$

Total system pressure drop across the facility:

$$\Delta P_{\text{total}} = \sum_{i=1}^{n} \Delta P_i + P_{\text{filter}} + P_{\text{duct}}$$

Where:
- $\Delta P_i$ = pressure drop across each zone boundary
- $P_{\text{filter}}$ = filter bank pressure loss
- $P_{\text{duct}}$ = distribution system resistance

## System Architecture Considerations

### Equipment Location and Access

Equipment must be located in secure areas inaccessible to inmates while allowing maintenance access:

1. **Air handling units**: mechanical penthouses or secure mechanical rooms
2. **Terminal units**: above secure ceilings with tamper-proof fasteners
3. **Ductwork**: concealed in chase walls or structural spaces
4. **Controls**: centralized with limited local access
5. **Outdoor equipment**: secured yards or rooftop installations with controlled access

### Redundancy Requirements

Critical spaces require backup systems per ACA and local jurisdiction standards:

- **Medical units**: 100% redundant capacity with automatic failover
- **Kitchen**: dual exhaust fans with emergency power
- **Housing units**: N+1 equipment redundancy for air handling
- **Control rooms**: independent systems with UPS backup

The redundant capacity calculation:

$$Q_{\text{redundant}} = Q_{\text{design}} \times 1.0$$

For N+1 configuration with modular equipment:

$$N_{\text{units}} = \left\lceil \frac{Q_{\text{total}}}{Q_{\text{module}}} \right\rceil + 1$$

## Control System Security

HVAC controls in correctional facilities must prevent tampering while allowing operational flexibility:

- **Building automation**: role-based access with audit logging
- **Local controls**: lockable or eliminated in housing units
- **Temperature limits**: software-enforced ranges per ACA standards
- **Override capability**: emergency control from secure command center
- **Monitoring**: continuous verification of pressure relationships

## Energy Efficiency in Secure Environments

Energy conservation must not compromise security or safety:

**Acceptable strategies:**
- Heat recovery on general exhaust streams (not from contaminated sources)
- Variable volume systems in administrative areas
- Occupancy-based control in intermittently used spaces
- Premium efficiency motors and drives
- Free cooling when outdoor conditions permit

**Prohibited or restricted:**
- Operable windows in housing units
- Decentralized equipment accessible to inmates
- Economizer cycles that compromise filtration
- Demand-controlled ventilation in housing areas

## Code and Standard References

Design must comply with:

- **ASHRAE Standard 62.1**: Ventilation for Acceptable Indoor Air Quality
- **ASHRAE Standard 170**: Ventilation of Health Care Facilities (medical units)
- **ACA Standards**: American Correctional Association performance-based standards
- **NFPA 90A**: Installation of Air-Conditioning and Ventilating Systems
- **International Mechanical Code**: Minimum ventilation and safety requirements
- **State/Local Corrections Regulations**: Jurisdiction-specific requirements

## Smoke Control and Fire Safety

Life safety systems must account for secured populations:

**Smoke management approach:**
- Zoned smoke control per IMC requirements
- Automatic damper operation coordinated with fire alarm
- Pressurization of egress routes
- Dedicated smoke exhaust in high-occupancy areas
- Manual override from fire command station

**Fire-smoke damper locations:**
- All penetrations of fire-rated assemblies
- Branch connections to common vertical shafts
- Boundaries between smoke control zones
- Interface between secure and non-secure areas

## Commissioning and Operational Verification

Verification testing must confirm:

1. Pressure relationships under all operating modes
2. Ventilation rates in all occupied spaces
3. Temperature control within specified ranges
4. Redundant system failover operation
5. Control system security and lockout functionality
6. Emergency override procedures
7. Filter replacement accessibility

Continuous commissioning protocols ensure ongoing compliance with environmental and security requirements as facility population and mission evolve.
