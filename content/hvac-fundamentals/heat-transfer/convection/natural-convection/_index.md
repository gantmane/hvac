---
title: "Natural Convection"
weight: 2
---

Natural convection heat transfer occurs when fluid motion is driven solely by buoyancy forces resulting from density differences caused by temperature gradients. This mechanism dominates in quiescent environments and drives airflow patterns in buildings, enclosures, and around heated or cooled surfaces.

## Physical Mechanism

Buoyancy-driven flow develops when fluid near a surface is heated or cooled relative to the surrounding fluid. Temperature changes alter fluid density according to:

ρ = ρ₀[1 - β(T - T₀)]

Where:
- ρ = fluid density at temperature T (kg/m³)
- ρ₀ = reference density at T₀ (kg/m³)
- β = volumetric thermal expansion coefficient (1/K)
- For ideal gases: β = 1/T_film (where T_film is in Kelvin)

The resulting density difference creates a net buoyancy force that initiates fluid motion. Heavier (cooler) fluid sinks while lighter (warmer) fluid rises, establishing circulation patterns.

## Grashof Number

The Grashof number characterizes the ratio of buoyancy forces to viscous forces:

Gr_L = (g β ΔT L³) / ν²

Where:
- g = gravitational acceleration (9.81 m/s²)
- β = volumetric expansion coefficient (1/K)
- ΔT = T_surface - T_∞ (K or °C)
- L = characteristic length (m)
- ν = kinematic viscosity (m²/s)

The Grashof number plays an analogous role in natural convection to the Reynolds number in forced convection. It indicates flow regime:

| Gr_L Range | Flow Regime |
|------------|-------------|
| < 10⁹ | Laminar |
| 10⁹ - 10¹⁰ | Transition |
| > 10¹⁰ | Turbulent |

## Rayleigh Number

The Rayleigh number combines buoyancy and thermal diffusion effects:

Ra_L = Gr_L × Pr = (g β ΔT L³) / (ν α)

Where:
- Pr = Prandtl number = ν/α
- α = thermal diffusivity (m²/s)

The Rayleigh number determines heat transfer intensity and boundary layer development. Critical values indicate transitions between flow regimes and heat transfer correlations.

## Vertical Surfaces

Vertical plates and walls generate upward or downward flow depending on surface temperature relative to ambient.

### Laminar Flow (10⁴ < Ra_L < 10⁹)

Average Nusselt number:

Nu_L = 0.59 Ra_L^(1/4)

Local Nusselt number:

Nu_x = 0.508 Pr^(1/2) / [0.952 + Pr]^(1/4) × Gr_x^(1/4)

Boundary layer thickness grows as x^(1/4) from the leading edge.

### Turbulent Flow (Ra_L > 10⁹)

Nu_L = 0.10 Ra_L^(1/3)

This correlation applies to vertical surfaces with:
- Height 0.1 to 10 m
- Temperature differences 5 to 50°C
- Air at atmospheric pressure

### General Correlation (All Ra_L)

Churchill-Chu correlation for isothermal vertical plates:

Nu_L = [0.825 + (0.387 Ra_L^(1/6)) / (1 + (0.492/Pr)^(9/16))^(8/27)]²

Valid for entire range of Ra_L and Pr.

## Horizontal Surfaces

Heat transfer depends on surface orientation relative to thermal gradient.

### Hot Surface Facing Up or Cold Surface Facing Down

Nu_L = 0.54 Ra_L^(1/4)     for 10⁴ < Ra_L < 10⁷

Nu_L = 0.15 Ra_L^(1/3)     for 10⁷ < Ra_L < 10¹¹

### Hot Surface Facing Down or Cold Surface Facing Up

Nu_L = 0.27 Ra_L^(1/4)     for 10⁵ < Ra_L < 10¹⁰

Characteristic length L = A_s / P where A_s is surface area and P is perimeter.

## Inclined Surfaces

For surfaces tilted at angle θ from vertical, replace g with g cos(θ) in Grashof and Rayleigh number calculations when θ < 60°. Beyond 60° from vertical, horizontal surface correlations become more appropriate.

For heated plates facing upward at inclination θ:

Nu = Nu_vertical × (cos θ)^n

Where n varies from 0.25 to 0.33 depending on Ra_L.

## Enclosed Spaces

Natural convection in enclosures drives heat transfer across building cavities, glazing systems, and equipment housings.

### Vertical Rectangular Enclosures

For air spaces with height H, spacing δ, and hot/cold vertical walls:

Nu = 0.18 (Pr / (0.2 + Pr) × Ra_δ)^0.29     for Ra_δ < 10³

Nu = 0.22 (Pr / (0.2 + Pr) × Ra_δ × (H/δ)^(-1/4))^0.28     for 10³ < Ra_δ < 10¹⁰

Here Ra_δ is based on spacing δ.

### Horizontal Enclosures

Heat transfer across horizontal air layers (heated from below):

Nu = 1 + 1.44[1 - 1708/Ra_L]⁺[1 - 1708(sin 1.8θ)^1.6/Ra_L]⁺ + [(Ra_L/5830)^(1/3) - 1]⁺

Where [X]⁺ = max(X, 0).

For heated from above: Nu = 1 (pure conduction).

### Concentric Cylinders and Spheres

Annular spaces between pipes or spherical shells use effective conductivity approach:

k_eff = k × Nu

Where Nu correlations depend on geometry and modified Rayleigh numbers.

## Building Natural Convection

### Room Air Motion

Natural convection establishes circulation patterns in occupied spaces:

- Warm surfaces (radiators, sunlit windows): rising plumes
- Cold surfaces (exterior walls, glazing): descending flows
- Stratification develops with warm air accumulating at ceiling
- Floor-to-ceiling temperature gradients typically 1-3°C in conditioned spaces

### Surface Heat Transfer Coefficients

Typical natural convection coefficients for building surfaces:

| Surface Type | Orientation | h (W/m²·K) |
|--------------|-------------|------------|
| Interior wall | Vertical | 3-5 |
| Ceiling | Heat flow up | 4-6 |
| Ceiling | Heat flow down | 1-2 |
| Floor | Heat flow up | 1-2 |
| Floor | Heat flow down | 4-6 |
| Window glazing | Vertical | 3-4 |

These values assume ΔT = 5-15°C and still air conditions.

### Thermal Plumes

Rising thermal plumes from heat sources create characteristic velocity and temperature profiles:

- Centerline velocity: w ∝ z^(1/3) Q^(1/3)
- Plume width: b ∝ z
- Entrainment draws surrounding air into plume

Where z is height above source and Q is heat release rate.

### Stratification

Temperature stratification in tall spaces follows approximate relationship:

dT/dz ≈ 0.5 to 2.0 K/m

Stronger stratification occurs with:
- Higher ceilings
- Greater heat inputs
- Lower ventilation rates
- Fewer obstructions to vertical airflow

## Mixed Convection

When both natural and forced convection are significant:

Combined regime: 0.1 < Gr_L/Re_L² < 10

For Gr_L/Re_L² < 0.1: forced convection dominates
For Gr_L/Re_L² > 10: natural convection dominates

## Application Guidelines

**Use natural convection correlations when:**
- Air velocities < 0.2 m/s
- No mechanical air movement present
- Analyzing free-standing equipment in still air
- Evaluating building envelope heat transfer
- Assessing cavity/enclosure heat transfer

**Consider forced convection when:**
- Fans or air handlers operate
- Wind effects are significant
- Duct or pipe flows exist
- Equipment has integral fans

## Practical Considerations

**Temperature difference selection:**
Use film temperature T_film = (T_surface + T_∞)/2 for property evaluation.

**Characteristic length:**
- Vertical plates: height L = H
- Horizontal plates: L = A_s/P
- Cylinders: diameter or length depending on orientation
- Enclosures: gap spacing or height depending on configuration

**Property variation:**
Air properties vary significantly with temperature. Evaluate properties at film temperature for accuracy within 5-10%.

**Surface emissivity:**
Natural convection surfaces often exchange radiation simultaneously. Total heat transfer includes both modes.

## Components

- Grashof Number
- Rayleigh Number
- Vertical Plates
- Horizontal Plates
- Inclined Plates
- Vertical Cylinders
- Horizontal Cylinders
- Spheres
- Enclosed Spaces
- Rectangular Cavities
- Concentric Cylinders
- Concentric Spheres
- Combined Free Forced Convection
