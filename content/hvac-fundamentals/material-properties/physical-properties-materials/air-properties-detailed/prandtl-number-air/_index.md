---
title: "Prandtl Number for Air"
description: "Comprehensive analysis of Prandtl number for air including temperature dependence, role in forced and natural convection heat transfer correlations, dimensionless analysis, and HVAC thermal design calculations for ductwork, heat exchangers, and equipment performance evaluation."
weight: 5
---

## Definition and Physical Significance

The Prandtl number (Pr) is a dimensionless parameter that characterizes the relative thickness of the velocity boundary layer to the thermal boundary layer in a fluid flow. For air and other fluids, it represents the ratio of momentum diffusivity to thermal diffusivity:

**Pr = ν/α = (μ/ρ)/(k/ρcp) = μcp/k**

Where:
- ν = kinematic viscosity (m²/s)
- α = thermal diffusivity (m²/s)
- μ = dynamic viscosity (Pa·s or kg/m·s)
- ρ = density (kg/m³)
- cp = specific heat at constant pressure (J/kg·K)
- k = thermal conductivity (W/m·K)

The Prandtl number indicates how quickly momentum diffuses compared to heat in a flowing fluid. For air under standard HVAC conditions, Pr ≈ 0.7, meaning momentum diffuses slightly faster than thermal energy.

## Physical Interpretation

**Velocity vs. Thermal Boundary Layers:**

The Prandtl number directly relates to the relative development of velocity and temperature profiles in boundary layer flow:

- **Pr < 1** (liquid metals): Thermal boundary layer is thicker than velocity boundary layer. Heat diffuses faster than momentum.
- **Pr ≈ 1** (gases, including air): Velocity and thermal boundary layers develop at similar rates.
- **Pr > 1** (water, oils): Thermal boundary layer is thinner than velocity boundary layer. Momentum diffuses faster than heat.

For air with Pr ≈ 0.7, the thermal boundary layer extends approximately 1.4 times farther than the velocity boundary layer (ratio ≈ Pr^(1/3) for turbulent flow).

## Temperature Dependence for Air

The Prandtl number for air exhibits weak temperature dependence over typical HVAC operating ranges. This near-constancy simplifies heat transfer calculations significantly.

### Prandtl Number Values for Air at Atmospheric Pressure

| Temperature (°C) | Temperature (°F) | Prandtl Number | % Change from 20°C |
|------------------|------------------|----------------|-------------------|
| -40 | -40 | 0.7246 | +2.9% |
| -20 | -4 | 0.7177 | +1.9% |
| 0 | 32 | 0.7119 | +1.1% |
| 10 | 50 | 0.7090 | +0.7% |
| 20 | 68 | 0.7062 | 0% (ref) |
| 30 | 86 | 0.7036 | -0.4% |
| 40 | 104 | 0.7012 | -0.7% |
| 50 | 122 | 0.6990 | -1.0% |
| 60 | 140 | 0.6969 | -1.3% |
| 80 | 176 | 0.6932 | -1.8% |
| 100 | 212 | 0.6899 | -2.3% |
| 150 | 302 | 0.6827 | -3.3% |
| 200 | 392 | 0.6770 | -4.1% |
| 250 | 482 | 0.6722 | -4.8% |
| 300 | 572 | 0.6681 | -5.4% |

**Engineering Practice:** For most HVAC calculations in the range -20°C to 60°C (-4°F to 140°F), using Pr = 0.71 introduces negligible error (< 2%).

## Role in Convective Heat Transfer Correlations

The Prandtl number appears in virtually all forced and natural convection heat transfer correlations, connecting the Nusselt number to Reynolds or Rayleigh numbers.

### Forced Convection Correlations

**Laminar Flow over Flat Plate:**

Nu_x = 0.332 Re_x^(1/2) Pr^(1/3)

Valid for: Re_x < 5×10⁵, Pr > 0.6

**Turbulent Flow over Flat Plate:**

Nu_x = 0.0296 Re_x^(4/5) Pr^(1/3)

Valid for: 5×10⁵ < Re_x < 10⁷, 0.6 < Pr < 60

**Laminar Flow in Circular Tubes (Developing Region):**

Nu = 3.66 + (0.0668(D/L)Re·Pr) / (1 + 0.04[(D/L)Re·Pr]^(2/3))

For fully developed: Nu = 3.66 (constant wall temperature)

**Turbulent Flow in Circular Tubes (Dittus-Boelter):**

Nu = 0.023 Re^(0.8) Pr^n

Where n = 0.4 for heating (Tw > Tb), n = 0.3 for cooling (Tw < Tb)

Valid for: Re > 10,000, 0.7 < Pr < 160, L/D > 10

**Turbulent Flow in Circular Tubes (Gnielinski):**

Nu = ((f/8)(Re-1000)Pr) / (1 + 12.7(f/8)^(1/2)(Pr^(2/3) - 1))

Where f = friction factor from Moody diagram or Colebrook equation

Valid for: 3000 < Re < 5×10⁶, 0.5 < Pr < 2000

This correlation accounts for transition region and provides better accuracy than Dittus-Boelter.

### Natural Convection Correlations

**Vertical Flat Plate:**

Nu_L = 0.59 Ra_L^(1/4)     (laminar, 10⁴ < Ra_L < 10⁹)

Nu_L = 0.10 Ra_L^(1/3)     (turbulent, 10⁹ < Ra_L < 10¹³)

Where Ra_L = Gr_L · Pr (Rayleigh number)

**Horizontal Cylinder:**

Nu_D = {0.60 + (0.387 Ra_D^(1/6)) / [1 + (0.559/Pr)^(9/16)]^(8/27)}²

Valid for: 10⁻⁵ < Ra_D < 10¹², all Pr

**Enclosed Air Spaces (vertical cavity):**

Nu_L = 0.42 Ra_L^(1/4) Pr^(0.012) (H/L)^(-0.3)

Valid for: 10⁴ < Ra_L < 10⁷, 1 < Pr < 2×10⁴, 10 < H/L < 40

## Relationship with Reynolds and Nusselt Numbers

The Prandtl number serves as a bridge between fluid mechanics (Reynolds number) and heat transfer (Nusselt number).

### Fundamental Dimensionless Groups

**Reynolds Number (Re):**

Re = ρVL/μ = VL/ν = inertial forces / viscous forces

Characterizes flow regime (laminar vs. turbulent)

**Nusselt Number (Nu):**

Nu = hL/k = convective heat transfer / conductive heat transfer

Dimensionless heat transfer coefficient

**Peclet Number (Pe):**

Pe = Re · Pr = VL/α

Ratio of advective to diffusive heat transport

**Stanton Number (St):**

St = Nu/(Re·Pr) = h/(ρVcp)

Dimensionless heat transfer coefficient for forced convection

### Physical Relationship

In forced convection, the general functional form is:

**Nu = f(Re, Pr, geometry)**

For most correlations: Nu ∝ Re^m · Pr^n

Where:
- m depends on flow regime (typically 0.5 for laminar, 0.8 for turbulent)
- n typically ranges from 1/3 to 0.4 for air

The Pr^(1/3) dependence in many correlations reflects the relative boundary layer thickness scaling:

δ_thermal/δ_velocity ∝ Pr^(1/3)

This means the thermal boundary layer thickness (which inversely affects heat transfer) scales with the cube root of Prandtl number.

## Application in HVAC Heat Transfer Calculations

### Duct Heat Transfer

**Problem:** Calculate convective heat transfer coefficient for air at 20°C flowing at 5 m/s through a 300 mm diameter circular duct.

**Solution:**

Properties at 20°C:
- ρ = 1.204 kg/m³
- μ = 1.825×10⁻⁵ Pa·s
- cp = 1005 J/kg·K
- k = 0.0257 W/m·K
- Pr = 0.7062

Reynolds number:

Re = ρVD/μ = (1.204)(5)(0.3)/(1.825×10⁻⁵) = 99,180 (turbulent)

Using Gnielinski correlation (assuming smooth duct, f ≈ 0.019):

Nu = ((0.019/8)(99,180-1000)(0.7062)) / (1 + 12.7(0.019/8)^(1/2)(0.7062^(2/3) - 1))

Nu = 247.6

Convective heat transfer coefficient:

h = Nu·k/D = (247.6)(0.0257)/0.3 = 21.2 W/m²·K

**Impact of Prandtl Number:**

If Pr were incorrectly assumed as 1.0 instead of 0.706:
- Nu would increase by approximately 9% (Pr^(1/3) term)
- This translates to 9% error in heat transfer coefficient
- For precision HVAC design, accurate Pr values matter

### Heat Exchanger Performance

In heat exchanger effectiveness-NTU calculations, the heat capacity rate ratio and NTU both depend on convective coefficients, which in turn depend on Prandtl number through Nu correlations.

**Number of Transfer Units (NTU):**

NTU = UA/C_min

Where U depends on convective coefficients h_hot and h_cold on both sides. For air-to-air heat exchangers:

1/U = 1/h_hot + R_wall + 1/h_cold

Both convective coefficients scale with Pr^n where n ≈ 0.3-0.4.

### Natural Convection from Equipment

**Problem:** Determine heat loss from a vertical 2 m tall control panel at 50°C in 20°C ambient air.

**Solution:**

Film temperature: T_f = (50+20)/2 = 35°C

Properties at 35°C:
- Pr ≈ 0.7025
- ν ≈ 1.655×10⁻⁵ m²/s
- k ≈ 0.0268 W/m·K
- β ≈ 1/308 K⁻¹

Grashof number:

Gr_L = gβΔTL³/ν² = (9.81)(1/308)(30)(2³)/(1.655×10⁻⁵)² = 2.78×10⁹

Rayleigh number:

Ra_L = Gr_L · Pr = (2.78×10⁹)(0.7025) = 1.95×10⁹

Using laminar vertical plate correlation:

Nu_L = 0.59 Ra_L^(1/4) = 0.59(1.95×10⁹)^(1/4) = 124.5

Average convective coefficient:

h = Nu_L·k/L = (124.5)(0.0268)/2 = 1.67 W/m²·K

The Pr = 0.7025 value is embedded in the Ra calculation and affects the boundary layer structure.

## Effect on Thermal Boundary Layer Development

The thermal entry length in ducts depends strongly on Prandtl number:

**Laminar Flow:**

L_t/D ≈ 0.05 Re·Pr

For air with Pr ≈ 0.7, thermal entry length is slightly shorter than hydrodynamic entry length (L_h/D ≈ 0.05 Re).

**Example:** Air at Re = 2000 in a 200 mm duct:
- L_t = 0.05(2000)(0.7)(0.2) = 14 m
- L_h = 0.05(2000)(0.2) = 20 m

The thermal boundary layer reaches fully developed conditions before the velocity profile.

**Turbulent Flow:**

L_t/D ≈ 10 (approximately independent of Re and Pr for gases)

Both thermal and velocity profiles develop rapidly in turbulent flow, typically within 10-20 diameters.

## Specialized Correlations for HVAC Equipment

### Finned Tube Heat Exchangers

Air-side heat transfer on finned tubes uses modified correlations accounting for fin geometry. The Colburn j-factor approach:

j = St·Pr^(2/3) = (h/ρVcp)·Pr^(2/3)

For air with Pr ≈ 0.7:

Pr^(2/3) ≈ 0.788

This factor appears in all j-factor correlations for compact heat exchangers.

### Coil Performance

Air-side thermal resistance dominates in most HVAC coils. The overall heat transfer coefficient:

1/(UA) = 1/(ηₒh_air A_air) + R_wall + 1/(h_water A_water)

For typical values:
- Air side: h_air ≈ 50-150 W/m²·K (depends on Pr via Nu correlations)
- Water side: h_water ≈ 3000-10,000 W/m²·K

The Pr^(1/3) dependence in air-side Nu correlations directly affects coil thermal performance.

## Computational Considerations

When solving coupled momentum and energy equations (CFD analysis), the Prandtl number determines the relative resolution required for velocity and temperature fields:

**Turbulent Prandtl Number:**

Pr_t = ε_M/ε_H

Where ε_M is eddy viscosity and ε_H is eddy thermal diffusivity.

For air in turbulent HVAC flows: Pr_t ≈ 0.85-0.90

This differs slightly from the molecular Pr ≈ 0.71 and affects turbulence modeling in CFD simulations.

## Accuracy and Uncertainty

**Temperature Evaluation:**

Properties (including Pr) should be evaluated at the appropriate reference temperature:
- **Forced convection:** Film temperature T_f = (T_surface + T_bulk)/2
- **Natural convection:** Film temperature T_f = (T_surface + T_ambient)/2
- **High temperature differences:** Consider property variation corrections

**Property Variation Corrections:**

For large temperature differences (ΔT > 50°C), some correlations include correction factors:

Nu = Nu_constant_properties · (Pr_surface/Pr_bulk)^0.25

This accounts for property variation across the boundary layer.

## Comparison with Other Fluids

| Fluid | Temperature (°C) | Prandtl Number |
|-------|------------------|----------------|
| Air | 20 | 0.71 |
| Water | 20 | 7.0 |
| R-134a vapor | 20 | 0.85 |
| R-410A vapor | 20 | 0.78 |
| Engine oil | 20 | 10,400 |
| Liquid sodium | 200 | 0.0047 |

Air's Pr ≈ 0.7 is characteristic of diatomic gases and represents balanced momentum and thermal diffusion. Refrigerant vapors have similar Prandtl numbers (0.75-0.85), simplifying heat transfer analysis in vapor compression systems.

## Engineering Approximations

**Standard HVAC Calculations:**

For typical HVAC applications (-20°C to 60°C):
- **Use Pr = 0.71** as a constant
- Error < 2% across temperature range
- Simplifies hand calculations significantly

**High-Temperature Applications:**

For combustion air preheaters, boiler applications (200°C+):
- Use temperature-dependent Pr from tables
- Error reduction: 2-5% improvement in accuracy
- Necessary for precise thermal design

**Precision Heat Transfer Design:**

For critical applications (test equipment, calibration standards):
- Evaluate Pr at actual film temperature
- Consider property variation corrections
- Account for humidity effects on Pr (negligible below 50% RH)

## Summary for Design Engineers

The Prandtl number for air (~0.71) represents a fundamental physical property linking momentum and thermal transport. Key points:

1. **Nearly constant** over typical HVAC temperature ranges
2. **Appears in all** forced and natural convection correlations
3. **Typical exponent** of 1/3 in turbulent flow correlations
4. **Affects boundary layer** thickness ratios (thermal vs. velocity)
5. **Critical for accurate** heat exchanger and duct heat transfer calculations

For most HVAC design work, treating Pr as constant at 0.71 provides sufficient accuracy while simplifying calculations. Temperature-dependent values become important only for high-temperature applications or precision thermal analysis.
