---
title: "Short Tube Orifice Expansion Devices"
description: "Technical analysis of short tube orifice expansion devices in refrigeration systems, including flow characteristics, pressure-flow relationships, sizing methods, and heat pump applications"
weight: 5
---

## Overview

Short tube orifices represent a fixed expansion device category characterized by length-to-diameter ratios typically between 2:1 and 20:1. These devices differ from capillary tubes through their significantly shorter length and larger diameter, creating distinct flow regimes and pressure-drop characteristics. Short tube orifices find primary application in heat pump systems where bidirectional refrigerant flow requires symmetric pressure reduction capability.

The fundamental operating principle relies on converting refrigerant pressure energy into kinetic energy through geometric restriction, followed by dissipation of this kinetic energy downstream of the restriction. Unlike capillary tubes where friction dominates pressure drop, short tube orifices derive pressure reduction primarily from entrance effects and acceleration losses.

## Flow Characteristics

### Flow Regimes

Short tube orifice flow exhibits three distinct regimes depending on operating conditions:

**Subcooled Liquid Flow**
- Occurs when upstream refrigerant remains entirely liquid
- Pressure drop follows incompressible flow equations
- Mass flow rate increases with increasing subcooling
- Bernoulli equation provides reasonable flow prediction

**Two-Phase Flow**
- Develops when pressure drops below saturation pressure within orifice
- Flash gas formation creates accelerating two-phase mixture
- Choked flow conditions possible at high pressure ratios
- Most common operating regime in heat pump applications

**Choked Flow**
- Establishes when downstream pressure cannot influence upstream flow
- Mass flow rate becomes independent of evaporator pressure
- Critical pressure ratio typically between 0.5 and 0.7
- Provides stable expansion device operation

### Pressure-Flow Relationships

The relationship between pressure differential and mass flow rate depends on flow regime and refrigerant properties.

For subcooled liquid flow:

ṁ = Cd × A × √(2ρ × ΔP)

Where:
- ṁ = mass flow rate (kg/s)
- Cd = discharge coefficient (0.6-0.85)
- A = orifice cross-sectional area (m²)
- ρ = liquid density (kg/m³)
- ΔP = pressure drop (Pa)

For two-phase and choked flow, empirical correlations account for flash gas formation:

ṁ = C × A × √(2ρl × ΔP) × (1 - x)^n

Where:
- ρl = liquid density at inlet conditions
- x = quality at orifice exit
- n = empirical exponent (typically 0.4-0.6)
- C = modified discharge coefficient

## Geometric Parameters

### Orifice Diameter

Orifice diameter represents the critical sizing parameter, typically ranging from 0.8 mm to 3.0 mm for residential equipment.

**Diameter Effects:**
- Larger diameters increase mass flow rate quadratically
- Smaller diameters provide greater pressure reduction
- Manufacturing tolerances critically impact performance
- Diameter selection depends on system capacity and refrigerant type

### Length-to-Diameter Ratio

The L/D ratio distinguishes short tube orifices from other expansion devices.

| L/D Ratio | Classification | Flow Characteristics |
|-----------|---------------|---------------------|
| 2:1 - 5:1 | Sharp-edge orifice | Entrance-dominated losses |
| 5:1 - 10:1 | Short tube | Mixed entrance and friction losses |
| 10:1 - 20:1 | Long short tube | Significant friction component |
| >20:1 | Capillary tube | Friction-dominated flow |

**L/D Ratio Impact:**
- Lower ratios exhibit higher discharge coefficients
- Higher ratios provide more stable flow characteristics
- Optimal ratio depends on application requirements
- Typical heat pump applications use L/D = 8:1 to 12:1

### Entrance Geometry

Entrance configuration significantly influences flow characteristics and discharge coefficient.

**Sharp-Edge Entrance:**
- Creates flow separation and vena contracta
- Discharge coefficient: 0.60-0.65
- Simple manufacturing
- Higher pressure drop per unit length

**Rounded Entrance:**
- Reduces separation losses
- Discharge coefficient: 0.75-0.85
- Requires precision machining
- More efficient flow transition

**Chamfered Entrance:**
- Intermediate performance characteristics
- Discharge coefficient: 0.68-0.75
- Balance of cost and efficiency
- Common in commercial applications

## Sizing Methodology

### Design Capacity Calculation

Short tube orifice sizing begins with determining required refrigerant mass flow rate:

ṁrequired = Qcooling / (hevap,out - hevap,in)

Where:
- Qcooling = cooling capacity (kW)
- hevap,out = evaporator exit enthalpy (kJ/kg)
- hevap,in = evaporator inlet enthalpy (kJ/kg)

### Diameter Selection

For specified operating conditions, orifice diameter calculation proceeds iteratively:

1. Determine inlet pressure and temperature
2. Calculate liquid density and subcooling
3. Establish design pressure drop
4. Select initial L/D ratio
5. Calculate required area from flow equation
6. Determine diameter: D = √(4A/π)
7. Verify performance across operating range

### Performance Verification

Critical operating points require verification:

**High Load Conditions:**
- Maximum condensing temperature
- Maximum subcooling
- Verify adequate flow capacity
- Prevent refrigerant underfeeding

**Low Load Conditions:**
- Minimum condensing temperature
- Minimum subcooling
- Verify against overfeeding
- Maintain acceptable superheat

**Intermediate Conditions:**
- Part-load performance
- Refrigerant distribution quality
- System efficiency optimization
- Control stability

## Heat Pump Applications

### Bidirectional Flow Requirements

Heat pump systems require expansion capability in both flow directions, making short tube orifices particularly suitable.

**Cooling Mode:**
- Flow from outdoor coil to indoor coil
- Primary orifice handles full capacity
- Check valve bypasses reverse-flow orifice

**Heating Mode:**
- Flow reverses to indoor to outdoor direction
- Secondary orifice becomes active
- Check valve configuration switches flow path

### Orifice Pairing Strategy

Heat pump systems typically employ two short tube orifices with associated check valves.

| Configuration | Cooling Orifice | Heating Orifice | Application |
|--------------|----------------|-----------------|-------------|
| Matched | 1.5 mm | 1.5 mm | Equal capacity modes |
| Unbalanced | 1.6 mm | 1.4 mm | Heating-priority systems |
| Capacity-adjusted | 1.7 mm | 1.5 mm | Climate-specific optimization |
| High-efficiency | 1.4 mm | 1.4 mm | Reduced tolerance design |

### Check Valve Integration

Check valve selection impacts system efficiency and reliability:

**Critical Parameters:**
- Opening pressure differential: 5-15 kPa typical
- Flow coefficient when open: minimize pressure drop
- Sealing capability when closed: prevent bypass flow
- Temperature rating: -40°C to 120°C range required

## Comparison with Capillary Tubes

### Performance Differences

| Parameter | Short Tube Orifice | Capillary Tube |
|-----------|-------------------|----------------|
| Length | 10-100 mm | 1-6 m |
| Diameter | 0.8-3.0 mm | 0.5-2.0 mm |
| L/D Ratio | 2:1 to 20:1 | 50:1 to 3000:1 |
| Pressure drop mechanism | Entrance losses | Friction losses |
| Flow stability | Moderate | High |
| Manufacturing tolerance | Critical | Less sensitive |
| Heat pump suitability | Excellent | Poor |
| Cost | Moderate | Low |

### Selection Criteria

**Choose Short Tube Orifice When:**
- Heat pump application requires bidirectional flow
- Compact device dimensions needed
- Fast response to pressure changes desired
- Multiple refrigerant options considered
- System employs accumulator for charge management

**Choose Capillary Tube When:**
- Unidirectional flow only required
- Critical charge system desired
- Maximum system simplicity needed
- Cost minimization paramount
- Longer tube routing acceptable

## Installation Considerations

### Orientation Requirements

Short tube orifice orientation affects performance through several mechanisms:

**Horizontal Installation:**
- Standard orientation for most applications
- Uniform flow distribution
- Minimal gravitational effects
- Preferred for manufacturing consistency

**Vertical Upflow:**
- Liquid column provides additional pressure
- Slightly reduced flow rate
- Better flash gas distribution downstream
- Suitable for space-constrained installations

**Vertical Downflow:**
- Gravitational assistance to flow
- Slightly increased flow rate
- Potential for flow instability
- Generally avoided unless necessary

### Upstream Conditioning

Flow conditioning upstream of the orifice influences performance:

**Straight Pipe Length:**
- Minimum 10D upstream straight length
- Eliminates approach velocity profile effects
- Reduces discharge coefficient variation
- Critical for consistent performance

**Filter-Drier Location:**
- Install upstream of orifice
- Prevents orifice contamination
- Protects against flow restriction
- Typical distance: 150-300 mm upstream

**Subcooling Control:**
- Adequate subcooling prevents vapor formation upstream
- Target subcooling: 8-15°C for stability
- Monitor subcooling across operating range
- Consider subcooling control strategies

## Specifications and Standards

### Common Orifice Sizes

Standard short tube orifice specifications for R-410A residential heat pumps:

| Nominal Capacity (kW) | Cooling Orifice (mm) | Heating Orifice (mm) | Length (mm) | L/D Ratio |
|----------------------|---------------------|---------------------|-------------|-----------|
| 5.3 (1.5 ton) | 1.40 | 1.35 | 16 | 11.4 |
| 7.0 (2 ton) | 1.55 | 1.50 | 18 | 11.6 |
| 8.8 (2.5 ton) | 1.70 | 1.65 | 20 | 11.8 |
| 10.5 (3 ton) | 1.85 | 1.80 | 22 | 11.9 |
| 12.3 (3.5 ton) | 2.00 | 1.95 | 24 | 12.0 |
| 14.0 (4 ton) | 2.15 | 2.10 | 26 | 12.1 |
| 17.6 (5 ton) | 2.40 | 2.35 | 30 | 12.5 |

### Material Requirements

**Orifice Body:**
- Brass (C36000) most common
- Stainless steel (304/316) for corrosive environments
- Copper alloys for specific applications
- Surface finish: Ra < 0.8 μm

**Assembly Components:**
- Housing compatible with refrigerant and oil
- O-rings: HNBR or FKM materials
- Check valve seats: wear-resistant polymers
- Temperature rating exceeds system requirements

## Performance Optimization

### Discharge Coefficient Enhancement

Optimizing discharge coefficient increases capacity without diameter changes:

**Approach Strategies:**
- Entrance radius optimization: 0.05D to 0.15D
- Surface finish improvement: electropolishing
- Length refinement for L/D ratio
- Upstream flow straightening

**Typical Improvements:**
- Sharp edge to radiused: 15-20% capacity increase
- Surface finish optimization: 3-5% capacity increase
- Flow conditioning: 2-3% variation reduction

### Multi-Orifice Configurations

Some applications employ multiple orifices for capacity modulation:

**Parallel Orifice Design:**
- Two or more orifices in parallel
- Solenoid valves enable/disable individual orifices
- Step capacity control capability
- Increased system complexity and cost

**Series Orifice Design:**
- Two orifices in series
- Greater total pressure drop
- Improved flow stability
- Reduced sensitivity to downstream conditions

## Troubleshooting

### Common Issues

**Insufficient Superheat:**
- Orifice oversized for conditions
- Excessive subcooling at inlet
- Check valve leaking in reverse mode
- Solution: Verify orifice size, check valve operation

**Excessive Superheat:**
- Orifice undersized for load
- Insufficient subcooling at inlet
- Partial orifice restriction
- Solution: Clean or replace orifice, verify subcooling

**Hunting/Cycling:**
- System charge incorrect
- Inadequate accumulator volume
- Orifice size marginal
- Solution: Adjust charge, verify accumulator, consider orifice change

**Capacity Loss:**
- Orifice contamination/restriction
- Check valve failure
- Incorrect orifice installed
- Solution: System cleanup, component replacement

### Diagnostic Procedures

**Performance Verification:**
1. Measure liquid line temperature and pressure
2. Calculate actual subcooling
3. Measure suction line temperature and pressure
4. Calculate actual superheat
5. Compare to design values
6. Assess capacity and efficiency

**Flow Rate Verification:**
- Use system capacity and enthalpy change
- Compare to manufacturer specifications
- Account for operating condition variations
- Verify against orifice flow calculations

## Advanced Topics

### Refrigerant-Specific Behavior

Different refrigerants exhibit varying flow characteristics through short tube orifices:

**R-410A:**
- High operating pressures require robust construction
- Smaller orifices than R-22 for equivalent capacity
- Greater sensitivity to subcooling variations
- Zeotropic mixture considerations minimal

**R-32:**
- Lower pressure ratio than R-410A
- Larger orifice diameters for equivalent capacity
- Excellent heat transfer characteristics
- Single-component refrigerant simplifies analysis

**R-454B (Low-GWP Alternative):**
- Pressure-temperature characteristics similar to R-410A
- Zeotropic glide affects flash behavior
- Orifice sizing requires mixture property considerations
- Temperature glide impacts evaporator performance

### Computational Modeling

Advanced orifice design employs computational fluid dynamics (CFD) for optimization:

**Modeling Capabilities:**
- Three-dimensional flow field visualization
- Phase change prediction within orifice
- Discharge coefficient prediction
- Geometry optimization studies

**Validation Requirements:**
- Experimental data correlation
- Multiple operating point verification
- Refrigerant property accuracy
- Turbulence model selection

Understanding short tube orifice expansion device characteristics enables proper selection, sizing, and application in refrigeration and heat pump systems, optimizing performance across varied operating conditions.
