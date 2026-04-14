---
title: "Passive House (Passivhaus) Standard"
aliases: ["Passive House (Passivhaus) Standard"]
description: "Comprehensive guide to Passive House certification requirements including heating/cooling demand limits, airtightness testing, MVHR systems, and thermal envelope specifications for ultra-low energy buildings"
keywords: ["passive house", "passivhaus", "ultra low energy", "airtightness", "blower door test", "MVHR", "heat recovery ventilation", "thermal bridge", "PHPP", "specific heating demand", "primary energy demand"]
tags: ["passive house", "passivhaus", "ultra low energy", "airtightness", "blower door test", "MVHR", "heat recovery ventilation", "thermal bridge", "PHPP", "specific heating demand"]
weight: 4
---

## Overview

Passive House (Passivhaus in German) represents the most rigorous voluntary energy performance standard in construction. Developed at the Passive House Institute in Darmstadt, Germany, this standard achieves space heating and cooling energy reductions of up to 90% compared to conventional buildings through optimized building envelope design, exceptional airtightness, and mechanical ventilation with heat recovery.

The standard is climate-independent and applies globally through climate-specific adjustments in the Passive House Planning Package (PHPP) software.

## Performance Criteria

Passive House certification requires meeting stringent quantitative thresholds across multiple metrics:

### Energy Demand Limits

| Criteria | Requirement | Units |
|----------|-------------|-------|
| Annual Heating Demand | ≤ 15 | kWh/(m²·year) |
| Annual Cooling Demand | ≤ 15 | kWh/(m²·year) |
| Heating Load | ≤ 10 | W/m² |
| Primary Energy Demand | ≤ 120 | kWh/(m²·year) |
| Airtightness (ACH₅₀) | ≤ 0.6 | air changes/hour |
| Thermal Comfort | ≥ 90% | hours/year |

**Note:** All area calculations use Treated Floor Area (TFA), which is net interior conditioned floor area.

### Heating Demand Calculation

The specific heating demand is calculated using:

```
Qₕ = (Qₜ + Qᵥ) - ηᵤ(Qₛ + Qᵢ)
```

Where:
- **Qₕ** = Annual heating demand (kWh/year)
- **Qₜ** = Transmission heat losses through envelope (kWh/year)
- **Qᵥ** = Ventilation heat losses (kWh/year)
- **Qₛ** = Solar heat gains through windows (kWh/year)
- **Qᵢ** = Internal heat gains from occupants and equipment (kWh/year)
- **ηᵤ** = Utilization factor for gains (typically 0.6-0.95)

### Primary Energy Demand

Primary Energy Renewable (PER) is calculated:

```
PER = Σ(Eᵢ × PEFᵢ)
```

Where:
- **Eᵢ** = End energy consumption for service i (heating, cooling, DHW, appliances, auxiliary)
- **PEFᵢ** = Primary energy factor for energy carrier i
- PER must not exceed 120 kWh/(m²·year) for Classic standard

## Thermal Envelope Requirements

### U-Value Specifications

Maximum thermal transmittance values for Passive House components:

| Component | Maximum U-Value | Typical Achieved |
|-----------|-----------------|------------------|
| Walls | 0.15 W/(m²·K) | 0.10-0.12 W/(m²·K) |
| Roof | 0.15 W/(m²·K) | 0.08-0.10 W/(m²·K) |
| Floor Slab | 0.15 W/(m²·K) | 0.10-0.12 W/(m²·K) |
| Windows (Uᵥ) | 0.80 W/(m²·K) | 0.60-0.75 W/(m²·K) |
| Glazing (Uₘ) | 0.60 W/(m²·K) | 0.50-0.55 W/(m²·K) |

### Envelope Performance Diagram

```
═══════════════════════════════════════════════════════════
                    PASSIVE HOUSE ENVELOPE
═══════════════════════════════════════════════════════════

ROOF: U ≤ 0.15 W/(m²·K)
├─ Continuous insulation 300-450mm
├─ Air barrier integrated
└─ Thermal bridge-free connection to walls

         ↓ Solar Gains (Qs)
      ┌──────────────┐
      │ Triple Glazed│  WINDOWS: Uw ≤ 0.80 W/(m²·K)
      │   Ug ≤ 0.6   │  ├─ Triple pane, gas-filled
      │   g ≥ 0.50   │  ├─ Insulated frames
      └──────────────┘  └─ Warm edge spacers

WALLS: U ≤ 0.15 W/(m²·K)
├─ 250-400mm continuous insulation
├─ Airtight membrane
└─ No thermal bridging: Ψ ≤ 0.01 W/(m·K)

FOUNDATION: U ≤ 0.15 W/(m²·K)
├─ Sub-slab insulation 250-350mm
├─ Edge insulation
└─ Radon/moisture protection

         ↑ Ground Heat Loss (Qt)
═══════════════════════════════════════════════════════════
        TOTAL TRANSMISSION LOSSES ≤ 15 kWh/(m²·year)
═══════════════════════════════════════════════════════════
```

## Airtightness Requirements

### Blower Door Test Standard

Airtightness is verified through pressurization testing per EN 13829 or ASTM E779:

**ACH₅₀ ≤ 0.6 air changes per hour at 50 Pa pressure differential**

This translates to approximately 0.03-0.05 ACH under natural conditions.

**Air leakage rate calculation:**

```
n₅₀ = (V₅₀ / Vₑₙᵥₑₗₒₚₑ) × 60
```

Where:
- **n₅₀** = Air change rate at 50 Pa (ACH₅₀)
- **V₅₀** = Measured air flow rate at 50 Pa (m³/h)
- **Vₑₙᵥₑₗₒₚₑ** = Interior conditioned volume (m³)

### Critical Airtightness Details

Continuous air barrier must be maintained at:
- All penetrations (electrical, plumbing, HVAC)
- Window and door rough openings
- Envelope transitions (wall-to-roof, wall-to-foundation)
- Service chases and dropped ceilings

## Mechanical Ventilation with Heat Recovery (MVHR)

### System Requirements

Passive House requires continuous balanced ventilation with high-efficiency heat recovery:

| Parameter | Requirement |
|-----------|-------------|
| Heat Recovery Efficiency (ηₕᵣ) | ≥ 75% (typically 80-90%) |
| Electrical Efficiency | ≤ 0.45 Wh/m³ |
| Minimum Air Change Rate | 0.3 ACH |
| Fresh Air Supply | 30 m³/(h·person) |

### Heat Recovery Effectiveness

The sensible heat recovery efficiency is:

```
ηₕᵣ = (Tₛᵤₚₚₗᵧ - Tₒᵤₜdₒₒᵣ) / (Tᵢₙdₒₒᵣ - Tₒᵤₜdₒₒᵣ) × 100%
```

Example: With outdoor air at -10°C, indoor at 20°C, and supply at 14°C:

```
ηₕᵣ = (14 - (-10)) / (20 - (-10)) = 24/30 = 80%
```

### Ventilation Heat Loss Reduction

Annual ventilation heat loss with heat recovery:

```
Qᵥ = 0.33 × V̇ × HDD × (1 - ηₕᵣ)
```

Where:
- **V̇** = Ventilation air flow rate (m³/h)
- **HDD** = Heating degree days (K·d)
- **0.33** = Volumetric heat capacity of air (Wh/(m³·K))

## Certification Process

### Project Phases

**1. Design Phase**
- PHPP energy modeling
- Envelope design optimization
- MVHR system sizing
- Thermal bridge analysis
- Pre-certification review

**2. Construction Phase**
- Quality assurance protocols
- Airtightness testing (mid-construction and final)
- Thermal imaging verification
- Installation verification

**3. Certification**
- Final PHPP submission
- Blower door test results ≤ 0.6 ACH₅₀
- Documentation of as-built conditions
- Certificate issued by accredited Certifier

### PHPP Modeling Requirements

The Passive House Planning Package (PHPP) requires detailed inputs:
- Climate data (monthly temperature, solar radiation, humidity)
- Building geometry and orientation
- All envelope component U-values
- Window properties (Uw, Ug, Uf, g-value, Ψg)
- Thermal bridge catalog (Ψ-values)
- Ventilation system specifications
- Heating/cooling/DHW system efficiency
- Internal heat gains and occupancy schedules

## Passive House Classes

Three certification levels accommodate different project goals:

| Class | Primary Energy | Renewable Generation |
|-------|----------------|---------------------|
| Classic | ≤ 120 kWh/(m²·year) | Not required |
| Plus | ≤ 60 kWh/(m²·year) | ≥ 60 kWh/(m²·year) |
| Premium | ≤ 30 kWh/(m²·year) | ≥ 120 kWh/(m²·year) |

All classes must meet the same heating/cooling demand and airtightness requirements.

## Benefits and Challenges

**Performance Benefits:**
- 75-90% reduction in heating/cooling energy
- Elimination of conventional HVAC systems in many climates
- Superior indoor air quality through filtered ventilation
- Enhanced thermal comfort with minimal temperature stratification
- Resilience to energy price volatility

**Implementation Challenges:**
- Higher upfront construction costs (5-15% premium)
- Requires specialized design and construction expertise
- Limited availability of certified components in some markets
- More complex construction detailing and quality control
- Occupant education required for optimal performance

## Practical Considerations

**Climate Adaptations:**
- Cold climates: Focus on solar gains, minimize north glazing
- Hot climates: Reduce south glazing, maximize shading, cooling demand becomes limiting factor
- Humid climates: Dehumidification strategies, moisture control in envelope

**Cost Optimization:**
- Simple, compact building form reduces envelope area
- Strategic glazing placement maximizes passive solar gains
- Thermal bridge-free design reduces insulation requirements
- Optimize window-to-wall ratio (typically 20-30%)

The Passive House standard demonstrates that dramatic energy reductions are achievable through integrated envelope design, precision construction, and efficient ventilation systems, providing a proven pathway to near-zero energy buildings.
