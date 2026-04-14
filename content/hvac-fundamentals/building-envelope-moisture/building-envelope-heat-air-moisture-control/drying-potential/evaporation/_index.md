---
title: "Evaporation"
aliases: ["Evaporation"]
description: "Evaporation processes in building envelope drying including surface evaporation rates, vapor pressure deficit effects, temperature and air velocity influences on moisture removal."
weight: 1
---

Evaporation represents the phase change of liquid water to water vapor at material surfaces, constituting the fundamental moisture removal mechanism in building envelope drying. This process occurs when the vapor pressure at the wet surface exceeds the vapor pressure of the adjacent air, enabling net moisture transfer from the material to the surrounding environment.

## Surface Evaporation Rate

Surface evaporation rate quantifies the mass of water converted to vapor per unit area per unit time, typically expressed in kg/m²·h or g/m²·day. The evaporation rate depends on the vapor pressure difference between the saturated surface and ambient air, surface area, air velocity, and temperature.

The basic evaporation equation follows: E = hm × (Ps - Pa), where E is evaporation rate (kg/m²·s), hm represents the mass transfer coefficient (kg/m²·s·Pa), Ps is saturated vapor pressure at the surface temperature (Pa), and Pa is ambient vapor pressure (Pa).

The mass transfer coefficient increases with air velocity following boundary layer theory. Typical values range from 0.01-0.10 kg/m²·s·Pa depending on air movement conditions. Forced convection through mechanical ventilation dramatically increases mass transfer coefficients compared to natural convection.

## Vapor Pressure Deficit

Vapor pressure deficit (VPD) represents the driving force for evaporation, defined as the difference between saturated vapor pressure at the surface temperature and the actual vapor pressure in ambient air. Greater VPD produces higher evaporation rates, providing stronger drying potential.

VPD varies with temperature and relative humidity. At 20°C, 50% RH air has VPD = 1,170 Pa (saturated vapor pressure 2,340 Pa minus ambient 1,170 Pa). Increasing temperature to 30°C at constant 50% RH increases VPD to 2,120 Pa, nearly doubling drying potential.

Cold surfaces exhibit reduced VPD even with low relative humidity air. A surface at 5°C has saturated vapor pressure of only 872 Pa. Air at 20°C and 50% RH (vapor pressure 1,170 Pa) would cause condensation rather than evaporation at this cold surface, demonstrating the critical importance of surface temperature in determining evaporation direction.

## Temperature Effects

Temperature influences evaporation through multiple mechanisms: saturated vapor pressure increases exponentially with temperature, molecular diffusion rates increase, and air's moisture-holding capacity expands. The Clausius-Clapeyron equation describes the exponential relationship between temperature and saturated vapor pressure.

Saturated vapor pressure approximately doubles with each 10°C temperature increase in typical building temperature ranges. This exponential relationship makes temperature the most powerful variable affecting evaporation potential. Heating wet materials or providing warm air dramatically accelerates drying rates.

Surface temperature determines whether evaporation or condensation occurs. Evaporation requires surface temperature above the dew point temperature of ambient air. The temperature gradient within materials affects internal moisture redistribution, with moisture migrating toward colder regions through vapor diffusion and potentially condensing at cold surfaces.

## Air Velocity Effects

Air velocity at the evaporating surface controls boundary layer resistance, directly affecting mass transfer coefficient and evaporation rate. Higher air velocities reduce boundary layer thickness, decrease vapor concentration at the surface, and increase evaporation rate.

The relationship between air velocity and evaporation rate follows: hm ∝ v^0.8, where v represents air velocity (m/s). Doubling air velocity increases evaporation rate by approximately 75%. This strong velocity dependence makes forced air movement essential for effective drying operations.

Stagnant air conditions create thick boundary layers where vapor accumulates near the evaporating surface, reducing vapor pressure deficit and limiting evaporation. Natural convection provides minimal air movement (0.05-0.2 m/s), while mechanical ventilation can achieve 0.5-5 m/s, increasing evaporation rates by factors of 5-10.

## Evaporative Drying

Evaporative drying represents the complete process of removing moisture from building materials through evaporation and vapor transport. The process involves three sequential resistances: internal liquid/vapor transport to the surface, phase change at the surface, and vapor removal from the surface.

The controlling resistance shifts as drying progresses. Initially, surface evaporation controls the rate when materials are very wet. As moisture content decreases, internal moisture transport becomes controlling. In the final drying stage, very low moisture content limits internal transport, resulting in extremely slow drying rates.

## Engineering Calculations

The drying time for building materials depends on initial moisture content, equilibrium moisture content, evaporation rate, and material thickness. For thin materials where surface evaporation controls: t = ρ × L × (Mi - Me) / E, where t is drying time (s), ρ is material density (kg/m³), L is thickness (m), Mi is initial moisture content (kg/kg), Me is equilibrium moisture content (kg/kg), and E is evaporation rate (kg/m²·s).

Thick materials exhibit extended drying times due to internal moisture transport resistance. Diffusion coefficient within the material becomes the limiting factor. Wood products demonstrate characteristic drying times proportional to thickness squared, following: t ∝ L²/D, where D represents effective moisture diffusivity (m²/s).

## Latent Heat Considerations

Evaporation requires substantial energy input as latent heat of vaporization, approximately 2,450 kJ/kg for water at 20°C. This energy demand causes evaporative cooling, reducing surface temperature and decreasing evaporation rate unless heat is continuously supplied.

Evaporating 1 kg of water requires energy equivalent to heating 580 kg of water by 1°C. Building materials undergoing evaporative drying can experience temperature depressions of 5-10°C below ambient temperature, reducing vapor pressure deficit and self-limiting evaporation rate.

Heating systems supporting drying operations must supply both sensible heat to maintain air temperature and latent heat to sustain evaporation. The total drying energy demand often exceeds steady-state heating loads by factors of 2-5 during aggressive drying operations.

## Practical Applications

Effective drying strategies maximize evaporation rate through combined interventions: heating to increase surface temperature and vapor pressure, dehumidification to maintain low ambient vapor pressure and high VPD, and air movement to reduce boundary layer resistance. These three factors synergistically enhance drying beyond individual effects.

Drying wet building assemblies requires access to evaporating surfaces through cavity ventilation or material removal. Trapped moisture within assemblies cannot evaporate without vapor transport paths to interior or exterior environments. Ventilation drying through cavity air changes enables evaporation followed by vapor removal.
