---
title: "Exterior Insulation Systems"
description: "Engineering analysis of continuous exterior insulation systems for wall assemblies including thermal bridge reduction, sheathing temperature control, condensation prevention, and moisture management strategies"
weight: 4
---

Exterior insulation systems provide continuous thermal resistance on the outside of wall structural elements, fundamentally altering the hygrothermal performance of building assemblies. By relocating the primary insulation layer to the exterior side of sheathing and structural framing, these systems warm the condensing surface temperatures, reduce thermal bridging, and shift dew point locations away from moisture-sensitive materials.

## Thermal Performance Principles

### Continuous Insulation Layer Function

Continuous insulation (ci) placed outboard of the wall structure creates an uninterrupted thermal barrier that addresses heat flow through both cavity and framing elements. The temperature distribution through the assembly shifts dramatically compared to cavity-only insulation.

**Temperature gradient modification:**

T_sheathing = T_interior - (R_cavity / (R_cavity + R_ci)) × (T_interior - T_exterior)

Where:
- T_sheathing = sheathing temperature at cavity/ci interface (°F)
- T_interior = interior air temperature (°F)
- T_exterior = exterior air temperature (°F)
- R_cavity = total R-value from interior to sheathing (hr·ft²·°F/Btu)
- R_ci = R-value of continuous exterior insulation (hr·ft²·°F/Btu)

**Design outcome:** As R_ci increases relative to R_cavity, the sheathing temperature approaches the interior temperature, reducing condensation risk.

### Thermal Bridge Mitigation

Framing members create thermal bridges that compromise overall wall R-value. The parallel path method quantifies this effect:

R_total = 1 / [(FF / R_framing) + ((1 - FF) / R_cavity)]

Where:
- FF = framing fraction (typically 0.15-0.25 for wood, 0.05-0.10 for steel)
- R_framing = R-value through framing path (hr·ft²·°F/Btu)
- R_cavity = R-value through cavity path (hr·ft²·°F/Btu)

Continuous exterior insulation added in series:

R_total,ci = R_ci + 1 / [(FF / R_framing) + ((1 - FF) / R_cavity)]

**Thermal bridge reduction efficiency:**

η_bridge = (R_total,ci - R_total,no_ci) / R_ci

Higher R_ci values provide diminishing returns as the assembly becomes less dominated by thermal bridging.

## Condensation Risk Control

### Minimum R-Value Ratios

ASHRAE 90.1 and the International Energy Conservation Code (IECC) establish minimum R_ci requirements to prevent condensation on sheathing surfaces. The critical ratio depends on climate zone and interior humidity levels.

**Condensation prevention criterion:**

R_ci / R_total ≥ R_ci,min / R_total

The minimum ratio ensures sheathing temperature remains above dew point temperature for design conditions.

| Climate Zone | Cavity Insulation | Min R_ci (Vented Cladding) | Min R_ci (Sealed Cladding) | R_ci/R_total Ratio |
|--------------|-------------------|----------------------------|----------------------------|-------------------|
| 5 (CDD≤3000) | R-13 | R-3 | R-5 | 0.23-0.28 |
| 5 (CDD>3000) | R-13 | R-5 | R-7.5 | 0.28-0.37 |
| 6 | R-13 | R-7.5 | R-11.25 | 0.37-0.46 |
| 7 | R-13 | R-10 | R-15 | 0.43-0.54 |
| 8 | R-13 | R-15 | R-20 | 0.54-0.61 |

CDD = Cooling Degree Days base 50°F

**Design consideration:** Higher interior humidity levels (>35% RH at design temperature) require increased R_ci ratios beyond minimum code values.

### Sheathing Temperature Analysis

The critical sheathing temperature for condensation risk occurs at the interface between cavity insulation and exterior insulation:

T_sheathing,critical = T_dew,interior

Where T_dew,interior is determined from interior design temperature and relative humidity using psychrometric relationships.

**Dew point calculation (simplified):**

T_dew ≈ T_db - ((100 - RH) / 5)

More precise calculation uses psychrometric tables or equations based on partial pressure of water vapor.

**Condensation analysis procedure:**

1. Determine interior design conditions (temperature, RH)
2. Calculate interior dew point temperature
3. Calculate sheathing temperature from thermal resistance ratio
4. Compare T_sheathing to T_dew,interior
5. If T_sheathing > T_dew,interior + 5°F safety margin, condensation risk is acceptable

## Exterior Insulation Material Types

### Rigid Board Insulation

#### Extruded Polystyrene (XPS)

**Thermal properties:**
- R-value: 5.0 per inch (aged)
- Compressive strength: 25-60 psi (ASTM C578)
- Water absorption: <0.3% by volume
- Vapor permeance: 0.8-1.2 perms at 1 inch thickness

**Application characteristics:**
- Closed cell structure provides moisture resistance
- Moderate vapor barrier (Type II designation)
- Good dimensional stability
- Available in densities from 1.3-3.0 lb/ft³

#### Expanded Polystyrene (EPS)

**Thermal properties:**
- R-value: 3.6-4.2 per inch
- Compressive strength: 10-60 psi (Type I-IX per ASTM C578)
- Water absorption: <4% by volume
- Vapor permeance: 2.0-5.8 perms at 1 inch (Type I)

**Application characteristics:**
- Lower cost than XPS
- Higher vapor permeability allows drying
- Available in various densities (0.7-3.0 lb/ft³)
- Requires UV protection

#### Polyisocyanurate (Polyiso)

**Thermal properties:**
- R-value: 5.6-6.5 per inch at 75°F mean temperature
- Temperature-dependent performance (decreases at low temperatures)
- Compressive strength: 20-40 psi
- Vapor permeance: 0.03-3.0 perms (depends on facer)

**Application characteristics:**
- Highest initial R-value per inch
- Facer type controls moisture properties
- Foil facers provide very low permeance (<0.05 perms)
- Performance degradation below 25°F (R-value drops ~20% at 0°F)

**Temperature correction factor for polyiso:**

R_actual = R_75°F × (1 - 0.008 × (75 - T_mean))

Where T_mean is the mean temperature through the insulation layer.

#### Mineral Wool (Rock Wool/Stone Wool)

**Thermal properties:**
- R-value: 3.8-4.3 per inch
- Compressive strength: 2-80 psi (density dependent)
- Water absorption: Non-hygroscopic
- Vapor permeance: >30 perms (highly permeable)

**Application characteristics:**
- Fire resistant (melting point >2000°F)
- Vapor permeable allows bidirectional drying
- Heavier than foam insulations (4-12 lb/ft³)
- Requires drainage management (absorbs water but drains)

### Spray-Applied Exterior Insulation

#### Closed-Cell Spray Polyurethane Foam (ccSPF)

**Thermal properties:**
- R-value: 6.0-7.0 per inch (initial)
- Density: 1.7-2.3 lb/ft³
- Vapor permeance: 0.8-1.5 perms at 2 inches
- Compressive strength: 25-40 psi

**Application characteristics:**
- Excellent air sealing properties
- Conforms to irregular surfaces
- Acts as water-resistive barrier when sufficient thickness (>3.5 inches)
- Requires UV and ignition protection

## Vapor Control Strategy

### Exterior Insulation as Vapor Control

The ratio of exterior to total insulation determines vapor drive through the assembly. Sufficient exterior insulation warms interior surface materials above dew point, allowing higher interior vapor permeance.

**Vapor control principle:** When R_ci is adequate, interior vapor retarder class can be relaxed.

| Climate Zone | R_ci Minimum | Interior Vapor Retarder Class |
|--------------|--------------|------------------------------|
| 5 | R-7.5 | Class III (1-10 perms) |
| 6 | R-11.25 | Class III or smart retarder |
| 7 | R-15 | Class III or smart retarder |
| 8 | R-20 | Class II (0.1-1.0 perms) |

**Smart vapor retarder application:** Variable permeance membranes that reduce permeance in winter (high RH) and increase permeance in summer allow seasonal drying.

### Permeance Relationships

Vapor flow through multi-layer assemblies follows series resistance:

1/M_total = 1/M_1 + 1/M_2 + ... + 1/M_n

Where M = permeance (perms) of each layer.

The layer with lowest permeance controls vapor flow. When exterior insulation has low permeance (XPS, foil-faced polyiso), the assembly must either:

1. Control interior humidity to prevent accumulation
2. Provide adequate R_ci to warm sheathing above dew point
3. Use permeable exterior insulation (mineral wool, EPS) to allow drying

## Water Management Integration

### Drainage Plane Considerations

Exterior insulation placement relative to the water-resistive barrier (WRB) affects drainage performance.

**Configuration A - WRB outboard of insulation:**
- Insulation protected from liquid water
- Drainage occurs at outer surface
- Flashing integration simplified
- Ventilation space can be created above insulation

**Configuration B - WRB inboard of insulation:**
- Insulation exposed to potential moisture
- Requires insulation with water-shedding properties
- More complex flashing details
- Common with insulated sheathing products

### Drainage and Ventilation

Water that penetrates cladding must drain without accumulating at the insulation layer.

**Drainage requirements:**
- Minimum 3/16 inch drainage gap (1/4 inch preferred)
- Top and bottom ventilation openings
- Net free vent area: 1 inch² per linear foot of wall

**Pressure equalization benefits:**
- Reduces water penetration driving forces
- Allows moisture drying
- Maintains air space functionality

## Attachment Considerations

### Cladding Support Through Insulation

Exterior cladding must be supported through the insulation layer to structural elements. Fastener thermal bridging increases with insulation thickness.

**Thermal bridging from fasteners:**

For metal fasteners penetrating insulation:

R_effective = R_insulation × (1 - A_fastener / A_total × (k_fastener / k_insulation))

Where:
- k_fastener ≈ 30-300 Btu·in/(hr·ft²·°F) for steel
- k_insulation ≈ 0.15-0.30 Btu·in/(hr·ft²·°F)

**Fastener density impact:** At typical fastener spacing (16-24 inches o.c.), thermal bridging is <5% of total R-value loss, but moisture condensation on cold fasteners can occur.

### Attachment Methods

**Mechanical fastening:**
- Long screws/nails through insulation to framing
- Plastic cap washers distribute loads
- Fastener length = insulation thickness + required embedment + sheathing

**Furring strip systems:**
- Wood or metal furring attached through insulation
- Creates drainage/ventilation space
- Provides direct cladding attachment
- Thermal bridging through furring must be calculated

**Proprietary attachment systems:**
- Thermally broken fasteners
- Composite structural elements
- Engineered to minimize thermal bridging while meeting structural loads

## Installation Details

### Continuous Insulation Board Joints

Board joints create thermal weak points and potential air/water infiltration paths.

**Joint treatment:**
- Stagger joints between layers for multi-layer installations
- Tape joints with compatible tape (check adhesion to facing material)
- Offset joints minimum 6 inches from framing members
- Seal joints at penetrations and transitions

**Multi-layer strategy:**
- Two layers of 2-inch insulation outperform single 4-inch layer
- Staggered joints eliminate continuous thermal paths
- Total thermal resistance equals sum: R_total = R_layer1 + R_layer2

### Interface Transitions

Critical interfaces require detailed moisture management:

**Foundation to wall:**
- Protect insulation top edge from water entry
- Flashing lapped over insulation
- Seal gap between insulation and foundation

**Window and door openings:**
- Insulation returns at jambs (or use insulated bucks)
- Flashing integrated with WRB and insulation layers
- Minimize thermal bridging at frame perimeter

**Roof-wall intersection:**
- Continuous insulation alignment (or calculated thermal break)
- Flashing above insulation protects top edge
- Air barrier continuity maintained

## Performance Verification

### Infrared Thermography

Thermal imaging identifies insulation defects and thermal bridges:

**Inspection conditions:**
- Minimum 15°F temperature difference across assembly
- Conduct during stable weather (no recent solar gain)
- Interior side imaging shows cold spots (missing insulation, thermal bridges)
- Exterior side imaging shows warm spots in winter (heat loss paths)

**Common defects detected:**
- Gaps at board joints
- Compressed or missing insulation
- Thermal bridging at attachments
- Air leakage paths

### Blower Door Testing

Air leakage through wall assemblies compromises thermal performance and can transport moisture.

**Target air tightness:**
- 3.0 ACH50 or less (residential)
- 0.40 CFM50/ft² of envelope area (commercial)

Exterior insulation alone does not provide air barrier function unless specifically designed (spray foam, sealed board joints).

## Hygrothermal Modeling

### WUFI and Similar Tools

Computer simulation predicts moisture accumulation and drying in multi-layer assemblies under dynamic conditions.

**Input requirements:**
- Material properties (thermal conductivity, vapor permeability, moisture storage)
- Climate data (temperature, RH, solar radiation, wind-driven rain)
- Interior conditions (temperature, RH generation rate)
- Initial moisture content

**Analysis outputs:**
- Moisture content vs. time at each layer
- Temperature and RH profiles
- Identification of condensation risk periods
- Drying potential assessment

**Design validation:** Assemblies should demonstrate:
- Moisture content remains below critical levels (wood MC <20%, RH <80%)
- Any moisture accumulation dries within seasonal cycle
- No sustained condensation periods

## Design Guidelines

### Climate-Specific Recommendations

**Cold climates (Zones 5-8):**
- Prioritize high R_ci ratios (40-60% of total R-value)
- Control interior humidity (<35% RH at design conditions)
- Use vapor-permeable cavity insulation to allow inward drying
- Consider smart vapor retarders for interior
- Verify sheathing temperature remains above dew point

**Mixed climates (Zones 4-5):**
- Balance heating and cooling season performance
- R_ci ratio 25-40% of total R-value
- Allow bidirectional drying where possible
- Avoid interior vapor barriers (use Class III retarders)
- Consider variable permeance materials

**Hot-humid climates (Zones 1-3):**
- Prevent inward vapor drive from exterior
- Use vapor-permeable exterior insulation (EPS, mineral wool)
- Interior vapor barriers not recommended
- Focus on drainage and drying capacity
- Control interior moisture from AC condensate and infiltration

### Material Selection Criteria

**Selection factors:**

1. **Thermal resistance:** R-value at operating temperature range
2. **Vapor permeance:** Compatible with assembly drying strategy
3. **Water resistance:** Drainage plane location and flood risk
4. **Compressive strength:** Cladding attachment loads
5. **Fire resistance:** Code requirements and building type
6. **Durability:** UV resistance, dimensional stability
7. **Cost:** Installed cost per R-value
8. **Sustainability:** Embodied carbon, recyclability, off-gassing

### Quality Assurance

**Installation inspection checklist:**
- Board joints tight and staggered
- Fastener penetrations sealed
- Flashing properly lapped
- No gaps at penetrations or transitions
- Proper embedment of fasteners
- Drainage space maintained (if required)
- Protection from weather during construction

## Code and Standard References

**ASHRAE Standards:**
- ASHRAE 90.1: Energy Standard for Buildings (minimum R_ci requirements)
- ASHRAE 160: Criteria for Moisture-Control Design Analysis
- ASHRAE Handbook - Fundamentals, Chapter 26 (Heat, Air, and Moisture Control)

**ASTM Standards:**
- ASTM C578: Rigid Cellular Polystyrene Thermal Insulation
- ASTM C1289: Polyisocyanurate Thermal Insulation
- ASTM C1104: Mineral Fiber Insulation Boards
- ASTM E96: Water Vapor Transmission of Materials
- ASTM E2178: Air Permeance of Building Materials

**Building Codes:**
- International Energy Conservation Code (IECC)
- International Building Code (IBC) - Section 1403 (exterior walls)
- International Residential Code (IRC) - Section R703

**Industry Guidelines:**
- Building Science Corporation - Information Sheets
- NIST - Moisture Control Guidance
- EIFS Industry Members Association (EIMA) - Technical bulletins
