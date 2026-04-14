---
title: "Schematic Design Phase"
aliases: ["Schematic Design Phase"]
description: "HVAC schematic design phase including system concept development, preliminary load calculations, equipment space allocation, major equipment selection, budget estimation, and preliminary energy analysis for mechanical system design."
weight: 2
---

The schematic design (SD) phase establishes fundamental HVAC system concepts and confirms design feasibility. This phase translates owner requirements into preliminary technical solutions, establishes spatial requirements, and provides cost and energy consumption estimates for decision-making.

## Phase Objectives

The schematic design phase accomplishes:

1. **System concept selection** based on building type, owner requirements, and site constraints
2. **Preliminary load calculations** establishing system capacity requirements
3. **Major equipment identification** defining primary system components
4. **Space allocation** for mechanical rooms, shafts, and distribution paths
5. **Cost estimation** providing budget validation (±20-30% accuracy)
6. **Energy analysis** comparing system alternatives and establishing performance baselines

## System Concept Development

### System Selection Criteria

System concept selection evaluates:

**Building Characteristics:**
- Occupancy type and schedule
- Space function and layout
- Floor-to-floor height limitations
- Ceiling plenum availability
- Architectural constraints

**Performance Requirements:**
- Thermal comfort criteria
- Indoor air quality targets
- Humidity control needs
- Acoustical limitations
- Operational flexibility

**Zoning Considerations:**
- Thermal zone requirements
- Exposure variations (perimeter vs. interior)
- Schedule diversity
- Space pressurization needs
- Simultaneous heating and cooling loads

### Primary System Types

**All-Air Systems:**
- Variable air volume (VAV) with reheat
- Constant volume multizone
- Dual duct systems
- Single zone constant volume

Application: Office buildings, schools, retail spaces requiring centralized control and high ventilation rates.

**Air-Water Systems:**
- Four-pipe fan coil units
- Chilled beams (active and passive)
- Water source heat pumps
- Radiators with ventilation systems

Application: Hotels, residential buildings, perimeter zones requiring individual control.

**All-Water Systems:**
- Hydronic radiant panels
- Baseboard radiation
- Unit heaters
- Trench heaters

Application: Industrial spaces, warehouses, perimeter heating applications.

**Refrigerant-Based Systems:**
- Variable refrigerant flow (VRF)
- Packaged terminal units
- Split systems
- Rooftop units

Application: Tenant spaces, renovations, buildings without central plant capacity.

### Distribution System Concepts

**Central vs. Distributed:**

Central plant systems concentrate equipment in mechanical rooms, distributing conditioned air or water throughout the building. Advantages include maintenance access, equipment efficiency, and acoustical isolation. Disadvantages include distribution losses, vertical shaft requirements, and single-point failure risk.

Distributed systems locate equipment throughout the building near served spaces. Advantages include reduced distribution, simplified zoning, and redundancy. Disadvantages include maintenance access challenges, space consumption, and acoustical concerns.

**Horizontal Distribution:**

Establish routing concepts for:
- Supply and return air ducts or piping
- Corridor ceiling vs. plenum distribution
- Above-ceiling vs. raised-floor pathways
- Coordination with structural systems
- Integration with electrical and plumbing systems

**Vertical Distribution:**

Define shaft requirements for:
- Main supply and return risers
- Equipment access and maintenance
- Future capacity expansion
- Fire and smoke separation
- Acoustic isolation between floors

## Preliminary Load Calculations

### Calculation Methodology

Schematic design load calculations use simplified methods providing ±15-25% accuracy:

**Block Load Approach:**

Calculate loads for entire building or major zones rather than individual spaces. This method establishes overall system capacity without detailed room-by-room analysis.

**Cooling Load Components:**

External loads:
- Envelope transmission: Q = U × A × CLTD
- Solar radiation through glazing: Q = A × SHGC × SC × CLF
- Infiltration: Q = 1.1 × CFM × ΔT + 4840 × CFM × Δω

Internal loads:
- Occupant sensible: Q = N × 250 BTU/hr (typical office)
- Occupant latent: Q = N × 200 BTU/hr (typical office)
- Lighting: Q = W × 3.41 × BF × CLF
- Equipment: Q = W × 3.41 × Usage Factor × CLF
- Miscellaneous sources

Ventilation:
- Outdoor air sensible: Q = 1.1 × CFM × (To - Ti)
- Outdoor air latent: Q = 4840 × CFM × (ωo - ωi)

**Heating Load Components:**

Envelope losses:
- Transmission: Q = U × A × ΔT
- Infiltration: Q = 1.1 × CFM × ΔT

Ventilation heating:
- Outdoor air heating: Q = 1.1 × CFM × (Ti - To)

Humidification (if required):
- Moisture addition: Q = CFM × Δω × 4840 BTU/lb-water

### Design Conditions

**Outdoor Conditions:**

Reference ASHRAE climatic design data:
- Summer: 0.4%, 1%, or 2% dry-bulb and mean coincident wet-bulb
- Winter: 99.6% or 99% dry-bulb
- Humidity ratios at design conditions

Selection depends on system reliability requirements and operational cost considerations.

**Indoor Conditions:**

Establish target conditions:
- Summer: 75°F ± 2°F, 50% RH ± 10%
- Winter: 70°F ± 2°F, 30% RH minimum
- Special requirements for specific space types

**Diversity Factors:**

Apply appropriate diversity to account for non-simultaneous operation:
- Occupancy: 0.7-0.9 (office buildings)
- Lighting: 0.8-1.0 (depends on control strategy)
- Equipment: 0.5-0.8 (depends on space type)
- System-level diversity: 0.85-0.95

### Load Calculation Software

Utilize simplified calculation tools:
- ASHRAE block load calculator
- eQuest preliminary design mode
- Carrier HAP quick load
- Trane TRACE 700 schematic module
- RTS method spreadsheets

## Equipment Space Allocation

### Mechanical Room Sizing

**Central Equipment Spaces:**

Estimate floor area requirements:

Boiler rooms:
- 1.5-2.5 SF per MBH input capacity
- Minimum clearances: 3 ft sides, 6 ft front, 4 ft rear
- Combustion air openings
- Fuel supply access

Chiller rooms:
- 2.0-3.0 SF per ton cooling capacity
- Tube pull space: 1.5 × tube length
- Maintenance access around equipment
- Refrigerant monitoring and ventilation

Air handling unit rooms:
- 3-4 times AHU footprint for access and ductwork
- Minimum ceiling height: equipment height + 3 ft
- Filter and coil access clearances
- Ductwork and piping transitions

Pump rooms:
- 50-100 SF per pump (depending on size)
- Clearances for motor removal
- Pipe and valve access
- Future expansion capacity

**Vertical Shafts:**

Size shafts for:
- Main supply risers: 0.3-0.5 SF per 1000 CFM
- Main return risers: 0.3-0.5 SF per 1000 CFM
- Hydronic risers: 0.1-0.2 SF per 100 GPM
- Access doors every 3-4 floors
- Fire damper locations

**Equipment Locations:**

Evaluate placement options:

Rooftop:
- Advantages: Outdoor air access, sound isolation, no building space consumption
- Disadvantages: Weather exposure, structural reinforcement, aesthetic impact

Basement:
- Advantages: Structural support, sound isolation, outdoor air via wells
- Disadvantages: Flooding risk, excavation cost, natural light limitation

Intermediate floors:
- Advantages: Reduced distribution distances, stacked shaft alignment
- Disadvantages: Floor space consumption, structural loading, noise transmission

Outdoor pads:
- Advantages: Easy access, no building space, simple installation
- Disadvantages: Weather exposure, security concerns, visual impact, noise

## Major Equipment Selection

### Heating Equipment

**Boilers:**

Preliminary selection based on:
- Fuel type: natural gas, fuel oil, electric
- Configuration: fire-tube, water-tube, condensing
- Capacity: total heating load × 1.15-1.25 safety factor
- Efficiency: AFUE 80-95% (non-condensing), 90-98% (condensing)
- Quantity: redundancy requirements (N+1 or 2×50%)

Typical sizing:
- Input capacity: output ÷ efficiency
- Footprint: estimate from manufacturer data
- Flue requirements: diameter based on input capacity

**Heat Pumps:**

Air-source heat pumps:
- Capacity: match cooling load, verify heating capacity at design conditions
- COP heating: 2.5-3.5 at 47°F, 1.5-2.5 at 17°F
- Supplemental heat: electric resistance or fossil fuel backup

Water-source heat pumps:
- Capacity: 0.5-2.0 tons per unit (varies by application)
- Loop temperature: 60-90°F operating range
- Boiler and cooling tower: size for simultaneous loads

### Cooling Equipment

**Chillers:**

Selection parameters:
- Capacity: total cooling load × 1.10-1.20 safety factor
- Efficiency: 0.5-0.65 kW/ton (water-cooled), 0.9-1.2 kW/ton (air-cooled)
- Configuration: air-cooled, water-cooled, evaporative-cooled
- Compressor type: centrifugal, screw, scroll
- Refrigerant: R-134a, R-513A, R-1233zd(E), R-515B

Preliminary sizing:
- Tons = sensible load + latent load + duct gain + safety factor
- GPM chilled water = (tons × 24) ÷ (ΔT × 500)
- Condenser water GPM = (tons × 30) ÷ (ΔT × 500)

**Cooling Towers:**

Estimate parameters:
- Capacity: chiller heat rejection + compressor power
- Approach: 7-10°F (counterflow), 5-7°F (crossflow)
- Range: 10-20°F (typically 10-15°F)
- GPM: match condenser water flow
- Type: induced draft, forced draft, crossflow, counterflow

### Air Handling Equipment

**Air Handling Units:**

Size based on:
- Airflow: CFM = sensible load ÷ (1.1 × ΔT)
- Supply temperature: 55-58°F (cooling), 95-105°F (heating)
- Face velocity: 400-500 FPM (coils), 500 FPM (filters)
- Pressure drop: 2-4 in. w.g. (internal), 2-6 in. w.g. (external)

Component sizing:
- Cooling coil: 4-6 rows, 8-12 fins per inch
- Heating coil: 2-4 rows, 8-10 fins per inch
- Filters: MERV 8-13, 300-500 FPM face velocity
- Fan: forward-curved, backward-inclined, or airfoil

**Package Units:**

Rooftop units:
- Capacity: 3-150 tons (standard sizes)
- Efficiency: 10-14 IEER (air-cooled)
- Configuration: single-zone or VAV
- Supply air: constant or variable volume

Split systems:
- Capacity: 1.5-5 tons (typical residential/light commercial)
- SEER: 13-21 (cooling efficiency)
- HSPF: 8-10 (heating efficiency)
- Configuration: single-stage, two-stage, variable-speed

### Pump Selection

**Chilled Water Pumps:**

Preliminary sizing:
- Flow rate: GPM = (tons × 24) ÷ (ΔT × 500)
- Temperature difference: 10-14°F (12°F typical)
- Head: estimate 50-100 ft for distribution + equipment drops
- Control: variable speed with pressure sensor

**Condenser Water Pumps:**

Sizing parameters:
- Flow rate: GPM = (tons × 30) ÷ (ΔT × 500)
- Temperature rise: 10-20°F (10°F typical)
- Head: estimate 40-80 ft including tower lift
- Control: constant speed or variable speed

**Heating Water Pumps:**

Design values:
- Flow rate: GPM = (MBH × 500) ÷ (ΔT × 500)
- Temperature drop: 20-40°F (20°F typical high-temp, 10°F low-temp)
- Head: estimate 40-100 ft for distribution + coils
- Control: variable speed with differential pressure sensor

## Budget Estimation

### Cost Estimating Methods

**Unit Cost Method:**

Apply costs per building area:
- Office buildings: $8-$15/SF
- Healthcare: $25-$40/SF
- Schools: $10-$18/SF
- Retail: $6-$12/SF
- Laboratories: $40-$80/SF

Ranges reflect system complexity, building size, and regional variations.

**System Component Method:**

Estimate major component costs:

Heating equipment:
- Boilers: $15-$30 per MBH input
- Heat pumps: $1,200-$2,000 per ton

Cooling equipment:
- Air-cooled chillers: $800-$1,200 per ton
- Water-cooled chillers: $600-$1,000 per ton
- Cooling towers: $150-$300 per ton
- Package rooftop units: $1,000-$1,500 per ton

Air distribution:
- Air handling units: $3-$6 per CFM
- Ductwork: $8-$15 per SF served
- Diffusers and grilles: $100-$300 each

Hydronic systems:
- Pumps: $200-$500 per HP
- Piping: $20-$40 per linear foot (installed)
- Terminal units: $800-$1,500 per unit

Controls:
- DDC system: $2-$5 per SF
- VAV boxes with controls: $1,500-$2,500 each

**Contingency Factors:**

Include appropriate contingencies:
- Design contingency: 15-25% (schematic phase)
- Escalation: 3-5% per year to construction midpoint
- Geographic adjustment: regional cost indices

### Cost Documentation

Prepare preliminary cost estimate including:
- Basis of estimate (building area, system type, equipment counts)
- Unit costs and quantities
- Subtotals by system category
- Contingencies and markups
- Total construction cost
- Comparison to budget allocation

## Preliminary Energy Analysis

### Analysis Objectives

Schematic phase energy analysis establishes:
- Baseline energy consumption and cost
- System alternative comparison
- Energy code compliance path
- Owner's sustainability goals feasibility

### Modeling Methodology

**Simplified Analysis:**

Use bin method or degree-day calculations:
- Annual heating load: HDD × 24 × UA × efficiency factor
- Annual cooling load: CDD × 24 × UA × efficiency factor
- Equipment energy: loads ÷ equipment efficiency × operating hours

**Simulation Tools:**

Employ preliminary energy modeling:
- eQuest quick mode
- Trace 700 early design
- IES VE conceptual design module
- Carrier HAP energy analysis

Input minimal detail:
- Building envelope U-values and SHGC
- System types and efficiencies
- Occupancy schedules
- Lighting power density
- Equipment power density
- HVAC system operating parameters

### System Comparison

**Performance Metrics:**

Compare alternatives using:
- Annual energy consumption (kBTU/SF-yr)
- Energy Use Intensity (EUI)
- Energy cost ($/SF-yr)
- Peak demand (W/SF)
- Source energy consumption
- Carbon emissions (lb CO₂/SF-yr)

**System Alternatives:**

Evaluate options:

Base case: code-minimum system
- Standard efficiency equipment
- Minimum insulation and glazing performance
- Required ventilation rates

Alternative 1: improved efficiency
- High-efficiency equipment (10-20% improvement)
- Enhanced envelope performance
- Heat recovery systems

Alternative 2: advanced systems
- Variable refrigerant flow
- Dedicated outdoor air systems
- Energy recovery ventilation
- Demand-controlled ventilation

Alternative 3: renewable integration
- Ground-source heat pumps
- Solar thermal domestic hot water
- Photovoltaic offset
- Combined heat and power

### Life Cycle Cost Analysis

**Economic Evaluation:**

Perform simplified LCC analysis:

First cost:
- Equipment and installation
- Design and commissioning
- Incremental envelope improvements

Operating costs:
- Annual energy consumption × utility rates
- Maintenance cost estimates
- Equipment replacement reserves

Analysis period: 15-25 years

Economic metrics:
- Simple payback period
- Net present value (NPV)
- Internal rate of return (IRR)
- Savings-to-investment ratio (SIR)

Discount rate: 3-5% real (excluding inflation)

## Deliverables

### Drawing Requirements

Produce schematic design drawings:

**Mechanical Plans (1/16" or 1/8" scale):**
- Major equipment locations and sizes
- Primary ductwork and piping mains
- Mechanical room layouts
- Vertical shaft locations
- Outdoor equipment placement
- Coordination with architectural and structural systems

**Riser Diagrams:**
- Vertical distribution concept
- Main supply and return routes
- Equipment connections
- Control zones

**Equipment Schedules:**
- Major equipment list with preliminary capacities
- Approximate dimensions and weights
- Utility requirements (electrical, gas, water)
- Performance specifications

### Technical Documentation

Prepare written descriptions:

**Basis of Design Narrative:**
- System selection rationale
- Design criteria and parameters
- Load calculation summary
- Equipment selection basis
- Energy analysis results
- Code compliance approach

**Specifications Outline:**
- Division 23 sections list
- Performance criteria
- Quality standards referenced
- Installation requirements overview

**Cost Estimate:**
- Component-level cost breakdown
- Comparison to budget
- Value engineering opportunities identified

### Owner Review Package

Compile submittal including:
- Design drawings
- Basis of design narrative
- Load calculation summary
- Equipment schedules
- Cost estimate
- Energy analysis comparison
- Design alternatives evaluation
- Project schedule implications

## Coordination Requirements

### Architectural Integration

Coordinate with architectural design:
- Ceiling heights and mechanical clearances
- Shaft locations and sizes
- Mechanical room locations
- Equipment access and egress
- Louver and grille locations
- Roof penetrations and equipment placement
- Acoustical criteria

### Structural Coordination

Provide structural team with:
- Equipment weights and locations
- Mechanical room live loads
- Roof equipment support requirements
- Pipe and duct support loads
- Seismic requirements
- Vibration isolation details

### Electrical Coordination

Define electrical requirements:
- Voltage and phase for major equipment
- Transformer and switchgear capacity
- Emergency power requirements
- Control power needs
- Lighting and receptacle coordination in mechanical spaces

### Plumbing Coordination

Coordinate with plumbing design:
- Domestic water heating method
- Condensate drainage
- Makeup water connections
- Backflow prevention
- Floor drains in mechanical rooms

## Design Review and Approval

### Internal Review

Conduct design team reviews:
- Load calculation verification
- System concept appropriateness
- Equipment sizing reasonableness
- Cost estimate accuracy
- Constructability assessment
- Code compliance verification

### Owner Review Meeting

Present design concept:
- System description and rationale
- Preliminary drawings explanation
- Cost and schedule implications
- Energy performance projections
- Design alternatives discussion
- Outstanding decisions requiring owner input

### Authority Having Jurisdiction

Engage code officials:
- Preliminary code review meeting
- Ventilation rate confirmation
- Energy code compliance path
- Fire and life safety coordination
- Special system requirements

Obtain feedback before proceeding to design development.

## Schematic Design Checklist

Verify completion of:
- [ ] Owner requirements documented and incorporated
- [ ] System concept selected and approved
- [ ] Preliminary load calculations completed
- [ ] Major equipment identified and sized
- [ ] Mechanical room locations and sizes established
- [ ] Shaft and distribution routing concepts defined
- [ ] Cost estimate prepared and within budget
- [ ] Energy analysis comparing alternatives completed
- [ ] Drawings at appropriate level of detail
- [ ] Basis of design narrative prepared
- [ ] Coordination with other disciplines completed
- [ ] Owner review and approval obtained
- [ ] Design schedule maintained

The schematic design phase establishes HVAC system fundamentals that guide subsequent design development and construction documentation. Thorough concept evaluation and stakeholder alignment during this phase prevent costly revisions later in the project delivery process.
