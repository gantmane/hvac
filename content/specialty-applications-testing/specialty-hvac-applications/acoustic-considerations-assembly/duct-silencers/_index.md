---
title: "Duct Silencers for HVAC Systems"
description: "Technical guide to rectangular and circular duct silencers including insertion loss data, pressure drop calculations, self-noise generation, and selection criteria for HVAC acoustic control."
keywords: "duct silencers, HVAC silencers, insertion loss, pressure drop, acoustic attenuation, rectangular silencers, circular silencers, self-noise generation, sound attenuation, dissipative silencers"
weight: 2
---

Duct silencers reduce airborne sound transmission in HVAC ductwork through acoustic absorption and reflection mechanisms. Proper silencer selection balances acoustic performance, pressure drop, physical constraints, and self-noise generation to achieve target noise criteria in occupied spaces.

## Silencer Types and Construction

**Rectangular Silencers**

Rectangular silencers consist of parallel baffle assemblies inserted into rectangular duct sections. Each baffle contains sound-absorptive material (typically glass fiber or mineral wool) encased in perforated metal facing. The airway passages between baffles provide acoustic treatment while maintaining airflow.

Standard baffle configurations:
- Splitter width: 4 to 6 inches (100 to 150 mm)
- Airway width: 4 to 8 inches (100 to 200 mm)
- Active length: 3, 5, 7, or 10 feet (0.9, 1.5, 2.1, 3.0 m)

**Circular Silencers**

Circular silencers feature a center pod or annular ring of absorptive material within a circular duct section. The center pod design positions absorptive media along the duct centerline, creating an annular airflow passage. Pod diameter typically ranges from 40% to 60% of the duct diameter.

**Dissipative vs. Reactive Silencers**

Dissipative silencers utilize fibrous absorptive materials to convert acoustic energy into heat through viscous and thermal losses. These devices provide broadband attenuation with effectiveness increasing at higher frequencies.

Reactive silencers employ geometry changes (expansion chambers, resonators) to reflect sound energy back toward the source. While effective at specific frequencies, reactive silencers offer limited broadband performance and see minimal use in standard HVAC applications.

## Insertion Loss Performance

Insertion loss (IL) quantifies the sound power level reduction achieved by installing a silencer, measured in decibels across octave frequency bands. Performance depends on silencer length, airway dimensions, absorptive material properties, and frequency.

**Typical Insertion Loss Values (dB)**

| Silencer Length | 125 Hz | 250 Hz | 500 Hz | 1000 Hz | 2000 Hz | 4000 Hz |
|-----------------|--------|--------|--------|---------|---------|---------|
| 3 ft (0.9 m)    | 3-5    | 6-9    | 12-16  | 18-23   | 22-28   | 24-30   |
| 5 ft (1.5 m)    | 5-8    | 10-14  | 18-24  | 26-33   | 30-38   | 32-40   |
| 7 ft (2.1 m)    | 7-10   | 13-18  | 22-30  | 32-41   | 36-46   | 38-48   |
| 10 ft (3.0 m)   | 9-13   | 17-23  | 28-37  | 38-49   | 42-54   | 44-56   |

Values represent parallel baffle silencers with 4-6 inch airways and glass fiber fill density of 3-6 lb/ft³ (48-96 kg/m³).

**Attenuation Characteristics**

Low frequency attenuation (63-250 Hz) remains limited due to the long wavelengths relative to absorptive material thickness. Effective low-frequency control requires longer silencers or increased airway treatment area.

Mid-to-high frequency attenuation (500-4000 Hz) demonstrates strong performance where absorptive materials efficiently dissipate acoustic energy. Silencer length directly correlates with insertion loss—doubling length increases attenuation by approximately 3-6 dB per octave band.

The relationship between insertion loss and silencer parameters follows:

**IL = α × L × (P/A)**

Where:
- IL = insertion loss (dB)
- α = absorption coefficient (frequency dependent)
- L = active silencer length (ft or m)
- P = perimeter of absorptive surface (ft or m)
- A = free airway area (ft² or m²)

## Pressure Drop Calculations

Silencer pressure drop results from friction losses as air passes through restricted airways. Higher face velocities and longer silencers increase pressure drop, imposing fan energy penalties.

**Pressure Drop Formula**

ΔP = K × (V²/2g) × ρ × (L/D_h)

Where:
- ΔP = pressure drop (inches w.c. or Pa)
- K = loss coefficient (0.8 to 1.5 for dissipative silencers)
- V = face velocity (fpm or m/s)
- g = gravitational constant (32.2 ft/s² or 9.81 m/s²)
- ρ = air density (lb/ft³ or kg/m³)
- L = silencer length (ft or m)
- D_h = hydraulic diameter of airway (ft or m)

**Simplified Calculation**

For standard rectangular silencers at sea level:

ΔP (in w.c.) = 0.00001 × V² × L × CF

Where:
- V = face velocity (fpm)
- L = active length (feet)
- CF = configuration factor (1.0 to 1.3)

**Typical Pressure Drop Values**

| Face Velocity | 3 ft Silencer | 5 ft Silencer | 7 ft Silencer | 10 ft Silencer |
|---------------|---------------|---------------|---------------|----------------|
| 1000 fpm      | 0.05 in w.c.  | 0.08 in w.c.  | 0.12 in w.c.  | 0.17 in w.c.   |
| 1500 fpm      | 0.11 in w.c.  | 0.19 in w.c.  | 0.26 in w.c.  | 0.38 in w.c.   |
| 2000 fpm      | 0.20 in w.c.  | 0.33 in w.c.  | 0.47 in w.c.  | 0.67 in w.c.   |
| 2500 fpm      | 0.31 in w.c.  | 0.52 in w.c.  | 0.73 in w.c.  | 1.04 in w.c.   |

Pressure drop increases with the square of velocity—doubling velocity quadruples pressure drop.

## Self-Noise Generation

Self-noise occurs when airflow through the silencer generates turbulence at the perforated facing or within airways. This regenerated noise can exceed the insertion loss benefit, particularly at high velocities.

**Critical Velocity Limits**

Maximum recommended face velocities to prevent excessive self-noise:

- NC 25-30 spaces: 1500 fpm (7.6 m/s)
- NC 30-35 spaces: 2000 fpm (10.2 m/s)
- NC 35-40 spaces: 2500 fpm (12.7 m/s)
- NC 40+ spaces: 3000 fpm (15.2 m/s)

Self-noise increases approximately 18 dB per doubling of velocity. A silencer operating at 2000 fpm generates about 18 dB more self-noise than the same unit at 1000 fpm.

## Selection Criteria and Design Process

**Step 1: Establish Acoustic Requirements**

Determine target noise criteria (NC or RC) for the occupied space and calculate required attenuation per octave band based on equipment sound power levels and duct end attenuation.

**Step 2: Calculate Required Insertion Loss**

IL_required = Lw_equipment - A_duct - A_terminal + NR - NC_target

Where:
- Lw_equipment = equipment sound power level (dB)
- A_duct = duct natural attenuation (dB)
- A_terminal = terminal device attenuation (dB)
- NR = room effect (dB)
- NC_target = target noise criterion level (dB)

**Step 3: Preliminary Silencer Sizing**

Select silencer length based on required insertion loss in critical octave bands (typically 500-2000 Hz). Determine face area based on airflow and velocity constraints.

Face Area = CFM ÷ Maximum Velocity (fpm)

**Step 4: Verify Pressure Drop**

Calculate pressure drop using manufacturer data or formulas. Ensure total system pressure drop remains within fan capacity. Consider upsizing silencer face area if pressure drop exceeds 0.5 inches w.c.

**Step 5: Check Self-Noise**

Verify face velocity remains below limits for target noise criteria. Manufacturer data provides self-noise power levels for specific silencer models and velocities.

**Step 6: Physical Integration**

Confirm available space for silencer length, access requirements for future media replacement, and structural support for silencer weight (typically 8-15 lb/ft² for parallel baffle units).

## Installation Requirements

Maintain straight duct runs equal to 1.5 times duct diameter upstream and downstream of silencers to ensure uniform airflow distribution. Elbows, dampers, or transitions placed too close create turbulence that degrades acoustic performance and increases self-noise.

Seal all joints between silencer sections and connecting ductwork to prevent acoustic flanking paths. Unsealed joints can reduce effective insertion loss by 3-6 dB.

Support silencers independently from ductwork using dedicated structural supports. Do not rely on duct hangers alone—silencer weight can overstress duct connections.

## ASHRAE References

Detailed silencer performance data, calculation methods, and application guidance appear in ASHRAE Handbook—HVAC Applications, Chapter 49 (Sound and Vibration Control). Testing procedures follow ASTM E477 (Standard Test Method for Laboratory Measurement of Acoustical and Airflow Performance of Duct Liner Materials and Prefabricated Silencers).

Manufacturers provide certified test data showing insertion loss, pressure drop, and self-noise for specific models and operating conditions. Selection software from major manufacturers incorporates ASHRAE methods for system-specific analysis.
