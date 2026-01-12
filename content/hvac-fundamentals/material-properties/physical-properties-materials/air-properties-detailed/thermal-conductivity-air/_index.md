---
title: "Thermal Conductivity of Air"
description: "Comprehensive analysis of air thermal conductivity including temperature relationships, kinetic theory principles, property tables, and HVAC design applications for insulation, heat transfer calculations, and boundary layer analysis."
weight: 4
---

## Overview

Thermal conductivity of air quantifies the rate of heat transfer through air by molecular conduction. This fundamental transport property governs convective heat transfer coefficients, insulation effectiveness, and boundary layer behavior in HVAC systems. Air's low thermal conductivity (k = 0.0257 W/m·K at 20°C) makes it an effective insulating medium when trapped in small cavities, explaining the effectiveness of fibrous insulation, double-pane windows, and air gaps in building envelopes.

Understanding air thermal conductivity is essential for:
- Calculating convective heat transfer coefficients
- Designing insulation systems with air-filled cavities
- Analyzing boundary layer thermal resistance
- Modeling free and forced convection processes
- Evaluating window and wall assembly thermal performance
- Predicting condensation potential in building cavities

## Physical Principles and Kinetic Theory

### Molecular Transport Mechanism

Thermal conductivity in gases results from molecular energy transport through random molecular motion and collisions. Unlike liquids and solids where intermolecular forces dominate, gas thermal conductivity derives primarily from kinetic energy transfer during molecular collisions.

The kinetic theory of gases relates thermal conductivity to molecular properties:

**Chapman-Enskog Equation (Dilute Gases):**

k = (5/16) × (√(πmkᵦT) / πd²) × (kᵦ / m)

Where:
- k = thermal conductivity (W/m·K)
- m = molecular mass (kg)
- kᵦ = Boltzmann constant = 1.381 × 10⁻²³ J/K
- T = absolute temperature (K)
- d = molecular collision diameter (m)

This relationship predicts that thermal conductivity is independent of pressure (for ideal gases) and increases with the square root of absolute temperature.

### Temperature Dependence

For air, thermal conductivity increases approximately linearly with temperature over typical HVAC operating ranges (-40°C to +100°C):

**Empirical Correlation (Standard Atmospheric Pressure):**

k(T) = k₀ × (T/T₀)ⁿ

Where:
- k₀ = 0.0257 W/m·K (reference at T₀ = 293 K or 20°C)
- n ≈ 0.8 to 1.0 for air (typically 0.85)
- T = absolute temperature (K)

**Simplified Linear Approximation:**

k(T) = 0.0224 + 7.5 × 10⁻⁵ × T_c

Where:
- T_c = temperature (°C)
- Valid range: -50°C to +100°C
- Error: ±2% within specified range

### Pressure Effects

For ideal gas behavior (pressures below 10 atm), thermal conductivity is essentially independent of pressure. This independence occurs because increased molecular density at higher pressure is offset by reduced mean free path between collisions.

**Pressure Independence Criterion:**

k(P) ≈ k(P₀) for P < 10 atm

At very low pressures (vacuum conditions, P < 0.1 Pa), molecular mean free path becomes comparable to container dimensions, and thermal conductivity decreases with pressure—the principle behind vacuum insulation panels.

### Humidity Effects

Water vapor has higher thermal conductivity than dry air (k_H₂O ≈ 0.0186 W/m·K at 20°C as vapor). Moist air thermal conductivity:

**Mixture Rule:**

k_mixture = x_dry × k_dry + x_H₂O × k_H₂O

Where:
- x = mole fraction
- Typical increase: 1-3% for saturated air vs. dry air at 20°C

For most HVAC calculations, humidity effects on thermal conductivity are negligible and can be ignored.

## Property Tables

### Thermal Conductivity at Standard Atmospheric Pressure

| Temperature | Thermal Conductivity | Prandtl Number | Thermal Diffusivity |
|-------------|---------------------|----------------|---------------------|
| °C (°F) | W/m·K (BTU/h·ft·°F) | Pr | α (m²/s × 10⁶) |
|-------------|---------------------|----------------|---------------------|
| -40 (-40) | 0.0209 (0.0121) | 0.728 | 14.9 |
| -30 (-22) | 0.0217 (0.0125) | 0.726 | 15.8 |
| -20 (-4) | 0.0224 (0.0129) | 0.724 | 16.7 |
| -10 (14) | 0.0231 (0.0134) | 0.722 | 17.6 |
| 0 (32) | 0.0238 (0.0138) | 0.720 | 18.6 |
| 10 (50) | 0.0246 (0.0142) | 0.718 | 19.6 |
| 20 (68) | 0.0257 (0.0149) | 0.715 | 21.0 |
| 30 (86) | 0.0267 (0.0154) | 0.713 | 22.4 |
| 40 (104) | 0.0276 (0.0159) | 0.711 | 23.7 |
| 50 (122) | 0.0285 (0.0165) | 0.709 | 25.1 |
| 60 (140) | 0.0294 (0.0170) | 0.708 | 26.5 |
| 70 (158) | 0.0303 (0.0175) | 0.706 | 27.9 |
| 80 (176) | 0.0312 (0.0180) | 0.705 | 29.3 |
| 90 (194) | 0.0321 (0.0186) | 0.704 | 30.7 |
| 100 (212) | 0.0330 (0.0191) | 0.703 | 32.1 |

**Reference Standard:** Properties based on dry air at 101.325 kPa (1 atm) per ASHRAE Handbook—Fundamentals.

### Extended Temperature Range Data

| Temperature | k (W/m·K) | Temperature | k (W/m·K) |
|-------------|-----------|-------------|-----------|
| -50°C | 0.0204 | 150°C | 0.0371 |
| -25°C | 0.0220 | 200°C | 0.0409 |
| 25°C | 0.0262 | 250°C | 0.0445 |
| 75°C | 0.0308 | 300°C | 0.0480 |

### Comparative Thermal Conductivities (20°C)

| Material/Gas | k (W/m·K) | Relative to Air |
|--------------|-----------|-----------------|
| Air (dry) | 0.0257 | 1.0 |
| Nitrogen (N₂) | 0.0259 | 1.01 |
| Oxygen (O₂) | 0.0265 | 1.03 |
| Carbon dioxide (CO₂) | 0.0166 | 0.65 |
| Argon (Ar) | 0.0177 | 0.69 |
| Helium (He) | 0.152 | 5.9 |
| Hydrogen (H₂) | 0.182 | 7.1 |
| Water vapor (H₂O) | 0.0186 | 0.72 |
| Krypton (Kr) | 0.0095 | 0.37 |
| Xenon (Xe) | 0.0057 | 0.22 |

## Engineering Calculations and Applications

### Convective Heat Transfer Coefficient

Thermal conductivity appears directly in dimensionless heat transfer correlations. The Nusselt number relates convective heat transfer coefficient to thermal conductivity:

**Nusselt Number Definition:**

Nu = h × L / k

Where:
- Nu = Nusselt number (dimensionless)
- h = convective heat transfer coefficient (W/m²·K)
- L = characteristic length (m)
- k = thermal conductivity of fluid (W/m·K)

**Solving for Convection Coefficient:**

h = Nu × k / L

For forced convection over a flat plate (laminar flow):

Nu_x = 0.332 × Re_x^0.5 × Pr^(1/3)

Where:
- Re_x = Reynolds number at position x
- Pr = Prandtl number

### Boundary Layer Thermal Resistance

The thermal boundary layer at solid surfaces provides thermal resistance:

**Thermal Boundary Layer Thickness (Laminar Flow):**

δ_T = δ / Pr^(1/3)

Where:
- δ_T = thermal boundary layer thickness (m)
- δ = velocity boundary layer thickness (m)
- Pr = Prandtl number ≈ 0.71 for air

**Conductive Resistance in Boundary Layer:**

R_boundary = δ_T / k

This relationship explains why even stagnant air films provide measurable thermal resistance at building surfaces.

### Still Air Surface Resistance

Building heat transfer calculations use surface film coefficients that depend on air thermal conductivity and natural convection patterns:

**Standard Surface Resistances (ASHRAE):**

| Surface Orientation | Film Coefficient h | Thermal Resistance R |
|---------------------|-------------------|---------------------|
| Horizontal, heat flow up | 9.26 W/m²·K | 0.108 m²·K/W |
| Vertical surface | 8.29 W/m²·K | 0.121 m²·K/W |
| Horizontal, heat flow down | 6.13 W/m²·K | 0.163 m²·K/W |
| Interior (still air) | 8.3 W/m²·K | 0.12 m²·K/W |
| Exterior (15 mph wind) | 34.0 W/m²·K | 0.03 m²·K/W |

**IP Units:**

Interior surface: R = 0.68 h·ft²·°F/BTU
Exterior surface: R = 0.17 h·ft²·°F/BTU

### Insulation Air Space Calculations

Thermal resistance of enclosed air spaces depends on air thermal conductivity, space thickness, surface emissivities, and orientation:

**Total Air Space Resistance:**

1/R_total = 1/R_radiation + 1/R_convection + 1/R_conduction

**Conductive Component:**

R_conduction = L / k

Where L = air space thickness

For thin air spaces (L < 20 mm), conduction dominates. For thicker spaces, convection currents reduce effective resistance.

**Effective Thermal Conductivity (with convection):**

k_eff = k × Nu

Where Nu > 1 when convection occurs.

### Optimal Air Gap Thickness

For vertical air spaces in wall cavities:

| Air Gap Thickness | Effective R-Value | Mechanism |
|-------------------|-------------------|-----------|
| 0-10 mm | Increases with thickness | Pure conduction |
| 10-20 mm | Maximum resistance | Conduction dominant |
| 20-40 mm | Slightly decreases | Convection begins |
| >40 mm | Significantly reduced | Full convection |

Optimal thickness for maximum R-value: approximately 19-25 mm (0.75-1.0 inch) for vertical cavities.

## HVAC System Applications

### Double-Pane Window Performance

Air-filled window cavities leverage low air thermal conductivity:

**Center-of-Glass U-Factor Components:**

U_total = 1 / (R_glass1 + R_airspace + R_glass2)

For 12 mm air space at 20°C mean temperature:
- R_airspace ≈ 0.16 m²·K/W (without low-e coating)
- R_airspace ≈ 0.30 m²·K/W (with low-e coating, ε = 0.1)

Replacing air with argon (k = 0.0177 W/m·K) improves performance:
- Argon R_airspace ≈ 0.19 m²·K/W (without low-e)
- 19% improvement over air

### Fibrous Insulation Performance

Fiberglass and mineral wool insulations trap air in small cells to minimize convection while leveraging air's low thermal conductivity:

**Effective Conductivity Model:**

k_eff = φ × k_air + (1-φ) × k_fiber + k_radiation

Where:
- φ = porosity (typically 0.90-0.98 for fiberglass)
- k_air = 0.0257 W/m·K
- k_fiber ≈ 1.0 W/m·K (glass)
- k_radiation = radiation heat transfer component

Typical fiberglass insulation:
- k_eff ≈ 0.035-0.040 W/m·K
- R-value ≈ 3.5-4.0 per inch (RSI-0.61 to 0.70 per 25 mm)

### Duct Air Film Resistance

Internal and external air films on ductwork provide thermal resistance:

**Internal Film (Forced Convection):**

For air flowing at 5 m/s (1000 fpm) in a 0.3 m diameter duct:

Re = ρ × V × D / μ = 1.2 × 5 × 0.3 / (1.85×10⁻⁵) ≈ 97,000

Nu = 0.023 × Re^0.8 × Pr^0.4 = 0.023 × 97,000^0.8 × 0.71^0.4 ≈ 235

h = Nu × k / D = 235 × 0.0257 / 0.3 ≈ 20.1 W/m²·K

R_internal ≈ 0.050 m²·K/W

This internal film resistance is typically negligible compared to duct insulation resistance.

### Free Convection Heat Transfer

Natural convection from warm surfaces depends on air thermal conductivity through the Rayleigh number:

**Rayleigh Number:**

Ra = (g × β × ΔT × L³) / (ν × α)

Where:
- α = thermal diffusivity = k / (ρ × cp)
- For air at 20°C: α ≈ 2.1 × 10⁻⁵ m²/s

**Natural Convection Nusselt Number (Vertical Plate):**

Nu = 0.59 × Ra^(1/4) for 10⁴ < Ra < 10⁹ (laminar)

Nu = 0.10 × Ra^(1/3) for 10⁹ < Ra < 10¹³ (turbulent)

Then: h = Nu × k / L

## Design Considerations

### Temperature Correction

When performing heat transfer calculations, use thermal conductivity at the appropriate mean film temperature:

**Film Temperature:**

T_film = (T_surface + T_∞) / 2

Where:
- T_surface = surface temperature
- T_∞ = bulk air temperature

**Example:** For a 50°C surface in 20°C air:
- T_film = (50 + 20) / 2 = 35°C
- k = 0.0271 W/m·K (from table or correlation)

Correction factor from 20°C: k(35°C) / k(20°C) = 1.055

### Altitude Corrections

Air density decreases with altitude, but thermal conductivity remains approximately constant (per kinetic theory). However, convective heat transfer coefficients decrease due to reduced density:

**Convection Coefficient Altitude Correction:**

h(z) = h(sea level) × (ρ(z) / ρ(sea level))^n

Where n ≈ 0.5 to 0.8 depending on flow regime.

Thermal conductivity correction: negligible for altitudes below 3000 m.

### Low Conductivity Applications

Air's low thermal conductivity makes it an effective insulator when properly contained:

**Aerogel Insulation:**
- Trapped air in nanoporous structure
- k ≈ 0.013-0.020 W/m·K
- Approaches theoretical minimum for air-based insulation

**Vacuum Insulation Panels:**
- Evacuated air (P < 0.1 Pa) in rigid panel
- k ≈ 0.004-0.008 W/m·K
- Air conductivity eliminated by vacuum

**Spray Foam Insulation:**
- Closed-cell foam traps air/blowing agent
- k ≈ 0.021-0.028 W/m·K
- Small cells prevent convection

## Code References and Standards

### ASHRAE Standards

**ASHRAE Handbook—Fundamentals, Chapter 1: Psychrometrics**
- Table 1: Thermophysical properties of dry and moist air
- Air thermal conductivity correlations
- Valid temperature ranges and uncertainties

**ASHRAE Handbook—Fundamentals, Chapter 26: Heat, Air, and Moisture Control in Building Assemblies**
- Surface film coefficients incorporating air conductivity
- Air space thermal resistance values
- Temperature correction factors

**ASHRAE Standard 90.1: Energy Standard for Buildings**
- References air properties for thermal transmittance calculations
- Fenestration U-factor calculation methods
- Insulation R-value determination procedures

### ISO Standards

**ISO 15099: Thermal Performance of Windows, Doors and Shading Devices**
- Detailed air property correlations for glazing cavity calculations
- Temperature-dependent thermal conductivity equations
- Gas mixture calculation methods

**ISO 9869: Thermal Insulation—Building Elements—In-Situ Measurement**
- Air property assumptions for heat flux measurements
- Surface resistance standard values

### NIST Reference Data

**NIST Chemistry WebBook**
- Air thermal conductivity reference data
- Temperature range: 100-2000 K
- Uncertainty: ±2-3% for dilute gas properties

**REFPROP Database (NIST Standard Reference Database 23)**
- High-accuracy air property calculations
- Includes real gas effects at high pressure
- Mixture property calculations

## Measurement Methods

### Transient Hot-Wire Method

Standard technique for measuring gas thermal conductivity:

**Principle:** Thin electrically heated wire suspended in gas. Temperature rise relates to thermal conductivity:

ΔT = (q / 4πk) × ln(t) + constant

Where:
- q = heat input per unit length (W/m)
- t = time (s)
- k determined from slope of ΔT vs. ln(t)

**Accuracy:** ±1-2% under controlled conditions

**Standards:** ASTM E1952, ISO 8894

### Guarded Hot Plate

For lower accuracy field measurements:

**Method:** Measure heat flux through known air gap with temperature sensors on each side.

k = q × L / (T₁ - T₂) × A

Where:
- q = total heat transfer (W)
- L = air gap thickness (m)
- A = plate area (m²)

Must account for convection and radiation components.

## Practical Engineering Guidelines

### Heat Transfer Calculation Checklist

1. **Determine appropriate mean temperature** for property evaluation
2. **Select thermal conductivity** from tables or correlations at mean temperature
3. **Verify pressure conditions** (standard atmospheric unless specified)
4. **Account for humidity** only in precision calculations (>±5% accuracy required)
5. **Calculate dimensionless parameters** (Re, Pr, Ra, Nu) using consistent properties
6. **Apply appropriate correlations** for geometry and flow conditions
7. **Validate Reynolds number range** for correlation applicability
8. **Check for free convection effects** in low-velocity or temperature-driven flows

### Common Errors to Avoid

**Using properties at wrong temperature:** Always evaluate at film or mean temperature, not ambient.

**Ignoring convection in air spaces:** Air gaps thicker than ~20 mm experience convection; conduction-only models overpredict resistance.

**Assuming pressure independence at vacuum:** Below 0.1 Pa, thermal conductivity decreases significantly.

**Neglecting radiation in air spaces:** Radiation often dominates over conduction in building cavities.

**Inappropriate extrapolation:** Do not extend correlations beyond validated temperature ranges.

### Accuracy Expectations

| Application | Required Accuracy | Notes |
|-------------|-------------------|-------|
| Building envelope U-factor | ±5-10% | Use ASHRAE handbook values |
| HVAC equipment rating | ±3-5% | Use manufacturer correlations |
| Research/CFD | ±1-2% | Use NIST reference data |
| Preliminary design | ±10-20% | Simplified correlations acceptable |

### Software Implementation

Most HVAC design software uses built-in correlations:

**TRACE 3D Plus, Carrier HAP, Trane TRACE:** ASHRAE polynomial correlations for air properties

**EnergyPlus:** Psychrometric functions include thermal conductivity variation with temperature

**CFD packages (ANSYS Fluent, OpenFOAM):** Sutherland's law or polynomial fits for temperature-dependent properties

Verify property calculation methods in software documentation for critical applications.

## Advanced Topics

### Non-Continuum Effects

When air gap dimensions approach molecular mean free path (λ ≈ 70 nm at STP), continuum assumptions break down:

**Knudsen Number:**

Kn = λ / L

- Kn < 0.01: Continuum (standard equations apply)
- 0.01 < Kn < 0.1: Slip flow (use temperature jump boundary conditions)
- 0.1 < Kn < 10: Transition regime (molecular-continuum hybrid)
- Kn > 10: Free molecular flow (kinetic theory only)

Relevant for micro-scale devices and vacuum insulation panels.

### High-Temperature Applications

Above 200°C, thermal conductivity deviates from linear correlations:

**Sutherland's Formula (Extended Temperature Range):**

k(T) = k₀ × (T₀ + C) / (T + C) × (T/T₀)^(3/2)

Where:
- k₀ = 0.0257 W/m·K at T₀ = 293.15 K
- C = 122 K (Sutherland constant for air)
- Valid to 1000 K

Use for high-temperature HVAC applications (commercial cooking, industrial processes).

### Mixture Calculations

For air-gas mixtures (e.g., natural gas-air combustion):

**Wassiljewa Equation:**

k_mix = Σ (xᵢ × kᵢ) / Σ (xᵢ × Aᵢⱼ)

Where:
- xᵢ = mole fraction of component i
- kᵢ = thermal conductivity of pure component i
- Aᵢⱼ = binary interaction parameter

More accurate than simple mole fraction averaging for dissimilar gases.

## Summary

Thermal conductivity of air is a fundamental property governing convective heat transfer, insulation performance, and boundary layer behavior in HVAC systems. Key points:

- **Standard value:** k = 0.0257 W/m·K at 20°C and 1 atm
- **Temperature dependence:** Increases approximately 7.5 × 10⁻⁵ W/m·K per °C
- **Pressure independence:** Constant for pressures 0.1 Pa to 10 atm
- **Low magnitude:** Makes air an effective insulator when trapped in small cavities
- **Application critical:** Required for calculating convection coefficients, air space resistances, and insulation performance

Accurate thermal conductivity values at appropriate temperatures ensure reliable heat transfer calculations for HVAC system design, energy modeling, and building envelope analysis. Reference ASHRAE Handbook—Fundamentals for standardized values and correlations applicable to typical HVAC design conditions.
