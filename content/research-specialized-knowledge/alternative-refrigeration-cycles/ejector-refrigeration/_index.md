---
title: "Ejector Refrigeration"
aliases: ["Ejector Refrigeration"]
description: "Ejector-based refrigeration cycles utilizing jet entrainment principles for thermally-driven cooling, including steam ejector systems, two-phase flow ejectors, and solar-powered applications."
weight: 2
---

Ejector refrigeration systems employ high-velocity fluid jets to entrain and compress low-pressure refrigerant vapor, creating a thermally-driven cooling cycle without mechanical compressors. These systems convert low-grade thermal energy from waste heat, solar collectors, or cogeneration systems into useful cooling, offering advantages in simplicity, reliability, and utilization of renewable or waste energy sources.

## Ejector Cycle Fundamentals

The ejector refrigeration cycle consists of a generator, ejector, condenser, expansion valve, and evaporator. The generator produces high-pressure primary vapor using heat input at temperatures typically 80-150°C. This primary stream enters the ejector at supersonic velocities, creating a low-pressure region that entrains secondary vapor from the evaporator.

The momentum transfer from primary to secondary flow compresses the mixed stream to condenser pressure. The thermodynamic advantage derives from using thermal energy rather than mechanical work for vapor compression. The coefficient of performance COP = Q_evap/Q_gen typically ranges from 0.2-0.6, significantly lower than vapor compression but economically viable when waste heat or solar thermal energy is available at low cost.

The entrainment ratio ω = ṁ_secondary/ṁ_primary represents a critical performance parameter, relating secondary vapor flow rate to primary flow. Higher entrainment ratios improve COP but reduce pressure lift capability. Values of ω = 0.3-0.8 are typical for air conditioning applications with water as refrigerant.

## Steam Ejector Cooling Systems

Water-based steam ejector systems dominate large-scale applications due to water's environmental benignity, thermophysical properties, and zero ozone depletion potential. These systems operate with evaporator temperatures of 4-15°C, condenser temperatures of 25-40°C, and generator temperatures of 70-120°C, making them well-suited for solar thermal or waste heat integration.

The ejector operates as a momentum-driven vacuum pump, maintaining evaporator pressures of 0.8-1.7 kPa corresponding to saturation temperatures of 4-15°C. Primary steam enters at pressures of 50-300 kPa depending on available heat source temperature. The pressure ratio between condenser and evaporator typically ranges from 3-8.

Cooling capacities for commercial steam ejector chillers range from 50-5000 kW. The technology excels in applications with abundant low-grade heat and moderate cooling requirements, such as industrial process cooling, district cooling, and solar-assisted air conditioning.

## Two-Phase Ejector Systems

Advanced ejector designs employ two-phase flow regimes to improve performance beyond pure vapor compression. Two-phase ejectors accept liquid-vapor mixtures from the evaporator or utilize flash evaporation within the ejector to enhance momentum transfer. The presence of liquid droplets increases density and momentum, improving entrainment and compression efficiency.

The critical challenge in two-phase ejector design involves managing complex fluid dynamics including droplet formation, evaporation kinetics, shock waves, and phase interactions. Non-equilibrium thermodynamic effects become significant as rapid acceleration and mixing prevent thermal equilibrium between phases.

Numerical modeling of two-phase ejectors requires computational fluid dynamics with homogeneous or separated flow models. The homogeneous equilibrium model (HEM) assumes thermal and velocity equilibrium between phases, providing reasonable accuracy for design calculations. More sophisticated models account for slip velocity and thermal non-equilibrium through relaxation time formulations.

## Ejector Geometry and Design

The ejector consists of four primary sections: the converging-diverging nozzle for primary flow acceleration, the suction chamber for secondary flow entrainment, the mixing chamber where momentum transfer occurs, and the diffuser for pressure recovery. Each section's geometry critically influences performance.

The primary nozzle accelerates high-pressure vapor to supersonic velocities (Mach 2-3), converting thermal energy to kinetic energy. The nozzle exit diameter and position relative to the mixing chamber determine the entrainment characteristics. Throat-to-exit area ratios of 3-8 are typical for steam ejectors.

The mixing chamber length-to-diameter ratio L/D typically ranges from 5-12, balancing sufficient length for complete mixing against excessive wall friction losses. Longer mixing sections improve pressure recovery but increase losses, requiring optimization for specific operating conditions.

The diffuser recovers kinetic energy through gradual deceleration, with divergence angles of 2-4 degrees to avoid flow separation. Pressure recovery efficiency in the diffuser significantly impacts overall ejector performance, with well-designed diffusers recovering 70-85 percent of available dynamic pressure.

## Ejector Performance Characteristics

Ejector performance exhibits strong sensitivity to operating conditions. The critical operating mode occurs when the evaporator pressure reaches its design value while the entrainment ratio achieves its maximum. Operating at off-design conditions reduces entrainment ratio or causes back-flow into the evaporator.

Three distinct operating regimes characterize ejector behavior: critical mode (choked flow, constant entrainment), subcritical mode (reduced entrainment with increasing condenser pressure), and reverse-flow mode (compression ratio exceeds ejector capability). Design optimization targets maximum time operating in critical mode.

The ejector coefficient of performance depends on generator temperature, evaporator temperature, and condenser temperature. Increasing generator temperature improves COP through higher primary vapor pressure and velocity. Reducing evaporator temperature or increasing condenser temperature degrades performance by increasing required compression ratio.

Performance maps express entrainment ratio and COP as functions of dimensionless parameters including area ratio A_mixing/A_nozzle, pressure ratios P_condenser/P_evaporator and P_generator/P_condenser, and non-dimensional geometric ratios.

## Variable Geometry Ejectors

Fixed-geometry ejectors operate efficiently only near design conditions, severely limiting part-load performance and operational flexibility. Variable geometry designs incorporate adjustable needle valves, spindles, or movable nozzles to adapt to changing conditions.

Spindle-type ejectors employ a conical needle within the primary nozzle, allowing adjustment of the nozzle throat area. Retracting the spindle increases throat area, accommodating higher primary flow rates or lower generator temperatures. This adaptation maintains critical operating mode across broader conditions.

Multi-ejector systems parallel multiple fixed-geometry ejectors with staged activation, approximating variable capacity while maintaining high efficiency. The modular approach provides redundancy and gradual capacity control, though at increased complexity and capital cost compared to single variable-geometry units.

Control strategies for variable geometry ejectors balance cooling capacity, COP optimization, and response to transient loads. Model-based control using real-time performance maps and extremum-seeking algorithms maximize COP under varying conditions.

## Solar-Driven Ejector Systems

Solar thermal collectors provide heat input to ejector cooling systems, creating completely renewable cooling with zero operating emissions. Flat-plate collectors generating 70-90°C thermal output suit low-temperature ejector designs with water refrigerant. Evacuated tube collectors achieve 90-120°C, improving COP and expanding the operational window.

Thermal energy storage using phase change materials or stratified water tanks decouples solar collection from cooling demand, enabling operation during cloudy periods or nighttime. Storage typically provides 2-6 hours of full-capacity operation, sized based on local insolation patterns and demand profiles.

The solar fraction, defined as the portion of cooling energy derived from solar thermal input, typically reaches 60-85 percent for well-designed systems with adequate storage. Auxiliary heaters (gas, electric, or biomass) cover periods of insufficient solar availability, ensuring continuous cooling capacity.

Economic viability of solar ejector systems depends on local energy costs, solar resource quality, and system capital costs. Payback periods of 5-12 years are typical in regions with high electricity costs and strong solar resources, improving with decreasing collector costs and carbon pricing mechanisms.

## Refrigerant Selection

Refrigerant choice profoundly impacts ejector system performance and application suitability. Water dominates large-scale applications above 5°C evaporator temperature due to excellent environmental properties, high latent heat, and compatibility with low-cost materials. The requirement for vacuum conditions (below atmospheric pressure) necessitates robust sealing and purging of non-condensables.

Alternative refrigerants enable sub-zero cooling and compact system designs. R-134a, R-245fa, and low-GWP alternatives such as R-1234yf or R-1233zd operate at elevated pressures, eliminating vacuum concerns while requiring higher quality sealing and pressure vessels. These refrigerants suit mobile applications, compact chillers, and moderate-temperature refrigeration.

Ammonia provides excellent thermodynamic performance with zero GWP, suitable for industrial refrigeration with appropriate safety considerations. Natural refrigerants including propane and carbon dioxide offer environmental advantages but require careful system design addressing flammability or high operating pressures respectively.

## Multi-Ejector and Cascade Systems

Cascaded ejector stages enable higher compression ratios and temperature lifts than single-stage designs. Two-stage systems position an intermediate condenser-evaporator between ejector stages, with the first stage compressing from evaporator to intermediate pressure and the second stage compressing to final condenser pressure.

The cascade configuration extends the operational range to lower evaporator temperatures (down to -10°C with water) or higher condenser temperatures, at the cost of increased complexity and capital investment. COP remains lower than single-stage systems but enables applications infeasible with single-stage compression.

Parallel multi-ejector architectures operate several ejectors with different optimal conditions, switching between units or modulating flow distribution to maintain peak efficiency across varying loads. This approach provides variable capacity with high part-load efficiency, critical for applications with fluctuating cooling demands.

## Hybrid Compression-Ejector Systems

Combining mechanical vapor compression with ejector-assisted flash gas recovery improves overall system COP by 10-30 percent. The ejector captures flash gas from the expansion process, using it to entrain additional vapor and pre-compress the combined stream before entering the mechanical compressor.

This hybrid approach reduces compressor work by recovering expansion losses and utilizing the kinetic energy of flash gas. The ejector operates at moderate entrainment ratios (0.1-0.3), requiring less critical geometry tolerances than stand-alone ejector refrigeration systems.

Hybrid systems prove particularly effective in supermarket refrigeration, cold storage, and industrial refrigeration where substantial flash gas generation occurs. Retrofit applications add ejectors to existing vapor compression systems, yielding efficiency improvements of 8-18 percent with moderate capital investment.

## Engineering Considerations

Ejector design employs computational fluid dynamics for geometry optimization, validated through experimental testing. One-dimensional models provide initial sizing and performance estimates, while CFD resolves complex flow phenomena including shock structure, mixing patterns, and phase interactions.

Material selection addresses corrosion resistance, thermal stability, and manufacturability. Stainless steel 316 suits water-based systems, while copper alloys, aluminum, or polymer-lined components serve alternative refrigerants. Precision machining achieves surface finishes below Ra 0.8 μm for optimal aerodynamic performance.

System integration requires careful attention to generator heat exchanger design, condenser sizing for mixed refrigerant streams, and control sequences managing start-up, shutdown, and off-design operation. Instrumentation includes pressure sensors at critical locations, flow measurement, and temperature monitoring for performance verification.

## Best Practices

Begin design with selection of refrigerant and operating temperatures based on application requirements and available heat source. Establish primary vapor conditions from generator temperature and pressure, typically 0.8-0.9 of saturation pressure at generator temperature to account for superheating and pressure drops.

Size the primary nozzle for choked flow conditions at design point, using isentropic flow relationships with nozzle efficiency of 85-95 percent. Select mixing chamber diameter 2-4 times the nozzle throat diameter, with length optimized through CFD or empirical correlations.

Oversize the condenser by 15-25 percent relative to rated capacity to accommodate non-condensable accumulation and performance degradation. Install vacuum pumps for initial evacuation and periodic purging of air and non-condensables, maintaining proper evaporator vacuum.

Commission systems with careful verification of flow rates, temperatures, and pressures at design conditions. Measure actual COP and compare to design predictions, adjusting nozzle position or geometry if variable mechanisms are provided. Implement monitoring systems for early detection of non-condensable buildup or fouling.

Maintain water treatment protocols for steam ejector systems, targeting pH 7-9, conductivity below 10 μS/cm, and dissolved oxygen below 0.5 ppm. Regular inspection of ejector internals identifies erosion, corrosion, or deposits requiring cleaning or replacement.
