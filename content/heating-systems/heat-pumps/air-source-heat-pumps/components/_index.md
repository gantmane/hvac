---
title: "Air Source Heat Pump Components"
aliases: ["Air Source Heat Pump Components"]
weight: 1
description: "Comprehensive technical analysis of air source heat pump components including compressors, reversing valves, heat exchangers, expansion devices, defrost controls, and refrigerant charge requirements."
keywords: ["heat pump compressor", "reversing valve operation", "heat pump coils", "expansion valve", "defrost control", "auxiliary heat", "refrigerant charge"]
tags: ["heat pump compressor", "reversing valve operation", "heat pump coils", "expansion valve", "defrost control", "auxiliary heat", "refrigerant charge"]
---

## Air Source Heat Pump Components

Air source heat pumps contain specialized components engineered to enable reversible refrigeration cycles for both heating and cooling operation. The integration of these components determines system efficiency, reliability, and performance across varying ambient conditions.

## Compressor Types

### Scroll Compressors

Scroll compressors dominate residential and light commercial heat pump applications due to their high efficiency and operational reliability. Two involute spiral scrolls compress refrigerant through progressive reduction in gas pockets as the orbiting scroll rotates against the fixed scroll. Efficiency advantages stem from continuous compression without suction and discharge valve losses.

Scroll compressors operate with fewer moving parts than reciprocating designs, reducing wear and mechanical failure potential. Isentropic efficiency typically ranges from 65-75% at design conditions. The absence of suction valves eliminates re-expansion losses inherent in reciprocating compression.

### Rotary Compressors

Single and twin-rotary compressors serve ductless mini-split systems and smaller capacity applications. The rotating cylinder and blade mechanism provides smooth, low-vibration operation. Twin-rotary configurations balance loads and reduce torque pulsations, enabling variable-speed operation across wide capacity ranges.

Rotary compressors achieve competitive efficiency while maintaining compact form factors essential for wall-mounted indoor units. Inverter-driven rotary compressors modulate from 10-130% of nominal capacity in premium systems.

### Variable-Speed Compressor Technology

Inverter-driven compressors using pulse-width modulation adjust motor speed continuously to match thermal loads. This technology eliminates cycling losses and maintains precise temperature control. Seasonal efficiency improvements of 30-50% over single-speed systems result from reduced cycling frequency and optimized part-load operation.

Variable-speed operation extends to pressures and temperatures outside the envelope of fixed-speed designs, enabling heating operation at lower ambient temperatures.

## Reversing Valve

The four-way reversing valve directs hot discharge gas to either the indoor or outdoor coil, establishing heating or cooling mode. The pilot-operated valve contains a sliding piston that redirects refrigerant flow paths in response to solenoid energization.

**Heating Mode:** Discharge gas flows to the indoor coil (condenser). The outdoor coil functions as the evaporator, absorbing heat from ambient air.

**Cooling Mode:** Discharge gas flows to the outdoor coil (condenser). The indoor coil functions as the evaporator, removing heat from conditioned space air.

Valve position is maintained by pressure differential between high and low sides. Solenoid energization in one mode is standard, though manufacturer-specific control schemes vary. The valve introduces approximately 1-2 psi pressure drop in the discharge line.

## Indoor and Outdoor Coils

### Coil Design Parameters

Heat pump coils operate bidirectionally as both evaporators and condensers. Coil circuitry must accommodate refrigerant distribution requirements in both modes while minimizing pressure drop and optimizing heat transfer.

**Face Velocity:** Indoor coils typically operate at 300-450 fpm. Outdoor coils accommodate 400-800 fpm depending on unit configuration.

**Fin Spacing:** Indoor coils use 12-16 fins per inch. Outdoor coils employ 16-20 fins per inch, balancing heat transfer surface area against frost accumulation and cleaning requirements.

**Circuitry:** Multi-circuit designs with refrigerant distributors ensure uniform coil loading. Indoor coils typically contain 2-4 circuits. Outdoor coils may employ 4-8 circuits in larger systems.

### Heat Transfer Considerations

Coil effectiveness depends on the UA product (overall heat transfer coefficient multiplied by surface area). Enhanced surfaces using rifled tubing, lanced fins, and hydrophilic coatings improve heat transfer coefficients by 15-30%.

Air-side pressure drop must not exceed 0.15 in. w.c. for indoor coils to prevent excessive fan power consumption. Outdoor coils tolerate higher pressure drops given larger fan capacity margins.

## Expansion Devices

### Thermostatic Expansion Valves (TXV)

Bi-flow TXVs contain internal check valves enabling refrigerant flow in both directions while maintaining superheat control. The valve modulates in response to superheat at the evaporator outlet, measured by a remote bulb sensing suction line temperature.

Target superheat typically ranges from 8-12°F at the evaporator outlet. The valve adjusts orifice opening to maintain this superheat across varying load conditions, preventing liquid floodback while maximizing coil utilization.

### Electronic Expansion Valves (EEV)

Stepper motor-driven EEVs provide precise superheat control through continuous modulation. Control algorithms adjust valve position based on measured superheat, evaporator pressure, and system operating mode.

EEVs enable superior part-load efficiency by optimizing refrigerant flow at reduced capacities. Response time advantages over TXVs improve system stability during transient conditions and mode changes.

### Capillary Tubes

Fixed-orifice capillary tubes appear in smaller fixed-capacity systems. Flow rate depends solely on pressure differential and refrigerant subcooling, requiring precise charge and careful system matching. Capillary systems use bidirectional flow with different lengths for heating and cooling modes, selected by check valves.

## Defrost Controls

### Defrost Necessity

When outdoor coil temperature falls below 32°F during heating operation, moisture in outdoor air condenses and freezes on coil surfaces. Frost accumulation reduces airflow and heat transfer, degrading heating capacity and efficiency. Defrost cycles reverse system operation temporarily to melt accumulated frost.

### Defrost Initiation Methods

**Time-Temperature Control:** Most common residential approach. Defrost initiates if coil temperature remains below a setpoint (typically 26-32°F) after a timed interval (30-90 minutes of compressor runtime). This prevents unnecessary defrost cycles during conditions that do not promote frost formation.

**Demand Defrost:** Advanced systems monitor performance parameters including coil temperature, pressure drop, and capacity degradation. Defrost initiates only when frost accumulation degrades performance, minimizing energy waste from unnecessary defrost cycles.

### Defrost Sequence

1. Reversing valve switches to cooling mode, directing hot discharge gas to the outdoor coil
2. Outdoor fan de-energizes to accelerate temperature rise
3. Indoor fan typically continues operation, though some designs reduce speed or cycle off
4. Auxiliary heat energizes to offset cooling effect on conditioned space

Defrost termination occurs when outdoor coil temperature reaches 50-65°F or after a maximum time limit (typically 10 minutes). The system then returns to heating mode.

### Defrost Energy Penalty

Each defrost cycle consumes energy and temporarily reduces space temperature. Integrated seasonal performance accounts for defrost penalties through HSPF ratings. Typical defrost cycles consume 3-8% of total heating season energy in moderate climates, increasing to 10-15% in severe cold climates with frequent frosting conditions.

## Auxiliary Heat

Electric resistance heaters supplement heat pump capacity during high load conditions and defrost cycles. Auxiliary heat staging occurs when heat pump capacity proves insufficient to meet thermostat demand.

**Supplementary Heat:** Operates simultaneously with the heat pump to meet loads exceeding heat pump capacity.

**Emergency Heat:** Disables the heat pump compressor, operating electric heat exclusively. Used during compressor failure or extremely low ambient temperatures where heat pump operation becomes ineffective.

Staging control energizes resistance elements in 5-10 kW increments based on thermostat demand and outdoor temperature. Outdoor thermostat lockouts prevent electric heat operation above ambient temperatures where heat pump COP exceeds resistance heating (typically 35-45°F).

## Refrigerant Circuit Components

### Accumulator

The suction accumulator protects the compressor from liquid refrigerant floodback during transient conditions and after defrost cycles. The cylindrical vessel separates liquid refrigerant from suction vapor, allowing only gas to enter the compressor through an internal pickup tube with metering orifice.

A small oil return orifice at the bottom ensures lubricant returns to the compressor. Accumulator sizing provides volume equivalent to 50-100% of system charge, accommodating refrigerant migration during off-cycles.

### Check Valves

Check valves direct refrigerant through specific expansion devices and bypass paths depending on operating mode. In heating mode, refrigerant bypasses one expansion device while flowing through the other. This arrangement optimizes expansion device sizing for each mode's differing mass flow and pressure ratio conditions.

### Bidirectional Filter Driers

Heat pump systems employ bidirectional filter driers containing molecular sieve desiccant that absorbs moisture regardless of flow direction. The desiccant removes water that would otherwise freeze at expansion devices or react with refrigerant and oil, forming acids.

Pressure drop across clean driers should not exceed 2 psi. Excessive pressure drop indicates desiccant saturation or particulate contamination, requiring drier replacement.

### Crankcase Heater

Electric resistance heaters wrapped around the compressor crankcase prevent refrigerant condensation in compressor oil during off-cycles. When system pressure equalizes during shutdown, refrigerant migrates to the coldest location, typically the outdoor compressor in winter.

Crankcase heaters maintain oil temperature 10-20°F above ambient, keeping refrigerant in vapor form. Heater energization during off-cycles consumes 50-150 watts continuously, representing a parasitic energy penalty that must be considered in seasonal efficiency calculations.

## Refrigerant Charge Requirements

### Charging Methods

**Superheat Method:** Used on fixed-orifice systems. Charge adjustment continues until measured superheat matches manufacturer specifications at design conditions (typically 8-15°F for heat pumps).

**Subcooling Method:** Applies to TXV systems. Charge is correct when liquid line subcooling matches specifications (typically 5-15°F) at nominal outdoor conditions.

**Weigh-In Method:** Most accurate approach. Total system charge per nameplate specification is weighed into the system using calibrated charging equipment.

### Charge Sensitivity

Heat pumps exhibit greater charge sensitivity than air conditioners due to bidirectional operation and varying refrigerant distribution between modes. A 10% undercharge reduces heating capacity by 5-10% and efficiency by 3-7%. Overcharge by 10% reduces capacity by 3-5% and efficiency by 2-5%.

Proper charging requires operation in the mode specified by manufacturer procedures (typically cooling mode at 70-95°F outdoor ambient). Charging in heating mode introduces substantial error due to outdoor coil temperature variations and defrost cycle influences.

### Refrigerant Migration

During off-cycles, refrigerant migrates to the coldest system component. In winter, this is typically the outdoor unit. In summer, refrigerant accumulates in the indoor coil. System design must ensure adequate liquid line capacity and receiver volume (accumulator) to accommodate charge migration without liquid accumulation in undesired locations.

Pressure equalization during off-cycles occurs through internal leakage paths in the compressor and expansion device. Full pressure equalization typically requires 5-15 minutes, reducing starting torque requirements for the next compressor cycle.
