---
title: "Correlations"
weight: 4
---

Convection correlations provide empirical relationships between dimensionless parameters to predict heat transfer coefficients. These correlations are derived from experimental data and dimensional analysis, enabling engineers to calculate convection heat transfer without solving the full governing equations.

## Dimensionless Parameters

Convection correlations relate dimensionless groups that characterize the physical phenomena.

### Nusselt Number

The Nusselt number represents the ratio of convective to conductive heat transfer:

Nu = hL/k

where:
- h = convection heat transfer coefficient (W/m²·K)
- L = characteristic length (m)
- k = thermal conductivity of fluid (W/m·K)

Nu = 1 indicates pure conduction. Higher values indicate enhanced heat transfer from convection.

### Reynolds Number

The Reynolds number characterizes flow regime:

Re = ρVL/μ = VL/ν

where:
- ρ = fluid density (kg/m³)
- V = velocity (m/s)
- μ = dynamic viscosity (Pa·s)
- ν = kinematic viscosity (m²/s)

Flow transitions:
- Re < 2300: Laminar flow in pipes
- 2300 < Re < 4000: Transition region
- Re > 4000: Turbulent flow in pipes
- Re < 5×10⁵: Laminar boundary layer on flat plates
- Re > 5×10⁵: Turbulent boundary layer

### Prandtl Number

The Prandtl number relates momentum diffusivity to thermal diffusivity:

Pr = ν/α = μcp/k

where:
- α = thermal diffusivity (m²/s)
- cp = specific heat (J/kg·K)

Typical values:
- Liquid metals: Pr ≈ 0.01
- Gases: Pr ≈ 0.7
- Water: Pr ≈ 7
- Oils: Pr ≈ 100-1000

### Grashof Number

The Grashof number characterizes natural convection:

Gr = gβ(Ts - T∞)L³/ν²

where:
- g = gravitational acceleration (9.81 m/s²)
- β = volumetric thermal expansion coefficient (1/K)
- Ts = surface temperature (K)
- T∞ = fluid temperature (K)

For ideal gases: β = 1/T (T in absolute temperature)

### Rayleigh Number

The Rayleigh number combines buoyancy and thermal effects:

Ra = Gr·Pr = gβ(Ts - T∞)L³/(να)

Natural convection regimes:
- Ra < 10⁹: Laminar natural convection
- Ra > 10⁹: Turbulent natural convection

### Stanton Number

The Stanton number relates heat transfer to thermal capacity:

St = h/(ρVcp) = Nu/(Re·Pr)

### Graetz Number

The Graetz number characterizes developing thermal flow:

Gz = (D/L)·Re·Pr

where D = pipe diameter, L = thermal entry length

## Correlation Selection Criteria

Selecting the appropriate correlation requires matching the physical configuration and flow conditions.

### Geometry Classification

| Geometry | Examples | Key Parameters |
|----------|----------|----------------|
| Internal flow | Pipes, ducts, tubes | Re, Pr, L/D |
| External flow | Cylinders, spheres, flat plates | Re, Pr, geometry |
| Natural convection | Vertical plates, enclosures | Ra, Pr, orientation |
| Mixed convection | Low-velocity forced flow | Gr/Re², Richardson number |
| Coils and bundles | Heat exchangers | Tube arrangement, pitch |

### Flow Regime Identification

Determine the flow regime before selecting a correlation:

1. Calculate Reynolds number
2. Identify laminar, transition, or turbulent flow
3. Check for developing vs. fully developed flow
4. Assess natural convection contribution (Gr/Re²)

### Property Evaluation

Most correlations require fluid properties at a reference temperature:

- Film temperature: Tf = (Ts + T∞)/2
- Bulk temperature: Tb = average fluid temperature
- Surface temperature: Ts (with property ratio corrections)

## Accuracy Ranges and Uncertainty

Correlations have validity ranges and inherent uncertainty.

### Typical Uncertainty Levels

| Correlation Type | Typical Uncertainty | Notes |
|------------------|---------------------|-------|
| Internal turbulent flow | ±10-15% | Well-established correlations |
| Internal laminar flow | ±5-10% | More predictable |
| External flow cylinders | ±15-25% | Geometry-dependent |
| Natural convection | ±20-30% | Sensitive to boundary conditions |
| Mixed convection | ±25-40% | Interaction effects |
| Boiling/condensation | ±30-50% | Highly complex phenomena |

### Validity Range Considerations

Operating outside correlation validity ranges leads to significant errors:

- Reynolds number range
- Prandtl number range
- Geometric constraints (L/D ratios, aspect ratios)
- Surface conditions (roughness, entrance effects)

## HVAC-Specific Correlations

HVAC applications involve characteristic geometries and operating conditions.

### Internal Flow in Ducts

**Gnielinski Correlation (Turbulent Flow in Smooth Pipes):**

Nu = (f/8)(Re - 1000)Pr / [1 + 12.7(f/8)^(1/2)(Pr^(2/3) - 1)]

Valid for:
- 0.5 < Pr < 2000
- 3000 < Re < 5×10⁶
- Fully developed flow

where f = (0.790 ln Re - 1.64)⁻² (Petukhov friction factor)

**Dittus-Boelter Equation (Simpler Alternative):**

Nu = 0.023 Re^(0.8) Pr^n

where:
- n = 0.4 for heating (Ts > Tb)
- n = 0.3 for cooling (Ts < Tb)

Valid for:
- 0.7 < Pr < 160
- Re > 10,000
- L/D > 10 (fully developed)

**Laminar Flow (Constant Surface Temperature):**

Nu = 3.66 (fully developed, circular tube)

**Laminar Flow (Constant Heat Flux):**

Nu = 4.36 (fully developed, circular tube)

### External Flow Over Tubes

**Churchill-Bernstein Correlation (Single Cylinder in Crossflow):**

Nu = 0.3 + [0.62 Re^(1/2) Pr^(1/3)] / [1 + (0.4/Pr)^(2/3)]^(1/4) × [1 + (Re/282,000)^(5/8)]^(4/5)

Valid for:
- Re·Pr > 0.2
- All Re values

**Zhukauskas Correlation (Alternative for Cylinders):**

Nu = C Re^m Pr^0.36 (Pr/Prs)^(1/4)

| Re Range | C | m |
|----------|---|---|
| 1-40 | 0.75 | 0.4 |
| 40-1000 | 0.51 | 0.5 |
| 1000-200,000 | 0.26 | 0.6 |
| 200,000-1,000,000 | 0.076 | 0.7 |

Valid for:
- 0.7 < Pr < 500
- 1 < Re < 10⁶

### Natural Convection on Vertical Surfaces

**Vertical Plate or Surface:**

Laminar (10⁴ < Ra < 10⁹):
Nu = 0.59 Ra^(1/4)

Turbulent (10⁹ < Ra < 10¹³):
Nu = 0.10 Ra^(1/3)

**Churchill-Chu Correlation (Entire Range):**

Nu = {0.825 + [0.387 Ra^(1/6)] / [1 + (0.492/Pr)^(9/16)]^(8/27)}²

Valid for: Ra < 10¹²

### Horizontal Surfaces

**Upper Surface of Hot Plate or Lower Surface of Cold Plate:**

Laminar (10⁴ < Ra < 10⁷):
Nu = 0.54 Ra^(1/4)

Turbulent (10⁷ < Ra < 10¹¹):
Nu = 0.15 Ra^(1/3)

**Lower Surface of Hot Plate or Upper Surface of Cold Plate:**

Nu = 0.27 Ra^(1/4) (10⁵ < Ra < 10¹⁰)

## Coil Correlations

Heat exchanger coils require specialized correlations accounting for tube arrangement and fin geometry.

### Bare Tube Bundles

**Tube Arrangement Factor:**

| Configuration | Correlation Multiplier |
|--------------|----------------------|
| Inline staggered | 1.0 (baseline) |
| Inline square | 0.8-0.9 |
| Staggered triangular | 1.0-1.1 |

**Grimison Correlation (Tube Banks in Crossflow):**

Nu = C₁ Re_max^m Pr^(1/3)

where Re_max uses maximum velocity in bundle.

Coefficients C₁ and m depend on:
- Tube arrangement (inline vs. staggered)
- Transverse pitch ratio (ST/D)
- Longitudinal pitch ratio (SL/D)
- Number of tube rows (NL ≥ 10 for fully developed)

### Finned Tube Coils

**Effectiveness Considerations:**

Fin efficiency reduces effective heat transfer:

ηf = tanh(mL) / (mL)

where m = √(hP/kA), P = fin perimeter, A = fin cross-section

Overall surface efficiency:

ηo = 1 - (Af/A)(1 - ηf)

**Rich Correlation (Plate Fin-Tube Heat Exchangers):**

j = 0.14 Re_Dc^(-0.328) (ST/SL)^(-0.502) (Fp/Dc)^(0.031)

where:
- j = Colburn j-factor = St·Pr^(2/3)
- Re_Dc = Reynolds number based on tube collar diameter
- ST = transverse tube spacing
- SL = longitudinal tube spacing
- Fp = fin pitch

Valid for:
- 500 < Re_Dc < 8000
- Typical HVAC coil geometries

## Mixed Convection

Mixed convection occurs when both forced and natural convection are significant.

### Richardson Number

The Richardson number quantifies the relative importance:

Ri = Gr/Re² = (buoyancy forces)/(inertial forces)

Classification:
- Ri < 0.1: Forced convection dominates
- 0.1 < Ri < 10: Mixed convection
- Ri > 10: Natural convection dominates

### Horizontal Tubes

For horizontal tubes with internal flow:

Nu_mixed³·⁵ = Nu_forced³·⁵ ± Nu_natural³·⁵

Use + for assisting flow (same direction), - for opposing flow.

### Vertical Tubes

**Assisting Flow (buoyancy aids forced flow):**

Nu_mixed = Nu_forced + Nu_natural

**Opposing Flow (buoyancy opposes forced flow):**

More complex; use specialized correlations or computational methods.

### Combined Correlation Approach

For general mixed convection:

Nu = [Nu_forced^n ± Nu_natural^n]^(1/n)

where n = 3 to 4 depending on geometry.

## Application Procedure

1. **Identify geometry and flow configuration**
2. **Calculate characteristic length and velocity**
3. **Determine fluid properties at appropriate temperature**
4. **Calculate dimensionless parameters (Re, Pr, Gr, Ra)**
5. **Classify flow regime and convection mode**
6. **Select appropriate correlation within validity range**
7. **Calculate Nusselt number**
8. **Determine heat transfer coefficient: h = Nu·k/L**
9. **Verify assumptions and check validity ranges**
10. **Estimate uncertainty based on correlation type**

## Property Temperature Corrections

Temperature-dependent property variations affect correlation accuracy.

### Viscosity Correction

For large temperature differences:

Nu = Nu₀(μb/μs)^n

where:
- μb = viscosity at bulk temperature
- μs = viscosity at surface temperature
- n ≈ 0.14 for heating, 0.25 for cooling

### Prandtl Number Correction

Some correlations include (Pr/Prs)^(1/4) terms to account for property variation between bulk and surface.

## Components

- Nusselt Number Definitions
- Prandtl Number Effects
- Reynolds Number Regimes
- Churchill Bernstein Correlation
- Zhukauskas Correlation
- Whitaker Correlation
- Ranz Marshall Correlation
- Dimensional Analysis
- Buckingham Pi Theorem
