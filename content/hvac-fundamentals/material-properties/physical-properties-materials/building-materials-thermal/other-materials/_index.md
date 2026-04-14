---
title: "Other Building Materials"
aliases: ["Other Building Materials"]
description: "Thermal properties of glass, ceramics, composites, membranes, gypsum, and earth materials used in HVAC load calculations and envelope design"
weight: 5
---

## Overview

Building envelope materials beyond conventional insulation and structural components significantly impact HVAC load calculations and system performance. Glass, ceramics, roofing membranes, gypsum products, and earth materials each exhibit distinct thermal behaviors that influence heat transfer, thermal mass effects, and overall building energy performance.

Accurate thermal property data for these materials enables proper load calculations per ASHRAE Fundamentals and ensures compliance with energy codes including ASHRAE 90.1, IECC, and Title 24.

## Glass and Glazing Materials

### Window Glass

Glass exhibits high thermal conductivity compared to typical insulation materials, making it a critical component in building envelope thermal performance.

#### Thermal Properties

**Standard float glass:**

| Glass Type | Thickness (mm) | k (W/m·K) | c (J/kg·K) | ρ (kg/m³) | α (m²/s × 10⁻⁷) |
|------------|----------------|-----------|------------|-----------|------------------|
| Clear float | 3 | 1.0 | 750 | 2500 | 5.3 |
| Clear float | 6 | 1.0 | 750 | 2500 | 5.3 |
| Clear float | 12 | 1.0 | 750 | 2500 | 5.3 |
| Tinted | 6 | 0.9-1.0 | 750 | 2500 | 4.8-5.3 |
| Low-iron | 6 | 1.0 | 750 | 2500 | 5.3 |

where:
- k = thermal conductivity
- c = specific heat capacity
- ρ = density
- α = thermal diffusivity

**Low-emissivity coatings:**

Low-e coatings reduce radiative heat transfer but do not significantly alter the glass substrate thermal conductivity. The coating layer (typically 100-300 nm) affects surface emissivity (ε):

- Uncoated glass: ε = 0.84
- Hard-coat low-e: ε = 0.15-0.20
- Soft-coat low-e: ε = 0.04-0.10

#### Insulating Glass Units (IGU)

The effective thermal resistance of IGU assemblies depends on:

1. **Gas fill thermal conductivity** (W/m·K at 10°C):
   - Air: k = 0.0241
   - Argon: k = 0.0163 (32% lower than air)
   - Krypton: k = 0.0088 (63% lower than air)
   - Xenon: k = 0.0051 (79% lower than air)

2. **Gap width optimization:**
   - Air/argon: optimum 12-16 mm
   - Krypton: optimum 8-10 mm (allows thinner profiles)
   - Below optimum: increased conduction
   - Above optimum: increased convection

3. **Edge effects:**
   - Aluminum spacers: k = 160 W/m·K (thermal bridge)
   - Stainless steel spacers: k = 17 W/m·K
   - Insulated spacers: k = 0.2-0.3 W/m·K

#### Solar Heat Gain Considerations

While not purely thermal conduction properties, solar optical characteristics directly affect HVAC cooling loads:

| Glass Type | SHGC | Visible Transmittance | U-factor (W/m²·K) |
|------------|------|----------------------|-------------------|
| Single clear | 0.86 | 0.90 | 5.8 |
| Double clear | 0.76 | 0.81 | 2.8 |
| Double low-e | 0.32-0.70 | 0.70-0.80 | 1.4-1.7 |
| Triple low-e | 0.28-0.50 | 0.65-0.75 | 0.8-1.1 |

Reference: ASHRAE Handbook—Fundamentals, Chapter 15: Fenestration

#### Temperature Limits

- Standard annealed glass: continuous service to 100°C
- Tempered glass: continuous service to 250°C
- Thermal shock resistance: 40-50°C for annealed, 200°C for tempered
- Glass stress failure occurs at temperature differentials >20°C across pane

### Glass Block

Glass block walls provide daylighting with improved thermal performance versus standard glazing.

**Thermal properties:**

| Block Type | Dimensions (mm) | U-factor (W/m²·K) | SHGC | Light Transmission |
|------------|-----------------|-------------------|------|-------------------|
| Standard hollow | 190 × 190 × 80 | 2.8-3.2 | 0.48-0.56 | 0.60-0.70 |
| Low-e coated | 190 × 190 × 80 | 2.0-2.3 | 0.41-0.48 | 0.55-0.65 |
| Argon filled | 190 × 190 × 80 | 1.8-2.1 | 0.44-0.51 | 0.58-0.68 |

The glass itself: k = 1.0 W/m·K, but the assembly includes air space and mortar joints.

### Specialty Glass

**Fire-rated glass:**
- Wired glass: k = 1.0 W/m·K (wire has negligible impact on bulk conductivity)
- Ceramic glass: k = 1.1-1.3 W/m·K
- Intumescent interlayer systems: k = 0.9-1.0 W/m·K (base glass)

**Security glazing:**
- Laminated glass: k = 0.95-1.0 W/m·K (PVB interlayer: k = 0.17 W/m·K)
- Impact-resistant: k = 1.0 W/m·K (multiple glass plies with polymer interlayers)

## Ceramic Materials

### Clay Brick and Tile

Fired clay products exhibit variable thermal properties based on density and firing temperature.

**Solid clay brick:**

| Density (kg/m³) | k (W/m·K) | c (J/kg·K) | Thermal Mass (kJ/m³·K) |
|-----------------|-----------|------------|------------------------|
| 1600 | 0.60-0.70 | 920 | 1472 |
| 1800 | 0.70-0.80 | 920 | 1656 |
| 2000 | 0.80-0.90 | 920 | 1840 |
| 2200 | 0.90-1.00 | 920 | 2024 |

**Hollow clay tile:**

| Product | Density (kg/m³) | k (W/m·K) | R-value (m²·K/W per 100mm) |
|---------|-----------------|-----------|----------------------------|
| Standard hollow | 1200-1400 | 0.40-0.50 | 0.20-0.25 |
| Structural tile | 1400-1600 | 0.50-0.60 | 0.17-0.20 |

#### Temperature Performance

- Continuous service: up to 800°C for standard brick
- Thermal expansion coefficient: 5-7 × 10⁻⁶ /°C
- High thermal mass provides beneficial thermal lag in diurnal temperature swings
- Time lag for 200mm brick wall: approximately 8-10 hours

### Ceramic Tile and Porcelain

**Wall and floor tile:**

| Material | k (W/m·K) | c (J/kg·K) | ρ (kg/m³) | Typical Thickness (mm) |
|----------|-----------|------------|-----------|------------------------|
| Ceramic tile | 1.0-1.3 | 840 | 2300 | 6-10 |
| Porcelain tile | 1.2-1.5 | 880 | 2400 | 8-12 |
| Quarry tile | 1.0-1.2 | 850 | 2200 | 12-20 |

**Thin-set mortar adhesive:**
- k = 0.7-0.9 W/m·K
- Typical thickness: 3-6 mm
- Contributes minimal thermal resistance

**Grout:**
- Cementitious grout: k = 0.9-1.1 W/m·K
- Epoxy grout: k = 0.3-0.5 W/m·K

#### HVAC Design Considerations

1. **Thermal mass impact:**
   - Ceramic floors provide thermal storage for radiant heating systems
   - High heat capacity moderates temperature swings
   - Porcelain: volumetric heat capacity = 2.11 MJ/m³·K

2. **Radiant system response:**
   - Higher conductivity improves surface temperature uniformity
   - Thermal diffusivity affects system response time
   - 12mm porcelain over radiant: response time ≈ 1.5-2 hours

3. **Condensation risk:**
   - Low vapor permeability creates moisture barrier
   - Surface temperature must remain above dew point
   - Critical in humid climates and pool environments

## Gypsum Products

### Gypsum Wallboard (Drywall)

Standard gypsum board consists of gypsum plaster core between paper facing layers.

**Thermal properties:**

| Product Type | k (W/m·K) | c (J/kg·K) | ρ (kg/m³) | R-value (m²·K/W per 12.7mm) |
|--------------|-----------|------------|-----------|----------------------------|
| Regular | 0.16-0.17 | 1090 | 640 | 0.079 |
| Type X (fire-rated) | 0.17-0.18 | 1090 | 730 | 0.074 |
| Moisture-resistant | 0.16-0.17 | 1090 | 660 | 0.079 |
| Foil-backed | 0.16 (core) | 1090 | 640 | 0.079 + foil |

**Foil-backed enhancement:**
- Adds reflective air space resistance
- Requires minimum 19mm air space
- Additional R = 0.44 m²·K/W (foil facing 19mm air space)

#### Moisture Effects

Thermal conductivity increases significantly with moisture content:

| Moisture Content (% by mass) | k (W/m·K) | Increase vs. Dry |
|------------------------------|-----------|------------------|
| 0 (oven dry) | 0.16 | baseline |
| 1 | 0.19 | +19% |
| 5 | 0.28 | +75% |
| 10 | 0.42 | +163% |

Water has k = 0.60 W/m·K, dramatically increasing heat transfer through wetted gypsum.

#### Fire Performance

Type X gypsum board contains glass fiber reinforcement and other additives:
- 15.9mm (5/8"): 1-hour fire rating
- Gypsum dehydration endothermic reaction absorbs heat
- Releases chemically bound water at 100-150°C, creating steam barrier

### Gypsum Plaster

**Three-coat system thermal properties:**

| Layer | Thickness (mm) | k (W/m·K) | ρ (kg/m³) |
|-------|----------------|-----------|-----------|
| Scratch coat | 6-10 | 0.22-0.25 | 1200 |
| Brown coat | 6-10 | 0.22-0.25 | 1200 |
| Finish coat | 2-3 | 0.20-0.22 | 1150 |

**Total assembly:**
- 19mm three-coat plaster: R = 0.086 m²·K/W
- Higher density than drywall provides greater thermal mass
- Volumetric heat capacity: 1.32-1.38 MJ/m³·K

### Gypsum Sheathing

Exterior gypsum sheathing used in wall assemblies:

| Product | k (W/m·K) | ρ (kg/m³) | Water Resistance |
|---------|-----------|-----------|------------------|
| Regular sheathing | 0.17 | 730 | Limited |
| Weather-resistant | 0.17 | 730 | Enhanced |
| Glass mat faced | 0.17 | 730 | High |

The glass mat facing (not paper) provides weather protection but does not alter thermal properties.

## Composite Materials

### Fiber-Reinforced Polymer (FRP)

FRP panels used in humid environments (kitchens, pools, healthcare) have distinct thermal properties.

**Material properties:**

| Matrix/Reinforcement | k (W/m·K) | c (J/kg·K) | ρ (kg/m³) | α (m²/s × 10⁻⁷) |
|---------------------|-----------|------------|-----------|------------------|
| Polyester/fiberglass | 0.25-0.30 | 1200 | 1600 | 1.3-1.6 |
| Vinyl ester/fiberglass | 0.28-0.33 | 1150 | 1650 | 1.5-1.7 |
| Epoxy/fiberglass | 0.30-0.40 | 1100 | 1700 | 1.6-2.1 |

**Thickness:** typically 1.0-2.5mm over substrate

**Temperature limits:**
- Polyester matrix: continuous service to 80°C
- Vinyl ester: continuous service to 95°C
- Epoxy: continuous service to 120°C
- Heat deflection temperature: 95-180°C depending on formulation

### Fiber-Cement Panels

Fiber-cement cladding and siding materials:

**Thermal properties:**

| Product Density (kg/m³) | k (W/m·K) | c (J/kg·K) | R-value (m²·K/W per 12mm) |
|-------------------------|-----------|------------|---------------------------|
| 1400 | 0.30-0.35 | 1050 | 0.034-0.040 |
| 1600 | 0.35-0.40 | 1050 | 0.030-0.034 |
| 1800 | 0.40-0.45 | 1050 | 0.027-0.030 |

**Characteristics:**
- Non-combustible (reaction-to-fire class A1)
- Stable thermal properties across temperature range -40°C to +80°C
- Low thermal expansion: 6-8 × 10⁻⁶ /°C
- Moisture-stable thermal performance

### Phenolic Foam Composites

Rigid phenolic foam boards and faced panels:

**Core thermal properties:**

| Density (kg/m³) | k (W/m·K) | c (J/kg·K) | R-value (m²·K/W per 25mm) |
|-----------------|-----------|------------|---------------------------|
| 35-40 | 0.018-0.020 | 1400 | 1.25-1.39 |
| 50-60 | 0.020-0.022 | 1400 | 1.14-1.25 |

**Faced panels:**
- Aluminum foil facers: add vapor barrier, improve R-value
- Glass tissue facers: improve fire performance
- Composite facers: k = 0.020-0.023 W/m·K (overall assembly)

**Temperature performance:**
- Continuous service: -180°C to +120°C
- Fire performance: self-extinguishing, low smoke
- Aging: k increases 5-10% over 25 years as cell gas diffuses

## Roofing Membranes

### Single-Ply Membranes

Flexible roofing membranes exhibit low thermal resistance but affect total roof assembly performance.

**EPDM (Ethylene Propylene Diene Monomer):**

| Property | Value |
|----------|-------|
| k (W/m·K) | 0.23-0.25 |
| c (J/kg·K) | 2000 |
| ρ (kg/m³) | 1150-1250 |
| Typical thickness | 1.1-2.3 mm |
| Color options | Black, white, tan |

**PVC (Polyvinyl Chloride):**

| Property | Value |
|----------|-------|
| k (W/m·K) | 0.16-0.19 |
| c (J/kg·K) | 1050 |
| ρ (kg/m³) | 1300-1500 |
| Typical thickness | 1.1-2.0 mm |
| Color options | White, tan, gray (white most common) |

**TPO (Thermoplastic Polyolefin):**

| Property | Value |
|----------|-------|
| k (W/m·K) | 0.17-0.20 |
| c (J/kg·K) | 1800 |
| ρ (kg/m³) | 1100-1300 |
| Typical thickness | 1.1-2.0 mm |
| Color options | White, tan, gray |

#### Thermal Resistance

Individual membrane R-values are negligible:
- 1.5mm EPDM: R = 0.006 m²·K/W
- 1.5mm PVC: R = 0.008 m²·K/W
- 1.5mm TPO: R = 0.008 m²·K/W

#### Solar Reflectance Impact

Membrane color significantly affects cooling loads via solar reflectance:

| Membrane Type/Color | Solar Reflectance | Thermal Emittance | SRI |
|---------------------|-------------------|-------------------|-----|
| Black EPDM | 0.06 | 0.86 | 1 |
| White EPDM | 0.69 | 0.87 | 84 |
| White PVC | 0.83 | 0.92 | 104 |
| White TPO | 0.85 | 0.90 | 106 |
| Tan TPO | 0.45 | 0.90 | 50 |

SRI = Solar Reflectance Index per ASTM E1980

**Cooling load impact:**
- White membrane vs. black can reduce roof surface temperature by 30-50°C on summer day
- Peak heat flux reduction: 50-80 W/m² for well-insulated roof
- Greater impact on poorly insulated roofs

#### Temperature Limits

**Service temperature ranges:**
- EPDM: -45°C to +150°C (brief exposure)
- PVC: -35°C to +80°C continuous, +105°C brief
- TPO: -40°C to +115°C continuous

**Heat welding temperatures:**
- PVC: 425-650°C (hot air welding)
- TPO: 540-600°C (hot air welding)
- EPDM: solvent or tape bonded (not heat welded)

### Built-Up Roofing (BUR)

Asphalt and tar-based systems with aggregate surfacing.

**Typical assembly layers:**

| Layer | k (W/m·K) | Thickness (mm) |
|-------|-----------|----------------|
| Asphalt (bitumen) | 0.17 | 3-5 per ply |
| Organic felt | 0.06 | 1.0-1.5 per ply |
| Fiberglass felt | 0.04 | 0.8-1.2 per ply |
| Gravel surfacing | 0.8-1.2 | 10-20 |
| Asphalt flood coat | 0.17 | 5-8 |

**Four-ply assembly thermal properties:**
- Total thickness: approximately 15-20mm
- Effective k: 0.12-0.16 W/m·K
- R-value: 0.094-0.167 m²·K/W

**Aggregate surfacing impact:**
- Provides thermal mass and UV protection
- Light-colored gravel increases solar reflectance
- Gravel holds moisture, maintaining cooler roof temperature via evaporation

### Modified Bitumen

**APP (Atactic Polypropylene):**
- k = 0.17-0.20 W/m·K
- Thickness: 3-4mm
- Heat applied installation
- Service temperature: -30°C to +120°C

**SBS (Styrene-Butadiene-Styrene):**
- k = 0.17-0.19 W/m·K
- Thickness: 3-4mm
- Heat or cold applied
- Service temperature: -45°C to +135°C
- Superior low-temperature flexibility

## Asphalt Shingles

Composition shingles widely used in residential steep-slope roofing.

### Thermal Properties

**Standard three-tab shingles:**

| Property | Value |
|----------|-------|
| k (W/m·K) | 1.1-1.3 |
| c (J/kg·K) | 1200 |
| ρ (kg/m³) | 1100-1300 |
| Thickness | 3-4 mm |
| R-value | 0.003 m²·K/W (negligible) |

**Architectural (dimensional) shingles:**
- Thickness: 6-8mm at thickest point
- Similar k values
- Slight additional thermal mass

### Solar Reflectance Properties

Shingle color dramatically affects attic and cooling loads:

| Shingle Color | Solar Reflectance | Surface Temperature Increase |
|---------------|-------------------|------------------------------|
| Black | 0.03-0.05 | +60-70°C above ambient |
| Dark brown | 0.08-0.12 | +55-65°C above ambient |
| Medium brown | 0.15-0.20 | +45-55°C above ambient |
| Light tan | 0.25-0.30 | +35-45°C above ambient |
| White | 0.25-0.35 | +30-40°C above ambient |
| "Cool" colors | 0.25-0.40 | +25-40°C above ambient |

**Cool roof shingles:**
- Specially formulated pigments increase solar reflectance
- ENERGY STAR rated steep-slope products: SR ≥ 0.25 (initial)
- Can reduce attic temperature by 10-20°C versus standard dark shingles
- Cooling load reduction: 10-20% in cooling-dominated climates

### Composition and Structure

**Material layers:**
1. Mineral granules (ceramic-coated): weather protection, color, solar reflectance
2. Asphalt coating: waterproofing
3. Fiberglass mat: reinforcement (k ≈ 0.04 W/m·K)
4. Asphalt coating: adhesion
5. Back surface treatment: anti-stick coating

**Temperature performance:**
- Service range: -45°C to +110°C
- Surface temperature on black shingle: can exceed 80°C
- Thermal cycling drives aging and degradation

## Earth Materials

### Soil Thermal Properties

Soil thermal characteristics vary dramatically with moisture content, density, and mineral composition.

**Dry soil (moisture content <5% by mass):**

| Soil Type | k (W/m·K) | c (J/kg·K) | ρ (kg/m³) | Thermal Mass (kJ/m³·K) |
|-----------|-----------|------------|-----------|------------------------|
| Sand | 0.30-0.40 | 800 | 1600 | 1280 |
| Silt | 0.25-0.35 | 850 | 1500 | 1275 |
| Clay | 0.25-0.30 | 880 | 1400 | 1232 |
| Loam | 0.25-0.35 | 830 | 1500 | 1245 |
| Gravel | 0.40-0.50 | 750 | 1800 | 1350 |

**Moist soil (moisture content 15-25% by mass):**

| Soil Type | k (W/m·K) | c (J/kg·K) | ρ (kg/m³) | Thermal Mass (kJ/m³·K) |
|-----------|-----------|------------|-----------|------------------------|
| Sand | 1.5-2.0 | 1480 | 1900 | 2812 |
| Silt | 1.3-1.8 | 1520 | 1850 | 2812 |
| Clay | 1.1-1.5 | 1550 | 1750 | 2713 |
| Loam | 1.2-1.7 | 1500 | 1850 | 2775 |
| Gravel | 1.8-2.5 | 1400 | 2000 | 2800 |

**Saturated soil (moisture content >30% by mass):**

| Soil Type | k (W/m·K) | Increase vs. Dry |
|-----------|-----------|------------------|
| Sand | 2.0-3.0 | +500-650% |
| Silt | 1.8-2.5 | +520-610% |
| Clay | 1.3-2.0 | +420-570% |
| Loam | 1.5-2.5 | +430-610% |

Water content dominates thermal behavior: k(water) = 0.60 W/m·K versus k(air) = 0.025 W/m·K.

#### HVAC Applications

**Earth-coupled systems:**

1. **Ground-source heat pumps:**
   - Require accurate soil k for ground loop sizing
   - In-situ thermal conductivity testing recommended for large systems
   - IGSHPA guidelines specify thermal response testing for systems >50 kW
   - Typical design assumption: k = 1.5-2.5 W/m·K for moist soils

2. **Earth-sheltered construction:**
   - Soil thermal mass moderates temperature swings
   - Annual temperature amplitude at depth z: A(z) = A₀ × exp(-z/d)
   - Damping depth: d = √(α × P / π) where P = 365 days
   - For typical soil α = 0.05 × 10⁻⁶ m²/s: d ≈ 2.1 m
   - Temperature stable at depth >3-4 m (approximately mean annual air temperature)

3. **Underslab insulation design:**
   - Soil heat loss path must be considered
   - Higher moisture content increases heat loss
   - Perimeter insulation more critical than center-of-slab

**Temperature variation with depth:**

| Depth (m) | Annual Amplitude Reduction | Phase Lag (days) |
|-----------|---------------------------|------------------|
| 0 (surface) | 100% | 0 |
| 0.5 | 78% | 15 |
| 1.0 | 61% | 30 |
| 2.0 | 37% | 60 |
| 3.0 | 22% | 90 |
| 4.0 | 14% | 120 |

### Compacted Fill and Base Materials

**Crushed stone/gravel base:**
- k = 0.8-1.5 W/m·K (dry)
- k = 1.5-2.2 W/m·K (moist)
- High drainage reduces moisture content and k
- Used under slabs and earth-coupled heat exchangers

**Controlled low-strength material (CLSM):**
- k = 1.0-1.4 W/m·K
- Flowable fill used around underground piping
- Provides uniform thermal contact for buried thermal systems

### Rammed Earth and Adobe

**Rammed earth walls:**

| Density (kg/m³) | k (W/m·K) | c (J/kg·K) | Thermal Mass (MJ/m³·K) |
|-----------------|-----------|------------|------------------------|
| 1700 | 0.70-0.90 | 1000 | 1.70 |
| 1900 | 0.85-1.10 | 1000 | 1.90 |
| 2100 | 1.00-1.30 | 1000 | 2.10 |

**Adobe brick:**
- k = 0.50-0.70 W/m·K
- ρ = 1400-1600 kg/m³
- c = 950-1050 J/kg·K
- High thermal mass benefits in climates with large diurnal temperature swings

**Thermal performance:**
- R-value: 0.20-0.30 m²·K/W per 300mm thickness
- Time lag: 10-12 hours for 300-400mm wall
- Decrement factor: 0.15-0.25 (significant peak load reduction)

## Temperature Correction Factors

Thermal conductivity varies with temperature. For most building materials:

k(T) = k₀ × [1 + β(T - T₀)]

where:
- k₀ = reference conductivity at T₀ (typically 20°C)
- β = temperature coefficient (1/K)

**Typical β values:**
- Glass: β = 0.0001 to 0.0005 /K
- Ceramic materials: β = 0.0002 to 0.0008 /K
- Gypsum: β = 0.0015 to 0.0025 /K
- Polymers: β = 0.002 to 0.005 /K
- Soil (dry): β = 0.001 to 0.002 /K

For temperature range 0-40°C encountered in most building applications, correction is typically <5% and often neglected in load calculations.

## ASHRAE and Code References

**Primary references:**

1. **ASHRAE Handbook—Fundamentals, Chapter 26: Heat, Air, and Moisture Control in Building Assemblies—Material Properties**
   - Tables 1-3: Thermal properties of building materials
   - Methodology for effective assembly properties

2. **ASHRAE Handbook—Fundamentals, Chapter 15: Fenestration**
   - Window thermal and optical properties
   - NFRC rating procedures
   - Solar heat gain calculations

3. **ASHRAE Standard 90.1: Energy Standard for Buildings Except Low-Rise Residential Buildings**
   - Minimum thermal performance requirements
   - Fenestration U-factor and SHGC criteria by climate zone

4. **ASTM C177: Standard Test Method for Steady-State Heat Flux Measurements and Thermal Transmission Properties by Means of the Guarded-Hot-Plate Apparatus**
   - Reference method for thermal conductivity determination

5. **ASTM C518: Standard Test Method for Steady-State Thermal Transmission Properties by Means of the Heat Flow Meter Apparatus**
   - Alternative test method for thermal conductivity

6. **NFRC 100: Procedure for Determining Fenestration Product U-factors**
   - Standard window thermal performance rating

7. **IGSHPA Design and Installation Standards**
   - Ground thermal properties for geothermal systems

## Design Considerations

### Load Calculation Accuracy

1. **Use appropriate material properties:**
   - Reference ASHRAE Fundamentals tables
   - Account for moisture effects in humid climates
   - Consider aging effects for foam insulations

2. **Fenestration dominates envelope performance:**
   - Window area and properties critical in load calculations
   - SHGC more important than U-factor in cooling-dominated buildings
   - Properly model shading devices and overhangs

3. **Thermal mass impacts peak loads:**
   - Materials with high ρ × c reduce peak loads and shift timing
   - Important for thermal storage systems
   - Radiant time series method accounts for mass effects

### Assembly Performance

1. **Material layers interact:**
   - Series thermal resistance: R_total = Σ R_i
   - Parallel heat flow paths reduce effective R-value
   - Air films and cavities contribute significant resistance

2. **Air barriers and vapor retarders:**
   - Convective loops in air spaces increase effective k
   - Moisture accumulation degrades performance
   - Proper sequencing of materials prevents condensation

3. **Thermal bridging:**
   - Metal components create parallel high-conductivity paths
   - Steel studs, window frames, balcony connections
   - Isothermal planes method or finite element analysis for complex geometry

### System Selection

1. **Radiant systems require conductive surfaces:**
   - Ceramic tile excellent for radiant floors (k = 1.0-1.5 W/m·K)
   - Carpet poor for radiant (k = 0.05-0.08 W/m·K with pad)
   - Surface material affects system capacity and control response

2. **Cool roof selection:**
   - Mandatory in some jurisdictions (Title 24, ASHRAE 90.1 Climate Zones 1-3)
   - Greater benefit for buildings with high roof-to-wall ratio
   - Consider aesthetics, especially for steep-slope applications

3. **Ground-coupled systems:**
   - Require site-specific soil thermal properties
   - Thermal conductivity testing for systems >100 kW
   - Soil moisture content varies seasonally—impacts performance

### Moisture Management

1. **Hygroscopic materials:**
   - Gypsum, wood, earth materials absorb moisture
   - Thermal conductivity increases 50-100% at high humidity
   - Can lead to mold growth and IAQ issues

2. **Vapor drive:**
   - Materials with low vapor permeability trap moisture
   - Vapor retarder placement depends on climate
   - Avoid double vapor barriers

3. **Interstitial condensation:**
   - Occurs when vapor pressure exceeds saturation in assembly
   - Dew point analysis required for cold climates
   - Insulation placement affects condensation risk

## Summary

Thermal properties of glass, ceramics, composites, membranes, gypsum, and earth materials significantly impact HVAC system design and energy performance. Key considerations include:

- **Glass thermal conductivity** (k = 1.0 W/m·K) creates fenestration heat loss/gain; low-e coatings and insulating gas fills improve performance
- **Ceramic materials** provide high thermal mass (ρc = 1.8-2.1 MJ/m³·K), beneficial for load shifting and radiant systems
- **Gypsum products** offer moderate insulation (k = 0.16-0.17 W/m·K) but performance degrades significantly with moisture
- **Roofing membranes** provide negligible R-value but color/reflectance dramatically affects cooling loads (ΔT = 30-50°C)
- **Soil thermal properties** vary by factor of 5-8 with moisture content, critical for ground-coupled systems
- **Accurate material data** from ASHRAE Fundamentals and testing per ASTM standards ensures proper load calculations and system sizing

Understanding these properties enables HVAC professionals to perform accurate load calculations, optimize system selection, and design energy-efficient building envelopes that meet code requirements and performance objectives.
