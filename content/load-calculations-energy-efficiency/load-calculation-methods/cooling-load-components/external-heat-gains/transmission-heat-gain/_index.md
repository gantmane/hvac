---
title: "Transmission Heat Gain"
description: "Engineering analysis of conductive heat transfer through building envelope components including walls, roofs, floors, and thermal bridging effects on cooling loads."
weight: 2
---

## Fundamental Heat Transfer Theory

Transmission heat gain through opaque building envelope assemblies results from conductive heat transfer driven by temperature differences between indoor and outdoor environments. The heat flux follows Fourier's law, q = -kA(dT/dx), where k represents material thermal conductivity, A is surface area, and dT/dx is the temperature gradient perpendicular to the surface. For steady-state conditions through multilayer assemblies, the overall heat transfer rate simplifies to Q = UA(To - Ti), where U is the overall heat transfer coefficient.

The U-factor consolidates thermal resistances of all material layers plus interior and exterior surface film coefficients. Each material layer contributes thermal resistance R = L/k, where L is thickness and k is thermal conductivity. Surface film resistances account for convective and radiative heat transfer at interior and exterior surfaces. Standard ASHRAE surface resistances are 0.68 hr-ft²-°F/BTU for interior vertical surfaces and 0.25 hr-ft²-°F/BTU for exterior surfaces at 15 mph wind speed.

## Sol-Air Temperature Application

For opaque surfaces exposed to solar radiation, the sol-air temperature provides an equivalent outdoor air temperature that accounts for both convective heat transfer and absorbed solar radiation. The sol-air temperature equation is:

Tsol-air = To + (α·I/ho) - (ε·ΔR/ho)

where To is outdoor air temperature, α is solar absorptance, I is incident solar radiation, ho is exterior heat transfer coefficient, ε is surface emittance, and ΔR represents net longwave radiation exchange with sky and surroundings.

Solar absorptance ranges from 0.3-0.4 for light-colored surfaces to 0.8-0.95 for dark surfaces. The absorbed solar radiation term elevates sol-air temperature substantially above air temperature during daytime hours. A dark roof surface receiving 250 BTU/hr-ft² solar radiation experiences sol-air temperature approximately 50°F above outdoor air temperature. Cool roof coatings with solar reflectance above 0.65 reduce sol-air temperature by 25-35°F compared to conventional dark surfaces.

## Roof Heat Gain Characteristics

Roof assemblies typically experience the highest transmission heat gains due to horizontal orientation maximizing solar exposure and minimal shading. Peak roof heat gains occur 2-4 hours after solar noon due to thermal mass effects in roof construction. Lightweight metal roof systems exhibit minimal time lag while heavyweight concrete roof decks delay peak heat gain by 4-6 hours.

Roof insulation location significantly impacts heat gain characteristics. Insulation above the roof deck (protected membrane roof or PMRA) maintains the structural deck near indoor temperature, minimizing thermal stress and preserving waterproofing membrane life. Below-deck insulation allows the roof deck to reach high temperatures, potentially degrading roofing materials and increasing cooling loads if insulation is damaged or incomplete.

Ventilated attic spaces in residential construction provide an intermediate zone between outdoor conditions and ceiling insulation. Attic ventilation reduces summer cooling loads by exhausting solar heat gains before conduction through ceiling insulation. Recommended attic ventilation rates of 1 square foot net free area per 150 square feet floor area maintain attic temperatures 5-15°F below unvented configurations.

## Wall Heat Transfer Considerations

Wall heat gains depend on orientation, solar exposure, and thermal properties. South-facing walls in northern hemisphere receive maximum solar radiation during winter months when sun angles are low but minimal exposure during summer with high sun angles. East and west walls experience peak gains during morning and afternoon respectively, contributing to cooling loads during occupied periods.

Thermal mass in wall assemblies delays and attenuates heat gains similar to roof effects. Massive masonry or concrete walls with exterior insulation provide decrement factors of 0.1-0.3, meaning interior surface temperature swing is only 10-30% of exterior temperature swing. Lightweight frame walls with minimal thermal mass provide little attenuation benefit.

Thermal bridging through steel or wood studs creates parallel heat flow paths with significantly lower resistance than insulated cavities. Steel studs reduce overall assembly thermal resistance by 40-50% compared to cavity insulation alone due to high thermal conductivity of steel. Continuous exterior insulation or thermal breaks in framing minimize bridging effects and improve overall wall performance.

## Below-Grade Heat Transfer

Below-grade walls and slabs on grade exchange heat with soil rather than outdoor air. Ground temperature varies seasonally with amplitude decreasing and phase lag increasing with depth. Annual average ground temperature approximates mean annual air temperature. At depths below 15-20 feet, temperature remains essentially constant year-round.

Heat flow to ground follows three-dimensional paths from conditioned space through foundation walls and floor slabs, then through soil to the surface. Simplified calculation methods use equivalent U-factors and temperature differences, but accuracy improves with two-dimensional finite element analysis accounting for actual geometry and soil properties.

Below-grade spaces typically experience net heat loss rather than heat gain in most climates since deep ground temperature remains below heating setpoint. Cooling loads occur only in hot climates where ground temperature exceeds indoor setpoint or in summer months with minimal below-grade depth. Foundation insulation placement (exterior vs. interior vs. under slab) significantly impacts heat flow patterns and required insulation levels.

## Thermal Bridge Analysis

Thermal bridges represent localized areas of higher heat flow due to discontinuous insulation or high-conductivity materials penetrating envelope assemblies. Common thermal bridges include window and door frames, concrete balcony slabs, steel shelf angles supporting brick veneer, and steel framing members in wall assemblies.

The linear transmittance or psi-value (ψ) quantifies excess heat flow through thermal bridges beyond one-dimensional heat transfer. Total heat flow through a bridged assembly equals Q = UA(To - Ti) + ψL(To - Ti), where ψ is linear transmittance and L is the length of thermal bridge. Thermal bridge contributions can increase overall envelope heat transfer by 15-30% compared to clear wall sections.

Infrared thermography reveals thermal bridges as cold spots during heating season or hot spots during cooling season. Temperature differences exceeding 5-8°F indicate significant thermal bridging requiring mitigation. Thermal break materials with low conductivity interrupt heat flow paths through structural elements, reducing ψ-values by 50-80%.

## Window and Door Frame Conduction

Fenestration frames contribute significantly to overall window U-factor due to higher conductivity than insulated glazing units. Aluminum frames without thermal breaks conduct heat readily, with frame U-factors exceeding 1.0 BTU/hr-ft²-°F. Thermally broken aluminum, fiberglass, and vinyl frames reduce frame U-factors to 0.3-0.5 range. Wood and vinyl frames provide best thermal performance with U-factors below 0.3.

The frame fraction of total window area ranges from 15-30% depending on window size and configuration. Small windows with divided lites have higher frame fractions and correspondingly higher overall U-factors. Proper window U-factor calculation requires area-weighted averaging of center-of-glass, edge-of-glass, and frame U-factors according to NFRC procedures.

## Material Property Variations

Thermal conductivity of building materials varies with temperature, moisture content, and aging. Insulation materials experience degradation in thermal resistance due to moisture absorption, settling, and gas diffusion from closed-cell foams. Design calculations should use aged thermal properties rather than initial values to ensure long-term performance.

Moisture increases effective thermal conductivity substantially. Wet insulation loses 50-70% of thermal resistance compared to dry conditions. Vapor retarders and proper drainage design prevent moisture accumulation that degrades insulation performance and envelope durability.

## Dynamic Heat Transfer Effects

Transient heat transfer through building envelope involves thermal storage in addition to conduction. The periodic heat flow varies sinusoidally with 24-hour period for daily temperature swings. Thermal mass dampens and delays heat flow according to material properties and thickness.

The decrement factor quantifies amplitude reduction while the time lag measures phase shift between exterior and interior temperature swings. Heavy mass walls (concrete, masonry) achieve decrement factors of 0.1-0.3 and time lags of 8-12 hours. Lightweight construction shows decrement factors near 1.0 and minimal time lag.
