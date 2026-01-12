---
title: "External Flow"
description: "Comprehensive analysis of external flow over bodies including drag forces, boundary layer effects, flow separation, and applications to HVAC equipment design including cooling towers, heat exchangers, and outdoor air handling systems"
weight: 7
---

External flow refers to fluid flow over solid bodies where the boundary layer develops along the surface but does not fill the entire flow domain. Unlike internal flow confined within ducts and pipes, external flow problems involve unbounded fluid domains where the flow field extends to infinity. External flow analysis is critical for HVAC applications including cooling tower fill design, heat exchanger tube bank arrangements, outdoor equipment aerodynamics, and building wind effects.

## Fundamental Concepts

### Flow Regimes

External flow exhibits distinct regimes based on Reynolds number:

**Reynolds Number Definition:**
Re = ρVL/μ = VL/ν

Where:
- ρ = fluid density (lbm/ft³ or kg/m³)
- V = freestream velocity (ft/s or m/s)
- L = characteristic length (ft or m)
- μ = dynamic viscosity (lbm/ft·s or Pa·s)
- ν = kinematic viscosity (ft²/s or m²/s)

**Flow Regime Classification:**

| Reynolds Number | Flow Regime | Characteristics |
|-----------------|-------------|-----------------|
| Re < 5 × 10⁵ | Laminar | Smooth boundary layer, low drag |
| 5 × 10⁵ < Re < 10⁶ | Transition | Boundary layer transitions to turbulent |
| Re > 10⁶ | Turbulent | Fully turbulent boundary layer, higher drag |

### Boundary Layer Development

The boundary layer represents the thin region adjacent to the surface where viscous effects dominate. Velocity increases from zero at the wall (no-slip condition) to the freestream velocity at the boundary layer edge.

**Boundary Layer Thickness:**

For flat plate laminar flow:
δ = 5x/√Re_x = 5x√(ν/Vx)

For flat plate turbulent flow (Re_x > 5 × 10⁵):
δ = 0.37x/Re_x^(1/5)

Where x is the distance from the leading edge.

**Displacement Thickness:**
δ* = ∫₀^∞ (1 - u/U) dy

This represents how far the external streamlines are displaced due to boundary layer growth.

**Momentum Thickness:**
θ = ∫₀^∞ (u/U)(1 - u/U) dy

Critical parameter for calculating skin friction drag.

## Drag Forces

Drag force consists of two primary components: friction drag from viscous shear stress and pressure drag from pressure distribution asymmetry.

### Total Drag Force

**Drag Force Equation:**
F_D = C_D A (ρV²/2)

Where:
- F_D = drag force (lbf or N)
- C_D = drag coefficient (dimensionless)
- A = reference area (ft² or m²)
- ρ = fluid density (lbm/ft³ or kg/m³)
- V = freestream velocity (ft/s or m/s)

The factor (ρV²/2) represents the dynamic pressure of the flow.

### Friction Drag

Friction drag results from viscous shear stress acting tangentially along the surface. For laminar boundary layers, friction drag dominates. Streamlined bodies experience primarily friction drag.

**Local Skin Friction Coefficient (Laminar):**
C_f,x = 0.664/√Re_x

**Average Skin Friction Coefficient (Laminar, Flat Plate):**
C_f,avg = 1.328/√Re_L

**Average Skin Friction Coefficient (Turbulent, Flat Plate):**
C_f,avg = 0.074/Re_L^(1/5) (5 × 10⁵ < Re_L < 10⁷)

C_f,avg = 0.455/(log Re_L)^2.58 (Re_L > 10⁷)

### Pressure Drag

Pressure drag arises from asymmetric pressure distribution around the body, caused by flow separation and wake formation. Bluff bodies experience significant pressure drag.

**Pressure Coefficient:**
C_p = (p - p_∞)/(ρV²/2)

Where p is local pressure and p_∞ is freestream pressure.

Pressure drag force:
F_D,pressure = ∫∫_surface C_p (ρV²/2) n_x dA

Where n_x is the component of surface normal in the flow direction.

### Form Drag

Form drag represents the pressure drag component attributed to body shape. Streamlined shapes minimize form drag by preventing or delaying flow separation.

**Drag Coefficient Values for Common Shapes:**

| Geometry | Orientation | Re Range | C_D |
|----------|-------------|----------|-----|
| Flat plate | Perpendicular to flow | > 10³ | 1.28 - 2.0 |
| Flat plate | Parallel to flow | 10⁴ - 10⁵ | 0.001 - 0.005 |
| Circular cylinder | Crossflow | 10³ - 10⁵ | 1.0 - 1.2 |
| Circular cylinder | Crossflow | > 10⁶ | 0.3 - 0.5 |
| Sphere | - | 10³ - 10⁵ | 0.4 - 0.5 |
| Sphere | - | > 10⁶ | 0.1 - 0.2 |
| Streamlined body (3:1) | Aligned | 10⁴ - 10⁶ | 0.04 - 0.10 |
| Hemisphere | Hollow facing flow | > 10⁴ | 1.42 |
| Hemisphere | Hollow facing downstream | > 10⁴ | 0.38 |

Reference area A is typically frontal area for bluff bodies and planform area for streamlined bodies.

## Flow Separation

Flow separation occurs when the boundary layer detaches from the surface due to adverse pressure gradient (pressure increasing in flow direction). Separation creates recirculation zones and large wakes, dramatically increasing pressure drag.

### Separation Mechanism

Adverse pressure gradient (dp/dx > 0) causes flow deceleration in the boundary layer. Near-wall fluid particles have insufficient momentum to overcome the pressure rise and reverse direction, causing separation.

**Separation Criterion:**
At separation point: ∂u/∂y|_wall = 0 and τ_wall = 0

### Wake Formation

Behind separated flow regions, low-pressure recirculating wakes form. Wake width and intensity directly correlate with pressure drag magnitude.

**Wake Characteristics:**
- Velocity deficit region downstream of body
- Vortex shedding for certain geometries (Strouhal number: St = fD/V)
- Turbulent mixing and energy dissipation
- Pressure recovery in far wake

**Vortex Shedding Frequency:**

For circular cylinders (300 < Re < 3 × 10⁵):
f = StV/D

Where Strouhal number St ≈ 0.21 for circular cylinders.

Vortex shedding can cause acoustic noise and structural vibration in heat exchanger tube banks and outdoor equipment.

### Boundary Layer Separation

Separation point location depends on:
- Body geometry (curvature, surface roughness)
- Reynolds number
- Pressure gradient magnitude
- Boundary layer state (laminar vs. turbulent)

Turbulent boundary layers resist separation better than laminar layers due to enhanced momentum transport. This explains the drag crisis on spheres and cylinders at Re ≈ 3 × 10⁵.

### Adverse Pressure Gradient

Pressure gradient parameter:
Λ = (θ²/ν)(dp/dx)

Positive values indicate adverse gradient. Separation occurs when boundary layer cannot sustain adverse gradient.

**Separation Prediction (Laminar Flow):**
Falkner-Skan solutions predict separation for pressure gradient parameter values.

**Turbulent Flow:**
Separation delayed compared to laminar due to higher momentum transport. Empirical correlations and CFD typically required.

### Streamlining Effects

Streamlining reduces drag by:
1. Delaying or preventing separation
2. Reducing wake size
3. Minimizing form drag
4. Gradually recovering pressure

**Fineness Ratio:**
FR = L/D

Where L is body length and D is maximum diameter.

Optimal fineness ratio for minimum drag: FR ≈ 2.5 - 4.0 for axisymmetric bodies.

## HVAC Applications

### Heat Exchanger Design

**Tube Bank Flow:**

External flow over tube banks in shell-and-tube heat exchangers and finned coil heat exchangers exhibits complex patterns:

- Staggered vs. inline arrangements affect drag and heat transfer
- First row experiences lower drag coefficient
- Downstream rows experience increased turbulence
- Pressure drop correlates with number of tube rows

**Tube Bank Drag Coefficient:**

For staggered tubes (10 or more rows):
C_D = C_D,∞ [1 + (N - 10)/10]

Where C_D,∞ is fully developed drag coefficient and N is number of rows.

**Finned Tube Design:**

External flow over fins requires analysis of:
- Fin efficiency reduction due to flow separation
- Optimal fin spacing for minimum drag at required heat transfer
- Frost accumulation effects on aerodynamic performance
- Louver and slit fin designs to enhance mixing

### Cooling Tower Fill

Cooling tower fill design directly applies external flow principles:

**Film Fill:** Water flows as thin film over closely-spaced sheets. Air flows in crossflow or counterflow configuration. External flow drag determines air-side pressure drop.

**Splash Fill:** Falling water droplets experience external flow drag. Terminal velocity:

V_terminal = √(4gD(ρ_water - ρ_air)/(3C_D ρ_air))

For water droplets (D = 3-5 mm), C_D ≈ 0.4-0.5, yielding V_terminal ≈ 20-25 ft/s.

**Fill Pressure Drop:**

Δp = C_K (ρV²/2) (Z/L_char)

Where:
- C_K = loss coefficient (empirical, 30-80 for splash fill, 50-120 for film fill)
- Z = fill depth (ft or m)
- L_char = characteristic length (ft or m)

### Outdoor Equipment Aerodynamics

Wind effects on rooftop units, cooling towers, and condensing units:

**Wind Loading:**

Design wind pressure:
q_z = 0.00256K_z K_zt K_d V² (psf)

Where V is wind speed (mph) and K factors account for height, topography, and directionality per ASCE 7.

Total wind force:
F = q_z G C_f A_f

Where:
- G = gust effect factor
- C_f = force coefficient (0.8-2.0 for rectangular equipment)
- A_f = projected area

**Air Recirculation:**

Rooftop equipment placement must prevent exhaust air entrainment. External flow analysis determines separation zones and recirculation regions.

ASHRAE 90.1 requires minimum separation distances based on equipment capacity and wind patterns.

### Air-Cooled Condenser Coils

External airflow over condenser coils involves:

**Coil Face Velocity:**
V_face = CFM/A_face (fpm)

Typical range: 300-800 fpm for optimal balance between heat transfer and pressure drop.

**Coil Pressure Drop:**

Δp_coil = K_coil (ρV²/2) (N_rows)

Where K_coil depends on fin spacing, fin type, and Reynolds number.

**Fouling Effects:**

Dirt and debris accumulation increases effective fin thickness, promoting earlier separation and increasing form drag. Pressure drop can increase 50-150% before cleaning.

### Building-Integrated Systems

External flow affects building-mounted HVAC equipment:

- Exhaust stack dispersion and dilution
- Fresh air intake contamination risk
- Louver performance in wind
- Penthouse pressurization

**Stack Exit Velocity:**

Minimum exit velocity to prevent downdraft:
V_exit > 1.5V_wind

Per ASHRAE 62.1, stack height and exit velocity must ensure adequate dispersion.

## Design Considerations

### Reynolds Number Effects

Design must account for Reynolds number variation:

1. Startup transients (low Re, high drag)
2. Part-load operation (reduced velocities)
3. Temperature effects on fluid properties (viscosity changes)
4. Altitude effects (density variation)

### Surface Roughness

Roughness elements trip boundary layer to turbulence, affecting drag:

**Roughness Reynolds Number:**
Re_k = Vk/ν

Where k is roughness height.

Fully rough regime when Re_k > 70-100. In this regime, drag coefficient becomes independent of Reynolds number.

**Frost and Fouling:**

Surface contamination increases roughness:
- Enhanced turbulence (beneficial for heat transfer)
- Increased friction drag (detrimental to pressure drop)
- Altered separation point (may increase or decrease form drag)

Regular maintenance critical for design performance.

### Turbulence Intensity

Freestream turbulence affects:
- Transition Reynolds number (higher turbulence reduces Re_crit)
- Separation point (turbulence delays separation)
- Heat transfer coefficient (turbulence enhances mixing)

**Turbulence Intensity:**
Tu = u'/V

Where u' is RMS velocity fluctuation.

Outdoor equipment: Tu = 5-15%
Indoor ducted flow: Tu = 1-5%

### Vibration and Acoustics

Vortex shedding causes periodic forces:

**Lift Coefficient Fluctuation:**
C_L(t) = C_L,max sin(2πft)

For circular cylinders at Re = 10⁴-10⁵: C_L,max ≈ 0.3-0.5

**Acoustic Power:**

Sound pressure level from vortex shedding:
SPL ≈ 10 log(ρV⁵D²/r²) + constant

Mitigation strategies:
- Streamlining to prevent vortex formation
- Helical strakes on large diameter components
- Vibration isolation mounts
- Acoustic treatment in air path

### Computational Considerations

CFD analysis for complex external flow:

**Mesh Requirements:**
- y⁺ < 1 for wall-resolved LES/DNS
- 30 < y⁺ < 300 for wall-function RANS
- Structured prismatic layers near walls
- Sufficient domain extent (10-20 body lengths downstream)

**Turbulence Modeling:**
- k-ε: Economical, reasonable for attached flow
- k-ω SST: Better separation prediction
- LES: High accuracy for unsteady effects, computationally expensive

## Codes and Standards

**ASHRAE Fundamentals:**
- Chapter 4: Heat Transfer
- Chapter 21: Duct Design (external pressure losses)

**ASHRAE 62.1:**
- Section 5.4: Exhaust system design
- Appendix C: Stack exit velocity requirements

**ASCE 7:**
- Chapter 29: Wind loads on building appurtenances

**ASME PTC 51:**
- Cooling tower performance testing (fill drag characteristics)

**CTI Standards:**
- Fill design and performance certification
- Drift eliminator drag testing

## Performance Optimization

### Drag Reduction Strategies

1. Streamline body shapes (minimize bluff regions)
2. Add trip wires to force turbulent boundary layer (reduces form drag at expense of friction drag)
3. Optimize fin spacing and geometry
4. Use dimpled or textured surfaces selectively
5. Implement vortex generators upstream of separation-prone regions

### Heat Transfer Enhancement

External flow modifications to enhance heat transfer:
- Turbulators and surface roughness (increased turbulence)
- Wing-shaped vortex generators (streamwise vortices)
- Oval and flattened tubes (reduced form drag)
- Louvered fins (boundary layer interruption)

### Economic Balance

Optimal design minimizes total cost:
- Capital cost: Equipment size, material
- Operating cost: Fan/pump power to overcome drag
- Maintenance cost: Cleaning frequency

**Life Cycle Cost Analysis:**

Total cost = Initial cost + NPV(Energy cost + Maintenance cost)

Drag reduction may justify higher initial cost through energy savings.

## Measurement and Testing

**Drag Force Measurement:**
- Force balance (direct measurement)
- Wake survey (momentum deficit method)
- Pressure integration (surface pressure taps)

**Wind Tunnel Testing:**

Scale model requirements:
- Geometric similarity
- Reynolds number similarity (often relaxed)
- Froude number matching for free surface flows

Blockage correction when model area > 5% of tunnel cross-section.

**Field Testing:**

Per AMCA 210 and ASHRAE 51, external static pressure measurements must account for velocity pressure effects:

P_total = P_static + P_velocity

Where P_velocity = ρV²/2

## Practical Examples

**Example 1: Rooftop Unit Wind Load**

Calculate wind drag force on rooftop unit:
- Dimensions: 10 ft × 6 ft × 4 ft (L × W × H)
- Design wind speed: 90 mph (132 ft/s)
- Air density: 0.075 lbm/ft³

Frontal area: A = 6 × 4 = 24 ft²
Dynamic pressure: q = 0.075 × 132²/2 = 653.4 lbf/ft²
Drag coefficient: C_D ≈ 1.3 (rectangular shape)

Drag force: F_D = 1.3 × 24 × 653.4/32.2 = 632 lbf

This force must be resisted by structural supports and anchorage.

**Example 2: Cooling Tower Drift Eliminator Pressure Drop**

Calculate pressure drop across drift eliminator:
- Face velocity: 600 fpm (10 ft/s)
- Air density: 0.070 lbm/ft³
- Eliminator loss coefficient: K = 2.5

Δp = 2.5 × (0.070 × 10²/2) / 32.2 = 0.273 lbf/ft² = 0.078 in. H₂O

This contributes to total cooling tower static pressure requirement.

## Conclusion

External flow analysis provides the foundation for designing aerodynamically efficient HVAC equipment. Understanding drag mechanisms, boundary layer behavior, and flow separation enables engineers to optimize heat exchanger performance, minimize fan power consumption, and ensure structural adequacy of outdoor equipment. Application of external flow principles, combined with empirical correlations and computational tools, yields designs that balance thermal performance, pressure drop, and cost-effectiveness throughout the equipment lifecycle.
