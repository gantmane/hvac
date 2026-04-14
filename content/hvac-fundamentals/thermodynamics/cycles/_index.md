---
title: "Cycles"
aliases: ["Cycles"]
weight: 2
---

Thermodynamic cycles form the foundation of all HVAC equipment operation. Understanding these cycles enables proper equipment selection, performance analysis, and optimization. The analysis of real cycles compared to ideal cycles reveals opportunities for efficiency improvements and identifies practical limitations.

## Carnot Cycle

The Carnot cycle represents the maximum theoretical efficiency between two temperature reservoirs. No real cycle can exceed Carnot efficiency, making it the standard for comparison.

**Four Reversible Processes:**

1. Isothermal heat addition at high temperature TH
2. Isentropic expansion from TH to TL
3. Isothermal heat rejection at low temperature TL
4. Isentropic compression from TL to TH

**Carnot COP for Refrigeration:**

COP_Carnot = TL / (TH - TL)

Where temperatures are absolute (Rankine or Kelvin). This equation reveals that smaller temperature differences yield higher efficiency.

**Practical Limitations:**

- Isothermal compression and expansion are impossible to achieve in real equipment
- Infinite heat transfer area required for truly isothermal processes
- Isentropic processes require zero friction and perfect insulation
- Carnot efficiency establishes theoretical maximum only

Real refrigeration cycles achieve 40-60% of Carnot efficiency, while real heat pump cycles achieve 30-50% of Carnot COP.

## Vapor Compression Cycle

The vapor compression cycle is the workhorse of modern air conditioning and refrigeration. It approximates the Carnot cycle using real components and achievable processes.

**Four Actual Processes:**

1. **Isentropic Compression (1-2):** Compressor raises refrigerant pressure and temperature from saturated vapor to superheated vapor
2. **Isobaric Heat Rejection (2-3):** Condenser removes heat at constant pressure; refrigerant exits as saturated or subcooled liquid
3. **Isenthalpic Expansion (3-4):** Expansion device reduces pressure through throttling; refrigerant becomes low-quality two-phase mixture
4. **Isobaric Heat Addition (4-1):** Evaporator absorbs heat at constant pressure; refrigerant exits as saturated vapor

**P-h Diagram Characteristics:**

On a pressure-enthalpy diagram, the vapor compression cycle appears as:
- Vertical line upward (compression) in superheated region
- Horizontal line leftward (condensing) along saturation dome
- Vertical line downward (expansion) crossing into two-phase region
- Horizontal line rightward (evaporating) in two-phase region

The area enclosed represents net work input. The horizontal distance in the evaporator represents cooling capacity.

**Key Performance Parameters:**

| Parameter | Typical Range | Significance |
|-----------|---------------|--------------|
| Evaporator Temperature | 35-50°F cooling | Determines suction pressure |
| Condenser Temperature | 95-120°F | Determines discharge pressure |
| Superheat | 8-15°F | Ensures complete evaporation |
| Subcooling | 5-15°F | Increases capacity, prevents flashing |
| Compression Ratio | 3:1 to 8:1 | Affects compressor efficiency |

**COP Calculation:**

COP_cooling = Q_evaporator / W_compressor = (h1 - h4) / (h2 - h1)

COP_heating = Q_condenser / W_compressor = (h2 - h3) / (h2 - h1)

Where h represents specific enthalpy at each state point.

## Absorption Cycle

Absorption cycles replace mechanical compression with thermal compression using a refrigerant-absorbent pair. Common pairs include lithium bromide-water (LiBr-H2O) and ammonia-water (NH3-H2O).

**Six Primary Processes:**

1. Evaporation at low pressure (produces cooling effect)
2. Absorption of refrigerant vapor into absorbent
3. Solution pumping (minimal mechanical work)
4. Heat addition to generator (drives refrigerant from solution)
5. Condensation at high pressure
6. Expansion back to evaporator pressure

**P-T-X Diagram Analysis:**

Absorption cycles are best represented on pressure-temperature-concentration diagrams showing:
- Crystallization boundaries (prevent solid formation)
- Solution concentration lines
- Vapor pressure relationships
- Operating temperature ranges

**COP for Absorption Systems:**

COP = Q_evaporator / (Q_generator + W_pump)

Since pump work is negligible: COP ≈ Q_evaporator / Q_generator

Typical single-effect COP: 0.6-0.7
Typical double-effect COP: 1.0-1.2

**Advantages:**

- Uses low-grade heat (steam, hot water, direct-fired)
- Minimal moving parts
- Quiet operation
- No CFCs or HCFCs in LiBr systems

**Disadvantages:**

- Lower COP than vapor compression
- Larger physical size
- Crystallization risk with LiBr systems
- Part-load efficiency issues

## Heat Pump Cycles

Heat pump cycles are vapor compression cycles operated to deliver heating rather than cooling. The thermodynamics remain identical, but the condenser becomes the useful heat output.

**Heating Mode Operation:**

- Indoor coil acts as condenser (heat rejection to space)
- Outdoor coil acts as evaporator (heat absorption from ambient)
- Four-way reversing valve switches refrigerant flow direction

**Heating COP Analysis:**

COP_heating = COP_cooling + 1

This relationship holds because the heat rejected includes both the cooling capacity and the compressor work. Heat pumps always have higher COP in heating mode than cooling mode.

**Defrost Cycle:**

When outdoor coil temperature drops below 32°F with sufficient humidity, frost accumulates on the evaporator. Defrost methods include:

1. **Hot Gas Defrost:** Reverse cycle briefly, use hot discharge gas
2. **Electric Defrost:** Resistance heaters melt frost
3. **Time-Temperature Initiation:** Start defrost based on runtime and coil temperature
4. **Demand Defrost:** Monitor pressure drop across coil

Defrost cycles reduce seasonal efficiency by 5-15% depending on climate.

**Balance Point:**

The outdoor temperature where heat pump capacity equals building load. Below balance point, supplemental heat activates. Proper balance point selection affects:
- Equipment sizing
- Operating cost
- Backup heat staging
- Thermal comfort

## COP and Efficiency Analysis

**Coefficient of Performance (COP):**

COP represents the ratio of useful energy output to required energy input. Higher values indicate better performance.

**Cooling COP:**
COP_c = Cooling Capacity / Power Input

**Heating COP:**
COP_h = Heating Capacity / Power Input

**Energy Efficiency Ratio (EER):**
EER = Cooling Capacity (Btu/hr) / Power Input (watts)

Conversion: COP = EER / 3.412

**Seasonal Performance:**

- SEER (Seasonal Energy Efficiency Ratio): Accounts for part-load operation and varying conditions
- HSPF (Heating Seasonal Performance Factor): Includes defrost penalties and auxiliary heat
- IPLV (Integrated Part Load Value): Weighted average at 100%, 75%, 50%, 25% load

**Second Law Efficiency:**

η_II = COP_actual / COP_Carnot

This ratio indicates how closely a real system approaches ideal performance. Values range from 0.3 to 0.6 for most HVAC equipment.

## Cycle Improvements and Optimization

**Subcooling Enhancement:**

Additional subcooling beyond saturation increases refrigerant enthalpy difference across the evaporator. Each °F of subcooling improves capacity by approximately 0.5-1.0%.

Methods:
- Dedicated subcooler heat exchanger
- Liquid-to-suction heat exchanger
- Mechanical subcooling with separate circuit

**Two-Stage Compression:**

For high compression ratios (>6:1), two-stage compression improves efficiency by:
- Reducing discharge temperature
- Minimizing volumetric efficiency losses
- Allowing intercooling between stages

Efficiency improvement: 8-15% compared to single-stage.

**Economizer Cycles:**

Flash economizers or subcooled economizers inject partially expanded refrigerant into the compression process. Benefits include:
- 10-20% capacity increase
- 5-12% efficiency improvement
- Lower discharge temperatures

Best suited for low-temperature applications and scroll or screw compressors.

**Variable Speed Compressors:**

Modulating compressor speed to match load provides:
- Part-load efficiency gains of 15-30%
- Improved humidity control in cooling
- Reduced cycling losses
- Better temperature control

**Hot Gas Bypass (Obsolete):**

Traditional capacity control method now largely abandoned due to:
- Poor part-load efficiency
- Wasted compressor work
- Energy code restrictions

Replaced by variable speed or digital scroll technology.

**Ejector Expansion:**

Replacing expansion valve with ejector recovers expansion work, improving COP by 5-15%. The ejector uses high-pressure liquid to entrain and compress low-pressure vapor from the evaporator outlet.

**Transcritical Cycles (CO2):**

Operating above critical pressure (1070 psia for CO2) eliminates distinct phase change. The P-h diagram shows:
- Supercritical heat rejection (curved line, not horizontal)
- Gliding temperature profiles
- Gas cooler replaces condenser
- Optimal discharge pressure varies with ambient conditions

## Cycle Selection Criteria

**Application Factors:**

| Factor | Vapor Compression | Absorption | Transcritical CO2 |
|--------|-------------------|------------|-------------------|
| COP Range | 2.5-5.0 cooling | 0.6-1.2 cooling | 2.0-4.0 cooling |
| Power Source | Electricity | Thermal energy | Electricity |
| Capacity Range | 1 ton to 10,000 tons | 100 tons to 10,000 tons | 1 ton to 500 tons |
| Maintenance | Moderate | Low | Moderate-High |
| First Cost | Low-Moderate | High | Moderate-High |

**Climate Considerations:**

- Hot, humid climates favor high-efficiency vapor compression with enhanced dehumidification
- Mild climates enable heat pump operation with minimal supplemental heat
- Cold climates require low-temperature heat pump designs or backup systems
- Areas with thermal energy availability benefit from absorption systems

**Load Profile Impact:**

- Constant loads favor simple single-stage systems
- Variable loads require staging, variable speed, or multiple units
- Simultaneous heating-cooling loads enable heat recovery configurations
- Peak demand charges justify thermal storage integration

## Real Cycle Deviations from Ideal

**Compression Process:**

- Actual: Polytropic with heat generation
- Ideal: Isentropic (adiabatic and reversible)
- Impact: 10-20% higher discharge temperature and power consumption

**Expansion Process:**

- Actual: Isenthalpic throttling with pressure drop
- Ideal: Isentropic expansion with work recovery
- Impact: 5-10% capacity loss compared to ideal expansion turbine

**Heat Exchangers:**

- Actual: Finite temperature difference drives heat transfer
- Ideal: Isothermal with zero temperature difference
- Impact: 15-25% reduction in COP due to required temperature lift

**Pressure Drops:**

Friction in piping, heat exchangers, and valves causes pressure loss, requiring additional compression work. Typical impacts:
- Suction line: 1-2 psi drop acceptable
- Discharge line: 2-5 psi drop acceptable
- Liquid line: Minimize to prevent flashing
