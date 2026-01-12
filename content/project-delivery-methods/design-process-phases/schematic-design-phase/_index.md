---
title: "Schematic Design Phase"
description: "Comprehensive guide to HVAC schematic design phase including system concept development, preliminary load calculations, equipment space allocation, major equipment selection, energy analysis, and schematic drawings for HVAC professionals"
weight: 1
---

The schematic design (SD) phase establishes the fundamental HVAC system concepts and approaches that will define the project through subsequent design phases. This phase translates Owner's Project Requirements (OPR) and architectural concepts into viable HVAC strategies, providing sufficient technical detail to support cost estimating and design decision-making.

## Phase Objectives and Deliverables

The schematic design phase produces:

- System concept narratives with comparative analysis
- Preliminary load calculations (typically 15-20% accuracy)
- Major equipment schedules with capacities
- Space allocation diagrams for mechanical rooms
- Single-line schematic HVAC diagrams
- Preliminary energy analysis
- Budget-level cost estimates (±25% accuracy)
- Basis of Design documentation

These deliverables enable the owner to evaluate system alternatives, understand first cost implications, and assess operational characteristics before committing to detailed design.

## System Concept Development

### Load Analysis Methodology

Preliminary load calculations during schematic design employ simplified methods appropriate to the conceptual nature of the phase:

**Cooling Load Estimation:**
- Envelope loads: U·A·ΔT calculations using assumed assembly values
- Internal gains: Area-based assumptions (W/ft² by space type)
- Ventilation loads: 1.1·CFM·ΔT + 4840·CFM·Δω
- Simultaneous diversity: Apply block load methods
- Safety factors: 10-15% for equipment sizing uncertainty

**Heating Load Estimation:**
- Transmission: U·A·ΔT for all envelope components
- Infiltration: Simplified air change method or area/perimeter method
- Humidification: If required, based on ventilation air and infiltration
- Pickup loads: Proportional estimates based on building mass

For block load calculations during SD phase:

```
Q_total = Q_envelope + Q_internal + Q_ventilation + Q_infiltration

Where:
Q_envelope = Σ(U·A·CLTD) for walls, roof, glazing
Q_internal = (People·ΔT·1.1·CFM/person) + (Lights·W/ft²·A) + (Equipment·W/ft²·A)
Q_ventilation = 1.1·CFM_oa·ΔT + 4840·CFM_oa·Δω
```

The coefficient 1.1 derives from ρ·c_p = 1.08 Btu/(hr·ft³·°F) for sensible heat, and 4840 for latent heat represents the product of air density, specific heat of vaporization, and unit conversions.

### System Selection Criteria

HVAC system selection during schematic design evaluates multiple alternatives against weighted criteria:

**Performance Factors:**
- Thermal control capability (zone-level vs. space-level)
- Indoor air quality delivery (ventilation effectiveness)
- Acoustical performance (NC/RC criteria compliance)
- Humidity control precision (if critical)
- Space temperature stratification potential

**Economic Considerations:**
- First cost (equipment + installation + infrastructure)
- Operating costs (energy + maintenance + replacement)
- Life-cycle cost analysis over evaluation period
- Utility incentives and rebates
- Future flexibility and expansion capability

**Physical Constraints:**
- Available mechanical space (equipment rooms, shafts, ceiling plenums)
- Structural load capacity for equipment
- Architectural coordination requirements
- Site constraints (outdoor equipment placement, louver locations)
- Code compliance paths

**Operational Requirements:**
- Maintenance accessibility and complexity
- Control system sophistication
- Part-load performance characteristics
- Redundancy requirements
- Operator skill level assumptions

### Comparative System Analysis

Present 2-3 viable system alternatives with quantitative comparison:

| Criterion | Weight | VAV with Reheat | Chilled Beam | Fan Coil + DOAS |
|-----------|--------|-----------------|--------------|-----------------|
| First Cost ($/ft²) | 25% | $28-32 | $32-38 | $24-28 |
| Energy Cost ($/ft²/yr) | 30% | $2.40 | $1.85 | $2.10 |
| Acoustics (NC) | 15% | 38-42 | 30-35 | 35-40 |
| Zone Control | 20% | Excellent | Good | Excellent |
| Ceiling Height Impact | 10% | 18-24" | 12-16" | 14-18" |
| **Weighted Score** | - | **75** | **82** | **71** |

Document assumptions clearly: climate zone, occupancy type, building configuration, local labor rates, utility costs.

## Equipment Space Allocation

### Mechanical Room Sizing

Schematic design establishes mechanical room areas using equipment-based methods:

**Central Plant Rooms:**
- Chiller plant: 0.15-0.25 ft²/ton (includes chillers, pumps, expansion tanks, VFDs, clearances)
- Boiler plant: 0.08-0.15 ft²/MBH (includes boilers, pumps, expansion, fuel train)
- Air handler rooms: Plan for 1.5x equipment footprint for maintenance access
- Add 20-30% circulation and service area beyond equipment footprints

**Vertical Distribution:**
- Mechanical shafts: Size for maximum floor supply/return risers plus 40% future
- Typical sizing: 1.0-1.5 ft² per 10,000 ft² served per floor
- Stack supply and return shafts separately for balancing flexibility
- Coordinate shaft locations with structural column grid

**Equipment Access:**
- Door sizes: Minimum 6'-0" × 8'-0" for central plant access
- Removal routes: Verify path from loading dock to mechanical rooms
- Rigging provisions: Coordinate structural support for equipment replacement
- Clearances: ASHRAE Guideline 1.1 maintenance access requirements

### Ceiling Space Coordination

Establish ceiling plenum depth requirements:

```
Plenum Depth = Duct_depth + Pipe_depth + Electrical_depth + Clearance + Structure

Typical VAV System:
- Supply duct: 24-36" for mains (aspect ratio 4:1 maximum)
- Return duct/plenum: 18-24" if ducted returns
- Sprinkler piping: 4-6" below structure
- Electrical: 6-12" for conduit/cable tray
- Minimum clearance: 3-6" between systems
Total: 36-48" below structure to ceiling
```

Coordinate with architectural reflected ceiling plans to identify congestion zones and required soffits.

## Major Equipment Selection

### Capacity Determination

Size central plant equipment using block loads with appropriate diversity and safety factors:

**Chiller Capacity:**
```
Chiller Tons = (Peak Block Load / Diversity) × Safety Factor

Where:
Diversity = 0.85-0.95 for multiple zones
Safety Factor = 1.10-1.15 for load estimate uncertainty

For redundancy: N+1 configuration
Each chiller = Total Load / (N chillers) × 1.0
```

**Boiler Capacity:**
```
Boiler MBH = Peak Heating Load + Pickup Load + Piping Loss

Pickup Load = 0.20-0.30 × Steady State Load (depends on building mass)
Piping Loss = 0.10-0.15 × Steady State Load
For N+1 redundancy: Size each = Total / (N boilers)
```

**Air Handler Sizing:**
```
CFM = Sensible Load / (1.08 × ΔT)

Where ΔT = 18-22°F for cooling (schematic assumption)
      ΔT = 40-70°F for heating

External Static Pressure = Filter + Coil + Duct + Terminal + Safety
Typical SD estimate: 2.5-4.0 inches w.g. total
```

### Equipment Type Selection

Document preliminary equipment selections with key performance parameters:

**Chillers:**
- Type: Water-cooled centrifugal, air-cooled screw, magnetic bearing, etc.
- Full-load efficiency: kW/ton or COP
- Part-load performance: IPLV or NPLV
- Refrigerant type and charge volume
- Physical dimensions and weight

**Boilers:**
- Type: Condensing, non-condensing, fire-tube, water-tube
- Efficiency: Combustion efficiency and AFUE
- Turndown ratio capability
- Emissions: NOx, CO levels (if applicable)
- Fuel type and consumption rate

**Air Handlers:**
- Configuration: Draw-through, blow-through, custom
- Fan type: Plenum, housed, AFMS
- Coil rows: Cooling (6-8 row typical), heating (1-2 row)
- Filter type: MERV rating and pressure drop
- Casing construction: Double-wall insulated

## Budget Development

### Cost Estimating Methods

Schematic design cost estimates employ parametric methods:

**Area-Based Estimating:**
```
HVAC Cost = Area × ($/ft² factor) × Location Multiplier × Escalation

Where $/ft² varies by:
- Building type (office: $20-30, hospital: $45-65, lab: $60-90)
- System type (VAV +$0, radiant +$8-12, displacement +$5-8)
- Climate zone (extreme climates +10-20%)
```

**System Component Method:**
- Central plant: $/ton for cooling, $/MBH for heating
- Distribution: $/CFM for ductwork and air devices
- Terminal units: $/unit or $/CFM
- Controls: % of equipment cost (12-18% typical)
- Testing/commissioning: 1-3% of construction cost

**Cost Breakdown Structure:**
- Equipment: 40-50%
- Labor: 35-45%
- Materials (pipe, duct, supports): 10-15%
- Controls: 5-8%
- Testing and commissioning: 2-4%

Apply geographic cost indices from RSMeans, Dodge, or regional data.

### Life-Cycle Cost Analysis

Perform simplified LCC to inform system selection:

```
LCC = First Cost + PW(Operating Costs) + PW(Maintenance) - PW(Salvage)

Present Worth Factor = [(1 + i)^n - 1] / [i(1 + i)^n]

Where:
i = real discount rate (typically 3-5%)
n = evaluation period (20-25 years for HVAC)
```

Operating cost components:
- Energy: $/kWh × annual consumption × escalation
- Demand charges: $/kW-month × peak demand × 12
- Maintenance: % of first cost (typically 2-4% annually)
- Major replacements: Present worth of equipment replacement at mid-life

Document sensitivity to key assumptions (energy cost escalation, discount rate, equipment life).

## Energy Analysis

### Schematic Energy Modeling

Preliminary energy analysis during SD establishes baseline performance and evaluates alternatives:

**Modeling Approach:**
- Single-block or limited-zone models appropriate for SD
- Envelope: Representative wall/roof/glazing assemblies
- Lighting: Area-based assumptions (W/ft²)
- Equipment: Plug load density by space type
- Occupancy: Peak and schedule assumptions
- HVAC: System type with representative efficiencies

**Baseline Performance:**
Establish energy use intensity (EUI) relative to benchmarks:

```
EUI = Annual Energy Use (kBtu) / Gross Floor Area (ft²)

Typical ranges by building type:
- Office: 50-80 kBtu/ft²/yr
- Retail: 60-100 kBtu/ft²/yr
- School: 55-85 kBtu/ft²/yr
- Hospital: 200-350 kBtu/ft²/yr
```

**Energy Cost Index (ECI):**
```
ECI = Annual Energy Cost ($) / Gross Floor Area (ft²)

Accounts for different utility rate structures and fuel costs
More meaningful than EUI for owner decision-making
```

### Energy Conservation Strategies

Evaluate energy efficiency measures (EEMs) with incremental cost-effectiveness:

**High-Performance HVAC Systems:**
- Economizer cycles: Free cooling when OA < RA temperature
- Heat recovery: Sensible or total energy recovery (ERV)
- Variable-flow systems: VFD on pumps, fans for part-load efficiency
- High-efficiency equipment: Premium efficiency chillers, boilers, motors

**Passive Strategies:**
- Envelope optimization: Insulation, glazing performance, thermal mass
- Solar control: Shading, glazing orientation, external devices
- Natural ventilation: Where climate and program permit
- Daylighting integration: Reduced lighting loads and heat gain

**Cost-Effectiveness Metrics:**
```
Simple Payback = Incremental First Cost / Annual Energy Savings

If SPB < 7-10 years → Typically cost-effective
If SPB > 15 years → Requires non-energy justification

For incentive programs, calculate:
Savings-to-Investment Ratio (SIR) = PW(Savings) / First Cost
SIR > 1.0 → Cost-effective over analysis period
```

### Energy Code Compliance

Verify preliminary design meets or exceeds minimum code requirements:

**Performance Path (ASHRAE 90.1):**
- Proposed building EUI ≤ Baseline building EUI
- Model both using identical assumptions except HVAC/envelope measures
- Document percent better than baseline (0%, 10%, 20%+ for certifications)

**Prescriptive Path:**
- Equipment efficiencies: Minimum COP, EER, AFUE, combustion efficiency
- Economizers: Required for cooling capacity > thresholds
- Duct/pipe insulation: R-values per Table 6.8.3
- Controls: Setback, deadband, demand control ventilation

For projects targeting green building certification (LEED, Living Building Challenge, Passive House), establish energy performance targets during SD:
- LEED: 5-20% better than ASHRAE 90.1 baseline
- Net Zero Energy: EUI targets of 20-35 kBtu/ft²/yr (office)
- Passive House: 4.75 kBtu/ft²/yr heating + cooling demand

## Schematic HVAC Drawings

### Drawing Content and Scale

Schematic design drawings communicate system concepts graphically:

**Floor Plan Drawings (1/16" = 1'-0" or 1/8" = 1'-0"):**
- Major equipment locations (AHUs, fan coils, unit ventilators)
- Mechanical room layouts with access paths
- Primary duct/pipe distribution routes (single-line)
- Terminal device locations (VAV boxes, diffusers in schematic grid)
- Control zones indicated
- Coordinate with architectural furniture/partition plans

**Single-Line Diagrams:**
- System flow from source to end use
- Major equipment with capacity labels
- Control sequences indicated schematically
- Diversity and coincidence factors noted
- Pressure/temperature conditions at key points

**Riser Diagrams:**
- Vertical distribution of supply/return systems
- Equipment served per floor
- Shaft sizes and locations
- Isolation valve locations
- Expansion provisions

**Mechanical Room Plans (1/4" = 1'-0"):**
- Equipment footprints with manufacturer's general dimensions
- Maintenance clearances per ASHRAE Guideline 1.1
- Access doors and equipment removal paths
- Floor drains and housekeeping pads
- Electrical/control panel locations

### Coordination Elements

Indicate key coordination requirements:

**Structural:**
- Equipment loads (psf or concentrated loads in lbs)
- Roof equipment curb locations
- Vibration isolation requirements
- Penetration sizes through floors/walls

**Architectural:**
- Louver locations and free areas
- Mechanical room door sizes
- Ceiling height requirements and soffits
- Equipment screening requirements

**Electrical:**
- Electrical room adjacency to mechanical rooms
- Preliminary voltage and phase (480V/3ph, 208V/3ph)
- Approximate connected loads (kW)
- Emergency power requirements

**Plumbing:**
- Condenser water connections to cooling towers
- Domestic water for humidification/makeup
- Drainage for coil condensate and equipment drains
- Fuel gas piping to boilers/generators

### Drawing Notes and Legends

Include standard schematic design notes:

1. "All quantities, capacities, and locations are preliminary and subject to refinement during design development."

2. "Equipment selections based on preliminary load calculations; verify during detailed design."

3. "Coordinate all mechanical equipment locations and distribution routing with structural, electrical, and plumbing systems."

4. "Contractor shall verify all field dimensions before fabrication."

5. Reference applicable design standards:
   - ASHRAE 90.1: Energy Standard for Buildings Except Low-Rise Residential Buildings
   - ASHRAE 62.1: Ventilation for Acceptable Indoor Air Quality
   - IMC: International Mechanical Code
   - Local amendments and jurisdictional requirements

## Design Review and Approval

### Internal Design Review

Conduct multidisciplinary design reviews to verify:

**HVAC System Integrity:**
- Load calculations reasonable for building type and climate
- Equipment capacities adequate with appropriate safety factors
- Distribution system can fit within architectural constraints
- Control strategies align with operational requirements

**Interdisciplinary Coordination:**
- Structural: Equipment loads within capacity, penetrations feasible
- Architectural: Space allocations adequate, aesthetic integration acceptable
- Electrical: Power availability, voltage compatibility, panel locations
- Plumbing: Water/drain connections feasible, no conflicts

**Code and Standard Compliance:**
- Energy code performance path or prescriptive compliance
- Ventilation rates per ASHRAE 62.1 or local code
- Mechanical code clearances and safety requirements
- Fire/life safety integration (smoke control, fire dampers)

### Owner Review Process

Present schematic design to owner stakeholders:

**Design Narrative:**
- System selection rationale with pros/cons of alternatives
- How system meets OPR and Basis of Design
- Operational characteristics and maintenance implications
- Energy performance relative to goals

**Cost Implications:**
- First cost estimate with contingency
- Annual operating cost projections
- Life-cycle cost comparison if alternatives presented
- Value engineering opportunities identified

**Schedule Impact:**
- Long-lead equipment requiring early procurement
- Phasing requirements for occupied renovations
- Utility coordination needs (service upgrades)

**Risk Assessment:**
- Technical risks (unproven technologies, tight fits)
- Cost risks (market volatility, incomplete information)
- Schedule risks (permitting, utility lead times)
- Mitigation strategies proposed

### Approval for Design Development

Obtain explicit owner approval to proceed:

1. **System Selection Approval:** Written acceptance of HVAC system type(s)

2. **Budget Acceptance:** Concurrence with cost estimate and contingency

3. **Space Planning Approval:** Acceptance of mechanical room sizes/locations

4. **Energy Performance:** Confirmation that preliminary energy analysis meets project goals

5. **Design Criteria Sign-off:** Approval of Basis of Design document

This approval establishes the design direction and prevents major changes during subsequent phases, which become increasingly costly to implement.

## Transition to Design Development

Prepare for the design development phase:

**Information Transfer:**
- Finalized system selection with owner approval documentation
- Preliminary load calculations and assumptions
- Equipment space allocations confirmed
- Energy analysis baseline established
- Budget baseline for cost control

**Outstanding Issues:**
- Items requiring further investigation or analysis
- Coordination challenges identified but not resolved
- Value engineering considerations for DD phase
- Owner decision points that will affect DD work

**Design Development Scope:**
- More detailed load calculations (room-by-room or zone-by-zone)
- Specific equipment selection with model numbers
- Ductwork and piping sizing calculations
- Detailed control system design
- Refined energy modeling
- Updated cost estimate (±15% accuracy target)

The quality and completeness of schematic design work directly impacts the efficiency of design development and the ultimate success of the constructed system. Thorough analysis, clear documentation, and effective communication during SD phase establish the foundation for project success.

## Documentation Standards

### Basis of Design Report

The schematic design Basis of Design includes:

**Design Criteria:**
- Indoor design conditions (temperature, humidity, pressure)
- Outdoor design conditions (summer/winter, coincident wet bulb)
- Ventilation rates by space type
- Filtration requirements (MERV levels)
- Acoustical criteria (NC/RC curves)

**System Description:**
- Narrative explanation of each HVAC system
- Major equipment list with capacities
- Distribution system overview
- Control system philosophy
- Sequence of operations (preliminary)

**Analysis Summary:**
- Load calculation methodology and results
- Energy analysis findings
- Life-cycle cost summary
- Code compliance approach

**Assumptions and Exclusions:**
- Design assumptions requiring verification
- Items excluded from scope
- Allowances (testing, commissioning, controls programming)
- Interfaces with other systems or phases

This document becomes the technical reference for the remainder of the design process and informs construction and commissioning activities.

