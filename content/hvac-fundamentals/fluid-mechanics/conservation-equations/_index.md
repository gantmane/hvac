---
title: "Conservation Equations"
description: "Fundamental conservation principles governing fluid flow in HVAC systems including continuity, momentum, and energy equations with engineering applications"
weight: 4
---

## Overview

Conservation equations form the mathematical foundation for analyzing fluid flow in HVAC systems. These equations express the physical laws of conservation of mass, momentum, and energy applied to fluid continua. Understanding these principles enables engineers to predict pressure drops, flow distributions, pump/fan power requirements, and thermal performance in piping networks, ductwork, and hydronic systems.

The three fundamental conservation laws govern all fluid flow phenomena:

1. Conservation of mass (continuity equation)
2. Conservation of momentum (Newton's second law)
3. Conservation of energy (first law of thermodynamics)

These equations can be expressed in differential form (for infinitesimal control volumes) or integral form (for finite control volumes). The choice depends on the analysis requirements and boundary conditions.

## Continuity Equation (Conservation of Mass)

The continuity equation states that mass cannot be created or destroyed within a control volume. For HVAC applications, this principle determines flow rates through system components and validates flow balancing.

### Differential Form

For a compressible fluid in three-dimensional Cartesian coordinates:

```
∂ρ/∂t + ∂(ρu)/∂x + ∂(ρv)/∂y + ∂(ρw)/∂z = 0
```

Or in vector notation:

```
∂ρ/∂t + ∇·(ρV) = 0
```

Where:
- ρ = fluid density (kg/m³)
- t = time (s)
- u, v, w = velocity components in x, y, z directions (m/s)
- V = velocity vector (m/s)
- ∇· = divergence operator

For incompressible flow (ρ = constant), the equation simplifies to:

```
∇·V = ∂u/∂x + ∂v/∂y + ∂w/∂z = 0
```

This simplified form applies to most liquid hydronic systems and low-velocity air distribution systems where density changes are negligible.

### Integral Form

For a control volume with multiple inlets and outlets:

```
d/dt ∫∫∫(CV) ρ dV + ∫∫(CS) ρ(V·n) dA = 0
```

For steady flow through a control volume:

```
Σ ṁ_in = Σ ṁ_out
```

Or equivalently:

```
Σ ρ_in A_in V_in = Σ ρ_out A_out V_out
```

Where:
- ṁ = mass flow rate (kg/s)
- A = cross-sectional area (m²)
- V = average velocity (m/s)
- n = outward normal unit vector

### HVAC Applications

**Duct System Analysis:**

For incompressible flow in circular ducts:

```
A₁V₁ = A₂V₂
(πD₁²/4)V₁ = (πD₂²/4)V₂
```

**Branch Flow Distribution:**

At a duct junction with one inlet and two outlets:

```
ṁ₁ = ṁ₂ + ṁ₃
ρA₁V₁ = ρA₂V₂ + ρA₃V₃
```

For air at constant density:

```
Q₁ = Q₂ + Q₃
```

Where Q = volumetric flow rate (m³/s or CFM)

**Practical Example:**

A 24-inch diameter main duct (Q = 8,000 CFM) branches into two 16-inch ducts. If one branch carries 5,000 CFM, the second branch must carry 3,000 CFM.

| Parameter | Main Duct | Branch 1 | Branch 2 |
|-----------|-----------|----------|----------|
| Diameter (in) | 24 | 16 | 16 |
| Flow Rate (CFM) | 8,000 | 5,000 | 3,000 |
| Velocity (FPM) | 2,546 | 3,579 | 2,148 |
| Area (ft²) | 3.14 | 1.40 | 1.40 |

## Momentum Equation (Conservation of Momentum)

The momentum equation is the fluid mechanics expression of Newton's second law: the rate of change of momentum equals the sum of forces acting on the fluid.

### Differential Form (Navier-Stokes Equations)

For a Newtonian, incompressible fluid with constant viscosity:

**x-direction:**
```
ρ(∂u/∂t + u∂u/∂x + v∂u/∂y + w∂u/∂z) = -∂p/∂x + μ(∂²u/∂x² + ∂²u/∂y² + ∂²u/∂z²) + ρgₓ
```

In vector form:
```
ρ(∂V/∂t + (V·∇)V) = -∇p + μ∇²V + ρg
```

Where:
- p = pressure (Pa)
- μ = dynamic viscosity (Pa·s)
- g = gravitational acceleration vector (m/s²)
- ∇² = Laplacian operator

The left side represents inertial forces (acceleration), while the right side includes pressure forces, viscous forces, and body forces.

### Euler Equations

For inviscid flow (μ = 0), the Navier-Stokes equations reduce to the Euler equations:

```
ρ(∂V/∂t + (V·∇)V) = -∇p + ρg
```

These equations apply to flow regions outside boundary layers where viscous effects are negligible.

### Integral Form (Momentum Theorem)

For a control volume:

```
Σ F = d/dt ∫∫∫(CV) ρV dV + ∫∫(CS) V(ρV·n) dA
```

For steady flow:

```
Σ F = Σ (ṁV)_out - Σ (ṁV)_in
```

The sum of forces equals the net momentum flux leaving the control volume.

### HVAC Applications

**Pressure Drop in Straight Ducts:**

The momentum equation combined with dimensional analysis yields the Darcy-Weisbach equation:

```
Δp = f (L/D) (ρV²/2)
```

Where:
- f = friction factor (dimensionless)
- L = duct length (m)
- D = hydraulic diameter (m)

**Force on Duct Bends:**

The momentum equation calculates forces on duct supports at bends:

```
F = ṁ(V₂ - V₁) + p₂A₂ - p₁A₁
```

For a 90-degree elbow with constant area:

```
F = ṁV√2 + (p₂ - p₁)A
```

**Hydronic System Pressure Drop:**

In piping systems, the momentum equation determines pump head requirements:

```
H_pump = Δp/(ρg) + Δz + h_L
```

Where:
- H_pump = pump head (m)
- Δz = elevation change (m)
- h_L = head loss due to friction (m)

## Energy Equation (Conservation of Energy)

The energy equation applies the first law of thermodynamics to fluid flow: energy cannot be created or destroyed, only converted between forms.

### Differential Form

For a compressible fluid with heat transfer and viscous dissipation:

```
ρ(∂e/∂t + V·∇e) = -p(∇·V) + ∇·(k∇T) + Φ
```

Where:
- e = specific internal energy (J/kg)
- k = thermal conductivity (W/m·K)
- T = temperature (K)
- Φ = viscous dissipation function (W/m³)

For most HVAC applications, viscous dissipation is negligible.

### Integral Form (Steady Flow Energy Equation)

For steady flow through a control volume with one inlet and one outlet:

```
Q̇ - Ẇ = ṁ[(h₂ - h₁) + (V₂² - V₁²)/2 + g(z₂ - z₁)]
```

Where:
- Q̇ = heat transfer rate (W)
- Ẇ = shaft work rate (W)
- h = specific enthalpy (J/kg)
- z = elevation (m)

Per unit mass flow:

```
q - w = Δh + ΔKE + ΔPE
```

### Mechanical Energy Equation

For incompressible flow without heat transfer, the energy equation reduces to:

```
(p₁/ρ + V₁²/2 + gz₁) + w_pump = (p₂/ρ + V₂²/2 + gz₂) + w_loss
```

Where:
- w_pump = pump/fan work per unit mass (J/kg)
- w_loss = friction loss per unit mass (J/kg)

Dividing by g yields the familiar head form:

```
H₁ + H_pump = H₂ + h_L
```

Where:
- H = total head = p/(ρg) + V²/(2g) + z (m)
- h_L = head loss (m)

### HVAC Applications

**Cooling Coil Analysis:**

Energy balance on a cooling coil:

```
Q̇_coil = ṁ_air(h_out - h_in) = ṁ_water c_p(T_in - T_out)
```

**Fan Power Requirements:**

The energy equation determines fan shaft power:

```
P_fan = ṁ(Δp/ρ)/η = Q·Δp/η
```

Where η = fan efficiency

**Pump Head Calculation:**

Total head required:

```
H_total = Δp_static/(ρg) + Δz + Σ h_L
```

| Component | Head Loss (ft) |
|-----------|----------------|
| Straight pipe | 12.5 |
| Fittings/valves | 8.2 |
| Coils | 15.0 |
| Control valve | 10.0 |
| Elevation change | 25.0 |
| **Total** | **70.7** |

## Bernoulli Equation

The Bernoulli equation is a simplified form of the energy equation for steady, inviscid, incompressible flow along a streamline.

### Derivation from Euler Equations

Starting with the Euler equation for steady flow:

```
(V·∇)V = -(1/ρ)∇p + g
```

For flow along a streamline with constant elevation:

```
V dV = -(dp/ρ)
```

Integrating:

```
V²/2 + p/ρ = constant
```

Including elevation changes:

```
p/ρ + V²/2 + gz = constant
```

### Standard Form

Between two points on a streamline:

```
p₁/ρ + V₁²/2 + gz₁ = p₂/ρ + V₂²/2 + gz₂
```

Dividing by g:

```
p₁/(ρg) + V₁²/(2g) + z₁ = p₂/(ρg) + V₂²/(2g) + z₂
```

Each term represents a form of head:
- p/(ρg) = pressure head (m)
- V²/(2g) = velocity head (m)
- z = elevation head (m)

### Modified Bernoulli Equation with Losses

For real fluids with friction:

```
p₁/(ρg) + V₁²/(2g) + z₁ = p₂/(ρg) + V₂²/(2g) + z₂ + h_L
```

### HVAC Applications

**Pitot Tube Velocity Measurement:**

For air flow measurement:

```
V = C√(2Δp/ρ)
```

Where C = pitot tube coefficient (typically 0.99-1.00)

For standard air (ρ = 1.204 kg/m³):

```
V (m/s) = 1.29√(Δp (Pa))
V (FPM) = 4005√(Δp (in. w.g.))
```

**Duct Pressure Relationships:**

Total pressure = static pressure + velocity pressure

```
p_t = p_s + p_v
p_t = p_s + ρV²/2
```

| Velocity (FPM) | Velocity Pressure (in. w.g.) |
|----------------|------------------------------|
| 1,000 | 0.062 |
| 1,500 | 0.140 |
| 2,000 | 0.249 |
| 2,500 | 0.389 |
| 3,000 | 0.560 |
| 4,000 | 0.996 |

**Venturi Flow Measurement:**

For a venturi meter:

```
Q = C A₂ √(2(p₁-p₂)/(ρ(1-(A₂/A₁)²)))
```

**Pump Selection:**

Static head difference:

```
Δh_static = (p₂-p₁)/(ρg) + (z₂-z₁)
```

Total head including velocity changes:

```
H_pump = Δh_static + (V₂²-V₁²)/(2g) + h_L
```

## Energy Line and Hydraulic Grade Line

Graphical representations of energy in flowing fluids provide visual insight into system hydraulic performance.

### Energy Line (EL)

The energy line represents total head at each point in the system:

```
EL = p/(ρg) + V²/(2g) + z
```

The EL always slopes downward in the direction of flow (except at pumps/fans) by an amount equal to friction losses.

### Hydraulic Grade Line (HGL)

The hydraulic grade line represents pressure head plus elevation:

```
HGL = p/(ρg) + z
```

The vertical distance between EL and HGL equals velocity head:

```
EL - HGL = V²/(2g)
```

### Characteristics

**Energy Line:**
- Decreases continuously except at pumps/fans
- Jump upward at pumps by amount equal to pump head
- Slope indicates head loss per unit length

**Hydraulic Grade Line:**
- Indicates piezometric head
- Can increase if velocity decreases (area expansion)
- Must remain above pipe centerline to avoid cavitation
- Jump upward at pumps by pump head minus velocity head change

### HVAC System Analysis

For hydronic piping:

| Location | Elevation (ft) | Velocity (ft/s) | Pressure (psig) | HGL (ft) | EL (ft) |
|----------|----------------|-----------------|-----------------|----------|---------|
| Pump inlet | 0 | 8.0 | 5.0 | 11.6 | 12.6 |
| Pump outlet | 0 | 8.0 | 55.0 | 127.0 | 128.0 |
| Riser bottom | 0 | 8.0 | 54.5 | 126.8 | 127.8 |
| Riser top | 100 | 8.0 | 11.7 | 127.0 | 128.0 |
| Coil inlet | 100 | 4.0 | 11.5 | 126.5 | 126.8 |
| Coil outlet | 100 | 4.0 | 5.2 | 112.0 | 112.2 |

**Design Implications:**

1. EL must provide adequate NPSH at pump inlet
2. HGL must remain above highest point in system to prevent air accumulation
3. Adequate pressure head required at terminal units for proper control valve operation
4. Expansion tank connection point should be at pump suction for optimal system pressurization

## References and Standards

**ASHRAE Handbooks:**
- ASHRAE Fundamentals, Chapter 3: Fluid Flow
- ASHRAE Fundamentals, Chapter 22: Pipe Sizing
- ASHRAE HVAC Systems and Equipment, Chapter 43: Centrifugal Pumps
- ASHRAE HVAC Systems and Equipment, Chapter 21: Fans

**Industry Standards:**
- ASME MFC-3M: Measurement of Fluid Flow in Pipes Using Orifice, Nozzle, and Venturi
- ISO 5167: Measurement of Fluid Flow by Means of Pressure Differential Devices
- AMCA 210: Laboratory Methods of Testing Fans for Certified Aerodynamic Performance Rating

**Design Guides:**
- Bell & Gossett System Syzer software (pump head calculations)
- SMACNA HVAC Systems Duct Design (friction loss methods)
- Crane TP-410: Flow of Fluids Through Valves, Fittings, and Pipe

## Design Considerations

**System Analysis Requirements:**

1. Identify control volumes with clear boundaries
2. Determine which conservation equations apply
3. Assess flow regime (laminar vs. turbulent, compressible vs. incompressible)
4. Account for all energy inputs/outputs and losses
5. Apply appropriate simplifications while maintaining accuracy

**Computational Approach:**

Modern HVAC design employs computational fluid dynamics (CFD) to solve conservation equations numerically for complex geometries. However, simplified analytical approaches using integral forms remain valuable for preliminary design and validation.

**Pressure Drop Calculations:**

Conservation of momentum governs pressure drop analysis. Total pressure drop includes:
- Friction losses in straight sections
- Minor losses at fittings, transitions, dampers
- Equipment pressure drops (coils, filters, terminals)

**Flow Distribution:**

Conservation of mass ensures proper flow balancing. Critical considerations:
- Branch pressure drops must be equal for balanced flow
- Balancing valves/dampers adjust individual branch resistances
- Main duct/pipe sizing affects branch pressure ratios

**Pump/Fan Sizing:**

Conservation of energy determines mechanical power requirements:
- Calculate total system head loss
- Add safety factors for uncertainties (typically 10-15%)
- Select equipment with adequate pressure rise at design flow
- Verify adequate NPSH for pump applications

**Validation Methods:**

1. Mass flow verification through flow measurement devices
2. Pressure traverse measurements confirm momentum predictions
3. Power consumption validates energy calculations
4. Thermal performance testing confirms heat transfer analysis

## Practical Engineering Applications

**Example 1: Duct System Design**

Given: 10,000 CFM through 200 ft of 24-inch round duct

Calculate pressure drop using conservation of momentum:

```
Δp = f (L/D) (ρV²/2)
V = Q/A = 10,000/(π(2)²/4) = 3,183 FPM = 16.2 ft/s
Re = ρVD/μ = 205,000 (turbulent)
f ≈ 0.018 (from Moody diagram for commercial steel)
Δp = 0.018 × (200/2) × (0.075 × 16.2²/2) = 1.77 lbf/ft² = 0.85 in. w.g.
```

**Example 2: Pump Head Calculation**

Chilled water system with:
- Flow rate: 500 GPM
- Static lift: 40 ft
- Pipe friction: 25 ft head
- Coil pressure drop: 15 ft head
- Control valve authority: 10 ft head

Total head required:

```
H_pump = 40 + 25 + 15 + 10 = 90 ft
```

Power requirement:

```
P = ρgQH/η = (62.4 × 500/449 × 90)/0.75 = 16.7 hp
```

**Example 3: Bernoulli Application**

Air flow measurement with pitot tube:
- Differential pressure: 0.25 in. w.g.
- Standard air density: 0.075 lbm/ft³

Velocity calculation:

```
V = 4005√(0.25) = 2,002 FPM
```

These examples demonstrate how conservation equations translate directly into design calculations for HVAC systems.

## Components

- [Continuity Equation Differential](continuity-equation-differential/)
- [Continuity Equation Integral](continuity-equation-integral/)
- [Momentum Equation Differential](momentum-equation-differential/)
- [Momentum Equation Integral](momentum-equation-integral/)
- [Energy Equation Differential](energy-equation-differential/)
- [Energy Equation Integral](energy-equation-integral/)
- [Navier Stokes Equations](navier-stokes-equations/)
- [Euler Equations](euler-equations/)
- [Bernoulli Equation Derivation](bernoulli-equation-derivation/)
- [Bernoulli Applications](bernoulli-applications/)
- [Energy Line](energy-line/)
- [Hydraulic Grade Line](hydraulic-grade-line/)
