---
title: "Schedules Format Content"
aliases: ["Schedules Format Content"]
description: "Equipment schedules format and content standards for HVAC construction drawings including diffuser schedules, grille schedules, valve schedules, motor schedules, data columns, notes, and schedule coordination requirements"
weight: 3
---

Schedules are tabular data presentations on construction drawings that provide systematic organization of equipment specifications, performance data, and installation requirements. Properly formatted schedules eliminate ambiguity, reduce errors, and streamline equipment procurement and installation.

## Schedule Organization Principles

### General Format Standards

**Tabular Structure Requirements:**
- Mark designation column positioned as leftmost column
- Equipment description immediately following mark designation
- Performance data arranged in logical left-to-right sequence
- Installation requirements grouped in dedicated columns
- Notes column positioned as rightmost column

**Header Information:**
- Schedule title indicating equipment type
- Drawing number and sheet location
- Revision tracking for schedule modifications
- Legend for abbreviations and symbols used

**Mark Designation System:**
- Consistent prefix system by equipment type (AHU-, EF-, P-, etc.)
- Sequential numbering within equipment categories
- Hierarchical numbering for system relationships
- Cross-reference to detail callouts and sections

### Sheet Layout Considerations

Position schedules to maximize readability while minimizing sheet count. Large schedules may extend across multiple sheets with header information repeated on each continuation. Coordinate schedule placement with drawing views to avoid obscuring critical information.

**Scale and Text Size:**
- Minimum 3/32" text height for printed drawings
- Column width proportional to data content
- Adequate row spacing for legibility (minimum 3/16" row height)
- Bold or increased font size for headers

## Equipment Schedule Components

### Air Handling Unit Schedules

Air handling unit schedules present comprehensive performance and construction data for central station air handlers.

**Essential Data Columns:**

| Column Category | Required Information |
|----------------|---------------------|
| Identification | Mark, location, service area |
| Airflow | Supply CFM, return CFM, outside air CFM |
| Pressures | Total static pressure, external static pressure |
| Heating | Capacity (MBH), entering/leaving temperatures |
| Cooling | Capacity (MBH or tons), entering/leaving temperatures |
| Motor Data | HP, voltage, phase, RPM, frame, enclosure |
| Dimensions | Length, width, height |
| Weight | Operating weight, shipping weight |
| Acoustics | Sound power levels by octave band |

**Component-Specific Columns:**
- Coil construction (rows, FPI, materials)
- Filter specifications (type, efficiency, initial/final pressure drop)
- Fan type and arrangement
- Drive system (belt/direct, sheave sizes, belt sections)
- Access panel locations
- Casing construction (gauge, insulation type/thickness)

**Performance Conditions:**
- Design airflow at specified external static pressure
- Coil entering/leaving conditions at design load
- Motor service factor and maximum BHP
- Fan speed at design conditions

### Fan Schedule Format

**Exhaust and Supply Fan Data:**

```
Mark | Location | CFM | TSP | Motor HP | Voltage | Drive | Inlet Size | Notes
EF-1 | Toilet    | 450 | 0.5 | 1/4     | 120/1   | Direct| 10" Ø     | Roof mounted
```

**Required Performance Parameters:**
- Volumetric flow rate at standard air density
- Static pressure (total, velocity, or external)
- Fan type (centrifugal, axial, inline)
- Wheel diameter and width (for centrifugal fans)
- Operating RPM at design point
- Motor electrical characteristics
- Sound ratings (sones or dBA)

**Construction Specifications:**
- Housing material and gauge
- Wheel construction (material, backward/forward curved)
- Shaft and bearing types
- Vibration isolation requirements
- Mounting orientation

### Pump Schedule Structure

Hydronic pump schedules define fluid moving equipment for heating and cooling systems.

**Performance Specifications:**

| Data Element | Description |
|-------------|-------------|
| Flow rate | GPM at design conditions |
| Head | Total dynamic head (feet) |
| Fluid | Water, glycol mixture (specify %) |
| Temperature | Design fluid temperature |
| NPSH | Net positive suction head available/required |

**Physical Characteristics:**
- Pump type (centrifugal, inline, vertical turbine)
- Casing material (cast iron, bronze, stainless)
- Impeller material and trim
- Seal type (mechanical, packing)
- Coupling type (flexible, rigid, spacer)

**Motor and Drive:**
- Horsepower (design point and service factor)
- Electrical specifications (voltage, phase, frequency)
- Enclosure type (TEFC, ODP, explosion-proof)
- Efficiency class and premium efficiency compliance
- Variable frequency drive compatibility

**Installation Requirements:**
- Suction/discharge connection sizes and types
- Isolation valve requirements
- Strainer/filter specifications
- Base/mounting details
- Minimum clearance dimensions

## Terminal Device Schedules

### Diffuser and Grille Schedule Content

Air distribution device schedules organize supply outlets, return grilles, and exhaust registers.

**Supply Diffuser Schedule Format:**

```
MARK | ROOM | TYPE | SIZE | NECK | CFM | THROW | NC | NOTES
------------------------------------------------------------------------------------------------
SD-1 | 101  | 4SQ  | 24x24| 12"Ø | 400 | 15'   | 30 | White finish
SD-2 | 102  | 4SQ  | 24x24| 12"Ø | 350 | 15'   | 28 | White finish
SD-3 | 103  | 2SL  | 12x6 | 8x6  | 150 | 8'-3  | 25 | Vertical throw
```

**Performance Data Requirements:**
- Design airflow (CFM) for heating and cooling modes
- Throw distance at specified terminal velocity (50 or 100 FPM)
- Pressure drop at design flow
- Noise criteria (NC) or sound level (dBA)
- Induction ratio for high-induction diffusers

**Physical Specifications:**
- Manufacturer's type designation
- Face size dimensions
- Neck size and configuration
- Number of slots, cones, or directional patterns
- Deflection settings (0°, 15°, 30°, 45°)

**Installation Details:**
- Mounting type (lay-in, surface, recessed)
- Finish and color specification
- Damper type (opposed blade, butterfly)
- Actuator requirements for VAV terminals

### Return and Exhaust Grille Schedules

**Essential Columns:**
- Mark designation coordinated with drawing symbols
- Free area (square feet) for velocity calculations
- Face velocity at design CFM
- Core type (eggcrate, bar, louver)
- Frame type (1", 2", surface mount)
- Filter grille requirements (specify filter type/efficiency)

**Special Considerations:**
- Door undercut transfers with specified free area
- Transfer grilles between spaces (provide airflow direction)
- Exhaust grilles in corrosive environments (specify materials)
- Fire-rated grille assemblies (UL rating and manufacturer)

## Control Device Schedules

### Valve Schedule Organization

Control and isolation valve schedules prevent field confusion and ensure proper valve selection.

**Two-Way Control Valve Schedule:**

| Mark | Service | Size | Type | Body | Trim | Cv | Close-Off PSI | Actuator | Signal |
|------|---------|------|------|------|------|----|--------------|-----------| -------|
| V-1  | HW-CHW  | 2"   | Globe| Bronze| SS | 45 | 100          | Electric  | 2-10VDC|

**Three-Way Valve Specifications:**
- Mixing or diverting configuration
- Port connections (A, B, AB labeling)
- Characterized plug (linear, equal percentage)
- Maximum pressure drop through common port
- Flow characteristics at intermediate positions

**Actuator Requirements:**
- Control type (pneumatic, electric, electro-hydraulic)
- Fail position (normally open, normally closed, fail-last)
- Spring return or non-spring return
- Control signal type and range
- Auxiliary switches and positioners

**Material Specifications:**
- Body material compatible with fluid service
- Trim material for shutoff requirements
- Seat leakage class (ANSI Class II through VI)
- Pressure and temperature ratings
- End connections (threaded, flanged, grooved, soldered)

### Isolation Valve Schedule

**Ball and Butterfly Valve Data:**
- Size matching connected piping
- Pressure class (125#, 150#, 250#)
- Body material (bronze, iron, DI, stainless)
- Seat material and shutoff rating
- Operator type (lever, gear, chainwheel)
- Locking provisions for critical services

**Check Valve Specifications:**
- Type (swing, dual-plate, spring-loaded)
- Installation orientation requirements
- Cracking pressure
- End connections and flange class

## Motor and Electrical Schedules

### Motor Schedule Content

When motors are provided separate from driven equipment, dedicated motor schedules provide electrical specifications.

**Electrical Characteristics:**

| Parameter | Specification |
|-----------|--------------|
| HP | Nameplate horsepower |
| Voltage | Operating voltage (208, 230, 460, 575) |
| Phase | Single or three-phase |
| Frequency | 60 Hz (50 Hz international) |
| Full Load Amps | FLA at rated voltage |

**Performance Data:**
- Service factor (typically 1.15 for HVAC applications)
- Efficiency class (IE3, NEMA Premium)
- Power factor at full load
- Locked rotor code letter
- Starting torque characteristics

**Construction:**
- Frame size (NEMA standard)
- Enclosure (TEFC, ODP, TENV, explosion-proof)
- Mounting (foot, flange, resilient base)
- Insulation class (B, F, H)
- Thermal protection (manual reset, automatic)

**Application Notes:**
- Variable frequency drive compatibility
- Inverter duty rated for VFD applications
- Special bearings or lubrication
- Altitude and ambient temperature derating
- Hazardous location classifications

### Electrical Connection Schedule

**Power Requirements:**
- Maximum overcurrent protection (MOCP)
- Minimum circuit ampacity (MCA)
- Recommended disconnect switch size
- Wire size and type recommendations
- Conduit size for power conductors

**Control Wiring:**
- Low voltage control power requirements
- Control circuit voltage and VA loading
- Number of control points and interlock circuits
- Communication protocol requirements (BACnet, Modbus, etc.)

## Specialized Schedules

### Coil Schedule Standalone Format

When coils are specified separately from air handling equipment.

**Heat Transfer Data:**
- Capacity at entering/leaving conditions
- Airside flow and pressure drop
- Fluid side flow and pressure drop
- LMTD or effectiveness ratings

**Construction Parameters:**
- Tube material, diameter, and wall thickness
- Fin material, spacing (FPI), and thickness
- Number of rows and circuits
- Casing material and connection sizes
- Working pressure test requirements

### Heat Exchanger Schedule

**Plate and Frame Exchangers:**
- Heat transfer capacity (MBH)
- Hot/cold side flows and temperatures
- Pressure drops on both sides
- Number of plates and plate material
- Gasket material compatibility
- Maximum working pressure

**Shell and Tube Specifications:**
- Tube material, diameter, length, and gauge
- Number of passes and tube count
- Shell diameter and material
- Baffle type and spacing
- Removable bundle requirements

### Boiler and Water Heater Schedules

**Capacity and Efficiency:**
- Input rating (MBH gas input)
- Output capacity (MBH or Btuh net)
- Thermal efficiency at design conditions
- Turndown ratio for modulating burners
- Combustion efficiency at various loads

**Fuel Specifications:**
- Fuel type (natural gas, propane, oil)
- Gas pressure requirements (inlet minimum/maximum)
- Gas connection size
- Oil grade and supply temperature
- Electric power for controls and auxiliaries

**Physical Data:**
- Shipping dimensions and weight
- Clearance requirements (sides, front, back, top)
- Flue connection size and centerline height
- Combustion air requirements (CFM)

## Data Column Standards

### Measurement Units Consistency

Maintain consistent units throughout schedules to prevent calculation errors.

**Standard HVAC Units:**
- Airflow: CFM (cubic feet per minute)
- Air pressure: inches water column (in. w.c. or in. w.g.)
- Heating/cooling: MBH (thousands Btuh) or tons
- Water flow: GPM (gallons per minute)
- Water pressure: feet of head or PSI
- Temperature: °F
- Dimensions: inches or feet-inches
- Weight: pounds (shipping/operating)

**Derived Values:**
- Face velocity: FPM (feet per minute)
- Heat transfer: Btuh per square foot
- Flow per ton: GPM per ton
- Temperature difference: ΔT in °F

### Precision and Significant Figures

**Airflow Values:**
- Round to nearest 5 CFM for flows under 500 CFM
- Round to nearest 10 CFM for flows 500-2000 CFM
- Round to nearest 50 CFM for flows over 2000 CFM

**Capacity Values:**
- Report capacities to 2-3 significant figures
- Use MBH for heating (12.5 MBH, not 12,500 Btuh)
- Use tons for cooling (7.5 tons, not 90 MBH)

**Dimensional Data:**
- Equipment sizes to nearest inch or half-inch
- Duct/pipe sizes per standard increments
- Connection sizes per standard pipe/duct sizing

## Notes and Remarks Column

### General Notes Format

The notes column provides critical information not captured in dedicated data columns.

**Installation Requirements:**
- "Provide seismic restraints per detail 5/M-4"
- "Coordinate location with structural penetration"
- "Maintain 36" minimum service clearance"
- "Mount on spring isolators, type S-3"

**Performance Qualifications:**
- "Select for quiet operation, maximum NC 35"
- "Size for 20% future capacity increase"
- "Verify available voltage before ordering"
- "Field verify dimensions before fabrication"

**Material Specifications:**
- "Stainless steel in corrosive environment"
- "Food-grade materials, NSF certified"
- "Powder coat finish, color per architect"
- "Galvanized casing, 16 gauge minimum"

**Operational Notes:**
- "Normally OFF, energize during fire alarm"
- "Interlocked with hood operation"
- "VFD controlled from BAS"
- "Manual override switch at entry"

### Cross-Reference Annotations

Link schedule entries to drawing details, specifications, and other documentation.

**Drawing References:**
- "See detail 3/M-6 for mounting"
- "Refer to riser diagram sheet M-1.1"
- "Match duct connection shown in section A-A"
- "Coordinate with reflected ceiling plan A-3.2"

**Specification References:**
- "Per spec section 23 74 00"
- "Basis of design: Trane model XYZ (or approved equal)"
- "Comply with specification section 23 05 13"
- "Submit product data per section 01 33 00"

**Addenda and Revisions:**
- "Revised per addendum 3"
- "CFM increased per RFI 042"
- "See clarification bulletin CB-12"
- "Updated capacity - resubmit selections"

## Schedule Coordination

### Inter-Schedule Consistency

Data must remain consistent across all related schedules and drawings.

**Airflow Balance Verification:**
- Sum of diffuser CFM equals scheduled air handling unit supply CFM
- Return grille total matches AHU return CFM
- Exhaust fan CFM accounts for all exhaust devices served
- Outside air CFM meets ventilation requirements and system balance

**Electrical Load Coordination:**
- Motor HP in equipment schedule matches electrical schedule
- Voltage specifications consistent across all schedules
- Starter/disconnect sizes adequate for connected loads
- Total connected load tallied for service sizing

**Piping System Consistency:**
- Pump GPM serves scheduled coil and terminal loads
- Valve sizes appropriate for connected loads
- Pipe sizing schedule flow rates match equipment connections
- Expansion tank sizing reflects total system volume

### Drawing-to-Specification Coordination

Equipment schedules must align with written specification requirements.

**Specification Cross-References:**
- Equipment types match specified products
- Performance criteria meet or exceed specification minimums
- Material selections comply with specification requirements
- Testing and certification requirements noted in schedules

**Basis of Design Clarifications:**
- When schedule shows specific manufacturer model, add "or approved equal"
- Performance specifications take precedence over model numbers
- Substitution requests reference schedule mark and drawing
- Approved equals must meet all scheduled parameters

### Schedule Updates and Revisions

**Revision Tracking Methods:**
- Cloud/triangle revision markers adjacent to modified entries
- Revision description in schedule header or title block
- Date of revision and revision sequence
- "NIC" (not in contract) or "FUT" (future) for deferred equipment

**Submittal Coordination:**
- Schedule data reflects approved submittals
- As-built schedules updated with actual installed equipment
- Deviations from scheduled values clearly noted
- Record drawings include final operating conditions

### Multi-Discipline Coordination

**Architectural Coordination:**
- Equipment weights for structural design
- Equipment dimensions for spatial planning
- Ceiling heights adequate for equipment and clearances
- Finish specifications matching architectural requirements

**Electrical Coordination:**
- Electrical characteristics provided for service calculations
- Disconnect locations coordinated with access requirements
- Control voltage requirements for low-voltage systems
- Emergency power connections identified

**Plumbing Coordination:**
- Condensate drain requirements from cooling coils
- Water supply for humidifiers and evaporative coolers
- Floor drain proximity for equipment drip pans
- Tempered water for air handler coil flushing

**Fire Protection Coordination:**
- Smoke/fire damper requirements at duct penetrations
- Fire alarm interfaces for fan shutdown/activation
- Kitchen hood suppression system interlocks
- Smoke control system sequence coordination

## Quality Control Procedures

### Schedule Accuracy Verification

**Pre-Issue Checks:**
1. Verify all equipment shown on plans has schedule entry
2. Confirm schedule marks match drawing symbols exactly
3. Calculate totals and verify system balance
4. Cross-check electrical loads and circuit assignments
5. Review for specification compliance
6. Verify units and significant figures
7. Proofread all text entries for clarity

**Calculation Verification:**
- Air system CFM totals balanced within 5%
- Hydronic GPM totals match pump schedules
- Equipment capacities sum to design load calculations
- Diversity factors applied consistently
- Safety factors documented and appropriate

### Common Schedule Errors to Avoid

**Data Entry Mistakes:**
- Transposed digits in equipment marks or model numbers
- Inconsistent units within same column
- Missing decimal points in capacity values
- Conflicting data between related schedules

**Design Coordination Errors:**
- Equipment capacities insufficient for loads
- Motor sizes undersized for driven equipment
- Pressure ratings inadequate for system conditions
- Clearance dimensions insufficient for maintenance

**Documentation Deficiencies:**
- Undefined abbreviations or symbols
- Missing cross-references to details
- Ambiguous performance conditions
- Incomplete electrical specifications

Comprehensive, accurate schedules form the backbone of successful HVAC project documentation. They translate design intent into actionable procurement and installation information while providing permanent record of system design parameters. Meticulous attention to schedule format, content completeness, and coordination prevents costly field issues and supports efficient construction execution.
