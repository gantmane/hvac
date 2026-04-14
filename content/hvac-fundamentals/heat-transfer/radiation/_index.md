---
title: "Radiation"
aliases: ["Radiation"]
description: "Comprehensive coverage of thermal radiation heat transfer including Stefan-Boltzmann Law, radiative properties, view factors, solar radiation, and HVAC applications in radiant systems and building energy analysis."
weight: 3
---

Radiation heat transfer occurs through electromagnetic wave propagation without requiring a physical medium. Unlike conduction and convection, radiation can transfer energy across vacuum and becomes increasingly significant at elevated temperatures due to its fourth-power temperature dependence.

## Stefan-Boltzmann Law and Blackbody Radiation

A blackbody represents an ideal surface that absorbs all incident radiation and emits the maximum possible thermal radiation at any given temperature. The total emissive power of a blackbody follows the Stefan-Boltzmann Law:

**Eb = σT⁴**

Where:
- Eb = blackbody emissive power (W/m²)
- σ = Stefan-Boltzmann constant (5.670 × 10⁻⁸ W/m²·K⁴)
- T = absolute surface temperature (K)

The spectral distribution of blackbody radiation is governed by Planck's Law, with peak wavelength shifting toward shorter wavelengths as temperature increases (Wien's displacement law). For HVAC applications, building surfaces typically operate at 250-320 K, emitting primarily in the longwave infrared spectrum (4-50 μm).

## Radiative Surface Properties

Real surfaces deviate from blackbody behavior through four fundamental properties that must sum to unity:

**α + ρ + τ = 1**

Where α (absorptivity), ρ (reflectivity), and τ (transmissivity) represent the fractions of incident radiation absorbed, reflected, and transmitted, respectively.

**Emissivity (ε)** quantifies the ratio of actual surface emission to blackbody emission at the same temperature. For real surfaces:

**E = εσT⁴**

By Kirchhoff's Law, for surfaces in thermal equilibrium, directional spectral emissivity equals directional spectral absorptivity (ε = α). This equivalence is crucial for analyzing radiation exchange between building surfaces.

Common HVAC material emissivities:
- Polished aluminum: 0.04-0.06
- Galvanized steel (new): 0.23-0.28
- Concrete, brick: 0.85-0.95
- Paint (most colors): 0.85-0.95
- Low-e coatings: 0.02-0.20

## Gray Body Approximation

The gray body assumption simplifies radiation calculations by treating radiative properties as independent of wavelength. While not perfectly accurate (most surfaces exhibit selective behavior), this approximation provides acceptable accuracy for most HVAC load calculations and is adopted throughout ASHRAE Fundamentals. The gray body assumption allows emissivity to be treated as a single value rather than a spectral distribution.

## View Factors and Surface Exchange

Radiation exchange between surfaces depends on geometric configuration through view factors (also called shape factors or configuration factors). The view factor F₁₋₂ represents the fraction of radiation leaving surface 1 that directly strikes surface 2.

Fundamental view factor relationships:
- **Reciprocity**: A₁F₁₋₂ = A₂F₂₋₁
- **Summation**: Σ Fᵢ₋ⱼ = 1 (for enclosure)

Net radiation exchange between two gray, diffuse, opaque surfaces:

**Q₁₋₂ = (σ(T₁⁴ - T₂⁴)) / ((1-ε₁)/(ε₁A₁) + 1/(A₁F₁₋₂) + (1-ε₂)/(ε₂A₂))**

For infinite parallel planes (F₁₋₂ = 1, A₁ = A₂):

**q = σ(T₁⁴ - T₂⁴) / (1/ε₁ + 1/ε₂ - 1)**

This simplified geometry applies to radiant ceiling panels, floor heating systems, and wall cavity analysis.

## Solar Radiation Fundamentals

Solar radiation reaching building surfaces consists of three components:

1. **Direct (beam) radiation**: Travels directly from sun to surface without scattering
2. **Diffuse (sky) radiation**: Scattered by atmospheric constituents and clouds
3. **Reflected (ground) radiation**: Reflected from surrounding surfaces (ground albedo typically 0.2)

Total incident solar radiation on a surface:

**Iₜₒₜₐₗ = Iᵦₑₐₘ·cos(θ) + Iᵈⁱᶠᶠᵘˢᵉ + Iʳᵉᶠˡᵉᶜᵗᵉᵈ**

Where θ is the incident angle between beam radiation and surface normal.

ASHRAE Fundamentals Chapter 14 provides clear-sky solar radiation models and typical meteorological year (TMY) data for building energy analysis. Solar heat gain through fenestration is calculated using solar heat gain coefficient (SHGC) values that account for both transmitted and absorbed-then-reradiated components.

## Mean Radiant Temperature (MRT)

Mean radiant temperature quantifies the uniform surface temperature of an imaginary enclosure that would produce the same radiation exchange with the occupant as the actual non-uniform environment:

**MRT = [(Σ Fₚ₋ᵢ·Tᵢ⁴)]^(1/4)**

Where Fₚ₋ᵢ represents view factors from the person to each surface i, and Tᵢ is the absolute temperature of surface i.

MRT significantly influences thermal comfort, particularly in high-performance buildings with large window areas. A person positioned near cold windows in winter experiences reduced MRT despite adequate air temperature, creating thermal discomfort. ASHRAE Standard 55 incorporates MRT into operative temperature calculations:

**Tₒₚ = (Tₐ + Tₘᵣₜ) / 2** (for air velocities < 0.2 m/s)

## Low-Emissivity Surfaces and Radiant Barriers

Low-emissivity (low-e) surfaces reduce radiation heat transfer by reflecting rather than absorbing/emitting thermal radiation. Applications include:

**Glazing systems**: Low-e coatings (ε ≈ 0.04-0.20) on glass surfaces reduce radiative heat transfer while maintaining visible light transmission. Position within the insulated glazing unit determines whether the coating minimizes heat loss (surface 3, heating climates) or solar gain (surface 2, cooling climates).

**Radiant barriers**: Reflective materials (ε < 0.10) installed in attic spaces or wall cavities reduce summer heat gain. Effectiveness depends critically on adjacent air space—a low-e surface contacting insulation provides no radiant benefit. ASHRAE Fundamentals Chapter 27 quantifies radiant barrier R-values, which vary with heat flow direction, emissivity, and air space characteristics.

**Ductwork**: Reflective duct insulation with exterior low-e facing reduces radiative heat gain in unconditioned spaces, particularly attics where surrounding surface temperatures may reach 65-70°C (150-160°F).

## HVAC Applications

**Radiant Heating and Cooling Systems**: Operate primarily through radiation exchange between conditioned surfaces (floor, ceiling, walls) and occupants. Design requires careful attention to surface temperatures, mean radiant temperature distribution, and condensation risk for cooling applications. Panel surface temperatures typically range from 19-29°C (66-84°F) for cooling and 24-40°C (75-104°F) for heating, depending on system type and comfort requirements.

**Solar Heat Gain**: Represents a significant cooling load component in glazing-dominated buildings. Accurate calculation requires spectral properties of glazing systems, shading device analysis, and hourly solar position calculations. ASHRAE cooling load calculation methods (radiant time series, heat balance) account for the time lag between solar absorption and convective heat transfer to space air.

**Night Sky Radiation**: In arid climates with clear night skies, surfaces can radiate to the effective sky temperature (often 20-40 K below ambient air temperature), enabling radiative cooling strategies. This principle underlies both traditional architecture and emerging radiative cooling technologies.

**Thermal Bridging**: Building envelope discontinuities alter surface temperatures, creating localized radiation exchange patterns that affect both heat transfer and condensation risk. Accurate modeling requires two- or three-dimensional heat transfer analysis to capture these effects.

## Linearization for Engineering Calculations

For moderate temperature differences, radiation heat transfer can be linearized to simplify combined convection-radiation calculations:

**q = hᵣ·(T₁ - T₂)**

Where the radiation heat transfer coefficient:

**hᵣ = 4εσTₘ³** (Tₘ = mean absolute temperature)

This linearization enables direct summation with convection coefficients (hₜₒₜₐₗ = hc + hᵣ) for surface film calculations, as employed in ASHRAE steady-state R-value determinations and simplified load calculation methods. The approximation introduces less than 2% error for temperature differences below 30 K near room temperature conditions.
