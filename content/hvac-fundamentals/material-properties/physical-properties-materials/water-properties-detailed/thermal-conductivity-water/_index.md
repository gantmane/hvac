---
title: "Thermal Conductivity of Water"
description: "Comprehensive analysis of water thermal conductivity in HVAC applications including temperature dependencies, calculation methods, heat exchanger design implications, and fouling factor considerations"
weight: 4
---

## Fundamental Principles

Thermal conductivity (k) represents the ability of water to conduct heat through molecular-level energy transfer mechanisms. For HVAC applications involving hydronic systems, heat exchangers, and thermal storage, understanding water's thermal conductivity is critical for accurate heat transfer calculations and equipment sizing.

Water conducts heat through two primary mechanisms:

1. **Molecular Translation**: Random molecular motion transfers kinetic energy from high-temperature regions to low-temperature regions
2. **Molecular Rotation and Vibration**: Quantum mechanical energy states contribute to energy transport

The thermal conductivity of water increases with temperature due to enhanced molecular mobility and mean free path, contrary to most gases where conductivity decreases with temperature under certain conditions.

## Temperature Dependence

Water thermal conductivity exhibits a nearly linear relationship with temperature over the typical HVAC operating range (0-100°C / 32-212°F):

**General Trend**: k increases approximately 0.14% per degree Celsius in the range 0-100°C

### Empirical Correlation

For liquid water at atmospheric pressure (14.7 psia / 101.325 kPa):

```
k(T) = 0.5650 + 0.00190 × T - 0.00000680 × T²
```

Where:
- k = thermal conductivity (W/m·K)
- T = temperature (°C)

**Valid Range**: 0-150°C
**Accuracy**: ±1.5%

### Alternative Polynomial Expression (SI Units)

For higher precision across extended temperature ranges:

```
k(T) = -0.8690 + 0.00894 × T - 0.0000158 × T² + 0.00000000808 × T³
```

**Valid Range**: 0-200°C
**Accuracy**: ±0.5%

### IP Units Correlation

For temperature in degrees Fahrenheit:

```
k(T) = 0.3270 + 0.000596 × T - 0.00000105 × T²
```

Where:
- k = thermal conductivity (BTU/hr·ft·°F)
- T = temperature (°F)

**Valid Range**: 32-300°F

## Thermal Conductivity Data Tables

### SI Units (W/m·K)

| Temperature (°C) | Temperature (°F) | k (W/m·K) | % Change from 20°C |
|-----------------|------------------|-----------|-------------------|
| 0 | 32 | 0.561 | -6.19% |
| 5 | 41 | 0.571 | -4.51% |
| 10 | 50 | 0.580 | -3.01% |
| 15 | 59 | 0.589 | -1.50% |
| 20 | 68 | 0.598 | 0.00% (reference) |
| 25 | 77 | 0.607 | +1.50% |
| 30 | 86 | 0.615 | +2.84% |
| 35 | 95 | 0.623 | +4.18% |
| 40 | 104 | 0.631 | +5.52% |
| 45 | 113 | 0.637 | +6.52% |
| 50 | 122 | 0.644 | +7.69% |
| 55 | 131 | 0.649 | +8.53% |
| 60 | 140 | 0.654 | +9.36% |
| 65 | 149 | 0.659 | +10.20% |
| 70 | 158 | 0.663 | +10.87% |
| 75 | 167 | 0.667 | +11.54% |
| 80 | 176 | 0.670 | +12.04% |
| 85 | 185 | 0.673 | +12.54% |
| 90 | 194 | 0.675 | +12.88% |
| 95 | 203 | 0.677 | +13.21% |
| 100 | 212 | 0.679 | +13.55% |

### IP Units (BTU/hr·ft·°F)

| Temperature (°F) | k (BTU/hr·ft·°F) | % Change from 68°F |
|-----------------|------------------|-------------------|
| 32 | 0.3241 | -6.19% |
| 40 | 0.3289 | -4.64% |
| 50 | 0.3351 | -2.85% |
| 60 | 0.3406 | -1.26% |
| 68 | 0.3454 | 0.00% (reference) |
| 70 | 0.3461 | +0.20% |
| 80 | 0.3509 | +1.59% |
| 90 | 0.3554 | +2.89% |
| 100 | 0.3594 | +4.05% |
| 110 | 0.3630 | +5.09% |
| 120 | 0.3662 | +6.02% |
| 130 | 0.3690 | +6.83% |
| 140 | 0.3714 | +7.53% |
| 150 | 0.3735 | +8.14% |
| 160 | 0.3752 | +8.63% |
| 170 | 0.3766 | +9.04% |
| 180 | 0.3776 | +9.32% |
| 190 | 0.3783 | +9.52% |
| 200 | 0.3787 | +9.64% |
| 212 | 0.3921 | +13.52% |

## Pressure Effects

For typical HVAC hydronic system pressures (0-300 psig / 0-2070 kPa gauge), the effect of pressure on thermal conductivity is negligible:

**Pressure correction factor** < 0.5% for ΔP up to 500 psi (3.45 MPa)

This allows designers to use atmospheric pressure values for all practical HVAC calculations without introducing significant error.

**Exception**: High-pressure steam systems and supercritical water applications require pressure-corrected values from ASME Steam Tables or NIST databases.

## Heat Transfer Implications

### Convective Heat Transfer Coefficient

Thermal conductivity directly influences the convective heat transfer coefficient through the Nusselt number relationship:

```
h = (Nu × k) / D_h
```

Where:
- h = convective heat transfer coefficient (W/m²·K or BTU/hr·ft²·°F)
- Nu = Nusselt number (dimensionless)
- k = thermal conductivity (W/m·K or BTU/hr·ft·°F)
- D_h = hydraulic diameter (m or ft)

**Design Impact**: A 13.5% increase in thermal conductivity from 0°C to 100°C translates to a proportional increase in convective coefficient, assuming Reynolds and Prandtl numbers remain constant.

### Overall Heat Transfer Coefficient (U-factor)

For heat exchangers, the overall heat transfer coefficient incorporates thermal conductivity:

```
1/U = 1/h_i + t_wall/k_wall + 1/h_o + R_f,i + R_f,o
```

Where:
- U = overall heat transfer coefficient
- h_i, h_o = inside and outside convective coefficients
- t_wall = wall thickness
- k_wall = wall material thermal conductivity
- R_f = fouling resistance

Since convective coefficients depend on water thermal conductivity, temperature significantly affects U-factor calculations.

## ASHRAE and Reference Standards

### ASHRAE Handbook - Fundamentals

**Chapter 33: Physical Properties of Materials** provides authoritative thermal conductivity data for water and aqueous solutions.

**Reference Values (ASHRAE 2021)**:
- 20°C (68°F): k = 0.598 W/m·K (0.345 BTU/hr·ft·°F)
- Data sourced from IAPWS (International Association for Properties of Water and Steam)

### IAPWS Formulation

The International Association for the Properties of Water and Steam (IAPWS) provides the definitive formulation for thermophysical properties:

**IAPWS-IF97**: Industrial formulation for thermal conductivity
**Uncertainty**: ±1% for temperatures 0-150°C at atmospheric pressure

### NIST Reference Fluid Database

NIST Standard Reference Database 23 (REFPROP) offers high-precision water property calculations:
- Thermal conductivity uncertainty: ±0.5% in liquid region
- Valid to 1000 K and 1000 MPa

## Design Considerations for Heat Exchangers

### Shell-and-Tube Heat Exchangers

Thermal conductivity affects both tube-side and shell-side calculations:

**Tube-side Nusselt correlations** (Gnielinski equation for turbulent flow):

```
Nu = (f/8)(Re - 1000)Pr / [1 + 12.7(f/8)^0.5(Pr^(2/3) - 1)]
```

Where f = friction factor from Moody diagram

The resulting convective coefficient:

```
h = Nu × k / D_i
```

**Temperature consideration**: Use arithmetic mean temperature for k evaluation in counterflow exchangers, or log-mean temperature for complex flow arrangements.

### Plate Heat Exchangers

High turbulence in plate heat exchangers (Re typically 400-5000) enhances heat transfer. Thermal conductivity variations across the temperature profile affect local heat transfer rates:

**Plate correlation** (modified Martin correlation):

```
Nu = C × Re^m × Pr^(1/3) × (μ/μ_wall)^0.14
```

**Design Practice**: Evaluate k at the bulk fluid temperature, then apply wall temperature correction factors.

### Cooling Coils and Chilled Water Systems

For chilled water coils operating at 5-12°C (41-54°F):

- k ≈ 0.571-0.583 W/m·K
- Lower thermal conductivity compared to hot water systems
- Moisture condensation on coil surfaces introduces additional resistance

**Coil design impact**: Lower k values require:
- Increased surface area (more rows)
- Higher water velocities to maintain turbulent flow
- Attention to laminar-to-turbulent transition regions

### Hot Water and Heating Systems

For hot water heating systems operating at 60-85°C (140-185°F):

- k ≈ 0.654-0.673 W/m·K
- Approximately 15% higher than chilled water systems
- Enhanced natural convection effects at elevated temperatures

**Heating coil advantages**:
- Higher thermal conductivity improves heat transfer
- Reduced surface area requirements versus chilled water coils
- Lower pumping energy for equivalent heat transfer

## Glycol Solutions and Thermal Conductivity

Antifreeze solutions commonly used in HVAC systems exhibit significantly lower thermal conductivity than pure water:

### Ethylene Glycol Solutions

| Concentration (% by mass) | k at 20°C (W/m·K) | Reduction vs. Water |
|--------------------------|-------------------|-------------------|
| 0% (pure water) | 0.598 | 0% |
| 10% | 0.560 | -6.4% |
| 20% | 0.524 | -12.4% |
| 30% | 0.490 | -18.1% |
| 40% | 0.458 | -23.4% |
| 50% | 0.428 | -28.4% |

### Propylene Glycol Solutions

| Concentration (% by mass) | k at 20°C (W/m·K) | Reduction vs. Water |
|--------------------------|-------------------|-------------------|
| 0% (pure water) | 0.598 | 0% |
| 10% | 0.552 | -7.7% |
| 20% | 0.511 | -14.5% |
| 30% | 0.473 | -20.9% |
| 40% | 0.438 | -26.8% |
| 50% | 0.406 | -32.1% |

**Design Impact**: Heat exchangers designed for glycol solutions require:
- 20-35% greater surface area for equivalent performance
- Higher pumping energy due to increased viscosity
- Careful consideration of laminar flow regions

## Fouling Effects and Thermal Resistance

While fouling does not change water's intrinsic thermal conductivity, fouling layers add thermal resistance that dominates heat transfer calculations in aged systems:

### Fouling Resistances (TEMA Standards)

| Water Type | Fouling Resistance R_f (m²·K/W) | R_f (hr·ft²·°F/BTU) |
|------------|--------------------------------|-------------------|
| Distilled water | 0.00009 | 0.0005 |
| Treated cooling water | 0.00018 | 0.001 |
| Untreated cooling water | 0.00035 | 0.002 |
| City water (soft) | 0.00018 | 0.001 |
| City water (hard) | 0.00035 | 0.002 |
| Seawater | 0.00009-0.00018 | 0.0005-0.001 |
| River water | 0.00035-0.00053 | 0.002-0.003 |

**Comparison to Water Conductivity**:

For a 1 mm water film: R_water = t/k = 0.001 m / 0.598 W/m·K = 0.00167 m²·K/W

A hard water fouling layer (R_f = 0.00035 m²·K/W) represents approximately 21% of the thermal resistance of a 1 mm water film, illustrating the significance of fouling in long-term performance.

## Computational Considerations

### CFD Modeling

Computational fluid dynamics simulations require accurate thermal conductivity inputs:

**Best Practices**:
- Use temperature-dependent k(T) functions rather than constant values
- For large temperature gradients (ΔT > 20°C), employ local property evaluation
- Validate CFD results against correlations for limiting cases

### Energy Modeling Software

Building energy simulation tools (EnergyPlus, TRACE, HAP) typically use simplified constant-property assumptions:

**Default Values** (typical):
- Chilled water: k = 0.580 W/m·K
- Hot water: k = 0.640 W/m·K
- Condenser water: k = 0.610 W/m·K

**Accuracy Impact**: Constant-property assumptions introduce <2% error for most HVAC applications with moderate temperature ranges (ΔT < 30°C).

## Measurement and Verification

### Laboratory Methods

**Transient Hot-Wire Method** (ASTM D2717):
- Accuracy: ±2%
- Temperature range: -50 to 200°C
- Industry standard for liquids

**Guarded Hot Plate Method** (ASTM C177):
- Lower accuracy for liquids
- Primarily for solids and semi-solids

### Field Verification

Direct measurement of thermal conductivity in operating systems is impractical. Instead, verify heat exchanger performance through:

1. **Inlet/Outlet Temperature Measurements**: Compare measured to predicted performance
2. **Flow Rate Verification**: Confirm design flow rates achieved
3. **Overall U-factor Calculation**: Back-calculate U-factor from measured data
4. **Fouling Assessment**: Trending U-factor degradation over time

## Practical Applications and Examples

### Example 1: Chilled Water Coil Selection

**Given**:
- Entering water temperature: 7°C (44.6°F)
- Leaving water temperature: 12°C (53.6°F)
- Mean water temperature: 9.5°C

**Thermal conductivity at 9.5°C**:
k = 0.5650 + 0.00190(9.5) - 0.00000680(9.5)² = 0.583 W/m·K

**Impact on heat transfer coefficient**:
For identical geometry and flow conditions, a coil designed using k = 0.598 W/m·K (20°C value) would underestimate the actual convective coefficient by:
(0.598 - 0.583)/0.598 = 2.5%

### Example 2: Hot Water Heating System

**Given**:
- Supply temperature: 80°C (176°F)
- Return temperature: 60°C (140°F)
- Mean temperature: 70°C

**Thermal conductivity at 70°C**:
k = 0.663 W/m·K

**Comparison to standard reference** (20°C):
Increase = (0.663 - 0.598)/0.598 = 10.9%

This 11% enhancement in thermal conductivity contributes to improved heat transfer performance, partially offsetting reduced temperature differential in modern low-temperature heating systems.

### Example 3: Counterflow Heat Exchanger

**Configuration**: Hot water cooling from 85°C to 65°C, cold water heating from 15°C to 30°C

**Hot side mean temperature**: 75°C → k_hot = 0.667 W/m·K
**Cold side mean temperature**: 22.5°C → k_cold = 0.604 W/m·K

**Thermal conductivity ratio**: k_hot/k_cold = 1.104

For symmetric geometry with equal flow rates, the hot-side convective coefficient will be approximately 10% higher than the cold side, assuming similar Reynolds numbers. This asymmetry affects optimal flow distribution in complex heat exchanger networks.

## References and Standards

**ASHRAE Handbook - Fundamentals** (2021)
- Chapter 33: Physical Properties of Materials
- Table 1: Properties of Water

**IAPWS Release on Thermal Conductivity of Ordinary Water Substance** (2011)
- International standard for water properties
- Temperature range: 0-800°C, pressure range: 0-400 MPa

**NIST Chemistry WebBook**
- Thermophysical Properties of Fluid Systems
- Free online access to water properties

**TEMA Standards** (Tubular Exchanger Manufacturers Association)
- 10th Edition: Fouling resistances for heat exchanger design

**ASHRAE Standard 90.1**: Energy Standard for Buildings
- Minimum efficiency requirements incorporating heat transfer fundamentals

**ASME Steam Tables** (ASME International Steam Tables)
- Comprehensive water and steam properties to 1000°C and 100 MPa

## Emerging Research and Advanced Topics

### Nanofluids

Recent research explores water-based nanofluids with suspended nanoparticles (Cu, Al₂O₃, TiO₂) achieving thermal conductivity enhancements of 10-40% compared to pure water. While promising for specialized applications, practical HVAC implementation faces challenges:

- Nanoparticle stability and sedimentation
- Pumping energy penalties from increased viscosity
- Long-term fouling and erosion concerns
- Cost-benefit analysis for conventional systems

### Supercritical Water

At pressures above 22.06 MPa and temperatures above 373.95°C, water enters the supercritical region where thermal conductivity exhibits unique behavior. While outside typical HVAC applications, supercritical water heat transfer appears in advanced power generation and industrial processes.

### Temperature-Dependent Design Optimization

Advanced heat exchanger design increasingly incorporates temperature-dependent property evaluation for each control volume, enabled by modern computational tools. This approach yields 2-5% improvements in predicted performance accuracy compared to constant-property assumptions.

## Summary and Design Recommendations

1. **Use temperature-specific values**: For critical applications, evaluate thermal conductivity at actual operating temperatures rather than standard reference conditions

2. **Account for temperature variation**: In systems with large temperature differentials (ΔT > 30°C), consider using mean film temperature for property evaluation

3. **Recognize glycol penalties**: Antifreeze solutions reduce thermal conductivity by 20-35%, requiring proportional increases in heat transfer surface area

4. **Monitor fouling**: Fouling thermal resistance often exceeds the impact of thermal conductivity variations; implement water treatment and periodic cleaning

5. **Leverage higher temperatures**: Hot water systems benefit from enhanced thermal conductivity at elevated temperatures, potentially allowing more compact heat exchangers

6. **Validate assumptions**: For unusual operating conditions or critical applications, verify thermal conductivity values using IAPWS formulations or NIST databases

7. **Consider practical tolerances**: For most conventional HVAC applications, thermal conductivity uncertainties of ±2% are acceptable given larger uncertainties in fouling, flow distribution, and manufacturing tolerances

The thermal conductivity of water, while often treated as a constant in simplified analyses, exhibits meaningful temperature dependence across HVAC operating ranges. Designers who account for these variations produce more accurate equipment selections, particularly for large-capacity systems where small percentage improvements translate to significant energy and cost savings.
