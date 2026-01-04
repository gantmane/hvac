---
title: "Refuge Areas and Safe Havens"
description: "Pressurization requirements, air supply systems, elevator lobbies as refuge areas, and life safety design for protected spaces in tall buildings."
date: "2026-01-04"
weight: 8
tags: ["refuge areas", "safe havens", "elevator lobbies", "pressurization", "life safety", "accessibility"]
categories: ["Specialty Applications"]
---

## Refuge Area Concepts

Refuge areas provide temporary safe locations within tall buildings for occupants unable to immediately evacuate during emergencies. These spaces—also called areas of refuge, safe havens, or evacuation assistance spaces—protect occupants from fire, smoke, and heat while awaiting rescue or until conditions allow continued evacuation.

Building codes require refuge areas in specific circumstances:
- High-rise buildings (> 75 feet above fire department access)
- Buildings lacking adequate egress capacity for all occupants
- Areas serving occupants with mobility impairments
- Locations designated for firefighter staging operations

## Code Requirements

### International Building Code (IBC)

IBC establishes refuge area provisions:

**Location Requirements**:
- Located immediately adjacent to exit enclosures (stairs)
- Accessible without passing through non-protected spaces
- Maximum travel distance same as for exits
- Minimum of two refuge areas per floor (egress independence)

**Size Requirements**:
- Minimum area: 30 inches × 48 inches per occupant wheelchair space
- Minimum two wheelchair spaces per refuge area
- Additional space for ambulatory occupants if area serves general refuge function
- Clear floor space complying with accessibility standards

**Separation Requirements**:
- Separated from remainder of floor by smoke barrier (minimum 1-hour fire-resistance rating)
- Protected from exposure through exterior walls
- Protected from vertical fire spread through floor/ceiling assemblies

**Communication**:
- Two-way communication system to fire command center
- Visual and tactile identification signage
- Emergency lighting per life safety code

### NFPA 101 (Life Safety Code)

NFPA 101 provides additional criteria:

**Occupant Load Calculation**: Refuge area sized for:
- Occupants served by that area
- Typically calculated as percentage of floor occupant load (15-20% for mobility-impaired)
- All occupants if area serves as general safe haven

**Environmental Control**: Maintain tenable conditions:
- Smoke-free environment through pressurization
- Thermal conditions within survivable limits
- Adequate oxygen concentration through ventilation

**Duration**: Designed for occupancy duration until:
- Rescue by firefighters
- Fire suppression enables continued evacuation
- Typically 30-60 minutes minimum design period

## Pressurization Requirements

Refuge areas require positive pressure relative to fire floor to prevent smoke infiltration.

### Minimum Pressure Differentials

**Design Pressures**:
- Minimum: 0.05 in. w.c. (25 Pa) across smoke barrier
- Typical design target: 0.10-0.15 in. w.c. (50-75 Pa)
- Maximum: 0.35 in. w.c. (175 Pa) to limit door opening forces

These values align with smoke control system requirements per NFPA 92.

### Pressure Hierarchy

In integrated systems, pressure staging creates multiple protection layers:

**Four-Zone System Example**:
1. Exit stair: 0.25 in. w.c. (highest pressure)
2. Refuge area: 0.15 in. w.c.
3. Protected corridor: 0.05 in. w.c.
4. Fire floor: 0.00 in. w.c. (reference)

Each boundary maintains minimum differential while limiting maximum for door operation.

### Stack Effect Considerations

Tall building stack effect affects refuge area pressurization:

**Winter Conditions** (upward stack effect):
- Lower floors: stack effect creates negative pressure
- Refuge area system must overcome stack effect plus provide design differential
- Upper floors: stack effect assists pressurization
- Risk of over-pressurization requiring pressure relief

**Summer Conditions** (downward or minimal stack effect):
- More uniform pressure distribution
- Upper floors may require increased pressurization
- Generally less challenging than winter conditions

**Design Approach**:
- Calculate stack effect for design outdoor temperature
- Size system for worst-case floor and conditions
- Provide floor-by-floor pressure balancing
- Install relief dampers where over-pressurization anticipated

## Air Supply Systems

### Supply Airflow Calculation

Required supply airflow maintains design pressure against all leakage paths:

$$Q_{supply} = \sum \left(A_i \times 2610 \times \sqrt{\Delta P_i}\right)$$

Where:
- $Q_{supply}$ = required supply airflow (cfm)
- $A_i$ = effective leakage area of opening i (ft²)
- $\Delta P_i$ = pressure differential across opening i (in. w.c.)

**Leakage Paths**:
- Doors to fire floor (primary leakage)
- Doors to exit stair (if pressure staging employed)
- Construction leakage through smoke barrier
- Ventilation or relief air openings

**Example Calculation**: Refuge area (elevator lobby) with:
- 1 door to fire floor corridor (0.15 ft² leakage)
- 1 door to exit stair (0.15 ft² leakage)
- Construction leakage (0.05 ft² estimated)
- Design pressure: 0.10 in. w.c. to corridor, 0.05 in. w.c. to stair

$$Q_{supply} = (0.15 \times 2610 \times \sqrt{0.10}) + (0.15 \times 2610 \times \sqrt{0.05}) + (0.05 \times 2610 \times \sqrt{0.10})$$
$$Q_{supply} = 124 + 88 + 41 = 253 \text{ cfm (all doors closed)}$$

### Open Door Flow

When doors open during refuge area use:

$$Q_{open\_door} = C_d \times A_{open} \times 4005 \times \sqrt{\Delta P}$$

Where:
- $Q_{open\_door}$ = flow through open doorway (cfm)
- $C_d$ = discharge coefficient (0.65 typical)
- $A_{open}$ = open door area (ft², typically 21 ft² for 3' × 7' door)
- $\Delta P$ = pressure differential (in. w.c.)

For single door open at 0.10 in. w.c.:

$$Q_{open\_door} = 0.65 \times 21 \times 4005 \times \sqrt{0.10} = 17,300 \text{ cfm}$$

This flow rate 68 times larger than closed-door leakage. Supply system must maintain adequate airflow with design number of doors open (typically one door).

### Supply System Configurations

**Dedicated Supply Fan**:
- Independent fan serving refuge area only
- Located in protected space or remote location
- Sized for maximum required airflow
- Variable speed control responding to pressure differential

**Shared Supply with Zone Dampers**:
- Common supply fan serving multiple refuge areas
- Zone dampers control airflow to each area
- Pressure-independent dampers maintain setpoint
- Central monitoring of all zones

**Integration with Stairwell Pressurization**:
- Refuge areas adjacent to stairs share pressurization air
- Transfer grilles or relief dampers allow airflow from stair to refuge area
- Simpler system but less independent control
- Requires coordinated pressure analysis

### Makeup Air Sources

Air supplied to refuge area originates from:

**100% Outdoor Air**: Dedicated outdoor air intake:
- Ensures fresh, smoke-free air supply
- Located to avoid smoke contamination
- Protected from wind effects
- Provides guaranteed air quality

**Filtered Recirculated Air**: Return air from non-fire floors:
- Requires smoke detection to prevent smoke recirculation
- Automatic dampers isolate contaminated zones
- HEPA filtration for smoke particle removal
- Cost effective but requires careful controls

**Transfer from Protected Zones**: Air from adjacent pressurized spaces:
- Stairwell pressurization air transfers to refuge area
- Reduced total airflow requirement
- Simplified system architecture
- Dependent on maintaining stair pressurization

## Elevator Lobbies as Refuge Areas

Protected elevator lobbies serve dual functions:
- Elevator smoke protection during normal firefighter access
- Refuge areas for occupants during emergencies

### Configuration Requirements

**Separation**: 1-hour fire-resistance-rated smoke barrier separating lobby from:
- Floor corridors and occupied spaces
- Elevator shafts (except at elevator doors)
- Other non-protected spaces

**Access**: Direct access from:
- Floor corridors through self-closing smoke barrier doors
- Exit stairs through self-closing doors
- Minimum two means of egress from lobby

**Size**: Adequate for:
- Elevator service to floor
- Refuge area occupants (minimum two wheelchairs)
- Firefighting operations staging
- Typical size: 150-300 ft² depending on building size

### Pressurization Design

Three-zone pressurization system typical:

**Zone 1 - Exit Stair** (highest pressure):
- Design pressure: 0.20-0.25 in. w.c. relative to fire floor
- Primary protected egress path
- Independent pressurization system

**Zone 2 - Elevator Lobby** (intermediate pressure):
- Design pressure: 0.10-0.15 in. w.c. relative to fire floor
- Refuge area and firefighter staging
- Dedicated or shared pressurization

**Zone 3 - Floor Corridor** (fire floor, lowest pressure):
- Reference pressure (0.00 in. w.c.)
- May have negative pressure if smoke exhaust employed
- Contains fire and smoke

**Differential Across Boundaries**:
- Stair to lobby: 0.05-0.10 in. w.c.
- Lobby to corridor: 0.10-0.15 in. w.c.
- Stair to corridor: 0.15-0.25 in. w.c. (sum of above)

### Door Opening Force Management

Pressure staging reduces door opening forces:

**Single Barrier**: Stair door opens directly to fire floor:
- Full pressure differential across single door
- At 0.25 in. w.c., door opening force ~50 lbf (exceeds 30 lbf limit)
- Requires pressure limitation or force-reduction measures

**Pressure Staging through Lobby**: Two doors in series:
- Stair to lobby door: 0.10 in. w.c. differential, ~20 lbf opening force
- Lobby to corridor door: 0.15 in. w.c. differential, ~30 lbf opening force
- Each door within code limits
- Enables higher total protection level

### Integration with Elevator Operations

**Normal Operations**: Elevator recall on fire alarm:
- Elevators recalled to designated landing
- Lobby maintains normal environment
- Pressurization system may activate proactively

**Fire Service Operations**: Firefighter elevator use:
- Lobby pressurized to exclude smoke
- Adequate airflow to accommodate firefighter door traffic
- Communication system to fire command center
- Emergency lighting and signage

**Refuge Function**: Occupants use lobby as safe haven:
- Pressurization maintains smoke-free environment
- Two-way communication enables status updates
- Clear space for wheelchairs and occupants
- Visual confirmation of protected status

## Ventilation and Air Quality

### Minimum Ventilation Rates

Refuge areas require adequate outdoor air for occupants:

**ASHRAE 62.1 Basis**: Minimum outdoor air per person:
- Standard occupancy: 5-7.5 cfm/person
- Refuge area with potential stress: 15-20 cfm/person recommended

**Occupant Load Calculation**:
- Design occupancy: maximum anticipated refuge area use
- Mobility-impaired positions: minimum two
- Additional occupants: based on area size and accessibility
- Typical design: 10-30 occupants

**Example**: 20-person refuge area at 15 cfm/person:
$$Q_{ventilation} = 20 \times 15 = 300 \text{ cfm}$$

This ventilation requirement typically smaller than pressurization airflow requirement.

### Thermal Control

Maintaining acceptable temperatures in refuge areas:

**Heat Gain Sources**:
- Solar radiation through exterior walls/windows
- Heat transfer from fire floor (if adjacent)
- Occupant metabolic heat (250-300 Btu/hr per person)
- Lighting and equipment

**Temperature Control Strategies**:
- Tempered supply air (55-65°F) to offset heat gains
- Radiant cooling for perimeter heat gains
- Thermal insulation in smoke barrier construction
- Emergency cooling capacity in extreme conditions

**Design Criteria**:
- Maximum temperature: 95°F for 30-minute duration
- Preferred range: 65-85°F for occupant comfort
- Account for reduced air change rates during emergency
- Coordinate with fire scenario temperature analysis

### Air Quality Monitoring

**Oxygen Concentration**: Ensure adequate oxygen for respiration:
- Minimum: 19.5% O₂ (OSHA standard)
- Normal atmosphere: 21% O₂
- Outdoor air ventilation maintains acceptable levels
- Monitor in sealed refuge areas with long duration occupancy

**CO₂ Concentration**: Indicator of ventilation adequacy:
- Maximum: 5,000 ppm for emergency conditions
- Preferred: < 1,000 ppm for extended occupancy
- Ventilation rate prevents excessive accumulation

**Smoke Detection**: Continuous smoke monitoring:
- Photoelectric or ionization detectors
- Alarm on smoke detection indicating system failure
- Automatic control response to increase pressurization
- Visual and audible alarms in refuge area

## Control and Monitoring Systems

### Activation Sequences

**Automatic Activation**: Smoke control system activation triggers refuge area pressurization:
1. Fire alarm receives smoke detector signal
2. System identifies fire floor and zone
3. Refuge area pressurization activates on fire floor
4. Adjacent floor refuge areas may activate (design dependent)
5. Monitoring system confirms target pressures achieved

**Manual Activation**: Fire command center override:
- Operator selects specific refuge areas to pressurize
- Independent of automatic smoke detection
- Allows response to non-fire emergencies
- Requires trained personnel

### Pressure Monitoring

**Sensor Locations**:
- Differential pressure across each smoke barrier door
- Reference to fire floor corridor
- Reference to adjacent protected spaces (stairs)
- Multiple sensors in large refuge areas

**Monitoring Parameters**:
- Real-time pressure differential display
- Trend logging for forensic analysis
- Alarm on out-of-range conditions
- Integration with building management system

**Control Response**:
- Modulate supply fan speed to maintain target pressure
- Adjust relief dampers to prevent over-pressurization
- Alarm on inability to achieve target pressures
- Automatic switchover to backup systems if available

### Communication Systems

**Two-Way Communication**: Direct connection to fire command center:
- Voice communication (intercom or telephone)
- Visual indicators showing communication status
- Located at wheelchair accessible height
- Clearly marked and illuminated

**Mass Notification**: Broadcast system in refuge area:
- Emergency voice/alarm communication system
- Instructions to occupants
- Status updates from incident commander
- Coordination with building-wide emergency communication

**Visual Displays**: Information for occupants:
- Illuminated signs identifying refuge area
- Pressure status indicators (optional)
- Exit route confirmation
- Instructions for refuge area use

## Design Integration Challenges

### Multi-Floor Coordination

Tall buildings with refuge areas on each floor:

**Simultaneous Activation**: Fire scenarios may affect multiple floors:
- Vertical fire spread to adjacent floors
- Smoke migration through shafts
- Multiple refuge areas activate simultaneously
- System capacity for worst-case scenario

**Phased Evacuation**: Building evacuation strategy affects refuge area use:
- Fire floor and adjacent floors evacuate first
- Other floors shelter in place or use refuge areas
- System must support varying occupancy patterns

### Interaction with Building HVAC

Refuge area pressurization coordinates with normal HVAC:

**Dual-Purpose Equipment**: HVAC equipment serves normal and emergency functions:
- Normal mode: ventilation and conditioning
- Emergency mode: smoke control and pressurization
- Sizing for larger of two requirements
- Control system mode switching

**Ductwork Sharing**: Supply ductwork serves both functions:
- Normal HVAC distribution to occupied spaces
- Emergency pressurization air to refuge areas
- Smoke dampers ensure proper isolation
- Leakage requirements differ between modes

### Maintenance and Testing

**Periodic Testing**: Regular verification of system performance:
- Quarterly functional test of pressurization system
- Annual pressure differential testing
- Door opening force verification
- Communication system testing

**Maintenance Access**: Refuge area equipment requires service access:
- Fans, dampers, and controls in protected locations
- Accessible without compromising protection
- Adequate clearances for maintenance
- Spare parts stocking for critical components

**Training**: Building staff and occupants require training:
- Refuge area location and use
- Communication system operation
- Emergency procedures specific to refuge areas
- Coordination with fire department operations

Refuge areas provide critical life safety functions in tall buildings where immediate evacuation may not be possible for all occupants. Proper pressurization design, adequate air supply, and reliable control systems ensure these spaces maintain tenable conditions during fire emergencies. Integration with overall smoke control systems, compliance with code requirements, and comprehensive commissioning create dependable safe havens when needed most.
