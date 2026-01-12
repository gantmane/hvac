---
title: "Material-Specific Sorption Isotherms"
description: "Detailed sorption isotherm characteristics for common building materials including wood, concrete, masonry, gypsum, and insulation materials with equations and data for hygrothermal analysis"
weight: 2
---

Material-specific sorption isotherms quantify the equilibrium moisture content of building materials as a function of relative humidity at constant temperature. These isotherms are fundamental to hygrothermal modeling, moisture buffering analysis, and prediction of material durability in building envelopes. Each material exhibits unique sorption behavior based on its pore structure, surface chemistry, and composition.

## Wood Sorption Isotherms

Wood exhibits strong hygroscopic behavior due to the presence of hydroxyl groups in cellulose, hemicellulose, and lignin. Moisture sorption in wood occurs through monolayer adsorption, multilayer adsorption, and capillary condensation in cell wall micropores.

### Equilibrium Moisture Content Relationships

The Hailwood-Horrobin model describes wood sorption:

**Hailwood-Horrobin Equation:**
```
u = (1800/W) × [(K₁h)/(1-K₁h) + (K₁K₂h)/(1+K₁K₂h)]
```

Where:
- u = equilibrium moisture content (%)
- W = molecular weight of wood substance (≈ 162 kg/kmol)
- K₁ = hydrate equilibrium constant
- K₂ = dissolution equilibrium constant
- h = relative humidity (decimal)

**Simplified Simpson Model:**
```
u = (1800/W) × [(K₁K₂h)/(1-K₂h) + (K₁h)/(1-K₁h)]
```

### Wood Species Isotherms

| Species | EMC at 30% RH | EMC at 50% RH | EMC at 70% RH | EMC at 90% RH |
|---------|---------------|---------------|---------------|---------------|
| Douglas Fir | 5.8% | 8.9% | 12.5% | 19.2% |
| Southern Pine | 6.1% | 9.2% | 13.0% | 19.8% |
| Red Oak | 6.0% | 9.1% | 12.8% | 19.6% |
| White Oak | 5.9% | 8.9% | 12.6% | 19.3% |
| Western Red Cedar | 5.5% | 8.4% | 11.9% | 18.5% |
| Spruce-Pine-Fir | 5.9% | 9.0% | 12.7% | 19.4% |
| Plywood (softwood) | 6.2% | 9.5% | 13.4% | 20.2% |
| OSB | 6.5% | 10.0% | 14.2% | 21.5% |

*Note: Values at 20°C (68°F). EMC decreases approximately 0.02-0.03% per °C increase.*

### Temperature Effect on Wood EMC

**Temperature Correction:**
```
u(T) = u(20°C) × [1 - α(T - 20)]
```

Where:
- α = temperature coefficient (typically 0.015-0.020 per °C)
- T = temperature (°C)

### Hysteresis in Wood

Wood exhibits significant hysteresis between adsorption and desorption:

**Hysteresis Ratio:**
- At 65% RH: Desorption EMC / Adsorption EMC ≈ 1.15
- At 80% RH: Desorption EMC / Adsorption EMC ≈ 1.20

## Concrete Sorption Isotherms

Concrete moisture storage is governed by water in capillary pores, gel pores in C-S-H (calcium silicate hydrate), and interlayer water. Sorption behavior depends strongly on water-cement ratio, degree of hydration, and aggregate type.

### Concrete Isotherm Models

**Xi-Bazant-Jennings Model:**
```
u = G₁[α₁h + (1-α₁)h^n₁] / [1 + (G₁-1)[α₁h + (1-α₁)h^n₁]]
```

Where:
- u = moisture content (kg/m³) normalized by maximum
- G₁ = ratio of maximum to monolayer capacity
- α₁, n₁ = empirical parameters
- h = relative humidity (decimal)

**Simplified Power Law:**
```
u = A × h^B
```

For typical concrete: A = 140-180 kg/m³, B = 3-5

### Concrete Moisture Content by w/c Ratio

| w/c Ratio | 50% RH | 65% RH | 80% RH | 95% RH | Saturation |
|-----------|--------|--------|--------|--------|------------|
| 0.40 | 25 kg/m³ | 35 kg/m³ | 50 kg/m³ | 85 kg/m³ | 110 kg/m³ |
| 0.50 | 30 kg/m³ | 42 kg/m³ | 60 kg/m³ | 100 kg/m³ | 135 kg/m³ |
| 0.60 | 35 kg/m³ | 50 kg/m³ | 72 kg/m³ | 120 kg/m³ | 160 kg/m³ |
| 0.70 | 40 kg/m³ | 58 kg/m³ | 85 kg/m³ | 140 kg/m³ | 185 kg/m³ |

*At 20°C, 28-day cured concrete*

### Maturity Effects

Concrete moisture storage capacity decreases with continued hydration:

**Maturity Correction:**
```
u(t) = u₂₈ × [1 + β × log(28/t)]
```

Where:
- t = age (days)
- β = maturity coefficient (typically 0.10-0.15)
- Valid for t < 28 days

## Brick and Masonry Isotherms

Clay brick and concrete masonry units exhibit different sorption characteristics based on firing temperature, composition, and pore structure.

### Clay Brick Isotherms

**Typical Clay Brick Moisture Content:**

| Brick Type | Bulk Density | 50% RH | 80% RH | 95% RH | Saturation |
|------------|--------------|--------|--------|--------|------------|
| Common brick | 1750 kg/m³ | 8 kg/m³ | 22 kg/m³ | 45 kg/m³ | 180 kg/m³ |
| Face brick | 1900 kg/m³ | 6 kg/m³ | 18 kg/m³ | 38 kg/m³ | 140 kg/m³ |
| Engineering brick | 2100 kg/m³ | 4 kg/m³ | 12 kg/m³ | 28 kg/m³ | 80 kg/m³ |
| Soft brick | 1650 kg/m³ | 12 kg/m³ | 32 kg/m³ | 65 kg/m³ | 240 kg/m³ |

### Concrete Masonry Units (CMU)

**CMU Moisture Content:**

| CMU Type | Density | 50% RH | 80% RH | 95% RH | Saturation |
|----------|---------|--------|--------|--------|------------|
| Normal weight | 2000 kg/m³ | 18 kg/m³ | 40 kg/m³ | 75 kg/m³ | 150 kg/m³ |
| Medium weight | 1700 kg/m³ | 22 kg/m³ | 50 kg/m³ | 95 kg/m³ | 190 kg/m³ |
| Lightweight | 1400 kg/m³ | 28 kg/m³ | 65 kg/m³ | 120 kg/m³ | 250 kg/m³ |

### Mortar Isotherms

Mortar exhibits similar behavior to concrete but with variations based on lime content:

**Type N Mortar (1:1:6):**
```
u = 25h + 85h⁴  (kg/m³)
```

**Type S Mortar (1:0.5:4.5):**
```
u = 22h + 75h⁴  (kg/m³)
```

## Gypsum Board Isotherms

Gypsum board (calcium sulfate dihydrate with paper facing) exhibits distinct sorption in the gypsum core versus the paper facing.

### Gypsum Core Isotherm

**Modified GAB Model for Gypsum:**
```
u = (u_m × C × K × h) / [(1-K×h)(1-K×h+C×K×h)]
```

Where:
- u_m = monolayer moisture content ≈ 0.8-1.0%
- C = Guggenheim constant ≈ 8-12
- K = multilayer constant ≈ 0.85-0.95

### Gypsum Board Moisture Content

| Board Type | Thickness | 40% RH | 60% RH | 80% RH | 95% RH |
|------------|-----------|--------|--------|--------|--------|
| Regular | 12.7 mm (1/2") | 0.45% | 0.85% | 1.8% | 4.2% |
| Regular | 15.9 mm (5/8") | 0.45% | 0.85% | 1.8% | 4.2% |
| Type X | 15.9 mm (5/8") | 0.42% | 0.80% | 1.7% | 4.0% |
| Paperless | 12.7 mm (1/2") | 0.38% | 0.72% | 1.5% | 3.5% |
| Moisture-resistant | 12.7 mm (1/2") | 0.35% | 0.65% | 1.3% | 3.0% |

*Percentages by mass*

### Paper Facing Contribution

Paper facing contributes significantly to total moisture storage:

**Total Moisture Content:**
```
u_total = w_gypsum × u_gypsum + w_paper × u_paper
```

Where:
- w_gypsum ≈ 0.92 (weight fraction)
- w_paper ≈ 0.08 (weight fraction)
- u_paper follows cellulose isotherm (similar to wood)

## Insulation Material Isotherms

Insulation materials exhibit widely varying sorption behavior from nearly non-hygroscopic (closed-cell foam) to highly hygroscopic (cellulose, mineral wool).

### Fibrous Insulation

**Fiberglass Insulation:**

Minimal sorption, primarily on binder:
```
u = 0.02h + 0.15h⁶  (% by mass)
```

At 80% RH: u ≈ 0.4%

**Mineral Wool (Stone Wool):**

| Product | Density | 50% RH | 80% RH | 95% RH |
|---------|---------|--------|--------|--------|
| Batt insulation | 30 kg/m³ | 0.15 kg/m³ | 0.45 kg/m³ | 1.2 kg/m³ |
| Board insulation | 100 kg/m³ | 0.50 kg/m³ | 1.5 kg/m³ | 4.0 kg/m³ |
| High-density board | 150 kg/m³ | 0.75 kg/m³ | 2.2 kg/m³ | 6.0 kg/m³ |

### Cellulose Insulation

Cellulose is highly hygroscopic due to cellulose fiber structure:

**Cellulose Isotherm:**
```
u = 0.08h + 0.12h² + 0.15h⁴  (kg/kg)
```

**Cellulose Moisture Content:**

| Density | 40% RH | 60% RH | 80% RH | 95% RH |
|---------|--------|--------|--------|--------|
| 50 kg/m³ | 2.5 kg/m³ | 4.5 kg/m³ | 8.5 kg/m³ | 14.0 kg/m³ |
| 60 kg/m³ | 3.0 kg/m³ | 5.4 kg/m³ | 10.2 kg/m³ | 16.8 kg/m³ |

### Foam Insulation

**Extruded Polystyrene (XPS):**

Negligible moisture sorption; moisture content primarily from condensation in cells:
```
u < 0.1% by volume for h < 0.90
```

**Expanded Polystyrene (EPS):**
```
u ≈ 0.02h³  (% by volume)
```

At 80% RH: u ≈ 1.0% by volume

**Closed-Cell Spray Polyurethane Foam:**

Essentially non-hygroscopic:
```
u < 0.05% by volume for all RH
```

**Open-Cell Spray Polyurethane Foam:**

Limited sorption on cell struts:
```
u = 0.01h + 0.08h⁵  (% by mass)
```

### Rigid Board Insulation

**Polyisocyanurate (PIR) with Facers:**

| Facer Type | 50% RH | 80% RH | 95% RH |
|------------|--------|--------|--------|
| Foil both sides | 0.1% | 0.2% | 0.5% |
| Fiberglass mat | 0.8% | 2.2% | 4.5% |
| Organic felt | 1.2% | 3.5% | 7.0% |

*Percentages by mass of board*

**Mineral Wool Board:**

| Density | 50% RH | 80% RH | 95% RH |
|---------|--------|--------|--------|
| 100 kg/m³ | 0.5 kg/m³ | 1.5 kg/m³ | 4.0 kg/m³ |
| 150 kg/m³ | 0.75 kg/m³ | 2.2 kg/m³ | 6.0 kg/m³ |
| 200 kg/m³ | 1.0 kg/m³ | 3.0 kg/m³ | 8.0 kg/m³ |

## Engineered Wood Products

### Oriented Strand Board (OSB)

OSB exhibits higher moisture uptake than plywood due to strand geometry and adhesive distribution:

**OSB Moisture Content:**

| Grade | 50% RH | 65% RH | 80% RH | 95% RH |
|-------|--------|--------|--------|--------|
| OSB/1 (interior) | 10.5% | 12.8% | 15.5% | 22.5% |
| OSB/2 (structural) | 10.0% | 12.2% | 14.8% | 21.8% |
| OSB/3 (exterior) | 9.2% | 11.2% | 13.6% | 20.2% |

### Plywood

**Plywood Moisture Content by Glue Type:**

| Glue Type | 50% RH | 65% RH | 80% RH | 95% RH |
|-----------|--------|--------|--------|--------|
| Phenol-formaldehyde | 8.8% | 10.5% | 13.0% | 19.5% |
| Melamine-urea | 9.2% | 11.0% | 13.8% | 20.5% |
| Urea-formaldehyde | 9.5% | 11.5% | 14.5% | 21.5% |

### Medium Density Fiberboard (MDF)

MDF is highly hygroscopic due to fine fiber structure:

**MDF Isotherm:**
```
u = 0.095h + 0.08h² + 0.12h⁴  (kg/kg)
```

**MDF Moisture Content:**

| Density | 50% RH | 65% RH | 80% RH | 95% RH |
|---------|--------|--------|--------|--------|
| 600 kg/m³ | 54 kg/m³ | 69 kg/m³ | 96 kg/m³ | 150 kg/m³ |
| 750 kg/m³ | 68 kg/m³ | 86 kg/m³ | 120 kg/m³ | 188 kg/m³ |

## Application in Hygrothermal Modeling

### Material Database Requirements

Hygrothermal simulation programs (WUFI, DELPHIN, hygIRC) require complete isotherm data:

**Required Data Points:**
- Minimum 8-10 RH points from 0% to 98% RH
- Both adsorption and desorption curves
- Temperature dependence data (at least 2 temperatures)
- Free water saturation moisture content

### Interpolation Methods

Between measured points, appropriate interpolation is critical:

**Spline Interpolation:**
```
u(h) = Σ[aᵢ(h-hᵢ)³ + bᵢ(h-hᵢ)² + cᵢ(h-hᵢ) + dᵢ]
```

Applied piecewise between measurement points.

### Hysteresis Implementation

**Scanning Curve Approach:**

When RH changes direction, moisture content follows scanning curves between main isotherms:

```
u_scan = u_ads + f(h)×(u_des - u_ads)
```

Where f(h) depends on reversal history.

## Measurement Standards and Protocols

### Standard Test Methods

**ASTM C1498** - Standard Test Method for Hygroscopic Sorption Isotherms of Building Materials

**ISO 12571** - Hygrothermal performance of building materials and products — Determination of hygroscopic sorption properties

### Equilibrium Criteria

Sample considered at equilibrium when:
```
Δm/Δt < 0.001% per 24 hours
```

Typical equilibration times:
- Low RH (< 50%): 7-14 days
- High RH (> 80%): 14-28 days
- Dense materials: longer equilibration

## Design Implications

### Moisture Buffering Capacity

Materials with steep isotherms in the 40-70% RH range provide effective moisture buffering:

**Buffering Value Calculation:**
```
BV = (u₇₅% - u₃₃%) × ρ × δₚ × √(t/π)
```

Where:
- ρ = material density (kg/m³)
- δₚ = vapor permeability (kg/(m·s·Pa))
- t = time period (s)

**Effective Buffering Materials:**
- Gypsum board: BV = 1.5-2.0 g/(m²·%RH)
- Wood paneling: BV = 2.0-3.0 g/(m²·%RH)
- Cellulose insulation: BV = 1.2-1.8 g/(m²·%RH)

### Critical Moisture Content

Design must account for critical moisture contents:

| Material | Moisture Content | Significance |
|----------|------------------|--------------|
| Wood | 20% | Fiber saturation point |
| Wood | 28% | Fungal growth threshold |
| Gypsum | 1% | Equilibrium at 60% RH |
| Gypsum | 5% | Risk of mold growth |
| Concrete | 75% of saturation | Freeze-thaw damage risk |
| Brick | 80% RH exposure | Efflorescence risk |

### Selection Criteria

**For Moisture Buffering Applications:**
- Select materials with high moisture capacity in service RH range
- Ensure adequate vapor permeability for buffering response
- Consider surface area exposure

**For Low Moisture Sensitivity:**
- Prefer materials with flat isotherms (low uptake)
- Consider vapor-impermeable materials where appropriate
- Minimize hygroscopic material exposure in high-RH zones

## Temperature-Dependent Isotherm Adjustment

### Thermodynamic Relationships

Sorption isotherms shift with temperature following thermodynamic principles:

**Clausius-Clapeyron Relationship:**
```
ln(h₂/h₁) = (ΔH_ads/R) × [(1/T₁) - (1/T₂)]
```

Where:
- ΔH_ads = heat of adsorption (J/mol)
- R = universal gas constant (8.314 J/(mol·K))
- T = absolute temperature (K)

**Typical Heat of Adsorption Values:**
- Wood: 45-60 kJ/mol
- Gypsum: 40-50 kJ/mol
- Concrete: 50-65 kJ/mol
- Cellulose: 45-55 kJ/mol

### Practical Temperature Correction

**Simplified Correction Factor:**
```
u(T₂) = u(T₁) × [1 - α(T₂ - T₁)]
```

Where α ranges from 0.010-0.020 per °C for most building materials.

## Quality Assurance in Isotherm Data

### Data Validation Checks

**Physical Constraints:**
- Monotonically increasing with RH
- Smooth curve without discontinuities
- Desorption ≥ Adsorption at all RH
- Zero intercept at h = 0

**Consistency Checks:**
```
0 < u(h) < u_sat for all h < 1.0
du/dh > 0 for all h
```

### Uncertainty Analysis

Measurement uncertainty in isotherms affects hygrothermal predictions:

**Typical Uncertainties:**
- RH control: ±2% RH
- Mass measurement: ±0.1% of sample mass
- Temperature: ±0.2°C

**Propagated uncertainty in moisture content:**
```
σ_u = √[(∂u/∂h × σ_h)² + (∂u/∂T × σ_T)²]
```

## ASHRAE References

**ASHRAE Handbook - Fundamentals (Chapter 26)**: Heat, Air, and Moisture Control in Building Assemblies - Material Properties

**ASHRAE 160**: Criteria for Moisture-Control Design Analysis in Buildings - Material property requirements

**ASHRAE 1449-RP**: Material Properties for Hygrothermal Modeling - Comprehensive isotherm database

## Advanced Considerations

### Multi-Regime Sorption

Some materials exhibit distinct sorption mechanisms across RH ranges:

**Low RH (0-50%):** Monolayer and multilayer adsorption
**Medium RH (50-80%):** Micropore filling
**High RH (80-98%):** Capillary condensation
**Over-hygroscopic (>98%):** Free water absorption

### Salt-Contaminated Materials

Presence of hygroscopic salts dramatically alters isotherms:

**Modified Isotherm with Salts:**
```
u_total = u_matrix(h) + u_salt(h)
```

Salts can increase moisture content by 2-10× at high RH.

### Aging Effects

Long-term exposure to moisture cycling can alter sorption properties:
- Carbonation in concrete (reduced capacity)
- Loss of sizing in wood products
- Binder degradation in insulation

Regular isotherm updates may be needed for service life > 20 years.

---

Material-specific sorption isotherms form the foundation of accurate hygrothermal analysis. Selection of appropriate materials and understanding their moisture storage behavior is critical for durable, energy-efficient building envelope design that maintains indoor environmental quality while preventing moisture-related deterioration.
