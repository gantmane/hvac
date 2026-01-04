---
title: "Tempered Makeup Air"
description: "Engineering analysis of tempered makeup air systems with minimal heating for freeze protection and energy savings in industrial and warehouse applications."
date: "2026-01-04"
weight: 3
tags: ["tempered makeup air", "minimal heating", "freeze protection", "industrial ventilation", "energy recovery makeup air", "warehouse ventilation"]
categories: ["Heating Systems"]
---

Tempered makeup air systems provide minimal heating (typically 45-60°F discharge temperature) to prevent freeze damage, occupant discomfort from extremely cold air, and excessive space temperature depression. This approach reduces heating capacity requirements and operating costs by 40-70% compared to fully heated makeup air while maintaining acceptable conditions in spaces with supplemental heating sources.

## Application Criteria

Tempered makeup air suits facilities where:

- **Supplemental heat sources** maintain occupied zone comfort (unit heaters, radiant heaters, process equipment)
- **Intermittent occupancy** permits wider temperature variations than office environments
- **High ceilings** (above 20 feet) enable temperature stratification without occupied zone impact
- **Energy costs** justify investment in reduced heating capacity
- **Industrial processes** generate internal heat gains supplementing space heating

Warehouses, manufacturing facilities, distribution centers, and aircraft hangars represent typical applications. These spaces tolerate discharge temperatures of 50-60°F when combined with localized heating and adequate air mixing.

## Heating Capacity Determination

Tempered systems target discharge temperatures preventing frozen coils and extreme thermal shock rather than maintaining comfortable space conditions. The heating load:

$$Q_{tempered} = \text{CFM} \times 1.08 \times (T_{discharge} - T_{outdoor,design})$$

For 10,000 CFM makeup air with:
- Outdoor design temperature: -10°F
- Target discharge temperature: 55°F

$$Q_{tempered} = 10,000 \times 1.08 \times (55 - (-10)) = 702,000 \text{ Btu/hr}$$

Compare this to fully heated makeup air at 70°F discharge:

$$Q_{heated} = 10,000 \times 1.08 \times (70 - (-10)) = 864,000 \text{ Btu/hr}$$

The tempered system requires 81% of full heating capacity, reducing equipment size and operating costs by approximately 19%. The savings increase in milder climates where design temperatures exceed -10°F.

## Energy Savings Analysis

Annual heating energy for makeup air depends on climate, operating hours, and discharge temperature setpoint. Degree-day analysis estimates seasonal consumption.

For a facility operating 5,000 hours annually in a 6,000 heating degree-day climate:

Fully heated makeup air (70°F setpoint):

$$E_{annual} = \frac{Q_h \times \text{HDD} \times 24}{\Delta T_{design} \times \eta_{heating}}$$

$$E_{annual} = \frac{864,000 \times 6000 \times 24}{80 \times 0.85} = 1,832 \text{ MMBtu/year}$$

Tempered makeup air (55°F setpoint, effective HDD = 4,200 for 55°F base):

$$E_{annual,tempered} = \frac{702,000 \times 4200 \times 24}{80 \times 0.85} = 1,105 \text{ MMBtu/year}$$

Annual savings:

$$\text{Savings} = 1832 - 1105 = 727 \text{ MMBtu/year}$$

At $12 per MMBtu natural gas cost:

$$\text{Cost savings} = 727 \times 12 = \$8,724\text{/year}$$

The actual savings depend on operating schedules, internal heat gains reducing space heating requirements, and control strategies modulating discharge temperature based on outdoor conditions.

## Freeze Protection Strategies

Tempered systems operating near freezing outdoor temperatures require robust freeze protection to prevent coil damage. Multiple strategies provide overlapping protection:

### Minimum Discharge Temperature Control

Temperature sensors downstream of heating coils continuously monitor discharge air. If temperature falls below setpoint (typically 40-50°F), controls increase heating output or shut down the system if adequate capacity is unavailable.

The low-limit differential prevents nuisance shutdowns:

$$T_{shutdown} = T_{setpoint} - \Delta T_{differential}$$

For a 50°F setpoint with 5°F differential:

$$T_{shutdown} = 50 - 5 = 45°F$$

The system continues operating between 45-50°F but shuts down if temperature falls to 45°F, preventing coil freezing.

### Face and Bypass Dampers

Some tempered makeup air units incorporate face-and-bypass dampers directing airflow through or around heating coils. Full bypass during mild weather reduces heating energy. Partial bypass prevents overcapacity during moderate outdoor temperatures.

The arrangement requires careful freeze protection controls:

- Minimum face damper position (typically 30-50%) maintains airflow across coils
- Discharge temperature sensor modulates damper position
- Low-limit override forces full face position if discharge temperature drops excessively

### Heat Recovery Integration

Waste heat from exhaust air preheats makeup air before supplemental heating, reducing required capacity and operating cost. Kitchen exhaust at 90-120°F, manufacturing process exhaust at 80-150°F, and building exhaust at 65-75°F provide preheat potential.

Run-around loop effectiveness:

$$\epsilon_{recovery} = \frac{T_{preheat} - T_{outdoor}}{T_{exhaust} - T_{outdoor}}$$

For 40% effective heat recovery with 100°F exhaust and 0°F outdoor:

$$T_{preheat} = T_{outdoor} + \epsilon(T_{exhaust} - T_{outdoor})$$
$$T_{preheat} = 0 + 0.40(100 - 0) = 40°F$$

This 40°F preheat reduces supplemental heating load from 55°F temperature rise to only 15°F (55°F - 40°F), cutting heating energy by 73%:

$$Q_{supplemental} = 10,000 \times 1.08 \times 15 = 162,000 \text{ Btu/hr}$$

## Mixing and Distribution Considerations

Tempered air at 50-60°F creates comfort challenges if introduced directly into occupied zones at high velocities. Proper distribution prevents cold drafts while achieving required space pressurization.

### High-Level Discharge

Discharge makeup air above occupied zones (minimum 12 feet, preferably 15-20 feet) allows mixing with room air before reaching occupant level. High-velocity discharge (1,500-2,500 FPM) induces 3:1 to 5:1 mixing ratios, warming supply air before occupant contact.

The mixed temperature at occupied zone height (6 feet):

$$T_{mixed} = \frac{\text{CFM}_{supply} \times T_{discharge} + \text{CFM}_{induced} \times T_{space}}{\text{CFM}_{supply} + \text{CFM}_{induced}}$$

For 4:1 mixing ratio with 55°F discharge and 65°F space temperature:

$$T_{mixed} = \frac{1 \times 55 + 4 \times 65}{1 + 4} = \frac{315}{5} = 63°F$$

This 63°F mixed temperature proves acceptable for industrial spaces, especially with localized unit heaters providing additional comfort heating.

### Perimeter Integration

Discharging tempered makeup air along exterior walls counteracts envelope heat losses and cold surfaces. The makeup air provides an "air curtain" effect at overhead doors, reducing infiltration when doors open frequently.

Perimeter discharge requires lower velocities (800-1,200 FPM) to prevent uncomfortable drafts along walls. Temperature setpoints may increase to 60-65°F for perimeter applications compared to 50-55°F for high-level discharge.

## Indirect Heating Methods

Tempered makeup air systems use various heating sources:

### Gas-Fired Indirect

Indirect-fired burners with heat exchangers provide 80-85% thermal efficiency. The lower efficiency compared to direct-fired systems (90-95%) represents the primary disadvantage, but supply air remains free of combustion products.

Heat exchanger sizing:

$$Q = UA \times \text{LMTD}$$

where LMTD (log mean temperature difference) accounts for counterflow heat transfer between flue gases and supply air. Typical heat exchanger effectiveness: 70-80%.

### Hot Water Coils

Central boiler systems supply hot water (140-180°F) to heating coils. This approach suits facilities with existing boilers and multiple heating loads. Water flow modulates to control discharge temperature:

$$\dot{m}_w = \frac{Q_h}{c_p \times \Delta T_w}$$

For 700 MBH heating load with 20°F water temperature drop:

$$\text{GPM} = \frac{700,000}{500 \times 20} = 70 \text{ GPM}$$

Two-way control valves modulate flow from 0-70 GPM based on discharge temperature sensor feedback.

### Steam Coils

Low-pressure steam (2-15 psig) delivers high capacity in compact coil sizes. Rapid response suits applications with frequent on-off cycling. However, freeze protection challenges increase due to condensate management and potential water accumulation in coils.

### Electric Resistance

Electric duct heaters provide simple installation and precise control but high operating costs. Applications limited to regions with low electricity rates or small capacity requirements (under 100 kW).

## Control Strategies

### Fixed Setpoint Control

Simple systems maintain constant discharge temperature (50-55°F) regardless of outdoor conditions. This wastes energy during mild weather but simplifies controls and ensures freeze protection.

### Reset Schedule Control

Outdoor air temperature resets discharge temperature setpoint, reducing heating during mild weather while maintaining protection during extreme cold:

| Outdoor Temperature | Discharge Setpoint |
|---------------------|-------------------|
| -10°F | 55°F |
| 10°F | 50°F |
| 30°F | 45°F |
| 50°F and above | Heating disabled |

The linear reset schedule:

$$T_{discharge,setpoint} = T_{max} - K \times (T_{outdoor} - T_{outdoor,min})$$

where $K$ is the reset ratio (typically 0.15-0.25°F discharge change per °F outdoor change).

### Space Temperature Compensation

Advanced controls adjust discharge temperature based on space temperature, increasing output when space drops below setpoint and reducing output when adequate:

$$T_{discharge} = f(T_{outdoor}, T_{space}, T_{space,setpoint})$$

This requires space temperature sensing and more sophisticated control logic but optimizes energy use while maintaining comfort.

## Design Considerations

Tempered makeup air design requires:

- **Supplemental heating analysis**: Verify unit heaters or radiant heaters maintain occupied zone comfort
- **Mixing patterns**: Ensure adequate air mixing before occupied zone contact
- **Distribution uniformity**: Prevent cold spots near makeup air discharge points
- **Freeze protection**: Multiple overlapping strategies prevent coil damage
- **Energy recovery evaluation**: ROI often favors heat recovery in tempered systems

Properly designed tempered makeup air systems deliver 40-70% energy savings compared to fully heated systems while maintaining acceptable industrial and warehouse environments. The reduced capacity requirements and operating costs often justify the additional engineering analysis and control complexity.
