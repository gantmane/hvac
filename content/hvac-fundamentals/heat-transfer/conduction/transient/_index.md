---
title: "Transient Conduction"
aliases: ["Transient Conduction"]
weight: 2
---

Transient conduction describes heat transfer when temperature varies with both position and time. This analysis is essential for HVAC applications including equipment startup, building thermal response, and thermal storage systems.

## Governing Equation

The general transient heat conduction equation:

$$\frac{\partial T}{\partial t} = \alpha \nabla^2 T + \frac{\dot{q}}{k}$$

Where:
- α = thermal diffusivity (m²/s)
- ∇² = Laplacian operator
- q̇ = internal heat generation per unit volume (W/m³)

## Thermal Diffusivity

Thermal diffusivity governs the rate of temperature propagation through a material:

$$\alpha = \frac{k}{\rho c_p}$$

**Physical Interpretation:**
- High α: rapid temperature response (metals)
- Low α: slow temperature response (insulation)

| Material | α (m²/s × 10⁻⁶) | Response Characteristic |
|----------|----------------|------------------------|
| Copper | 111 | Very rapid |
| Aluminum | 97 | Very rapid |
| Steel | 15 | Rapid |
| Concrete | 0.75 | Moderate |
| Brick | 0.52 | Slow |
| Wood | 0.14 | Very slow |
| Insulation | 0.03 | Extremely slow |

## Lumped Capacitance Method

The lumped capacitance approach assumes uniform temperature throughout an object at any instant. Valid when internal thermal resistance is negligible compared to external convective resistance.

### Governing Equation

Energy balance for a lumped system:

$$\rho V c_p \frac{dT}{dt} = -hA_s(T - T_\infty)$$

**Solution:**

$$\frac{T(t) - T_\infty}{T_i - T_\infty} = e^{-t/\tau}$$

Where the thermal time constant is:

$$\tau = \frac{\rho V c_p}{hA_s} = \frac{mc_p}{hA_s}$$

### Time Constant Significance

The time constant τ represents the time required for the temperature difference to decrease to 36.8% (1/e) of its initial value.

**Design Guidelines:**
- τ < 5 min: rapid response (thermostats, sensors)
- τ = 15-60 min: moderate response (hydronic terminal units)
- τ = 2-8 hr: slow response (building thermal mass)
- τ > 12 hr: very slow response (earth coupling)

## Biot Number

The Biot number determines the validity of the lumped capacitance assumption:

$$Bi = \frac{hL_c}{k} = \frac{\text{Internal conduction resistance}}{\text{External convection resistance}}$$

Where Lc is the characteristic length:

$$L_c = \frac{V}{A_s}$$

**Criteria:**
- Bi < 0.1: lumped capacitance valid (< 5% error)
- Bi < 0.05: excellent accuracy (< 2% error)
- Bi > 0.1: spatial temperature gradients significant

### HVAC Applications

| Application | Typical Bi | Analysis Method |
|-------------|-----------|-----------------|
| Thermostat bimetal | 0.01-0.05 | Lumped |
| Hydronic radiator fins | 0.1-0.5 | Spatial methods |
| Building walls | 1-100 | Full numerical |
| Underground pipes | 10-1000 | Full numerical |

## Fourier Number

The Fourier number is the dimensionless time parameter:

$$Fo = \frac{\alpha t}{L_c^2}$$

**Physical Meaning:**
- Ratio of heat conducted to heat stored
- Measures depth of thermal penetration
- Critical for transient analysis validity

## Heisler Charts

Heisler charts provide graphical solutions for one-dimensional transient conduction in simple geometries when Bi > 0.1.

### Available Geometries

**Plane Wall (thickness 2L):**

$$\frac{T(x,t) - T_\infty}{T_i - T_\infty} = f(Bi, Fo, x/L)$$

**Infinite Cylinder (radius ro):**

$$\frac{T(r,t) - T_\infty}{T_i - T_\infty} = f(Bi, Fo, r/r_o)$$

**Sphere (radius ro):**

$$\frac{T(r,t) - T_\infty}{T_i - T_\infty} = f(Bi, Fo, r/r_o)$$

### Chart Application Procedure

1. Calculate Biot number: Bi = hLc/k
2. Calculate Fourier number: Fo = αt/Lc²
3. Read centerline temperature from Chart 1
4. Read position correction from Chart 2 (if needed)
5. Read total heat transfer from Chart 3 (if needed)

### Limitations

- Constant properties
- Uniform initial temperature
- Constant surface conditions
- Fo > 0.2 for accuracy

## Semi-Infinite Solids

A semi-infinite solid extends infinitely in one direction. Valid when thermal penetration is small compared to physical dimensions.

### Penetration Depth

Approximate thermal penetration depth:

$$\delta \approx 2\sqrt{\alpha t}$$

**Criterion for Semi-Infinite Assumption:**

Physical dimension > 4√(αt)

### Constant Surface Temperature

For sudden change to surface temperature Ts:

$$\frac{T(x,t) - T_s}{T_i - T_s} = \text{erf}\left(\frac{x}{2\sqrt{\alpha t}}\right)$$

Where erf is the error function.

**Surface Heat Flux:**

$$q''_s(t) = \frac{k(T_s - T_i)}{\sqrt{\pi \alpha t}}$$

### Constant Surface Heat Flux

For imposed heat flux q''s:

$$T(x,t) - T_i = \frac{2q''_s\sqrt{\alpha t/\pi}}{k}\exp\left(-\frac{x^2}{4\alpha t}\right) - \frac{q''_s x}{k}\text{erfc}\left(\frac{x}{2\sqrt{\alpha t}}\right)$$

### Convective Boundary Condition

For convection to fluid at T∞:

$$\frac{T(x,t) - T_i}{T_\infty - T_i} = \text{erfc}\left(\frac{x}{2\sqrt{\alpha t}}\right) - \exp\left(\frac{hx}{k} + \frac{h^2\alpha t}{k^2}\right)\text{erfc}\left(\frac{x}{2\sqrt{\alpha t}} + \frac{h\sqrt{\alpha t}}{k}\right)$$

### HVAC Applications

**Ground Temperature Calculations:**
- Buried pipe analysis
- Earth-coupled heat exchangers
- Slab-on-grade heat loss
- Foundation heat transfer

**Validity Check:**
- Daily cycles: depth > 0.5 m typically valid
- Annual cycles: depth > 5 m typically valid

## Building Thermal Mass

Thermal mass describes the capacity of building materials to store and release heat, dampening temperature swings.

### Effective Thermal Mass

For periodic heating/cooling cycles:

$$\delta_m = \sqrt{\frac{\alpha P}{\pi}}$$

Where P is the period (24 hours for diurnal cycles).

**Effective Mass Depth:**

| Material | δm (mm) for 24-hr cycle |
|----------|------------------------|
| Concrete | 65 |
| Brick | 55 |
| Wood | 28 |
| Gypsum | 35 |

### Thermal Admittance

The ability of a surface to exchange heat with the environment:

$$Y = \sqrt{k\rho c_p \omega}$$

Where ω = 2π/P is the angular frequency.

### Decrement Factor

Ratio of output to input temperature amplitude:

$$f = \frac{|T_{\text{indoor amplitude}}|}{|T_{\text{outdoor amplitude}}|}$$

For massive construction: f = 0.2-0.4
For lightweight construction: f = 0.6-0.9

### Time Lag

Phase shift between outdoor and indoor temperature peaks:

$$\phi = \sqrt{\frac{P}{\pi \alpha}}L$$

**Design Implications:**
- High thermal mass: reduced peak loads, increased time lag
- Optimal for climates with large diurnal temperature swings
- Requires night ventilation or night setback for effectiveness

## Numerical Methods

For complex geometries and boundary conditions, numerical methods are required.

### Finite Difference Methods

Discretize space and time domains:

$$\frac{T_i^{n+1} - T_i^n}{\Delta t} = \alpha \frac{T_{i+1}^n - 2T_i^n + T_{i-1}^n}{(\Delta x)^2}$$

**Explicit Method:**
- Simple to implement
- Stability criterion: Fo ≤ 0.5

**Implicit Method:**
- Unconditionally stable
- Requires matrix solution
- Crank-Nicolson provides optimal accuracy

### Building Energy Simulation

Modern building simulation tools (EnergyPlus, TRNSYS) solve coupled transient equations:
- Multi-layer wall conduction
- Radiation exchange
- Convection boundaries
- Internal gains
- HVAC system interaction

## Components

- Lumped Capacitance Method
- Biot Number
- Fourier Number
- Heisler Charts
- Semi Infinite Solids
- Finite Difference Methods
- Crank Nicolson Method
- Explicit Methods
- Implicit Methods
- Alternating Direction Implicit
- Finite Element Methods
- Phase Change Problems
- Moving Boundary Problems
- Stefan Problem
