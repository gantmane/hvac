---
title: "Design Development Phase"
description: "Comprehensive guide to HVAC design development phase including detailed system design, equipment selection finalization, duct and pipe sizing, control sequences, interdisciplinary coordination, cost estimating, and DD drawings and specifications for mechanical engineering projects"
weight: 2
---

The Design Development (DD) phase represents the critical transition from conceptual design to a fully coordinated, detailed engineering solution. During this phase, HVAC systems evolve from schematic representations into precisely defined systems with equipment selections, distribution layouts, control strategies, and coordination with all building disciplines.

## DD Phase Objectives

The primary objectives of the Design Development phase include:

**System Refinement**
- Finalize HVAC system configurations and zoning strategies
- Complete equipment selection with manufacturer-specific data
- Size all major distribution components (ductwork, piping, terminals)
- Develop comprehensive control sequences and strategies

**Interdisciplinary Coordination**
- Coordinate mechanical systems with architectural, structural, electrical, and plumbing designs
- Resolve spatial conflicts and establish routing corridors
- Coordinate ceiling heights, shaft locations, and equipment room layouts
- Integrate mechanical systems with building envelope performance

**Documentation Development**
- Produce DD drawings at 60-75% completion level
- Develop outline specifications for major equipment and systems
- Prepare cost estimates within ±10-15% accuracy
- Document design decisions and basis of design updates

**Owner Review and Approval**
- Present detailed design solutions to owner for review
- Obtain approvals on equipment selections and system configurations
- Confirm compliance with owner's project requirements (OPR)
- Address value engineering opportunities

## Load Calculation Refinement

Design Development requires refinement of preliminary load calculations to reflect actual building design conditions.

**Updated Input Parameters**
- Finalized building envelope specifications (wall assemblies, glazing performance, roof construction)
- Actual window-to-wall ratios and orientation-specific glazing properties
- Interior finish schedules affecting thermal mass and surface reflectance
- Confirmed occupancy densities and operational schedules
- Lighting power densities from electrical design
- Process load verification from owner and equipment vendors

**Calculation Methodology**
- Perform room-by-room load calculations using ASHRAE transfer function method or radiant time series
- Account for diversity factors in simultaneous cooling loads
- Calculate heating loads at design outdoor conditions with appropriate safety factors
- Determine ventilation airflow requirements per ASHRAE 62.1 using actual occupancy and space classifications
- Calculate latent loads from occupants, outdoor air, and internal moisture sources

**Load Documentation**
- Summarize peak heating and cooling loads by zone and system
- Document critical assumptions and design conditions
- Identify zones with special requirements (high internal gains, humidity control, temperature precision)
- Provide load breakdown showing envelope, ventilation, lighting, equipment, and occupancy components

## Equipment Selection and Specification

Equipment selection during DD phase transitions from budgetary sizing to manufacturer-specific selections with performance data.

**Central Plant Equipment**

Chillers require detailed selection based on:
- Cooling capacity at design entering and leaving water temperatures
- Part-load performance characteristics (IPLV, NPLV per AHRI 550/590)
- Refrigerant type and compliance with environmental regulations
- Physical dimensions, rigging weights, and clearance requirements
- Sound power levels and vibration characteristics
- Control interfaces and communication protocols
- Efficiency compliance with ASHRAE 90.1 or local energy codes

Boilers must be specified with:
- Heating capacity at design supply and return water temperatures
- Turndown ratio and modulation capabilities
- Thermal efficiency at full and part-load conditions (AFUE, combustion efficiency)
- Fuel type, supply pressure requirements, and consumption rates
- Venting requirements (flue diameter, materials, termination clearances)
- Condensing or non-condensing operation characteristics
- Integrated controls and safety devices

**Air Handling Equipment**

Air handling units require complete schedules specifying:
- Airflow capacity at design external static pressure
- Coil selections with entering/leaving conditions, rows, fins per inch, face velocity
- Filter specifications (MERV rating, pressure drop, dimensions, quantity)
- Fan type (plenum, housed, class), motor horsepower, drive arrangement
- Heat recovery device performance (effectiveness, pressure drop, bypass dampers)
- Economizer dampers, actuators, and minimum outdoor air provisions
- Access sections, insulation specifications, casing construction (single/double wall)
- Drain pan materials, slope, and connections

Terminal devices must be scheduled with:
- VAV box airflow range (minimum and maximum CFM)
- Inlet size and connection type (round, rectangular, flexible)
- Control type (pressure independent, pressure dependent)
- Reheat coil capacity and configurations (hot water, electric)
- Actuator specifications (spring return, electronic, control signal type)
- Sound ratings (NC levels at minimum and maximum flow)

**Pumps and Hydronic Components**

Pump selections require:
- Flow rate (GPM) at design head (feet of water)
- Impeller diameter, speed, and trim
- Motor horsepower, voltage, and efficiency class
- Pump curve with operating point clearly marked
- NPSH requirements and verification of available NPSH
- Seal type, materials of construction, and coupling type
- Variable speed drive requirements and control integration

## Ductwork Design and Sizing

Ductwork distribution systems must be sized to deliver required airflow while maintaining acceptable velocities, static pressures, and acoustic performance.

**Sizing Methodology**

Equal friction method provides balanced pressure drop:
- Select friction rate (typically 0.08-0.15 in. w.g. per 100 ft)
- Calculate duct diameter or dimensions for each section based on airflow
- Verify velocity limits (main ducts: 1,200-2,000 FPM; branches: 800-1,200 FPM; final runouts: 600-800 FPM)
- Check total system pressure drop against fan capacity

Static regain method for constant static pressure at takeoffs:
- Size ducts to maintain velocity pressure reduction equal to friction losses
- Downstream ducts increase in size to reduce velocity
- Provides uniform static pressure for branch takeoffs
- Preferred for systems with numerous branches or long runs

**Duct Construction Standards**

Specify duct construction per SMACNA standards:
- Pressure class (0.5", 1", 2", 3", 4", 6", 10" w.g.)
- Reinforcement requirements (maximum unsupported spans)
- Sealing class (Seal Class A, B, or C per SMACNA)
- Insulation specifications (internal or external, thickness, facing)
- Joint types (TDC, TDF, flanged, welded)

**Acoustic Considerations**

Control noise generation and transmission:
- Limit duct velocities to maintain acceptable NC levels
- Specify sound attenuators at air handler discharge and zone entry points
- Calculate required attenuation by octave band
- Avoid abrupt transitions causing turbulence and regenerated noise
- Specify acoustic duct lining where required (1" or 2" thickness)

## Piping Design and Sizing

Hydronic piping systems require proper sizing to deliver design flow rates while maintaining acceptable pressure drops and flow velocities.

**Sizing Criteria**

Pipe sizing based on friction loss and velocity limits:
- Friction rate: 1-4 feet of head per 100 feet of pipe (typical: 2-2.5 ft/100 ft)
- Velocity limits for noise control: 4-8 FPS for pipe sizes under 2", up to 10 FPS for larger pipes
- Return piping typically one to two sizes larger than supply
- Critical circuits (long runs, high flow) require detailed pressure drop analysis

**System Types and Configurations**

Primary-secondary pumping systems:
- Primary loop serves production equipment (chillers, boilers) at constant flow
- Secondary loop serves building loads with variable flow
- Decoupler piping section connects loops with minimal pressure drop
- Provides hydraulic separation allowing independent flow control

Variable primary flow systems:
- Single loop serving both production and distribution
- Chillers or boilers arranged in parallel with individual isolation valves
- Minimum flow bypass ensures equipment minimum flow requirements
- Requires careful control sequence to avoid low-flow conditions

**Pipe Material Selection**

Specify appropriate materials based on service:
- Chilled water: Steel (Schedule 40, black), copper (Type L), CPVC for smaller sizes
- Hot water heating: Steel (Schedule 40, black), copper (Type L)
- Condenser water: Steel (Schedule 40, black), 304/316 stainless for corrosive conditions
- Steam: Steel (Schedule 40, black) with appropriate pressure ratings
- Condensate return: Steel (Schedule 80 for vented, Schedule 40 for pressurized)

## Control System Design

Control sequences developed during DD phase provide the framework for system operation and energy management.

**Control Architecture**

Define control system hierarchy:
- Building automation system (BAS) architecture and communication protocols (BACnet, Modbus, LON)
- Network topology (distributed controllers, field panels, workstation locations)
- Integration with existing BAS or standalone operation
- Data point requirements (physical points, virtual points, trending capacity)

**Sequence Development**

Air handling unit control sequences must address:
- Supply air temperature reset based on zone demand or outdoor air temperature
- Economizer operation with differential enthalpy or dry-bulb comparison
- Minimum outdoor air control with CO2 or occupancy-based demand control ventilation
- Morning warm-up and night setback strategies
- Freeze protection for cooling coils (discharge air low-limit, mixed air low-limit)
- Filter status monitoring and alarm generation
- Smoke detection response and fan shutdown/override

VAV system sequences include:
- Zone temperature control with airflow modulation (cooling mode)
- Minimum airflow setpoints (ventilation requirement or 30% of maximum, whichever is greater)
- Reheat coil staging or modulation when airflow reaches minimum
- Static pressure reset based on zone damper positions (trim and respond logic)
- Supply air temperature reset based on zone with highest cooling demand
- Occupied/unoccupied setpoint changes and scheduling

Chilled water plant sequences specify:
- Chiller staging based on load (lead-lag-lag configuration typical)
- Condenser water temperature optimization and tower fan staging
- Chilled water supply temperature reset based on outdoor air or return temperature
- Primary/secondary pump control and flow verification
- Free cooling operation if applicable (waterside economizer)
- Equipment rotation for equal run-time distribution
- Optimal start algorithms for equipment pre-cooling

**Control Valve and Damper Sizing**

Size control devices for proper authority and rangeability:
- Control valves: Select Cv based on pressure drop across valve equal to 25-50% of total circuit pressure drop
- Valve authority (N) = ΔP_valve / (ΔP_valve + ΔP_system) should be 0.25-0.50
- Damper sizing: Face velocity typically 1,000-1,500 FPM through wide-open damper
- Specify actuator torque requirements accounting for startup and airstream forces

## Coordination with Other Disciplines

Interdisciplinary coordination intensifies during DD phase as systems become spatially defined.

**Architectural Coordination**

Coordinate mechanical systems with architectural design:
- Confirm equipment room sizes, door widths, and ceiling heights accommodate equipment and maintenance clearances
- Verify shaft dimensions and locations for vertical distribution
- Coordinate ceiling heights with ductwork, piping, and lighting
- Establish locations for air terminals, grilles, registers, and thermostats
- Confirm exterior louver locations, sizes, and architectural finishes
- Coordinate mechanical equipment visibility and screening requirements

**Structural Coordination**

Coordinate with structural engineer:
- Provide equipment weights and seismic loads for structural analysis
- Identify required roof openings for equipment rigging
- Coordinate hanger and support locations with structural framing
- Identify locations requiring supplemental steel for heavy equipment
- Provide vibration isolation requirements for rotating equipment
- Confirm slab depressions or pits for equipment

**Electrical Coordination**

Coordinate power requirements with electrical engineer:
- Provide complete equipment electrical schedules (voltage, phase, FLA, MCA, MOCP)
- Identify VFD locations and harmonic mitigation requirements
- Coordinate control power requirements (120V, 24V transformers)
- Provide motor starter locations and control wiring requirements
- Coordinate emergency power requirements for life safety systems
- Establish BAS network power and communication infrastructure

**Plumbing Coordination**

Coordinate with plumbing engineer:
- Heating and cooling coil drain connections to sanitary or storm systems
- Humidifier water supply and drain requirements
- Equipment and floor drain locations in mechanical rooms
- Makeup water connections for cooling towers and closed-loop systems
- Steam and condensate piping coordination if applicable
- Domestic water heating integration with HVAC systems

**Fire Protection Coordination**

Coordinate with fire protection engineer:
- Sprinkler head locations to avoid air diffusers and ductwork
- Smoke dampers in duct penetrations through fire-rated assemblies
- Fire dampers in air transfer openings
- Smoke detection integration with HVAC controls
- Stair pressurization system coordination with building pressurization

## Spatial Coordination and Routing

Develop major distribution routing during DD phase to establish feasibility and spatial requirements.

**Horizontal Distribution**

Establish primary distribution paths:
- Main duct and pipe runs in corridors or above circulation spaces
- Coordinate with structural beam depths and lighting layouts
- Maintain minimum clearances (typically 12-18" above finished floor for access)
- Identify areas requiring bulkheads or soffits
- Plan for future access to valves, dampers, and control devices

**Vertical Distribution**

Design shaft systems for efficient vertical transport:
- Size shafts for ductwork and piping with 20-25% additional space for future needs
- Provide access doors at each floor for installation and maintenance
- Coordinate shaft locations for minimal impact on floor plans
- Establish fire-rated shaft construction requirements
- Plan for seismic separation at floor penetrations

**Equipment Room Layouts**

Develop mechanical room arrangements:
- Equipment placement with code-required clearances (typically 36" access, 48" for maintenance)
- Establish maintenance clearances for tube bundle removal, filter access, motor replacement
- Provide clear path for equipment replacement and rigging
- Locate isolation valves and service disconnects for accessibility
- Plan floor drains, housekeeping pads, and equipment bases

## Energy Modeling and Analysis

Energy analysis during DD phase provides accurate performance predictions and identifies optimization opportunities.

**Model Development**

Develop detailed energy model reflecting DD design:
- Model geometry matching architectural floor plans and elevations
- HVAC systems as designed (equipment types, efficiencies, control strategies)
- Actual equipment performance data from manufacturer selections
- Lighting power densities from electrical design
- Plug load assumptions confirmed with owner
- Operational schedules by space type and day of week

**Analysis Output**

Energy model provides critical design information:
- Annual energy consumption by end use (heating, cooling, fans, pumps, lighting, plug loads)
- Peak demand analysis for utility connection sizing
- Comparison to baseline performance (ASHRAE 90.1 Appendix G)
- Energy cost analysis with local utility rates
- Identification of high-energy systems for targeted efficiency improvements

**Optimization Studies**

Evaluate design alternatives during DD phase:
- Equipment efficiency impacts (premium efficiency vs. standard)
- Heat recovery options (energy recovery ventilators, waterside economizers)
- Control strategy refinements (optimal start/stop, demand-based ventilation)
- System configuration alternatives (VAV vs. fan coil, chilled beams)
- Renewable energy integration (solar thermal, ground-source heat pumps)

## Cost Estimating

DD phase cost estimates provide refined budget validation and value engineering opportunities.

**Estimate Accuracy**

DD estimates target ±10-15% accuracy through:
- Quantity takeoffs from DD drawings (major equipment, duct/pipe lengths by size)
- Manufacturer budget pricing for specified equipment
- Unit pricing for distribution systems ($/lb ductwork, $/LF piping by size)
- Regional labor rates and productivity factors
- Material and equipment escalation to bid date

**Estimate Components**

Comprehensive mechanical estimate includes:
- Equipment costs (chillers, boilers, air handlers, terminal units, pumps, specialties)
- Distribution costs (ductwork, piping, fittings, hangers, insulation)
- Controls and automation systems
- Testing, adjusting, and balancing (TAB)
- Equipment start-up and commissioning support
- General conditions and contractor overhead/profit

**Value Engineering**

DD phase provides optimal timing for value engineering:
- System alternative comparisons with life-cycle cost analysis
- Equipment efficiency trade-offs balancing first cost and operating cost
- Distribution system optimization (centralized vs. distributed equipment)
- Control system sophistication relative to operational capabilities
- Phasing opportunities to spread capital expenditure
- Energy incentive and rebate opportunities

## DD Drawings and Documentation

Design Development drawings communicate system design to owner, contractors, and coordination team.

**Drawing Content and Detail Level**

Mechanical plans (scale 1/8" = 1'-0" typical):
- Equipment locations with dimensions to building grid
- Major ductwork and piping distribution with sizes indicated
- Air terminals, grilles, registers, and diffusers located
- Thermostats and control devices shown
- Fire dampers, smoke dampers, and volume dampers indicated
- Coordination with architectural elements (ceiling heights, door swings, casework)

Mechanical sections and details:
- Equipment room sections showing equipment arrangement and clearances
- Shaft sections illustrating vertical distribution and penetrations
- Typical connection details for common conditions
- Critical coordination sections showing interferences and resolutions

Schedules:
- Equipment schedules with capacities, sizes, electrical characteristics, and performance data
- Ductwork schedules summarizing sizes, pressure classes, and insulation requirements
- Piping schedules listing sizes, materials, insulation, and heat tracing
- Air device schedules with types, sizes, and airflow quantities

Control diagrams:
- System riser diagrams showing control architecture
- Sequence flow diagrams illustrating operating modes
- Control point summaries listing all monitored and controlled points

**Specification Development**

DD specifications transition from outline format to technical sections:
- Division 23 - HVAC sections organized by CSI MasterFormat
- Equipment specifications with detailed performance requirements
- Material specifications for ductwork, piping, insulation, supports
- Execution requirements for installation, testing, and commissioning
- Submittal requirements and approval procedures
- Warranty and maintenance requirements

**Basis of Design Updates**

Update basis of design report to document DD decisions:
- Design criteria refinement (loads, flow rates, temperatures)
- Equipment selection rationale and alternatives considered
- Control philosophy and sequence narrative descriptions
- Energy analysis results and compliance documentation
- Code compliance summary and applicable standards
- Outstanding design issues requiring resolution in CD phase

## Owner Review and Approval Process

DD phase concludes with formal owner review and approval to authorize Construction Documents phase.

**DD Submission Package**

Prepare comprehensive submission:
- Complete DD drawing set (mechanical, electrical, plumbing, fire protection)
- Updated basis of design report
- Equipment specifications and performance data
- Cost estimate with line-item breakdown
- Energy model results and analysis
- Value engineering recommendations if applicable

**Design Review Meeting**

Present design to owner and stakeholders:
- Walkthrough of mechanical systems and equipment selections
- Discussion of spatial impacts and coordination challenges
- Review of cost estimate relative to budget
- Energy performance and sustainability features
- Operation and maintenance considerations
- Schedule impacts and long-lead equipment items

**Approval and Authorization**

Obtain formal approval to proceed:
- Owner approval of equipment selections and system configurations
- Budget confirmation or value engineering direction
- Resolution of outstanding design issues
- Authorization to proceed to Construction Documents phase
- Updated project schedule and milestone dates

## DD Phase Deliverables Checklist

Verify completion of all DD requirements:

**Drawings**
- Mechanical floor plans at 1/8" scale showing equipment, distribution, and devices
- Equipment room plans and sections with dimensions and clearances
- Mechanical schedules (equipment, ductwork, piping, air devices)
- Control diagrams and riser diagrams
- Coordination sections resolving critical interferences

**Calculations**
- Room-by-room load calculations
- Duct and pipe sizing calculations
- Pump and fan head calculations
- Diversity and load profile analysis
- Energy model and annual consumption analysis

**Specifications**
- Outline specifications for all Division 23 sections
- Equipment performance specifications
- Material and installation requirements
- Testing and commissioning requirements

**Reports**
- Updated basis of design report
- Cost estimate with quantity takeoffs
- Energy analysis and code compliance documentation
- Value engineering study results if performed

**Approvals**
- Owner approval of equipment selections
- Design review meeting minutes
- Budget approval and authorization to proceed to CD

The Design Development phase establishes the complete framework for construction documentation. All major design decisions are finalized, equipment is selected with performance data, distribution systems are sized and routed, and coordination with other disciplines resolves spatial conflicts. The DD deliverables provide the foundation for preparing complete and coordinated construction documents that contractors can bid and build from with confidence.

