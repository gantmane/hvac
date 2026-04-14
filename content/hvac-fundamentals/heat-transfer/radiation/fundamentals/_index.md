---
title: "Fundamentals"
aliases: ["Fundamentals"]
weight: 1
---

Thermal radiation is electromagnetic energy emitted by matter at finite temperature. All surfaces above absolute zero emit thermal radiation across a continuous spectrum of wavelengths. Understanding radiation fundamentals is essential for HVAC applications including radiant heating, solar load calculations, and building envelope analysis.

## Electromagnetic Spectrum

Thermal radiation occupies the portion of the electromagnetic spectrum from approximately 0.1 to 100 μm. The thermal radiation spectrum subdivides into three regions:

| Region | Wavelength Range | Percentage at 300K | Percentage at 1000K |
|--------|------------------|-------------------|---------------------|
| Ultraviolet (UV) | 0.1 - 0.4 μm | ~0% | <1% |
| Visible | 0.4 - 0.7 μm | ~0% | ~10% |
| Infrared (IR) | 0.7 - 100 μm | ~100% | ~90% |

For HVAC applications at typical building temperatures (250-350K), thermal radiation occurs almost entirely in the infrared region.

## Blackbody Radiation

A blackbody is an ideal surface that:
- Absorbs all incident radiation regardless of wavelength and direction
- Emits the maximum possible radiation at any given temperature
- Has emissivity ε = 1 and absorptivity α = 1

No real surface is a perfect blackbody, but the blackbody represents the upper limit for thermal radiation emission.

## Planck's Law

Planck's law describes the spectral distribution of radiation emitted by a blackbody:

**E_λ,b(λ,T) = (C₁) / [λ⁵(e^(C₂/λT) - 1)]**

Where:
- E_λ,b = spectral emissive power of blackbody, W/(m²·μm)
- λ = wavelength, μm
- T = absolute temperature, K
- C₁ = 3.742 × 10⁸ W·μm⁴/m² (first radiation constant)
- C₂ = 1.439 × 10⁴ μm·K (second radiation constant)

Key observations from Planck's law:
- At any wavelength, emissive power increases with temperature
- As temperature increases, the peak emission shifts to shorter wavelengths
- The area under the curve represents total emissive power

## Wien's Displacement Law

Wien's displacement law determines the wavelength at which maximum spectral emissive power occurs:

**λ_max·T = 2897.8 μm·K**

Applications:

| Temperature | λ_max | Primary Region |
|-------------|-------|----------------|
| 300K (80°F) | 9.66 μm | Far infrared |
| 373K (212°F) | 7.77 μm | Mid infrared |
| 1000K (1340°F) | 2.90 μm | Near infrared |
| 5800K (sun) | 0.50 μm | Visible (green) |

This relationship explains why room temperature surfaces emit infrared radiation while the sun emits primarily visible light.

## Stefan-Boltzmann Law

The Stefan-Boltzmann law calculates total emissive power from a blackbody by integrating Planck's law over all wavelengths:

**E_b(T) = σT⁴**

Where:
- E_b = total hemispherical emissive power, W/m²
- σ = 5.670 × 10⁻⁸ W/(m²·K⁴) (Stefan-Boltzmann constant)
- T = absolute temperature, K

For real surfaces with emissivity ε:

**E(T) = εσT⁴**

The total radiation emitted is proportional to the fourth power of absolute temperature, making radiation heat transfer highly sensitive to temperature changes.

## Radiative Properties

### Emissivity (ε)

Emissivity is the ratio of radiation emitted by a real surface to that emitted by a blackbody at the same temperature:

**ε = E(T) / E_b(T)**

Emissivity ranges from 0 to 1, where:
- ε = 1: Perfect blackbody
- ε = 0: Perfect reflector (no emission)

### Absorptivity (α)

Absorptivity is the fraction of incident radiation absorbed by a surface:

**α = G_absorbed / G_incident**

Where:
- G_absorbed = absorbed irradiation, W/m²
- G_incident = incident irradiation, W/m²

### Reflectivity (ρ)

Reflectivity is the fraction of incident radiation reflected by a surface:

**ρ = G_reflected / G_incident**

### Transmissivity (τ)

Transmissivity is the fraction of incident radiation transmitted through a surface:

**τ = G_transmitted / G_incident**

### Energy Balance

For an opaque surface (τ = 0):

**α + ρ = 1**

For a semitransparent surface:

**α + ρ + τ = 1**

## Kirchhoff's Law

Kirchhoff's law states that for a surface in thermal equilibrium:

**ε_λ(λ,T,θ,φ) = α_λ(λ,T,θ,φ)**

In words: spectral, directional emissivity equals spectral, directional absorptivity at the same wavelength, temperature, and direction.

For diffuse, gray surfaces at thermal equilibrium:

**ε = α**

This simplification is commonly applied in HVAC calculations when:
- Surface temperature ≈ source temperature (within ~100K)
- Surface properties do not vary strongly with wavelength
- Directional effects are negligible

## Emissivity Values for Common Building Materials

| Material | Temperature (°F) | Emissivity ε |
|----------|------------------|--------------|
| Aluminum, polished | 70 | 0.04 - 0.06 |
| Aluminum, oxidized | 70 | 0.11 - 0.19 |
| Aluminum paint | 70 | 0.27 - 0.67 |
| Asphalt pavement | 70 | 0.85 - 0.93 |
| Brick, red common | 70 | 0.93 - 0.96 |
| Concrete, rough | 70 | 0.94 - 0.97 |
| Copper, polished | 70 | 0.04 - 0.05 |
| Copper, oxidized | 70 | 0.65 - 0.75 |
| Glass, window | 70 | 0.90 - 0.95 |
| Gypsum board | 70 | 0.90 - 0.92 |
| Paint, white | 70 | 0.90 - 0.95 |
| Paint, black | 70 | 0.95 - 0.98 |
| Plaster | 70 | 0.91 - 0.94 |
| Stainless steel, polished | 70 | 0.07 - 0.17 |
| Stainless steel, oxidized | 70 | 0.85 - 0.90 |
| Wood, oak planed | 70 | 0.90 - 0.92 |

Key observations:
- Polished metals: very low emissivity (0.04-0.10)
- Oxidized metals: moderate to high emissivity (0.20-0.90)
- Non-metallic building materials: high emissivity (0.85-0.97)
- Surface finish significantly affects metal emissivity

## Spectral vs. Total Properties

**Spectral properties** vary with wavelength:
- ε_λ(λ): spectral emissivity
- α_λ(λ): spectral absorptivity

**Total properties** are integrated over all wavelengths:
- ε: total hemispherical emissivity
- α: total hemispherical absorptivity

A **gray surface** has constant spectral properties (ε_λ = constant). Most non-metallic building materials approximate gray behavior in the thermal infrared spectrum.

## Directional vs. Hemispherical Properties

**Directional properties** depend on emission/incidence angle (θ, φ):
- ε(θ,φ): directional emissivity
- α(θ,φ): directional absorptivity

**Hemispherical properties** are integrated over all directions:
- ε: hemispherical emissivity
- α: hemispherical absorptivity

A **diffuse surface** has constant directional properties. HVAC calculations typically assume diffuse surfaces unless dealing with specular reflections from polished metals or glass.

## Graybody Approximation

A graybody is a real surface with:
- ε < 1 (emissivity less than blackbody)
- ε_λ = constant (spectral emissivity independent of wavelength)
- ε(θ) = constant (emissivity independent of direction)

For graybody surfaces:

**E = εσT⁴**

**α = ε** (when Kirchhoff's law applies)

Most building materials can be treated as graybodies for HVAC radiation calculations.

## Engineering Applications

**Radiant heating systems**: Stefan-Boltzmann law determines heat output from radiant panels or surfaces.

**Solar heat gain**: Absorptivity determines how much solar radiation is absorbed by building surfaces and converted to heat.

**Low-emissivity coatings**: Low-e windows use thin metallic coatings (ε ≈ 0.10-0.20) to reduce radiative heat transfer while maintaining visible light transmission.

**Thermal comfort**: Mean radiant temperature calculations require emissivity values for surrounding surfaces.

**Building envelope**: Radiative properties affect heat transfer through walls, roofs, and windows.

## Calculation Example

Calculate the radiation emitted by a concrete floor at 75°F (297K) with emissivity ε = 0.95:

**E = εσT⁴**
**E = 0.95 × 5.67×10⁻⁸ × (297)⁴**
**E = 0.95 × 5.67×10⁻⁸ × 7.78×10⁹**
**E = 419 W/m² (133 Btu/h·ft²)**

For comparison, a blackbody at the same temperature emits:

**E_b = σT⁴ = 441 W/m² (140 Btu/h·ft²)**

The concrete floor emits 95% of blackbody radiation at this temperature.
