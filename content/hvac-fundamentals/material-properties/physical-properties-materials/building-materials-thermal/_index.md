---
title: "Building Materials Thermal Properties"
description: "Comprehensive thermal properties of building materials including thermal conductivity, specific heat, density, thermal mass, R-values, and U-values for HVAC load calculations and energy modeling"
weight: 2
---

Building material thermal properties govern heat transfer through building envelopes and directly impact HVAC load calculations, energy consumption, and occupant comfort. Accurate knowledge of thermal conductivity, specific heat, density, and thermal mass enables precise heat transfer analysis and system sizing.

## Thermal Conductivity

Thermal conductivity (k) quantifies a material's ability to conduct heat, expressed in W/(m·K) or Btu·in/(h·ft²·°F). Lower values indicate better insulating properties.

**Fundamental relationship:**

q = k × A × (ΔT/L)

Where:
- q = heat transfer rate (W)
- k = thermal conductivity (W/(m·K))
- A = cross-sectional area (m²)
- ΔT = temperature difference (K)
- L = material thickness (m)

### Thermal Conductivity by Material Category

| Material Category | k (W/(m·K)) | k (Btu·in/(h·ft²·°F)) | Application |
|------------------|-------------|----------------------|-------------|
| **Metals** |
| Copper | 385-401 | 2,670-2,780 | Piping, heat exchangers |
| Aluminum | 205-250 | 1,420-1,730 | Ductwork, fins |
| Steel (carbon) | 43-65 | 298-450 | Structural, ductwork |
| Stainless steel 304 | 16.2 | 112 | Corrosion-resistant applications |
| **Masonry** |
| Concrete (normal weight) | 1.0-1.8 | 6.9-12.5 | Structural walls, slabs |
| Concrete (lightweight) | 0.4-0.7 | 2.8-4.9 | Non-structural infill |
| Brick (common) | 0.6-0.9 | 4.2-6.3 | Exterior walls |
| Brick (face) | 1.0-1.3 | 6.9-9.0 | Veneer cladding |
| Concrete block (hollow) | 0.4-0.6 | 2.8-4.2 | Structural/partition walls |
| Concrete block (filled) | 0.7-1.0 | 4.9-6.9 | Load-bearing walls |
| **Wood Products** |
| Softwood (pine, fir) | 0.10-0.15 | 0.69-1.04 | Framing, sheathing |
| Hardwood (oak, maple) | 0.16-0.21 | 1.11-1.45 | Flooring, millwork |
| Plywood | 0.12-0.16 | 0.83-1.11 | Sheathing, subflooring |
| OSB (oriented strand board) | 0.10-0.14 | 0.69-0.97 | Sheathing, subflooring |
| Particle board | 0.12-0.17 | 0.83-1.18 | Underlayment |
| **Insulation Materials** |
| Fiberglass batt | 0.038-0.046 | 0.26-0.32 | Cavity insulation |
| Mineral wool | 0.033-0.040 | 0.23-0.28 | Fire-rated assemblies |
| Cellulose (loose-fill) | 0.037-0.042 | 0.26-0.29 | Attic insulation |
| Expanded polystyrene (EPS) | 0.032-0.038 | 0.22-0.26 | Board insulation |
| Extruded polystyrene (XPS) | 0.028-0.032 | 0.19-0.22 | Below-grade insulation |
| Polyisocyanurate (polyiso) | 0.022-0.028 | 0.15-0.19 | Roof insulation |
| Spray polyurethane foam (closed-cell) | 0.021-0.028 | 0.15-0.19 | Air sealing, insulation |
| Spray polyurethane foam (open-cell) | 0.036-0.040 | 0.25-0.28 | Cavity insulation |
| **Gypsum Products** |
| Gypsum board (drywall) | 0.16-0.17 | 1.11-1.18 | Interior finish |
| Gypsum plaster | 0.22-0.30 | 1.53-2.08 | Wall finish |
| **Other Materials** |
| Glass (window) | 0.96-1.05 | 6.7-7.3 | Glazing |
| Air (still, 10°C) | 0.025 | 0.17 | Cavity resistance |
| Asphalt shingles | 0.15-0.18 | 1.04-1.25 | Roofing |
| Built-up roofing | 0.16-0.19 | 1.11-1.32 | Low-slope roofing |

## Thermal Resistance and Transmittance

### R-Value (Thermal Resistance)

R-value represents resistance to heat flow through a specific thickness of material:

R = L / k

Where:
- R = thermal resistance (m²·K/W or h·ft²·°F/Btu)
- L = material thickness (m or ft)
- k = thermal conductivity

**SI Units:** m²·K/W
**IP Units:** h·ft²·°F/Btu (commonly stated as just "R-value")

For multi-layer assemblies, total R-value equals the sum of individual layer resistances plus surface film resistances:

R_total = R_si + R₁ + R₂ + ... + R_n + R_so

Where R_si is inside surface resistance and R_so is outside surface resistance.

### U-Value (Thermal Transmittance)

U-value represents overall heat transfer coefficient:

U = 1 / R_total

**SI Units:** W/(m²·K)
**IP Units:** Btu/(h·ft²·°F)

Lower U-values indicate better insulating performance. Building energy codes specify maximum U-values for envelope assemblies.

### Surface Film Resistances

| Surface | Position | R (m²·K/W) | R (h·ft²·°F/Btu) |
|---------|----------|-----------|------------------|
| Interior | Horizontal (heat flow up) | 0.107 | 0.61 |
| Interior | Horizontal (heat flow down) | 0.162 | 0.92 |
| Interior | Vertical | 0.120 | 0.68 |
| Exterior | Any (15 mph wind) | 0.030 | 0.17 |
| Exterior | Any (7.5 mph wind) | 0.044 | 0.25 |

## Density and Specific Heat

### Density Values

Density (ρ) affects thermal mass and structural considerations:

| Material | Density (kg/m³) | Density (lb/ft³) |
|----------|----------------|------------------|
| Concrete (normal weight, 4000 psi) | 2,240-2,400 | 140-150 |
| Concrete (lightweight) | 1,440-1,840 | 90-115 |
| Brick (common) | 1,760-2,080 | 110-130 |
| Concrete block (hollow) | 1,280-1,440 | 80-90 |
| Softwood | 480-560 | 30-35 |
| Hardwood | 640-800 | 40-50 |
| Gypsum board | 640-800 | 40-50 |
| Fiberglass insulation | 10-48 | 0.6-3.0 |
| Mineral wool | 24-96 | 1.5-6.0 |
| XPS insulation | 28-45 | 1.75-2.8 |
| Polyiso insulation | 28-32 | 1.75-2.0 |

### Specific Heat Capacity

Specific heat (c_p) determines energy storage per unit mass:

| Material | c_p (kJ/(kg·K)) | c_p (Btu/(lb·°F)) |
|----------|----------------|-------------------|
| Concrete | 0.88-1.00 | 0.21-0.24 |
| Brick | 0.84-0.92 | 0.20-0.22 |
| Stone | 0.80-0.90 | 0.19-0.21 |
| Wood | 1.20-1.76 | 0.29-0.42 |
| Gypsum board | 1.09 | 0.26 |
| Glass | 0.84 | 0.20 |
| Steel | 0.46 | 0.11 |
| Aluminum | 0.90 | 0.21 |

## Thermal Mass

Thermal mass quantifies a material's ability to store and release thermal energy. High thermal mass materials moderate temperature swings and shift peak cooling loads.

### Volumetric Heat Capacity

Thermal mass per unit volume:

C_v = ρ × c_p

Where:
- C_v = volumetric heat capacity (kJ/(m³·K))
- ρ = density (kg/m³)
- c_p = specific heat (kJ/(kg·K))

| Material | C_v (kJ/(m³·K)) | C_v (Btu/(ft³·°F)) |
|----------|----------------|-------------------|
| Concrete (normal weight) | 1,970-2,400 | 29.4-35.8 |
| Concrete (lightweight) | 1,270-1,840 | 19.0-27.5 |
| Brick | 1,480-1,910 | 22.1-28.5 |
| Concrete block (hollow) | 1,070-1,320 | 16.0-19.7 |
| Wood (softwood) | 576-985 | 8.6-14.7 |
| Gypsum board | 697-872 | 10.4-13.0 |
| Water (reference) | 4,186 | 62.4 |

### Thermal Diffusivity

Thermal diffusivity (α) characterizes how quickly temperature changes propagate through a material:

α = k / (ρ × c_p)

Where:
- α = thermal diffusivity (m²/s)
- k = thermal conductivity (W/(m·K))
- ρ = density (kg/m³)
- c_p = specific heat (kJ/(kg·K))

High diffusivity indicates rapid temperature response; low diffusivity indicates thermal lag.

| Material | α × 10⁻⁶ (m²/s) | α × 10⁻³ (ft²/h) |
|----------|----------------|------------------|
| Copper | 111-117 | 430-450 |
| Aluminum | 84-97 | 324-374 |
| Steel | 15-23 | 58-89 |
| Concrete (normal weight) | 0.42-0.75 | 1.6-2.9 |
| Brick | 0.36-0.52 | 1.4-2.0 |
| Wood (softwood) | 0.12-0.18 | 0.46-0.69 |
| Gypsum board | 0.20-0.24 | 0.77-0.93 |
| Insulation (typical) | 0.8-1.5 | 3.1-5.8 |

### Thermal Mass Design Applications

**Beneficial applications:**
- High diurnal temperature swing climates
- Spaces with intermittent occupancy
- Passive solar heating strategies
- Peak load shifting for demand management
- Night ventilation cooling (night flush)

**Critical thickness concept:**
Temperature waves penetrate materials to a depth dependent on the thermal diffusivity and cycle period. For 24-hour cycles, penetration depth:

δ = √(α × t / π)

Where:
- δ = penetration depth (m)
- α = thermal diffusivity (m²/s)
- t = period (86,400 s for 24 hours)

For concrete (α ≈ 0.6 × 10⁻⁶ m²/s), effective thermal mass depth ≈ 100-150 mm (4-6 inches).

## Building Envelope Assembly U-Values

### Typical Wall Assemblies

| Wall Type | Construction | U-Value (W/(m²·K)) | U-Value (Btu/(h·ft²·°F)) |
|-----------|-------------|-------------------|-------------------------|
| Wood frame, R-13 batt | 2×4 studs, fiberglass | 0.51-0.57 | 0.09-0.10 |
| Wood frame, R-19 batt | 2×6 studs, fiberglass | 0.37-0.42 | 0.065-0.074 |
| Wood frame, R-21 batt + R-5 CI | 2×6 studs + exterior foam | 0.30-0.34 | 0.053-0.060 |
| Steel frame, R-13 batt | 3-5/8" studs, fiberglass | 0.62-0.68 | 0.109-0.120 |
| Steel frame, R-13 + R-5 CI | 3-5/8" studs + exterior foam | 0.44-0.48 | 0.077-0.085 |
| CMU, uninsulated | 8" hollow block | 1.59-1.82 | 0.28-0.32 |
| CMU, fully grouted | 8" filled block | 2.27-2.50 | 0.40-0.44 |
| CMU + R-10 CI | 8" block + exterior foam | 0.45-0.51 | 0.079-0.090 |
| Insulated concrete form (ICF) | R-22 EPS, 6" concrete core | 0.23-0.26 | 0.040-0.046 |

### Typical Roof/Ceiling Assemblies

| Assembly Type | Construction | U-Value (W/(m²·K)) | U-Value (Btu/(h·ft²·°F)) |
|---------------|-------------|-------------------|-------------------------|
| Attic, R-30 insulation | Vented attic, blown cellulose | 0.30-0.34 | 0.053-0.060 |
| Attic, R-49 insulation | Vented attic, blown fiberglass | 0.19-0.21 | 0.033-0.037 |
| Attic, R-60 insulation | Vented attic, cellulose | 0.15-0.17 | 0.026-0.030 |
| Cathedral ceiling, R-30 | 2×10 rafters, spray foam | 0.30-0.34 | 0.053-0.060 |
| Flat roof, R-20 CI | Metal deck + polyiso | 0.42-0.45 | 0.074-0.079 |
| Flat roof, R-30 CI | Metal deck + polyiso | 0.28-0.31 | 0.049-0.055 |

### Typical Floor Assemblies

| Floor Type | Construction | U-Value (W/(m²·K)) | U-Value (Btu/(h·ft²·°F)) |
|------------|-------------|-------------------|-------------------------|
| Slab-on-grade, uninsulated | 4" concrete, no edge insulation | 1.02-1.42 | 0.18-0.25 |
| Slab-on-grade, R-10 edge | 4" concrete, perimeter insulation | 0.45-0.57 | 0.08-0.10 |
| Raised floor, R-19 | Wood joists, fiberglass batt | 0.37-0.42 | 0.065-0.074 |
| Raised floor, R-30 | Wood joists, spray foam | 0.28-0.31 | 0.049-0.055 |

## Moisture-Related Properties

### Water Vapor Permeability

Water vapor transmission affects condensation potential and material durability:

| Material | Permeance (ng/(Pa·s·m²)) | Perm (grains/(h·ft²·in Hg)) | Classification |
|----------|--------------------------|----------------------------|----------------|
| Polyethylene sheet (6 mil) | 3-9 | 0.06-0.16 | Vapor barrier |
| Aluminum foil (1 mil) | 0-0.3 | 0-0.005 | Vapor barrier |
| Kraft paper | 29-86 | 0.5-1.5 | Vapor retarder |
| Latex paint (2 coats) | 285-860 | 5-15 | Vapor retarder |
| Gypsum board (unpainted) | 2,850-3,420 | 50-60 | Permeable |
| XPS insulation (1 inch) | 57-171 | 1.0-3.0 | Vapor retarder |
| Polyiso insulation (1 inch) | 29-86 | 0.5-1.5 | Vapor retarder |
| Plywood (1/2 inch) | 171-400 | 3-7 | Semi-permeable |
| OSB (1/2 inch) | 114-342 | 2-6 | Semi-permeable |

**Classification:**
- Vapor barrier: ≤ 5.7 ng/(Pa·s·m²) (0.1 perm)
- Class I vapor retarder: ≤ 57 ng/(Pa·s·m²) (1 perm)
- Class II vapor retarder: 57-570 ng/(Pa·s·m²) (1-10 perms)
- Class III vapor retarder: 570-1,710 ng/(Pa·s·m²) (10-30 perms)
- Permeable: > 1,710 ng/(Pa·s·m²) (>30 perms)

## Application to HVAC Load Calculations

### Conduction Heat Transfer Through Walls

Steady-state heat transfer:

q = U × A × ΔT

For cooling load calculations, account for:
- Solar radiation absorbed by exterior surfaces
- Thermal mass time lag effects
- Interior radiation heat transfer

### Equivalent Temperature Difference Method

Total heat gain through opaque surfaces:

q = U × A × TETD

Where TETD (Total Equivalent Temperature Difference) accounts for:
- Outdoor-indoor temperature difference
- Solar radiation effects
- Thermal storage/release

### Thermal Bridging

Structural penetrations through insulation create thermal bridges that increase effective U-values:

**Typical framing factors:**
- Wood frame walls: 15-25% framing fraction
- Steel frame walls: 15-25% framing fraction with higher thermal bridging impact
- CMU walls: Negligible framing but grouted cells create bridges

**Advanced framing techniques** reduce thermal bridging:
- 24-inch on-center spacing vs. 16-inch
- Insulated headers
- Two-stud corners
- Single top plates
- In-line framing

Effective assembly U-values account for parallel heat flow paths through framing and cavity insulation using:

U_eff = (f_frame × U_frame) + (f_cavity × U_cavity)

Where f represents area fraction.

## Material Selection Criteria for HVAC Applications

**High thermal mass materials** (concrete, brick, stone):
- Moderate temperature swings
- Shift peak loads
- Improve comfort in intermittent heating/cooling
- Require careful control strategies

**High thermal resistance materials** (insulation):
- Reduce steady-state heat transfer
- Lower annual energy consumption
- Minimal temperature lag effects
- Essential for envelope thermal performance

**Low permeability materials**:
- Control moisture migration
- Prevent condensation in assemblies
- Must be positioned correctly based on climate zone

**Selection process:**
1. Establish energy code requirements (maximum U-values)
2. Evaluate thermal mass benefits for specific climate
3. Assess moisture control requirements
4. Calculate cost-effectiveness of insulation levels
5. Consider structural and fire requirements
6. Verify compatibility with air/vapor barriers

## Standards References

- ASHRAE Handbook—Fundamentals, Chapter 26: Heat, Air, and Moisture Control in Building Assemblies
- ASHRAE Standard 90.1: Energy Standard for Buildings Except Low-Rise Residential Buildings
- ISO 10456: Building materials and products—Hygrothermal properties
- ASTM C177: Standard Test Method for Steady-State Heat Flux Measurements and Thermal Transmission Properties
- ASTM C518: Standard Test Method for Steady-State Thermal Transmission Properties by Means of the Heat Flow Meter Apparatus
- NFRC 100: Procedure for Determining Fenestration Product U-factors
