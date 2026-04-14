---
title: "Evaporation Methods"
aliases: ["Evaporation Methods"]
description: "Comprehensive analysis of evaporation technologies for fruit juice concentration including single and multi-effect systems, vacuum evaporation, mechanical and thermal vapor recompression, heat transfer calculations, and aroma recovery systems"
weight: 1
---

## Overview

Evaporation remains the primary commercial method for concentrating fruit juices from typical feed concentrations of 10-15°Brix to final concentrations of 42-72°Brix. The fundamental challenge is removing water while preserving heat-sensitive flavor compounds, vitamins, and color pigments. Modern evaporation systems achieve this through low-temperature vacuum operation, short residence times, and integrated aroma recovery.

The evaporation process removes water vapor from juice by applying heat at temperatures below atmospheric boiling points through vacuum reduction. Energy efficiency is paramount due to the large quantities of water requiring vaporization—concentrating juice from 12°Brix to 60°Brix requires evaporating approximately 83% of the original mass.

## Evaporator Types for Juice Concentration

### Falling Film Evaporators

Falling film evaporators represent the industry standard for juice concentration due to minimal product degradation and short residence times.

**Operating Principles:**
- Juice distributed at tube top via distribution plates or nozzles
- Thin film flows down vertical tubes under gravity
- Steam condenses on tube exterior, heating falling film
- Vapor generated travels upward in tube center
- Liquid concentrate collects at bottom separator

**Performance Characteristics:**

| Parameter | Typical Value | Notes |
|-----------|---------------|-------|
| Tube length | 6-12 m | Longer tubes increase efficiency |
| Tube diameter | 50-75 mm | Larger for viscous products |
| Film thickness | 0.3-1.5 mm | Decreases with concentration |
| Heat transfer coefficient | 1500-3500 W/m²·K | Function of film velocity, viscosity |
| Residence time | 5-30 seconds | Critical for heat-sensitive juices |
| Evaporation rate | 5-50 kg/m²·h | Dependent on temperature differential |

**Heat Transfer Calculation:**

The overall heat transfer in falling film evaporators follows:

Q = U × A × LMTD

Where:
- Q = heat transfer rate (W)
- U = overall heat transfer coefficient (W/m²·K)
- A = heat transfer area (m²)
- LMTD = logarithmic mean temperature difference (K)

LMTD = (ΔT₁ - ΔT₂) / ln(ΔT₁/ΔT₂)

The overall heat transfer coefficient accounts for multiple resistances:

1/U = 1/h_steam + δ_wall/k_wall + 1/h_juice + R_fouling

Where:
- h_steam = steam-side heat transfer coefficient (8000-12000 W/m²·K)
- h_juice = juice-side heat transfer coefficient (1500-4000 W/m²·K)
- δ_wall = tube wall thickness (typically 1.5-2.5 mm)
- k_wall = thermal conductivity of stainless steel (16 W/m·K)
- R_fouling = fouling resistance (0.0001-0.0005 m²·K/W)

**Advantages:**
- Minimal thermal degradation
- Short residence time (10-30 seconds typical)
- High heat transfer coefficients
- Suitable for viscous products up to 70°Brix
- Effective with temperature-sensitive materials

**Limitations:**
- Requires minimum feed concentration (typically >8°Brix)
- Sensitive to flow distribution
- Not suitable for highly viscous products above 70°Brix
- Fouling can disrupt film formation

### Rising Film Evaporators

Rising film evaporators utilize vapor generation within vertical tubes to propel liquid upward as a thin film on tube walls.

**Operating Principles:**
- Dilute juice enters at tube bottom
- Steam heating initiates vapor bubble formation
- Expanding bubbles propel liquid upward
- Mixed two-phase flow develops along tube length
- Vapor and concentrate separate at top

**Performance Parameters:**

| Parameter | Typical Value | Notes |
|-----------|---------------|-------|
| Tube length | 8-15 m | Must achieve full film development |
| Tube diameter | 25-50 mm | Smaller than falling film |
| Heat transfer coefficient | 2000-4500 W/m²·K | Higher than falling film initially |
| Residence time | 2-10 seconds | Very short, good for heat-sensitive products |
| Maximum concentration | 35-40°Brix | Limited by film collapse |

**Advantages:**
- Very short residence time
- High heat transfer coefficients
- Self-cleaning action from turbulent flow
- Lower capital cost than falling film
- Effective for low-viscosity feeds

**Limitations:**
- Limited to lower final concentrations (typically 30-40°Brix)
- Requires higher temperature differentials
- Less flexible in operation
- Cannot handle suspended solids well

### Forced Circulation Evaporators

Forced circulation evaporators use external pumps to circulate juice through heat exchanger tubes at high velocity, preventing boiling within tubes.

**Operating Configuration:**
- Centrifugal pump circulates juice at 1.5-3 m/s
- External tube bundle or plate heat exchanger
- Boiling occurs only in flash chamber
- Concentrate recirculates multiple passes
- Temperature differential: 3-8 K

**Performance Specifications:**

| Parameter | Value | Application |
|-----------|-------|-------------|
| Circulation rate | 3-10 × evaporation rate | Prevents tube boiling |
| Tube velocity | 1.5-3.5 m/s | Reduces fouling |
| Heat transfer coefficient | 2500-5000 W/m²·K | High due to forced convection |
| Pump power | 15-40 kW per effect | Significant energy input |
| Maximum concentration | 50-60°Brix | Handles viscous products |

**Heat Transfer:**

For forced circulation evaporators, the tube-side heat transfer coefficient follows:

Nu = 0.023 × Re^0.8 × Pr^0.4

Where:
- Nu = Nusselt number = (h × D) / k
- Re = Reynolds number = (ρ × v × D) / μ
- Pr = Prandtl number = (Cp × μ) / k
- h = heat transfer coefficient (W/m²·K)
- D = tube diameter (m)
- v = fluid velocity (m/s)
- ρ = density (kg/m³)
- μ = dynamic viscosity (Pa·s)
- Cp = specific heat (J/kg·K)
- k = thermal conductivity (W/m·K)

**Applications:**
- High-viscosity products (40-60°Brix)
- Fouling-prone juices (high pulp content)
- Products with suspended solids
- Situations requiring low temperature differentials

### Plate Evaporators

Plate evaporators employ stacked heat transfer plates with alternating steam and juice channels, offering compact design and high efficiency.

**Design Features:**
- Gasketed or brazed plate assemblies
- Chevron or herringbone surface patterns
- Counter-current or co-current flow arrangements
- Modular design for capacity adjustment
- Typical plate spacing: 3-6 mm

**Performance Data:**

| Parameter | Range | Notes |
|-----------|-------|-------|
| Heat transfer coefficient | 3000-6000 W/m²·K | Highest among evaporator types |
| Temperature approach | 2-5 K | Very efficient heat transfer |
| Residence time | 10-60 seconds | Varies with configuration |
| Pressure drop | 20-100 kPa | Higher than shell-and-tube |
| Maximum concentration | 45-55°Brix | Limited by flow channels |

**Advantages:**
- Extremely high heat transfer coefficients
- Compact footprint (1/5 to 1/10 of shell-and-tube)
- Easy inspection and cleaning
- Flexible capacity through plate addition/removal
- Lower fouling tendency due to turbulence

**Limitations:**
- Gasket maintenance required (gasketed type)
- Limited to lower pressures (typically <10 bar)
- Channel blockage risk with high-pulp juices
- Higher pressure drop than shell-and-tube designs

## Multi-Effect Evaporator Configurations

Multi-effect evaporation cascades vapor from one effect to heat the next, dramatically improving steam economy.

### Forward Feed Configuration

Juice and vapor flow in the same direction from first to last effect.

**Characteristics:**
- Feed enters highest pressure/temperature effect
- Concentrate exits lowest pressure/temperature effect
- Simple pumping arrangement (gravity flow possible)
- Natural viscosity increase in direction of decreasing temperature
- Feed preheating often unnecessary

**Steam Economy:**

Steam economy (SE) represents kg water evaporated per kg steam supplied:

SE = W_total / W_steam

For ideal multi-effect systems:

SE_theoretical ≈ N × 0.85

Where N = number of effects. The 0.85 factor accounts for boiling point elevation and heat losses.

**Typical Steam Economies:**

| Configuration | Steam Economy | Live Steam (kg/h per 1000 kg/h water evaporated) |
|---------------|---------------|--------------------------------------------------|
| Single effect | 0.85-0.95 | 1050-1180 |
| Double effect | 1.6-1.8 | 555-625 |
| Triple effect | 2.3-2.7 | 370-435 |
| Quadruple effect | 3.0-3.6 | 280-335 |
| Quintuple effect | 3.7-4.5 | 222-270 |

### Backward Feed Configuration

Juice and vapor flow in opposite directions.

**Operating Principles:**
- Feed enters lowest pressure/temperature effect
- Concentrate exits highest pressure/temperature effect
- Requires interstage pumps between each effect
- Best for heat-sensitive products
- Lower product temperature exposure

**Advantages:**
- Minimizes high-temperature exposure of concentrated product
- Better for heat-sensitive juices
- More uniform concentration distribution
- Reduced thermal degradation

**Disadvantages:**
- Requires pumps between all effects
- Higher capital cost
- More complex control system
- Higher energy consumption for pumping

### Mixed Feed Configuration

Combines elements of forward and backward feed for optimal thermal efficiency and product quality.

**Typical Arrangement:**
- First effects: backward feed (product quality)
- Later effects: forward feed (energy efficiency)
- Optimizes temperature-concentration relationship
- Balances product quality and steam economy

## Operating Temperatures and Pressures

### Vacuum Levels and Boiling Points

Juice concentration occurs under vacuum to reduce boiling temperatures, preserving heat-sensitive compounds.

**Typical Operating Conditions:**

| Effect Position | Absolute Pressure (kPa) | Boiling Point (°C) | Vacuum Level (%) |
|-----------------|-------------------------|-------------------|------------------|
| First effect | 60-80 | 85-93 | 21-41 |
| Second effect | 40-55 | 76-84 | 46-61 |
| Third effect | 25-35 | 65-73 | 66-75 |
| Fourth effect | 15-20 | 54-60 | 80-85 |
| Fifth effect | 8-12 | 42-49 | 88-92 |

**Boiling Point Elevation:**

Dissolved solids raise the boiling point above that of pure water at the same pressure:

BPE = T_solution - T_water

For fruit juices, boiling point elevation correlates with concentration:

BPE ≈ (0.03 to 0.05) × °Brix

At 60°Brix and 20 kPa absolute pressure:
- Pure water boiling point: 60.1°C
- Juice boiling point: 60.1 + (0.04 × 60) = 62.5°C

This elevation must be considered in multi-effect temperature differential calculations.

### Temperature Differential Distribution

The available temperature differential between steam supply and final condenser divides among effects, pressure drops, and boiling point elevations.

**Example Calculation for Triple-Effect System:**

Given:
- Steam supply: 150 kPa (g), 121°C
- Condenser: 10 kPa (a), 46°C
- Total temperature differential: 75 K

Temperature differential allocation:
- Effect 1: 85-93°C (ΔT ≈ 28 K)
- Effect 2: 68-76°C (ΔT ≈ 25 K)
- Effect 3: 50-58°C (ΔT ≈ 22 K)

Each effect operates with 8-12 K differential between heating steam and boiling juice.

## Condensing Water Requirements

Condensing systems remove vapor from the final effect, maintaining vacuum and recovering condensate.

### Surface Condenser Sizing

Surface condensers cool vapor below saturation temperature using indirect heat exchange.

**Heat Load Calculation:**

Q_condenser = W_vapor × (h_vapor - h_condensate)

Where:
- W_vapor = vapor flow rate (kg/s)
- h_vapor = vapor enthalpy at condenser pressure (kJ/kg)
- h_condensate = condensate enthalpy at outlet (kJ/kg)

**Cooling Water Requirements:**

W_cooling = Q_condenser / (Cp_water × ΔT_water)

Typical values:
- Cooling water inlet: 25-30°C
- Cooling water outlet: 35-42°C
- ΔT_water: 8-12 K
- Cooling water ratio: 40-60 kg cooling water per kg vapor condensed

**Condenser Specifications:**

| Parameter | Shell-and-Tube | Plate Type |
|-----------|----------------|------------|
| Heat transfer coefficient | 1500-2500 W/m²·K | 2500-4000 W/m²·K |
| Cooling water velocity | 1.5-2.5 m/s | 0.4-0.8 m/s |
| Tube material | Stainless 316L, Titanium | Stainless 316L |
| Fouling factor | 0.0002 m²·K/W | 0.0001 m²·K/W |
| Subcooling | 2-5 K | 2-5 K |

### Barometric Condenser (Direct Contact)

Direct mixing of vapor and cooling water eliminates the temperature differential of surface condensers.

**Operating Principle:**
- Vapor contacts cold water spray directly
- Mixture drains through barometric leg
- Leg height provides sealing against vacuum
- Minimum leg height: 10.33 m at full vacuum

**Advantages:**
- Lower capital cost
- Higher heat transfer (no surface resistance)
- No fouling issues
- Simpler maintenance

**Disadvantages:**
- Mixed condensate and cooling water
- Cannot recover clean condensate
- Requires elevation for barometric leg
- Higher water consumption

## Vacuum Systems

### Vacuum Pump Selection

Vacuum pumps maintain system pressure by removing non-condensable gases that accumulate from air in-leakage and product degassing.

**Common Vacuum Pump Types:**

| Pump Type | Pressure Range (kPa-a) | Capacity Range (m³/h) | Typical Application |
|-----------|------------------------|----------------------|---------------------|
| Liquid ring | 3-100 | 50-5000 | Most common for food |
| Steam ejector | 1-50 | 100-10000 | Large installations |
| Rotary vane | 0.1-10 | 10-500 | Small systems |
| Roots blower | 5-100 | 500-20000 | Booster applications |

**Vacuum System Sizing:**

Required capacity includes:
1. Non-condensable gases from product (0.1-0.5% of vapor flow)
2. Air in-leakage (function of system tightness)
3. Process gases (CO₂ from juice, typically 0.2-0.8% by mass)

Total gas load = Product gases + In-leakage + Safety factor

Safety factor: 1.5-2.0 for commercial systems

**Liquid Ring Vacuum Pump Performance:**

Power consumption: P = (W_gas × R × T₁)/(η × (n-1)) × [(P₂/P₁)^((n-1)/n) - 1]

Where:
- W_gas = gas mass flow rate (kg/s)
- R = gas constant (J/kg·K)
- T₁ = inlet temperature (K)
- η = isentropic efficiency (0.50-0.65)
- n = polytropic exponent (1.2-1.4)
- P₁, P₂ = inlet and outlet pressure (Pa)

**Typical Operating Data:**

| System Pressure (kPa-a) | Gas Load (kg/h) | Pump Power (kW) | Sealing Water (L/min) |
|-------------------------|-----------------|-----------------|----------------------|
| 10 | 50 | 15 | 80 |
| 10 | 100 | 28 | 140 |
| 5 | 50 | 22 | 95 |
| 5 | 100 | 40 | 165 |

### Air In-Leakage Control

Maintaining vacuum integrity minimizes pump size and energy consumption.

**Typical In-Leakage Rates:**

| System Condition | In-Leakage Rate |
|------------------|-----------------|
| Excellent (new, welded) | <0.5 kg air/h per m³ volume |
| Good (gasketed, maintained) | 0.5-2.0 kg air/h per m³ |
| Fair (normal wear) | 2.0-5.0 kg air/h per m³ |
| Poor (maintenance needed) | >5.0 kg air/h per m³ |

**In-Leakage Testing:**

Rate of pressure rise test:
1. Isolate evacuated system
2. Monitor pressure increase over time
3. Calculate: In-leakage (kg/h) = V × dP/dt × M/(R × T)

Where:
- V = system volume (m³)
- dP/dt = pressure rise rate (Pa/s)
- M = molecular weight of air (29 kg/kmol)
- R = universal gas constant (8314 J/kmol·K)
- T = temperature (K)

## Mechanical Vapor Recompression (MVR)

MVR systems compress vapor from the evaporator, raising its temperature and pressure to serve as heating steam, eliminating or drastically reducing live steam requirements.

### Operating Principles

**Thermodynamic Cycle:**
1. Juice boils at low pressure/temperature (e.g., 15 kPa, 54°C)
2. Vapor compresses to higher pressure/temperature (e.g., 50 kPa, 81°C)
3. Compressed vapor condenses in evaporator heat exchanger
4. Condensate returns as makeup or product water
5. Small fresh steam supplement compensates heat losses

**Compression Requirements:**

For vapor at saturation:
- Compression ratio: 2.5-4.0
- Temperature lift: 20-30 K
- Specific work: 80-120 kJ/kg vapor

**Energy Calculation:**

Compressor power: P = W_vapor × Δh_compression / η_compressor

Where:
- W_vapor = vapor flow rate (kg/s)
- Δh_compression = enthalpy increase (kJ/kg)
- η_compressor = overall efficiency (0.65-0.75)

For saturated vapor compression:
- At 15 kPa (54°C): h = 2599 kJ/kg
- At 50 kPa (81°C): h = 2645 kJ/kg
- Δh ≈ 46 kJ/kg (isentropic)
- Actual Δh ≈ 65 kJ/kg (accounting for efficiency)

**Example MVR System:**

Evaporating 5000 kg/h water:
- Compressor power: (5000/3600 kg/s) × (65 kJ/kg) / 0.70 ≈ 130 kW
- Equivalent steam (if boiler efficiency 85%): 5000 kg/h
- Steam energy: 5000 × 2200 / 0.85 ≈ 12,940 MJ/h = 3595 kW thermal
- MVR electrical: 130 kW
- Energy ratio: 3595/130 ≈ 27.7

MVR systems convert high-grade electrical energy to low-grade thermal energy efficiently.

### Compressor Types for MVR

**Centrifugal Compressors:**
- Capacity: 1000-20000 kg/h vapor
- Compression ratio: 1.8-3.5
- Efficiency: 70-78%
- Speed: 3000-15000 rpm
- Best for large installations (>3000 kg/h)

**Roots Blowers:**
- Capacity: 100-5000 kg/h vapor
- Compression ratio: 1.5-2.5
- Efficiency: 50-65%
- Speed: 1000-3000 rpm
- Best for small to medium systems

**Performance Comparison:**

| Compressor Type | Capital Cost | Operating Cost | Turndown Ratio | Maintenance |
|-----------------|--------------|----------------|----------------|-------------|
| Centrifugal | High | Low | 50-100% | Low |
| Roots blower | Medium | Medium-High | 30-100% | Medium |
| Screw | Medium-High | Medium | 25-100% | Medium-High |

## Thermal Vapor Recompression (TVR)

TVR systems use high-pressure motive steam in ejectors to compress low-pressure vapor, reducing net steam consumption.

### Steam Ejector Design

**Operating Principle:**
- High-pressure motive steam (typically 600-1000 kPa)
- Entrains low-pressure vapor from evaporator
- Mixed steam compresses in diffuser section
- Supplies intermediate pressure steam to evaporator

**Performance Characteristics:**

Entrainment ratio = W_entrained / W_motive

Typical values:
- Single-stage ejector: 0.3-0.8
- Two-stage ejector: 0.8-1.5

**Energy Analysis:**

Net steam consumption = W_motive + W_makeup

Where W_makeup compensates for heat losses and concentration heat requirements.

**Steam Economy Improvement:**

| Base System | TVR Addition | Net Steam Economy | Steam Reduction |
|-------------|--------------|-------------------|-----------------|
| Single effect | Single stage | 1.5-1.8 | 40-47% |
| Double effect | Single stage | 2.4-2.8 | 25-33% |
| Triple effect | Single stage | 3.2-3.8 | 15-23% |

**Ejector Sizing Example:**

For 3000 kg/h vapor at 20 kPa entrained with 800 kPa motive steam:
- Entrainment ratio required: 0.5
- Motive steam: 3000/0.5 = 6000 kg/h
- Mixed steam pressure: 50-60 kPa
- Net steam saving vs. direct heating: 40%

### TVR vs. MVR Comparison

| Factor | TVR | MVR |
|--------|-----|-----|
| Capital cost | Low-Medium | High |
| Operating cost (steam) | Medium | Very Low |
| Operating cost (electric) | Low | Medium-High |
| Flexibility | Low | High |
| Maintenance | Very Low | Medium |
| Turndown capability | Poor (30-100%) | Good (25-100%) |
| Best application | Existing multi-effect | New installations, expensive steam |

## Energy Efficiency Considerations

### Heat Recovery Opportunities

**Condensate Heat Recovery:**

Evaporator condensate contains significant recoverable energy:
- Temperature: 80-95°C
- Heat content: 335-400 kJ/kg above 25°C ambient

Recovery applications:
1. Feed juice preheating
2. CIP solution heating
3. Building heating water
4. Boiler makeup preheating

Energy recovery = W_condensate × Cp × (T_condensate - T_reference)

For 5000 kg/h condensate at 90°C:
Q = 5000 × 4.18 × (90-25) = 1,358,500 kJ/h = 377 kW

**Vapor Condensation Energy:**

Final effect vapor represents the largest energy loss:
- Latent heat: 2300-2450 kJ/kg
- Sensible cooling: 40-80 kJ/kg
- Total: 2340-2530 kJ/kg

### Overall System Efficiency

**Total Energy Balance:**

Energy input sources:
1. Live steam to first effect: E_steam
2. Electrical drives (pumps, fans): E_electric
3. Vacuum pump energy: E_vacuum

Energy outputs:
1. Water evaporation (useful): E_evaporation
2. Concentrate heating: E_concentrate
3. Condensate heat: E_condensate
4. Condenser cooling water: E_cooling
5. Losses (radiation, convection): E_losses

Overall thermal efficiency:
η_thermal = E_evaporation / (E_steam + E_electric × 2.5)

The factor 2.5 converts electrical energy to equivalent thermal energy (assumes 40% power generation efficiency).

**Typical Efficiency Values:**

| System Configuration | Thermal Efficiency | Specific Energy (kJ/kg water evaporated) |
|---------------------|-------------------|------------------------------------------|
| Single effect | 75-82% | 3000-3200 |
| Triple effect | 83-87% | 1100-1300 |
| Quintuple effect | 85-89% | 650-800 |
| MVR single effect | 90-94% | 280-350 (electrical equivalent) |
| Triple effect + TVR | 86-90% | 850-1000 |

## Aroma Recovery Systems

Volatile flavor compounds evaporate preferentially during concentration, requiring capture and reincorporation to maintain juice quality.

### Volatile Compound Behavior

**Key Aroma Compounds in Fruit Juice:**

| Compound Class | Relative Volatility | Concentration Effect |
|----------------|---------------------|---------------------|
| Acetaldehyde | 15-25 | Lost first, harsh odor |
| Ethyl acetate | 8-15 | Fruity notes |
| Alcohols (ethanol) | 5-10 | Fermented character |
| Esters | 3-8 | Primary fruit character |
| Terpenes | 2-5 | Citrus notes |
| Aldehydes | 1.5-4 | Green, fresh notes |

Relative volatility α = y/x (vapor mole fraction / liquid mole fraction)

Compounds with α > 2 concentrate significantly in first vapors.

### Essence Recovery Process

**Stripping Column Operation:**

1. **Feed Position:** First 5-15% of feed juice enters stripping column
2. **Operating Conditions:**
   - Pressure: 30-50 kPa absolute
   - Temperature: 40-55°C
   - Theoretical stages: 3-6
3. **Vapor Collection:** Aroma-rich vapor exits column top
4. **Depleted Juice:** Proceeds to main evaporator

**Essence Concentration:**

Stripped vapor condenses and re-concentrates:
- Primary condensation: 95-98°C to liquid
- Secondary evaporation at 20-30 kPa
- Final essence concentration: 100-500 fold

**Typical Essence Recovery System:**

| Parameter | Value | Notes |
|-----------|-------|-------|
| Feed rate to stripper | 5-15% of total feed | Higher for more aroma |
| Stripper vapor rate | 0.5-2% of feed mass | Rich in volatiles |
| Essence concentration | 100-500× | Depends on compound |
| Final essence volume | 0.1-0.3% of feed | Added back to concentrate |
| Aroma recovery efficiency | 60-85% | Varies by compound |

**Integration with Main Evaporator:**

```
Feed Juice (100%) → Split
                     ├─→ Stripper (10%) → Depleted Feed (9.5%) ──┐
                     │                                            │
                     │   Aroma Vapor (0.5%) → Condenser → Essence│
                     │                                            ↓
                     └─→ Main Evaporator (90%) ←─────────────────┘
                              ↓
                         Concentrate (17%) + Water Vapor (83%)
                              ↓
                         Essence Addition (0.1%)
                              ↓
                         Final Product (17.1%)
```

### Essence Stability and Storage

**Degradation Mechanisms:**
- Oxidation of terpenes and aldehydes
- Polymerization reactions
- Thermal degradation during storage
- Microbial contamination

**Preservation Methods:**

| Method | Storage Conditions | Shelf Life | Application |
|--------|-------------------|------------|-------------|
| Refrigeration | 0-4°C, inert atmosphere | 6-12 months | Short-term |
| Freezing | -18 to -25°C | 18-24 months | Medium-term |
| Aseptic storage | 20°C, sterile, inert | 12-18 months | Convenient |
| Phase separation | Aqueous/oil phases separate | 12-24 months | Technical grades |

## Fouling and Cleaning

### Fouling Mechanisms in Juice Evaporators

**Types of Fouling:**

1. **Protein Denaturation:**
   - Temperature-dependent precipitation
   - Adheres to hot surfaces
   - Resistance: 0.0002-0.001 m²·K/W

2. **Pectin Gelation:**
   - Concentration and temperature dependent
   - Forms gel layer on surfaces
   - Resistance: 0.0001-0.0005 m²·K/W

3. **Mineral Scale:**
   - Calcium and magnesium phosphates, oxalates
   - Crystallization from supersaturation
   - Resistance: 0.001-0.005 m²·K/W

4. **Caramelization:**
   - Sugar degradation at high temperatures
   - Darkens surfaces, difficult to remove
   - Resistance: 0.0005-0.002 m²·K/W

**Fouling Impact on Performance:**

As fouling layer builds:
1. Heat transfer coefficient decreases
2. Evaporation rate declines
3. Energy consumption increases
4. Product temperature rises (quality loss)

**Fouling Resistance Growth:**

R_fouling(t) = R_asymptotic × (1 - e^(-t/τ))

Where:
- t = operating time
- τ = fouling time constant (10-100 hours)
- R_asymptotic = maximum fouling resistance

### Cleaning-in-Place (CIP) Systems

**CIP Sequence for Juice Evaporators:**

1. **Pre-Rinse:** Water flush at 60-70°C, 15-30 min
2. **Alkaline Wash:** 1.5-2.5% NaOH, 75-85°C, 30-60 min
3. **Intermediate Rinse:** Water flush until neutral pH
4. **Acid Wash:** 1-2% HNO₃ or citric acid, 60-75°C, 20-40 min
5. **Final Rinse:** Water flush until neutral pH and conductivity <500 μS/cm
6. **Sanitization:** Hot water >85°C or chemical sanitizer

**CIP Solution Specifications:**

| Stage | Chemical | Concentration | Temperature | Duration | Velocity |
|-------|----------|---------------|-------------|----------|----------|
| Alkaline | NaOH | 1.5-2.5% | 75-85°C | 30-60 min | >1.5 m/s |
| Acid | Nitric acid | 1.0-2.0% | 60-75°C | 20-40 min | >1.5 m/s |
| Sanitizing | Hot water | - | >85°C | 15-30 min | >1.0 m/s |

**CIP Effectiveness Monitoring:**

Parameters tracked:
- Solution temperature (continuous)
- Concentration (conductivity or titration)
- pH (continuous monitoring)
- Turbidity (cleaning progress indicator)
- Final rinse conductivity (<500 μS/cm target)
- ATP swabs for biofilm detection

**CIP System Design:**

Required flow rates:
- Evaporator tubes: 1.5-2.5 m/s
- Spray balls: 3-8 L/min per ball
- Tank capacity: 1.5-2× system holdup volume
- Heating capacity: Raise full charge 40 K in <30 minutes

## Equipment Specifications and Selection

### Evaporator Capacity Determination

**Design Basis:**

Required evaporation rate:

W_evap = Q_feed × (C_final - C_feed) / C_final

Where:
- Q_feed = feed flow rate (kg/h)
- C_feed = feed concentration (fraction)
- C_final = final concentration (fraction)

**Example Calculation:**

Orange juice concentration:
- Feed: 10,000 kg/h at 12°Brix
- Product: 65°Brix
- Required evaporation: 10,000 × (0.65 - 0.12) / 0.65 = 8,154 kg/h

### Heat Transfer Area Sizing

**Single Effect Calculation:**

A = W_evap × λ / (U × LMTD)

Where:
- λ = latent heat of vaporization (≈2300 kJ/kg)
- U = overall heat transfer coefficient (W/m²·K)
- LMTD = log mean temperature difference (K)

For orange juice example at 20 kPa evaporation:
- W_evap = 8,154 kg/h = 2.265 kg/s
- λ = 2358 kJ/kg
- U = 2000 W/m²·K (falling film evaporator)
- Steam at 150 kPa: T = 111.4°C
- Juice boiling: T = 60.1 + 3.6 (BPE) = 63.7°C
- LMTD ≈ 47 K (calculated)

A = (2.265 × 2,358,000) / (2000 × 47) = 56.7 m²

With fouling factor 1.25: A_actual = 70.9 m²

### Multi-Effect System Design Summary

**Triple-Effect Orange Juice Concentrator:**

| Effect | Pressure (kPa-a) | Temperature (°C) | Area (m²) | Steam Economy |
|--------|------------------|------------------|-----------|---------------|
| First | 70 | 90 | 42 | - |
| Second | 35 | 73 | 48 | - |
| Third | 15 | 54 | 56 | - |
| Total | - | - | 146 | 2.6 |

Operating parameters:
- Feed rate: 10,000 kg/h at 12°Brix
- Product: 1,846 kg/h at 65°Brix
- Water removed: 8,154 kg/h
- Live steam: 3,136 kg/h at 200 kPa
- Cooling water: 360 m³/h at 8 K rise
- Vacuum pump: 45 kW
- Feed pump: 15 kW
- Total power: 60 kW

**Economic Considerations:**

Capital cost increases approximately:
- Single to double effect: +60-80%
- Double to triple effect: +50-70%
- Triple to quadruple effect: +45-60%

Operating cost decreases with each effect addition, but diminishing returns occur beyond 5 effects for most applications due to:
- Increased complexity
- Higher fouling rates at lower temperatures
- Larger heat transfer areas required
- Higher vacuum system costs

The optimal configuration balances capital cost, energy cost, product quality requirements, and operational complexity.

## Process Control and Automation

### Critical Control Parameters

**Primary Variables:**

| Parameter | Typical Range | Control Method | Importance |
|-----------|---------------|----------------|------------|
| Feed rate | 80-100% design | Flow control valve | Production rate |
| Steam pressure | ±5% setpoint | Pressure control valve | Heat input |
| Vacuum level | ±2 kPa | Vacuum pump speed | Boiling point |
| Concentrate °Brix | ±0.5°Brix | Product valve | Quality |
| Liquid level | 30-70% | Feed/product valves | Stability |

**Advanced Control Strategies:**

1. **Cascade Control:** Steam pressure cascade to evaporator temperature
2. **Feedforward Control:** Feed flow rate adjusts steam valve anticipatorily
3. **Model Predictive Control (MPC):** Optimizes multi-variable system performance
4. **Adaptive Control:** Adjusts parameters based on fouling progression

Modern systems employ distributed control systems (DCS) with continuous monitoring of 40-100+ parameters for optimal performance and product quality assurance.
