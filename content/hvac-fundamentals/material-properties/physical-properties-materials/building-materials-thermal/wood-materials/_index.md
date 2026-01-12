---
title: "Wood Materials"
description: "Thermal properties of softwood, hardwood, and engineered wood products including conductivity, specific heat, moisture effects, and temperature-density relationships for HVAC load calculations"
weight: 2
---

Wood materials constitute a significant component of building envelopes and structural systems. Their thermal properties vary considerably based on species, grain orientation, density, moisture content, and temperature. Accurate characterization of wood thermal behavior is essential for precise heat transfer calculations in HVAC design.

## Fundamental Thermal Properties

### Thermal Conductivity Range

Wood thermal conductivity varies with multiple factors:

**Density Effects:**
- Low density woods (< 400 kg/m³): k = 0.10-0.13 W/(m·K)
- Medium density woods (400-600 kg/m³): k = 0.13-0.17 W/(m·K)
- High density woods (> 600 kg/m³): k = 0.17-0.23 W/(m·K)

**Grain Orientation:**
- Parallel to grain: k‖ = 2.0 to 2.8 times perpendicular conductivity
- Perpendicular to grain: k⊥ (baseline reference)
- Radial direction: typically 5-10% higher than tangential
- Most heat transfer calculations use perpendicular values (conservative)

### Specific Heat Capacity

Wood specific heat varies with moisture content and temperature:

**Dry Wood (0% moisture content):**
- cp,dry = 1200-1400 J/(kg·K) at 20°C
- Temperature dependence: cp = 1030 + 3.9T (T in °C)

**Moist Wood:**
- cp,moist = cp,dry + mc × cp,water
- Where mc = moisture content (decimal)
- cp,water = 4186 J/(kg·K)

**Practical Values:**
- Oven-dry wood: 1300 J/(kg·K)
- 6% MC (typical interior): 1380 J/(kg·K)
- 12% MC (typical exterior): 1500 J/(kg·K)
- 20% MC (high humidity): 1750 J/(kg·K)

### Density Classifications

**Oven-Dry Density (ρ₀):**
- Mass of wood substance / volume at given moisture content
- Fundamental property for thermal calculations

**Moisture Content Effects:**
- ρ = ρ₀(1 + mc)
- Below fiber saturation point (FSP ≈ 28-30%)
- Dimensional changes accompany moisture changes

## Softwood Species

Softwoods (coniferous species) generally exhibit lower density and thermal conductivity compared to hardwoods.

### Common Softwood Properties

**Douglas Fir (Pseudotsuga menziesii):**
- Density: 480-530 kg/m³ (oven-dry)
- k⊥: 0.12-0.14 W/(m·K) at 12% MC
- k‖: 0.27-0.34 W/(m·K)
- Specific heat: 1380 J/(kg·K)
- Widely used in structural framing

**Southern Yellow Pine (Pinus spp.):**
- Density: 510-590 kg/m³
- k⊥: 0.14-0.15 W/(m·K) at 12% MC
- k‖: 0.32-0.38 W/(m·K)
- High resin content affects moisture behavior
- Common in dimensional lumber

**Spruce-Pine-Fir (SPF) Group:**
- Density: 360-450 kg/m³
- k⊥: 0.10-0.12 W/(m·K) at 12% MC
- k‖: 0.22-0.28 W/(m·K)
- Lower thermal conductivity due to lower density
- Standard framing lumber in cold climates

**Western Red Cedar (Thuja plicata):**
- Density: 310-370 kg/m³
- k⊥: 0.09-0.11 W/(m·K)
- Excellent insulating properties
- Naturally durable, used in exterior applications

**Hemlock (Tsuga spp.):**
- Density: 400-480 kg/m³
- k⊥: 0.11-0.13 W/(m·K)
- Moderate thermal resistance
- Used in framing and sheathing

### Softwood Design Values

For HVAC calculations, use these conservative values:

| Application | k [W/(m·K)] | ρ [kg/m³] | cp [J/(kg·K)] |
|-------------|-------------|-----------|---------------|
| Framing (2×4, 2×6) | 0.12 | 450 | 1380 |
| Structural timbers | 0.13 | 500 | 1380 |
| Siding | 0.11 | 420 | 1400 |
| Interior trim | 0.10 | 400 | 1350 |

## Hardwood Species

Hardwoods (deciduous species) generally have higher density and thermal conductivity, affecting thermal mass and heat transfer rates.

### Common Hardwood Properties

**Oak (Quercus spp.):**
- Red Oak density: 630-720 kg/m³
- White Oak density: 690-770 kg/m³
- k⊥: 0.16-0.18 W/(m·K)
- k‖: 0.35-0.42 W/(m·K)
- High thermal mass, used in flooring

**Maple (Acer spp.):**
- Hard Maple density: 630-710 kg/m³
- k⊥: 0.16-0.17 W/(m·K)
- Common in flooring and interior finish

**Ash (Fraxinus spp.):**
- Density: 600-680 kg/m³
- k⊥: 0.15-0.17 W/(m·K)
- Similar properties to oak

**Birch (Betula spp.):**
- Yellow Birch density: 620-680 kg/m³
- k⊥: 0.15-0.16 W/(m·K)
- Used in cabinets and millwork

**Walnut (Juglans nigra):**
- Density: 550-660 kg/m³
- k⊥: 0.14-0.16 W/(m·K)
- Premium interior applications

### Hardwood Design Values

| Application | k [W/(m·K)] | ρ [kg/m³] | cp [J/(kg·K)] |
|-------------|-------------|-----------|---------------|
| Hardwood flooring | 0.16 | 650 | 1400 |
| Interior paneling | 0.15 | 600 | 1380 |
| Cabinetry | 0.16 | 630 | 1400 |
| Millwork | 0.15 | 620 | 1390 |

## Engineered Wood Products

Engineered wood products consist of wood elements bonded with adhesives. Thermal properties depend on composition, density, and manufacturing process.

### Plywood

**Construction:**
- Cross-laminated veneer layers
- Alternating grain orientation
- Adhesive bonds between layers

**Thermal Properties:**
- Density: 450-650 kg/m³ (varies by species and voids)
- k: 0.12-0.14 W/(m·K) perpendicular to face
- Effective isotropic behavior due to cross-lamination
- Specific heat: 1380 J/(kg·K)

**HVAC Applications:**
- Sheathing: use k = 0.12 W/(m·K)
- Subfloors: use k = 0.13 W/(m·K)
- Interior paneling: use k = 0.11 W/(m·K)

**Common Types:**
- CDX plywood (sheathing): ρ = 500 kg/m³, k = 0.12 W/(m·K)
- Marine plywood: ρ = 600 kg/m³, k = 0.13 W/(m·K)
- Hardwood plywood: ρ = 550 kg/m³, k = 0.13 W/(m·K)

### Oriented Strand Board (OSB)

**Construction:**
- Wood strands oriented in layers
- Phenolic resin binder
- Compressed under heat and pressure

**Thermal Properties:**
- Density: 600-680 kg/m³
- k: 0.13-0.14 W/(m·K)
- Higher density than plywood of equal thickness
- Specific heat: 1400 J/(kg·K)

**Design Values:**
- Wall sheathing: k = 0.13 W/(m·K), ρ = 640 kg/m³
- Roof sheathing: k = 0.13 W/(m·K), ρ = 650 kg/m³
- Subfloor: k = 0.14 W/(m·K), ρ = 660 kg/m³

**Moisture Sensitivity:**
- More susceptible to edge swelling than plywood
- Affects dimensional stability and thermal bridging
- Critical in moisture-control designs

### Particleboard

**Construction:**
- Wood particles bonded with resin
- Uniform density distribution
- Lower strength than OSB or plywood

**Thermal Properties:**
- Density: 600-750 kg/m³
- k: 0.17-0.18 W/(m·K)
- Higher conductivity due to compression
- Specific heat: 1420 J/(kg·K)

**Applications:**
- Underlayment: k = 0.17 W/(m·K)
- Core stock: k = 0.18 W/(m·K)
- Shelving: k = 0.17 W/(m·K)

### Medium Density Fiberboard (MDF)

**Construction:**
- Fine wood fibers bonded with resin
- Uniform, dense structure
- Smooth surface finish

**Thermal Properties:**
- Density: 700-850 kg/m³
- k: 0.18-0.20 W/(m·K)
- Highest conductivity of common engineered woods
- Specific heat: 1450 J/(kg·K)

**Design Considerations:**
- Thermal mass higher than solid wood of equal volume
- Used in interior applications (trim, cabinetry)
- Not suitable for direct exterior exposure
- Standard value: k = 0.19 W/(m·K), ρ = 750 kg/m³

### Laminated Veneer Lumber (LVL)

**Construction:**
- Thin wood veneers laminated with grain parallel
- Used in structural applications (beams, headers)

**Thermal Properties:**
- Density: 550-650 kg/m³
- k‖: 0.28-0.35 W/(m·K) (along length)
- k⊥: 0.13-0.15 W/(m·K) (through thickness)
- Acts as thermal bridge in wall assemblies

**HVAC Impact:**
- Headers over openings create thermal bridges
- Parallel grain orientation increases heat flow along length
- Consider thermal break strategies in high-performance assemblies

### Glulam Beams

**Construction:**
- Laminated dimensional lumber
- Grain parallel in all layers

**Thermal Properties:**
- Density: 500-550 kg/m³
- k‖: 0.30-0.38 W/(m·K)
- k⊥: 0.12-0.14 W/(m·K)
- Similar to solid wood of same species

## Moisture Content Effects

Moisture profoundly affects wood thermal properties through multiple mechanisms.

### Thermal Conductivity and Moisture

**Relationship:**
- k = k₀[1 + (mc/100)(α)]
- Where α = 2.5 to 3.5 for most species
- k₀ = conductivity at 0% MC

**Physical Mechanism:**
- Water conductivity: kwater = 0.60 W/(m·K) at 20°C
- Water replaces air in cell structure (kair = 0.026 W/(m·K))
- Net increase in effective conductivity

**Practical Impact:**
- 12% MC increases k by 25-35% vs oven-dry
- 20% MC increases k by 50-70% vs oven-dry
- Critical for exterior applications and high-humidity spaces

### Moisture Content Guidelines

**Equilibrium Moisture Content (EMC):**
- Interior conditioned space: 6-9% MC
- Exterior in temperate climate: 12-15% MC
- High humidity environments: 16-20% MC

**Design Values by Application:**

| Location | EMC (%) | k Multiplier |
|----------|---------|--------------|
| Interior heated | 6-8 | 1.20 |
| Interior unheated | 10-12 | 1.30 |
| Exterior protected | 12-15 | 1.35 |
| Exterior exposed | 15-20 | 1.50 |

### Fiber Saturation Point

**Definition:**
- Moisture content where cell walls are saturated but no free water exists
- Typically 28-30% MC for most species
- Above FSP, dimensional changes cease

**Thermal Implications:**
- Conductivity increases continue above FSP
- Latent heat effects become significant
- Condensation risk in assemblies

## Temperature Effects

Wood thermal properties vary with temperature, though effects are less pronounced than moisture.

### Conductivity Temperature Dependence

**Relationship:**
- k(T) = k₂₀[1 + β(T - 20)]
- Where β = 0.002 to 0.003 K⁻¹
- T = temperature (°C)

**Practical Range:**
- -20°C to +50°C: conductivity increases 15-20%
- Effect is secondary to moisture content changes
- Most design standards use 20°C reference

### Specific Heat Temperature Dependence

**Dry Wood:**
- cp(T) = 1030 + 3.9T [J/(kg·K)]
- Linear relationship over HVAC temperature range
- At -20°C: cp ≈ 952 J/(kg·K)
- At +50°C: cp ≈ 1225 J/(kg·K)

### Combined Temperature-Moisture Effects

**Interactive Effects:**
- Higher temperatures increase EMC at given RH
- Thermal conductivity increases with both T and MC
- Design calculations should account for seasonal extremes

**Example Calculation:**
- SPF framing, interior winter: T = 20°C, MC = 7%
  - k = 0.12 × 1.18 = 0.14 W/(m·K)
- Same framing, summer exterior face: T = 50°C, MC = 14%
  - k = 0.12 × 1.35 × 1.05 = 0.17 W/(m·K)

## Density-Property Relationships

Density serves as the primary predictor of wood thermal properties.

### Empirical Correlations

**Thermal Conductivity:**
- k = 0.04 + 0.00026ρ [W/(m·K)]
- Valid for ρ in kg/m³, MC = 12%
- Perpendicular to grain orientation

**Alternative Form:**
- k = 0.01w + 0.1 [W/(m·K)]
- Where w = specific gravity (relative to water)

**Thermal Diffusivity:**
- α = k/(ρcp)
- Decreases with increasing density
- Typical range: (0.8-1.5) × 10⁻⁷ m²/s

### Species Comparison

| Species | ρ [kg/m³] | k [W/(m·K)] | α [m²/s × 10⁻⁷] |
|---------|-----------|-------------|------------------|
| Balsa | 120 | 0.05 | 2.5 |
| Cedar | 350 | 0.10 | 1.5 |
| SPF | 420 | 0.12 | 1.3 |
| Douglas Fir | 500 | 0.13 | 1.2 |
| Oak | 680 | 0.17 | 1.0 |
| Lignum Vitae | 1100 | 0.25 | 0.8 |

## ASHRAE References

### ASHRAE Handbook - Fundamentals

**Chapter 26: Heat, Air, and Moisture Control in Building Assemblies:**
- Table 4: Thermal properties of building materials
- Wood species thermal conductivity data
- Moisture effects on conductivity

**Chapter 33: Energy Resources:**
- Wood as fuel source properties
- Heating values and combustion characteristics

**Standard Values (ASHRAE Table 26.4):**
- Softwood lumber (80 lb/ft³): k = 0.12 W/(m·K), R = 1.25 per inch
- Hardwood (45 lb/ft³): k = 0.16 W/(m·K), R = 0.91 per inch
- Plywood (34 lb/ft³): k = 0.12 W/(m·K), R = 1.25 per inch
- Particleboard (50 lb/ft³): k = 0.17 W/(m·K), R = 0.85 per inch

### ASHRAE Standard 90.1

**Envelope Requirements:**
- Wood framing thermal bridging calculations
- Parallel path method for framed assemblies
- Clear wall vs whole wall R-values

**Framing Factors:**
- 2×4 @ 16" O.C.: 15-20% framing
- 2×6 @ 16" O.C.: 15-20% framing
- 2×4 @ 24" O.C.: 10-15% framing

## Code References

### International Energy Conservation Code (IECC)

**Thermal Performance:**
- Wood framing assumed at R-1.25 per inch (softwood)
- Advanced framing techniques reduce thermal bridging
- Continuous insulation strategies

### International Residential Code (IRC)

**Prescriptive Requirements:**
- Framing member thermal properties
- Wall assembly calculations
- Foundation wood sill plates

### Building Codes

**Fire Resistance:**
- Wood charring rates affect thermal barrier
- Typical char rate: 0.6-0.8 mm/min
- Char layer provides insulation

## HVAC Design Considerations

### Heat Transfer Calculations

**Framed Wall Assemblies:**
- Parallel path method accounts for wood framing
- Effective R-value lower than cavity insulation alone
- Framing fraction typically 15-25%

**Calculation Method:**
1. Identify framing fraction (Ff) and cavity fraction (Fc)
2. Calculate U-value through framing path: Uframe = Σ(1/R)
3. Calculate U-value through cavity path: Ucavity = Σ(1/R)
4. Effective U = FfUframe + FcUcavity
5. Effective R = 1/U

**Example:**
- 2×6 wall, R-21 cavity insulation, 20% framing
- Framing path: R = 1.0 (exterior) + 6.9 (stud) + 0.68 (interior) = 8.58
  - Uframe = 0.117 W/(m²·K)
- Cavity path: R = 1.0 + 21 + 0.68 = 22.68
  - Ucavity = 0.044 W/(m²·K)
- Ueff = 0.20(0.117) + 0.80(0.044) = 0.0584 W/(m²·K)
- Reff = 17.1 (compared to R-22.68 nominal)

### Thermal Bridging

**Common Bridge Locations:**
- Studs and joists penetrating insulation
- Headers over windows and doors
- Rim joists and band boards
- Sill plates and bottom plates

**Mitigation Strategies:**
- Continuous exterior insulation
- Advanced framing (24" O.C., single top plate)
- Insulated headers
- Thermal breaks at critical junctions

### Moisture Management

**Condensation Risk:**
- Wood framing members as condensing surfaces
- Dew point analysis required in cold climates
- Vapor retarder placement critical

**Design Approach:**
1. Calculate temperature profile through assembly
2. Determine dew point temperature at each interface
3. Compare actual temperature to dew point
4. If Tactual < Tdew, condensation occurs

**Hygrothermal Modeling:**
- WUFI or similar software for dynamic analysis
- Accounts for moisture storage in wood
- Validates assembly performance over annual cycle

### Thermal Mass Effects

**Lightweight Wood Frame:**
- Low thermal mass compared to masonry or concrete
- Minimal heat storage capacity
- Faster temperature response

**Quantification:**
- Thermal mass per unit area: M = ρcpL
- 2×6 stud wall: M ≈ 3.5 kJ/(m²·K) of framing area
- Negligible compared to conditioned space loads

**Design Implications:**
- Less effective for passive solar thermal storage
- Reduced peak load shifting capability
- Lower temperature swing damping

### Load Calculations

**Envelope Transmission:**
- Use effective U-value accounting for framing
- Apply area-weighted average for assemblies
- Consider orientation-specific solar gains

**Thermal Bridging Impact:**
- Increases heating loads 10-30% vs clear wall
- Greater impact in high-performance envelopes
- Critical for net-zero and passive house designs

**Dynamic Effects:**
- Wood structures respond quickly to setback/setup
- Lower recovery loads compared to mass construction
- Shorter time constants for transient analysis

### Flooring Systems

**Wood Floor Over Conditioned Space:**
- Minimal heat transfer impact
- Thermal comfort driven by surface temperature
- Radiant floor heating compatibility

**Wood Floor Over Unconditioned Space:**
- Significant heat loss pathway
- Requires insulation below
- Cantilever conditions create thermal bridges

**Design Values:**
- 3/4" hardwood flooring: R = 0.67
- 3/4" softwood flooring: R = 0.90
- Subfloor typically adds R = 1.0 to 1.3

### Ceiling and Roof Assemblies

**Cathedral Ceilings:**
- Wood rafter thermal bridging
- Ventilation channel requirements
- Insulation depth limitations

**Attic Floor:**
- Wood joists bridge insulation
- Lower impact due to full cavity insulation
- Effective R-value reduction typically 2-5%

## Advanced Considerations

### Anisotropic Heat Flow

**Grain Orientation Effects:**
- Parallel grain conductivity 2-3× perpendicular
- Important in heavy timber construction
- Glulam beams act as thermal highways

**Finite Element Analysis:**
- Required for complex geometries
- Orthotropic material properties
- Transient heat transfer in mass timber

### Mass Timber Systems

**Cross-Laminated Timber (CLT):**
- Alternating layer orientation
- Effective isotropic behavior in plane
- Through-thickness: k ≈ 0.13 W/(m·K)

**Nail-Laminated Timber (NLT):**
- All layers same orientation
- Highly anisotropic thermal properties
- Requires directional analysis

**Thermal Mass:**
- Significant compared to light frame
- CLT panel: M = 40-80 kJ/(m²·K) for 175mm thickness
- Affects peak load timing and magnitude

### Fire Effects

**Charring:**
- Surface char forms insulating layer
- Reduces heat penetration to interior wood
- Char conductivity: k ≈ 0.05 W/(m·K)

**Temperature-Dependent Properties:**
- Wood decomposes above 200-300°C
- Thermal properties change significantly
- Specialized analysis required for fire scenarios

### Hygrothermal Coupling

**Moisture Transport:**
- Vapor diffusion through wood
- Capillary action in wood structure
- Liquid water movement

**Latent Heat Effects:**
- Evaporation/condensation within assembly
- Affects effective thermal properties
- Dynamic heat and moisture transfer analysis

## Summary Design Values

### Quick Reference Table

| Material | k [W/(m·K)] | ρ [kg/m³] | cp [J/(kg·K)] | Application Notes |
|----------|-------------|-----------|---------------|-------------------|
| Softwood framing | 0.12 | 450 | 1380 | Studs, joists, rafters @ 12% MC |
| Hardwood flooring | 0.16 | 650 | 1400 | Interior finish floors |
| Plywood sheathing | 0.12 | 500 | 1380 | Wall/roof sheathing |
| OSB sheathing | 0.13 | 640 | 1400 | Wall/roof/floor sheathing |
| Particleboard | 0.17 | 700 | 1420 | Underlayment, core stock |
| MDF | 0.19 | 750 | 1450 | Interior trim, millwork |
| LVL/Glulam (⊥) | 0.14 | 600 | 1380 | Structural beams, headers |
| LVL/Glulam (‖) | 0.33 | 600 | 1380 | Along beam length |

### Standard Conditions

All values at:
- Temperature: 20°C (68°F)
- Moisture content: 12% (typical building interior)
- Perpendicular to grain (except where noted)

Adjust for actual site conditions using correction factors provided in moisture and temperature sections.

