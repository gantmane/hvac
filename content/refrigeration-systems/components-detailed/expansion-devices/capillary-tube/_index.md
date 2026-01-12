---
title: "Capillary Tube Expansion Devices"
description: "Technical analysis of capillary tube expansion devices including flow characteristics, sizing methodology, critical flow conditions, suction line heat exchange, and refrigerant charge effects in vapor compression refrigeration systems."
weight: 3
---

Capillary tubes serve as fixed-orifice expansion devices in small vapor compression refrigeration systems, providing a simple, cost-effective means of refrigerant metering without moving parts. The device operates by imposing a precisely calculated pressure drop through viscous friction and acceleration effects in a small-diameter tube.

## Operating Principles

The capillary tube performs two critical functions in the refrigeration cycle:

1. **Pressure reduction**: Reduces high-side pressure to evaporator pressure through frictional resistance
2. **Flow metering**: Controls refrigerant mass flow rate through fixed geometric resistance

Unlike modulating expansion valves, capillary tubes provide no active control response to varying load conditions. The system self-regulates through pressure equilibration during off-cycles and charge-dependent operating characteristics.

## Flow Characteristics

### Critical Flow (Choked Flow)

Critical flow occurs when refrigerant velocity reaches sonic conditions at the tube exit. This phenomenon limits maximum mass flow rate regardless of further downstream pressure reduction.

**Critical flow conditions:**
- Exit pressure ratio < 0.5 to 0.6 of inlet pressure (refrigerant-dependent)
- Refrigerant reaches saturation during expansion
- Two-phase mixture at tube exit
- Maximum possible mass flow rate for given inlet conditions

The critical pressure ratio varies by refrigerant:

| Refrigerant | Critical Pressure Ratio | Typical Application |
|-------------|------------------------|---------------------|
| R-134a | 0.54 - 0.58 | Domestic refrigeration |
| R-410A | 0.52 - 0.56 | Small heat pumps |
| R-600a | 0.56 - 0.60 | Hydrocarbon systems |
| R-290 | 0.55 - 0.59 | Commercial refrigeration |

### Subcritical Flow

When evaporator pressure exceeds the critical pressure ratio, subcritical flow exists. Mass flow rate becomes sensitive to both upstream and downstream conditions, resulting in reduced system stability.

**Subcritical flow characteristics:**
- Downstream pressure influences flow rate
- Reduced refrigerant metering precision
- Potential for capacity oscillation
- Generally undesirable operating regime

## Pressure Drop Mechanisms

Total pressure drop in a capillary tube results from:

**Frictional pressure drop:**
ΔP_f = f × (L/D) × (ρV²/2)

Where:
- f = Darcy friction factor
- L = tube length (ft or m)
- D = internal diameter (in or mm)
- ρ = refrigerant density (lb/ft³ or kg/m³)
- V = refrigerant velocity (ft/s or m/s)

**Acceleration pressure drop:**
ΔP_a = ṁ(V_exit - V_inlet)/A

Acceleration effects dominate when refrigerant flashes to two-phase flow, with vapor generation increasing mixture velocity significantly.

## Sizing Methodology

Proper capillary tube selection requires matching:
- Refrigerant mass flow rate to compressor displacement
- Pressure drop to achieve design evaporator pressure
- Subcooling requirement at tube inlet

### Empirical Sizing Approach

1. **Determine required refrigerant flow rate:**
   ṁ = (Q_evap)/(h_evap_out - h_evap_in)

2. **Calculate refrigerant properties at capillary inlet:**
   - Subcooled liquid temperature
   - Pressure (condensing pressure)
   - Enthalpy and density

3. **Select tube diameter and length combination** from manufacturer data or empirical correlations

4. **Verify critical flow conditions** at design operating point

### Common Sizing Parameters

| System Capacity | Tube ID | Typical Length | Refrigerant |
|----------------|---------|----------------|-------------|
| 1/8 ton | 0.028 in (0.71 mm) | 60-80 in | R-134a |
| 1/4 ton | 0.031 in (0.79 mm) | 70-100 in | R-134a |
| 1/3 ton | 0.036 in (0.91 mm) | 80-120 in | R-134a |
| 1/2 ton | 0.042 in (1.07 mm) | 90-140 in | R-134a |
| 3/4 ton | 0.050 in (1.27 mm) | 100-160 in | R-410A |
| 1 ton | 0.055 in (1.40 mm) | 120-180 in | R-410A |

**Note:** Length varies significantly with operating conditions, subcooling, and suction line heat exchange configuration.

## Suction Line Heat Exchange

Capillary tube-suction line heat exchangers improve system performance by:

1. **Increasing subcooling**: Ensures liquid refrigerant enters capillary tube
2. **Preventing compressor liquid slugging**: Superheats suction vapor
3. **Improving capacity**: Reduces flash gas at expansion device inlet

### Heat Exchange Configuration

The capillary tube attaches to the suction line over a specified length, typically:
- 12-36 inches (300-900 mm) contact length
- Soldered or brazed thermal bond
- Located after suction line service valve
- Insulated as assembly

**Thermal effectiveness:**
ε = (T_cap_in - T_cap_out)/(T_cap_in - T_suct_in)

Typical effectiveness: 0.4-0.7 depending on contact length and refrigerant

### Performance Impact

| Parameter | Without Heat Exchange | With Heat Exchange | Change |
|-----------|----------------------|-------------------|---------|
| Subcooling | 5-8°F | 12-18°F | +7-10°F |
| Suction superheat | 8-12°F | 15-25°F | +7-13°F |
| System capacity | Baseline | +2-5% | Increase |
| COP | Baseline | +3-8% | Increase |

## Refrigerant Charge Effects

Capillary tube systems exhibit charge-critical behavior. The refrigerant charge directly determines:
- Condensing pressure
- Subcooling entering expansion device
- Mass flow rate
- System capacity and efficiency

### Charge Sensitivity

**Undercharged condition:**
- Reduced condensing pressure
- Insufficient subcooling
- Flash gas at capillary inlet
- Reduced capacity (approximately 3-5% per 10% charge deficit)
- Potential evaporator starvation

**Overcharged condition:**
- Elevated condensing pressure
- Excessive subcooling
- Liquid refrigerant in suction line
- Reduced efficiency
- Compressor liquid slugging risk

**Optimal charge determination:**
- Specific to system geometry
- Verified by subcooling measurement (8-15°F typical)
- Fine-tuned during commissioning
- Typically ±5% tolerance for acceptable performance

## Installation Requirements

### Slope and Orientation

Capillary tubes must maintain specific orientation:

**Horizontal installation:**
- Slope downward minimum 1/4 in per foot toward evaporator
- Prevents oil trapping
- Ensures liquid seal at inlet

**Vertical installation:**
- Liquid flow downward preferred
- Upward flow acceptable if inlet seal maintained
- Avoid gas pockets at inlet

### Physical Constraints

- **No kinks or bends**: Restricts flow, unpredictable pressure drop
- **Minimum bend radius**: 6 × tube OD minimum
- **Support spacing**: Every 12-18 inches to prevent vibration damage
- **Clearance**: Avoid contact with sharp edges or heat sources
- **Service access**: Cannot be field-adjusted, must allow replacement

## Applications and Limitations

### Suitable Applications

Capillary tubes work best in:
- **Residential refrigerators/freezers**: Constant load, fixed conditions
- **Small window air conditioners**: Cost-sensitive, simple design
- **Dehumidifiers**: Steady-state operation
- **Water coolers**: Limited capacity variation
- **Small commercial refrigeration**: Vending machines, compact coolers

**Advantages:**
- Low cost (no moving parts)
- High reliability
- Silent operation
- Pressure equalization during off-cycle (reduced starting torque)
- No external power requirement

### Limitations

**Not suitable for:**
- Variable load applications
- Wide ambient temperature variation
- Frequent cycling with rapid pull-down
- Systems requiring capacity modulation
- Applications exceeding ~5 tons

**Performance constraints:**
- Fixed metering (no load adjustment)
- Charge-critical operation
- Poor tolerance to condenser fouling
- Limited superheat control
- Inefficient at off-design conditions

## Design Considerations

### System Matching

Successful capillary tube application requires:

1. **Compressor selection**: Displacement matched to capillary flow at design point
2. **Condenser sizing**: Adequate capacity to achieve required subcooling across load range
3. **Evaporator sizing**: Sufficient surface to evaporate metered refrigerant
4. **Charge optimization**: Precise charge for design subcooling

### Operating Range

Capillary tube systems should operate within:
- Condensing temperature: ±10°F of design point
- Evaporating temperature: ±5°F of design point
- Ambient temperature: ±15°F of design point

Operation outside these ranges results in:
- Incorrect superheat
- Capacity degradation
- Potential compressor damage

## Troubleshooting Guide

| Symptom | Probable Cause | Verification Method |
|---------|---------------|---------------------|
| Low suction pressure | Restriction in capillary | Temperature drop along tube |
| High superheat | Undercharge or restriction | Check subcooling, capacity |
| Low superheat | Overcharge | Measure subcooling >20°F |
| Frosted capillary | Flash gas at inlet | Insufficient subcooling |
| Capacity loss | Partial blockage | Compare to design flow |
| Compressor short-cycle | Oversized capillary | Rapid pressure equalization |

## Selection Procedure Summary

1. Establish design operating conditions (evaporator/condenser temperatures)
2. Calculate required refrigerant mass flow rate from load
3. Determine available subcooling at capillary inlet
4. Select tube diameter (smaller = higher ΔP per unit length)
5. Calculate required length for design pressure drop
6. Verify critical flow at design point
7. Design suction line heat exchanger (if used)
8. Specify installation requirements
9. Determine optimal refrigerant charge

## Performance Optimization

**Maximizing efficiency:**
- Use suction line heat exchange to increase subcooling
- Optimize condenser performance for consistent subcooling
- Maintain clean condenser surfaces
- Verify correct refrigerant charge annually
- Ensure proper airflow across all heat exchangers

**Extending operating range:**
- Increase tube length (reduces sensitivity to pressure variation)
- Maximize subcooling through enhanced heat exchange
- Oversized condenser for improved charge tolerance

Capillary tube expansion devices offer an economical, reliable solution for fixed-load refrigeration applications where simplicity and low cost outweigh the performance advantages of modulating expansion valves. Proper sizing and charge optimization are essential for achieving design performance and long-term reliability.
