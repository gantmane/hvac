---
title: "Enclosure Radiation"
weight: 3
---

Enclosure radiation analysis addresses heat exchange between multiple surfaces that form a closed or partially closed volume. This is fundamental to HVAC applications including building surfaces, duct interiors, radiant heating panels, and furnace chambers.

## View Factors

View factors (also called shape factors or configuration factors) quantify the geometric relationship between surfaces exchanging radiation.

### Definition

The view factor F₁₂ represents the fraction of radiation leaving surface 1 that is intercepted by surface 2:

F₁₂ = (1/A₁) ∫∫(cos θ₁ cos θ₂)/(πr²) dA₁ dA₂

Where:
- A₁ = area of surface 1 (ft² or m²)
- θ₁, θ₂ = angles between surface normals and line connecting differential areas
- r = distance between differential areas (ft or m)

### Fundamental Properties

**Reciprocity Relation:**

A₁F₁₂ = A₂F₂₁

This allows calculation of one view factor from another when areas are known.

**Summation Rule:**

For an N-surface enclosure:

Σ(j=1 to N) Fᵢⱼ = 1

All radiation leaving surface i must reach some surface in the enclosure (including itself if concave).

**Superposition:**

View factors are additive. For composite surface (1+2) viewing surface 3:

A₁₊₂F₁₊₂,₃ = A₁F₁,₃ + A₂F₂,₃

### View Factor Tables

**Parallel Directly Opposed Rectangles:**

| Aspect Ratio X/D | Aspect Ratio Y/D | View Factor F₁₂ |
|------------------|------------------|-----------------|
| 0.5 | 0.5 | 0.120 |
| 1.0 | 1.0 | 0.200 |
| 2.0 | 2.0 | 0.415 |
| 5.0 | 5.0 | 0.718 |
| 10.0 | 10.0 | 0.851 |

Where X and Y are rectangle dimensions, D is separation distance.

**Perpendicular Rectangles with Common Edge:**

| Height/Width | Depth/Width | View Factor F₁₂ |
|--------------|-------------|-----------------|
| 1.0 | 1.0 | 0.200 |
| 2.0 | 2.0 | 0.260 |
| 5.0 | 5.0 | 0.298 |
| 10.0 | 10.0 | 0.312 |

**Two Infinite Parallel Plates:**

F₁₂ = 1.0 (all radiation from one plate reaches the other)

**Small Object in Large Enclosure:**

F₁₂ ≈ 1.0 (nearly all radiation from small object reaches enclosure)
F₂₁ ≈ A₁/A₂ (very small fraction of enclosure radiation reaches object)

## Radiosity Method

Radiosity (J) represents the total radiant energy leaving a surface per unit area, including both emitted and reflected radiation.

### Radiosity Definition

J = E + ρG = εEᵦ + ρG

Where:
- E = emitted radiation (Btu/hr-ft² or W/m²)
- G = irradiation (incident radiation)
- ρ = reflectivity
- ε = emissivity
- Eᵦ = blackbody emissive power = σT⁴

For gray, diffuse, opaque surfaces: ρ = 1 - ε

Therefore:

J = εσT⁴ + (1-ε)G

### Surface Energy Balance

Net radiation leaving surface i:

qᵢ = Aᵢ(Jᵢ - Gᵢ)

The irradiation is the sum of radiosities from all surfaces:

Gᵢ = Σ(j=1 to N) FᵢⱼJⱼ

Combining:

qᵢ = Aᵢ[Jᵢ - Σ(j=1 to N) FᵢⱼJⱼ]

## Radiation Network Method

The electrical network analogy simplifies enclosure radiation analysis by representing the problem as thermal resistances and potentials.

### Surface Resistance

Resistance between blackbody emissive power and radiosity:

Rₛᵤᵣf,ᵢ = (1-εᵢ)/(εᵢAᵢ)

This represents the surface's resistance to emitting radiation based on its emissivity.

### Space Resistance

Resistance between surfaces due to geometry:

Rₛₚₐcₑ,ᵢⱼ = 1/(AᵢFᵢⱼ) = 1/(AⱼFⱼᵢ)

This is analogous to radiative exchange area.

### Network Heat Transfer

Heat transfer from surface i to j:

qᵢⱼ = (Eᵦ,ᵢ - Eᵦ,ⱼ)/(Rₛᵤᵣf,ᵢ + Rₛₚₐcₑ,ᵢⱼ + Rₛᵤᵣf,ⱼ)

qᵢⱼ = (σT₁⁴ - σT₂⁴)/[(1-ε₁)/(ε₁A₁) + 1/(A₁F₁₂) + (1-ε₂)/(ε₂A₂)]

## Gray Body Exchange Between Two Surfaces

For two gray, diffuse, opaque surfaces forming an enclosure:

q₁₂ = (σA₁(T₁⁴ - T₂⁴))/[1/ε₁ + (A₁/A₂)(1/ε₂ - 1) + (1-F₁₂)/F₁₂]

### Special Cases

**Infinite Parallel Plates (F₁₂ = 1, A₁ = A₂):**

q₁₂/A = σ(T₁⁴ - T₂⁴)/(1/ε₁ + 1/ε₂ - 1)

**Small Object in Large Enclosure (A₁ << A₂):**

q₁ = ε₁A₁σ(T₁⁴ - T₂⁴)

The emissivity of the large enclosure becomes irrelevant.

**Concentric Cylinders or Spheres:**

q = (σA₁(T₁⁴ - T₂⁴))/[1/ε₁ + (r₁/r₂)(1/ε₂ - 1)]

Where r₁ and r₂ are inner and outer radii.

## Three Surface Enclosures

For three-surface enclosures (common in HVAC: floor, ceiling, walls), the network method requires solving simultaneous equations.

### Network Equations

For surface i at known temperature:

Eᵦ,ᵢ = Jᵢ + (1-εᵢ)/εᵢAᵢ · Σ(j=1 to 3) (Jᵢ - Jⱼ)/(1/AᵢFᵢⱼ)

For three surfaces:
- If all temperatures are known: solve for radiosities J₁, J₂, J₃
- If one heat flux is specified: solve for that temperature

### Refractory Surfaces

A refractory (re-radiating) surface has zero net heat transfer (qᵢ = 0). It reaches an equilibrium temperature where absorbed radiation equals emitted radiation.

For refractory surface r:

Jᵣ = Σ(j=1 to N) FᵣⱼJⱼ

The refractory surface redistributes radiation but adds no thermal resistance.

## Radiation Shields

Radiation shields are low-emissivity surfaces placed between hot and cold surfaces to reduce radiant heat transfer.

### Single Shield Analysis

For infinite parallel plates with one shield:

q/A = σ(T₁⁴ - T₂⁴)/[(1/ε₁ + 1/ε₂ - 1) + (1/ε₃,ₐ + 1/ε₃,ᵦ - 1)]

Where ε₃,ₐ and ε₃,ᵦ are shield emissivities on sides facing surfaces 1 and 2.

For a shield with equal emissivities on both sides (ε₃,ₐ = ε₃,ᵦ = ε₃):

q/A = σ(T₁⁴ - T₂⁴)/[(1/ε₁ + 1/ε₂ - 1) + 2/ε₃ - 1]

### Shield Effectiveness

Reduction factor with one shield:

q_with_shield/q_without_shield = (1/ε₁ + 1/ε₂ - 1)/[(1/ε₁ + 1/ε₂ - 1) + (2/ε₃ - 1)]

For low-emissivity shield (ε₃ = 0.05) between surfaces with ε₁ = ε₂ = 0.9:

Reduction factor = 0.026 (96% reduction in heat transfer)

### Multiple Shields

With N shields between parallel plates:

q/A = σ(T₁⁴ - T₂⁴)/[(1/ε₁ + 1/ε₂ - 1) + N(2/ε_shield - 1)]

For identical shields with ε = 0.05:

| Number of Shields | Relative Heat Transfer |
|-------------------|------------------------|
| 0 | 1.000 |
| 1 | 0.026 |
| 2 | 0.014 |
| 3 | 0.009 |
| 5 | 0.006 |

### Shield Temperature

The shield reaches an equilibrium temperature between the boundary surfaces. For single shield with equal emissivities:

T₃⁴ ≈ (T₁⁴ + T₂⁴)/2

More precisely, solve:

(T₁⁴ - T₃⁴)/(1/ε₁ + 1/ε₃ - 1) = (T₃⁴ - T₂⁴)/(1/ε₃ + 1/ε₂ - 1)

## HVAC Enclosure Applications

### Building Envelope Radiation

Room surfaces exchange radiation continuously. For a rectangular room:
- 6 surfaces (floor, ceiling, 4 walls)
- Surface temperatures vary with solar gains, heating/cooling
- Mean radiant temperature affects occupant comfort

Simplified calculation using area-weighted average:

MRT = Σ(AᵢTᵢ)/Σ(Aᵢ)

### Radiant Panel Systems

Ceiling or floor radiant panels exchange with room surfaces:

q_panel = A_panel · ε_panel · σ · Σ Fₚ,ᵢ(T_panel⁴ - Tᵢ⁴)

Typical ceiling panel view factors to floor: 0.3-0.5 depending on ceiling height.

### Duct Interior Radiation

In large rectangular or round ducts, radiation between interior surfaces affects heat transfer:
- Important at temperatures above 200°F (93°C)
- Combined convection-radiation heat transfer
- View factors approach 1.0 for long ducts

### Furnace and Boiler Chambers

Combustion chambers involve high-temperature radiation:
- Flame radiation to furnace walls
- Multiple surface enclosures (burner, walls, tubes)
- Combination of gas and surface radiation
- Temperatures 1000-3000°F (540-1650°C)

## Matrix Solution Methods

For N-surface enclosures, radiosity equations form a system of linear equations:

[A][J] = [B]

Where:
- [A] = coefficient matrix involving view factors
- [J] = radiosity vector
- [B] = vector of known quantities (blackbody emissive powers)

For surface i:

Jᵢ(1 - Σ ρᵢFᵢᵢ) - Σ(j≠i) ρᵢFᵢⱼJⱼ = εᵢσTᵢ⁴

This system is solved numerically for unknown radiosities, then heat fluxes are calculated:

qᵢ = εᵢAᵢ(σTᵢ⁴ - Jᵢ)/(1-εᵢ)

## Design Considerations

**Surface Selection:**
- Low-emissivity surfaces (ε < 0.1) for radiation barriers
- High-emissivity surfaces (ε > 0.9) for radiant heat transfer
- Polished aluminum: ε ≈ 0.05
- Painted surfaces: ε ≈ 0.85-0.95

**Geometric Configuration:**
- Maximize view factors for desired heat transfer
- Minimize view factors where heat transfer is unwanted
- Use shields to redirect radiation paths

**Temperature Levels:**
- Radiation becomes dominant above 400°F (204°C)
- Fourth power temperature dependence makes high-temperature radiation critical
- Combined radiation-convection analysis required for moderate temperatures

## Components

- Two Surface Enclosures
- Three Surface Enclosures
- N Surface Enclosures
- Radiation Network Method
- Matrix Solution Methods
- Electrical Analogy
- Gray Diffuse Surfaces
- Opaque Surfaces
- Refractory Surfaces
- Radiation Shields
- Multiple Shields
- Shield Optimization
