---
title: "Refrigerant Mixtures"
description: "Comprehensive analysis of refrigerant mixture thermodynamics including zeotropic and azeotropic blends, temperature glide, fractionation effects, and mixture property calculations for HVAC applications."
weight: 9
---

Refrigerant mixtures combine two or more pure refrigerants to achieve performance characteristics, environmental properties, or safety profiles unattainable with single-component fluids. Understanding mixture thermodynamics is fundamental for system design, charging procedures, and leak management.

## Mixture Classification

Refrigerant blends are classified based on their phase equilibrium behavior during evaporation and condensation.

### Zeotropic Mixtures

Zeotropic blends exhibit temperature glide during phase change processes. Components have different volatilities, causing the mixture composition to change as evaporation or condensation progresses.

**Characteristics:**
- Non-constant temperature during phase change at constant pressure
- Composition shift between liquid and vapor phases (fractionation)
- Temperature glide typically 2-10°F (1-6°C)
- Require careful charging and leak management procedures

**Common zeotropic refrigerants:**
- R-407C (R-32/125/134a: 23/25/52% mass)
- R-410A (R-32/125: 50/50% mass, near-azeotropic)
- R-407A (R-32/125/134a: 20/40/40% mass)
- R-404A (R-125/143a/134a: 44/52/4% mass, near-azeotropic)

### Azeotropic Mixtures

Azeotropic blends behave as single-component refrigerants during phase change at specific compositions. The liquid and vapor phases maintain identical compositions throughout evaporation and condensation.

**Characteristics:**
- Constant temperature during phase change (like pure refrigerants)
- No composition shift between phases
- Zero temperature glide
- Can be charged as liquid or vapor without fractionation concerns

**Common azeotropic refrigerants:**
- R-507A (R-125/143a: 50/50% mass, true azeotrope)
- R-500 (R-12/152a: 73.8/26.2% mass, obsolete)
- R-502 (R-22/115: 48.8/51.2% mass, obsolete)

### Near-Azeotropic Mixtures

These blends exhibit minimal temperature glide (typically <1°F or 0.5°C) and behave nearly as azeotropes for practical applications. R-410A is the most significant near-azeotropic refrigerant in modern HVAC systems.

## Temperature Glide Fundamentals

Temperature glide is the temperature difference between the bubble point (saturation liquid) and dew point (saturation vapor) at constant pressure.

### Physical Mechanism

During evaporation of a zeotropic mixture:
1. More volatile components vaporize preferentially at lower temperatures
2. Liquid becomes progressively enriched in less volatile components
3. Evaporation temperature increases as composition shifts
4. Total temperature change equals the glide magnitude

### Glide Magnitude Factors

Temperature glide magnitude depends on:
- Component volatility differences (vapor pressure differential)
- Mixture composition (mass fractions)
- Operating pressure (higher pressure = lower glide)
- Non-ideal thermodynamic interactions

| Refrigerant | Composition (mass %) | Glide at 40°F | Glide at 100°F |
|-------------|---------------------|---------------|----------------|
| R-407C | R-32/125/134a (23/25/52) | 11°F (6.1°C) | 8°F (4.4°C) |
| R-407A | R-32/125/134a (20/40/40) | 9°F (5.0°C) | 7°F (3.9°C) |
| R-404A | R-125/143a/134a (44/52/4) | 1°F (0.6°C) | 0.7°F (0.4°C) |
| R-410A | R-32/125 (50/50) | 0.3°F (0.2°C) | 0.2°F (0.1°C) |
| R-417A | R-125/134a/600 (46.6/50/3.4) | 9°F (5.0°C) | 7°F (3.9°C) |

### Impact on Heat Transfer

Temperature glide affects heat exchanger performance:
- **Evaporator:** Refrigerant temperature increases during evaporation, reducing temperature difference with heat source
- **Condenser:** Refrigerant temperature decreases during condensation, reducing temperature difference with heat sink
- **Net effect:** Counterflow heat exchangers can utilize glide beneficially when temperature profiles match
- **Design consideration:** Mean temperature difference must account for variable refrigerant temperature

## Fractionation Phenomena

Fractionation is the separation of mixture components due to preferential phase change, resulting in composition shift.

### Leak-Induced Fractionation

When vapor leaks from a system containing zeotropic refrigerant:
- More volatile components escape preferentially
- Remaining charge becomes enriched in less volatile components
- System capacity and efficiency degrade
- Measured pressures no longer correspond to original mixture properties

**Consequence:** Liquid-phase charging is mandatory for zeotropic blends to maintain proper composition.

### Charge Loss Sensitivity

| Refrigerant | Vapor Leak Impact | Recommended Action |
|-------------|-------------------|-------------------|
| R-407C | High sensitivity | Remove remaining charge, recharge with liquid |
| R-410A | Very low sensitivity | Top-off acceptable for small leaks |
| R-404A | Low sensitivity | Top-off acceptable for small leaks |
| R-407A | High sensitivity | Remove remaining charge, recharge with liquid |

### Accumulator Fractionation

In systems with accumulators or liquid receivers:
- Composition can differ between liquid and vapor spaces
- Extended off-cycles allow equilibration
- Startup transients may show temporary composition variation
- Proper oil management prevents concentration of one component in oil

## Mixture Property Calculations

Thermodynamic properties of refrigerant mixtures cannot be determined by simple averaging of pure component properties due to non-ideal behavior.

### Equation of State Approach

Accurate property calculations require:
- Multi-component equation of state (Martin-Hou, Peng-Robinson, or REFPROP)
- Binary interaction parameters for component pairs
- Fugacity coefficient calculations for phase equilibrium
- Iterative solution for saturation conditions

### Bubble Point and Dew Point

At a given pressure, the mixture exhibits two saturation temperatures:
- **Bubble point (T_bubble):** Temperature at which first vapor bubble forms
- **Dew point (T_dew):** Temperature at which first liquid droplet forms
- **Glide:** ΔT = T_dew - T_bubble

### Enthalpy Calculations

For a zeotropic mixture at two-phase conditions:
- Enthalpy is NOT uniquely determined by temperature and pressure alone
- Quality (vapor mass fraction) must be specified
- Composition varies with quality
- Energy balance calculations must track composition changes

**Critical design implication:** Standard superheat and subcooling measurements require dew point and bubble point references, not single saturation temperatures.

## Practical Charging Considerations

### Liquid Charging Requirements

For zeotropic mixtures:
1. Always charge from liquid port of cylinder
2. Use charging device with liquid valve or invert cylinder (check manufacturer guidance)
3. Subcool charged liquid to prevent flashing
4. Never top-off with vapor after significant leak

### Composition Verification

After charging or leak repair:
- Pressure-temperature measurements may not confirm correct charge
- Superheat/subcooling measurements require glide-adjusted saturation references
- Consider chemical analysis for critical applications
- Manufacturers provide P-T-composition charts for verification

## System Performance Optimization

### Matching Glide to Application

Temperature glide can be advantageous when:
- Heat source or sink has large temperature change (counterflow arrangement)
- Water-source heat pumps with high ΔT across coils
- Process cooling with significant fluid temperature rise

Temperature glide is disadvantageous when:
- Constant temperature heat source/sink (air systems)
- Cross-flow or parallel-flow heat exchanger arrangements
- Precise temperature control requirements

### Retrofit Considerations

When retrofitting systems to mixture refrigerants:
- Verify compatibility with system materials and lubricants
- Recalculate heat exchanger performance accounting for glide
- Adjust expansion device sizing for different pressure-enthalpy characteristics
- Update pressure-temperature charts and service documentation
- Retrain service personnel on liquid charging requirements

## Regulatory and Safety Classification

ASHRAE Standard 34 assigns refrigerant blends:
- 400-series designations for zeotropic mixtures
- 500-series designations for azeotropic mixtures
- Safety classifications (A1, A2L, etc.) based on composite mixture properties
- Composition tolerances (typically ±2% mass for each component)

Understanding refrigerant mixture thermodynamics is essential for proper system design, accurate performance prediction, and correct service procedures. The temperature glide and fractionation characteristics of zeotropic blends require careful attention to charging methods and leak management protocols to maintain system performance and efficiency.
