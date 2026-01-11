---
title: "Spectator Area Separation in Competitive Natatoriums"
description: "Engineering strategies for effective physical and air separation between pool decks and spectator zones using pressure differentials, air curtains, and barrier systems."
keywords: ["natatorium spectator separation", "pool deck air barriers", "pressure differential design", "air curtain sizing", "pool facility HVAC zoning", "spectator comfort control", "natatorium glass walls", "pool humidity control"]
weight: 3
---

## Physical and Air Separation Requirements

Competitive natatoriums demand rigorous separation between high-humidity pool environments and climate-controlled spectator areas. This separation prevents moisture migration, maintains spectator comfort at lower humidity levels (40-50% RH versus 50-60% RH on pool decks), and reduces energy consumption by isolating the intensive dehumidification loads.

### Pressure Differential Strategy

Establishing proper pressure relationships forms the foundation of effective separation. ASHRAE Handbook—HVAC Applications (Chapter 6) recommends maintaining spectator areas at positive pressure relative to pool decks to prevent chloramine and moisture migration into occupied seating zones.

**Recommended Pressure Differentials:**

| Zone Relationship | Pressure Difference | Air Change Impact |
|-------------------|---------------------|-------------------|
| Spectator to Pool Deck | +0.02 to +0.05 in. w.c. | Prevents moisture infiltration |
| Spectator to Corridor | +0.01 to +0.03 in. w.c. | Controls odor migration |
| Pool Deck to Exterior | -0.02 to -0.03 in. w.c. | Manages outdoor air intake |

The pressure differential required depends on barrier integrity and intended protection level:

$$\Delta P = \frac{\rho v^2}{2} \cdot C_d$$

Where:
- $\Delta P$ = pressure differential across barrier (in. w.c.)
- $\rho$ = air density (lb/ft³)
- $v$ = velocity through openings (ft/min)
- $C_d$ = discharge coefficient (typically 0.6-0.65)

For a spectator zone requiring +0.04 in. w.c. relative to pool deck with standard air density (0.075 lb/ft³) and typical leakage paths:

$$v = \sqrt{\frac{2 \Delta P}{\rho \cdot C_d}} = \sqrt{\frac{2 \times 0.04 \times 5.2}{0.075 \times 0.6}} \approx 115 \text{ ft/min}$$

This velocity through barrier penetrations drives sizing of makeup air and exhaust systems.

### Physical Barrier Systems

**Glass Wall Assemblies:**

Tempered or laminated glass barriers provide visual connectivity while creating physical separation. Key design considerations include:

- **Thermal performance:** Minimum U-factor of 0.35 for condensation prevention with spectator-side dew point differential
- **Structural capacity:** Wind loading equivalent to 20-30 psf for large-span installations
- **Seal integrity:** EPDM or silicone gaskets rated for chlorine exposure and continuous 85°F, 60% RH conditions
- **Access control:** Minimize door openings; specify automatic closers with hold-open capability only during emergencies

**Air Curtain Applications:**

When physical barriers are impractical for large openings or operational flexibility, properly sized air curtains provide separation. ASHRAE Standard 90.1 recognizes air curtains for conditioned space protection when meeting performance criteria.

Air curtain discharge velocity calculation:

$$V_d = V_c \sqrt{\frac{H}{W}}$$

Where:
- $V_d$ = discharge velocity (ft/min)
- $V_c$ = crossflow velocity (infiltration velocity, typically 50-150 ft/min)
- $H$ = opening height (ft)
- $W$ = air curtain width (effective jet width, ft)

For a 10-ft high opening with anticipated crossflow of 100 ft/min and 6-inch jet width:

$$V_d = 100 \sqrt{\frac{10}{0.5}} \approx 447 \text{ ft/min}$$

Required airflow per linear foot:

$$CFM/ft = \frac{V_d \times W \times 60}{144} = \frac{447 \times 0.5 \times 60}{144} \approx 93 \text{ CFM/ft}$$

A 20-ft wide opening requires approximately 1,860 CFM air curtain capacity.

### Separation System Comparison

| Strategy | Effectiveness | Capital Cost | Operating Cost | Maintenance | Best Application |
|----------|---------------|--------------|----------------|-------------|------------------|
| Full Glass Walls | 95-100% | High | Low | Low | Permanent separation, year-round facilities |
| Partial Glass + Curtains | 85-95% | Medium-High | Medium | Medium | Flexible access requirements |
| Air Curtains Only | 70-85% | Medium | Medium-High | Medium | Seasonal facilities, budget constraints |
| Pressure Control Only | 50-70% | Low | Medium | Low | Low-use facilities, minimal separation needs |
| Vestibules with Airlocks | 90-98% | High | Low | Low | High-traffic access points |

### HVAC System Zoning

Separate air handling systems for each zone enable independent control of temperature, humidity, and pressure:

**Pool Deck System:**
- 100% outdoor air or dedicated dehumidification with energy recovery
- Discharge conditions: 78-82°F, 50-60% RH
- 4-6 air changes per hour minimum
- Negative or neutral pressure relative to outdoors

**Spectator System:**
- Conventional mixed-air system with economizer capability
- Discharge conditions: 70-74°F, 40-50% RH
- 6-8 air changes per hour during events
- Positive pressure relative to adjacent zones (+0.02 to +0.05 in. w.c.)

Interlocked control sequences prevent simultaneous operation in modes that would reverse pressure relationships.

### Code and Standard References

- **IMC Section 403.3:** Mechanical ventilation requirements for assembly occupancies
- **ASHRAE 62.1:** Outdoor air requirements (spectator areas: 7.5 CFM/person; natatoriums: air quality procedure)
- **ASHRAE Handbook—HVAC Applications, Chapter 6:** Specific natatorium design guidance
- **IBC Section 303:** Assembly occupancy classification and separation requirements

## Separation Methodology Diagram

```mermaid
graph TB
    subgraph "Spectator Zone +0.03 in. w.c."
        A[Supply Air<br/>72°F, 45% RH<br/>6-8 ACH]
        B[Glass Wall Barrier<br/>U=0.35<br/>Sealed Construction]
        C[Access Doors<br/>Auto-Close<br/>Weather-stripped]
        D[Air Curtain<br/>450 fpm discharge<br/>At large openings]
    end

    subgraph "Pool Deck Zone -0.01 in. w.c."
        E[Supply Air<br/>80°F, 55% RH<br/>4-6 ACH]
        F[Dedicated Dehumidification<br/>Energy Recovery]
        G[Exhaust<br/>Low-level return<br/>Chloramine removal]
    end

    subgraph "Pressure Control"
        H[Spectator Supply Fan<br/>VFD + Pressure Control]
        I[Pool Deck Exhaust<br/>VFD + Pressure Control]
        J[Differential Pressure Sensor<br/>±0.001 in. w.c. accuracy]
    end

    A --> B
    B -.Moisture barrier.-> E
    C --> D
    D -.Air seal.-> E
    H --> A
    I --> G
    J --> H
    J --> I
    F --> E

    style B fill:#e1f5ff
    style D fill:#fff4e1
    style J fill:#ffe1e1
</antmlaid>
```

**Diagram Key:**
- **Blue (Physical Barriers):** Glass walls and sealed construction elements
- **Yellow (Air Barriers):** Air curtain and pressure-driven separation
- **Red (Control Systems):** Pressure monitoring and active control components

## Implementation Considerations

**Design Phase:**
- Model pressure relationships using multizone airflow simulation (CONTAM, EnergyPlus)
- Calculate barrier leakage area from construction drawings and door schedules
- Size air handling equipment with 15-20% capacity margin for pressure control authority

**Construction Phase:**
- Verify glass wall seal continuity with blower door testing before interior finishes
- Commission pressure control sequences with all doors and openings in various states
- Document baseline pressure measurements across all barrier elements

**Operational Phase:**
- Monitor differential pressure continuously; alarm at ±0.01 in. w.c. deviation from setpoint
- Inspect door seals and automatic closers quarterly
- Clean air curtain nozzles and verify discharge velocity annually

Properly engineered separation systems deliver comfortable spectator environments while protecting viewing areas from the aggressive pool deck atmosphere, reducing maintenance costs and extending facility service life.
