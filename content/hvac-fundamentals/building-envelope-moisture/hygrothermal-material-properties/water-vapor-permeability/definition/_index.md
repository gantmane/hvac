---
title: "Definition and Fundamental Concepts"
description: "Technical definition of water vapor permeability and permeance, including governing physics, measurement units, material property relationships, and distinction between permeability coefficients and installed permeance values."
weight: 1
---

Water vapor permeability quantifies a material's intrinsic ability to permit water vapor transmission through molecular diffusion. This fundamental hygrothermal property governs moisture migration through building envelope assemblies and determines condensation risk, drying capacity, and long-term durability performance.

## Physical Basis

Water vapor diffusion through porous building materials follows Fick's first law of diffusion, driven by vapor pressure gradients across material boundaries. The diffusion process occurs through:
- **Gas-phase diffusion** through interconnected pores and voids
- **Surface diffusion** along internal pore surfaces
- **Sorption-desorption cycles** in hygroscopic materials

The steady-state vapor flux through a homogeneous material layer is expressed:

g = -μ × A × (∂P_v / ∂x)

Where:
- g = vapor flux (mass/time)
- μ = vapor permeability coefficient (mass·length / time·area·pressure)
- A = cross-sectional area perpendicular to flux
- ∂P_v/∂x = vapor pressure gradient through thickness

## Permeability Coefficient

The permeability coefficient (μ) represents an intensive material property independent of specimen thickness. This intrinsic characteristic depends on:

**Material microstructure**:
- Porosity and pore size distribution
- Tortuosity of diffusion pathways
- Pore connectivity and dead-end pore fraction
- Surface area available for sorption

**Environmental conditions**:
- Temperature affects molecular diffusion rate
- Relative humidity influences hygroscopic moisture content
- Pressure affects gas-phase diffusion coefficients

Standard units:
- IP units: perm·inch = grain/(hr·ft²·in.Hg·inch)
- SI units: kg·m/(Pa·s·m²) = kg/(Pa·s·m)

## Permeance Definition

Permeance (M) represents the vapor transmission characteristic of a specific material specimen accounting for installed thickness:

M = μ / t

Where:
- M = permeance (perm or grain/hr·ft²·in.Hg)
- μ = permeability coefficient (perm·inch)
- t = material thickness (inch)

**Critical distinction**: Permeance is an extensive property that varies with thickness, while permeability is intensive and thickness-independent.

Standard permeance units:
- IP units: 1 perm = 1 grain/(hr·ft²·in.Hg)
- SI units: 1 perm = 5.75 × 10⁻¹¹ kg/(Pa·s·m²)

## Permeance vs. Permeability

The relationship between permeability and permeance parallels thermal property relationships:

| Thermal Property | Moisture Property | Units (IP) | Thickness Dependence |
|-----------------|------------------|-----------|---------------------|
| Thermal conductivity (k) | Permeability (μ) | perm·inch | Independent |
| Thermal resistance (R) | Vapor resistance (1/M) | 1/perm | Linear with thickness |
| Thermal conductance (C) | Permeance (M) | perm | Inverse with thickness |

**Example calculation**:
- Material: XPS rigid insulation
- Permeability: μ = 1.0 perm·inch
- Installed thickness: t = 2 inches
- Permeance: M = 1.0 / 2 = 0.5 perm

Doubling thickness halves permeance (doubles vapor resistance).

## Thickness Independence of Permeability

Permeability remains constant regardless of specimen thickness for homogeneous materials under steady-state conditions:

**Experimental verification**:
- Test specimens of varying thickness (0.5", 1.0", 2.0")
- Measure permeance M for each thickness
- Calculate permeability μ = M × t
- Result: μ constant across thickness range

**Practical implications**:
- Published permeability data applies to any installed thickness
- Assembly calculations use permeance (accounting for actual thickness)
- Multi-layer assemblies require individual layer permeance values

## Material Property Classification

Materials exhibit vastly different permeability coefficients:

| Material Category | Permeability Range (perm·inch) | Relative Permeability |
|------------------|------------------------------|---------------------|
| Metals, glass | 0.00 | Impermeable |
| Polymer membranes | 0.01 - 0.1 | Very low |
| Closed-cell foams | 0.2 - 3.0 | Low |
| Wood products | 0.4 - 2.0 | Low to moderate |
| Mineral insulations | 50 - 200+ | Very high |
| Fibrous insulations | 100 - 500+ | Extremely high |

## Vapor Resistance

The inverse of permeance defines vapor resistance, analogous to thermal resistance:

R_vapor = 1 / M = t / μ

Where:
- R_vapor = vapor resistance (perm⁻¹ or rep)
- M = permeance (perm)
- t = thickness (inch)
- μ = permeability (perm·inch)

**Series resistance**:
Multi-layer assemblies exhibit total vapor resistance equal to the sum of individual layer resistances:

R_total = R₁ + R₂ + R₃ + ... + Rₙ

Total permeance:
M_total = 1 / R_total

## Environmental Dependence

Permeability varies with temperature and humidity for many materials:

**Temperature effects**:
- Molecular diffusion increases approximately 1-2% per °C
- Gas permeability follows Arrhenius relationship
- Most significant for polymer membranes

**Humidity effects**:
- Hygroscopic materials exhibit increased permeability at high RH
- Moisture content in pores enhances vapor transport
- "Smart" vapor retarders exploit this phenomenon
- OSB permeability increases 3-5× from dry to wet conditions

## Measurement Standards

ASTM E96 defines standardized test methods:

**Dry cup method** (desiccant):
- Used for materials >1 perm
- Desiccant maintains 0% RH on one side
- Test chamber at 50% RH
- Weight gain indicates vapor transmission

**Wet cup method** (water):
- Used for materials <1 perm
- Water maintains 100% RH on one side
- Test chamber at 50% RH
- Weight loss indicates vapor transmission

**Test conditions**:
- Standard: 73.4°F (23°C)
- Alternative: 90°F for hot-humid applications
- Constant temperature and humidity maintained
- Steady-state conditions verified before measurement

## Engineering Applications

Permeability and permeance values enable quantitative hygrothermal analysis:

**Condensation risk assessment**: Dewpoint calculations determine if vapor pressure at any interface exceeds saturation pressure.

**Drying time prediction**: Permeance values with vapor pressure differentials calculate moisture removal rates.

**Vapor retarder specification**: Code-compliant material selection based on permeance classification (Class I, II, III).

**Assembly optimization**: Balancing vapor control on high-pressure side with drying capacity on opposite side.

Understanding the distinction between permeability (material property) and permeance (installed performance) enables proper specification and analysis of moisture control strategies in building envelope design.
