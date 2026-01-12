---
title: "Adsorption Refrigeration"
weight: 3
description: "Comprehensive guide to adsorption refrigeration systems using solid adsorbent materials, cycle operation principles, performance analysis, and solar cooling applications."
keywords: ["adsorption refrigeration", "silica gel water system", "zeolite refrigeration", "activated carbon ammonia", "solar cooling", "adsorption cycle", "solid state refrigeration"]
---

Adsorption refrigeration systems utilize solid adsorbent materials to capture and release refrigerant vapor through physical or chemical bonding processes. These thermally-driven cooling systems operate without mechanical compressors, making them suitable for waste heat recovery and solar cooling applications where low-grade thermal energy is available.

## Fundamental Operating Principle

The adsorption refrigeration cycle exploits the reversible adsorption-desorption behavior of refrigerant vapors on porous solid surfaces. During adsorption, refrigerant molecules attach to the adsorbent surface through van der Waals forces (physical adsorption) or chemical bonding (chemisorption), releasing heat. Desorption occurs when thermal energy breaks these bonds, liberating refrigerant vapor for condensation and subsequent cooling.

The cycle operates between four thermal reservoirs: heat source temperature (Tgen = 50-95°C), ambient rejection temperature (Tabs = 25-40°C), cooling water temperature (Tcond = 25-35°C), and evaporator temperature (Tevap = 5-15°C for air conditioning, -10 to 5°C for refrigeration).

## Adsorbent-Refrigerant Pairs

### Silica Gel-Water Systems

Silica gel combined with water represents the most common adsorption pair for air conditioning applications. The microporous structure of silica gel (pore size 2-10 nm) provides surface area of 600-800 m²/g, enabling water uptake of 0.25-0.40 kg H₂O/kg silica gel.

Performance characteristics:
- Regeneration temperature: 50-90°C
- Evaporator temperature: 5-15°C
- COP: 0.3-0.6 under typical conditions
- Cycle time: 300-1500 seconds per bed

The relatively low regeneration temperature makes silica gel-water systems ideal for solar thermal cooling and waste heat applications. Limitations include low refrigeration capacity per unit mass and sensitivity to non-condensable gases.

### Zeolite-Water Systems

Zeolites are crystalline aluminosilicate materials with uniform pore structures (typically 4-10 Å). Common types include zeolite 13X, zeolite 4A, and SAPO-34. Zeolite-water pairs achieve higher temperature lifts than silica gel systems due to stronger adsorption energy.

Operational parameters:
- Regeneration temperature: 150-250°C
- Working capacity: 0.20-0.35 kg H₂O/kg zeolite
- Suitable for ice-making applications (Tevap < 0°C)
- Higher desorption temperature limits use to high-grade heat sources

The strong hydrophilic nature of zeolites requires complete regeneration to prevent performance degradation from residual moisture.

### Activated Carbon-Ammonia Systems

Activated carbon paired with ammonia refrigerant enables operation at sub-zero evaporator temperatures suitable for freezing and cold storage applications. The high latent heat of ammonia (1370 kJ/kg at 0°C) provides greater cooling capacity per unit mass compared to water.

System characteristics:
- Regeneration temperature: 85-150°C
- Evaporator temperature: -30 to 5°C
- Adsorption capacity: 0.15-0.35 kg NH₃/kg carbon
- COP: 0.35-0.55

Safety considerations include ammonia toxicity (OSHA PEL: 50 ppm) and flammability at concentrations of 16-25% by volume. Systems require proper pressure vessel design and leak detection protocols.

### Activated Carbon-Methanol Systems

Activated carbon-methanol pairs offer moderate performance between water and ammonia systems. Methanol's freezing point (-97°C) prevents solidification issues, but lower latent heat (1100 kJ/kg) reduces cooling capacity.

### Metal-Organic Frameworks (MOFs)

Advanced MOF materials such as MIL-101(Cr), HKUST-1, and UiO-66 exhibit surface areas exceeding 3000 m²/g with tunable pore structures. Water uptake can reach 0.5-1.0 kg H₂O/kg MOF, doubling the capacity of conventional silica gel. Current limitations include material cost, long-term stability under cycling conditions, and manufacturing scalability.

## Adsorption and Desorption Isotherms

The relationship between refrigerant uptake (x, kg refrigerant/kg adsorbent) and pressure (P) at constant temperature follows the Dubinin-Astakhov equation:

x = x₀ exp[-(A/E)ⁿ]

where A = RT ln(Psat/P), E represents characteristic energy, and n is the heterogeneity parameter (typically 1-3).

The Clausius-Clapeyron equation governs the vapor pressure relationship:

ln(P) = -ΔHads/(RT) + C

These isotherms determine the working capacity (Δx) between adsorption and desorption conditions, directly impacting system COP and specific cooling power (SCP).

## Cycle Operation Principles

### Intermittent Cycle Operation

The basic intermittent cycle operates with a single adsorbent bed cycling through four distinct phases:

**Phase 1 - Isosteric Heating (Closed Bed):** The saturated adsorbent bed is isolated and heated, increasing pressure from evaporator to condenser level at constant refrigerant concentration.

**Phase 2 - Desorption (Bed Connected to Condenser):** Continued heating drives refrigerant from the adsorbent. Vapor flows to the condenser where it liquefies, rejecting heat to ambient. This phase provides zero cooling output.

**Phase 3 - Isosteric Cooling (Closed Bed):** The regenerated bed is isolated and cooled, decreasing pressure from condenser to evaporator level.

**Phase 4 - Adsorption (Bed Connected to Evaporator):** Refrigerant evaporates in the evaporator, producing the cooling effect. Vapor flows to the cooling adsorbent bed where it adsorbs, releasing heat to ambient. This phase provides the useful refrigeration.

Cycle COP is calculated as:

COP = Qevap / Qgen = λΔx / (cpbed∫ΔT + ΔHadsΔx)

where λ is latent heat, cpbed is bed heat capacity, and ΔHads is heat of adsorption.

Typical intermittent cycle performance:
- Cycle time: 600-2000 seconds
- COP: 0.30-0.45
- Cooling capacity: 50-200 W/kg adsorbent

The intermittent nature results in 50% dead time (phases 1 and 3), limiting practical applications.

### Continuous Cycle Systems

Continuous operation requires at least two adsorbent beds operating 180° out of phase. While one bed undergoes desorption, the other performs adsorption, providing uninterrupted cooling.

Heat recovery between beds improves efficiency:
- Hot regenerated bed preheats the saturated bed entering desorption
- Reduces heat input requirement by 15-30%
- Increases system COP to 0.45-0.60

### Multi-Bed Configurations

Advanced systems employ three or more beds with phase-shifted operation to smooth cooling output and implement cascaded heat recovery. Four-bed systems achieve:
- Reduced temperature swing per bed
- Lower thermal stress and longer component life
- COP improvement of 20-35% over two-bed systems
- Increased system complexity and cost

## Heat and Mass Transfer in Adsorbent Beds

Performance is limited by thermal diffusion within the adsorbent and mass transfer resistance for refrigerant vapor. The characteristic time constants differ significantly:

- Heat transfer time: τh = ρcpR²/(keff) ≈ 100-500 seconds
- Mass transfer time: τm = R²/(Deff) ≈ 10-50 seconds

where R is characteristic bed dimension, keff is effective thermal conductivity (0.1-0.3 W/m·K), and Deff is effective diffusivity.

The low thermal conductivity of adsorbent materials creates thermal resistance that reduces SCP. Enhancement methods include:
- Consolidated composite materials with graphite or metal foam (keff = 1-10 W/m·K)
- Finned tube heat exchangers
- Coated heat exchangers with thin adsorbent layers (0.3-2 mm)

## Solar Cooling Applications

Adsorption chillers match well with solar thermal collectors due to:
- Low regeneration temperatures compatible with flat-plate and evacuated tube collectors
- Cooling demand coinciding with solar availability
- No moving parts in refrigerant circuit (high reliability)

A typical solar adsorption cooling system requires:
- Collector area: 2-4 m²/kW cooling capacity
- Storage tank: 50-100 L/m² collector area
- System COP (cooling/solar): 0.15-0.35 (including collection losses)

Solar fraction (percentage of cooling from solar energy) reaches 70-90% in sunny climates with properly sized thermal storage.

## Performance Comparison with Absorption Systems

| Parameter | Adsorption | Absorption |
|-----------|-----------|-----------|
| Working Principle | Solid-vapor | Liquid-vapor |
| COP | 0.3-0.6 | 0.6-1.2 |
| Driving Temperature | 50-95°C | 70-150°C |
| Moving Parts | Pumps only | Solution pump, refrigerant pump |
| Refrigerant Circulation | Intermittent | Continuous |
| Capacity Modulation | Difficult | Good (10-100%) |
| Part-Load Efficiency | Poor | Good |
| Crystallization Risk | None | Moderate (LiBr-H₂O) |
| Corrosion | Minimal | Moderate to severe |
| Vibration/Noise | Very low | Low |
| Specific Cooling Power | 50-200 W/kg | 100-400 W/kg |

Adsorption systems excel in applications prioritizing reliability, low maintenance, and ultra-low grade heat utilization. Absorption systems provide higher efficiency and capacity when higher temperature heat sources are available.

## System Design Considerations

Effective adsorption refrigeration system design addresses:
- Adsorbent bed thermal management (heat exchanger effectiveness >0.8)
- Vacuum integrity (leak rate < 1 Pa/hr to prevent non-condensable gas buildup)
- Thermal mass minimization (adsorbent mass/total bed mass >0.3)
- Heat recovery effectiveness (temperature approach 5-15°C)
- Control strategy for variable load and heat source conditions

Mass and heat recovery between beds represents the primary opportunity for COP improvement in practical systems, though capital cost increases limit economic viability for small-scale applications.
