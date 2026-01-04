---
title: "Automatic Fuel-Burning Equipment"
weight: 3
description: "Engineering analysis of automatic fuel-burning equipment including oil burners, gas burners, dual-fuel systems, flame safeguard controls, air-fuel ratio control, combustion efficiency calculations, and NOx reduction techniques for industrial and commercial heating applications."
keywords: "automatic burners, oil burners, gas burners, dual-fuel burners, flame safeguard, air-fuel ratio, combustion efficiency, NOx reduction, FGR, SCR, low-NOx burners"
---

# Automatic Fuel-Burning Equipment

Automatic fuel-burning equipment encompasses oil burners, gas burners, and dual-fuel systems that provide controlled, efficient combustion for boilers, furnaces, process heaters, and industrial heating applications. Modern burner technology focuses on achieving high thermal efficiency (80-95%), minimizing emissions (NOx < 9-30 ppm, CO < 50 ppm), ensuring safe operation through sophisticated flame safeguard systems, and maintaining optimal air-fuel ratios across varying firing rates. Burner selection requires comprehensive analysis of fuel characteristics, firing rate requirements, turndown ratio needs, efficiency targets, emission compliance, and control system integration.

## Combustion Fundamentals

### Stoichiometric Combustion

**Natural gas (methane) combustion:**

$$\text{CH}_4 + 2\text{O}_2 + 7.52\text{N}_2 \rightarrow \text{CO}_2 + 2\text{H}_2\text{O} + 7.52\text{N}_2$$

**Stoichiometric air requirement:**

$$A_s = 9.52 \text{ ft}^3 \text{ air/ft}^3 \text{ CH}_4 \text{ (at standard conditions)}$$

**No. 2 fuel oil combustion:**

$$\text{C}_{12}\text{H}_{23} + 17.375\text{O}_2 + 65.4\text{N}_2 \rightarrow 12\text{CO}_2 + 11.5\text{H}_2\text{O} + 65.4\text{N}_2$$

**Stoichiometric air requirement:**

$$A_s = 1368 \text{ ft}^3 \text{ air/gal oil} \approx 13.9 \text{ lb air/lb oil}$$

### Excess Air Requirements

Actual combustion requires excess air beyond stoichiometric to ensure complete oxidation:

$$\text{Excess Air (\%)} = \frac{A_{actual} - A_s}{A_s} \times 100$$

**Typical excess air by burner type:**
- Atmospheric gas burners: 40-50%
- Power gas burners: 10-20%
- Pressure atomizing oil burners: 15-25%
- Rotary oil burners: 10-15%
- Dual-fuel burners: 15-25%

**Relationship to oxygen content:**

$$\text{O}_2\% = \frac{21 \times \text{Excess Air}}{100 + \text{Excess Air}}$$

For natural gas with 15% excess air:

$$\text{O}_2\% = \frac{21 \times 15}{115} = 2.74\%$$

### Adiabatic Flame Temperature

Maximum theoretical combustion temperature with no heat loss:

$$T_{flame} = T_{air} + \frac{HHV}{C_p \times (1 + EA) \times A_s}$$

Where:
- $HHV$ = Higher heating value of fuel (Btu/unit)
- $C_p$ = Specific heat of combustion products (Btu/lb·°F)
- $EA$ = Excess air fraction
- $A_s$ = Stoichiometric air (lb/unit fuel)

**Typical adiabatic flame temperatures:**
- Natural gas: 3600°F (0% excess air) → 3100°F (15% excess air)
- No. 2 oil: 3750°F (0% excess air) → 3200°F (15% excess air)
- No. 6 oil: 3800°F (0% excess air) → 3250°F (15% excess air)

## Combustion Efficiency

### Thermal Efficiency Calculation

Overall burner/boiler efficiency:

$$\eta_{total} = 100 - L_{stack} - L_{radiation} - L_{incomplete}$$

**Stack loss** (dominant loss mechanism):

$$L_{stack} = \frac{(T_{stack} - T_{air}) \times C_p \times m_{gas}}{HHV \times m_{fuel}} \times 100$$

Simplified form using flue gas CO₂ or O₂:

$$L_{stack} = K \times \frac{T_{stack} - T_{air}}{CO_2\%}$$

Where $K$ = Fuel constant (0.65 for natural gas, 0.54 for No. 2 oil)

**Alternative oxygen-based stack loss:**

$$L_{stack} = \frac{(T_{stack} - T_{air})}{T_{stack} - 450} \times \frac{\% O_2}{21 - \% O_2}$$

**Radiation and convection loss:**
- Small boilers (<10 MMBtu/h): 1-3%
- Medium boilers (10-100 MMBtu/h): 0.5-1.5%
- Large boilers (>100 MMBtu/h): 0.2-0.8%

**Incomplete combustion loss:**
Indicated by CO and smoke. Should be <0.5% for properly operating burners.

### Efficiency Example

Natural gas burner operating conditions:
- Stack temperature: 450°F
- Combustion air temperature: 70°F
- Flue gas O₂: 3.5%
- CO: 10 ppm (negligible)

Stack loss calculation:

$$L_{stack} = \frac{450 - 70}{450 - 450} \times \frac{3.5}{21 - 3.5} \approx 20\% \text{ (using graphical method)}$$

Simplified: For natural gas, approximately 1% efficiency loss per 40°F stack temperature rise above ambient, per % O₂.

$$L_{stack} \approx \frac{380°F \times 3.5\%}{40} \approx 19.5\%$$

Total efficiency:

$$\eta_{total} = 100 - 19.5 - 1.0 - 0.2 = 79.3\%$$

## Burner Types Overview

| Burner Type | Fuel | Turndown Ratio | Efficiency | NOx (ppm) | Applications |
|-------------|------|----------------|-----------|-----------|--------------|
| Gun-type oil | Oil | 2:1 - 3:1 | 80-85% | 80-150 | Residential, light commercial |
| Rotary oil | Oil | 4:1 - 8:1 | 82-87% | 60-120 | Commercial, industrial |
| Steam atomizing | Oil | 10:1 - 20:1 | 83-88% | 50-100 | Large industrial |
| Atmospheric gas | Gas | 3:1 - 4:1 | 75-82% | 40-80 | Residential, small commercial |
| Power gas | Gas | 5:1 - 10:1 | 82-88% | 30-60 | Commercial, industrial |
| Premix gas | Gas | 8:1 - 15:1 | 85-92% | 9-30 | High efficiency commercial |
| Low-NOx gas | Gas | 5:1 - 10:1 | 82-88% | 9-30 | Emission-critical applications |
| Dual-fuel | Oil/Gas | 4:1 - 10:1 | 80-88% | 40-100 | Fuel flexibility required |

## Air-Fuel Ratio Control

### Control Methods

**On-off positioning:**
- Fixed linkage between air damper and fuel valve
- Single air-fuel ratio setting
- Accuracy: ±15-20% of optimal
- Applications: Small burners (<1 MMBtu/h)

**High-low-off positioning:**
- Two discrete firing rates
- Two air-fuel ratio settings
- Low-fire typically 30-50% of high-fire
- Applications: Residential and light commercial

**Fully modulating:**
- Continuous firing rate adjustment
- Mechanical linkage or electronic positioning
- Jackshaft systems: Air damper and fuel valve mechanically linked
- Parallel positioning: Electronic actuators maintain ratio
- Accuracy: ±5-10% across firing range

**Cross-limiting:**
- Air leads on increasing fire
- Fuel leads on decreasing fire
- Prevents dangerous fuel-rich conditions
- Essential for large burners (>10 MMBtu/h)

### Oxygen Trim Control

Closed-loop control system maintains optimal excess air:

**Components:**
- Oxygen sensor (zirconia or electrochemical)
- Control algorithm (PID)
- Air damper actuator or VFD fan control

**Target setpoint:**
- Natural gas: 2.0-3.5% O₂
- No. 2 oil: 2.5-4.0% O₂
- No. 6 oil: 2.5-4.5% O₂

**Efficiency improvement:**

$$\Delta \eta = L_{stack,high} - L_{stack,optimized}$$

Reducing excess air from 30% (5.5% O₂) to 15% (2.7% O₂) at 450°F stack temperature improves efficiency by approximately 2-3%.

**Trim response:**
- Response time: 10-30 seconds
- Update frequency: 1-10 seconds
- Stability: ±0.2-0.5% O₂

## Flame Safeguard Systems

Modern flame safeguard controls provide safe burner startup, operation, and shutdown:

**Startup sequence:**
1. Pre-purge: 15-60 seconds (4 air changes minimum)
2. Pilot ignition: 3-10 seconds
3. Pilot flame establishment: 4-10 seconds
4. Main fuel valve opening
5. Main flame establishment: 4-10 seconds

**Flame detection methods:**
- Cadmium sulfide (CdS) cell: Detects visible light (residential/light commercial)
- Ultraviolet (UV) scanner: Detects UV radiation 1850-2900Å (commercial/industrial)
- Flame rod (ionization): Detects flame conductivity (gas only)
- Infrared (IR) scanner: Detects specific IR wavelengths (high-reliability applications)

**Safety lockout conditions:**
- Flame failure during operation
- Flame not established within trial-for-ignition period
- Loss of atomizing medium (steam/air atomizing burners)
- Low fuel pressure
- High/low combustion air pressure
- Unsafe flue draft conditions

## Emissions Characteristics

### NOx Formation Mechanisms

**Thermal NOx:**
Formed at high temperatures (>2800°F) via Zeldovich mechanism:

$$\text{Rate} \propto e^{-E_a/RT} \times [\text{O}_2]^{0.5} \times [\text{N}_2]$$

Doubles approximately every 100°F above 2800°F.

**Fuel NOx:**
Oxidation of nitrogen compounds in fuel (significant for residual oils, coal).

**Prompt NOx:**
Formed in fuel-rich flame zones via hydrocarbon radical reactions (minor contributor).

### Emission Reduction Techniques

**Flue gas recirculation (FGR):**
- Recirculates 10-30% of flue gas to combustion air
- Reduces flame temperature by 200-400°F
- Reduces O₂ concentration
- NOx reduction: 40-70%

**Staged combustion:**
- Fuel staging: Primary zone fuel-rich, secondary zone fuel-lean
- Air staging: Primary zone sub-stoichiometric, secondary air downstream
- NOx reduction: 50-80%

**Low-NOx burner design:**
- Internal FGR
- Delayed mixing
- Distributed combustion
- NOx reduction: 50-85% vs. conventional

**Selective catalytic reduction (SCR):**
- Post-combustion ammonia injection
- Catalyst bed at 600-800°F
- NOx reduction: 80-95%
- Expensive; used when <9 ppm required

## Burner Sizing Methodology

### Required Firing Rate

**Heating load:**

$$Q_{burner} = \frac{Q_{load}}{\eta_{system}}$$

Where:
- $Q_{load}$ = Building/process heating load (Btu/h)
- $\eta_{system}$ = System efficiency (burner × distribution × heat exchanger)

**Warm-up capacity:**

$$Q_{warmup} = \frac{M \times C_p \times \Delta T}{t_{warmup} \times 3600}$$

Where:
- $M$ = Mass of system water/structure (lb)
- $\Delta T$ = Temperature rise (°F)
- $t_{warmup}$ = Allowable warmup time (hours)

**Burner capacity:**

$$Q_{burner} = \max(Q_{load}, Q_{warmup}) \times SF$$

Safety factor $SF$ = 1.10-1.25 for boilers, 1.15-1.30 for process heaters.

### Turndown Requirements

Minimum burner turndown ratio:

$$TD = \frac{Q_{max}}{Q_{min}} \geq \frac{Q_{design}}{Q_{summer}}$$

Typical requirements:
- Boilers: 4:1 to 10:1
- Process heaters: 3:1 to 8:1
- High-efficiency modulating systems: 10:1 to 25:1

## Section Components

This section provides detailed analysis of:

1. **Oil burner types**: Gun-type pressure atomizing, rotary cup, air atomizing, and steam atomizing systems with atomization theory and sizing
2. **Gas burner types**: Atmospheric, power, premix, and low-NOx configurations with flame stability and mixing analysis
3. **Dual-fuel systems**: Combination burners, automatic changeover, and fuel interchangeability
4. **Burner controls**: Flame safeguard programming, positioning controls, and safety interlocks
5. **Combustion air**: Supply requirements, fan sizing, and air temperature effects
6. **Flue gas analysis**: Efficiency optimization, continuous emissions monitoring, and diagnostic techniques
7. **NOx reduction**: FGR systems, SCR catalysts, and ultra-low NOx burner design
