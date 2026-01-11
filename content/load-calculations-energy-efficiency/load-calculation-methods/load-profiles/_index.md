---
title: "Load Profiles"
description: "Analysis of hourly load profiles for HVAC system design including peak load timing, diversity factors, coincident vs. non-coincident loads, and load duration curves for equipment optimization."
weight: 4
---

## Load Profile Fundamentals

Load profiles characterize the time-varying nature of heating and cooling requirements throughout daily and annual cycles. Understanding temporal load patterns enables optimization of equipment sizing, thermal storage strategies, and control sequences. The profile shape reveals peak load magnitude and timing, load duration at various capacities, and diversity between different building zones and systems.

Hourly load profiles plot thermal loads as a function of time, typically showing 24-hour patterns for design days or full 8760-hour annual profiles. Design day profiles establish peak loads for equipment sizing while annual profiles enable energy consumption calculations, part-load performance evaluation, and economic analysis of efficiency measures. The area under the load profile curve represents total thermal energy consumption over the time period.

## Peak Design Day Selection

Peak design day profiles determine maximum equipment capacity requirements. The cooling design day experiences maximum solar heat gain and outdoor temperature, typically occurring during clear sky conditions in July or August for northern hemisphere mid-latitudes. The specific day showing maximum load depends on building orientation, window distribution, internal load schedules, and thermal mass characteristics.

East and west-facing buildings may peak on days differing from south-facing structures due to varying solar geometry. Buildings with high internal loads may show relatively constant cooling loads with minimal sensitivity to outdoor conditions, peaking when internal loads and occupancy reach maximum rather than on the hottest outdoor day. Detailed hour-by-hour simulation across multiple design days identifies the true peak condition for each system.

Heating design days typically assume clear night sky conditions allowing maximum radiative heat loss, minimum outdoor temperature, and no solar gain contribution. The peak heating load occurs during morning warm-up when the building must recover from nighttime setback while outdoor temperature remains at minimum. Continuous heating without setback eliminates warm-up load but requires capacity to offset steady-state envelope losses at design temperature.

## Coincident vs. Non-Coincident Loads

Coincident load analysis evaluates total building or system load at each hour, accounting for time lags between zone peaks due to varying solar exposure and schedules. The peak coincident load represents the maximum simultaneous load across all zones, occurring when the time-weighted sum reaches maximum. This coincident peak typically falls 10-25% below the sum of individual zone peak loads due to diversity.

Non-coincident load summation adds individual zone peaks regardless of timing, resulting in conservative equipment sizing that provides excess capacity during actual operation. This approach applies appropriately when zones require independent systems with no opportunity for load diversity benefits. Central plant sizing based on non-coincident loads results in substantial overcapacity since zones rarely peak simultaneously.

The diversity factor equals the ratio of coincident peak load to non-coincident peak load, typically ranging from 0.75-0.90 for commercial buildings. Higher diversity occurs in buildings with varied orientations and occupancy patterns. Low diversity characterizes uniform spaces with similar solar exposure and synchronized schedules. Proper diversity factor application prevents oversizing while ensuring adequate capacity during actual peak conditions.

## Hourly Load Distribution Patterns

Commercial office building load profiles typically show morning ramp-up as systems overcome nighttime setback and building warms toward occupied setpoint. Loads increase through morning hours as occupancy, lighting, and equipment reach full operation. Peak loads occur during mid-to-late afternoon when solar gains on west facades combine with sustained internal loads. Evening profiles show declining loads as occupancy decreases and outdoor temperatures moderate.

Retail spaces experience different patterns with peak loads coinciding with maximum customer occupancy, often occurring evenings and weekends rather than weekday afternoons. The high occupant density and lighting levels create substantial internal loads that dominate total load. Outdoor air ventilation requirements tracking occupancy create proportional load variations.

Industrial facilities may show relatively constant loads driven by continuous processes and high equipment heat gains with minimal variation from outdoor conditions or time of day. Data centers similarly exhibit constant high internal loads with peak capacity required continuously rather than only during specific hours. These applications require different equipment strategies than conventional commercial buildings with variable loads.

## Block Load Estimation

Block load calculations estimate total building cooling capacity by summing zone loads at their individual peak times, providing a simplified alternative to detailed hourly analysis. This method quickly establishes approximate equipment capacity requirements during preliminary design phases when detailed schedules and profiles remain undefined.

The block load approach inherently includes non-coincident summation, resulting in overcapacity relative to actual simultaneous peak. Typical overcapacity ranges from 10-25% depending on building diversity. Experience-based adjustment factors can correct for anticipated diversity, though accuracy remains limited compared to rigorous hourly simulation.

Block loads suit residential applications and small commercial buildings where load diversity benefits are minimal and simulation complexity is unwarranted. Large commercial buildings with varied zone characteristics benefit from detailed hourly analysis that captures actual coincident peak timing and magnitude.

## Diversity Factors Application

Diversity factors account for the statistical unlikelihood of all systems or zones simultaneously operating at peak capacity. These factors apply at multiple levels including zone-to-zone diversity within systems, system-to-system diversity within buildings, and building-to-building diversity in campus or district applications.

Lighting diversity recognizes that not all luminaires operate simultaneously in large spaces with manual switching or daylight harvesting controls. Typical diversity factors of 0.8-0.9 account for vacant areas and disabled lighting zones. Occupancy diversity similarly recognizes that design occupancy density rarely occurs uniformly throughout large buildings. Conference rooms, offices, and common areas reach peak occupancy at different times with diversity factors of 0.7-0.85.

Equipment diversity reflects the reality that computers, printers, and appliances do not all operate simultaneously at full power. Measured equipment loads typically reach only 50-70% of nameplate ratings due to power management, idle states, and partial utilization. Diversity factors between 0.5-0.7 are common for office equipment loads.

## Load Duration Curves

Load duration curves re-plot hourly loads in descending order from maximum to minimum, showing the number of hours at or above each capacity level. The curve enables rapid visualization of equipment part-load operation time distribution, supporting economic analysis of high-efficiency equipment and thermal storage sizing.

A steep load duration curve indicates high peaking factor with few hours at peak capacity and many hours at reduced load. Flat load duration curves show relatively constant loads with less capacity variation. The curve shape impacts equipment selection since variable-capacity systems provide greatest benefit for steep curves with extensive part-load operation, while constant-capacity equipment suits flat curves.

Integration of the load duration curve yields total annual thermal energy consumption. The area under the curve multiplied by time increment equals annual cooling or heating energy requirement in ton-hours or BTU-hours. This energy consumption value enables calculation of operating costs and comparison of efficiency improvement measures.

## Part-Load Performance Implications

Modern variable-capacity equipment achieves high efficiency at partial load but requires appropriate load profiles to realize benefits. Load duration curves showing predominantly part-load operation (below 70% capacity) justify variable-speed compressors, variable-frequency drive fan systems, and modulating boilers that maintain efficiency at reduced output.

Constant-capacity equipment with on-off control suffers efficiency degradation at part load due to cycling losses. Load profiles with short cycles and frequent starts increase wear and reduce seasonal efficiency. Proper equipment sizing relative to load profile characteristics optimizes both peak capacity provision and part-load efficiency.

Multiple smaller units rather than single large equipment enable better capacity matching to varying loads through staging. Three 33% capacity units provide 33%, 67%, and 100% operation points compared to single-step on-off control. The improved capacity modulation reduces cycling frequency and maintains higher average efficiency.

## Annual Load Profiles and Energy Analysis

Annual 8760-hour load profiles enable detailed energy consumption calculation accounting for actual weather patterns, occupancy schedules, and system operation throughout the year. The profiles reveal seasonal load patterns, identify opportunities for free cooling or economizer operation, and support evaluation of thermal storage and load management strategies.

Monthly load aggregation from hourly profiles shows seasonal energy distribution between heating and cooling. The shoulder seasons between peak summer and winter may offer opportunities for natural ventilation, economizer cooling, or heat recovery that reduce annual energy consumption. System control strategies optimized for annual performance rather than peak conditions can achieve substantial energy savings.

## Load Profile Optimization Strategies

Analysis of load profiles identifies opportunities to reduce peak demands and shift loads to off-peak periods. Precooling strategies use overnight capacity to charge building thermal mass, reducing daytime cooling requirements. Acceptable thermal drift during peak afternoon hours enables smaller equipment by leveraging thermal storage.

Time-of-use electricity rates create economic incentives for load shifting that may justify thermal storage systems. The load profile analysis quantifies peak reduction potential and storage capacity requirements. Demand response programs reward load curtailment during utility peak events, requiring profile analysis to identify dispatchable loads and quantify curtailment capacity.
