---
title: "Forced Convection"
description: "Forced convection heat transfer fundamentals for HVAC systems including Reynolds, Nusselt, and Prandtl number correlations, internal and external flow equations, Dittus-Boelter and Sieder-Tate correlations, and convection coefficient calculations for heat exchangers"
weight: 1
---

Forced convection occurs when external mechanical means such as fans, pumps, or wind creates fluid motion over a surface or through a conduit. This mechanism dominates heat transfer in most HVAC applications including air handlers, fan coil units, heat exchangers, and all ducted air distribution systems.

## Fundamental Governing Parameters

Three dimensionless numbers characterize forced convection heat transfer behavior:

**Reynolds Number (Re)**

The Reynolds number quantifies the ratio of inertial forces to viscous forces in the fluid flow:

$$Re = \frac{\rho V D}{\mu} = \frac{V D}{\nu}$$

Where:
- ρ = fluid density (kg/m³)
- V = fluid velocity (m/s)
- D = characteristic length (hydraulic diameter for internal flow, m)
- μ = dynamic viscosity (Pa·s)
- ν = kinematic viscosity (m²/s)

Flow transitions from laminar to turbulent at Re ≈ 2300 for internal pipe flow and Re ≈ 500,000 for external flow over flat plates.

**Nusselt Number (Nu)**

The Nusselt number represents the ratio of convective to conductive heat transfer:

$$Nu = \frac{h D}{k}$$

Where:
- h = convection heat transfer coefficient (W/m²·K)
- D = characteristic length (m)
- k = thermal conductivity of fluid (W/m·K)

The Nusselt number is the primary output of convection correlations and directly determines the convection coefficient.

**Prandtl Number (Pr)**

The Prandtl number relates momentum diffusivity to thermal diffusivity:

$$Pr = \frac{\nu}{\alpha} = \frac{c_p \mu}{k}$$

Where:
- ν = kinematic viscosity (m²/s)
- α = thermal diffusivity (m²/s)
- c_p = specific heat at constant pressure (J/kg·K)

For air at standard conditions, Pr ≈ 0.71. For water at 20°C, Pr ≈ 7.0.

## Internal Flow Correlations

### Turbulent Flow in Pipes and Ducts

**Dittus-Boelter Equation**

The most widely used correlation for turbulent flow in smooth tubes with moderate temperature differences:

$$Nu = 0.023 Re^{0.8} Pr^n$$

Where:
- n = 0.4 for heating the fluid (T_surface > T_fluid)
- n = 0.3 for cooling the fluid (T_surface < T_fluid)

Valid for:
- Re > 10,000
- 0.7 < Pr < 160
- L/D > 10 (fully developed flow)

**Sieder-Tate Equation**

Provides improved accuracy for large temperature differences by accounting for viscosity variation:

$$Nu = 0.027 Re^{0.8} Pr^{1/3} \left(\frac{\mu}{\mu_s}\right)^{0.14}$$

Where:
- μ = dynamic viscosity at bulk fluid temperature (Pa·s)
- μ_s = dynamic viscosity at surface temperature (Pa·s)

Valid for:
- Re > 10,000
- 0.7 < Pr < 16,700
- L/D > 10

**Gnielinski Equation**

Modern correlation providing superior accuracy across wider Reynolds number range:

$$Nu = \frac{(f/8)(Re - 1000)Pr}{1 + 12.7(f/8)^{0.5}(Pr^{2/3} - 1)}$$

Where f is the Darcy friction factor from the Moody diagram or Colebrook equation.

Valid for:
- 3000 < Re < 5×10⁶
- 0.5 < Pr < 2000

### Laminar Flow in Pipes

For fully developed laminar flow with constant wall temperature:

$$Nu = 3.66$$

For fully developed laminar flow with constant heat flux:

$$Nu = 4.36$$

These constant values apply for Re < 2300 with L/D > 10.

### Entrance Region Effects

In the developing flow region near the entrance, heat transfer coefficients are higher than fully developed values. The thermal entrance length is:

$$L_t = 0.05 Re \cdot Pr \cdot D$$

For turbulent flow, entrance effects are typically negligible beyond 10-20 diameters.

## External Flow Correlations

### Flow Over Flat Plates

**Laminar Boundary Layer (Re < 500,000)**

$$Nu_x = 0.332 Re_x^{0.5} Pr^{1/3}$$

Where Nu_x and Re_x are evaluated at distance x from the leading edge.

Average Nusselt number over length L:

$$\overline{Nu}_L = 0.664 Re_L^{0.5} Pr^{1/3}$$

**Turbulent Boundary Layer (Re > 500,000)**

$$\overline{Nu}_L = 0.037 Re_L^{0.8} Pr^{1/3}$$

Valid for 0.6 < Pr < 60.

### Flow Across Tube Banks

For staggered and in-line tube arrangements common in finned coil heat exchangers:

$$Nu_D = C Re_D^m Pr^{0.36} \left(\frac{Pr}{Pr_s}\right)^{0.25}$$

Constants C and m depend on tube arrangement and Reynolds number range. Typical values for 10-row deep staggered arrangements with Re_D > 1000:

- C ≈ 0.27
- m ≈ 0.63

### Flow Over Cylinders

For cross-flow over single cylinders (representative of single tubes):

$$Nu_D = C Re_D^m Pr^{1/3}$$

| Re_D Range | C | m |
|------------|-------|------|
| 0.4-4 | 0.989 | 0.330 |
| 4-40 | 0.911 | 0.385 |
| 40-4,000 | 0.683 | 0.466 |
| 4,000-40,000 | 0.193 | 0.618 |
| 40,000-400,000 | 0.027 | 0.805 |

Valid for 0.7 < Pr < 500.

## Convection Coefficient Calculation Procedure

1. **Determine fluid properties** at the bulk temperature (average of inlet and outlet):
   - Density ρ
   - Specific heat c_p
   - Thermal conductivity k
   - Dynamic viscosity μ

2. **Calculate Reynolds number** using appropriate characteristic length

3. **Evaluate Prandtl number** from fluid properties

4. **Select appropriate correlation** based on geometry and flow regime

5. **Calculate Nusselt number** from the correlation

6. **Solve for convection coefficient**:

$$h = \frac{Nu \cdot k}{D}$$

## Typical Convection Coefficients for HVAC Applications

| Application | Fluid | Velocity | h (W/m²·K) |
|-------------|-------|----------|------------|
| Air in ducts | Air | 3-10 m/s | 10-40 |
| Air over finned coils | Air | 2-5 m/s | 25-65 |
| Air over bare tubes | Air | 3-8 m/s | 30-80 |
| Water in pipes | Water | 0.5-2 m/s | 500-3,000 |
| Water in shell-and-tube HX | Water | 1-3 m/s | 2,000-10,000 |
| Refrigerant liquid flow | R-410A | 0.3-1.5 m/s | 800-2,500 |
| Glycol solutions | 30% glycol | 0.5-2 m/s | 400-2,000 |
| Air over building surfaces | Air | 3-7 m/s | 20-50 |

These values represent single-phase forced convection without phase change. Condensation and evaporation produce significantly higher coefficients.

## Heat Exchanger Design Applications

For heat exchangers, convection coefficients on both fluid sides determine the overall heat transfer coefficient U:

$$\frac{1}{U} = \frac{1}{h_i} + R_{fouling} + \frac{t_{wall}}{k_{wall}} + \frac{1}{h_o}$$

Where:
- h_i = inside convection coefficient (W/m²·K)
- h_o = outside convection coefficient (W/m²·K)
- R_fouling = fouling resistance (m²·K/W)
- t_wall = wall thickness (m)
- k_wall = wall thermal conductivity (W/m·K)

The fluid side with lower convection coefficient controls overall performance. In air-to-water heat exchangers, the air side typically controls with h values 20-50 times lower than the water side.

## Enhancement Techniques

Several methods increase forced convection heat transfer:

**Velocity Increase**

Since h ∝ V^0.8 for turbulent flow, increasing velocity from 2 to 4 m/s increases h by approximately 74%. Pressure drop increases with V², requiring careful fan or pump power analysis.

**Turbulence Promotion**

Surface roughness, turbulators, and twisted tape inserts increase turbulence and Nusselt number by 50-200% at the cost of 2-4 times higher pressure drop.

**Extended Surfaces**

Fins on the low-h side increase effective area. Air-side fins in HVAC coils provide 10-20 times more surface area than the base tube area.

**Reduced Hydraulic Diameter**

For constant velocity, reducing hydraulic diameter increases Reynolds number and convection coefficient. Microchannel heat exchangers exploit this principle.

## Practical Considerations

**Temperature-Dependent Properties**

Fluid properties vary significantly with temperature. Evaluate properties at the film temperature for external flow:

$$T_{film} = \frac{T_s + T_\infty}{2}$$

For internal flow, use bulk temperature unless temperature difference exceeds 20°C, then apply the Sieder-Tate correction.

**Developing Flow Regions**

Standard correlations assume fully developed flow. Short tubes and ducts near inlets have higher local heat transfer coefficients. Account for entrance effects when L/D < 10.

**Non-Circular Ducts**

For rectangular or other non-circular ducts, use hydraulic diameter:

$$D_h = \frac{4A_c}{P}$$

Where A_c is cross-sectional area and P is wetted perimeter.

**Uncertainty in Correlations**

Empirical correlations typically have uncertainty of ±15-25%. Design heat exchangers with appropriate safety factors to account for this variability and fouling accumulation over time.

