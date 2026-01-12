---
title: "Masonry Materials"
description: "Thermal properties of masonry materials including brick, concrete, CMU, and stone for HVAC load calculations and building envelope analysis"
weight: 1
---

Masonry materials represent a critical category of building envelope components characterized by high thermal mass, variable thermal conductivity, and significant moisture sensitivity. These materials include brick, concrete, concrete masonry units (CMU), stone, mortar, and plaster, each exhibiting distinct thermophysical properties that influence building heat transfer and thermal storage behavior.

## Fundamental Thermal Properties

### Thermal Conductivity Overview

Masonry thermal conductivity varies significantly based on material composition, density, moisture content, and temperature. The thermal conductivity (k) determines the rate of heat transfer through a material under steady-state conditions according to Fourier's law:

q = -k × A × (dT/dx)

Where:
- q = heat transfer rate (W)
- k = thermal conductivity (W/m·K)
- A = cross-sectional area (m²)
- dT/dx = temperature gradient (K/m)

Moisture content dramatically affects thermal conductivity. Water has a thermal conductivity approximately 25 times higher than air, so moisture migration into porous masonry structures significantly increases heat transfer rates.

## Brick Materials

### Common Brick

Common brick, also known as building brick, is manufactured primarily for structural applications and typically exhibits lower density than face brick.

**Thermal Properties:**
- Thermal conductivity: 0.40 to 0.70 W/m·K (dry conditions)
- Density: 1600 to 1920 kg/m³
- Specific heat capacity: 840 to 920 J/kg·K
- Thermal diffusivity: 0.30 to 0.45 × 10⁻⁶ m²/s

**Moisture Effects:**
At 5% moisture content by volume, thermal conductivity increases by approximately 30-50%. At saturation (15-20% moisture), conductivity may double compared to dry conditions.

**Design Considerations:**
- Common brick typically used in multi-wythe wall assemblies
- High thermal mass provides beneficial load shifting in moderate climates
- Requires proper moisture control to maintain insulating value
- Thermal bridging occurs through mortar joints (10-15% of wall area)

### Face Brick

Face brick is manufactured with tighter density control and lower porosity for exterior applications, resulting in higher thermal conductivity.

**Thermal Properties:**
- Thermal conductivity: 1.20 to 1.40 W/m·K (dry conditions)
- Density: 2000 to 2240 kg/m³
- Specific heat capacity: 900 to 1000 J/kg·K
- Thermal diffusivity: 0.60 to 0.75 × 10⁻⁶ m²/s

**Performance Characteristics:**
- Lower moisture absorption than common brick (3-8% vs 10-15%)
- Provides durable weather-resistant surface
- Higher thermal conductivity necessitates additional insulation in climate zones 4 and above
- Contributes 4 to 8 hours of thermal lag in mass wall assemblies

## Concrete Materials

### Normal Weight Concrete

Normal weight concrete consists of Portland cement, water, sand, and coarse aggregates (gravel or crushed stone), producing densities of 2200 to 2400 kg/m³.

**Thermal Properties (ASHRAE Fundamentals):**
- Thermal conductivity: 1.40 to 2.00 W/m·K
- Density: 2240 to 2400 kg/m³
- Specific heat capacity: 880 to 1050 J/kg·K
- Thermal diffusivity: 0.70 to 1.00 × 10⁻⁶ m²/s

**Concrete Mix Design Impact:**

| Aggregate Type | k (W/m·K) | Density (kg/m³) | Notes |
|---------------|-----------|-----------------|-------|
| Limestone | 1.40-1.70 | 2240-2320 | Most common, moderate conductivity |
| Granite | 1.90-2.20 | 2320-2400 | Highest conductivity |
| Sandstone | 1.30-1.60 | 2160-2240 | Lower conductivity |
| Basalt | 1.70-2.00 | 2320-2400 | High density, high conductivity |

**Moisture Content Effects:**

Concrete moisture equilibrium varies with ambient relative humidity:
- 30% RH: 2.5% moisture content by mass
- 50% RH: 3.5% moisture content
- 75% RH: 5.0% moisture content
- 100% RH: 8.0-10% moisture content

Each 1% increase in moisture content raises thermal conductivity by approximately 5-8%.

**Design Applications:**
- Tilt-up construction
- Structural slabs and walls
- Thermal mass applications in passive solar design
- Below-grade walls (requires exterior insulation)

### Lightweight Concrete

Lightweight concrete utilizes expanded shale, clay, slate, or slag aggregates to reduce density and thermal conductivity while maintaining structural capacity.

**Thermal Properties:**
- Thermal conductivity: 0.40 to 1.00 W/m·K (varies with density)
- Density: 1440 to 1920 kg/m³
- Specific heat capacity: 840 to 1000 J/kg·K
- Thermal diffusivity: 0.30 to 0.65 × 10⁻⁶ m²/s

**Density-Conductivity Relationship:**

| Density (kg/m³) | k (W/m·K) | Typical Application |
|----------------|-----------|---------------------|
| 1440 | 0.40-0.50 | Non-structural insulating concrete |
| 1600 | 0.55-0.70 | Roof deck systems |
| 1760 | 0.70-0.85 | Structural lightweight concrete |
| 1920 | 0.85-1.00 | High-strength lightweight |

**Advantages:**
- Reduced dead load (20-30% lighter than normal weight)
- Lower thermal conductivity improves envelope performance
- Reduced thermal bridging through structural elements
- Improved fire resistance compared to normal weight concrete

**Limitations:**
- Higher material cost (15-25% premium)
- Lower thermal mass reduces passive cooling effectiveness
- May require specialized mix design and placement procedures

## Concrete Masonry Units (CMU)

Concrete block, or CMU, provides a versatile structural and envelope material with air voids that significantly influence thermal performance.

### Standard CMU Thermal Properties

**Solid-Grouted CMU:**
- Thermal conductivity: 0.90 to 1.20 W/m·K
- Density: 2080 to 2240 kg/m³
- Effective R-value (200mm/8" block): 0.14 to 0.18 m²·K/W (R-0.8 to R-1.0)

**Hollow CMU (unfilled cores):**
- Thermal conductivity (equivalent): 0.60 to 0.80 W/m·K
- Density: 1440 to 1600 kg/m³
- Effective R-value (200mm/8" block): 0.26 to 0.35 m²·K/W (R-1.5 to R-2.0)

### CMU Thermal Performance Enhancement

**Core Insulation Methods:**

1. **Expanded Polystyrene (EPS) Inserts:**
   - Increases R-value to 0.88-1.23 m²·K/W (R-5 to R-7)
   - Requires placement during construction
   - Reduces thermal bridging through webs by 40-60%

2. **Perlite Fill:**
   - Increases R-value to 0.53-0.70 m²·K/W (R-3 to R-4)
   - Can be installed after construction
   - Provides fire resistance
   - Less effective than rigid inserts

3. **Vermiculite Fill:**
   - Increases R-value to 0.44-0.62 m²·K/W (R-2.5 to R-3.5)
   - Lower cost than perlite
   - Settles over time, reducing long-term performance

**Web Configuration Impact:**

CMU web design significantly affects thermal bridging:
- Standard two-web design: 25-30% thermal bridging
- Three-web design: 35-40% thermal bridging
- Split-face units: Similar to standard two-web
- Architectural units with thicker webs: 30-40% thermal bridging

### Moisture Effects on CMU Performance

CMU exhibits high moisture absorption capacity due to porosity:
- Initial absorption: 1.4 to 2.4 kg/m² per hour
- Saturation coefficient: 0.75 to 0.85
- Total absorption at saturation: 8-15% by mass

**Thermal Conductivity vs. Moisture Content:**

| Moisture Content | k Increase | Performance Impact |
|-----------------|-----------|-------------------|
| 0% (oven dry) | Baseline | Design condition |
| 2-4% (equilibrium) | +15-25% | Normal service condition |
| 6-8% (wet climate) | +35-50% | Requires drainage/flashing |
| 10-15% (saturated) | +75-100% | Failure condition |

## Stone Materials

Natural stone provides durable, high-thermal-mass envelope assemblies with thermal properties dependent on mineralogical composition and density.

### Granite

**Thermal Properties:**
- Thermal conductivity: 2.50 to 3.00 W/m·K
- Density: 2560 to 2720 kg/m³
- Specific heat capacity: 790 to 890 J/kg·K
- Thermal diffusivity: 1.10 to 1.40 × 10⁻⁶ m²/s

**Characteristics:**
- Highest thermal conductivity among common building stones
- Excellent durability and weather resistance
- Low moisture absorption (0.2-0.5%)
- Minimal thermal conductivity variation with moisture
- Common in cladding and high-end construction

### Limestone

**Thermal Properties:**
- Thermal conductivity: 1.80 to 2.40 W/m·K
- Density: 2240 to 2560 kg/m³
- Specific heat capacity: 840 to 950 J/kg·K
- Thermal diffusivity: 0.85 to 1.15 × 10⁻⁶ m²/s

**Characteristics:**
- Moderate thermal conductivity
- Higher porosity than granite (5-15% vs. 0.5-1.5%)
- Moisture absorption: 1-3% by mass
- Thermal conductivity increases 10-20% when saturated
- Widely used in commercial construction

### Sandstone

**Thermal Properties:**
- Thermal conductivity: 1.40 to 2.00 W/m·K
- Density: 2000 to 2400 kg/m³
- Specific heat capacity: 800 to 920 J/kg·K
- Thermal diffusivity: 0.75 to 1.05 × 10⁻⁶ m²/s

**Characteristics:**
- Lower thermal conductivity due to higher porosity
- Moisture absorption: 3-8% by mass
- Significant thermal conductivity increase when wet (+30-50%)
- Variable properties based on formation geology

### Marble

**Thermal Properties:**
- Thermal conductivity: 2.40 to 3.20 W/m·K
- Density: 2560 to 2720 kg/m³
- Specific heat capacity: 810 to 920 J/kg·K
- Thermal diffusivity: 1.00 to 1.45 × 10⁻⁶ m²/s

**Characteristics:**
- High thermal conductivity similar to granite
- Low porosity (0.5-2%)
- Minimal moisture effects on thermal properties
- Used in high-end interior and exterior applications

## Mortar and Plaster Materials

### Cement Mortar

**Thermal Properties:**
- Thermal conductivity: 1.20 to 1.60 W/m·K
- Density: 1760 to 2080 kg/m³
- Specific heat capacity: 840 to 960 J/kg·K

**Performance Considerations:**
- Mortar joints constitute 7-15% of masonry wall area
- Create thermal bridges through wall assemblies
- Weaker links in moisture resistance
- Type N mortar (lower cement content) has lower conductivity than Type S
- Joint tooling affects moisture penetration and thermal performance

### Gypsum Plaster

**Thermal Properties:**
- Thermal conductivity: 0.40 to 0.60 W/m·K
- Density: 1120 to 1440 kg/m³
- Specific heat capacity: 840 to 1090 J/kg·K

**Application Types:**

| Plaster Type | k (W/m·K) | Density (kg/m³) | Application |
|-------------|-----------|-----------------|-------------|
| Gypsum sand | 0.50-0.60 | 1360-1440 | General interior |
| Gypsum perlite | 0.35-0.45 | 960-1120 | Insulating plaster |
| Gypsum vermiculite | 0.30-0.40 | 800-960 | Fire-rated assemblies |

## Thermal Mass Effects

Masonry thermal mass provides heat storage capacity characterized by volumetric heat capacity (ρc):

**Volumetric Heat Capacity:**

| Material | ρc (MJ/m³·K) | Thermal Mass Class |
|----------|-------------|-------------------|
| Common brick | 1.34-1.77 | High |
| Face brick | 1.80-2.24 | Very high |
| Normal weight concrete | 1.97-2.52 | Very high |
| Lightweight concrete | 1.21-1.92 | Moderate to high |
| CMU (grouted) | 1.75-2.24 | High |
| CMU (hollow) | 1.21-1.34 | Moderate |
| Stone (average) | 2.03-2.50 | Very high |

### Thermal Time Constant

The thermal time constant (τ) indicates the time required for a material to respond to temperature changes:

τ = (ρ × c × L²) / k

Where:
- ρ = density (kg/m³)
- c = specific heat (J/kg·K)
- L = thickness (m)
- k = thermal conductivity (W/m·K)

**Representative Time Constants (200mm wall):**
- Brick masonry: 6-10 hours
- Concrete: 8-14 hours
- CMU (grouted): 6-12 hours
- Stone: 8-12 hours

These time constants enable passive load shifting, reducing peak cooling loads by 20-40% in properly designed mass wall buildings.

## Moisture Migration and Thermal Performance

### Hygrothermal Behavior

Masonry materials exhibit complex moisture transport mechanisms:

1. **Capillary Absorption:** Dominant mechanism in most masonry
2. **Vapor Diffusion:** Secondary mechanism, important in interior conditions
3. **Surface Condensation:** Occurs when surface temperature falls below dew point
4. **Interstitial Condensation:** Can occur within wall assemblies

### Critical Moisture Content

Each masonry material has a critical moisture content above which thermal performance degrades significantly:

| Material | Critical Moisture (% by mass) | k Increase at Critical |
|----------|------------------------------|----------------------|
| Common brick | 5-8% | +40-60% |
| Face brick | 3-5% | +30-45% |
| Concrete | 4-6% | +35-50% |
| CMU | 6-10% | +50-75% |
| Limestone | 2-4% | +25-40% |

### Moisture Control Strategies

1. **Cavity Wall Design:**
   - 50-100mm air space with weep holes
   - Flashing at all horizontal penetrations
   - Reduces moisture migration to interior wythe by 80-95%

2. **Exterior Insulation:**
   - Maintains mass wall above dew point
   - Eliminates thermal bridging
   - Improves effective R-value by 15-25%

3. **Vapor Retarders:**
   - Install on warm side of insulation
   - Gypsum board with paint typically sufficient in most climates
   - Polyethylene sheets required in extreme cold climates (CZ 6-8)

4. **Drainage Planes:**
   - Air gap behind veneer with weep system
   - Self-adhered membranes on sheathing
   - Reduces masonry moisture content by 50-70%

## ASHRAE References and Standards

### ASHRAE Handbook - Fundamentals

**Chapter 26: Heat, Air, and Moisture Control in Building Assemblies**
- Table 1: Thermal properties of typical building materials
- Table 4: Water vapor permeability of materials
- Moisture control design procedures

**Chapter 18: Nonresidential Cooling and Heating Load Calculations**
- Conduction transfer functions for masonry assemblies
- Thermal mass effects on cooling loads
- Sol-air temperature calculations

### ASHRAE Standard 90.1

**Envelope Requirements by Climate Zone:**

Masonry wall assemblies must meet minimum R-values:
- Climate Zone 1: R-2.3 (R-13)
- Climate Zone 2: R-2.3 (R-13)
- Climate Zone 3: R-2.3 + R-1.3 c.i. (R-13 + R-7.5 c.i.)
- Climate Zone 4: R-2.3 + R-1.6 c.i. (R-13 + R-9.5 c.i.)
- Climate Zone 5: R-2.3 + R-2.1 c.i. (R-13 + R-11.4 c.i.)
- Climate Zone 6: R-2.3 + R-2.3 c.i. (R-13 + R-13.3 c.i.)
- Climate Zone 7-8: R-2.3 + R-3.3 c.i. (R-13 + R-19.0 c.i.)

Note: c.i. = continuous insulation (uninterrupted by framing)

## Design Considerations for HVAC Load Calculations

### Effective R-Value Calculation

Masonry walls require parallel path calculation to account for thermal bridging through mortar joints and CMU webs:

R-effective = 1 / [(A₁/R₁) + (A₂/R₂) + ... + (Aₙ/Rₙ)]

Where A₁, A₂, etc. are fractional areas and R₁, R₂, etc. are corresponding R-values.

**Example: 200mm CMU Wall**
- CMU core area (60%): R = 1.76 m²·K/W (R-10)
- CMU web area (25%): R = 0.18 m²·K/W (R-1.0)
- Mortar joint area (15%): R = 0.14 m²·K/W (R-0.8)

R-effective = 1 / [(0.60/1.76) + (0.25/0.18) + (0.15/0.14)]
R-effective = 0.44 m²·K/W (R-2.5)

This represents a 75% reduction from the core R-value due to thermal bridging.

### Thermal Mass Benefits in Load Calculations

ASHRAE transfer function method accounts for thermal mass effects through conduction transfer function coefficients. For manual calculations, simplified methods apply:

**Peak Load Reduction Factor:**
- Lightweight construction: 1.00 (baseline)
- Medium mass (100-150 kg/m² floor area): 0.90-0.95
- Heavy mass (>200 kg/m² floor area): 0.75-0.85

**Time Lag:**
Mass walls shift peak cooling loads by 4-12 hours, potentially moving loads from peak utility rate periods to off-peak periods.

### Condensation Risk Assessment

Surface condensation risk exists when:
T-surface < T-dewpoint

For masonry walls, calculate interior surface temperature:
T-surface = T-indoor - [(T-indoor - T-outdoor) / (R-total × h-i)]

Where h-i = interior surface film coefficient (8.3 W/m²·K for walls)

If T-surface < T-dewpoint at design conditions, mold risk exists and additional insulation or vapor control is required.

### Energy Modeling Considerations

When modeling masonry buildings in energy simulation software:
- Use actual material densities, not defaults
- Account for mortar joints separately in detailed models
- Consider moisture content for realistic performance
- Apply thermal mass credits per ASHRAE 90.1 Appendix G
- Model time-of-day utility rates to capture mass benefits

## Installation and Quality Control

### Field Verification

Critical parameters requiring field verification:
- Mortar joint thickness: 9.5-12.7mm (3/8"-1/2")
- CMU core fill percentage (if applicable)
- Flashing installation and termination
- Weep hole spacing: 610-810mm (24"-32") o.c.
- Insulation continuity at penetrations

### Common Deficiencies Affecting Thermal Performance

1. **Incomplete Mortar Joints:** Reduces effective R-value by 10-20%
2. **Wet Masonry at Enclosure:** Increases heat loss by 30-60% until dry
3. **Missing Flashing:** Allows chronic moisture accumulation
4. **Thermal Bridges at Shelf Angles:** Can reduce assembly R-value by 15-30%
5. **Air Leakage Paths:** Increases heat loss by 5-25% depending on severity

### Testing and Verification Methods

- **Infrared Thermography:** Identifies thermal bridges, missing insulation, air leakage
- **Blower Door Testing:** Quantifies air leakage through masonry assemblies
- **Moisture Content Testing:** Verify acceptable moisture levels before insulation installation
- **Nuclear Density Gauge:** Verifies concrete density and uniformity

## Summary

Masonry materials provide durable, fire-resistant building envelope assemblies with thermal properties ranging from highly conductive (stone, dense concrete) to moderately insulating (lightweight concrete, insulated CMU). The thermal performance of masonry construction depends critically on:

- Material composition and density
- Moisture content and control
- Thermal bridging through joints and webs
- Proper integration with insulation systems
- Installation quality and continuity

HVAC designers must account for both the thermal conductivity and thermal mass of masonry assemblies. While masonry generally requires supplemental insulation to meet modern energy codes, the thermal mass provides significant peak load reduction and load shifting benefits when properly designed and operated.

Accurate thermal property data, appropriate moisture assumptions, and correct modeling of thermal bridging are essential for realistic load calculations and energy predictions in masonry buildings.
