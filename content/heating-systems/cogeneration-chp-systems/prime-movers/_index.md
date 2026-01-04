---
title: "Prime Movers for CHP Applications"
description: "Comprehensive comparison and analysis of prime mover technologies for combined heat and power including reciprocating engines, gas turbines, steam turbines, microturbines, and fuel cells with performance characteristics, heat recovery potential, and selection criteria."
date: 2026-01-04
weight: 2
---

Prime movers convert fuel chemical energy to mechanical shaft power, which drives electrical generators while producing recoverable thermal energy. The selection of prime mover technology fundamentally determines CHP system performance, economics, and applicability. Each technology exhibits distinct characteristics regarding capacity range, efficiency, heat recovery temperature, emissions, fuel flexibility, and capital cost.

## Technology Comparison Overview

The following table summarizes key performance parameters across prime mover technologies:

| Technology | Capacity Range | Electrical Efficiency | Heat Recovery Temp | Exhaust Mass Flow | Part-Load Performance | Typical Applications |
|------------|---------------|---------------------|-------------------|------------------|---------------------|---------------------|
| Gas Engine | 100 kW - 10 MW | 35-42% | 400-500°C exhaust<br>90-95°C jacket | Moderate | Good (linear) | Commercial, institutional, industrial |
| Diesel Engine | 200 kW - 20 MW | 38-45% | 350-450°C exhaust<br>90-95°C jacket | Moderate | Excellent | Backup power, remote sites, marine |
| Gas Turbine | 1 MW - 300 MW | 25-42% | 450-600°C | Very high | Poor | Large facilities, industrial, utilities |
| Steam Turbine | 500 kW - 300 MW | 15-35% | Varies by config | N/A | Good | Industrial processes, waste heat |
| Microturbine | 30 kW - 300 kW | 26-33% | 250-300°C | Low | Fair | Small commercial, distributed |
| PAFC Fuel Cell | 200 kW - 2 MW | 40-42% | 200°C | Very low | Excellent | Premium power quality |
| MCFC Fuel Cell | 300 kW - 3 MW | 47-50% | 400-650°C | Very low | Good | Large commercial, industrial |
| SOFC Fuel Cell | 100 kW - 2 MW | 50-60% | 600-1000°C | Very low | Good | High efficiency applications |

## Thermodynamic Cycle Fundamentals

Reciprocating engines operate on the Otto cycle (spark ignition) or Diesel cycle (compression ignition). Both cycles involve intake, compression, combustion, expansion, and exhaust. The theoretical thermal efficiency of the Otto cycle depends on compression ratio:

$$\eta_{Otto} = 1 - \frac{1}{r^{\gamma-1}}$$

Where $r$ represents compression ratio (typically 10-12 for natural gas engines) and $\gamma$ represents the specific heat ratio (approximately 1.4 for air). Actual engine efficiency is lower due to irreversibilities, heat transfer, and incomplete combustion.

Gas turbines operate on the Brayton cycle, involving compression, combustion, and expansion. The ideal cycle efficiency depends on the pressure ratio:

$$\eta_{Brayton} = 1 - \frac{1}{\pi_r^{(\gamma-1)/\gamma}}$$

Where $\pi_r$ represents pressure ratio (typically 10-40 for industrial gas turbines). Real gas turbines incorporate component efficiencies for the compressor, combustion chamber, and turbine.

Steam turbines operate on the Rankine cycle when coupled with a boiler, or extract work from process steam. The Rankine cycle efficiency depends on boiler pressure, superheat temperature, and condenser pressure:

$$\eta_{Rankine} = \frac{h_1 - h_2}{h_1 - h_3}$$

Where $h_1$ represents turbine inlet enthalpy, $h_2$ represents turbine exhaust enthalpy, and $h_3$ represents feedwater enthalpy. Back-pressure steam turbines sacrifice electrical efficiency for thermal recovery.

Fuel cells operate on electrochemical principles rather than thermodynamic cycles. The maximum theoretical efficiency derives from the Gibbs free energy rather than the Carnot limit:

$$\eta_{FC,max} = \frac{\Delta G}{\Delta H}$$

Where $\Delta G$ represents Gibbs free energy change and $\Delta H$ represents enthalpy change. For hydrogen oxidation at 25°C, this ratio equals 0.83, explaining fuel cells' ability to exceed Carnot efficiency for low-temperature heat engines.

## Heat Recovery Characteristics

Each prime mover produces thermal energy at different temperatures and in different forms, affecting heat recovery system design and utility integration.

Reciprocating engines generate multiple thermal streams: high-temperature exhaust gas (400-500°C), engine jacket cooling water (90-95°C), lubricating oil cooling (60-70°C), and intercooler heat rejection (40-60°C). The exhaust stream provides approximately 30-40% of fuel input as recoverable thermal energy at temperatures suitable for steam generation or absorption cooling. Jacket water provides an additional 20-30% at lower temperatures suitable for space heating and domestic hot water.

Gas turbines produce a single high-temperature, high-mass-flow exhaust stream (450-600°C). This exhaust contains 50-65% of fuel input as recoverable thermal energy. The high temperature and flow rate suit high-pressure steam generation through heat recovery steam generators (HRSG). Combined cycle configurations add a steam turbine to extract additional electrical work from recovered thermal energy.

Steam turbines can be configured for varying levels of thermal recovery. Back-pressure turbines exhaust at elevated pressure (15-150 psig) for process use, maximizing thermal recovery at the expense of electrical output. Extraction turbines allow steam withdrawal at intermediate pressures. Condensing turbines maximize electrical generation but provide minimal useful thermal energy.

Microturbines use recuperators to preheat combustion air with exhaust energy, improving electrical efficiency. The recuperator outlet (250-300°C) provides the available thermal recovery. Some designs incorporate water-cooled intercoolers, providing additional low-temperature heat recovery.

Fuel cells produce high-quality thermal energy from electrochemical inefficiencies and reaction heat. High-temperature fuel cells (MCFC, SOFC) deliver thermal energy at temperatures suitable for high-pressure steam or gas turbine integration. Low-temperature fuel cells (PAFC, PEMFC) provide lower-temperature heat suitable for hot water or low-pressure steam.

## Fuel Flexibility Considerations

Natural gas represents the dominant CHP fuel due to availability, cost, cleanliness, and infrastructure. All prime mover technologies can operate on natural gas, though specific modifications may be required for varying gas quality.

Diesel fuel and fuel oil enable operation at sites without natural gas service. Diesel engines operate efficiently on liquid fuels, while dual-fuel engines can switch between gas and liquid fuels. Gas turbines require fuel oil specifications compatible with atomization and combustion systems.

Biogas from anaerobic digestion, landfills, or wastewater treatment provides renewable fuel for CHP systems. The lower heating value (typically 600-700 Btu/scf versus 1000 Btu/scf for natural gas) and presence of contaminants (hydrogen sulfide, siloxanes, moisture) require equipment modifications. Reciprocating engines and fuel cells tolerate biogas with appropriate cleanup.

Syngas from gasification of coal, biomass, or waste materials can fuel CHP systems. The low heating value (150-300 Btu/scf) and presence of tars, particulates, and sulfur compounds necessitate extensive gas cleanup and engine derating. Fuel cells require particularly clean gas to avoid poisoning electrocatalysts.

Hydrogen and hydrogen blends represent emerging fuel options as hydrogen infrastructure develops. Fuel cells operate directly on hydrogen with zero carbon emissions. Reciprocating engines and gas turbines require modifications to address hydrogen's high flame speed, wide flammability limits, and reduced volumetric energy density.

## Part-Load Performance

CHP systems frequently operate at part load due to varying facility demands, scheduled maintenance, and equipment cycling. Part-load performance characteristics significantly affect annual energy production and economics.

Reciprocating engines exhibit relatively flat efficiency curves down to 50% load, with efficiency degradation of only 2-4 percentage points from full load to half load. Below 50% load, efficiency decreases more rapidly. This characteristic enables effective load-following operation.

Gas turbines experience substantial efficiency penalties at part load, with simple cycle units losing 5-10 percentage points of efficiency at 50% load. The efficiency degradation results from increased combustion temperature at reduced flow, lower component efficiencies at off-design conditions, and increased auxiliary power fractions. Combined cycle plants mitigate part-load penalties through sliding-pressure HRSG operation and sophisticated controls.

Steam turbines maintain good efficiency at part load when operating in extraction or back-pressure modes with varying steam demands. Condensing turbines sacrifice efficiency when operating at reduced load with fixed condenser pressure.

Microturbines incorporate variable-speed operation and recuperators that partially compensate for part-load efficiency losses. Efficiency typically decreases 3-5 percentage points from full load to 50% load.

Fuel cells exhibit excellent part-load characteristics, maintaining nearly constant efficiency from 100% to 30% load. This flat efficiency curve makes fuel cells particularly suitable for variable loads and load-following applications.

## Emissions Characteristics

Prime mover emissions depend on combustion temperature, air-fuel ratio, fuel composition, and emission control technologies.

Natural gas reciprocating engines produce low emissions through lean-burn or stoichiometric combustion with three-way catalysts. Lean-burn engines achieve NOx levels of 0.07-0.15 lb/MWh without exhaust treatment. Stoichiometric engines with catalysts reach sub-0.07 lb/MWh NOx. Carbon monoxide emissions range from 0.1-0.3 lb/MWh with catalytic oxidation.

Gas turbines inherently produce higher NOx due to elevated combustion temperatures. Dry low-NOx (DLN) combustors achieve 0.15-0.35 lb/MWh NOx through lean premixed combustion. Selective catalytic reduction (SCR) systems reduce NOx below 0.05 lb/MWh when stringent limits apply. CO emissions typically remain below 0.1 lb/MWh.

Fuel cells produce minimal criteria pollutant emissions since combustion occurs only in fuel processing (for non-hydrogen fuels). NOx emissions below 0.01 lb/MWh are typical. Carbon monoxide and unburned hydrocarbons are negligible. The low emissions enable siting in environmentally sensitive areas.

## Selection Methodology

Prime mover selection considers multiple interdependent factors. A systematic evaluation process examines:

1. Capacity requirements based on facility electrical and thermal loads
2. Power-to-heat ratio matching between prime mover output and facility demands
3. Heat recovery temperature requirements for facility thermal applications
4. Fuel availability, costs, and contractual constraints
5. Site characteristics including space, noise limits, and emission regulations
6. Reliability requirements and maintenance capabilities
7. Capital budget and project economics
8. Operating profile and capacity factor expectations

No single technology optimizes all criteria. Reciprocating engines provide the most versatile balance of efficiency, cost, and operational flexibility for facilities in the 100 kW to 5 MW range. Gas turbines dominate above 5 MW where their economies of scale and high-temperature heat recovery justify lower electrical efficiency. Fuel cells suit applications prioritizing efficiency, emissions, and power quality over capital cost.
