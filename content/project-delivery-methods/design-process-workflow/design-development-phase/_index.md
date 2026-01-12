---
title: "Design Development Phase"
description: "Comprehensive HVAC design development phase documentation covering detailed system design, equipment selection criteria, duct and pipe sizing methodologies, control sequence development, multidisciplinary coordination, and cost estimation for mechanical systems"
weight: 3
---

The Design Development (DD) phase translates schematic design concepts into specific, coordinated systems with defined equipment, distribution networks, and control strategies. This phase establishes the technical basis for construction documents and provides sufficient detail for accurate cost estimation and value engineering.

## Phase Objectives

The DD phase produces 50-75% complete design documentation that:

- Specifies major equipment types, capacities, and performance characteristics
- Sizes primary distribution systems (ductwork, piping, diffusers)
- Develops control sequences and integration strategies
- Coordinates HVAC systems with architectural, structural, electrical, and plumbing disciplines
- Refines energy models and validates code compliance
- Establishes project cost with ±15% accuracy

## System Design Refinement

### Load Calculation Finalization

Detailed load calculations incorporate:

**Building envelope refinement:**
- Actual window-to-wall ratios from architectural drawings
- Confirmed wall, roof, and floor assembly U-values
- Specific glazing properties (U-factor, SHGC, VT)
- Thermal bridge analysis at critical junctions
- Infiltration based on building tightness specifications

**Internal load verification:**
- Lighting power density from electrical drawings (W/ft²)
- Receptacle loads by space type
- Process equipment schedules with connected loads and diversity factors
- Occupant density from architectural program
- Equipment heat gain (sensible and latent components)

**Ventilation air quantities:**
- ASHRAE 62.1 calculations by zone
- Exhaust system requirements
- Multiple spaces equations for system-level ventilation
- Outdoor air fraction at design conditions

**Peak load timing:**
- Hour-by-hour load profiles for energy modeling
- Simultaneous vs. non-simultaneous loads
- Part-load conditions for equipment staging

### Zone-Level Design

Each thermal zone receives specific design attention:

**Air distribution:**
- CFM per zone (heating, cooling, ventilation minimum)
- Diffuser quantities and layout aligned with ceiling plans
- Throw distances and discharge velocities
- Return air pathways (ducted, plenum, transfer)
- Sound criteria (NC/RC targets)

**Terminal equipment selection:**
- VAV box sizes with min/max CFM
- Reheat coil capacities (electric kW or hot water MBH)
- Fan-powered box specifications
- Radiant panel areas and output
- Baseboard or convector lengths

**Temperature control:**
- Setpoint schedules (occupied, unoccupied, warmup, setback)
- Throttling range and control authority
- Sensor locations
- Override capabilities

## Equipment Selection

### Primary Equipment Specifications

**Central air handling units:**

Selection criteria include:
- Supply airflow (CFM) at external static pressure (in. w.g.)
- Coil face velocities (typically 400-550 FPM)
- Filter efficiency (MERV rating) and pressure drop
- Mixing box configuration (return, outdoor, relief)
- Fan type (plenum, housed, AF plug) and drive (belt, direct)
- Heating/cooling coil rows, fin density, and capacity
- Humidification type and capacity
- Sound attenuation requirements
- Access door locations
- Seismic certification

Dimensional constraints:
- Overall length, width, height
- Coil removal clearances
- Filter access requirements
- Rigging weights for roof units

**Chillers:**

Specification parameters:
- Cooling capacity (tons) at ARI standard conditions
- Entering/leaving chilled water temperatures
- Condenser type (water-cooled, air-cooled) and approach
- Compressor type (screw, centrifugal, scroll)
- Efficiency (kW/ton or IPLV)
- Refrigerant type and charge
- Sound levels (dBA at specified distance)
- Physical dimensions and operating weight
- Electrical characteristics (voltage, phase, MCA, MOCP)
- Vibration isolation requirements

**Boilers:**

Key selections:
- Output capacity (MBH or HP)
- Fuel type (natural gas, oil, electric)
- Efficiency (AFUE, combustion, thermal)
- Burner turndown ratio
- Operating pressure and temperature
- Condensing vs. non-condensing
- Venting method (Category I-IV)
- Emissions compliance (NOx, CO limits)
- Sequencing strategy for multiple units

**Cooling towers:**

Design specifications:
- Heat rejection capacity (MBH or tons)
- Entering/leaving water temperatures
- Wet bulb design temperature
- Flow rate (GPM)
- Fan motor horsepower and quantity
- Fill type and material
- Basin heater capacity
- Blow-down rate for water treatment
- Footprint and height clearances

### Secondary Equipment

**Pumps:**

Sizing methodology:
- Flow rate: Q = (Cooling or Heating Load in BTU/hr) / (500 × ΔT)
- Head pressure from system pressure drop calculation
- Impeller diameter and trim
- Motor horsepower with service factor
- Pump curve matching to system curve
- NPSH requirements
- Seal type (mechanical, gland packing)
- Base and coupling specifications

**Terminal units:**

VAV box specifications:
- Maximum CFM (primary air)
- Minimum CFM (ventilation or comfort)
- Inlet size and connection type
- Damper type (single blade, opposed blade)
- Controls package (pneumatic, DDC)
- Sound rating (NC level)
- Reheat coil (if applicable): capacity, rows, GPM
- Fan (if fan-powered): CFM, static, BHP, sound

**Heat exchangers:**

Plate and frame or shell-and-tube selection:
- Heat transfer capacity (MBH)
- Primary/secondary fluid flow rates
- Approach temperature
- Pressure drop limits (both sides)
- Materials (copper, stainless steel, brazed)
- Connection sizes
- Isolation and bypass provisions

## Distribution System Sizing

### Ductwork Design

**Sizing methods:**

Equal friction method:
- Select friction rate (typically 0.08-0.15 in. w.g./100 ft)
- Size each section for calculated CFM
- Results in balanced pressure drops
- Suitable for most commercial systems

Static regain method:
- Velocity decreases at each branch
- Static pressure regained offsets downstream losses
- Maintains constant static at takeoffs
- Used for long runs or constant volume systems

Velocity method:
- Main ducts: 1200-1800 FPM
- Branch ducts: 800-1200 FPM
- Runouts to diffusers: 500-800 FPM
- Simple but may not optimize energy

**Aspect ratio limits:**
- Maximum 4:1 for rectangular ducts
- Equivalent round diameter calculation for aspect ratios >2:1
- Flat oval considered for height-restricted spaces

**Material specifications:**
- Galvanized steel gauge per SMACNA (pressure class)
- Duct board for shorter runs, internal insulation
- Flexible duct limited to 5 ft lengths at terminals
- Stainless steel for kitchen exhaust, corrosive environments

**Pressure drop budget:**

Typical system breakdown (in. w.g.):
- Duct friction: 0.3-0.6
- Fittings and transitions: 0.2-0.4
- Coils: 0.3-0.8
- Filters: 0.2-0.5 (clean), 0.5-1.2 (dirty)
- Terminal devices: 0.05-0.15
- Total external static: 1.5-3.0

### Piping System Design

**Flow calculations:**

For hydronic systems:
- GPM = (Load in MBH × 1000) / (500 × ΔT)
- Standard ΔT: 10-20°F for heating, 10-16°F for chilled water

Pipe sizing criteria:
- Velocity: 4-8 ft/s for distribution mains
- Velocity: <4 ft/s for risers (noise control)
- Friction rate: 1-4 ft head/100 ft equivalent length
- Pressure drop budget: Typically 10-30 ft head total

**Material selection:**

Schedule 40 black steel:
- Most common for closed-loop hydronic
- Welded or threaded connections (2.5" transition point)
- Requires expansion compensation

Type L copper:
- Domestic water, condensate drains
- Brazed or press fittings
- Higher cost but corrosion-resistant

CPVC or PEX:
- Domestic water applications
- Lower installation cost
- Temperature limitations (180-200°F max)

**Insulation requirements:**

Chilled water piping:
- 1-2" closed-cell elastomeric foam
- Continuous vapor barrier (sealed seams)
- Prevents condensation and energy loss

Hot water piping:
- 1-2" fiberglass or mineral wool
- All-service jacket
- Reduces heat loss and maintains supply temperature

### Specialty Piping Systems

**Condensate drainage:**
- Gravity drains sized at 60 FPM maximum velocity
- 1/4" per foot minimum slope
- Trap depth = operating pressure + 1" minimum
- Overflow provisions for primary drains

**Refrigerant piping:**
- Suction, liquid, and hot gas line sizing per manufacturer
- Oil return velocity requirements (minimum 500 FPM)
- Insulation on suction lines
- Vibration isolation at compressors

**Steam and condensate:**
- Steam velocity: 4000-6000 FPM
- Condensate return: sized for gravity or pumped
- Drip legs at low points and ahead of control valves
- Expansion loops or expansion joints

## Control System Development

### System-Level Sequences

**Air handling unit sequence:**

Occupied mode:
1. Smoke dampers proven open
2. Supply fan starts after 5-second VFD delay
3. Return/exhaust fan starts with airflow tracking
4. Outdoor air damper modulates to maintain minimum ventilation
5. Mixed air temperature controlled via economizer sequence
6. Heating coil valve modulates to maintain discharge air temperature (45-55°F lockout prevents simultaneous heating/cooling)
7. Cooling coil valve modulates to maintain discharge air setpoint
8. Supply air static pressure resets based on zone demand (trim & respond)
9. Humidifier activates if space humidity <30% RH

Unoccupied mode:
1. System off unless space temperature falls below 55°F (freeze protection)
2. Night setback heating to 60°F
3. Optimal start calculates fan startup time

**Chilled water plant sequence:**

Normal operation:
- Lead chiller starts when any AHU calls for cooling
- Condenser water pump starts with chiller interlock
- Cooling tower fan stages based on condenser water temperature
- Primary chilled water pumps run continuously (primary-only) or on chiller status (primary-secondary)
- Secondary pumps modulate speed to maintain differential pressure
- Chiller stages based on supply temperature or system load
- Lead/lag rotation on runtime or weekly schedule

Reset strategies:
- Chilled water supply temperature reset from 42°F to 54°F based on outdoor air temperature
- Condenser water temperature reset to improve chiller efficiency
- Differential pressure setpoint reset based on valve positions

### Zone-Level Control

**VAV terminal unit:**

Standard cooling sequence:
1. Damper modulates from minimum (ventilation) to maximum based on space temperature
2. At minimum position, damper holds for X minutes before entering deadband
3. Deadband prevents simultaneous heating and cooling (typically 2-4°F)
4. Reheat coil activates below heating setpoint
5. Coil modulates proportionally to maintain setpoint

Advanced features:
- Occupancy-based setpoint adjustment
- Effective occupied/unoccupied schedules per zone
- Trim & respond minimum airflow reset (DCV integration)
- Morning warmup mode (maximum heat, minimum airflow)
- Supply air temperature compensation

**Radiant panel control:**

Zoning strategy:
- Water temperature modulated based on space temperature and outdoor reset
- Low supply temperatures (90-110°F) for comfort and condensation prevention
- Individual zone valves or injection mixing
- Dew point monitoring in cooling applications

### Integration Requirements

**BACnet network architecture:**
- MS/TP trunk for field controllers (VAV, FCU)
- BACnet/IP backbone for supervisors, servers, workstations
- Object naming conventions (site.building.system.point)
- Standard point types (AV, BV, AI, BI, AO, BO)

**Trend logging:**
- Critical points logged at 15-minute intervals
- Calculated values (energy, efficiency) logged hourly
- Alarm events logged on change-of-state
- Data storage for minimum 2-year history

**Alarm management:**
- Priority levels (critical, warning, informational)
- Notification via email, SMS for critical alarms
- Alarm suppression during maintenance
- Acknowledgment and reset procedures

## Multidisciplinary Coordination

### Architectural Coordination

**Space allocations:**
- Mechanical room sizes confirmed (equipment, clearances, maintenance)
- Shaft sizes for vertical distribution
- Ceiling plenum depths for ductwork, piping, diffusers
- Roof penetration locations and curb details
- Louver locations and sizing (free area, face velocity)

**Aesthetic considerations:**
- Exposed ductwork in design-exposed ceilings
- Diffuser types matching ceiling grid (2×2, 2×4, linear)
- Grille and register finishes coordinating with interiors
- Equipment screening on roofs or grade

### Structural Coordination

**Equipment loads:**
- Point loads at roof units (operating + rigging weights)
- Seismic bracing requirements per ASCE 7
- Vibration isolation specifications
- Suspended equipment support (AHU, piping risers)

**Penetrations:**
- Core drilling vs. cast-in sleeves
- Structural beam web penetration limits
- Fire-rated assemblies and firestopping

### Electrical Coordination

**Power requirements:**
- Voltage, phase, hertz for all equipment
- Minimum circuit ampacity (MCA)
- Maximum overcurrent protection (MOCP)
- Disconnect locations and types (fused, non-fused)
- Motor control center specifications

**Control power:**
- 120V circuits for controllers, actuators, sensors
- UPS backup for critical control systems
- Panel locations and homerun routing

### Plumbing Coordination

**Domestic water interfaces:**
- Heating coil makeup water connections
- Humidifier water supply with treatment
- Cooling tower makeup and blowdown
- Condensate drain connections to sanitary or storm

**Natural gas coordination:**
- Gas pressure available at meter
- Regulator requirements for equipment
- Pipe sizing for simultaneous loads
- Seismic shutoff valve locations

## Cost Estimation

### DD Phase Estimating Methods

**Unit cost approach:**

Equipment costs:
- Cost per ton for chillers, RTUs
- Cost per CFM for air handlers, exhaust fans
- Cost per MBH for boilers, furnaces
- Include manufacturer's representative quotes for major items

Distribution costs:
- Cost per linear foot by duct size
- Cost per linear foot by pipe size and insulation
- Diffuser/grille costs per unit
- Terminal unit costs per box

Labor factors:
- Installation labor as percentage of equipment (30-60%)
- Regional wage rate adjustments
- Project complexity multipliers (high-rise, occupied renovation)

**Historical project database:**
- Cost per square foot by building type
- Adjust for inflation (ENR Construction Cost Index)
- Regional cost multipliers (New York vs. Atlanta)
- Scope differences (4-pipe vs. 2-pipe systems)

### Cost Breakdown Structure

Typical HVAC cost distribution:

| Category | Percentage |
|----------|-----------|
| Chilled water plant | 15-25% |
| Heating plant | 5-15% |
| Air handling equipment | 20-30% |
| Ductwork and insulation | 15-25% |
| Piping and insulation | 10-15% |
| Terminal devices | 8-12% |
| Controls and automation | 8-15% |
| Testing, balancing, commissioning | 2-5% |
| General conditions and profit | 10-18% |

### Value Engineering Preparation

Identify potential VE targets:

**High-impact, moderate-cost items:**
- Heat recovery (energy vs. first cost payback)
- Premium efficiency equipment (ROI analysis)
- Control system sophistication (basic DDC vs. advanced analytics)

**Alternative systems:**
- VRF vs. traditional ducted systems
- Radiant vs. all-air conditioning
- Geothermal heat pumps vs. conventional plant

**Design optimizations:**
- Right-sizing equipment (avoid over-capacity)
- Distribution efficiency (duct vs. pipe, insulation levels)
- Zoning strategies (perimeter vs. interior)

## Deliverables

### Drawing Set (50-75% Complete)

**Mechanical plans:**
- Equipment locations with dimensions to grid lines
- Ductwork routing with sizes (main and branch)
- Piping routing with sizes (supply, return, condensate)
- Diffuser locations with CFM callouts
- Refrigerant line routing for split systems

**Details:**
- Equipment connection details (duct, pipe, drain, power)
- Typical duct and pipe support details
- Vibration isolation specifications
- Penetration through fire-rated assemblies

**Schedules:**
- Air handling unit schedule (capacity, static, coils, fans)
- Exhaust fan schedule (CFM, static, hp, location)
- Pump schedule (GPM, head, hp, impeller)
- Heating/cooling equipment schedule (capacity, fuel, efficiency)

**Diagrams:**
- Refrigeration cycle (P-h diagram or flow schematic)
- Hydronic flow diagrams (primary-secondary, distributed pumping)
- Control diagrams (system-level sequences)
- Ventilation airflow diagrams (supply, return, exhaust, outdoor air)

### Specifications Outline

Division 23 - HVAC (Outline format):

- General requirements (submittals, warranties, coordination)
- Equipment specifications (performance, construction, accessories)
- Ductwork and accessories (materials, construction standards, accessories)
- Piping and specialties (materials, joining methods, insulation)
- Controls and instrumentation (BAS architecture, sequences, interfaces)
- Testing and commissioning requirements

### Basis of Design Narrative

Document key decisions:

**System selection rationale:**
- Why selected system type (VAV, FCU, radiant, etc.)
- Equipment efficiency targets and energy code compliance
- Redundancy and reliability provisions
- Maintenance and operational considerations

**Design criteria summary:**
- Indoor and outdoor design conditions
- Ventilation rates and standards applied
- Sound and vibration criteria
- Filtration and indoor air quality targets

**Energy analysis:**
- Annual energy consumption (kBTU/ft²-yr)
- Energy cost index ($/ft²-yr)
- Comparison to baseline or code minimum
- Renewable energy integration

## Quality Control Review

### Design Review Checklist

**Load calculations:**
- Envelope inputs match architectural drawings
- Internal loads verified with electrical, lighting
- Ventilation rates calculated per ASHRAE 62.1
- Simultaneous vs. block loads applied correctly

**Equipment sizing:**
- Capacity margins appropriate (typically 5-15%)
- Not grossly oversized (>25% margin)
- Part-load performance considered
- Redundancy provisions clearly identified

**Distribution systems:**
- Pressure drop within acceptable limits
- Velocities meet noise criteria
- Materials suitable for application and code
- Expansion compensation provided

**Coordination:**
- No conflicts with structure, architectural elements
- Adequate clearances for installation and maintenance
- Roof loads verified with structural
- Electrical loads confirmed with power available

**Code compliance:**
- Energy code (ASHRAE 90.1, IECC, or local)
- Mechanical code (IMC, UMC, or local amendments)
- Fire and life safety (IBC, NFPA)
- Accessibility (ADA requirements for thermostats, controls)

### Constructability Review

Engage contractor or construction manager for input:

- Equipment rigging paths to final locations
- Prefabrication opportunities (duct, pipe assemblies)
- Material lead times (chillers, custom AHU, controls)
- Phasing and temporary systems
- Site access and laydown areas

## Next Phase Preparation

### Construction Document Readiness

Items to finalize before CD phase:

- Owner approval of all major equipment selections
- Energy model results accepted and code compliance confirmed
- Cost estimate within budget (or VE implemented)
- Coordination drawings completed (3D model or 2D overlays)
- All RFIs from DD phase review closed

### Specification Development

Transition outline to full specifications:

- Three-part format (General, Products, Execution)
- Performance vs. prescriptive specifications
- Approved manufacturers (or approved equal process)
- Testing and acceptance criteria
- Warranty requirements

### Detail and Standard Development

Standardize repetitive details:

- Duct and pipe supports at spacing intervals
- Equipment connection diagrams by type
- Control schematics for terminal units
- Seismic bracing typical details
- Penetration and firestopping standards

The DD phase establishes the technical foundation for successful construction. Thorough equipment selection, accurate sizing, multidisciplinary coordination, and constructability consideration at this stage prevent costly changes during construction documents and field installation.
