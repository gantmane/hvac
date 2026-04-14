---
title: "Concentration Effects"
aliases: ["Concentration Effects"]
description: "Impact of glycol concentration on freeze point, viscosity, specific heat, thermal conductivity, and system performance including optimal concentration selection for HVAC applications."
weight: 3
---

Glycol concentration profoundly affects both freeze protection and thermal-hydraulic performance. The concentration selection process balances adequate freeze protection against performance degradation, pumping power penalties, and heat exchanger sizing impacts.

## Freeze Point Depression Curves

Freeze point depression follows nonlinear concentration relationships documented in ASHRAE Fundamentals Chapter 31. The freeze point decreases with increasing concentration until reaching a eutectic minimum, beyond which further concentration increases the freeze point.

**Propylene glycol concentration-freeze point relationship:**

| Concentration (% by weight) | Freeze Point (°C) | Freeze Point (°F) |
|----------------------------|-------------------|-------------------|
| 10% | -4 | 25 |
| 20% | -9 | 16 |
| 30% | -16 | 3 |
| 40% | -24 | -12 |
| 50% | -34 | -29 |
| 60% | -52 | -62 |

**Ethylene glycol exhibits similar but slightly lower freeze points at equivalent concentrations.**

The freeze point represents onset of ice crystal formation. Slush formation occurs over a temperature range, with complete solidification requiring significantly lower temperatures than the tabulated freeze point.

## Eutectic Composition

The eutectic point represents the lowest achievable freeze point for the glycol-water system. At eutectic concentration, solution and ice crystals form simultaneously during freezing.

**Propylene glycol eutectic:** 60% by weight at approximately -60°C (-76°F). Concentrations above 60% provide less freeze protection due to the -59°C freezing point of pure propylene glycol.

**Ethylene glycol eutectic:** 60% by weight at approximately -52°C (-62°F). Pure ethylene glycol freezes at -13°C (9°F), limiting utility of high concentrations.

Practical HVAC systems rarely approach eutectic concentration. Most applications use 20-40% solutions balancing adequate freeze protection (typically -10 to -25°C) against thermal performance degradation.

## Specific Heat Capacity Reduction

Specific heat capacity decreases approximately linearly with glycol concentration, directly impacting system flow rate requirements.

**Propylene glycol specific heat at 20°C:**

| Concentration | cp [kJ/(kg·K)] | cp [Btu/(lb·°F)] | Relative to Water |
|--------------|----------------|------------------|-------------------|
| 0% (water) | 4.18 | 1.00 | 100% |
| 20% | 3.98 | 0.95 | 95% |
| 30% | 3.85 | 0.92 | 92% |
| 40% | 3.72 | 0.89 | 89% |
| 50% | 3.52 | 0.84 | 84% |

The flow rate increase required to maintain capacity follows:

ṁ_glycol / ṁ_water = cp_water / cp_glycol

A 40% propylene glycol solution requires 12% higher flow rate than water for equivalent heat transfer capacity. This increased flow rate propagates through the entire system, affecting:
- Pipe sizing for equivalent velocity
- Pump selection and power consumption
- Heat exchanger effectiveness
- Temperature differences across loads

## Viscosity Increase with Concentration

Viscosity increases dramatically with glycol concentration, exhibiting exponential temperature dependence per the Arrhenius relationship:

μ = A · exp(B/T)

where A and B are empirical constants varying with concentration.

**Propylene glycol dynamic viscosity at 20°C:**

| Concentration | μ (cP) | μ (Pa·s) | Relative to Water |
|--------------|--------|----------|-------------------|
| 0% (water) | 1.0 | 0.001 | 1.0× |
| 20% | 1.9 | 0.0019 | 1.9× |
| 30% | 2.8 | 0.0028 | 2.8× |
| 40% | 4.3 | 0.0043 | 4.3× |
| 50% | 7.0 | 0.0070 | 7.0× |

Viscosity effects compound at low temperatures. A 40% propylene glycol solution at -10°C exhibits viscosity approaching 30 cP—30 times that of water at room temperature.

**Pressure drop implications:**

Pressure drop in turbulent flow scales with viscosity per the Darcy-Weisbach equation:

∆P = f · (L/D) · (ρV²/2)

where friction factor f depends on Reynolds number Re = ρVD/μ. Higher viscosity reduces Re, increasing friction factor and pressure drop. The combined effect increases pressure drop by factors of 1.5-4× compared to water at equivalent flow rates.

Laminar flow (Re < 2300) becomes more likely in small diameter pipes with glycol solutions. Laminar flow exhibits f = 64/Re, making pressure drop directly proportional to viscosity with ∆P ∝ μV.

## Thermal Conductivity Degradation

Thermal conductivity decreases with glycol concentration, reducing convective heat transfer coefficients in heat exchangers:

**Propylene glycol thermal conductivity at 20°C:**

| Concentration | k [W/(m·K)] | k [Btu/(h·ft·°F)] | Relative to Water |
|--------------|-------------|-------------------|-------------------|
| 0% (water) | 0.598 | 0.346 | 100% |
| 20% | 0.510 | 0.295 | 85% |
| 30% | 0.470 | 0.272 | 79% |
| 40% | 0.435 | 0.252 | 73% |
| 50% | 0.395 | 0.228 | 66% |

Reduced thermal conductivity affects the Prandtl number:

Pr = cpμ/k

Prandtl number increases with glycol concentration (water Pr ≈ 7, glycol solutions Pr ≈ 20-100), reducing convective heat transfer coefficients per correlations like Dittus-Boelter:

Nu = 0.023 Re^0.8 Pr^0.4

The net effect reduces heat transfer coefficients by 20-40% compared to water, requiring 25-60% additional heat exchanger surface area for equivalent performance.

## Density Effects

Density increases approximately linearly with glycol concentration:

**Propylene glycol density at 20°C:**

| Concentration | ρ (kg/m³) | ρ (lb/ft³) | Relative to Water |
|--------------|-----------|------------|-------------------|
| 0% (water) | 998 | 62.3 | 100% |
| 20% | 1015 | 63.4 | 102% |
| 30% | 1023 | 63.9 | 103% |
| 40% | 1032 | 64.4 | 103% |
| 50% | 1041 | 65.0 | 104% |

Higher density slightly increases pump head requirements for equivalent system elevation changes. The density increase is small compared to viscosity and specific heat effects.

## Prandtl Number and Heat Transfer

Prandtl number Pr = cpμ/k represents the ratio of momentum diffusivity to thermal diffusivity. Glycol solutions exhibit higher Prandtl numbers than water due to increased viscosity and reduced thermal conductivity:

**Propylene glycol Prandtl number at 20°C:**

| Concentration | Prandtl Number | Heat Transfer Impact |
|--------------|----------------|----------------------|
| 0% (water) | 7 | Baseline (h = 1.0) |
| 20% | 15 | h ≈ 0.85 |
| 30% | 23 | h ≈ 0.75 |
| 40% | 37 | h ≈ 0.65 |
| 50% | 62 | h ≈ 0.55 |

Higher Prandtl numbers indicate thicker thermal boundary layers relative to velocity boundary layers, reducing convective heat transfer coefficients. The Pr^0.4 dependency in turbulent flow correlations means a 5× increase in Prandtl number reduces heat transfer coefficient by approximately 35%.

## Optimal Concentration Selection

Optimal concentration balances competing objectives:

**Minimum concentration requirement:**
- Freeze point < minimum system temperature - 10°F safety margin
- Account for stagnant areas, shutdown conditions, cold spots

**Performance penalties above minimum:**
- 10% concentration increase → 2% specific heat reduction
- 10% concentration increase → 30-50% viscosity increase
- 10% concentration increase → 5% thermal conductivity reduction
- Combined effect: 5-10% heat transfer coefficient reduction per 10% concentration

**Economic optimization:**
The lifecycle cost optimum typically occurs at minimum concentration satisfying freeze protection requirements plus a safety margin. Over-concentration increases:
- Initial heat exchanger capital cost (larger required area)
- Pumping energy cost (higher viscosity, higher flow rate)
- Fluid replacement cost (more expensive fluid volume)

## Pumping Power Increase

Pumping power follows:

P_pump = (ṁ · ∆P) / (ρ · η_pump)

For glycol solutions versus water at equivalent capacity:
- ṁ increases by (cp_water/cp_glycol) factor due to reduced specific heat
- ∆P increases by 1.5-4× due to combined viscosity and flow rate effects
- Net pumping power increases by 1.8-5× for 30-40% glycol solutions

This parasitic power penalty persists throughout system operating life, making minimum adequate concentration economically optimal.

## Over-Concentration Disadvantages

Concentrations exceeding freeze protection requirements impose penalties without benefits:

**Performance degradation:** Exponentially increasing viscosity reduces heat transfer and increases pressure drop.

**Economic waste:** Glycol costs $3-8/gallon. Excess concentration adds unnecessary fluid cost.

**Freeze protection reversal:** Concentrations above eutectic (60%) actually reduce freeze protection.

**Inhibitor depletion:** Higher glycol concentrations accelerate inhibitor consumption in some formulations.

**Operational difficulties:** Very viscous solutions (50%+) exhibit difficult cold-start behavior, require oversized pumps, and may cause flow measurement errors.

Best practice specifies concentration providing required freeze protection plus 10-15°F safety margin, avoiding over-concentration beyond this requirement.
