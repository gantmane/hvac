---
title: "Stairwell Pressurization (Smoke Control)"
description: "Positive pressure stairwell systems, NFPA 92 requirements, pressure differential targets, supply fan sizing, and door opening force analysis."
date: "2026-01-04"
weight: 4
tags: ["stairwell pressurization", "smoke control", "NFPA 92", "door opening forces", "life safety"]
categories: ["Specialty Applications"]
---

## System Purpose and Operation

Stairwell pressurization systems create positive air pressure within exit stairs relative to building spaces, preventing smoke infiltration during fire emergencies. These systems enable safe egress by maintaining tenable conditions in stairwells while the building evacuates and firefighters ascend to the fire floor.

The pressurization system operates by supplying outdoor air to the stairwell at a rate exceeding all leakage paths. When stair doors remain closed, pressure builds to design level. As doors open during egress, airflow through openings prevents smoke entry while maintaining adequate pressure differential for doors that remain closed.

## NFPA 92 Requirements

NFPA 92 (Standard for Smoke Control Systems) establishes design criteria for stairwell pressurization:

### Minimum Pressure Differentials

**All Doors Closed**: Minimum 0.10 in. w.c. across stair doors. This pressure must be maintained with all stair doors closed under design conditions. Accounts for stack effect, wind, and HVAC system operation.

**Design Door Opening**: System must maintain minimum pressure with design number of doors open. Typical design scenario: doors open on fire floor and discharge level. Some jurisdictions require analysis with doors open on two adjacent floors plus discharge.

**Maximum Pressure Differential**: Maximum 0.35 in. w.c. with all doors closed. Ensures door opening forces remain below code limits. Excessive pressure prevents door opening or causes operator damage.

### Door Opening Forces

International Building Code (IBC) limits door opening forces:

- Maximum force: 30 lbf for interior doors
- Maximum force: 15 lbf for exterior doors in accessible routes
- Force measured at latch side of door, 48 inches above floor

Pressure differential directly affects opening force:

$$F_{total} = F_{latch} + F_{closer} + F_{pressure}$$

Where:
- $F_{total}$ = total opening force (lbf)
- $F_{latch}$ = latch mechanism resistance (typically 5-10 lbf)
- $F_{closer}$ = door closer resistance (5-15 lbf depending on adjustment)
- $F_{pressure}$ = force from pressure differential

For a 3-foot wide by 7-foot high door at 0.35 in. w.c.:

$$F_{pressure} = \Delta P \times A_{door} = (0.35/27.7) \times (3 \times 7) \times 144 = 38 \text{ lbf}$$

This pressure force alone exceeds the 30 lbf code limit, demonstrating why maximum pressure must be limited to 0.35 in. w.c. or less.

### Stack Effect Consideration

NFPA 92 requires analysis of stack effect interaction with pressurization system:

**Additive Stack Effect**: Winter conditions create upward stack effect. Building pressure increases with height. Stairwell pressurization adds to stack effect at upper floors. Upper floors may exceed maximum pressure limit.

**Subtractive Stack Effect**: Stack effect subtracts from pressurization at lower floors. Lower floors may fall below minimum pressure requirement. System must provide adequate pressure margin to overcome stack effect reduction.

**Design Approach**: Calculate stack effect for design outdoor temperature. Size supply system to maintain minimum pressure at worst-case floor. Install pressure relief or modulation to prevent excessive pressure at best-case floor.

## Pressure Differential Targets

Establishing appropriate pressure targets balances competing requirements:

| System Condition | Minimum Pressure | Target Pressure | Maximum Pressure |
|------------------|------------------|-----------------|------------------|
| All doors closed | 0.10 in. w.c. | 0.15-0.25 in. w.c. | 0.35 in. w.c. |
| Design doors open | 0.05 in. w.c. | 0.10-0.15 in. w.c. | N/A |
| Single door open | 0.08 in. w.c. | 0.12-0.18 in. w.c. | 0.30 in. w.c. |

### Floor-by-Floor Variation

Pressure differential varies by floor due to:

1. **Stack Effect**: Adds approximately 0.005 in. w.c. per floor in winter (70°F indoor, 0°F outdoor). For a 40-story building: 0.20 in. w.c. variation from bottom to top. System design must accommodate this variation.

2. **Leakage Distribution**: Floors with higher leakage (larger doors, more penetrations) experience lower pressure. Floors with minimal leakage experience higher pressure. Non-uniform pressure distribution requires balancing.

3. **Supply Air Distribution**: Air supplied at stairwell top creates pressure gradient. Pressure highest near supply point. Pressure decreases toward bottom due to cumulative leakage. Multiple injection points improve uniformity.

### Barometric Dampers

Barometric (pressure relief) dampers prevent excessive pressurization:

**Placement**: Install at each floor or at intervals (every 3-5 floors). Located in stairwell wall, discharging to building corridor or exterior. Sized to relieve excess airflow while maintaining minimum pressure.

**Operating Pressure**: Set to open at maximum design pressure (typically 0.28-0.32 in. w.c.). Prevents pressure from exceeding 0.35 in. w.c. limit. Accounts for damper opening characteristics and control tolerance.

**Sizing**: Relief damper area based on maximum relief flow:

$$A_{relief} = \frac{Q_{relief}}{V_{damper} \times C_{flow}}$$

Where:
- $A_{relief}$ = required damper free area (ft²)
- $Q_{relief}$ = relief airflow (cfm)
- $V_{damper}$ = air velocity through damper (typically 1000-1500 fpm)
- $C_{flow}$ = flow coefficient (0.6-0.7 for typical damper)

## Supply Fan Sizing

Stairwell pressurization fan capacity must overcome all leakage paths while maintaining design pressure.

### Leakage Path Calculation

**Door Leakage**: Primary leakage path in stairwell. Per NFPA 92, door leakage calculated using:

$$Q_{door} = A_{door} \times 2630 \times \sqrt{\Delta P}$$

Where:
- $Q_{door}$ = airflow through door (cfm)
- $A_{door}$ = effective leakage area (ft²)
- $\Delta P$ = pressure differential (in. w.c.)
- 2630 = constant for standard air

Effective leakage area depends on door construction:
- Standard commercial door: 0.15-0.35 ft² per door
- Weather-stripped door: 0.10-0.20 ft² per door
- Gasketed fire door: 0.05-0.15 ft² per door

For 20 floors with 2 doors per floor (stairwell and corridor), weather-stripped construction (0.15 ft² per door), at 0.20 in. w.c.:

$$Q_{doors} = 40 \times 0.15 \times 2630 \times \sqrt{0.20} = 7,050 \text{ cfm}$$

**Construction Leakage**: Includes leakage through:
- Wall penetrations for electrical, plumbing, HVAC
- Construction joints between walls and floor slabs
- Gaps around door frames
- Ventilation openings (if present)

Estimate at 10-25% of door leakage for typical construction. Add specific calculations for known large openings.

**Open Door Flow**: When doors open during egress, airflow increases dramatically:

$$Q_{open} = C_{flow} \times A_{open} \times 4005 \times \sqrt{\Delta P}$$

Where:
- $Q_{open}$ = flow through open doorway (cfm)
- $C_{flow}$ = flow coefficient (0.65 typical)
- $A_{open}$ = open door area (ft²)
- 4005 = constant for standard air

For 3-foot by 7-foot door opening at 0.10 in. w.c.:

$$Q_{open} = 0.65 \times 21 \times 4005 \times \sqrt{0.10} = 17,300 \text{ cfm per door}$$

### Fan Sizing Methodology

Total fan capacity equals sum of all simultaneous flows:

$$Q_{total} = Q_{doors\_closed} + Q_{doors\_open} + Q_{construction} + Q_{safety}$$

Where:
- $Q_{doors\_closed}$ = leakage through closed doors
- $Q_{doors\_open}$ = flow through design number of open doors
- $Q_{construction}$ = construction leakage
- $Q_{safety}$ = safety factor (typically 10-20%)

**Design Scenario 1**: All doors closed
- Provides maximum pressure (limited by relief dampers)
- Lowest airflow requirement
- Tests worst-case pressure differential

**Design Scenario 2**: Design doors open (typically 2 doors)
- Fire floor and discharge level doors open
- Most common design basis
- Balances flow capacity with pressure maintenance

**Design Scenario 3**: Multiple doors open (worst-case egress)
- Three or more doors open simultaneously
- Some jurisdictions require this scenario
- Maximum airflow requirement

Example calculation for 40-story stairwell:
- Doors closed: 7,050 cfm (from earlier calculation)
- Two doors open: 7,050 - (2 × 0.15 × 2630 × √0.10) + (2 × 17,300) = 41,250 cfm
- Construction leakage (15%): 6,190 cfm
- Safety factor (15%): 7,120 cfm
- **Total fan capacity: 54,560 cfm at 0.10 in. w.c. with two doors open**

### Static Pressure Requirements

Fan must overcome:
- Ductwork friction losses from outdoor intake to stairwell
- Supply air diffuser/grille pressure drop
- Velocity pressure at discharge points
- Margin for system effect and control

Typical static pressure: 2.0-4.0 in. w.c. depending on distribution system length and complexity.

## System Configurations

### Single Injection Point

Supply air introduced at single location (typically stairwell top):

**Advantages**:
- Simplest installation
- Minimal ductwork in stairwell
- Single supply grille or diffuser

**Disadvantages**:
- Vertical pressure gradient due to cumulative leakage
- May require excessive top-floor pressure to maintain bottom-floor minimum
- Less uniform pressure distribution

**Application**: Buildings under 20 stories with uniform leakage distribution.

### Multiple Injection Points

Supply air introduced at several floors:

**Advantages**:
- More uniform pressure distribution
- Reduced pressure variation from top to bottom
- Better performance with stack effect

**Disadvantages**:
- Complex ductwork installation in stairwell
- Multiple supply grilles to coordinate
- Higher installation cost

**Application**: Buildings over 20 stories or where pressure uniformity critical.

**Design Method**: Distribute airflow proportional to leakage area below each injection point. Bottom injection point supplies only its floor. Each higher injection supplies its floor plus all below.

### Vestibule Pressurization

Some designs pressurize vestibule between stairwell and corridor:

**Three-Zone System**:
- Zone 1: Stairwell (highest pressure)
- Zone 2: Vestibule (intermediate pressure)
- Zone 3: Corridor (lowest pressure/fire floor)

**Pressure Staging**:
- Stair to vestibule: 0.10-0.15 in. w.c.
- Vestibule to corridor: 0.05-0.10 in. w.c.
- Total (stair to corridor): 0.15-0.25 in. w.c.

**Advantages**:
- Reduces door opening force by staging pressure differential
- Provides additional smoke barrier
- Allows independent control of stair and vestibule pressure

**Disadvantages**:
- Requires separate supply systems or zone dampers
- More complex control system
- Additional monitoring points

## Control Strategies

### Constant Volume

Simplest control method: constant fan speed regardless of door position.

**Operation**:
- Fan operates at fixed airflow on fire alarm activation
- Barometric dampers relieve excess pressure
- No feedback control

**Advantages**:
- Simple, reliable operation
- No sensors or feedback loops
- Lowest installation cost

**Disadvantages**:
- Cannot adapt to varying conditions
- May over-pressurize with all doors closed
- May under-pressurize with multiple doors open
- Suboptimal for varying stack effect

### Pressure-Modulated

Fan speed varies to maintain target pressure differential:

**Operation**:
- Differential pressure sensors on multiple floors
- Fan speed modulates based on pressure feedback
- Variable frequency drive (VFD) controls fan
- Target pressure adjusted for worst-case sensor

**Advantages**:
- Maintains consistent pressure regardless of door position
- Adapts to stack effect variation
- Reduces energy consumption
- Optimal performance across conditions

**Disadvantages**:
- Complex control system
- Requires reliable pressure sensors
- VFD maintenance and failure modes
- Higher installation cost

**Control Algorithm**:
```
IF (minimum measured pressure < setpoint - deadband) THEN
    Increase fan speed
ELSE IF (maximum measured pressure > setpoint + deadband) THEN
    Decrease fan speed
ELSE
    Maintain current fan speed
END IF
```

### Door Position Feedback

Advanced systems respond to door position:

**Operation**:
- Door position switches on critical doors
- Fan airflow adjusted based on number of open doors
- Predictive response before pressure drops

**Advantages**:
- Rapid response to door opening
- Maintains pressure during door use
- Optimized energy consumption

**Disadvantages**:
- Requires door position monitoring
- Complex wiring and controls
- Maintenance of position switches

## Commissioning and Testing

### Pre-Functional Testing

Before occupancy:

1. **Leakage Area Verification**: Measure door leakage using fan pressurization. Compare to design assumptions. Adjust fan capacity if significant deviation.

2. **Ductwork Testing**: Verify ductwork leakage within tolerances. Test supply grille/diffuser airflow distribution. Confirm uniform air delivery.

3. **Control System Checkout**: Verify sensor calibration and accuracy. Test control algorithms under simulated conditions. Confirm proper fan response to pressure changes.

### Functional Performance Testing

With building systems operating:

1. **Pressure Differential Testing**:
   - Measure pressure at each floor with all doors closed
   - Verify minimum 0.10 in. w.c. at all locations
   - Verify maximum does not exceed 0.35 in. w.c. at any location
   - Test under range of outdoor temperatures (varying stack effect)

2. **Door Opening Force Testing**:
   - Measure opening force at each floor
   - Use calibrated force gauge at latch side, 48 inches above floor
   - Verify forces below 30 lbf
   - Test both opening and closing operations

3. **Dynamic Testing**:
   - Open design number of doors
   - Verify pressure maintained at remaining closed doors
   - Measure time to re-establish pressure after door closure
   - Test with varying door combinations

### Seasonal Testing

Stack effect varies with outdoor temperature:

**Winter Testing** (maximum stack effect):
- Conduct during coldest anticipated conditions
- Verify upper floors do not exceed maximum pressure
- Confirm lower floors maintain minimum pressure
- Adjust relief damper settings if necessary

**Summer Testing** (reverse stack effect):
- Test during warmest conditions
- Verify system performance with reduced or reverse stack effect
- Confirm adequate pressure at all floors

**Shoulder Season**: Test during moderate conditions to verify control system response to varying stack effect.

## Common Design Errors

### Undersized Fan Capacity

Failure to account for multiple simultaneous open doors. Results in:
- Inadequate pressure with doors open during egress
- Smoke infiltration potential
- Code violation during inspection

### Inadequate Pressure Relief

Insufficient relief damper capacity or improper settings. Results in:
- Excessive pressure with all doors closed
- Door opening forces exceeding code limits
- Potential door hardware damage

### Ignoring Stack Effect

Designing for single pressure setpoint without stack effect analysis. Results in:
- Over-pressurization at upper floors (winter)
- Under-pressurization at lower floors (winter)
- Inability to meet code requirements across building height

### Poor Sensor Placement

Pressure sensors located in non-representative positions. Results in:
- Control system responding to local anomalies
- Inadequate pressure at unmonitored locations
- Unreliable system performance

Stairwell pressurization represents a critical life safety system requiring careful design, installation, and commissioning. Proper fan sizing, pressure control, and integration with building stack effect ensures reliable smoke protection during fire emergencies while maintaining code-compliant door opening forces.
