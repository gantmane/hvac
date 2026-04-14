---
title: "Liquid Water Conductivity"
aliases: ["Liquid Water Conductivity"]
description: "Liquid water conductivity in building materials governs capillary moisture transport through porous building envelope assemblies. Critical hygrothermal property for WUFI modeling and moisture analysis in walls, roofs, and foundation systems."
weight: 4
---

Liquid water conductivity quantifies the rate at which liquid moisture moves through porous building materials under capillary pressure gradients. This transport property dominates moisture behavior when materials reach high moisture contents, particularly during rain penetration, capillary rise from foundations, and condensation accumulation within building assemblies.

## Fundamental Transport Mechanism

Liquid water transport in porous building materials occurs through capillary action in the interconnected pore network. The driving force is the gradient in capillary pressure (suction), which pulls moisture from regions of higher moisture content toward drier regions.

The governing equation for liquid transport follows Darcy's law for unsaturated porous media:

**g_w = -K_l(w) · ∇p_c**

Where:
- g_w = liquid water flux (kg/m²·s)
- K_l(w) = liquid water conductivity as function of moisture content (kg/m·s·Pa)
- ∇p_c = capillary pressure gradient (Pa/m)

The negative sign indicates flow from high pressure (wet) to low pressure (dry) regions.

## Moisture Content Dependency

Liquid water conductivity is not a constant material property but varies dramatically with moisture content. The relationship is typically highly nonlinear:

**K_l(w) = K_sat · [w/w_sat]^n**

Where:
- K_sat = saturated liquid conductivity (kg/m·s·Pa)
- w = actual moisture content (kg/m³)
- w_sat = saturated moisture content (kg/m³)
- n = empirical exponent (typically 3-10)

At low moisture contents, conductivity approaches zero because capillary pathways become disconnected. As moisture content increases, conductivity rises exponentially as more pore pathways fill with liquid water.

## Capillary Transport Regimes

### Pendular Regime
At low moisture contents, liquid exists only at contact points between particles as pendular rings. Transport is minimal because continuous liquid pathways do not exist. Vapor diffusion dominates in this regime.

### Funicular Regime
As moisture content increases, liquid bridges form between pores, creating continuous transport pathways. Liquid conductivity increases rapidly. This is the primary regime for most moisture transport in building materials.

### Capillary Saturated
At very high moisture contents approaching saturation, nearly all pores are filled. Conductivity reaches its maximum value but remains dependent on pore structure and connectivity.

## Relationship to Capillary Pressure

Liquid water conductivity can also be expressed as a function of capillary pressure (suction):

**K_l(p_c) = K_sat · [p_c,entry/p_c]^m**

Where:
- p_c,entry = air entry pressure (Pa)
- m = pore size distribution parameter

This formulation directly links conductivity to the moisture retention curve. Materials with narrow pore size distributions show steeper conductivity functions.

## Measurement Methods

### Cup Method with Moisture Content Monitoring
Traditional cup methods can be extended to measure liquid conductivity by monitoring transient moisture redistribution in samples with known initial moisture gradients. This requires:
- Gamma-ray attenuation for moisture profiling
- Nuclear magnetic resonance (NMR) imaging
- Time-domain reflectometry (TDR) sensors

### Pressure Plate Extraction
Centrifuge or pressure plate apparatus can determine conductivity by measuring steady-state flow rates under applied pressure differences at controlled moisture contents.

### Instantaneous Profile Method
Non-destructive measurement during redistribution experiments. Material samples are wetted, sealed, and allowed to redistribute moisture while monitoring internal moisture profiles and total mass.

### Inverse Analysis from Hygrothermal Modeling
WUFI and similar hygrothermal models can determine liquid conductivity functions through inverse parameter estimation by matching simulated and measured moisture responses.

## WUFI Simulation Parameters

Hygrothermal simulation programs require liquid water conductivity as input data. WUFI uses a simplified exponential function:

**D_w(w) = D_ww · [w_cap - w_80/w_cap - w_free]^[-1]**

Where:
- D_w = moisture-dependent liquid transport coefficient (m²/s)
- D_ww = liquid transport coefficient at saturation (m²/s)
- w_cap = capillary saturation moisture content (kg/m³)
- w_80 = moisture content at 80% RH (kg/m³)
- w_free = free water saturation (kg/m³)

The liquid transport coefficient D_w relates to liquid conductivity K_l through:

**D_w = K_l · (dp_c/dw)**

This formulation accounts for the moisture retention curve characteristics.

## Material Conductivity Values

### Common Building Materials

| Material | K_sat (kg/m·s·Pa) | Exponent n | Notes |
|----------|-------------------|------------|-------|
| Brick (clay, solid) | 1.5-3.0 × 10⁻¹¹ | 4-6 | Higher for pressed brick |
| Concrete (normal) | 0.8-2.0 × 10⁻¹¹ | 6-8 | Density dependent |
| Concrete block | 1.0-2.5 × 10⁻¹¹ | 5-7 | Lower for lightweight |
| Mortar (cement) | 2.0-5.0 × 10⁻¹¹ | 4-6 | Sand ratio affects value |
| Wood (softwood) | 1.0-3.0 × 10⁻¹² | 8-12 | Anisotropic property |
| Wood (hardwood) | 0.5-1.5 × 10⁻¹² | 10-15 | Denser species lower |
| Cellular concrete | 3.0-8.0 × 10⁻¹¹ | 4-5 | High porosity increases |

### Insulation Materials

| Material | K_sat (kg/m·s·Pa) | Exponent n | Notes |
|----------|-------------------|------------|-------|
| Mineral wool | 8.0-15 × 10⁻¹¹ | 3-4 | Open pore structure |
| EPS (expanded polystyrene) | 1.0-2.0 × 10⁻¹³ | 15-20 | Nearly impermeable |
| XPS (extruded polystyrene) | 5.0-10 × 10⁻¹⁴ | 20-25 | Closed cell structure |
| Cellulose (blown) | 4.0-8.0 × 10⁻¹¹ | 4-6 | Settles over time |
| Fiberglass (batt) | 6.0-12 × 10⁻¹¹ | 3-4 | Similar to mineral wool |
| Polyisocyanurate | 1.0-3.0 × 10⁻¹³ | 18-22 | Foil facers reduce further |

### Membrane and Sheathing Materials

| Material | K_sat (kg/m·s·Pa) | Exponent n | Notes |
|----------|-------------------|------------|-------|
| OSB (oriented strand board) | 2.0-4.0 × 10⁻¹² | 8-10 | Resin content critical |
| Plywood | 1.5-3.0 × 10⁻¹² | 9-12 | Glue layers reduce |
| Gypsum board | 3.0-6.0 × 10⁻¹¹ | 5-7 | Paper facing increases |
| Cement board | 1.5-3.0 × 10⁻¹¹ | 6-8 | Fiber reinforcement affects |
| Building paper | 1.0-2.0 × 10⁻¹⁰ | 2-3 | Very permeable |
| WRB (spunbonded) | 5.0-10 × 10⁻¹¹ | 3-4 | Product specific |

## Design Implications

### Rain Penetration Analysis
Liquid water conductivity determines how quickly rain that penetrates the exterior cladding can redistribute and potentially reach interior layers. Materials with high conductivity allow rapid moisture spread, while low conductivity materials tend to accumulate moisture locally.

### Capillary Break Design
Effective capillary breaks require materials with liquid conductivity at least 2-3 orders of magnitude lower than adjacent materials. This prevents moisture wicking from foundations or through continuous material bridges.

### Drying Potential
Assembly drying rates depend on liquid conductivity of all layers. A single layer with very low conductivity can act as a moisture trap, preventing liquid moisture from reaching evaporative surfaces even when vapor permeance is adequate.

### Critical Moisture Content
The threshold moisture content where liquid conductivity becomes significant (typically 70-80% RH equivalent) represents a critical design parameter. Assemblies should be designed to remain below this threshold under normal conditions.

## Temperature Dependence

Liquid water conductivity increases with temperature due to reduced viscosity:

**K_l(T) = K_l,ref · [μ(T_ref)/μ(T)]**

Where:
- μ(T) = dynamic viscosity of water at temperature T
- T_ref = reference temperature (typically 20°C)

The viscosity ratio ranges from approximately 0.6 at 0°C to 1.4 at 40°C relative to 20°C. This 2-3× variation is significant for seasonal moisture behavior analysis.

## Hysteresis Effects

Liquid water conductivity exhibits hysteresis between wetting and drying processes. During wetting, larger pores fill first, creating transport pathways. During drying, water retreats from larger pores while smaller pores remain filled, maintaining some conductivity at lower average moisture contents.

The hysteresis effect can result in 2-5× higher apparent conductivity during drying compared to wetting at the same moisture content. Most hygrothermal simulations use a single main curve, typically representing the average behavior.

## Anisotropy in Fibrous Materials

Wood and wood-based materials exhibit highly anisotropic liquid water conductivity:

**K_l,longitudinal / K_l,transverse ≈ 10-100**

This directional dependence results from cellular structure with continuous vessels in the longitudinal direction but limited pit connections in the transverse direction. Hygrothermal modeling of wood-frame assemblies must account for this anisotropy when moisture flow direction varies.

## Quality Assurance for Simulation

When preparing liquid water conductivity data for hygrothermal simulations:

1. Verify conductivity values align with measured moisture retention curves
2. Ensure conductivity approaches zero at w_80 (80% RH moisture content)
3. Check that saturated conductivity matches material permeability data
4. Validate exponent produces reasonable transport rates in critical moisture range
5. Compare simulation results to field or laboratory validation data

Inconsistent conductivity and retention data produces non-physical simulation results with moisture appearing or disappearing within assemblies.

## Interaction with Other Transport Properties

Liquid water conductivity does not act independently but couples with:

- **Vapor permeability**: At intermediate moisture contents, both mechanisms contribute
- **Moisture capacity**: Higher capacity buffers changes in moisture content and pressure gradients
- **Thermal conductivity**: Moisture redistribution affects temperature gradients, which in turn affect moisture transport
- **Air permeability**: Air leakage can transport liquid droplets or deposit condensation that then redistributes by liquid conduction

Comprehensive hygrothermal analysis requires simultaneous solution of coupled heat, air, and moisture transport equations with all material properties properly characterized.
