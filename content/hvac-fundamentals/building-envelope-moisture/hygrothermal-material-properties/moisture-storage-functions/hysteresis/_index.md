---
title: "Hysteresis"
description: "Moisture storage hysteresis phenomenon in building materials, including adsorption-desorption differences, scanning curves, and mathematical models for hygrothermal analysis"
weight: 3
---

## Physical Principles

Hysteresis in moisture storage describes the phenomenon where the equilibrium moisture content of a porous building material differs depending on whether the material is wetting (adsorption) or drying (desorption) at the same relative humidity. This path-dependent behavior fundamentally affects moisture transport calculations and building envelope performance predictions.

### Thermodynamic Basis

The hysteresis effect originates from several physical mechanisms operating at the pore scale:

**Capillary Condensation Asymmetry**

The Kelvin equation describes equilibrium vapor pressure over curved menisci, with different contact angles during wetting and drying:

$$r_k = \frac{-2\sigma V_m \cos\theta}{RT \ln(\phi)}$$

Where:
- r_k = Kelvin radius (m)
- σ = surface tension of water (0.0728 N/m at 20°C)
- V_m = molar volume of water (1.8 × 10⁻⁵ m³/mol)
- θ = contact angle (different for advancing and receding menisci)
- R = universal gas constant (8.314 J/(mol·K))
- T = absolute temperature (K)
- φ = relative humidity (decimal)

During adsorption, the advancing contact angle is larger, requiring higher relative humidity to fill a given pore compared to the receding contact angle during desorption. This creates the hysteresis loop.

**Ink-Bottle Effect**

Pores with narrow necks and wide bodies fill at the relative humidity corresponding to the neck diameter but empty at the relative humidity corresponding to the body diameter, creating irreversible behavior in the moisture retention curve.

**Contact Angle Hysteresis**

Surface roughness and chemical heterogeneity cause contact angle differences:

$$\theta_{advancing} - \theta_{receding} = \Delta\theta_{hysteresis}$$

Typical values for building materials range from 10° to 40°.

## Moisture Storage Curves

### Primary Curves

The two boundary curves define the hysteresis envelope:

**Adsorption Curve (Wetting)**

Material starting from dry state, exposed to increasing relative humidity:

$$u_{ads}(\phi) = u_{m} \frac{CK\phi}{(1-K\phi)(1-K\phi+CK\phi)}$$

Where:
- u_ads = adsorption moisture content (kg/m³)
- u_m = monolayer moisture content (kg/m³)
- C = energy constant (dimensionless)
- K = multilayer constant (dimensionless)
- φ = relative humidity (decimal)

**Desorption Curve (Drying)**

Material starting from saturated state, exposed to decreasing relative humidity:

$$u_{des}(\phi) = u_{ads}(\phi) + \Delta u_{hyst}(\phi)$$

Where Δu_hyst represents the hysteresis offset, typically 20-50% of the adsorption value at mid-range relative humidity (40-70% RH).

### Hysteresis Loop Characteristics

| Material Type | Loop Width (Δu at 50% RH) | Hysteresis Ratio | Significance |
|---------------|---------------------------|------------------|--------------|
| Dense concrete | 5-10 kg/m³ | 1.2-1.4 | Moderate |
| Cellular concrete | 15-30 kg/m³ | 1.4-1.8 | High |
| Brick (clay) | 8-15 kg/m³ | 1.3-1.5 | Moderate-High |
| Wood (softwood) | 10-20 kg/m³ | 1.5-2.0 | High |
| Wood (hardwood) | 8-16 kg/m³ | 1.4-1.8 | High |
| Mineral wool | 0.5-2 kg/m³ | 1.1-1.3 | Low |
| Calcium silicate | 12-25 kg/m³ | 1.4-1.7 | High |
| Gypsum board | 6-12 kg/m³ | 1.3-1.6 | Moderate-High |

*Hysteresis ratio = u_des/u_ads at 50% RH*

## Scanning Curves

### Mathematical Description

Scanning curves represent intermediate moisture history paths between the primary adsorption and desorption curves. These occur during cyclic humidity variations typical of real building conditions.

**Mualem Model for Scanning Curves**

$$u_{scan}(\phi) = u_{ads}(\phi) + \alpha[u_{des}(\phi_{rev}) - u_{ads}(\phi_{rev})]\left(\frac{\phi}{\phi_{rev}}\right)^{\beta}$$

Where:
- u_scan = moisture content on scanning curve (kg/m³)
- φ_rev = relative humidity at reversal point (decimal)
- α = shape parameter (0.5-0.9, typically 0.7)
- β = curvature parameter (1.5-3.0, typically 2.0)

**First-Order Hysteresis Model**

Simpler approach assuming scanning curves are linear interpolations:

$$u_{scan} = u_{ads} + f(u_{des} - u_{ads})$$

Where f is the scanning factor (0 ≤ f ≤ 1) depending on moisture history.

### Reversal Points

Each humidity reversal creates a new scanning curve. The material "remembers" its moisture history through the sequence of reversal points. For practical hygrothermal simulations, tracking more than 3-5 reversal points provides diminishing accuracy improvement.

## Practical Implications for HVAC Design

### Moisture Buffer Capacity

The area enclosed by the hysteresis loop represents additional moisture storage capacity available during cyclic humidity fluctuations:

$$MBC = \int_{\phi_1}^{\phi_2} [u_{des}(\phi) - u_{ads}(\phi)] d\phi$$

Where MBC is the moisture buffer capacity (kg/(m²·%RH)) for a material thickness L:

$$MBC = \rho L \int_{\phi_1}^{\phi_2} [u_{des}(\phi) - u_{ads}(\phi)] d\phi$$

**Practical Moisture Buffer Values**

| Material | Thickness (mm) | MBC (g/(m²·%RH)) | Buffering Class |
|----------|----------------|------------------|-----------------|
| Gypsum board | 12.5 | 0.9-1.2 | Moderate |
| Wood paneling (pine) | 19 | 1.5-2.1 | Good |
| Clay plaster | 15 | 2.0-2.8 | Excellent |
| Concrete (exposed) | 100 | 0.8-1.1 | Moderate |
| Cellulose insulation | 150 | 1.2-1.8 | Good |

Classification per Rode et al. (2005):
- Negligible: MBC < 0.2 g/(m²·%RH)
- Limited: 0.2-0.5
- Moderate: 0.5-1.0
- Good: 1.0-2.0
- Excellent: > 2.0

### Latent Load Calculations

Ignoring hysteresis leads to systematic errors in latent cooling load calculations for spaces with significant hygroscopic surface area. The error magnitude:

$$Error_{latent} = h_{fg} \cdot SA \cdot \rho_{mat} \cdot \Delta u_{hyst} \cdot \frac{1}{\Delta t}$$

Where:
- h_fg = latent heat of vaporization (2,450 kJ/kg at 20°C)
- SA = hygroscopic surface area (m²)
- ρ_mat = material density (kg/m³)
- Δu_hyst = hysteresis offset (kg/kg)
- Δt = time period for humidity cycle (s)

For typical interior spaces with 200 m² of gypsum board surface:

$$Error_{latent} \approx 50-150 \text{ W during humidity transients}$$

This represents 5-15% of typical dehumidification loads in humid climates.

## Engineering Models

### Empirical Hysteresis Functions

**Mualem-van Genuchten Model**

Extended for hysteresis with independent parameters for wetting and drying:

$$u(\phi) = u_{res} + \frac{u_{sat} - u_{res}}{[1 + (\alpha\phi)^n]^m}$$

Parameters differ for adsorption (α_ads, n_ads, m_ads) and desorption (α_des, n_des, m_des).

Typical parameter ranges:

| Parameter | Adsorption Range | Desorption Range | Units |
|-----------|------------------|------------------|-------|
| α | 0.5-2.0 | 1.0-4.0 | - |
| n | 1.2-2.5 | 1.5-3.5 | - |
| m | 0.3-0.7 | 0.4-0.8 | - |
| u_res | 0.01-0.05 | 0.02-0.08 | m³/m³ |

### ASHRAE References

**ASHRAE Handbook—Fundamentals (2021), Chapter 25**: Provides moisture sorption isotherms for common building materials but notes that hysteresis effects may introduce 20-40% uncertainty in transient moisture calculations.

**ASHRAE 160-2016**: Standard for moisture control design requires consideration of hysteresis when modeling assemblies exposed to cyclic humidity conditions, particularly for:
- Hygroscopic insulation materials
- Interior finish materials with high moisture storage
- Assemblies with vapor-open designs

**ASHRAE Research Project RP-1325**: Documented hysteresis parameters for 47 building materials, establishing that neglecting hysteresis in dynamic simulations can underpredict peak moisture contents by 15-35%.

## Measurement and Characterization

### Laboratory Determination

**Dynamic Vapor Sorption (DVS)**

Automated gravimetric method measuring mass change during controlled RH steps:

1. Dry sample to constant mass at 0% RH
2. Step RH from 0% to 95% in 5-10% increments (adsorption)
3. Step RH from 95% to 0% in 5-10% decrements (desorption)
4. Equilibrium criterion: dm/dt < 0.002%/min

Typical test duration: 3-7 days for complete hysteresis loop.

**Desiccator Method (ASTM C1498)**

Salt solution method for discrete RH points:

| Salt Solution | Equilibrium RH (23°C) | Tolerance |
|---------------|----------------------|-----------|
| LiCl | 11.3% | ±0.3% |
| MgCl₂ | 33.1% | ±0.2% |
| Mg(NO₃)₂ | 54.4% | ±0.5% |
| NaCl | 75.5% | ±0.1% |
| KCl | 85.1% | ±0.3% |
| K₂SO₄ | 97.6% | ±0.5% |

Requires 4-8 weeks for complete hysteresis characterization with sufficient data points.

### In-Situ Monitoring

Field measurements reveal actual hysteresis behavior under service conditions:

**RH/Moisture Content Sensor Pairs**

Install embedded RH sensors and capacitance moisture content sensors at identical depths to track u-φ relationship during seasonal cycles. Plots reveal hysteresis loops under real boundary conditions.

**Data Analysis**

Extract hysteresis parameters by fitting measured loops to Mualem or van Genuchten models using nonlinear regression. Typical field loops are narrower than laboratory loops due to incomplete moisture penetration during short-duration RH fluctuations.

## Design Considerations

### Hygrothermal Simulation

**Software Implementation**

Leading hygrothermal analysis tools (WUFI, DELPHIN, MOISTURE-EXPERT) employ different hysteresis approaches:

- **Full hysteresis tracking**: Maintains complete reversal point history, computationally intensive
- **Simplified scanning curves**: Linear interpolation between primary curves, 90% accuracy with 10% computational cost
- **Hysteresis neglect**: Uses single curve (typically desorption), introduces systematic conservatism

**Recommended Approach**

For HVAC system design affecting moisture-sensitive assemblies:

1. Use full hysteresis model for assemblies with:
   - Hygroscopic insulation (cellulose, wood fiber)
   - Vapor-open exterior finishes
   - Interior moisture buffering layers

2. Use simplified model for:
   - Standard cavity insulation with vapor barriers
   - Non-hygroscopic materials (XPS, polyiso)
   - Assemblies with steady-state moisture conditions

3. Neglect hysteresis only for:
   - Preliminary screening calculations
   - Non-critical assemblies
   - Conservative estimates (use desorption curve)

### Material Selection Criteria

**High Hysteresis Materials (Δu > 15 kg/m³ at 50% RH)**

Advantages:
- Superior moisture buffering capacity
- Reduced peak RH during moisture events
- Enhanced occupant comfort through RH stabilization

Disadvantages:
- Slower drying rates during desorption
- Prolonged elevated moisture content
- Increased mold risk if assembly cannot dry

Appropriate applications: Interior finishes in occupied spaces, moisture buffering layers in balanced assemblies

**Low Hysteresis Materials (Δu < 5 kg/m³ at 50% RH)**

Advantages:
- Predictable moisture behavior
- Rapid response to drying conditions
- Simplified modeling with single isotherm

Disadvantages:
- Minimal moisture buffering
- RH fluctuations track ambient conditions
- Limited passive humidity control

Appropriate applications: Vapor control layers, moisture-sensitive assemblies requiring rapid drying, exterior air barrier materials

### Climate-Specific Recommendations

**Hot-Humid Climates (ASHRAE Climate Zones 1-2)**

Hysteresis effects amplify during cooling season when:
- Exterior materials cycle between high nighttime RH and solar-driven drying
- Interior materials buffer air conditioning dehumidification cycles

Critical design factor: Ensure desorption pathway exists for materials that adsorb moisture during high-RH periods.

**Cold Climates (ASHRAE Climate Zones 6-8)**

Hysteresis influences winter moisture accumulation:
- Materials on warm side adsorb moisture from interior sources
- Slow desorption rates during heating season
- Spring drying must overcome accumulated moisture

Critical design factor: Size heating/ventilation to account for moisture release from interior materials during shoulder seasons.

**Mixed Climates (ASHRAE Climate Zones 3-5)**

Seasonal reversal of vapor drive creates complex hysteresis patterns:
- Summer: inward vapor drive, adsorption in exterior sheathing
- Winter: outward vapor drive, desorption from interior materials

Critical design factor: Use materials with moderate hysteresis and ensure bidirectional drying capacity.

## Advanced Topics

### Temperature Dependence of Hysteresis

The hysteresis loop width varies with temperature according to:

$$\Delta u_{hyst}(T) = \Delta u_{hyst}(T_0) \cdot \exp\left[\frac{E_a}{R}\left(\frac{1}{T_0} - \frac{1}{T}\right)\right]$$

Where:
- E_a = activation energy for hysteresis (typically 15-25 kJ/mol)
- T_0 = reference temperature (293 K)
- R = universal gas constant (8.314 J/(mol·K))

Effect: Hysteresis loop narrows at elevated temperatures, widening the uncertainty in moisture predictions for assemblies with temperature gradients.

### Cyclic Steady-State

Under repeating diurnal or seasonal cycles, materials approach a "cyclic steady-state" where the moisture content traces the same scanning curve loop each cycle:

$$\oint u(t) dt = 0 \text{ (over one complete cycle)}$$

This equilibrium scanning loop may occur between the primary curves, representing a practical operating condition distinct from laboratory-measured boundary curves.

**HVAC Implications**

Design calculations should target cyclic steady-state conditions rather than primary curve extremes. This typically results in:
- 10-20% lower peak moisture content predictions
- More accurate latent load estimates
- Realistic material stress/degradation assessments

### Coupling with Salt Transport

In masonry and concrete, dissolved salt concentration affects hysteresis behavior:

$$u_{total} = u_{capillary} + u_{osmotic}$$

Where osmotic moisture storage (from salt solutions) exhibits different hysteresis characteristics than pure water storage. Relevant for:
- Coastal buildings exposed to airborne chlorides
- Concrete containing deicing salt contaminants
- Masonry with efflorescence issues

## References and Standards

**ASTM Standards**
- ASTM C1498: Standard Test Method for Hygroscopic Sorption Isotherms of Building Materials
- ASTM E96: Standard Test Methods for Water Vapor Transmission of Materials

**ISO Standards**
- ISO 12571: Hygrothermal performance of building materials—Determination of hygroscopic sorption properties
- ISO 15148: Hygrothermal performance of building materials—Determination of water absorption coefficient

**Key Research Literature**
- Mualem, Y. (1974): "Modified approach to capillary hysteresis based on similarity hypothesis"
- Pedersen, C.R. (1990): "Combined heat and moisture transfer in building constructions" (PhD thesis establishing practical hysteresis models)
- Rode, C. et al. (2005): "Moisture buffering of building materials" (BYG·DTU report establishing classification system)

**Software Documentation**
- WUFI Pro 6.0 Manual: Sections on hysteresis implementation and scanning curve algorithms
- ASHRAE RP-1325 Final Report: Comprehensive hysteresis data for 47 building materials

## Components

The following subsections provide detailed analysis of specific hysteresis mechanisms:

- **Adsorption Vs Desorption**: Physical differences in wetting and drying processes
- **Hysteresis Loop**: Geometric characteristics and parametric description
- **Scanning Curves**: Mathematical models for intermediate moisture history paths
- **Primary Curves**: Boundary isotherms defining the hysteresis envelope
