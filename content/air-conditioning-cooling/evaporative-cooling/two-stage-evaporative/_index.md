---
title: "Two-Stage Evaporative Cooling"
description: "Design and performance of two-stage indirect-direct evaporative cooling systems achieving supply temperatures below outdoor wet-bulb."
keywords: ["two-stage evaporative", "indirect-direct", "hybrid evaporative", "sub-wet-bulb cooling", "IDEC", "evaporative cooling"]
weight: 3
---

Two-stage evaporative cooling combines indirect and direct stages to achieve supply air temperatures below the outdoor wet-bulb temperature—a thermodynamic impossibility with single-stage systems. This configuration maximizes evaporative cooling effectiveness while managing humidity addition.

## System Configuration

### Indirect-Direct Arrangement

The standard two-stage configuration:

**Stage 1 - Indirect Evaporative Cooling (IEC)**:
- Pre-cools outdoor air sensibly
- No moisture addition to supply air
- Reduces dry-bulb without affecting wet-bulb
- Sets up favorable conditions for Stage 2

**Stage 2 - Direct Evaporative Cooling (DEC)**:
- Further cools pre-cooled air
- Adds moisture through adiabatic saturation
- Achieves lowest possible supply temperature

### Process Path on Psychrometric Chart

```
Outdoor Air → [IEC: horizontal left] → [DEC: diagonal toward saturation] → Supply
```

The two-stage process reaches lower temperatures because Stage 1 reduces the dry-bulb while the wet-bulb remains unchanged, increasing the wet-bulb depression available for Stage 2.

## Thermodynamic Analysis

### Stage 1: Indirect Cooling

$$T_{1,out} = T_{OA} - \epsilon_{IEC}(T_{OA} - T_{wb,OA})$$

The wet-bulb temperature remains constant:
$$T_{wb,1} = T_{wb,OA}$$

### Stage 2: Direct Cooling

Using pre-cooled air with unchanged wet-bulb:
$$T_{supply} = T_{1,out} - \epsilon_{DEC}(T_{1,out} - T_{wb,1})$$

### Combined Effectiveness

Overall wet-bulb effectiveness exceeds either stage alone:

$$\epsilon_{total} = \epsilon_{IEC} + \epsilon_{DEC}(1 - \epsilon_{IEC})$$

Example: εIEC = 70%, εDEC = 85%
$$\epsilon_{total} = 0.70 + 0.85(1 - 0.70) = 0.70 + 0.255 = 0.955$$

### Sub-Wet-Bulb Achievement

Two-stage systems achieve supply temperatures below outdoor wet-bulb when:
$$T_{supply} < T_{wb,OA}$$

This occurs when combined effectiveness exceeds 100%:
$$T_{supply} = T_{OA} - \epsilon_{total}(T_{OA} - T_{wb,OA})$$

## Performance Example

**Design Conditions**: 105°F DB / 70°F WB outdoor

**Stage 1 (IEC, 70% effective)**:
- Temperature drop: 0.70 × (105 - 70) = 24.5°F
- After Stage 1: 105 - 24.5 = 80.5°F DB / 70°F WB

**Stage 2 (DEC, 85% effective)**:
- Temperature drop: 0.85 × (80.5 - 70) = 8.9°F
- Supply air: 80.5 - 8.9 = 71.6°F DB

**Result**: Supply air (71.6°F) is below outdoor wet-bulb (70°F)!

### Performance Comparison

| Condition | DEC Only | Two-Stage |
|-----------|----------|-----------|
| 105°F/70°F WB | 75°F | 71.6°F |
| 100°F/66°F WB | 71°F | 68.3°F |
| 95°F/65°F WB | 70°F | 67.6°F |

## System Components

### Integrated Packaged Units

Factory-assembled two-stage coolers:

**Components**:
- Indirect heat exchanger (plate or tube)
- Direct media section (rigid cellulose)
- Two water systems (may share sump)
- Separate or common fans
- Integrated controls

**Capacities**: 3,000-30,000+ CFM

### Built-Up Systems

Custom configurations for large installations:

- Separate IEC and DEC modules
- Central station AHU integration
- Multiple stages for ultra-low temperatures
- Process cooling applications

### Water Systems

Each stage requires water management:

**IEC Water System**:
- Secondary airstream wetting
- Recirculating pump
- Lower evaporation rate
- Bleed-off for concentration control

**DEC Water System**:
- Media wetting distribution
- Higher evaporation rate
- Combined or separate sump options

## Control Strategies

### Staged Operation

Sequential control based on conditions:

1. **Mild conditions**: IEC only
2. **Warm conditions**: IEC + DEC
3. **Hot conditions**: Maximum staging

### Variable Speed Control

Modulating fan speeds optimize efficiency:

- Primary fan: Matches supply CFM demand
- Secondary fan: Balances effectiveness vs. energy
- Pumps: Ensure adequate wetting

### Leaving Air Temperature Control

Supply temperature setpoint control:

$$T_{setpoint} = f(outdoor\ conditions,\ load)$$

Controller modulates stages to maintain setpoint.

## Energy Performance

### Comparison with Mechanical Cooling

Two-stage evaporative vs. DX cooling:

| Metric | Two-Stage Evap | DX Cooling |
|--------|----------------|------------|
| EER | 30-50 | 10-14 |
| Peak kW/ton | 0.3-0.5 | 0.9-1.2 |
| Water use | 3-4 gal/ton·hr | 0 |
| Peak demand | 60-75% reduction | Baseline |

### Annual Energy Analysis

Bin analysis determines annual performance:

$$Energy_{annual} = \sum_{bins} hours_i \times \frac{Q_i}{EER_i}$$

Compare two-stage evaporative, single-stage, and mechanical systems for lifecycle cost.

## Applications

### Commercial Buildings

Excellent fit for:
- Office buildings in dry climates
- Retail and big-box stores
- Schools and universities
- Gymnasiums and recreation

### Industrial Facilities

Process and comfort cooling:
- Manufacturing plants
- Warehouses
- Aircraft hangars
- Assembly facilities

### Data Centers

Growing application:
- Free cooling hours maximized
- PUE improvement
- Backup mechanical for peak
- ASHRAE climate zones 1-5

## Design Considerations

### Climate Suitability

Two-stage most effective when:
- Outdoor RH < 50% design
- Wet-bulb depression > 20°F
- Hot-dry summer climate
- Extended cooling season

### Humidity Management

Stage 2 adds moisture—consider:
- Leaving humidity acceptable for application
- Ventilation rate dilutes indoor humidity
- Bypass damper for humidity-sensitive periods

### First Cost vs. Operating Cost

Higher equipment cost offset by:
- Lower operating energy
- Reduced peak demand charges
- Lower maintenance than mechanical

### Water Availability

Total consumption both stages:
$$\dot{m}_{water} ≈ \frac{Q_{total}}{h_{fg}} + Bleed$$

Typically 4-6 gal/ton·hr total

Two-stage evaporative cooling provides the ultimate evaporative cooling performance, achieving supply temperatures impossible with single-stage systems while maintaining exceptional energy efficiency in appropriate climates.
