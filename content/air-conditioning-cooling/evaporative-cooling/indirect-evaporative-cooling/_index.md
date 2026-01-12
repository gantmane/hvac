---
title: "Indirect Evaporative Cooling"
description: "Design and application of indirect evaporative cooling systems that provide sensible cooling without adding moisture to supply air."
keywords: ["indirect evaporative cooling", "IEC", "dew-point cooling", "plate heat exchanger", "sensible cooling", "dry cooling"]
weight: 2
---

Indirect evaporative cooling (IEC) provides sensible cooling to supply air without adding moisture, overcoming a key limitation of direct evaporative systems. By separating the supply airstream from the evaporative process, IEC extends evaporative cooling applicability to humidity-sensitive applications.

## Operating Principles

### Two-Airstream Concept

IEC systems use two separate airstreams:

**Primary Air** (Product/Supply):
- Air delivered to conditioned space
- Cooled by heat exchange
- No moisture added

**Secondary Air** (Working/Scavenger):
- Evaporatively cooled
- Absorbs heat from primary
- Exhausted outdoors

### Heat Exchange Process

Heat transfer occurs across an exchange surface:

$$Q = UA \times LMTD$$

Where LMTD accounts for temperature differences between streams.

**Primary Air Cooling**:
$$T_{primary,out} = T_{primary,in} - \epsilon_{sensible}(T_{primary,in} - T_{secondary,wb})$$

### Effectiveness Definition

IEC effectiveness relates outlet temperature to wet-bulb approach:

**Wet-Bulb Effectiveness**:
$$\epsilon_{wb} = \frac{T_{1,in} - T_{1,out}}{T_{1,in} - T_{2,wb,in}}$$

Typical values: 50-80% for conventional IEC

## Heat Exchanger Types

### Plate-Type Exchangers

Parallel plates separate primary and secondary streams:

**Construction**:
- Aluminum or polymer plates
- Alternating primary/secondary passages
- Secondary side wetted for evaporation
- Cross-flow or counter-flow arrangement

**Performance**:
- Effectiveness: 50-70%
- Pressure drop: 0.3-0.5" w.g. each stream
- Compact design
- Moderate cost

### Tube-Type Exchangers

Air flows through or around tubes:

**Configuration**:
- Primary air inside tubes
- Secondary air over wetted tubes
- Vertical tube orientation common
- Enhanced surfaces available

**Characteristics**:
- Robust construction
- Higher pressure capability
- Easier maintenance
- Lower effectiveness than plate

### Heat Pipe Exchangers

Two-phase heat transfer mechanism:

- Evaporator section in hot stream
- Condenser section in cool stream
- Working fluid transfers heat
- No cross-contamination

### Regenerative (M-Cycle) Exchangers

Advanced design achieves sub-wet-bulb cooling:

**Maisotsenko Cycle**:
1. Primary air pre-cools through dry channels
2. Portion diverted to wet channels
3. Evaporative cooling in wet channels
4. Counter-flow heat exchange

**Performance**:
- Achieves 80-90% dew-point effectiveness
- Supply temperature approaches dew-point
- Highest efficiency IEC technology

## Performance Characteristics

### Wet-Bulb Approach

Primary air outlet approaches secondary wet-bulb:

| IEC Type | Wet-Bulb Approach | Typical Effectiveness |
|----------|-------------------|----------------------|
| Cross-flow plate | 15-25°F | 50-60% |
| Counter-flow plate | 10-20°F | 60-75% |
| Regenerative | 5-10°F | 80-90% |

### Airflow Ratio

Secondary-to-primary flow ratio affects performance:

$$Ratio = \frac{\dot{m}_{secondary}}{\dot{m}_{primary}}$$

Typical range: 0.3-1.0

Higher ratio increases effectiveness but also:
- Fan energy consumption
- Water consumption
- Equipment size

### Cooling Capacity

Sensible cooling delivered:

$$Q_{sensible} = \dot{m}_{primary} \times c_p \times (T_{in} - T_{out})$$

Example: 10,000 CFM primary, 100°F inlet, 78°F outlet
$$Q = 1.08 \times 10,000 \times 22 = 237,600\ Btu/h ≈ 20\ tons$$

## System Configurations

### Standalone IEC Units

Pre-packaged indirect coolers:
- Self-contained with fans and pumps
- Outdoor air intake
- Supply air delivery
- Capacities: 5,000-50,000 CFM

### AHU Integration

IEC section within air handling unit:
- Pre-cooling outdoor air
- Upstream of cooling coil
- Reduces mechanical cooling load
- Energy recovery function

### Hybrid Systems

Combined IEC with mechanical cooling:
- IEC provides first-stage cooling
- DX or chilled water for trim cooling
- Optimizes efficiency across conditions
- Automatic staging based on demand

## Advantages Over Direct Evaporative

### No Moisture Addition

Supply air humidity unchanged:
- Suitable for humidity-sensitive spaces
- Offices, retail, data centers
- Museums and archives
- Healthcare facilities

### Wider Climate Applicability

Effective in moderately humid climates:
- Operates when direct evaporative marginal
- Useful to 60% outdoor RH
- More consistent performance

### Better Indoor Air Quality

No water contact with supply air:
- Eliminates microbial growth concern
- No carryover of treatment chemicals
- Cleaner supply air

## Design Considerations

### Airstream Arrangement

**Counter-flow**: Maximum effectiveness
**Cross-flow**: Lower pressure drop, simpler construction
**Parallel-flow**: Lowest effectiveness (rarely used)

### Secondary Air Source

Options for secondary airstream:

1. **100% Outdoor Air**: Maximum cooling potential
2. **Exhaust Air**: Energy recovery mode (ERV function)
3. **Return Air**: Not recommended (humidity concern)

### Water Management

Secondary side wetting requirements:
- Continuous recirculating spray
- Drip-type distribution
- Media-assisted wetting

Water quality and treatment similar to direct evaporative.

### Pressure Drop Budget

Both airstreams require fan energy:

$$W_{total} = \frac{\dot{V}_1 \Delta P_1}{\eta_1} + \frac{\dot{V}_2 \Delta P_2}{\eta_2}$$

Balance effectiveness vs. fan energy in design.

## Applications

### Data Center Cooling

IEC increasingly specified for data centers:
- ASHRAE TC 9.9 expanded temperature envelope
- Significant energy savings
- Partial cooling adequate for much of year
- DX backup for peak conditions

### Commercial Buildings

Suitable for many commercial applications:
- Office buildings in dry to moderate climates
- Pre-cooling for conventional systems
- Dedicated outdoor air systems (DOAS)

### Industrial Processes

Process cooling applications:
- Cooling without humidity increase
- Make-up air systems
- Equipment heat rejection

Indirect evaporative cooling provides the energy efficiency benefits of evaporative technology while maintaining supply air humidity control, enabling broader application across building types and climates.
