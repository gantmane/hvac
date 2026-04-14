---
title: "Transport Properties"
aliases: ["Transport Properties"]
description: "Refrigerant transport properties including dynamic and kinematic viscosity, thermal conductivity, and surface tension - critical parameters for heat transfer coefficient calculation, pressure drop analysis, and refrigeration system design"
weight: 7
---

Transport properties govern the movement of momentum, energy, and mass within refrigerants during phase change and fluid flow. These properties directly influence heat transfer coefficients, pressure drop, pumping power requirements, and overall system performance in vapor-compression refrigeration cycles.

## Dynamic Viscosity

Dynamic viscosity (μ) quantifies a fluid's internal resistance to flow, representing the ratio of shear stress to velocity gradient:

τ = μ(dv/dy)

Where:
- τ = shear stress (Pa)
- μ = dynamic viscosity (Pa·s or kg/m·s)
- dv/dy = velocity gradient perpendicular to flow direction (s⁻¹)

### Temperature Dependence

Dynamic viscosity decreases with increasing temperature for both liquid and vapor phases. For liquids, viscosity reduction follows an approximately exponential relationship, while vapor viscosity increases slightly with temperature due to increased molecular kinetic activity.

Liquid refrigerants typically exhibit viscosities of 0.0001 to 0.0005 Pa·s at typical evaporator and condenser temperatures. Vapor viscosities are approximately two orders of magnitude lower, ranging from 0.00001 to 0.00002 Pa·s.

### Pressure Effects

Liquid viscosity increases moderately with pressure due to reduced molecular spacing. This effect becomes pronounced at pressures exceeding 50% of critical pressure. Vapor viscosity shows minimal pressure dependence at subcritical conditions but increases significantly near the critical point.

## Kinematic Viscosity

Kinematic viscosity (ν) represents the ratio of dynamic viscosity to density:

ν = μ/ρ

Where:
- ν = kinematic viscosity (m²/s)
- μ = dynamic viscosity (Pa·s)
- ρ = density (kg/m³)

This property appears directly in Reynolds number calculations and convective heat transfer correlations. Typical values:

| Refrigerant | Liquid ν at 0°C (×10⁻⁷ m²/s) | Vapor ν at 0°C (×10⁻⁶ m²/s) |
|-------------|------------------------------|------------------------------|
| R-134a      | 2.8                          | 1.1                          |
| R-410A      | 2.1                          | 0.89                         |
| R-32        | 1.9                          | 0.95                         |
| R-407C      | 2.4                          | 1.0                          |
| Ammonia     | 3.2                          | 1.8                          |

## Thermal Conductivity

Thermal conductivity (k) quantifies the rate of heat transfer through a material by conduction, governed by Fourier's law:

q" = -k(dT/dx)

Where:
- q" = heat flux (W/m²)
- k = thermal conductivity (W/m·K)
- dT/dx = temperature gradient in direction of heat flow (K/m)

### Liquid Phase Thermal Conductivity

Liquid refrigerants exhibit thermal conductivities ranging from 0.07 to 0.15 W/m·K at typical operating conditions. Thermal conductivity decreases linearly with increasing temperature as molecular spacing increases.

Ammonia possesses exceptionally high liquid thermal conductivity (approximately 0.5 W/m·K), contributing to superior heat transfer performance in industrial refrigeration applications.

### Vapor Phase Thermal Conductivity

Vapor thermal conductivity is significantly lower than liquid values, typically 0.01 to 0.02 W/m·K. Unlike liquids, vapor thermal conductivity increases with temperature due to enhanced molecular kinetic energy and mean free path.

### Impact on Heat Transfer

Thermal conductivity appears in the Prandtl number, which characterizes the relative importance of momentum and thermal diffusion:

Pr = (c_p × μ)/k

Higher thermal conductivity reduces Prandtl number and generally improves convective heat transfer coefficients through the relationship:

Nu = f(Re, Pr)

Where Nu is the Nusselt number, relating convective to conductive heat transfer.

## Surface Tension

Surface tension (σ) represents the energy per unit area required to create a liquid-vapor interface. This property governs bubble formation during boiling, droplet behavior during condensation, and capillary effects in evaporators.

### Magnitude and Temperature Dependence

Surface tension decreases linearly with temperature, approaching zero at the critical point. Typical values at 25°C:

| Refrigerant | Surface Tension at 25°C (mN/m) |
|-------------|--------------------------------|
| R-134a      | 8.9                            |
| R-410A      | 6.2                            |
| R-32        | 10.3                           |
| R-407C      | 7.5                            |
| Ammonia     | 21.2                           |
| R-1234yf    | 7.8                            |
| R-290 (Propane) | 7.2                        |

### Nucleate Boiling

Surface tension directly influences nucleate boiling heat transfer through the critical radius for bubble nucleation:

r_c = (2σT_sat)/(ρ_v h_fg ΔT_sat)

Where:
- r_c = critical bubble radius (m)
- σ = surface tension (N/m)
- T_sat = saturation temperature (K)
- ρ_v = vapor density (kg/m³)
- h_fg = latent heat of vaporization (J/kg)
- ΔT_sat = wall superheat (K)

Lower surface tension promotes earlier nucleation at smaller cavity sizes, enhancing boiling heat transfer coefficients.

## Transport Property Data Tables

### HFC and HFO Refrigerants at 0°C Saturation

| Property | R-134a | R-410A | R-32 | R-1234yf |
|----------|--------|--------|------|----------|
| μ_liquid (μPa·s) | 280 | 170 | 160 | 240 |
| μ_vapor (μPa·s) | 10.8 | 12.1 | 11.5 | 10.2 |
| k_liquid (mW/m·K) | 94 | 102 | 115 | 85 |
| k_vapor (mW/m·K) | 11.2 | 14.8 | 13.9 | 10.8 |
| σ (mN/m) | 11.6 | 8.5 | 13.2 | 10.1 |

### Natural Refrigerants at 0°C Saturation

| Property | Ammonia (R-717) | Propane (R-290) | CO₂ (R-744) |
|----------|-----------------|-----------------|-------------|
| μ_liquid (μPa·s) | 168 | 125 | 95 |
| μ_vapor (μPa·s) | 9.2 | 7.8 | 13.5 |
| k_liquid (mW/m·K) | 520 | 108 | 135 |
| k_vapor (mW/m·K) | 22.5 | 16.2 | 14.8 |
| σ (mN/m) | 26.5 | 9.8 | 3.2 |

## Engineering Applications

### Pressure Drop Calculations

Dynamic viscosity appears directly in friction factor correlations for both laminar and turbulent flow:

**Laminar flow (Re < 2300):**
f = 64/Re = 64μ/(ρvD)

**Turbulent flow (Re > 4000):**
f = f(Re, ε/D) where Re = ρvD/μ

Pressure drop through piping, heat exchangers, and expansion devices increases with viscosity, affecting compressor work input and system efficiency.

### Heat Transfer Coefficient Prediction

Transport properties appear in dimensional analysis correlations for forced convection:

Nu = C × Re^m × Pr^n

Where the Prandtl number couples viscosity and thermal conductivity:

Pr = μc_p/k

For flow boiling, the dimensionless groups include:
- Reynolds number: Re = GD/μ
- Boiling number: Bo = q"/(Gh_fg)
- Convection number: Co = [(ρ_l/ρ_v - 1)]^0.5 × (1-x)/x

### Oil Effects on Transport Properties

Lubricating oil dissolved in liquid refrigerant significantly alters transport properties:

- Viscosity increases exponentially with oil concentration
- Thermal conductivity decreases by 5-20% with typical oil concentrations (2-5%)
- Surface tension decreases, affecting nucleate boiling initiation

Oil concentrations exceeding 5% by mass can reduce evaporator heat transfer coefficients by 20-40% due to viscosity increases and thermal conductivity reductions.

## Measurement and Correlation Methods

### Viscosity Measurement

Capillary viscometers measure dynamic viscosity by timing fluid flow through calibrated tubes under known pressure differential. Falling body viscometers determine viscosity from terminal velocity of spheres through the fluid.

### Thermal Conductivity Measurement

Transient hot-wire methods provide accurate thermal conductivity data across wide temperature and pressure ranges. A thin platinum wire immersed in the refrigerant experiences controlled heating while temperature rise is monitored.

### Property Correlations

Extended corresponding states models predict transport properties using critical constants and acentric factor. These correlations provide accuracy within 5-10% for most refrigerants across normal operating ranges.

REFPROP (NIST Reference Fluid Thermodynamic and Transport Properties Database) implements advanced equations of state and transport property models, serving as the industry standard for refrigerant property data.

## Design Considerations

Selection of refrigerants for specific applications must consider transport properties alongside thermodynamic characteristics:

- Low viscosity reduces pressure drop but may compromise oil return in direct expansion systems
- High thermal conductivity improves heat exchanger performance, enabling smaller heat transfer areas
- Moderate surface tension optimizes both nucleate boiling (lower is better) and condensation heat transfer (higher prevents dropwise collapse)

Transport properties vary by 20-30% across the typical operating range of refrigeration equipment, necessitating evaluation at actual operating conditions rather than relying on single-point property data.
