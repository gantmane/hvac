---
title: "Water Properties Detailed"
description: "Comprehensive thermophysical properties of water and aqueous solutions for HVAC system design including density, viscosity, thermal conductivity, specific heat, and saturation properties across operating temperatures"
weight: 6
---

Water serves as the primary heat transfer fluid in hydronic HVAC systems. Accurate knowledge of its thermophysical properties is essential for proper sizing of pipes, pumps, heat exchangers, and expansion tanks. Properties vary significantly with temperature, requiring temperature-dependent calculations for precise system design.

## Density and Specific Volume

Water density decreases with increasing temperature due to thermal expansion. This variation affects flow calculations, pump sizing, and expansion tank volume determination.

**Density at atmospheric pressure:**

| Temperature (°F) | Density (lb/ft³) | Specific Volume (ft³/lb) |
|------------------|------------------|--------------------------|
| 32               | 62.42            | 0.01602                  |
| 40               | 62.43            | 0.01602                  |
| 50               | 62.41            | 0.01603                  |
| 60               | 62.37            | 0.01604                  |
| 70               | 62.30            | 0.01605                  |
| 80               | 62.22            | 0.01607                  |
| 90               | 62.11            | 0.01609                  |
| 100              | 62.00            | 0.01613                  |
| 120              | 61.71            | 0.01621                  |
| 140              | 61.38            | 0.01629                  |
| 160              | 61.00            | 0.01639                  |
| 180              | 60.58            | 0.01651                  |
| 200              | 60.13            | 0.01663                  |
| 212              | 59.83            | 0.01672                  |

The density variation from 40°F to 200°F is approximately 4.2%, which directly impacts expansion tank sizing. For systems with temperature swings, calculate expansion volume as:

V_expansion = V_system × (v_hot - v_cold) / v_cold

## Specific Heat Capacity

Specific heat of water remains relatively constant across typical HVAC operating temperatures, varying by less than 0.5% from 40°F to 200°F. This stability simplifies sensible heat transfer calculations.

**Specific heat values:**
- c_p = 1.000 Btu/lb·°F at 60°F (reference)
- c_p = 0.998 Btu/lb·°F at 32°F
- c_p = 1.000 Btu/lb·°F at 100°F
- c_p = 1.007 Btu/lb·°F at 200°F

For hydronic system heat transfer calculations:
Q = ṁ × c_p × ΔT = (ρ × V̇) × c_p × ΔT

The commonly used approximation Q (Btu/hr) = 500 × GPM × ΔT(°F) assumes ρ = 62.3 lb/ft³ and c_p = 1.0 Btu/lb·°F.

## Dynamic Viscosity

Viscosity dramatically affects pressure drop in piping systems and heat exchanger performance. Water viscosity decreases exponentially with increasing temperature, reducing friction losses at higher temperatures.

| Temperature (°F) | Dynamic Viscosity (lb/ft·s × 10⁴) | Kinematic Viscosity (ft²/s × 10⁶) |
|------------------|------------------------------------|------------------------------------|
| 32               | 37.73                              | 18.37                              |
| 40               | 32.71                              | 15.92                              |
| 60               | 23.50                              | 11.44                              |
| 80               | 17.84                              | 8.71                               |
| 100              | 14.13                              | 6.93                               |
| 120              | 11.60                              | 5.71                               |
| 140              | 9.75                               | 4.83                               |
| 160              | 8.37                               | 4.17                               |
| 180              | 7.30                               | 3.66                               |
| 200              | 6.44                               | 3.25                               |

Viscosity reduction from 40°F to 180°F is approximately 78%, explaining the significant pressure drop decrease in heating systems at operating temperature versus startup conditions. Reynolds number calculations for flow regime determination use kinematic viscosity:

Re = V × D / ν

## Thermal Conductivity

Thermal conductivity of water influences convective heat transfer coefficients. The property increases with temperature up to approximately 250°F, then decreases.

| Temperature (°F) | Thermal Conductivity (Btu/hr·ft·°F) |
|------------------|-------------------------------------|
| 32               | 0.319                               |
| 60               | 0.340                               |
| 100              | 0.363                               |
| 140              | 0.379                               |
| 180              | 0.390                               |
| 212              | 0.395                               |

The Prandtl number (Pr = μc_p/k) characterizes the relative thickness of velocity and thermal boundary layers, critical for Nusselt number correlations in heat exchanger design.

## Vapor Pressure and Saturation Properties

Water vapor pressure determines the minimum system pressure required to prevent cavitation in pumps and flashing in low-pressure zones. Saturation pressure increases exponentially with temperature.

| Temperature (°F) | Saturation Pressure (psia) | Enthalpy of Vaporization (Btu/lb) |
|------------------|----------------------------|-----------------------------------|
| 60               | 0.256                      | 1059.6                            |
| 80               | 0.507                      | 1048.3                            |
| 100              | 0.949                      | 1037.0                            |
| 120              | 1.692                      | 1025.4                            |
| 140              | 2.888                      | 1013.4                            |
| 160              | 4.741                      | 1000.9                            |
| 180              | 7.510                      | 987.8                             |
| 200              | 11.526                     | 974.0                             |
| 212              | 14.696                     | 970.3                             |

System pressure must exceed saturation pressure plus pump NPSH requirements to prevent cavitation. For closed systems, pressurization maintains pressure above saturation at the highest temperature point.

## Glycol Solutions

Ethylene glycol and propylene glycol additions depress freezing point but degrade heat transfer performance. Property changes are concentration-dependent.

**Property multipliers for 30% propylene glycol by volume:**
- Density: 1.03× water
- Specific heat: 0.94× water
- Viscosity: 2.5× water at 40°F, 1.7× water at 100°F
- Thermal conductivity: 0.88× water

**Freezing point depression (propylene glycol):**
- 20% solution: +20°F freeze point
- 30% solution: +7°F freeze point
- 40% solution: -8°F freeze point
- 50% solution: -26°F freeze point

The heat transfer capacity penalty for glycol solutions requires increased flow rates:
GPM_glycol = GPM_water × (c_p,water / c_p,glycol)

Pressure drop increases substantially due to elevated viscosity, particularly at low temperatures. Friction loss multipliers range from 1.3 to 2.8 depending on concentration and temperature.

## Temperature-Dependent Pressure Drop

Pressure drop calculations must account for temperature-dependent viscosity when system temperatures vary significantly. The Darcy-Weisbach equation shows friction factor depends on Reynolds number, which is viscosity-dependent:

Δp = f × (L/D) × (ρV²/2)

For turbulent flow, the Colebrook equation relates friction factor to Reynolds number and relative roughness. The viscosity term in Reynolds number means identical flow rates produce different pressure drops at different temperatures.

**Example pressure drop multipliers (reference to 60°F):**
- At 40°F: 1.35× pressure drop
- At 100°F: 0.62× pressure drop
- At 180°F: 0.33× pressure drop

This effect explains why chilled water systems experience higher pressure drops than heating water systems at equivalent flow rates and pipe sizes.

## Compressibility and Bulk Modulus

Water exhibits minimal compressibility under typical HVAC pressures, justifying the incompressible flow assumption for hydraulic calculations. The bulk modulus of water at 60°F is approximately 320,000 psi, meaning a 100 psi pressure increase produces only 0.03% volume reduction.

This near-incompressibility has important implications:
- Water hammer pressure surges propagate at approximately 4,000 ft/s
- Pressure changes transmit essentially instantaneously throughout systems
- Expansion tanks must accommodate thermal expansion, not compression
- Pump curves are flow-dependent, not pressure-dependent

## Enthalpy and Sensible Heat

For liquid water below saturation, enthalpy is calculated from specific heat:
h = c_p × T (reference to 32°F)

The sensible heat equation for hydronic systems:
Q = ṁ × Δh ≈ ṁ × c_p × ΔT

At typical HVAC temperatures, the approximation h (Btu/lb) ≈ T(°F) - 32 introduces less than 1% error, simplifying hand calculations.

ASHRAE Fundamentals provides complete thermophysical property tables for water, steam, and aqueous solutions across the full range of HVAC operating conditions.
