---
title: "Phase Change Heat Transfer"
description: "Phase change convection fundamentals for HVAC including boiling and condensation mechanisms, nucleate and film boiling regimes, two-phase flow in evaporators and condensers, and heat transfer coefficient correlations for refrigerant phase transitions."
weight: 3
---

Phase change heat transfer represents the most efficient convective heat transfer mechanism in HVAC systems, occurring in evaporators, condensers, boilers, and cooling towers. The absorption or release of latent heat during phase transitions enables extremely high heat transfer coefficients, typically 5-50 times greater than single-phase convection.

## Boiling Heat Transfer

Boiling is the liquid-to-vapor phase change that occurs when liquid temperature reaches the saturation temperature at system pressure. This process dominates heat transfer in evaporators of refrigeration systems, chillers, and steam boilers.

### Pool Boiling Regimes

Pool boiling describes phase change when a heated surface is submerged in stagnant liquid. The heat flux varies dramatically with surface superheat (ΔT<sub>e</sub> = T<sub>wall</sub> - T<sub>sat</sub>):

**Free Convection (ΔT<sub>e</sub> < 5°C):** Single-phase natural convection dominates before bubble formation. Heat transfer coefficient: h = 50-500 W/m²·K.

**Nucleate Boiling (5°C < ΔT<sub>e</sub> < 30°C):** Bubbles form at nucleation sites on the surface and rise through the liquid. This is the most desirable regime for HVAC equipment, providing the highest heat transfer coefficients.

**Transition Boiling (30°C < ΔT<sub>e</sub> < 120°C):** Unstable regime where vapor film partially covers the surface. Heat flux decreases as superheat increases—an unstable operating condition avoided in HVAC design.

**Film Boiling (ΔT<sub>e</sub> > 120°C):** Stable vapor film blankets the surface, drastically reducing heat transfer. This regime never occurs in properly designed refrigeration systems but may develop during abnormal conditions.

### Nucleate Boiling Correlations

The Rohsenow correlation predicts nucleate boiling heat flux:

q" = μ<sub>l</sub> h<sub>fg</sub> [g(ρ<sub>l</sub> - ρ<sub>v</sub>)/σ]<sup>0.5</sup> [(c<sub>p,l</sub> ΔT<sub>e</sub>)/(C<sub>sf</sub> h<sub>fg</sub> Pr<sub>l</sub><sup>n</sup>)]<sup>3</sup>

Where:
- μ<sub>l</sub> = liquid dynamic viscosity
- h<sub>fg</sub> = latent heat of vaporization
- g = gravitational acceleration
- ρ<sub>l</sub>, ρ<sub>v</sub> = liquid and vapor densities
- σ = surface tension
- c<sub>p,l</sub> = liquid specific heat
- C<sub>sf</sub> = surface-fluid constant (0.006-0.015 for most HVAC fluids)
- Pr<sub>l</sub> = liquid Prandtl number
- n = exponent (typically 1.0 for water, 1.7 for refrigerants)

For engineering calculations, the Cooper correlation provides simpler nucleate boiling estimates:

h = 55 P<sub>r</sub><sup>0.12</sup> (-log<sub>10</sub> P<sub>r</sub>)<sup>-0.55</sup> M<sup>-0.5</sup> q"<sup>0.67</sup>

Where P<sub>r</sub> = P/P<sub>crit</sub> (reduced pressure) and M = molecular weight.

### Flow Boiling in Evaporators

Flow boiling occurs in refrigerant evaporators where liquid flows through tubes while absorbing heat. The process involves complex two-phase flow patterns:

**Bubbly Flow (x < 0.05):** Discrete bubbles in continuous liquid phase. Heat transfer coefficient similar to single-phase liquid convection.

**Slug Flow (0.05 < x < 0.25):** Large vapor slugs separate liquid plugs. Intermittent surface wetting creates periodic heat transfer variations.

**Annular Flow (0.25 < x < 0.95):** Liquid film on tube wall with vapor core. This regime provides the highest evaporator heat transfer coefficients. Most DX evaporators operate in this region.

**Mist Flow (x > 0.95):** Liquid droplets entrained in vapor. Heat transfer deteriorates as surface dries out—requires adequate refrigerant feed control.

The Chen correlation combines nucleate and convective boiling contributions:

h<sub>tp</sub> = h<sub>nb</sub> S + h<sub>conv</sub> F

Where h<sub>nb</sub> is nucleate boiling component, h<sub>conv</sub> is convective component, S is suppression factor, and F is enhancement factor accounting for two-phase effects.

## Condensation Heat Transfer

Condensation transfers heat when vapor cools below saturation temperature, releasing latent heat as liquid forms on surfaces. This process governs heat rejection in condensers, cooling towers, and dehumidification coils.

### Film Condensation

Film condensation produces a continuous liquid film on cooled surfaces—the dominant mechanism in HVAC condensers. The Nusselt theory for laminar film condensation on vertical surfaces provides:

h = 0.943 [ρ<sub>l</sub>(ρ<sub>l</sub> - ρ<sub>v</sub>) g k<sub>l</sub><sup>3</sup> h<sub>fg</sub>/(μ<sub>l</sub> L ΔT)]<sup>0.25</sup>

For vertical surfaces of height L with temperature difference ΔT = T<sub>sat</sub> - T<sub>wall</sub>.

For horizontal tubes (diameter D), the correlation becomes:

h = 0.725 [ρ<sub>l</sub>(ρ<sub>l</sub> - ρ<sub>v</sub>) g k<sub>l</sub><sup>3</sup> h<sub>fg</sub>/(μ<sub>l</sub> D ΔT)]<sup>0.25</sup>

For horizontal tube banks with N tubes in vertical column, the average coefficient reduces due to condensate drainage from upper tubes:

h<sub>N</sub> = h<sub>1</sub> / N<sup>0.25</sup>

### Dropwise Condensation

Dropwise condensation occurs when condensate forms discrete droplets that roll off the surface rather than forming a continuous film. Heat transfer coefficients reach 5-10 times film condensation values due to minimal thermal resistance. However, dropwise condensation rarely persists in HVAC equipment due to surface contamination and oxidation.

Promoting coatings or surface treatments can sustain dropwise condensation, but practical HVAC designs assume film condensation for conservative performance predictions.

### Condensation in Horizontal Tubes

Flow condensation inside horizontal tubes involves stratified flow patterns where gravity drains condensate to the bottom. The Shah correlation predicts condensing heat transfer coefficients:

h<sub>tp</sub>/h<sub>l</sub> = [(1-x)<sup>0.8</sup> + (3.8 x<sup>0.76</sup> (1-x)<sup>0.04</sup>)/P<sub>r</sub><sup>0.38</sup>]

Where h<sub>l</sub> is the liquid-phase heat transfer coefficient and x is vapor quality.

For microchannel condensers common in modern HVAC equipment, enhanced correlations account for surface tension effects and reduced tube diameters.

## Heat Transfer Coefficient Comparison

| Heat Transfer Mode | Typical h Range (W/m²·K) | Application |
|-------------------|-------------------------|-------------|
| Free convection (air) | 5-25 | Natural draft cooling |
| Forced convection (air) | 25-250 | Air-cooled condensers |
| Forced convection (water) | 500-10,000 | Water-cooled equipment |
| Nucleate boiling | 2,500-100,000 | Evaporators, chillers |
| Film condensation | 5,000-100,000 | Condensers, cooling towers |
| Dropwise condensation | 50,000-250,000 | Specialized surfaces |

## Two-Phase Flow Parameters

Understanding two-phase flow requires tracking several key parameters:

**Vapor Quality (x):** Mass fraction of vapor in two-phase mixture, ranging from x = 0 (saturated liquid) to x = 1 (saturated vapor).

**Void Fraction (α):** Volume fraction occupied by vapor phase. Due to density differences, void fraction exceeds vapor quality (α > x) throughout evaporators and condensers.

**Flow Regime:** Geometric distribution of phases determines heat transfer and pressure drop. HVAC equipment typically operates in annular flow for highest performance.

**Heat Flux (q"):** Heat transfer rate per unit area. Evaporators typically operate at 5-15 kW/m² while condensers handle 8-20 kW/m².

## Refrigerant Phase Change Properties

| Refrigerant | h<sub>fg</sub> at 5°C (kJ/kg) | ρ<sub>l</sub>/ρ<sub>v</sub> | σ (mN/m) | Typical h (kW/m²·K) |
|-------------|-------------------------------|----------------------------|----------|-------------------|
| R-134a | 198.6 | 82 | 10.5 | 2.5-4.5 (evap) / 3.5-6.0 (cond) |
| R-410A | 252.9 | 98 | 8.2 | 3.0-5.5 (evap) / 4.0-7.5 (cond) |
| R-32 | 327.5 | 118 | 10.8 | 3.5-6.5 (evap) / 4.5-8.5 (cond) |
| R-744 (CO₂) | 194.7 | 8 | 2.5 | 5.0-12.0 (gas cooler, transcritical) |
| Ammonia (R-717) | 1297.6 | 135 | 32.5 | 4.0-8.0 (evap) / 5.0-10.0 (cond) |

## Critical Heat Flux

The critical heat flux (CHF) represents the maximum heat transfer rate in nucleate boiling before transition to film boiling. The Zuber correlation for pool boiling provides:

q"<sub>max</sub> = 0.149 ρ<sub>v</sub> h<sub>fg</sub> [σ g (ρ<sub>l</sub> - ρ<sub>v</sub>)/ρ<sub>v</sub><sup>2</sup>]<sup>0.25</sup>

HVAC evaporators operate at heat fluxes 10-30% of CHF to ensure stable nucleate boiling and prevent localized overheating that would damage compressors with superheated, oil-depleted vapor.

## Enhancement Techniques

Modern HVAC equipment employs surface enhancements to increase phase change heat transfer:

**Microfin Tubes:** Helical internal fins in condenser and evaporator tubes increase surface area 1.5-2.5 times while promoting turbulence. Heat transfer enhancement reaches 50-150% over smooth tubes.

**Porous Coatings:** Sintered or electroplated porous surfaces increase nucleation site density, enhancing nucleate boiling by 100-300%.

**Surface Geometry:** Three-dimensional enhanced surfaces (dimples, protrusions, re-entrant cavities) trap vapor nuclei and sustain boiling at lower superheats.

**Twisted Tape Inserts:** Induce swirl flow to prevent stratification in horizontal condensing tubes, maintaining annular flow and uniform heat transfer.

These enhancements must balance increased heat transfer against elevated pressure drop, requiring optimization for specific HVAC applications and refrigerant properties.

## Practical Design Considerations

Phase change heat transfer in HVAC systems requires attention to several practical factors:

**Refrigerant Charge:** Insufficient charge causes premature evaporator dryout and loss of heat transfer. Overcharge floods the condenser, reducing effective surface area.

**Superheat Control:** Maintains annular flow throughout the evaporator while ensuring liquid-free compressor suction. Typical settings: 4-7°C for thermostatic expansion valves, 2-4°C for electronic expansion valves.

**Subcooling:** Ensures liquid refrigerant to expansion devices while maximizing condenser heat rejection. Standard subcooling: 3-6°C for air-cooled systems, 5-10°C for water-cooled systems.

**Oil Return:** Two-phase flow must maintain sufficient velocity (>3-5 m/s vapor velocity) to entrain oil droplets and return lubricant to the compressor.

**Non-Condensables:** Air and other gases accumulate in condensers, blanketing surfaces and reducing heat transfer coefficients by 20-50%. Purging systems remove these gases in large chillers.

Understanding phase change heat transfer mechanisms enables proper sizing of evaporators and condensers, selection of appropriate refrigerants, and optimization of operating conditions for maximum HVAC system efficiency and capacity.
