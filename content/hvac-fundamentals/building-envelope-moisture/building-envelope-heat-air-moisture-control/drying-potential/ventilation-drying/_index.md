---
title: "Ventilation Drying"
description: "Ventilation-based drying mechanisms for building envelopes including air change drying, dilution ventilation, moisture removal rates, outdoor air moisture effects, and drying capacity calculations."
weight: 2
---

Ventilation drying removes moisture from building assemblies and spaces through air exchange, replacing humid interior air with drier exterior air or removing moisture-laden air from within assembly cavities. This mechanism typically provides 10-100 times faster moisture removal than diffusion drying, making it the dominant drying pathway for most building envelope moisture problems.

## Air Change Drying

Air change drying quantifies moisture removal through complete air exchange within a space or cavity. Each air change replaces the existing air volume with fresh air at different moisture content. The drying effectiveness depends on the moisture content difference between incoming and outgoing air and the air change rate.

The relationship between air changes and moisture removal follows exponential decay. After n air changes, the remaining moisture concentration approaches: C(n) = C0 × e^(-n) + Ceq × (1 - e^(-n)), where C0 represents initial concentration, Ceq is equilibrium concentration with outdoor air, and n is the number of air changes.

Cavity ventilation provides effective drying when outdoor air has lower moisture content than cavity air. A vented rainscreen cavity receiving 10 air changes per hour can remove substantial moisture, provided the vapor pressure in outdoor air remains below cavity vapor pressure. Seasonal variations in outdoor humidity determine when ventilation drying is effective versus counterproductive.

## Dilution Ventilation

Dilution ventilation reduces space humidity by mixing drier outdoor air with humid interior air. This approach works effectively when outdoor absolute humidity (moisture content per unit mass of dry air) is lower than interior absolute humidity, regardless of relative humidity differences.

The moisture dilution rate follows: dW/dt = Q × ρ × (ωo - ωi), where W is total moisture mass (kg), Q is ventilation rate (m³/s), ρ is air density (kg/m³), ωo is outdoor humidity ratio (kg/kg), and ωi is interior humidity ratio (kg/kg). Positive dW/dt indicates moisture addition, while negative values indicate moisture removal.

During winter in cold climates, outdoor air typically has very low absolute humidity despite high relative humidity. Introducing this air through ventilation effectively dries indoor spaces. Summer conditions in humid climates reverse this relationship, with outdoor air often containing more moisture than conditioned indoor air, making ventilation counterproductive for drying.

## Moisture Removal Rate

Moisture removal rate through ventilation depends on volumetric flow rate and the humidity ratio difference between supply and exhaust air. The mass flow rate of moisture removed equals: m_moisture = Q × ρ × Δω, where Q is airflow rate (m³/s), ρ is air density (≈1.2 kg/m³), and Δω is humidity ratio difference (kg moisture/kg dry air).

For typical residential ventilation at 0.05 m³/s (100 CFM) with Δω = 0.005 kg/kg (winter conditions): m_moisture = 0.05 × 1.2 × 0.005 = 0.0003 kg/s = 26 kg/day. This removal rate dramatically exceeds diffusion drying capacity, which typically ranges 0.01-0.1 kg/m²·day over limited surface areas.

Assembly cavity ventilation achieves even higher area-specific removal rates. A rainscreen cavity with 20 ACH and 25 mm depth removing air with Δω = 0.003 kg/kg achieves approximately 0.7 kg/m²·day moisture removal, 10-70 times greater than diffusion drying.

## Outdoor Air Moisture

Outdoor air moisture content varies dramatically with season, time of day, and weather conditions. The absolute humidity (moisture content) depends on temperature and relative humidity, following: ω ≈ 0.622 × Pv / (Patm - Pv), where Pv is water vapor pressure (Pa) and Patm is atmospheric pressure (Pa).

Cold winter air has inherently low moisture content due to low saturated vapor pressure at cold temperatures. Air at -10°C and 80% RH contains only 1.5 g/kg moisture. When heated to 20°C without moisture addition, this air reaches 11% RH, providing extremely strong drying potential.

Hot humid summer air can contain 15-20 g/kg moisture in humid climates. This moisture-laden air should not be introduced into air-conditioned spaces or assemblies where it will encounter cold surfaces and condense. Ventilation drying only works when outdoor air is drier than the target space or assembly.

Psychrometric analysis determines ventilation drying potential by comparing outdoor and indoor conditions on absolute humidity basis. The drying potential exists when outdoor dew point temperature is lower than indoor dew point temperature, regardless of relative humidity values.

## Drying Capacity Calculation

Ventilation drying capacity calculation requires three parameters: volumetric airflow rate, air density, and humidity ratio difference. The total daily drying capacity equals: Capacity (kg/day) = 86,400 × Q × ρ × (ωi - ωo), where 86,400 converts seconds to days.

For cavity ventilation, the effective ventilation rate depends on cavity geometry, wind pressure, stack effect, and vent opening area. The ventilation rate for a cavity with openings at top and bottom follows: Q = Cd × A × √(2 × ΔP / ρ), where Cd is discharge coefficient (≈0.65), A is opening area (m²), and ΔP is pressure difference (Pa).

Stack effect pressure difference in vertical cavities equals: ΔP = 3,460 × H × (1/To - 1/Ti), where H is cavity height (m), To is outdoor temperature (K), and Ti is cavity temperature (K). A 3-meter cavity with 15°C temperature difference generates approximately 3-4 Pa pressure difference, driving substantial airflow.

## Design Considerations

Effective ventilation drying requires continuous airflow paths through cavities or spaces. Blocked ventilation openings eliminate drying capacity. Insect screens reduce effective opening area by 50-70%, significantly reducing ventilation rates. Design vent openings 2-3 times larger than calculated requirements to account for blockage and uncertainty.

Ventilation paths must allow moisture-laden air to exit while preventing rain entry. Properly designed ventilation openings incorporate overhang protection, baffles, or labyrinth paths. The ventilation opening area should balance drying requirements with water entry risk.

Two-sided ventilation (both inlet and outlet) provides significantly higher airflow than one-sided ventilation. Cross-ventilation utilizing wind pressure differences between windward and leeward surfaces can generate pressure differences of 10-30 Pa, creating robust airflow. Single-sided ventilation relies on much weaker stack effect, achieving 1-5 Pa typical pressure differences.

## Seasonal Effectiveness

Ventilation drying effectiveness varies seasonally with outdoor moisture conditions. Winter typically provides excellent drying conditions in cold climates due to low outdoor absolute humidity. Summer ventilation may humidify rather than dry, particularly in humid climates or when outdoor dew points exceed interior dew points.

Control strategies for mechanical ventilation should respond to outdoor moisture conditions. Humidity-controlled ventilation increases rates when outdoor air is dry and reduces rates when outdoor moisture content is high. Simple dew point comparison between indoor and outdoor air determines when ventilation promotes drying.

Mid-season conditions in swing seasons offer variable drying potential. Spring warming increases outdoor moisture content as temperatures rise, potentially reversing drying effectiveness. Fall cooling generally improves drying as absolute humidity drops with temperature.

## Measurement and Verification

Verification of ventilation drying requires measuring airflow rates and humidity conditions. Airflow measurement in cavities uses tracer gas techniques, velocity traverse methods, or pressure difference measurements with flow coefficient correlations.

Humidity measurements must use absolute humidity (dew point or humidity ratio) rather than relative humidity to evaluate drying potential. Two locations showing identical relative humidity can have vastly different absolute humidity if temperatures differ. Dew point measurements directly indicate moisture content independent of temperature.

Continuous monitoring during drying operations tracks moisture removal rates and identifies when ventilation becomes ineffective. Data logging at 15-60 minute intervals captures diurnal variations in outdoor conditions and assembly response.
