---
title: "Direct Evaporative Cooling"
description: "Design principles and applications of direct evaporative cooling systems including media types, performance characteristics, and system configurations."
keywords: ["direct evaporative cooling", "swamp cooler", "evaporative media", "adiabatic cooling", "wetted pad", "DEC"]
weight: 1
---

Direct evaporative cooling (DEC) passes air directly through wetted media, achieving sensible cooling through the adiabatic saturation process. This fundamental cooling technology offers exceptional energy efficiency in appropriate climates.

## Operating Principles

### Adiabatic Saturation Process

In direct evaporative cooling, air contacts water at the wet-bulb temperature:

$$T_{out} = T_{in} - \epsilon (T_{in} - T_{wb,in})$$

Where:
- $T_{out}$ = leaving dry-bulb temperature
- $T_{in}$ = entering dry-bulb temperature
- $T_{wb,in}$ = entering wet-bulb temperature
- $\epsilon$ = saturation effectiveness (0.7-0.95)

### Humidity Addition

Moisture content increases as sensible heat converts to latent:

$$W_{out} = W_{in} + \frac{c_p (T_{in} - T_{out})}{h_{fg}}$$

The leaving relative humidity approaches saturation (85-95% RH).

### Heat and Mass Transfer

Combined heat and mass transfer governs performance:

$$\dot{Q} = h_c A (T_{air} - T_{water}) + h_m A h_{fg} (W_{sat,water} - W_{air})$$

The Lewis relation connects heat and mass transfer coefficients:
$$\frac{h_c}{h_m c_p} \approx 1$$ (Lewis number ≈ 1 for air-water)

## Media Types

### Rigid Media (Cellulose)

Cross-corrugated cellulose pads dominate commercial applications:

**Construction**:
- Kraft paper impregnated with anti-rot compounds
- Cross-fluted design creates turbulent flow
- Standard thicknesses: 6", 12", 18"
- Available widths: 12-60 inches

**Performance**:
| Thickness | Effectiveness | Pressure Drop |
|-----------|---------------|---------------|
| 6" | 70-75% | 0.10-0.15" w.g. |
| 12" | 85-90% | 0.20-0.30" w.g. |
| 18" | 90-95% | 0.30-0.40" w.g. |

**Service Life**: 5-10 years with proper maintenance

### Aspen Pads

Traditional residential and small commercial media:

- Random fiber packing (aspen wood excelsior)
- Lower cost than rigid media
- Effectiveness: 60-70%
- Shorter life: 1-3 seasons
- Requires more frequent replacement

### Synthetic Media

Engineered plastic or fiberglass media:

- Washable and reusable
- Consistent performance over time
- Higher initial cost
- Suitable for harsh water conditions

## System Components

### Water Distribution

Uniform wetting ensures maximum effectiveness:

**Distribution Methods**:
- Gravity overflow troughs
- Spray headers with nozzles
- Recirculating pump systems

**Design Requirements**:
- Flow rate: 1.5-3 GPM per linear foot of media
- Coverage: 100% media saturation
- Even distribution prevents dry spots

### Sump and Pump

Recirculating water system includes:

- Sump capacity: 5-10 gallons per face ft²
- Pump sizing: 3-5 GPM/ft² face area
- Float valve for makeup water
- Overflow/bleed connection

### Air Moving

Fan selection for evaporative coolers:

$$CFM = \frac{Q_{sensible}}{1.08 \times (T_{room} - T_{supply})}$$

**Face Velocity**: 400-600 fpm through media (500 typical)

## Performance Characteristics

### Effectiveness Factors

Saturation effectiveness depends on:

1. **Media depth**: Deeper = higher effectiveness
2. **Face velocity**: Lower velocity = higher effectiveness
3. **Media condition**: Clean, properly wetted
4. **Water temperature**: Approach to wet-bulb

### Performance Curves

Typical direct evaporative cooler performance:

| Inlet DB | Inlet WB | Effectiveness | Outlet DB | Outlet RH |
|----------|----------|---------------|-----------|-----------|
| 100°F | 66°F | 85% | 71°F | 85% |
| 95°F | 65°F | 85% | 70°F | 85% |
| 90°F | 64°F | 85% | 68°F | 85% |
| 105°F | 70°F | 85% | 75°F | 85% |

### Capacity

Cooling capacity:

$$Q = 1.08 \times CFM \times (T_{in} - T_{out})$$

Example: 10,000 CFM, 100°F inlet, 71°F outlet
$$Q = 1.08 \times 10,000 \times 29 = 313,200\ Btu/h = 26\ tons$$

## System Configurations

### Packaged Rooftop Units

Complete factory-assembled coolers:
- Capacities: 1,000-30,000+ CFM
- Horizontal or downdraft discharge
- Pre-piped water connections
- Integrated controls

### Side-Draft Units

Ground or wall-mounted:
- Horizontal airflow through media
- Suitable for residential/light commercial
- Gravity water distribution
- Capacities: 2,000-10,000 CFM

### Built-Up Systems

Custom installations for large applications:
- Multiple media banks
- Plenum construction
- Central station AHU integration
- Capacities: 10,000-200,000+ CFM

## Control Strategies

### Basic Control

Simple on/off control:
- Thermostat starts fan and pump
- Pump starts before fan (pre-wet cycle)
- Timer delay between stages

### Variable Speed

Modulating capacity:
- Variable frequency drive on fan
- Speed varies with cooling demand
- Maintains leaving air temperature
- Improved part-load efficiency

### Economizer Integration

Outdoor air economizer mode:
1. Free cooling when outdoor < indoor
2. DEC when outdoor dry-bulb elevated
3. Mechanical backup when DEC insufficient

## Limitations

### Climate Constraints

Direct evaporative cooling limited by:
- Outdoor wet-bulb temperature
- Required supply air temperature
- Indoor humidity tolerance

**Rule of Thumb**: Effective when outdoor RH < 40%

### Indoor Humidity

Moisture addition may cause:
- Occupant discomfort at high supply RH
- Material damage in humidity-sensitive areas
- Mold growth potential in conditioned space

**Mitigation**: Increased ventilation rate flushes moisture

### Water Quality Effects

Hard water causes:
- Scale buildup on media
- Reduced effectiveness
- Shortened media life
- Increased maintenance

Treatment options: Bleed-off, softening, chemical treatment

Direct evaporative cooling delivers outstanding energy efficiency when climate conditions and application requirements align, providing sustainable cooling with minimal environmental impact.
