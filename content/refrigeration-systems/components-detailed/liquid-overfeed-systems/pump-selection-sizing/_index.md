---
title: "Pump Selection and Sizing for Liquid Overfeed Systems"
aliases: ["Pump Selection and Sizing for Liquid Overfeed Systems"]
description: "Comprehensive guide to refrigerant pump selection, NPSH requirements, flow calculations, and sizing methodology for industrial liquid overfeed refrigeration systems including ammonia applications"
weight: 11
---

## Overview

Refrigerant pump selection and sizing represents a critical engineering task in liquid overfeed refrigeration systems. Proper pump selection ensures adequate refrigerant circulation, maintains system efficiency, and prevents cavitation while minimizing power consumption. The pump must deliver sufficient flow at the required head while operating within acceptable NPSH margins across all operating conditions.

## Pump Configuration Types

### Hermetic Pumps

Hermetic refrigerant pumps feature a motor-pump assembly sealed within a pressure vessel, eliminating shaft seals and external leak points.

**Advantages:**
- Zero refrigerant leakage potential
- Simplified maintenance requirements
- Reduced installation complexity
- Improved safety for ammonia applications
- Lower labor costs for operation

**Limitations:**
- Limited motor cooling in low-temperature applications
- Higher initial equipment cost
- Entire assembly replacement on motor failure
- Maximum power typically 7.5 to 15 hp
- Limited serviceability in field

**Applications:**
- Systems with strict environmental requirements
- Ammonia systems where leak prevention is critical
- Installations with limited maintenance staff
- Low to medium capacity installations

### Open-Drive Pumps

Open-drive pumps utilize external motors with mechanical shaft seals, offering greater flexibility and serviceability.

**Advantages:**
- Higher horsepower availability (up to 200+ hp)
- Standard motor replacement capability
- Better motor cooling in all conditions
- Lower equipment replacement cost
- Field serviceable seals and bearings

**Limitations:**
- Mechanical seal maintenance requirements
- Potential for refrigerant leakage at seal
- Higher installation labor
- Additional space requirements
- Seal compatibility considerations

**Applications:**
- Large industrial refrigeration systems
- High-flow ammonia overfeed systems
- Facilities with maintenance capabilities
- Systems requiring variable speed operation

## Flow Rate Calculation Methodology

### Recirculation Ratio Determination

Flow rate requirements depend on the system recirculation ratio, defined as the ratio of liquid refrigerant circulated to vapor generated in the evaporators.

**Q_pump = Q_evap × n × CR**

Where:
- Q_pump = Total pump flow rate (gpm or kg/s)
- Q_evap = Total evaporator refrigeration capacity (tons or kW)
- n = Liquid circulation factor (2.5 to 4.5 typical)
- CR = Capacity ratio accounting for diversity

**Typical Recirculation Ratios:**

| Application | Circulation Ratio | Liquid Quality Exit |
|-------------|------------------|-------------------|
| Cold storage evaporators | 3.0 - 4.0 | 25% - 33% vapor |
| Blast freezers | 2.5 - 3.5 | 29% - 40% vapor |
| Process cooling | 3.5 - 4.5 | 22% - 29% vapor |
| Ice making | 2.5 - 3.0 | 33% - 40% vapor |
| Spiral freezers | 3.0 - 4.0 | 25% - 33% vapor |

### Mass Flow Calculation

**ṁ = (Q_ref × 12,000) / (h_fg × η_evap)**

Where:
- ṁ = Refrigerant mass flow (lb/hr)
- Q_ref = Refrigeration load (tons)
- h_fg = Latent heat of vaporization (Btu/lb)
- η_evap = Evaporator effectiveness (0.85 - 0.95)

### Volumetric Flow Conversion

**GPM = (ṁ × n) / (ρ_liq × 60 × 8.33)**

Where:
- GPM = Volumetric flow rate (gallons per minute)
- ṁ = Mass flow rate (lb/hr)
- n = Recirculation ratio
- ρ_liq = Liquid density (lb/gal)

## Total Dynamic Head Calculation

### System Head Components

**TDH = h_s + h_d + h_f + h_v + h_e**

Where:
- TDH = Total dynamic head (ft)
- h_s = Static lift (ft)
- h_d = Discharge pressure head (ft)
- h_f = Friction losses in piping (ft)
- h_v = Valve and fitting losses (ft)
- h_e = Evaporator pressure drop (ft)

### Friction Loss Estimation

**h_f = f × (L/D) × (v²/2g)**

Where:
- f = Friction factor (Darcy-Weisbach)
- L = Pipe length (ft)
- D = Pipe diameter (ft)
- v = Fluid velocity (ft/s)
- g = Gravitational acceleration (32.2 ft/s²)

### Typical System Head Requirements

| System Configuration | Total Head Range | Dominant Component |
|---------------------|-----------------|-------------------|
| Single-level evaporators | 30 - 80 ft | Evaporator ΔP |
| Multi-level facility | 80 - 150 ft | Static lift |
| Long piping runs | 60 - 120 ft | Friction loss |
| High ΔP evaporators | 50 - 100 ft | Coil resistance |

## NPSH Requirements for Ammonia Systems

### Net Positive Suction Head

NPSH Available must exceed NPSH Required by an adequate safety margin to prevent cavitation.

**NPSH_A = (P_vessel - P_vp) / (ρ × g) + h_static - h_f,suction**

Where:
- NPSH_A = Available NPSH (ft)
- P_vessel = Pump vessel absolute pressure (psi)
- P_vp = Vapor pressure at pumping temperature (psi)
- ρ = Liquid density (lb/ft³)
- g = Gravitational constant
- h_static = Static head on suction (ft)
- h_f,suction = Suction line friction loss (ft)

### NPSH Safety Margins

**NPSH_A ≥ NPSH_R + Safety Margin**

| Operating Condition | Minimum Safety Margin |
|--------------------|----------------------|
| Steady-state design | 5 ft |
| Load variations expected | 8 ft |
| High ambient conditions | 10 ft |
| Critical applications | 12 - 15 ft |
| Variable speed operation | 10 - 12 ft |

### Ammonia NPSH Considerations

Ammonia's high vapor pressure and low liquid density create challenging NPSH conditions:

**Critical Factors:**
- Maintain adequate vessel pressure (15 - 35 psig typical)
- Minimize suction line pressure drop
- Maximize static head from vessel to pump
- Use subcooled liquid when possible (2 - 5°F)
- Size suction piping for low velocity (< 3 ft/s)
- Avoid suction line restrictions

**Ammonia Liquid Density vs Temperature:**

| Temperature (°F) | Liquid Density (lb/ft³) | Vapor Pressure (psig) |
|-----------------|------------------------|----------------------|
| -40 | 43.5 | 10.4 |
| -20 | 42.5 | 18.3 |
| 0 | 41.4 | 30.4 |
| 20 | 40.3 | 48.2 |
| 40 | 39.1 | 73.3 |

## Pump Performance Characteristics

### Pump Curve Analysis

Centrifugal pump performance follows characteristic curves relating flow, head, efficiency, and power.

**Head-Flow Relationship:**
- Steep curve: Stable operation, flow sensitive to head
- Flat curve: Unstable at high flows
- Drooping curve: Avoid parallel pump operation

**Best Efficiency Point (BEP):**
- Target operation: 80% - 110% of BEP flow
- Efficiency penalty outside this range
- Increased wear at extreme flows
- Higher power consumption

### Pump Affinity Laws

**Flow relationship:**
**Q₂/Q₁ = (N₂/N₁)**

**Head relationship:**
**H₂/H₁ = (N₂/N₁)²**

**Power relationship:**
**P₂/P₁ = (N₂/N₁)³**

Where:
- Q = Flow rate
- H = Head
- P = Power
- N = Rotational speed
- Subscripts 1, 2 = Initial and final conditions

## Material Selection Requirements

### Wetted Component Materials

| Component | Ammonia Service | Halocarbon Service |
|-----------|----------------|-------------------|
| Impeller | 316 SS | 316 SS, bronze |
| Casing | Carbon steel, 316 SS | Cast iron, steel |
| Shaft | 316 SS, 17-4 PH | 316 SS, 400-series |
| Wear rings | 316 SS | Bronze, 316 SS |
| Fasteners | 316 SS | 316 SS, steel |

### Seal Material Compatibility

**Ammonia Applications:**
- Primary seal faces: Silicon carbide vs carbon
- Secondary seals: EPDM, Kalrez
- O-rings: EPDM, Buna-N (avoid)
- Gaskets: EPDM, Viton (limited)

**Halocarbon Applications:**
- Primary seal faces: Carbon vs ceramic
- Secondary seals: Viton, PTFE
- O-rings: Viton, Buna-N
- Gaskets: Compressed fiber, Viton

## Motor Sizing and Power Requirements

### Brake Horsepower Calculation

**BHP = (Q × H × SG) / (3,960 × η_pump)**

Where:
- BHP = Brake horsepower required
- Q = Flow rate (gpm)
- H = Total head (ft)
- SG = Specific gravity of refrigerant
- η_pump = Pump efficiency (decimal)

### Motor Safety Factor

**Motor HP = BHP × Service Factor**

| Application | Service Factor |
|-------------|---------------|
| Steady load, clean power | 1.15 - 1.20 |
| Variable load | 1.20 - 1.25 |
| Frequent starts | 1.25 - 1.30 |
| Harsh environment | 1.25 - 1.35 |
| Critical service | 1.30 - 1.50 |

### Variable Speed Drive Considerations

Variable frequency drives enable optimized pump operation across load ranges.

**Advantages:**
- Energy savings at part load (30% - 50% typical)
- Soft starting reduces mechanical stress
- Adjustable flow without throttling
- System pressure control capability
- Extended equipment life

**Design Requirements:**
- Minimum speed: 40% - 50% of full speed
- Maintain NPSH at all speeds
- Motor cooling verification at low speed
- Harmonic mitigation on electrical system
- VFD rated motor insulation

## Pump Efficiency and Performance

### Efficiency Factors

| Pump Size | Typical Efficiency Range |
|-----------|-------------------------|
| Small (< 5 hp) | 40% - 60% |
| Medium (5 - 25 hp) | 55% - 75% |
| Large (25 - 100 hp) | 65% - 80% |
| Very large (> 100 hp) | 70% - 85% |

### Performance Degradation

**Common Issues:**
- Wear ring clearance increase: 5% - 10% flow loss
- Impeller damage: 10% - 20% efficiency loss
- Seal leakage: Reduced NPSH, cavitation risk
- Bearing wear: Vibration, alignment issues

## Selection Procedure

### Step-by-Step Methodology

1. **Calculate refrigeration load and mass flow**
   - Determine total evaporator capacity
   - Apply diversity factors
   - Calculate refrigerant mass flow

2. **Select recirculation ratio**
   - Review application requirements
   - Consider evaporator types
   - Determine volumetric flow

3. **Calculate total dynamic head**
   - Static lift measurement
   - Friction loss calculation
   - Component pressure drops
   - Safety margin addition

4. **Verify NPSH availability**
   - Pump vessel pressure determination
   - Suction conditions analysis
   - Safety margin verification

5. **Select pump from manufacturer curves**
   - Plot duty point
   - Verify BEP proximity
   - Check efficiency
   - Confirm NPSH requirements

6. **Size motor and drive**
   - Calculate brake horsepower
   - Apply service factors
   - Evaluate VFD requirements

7. **Specify materials and seals**
   - Refrigerant compatibility
   - Environmental conditions
   - Maintenance preferences

## Lifecycle Cost Analysis

### Total Cost of Ownership

**LCC = IC + Σ(E_cost + M_cost + D_cost) - SV**

Where:
- LCC = Lifecycle cost
- IC = Initial capital cost
- E_cost = Annual energy cost
- M_cost = Annual maintenance cost
- D_cost = Downtime cost
- SV = Salvage value

### Economic Optimization

| Factor | Impact on LCC |
|--------|--------------|
| Pump efficiency | 40% - 60% of operating cost |
| Maintenance frequency | 15% - 25% of total cost |
| Equipment reliability | Downtime cost varies widely |
| Energy escalation | 3% - 5% annual increase typical |

**Analysis Period:**
- Typical evaluation: 15 - 20 years
- Discount rate: 6% - 10%
- Energy cost escalation: 3% - 5% annually

### Efficiency Investment Payback

Higher efficiency pumps typically show payback in 2 - 5 years through reduced operating costs, making premium efficiency selection economically justified for continuous operation applications.

## Practical Application Guidelines

**Best Practices:**
- Select pumps for 80% - 110% of BEP flow
- Provide minimum 5 ft NPSH margin for ammonia
- Use hermetic pumps for small systems (< 10 hp)
- Specify 316 stainless steel for ammonia wetted parts
- Consider VFD for loads varying > 30%
- Oversizing: Limit to 10% - 15% maximum
- Plan for parallel pump operation in large systems
- Include isolation valves for maintenance
- Provide pressure gauges at pump suction and discharge
- Install suction strainers for system protection