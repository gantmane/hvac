---
title: "Smoke Dampers: UL 555S Requirements and Control Logic"
linkTitle: "Smoke Dampers"
weight: 2
date: 2026-01-04
description: "Comprehensive guide to smoke damper requirements per UL 555S and NFPA standards, including leakage classifications, control logic design, actuator specifications, smoke detector integration, and testing procedures for smoke management systems."
keywords: ["smoke dampers", "UL 555S", "smoke control", "leakage class", "smoke damper actuators", "smoke detector integration", "smoke barrier penetrations", "smoke management systems", "damper control logic"]
---

## Smoke Damper Fundamentals

Smoke dampers are active fire protection devices designed to restrict smoke passage through HVAC ductwork during fire events. Unlike fire dampers that primarily respond to heat through fusible links, smoke dampers receive electrical or pneumatic control signals from smoke detectors or fire alarm systems, closing before smoke significantly contaminates air distribution pathways.

### Primary Functions and Objectives

Smoke dampers serve critical life safety functions:

1. **Smoke compartmentation:** Maintain smoke barrier integrity by preventing smoke migration through ducts
2. **Egress protection:** Keep exit corridors and stairwells smoke-free for occupant evacuation
3. **Smoke control system operation:** Enable zoned smoke management by isolating fire areas
4. **Staging area protection:** Preserve areas of refuge in healthcare and high-rise buildings

**Fundamental operating principle:**

Smoke dampers remain open during normal HVAC operation, close rapidly upon smoke detection signal or fire alarm activation, and prevent smoke leakage while maintaining structural integrity during fire exposure.

## UL 555S Standard for Smoke Dampers

UL 555S, Standard for Smoke Dampers, establishes testing protocols and performance criteria that smoke dampers must meet for listing and code compliance. This standard complements UL 555 (fire dampers) but focuses on smoke leakage characteristics rather than fire resistance.

### Key Differences from UL 555 Fire Dampers

| Characteristic | UL 555 Fire Dampers | UL 555S Smoke Dampers |
|----------------|---------------------|----------------------|
| Primary function | Block flames and heat | Restrict smoke passage |
| Activation method | Fusible link (thermal) | Electrical/pneumatic signal |
| Testing focus | Fire resistance time | Air leakage rates |
| Temperature exposure | Standard fire curve | Ambient and elevated temp |
| Closure mechanism | Passive (gravity/spring) | Active (motorized actuator) |
| Power requirements | None | Electrical or pneumatic |

### Leakage Classifications

UL 555S defines smoke damper performance by leakage class, representing maximum allowable air leakage when closed under test pressure differential.

**Leakage class ratings:**

- **Class I:** 10 cfm/sq ft at 4.0 inches water gauge
- **Class II:** 40 cfm/sq ft at 4.0 inches water gauge
- **Class III:** 80 cfm/sq ft at 4.0 inches water gauge

**Leakage calculation for specific damper:**

$$Q_{leak,max} = L_{class} \times A_{damper}$$

Where:
- $Q_{leak,max}$ = Maximum allowable leakage (cfm)
- $L_{class}$ = Leakage class rating (cfm/sq ft)
- $A_{damper}$ = Damper free area (sq ft)

**Example calculation:**

For a 24" × 24" (4 sq ft) Class I smoke damper:

$$Q_{leak,max} = 10 \frac{\text{cfm}}{\text{sq ft}} \times 4 \text{ sq ft} = 40 \text{ cfm}$$

This damper may leak up to 40 cfm when closed under 4" w.g. pressure differential.

### Temperature Ratings

Smoke dampers receive temperature ratings indicating sustained operational capability:

**Ambient temperature rating:**
- Operating range: 0°F to 250°F
- Standard applications in conditioned spaces
- Most common rating for general HVAC

**Elevated temperature rating:**
- Continuous: Minimum 250°F
- Intermittent: Minimum 350°F for specified duration
- Required near boilers, high-temperature equipment, rooftop installations

**Temperature rating selection:**

$$T_{damper,rated} \geq T_{ambient,max} + 25°F$$

Where:
- $T_{damper,rated}$ = Required damper temperature rating (°F)
- $T_{ambient,max}$ = Maximum expected ambient temperature (°F)

### Velocity Ratings

UL 555S dampers receive velocity ratings representing maximum air velocity at which the damper can close and seal properly:

- **Low velocity:** 2,000 fpm
- **Medium velocity:** 2,500 fpm
- **High velocity:** 4,000 fpm

Higher velocity ratings require more robust actuators and reinforced blade construction.

## Smoke Damper Applications and Code Requirements

### Required Locations per Model Codes

International Building Code (IBC) and NFPA standards mandate smoke dampers at specific locations:

**Smoke barriers (IBC Section 709.5):**
- All duct penetrations through smoke barriers
- Required in Group I-2 (hospitals), I-1 (assisted living), I-3 (detention facilities)
- Maintain smoke compartment separation for defend-in-place strategies

**Corridors (IBC Section 710.5):**
- Air transfer openings in rated corridor walls
- Group I-2 occupancies and some Group I-1 applications
- Both supply and return/exhaust penetrations

**Smoke control systems (IBC Section 909):**
- Zone boundaries in engineered smoke control systems
- Stairwell pressurization systems
- Elevator pressurization systems
- Atrium smoke management

**Vertical shafts:**
- May require smoke dampers where ductwork exits shafts into habitable spaces
- Coordinate with fire damper requirements

### Engineered Smoke Control Systems

Dedicated smoke control systems use smoke dampers to create pressure differentials:

**Stairwell pressurization:**
- Supply dampers modulate to maintain 0.05" to 0.10" w.g. positive pressure
- Exhaust dampers in fire floor corridors remove smoke
- Control algorithm adjusts damper position based on pressure sensors

**Zoned smoke control:**
- Dampers isolate fire zone for smoke extraction
- Adjacent zones maintain normal or pressurized conditions
- Typical pressure differential: 0.05" to 0.15" w.g. across smoke barriers

**Pressure differential calculation:**

$$\Delta P = \frac{\rho V^2}{2g_c} + P_{static}$$

Where:
- $\Delta P$ = Total pressure differential across damper (in. w.g.)
- $\rho$ = Air density (lbm/cu ft)
- $V$ = Air velocity (fpm)
- $g_c$ = Gravitational constant (32.2 lbm-ft/lbf-sec²)
- $P_{static}$ = Static pressure differential (in. w.g.)

## Smoke Damper Construction and Types

### Blade Configurations

**Single-blade dampers:**
- One rotating or sliding blade
- Simplest construction and highest reliability
- Limited to smaller duct sizes (typically ≤24" diameter)
- Low pressure drop when open
- Fast closure time (typically 1-3 seconds)

**Multi-blade opposed-blade dampers:**
- Multiple blades rotating in opposite directions
- Better flow control and lower pressure drop
- Standard for rectangular ducts
- Even air distribution across opening
- Typical for dampers >36" in any dimension

**Multi-blade parallel-blade dampers:**
- All blades rotate in same direction
- Higher closure torque capability
- Suitable for high-velocity applications
- May create uneven flow distribution

### Actuator Types and Specifications

Smoke dampers require powered actuators to close against air pressure and maintain closed position.

**Electric actuators:**

- **Spring-return:** Spring closes damper; motor opens against spring tension
  - Power failure = damper closes (fail-safe)
  - Typical torque: 35-500 in-lbs
  - Run time: 15-90 seconds for 90° rotation

- **Non-spring-return:** Motor drives both directions
  - Requires battery backup for fail-safe operation
  - Higher available torque: 150-2,000 in-lbs
  - Faster operation: 10-60 seconds typical

**Pneumatic actuators:**
- Compressed air supply (typically 15-25 psi)
- Spring-return or double-acting
- Very fast operation (3-15 seconds)
- Requires backup air compressor for fail-safe

**Actuator torque calculation:**

$$T_{required} = A_{blade} \times P_{differential} \times L_{moment} \times SF$$

Where:
- $T_{required}$ = Required actuator torque (in-lbs)
- $A_{blade}$ = Total blade area (sq in)
- $P_{differential}$ = Maximum pressure differential (psi)
- $L_{moment}$ = Moment arm length from blade axis to center of pressure (inches)
- $SF$ = Safety factor (typically 1.25-1.5)

### Edge Seals and Gaskets

Achieving low leakage classifications requires effective sealing:

**Blade edge seals:**
- **Silicone gaskets:** Compressible seals on blade edges
- **Neoprene bulbs:** Inflatable seals activated when closed
- **Mechanical seals:** Metal-to-metal contact with precision machining

**Frame seals:**
- Gasket material around damper frame perimeter
- Must withstand elevated temperatures if rated damper
- Compression ensures tight seal when blades close

**Jamb seals:**
- Side seals between blade edges and damper frame
- Critical for low-leakage performance
- Must accommodate blade manufacturing tolerances

## Control Logic and Integration

### Basic Control Sequences

**Smoke detector activation sequence:**

1. Area smoke detector activates
2. Fire alarm control panel receives signal
3. Control panel sends close signal to smoke dampers
4. Dampers close within specified time (typically 15-60 seconds)
5. End switches confirm closed position
6. HVAC control system receives damper status
7. HVAC system responds per smoke control sequence

**Sequence of operation flowchart:**

```
Smoke Detected → Fire Alarm Panel → Smoke Damper Close Signal
                        ↓
                Position Confirmation
                        ↓
                BAS/HVAC System → Execute Smoke Control Strategy
```

### Fire Alarm System Integration

Smoke dampers interface with fire alarm systems per NFPA 72:

**Wiring requirements:**
- Dedicated control circuit from fire alarm panel
- Separate monitoring circuit for end switch status
- Circuit survivability per NFPA 72 (fire-rated cable or conduit)
- Emergency power backup (battery or generator)

**Control signals:**
- **Normally open (NO) contact:** Closes to activate damper
- **Normally closed (NC) contact:** Opens to activate damper (less common)
- **Voltage signal:** 24 VDC/VAC common; 120 VAC for larger actuators

**Position monitoring:**
- End switches (limit switches) confirm damper position
- **Closed position:** Proves damper sealed when required
- **Open position:** Confirms normal operation capability
- Supervisory signals to fire alarm panel

### Building Automation System Coordination

Integration with BAS enables sophisticated smoke control:

**Data points typically provided:**
- Damper position (open/closed/intermediate)
- Actuator fault conditions
- Manual override status
- Smoke detector status

**BAS control strategies:**

**Mode 1: Normal operation**
- All smoke dampers open
- HVAC operates normally
- Position monitoring active

**Mode 2: Fire alarm**
- Smoke dampers in fire zone close
- EXHAUST dampers in fire zone open (if smoke control system)
- Adjacent zone dampers modulate per pressure control
- Non-fire zones continue normal operation or shut down per design

**Mode 3: Manual firefighter control**
- Manual switches override automatic control
- Firefighter smoke control panel provides zone-by-zone control
- BAS monitors but does not override firefighter commands

### Pressure Control Logic for Smoke Management

Engineered smoke control systems use pressure-independent control:

**Pressure sensor locations:**
- Fire zone (reduced or negative pressure)
- Adjacent zones (normal or positive pressure)
- Egress routes (positive pressure relative to building)

**PID control algorithm:**

$$u(t) = K_p e(t) + K_i \int_0^t e(\tau)d\tau + K_d \frac{de(t)}{dt}$$

Where:
- $u(t)$ = Control signal to damper actuator
- $e(t)$ = Error between setpoint and measured pressure
- $K_p$ = Proportional gain
- $K_i$ = Integral gain
- $K_d$ = Derivative gain

**Typical tuning parameters for smoke control:**
- $K_p$ = 5-15 (aggressive response to pressure changes)
- $K_i$ = 0.5-2 (eliminate steady-state offset)
- $K_d$ = 0-1 (minimize oscillation)

## Installation Requirements

### Mounting and Clearances

Proper installation ensures UL 555S listing validity:

**Mounting orientation:**
- Verify damper rated for installation orientation (horizontal/vertical)
- Some dampers rated for any orientation
- Actuator position affects required clearances

**Clearance requirements:**

$$C_{actuator} \geq \text{stroke length} + 3"$$

Where:
- $C_{actuator}$ = Minimum clearance for actuator (inches)
- Stroke length = Full travel distance of actuator arm/linkage

**Access requirements:**
- 18" × 18" minimum access panel within 10 feet of damper
- Adequate working space for actuator removal and replacement
- Lighting in access areas

### Sleeve and Duct Connections

**Sleeve installation:**
- 22-gauge minimum galvanized steel
- Length = barrier thickness + 1" minimum extension each side
- Sealed to barrier per firestop system requirements

**Duct connections to damper:**
- Flexible connections NOT permitted within 6 feet of smoke damper
- Rigid duct connections required
- Support ducts independently (do not hang from damper frame)
- Maintain alignment to prevent blade binding

### Electrical and Pneumatic Connections

**Electrical wiring:**
- Size per actuator specifications and voltage drop calculations
- Typical: 18 AWG minimum for 24V circuits up to 100 feet
- Conduit required in plenums unless plenum-rated cable
- Label circuits at panel and at damper

**Pneumatic tubing:**
- 1/4" or 3/8" nylon or copper tubing typical
- Maximum run length per actuator specifications (typically 100-150 feet)
- Pressure regulators at branch circuits
- Air quality per actuator requirements (filtered, dried)

## Testing and Commissioning

### Initial Acceptance Testing

Commission smoke dampers before building occupancy:

**Pre-functional checklists:**

1. **Visual inspection:**
   - [ ] Correct damper size, type, and leakage class
   - [ ] Proper mounting orientation
   - [ ] Actuator correctly installed and wired
   - [ ] No damage from construction
   - [ ] Blade movement unrestricted
   - [ ] End switches properly adjusted

2. **Operational tests:**
   - [ ] Manual actuator operation (use actuator manual override)
   - [ ] Automatic operation from fire alarm panel
   - [ ] Confirm closure time meets specifications
   - [ ] Verify end switch signals at fire alarm panel
   - [ ] Test fail-safe operation (power interruption)
   - [ ] Check BAS integration and status points

3. **Functional performance testing:**

**Closure time measurement:**

$$t_{close} = t_{signal} - t_{confirmation}$$

Where:
- $t_{close}$ = Damper closure time (seconds)
- $t_{signal}$ = Time close command issued
- $t_{confirmation}$ = Time end switch confirms closed position

Typical requirements: 15-60 seconds maximum depending on application

### Periodic Testing Per NFPA 105

NFPA 105, Standard for Smoke Door Assemblies and Other Opening Protectives, establishes inspection requirements for smoke dampers:

**Testing frequency:**
- **Initial:** 1 year after installation
- **Subsequent:** Annually, or per manufacturer recommendations
- **After repairs:** Immediate retest of affected dampers

**Annual test procedure:**

1. **Notification:**
   - Inform building occupants and fire department
   - Schedule during off-hours if possible
   - Coordinate with facility operations staff

2. **Smoke detector test:**
   - Activate smoke detector serving damper
   - Verify damper receives close signal
   - Confirm damper closes within specified time
   - Check end switch indication at fire alarm panel

3. **Manual test:**
   - Use fire alarm panel manual control
   - Operate damper through full open/close cycle
   - Verify smooth operation without binding
   - Test both directions for non-spring-return actuators

4. **Visual inspection:**
   - Inspect blade edges and seals for damage
   - Check actuator mounting security
   - Verify linkage connections tight
   - Examine wiring and connections

5. **Documentation:**
   - Record all test results
   - Note any deficiencies
   - Schedule repairs for failed items
   - Update inspection database

### Leakage Testing

While not required for routine inspections, leakage testing verifies UL 555S performance:

**Test setup:**
- Seal damper and duct section in temporary enclosure
- Create 4.0" w.g. pressure differential using calibrated fan
- Measure airflow required to maintain pressure
- Compare to leakage class limits

**Measured leakage calculation:**

$$L_{measured} = \frac{Q_{measured}}{A_{damper}}$$

Where:
- $L_{measured}$ = Measured leakage rate (cfm/sq ft)
- $Q_{measured}$ = Airflow through damper at 4" w.g. (cfm)
- $A_{damper}$ = Damper area (sq ft)

**Acceptance criteria:**

$$L_{measured} \leq L_{class}$$

Damper passes if measured leakage does not exceed its rated class.

## Troubleshooting and Maintenance

### Common Operational Issues

**Damper fails to close:**

*Possible causes:*
- Power failure without backup
- Failed actuator motor
- Broken linkage
- Blade obstruction or binding
- Control signal failure

*Diagnostic steps:*
1. Check power supply voltage at actuator
2. Manually operate actuator override
3. Inspect blades for obstructions
4. Verify control signal at actuator terminals
5. Check actuator fault indicators

**Damper closes but end switch not confirmed:**

*Possible causes:*
- Misadjusted end switch
- Broken end switch
- Wiring fault
- Blade not fully closed

*Corrections:*
- Adjust end switch cam position
- Replace failed switch
- Repair wiring connections
- Investigate blade binding

**Excessive air leakage:**

*Possible causes:*
- Damaged edge seals
- Warped or bent blades
- Debris preventing full closure
- Improper blade adjustment

*Corrections:*
- Replace gaskets and seals
- Straighten or replace blades
- Clean damper and duct
- Adjust blade linkages per manufacturer specifications

### Preventive Maintenance Schedule

**Quarterly:**
- Visual inspection of accessible dampers
- Verify power supply and actuator indicators
- Check access panel security

**Annually:**
- Full functional testing per NFPA 105
- Lubricate bearings and pivot points
- Tighten mounting hardware
- Clean blades and frame
- Test backup power systems

**Every 5 years:**
- Comprehensive assessment of all dampers
- Actuator overhaul or replacement
- Seal and gasket replacement
- Retesting of critical life-safety dampers

### Replacement and Upgrade Considerations

**When to replace smoke dampers:**
- Failed leakage testing
- Obsolete actuator models
- Code requirement changes (new leakage class needed)
- Repeated maintenance issues
- Physical damage beyond repair

**Actuator replacement:**
- Ensure replacement matches damper torque requirements
- Verify voltage and control signal compatibility
- Reprogram control sequences if needed
- Conduct full commissioning after replacement

## Advanced Applications

### Combination Fire/Smoke Dampers

Devices combining UL 555 and UL 555S listings:

**Dual protection:**
- Fire resistance rating (1-hour, 1.5-hour, 3-hour)
- Smoke leakage class (I, II, or III)
- Dual activation: Fusible link OR electrical signal

**Applications:**
- Smoke barriers with fire-resistance rating
- Reduces penetrations (one damper vs. two separate)
- Simplifies inspection and maintenance

**Control logic:**

```
Fire Condition (Heat):
  Fusible Link Melts → Damper Closes → Remains Closed

Smoke Condition (Before Fire):
  Smoke Detected → Electrical Signal → Damper Closes → May Reopen After All-Clear

Fire Alarm Condition:
  Alarm Activated → Electrical Signal → Damper Closes
```

### Smoke Dampers in Smoke Exhaust Systems

High-temperature smoke exhaust dampers:

**Special requirements:**
- Elevated temperature rating (minimum 350°F intermittent, 500°F common)
- Non-spring-return actuators (springs weaken at high temperature)
- High-velocity ratings (4,000+ fpm)
- Larger actuator torque for pressure differential

**Exhaust damper control:**
- Normally closed during HVAC operation
- Open on fire alarm in designated fire zone
- Modulate based on pressure control or smoke optical density

### Radiation Dampers

Specialized dampers for radiation protection:

**Function:**
- Limit radiant heat transfer through ductwork
- Used in nuclear facilities, laboratories, specific industrial applications
- May combine radiation shielding with smoke/fire protection

**Construction:**
- Lead-lined blades or frames
- Special seal materials
- Certified for radiation attenuation performance

## Conclusion

Smoke dampers are sophisticated active fire protection devices essential for smoke management and occupant life safety. Understanding UL 555S requirements, proper control logic design, and integration with fire alarm and building automation systems ensures effective smoke compartmentation during fire events. Engineers must carefully select damper leakage classes, temperature ratings, and actuator specifications based on specific application requirements. Contractors must follow manufacturer installation instructions precisely and verify proper operation through comprehensive commissioning. Facility managers must maintain regular inspection and testing schedules per NFPA 105 to ensure smoke dampers remain functional throughout the building's life. Proper application of smoke damper technology, combined with engineered smoke control strategies, protects egress routes and staging areas, enabling safe evacuation and effective firefighting operations.
