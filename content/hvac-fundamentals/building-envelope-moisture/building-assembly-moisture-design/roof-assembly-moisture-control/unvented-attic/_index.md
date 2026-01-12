---
title: "Unvented Attic"
description: "Technical design and analysis of unvented attic assemblies including insulation strategies, moisture control mechanisms, condensation prevention, code compliance requirements, and thermal performance optimization for conditioned attic spaces"
weight: 2
---

Unvented attic assemblies represent a fundamental departure from traditional ventilated attic construction by moving the thermal and air control boundary to the roof deck plane rather than the ceiling plane. This design strategy creates a conditioned or semi-conditioned space within the attic volume, eliminating the need for attic ventilation while providing superior air sealing, duct system performance when located in attics, and moisture control when properly designed and constructed.

The unvented attic approach addresses multiple building science challenges simultaneously: reducing air leakage through the ceiling plane, improving HVAC distribution system efficiency by bringing ductwork into conditioned space, minimizing stack effect-driven air movement, and preventing ice dam formation in cold climates through elimination of heat loss to the attic space.

## Fundamental Heat and Moisture Transport Principles

### Heat Transfer Through Unvented Roof Assemblies

Heat flow through an unvented roof deck follows the standard steady-state conduction equation modified for multi-layer assemblies:

**Q = U × A × ΔT**

Where:
- Q = heat transfer rate (Btu/hr or W)
- U = overall thermal transmittance coefficient (Btu/hr·ft²·°F or W/m²·K)
- A = roof assembly area (ft² or m²)
- ΔT = temperature difference between interior and exterior (°F or K)

The overall U-factor for the assembly is calculated from individual layer resistances:

**U = 1 / (R_outside + R_roofing + R_sheathing + R_insulation + R_airspace + R_inside)**

For unvented assemblies, the primary insulation layer at the roof deck must provide sufficient R-value to prevent condensation on the underside of the roof sheathing during winter conditions.

### Dewpoint Temperature and Condensation Risk

The critical design parameter for unvented roofs is maintaining sheathing temperature above the dewpoint temperature of interior air:

**T_sheathing > T_dewpoint**

Dewpoint temperature is calculated from interior conditions:

**T_d = T - ((100 - RH) / 5)**

Simplified approximation where:
- T_d = dewpoint temperature (°F)
- T = dry-bulb temperature (°F)
- RH = relative humidity (%)

More precise calculation using vapor pressure:

**T_d = (237.3 × α) / (17.27 - α)**

Where α = ln(e_s / 610.78) / 17.27, and e_s is the saturation vapor pressure.

### Moisture Accumulation Potential

The moisture balance in an unvented attic depends on:

1. **Vapor diffusion through materials** - governed by material permeance
2. **Air leakage carrying moisture** - dominant transport mechanism
3. **Interior moisture generation** - from occupant activities
4. **Condensation potential** - at cold surfaces
5. **Drying capacity** - through diffusion and air exchange

The vapor diffusion rate through a material follows Fick's Law:

**G = M × A × Δp**

Where:
- G = moisture transfer rate (grains/hr or kg/s)
- M = material permeance (perms or kg/Pa·s·m²)
- A = area (ft² or m²)
- Δp = vapor pressure difference (in. Hg or Pa)

## Air-Impermeable Insulation Requirements

### Spray Polyurethane Foam (SPF) Systems

Spray foam insulation provides both thermal resistance and air/vapor control in a single material application.

**Closed-Cell SPF Properties:**

| Property | Typical Value | Test Method |
|----------|--------------|-------------|
| R-value per inch | 6.0-6.5 hr·ft²·°F/Btu | ASTM C518 |
| Density | 1.8-2.2 lb/ft³ | ASTM D1622 |
| Air permeance @ 1 in. | <0.002 L/s·m² @ 75 Pa | ASTM E2178 |
| Vapor permeance @ 2 in. | <1.0 perm | ASTM E96 |
| Compressive strength | 25-40 psi | ASTM D1621 |
| Tensile strength | 40-50 psi | ASTM D1623 |
| Water absorption | <2% by volume | ASTM D2842 |

**Open-Cell SPF Properties:**

| Property | Typical Value | Test Method |
|----------|--------------|-------------|
| R-value per inch | 3.6-3.8 hr·ft²·°F/Btu | ASTM C518 |
| Density | 0.4-0.6 lb/ft³ | ASTM D1622 |
| Air permeance @ 3.5 in. | <0.02 L/s·m² @ 75 Pa | ASTM E2178 |
| Vapor permeance @ 5.5 in. | 8-16 perms | ASTM E96 |
| Sound absorption | NRC 0.70 @ 3.5 in. | ASTM C423 |

Closed-cell SPF provides both air sealing and vapor control, while open-cell SPF requires a separate vapor retarder in cold climates per code requirements.

### Rigid Foam Insulation Systems

Rigid foam boards applied above roof sheathing provide continuous insulation without thermal bridging through framing members.

**Rigid Foam Thermal Properties:**

| Material | R-value/in. | Permeance @ 1 in. | Max Service Temp | Compressive Strength |
|----------|-------------|-------------------|------------------|---------------------|
| Polyisocyanurate (polyiso) | 6.0-6.5 | 1.0-2.0 perms | 250°F | 25-40 psi |
| Extruded polystyrene (XPS) | 5.0 | 1.0-1.5 perms | 165°F | 25-60 psi |
| Expanded polystyrene (EPS) | 3.6-4.2 | 2.0-5.0 perms | 165°F | 10-60 psi |

Temperature-dependent performance must be considered for polyiso, which experiences R-value reduction at low temperatures:

**R_effective = R_nominal × (1 - 0.003 × (75 - T_mean))**

Where T_mean is the mean temperature through the insulation layer.

### Hybrid Insulation Assemblies

Many unvented roof designs combine air-impermeable insulation with air-permeable insulation to optimize cost and performance:

**Configuration 1: SPF + Fibrous Insulation**
- Closed-cell SPF at roof deck (minimum thickness per climate zone)
- Fiberglass or mineral wool batts filling remaining rafter cavity
- SPF provides air sealing and minimum vapor control

**Configuration 2: Rigid Foam + Cavity Insulation**
- Continuous rigid foam above roof sheathing
- Air-permeable insulation in rafter cavities
- Rigid foam provides condensation control

## Code Requirements and Compliance

### International Residential Code (IRC) Section R806.5

The IRC establishes specific requirements for unvented attic assemblies:

**Air-Impermeable Insulation Directly Applied to Underside of Structural Roof Deck:**

Climate zone requirements for minimum air-impermeable insulation R-value as percentage of total assembly R-value:

| Climate Zone | Minimum Air-Impermeable R-value | % of Total R-value |
|--------------|--------------------------------|--------------------|
| 1, 2A, 2B | None required | 0% |
| 3 | R-5 | ~15% of R-30 |
| 4C | R-10 | ~25% of R-38 |
| 4A, 4B | R-15 | ~30% of R-49 |
| 5 | R-20 | ~35% of R-49 |
| 6 | R-25 | ~40% of R-49 |
| 7 | R-30 | ~45% of R-49 |
| 8 | R-35 | ~50% of R-49 |

These minimum requirements ensure the underside of the structural roof sheathing remains above dewpoint temperature during winter conditions, preventing condensation accumulation.

### International Building Code (IBC) Section 1203.3

Commercial buildings must comply with IBC requirements that parallel IRC provisions but reference IECC for thermal performance requirements. IBC Section 1203.3 permits unvented attic assemblies when designed to control condensation.

### IECC Requirements

The International Energy Conservation Code establishes overall thermal performance requirements that must be met in addition to condensation control provisions:

- Minimum total R-values by climate zone
- Air leakage testing requirements
- Thermal bridging considerations for continuous insulation
- Documentation and certification requirements

## Design Methodology and Calculations

### Step 1: Climate Zone Determination

Identify the project climate zone using ASHRAE 169-2013 or IECC climate zone maps. This determines:
- Minimum air-impermeable insulation thickness
- Vapor retarder requirements
- Overall R-value targets

### Step 2: Condensation Plane Analysis

Calculate the temperature at the sheathing/insulation interface under design winter conditions:

**T_sheathing = T_exterior + (R_exterior / R_total) × (T_interior - T_exterior)**

Where:
- R_exterior = R-value of all layers outboard of analysis plane
- R_total = total assembly R-value
- T_interior = interior design temperature (typically 70°F)
- T_exterior = 99% winter design temperature from ASHRAE Fundamentals

Compare T_sheathing to dewpoint temperature of interior air at design relative humidity (typically 35% in winter).

**Design Criterion: T_sheathing > T_dewpoint + 5°F safety margin**

### Step 3: Thickness Determination

For spray foam applications, calculate minimum closed-cell SPF thickness:

**t_min = (R_min required) / (R-value per inch)**

For Climate Zone 5 example:
- R_min = R-20
- SPF R-value = 6.5/in
- t_min = 20/6.5 = 3.1 inches minimum

Round up to nearest 0.5 inch for field application: 3.5 inches.

### Step 4: Total Assembly R-Value

Calculate complete assembly thermal performance including:
- Outside air film resistance: R-0.17
- Roofing materials: R-0.5 to R-1.0
- Roof sheathing: R-0.6 (½" OSB)
- Air-impermeable insulation: as calculated
- Air-permeable cavity insulation: standard R-values
- Interior air film resistance: R-0.61

**R_total = Σ R_individual_layers**

Verify R_total meets or exceeds code-required values for the climate zone.

### Step 5: Thermal Bridging Analysis

For assemblies with framing members, calculate assembly-average U-factor accounting for thermal bridging:

**U_assembly = (U_cavity × %_cavity) + (U_framing × %_framing)**

Where framing fraction typically ranges from 10-15% of roof area.

## Material Selection and Specifications

### Spray Foam Application Requirements

**Surface Preparation:**
- Roof sheathing clean, dry, and free of dust/debris
- Surface temperature between 60-90°F for proper adhesion
- No moisture content above 19% in wood substrates

**Application Parameters:**

| Parameter | Closed-Cell SPF | Open-Cell SPF |
|-----------|----------------|---------------|
| Pass thickness | 1-2 inches | 3-4 inches |
| Substrate temp | 60-100°F | 60-100°F |
| Ambient temp | 60-90°F | 60-90°F |
| Relative humidity | <80% | <80% |
| Coverage rate | 15-20 bd ft/lb | 50-60 bd ft/lb |
| Yield | 95-105% of theoretical | 95-105% of theoretical |

**Quality Control:**
- Core samples taken at 1 per 5,000 ft² minimum
- Thickness verification with depth gauges
- Visual inspection for voids, gaps, delamination
- Density testing per ASTM D1622

### Rigid Foam Board Installation

**Above-Sheathing Installation:**
- Continuous layer with staggered joints
- Joints taped with compatible tape product
- Mechanical fastening with plates and long screws
- Proper slope maintained for drainage (minimum ¼ in./ft)

**Fastening Requirements:**

| Insulation Thickness | Fastener Spacing | Plate Size |
|---------------------|------------------|------------|
| 1-2 inches | 12 in. o.c. | 2.5-3 in. diameter |
| 2-4 inches | 10 in. o.c. | 3-4 in. diameter |
| >4 inches | 8 in. o.c. | 4 in. diameter |

### Vapor Retarder Requirements

When using air-permeable insulation or open-cell SPF in climate zones 5 and higher:

**Class II Vapor Retarder Required:**
- Permeance between 0.1 and 1.0 perm
- Installed on interior (warm in winter) side of insulation
- Sealed at penetrations and joints
- Common materials: kraft facing, painted gypsum, vapor retarder paint

Exception: When air-impermeable insulation meets minimum R-value ratios per IRC Table R806.5, vapor retarder can be omitted.

## Performance Verification and Testing

### Air Leakage Testing

Unvented attic assemblies should be verified for air tightness using blower door testing:

**Target Performance:**
- Whole-building: <3.0 ACH50 (IECC requirement)
- High-performance: <1.5 ACH50
- Passive House: <0.6 ACH50

Attic air sealing effectiveness can be isolated using zonal pressure testing with attic access sealed.

### Thermal Imaging Inspection

Infrared thermography identifies:
- Missing or compressed insulation
- Thermal bridging at framing members
- Air leakage pathways
- Installation defects

Conduct thermal imaging during heating season with minimum 20°F indoor-outdoor temperature difference.

### Moisture Content Monitoring

For validation of hygrothermal performance:

**Wood Moisture Content Limits:**
- Target: <12% for dimensional stability
- Warning: 16-19% (risk zone)
- Critical: >20% (mold growth potential)

Install moisture sensors in roof sheathing at multiple locations:
- Ridge area (warmest, driest)
- Mid-slope (representative)
- Eave area (coldest, highest risk)

## Design Considerations and Best Practices

### HVAC Equipment and Ductwork in Unvented Attics

The primary benefit of unvented attics for HVAC performance:

**Duct System Efficiency Improvement:**
- Reduced conductive losses (ductwork in conditioned space)
- Elimination of air leakage to unconditioned space
- Typical energy savings: 10-25% for space conditioning

**Equipment Sizing Impact:**
- Load calculation treats attic as semi-conditioned space
- Reduced peak cooling loads
- Potential for downsized equipment capacity

### Attic Access and Penetrations

Every penetration through the insulation layer compromises performance:

**Air Sealing Details:**
- Attic access hatches: weatherstripping, insulated covers
- Penetrations: sealed with spray foam or appropriate sealant
- Recessed lighting: IC-rated fixtures with sealed housings
- Plumbing vents: boot and collar sealed to roof deck insulation

### Fire Rating Considerations

Spray foam insulation materials require thermal barrier protection in occupied spaces per IRC Section R316.4:

**Thermal Barrier Requirements:**
- ½-inch gypsum wallboard, or
- Equivalent 15-minute thermal barrier
- Exception: Products tested and approved for exposed application

Unvented attics typically qualify as "attic spaces entered only for service of utilities" allowing ignition barrier rather than full thermal barrier (IRC R316.5.11).

### Roof Covering Service Life

Unvented attics may increase roof deck temperature during summer:

**Temperature Elevation:**
- Ventilated attic peak: 130-150°F
- Unvented attic with insulation at deck: 150-170°F
- Impact on shingle life: 10-20% reduction in some climates

**Mitigation Strategies:**
- Cool roof coatings or light-colored roofing
- Above-sheathing ventilation gap (hybrid approach)
- High-temperature-rated roofing materials
- Continuous rigid insulation above sheathing

### Moisture Management in Heating Climates

Cold climate installations require careful moisture control:

**Interior Moisture Control:**
- Maintain relative humidity <40% in winter (35% target)
- Continuous mechanical ventilation per ASHRAE 62.2
- Kitchen and bathroom exhaust vented to exterior
- Address moisture sources (crawlspaces, basements)

**Assembly Drying Capacity:**
- Vapor-open exterior (avoid low-perm roofing underlayments)
- Diffusion drying toward interior when air-permeable insulation used
- Monitor moisture accumulation in sheathing

### Integration with Wall Assemblies

The thermal and air control boundary transitions require careful detailing:

**Continuous Air Barrier:**
- Roof deck insulation connects to top plates
- Sealed connection to wall air barrier system
- Address transitions at rake walls, gable ends
- Maintain continuity through complex geometry

## Long-Term Performance and Monitoring

### Sheathing Moisture Evaluation

ASHRAE 160-2016 provides criteria for moisture-safe design:

**30-Day Running Average:**
- Surface RH <80% at interface temperature
- Or moisture content <20% in wood-based materials
- Evaluated using hourly hygrothermal simulation

### Hygrothermal Modeling

Advanced analysis using WUFI or similar software simulates:
- Transient moisture accumulation and drying
- Material properties and boundary conditions
- Multi-year performance prediction
- Climate-specific risk assessment

Input parameters include:
- Hourly weather data for project location
- Material hygric properties (sorption isotherms, liquid transport)
- Interior moisture generation (occupant density, activities)
- Air change rates and infiltration

### Warranty and Insurance Considerations

Document design approach for liability protection:
- Design calculations showing code compliance
- Material specifications and installation requirements
- Testing and verification results
- Maintenance and monitoring requirements

## Comparative Performance Analysis

### Energy Performance Comparison

Typical heating and cooling energy comparison (Climate Zone 5):

| Assembly Type | Heating Energy Index | Cooling Energy Index | Total Site Energy |
|---------------|---------------------|---------------------|-------------------|
| Vented attic, R-49 ceiling | 100 (baseline) | 100 (baseline) | 100 (baseline) |
| Unvented attic, R-49 @ deck, ducts in attic | 88 | 82 | 85 |
| Unvented attic, R-60 @ deck, ducts in attic | 82 | 78 | 80 |

Energy savings from unvented assemblies result from:
1. Reduced duct leakage impact (60-70% of benefit)
2. Reduced duct conductive losses (20-30% of benefit)
3. Improved ceiling plane air tightness (10-20% of benefit)

### First Cost Implications

Relative construction cost factors:

| Assembly Strategy | Material Cost Factor | Labor Cost Factor | Total Cost Factor |
|-------------------|---------------------|-------------------|-------------------|
| Vented attic + R-49 blown insulation | 1.00 | 1.00 | 1.00 |
| Unvented + closed-cell SPF @ deck | 2.5-3.0 | 1.2-1.4 | 2.2-2.6 |
| Unvented + hybrid SPF + batts | 1.8-2.2 | 1.3-1.5 | 1.6-2.0 |
| Unvented + continuous rigid foam | 2.0-2.5 | 1.4-1.6 | 1.8-2.2 |

Life cycle cost analysis must include energy savings, duct sealing costs, and maintenance factors to determine economic optimum.

## References and Standards

**ASHRAE Standards:**
- ASHRAE 90.1: Energy Standard for Buildings Except Low-Rise Residential Buildings
- ASHRAE 62.1/62.2: Ventilation for Acceptable Indoor Air Quality
- ASHRAE 160: Criteria for Moisture-Control Design Analysis in Buildings
- ASHRAE Standard 55: Thermal Environmental Conditions for Human Occupancy

**Building Codes:**
- International Residential Code (IRC) Section R806.5
- International Building Code (IBC) Section 1203.3
- International Energy Conservation Code (IECC)

**Test Methods:**
- ASTM C518: Steady-State Thermal Transmission Properties
- ASTM E96: Water Vapor Transmission of Materials
- ASTM E2178: Air Permeance of Building Materials
- ASTM E779/E1827: Air Leakage Testing

**Design Guidance:**
- Building Science Corporation: Building Science Digests
- U.S. DOE Building America Program: Best Practice Guides
- ASHRAE Handbook of Fundamentals: Chapter on Heat, Air, and Moisture Control
