---
title: "Thermoelastic Cooling"
description: "Solid-state thermoelastic and elastocaloric cooling using shape memory alloys, nitinol wire systems, and mechanically-induced phase transformations for environmentally benign refrigeration."
weight: 4
---

Thermoelastic cooling, also termed elastocaloric cooling, exploits the reversible temperature change in certain materials undergoing mechanically-induced phase transformations. This solid-state cooling mechanism eliminates vapor compression cycles and halogenated refrigerants, offering a potentially transformative approach to environmentally sustainable refrigeration with no direct greenhouse gas emissions.

## Elastocaloric Effect Fundamentals

The elastocaloric effect manifests when mechanical stress induces a crystallographic phase transformation in materials, particularly shape memory alloys. During loading, the material undergoes an entropy-reducing phase transition (typically austenite to martensite), releasing latent heat ΔQ = T·ΔS, where ΔS is the entropy change associated with the transformation.

Upon unloading, the reverse transformation absorbs heat from surroundings, producing a cooling effect. The adiabatic temperature change ΔT_ad can reach 10-30 K in optimized materials, with values described by ΔT_ad = -(T/ρC_p)(∂σ/∂T)_ε·Δε, where σ is stress, ε is strain, ρ is density, and C_p is specific heat.

The coefficient of performance for an ideal elastocaloric cycle approaches Carnot efficiency η_Carnot = T_C/(T_H - T_C), with practical systems achieving 30-60 percent of Carnot COP when accounting for hysteresis losses, mechanical work, and heat transfer irreversibilities.

## Shape Memory Alloy Materials

Nickel-titanium (nitinol) alloys dominate elastocaloric research due to their exceptional superelastic properties, phase transformation characteristics, and mechanical durability. Equiatomic NiTi and near-equiatomic compositions exhibit transformation temperatures controllable through composition and heat treatment in the range -50°C to +100°C.

The martensitic transformation in NiTi produces adiabatic temperature changes of 15-25 K under stress levels of 400-800 MPa, with transformation strains of 6-8 percent. The material exhibits excellent cyclic stability when operated below the stress-induced fracture limit of approximately 1 GPa.

Alternative elastocaloric materials under investigation include Cu-Zn-Al alloys, Ni-Mn-based Heusler alloys, and Fe-Rh compounds. Cu-based alloys offer lower material costs but suffer from lower transformation enthalpy and reduced mechanical stability. Heusler alloys provide large entropy changes but require brittle material management.

## Nitinol Elastocaloric Systems

Practical elastocaloric refrigerators employ nitinol in wire, tube, or bulk configurations. Wire-based systems benefit from high surface-area-to-volume ratios enabling rapid heat transfer, with typical diameters ranging from 0.1-1.0 mm. Thin wires allow operating frequencies of 1-10 Hz through reduced thermal masses and heat transfer time constants.

The mechanical loading system must provide sufficient stress to complete the martensitic transformation while maintaining alignment and uniform stress distribution. Typical implementations use linear actuators, rotating cams, or hydraulic systems to apply tensile stresses in the 400-700 MPa range with strokes of 6-8 percent wire elongation.

Heat transfer between the nitinol element and heat transfer fluid occurs through direct contact in most configurations. Forced convection with water or air serves as the heat transfer medium, with convection coefficients of 100-1000 W/m²K for water and 10-100 W/m²K for air. The Biot number Bi = hD/k should remain below 0.1 to ensure uniform temperature distribution during heat transfer periods.

## Mechanical Stress Loading Systems

The mechanical loading system consumes work input equivalent to the integral ∫σdε over the loading path, including both recoverable elastic energy and dissipative hysteresis losses. Hysteresis during the phase transformation cycle represents 5-15 percent of the transformation energy, appearing as irreversible mechanical dissipation.

Linear motor actuators provide precise control of loading profiles with efficiencies of 70-85 percent. The mechanical work per cycle W_mech = ∫σdε typically ranges from 10-30 J/g of active material. Peak force requirements reach 1-10 kN for wire bundle systems, with stroke frequencies limited by heat transfer rates rather than mechanical considerations.

Energy recovery through regenerative mechanical systems can reclaim 50-70 percent of elastic energy during unloading. Spring-based energy storage, hydraulic accumulators, or electromagnetic regeneration capture work that would otherwise dissipate, significantly improving system-level COP.

## Solid-State Cooling Advantages

Elastocaloric systems offer numerous advantages over vapor compression technology. The absence of working fluid eliminates refrigerant leakage, charge loss, and associated environmental impacts. Solid-state operation enables compact form factors, reduces noise to mechanical actuator levels, and eliminates compressor failure modes.

Scalability extends from micro-cooling applications (10-100 W) to residential and commercial capacities (1-10 kW) through parallel arrangement of active elements. The technology operates effectively across temperature spans of -20°C to +40°C, covering typical air conditioning and refrigeration needs.

Linear scaling of cooling power with operating frequency allows variable capacity control without efficiency penalties characteristic of compressor cycling. Part-load performance remains high as frequency reduces proportionally with demand while maintaining steady-state efficiency.

## Regenerative Cycles

Advanced elastocaloric systems employ regenerative thermal cycling analogous to magnetic refrigeration. Active material elements traverse sequentially between heat rejection and heat absorption phases, establishing a temperature gradient along the regenerator bed. This cascading effect amplifies the single-stage temperature span.

A typical regenerative cycle consists of four steps: adiabatic loading (heating), hot-side heat rejection with fluid flow, adiabatic unloading (cooling), and cold-side heat absorption with reverse fluid flow. The fluid flow direction alternates synchronously with mechanical loading to extract maximum thermal energy from each stage.

Temperature spans of 30-50 K have been demonstrated with multi-stage regenerative elastocaloric systems, compared to 10-25 K for single-stage configurations. The utilization factor, defined as the ratio of fluid thermal capacitance to solid thermal capacitance, should approximate unity for optimal regenerative effectiveness.

## Heat Transfer Optimization

Heat transfer between active material and heat transfer fluid dominates the performance limitations of elastocaloric systems. The thermal response time τ = ρC_pV/hA must remain small compared to the cycle period to achieve high utilization of the elastocaloric effect.

For cylindrical nitinol wires, the characteristic heat transfer length scale is the wire radius r. The Biot number Bi = hr/k_wire determines the temperature uniformity during heat transfer. Values of Bi < 0.1 indicate lumped capacitance behavior, while Bi > 1 requires distributed thermal analysis.

Surface enhancement through texturing, fins, or porous structures increases effective heat transfer area. Wire bundle configurations with cross-flow or parallel-flow heat transfer fluids achieve area enhancement factors of 10-100 compared to single wire arrangements while maintaining acceptable pressure drops below 10 kPa.

## Fatigue and Mechanical Durability

Cyclic mechanical loading induces fatigue in elastocaloric materials, limiting operational lifetime. Nitinol exhibits excellent low-cycle fatigue resistance when operated within the superelastic stress plateau, with demonstrated lifetimes exceeding 10⁷ cycles at stress amplitudes of 500 MPa.

Functional fatigue, characterized by gradual shifts in transformation temperatures and stress plateaus, occurs due to accumulated defects and residual martensite stabilization. Proper aging heat treatments and stress-controlled loading profiles minimize functional fatigue, maintaining stable performance over millions of cycles.

Stress concentrations at grips, clamps, or geometric discontinuities accelerate crack initiation. Uniform stress distribution requires precision alignment, appropriate grip designs with gradual stress transitions, and avoidance of excessive localized strains beyond 8-9 percent.

## System Architecture and Design

Practical elastocaloric refrigerators integrate mechanical actuation, active material elements, heat exchangers, and thermal management in compact packages. Parallel operation of multiple wire bundles provides scalable cooling capacity, with each bundle containing 10-100 wires operating in synchronized loading cycles.

Phase-shifted operation of multiple bundles creates quasi-continuous cooling by staggering the timing of individual bundle cycles. Four-bundle configurations with 90-degree phase shifts approximate steady-state cooling with ripple amplitudes of 10-20 percent of mean cooling power.

Heat exchanger design accommodates alternating fluid flow direction with minimal pressure drop and thermal capacitance. Manifolded channels, porous media, or microchannel geometries achieve low thermal resistance while maintaining structural support for the active material under stress.

## Engineering Considerations

Material selection balances transformation temperature, entropy change, mechanical properties, cost, and availability. Nitinol remains the primary candidate material despite higher costs ($50-200/kg) due to superior performance and durability. Continued material development targets increased entropy changes and reduced hysteresis.

Mechanical system design requires accurate stress and strain measurement, closed-loop control of loading profiles, and mechanical energy recovery. Servo-controlled linear motors provide precise position control with force feedback, enabling optimization of loading rates and stress limits.

Thermal management includes both hot-side heat rejection and cold-side heat absorption heat exchangers. Liquid-coupled systems using water, water-glycol, or dielectric fluids offer higher heat transfer coefficients than air-coupled designs but introduce pumping energy penalties and freeze protection requirements.

## Best Practices

Initial system design should establish material selection, operating stress range, and frequency based on target temperature span and cooling capacity. Stress levels of 60-80 percent of the transformation completion stress provide optimal balance between temperature change and mechanical durability.

Optimize heat transfer through appropriate wire diameter selection, achieving Biot numbers of 0.05-0.2 for efficient heat transfer within available cycle time. Operating frequencies of 0.5-5 Hz accommodate typical heat transfer time constants while limiting mechanical actuation power.

Implement mechanical energy recovery to improve system COP, targeting recovery of 50-70 percent of elastic strain energy. Spring-based systems offer simplicity for low-capacity applications, while electromagnetic or hydraulic regeneration suits larger capacities.

Monitor functional fatigue through periodic measurement of transformation characteristics. Compensate for gradual shifts in transformation stress through adaptive control of mechanical loading profiles, maintaining consistent cooling performance throughout system lifetime.
