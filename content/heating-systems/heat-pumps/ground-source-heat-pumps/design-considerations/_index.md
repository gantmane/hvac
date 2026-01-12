---
title: "Ground Source Heat Pump Design Considerations"
description: "Comprehensive technical guide covering ground loop sizing, load calculations, antifreeze selection, pumping energy, entering water temperature design, and annual energy balance for geothermal heat pump systems."
keywords: "ground source heat pump design, geothermal loop sizing, GSHP load calculations, ground loop antifreeze, entering water temperature, annual energy balance, geothermal heat exchanger design"
weight: 3
---

Ground source heat pump system design requires rigorous analysis of building thermal loads, ground thermal properties, and equipment performance characteristics to achieve long-term system sustainability and efficiency. Proper design ensures the ground loop neither progressively gains nor loses heat over multiple years of operation.

## Load Calculations and System Sizing

Building load calculations form the foundation of ground source heat pump design. Peak heating and cooling loads determine heat pump capacity, while annual heating and cooling energy establishes ground loop size.

**Critical Load Parameters:**
- Peak block heating load with appropriate safety factors (typically 1.10-1.15)
- Peak block cooling load accounting for diversity and load shedding
- Annual heating energy consumption (kWh or ton-hours)
- Annual cooling energy consumption with rejection heat from compressor work
- Load imbalance ratio between heating and cooling demands

The ratio of annual heating to cooling energy significantly impacts ground loop sizing. Heating-dominated buildings (schools, northern climate offices) progressively cool the ground, while cooling-dominated facilities (data centers, southern buildings) add heat to the soil annually.

## Ground Loop Sizing Methods

Ground loop length calculation employs empirical design methods or detailed simulation software. The fundamental sizing equation balances heat transfer requirements against available ground thermal conductivity.

**Design Approaches:**
1. Rule-of-thumb methods (50-80 ft/ton for vertical bores in typical soil)
2. IGSHPA design manual procedures with monthly load profiles
3. ASHRAE Handbook methods using peak and annual loads
4. Detailed hourly simulation (GLD, GLHEPRO, EnergyPlus)

Vertical borehole systems typically require 150-250 ft depth per ton of capacity, while horizontal loops need 400-600 ft of pipe per ton. Actual requirements vary by ground thermal conductivity (0.6-1.8 Btu/hr·ft·°F for soil, 1.5-3.5 for rock), undisturbed ground temperature, and load characteristics.

**Sizing Factors:**
- Ground thermal conductivity from thermal response test or estimated values
- Undisturbed ground temperature (typically 50-60°F in continental US)
- Borehole thermal resistance (grout conductivity and pipe configuration)
- Design entering water temperatures (heating: 25-40°F, cooling: 80-95°F)
- Required loop temperature differential (5-10°F for typical flow rates)

## Entering Water Temperature Design

Heat pump entering water temperature (EWT) directly impacts capacity and efficiency. Lower EWT during heating reduces capacity and COP, while higher EWT during cooling produces similar degradation.

Manufacturers rate equipment at standard conditions (77°F EWT for cooling, 32°F for heating per ISO 13256-2), but actual design conditions vary. Conservative design uses 30-35°F minimum heating EWT and 90-95°F maximum cooling EWT for 20-30 year design life.

**Temperature Design Criteria:**
- Minimum heating EWT: 25-40°F (lower values require larger loops)
- Maximum cooling EWT: 80-95°F (higher values need additional loop capacity)
- Loop temperature range over operating season: 15-25°F typical
- Avoid ground freezing (antifreeze required below 32°F)
- Long-term temperature drift: limit to 5°F over 20 years

## Antifreeze Selection and Concentration

Ground loops operating below 40°F require antifreeze to prevent freezing. Antifreeze selection balances freeze protection, pumping energy, heat transfer performance, toxicity, and cost.

| Antifreeze Type | Freeze Point at 25% | Viscosity Impact | Applications |
|-----------------|---------------------|------------------|--------------|
| Propylene Glycol | 10°F | High (2.5x water) | Potable water concern areas |
| Ethylene Glycol | 5°F | Moderate (2.0x water) | Industrial, commercial systems |
| Methanol | -15°F | Low (1.3x water) | Cold climate, higher pumping efficiency |
| Potassium Acetate | 15°F | Moderate | Food facilities, low toxicity required |

Antifreeze reduces fluid thermal conductivity by 5-10% and increases viscosity significantly, raising pumping power 50-150% compared to water. Concentration must provide freeze protection 10-15°F below minimum design EWT as safety margin.

**Design Considerations:**
- Calculate required freeze point from minimum loop temperature
- Add 10-15°F safety margin for design concentration
- Account for increased pumping energy in system power consumption
- Include inhibitor packages to prevent corrosion
- Plan for periodic testing and replacement (every 3-5 years)

## Pumping Energy and Flow Rate Design

Loop circulation pumps represent 8-15% of total ground source heat pump system energy consumption. Optimal design balances heat transfer effectiveness against pumping power.

**Flow Rate Design:**
- Standard flow: 2.5-3.0 gpm per ton of capacity
- Laminar flow avoided (Reynolds number > 4000)
- Turbulent flow ensures effective heat transfer
- Loop temperature differential: 5-10°F at design conditions
- Higher flow rates improve EWT but increase pumping energy

Pressure drop through ground loop piping determines pumping power. Vertical borehole systems exhibit lower pressure drop (10-25 ft head per 100 ft loop) compared to horizontal loops (30-50 ft head per 100 ft) due to larger pipe diameters and shorter total length per bore.

**Pump Selection Criteria:**
- Total dynamic head: loop pressure drop plus manifold and equipment losses
- Flow rate: system capacity x 2.5-3.0 gpm/ton
- Pump efficiency: select 70-85% peak efficiency at design point
- Variable speed pumps for multiple heat pump systems
- Redundant pumps for critical applications

## Annual Energy Balance

Long-term system viability requires the ground loop to reject approximately the same heat annually as it absorbs. Imbalanced loads cause progressive ground temperature drift, degrading performance over 10-20 years.

**Balance Analysis:**
- Calculate annual heat rejection during cooling (includes compressor heat)
- Calculate annual heat extraction during heating
- Net annual imbalance should remain within ±5% of total annual energy
- Excessive imbalance requires hybrid system design

Heat rejected during cooling includes building cooling load plus compressor work (typically 1.25-1.3 times cooling load). Heat absorbed during heating equals building heating load minus compressor work (typically 0.70-0.75 times heat pump heating output).

**Imbalance Mitigation:**
1. Hybrid systems with supplemental heat rejection (cooling tower, dry cooler)
2. Hybrid systems with auxiliary heating (boiler bypass, solar thermal)
3. Oversized ground loop to accommodate long-term drift
4. Strategic building load management to balance annual energy

## Equipment Selection and Integration

Heat pump selection coordinates with ground loop design to optimize system performance across the operating temperature range.

**Selection Parameters:**
- Rated capacity at design entering water temperatures
- COP/EER performance curves throughout temperature range
- Compressor type (scroll for variable capacity, reciprocating for multi-stage)
- Built-in or external flow centers with pumps and controls
- Reversible or heating/cooling only configurations

Water-to-water heat pumps for hydronic distribution offer higher efficiency than water-to-air units but require separate ventilation systems. Multiple smaller heat pumps provide better part-load efficiency than single large units through staging and variable capacity operation.

**Design Integration:**
- Buffer tanks to reduce short cycling with low thermal mass distribution
- Heat pump staging controls based on load and EWT
- Loop temperature monitoring with diagnostic alarms
- Desuperheaters for domestic hot water heating
- Integration with building automation for optimal scheduling

## Ground Thermal Properties

Accurate characterization of subsurface thermal properties directly impacts ground loop sizing accuracy. Ground thermal conductivity varies by soil type, moisture content, and density.

**Thermal Conductivity Ranges:**
- Dry sand/gravel: 0.6-1.0 Btu/hr·ft·°F
- Moist sand/gravel: 1.2-1.8 Btu/hr·ft·°F
- Saturated sand/gravel: 1.5-2.2 Btu/hr·ft·°F
- Clay (dry to saturated): 0.5-1.5 Btu/hr·ft·°F
- Rock (granite, limestone): 1.8-3.5 Btu/hr·ft·°F
- Groundwater flow significantly increases effective conductivity

Thermal response testing (TRT) provides in-situ measurement of effective ground thermal conductivity and borehole thermal resistance. Testing involves circulating heated fluid through a test bore for 48-72 hours while monitoring temperature response.

**TRT Benefits:**
- Site-specific thermal conductivity measurement (±10% accuracy)
- Eliminates conservative safety factors from estimates
- Identifies high groundwater flow zones
- Optimizes loop design for project-specific conditions
- Typically cost-effective for projects >30 tons

Undisturbed ground temperature equals the annual average air temperature at depths below 15-20 ft. Shallow horizontal loops experience annual temperature variation, while vertical bores below 250 ft remain at constant temperature year-round.

Ground thermal diffusivity determines the rate of temperature change propagation and annual heat storage capacity. Higher diffusivity (rock, saturated soil) allows heat to dissipate faster from boreholes, improving long-term performance.
