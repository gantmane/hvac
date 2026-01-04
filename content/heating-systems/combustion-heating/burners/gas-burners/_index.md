---
title: "Gas Burners"
weight: 1
description: "Engineering analysis of gas burner types including atmospheric burners, power burners, premix burners, and low-NOx burners with flame stability theory, mixing mechanisms, combustion efficiency calculations, and emissions control for natural gas and propane combustion in commercial and industrial heating systems."
keywords: "gas burners, atmospheric burners, power burners, premix burners, low-NOx burners, flame stability, Wobbe index, flame speed, NOx reduction, forced draft burners"
---

# Gas Burners

Gas burners mix gaseous fuel with combustion air and stabilize a flame to produce controlled heat release for heating applications. Unlike oil burners requiring atomization, gas burners achieve molecular-level mixing of fuel and air, enabling high combustion efficiency (85-95%), low emissions (NOx 9-80 ppm, CO <50 ppm), and wide turndown ratios (3:1 to 25:1 depending on type). Gas burner design focuses on proper air-gas mixing, flame stability across firing range, complete combustion within available residence time, and emissions minimization through temperature and stoichiometry control.

## Gas Combustion Fundamentals

### Stoichiometric Relationships

**Natural gas (methane) combustion:**

$$\text{CH}_4 + 2\text{O}_2 \rightarrow \text{CO}_2 + 2\text{H}_2\text{O} + 383,000 \text{ Btu/lb CH}_4$$

**Air requirement:**

$$A_s = \frac{2 \text{ mol O}_2}{1 \text{ mol CH}_4} \times \frac{1 \text{ mol air}}{0.21 \text{ mol O}_2} = 9.52 \text{ mol air/mol CH}_4$$

At standard conditions (60°F, 14.7 psia):

$$A_s = 9.52 \text{ ft}^3 \text{ air/ft}^3 \text{ CH}_4$$

**Mass basis:**

$$A_s = \frac{2 \times 32}{16} \times \frac{1}{0.2315} = 17.24 \text{ lb air/lb CH}_4$$

**Propane combustion:**

$$\text{C}_3\text{H}_8 + 5\text{O}_2 \rightarrow 3\text{CO}_2 + 4\text{H}_2\text{O}$$

$$A_s = 23.8 \text{ ft}^3 \text{ air/ft}^3 \text{ C}_3\text{H}_8 = 15.7 \text{ lb air/lb C}_3\text{H}_8$$

### Wobbe Index

Critical parameter for burner interchangeability:

$$WI = \frac{HHV}{\sqrt{SG}}$$

Where:
- $HHV$ = Higher heating value (Btu/ft³)
- $SG$ = Specific gravity relative to air

**Typical values:**
- Natural gas: WI = 1310-1390 Btu/ft³
- Propane: WI = 2550 Btu/ft³
- Manufactured gas: WI = 500-700 Btu/ft³

**Interchangeability criterion:** Burners operate properly when Wobbe index variation is within ±5%.

**Heat input calculation:**

$$Q = C_d A P \times WI$$

Where:
- $C_d$ = Orifice discharge coefficient
- $A$ = Orifice area (in²)
- $P$ = Gas pressure (in w.c.)

Constant Wobbe index means constant heat input for fixed orifice and pressure.

### Flame Speed

Fundamental property governing burner design:

$$S_u = \sqrt{\frac{k \times \alpha}{\tau_{reaction}}}$$

Where:
- $k$ = Thermal conductivity
- $\alpha$ = Thermal diffusivity
- $\tau_{reaction}$ = Chemical reaction time

**Typical laminar flame speeds (ft/s):**
- Methane-air (stoichiometric): 0.33 ft/s
- Propane-air (stoichiometric): 0.38 ft/s
- Hydrogen-air (stoichiometric): 8.7 ft/s

**Flame speed dependence on equivalence ratio:**

$$\phi = \frac{(F/A)_{actual}}{(F/A)_{stoichiometric}}$$

Maximum flame speed occurs at $\phi = 1.05-1.10$ (slightly rich mixture).

**Port loading limit:**

Gas velocity through burner port must satisfy:

$$V_{port,min} < S_u < V_{port,max}$$

- If $V_{port} < S_u$: Flashback (flame travels upstream into burner)
- If $V_{port} > S_u$: Liftoff (flame detaches and extinguishes)

## Atmospheric Burners

### Operating Principle

**Venturi mixing process:**
1. Gas pressure (3.5-7 in w.c.) supplies gas to injector orifice
2. High-velocity gas jet (200-400 ft/s) creates low-pressure zone
3. Primary air aspirated through adjustable shutters (40-60% of stoichiometric)
4. Gas and primary air mix in venturi throat and burner tube
5. Mixture exits through burner ports
6. Secondary air entrained by natural draft at flame zone
7. Complete combustion achieved with combined primary and secondary air

**Air inspiration:**

$$\dot{m}_{air,primary} = K \times \dot{m}_{gas} \times \sqrt{\frac{\Delta P_{gas}}{P_{atm}}}$$

Where $K$ = Inspirator constant (function of venturi geometry)

### Burner Port Design

**Port sizing:**

$$A_{ports} = \frac{\dot{V}_{mix}}{V_{port}}$$

Where:
- $\dot{V}_{mix}$ = Gas-air mixture flow rate (ft³/h)
- $V_{port}$ = Port velocity (ft/s)
- $A_{ports}$ = Total port area (in²)

**Port velocity limits:**
- Minimum: 20-30 ft/s (prevent flashback)
- Maximum: 100-150 ft/s (prevent liftoff)
- Typical design: 50-80 ft/s

**Port diameter:**
- Natural gas: 0.050-0.125 in
- Propane: 0.040-0.100 in (smaller due to higher flame speed)

**Flame retention:**
Ports arranged to create flame stabilization zone with low-velocity recirculation.

### Primary Air Adjustment

**Primary air percentage:**

$$PA\% = \frac{\dot{m}_{air,primary}}{\dot{m}_{air,stoichiometric}} \times 100$$

**Optimal setting:**
- Too low (<40%): Yellow flame, soot production, CO formation
- Optimal (40-60%): Blue flame, stable combustion, low emissions
- Too high (>60%): Flashback risk, lifting tendency, hard flame

**Adjustment procedure:**
1. Set gas pressure to specified value (typically 3.5 in w.c.)
2. Open primary air shutter gradually
3. Observe flame color change: Yellow → orange → blue
4. Continue until sharp blue inner cone appears
5. Increase air slightly until CO <100 ppm
6. Check for flashback by temporarily reducing gas flow
7. Lock shutter setting

### Performance Characteristics

**Turndown ratio:** 3:1 to 4:1

Limited by:
- Minimum gas pressure for adequate air aspiration
- Port velocity limits (flashback/liftoff)
- Flame stability

**Combustion efficiency:**
- 75-82% (lower than power burners)
- Stack temperature: 400-600°F
- Excess air: 40-50% (6-8% O₂)
- High excess air due to uncontrolled secondary air entrainment

**Emissions:**
- NOx: 40-80 ppm (low due to lower combustion intensity)
- CO: 50-150 ppm (proper adjustment <100 ppm)

### Applications

**Typical uses:**
- Residential furnaces: 40,000-150,000 Btu/h
- Small commercial units: 100,000-400,000 Btu/h
- Water heaters: 30,000-75,000 Btu/h
- Pool heaters: 100,000-400,000 Btu/h

**Advantages:**
- Simple, reliable design
- No external air source required
- Low first cost
- Low operating cost (no fan power)
- Quiet operation

**Limitations:**
- Limited turndown capability
- Altitude sensitivity (reduced air density affects aspiration)
- Efficiency lower than forced-draft systems
- Difficult to control excess air precisely

## Power Burners (Forced Draft)

### Operating Principle

**Forced mixing combustion:**
1. Combustion air fan supplies controlled air flow
2. Gas pressure regulator controls fuel flow
3. Gas and air mix in burner mixing chamber or at burner head
4. Mixture (premix) or separate streams (nozzle-mix) supplied to burner
5. High-velocity discharge creates turbulent flame
6. Air-fuel ratio controlled mechanically or electronically
7. Complete combustion within furnace chamber

**Air supply:**
- Fan type: Centrifugal or vane-axial
- Pressure: 1-10 in w.c. (typical 2-6 in w.c.)
- Control: On-off, high-low, or modulating

### Burner Configurations

**Nozzle-mix (raw gas) burners:**
- Separate gas and air supplies to burner head
- Mixing occurs at burner tile/nozzle exit
- Turbulent diffusion flame
- Gas pressure: 5-15 psi
- Applications: Industrial heating, high-fire loads

**Premix burners:**
- Gas and air mix upstream of burner head
- Mixture supplied to burner ports
- Premixed flame (blue, compact)
- Gas pressure: 3-10 in w.c.
- Applications: Packaged boilers, commercial heating

**Tunnel burners:**
- Burner fires into refractory tunnel
- Flame stabilization via tunnel geometry
- High thermal release rates
- Radiant and convective heat transfer

### Air-Fuel Ratio Control

**Mechanical linkage (Jackshaft):**

Single actuator positions both air damper and fuel valve via mechanical linkage.

**Cam profile design:**
Fuel valve position = f(damper position) determined by cam shape to maintain proper ratio across firing range.

**Parallel positioning:**

Separate actuators for air and fuel with electronic controller:

$$\dot{m}_{fuel} = K \times \dot{m}_{air}$$

Controller maintains constant ratio via feedback from actuator positions.

**Cross-limiting:**

Safety logic prevents fuel-rich conditions:
- Increasing fire: Air damper leads, fuel valve follows
- Decreasing fire: Fuel valve leads, air damper follows

**Typical response:**
- Air opens to 90% of target before fuel increases
- Fuel closes to 110% of target before air decreases

### Flame Stabilization

**Stabilization mechanisms:**

1. **Boundary layer separation:**
   - Bluff body creates recirculation zone
   - Low-velocity region allows flame anchoring
   - Hot products ignite incoming mixture

2. **Swirl stabilization:**
   - Tangential air inlet creates rotating flow
   - Central low-pressure zone promotes recirculation
   - Swirl number $S = 0.3-0.8$ for optimal stability

3. **Pilot flame:**
   - Continuous or intermittent pilot
   - Provides ignition source for main flame
   - Typically 1-5% of main burner capacity

**Flame stability limits:**

$$\frac{V_{mix}}{S_u} < 10 \text{ (lower limit)}$$

$$\frac{V_{mix}}{S_u} > 2 \text{ (upper limit)}$$

### Performance Characteristics

**Turndown ratio:** 5:1 to 10:1

Achieved by:
- Modulating air and fuel flows
- Maintaining air-fuel ratio via linkage or control
- Stable combustion across wide flow range

**Combustion efficiency:**
- 82-88%
- Stack temperature: 300-450°F
- Excess air: 10-20% (1.5-3.5% O₂)

**Emissions:**
- NOx: 30-60 ppm (conventional)
- CO: <50 ppm
- Unburned hydrocarbons: <10 ppm

### Applications and Sizing

**Typical applications:**
- Commercial boilers: 0.5-30 MMBtu/h
- Industrial process heaters: 1-100 MMBtu/h
- Packaged boilers: 0.5-15 MMBtu/h
- Duct furnaces: 1-50 MMBtu/h

**Burner selection:**

Required burner capacity:

$$Q_{burner} = \frac{Q_{load}}{\eta_{system}} \times SF$$

Where $SF$ = 1.15-1.25 safety factor

**Fan sizing:**

Required air flow:

$$\dot{V}_{air} = \frac{Q_{burner}}{HHV_{gas}} \times A_s \times (1 + EA)$$

For natural gas: $HHV = 1000$ Btu/ft³, $A_s = 9.52$ ft³/ft³

$$\dot{V}_{air} = \frac{Q_{Btu/h}}{1000} \times 9.52 \times 1.15 = 0.0110 \times Q$$

**Fan pressure:**
- Burner pressure drop: 1-6 in w.c.
- Ductwork losses: 0.5-2 in w.c.
- Total static pressure: 2-10 in w.c.

## Premix Burners

### Operating Principle

**Complete premixing combustion:**
1. Gas and air fully mixed upstream of combustion zone
2. Uniform stoichiometry throughout mixture
3. Laminar or turbulent premixed flame
4. Surface or matrix stabilization
5. Low peak flame temperatures
6. Minimal NOx formation

**Premixing methods:**

**Venturi premixing:**
- Similar to atmospheric burner
- Higher gas pressure (5-15 in w.c.)
- Forced air supply
- 100% primary air premixing

**Blower premixing:**
- Gas injected into fan inlet or discharge
- Thorough mixing in fan or duct
- Explosionproof fan required
- Safety interlocks critical

### Burner Head Types

**Perforated surface burner:**
- Flat or cylindrical surface with small holes
- Hole diameter: 0.020-0.060 in
- Port velocity: 10-50 ft/s
- Flame stabilized on surface
- Radiant heat from surface
- Applications: Infrared heaters, process heaters

**Metal fiber burner:**
- Woven metal fiber matrix
- High surface area
- Flame stabilizes within matrix
- Surface temperature: 1600-2200°F
- Excellent radiant efficiency
- Applications: High-efficiency commercial boilers

**Ceramic matrix burner:**
- Porous ceramic material
- Very high surface area
- Flame distributed through matrix
- Surface temperature: 1800-2400°F
- Ultra-low emissions
- Applications: Ultra-low NOx burners

### Flame Temperature Control

**Peak flame temperature:**

$$T_{peak} = T_{reactants} + \frac{HHV \times \phi}{C_p \times (1 + \frac{1}{\phi} \times A_s)}$$

Where $\phi$ = equivalence ratio

**NOx formation strongly temperature-dependent:**

$$\frac{d[NOx]}{dt} \propto e^{-E_a/RT}$$

Activation energy $E_a \approx 70,000$ cal/mol

**Temperature reduction strategies:**

1. **Lean premix ($\phi < 1.0$):**
   - Operate at equivalence ratio 0.6-0.9
   - Reduces peak temperature 200-400°F
   - Requires very precise air-fuel ratio control

2. **Surface stabilization:**
   - Heat loss to burner surface
   - Reduces gas temperature 100-300°F
   - Increases efficiency via radiation

3. **Staged combustion:**
   - Primary zone sub-stoichiometric
   - Secondary air downstream
   - Reduces peak temperature zone residence time

### Performance Characteristics

**Turndown ratio:** 8:1 to 15:1

Achieved by:
- Modulating gas and air flows
- Maintaining precise premix ratio
- Electronic control essential
- Oxygen trim improves stability

**Combustion efficiency:**
- 85-92% (highest among gas burner types)
- Low excess air requirement: 5-15%
- Stack temperature: 250-350°F (with economizer)

**Emissions:**
- NOx: 9-30 ppm (ultra-low)
- CO: <50 ppm (typically <25 ppm)
- Unburned HC: <5 ppm

### Applications

**Typical uses:**
- High-efficiency condensing boilers
- Ultra-low NOx commercial boilers
- Food processing (clean combustion)
- Semiconductor manufacturing (particulate-sensitive)

**Capacity range:** 0.2-15 MMBtu/h (per burner)

**Selection criteria:**
- Emissions requirements <30 ppm NOx
- High efficiency targets >90%
- Clean combustion essential
- Precise control available

## Low-NOx Burners

### NOx Formation Mechanisms

**Thermal NOx (Zeldovich mechanism):**

$$\text{O} + \text{N}_2 \rightarrow \text{NO} + \text{N}$$
$$\text{N} + \text{O}_2 \rightarrow \text{NO} + \text{O}$$

**Rate equation:**

$$\frac{d[NO]}{dt} = k \times e^{-70,000/RT} \times [O_2]^{0.5} \times [N_2]$$

**Temperature sensitivity:**
NOx formation rate doubles approximately every 90°F above 2800°F.

**Prompt NOx:**
Formed in fuel-rich zones via CH radical reactions. Minor contributor for natural gas (<10% of total NOx).

### Low-NOx Design Strategies

**Flame temperature reduction:**

1. **Flue gas recirculation (FGR):**
   - Recirculate 10-30% flue gas to combustion air
   - Reduces O₂ concentration
   - Increases heat capacity of mixture
   - Reduces peak temperature 200-400°F
   - NOx reduction: 50-70%

**FGR ratio:**

$$FGR\% = \frac{\dot{m}_{flue gas}}{\dot{m}_{air}} \times 100$$

**Temperature reduction:**

$$\Delta T = \frac{FGR \times C_{p,flue} \times (T_{flue} - T_{air})}{C_{p,mix}}$$

2. **Staged combustion:**

**Fuel staging:**
- Primary zone: Fuel-rich (φ = 1.2-1.5)
- Low oxygen suppresses NOx
- Secondary fuel: Added downstream
- Complete combustion in fuel-lean zone

**Air staging:**
- Primary zone: Sub-stoichiometric (φ = 1.3-1.8)
- Low excess oxygen limits NOx
- Secondary air: Added downstream
- Complete combustion with minimal NOx

**NOx reduction:** 60-80% vs. conventional burners

3. **Delayed mixing:**
- Segregate fuel and air streams
- Gradual mixing along flame length
- Avoids high-temperature stoichiometric zones
- Creates distributed reaction zone
- NOx reduction: 50-70%

### Internal FGR Burners

**Operating principle:**

Burner design induces flue gas entrainment without external FGR fan:

1. High-velocity air jet creates low-pressure zone
2. Furnace flue gases entrained
3. Flue gases mix with combustion air
4. Effective FGR ratio: 15-25%

**Advantages:**
- No external FGR system required
- Lower installation cost
- Reduced maintenance
- Simpler control

**Limitations:**
- Less FGR than external system
- Furnace pressure sensitive
- NOx reduction limited to 40-60%

### Ultra-Low NOx Burners

**Design features:**
- Lean premix combustion
- Surface stabilization
- Precise air-fuel ratio control (±2%)
- Oxygen trim mandatory
- Multiple burner stages
- Distributed firing

**Performance targets:**
- NOx: <9 ppm @ 3% O₂
- CO: <50 ppm
- Turndown: 10:1 to 15:1

**Control requirements:**
- Electronic air-fuel ratio control
- O₂ trim with response time <15 seconds
- Flame safeguard with UV scanner
- High-accuracy flow measurement

### Emissions Comparisons

| Burner Type | NOx (ppm @ 3% O₂) | CO (ppm) | Efficiency | Turndown |
|-------------|-------------------|----------|------------|----------|
| Atmospheric | 40-80 | 50-150 | 75-82% | 3:1-4:1 |
| Standard power | 50-100 | <50 | 82-85% | 5:1-8:1 |
| Low-NOx power | 30-60 | <50 | 82-88% | 5:1-10:1 |
| FGR power | 20-40 | <50 | 80-85% | 5:1-10:1 |
| Premix | 9-30 | <25 | 85-92% | 8:1-15:1 |
| Ultra-low NOx | <9 | <50 | 85-92% | 10:1-20:1 |

### Applications and Selection

**Regulatory compliance:**

**SCAQMD Rule 1146.2 (Southern California):**
- NOx limit: 20 ppm @ 3% O₂ (>2 MMBtu/h)
- Ultra-low: 9 ppm @ 3% O₂ (>5 MMBtu/h)

**Bay Area AQMD Regulation 9-7:**
- NOx limit: 30 ppm @ 3% O₂

**Selection based on limit:**
- >60 ppm: Standard power burner adequate
- 40-60 ppm: Low-NOx or FGR burner
- 20-40 ppm: FGR or premix burner
- 9-20 ppm: Premix or ultra-low NOx required
- <9 ppm: Ultra-low NOx with SCR post-treatment

**Installation considerations:**

1. **Space requirements:**
   - Ultra-low NOx burners often larger
   - FGR systems require ducting and fan
   - Plan for adequate clearances

2. **Control complexity:**
   - Electronic controls required
   - O₂ trim essential for <30 ppm
   - Training requirements higher

3. **Fuel quality:**
   - Wobbe index variation critical
   - Gas pressure regulation tighter
   - Consider fuel conditioning

4. **Operating cost:**
   - Fan power higher for FGR
   - Efficiency gains offset by complexity
   - Maintenance requirements increase

## Burner Selection Methodology

**Step 1: Determine firing rate**

$$Q_{burner} = \frac{Q_{load}}{\eta_{boiler}} \times SF$$

**Step 2: Establish turndown requirement**

$$TD_{required} = \frac{Q_{design}}{Q_{minimum}}$$

**Step 3: Identify emission limits**

Check local air quality regulations for applicable NOx and CO limits.

**Step 4: Select burner type**

Use decision matrix:
- Capacity + turndown + emissions → burner type
- Cost vs. performance tradeoff
- Installation constraints

**Step 5: Verify fan capacity**

$$\dot{V}_{air} = \frac{Q_{burner}}{1000} \times 9.52 \times (1 + EA)$$

$$P_{fan} = \text{Burner drop + duct losses}$$

**Step 6: Control system**

- <30 ppm NOx: Oxygen trim mandatory
- Modulating: Electronic positioning
- Safety: Flame safeguard per NFPA 86

**Example:**

Required: 8 MMBtu/h, turndown 6:1, NOx <30 ppm

**Solution:**
- Burner type: Premix low-NOx burner
- Expected NOx: 20-25 ppm
- Efficiency: 88-90%
- Control: Electronic with O₂ trim
- Air flow: $8,000,000 / 1000 \times 9.52 \times 1.10 = 83,700$ scfh
- Fan: 1400 cfm @ 6 in w.c.
