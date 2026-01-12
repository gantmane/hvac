---
title: "Moisture Storage Functions"
description: "Sorption isotherms, hysteresis, capillary suction curves, and moisture capacity for hygrothermal analysis. Material moisture storage data for WUFI simulation and building envelope design."
weight: 3
---

Moisture storage functions describe the equilibrium relationship between moisture content and relative humidity or capillary pressure in building materials. These functions are fundamental inputs for hygrothermal simulation tools like WUFI, DELPHIN, and COMSOL, enabling prediction of moisture accumulation, drying potential, and durability performance in building assemblies.

## Sorption Isotherms

Sorption isotherms represent the equilibrium moisture content of a material as a function of relative humidity at constant temperature. The moisture content is expressed as mass of water per mass of dry material (kg/kg) or volumetric moisture content (m³/m³).

### Hygroscopic Range

In the hygroscopic range (0-95% RH), moisture is stored in pores through:

**Monolayer Adsorption** - Water molecules form a single layer on pore surfaces at low RH (<20%). The BET (Brunauer-Emmett-Teller) equation describes this region:

w = (w_m × C × φ) / ((1 - φ) × (1 + (C - 1) × φ))

Where:
- w = moisture content (kg/kg)
- w_m = monolayer capacity (kg/kg)
- C = energy constant
- φ = relative humidity (0-1)

**Multilayer Adsorption** - Additional water layers form at moderate RH (20-60%). Materials with high specific surface area (fibrous insulation, lightweight concrete) store significant moisture in this range.

**Capillary Condensation** - Water condenses in small pores at high RH (60-95%). The Kelvin equation relates pore radius to condensation RH:

r = (2 × σ × V_m) / (R × T × ln(φ))

Where:
- r = pore radius (m)
- σ = surface tension (N/m)
- V_m = molar volume of water (m³/mol)
- R = gas constant (J/mol·K)
- T = temperature (K)

### Empirical Sorption Models

Several equations fit experimental sorption data across the full hygroscopic range:

| Model | Equation | Parameters | Best For |
|-------|----------|------------|----------|
| GAB | w = (w_m×C×k×φ)/((1-k×φ)×(1+(C-1)×k×φ)) | w_m, C, k | Wood products, organics |
| Hansen | w = (A×φ)/(1-k×φ) + (B×φ)^n | A, B, k, n | Concrete, masonry |
| Künzel | w = w_f×((b-1)×φ^a)/((b-φ^a)×(1-(1-b)×φ^a)) | w_f, a, b | General purpose (WUFI) |
| Modified Oswin | w = (A×φ^B)/(1-φ)^C | A, B, C | Gypsum, plaster |

The Künzel equation is implemented in WUFI and provides good fits for most building materials with three physically meaningful parameters.

## Sorption Hysteresis

Moisture content at a given RH differs depending on whether the material is adsorbing (increasing moisture) or desorbing (drying). This hysteresis results from:

- **Pore geometry effects** - Capillary condensation and evaporation occur at different RH levels in non-cylindrical pores (ink-bottle effect)
- **Contact angle differences** - Advancing and receding contact angles differ during wetting and drying
- **Air entrapment** - Trapped air prevents full rewetting of previously dried pores

The hysteresis loop is bounded by:
- **Adsorption curve** (lower boundary) - Material increasing in moisture content
- **Desorption curve** (upper boundary) - Material drying from saturated state
- **Scanning curves** - Intermediate paths during partial wetting/drying cycles

For most materials, moisture content on the desorption curve is 1.2-2.0 times higher than the adsorption curve at the same RH. Hygrothermal simulations typically use the desorption curve as it represents the more common field condition.

### Measurement Standards

- **ISO 12571** - Hygroscopic sorption properties (desiccator method, climatic chamber method)
- **ASTM C1498** - Hygroscopic sorption isotherms (dynamic vapor sorption)
- **EN ISO 12571** - Building materials hygrothermal properties

## Capillary Suction Curves

Above 95% RH and in the over-hygroscopic range, liquid water is transported by capillary suction. The moisture storage function in this range is expressed as moisture content versus capillary pressure (suction).

### Capillary Pressure Relationship

Capillary pressure is the pressure difference across the air-water interface in pores:

p_c = p_air - p_water

For cylindrical pores, the Young-Laplace equation relates capillary pressure to pore radius:

p_c = (2 × σ × cos(θ)) / r

Where:
- p_c = capillary pressure (Pa)
- σ = surface tension (0.0728 N/m at 20°C)
- θ = contact angle (typically 0° for water on hydrophilic surfaces)
- r = pore radius (m)

### Retention Curves

The water retention curve (also called moisture retention curve or capillary pressure curve) shows the relationship between volumetric moisture content and capillary pressure.

**van Genuchten Model** - Most widely used for modeling retention curves:

θ = θ_r + (θ_s - θ_r) / (1 + (α × p_c)^n)^m

Where:
- θ = volumetric moisture content (m³/m³)
- θ_r = residual moisture content (m³/m³)
- θ_s = saturated moisture content (m³/m³)
- α = inverse of air entry pressure (1/Pa)
- n, m = pore size distribution parameters (m = 1 - 1/n)

**Brooks-Corey Model** - Alternative formulation:

θ = θ_s × (p_c / p_b)^(-λ) for p_c > p_b
θ = θ_s for p_c ≤ p_b

Where:
- p_b = air entry pressure (Pa)
- λ = pore size distribution index

### Critical Moisture Regions

| Pressure Range | Moisture State | Transport | RH Equivalent |
|----------------|----------------|-----------|---------------|
| 0-1,000 Pa | Free water | Capillary flow | >99.3% |
| 1,000-10,000 Pa | Capillary water | Capillary + vapor | 99.3-93% |
| 10,000-100,000 Pa | Funicular | Reduced capillary | 93-47% |
| >100,000 Pa | Hygroscopic | Vapor diffusion | <47% |

The transition from capillary suction to vapor diffusion typically occurs around 93-95% RH (approximately 10,000 Pa capillary pressure).

## Material Moisture Capacity

Moisture capacity (also called moisture storage capacity or differential water capacity) describes how much moisture content changes for a given change in relative humidity or capillary pressure:

ξ = ∂w/∂φ (kg/kg per unit RH)

or in volumetric terms:

C_m = ∂θ/∂φ (m³/m³ per unit RH)

This property determines:
- **Buffering capacity** - Ability to moderate indoor humidity fluctuations
- **Transient response** - Time required for moisture redistribution
- **Simulation time steps** - Materials with high moisture capacity require smaller time steps

Moisture capacity varies significantly with RH. Most materials show peak capacity at 80-95% RH where capillary condensation is most active.

## Representative Moisture Storage Data

### Wood and Wood-Based Materials

| Material | w at 50% RH | w at 80% RH | w_max (kg/m³) | Notes |
|----------|-------------|-------------|---------------|-------|
| Softwood (spruce) | 0.090 kg/kg | 0.180 kg/kg | 350-400 | Strong hysteresis |
| Hardwood (oak) | 0.085 kg/kg | 0.165 kg/kg | 400-450 | Denser, lower porosity |
| Plywood | 0.080 kg/kg | 0.155 kg/kg | 320-380 | Depends on adhesive |
| OSB | 0.075 kg/kg | 0.145 kg/kg | 280-340 | Lower sorption than solid wood |
| Particle board | 0.095 kg/kg | 0.190 kg/kg | 340-400 | High surface area |
| MDF | 0.085 kg/kg | 0.170 kg/kg | 320-380 | Uniform pore structure |

### Masonry and Concrete

| Material | w at 80% RH | w_max (kg/m³) | θ_cap (vol%) | A-value (kg/m²·s^0.5) |
|----------|-------------|---------------|--------------|------------------------|
| Fired clay brick | 0.015-0.030 | 150-250 | 25-35% | 0.10-0.25 |
| Calcium silicate brick | 0.030-0.045 | 180-300 | 28-40% | 0.25-0.50 |
| Concrete block (standard) | 0.020-0.035 | 120-180 | 15-22% | 0.08-0.15 |
| AAC (autoclaved aerated) | 0.050-0.080 | 300-450 | 60-80% | 0.30-0.60 |
| Normal concrete (3000 psi) | 0.025-0.040 | 60-95 | 12-18% | 0.05-0.12 |
| Lightweight concrete | 0.040-0.065 | 140-220 | 25-38% | 0.15-0.35 |

### Insulation Materials

| Material | w at 80% RH | w_max (vol%) | μ-value (dry) | Hydrophobic |
|----------|-------------|--------------|---------------|-------------|
| Mineral wool (stone) | 0.003-0.008 | <5% | 1.1-1.5 | No |
| Fiberglass | 0.002-0.006 | <3% | 1.0-1.3 | No |
| Cellulose (treated) | 0.080-0.140 | 25-35% | 1.5-2.5 | No |
| EPS (expanded polystyrene) | <0.001 | <2% | 30-70 | Yes |
| XPS (extruded polystyrene) | <0.001 | <1% | 80-250 | Yes |
| Polyurethane foam (closed) | <0.001 | <2% | 40-100 | Yes |
| Phenolic foam | 0.002-0.005 | <3% | 30-60 | Moderate |

### Gypsum and Plaster Materials

| Material | w at 50% RH | w at 80% RH | w_max (kg/m³) | Moisture buffering |
|----------|-------------|-------------|---------------|--------------------|
| Gypsum board (standard) | 0.007 kg/kg | 0.015 kg/kg | 80-120 | Good |
| Gypsum plaster | 0.006 kg/kg | 0.012 kg/kg | 60-90 | Good |
| Lime plaster | 0.008 kg/kg | 0.018 kg/kg | 90-140 | Excellent |
| Cement plaster | 0.005 kg/kg | 0.011 kg/kg | 70-110 | Moderate |
| Clay plaster | 0.012 kg/kg | 0.028 kg/kg | 120-180 | Excellent |

## WUFI Database Parameters

WUFI (Wärme Und Feuchte Instationär - Heat and Moisture Transient) requires specific moisture storage parameters:

**Free Water Saturation (w_f)** - Maximum moisture content by capillary saturation (kg/m³)

**Moisture Storage Function** - Künzel equation parameters:
- w_80 - moisture content at 80% RH (kg/m³)
- b - shape parameter (typically 5-15)

**Typical Derivation**:
1. Measure sorption isotherm (minimum 5 RH points from 30-95%)
2. Determine capillary saturation by vacuum saturation test (EN ISO 15148)
3. Fit Künzel equation to measured data
4. Validate against independent test points

## Measurement Methods

### Desiccator Method (Gravimetric)

Standard method per ISO 12571:
1. Condition samples over saturated salt solutions at controlled temperature
2. Weigh samples periodically until mass equilibrium (<0.1% change in 7 days)
3. Calculate moisture content: w = (m_wet - m_dry) / m_dry
4. Plot w versus RH for each salt solution

Common salt solutions:

| Salt | RH at 23°C | Application |
|------|------------|-------------|
| LiCl | 11% | Low RH point |
| MgCl₂ | 33% | Lower hygroscopic |
| Mg(NO₃)₂ | 54% | Mid-range |
| NaCl | 75% | Upper hygroscopic |
| KCl | 85% | Near-capillary transition |
| K₂SO₄ | 97% | Capillary range |

### Dynamic Vapor Sorption (DVS)

Automated method providing high-resolution isotherms:
- Sample mass: 10-100 mg
- RH control: ±0.5%
- Resolution: 0.1 μg
- Time: 24-72 hours for full isotherm
- Provides both adsorption and desorption curves

### Pressure Plate Method

For capillary pressure curves (over-hygroscopic range):
1. Saturate sample on porous ceramic plate
2. Apply known air pressure (1-1500 kPa)
3. Allow water to drain until equilibrium
4. Measure moisture content gravimetrically
5. Repeat for multiple pressure steps

Equivalent to RH range of 99.3% (1 kPa) to 0.1% (1500 kPa).

### Centrifuge Method

Rapid determination of retention curves:
- Centrifugal force simulates capillary pressure
- Higher rotation speed = higher suction
- Faster than pressure plate (hours vs. weeks)
- Limited to relatively permeable materials

## Temperature Dependence

Moisture storage functions vary with temperature due to:

**Surface Energy Changes** - Surface tension decreases with temperature (0.0758 N/m at 0°C, 0.0728 N/m at 20°C, 0.0589 N/m at 100°C)

**Isosteric Heat of Sorption** - Energy released during adsorption, typically 2000-5000 J/mol above heat of vaporization for building materials

**Kelvin Effect** - Higher temperature shifts capillary condensation to higher RH

For most hygrothermal simulations in building envelopes (temperature range -20°C to +60°C), moisture storage functions measured at 23°C provide acceptable accuracy. For extreme conditions, temperature corrections using the Clausius-Clapeyron equation are necessary.

## Practical Applications

### Assembly Design

Materials with high moisture storage capacity at the operating RH range provide:
- Buffering against transient moisture loads
- Reduced peak RH and condensation risk
- Improved drying reservoir after wetting events

Place hygroscopic materials (wood sheathing, cellulose insulation, mineral wool) toward the interior where they buffer indoor humidity fluctuations.

### Simulation Inputs

Accurate moisture storage functions are critical for:
- Predicting mold growth risk (depends on surface RH)
- Freeze-thaw damage assessment (requires accurate moisture content)
- Drying time calculations (governed by storage and transport properties)
- Retrofit analysis (existing moisture must redistribute)

### Quality Control

Verify manufacturer-provided data:
- Check w_80 against published ranges for material type
- Ensure w_f is less than total porosity
- Validate that desorption curve is above adsorption curve
- Compare capillary absorption coefficient with moisture storage capacity

Inconsistent data leads to simulation errors, particularly overprediction of moisture accumulation or underprediction of drying rates.
