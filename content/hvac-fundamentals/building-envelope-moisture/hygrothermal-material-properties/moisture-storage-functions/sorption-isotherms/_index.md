---
title: "Sorption Isotherms"
description: "Comprehensive analysis of moisture sorption isotherms for building materials, including thermodynamic principles, classification systems, measurement methods, and application to hygrothermal design and moisture storage prediction."
weight: 1
---

## Fundamental Principles

Sorption isotherms represent the equilibrium relationship between moisture content in a porous building material and the surrounding relative humidity at constant temperature. This relationship is fundamental to understanding moisture storage, transport, and accumulation in building envelopes.

The sorption isotherm describes the material's hygroscopic behavior—its ability to absorb and release water vapor from the air. This characteristic directly influences:

- Moisture buffering capacity
- Hygrothermal performance under cyclic conditions
- Drying potential after wetting events
- Condensation risk assessment
- Material durability and service life

### Thermodynamic Basis

Moisture sorption in porous materials involves multiple physical mechanisms operating simultaneously:

**Surface Adsorption**: Water molecules form monomolecular and multimolecular layers on pore surfaces through van der Waals forces and hydrogen bonding. This mechanism dominates at low relative humidity (RH < 50%).

**Capillary Condensation**: At higher relative humidity, water condenses in small pores where the vapor pressure is reduced below saturation due to meniscus curvature (Kelvin effect). This process becomes significant at RH > 50% and dominates near saturation.

**Solution Effects**: For materials containing hygroscopic salts or other soluble substances, moisture absorption is enhanced by dissolution, reducing water activity and drawing additional moisture from the air.

### Kelvin Equation

The Kelvin equation describes capillary condensation in cylindrical pores:

```
ln(p/p_sat) = -2σV_m cos(θ) / (r·R·T)
```

Where:
- p = vapor pressure in pore
- p_sat = saturation vapor pressure
- σ = surface tension of water (0.0728 N/m at 20°C)
- V_m = molar volume of water (1.8×10⁻⁵ m³/mol)
- θ = contact angle
- r = pore radius (m)
- R = universal gas constant (8.314 J/(mol·K))
- T = absolute temperature (K)

For complete wetting (θ = 0°), this simplifies to:

```
r_critical = -2σV_m / (R·T·ln(RH/100))
```

At 20°C and RH = 95%, critical pore radius is approximately 7.5 nm. Pores smaller than this radius will fill with condensed water.

## Moisture Content Relationships

Moisture content can be expressed on different bases:

**Mass Basis (w)**:
```
w = (m_water / m_dry) × 100%
```

**Volumetric Basis (θ)**:
```
θ = V_water / V_total
```

**Degree of Saturation (S)**:
```
S = V_water / V_pore = θ / n
```

Where n is porosity.

The relationship between mass and volumetric moisture content:

```
θ = w × ρ_dry / ρ_water
```

For hygrothermal calculations, volumetric moisture content is preferred because it directly relates to thermal conductivity changes and moisture storage capacity.

## Brunauer Classification System

The Brunauer-Emmett-Teller (BET) classification categorizes sorption isotherms into five types based on pore structure and surface chemistry. This system, established in 1940, remains the standard framework for characterizing hygroscopic materials.

### Type I Isotherms

**Characteristics**:
- Steep initial rise at low RH
- Plateau or very gradual increase at higher RH
- Limited maximum moisture uptake

**Physical Interpretation**: Microporous materials with pore diameters < 2 nm where monolayer adsorption quickly transitions to pore filling. Once micropores are saturated, little additional sorption occurs.

**Typical Materials**:
- Activated carbon
- Molecular sieves
- Some zeolites
- Highly carbonized materials

**Mathematical Representation** (Langmuir equation):

```
w = w_m · b · RH / (1 + b · RH)
```

Where:
- w = moisture content (kg/kg)
- w_m = monolayer capacity (kg/kg)
- b = adsorption constant related to heat of adsorption
- RH = relative humidity (decimal)

Type I isotherms are rare in building materials but important for specialized applications like desiccant dehumidification systems.

### Type II Isotherms

**Characteristics**:
- Gradual S-shaped curve
- Inflection point (Point B) indicating monolayer completion
- Continuous increase toward saturation
- Most common isotherm type for building materials

**Physical Interpretation**: Non-porous or macroporous materials where multilayer adsorption dominates. The inflection point marks the transition from monolayer to multilayer adsorption. At high RH, capillary condensation in large pores causes accelerated uptake.

**Typical Materials**:
- Wood and wood products
- Gypsum board
- Concrete and masonry
- Mineral fiber insulation
- Cellulose insulation
- Most building envelope materials

**Mathematical Representation** (BET equation):

```
w = (w_m · C · RH) / [(1 - RH)(1 + (C - 1) · RH)]
```

Where:
- C = constant related to heat of adsorption
- Valid typically for RH = 5% to 45%

For extended range, the GAB (Guggenheim-Anderson-de Boer) equation provides better fit:

```
w = (w_m · C · K · RH) / [(1 - K · RH)(1 + (C - 1) · K · RH)]
```

Where K is an additional parameter accounting for multilayer properties.

### Type III Isotherms

**Characteristics**:
- Convex shape with no inflection point
- Very low uptake at low and moderate RH
- Rapid increase only near saturation
- Weak adsorbent-adsorbate interactions

**Physical Interpretation**: Materials where water-surface interaction is weaker than water-water interaction. Adsorption is unfavorable until sufficient moisture accumulates to enable clustering, then rapid uptake occurs.

**Typical Materials**:
- Non-polar polymers
- Bituminous materials
- Some synthetic membranes
- Materials with hydrophobic surfaces

**Relevance**: These materials provide minimal moisture buffering and can be considered hygroscopically inert for practical HVAC applications.

### Type IV Isotherms

**Characteristics**:
- Initial Type II behavior at low RH
- Plateau at intermediate RH
- Hysteresis loop between adsorption and desorption
- Limited uptake at high RH

**Physical Interpretation**: Mesoporous materials (pore diameter 2-50 nm) where capillary condensation occurs in defined pore size ranges. The hysteresis reflects different pore filling and emptying mechanisms—filling proceeds via meniscus advance, while emptying requires pore neck evaporation.

**Typical Materials**:
- Aerated autoclaved concrete (AAC)
- Calcium silicate boards
- Some clay bricks
- Porous ceramics

**Hysteresis Mechanisms**:

The desorption curve typically lies above the adsorption curve at the same RH, meaning materials retain more moisture during drying than they initially absorbed. This results from:

1. **Pore geometry effects**: Ink-bottle pores empty through narrow necks
2. **Contact angle hysteresis**: Advancing and receding contact angles differ
3. **Irreversible pore structure changes**: Swelling or shrinkage

Hysteresis magnitude depends on pore size distribution and connectivity.

### Type V Isotherms

**Characteristics**:
- Convex initial portion similar to Type III
- S-shaped curve development
- Hysteresis at moderate to high RH
- Weak surface interaction

**Physical Interpretation**: Mesoporous materials with weak adsorbent-adsorbate interaction. Combines features of Type III (weak bonding) and Type IV (defined pore structure).

**Typical Materials**:
- Some activated carbons with specific treatments
- Rare in conventional building materials

## Hysteresis Phenomena

Hysteresis—the difference between adsorption and desorption isotherms—is critical for accurate hygrothermal modeling.

### Quantification of Hysteresis

**Hysteresis Index (HI)**:

```
HI = (A_des - A_ads) / A_des × 100%
```

Where A_des and A_ads are areas under desorption and adsorption curves, respectively.

Typical values:
- Wood: HI = 10-15%
- Concrete: HI = 15-25%
- AAC: HI = 25-35%
- Brick: HI = 20-30%

### Scanning Curves

Real hygrothermal conditions involve partial wetting and drying cycles, creating scanning curves between the main adsorption and desorption isotherms. Several models predict scanning behavior:

**Independent Domain Model**: Assumes pores fill/empty independently
**Dependent Domain Model**: Accounts for pore connectivity effects

For practical calculations, simplified approaches:

1. **Main curves**: Use full hysteresis loop for major cycles
2. **First approximation**: Assume scanning curves parallel to main curves
3. **Advanced models**: Implement pore network simulations

## Representative Sorption Isotherm Data

### Wood Products

| Material | Moisture Content (% by mass) at RH | | | | | |
|----------|-----|-----|-----|-----|-----|-----|
| | 30% | 50% | 65% | 80% | 90% | 95% |
| Softwood (spruce, pine) | 6.0 | 9.0 | 12.0 | 16.5 | 21.0 | 25.0 |
| Hardwood (oak, maple) | 5.5 | 8.5 | 11.5 | 16.0 | 20.5 | 24.5 |
| Plywood | 5.0 | 8.0 | 11.0 | 15.5 | 20.0 | 24.0 |
| OSB | 4.5 | 7.5 | 10.5 | 15.0 | 19.5 | 23.5 |
| Fiberboard (MDF) | 6.5 | 10.0 | 13.5 | 18.5 | 23.5 | 27.5 |

Temperature effect: Moisture content decreases approximately 0.01-0.02% per °C temperature increase at constant RH.

### Masonry and Concrete Materials

| Material | Moisture Content (kg/m³) at RH | | | | | |
|----------|-----|-----|-----|-----|-----|-----|
| | 30% | 50% | 65% | 80% | 90% | 95% |
| Dense concrete | 8 | 12 | 18 | 30 | 48 | 70 |
| Lightweight concrete | 15 | 25 | 40 | 70 | 110 | 145 |
| Autoclaved aerated concrete | 12 | 22 | 38 | 85 | 160 | 220 |
| Clay brick (fired) | 3 | 5 | 8 | 15 | 30 | 50 |
| Calcium silicate brick | 6 | 10 | 18 | 40 | 80 | 120 |
| Cement mortar | 10 | 16 | 25 | 45 | 75 | 105 |

### Insulation Materials

| Material | Moisture Content (kg/m³) at RH | | | | | |
|----------|-----|-----|-----|-----|-----|-----|
| | 30% | 50% | 65% | 80% | 90% | 95% |
| Mineral wool | 0.1 | 0.2 | 0.3 | 0.6 | 1.2 | 2.0 |
| Cellulose insulation | 2.0 | 3.5 | 5.5 | 9.0 | 14.0 | 18.0 |
| Wood fiber insulation | 3.5 | 6.0 | 9.5 | 15.5 | 24.0 | 31.0 |
| EPS (expanded polystyrene) | 0.02 | 0.03 | 0.04 | 0.06 | 0.10 | 0.15 |
| Polyurethane foam | 0.05 | 0.08 | 0.12 | 0.20 | 0.35 | 0.55 |

### Gypsum-Based Materials

| Material | Moisture Content (% by mass) at RH | | | | | |
|----------|-----|-----|-----|-----|-----|-----|
| | 30% | 50% | 65% | 80% | 90% | 95% |
| Gypsum board | 0.3 | 0.6 | 1.0 | 1.8 | 3.2 | 5.0 |
| Gypsum plaster | 0.4 | 0.7 | 1.2 | 2.2 | 4.0 | 6.5 |
| Fiber-reinforced gypsum | 0.5 | 0.9 | 1.5 | 2.8 | 5.0 | 8.0 |

## Measurement Methods

### Standard Test Protocols

**ASTM C1498**: Standard Test Method for Hygroscopic Sorption Isotherms of Building Materials

**ISO 12571**: Hygrothermal performance of building materials and products—Determination of hygroscopic sorption properties

**EN 15026**: Hygrothermal performance of building components and building elements—Assessment of moisture transfer by numerical simulation

### Measurement Techniques

#### Desiccator Method

**Principle**: Specimens equilibrated over saturated salt solutions providing fixed RH environments.

**Procedure**:
1. Prepare samples 10-50 g, thickness 5-10 mm
2. Pre-condition to dry state (105°C until constant mass)
3. Place over salt solutions in sealed desiccators
4. Weigh periodically until equilibrium (Δm < 0.1% in 7 days)
5. Repeat for multiple RH levels

**Standard Salt Solutions**:

| Salt | RH at 23°C | RH at 10°C | RH at 30°C |
|------|------------|------------|------------|
| LiCl | 11.3% | 11.2% | 11.3% |
| CH₃COOK | 23.1% | 24.4% | 22.5% |
| MgCl₂ | 33.1% | 33.5% | 32.4% |
| K₂CO₃ | 43.2% | 43.1% | 43.2% |
| Mg(NO₃)₂ | 54.4% | 57.4% | 51.4% |
| NaCl | 75.5% | 75.7% | 75.1% |
| KCl | 84.3% | 86.8% | 83.6% |
| K₂SO₄ | 97.3% | 98.2% | 96.7% |

**Advantages**: Simple, inexpensive, multiple samples simultaneously
**Disadvantages**: Time-consuming (weeks), limited data points, assumes isothermal conditions

#### Dynamic Vapor Sorption (DVS)

**Principle**: Automated gravimetric measurement with precise RH control.

**Procedure**:
1. Small sample (10-100 mg) placed in microbalance
2. RH ramped in steps (typically 10% increments)
3. Mass monitored continuously
4. Equilibrium defined by dm/dt criterion
5. Complete isotherm generated automatically

**Advantages**: High precision, complete isotherm, adsorption and desorption, temperature control
**Disadvantages**: Expensive equipment, small sample size may not represent heterogeneous materials

#### Pressure Plate Method

**Principle**: Applied suction controls moisture content in contact with liquid water (RH > 98%).

**Application**: Extends sorption measurements into capillary moisture range, bridging hygroscopic and capillary regimes.

## Temperature Dependence

Sorption isotherms shift with temperature due to thermodynamic effects on adsorption energy and vapor pressure.

### Temperature Correction

Empirical correction factor:

```
w(T₂) = w(T₁) × exp[α(T₂ - T₁)]
```

Where:
- α = temperature coefficient (-0.005 to -0.015 K⁻¹ for most materials)
- T in °C

For wood: α ≈ -0.01 K⁻¹
For concrete: α ≈ -0.008 K⁻¹

### Isosteric Heat of Sorption

The isosteric heat of sorption (q_st) quantifies the energy released during adsorption:

```
q_st = R × d(ln p) / d(1/T)|_w
```

At low moisture content, q_st exceeds the latent heat of vaporization (2.45 MJ/kg at 20°C), indicating strong surface binding. As moisture content increases, q_st approaches the latent heat, indicating bulk water behavior.

Typical values:
- Wood at w = 5%: q_st ≈ 3.5 MJ/kg
- Wood at w = 20%: q_st ≈ 2.6 MJ/kg
- Concrete at w = 2 kg/m³: q_st ≈ 3.2 MJ/kg

## Application to Hygrothermal Design

### Moisture Storage Function

The sorption isotherm provides the moisture storage function ξ(φ), relating moisture content to relative humidity:

```
ξ(φ) = dw/dφ
```

This derivative represents the slope of the sorption isotherm and appears in the moisture diffusion equation:

```
ξ(φ) × ∂φ/∂t = ∇·[D_φ(φ) × ∇φ]
```

Where D_φ is the moisture diffusivity.

Materials with steep isotherms (high ξ) provide strong moisture buffering, moderating interior humidity fluctuations.

### Moisture Buffering Capacity

**Practical Moisture Buffer Value (MBV)**:

```
MBV = Δm / (A × Δφ)  [kg/(m²·%RH)]
```

Where:
- Δm = mass change in 8-hour exposure
- A = exposed surface area
- Δφ = RH change (typically 33% to 75%)

Classification:
- Negligible: MBV < 0.2 kg/(m²·%RH)
- Limited: 0.2 < MBV < 0.5
- Moderate: 0.5 < MBV < 1.0
- Good: 1.0 < MBV < 2.0
- Excellent: MBV > 2.0

Materials with steep sorption isotherms at typical indoor RH ranges (40-60%) provide superior buffering.

### Critical Moisture Content Determination

From sorption isotherms, identify critical moisture levels:

**Mold Growth Risk**: RH > 80% sustained
- Determine corresponding moisture content from isotherm
- Set as upper limit for envelope design

**Freeze-Thaw Damage**: Critical degree of saturation S_crit ≈ 0.85-0.91
- Calculate moisture content at various RH levels
- Ensure design prevents exceeding S_crit in freeze conditions

**Corrosion Risk**: For metals, critical RH ≈ 60-80% depending on contamination
- Evaluate hygroscopic salts effect on adjacent materials

### Drying Potential Assessment

Steep desorption isotherms indicate favorable drying potential. The slope at relevant RH determines how effectively reduced RH extracts moisture.

**Drying Efficiency Factor**:

```
η_dry = (w₈₀ - w₅₀) / (w₈₀ - w₃₀)
```

Higher values indicate better drying in the typical range (80% → 50% RH).

## Modeling and Curve Fitting

### Empirical Models

Several mathematical models fit sorption isotherm data for use in hygrothermal simulations.

#### Modified Oswin Equation

```
w = A × [RH / (1 - RH)]^B
```

Parameters A and B fitted to experimental data. Provides good fit for wood and cellulosic materials.

#### Henderson Equation

```
w = [-ln(1 - RH) / (A × T)]^(1/B)
```

Includes temperature dependence. Widely used for agricultural products and can apply to wood fiber materials.

#### Halsey Equation

```
w = [A / ln(1/RH)]^(1/B)
```

Suitable for Type II isotherms, particularly multilayer adsorption region.

#### Generalized Model (Hailwood-Horrobin)

For wood and cellulosic materials:

```
w = (1800/M) × [(KH + 2K₁KH²) / (1 - KH + K₁KH²)]
```

Where:
- M = molecular weight of sorption sites
- H = RH/100
- K, K₁ = equilibrium constants

This model distinguishes between dissolved water and hydrated water molecules.

### Fitting Procedures

**Least Squares Optimization**:

Minimize sum of squared residuals:

```
SSR = Σ[w_measured,i - w_model,i]²
```

Use nonlinear regression (Levenberg-Marquardt or similar algorithms) to determine parameters.

**Goodness of Fit Metrics**:

**Coefficient of Determination (R²)**:
```
R² = 1 - (SS_residual / SS_total)
```
Target: R² > 0.98 for acceptable fit

**Root Mean Square Error (RMSE)**:
```
RMSE = √[Σ(w_measured - w_model)² / n]
```

Lower RMSE indicates better fit. Express relative to maximum moisture content for normalization.

## Design Considerations

### Material Selection

**High Moisture Buffering Applications**:
- Select Type II isotherms with steep slopes at 40-60% RH
- Wood, gypsum, cellulose insulation provide excellent buffering
- Interior finishes: clay plaster, lime plaster, wood paneling

**Low Moisture Sensitivity Applications**:
- Exterior cladding: prefer low hygroscopicity (Type III behavior)
- Minimize dimensional changes and weathering degradation
- Synthetic materials, treated wood, dense ceramics

**Vapor Control Layer Placement**:
- Position considering sorption capacity of adjacent layers
- High storage capacity materials can tolerate temporary elevated moisture
- Low storage capacity requires strict vapor control

### Hygrothermal Simulation Inputs

Accurate simulations require:

1. **Full isotherm data**: 5-95% RH minimum, preferably 10% increments
2. **Hysteresis characterization**: Main adsorption and desorption curves
3. **Temperature dependence**: Isotherms at multiple temperatures or correction factors
4. **Moisture-dependent properties**: Thermal conductivity, vapor permeability as f(w)

### Quality Control

**Material Variability**:
- Natural materials show 10-30% variation in sorption behavior
- Specify testing for critical applications
- Use conservative values in design (upper bound for moisture uptake)

**Aging Effects**:
- Some materials show changed sorption after weathering
- Carbonation of concrete reduces sorption capacity
- Chemical degradation can increase hygroscopicity

## ASHRAE and Code References

**ASHRAE Handbook—Fundamentals (2021)**:
- Chapter 26: Heat, Air, and Moisture Control in Building Assemblies
- Section on moisture sorption isotherms and measurement methods
- Material property tables including sorption data

**ASHRAE Standard 160**: Criteria for Moisture-Control Design Analysis in Buildings
- Requires consideration of material moisture storage for mold risk assessment
- Specifies critical surface RH of 80% at material surface

**ASHRAE Standard 55**: Thermal Environmental Conditions for Human Occupancy
- Indoor humidity recommendations affect material moisture cycling
- Typical range 30-60% RH influences material selection

**International Energy Conservation Code (IECC)**:
- Vapor retarder requirements based on climate zone
- Must consider hygroscopic properties of assemblies

**ICC International Building Code (IBC)**:
- Weather-resistant barriers must account for moisture storage
- Drainage and drying provisions

## Advanced Topics

### Multi-Component Isotherms

Materials containing multiple constituents (e.g., wood with extractives, concrete with salts) exhibit modified sorption:

```
w_total = Σ[f_i × w_i(RH)]
```

Where f_i is the mass fraction of component i.

Hygroscopic salts dramatically increase moisture uptake at specific RH levels (deliquescence points).

### Non-Isothermal Sorption

Under combined temperature and humidity gradients, coupled phenomena occur:

**Soret Effect**: Temperature gradient drives moisture flux:
```
J_moisture = -D_T × ∇T - D_RH × ∇RH
```

Important in building envelopes with large temperature differences.

### Dynamic Sorption Effects

Real hygrothermal conditions involve time-dependent RH changes. Moisture uptake/release kinetics become important:

**Penetration Depth Concept**:
```
d_p = √(D_w × t)
```

Where:
- D_w = moisture diffusivity
- t = exposure time

For daily cycles (t = 12 hours), typical penetration depths:
- Wood: 5-15 mm
- Concrete: 10-30 mm
- Gypsum: 8-20 mm

Surface layers dominate short-term buffering; full thickness affects seasonal moisture management.

### Pore Size Distribution Analysis

Combining sorption isotherms with Kelvin equation yields pore size distribution:

```
dV/d(log r) = -d(V_ads)/d(log RH) × d(log RH)/d(log r)
```

This characterization helps predict:
- Frost damage susceptibility
- Salt crystallization pressure
- Water entry function for capillary absorption

## Practical Implementation

### Measurement Protocol for Projects

For critical applications requiring material-specific data:

1. **Sample Collection**: Obtain representative samples from actual project materials
2. **Conditioning**: Dry at 60-80°C (not 105°C for polymers) until constant mass
3. **Testing**: Minimum RH levels—10%, 30%, 50%, 65%, 80%, 90%, 95%
4. **Equilibration**: Allow 2-4 weeks per RH level, monitor mass weekly
5. **Hysteresis**: Measure both adsorption (dry → wet) and desorption (wet → dry)
6. **Replication**: Test 3-5 samples, report mean and standard deviation

### Database Resources

**ASHRAE**: Material property tables with selected sorption data
**WUFI Database**: Extensive sorption isotherms for North American and European materials
**masea Database**: European building materials focus
**Fraunhofer IBP**: Research data on advanced materials

### Software Implementation

Hygrothermal simulation programs (WUFI, DELPHIN, hygIRC) require isotherm input as:
- Tabulated data points (RH, moisture content pairs)
- Mathematical function parameters
- Temperature-dependent coefficients

Ensure units consistency: volumetric (kg/m³) vs. mass basis (kg/kg).

## Summary

Sorption isotherms quantify the fundamental hygroscopic behavior of building materials, providing essential data for moisture management design. Understanding isotherm classification, measurement methods, and application to hygrothermal analysis enables:

- Accurate prediction of moisture storage and release
- Selection of materials for moisture buffering or vapor control
- Assessment of condensation, mold growth, and material degradation risks
- Optimization of building envelope assemblies for durability and energy efficiency

The sorption isotherm transforms relative humidity—the driving potential—into moisture content—the physical quantity affecting thermal performance, dimensional stability, and biological susceptibility. This relationship forms the foundation for moisture control engineering in building systems.
