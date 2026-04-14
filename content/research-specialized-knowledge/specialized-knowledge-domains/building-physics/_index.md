---
title: "Building Physics"
aliases: ["Building Physics"]
description: "Building physics fundamentals for HVAC design including heat transfer, air and moisture transport, thermal bridging, condensation analysis, hygrothermal modeling, and building simulation tools for integrated building envelope and mechanical system design."
weight: 2
---

Building physics provides the fundamental scientific framework for understanding heat, air, and moisture transport through building envelopes. This discipline directly influences HVAC system design, energy performance, occupant comfort, and building durability. A comprehensive understanding of building physics principles enables HVAC engineers to properly account for envelope loads, prevent moisture damage, optimize system sizing, and integrate mechanical systems with architectural assemblies.

## Heat Transfer Fundamentals

Heat transfer through building envelopes occurs via three mechanisms that operate simultaneously and must be quantified for accurate load calculations.

**Conduction through solid materials** follows Fourier's Law:

q = -k × A × (dT/dx)

where k represents thermal conductivity (W/m·K), A is area (m²), and dT/dx is the temperature gradient. For steady-state one-dimensional heat flow through a homogeneous wall:

Q = U × A × ΔT

The overall heat transfer coefficient U (W/m²·K) accounts for all layers including surface film resistances.

**Convection at surfaces** transfers heat between solid boundaries and adjacent air through the convective heat transfer coefficient h:

q = h × A × (T_surface - T_air)

Surface coefficients vary with air velocity, surface orientation, and flow regime (laminar vs. turbulent). Interior surface coefficients typically range 5-10 W/m²·K for vertical surfaces, while exterior values reach 15-30 W/m²·K depending on wind speed.

**Radiation exchange** between surfaces and to the sky follows Stefan-Boltzmann principles:

q_rad = ε × σ × A × (T₁⁴ - T₂⁴)

where ε is emissivity, σ is the Stefan-Boltzmann constant (5.67×10⁻⁸ W/m²·K⁴), and temperatures are absolute. Long-wave radiation to the night sky can lower roof surface temperatures 5-10 K below ambient, affecting heating loads and condensation risk.

## Thermal Bridging Analysis

Thermal bridges create localized heat flow paths that bypass insulation, increasing energy consumption and creating condensation risks. These effects cannot be captured by one-dimensional U-value calculations.

| Thermal Bridge Type | Typical ψ-Value (W/m·K) | Temperature Factor f_Rsi |
|---------------------|-------------------------|--------------------------|
| Steel stud wall (600mm o.c.) | 0.05-0.15 | 0.65-0.75 |
| Concrete balcony slab | 0.25-1.2 | 0.45-0.65 |
| Window perimeter (insulated frame) | 0.02-0.06 | 0.70-0.85 |
| Window perimeter (aluminum frame) | 0.10-0.25 | 0.50-0.70 |
| Foundation wall to slab | 0.15-0.45 | 0.55-0.75 |
| Roof-to-wall junction | 0.10-0.30 | 0.60-0.80 |

The linear thermal transmittance ψ (psi-value) quantifies additional heat loss per linear meter of thermal bridge:

Q_bridge = ψ × L × ΔT

where L is the length of the thermal bridge. The temperature factor f_Rsi indicates condensation risk, with values below 0.70 requiring careful analysis in cold climates.

**Design strategies to minimize thermal bridging:**

- Continuous exterior insulation over structural elements
- Thermally broken connections at balconies and canopies
- Insulated structural thermal breaks at foundation transitions
- Advanced framing techniques (24" o.c. spacing, single top plates)
- Window installation in the insulation plane
- Three-dimensional thermal modeling for complex junctions

## Air Leakage and Infiltration

Air leakage through the building envelope drives both energy consumption and moisture transport. The relationship between pressure difference and airflow follows the power law:

Q = C × (ΔP)ⁿ

where Q is volumetric flow rate (m³/s), C is the flow coefficient (m³/s·Paⁿ), ΔP is pressure difference (Pa), and n is the flow exponent (0.5-1.0, typically 0.65 for building envelopes).

**Driving forces for air movement:**

1. **Stack effect:** ΔP = ρ_o × g × h × (T_i - T_o) / T_i
2. **Wind pressure:** ΔP = 0.5 × ρ × C_p × V²
3. **Mechanical system pressurization:** ΔP_mech = supply flow - return flow - exhaust flow

| Climate Zone | Target Airtightness (ACH50) | Equivalent ELA (cm²/m²) |
|--------------|----------------------------|-------------------------|
| Cold (Zone 6-7) | < 1.5 | < 1.0 |
| Mixed (Zone 4-5) | < 3.0 | < 2.0 |
| Hot-Humid (Zone 1-2) | < 5.0 | < 3.5 |
| Passive House | < 0.6 | < 0.4 |
| Commercial Standard | < 0.25 cfm/ft² @ 75 Pa | < 1.3 |

Air leakage testing via blower door establishes building airtightness at standardized pressure (50 Pa). The results inform infiltration load calculations and identify envelope deficiencies requiring remediation.

## Moisture Transport Mechanisms

Moisture moves through building assemblies via vapor diffusion, capillary transport, air leakage, and gravity drainage. Each mechanism operates under different driving forces and time scales.

**Vapor diffusion** follows Fick's Law for one-dimensional steady-state conditions:

g = δ × A × (p₁ - p₂) / d

where g is vapor flow rate (kg/s), δ is vapor permeability (kg/m·s·Pa), and p is vapor pressure (Pa). The vapor diffusion resistance factor μ relates material permeability to air:

μ = δ_air / δ_material

| Material | μ-Value | S_d Value (m) at 100mm |
|----------|---------|------------------------|
| Concrete (dense) | 80-130 | 8-13 |
| OSB | 50-200 | 5-20 |
| Plywood | 30-150 | 3-15 |
| XPS insulation | 80-250 | 8-25 |
| Polyethylene sheet (6 mil) | 100,000+ | 50+ |
| "Smart" vapor retarder | 5-100* | 0.5-10* |
| Latex paint (2 coats) | 5-15 | 0.1-0.3 |

*Smart vapor retarders exhibit humidity-dependent permeability

**Capillary transport** moves liquid water through porous materials under surface tension forces. The capillary absorption coefficient A_w (kg/m²·s^0.5) characterizes this process. Capillary active materials can redistribute moisture, providing beneficial buffering capacity but also pathways for moisture entry.

**Air leakage moisture transport** typically exceeds diffusion by factors of 10-100 in building assemblies. A 1 mm² crack transports 100× more moisture than vapor diffusion through 1 m² of polyethylene vapor barrier under typical winter conditions.

## Condensation Risk Assessment

Interstitial condensation occurs when moisture-laden air reaches its dewpoint temperature within a building assembly. Two complementary methods assess condensation risk:

**Glaser method** (steady-state analysis):
- Calculates temperature and vapor pressure profiles through layered assemblies
- Identifies condensation planes where vapor pressure exceeds saturation
- Appropriate for initial screening in cold climates
- Limitations: ignores moisture storage, assumes steady-state conditions

**Hygrothermal simulation** (dynamic analysis):
- Solves coupled heat and moisture transfer equations with hourly time steps
- Accounts for moisture storage, capillary transport, and variable boundary conditions
- Required for complex assemblies, hygroscopic materials, and challenging climates
- Tools: WUFI, DELPHIN, HygIRC, MOISTURE-EXPERT

**Critical design parameters for condensation prevention:**

1. Interior vapor control (when required): Class I or II vapor retarder on warm side in cold climates
2. Exterior drying potential: vapor-permeable sheathing, air-ventilated cladding
3. Insulation distribution: maintain sheathing temperature above dewpoint
4. Air barrier continuity: prevent moisture-laden air entry to cavities
5. Drainage and flashing: manage bulk water before envelope penetration

## Building Energy Modeling

Building energy simulation tools integrate envelope physics with HVAC system performance to predict annual energy consumption, peak loads, and thermal comfort.

| Software Platform | Calculation Engine | Primary Applications | Complexity Level |
|-------------------|-------------------|----------------------|------------------|
| EnergyPlus | DOE-2 derivative | Whole-building analysis, compliance | Advanced |
| IES-VE | ApacheSim | Integrated design, daylighting | Advanced |
| TRNSYS | Modular components | Research, custom systems | Expert |
| eQUEST | DOE-2.2 | Quick energy estimates | Intermediate |
| DesignBuilder | EnergyPlus GUI | Parametric studies, optimization | Intermediate |
| TRACE 3D Plus | Trane proprietary | HVAC system selection | Intermediate |

**Critical modeling inputs affecting accuracy:**

- **Envelope thermal properties:** U-values including thermal bridging corrections, fenestration SHGC and U-factor, thermal mass heat capacity
- **Air infiltration:** temperature-dependent infiltration rates, wind pressure coefficients, HVAC system pressurization effects
- **Internal gains:** occupancy schedules, plug loads, lighting power density, process equipment diversity
- **HVAC systems:** part-load performance curves, control sequences, ventilation rates, distribution losses
- **Weather data:** TMY3 files for energy analysis, design day data for load calculations

**Output metrics for design decisions:**

1. Peak heating/cooling loads for equipment sizing
2. Annual energy consumption by end use
3. Utility cost estimates with time-of-use rates
4. Thermal comfort indices (PMV, PPD, operative temperature)
5. Parametric sensitivity to envelope improvements
6. Life-cycle cost optimization for integrated design

## Integration with HVAC Design

Building physics analysis directly informs HVAC system design decisions and performance predictions.

**Load calculation refinements:**
- Thermal bridging adds 10-30% to envelope conduction loads in typical construction
- Air leakage contributes 20-40% of heating loads in leaky buildings
- Thermal mass reduces peak cooling loads 5-15% in heavyweight construction
- Solar heat gain varies with glazing orientation, shading, and SHGC selection

**System sizing implications:**
- Improved envelope airtightness reduces equipment capacity requirements 15-40%
- Continuous exterior insulation enables smaller heating equipment and distribution
- Effective air barriers lower humidification/dehumidification loads
- Thermal mass integration enables peak load shifting strategies

**Moisture management coordination:**
- HVAC pressurization strategy must align with envelope air barrier location
- Dehumidification capacity required when envelope prevents drying
- Ventilation air preconditioning needed in extreme climates
- Mechanical systems cannot compensate for fundamental envelope moisture failures

**Commissioning and diagnostics:**
- Infrared thermography identifies thermal bridging and insulation defects
- Blower door testing verifies envelope airtightness targets
- Pressure mapping confirms proper building pressurization under HVAC operation
- Hygrothermal sensors monitor in-service moisture conditions in critical assemblies

Building physics provides the analytical foundation for integrated envelope and HVAC system design. Proper application of heat transfer, air leakage, and moisture transport principles enables energy-efficient, durable, and comfortable buildings while ensuring mechanical systems operate as intended.
