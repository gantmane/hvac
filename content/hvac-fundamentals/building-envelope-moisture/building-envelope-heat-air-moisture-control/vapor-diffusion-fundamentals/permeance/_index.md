---
title: "Permeance"
aliases: ["Permeance"]
description: "Engineering fundamentals of vapor permeance including measurement units, material properties, temperature and humidity dependence, and application in building envelope moisture control design"
weight: 2
---

## Overview

Permeance quantifies the rate of water vapor transmission through a unit area of material under specified conditions of temperature and humidity differential. This property represents the material's actual resistance to vapor flow including thickness effects, distinguishing it from permeability which is a thickness-independent material property.

The permeance value directly determines the vapor resistance (or vapor retardance) of building assembly components and governs moisture migration patterns through multi-layer envelope systems. Understanding permeance characteristics enables accurate prediction of condensation risk, drying potential, and long-term hygrothermal performance.

## Fundamental Definition

Permeance (M) represents the time rate of water vapor transmission through unit area of flat material or construction induced by unit vapor pressure difference between two surfaces.

**Mathematical Expression:**

M = μ / t

Where:
- M = permeance (perm or metric perm)
- μ = permeability (perm-inch or metric perm-m)
- t = material thickness (inch or m)

**Flux Relationship:**

g = M × Δp

Where:
- g = water vapor flux (mass per unit area per unit time)
- M = permeance
- Δp = vapor pressure difference across material

## Unit Systems and Conversions

### Imperial Perms (US System)

**Definition:**

1 perm = 1 grain/(h·ft²·inHg)

This represents the passage of 1 grain of water vapor through 1 square foot of material in 1 hour under a vapor pressure differential of 1 inch of mercury.

**Alternative Expression:**

1 perm = 5.72135 × 10⁻¹¹ kg/(Pa·s·m²)

**Common Material Ranges:**

| Classification | Permeance Range | Examples |
|----------------|-----------------|----------|
| Vapor impermeable | ≤ 0.1 perm | Polyethylene film, aluminum foil, glass |
| Vapor semi-impermeable | 0.1 to 1.0 perm | Kraft-faced insulation, plywood, OSB |
| Vapor semi-permeable | 1.0 to 10 perm | Latex paint, gypsum board, building paper |
| Vapor permeable | > 10 perm | Unfaced insulation, kraft paper, unpainted drywall |

### Metric Perms (SI System)

**Definition:**

1 metric perm = 1 ng/(Pa·s·m²)

This represents the passage of 1 nanogram of water vapor through 1 square meter of material in 1 second under a vapor pressure differential of 1 Pascal.

**Conversion Factor:**

1 imperial perm = 57.2135 metric perms

1 metric perm = 0.01748 imperial perms

**SI Classification:**

| Classification | Metric Permeance Range | IRC/IBC Designation |
|----------------|------------------------|---------------------|
| Class I (impermeable) | ≤ 5.7 ng/(Pa·s·m²) | Vapor retarder |
| Class II (semi-impermeable) | 5.7 to 57 ng/(Pa·s·m²) | Vapor retarder |
| Class III (semi-permeable) | 57 to 575 ng/(Pa·s·m²) | Vapor retarder |
| Permeable | > 575 ng/(Pa·s·m²) | Not classified as retarder |

## Measurement Standards

### ASTM E96 - Water Vapor Transmission Testing

**Test Methods:**

**Desiccant Method (Procedure A):**
- Specimen sealed over cup containing desiccant
- Exposed to controlled humidity environment (typically 50% RH)
- Weight gain measured over time
- Provides dry cup permeance values

**Water Method (Procedure B):**
- Specimen sealed over cup containing water
- Exposed to controlled humidity environment
- Weight loss measured over time
- Provides wet cup permeance values

**Calculation:**

M = (ΔW × t) / (A × Δt × Δp)

Where:
- M = permeance (perm or metric perm)
- ΔW = weight change (mass)
- t = time interval
- A = test area
- Δt = elapsed time
- Δp = vapor pressure difference

**Test Conditions:**

| Procedure | Temperature | RH Gradient | Typical Use |
|-----------|-------------|-------------|-------------|
| Dry Cup | 73.4°F (23°C) | 0% to 50% RH | Cold climate, winter |
| Wet Cup | 90°F (32°C) | 50% to 100% RH | Hot humid climate, summer |

### ASTM C1147 - Liquid Moisture Permeability

Measures permeance to liquid water under hydrostatic pressure, applicable to materials that may experience direct wetting or capillary moisture transport.

## Temperature Dependence

Permeance exhibits temperature sensitivity due to vapor pressure-temperature relationships and material property variations.

**Temperature Effect Mechanisms:**

1. **Vapor Pressure Change:** Saturation vapor pressure increases exponentially with temperature (Clausius-Clapeyron)
2. **Material Expansion:** Pore structure may enlarge with thermal expansion
3. **Molecular Mobility:** Diffusion coefficients increase with temperature
4. **Sorption Isotherms:** Moisture content at given RH varies with temperature

**Approximate Temperature Correction:**

M(T₂) = M(T₁) × exp[E_a/R × (1/T₁ - 1/T₂)]

Where:
- M(T) = permeance at temperature T
- E_a = activation energy for diffusion (material-dependent)
- R = universal gas constant = 8.314 J/(mol·K)
- T = absolute temperature (K)

**Typical Temperature Coefficients:**

| Material Type | E_a Range | Permeance Change |
|---------------|-----------|------------------|
| Polymer films | 30-50 kJ/mol | 2-4% per °C |
| Cementitious | 15-25 kJ/mol | 1-2% per °C |
| Wood products | 20-40 kJ/mol | 1.5-3% per °C |
| Gypsum board | 10-20 kJ/mol | 0.8-1.5% per °C |

**Design Implications:**

- Permeance values typically reported at 73°F (23°C)
- Cold surface permeance may be 20-40% lower than warm surface
- Dynamic modeling should account for seasonal temperature variations
- Condensation analysis requires permeance at actual surface temperatures

## Humidity Dependence

Many hygroscopic materials exhibit significant permeance variation with relative humidity due to moisture content effects on diffusion pathways.

**Mechanisms:**

1. **Pore Filling:** Water molecules block vapor diffusion paths
2. **Swelling:** Moisture uptake expands material structure
3. **Liquid Transport Enhancement:** Capillary action supplements vapor diffusion
4. **Surface Resistance Change:** Adsorbed moisture layers affect boundary conditions

**Permeance-Humidity Relationship:**

M(φ) = M₀ × [1 + α × φⁿ]

Where:
- M(φ) = permeance at relative humidity φ
- M₀ = dry permeance
- α = humidity sensitivity coefficient
- n = empirical exponent (typically 1.5 to 3.0)

**Material Categories:**

| Material Type | Humidity Dependence | Wet/Dry Ratio |
|---------------|---------------------|---------------|
| Non-hygroscopic (polyethylene) | Negligible | 1.0 - 1.1 |
| Low hygroscopic (XPS) | Slight | 1.1 - 1.5 |
| Moderate hygroscopic (OSB, plywood) | Moderate | 1.5 - 3.0 |
| High hygroscopic (wood fiber, cellulose) | Strong | 3.0 - 10.0 |
| Variable retarders (smart membranes) | Engineered variation | 5.0 - 50.0 |

**Common Building Materials - Humidity Effect:**

| Material | Dry Cup (50% RH) | Wet Cup (90% RH) | Ratio |
|----------|------------------|------------------|-------|
| Plywood 1/4" | 0.5 perm | 1.5 perm | 3.0 |
| OSB 7/16" | 0.7 perm | 2.0 perm | 2.9 |
| Kraft paper | 3.0 perm | 10.0 perm | 3.3 |
| Latex paint (2 coats) | 5.0 perm | 8.0 perm | 1.6 |
| Smart vapor retarder | 0.8 perm | 20 perm | 25.0 |

## Permeability vs Permeance Relationship

**Permeability (μ):** Intrinsic material property independent of thickness

M = μ / t

**Example Calculation:**

Given: Polyethylene sheet, permeability = 0.06 perm-inch

Thickness 4 mil (0.004 inch):
M = 0.06 / 0.004 = 15 perm

Thickness 6 mil (0.006 inch):
M = 0.06 / 0.006 = 10 perm

Thickness 10 mil (0.010 inch):
M = 0.06 / 0.010 = 6 perm

**Series Resistance (Multi-layer Assemblies):**

For layers in series, vapor resistances add:

1/M_total = 1/M₁ + 1/M₂ + 1/M₃ + ... + 1/Mₙ

**Vapor Resistance (Z):**

Z = 1/M (units: rep = 1/perm)

Z_total = Z₁ + Z₂ + Z₃ + ... + Zₙ

**Example - Wall Assembly:**

| Layer | Permeance (perm) | Resistance (rep) |
|-------|------------------|------------------|
| Interior latex paint | 5.0 | 0.20 |
| Gypsum board 1/2" | 50.0 | 0.02 |
| Kraft-faced batt | 1.0 | 1.00 |
| OSB sheathing 7/16" | 2.0 | 0.50 |
| Weather barrier | 10.0 | 0.10 |
| **Total** | **0.55** | **1.82** |

M_total = 1 / (0.20 + 0.02 + 1.00 + 0.50 + 0.10) = 0.55 perm

## Material Property Data

### Common Building Materials - Permeance Values

**Sheathing Materials:**

| Material | Thickness | Permeance (perm) | Test Condition |
|----------|-----------|------------------|----------------|
| Plywood | 1/4" | 0.5 - 0.7 | Dry cup |
| Plywood | 1/2" | 0.3 - 0.5 | Dry cup |
| OSB | 7/16" | 0.7 - 1.0 | Dry cup |
| OSB | 7/16" | 2.0 - 3.0 | Wet cup |
| Fiber board 1/2" | 3.0 - 5.0 | 15 - 20 | Dry cup |
| Gypsum sheathing 1/2" | 15 - 20 | 50 - 60 | Wet cup |
| Densglass 1/2" | 10 - 12 | 20 - 25 | Dry cup |

**Vapor Retarder Materials:**

| Material | Thickness | Permeance (perm) | Classification |
|----------|-----------|------------------|----------------|
| Polyethylene | 6 mil | 0.06 | Class I |
| Polyethylene | 10 mil | 0.03 | Class I |
| Aluminum foil | 1 mil | 0.0 | Class I |
| Kraft facing | - | 0.3 - 0.5 | Class II |
| Asphalt-coated kraft | - | 0.2 - 0.4 | Class II |
| Smart membrane (dry) | - | 0.7 - 1.0 | Class II/III |
| Smart membrane (wet) | - | 20 - 40 | Permeable |

**Insulation Materials (unfaced):**

| Material | Permeance per inch | Notes |
|----------|-------------------|-------|
| Fiberglass batt | > 100 perm-inch | Essentially transparent |
| Mineral wool | > 100 perm-inch | Essentially transparent |
| Cellulose (dense-pack) | 50 - 80 perm-inch | Slight resistance |
| XPS (extruded polystyrene) | 3.5 - 5.0 perm-inch | Accumulates with thickness |
| EPS (expanded polystyrene) | 2.0 - 5.5 perm-inch | Variable by density |
| Polyisocyanurate (foil-faced) | 0.02 - 0.05 perm | Class I retarder |

**Interior Finishes:**

| Material | Application | Permeance (perm) |
|----------|-------------|------------------|
| Latex paint | 1 coat on drywall | 8 - 12 |
| Latex paint | 2 coats on drywall | 5 - 8 |
| Oil-based paint | 1 coat | 0.3 - 1.0 |
| Vinyl wallpaper | - | 0.5 - 1.5 |
| Vinyl wallcovering | - | 0.1 - 0.5 |
| Unpainted gypsum | 1/2" | 50 - 60 |

## Design Considerations

### Climate-Specific Requirements

**Cold Climate (Zones 5-8):**
- Interior vapor retarder (Class I or II) typically required
- Limit exterior impermeability to allow outward drying
- Consider condensation potential at sheathing
- Verify sufficient insulation to keep sheathing warm

**Mixed Climate (Zones 3-4):**
- Class II or III retarder preferred over Class I
- Allow bi-directional drying
- Smart retarders optimize seasonal performance
- Avoid double vapor barriers

**Hot-Humid Climate (Zones 1-2):**
- Interior vapor retarder often prohibited
- Exterior drainage and drying critical
- Interior should be more permeable than exterior
- Air conditioning drives inward vapor flow

### Permeance Ratio Method

The relative permeability of layers determines condensation risk.

**Criterion:**

M_interior / M_exterior ≥ 5:1 (cold climate)

M_exterior / M_interior ≥ 5:1 (hot-humid climate)

**Application:**

If interior is Class I retarder (M = 0.1 perm):
- Exterior must be M ≥ 0.5 perm (5× more permeable)

If exterior is Class II retarder (M = 0.5 perm):
- Interior should be M ≥ 2.5 perm (5× more permeable) in hot-humid climate

### Code Requirements

**IRC Section R702.7 (Vapor Retarders):**

Class I or II vapor retarder required on interior side in Climate Zones 5, 6, 7, 8, and Marine 4.

**Exceptions:**
1. Basement walls
2. Below-grade portions of walls
3. Construction with specific exterior materials meeting drainage criteria
4. Walls with sufficient vapor-permeable continuous insulation

**IBC/IECC:**

Similar requirements with specific climate zone applications and exceptions for assemblies meeting hygrothermal performance criteria.

### Assembly Analysis

**Glaser Method (Simplified):**

Plot vapor pressure profile through assembly:
1. Calculate temperature at each layer interface
2. Determine saturation vapor pressure at each temperature
3. Calculate actual vapor pressure based on permeance ratios
4. Condensation occurs where actual exceeds saturation

**Software Analysis:**

WUFI, MOISTURE-EXPERT, THERM, or hygIRC enable dynamic analysis accounting for:
- Transient temperature and humidity
- Material moisture storage capacity
- Liquid transport and capillary effects
- Solar-driven moisture redistribution
- Rainfall and wind-driven rain

## Advanced Considerations

### Variable Permeance Materials

Smart vapor retarders modify permeance based on ambient humidity:

**Mechanism:**
- Polyamide or cellulose-based films
- Hydrophilic properties cause swelling at high RH
- Increased permeance allows drying during high humidity periods
- Low permeance during heating season protects from interior moisture

**Performance Characteristics:**

| RH Condition | Permeance | Function |
|--------------|-----------|----------|
| 0-30% RH | 0.7 - 1.0 perm | Winter moisture protection |
| 30-50% RH | 2 - 5 perm | Transition |
| 50-80% RH | 10 - 30 perm | Moderate drying |
| 80-100% RH | 20 - 50 perm | Maximum drying potential |

**Applications:**
- Mixed and cold climates with air conditioning
- Retrofit applications where exterior permeance unknown
- Assemblies requiring bi-directional drying

### Air Leakage vs Vapor Diffusion

Convective moisture transport through air leakage paths typically exceeds diffusion by 10 to 100 times.

**Mass Transport Comparison:**

Vapor diffusion through 1000 ft² wall at 0.5 perm over winter:
g_diffusion ≈ 5-10 lb water

Air leakage at 0.1 CFM/ft² with same vapor pressure difference:
g_convection ≈ 50-200 lb water

**Design Priority:**
1. Air barrier continuity and detailing
2. Vapor retarder placement and class selection
3. Drying mechanisms and redundancy

### Material Aging Effects

**Degradation Mechanisms:**
- UV radiation (outdoor exposure)
- Mechanical damage during construction
- Chemical degradation (alkaline concrete)
- Biological growth (mold on organic facings)
- Thermal cycling stress

**Permeance Change Over Time:**

| Material | Initial | After 10 years | Change |
|----------|---------|----------------|--------|
| Polyethylene (protected) | 0.06 perm | 0.08 perm | +30% |
| Asphalt felt | 5 perm | 15 perm | +200% |
| Building paper | 10 perm | 25 perm | +150% |
| Latex paint | 6 perm | 12 perm | +100% |

**Design Approach:**
- Use conservative values for long-term performance
- Provide redundancy in critical assemblies
- Specify durable materials for permanent applications

## Quality Control and Verification

**Installation Considerations:**

1. **Continuity:** Vapor retarder must be continuous with sealed penetrations
2. **Overlap:** Minimum 6-inch overlap at seams
3. **Sealing:** Compatible tape, adhesive, or caulk at joints
4. **Penetrations:** Seal around electrical boxes, plumbing, HVAC
5. **Inspection:** Visual verification before covering

**Testing Methods:**

- ASTM E96: Laboratory permeance measurement
- ASTM E783: Field air leakage testing (pressure box)
- Infrared thermography: Identify moisture accumulation zones
- Moisture content monitoring: Long-term hygrothermal verification

## References and Standards

**ASTM Standards:**
- ASTM E96: Water Vapor Transmission of Materials
- ASTM C1147: Measuring Liquid Moisture Permeability
- ASTM E2178: Air Permeance of Building Materials

**Building Codes:**
- IRC Section R702.7: Vapor Retarders
- IBC Section 1404: Exterior Wall Coverings
- IECC: Climate-specific requirements

**Technical Resources:**
- ASHRAE Handbook - Fundamentals, Chapter 25: Heat, Air, and Moisture Control
- ASHRAE Standard 160: Criteria for Moisture-Control Design Analysis
- Building Science Corporation: Moisture control guidance documents

**Industry Guidelines:**
- Canadian Mortgage and Housing Corporation (CMHC) Best Practice Guides
- Oak Ridge National Laboratory: Moisture control research
- Building America: Hygrothermal performance protocols
