---
title: "Fick's Law of Diffusion"
description: "Fundamental physics of vapor diffusion through building materials, governing equations, mass transfer coefficients, and engineering calculations for moisture control"
weight: 1
---

## Physical Principles

Fick's Law describes the diffusive transport of water vapor through porous building materials under a concentration gradient. This fundamental relationship governs vapor diffusion analysis in building envelopes and forms the basis for permeance calculations, condensation risk assessment, and hygrothermal modeling.

The law applies when vapor transport occurs by molecular diffusion rather than bulk air movement, which is the case for most building materials under typical pressure differentials.

### Molecular Diffusion Mechanism

Water vapor molecules move through the pore structure of building materials by random thermal motion. The net flux occurs from regions of high vapor concentration to regions of low vapor concentration. The driving force is the concentration gradient, not the pressure gradient directly, though vapor pressure and concentration are related through the ideal gas law.

The diffusion process involves:
- Random molecular motion (Brownian motion)
- Collision with material pore surfaces
- Passage through interconnected pore network
- Adsorption and desorption at pore surfaces
- Concentration-driven net transport

## Fick's First Law - Steady State Diffusion

The first law describes steady-state diffusion where vapor concentration at any point does not change with time.

### Mathematical Formulation

The one-dimensional form:

**J = -D (dC/dx)**

Where:
- J = vapor flux density (kg/m²·s)
- D = diffusion coefficient (m²/s)
- dC/dx = concentration gradient (kg/m⁴)
- Negative sign indicates flow from high to low concentration

### Alternative Forms for Building Applications

**Vapor Pressure Driving Force:**

**g = -δ (dp/dx)**

Where:
- g = vapor flux density (kg/m²·s)
- δ = vapor permeability (kg/m·s·Pa)
- dp/dx = vapor pressure gradient (Pa/m)

**Partial Pressure Form:**

**g = -δₚ (dπ/dx)**

Where:
- δₚ = water vapor permeability (kg/m·s·Pa)
- π = partial pressure of water vapor (Pa)

### Relationship to Permeance

For a material layer of thickness L:

**g = M Δp**

Where:
- M = permeance (kg/m²·s·Pa) = δ/L
- Δp = vapor pressure difference across layer (Pa)

## Diffusion Coefficient

The diffusion coefficient quantifies the material's ability to transmit vapor under a concentration gradient.

### Temperature Dependence

The diffusion coefficient varies with temperature according to:

**D(T) = D₀ exp(-Ea/RT)**

Where:
- D₀ = pre-exponential factor (m²/s)
- Ea = activation energy (J/mol)
- R = universal gas constant = 8.314 J/mol·K
- T = absolute temperature (K)

For water vapor in air at atmospheric pressure:

**Dₐᵢᵣ = 2.306 × 10⁻⁵ (T/273.15)^1.81 m²/s**

At 20°C: Dₐᵢᵣ ≈ 2.5 × 10⁻⁵ m²/s

### Material Diffusion Coefficient

For porous materials, the effective diffusion coefficient is reduced from the air value:

**Dₑff = (Dₐᵢᵣ × ε × τ) / ζ**

Where:
- ε = porosity (fraction of void volume)
- τ = tortuosity factor (accounts for indirect path)
- ζ = constriction factor (accounts for pore narrowing)

### Diffusion Resistance Factor

Building materials are commonly characterized by the water vapor diffusion resistance factor (μ):

**μ = Dₐᵢᵣ / Dₘₐₜ**

This dimensionless factor indicates how many times more resistant the material is compared to still air of the same thickness.

## Vapor Permeability

Vapor permeability relates vapor flux to partial pressure gradient and is the key material property for building envelope analysis.

### Definition and Units

**δ = vapor permeability**

SI Units: kg/m·s·Pa
US Units: grain/ft·hr·in.Hg

Conversion: 1 grain/ft·hr·in.Hg = 1.459 × 10⁻¹⁰ kg/m·s·Pa

### Relationship to Diffusion Coefficient

**δ = D × Mᵥ / (R × T)**

Where:
- Mᵥ = molecular weight of water = 18.015 kg/kmol
- R = universal gas constant = 8314 J/kmol·K
- T = absolute temperature (K)

At 20°C for air: δₐᵢᵣ ≈ 1.85 × 10⁻¹⁰ kg/m·s·Pa

### Material Vapor Permeability

**δₘₐₜ = δₐᵢᵣ / μ**

The resistance factor μ is the inverse of the relative permeability.

## Vapor Permeance

Permeance is the property of a specific thickness of material, analogous to thermal conductance.

### Definition

**M = δ / L**

Where:
- M = permeance (kg/m²·s·Pa)
- δ = permeability (kg/m·s·Pa)
- L = material thickness (m)

### US Units - Perms

Permeance is commonly expressed in perms:

- 1 perm (US) = 1 grain/ft²·hr·in.Hg = 5.721 × 10⁻¹¹ kg/m²·s·Pa
- 1 metric perm = 1 grain/m²·s·Pa = 5.745 × 10⁻¹¹ kg/m²·s·Pa

### Vapor Retarder Classification (IBC/IRC)

| Class | Permeance Range | Example Materials |
|-------|-----------------|-------------------|
| Class I (Impermeable) | ≤ 0.1 perm | Polyethylene sheet, aluminum foil, sheet metal |
| Class II (Semi-impermeable) | 0.1 < M ≤ 1.0 perm | Kraft-faced insulation, plywood, OSB |
| Class III (Semi-permeable) | 1.0 < M ≤ 10 perm | Latex paint, unfaced insulation, gypsum board |
| Permeable | > 10 perm | Unpainted gypsum, fiberglass insulation |

## Vapor Flux Calculation

### Single Layer

For a homogeneous material layer:

**g = M (pᵢ - pₒ)**

**g = (δ/L) (pᵢ - pₒ)**

Where:
- pᵢ = interior vapor pressure (Pa)
- pₒ = exterior vapor pressure (Pa)

### Multilayer Assembly

For multiple layers in series (analogous to thermal resistance):

**Total vapor resistance: Rᵥ = Σ(Rᵥ,ᵢ) = Σ(Lᵢ/δᵢ) = Σ(1/Mᵢ)**

**Total permeance: M_total = 1 / Rᵥ**

**Vapor flux: g = M_total × Δp_total**

### Including Surface Resistances

For complete assembly analysis including surface vapor resistances:

**Rᵥ,total = Rᵥ,ᵢ + Σ(Lᵢ/δᵢ) + Rᵥ,ₒ**

Surface vapor resistances are typically negligible compared to material resistances except for highly permeable materials.

### Example Calculation: Wood Frame Wall

Consider a wall assembly (interior to exterior):
1. Gypsum board: 12.7 mm, μ = 8.3
2. Kraft paper: 0.2 mm, μ = 30
3. Fiberglass insulation: 89 mm, μ = 1.0
4. OSB sheathing: 11 mm, μ = 200
5. Building paper: 0.5 mm, μ = 50

Using δₐᵢᵣ = 1.85 × 10⁻¹⁰ kg/m·s·Pa at 20°C:

| Layer | Thickness (m) | μ | δ (kg/m·s·Pa) | Rᵥ (m²·s·Pa/kg) |
|-------|---------------|---|---------------|-----------------|
| Gypsum | 0.0127 | 8.3 | 2.23 × 10⁻¹¹ | 5.69 × 10⁸ |
| Kraft | 0.0002 | 30 | 6.17 × 10⁻¹² | 3.24 × 10⁷ |
| Fiberglass | 0.089 | 1.0 | 1.85 × 10⁻¹⁰ | 4.81 × 10⁸ |
| OSB | 0.011 | 200 | 9.25 × 10⁻¹³ | 1.19 × 10¹⁰ |
| Building paper | 0.0005 | 50 | 3.70 × 10⁻¹² | 1.35 × 10⁸ |

**R_v,total = 1.31 × 10¹⁰ m²·s·Pa/kg**

**M_total = 7.6 × 10⁻¹¹ kg/m²·s·Pa = 1.3 perms**

This assembly qualifies as Class II vapor retarder, with the OSB sheathing providing the dominant resistance.

## Concentration Gradient

The concentration gradient is the spatial rate of change of vapor concentration.

### Vapor Concentration

Mass concentration of water vapor:

**C = ρᵥ = p × Mᵥ / (R × T)**

Where:
- ρᵥ = vapor density (kg/m³)
- p = vapor pressure (Pa)
- Mᵥ = 18.015 kg/kmol
- R = 8314 J/kmol·K
- T = absolute temperature (K)

At 20°C and 1000 Pa vapor pressure:
**C = 1000 × 18.015 / (8314 × 293.15) = 0.0074 kg/m³**

### Linear Gradient Assumption

For steady-state conditions through a homogeneous material, the concentration profile is linear:

**C(x) = Cᵢ - (Cᵢ - Cₒ) × (x/L)**

Where:
- x = distance from interior surface (m)
- L = total thickness (m)
- Cᵢ = interior surface concentration
- Cₒ = exterior surface concentration

### Gradient Calculation

**dC/dx = -(Cᵢ - Cₒ) / L = -ΔC / L**

For vapor pressure gradient:

**dp/dx = -(pᵢ - pₒ) / L = -Δp / L**

## Fick's Second Law - Transient Diffusion

The second law describes time-dependent diffusion where vapor concentration changes with time.

### Differential Equation

**∂C/∂t = D (∂²C/∂x²)**

For one-dimensional diffusion with constant diffusion coefficient.

**∂C/∂t = ∂/∂x (D ∂C/∂x)**

For variable diffusion coefficient (moisture-dependent permeability).

### Hygroscopic Materials

For materials with significant moisture storage capacity:

**∂u/∂t = ∂/∂x (D_w ∂u/∂x)**

Where:
- u = moisture content (kg/kg)
- D_w = moisture diffusivity (m²/s)

The moisture diffusivity relates to vapor permeability through:

**D_w = (δ/ρ_dry) × (dp/du)**

Where:
- ρ_dry = dry density of material (kg/m³)
- dp/du = slope of sorption isotherm (Pa·kg/kg)

### Characteristic Diffusion Time

The time scale for diffusion through a material:

**t_char = L² / (4D)**

| Material | Thickness (m) | D (m²/s) | t_char |
|----------|---------------|----------|--------|
| Gypsum board | 0.0127 | 3.0 × 10⁻⁶ | 13.4 seconds |
| OSB sheathing | 0.011 | 1.2 × 10⁻⁷ | 15.8 minutes |
| Concrete block | 0.20 | 5.0 × 10⁻⁸ | 2.3 hours |
| Brick wall | 0.10 | 2.0 × 10⁻⁸ | 3.5 hours |

These time scales indicate how quickly materials respond to changes in boundary conditions.

## Mass Transfer Coefficient

The mass transfer coefficient relates vapor flux to a vapor pressure difference, analogous to the convective heat transfer coefficient.

### Surface Mass Transfer

At material surfaces, vapor transfer occurs by convection:

**g = h_m (p_air - p_surface)**

Where:
- h_m = mass transfer coefficient (kg/m²·s·Pa)
- p_air = vapor pressure in bulk air
- p_surface = vapor pressure at surface

### Relationship to Heat Transfer Coefficient

Lewis relation for air-water vapor mixtures:

**h_m / h_c = 1 / (c_p × Le^(2/3))**

Where:
- h_c = convective heat transfer coefficient (W/m²·K)
- c_p = specific heat of air = 1006 J/kg·K
- Le = Lewis number ≈ 0.87 for air-water vapor

For typical conditions:
**h_m ≈ h_c / (1006 × 0.93) ≈ h_c / 935**

### Typical Surface Mass Transfer Coefficients

| Surface Condition | h_c (W/m²·K) | h_m (kg/m²·s·Pa) |
|-------------------|--------------|------------------|
| Interior still air | 8.3 | 8.9 × 10⁻⁹ |
| Interior moving air | 25 | 2.7 × 10⁻⁸ |
| Exterior (summer, 3.4 m/s) | 34 | 3.6 × 10⁻⁸ |
| Exterior (winter, 6.7 m/s) | 40 | 4.3 × 10⁻⁸ |

### Surface Vapor Resistance

**R_v,surface = 1 / h_m**

Interior surface: R_v,i ≈ 1.1 × 10⁸ m²·s·Pa/kg
Exterior surface: R_v,o ≈ 2.5 × 10⁷ m²·s·Pa/kg

These resistances are significant only for highly permeable materials (M > 100 perms).

## Temperature Effects on Vapor Diffusion

### Permeability Temperature Dependence

Most building materials show temperature-dependent permeability:

**δ(T) = δ₀ exp[a(T - T₀)]**

Where:
- δ₀ = permeability at reference temperature T₀
- a = temperature coefficient (1/K)
- Typical range: a = 0.01 to 0.04 K⁻¹

For moisture content also affects permeability:

**δ(T, u) = δ₀(u) exp[a(T - T₀)]**

### Temperature Gradient Effects

In building envelopes with temperature gradients, the vapor pressure gradient depends on both partial pressure and temperature:

**g = -δ(T) × dp/dx**

Where both δ and p vary with position.

## Design Considerations

### ASHRAE Standard 160 Analysis

ASHRAE Standard 160 requires evaluation of moisture accumulation:

1. Calculate hourly vapor flux through each layer
2. Determine condensation potential at material interfaces
3. Check moisture accumulation against material limits
4. Verify adequate drying capacity

### Critical Interface Identification

Condensation occurs where temperature drops below dewpoint. The critical location is typically:
- Cold side of insulation in heating climates
- Warm side of insulation in cooling climates
- At low-permeability layers (vapor retarders)

### Vapor Retarder Placement

**Heating-dominated climates:** Place vapor retarder on warm (interior) side

**Cooling-dominated climates:** Either no interior vapor retarder or use permeable materials

**Mixed climates:** Use "smart" vapor retarders that adjust permeability with humidity

### Drying Potential

Assemblies must be able to dry to at least one side:

**Inward drying:** Permeable interior finish (M > 10 perms)

**Outward drying:** Permeable exterior sheathing and cladding

**Bidirectional:** No vapor retarders, all materials relatively permeable

### Material Property Data Sources

- ASHRAE Handbook - Fundamentals, Chapter 26 (Heat, Air, and Moisture Control)
- ASHRAE Standard 160 - Design Criteria for Moisture Control
- Building Science Corporation: buildingscience.com
- Oak Ridge National Laboratory (ORNL) materials database
- Material manufacturer technical data sheets
- ASTM E96 test data (water vapor transmission)

## Engineering Applications

### Condensation Risk Assessment

Compare actual interface conditions to dewpoint:

**If T_interface < T_dewpoint → Condensation occurs**

Calculate accumulated moisture:
**Δm = ∫(g_in - g_out) dt**

Where:
- g_in = vapor flux arriving at interface
- g_out = vapor flux leaving interface

### Hygrothermal Modeling

Advanced analysis using coupled heat and moisture transport:

**WUFI, DELPHIN, COMSOL, MOISTURE-EXPERT**

These tools solve coupled equations:
- Heat conduction with latent heat effects
- Vapor diffusion (Fick's Law)
- Capillary liquid transport
- Air infiltration effects
- Solar radiation absorption
- Rainfall absorption

### Vapor Pressure Profiling

Calculate vapor pressure at each interface in steady-state:

**p_interface,n = p_i - g × Σ(R_v,1 to R_v,n)**

Plot vapor pressure profile and compare to saturation pressure (dewpoint) profile to identify condensation planes.

## Limitations and Practical Considerations

### When Fick's Law Applies

Valid assumptions:
- Diffusion-dominated transport (negligible air leakage)
- Dilute vapor concentration
- Isothermal or slowly varying temperature
- Homogeneous material properties
- No chemical reactions or phase changes

### When Fick's Law is Insufficient

Fick's Law alone does not account for:
- **Capillary liquid transport** - dominant in high humidity
- **Air leakage** - often exceeds diffusion by 10-100×
- **Moisture storage** - important for transient analysis
- **Sorption hysteresis** - different wetting/drying paths
- **Rain penetration** - exterior moisture source

### Air Leakage Dominance

The vapor transport by air leakage at pressure difference Δp_air:

**g_air = ρ_v × Q_air = ρ_v × (ELA/1000) × Δp_air^0.6**

Where:
- ELA = effective leakage area (cm²)
- Δp_air = air pressure difference (Pa)

Even small air leakage paths transport far more moisture than diffusion through the same area.

**Critical design principle:** Air barriers are more important than vapor retarders for moisture control.

## ASHRAE and Code References

### ASHRAE Handbooks

- **ASHRAE Handbook - Fundamentals, Chapter 26:** Heat, Air, and Moisture Control in Building Assemblies - Material Properties
- **ASHRAE Handbook - Fundamentals, Chapter 1:** Psychrometrics - Vapor pressure relationships
- **ASHRAE Handbook - Fundamentals, Chapter 25:** Thermal and Water Vapor Transmission Data

### ASHRAE Standards

- **ASHRAE Standard 160-2021:** Criteria for Moisture-Control Design Analysis in Buildings
- **ASHRAE Standard 55-2020:** Thermal Environmental Conditions for Human Occupancy
- **ASHRAE Standard 62.1-2022:** Ventilation for Acceptable Indoor Air Quality

### Building Codes

- **International Building Code (IBC):** Section 1405 - Vapor retarders
- **International Residential Code (IRC):** Section R702.7 - Vapor retarders
- **International Energy Conservation Code (IECC):** Air barrier and vapor retarder requirements

### Test Methods

- **ASTM E96/E96M:** Standard Test Methods for Water Vapor Transmission of Materials
- **ASTM C1498:** Standard Test Method for Hygroscopic Sorption Isotherms of Building Materials
- **ASTM C1794:** Standard Test Method for Determination of the Water Absorption Coefficient by Partial Immersion

## Advanced Topics

### Moisture-Dependent Permeability

Many materials show significant permeability variation with moisture content:

**δ(u) = δ_dry × f(u)**

For wood and wood products:
**f(u) ≈ exp(b × u)**

Where b is material-specific coefficient (typically 5-15).

This nonlinearity requires iterative solution methods for accurate predictions.

### Capillary Condensation

At high relative humidity (> 95%), capillary condensation in material pores creates liquid moisture before bulk condensation occurs. This accelerates moisture transport beyond Fick's Law predictions.

### Salt Transport and Efflorescence

In masonry and concrete, dissolved salts affect vapor diffusion and can crystallize at evaporative surfaces, potentially causing deterioration.

## Summary

Fick's Law provides the fundamental framework for analyzing vapor diffusion in building envelopes:

1. **First Law** governs steady-state vapor flux driven by concentration/pressure gradients
2. **Second Law** describes transient moisture accumulation and storage
3. **Material permeability** is the key property, varying with temperature and moisture content
4. **Multilayer analysis** uses series resistance calculation analogous to thermal analysis
5. **Critical design applications** include vapor retarder selection, condensation risk assessment, and drying potential evaluation
6. **Limitations** include neglecting air leakage (often dominant) and liquid transport
7. **Modern practice** uses hygrothermal modeling that couples Fick's Law with heat transfer, capillary transport, and air movement for comprehensive moisture analysis

Proper application of diffusion theory, combined with effective air sealing, enables durable building envelope design that controls moisture accumulation and prevents material degradation.
