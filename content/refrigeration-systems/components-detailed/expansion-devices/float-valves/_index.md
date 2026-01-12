---
title: "Float Valves"
description: "Comprehensive guide to refrigeration float valves including high-side and low-side configurations, liquid level control mechanisms, flooded evaporator applications, and sizing criteria for HVAC systems."
weight: 4
---

Float valves provide automatic refrigerant flow control by maintaining constant liquid levels in refrigeration system components. These mechanical expansion devices use buoyancy principles to regulate refrigerant metering without external power or control signals.

## Operating Principles

Float valves operate on the principle that a buoyant element responds to liquid level changes, mechanically positioning a needle valve to modulate refrigerant flow. The float assembly maintains equilibrium between refrigerant supply and evaporation rate, ensuring optimal liquid inventory in the controlled vessel.

The fundamental operation relies on Archimedes' principle where the buoyant force equals the weight of displaced liquid:

F_b = ρ_liquid × V_displaced × g

As liquid level rises, increased buoyant force overcomes spring and linkage forces to close the valve. Conversely, falling liquid levels reduce buoyancy, allowing the valve to open and admit more refrigerant.

## High-Side Float Valves

High-side float (HSF) valves install in the high-pressure liquid line before the evaporator, maintaining liquid level in a high-pressure receiver or float chamber. The float responds to liquid refrigerant at condenser pressure.

### Configuration and Operation

The HSF assembly consists of:

- Float chamber operating at condensing pressure (100-300 psig typical)
- Spherical or cylindrical float element constructed from copper, brass, or stainless steel
- Needle valve and seat assembly sized for system capacity
- Mechanical linkage connecting float to valve stem
- Equalization connections for pressure balance

When evaporator load increases, liquid level in the high-side chamber drops. The descending float opens the valve, metering refrigerant to the evaporator. Reduced load causes liquid accumulation, raising the float and throttling flow.

### Applications

HSF valves are suited for:

- Flooded shell-and-tube evaporators in large chillers
- Multiple evaporator systems requiring individual level control
- Applications with widely varying loads
- Marine and mobile refrigeration where orientation changes occur
- Low-temperature systems where precise liquid management is critical

### Advantages and Limitations

**Advantages:**
- Maintains constant liquid level regardless of load variations
- No superheat hunting or capacity loss from superheat requirements
- Automatically compensates for refrigerant charge variations
- Suitable for systems with multiple evaporators at different temperatures

**Limitations:**
- Requires vertical installation for proper float orientation
- Not suitable for direct expansion (DX) systems
- Limited turndown ratio (typically 10:1 maximum)
- Sensitive to liquid line pressure drop
- Requires adequately sized float chamber volume

## Low-Side Float Valves

Low-side float (LSF) valves maintain liquid level directly in the evaporator, operating at evaporating pressure. The float chamber forms an integral part of the evaporator vessel or connects via external equalization lines.

### Configuration and Operation

LSF valve assemblies include:

- Float mechanism immersed in evaporator at suction pressure (5-70 psig typical)
- Valve body constructed to withstand full high-side pressure differential
- Needle and seat designed for high pressure drop service (100-250 psi ΔP)
- Float arm and linkage configured for evaporator geometry
- Optional pilot-operated designs for larger capacities

The LSF valve opens when liquid level drops due to evaporation, admitting high-pressure liquid directly from the receiver. Rising liquid level closes the valve, preventing overfilling and liquid slugging to the compressor.

### Design Considerations

**Float Sizing:**
Float displacement must overcome valve spring force, friction, and differential pressure effects. Required float volume:

V_float = (F_spring + F_friction + F_ΔP) / (ρ_liquid × g)

**Valve Capacity:**
LSF valves must pass full system capacity through a single orifice. Capacity depends on:
- Orifice diameter and flow coefficient
- Pressure differential across valve
- Refrigerant subcooling entering valve
- Flashing losses in valve body

### Applications

LSF valves excel in:

- Flooded shell-and-tube evaporators
- Ammonia refrigeration systems
- Ice-making equipment
- Large cold storage facilities
- Industrial process cooling with constant evaporator temperature

## Float Valve Specifications

| Parameter | High-Side Float | Low-Side Float | Units |
|-----------|----------------|----------------|-------|
| Operating Pressure | Condensing | Evaporating | psig |
| Typical Pressure Range | 100-300 | 5-70 | psig |
| Pressure Drop Across Valve | 5-15 | 100-250 | psi |
| Capacity Range | 1-100 | 1-50 | tons |
| Turndown Ratio | 10:1 | 5:1 | - |
| Response Time | 5-15 | 2-8 | seconds |
| Float Material | Copper, Brass | Stainless Steel | - |
| Installation Orientation | Vertical ±10° | Vertical ±5° | degrees |

## Float Construction and Materials

### Float Element Design

Float elements must provide sufficient buoyancy while withstanding system pressures and temperatures:

**Hollow Sphere Floats:**
- Diameter: 2-8 inches typical
- Wall thickness: 0.020-0.060 inches
- Material: Seamless drawn copper or brass
- Maximum working pressure: 400 psig
- Buoyant force: 0.5-8 lbf depending on size

**Cylindrical Floats:**
- Length: 4-12 inches
- Diameter: 1.5-4 inches
- Sealed end caps welded or brazed
- Lower profile for compact installations

### Valve Body Materials

| Component | Material | Pressure Rating | Application |
|-----------|----------|-----------------|-------------|
| Body | Bronze, Cast Iron | 300-600 psig | Standard duty |
| Body | Stainless Steel | 600-1000 psig | High pressure, ammonia |
| Seat | Brass, Stainless | - | All applications |
| Needle | Hardened Stainless | - | Erosion resistance |
| Linkage | Stainless Steel | - | Corrosion resistance |

## Liquid Level Control Mechanisms

### Direct Acting Float Valves

The float directly connects to the valve stem through a simple lever mechanism. Movement ratio between float travel and valve lift typically ranges from 3:1 to 8:1.

**Design Parameters:**
- Float travel: 2-6 inches
- Valve lift: 0.25-1 inch
- Mechanical advantage: Lever ratio determines force multiplication
- Sealing force: Must overcome system pressure differential

### Pilot-Operated Float Valves

Large capacity systems use pilot-operated designs where the float controls a small pilot valve. Pilot pressure actuates a main valve diaphragm or piston.

**Advantages:**
- Handles capacities exceeding 100 tons refrigeration
- Reduces float size and force requirements
- Enables remote float chamber location
- Improves response time and control stability

**Configuration:**
- Pilot valve: 1/8 to 1/4 inch orifice
- Main valve: 1/2 to 3 inch connection
- Pressure amplification ratio: 10:1 to 50:1
- Response lag: 1-3 seconds additional

## Flooded Evaporator Applications

Float valves enable flooded evaporator operation, where liquid refrigerant covers the entire heat transfer surface. This configuration maximizes heat transfer coefficient and evaporator effectiveness.

### System Requirements

**Refrigerant Charge:**
Flooded systems require substantial refrigerant inventory:
- 50-70% of evaporator internal volume filled with liquid
- Additional charge in receiver and float chamber
- Charge mass: 2-5 lbm per ton of refrigeration typical

**Liquid Management:**
- Suction accumulator prevents liquid carryover to compressor
- Oil return provisions ensure lubricant circulation
- Purge systems remove non-condensables from evaporator

### Heat Transfer Performance

Flooded evaporators achieve superior performance compared to DX designs:

| Parameter | Flooded with Float | Direct Expansion | Improvement |
|-----------|-------------------|------------------|-------------|
| Overall U-Value | 150-200 | 100-140 | Btu/hr-ft²-°F |
| Required LMTD | 5-8 | 8-12 | °F |
| Active Surface | 95-100% | 60-80% | % |
| Superheat Penalty | 0-2 | 8-15 | °F |

## Sizing and Selection Criteria

### Capacity Determination

Float valve capacity must equal maximum evaporator load accounting for safety factors:

Q_valve = Q_evaporator × SF

Where:
- Q_valve = Required valve capacity (tons or Btu/hr)
- Q_evaporator = Maximum evaporator load
- SF = Safety factor (1.15-1.25 typical)

### Valve Flow Coefficient

The valve flow coefficient C_v relates capacity to pressure drop:

C_v = Q / (ΔP × SG)^0.5

For refrigerants, manufacturers provide capacity charts showing tons of refrigeration versus pressure differential and refrigerant type.

### Orifice Sizing

Minimum orifice diameter prevents excessive pressure drop and flashing:

d_min = [4Q / (π × v_max × ρ_liquid)]^0.5

Where:
- d_min = Minimum orifice diameter (inches)
- Q = Volumetric flow rate (in³/sec)
- v_max = Maximum velocity (300-600 ft/min)
- ρ_liquid = Liquid density (lbm/ft³)

## Selection Tables

### Float Valve Capacity by Refrigerant

| Valve Size | R-22 | R-134a | R-404A | R-717 (NH3) | Units |
|------------|------|--------|--------|-------------|-------|
| 1/2 inch | 5 | 4.5 | 4.8 | 6.5 | tons |
| 3/4 inch | 12 | 10.5 | 11 | 15 | tons |
| 1 inch | 22 | 19 | 20 | 28 | tons |
| 1-1/4 inch | 38 | 33 | 35 | 48 | tons |
| 1-1/2 inch | 55 | 48 | 51 | 70 | tons |
| 2 inch | 95 | 83 | 88 | 120 | tons |

*Based on 100 psi pressure drop, 40°F evaporator temperature, 10°F subcooling*

### Float Chamber Sizing

| System Capacity | Chamber Volume | Float Diameter | Liquid Holdup | Units |
|----------------|----------------|----------------|---------------|-------|
| 5-10 tons | 0.5 | 3 | 0.3 | gallons/inches/gallons |
| 10-20 tons | 1.0 | 4 | 0.6 | gallons/inches/gallons |
| 20-40 tons | 2.0 | 5 | 1.2 | gallons/inches/gallons |
| 40-75 tons | 4.0 | 6 | 2.4 | gallons/inches/gallons |
| 75-150 tons | 8.0 | 8 | 4.8 | gallons/inches/gallons |

## Installation Requirements

### Mounting Orientation

Float valves require vertical installation within specified tolerances:
- HSF valves: ±10° from vertical maximum
- LSF valves: ±5° from vertical maximum
- Float chamber must be plumb for accurate level control
- Vibration isolation prevents mechanical wear

### Piping Connections

**High-Side Float:**
- Inlet: Liquid line from condenser or receiver
- Outlet: Liquid line to evaporator inlet
- Equalizer: Vapor connection to maintain pressure balance
- Drain: Low-point connection for service

**Low-Side Float:**
- Inlet: High-pressure liquid from receiver
- Float chamber: Integrated with evaporator or external vessel
- Equalization: Vapor lines between float chamber and evaporator
- Level sight glass: Visual verification of liquid level

### Service Access

- Isolation valves on inlet and outlet for valve replacement
- Strainer upstream of valve to prevent debris damage
- Pressure test ports for differential measurement
- Access flanges for internal inspection without system disassembly

## Maintenance and Troubleshooting

### Preventive Maintenance

**Quarterly Inspection:**
- Verify proper liquid level through sight glass
- Check for refrigerant leaks at valve body and connections
- Inspect linkage for wear or corrosion
- Monitor pressure drop across valve

**Annual Service:**
- Disassemble and inspect valve internals
- Replace seats if scoring or erosion evident
- Check float for leaks (submerge in water, observe bubbles)
- Verify valve stroke and seating force
- Clean strainer and check for debris accumulation

### Common Problems

| Symptom | Probable Cause | Corrective Action |
|---------|---------------|-------------------|
| Liquid level hunting | Oversized valve | Reduce valve capacity or add restriction |
| Low liquid level | Undersized valve, restricted inlet | Increase valve size, clear restriction |
| High liquid level | Float leak, linkage failure | Replace float, repair linkage |
| Flooding to compressor | LSF valve stuck open | Clean valve, check for debris |
| Starved evaporator | HSF valve stuck closed | Check inlet pressure, clean valve |
| Erratic operation | Flashing in liquid line | Increase subcooling, reduce line ΔP |

## Performance Optimization

### Control Stability

Float valve systems achieve stable control when:
- Float displacement provides 2-3 times minimum required force
- Valve capacity matches load within 15%
- Chamber volume equals 5-10 minutes of flow at design capacity
- Pressure drop does not cause excessive flashing

### Efficiency Improvements

**Subcooling Enhancement:**
Increased liquid subcooling improves float valve performance:
- Reduces flashing losses in valve body
- Enables smaller valve sizing
- Improves capacity stability
- Typical target: 10-15°F subcooling

**Pressure Drop Reduction:**
Minimize liquid line pressure drop to prevent premature flashing:
- Limit velocity to 300 ft/min maximum
- Size piping for 1-2 psi/100 ft pressure drop
- Locate float chamber close to evaporator
- Eliminate unnecessary fittings and valves

## Comparison with Other Expansion Devices

| Characteristic | Float Valve | TXV | EEV | Capillary Tube |
|----------------|-------------|-----|-----|----------------|
| Superheat Control | No | Yes | Yes | No |
| Load Following | Excellent | Good | Excellent | Poor |
| Refrigerant Distribution | Excellent | Good | Excellent | Fair |
| Cost | Moderate | Moderate | High | Low |
| Maintenance | Moderate | Low | Moderate | None |
| Application | Flooded | DX | DX | Small DX |
| Turndown Ratio | 10:1 | 5:1 | 20:1 | Fixed |

Float valves excel in flooded evaporator applications where maintaining constant liquid level maximizes heat transfer efficiency and eliminates superheat penalties associated with direct expansion systems.
