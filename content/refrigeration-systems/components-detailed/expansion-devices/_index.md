---
title: "Expansion Devices"
description: "Technical analysis of refrigeration expansion devices including thermostatic expansion valves, electronic expansion valves, capillary tubes, and float valves. Covers throttling thermodynamics, superheat control, sizing methodology, and stability considerations."
weight: 5
---

Expansion devices serve as the critical metering component in vapor-compression refrigeration cycles, reducing refrigerant pressure from condenser to evaporator conditions while regulating refrigerant flow to match system load. The expansion process is fundamentally a throttling process, characterized as isenthalpic (constant enthalpy) with significant entropy generation, representing the primary irreversibility in the refrigeration cycle.

## Throttling Process Thermodynamics

The expansion device operates as an adiabatic throttle, where refrigerant experiences rapid pressure reduction without external work or heat transfer. For steady flow through the expansion device:

**Energy Balance:**
h₁ = h₂

Where h₁ is enthalpy entering the device (subcooled liquid) and h₂ is enthalpy leaving (two-phase mixture). Despite constant enthalpy, the process generates entropy:

**Entropy Generation:**
Δs = s₂ - s₁ > 0

This entropy increase represents lost work potential. The refrigerant exits the expansion device as a low-quality two-phase mixture, with typical quality values of 0.20-0.30 (20-30% vapor by mass). Lower flash gas formation improves cycle efficiency by maximizing liquid refrigerant available for evaporation.

The pressure drop creates a temperature reduction governed by refrigerant saturation properties. For isenthalpic expansion:

**Quality After Expansion:**
x₂ = (h₂ - hf₂) / hfg₂

Where hf₂ is saturated liquid enthalpy and hfg₂ is enthalpy of vaporization at evaporator pressure.

## Thermostatic Expansion Valve (TXV)

The TXV represents the most common modulating expansion device, maintaining constant superheat at the evaporator outlet through mechanical feedback control. Three forces act on the TXV diaphragm:

**Force Balance:**
Pbulb × A = (Pevap + Pspring) × A

Where Pbulb is bulb pressure (sensing superheat), Pevap is evaporator pressure, and Pspring is adjustable spring pressure setting superheat setpoint.

### TXV Operation Principle

The remote bulb, charged with refrigerant or cross-charged fluid, senses suction line temperature. As evaporator superheat increases, bulb pressure rises, opening the valve to admit more refrigerant. This negative feedback loop maintains superheat at the spring setting, typically 4-8°C (7-14°F) for DX systems.

The TXV opening responds to:
- Superheat deviation from setpoint (primary control)
- Evaporator pressure changes (compensated by internal/external equalizer)
- Liquid line pressure variations (compensated by subcooling)

**Superheat Setpoint:**
ΔTsh,set = Tspring / Kbulb

Where Tspring is spring force equivalent temperature and Kbulb is bulb charge constant.

### Static and Operating Superheat

**Static Superheat:** Minimum superheat required to overcome spring force and begin valve opening, typically 2-4°C (3.5-7°F).

**Operating Superheat:** Additional superheat beyond static value required for full valve opening, typically 2-4°C (3.5-7°F).

**Total Superheat:** Sum of static and operating superheat, typically 4-8°C (7-14°F) at design conditions.

### Internal vs. External Equalizer

Internal equalizer TXVs sense evaporator inlet pressure, suitable for systems with minimal evaporator pressure drop (< 0.3 bar / 5 psi). External equalizer connections sense evaporator outlet pressure, compensating for significant pressure drop through the evaporator and preventing refrigerant starvation. External equalizers are required for:
- Evaporator pressure drop > 0.3 bar (5 psi)
- Distributor-fed evaporators
- Suction line heat exchangers present

### TXV Adjustment Procedures

Superheat adjustment requires systematic approach:

1. Measure suction line temperature 15-30 cm (6-12 inches) from bulb location
2. Measure suction pressure and convert to saturation temperature
3. Calculate superheat: ΔTsh = Tsuction - Tsat,evap
4. Adjust spring tension (clockwise increases setpoint, counterclockwise decreases)
5. Allow 10-15 minutes stabilization between adjustments
6. Verify adjustment across load range

Excessive superheat (> 10°C / 18°F) indicates valve underfeeding, reducing capacity and potentially overheating the compressor. Insufficient superheat (< 3°C / 5°F) risks liquid floodback and compressor damage.

## Electronic Expansion Valve (EEV)

EEVs employ stepper motor or pulse-width modulated actuators to position the valve pin, controlled by microprocessor logic analyzing multiple inputs: suction temperature, suction pressure, liquid temperature, and discharge conditions. This multi-parameter control enables superior performance compared to TXVs.

### EEV Advantages

**Precise Superheat Control:** EEVs maintain superheat within ±0.5°C (±1°F), compared to ±2°C (±3.5°F) for TXVs, maximizing evaporator utilization without liquid floodback risk.

**Load Adaptability:** Electronic control algorithms adjust opening rates based on load changes, preventing hunting during transient conditions.

**Capacity Enhancement:** Tighter superheat control increases effective evaporator surface area, improving capacity 3-8% compared to TXV systems.

**Multi-Evaporator Coordination:** Central controllers optimize refrigerant distribution across multiple evaporators based on individual demands.

**Diagnostic Capability:** Continuous monitoring enables fault detection, predictive maintenance, and system optimization.

### EEV Control Algorithms

Proportional-integral (PI) or PID control calculates valve position:

**PI Control:**
Position = Kp × e(t) + Ki × ∫e(t)dt

Where e(t) is superheat error, Kp is proportional gain, and Ki is integral gain. Derivative action (D) adds predictive response to rapid load changes.

## Capillary Tube

Capillary tubes are fixed-orifice devices consisting of small-diameter copper tubing (0.5-2.0 mm / 0.020-0.080 inch ID) with lengths of 1-6 meters (3-20 feet). Refrigerant flow is governed by tube geometry and pressure differential, with no modulation capability.

### Capillary Tube Characteristics

**Flow Equation (Simplified):**
ṁ = K × √(ΔP × ρ)

Where ṁ is mass flow rate, K is tube flow coefficient (function of diameter and length), ΔP is pressure differential, and ρ is refrigerant density.

Flow capacity depends on:
- Tube inside diameter (most significant factor, flow proportional to d⁴)
- Tube length (longer length reduces flow)
- Refrigerant subcooling (increased subcooling increases capacity)
- Pressure differential (higher ΔP increases flow)

### Capillary Tube Applications

Capillary tubes suit fixed-load applications:
- Domestic refrigerators and freezers
- Small window air conditioners
- Dehumidifiers
- Beverage coolers

Advantages include low cost, no moving parts, and pressure equalization during off-cycle (reducing compressor starting torque). Disadvantages include fixed capacity, no superheat control, and sensitivity to refrigerant charge. Critical charge systems require precise refrigerant quantity (±2-5%).

### Capillary Tube Sizing

Proper sizing matches compressor capacity at design conditions. Undersized tubes starve the evaporator, while oversized tubes flood the compressor. ASHRAE provides correlation charts for common refrigerants. Iterative calculations or manufacturer selection software account for two-phase flow complexity.

## Float Valves

Float valves maintain constant liquid level in the evaporator (low-side float) or receiver (high-side float) through mechanical level sensing.

### Low-Side Float Valve

Installed in the evaporator or surge drum, the low-side float opens as liquid level drops, admitting refrigerant to maintain level. This ensures continuous liquid availability for evaporator flooding. Applications include:
- Flooded shell-and-tube evaporators
- Liquid overfeed systems
- Industrial ammonia systems

### High-Side Float Valve

Located after the condenser, the high-side float drains condensed liquid as it accumulates, preventing condenser flooding. The evaporator receives all condensed refrigerant, requiring critical charge matching. Limited to systems where evaporator can safely hold entire refrigerant charge.

## Expansion Device Selection Criteria

Selection depends on application requirements, system type, and control precision needs:

| Device Type | Capacity Range | Control Precision | Load Variation | Cost | Typical Applications |
|-------------|---------------|-------------------|----------------|------|---------------------|
| TXV | 0.5-500+ TR | Moderate (±2°C) | Good | Medium | DX systems, commercial refrigeration |
| EEV | 0.2-500+ TR | Excellent (±0.5°C) | Excellent | High | Variable load, heat pumps, precision control |
| Capillary Tube | < 5 TR | None (fixed) | Poor | Low | Fixed load, residential units |
| Float Valve | 5-500+ TR | Level control | Good | Medium | Flooded evaporators, industrial systems |

### Sizing Methodology

Expansion devices must satisfy capacity at design conditions while maintaining stability across operating range. TXV and EEV sizing requires:

**Capacity Requirement:**
Q̇evap = ṁref × (hevap,out - hevap,in)

Select valve with capacity rating 10-25% above calculated requirement to ensure adequate control range. Undersizing causes excessive superheat, while oversizing may cause hunting.

Manufacturers provide capacity tables based on:
- Refrigerant type
- Evaporator temperature
- Pressure drop across valve (ΔP = Pcond - Pevap)
- Liquid subcooling entering valve

**Valve Capacity Correction:**
Qcorrected = Qrated × Fref × Fsubcool × Fpress

Where correction factors account for non-standard conditions.

## Hunting and Stability Issues

Hunting describes oscillatory behavior where the expansion device alternately over-feeds and under-feeds refrigerant, causing cyclical superheat variations. This instability results from:

### Hunting Causes

**System Dynamics:** Time delays between valve adjustment and superheat response at the bulb location create control loop instability. Long evaporators or low refrigerant velocities exacerbate delays.

**Oversized Valves:** Excessive capacity makes valves overly responsive, with small position changes causing large flow variations.

**Improper Bulb Location:** Bulb placement in cold spots or inadequate thermal coupling causes erratic sensing.

**Refrigerant Migration:** Off-cycle migration concentrating liquid in evaporator causes flooding at startup.

**Load Fluctuations:** Rapid load changes exceeding valve response capability.

### Stability Solutions

1. **Valve Downsizing:** Select smallest valve meeting capacity requirements
2. **Bulb Relocation:** Position bulb on horizontal suction line section, away from liquid traps
3. **Bulb Mounting:** Ensure solid thermal contact (10 o'clock or 2 o'clock position on horizontal lines > 22 mm OD, 4-8 o'clock on lines < 22 mm OD)
4. **External Equalizer:** Eliminates evaporator pressure drop influence
5. **Distributor Nozzles:** Properly sized distributors ensure even refrigerant distribution
6. **Suction Accumulator:** Provides liquid buffering capacity
7. **EEV Upgrade:** Electronic control with adaptive algorithms prevents hunting

## Application Guidelines by System Type

### Direct Expansion (DX) Air Conditioning

TXVs or EEVs with external equalizers. Superheat setting: 4-7°C (7-12°F). Bulb location: suction line exit from evaporator, well-insulated. Consider EEVs for:
- Variable-speed compressors
- Heat pump applications
- High-efficiency requirements

### Commercial Refrigeration

TXVs standard for medium and low-temperature applications. Superheat settings: medium temp (2-7°C) 3-6°C (5-10°F), low temp (-18 to -29°C) 5-8°C (9-14°F). Multiple evaporators require individual valves or EPR valves for temperature control.

### Flooded Evaporator Systems

Low-side float or recirculation pumps with liquid level control. Typical applications: chillers, ice rinks, industrial processes. Provides maximum heat transfer efficiency through complete surface wetting.

### Heat Pump Systems

Bidirectional TXVs or EEVs required for reversing cycle operation. Check valves bypass expansion device in reverse mode. EEVs preferred for:
- Wide operating temperature range
- Defrost cycle optimization
- Improved part-load efficiency

### Transport Refrigeration

TXVs selected for vibration resistance and wide ambient range. External equalizers mandatory due to evaporator pressure drop. Consider dual-capacity or dual-setpoint valves for multi-temperature applications.

## References

ASHRAE Handbook—Refrigeration (2022), Chapter 11: Refrigerant-Control Devices provides detailed expansion device theory, selection, and application guidance. Manufacturer technical bulletins offer specific product selection software and installation requirements for optimal performance.
