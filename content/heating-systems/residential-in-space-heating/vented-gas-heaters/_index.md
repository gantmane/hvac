---
title: "Vented Gas Heaters"
description: "Technical analysis of vented gas heaters including wall furnaces, floor furnaces, and direct-vent systems with efficiency ratings and installation requirements."
date: "2026-01-04"
weight: 1
tags: ["vented gas heater", "wall furnace", "floor furnace", "direct vent", "gas heating", "residential heating"]
categories: ["Heating Systems"]
---

## Vented Gas Heater Fundamentals

Vented gas heaters combust natural gas or propane while exhausting combustion products outdoors through approved venting systems. Unlike central furnaces, these units heat spaces directly without ductwork distribution, making them suitable for individual rooms, small dwellings, or supplemental heating applications.

Venting configurations determine efficiency, installation requirements, and suitability for specific building types. Atmospherically vented units achieve 60-70% AFUE while consuming indoor air for combustion. Direct-vent sealed combustion systems reach 82-90% AFUE using outdoor air, eliminating draft concerns and building pressurization effects.

## Wall Furnaces

### Design and Operation

Wall furnaces mount in wall cavities with heat exchanger and burner assembly exposed to conditioned space. Combustion products flow through vertical heat exchanger tubes to vent connection at top of cabinet.

**Heat Transfer Mechanisms**
Convective heat transfer from exchanger to room air:

$$Q = h A \Delta T_{lm}$$

Where:
- $Q$ = heat transfer rate (W)
- $h$ = convection coefficient (10-25 W/m²·K for natural convection)
- $A$ = heat exchanger surface area (m²)
- $\Delta T_{lm}$ = log mean temperature difference (K)

Log mean temperature difference:

$$\Delta T_{lm} = \frac{(T_g,in - T_a) - (T_g,out - T_a)}{\ln\left(\frac{T_g,in - T_a}{T_g,out - T_a}\right)}$$

Where:
- $T_g,in$ = entering flue gas temperature (K)
- $T_g,out$ = leaving flue gas temperature (K)
- $T_a$ = ambient air temperature (K)

### Atmospherically Vented Wall Furnaces

**Venting Configuration**
Type B double-wall vent extends from unit through roof or external wall. Draft hood dilutes flue gases with room air, reducing vent temperature and preventing backdrafting during burner shutdown.

Draft hood operation introduces approximately 60-100% excess air:

$$\eta_{max} = 1 - \frac{(1 + r) \cdot m_g c_p (T_f - T_a)}{Q_{input}}$$

Where:
- $r$ = ratio of dilution air to combustion products
- $m_g$ = combustion product mass flow (kg/s)
- $T_f$ = final vent temperature (K)

Typical steady-state efficiency: 65-72%

**Capacity Range**
- Input: 12,000-65,000 BTU/hr
- Output: 8,000-45,000 BTU/hr
- Heating coverage: 400-1,500 square feet

**Installation Requirements**
- Minimum wall cavity depth: 3.5 inches (2x4 framing)
- Clearances to combustibles per listing (typically none required to framing)
- Type B vent sized per manufacturer and NFGC tables
- Combustion air from room (50 ft³ per 1,000 BTU/hr minimum room volume)

### Direct-Vent Wall Furnaces

**Sealed Combustion Design**
Concentric or separated intake/exhaust terminates through exterior wall. Combustion chamber completely isolated from indoor space.

**Efficiency Advantages**
- No draft hood dilution losses
- No indoor air consumption for combustion
- Lower stack temperatures through extended heat transfer
- Typical efficiency: 78-85% AFUE

**Venting System**
Concentric configuration uses inner exhaust pipe surrounded by outer intake air annulus. Heat transfer from exhaust preheats combustion air:

$$Q_{preheat} = \dot{m}_a c_p (T_{a,preheat} - T_{a,outdoor})$$

Reduces net heat loss to approximately 15-22% of input.

**Capacity and Application**
- Input: 10,000-40,000 BTU/hr
- Suitable for tight construction (no infiltration dependency)
- Terminates through wall up to 40 feet from unit
- Requires specific clearances to windows, doors, property lines

### Fan-Assisted Wall Furnaces

**Blower Integration**
Centrifugal fan forces air across heat exchanger, increasing heat transfer coefficient from 12 to 35-50 W/m²·K. Enhanced convection allows:
- Smaller heat exchanger for given capacity
- More uniform heat distribution
- Faster response to thermostat calls

**Performance Impact**
Fan power consumption: 50-150 watts
Heat output increase: 20-35% versus gravity circulation
Net efficiency reduction: 1-2 percentage points

**Noise Considerations**
Sound power levels: 45-55 dBA at 3 feet
Specify low-noise motors (PSC or ECM) for bedroom applications

## Floor Furnaces

### Configuration and Heat Distribution

Floor furnaces install in floor cavities with burner and heat exchanger below floor level. Heated air rises through floor register by natural convection or forced circulation.

**Gravity Floor Furnaces**
Rely entirely on buoyancy-driven flow. Air velocity at register:

$$v = \sqrt{2g H \frac{\Delta T}{T_a}}$$

Where:
- $v$ = air velocity (m/s)
- $g$ = gravitational acceleration (9.81 m/s²)
- $H$ = height of heat exchanger (m)
- $\Delta T$ = temperature rise (K)
- $T_a$ = ambient absolute temperature (K)

Typical velocity: 0.5-1.2 m/s (100-240 fpm)
Air delivery: 150-400 CFM for 25,000-50,000 BTU/hr units

**Forced-Air Floor Furnaces**
Integral blower increases air delivery to 300-800 CFM. Supply ducts can extend to adjacent spaces, expanding heating coverage.

### Venting and Combustion Air

**Type B Venting**
Vertical vent run from draft hood minimizes horizontal offsets. Each 90-degree elbow equivalent to 5-10 feet of vertical rise for draft calculations.

Available draft must exceed resistance:

$$\Delta P_{available} > \Delta P_{vent} + \Delta P_{hood} + \Delta P_{exchanger}$$

**Combustion Air**
Below-floor installation typically provides:
- Perimeter vents to crawlspace: 1 square inch per 1,000 BTU/hr
- Underfloor ventilation reduces moisture accumulation
- Prevents draft interference from wind effects

### Installation Requirements

**Structural Considerations**
- Floor joists must support unit weight (80-150 lbs)
- Minimum clearance to joists: 1 inch (6 inches for reduced clearance models)
- Floor grille must be non-combustible with load rating >250 lbs

**Safety Requirements**
- High-limit switch prevents excessive plenum temperature
- Flame rollout protection (bimetal switch or fusible link)
- Gas valve with 100% shutoff on pilot failure
- Floor grille secured against displacement

**Coverage Limitations**
Single register limits effective coverage:
- Open floor plan: 800-1,200 square feet
- Partitioned spaces: 400-700 square feet
- Stratification losses increase with ceiling height >9 feet

## Direct-Vent Heater Systems

### Design Principles

Direct-vent heaters eliminate chimney requirements through horizontal or vertical venting to outdoors. Sealed combustion chamber prevents any indoor air interaction with combustion process.

**Venting Methods**

**Coaxial Configuration**
- Inner pipe: combustion products exhaust
- Outer pipe: combustion air intake
- Typical diameter: 3-5 inch inner, 5-8 inch outer
- Maximum equivalent length: 40-75 feet

**Separated Pipes**
Two independent pipes for intake and exhaust:
- Greater installation flexibility
- Longer allowable runs (up to 100 feet)
- Lower pressure drop per pipe
- More wall penetrations required

### Efficiency and Performance

**Heat Recovery**
Exhaust gases preheat incoming combustion air through coaxial pipe walls:

$$\eta_{hr} = \frac{T_{air,heated} - T_{air,outdoor}}{T_{exhaust} - T_{air,outdoor}}$$

Heat recovery effectiveness: 15-25%
Reduces net flue losses to 15-18% of input

**Combustion Efficiency**
Advanced models modulate burner input 25-100% capacity:
- Excess air reduced to 30-50% (versus 100-150% for atmospheric)
- Lower stack temperature: 120-180°F versus 300-400°F
- Condensing models achieve 90-95% efficiency

**Turndown Performance**
Modulating burners maintain comfort while reducing cycling losses:

$$CL = \frac{t_{off}}{t_{cycle}} \cdot Q_{jacket}$$

Where:
- $CL$ = cycling loss (BTU/hr)
- $t_{off}$ = off-time per cycle (seconds)
- $t_{cycle}$ = total cycle time (seconds)
- $Q_{jacket}$ = jacket loss rate (BTU/hr)

### Termination Requirements

**Clearance to Building Components**

| Component | Minimum Clearance |
|---|---|
| Windows (above) | 12 inches |
| Windows (beside) | 12 inches |
| Doors | 12 inches |
| Gas meters | 36 inches |
| Electric meters | 36 inches |
| Building corners (inside) | 12 inches |
| Building corners (outside) | Not allowed |
| Grade level | 12 inches |
| Property line | 36 inches |

**Wind and Pressure Effects**
Terminal location must prevent:
- Recirculation of exhaust into air intake
- Excessive wind-induced backdraft
- Snow or ice blockage
- Debris accumulation

Install terminals away from areas subject to drifting snow. Provide minimum 12 inches above anticipated snow depth.

## Ignition and Control Systems

### Pilot Systems

**Standing Pilot**
Continuous small flame (500-1,200 BTU/hr) maintains thermocouple temperature. Pilot outage shuts gas valve through thermoelectric control.

Annual pilot fuel consumption:

$$Q_{pilot,annual} = P_{pilot} \times 8760 \text{ hours}$$

For 800 BTU/hr pilot: 7,008,000 BTU/year ≈ 70 therms

Reduces annual efficiency by 2-5 percentage points depending on heating load.

**Intermittent Pilot**
Electronic ignition lights pilot only on heat calls. Pilot proves before main valve opens, then extinguishes after main flame establishment.

Eliminates off-season pilot consumption, improving annual efficiency by 3-5%.

### Electronic Ignition

**Direct Spark Ignition (DSI)**
High-voltage spark (8,000-25,000V) directly lights main burner. Flame sensing via rectification current confirms ignition before trial-for-ignition period expires (typically 5-15 seconds).

**Hot Surface Ignition (HSI)**
Silicon carbide or silicon nitride element heats to 2,500°F, igniting gas on contact. Element durability: 40,000-100,000 cycles.

Warm-up time: 15-30 seconds
Power consumption: 40-100 watts during warm-up

### Safety Controls

**Oxygen Depletion Sensor (ODS)**
Required on unvented models, optional on vented units for backup safety. Thermocouple positioned in room air monitors oxygen level indirectly through flame temperature.

Depletion to 18% oxygen (from 20.9% normal) cools flame, dropping thermocouple millivoltage below holding threshold, closing gas valve.

**High-Limit Protection**
Manual or automatic reset bimetal switch:
- Open temperature: 175-200°F (direct air discharge models)
- Open temperature: 160-180°F (indirect discharge models)
- Reset differential: 30-50°F

**Flame Rollout Detection**
Switch mounted outside combustion chamber detects flame impingement from blocked vent or excessive draft. Immediate gas shutoff prevents property damage and carbon monoxide production.

## Efficiency Ratings and Seasonal Performance

### AFUE Determination

Annual Fuel Utilization Efficiency accounts for:
1. Steady-state combustion efficiency
2. Cycling losses (on/off operation)
3. Pilot light consumption (standing pilot models)
4. Jacket losses during off-cycles

$$AFUE = \frac{Q_{delivered,annual}}{Q_{input,annual}}$$

**Typical AFUE Values**

| Heater Type | AFUE Range |
|---|---|
| Atmospherically vented | 60-72% |
| Direct-vent | 78-85% |
| Direct-vent condensing | 90-95% |
| Sealed combustion with modulation | 88-92% |

### Part-Load Performance

Heating seasonal efficiency depends on climate and building load:

$$HSE = \frac{AFUE}{1 + (C_D \cdot CDF)}$$

Where:
- $HSE$ = heating seasonal efficiency
- $AFUE$ = annual fuel utilization efficiency
- $C_D$ = degradation coefficient (0.05-0.20)
- $CDF$ = cycling degradation factor based on climate

Modulating burners reduce $C_D$ to 0.02-0.05 versus 0.10-0.15 for single-stage operation.

## Maintenance and Troubleshooting

### Annual Service Procedures

**Combustion Analysis**
Measure with calibrated instruments:
- CO level in flue (target <100 ppm, not to exceed 200 ppm air-free)
- O₂ level (target 6-8% for natural gas)
- Stack temperature
- Draft or pressure differential

Calculate combustion efficiency:

$$\eta_{comb} = 1 - \frac{K \cdot (T_s - T_a)}{%CO_2}$$

Where $K$ = 0.31 for natural gas

**Cleaning Requirements**
- Burner ports and orifice
- Heat exchanger surfaces (wire brush for light deposits)
- Vent connector interior (creosote or soot accumulation)
- Blower wheel and motor (forced-air models)

**Control Verification**
- Thermocouple output: >20 mV hot, <2 mV cold
- Gas pressure at manifold: 3.5 inches w.c. (natural gas), 10-11 inches w.c. (propane)
- Temperature rise across exchanger: within manufacturer specifications
- Safety control operation: manual trip of high-limit and flame rollout switches

### Common Issues and Diagnostics

**Insufficient Heat Output**
- Verify gas pressure at inlet and manifold
- Check orifice sizing for fuel type (natural gas vs propane)
- Inspect heat exchanger for blockage or deformation
- Measure temperature rise (should meet rating plate)

**Short Cycling**
- Oversized for load (most common)
- Thermostat location in warm zone
- Restricted airflow across heat exchanger
- High-limit switch set too low

**Sooting or Incomplete Combustion**
- Insufficient primary air (adjust shutter)
- Blocked vent creating positive pressure
- Cracked or deteriorated heat exchanger
- Wrong orifice size or fuel type

Regular maintenance extends equipment life to 20-30 years and maintains safety and efficiency.
