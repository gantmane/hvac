---
title: "Evaporative Cooling Systems"
description: "Comprehensive guide to evaporative cooling technologies including direct, indirect, and two-stage systems for energy-efficient HVAC applications."
keywords: ["evaporative cooling", "swamp cooler", "direct evaporative", "indirect evaporative", "adiabatic cooling", "HVAC"]
weight: 20
---

Evaporative cooling harnesses the thermodynamic process of water evaporation to provide sensible cooling with minimal energy input. These systems offer compelling advantages in appropriate climates, delivering significant energy savings compared to vapor-compression refrigeration.

## Fundamental Principles

### Psychrometric Basis

Evaporative cooling exploits the conversion of sensible heat to latent heat during water evaporation. The process follows constant wet-bulb temperature lines on the psychrometric chart.

**Adiabatic Saturation**:
$$h_1 = h_2$$ (neglecting work input)

The cooling potential depends on the wet-bulb depression:
$$\Delta T_{max} = T_{db} - T_{wb}$$

### Cooling Effectiveness

Evaporative cooler effectiveness measures actual cooling relative to maximum possible:

$$\epsilon = \frac{T_{db,in} - T_{db,out}}{T_{db,in} - T_{wb,in}}$$

**Typical Effectiveness Values**:
- Direct evaporative: 70-95%
- Indirect evaporative: 50-80%
- Two-stage indirect-direct: 100-120% (below inlet wet-bulb)

### Energy Efficiency

Evaporative coolers consume only fan and pump power:

$$EER_{evap} = \frac{Q_{cooling}}{W_{fan} + W_{pump}}$$

Typical values: 15-40 EER vs. 8-14 for vapor-compression systems

## System Types Overview

### Direct Evaporative Cooling (DEC)

Supply air contacts water directly, providing cooling with moisture addition:

- Air passes through wetted media
- Temperature drops toward wet-bulb
- Humidity increases toward saturation
- Best for dry climates (<40% RH outdoor)

### Indirect Evaporative Cooling (IEC)

Primary air is cooled without moisture addition via heat exchange:

- Secondary air stream evaporatively cooled
- Heat exchanger transfers cooling to supply air
- Supply air remains at constant humidity ratio
- Applicable in wider climate range

### Two-Stage Systems

Combining indirect and direct stages achieves lowest temperatures:

1. **Stage 1** (Indirect): Pre-cool without adding moisture
2. **Stage 2** (Direct): Further cool with evaporation

Achieves supply temperatures below outdoor wet-bulb.

## Climate Suitability

### Hot-Dry Climates

Ideal conditions for evaporative cooling:
- Wet-bulb depression: >20°F
- Design wet-bulb: <65°F
- Low outdoor humidity: <30% RH

**Excellent regions**: Southwest US, Mediterranean, Middle East, Australia interior

### Hot-Humid Limitations

Limited effectiveness when:
- Wet-bulb depression: <10°F
- Outdoor humidity: >50% RH
- Required supply temperature below achievable

**Alternative approach**: Indirect evaporative pre-cooling of condenser air

### Transition Climates

Hybrid systems combine evaporative and mechanical cooling:
- Evaporative operation when effective
- Mechanical backup for humid periods
- Automatic changeover based on conditions

## Applications

### Commercial Buildings

- **Warehouses and distribution**: High volume, low cost
- **Data centers**: Indirect or hybrid systems
- **Retail**: Big-box stores in dry climates
- **Outdoor air pre-cooling**: Energy recovery

### Industrial

- **Process cooling**: Manufacturing facilities
- **Spot cooling**: Worker comfort stations
- **Turbine inlet cooling**: Power generation efficiency
- **Agricultural**: Greenhouse and livestock cooling

### Residential

- **Whole-house cooling**: Traditional "swamp coolers"
- **Room coolers**: Portable units
- **Hybrid systems**: Mini-split backup

## Energy and Water Considerations

### Energy Savings

Compared to vapor-compression:
- 60-80% energy reduction in suitable climates
- Peak demand reduction
- Reduced refrigerant-related environmental impact

### Water Consumption

Evaporation rate:
$$\dot{m}_{water} = \frac{Q_{cooling}}{h_{fg}} \approx 3\ gal/ton \cdot hr$$

Additional water for bleed-off prevents mineral concentration:
- Total consumption: 4-5 gal/ton·hr typical
- Water quality affects media life
- Reclaimed water potential

## System Selection

### Decision Factors

1. **Climate data**: Wet-bulb frequency analysis
2. **Cooling requirements**: Temperature and humidity targets
3. **Water availability**: Cost and quality
4. **Energy costs**: Electric rates and demand charges
5. **Maintenance capability**: Media replacement, water treatment

### Performance Analysis

Evaluate annual performance using bin data:
$$Q_{annual} = \sum_{bins} hours_i \times Q_i(\epsilon, T_{wb,i})$$

Compare total cost of ownership vs. alternatives.

Evaporative cooling provides an environmentally responsible, energy-efficient cooling strategy when matched appropriately to climate conditions and application requirements.
