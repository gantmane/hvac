---
title: "Combustion Gas Turbines for CHP"
description: "Comprehensive engineering analysis of gas turbine prime movers including Brayton cycle thermodynamics, component design, heat recovery steam generation, combined cycle configurations, and performance optimization for distributed generation applications."
date: 2026-01-04
weight: 2
---

Combustion gas turbines convert fuel energy to mechanical shaft power through continuous-flow compression, combustion, and expansion processes. These machines dominate CHP applications above 5 MW capacity, with industrial gas turbines reaching over 300 MW in combined cycle configurations. The high-temperature, high-mass-flow exhaust makes gas turbines particularly suitable for steam generation and combined cycle operation, achieving overall efficiencies exceeding 80%.

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

## Component Design and Performance

The axial-flow compressor comprises 10-20 stages of rotating and stationary airfoils. Each stage increases pressure by 10-25%, with cumulative pressure ratios of 10-40. Compressor efficiency critically affects overall performance since compression work typically consumes 50-70% of turbine work output.

Compressor surge represents a fundamental operating limitation. At low flow rates or high pressure ratios, flow separation causes reversed flow and violent pressure oscillations. The surge line defines the minimum stable flow at each speed. Modern compressors incorporate variable inlet guide vanes and variable stator vanes to extend the operating range and prevent surge during startup and part-load operation.

The combustion chamber burns fuel at nearly constant pressure, raising temperature to the maximum allowable turbine inlet temperature. Combustor design balances complete combustion, low emissions, and combustor liner durability. Dry low-NOx (DLN) combustors premix fuel and air in lean mixtures (φ = 0.5-0.6) to reduce peak flame temperature and NOx formation. The lean premixed approach requires careful control to prevent flashback (upstream flame propagation) and combustion instability.

The turbine extracts energy from the high-temperature, high-pressure gas through 2-5 expansion stages. The first stage experiences the highest thermal and mechanical stresses, requiring advanced nickel-based superalloys or ceramic matrix composites. Internal air cooling, thermal barrier coatings, and film cooling enable operation with gas temperatures exceeding metal melting points.

## Heat Recovery and CHP Integration

Gas turbine exhaust contains 50-65% of fuel input energy at temperatures of 450-600°C (840-1110°F), providing exceptional heat recovery potential. The high temperature enables high-pressure steam generation and supports absorption cooling or industrial process heat.

A heat recovery steam generator (HRSG) extracts thermal energy from turbine exhaust to produce steam. The HRSG typically incorporates multiple pressure levels (single, dual, or triple pressure) to maximize heat recovery across the exhaust temperature range.

The recoverable thermal energy follows from the exhaust mass flow and temperature:

$$Q_{recovery} = \dot{m}_{exh} \cdot c_p \cdot (T_{exh,in} - T_{stack})$$

For a 5 MW gas turbine with 50,000 lb/hr exhaust at 950°F, cooling to 300°F stack temperature yields:

$$Q_{recovery} = 50000 \cdot 0.26 \cdot (950 - 300) = 8.45 \text{ MMBtu/hr}$$

This thermal recovery combined with 5 MW (17.1 MMBtu/hr) electrical output from 30 MMBtu/hr fuel input achieves 85% total CHP efficiency.

The approach temperature (difference between steam temperature and exhaust temperature at the same location) limits steam pressure. A 30°F approach requires exhaust temperature 30°F above saturation temperature. For 150 psig steam (366°F saturation), exhaust must remain above 396°F, constraining heat recovery depth.

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

Variable inlet guide vanes and variable geometry compressor stators partially mitigate these losses by maintaining pressure ratio as flow decreases. Advanced controls optimize firing temperature and pressure ratio for each load point.

The exhaust temperature increases at part load as less energy is extracted by the turbine. This characteristic can benefit heat recovery by maintaining high exhaust temperature, though the reduced mass flow decreases total thermal output.

## Emissions Control Technologies

Gas turbines inherently produce NOx through thermal formation at high combustion temperatures. The NOx formation rate follows exponential temperature dependence:

$$\text{NOx} \propto e^{-38000/T}$$

Where temperature T is in Kelvin. This strong dependence drives emissions control toward combustion temperature reduction.

Dry low-NOx combustors achieve 0.15-0.35 lb/MWh (25-60 ppmv at 15% O₂) through lean premixed combustion. Multiple combustion zones with staged fuel injection optimize the temperature profile. Water or steam injection can further reduce NOx but penalizes efficiency through lost steam or demineralized water.

Selective catalytic reduction (SCR) reduces NOx by 80-95% through reactions with ammonia over a catalyst. For gas turbines with 30 ppmv raw NOx, SCR achieves sub-5 ppmv (0.03 lb/MWh). The SCR reactor installs in the HRSG between high and intermediate pressure sections where exhaust temperature optimizes catalyst activity (600-750°F).

Carbon monoxide and unburned hydrocarbons result from incomplete combustion, particularly during startup and low-load operation. Oxidation catalysts convert these species to CO₂ when exhaust temperature exceeds 450°F. CO emissions typically remain below 0.1 lb/MWh for well-designed combustors.
