---
title: "Thermal Energy Storage"
description: "Thermal energy storage systems for load shifting, demand reduction, and peak shaving including ice storage, chilled water storage, and phase change materials in HVAC applications."
weight: 4
---

## Thermal Storage Fundamentals

Thermal energy storage (TES) systems decouple thermal energy production from consumption by storing cooling or heating capacity during off-peak periods for use during peak demand times. This temporal load shifting reduces peak electrical demand charges, takes advantage of time-of-use utility rate structures, enables downsized production equipment through load leveling, and provides backup capacity during equipment failures or maintenance. The fundamental principle stores energy in the form of sensible heat (temperature change) or latent heat (phase change) in storage media including water, ice, or phase change materials.

The economic justification for thermal storage depends on utility rate structures that create significant cost differential between peak and off-peak electricity consumption. Demand charges ranging from $10-30 per kW-month for peak consumption combined with time-of-use energy charges showing 2:1 to 4:1 on-peak to off-peak ratios can provide 3-7 year simple payback on storage system capital costs. Markets with flat rate structures offer minimal economic incentive for storage despite technical benefits of load leveling and backup capacity.

## Storage Configuration Strategies

Full storage systems size storage capacity to meet entire daytime cooling load from stored capacity without operating chillers during occupied on-peak hours. The chillers operate only at night to recharge storage, completely eliminating daytime electricity demand for cooling production. This configuration provides maximum demand charge reduction but requires largest storage tank volume and chiller capacity sufficient to both meet nighttime loads and fully charge storage.

Partial storage systems operate chillers continuously while storage supplements chiller capacity during peak hours and charges during off-peak periods. The load leveling strategy sizes chillers to meet average rather than peak load, using storage to handle the difference between instantaneous loads and chiller output. Typical chiller sizing at 60-70% of peak load combined with storage covering the remaining 30-40% reduces chiller capital cost while achieving significant demand charge savings.

Demand limiting strategies operate chillers at maximum economical capacity (below demand charge threshold) with storage supplementing during high load periods. This approach optimizes the economic balance between chiller capacity, storage volume, and utility charges for specific rate structures and load profiles. Dynamic optimization algorithms can manage storage charging and discharging to minimize total energy costs considering time-varying electricity prices and load forecasts.

## Ice Storage Systems

Ice storage provides cooling capacity through the latent heat of fusion, storing approximately 144 BTU per pound of ice during the phase change from water at 32°F to ice at 32°F. The high energy density relative to sensible cooling (1 BTU per pound per degree F temperature change in water) enables compact storage volumes. Ice storage requires chiller operation at evaporator temperatures of 20-28°F to freeze water, reducing chiller efficiency by 15-25% compared to operation at standard 44°F leaving water temperature.

Ice-on-coil systems circulate glycol solution through tubes submerged in water tanks, forming ice on the exterior surface of the tubes during charging. Discharge reverses the process, melting ice and cooling the glycol. External melt configuration draws water from the bottom of tanks where melting occurs first, providing consistent discharge capacity. Internal melt systems circulate glycol through the same tubes for both charging and discharging, simplifying piping but with variable discharge capacity as ice thickness changes.

Ice harvesting systems freeze ice on refrigerated plates or evaporator surfaces, then release formed ice into storage tanks through brief warm refrigerant flow or mechanical scrapers. The ice accumulates in tanks with glycol or water flowing through void spaces during discharge. This configuration separates ice making from storage volume, enabling use of standard chillers with ice-making attachments rather than specialized in-tank heat exchangers.

## Chilled Water Storage

Stratified chilled water storage tanks maintain temperature gradient from warm water at top to cold water at bottom, enabling simultaneous charging and discharging without mixing. The thermocline region of intermediate temperature occupies 1-3 feet of tank height, with temperature changing rapidly across this narrow zone. Proper inlet diffuser design maintains stratification by introducing charging water at appropriate level based on density without disturbing the thermocline.

Storage capacity equals the water volume multiplied by temperature difference and specific heat: Q = m × cp × ΔT. A 100,000 gallon tank with 20°F temperature range (44°F supply to 64°F return) stores approximately 1670 ton-hours of cooling. The large volume requirements relative to ice storage (6-8 times greater for equivalent capacity) limit chilled water storage to applications with available space and minimal storage temperature depression acceptable.

Stratified storage tanks require height-to-diameter ratio of 1:1 or greater to establish stable stratification. Shorter, wider tanks experience greater mixing and thermocline degradation. The tank design incorporates inlet diffusers that distribute charging flow horizontally across the tank cross-section at appropriate elevation determined by entering water density. Radial diffusers, octagonal ring diffusers, or slotted pipe manifolds provide the required flow distribution with minimal velocity to prevent jet mixing.

## Phase Change Materials

Phase change materials (PCM) store and release thermal energy through solid-liquid phase transitions at specific temperatures. Organic PCMs including paraffin waxes offer phase change temperatures from 40-80°F suitable for building thermal storage, with latent heat of fusion ranging from 60-90 BTU/lb. Inorganic PCMs including salt hydrates provide higher energy density (100-150 BTU/lb) but may experience supercooling and phase segregation reducing long-term reliability.

Encapsulated PCM systems enclose material in plastic containers, metal tubes, or panels that provide containment while enabling heat transfer with surrounding air or water. Encapsulation in small containers (1-2 inch diameter spheres or flat panels) provides high surface area for rapid charging and discharging. The containers pack into storage tanks with air or water flowing through interstitial spaces, or integrate directly into building components including ceiling panels, floor systems, or drywall.

PCM thermal storage applications include passive building thermal mass enhancement, off-peak precooling of building structure, peak load shifting in packaged AC units, and thermal buffering in transport refrigeration. The narrow temperature range of phase transition (typically 2-4°F) limits storage capacity compared to sensible storage with wide temperature swings but enables isothermal storage maintaining precise temperature control during discharge.

## Storage System Design Considerations

Storage tank sizing depends on load profile characteristics, utility rate structure, and selected storage strategy. Full storage requires capacity equal to entire daytime cooling load minus any base load chiller operation. Partial storage capacity equals the difference between peak instantaneous load and average load over the charging period. Load duration curves showing accumulated cooling energy requirement over time enable direct determination of required storage capacity to meet specific demand reduction targets.

Chiller sizing for storage systems accounts for nighttime storage charging load plus concurrent building loads during charging period. The required chiller capacity equals: Q_chiller = Q_storage/t_charge + Q_night, where Q_storage is total storage capacity, t_charge is available charging hours, and Q_night represents nighttime building loads. Available charging time depends on utility rate schedule and desired charging completion time, typically 8-12 hours for most applications.

Storage discharge rates vary throughout the day as building loads change and storage capacity depletes. Variable speed pumps modulate flow between chillers and storage to match instantaneous cooling demand. Control strategies prioritize storage discharge during highest cost periods while maintaining sufficient reserve capacity to meet unexpected load increases or extended peak periods. Predictive controls using weather forecasts and historical load patterns optimize storage utilization across multi-day time horizons.

## Integration with Building Systems

Thermal storage integrates with building chilled water distribution through series, parallel, or combined configurations. Series connection places storage in the main distribution loop, with all return water passing through storage before returning to chillers. This arrangement provides maximum storage utilization but may limit flow rates and temperature differentials. Parallel connection enables independent control of storage flow separate from main distribution, offering operational flexibility at the cost of additional piping and pumps.

The storage system must coordinate with building automation system to implement charging and discharging schedules, respond to utility demand response signals, and optimize operation based on real-time pricing where available. Monitoring of storage state-of-charge, chiller loading, building loads, and electricity costs enables dynamic optimization adjusting operations to minimize costs while ensuring comfort requirements are met.

## Performance Monitoring and Optimization

Continuous monitoring of storage system performance verifies expected energy cost savings, identifies operational problems, and enables ongoing optimization. Key performance metrics include storage efficiency (energy out divided by energy in), peak demand reduction achieved, time-of-use energy cost savings, and chiller energy consumption compared to non-storage baseline. Storage efficiency typically ranges from 85-95% accounting for thermal losses and parasitic pumping energy.

Common operational problems reducing storage performance include improper charging schedules leaving storage partially charged at peak periods, excessive thermal losses from inadequate tank insulation, thermocline degradation in stratified storage reducing effective capacity, and control sequence problems that operate chillers during high-cost peak periods unnecessarily. Regular commissioning and performance verification maintain design performance and identify opportunities for control refinement improving economic returns.
