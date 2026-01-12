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

## Advanced Flow Analysis

### Two-Phase Flow Regimes

As refrigerant expands through the capillary tube, distinct flow regimes develop:

**Single-phase liquid region:**
- Inlet section where refrigerant remains subcooled
- Pressure drop primarily frictional
- Length depends on subcooling and tube geometry
- Reynolds number typically 500-2000 (laminar to transitional)

**Metastable region:**
- Refrigerant below saturation pressure but remains liquid
- Nucleation delay due to surface tension effects
- Length: 1-10 tube diameters
- Highly unstable, sensitive to surface roughness

**Two-phase region:**
- Flash evaporation initiates
- Vapor generation accelerates flow
- Dominates total pressure drop
- Exit quality typically 0.15-0.35

### Flow Quality at Exit

The refrigerant quality (vapor fraction) at capillary tube exit significantly affects evaporator performance:

x = (h_exit - h_f)/(h_fg)

Where:
- x = vapor quality (dimensionless)
- h_exit = enthalpy at tube exit (Btu/lb or kJ/kg)
- h_f = saturated liquid enthalpy at exit pressure
- h_fg = latent heat of vaporization at exit pressure

| Inlet Subcooling | Exit Quality | Flash Gas Penalty | Effective Capacity |
|------------------|--------------|-------------------|-------------------|
| 0°F | 0.32-0.38 | High | 70-75% |
| 5°F | 0.25-0.30 | Moderate | 78-82% |
| 10°F | 0.18-0.24 | Low | 85-88% |
| 15°F | 0.12-0.18 | Minimal | 90-93% |
| 20°F | 0.08-0.14 | Very low | 94-96% |

## Detailed Sizing Correlations

### Empirical Flow Equations

Several correlations predict capillary tube mass flow rate. The Hopkins-based correlation:

ṁ = C × D^a × L^b × ΔP^c × ρ^d

Typical exponents for R-134a:
- a = 2.5 to 2.7 (diameter dominates)
- b = -0.4 to -0.5 (inverse length relationship)
- c = 0.45 to 0.55 (pressure differential impact)
- d = 0.3 to 0.4 (density contribution)
- C = empirical constant (refrigerant-specific)

### Dimensionless Analysis

The capillary tube performance can be characterized by dimensionless groups:

**Reynolds number at inlet:**
Re = (ρVD)/μ

**Pressure drop ratio:**
Π = ΔP/P_inlet

**Length-to-diameter ratio:**
L/D = 800 to 4000 (typical range)

Higher L/D ratios provide:
- Greater flow stability
- Reduced sensitivity to charge variation
- More gradual pressure recovery after flashing
- Improved tolerance to manufacturing variations

## Refrigerant-Specific Characteristics

### Property Effects on Sizing

Different refrigerants require different tube geometries for equivalent capacity:

| Refrigerant | Vapor Density Ratio | Viscosity | Required L/D vs R-134a | Typical ID Range |
|-------------|---------------------|-----------|------------------------|------------------|
| R-134a | 1.00 (baseline) | 1.00 | 1.00 | 0.028-0.055 in |
| R-410A | 1.45 | 1.12 | 0.85-0.90 | 0.026-0.050 in |
| R-290 (Propane) | 0.78 | 0.88 | 1.10-1.15 | 0.030-0.058 in |
| R-600a (Isobutane) | 0.52 | 0.82 | 1.25-1.35 | 0.032-0.062 in |
| R-32 | 1.68 | 1.05 | 0.80-0.85 | 0.024-0.048 in |
| R-744 (CO₂) | 3.20 | 1.42 | 0.45-0.55 | 0.015-0.035 in |

### Critical Pressure Considerations

CO₂ transcritical systems require special capillary tube design:
- Gas cooler outlet at supercritical pressure (1000-1400 psi)
- Extreme pressure ratio (10:1 to 20:1)
- Single-phase to two-phase transition at critical point
- Requires shorter tubes with precise diameter control

## Manufacturing Tolerances

Capillary tube performance is highly sensitive to dimensional variations:

| Parameter | Tolerance | Flow Impact | Quality Control Method |
|-----------|-----------|-------------|------------------------|
| Internal diameter | ±0.001 in | ±12-18% | Laser measurement, air flow test |
| Length | ±0.5 in | ±2-4% | Precision cutting, verification |
| Surface roughness | Ra < 8 μin | ±3-6% | Honing, electropolishing |
| Circularity | <5% ovality | ±4-8% | Drawn tubing specification |
| Inlet edge | Sharp, burr-free | ±5-10% | Chamfering, deburring |

**Manufacturing process control:**
- Drawn seamless copper tubing (ASTM B280)
- Internal diameter verified by air flow calibration
- Length cut with precision tube cutter
- Ends reamed and deburred
- Sample testing for flow capacity verification

## Heat Exchanger Design Details

### Optimized Suction Line Contact

The effectiveness of suction line heat exchange depends on contact configuration:

**Soldered bond design:**
- Capillary tube positioned along bottom of suction line
- Continuous solder fillet along contact length
- Thermal conductivity: 200-240 Btu/(hr·ft·°F) for copper
- Contact thermal resistance: 0.01-0.03 (hr·ft·°F)/Btu

**Heat transfer analysis:**

Q = UA(LMTD)

Where:
- U = overall heat transfer coefficient: 15-30 Btu/(hr·ft²·°F)
- A = contact surface area
- LMTD = log mean temperature difference

| Contact Length | Subcooling Increase | Superheat Increase | Effectiveness | COP Improvement |
|----------------|---------------------|--------------------|--------------|-----------------|
| 12 in (300 mm) | 4-6°F | 5-8°F | 0.35-0.45 | +2-3% |
| 18 in (450 mm) | 6-9°F | 8-12°F | 0.45-0.55 | +3-5% |
| 24 in (600 mm) | 8-12°F | 10-15°F | 0.50-0.60 | +4-6% |
| 36 in (900 mm) | 10-15°F | 13-20°F | 0.60-0.70 | +5-8% |

### Insulation Requirements

The capillary-suction line assembly requires external insulation:
- Minimum R-4 foam insulation
- Closed-cell structure to prevent moisture ingress
- Temperature rating: -40°F to 180°F
- Thickness: 0.375-0.5 in typical

## Field Service Procedures

### Restriction Diagnosis

Capillary tube restrictions manifest as:

**Temperature profile analysis:**
- Normal operation: Gradual temperature drop along length
- Partial blockage: Abrupt temperature drop at restriction point
- Complete blockage: No temperature change after obstruction

**Pressure differential measurement:**
- Install pressure taps before and after suspected restriction
- Normal ΔP: 150-250 psi for typical small systems
- Restricted ΔP: >300 psi or insufficient evaporator pressure

**Common restriction causes:**
- Moisture freeze-out (ice formation)
- Contamination particles
- Oil sludge accumulation
- Wax precipitation (with mineral oil)
- Copper oxide scale

### Replacement Procedure

Capillary tube replacement requires:

1. **System evacuation**: Recover refrigerant per EPA Section 608
2. **Component access**: Disconnect at filter-drier and evaporator inlet
3. **Dimensional verification**: Measure existing tube ID and length
4. **New tube installation**:
   - Cut to exact length
   - Deburr both ends
   - Install with proper orientation
   - Braze connections with 15% silver alloy
5. **Leak test**: Pressurize to 150% operating pressure
6. **System cleanup**: Install new filter-drier
7. **Evacuation**: Deep vacuum to 500 microns
8. **Recharge**: Weigh-in specified refrigerant charge
9. **Performance verification**: Measure subcooling and superheat

## Blockage Prevention

### Filter-Drier Integration

Capillary tube systems require filter-driers positioned immediately before the tube inlet:

**Filter-drier specifications:**
- XH-9 or equivalent desiccant (10-15 gram capacity for small systems)
- 40-micron filtration minimum
- Pressure drop <2 psi at design flow
- Located in liquid line before capillary
- Replaced after any compressor burnout

### Moisture Control

Moisture in capillary tube systems causes:

**Ice formation at flashing point:**
- Occurs when moisture content >50 ppm by weight
- Forms at location where refrigerant reaches 32°F
- Blocks flow, creates system short-cycling
- Temporary during initial cool-down

**Prevention methods:**
- Triple evacuation during installation
- Deep vacuum <500 microns before charging
- Proper filter-drier selection and installation
- Minimize system open time during service
- Use dry nitrogen for leak testing

## Performance Under Varying Conditions

### Ambient Temperature Effects

Capillary tube performance varies with ambient conditions:

| Ambient Temp | Condensing Pressure | Subcooling | Mass Flow | Capacity | COP |
|--------------|---------------------|------------|-----------|----------|-----|
| 70°F | 130 psia | 12°F | 100% | 100% | 100% |
| 80°F | 155 psia | 10°F | 108% | 102% | 96% |
| 90°F | 185 psia | 8°F | 116% | 103% | 91% |
| 100°F | 220 psia | 6°F | 122% | 102% | 85% |
| 110°F | 260 psia | 4°F | 126% | 98% | 78% |

**Key observations:**
- Mass flow increases with condensing pressure
- Subcooling decreases as ambient rises
- Capacity peaks then declines at high ambient
- Efficiency degrades significantly above design point

### Part-Load Performance

Capillary tubes exhibit poor part-load efficiency:
- Cannot modulate flow to match reduced load
- System cycles on-off to maintain setpoint
- Cycling losses: 2-5% of full-load efficiency per cycle/hour
- Compressor short-cycling risk at very light loads

## Comparison with Other Expansion Devices

| Feature | Capillary Tube | TXV | EEV | Fixed Orifice |
|---------|---------------|-----|-----|---------------|
| Cost | $ | $$$ | $$$$ | $ |
| Complexity | Very low | Medium | High | Very low |
| Load response | None | Good | Excellent | None |
| Superheat control | None | Fixed setpoint | Variable | None |
| Efficiency | Design point only | Good | Excellent | Design point only |
| Reliability | Excellent | Good | Fair | Excellent |
| Service | Replace only | Adjustable | Requires calibration | Replace only |
| Typical capacity | <2 tons | 0.5-100+ tons | 1-100+ tons | <5 tons |
| Pressure equalization | Yes | No | No | Yes |
| Starting torque | Low | High | High | Low |

## Advanced Applications

### Dual Capillary Systems

Some systems employ parallel capillary tubes for improved turndown:
- Two tubes with solenoid valve on one circuit
- Single tube operation at low load
- Both tubes at high load
- Provides 2:1 capacity modulation
- Common in room dehumidifiers

### Adiabatic vs Non-Adiabatic

**Adiabatic capillary tubes:**
- No heat exchange with surroundings
- Simpler analysis
- Lower performance
- Shorter required length

**Non-adiabatic (suction line heat exchange):**
- Heat transfer increases subcooling
- Improved capacity and efficiency
- More complex sizing
- Standard in modern appliances

## Quality Assurance and Testing

### Factory Flow Testing

Manufacturers verify capillary tube performance through:

**Air flow correlation method:**
- Measure air flow at specified pressure differential
- Correlate to refrigerant flow via empirical relationships
- Fast, non-destructive testing
- Accuracy: ±5% of design flow

**Refrigerant flow bench:**
- Direct measurement with refrigerant at design conditions
- Higher accuracy (±2-3%)
- More complex test setup
- Used for validation and development

### Installation Verification

After installation, verify proper operation:

**Superheat method:**
- Measure suction line temperature and pressure
- Calculate superheat: 8-15°F typical for properly charged system
- Too high: undercharge or restriction
- Too low: overcharge

**Subcooling method:**
- Measure liquid line temperature and pressure at condenser outlet
- Calculate subcooling: 8-15°F typical
- Too low: undercharge or poor condenser performance
- Too high: overcharge

**Performance verification:**
- Measure system capacity via temperature and airflow
- Compare to nameplate rating
- Should achieve 95-105% of rated capacity at design conditions

## Regulatory and Safety Considerations

### Refrigerant Containment

Capillary tube connections must meet:
- ASHRAE 15 requirements for refrigerant containment
- Brazed joints required (no mechanical fittings)
- Leak rate <0.5% annually
- Pressure test to 1.5× operating pressure minimum

### Flammable Refrigerant Precautions

A2L and A3 refrigerants (R-290, R-32, R-1234yf) require:
- Charge size limits per ASHRAE 15
- Ventilation requirements in mechanical spaces
- Leak detection in commercial applications
- Special brazing procedures to prevent contamination
- Grounding to prevent static discharge

## Future Trends

### Microchannel Integration

Emerging designs integrate capillary function into heat exchanger headers:
- Eliminates discrete capillary tube component
- Optimizes refrigerant distribution
- Reduces system volume and charge
- Improves transient response

### Smart Capillary Systems

Development of electronically-augmented capillary tubes:
- Integrated flow sensor
- Temperature monitoring
- Diagnostic capability
- Predictive maintenance alerts
- Remains passive expansion but adds intelligence

Capillary tube expansion devices offer an economical, reliable solution for fixed-load refrigeration applications where simplicity and low cost outweigh the performance advantages of modulating expansion valves. Proper sizing, charge optimization, and installation practices are essential for achieving design performance and long-term reliability in residential and light commercial refrigeration systems.
