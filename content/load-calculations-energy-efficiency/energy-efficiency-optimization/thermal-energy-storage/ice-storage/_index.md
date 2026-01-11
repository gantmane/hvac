---
title: "Ice Storage Systems"
description: "Ice thermal storage design including full and partial storage strategies, ice-on-coil, ice harvesting, and encapsulated ice systems for cooling load management and demand reduction."
weight: 1
---

## Ice Storage Principles

Ice storage systems utilize the latent heat of fusion (144 BTU/lb or 334 kJ/kg) to store cooling capacity in compact volumes compared to sensible chilled water storage. The phase change from water to ice at 32°F occurs at constant temperature, enabling isothermal storage and discharge without the temperature stratification concerns of chilled water systems. This high energy density reduces required storage tank volume by 85-90% relative to equivalent chilled water storage with 18-22°F temperature differential.

The tradeoff for compact storage volume is reduced chiller efficiency during ice-making operation. Producing ice requires refrigerant evaporator temperatures of 18-26°F compared to 38-42°F for conventional chilled water production. This lower evaporating temperature increases compressor lift and reduces coefficient of performance (COP) by 15-25% during charging. The overall system efficiency depends on balancing storage capacity benefits against ice-making inefficiency through optimal charging schedules and equipment selection.

## Full Storage Configuration

Full storage systems produce sufficient ice during off-peak nighttime hours to meet entire daytime cooling load without chiller operation during peak utility demand periods. The chillers charge storage from approximately 8 PM to 6 AM, then remain off while building loads discharge stored cooling throughout the occupied day. This strategy eliminates on-peak electricity demand for cooling production, maximizing demand charge savings in rate structures with high per-kW demand charges.

The required storage capacity equals the integrated daytime cooling load minus any nighttime charging periods that overlap with occupied hours. A building with 1000 ton peak load operating 10 hours per day with 70% average load factor requires approximately 7000 ton-hours storage capacity (1000 tons × 10 hours × 0.70). The chiller must produce this cooling energy plus concurrent nighttime building loads within the available charging window, typically requiring installed chiller capacity of 60-80% of peak building load depending on charging hours available.

Full storage maximizes demand reduction but requires largest storage tanks and highest ice-making capacity. Economic optimization considers utility rate structure, available storage space, and capital budget constraints. Markets with demand charges exceeding $15-20/kW typically justify full storage, while lower demand charge markets may favor partial storage with reduced first cost.

## Partial Storage Design

Partial storage systems operate chillers continuously, using storage to supplement chiller output during peak load periods and charging during low-load hours. The load leveling strategy sizes chillers at 50-70% of peak building load, with storage providing the difference between instantaneous loads and constant chiller output. This configuration reduces chiller capital cost while achieving significant demand charge savings through peak shaving rather than complete elimination.

The optimal chiller-to-storage capacity ratio depends on the specific utility rate structure and building load profile. Graphical optimization plots total utility cost (energy plus demand charges) versus chiller capacity, identifying the economically optimal chiller size. Typical optimal points occur at chiller capacities of 50-65% of peak load, balancing reduced demand charges against ice-making energy penalty and storage capital costs.

Demand limiting strategies operate chillers at maximum output below utility demand charge thresholds, supplementing with storage when building loads exceed chiller capacity. This approach optimizes operation for complex rate structures with multiple demand charge tiers or seasonal variations. Real-time optimization algorithms dynamically adjust charging and discharging schedules based on actual loads, outdoor conditions, and electricity costs.

## Ice-on-Coil Technology

Ice-on-coil systems freeze ice directly on the exterior of submerged heat exchanger tubing containing circulating glycol solution (typically 20-30% ethylene or propylene glycol). During charging, cold glycol at 18-22°F flows through tubes, extracting heat from surrounding water and freezing ice layers up to 0.5-1.0 inch thickness on tube exteriors. The growing ice reduces heat transfer area and increases thermal resistance, requiring gradually decreasing glycol temperature to maintain ice production rate as charge cycle progresses.

Discharge operation circulates warm glycol returning from building loads through the same tubes, melting ice from the inside surface outward. External melt configuration extracts water from the tank bottom where melting occurs preferentially, providing consistent discharge capacity and glycol temperature. Internal melt systems rely on conduction through ice layers to tube surface, creating variable discharge capacity as ice thickness changes and distance from tube to ice surface increases.

Typical ice-on-coil systems achieve storage efficiencies of 90-95%, accounting for glycol pumping energy and thermal losses. The tubes occupy 30-40% of tank volume, limiting effective storage density compared to other technologies. Modular design enables capacity expansion by adding tanks. The requirement for glycol systems increases cost and maintenance complexity compared to direct water systems but prevents freezing damage and enables operation below 32°F for enhanced heat transfer.

## Ice Harvesting Systems

Ice harvesting technology freezes thin ice sheets on vertical refrigerated plates or horizontal evaporator surfaces, then releases formed ice into storage tanks through brief heating cycles. During the harvest cycle, warm refrigerant gas flows through evaporator surfaces for 10-30 seconds, warming the surface to 35-40°F and releasing ice sheets through thermal expansion differential. The ice falls into storage tanks where it accumulates as discrete pieces with high surface area and good thermal communication with discharge fluid.

The harvest cycle occurs every 15-45 minutes depending on ice thickness desired (typically 0.25-0.375 inches) and refrigeration capacity. Thinner ice provides faster harvesting and better storage-to-discharge heat transfer but lower harvesting efficiency due to frequent defrost penalties. Thicker ice reduces harvest frequency and improves efficiency but increases storage inventory and thermal mass delaying discharge response. Typical designs optimize for 0.3 inch ice thickness harvested every 20-30 minutes.

Ice harvesting separates ice making from storage, enabling use of conventional chillers with ice-maker modules rather than specialized in-tank equipment. The modular ice makers occupy less floor space than equivalent ice-on-coil tanks, suiting retrofits in existing mechanical rooms. Storage tanks can be located remotely from ice makers, providing installation flexibility. The discrete ice pieces with high surface area enable rapid discharge response and consistent outlet temperatures compared to ice-on-coil systems.

## Encapsulated Ice Storage

Encapsulated ice systems contain water in sealed plastic containers (typically 4-6 inch diameter spheres or rectangular canisters) that freeze and melt without direct contact between ice/water and heat transfer fluid. The glycol solution circulates through void spaces between containers, extracting or delivering thermal energy through container walls. The complete separation of storage water from heat transfer fluid prevents contamination, eliminates need for water treatment, and simplifies system maintenance.

The encapsulation reduces effective storage density by 25-35% compared to direct-contact systems since container walls add thermal resistance and containers occupy 50-55% of tank volume with remainder filled by glycol. The modular containers enable easy capacity expansion and replacement of damaged units. Various container geometries optimize packing density versus surface area for heat transfer, with spherical shapes providing good compromise.

Encapsulated systems suit applications requiring glycol separation for water quality reasons or where future capacity expansion is anticipated. The containers can integrate into existing storage tanks during retrofits without modifying tank internals. Lower first cost compared to ice-on-coil systems offsets slightly reduced storage efficiency, making encapsulated ice attractive for smaller applications where ice-on-coil tanks would be oversized.

## Ice Slurry Systems

Ice slurry technology produces microscopic ice crystals suspended in liquid carrier fluid (water or dilute glycol), creating a pumpable mixture with high cooling capacity density. The slurry typically contains 10-40% ice by mass, providing cooling density intermediate between chilled water and solid ice while maintaining fluid flow characteristics. Production methods include scraped-surface heat exchangers, supercooling with nucleation, or vacuum-flash freezing.

The pumpable nature of ice slurry eliminates separate charging and discharging circuits required by static ice storage, enabling direct use as cooling medium in building distribution systems. This reduces system complexity and improves heat transfer compared to glycol intermediate heat transfer. Ice slurry suits district cooling applications and industrial processes requiring large capacity cooling with minimal temperature depression, though residential and commercial building applications remain limited due to complexity and cost.

## Control Strategies and Optimization

Effective ice storage operation requires sophisticated controls managing charging schedules, discharge priorities, and chiller loading to minimize energy costs while ensuring adequate storage for peak periods. Optimal charging initiates at the onset of off-peak electricity rates, modulating chiller output to complete storage charging just before peak rate period begins. Premature charge completion wastes cold storage capacity to standby losses, while incomplete charging leaves insufficient capacity for peak demands.

Discharge control prioritizes storage utilization during highest electricity cost periods, preserving chiller operation for lower-cost hours. Weather-based predictive controls use temperature forecasts to adjust charging schedules for anticipated next-day loads, preventing storage depletion during extended heat waves while avoiding over-charging during mild weather. The control system monitors storage inventory continuously, adjusting discharge rates to extend capacity across the full peak period without premature exhaustion.
