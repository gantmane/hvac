---
title: "Ignition Systems"
weight: 4
description: "Comprehensive guide to gas furnace ignition systems including standing pilot, intermittent pilot, direct spark ignition, hot surface ignition, transformers, electrode positioning, and troubleshooting procedures."
keywords: ["ignition systems", "hot surface ignition", "direct spark ignition", "intermittent pilot", "standing pilot", "ignition transformer", "electrode positioning", "ignition troubleshooting", "flame sensing", "silicon carbide igniter"]
---

Ignition systems initiate and maintain combustion in gas-fired heating equipment. Modern ignition technology has evolved from continuous pilot flames to electronic systems that improve efficiency and reliability while reducing energy consumption.

## Standing Pilot Systems

Standing pilot ignition maintains a continuous flame throughout the heating season. The pilot flame provides instantaneous ignition of the main burner when the thermostat signals for heat.

### Operational Characteristics

The pilot burner operates 24 hours per day, consuming approximately 500-1,000 Btu/hr depending on orifice size and gas pressure. Annual pilot gas consumption ranges from 4-9 therms for natural gas systems. The pilot flame heats a thermocouple or thermopile that generates millivoltage signals for safety control.

### Thermocouple Operation

Standard thermocouples generate 20-30 millivolts when properly heated. The DC voltage holds open an electromagnetically operated safety valve. If the pilot flame extinguishes, thermocouple output drops below the minimum holding voltage (typically 8-12 mV) within 30-60 seconds, closing the main gas valve.

### Thermopile Systems

Thermopiles consist of multiple thermocouples connected in series, generating 500-750 millivolts. Higher voltage output enables direct operation of 24V gas valves without external power. Thermopile systems provide power for control circuits in millivoltage systems used in wall furnaces and space heaters.

## Intermittent Pilot Ignition (IPI)

Intermittent pilot systems use electronic ignition to light a pilot burner only when the thermostat calls for heat. After proving pilot flame, the system energizes the main gas valve. This design eliminates continuous pilot gas consumption.

### Spark Ignition Module

The ignition control module produces high-voltage sparks (typically 10,000-14,000V) across a spark electrode gap positioned adjacent to the pilot orifice. Spark generation continues until the flame sensor confirms pilot ignition, typically within 4-7 seconds.

### Flame Sensing Circuit

A flame rectification sensor proves pilot flame by detecting the rectification current that flows when AC voltage is applied across the flame ionization path. The flame acts as a semiconductor diode, allowing current flow in one direction. Rectification current must exceed 1.0-2.0 microamperes for reliable flame detection.

### Trial for Ignition Period

The control module attempts pilot ignition for a programmed period (typically 15-90 seconds). If flame sensing does not confirm ignition within this period, the system enters safety lockout mode requiring manual reset.

## Direct Spark Ignition (DSI)

Direct spark ignition systems eliminate the pilot burner entirely. The spark electrode ignites gas flowing from the main burner directly.

### System Configuration

The spark electrode positions 1/8 to 3/16 inch from the burner ground surface, creating a spark gap across the path of gas flow. When the thermostat calls for heat, the ignition module simultaneously opens the gas valve and generates high-voltage sparks at the electrode.

### Ignition Transformer Specifications

Spark ignition transformers step up 120V AC input to 4,000-14,000V output at the secondary winding. Current capacity ranges from 20-35 mA. The transformer operates continuously during the ignition trial period until flame is proven.

### Electrode Positioning Requirements

Proper electrode placement is critical for reliable ignition. The electrode tip must position in the gas stream path but avoid direct flame impingement. Distance from the burner surface affects both spark gap and flame sensing capability:

| Gap Distance | Characteristics |
|--------------|-----------------|
| 1/8" (3.2 mm) | Stronger spark, higher flame signal, shorter electrode life |
| 5/32" (4.0 mm) | Optimal balance for most applications |
| 3/16" (4.8 mm) | Reduced spark intensity, longer electrode life |

Horizontal alignment must center the electrode over the main burner orifice where gas velocity is highest. Misalignment beyond 1/4 inch reduces ignition reliability.

## Hot Surface Ignition (HSI)

Hot surface igniters use electrical resistance heating to ignite gas without spark generation. Silicon carbide or silicon nitride elements heat to 2,500°F in 15-30 seconds.

### Silicon Carbide Elements

First-generation silicon carbide igniters draw 2.5-4.0 amperes at 120V AC and reach ignition temperature in 17-30 seconds. The ceramic material has negative temperature coefficient characteristics, increasing resistance as temperature rises. Silicon carbide igniters are mechanically fragile and sensitive to thermal shock and handling damage.

### Silicon Nitride Elements

Silicon nitride igniters provide superior mechanical strength and thermal shock resistance. These elements draw lower current (1.0-2.5 amperes) and heat faster (10-20 seconds). Service life exceeds silicon carbide by 2-3 times under typical operating conditions.

### Ignition Sequence

The control board energizes the igniter element at the start of a heat call. After the warm-up period, a temperature sensor or timer confirms the element has reached ignition temperature. The gas valve then opens, directing gas across the glowing element surface. Ignition occurs within 1-2 seconds of gas valve opening.

### Current Sensing

Modern hot surface ignition controls monitor igniter current draw to verify element integrity. Open circuits, partial breaks, or degraded elements exhibit abnormal current signatures that trigger diagnostic alerts or prevent gas valve operation.

## Ignition Transformers

Spark ignition transformers convert line voltage to the high voltage required for arc generation across the electrode gap.

### Electrical Specifications

Standard ignition transformers feature:

| Parameter | Specification |
|-----------|--------------|
| Primary Voltage | 120V AC, 60 Hz |
| Secondary Voltage | 4,000-14,000V AC |
| Secondary Current | 20-35 mA |
| Spark Rate | 60-120 sparks/second |
| Duty Cycle | Intermittent (15-90 seconds max) |

### Output Characteristics

The transformer generates AC voltage at line frequency (60 Hz), producing 60 or 120 sparks per second depending on whether half-wave or full-wave rectification occurs in the gap. Higher spark rates improve ignition reliability by increasing the probability of spark occurrence during optimal fuel-air mixture conditions.

### Insulation Requirements

High-voltage secondary windings require careful insulation design. Breakdown voltage ratings exceed normal operating voltage by a minimum safety factor of 2:1. Transformer potting compounds prevent moisture intrusion that causes insulation failure and internal arcing.

## Electrode Design and Positioning

Ignition electrode configuration directly impacts system reliability and component longevity.

### Electrode Materials

Electrodes use high-temperature alloys that resist oxidation and erosion:

- Stainless steel (304/316): General purpose applications
- Inconel alloys: High-temperature resistance above 1800°F
- Platinum-tipped: Extended service life in severe conditions

### Positioning Geometry

The electrode must maintain proper relationship to both the burner ground and gas flow path:

**Vertical Position**: The electrode tip positions at or slightly above the top surface of the burner ports where gas exits with maximum velocity.

**Horizontal Position**: Electrode center aligns with the burner orifice centerline, placing the spark path directly in the gas stream.

**Spark Gap**: The distance between electrode tip and ground determines voltage requirements and spark intensity. Wider gaps require higher voltage but produce more visible sparks. Typical gaps range from 1/8 to 1/4 inch.

### Flame Rod Configuration

The same electrode that produces ignition spark also functions as the flame sensor in most modern systems. The electrode must position to remain within the flame envelope during main burner operation while avoiding flame impingement damage. The flame rod extends into the flame approximately 1/2 to 1 inch from the burner surface.

## Troubleshooting Ignition Systems

Systematic diagnosis identifies ignition failures quickly and accurately.

### Standing Pilot Failures

**No Pilot Flame**:
1. Verify gas supply valve position
2. Check pilot orifice for blockage
3. Measure gas supply pressure (7" W.C. natural gas, 11" W.C. propane)
4. Inspect pilot assembly alignment

**Pilot Lights But Will Not Stay Lit**:
1. Measure thermocouple output (minimum 20 mV hot, dropping to <8 mV when cooled)
2. Verify thermocouple tip position in pilot flame (engulfed in blue inner cone)
3. Test electromagnet holding coil resistance (typically 5-15 ohms)
4. Check for loose thermocouple connections causing voltage drop

### Hot Surface Ignition Failures

**Igniter Does Not Glow**:
1. Measure voltage at igniter terminals (should read 120V AC during warm-up)
2. Test igniter resistance when cold (typical range 50-400 ohms depending on design)
3. Inspect igniter element for cracks or breaks
4. Check igniter mounting bracket for proper grounding

**Igniter Glows But No Ignition**:
1. Verify gas valve energization during ignition period
2. Check gas supply pressure at manifold
3. Inspect burner orifices for blockage
4. Verify proper igniter positioning over burner ports (within 1/4 inch)
5. Test for adequate air supply to burners

**Repetitive Igniter Failure**:
1. Measure incoming voltage stability (low voltage causes igniter overheating)
2. Check for flame rollout contacting igniter
3. Verify blower timing (early blower start cools igniter prematurely)
4. Inspect for improper igniter handling during installation (oil contamination)

### Direct Spark Ignition Failures

**No Spark at Electrode**:
1. Verify 120V supply to ignition transformer primary
2. Test transformer output with high-voltage probe (4,000-14,000V)
3. Inspect electrode wire insulation for cracks or carbon tracking
4. Check electrode wire connection security at transformer and electrode

**Spark Present But No Ignition**:
1. Measure spark gap (should be 1/8 to 3/16 inch)
2. Verify electrode positioning over burner orifice
3. Check gas valve operation and manifold pressure
4. Inspect for electrode fouling or corrosion
5. Test flame sensor circuit continuity

**Weak or Intermittent Spark**:
1. Clean electrode and ground surfaces
2. Verify proper electrode gap
3. Test transformer output voltage under load
4. Check for high-voltage cable damage or moisture intrusion
5. Measure ground resistance (should be <1 ohm to chassis)

### Flame Sensing Failures

**System Ignites Then Shuts Off**:
1. Measure flame rectification current (must exceed 1.0 microamperes)
2. Clean flame sensor rod with fine abrasive cloth
3. Verify sensor position within flame envelope
4. Check sensor wire insulation and connections
5. Test for proper burner grounding

**Nuisance Flame Sensor Trips**:
1. Inspect for flame rollout or impingement
2. Verify proper combustion air supply
3. Check for burner misalignment
4. Test for electrical noise interference in sensing circuit
5. Measure gas manifold pressure (high pressure causes flame lifting)

## Safety Considerations

All ignition systems incorporate multiple safety interlocks to prevent gas accumulation and unsafe operating conditions.

### Lockout Timing

Electronic ignition controls enforce maximum trial for ignition periods. If flame sensing does not confirm ignition within the programmed time (typically 15-90 seconds), the control enters lockout mode. Lockout requires manual reset to prevent repeated ignition attempts that could accumulate unburned gas.

### Flame Proving Response Time

Flame sensors must detect loss of flame and close the gas valve within 4 seconds maximum for direct burner ignition and 10 seconds for pilot ignition systems per ANSI standards. This rapid response prevents gas accumulation in the combustion chamber.

### Grounding Requirements

Proper system grounding is essential for both spark generation and flame sensing. The burner assembly must provide electrical continuity to the control chassis with resistance below 1 ohm. Poor grounding causes weak sparks and unreliable flame detection.
