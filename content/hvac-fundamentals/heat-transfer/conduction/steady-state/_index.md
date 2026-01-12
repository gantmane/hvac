---
title: "Steady State Conduction"
weight: 1
---

Steady-state conduction occurs when the temperature field within a material does not change with time. The temperature at any point remains constant, and the heat flux is time-invariant. This condition is fundamental to HVAC heat transfer analysis for building envelopes, insulation systems, and heat exchangers.

## Fourier's Law of Heat Conduction

Fourier's law provides the fundamental relationship between heat flux and temperature gradient:

**One-Dimensional Form:**

q = -kA(dT/dx)

Where:
- q = heat transfer rate (W)
- k = thermal conductivity (W/m·K)
- A = cross-sectional area perpendicular to heat flow (m²)
- dT/dx = temperature gradient (K/m)
- Negative sign indicates heat flows from high to low temperature

**Heat Flux Form:**

q" = -k(dT/dx)

Where q" = heat flux (W/m²)

The thermal conductivity k is a material property. For most building materials, k varies weakly with temperature and can be treated as constant over typical HVAC temperature ranges.

## Plane Wall Conduction

For a plane wall of thickness L with constant thermal conductivity and uniform surface temperatures T₁ and T₂:

**Temperature Distribution:**

T(x) = T₁ - (T₁ - T₂)(x/L)

The temperature varies linearly through the wall thickness.

**Heat Transfer Rate:**

q = kA(T₁ - T₂)/L

**Thermal Resistance:**

The thermal resistance concept simplifies analysis by analogy to Ohm's law (V = IR):

R_cond = L/(kA)

Heat transfer rate becomes:

q = ΔT/R_cond = (T₁ - T₂)/(L/kA)

Units: R_cond in K/W or °C/W

## Composite Walls - Series Configuration

For multiple layers in series (typical building wall construction), resistances add:

**Total Resistance:**

R_total = R₁ + R₂ + R₃ + ... + R_n

For n layers:

R_total = Σ(L_i/k_i A)

**Heat Transfer Rate:**

q = ΔT_overall/R_total = (T_∞1 - T_∞2)/(R_conv,1 + R_cond,1 + R_cond,2 + ... + R_conv,2)

Where:
- R_conv,1 = 1/(h₁A) = interior surface convection resistance
- R_conv,2 = 1/(h₂A) = exterior surface convection resistance
- R_cond,i = L_i/(k_i A) = conduction resistance of layer i

**Interface Temperatures:**

For any interface between layers i and i+1:

T_interface = T_upstream - q·R_layers_upstream

## R-Values and U-Values

**R-Value (Thermal Resistance per Unit Area):**

R = L/k  (units: m²·K/W or ft²·°F·hr/BTU)

The R-value is independent of area and commonly used in building construction:

- R-13 fiberglass batt: R = 2.29 m²·K/W (13 ft²·°F·hr/BTU)
- R-19 fiberglass batt: R = 3.35 m²·K/W (19 ft²·°F·hr/BTU)
- R-30 blown cellulose: R = 5.28 m²·K/W (30 ft²·°F·hr/BTU)

**U-Value (Overall Heat Transfer Coefficient):**

U = 1/(R_total)  (units: W/m²·K or BTU/hr·ft²·°F)

Heat flux through assembly:

q" = U·ΔT

Lower U-values indicate better insulation performance.

## Contact Resistance

At interfaces between solid materials, microscopic surface roughness creates air gaps that impede heat transfer. Contact resistance R_c depends on:

- Surface roughness and waviness
- Contact pressure
- Interstitial fluid (air, thermal grease)
- Material hardness

**Typical Values:**

| Interface | Contact Pressure | R_c (m²·K/W × 10⁻⁴) |
|-----------|------------------|---------------------|
| Aluminum-Aluminum | 1 MPa | 1.5-5.0 |
| Copper-Copper | 1 MPa | 1.0-3.0 |
| Steel-Steel | 1 MPa | 2.0-10.0 |
| With thermal grease | 1 MPa | 0.1-0.5 |

Contact resistance is included in series with other resistances:

R_total = R₁ + R_c,1-2 + R₂ + R_c,2-3 + R₃

## Cylindrical Coordinates

For radial conduction through cylindrical geometries (pipes, insulated ducts):

**Temperature Distribution:**

T(r) = T₁ - (T₁ - T₂)[ln(r/r₁)/ln(r₂/r₁)]

Logarithmic profile, not linear.

**Heat Transfer Rate (per unit length):**

q' = 2πk(T₁ - T₂)/ln(r₂/r₁)

Where:
- q' = heat transfer per unit length (W/m)
- r₁ = inner radius (m)
- r₂ = outer radius (m)

**Thermal Resistance (per unit length):**

R'_cyl = ln(r₂/r₁)/(2πk)  (units: K·m/W)

For cylindrical pipe with insulation:

R'_total = ln(r₂/r₁)/(2πk_pipe) + ln(r₃/r₂)/(2πk_insulation)

## Thermal Resistance Networks

Complex geometries are solved using resistance networks analogous to electrical circuits:

**Series Resistances:**
- Heat flows through each element sequentially
- Same heat flow through all elements
- R_total = R₁ + R₂ + R₃ + ...

**Parallel Resistances:**
- Heat flow divides among parallel paths
- Same temperature difference across all paths
- 1/R_total = 1/R₁ + 1/R₂ + 1/R₃ + ...

**Example: Wall with thermal bridge**

Wood stud (k = 0.12 W/m·K) and fiberglass insulation (k = 0.038 W/m·K) in parallel create a thermal bridge. Total heat flow is the sum of paths.

## Worked Example 1: Composite Wall Heat Loss

**Problem:** Calculate heat loss through a wall assembly:
- Interior surface: T₁ = 22°C, h₁ = 8 W/m²·K
- Gypsum board: L = 12.7 mm, k = 0.17 W/m·K
- Fiberglass insulation: L = 140 mm, k = 0.038 W/m·K
- Wood siding: L = 19 mm, k = 0.12 W/m·K
- Exterior surface: T₂ = -5°C, h₂ = 30 W/m²·K

**Solution:**

Calculate resistances per unit area (R-values):

R_conv,i = 1/h₁ = 1/8 = 0.125 m²·K/W

R_gypsum = L/k = 0.0127/0.17 = 0.075 m²·K/W

R_insulation = L/k = 0.140/0.038 = 3.684 m²·K/W

R_siding = L/k = 0.019/0.12 = 0.158 m²·K/W

R_conv,o = 1/h₂ = 1/30 = 0.033 m²·K/W

R_total = 0.125 + 0.075 + 3.684 + 0.158 + 0.033 = 4.075 m²·K/W

Heat flux:

q" = ΔT/R_total = (22 - (-5))/4.075 = 27/4.075 = 6.63 W/m²

U-value:

U = 1/R_total = 1/4.075 = 0.245 W/m²·K

For a 20 m² wall:

q = q"·A = 6.63 × 20 = 133 W

## Worked Example 2: Insulated Pipe Heat Loss

**Problem:** A copper steam pipe carries saturated steam at 150°C. Calculate heat loss per meter length:
- Pipe: inner radius r₁ = 50 mm, outer radius r₂ = 57 mm, k = 401 W/m·K
- Insulation: thickness = 50 mm (r₃ = 107 mm), k = 0.045 W/m·K
- Ambient air: T_∞ = 20°C, h = 10 W/m²·K
- Inner surface temperature = steam temperature (neglect steam-side resistance)

**Solution:**

Calculate thermal resistances per unit length:

R'_pipe = ln(r₂/r₁)/(2πk_pipe) = ln(57/50)/(2π × 401)
R'_pipe = ln(1.14)/(2519) = 0.131/2519 = 0.000052 K·m/W

R'_insulation = ln(r₃/r₂)/(2πk_insulation) = ln(107/57)/(2π × 0.045)
R'_insulation = ln(1.877)/(0.283) = 0.630/0.283 = 2.227 K·m/W

R'_conv = 1/(h × 2πr₃) = 1/(10 × 2π × 0.107)
R'_conv = 1/6.72 = 0.149 K·m/W

R'_total = 0.000052 + 2.227 + 0.149 = 2.376 K·m/W

Heat loss per unit length:

q' = (T_steam - T_∞)/R'_total = (150 - 20)/2.376 = 130/2.376 = 54.7 W/m

**Note:** The copper pipe resistance is negligible (0.002% of total). This is typical for metal pipes where insulation dominates.

Outer surface temperature of insulation:

T_surface = T_∞ + q'·R'_conv = 20 + 54.7 × 0.149 = 28.2°C

## Worked Example 3: Critical Radius of Insulation

**Problem:** For the pipe in Example 2, does adding more insulation always reduce heat loss?

**Solution:**

The critical radius for cylindrical insulation is:

r_critical = k_insulation/h = 0.045/10 = 0.0045 m = 4.5 mm

Current insulation outer radius: r₃ = 107 mm >> r_critical

Since r₃ > r_critical, adding more insulation will reduce heat loss. However, if the bare pipe radius exceeded r_critical, adding thin insulation would initially increase heat loss by increasing surface area more than it increases resistance.

For typical building applications with low h values and moderate insulation thickness, r > r_critical, so adding insulation always helps.

## Temperature-Dependent Thermal Conductivity

When thermal conductivity varies significantly with temperature:

k(T) = k₀(1 + βT)

Use mean thermal conductivity:

k_mean = k₀[1 + β(T₁ + T₂)/2]

Or integrate Fourier's law:

q = A(k₀ΔT + k₀β(T₁² - T₂²)/2)/L

For most HVAC applications over moderate temperature ranges, constant k is adequate.

## Design Implications

**Building Envelope Design:**
- Maximize R-values in walls, roofs, and floors
- Minimize thermal bridges (studs, structural elements)
- Ensure continuous insulation where possible
- Account for contact resistance at material interfaces

**Duct and Pipe Insulation:**
- Use logarithmic equations for cylindrical geometry
- Verify insulation thickness exceeds critical radius
- Consider vapor barriers to prevent condensation
- Account for degradation of k due to moisture

**Resistance Network Analysis:**
- Identify series and parallel heat flow paths
- Calculate effective R-value for composite assemblies
- Locate interface temperatures to check for condensation risk
- Use U-values for assembly comparison and energy modeling

## Components

- Fourier Law One Dimensional
- Thermal Conductivity Temperature Dependent
- Thermal Resistance Concept
- Composite Walls Series
- Composite Walls Parallel
- Multilayer Systems
- Cylindrical Coordinates
- Spherical Coordinates
- Critical Radius Insulation
- Contact Resistance
- Thermal Interface Materials
