---
title: "Pressure Differentials in Vertical Shafts"
description: "Elevator shaft, stairwell, and mechanical shaft pressure analysis, measurement methodology, and design considerations for tall buildings."
date: "2026-01-04"
weight: 2
tags: ["pressure differentials", "elevator shafts", "stairwells", "vertical shafts", "pressure measurement"]
categories: ["Specialty Applications"]
---

## Vertical Shaft Characteristics

Vertical shafts in tall buildings—elevators, stairs, mechanical chases, and plumbing stacks—function as continuous air columns subjected to stack effect, mechanical pressurization, and wind loads. These shafts experience cumulative pressure effects across their height, creating operational challenges for doors, dampers, and connected systems.

A sealed shaft extending 600 feet with interior temperature 70°F and exterior temperature 0°F develops theoretical pressure differential:

$$\Delta P_{shaft} = 7.64 \times 600 \times \left(\frac{1}{460} - \frac{1}{530}\right) = 1.40 \text{ in. w.c.}$$

This represents maximum differential between shaft bottom and top. Actual pressures depend on leakage distribution, connections to building spaces, and mechanical system operation.

## Elevator Shafts

Elevator shafts present unique pressure challenges due to:

- Large vertical extent (ground to roof)
- Moving elevator cars creating piston effect
- Door openings on multiple floors
- Ventilation and pressure relief requirements
- Fire service access requirements

### Pressure Distribution

Elevator shaft pressure distribution depends on shaft connectivity:

**Isolated Shaft**: Shaft sealed from building spaces except at door openings. Shaft experiences full stack effect pressure. Bottom of shaft: negative pressure relative to building. Top of shaft: positive pressure relative to building. Pressure differential across closed doors varies by floor.

**Connected Shaft**: Shaft connected to building through ventilation openings or leakage. Building pressurization affects shaft pressure. HVAC system operation modifies stack effect. Pressure differential reduced compared to isolated shaft.

**Pressurized Shaft**: Mechanical ventilation supplies air to shaft. Supply air rate determines pressurization level. Positive pressure relative to building on all floors. Used for smoke control in fire service elevators.

### Leakage Paths

Elevator shaft leakage occurs through:

1. **Door Clearances**: Gap around elevator car doors (typically 1/8 to 1/4 inch). Gap around hoistway doors. Total leakage area 0.5-1.5 ft² per door pair.

2. **Structural Penetrations**: Electrical conduit and cable penetrations. Guide rail brackets and supports. Ventilation openings and relief vents. Construction joints between shaft walls and floor slabs.

3. **Top and Bottom Openings**: Machine room openings at top. Pit ventilation at bottom. Pressure relief vents per ASME A17.1. Emergency access hatches.

### Pressure Measurement

Measuring elevator shaft pressure requires:

**Sensor Placement**: Install differential pressure sensors at representative floors. Minimum: bottom (2nd floor), mid-height, top (below machine room). Additional sensors every 10-15 floors in super-tall buildings. Reference pressure: adjacent building space or outdoor.

**Measurement Conditions**: Test with elevators stationary (static pressure). Test with elevators moving (dynamic pressure, piston effect). Test under various outdoor temperature conditions. Test with different HVAC system operating modes.

**Data Acquisition**: Continuous monitoring during occupied hours. Record maximum and minimum pressures. Correlate with outdoor temperature and wind. Identify patterns related to HVAC operation and occupancy.

## Stairwells

Stairwell shafts serve dual functions:

- Ordinary egress during normal building operation
- Protected egress during fire emergencies

Pressure characteristics affect both functions but design prioritizes fire emergency performance.

### Normal Operation

During normal operation, stairwells experience:

**Stack Effect Pressure**: Stairwell temperature typically lower than occupied spaces. Temperature difference creates additional stack effect within stair. Combined building and stair stack effect determines pressure distribution. Exterior stairs experience full outdoor temperature variation.

**Door Opening Forces**: Pressure differential across stair doors affects opening force. Excessive pressure (> 0.35 in. w.c.) creates unacceptable door forces. Insufficient pressure (< 0.05 in. w.c.) allows smoke infiltration during fires. Target range: 0.10-0.20 in. w.c. for normal operation.

**Ventilation**: Interior stairs require ventilation for odor control. Exterior stairs may receive outdoor air infiltration. Uncontrolled ventilation affects pressure distribution. Mechanical ventilation provides consistent air change rates.

### Emergency Operation (Fire)

Fire conditions require positive stairwell pressurization:

**Pressurization Objectives**:
- Prevent smoke migration into stair shaft
- Maintain tenable conditions for egress
- Provide firefighter access route
- Create pressure barrier between fire floor and stair

**Pressure Requirements** (NFPA 92):
- Minimum: 0.10 in. w.c. across closed doors
- Maximum: 0.35 in. w.c. to limit door opening forces
- Target: 0.15-0.25 in. w.c. for design conditions

**System Design Challenges**:
- Pressure varies with door position (open/closed)
- Stack effect adds to or subtracts from fan pressure
- Multiple open doors dramatically reduce pressure
- Wind effects modify exterior pressure reference

### Stairwell Pressure Measurement

Measuring stairwell pressure during commissioning:

1. **Static Testing**: All stair doors closed. Measure pressure floor-by-floor. Reference: adjacent building space. Verify minimum pressure on all floors.

2. **Dynamic Testing**: Open doors on fire floor. Measure pressure on floor above and below. Verify adequate pressure maintained. Test with multiple door scenarios.

3. **Door Force Testing**: Measure actual door opening force at each floor. Confirm forces below 30 lbf (IBC requirement). Identify floors requiring pressure adjustment.

4. **Stack Effect Variation**: Test under range of outdoor temperatures. Verify system performs at winter and summer design conditions. Adjust control algorithms based on temperature.

## Mechanical Shafts

Mechanical shafts house vertical distribution systems:

- Supply and return air ducts
- Hydronic piping risers
- Refrigerant piping
- Electrical and controls wiring

### Pressure Considerations

Mechanical shaft pressure affects:

**Fire Damper Operation**: Pressure differential across fire dampers determines closing force. Excessive pressure prevents proper damper closure. Damper leakage increases with pressure differential. Design pressure: typically < 4 in. w.c. for reliable damper operation.

**Smoke Damper Performance**: Smoke dampers rated for specific leakage at pressure differential. Class I: 20 cfm/ft² at 4 in. w.c. Class II: 10 cfm/ft² at 4 in. w.c. Class III: 4 cfm/ft² at 4 in. w.c. Higher leakage rates compromise smoke control.

**Shaft Integrity**: Pressure forces on shaft walls and doors. Positive pressure: outward force, potential for joint failure. Negative pressure: inward force, structural loading. Design for maximum anticipated pressure including wind and stack effect.

### Compartmentation Strategy

Effective mechanical shaft design requires:

**Vertical Segmentation**: Divide shaft into zones every 10-15 floors. Provide fire-rated separation between zones. Install fire/smoke dampers at zone boundaries. Limit vertical pressure accumulation.

**Horizontal Isolation**: Seal shaft from occupied spaces. Provide access doors only where required. Minimize penetrations through shaft walls. Seal all penetrations with approved firestop materials.

**Pressure Relief**: Install pressure relief dampers in over-pressurized shafts. Size relief for maximum anticipated airflow. Discharge to appropriate location (not into occupied space). Consider backdraft prevention for normally closed relief dampers.

## Pressure Measurement Methodology

### Instrumentation

**Differential Pressure Sensors**:
- Range: ±2.0 in. w.c. for most applications
- Accuracy: ±2% of reading or ±0.01 in. w.c., whichever is greater
- Response time: < 1 second for dynamic measurements
- Environmental rating: suitable for shaft conditions

**Reference Pressure**:
- Static pressure tap in adjacent building space
- Outdoor pressure tap on building facade
- Avoid air current effects on pressure tap location
- Multiple reference points for verification

### Measurement Technique

1. **Sensor Installation**: Mount sensor in non-turbulent location. Protect from water infiltration. Ensure free air circulation to sensing ports. Label sensor with location and reference point.

2. **Tubing Routing**: Use rigid tubing (copper or plastic) for pressure taps. Minimize tubing length (< 20 feet preferred). Slope tubing to prevent water accumulation. Avoid kinks and sharp bends.

3. **Calibration**: Zero sensor with equal pressure on both ports. Verify accuracy using precision manometer. Calibrate at multiple points across operating range. Re-calibrate annually or after significant maintenance.

4. **Data Recording**: Log pressure at 1-minute intervals minimum. Record corresponding outdoor temperature and wind speed. Note HVAC system operating status. Document door open/close events if monitored.

### Analysis Methods

**Pressure Profile Development**: Plot pressure vs. height for shaft. Compare measured to theoretical stack effect calculation. Identify anomalies indicating unexpected leakage or connections. Correlate pressure variation with outdoor temperature.

**Leakage Area Estimation**: Measure pressure differential across shaft height. Measure airflow through shaft (tracer gas or flow stations). Calculate effective leakage area using orifice equation:

$$Q = C_d A \sqrt{\frac{2 \Delta P}{\rho}}$$

Where:
- $Q$ = volumetric flow rate (cfm)
- $C_d$ = discharge coefficient (0.6-0.7 typical)
- $A$ = effective leakage area (ft²)
- $\Delta P$ = pressure differential (lbf/ft²)
- $\rho$ = air density (lbm/ft³)

**Performance Verification**: Compare measured pressures to design targets. Verify door opening forces calculated from measured pressures. Confirm smoke control system performance margins. Identify required adjustments to fan capacity or control strategies.

## Design Implications

### Shaft Pressurization Systems

Actively managing shaft pressure requires:

**Supply Air Systems**: Dedicated supply fans serving shaft. Variable speed control responding to pressure differential. Multiple injection points to distribute air vertically. Sized for worst-case stack effect condition.

**Relief Air Systems**: Pressure relief dampers or fans. Automatic opening based on pressure differential. Discharge to non-critical locations. Sized for maximum supply air rate plus stack effect.

**Control Integration**: Differential pressure sensors throughout shaft height. Building automation system monitoring and control. Coordination with HVAC system operation and fire alarm system. Automatic adjustment for outdoor temperature variation.

### Leakage Reduction

Minimizing shaft leakage improves pressure control:

- Specify gasketed or weather-stripped shaft doors
- Seal all penetrations with UL-listed firestop systems
- Design shaft construction with continuous air barriers
- Minimize required shaft openings and access points
- Test shaft leakage during construction (blower door testing)
- Verify firestop installation quality and completeness

### Multi-Shaft Coordination

Buildings with multiple vertical shafts require coordinated analysis:

- Model combined stack effect from all shafts
- Account for inter-shaft air movement through building spaces
- Design HVAC system for cumulative infiltration/exfiltration
- Coordinate smoke control between multiple stair and elevator shafts
- Analyze worst-case shaft combinations during fire scenarios

Vertical shaft pressure management represents a critical aspect of tall building HVAC design. Shafts extending hundreds of feet develop pressure differentials that affect door operation, smoke control, and overall building performance. Proper measurement, analysis, and control of these pressures ensures code compliance and reliable operation under all environmental conditions.
