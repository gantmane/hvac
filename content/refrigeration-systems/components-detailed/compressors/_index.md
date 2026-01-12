---
title: "Compressors"
weight: 1
description: "Technical analysis of refrigeration compressors including reciprocating, scroll, screw, and centrifugal types. Covers compression thermodynamics, volumetric and isentropic efficiency, capacity control methods, performance characteristics, and maintenance requirements."
---

Compressors function as the primary energy input device in vapor-compression refrigeration cycles, raising refrigerant pressure from evaporator to condenser levels while simultaneously increasing temperature to enable heat rejection. The compressor establishes refrigerant mass flow rate through the system and determines overall system capacity and efficiency.

## Compression Process Thermodynamics

The ideal compression process follows an isentropic path where entropy remains constant (s₁ = s₂). Actual compression involves irreversibilities from friction, heat transfer, and flow losses, resulting in entropy increase. The isentropic efficiency quantifies this deviation:

η_isentropic = (h₂s - h₁) / (h₂ - h₁)

where h₁ is suction enthalpy, h₂ is actual discharge enthalpy, and h₂s is isentropic discharge enthalpy at the same discharge pressure. Typical isentropic efficiencies range from 0.60 to 0.85 depending on compressor type and operating conditions.

Compression work per unit mass equals:

W_comp = h₂ - h₁ = ṁ × cp × (T₂ - T₁)

The discharge temperature for ideal gas approximation follows:

T₂ = T₁ × (P₂/P₁)^((k-1)/k)

where k is the specific heat ratio (cp/cv). For actual processes, discharge temperatures exceed this value due to irreversibilities and superheat gain.

## Volumetric Efficiency

Volumetric efficiency represents the ratio of actual refrigerant mass flow to theoretical displacement capacity. For reciprocating compressors, clearance volume creates re-expansion losses:

η_vol = 1 - C × [(P₂/P₁)^(1/n) - 1]

where C is clearance volume ratio (typically 0.02 to 0.05) and n is polytropic exponent (1.05 to 1.15). Volumetric efficiency decreases with increasing pressure ratio, ranging from 0.85 at low ratios to 0.50 at high compression ratios exceeding 8:1.

Additional factors reducing volumetric efficiency include suction gas superheat, pressure drops through valves and ports, heat transfer from compression chamber walls, and leakage past seals or valve seats.

## Reciprocating Compressors

Reciprocating compressors use pistons driven by crankshaft to compress refrigerant in cylinders. They operate across wide capacity ranges (0.1 to 200+ tons) and pressure ratios up to 10:1 per stage. Multiple cylinder configurations (2, 4, 6, 8 cylinders) provide different capacity steps.

**Advantages:** High efficiency at design point, wide operating envelope, proven reliability, tolerance of liquid slugging, field-serviceable components.

**Limitations:** Pulsating discharge flow, higher vibration levels, capacity steps rather than continuous modulation, oil circulation requirements.

## Scroll Compressors

Scroll compressors employ two spiral-shaped scroll elements—one fixed, one orbiting—creating crescent-shaped pockets that decrease in volume as refrigerant moves from outer to center discharge port. The continuous compression process produces smooth, pulse-free discharge.

Compression ratio is geometrically fixed by scroll geometry, typically 2.5:1 to 3.5:1, making scrolls well-suited for air conditioning applications. Built-in volume ratio matches typical evaporator-to-condenser pressure relationships for R-410A and R-134a systems.

**Advantages:** Fewer moving parts (70% reduction vs reciprocating), high efficiency (5-10% better than reciprocating), low noise and vibration, compact size, tolerance of liquid refrigerant.

**Limitations:** Fixed volume ratio limits high-lift applications, limited capacity modulation options, higher sensitivity to contaminants, non-serviceable hermetic construction.

## Screw Compressors

Rotary screw compressors use intermeshing helical rotors (male and female) in a cylindrical housing. Gas enters at one end, progressively compresses as it moves axially along decreasing volume pockets, and discharges at the opposite end. Twin-screw designs dominate industrial refrigeration (50 to 1500+ tons).

The built-in volume ratio (Vi) represents the geometric compression ratio:

Vi = V_suction / V_discharge

Optimal efficiency occurs when the built-in pressure ratio matches the system pressure ratio. Mismatch causes over-compression (wasted work) or under-compression (discharge port losses).

**Advantages:** Continuous capacity modulation via slide valve (10-100%), oil cooling reduces discharge temperature, high reliability, tolerance of liquid carryover, compact for large capacities.

**Limitations:** Requires oil separation and management systems, efficiency sensitive to Vi matching, higher first cost than reciprocating, rotor clearances critical for performance.

## Centrifugal Compressors

Centrifugal compressors impart kinetic energy to refrigerant through high-speed impellers (15,000-30,000 rpm), then convert velocity to pressure in diffuser sections. Single-stage units provide 1.5:1 to 3:1 pressure ratios; multi-stage designs achieve higher lifts. Capacities range from 150 to 10,000+ tons.

The pressure rise relates to impeller tip speed:

Δh = U²/gc

where U is tip velocity. Surge occurs when flow drops below minimum stable operating point, causing flow reversal and potential mechanical damage. Surge margin of 10-15% is standard safety factor.

**Advantages:** Oil-free compression (magnetic bearings or separate oil system), infinite capacity modulation via inlet guide vanes or VFD, low vibration, high efficiency at full load.

**Limitations:** Surge limits low-load operation (typically 15-20% minimum), efficiency drops significantly at part load, sensitive to refrigerant density, high speed requires precision balancing.

## Capacity Control Methods

### Cylinder Unloading
Reciprocating compressors use solenoid-actuated unloaders to hold suction valves open, preventing compression in selected cylinders. Step control provides 25%, 50%, 75%, 100% capacity (4-cylinder). Part-load efficiency degrades because motor and mechanical losses remain constant.

### Variable Frequency Drives
VFDs modulate compressor speed from 30-100% of design, providing continuous capacity control. Power input reduces approximately with cube of speed reduction at constant pressure ratio. Combines well with scroll and screw compressors. Critical considerations include motor cooling at low speed, minimum oil pressure, and inverter harmonics.

### Hot Gas Bypass
Diverts discharge gas back to evaporator or suction to reduce net refrigeration effect. Simple and inexpensive but highly inefficient—power input remains constant while capacity decreases. Used only for minimum load maintenance or temporary conditions.

### Slide Valve (Screw)
Axial or radial slide valve controls the point where compression begins, effectively varying displacement. Provides 10-100% capacity with better part-load efficiency than unloading.

## Selection Criteria

Application-specific requirements determine optimal compressor type:

| Application | Recommended Type | Rationale |
|-------------|------------------|-----------|
| Residential AC | Scroll, reciprocating | Cost-effective, reliable, appropriate capacity range |
| Commercial AC | Scroll, screw, centrifugal | Efficiency, modulation capability, capacity range |
| Industrial refrigeration | Screw, reciprocating | Ammonia compatibility, wide operating range, reliability |
| Process chillers | Centrifugal, screw | Large capacity, efficiency, oil-free options |
| Low-temperature | Reciprocating, screw (2-stage) | High pressure ratio capability |

Additional selection factors include refrigerant type, ambient conditions, sound level requirements, maintenance access, redundancy needs, and life-cycle cost analysis.

## Performance Characteristics

Compressor performance maps plot capacity, power input, and efficiency against evaporating temperature at various condensing temperatures. Key observations:

- Capacity increases with higher evaporator temperature (increased suction density)
- Capacity decreases with higher condenser temperature (increased compression ratio)
- Efficiency peaks at moderate pressure ratios (typically 2.5:1 to 4:1)
- Power input increases with both higher lift and higher capacity

The coefficient of performance for compression refrigeration:

COP = Q_evap / W_comp = (h₁ - h₄) / (h₂ - h₁)

where h₄ is enthalpy entering evaporator after expansion. Carnot COP provides theoretical maximum:

COP_Carnot = T_evap / (T_cond - T_evap)

## Oil Management

Positive displacement compressors (reciprocating, scroll, screw) require oil for lubrication, sealing, and cooling. Oil inevitably circulates with refrigerant, requiring management systems:

**Oil Separators:** Centrifugal or coalescing designs remove 95-99% of oil from discharge gas. Critical for long refrigerant lines and low-temperature systems where oil return becomes difficult.

**Oil Return:** Proper piping design with minimum gas velocities (700-1500 fpm in vertical risers) ensures oil entrainment back to compressor. Traps and inverted loops require careful attention.

**Oil Cooling:** Screw compressors inject oil directly into compression process for cooling and sealing. External oil coolers (water or refrigerant) maintain 140-180°F oil temperatures.

**Miscibility:** Mineral oil exhibits limited solubility in HFC refrigerants, while POE (polyolester) oils remain miscible. Refrigerant dissolved in oil reduces viscosity and lubricating capacity.

## Maintenance Considerations

Preventive maintenance programs extend compressor life and maintain efficiency:

**Daily/Weekly:** Monitor suction/discharge pressures, temperatures, oil level and pressure, motor current, vibration levels, unusual sounds.

**Monthly:** Oil analysis (acid number, moisture, metal content), refrigerant leak detection, control calibration verification.

**Annual:** Megohm motor winding resistance test, valve inspection and replacement (reciprocating), bearing inspection, alignment verification, oil change.

**3-5 Years:** Complete teardown and rebuild (reciprocating), rotor timing check (screw), impeller balance verification (centrifugal).

Common failure modes include liquid slugging (valve damage, bearing failure), oil breakdown (acid formation, copper plating), refrigerant contamination (moisture, non-condensables), and mechanical wear (bearings, seals, valve plates). ASHRAE Refrigeration Handbook provides detailed maintenance schedules and troubleshooting procedures for each compressor type.

Compressor reliability directly impacts system uptime and operating costs. Proper selection, installation, and maintenance practices ensure design life expectancy of 15-30 years depending on application severity and operating hours.
