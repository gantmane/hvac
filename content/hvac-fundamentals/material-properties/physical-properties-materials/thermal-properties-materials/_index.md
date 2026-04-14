---
title: "Thermal Properties of Materials"
aliases: ["Thermal Properties of Materials"]
description: "Engineering fundamentals of thermal conductivity, specific heat, thermal diffusivity, and related properties critical for heat transfer calculations, insulation design, and thermal mass analysis in HVAC systems."
weight: 1
---

Thermal properties govern heat transfer through building envelopes, HVAC equipment, and distribution systems. Understanding these fundamental material characteristics enables accurate load calculations, proper insulation specification, and effective thermal storage design.

## Thermal Conductivity (k)

Thermal conductivity quantifies a material's ability to conduct heat. Materials with high conductivity rapidly transfer thermal energy, while low-conductivity materials resist heat flow and function as insulators.

### Definition and Units

**Thermal Conductivity (k)**: Heat transfer rate through unit thickness per unit area per unit temperature difference.

| Unit System | Expression | Common Values |
|-------------|-----------|---------------|
| SI (Metric) | W/(m·K) | 0.02-400 W/(m·K) |
| I-P (Imperial) | Btu·in/(hr·ft²·°F) | 0.15-2800 Btu·in/(hr·ft²·°F) |

**Conversion**: 1 Btu·in/(hr·ft²·°F) = 0.1442 W/(m·K)

### Fourier's Law

Heat conduction through a homogeneous material follows Fourier's law:

```
q = -k·A·(dT/dx)
```

Where:
- q = heat transfer rate (W or Btu/hr)
- k = thermal conductivity (W/(m·K) or Btu·in/(hr·ft²·°F))
- A = cross-sectional area (m² or ft²)
- dT/dx = temperature gradient (K/m or °F/ft)

For steady-state conduction through a plane wall:

```
q = k·A·(T₁ - T₂)/L
```

Where:
- T₁, T₂ = surface temperatures (K or °F)
- L = material thickness (m or ft)

### Thermal Conductivity of Building Materials

**Structural Materials:**

| Material | Density (lb/ft³) | k (Btu·in/(hr·ft²·°F)) | k (W/(m·K)) |
|----------|------------------|------------------------|-------------|
| Concrete, normal weight | 140-150 | 12-15 | 1.73-2.16 |
| Concrete, lightweight | 80-120 | 3-9 | 0.43-1.30 |
| Brick, common | 120 | 5.0 | 0.72 |
| Brick, face | 130 | 9.0 | 1.30 |
| Concrete block, hollow | 75-95 | 2.5-4.5 | 0.36-0.65 |
| Concrete block, filled | 110-125 | 5.5-8.0 | 0.79-1.15 |
| Stone, granite | 165 | 15-20 | 2.16-2.88 |
| Stone, limestone | 140-165 | 10-15 | 1.44-2.16 |
| Wood, softwood (fir, pine) | 26-33 | 0.80-1.00 | 0.12-0.14 |
| Wood, hardwood (oak, maple) | 40-47 | 1.00-1.25 | 0.14-0.18 |
| Plywood | 34 | 0.80 | 0.12 |
| Steel, structural | 490 | 310 | 45 |
| Aluminum | 170 | 1400 | 200 |
| Copper | 560 | 2700 | 390 |

**Insulation Materials:**

| Material | Density (lb/ft³) | k (Btu·in/(hr·ft²·°F)) | k (W/(m·K)) |
|----------|------------------|------------------------|-------------|
| Fiberglass batt, R-11 | 0.4-1.0 | 0.27-0.30 | 0.039-0.043 |
| Fiberglass batt, R-19 | 0.5-1.2 | 0.27-0.30 | 0.039-0.043 |
| Mineral wool batt | 1.5-3.0 | 0.29-0.33 | 0.042-0.048 |
| Cellulose, loose-fill | 1.5-2.5 | 0.27-0.32 | 0.039-0.046 |
| Extruded polystyrene (XPS) | 1.8-2.2 | 0.20-0.22 | 0.029-0.032 |
| Expanded polystyrene (EPS) | 0.9-1.2 | 0.24-0.28 | 0.035-0.040 |
| Polyisocyanurate (polyiso) | 2.0-2.5 | 0.13-0.16 | 0.019-0.023 |
| Spray polyurethane foam, closed-cell | 2.0-2.5 | 0.13-0.17 | 0.019-0.024 |
| Spray polyurethane foam, open-cell | 0.4-0.7 | 0.26-0.28 | 0.038-0.040 |
| Vacuum insulation panel (VIP) | 4-8 | 0.03-0.05 | 0.004-0.007 |
| Aerogel blanket | 2-4 | 0.10-0.14 | 0.014-0.020 |

**Roofing and Finish Materials:**

| Material | Density (lb/ft³) | k (Btu·in/(hr·ft²·°F)) | k (W/(m·K)) |
|----------|------------------|------------------------|-------------|
| Asphalt shingles | 70 | 1.50 | 0.22 |
| Built-up roofing (BUR) | 70 | 1.20 | 0.17 |
| EPDM membrane | 75 | 1.10 | 0.16 |
| TPO/PVC membrane | 68 | 1.00-1.20 | 0.14-0.17 |
| Gypsum board, 1/2 in | 50 | 1.10 | 0.16 |
| Plaster, sand aggregate | 116 | 5.60 | 0.81 |
| Carpet with fibrous pad | 8 | 0.34 | 0.049 |
| Tile, ceramic | 130 | 6.50 | 0.94 |

### Temperature Dependence

Thermal conductivity varies with temperature. For most building materials over typical HVAC operating ranges (-40°F to 150°F or -40°C to 65°C), linear approximation suffices:

```
k(T) = k₀[1 + β(T - T₀)]
```

Where:
- k₀ = conductivity at reference temperature T₀
- β = temperature coefficient (typically 0.001-0.003 K⁻¹)
- T = material temperature

### Moisture Effects

Moisture dramatically increases thermal conductivity. Water has k = 0.6 W/(m·K), roughly 20 times higher than dry insulation. Moisture content by volume increases effective conductivity:

```
k_effective = k_dry + k_water × moisture_fraction
```

For fibrous insulation at 5% moisture by volume, conductivity can increase 50-100%. Vapor retarders and proper drainage prevent moisture accumulation.

## Thermal Resistance (R-value)

Thermal resistance quantifies a material's ability to resist heat flow. R-value is the inverse of thermal conductance.

### Definition and Calculation

**R-value for Homogeneous Material:**

```
R = L/k
```

Where:
- R = thermal resistance (m²·K/W or hr·ft²·°F/Btu)
- L = thickness (m or in)
- k = thermal conductivity

**Heat Flow Through Resistance:**

```
q = A·(T₁ - T₂)/R
```

### Series Resistances

For layered assemblies, resistances add in series:

```
R_total = R₁ + R₂ + R₃ + ... + R_n
```

**Complete Wall Assembly:**

```
R_total = R_interior_film + R_wall_layers + R_exterior_film
```

Typical surface film resistances:
- Interior wall (still air): 0.68 hr·ft²·°F/Btu (0.12 m²·K/W)
- Exterior wall (15 mph wind): 0.17 hr·ft²·°F/Btu (0.03 m²·K/W)
- Interior ceiling (heat flow up): 0.61 hr·ft²·°F/Btu (0.11 m²·K/W)
- Interior floor (heat flow down): 0.92 hr·ft²·°F/Btu (0.16 m²·K/W)

### Overall Heat Transfer Coefficient (U-factor)

U-factor represents the overall heat transmission:

```
U = 1/R_total
```

Units: W/(m²·K) or Btu/(hr·ft²·°F)

Lower U-factors indicate better insulation performance. Energy codes specify maximum U-factors for envelope components.

## Specific Heat Capacity (c_p)

Specific heat quantifies thermal energy storage per unit mass per degree temperature change.

### Definition and Units

| Unit System | Expression | Typical Range |
|-------------|-----------|---------------|
| SI | J/(kg·K) or kJ/(kg·K) | 800-4200 J/(kg·K) |
| I-P | Btu/(lb·°F) | 0.19-1.00 Btu/(lb·°F) |

**Conversion**: 1 Btu/(lb·°F) = 4186.8 J/(kg·K)

### Sensible Heat Equation

Energy required to change material temperature without phase change:

```
Q = m·c_p·ΔT
```

Where:
- Q = sensible heat (J or Btu)
- m = mass (kg or lb)
- c_p = specific heat (J/(kg·K) or Btu/(lb·°F))
- ΔT = temperature change (K or °F)

### Specific Heat of Common Materials

**Building Materials:**

| Material | c_p (Btu/(lb·°F)) | c_p (kJ/(kg·K)) |
|----------|-------------------|-----------------|
| Water (reference) | 1.00 | 4.18 |
| Air (dry, 75°F) | 0.240 | 1.00 |
| Concrete | 0.20-0.23 | 0.84-0.96 |
| Brick | 0.20 | 0.84 |
| Gypsum board | 0.26 | 1.09 |
| Wood | 0.33-0.40 | 1.38-1.67 |
| Steel | 0.11 | 0.46 |
| Aluminum | 0.21 | 0.88 |
| Copper | 0.092 | 0.39 |
| Glass | 0.18-0.20 | 0.75-0.84 |
| Stone | 0.19-0.21 | 0.80-0.88 |

**HVAC Fluids:**

| Fluid | Temperature (°F) | c_p (Btu/(lb·°F)) | c_p (kJ/(kg·K)) |
|-------|------------------|-------------------|-----------------|
| Water | 50 | 1.000 | 4.18 |
| Water | 150 | 0.999 | 4.18 |
| Ethylene glycol (50%) | 50 | 0.820 | 3.43 |
| Propylene glycol (50%) | 50 | 0.860 | 3.60 |
| R-410A liquid | 40 | 0.342 | 1.43 |
| R-134a liquid | 40 | 0.334 | 1.40 |

### Volumetric Heat Capacity

For thermal mass calculations, volumetric heat capacity proves more useful:

```
C_v = ρ·c_p
```

Where:
- C_v = volumetric heat capacity (Btu/(ft³·°F) or kJ/(m³·K))
- ρ = density (lb/ft³ or kg/m³)
- c_p = specific heat

| Material | C_v (Btu/(ft³·°F)) | C_v (kJ/(m³·K)) |
|----------|--------------------|--------------------|
| Water | 62.4 | 4180 |
| Concrete | 30 | 2000 |
| Brick | 25 | 1670 |
| Gypsum board | 13 | 870 |
| Wood | 10-15 | 670-1000 |

## Thermal Diffusivity (α)

Thermal diffusivity characterizes transient heat conduction, indicating how rapidly temperature changes propagate through a material.

### Definition and Calculation

```
α = k/(ρ·c_p)
```

Where:
- α = thermal diffusivity (m²/s or ft²/hr)
- k = thermal conductivity
- ρ = density
- c_p = specific heat

**Units**:
- SI: m²/s (typical range: 10⁻⁷ to 10⁻⁴ m²/s)
- I-P: ft²/hr (typical range: 0.01 to 50 ft²/hr)

### Physical Interpretation

High thermal diffusivity means:
- Rapid temperature response to boundary condition changes
- Low thermal mass effect
- Temperature quickly equalizes throughout material

Low thermal diffusivity means:
- Slow temperature response
- High thermal mass effect
- Temperature gradients persist longer

### Thermal Diffusivity Values

| Material | α (ft²/hr) | α × 10⁻⁶ (m²/s) |
|----------|------------|-----------------|
| Copper | 4.5 | 117 |
| Aluminum | 3.5 | 91 |
| Steel | 0.54 | 14 |
| Concrete | 0.040-0.055 | 1.0-1.4 |
| Brick | 0.025-0.035 | 0.65-0.91 |
| Gypsum board | 0.035 | 0.91 |
| Wood | 0.0065-0.010 | 0.17-0.26 |
| Insulation (fiberglass) | 0.028-0.035 | 0.73-0.91 |

### Application in Transient Analysis

**Penetration Depth** for cyclic temperature variations:

```
δ = √(α·t)
```

Where:
- δ = penetration depth (m or ft)
- t = time period (s or hr)

For 24-hour cycle (diurnal temperature swing):

| Material | Penetration Depth (in) | Penetration Depth (mm) |
|----------|------------------------|------------------------|
| Concrete | 5-6 | 130-150 |
| Brick | 4-5 | 100-130 |
| Wood | 2-3 | 50-75 |

**Thermal Time Constant** for slab or wall:

```
τ = L²/(π²·α)
```

Where:
- τ = time constant (s or hr)
- L = thickness (m or ft)

This determines lag time for temperature changes to propagate through the material.

## Thermal Mass

Thermal mass stores sensible heat, moderating indoor temperature swings and reducing peak cooling/heating loads.

### Effective Thermal Mass

Materials exposed to conditioned space provide thermal storage. The effective thermal mass depends on:
- Volumetric heat capacity (ρ·c_p)
- Surface area exposed to indoor air
- Thermal coupling (convective heat transfer coefficient)
- Diurnal temperature swing penetration depth

**Effective Heat Capacity:**

```
C_eff = ρ·c_p·V_eff
```

Where V_eff = A·δ, with A = surface area and δ = penetration depth.

### Thermal Mass Benefits

**Load Shifting**: Absorbs heat during day, releases at night, reducing peak cooling demand.

**Temperature Stabilization**: Dampens indoor temperature swings from solar gains and outdoor temperature variations.

**Quantification**: Thermal decrement factor and time lag from ASHRAE Handbook of Fundamentals, Chapter 18 (Heat, Air, and Moisture Control in Building Assemblies).

| Assembly | Thermal Decrement Factor | Time Lag (hr) |
|----------|--------------------------|---------------|
| Light frame wall (wood studs, insulation) | 0.85-0.95 | 2-4 |
| Brick veneer wall | 0.70-0.80 | 4-6 |
| Mass wall (8 in concrete) | 0.50-0.65 | 8-12 |
| Mass wall (12 in concrete) | 0.30-0.45 | 12-16 |

## Thermal Effusivity (e)

Thermal effusivity characterizes transient surface temperature response to heat flux, critical for contact thermal comfort and short-term heat storage.

### Definition

```
e = √(k·ρ·c_p)
```

Units: J/(m²·K·s^0.5) or Btu/(ft²·°F·hr^0.5)

### Physical Significance

High effusivity materials:
- Feel cool to touch (extract heat rapidly from skin)
- Rapidly absorb/release heat at surface
- Metal, concrete, stone

Low effusivity materials:
- Feel warm to touch (extract heat slowly)
- Slowly absorb/release surface heat
- Wood, carpet, insulation

### Contact Temperature

When two semi-infinite bodies at different temperatures contact, the interface temperature is:

```
T_interface = (e₁·T₁ + e₂·T₂)/(e₁ + e₂)
```

This explains why metal feels colder than wood at the same temperature: metal's high effusivity extracts heat rapidly from skin.

## Emissivity (ε)

Emissivity quantifies thermal radiation emission relative to an ideal blackbody.

### Definition and Range

**Emissivity (ε)**: Ratio of actual emitted radiation to blackbody radiation at same temperature.

Range: 0 ≤ ε ≤ 1
- ε = 1: Perfect blackbody (theoretical maximum)
- ε = 0: Perfect reflector (no emission)

### Stefan-Boltzmann Law

Radiation heat transfer from a surface:

```
q = ε·σ·A·(T_s⁴ - T_surr⁴)
```

Where:
- σ = Stefan-Boltzmann constant = 5.67×10⁻⁸ W/(m²·K⁴) = 0.1714×10⁻⁸ Btu/(hr·ft²·R⁴)
- T_s = surface absolute temperature (K or R)
- T_surr = surrounding surface absolute temperature (K or R)

### Emissivity Values

**Building Surfaces:**

| Surface | Emissivity (ε) |
|---------|----------------|
| Aluminum foil, bright | 0.03-0.05 |
| Aluminum, oxidized | 0.10-0.15 |
| Steel, polished | 0.10-0.15 |
| Steel, oxidized | 0.70-0.80 |
| Copper, polished | 0.03-0.05 |
| Copper, oxidized | 0.60-0.70 |
| Concrete | 0.85-0.95 |
| Brick | 0.90-0.95 |
| Wood | 0.80-0.90 |
| Gypsum board | 0.90-0.92 |
| Paint (all colors) | 0.85-0.95 |
| Asphalt shingles | 0.90-0.92 |
| White roofing membrane | 0.85-0.90 |
| Aluminum roof coating | 0.50-0.60 |

### Radiant Barriers

Low-emissivity surfaces (ε < 0.1) function as radiant barriers, reducing radiative heat transfer across air spaces. Applications include:

**Attic Radiant Barriers**: Aluminum foil facing reduces radiant gain to ceiling insulation, lowering cooling loads in hot climates. Per ASHRAE, effective R-value increase: R-3 to R-6 depending on configuration.

**Reflective Insulation Systems**: Multiple low-emissivity surfaces separated by air spaces achieve high thermal resistance despite minimal material thickness.

**Effective R-value of Air Space** with radiant barrier (3.5 in horizontal, heat flow up, winter):
- Without radiant barrier (ε = 0.90 both surfaces): R-0.84 hr·ft²·°F/Btu
- With one radiant barrier (ε = 0.05): R-2.86 hr·ft²·°F/Btu
- With two radiant barriers (ε = 0.05 both): R-4.55 hr·ft²·°F/Btu

## Design Considerations

### Load Calculation Implications

**Transmission Loads**: U-factor (inverse of R-value) directly determines conduction heat gain/loss:

```
Q_transmission = U·A·(T_outdoor - T_indoor)
```

Material selection affects:
- Peak heating/heating loads
- Annual energy consumption
- Equipment sizing

### Thermal Bridging

Discontinuities in insulation create thermal bridges, locally increasing heat transfer. Common bridges:
- Steel studs in walls (reduce effective R-value by 20-50%)
- Concrete balconies penetrating envelope
- Window frames and mullions
- Parapets and ledgers

**Effective U-factor** accounting for thermal bridging:

```
U_eff = (U_clear·A_clear + U_bridge·A_bridge)/(A_clear + A_bridge)
```

### Moisture Control

Materials must remain dry to maintain thermal performance. Water condensation occurs when material temperature drops below dewpoint. Vapor retarders, air barriers, and continuous insulation prevent moisture accumulation.

**Critical Condensation Plane**: Location within assembly where temperature equals dewpoint. Proper vapor retarder placement keeps this plane outside moisture-sensitive materials.

### Thermal Mass Strategy

Effective thermal mass requires:
- **Exposure**: Material surface exposed to indoor air, not covered by carpet or insulation
- **Thickness**: Sufficient to engage penetration depth (4-6 in concrete optimal)
- **Location**: Internal mass most effective (exterior insulation with interior mass)
- **Climate**: Most beneficial in climates with large diurnal temperature swings

### Material Selection Criteria

**Envelope Insulation**:
- Target R-value per code requirements (IECC, ASHRAE 90.1)
- Compatibility with assembly (compression, moisture resistance)
- Cost-effectiveness ($/R-value)

**Thermal Storage**:
- High volumetric heat capacity (concrete, masonry, water)
- Appropriate thickness for diurnal cycle
- Low resistance between mass and conditioned space

**Equipment and Piping**:
- Minimize conduction losses (insulate hot/cold surfaces)
- Consider thermal expansion (α affects dimensional change)
- Efficiency implications (insulation reduces standby losses)

## Code and Standards References

**ASHRAE Standards**:
- **ASHRAE Handbook—Fundamentals, Chapter 26**: Heat, Air, and Moisture Control in Building Assemblies—Climatic Data
- **ASHRAE Handbook—Fundamentals, Chapter 33**: Properties of Materials
- **ASHRAE Standard 90.1**: Energy Standard for Buildings (prescriptive envelope requirements)
- **ASHRAE Standard 90.2**: Energy-Efficient Design of Low-Rise Residential Buildings

**Test Methods**:
- **ASTM C177**: Steady-State Heat Flux Measurements (guarded hot plate)
- **ASTM C518**: Steady-State Thermal Transmission Properties (heat flow meter)
- **ASTM C1549**: Solar Reflectance (for cool roof materials)
- **ASTM E1980**: Calculation of Solar Reflectance Index

**Building Codes**:
- **International Energy Conservation Code (IECC)**: Prescriptive envelope insulation requirements by climate zone
- **International Building Code (IBC)**: Fire resistance ratings affected by material thermal properties
- **Local Amendments**: Jurisdiction-specific envelope performance requirements

## Practical Application Examples

### Example 1: Wall Assembly R-Value

**8-inch concrete block wall with exterior insulation:**

Layers (exterior to interior):
1. Exterior film resistance: R-0.17
2. 2-inch XPS insulation (k = 0.22): R = 2.0/0.22 = 9.09
3. 8-inch concrete block (k = 4.0): R = 8.0/4.0 = 2.00
4. Interior film resistance: R-0.68

```
R_total = 0.17 + 9.09 + 2.00 + 0.68 = 11.94 hr·ft²·°F/Btu
U = 1/11.94 = 0.084 Btu/(hr·ft²·°F)
```

### Example 2: Thermal Mass Storage Capacity

**1000 ft² concrete slab, 4 inches thick:**

```
Volume = 1000 ft² × (4/12) ft = 333.3 ft³
Mass = 333.3 ft³ × 145 lb/ft³ = 48,333 lb
Temperature swing = 75°F - 70°F = 5°F

Q = m·c_p·ΔT = 48,333 lb × 0.22 Btu/(lb·°F) × 5°F
Q = 53,166 Btu = 4.43 ton-hours
```

This thermal storage can shift peak cooling loads by several hours.

### Example 3: Heat Loss Through Pipe Insulation

**4-inch steel pipe carrying 180°F water, ambient 70°F:**

Pipe parameters:
- Outside diameter: 4.5 in
- Insulation: 1.5-inch fiberglass (k = 0.27)
- Pipe length: 100 ft

```
R_insulation = (d_o/2)·ln(r_outer/r_inner)/k
R_insulation = (4.5/2)·ln(3.75/2.25)/0.27 = 3.63 hr·ft²·°F/Btu (per ft²)

Surface area = π·d_o·L = π·(7.5/12 ft)·100 ft = 196 ft²

q = A·ΔT/R = 196 ft²·(180-70)°F / 3.63 = 5,934 Btu/hr
```

Without insulation, heat loss would be approximately 50,000 Btu/hr, demonstrating 88% reduction.

---

**Last Updated**: 2026-01-12
**Cross-References**:
- Material Properties Overview
- Heat Transfer Fundamentals
- Insulation Systems
- Load Calculation Methods
- Envelope Design