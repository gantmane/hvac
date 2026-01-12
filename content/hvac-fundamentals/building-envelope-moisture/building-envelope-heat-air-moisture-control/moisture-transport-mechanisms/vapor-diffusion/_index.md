---
title: "Vapor Diffusion"
description: "Molecular-level water vapor transport through building materials driven by vapor pressure gradients, governed by Fick's laws of diffusion and characterized by material permeability properties"
weight: 1
---

## Fundamental Principles

Vapor diffusion represents the molecular-level transport of water vapor through porous building materials in response to vapor pressure gradients. Unlike air leakage, which involves bulk moisture movement through openings, diffusion occurs at the molecular scale as water vapor molecules migrate from regions of high vapor pressure to regions of low vapor pressure. This phenomenon critically affects building envelope performance, condensation risk, and material durability.

The driving force for vapor diffusion is the partial pressure differential of water vapor across a material assembly. In HVAC applications, this typically manifests as the difference between interior and exterior vapor pressures, which vary seasonally based on temperature and relative humidity conditions. Understanding diffusion mechanics is essential for proper vapor retarder placement, material selection, and condensation prevention strategies.

## Fick's First Law of Diffusion

### Governing Equation

Steady-state vapor diffusion through homogeneous materials follows Fick's first law:

**g = -δ(dp/dx)**

Where:
- g = vapor flux density (kg/m²·s or gr/ft²·hr)
- δ = vapor permeability of material (kg/m·s·Pa or perm·in)
- dp/dx = vapor pressure gradient (Pa/m or in.Hg/in)

The negative sign indicates that vapor flows from high to low vapor pressure (down the gradient).

### Alternative Formulation

For finite material thickness, the equation becomes:

**g = δ(Δp/L)**

Where:
- Δp = vapor pressure difference across material (Pa or in.Hg)
- L = material thickness (m or in)

### Permeance-Based Calculation

Using permeance (M) instead of permeability:

**g = M·Δp**

Where:
- M = vapor permeance = δ/L (kg/m²·s·Pa or perms)

This form is practical for building assembly calculations where material thickness is incorporated into the permeance value.

## Vapor Pressure Gradient

### Driving Force Fundamentals

The vapor pressure gradient represents the spatial rate of change in water vapor partial pressure. For building envelopes, this gradient develops due to differences in temperature and humidity between interior and exterior environments.

Vapor pressure at any point depends on temperature and relative humidity:

**p_v = φ·p_sat(T)**

Where:
- p_v = actual vapor pressure (Pa or in.Hg)
- φ = relative humidity (decimal fraction)
- p_sat(T) = saturation vapor pressure at temperature T (Pa or in.Hg)

### Saturation Vapor Pressure

The saturation vapor pressure as a function of temperature can be calculated using the Antoine equation or empirical correlations:

**p_sat = exp(A - B/(T+C))**

For water vapor in typical HVAC temperature ranges, common approximations include:

**p_sat (Pa) ≈ 610.78·exp(17.27·T/(T+237.3))** for T in °C

**p_sat (in.Hg) ≈ 0.00346·exp(0.0685·T)** for T in °F

### Gradient Calculation

For a single-layer material:

**dp/dx = (p_in - p_out)/L**

For multi-layer assemblies, the gradient varies through each layer based on its vapor resistance.

## Diffusion Coefficient and Material Properties

### Vapor Permeability (δ)

Vapor permeability quantifies a material's intrinsic ability to transmit water vapor, independent of thickness. This property varies significantly across building materials:

| Material | Permeability (ng/Pa·s·m) | Permeability (perm·in) |
|----------|-------------------------|------------------------|
| Air (still) | 110,000 | 640 |
| Extruded polystyrene | 60-180 | 0.35-1.05 |
| Polyethylene (6 mil) | 3.5 | 0.02 |
| Concrete (1:2:4 mix) | 1,700-3,400 | 10-20 |
| Plywood (exterior) | 340-1,000 | 2-6 |
| Gypsum board | 3,400 | 20 |
| Fiberglass batt | 110,000 | 640 |
| Cellulose insulation | 34,000-68,000 | 200-400 |
| Mineral wool | 110,000 | 640 |
| Brick (fired clay) | 140-680 | 0.8-4.0 |
| OSB sheathing | 170-680 | 1-4 |

### Vapor Permeance (M)

Permeance represents the combined effect of permeability and thickness:

**M = δ/L**

Units: ng/Pa·s·m² (SI) or perms (I-P)

1 perm = 57.4 ng/Pa·s·m²

### Vapor Resistance (R_v)

The reciprocal of permeance:

**R_v = 1/M = L/δ**

Units: m²·s·Pa/kg or rep (1/perm)

For multi-layer assemblies, vapor resistances add in series:

**R_v,total = R_v,1 + R_v,2 + ... + R_v,n**

### Temperature Dependence

Vapor permeability increases with temperature for most materials. The relationship can be approximated:

**δ(T) = δ_ref·exp[α(T - T_ref)]**

Where:
- δ_ref = permeability at reference temperature
- α = temperature coefficient (typically 0.01-0.05 K⁻¹)
- T_ref = reference temperature (typically 20°C or 68°F)

### Moisture Content Dependence

Many hygroscopic materials exhibit permeability that increases with moisture content. This nonlinear behavior complicates diffusion analysis and requires iterative or numerical solution methods.

## Steady-State Diffusion Analysis

### Single-Layer Systems

For a homogeneous wall section under steady conditions:

**g = δ(p_in - p_out)/L = M(p_in - p_out)**

The total vapor transmission rate through area A:

**G = g·A = M·A·(p_in - p_out)**

### Multi-Layer Assemblies

For a composite wall with n layers:

**g = (p_in - p_out)/(R_v,1 + R_v,2 + ... + R_v,n) = (p_in - p_out)/R_v,total**

The vapor pressure at interface j between layers can be determined:

**p_j = p_in - g·Σ(R_v,i)** for i = 1 to j

This allows calculation of the vapor pressure profile through the assembly, critical for identifying condensation planes.

### Condensation Risk Assessment

Condensation occurs at any interface where the actual vapor pressure equals or exceeds the saturation vapor pressure at that location. The condensation criterion:

**p(x) ≥ p_sat[T(x)]**

Where both vapor pressure and temperature distributions must be determined simultaneously. Temperature distribution follows from thermal analysis:

**T(x) = T_in - Q·Σ(R_th,i)** for heat flux Q through thermal resistances R_th

### Dew Point Method

An alternative approach uses dew point temperature:

**T_dp = T_sat(p_v)**

Condensation risk exists where T_dp > T_actual at any point in the assembly.

## Transient Diffusion Analysis

### Fick's Second Law

Non-steady-state vapor diffusion requires Fick's second law:

**∂C/∂t = D·∂²C/∂x²**

Where:
- C = water vapor concentration (kg/m³)
- t = time (s)
- D = diffusion coefficient (m²/s)
- x = spatial coordinate (m)

For vapor pressure formulation:

**∂p/∂t = D_p·∂²p/∂x²**

Where D_p is the vapor pressure diffusivity.

### Moisture Capacity Effects

In hygroscopic materials, moisture storage capacity affects transient response:

**∂u/∂t = D_m·∂²u/∂x²**

Where:
- u = moisture content (kg/kg or kg/m³)
- D_m = moisture diffusivity (m²/s)

The moisture diffusivity relates to vapor permeability through:

**D_m = (δ/ρ_0)·(∂p/∂u)**

Where:
- ρ_0 = dry material density (kg/m³)
- ∂p/∂u = slope of sorption isotherm

### Diurnal and Seasonal Cycles

Building envelopes experience cyclic vapor pressure boundary conditions:

**p(t) = p_mean + p_amp·sin(2πt/τ + φ)**

Where:
- τ = period (24 hr for diurnal, 365 days for seasonal)
- p_amp = amplitude of vapor pressure variation
- φ = phase angle

The penetration depth for diffusion waves:

**δ_p = √(2D·τ/2π)**

This indicates how deeply vapor pressure variations penetrate into assemblies.

### Numerical Methods

Transient hygrothermal analysis typically requires numerical solution:

- Finite difference methods
- Finite element methods
- Control volume approaches

Software tools like WUFI, DELPHIN, or MOISTURE-EXPERT implement coupled heat and moisture transport equations.

## Vapor Retarder Design

### Classification System

ASHRAE 160 and International Building Code classify vapor retarders by permeance:

| Class | Permeance Range | Common Materials |
|-------|----------------|------------------|
| I (Vapor Impermeable) | ≤ 0.1 perm | Polyethylene sheet, aluminum foil, sheet metal |
| II (Vapor Semi-Impermeable) | > 0.1 to ≤ 1.0 perm | Kraft-faced insulation, plywood, bitumen-coated paper |
| III (Vapor Semi-Permeable) | > 1.0 to ≤ 10 perm | Latex paint, some housewraps, unfaced fiberglass |

Materials > 10 perms are considered vapor permeable.

### Placement Guidelines

Vapor retarder placement depends on climate zone and assembly type:

**Heating-Dominated Climates (Zones 5-8):**
- Vapor retarder on interior (warm-in-winter) side
- Prevents interior moisture from diffusing into cold sheathing
- Class I or II retarder typically required

**Cooling-Dominated Climates (Zones 1-2):**
- Interior vapor retarder problematic
- Can trap moisture from exterior diffusion
- Class III or no interior vapor retarder preferred

**Mixed Climates (Zones 3-4):**
- Balance heating and cooling season risks
- Class II or III retarders provide flexibility
- "Smart" variable-permeance retarders advantageous

### Vapor Retarder Continuity

Effectiveness requires continuous installation:
- Sealed overlaps (minimum 6 in recommended)
- Sealed penetrations (electrical boxes, pipes)
- Sealed edges at transitions
- Minimal fastener penetrations

A 1% hole area can reduce vapor retarder effectiveness by 20-40% due to air leakage effects.

## Combined Heat and Moisture Transport

### Coupled Equations

Rigorous hygrothermal analysis requires simultaneous solution of heat and moisture transport:

**Heat:** ρc_p·∂T/∂t = ∂/∂x(λ·∂T/∂x) + L_v·∂g_v/∂x

**Moisture:** ∂u/∂t = ∂/∂x(D_m·∂u/∂x)

Where:
- λ = thermal conductivity (W/m·K)
- L_v = latent heat of vaporization (J/kg)
- Coupling occurs through temperature-dependent properties and latent heat effects

### Thermal Moisture Diffusion

Temperature gradients drive additional moisture flux through the Soret effect:

**g_total = -δ·∂p/∂x - D_T·∂T/∂x**

Where D_T is the thermal moisture diffusion coefficient. This effect is generally small but can be significant in extreme temperature gradients.

## Design Considerations

### Material Selection Strategy

**Exterior-to-Interior Permeability:**

Building assemblies should generally become more permeable from exterior to interior (or remain constant). This "drying-to-the-interior" strategy allows:
- Redistribution of construction moisture
- Seasonal moisture reversals
- Recovery from leakage events

Quantitatively: M_interior ≥ 5·M_exterior (ASHRAE guideline)

### Air Barrier vs Vapor Retarder

Critical distinction:
- Air barriers control convective moisture transport (dominant)
- Vapor retarders control diffusive moisture transport (secondary)
- Both functions may be served by same or different layers
- Air barrier is always more critical for moisture control

Air leakage can transport 100-1000 times more moisture than vapor diffusion under typical conditions.

### Interstitial Condensation Analysis

Dewpoint calculation procedure:
1. Calculate temperature profile through assembly (thermal analysis)
2. Calculate vapor pressure profile through assembly (diffusion analysis)
3. Determine saturation vapor pressure at each point using local temperature
4. Compare actual vapor pressure to saturation vapor pressure
5. Condensation occurs where p_v(x) > p_sat[T(x)]

### Drainage and Drying

Assemblies must accommodate moisture through:
- **Drainage:** Liquid water removal (gravity, capillary breaks)
- **Drying:** Vapor diffusion to exterior and/or interior
- **Ventilation:** Air movement in cavities

Successful envelope design integrates all three mechanisms.

## Common Design Errors

### Vapor Retarder Misapplication

- Class I retarder in cooling climates (traps moisture)
- Dual vapor retarders (prevents drying in both directions)
- Discontinuous installation (negates effectiveness)
- Retarder on wrong side of insulation

### Ignoring Air Leakage

Focusing exclusively on vapor diffusion while neglecting air barrier continuity. Air leakage dominates moisture transport in most failures.

### Simplified Analysis Limitations

Steady-state diffusion calculations cannot capture:
- Seasonal wetting/drying cycles
- Moisture storage in hygroscopic materials
- Rain penetration and redistribution
- Solar-driven moisture flow

These factors require advanced hygrothermal simulation.

## ASHRAE Standards and References

**ASHRAE Standard 160:** Criteria for Moisture-Control Design Analysis in Buildings
- Establishes methodology for hygrothermal analysis
- Defines acceptable moisture accumulation limits
- Provides climate data and boundary conditions

**ASHRAE Handbook—Fundamentals, Chapter 26:** Heat, Air, and Moisture Control in Building Assemblies
- Comprehensive treatment of diffusion theory
- Material property data
- Calculation procedures and examples

**ASHRAE Standard 62.1/62.2:** Ventilation for Acceptable Indoor Air Quality
- Impacts interior moisture levels
- Affects vapor pressure differentials

## Measurement and Testing

### Permeability Testing

**ASTM E96:** Standard Test Methods for Water Vapor Transmission of Materials
- Desiccant method (dry cup)
- Water method (wet cup)
- Results vary with test conditions and relative humidity

**ASTM C1340:** Standard Test Method for Water Vapor Transmission Rate (time-modulated)
- More rapid testing approach
- Applicable to low-permeance materials

### Field Verification

In-situ moisture monitoring:
- Embedded moisture content sensors
- Relative humidity sensors at interfaces
- Temperature sensors for dewpoint determination
- Long-term data logging to capture seasonal cycles

## Advanced Topics

### Variable Permeance Materials

"Smart" vapor retarders exhibit permeance that varies with relative humidity:
- Low permeance at low RH (winter condition)
- High permeance at high RH (summer condition)
- Allows seasonal adaptation

Typical behavior: 0.5 perms at 30% RH increasing to 5-10 perms at 80% RH

### Capillary Transport

In porous materials, liquid water transport by capillarity can exceed vapor diffusion:

**g_cap = ρ_w·D_cap·∂θ/∂x**

Where:
- D_cap = capillary diffusivity (m²/s)
- θ = volumetric moisture content

Capillary redistribution affects moisture profiles and must be considered in high-moisture-content scenarios.

### Surface Film Coefficients

Vapor exchange at surfaces introduces additional resistance:

**h_v = β·h_c**

Where:
- h_v = vapor transfer coefficient (kg/m²·s·Pa)
- β = Lewis number ≈ 0.015 for air
- h_c = convective heat transfer coefficient (W/m²·K)

Surface resistances affect overall diffusion rates and boundary conditions for analysis.

## Practical Engineering Applications

### Refrigerated Warehouses

Extreme vapor pressure differentials:
- Interior: -20°C, 80% RH → p_v ≈ 100 Pa
- Exterior: 30°C, 60% RH → p_v ≈ 2,500 Pa
- Inward diffusion drives massive condensation potential
- Requires robust exterior vapor retarder (Class I)
- Interior finishes must be highly permeable for drying

### Natatoriums

High interior moisture loads:
- Interior: 28°C, 50-60% RH → p_v ≈ 2,300 Pa
- Significant outward diffusion in winter
- Dehumidification reduces vapor pressure gradients
- Enhanced vapor retarders on interior mandatory
- Specialty air barriers required

### Hot-Humid Climates

Vapor drive reversal:
- Summer: inward diffusion from humid exterior
- Interior vapor retarders trap moisture
- Vapor-open interior finishes essential
- Dehumidification controls interior RH
- Vapor-permeable insulation preferred
