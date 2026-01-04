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
