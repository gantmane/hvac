---
title: "Vapor Diffusion Fundamentals"
aliases: ["Vapor Diffusion Fundamentals"]
description: "Comprehensive analysis of vapor diffusion physics, Fick's Law, permeance ratings, vapor retarder classifications, and dewpoint analysis for building envelope moisture control in HVAC systems."
weight: 2
---

Vapor diffusion represents the molecular transport of water vapor through materials in response to vapor pressure gradients. This mechanism accounts for 1-2% of moisture transport in typical building envelopes, with air leakage dominating at 98-99%, yet vapor diffusion drives condensation risk analysis and vapor retarder design.

## Vapor Diffusion Physics

Water vapor molecules migrate through porous materials via diffusion, moving from regions of high vapor pressure to regions of low vapor pressure. This process occurs independently of air movement and follows Fick's First Law of Diffusion:

**q = -μA(dp/dx)**

Where:
- q = vapor flow rate (grains/hr or kg/s)
- μ = permeability coefficient (perm-inch or ng/(s·m·Pa))
- A = area perpendicular to flow (ft² or m²)
- dp/dx = vapor pressure gradient (in Hg/in or Pa/m)

The negative sign indicates flow in the direction of decreasing vapor pressure. This relationship parallels Fourier's Law for heat conduction, with vapor pressure gradient driving moisture flow as temperature gradient drives heat flow.

## Vapor Pressure Gradients

Vapor pressure difference across building envelope assemblies creates the driving force for diffusion. Vapor pressure is the partial pressure exerted by water vapor in air and depends on temperature and relative humidity:

**p_v = φ × p_sat(T)**

Where:
- p_v = vapor pressure (Pa or in Hg)
- φ = relative humidity (decimal)
- p_sat(T) = saturation vapor pressure at temperature T

Saturation vapor pressure increases exponentially with temperature according to the Clausius-Clapeyron equation. At 70°F (21°C), saturation vapor pressure equals 0.739 in Hg (2503 Pa). At 32°F (0°C), it drops to 0.18 in Hg (610 Pa).

Critical insight: Warm air holds substantially more moisture than cold air. A 70°F interior at 40% RH (p_v = 0.296 in Hg) drives vapor outward during winter toward cold exterior surfaces. Summer conditions reverse this gradient in air-conditioned buildings.

## Permeability and Permeance

**Permeability (μ)** quantifies a material's intrinsic resistance to vapor diffusion, independent of thickness. Units: perm-inch (US) or ng/(s·m·Pa) (SI).

**Permeance (M)** describes vapor transmission through a specific thickness of material:

**M = μ/d**

Where:
- M = permeance (perm)
- μ = permeability (perm-inch)
- d = thickness (inches)

One perm equals one grain of water vapor transmitted per hour through one square foot of material per inch of mercury vapor pressure difference (1 perm = 57.4 ng/(s·m²·Pa) in SI units).

For composite assemblies with multiple layers in series, total resistance equals the sum of individual resistances:

**1/M_total = 1/M₁ + 1/M₂ + ... + 1/M_n**

This parallels thermal resistance calculations for series assemblies.

## Material Permeance Values

| Material | Thickness | Permeance (perm) | Classification |
|----------|-----------|------------------|----------------|
| Polyethylene sheet | 6 mil | 0.06 | Class I |
| Polyethylene sheet | 4 mil | 0.08 | Class I |
| Aluminum foil | 1 mil | 0.05 | Class I |
| Kraft-faced batt insulation | — | 0.4-1.0 | Class II |
| Asphalt-coated kraft paper | — | 0.5 | Class II |
| Plywood | 3/8 in | 0.7 | Class II |
| Plywood | 1/2 in | 0.5 | Class II |
| OSB | 7/16 in | 0.7-2.0 | Class II/III |
| Gypsum board (unpainted) | 1/2 in | 50 | Class III |
| Gypsum board (latex paint) | 1/2 in | 5-20 | Class III |
| Gypsum board (oil paint) | 1/2 in | 0.3-1.5 | Class I/II |
| Expanded polystyrene | 1 in | 2-5 | Class III |
| Extruded polystyrene | 1 in | 0.5-1.0 | Class II |
| Polyisocyanurate (foil-faced) | 1 in | 0.05 | Class I |
| Concrete block (8 in, unpainted) | 8 in | 2.4 | Class III |
| Brick masonry | 4 in | 0.8 | Class II |
| Building paper (asphalt-felt) | 15 lb | 5 | Class III |
| Housewrap (spun polyolefin) | — | 40-60 | Class III |

## Vapor Retarder Classifications

The International Residential Code (IRC) and International Building Code (IBC) classify vapor retarders into three classes based on permeance:

**Class I Vapor Retarders (Impermeable):**
- Permeance ≤ 0.1 perm
- Examples: Polyethylene sheet, aluminum foil, rubber membrane, foil-faced polyiso
- Applications: Cold climates (Zones 5-8) on interior side of insulation
- Risk: Traps moisture in assemblies; avoid in mixed-humid or hot climates

**Class II Vapor Retarders (Semi-Impermeable):**
- Permeance > 0.1 and ≤ 1.0 perm
- Examples: Kraft facing, extruded polystyrene, certain paints
- Applications: Moderate climates (Zones 4-5); provides diffusion resistance with some drying capacity
- Advantage: Balances inward and outward drying potential

**Class III Vapor Retarders (Semi-Permeable):**
- Permeance > 1.0 and ≤ 10 perm
- Examples: Latex paint on gypsum board, unfaced insulation, housewrap
- Applications: Hot-humid climates (Zones 1-3); allows bi-directional drying
- Code requirement: IRC permits Class III on interior in Zones 1-3 and marine Zone 4

Materials exceeding 10 perm are vapor-permeable and not classified as vapor retarders.

## Dewpoint Analysis Methods

Dewpoint temperature represents the temperature at which air becomes saturated (RH = 100%) and condensation begins. Dewpoint analysis predicts condensation risk within wall assemblies.

**Dewpoint Calculation:**

For a given vapor pressure p_v, dewpoint temperature T_d follows:

**T_d = (243.04 × α) / (17.625 - α)**

Where α = ln(p_v/611.2) and p_v is in Pascals.

**Temperature Profile Analysis:**

1. Calculate steady-state temperature distribution through assembly using thermal resistances
2. Calculate vapor pressure at each interface using interior/exterior conditions
3. Determine saturation vapor pressure at each interface based on temperature
4. Compare actual vapor pressure to saturation vapor pressure
5. Condensation occurs where actual vapor pressure exceeds saturation vapor pressure

**Glaser Method (Manual Calculation):**

The Glaser diagram plots vapor pressure and saturation vapor pressure across assembly thickness:

- Horizontal axis: cumulative vapor resistance (1/perm)
- Vertical axis: vapor pressure
- Actual vapor pressure plots as straight line from interior to exterior conditions
- Saturation vapor pressure curve follows temperature profile
- Intersection indicates condensation plane and quantity

**WUFI and Hygrothermal Modeling:**

Advanced modeling accounts for:
- Transient conditions (daily/seasonal cycles)
- Moisture storage in materials
- Capillary transport
- Solar-driven moisture
- Wind-driven rain

These factors significantly affect real-world performance beyond steady-state Glaser calculations.

## Climate Zone Considerations

**Cold Climates (IECC Zones 5-8):**
- Dominant moisture drive: outward during winter
- Strategy: Class I or II vapor retarder on interior (warm side)
- Risk: Interior vapor retarders trap summer moisture from air conditioning
- Solution: Exterior insulation or reservoir cladding for inward drying

**Mixed Climates (IECC Zone 4):**
- Seasonal reversal of moisture drive
- Strategy: Class II retarder or "smart" vapor retarders
- Risk: Both inward and outward condensation potential
- Solution: Balance vapor resistance; allow bi-directional drying

**Hot-Humid Climates (IECC Zones 1-3):**
- Dominant moisture drive: inward during cooling season
- Strategy: No interior vapor retarder or Class III only
- Risk: Impermeable interior finishes trap moisture
- Solution: Vapor-permeable interior; control exterior moisture with drainage plane and air barrier

**Marine Climates (IECC Zone 4 Marine):**
- Moderate temperatures with high humidity
- Strategy: Class III interior vapor retarder permitted
- Risk: Limited drying potential in both directions
- Solution: Emphasis on drainage and air sealing

## Vapor Retarder Placement

Proper vapor retarder location depends on climate and assembly construction:

**Traditional Rule (Zones 5-8):**
Install vapor retarder on warm-in-winter side (interior in heating climates).

**Modern Approach:**
1. Place vapor retarder on side with greater vapor pressure (typically heating-dominated side)
2. Ensure 5:1 ratio of drying capacity to wetting capacity
3. Avoid vapor barriers on both sides of assembly ("double vapor barrier")
4. Use materials with appropriate permeance for expected conditions

**Continuous Exterior Insulation:**
When exterior insulation R-value exceeds minimum values per code, interior vapor retarder requirements relax. Exterior insulation raises interior surface of sheathing above dewpoint, preventing condensation.

| Climate Zone | Min. Exterior R-Value (Wall) | Interior Vapor Retarder |
|--------------|------------------------------|------------------------|
| 5 | R-5 | Class III permitted |
| 6 | R-7.5 | Class III permitted |
| 7 | R-10 | Class III permitted |
| 8 | R-12.5 | Class III permitted |

## Smart Vapor Retarders

Variable-permeance membranes adjust permeance based on ambient relative humidity:
- Low RH (winter): 0.5-1.0 perm (restrict outward flow)
- High RH (summer): 5-10+ perm (allow inward drying)

This adaptive behavior addresses seasonal moisture drive reversal in mixed climates while maintaining code compliance based on dry-cup permeance testing.

## Design Recommendations

1. **Prioritize air sealing:** Air leakage transports 50-100 times more moisture than vapor diffusion
2. **Conduct dewpoint analysis** for climate-specific assemblies
3. **Avoid Class I vapor retarders** except in severe cold climates (Zones 6-8)
4. **Never install impermeable materials on both sides** of moisture-sensitive assemblies
5. **Coordinate vapor retarder with insulation location** and type
6. **Consider occupancy moisture loads:** High-moisture spaces require adjusted strategies
7. **Detail continuity** of vapor retarder at penetrations and transitions
8. **Account for assembly-specific factors:** Reservoir cladding, ventilated cavities, and capillary breaks affect moisture performance

Vapor diffusion analysis forms one component of comprehensive hygrothermal design. Integration with air barrier design, water management, and thermal control ensures durable, moisture-safe building envelope assemblies.
