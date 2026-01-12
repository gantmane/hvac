---
title: "Air Properties Detailed"
description: "Comprehensive air thermophysical properties for HVAC engineering including density, viscosity, thermal conductivity, specific heat, and Prandtl number as functions of temperature with calculation equations and property tables"
weight: 7
---

Air serves as the primary heat transfer medium in most HVAC systems. Accurate knowledge of air thermophysical properties enables precise calculation of heat transfer rates, pressure drops, flow velocities, and energy consumption. These properties vary significantly with temperature and, to a lesser extent, with pressure and humidity.

## Standard Air Conditions

HVAC calculations reference standard air conditions to establish baseline performance metrics and enable equipment comparisons.

**ASHRAE Standard Air:**
- Temperature: 20°C (68°F)
- Pressure: 101.325 kPa (14.696 psia, 29.92 in Hg)
- Density: 1.204 kg/m³ (0.0752 lb/ft³)
- Relative humidity: 0% (dry air)

**Standard Atmosphere (Sea Level):**
- Temperature: 15°C (59°F)
- Pressure: 101.325 kPa (14.696 psia)
- Density: 1.225 kg/m³ (0.0765 lb/ft³)

Equipment ratings typically reference ASHRAE standard air. Performance at actual conditions requires density corrections using the affinity laws for fans and psychrometric adjustments for cooling coils.

## Ideal Gas Behavior

Dry air behaves as an ideal gas across the temperature and pressure ranges encountered in HVAC applications. The ideal gas law relates pressure, temperature, and density:

**Equation of State:**

ρ = P / (R × T)

Where:
- ρ = density (kg/m³)
- P = absolute pressure (Pa)
- R = specific gas constant for dry air = 287.05 J/(kg·K)
- T = absolute temperature (K)

**Alternative Form:**

P × V = m × R × T

This relationship enables density calculation at any pressure and temperature combination, critical for fan selection at non-standard conditions and high-altitude applications.

## Deviations from Ideal Gas Behavior

Air exhibits ideal gas behavior to within 0.1% accuracy at atmospheric pressure across the temperature range -40°C to 100°C. Deviations become significant only at:

- Pressures exceeding 10 MPa (1450 psi)
- Temperatures below -100°C (-148°F)
- Near saturation conditions with high humidity

Standard HVAC applications fall well within the ideal gas regime. Compressed air systems operating above 1 MPa may require compressibility factor corrections.

## Density

Air density decreases with increasing temperature at constant pressure due to thermal expansion. Density directly affects:

- Fan static pressure generation (proportional to ρ)
- Duct friction losses (proportional to ρ)
- Heat transfer rates (ρ appears in convection correlations)
- Airflow measurement (velocity pressure = 0.5 × ρ × V²)

**Density at Atmospheric Pressure (101.325 kPa):**

| Temperature (°C) | Temperature (°F) | Density (kg/m³) | Density (lb/ft³) |
|------------------|------------------|-----------------|------------------|
| -40 | -40 | 1.514 | 0.0945 |
| -20 | -4 | 1.395 | 0.0871 |
| 0 | 32 | 1.293 | 0.0807 |
| 10 | 50 | 1.247 | 0.0779 |
| 20 | 68 | 1.204 | 0.0752 |
| 30 | 86 | 1.165 | 0.0727 |
| 40 | 104 | 1.128 | 0.0704 |
| 50 | 122 | 1.093 | 0.0682 |
| 60 | 140 | 1.060 | 0.0662 |
| 70 | 158 | 1.029 | 0.0642 |
| 80 | 176 | 1.000 | 0.0624 |
| 90 | 194 | 0.972 | 0.0607 |
| 100 | 212 | 0.946 | 0.0590 |

Density decreases approximately 0.35% per °C temperature increase near room temperature. A 20°C temperature rise reduces density by about 7%, directly reducing fan capacity by the same percentage at constant speed.

## Dynamic Viscosity

Dynamic viscosity (absolute viscosity) quantifies air's resistance to shear deformation. Viscosity increases with temperature for gases due to increased molecular kinetic energy and collision frequency, opposite to the behavior of liquids.

**Dynamic Viscosity at Atmospheric Pressure:**

| Temperature (°C) | Temperature (°F) | Viscosity (μPa·s) | Viscosity (lb/(ft·h)) |
|------------------|------------------|-------------------|------------------------|
| -40 | -40 | 15.2 | 0.0368 |
| -20 | -4 | 16.2 | 0.0392 |
| 0 | 32 | 17.2 | 0.0416 |
| 10 | 50 | 17.6 | 0.0426 |
| 20 | 68 | 18.1 | 0.0438 |
| 30 | 86 | 18.6 | 0.0450 |
| 40 | 104 | 19.1 | 0.0462 |
| 50 | 122 | 19.6 | 0.0474 |
| 60 | 140 | 20.1 | 0.0486 |
| 70 | 158 | 20.6 | 0.0498 |
| 80 | 176 | 21.1 | 0.0510 |
| 90 | 194 | 21.5 | 0.0520 |
| 100 | 212 | 22.0 | 0.0532 |

**Sutherland's Formula** provides accurate viscosity calculation across wide temperature ranges:

μ = μ₀ × (T / T₀)^(3/2) × [(T₀ + S) / (T + S)]

Where:
- μ = dynamic viscosity at temperature T (Pa·s)
- μ₀ = reference viscosity = 1.716 × 10⁻⁵ Pa·s at T₀ = 273.15 K
- S = Sutherland's constant for air = 110.4 K
- T = absolute temperature (K)

Viscosity affects duct friction losses, boundary layer development, and heat transfer coefficients through the Reynolds number.

## Kinematic Viscosity

Kinematic viscosity represents the ratio of dynamic viscosity to density:

ν = μ / ρ

Where:
- ν = kinematic viscosity (m²/s)
- μ = dynamic viscosity (Pa·s)
- ρ = density (kg/m³)

Kinematic viscosity appears directly in Reynolds number calculations for airflow analysis. Unlike dynamic viscosity, kinematic viscosity increases significantly with temperature due to the combined effects of increasing μ and decreasing ρ.

**Kinematic Viscosity at Atmospheric Pressure:**

| Temperature (°C) | Kinematic Viscosity (m²/s × 10⁶) |
|------------------|-----------------------------------|
| 0 | 13.3 |
| 20 | 15.1 |
| 40 | 16.9 |
| 60 | 18.9 |
| 80 | 21.1 |
| 100 | 23.3 |

## Thermal Conductivity

Thermal conductivity quantifies air's ability to conduct heat. Air has low thermal conductivity, making it an effective insulator when stationary but requiring convection for effective heat transfer.

**Thermal Conductivity at Atmospheric Pressure:**

| Temperature (°C) | Temperature (°F) | Conductivity (W/(m·K)) | Conductivity (Btu/(h·ft·°F)) |
|------------------|------------------|------------------------|-------------------------------|
| -40 | -40 | 0.0209 | 0.0121 |
| -20 | -4 | 0.0223 | 0.0129 |
| 0 | 32 | 0.0237 | 0.0137 |
| 10 | 50 | 0.0244 | 0.0141 |
| 20 | 68 | 0.0251 | 0.0145 |
| 30 | 86 | 0.0258 | 0.0149 |
| 40 | 104 | 0.0265 | 0.0153 |
| 50 | 122 | 0.0272 | 0.0157 |
| 60 | 140 | 0.0279 | 0.0161 |
| 70 | 158 | 0.0286 | 0.0165 |
| 80 | 176 | 0.0293 | 0.0169 |
| 90 | 194 | 0.0300 | 0.0173 |
| 100 | 212 | 0.0307 | 0.0177 |

Thermal conductivity increases approximately 0.3% per °C. This variation is small compared to convection effects, which dominate heat transfer in forced air systems.

## Specific Heat Capacity

Specific heat at constant pressure (cₚ) represents the energy required to raise air temperature by one degree. This property determines sensible heating and cooling loads.

**Specific Heat at Constant Pressure:**

| Temperature (°C) | Temperature (°F) | cₚ (J/(kg·K)) | cₚ (Btu/(lb·°F)) |
|------------------|------------------|---------------|------------------|
| -40 | -40 | 1005 | 0.240 |
| -20 | -4 | 1005 | 0.240 |
| 0 | 32 | 1005 | 0.240 |
| 20 | 68 | 1005 | 0.240 |
| 40 | 104 | 1005 | 0.240 |
| 60 | 140 | 1009 | 0.241 |
| 80 | 176 | 1009 | 0.241 |
| 100 | 212 | 1009 | 0.241 |

Specific heat remains essentially constant at 1005 J/(kg·K) or 0.240 Btu/(lb·°F) across HVAC temperature ranges. This constancy simplifies sensible heat calculations:

Q = ṁ × cₚ × ΔT = 1.005 × ṁ × ΔT (kW, with ṁ in kg/s, ΔT in K)

Or in IP units:

Q = 60 × ṁ × cₚ × ΔT = 1.08 × CFM × ΔT (Btu/h, with ΔT in °F)

The factor 1.08 derives from: 60 min/h × 0.075 lb/ft³ × 0.240 Btu/(lb·°F) = 1.08.

## Prandtl Number

The Prandtl number represents the ratio of momentum diffusivity to thermal diffusivity:

Pr = (μ × cₚ) / k

Where:
- Pr = Prandtl number (dimensionless)
- μ = dynamic viscosity (Pa·s)
- cₚ = specific heat at constant pressure (J/(kg·K))
- k = thermal conductivity (W/(m·K))

**Prandtl Number for Air:**

| Temperature (°C) | Prandtl Number |
|------------------|----------------|
| 0 | 0.72 |
| 20 | 0.71 |
| 40 | 0.71 |
| 60 | 0.71 |
| 80 | 0.71 |
| 100 | 0.70 |

The Prandtl number remains nearly constant at 0.71 for air across HVAC temperature ranges. This value indicates that momentum and thermal boundary layers develop at similar rates. The constancy of Pr simplifies convection heat transfer correlations, which often take the form:

Nu = f(Re, Pr)

For air, Pr^n terms in these correlations become constants.

## Temperature-Dependent Property Correlations

For computerized calculations, polynomial correlations provide accurate property values:

**Density (kg/m³) at 101.325 kPa:**

ρ = 101325 / (287.05 × (T + 273.15))

**Dynamic Viscosity (Pa·s):**

μ = 1.716 × 10⁻⁵ × ((T + 273.15) / 273.15)^1.5 × (383.55 / (T + 383.55))

**Thermal Conductivity (W/(m·K)):**

k = 2.4 × 10⁻⁵ + 7.6 × 10⁻⁵ × (T / 100)

Where T is temperature in °C. These correlations provide accuracy within 1% across -40°C to 100°C.

## Humidity Effects on Air Properties

Water vapor presence modifies air properties. Moist air density decreases with increasing humidity because water vapor (molecular weight 18) is lighter than dry air (molecular weight 28.97).

**Moist Air Density:**

ρ_moist = (P_dry / (R_air × T)) + (P_vapor / (R_vapor × T))

Or using humidity ratio W (kg water/kg dry air):

ρ_moist = ρ_dry / (1 + 1.608 × W)

At 50% RH and 25°C, humidity reduces density by approximately 0.6%. This effect becomes significant in precise psychrometric calculations.

**Moist Air Specific Heat:**

cₚ_moist = cₚ_air + W × cₚ_vapor = 1.005 + 1.88 × W (kJ/(kg·K))

Humidity increases specific heat, raising the energy required for sensible temperature changes.

## Altitude Corrections

Atmospheric pressure decreases with altitude, directly affecting air density:

ρ_altitude = ρ_sea_level × (P_altitude / P_sea_level)

**Approximate pressure at altitude:**

P = 101.325 × (1 - 2.256 × 10⁻⁵ × h)^5.256 (kPa)

Where h = altitude in meters above sea level.

At 1500 m (4920 ft) elevation, pressure drops to 84.6 kPa, reducing density by 16.5%. Fan performance, heat transfer rates, and airflow measurement all require altitude corrections.

## Application to HVAC Calculations

Air properties directly impact fundamental HVAC design calculations:

**Reynolds Number:**

Re = (ρ × V × D) / μ = (V × D) / ν

Determines flow regime (laminar, transitional, turbulent) affecting friction factors and heat transfer coefficients.

**Friction Factor (Turbulent Flow):**

Pressure drop calculations require density and viscosity through Reynolds number and Darcy-Weisbach equation.

**Convection Heat Transfer:**

h = (Nu × k) / L

Nusselt number correlations depend on Reynolds and Prandtl numbers, incorporating μ, ρ, cₚ, and k.

**Psychrometric Processes:**

All sensible and latent heat calculations require accurate density and specific heat values at actual operating conditions.

Proper accounting for temperature-dependent air properties ensures accurate system performance prediction, appropriate equipment selection, and energy consumption estimation.
