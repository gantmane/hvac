---
title: "Combustion Gas Turbines for CHP"
description: "Comprehensive engineering analysis of gas turbine prime movers including microturbines, Brayton cycle thermodynamics, electrical efficiency optimization, heat recovery steam generation, inlet air cooling, part-load performance, emissions control, and maintenance requirements for cogeneration applications."
date: 2026-01-04
weight: 2
---

Combustion gas turbines convert fuel energy to mechanical shaft power through continuous-flow compression, combustion, and expansion processes. These machines dominate CHP applications above 5 MW capacity, with industrial gas turbines reaching over 300 MW in combined cycle configurations. The high-temperature, high-mass-flow exhaust makes gas turbines particularly suitable for steam generation and combined cycle operation, achieving overall efficiencies exceeding 80%. Microturbines extend gas turbine technology down to 30 kW, providing distributed generation for commercial buildings and small industrial facilities.

## Gas Turbine Size Classes and Applications

Gas turbines span four distinct size categories, each optimized for specific CHP applications:

**Microturbines (30-500 kW)** employ single-stage radial compressors and turbines with recuperators to preheat combustion air using exhaust heat. Electrical efficiency ranges from 26-33%, with 90-95% exhaust energy available for thermal recovery. The compact footprint and low weight (50-100 lb/kW) suit building-integrated applications. Air bearings eliminate oil lubrication and reduce maintenance. High-speed operation (50,000-120,000 rpm) requires power electronics to convert generator output to grid frequency.

**Small Industrial Turbines (0.5-10 MW)** use multi-stage axial compressors with pressure ratios of 10-18 and achieve 28-35% simple cycle efficiency. These units provide the primary capacity range for industrial CHP, matching thermal loads of manufacturing facilities, universities, and hospitals. Package systems integrate the turbine, generator, controls, and auxiliary equipment in weather-resistant enclosures.

**Intermediate Industrial Turbines (10-50 MW)** operate at 30-38% simple cycle efficiency with pressure ratios of 15-25. The increased firing temperatures (1250-1400°C) and improved component efficiencies justify the higher complexity and cost. These turbines typically serve large industrial complexes, district energy systems, and power generation facilities with substantial thermal loads.

**Large Frame Turbines (50-300+ MW)** achieve 38-42% simple cycle and 55-62% combined cycle efficiency. Advanced aerodynamics, single-crystal turbine blades, and sophisticated cooling systems enable firing temperatures approaching 1500°C. While primarily utility-scale, these machines serve large petrochemical complexes and industrial sites requiring major electrical and thermal outputs.

## Brayton Cycle Thermodynamics

Gas turbines operate on the Brayton cycle, consisting of isentropic compression, constant-pressure heat addition, isentropic expansion, and constant-pressure heat rejection. The ideal cycle efficiency depends solely on pressure ratio:

$$\eta_{Brayton} = 1 - \frac{1}{\pi_r^{(\gamma-1)/\gamma}}$$

Where $\pi_r$ represents compressor pressure ratio and $\gamma$ equals approximately 1.4 for air. A gas turbine with pressure ratio of 15 achieves theoretical efficiency of:

$$\eta_{Brayton} = 1 - \frac{1}{15^{0.286}} = 0.465 \text{ or } 46.5\%$$

Real gas turbines achieve lower efficiency due to component inefficiencies, combustor pressure loss, and mechanical losses. The actual efficiency can be expressed as:

$$\eta_{actual} = \eta_{ideal} \cdot \eta_{compressor} \cdot \eta_{turbine} \cdot \eta_{combustor} \cdot \eta_{mechanical}$$

With component efficiencies: compressor 85-90%, turbine 88-92%, combustor 99%, mechanical 98-99%. These losses reduce actual simple cycle efficiency to 25-42% depending on size and technology level.

The specific work output (work per unit mass flow) increases with both pressure ratio and turbine inlet temperature:

$$w_{net} = c_p T_1 \left[\pi_r^{(\gamma-1)/\gamma}(r_t - 1) - (\pi_r^{(\gamma-1)/\gamma} - 1)\right]$$

Where $r_t$ represents the ratio of turbine inlet to compressor inlet temperature. Higher firing temperatures enable greater specific work, allowing smaller turbines for the same power output. Modern industrial gas turbines achieve firing temperatures of 1200-1500°C (2200-2700°F) using advanced materials and cooling technologies.

## Electrical Efficiency Characteristics

Simple cycle electrical efficiency varies significantly with turbine size and technology generation. The fundamental constraints limiting efficiency include:

**Compressor Work Requirements**: The compressor consumes 50-70% of turbine gross output. Each percentage point improvement in compressor efficiency increases net output by 2-3 percentage points. Axial compressors achieve 88-92% polytropic efficiency in large industrial turbines, while microturbine radial compressors reach 75-82% efficiency.

**Turbine Inlet Temperature**: Each 50°C increase in firing temperature improves simple cycle efficiency by approximately 2 percentage points. Material limitations constrain turbine inlet temperature. Single-crystal superalloy blades with thermal barrier coatings and sophisticated film cooling enable operation with gas temperatures 150-200°C above blade metal temperatures.

**Cooling Air Penalties**: Turbine cooling requires 10-25% of compressor discharge air, reducing work-producing mass flow through the turbine. Advanced cooling techniques including impingement cooling, serpentine passages, and film cooling minimize cooling air requirements while protecting hot section components.

**Mechanical and Generator Losses**: Bearings, seals, and oil pumps consume 1-2% of gross output. Generator losses add another 1-2%. High-speed generators in microturbines require power electronics, introducing 3-5% conversion losses.

Recuperated microturbines improve efficiency by preheating combustion air using exhaust heat. The recuperator effectiveness (typically 85-90%) determines the temperature rise:

$$T_{3} = T_{2} + \varepsilon(T_{5} - T_{2})$$

Where $T_3$ is combustion air inlet temperature, $T_2$ is compressor discharge temperature, $T_5$ is turbine exhaust temperature, and $\varepsilon$ is recuperator effectiveness. This preheating reduces fuel input by 30-40%, improving efficiency from 18-22% (non-recuperated) to 26-33% (recuperated).

## Component Design and Performance

The axial-flow compressor comprises 10-20 stages of rotating and stationary airfoils. Each stage increases pressure by 10-25%, with cumulative pressure ratios of 10-40. Compressor efficiency critically affects overall performance since compression work typically consumes 50-70% of turbine work output.

Compressor surge represents a fundamental operating limitation. At low flow rates or high pressure ratios, flow separation causes reversed flow and violent pressure oscillations. The surge line defines the minimum stable flow at each speed. Modern compressors incorporate variable inlet guide vanes and variable stator vanes to extend the operating range and prevent surge during startup and part-load operation.

The combustion chamber burns fuel at nearly constant pressure, raising temperature to the maximum allowable turbine inlet temperature. Combustor design balances complete combustion, low emissions, and combustor liner durability. Dry low-NOx (DLN) combustors premix fuel and air in lean mixtures (φ = 0.5-0.6) to reduce peak flame temperature and NOx formation. The lean premixed approach requires careful control to prevent flashback (upstream flame propagation) and combustion instability.

The turbine extracts energy from the high-temperature, high-pressure gas through 2-5 expansion stages. The first stage experiences the highest thermal and mechanical stresses, requiring advanced nickel-based superalloys or ceramic matrix composites. Internal air cooling, thermal barrier coatings, and film cooling enable operation with gas temperatures exceeding metal melting points.

## Exhaust Heat Recovery Systems

Gas turbine exhaust contains 50-65% of fuel input energy at temperatures of 450-600°C (840-1110°F), providing exceptional heat recovery potential. The high temperature enables high-pressure steam generation and supports absorption cooling or industrial process heat. Microturbines produce exhaust at 260-320°C (500-610°F), suitable for low-pressure steam, hot water, or direct process heating.

A heat recovery steam generator (HRSG) extracts thermal energy from turbine exhaust to produce steam. The HRSG typically incorporates multiple pressure levels (single, dual, or triple pressure) to maximize heat recovery across the exhaust temperature range.

The recoverable thermal energy follows from the exhaust mass flow and temperature:

$$Q_{recovery} = \dot{m}_{exh} \cdot c_p \cdot (T_{exh,in} - T_{stack})$$

For a 5 MW gas turbine with 50,000 lb/hr exhaust at 950°F, cooling to 300°F stack temperature yields:

$$Q_{recovery} = 50000 \cdot 0.26 \cdot (950 - 300) = 8.45 \text{ MMBtu/hr}$$

This thermal recovery combined with 5 MW (17.1 MMBtu/hr) electrical output from 30 MMBtu/hr fuel input achieves 85% total CHP efficiency.

The approach temperature (difference between steam temperature and exhaust temperature at the same location) limits steam pressure. A 30°F approach requires exhaust temperature 30°F above saturation temperature. For 150 psig steam (366°F saturation), exhaust must remain above 396°F, constraining heat recovery depth.

The pinch point occurs where exhaust temperature equals steam saturation temperature plus approach. Effective HRSG design positions the pinch 10-20°F above the minimum approach to maximize heat transfer surface utilization. Triple-pressure HRSGs eliminate the large temperature difference between high-pressure steam generation and low-temperature economizing, recovering 5-10% additional thermal energy.

## Inlet Air Cooling Effects

Gas turbine power output and efficiency decrease with rising ambient temperature because air density decreases, reducing compressor mass flow. The power output varies approximately:

$$\frac{P_2}{P_1} = \frac{\rho_2}{\rho_1} = \frac{T_1}{T_2}$$

A turbine producing 10 MW at 15°C (59°F) delivers only 8.5 MW at 35°C (95°F), representing 15% capacity loss. The efficiency also degrades by 1-3 percentage points due to increased compressor work relative to turbine output.

Inlet air cooling restores capacity and efficiency during hot weather. Three principal technologies serve this application:

**Evaporative Cooling** sprays water into inlet airflow or uses wetted media. The evaporation depresses dry bulb temperature toward wet bulb temperature, increasing air density. Power augmentation of 8-15% results during hot, dry conditions. The effectiveness depends on wet bulb depression (difference between dry bulb and wet bulb temperatures). In humid climates, limited evaporation potential restricts augmentation to 3-5%.

**Refrigeration Cooling** uses mechanical or absorption chillers to cool inlet air below wet bulb temperature. Cooling coils reduce temperature by 10-20°C (18-36°F), increasing output 15-30%. The parasitic power for mechanical chilling consumes 10-20% of capacity gain, yielding net augmentation of 12-24%. Absorption chillers using turbine waste heat eliminate parasitic load but add complexity and capital cost.

**Ice Thermal Storage** generates ice during off-peak hours and melts the ice during peak demand to cool inlet air. This approach shifts electrical load to off-peak periods and provides economical peaking capacity. Storage systems deliver 2-4 hours of full cooling, targeting utility peak pricing periods.

The economic justification for inlet cooling depends on peak power pricing. Capacity payments of $100-200/kW-year justify evaporative or refrigeration cooling. Ice storage economics depend on daily pricing differentials exceeding $0.05-0.10/kWh.

## Combined Cycle Configurations

Combined cycle systems add a steam turbine to extract additional electrical work from heat recovered in the HRSG. This configuration achieves electrical efficiencies of 50-60%, substantially exceeding simple cycle performance.

The combined cycle output equals the gas turbine output plus steam turbine output:

$$W_{CC} = W_{GT} + W_{ST}$$

The steam turbine typically produces 30-50% of gas turbine output, depending on HRSG configuration and steam conditions. A 40 MW gas turbine with 55 MW electrical output operates at 55% combined cycle efficiency versus 35% simple cycle.

The combined cycle power-to-heat ratio increases to 1.0-1.5 versus 0.5-0.8 for simple cycle, better matching facilities with higher electrical loads. However, steam extraction for thermal use reduces electrical output, requiring careful optimization of electrical and thermal production.

Supplementary firing in the HRSG increases steam production by burning additional fuel in the oxygen-rich turbine exhaust. The exhaust contains 15-17% O₂, enabling firing to 1400-1600°F without additional air. Supplementary firing increases thermal output and lowers the power-to-heat ratio, providing operational flexibility.

## Part-Load Performance Characteristics

Gas turbines exhibit substantial efficiency degradation at part load due to reduced compressor efficiency and increased turbine cooling flow fractions. Simple cycle efficiency at 50% load typically decreases by 5-10 percentage points from full-load efficiency.

The part-load efficiency penalty results from multiple factors:

- Reduced compressor efficiency at off-design flow conditions
- Lower pressure ratio due to reduced speed or variable geometry
- Increased parasitic losses (fixed auxiliary power, higher cooling flows)
- Combustor inefficiency at low firing temperatures
- Higher exhaust oxygen concentration indicating incomplete heat extraction

Variable inlet guide vanes and variable geometry compressor stators partially mitigate these losses by maintaining pressure ratio as flow decreases. Advanced controls optimize firing temperature and pressure ratio for each load point. Two-shaft turbines separate the gas generator from power turbine, allowing independent speed optimization and improving part-load efficiency by 2-4 percentage points.

The exhaust temperature increases at part load as less energy is extracted by the turbine. A turbine with 510°C (950°F) full-load exhaust temperature produces 565°C (1050°F) exhaust at 50% load. This characteristic benefits heat recovery by maintaining high exhaust temperature, though the reduced mass flow decreases total thermal output. The increased exhaust temperature at part load can maintain steam production closer to design conditions, improving overall CHP efficiency relative to electrical-only operation.

The heat rate (fuel input per kWh output) increases substantially at part load. A turbine with 10,000 Btu/kWh heat rate at full load operates at 12,500-14,000 Btu/kWh at 50% load. This 25-40% heat rate penalty limits economic operation at low loads. Combined cycle plants maintain better part-load performance because reduced gas turbine output is partially offset by maintained or increased steam turbine output from higher exhaust temperatures.

## Emissions Characteristics and Control

Gas turbines inherently produce NOx through thermal formation at high combustion temperatures. The NOx formation rate follows exponential temperature dependence:

$$\text{NOx} \propto e^{-38000/T}$$

Where temperature T is in Kelvin. This strong dependence drives emissions control toward combustion temperature reduction.

**Nitrogen Oxides (NOx)**: Conventional diffusion flame combustors produce 150-250 ppmv NOx (0.9-1.5 lb/MWh). Dry low-NOx combustors achieve 0.15-0.35 lb/MWh (25-60 ppmv at 15% O₂) through lean premixed combustion. Multiple combustion zones with staged fuel injection optimize the temperature profile. Water or steam injection can further reduce NOx to 0.10-0.20 lb/MWh but penalizes efficiency 2-3 percentage points through lost steam or demineralized water consumption.

Selective catalytic reduction (SCR) reduces NOx by 80-95% through reactions with ammonia over a catalyst. For gas turbines with 30 ppmv raw NOx, SCR achieves sub-5 ppmv (0.03 lb/MWh). The SCR reactor installs in the HRSG between high and intermediate pressure sections where exhaust temperature optimizes catalyst activity (600-750°F). Ammonia slip (unreacted ammonia) must remain below 5-10 ppmv to prevent ammonium sulfate formation and air quality violations.

**Carbon Monoxide and Hydrocarbons**: CO and unburned hydrocarbons result from incomplete combustion, particularly during startup and low-load operation. Oxidation catalysts convert these species to CO₂ when exhaust temperature exceeds 450°F. CO emissions typically remain below 0.1 lb/MWh (10-20 ppmv) for well-designed combustors. Lean premixed combustors may experience elevated CO at low loads where lean blowout limits operation, requiring rich-burn zones or variable fuel staging.

**Particulate Matter**: Natural gas combustion produces minimal particulate emissions (0.002-0.005 lb/MWh). Liquid fuel firing generates significantly higher particulate from fuel ash and unburned carbon, requiring steam injection or water injection for smoke suppression.

**Carbon Dioxide**: Gas turbines burning natural gas emit 1000-1300 lb CO₂/MWh in simple cycle and 750-950 lb CO₂/MWh in combined cycle. These emissions rates are 50-60% of coal-fired generation. CHP operation further reduces CO₂ emissions per unit of delivered energy by displacing separate thermal generation with waste heat recovery.

The emissions performance at part load generally degrades for CO and hydrocarbons due to lower combustion temperatures and less complete mixing. NOx emissions typically decrease at part load following the exponential temperature relationship, though some combustor designs exhibit increased NOx at intermediate loads due to flame stabilization requirements.

## Maintenance Requirements and Intervals

Gas turbine maintenance divides into scheduled inspections and component replacements based on operating hours, starts, and fuel quality. The maintenance intensity and cost significantly influence lifecycle economics.

**Hot Section Inspection (8,000-12,000 hours)**: Borescope inspection examines combustor liners, transition pieces, and turbine blades without disassembly. Typical duration 1-2 days. Internal inspections require combustor removal to access hot gas path components. Minor repairs address localized damage including coating spallation, oxidation, and minor cracking. Duration 3-7 days. Cost: 0.2-0.4 ¢/kWh.

**Major Inspection (24,000-48,000 hours)**: Complete disassembly enables replacement of combustor liners, transition pieces, and turbine blades/vanes showing thermal distress or life consumption. Compressor cleaning and blade reconditioning restore aerodynamic performance. Control system upgrades and generator rewinding may coincide with major inspections. Duration 2-4 weeks. Cost: 0.5-1.2 ¢/kWh.

**Compressor Water Wash**: Online or offline washing removes airborne contaminants depositing on compressor blades. Fouling degrades performance 2-8% over 3-6 months of operation. Automated online washing maintains performance with minimal downtime. Offline washing provides deeper cleaning during planned outages. Frequency varies from daily online washing in harsh environments to quarterly offline washing in clean locations.

**Combustion System Components**: Combustor liners and transition pieces operate at extreme temperatures with thermal cycling during starts and stops. Expected life ranges from 16,000-32,000 hours for conventional combustors to 8,000-16,000 hours for DLN combustors. Each start cycle consumes 2-4 hours of equivalent operating life due to thermal stress.

**Turbine Blades and Vanes**: First stage components experience the highest temperatures and stresses, requiring replacement at 24,000-48,000 hours. Advanced coatings and cooling extend life but increase replacement cost. Later stages achieve 48,000-96,000 hour life. Blade tip clearance increases with wear, degrading efficiency 0.5-1.5% over the interval between major inspections.

**Bearings and Seals**: Journal and thrust bearings require replacement at 48,000-96,000 hours based on oil analysis and vibration monitoring. Labyrinth seals wear gradually, increasing internal leakage and reducing efficiency. Seal replacement during major inspections restores performance.

Maintenance costs accumulate to 0.5-1.8 ¢/kWh over the turbine lifetime, with larger machines achieving lower per-kWh costs through economy of scale. Peak-fired units with frequent starts accumulate higher maintenance costs due to thermal cycling damage. Combined cycle plants operate at lower exhaust temperatures, extending hot section life by 20-40% compared to simple cycle operation.

Microturbines employ different maintenance approaches. Air bearings eliminate oil and reduce scheduled maintenance to air filter replacement every 1,000-2,000 hours. Recuperator fouling degrades efficiency 2-5% over 8,000-16,000 hours, requiring removal for external cleaning. The compact construction often dictates full module replacement rather than field overhaul, with complete engine exchange at 40,000-60,000 hours. Maintenance costs range from 0.8-1.5 ¢/kWh for microturbines.

Fuel quality significantly impacts maintenance requirements. Natural gas with less than 0.1 grain H₂S per 100 scf and minimal particulates enables standard intervals. Sour gas, liquid fuels, and biogas require upgraded materials, more frequent inspections, and potentially 25-50% shorter component life. Fuel filtration to 3-5 microns protects fuel nozzles and reduces combustor degradation.
