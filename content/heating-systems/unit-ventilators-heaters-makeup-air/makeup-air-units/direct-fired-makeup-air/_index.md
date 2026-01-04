---
title: "Direct-Fired Makeup Air Units"
description: "Technical guide to direct-fired makeup air systems with combustion products in supply air, efficiency analysis, CO2 dilution calculations, and code requirements."
date: "2026-01-04"
weight: 2
tags: ["direct fired makeup air", "100% efficiency heating", "combustion products airstream", "warehouse makeup air", "industrial ventilation", "direct gas fired"]
categories: ["Heating Systems"]
---

Direct-fired makeup air units achieve 90-100% thermal efficiency by burning fuel directly in the supply airstream without heat exchangers separating combustion products from conditioned air. The combustion products (CO₂, water vapor, and nitrogen) mix with outdoor air, diluting to concentrations acceptable for most industrial and warehouse applications. This configuration eliminates the 15-20% efficiency penalty of indirect-fired units while reducing equipment size and first cost.

## Operating Principles

Conventional indirect-fired heating separates combustion products from supply air using heat exchangers. Flue gas temperatures of 300-500°F represent lost energy, reducing system efficiency to 80-85%. Direct-fired burners eliminate this loss by mixing all combustion heat directly into the supply airstream.

The energy balance for direct-fired combustion:

$$Q_{useful} = \dot{m}_{fuel} \times \text{HHV} \times \eta_{combustion}$$

where combustion efficiency ($\eta_{combustion}$) reaches 95-100% with proper air-fuel ratio control. For natural gas at 1,020 Btu/ft³ (higher heating value) and 98% combustion efficiency:

$$Q_{useful} = \dot{V}_{gas} \times 1020 \times 0.98$$

A unit consuming 500 ft³/hr natural gas delivers:

$$Q_{useful} = 500 \times 1020 \times 0.98 = 499,800 \text{ Btu/hr}$$

Only 2% losses occur from incomplete combustion. The remaining 98% heats supply air directly.

## Combustion Products and Dilution

Stoichiometric combustion of methane (primary natural gas component) follows:

$$\text{CH}_4 + 2\text{O}_2 + 7.52\text{N}_2 \rightarrow \text{CO}_2 + 2\text{H}_2\text{O} + 7.52\text{N}_2$$

Per cubic foot of natural gas burned with theoretical air:
- 1.0 ft³ CO₂ produced
- 2.0 ft³ H₂O produced (as steam)
- 9.52 ft³ total combustion products

Practical burners operate with 10-20% excess air for complete combustion, increasing total products to 10.5-11.5 ft³ per ft³ fuel.

The concentration of combustion products in supply air depends on airflow rate:

$$\text{CO}_2\text{ (ppm)} = \frac{\dot{V}_{gas} \times 10^6}{\text{CFM} \times 60}$$

For 500 ft³/hr gas consumption with 10,000 CFM supply:

$$\text{CO}_2 = \frac{500 \times 10^6}{10,000 \times 60} = 833 \text{ ppm}$$

ASHRAE 62.1 establishes 1,000 ppm as the indoor CO₂ threshold for acceptable IAQ (700 ppm above outdoor ambient of 400 ppm). Direct-fired units typically add 600-900 ppm depending on sizing, operating near but below code limits.

## Moisture Addition

Combustion produces water vapor at 2 ft³ per ft³ fuel (approximately 0.12 lbs H₂O per ft³ gas). This moisture enters the space, increasing humidity levels.

For the 500 ft³/hr example:

$$\dot{m}_{H_2O} = 500 \times 0.12 = 60 \text{ lbs/hr}$$

With 10,000 CFM airflow at 70°F and 30% RH (moisture content = 0.0047 lbs/lb dry air):

Existing moisture flow:

$$\dot{m}_{existing} = 10,000 \times 60 \times 0.075 \times 0.0047 = 211 \text{ lbs/hr}$$

Total moisture with combustion:

$$\dot{m}_{total} = 211 + 60 = 271 \text{ lbs/hr}$$

New moisture ratio:

$$W_{new} = \frac{271}{10,000 \times 60 \times 0.075} = 0.0060 \text{ lbs/lb}$$

This represents approximately 40% RH at 70°F, acceptable for most industrial spaces. Cold-climate applications benefit from humidification preventing excessively dry conditions that plague indirect-fired systems.

## Efficiency Comparison

Direct-fired units achieve superior energy performance compared to indirect alternatives:

| System Type | Thermal Efficiency | Annual Energy (MMBtu) | Annual Cost ($0.80/therm) |
|-------------|-------------------|----------------------|---------------------------|
| Direct-Fired | 95-98% | 1,050 | $8,400 |
| Indirect-Fired | 80-85% | 1,250 | $10,000 |
| Electric Resistance | 100% (site) | 1,025 MMBtu equivalent | $30,000 (at $0.10/kWh) |

The 16% efficiency improvement of direct-fired over indirect-fired translates to annual savings of $1,600 for a typical 1 MMBtu/year makeup air heating load.

## Burner Configuration

Direct-fired burners position flame and combustion zone directly in the airstream. Three common designs:

### In-Duct Burners

Linear burner assemblies mount perpendicular to airflow within rectangular or round ducts. Gas injectors and ignition electrodes distribute across the duct width, creating uniform heating patterns. Airflow velocities of 1,500-2,500 FPM through the burner section ensure proper air-fuel mixing and complete combustion.

### Diffusion Burners

Multiple small flames distribute across the air stream. Each burner nozzle receives gas and combustion air, creating individual flames. The array provides redundancy (single burner failure doesn't disable the system) and uniform temperature profiles.

### Premix Burners

Fuel and combustion air mix upstream of ignition, producing low-NOx flames through lean premix combustion. These burners achieve NOx emissions below 20 ppm (at 3% O₂) compared to 40-80 ppm for diffusion burners. Additional cost of $2,000-5,000 is justified in areas with strict air quality regulations.

## Safety Controls

Direct-fired units require comprehensive safety systems preventing hazardous conditions:

### Flame Safeguard System

Electronic controls supervise burner ignition, operation, and shutdown:

1. **Pre-purge**: Fan operates 30-60 seconds before ignition, clearing any fuel accumulation
2. **Spark ignition**: High-voltage spark ignites gas while flame sensor monitors for flame establishment
3. **Flame proving**: UV scanner or flame rod confirms combustion within 4-10 seconds
4. **Normal operation**: Continuous flame monitoring with 1-4 second response to flame loss
5. **Lockout on failure**: System requires manual reset after ignition failure or flame loss

Modern systems use microprocessor-based controls providing diagnostic information and self-testing capabilities.

### Airflow Proving

Differential pressure switches or airflow measurement stations prove adequate air velocity through burners before gas valve opening. Typical setpoints require 0.2-0.5 inches water gauge differential across the burner section.

Loss of airflow signal immediately closes gas valves and initiates shutdown sequence, preventing fuel accumulation.

### High Limit Temperature

Downstream temperature sensors (6-12 feet after burner section) monitor discharge air. Limits typically set at 140-180°F prevent overheating from control failures or low airflow conditions.

Manual reset limits require technician intervention after high-temperature events, preventing automatic restart of malfunctioning equipment.

### Low Gas Pressure Switch

Gas pressure switches prove adequate fuel pressure (typically 4-14 inches water column for natural gas) before allowing ignition. Low pressure causes incomplete combustion and potential flame instability.

## Application Limitations

Direct-fired makeup air suits specific applications. Code restrictions and IAQ requirements limit use:

### Acceptable Applications

- **Warehouses and distribution centers**: Large airflow rates adequately dilute combustion products
- **Manufacturing facilities**: Industrial processes tolerate elevated CO₂ and moisture
- **Aircraft hangars**: High ceilings and large volumes enable dilution
- **Loading docks**: Intermittent operation with large outdoor air quantities
- **Agricultural buildings**: Livestock facilities benefit from moisture addition

### Prohibited or Restricted Applications

- **Healthcare facilities**: ASHRAE 170 prohibits combustion products in supply air
- **Laboratories**: Fume hood exhaust may recirculate combustion products, affecting experiments
- **Food processing**: Moisture addition and combustion products risk product contamination
- **Residential buildings**: IAQ requirements and code restrictions typically prohibit direct-fired systems
- **Schools and offices**: Most codes require indirect-fired heating for occupied comfort spaces

Local building codes provide specific requirements. AHJ approval is mandatory before specifying direct-fired equipment for any occupied space application.

## Sizing Methodology

Direct-fired unit sizing balances heating capacity against acceptable combustion product concentrations:

$$\text{CFM}_{min} = \frac{\dot{V}_{gas,max} \times 10^6}{\text{CO}_2\text{limit(ppm)} \times 60}$$

For a maximum gas input of 1,000 ft³/hr and CO₂ limit of 800 ppm:

$$\text{CFM}_{min} = \frac{1000 \times 10^6}{800 \times 60} = 20,833 \text{ CFM}$$

This minimum airflow requirement may exceed the airflow needed for building pressurization, forcing oversized makeup air systems in tight buildings with limited exhaust.

Temperature rise check:

$$\Delta T = \frac{\dot{V}_{gas} \times \text{HHV} \times \eta}{\text{CFM} \times 1.08}$$

$$\Delta T = \frac{1000 \times 1020 \times 0.98}{20,833 \times 1.08} = 44.5°F$$

For 0°F outdoor air, discharge temperature reaches 44.5°F, adequate for tempered makeup air applications but insufficient for fully heated systems.

## Venting and Combustion Air

Direct-fired units require combustion air from outdoors or the conditioned space. The combustion air volume approximates:

$$\text{CFM}_{combustion} = \dot{V}_{gas} \times 10 \text{ to } 12$$

For 1,000 ft³/hr gas rate:

$$\text{CFM}_{combustion} = \frac{1000}{60} \times 11 = 183 \text{ CFM}$$

When drawing combustion air from indoors, this reduces available makeup air by the combustion air quantity. Outdoor combustion air eliminates this penalty but requires additional ductwork and draft controls.

Direct-fired units produce no flue gases requiring venting. All combustion products enter the supply air, eliminating vent systems and associated costs.

## Maintenance Requirements

Direct-fired systems require periodic maintenance:

- **Burner inspection**: Annual cleaning of ignition electrodes, flame sensors, and gas orifices
- **Combustion analysis**: Verify proper air-fuel ratio and low CO emissions (under 50 ppm)
- **Flame sensor testing**: Confirm rapid response to flame presence/absence
- **Gas train inspection**: Check valve sealing, pressure regulation, and safety shutoffs
- **Air filter replacement**: Quarterly to monthly depending on outdoor air quality

Maintenance costs run approximately $500-1,200 annually for commercial units, comparable to indirect-fired systems.

Direct-fired makeup air units provide the most energy-efficient heating method for 100% outdoor air applications in industrial and warehouse environments. The 90-100% thermal efficiency, reduced equipment size, and eliminated venting requirements deliver first cost and operating cost advantages over indirect alternatives when application constraints permit combustion products in supply air.
