---
title: "Gas Radiation"
aliases: ["Gas Radiation"]
weight: 4
---

Gas radiation governs energy transfer in combustion systems, furnaces, boilers, and high-temperature processes. Unlike solid surfaces that emit and absorb radiation across continuous wavelength spectra, gases radiate and absorb only at specific wavelength bands corresponding to molecular vibration and rotation modes.

## Participating Media

Participating media are gases that emit, absorb, and scatter thermal radiation as it passes through them.

**Radiatively Active Gases:**
- Carbon dioxide (CO₂)
- Water vapor (H₂O)
- Carbon monoxide (CO)
- Sulfur dioxide (SO₂)
- Ammonia (NH₃)
- Methane (CH₄)

**Non-Participating Gases:**
- Nitrogen (N₂)
- Oxygen (O₂)
- Argon (Ar)
- Helium (He)

These monatomic and homonuclear diatomic molecules possess no permanent dipole moment and do not absorb or emit thermal radiation at typical combustion temperatures.

The participating medium emits radiation at every point within its volume. The local volumetric emission rate depends on temperature and gas composition. As radiation travels through the gas, it is continuously absorbed and re-emitted, creating a complex radiation field.

## Gas Absorption Bands

Gases absorb and emit radiation in discrete wavelength bands, not continuously. These bands result from quantum transitions between molecular energy states.

**CO₂ Absorption Bands:**
- 2.7 μm (strong)
- 4.3 μm (very strong)
- 15 μm (strong)

**H₂O Absorption Bands:**
- 2.7 μm (strong)
- 6.3 μm (very strong)
- Beyond 12 μm (rotation bands)

The band intensity depends on the product of partial pressure and path length (pL), where p is partial pressure in atmospheres and L is the beam length in meters or feet.

## Gas Emissivity and Absorptivity

Gas emissivity ε_g quantifies the ability of a gas volume to emit radiation relative to a blackbody at the same temperature. Unlike solid surfaces where emissivity is primarily temperature-dependent, gas emissivity depends on:

1. **Temperature (T_g)** - Gas absolute temperature
2. **Partial pressure (p)** - Partial pressure of the radiating species
3. **Beam length (L)** - Mean path length through the gas
4. **Product pL** - Primary correlating parameter

The gas emissivity is determined from empirical correlations based on spectroscopic measurements.

## CO₂ Radiation

Carbon dioxide emissivity depends on the product p_CO₂·L and gas temperature.

**Emissivity determination:**
1. Calculate p_CO₂·L product (atm·m or atm·ft)
2. Determine gas temperature T_g
3. Use Hottel charts or correlations to find ε_CO₂

**Correction for total pressure:**
The emissivity charts are based on CO₂ in a mixture at atmospheric pressure. For other total pressures P_t, apply a correction:

C_CO₂ = (P_t + p_CO₂)/(2p_CO₂)

Corrected product: (p_CO₂·L)_corrected = p_CO₂·L × C_CO₂

## H₂O Vapor Radiation

Water vapor possesses stronger radiation characteristics than CO₂ at typical combustion temperatures due to its broader absorption bands.

**Emissivity determination:**
1. Calculate p_H₂O·L product (atm·m or atm·ft)
2. Determine gas temperature T_g
3. Use Hottel charts or correlations to find ε_H₂O

**Correction for total pressure and partial pressure:**
For water vapor, the pressure correction is:

C_H₂O = [(P_t + p_H₂O)/2]^0.5 / [(1 + p_H₂O)]^0.5

This correction accounts for pressure broadening of the spectral lines.

## Gas Mixture Radiation

When both CO₂ and H₂O are present (typical in combustion products), their combined emissivity is not simply additive because of spectral overlap in the 2.7 μm band.

**Mixture emissivity:**

ε_g = ε_CO₂ + ε_H₂O - Δε

where:
- ε_CO₂ = emissivity of CO₂ alone (corrected for pressure)
- ε_H₂O = emissivity of H₂O alone (corrected for pressure)
- Δε = correction factor for band overlap

The correction factor Δε is determined from charts as a function of:
- p_H₂O/(p_CO₂ + p_H₂O) ratio
- (p_CO₂ + p_H₂O)·L product
- Gas temperature

Typical values of Δε range from 0.01 to 0.05 for combustion gases.

## Mean Beam Length

The mean beam length L is the characteristic path length that accounts for the geometry of the gas volume radiating to a surface. It represents the radius of a hemisphere of gas that would exchange the same radiation with a surface element at its base as the actual geometry.

**Common geometries:**

| Geometry | Mean Beam Length (L) |
|----------|---------------------|
| Sphere radiating to surface | 0.65 × diameter |
| Infinite cylinder to curved surface | 0.95 × diameter |
| Infinite cylinder to base | 0.65 × diameter |
| Semi-infinite cylinder to base | 0.90 × diameter |
| Infinite slab to surface | 1.8 × slab thickness |
| Cube to face | 0.66 × side length |
| Rectangular parallelepiped (1:1:4) | 0.9 × shortest side |

**General formula for arbitrary volumes:**

L = 3.6 × V/A

where:
- V = gas volume (m³ or ft³)
- A = surface area of enclosure (m² or ft²)

This approximation works reasonably well for compact geometries. For highly elongated shapes, use specific correlations.

## Hottel Charts

Hottel charts are empirical graphical representations of gas emissivity based on experimental spectroscopic data compiled by H.C. Hottel and others.

**Chart usage procedure:**

1. **Calculate partial pressure:** Determine p_CO₂ and p_H₂O from combustion stoichiometry or gas analysis
2. **Determine mean beam length:** Calculate L based on geometry
3. **Find individual emissivities:**
   - For CO₂: Enter chart with p_CO₂·L and T_g to get ε_CO₂ at 1 atm total pressure
   - For H₂O: Enter chart with p_H₂O·L and T_g to get ε_H₂O at 1 atm total pressure
4. **Apply pressure corrections:** Multiply by C_CO₂ and C_H₂O as needed
5. **Account for overlap:** Subtract Δε from sum
6. **Calculate mixture emissivity:** ε_g = ε_CO₂ + ε_H₂O - Δε

**Absorptivity determination:**

When gas absorbs radiation from a surface at temperature T_s (different from gas temperature T_g):

α_CO₂ = ε_CO₂(T_s) × (T_g/T_s)^0.65

α_H₂O = ε_H₂O(T_s) × (T_g/T_s)^0.45

The temperature ratio accounts for the shift in spectral distribution between the emitting surface and absorbing gas.

## Combustion Gas Radiation

In combustion systems, the products of complete combustion typically contain CO₂, H₂O, N₂, and excess O₂. The radiative properties are dominated by CO₂ and H₂O.

**Typical combustion gas compositions (dry basis):**

| Fuel | CO₂ (%) | H₂O (%) | N₂ (%) | O₂ (%) |
|------|---------|---------|--------|--------|
| Natural gas | 8-10 | 16-20 | 70-74 | 2-4 |
| Fuel oil | 11-13 | 10-12 | 73-76 | 2-4 |
| Coal | 14-16 | 6-8 | 74-78 | 2-4 |

**Heat transfer from gas to surface:**

The net radiative heat flux from hot combustion gas at temperature T_g to a cooler surface at temperature T_s is:

q = σ × A × [ε_g × T_g⁴ - α_g × T_s⁴]

where:
- σ = Stefan-Boltzmann constant = 5.67×10⁻⁸ W/(m²·K⁴)
- A = surface area (m²)
- ε_g = gas emissivity at T_g
- α_g = gas absorptivity for radiation from surface at T_s

**Alternative formulation:**

q = σ × A × ε_g × (T_g⁴ - τ_g × T_s⁴)

where τ_g is the gas transmissivity. For gray gas assumption: τ_g ≈ 1 - ε_g

## Furnace Analysis

Furnace heat transfer involves combined radiation from hot combustion gases and refractory walls to the heat-absorbing surfaces (tubes, stock, etc.).

**Zone method energy balance:**

The furnace is divided into gas and surface zones. For a simple furnace with uniform gas temperature:

**Heat absorbed by surface:**

q = A_s × [ε_eff × σ × (T_g⁴ - T_s⁴)]

where ε_eff is an effective emissivity accounting for gas radiation, refractory reflection, and surface properties:

ε_eff = [ε_g + ε_r × τ_g × (1 - ε_s)] / [1 - ρ_s × ρ_r × τ_g²]

where:
- ε_g = gas emissivity
- ε_r = refractory emissivity (typically 0.7-0.9)
- ε_s = surface (tube) emissivity
- τ_g = gas transmissivity ≈ 1 - ε_g
- ρ_s = surface reflectivity = 1 - ε_s - α_s ≈ 1 - ε_s (for opaque surfaces)
- ρ_r = refractory reflectivity = 1 - ε_r

**Simplified approach:**

For preliminary calculations with well-mixed furnace gases:

q/A = σ × F × (T_g⁴ - T_s⁴)

where F is an interchange factor:

F = 1 / [(1/ε_g) + (1/ε_s) - 1]

This treats the gas volume as a gray surface exchanging radiation with the absorbing surface.

**Radiant section efficiency:**

The fraction of fuel energy released that is absorbed by radiant section tubes:

η_radiant = q_absorbed / (ṁ_fuel × LHV)

Typical values range from 0.50 to 0.70 for well-designed fired heaters and boilers.

**Practical considerations:**

1. **Gas temperature distribution:** Real furnaces exhibit temperature gradients requiring zone-by-zone analysis
2. **Soot and particulates:** Increase gas emissivity significantly; soot can raise ε_g from 0.3 to 0.8
3. **Flame radiation:** Luminous flames radiate more intensely than calculated from gas emissivity alone
4. **Tube arrangement:** Affects view factors and heat flux distribution
5. **Fouling:** Reduces surface absorptivity and increases thermal resistance

**Weighted sum of gray gases (WSGG) model:**

Modern CFD analysis uses the WSGG model to account for non-gray gas behavior:

ε_g = Σ a_i(T) × [1 - exp(-κ_i × p × L)]

where:
- a_i(T) = temperature-dependent weighting factors
- κ_i = absorption coefficient for gray gas i
- Sum typically includes 3-4 gray gases plus one transparent gas

This approach provides better accuracy than single-value emissivity methods, particularly for large temperature differences between gas and surfaces.

## Practical Applications

**Boiler design:**
- Radiant section heat absorption determines required furnace volume
- Furnace exit gas temperature (FEGT) affects convection section performance
- Water wall tube spacing balances heat flux uniformity and furnace volume

**Industrial furnaces:**
- Steel reheat furnaces: gas emissivity 0.25-0.35 (clean natural gas)
- Glass melting tanks: gas emissivity 0.15-0.25 (oxy-fuel combustion)
- Ceramic kilns: gas emissivity 0.30-0.40 (with combustion products)

**Calculation sequence:**

1. Determine fuel composition and firing rate
2. Calculate stoichiometric combustion products
3. Establish gas temperature (from energy balance or measurement)
4. Calculate partial pressures of CO₂ and H₂O
5. Determine furnace geometry and mean beam length
6. Find gas emissivity from charts or correlations
7. Calculate absorptivity at surface temperature
8. Determine heat transfer rate using appropriate model
9. Verify energy balance and iterate if necessary
