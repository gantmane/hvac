---
title: "Convection"
aliases: ["Convection"]
description: "Convection heat transfer fundamentals including Newton's Law of Cooling, heat transfer coefficients, dimensionless numbers, and HVAC applications in coils and heat exchangers."
weight: 2
---

Convection heat transfer occurs when a fluid in motion exchanges thermal energy with a surface. This mode combines conduction at the surface with bulk fluid motion, making it the dominant mechanism in HVAC equipment such as coils, heat exchangers, and air distribution systems.

## Newton's Law of Cooling

The convective heat transfer rate is expressed by Newton's Law of Cooling:

**Q = h·A·ΔT**

Where:
- Q = convective heat transfer rate (W or Btu/h)
- h = convective heat transfer coefficient (W/m²·K or Btu/h·ft²·°F)
- A = surface area (m² or ft²)
- ΔT = temperature difference between surface and bulk fluid (K or °F)

The heat transfer coefficient h encapsulates all complexities of fluid flow, thermophysical properties, and geometry. Determining h is the primary challenge in convection analysis.

## Natural vs Forced Convection

**Natural (Free) Convection** occurs when fluid motion results solely from buoyancy forces caused by density differences. Applications include baseboard heaters, natural convection from building surfaces, and heat dissipation from equipment enclosures. Heat transfer coefficients typically range from 3-25 W/m²·K (0.5-4.5 Btu/h·ft²·°F) for gases.

**Forced Convection** involves externally induced fluid motion via fans, pumps, or wind. This mechanism dominates in air handlers, coils, and hydronic systems. Heat transfer coefficients range from 25-250 W/m²·K (4.5-45 Btu/h·ft²·°F) for air and 500-10,000 W/m²·K (90-1800 Btu/h·ft²·°F) for water, depending on velocity and turbulence.

## Dimensionless Numbers

Convection analysis relies on dimensionless groups that characterize flow and heat transfer:

**Reynolds Number (Re)**: Ratio of inertial to viscous forces, determines flow regime.

Re = ρ·V·L / μ = V·L / ν

Where ρ = density, V = velocity, L = characteristic length, μ = dynamic viscosity, ν = kinematic viscosity. Transition from laminar to turbulent flow typically occurs at Re ≈ 2300 for internal pipe flow and Re ≈ 500,000 for external flow over flat plates.

**Prandtl Number (Pr)**: Ratio of momentum diffusivity to thermal diffusivity.

Pr = μ·cp / k = ν / α

Where cp = specific heat, k = thermal conductivity, α = thermal diffusivity. For air at standard conditions, Pr ≈ 0.7; for water, Pr ≈ 7. This indicates that momentum and thermal boundary layers develop differently.

**Nusselt Number (Nu)**: Dimensionless heat transfer coefficient representing the ratio of convective to conductive heat transfer.

Nu = h·L / k

The Nusselt number is the target of empirical correlations, as it directly yields the heat transfer coefficient once determined.

**Grashof Number (Gr)**: Ratio of buoyancy to viscous forces in natural convection.

Gr = g·β·ΔT·L³ / ν²

Where g = gravitational acceleration, β = volumetric thermal expansion coefficient. For ideal gases, β = 1/T (absolute temperature).

**Rayleigh Number (Ra)**: Combined parameter for natural convection.

Ra = Gr·Pr = g·β·ΔT·L³ / (ν·α)

Natural convection transitions to turbulence at Ra ≈ 10⁹ for vertical surfaces.

## Correlations for Common Geometries

### Flat Plates (External Flow)

**Laminar flow (Re < 500,000):**

Nu_x = 0.332·Re_x^0.5·Pr^(1/3)

**Turbulent flow (Re > 500,000):**

Nu_x = 0.0296·Re_x^0.8·Pr^(1/3)

Where subscript x denotes local values at distance x from the leading edge.

### Cylinders in Cross-Flow

For air flowing perpendicular to tubes (common in finned-tube coils):

Nu_D = C·Re_D^m·Pr^(1/3)

Constants C and m depend on Reynolds number range. For 40 < Re_D < 4000: C = 0.683, m = 0.466. For 4000 < Re_D < 40,000: C = 0.193, m = 0.618. ASHRAE Fundamentals Chapter 4 provides detailed correlations for tube banks.

### Internal Flow in Tubes

**Laminar flow (Re < 2300):**

For fully developed flow with constant surface temperature: Nu = 3.66

For fully developed flow with constant heat flux: Nu = 4.36

**Turbulent flow (Re > 4000):**

Dittus-Boelter equation (smooth tubes, 0.6 < Pr < 160, Re > 10,000):

Nu_D = 0.023·Re_D^0.8·Pr^n

Where n = 0.4 for heating (Ts > Tb) and n = 0.3 for cooling (Ts < Tb).

Gnielinski correlation (improved accuracy, 3000 < Re < 5×10⁶, 0.5 < Pr < 2000):

Nu_D = [(f/8)·(Re_D - 1000)·Pr] / [1 + 12.7·(f/8)^0.5·(Pr^(2/3) - 1)]

Where f = (0.790·ln(Re_D) - 1.64)^(-2) is the Darcy friction factor.

## Internal Flow in Ducts

For non-circular ducts, the hydraulic diameter replaces the diameter:

D_h = 4·A_c / P

Where A_c = cross-sectional area, P = wetted perimeter. For rectangular ducts: D_h = 2·a·b / (a + b), where a and b are duct dimensions.

Turbulent flow correlations for tubes apply to ducts using D_h, though accuracy decreases for aspect ratios exceeding 4:1. ASHRAE Fundamentals Chapter 21 provides duct-specific correlations accounting for aspect ratio effects.

## HVAC Applications

**Finned-Tube Coils**: Heat transfer involves air-side convection (limiting resistance), tube-side convection (water or refrigerant), and conduction through fins. Air-side coefficients range from 40-100 W/m²·K depending on face velocity (typically 1.5-3 m/s). Water-side coefficients reach 3000-8000 W/m²·K in turbulent flow.

**Heat Exchangers**: Overall heat transfer coefficient U combines convective resistances on both fluid sides plus conduction through the separating wall:

1/U = 1/h_i + t_wall/k_wall + 1/h_o

Where subscripts i and o denote inside and outside. Fouling factors are added as additional thermal resistances per ASHRAE Fundamentals Chapter 4.

**Room Surfaces**: Natural convection from walls, ceilings, and floors contributes to room heat balance. Combined convection and radiation coefficients typically range from 8-12 W/m²·K for vertical surfaces and 6-10 W/m²·K for horizontal surfaces, depending on orientation and temperature difference.

**Ductwork Heat Loss/Gain**: External forced convection from duct surfaces depends on air velocity around the duct. For rectangular ducts in mechanical rooms, h ranges from 10-20 W/m²·K. This affects supply air temperature and system efficiency.

Understanding convection principles enables accurate sizing of heat exchangers, prediction of coil performance, calculation of duct heat transfer, and evaluation of natural ventilation effectiveness. The heat transfer coefficient h bridges theoretical analysis and practical equipment selection.
