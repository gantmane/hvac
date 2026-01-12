---
title: "Energy Resources"
description: "Comprehensive analysis of energy resources for HVAC systems including fossil fuels, electricity, and renewables with energy conversion efficiency, site vs source energy distinctions, and ASHRAE 90.1 compliance requirements"
weight: 6
---

HVAC system energy consumption accounts for 40-60% of total building energy use in commercial structures, making understanding energy resources critical for system design and optimization. Energy resource selection impacts equipment sizing, operating costs, environmental footprint, and compliance with energy codes including ASHRAE Standard 90.1 and the International Energy Conservation Code (IECC).

## Primary Energy Sources

HVAC systems utilize three categories of energy resources:

**Fossil Fuels**: Direct combustion of natural gas, propane, fuel oil, or coal for heating applications. Combustion releases chemical energy stored in hydrocarbon bonds through oxidation reactions. These sources provide high energy density and rapid heat release rates suitable for space heating, domestic hot water generation, and steam production.

**Electricity**: Generated from diverse sources including fossil fuel power plants, nuclear reactors, hydroelectric dams, wind turbines, and solar photovoltaic arrays. Electricity powers compressors, fans, pumps, and electric resistance heating elements. The electrical grid delivers alternating current at standardized voltages.

**Renewable Energy**: Solar thermal collectors, ground-source heat pumps, biomass combustion, and renewable electricity generation. These sources reduce dependence on fossil fuels and lower greenhouse gas emissions when properly implemented.

## Energy Content by Fuel Type

Energy content varies significantly across fuel types, affecting storage requirements, piping sizing, and combustion system design.

| Fuel Type | Higher Heating Value (HHV) | Lower Heating Value (LHV) | Typical Units |
|-----------|---------------------------|---------------------------|---------------|
| Natural Gas | 1,030 Btu/ft³ | 930 Btu/ft³ | Therms (100,000 Btu) |
| Propane (LPG) | 91,500 Btu/gal | 84,000 Btu/gal | Gallons |
| No. 2 Fuel Oil | 140,000 Btu/gal | 132,000 Btu/gal | Gallons |
| Electricity | 3,412 Btu/kWh | 3,412 Btu/kWh | Kilowatt-hours |
| Coal (Bituminous) | 24,000,000 Btu/ton | 23,000,000 Btu/ton | Tons |

Higher heating value includes latent heat of condensation from water vapor in combustion products. Lower heating value excludes this latent heat. Condensing boilers and furnaces recover latent heat, achieving efficiencies above 90% based on HHV.

## Site Energy vs Source Energy

**Site Energy** (delivered energy) represents energy consumed at the building boundary as measured by utility meters. This includes electricity, natural gas, fuel oil, and other delivered fuels. Site energy calculations determine operating costs and code compliance for prescriptive paths.

**Source Energy** (primary energy) accounts for all energy required to generate, transmit, and deliver energy to the building site. Source energy includes:

- Extraction and processing losses
- Power plant conversion efficiency
- Transmission and distribution losses
- Pipeline compression energy

The site-to-source conversion factor quantifies these upstream losses:

$$E_{source} = E_{site} \times F_{conv}$$

Where:
- $E_{source}$ = source energy (Btu)
- $E_{site}$ = site energy (Btu)
- $F_{conv}$ = site-to-source conversion factor (dimensionless)

Typical conversion factors per ASHRAE Standard 105:

| Energy Type | Site-to-Source Factor |
|-------------|----------------------|
| Electricity (US Grid) | 3.15 |
| Natural Gas | 1.09 |
| Fuel Oil | 1.19 |
| Propane | 1.15 |
| District Steam | 1.45 |
| District Chilled Water | 1.05 |

Electricity exhibits the highest site-to-source ratio due to thermal power plant efficiency limitations. Carnot cycle constraints limit fossil fuel power plants to 33-40% conversion efficiency, with additional 7-10% transmission losses.

## Energy Conversion Efficiency

Combustion efficiency for fossil fuel heating equipment:

$$\eta_{comb} = \frac{Q_{output}}{Q_{input}} = \frac{Q_{input} - Q_{loss}}{Q_{input}}$$

Where:
- $\eta_{comb}$ = combustion efficiency (decimal)
- $Q_{output}$ = useful heat output (Btu/hr)
- $Q_{input}$ = fuel energy input based on HHV (Btu/hr)
- $Q_{loss}$ = stack losses + jacket losses (Btu/hr)

Stack losses dominate combustion equipment inefficiency. Flue gas exits at elevated temperatures carrying sensible heat and latent heat from water vapor formed during combustion. Stack loss calculation:

$$Q_{stack} = \dot{m}_{fg} \times c_{p,fg} \times (T_{fg} - T_{amb}) + \dot{m}_{H_2O} \times h_{fg}$$

Where:
- $\dot{m}_{fg}$ = flue gas mass flow rate (lb/hr)
- $c_{p,fg}$ = specific heat of flue gas (Btu/lb·°F)
- $T_{fg}$ = flue gas temperature (°F)
- $T_{amb}$ = ambient temperature (°F)
- $\dot{m}_{H_2O}$ = water vapor mass flow rate (lb/hr)
- $h_{fg}$ = latent heat of vaporization (Btu/lb)

Non-condensing equipment typically achieves 78-84% steady-state efficiency. Condensing equipment recovers latent heat by cooling flue gases below the water vapor dew point (120-135°F for natural gas), achieving 90-98% efficiency based on HHV.

## Coefficient of Performance

Heat pumps and cooling equipment move thermal energy rather than converting fuel to heat, achieving efficiencies exceeding 100% when referenced to electric resistance heating.

$$COP = \frac{Q_{delivered}}{W_{input}}$$

Where:
- $COP$ = coefficient of performance (dimensionless)
- $Q_{delivered}$ = heating or cooling delivered (Btu/hr)
- $W_{input}$ = electrical power input (Btu/hr)

Carnot COP establishes theoretical maximum efficiency:

$$COP_{Carnot,heating} = \frac{T_H}{T_H - T_C}$$

$$COP_{Carnot,cooling} = \frac{T_C}{T_H - T_C}$$

Where $T_H$ and $T_C$ represent absolute temperatures (Rankine) of hot and cold reservoirs. Real equipment achieves 40-60% of Carnot efficiency due to compressor inefficiency, heat exchanger temperature differences, and pressure drops.

## ASHRAE Standard 90.1 Energy Cost Budget Method

The Energy Cost Budget (ECB) method in Appendix G compares proposed building energy cost against baseline building energy cost. This performance path requires:

1. Annual energy simulation using approved software (DOE-2, EnergyPlus, TRACE, eQUEST)
2. Baseline building configuration per prescriptive requirements
3. Proposed design energy cost ≤ baseline energy cost

Energy cost calculation:

$$C_{annual} = \sum_{i=1}^{n} (E_{i} \times R_{i})$$

Where:
- $C_{annual}$ = annual energy cost (\$)
- $E_{i}$ = annual consumption of energy type i (units)
- $R_{i}$ = energy rate for type i (\$/unit)
- $n$ = number of energy types

Fuel escalation rates and time-of-use pricing structures significantly impact lifecycle cost analysis. Natural gas prices exhibit seasonal variation with winter peaks in heating-dominated climates. Electricity demand charges penalize peak power draw independent of total consumption.

## Utility Rate Structures

Commercial and industrial electricity rates typically include:

**Energy Charges**: Cost per kWh consumed, often tiered by monthly consumption or time-of-use (on-peak, off-peak, shoulder periods)

**Demand Charges**: Cost per kW of maximum 15-minute or 30-minute average power draw during billing period. Demand charges incentivize load shifting and peak shaving strategies.

**Power Factor Penalties**: Charges for reactive power when power factor falls below 0.90-0.95. Inductive loads (motors, transformers) without power factor correction draw reactive current, increasing distribution system losses.

Natural gas rates structure includes:

**Commodity Charges**: Cost per therm or CCF (100 cubic feet) of gas consumed

**Transportation/Distribution Charges**: Fixed infrastructure costs

**Interruptible vs Firm Service**: Interruptible service offers lower rates but allows utility to curtail supply during peak demand. Dual-fuel capability (gas/oil) enables interruptible service for heating plants.

## Renewable Energy Integration

Solar thermal collectors convert solar radiation directly to thermal energy for domestic hot water preheating or space heating. Flat-plate collectors achieve 40-60% conversion efficiency. Evacuated tube collectors reach 60-75% efficiency with better performance at elevated temperatures and cold ambient conditions.

Ground-source heat pumps extract thermal energy from soil or groundwater, achieving heating COPs of 3.0-4.5. The ground acts as heat source during heating mode and heat sink during cooling mode. Soil temperature at depth remains relatively constant year-round (50-60°F in most US climates), providing favorable source/sink conditions compared to air-source equipment.

Photovoltaic systems generate electricity at 15-22% conversion efficiency for crystalline silicon modules. Building-integrated PV reduces purchased electricity but introduces intermittency requiring energy storage or grid connection for continuous operation.

## Energy Storage Systems

Thermal energy storage decouples HVAC equipment operation from building load, enabling load shifting to off-peak periods with lower electricity rates.

**Ice Storage**: Chillers operate overnight to freeze water in tanks. Ice melts during daytime cooling mode to satisfy building loads. Ice formation requires evaporator temperatures of 15-25°F, reducing chiller efficiency by 15-25% compared to conventional chilled water production.

**Chilled Water Storage**: Stratified storage tanks maintain cold water at bottom (42-45°F) and warm return water at top (54-58°F). Lower temperature lift compared to ice storage improves chiller efficiency.

**Phase Change Materials**: Eutectic salts or paraffin waxes with melting points of 45-75°F store latent heat at constant temperature during phase transition.

Storage capacity calculation:

$$Q_{storage} = m \times c_p \times \Delta T + m \times h_{fusion}$$

Where:
- $Q_{storage}$ = storage capacity (Btu)
- $m$ = storage medium mass (lb)
- $c_p$ = specific heat (Btu/lb·°F)
- $\Delta T$ = temperature change (°F)
- $h_{fusion}$ = latent heat of fusion for phase change materials (Btu/lb)

Economic analysis requires comparing capital cost premium for storage against energy cost savings from time-of-use rates. Simple payback periods typically range from 3-8 years depending on utility rate structure and chiller plant sizing.

## Carbon Intensity and Emissions

Greenhouse gas emissions vary by energy source based on carbon content and conversion efficiency. Carbon dioxide emissions factors:

| Energy Source | CO₂ Emissions Factor |
|---------------|---------------------|
| Natural Gas | 117 lb CO₂/MMBtu (site) |
| Propane | 139 lb CO₂/MMBtu (site) |
| No. 2 Fuel Oil | 163 lb CO₂/MMBtu (site) |
| Electricity (US Grid) | 390-850 lb CO₂/MWh (varies by region) |
| Coal | 210 lb CO₂/MMBtu (site) |

Grid electricity carbon intensity exhibits significant regional variation. Regions with high hydroelectric, nuclear, or renewable generation (Pacific Northwest, Northeast) demonstrate lower emission factors. Coal-dependent regions (Midwest, Southeast) show higher emission factors.

Annual emissions calculation:

$$M_{CO_2} = \sum_{i=1}^{n} (E_{i} \times EF_{i})$$

Where:
- $M_{CO_2}$ = annual CO₂ emissions (lb)
- $E_{i}$ = annual energy consumption of type i (units)
- $EF_{i}$ = emission factor for energy type i (lb CO₂/unit)

Building decarbonization initiatives prioritize electrification of heating systems combined with grid decarbonization through renewable energy expansion. Heat pump technology enables efficient electric heating superior to resistance heating while eliminating direct fossil fuel combustion emissions at the building site.
