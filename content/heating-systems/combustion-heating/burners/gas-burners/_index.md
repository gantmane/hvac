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

## Turndown Ratio Analysis

Turndown ratio quantifies burner operating range flexibility, critical for matching varying load profiles and maintaining efficiency across load conditions.

### Definition and Calculation

**Turndown ratio:**

$$TD = \frac{Q_{maximum}}{Q_{minimum}}$$

Where:
- $Q_{maximum}$ = Maximum stable firing rate (Btu/h)
- $Q_{minimum}$ = Minimum stable firing rate (Btu/h)

**Example:** Burner with maximum 10 MMBtu/h and minimum 2 MMBtu/h has turndown ratio = 10:2 = 5:1.

### Turndown Limitations by Burner Type

**Atmospheric burners (3:1 to 4:1):**

Limited by venturi air aspiration physics. As gas pressure decreases, primary air aspiration becomes insufficient. Below minimum pressure:
- Inadequate primary air causes yellow flame
- Port velocity drops toward flashback limit
- Flame stability deteriorates

**Power burners standard (5:1 to 8:1):**

Limited by flame stability and air-fuel ratio control:
- Below minimum fire, flame detaches from stabilizer
- Mechanical linkage accuracy degrades at extremes
- Pilot flame becomes disproportionately large relative to main flame

**Power burners with modulating control (8:1 to 12:1):**

Electronic positioning enables wider range:
- Precise air-fuel ratio maintained via feedback control
- Variable frequency drive controls fan speed
- Advanced flame detection maintains supervision

**Premix burners (10:1 to 20:1):**

Highest turndown achieved through:
- Electronic mass flow control of gas and air
- Surface stabilization maintains flame at low firing rates
- Multiple burner staging (sequential activation)
- Oxygen trim continuously optimizes ratio

### Load Matching Analysis

**Load profile characterization:**

Annual load duration curve determines required turndown:

$$Q_{load}(t) = Q_{design} \times LF(t)$$

Where $LF(t)$ = Load factor vs. time

**Cycling analysis:**

Insufficient turndown causes cycling:

$$\text{Cycles per hour} = \frac{Q_{load,avg} - Q_{burner,min}}{Q_{burner,rated} \times t_{on}}$$

**Cycling penalties:**
- Efficiency loss: 2-5% per additional cycle
- Pre-purge and post-purge losses
- Wear on ignition components
- Thermal stress on heat exchanger

**Turndown requirement determination:**

$$TD_{required} = \frac{Q_{design,connected}}{Q_{load,minimum}}$$

**Example:** Building with 12 MMBtu/h design load and 2 MMBtu/h minimum load requires minimum 6:1 turndown to avoid cycling.

### Turndown Impact on Efficiency

**Excess air relationship:**

As firing rate decreases, maintaining proper combustion requires excess air adjustment:

$$EA\% = EA_{design} \times \left(1 + k \times \left(\frac{Q_{actual}}{Q_{rated}} - 1\right)\right)$$

Coefficient $k = 0.2-0.5$ depending on control sophistication.

**Fixed excess air penalty:**

Without modulation, excess air remains constant, causing efficiency degradation:

$$\eta = \eta_{design} - \frac{K \times (T_{stack} - T_{ambient}) \times EA\%}{HHV}$$

**Modulating control advantage:**

O₂ trim maintains optimal excess air across firing range, preserving efficiency within ±1% from full to minimum fire.

### Multiple Burner Staging

**Lead-lag operation:**

Install multiple smaller burners rather than single large burner:

$$N_{burners} = \frac{Q_{total}}{Q_{burner,each}}$$

**System turndown:**

$$TD_{system} = N \times TD_{individual}$$

**Example:** Four burners with individual 5:1 turndown provide system turndown of 20:1.

**Staging sequence:**
1. Burner 1 modulates from minimum to maximum
2. Burner 2 starts at minimum fire
3. Burner 1 returns to optimum fire point
4. Burners 1 and 2 modulate together
5. Sequence continues for burners 3 and 4

**Advantages:**
- Extended system turndown
- Redundancy for reliability
- Maintenance flexibility
- Optimized efficiency at partial loads

### Altitude Effects on Turndown

**Air density correction:**

$$\rho_{altitude} = \rho_{sea level} \times e^{-\frac{altitude}{28,000}}$$

**Impact on atmospheric burners:**

Reduced air density decreases venturi aspiration, narrowing turndown:

$$TD_{altitude} = TD_{sea level} \times \left(\frac{\rho_{altitude}}{\rho_{sea level}}\right)^{0.5}$$

**Example:** 4:1 turndown at sea level becomes 3.3:1 at 5,000 ft elevation.

**Power burner compensation:**

Forced draft burners maintain turndown with altitude adjustments:
- Increase fan speed to compensate for density
- Adjust combustion air flow measurement
- Recalibrate O₂ trim setpoint

## Flame Safeguard Controls

Flame safeguard systems provide critical safety supervision of burner operation, preventing unsafe accumulation of unburned fuel in combustion chamber.

### Regulatory Framework

**NFPA 86:** Standard for Ovens and Furnaces
**NFPA 85:** Boiler and Combustion Systems Hazards Code
**FM Global:** Property Loss Prevention Data Sheets

**Key requirements:**
- Flame detection proven before fuel valve opening
- Maximum time to flame establishment: 5-15 seconds
- Immediate fuel shutoff on flame failure
- Pre-purge before ignition: 4-5 air changes
- Post-purge after shutdown: 1 minute minimum

### Flame Detection Technologies

**Flame rod (flame rectification):**

**Operating principle:**
- AC voltage applied between flame rod and burner ground
- Flame conducts electricity asymmetrically (rectification)
- AC becomes pulsating DC
- Microamp signal indicates flame presence

**Rectification mechanism:**

Hot combustion gases contain ions enabling current flow. Flame rectification occurs due to asymmetric electrode areas:

$$I_{rod \rightarrow ground} > I_{ground \rightarrow rod}$$

**Signal characteristics:**
- Current: 0.5-10 μA
- Voltage: 80-250 VAC applied
- Prove threshold: >0.5 μA
- Response time: <1 second

**Installation requirements:**
- Rod positioned in flame envelope
- Clearance from ground: 0.125-0.375 in
- Avoid direct impingement of flame on rod
- Ceramic insulator prevents leakage current

**Advantages:**
- Simple, reliable
- Self-checking (rod breakage causes failure indication)
- Low cost
- No external power required

**Limitations:**
- Requires electrical ground through flame
- Susceptible to contamination
- Not suitable for UV-rich or low-temperature flames
- Single burner monitoring only

**Ultraviolet (UV) scanners:**

**Operating principle:**
- UV-sensitive tube detects 1900-2900 Å radiation
- Flame produces UV from C₂ radical emission
- Tube conducts only when UV present
- Electronic amplifier proves flame signal

**UV tube construction:**
- Electrodes in gas-filled envelope
- UV-transparent window
- Ionization threshold at UV wavelengths
- Self-extinguishing when UV removed

**Signal processing:**

Controller requires minimum pulse frequency to prove flame:

$$f_{pulse} > 4 \text{ Hz (typical minimum)}$$

Discriminates flame from ambient light and hot refractory.

**Sighting tube design:**

$$L_{sight} / D_{sight} = 8-12$$

Provides directional sensitivity, viewing specific burner.

**Advantages:**
- Sees flame directly (not secondary effects)
- Fast response: 1-4 seconds
- Multiple burner monitoring possible
- No contact with flame
- Discriminates against non-flame radiation

**Limitations:**
- Requires clear sight path to flame
- Susceptible to UV from arc welding, sunlight
- Sighting tube contamination degrades signal
- Higher cost than flame rod

**Infrared (IR) scanners:**

**Operating principle:**
- Detects 4.3 μm CO₂ emission band
- Filtered sensor eliminates ambient IR
- Flicker frequency detection (5-100 Hz)
- Discriminates flame from hot refractory

**Flicker detection:**

Flame produces characteristic flicker due to turbulence. Scanner analyzes frequency spectrum:

$$f_{flame} = 5-100 \text{ Hz (typical)}$$

Hot refractory produces steady IR signal (DC component), rejected by AC-coupled amplifier.

**Self-checking features:**
- Shutter mechanism periodically blocks detector
- Verifies scanner responds to signal removal
- Optical path check via internal reference source
- Microprocessor diagnostics

**Advantages:**
- Discriminates flame from hot refractory
- Long-distance viewing (up to 20 ft)
- Minimal maintenance
- Multiple burner monitoring
- Self-checking capability

**Limitations:**
- Most expensive detection method
- Complex electronics
- Requires clean optical path
- May not respond to certain blue premix flames

### Burner Management Sequences

**Pre-start checks:**

Before permitting burner start, controller verifies:
1. All limit switches satisfied (pressure, temperature, flow)
2. No flame signal present (confirms detector function)
3. Fuel valves proven closed
4. Air pressure switch proven
5. Combustion air damper position confirmed

**Pre-purge:**

Purpose: Remove any combustible gas mixture from combustion chamber and flue passages.

**Purge air volume:**

$$V_{purge} = V_{chamber} \times N_{changes}$$

Where $N_{changes} = 4-5$ (NFPA requirement)

**Purge time:**

$$t_{purge} = \frac{V_{purge}}{\dot{V}_{air,purge}} \times 60$$

Typical purge rates: 25-100% of maximum combustion air flow.

**Minimum purge times:**
- Small burners (<400,000 Btu/h): 15 seconds
- Commercial burners (0.4-10 MMBtu/h): 30-60 seconds
- Industrial burners (>10 MMBtu/h): 2-5 minutes
- After fuel trip: Immediate purge, 1 minute minimum

**Pilot ignition sequence (interrupted pilot):**

1. Pilot gas valve opens
2. Ignition transformer energizes
3. Trial for ignition period: 5-10 seconds
4. Flame detector must prove pilot flame
5. If no pilot flame detected, lockout occurs
6. Main gas valve permitted after pilot proven

**Main burner ignition:**

1. Main fuel valve opens
2. Flame must be established within trial period: 5-15 seconds
3. Controller monitors flame signal continuously
4. Pilot remains on or shuts off (depending on system)

**Normal operation monitoring:**

Controller continuously verifies:
- Flame signal strength above minimum threshold
- Airflow proven
- All operating limits within range
- Fuel pressure within acceptable band

**Flame failure response:**

Upon loss of flame signal:
1. Immediate fuel valve closure (<1 second)
2. Post-purge initiated
3. Lockout condition set (manual reset required)
4. Alarm indication

**Safety shutdown:**

Conditions causing immediate shutdown:
- Flame failure
- Low/high gas pressure
- Low combustion airflow
- High temperature limit
- Low water level (boiler applications)
- Emergency stop activated

**Post-purge:**

After shutdown, controller runs fan to clear combustion chamber:
- Minimum duration: 1 minute
- Ensures no residual fuel vapor
- Cools heat exchanger

**Lockout and reset:**

After safety trip:
1. Lockout relay latches
2. Fault indication provided
3. Manual reset required (prevents automatic restart)
4. Fault must be corrected before reset permitted
5. Reset button acknowledges fault and clears lockout

### Redundant Safety Features

**Double block and bleed valve configuration:**

Required for burners >400,000 Btu/h:

**Valve arrangement:**
- Main safety shutoff valve #1 (normally closed)
- Vent valve to atmosphere (normally open during off cycle)
- Main safety shutoff valve #2 (normally closed)

**Safety logic:**
- Both main valves must open to supply fuel
- Vent valve closes only when both main valves proven closed on shutdown
- Prevents leakage past single valve from reaching burner

**Valve proving system:**

Before permitting ignition, controller verifies valve tightness:

1. Close both main valves
2. Open vent valve
3. Pressurize test section between valves with gas pressure
4. Close valve #2
5. Open vent valve and measure pressure decay
6. If pressure holds, valve #1 leaking (alarm condition)
7. Repeat test for valve #2 leakage

**Test frequency:** Before each burner start or daily, per NFPA 86.

**Combustion air proving:**

**Air pressure switch:**
- Senses air flow via pressure differential across fan or burner
- Minimum pressure setting: 75% of normal operating pressure
- Must close before fuel valve permitted to open
- Opens on airflow loss, immediately trips burner

**Air flow switch (optional for critical applications):**
- Paddle or thermal sensor in air duct
- Direct flow measurement
- Backup to pressure switch

**High/low gas pressure switches:**

Monitor fuel pressure within operating range:

**Low pressure switch:**
- Setting: 80-90% of normal operating pressure
- Prevents insufficient fuel delivery
- Causes immediate shutdown

**High pressure switch:**
- Setting: 110-120% of normal operating pressure
- Prevents over-firing
- Protects against regulator failure

## Modulating vs On-Off Control

Control strategy selection significantly impacts efficiency, equipment life, and occupant comfort. On-off and modulating control represent fundamentally different approaches to load matching.

### On-Off (Two-Position) Control

**Operating principle:**

Burner operates at full fire or completely off based on thermostat or pressure switch:

$$Q_{burner}(t) = \begin{cases} Q_{rated} & T < T_{setpoint} - \Delta T_{diff} \\ 0 & T > T_{setpoint} + \Delta T_{diff} \end{cases}$$

**Control differential:**

$$\Delta T_{diff} = 5-15°F \text{ (typical for heating applications)}$$

**Cycling rate:**

$$\text{CPH} = \frac{Q_{load,avg}}{Q_{burner,rated} \times t_{on,avg}}$$

Where $t_{on,avg}$ = average on-time per cycle.

**On-cycle duration:**

$$t_{on} = \frac{C_{system} \times \Delta T_{diff}}{Q_{burner,rated} - Q_{load}}$$

Where $C_{system}$ = System thermal capacitance (Btu/°F).

**Cycling losses:**

Each cycle incurs fixed losses:

**Pre-purge loss:**

$$Q_{prepurge} = \dot{m}_{air,purge} \times C_p \times (T_{boiler} - T_{ambient}) \times t_{purge}$$

**Post-purge loss:**

$$Q_{postpurge} = \dot{m}_{air,purge} \times C_p \times (T_{boiler} - T_{ambient}) \times t_{purge}$$

**Jacket loss during off-cycle:**

Heat exchanger cools to ambient during off-cycle, requiring reheat:

$$Q_{jacket,cycle} = C_{HX} \times \Delta T_{HX}$$

**Annual cycling efficiency penalty:**

$$\eta_{penalty} = \frac{N_{cycles,annual} \times (Q_{prepurge} + Q_{postpurge} + Q_{jacket})}{Q_{fuel,annual}} \times 100$$

Typical penalty: 3-8% depending on cycling rate.

**Applications:**

On-off control suitable for:
- Small residential heating: <150,000 Btu/h
- Domestic water heaters
- Simple commercial systems with adequate thermal mass
- Low initial cost priority
- Consistent load profiles

**Advantages:**
- Simple, reliable control
- Low equipment cost
- Easy troubleshooting
- Adequate for high thermal mass systems

**Limitations:**
- Cycling losses reduce efficiency
- Temperature/pressure swings
- Ignition system wear
- Poor efficiency at partial loads (most operating hours)
- Limited ability to match varying loads

### High-Low-Off Control

Intermediate approach providing two firing rates:

$$Q_{burner}(t) = \begin{cases} Q_{high} & \text{High demand} \\ Q_{low} = Q_{high}/2 & \text{Low demand} \\ 0 & \text{No demand} \end{cases}$$

**Low-fire typically 40-60% of high-fire capacity.**

**Operating sequence:**
1. Burner starts on low fire
2. After 30-second stabilization, switch to high fire if needed
3. When load satisfied, return to low fire
4. After time delay (2-10 minutes), shut off if low fire excessive

**Advantages over on-off:**
- Reduced cycling frequency
- Lower average firing rate matches partial loads better
- 2-4% efficiency improvement
- Extended equipment life

**Applications:**
- Medium commercial heating: 0.5-5 MMBtu/h
- Variable load profiles
- Moderate cost premium acceptable

### Modulating Control

**Operating principle:**

Burner firing rate varies continuously to match load:

$$Q_{burner}(t) = f(T_{error}, \int T_{error} dt, \frac{dT_{error}}{dt})$$

**PID control algorithm:**

$$Q_{burner} = K_p \times e(t) + K_i \times \int e(t)dt + K_d \times \frac{de(t)}{dt}$$

Where:
- $e(t) = T_{setpoint} - T_{actual}$ (error signal)
- $K_p$ = Proportional gain
- $K_i$ = Integral gain
- $K_d$ = Derivative gain

**Proportional band:**

Range over which controller modulates from minimum to maximum fire:

$$PB = \frac{\Delta T_{full range}}{T_{setpoint}} \times 100\%$$

Typical proportional band: 10-30°F for heating, 5-15 psi for steam.

**Throttling range:**

Burner varies from minimum to maximum fire as measured variable traverses proportional band.

**Example:** Steam boiler with 150 psi setpoint and 15 psi proportional band:
- 142.5 psi: Maximum fire
- 150 psi: Mid-fire (approximately)
- 157.5 psi: Minimum fire
- >157.5 psi: Burner off

**Integral action (reset):**

Eliminates offset by adjusting output based on accumulated error:

$$\text{Reset rate} = \frac{K_i}{K_p} \text{ (repeats per minute)}$$

Typical reset: 0.1-0.5 repeats/minute for heating applications.

**Derivative action (rate):**

Responds to rate of change, anticipating overshoot:

$$\text{Rate time} = \frac{K_d}{K_p} \text{ (minutes)}$$

Seldom used in HVAC due to noise amplification.

**Modulating burner components:**

**Modulating gas valve:**
- Electric actuator positions valve plug
- Linear or equal-percentage characteristic
- Positioning accuracy: ±1-2%
- Response time: 15-60 seconds full stroke

**Modulating air damper:**
- Actuator coupled to damper shaft
- Jackshaft linkage maintains air-fuel ratio
- Parallel positioning system (electronic)

**Control types:**

**Mechanical linkage (jackshaft):**
- Single actuator positions both air and fuel
- Cam-shaped link establishes air-fuel ratio
- Simple, reliable
- Limited turndown (5:1 to 8:1)
- Requires field adjustment of cam

**Parallel positioning:**
- Separate actuators for air and fuel
- Electronic controller maintains ratio
- Higher accuracy
- Extended turndown (8:1 to 12:1)
- Cross-limiting prevents fuel-rich conditions

**Oxygen trim:**
- O₂ sensor in flue gas (zirconia or paramagnetic)
- Controller adjusts air-fuel ratio to maintain O₂ setpoint
- Compensates for fuel variations, altitude, temperature
- Optimizes efficiency continuously
- Essential for ultra-low NOx burners
- Typical O₂ setpoint: 2-4% for gas burners

**Performance benefits:**

**Efficiency improvement:**

Modulating control maintains near-optimal efficiency across load range:

$$\eta_{modulating} = \eta_{design} - 1\%$$ (across 30-100% load)

Compared to on-off control:

$$\eta_{on-off} = \eta_{design} - 5-10\%$$ (annual average)

**Annual efficiency gain: 4-9%**

**Load matching:**

Burner output continuously tracks load:

$$Q_{burner}(t) \approx Q_{load}(t)$$

Eliminates cycling losses and maintains stable temperature/pressure.

**Equipment life:**

Reduced cycling extends component life:
- Ignition system: 2-3x life extension
- Heat exchanger: Reduced thermal stress
- Controls: Less contact wear
- Valves: Fewer operations

**Comfort/process stability:**

Near-constant temperature/pressure:
- Temperature variation: ±1-2°F (vs. ±5-10°F on-off)
- Pressure variation: ±1-2 psi (vs. ±5-15 psi on-off)

**Applications:**

Modulating control recommended for:
- Commercial/industrial heating: >1 MMBtu/h
- Variable loads (weather-dependent, process variations)
- High annual operating hours
- Efficiency requirements >85%
- Emissions limits <30 ppm NOx
- Premium comfort requirements

**Economic justification:**

**Incremental cost:**
- Equipment premium: $3,000-$15,000 (depending on size)
- Installation: $1,000-$5,000 (more complex wiring, commissioning)

**Annual savings:**

$$\text{Savings} = Q_{annual} \times \Delta\eta \times \text{Fuel cost}$$

**Example:** 5 MMBtu/h boiler, 4,000 hours/year, 6% efficiency gain, $8/MMBtu gas:

$$\text{Savings} = 5 \times 4,000 \times 0.06 \times 8 = \$9,600/\text{year}$$

**Simple payback:** 1-3 years for most commercial applications.

## Natural Gas vs Propane Applications

Fuel selection impacts burner design, combustion characteristics, safety considerations, and operating economics. Natural gas and propane exhibit distinct physical and chemical properties requiring application-specific analysis.

### Fuel Property Comparison

**Physical properties:**

| Property | Natural Gas (Methane) | Propane |
|----------|----------------------|---------|
| Chemical formula | CH₄ (85-95%) + C₂H₆, C₃H₈ | C₃H₈ |
| Molecular weight | 16-20 lb/lbmol | 44 lb/lbmol |
| Specific gravity (air = 1.0) | 0.60-0.70 | 1.52 |
| Density @ 60°F, 1 atm | 0.042-0.048 lb/ft³ | 0.116 lb/ft³ (vapor) |
| Boiling point | -259°F | -44°F |
| Vapor pressure @ 70°F | N/A (gas) | 127 psia |
| Higher heating value | 1,000-1,050 Btu/ft³ | 2,516 Btu/ft³ |
| HHV (mass basis) | 23,000 Btu/lb | 21,500 Btu/lb |
| Lower heating value | 900-950 Btu/ft³ | 2,385 Btu/ft³ |
| Wobbe index | 1,310-1,390 | 2,550 |
| Stoichiometric air | 9.52 ft³/ft³ | 23.8 ft³/ft³ |
| Flammability limits | 5.0-15.0% | 2.1-9.5% |
| Ignition temperature | 1,004°F | 920°F |
| Flame speed | 0.33 ft/s | 0.38 ft/s |
| Flame temperature (stoich) | 3,542°F | 3,595°F |

### Burner Design Differences

**Orifice sizing:**

For equal heat input, orifice area must account for Wobbe index ratio:

$$\frac{A_{propane}}{A_{natural gas}} = \frac{WI_{NG}}{WI_{propane}} = \frac{1,350}{2,550} = 0.53$$

**Propane orifice approximately 53% of natural gas orifice area** (30% smaller diameter).

**Port design:**

Higher flame speed of propane requires different port sizing:

$$V_{port,propane} > V_{port,NG}$$

Propane ports typically 10-20% smaller diameter to maintain adequate velocity preventing flashback.

**Primary air:**

Propane requires more air per unit volume but similar mass basis:

**Volume basis:** Propane requires 2.5x air per ft³
**Mass basis:** Natural gas requires 10% more air per lb

Atmospheric burners: Primary air adjustment differs significantly between fuels.

**Conversion considerations:**

Converting burner from natural gas to propane:
1. Replace main orifice (smaller for propane)
2. Replace pilot orifice
3. Adjust primary air (typically increase opening)
4. Adjust gas pressure (typically 11 in w.c. for propane vs. 3.5 in w.c. for NG)
5. Verify proper combustion (O₂, CO testing)
6. Re-rate nameplate capacity

**Dual-fuel burners:**

Some commercial burners designed for either fuel:
- Changeable orifice spuds
- Adjustable primary air
- Gas pressure regulator adjustment
- Control system configuration for fuel type

### Safety Considerations

**Natural gas:**

**Lighter than air** (SG = 0.60-0.70):
- Leak rises and disperses
- Accumulates at high points
- Requires ceiling-level gas detection
- Venting strategy: High-point relief

**Propane:**

**Heavier than air** (SG = 1.52):
- Leak sinks to floor
- Accumulates in low areas (basements, pits, trenches)
- Requires floor-level gas detection
- Venting strategy: Low-point drains, mechanical ventilation
- Extremely hazardous in confined spaces below grade

**Propane storage safety:**

- Liquid propane stored at 100-250 psi (ambient temperature)
- Tank sizing: 2.5 gallons liquid = 1 MMBtu capacity
- Vaporization rate limits instantaneous capacity
- Cold weather reduces vapor pressure (requires vaporizers for large loads)
- NFPA 58 governs installation

**Leak detection:**

Both fuels odorized with mercaptan:
- Detection threshold: 20% LEL (Lower Explosive Limit)
- Propane leaks more dangerous due to accumulation in low areas
- Automatic shutoff recommended for propane installations >1 MMBtu/h

### Economic Analysis

**Fuel cost comparison (typical 2025 values):**

**Natural gas:**
- Utility rate: $6-$15/MMBtu (regional variation)
- No storage cost
- Consistent pressure and composition
- Uninterrupted supply (utility)

**Propane:**
- Delivered price: $15-$35/MMBtu ($1.50-$3.50/gallon)
- Storage tank required (rental or purchase)
- Delivery logistics and inventory management
- Price volatility (seasonal, market-driven)

**Cost per MMBtu delivered:**

Natural gas typically 40-60% less expensive than propane per unit energy.

**Application selection:**

**Natural gas preferred when:**
- Utility service available
- High annual consumption (>10,000 MMBtu)
- Consistent load profile
- Urban/suburban locations
- Low installation cost acceptable

**Propane preferred when:**
- No natural gas utility service
- Remote locations
- Backup fuel for dual-fuel systems
- Portable/temporary heating
- Peak shaving (supplement natural gas during high-demand periods)
- Higher energy density needed (portable applications)

**Dual-fuel systems:**

Install burners capable of both fuels:

**Peak shaving application:**
- Natural gas primary fuel
- Automatic switch to propane when utility curtails service
- Avoids interruptible rate penalties
- Maintains continuous operation

**Standby application:**
- Natural gas primary
- Propane backup for utility outages
- Critical process continuity

**Economic switchover:**

Automatic fuel selection based on cost:

$$\text{Fuel cost}_{NG} \times \eta_{NG} < \text{Fuel cost}_{propane} \times \eta_{propane}$$

Control system switches to most economical fuel in real-time.

### Combustion Characteristics

**Flame appearance:**

**Natural gas:** Light blue flame, shorter flame length, less luminous
**Propane:** Blue with slight orange, longer flame, more luminous (incandescent carbon particles)

**Flame length:**

$$L_{flame,propane} \approx 1.15 \times L_{flame,NG}$$

Propane produces 15% longer flame at equal heat input due to higher C:H ratio.

**Carbon formation:**

Propane more prone to soot formation if air-fuel ratio rich:
- Higher C:H ratio (3:8 vs. 1:4)
- Requires more precise combustion control
- Yellow flame indicates insufficient air (soot production)

**Emissions comparison:**

At optimized conditions:

| Emission | Natural Gas | Propane |
|----------|-------------|---------|
| NOx | 30-60 ppm | 35-70 ppm |
| CO | <50 ppm | <50 ppm |
| CO₂ | 8-9% | 10-11% |
| Particulate | Negligible | Trace (if optimized) |

Propane produces 10-15% higher NOx due to slightly higher flame temperature.

### Altitude Compensation

**Natural gas:**

Composition varies by source:
- Pipeline gas: Consistent composition
- Altitude affects air density, not gas composition
- Air-fuel ratio adjustment required at altitude

**Propane:**

Consistent composition (pure C₃H₈):
- Vaporization rate decreases with altitude (lower atmospheric pressure)
- Vapor pressure compensates partially
- May require vaporizer for high-altitude, high-capacity applications

**Correction factor:**

$$Q_{altitude} = Q_{sea level} \times \sqrt{\frac{P_{altitude}}{P_{sea level}}}$$

Both fuels require de-rating or compensation at altitude above 2,000 ft.
