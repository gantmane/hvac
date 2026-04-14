---
title: "Evaporator Distribution in Liquid Overfeed Systems"
aliases: ["Evaporator Distribution in Liquid Overfeed Systems"]
description: "Comprehensive technical analysis of liquid refrigerant distribution methods in overfeed evaporators including spray headers, multi-circuit feeding, orifice design, and distribution uniformity optimization for industrial refrigeration systems."
weight: 10
---

## Overview of Evaporator Distribution

Liquid overfeed systems require precise refrigerant distribution to ensure uniform wetting of heat transfer surfaces and optimal evaporator performance. Distribution effectiveness directly impacts heat transfer efficiency, system capacity, and evaporator temperature uniformity. Poor distribution results in dry patches, reduced capacity, and potential compressor damage from liquid carryover or inadequate superheat.

Distribution systems must deliver refrigerant uniformly across all circuits and tube surfaces while maintaining proper circulation ratios, minimizing pressure drop, and accommodating varying load conditions. The distribution method depends on evaporator orientation, refrigerant type, operating temperatures, and system architecture.

## Distribution Methods and Configurations

### Top Feed Distribution

Top feed distribution introduces liquid refrigerant at the evaporator's upper section, allowing gravity to assist in downward flow. This configuration provides natural drainage, reduced oil trapping, and simplified liquid return. Top feed systems typically use spray headers with downward-facing nozzles or distribution manifolds with internal baffles.

**Advantages:**
- Gravity-assisted liquid flow
- Natural oil drainage to suction header
- Reduced risk of liquid accumulation
- Simplified defrost drainage
- Lower pumping head requirements

**Design considerations:**
- Spray pattern uniformity
- Nozzle spacing and orientation
- Header pressure drop
- Liquid subcooling requirements
- Minimum wetting flow rates

### Bottom Feed Distribution

Bottom feed systems introduce refrigerant at the evaporator base, requiring pumped circulation to wet upper surfaces. This method suits horizontal tube bundles and plate evaporators where upward flow through circuits provides consistent wetting. Bottom feed requires higher circulation ratios and careful attention to vapor separation in the return header.

**Applications:**
- Horizontal shell-and-tube evaporators
- Plate-type heat exchangers
- Flooded evaporator conversions
- Systems with limited overhead clearance

**Critical parameters:**
- Minimum circulation velocity
- Vapor quality at circuit outlets
- Return header sizing for separation
- Oil return provisions
- Liquid level control stability

### Spray Header Design

Spray headers distribute liquid refrigerant through multiple nozzles positioned to create overlapping spray patterns across evaporator surfaces. Header design must ensure equal pressure at all nozzle locations, proper spray cone angles, and sufficient liquid momentum to reach all heat transfer surfaces.

**Header sizing criteria:**
- Velocity limitations: 1-3 ft/s (0.3-0.9 m/s) to minimize pressure variation
- Pressure drop < 5% of nozzle pressure drop
- Internal baffles for flow straightening
- End cap provisions for cleanout and maintenance
- Material compatibility with refrigerant and lubricants

**Nozzle specifications:**
- Spray cone angle: 60-90 degrees typical
- Orifice diameter: 0.125-0.375 in (3.2-9.5 mm)
- Pressure drop: 3-10 psi (20-70 kPa) minimum
- Spacing: 12-36 in (300-900 mm) based on spray overlap
- Material: brass, stainless steel, or engineered plastic

## Multi-Evaporator Feed Strategies

Large refrigeration systems often supply multiple evaporators from a single liquid overfeed pump. Distribution design must account for varying evaporator capacities, different operating temperatures, and unequal piping lengths.

### Parallel Feed Configuration

Parallel feeding supplies all evaporators from a common liquid header. Each evaporator receives flow through individual branch lines with balancing orifices or control valves.

| Configuration Element | Design Specification | Purpose |
|----------------------|----------------------|---------|
| Main liquid header | Sized for total system flow at 2-4 ft/s | Minimize pressure variation |
| Branch line sizing | Individual evaporator flow at 3-6 ft/s | Maintain liquid momentum |
| Balancing orifices | Calculated for equal pressure drop | Equalize flow distribution |
| Isolation valves | Full-port ball valves | Service without system shutdown |
| Liquid subcooling | 5-15°F at header inlet | Prevent flash gas formation |

### Series Feed Configuration

Series feeding connects evaporators sequentially, with liquid exiting one evaporator feeding the next. This arrangement suits applications where evaporators operate at progressively lower temperatures or where space constraints limit parallel piping.

**Design requirements:**
- Progressive capacity reduction through series
- Adequate circulation ratio at final evaporator
- Intermediate liquid separation vessels
- Individual circuit balancing
- Temperature stratification management

## Distribution Header Design

Distribution headers must deliver uniform flow to all evaporator circuits regardless of circuit location along the header length. Proper header design accounts for momentum effects, pressure recovery, and flow division at each circuit takeoff.

### Header Sizing Methodology

Header diameter calculation follows the momentum principle where pressure drop through the header must be small compared to circuit pressure drop:

**Sizing criteria:**
- Reverse return configuration preferred for automatic balancing
- Header velocity < 3 ft/s (0.9 m/s) for uniform pressure
- Taper sections for large evaporators (>20 circuits)
- Internal baffles at inlet to distribute momentum
- Lateral spacing minimum 2× circuit connection diameter

### Circuit Takeoff Design

Circuit connections must extract flow without creating preferential flow patterns or dead zones in the header.

| Takeoff Configuration | Application | Pressure Balance |
|-----------------------|-------------|------------------|
| Side tappings | Standard horizontal headers | Good with proper spacing |
| Bottom tappings | Liquid subcooling maintenance | Excellent, self-draining |
| Top tappings | Vapor separation applications | Poor, avoid for liquid feed |
| Radial tappings | Large diameter headers | Excellent flow distribution |

## Orifice Sizing for Distribution

Distribution orifices create pressure drop to balance flow among parallel circuits and maintain liquid conditions. Orifice design must account for refrigerant properties, operating conditions, and circuit pressure characteristics.

### Orifice Calculation Method

Flow through distribution orifices follows standard incompressible flow equations with refrigerant property corrections:

**Flow equation:**
Q = C × A × √(2 × ρ × ΔP)

Where:
- Q = volumetric flow rate (ft³/min or m³/s)
- C = discharge coefficient (0.60-0.85 typical)
- A = orifice area (in² or m²)
- ρ = liquid density (lb/ft³ or kg/m³)
- ΔP = pressure drop (psi or kPa)

**Design pressure drops:**

| Application | Pressure Drop | Rationale |
|-------------|---------------|-----------|
| Circuit balancing | 3-5 psi (20-35 kPa) | Overcome piping variations |
| Flash gas prevention | 5-10 psi (35-70 kPa) | Maintain liquid subcooling |
| Spray nozzles | 5-15 psi (35-100 kPa) | Atomization and spray pattern |
| Main distribution | 10-20 psi (70-140 kPa) | System pressure control |

### Orifice Selection Guidelines

Proper orifice sizing requires knowledge of refrigerant flow rate, liquid properties, and allowable pressure drop:

1. Calculate required flow rate per circuit (tons × 4 × circulation ratio / circuits)
2. Determine liquid density at operating temperature
3. Select target pressure drop based on application
4. Calculate orifice diameter using flow equation
5. Select nearest standard orifice size
6. Verify actual pressure drop and flow rate
7. Confirm liquid conditions maintained (no flash gas)

**Standard orifice sizes:**
- 1/8 in (3.2 mm) - low capacity circuits
- 3/16 in (4.8 mm) - medium capacity circuits
- 1/4 in (6.4 mm) - high capacity circuits
- 5/16 in (7.9 mm) - very high capacity circuits
- 3/8 in (9.5 mm) - maximum standard size

## Return Header Design

Return headers collect refrigerant vapor and entrained liquid from evaporator circuits, providing vapor-liquid separation before return to the low-pressure receiver. Proper return header design prevents liquid carryover, facilitates oil return, and maintains stable suction conditions.

### Separation Chamber Sizing

Return headers must provide sufficient volume and residence time for gravity separation of liquid droplets from vapor flow.

| Parameter | Design Value | Basis |
|-----------|--------------|-------|
| Minimum diameter | 1.5× largest circuit connection | Flow distribution |
| Vapor velocity | <5 ft/s (1.5 m/s) horizontal | Droplet settling |
| Length-to-diameter ratio | Minimum 6:1 | Separation efficiency |
| Liquid seal depth | 4-8 in (100-200 mm) | Prevent vapor bypass |
| Vapor outlet location | Top of header, opposite inlet | Maximum separation path |
| Liquid drain connection | Bottom, minimum 2 in (50 mm) | Continuous liquid removal |

### Internal Configuration

Return header internals promote separation and prevent liquid carryover:

**Inlet baffles:**
- Perforated plates to break up liquid jets
- Mesh pads for droplet coalescence
- Impact plates perpendicular to flow
- Tangential inlet for centrifugal separation

**Outlet provisions:**
- Suction screen to protect compressors
- Velocity limiters (perforated baffles)
- Vortex breakers for liquid drain connections
- Thermowells for temperature monitoring

## Distribution Uniformity Optimization

Achieving uniform distribution requires attention to system hydraulics, refrigerant properties, and evaporator geometry.

### Hydraulic Balancing Techniques

**Reverse return piping:**
Equalizes total pressure drop for all circuits by ensuring equal piping lengths. The first circuit fed is the last circuit returned, automatically balancing flow distribution.

**Orifice balancing:**
Individual orifices sized to compensate for piping length differences and circuit variations. Each circuit orifice creates pressure drop inversely proportional to circuit resistance.

**Pressure-independent distribution:**
Control valves at each circuit maintain constant flow regardless of header pressure variations. Suitable for systems with widely varying loads or multiple temperature zones.

### Performance Verification

Distribution uniformity assessment methods:

| Method | Measurement | Target Performance |
|--------|-------------|-------------------|
| Temperature profiling | Circuit outlet temperatures | Within 2-4°F across all circuits |
| Frost pattern observation | Visual inspection during operation | Uniform frost coverage |
| Pressure drop measurement | Circuit inlet/outlet pressure | Equal ΔP all circuits ±10% |
| Capacity measurement | Individual circuit refrigeration effect | Equal capacity ±15% |

## Liquid Distribution Uniformity Metrics

Quantifying distribution quality requires systematic performance metrics:

**Distribution coefficient (DC):**
DC = (Q_max - Q_min) / Q_average × 100%

Where acceptable performance shows DC < 20% for industrial systems and DC < 10% for critical applications.

**Wetting efficiency:**
Ratio of actual wetted surface area to total heat transfer surface area. Target minimum 95% wetting under design load conditions.

## Falling Film Distribution Systems

Falling film evaporators require specialized distribution to create thin liquid films on vertical surfaces. Distribution uniformity directly impacts film stability and heat transfer performance.

### Distribution Header Requirements

Falling film systems use perforated tubes or slotted headers positioned above tube bundles:

**Design specifications:**

| Component | Specification | Performance Impact |
|-----------|--------------|-------------------|
| Header type | Perforated tube or slotted channel | Film formation uniformity |
| Perforation spacing | 0.5-2 in (12-50 mm) centers | Film overlap and coverage |
| Hole diameter | 0.125-0.250 in (3-6 mm) | Film thickness control |
| Distribution height | 2-6 in (50-150 mm) above tubes | Splash prevention |
| Liquid flow rate | 0.5-2 gpm/ft (6-25 L/min/m) | Film stability |

**Film distribution quality factors:**
- Header pressure uniformity
- Liquid subcooling at distribution point
- Surface wetting characteristics
- Tube pitch and spacing
- Operating temperature and pressure

## System Integration Considerations

Distribution system design must account for interaction with other system components:

**Liquid supply requirements:**
- Pump delivery pressure adequate for distribution + static head + line losses
- Liquid subcooling margin to prevent flash gas
- Flow control for capacity modulation
- Emergency backup feed provisions

**Defrost integration:**
- Hot gas distribution for uniform defrost
- Condensate drainage provisions
- Liquid retention during defrost
- Re-wetting after defrost termination

**Control system interface:**
- Flow measurement and verification
- Temperature monitoring at critical points
- Pressure monitoring for hydraulic balance
- Alarm conditions for distribution failure

## Troubleshooting Distribution Problems

Common distribution issues and diagnostic approaches:

| Symptom | Probable Cause | Corrective Action |
|---------|----------------|-------------------|
| Uneven frosting patterns | Poor liquid distribution | Verify orifice sizing, check for plugging |
| Liquid carryover to suction | Excessive circulation ratio | Reduce feed rate, increase separation volume |
| Low system capacity | Inadequate refrigerant feed | Check pump performance, verify orifices |
| Temperature stratification | Preferential circuit flow | Balance circuit pressure drops |
| Oil accumulation | Insufficient liquid velocity | Increase circulation ratio, verify drain paths |

Distribution system performance directly determines liquid overfeed system efficiency, capacity, and reliability. Proper design, installation, and commissioning ensure optimal refrigerant distribution and long-term system performance.
