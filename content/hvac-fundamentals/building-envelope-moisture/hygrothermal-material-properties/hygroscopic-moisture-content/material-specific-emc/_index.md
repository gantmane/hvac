---
title: "Material-Specific Equilibrium Moisture Content"
description: "Comprehensive analysis of equilibrium moisture content characteristics for building materials including wood, masonry, insulation, and hygroscopic materials with sorption isotherms, fiber saturation points, and moisture storage functions"
weight: 2
---

## Overview

Material-specific equilibrium moisture content (EMC) represents the moisture content that each building material achieves when in equilibrium with surrounding air at specific temperature and relative humidity conditions. Understanding EMC characteristics for different materials is essential for predicting moisture storage, calculating buffering capacity, preventing material degradation, and designing building envelopes that manage hygrothermal loads effectively.

The EMC relationship is fundamentally governed by sorption isotherms, which describe the nonlinear relationship between relative humidity and moisture content at constant temperature. Each material exhibits unique sorption behavior based on its pore structure, chemical composition, and surface characteristics.

## Fundamental Sorption Physics

### Moisture Sorption Mechanisms

Building materials absorb moisture through three primary mechanisms:

**Monomolecular Adsorption (0-20% RH):**
Water molecules form a single layer on material surfaces through van der Waals forces and hydrogen bonding. This process follows the Langmuir adsorption model:

u₁ = (u_m × b × φ) / (1 + b × φ)

Where:
- u₁ = moisture content from monomolecular adsorption (kg/kg)
- u_m = monolayer moisture content (kg/kg)
- b = adsorption energy constant (-)
- φ = relative humidity (decimal)

**Multimolecular Adsorption (20-90% RH):**
Additional water layers build on the initial monolayer. The BET (Brunauer-Emmett-Teller) model describes this region:

u = (u_m × C × φ) / [(1 - φ) × (1 + (C - 1) × φ)]

Where:
- C = BET constant related to heat of adsorption (-)
- Other terms as previously defined

**Capillary Condensation (>90% RH):**
Water condenses in material pores when the vapor pressure exceeds the Kelvin equation threshold:

ln(φ) = (2 × σ × V_m × cos(θ)) / (R × T × r_c)

Where:
- σ = surface tension of water (0.0728 N/m at 20°C)
- V_m = molar volume of water (1.8×10⁻⁵ m³/mol)
- θ = contact angle (radians)
- R = universal gas constant (8.314 J/mol·K)
- T = absolute temperature (K)
- r_c = critical pore radius (m)

### Hysteresis Effects

The moisture content during adsorption (wetting) differs from desorption (drying) at the same relative humidity, creating hysteresis loops. The magnitude of hysteresis depends on pore structure and typically ranges from 1-5% moisture content for most building materials.

**Hysteresis ratio:**

HR = (u_des - u_ads) / u_des × 100%

Where:
- HR = hysteresis ratio (%)
- u_des = moisture content during desorption (kg/kg)
- u_ads = moisture content during adsorption (kg/kg)

## Wood Equilibrium Moisture Content

### Wood EMC Fundamentals

Wood is the most hygroscopic structural material in buildings, with EMC varying significantly with species, temperature, and relative humidity. The practical hygroscopic range extends from oven-dry conditions to the fiber saturation point.

**Simpson's equation for wood EMC (USDA Forest Products Laboratory):**

EMC = (1800/W) × [(K₁ × K₂ × φ)/(1 - K₁ × φ) + (K₃ × K₄ × φ)/(1 + K₃ × K₄ × φ)]

Where:
- EMC = equilibrium moisture content (%)
- W = 330 + 0.452 × T + 0.00415 × T²
- K₁ = 0.805 + 0.000736 × T - 0.00000273 × T²
- K₂ = 6.27 - 0.00938 × T - 0.000303 × T²
- K₃ = 1.91 + 0.0407 × T - 0.000293 × T²
- K₄ = 18.3 + 0.908 × T - 0.0106 × T²
- T = temperature (°C)
- φ = relative humidity (decimal)

### Wood EMC Table by Species Groups

| Species Group | Density (kg/m³) | EMC at 30% RH | EMC at 50% RH | EMC at 70% RH | EMC at 90% RH |
|---------------|-----------------|---------------|---------------|---------------|---------------|
| Softwoods (Pine, Spruce, Fir) | 400-550 | 6.2% | 9.5% | 13.5% | 21.0% |
| Medium Hardwoods (Oak, Ash) | 550-750 | 6.0% | 9.1% | 13.0% | 20.0% |
| Dense Hardwoods (Maple, Birch) | 650-800 | 5.8% | 8.8% | 12.5% | 19.0% |
| Very Dense Woods (Hickory, Beech) | 750-900 | 5.5% | 8.4% | 12.0% | 18.0% |

Note: Values at 20°C (68°F)

### Fiber Saturation Point (FSP)

The fiber saturation point represents the moisture content at which cell walls are saturated with bound water but free water has not yet accumulated in cell cavities. FSP is critically important because:

- Wood dimensional changes occur only below FSP
- Mechanical properties remain relatively constant above FSP
- Biological degradation risk increases significantly above FSP

**Typical FSP values:**

FSP = 28% to 32% moisture content (dry basis)

**Temperature correction for FSP:**

FSP(T) = FSP(20°C) × [1 - 0.0015 × (T - 20)]

Where:
- FSP(T) = fiber saturation point at temperature T (%)
- T = temperature (°C)

### Wood Moisture Content Measurement

**Dry basis moisture content:**

MC_dry = (m_wet - m_dry) / m_dry × 100%

**Wet basis moisture content:**

MC_wet = (m_wet - m_dry) / m_wet × 100%

Where:
- m_wet = mass of wet specimen (kg)
- m_dry = oven-dry mass (kg)

Conversion between bases:

MC_wet = MC_dry / (1 + MC_dry/100)

### Wood EMC Applications in HVAC Design

**Indoor climate control targets:**

- Furniture and millwork: Maintain 40-55% RH for 8-10% EMC
- Structural framing: Allow 8-14% EMC range
- Wood flooring: Control to 6-9% EMC (35-50% RH)
- Musical instruments: Strict 45-55% RH for 8.5-10% EMC

**Seasonal EMC variation control:**

Maximum allowable seasonal swing = ±2% EMC to prevent dimensional problems

Required RH control bandwidth:

ΔRH_max = (ΔEMC_max / (dEMC/dRH)) × 100%

At 50% RH and 20°C, dEMC/dRH ≈ 0.14%/%RH, so:

ΔRH_max = 2% / 0.14 ≈ 14% RH

This indicates that maintaining indoor RH within 40-55% limits seasonal wood movement to acceptable levels.

## Masonry Equilibrium Moisture Content

### Brick and Clay Products

Fired clay masonry exhibits relatively low hygroscopicity compared to wood, but moisture storage capacity significantly affects wall assembly performance.

**Brick EMC characteristics:**

| Brick Type | Bulk Density (kg/m³) | Porosity (%) | EMC at 50% RH | EMC at 80% RH | EMC at 95% RH |
|------------|---------------------|--------------|---------------|---------------|---------------|
| High-fired face brick | 2000-2200 | 8-12 | 0.5% | 1.2% | 2.8% |
| Medium-fired common brick | 1800-2000 | 15-22 | 1.0% | 2.5% | 6.0% |
| Low-fired brick | 1600-1800 | 22-30 | 1.8% | 4.5% | 10.5% |
| Clay tile | 1400-1700 | 25-35 | 2.2% | 5.5% | 12.0% |

**Sorption isotherm equation for brick (Modified GAB model):**

u = (u_m × C × k × φ) / [(1 - k × φ) × (1 + (C - 1) × k × φ)]

Where:
- u_m = 0.008 to 0.025 kg/kg (depending on firing temperature)
- C = 5 to 15 (-)
- k = 0.85 to 0.95 (-)

### Concrete and Cement Products

Concrete moisture content depends on cement content, water-cement ratio, age, and curing conditions.

**Concrete EMC values:**

| Concrete Type | w/c Ratio | EMC at 50% RH | EMC at 75% RH | EMC at 95% RH |
|---------------|-----------|---------------|---------------|---------------|
| High strength | 0.30 | 1.8% | 3.2% | 5.5% |
| Normal strength | 0.45 | 2.5% | 4.0% | 6.5% |
| Lightweight | 0.50 | 3.5% | 5.5% | 9.0% |
| Autoclaved aerated | 0.60 | 5.0% | 8.0% | 15.0% |

**Concrete moisture diffusivity:**

The moisture diffusivity of concrete varies exponentially with moisture content:

D_w(u) = D_0 × exp(n × u/u_sat)

Where:
- D_w = moisture diffusivity (m²/s)
- D_0 = reference diffusivity ≈ 1×10⁻¹² m²/s
- n = exponent (6-10 for concrete)
- u_sat = saturation moisture content (kg/kg)

### Mortar and Grout

Mortar exhibits higher hygroscopicity than brick, creating moisture distribution gradients in masonry assemblies.

**Mortar EMC by type:**

- Type N (1:1:6 cement:lime:sand): 4.0% at 75% RH
- Type S (1:0.5:4.5): 3.2% at 75% RH
- Type M (1:0.25:3.5): 2.8% at 75% RH

## Insulation Material EMC

### Fibrous Insulation

**Fiberglass:**
- Essentially non-hygroscopic: <0.1% EMC across full RH range
- No moisture storage capacity
- Performance degradation only from liquid water accumulation

**Mineral wool:**
- Slightly hygroscopic: 0.2% at 50% RH, 0.8% at 90% RH
- Hydrophobic treatment reduces moisture uptake further
- Moisture storage: 0.5-2 kg/m³ at 80% RH

**Cellulose (treated):**

Cellulose insulation exhibits significant hygroscopicity despite fire retardant treatments.

| Treatment Type | EMC at 50% RH | EMC at 75% RH | EMC at 90% RH | Buffering Capacity |
|----------------|---------------|---------------|---------------|-------------------|
| Borate-treated | 11.0% | 16.5% | 24.0% | High |
| Sulfate-treated | 12.5% | 18.0% | 26.0% | Very high |

**Cellulose sorption equation:**

EMC_cellulose = A × φ + B × φ² + C × φ³

Where (at 20°C):
- A = 15.2
- B = 8.7
- C = 5.1
- φ = relative humidity (decimal)

### Foam Insulation

**Closed-cell spray foam:**
- Negligible hygroscopicity: <0.3% across full RH range
- Acts as vapor retarder
- No significant moisture storage

**Extruded polystyrene (XPS):**
- EMC ≈ 0.5% at 75% RH
- Low moisture diffusivity: 2×10⁻¹² m²/s

**Expanded polystyrene (EPS):**
- EMC ≈ 1.5-3.0% at 75% RH (depending on density)
- Higher moisture uptake than XPS due to interconnected pores

**Polyisocyanurate:**
- Facers dominate moisture behavior
- Foam core: <0.5% EMC at 75% RH

## Gypsum Board EMC

Gypsum wallboard is moderately hygroscopic and provides significant moisture buffering.

**Standard gypsum board EMC:**

| Relative Humidity | EMC (%) | Moisture Storage (kg/m²) |
|-------------------|---------|--------------------------|
| 30% | 0.5% | 0.040 |
| 50% | 1.0% | 0.080 |
| 70% | 2.2% | 0.176 |
| 90% | 5.5% | 0.440 |

Assumptions: 12.7 mm (1/2") board, density 650 kg/m³

**Nordtest sorption equation for gypsum:**

u = 0.0138 × φ - 0.00564 × φ² + 0.0614 × φ³

Where:
- u = moisture content (kg/kg)
- φ = relative humidity (decimal)

**Moisture buffering value (MBV) for gypsum board:**

MBV = 1.0 to 1.4 g/(m²·%RH) for 8-hour cycles

This makes gypsum board an effective passive humidity buffer in conditioned spaces.

## Hygroscopic Salts and Deliquescence

### Critical Relative Humidity

Hygroscopic salts present in building materials can absorb moisture at specific relative humidity thresholds, causing material degradation.

**Deliquescence RH for common salts:**

| Salt | Chemical Formula | Deliquescence RH (20°C) |
|------|-----------------|-------------------------|
| Calcium chloride | CaCl₂ | 32% |
| Magnesium chloride | MgCl₂ | 33% |
| Sodium chloride | NaCl | 75% |
| Potassium nitrate | KNO₃ | 93% |
| Sodium sulfate | Na₂SO₄ | 93% |
| Sodium carbonate | Na₂CO₃ | 87% |

When RH exceeds the deliquescence point, salts dissolve and create saturated solutions, dramatically increasing local moisture content.

**Salt-contaminated material EMC:**

For materials containing soluble salts:

u_total = u_matrix + u_salt

Where:
- u_matrix = base material EMC (kg/kg)
- u_salt = additional moisture from salt deliquescence (kg/kg)

u_salt can exceed 10-20% when RH > deliquescence RH.

## Moisture Storage Functions

### Differential Moisture Capacity

The moisture storage function describes how much moisture is stored per unit change in relative humidity:

ξ = du/dφ

Where:
- ξ = moisture capacity (kg/kg per unit RH)
- u = moisture content (kg/kg)
- φ = relative humidity (decimal)

**Moisture capacity by material:**

| Material | ξ at 50% RH (kg/kg) | ξ at 80% RH (kg/kg) |
|----------|---------------------|---------------------|
| Wood (softwood) | 0.16 | 0.35 |
| Gypsum board | 0.012 | 0.055 |
| Brick (common) | 0.030 | 0.085 |
| Concrete | 0.025 | 0.070 |
| Cellulose insulation | 0.18 | 0.42 |

### Volumetric Moisture Storage

For hygrothermal modeling, volumetric moisture capacity is required:

ξ_v = ρ_0 × ξ = ρ_0 × du/dφ

Where:
- ξ_v = volumetric moisture capacity (kg/m³ per unit RH)
- ρ_0 = dry material density (kg/m³)

**Example calculation for wood framing:**

Given:
- Spruce framing: ρ_0 = 450 kg/m³
- At 50% RH: ξ = 0.16 kg/kg

ξ_v = 450 × 0.16 = 72 kg/m³

This means a 1% RH increase stores an additional 0.72 kg/m³ of moisture.

## Temperature Effects on EMC

### Temperature Dependency

EMC decreases with increasing temperature at constant relative humidity due to reduced adsorption energy and increased molecular kinetic energy.

**Temperature correction factor:**

EMC(T₂) = EMC(T₁) × [1 - α × (T₂ - T₁)]

Where:
- α = temperature coefficient (typically 0.01 to 0.02 per °C)
- T₁, T₂ = temperatures (°C)

**Wood EMC temperature effect:**

At 80% RH:
- 10°C: EMC = 16.5%
- 20°C: EMC = 15.0%
- 30°C: EMC = 13.5%
- 40°C: EMC = 12.2%

## ASHRAE and Code References

### Relevant Standards

**ASHRAE Standards:**
- ASHRAE 160: Criteria for Moisture-Control Design Analysis in Buildings
  - Provides EMC failure criteria for mold growth risk
  - References material moisture content thresholds

- ASHRAE Handbook—Fundamentals, Chapter 26: Heat, Air, and Moisture Control
  - Tables of sorption isotherms for common materials
  - Moisture storage function data

**ASTM Standards:**
- ASTM C1498: Standard Test Method for Hygroscopic Sorption Isotherms of Building Materials
- ASTM D4933: Standard Guide for Moisture Conditioning of Wood and Wood-Base Materials
- ASTM C1794: Standard Test Method for Determination of the Water Absorption Coefficient by Partial Immersion

### Material Moisture Limits

**ASHRAE 160 surface mold growth criteria:**

30-day running average:
- RH < 80% (any surface temperature), OR
- RH < 98% and T < 5°C

For wood-based materials, this translates to:
- EMC < 16% for most conditions
- EMC < 20% only at very cold temperatures

## Design Considerations

### Material Selection for Moisture Management

**High moisture buffering applications:**

Select materials with high ξ values:
- Gypsum board for interior finishes (MBV = 1.0-1.4)
- Wood paneling in appropriate climates (MBV = 2.0-2.5)
- Cellulose insulation in assemblies tolerant of hygroscopic materials

**Low moisture storage applications:**

Use materials with minimal EMC:
- Closed-cell foam insulation in critical assemblies
- Cement board in high-humidity locations
- Non-hygroscopic vapor retarders

### Hygrothermal Modeling Inputs

When performing hygrothermal simulations (WUFI, DELPHIN, hygIRC):

**Required material-specific EMC data:**
1. Complete sorption isotherm (adsorption and desorption curves)
2. Moisture capacity function ξ(φ)
3. Temperature dependency of EMC
4. Liquid transport coefficients at high moisture contents

**Data sources:**
- ASHRAE Handbook—Fundamentals
- WUFI material database
- DELPHIN material database
- Laboratory testing per ASTM C1498

### Moisture Buffering Design

**Effective moisture buffer capacity:**

MBC_eff = Σ(d_i × ρ_i × ξ_i)

Where:
- MBC_eff = effective buffering capacity (kg/m² per unit RH)
- d_i = material layer thickness (m)
- ρ_i = dry density (kg/m³)
- ξ_i = moisture capacity (kg/kg per unit RH)
- Summation over all hygroscopic layers

**Practical buffering depth:**

Only materials within the penetration depth contribute significantly during daily RH cycles:

δ_p = √(D_w × t / π)

Where:
- δ_p = penetration depth (m)
- D_w = moisture diffusivity (m²/s)
- t = cycle period (s)

For 24-hour cycles and typical building materials:
δ_p ≈ 10-30 mm

This indicates that surface layers (gypsum, wood paneling, finish materials) provide most buffering capacity.

### Condensation Risk Assessment

**Critical moisture content criteria:**

Establish material-specific critical moisture content thresholds:

| Material | Critical MC | Consequence |
|----------|-------------|-------------|
| Wood framing | >20% | Decay fungi activation |
| Wood finishes | >16% | Mold growth risk |
| Gypsum board | >5% | Paper facing mold |
| Mineral wool | No limit | Performance unaffected |
| Cellulose | >25% | Settling, reduced R-value |

**Design verification:**

Ensure hygrothermal analysis demonstrates:
- Monthly average MC < critical values
- Peak MC events limited to <7 consecutive days
- Drying capacity exceeds wetting potential

## Best Practices

### EMC Data Acquisition

**Testing protocols:**
1. Condition specimens at multiple RH levels (0%, 30%, 50%, 75%, 90%, 95%)
2. Allow full equilibration (typically 4-8 weeks per RH level)
3. Measure both adsorption and desorption curves
4. Test at multiple temperatures (10°C, 20°C, 30°C minimum)

**Quality control:**
- Verify repeatability: ±0.5% MC
- Check closure of hysteresis loops
- Confirm thermodynamic consistency

### Field Moisture Assessment

**In-service moisture content limits:**

Wood structures:
- Acceptable range: 7-14% MC
- Investigation threshold: >16% MC
- Remediation required: >20% MC

Masonry:
- Normal range: 1-5% MC (gravimetric)
- Elevated: 5-10% MC
- Investigation: >10% MC

**Monitoring strategies:**
- Install EMC sensors in critical assembly locations
- Log temperature and RH to calculate theoretical EMC
- Compare measured vs. theoretical for validation

### Climate-Specific EMC Management

**Humid climates:**
- Design for sustained high EMC in exterior materials
- Provide drying capacity to both exterior and interior
- Limit interior hygroscopic materials to reduce buffering load on HVAC

**Dry climates:**
- Account for very low winter EMC and shrinkage
- Provide adequate humidification to prevent overdrying
- Use hygroscopic materials for passive humidity stabilization

**Mixed climates:**
- Design for maximum EMC range (summer to winter)
- Ensure materials can accommodate moisture content swings
- Implement seasonal HVAC control strategies

---

**File path:** `/Users/evgenygantman/Documents/github/gantmane/hvac/content/hvac-fundamentals/building-envelope-moisture/hygrothermal-material-properties/hygroscopic-moisture-content/material-specific-emc/_index.md`
