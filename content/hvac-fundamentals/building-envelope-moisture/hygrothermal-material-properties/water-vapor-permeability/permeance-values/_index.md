---
title: "Permeance Values"
description: "Classification system for material vapor permeance ratings, including Class I, II, and III vapor retarders with quantitative permeance thresholds and application guidelines for building envelope moisture control."
weight: 2
---

Permeance values quantify the rate of water vapor transmission through materials, enabling systematic classification of vapor retarders and informed selection of building envelope components. The International Residential Code and International Building Code establish three permeance classes that govern material placement and assembly design.

## Permeance Classification System

The building code classification system divides materials based on steady-state water vapor transmission characteristics:

| Class | Permeance Range | Permeance (SI Units) | Vapor Retarder Type | Typical Applications |
|-------|----------------|---------------------|---------------------|---------------------|
| Class I | ≤0.1 perm | ≤5.75 × 10⁻¹² kg/Pa·s·m² | Vapor impermeable | Vapor barriers, extreme climate control |
| Class II | 0.1 to 1.0 perm | 5.75 × 10⁻¹² to 5.75 × 10⁻¹¹ | Vapor semi-impermeable | Moderate vapor control with drying |
| Class III | 1.0 to 10 perm | 5.75 × 10⁻¹¹ to 5.75 × 10⁻¹⁰ | Vapor semi-permeable | Balanced vapor/drying performance |
| Permeable | >10 perm | >5.75 × 10⁻¹⁰ kg/Pa·s·m² | Vapor permeable | Maximum drying capacity |

## Units and Conversions

Permeance expresses material-specific vapor transmission independent of thickness, measured in standard and SI units:

**IP Units (perms)**:
- 1 perm = 1 grain/(hr·ft²·in.Hg)
- Traditional engineering practice in North America
- Referenced in ASHRAE Handbook and building codes

**SI Units**:
- 1 perm = 5.75 × 10⁻¹¹ kg/(Pa·s·m²)
- International standard for scientific literature
- Required for compliance with ISO standards

**Metric perms** (occasionally used):
- 1 metric perm = 1 grain/(hr·m²·mmHg)
- 1 metric perm = 0.659 perm (IP)

## Relationship to Permeability

Permeance (M) relates to permeability (μ) through material thickness:

M = μ / t

Where:
- M = permeance (perm)
- μ = permeability coefficient (perm·inch)
- t = thickness (inches)

**Critical distinctions**:
- Permeability: intensive material property independent of specimen thickness
- Permeance: extensive property accounting for installed thickness
- Design calculations use permeance for assemblies, permeability for material comparisons

## Climate-Based Selection Criteria

Code-compliant vapor retarder class selection depends on climate zone and assembly configuration:

**Cold climates** (IECC Zones 6-8):
- Class I or II interior vapor retarder typically required
- Exceptions for certain wall constructions with exterior insulation
- Interior vapor control prevents winter condensation on cold sheathing

**Marine climates** (Zone 4 Marine):
- Class III or lower interior permeance recommended
- High exterior permeance enables outward drying
- Accommodates inward solar-driven vapor during summer

**Mixed-humid climates** (Zones 3-4A):
- Class III interior recommended, Class I/II prohibited without analysis
- Bidirectional vapor drive requires drying capacity both directions
- Painted gypsum board (medium permeance) standard practice

**Hot-humid climates** (Zones 1-2):
- Interior vapor retarders prohibited or restricted
- Exterior low-permeance cladding requires interior permeability
- Air conditioning creates inward vapor drive

## Testing Standards

ASTM E96 "Standard Test Methods for Water Vapor Transmission of Materials" establishes permeance measurement protocols:

**Desiccant (dry cup) method**:
- Specimen sealed over cup containing desiccant
- Placed in controlled humidity chamber
- Weight gain indicates vapor transmission
- Used for high-permeance materials (>1 perm)

**Water (wet cup) method**:
- Specimen sealed over cup containing water
- Exposed to low-humidity environment
- Weight loss indicates vapor transmission
- Used for low-permeance materials (<1 perm)

**Test conditions**:
- Standard: 73.4°F (23°C), 50% RH
- High humidity: 90°F (32.2°C), 90% RH for hot-humid applications
- Low temperature: 40°F (4.4°C), 50% RH for cold climate verification

## Assembly Permeance Calculations

Multi-layer assemblies exhibit series resistance behavior analogous to electrical circuits:

**Series resistance equation**:
1/M_total = 1/M₁ + 1/M₂ + 1/M₃ + ... + 1/Mₙ

**Example calculation** for wall assembly:
- Gypsum board 1/2" painted (10 perm): R = 1/10 = 0.10
- Fiberglass batt (>100 perm): R = 0 (negligible)
- OSB sheathing 7/16" (0.7 perm): R = 1/0.7 = 1.43
- Housewrap (50 perm): R = 1/50 = 0.02
- Total resistance: R_total = 0.10 + 0 + 1.43 + 0.02 = 1.55
- Assembly permeance: M_total = 1/1.55 = 0.65 perm

The lowest-permeance layer dominates total assembly resistance, typically the OSB sheathing or interior paint system.

## Moisture Load Implications

Permeance values directly determine steady-state vapor flux under given boundary conditions:

**Moisture flux equation**:
G = M × ΔP_v

Where:
- G = moisture flux (grains/hr·ft²)
- M = permeance (perm)
- ΔP_v = vapor pressure difference (in.Hg)

**Example**: 1000 ft² wall, 0.5 in.Hg vapor pressure difference, 0.7 perm assembly:
- Daily moisture transmission: 0.7 × 0.5 × 1000 × 24 = 8,400 grains/day = 1.2 lb/day
- Annual moisture load: 438 lb/year

## Variable Permeance Materials

Some materials exhibit permeance that varies with relative humidity, providing "smart" vapor control:

**Hygroscopically responsive materials**:
- Kraft paper: 0.4 perm dry, 2.0 perm at 90% RH
- OSB: 0.7 perm dry, 3.0 perm at 80% RH
- Certain polymeric membranes: 0.8 perm winter, 10+ perm summer

**Performance benefits**:
- Low permeance during peak heating (dry indoor conditions)
- High permeance during cooling season (humid indoor conditions)
- Self-regulating response to seasonal vapor drive direction

## Quality Assurance

Specification and verification of permeance values requires:
- Third-party testing per ASTM E96 at representative conditions
- Manufacturer technical data sheets with certified permeance values
- Installation inspection to verify continuous coverage
- Consideration of aging effects (UV degradation, thermal cycling)
- Field testing for critical applications using in-situ moisture monitoring

Proper application of permeance classification enables climate-appropriate assembly design that balances moisture protection with essential drying capacity.
