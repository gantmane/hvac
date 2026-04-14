---
title: "Cooling and Freezing Times for Foods"
aliases: ["Cooling and Freezing Times for Foods"]
description: "Cooling and freezing time prediction methods for food products including Plank equation, Biot number analysis, and ASHRAE calculation procedures for refrigeration system design"
weight: 11
---

Accurate prediction of cooling and freezing times is essential for refrigeration system design, process optimization, and food safety compliance. Time-temperature relationships govern equipment capacity requirements, production throughput, and product quality outcomes in commercial refrigeration applications.

## Fundamentals of Cooling Time Prediction

Cooling time calculations determine the duration required to reduce product temperature from an initial value to a specified final temperature. The governing heat transfer equation for unsteady-state cooling follows:

Q = m × cp × (Ti - Tf)

Where m is product mass (kg), cp is specific heat (kJ/kg·K), Ti is initial temperature (°C), and Tf is final temperature (°C). However, this energy balance alone does not determine time—surface heat transfer coefficient, product geometry, and thermal properties control the rate of temperature change.

## Biot Number and Heat Transfer Regimes

The Biot number (Bi) characterizes the relative importance of internal thermal resistance versus external convective resistance:

Bi = h × L / k

Where h is surface heat transfer coefficient (W/m²·K), L is characteristic dimension (m), and k is thermal conductivity (W/m·K). For food products, Bi < 0.1 indicates negligible internal resistance (uniform temperature distribution), while Bi > 40 represents high internal resistance with surface temperature approximating medium temperature.

Most food refrigeration processes operate in the intermediate regime (0.1 < Bi < 40), requiring consideration of both internal conduction and external convection. This significantly complicates analytical solutions and necessitates semi-empirical prediction methods.

## Cooling Time Calculation Methods

For simple geometries and uniform properties, the dimensionless Heisler charts or analytical solutions to Fourier's equation provide cooling time estimates. The Fourier number (Fo) relates time to thermal diffusivity:

Fo = α × t / L²

Where α is thermal diffusivity (m²/s) and t is time (s). Heisler charts correlate dimensionless temperature ratio with Fo and Bi for infinite slabs, infinite cylinders, and spheres.

For practical refrigeration applications, ASHRAE Refrigeration Handbook Chapter 19 presents empirical prediction equations accounting for irregular geometry, non-uniform properties, and variable heat transfer coefficients. These methods typically express cooling time as:

t = f(geometry, mass, surface area, thermal properties, ΔT, h)

## Plank Equation for Freezing Time

The Plank equation remains the foundation for freezing time prediction despite significant simplifying assumptions. For a food product with initial temperature at the freezing point uniformly cooled to a final center temperature:

tf = (ρ × Hf / (Tfz - Tm)) × (P × a / h + R × a² / k)

Where:
- tf = freezing time (s)
- ρ = density (kg/m³)
- Hf = latent heat of fusion (kJ/kg)
- Tfz = initial freezing point (°C)
- Tm = refrigerating medium temperature (°C)
- a = characteristic dimension (thickness for slab, radius for cylinder/sphere)
- P, R = geometric constants (slab: P=1/2, R=1/8; cylinder: P=1/4, R=1/16; sphere: P=1/6, R=1/24)

The Plank equation assumes instantaneous surface temperature drop to medium temperature, constant thermal properties, and negligible sensible heat removal. These assumptions limit accuracy but provide conservative estimates suitable for preliminary equipment sizing.

## Modified Plank Methods

Numerous modifications improve Plank equation accuracy by accounting for:

**Precooling effects**: Products enter freezers above their initial freezing point, requiring sensible heat removal before latent heat extraction begins. The effective latent heat (Heff) incorporates this precooling load:

Heff = Hf + cp,above × (Ti - Tfz) / 1.8

**Subcooling requirements**: Final product temperature typically falls below initial freezing point. The effective temperature difference accounts for subcooling:

ΔTeff = Tfz - Tm + 0.5 × (Ti - Tfz)

**Variable thermal properties**: Thermal conductivity and specific heat change dramatically during phase transition. Weighted average properties based on frozen fraction improve prediction accuracy.

## Surface Heat Transfer Coefficient Determination

Surface heat transfer coefficient (h) critically influences both cooling and freezing time predictions. For forced convection in blast freezers and coolers:

h = C × v^n

Where v is air velocity (m/s) and C, n are empirical constants depending on product geometry and air flow orientation. Typical values: n = 0.6-0.8, C = 5-15 W/m²·K per (m/s)^n.

For natural convection in holding coolers, h ranges from 5-10 W/m²·K. For immersion freezing in brine or glycol solutions, h reaches 100-500 W/m²·K. Contact plate freezers achieve h values of 200-400 W/m²·K at the contact surfaces.

## Product Geometry Effects

Characteristic dimension (a) represents the shortest distance from product center to surface for heat removal. For regular geometries:

- Infinite slab (thickness 2a): half-thickness controls heat transfer
- Infinite cylinder (diameter 2a): radius determines cooling rate
- Sphere (diameter 2a): radius establishes characteristic dimension
- Finite cylinder: equivalent heat transfer dimension accounting for both radial and axial heat flow

Irregular shapes require equivalent sphere diameter or equivalent heat transfer dimension based on volume-to-surface-area ratio:

a = V / A × correction factor

## Practical Design Considerations

Refrigeration system capacity must accommodate the thermal load integrated over the entire cooling or freezing cycle. Peak load occurs when maximum product mass enters the system simultaneously. Cooler or freezer retention time must exceed the calculated cooling/freezing time by 20-30% safety factor to account for:

- Air temperature variation within the refrigerated space
- Product size and shape variations
- Thermal property uncertainties
- Load factor (actual vs. design capacity operation)
- Intermittent product loading patterns

Process control strategies include monitoring air temperature, product surface temperature, and in some cases product core temperature to verify adequate processing time. Multi-stage cooling or freezing systems with progressive temperature reduction improve energy efficiency and product quality compared to single-stage processes.

## Validation and Verification

ASHRAE Refrigeration Handbook Chapter 19 provides extensive tabulated cooling and freezing time data for common food products under specified conditions. These empirical data serve as benchmarks for validating calculation methods. For critical applications, experimental time-temperature measurement during commissioning verifies actual performance against design predictions.

Computational fluid dynamics (CFD) coupled with finite element heat transfer analysis enables detailed prediction accounting for complex geometries, non-uniform air flow, and transient operating conditions. These numerical methods supplement analytical calculations for optimizing equipment layout and operating parameters in high-value refrigeration installations.
