---
title: "Emissions and Environmental Performance"
description: "Comprehensive analysis of CHP system emissions including NOx, CO, CO2, and particulate matter formation mechanisms, control technologies, emissions calculations, environmental benefits, air quality regulations, and permitting requirements for distributed generation."
date: 2026-01-04
weight: 7
---

CHP systems reduce overall emissions compared to separate generation of electricity and heat by improving fuel utilization efficiency. However, on-site combustion creates local air quality impacts requiring emissions control and regulatory compliance. Understanding emissions formation mechanisms, quantification methodologies, control technologies, and regulatory requirements enables proper system design and permitting.

## Carbon Dioxide Emissions and Climate Impact

Carbon dioxide emissions scale directly with fuel consumption and fuel carbon content. The emissions rate depends on fuel type and system efficiency:

$$\text{CO}_2 = Q_{fuel} \cdot EF_{CO_2} = \frac{W_{elec} + Q_{thermal}}{\eta_{CHP}} \cdot EF_{CO_2}$$

Where $EF_{CO_2}$ represents the fuel-specific emission factor. Natural gas combustion produces approximately 117 lb CO₂/MMBtu (LHV basis), while diesel fuel produces 161 lb CO₂/MMBtu.

For a 1 MW CHP system with 75% total efficiency operating 8000 hours per year on natural gas:

$$\text{CO}_2 = \frac{8000 \text{ MWh} \cdot 3.412 \text{ MMBtu/MWh}}{0.75} \cdot 117 \frac{\text{lb CO}_2}{\text{MMBtu}} = 4{,}260{,}000 \text{ lb CO}_2/\text{yr}$$

This equals 2130 tons CO₂ per year or 0.266 tons CO₂/MWh.

The environmental benefit derives from comparing CHP emissions to separate generation. The reference emissions equal grid electricity plus boiler fuel:

$$\text{CO}_{2,ref} = W_{elec} \cdot EF_{grid} + \frac{Q_{thermal}}{\eta_{boiler}} \cdot EF_{fuel,boiler}$$

Where $EF_{grid}$ represents grid electricity carbon intensity (typically 0.7-1.2 lb CO₂/kWh depending on generation mix) and $\eta_{boiler}$ represents displaced boiler efficiency.

For the previous example, assuming grid intensity of 1.0 lb CO₂/kWh, thermal output of 6000 MWh-thermal, and 80% boiler efficiency:

$$\text{CO}_{2,ref} = 8000 \cdot 1.0 \cdot 2000 + \frac{6000 \cdot 3.412}{0.80} \cdot 117/1{,}000{,}000 = 8000 + 2990 = 10{,}990 \text{ tons/yr}$$

The CHP reduces CO₂ emissions by 10,990 - 2,130 = 8,860 tons per year, a 81% reduction. The magnitude of reduction depends critically on grid carbon intensity and thermal utilization.

## Nitrogen Oxide Formation and Control

NOx forms through thermal, prompt, and fuel-bound mechanisms. Thermal NOx dominates in most combustion systems, forming through Zeldovich reactions at high temperatures:

$$\text{O} + \text{N}_2 \leftrightarrow \text{NO} + \text{N}$$
$$\text{N} + \text{O}_2 \leftrightarrow \text{NO} + \text{O}$$
$$\text{N} + \text{OH} \leftrightarrow \text{NO} + \text{H}$$

The formation rate exhibits exponential temperature dependence:

$$\frac{d[\text{NO}]}{dt} \propto e^{-69{,}090/T} \cdot [\text{O}_2]^{0.5} \cdot [\text{N}_2]$$

Where temperature T is in Kelvin. Peak NOx formation occurs at stoichiometric conditions (φ = 1.0) and maximum flame temperature.

Combustion modifications reduce NOx through temperature reduction and residence time control:

Lean premixed combustion operates with excess air (φ = 0.5-0.7), reducing peak temperature by 300-500K and suppressing NOx formation. Natural gas engines achieve 0.10-0.17 lb/MWh NOx through lean-burn without exhaust treatment.

Water or steam injection into gas turbines reduces flame temperature through evaporative cooling and increased thermal mass. Water injection rates of 0.5-2.0 times fuel mass flow reduce NOx by 50-80% but penalize efficiency through lost water/steam.

Staged combustion creates fuel-rich primary zones followed by fuel-lean secondary zones, limiting peak temperatures throughout the combustor. Dry low-NOx combustors in gas turbines achieve 25-60 ppmv (0.15-0.35 lb/MWh) through staged lean premixing.

Post-combustion NOx control through selective catalytic reduction (SCR) reduces emissions by 80-95%. The SCR injects ammonia or urea into exhaust upstream of a catalyst operating at 600-750°F:

$$4\text{NO} + 4\text{NH}_3 + \text{O}_2 \rightarrow 4\text{N}_2 + 6\text{H}_2\text{O}$$

$$2\text{NO}_2 + 4\text{NH}_3 + \text{O}_2 \rightarrow 3\text{N}_2 + 6\text{H}_2\text{O}$$

$$6\text{NO} + 4\text{NH}_3 \rightarrow 5\text{N}_2 + 6\text{H}_2\text{O}$$

Typical reduction efficiencies of 85-92% with ammonia slip below 5 ppm enable emissions of 0.03-0.07 lb/MWh for engines with raw emissions of 0.4-0.8 lb/MWh.

The SCR catalyst requires periodic replacement every 3-7 years depending on operating hours and exhaust conditions. Catalyst poisoning from silicon, phosphorus, or sulfur compounds accelerates degradation.

## Carbon Monoxide and Unburned Hydrocarbon Emissions

CO and unburned hydrocarbons result from incomplete combustion due to insufficient temperature, inadequate residence time, or improper air-fuel mixing. These emissions increase during startup, shutdown, and low-load operation when combustion temperatures decrease.

The CO oxidation rate depends exponentially on temperature:

$$\text{CO} + \text{OH} \rightarrow \text{CO}_2 + \text{H}$$

At temperatures below 1500K (2240°F), oxidation kinetics slow dramatically, allowing CO escape. Lean combustion with excess oxygen promotes CO oxidation but may reduce temperature below kinetic limits.

Oxidation catalysts convert CO and hydrocarbons to CO₂ and H₂O when exhaust temperature exceeds 450-500°F:

$$2\text{CO} + \text{O}_2 \rightarrow 2\text{CO}_2$$

$$\text{C}_x\text{H}_y + \left(x + \frac{y}{4}\right)\text{O}_2 \rightarrow x\text{CO}_2 + \frac{y}{2}\text{H}_2\text{O}$$

Conversion efficiencies of 90-98% reduce emissions below 0.1 lb/MWh for both CO and total hydrocarbons. Platinum-palladium catalysts operate effectively on lean exhaust from engines and turbines.

Three-way catalysts on stoichiometric engines simultaneously reduce NOx and oxidize CO/hydrocarbons within a narrow air-fuel ratio window (λ = 0.99-1.01). Oxygen storage materials (ceria-zirconia) buffer short-term excursions, maintaining high conversion efficiency.

## Particulate Matter Emissions

Natural gas combustion produces minimal particulate matter due to negligible fuel-bound ash and sulfur. Emissions typically remain below 0.01 lb/MWh without control equipment.

Diesel and fuel oil combustion generates substantial particulate from incomplete combustion of heavy hydrocarbons and fuel ash content. Raw emissions range from 0.1-0.5 lb/MWh depending on fuel quality and combustion conditions.

Diesel particulate filters (DPF) capture particulate matter through ceramic wall-flow filters with 85-95% collection efficiency. The accumulated particulate undergoes periodic regeneration through high-temperature oxidation (>1000°F) using fuel burners or electrical heaters.

Biogas and landfill gas engines may produce particulates from siloxane combustion. Silicon compounds in biogas oxidize to silicon dioxide that deposits on valves, spark plugs, and exhaust components. Siloxane removal upstream of the engine (activated carbon or refrigeration) prevents particulate formation.

## Sulfur Dioxide and Acid Gas Emissions

Natural gas contains minimal sulfur (typically <1 ppm), producing negligible SO₂ emissions. Pipeline specifications limit total sulfur to prevent odourant levels from causing emissions issues.

Biogas from wastewater treatment and landfills contains hydrogen sulfide (H₂S) requiring removal before combustion. H₂S oxidizes to SO₂:

$$\text{H}_2\text{S} + \frac{3}{2}\text{O}_2 \rightarrow \text{SO}_2 + \text{H}_2\text{O}$$

Desulfurization through activated carbon, iron sponge, or biological systems reduces H₂S below 100-200 ppm to prevent corrosion and minimize SO₂ emissions.

Diesel fuel sulfur content (15-500 ppm depending on fuel grade) produces SO₂ emissions proportional to fuel consumption. Ultra-low sulfur diesel (ULSD) with <15 ppm sulfur minimizes SO₂ and enables emission control catalysts.

## Emissions Permitting and Regulatory Compliance

CHP installations require air quality permits addressing both construction and operation. Permitting requirements depend on facility location, emissions levels, and existing permit status.

Minor source permits apply when total facility emissions remain below major source thresholds (typically 100 tons/year of any criteria pollutant or 10/25 tons/year of hazardous air pollutants). Minor source permitting involves:

- Emissions calculations demonstrating below-threshold operation
- Best available control technology (BACT) determination for significant emission units
- Air dispersion modeling for certain pollutants and locations
- Public notice and comment period (jurisdiction-dependent)

Major source permits (Title V) require comprehensive permitting for facilities exceeding major source thresholds. Title V permits involve:

- Detailed emissions inventory for all sources
- BACT analysis and implementation
- Continuous emissions monitoring or periodic testing
- Annual compliance certifications
- Enhanced monitoring and recordkeeping

Prevention of Significant Deterioration (PSD) applies to major modifications at major sources or new major sources in attainment areas. PSD review requires:

- Best available control technology analysis
- Air quality impact analysis
- Additional impacts analysis (visibility, soils, vegetation)
- Class I area analysis for facilities near national parks

Emissions calculation methodologies for permitting use vendor-guaranteed emissions rates, emissions testing data, or EPA emission factors. Conservative assumptions ensure permit compliance under all operating conditions.

Stack testing verifies emissions performance, typically required during commissioning and periodically (annually or semi-annually) thereafter. Test methods vary by pollutant:

- EPA Method 19 for NOx, CO, CO₂ from combustion sources
- EPA Method 25A for total hydrocarbons
- EPA Method 5 for particulate matter
- Continuous emissions monitoring systems (CEMS) for NOx and CO on larger units

## Noise and Other Environmental Impacts

CHP systems generate noise from combustion, mechanical equipment, cooling fans, and exhaust. Reciprocating engines produce 95-105 dBA at 3 feet, while gas turbines generate 100-110 dBA. Acoustic enclosures reduce noise by 20-35 dBA, enabling compliance with typical industrial limits of 70-80 dBA at property lines.

Thermal discharge from radiator cooling can affect local air temperatures and create visible plumes in cold weather. Water-cooled systems discharge heat to cooling towers or evaporative condensers with minimal thermal impact but consuming water through evaporation.

Visual impact considerations include exhaust stacks (typically 20-60 feet high for adequate dispersion), cooling tower plumes, and equipment installations. Facility siting should consider visual impacts on adjacent properties and screening vegetation or architectural features.
