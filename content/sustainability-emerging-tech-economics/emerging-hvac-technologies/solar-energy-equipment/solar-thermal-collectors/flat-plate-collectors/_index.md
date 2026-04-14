---
title: "Flat Plate Collectors"
aliases: ["Flat Plate Collectors"]
weight: 1
---

## Overview

Flat plate collectors represent the most common solar thermal collector technology for low-to-medium temperature applications (30-80°C). These devices convert solar radiation into thermal energy through absorption and transfer this energy to a heat transfer fluid for domestic water heating, space heating, and process applications.

## Collector Construction

### Basic Components

Flat plate collectors consist of five primary components arranged in layers:

1. **Transparent cover (glazing)** - Reduces convective and radiative heat losses
2. **Absorber plate** - Converts solar radiation to thermal energy
3. **Fluid channels** - Transport heat transfer fluid through or behind absorber
4. **Insulation** - Minimizes conductive heat losses from back and edges
5. **Enclosure (casing)** - Protects components and provides structural support

**Typical Construction Dimensions:**

| Parameter | Typical Range | Notes |
|-----------|---------------|-------|
| Collector length | 1.8-2.4 m | Standard modules |
| Collector width | 0.9-1.2 m | For handling |
| Total depth | 80-120 mm | Including casing |
| Gross area | 1.6-2.9 m² | Per module |
| Aperture area | 1.4-2.6 m² | Active absorption area |
| Weight (dry) | 25-45 kg/m² | Affects structural load |

### Absorber Plate Design

The absorber plate is the critical component that converts solar radiation into heat. Key design parameters:

**Material Selection:**

| Material | Thermal Conductivity | Density | Cost Factor | Applications |
|----------|---------------------|---------|-------------|--------------|
| Copper | 385 W/m·K | 8960 kg/m³ | High | Premium collectors |
| Aluminum | 205 W/m·K | 2700 kg/m³ | Medium | Standard collectors |
| Steel | 50 W/m·K | 7850 kg/m³ | Low | Low-cost applications |

**Absorber Plate Thickness:**
- Copper: 0.2-0.5 mm
- Aluminum: 0.4-0.8 mm
- Steel: 0.8-1.2 mm

**Tube Configuration:**

Parallel tube design dominates modern flat plate collectors:

- Tube spacing: 100-150 mm
- Tube diameter: 8-12 mm (internal)
- Number of tubes: 8-12 per collector
- Header diameter: 20-25 mm
- Bond width (tube-to-plate): 25-40 mm

The fin efficiency between tubes depends on the bond conductance and material properties:

**Fin Efficiency Equation:**

η_f = tanh(mL) / (mL)

Where:
- m = √(U_L / (k·δ))
- L = (W - D) / 2 (half the distance between tubes)
- U_L = Overall heat loss coefficient (W/m²·K)
- k = Thermal conductivity of absorber material (W/m·K)
- δ = Absorber plate thickness (m)
- W = Tube spacing (m)
- D = Tube outer diameter (m)

For optimized copper absorbers, fin efficiency typically ranges from 0.92-0.97.

## Selective Surface Coatings

Selective coatings maximize solar absorption (α) while minimizing thermal emittance (ε):

| Coating Type | Absorptance (α) | Emittance (ε) | α/ε Ratio | Durability | Cost |
|--------------|-----------------|---------------|-----------|------------|------|
| Black paint | 0.90-0.95 | 0.88-0.92 | 1.0-1.1 | Fair | Low |
| Black chrome | 0.92-0.96 | 0.09-0.15 | 6.4-10.7 | Good | Medium |
| Black nickel | 0.90-0.93 | 0.08-0.12 | 7.5-11.6 | Good | Medium |
| TiNOx (titanium oxide) | 0.94-0.96 | 0.04-0.06 | 15.7-24.0 | Excellent | High |
| Cermet coatings | 0.93-0.95 | 0.05-0.08 | 11.6-19.0 | Excellent | High |
| Aluminum-nitrogen | 0.92-0.95 | 0.03-0.05 | 18.4-31.7 | Excellent | High |

**Performance Impact:**

The selective surface reduces radiative heat loss (Q_rad):

Q_rad = ε·σ·A·(T_p⁴ - T_a⁴)

Where:
- ε = Emittance (dimensionless)
- σ = Stefan-Boltzmann constant (5.67×10⁻⁸ W/m²·K⁴)
- A = Absorber area (m²)
- T_p = Absorber plate temperature (K)
- T_a = Ambient temperature (K)

At an absorber temperature of 60°C (333 K) and ambient of 20°C (293 K), a selective coating with ε=0.05 reduces radiative losses by approximately 80-90% compared to black paint with ε=0.90.

## Glazing Systems

### Single vs. Double Glazing

**Single Glazing:**
- Transmittance (τ): 0.87-0.92 (low-iron glass)
- Heat loss coefficient contribution: 4-6 W/m²·K
- Weight: 10-12 kg/m² (4 mm thickness)
- Cost: Base reference
- Best for: Warm climates, moderate temperature applications

**Double Glazing:**
- Transmittance (τ): 0.77-0.84
- Heat loss coefficient contribution: 2-3 W/m²·K
- Weight: 20-24 kg/m² (two 4 mm panes)
- Cost: 1.4-1.6× single glazing
- Best for: Cold climates, high temperature applications

**Material Properties:**

| Glass Type | Solar Transmittance | Iron Content | Typical Thickness | Cost Factor |
|------------|---------------------|--------------|-------------------|-------------|
| Standard float | 0.84-0.87 | 0.1% Fe₂O₃ | 3-4 mm | 1.0 |
| Low-iron (water white) | 0.90-0.92 | 0.015% Fe₂O₃ | 3-4 mm | 1.3-1.5 |
| Tempered low-iron | 0.89-0.91 | 0.015% Fe₂O₃ | 3-4 mm | 1.5-1.8 |
| Anti-reflective coated | 0.94-0.96 | 0.015% Fe₂O₃ | 3-4 mm | 2.0-2.5 |

**Air Gap Spacing:**
- Single glazing to absorber: 25-40 mm
- Between double glazing panes: 12-20 mm

## Insulation Systems

Insulation minimizes conductive heat losses from the collector back and edges.

**Back Insulation:**

| Material | Thermal Conductivity | Density | Max Temperature | Thickness |
|----------|---------------------|---------|-----------------|-----------|
| Mineral wool | 0.035-0.040 W/m·K | 30-60 kg/m³ | 250°C | 50-80 mm |
| Polyurethane foam | 0.022-0.028 W/m·K | 30-50 kg/m³ | 110°C | 40-60 mm |
| Polyisocyanurate | 0.020-0.026 W/m·K | 30-40 kg/m³ | 150°C | 40-60 mm |
| Glass fiber | 0.032-0.038 W/m·K | 10-30 kg/m³ | 250°C | 50-80 mm |

**Edge Insulation:**
- Thickness: 20-30 mm
- Must prevent thermal bridging
- Typically same material as back insulation

**Conductive Heat Loss:**

Q_cond = U_back·A·(T_p - T_a)

Where U_back = k_insulation / thickness

For 60 mm polyurethane foam (k=0.025 W/m·K):
U_back = 0.025 / 0.060 = 0.42 W/m²·K

## Collector Efficiency

### Efficiency Equation

The instantaneous thermal efficiency of a flat plate collector is:

η = Q_useful / (G_T · A_c)

Where:
- Q_useful = Useful heat gain (W)
- G_T = Total solar irradiance on collector plane (W/m²)
- A_c = Collector gross or aperture area (m²)

**Modified Hottel-Whillier-Bliss Equation:**

η = F_R(τα) - F_R·U_L·(T_i - T_a) / G_T

Where:
- F_R = Heat removal factor (dimensionless, typically 0.85-0.95)
- (τα) = Transmittance-absorptance product (dimensionless)
- U_L = Overall heat loss coefficient (W/m²·K)
- T_i = Collector inlet fluid temperature (°C or K)
- T_a = Ambient air temperature (°C or K)

**Typical Performance Parameters:**

| Collector Type | F_R(τα) | F_R·U_L | Efficiency at ΔT/G_T=0.03 |
|----------------|---------|---------|---------------------------|
| Unglazed | 0.82-0.86 | 15-25 W/m²·K | 0.07-0.11 |
| Single glazed, black paint | 0.72-0.78 | 6-8 W/m²·K | 0.54-0.62 |
| Single glazed, selective | 0.70-0.76 | 3.5-5.0 W/m²·K | 0.60-0.68 |
| Double glazed, selective | 0.62-0.68 | 2.5-3.5 W/m²·K | 0.54-0.61 |

### Heat Loss Coefficient Components

The overall heat loss coefficient U_L consists of top, back, and edge losses:

U_L = U_top + U_back + U_edge

**Top Heat Loss (U_top):**

Includes convective and radiative losses from absorber to glazing and glazing to ambient:

U_top = [1/(h_c,p-c + h_r,p-c) + 1/(h_c,c-a + h_r,c-a)]^(-1)

Where:
- h_c,p-c = Convection coefficient, plate to cover (2-4 W/m²·K)
- h_r,p-c = Radiation coefficient, plate to cover (4-6 W/m²·K)
- h_c,c-a = Convection coefficient, cover to ambient (10-25 W/m²·K, wind dependent)
- h_r,c-a = Radiation coefficient, cover to sky (4-6 W/m²·K)

For a typical single-glazed selective surface collector: U_top = 3.5-5.0 W/m²·K

**Back Heat Loss (U_back):**

U_back = k_insulation / L_insulation

For 60 mm polyurethane (k=0.025 W/m·K): U_back = 0.42 W/m²·K

**Edge Heat Loss (U_edge):**

U_edge = (U_edge,perimeter · Perimeter · L_edge) / A_collector

Typically: U_edge = 0.1-0.3 W/m²·K

## Collector Tilt and Orientation

### Optimal Tilt Angle

For maximum annual energy collection, the optimal tilt angle β depends on latitude (φ):

**General Guidelines:**
- Year-round applications: β = φ (latitude)
- Summer optimization: β = φ - 15°
- Winter optimization: β = φ + 15°
- Space heating emphasis: β = φ + 10° to φ + 20°

**Seasonal Adjustment:**

The solar altitude angle at solar noon affects the optimal tilt:

α_noon = 90° - φ + δ

Where:
- α = Solar altitude angle
- φ = Latitude
- δ = Declination angle (-23.45° to +23.45°)

### Azimuth Orientation

**Performance Impact:**

| Azimuth Deviation | Annual Energy Reduction |
|-------------------|------------------------|
| 0° (due south in N. hemisphere) | 0% (baseline) |
| ±15° | 2-3% |
| ±30° | 8-12% |
| ±45° | 18-25% |
| ±60° | 30-40% |

## Stagnation Temperature

The maximum temperature reached under no-flow conditions:

T_stagnation = T_a + (G_T · F_R(τα)) / (F_R · U_L)

**Typical Stagnation Temperatures:**

| Collector Type | Stagnation Temperature |
|----------------|------------------------|
| Unglazed | 40-60°C |
| Single glazed, black paint | 120-140°C |
| Single glazed, selective | 150-180°C |
| Double glazed, selective | 180-220°C |
| Evacuated tube | 250-300°C |

**Design Implications:**
- Material selection must withstand stagnation temperatures
- Glycol degradation above 180°C
- Pressure relief valves required
- Thermal expansion accommodation needed

## Applications

**Domestic Water Heating:**
- Target temperature: 50-60°C
- Collector type: Single glazed, selective surface
- Typical area: 4-6 m² per household
- Annual solar fraction: 50-70% (climate dependent)

**Space Heating:**
- Target temperature: 35-50°C
- Collector type: Single or double glazed, selective
- Typical area: 0.15-0.25 m² per m² floor area
- Annual solar fraction: 20-40%

**Pool Heating:**
- Target temperature: 26-30°C
- Collector type: Unglazed (low cost)
- Typical area: 50-100% of pool surface area
- Annual solar fraction: 60-80%

**Process Heat (low temperature):**
- Target temperature: 60-90°C
- Collector type: Double glazed, selective surface
- Area: Application specific
- Annual solar fraction: 30-50%

## Performance Metrics

**Energy Output Estimation:**

Annual energy per unit area:

E_annual = Σ(η · G_T · Δt)

For a typical installation (40° N latitude, south-facing, 45° tilt):
- Annual irradiation: 1600-1900 kWh/m²
- System efficiency: 35-45%
- Annual energy output: 560-855 kWh/m²

**Economic Performance:**

| Metric | Typical Range |
|--------|---------------|
| Installed cost | $400-800/m² |
| Lifetime | 20-30 years |
| Annual maintenance | 1-2% of initial cost |
| Simple payback | 5-15 years |
| Levelized cost of heat | $0.04-0.12/kWh |
