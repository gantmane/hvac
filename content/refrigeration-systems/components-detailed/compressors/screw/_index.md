---
title: "Screw Compressors"
aliases: ["Screw Compressors"]
weight: 3
description: "Technical guide to screw compressors covering twin-screw and single-screw designs, rotor profiles, volume ratio, capacity control, oil management, and applications in chillers and industrial refrigeration systems."
keywords: "screw compressor, twin screw compressor, single screw compressor, rotor profile, volume ratio, slide valve, oil injection, oil separator, capacity control, industrial refrigeration, chiller compressor"
tags: ["screw compressor", "twin screw compressor", "single screw compressor", "rotor profile", "volume ratio", "slide valve", "oil injection", "oil separator", "capacity control", "industrial refrigeration"]
---

Screw compressors are positive displacement machines that compress refrigerant through the meshing action of helical rotors. These compressors dominate medium to large capacity applications due to continuous compression, high volumetric efficiency, and excellent part-load performance.

## Twin-Screw Compressors

Twin-screw compressors utilize two intermeshing helical rotors rotating in opposite directions within a fixed housing. The male rotor typically has 4-6 lobes, while the female rotor has 5-7 flutes. As the rotors mesh, refrigerant vapor is trapped between the rotor surfaces and the housing, progressively compressed as the trapped volume decreases along the rotor length.

The compression process occurs in three phases:
1. **Suction**: Refrigerant enters through the suction port, filling the spaces between rotor lobes
2. **Compression**: Rotation reduces trapped volume, increasing pressure and temperature
3. **Discharge**: Compressed refrigerant exits when the volume reaches the discharge port

Twin-screw units achieve capacities from 20 to 5,000+ tons, with continuous operation at single speed producing smoother flow than reciprocating compressors. The absence of suction and discharge valves eliminates re-expansion losses and mechanical valve failures.

## Single-Screw Compressors

Single-screw compressors employ one helical main rotor with helical grooves engaging two star-shaped gate rotors positioned on opposite sides. The main rotor typically has six grooves, while each gate rotor has 11 teeth. This configuration creates two separate compression chambers operating 180° out of phase.

Key advantages include:
- Balanced radial forces (no net bearing load perpendicular to shaft axis)
- Lower vibration compared to twin-screw designs
- Reduced bearing loads extend service life
- Symmetrical compression chambers improve volumetric efficiency

Single-screw designs achieve 5-10% higher isentropic efficiency than comparable twin-screw units at full load due to superior sealing and balanced loading. Applications range from 100 to 1,500 tons.

## Rotor Profiles

Rotor profile geometry directly affects efficiency, reliability, and manufacturing precision. Modern profiles result from computational optimization targeting minimum leakage, balanced loads, and efficient oil distribution.

**Asymmetric Profiles**: Male and female rotors have different lobe geometries optimized independently. Asymmetric designs reduce blow-hole area (the gap between rotors through which high-pressure gas leaks back to suction), improving volumetric efficiency by 2-4% compared to symmetric profiles. The male rotor generates more of the compression work, creating unbalanced radial loads on bearings.

**Symmetric Profiles**: Both rotors share identical geometric relationships, simplifying manufacturing and reducing costs. Symmetric designs exhibit balanced forces but higher leakage paths. These profiles are common in older compressors and cost-sensitive applications.

Modern asymmetric profiles (4/6 and 5/6 lobe combinations) dominate new installations, with profile-specific machining compensating for manufacturing complexity through superior efficiency gains.

## Volume Ratio (Vi)

Built-in volume ratio (Vi) is the ratio of trapped volume at the start of compression to volume at discharge port opening:

Vi = V_suction / V_discharge

Typical Vi values range from 2.2 to 5.5. Optimal Vi matches the pressure ratio across the compressor:

Pressure Ratio = (P_discharge / P_suction) = Vi^γ

where γ is the specific heat ratio (approximately 1.15 for common refrigerants).

**Under-compression** occurs when Vi is too low for the operating pressure ratio. Gas pressure remains below discharge pressure when the discharge port opens, requiring additional compression in the discharge plenum. Energy is wasted as high-pressure discharge gas rushes back into the compression chamber.

**Over-compression** occurs when Vi is too high. Gas pressure exceeds discharge pressure before port opening, with excess energy dissipated as turbulence and heat when the volume opens to discharge.

Fixed Vi compressors are optimized for specific applications. Variable Vi systems use sliding discharge port mechanisms to adjust volume ratio for varying operating conditions, maintaining efficiency across 15-30% wider operating ranges.

## Slide Valve Capacity Control

Slide valves provide stepless capacity modulation from 100% down to 10% of full load by varying the effective compression length. A sliding bar in the compressor housing moves axially, creating a bypass port that allows compressed refrigerant to return to suction before reaching full pressure.

At reduced capacity positions:
- Gas trapped between rotors is released back to suction at intermediate pressure
- Effective displacement decreases proportionally to slide position
- Power consumption reduces approximately linearly with capacity
- Refrigerant mass flow decreases while pressure ratio remains constant

Part-load efficiency remains high (85-95% of full-load efficiency) because compression work is only performed on the fraction of gas that completes full compression. Response time is 2-5 seconds, enabling precise matching to load variations.

Some designs incorporate dual slide valves: one for capacity control and a second for Vi adjustment, optimizing efficiency across the entire operating envelope.

## Oil Injection and Cooling

Oil injection serves multiple critical functions in screw compressors:

1. **Sealing**: Oil fills clearances between rotors and housing, minimizing internal leakage
2. **Cooling**: Injected oil absorbs compression heat, reducing discharge temperature by 40-60°F
3. **Lubrication**: Oil film protects bearings and rotor surfaces from wear
4. **Noise Reduction**: Oil dampens vibration and reduces compression noise

Oil is injected at 50-100 psig above suction pressure through multiple ports along the compression chamber. Typical oil flow rates are 2-5 gallons per ton of refrigeration. Injection temperature is controlled at 100-140°F to maintain proper viscosity.

The cooling effect enables higher pressure ratios (up to 20:1) in single-stage compression compared to 4-5:1 for dry compressors. Discharge temperatures remain below 220°F, well within safe limits for most refrigerants and lubricants.

## Oil Separation

Discharge gas exiting the compressor carries entrained oil requiring removal before entering the condenser. Multi-stage separation achieves less than 5 ppm oil carryover:

**Primary Separation**: Centrifugal separator removes bulk oil (95-98%) through velocity reduction and directional change. Gas enters tangentially, creating rotational flow that centrifuges oil droplets to the separator wall.

**Secondary Separation**: Coalescent filters capture fine oil mist. Gas passes through filter media where small droplets coalesce into larger drops that drain by gravity.

Separated oil returns to the compressor through pressure differential or dedicated oil pump, passing through an oil cooler to remove absorbed heat. Oil temperature entering the compressor is maintained at the setpoint through modulating water flow or variable speed oil pump control.

Oil management system pressure drop is 2-5 psi, representing minor parasitic loss relative to separation benefits.

## Efficiency Characteristics

Screw compressor isentropic efficiency typically ranges from 0.65 to 0.75, with best-in-class units achieving 0.78-0.80 at design conditions. Efficiency depends on:

- **Rotor profile quality**: Modern asymmetric profiles provide 3-5% improvement
- **Built-in volume ratio match**: Proper Vi selection maintains efficiency within ±2% of optimum
- **Clearances**: Tight tolerances reduce leakage but increase friction; optimal clearance is 0.003-0.006 inches
- **Oil injection rate**: Adequate oil improves sealing but excessive oil increases pumping losses
- **Speed**: Higher tip speeds (150-200 ft/s) improve efficiency but increase wear

Part-load efficiency exceeds reciprocating and centrifugal compressors due to capacity modulation without cylinder unloading or speed reduction penalties. At 50% capacity, efficiency typically remains at 90-95% of full-load values.

## Applications

**Water-Cooled Chillers**: Twin-screw compressors dominate 100-1,500 ton water-cooled chiller applications. Semi-hermetic designs integrate motor and compressor in a common housing with refrigerant cooling. Full-load efficiency (kW/ton) of 0.50-0.60 competes favorably with centrifugal machines in this capacity range while offering superior part-load performance and lower first cost.

**Air-Cooled Chillers**: Screw compressors handle the higher pressure ratios (12-15:1) of air-cooled systems better than reciprocating units. Multiple compressors provide redundancy and improved part-load efficiency through staging.

**Industrial Refrigeration**: Open-drive screw compressors with external motors dominate cold storage, food processing, and chemical applications from -40°F to +40°F evaporator temperatures. Ammonia, R-507A, and CO₂ systems use screw compressors from 50 to 3,000+ HP. Economizer ports enable two-stage compression in single-casing design, improving efficiency by 10-15% at low evaporator temperatures.

**Process Cooling**: Chemical, pharmaceutical, and data center applications requiring precise temperature control and high reliability utilize screw compressor packages with redundant oil systems, vibration monitoring, and rapid capacity response.

Screw compressor market share continues growing due to improving efficiency, declining manufacturing costs, and integration with variable frequency drives for optimized part-load performance.
