---
title: "Physical Properties of Materials"
description: "Thermal conductivity, specific heat, density, and mechanical properties of HVAC materials. Material property data for heat transfer calculations, equipment selection, and system design per ASHRAE Fundamentals."
weight: 3
---

Physical properties of materials govern heat transfer rates, energy storage capacity, structural performance, and acoustic characteristics in HVAC applications. Accurate property data is essential for load calculations, equipment sizing, insulation design, and energy modeling. Material properties vary with temperature, moisture content, and aging, requiring careful consideration during system design.

## Fundamental Thermal Properties

Three properties define thermal behavior of materials used in HVAC systems.

### Thermal Conductivity

Thermal conductivity (k) quantifies the rate of heat transfer through a material under unit temperature gradient:

- **Units**: W/(m·K) [SI], Btu·in/(h·ft²·°F) [I-P]
- **Physical meaning**: Heat flux per unit area per unit temperature gradient
- **Temperature dependence**: Most materials show increasing k with rising temperature
- **Moisture impact**: Wet materials exhibit significantly higher conductivity than dry materials

Conversion factor: 1 Btu·in/(h·ft²·°F) = 0.1442 W/(m·K)

| Material | k at 24°C, W/(m·K) | k at 24°C, Btu·in/(h·ft²·°F) |
|----------|-------------------|------------------------------|
| Copper | 401 | 2780 |
| Aluminum | 237 | 1644 |
| Steel (mild) | 45.3 | 314 |
| Stainless steel 304 | 16.2 | 112 |
| Concrete (normal) | 1.4 | 9.7 |
| Mineral fiber insulation | 0.036 | 0.25 |
| Polyurethane foam | 0.023 | 0.16 |
| Air (still, 1 atm) | 0.026 | 0.18 |

### Specific Heat Capacity

Specific heat (cp) represents the energy required to raise unit mass by unit temperature:

- **Units**: J/(kg·K) [SI], Btu/(lb·°F) [I-P]
- **Significance**: Determines thermal mass and energy storage capacity
- **System impact**: High specific heat materials moderate temperature swings
- **Phase change**: Discontinuous at melting/freezing points

Conversion factor: 1 Btu/(lb·°F) = 4186.8 J/(kg·K)

Water exhibits exceptionally high specific heat (4186 J/(kg·K) at 15°C), making it ideal for thermal energy storage and distribution. Most building materials have specific heat between 800-1000 J/(kg·K).

### Density

Density (ρ) affects thermal mass, structural loading, and acoustic performance:

- **Units**: kg/m³ [SI], lb/ft³ [I-P]
- **Thermal mass**: Product ρcp determines volumetric heat capacity
- **Structural**: Directly impacts dead loads on building structures
- **Range**: 10 kg/m³ (spray foam) to 8900 kg/m³ (copper)

Conversion factor: 1 lb/ft³ = 16.02 kg/m³

## Thermal Diffusivity

Thermal diffusivity (α) combines thermal properties to characterize transient heat transfer:

α = k / (ρ·cp)

- **Units**: m²/s [SI], ft²/h [I-P]
- **Physical meaning**: Rate of temperature change within material
- **High α**: Metals respond quickly to temperature changes
- **Low α**: Insulation materials exhibit slow thermal response

Materials with high thermal diffusivity reach thermal equilibrium rapidly. Concrete (α ≈ 7×10⁻⁷ m²/s) has lower diffusivity than aluminum (α ≈ 9.7×10⁻⁵ m²/s), explaining aluminum's faster temperature response.

## Mechanical Properties

Mechanical properties determine structural integrity, installation methods, and service life.

### Tensile and Yield Strength

Tensile strength defines maximum stress before fracture. Yield strength indicates onset of permanent deformation.

| Material | Yield Strength, MPa | Tensile Strength, MPa |
|----------|--------------------|-----------------------|
| Structural steel A36 | 250 | 400-550 |
| Copper tube (hard) | 275 | 345 |
| Aluminum 6061-T6 | 275 | 310 |
| PVC pipe | 48 | 52 |
| Concrete (28-day) | N/A | 20-40 (compression) |

### Modulus of Elasticity

Young's modulus (E) quantifies stiffness and deflection characteristics:

- **Steel**: 200 GPa (29×10⁶ psi)
- **Aluminum**: 69 GPa (10×10⁶ psi)
- **Concrete**: 17-31 GPa (2.5-4.5×10⁶ psi)
- **PVC**: 2.4-4.1 GPa (350-600×10³ psi)

Piping systems require adequate support spacing based on modulus to prevent excessive sag under fluid weight.

### Coefficient of Thermal Expansion

Linear thermal expansion coefficient (α_L) governs dimensional changes with temperature:

α_L = (ΔL/L) / ΔT

| Material | α_L, µm/(m·K) | α_L, in/(in·°F) ×10⁻⁶ |
|----------|---------------|----------------------|
| Copper | 16.5 | 9.2 |
| Steel | 11.7 | 6.5 |
| Aluminum | 23.6 | 13.1 |
| PVC | 50.4 | 28.0 |
| Concrete | 9-14 | 5-8 |
| Glass | 8.5 | 4.7 |

High expansion coefficients necessitate expansion loops, expansion joints, or flexible connectors in piping systems. Temperature excursions of 50 K in 10 m copper pipe produce 8.3 mm expansion.

## Material Selection Criteria

Selection of HVAC materials balances multiple performance requirements:

1. **Thermal performance**: Conductivity, thermal mass, temperature limits
2. **Mechanical strength**: Pressure rating, structural capacity, fatigue resistance
3. **Corrosion resistance**: Compatibility with fluids, galvanic coupling, atmospheric exposure
4. **Cost**: Initial material cost, installation labor, lifecycle maintenance
5. **Code compliance**: Material standards (ASTM, ASME, CSA), pressure vessel codes
6. **Availability**: Lead times, local suppliers, standard sizes
7. **Joining methods**: Welding, brazing, mechanical, solvent cement, threading
8. **Temperature range**: Operating limits, freeze protection, high-temperature capability

## Temperature-Dependent Properties

Material properties vary significantly with temperature, affecting design calculations.

### Conductivity Temperature Dependence

Most solid materials exhibit increasing thermal conductivity with temperature:

k(T) = k₀[1 + β(T - T₀)]

where β is temperature coefficient of conductivity (typically 0.001-0.003 K⁻¹ for metals).

Insulation materials show complex temperature dependence due to changing contributions from conduction, convection, and radiation within porous structures.

### Specific Heat Variation

Specific heat generally increases with temperature. Water shows anomalous behavior with cp minimum at 35°C.

For accurate enthalpy calculations across wide temperature ranges, integrate variable specific heat:

h₂ - h₁ = ∫[T₁ to T₂] cp(T) dT

## Property Data Sources

ASHRAE Handbook—Fundamentals provides comprehensive property data:

- **Chapter 33 (2021)**: Physical properties of materials
- **Chapter 26 (2021)**: Heat, air, and moisture transfer in building assemblies
- **Chapter 2 (2021)**: Thermodynamics and refrigeration cycles
- **Table format**: Properties at standard conditions with temperature corrections

Additional authoritative sources include:

- **NIST**: Thermophysical property databases (REFPROP for refrigerants)
- **ASTM standards**: Material specifications with property requirements
- **Manufacturer data**: Certified test data for proprietary materials
- **Engineering references**: Perry's Chemical Engineers' Handbook, Marks' Standard Handbook

## Moisture Effects on Properties

Water absorption dramatically alters thermal properties of porous materials.

### Thermal Conductivity Increase

Water (k = 0.6 W/(m·K)) conducts heat 23 times better than air (k = 0.026 W/(m·K)). Moisture in porous insulation displaces air, increasing effective conductivity:

- **Fiberglass**: 1% moisture by volume increases k by 5-8%
- **Mineral wool**: Similar moisture sensitivity to fiberglass
- **Closed-cell foam**: Minimal moisture absorption, stable conductivity
- **Cellulose**: High moisture sensitivity, requires vapor retarders

Wet insulation loses effectiveness and promotes mold growth. Proper vapor barrier placement and air sealing prevent moisture accumulation.

### Density and Specific Heat

Absorbed moisture increases both density and specific heat, raising thermal mass of building assemblies. High thermal mass benefits include:

- Temperature swing reduction in occupied spaces
- Peak load shifting for demand management
- Improved thermal comfort through radiant temperature stabilization

## Emissivity and Surface Properties

Surface emissivity (ε) governs radiative heat transfer between surfaces and surroundings.

| Surface | Emissivity ε |
|---------|--------------|
| Polished aluminum | 0.04-0.06 |
| Galvanized steel (new) | 0.23 |
| Oxidized steel | 0.80 |
| Painted surfaces | 0.90-0.95 |
| Glass | 0.84 |
| Brick | 0.93 |

Low-emissivity coatings on radiant barriers reduce radiative heat transfer. Aluminum foil facing on insulation (ε ≈ 0.05) reflects radiant heat, reducing effective thermal conductivity of air spaces.

Radiative heat transfer between parallel surfaces:

q/A = σ·ε_eff·(T₁⁴ - T₂⁴)

where ε_eff accounts for emissivities of both surfaces and geometry.

## Acoustic Properties

HVAC materials provide sound absorption and transmission loss.

### Sound Absorption Coefficient

Absorption coefficient (α) indicates fraction of incident sound energy absorbed:

- **Fiberglass duct liner**: α = 0.70-0.95 (500-4000 Hz)
- **Acoustic ceiling tile**: α = 0.55-0.75 (500-4000 Hz)
- **Concrete block**: α = 0.05-0.35 (500-4000 Hz)
- **Gypsum board**: α = 0.05-0.10 (500-4000 Hz)

Porous, fibrous materials absorb sound effectively, particularly at higher frequencies.

### Sound Transmission Class

STC rating quantifies airborne sound isolation through partitions. Higher STC values indicate better sound isolation. HVAC shafts, mechanical room walls, and vibration-isolated equipment foundations require high STC construction.

## Property Uncertainty and Safety Factors

Published material properties represent typical values with inherent variability:

- **Manufacturing tolerances**: Composition, processing affect properties
- **Testing methods**: Different standards yield different results
- **Aging effects**: Degradation over time changes properties
- **Installation quality**: Gaps, compression, moisture damage

Conservative design practice applies safety factors to critical properties and verifies actual performance through field testing and commissioning.
