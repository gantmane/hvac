---
title: "Smoke Control Systems for Tall Buildings"
description: "Smoke zones and barriers, pressurization and exhaust systems, NFPA 92 compliance, stair pressurization, and integrated smoke management design."
date: "2026-01-04"
weight: 7
tags: ["smoke control", "NFPA 92", "pressurization", "smoke exhaust", "life safety", "fire protection"]
categories: ["Specialty Applications"]
---

## Smoke Control Fundamentals

Smoke control systems manage smoke movement during fire emergencies to maintain tenable egress conditions. In tall buildings, smoke control must overcome stack effect, wind pressures, and vertical smoke migration through shafts while enabling safe evacuation and firefighter access.

Smoke movement follows pressure gradients. Pressure differential required to prevent smoke migration:

$$\Delta P_{min} = K \times \rho \times g \times h \times \Delta T / T_{avg}$$

Where:
- $\Delta P_{min}$ = minimum pressure differential (in. w.c.)
- $K$ = constant (0.052 for standard units)
- $\rho$ = air density (lbm/ft³)
- $g$ = gravitational acceleration (32.2 ft/s²)
- $h$ = height of opening (ft)
- $\Delta T$ = temperature difference (°F)
- $T_{avg}$ = average absolute temperature (°R)

For 8-foot door opening with 200°F temperature rise (fire floor to protected space):

$$\Delta P_{min} = 0.052 \times 0.075 \times 32.2 \times 8 \times 200 / 530 = 0.05 \text{ in. w.c.}$$

This represents theoretical minimum. NFPA 92 requires higher design values accounting for wind, stack effect, and system uncertainties.

## Smoke Zones and Barriers

### Zoning Strategies

Buildings divided into smoke control zones separated by smoke barriers:

**Floor-by-Floor Zoning**: Each floor constitutes separate smoke zone. Smoke control activates on fire floor only. Adjacent floors may be included in smoke zone. Simplest approach, applicable to most buildings.

**Tenant Separation Zoning**: Large floors divided into multiple zones. Separated by smoke barriers at tenant demising walls. Allows partial-floor smoke control. Appropriate for floors exceeding 20,000 ft².

**Vertical Zoning**: Groups of floors form vertical zones. Mechanical systems serve zone collectively. Smoke control operates on multiple-floor basis. Used with mechanical floor zoning strategy.

**Atrium Zoning**: Special provisions for multi-story atriums. Atrium forms separate smoke zone. Surrounding spaces protected from atrium smoke. Requires dedicated smoke exhaust system.

### Smoke Barrier Requirements

**Construction**: Smoke barriers constructed to limit smoke passage:
- 1-hour fire-resistance-rated construction (minimum)
- Sealed penetrations with smoke-rated dampers
- Gasketed or smoke-sealed doors
- Continuous from deck to deck (including above ceiling spaces)

**Leakage Area**: Smoke barrier leakage affects system sizing:
- Leakage area per IBC: approximately 0.15 ft² per door opening
- Construction leakage: 5-15% of door leakage
- Total leakage determines airflow required for pressurization

**Doors**: Doors in smoke barriers require:
- Self-closing or automatic-closing mechanisms
- Positive latching hardware
- Gasketing or sealing appropriate for smoke resistance
- Maximum opening force: 30 lbf (pressurization system constraint)

## Pressurization Systems

Pressurization systems supply outdoor air to create positive pressure in protected zones relative to fire zones.

### Design Pressure Differentials

NFPA 92 establishes pressure criteria:

**Minimum Pressure**: 0.05 in. w.c. (25 Pa) across smoke barrier. Sufficient to prevent smoke migration through sealed barriers. Accounts for neutral-plane shift during fire conditions.

**Design Pressure**: 0.10 in. w.c. (50 Pa) typical design target. Provides margin above minimum. Accommodates door leakage and system variations.

**Maximum Pressure**: 0.35 in. w.c. (175 Pa) to limit door opening forces. May be reduced where door forces verified by testing.

### Airflow Calculation

Required supply airflow equals leakage through all smoke barrier openings at design pressure:

$$Q_{supply} = \sum A_i \times 2610 \times \sqrt{\Delta P_i}$$

Where:
- $Q_{supply}$ = total supply airflow (cfm)
- $A_i$ = leakage area of opening i (ft²)
- $\Delta P_i$ = pressure differential across opening i (in. w.c.)

For floor with:
- 6 corridor doors (0.15 ft² leakage each)
- 2 stair doors (0.15 ft² each)
- Construction leakage (0.10 ft² total)
- Design pressure: 0.10 in. w.c.

$$Q_{supply} = (6 + 2 + 0.67) \times 0.15 \times 2610 \times \sqrt{0.10} = 5,100 \text{ cfm}$$

This represents all-doors-closed scenario. Open door flow significantly higher.

### Stack Effect Integration

Stack effect adds to or subtracts from mechanical pressurization:

**Winter (Upward Stack Effect)**:
- Lower floors: stack effect creates negative pressure
- Pressurization system must overcome stack effect plus provide design differential
- Upper floors: stack effect creates positive pressure
- Risk of over-pressurization; relief required

**Summer (Downward Stack Effect)**:
- Upper floors: stack effect creates negative pressure
- Increased pressurization required at upper floors
- Lower floors: stack effect assists pressurization
- More uniform pressure distribution than winter

**Design Approach**:
- Calculate stack effect for design fire temperature profile
- Size system for worst-case floor (highest required airflow)
- Provide pressure relief at floors with excess pressure
- Design for winter conditions (typically worst-case)

### Wind Effect Integration

Wind creates external pressure variations affecting smoke control:

**Windward Surfaces**: Positive external pressure opposes interior pressurization. Increased supply airflow required.

**Leeward Surfaces**: Negative external pressure assists interior pressurization. Risk of over-pressurization.

**Design Strategy**:
- Calculate wind pressures at design wind speed (typically 25-35 mph for smoke control)
- Design for worst-case wind direction (greatest opposing pressure)
- Provide adequate system capacity margin (20-30%)
- Consider multiple wind scenarios in performance-based designs

## Exhaust Systems

Smoke exhaust systems remove smoke from fire zones, creating negative pressure to contain smoke.

### Exhaust Airflow Sizing

**Zone Exhaust Method**: Exhaust air from fire floor at rate preventing smoke spread:

$$Q_{exhaust} = V_{zone} \times ACH$$

Where:
- $Q_{exhaust}$ = exhaust airflow (cfm)
- $V_{zone}$ = zone volume (ft³)
- $ACH$ = air change rate (4-10 ACH typical for smoke exhaust)

For 20,000 ft² floor with 9-foot ceiling at 6 ACH:

$$Q_{exhaust} = 20,000 \times 9 \times 6 = 1,080,000 \text{ cfm}$$

This high rate requires large exhaust fans and ductwork.

**Makeup Air**: Exhaust systems require makeup air:
- Supplied through building HVAC system
- Dedicated smoke control makeup air units
- Transfer from adjacent zones through smoke barriers
- Combination of sources

Makeup air rate equals exhaust rate minus designed leakage from surrounding zones.

### Dedicated Smoke Exhaust

**Smoke Shaft Exhaust**: Dedicated vertical shafts for smoke removal:
- Shaft penetrates fire floor(s)
- Smoke enters through automatic or manual dampers
- Roof-mounted exhaust fan draws smoke up shaft
- Discharges away from air intakes and occupied areas

**Sizing Example**: Shaft serving 40-story building
- Design exhaust rate: 50,000 cfm (reduced rate for shaft method)
- Shaft velocity: 2000-3000 fpm maximum (noise and pressure drop)
- Required shaft area: 50,000/2500 = 20 ft²
- Typical shaft: 4 ft × 5 ft

**Damper Configuration**: Smoke dampers at each floor:
- Normally closed dampers
- Open on fire floor (automatic or manual)
- Remain closed on non-fire floors
- Rated for elevated temperatures (250-350°F)

### Return/Exhaust Air System Utilization

Existing HVAC return/exhaust systems modified for smoke control:

**Configuration**:
- Fire floor: maximize exhaust airflow
- Adjacent floors: shut down supply air, operate exhaust
- Remote floors: maintain normal operation or shut down

**Limitations**:
- HVAC ductwork may not be rated for smoke exhaust service
- Return air ductwork often undersized for required exhaust rates
- Fire dampers in ductwork may close, blocking exhaust path
- Smoke contamination of return air system

**Enhancements**:
- Provide smoke dampers instead of fire dampers on fire floor return
- Dedicated smoke exhaust ductwork parallel to return system
- Upgrade return fan for higher capacity operation
- Ensure ductwork continuous and rated for smoke service

## Stairwell Pressurization Integration

Stairwell pressurization coordinates with overall building smoke control:

### Pressure Relationships

**Hierarchy**:
- Stairwell: highest pressure (safe egress path)
- Adjacent protected zones: intermediate pressure
- Fire floor: lowest pressure (smoke containment)

**Typical Differentials**:
- Stairwell to adjacent space: 0.10-0.15 in. w.c.
- Protected zone to fire floor: 0.05-0.10 in. w.c.
- Total stair to fire floor: 0.15-0.25 in. w.c.

### System Coordination

**Supply Air Coordination**: Stairwell and zone pressurization systems operate simultaneously:
- Independent systems: separate fans for stairs and zones
- Integrated systems: common fan with zone dampers
- Control sequence ensures pressure hierarchy maintained

**Door Opening Dynamics**: Opening stair door from fire floor affects both systems:
- Airflow from stair to fire floor
- Pressure drop in stairwell
- Pressure increase on fire floor
- Both systems must maintain minimum differentials

### Elevator Lobby Pressurization

Protected elevator lobbies require pressurization:

**Three-Zone System**:
1. Stairwell (highest pressure)
2. Elevator lobby (intermediate)
3. Fire floor (lowest)

**Pressure Staging**:
- Stair to lobby: 0.05-0.10 in. w.c.
- Lobby to fire floor: 0.05-0.10 in. w.c.
- Lobby serves as airlock between stair and fire floor

**Supply Air Delivery**: Dedicated supply to lobby or transfer from stairwell:
- Dedicated supply: independent control, higher cost
- Transfer from stair: simple, but affects stair pressure
- Design for worst-case door opening scenarios

## Control Sequences

### Manual vs. Automatic Operation

**Manual Operation**: Building operator activates smoke control from fire command center:
- Operator selects fire floor
- System configures for selected scenario
- Allows override of automatic sequences
- Required training and procedures

**Automatic Operation**: Smoke control activates automatically on detection:
- Smoke detectors on each floor identify fire location
- System activates appropriate zone configuration
- Stairwell pressurization activates
- HVAC systems configured for smoke control mode

**Combination Approach**: Automatic activation with manual override capability (most common).

### Sequence of Operation

Typical automatic sequence:

1. **Fire Alarm Activation**: Smoke detector or manual pull station activates on fire floor.

2. **System Configuration**:
   - Stairwell pressurization fans start
   - Fire floor exhaust activates (if provided)
   - Fire floor supply air shuts down
   - Adjacent floor supply air shuts down (optional)
   - Non-fire floor HVAC continues or shuts down per design

3. **Pressurization Establishment**:
   - Supply fans ramp to design airflow
   - Pressure monitoring verifies target pressures achieved
   - Relief dampers modulate to prevent over-pressurization

4. **Ongoing Operation**:
   - System maintains pressure differentials
   - Responds to door openings with increased airflow
   - Monitors for system faults and alarms
   - Continues until manual reset

### Feedback Control

Advanced systems use pressure feedback:

**Pressure Monitoring**:
- Differential pressure sensors at critical boundaries
- Stairwell sensors on multiple floors
- Fire floor to adjacent space pressure
- Elevator lobby pressures

**Fan Speed Modulation**:
- Variable frequency drives (VFDs) on supply fans
- Fan speed adjusts to maintain target pressures
- Compensates for varying door positions
- Adapts to stack effect and wind variations

**Relief Damper Control**:
- Motorized relief dampers instead of barometric
- Modulate based on pressure feedback
- Prevent over-pressurization more precisely
- Coordinate with supply fan control

## NFPA 92 Compliance

### Design Documentation

NFPA 92 requires comprehensive documentation:

**Narrative Description**: System objectives, design basis, operating sequences. Smoke control zones and boundaries. Coordination with other fire protection systems.

**Calculations**: Pressure differential calculations at all smoke boundaries. Airflow calculations for supply and exhaust systems. Stack effect analysis at design conditions. Wind effect analysis.

**Drawings**: Smoke control zone boundaries. Equipment locations and ductwork layout. Control sequences and wiring diagrams. Sensor and damper locations.

### Performance Acceptance Testing

Required testing before occupancy:

**Functional Testing**:
- Activate system in all design fire scenarios
- Verify all components operate per sequence
- Confirm interlocks with fire alarm and HVAC

**Pressure Testing**:
- Measure pressure differentials at all smoke barriers
- Verify minimum pressures achieved with doors closed
- Test pressure with design number of doors open
- Verify maximum pressures not exceeded

**Door Force Testing**:
- Measure opening forces at all stair and barrier doors
- Confirm forces below 30 lbf code limit
- Document forces for ongoing maintenance reference

**Airflow Testing**:
- Measure supply airflow rates
- Verify exhaust airflow if provided
- Check makeup air sources adequate

### Periodic Retesting

Ongoing testing requirements:

- Annual functional testing of all components
- Pressure differential verification
- Door force re-measurement
- System response time verification
- Documentation of test results and any deficiencies

## Design Challenges in Tall Buildings

### Cumulative Stack Effect

Tall buildings experience severe stack effect affecting smoke control:

**Winter Stack Effect**:
- Upper floors develop positive pressure
- Smoke buoyancy plus stack effect creates upward flow
- Stairwell pressurization must overcome combined effects
- Lower floors easier to pressurize (stack effect opposes smoke buoyancy)

**Design Response**:
- Compartmentalize vertical shafts to limit stack effect
- Size stairwell systems for worst-case upper floor conditions
- Provide adequate relief at lower floors to prevent over-pressurization
- Consider multiple supply injection points for pressure uniformity

### Multiple Smoke Zones

Tall buildings typically contain numerous smoke zones:

**Coordination Requirements**:
- Each zone requires independent or shared pressurization capability
- Control system must manage multiple simultaneous fire scenarios
- Makeup air for one zone may affect pressure in adjacent zones
- Complexity increases with number of zones

**System Architectures**:
- Independent systems per zone: maximum reliability, highest cost
- Shared supply with zone dampers: cost effective, single-point failure risk
- Combination approach: critical zones independent, others shared

### Integration with Occupied HVAC

Smoke control must coordinate with normal HVAC:

**Equipment Sharing**: HVAC equipment serves dual purpose:
- Normal mode: heating, cooling, ventilation
- Smoke control mode: pressurization, exhaust
- Equipment sized for larger of two requirements
- Controls ensure proper mode selection

**Ductwork Coordination**: Smoke control and HVAC ductwork overlap:
- Return air ductwork may serve as smoke exhaust
- Supply ductwork provides pressurization makeup air
- Fire/smoke dampers ensure proper compartmentation
- Sealing and leakage requirements differ between modes

### Firefighting Operations

Smoke control must support firefighter access:

**Stairwell Access**: Pressurized stairs provide safe firefighter access route. System maintains tenable conditions during ascent. Adequate airflow with doors open on multiple floors.

**Elevator Access**: Fire service elevators require smoke-free lobbies. Lobby pressurization independent of building system. Coordinate with elevator recall and firefighter operation.

**Fire Floor Operations**: Firefighters may ventilate fire floor manually. Smoke control system must adapt to changing conditions. Manual override capability essential.

Smoke control in tall buildings represents complex integration of building systems, code requirements, and fire safety objectives. Proper design accounts for stack effect, wind loads, and vertical smoke migration while providing reliable operation during the extreme conditions of fire emergencies. Success requires detailed analysis, comprehensive documentation, and thorough commissioning to ensure life safety performance when needed.
