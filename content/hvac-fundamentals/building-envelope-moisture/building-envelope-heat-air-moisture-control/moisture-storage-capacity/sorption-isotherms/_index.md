---
title: "Sorption Isotherms"
description: "Sorption isotherm characteristics in building materials including adsorption and desorption curves, hysteresis effects, temperature dependence, and material-specific moisture storage relationships."
weight: 3
---

Sorption isotherms quantify the relationship between material moisture content and ambient relative humidity at constant temperature, defining equilibrium moisture storage characteristics fundamental to hygrothermal analysis. These curves govern moisture buffering, storage capacity, and moisture-dependent material properties in building envelope assemblies.

## Sorption Curves

Sorption curves plot equilibrium moisture content (typically mass percent or kg/kg) versus relative humidity (0-100%) at constant temperature. These curves characterize how materials absorb or release moisture to maintain equilibrium with surrounding air humidity. The curve shape depends on material pore structure, chemical composition, and surface characteristics.

Most building materials exhibit Type II isotherms in the Brunauer classification system, showing gradual moisture uptake at low RH, steeper increase in mid-range RH (40-80%), and asymptotic approach to saturation near 100% RH. The inflection point typically occurs at 40-60% RH, representing transition from monolayer to multilayer adsorption.

Mathematical models describe sorption behavior including the GAB (Guggenheim-Anderson-de Boer) equation: M = (Mm × C × K × φ) / [(1 - K × φ) × (1 - K × φ + C × K × φ)], where M is moisture content, Mm is monolayer moisture content, C and K are material constants, and φ is relative humidity (decimal). This three-parameter model accurately represents most building material isotherms.

The BET (Brunauer-Emmett-Teller) equation provides simpler two-parameter representation: M = (Mm × C × φ) / [(1 - φ) × (1 - φ + C × φ)], effective for relative humidity below 50% but less accurate at higher humidity levels.

## Adsorption Isotherms

Adsorption isotherms describe moisture uptake when initially dry material is exposed to increasing relative humidity. These curves represent material behavior during wetting processes, typical of seasonal humidity increases or moisture exposure events.

The adsorption process involves multiple mechanisms: monolayer adsorption at low RH where water molecules attach to hygroscopic sites on material surfaces, multilayer adsorption at moderate RH building water molecule layers, and capillary condensation at high RH where water condenses in material pores due to reduced vapor pressure from surface tension effects.

Adsorption rate depends on relative humidity, temperature, and material diffusion characteristics. Initial adsorption occurs rapidly (hours to days for thin materials), while thick materials require weeks to months to achieve equilibrium due to internal diffusion limitations.

## Desorption Isotherms

Desorption isotherms characterize moisture release when saturated material is exposed to decreasing relative humidity. These curves represent drying behavior, typically lying above corresponding adsorption curves due to hysteresis effects.

The desorption process reverses moisture storage mechanisms: capillary water drains from larger pores at high RH, multilayer water evaporates at moderate RH, and strongly bound water releases at low RH. Complete desorption to zero moisture content typically requires relative humidity below 5-10%.

Desorption rates generally exceed adsorption rates for the same humidity difference. This asymmetry results from different transport mechanisms: desorption involves both liquid water transport and vapor diffusion, while adsorption relies primarily on vapor diffusion.

## Hysteresis Effects

Hysteresis describes the phenomenon where adsorption and desorption isotherms follow different paths, with desorption curves consistently above adsorption curves at equivalent relative humidity. This means materials retain more moisture during drying than they absorb during wetting at the same RH.

The hysteresis magnitude varies by material, typically ranging 1-5% moisture content difference between adsorption and desorption at 50-80% RH. Wood products exhibit substantial hysteresis (2-4% difference), while concrete shows moderate effects (1-2% difference). Hysteresis results from pore geometry effects, contact angle differences, and molecular arrangement.

Engineering implications of hysteresis include: moisture content predictions must account for moisture history (wetting vs. drying), material properties (thermal conductivity, strength) depend on whether material is in adsorption or desorption state, and cyclic humidity exposure leads to scanning curves between primary adsorption and desorption curves.

Scanning curves represent partial cycles between main isotherms. A material undergoing adsorption that reverses before saturation follows a scanning curve toward the desorption isotherm. Repeated cycling creates complex moisture content histories requiring detailed modeling.

## Temperature Effects

Temperature significantly affects sorption isotherms, with moisture content at constant relative humidity decreasing as temperature increases. This temperature dependence follows thermodynamic relationships, with moisture content change approximately 0.5-2% per 10°C temperature increase at constant RH.

The temperature effect results from entropic factors: higher temperature increases molecular kinetic energy, reducing binding energy effectiveness and lowering equilibrium moisture content. The relationship follows: ln(φ) = ΔH/(R×T) + const, where ΔH is heat of sorption, R is gas constant, and T is absolute temperature.

Sorption isotherms must be measured or specified at defined temperature, typically 20°C or 23°C for building materials. Applying isotherms at significantly different temperatures introduces errors in moisture content prediction. Temperature correction factors enable approximate conversion between temperatures when specific isotherm data is unavailable.

Practical implications include seasonal moisture content variation even at constant RH due to temperature changes, higher summer temperatures reducing equilibrium moisture content compared to winter conditions, and material testing requiring temperature control for reproducible results.

## Material Specific Curves

Different materials exhibit characteristic isotherm shapes reflecting their hygroscopic nature. Wood products show steep isotherms with fiber saturation point near 28-30% moisture content at 95-99% RH. Gypsum board demonstrates moderate hygroscopicity with 1-2% moisture content at 50% RH. Concrete and masonry show variable isotherms depending on composition and porosity.

Non-hygroscopic materials like plastics, metals, and glass exhibit effectively zero moisture storage except for surface condensation above 100% RH (supersaturated conditions). These materials do not participate in moisture buffering but can transport liquid water through capillarity or gravity.

Composite materials exhibit complex isotherms reflecting weighted contributions from constituent materials. Faced insulation boards combine hygroscopic facers with non-hygroscopic foam cores, creating isotherms dominated by facing materials but with reduced total storage due to foam volume.

## Engineering Applications

Sorption isotherms enable quantitative moisture analysis including: calculation of equilibrium moisture content for specified environmental conditions, prediction of moisture storage and buffering capacity, evaluation of moisture-dependent thermal conductivity and other properties, and input data for hygrothermal simulation tools.

Standard test methods for determining sorption isotherms include ASTM C1498 for hygroscopic sorption properties and ISO 12571 for moisture sorption curves. These methods use controlled humidity chambers with salt solutions or humidity generators to establish specific RH levels.

Database resources provide measured isotherms for common building materials. The WUFI database, Fraunhofer IBP materials database, and ASHRAE Handbook of Fundamentals contain extensive isotherm data. Material-specific testing is required for novel materials or critical applications where generic data is insufficient.
