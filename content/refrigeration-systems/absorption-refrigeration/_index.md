---
title: "Absorption Refrigeration"
aliases: ["Absorption Refrigeration"]
weight: 2
description: "Comprehensive technical guide to absorption refrigeration systems, including LiBr-water and ammonia-water cycles, COP calculations, and waste heat cooling applications for HVAC professionals."
---

Absorption refrigeration systems provide cooling through thermal energy input rather than mechanical compression, making them particularly valuable for applications with available waste heat, solar thermal energy, or direct-fired heat sources. Unlike vapor compression systems that require high-grade electrical energy for compressor operation, absorption chillers utilize low-grade thermal energy to drive the refrigeration cycle, offering significant operational advantages in specific applications.

## Fundamental Operating Principles

The absorption refrigeration cycle replaces the mechanical compressor with a thermal compressor consisting of an absorber, solution pump, and generator. The refrigerant vapor from the evaporator is absorbed into a solution at low pressure, pumped to high pressure as a liquid solution (requiring minimal work input), then released from the solution in the generator through heat addition. This process accomplishes the same pressure rise as mechanical compression but uses thermal energy as the primary input.

The cycle operates on four main pressure levels corresponding to four key components: evaporator (low pressure, low temperature), absorber (low pressure, moderate temperature), generator (high pressure, high temperature), and condenser (high pressure, moderate temperature). The refrigerant flows through the evaporator-absorber-generator-condenser path, while the absorbent solution circulates between the absorber and generator.

Key working fluid pairs must satisfy specific requirements: the refrigerant must have high volatility relative to the absorbent, the pair must exhibit strong affinity (high solubility), and the mixture must remain chemically stable across the operating temperature range. Two dominant working fluid combinations dominate commercial absorption refrigeration applications.

## Lithium Bromide-Water Systems

Lithium bromide-water (LiBr-H₂O) absorption chillers use water as the refrigerant and lithium bromide salt solution as the absorbent. This combination provides excellent thermodynamic properties for air conditioning applications but limits the minimum evaporator temperature to approximately 4°C (39°F) due to water's freezing point. The system operates under vacuum conditions, with evaporator pressures typically ranging from 0.7 to 1.2 kPa absolute.

In the generator, heat input (typically 80-150°C supply temperature) drives water vapor from the concentrated LiBr solution. The water vapor flows to the condenser where it releases heat and condenses at approximately 35-40°C. The condensed water passes through an expansion device into the evaporator, where it absorbs heat from the chilled water system at low pressure, producing cooling. The water vapor then enters the absorber where it is absorbed by the dilute LiBr solution (returning from the generator), releasing heat of absorption that must be rejected to the cooling tower.

The concentrated LiBr solution from the generator returns to the absorber through a heat exchanger that preheats the dilute solution flowing to the generator, significantly improving cycle efficiency. This solution heat exchanger typically recovers 70-90% of the available sensible heat, reducing the generator heat input requirement and the cooling load on the absorber.

LiBr-water systems face crystallization risks if solution concentration exceeds solubility limits or temperatures fall below critical values. Crystallization control requires careful monitoring of solution concentrations, dilution cycles, and heating during shutdown to prevent solution solidification that would block flow passages.

## Ammonia-Water Systems

Ammonia-water (NH₃-H₂O) absorption systems use ammonia as the refrigerant and water as the absorbent. Unlike LiBr-water systems, both components exhibit significant volatility, requiring a rectification column to separate water vapor from ammonia vapor leaving the generator. This additional complexity increases first cost but enables operation at evaporator temperatures well below 0°C, making ammonia-water systems suitable for industrial refrigeration applications.

The system operates at higher pressures than LiBr-water cycles, with evaporator pressures ranging from 200-400 kPa and condenser pressures from 1200-1800 kPa depending on operating temperatures. These elevated pressures require more robust pressure vessel construction but eliminate vacuum operation concerns and air infiltration problems.

Ammonia's toxicity classification (ASHRAE 34 Group B2L) necessitates compliance with strict safety requirements including refrigerant detection systems, ventilation provisions, and mechanical room access restrictions. However, ammonia provides superior heat transfer characteristics and environmental benefits with zero ozone depletion potential (ODP) and zero global warming potential (GWP).

The rectification process in ammonia-water systems involves partial condensation of the generator vapor stream with preferential condensation of water, which returns to the generator as reflux. The purified ammonia vapor (typically >99.5% purity) proceeds to the condenser. Insufficient rectification reduces system capacity and efficiency as water accumulation in the evaporator degrades refrigerant properties.

## Coefficient of Performance Analysis

The coefficient of performance (COP) for absorption chillers quantifies the refrigeration effect relative to heat input:

COP = Q_evap / Q_gen

Where Q_evap represents the cooling capacity (evaporator heat absorption) and Q_gen represents the generator heat input. Single-effect absorption chillers typically achieve COP values of 0.6-0.7, meaning approximately 1.4-1.7 units of heat input produce one unit of cooling effect.

This appears inefficient compared to vapor compression systems with COP values of 3-6, but the comparison misleads because it ignores energy quality. When accounting for power plant efficiency (approximately 33% for thermal-to-electric conversion), the primary energy ratio becomes more favorable for absorption systems utilizing waste heat or direct firing.

The maximum theoretical COP for an absorption cycle operating between three temperature levels (evaporator T_e, ambient T_a, and heat source T_g) follows from Carnot efficiency considerations:

COP_max = (T_a - T_e) / T_e × T_g / (T_g - T_a)

This expression reveals that absorption cycle efficiency improves with higher generator temperatures and lower ambient (absorber/condenser) temperatures, following fundamental thermodynamic principles.

## Multi-Effect Configurations

Single-effect absorption chillers utilize heat input once in a single generator. Double-effect systems cascade the refrigeration process through two generators operating at different temperature levels, effectively using the heat input twice. The high-temperature generator (typically 150-180°C) produces refrigerant vapor that condenses in the low-temperature generator, providing the heat input for the second stage.

Double-effect configurations achieve COP values of 1.0-1.2, representing approximately 70% improvement over single-effect systems. This efficiency gain requires higher-grade heat input (direct fuel firing or high-pressure steam) but substantially reduces fuel consumption and operating costs in applications running continuous cooling loads.

Triple-effect absorption chillers extend this cascading principle through three generator stages, achieving COP values approaching 1.5-1.7. These systems require very high temperature heat sources (200-250°C) and involve significantly greater complexity and cost. Triple-effect technology finds application in large-scale district cooling plants and industrial facilities with high-temperature waste heat availability.

The efficiency improvement from multi-effect staging diminishes with each additional effect due to inherent irreversibilities and reduced temperature differences at each stage. Economic analysis typically favors single-effect systems for waste heat applications and double-effect systems for fuel-fired installations, with triple-effect justified only for specific large-scale applications.

## Heat Source Requirements

Generator heat source temperature directly impacts system capacity and efficiency. Single-effect LiBr-water systems operate with heat sources from 80-120°C including low-pressure steam (0.5-1.5 bar gauge), hot water, or waste heat from engine jacket cooling, turbine exhaust, or industrial processes. The relatively low temperature requirement enables integration with solar thermal collectors, geothermal resources, and low-grade industrial waste heat.

Double-effect systems require 140-180°C heat sources, typically satisfied by medium-pressure steam (4-8 bar gauge), direct natural gas firing, or high-temperature waste heat from processes like gas turbine exhaust. Direct-fired double-effect chillers incorporate burners and heat exchangers within the chiller package, achieving seasonal efficiency (heating value basis) of 100-130% when utilizing both cooling output and heat recovery.

Heat source stability significantly affects absorption chiller performance. Temperature fluctuations or inadequate heat transfer area in the generator cause capacity reduction and COP degradation. Generator heat transfer design must account for fouling factors per ASHRAE Standard 90.1 requirements, typically 0.0001-0.0002 m²·K/W for water-side surfaces depending on water quality.

## Engineering Design Considerations

Absorption chiller selection requires evaluation of several critical parameters beyond simple capacity matching. The available heat source characteristics (temperature, quantity, availability profile) establish feasibility and determine single- versus multi-effect configuration. Chilled water supply temperature requirements influence evaporator design and capacity, with lower temperatures reducing achievable COP.

Part-load performance differs substantially from vapor compression chillers. Absorption machines maintain relatively constant COP across the load range (70-100%) through modulation of heat input to the generator. Below 50% load, efficiency typically degrades as fixed parasitic losses (solution pump power, standby heat loss) represent increasing proportions of total input.

Cooling tower water temperature critically affects absorption chiller performance because both condenser and absorber reject heat to the same cooling water loop. Each 1°C increase in cooling water supply temperature typically reduces capacity by 3-5% and increases heat input proportionally. Oversized cooling towers (approach within 2-3°C of wet bulb temperature) provide substantial performance benefits for absorption systems.

Water treatment requirements for absorption chillers exceed vapor compression systems due to vacuum operation in LiBr-water machines. Air infiltration introduces non-condensable gases that degrade heat transfer and must be continuously purged using dedicated vacuum pumps. Oxygen infiltration also accelerates corrosion, requiring inhibitor additions and pH control per manufacturer specifications.

Physical space requirements for absorption chillers substantially exceed equivalent-capacity vapor compression machines, typically 2-3 times the footprint and 1.5-2 times the height. This size difference results from the lower volumetric efficiency of thermal compression and the additional heat exchangers required for the absorption cycle. Adequate access space for tube bundle removal (typically equal to chiller length) must be provided for maintenance.

## Applications and Economic Considerations

Absorption refrigeration excels in applications with available low-cost or waste thermal energy. Combined heat and power (CHP) systems utilize engine or turbine waste heat for absorption cooling, achieving total system efficiencies exceeding 80% through tri-generation (power, heating, and cooling). District energy systems employ large absorption chillers to utilize central plant steam or hot water during cooling season.

Industrial facilities with process waste heat streams (chemical plants, refineries, steel mills) recover otherwise-rejected energy for refrigeration duty. Solar cooling systems pair evacuated tube or parabolic trough collectors with single-effect absorption chillers, providing renewable cooling although economic viability depends heavily on incentives and avoided electric rates.

Life-cycle cost analysis must account for higher first cost (typically 2-3 times vapor compression on a $/ton basis), lower electrical consumption (approximately 90% reduction for pumps versus compressors), fuel or heat costs, maintenance requirements, and equipment longevity. Absorption chillers demonstrate exceptional durability with service lives exceeding 25-30 years, substantially longer than vapor compression equipment.

Simple payback calculations require electrical rate differential analysis comparing absorption (minimal electrical, substantial thermal input) versus vapor compression (high electrical, minimal thermal input). Time-of-use rates, demand charges, and thermal energy costs interact complexly, often requiring hourly simulation to determine optimal system selection and sizing.

## Advantages and Limitations

Absorption refrigeration provides specific technical advantages: quiet operation with minimal vibration due to absence of reciprocating or rotating compressors, excellent part-load efficiency characteristics, utilization of waste or renewable thermal energy, and reduced electrical infrastructure requirements. The technology enables cooling in locations with limited electrical capacity and provides emergency cooling capability when natural gas remains available during power outages.

Primary limitations include higher first cost, larger physical size, lower efficiency relative to modern vapor compression when comparing electrical input only, cooling tower dependency (no air-cooled option), sensitivity to cooling water temperature, and crystallization risks in LiBr-water systems. Minimum stable load (typically 10-15%) exceeds vapor compression minimum (approximately 5%), requiring auxiliary cooling or cycling operation at very low loads.

Environmental considerations favor absorption systems using natural refrigerants (water or ammonia) versus synthetic refrigerants, eliminating direct GWP impacts. However, total equivalent warming impact (TEWI) analysis must account for indirect emissions from fuel combustion in direct-fired units, potentially offsetting refrigerant advantages depending on fuel source and grid electricity carbon intensity.

ASHRAE Standard 90.1 provides minimum efficiency requirements for absorption chillers based on path designation (Path A for LiBr-water units, Path B for ammonia-water units). Current standards specify minimum COP of 0.60 for single-effect and 1.00 for double-effect water-cooled LiBr absorption chillers at AHRI Standard 560 test conditions (44°F leaving chilled water, 85°F entering condenser water, 12°F chilled water range, 10°F condenser water range).

Understanding these fundamental principles, performance characteristics, and application requirements enables appropriate absorption chiller selection and integration within broader HVAC system design, particularly for facilities with thermal energy availability or specific operational requirements favoring thermal-driven refrigeration technology.
