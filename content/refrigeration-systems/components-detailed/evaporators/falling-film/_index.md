---
title: "Falling Film Evaporators"
aliases: ["Falling Film Evaporators"]
description: "Comprehensive technical guide to falling film evaporator design, spray distribution systems, tube wetting, heat transfer coefficients, and refrigerant charge reduction in chiller applications"
keywords: ["falling film evaporator", "spray distribution", "tube wetting", "heat transfer coefficient", "reduced refrigerant charge", "flooded evaporator comparison", "chiller applications", "falling film design"]
tags: ["falling film evaporator", "spray distribution", "tube wetting", "heat transfer coefficient", "reduced refrigerant charge", "flooded evaporator comparison", "chiller applications", "falling film design"]
weight: 5
---

Falling film evaporators represent an advanced heat exchanger design where liquid refrigerant flows as a thin film over the exterior surface of heat transfer tubes rather than flooding the entire shell. This configuration delivers superior heat transfer performance, reduced refrigerant charge, and enhanced operational efficiency compared to conventional flooded evaporators.

## Operating Principle

In a falling film evaporator, refrigerant is distributed across the top of a horizontal or vertical tube bundle and flows downward as a thin film (typically 0.2-0.5 mm thick) along the tube exterior surfaces. Heat absorbed from the process fluid flowing inside the tubes causes the refrigerant film to evaporate progressively as it descends. The vapor-liquid mixture collects at the bottom and separates, with vapor routed to the compressor and any remaining liquid recirculated back to the distribution system.

The thin film configuration maximizes heat transfer by minimizing thermal resistance between the tube surface and the evaporating refrigerant. Unlike flooded designs where tubes are submerged in a large refrigerant pool, falling film evaporators maintain only the refrigerant mass necessary for surface wetting, dramatically reducing total system charge.

## Spray Distribution Systems

The distribution system constitutes the most critical component in falling film evaporator design. Achieving uniform refrigerant distribution across all tubes directly determines heat transfer effectiveness and system capacity.

**Distribution Header Design:**
- Perforated pipe headers positioned above the tube bundle
- Orifice sizing calculated for equal flow distribution across tube length
- Pressure drop through orifices: 5-15 psi typical
- Multiple distribution points for wide tube bundles (>6 ft)

**Spray Nozzle Configuration:**
- Full-cone spray nozzles for uniform coverage
- Nozzle spacing: 12-24 inches depending on spray angle
- Flow rate per nozzle: 0.5-2 gpm typical
- Spray pattern verification during commissioning

**Recirculation Ratio:**
The ratio of liquid refrigerant circulated to the amount evaporated ranges from 2:1 to 6:1. Higher ratios ensure complete tube wetting but increase pump power consumption. Optimal ratios balance wetting effectiveness against parasitic energy losses.

## Tube Wetting Characteristics

Complete and uniform tube wetting is essential for maintaining design heat transfer coefficients. Insufficient wetting creates dry patches with significantly degraded thermal performance.

**Minimum Wetting Rate:**
Each tube requires a minimum liquid flow rate to maintain continuous film coverage. For horizontal tubes, the minimum wetting rate is:

Γ_min = 0.02-0.04 kg/(m·s)

Below this threshold, the film breaks into rivulets, creating unwetted areas with poor heat transfer.

**Film Thickness:**
Film thickness δ for laminar falling films is calculated from:

δ = (3μΓ/ρ²g)^(1/3)

Where:
- μ = dynamic viscosity
- Γ = mass flow rate per unit perimeter
- ρ = liquid density
- g = gravitational acceleration

Typical film thickness ranges from 0.2-0.5 mm for refrigerants like R-134a and ammonia under normal operating conditions.

**Wetting Performance Factors:**
- Surface finish: Smooth tubes promote uniform wetting; roughness can improve or degrade depending on pattern
- Tube material: Copper, stainless steel, and titanium all exhibit different wetting characteristics
- Refrigerant properties: Surface tension and viscosity affect film stability
- Heat flux: Higher heat flux increases evaporation rate and reduces film thickness

## Heat Transfer Coefficients

Falling film evaporators achieve heat transfer coefficients 20-40% higher than equivalent flooded designs due to reduced thermal resistance and enhanced nucleate boiling within the thin film.

**Typical Heat Transfer Coefficients:**

| Configuration | h_o (W/m²·K) | h_o (BTU/hr·ft²·°F) |
|---------------|--------------|---------------------|
| Flooded evaporator | 2,500-4,000 | 440-700 |
| Falling film evaporator | 3,500-6,000 | 615-1,055 |

**Heat Transfer Mechanisms:**
1. **Nucleate boiling** within the liquid film (dominant at higher heat flux)
2. **Convective evaporation** at the film-vapor interface
3. **Conduction** through the liquid film

The overall outside heat transfer coefficient h_o increases with:
- Higher mass flow rate (increased Γ)
- Higher heat flux (up to critical heat flux)
- Lower film thickness
- Enhanced surface geometry

**Enhanced Tube Performance:**
Enhanced tubes with specialized surface geometries (low-fin, turbulators, microgrooves) can increase falling film heat transfer coefficients by 50-100% compared to smooth tubes. The enhancements promote turbulence and increase nucleation site density.

## Reduced Refrigerant Charge

Falling film evaporators typically require 60-80% less refrigerant charge compared to flooded designs of equivalent capacity.

**Charge Comparison:**

| Evaporator Type | Refrigerant Charge | Relative Charge |
|-----------------|-------------------|-----------------|
| Flooded shell | 1.0-1.5 lb/ton | 100% (baseline) |
| Falling film | 0.2-0.5 lb/ton | 20-40% |

**Benefits of Reduced Charge:**
- Lower refrigerant cost, especially critical for expensive low-GWP alternatives
- Reduced environmental impact in case of leakage
- Simplified compliance with refrigerant quantity regulations
- Faster system response to load changes
- Lower pressure drop due to reduced static head

The charge reduction stems from eliminating the large liquid inventory required to submerge tubes in flooded designs. Only the refrigerant actively participating in heat transfer remains in the system.

## Flooded vs Falling Film Comparison

| Parameter | Flooded Evaporator | Falling Film Evaporator |
|-----------|-------------------|-------------------------|
| Heat transfer coefficient | 2,500-4,000 W/m²·K | 3,500-6,000 W/m²·K |
| Refrigerant charge | 1.0-1.5 lb/ton | 0.2-0.5 lb/ton |
| Tube wetting | Guaranteed by submersion | Requires proper distribution |
| Oil return | Natural to low point | Requires attention to design |
| Pressure drop (refrigerant) | Higher (static head) | Lower (no liquid column) |
| Part-load performance | Good | Excellent (no excess liquid) |
| Complexity | Lower | Higher (distribution system) |
| Fouling sensitivity | Moderate | Higher (distribution plugging) |
| Startup time | Longer (charge inventory) | Shorter (minimal charge) |

## Chiller Applications

Falling film evaporators are widely deployed in large centrifugal and screw chiller systems where refrigerant charge reduction and efficiency improvements justify the added complexity.

**Centrifugal Chillers:**
- Capacities: 200-10,000+ tons
- Refrigerants: R-134a, R-1233zd(E), R-513A, R-514A
- Applications: Commercial buildings, district cooling, industrial process cooling
- Typical configuration: Horizontal tube falling film with flooded process fluid side

**Screw Chillers:**
- Capacities: 100-1,500 tons
- Enhanced integration with economizer circuits
- Lower charge benefits particularly significant with HFO refrigerants

**Performance Advantages in Chillers:**
- EER improvements of 5-10% compared to flooded designs
- Reduced approach temperature (1-2°F improvement)
- Better part-load efficiency due to reduced refrigerant holdup
- Faster response to load changes

## Design Considerations

**Distribution System Design:**
Uniform refrigerant distribution across all tubes is non-negotiable. The distribution header must:
- Maintain adequate pressure to ensure equal flow from all orifices
- Account for momentum effects in horizontal headers
- Include provisions for cleaning and maintenance
- Provide visual inspection capability during commissioning

**Recirculation Pump Selection:**
- Pump head: 15-30 psi typical to overcome distribution pressure drop and elevation
- Flow rate: 2-6 times the evaporation rate
- Redundancy considerations for critical applications
- Variable speed capability for load optimization

**Tube Bundle Orientation:**
- **Horizontal tubes:** Most common, easier distribution, 5-10% lower h_o than vertical
- **Vertical tubes:** Higher heat transfer, compact footprint, more challenging distribution

**Vapor-Liquid Separation:**
Adequate separation volume and demister pads prevent liquid carryover to the compressor. Separation chamber design follows flooded evaporator principles but accommodates higher vapor velocities.

**Oil Management:**
Oil return to the compressor requires careful attention. Unlike flooded evaporators where oil naturally accumulates at the low point, falling film designs may retain oil in the recirculation loop. Solutions include:
- Oil skimming from the liquid separator
- Periodic oil bleed to discharge line or oil management system
- Miscible refrigerant-oil combinations with proper design

**Fouling Prevention:**
The thin liquid film cannot tolerate debris or scale formation. Water-side fouling reduces heat transfer more severely than in flooded designs. Required provisions:
- High-efficiency water filtration
- Chemical treatment programs
- Periodic tube cleaning access
- Refrigerant-side filtration to prevent distribution orifice plugging

**Turndown Capability:**
Falling film evaporators maintain high efficiency at part load because excess refrigerant does not flood inactive tube areas. At low loads, reduce recirculation ratio to maintain adequate wetting rates while minimizing pumping power.

**Control Strategy:**
- Monitor superheat at evaporator outlet (typically 5-10°F)
- Adjust expansion valve or electronic expansion valve to maintain target superheat
- Modulate recirculation pump speed based on load (advanced systems)
- Implement low-load wetting rate protection

## Performance Monitoring

Key operational parameters to monitor:

**Temperatures:**
- Process fluid inlet and outlet temperatures
- Refrigerant saturation temperature
- Approach temperature (should remain within 1-2°F of design)

**Pressures:**
- Evaporator saturation pressure
- Distribution header pressure (verify adequate distribution pressure drop)
- Pressure drop across tube bundle (refrigerant side)

**Flow Rates:**
- Process fluid flow rate
- Refrigerant recirculation rate
- Verify wetting rate remains above minimum threshold

Degradation in approach temperature or heat transfer effectiveness typically indicates distribution problems, fouling, or insufficient wetting. Address promptly to prevent further performance loss.

## Advantages and Limitations

**Advantages:**
- Superior heat transfer coefficients (20-40% higher than flooded)
- Reduced refrigerant charge (60-80% less)
- Lower refrigerant pressure drop
- Faster system response
- Better part-load efficiency
- Reduced environmental impact

**Limitations:**
- More complex distribution system
- Requires precise wetting rate control
- Higher sensitivity to fouling
- More sophisticated controls
- Higher initial cost
- Oil return requires careful design

Falling film evaporators represent the preferred technology for large chiller applications where efficiency, reduced refrigerant charge, and superior performance justify the additional design complexity.
