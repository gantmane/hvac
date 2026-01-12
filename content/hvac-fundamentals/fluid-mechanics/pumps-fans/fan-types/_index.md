---
title: "Fan Types"
description: "Comprehensive analysis of HVAC fan types including centrifugal, axial, and mixed flow configurations with performance characteristics, selection criteria, and sizing methods"
weight: 3
---

HVAC fans convert mechanical shaft power into airflow and pressure rise through two fundamental mechanisms: centrifugal force (radial flow) and axial momentum transfer. Fan selection requires matching impeller geometry, speed, and size to the required operating point defined by volumetric flow rate and static pressure rise.

## Classification by Flow Direction

Fans are classified by the primary direction of airflow through the impeller relative to the shaft axis.

### Centrifugal Fans

Centrifugal fans draw air axially into the impeller eye and discharge it radially at 90° to the shaft through centrifugal force. Air enters near the hub and is accelerated outward by impeller rotation, converting velocity pressure to static pressure in the scroll housing.

**Performance Characteristics:**
- Static pressure capability: 0.5 to 15 in. w.g. (125 to 3,750 Pa)
- Flow range: 100 to 300,000 cfm (50 to 150,000 L/s)
- Static efficiency: 60% to 85% (peak)
- Total efficiency: 65% to 88% (peak)
- Sound levels: 65 to 95 dBA at 5 ft (1.5 m)

**Construction Elements:**
- Housing (scroll or volute): converts velocity to static pressure
- Impeller with backward, forward, or radial blades
- Inlet cone or bell mouth for smooth entry
- Shaft, bearings, and drive system
- Cutoff point positioned to minimize recirculation

**Applications:**
- Air handling units and packaged equipment
- High static pressure duct systems
- Clean room pressurization
- Industrial exhaust systems
- Material handling (pneumatic conveying)

### Axial Fans

Axial fans move air parallel to the shaft axis. Airfoil-shaped blades impart axial momentum while generating a pressure rise through lift forces similar to aircraft propellers.

**Performance Characteristics:**
- Static pressure capability: 0.1 to 8 in. w.g. (25 to 2,000 Pa)
- Flow range: 500 to 500,000 cfm (250 to 250,000 L/s)
- Static efficiency: 40% to 75%
- Total efficiency: 50% to 85%
- Sound levels: 70 to 100 dBA at 5 ft (1.5 m)

**Configuration Types:**
- Propeller fans: no ductwork, free discharge
- Tubeaxial fans: cylindrical housing, no guide vanes
- Vaneaxial fans: cylindrical housing with straightening vanes

**Applications:**
- Cooling towers
- Air-cooled condensers
- Ventilation exhaust systems
- Low-pressure supply systems
- Equipment cooling

### Mixed Flow Fans

Mixed flow fans combine centrifugal and axial characteristics, with airflow entering axially and discharging at 45° to 60° from the shaft axis. These fans bridge the gap between centrifugal and axial designs.

**Performance Characteristics:**
- Static pressure capability: 1 to 6 in. w.g. (250 to 1,500 Pa)
- Flow range: 1,000 to 100,000 cfm (500 to 50,000 L/s)
- Static efficiency: 55% to 78%
- Compact installation envelope
- Lower noise than equivalent centrifugal fans

**Applications:**
- Space-constrained installations
- Variable air volume systems
- Data center cooling
- Industrial process ventilation

## Centrifugal Fan Blade Configurations

Blade shape fundamentally determines the performance curve characteristics and efficiency of centrifugal fans.

### Backward Curved (BC) and Backward Inclined (BI)

Blades curve or incline away from the direction of rotation. The outlet blade angle β₂ ranges from 45° to 90° (measured from tangent to rotation).

**Performance Characteristics:**
- Non-overloading power characteristic
- Peak efficiency: 75% to 88%
- Self-limiting horsepower curve
- Stable operation across wide flow range
- Lower discharge velocities than forward curved

**Blade Configurations:**
- Backward curved: 12 to 16 curved blades
- Backward inclined: 7 to 12 flat blades
- Airfoil: 9 to 16 airfoil-shaped blades (highest efficiency)

**Power Relationship:**

Power rises to a maximum at approximately 50% of wide-open volume, then decreases. This characteristic prevents motor overload during high-flow conditions.

**Applications:**
- Variable air volume systems
- Energy-efficient constant volume systems
- Clean air applications
- Where non-overloading power is critical

### Forward Curved (FC)

Blades curve toward the direction of rotation with outlet angles β₂ less than 90° (typically 60° to 75°). Also called "squirrel cage" fans.

**Performance Characteristics:**
- Overloading power characteristic
- Peak efficiency: 60% to 70%
- Compact design for given flow and pressure
- High discharge velocity
- More blades (24 to 64 shallow blades)

**Power Relationship:**

Power increases continuously with flow rate. Motor must be sized for worst-case maximum flow condition to prevent overload.

**Applications:**
- Packaged air handling units
- Rooftop units
- Furnaces and residential equipment
- Low first-cost applications
- Where space is limited

### Radial Blade (Straight Blade)

Blades extend straight from hub to rim with β₂ = 90°. Simple, rugged construction.

**Performance Characteristics:**
- Steep pressure curve
- Peak efficiency: 65% to 75%
- Self-cleaning capability
- Handles particulate-laden airstreams
- Moderate overloading characteristic

**Applications:**
- Industrial exhaust with particulates
- Material handling
- Corrosive or erosive environments
- High-temperature applications

## Axial Fan Configurations

### Propeller Fans

Simple blade design without housing, used for free air delivery against minimal resistance.

**Performance Characteristics:**
- Static pressure capability: 0 to 0.25 in. w.g. (0 to 60 Pa)
- High flow rates at low pressure
- Low efficiency: 35% to 55%
- Inexpensive construction
- Sheet metal or cast blades

**Applications:**
- Wall and roof ventilators
- Air circulation in large spaces
- Equipment cooling
- Agricultural ventilation

### Tubeaxial Fans

Axial impeller mounted in cylindrical housing without guide vanes.

**Performance Characteristics:**
- Static pressure capability: 0.5 to 3 in. w.g. (125 to 750 Pa)
- Efficiency: 50% to 70%
- Compact in-line installation
- Swirling discharge airflow

**Applications:**
- In-line duct boosting
- General ventilation
- Tunnel ventilation
- Industrial exhaust

### Vaneaxial Fans

Axial impeller with airfoil blades in cylindrical housing with inlet or discharge guide vanes to eliminate swirl and recover pressure.

**Performance Characteristics:**
- Static pressure capability: 1 to 8 in. w.g. (250 to 2,000 Pa)
- Efficiency: 65% to 85%
- Guide vanes recover velocity pressure
- Improved pressure characteristics
- Lower noise than tubeaxial

**Applications:**
- High-pressure ventilation systems
- Industrial process systems
- Clean room supply
- Laboratory exhaust

## Fan Performance Equations

### Fan Total Pressure

Fan total pressure (FTP) represents the total energy added by the fan:

**FTP = TP₂ - TP₁**

Where:
- TP₂ = total pressure at fan outlet
- TP₁ = total pressure at fan inlet

Alternatively:

**FTP = FSP + FVP**

Where:
- FSP = fan static pressure
- FVP = fan velocity pressure at discharge

### Fan Static Pressure

Fan static pressure represents the useful pressure rise for overcoming system resistance:

**FSP = SP₂ - SP₁ + VP₁**

The inlet velocity pressure is added because it represents energy already possessed by the air entering the fan.

### Velocity Pressure

Velocity pressure at any point:

**VP = (V/4005)² (for ρ = 0.075 lb/ft³)**

**VP = ρV²/2**

Where:
- V = velocity, fpm or m/s
- ρ = air density, lb/ft³ or kg/m³

### Fan Power

**Shaft Power (bhp) = (Q × FTP) / (6356 × η)**

Where:
- Q = airflow rate, cfm
- FTP = fan total pressure, in. w.g.
- η = fan total efficiency (decimal)

**Motor Power Required = bhp / η_m / SF**

Where:
- η_m = motor efficiency
- SF = service factor (typically 1.15)

### Efficiency Definitions

**Static Efficiency:**

**η_s = (Q × FSP) / (6356 × bhp)**

**Total Efficiency:**

**η_t = (Q × FTP) / (6356 × bhp)**

Total efficiency is always higher than static efficiency because it includes the useful work done in creating discharge velocity.

## Fan Laws

The fan laws describe how performance changes with speed, density, and size changes.

### Speed Changes (Constant Size and Density)

**Flow Rate:** Q₂/Q₁ = N₂/N₁

**Pressure:** P₂/P₁ = (N₂/N₁)²

**Power:** bhp₂/bhp₁ = (N₂/N₁)³

Where N = fan speed, rpm

### Density Changes (Constant Speed and Size)

**Flow Rate:** Q₂/Q₁ = 1 (unchanged)

**Pressure:** P₂/P₁ = ρ₂/ρ₁

**Power:** bhp₂/bhp₁ = ρ₂/ρ₁

### Size Changes (Constant Speed and Density)

**Flow Rate:** Q₂/Q₁ = (D₂/D₁)³

**Pressure:** P₂/P₁ = (D₂/D₁)²

**Power:** bhp₂/bhp₁ = (D₂/D₁)⁵

Where D = impeller diameter

## Selection Criteria

### Operating Point Determination

The fan must operate at the intersection of the fan curve and system curve.

**System Pressure Loss:**

**ΔP_sys = K × Q²**

Where K represents the system resistance coefficient incorporating all friction losses and dynamic losses.

### Efficiency Considerations

Select fans to operate within 10% of peak efficiency on the performance curve. Operating significantly left or right of peak efficiency results in:
- Increased energy consumption
- Higher noise levels
- Potential instability
- Reduced equipment life

### Sound Level Requirements

Fan sound power level is governed by:

**PWL ≈ K_L + 10 log(Q) + 20 log(P) + correction factors**

Where:
- PWL = sound power level, dB
- K_L = constant dependent on fan type
- Q = flow rate
- P = pressure rise

**Noise Reduction Strategies:**
- Operate at lower tip speeds (reduce rpm)
- Select backward curved or airfoil blades
- Oversize fan and operate at reduced speed
- Use inlet and discharge silencers
- Implement vibration isolation

### System Effect Factors

AMCA Standard 201 defines system effects that degrade installed performance:

**System Effect Factor Categories:**
- Inlet obstructions and poor entry conditions
- Outlet obstructions and duct transitions
- Inlet box effects
- Inadequate clearances

Add system effect losses to calculated system pressure to determine required fan pressure.

## Fan Sizing Methodology

### Step 1: Calculate Required Airflow

Determine required cfm from:
- Sensible cooling load: Q = Q_s / (1.08 × ΔT)
- Ventilation requirements: ASHRAE 62.1
- Exhaust requirements
- Process requirements

### Step 2: Calculate System Pressure Loss

Sum all pressure losses:

**ΔP_total = ΔP_duct + ΔP_fittings + ΔP_coils + ΔP_filters + ΔP_terminals + ΔP_grilles**

Add system effect factors per AMCA 201.

### Step 3: Apply Safety Factors

**Design Flow:** Q_design = Q_required × 1.1 to 1.25

**Design Pressure:** P_design = P_calculated × 1.1 to 1.15

Safety factors account for:
- Filter loading
- Coil fouling
- Duct leakage
- Future modifications

### Step 4: Select Fan

Review manufacturer's certified performance data. Ensure:
- Operating point within selection range
- Efficiency within 90% of peak
- Sound levels meet project requirements
- Motor sized for maximum load condition
- Structural and spatial requirements met

### Step 5: Verify Motor Power

Calculate required bhp including all losses and safety factors. Select motor per NEMA standards with adequate service factor.

## Comparative Performance Table

| Fan Type | Pressure Range (in. w.g.) | Peak Efficiency | Power Characteristic | Typical Applications | Relative First Cost |
|----------|---------------------------|-----------------|----------------------|----------------------|---------------------|
| **Centrifugal Fans** | | | | | |
| Airfoil (BC) | 1 - 10 | 82% - 88% | Non-overloading | VAV systems, high efficiency | High |
| Backward Inclined | 1 - 8 | 75% - 82% | Non-overloading | General HVAC, constant volume | Medium-High |
| Backward Curved | 0.5 - 6 | 70% - 78% | Non-overloading | Packaged equipment | Medium |
| Forward Curved | 0.25 - 3 | 60% - 70% | Overloading | Packaged units, residential | Low-Medium |
| Radial Blade | 1 - 10 | 65% - 75% | Moderately overloading | Industrial, particulate | Medium |
| **Axial Fans** | | | | | |
| Vaneaxial | 1 - 8 | 70% - 85% | Overloading | High-pressure ventilation | Medium-High |
| Tubeaxial | 0.5 - 3 | 50% - 70% | Overloading | General ventilation | Low-Medium |
| Propeller | 0 - 0.25 | 35% - 55% | Severely overloading | Free discharge | Low |
| **Mixed Flow** | 1 - 6 | 65% - 78% | Non-overloading | Compact installations | Medium-High |

## Design Considerations

### Installation Requirements

**Inlet Conditions:**
- Provide straight duct run of 2.5D to 4D upstream
- Use bell mouth or inlet cone for improved entry
- Avoid obstructions within 1D of inlet
- Maintain uniform velocity profile

**Outlet Conditions:**
- Provide straight duct run of 4D to 6D downstream
- Avoid abrupt transitions
- Size outlet duct to limit velocity to 2500 fpm
- Use turning vanes in elbows near discharge

### Vibration Isolation

Mount fans on:
- Inertia base for floor mounting
- Spring isolators (1 to 2 inches deflection)
- Flexible duct connectors at inlet and discharge
- Structural isolation from building

### Parallel and Series Operation

**Parallel Operation:**
- Increases flow rate at same pressure
- Fans must have similar characteristics
- Use for redundancy or capacity staging

**Series Operation:**
- Increases pressure at same flow rate
- Useful for high-resistance systems
- Requires careful matching of fan curves

### Variable Speed Control

Variable frequency drives (VFD) provide significant energy savings:

**Power Reduction:** bhp₂/bhp₁ = (N₂/N₁)³

Operating at 80% speed reduces power to 51% of full speed power.

**VFD Considerations:**
- Use inverter-duty motors
- Maintain minimum speed for bearing lubrication
- Consider harmonic impacts on electrical system
- Verify stable operation across speed range

## Code and Standard References

**AMCA Standards:**
- AMCA 210-16: Laboratory Methods of Testing Fans for Certified Aerodynamic Performance Rating
- AMCA 201: Fans and Systems
- AMCA 300: Reverberant Room Method for Sound Testing of Fans
- AMCA 99: Standards Handbook

**ASHRAE Standards:**
- ASHRAE Standard 51: Laboratory Methods of Testing Fans for Aerodynamic Performance Rating
- ASHRAE Standard 62.1: Ventilation for Acceptable Indoor Air Quality
- ASHRAE Handbook - HVAC Systems and Equipment, Chapter 21: Fans

**NFPA Standards:**
- NFPA 90A: Standard for Installation of Air-Conditioning and Ventilating Systems
- NFPA 92: Standard for Smoke Control Systems
- NFPA 96: Standard for Ventilation Control and Fire Protection of Commercial Cooking Operations

**Other References:**
- SMACNA HVAC Systems Duct Design
- UFC 3-410-01: Heating, Ventilating, and Air Conditioning Systems (for DoD facilities)

## Special Considerations

### High-Temperature Service

For temperatures exceeding 200°F (93°C):
- Use special high-temperature construction
- Select heat-resistant bearing lubricants
- Provide thermal expansion clearances
- Consider material thermal growth

### Corrosive Environments

Material selection for corrosive service:
- Stainless steel construction (304, 316)
- Coated carbon steel (epoxy, powder coat)
- Fiberglass reinforced plastic (FRP)
- Special alloys for severe service

### Explosion-Proof Requirements

Class I Division 1 or 2 locations require:
- Non-sparking construction (aluminum, bronze)
- Explosion-proof motors and starters
- Static grounding
- Spark-resistant construction per AMCA 99

### Seismic Requirements

In seismic zones, provide:
- Seismic isolation systems
- Structural reinforcement
- Flexible connections
- Compliance with IBC and ASCE 7

## Performance Testing and Verification

Field verification per AMCA 203:

**Measured Parameters:**
- Airflow rate (pitot traverse or flow station)
- Fan total pressure (inlet and outlet)
- Fan speed (tachometer)
- Motor power (true RMS power meter)
- Sound levels (per AMCA 300)

**Calculate and Compare:**
- Actual vs. design airflow (within ±10%)
- Actual vs. design pressure (within ±5%)
- Measured vs. predicted power (within ±10%)
- Fan efficiency vs. rated efficiency

Document deviations and implement corrective measures if performance does not meet specifications.
