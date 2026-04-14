---
title: "Material Conductivity"
aliases: ["Material Conductivity"]
description: "Liquid water transport coefficients and capillary conductivity relationships for porous building materials including measurement methods, moisture-dependent properties, and hygrothermal modeling parameters"
weight: 2
---

## Overview

Material conductivity for liquid water transport quantifies the ability of porous building materials to conduct moisture in the liquid phase under capillary suction and moisture gradients. This property, distinct from vapor diffusion, governs liquid water movement through interconnected pore networks and determines redistribution rates, drying potential, and moisture accumulation patterns in building envelopes.

The liquid transport coefficient represents a fundamental hygrothermal material property required for accurate moisture analysis in wall assemblies, roof systems, and foundation structures where capillary action drives moisture movement.

## Physical Mechanisms

### Capillary Transport Physics

Liquid water movement in porous materials occurs through multiple interconnected mechanisms:

**Primary driving forces:**
- Capillary suction gradients (dominant in unsaturated conditions)
- Moisture content gradients
- Temperature-induced flow
- Gravity effects (vertical assemblies)

**Pore-scale phenomena:**
- Capillary meniscus formation and movement
- Film flow along pore walls
- Corner flow in angular pores
- Hygroscopic moisture redistribution

The liquid flux density follows a diffusion-like relationship:

**q_l = -D_w × ∂w/∂x**

Where:
- q_l = liquid moisture flux density (kg/m²·s)
- D_w = liquid transport coefficient (m²/s)
- w = volumetric moisture content (kg/m³)
- x = spatial coordinate (m)

### Moisture-Dependent Conductivity

Liquid transport coefficients exhibit strong dependence on moisture content, typically spanning several orders of magnitude across the moisture range:

**D_w(w) = D_ws × f(w)**

Where:
- D_ws = liquid transport coefficient at saturation
- f(w) = dimensionless moisture function

The moisture function commonly follows exponential or power-law relationships:

**f(w) = [(w - w_h)/(w_cap - w_h)]^n**

Where:
- w_h = hygroscopic moisture content (kg/m³)
- w_cap = capillary saturation moisture content (kg/m³)
- n = material-specific exponent (typically 5-15)

## Transport Coefficient Relationships

### Suction-Based Formulation

The capillary conductivity relates directly to the moisture retention curve through the Darcy-Buckingham relationship:

**K(ψ) = k_rel(ψ) × K_sat**

Where:
- K(ψ) = capillary conductivity as function of suction (kg/m·s·Pa)
- k_rel(ψ) = relative conductivity (dimensionless)
- K_sat = saturated conductivity (kg/m·s·Pa)
- ψ = capillary suction pressure (Pa)

### Diffusivity-Conductivity Relationship

The liquid diffusivity relates to capillary conductivity:

**D_w = K(ψ) × (dψ/dw)**

Where:
- dψ/dw = slope of moisture retention curve (Pa·m³/kg)

This relationship links the transport coefficient to fundamental pore structure characteristics through the retention curve.

## Material-Specific Properties

### Clay Brick and Masonry

Clay brick exhibits relatively high liquid transport coefficients due to connected capillary pore networks:

| Moisture Content (w/w_cap) | D_w (m²/s) | Relative Conductivity |
|---------------------------|------------|----------------------|
| 0.95 - 1.0 (near saturation) | 1×10⁻⁷ to 5×10⁻⁷ | 1.0 |
| 0.80 - 0.95 | 5×10⁻⁸ to 1×10⁻⁷ | 0.2 - 0.5 |
| 0.60 - 0.80 | 1×10⁻⁸ to 5×10⁻⁸ | 0.05 - 0.2 |
| 0.40 - 0.60 | 1×10⁻⁹ to 1×10⁻⁸ | 0.005 - 0.05 |
| 0.20 - 0.40 | 1×10⁻¹⁰ to 1×10⁻⁹ | 0.0005 - 0.005 |
| < 0.20 (hygroscopic range) | < 1×10⁻¹⁰ | < 0.0005 |

**Typical parameters for red clay brick:**
- D_ws (saturated): 2×10⁻⁷ m²/s
- Exponent n: 8-12
- Capillary saturation: 150-200 kg/m³
- Hygroscopic moisture: 2-5 kg/m³

### Concrete Materials

Concrete liquid transport varies significantly with mix design, water/cement ratio, and age:

**Normal concrete (w/c = 0.50):**
- Saturated conductivity: 5×10⁻⁸ to 2×10⁻⁷ m²/s
- Moisture exponent: 10-15
- Strong aging effects (decreasing conductivity)

**High-performance concrete (w/c = 0.35):**
- Saturated conductivity: 1×10⁻⁹ to 1×10⁻⁸ m²/s
- Moisture exponent: 12-18
- Very low conductivity in partially saturated state

| Concrete Type | D_ws (m²/s) | w_cap (kg/m³) | Exponent n |
|---------------|-------------|---------------|------------|
| Normal (w/c 0.55) | 2×10⁻⁷ | 120-140 | 10-12 |
| Medium (w/c 0.45) | 5×10⁻⁸ | 100-120 | 12-15 |
| High-perf (w/c 0.35) | 5×10⁻⁹ | 80-100 | 15-18 |
| Lightweight | 5×10⁻⁷ to 2×10⁻⁶ | 200-400 | 6-10 |

### Wood and Wood-Based Materials

Wood exhibits anisotropic liquid transport with distinct longitudinal, radial, and tangential coefficients:

**Softwood (pine, spruce):**

| Direction | D_ws (m²/s) | Relative Magnitude |
|-----------|-------------|-------------------|
| Longitudinal | 1×10⁻⁶ to 5×10⁻⁶ | 100-500× |
| Radial | 5×10⁻⁹ to 2×10⁻⁸ | 5-20× |
| Tangential | 1×10⁻⁹ to 5×10⁻⁹ | 1× (reference) |

**Hardwood (oak, maple):**
- Generally lower transport coefficients
- More pronounced anisotropy
- Vessel structure creates preferential paths

**Engineered wood products:**

| Material | D_ws (m²/s) | w_cap (kg/m³) | Notes |
|----------|-------------|---------------|-------|
| Plywood | 2×10⁻⁸ to 1×10⁻⁷ | 400-500 | Glue layer effects |
| OSB | 5×10⁻⁸ to 3×10⁻⁷ | 500-600 | High variability |
| Particleboard | 1×10⁻⁷ to 5×10⁻⁷ | 600-800 | Rapid capillary uptake |
| MDF | 3×10⁻⁸ to 2×10⁻⁷ | 700-900 | Density dependent |

### Insulation Materials

Most fibrous and foam insulations exhibit very low liquid transport coefficients:

**Mineral wool:**
- D_ws: 1×10⁻⁸ to 1×10⁻⁷ m²/s
- Primarily gravity drainage, limited capillary action
- Moisture retention: 1-5 kg/m³ at typical RH

**Cellular glass:**
- Effectively zero liquid conductivity (closed cells)
- Transport only through cracks or damaged cells

**Wood fiber insulation:**
- D_ws: 5×10⁻⁸ to 3×10⁻⁷ m²/s
- Hygroscopic buffering capacity
- Moderate capillary redistribution

## Temperature Dependence

Liquid transport coefficients increase with temperature due to reduced viscosity and increased molecular mobility:

**D_w(T) = D_w(T_ref) × exp[β(T - T_ref)]**

Where:
- T = temperature (°C)
- T_ref = reference temperature, typically 23°C
- β = temperature coefficient (1/°C), typically 0.02-0.04

**Viscosity correction approach:**

**D_w(T) = D_w(T_ref) × [η(T_ref)/η(T)]**

Where:
- η(T) = dynamic viscosity of water at temperature T

For water between 0-50°C:
- At 0°C: η = 1.79 mPa·s (relative factor: 1.77)
- At 10°C: η = 1.31 mPa·s (relative factor: 1.30)
- At 20°C: η = 1.00 mPa·s (relative factor: 1.00, reference)
- At 30°C: η = 0.80 mPa·s (relative factor: 0.80)
- At 40°C: η = 0.65 mPa·s (relative factor: 0.65)

This produces approximately 10-15% change in liquid conductivity per 10°C temperature change.

## Measurement Methods

### Cup Test Methods

Modified cup tests determine liquid transport coefficients through controlled moisture gradients:

**Experimental setup:**
- Material sample with defined thickness
- Known moisture content gradient
- Steady-state flux measurement
- Temperature control

**Calculation:**

**D_w = (q_l × Δx)/(Δw)**

Where:
- Δx = sample thickness (m)
- Δw = moisture content difference (kg/m³)

### Absorption-Desorption Methods

**Capillary absorption test:**
- Measures water uptake rate versus time
- Determines A-value (kg/m²·s^0.5)
- Relates to liquid conductivity through:

**A² = D_w × w_cap × ρ_dry**

Where:
- ρ_dry = dry density (kg/m³)

**Pressure plate extraction:**
- Establishes moisture retention curve ψ(w)
- Combined with instantaneous profile method
- Yields K(ψ) relationship

### Nuclear Magnetic Resonance (NMR)

Advanced technique for direct measurement of moisture profiles:

**Advantages:**
- Non-destructive monitoring
- High spatial resolution (sub-millimeter)
- Distinguishes liquid phases

**Application:**
- Transient absorption experiments
- Inverse analysis for D_w(w)
- Validation of exponential models

### Inverse Modeling

Numerical optimization determines transport coefficients from measured moisture profiles:

**Process:**
1. Conduct controlled wetting/drying experiment
2. Measure moisture profiles at multiple times
3. Run hygrothermal simulation with variable D_w parameters
4. Minimize objective function between measured and simulated profiles
5. Extract optimized D_w(w) relationship

**Objective function:**

**F = Σ[w_measured(x,t) - w_simulated(x,t)]²**

## Hygrothermal Modeling Applications

### Moisture Balance Equation

Liquid transport coefficient appears in the comprehensive moisture balance:

**∂w/∂t = ∂/∂x[D_w × ∂w/∂x] + ∂/∂x[δ_p × ∂p_v/∂x]**

Where:
- First term: liquid transport
- Second term: vapor diffusion
- δ_p = vapor permeability (kg/m·s·Pa)
- p_v = vapor pressure (Pa)

### Coupled Heat-Moisture Transport

**Energy balance including liquid transport:**

**ρc × ∂T/∂t = ∂/∂x[λ × ∂T/∂x] + L_v × ∂/∂x[D_w × ∂w/∂x] + L_v × ∂/∂x[δ_p × ∂p_v/∂x]**

Where:
- ρc = volumetric heat capacity (J/m³·K)
- λ = thermal conductivity (W/m·K)
- L_v = latent heat of vaporization (J/kg)

The latent heat terms couple liquid and vapor transport to the thermal field.

### Numerical Implementation

Finite difference formulation for liquid transport:

**w_i^(n+1) = w_i^n + (Δt/Δx²)[D_(i+1/2) × (w_(i+1)^n - w_i^n) - D_(i-1/2) × (w_i^n - w_(i-1)^n)]**

Where:
- Subscript i denotes spatial node
- Superscript n denotes time step
- D_(i+1/2) = 0.5 × [D_w(w_i) + D_w(w_(i+1))]

**Stability criterion:**

**Δt ≤ (Δx²)/(2 × D_w,max)**

## Design Considerations

### Material Selection

**Low liquid conductivity materials (protective functions):**
- Exterior water-resistive barriers
- Capillary breaks in foundations
- Drainage plane materials
- Face-sealed cladding systems

**High liquid conductivity materials (redistribution functions):**
- Interior hygroscopic buffers
- Moisture-redistributing layers
- Capillary-active insulation systems
- Drying-optimized assemblies

### Assembly Design

**Capillary break placement:**

Position materials with D_w ratios > 100:1 to interrupt liquid transport:
- Foundation-to-wall transition
- Below-grade to above-grade
- Masonry veneer cavities
- Roof-to-wall interfaces

**Liquid transport pathways:**

Analyze dominant moisture paths:
1. Identify highest conductivity materials
2. Check moisture content operating ranges
3. Verify drying direction alignment
4. Confirm capillary break effectiveness

### Drying Potential

The drying rate from liquid-saturated conditions depends on liquid conductivity:

**t_dry ∝ L²/(D_w × Δw)**

Where:
- L = characteristic dimension (m)
- Δw = moisture content driving force (kg/m³)

**Example calculation for brick wall (100mm thick):**
- D_w,avg = 5×10⁻⁸ m²/s
- Δw = 100 kg/m³ (from 150 to 50 kg/m³)
- t_dry ≈ (0.1)²/(5×10⁻⁸ × 100) = 2×10⁶ s ≈ 23 days

This represents liquid redistribution time; complete drying requires additional vapor diffusion.

### Freeze-Thaw Considerations

High liquid conductivity in cold climates presents freeze-thaw risks:

**Critical moisture content:**

**w_crit = 0.9 × w_cap**

Above this threshold, freezing can generate damaging expansion stresses.

**Mitigation strategies:**
- Specify low-conductivity outer layers
- Provide adequate drainage
- Include capillary breaks
- Design for rapid spring drying

## ASHRAE and Code References

### ASHRAE Standards

**ASHRAE Standard 160 - Criteria for Moisture-Control Design Analysis:**
- References liquid transport coefficients for hygrothermal modeling
- Specifies material property requirements for simulation
- Defines acceptable moisture performance criteria

**ASHRAE Research Project RP-1325:**
- Compiled liquid transport data for common materials
- Established measurement protocols
- Created material property database

### ISO Standards

**ISO 15148 - Hygrothermal Performance of Building Materials and Products:**
- Standard test method for water absorption coefficient
- Relates A-value to liquid transport coefficient
- Specifies specimen preparation and conditioning

**ISO 12572 - Water Vapor Permeability:**
- Complementary to liquid transport measurement
- Combined analysis for full moisture transport characterization

### Modeling Tools

Software packages requiring liquid transport coefficients:

**WUFI (Wärme Und Feuchte Instationär):**
- Comprehensive hygrothermal simulation
- Built-in material database with D_w(w) functions
- Validated against field measurements

**DELPHIN:**
- Advanced coupled heat-moisture-salt transport
- User-defined transport functions
- Research-oriented platform

**COMSOL Multiphysics:**
- Custom PDE implementation
- Moisture-dependent property functions
- Couples to structural, thermal, and other physics

## Quality Control and Validation

### Material Variability

Liquid transport coefficients exhibit significant batch-to-batch variation:

**Typical coefficient of variation (COV):**
- Clay brick: 30-50%
- Concrete: 40-70%
- Wood products: 50-100%
- Engineered materials: 20-40%

**Sampling requirements:**
- Minimum 5 specimens per batch
- Test multiple moisture content levels
- Document manufacturing source
- Record environmental conditioning history

### Measurement Uncertainty

**Sources of uncertainty:**
- Moisture content determination: ±5-10%
- Flux measurement: ±10-15%
- Specimen geometry: ±2-5%
- Temperature control: ±3-8%

**Combined uncertainty:**
- Typical range: ±25-40% for D_w determination
- Improved to ±15-25% with advanced techniques

### Validation Approaches

**Component-level validation:**
1. Conduct controlled wetting experiments
2. Measure moisture profiles at multiple times
3. Compare to simulated profiles using measured D_w
4. Adjust parameters within uncertainty bounds

**Assembly-level validation:**
- Field monitoring of wall sections
- Embedded moisture sensors
- Multi-year data collection
- Inverse calibration of transport properties

## Advanced Topics

### Hysteresis Effects

Liquid transport coefficients differ between wetting and drying:

**D_w,wetting > D_w,drying** (at same moisture content)

**Hysteresis ratio:**

**HR = D_w,wetting / D_w,drying**

Typical values: 1.5-3.0 for most porous materials

**Modeling approaches:**
- Separate wetting/drying functions
- History-dependent conductivity
- Main curve with scanning curves

### Multi-Phase Transport

In saturated or near-saturated conditions, air phase affects liquid transport:

**Effective liquid conductivity:**

**D_w,eff = D_w × (1 - S_a)**

Where:
- S_a = air saturation (fraction of pore space occupied by air)

Trapped air reduces effective conductivity by 20-50% in field conditions.

### Salt Effects

Dissolved salts alter liquid transport through:
- Viscosity changes
- Surface tension modification
- Pore structure degradation

**Salt-laden materials:**
- 10-30% increase in D_w at moderate salt concentrations
- Crystallization damage creates new transport pathways
- Long-term conductivity increases in masonry

## Summary

Material conductivity for liquid water transport represents a critical hygrothermal property governing moisture redistribution, drying rates, and moisture accumulation in building assemblies. The strong moisture dependence, spanning orders of magnitude, necessitates careful characterization across the full moisture range. Proper application of liquid transport coefficients in hygrothermal modeling enables accurate prediction of envelope moisture performance and informs material selection and assembly design decisions.

**Key engineering parameters:**
- Saturated conductivity D_ws: 10⁻⁹ to 10⁻⁶ m²/s (material dependent)
- Moisture exponent n: 5-18 (controls shape of D_w(w) function)
- Temperature coefficient: 2-4%/°C
- Measurement uncertainty: ±25-40% typical

**Design applications:**
- Drying time estimation
- Capillary break placement
- Material compatibility analysis
- Freeze-thaw risk assessment
- Hygrothermal simulation input data
