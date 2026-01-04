---
title: "Chilled Water Systems for Cooling Applications"
description: "Comprehensive technical analysis of chilled water system design, including primary-secondary configurations, pump selection, differential pressure control, thermal storage, and energy optimization strategies with detailed calculations and performance curves."
keywords: ["chilled water systems", "primary-secondary pumping", "variable primary flow", "chiller performance curves", "delta-T syndrome", "pump selection", "differential pressure control", "waterside economizer", "thermal storage", "condenser water systems", "water treatment", "energy optimization"]
categories: ["Air Conditioning and Cooling"]
tags: ["chilled water", "chillers", "pumping systems", "system design", "energy efficiency", "thermal storage", "water treatment"]
author: "Evgeniy Gantman"
date: 2026-01-04
draft: false
---

Chilled water systems represent the primary cooling distribution method for medium to large commercial, institutional, and industrial facilities. Unlike direct expansion refrigeration systems that distribute refrigerant, chilled water systems use water as a secondary heat transfer medium, providing superior flexibility in zoning, capacity modulation, and central plant optimization. This analysis examines the fundamental physics, system configurations, component selection methodologies, and energy optimization strategies governing chilled water system design.

## Fundamental System Physics

### Heat Transfer Fundamentals

The cooling capacity delivered by a chilled water system derives from sensible heat transfer between the chilled water and the conditioned space air. The fundamental energy balance equation governs system sizing:

{{< formula display="true" >}}
$$\dot{Q} = \dot{m} \cdot c_p \cdot \Delta T = \rho \cdot \dot{V} \cdot c_p \cdot \Delta T$$
{{< /formula >}}

Where:
- $\dot{Q}$ = cooling capacity (kW or tons)
- $\dot{m}$ = mass flow rate (kg/s or lb/hr)
- $c_p$ = specific heat of water = 4.186 kJ/(kg·K) or 1.0 Btu/(lb·°F)
- $\Delta T$ = supply-return temperature difference (°C or °F)
- $\rho$ = water density = 1000 kg/m³ or 8.33 lb/gal
- $\dot{V}$ = volumetric flow rate (m³/s, L/s, or gpm)

For water systems using standard units:

{{< formula display="true" >}}
$$\dot{Q}_{tons} = \frac{\dot{V}_{gpm} \cdot \Delta T_F}{24}$$
{{< /formula >}}

{{< formula display="true" >}}
$$\dot{Q}_{kW} = \frac{\dot{V}_{L/s} \cdot \Delta T_C}{14.3}$$
{{< /formula >}}

### Design Delta-T Selection

The temperature difference between supply and return water fundamentally impacts system economics. Larger delta-T values reduce flow rate requirements, enabling smaller pipes, pumps, and reduced pumping energy, but may compromise heat transfer effectiveness at terminal units.

Standard design delta-T values:
- **10°F (5.6°C)**: Traditional design, conservative approach
- **12-14°F (6.7-7.8°C)**: Modern practice balancing equipment performance and pumping energy
- **16-20°F (8.9-11.1°C)**: High delta-T systems requiring careful terminal unit selection

Flow rate calculation for a given delta-T:

{{< formula display="true" >}}
$$\dot{V}_{gpm} = \frac{\dot{Q}_{tons} \cdot 24}{\Delta T_F}$$
{{< /formula >}}

Example: 500-ton cooling load with 12°F delta-T requires:

{{< formula display="true" >}}
$$\dot{V} = \frac{500 \times 24}{12} = 1000 \text{ gpm}$$
{{< /formula >}}

### Delta-T Syndrome

Delta-T degradation represents a persistent operational challenge where actual system delta-T falls below design values, causing excessive flow rates and pump energy consumption. Primary causes include:

1. **Coil bypass flow**: Improperly balanced terminal units allowing water to bypass coils
2. **Oversized pumps**: Excessive flow overcoming control valve authority
3. **Low load conditions**: Reduced heat transfer at partial load with constant flow
4. **Chiller control**: Supply temperature reset reducing delta-T
5. **Piping design**: Short-circuiting or unbalanced distribution

The energy impact scales significantly:

{{< formula display="true" >}}
$$\text{Power}_{pump} \propto \dot{V}^3$$
{{< /formula >}}

A 20% increase in flow rate from delta-T degradation (12°F design to 10°F actual) increases pump energy by:

{{< formula display="true" >}}
$$\left(\frac{1.2}{1.0}\right)^3 = 1.728 \text{ (73% increase)}$$
{{< /formula >}}

## System Configurations

### Primary-Secondary (Decoupled) Systems

Primary-secondary pumping decouples chiller flow (primary loop) from distribution flow (secondary loop) using a common pipe or decoupler. This configuration allows chillers to operate at optimal flow rates independent of building load variations.

{{< diagram >}}
graph TD
    CH1[Chiller 1] -->|Primary Pump 1| CP[Common Pipe]
    CH2[Chiller 2] -->|Primary Pump 2| CP
    CH3[Chiller 3] -->|Primary Pump 3| CP
    CP -->|Secondary Pump 1| LOAD1[Building Load 1]
    CP -->|Secondary Pump 2| LOAD2[Building Load 2]
    CP -->|Secondary Pump 3| LOAD3[Building Load 3]
    LOAD1 --> CP
    LOAD2 --> CP
    LOAD3 --> CP
{{< /diagram >}}

#### Common Pipe Sizing

The common pipe must maintain low pressure drop to prevent primary-secondary interaction. Velocity should not exceed 2-4 ft/s (0.6-1.2 m/s):

{{< formula display="true" >}}
$$v = \frac{\dot{V}}{A} = \frac{4\dot{V}}{\pi D^2}$$
{{< /formula >}}

Where:
- $v$ = velocity (ft/s)
- $\dot{V}$ = flow rate (ft³/s, converted from gpm: gpm/448.8)
- $D$ = pipe diameter (ft)

Common pipe length should be minimized (typically 10-20 pipe diameters) to reduce mixing and maintain temperature separation.

#### Flow Relationships

Three operating conditions exist:

1. **Primary flow > Secondary flow**: Excess chilled water returns through common pipe to chillers (rare)
2. **Primary flow = Secondary flow**: Ideal balanced condition
3. **Primary flow < Secondary flow**: Return water bypasses through common pipe, mixing with supply (typical at partial load)

The mixing temperature when secondary exceeds primary:

{{< formula display="true" >}}
$$T_{supply,mixed} = \frac{\dot{V}_{pri} \cdot T_{pri} + (\dot{V}_{sec} - \dot{V}_{pri}) \cdot T_{return}}{\dot{V}_{sec}}$$
{{< /formula >}}

### Variable Primary Flow (VPF)

Variable primary flow eliminates the secondary loop, using variable speed drives on primary pumps to modulate flow based on building demand. This configuration reduces pump count, initial cost, and pumping energy but requires careful chiller minimum flow protection.

{{< diagram >}}
graph TD
    VFD1[VFD Primary Pump 1] --> CH1[Chiller 1]
    VFD2[VFD Primary Pump 2] --> CH2[Chiller 2]
    VFD3[VFD Primary Pump 3] --> CH3[Chiller 3]
    CH1 --> DIST[Distribution System]
    CH2 --> DIST
    CH3 --> DIST
    DIST --> BPV[Bypass Valve]
    BPV --> CH1
    BPV --> CH2
    BPV --> CH3
{{< /diagram >}}

#### Minimum Flow Protection

Chillers require minimum flow to prevent evaporator freeze-up and ensure adequate heat transfer. Protection strategies include:

1. **Bypass valve**: Opens when system flow drops below chiller minimum
2. **Pump minimum speed**: VFD minimum frequency (typically 30-40 Hz)
3. **Chiller staging**: Shut down chillers to maintain flow through operating units

Bypass valve sizing equation:

{{< formula display="true" >}}
$$C_v = \frac{\dot{V}_{gpm}}{\sqrt{\frac{\Delta P_{psi}}{SG}}}$$
{{< /formula >}}

Where:
- $C_v$ = valve flow coefficient
- $\dot{V}_{gpm}$ = design flow rate through bypass
- $\Delta P_{psi}$ = differential pressure across valve (psi)
- $SG$ = specific gravity of fluid (1.0 for water)

### Distributed Pumping

Distributed pumping places pumps at terminal units or zones rather than centrally. This approach optimizes pressure delivery, reduces pipe sizing, and enables independent zone operation but increases equipment count and maintenance complexity.

Applications include:
- High-rise buildings with significant elevation changes
- Campus systems with distributed buildings
- Retrofit installations adapting existing infrastructure

Pump head calculation for distributed systems:

{{< formula display="true" >}}
$$H_{total} = H_{friction} + H_{elevation} + H_{equipment} + H_{control}$$
{{< /formula >}}

## Chiller Types and Performance

### Chiller Classification

Chilled water systems employ various chiller technologies, each with distinct performance characteristics:

{{< table >}}
| Chiller Type | Compressor | Capacity Range | Efficiency (kW/ton) | Part-Load Performance | Applications |
|--------------|------------|----------------|---------------------|----------------------|--------------|
| Air-Cooled Scroll | Scroll | 20-160 tons | 1.0-1.2 | Moderate | Small commercial, no cooling tower |
| Air-Cooled Screw | Screw | 150-500 tons | 0.85-1.05 | Good | Medium commercial, water scarcity |
| Water-Cooled Screw | Screw | 150-750 tons | 0.55-0.70 | Very Good | Industrial, process cooling |
| Water-Cooled Centrifugal | Centrifugal | 200-10,000+ tons | 0.45-0.60 | Excellent | Large commercial, central plants |
| Magnetic Bearing Centrifugal | Centrifugal | 150-2,000 tons | 0.40-0.55 | Excellent | High-efficiency applications |
| Absorption | Heat-driven | 100-1,500 tons | 15-20 lb steam/ton | Good | Waste heat recovery, CHP |
{{< /table >}}

### Chiller Performance Curves

Chiller efficiency varies with operating conditions, primarily affected by:
- Entering condenser water temperature (ECWT) or entering air temperature
- Leaving chilled water temperature (LCWT)
- Part-load ratio (PLR)

The integrated part-load value (IPLV) metric accounts for part-load operation:

{{< formula display="true" >}}
$$\text{IPLV} = 0.01A + 0.42B + 0.45C + 0.12D$$
{{< /formula >}}

Where A, B, C, D represent efficiency at 100%, 75%, 50%, and 25% load respectively.

Performance correction for non-standard conditions:

{{< formula display="true" >}}
$$\text{kW/ton}_{actual} = \text{kW/ton}_{rated} \times f_{ECWT} \times f_{LCWT} \times f_{PLR}$$
{{< /formula >}}

Typical centrifugal chiller part-load curve shows improving efficiency from 100% to 60-70% load:

{{< formula display="true" >}}
$$\text{kW/ton} = a + b \cdot PLR + c \cdot PLR^2 + d \cdot PLR^3$$
{{< /formula >}}

Representative coefficients for variable-speed centrifugal:
- a = 0.15
- b = 0.20
- c = 0.30
- d = 0.35

### Chiller Staging and Sequencing

Multiple chiller plants require optimization algorithms to minimize energy consumption. The fundamental approach stages chillers to maximize efficiency:

1. **Equal loading**: Distribute load evenly across operating chillers
2. **Incremental efficiency**: Stage next chiller when incremental efficiency improves
3. **Manufacturer curves**: Use actual performance data for staging decisions

Staging decision criterion:

{{< formula display="true" >}}
$$\text{Stage on when: } \frac{\text{kW}_{n+1}}{\text{Tons}_{n+1}} < \frac{\text{kW}_n}{\text{Tons}_n}$$
{{< /formula >}}

Where subscript $n$ represents current operating chillers and $n+1$ represents adding one additional chiller.

## Pump Selection and Analysis

### Pump Head Calculation

Total pump head consists of several components:

{{< formula display="true" >}}
$$H_{total} = H_{friction} + H_{static} + H_{equipment} + H_{control}$$
{{< /formula >}}

#### Friction Losses

Pipe friction follows the Darcy-Weisbach equation:

{{< formula display="true" >}}
$$\Delta P_f = f \cdot \frac{L}{D} \cdot \frac{\rho v^2}{2}$$
{{< /formula >}}

Where:
- $f$ = Darcy friction factor (dimensionless)
- $L$ = pipe length (ft or m)
- $D$ = pipe diameter (ft or m)
- $\rho$ = fluid density (lb/ft³ or kg/m³)
- $v$ = fluid velocity (ft/s or m/s)

Converting to head in feet of water:

{{< formula display="true" >}}
$$H_f = \frac{\Delta P_f}{\rho g} = f \cdot \frac{L}{D} \cdot \frac{v^2}{2g}$$
{{< /formula >}}

For turbulent flow in commercial steel pipe, the Colebrook equation determines friction factor:

{{< formula display="true" >}}
$$\frac{1}{\sqrt{f}} = -2\log_{10}\left(\frac{\epsilon/D}{3.7} + \frac{2.51}{Re\sqrt{f}}\right)$$
{{< /formula >}}

Where:
- $\epsilon$ = pipe roughness (ft), typically 0.00015 ft for steel
- $Re$ = Reynolds number = $\frac{\rho v D}{\mu}$
- $\mu$ = dynamic viscosity

Hazen-Williams equation provides simplified friction calculation:

{{< formula display="true" >}}
$$H_f = \frac{4.52 \cdot L \cdot \dot{V}^{1.852}}{C^{1.852} \cdot D^{4.87}}$$
{{< /formula >}}

Where:
- $H_f$ = friction head loss (ft per 100 ft)
- $\dot{V}$ = flow rate (gpm)
- $C$ = Hazen-Williams coefficient (120 for steel, 150 for copper)
- $D$ = inside diameter (inches)

#### Equipment Losses

Component pressure drops from manufacturer data:

{{< table >}}
| Component | Typical Pressure Drop |
|-----------|----------------------|
| Chiller evaporator | 10-20 ft |
| Air handler coil | 8-15 ft |
| Fan coil unit | 5-10 ft |
| Control valve (wide open) | 3-5 ft |
| Strainer | 2-5 ft |
| Heat exchanger | 8-15 ft |
{{< /table >}}

#### Control Valve Authority

Control valve authority ensures adequate control range:

{{< formula display="true" >}}
$$\beta = \frac{\Delta P_{valve}}{\Delta P_{valve} + \Delta P_{coil}}$$
{{< /formula >}}

Target authority: 0.25-0.50 for acceptable control. Lower authority causes poor control and delta-T degradation.

Design valve pressure drop:

{{< formula display="true" >}}
$$\Delta P_{valve} = \frac{\beta}{1-\beta} \cdot \Delta P_{coil}$$
{{< /formula >}}

For $\beta$ = 0.33 and coil drop of 10 ft:

{{< formula display="true" >}}
$$\Delta P_{valve} = \frac{0.33}{1-0.33} \cdot 10 = 4.9 \text{ ft}$$
{{< /formula >}}

### Pump Power and Efficiency

Pump power consumption derives from hydraulic principles:

{{< formula display="true" >}}
$$P_{hydraulic} = \frac{\rho g \dot{V} H}{1000}$$
{{< /formula >}}

Where:
- $P_{hydraulic}$ = hydraulic power (kW)
- $\rho$ = water density (kg/m³)
- $g$ = gravitational acceleration (9.81 m/s²)
- $\dot{V}$ = flow rate (m³/s)
- $H$ = total head (m)

In imperial units:

{{< formula display="true" >}}
$$P_{hp} = \frac{\dot{V}_{gpm} \cdot H_{ft} \cdot SG}{3960}$$
{{< /formula >}}

Actual motor power accounts for pump and motor efficiency:

{{< formula display="true" >}}
$$P_{motor} = \frac{P_{hydraulic}}{\eta_{pump} \cdot \eta_{motor}}$$
{{< /formula >}}

Typical efficiencies:
- Pump: 70-85% (larger pumps more efficient)
- Motor: 90-95% (premium efficiency motors)
- VFD: 95-97%

### Variable Speed Pumping

Variable frequency drives modulate pump speed to match system demand, following affinity laws:

{{< formula display="true" >}}
$$\frac{\dot{V}_2}{\dot{V}_1} = \frac{N_2}{N_1}$$
{{< /formula >}}

{{< formula display="true" >}}
$$\frac{H_2}{H_1} = \left(\frac{N_2}{N_1}\right)^2$$
{{< /formula >}}

{{< formula display="true" >}}
$$\frac{P_2}{P_1} = \left(\frac{N_2}{N_1}\right)^3$$
{{< /formula >}}

Where:
- $\dot{V}$ = flow rate
- $H$ = pump head
- $P$ = power
- $N$ = rotational speed
- Subscripts 1 and 2 represent initial and final conditions

Energy savings from variable speed operation scale dramatically with the cubic relationship. Reducing speed to 75% (75% flow) reduces power to:

{{< formula display="true" >}}
$$P_2 = P_1 \times 0.75^3 = 0.42 P_1 \text{ (58% energy reduction)}$$
{{< /formula >}}

This relationship drives the economic justification for VFD implementation on chilled water pumps.

## Differential Pressure Control

### Control Strategies

Differential pressure (DP) sensors provide feedback for VFD pump speed control. Sensor location and setpoint strategy critically impact energy performance:

#### 1. Fixed DP Setpoint at End of System

Traditional approach maintaining constant differential pressure at the critical (most remote) circuit:

{{< formula display="true" >}}
$$\Delta P_{setpoint} = \Delta P_{coil} + \Delta P_{valve} + \Delta P_{piping,critical}$$
{{< /formula >}}

Advantages:
- Guaranteed pressure at all loads
- Simple control logic

Disadvantages:
- Excessive pressure at partial load when remote loads are inactive
- Higher pumping energy

#### 2. Reset DP Setpoint

Reduces differential pressure setpoint when control valves approach full open:

{{< formula display="true" >}}
$$\Delta P_{reset} = \Delta P_{max} - \left(\Delta P_{max} - \Delta P_{min}\right) \times \frac{N_{open}}{N_{total}}$$
{{< /formula >}}

Where:
- $N_{open}$ = number of valves >90% open
- $N_{total}$ = total number of control valves

Typically implemented as:
- Reduce DP setpoint when all valves <90% open
- Increase DP setpoint when any valve >95% open
- Rate limit changes to prevent instability

Energy savings: 20-40% pump energy reduction compared to fixed DP.

#### 3. Flow-Based Control

Directly controls pump to deliver required system flow based on load:

{{< formula display="true" >}}
$$\dot{V}_{system} = \sum_{i=1}^{n} \dot{V}_{terminal,i}$$
{{< /formula >}}

Requires flow meters on terminal circuits or calculated flow from control valve positions.

### Sensor Placement

DP sensor location significantly affects control stability and energy performance:

1. **At pump discharge**: Measures only pump-generated pressure, simple but provides no load feedback
2. **Two-thirds into distribution**: Balances coverage of building zones
3. **Critical circuit**: Ensures most remote load receives adequate pressure
4. **Multiple sensors**: Use highest signal from multiple locations

## Bypass Valves and Decoupling

### Bypass Valve Functionality

Bypass valves (also called differential pressure bypass valves) protect chillers from low flow conditions in variable flow systems. The valve opens when system pressure exceeds setpoint, diverting flow from supply to return.

Bypass valve sizing methodology:

1. Determine maximum bypass flow requirement:

{{< formula display="true" >}}
$$\dot{V}_{bypass,max} = \dot{V}_{chiller,min} - \dot{V}_{system,min}$$
{{< /formula >}}

2. Calculate available differential pressure:

{{< formula display="true" >}}
$$\Delta P_{available} = \Delta P_{pump,max} - \Delta P_{chiller}$$
{{< /formula >}}

3. Size valve coefficient:

{{< formula display="true" >}}
$$C_v = \frac{\dot{V}_{bypass,max}}{\sqrt{\Delta P_{available}}}$$
{{< /formula >}}

Example: 1000 gpm chiller with 400 gpm minimum, 200 gpm minimum system flow, 60 psi pump pressure, 15 psi chiller drop:

{{< formula display="true" >}}
$$\dot{V}_{bypass} = 400 - 200 = 200 \text{ gpm}$$
{{< /formula >}}

{{< formula display="true" >}}
$$\Delta P = 60 - 15 = 45 \text{ psi}$$
{{< /formula >}}

{{< formula display="true" >}}
$$C_v = \frac{200}{\sqrt{45}} = 29.8$$
{{< /formula >}}

Select next larger standard valve size.

### Decoupler Design

In primary-secondary systems, the decoupler (common pipe) hydraulically separates primary and secondary loops. Proper design requires:

1. **Low pressure drop**: <0.5 ft to prevent interaction
2. **Short length**: 10-20 diameters to minimize mixing
3. **Bridge connections**: Close spacing between supply and return connections

Decoupler pressure drop verification:

{{< formula display="true" >}}
$$\Delta P_{decoupler} = f \cdot \frac{L}{D} \cdot \frac{v^2}{2g} < 0.5 \text{ ft}$$
{{< /formula >}}

Temperature mixing when secondary exceeds primary flow:

{{< formula display="true" >}}
$$T_{mixed} = \frac{\dot{V}_{pri} \cdot T_{LCHWT} + \dot{V}_{bypass} \cdot T_{RCHWT}}{\dot{V}_{sec}}$$
{{< /formula >}}

Where:
- $\dot{V}_{bypass} = \dot{V}_{sec} - \dot{V}_{pri}$
- $T_{LCHWT}$ = leaving chilled water temperature from chillers
- $T_{RCHWT}$ = return chilled water temperature from building

## Waterside Economizer Integration

### Free Cooling Principles

Waterside economizers utilize low ambient conditions to provide cooling without chiller operation. When outdoor wet-bulb temperature drops sufficiently below required supply water temperature, a heat exchanger or direct cooling tower connection provides "free cooling."

Available free cooling capacity:

{{< formula display="true" >}}
$$\dot{Q}_{free} = \dot{m} \cdot c_p \cdot (T_{RCHWT} - T_{LCHWT,target})$$
{{< /formula >}}

Subject to constraint:

{{< formula display="true" >}}
$$T_{LCHWT,target} \geq T_{WB,ambient} + \Delta T_{approach} + \Delta T_{HX}$$
{{< /formula >}}

Where:
- $T_{WB,ambient}$ = ambient wet-bulb temperature
- $\Delta T_{approach}$ = cooling tower approach (typically 5-7°F)
- $\Delta T_{HX}$ = heat exchanger temperature difference (if used, 2-5°F)

### Configuration Types

#### 1. Plate-Frame Heat Exchanger

Indirect connection between condenser water and chilled water loops through heat exchanger:

{{< diagram >}}
graph LR
    CT[Cooling Tower] --> CWP[Condenser Water Pump]
    CWP --> HX[Plate-Frame HX]
    HX --> CT
    CHW[Chilled Water Return] --> HX
    HX --> CHWSUP[Chilled Water Supply]
{{< /diagram >}}

Heat exchanger effectiveness:

{{< formula display="true" >}}
$$\varepsilon = \frac{T_{CWS,in} - T_{CWS,out}}{T_{CWS,in} - T_{CHW,in}}$$
{{< /formula >}}

Typical effectiveness: 0.60-0.85 for counterflow plate-frame exchangers.

Required heat exchanger capacity:

{{< formula display="true" >}}
$$UA = \frac{\dot{Q}}{\Delta T_{LMTD}}$$
{{< /formula >}}

Where log-mean temperature difference:

{{< formula display="true" >}}
$$\Delta T_{LMTD} = \frac{(T_{CWS,in} - T_{CHW,out}) - (T_{CWS,out} - T_{CHW,in})}{\ln\left(\frac{T_{CWS,in} - T_{CHW,out}}{T_{CWS,out} - T_{CHW,in}}\right)}$$
{{< /formula >}}

#### 2. Integrated Waterside Economizer

Direct connection using cooling tower to chill building supply water through integrated chiller-economizer:

Advantages:
- No separate heat exchanger
- Lower first cost
- Reduced maintenance

Disadvantages:
- Water treatment criticality (tower water in building loop)
- Limited to integrated chiller designs

### Control Sequences

Economizer operation modes:

1. **100% free cooling**: Chillers off, economizer provides full load
2. **Partial free cooling**: Economizer pre-cools, chillers supplement
3. **Chiller-only**: Ambient too warm for economizer benefit

Mode selection logic:

{{< formula display="true" >}}
$$\text{If } T_{WB} + \Delta T_{approach} + \Delta T_{HX} < T_{CHWST,target} - 2°F \text{: Enable economizer}$$
{{< /formula >}}

Energy savings calculation:

{{< formula display="true" >}}
$$\text{Annual Savings} = \sum_{h=1}^{8760} \left(\text{kW}_{chiller,h} - \text{kW}_{economizer,h}\right) \times \text{hours}$$
{{< /formula >}}

Where economizer energy includes:
- Condenser water pump
- Cooling tower fan
- Heat exchanger pump (if applicable)

Typical economizer energy: 0.05-0.15 kW/ton versus 0.50-0.70 kW/ton for chiller operation.

## Thermal Storage Systems

### Storage Fundamentals

Thermal energy storage (TES) shifts cooling production to off-peak periods, reducing demand charges and capitalizing on lower nighttime efficiency. The fundamental storage equation:

{{< formula display="true" >}}
$$E_{stored} = m \cdot c_p \cdot \Delta T = \rho \cdot V \cdot c_p \cdot \Delta T$$
{{< /formula >}}

Where:
- $E_{stored}$ = stored energy (kWh or ton-hours)
- $m$ = mass of storage medium (kg or lb)
- $V$ = volume (m³ or gal)
- $\Delta T$ = temperature difference between charged and discharged states

Converting to ton-hours:

{{< formula display="true" >}}
$$\text{Ton-hours} = \frac{V_{gal} \times 8.33 \times \Delta T_F}{12,000}$$
{{< /formula >}}

### Storage Technologies

{{< table >}}
| Technology | Storage Medium | Temperature | Energy Density | Efficiency | Applications |
|------------|----------------|-------------|----------------|------------|--------------|
| Chilled Water | Water | 42-50°F | 5-8 Btu/gal-°F | 90-95% | Large systems, retrofit |
| Ice (full storage) | Ice | 14-25°F | 144 Btu/lb | 85-90% | Limited space, high density |
| Ice (partial storage) | Ice/water | 25-40°F | 100-120 Btu/lb | 87-92% | Demand reduction, retrofit |
| Phase Change Material | Eutectic salts | 47°F | 60-80 Btu/lb | 88-93% | Moderate density, stable temp |
{{< /table >}}

### Storage Strategies

#### Full Storage

Chillers operate only during off-peak periods, storage meets entire on-peak load:

{{< formula display="true" >}}
$$V_{storage} = \frac{\dot{Q}_{peak} \times t_{discharge}}{\rho \cdot c_p \cdot \Delta T}$$
{{< /formula >}}

Where:
- $\dot{Q}_{peak}$ = peak cooling load
- $t_{discharge}$ = on-peak duration (hours)

Example: 500-ton peak load, 12-hour on-peak period, 16°F delta-T:

{{< formula display="true" >}}
$$V = \frac{500 \times 12 \times 12,000}{8.33 \times 16} = 539,568 \text{ gallons}$$
{{< /formula >}}

#### Partial Storage (Load Leveling)

Chillers operate continuously, storage supplements during peak periods:

{{< formula display="true" >}}
$$\dot{Q}_{chiller} = \frac{\int_0^{24} \dot{Q}_{load}(t) dt}{24}$$
{{< /formula >}}

Storage size based on area between load profile and chiller capacity:

{{< formula display="true" >}}
$$E_{storage} = \int_{t_1}^{t_2} \left(\dot{Q}_{load}(t) - \dot{Q}_{chiller}\right) dt$$
{{< /formula >}}

Partial storage reduces chiller size and storage volume compared to full storage while still providing demand reduction.

#### Demand Limiting

Storage discharges only during utility demand peaks to minimize demand charges:

{{< formula display="true" >}}
$$\text{Savings}_{\text{demand}} = (\dot{Q}_{reduced} - \dot{Q}_{with storage}) \times \text{Rate}_{\text{\$/kW}} \times 12 \text{ months}$$
{{< /formula >}}

### Storage System Hydraulics

Thermal storage requires careful piping design to maintain thermal stratification and prevent mixing.

Series configuration (charge-discharge flow path through storage):

{{< diagram >}}
graph LR
    CH[Chiller] --> STG[Storage Tank]
    STG --> LOAD[Building Load]
    LOAD --> CH
{{< /diagram >}}

Parallel configuration (storage in separate loop):

{{< diagram >}}
graph TD
    CH[Chiller] --> DIV{Diverting Valve}
    DIV --> LOAD[Building Load]
    DIV --> STG[Storage Tank]
    STG --> MIX{Mixing Valve}
    LOAD --> MIX
    MIX --> CH
{{< /diagram >}}

Diffuser design for stratification:

{{< formula display="true" >}}
$$Fr = \frac{v_{inlet}}{\sqrt{g \cdot H \cdot \frac{\Delta \rho}{\rho}}} < 1$$
{{< /formula >}}

Where:
- $Fr$ = Froude number (dimensionless)
- $v_{inlet}$ = inlet velocity (m/s)
- $g$ = gravitational acceleration (9.81 m/s²)
- $H$ = tank height (m)
- $\Delta \rho / \rho$ = relative density difference

Froude number <1 indicates stable stratification.

## System Diversity and Load Profiles

### Diversity Factors

Chilled water systems serving multiple zones rarely experience simultaneous peak loads. Diversity factors account for this non-coincident loading:

{{< formula display="true" >}}
$$\text{Diversity Factor} = \frac{\sum \dot{Q}_{zone,peak}}{\dot{Q}_{system,peak}}$$
{{< /formula >}}

Typical diversity factors:

{{< table >}}
| Building Type | Diversity Factor | Description |
|--------------|------------------|-------------|
| Single zone | 1.00 | No diversity |
| Multiple floors, similar use | 0.85-0.95 | Time-based diversity |
| Mixed-use building | 0.70-0.85 | Usage pattern diversity |
| Campus system | 0.60-0.80 | Building diversity |
| District cooling | 0.50-0.70 | Large-scale diversity |
{{< /table >}}

Applying diversity:

{{< formula display="true" >}}
$$\dot{Q}_{plant} = \frac{\sum \dot{Q}_{zone,peak}}{\text{DF}} \times \text{SF}$$
{{< /formula >}}

Where:
- $\text{DF}$ = diversity factor
- $\text{SF}$ = safety factor (1.10-1.20)

### Load Duration Curves

Load duration curves plot cooling load against hours of occurrence, enabling energy analysis and equipment sizing optimization:

{{< formula display="true" >}}
$$\text{Annual Energy} = \sum_{i=1}^{n} \dot{Q}_i \times \Delta t_i$$
{{< /formula >}}

Key metrics from load duration analysis:
- **Peak load**: Maximum instantaneous demand
- **Equivalent full-load hours**: Total annual energy divided by peak load
- **Part-load distribution**: Percentage of hours at various load levels

Equivalent full-load hours:

{{< formula display="true" >}}
$$\text{EFLH} = \frac{\sum_{h=1}^{8760} \dot{Q}_h}{\dot{Q}_{peak}}$$
{{< /formula >}}

Typical commercial buildings: 1,500-3,000 EFLH/year.

### Bin Analysis

Bin analysis correlates building load with outdoor temperature for energy modeling:

{{< formula display="true" >}}
$$E_{annual} = \sum_{i=1}^{n_{bins}} \dot{Q}(T_{bin,i}) \times h_{bin,i} \times \frac{\text{kW}}{\text{ton}}(T_{bin,i})$$
{{< /formula >}}

Where:
- $T_{bin,i}$ = representative temperature for bin $i$
- $h_{bin,i}$ = hours in bin $i$
- $\dot{Q}(T)$ = building load at temperature $T$
- $\text{kW/ton}(T)$ = chiller efficiency at temperature $T$

## Condenser Water Systems

### Cooling Tower Fundamentals

Cooling towers reject heat from chiller condensers through evaporative cooling. The governing heat and mass transfer relationship:

{{< formula display="true" >}}
$$\dot{Q}_{tower} = \dot{m}_w \cdot c_p \cdot (T_{CWR} - T_{CWS}) = \dot{m}_a \cdot (h_{out} - h_{in})$$
{{< /formula >}}

Where:
- $\dot{m}_w$ = water mass flow rate
- $T_{CWR}$ = condenser water return temperature
- $T_{CWS}$ = condenser water supply temperature
- $\dot{m}_a$ = air mass flow rate
- $h$ = air enthalpy

Tower performance characterized by approach and range:

{{< formula display="true" >}}
$$\text{Approach} = T_{CWS} - T_{WB}$$
{{< /formula >}}

{{< formula display="true" >}}
$$\text{Range} = T_{CWR} - T_{CWS}$$
{{< /formula >}}

Where $T_{WB}$ = ambient wet-bulb temperature.

Typical design values:
- Approach: 5-7°F (tighter approach requires larger tower)
- Range: 10-15°F (matches chiller condenser delta-T)

Tower effectiveness:

{{< formula display="true" >}}
$$\varepsilon = \frac{\text{Range}}{\text{Range} + \text{Approach}} = \frac{T_{CWR} - T_{CWS}}{T_{CWR} - T_{WB}}$$
{{< /formula >}}

### Tower Selection and Sizing

Tower thermal capacity rated in terms of heat rejection:

{{< formula display="true" >}}
$$\dot{Q}_{tower} = \dot{Q}_{cooling} \times \left(1 + \frac{1}{\text{COP}}\right)$$
{{< /formula >}}

For 500-ton chiller at 0.60 kW/ton (COP = 5.86):

{{< formula display="true" >}}
$$\dot{Q}_{tower} = 500 \times \left(1 + \frac{1}{5.86}\right) = 585 \text{ tons}$$
{{< /formula >}}

Tower performance varies with operating conditions according to manufacturer curves, typically expressed as:

{{< formula display="true" >}}
$$\frac{\dot{Q}_{actual}}{\dot{Q}_{rated}} = f\left(\frac{\dot{V}_w}{\dot{V}_{w,rated}}, \frac{\dot{V}_a}{\dot{V}_{a,rated}}, T_{WB}, T_{CWR}\right)$$
{{< /formula >}}

### Variable Speed Tower Fans

Tower fan power follows cubic relationship with speed (affinity laws):

{{< formula display="true" >}}
$$P_{fan} = P_{rated} \times \left(\frac{N}{N_{rated}}\right)^3$$
{{< /formula >}}

Fan speed modulates to maintain condenser water supply temperature setpoint. As ambient conditions cool, fan speed reduces, providing substantial energy savings.

Annual tower fan energy:

{{< formula display="true" >}}
$$E_{fan} = \sum_{h=1}^{8760} P_{fan,h} \times 1 \text{ hour}$$
{{< /formula >}}

Where $P_{fan,h}$ varies with load and ambient conditions each hour.

### Condenser Water Temperature Optimization

Lower condenser water temperature improves chiller efficiency but increases tower fan energy. The optimal setpoint balances these competing effects:

{{< formula display="true" >}}
$$P_{total} = P_{chiller}(T_{CWS}) + P_{tower}(T_{CWS})$$
{{< /formula >}}

Minimize total power:

{{< formula display="true" >}}
$$\frac{dP_{total}}{dT_{CWS}} = 0$$
{{< /formula >}}

Typical optimal range: 65-75°F depending on load and ambient conditions.

Chiller power sensitivity to condenser water temperature:

{{< formula display="true" >}}
$$\frac{d(\text{kW/ton})}{dT_{CWS}} \approx 0.01 \text{ to } 0.02 \text{ kW/ton per °F}$$
{{< /formula >}}

For 500-ton chiller at 0.60 kW/ton base:

{{< formula display="true" >}}
$$\Delta P = 500 \times 0.015 \times \Delta T_{CWS} \text{ kW}$$
{{< /formula >}}

A 5°F reduction saves approximately 37.5 kW of chiller power.

### Evaporative Loss and Makeup Water

Cooling towers lose water through evaporation, drift, and blowdown:

Evaporation rate:

{{< formula display="true" >}}
$$\dot{V}_{evap} = \frac{\dot{Q}_{tower}}{h_{fg} \times \rho_w}$$
{{< /formula >}}

Simplified:

{{< formula display="true" >}}
$$\dot{V}_{evap,gpm} \approx 0.001 \times \dot{V}_{CW,gpm} \times \Delta T_F$$
{{< /formula >}}

Where $\dot{V}_{CW}$ = condenser water flow rate.

Blowdown maintains water quality by limiting concentration:

{{< formula display="true" >}}
$$\dot{V}_{blowdown} = \frac{\dot{V}_{evap}}{\text{COC} - 1}$$
{{< /formula >}}

Where $\text{COC}$ = cycles of concentration (typically 3-6).

Total makeup water:

{{< formula display="true" >}}
$$\dot{V}_{makeup} = \dot{V}_{evap} + \dot{V}_{blowdown} + \dot{V}_{drift}$$
{{< /formula >}}

Drift typically 0.001-0.01% of circulation rate for modern drift eliminators.

## Water Treatment and Corrosion Control

### Water Quality Requirements

Chilled water and condenser water systems require chemical treatment to prevent:
1. Corrosion of metallic components
2. Scale formation from mineral precipitation
3. Biological growth (algae, bacteria, fungi)
4. Fouling from suspended solids

Critical water quality parameters:

{{< table >}}
| Parameter | Chilled Water | Condenser Water | Impact |
|-----------|---------------|-----------------|--------|
| pH | 7.5-9.0 | 6.5-8.5 | Corrosion, scale |
| Hardness (ppm CaCO₃) | <50 | <400 | Scale formation |
| Alkalinity (ppm CaCO₃) | 50-200 | 50-400 | pH buffering, scale |
| Chlorides (ppm) | <100 | <500 | Corrosion |
| Sulfates (ppm) | <100 | <500 | Corrosion, scale |
| Total Dissolved Solids | <500 | <1500 | Scale, corrosion |
| Biological count (CFU/mL) | <1000 | <10,000 | Biofouling |
{{< /table >}}

### Corrosion Mechanisms

Electrochemical corrosion occurs when dissimilar metals contact in an electrolyte (water):

{{< formula display="true" >}}
$$\text{Anode: } M \rightarrow M^{n+} + ne^-$$
{{< /formula >}}

{{< formula display="true" >}}
$$\text{Cathode: } O_2 + 2H_2O + 4e^- \rightarrow 4OH^-$$
{{< /formula >}}

Corrosion rate follows Faraday's law:

{{< formula display="true" >}}
$$\text{Corrosion Rate} = \frac{I \cdot M}{n \cdot F \cdot A \cdot \rho}$$
{{< /formula >}}

Where:
- $I$ = corrosion current (A)
- $M$ = molecular weight (g/mol)
- $n$ = electrons transferred
- $F$ = Faraday constant (96,485 C/mol)
- $A$ = surface area (cm²)
- $\rho$ = density (g/cm³)

Typical corrosion rates expressed as mils per year (mpy):
- Excellent: <2 mpy
- Acceptable: 2-5 mpy
- Poor: >5 mpy

### Scale Formation

Scale forms when mineral solubility limits are exceeded. Calcium carbonate represents the most common scale:

{{< formula display="true" >}}
$$Ca^{2+} + 2HCO_3^- \rightarrow CaCO_3 \downarrow + H_2O + CO_2$$
{{< /formula >}}

Langelier Saturation Index (LSI) predicts scaling tendency:

{{< formula display="true" >}}
$$\text{LSI} = \text{pH}_{actual} - \text{pH}_s$$
{{< /formula >}}

Where $\text{pH}_s$ = pH at calcium carbonate saturation.

Interpretation:
- LSI > 0: Supersaturated, scale-forming
- LSI = 0: Saturated, neutral
- LSI < 0: Undersaturated, corrosive

Target range: -0.5 to +0.5 for balanced condition.

Ryznar Stability Index provides alternate assessment:

{{< formula display="true" >}}
$$\text{RSI} = 2\text{pH}_s - \text{pH}_{actual}$$
{{< /formula >}}

Target RSI: 6.5-7.0 for stable conditions.

### Treatment Strategies

#### Closed Loop Systems (Chilled Water)

Closed systems require one-time treatment with long-term inhibitors:

1. **Corrosion inhibitors**: Sodium nitrite, sodium molybdate (200-1000 ppm)
2. **pH control**: Sodium hydroxide or potassium hydroxide (pH 8.5-9.5)
3. **Biocides**: Initial slug dose, periodic maintenance

Treatment concentration:

{{< formula display="true" >}}
$$\text{Dose}_{lbs} = \frac{V_{gal} \times \text{ppm}_{target}}{120,000}$$
{{< /formula >}}

Inhibitor depletion rate typically 10-20% per year requires monitoring and makeup.

#### Open Loop Systems (Condenser Water)

Open systems continuously lose water through evaporation, requiring ongoing treatment:

1. **Scale inhibitors**: Phosphonates, polymers (5-20 ppm)
2. **Corrosion inhibitors**: Azoles, phosphates (2-10 ppm)
3. **Biocides**: Oxidizing (chlorine, bromine) and non-oxidizing
4. **pH control**: Acid feed for alkalinity management

Blowdown control maintains concentration:

{{< formula display="true" >}}
$$\text{COC} = \frac{\text{[Conductivity]}_{CW}}{\text{[Conductivity]}_{makeup}}$$
{{< /formula >}}

Chemical feed rate:

{{< formula display="true" >}}
$$\dot{V}_{chemical} = \frac{\dot{V}_{makeup} \times \text{ppm}_{target}}{10^6 \times \rho_{chemical}}$$
{{< /formula >}}

### Filtration

Side-stream filtration removes suspended solids:

Filter flow rate typically 1-10% of system flow:

{{< formula display="true" >}}
$$\dot{V}_{filter} = 0.01 \text{ to } 0.10 \times \dot{V}_{system}$$
{{< /formula >}}

Particle removal efficiency:

{{< table >}}
| Filter Type | Particle Size | Efficiency | Pressure Drop |
|-------------|---------------|------------|---------------|
| Strainer | >500 μm | 80-90% | 2-5 psi |
| Sand filter | 20-100 μm | 90-95% | 5-10 psi |
| Cartridge filter | 5-50 μm | 95-99% | 5-15 psi |
| Bag filter | 1-25 μm | 90-98% | 3-8 psi |
{{< /table >}}

## Energy Optimization Strategies

### System-Level Optimization

Chilled water system energy consumption includes:

{{< formula display="true" >}}
$$E_{total} = E_{chiller} + E_{CHW\_pump} + E_{CW\_pump} + E_{tower} + E_{aux}$$
{{< /formula >}}

Optimization targets each component while maintaining comfort and reliability.

#### Chilled Water Temperature Reset

Raising chilled water supply temperature during low-load periods reduces chiller lift and improves efficiency:

{{< formula display="true" >}}
$$\text{COP}_{Carnot} = \frac{T_{evap}}{T_{cond} - T_{evap}}$$
{{< /formula >}}

Practical chiller efficiency improves approximately:

{{< formula display="true" >}}
$$\Delta(\text{kW/ton}) \approx -0.01 \text{ to } -0.015 \text{ per °F increase in CHWST}$$
{{< /formula >}}

Reset schedule based on outdoor air temperature or load:

{{< formula display="true" >}}
$$T_{CHWST} = T_{min} + (T_{max} - T_{min}) \times \left(1 - \frac{\dot{Q}_{current}}{\dot{Q}_{design}}\right)$$
{{< /formula >}}

Typical range: 42°F at design load to 50-55°F at minimum load.

Constraints:
- Maintain adequate dehumidification (dewpoint control)
- Ensure terminal unit capacity at elevated temperature
- Monitor valve positions (reset limit when valves saturate)

#### Condenser Water Temperature Optimization

Discussed previously, balances chiller efficiency gains against tower fan energy:

{{< formula display="true" >}}
$$T_{CWS,optimal} = f(\dot{Q}_{load}, T_{WB}, \text{Chiller curves}, \text{Tower curves})$$
{{< /formula >}}

Requires real-time optimization or pre-computed lookup tables.

#### Pump Speed Optimization

Variable speed pumps reduce energy consumption following cubic relationship:

Annual pump energy savings from variable speed:

{{< formula display="true" >}}
$$\text{Savings} = \sum_{h=1}^{8760} P_{constant,h} - P_{variable,h}$$
{{< /formula >}}

Typical savings: 30-60% versus constant speed operation.

Control optimization:
1. Differential pressure reset (described previously)
2. Flow-based control matching demand
3. Predictive control based on load forecasts

#### Chiller Plant Optimization

Multi-chiller plants require sequencing and load distribution optimization:

Objective function minimizes total plant power:

{{< formula display="true" >}}
$$\min P_{total} = \sum_{i=1}^{n} P_{chiller,i}(\dot{Q}_i) + P_{pumps}(\dot{V}) + P_{towers}(T_{CWS})$$
{{< /formula >}}

Subject to constraints:
- $\sum_{i=1}^{n} \dot{Q}_i = \dot{Q}_{load}$ (meet load requirement)
- $\dot{Q}_{min,i} \leq \dot{Q}_i \leq \dot{Q}_{max,i}$ (chiller capacity limits)
- $\dot{V}_{min,i} \leq \dot{V}_i$ (minimum chiller flow)

Solution methods:
1. **Lagrange multipliers**: Analytical solution for differentiable curves
2. **Dynamic programming**: Discrete optimization
3. **Real-time optimization**: Use building automation system and chiller plant meter data

Equal marginal efficiency criterion:

{{< formula display="true" >}}
$$\frac{dP_1}{d\dot{Q}_1} = \frac{dP_2}{d\dot{Q}_2} = \cdots = \frac{dP_n}{d\dot{Q}_n}$$
{{< /formula >}}

### Heat Recovery

Chiller condenser heat recovery captures rejected heat for simultaneous heating loads:

Available heat:

{{< formula display="true" >}}
$$\dot{Q}_{cond} = \dot{Q}_{evap} + P_{compressor}$$
{{< /formula >}}

Condenser heat available at 85-105°F suitable for:
- Domestic hot water preheating
- Space heating during swing seasons
- Pool heating
- Process heating

Heat recovery effectiveness:

{{< formula display="true" >}}
$$\varepsilon_{HR} = \frac{\dot{Q}_{recovered}}{\dot{Q}_{cond,available}}$$
{{< /formula >}}

Economic analysis:

{{< formula display="true" >}}
$$\text{Savings}_{annual} = \frac{\dot{Q}_{recovered} \times \text{hours}}{\eta_{boiler}} \times \text{Cost}_{fuel}$$
{{< /formula >}}

Where $\eta_{boiler}$ represents efficiency of displaced heating system.

### Thermal Zoning and Diversity

Optimize chilled water distribution by thermal zones:

1. **Core zones**: Constant cooling loads year-round
2. **Perimeter zones**: Variable loads based on solar and envelope
3. **Process loads**: Independent of weather
4. **Ventilation loads**: Dependent on outdoor air conditions

Separate distribution enables:
- Temperature optimization by zone characteristics
- Reduced mixing losses
- Improved control and delta-T

Load aggregation diversity:

{{< formula display="true" >}}
$$\dot{Q}_{plant} = \sqrt{\left(\sum \dot{Q}_{sensible}\right)^2 + \left(\sum \dot{Q}_{latent}\right)^2}$$
{{< /formula >}}

This vector sum acknowledges non-coincident peak conditions.

## Practical Design Example

### System Design Specification

**Building**: 200,000 ft² office building, 10 stories
**Location**: Chicago, IL
**Cooling load**: 800 tons peak (4.0 tons/1000 ft²)
**Hours of operation**: 6 AM - 8 PM weekdays, 8 AM - 4 PM Saturday
**Design delta-T**: 14°F (42°F supply, 56°F return)

### Load Profile Analysis

Monthly peak loads:

{{< table >}}
| Month | Peak Load (tons) | Load Factor | Equivalent Full-Load Hours |
|-------|------------------|-------------|---------------------------|
| January | 240 | 0.30 | 80 |
| February | 280 | 0.35 | 100 |
| March | 400 | 0.50 | 150 |
| April | 520 | 0.65 | 200 |
| May | 640 | 0.80 | 240 |
| June | 760 | 0.95 | 280 |
| July | 800 | 1.00 | 310 |
| August | 800 | 1.00 | 300 |
| September | 680 | 0.85 | 260 |
| October | 480 | 0.60 | 180 |
| November | 320 | 0.40 | 120 |
| December | 240 | 0.30 | 80 |
| **Annual** | **800** | **0.65** | **2,300** |
{{< /table >}}

### Chiller Selection

Select three chillers for capacity, efficiency, and redundancy:

**Configuration**: Three 350-ton water-cooled centrifugal chillers with variable speed drives

Capacity analysis:
- Total installed: 1,050 tons (131% of peak)
- N+1 redundancy: 700 tons (87.5% of peak with one chiller down)
- Optimal loading: 267 tons per chiller at peak (76% of chiller capacity)

Performance specifications:

{{< table >}}
| Load Point | Efficiency (kW/ton) | Total Plant (kW) |
|------------|---------------------|------------------|
| 100% (800 tons) | 0.52 | 416 |
| 75% (600 tons) | 0.48 | 288 |
| 50% (400 tons) | 0.46 | 184 |
| 25% (200 tons) | 0.50 | 100 |
{{< /table >}}

IPLV calculation:

{{< formula display="true" >}}
$$\text{IPLV} = 0.01(0.52) + 0.42(0.48) + 0.45(0.46) + 0.12(0.50) = 0.474 \text{ kW/ton}$$
{{< /formula >}}

### Chilled Water Pumping

**Configuration**: Variable primary flow with three dedicated chiller pumps

Flow rate per chiller:

{{< formula display="true" >}}
$$\dot{V} = \frac{350 \times 24}{14} = 600 \text{ gpm}$$
{{< /formula >}}

Head calculation:
- Pipe friction: 35 ft
- Chiller evaporator: 15 ft
- Coil pressure drop: 12 ft average
- Control valve: 5 ft
- Fittings and accessories: 8 ft
- **Total**: 75 ft

Pump power at design:

{{< formula display="true" >}}
$$P_{hp} = \frac{600 \times 75}{3960 \times 0.78 \times 0.94} = 15.6 \text{ hp}$$
{{< /formula >}}

Select 20 hp motor with VFD.

Annual pumping energy (simplified):

{{< formula display="true" >}}
$$E_{pump} = 3 \times 15.6 \times 0.746 \times 2,300 \times 0.65^3 = 22,150 \text{ kWh}$$
{{< /formula >}}

Where $0.65^3$ represents average speed cubed based on load factor.

### Condenser Water System

**Cooling tower selection**: Three 410-ton induced-draft counterflow towers with VFD fans

Heat rejection per tower:

{{< formula display="true" >}}
$$\dot{Q}_{tower} = 350 \times 1.17 = 410 \text{ tons}$$
{{< /formula >}}

(117% of chiller capacity based on 0.52 kW/ton)

Design conditions:
- Entering water: 95°F
- Leaving water: 85°F
- Range: 10°F
- Wet-bulb: 78°F
- Approach: 7°F

Condenser water flow:

{{< formula display="true" >}}
$$\dot{V}_{CW} = \frac{410 \times 24}{10} = 984 \text{ gpm} \approx 1000 \text{ gpm per tower}$$
{{< /formula >}}

Condenser water pump head:
- Pipe friction: 25 ft
- Chiller condenser: 20 ft
- Tower: 15 ft
- Control valve: 5 ft
- Fittings: 10 ft
- **Total**: 75 ft

Pump power per unit:

{{< formula display="true" >}}
$$P_{hp} = \frac{1000 \times 75}{3960 \times 0.78 \times 0.94} = 26.0 \text{ hp}$$
{{< /formula >}}

Select 30 hp motor with VFD.

Tower fan power: 15 hp per tower

Annual condenser water system energy:

{{< formula display="true" >}}
$$E_{CW} = 3 \times (26.0 + 15.0) \times 0.746 \times 2,300 \times 0.65^2 = 70,800 \text{ kWh}$$
{{< /formula >}}

### Total System Energy

Annual energy summary:

{{< table >}}
| Component | Annual Energy (kWh) | Percentage |
|-----------|---------------------|------------|
| Chillers | 872,000 | 87.0% |
| CHW pumps | 22,150 | 2.2% |
| CW pumps | 56,400 | 5.6% |
| Tower fans | 51,800 | 5.2% |
| **Total** | **1,002,350** | **100%** |
{{< /table >}}

System efficiency:

{{< formula display="true" >}}
$$\text{kW/ton}_{system} = \frac{1,002,350}{800 \times 2,300} = 0.544 \text{ kW/ton}$$
{{< /formula >}}

This represents excellent performance for a water-cooled centrifugal plant with optimized auxiliary equipment.

### Economic Analysis

Capital cost estimate:
- Chillers (3 × $180,000): $540,000
- Cooling towers (3 × $45,000): $135,000
- CHW pumps (3 × $15,000): $45,000
- CW pumps (3 × $18,000): $54,000
- Piping and valves: $250,000
- Controls and instrumentation: $80,000
- Installation labor: $200,000
- **Total**: $1,304,000

Operating cost ($0.10/kWh):

{{< formula display="true" >}}
$$\text{Cost}_{annual} = 1,002,350 \times 0.10 = \$100,235$$
{{< /formula >}}

Comparison to air-cooled system:
- Air-cooled efficiency: 1.05 kW/ton
- Air-cooled annual energy: 1,932,000 kWh
- Annual savings: 929,650 kWh × $0.10 = $92,965
- Simple payback: $304,000 incremental cost / $92,965 = 3.3 years

## Conclusion

Chilled water system design requires integrated analysis of thermodynamic performance, fluid mechanics, heat transfer, and energy economics. Optimal configurations balance first cost, energy efficiency, reliability, and operational flexibility. Key design principles include:

1. **Delta-T preservation**: Maintain design temperature difference through proper coil selection, balancing, and control valve authority
2. **Variable flow implementation**: Utilize VFDs on pumps and tower fans to capture substantial energy savings at part-load conditions
3. **Chiller plant optimization**: Select equipment sizes and implement controls to optimize total plant efficiency across the load spectrum
4. **Water quality management**: Implement comprehensive treatment programs to prevent corrosion, scaling, and biological growth
5. **System diversity utilization**: Account for non-coincident loads to rightsize equipment and reduce capital and operating costs
6. **Performance monitoring**: Meter and track key parameters to verify design performance and identify optimization opportunities

The analytical methods presented enable rigorous system design based on fundamental physics and proven engineering principles. Proper application of these methodologies yields chilled water systems that deliver reliable, efficient cooling throughout their 20-30 year service life.
