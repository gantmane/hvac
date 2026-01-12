---
title: "Thermal Energy Storage Advanced"
weight: 1
description: "Advanced thermal energy storage systems for HVAC applications including sensible heat storage, latent heat storage, phase change materials, ice storage, and thermochemical storage with system sizing and economic analysis."
keywords: ["thermal energy storage", "TES systems", "ice storage", "phase change materials", "PCM", "chilled water storage", "hot water storage", "thermochemical storage", "load shifting", "peak demand reduction"]
---

Thermal energy storage (TES) systems decouple energy production from consumption, enabling equipment operation during off-peak periods when electricity costs are lower and utility demand charges can be minimized. These systems store thermal energy in sensible, latent, or thermochemical form for later use in heating or cooling applications.

## Sensible Heat Storage Systems

Sensible storage systems utilize the temperature change of a storage medium to store and release thermal energy according to Q = mcΔT. The storage capacity depends directly on the mass of the storage medium, its specific heat, and the temperature differential maintained.

### Chilled Water Storage

Chilled water storage represents the most straightforward TES approach. Water is chilled during off-peak hours and stored at temperatures between 39°F and 45°F in insulated tanks. The storage capacity is calculated as:

Q = m × cp × (Treturn - Tsupply)

Where cp for water is 1.0 BTU/lb-°F. A 10°F temperature differential provides approximately 10 BTU/lb of storage capacity.

Tank configurations include stratified storage tanks that maintain temperature layering through diffusers at inlet and outlet points, preventing mixing between warm return water and cold supply water. Properly designed diffusers maintain a thermocline thickness of 1 to 2 feet, maximizing the usable storage volume.

Storage tank sizing requires evaluation of the cooling load profile, available charging time, and desired discharge duration. Full storage systems meet the entire daily cooling load from storage, while partial storage systems combine storage discharge with simultaneous chiller operation during peak periods.

### Hot Water Storage

Hot water storage operates on identical principles but at elevated temperatures, typically 140°F to 180°F for space heating applications and 180°F to 200°F for domestic hot water storage. The higher temperature differential compared to chilled water storage provides greater volumetric energy density.

Pressurized storage vessels accommodate temperatures above 212°F, with storage capacities exceeding 15 BTU/lb for a 15°F differential. Tank insulation becomes critical at elevated temperatures, with heat loss rates proportional to the temperature difference between stored water and ambient conditions.

## Latent Heat Storage Systems

Latent heat storage exploits phase change processes that absorb or release substantial energy at nearly constant temperature. The latent heat of fusion provides energy densities 3 to 10 times greater than sensible storage over equivalent temperature ranges.

### Ice Storage Systems

Ice storage utilizes the latent heat of fusion of water at 144 BTU/lb, providing high energy density in a compact volume. Ice-on-coil systems circulate glycol solution through submerged heat exchanger coils, building ice layers during charging. External melt systems discharge from the outside of the ice mass, while internal melt systems circulate glycol through the ice mass for faster discharge rates.

Ice harvesting systems produce ice on evaporator plates and periodically release ice pieces into a storage tank. Warm return glycol melts the ice during discharge, providing chilled solution at 32°F to 34°F for low-temperature air distribution systems.

System selection depends on discharge rate requirements, available space, and desired supply temperatures. Ice-on-coil systems provide moderate discharge rates with simple construction, while ice harvesting systems deliver high discharge rates and full storage utilization.

### Encapsulated Ice Storage

Encapsulated ice systems contain water in plastic containers submerged in a glycol tank. Ice forms inside the containers during charging, with the glycol solution acting as the heat transfer fluid. This approach eliminates the 25% glycol solution required for ice-on-coil systems, improving charging efficiency.

### Phase Change Material Storage

PCM storage extends beyond water/ice systems to materials with phase change temperatures matching specific application requirements. Eutectic salt solutions, paraffin waxes, and engineered PCMs provide phase change temperatures from -20°F to 120°F.

Salt hydrates offer high volumetric energy density and thermal conductivity but experience phase separation and subcooling. Paraffin-based PCMs provide reliable phase change behavior with minimal subcooling but require thermal conductivity enhancement through fins or graphite additives.

Microencapsulated PCMs incorporate phase change material in protective shells ranging from 1 to 1000 micrometers in diameter. This approach prevents leakage, increases surface area for heat transfer, and enables PCM integration into building materials.

## Thermochemical Storage

Thermochemical energy storage utilizes reversible chemical reactions that absorb heat during an endothermic charging reaction and release heat during an exothermic discharging reaction. These systems achieve energy densities 5 to 10 times greater than sensible storage with minimal thermal losses during long-term storage.

Adsorption systems using silica gel, zeolite, or activated carbon pairs with water or ammonia provide chemical heat pumping effects. Absorption systems using lithium bromide/water or ammonia/water solutions operate on similar principles with liquid absorbent phases.

The primary advantage lies in energy storage without insulated tanks, as energy resides in chemical bonds rather than temperature differences. This enables seasonal storage applications where heat collected in summer provides heating in winter months.

## System Sizing Methodology

TES system sizing requires detailed analysis of facility load profiles, utility rate structures, and equipment operating constraints. The fundamental sizing equation balances daily cooling load with storage capacity and charging capacity:

Qload = Qstorage + Qchiller-on-peak

For full storage systems, chiller capacity matches the charging rate rather than peak load, typically 40% to 60% of conventional design capacity. Partial storage systems utilize smaller storage volumes while maintaining higher chiller capacity for simultaneous operation during peak periods.

The optimal storage-to-peak-load ratio depends on the utility rate structure. Time-of-use rates with significant on-peak to off-peak differentials favor larger storage systems, while demand charge structures may justify partial storage approaches that limit peak demand without complete load shifting.

## Discharge Rate Considerations

Storage discharge rate capabilities determine system response to varying loads. The discharge rate factor expresses the ratio of discharge capacity to total storage capacity:

DRF = Discharge Rate (tons) / Total Storage (ton-hours)

Ice storage systems typically achieve DRF values of 0.15 to 0.35, meaning a 1000 ton-hour storage system delivers 150 to 350 tons of instantaneous cooling. Chilled water storage provides higher DRF values of 0.5 to 1.0 due to active pumping and minimal thermal resistance.

Heat exchanger sizing in latent storage systems controls discharge rates. Insufficient heat transfer area limits discharge capacity even with adequate stored energy. The log mean temperature difference between storage medium and heat transfer fluid governs heat exchanger performance:

Q = UA × LMTD

Where U represents the overall heat transfer coefficient including fouling factors and thermal resistances.

## Economic Analysis Framework

TES system economics depend on capital costs, operating cost savings, and demand charge reductions. The simple payback period compares incremental system cost to annual utility savings:

Payback = (CAPEX_TES - CAPEX_baseline) / Annual Savings

Capital cost components include storage tanks or modules, expanded cooling plant equipment, controls, and installation labor. Chilled water storage typically costs $50 to $150 per ton-hour, while ice storage ranges from $150 to $400 per ton-hour depending on system type and capacity.

Operating cost savings derive from energy cost reductions through off-peak operation and demand charge reductions from peak load shifting. Facilities with demand charges exceeding $15/kW and on-peak energy rates above $0.15/kWh present favorable economics for TES implementation.

Life cycle cost analysis incorporates maintenance costs, efficiency impacts, and equipment life. Sensible storage systems require minimal maintenance beyond tank inspections and insulation verification. Latent storage systems need glycol testing, freeze protection verification, and heat exchanger maintenance.

The net present value calculation accounts for the time value of money over the system lifetime:

NPV = Σ (Annual Savings / (1 + r)^n) - Initial Investment

Where r represents the discount rate and n is the analysis period. TES systems with NPV greater than zero provide positive returns over the analysis period.

Integration with renewable energy systems enhances TES economics by storing excess generation for later use. Solar thermal systems coupled with hot water storage provide continuous heating capability despite intermittent solar availability. Photovoltaic systems combined with chilled water or ice storage shift electrical demand from generation periods to consumption periods.
