---
title: "ASHRAE 160 Standard"
aliases: ["ASHRAE 160 Standard"]
weight: 4
---

ASHRAE Standard 160 provides design criteria for moisture control in buildings to prevent mold growth and material deterioration. The standard establishes surface relative humidity limits and temperature-RH combinations that predict conditions favorable for mold development.

## Standard Scope and Application

ASHRAE 160 applies to:

- Residential buildings
- Commercial buildings
- Institutional facilities
- New construction and major renovations
- All climate zones

The standard addresses moisture control during both design and construction phases.

## Design Criteria Philosophy

ASHRAE 160 establishes performance-based criteria:

**Fundamental Principle**: Building envelope assemblies must be designed to limit moisture accumulation such that mold growth does not occur under normal occupancy conditions.

**Performance Metric**: Surface relative humidity and temperature combinations at material interfaces.

**Time-Dependent Assessment**: 30-day running average method accounts for material moisture buffering capacity.

## Surface RH Limits

The standard specifies maximum allowable surface relative humidity based on surface temperature:

| Surface Temperature (°F) | Maximum 30-Day Average RH (%) | Maximum Monthly Average RH (%) |
|--------------------------|-------------------------------|--------------------------------|
| 32-41 | 100 | 100 |
| 41-50 | 95 | 98 |
| 50-59 | 85 | 92 |
| 59-68 | 80 | 88 |
| 68-77 | 80 | 88 |
| 77-86 | 80 | 88 |
| > 86 | 80 | 88 |

**Critical Threshold**: Surface RH should not exceed 80% when surface temperature is above 41°F (5°C) for extended periods.

## Temperature-RH Combinations

Mold growth potential increases with both temperature and humidity. Critical combinations:

| Condition | Surface Temperature (°F) | Surface RH (%) | Mold Risk |
|-----------|-------------------------|----------------|-----------|
| Low Risk | < 50 | < 80 | Minimal |
| Moderate Risk | 50-68 | 80-85 | Moderate |
| High Risk | 68-86 | > 85 | High |
| Very High Risk | > 77 | > 90 | Very High |

**Optimal Mold Growth**: 77-86°F (25-30°C) with RH > 85%.

## 30-Day Running Average Method

The standard uses a 30-day running average calculation to account for material moisture buffering:

**Calculation Method**:

1. Calculate hourly surface temperature and RH for one year
2. Compute 30-day running average RH for each hour
3. Compare running average against criteria limits
4. Identify exceedance periods

**Formula**:

RH_30day(t) = (1/720) × Σ[RH(t-i)] for i = 0 to 719 hours

Where:
- RH_30day(t) = 30-day running average RH at time t
- RH(t-i) = hourly RH at time t minus i hours
- 720 hours = 30 days × 24 hours/day

**Compliance Criterion**: The 30-day running average RH must not exceed limits in the table above.

## Climate Data Requirements

ASHRAE 160 analysis requires hourly climate data:

**Essential Parameters**:

- Outdoor dry-bulb temperature (hourly)
- Outdoor relative humidity (hourly)
- Solar radiation (direct and diffuse)
- Wind speed and direction
- Rainfall data
- Ground temperature

**Data Sources**:

| Source | Data Type | Resolution | Coverage |
|--------|-----------|------------|----------|
| TMY3 | Typical meteorological year | Hourly | 1020 US locations |
| IWEC | International weather | Hourly | Global |
| CWEC | Canadian weather | Hourly | Canadian locations |
| Custom | Site-specific measured | Hourly | As available |

**Minimum Duration**: One full year (8760 hours) of climate data required.

## Material Properties for Analysis

Surface conditions depend on material hygrothermal properties:

**Required Properties**:

| Property | Units | Typical Range | Importance |
|----------|-------|---------------|------------|
| Thermal conductivity | Btu·in/hr·ft²·°F | 0.2-10 | High |
| Density | lb/ft³ | 5-150 | Medium |
| Specific heat | Btu/lb·°F | 0.2-0.4 | Medium |
| Vapor permeability | perm·in | 0.01-1000 | High |
| Moisture storage | lb/lb per %RH | 0.001-0.15 | High |
| Liquid diffusivity | ft²/hr | 10⁻⁸-10⁻⁴ | Medium |

**Material Classes**:

- Class I (vapor impermeable): < 0.1 perm
- Class II (vapor semi-impermeable): 0.1-1.0 perm
- Class III (vapor semi-permeable): 1.0-10 perm
- Class IV (vapor permeable): > 10 perm

## Analysis Methods

ASHRAE 160 compliance can be demonstrated through three approaches:

### 1. Simplified Prescriptive Method

**Application**: Simple assemblies in mild climates.

**Requirements**:
- Continuous air barrier
- Thermal insulation meeting code minimums
- Vapor retarder placement per climate zone
- Proper flashing and drainage

**Limitations**: Not applicable for complex assemblies or severe climates.

### 2. Intermediate Calculation Method

**Application**: Standard assemblies with known properties.

**Process**:
1. Calculate steady-state temperature distribution
2. Determine surface temperatures at critical interfaces
3. Calculate surface RH from indoor/outdoor conditions
4. Compare against criteria limits

**Tools**: Spreadsheet calculations, simple software.

### 3. Advanced Hygrothermal Simulation

**Application**: Complex assemblies, innovative designs, severe climates.

**Process**:
1. Model full assembly with all layers
2. Input hourly climate data
3. Run transient heat and moisture simulation
4. Calculate hourly surface conditions
5. Apply 30-day running average
6. Verify compliance

**Software**: WUFI, DELPHIN, MOISTURE-EXPERT, hygIRC.

## Critical Surface Locations

Analysis must evaluate RH at moisture-sensitive interfaces:

**Exterior Assemblies**:

- Exterior sheathing inner surface
- Interior surface of exterior insulation
- First condensing surface inward from exterior
- Roof deck underside
- Rim joist interfaces

**Interior Conditions**:

- Behind vapor retarders
- Cold corners and thermal bridges
- Window and door perimeters
- Basement walls
- Slab edges

## Indoor Humidity Assumptions

ASHRAE 160 specifies design indoor humidity levels:

**Residential Buildings**:

| Outdoor Temperature (°F) | Indoor RH (%) |
|-------------------------|---------------|
| < 20 | 15 |
| 20-30 | 20 |
| 30-40 | 25 |
| 40-50 | 30 |
| > 50 | 35 |

**Additional Sources**:
- 1.0 gal/day per occupant (moisture generation)
- Cooking, bathing, laundry activities
- Mechanical ventilation rate: 0.35 ACH or 15 CFM/person

**Commercial Buildings**: Maintain 40-60% RH per ASHRAE 55 with mechanical systems.

## Compliance Verification

Demonstrating compliance with ASHRAE 160 requires:

### Documentation Requirements

**Design Phase**:
- Climate data source and location
- Assembly drawings and specifications
- Material property data
- Calculation method and results
- Critical surface identification

**Compliance Report Must Include**:

| Item | Details |
|------|---------|
| Project location | City, state, climate zone |
| Climate data | Source, type, period |
| Assembly description | All layers, thicknesses, materials |
| Material properties | Thermal, hygric properties |
| Boundary conditions | Indoor/outdoor conditions |
| Analysis method | Simplified, intermediate, advanced |
| Results | Surface RH vs. time plots |
| Compliance statement | Pass/fail for each surface |

### Verification Procedures

**Step 1: Identify Critical Surfaces**
- Locate first condensing surface
- Identify thermal bridges
- Consider material compatibility

**Step 2: Determine Surface Conditions**
- Calculate hourly temperature
- Calculate hourly RH
- Apply 30-day running average

**Step 3: Compare Against Criteria**
- Check maximum monthly average
- Check 30-day running average
- Identify exceedances

**Step 4: Evaluate Compliance**
- Pass: All criteria met
- Fail: Any exceedance requires redesign

## Failure Consequences and Redesign

When analysis shows non-compliance:

**Common Solutions**:

- Increase thermal resistance (reduce surface temperature depression)
- Relocate vapor control layer
- Add ventilation or drainage
- Modify interior humidity control
- Change materials to more vapor-open
- Add exterior insulation
- Improve air sealing

**Redesign Verification**: Rerun analysis with proposed modifications until compliance achieved.

## Relationship to Building Codes

ASHRAE 160 referenced by:

- International Energy Conservation Code (IECC)
- International Residential Code (IRC)
- Local jurisdictions for moisture control verification
- Green building rating systems (LEED, NGBS)

**Code Requirement**: Some jurisdictions mandate ASHRAE 160 analysis for assemblies with insulation exceeding code minimums or in moisture-prone climates.

## Limitations and Considerations

**Standard Limitations**:

- Addresses mold only, not structural moisture damage
- Assumes proper construction and installation
- Does not cover construction moisture
- Limited to normal occupancy patterns
- Does not address water intrusion events

**Conservative Nature**: The 80% RH limit at warm temperatures provides safety margin below actual mold germination thresholds (typically 85-95% RH).

**Professional Judgment**: Complex projects require experienced building science analysis beyond minimum standard compliance.

## Implementation Strategy

**Design Process Integration**:

1. Preliminary assembly design based on thermal performance
2. ASHRAE 160 analysis at design development
3. Iteration if non-compliant
4. Final verification before construction documents
5. Construction quality assurance to match design assumptions
6. Post-occupancy verification if concerns arise

**Quality Control**: Site inspections to verify proper installation of air barriers, vapor retarders, insulation continuity, and flashing details critical to moisture performance.
