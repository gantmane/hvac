---
title: "Mold Growth Models"
description: "Mathematical models for predicting mold growth including VTT model, biohygrothermal isopleth systems, time-of-wetness criteria, ASHRAE 160 standards, and material-specific sensitivity classifications for building envelope design."
weight: 3
---

Mold growth prediction models provide quantitative tools for assessing moisture damage risk in building envelopes. These models translate hygrothermal analysis results into biological risk metrics, enabling engineers to evaluate design alternatives and establish performance thresholds for moisture control systems.

## VTT Mold Growth Model

The VTT (Technical Research Centre of Finland) model represents the most widely validated empirical approach for mold growth prediction on building materials. Developed by Viitanen and Ojanen, the model calculates a mold index (MI) ranging from 0 to 6 based on time-dependent exposure to temperature and relative humidity conditions.

### Model Structure

The VTT model employs differential equations that account for:

**Growth Phase:**
- Mold index increases when surface conditions exceed critical thresholds
- Growth rate depends on material sensitivity class, temperature, and RH
- Maximum growth rate occurs at optimal conditions (25-30°C, >95% RH)

**Decline Phase:**
- Mold index decreases during dry periods
- Decline rate is slower than growth rate (hysteresis effect)
- Complete reversal does not occur; residual spores remain viable

**Mathematical Formulation:**

When conditions favor growth:

```
dM/dt = (1/7) × (1/t_max) × k₁ × k₂
```

Where:
- M = Mold index (0-6 scale)
- t_max = Time to reach maximum mold index under optimal conditions
- k₁ = Intensity factor dependent on RH
- k₂ = Intensity factor dependent on temperature

When conditions inhibit growth:

```
dM/dt = -0.032 (for M > 1)
dM/dt = 0 (for M ≤ 1)
```

### Mold Index Scale

| Index | Visual Observation | Practical Significance |
|-------|-------------------|------------------------|
| 0 | No growth | Acceptable conditions |
| 1 | Initial spore germination (microscopic) | Risk threshold |
| 2 | Sparse growth (microscopic, <10% coverage) | Early detection possible |
| 3 | Visual growth (<10% coverage) | Visible damage begins |
| 4 | Visual coverage 10-50% | Clear deterioration |
| 5 | Visual coverage 50-100% | Extensive damage |
| 6 | Heavy, profuse growth | Complete colonization |

### Material Sensitivity Classes

The VTT model categorizes materials into four sensitivity classes based on their susceptibility to mold growth:

**Very Sensitive Materials (Class 1):**
- Untreated wood (pine sapwood)
- Porous insulation materials
- Nutrient-rich surfaces
- Critical RH threshold: 80%

**Sensitive Materials (Class 2):**
- Treated wood products
- Planed pine surfaces
- Concrete with biodegradable additives
- Critical RH threshold: 85%

**Medium Resistant Materials (Class 3):**
- Cement-based materials
- Plaster surfaces
- Painted wood
- Critical RH threshold: 90%

**Resistant Materials (Class 4):**
- Glass surfaces
- Glazed ceramic tiles
- PVC materials
- Critical RH threshold: 95%

## Isopleth Systems

Biohygrothermal isopleths represent graphical models that define boundary conditions for mold germination and growth. These diagrams plot temperature versus relative humidity, with curves indicating germination time and growth rates.

### Lowest Isopleth for Mold (LIM)

The LIM curve defines the minimum combined temperature-humidity conditions that permit initial spore germination. Conditions below this threshold prevent mold establishment regardless of exposure duration.

**Key LIM Characteristics:**
- Minimum RH decreases as temperature increases (within viable range)
- At 5°C: approximately 85-90% RH required
- At 20°C: approximately 80% RH required
- At 30°C: approximately 78-80% RH required

### Isopleth Applications

Isopleth systems serve multiple engineering functions:

1. **Design Verification:** Compare hygrothermal simulation results against critical isopleths
2. **Material Selection:** Identify materials whose resistance exceeds predicted exposure conditions
3. **Risk Duration Assessment:** Estimate time to visible growth under specific conditions
4. **Threshold Definition:** Establish control setpoints for active moisture management systems

## Time-of-Wetness Models

Time-of-wetness (TOW) approaches simplify mold risk assessment by tracking cumulative duration above critical moisture thresholds. These models assume binary conditions: growth-permitting or growth-inhibiting.

### Critical Moisture Thresholds

| Material Type | Critical RH | Critical MC | Temperature Range |
|---------------|-------------|-------------|-------------------|
| Wood products | 80% | 20% | 5-30°C |
| Gypsum board | 90% | 1% | 10-30°C |
| Concrete | 95% | 5% | 15-30°C |
| Insulation (organic) | 85% | 15% | 5-30°C |
| Painted surfaces | 90% | N/A | 10-30°C |

### Accumulation Criteria

TOW models typically employ one of three accumulation methods:

**Simple Accumulation:**
- Count hours above critical RH threshold
- Common criterion: <500 hours/year at surface RH >80%
- Does not account for temperature variation

**Degree-Hour Method:**
- Weight hours by RH excess above threshold
- Formula: Σ(RH - RH_critical) × time
- Provides severity weighting

**Temperature-Adjusted TOW:**
- Apply multipliers based on temperature favorability
- Growth factor at 25°C = 1.0
- Growth factor at 10°C ≈ 0.3
- Growth factor at 5°C ≈ 0.1

## ASHRAE Standard 160

ASHRAE 160 (Criteria for Moisture-Control Design Analysis in Buildings) establishes quantitative performance criteria for preventing mold growth in building assemblies.

### 30-Day Running Average Method

ASHRAE 160 employs a 30-day moving average of surface RH and temperature to assess mold growth risk. This approach filters short-term fluctuations while capturing sustained moisture exposure.

**Acceptance Criteria:**

| Surface Type | Maximum 30-Day Avg RH | Temperature Condition |
|--------------|----------------------|---------------------|
| Sensitive materials | 80% | All temperatures |
| Intermediate materials | 85% | T > 5°C |
| Resistant materials | 90% | T > 10°C |

### Implementation Requirements

**Simulation Parameters:**
- Minimum 3-year hourly simulation required
- Use typical meteorological year (TMY) climate data
- Include solar radiation and wind-driven rain
- Model actual construction sequence and drying periods

**Evaluation Locations:**
- All material interfaces subject to condensation risk
- Exterior sheathing surfaces
- Interior vapor retarder surfaces
- Roof deck assemblies
- Foundation walls and slabs

**Pass/Fail Criteria:**
- No 30-day period shall exceed material-specific RH thresholds
- Initial construction moisture must dry below criteria within first year
- Analysis must demonstrate compliance for worst-case orientation

## ESP-r Mold Prediction Module

The ESP-r building simulation platform incorporates a deterministic mold growth model based on substrate-specific germination and growth rate functions.

**Model Features:**
- Hourly calculation of germination potential
- Species-specific parameters (Aspergillus, Penicillium, Stachybotrys)
- Integration with hygrothermal solver
- Surface and interstitial prediction capability

**Critical Parameters:**
- Minimum germination time: 24-72 hours at optimal conditions
- Decay rate during dry periods: 50% reduction per 30 days
- Temperature optimum: 25-28°C for most species
- Substrate adjustment factors for nutrient availability

## Material-Specific Growth Characteristics

Different building materials exhibit distinct mold growth behaviors due to variations in nutrient content, pH, surface texture, and moisture retention.

### Wood and Wood-Based Products

**Growth Factors:**
- Fiber saturation point: ~28% moisture content
- Surface mold initiation: 20-22% MC
- Deep colonization: >25% MC sustained
- Species variation: sapwood > heartwood susceptibility

**Critical Conditions:**
- Germination threshold: 80% RH at 20°C for 5-7 days
- Visible growth: 85% RH at 20°C for 30 days
- Temperature acceleration: growth rate doubles per 10°C rise (5-30°C range)

### Gypsum-Based Materials

**Growth Factors:**
- Paper facing provides primary nutrient source
- Core remains relatively resistant
- Capillary moisture transport from adjacent materials
- Alkalinity inhibits growth initially

**Critical Conditions:**
- Surface RH threshold: 90% at 25°C
- Paper backing saturation: critical risk point
- Repeated wetting cycles: cumulative damage
- Contact with wet materials: direct moisture transfer

### Concrete and Masonry

**Growth Factors:**
- High initial pH (12-13) inhibits growth
- Carbonation reduces alkalinity over time
- Surface dust and efflorescence provide nutrients
- Porous structure retains moisture

**Critical Conditions:**
- New concrete: minimal risk for 6-12 months
- Aged concrete: 95% RH threshold at 20°C
- Surface condensation: primary initiation mechanism
- Thermal bridging locations: elevated risk zones

## Model Validation and Uncertainty

Mold growth models carry inherent uncertainties due to biological variability and environmental complexity.

### Validation Studies

**Laboratory Validation:**
- Controlled exposure chambers with inoculated specimens
- Measured agreement: ±0.5 mold index units
- Temperature range: 5-30°C
- RH range: 75-100%

**Field Validation:**
- Limited full-scale validation data available
- Correlation with observed damage: moderate to good
- Under-prediction common in optimal growth conditions
- Over-prediction in borderline conditions

### Uncertainty Sources

1. **Material Variability:** Substrate composition, surface condition, contamination
2. **Biological Variation:** Species diversity, spore availability, adaptation
3. **Microclimate Effects:** Air film resistance, local convection, radiation
4. **Model Simplifications:** Nutrient depletion, competition, succession ignored

### Safety Factors

Conservative design practice applies safety margins:
- Reduce critical RH thresholds by 5% for design purposes
- Apply 1.5× factor to predicted TOW accumulation
- Consider worst-case material sensitivity classification
- Evaluate multiple climate years for inter-annual variability

## Integration with Hygrothermal Analysis

Mold growth models require accurate hygrothermal boundary conditions from coupled heat and moisture transport simulations.

### Required Inputs

**Environmental Conditions:**
- Hourly outdoor temperature and RH
- Solar radiation intensity and angle
- Wind speed and direction
- Precipitation (wind-driven rain)

**Material Properties:**
- Moisture storage functions
- Liquid and vapor transport coefficients
- Thermal conductivity (moisture-dependent)
- Initial moisture content

**Boundary Conditions:**
- Interior temperature and RH schedules
- Surface heat transfer coefficients
- Air leakage rates through assembly
- Solar absorptance and emittance

### Simulation Best Practices

1. **Mesh Refinement:** Fine spatial discretization at material interfaces (≤5 mm)
2. **Time Step:** Hourly maximum for mold prediction (1-15 min for hygrothermal core)
3. **Convergence:** Verify moisture balance closure (<1% error)
4. **Duration:** Minimum 3 years to capture inter-annual variability
5. **Post-Processing:** Apply moving averages to filter numerical noise

Accurate mold growth prediction enables evidence-based envelope design decisions, quantifies moisture safety margins, and establishes performance acceptance criteria for moisture control strategies. Engineers must select models appropriate to material systems, validate predictions against acceptance criteria, and apply conservative thresholds to account for model uncertainties and field variability.
