---
title: "Infiltration and Ventilation"
description: "Technical analysis of infiltration air leakage and mechanical ventilation loads including calculation methods, driving forces, and energy recovery strategies."
weight: 3
---

## Infiltration Fundamentals

Infiltration represents uncontrolled air leakage through unintentional openings in the building envelope including cracks around windows and doors, penetrations for utilities and services, and gaps in construction assemblies. The volumetric infiltration rate depends on the magnitude of pressure differences across the envelope and the distribution and size of leakage paths. Pressure differences arise from wind forces, stack effect due to temperature differences, and mechanical system operation creating building pressurization or depressurization.

The sensible heat transfer associated with infiltration equals Q = ρ·V·cp·ΔT, where ρ is air density (0.075 lb/ft³ at standard conditions), V is volumetric infiltration rate (CFM), cp is specific heat (0.24 BTU/lb-°F), and ΔT is the indoor-outdoor temperature difference. This simplifies to Q = 1.08·CFM·ΔT for sensible heat transfer in BTU/hr. The latent heat transfer equals Q = ρ·V·hfg·ΔW = 4840·CFM·ΔW, where hfg is latent heat of vaporization and ΔW is humidity ratio difference in pounds moisture per pound dry air.

## Air Change Method

The air change method estimates infiltration based on building volume and assumed air changes per hour (ACH). The volumetric infiltration rate equals V = (ACH·Volume)/60, converting building volume and air changes to CFM. Typical ACH values range from 0.1-0.5 for tight modern construction to 1.0-2.0 for older buildings with poor envelope sealing.

The air change method provides reasonable accuracy for preliminary estimates but fails to account for actual driving forces or envelope characteristics. Single ACH values cannot represent the wide variation in infiltration rates with changing weather conditions. The method is most applicable to residential buildings where extensive air leakage testing data has established typical ACH ranges for various construction vintages and quality levels.

## Effective Leakage Area Method

The effective leakage area (ELA) method characterizes envelope airtightness by the equivalent area of a sharp-edged orifice that would produce measured airflow at reference pressure. The relationship between airflow and pressure follows Q = C·A·(ΔP)^n, where C is flow coefficient (approximately 0.6 for sharp-edged orifices), A is leakage area, ΔP is pressure difference, and n is flow exponent (0.5-0.7, typically 0.65 for building envelopes).

Blower door testing measures building leakage by depressurizing the building to standard reference pressure (typically 50 Pascals or 0.2 in w.c.) and measuring airflow required to maintain that pressure. The test result expressed as CFM50 converts to effective leakage area using standard correlations. Tight construction achieves leakage rates below 1.5 CFM50 per square foot of envelope area, while conventional construction typically ranges from 3-6 CFM50/ft².

The effective leakage area enables calculation of infiltration rates under actual operating conditions by applying weather-induced and mechanically-induced pressure differences to the leakage distribution. The Lawrence Berkeley Laboratory infiltration model relates ELA to weather parameters including temperature difference, wind speed, and building height to predict time-varying infiltration rates.

## Stack Effect Pressure Distribution

Stack effect pressure differences result from buoyancy forces when indoor air density differs from outdoor air density. Warmer air is less dense and experiences upward buoyant force, creating positive pressure in upper building levels and negative pressure in lower levels. The neutral pressure level (NPL) occurs where indoor and outdoor pressures are equal, typically near the mid-height of the building.

The stack pressure difference at any height relative to the NPL follows ΔPstack = Cs·ρo·g·H·(Ti - To)/To, where Cs is a constant (7.64 for ΔP in Pascals), ρo is outdoor air density, g is gravitational acceleration, H is height above NPL, Ti and To are indoor and outdoor absolute temperatures. A 10-story building with 20°F temperature difference experiences stack pressures approaching 0.3 in w.c. at top and bottom floors.

Stack effect drives substantial infiltration in tall buildings during heating season when indoor temperatures significantly exceed outdoor values. Upper floors experience exfiltration (leakage outward) while lower floors see infiltration of cold outdoor air. The resulting heat loss can dominate envelope thermal transmission losses in cold climates. Compartmentalization strategies including elevator and stair shaft pressurization help control stack-induced air movement.

## Wind-Induced Pressures

Wind impinging on building surfaces creates pressure distributions with positive (windward) and negative (leeward and side) regions. The pressure at any surface point depends on wind speed, building geometry, surrounding terrain, and local surface orientation. Surface pressure coefficients (Cp) quantify pressure relative to reference velocity pressure, with values ranging from +0.8 on windward faces to -0.8 on leeward faces for typical rectangular buildings.

The wind-induced pressure difference driving infiltration equals ΔPwind = 0.5·ρ·V²·Cp, where V is wind speed at building height. A 15 mph wind creates pressure differences of 0.08-0.10 in w.c. on building surfaces. Simultaneous positive windward and negative leeward pressures drive cross-flow infiltration through the building.

Wind effects vary rapidly with changing wind direction and speed, creating highly variable infiltration rates. Sheltering by surrounding buildings and terrain features significantly reduces effective wind speeds and resulting pressures. Computational fluid dynamics (CFD) modeling can predict detailed surface pressure distributions for complex building geometries and site conditions.

## Mechanical System Pressurization Effects

HVAC system operation modifies building pressure relative to outdoors, affecting infiltration rates and distribution. Supply air exceeding return plus exhaust airflow creates positive building pressure, reducing infiltration. Exhaust-dominated systems depressurize buildings, increasing infiltration. The pressure difference induced by system unbalance depends on building envelope tightness, with tighter buildings experiencing larger pressure changes for given airflow imbalances.

Building pressurization of 0.02-0.05 in w.c. relative to outdoors helps control infiltration while avoiding excessive envelope stress or elevator door operation problems. Positive pressurization also prevents backdrafting of combustion appliances and infiltration of soil gases including radon. Pressure-independent demand-controlled ventilation systems must include controlled relief to maintain appropriate building pressure as outdoor air intake varies.

## Ventilation Load Characteristics

Mechanical ventilation provides controlled outdoor air introduction for indoor air quality maintenance and space pressurization. ASHRAE Standard 62.1 specifies minimum ventilation rates based on occupancy density and floor area, with typical office space requirements of 5-7 CFM per person plus area-based component. High-occupancy spaces including classrooms, conference rooms, and assembly areas require higher per-person ventilation rates.

Ventilation loads often exceed envelope transmission and infiltration loads, particularly in high-performance buildings with excellent air sealing and insulation. The ventilation sensible cooling load at design conditions can reach 20-30% of total building load in humid climates, while latent ventilation loads may represent 40-50% of total latent load.

Unlike infiltration, ventilation rates remain relatively constant during occupied periods regardless of outdoor conditions. The resulting energy consumption depends on annual weather patterns and operating schedules rather than peak design conditions. In moderate climates, economizer operation can eliminate ventilation cooling loads during many hours by using outdoor air for free cooling when conditions permit.

## Demand-Controlled Ventilation

Demand-controlled ventilation (DCV) modulates outdoor air intake based on actual occupancy rather than design occupancy. CO₂ sensors measure space concentration as a proxy for occupancy, increasing ventilation when CO₂ rises above setpoint (typically 800-1000 ppm) and reducing flow during low-occupancy periods. Properly implemented DCV reduces ventilation energy consumption by 20-40% in spaces with variable occupancy including conference rooms, auditoriums, and lobbies.

The CO₂ generation rate from occupants ranges from 0.3-0.5 CFH per person depending on activity level. The steady-state CO₂ concentration equals Css = Co + (N·G)/(Q·60), where Co is outdoor CO₂ concentration (approximately 400 ppm), N is number of occupants, G is generation rate per person, and Q is ventilation rate in CFM. A space with 0.4 CFH generation rate requires approximately 15 CFM outdoor air per person to maintain 800 ppm.

DCV effectiveness depends on sensor accuracy, placement, and control algorithms. Sensors require periodic calibration to maintain accuracy. Multiple sensors may be needed in large spaces to capture spatial variations. The ventilation system must respond quickly enough to prevent excessive CO₂ excursions during rapid occupancy increases.

## Energy Recovery Ventilation

Energy recovery ventilators (ERV) and heat recovery ventilators (HRV) reduce ventilation loads by transferring energy between exhaust and outdoor air streams. ERVs transfer both sensible and latent energy through permeable heat exchange cores, while HRVs transfer only sensible heat. Sensible effectiveness of 60-80% and latent effectiveness of 40-60% can reduce annual ventilation energy consumption by 40-60% compared to unrecovered ventilation.

The temperature effectiveness equals εT = (Tsupply - Toutdoor)/(Texhaust - Toutdoor), representing the fraction of available temperature difference recovered. The enthalpy effectiveness similarly characterizes total (sensible plus latent) energy recovery. Higher effectiveness requires larger heat exchanger surface area and lower face velocities, increasing pressure drop and fan energy while improving heat recovery.

Energy recovery economics depend on climate, ventilation rates, and utility costs. Cold climates with high heating costs provide rapid payback, while mild climates may not justify the initial investment. In humid climates, latent heat recovery substantially reduces dehumidification loads and improves economic performance compared to sensible-only recovery.
