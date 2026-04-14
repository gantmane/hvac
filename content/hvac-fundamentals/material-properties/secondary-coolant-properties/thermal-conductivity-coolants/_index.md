---
title: "Thermal Conductivity of Secondary Coolants"
aliases: ["Thermal Conductivity of Secondary Coolants"]
description: "Comprehensive analysis of thermal conductivity in secondary refrigerants including glycol solutions and brines. Covers temperature dependence, concentration effects, heat transfer coefficients, and heat exchanger design implications for HVAC systems."
weight: 5
---

## Technical Overview

Thermal conductivity (k) represents the ability of a secondary coolant to conduct heat through its bulk fluid mass. This transport property directly influences convective heat transfer coefficients, overall heat transfer rates, and ultimately the required heat exchanger surface area in secondary refrigeration systems.

The thermal conductivity of secondary coolants is invariably lower than that of water, resulting in reduced heat transfer performance. This fundamental limitation must be accounted for in all heat exchanger sizing and system design calculations.

## Fundamental Physics

### Heat Conduction Mechanism

Heat conduction in liquid coolants occurs through three mechanisms:

**Molecular Translation**
Energy transfer via translational motion of molecules from high to low temperature regions. This dominates in low-viscosity fluids.

**Molecular Vibration**
Energy transfer through vibrational modes of polyatomic molecules. This becomes significant in glycol solutions with complex molecular structures.

**Molecular Rotation**
Rotational energy transfer between adjacent molecules. This contributes minimally in most secondary coolants.

### Fourier's Law

The governing equation for steady-state heat conduction:

```
q = -k × A × (dT/dx)
```

Where:
- q = heat transfer rate (W)
- k = thermal conductivity (W/m·K)
- A = cross-sectional area perpendicular to heat flow (m²)
- dT/dx = temperature gradient (K/m)

The negative sign indicates heat flows from high to low temperature.

## Temperature Dependence

### General Relationship

Thermal conductivity of secondary coolants exhibits weak positive temperature dependence:

```
k(T) = k₀ × [1 + α × (T - T₀)]
```

Where:
- k(T) = thermal conductivity at temperature T (W/m·K)
- k₀ = reference thermal conductivity at T₀ (W/m·K)
- α = temperature coefficient (K⁻¹)
- T₀ = reference temperature (typically 0°C or 20°C)

For most secondary coolants, α ranges from 0.001 to 0.003 K⁻¹, indicating thermal conductivity increases approximately 0.1-0.3% per degree Celsius.

### Temperature Effect Magnitude

The temperature dependence is considerably weaker than the concentration dependence. Over typical HVAC operating ranges (-40°C to +20°C), temperature variations cause 6-18% changes in thermal conductivity, whereas concentration changes can reduce k by 30-50% compared to pure water.

## Concentration Effects

### Dilution Impact

Adding antifreeze to water systematically reduces thermal conductivity:

```
k_mix < k_water
```

This occurs because:
1. Glycol molecules have lower intrinsic thermal conductivity than water
2. Hydrogen bonding networks are disrupted
3. Molecular motion is hindered by increased viscosity
4. Energy transfer pathways become less efficient

### Empirical Correlation

A general form for concentration dependence:

```
k_solution = k_water × (1 - β × C + γ × C²)
```

Where:
- C = mass fraction of antifreeze (0 to 1)
- β, γ = empirical constants depending on antifreeze type

For ethylene glycol: β ≈ 0.45, γ ≈ 0.15
For propylene glycol: β ≈ 0.50, γ ≈ 0.20

### Maximum Reduction

At typical freeze protection concentrations (30-50% by mass), thermal conductivity reductions are:

| Antifreeze Type | Concentration | k Reduction |
|-----------------|---------------|-------------|
| Ethylene glycol | 30% | 25-30% |
| Ethylene glycol | 40% | 30-35% |
| Ethylene glycol | 50% | 35-40% |
| Propylene glycol | 30% | 28-33% |
| Propylene glycol | 40% | 33-38% |
| Propylene glycol | 50% | 38-43% |
| Calcium chloride brine | 20% | 15-20% |
| Sodium chloride brine | 20% | 12-18% |

## Thermal Conductivity Data Tables

### Ethylene Glycol Solutions

| Temperature (°C) | Pure Water | 30% EG | 40% EG | 50% EG |
|------------------|------------|--------|--------|--------|
| -40 | - | 0.415 | 0.398 | 0.380 |
| -30 | - | 0.425 | 0.408 | 0.390 |
| -20 | 0.540 | 0.435 | 0.418 | 0.400 |
| -10 | 0.555 | 0.445 | 0.428 | 0.410 |
| 0 | 0.571 | 0.455 | 0.438 | 0.420 |
| 10 | 0.585 | 0.465 | 0.448 | 0.430 |
| 20 | 0.598 | 0.475 | 0.458 | 0.440 |

All values in W/m·K at atmospheric pressure.

### Propylene Glycol Solutions

| Temperature (°C) | Pure Water | 30% PG | 40% PG | 50% PG |
|------------------|------------|--------|--------|--------|
| -40 | - | 0.395 | 0.375 | 0.355 |
| -30 | - | 0.405 | 0.385 | 0.365 |
| -20 | 0.540 | 0.415 | 0.395 | 0.375 |
| -10 | 0.555 | 0.425 | 0.405 | 0.385 |
| 0 | 0.571 | 0.435 | 0.415 | 0.395 |
| 10 | 0.585 | 0.445 | 0.425 | 0.405 |
| 20 | 0.598 | 0.455 | 0.435 | 0.415 |

All values in W/m·K at atmospheric pressure.

### Calcium Chloride Brine

| Temperature (°C) | Pure Water | 15% CaCl₂ | 20% CaCl₂ | 25% CaCl₂ |
|------------------|------------|-----------|-----------|-----------|
| -40 | - | 0.475 | 0.460 | 0.445 |
| -30 | - | 0.485 | 0.470 | 0.455 |
| -20 | 0.540 | 0.495 | 0.480 | 0.465 |
| -10 | 0.555 | 0.505 | 0.490 | 0.475 |
| 0 | 0.571 | 0.515 | 0.500 | 0.485 |
| 10 | 0.585 | 0.525 | 0.510 | 0.495 |
| 20 | 0.598 | 0.535 | 0.520 | 0.505 |

All values in W/m·K at atmospheric pressure.

### Sodium Chloride Brine

| Temperature (°C) | Pure Water | 10% NaCl | 15% NaCl | 20% NaCl |
|------------------|------------|----------|----------|----------|
| -20 | 0.540 | 0.500 | 0.485 | 0.470 |
| -10 | 0.555 | 0.510 | 0.495 | 0.480 |
| 0 | 0.571 | 0.520 | 0.505 | 0.490 |
| 10 | 0.585 | 0.530 | 0.515 | 0.500 |
| 20 | 0.598 | 0.540 | 0.525 | 0.510 |

All values in W/m·K at atmospheric pressure.

## Impact on Heat Transfer Coefficients

### Convective Heat Transfer

The convective heat transfer coefficient (h) relates thermal conductivity through dimensionless analysis:

```
Nu = (h × D) / k
```

Where:
- Nu = Nusselt number (dimensionless)
- h = convective heat transfer coefficient (W/m²·K)
- D = characteristic length (m)
- k = thermal conductivity (W/m·K)

Solving for h:

```
h = (Nu × k) / D
```

This shows heat transfer coefficient is directly proportional to thermal conductivity. A 30% reduction in k produces a 30% reduction in h, all else equal.

### Film Coefficients

The film coefficient (individual convective coefficient) for internal flow:

```
h_i = (Nu_D × k) / D_i
```

For turbulent flow in tubes (Re > 10,000):

```
Nu_D = 0.023 × Re^0.8 × Pr^0.4
```

Where:
- Re = Reynolds number = (ρ × V × D) / μ
- Pr = Prandtl number = (c_p × μ) / k

The thermal conductivity appears in both the Nusselt correlation (through Pr) and the conversion to h, creating compound effects.

### Prandtl Number Effects

The Prandtl number represents the ratio of momentum diffusivity to thermal diffusivity:

```
Pr = (c_p × μ) / k
```

For secondary coolants:
- Pure water at 0°C: Pr ≈ 13
- 40% ethylene glycol at 0°C: Pr ≈ 50
- 40% propylene glycol at 0°C: Pr ≈ 85

Higher Prandtl numbers indicate thicker thermal boundary layers relative to velocity boundary layers, reducing heat transfer effectiveness.

## Overall Heat Transfer Coefficient

### Series Resistance Model

In heat exchangers, overall heat transfer coefficient (U) depends on thermal conductivity through film coefficients:

```
1/U = 1/h_i + t_wall/k_wall + 1/h_o + R_fouling
```

Where:
- U = overall heat transfer coefficient (W/m²·K)
- h_i = inside film coefficient (W/m²·K)
- h_o = outside film coefficient (W/m²·K)
- t_wall = wall thickness (m)
- k_wall = wall thermal conductivity (W/m·K)
- R_fouling = fouling resistance (m²·K/W)

### Typical U Values

Representative overall heat transfer coefficients:

| Configuration | Pure Water | 40% Glycol | Reduction |
|---------------|------------|------------|-----------|
| Plate heat exchanger (liquid-liquid) | 3000-4500 | 1800-2800 | 35-40% |
| Shell-and-tube (liquid-liquid) | 850-1400 | 550-900 | 30-35% |
| Direct expansion evaporator | 1700-2800 | 1100-1800 | 30-35% |
| Air coil (finned tube) | 60-120 | 45-90 | 20-30% |

The reduction is less than the thermal conductivity reduction alone because air-side or refrigerant-side resistance often dominates.

## Nusselt Number Correlations

### Turbulent Flow in Tubes

**Dittus-Boelter Equation** (heating):

```
Nu = 0.023 × Re^0.8 × Pr^0.4
```

Valid for:
- Re > 10,000
- 0.7 < Pr < 160
- L/D > 10

**Gnielinski Correlation** (more accurate):

```
Nu = [(f/8) × (Re - 1000) × Pr] / [1 + 12.7 × (f/8)^0.5 × (Pr^(2/3) - 1)]
```

Where f = friction factor = (0.790 × ln(Re) - 1.64)^(-2)

Valid for:
- 3000 < Re < 5×10⁶
- 0.5 < Pr < 2000

### Laminar Flow in Tubes

For fully developed laminar flow:

**Constant wall temperature:**
```
Nu = 3.66 (circular tubes)
```

**Constant heat flux:**
```
Nu = 4.36 (circular tubes)
```

These are independent of Re and Pr, indicating thermal conductivity's direct impact dominates in laminar regimes.

### Plate Heat Exchangers

Modified correlation for plate geometries:

```
Nu = C × Re^m × Pr^(1/3)
```

Where C and m depend on plate corrugation:
- C = 0.15-0.40
- m = 0.65-0.85

The weaker Reynolds number dependence (compared to tubes) means thermal conductivity effects are more pronounced in plate exchangers.

## Heat Exchanger Sizing Implications

### Required Surface Area

The fundamental heat exchanger equation:

```
Q = U × A × LMTD
```

Solving for required area:

```
A = Q / (U × LMTD)
```

Where:
- Q = heat transfer rate (W)
- A = heat transfer surface area (m²)
- LMTD = log mean temperature difference (K)

Since U decreases with thermal conductivity, required area increases proportionally.

### Size Penalty Factor

The additional heat transfer area required when using glycol versus water:

```
SF = A_glycol / A_water = U_water / U_glycol
```

Typical size penalty factors:

| Glycol Concentration | Plate HX | Shell-Tube | Air Coil |
|----------------------|----------|------------|----------|
| 25% ethylene glycol | 1.20 | 1.18 | 1.12 |
| 35% ethylene glycol | 1.30 | 1.25 | 1.15 |
| 45% ethylene glycol | 1.40 | 1.32 | 1.18 |
| 25% propylene glycol | 1.25 | 1.22 | 1.15 |
| 35% propylene glycol | 1.35 | 1.28 | 1.18 |
| 45% propylene glycol | 1.45 | 1.35 | 1.22 |

### Economic Implications

The size penalty translates directly to cost:
- 20-45% increase in heat exchanger first cost
- Larger footprint and space requirements
- Increased refrigerant charge (DX systems)
- Higher pressure drop (partially offsetting smaller temperature differences)

## Design Considerations

### Concentration Optimization

Select minimum concentration providing adequate freeze protection:

```
C_min = f(T_minimum, safety_factor)
```

Standard practice: design for 5-10°F (3-6°C) below minimum expected fluid temperature.

Over-concentration penalties:
- Reduced thermal conductivity (3-5% per 10% excess concentration)
- Increased viscosity (15-25% per 10% excess concentration)
- Higher pumping energy (20-40% per 10% excess concentration)
- Greater pressure drop

### Temperature Selection

Higher operating temperatures improve thermal conductivity:
- Increase k by 1-2% per 5°C temperature rise
- Reduce viscosity by 10-15% per 5°C temperature rise
- Compound benefit to heat transfer coefficient

Balance against:
- Refrigeration system efficiency (lower condensing temperature preferred)
- Process requirements
- Storage stability

### Flow Velocity

Increase velocity to compensate for reduced thermal conductivity:

The convective coefficient scales approximately:

```
h ∝ V^0.8 (turbulent flow)
```

A 25% velocity increase produces approximately 20% improvement in h, partially offsetting thermal conductivity reduction.

Limitations:
- Pressure drop increases as V²
- Erosion concerns above 3-4 m/s
- Pumping energy rises significantly

### Enhanced Heat Transfer Surfaces

Compensate for thermal conductivity reduction through surface enhancement:

**Turbulence promoters:**
- Internal fins
- Twisted tape inserts
- Wire coil inserts

Enhancement factors: 1.5-3.0× baseline h

**Extended surfaces:**
- External fins (air coils)
- Enhanced tube surfaces (fluted, corrugated)

Effectiveness factors: 2.5-5.0× bare tube area

**Plate heat exchangers:**
- Herringbone patterns
- Chevron corrugations

Provide inherently higher h (3-5× shell-and-tube)

## ASHRAE References

### Fundamental Data Sources

**ASHRAE Handbook—Fundamentals (2021), Chapter 31: Physical Properties of Secondary Coolants**
- Thermal conductivity data tables for common coolants
- Temperature and concentration correlations
- Measurement methods and uncertainties

**ASHRAE Handbook—Fundamentals (2021), Chapter 4: Heat Transfer**
- Convective heat transfer correlations
- Dimensionless analysis methods
- Heat exchanger effectiveness-NTU method

**ASHRAE Handbook—HVAC Systems and Equipment (2020), Chapter 13: Liquid Coolers**
- Heat exchanger sizing procedures incorporating thermal conductivity effects
- Selection guidelines for secondary coolants

### Design Standards

**ASHRAE Standard 15-2019: Safety Standard for Refrigeration Systems**
- Secondary coolant selection criteria
- Leak detection requirements
- Pressure relief sizing (affects by coolant properties)

**ASHRAE Guideline 3-2018: Reducing Emission of Halogenated Refrigerants from Refrigerating and Air-Conditioning Equipment and Systems**
- Promotes secondary coolant systems for refrigerant containment
- Design best practices

## Related Properties Interaction

### Thermal Conductivity and Viscosity

These properties interact in the Prandtl number:

```
Pr = (c_p × μ) / k
```

Glycol addition:
- Increases viscosity: +100-400%
- Decreases thermal conductivity: -30-40%
- Net effect: Pr increases 200-700%

High Prandtl numbers indicate heat transfer is more difficult than momentum transfer, leading to thick thermal boundary layers.

### Thermal Conductivity and Density

Mass flow requirements:

```
ṁ = Q / (c_p × ΔT)
```

Volumetric flow:

```
V̇ = ṁ / ρ = Q / (ρ × c_p × ΔT)
```

Lower thermal conductivity requires larger heat exchangers to achieve Q, but flow rates remain determined by c_p and ΔT, not k directly.

### Thermal Conductivity and Specific Heat

The thermal diffusivity combines these properties:

```
α = k / (ρ × c_p)
```

Where α represents the rate of temperature change in transient situations.

For secondary coolants:
- Pure water at 0°C: α = 0.137 × 10⁻⁶ m²/s
- 40% ethylene glycol at 0°C: α = 0.106 × 10⁻⁶ m²/s
- 40% propylene glycol at 0°C: α = 0.095 × 10⁻⁶ m²/s

Lower thermal diffusivity means slower thermal response during load changes or startup.

## Measurement Methods

### Transient Hot-Wire Method

Standard technique for liquid thermal conductivity:
1. Immerse fine platinum wire in fluid
2. Apply constant heat flux to wire
3. Measure temperature rise versus time
4. Calculate k from transient heat conduction equation

Accuracy: ±2-3% for calibrated systems

### Guarded Hot-Plate Method

Less common for liquids, used for reference measurements:
- Maintains one-dimensional heat flow
- Direct application of Fourier's law
- High accuracy (±1%) but complex apparatus

### Correlation Methods

For field applications, estimate k from temperature and concentration using published correlations.

Uncertainty: ±5-10% depending on data quality and extrapolation range

## Best Practices

1. **Use manufacturer data when available** - Inhibited coolants may have different properties than pure solutions

2. **Account for temperature variation** - Use average bulk temperature or integrate along flow path for precise calculations

3. **Consider aging effects** - Thermal conductivity remains stable, but degraded inhibitors may cause fouling that increases thermal resistance

4. **Verify concentration periodically** - Use refractometer or titration to confirm in-service concentration

5. **Design for minimum concentration** - Over-protection wastes energy and increases capital cost

6. **Evaluate enhanced surfaces** - Often more cost-effective than oversizing standard heat exchangers

7. **Calculate actual film coefficients** - Don't rely on generic U values; compute h_i and h_o specifically for your coolant

8. **Include fouling margins** - Secondary coolants may foul differently than water; consult TEMA or manufacturer data

9. **Optimize flow distribution** - Uneven flow reduces effective heat transfer more severely with high-Pr fluids

10. **Consider pump energy** - Reduced thermal conductivity requires larger heat exchangers, but increased flow velocity trades higher pumping costs for improved heat transfer

## Performance Verification

### Field Testing

Measure actual overall heat transfer coefficient:

```
U_actual = Q_measured / (A × LMTD_measured)
```

Compare to design calculations. Typical causes of discrepancy:
- Incorrect coolant concentration
- Flow maldistribution
- Fouling accumulation
- Air entrainment (reduces effective k)

### Acceptance Criteria

ASHRAE Standard 30-2019 (Methods of Testing Liquid Chilling Packages) suggests:
- Measured capacity within 5% of rating
- Corresponding U-value verification

For secondary coolant systems, allow additional tolerance (±10%) due to property uncertainty.

## Conclusion

Thermal conductivity is a critical transport property governing heat transfer rates in secondary coolant systems. The systematic reduction in k when antifreeze is added to water (30-40% for typical glycol concentrations) directly reduces heat transfer coefficients and increases required heat exchanger surface area by 20-45%.

Design engineers must account for these effects through:
- Accurate property data at operating conditions
- Rigorous heat transfer calculations using appropriate Nusselt correlations
- Selection of minimum freeze protection concentration
- Consideration of enhanced heat transfer surfaces
- Optimization of flow velocities within pressure drop constraints

Proper attention to thermal conductivity effects ensures secondary coolant systems achieve specified performance while avoiding costly over-design or inadequate capacity.
