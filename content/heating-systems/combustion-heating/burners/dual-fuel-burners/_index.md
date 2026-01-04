---
title: "Dual-Fuel Burners"
weight: 3
description: "Engineering analysis of dual-fuel burner systems for gas-oil combustion including combination burner design, automatic fuel changeover systems, fuel interchangeability calculations, simultaneous firing capabilities, and burner sizing for fuel flexibility in commercial and industrial heating applications."
keywords: "dual-fuel burners, combination burners, gas-oil burners, automatic fuel changeover, fuel interchangeability, simultaneous firing, backup fuel systems"
---

# Dual-Fuel Burners

Dual-fuel burners provide operational flexibility by combusting either natural gas/propane or fuel oil without burner replacement, enabling fuel cost optimization, supply reliability during gas curtailment, and emergency backup capability. Modern dual-fuel systems achieve comparable performance on both fuels with combustion efficiency 80-88%, emissions compliance (NOx 40-120 ppm depending on fuel and configuration), and turndown ratios 4:1-10:1. Dual-fuel burner design addresses the fundamental challenge of accommodating vastly different fuel properties (gaseous vs. liquid, premixed vs. atomized) within a single burner assembly while maintaining flame stability, efficiency, and emissions performance across fuel types.

## Fuel Property Comparisons

### Critical Parameter Differences

| Property | Natural Gas | No. 2 Oil | Impact on Burner Design |
|----------|-------------|-----------|-------------------------|
| Physical state | Gas | Liquid | Oil requires atomization system |
| Heating value | 1000 Btu/ft³ | 140,000 Btu/gal | Different fuel delivery rates |
| Stoichiometric air | 9.52 ft³/ft³ | 1368 ft³/gal | Different air requirements |
| Flame temperature | 3600°F | 3750°F | Oil produces slightly higher temp |
| Flame speed | 0.33 ft/s | N/A (diffusion) | Gas flame premixed, oil diffusion |
| Ignition temperature | 1200°F | 500°F | Different ignition requirements |
| Flame luminosity | Low (blue) | High (yellow-orange) | Oil flame more radiant |

### Air Requirement Calculation

**For equivalent heat release:**

Gas: 10 MMBtu/h input

$$\dot{V}_{gas} = \frac{10,000,000}{1000} = 10,000 \text{ ft}^3\text{/h}$$

$$\dot{V}_{air,gas} = 10,000 \times 9.52 \times 1.15 = 109,500 \text{ scfh}$$

Oil: 10 MMBtu/h input

$$GPH_{oil} = \frac{10,000,000}{140,000} = 71.4 \text{ gph}$$

$$\dot{V}_{air,oil} = 71.4 \times 1368 \times 1.20 = 117,200 \text{ scfh}$$

**Air requirement difference:** Oil requires approximately 7% more combustion air than gas for same heat input due to higher stoichiometric requirement and typical excess air.

### Flame Characteristic Differences

**Natural gas flame:**
- Premixed (power burners) or partially premixed (atmospheric)
- Short, compact, blue flame
- Low luminosity (primarily convective heat transfer)
- Uniform temperature distribution
- Lower particulate emissions

**No. 2 oil flame:**
- Diffusion flame (mixing during combustion)
- Longer, more luminous, yellow-orange flame
- High radiation component
- Temperature gradient from spray center to periphery
- Atomization quality affects completeness

**Design consequence:** Burner must accommodate different flame geometries, heat transfer patterns, and combustion chamber requirements.

## Combination Burner Design

### Oil Atomization Integration

**Gun-type oil atomization:**
- Pressure atomizing nozzle (100-300 psi)
- Centered in burner head
- Hollow cone spray pattern (60-80° typical)
- Nozzle capacity: Sized for oil firing rate

**Gas supply integration:**

**Concentric ring design:**
1. Oil nozzle centered on burner axis
2. Gas spuds arranged in concentric ring around oil nozzle
3. Gas-air mixing in annular region
4. Separate gas manifold with individual orifices

**Advantages:**
- Independent fuel systems
- Minimal interference between gas and oil modes
- Simple fuel changeover

**Limitations:**
- Larger burner envelope
- More complex windbox design

### Air Distribution System

**Single air fan supplies both fuel modes:**

**Requirements:**
1. Adequate capacity for higher air demand (typically oil)
2. Adjustable damper for each fuel mode
3. Pressure range accommodates both fuels
4. Fan curve provides stable operation across range

**Dual-damper configuration:**
- Gas mode damper: Optimized for gas air requirements
- Oil mode damper: Optimized for oil air requirements
- Fuel selector positions appropriate damper
- Prevents manual adjustment error

**Air pressure requirements:**
- Gas firing: 2-6 in w.c. (typical 3-4 in w.c.)
- Oil firing: 3-8 in w.c. (typical 4-6 in w.c.)
- Fan selection: Based on oil requirement (higher)

### Ignition System

**Dual ignition approach:**

**Gas pilot for gas firing:**
- Small gas pilot burner (10,000-50,000 Btu/h)
- Spark ignited
- Proves before main gas valve opens
- Can use standing pilot or intermittent ignition

**Oil igniter for oil firing:**
- High-voltage spark (10,000V)
- Positioned to ignite oil spray periphery
- May use gas pilot assist for difficult ignition
- Electrode position critical (not fouled by oil spray)

**Flame detection:**
- UV scanner: Detects both gas and oil flames reliably
- Cadmium sulfide cell: Works but less reliable for oil
- Flame rod: Gas only (oil flame too conductive)
- Dual sensors: UV for oil, flame rod for gas (redundancy)

## Automatic Fuel Changeover

### Changeover Sequence Logic

**Gas-to-oil changeover:**

1. **Detect gas supply failure or price trigger**
   - Low gas pressure switch (<80% normal)
   - Manual selection via selector switch
   - Time-based schedule (peak pricing)

2. **Burner shutdown sequence**
   - Main gas valve closes
   - Purge burner with air (15-30 seconds)
   - Verify flame off (flame scanner)
   - Await post-purge completion

3. **Fuel system preparation**
   - Position oil mode air damper
   - Energize oil pump (build pressure)
   - Verify oil pressure (100-300 psi)
   - Verify oil temperature if heated (>50°F minimum)

4. **Oil burner startup**
   - Pre-purge (15-30 seconds minimum)
   - Spark ignition energized
   - Oil valve opens (trial for ignition: 10-15 seconds)
   - Flame proven via UV scanner
   - Ramp to firing rate

**Total changeover time:** 60-120 seconds (includes purges and ignition)

**Oil-to-gas changeover:**

1. **Trigger changeover**
   - Gas supply restored
   - Price optimization
   - Manual selection

2. **Burner shutdown**
   - Oil valve closes
   - Extended purge (30-60 seconds to clear oil vapor)
   - Flame proven off
   - Oil pump de-energized

3. **Gas system preparation**
   - Position gas mode air damper
   - Verify gas pressure available
   - Gas pilot system ready

4. **Gas burner startup**
   - Pre-purge (15-30 seconds)
   - Pilot ignition and proving
   - Main gas valve opens
   - Flame established
   - Ramp to firing rate

### Control System Requirements

**Fuel selector logic:**

**Inputs:**
- Gas pressure switch (prove availability)
- Oil pressure switch (prove pump operation)
- Oil temperature (if heated oil required)
- Fuel selector switch (manual override)
- Fuel priority setting (economic optimization)

**Outputs:**
- Gas mode enable
- Oil mode enable
- Gas valve positioning
- Oil valve positioning
- Air damper positioning (mode-specific)

**Interlocks:**

Critical safety interlocks prevent unsafe conditions:

1. **Fuel exclusion:** Only one fuel enabled at any time (unless simultaneous firing designed)
2. **Purge enforcement:** Adequate purge between fuel changes
3. **Flame detection:** Proper scanner for active fuel
4. **Air proving:** Correct damper position for fuel mode
5. **Pressure proving:** Fuel supply pressure adequate before ignition attempt

### Programmable Logic Controller

**Modern dual-fuel systems use PLC:**

**Advantages:**
- Complex sequencing logic
- Fuel optimization algorithms
- Data logging (run times, cycles, fuel consumption)
- Remote monitoring capability
- Preventive maintenance scheduling

**Typical PLC functions:**

1. **Automatic fuel selection:**
   - Compare fuel costs (inputs: gas price $/therm, oil price $/gal)
   - Calculate cost per MMBtu for each fuel
   - Select lower cost fuel automatically
   - Account for changeover frequency limits

2. **Demand-based switching:**
   - Low load → gas (better turndown, lower emissions)
   - High load → oil (if more economical)
   - Smooth transitions at threshold firing rates

3. **Supply monitoring:**
   - Track gas pressure trends
   - Predict curtailment
   - Switch proactively before interruption

## Simultaneous Firing Systems

### Design for Dual-Fuel Combustion

Some applications require firing both fuels simultaneously:

**Applications:**
- Peak demand supplementation (gas base + oil boost)
- Waste oil disposal (primary gas + supplemental waste oil)
- Gradual fuel transition (avoid thermal shock)

**Burner configuration:**

**Separate fuel burner heads:**
- Gas burner: Conventional gas burner design
- Oil burner: Separate gun or rotary oil burner
- Positioned side-by-side or concentric
- Independent control of each fuel stream

**Combined heat release:**

$$Q_{total} = Q_{gas} + Q_{oil}$$

**Air requirement:**

$$\dot{m}_{air,total} = \dot{m}_{air,gas} + \dot{m}_{air,oil}$$

Must size air system for maximum simultaneous firing condition.

### Control Strategy

**Modulating control with dual fuels:**

**Base loading:**
- Gas provides base load (0-100% of gas burner capacity)
- Oil burner off until gas at maximum
- Oil burner modulates for additional capacity

**Proportional firing:**
- Both fuels modulate proportionally
- Maintain fixed gas-to-oil ratio
- Used for waste oil disposal applications

**Control complexity:**

Requires independent air-fuel ratio control for each fuel:
- Gas air damper and gas valve linked
- Oil air damper and oil valve linked
- Total air = sum of individual fuel air requirements
- Cross-limiting for safety

## Performance Characteristics

### Efficiency by Fuel Mode

**Gas mode efficiency:** 82-88%
- Lower excess air possible (10-20%)
- No atomization losses
- Cleaner combustion (less fouling)
- Stack temperature: 300-450°F

**Oil mode efficiency:** 80-85%
- Higher excess air (15-25%)
- Atomization requires energy
- More radiant losses
- Stack temperature: 350-500°F

**Efficiency difference:** Gas typically 2-4% higher efficiency than oil for same burner.

### Emissions by Fuel Mode

**Natural gas emissions:**
- NOx: 30-60 ppm (standard power burner)
- NOx: 9-30 ppm (low-NOx designs)
- CO: <50 ppm
- Particulates: Negligible
- SO₂: Zero (no sulfur in natural gas)

**No. 2 oil emissions:**
- NOx: 80-150 ppm (standard)
- NOx: 50-100 ppm (low-NOx designs with FGR)
- CO: 50-150 ppm
- Particulates: Trace 0 (zero smoke when optimized)
- SO₂: 10-50 ppm (depends on fuel sulfur content 0.05-0.5%)

**Emissions consideration:** Gas mode produces significantly lower NOx and zero SO₂.

### Turndown Ratio

**Gas mode turndown:** 5:1 to 10:1 typical

**Oil mode turndown:** 3:1 to 6:1 typical
- Limited by oil atomization quality at low pressure
- Gun-type nozzles: 2:1-3:1
- Rotary atomizers: 4:1-8:1

**System turndown:** Limited by poorest fuel mode
- Overall turndown = minimum of gas and oil turndown
- May operate in gas mode only for low firing rates

## Application and Sizing

### Typical Applications

**Fuel supply reliability:**
- Facilities in interruptible gas service areas
- Critical processes requiring backup fuel
- Peak demand periods with gas curtailment

**Economic optimization:**
- Capitalize on fuel price differentials
- Lock in long-term oil contracts with gas spot market
- Seasonal fuel switching

**Emission compliance:**
- Gas for normal operation (low emissions)
- Oil for emergency only (emission exceedances allowed)

**Capacity:** 0.5-100 MMBtu/h (commercial and industrial)

### Sizing Methodology

**Step 1: Determine heat input required**

$$Q_{burner} = \frac{Q_{load}}{\eta_{boiler}} \times SF$$

Safety factor: 1.15-1.25

**Step 2: Size for both fuels**

**Gas capacity check:**

$$\dot{V}_{gas} = \frac{Q_{burner}}{HHV_{gas} \times \eta_{comb,gas}}$$

For natural gas: $HHV = 1000$ Btu/ft³, $\eta = 0.85$

$$\dot{V}_{gas} = \frac{Q}{850} \text{ ft}^3\text{/h}$$

**Oil capacity check:**

$$GPH = \frac{Q_{burner}}{HHV_{oil} \times \eta_{comb,oil}}$$

For No. 2 oil: $HHV = 140,000$ Btu/gal, $\eta = 0.82$

$$GPH = \frac{Q}{114,800}$$

**Step 3: Air system sizing**

Calculate air requirement for both fuels; size for larger (typically oil):

**Gas air requirement:**

$$\dot{V}_{air,gas} = \dot{V}_{gas} \times 9.52 \times (1 + EA_{gas})$$

With $EA_{gas} = 15\%$:

$$\dot{V}_{air,gas} = \dot{V}_{gas} \times 10.95 \text{ scfh}$$

**Oil air requirement:**

$$\dot{V}_{air,oil} = GPH \times 1368 \times (1 + EA_{oil})$$

With $EA_{oil} = 20\%$:

$$\dot{V}_{air,oil} = GPH \times 1642 \text{ scfh}$$

**Fan selection:** Size for maximum air requirement (typically oil mode) at required static pressure.

**Step 4: Fuel system design**

**Gas system:**
- Gas pressure regulator: Size for maximum gas flow
- Gas valve: Sized per pressure drop tables
- Gas piping: Size for <0.5 in w.c. drop at max flow
- Gas train: Per NFPA 86 (double block-bleed typical)

**Oil system:**
- Oil pump: Capacity for max gph at required pressure
- Oil nozzle: Standard size matching oil flow and spray pattern
- Oil piping: Minimum 1/2 in (avoid restrictions)
- Oil filter: 100 mesh minimum
- Oil heater: If required for heavy oils

**Step 5: Control system**

- Burner management system with dual-fuel programming
- Separate positioning controls for gas and oil modes
- Fuel selector logic (manual or automatic)
- Appropriate flame detection (UV scanner recommended)

### Economic Analysis

**Fuel cost comparison:**

Natural gas: $P_g$ ($/therm or $/MMBtu)

No. 2 oil: $P_o$ ($/gallon)

**Cost per MMBtu:**

$$C_g = P_g \text{ (\$/MMBtu directly)}$$

$$C_o = \frac{P_o \times 1,000,000}{140,000} = P_o \times 7.14 \text{ (\$/MMBtu)}$$

**Example:**
- Gas: $8.00/MMBtu
- Oil: $3.00/gallon

$$C_o = 3.00 \times 7.14 = \$21.42\text{/MMBtu}$$

Gas is more economical.

**Breakeven analysis:**

$$P_o = \frac{P_g}{7.14}$$

If gas costs $8.00/MMBtu, oil is competitive at $1.12/gallon or less.

**Changeover decision threshold:**
Include efficiency difference:

$$\frac{P_o / \eta_o}{HHV_o} < \frac{P_g / \eta_g}{HHV_g}$$

$$P_o < P_g \times \frac{HHV_o}{HHV_g} \times \frac{\eta_o}{\eta_g}$$

For $HHV_o = 140,000$ Btu/gal, $HHV_g = 1,000$ Btu/ft³ = 100,000 Btu/therm:

$$P_o < P_g \times \frac{140}{100} \times \frac{0.82}{0.85} = P_g \times 1.35$$

If gas = $8.00/MMBtu = $0.80/therm:

$$P_o < 0.80 \times 1.35 = \$1.08\text{/gal}$$

**Operating cost annual analysis:**

Annual operating hours: $H$ (hours/year)
Average firing rate: $Q_{avg}$ (MMBtu/h)
Annual heat: $Q_{annual} = Q_{avg} \times H$ (MMBtu)

**Gas annual cost:**

$$Cost_{gas} = Q_{annual} \times P_g$$

**Oil annual cost:**

$$Cost_{oil} = Q_{annual} \times C_o = Q_{annual} \times P_o \times 7.14$$

**Dual-fuel value:** Ability to switch fuels when oil becomes economical, or during gas curtailment when gas unavailable at any price.

## Selection Criteria

**Choose dual-fuel burner when:**

1. **Fuel supply reliability critical:**
   - Interruptible gas service
   - Critical process cannot tolerate shutdown
   - Geographic area prone to gas curtailment

2. **Economic optimization opportunity:**
   - Significant fuel price volatility
   - Ability to secure favorable oil contracts
   - Seasonal price differentials exceed dual-fuel premium cost

3. **Emission compliance flexibility:**
   - Gas for normal operation (tight emission limits)
   - Oil for emergency backup (relaxed limits during curtailment)

**Choose single-fuel when:**

1. Fuel supply highly reliable (firm gas service)
2. Fuel price stable or single fuel clearly lowest cost
3. Emissions require cleanest fuel (gas) at all times
4. Capital budget limited (single-fuel less expensive)
5. Maintenance resources limited (dual-fuel more complex)

**Cost premium:** Dual-fuel burners typically 40-80% higher first cost than comparable single-fuel burner.
