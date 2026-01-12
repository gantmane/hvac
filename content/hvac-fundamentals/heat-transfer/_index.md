---
title: "Heat Transfer"
weight: 2
description: "Comprehensive overview of heat transfer principles in HVAC systems including conduction, convection, and radiation with governing equations, thermal properties, and engineering applications."
---

Heat transfer governs every aspect of HVAC system design and operation. Energy moves from high to low temperature through three fundamental mechanisms: conduction, convection, and radiation. Understanding these modes and their mathematical relationships enables accurate load calculations, equipment sizing, and system performance prediction.

## Conduction Heat Transfer

Conduction transfers energy through solid materials or stationary fluids via molecular vibration and electron motion. Fourier's Law quantifies steady-state conductive heat transfer:

**Q = -kA(dT/dx)**

Where:
- Q = heat transfer rate (W)
- k = thermal conductivity (W/m·K)
- A = cross-sectional area perpendicular to heat flow (m²)
- dT/dx = temperature gradient (K/m)

For one-dimensional steady conduction through a plane wall of thickness L with constant thermal conductivity:

**Q = kA(T₁ - T₂)/L**

Thermal conductivity varies widely among materials. Metals exhibit high values (copper: 385 W/m·K, aluminum: 205 W/m·K) while insulation materials provide low conductivity (fiberglass: 0.040 W/m·K, polyurethane foam: 0.023 W/m·K). ASHRAE Fundamentals Chapter 26 provides comprehensive thermal property data for building materials and HVAC components.

The concept of thermal resistance (R-value) simplifies analysis. For conductive resistance through a homogeneous layer:

**R = L/k** (m²·K/W)

Where higher R-values indicate better insulation performance. The inverse relationship between thermal conductivity and thickness determines resistance. Multiple layers add in series: R_total = R₁ + R₂ + R₃...

## Convection Heat Transfer

Convection transfers energy between a solid surface and adjacent moving fluid through combined molecular diffusion and bulk fluid motion. Newton's Law of Cooling describes convective heat transfer:

**Q = hA(T_s - T_∞)**

Where:
- h = convective heat transfer coefficient (W/m²·K)
- A = surface area (m²)
- T_s = surface temperature (K)
- T_∞ = bulk fluid temperature (K)

The heat transfer coefficient depends on fluid properties (density, viscosity, thermal conductivity, specific heat), flow conditions (velocity, turbulence), and surface geometry. Typical ranges for HVAC applications:

| Condition | h (W/m²·K) |
|-----------|-----------|
| Natural convection, air | 5-25 |
| Forced convection, air (low velocity) | 10-100 |
| Forced convection, air (high velocity) | 100-500 |
| Natural convection, water | 100-1000 |
| Forced convection, water | 500-10,000 |
| Condensing steam | 5,000-100,000 |

Engineers calculate convection coefficients using dimensionless correlations involving Reynolds number (Re), Prandtl number (Pr), Nusselt number (Nu), and Grashof number (Gr) for natural convection. These correlations appear extensively in ASHRAE Fundamentals Chapter 4.

Convective resistance follows: **R_conv = 1/(hA)**

## Radiation Heat Transfer

Radiation transfers energy through electromagnetic waves without requiring an intervening medium. All surfaces above absolute zero emit thermal radiation. The Stefan-Boltzmann Law governs emission from a blackbody:

**Q = σAT⁴**

Where:
- σ = Stefan-Boltzmann constant (5.67 × 10⁻⁸ W/m²·K⁴)
- A = surface area (m²)
- T = absolute temperature (K)

Real surfaces emit less than ideal blackbodies. Emissivity (ε) ranges from 0 to 1, with typical building materials exhibiting values of 0.85-0.95. Polished metals show low emissivity (0.02-0.10), making them effective radiant barriers.

Net radiation exchange between two surfaces involves:

**Q = εσA(T₁⁴ - T₂⁴)**

For small temperature differences, radiation can be linearized and incorporated into combined surface coefficients. This simplification aids building envelope calculations where radiation and convection occur simultaneously at interior and exterior surfaces.

## Combined Heat Transfer and U-Values

Most HVAC applications involve multiple heat transfer modes in series. The overall heat transfer coefficient (U-value) combines all resistances:

**U = 1/R_total = 1/(R_conv,1 + R_cond,1 + R_cond,2 + ... + R_conv,2)** (W/m²·K)

For a typical wall assembly:
**R_total = 1/h_i + L₁/k₁ + L₂/k₂ + ... + 1/h_o**

Where h_i and h_o represent interior and exterior surface coefficients including both convection and radiation effects. ASHRAE Handbook provides standard surface coefficients: h_i = 8.29 W/m²·K for vertical surfaces and h_o = 34.0 W/m²·K for winter conditions at 6.7 m/s wind speed.

Heat transfer through composite assemblies becomes:

**Q = UA(T_i - T_o)**

This expression drives building load calculations, determining heating and cooling requirements based on envelope construction and indoor-outdoor temperature differences.

## HVAC Applications

**Heat Exchangers:** Conduction through tube walls combined with convection on both fluid sides governs heat exchanger performance. Log mean temperature difference (LMTD) method and effectiveness-NTU approaches design shell-and-tube, plate, and coaxial heat exchangers. Fouling factors account for deposit buildup reducing thermal conductivity over time.

**Building Envelope:** Windows present complex heat transfer involving conduction through glazing layers, convection in gas gaps, and radiation between surfaces. Solar heat gain combines transmitted shortwave radiation with absorbed energy conducted inward. Low-e coatings reduce radiative exchange while multiple glazing layers increase conductive resistance.

**Equipment Heat Loss:** Uninsulated pipes and ducts lose energy through combined convection and radiation to surroundings. Insulation thickness optimization balances material cost against energy savings, with economic analysis determining optimal R-values for specific applications and energy costs.

## Steady-State vs Transient Analysis

Steady-state analysis assumes constant temperatures over time, simplifying calculations for design conditions. This approach sizes equipment for peak loads and establishes baseline performance expectations.

Transient analysis incorporates thermal mass effects. The heat equation with time dependence becomes:

**ρc_p(∂T/∂t) = k(∂²T/∂x²)**

Where:
- ρ = density (kg/m³)
- c_p = specific heat (J/kg·K)
- t = time (s)

Thermal mass (ρc_p) stores and releases energy, dampening temperature swings. Heavy construction materials like concrete provide thermal inertia, reducing peak loads and improving comfort. Dynamic simulation software solves transient equations hourly, capturing diurnal temperature variations, solar effects, and occupancy patterns.

## Engineering Calculations

Design procedures follow systematic approaches:

1. **Identify heat transfer paths** - Map energy flow through system components
2. **Determine thermal properties** - Obtain k, h, ε values from ASHRAE data or manufacturer specifications
3. **Calculate individual resistances** - Apply Fourier, Newton, and Stefan-Boltzmann relationships
4. **Combine resistances** - Sum series resistances, handle parallel paths appropriately
5. **Compute heat transfer rates** - Calculate Q using overall coefficients and temperature differences
6. **Verify against standards** - Check compliance with energy codes and best practices

Safety factors account for uncertainties in properties, installation quality, and operating conditions. Conservative assumptions prevent undersized equipment while economic analysis prevents excessive oversizing.

Understanding heat transfer fundamentals enables engineers to optimize HVAC system performance, minimize energy consumption, and ensure occupant comfort across diverse building types and climates. These principles connect directly to equipment selection, duct and pipe sizing, insulation specification, and control strategy development throughout the HVAC design process.
