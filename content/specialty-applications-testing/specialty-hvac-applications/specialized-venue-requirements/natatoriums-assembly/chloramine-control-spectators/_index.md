---
title: "Chloramine Control for Spectators"
description: "Engineering strategies for protecting spectators from chloramine exposure in natatoriums through air barriers, dilution ventilation, and pressure control systems."
keywords: ["chloramine control", "spectator protection", "natatorium ventilation", "trichloramine limits", "air curtains", "dilution ventilation", "indoor air quality", "pool spectator areas"]
weight: 2
---

## Overview

Spectator areas in competitive natatoriums face unique air quality challenges from chloramine migration. Trichloramine (NCl₃), the primary airborne contaminant, originates from the pool deck and disperses through buoyancy-driven airflows. Protecting spectators requires engineered barriers and dedicated ventilation to maintain acceptable indoor air quality while minimizing cross-contamination.

ASHRAE Standard 62.1 establishes general ventilation requirements, while the ASHRAE Applications Handbook Chapter 6 provides natatorium-specific guidance. The critical design challenge is preventing chloramine-laden air from the pool deck (elevated temperature, high humidity, contaminant source) from reaching spectator zones through thermal stratification and pressure differentials.

## Chloramine Exposure Limits

Trichloramine concentrations must remain below established exposure thresholds:

**Exposure Guidelines:**
- **Occupational limit**: 0.5 mg/m³ (8-hour TWA)
- **Spectator target**: 0.2 mg/m³ (comfort threshold)
- **Detection threshold**: 0.02 mg/m³ (odor perception)

The relationship between source strength and spectator exposure depends on air exchange effectiveness:

$$C_s = \frac{G \cdot (1 - \eta)}{Q_s \cdot E}$$

Where:
- $C_s$ = spectator zone concentration (mg/m³)
- $G$ = chloramine generation rate at pool surface (mg/hr)
- $\eta$ = barrier effectiveness (0-1)
- $Q_s$ = spectator ventilation rate (m³/hr)
- $E$ = ventilation effectiveness factor (0.5-1.0)

## Air Barrier Strategies

### Physical Separation

Architectural and mechanical barriers prevent chloramine migration:

1. **Elevation differential**: Position spectator seating 1.5-3 m above pool deck to exploit thermal stratification
2. **Glazing barriers**: Full-height glass partitions with sealed joints (infiltration < 0.1 ACH)
3. **Air curtains**: Vertical jet systems at transitions (discharge velocity 3-5 m/s)

**Air Curtain Design:**

$$v_j = v_c \sqrt{\frac{\rho_c}{\rho_j}}$$

Where:
- $v_j$ = jet discharge velocity (m/s)
- $v_c$ = crossflow velocity to block (m/s)
- $\rho_c$ = crossflow air density (kg/m³)
- $\rho_j$ = jet air density (kg/m³)

For typical natatoriums with 0.5 m/s crossflow, minimum discharge velocity is 3.5 m/s across a 2.5 m height.

### Pressure Relationships

Maintain positive pressure in spectator areas relative to pool deck:

**Target Differentials:**
- Spectator to pool deck: +2.5 to +5 Pa
- Spectator to exterior: +5 to +7.5 Pa
- Pool deck to natatorium support spaces: -2.5 Pa

Monitor pressure continuously with building automation systems; alarms trigger at ±1 Pa deviation from setpoint.

## Dilution Ventilation

{{< mermaid >}}
graph TB
    A[Pool Surface<br/>Chloramine Source] -->|Thermal Plume| B[Pool Deck Zone<br/>30-32°C, 60% RH]
    B -->|Barrier Interface| C{Air Barrier}
    C -->|Leakage η=0.9| D[Spectator Zone<br/>22-24°C, 50% RH]
    E[Exhaust 8-10 ACH] --> B
    F[Supply 6-8 ACH] --> D
    G[Return Above Pool] --> B
    D --> H[Exhaust Low Level]

    style A fill:#ffcccc
    style B fill:#ffe6cc
    style D fill:#ccffcc
    style C fill:#cce5ff
{{< /mermaid >}}

### Ventilation Requirements

**Spectator Zone Air Change Rates:**

| Condition | Air Changes/Hour | Outdoor Air Minimum |
|-----------|------------------|---------------------|
| Separated (glazed barrier) | 6-8 ACH | 15 cfm/person |
| Open connection | 10-12 ACH | 20 cfm/person |
| Competition events | 8-10 ACH | 20 cfm/person |

**Pool Deck Requirements:**
- Minimum: 6 ACH with 100% outdoor air
- Typical: 8-10 ACH for competitive facilities
- High-use: 12-15 ACH for intensive training

### Dilution Ventilation Calculation

Required ventilation to achieve target concentration:

$$Q = \frac{G \cdot (1 - \eta)}{C_s \cdot E \cdot 3600}$$

**Example Calculation:**
- Pool chloramine generation: $G = 500$ mg/hr
- Barrier effectiveness: $\eta = 0.90$
- Target spectator concentration: $C_s = 0.2$ mg/m³
- Ventilation effectiveness: $E = 0.8$

$$Q = \frac{500 \cdot (1 - 0.90)}{0.2 \cdot 0.8 \cdot 3600} = 0.087 \text{ m}^3\text{/s} = 184 \text{ cfm}$$

For 500-seat spectator area (volume 5,000 m³), this yields 6.3 ACH—confirming the 6-8 ACH design guideline.

## Control Method Comparison

| Method | Effectiveness | Capital Cost | Operating Cost | Maintenance | Application |
|--------|---------------|--------------|----------------|-------------|-------------|
| **Full glazing barrier** | 90-95% | High | Low | Low | New construction |
| **Air curtain** | 70-85% | Medium | Medium | Medium | Retrofit, transitions |
| **Pressure control** | 60-75% | Medium | Medium | Low | Open plans |
| **High dilution (12+ ACH)** | 80-90% | Low | Very High | Low | Budget-limited |
| **Combined barrier + dilution** | 95-98% | High | Medium | Medium | Competition venues |

## System Design Integration

### Supply Air Distribution

**Spectator Zone:**
- Overhead diffusers with horizontal throw
- Supply temperature 13-16°C below space temperature
- Maximum terminal velocity 0.25 m/s in occupied zone
- Locate returns at low level to capture any infiltrated contaminants

**Pool Deck Interface:**
- Exhaust at pool surface level (return grilles 0.3-0.6 m above deck)
- High sidewall supply directed across water surface
- Avoid short-circuiting between supply and return

### Air Cleaning Supplemental

While source control and dilution are primary strategies, supplemental air cleaning provides additional protection:

**Activated Carbon:**
- Chloramine removal efficiency: 40-60%
- Media depth: 50-100 mm
- Face velocity: 2.5 m/s maximum
- Replacement: annually or at 50% breakthrough

**UV-C Photolysis:**
- Effective wavelength: 254 nm
- Dose requirement: 1000-2000 μW·s/cm²
- Placement: in-duct or upper room
- Maintenance: lamp replacement every 12-18 months

## Monitoring and Verification

**Continuous Monitoring:**
1. Differential pressure (pool deck to spectator zone)
2. Temperature stratification (deck vs. spectator)
3. Relative humidity (both zones)
4. CO₂ concentration (occupancy proxy)

**Periodic Testing:**
- Trichloramine concentration (quarterly)
- Air change rate verification (smoke tests, tracer gas)
- Air curtain velocity profile (annually)
- Barrier leakage rates (annually)

Maintain trichloramine below 0.3 mg/m³ in spectator areas during events. Concentrations exceeding 0.4 mg/m³ require immediate investigation and corrective action.

## Source Control Integration

Effective spectator protection begins with minimizing chloramine generation:

1. **Water chemistry**: Maintain free chlorine 2-4 ppm, combined chlorine < 0.2 ppm
2. **Bather load management**: Enforce pre-swim hygiene
3. **UV or ozone supplemental treatment**: Reduce chlorine demand
4. **Continuous circulation**: 6-8 hour turnover rate minimum

When pool deck concentrations remain below 0.5 mg/m³, achieving spectator targets becomes achievable with standard barrier and ventilation strategies.

## References

- ASHRAE Standard 62.1: Ventilation for Acceptable Indoor Air Quality
- ASHRAE Applications Handbook, Chapter 6: Natatoriums
- WHO Guidelines for Safe Recreational Water Environments, Volume 2: Swimming Pools and Similar Environments
- CDC Model Aquatic Health Code (MAHC)
