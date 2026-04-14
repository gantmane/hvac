---
title: "Conduction"
aliases: ["Conduction"]
description: "Detailed analysis of heat conduction principles in HVAC applications, including Fourier's Law, thermal resistance, R-values and U-values, one-dimensional and multidimensional conduction, and transient heat transfer for building envelope design."
weight: 1
---

Heat conduction is the transfer of thermal energy through matter via molecular collisions and electron diffusion without bulk motion of the material. In HVAC systems, conduction governs heat transfer through building envelopes, pipe insulation, heat exchanger walls, and any solid boundary separating regions of different temperature.

## Fourier's Law of Heat Conduction

The fundamental relationship governing conduction is Fourier's Law, which states that heat flux is proportional to the temperature gradient:

**q" = -k(dT/dx)**

Where:
- q" = heat flux (W/m²)
- k = thermal conductivity (W/m·K)
- dT/dx = temperature gradient in the direction of heat flow (K/m)
- The negative sign indicates heat flows from high to low temperature

For one-dimensional steady-state conduction through a plane wall of thickness L with constant thermal conductivity:

**Q = kA(T₁ - T₂)/L**

Where Q is the heat transfer rate (W), A is the area (m²), and T₁ and T₂ are the surface temperatures.

## Thermal Conductivity of HVAC Materials

Thermal conductivity varies significantly across materials encountered in HVAC applications. Representative values at 20°C include:

| Material | k (W/m·K) | k (Btu·in/hr·ft²·°F) |
|----------|-----------|----------------------|
| Copper | 401 | 2780 |
| Aluminum | 237 | 1644 |
| Steel (carbon) | 50-60 | 347-416 |
| Concrete (normal weight) | 1.4-1.7 | 9.7-11.8 |
| Brick (common) | 0.6-0.9 | 4.2-6.2 |
| Gypsum board | 0.16 | 1.1 |
| Fiberglass insulation | 0.04 | 0.28 |
| Polyurethane foam | 0.023-0.026 | 0.16-0.18 |
| Air (still) | 0.026 | 0.18 |

Thermal conductivity generally increases with temperature for most insulating materials but remains relatively constant for metals within typical HVAC operating ranges.

## Thermal Resistance and Composite Walls

Building envelopes consist of multiple layers with different thermal properties. The thermal resistance concept simplifies analysis of these composite assemblies.

Thermal resistance for a single layer:

**R = L/k** (units: m²·K/W or hr·ft²·°F/Btu)

For steady-state conduction through multiple layers in series, resistances add directly:

**R_total = R₁ + R₂ + R₃ + ... + R_n**

The heat transfer rate through a composite wall becomes:

**Q = A(T₁ - T₂)/R_total**

This equation is analogous to Ohm's Law in electrical circuits, where heat flow corresponds to current, temperature difference to voltage, and thermal resistance to electrical resistance.

Surface film coefficients at interior and exterior boundaries contribute additional resistance:

**R_total = R_inside_film + R_wall_layers + R_outside_film**

ASHRAE Fundamentals provides tabulated values for surface conductances (h) and their reciprocal film resistances (R = 1/h) under various conditions.

## R-Value and U-Value

The R-value is the total thermal resistance of an assembly, commonly expressed in IP units (hr·ft²·°F/Btu). Higher R-values indicate better insulation performance. Building codes typically specify minimum R-values for walls, roofs, and foundations.

The U-value (overall heat transfer coefficient) is the reciprocal of total thermal resistance:

**U = 1/R_total** (units: W/m²·K or Btu/hr·ft²·°F)

U-values are preferred in heat transfer calculations because they directly relate heat flux to temperature difference:

**q" = U(T₁ - T₂)**

For ASHRAE load calculations, U-values multiply by area and temperature difference to yield heat gains or losses. Window manufacturers report U-values for their products, with lower values indicating better insulation.

## Cylindrical Conduction (Pipes and Tubes)

Heat conduction through pipe walls and cylindrical insulation follows a logarithmic temperature profile. For a hollow cylinder with inner radius r₁, outer radius r₂, length L, and thermal conductivity k:

**Q = 2πkL(T₁ - T₂)/ln(r₂/r₁)**

Thermal resistance per unit length:

**R' = ln(r₂/r₁)/(2πk)** (units: m·K/W or hr·ft·°F/Btu)

For insulated pipes with multiple cylindrical layers:

**Q = 2πL(T_inside - T_outside)/[ln(r₂/r₁)/(k_pipe) + ln(r₃/r₂)/(k_insulation) + ...]**

Critical insulation radius exists for small-diameter pipes where adding thin insulation may initially increase heat transfer by increasing surface area more than resistance. For cylindrical geometries:

**r_critical = k/h**

Where h is the outer surface convection coefficient. This phenomenon is relevant for small-diameter tubes but negligible for standard pipe sizes with typical insulation thicknesses.

## Spherical Conduction (Tanks and Vessels)

Heat transfer through spherical shells (pressure vessels, storage tanks) follows:

**Q = 4πkr₁r₂(T₁ - T₂)/(r₂ - r₁)**

Thermal resistance:

**R = (r₂ - r₁)/(4πkr₁r₂)**

The spherical geometry provides the most favorable surface-area-to-volume ratio for minimizing heat transfer per unit stored volume.

## Transient Conduction

Transient (time-dependent) conduction occurs during startup, shutdown, or varying load conditions. The governing equation for one-dimensional transient conduction is:

**ρc_p(∂T/∂t) = k(∂²T/∂x²)**

Where ρ is density (kg/m³) and c_p is specific heat (J/kg·K). Two dimensionless numbers characterize transient behavior:

**Biot Number: Bi = hL_c/k**

The Biot number represents the ratio of internal conduction resistance to surface convection resistance. When Bi < 0.1, internal temperature gradients are negligible, and the lumped capacitance method applies:

**T(t) - T_∞ / T_i - T_∞ = exp(-hA/ρVc_p · t)**

**Fourier Number: Fo = αt/L_c²**

Where α = k/(ρc_p) is thermal diffusivity (m²/s) and L_c is the characteristic length. The Fourier number represents the ratio of heat conducted to heat stored.

For Bi > 0.1, spatial temperature distributions develop, requiring series solutions or numerical methods. ASHRAE provides charts and analytical approximations for common geometries (infinite slab, cylinder, sphere) based on Bi and Fo.

## Building Envelope Applications

Conduction analysis is fundamental to building load calculations and energy modeling. Key applications include:

**Wall and Roof Assemblies**: Multi-layer constructions with framing members create parallel heat flow paths. Effective U-values account for thermal bridging through studs using zone methods or isothermal planes methods per ASHRAE Fundamentals Chapter 27.

**Below-Grade Heat Transfer**: Ground-coupled heat transfer involves two-dimensional conduction with temperature-dependent boundary conditions. ASHRAE provides F-factors (perimeter heat loss factors) and U-factors for slab-on-grade and basement configurations.

**Thermal Bridging**: Continuous metal elements (window frames, shelf angles, Z-girts) bypass insulation layers, creating localized high heat flux areas. Linear thermal transmittance (ψ-value) quantifies this effect in W/m·K.

**Thermal Mass**: Materials with high volumetric heat capacity (ρc_p) dampen temperature swings through transient storage effects. Heavy construction exhibits lower peak loads and phase lag compared to lightweight assemblies with equivalent steady-state R-values.

**Interface Resistances**: Imperfect contact between layers creates additional thermal resistance. ASHRAE provides typical values for air gaps of various thicknesses and emissivities, which significantly affect performance of reflective insulation systems.

Accurate conduction modeling requires attention to moisture content (increases k), air infiltration through envelope defects, and installation quality. Field measurements often show 10-30% degradation from design U-values due to thermal bridging and gaps in insulation coverage.
