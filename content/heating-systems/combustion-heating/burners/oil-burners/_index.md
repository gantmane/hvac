---
title: "Oil Burners"
weight: 2
description: "Comprehensive analysis of oil burner types including gun-type pressure atomizing burners, rotary cup burners, air atomizing systems, and steam atomizing burners with atomization theory, droplet size distributions, combustion efficiency calculations, and burner sizing for commercial and industrial heating applications."
keywords: "oil burners, gun-type burners, pressure atomizing, rotary burners, steam atomizing, air atomizing, fuel oil atomization, droplet size, Sauter mean diameter, combustion efficiency"
---

# Oil Burners

Oil burners atomize liquid fuel oil into fine droplets, mix the fuel spray with combustion air, and ignite the mixture to produce controlled flame for heating applications. Successful oil combustion requires achieving proper atomization (20-80 μm Sauter mean diameter), adequate air-fuel mixing, sufficient residence time for droplet evaporation and combustion (0.05-0.15 seconds), and flame temperature control. Oil burners range from small residential gun-type units (0.5-5 gph, 70,000-700,000 Btu/h) to large industrial steam-atomizing systems (500-5000 gph, 70-700 MMBtu/h) with widely varying atomization mechanisms, turndown capabilities, and efficiency characteristics.

## Atomization Fundamentals

### Droplet Size Theory

Fuel oil must be atomized to increase surface area for rapid evaporation and combustion. Surface area increase factor:

$$\frac{A_{droplets}}{A_{stream}} = \frac{6V/d_{32}}{4\pi r^2} = \frac{6D}{d_{32}}$$

Where:
- $d_{32}$ = Sauter mean diameter (volume-to-surface ratio mean, μm)
- $D$ = Original stream diameter (μm)
- $V$ = Fuel volume (constant)

**Example:** 1 mm oil stream atomized to 50 μm SMD:

$$\frac{A_{droplets}}{A_{stream}} = \frac{6 \times 1000}{50} = 120 \times \text{ surface area}$$

### Sauter Mean Diameter

Critical parameter defining droplet size distribution:

$$d_{32} = \frac{\sum n_i d_i^3}{\sum n_i d_i^2}$$

Where:
- $n_i$ = Number of droplets in size class $i$
- $d_i$ = Diameter of size class $i$

**Target SMD for complete combustion:**
- Light oil (No. 2): 40-80 μm
- Heavy oil (No. 6): 80-150 μm
- Residual fuels: 100-200 μm

### Evaporation and Combustion Time

Droplet evaporation follows d-squared law:

$$d^2(t) = d_0^2 - kt$$

Where:
- $d_0$ = Initial droplet diameter (μm)
- $k$ = Evaporation constant (μm²/s)
- $t$ = Time (s)

**Total evaporation time:**

$$t_{evap} = \frac{d_0^2}{k}$$

For No. 2 oil at 2000°F, $k \approx 0.8$ mm²/s:
- 50 μm droplet: $t_{evap} = (0.05)^2 / 0.8 = 3.1$ ms
- 100 μm droplet: $t_{evap} = (0.10)^2 / 0.8 = 12.5$ ms

**Residence time requirement:**

$$t_{residence} = \frac{L_{flame}}{V_{gas}} > 2-3 \times t_{evap}$$

Inadequate residence time causes incomplete combustion, smoke, and reduced efficiency.

## Gun-Type (Pressure Atomizing) Burners

### Operating Principle

**Atomization mechanism:**
1. Fuel oil pumped to 100-300 psi
2. Oil enters atomizing nozzle tangentially
3. Swirl chamber imparts rotational velocity
4. High-velocity oil exits orifice (150-300 ft/s)
5. Centrifugal force creates hollow cone spray
6. Surface tension instability breaks sheet into droplets

**Spray cone angle:**

$$\tan(\theta/2) = \frac{V_{tangential}}{V_{axial}}$$

Typical cone angles: 30-90° (most common: 60-80°)

### Nozzle Design

**Flow rate through nozzle:**

$$\dot{m} = C_d A \sqrt{2 \rho \Delta P}$$

Where:
- $C_d$ = Discharge coefficient (0.75-0.85)
- $A$ = Orifice area (in²)
- $\rho$ = Oil density (lb/ft³)
- $\Delta P$ = Pressure drop across nozzle (psi)

**Standard rating:** Flow rate in gallons per hour at 100 psi with No. 2 oil.

**Nozzle capacity at different pressure:**

$$GPH_2 = GPH_1 \times \sqrt{\frac{P_2}{P_1}}$$

Example: 1.0 gph nozzle at 100 psi operating at 150 psi:

$$GPH_{150} = 1.0 \times \sqrt{\frac{150}{100}} = 1.22 \text{ gph}$$

### Sauter Mean Diameter - Pressure Atomizing

Empirical correlation for SMD:

$$d_{32} = 3.68 \times \frac{\sigma^{0.6} \dot{m}^{0.25}}{\rho_a^{0.25} \Delta P^{0.4}}$$

Where:
- $\sigma$ = Surface tension (dyne/cm)
- $\dot{m}$ = Fuel flow rate (g/s)
- $\rho_a$ = Air density (g/cm³)
- $\Delta P$ = Pressure drop (bar)

**Key relationships:**
- SMD decreases with increasing pressure: $d_{32} \propto \Delta P^{-0.4}$
- SMD increases with flow rate: $d_{32} \propto \dot{m}^{0.25}$
- Higher pressure → finer atomization → better combustion

### Component Configuration

**Fuel system:**
- Oil tank with supply line
- Fuel pump: Single-stage (residential) or two-stage (commercial)
- Pressure: 100 psi (residential), 100-300 psi (commercial)
- Flow rate: 0.5-10 gph (residential), 5-150 gph (commercial)
- Solenoid valve for on-off control

**Air system:**
- Fan: Centrifugal blower, 3450 RPM
- Static pressure: 0.5-4.0 in w.c.
- Air pattern: Annular around fuel spray
- Primary air: 80-100% of stoichiometric
- Secondary air: Entrained naturally

**Ignition:**
- Spark transformer: 10,000V, 23 mA
- Electrodes: Position critical (1/8" gap, 5/16" ahead of nozzle)
- Ignition timing: 3-5 seconds before main fuel

**Flame detection:**
- Cadmium sulfide (CdS) cell
- Response time: 1-3 seconds
- Mounted to sight flame, not ignition spark

### Performance Characteristics

**Turndown ratio:** 2:1 to 3:1 maximum

Limited by:
- Minimum oil pressure for adequate atomization (60-80 psi)
- Air-fuel ratio maintenance
- Flame stability at low fire

**Combustion efficiency:**
- Properly tuned: 80-85%
- Stack temperature: 350-550°F
- Excess air: 25-50% (4-7% O₂)

**Emissions:**
- NOx: 80-150 ppm (No. 2 oil)
- CO: 50-200 ppm (should be <100 ppm when tuned)
- Smoke: Trace 0 (zero smoke number when optimized)

### Applications and Sizing

**Typical applications:**
- Residential heating: 0.5-2.0 gph (70,000-280,000 Btu/h)
- Small commercial: 2.0-5.0 gph (280,000-700,000 Btu/h)
- Light industrial: 5-25 gph (0.7-3.5 MMBtu/h)

**Burner selection:**

Required nozzle size:

$$GPH = \frac{Q_{output}}{HHV \times \eta_{combustion}}$$

For No. 2 oil: $HHV = 140,000$ Btu/gal

$$GPH = \frac{Q_{Btu/h}}{140,000 \times 0.82} = \frac{Q}{114,800}$$

**Example:** 500,000 Btu/h output required:

$$GPH = \frac{500,000}{114,800} = 4.36 \text{ gph}$$

Select 4.5 gph nozzle (next larger standard size).

## Rotary Cup Burners

### Operating Principle

**Atomization mechanism:**
1. Fuel oil fed to center of rotating cup
2. Centrifugal force spreads oil across cup inner surface
3. Oil flows to cup rim (1500-6000 RPM)
4. High tangential velocity at rim (100-300 ft/s)
5. Oil leaves rim as thin sheet
6. Aerodynamic forces break sheet into droplets
7. Primary air supplied around cup for atomization assistance

**Centrifugal atomization advantage:** Mechanical energy atomizes fuel rather than pressure energy alone. Achieves fine atomization at lower pressures (5-50 psi vs. 100-300 psi).

### Sauter Mean Diameter - Rotary Atomization

Empirical SMD correlation:

$$d_{32} = 2.9 \sigma^{0.6} \left(\frac{\dot{m}}{\rho_a V_{rel}}\right)^{0.4} + 0.068 \left(\frac{\mu_l^2}{\rho_l \sigma}\right)^{0.25} D_{cup}$$

Where:
- $V_{rel}$ = Relative velocity between oil and air (ft/s)
- $\mu_l$ = Oil dynamic viscosity (centipoise)
- $D_{cup}$ = Cup diameter (in)

**Key parameter - Rotational speed:**

$$V_{rim} = \pi D_{cup} \times \frac{RPM}{60}$$

Higher RPM → higher rim velocity → finer atomization.

**Typical SMD:** 40-100 μm for No. 2 oil, 80-150 μm for No. 6 oil

### Cup Design

**Cup configurations:**
- Plain rim cup: Simple, lower cost
- Serrated rim cup: Better atomization, higher air shear
- Vaned cup: Internal vanes increase centrifugal force

**Cup diameter:** 2-6 inches (larger for heavy fuels, higher flow rates)

**Rotational speed:**
- Small burners: 3000-6000 RPM
- Large burners: 1500-3000 RPM
- Drive: Direct-coupled electric motor or air turbine

### Air System

**Primary air:**
- Supplied at high velocity (100-200 ft/s) around cup
- Provides atomization assistance via aerodynamic shear
- Flow: 20-40% of total combustion air
- Pressure: 2-10 in w.c.

**Secondary air:**
- Supplied at lower velocity for combustion completion
- Flow: 60-80% of total air
- Adjustable dampers for air-fuel ratio control

### Performance Characteristics

**Turndown ratio:** 4:1 to 8:1

Achieved by:
- Variable fuel flow (5-50 psi modulating pressure)
- Constant cup speed
- Modulating air dampers
- Electronic air-fuel ratio control

**Combustion efficiency:**
- Properly tuned: 82-87%
- Stack temperature: 300-450°F
- Excess air: 15-30% (2.5-5% O₂)

**Emissions:**
- NOx: 60-120 ppm (No. 2 oil), 80-150 ppm (No. 6 oil)
- CO: 25-100 ppm
- Smoke: Trace 0-1

### Applications and Sizing

**Typical applications:**
- Commercial heating: 1-10 MMBtu/h
- Industrial process: 5-50 MMBtu/h
- Medium commercial boilers: 2-15 MMBtu/h

**Capacity range:** 10-500 gph (1.4-70 MMBtu/h)

**Selection criteria:**
- Turndown requirement >3:1: Rotary superior to gun-type
- Viscous fuels (No. 4-6): Rotary handles better with preheating
- Modulating control: Rotary provides smooth modulation

## Air Atomizing Burners

### Operating Principle

**Twin-fluid atomization:**
1. Low-pressure fuel oil (5-30 psi) supplied to nozzle
2. High-pressure air (30-100 psi) supplied to nozzle
3. Air and oil converge in mixing chamber
4. High-velocity air stream (400-800 ft/s) shears oil
5. Internal mixing produces fine droplets before discharge
6. External mixing produces droplets at nozzle exit

**Atomizing air requirement:**

$$\frac{\dot{m}_{air}}{\dot{m}_{fuel}} = 0.05 - 0.30 \text{ (mass ratio)}$$

Typical: 0.10-0.15 lb air per lb oil

### Sauter Mean Diameter - Air Atomization

$$d_{32} = k \left(\frac{\sigma}{\rho_a V_{rel}^2}\right)^{0.5} \left(1 + \frac{1}{ALR}\right)$$

Where:
- $ALR$ = Air-to-liquid mass ratio
- $V_{rel}$ = Relative velocity (ft/s)
- $k$ = Empirical constant (function of nozzle design)

**Key relationship:** SMD decreases with increasing ALR and air velocity.

**Typical SMD:** 20-60 μm (finest atomization among oil burner types)

### Nozzle Types

**Internal mixing:**
- Air and fuel mix inside nozzle body
- Higher atomization quality
- More prone to plugging
- Used for clean, light oils

**External mixing:**
- Air and fuel streams meet at nozzle exit
- Less prone to fouling
- Handles heavier, contaminated fuels
- Slightly larger droplet size

**Y-jet configuration:**
- Separate air and fuel passages
- Air jets impinge on fuel stream
- Good for wide flow range
- Common in industrial applications

### Performance Characteristics

**Turndown ratio:** 10:1 to 20:1

Achieved by:
- Modulating fuel pressure (5-30 psi)
- Modulating atomizing air pressure (30-100 psi)
- Maintaining approximately constant ALR
- Wide stable combustion range

**Combustion efficiency:**
- 82-88% (superior to gun-type and rotary)
- Fine atomization improves combustion completeness
- Lower excess air possible (10-20%)

**Emissions:**
- NOx: 50-100 ppm
- CO: <50 ppm
- Smoke: Trace 0

### Applications

**Typical uses:**
- Process heating requiring wide turndown
- Soot blower operation (intermittent firing)
- Dual-fuel burners (air for oil, gas self-aspirating)
- Heavy fuel oils with preheating

**Capacity range:** 5-200 gph (0.7-28 MMBtu/h)

## Steam Atomizing Burners

### Operating Principle

**Steam atomization process:**
1. Fuel oil supplied at low pressure (20-100 psi)
2. High-pressure steam supplied (60-300 psi)
3. Steam and oil converge in mixing chamber
4. Steam expands rapidly, fragmenting oil into droplets
5. Steam provides additional turbulence for mixing
6. Very fine atomization achieved (30-80 μm SMD)

**Steam consumption:**

$$\frac{\dot{m}_{steam}}{\dot{m}_{fuel}} = 0.10 - 0.40 \text{ (mass ratio)}$$

Typical: 0.20-0.30 lb steam per lb oil (2.4-3.6 lb/gal No. 2 oil)

### Sauter Mean Diameter - Steam Atomization

Similar to air atomization:

$$d_{32} = k \left(\frac{\sigma \dot{m}_{fuel}}{\dot{m}_{steam} V_{steam}}\right)^{0.5}$$

**Steam velocity:**

$$V_{steam} = \sqrt{2 g_c h}$$

Where $h$ = Enthalpy drop across nozzle (Btu/lb)

For 150 psig steam expanding to atmospheric:

$$h \approx 200 \text{ Btu/lb}, \quad V_{steam} \approx 2800 \text{ ft/s}$$

**Typical SMD:** 30-80 μm (finest atomization available)

### Nozzle Design

**Y-jet steam atomizers:**
- Steam jets impinge on oil stream at 60-90° angle
- Multiple steam ports (2-6) around fuel port
- External mixing design
- Handles heavy fuels well

**Return-flow atomizers:**
- Portion of fuel returned to tank
- Provides internal circulation and heating
- Improves atomization of viscous fuels
- Steam-to-fuel ratio adjustable

**Wide-range atomizers:**
- Variable steam and fuel orifices
- Turndown ratio up to 20:1
- Automatic turndown adjustment
- Used in large industrial boilers

### Performance Characteristics

**Turndown ratio:** 10:1 to 20:1 (highest among oil burners)

Achieved by:
- Modulating fuel flow valve
- Modulating steam flow valve (maintaining steam/oil ratio)
- Wide stable flame range
- Superior to all mechanical atomization methods

**Combustion efficiency:**
- 83-88%
- Lowest excess air requirement: 10-20% (1.5-3.5% O₂)
- Fine atomization enables complete combustion

**Emissions:**
- NOx: 50-100 ppm (No. 2), 80-140 ppm (No. 6)
- CO: <50 ppm
- Smoke: Trace 0

**Steam consumption impact:**

For 10 MMBtu/h burner with 0.25 lb steam/lb oil:
- Fuel flow: 71.4 lb/h oil
- Steam flow: 17.9 lb/h steam
- Steam heat: $17.9 \times 1000 = 17,900$ Btu/h
- Efficiency penalty: $17,900 / 10,000,000 = 0.18\%$ (negligible)

### Applications and Sizing

**Typical applications:**
- Large industrial boilers: 10-100 MMBtu/h
- Process heaters: 20-200 MMBtu/h
- Power plant auxiliary boilers
- Heavy fuel oil combustion (No. 5, No. 6)
- Marine boilers

**Capacity range:** 50-5000 gph (7-700 MMBtu/h)

**Selection criteria:**
- High turndown required (>8:1)
- Heavy fuel oils requiring superior atomization
- Low emissions essential
- Steam readily available (existing boiler plant)

**Sizing example:**

Required: 50 MMBtu/h output, No. 6 oil, 85% efficiency

$$\text{Fuel input} = \frac{50}{0.85} = 58.8 \text{ MMBtu/h}$$

$$GPH = \frac{58,800,000}{150,000 \text{ Btu/gal}} = 392 \text{ gph}$$

Steam requirement at 0.30 lb/lb oil:

$$\dot{m}_{steam} = 392 \times 7.4 \times 0.30 = 870 \text{ lb/h}$$

At 150 psig saturated steam: 870 lb/h steam consumption

## Burner Comparison and Selection

| Parameter | Gun-Type | Rotary | Air Atomizing | Steam Atomizing |
|-----------|----------|--------|---------------|-----------------|
| Capacity range | 0.5-25 gph | 10-500 gph | 5-200 gph | 50-5000 gph |
| Turndown ratio | 2:1 - 3:1 | 4:1 - 8:1 | 10:1 - 20:1 | 10:1 - 20:1 |
| SMD (No. 2 oil) | 50-80 μm | 40-100 μm | 20-60 μm | 30-80 μm |
| Fuel pressure | 100-300 psi | 5-50 psi | 5-30 psi | 20-100 psi |
| Atomizing medium | Pressure | Mechanical | Air | Steam |
| Efficiency | 80-85% | 82-87% | 82-88% | 83-88% |
| Excess air | 25-50% | 15-30% | 10-20% | 10-20% |
| NOx (ppm) | 80-150 | 60-120 | 50-100 | 50-100 |
| Heavy fuel capability | No | Yes | Limited | Excellent |
| First cost | Low | Medium | Medium | Medium-High |
| Maintenance | Low | Medium | Medium | Medium |

**Selection guidelines:**

1. **Capacity requirement:**
   - <1 gph: Gun-type only option
   - 1-25 gph: Gun-type or small rotary
   - 25-100 gph: Rotary or air atomizing
   - >100 gph: Steam atomizing or large rotary

2. **Turndown requirement:**
   - <3:1: Gun-type adequate
   - 3:1-8:1: Rotary preferred
   - >8:1: Air or steam atomizing required

3. **Fuel type:**
   - No. 2 oil: Any burner type suitable
   - No. 4 oil: Rotary, air, or steam (with preheating)
   - No. 5-6 oil: Steam atomizing strongly preferred

4. **Emissions limits:**
   - Standard: Gun-type or rotary acceptable
   - Low-NOx (<80 ppm): Air or steam atomizing
   - Ultra-low NOx (<50 ppm): Steam atomizing with FGR

5. **Steam availability:**
   - Available: Steam atomizing advantageous for large sizes
   - Not available: Air atomizing or rotary cup

## Nozzle Selection and Specification

### Nozzle Flow Rating (GPH)

Oil burner nozzles are rated at standard conditions: 100 psi pressure differential with No. 2 fuel oil at 60°F. The flow rate varies with pressure according to:

$$GPH = GPH_{rated} \sqrt{\frac{P_{actual}}{100}}$$

**Standard nozzle sizes (gph at 100 psi):**
- Residential: 0.50, 0.65, 0.75, 0.85, 1.00, 1.25, 1.50, 1.75, 2.00, 2.50, 3.00
- Commercial: 3.50, 4.00, 4.50, 5.00, 6.00, 7.00, 8.00, 10.0, 12.0, 15.0, 20.0

**Sizing calculation:**

Required firing rate converted to nozzle capacity:

$$GPH = \frac{Q_{input}}{HHV \times 1.0}$$

For No. 2 oil: $HHV = 140,000$ Btu/gal

**Example:** 700,000 Btu/h input required:

$$GPH = \frac{700,000}{140,000} = 5.0 \text{ gph}$$

Select 5.0 gph nozzle (exact match) or 5.5 gph (next larger).

**Pressure adjustment for fine-tuning:**

Reduce flow 10% from 5.0 gph nozzle:

$$P_{required} = 100 \times (0.90)^2 = 81 \text{ psi}$$

Adjust pump pressure regulator to 81 psi to achieve 4.5 gph effective flow.

### Spray Angle Selection

Spray angle defines the cone geometry of the fuel spray pattern. Critical for proper air-fuel mixing and flame shape matching to combustion chamber geometry.

**Standard spray angles:**
- Solid cone: 30°, 45°, 60°, 70°, 80°, 90°
- Hollow cone: 60°, 70°, 80°, 90°

**Selection criteria:**

| Combustion Chamber | Recommended Angle | Reason |
|-------------------|-------------------|---------|
| Short, wide | 80-90° | Wide spray fills chamber |
| Long, narrow | 45-60° | Narrow spray prevents impingement |
| Standard residential | 60-80° | Balanced flame shape |
| Retention head burner | 60-70° | Head stabilizes wide spray |
| Industrial box furnace | 30-45° | Long flame travel distance |

**Spray angle impact on combustion:**

Narrow angle (30-45°):
- Longer flame length
- Higher flame temperature at core
- Reduced wall impingement risk
- May require longer combustion chamber

Wide angle (80-90°):
- Shorter, bushy flame
- Faster air entrainment
- Better for compact chambers
- Risk of wall wetting if chamber too small

### Spray Pattern Type

**Solid cone pattern:**
- Fuel distributed throughout cone volume
- Better atomization at center
- Uniform heat release
- Standard for most applications

**Hollow cone pattern:**
- Fuel concentrated at cone periphery
- Air flows through cone center
- Enhanced air-fuel mixing
- Better for high excess air applications
- Common in industrial burners

**Semi-solid pattern:**
- Intermediate distribution
- Fuel concentrated near cone surface with some center distribution
- Compromise between solid and hollow
- Used for specific combustion chamber geometries

**Pattern selection:**

Standard residential/commercial: Solid cone 60-80°

Heavy commercial/industrial: Hollow cone 45-70°

Process heating: Semi-solid 60-80°

### Nozzle Spray Quality

**Delavan nozzle designations:**
- A: Hollow cone
- B: Solid cone (standard)
- AR: Auxiliary return (special flow pattern)
- PL: Special angle (15-30°)
- NS: Non-standard angle
- W: Wide angle (90°)
- H: Hollow cone with center solid stream

**Example nozzle specification:**

Delavan 3.00 gph 60° B

Interpretation:
- 3.00 gph flow at 100 psi
- 60° spray angle
- B = Solid cone pattern

### Dual-Orifice and Special Nozzles

**Dual-orifice nozzles:**

Two concentric spray patterns for improved turndown:
- Primary orifice: 30-40% of total flow (low fire)
- Secondary orifice: 60-70% of total flow (high fire)
- Total turndown: 3:1 to 4:1 (vs. 2:1 single nozzle)

**Operation:**
- Low fire: Primary orifice only (e.g., 2.0 gph)
- High fire: Both orifices (e.g., 5.0 gph total)
- Better atomization at low fire improves efficiency

**Return-flow nozzles:**

Portion of fuel returns to tank:
- Total pump flow > nozzle discharge
- Excess oil circulates through nozzle body
- Reduces oil temperature rise in gun assembly
- Improves heavy oil atomization
- Requires special pump with bypass

## Fuel Preheating for Heavy Oils

### Heavy Fuel Oil Characteristics

**Fuel oil grades and viscosity:**

| Grade | Viscosity at 100°F (SSU) | Pour Point (°F) | Preheat Required |
|-------|-------------------------|----------------|------------------|
| No. 2 | 32-38 | -10 to 20 | None |
| No. 4 | 45-125 | 20-40 | 100-120°F |
| No. 5 Light | 150-300 | 40-60 | 150-180°F |
| No. 5 Heavy | 300-900 | 50-75 | 180-220°F |
| No. 6 | 900-9000 | 60-90 | 200-240°F |

**Viscosity-temperature relationship:**

Walther equation for fuel oil:

$$\log \log(\nu + 0.7) = A - B \log T$$

Where:
- $\nu$ = Kinematic viscosity (centistokes)
- $T$ = Absolute temperature (°R)
- $A, B$ = Fuel-specific constants

**Target viscosity for atomization:**

Proper atomization requires:
- Pressure atomizing: 150-250 SSU (35-55 cSt)
- Rotary cup: 100-200 SSU (20-45 cSt)
- Steam atomizing: 100-150 SSU (20-35 cSt)

### Preheating System Design

**Tank heating:**

Maintain bulk storage temperature above pour point + 10-20°F:
- Steam coils in tank bottom
- Electric immersion heaters
- Heat tracing on tank walls
- Insulation to minimize losses

**Transfer line heating:**

Heat tracing maintains pumping viscosity:
- Electric heat tracing: 5-15 W/ft
- Steam tracing: 1/2" tube parallel to fuel line
- Insulation over tracing
- Temperature control at 20-40°F above pour point

**Burner preheater:**

Final heating to atomization viscosity:
- Steam-to-oil heater: Shell-and-tube design
- Electric preheater: Immersion elements in fuel chamber
- Temperature control: ±5°F of setpoint
- Safety: High-limit cutout at 250°F

**Preheater sizing:**

Heat required to raise oil temperature:

$$Q = \dot{m}_{oil} c_p \Delta T$$

Where:
- $\dot{m}_{oil}$ = Oil mass flow (lb/h)
- $c_p$ = Specific heat ≈ 0.45 Btu/(lb·°F) for fuel oil
- $\Delta T$ = Temperature rise (°F)

**Example:** 100 gph No. 6 oil, 70°F ambient, 220°F final temperature

Mass flow: $\dot{m} = 100 \times 7.8 = 780$ lb/h

Heat required: $Q = 780 \times 0.45 \times (220-70) = 52,650$ Btu/h

Select 60,000 Btu/h preheater (safety factor 1.15).

### Preheating Control Strategy

**Temperature sensing:**
- RTD sensor in oil stream downstream of preheater
- Response time: <10 seconds
- Accuracy: ±2°F

**Modulating control:**
- PID controller adjusts steam valve or electric power
- Setpoint: Target atomization temperature
- Prevents temperature overshoot (coking risk)

**Interlocks:**
- Burner permissive: Oil temperature >minimum setpoint
- High-limit shutdown: Oil temperature >maximum safe limit (250°F)
- Low flow shutdown: Prevents overheating at low fire

## Combustion Air Requirements

### Stoichiometric Air Calculation

**Theoretical air for complete combustion:**

For hydrocarbon fuel:

$$\text{Stoich Air} = \frac{11.5 \times C + 34.5(H - O/8) + 4.3S}{0.232}$$

Where C, H, O, S are weight fractions.

**Simplified for typical fuel oils:**

No. 2 oil composition: C=87%, H=13%

$$\text{Stoich Air} = \frac{11.5 \times 0.87 + 34.5 \times 0.13}{0.232} = 62.3 \text{ lb air/lb fuel}$$

Or: 1547 ft³ air/gal at 60°F (assuming air density 0.075 lb/ft³)

**Actual air requirement:**

$$\text{Actual Air} = \text{Stoich Air} \times (1 + \frac{EA}{100})$$

Where EA = Excess air percentage

**Example:** 5.0 gph burner with 25% excess air:

Stoichiometric: $5.0 \times 1547 = 7735$ ft³/h

Actual: $7735 \times 1.25 = 9669$ ft³/h = 161 cfm at 60°F

At combustion air temperature 70°F: $161 \times (530/520) = 164$ cfm

### Primary and Secondary Air Distribution

**Primary air (delivered by burner fan):**
- 80-100% of stoichiometric requirement
- High velocity (2000-4000 fpm at nozzle)
- Atomizes and mixes with fuel spray
- Creates flame pattern

**Secondary air (natural draft or induced):**
- 0-20% of stoichiometric plus all excess air
- Lower velocity (<1000 fpm)
- Completes combustion
- Provided by draft or entrained naturally

**Air distribution impact:**

High primary air percentage:
- Better initial mixing
- Shorter flame
- Higher fan power
- Reduced secondary air flexibility

Low primary air percentage:
- Longer flame
- May cause smoking if insufficient
- Lower fan power
- Greater secondary air control needed

### Combustion Air Temperature Effects

**Density correction:**

Air volume varies inversely with absolute temperature:

$$CFM_2 = CFM_1 \times \frac{T_2}{T_1}$$

Where T in °R (°F + 460)

**Cold ambient operation:**

Winter air at 0°F vs. 70°F:
- Density increase: 15%
- Volume flow decrease: 13% for same mass
- Over-airing tendency requires damper adjustment
- Improved combustion efficiency (denser air)

**Hot ambient operation:**

Mechanical room at 120°F:
- Density decrease: 11%
- Under-airing risk
- Reduced fan performance
- May require combustion air ducted from outdoors

**Preheated combustion air:**

Intentional air preheat (heat recovery):
- Every 100°F air preheat ≈ 1% efficiency gain
- Reduces fuel consumption
- Requires NOx consideration (higher flame temperature)
- Used in large industrial installations

## Flame Retention Heads

### Operating Principle

Flame retention head stabilizes combustion by creating:
- Recirculation zone of hot combustion products
- Low-velocity region for flame anchoring
- Enhanced air-fuel mixing through turbulence
- Continuous ignition source for incoming fuel-air mixture

**Mechanism:**
1. Primary air flows through head vanes (swirling)
2. Head creates wake region behind burner
3. Hot combustion products recirculate in wake
4. Incoming fuel-air mixture ignited by recirculation zone
5. Flame anchored at retention head face

### Design Configurations

**Vane patterns:**
- Straight vanes: Radial airflow, simple design
- Curved vanes: Swirling airflow, enhanced mixing
- Louvered vanes: Multiple air jets, high turbulence

**Head geometry:**
- Flat face: Standard retention
- Recessed face: Deeper recirculation zone
- Extended cone: Long flame applications
- Stabilizer ring: Enhanced low-fire retention

### Performance Benefits

**Improved combustion quality:**
- Smoke reduction: 30-50% lower smoke number
- CO reduction: 20-40% lower CO emissions
- Excess air reduction: Can operate at 15-25% vs. 30-50%
- Efficiency improvement: 1-3% combustion efficiency gain

**Turndown improvement:**
- Low-fire stability: Down to 40% of rated capacity
- Wider operating range without smoking
- Better modulating burner performance

**Flame characteristics:**
- Shorter, more compact flame
- Cooler flame tips (reduced NOx)
- Better flame pattern consistency
- Reduced combustion noise

### Selection and Adjustment

**Head sizing:**

Match retention head diameter to burner capacity:
- Small residential (0.5-2.0 gph): 2.5-3.5" diameter
- Medium commercial (2.0-5.0 gph): 3.5-4.5" diameter
- Large commercial (5.0-15 gph): 4.5-6.0" diameter

**Air pattern adjustment:**
- Vane angle: Controls swirl intensity
- Head position: Distance from nozzle affects mixing
- Air shutter: Modulates total primary air

**Nozzle positioning:**

Critical dimension - nozzle tip to head face:
- Too close (<1/4"): Flame impingement, sooting
- Optimal (5/16" to 3/8"): Proper mixing, clean flame
- Too far (>1/2"): Loss of retention benefit, smoking

## Efficiency Optimization

### Combustion Efficiency Fundamentals

**Total efficiency equation:**

$$\eta_{combustion} = \frac{Q_{released}}{Q_{input}} = 1 - \frac{Q_{losses}}{Q_{input}}$$

**Primary heat losses:**

1. **Dry flue gas loss:**

$$L_{dry} = \frac{K(T_{stack} - T_{ambient})}{CO_2}$$

Where K ≈ 0.48 for fuel oil

Typical: 12-18% loss at 400°F stack, 10% CO₂

2. **Moisture loss (H₂O from combustion):**

$$L_{H_2O} = 0.09 \times H \times (1 + \frac{EA}{100})$$

Where H = hydrogen fraction (0.13 for No. 2 oil)

Typical: 6-8% loss

3. **Incomplete combustion loss:**

From CO, smoke, unburned hydrocarbons: 0-5% if properly tuned

4. **Radiation and convection:** 1-2% for insulated equipment

**Achievable combustion efficiency:**

Optimized conditions: 82-86% combustion efficiency

### Excess Air Optimization

**Excess air determination:**

From flue gas O₂ measurement:

$$EA = \frac{O_2}{20.9 - O_2} \times 100$$

**Example:** Measured O₂ = 5%:

$$EA = \frac{5}{20.9-5} \times 100 = 31\%$$

**Optimal excess air range:**

| Burner Type | Optimal EA | O₂ Range |
|-------------|-----------|----------|
| Gun-type | 25-40% | 4-6% |
| Gun-type with retention head | 20-30% | 3-5% |
| Rotary cup | 15-25% | 2.5-4.5% |
| Air/steam atomizing | 10-20% | 1.5-3.5% |

**Effects of excess air deviation:**

Too low (<15%):
- Incomplete combustion
- CO formation
- Smoke and soot
- Efficiency loss from unburned fuel

Too high (>50%):
- Excessive stack heat loss
- Every 15% excess air ≈ 1% efficiency loss
- Increased fan power
- Lower flame temperature

### Stack Temperature Control

**Target stack temperatures:**

| Application | Target T_stack | Condensation Risk |
|-------------|---------------|-------------------|
| Non-condensing boiler | 350-450°F | Minimal |
| Hot water boiler | 300-400°F | Low |
| Steam boiler | 400-500°F | None |
| Condensing boiler | 120-160°F | Intentional |

**Stack temperature impact:**

Every 40°F stack temperature reduction ≈ 1% efficiency improvement

**Example calculation:**

Baseline: 450°F stack, 82% efficiency
Improved: 370°F stack (80°F reduction)

Efficiency gain: $80/40 \times 1\% = 2\%$

New efficiency: 84%

Annual savings for 5 MMBtu/h boiler at $15/MMBtu:

$$\text{Savings} = 5 \times 8760 \times \frac{2}{100} \times 15 = \$131,400/\text{year}$$

### Combustion Testing and Tuning

**Required measurements:**
- Stack temperature (°F)
- Flue gas O₂ or CO₂ (%)
- Carbon monoxide (ppm)
- Smoke number (Bacharach scale)
- Draft (in w.c.)

**Tuning procedure:**

1. **Initial settings:**
   - Set fuel pressure to rated value (100-150 psi gun-type)
   - Open air shutter fully
   - Start burner and allow warm-up (5-10 minutes)

2. **Reduce excess air:**
   - Close air shutter incrementally
   - Monitor CO and smoke
   - Target: CO <100 ppm, smoke trace 0-1
   - Final O₂: 3-5% for retention head burners

3. **Verify operation:**
   - Check flame pattern (no impingement, orange tips)
   - Confirm draft adequate (-0.02 to -0.04 in w.c. over fire)
   - Measure combustion efficiency

4. **Load variation test:**
   - Test at low fire and high fire (modulating burners)
   - Ensure clean combustion across operating range
   - Adjust linkages if necessary

**Optimization results:**

Properly tuned oil burner:
- Combustion efficiency: 82-85%
- Stack temperature: 350-450°F
- Excess air: 25-35% (4-5.5% O₂)
- CO: <100 ppm
- Smoke: Trace 0
- NOx: 80-120 ppm (No. 2 oil)
