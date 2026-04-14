---
title: "General External Flow Principles"
aliases: ["General External Flow Principles"]
description: "Comprehensive analysis of external flow mechanics including drag forces, boundary layer development, flow separation, and heat transfer correlations for HVAC applications including cooling towers, air-cooled condensers, and building aerodynamics"
weight: 1
---

## Overview

External flow refers to fluid motion over bodies immersed in an unbounded fluid stream. In HVAC systems, external flow phenomena govern the performance of air-cooled heat exchangers, cooling towers, outdoor air intakes, rooftop equipment, and building envelope interactions with wind. Understanding drag forces, boundary layer behavior, and convective heat transfer coefficients is essential for accurate equipment selection, proper installation clearances, and performance prediction under varying environmental conditions.

The fundamental distinction between external and internal flow lies in boundary layer development. In external flow, the boundary layer grows from the leading edge but never fills the entire flow domain, leaving a core region of inviscid flow. This contrasts with internal flow where viscous effects eventually dominate the entire cross-section once fully developed flow is established.

## Fundamental Flow Regimes

External flow behavior is characterized by the Reynolds number based on characteristic length:

**Reynolds Number Definition:**

Re_L = (ρ U_∞ L) / μ = (U_∞ L) / ν

Where:
- ρ = fluid density (kg/m³)
- U_∞ = freestream velocity (m/s)
- L = characteristic length (m)
- μ = dynamic viscosity (Pa·s)
- ν = kinematic viscosity (m²/s)

| Flow Regime | Reynolds Number Range | Characteristics | HVAC Examples |
|-------------|----------------------|-----------------|---------------|
| Laminar | Re < 5×10⁵ | Smooth streamlines, low drag | Small diameter tubes, low velocity |
| Transition | 5×10⁵ < Re < 4×10⁶ | Intermittent turbulence | Variable speed fans, seasonal conditions |
| Turbulent | Re > 4×10⁶ | Chaotic motion, high mixing | Cooling towers, outdoor units, wind on buildings |

## Boundary Layer Development

The boundary layer is the thin region near a surface where viscous effects are significant. For flow over a flat plate, the boundary layer thickness grows as:

**Laminar Boundary Layer Thickness:**

δ / x = 5.0 / √(Re_x)

Where Re_x = (U_∞ x) / ν

**Turbulent Boundary Layer Thickness:**

δ / x = 0.37 / (Re_x)^(1/5)

**Displacement Thickness:**

The displacement thickness (δ*) represents the distance by which external streamlines are displaced due to boundary layer velocity deficit:

δ* / x = 1.72 / √(Re_x)  (laminar)

δ* / x = 0.046 / (Re_x)^(1/5)  (turbulent)

**Momentum Thickness:**

θ / x = 0.664 / √(Re_x)  (laminar)

θ / x = 0.036 / (Re_x)^(1/5)  (turbulent)

## Drag Force Fundamentals

Drag is the component of force on a body parallel to the flow direction. Total drag consists of friction drag (viscous shear) and pressure drag (form drag).

**Total Drag Force:**

F_D = C_D (1/2) ρ U_∞² A

Where:
- C_D = drag coefficient (dimensionless)
- A = frontal area (m²) or planform area depending on application
- ρ = fluid density (kg/m³)
- U_∞ = freestream velocity (m/s)

**Drag Coefficient Components:**

C_D = C_Df + C_Dp

Where:
- C_Df = friction drag coefficient
- C_Dp = pressure drag coefficient

### Friction Drag

Friction drag results from viscous shear stress at the surface. For a flat plate aligned with flow:

**Laminar Flat Plate (Re_L < 5×10⁵):**

C_Df = 1.328 / √(Re_L)

**Turbulent Flat Plate (5×10⁵ < Re_L < 10⁷):**

C_Df = 0.074 / (Re_L)^(1/5)

**Turbulent Flat Plate (10⁷ < Re_L < 10⁹):**

C_Df = 0.455 / (log₁₀ Re_L)^2.58

**Mixed Boundary Layer (Transition at Re_c):**

C_Df = 0.074 / (Re_L)^(1/5) - 1742 / Re_L

This correlation assumes transition at Re_c = 5×10⁵.

### Pressure Drag (Form Drag)

Pressure drag dominates for blunt bodies and results from flow separation creating a low-pressure wake region. Streamlined shapes minimize separation and pressure drag.

**Pressure Distribution Parameter:**

C_p = (p - p_∞) / (1/2 ρ U_∞²)

Where:
- p = local static pressure (Pa)
- p_∞ = freestream static pressure (Pa)

## Flow Separation and Wake Formation

Flow separation occurs when the boundary layer detaches from the surface, typically caused by an adverse pressure gradient (dp/dx > 0). Separation creates a wake region with recirculating flow and elevated pressure drag.

**Separation Criteria:**

Separation occurs when the wall shear stress becomes zero:

τ_w = μ (∂u/∂y)|_(y=0) = 0

**Adverse Pressure Gradient:**

An adverse pressure gradient exists when pressure increases in the flow direction:

dp/dx > 0

This decelerates the boundary layer. Near-wall fluid with low momentum cannot overcome the pressure rise and reverses direction, causing separation.

**Wake Characteristics:**

- Low pressure region behind body
- Recirculating flow
- High turbulence intensity
- Periodic vortex shedding (von Kármán vortex street)

**Vortex Shedding Frequency (Strouhal Number):**

St = (f L) / U_∞ ≈ 0.20

Where:
- f = vortex shedding frequency (Hz)
- L = characteristic dimension perpendicular to flow (m)

## Drag Coefficients for Common Geometries

| Geometry | Orientation | Reynolds Number | Drag Coefficient C_D |
|----------|-------------|-----------------|---------------------|
| Sphere | - | Re < 1 | 24/Re (Stokes flow) |
| Sphere | - | 10³ < Re < 2×10⁵ | 0.40 - 0.47 |
| Sphere | - | Re > 4×10⁵ | 0.10 (supercritical) |
| Circular cylinder | Perpendicular | 10³ < Re < 2×10⁵ | 1.0 - 1.2 |
| Circular cylinder | Perpendicular | Re > 4×10⁵ | 0.3 |
| Circular cylinder | Parallel | - | 0.01 - 0.02 |
| Square cylinder | Face normal | - | 2.0 - 2.2 |
| Square cylinder | Diagonal | - | 1.5 - 1.6 |
| Flat plate | Perpendicular | - | 1.17 |
| Flat plate | Parallel | See friction drag | - |
| Hemisphere | Hollow upstream | - | 1.42 |
| Hemisphere | Hollow downstream | - | 0.38 |
| Streamlined airfoil | α = 0° | - | 0.04 - 0.10 |
| Cube | Face normal | - | 1.05 |
| Rectangular building | L/W = 2 | - | 1.3 - 1.5 |
| Cooling tower (round) | - | - | 0.6 - 0.8 |

## Lift Force

Lift is the force component perpendicular to the freestream direction, generated by asymmetric pressure distribution.

**Lift Force:**

F_L = C_L (1/2) ρ U_∞² A

Where:
- C_L = lift coefficient (dimensionless)
- A = planform area (m²)

**Lift Coefficient for Airfoil:**

C_L = 2π sin(α)  (thin airfoil theory, small α)

Where α = angle of attack (radians)

**Circulation Theory (Kutta-Joukowski Theorem):**

L' = ρ U_∞ Γ

Where:
- L' = lift per unit span (N/m)
- Γ = circulation (m²/s)

## Heat Transfer in External Flow

Convective heat transfer from surfaces in external flow is critical for air-cooled heat exchanger performance, condensing unit capacity, and building heat loss calculations.

**Newton's Law of Cooling:**

q" = h (T_s - T_∞)

Where:
- q" = heat flux (W/m²)
- h = convective heat transfer coefficient (W/m²·K)
- T_s = surface temperature (K)
- T_∞ = freestream temperature (K)

**Total Heat Transfer:**

Q = h A (T_s - T_∞)

### Dimensionless Numbers

**Nusselt Number:**

Nu = hL / k

Represents the ratio of convective to conductive heat transfer.

**Prandtl Number:**

Pr = ν / α = (c_p μ) / k

Represents the ratio of momentum diffusivity to thermal diffusivity.

For air at typical HVAC conditions: Pr ≈ 0.7

**Reynolds Analogy:**

For turbulent flow with Pr ≈ 1:

St = C_f / 2

Where St = Nu / (Re Pr) is the Stanton number.

### Flat Plate Heat Transfer Correlations

**Laminar Flow (Re_L < 5×10⁵, Pr ≥ 0.6):**

Nu_L = 0.664 Re_L^(1/2) Pr^(1/3)

**Local Nusselt Number (Laminar):**

Nu_x = 0.332 Re_x^(1/2) Pr^(1/3)

**Turbulent Flow (Re_L > 5×10⁵, 0.6 ≤ Pr ≤ 60):**

Nu_L = (0.037 Re_L^(4/5) - 871) Pr^(1/3)

This accounts for transition at Re_c = 5×10⁵.

**Alternative Turbulent Correlation:**

Nu_L = 0.0296 Re_L^(4/5) Pr^(1/3)  (fully turbulent)

**Local Nusselt Number (Turbulent):**

Nu_x = 0.0296 Re_x^(4/5) Pr^(1/3)

### Cylinder in Crossflow

Circular cylinders are fundamental to finned-tube heat exchangers, condensing units, and cooling coils.

**Churchill-Bernstein Correlation (All Re, Pr ≥ 0.2):**

Nu_D = 0.3 + [0.62 Re_D^(1/2) Pr^(1/3)] / [1 + (0.4/Pr)^(2/3)]^(1/4) × [1 + (Re_D / 282,000)^(5/8)]^(4/5)

**Simplified Correlations for Specific Ranges:**

| Reynolds Range | Correlation |
|----------------|-------------|
| 0.4 - 4 | Nu_D = 0.989 Re_D^0.330 Pr^(1/3) |
| 4 - 40 | Nu_D = 0.911 Re_D^0.385 Pr^(1/3) |
| 40 - 4,000 | Nu_D = 0.683 Re_D^0.466 Pr^(1/3) |
| 4,000 - 40,000 | Nu_D = 0.193 Re_D^0.618 Pr^(1/3) |
| 40,000 - 400,000 | Nu_D = 0.027 Re_D^0.805 Pr^(1/3) |

**Zhukauskas Correlation (1,000 < Re_D < 10⁶):**

Nu_D = C Re_D^m Pr^0.36 (Pr / Pr_s)^(1/4)

Where constants C and m depend on Reynolds number:

| Re_D Range | C | m |
|------------|---|---|
| 1 - 40 | 0.75 | 0.4 |
| 40 - 1,000 | 0.51 | 0.5 |
| 1,000 - 2×10⁵ | 0.26 | 0.6 |
| 2×10⁵ - 10⁶ | 0.076 | 0.7 |

Properties evaluated at film temperature T_f = (T_s + T_∞)/2, except Pr_s at surface temperature.

### Sphere Heat Transfer

Relevant for spray cooling, water droplets in cooling towers, and spherical tank applications.

**Whitaker Correlation (0.71 ≤ Pr ≤ 380, 3.5 ≤ Re_D ≤ 7.6×10⁴):**

Nu_D = 2 + [0.4 Re_D^(1/2) + 0.06 Re_D^(2/3)] Pr^0.4 (μ_∞ / μ_s)^(1/4)

**Ranz-Marshall Correlation (for droplets):**

Nu_D = 2 + 0.6 Re_D^(1/2) Pr^(1/3)

The limit Nu_D = 2 represents pure conduction from a sphere in stagnant fluid.

## HVAC Applications of External Flow

### Air-Cooled Condensers and Heat Exchangers

External flow over finned-tube bundles governs condenser capacity. Design considerations:

- Minimum clearance requirements for adequate airflow
- Wind effects on fan performance and capacity
- Recirculation from discharge to inlet (hot air recycling)
- Coil face velocity: typically 2.0 - 3.5 m/s (400 - 700 fpm)
- Fin spacing: 8 - 20 fins per inch depending on fouling potential

**Effective Heat Transfer:**

Q = U A ΔT_m

Where:
- U = overall heat transfer coefficient (W/m²·K)
- A = total heat transfer area including fins (m²)
- ΔT_m = log mean temperature difference (K)

### Cooling Towers

External flow around fill material and drift eliminators creates drag and heat/mass transfer. Crossflow and counterflow configurations exhibit different aerodynamic characteristics.

**Fill Drag Coefficient:**

Higher fill density increases drag and fan power requirements but improves contact area for evaporative cooling.

**Typical Design Parameters:**

- Air velocity through fill: 1.5 - 3.0 m/s
- Water loading: 2.0 - 5.5 L/(s·m²)
- Fill depth: 0.6 - 1.8 m

### Building Aerodynamics

External flow around buildings creates pressure distributions affecting infiltration, wind loads, and HVAC system performance.

**Wind Pressure Coefficient:**

C_p = (p - p_ref) / (1/2 ρ U_ref²)

Positive pressure (windward): C_p ≈ +0.6 to +0.8
Negative pressure (leeward): C_p ≈ -0.3 to -0.5
Negative pressure (sides): C_p ≈ -0.5 to -0.7

**Infiltration Pressure:**

Δp = C_p (1/2) ρ U²

### Rooftop Unit Installations

Rooftop equipment experiences:

- Increased wind exposure compared to grade-level installations
- Flow separation and recirculation zones on roof
- Reduced capacity in high winds (up to 15% capacity loss)
- Structural loading from drag forces

**Minimum Clearances (ASHRAE Guideline 1):**

- Discharge to intake: minimum 3 m (10 ft) horizontal
- Discharge to adjacent obstruction: minimum 1.5 m (5 ft)
- Service clearance: minimum 0.9 m (3 ft)

## Flow Control and Streamlining

### Streamlining Benefits

Streamlined shapes delay separation and reduce pressure drag:

- Teardrop/airfoil shapes: C_D ≈ 0.04 - 0.10
- Circular cylinder: C_D ≈ 1.0 - 1.2
- Square cylinder: C_D ≈ 2.0 - 2.2

**Fineness Ratio:**

FR = L / D

Optimal fineness ratio for minimum drag: FR ≈ 2.5 - 4.0

### Turbulence Effects

Freestream turbulence intensity affects transition location and heat transfer:

**Turbulence Intensity:**

Tu = u' / U_∞

Where:
- u' = RMS velocity fluctuation (m/s)
- U_∞ = mean freestream velocity (m/s)

Higher turbulence:
- Advances transition to lower Re
- Increases heat transfer coefficient (10-30% increase possible)
- Reduces drag coefficient for bluff bodies (supercritical flow)

## Design Considerations

### Equipment Selection

1. Account for reduced capacity at elevated wind speeds for outdoor equipment
2. Specify adequate structural support for drag and lift forces
3. Consider seasonal variations in air density affecting Re and heat transfer
4. Evaluate potential for recirculation using CFD or physical testing

### Installation Best Practices

1. Orient equipment to minimize prevailing wind impact on performance
2. Provide screens or barriers to reduce wind velocity (reduces drag force and improves heat transfer effectiveness)
3. Maintain manufacturer-specified clearances for proper airflow
4. Avoid installing discharge air into prevailing wind direction
5. Install equipment away from roof edges where flow separation creates turbulent zones

### Performance Calculations

1. Use appropriate drag coefficients for actual geometry and Re
2. Apply heat transfer correlations valid for operating Re and Pr ranges
3. Consider property variations with temperature (evaluate at film temperature)
4. Account for fin efficiency in finned-tube calculations
5. Include safety factors for fouling and degradation (typically 15-25%)

### Code and Standard References

**ASHRAE Standards:**

- ASHRAE Standard 62.1: Ventilation requirements affecting outdoor air intakes
- ASHRAE Guideline 1: Commissioning process including clearance verification
- ASHRAE Handbook - Fundamentals, Chapter 4: Heat Transfer
- ASHRAE Handbook - Fundamentals, Chapter 24: Airflow Around Buildings

**Testing Standards:**

- AHRI Standard 210/240: Performance rating of unitary air-conditioning equipment
- AHRI Standard 340/360: Performance rating of commercial refrigerated display equipment
- CTI Standards: Cooling tower performance certification

## Advanced Topics

### Drag Reduction Techniques

- Surface roughness optimization
- Vortex generators to delay separation
- Boundary layer suction
- Dimpled surfaces (golf ball effect for supercritical Re)

### Compressibility Effects

For air velocities above Mach 0.3 (approximately 100 m/s at standard conditions), compressibility becomes significant. HVAC applications rarely encounter this regime except in high-velocity exhaust jets.

**Mach Number:**

Ma = U / a

Where a = √(γ R T) is the speed of sound.

### Conjugate Heat Transfer

Simultaneous solution of conduction in solid and convection in fluid, critical for accurate fin efficiency calculations in heat exchangers.

**Fin Efficiency:**

η_f = tanh(mL) / (mL)

Where m = √(hP / kA_c) and L is the corrected fin length.

## Summary

External flow analysis provides the foundation for understanding drag forces, heat transfer, and aerodynamic performance of HVAC equipment exposed to unbounded fluid streams. Proper application of drag coefficients, boundary layer theory, and heat transfer correlations enables accurate equipment selection, performance prediction, and installation design. Recognition of flow separation, wake formation, and turbulence effects allows engineers to optimize configurations and minimize adverse impacts on system efficiency and capacity.
