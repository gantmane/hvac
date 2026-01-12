---
title: "Vapor Compression Cycles"
description: "Comprehensive analysis of vapor compression refrigeration cycles including ideal vs actual cycles, P-h diagram analysis, COP calculations, multi-stage compression, cascade systems, economizers, subcooling and superheat effects, and performance optimization for HVAC professionals."
weight: 1
---

The vapor compression cycle forms the foundation of modern refrigeration and air conditioning systems. This thermodynamic cycle transfers thermal energy from a low-temperature region to a high-temperature region through the phase change and compression of a refrigerant working fluid.

## Ideal Vapor Compression Cycle

The ideal vapor compression cycle consists of four reversible processes operating between two constant pressure levels:

### Process Sequence

1. **Isentropic Compression (1→2)**: Saturated vapor enters the compressor and undergoes reversible adiabatic compression to condenser pressure
2. **Isobaric Heat Rejection (2→3)**: Superheated vapor flows through the condenser, desuperheating, condensing, and subcooling to saturated liquid
3. **Isenthalpic Expansion (3→4)**: Saturated liquid expands through a throttling device to evaporator pressure
4. **Isobaric Heat Absorption (4→1)**: Two-phase refrigerant evaporates completely to saturated vapor

### Thermodynamic Analysis

For the ideal cycle operating between evaporator pressure P_evap and condenser pressure P_cond:

**Refrigeration Effect:**
```
q_e = h₁ - h₄ = h₁ - h₃  [kJ/kg]
```

**Compression Work:**
```
w_comp = h₂s - h₁  [kJ/kg]
```

**Heat Rejection:**
```
q_c = h₂s - h₃  [kJ/kg]
```

**Coefficient of Performance (COP):**
```
COP_ideal = q_e / w_comp = (h₁ - h₄) / (h₂s - h₁)
```

Where subscript 's' denotes isentropic compression.

### Carnot Cycle Comparison

The Carnot refrigeration cycle represents the theoretical maximum efficiency between two temperature reservoirs. For refrigeration:

```
COP_Carnot = T_evap / (T_cond - T_evap)
```

The vapor compression cycle achieves 50-60% of Carnot COP due to:
- Irreversible throttling process (replacing isentropic expansion)
- Pressure drops in heat exchangers
- Non-isothermal heat transfer
- Compressor inefficiencies

## Actual Vapor Compression Cycle

Real refrigeration systems deviate significantly from the ideal cycle due to irreversibilities and practical design constraints.

### Key Deviations from Ideal Cycle

| Parameter | Ideal Cycle | Actual Cycle | Impact |
|-----------|-------------|--------------|--------|
| Evaporator outlet | Saturated vapor | 5-10°F superheat | Prevents liquid slugging |
| Condenser outlet | Saturated liquid | 5-15°F subcooling | Ensures liquid to expansion valve |
| Compression | Isentropic (s = const) | Polytropic (η = 0.65-0.85) | Increased work, discharge temp |
| Pressure drop | Zero | 2-5 psi evaporator, 5-10 psi condenser | Reduces capacity, increases work |
| Expansion | Isenthalpic | Isenthalpic | Same as ideal |

### Compressor Isentropic Efficiency

Real compressor performance is characterized by isentropic efficiency:

```
η_isentropic = (h₂s - h₁) / (h₂a - h₁)
```

Where:
- h₂s = enthalpy after isentropic compression
- h₂a = actual discharge enthalpy

Typical isentropic efficiencies by compressor type:

| Compressor Type | Isentropic Efficiency | Application Range |
|-----------------|----------------------|-------------------|
| Reciprocating | 0.70 - 0.85 | 1 - 100 tons |
| Scroll | 0.65 - 0.78 | 2 - 60 tons |
| Screw (single) | 0.65 - 0.75 | 20 - 300 tons |
| Screw (twin) | 0.70 - 0.80 | 50 - 1000 tons |
| Centrifugal | 0.75 - 0.85 | 100 - 10,000 tons |

### Volumetric Efficiency

Volumetric efficiency accounts for re-expansion of clearance volume gas and suction valve pressure drop:

```
η_vol = (V_act / V_swept) = 1 - C(r^(1/n) - 1) - L_valve
```

Where:
- C = clearance volume ratio (0.02-0.06 for reciprocating)
- r = pressure ratio (P_discharge / P_suction)
- n = polytropic exponent (1.1-1.3)
- L_valve = valve loss factor (0.02-0.05)

## Pressure-Enthalpy (P-h) Diagram Analysis

The P-h diagram provides essential visualization of refrigeration cycle performance and enables rapid cycle analysis.

### Diagram Regions

**Subcooled Liquid Region** (left of saturated liquid line):
- Single-phase liquid below saturation temperature
- Subcooling degree = T_sat - T_actual at constant pressure
- Increases refrigeration effect, reduces flash gas

**Two-Phase Region** (between saturation lines):
- Liquid-vapor mixture at constant temperature and pressure
- Quality x = m_vapor / m_total
- Primary region for evaporation and condensation

**Superheated Vapor Region** (right of saturated vapor line):
- Single-phase vapor above saturation temperature
- Superheat degree = T_actual - T_sat at constant pressure
- Necessary for compressor protection

### Critical State Points on P-h Diagram

For R-410A at standard rating conditions (ARI 550/590):
- Evaporating temperature: 45°F (410 psia)
- Condensing temperature: 130°F (2350 psia)

| State Point | Condition | Pressure (psia) | Enthalpy (Btu/lb) | Temperature (°F) |
|-------------|-----------|-----------------|-------------------|------------------|
| 1 - Compressor inlet | Saturated vapor + 10°F SH | 118 | 175.2 | 55 |
| 2 - Compressor discharge | Superheated vapor | 475 | 196.8 | 165 |
| 3 - Condenser outlet | Saturated liquid + 10°F SC | 475 | 48.5 | 120 |
| 4 - Evaporator inlet | Two-phase mixture | 118 | 48.5 | 45 |

Performance metrics:
```
Refrigeration effect = h₁ - h₄ = 175.2 - 48.5 = 126.7 Btu/lb
Compression work = h₂ - h₁ = 196.8 - 175.2 = 21.6 Btu/lb
COP = 126.7 / 21.6 = 5.86
```

### P-h Diagram Applications

**Cycle modifications visualization:**
- Quantify effect of subcooling and superheat
- Evaluate multi-stage compression benefits
- Analyze economizer cycle improvements
- Determine flash gas formation

**Performance troubleshooting:**
- Identify inefficient operating conditions
- Diagnose compressor issues (high superheat)
- Detect refrigerant charge problems
- Evaluate heat exchanger fouling

## Coefficient of Performance Calculations

### Basic COP Formulations

**Refrigeration COP:**
```
COP_R = Q_evap / W_comp = ṁ(h₁ - h₄) / ṁ(h₂ - h₁) = (h₁ - h₄) / (h₂ - h₁)
```

**Heat Pump COP:**
```
COP_HP = Q_cond / W_comp = (h₂ - h₃) / (h₂ - h₁)
```

**Energy Balance Relationship:**
```
COP_HP = COP_R + 1
```

### COP Variation with Operating Conditions

For R-134a vapor compression cycle (ASHRAE Handbook - Fundamentals):

| T_evap (°F) | T_cond (°F) | Compression Ratio | COP_R | Discharge Temp (°F) |
|-------------|-------------|-------------------|-------|---------------------|
| 40 | 100 | 2.94 | 5.82 | 125 |
| 40 | 120 | 3.81 | 4.35 | 150 |
| 40 | 140 | 4.88 | 3.28 | 178 |
| 20 | 100 | 3.68 | 4.52 | 138 |
| 0 | 100 | 4.71 | 3.47 | 153 |
| -20 | 100 | 6.25 | 2.65 | 172 |

**Key observations:**
- COP decreases as condensing temperature increases (reduced Carnot efficiency)
- COP decreases as evaporating temperature decreases (increased lift)
- Compression ratio exponentially impacts discharge temperature
- High discharge temperatures limit compressor operation (typically 225-250°F max)

### Actual COP Accounting for Component Inefficiencies

```
COP_actual = COP_ideal × η_compressor × η_motor / (1 + ΔP_fraction)
```

Where:
- η_compressor = combined isentropic and volumetric efficiency
- η_motor = motor efficiency (0.85-0.95)
- ΔP_fraction = pressure drop impact factor (1.02-1.08)

Example calculation for scroll compressor system:
```
COP_ideal = 5.86
η_isentropic = 0.70
η_volumetric = 0.95
η_motor = 0.90
ΔP_fraction = 1.05

COP_actual = 5.86 × 0.70 × 0.95 × 0.90 / 1.05 = 3.32
```

## Effects of Subcooling and Superheat

### Subcooling Analysis

Subcooling the refrigerant liquid below saturation temperature at condenser pressure increases system capacity and efficiency.

**Benefits of subcooling:**

1. **Increased refrigeration effect**: Lower enthalpy entering expansion valve
2. **Reduced flash gas**: Less vapor formed during throttling
3. **Improved compressor efficiency**: Higher mass flow for given displacement

**Quantitative impact:**

For R-410A at 130°F condensing, 45°F evaporating:

| Subcooling (°F) | h₃ (Btu/lb) | Flash Gas (%) | q_e (Btu/lb) | COP Change |
|-----------------|-------------|---------------|--------------|------------|
| 0 | 52.3 | 24.8 | 122.9 | Baseline |
| 5 | 50.8 | 23.2 | 124.4 | +1.2% |
| 10 | 49.3 | 21.6 | 125.9 | +2.4% |
| 15 | 47.8 | 20.0 | 127.4 | +3.7% |
| 20 | 46.3 | 18.4 | 128.9 | +4.9% |

**Rule of thumb**: Each 1°F of subcooling increases capacity by approximately 0.5%.

**Methods to achieve subcooling:**
- Oversized condenser coil area
- Dedicated subcooler heat exchanger
- Suction-to-liquid heat exchanger (internal heat exchange)
- Mechanical subcooling (separate refrigeration circuit)

### Superheat Analysis

Superheat serves protective and operational functions but impacts cycle performance differently at evaporator vs compressor inlet.

**Evaporator superheat (useful superheat):**
- Ensures complete evaporation before leaving coil
- Prevents liquid floodback to compressor
- Typical range: 5-10°F
- Minimal impact on capacity (slight decrease)

**Suction line superheat (parasitic superheat):**
- Heat gain from ambient environment
- Reduces refrigeration effect (higher h₁)
- Increases compression work (higher specific volume)
- Should be minimized through insulation

**Compressor inlet superheat impact:**

For R-134a at 40°F evaporating, 100°F condensing:

| Total Superheat (°F) | h₁ (Btu/lb) | v₁ (ft³/lb) | q_e (Btu/lb) | COP_R |
|---------------------|-------------|-------------|--------------|-------|
| 5 | 104.2 | 0.385 | 66.5 | 5.82 |
| 10 | 105.1 | 0.392 | 65.6 | 5.68 |
| 15 | 106.0 | 0.398 | 64.7 | 5.55 |
| 20 | 106.9 | 0.405 | 63.8 | 5.42 |
| 30 | 108.7 | 0.418 | 62.0 | 5.18 |

**Rule of thumb**: Each 10°F of superheat reduces capacity by approximately 2-3%.

### Suction-to-Liquid Heat Exchanger (SLHX)

Internal heat exchange between cold suction gas and warm liquid refrigerant provides:

**Advantages:**
- Guaranteed liquid to expansion valve (prevents flash gas in receiver)
- Reduced compressor suction temperature variation
- Improved capacity for refrigerants with wet compression (e.g., R-134a, R-407C)

**Disadvantages:**
- Increased compressor discharge temperature
- Reduced COP for dry compression refrigerants (e.g., R-22, R-410A)
- Additional pressure drop

**Effectiveness calculation:**

```
ε = (T_liquid,in - T_liquid,out) / (T_liquid,in - T_suction,in)
```

Typical effectiveness: 0.40 - 0.70

**Application guidelines:**

| Refrigerant | SLHX Recommended | Typical COP Change |
|-------------|------------------|-------------------|
| R-134a | Yes | +2% to +5% |
| R-404A | Yes | +1% to +3% |
| R-407C | Yes | +2% to +4% |
| R-410A | No | -1% to -2% |
| R-22 | No | 0% to -1% |
| NH₃ (Ammonia) | No | -2% to -3% |

## Multi-Stage Compression Systems

Multi-stage compression divides the compression process into two or more steps with intercooling, reducing compression work and discharge temperature for high pressure ratio applications.

### Two-Stage Compression with Intercooling

**Application criteria:**
- Compression ratio > 8:1 (typically T_evap < 0°F, T_cond > 100°F)
- Discharge temperature > 250°F in single-stage
- Large capacity systems (> 100 tons)

**Optimal intermediate pressure:**

For minimum total compression work, the optimal intermediate pressure is the geometric mean:

```
P_int,opt = √(P_evap × P_cond)
```

Or in terms of saturation temperatures (approximate):

```
T_int,opt = (T_evap + T_cond) / 2
```

**Performance comparison (R-404A, -20°F evap, 100°F cond):**

| Configuration | Compression Ratio | Discharge Temp (°F) | Work (Btu/lb) | COP_R |
|---------------|-------------------|---------------------|---------------|-------|
| Single-stage | 6.8 | 195 | 22.4 | 2.52 |
| Two-stage, no intercool | 6.8 (2.6 × 2.6) | 195 | 22.4 | 2.52 |
| Two-stage, flash intercool | 6.8 (2.6 × 2.6) | 145 | 20.1 | 2.81 |
| Two-stage, full intercool | 6.8 (2.6 × 2.6) | 120 | 18.9 | 2.99 |

**Work savings:** 15-20% compared to single-stage at high compression ratios.

### Intercooling Methods

**Flash intercooling (flash gas removal):**
- High-pressure liquid throttled to intermediate pressure
- Flash vapor separated and directed to second-stage suction
- Remaining liquid provides additional subcooling
- Most common method for refrigeration systems

**Direct contact intercooling:**
- Liquid refrigerant injected into discharge gas between stages
- Evaporation cools gas to saturation at intermediate pressure
- Simple, effective, minimal pressure drop
- Used in screw compressor systems

**Indirect intercooling (water or air-cooled):**
- External heat exchanger cools gas between stages
- Can achieve subcooled gas entering second stage
- Maximum thermodynamic benefit
- Added cost and complexity

## Economizer Cycles

The economizer cycle combines flash intercooling with vapor injection to increase capacity and efficiency in single or two-stage compressor systems.

### Flash Tank Economizer Configuration

**System components:**
1. Main expansion valve (high pressure to intermediate pressure)
2. Flash tank separator at intermediate pressure
3. Secondary expansion valve (intermediate to evaporator pressure)
4. Vapor injection port on compressor

**Mass flow analysis:**

```
ṁ_total = ṁ_evaporator + ṁ_economizer
ṁ_economizer = ṁ_total × (x_flash)
```

Where x_flash is flash gas quality at intermediate pressure.

**Capacity increase:**

```
Q_evap,econ = ṁ_evap(h₁ - h₄) = ṁ_total(1 - x_flash)(h₁ - h₄)
Q_evap,basic = ṁ_total(h₁ - h₃)

Capacity increase = [(1-x_flash)(h₁-h₄) - (h₁-h₃)] / (h₁-h₃) × 100%
```

**Performance example (R-134a, 0°F evap, 120°F cond):**

| Parameter | Single-Stage | Economizer | Improvement |
|-----------|-------------|------------|-------------|
| Refrigeration effect (Btu/lb) | 58.3 | 68.9 | +18.2% |
| Compression work (Btu/lb) | 16.8 | 17.2 | +2.4% |
| COP | 3.47 | 4.01 | +15.6% |
| Capacity (per lb/min condenser flow) | 58.3 | 62.1 | +6.5% |
| Flash gas at P_int (%) | - | 18.4 | - |

### Subcooler Economizer Configuration

Alternative arrangement using dedicated subcooler heat exchanger instead of flash tank:

**Advantages:**
- Precise control of subcooling degree
- Can achieve greater subcooling than flash economizer
- Better for systems with variable loads

**Disadvantages:**
- Higher pressure drop than flash tank
- More complex piping and controls
- Requires additional heat exchanger

### Economizer Selection Criteria

| Application | System Type | Expected COP Gain |
|-------------|-------------|-------------------|
| Low-temp refrigeration (-40 to 0°F) | Flash economizer | 15-25% |
| Medium-temp refrigeration (0 to 40°F) | Flash economizer | 8-15% |
| Air conditioning (40 to 50°F evap) | Subcooler economizer | 5-10% |
| Heat pump (winter heating) | Flash or subcooler | 10-18% |
| Screw compressor (any temp) | Liquid injection | 12-20% |

## Cascade Refrigeration Systems

Cascade systems employ two separate refrigeration cycles operating in series to achieve very low evaporating temperatures (-100°F to -250°F) not practical with single-stage systems.

### Cascade System Configuration

**Low-temperature circuit:**
- Evaporator at desired low temperature
- Condenser serving as cascade heat exchanger
- Refrigerant selected for low-temperature properties

**High-temperature circuit:**
- Evaporator is cascade heat exchanger
- Condenser rejecting heat to ambient
- Refrigerant selected for efficient heat rejection

### Refrigerant Pair Selection

Optimum refrigerant combinations for cascade systems:

| Application Range | Low-Stage Refrigerant | High-Stage Refrigerant | Cascade Temp (°F) |
|-------------------|----------------------|------------------------|-------------------|
| -40 to -80°F | R-404A, R-507A | R-404A, R-22 | -30 to -40 |
| -80 to -120°F | R-508B, R-23 | R-404A, R-507A | -50 to -60 |
| -120 to -160°F | R-23, R-13 | R-404A, R-508B | -70 to -80 |
| -160 to -250°F | R-14, R-508A | R-23, R-508B | -90 to -110 |

**Selection criteria:**
1. Normal boiling point of low-stage refrigerant below minimum evaporating temperature
2. Critical temperature of high-stage refrigerant well above condensing temperature
3. Compatible operating pressures (avoid excessive vacuum or pressure)
4. Minimal temperature difference at cascade heat exchanger (5-10°F)

### Cascade Heat Exchanger Analysis

The cascade condenser/evaporator operates with:

**Low-stage condensing temperature:** T_cascade + ΔT_approach (typically 5-10°F)
**High-stage evaporating temperature:** T_cascade

**Heat balance:**

```
Q_cascade = ṁ_low × (h₂,low - h₃,low) = ṁ_high × (h₁,high - h₄,high)
```

**Optimal cascade temperature:**

For minimum total compression work:

```
T_cascade,opt ≈ √(T_evap × T_cond)  [absolute temperatures]
```

More precisely, considering different refrigerants and efficiencies:

```
T_cascade,opt = (T_evap + α×T_cond) / (1 + α)
```

Where α accounts for refrigerant properties and compressor efficiencies (typically 1.2-1.5).

### Cascade System Performance

**Performance example:** -100°F evaporator, 100°F condenser

Low stage: R-508B (-100°F to -45°F cascade)
High stage: R-404A (-40°F cascade to 100°F)

| Parameter | Low Stage | High Stage | Combined |
|-----------|-----------|------------|----------|
| Evaporating pressure (psia) | 23.4 | 55.3 | - |
| Condensing pressure (psia) | 118.7 | 278.6 | - |
| Compression ratio | 5.07 | 5.04 | 25.5 (equivalent) |
| Discharge temperature (°F) | 85 | 145 | - |
| Compression work (Btu/lb) | 11.2 | 14.8 | - |
| Individual COP | 3.89 | 4.12 | - |
| **System COP** | - | - | **1.47** |

**Comparison to single-stage (theoretical):**
- Single-stage R-508B would require compression ratio of 11.9
- Discharge temperature would exceed 250°F
- COP would be approximately 1.1
- Cascade provides 34% COP improvement plus reliable operation

### Auto-Cascade Systems

Single refrigerant circuit using zeotropic mixture (e.g., R-508A, R-23/R-116) with rectifying column to separate components:
- High-boiling component condenses first (warm end)
- Low-boiling component evaporates last (cold end)
- Eliminates cascade heat exchanger
- Simplified design but less efficient than true cascade

## Cycle Modifications and Advanced Configurations

### Compound Compression Systems

Single refrigerant circuit with two compressor stages, but evaporators at both intermediate and low temperature levels.

**Applications:**
- Supermarket refrigeration (medium and low temp cases)
- Cold storage with multiple temperature zones
- Process cooling with varied temperature requirements

**Advantages over separate systems:**
- Reduced total compressor capacity (work shared)
- Lower condensing load
- Improved COP for medium-temp loads

**Mass flow relationship:**

```
ṁ_high-stage = ṁ_medium-temp + ṁ_low-temp
```

### Hot Gas Bypass Capacity Control

Diverts high-pressure discharge gas directly to evaporator inlet or compressor suction for capacity reduction.

**Methods:**

1. **Evaporator pressure regulator (EPR) bypass:** Gas to evaporator inlet
   - Maintains minimum evaporator pressure
   - Prevents coil icing
   - Capacity reduction: 0-100%

2. **Suction gas bypass:** Gas to suction line
   - Prevents compressor surge
   - Less efficient than unloading
   - Used for minimum load situations

**Efficiency impact:**

| Capacity (%) | Actual Load (%) | Power (%) | Wasted Energy (%) |
|--------------|----------------|-----------|-------------------|
| 100 | 100 | 100 | 0 |
| 75 | 75 | 85 | 10 |
| 50 | 50 | 70 | 20 |
| 25 | 25 | 60 | 35 |

Hot gas bypass is inefficient; use variable speed or digital scroll for better part-load performance.

### Liquid Overfeed Systems

Circulate excess liquid refrigerant through evaporator (2-4 times required for heat absorption) with separation vessel.

**Components:**
- Liquid overfeed pump or gravity circulation
- Separation vessel (accumulator)
- Liquid recirculation line

**Advantages:**
- Higher heat transfer coefficient (wetted surface)
- More uniform coil temperature
- Better oil return
- Reduced superheat requirement

**Applications:**
- Large industrial refrigeration (ammonia)
- Ice rinks
- Food processing facilities
- Cold storage warehouses

**Performance:** 5-15% higher evaporator capacity vs direct expansion at same temperature.

## Refrigerant Property Effects on Cycle Performance

### Critical Refrigerant Selection Parameters

| Refrigerant | Normal BP (°F) | Critical Temp (°F) | Latent Heat (Btu/lb) | Liquid Density (lb/ft³) | Vapor Density (lb/ft³) | ODP | GWP |
|-------------|----------------|--------------------|--------------------|----------------------|---------------------|-----|-----|
| R-22 | -41.4 | 205.1 | 100.5 | 74.4 | 0.368 | 0.055 | 1810 |
| R-134a | -15.1 | 213.9 | 93.2 | 75.3 | 0.461 | 0 | 1430 |
| R-404A | -51.0 | 161.9 | 71.8 | 69.5 | 0.398 | 0 | 3922 |
| R-407C | -43.6 | 187.2 | 91.4 | 70.8 | 0.411 | 0 | 1774 |
| R-410A | -61.9 | 158.3 | 105.7 | 69.0 | 0.429 | 0 | 2088 |
| R-32 | -61.1 | 172.0 | 154.3 | 60.4 | 0.298 | 0 | 675 |
| R-717 (NH₃) | -28.0 | 270.0 | 589.3 | 37.5 | 0.044 | 0 | <1 |

At 40°F saturated conditions (typical AC evaporator).

### Temperature Glide in Zeotropic Mixtures

Zeotropic refrigerant blends (e.g., R-404A, R-407C, R-410A) exhibit temperature glide during phase change.

**Temperature glide:** Difference between bubble point and dew point at constant pressure.

| Refrigerant | Composition | Glide at 1 atm (°F) | Impact |
|-------------|-------------|---------------------|--------|
| R-404A | R-125/143a/134a (44/52/4) | 0.9 | Minimal |
| R-407C | R-32/125/134a (23/25/52) | 10.0 | Significant |
| R-410A | R-32/125 (50/50) | 0.3 | Negligible |
| R-407A | R-32/125/134a (20/40/40) | 11.4 | High |

**Design implications:**
- Use dew point for evaporator temperature (end of evaporation)
- Use bubble point for condenser temperature (start of condensation)
- Counterflow heat exchangers perform better (temperature matching)
- Charge critically important (composition shift with leaks)

## Performance Optimization Strategies

### Operating Condition Optimization

**Maximize COP by:**

1. **Lower condensing temperature:**
   - Use largest economical condenser
   - Clean condenser surfaces regularly
   - Reduce condenser air/water temperature
   - Effect: 2-3% COP increase per 1°F reduction

2. **Higher evaporating temperature:**
   - Optimize air/water flow across evaporator
   - Minimize fouling and defrost frequency
   - Use lowest practical supply air/fluid temperature
   - Effect: 2-4% COP increase per 1°F increase

3. **Optimize superheat and subcooling:**
   - 5-10°F evaporator superheat (thermostatic expansion valve)
   - 10-15°F condenser subcooling
   - Minimize suction line heat gain
   - Effect: 3-5% COP improvement

4. **Reduce pressure drops:**
   - Properly size suction lines (ΔP < 2 psi, Δ < 1°F)
   - Clean filters and strainers
   - Minimize line length and fittings
   - Effect: 1-2% COP improvement per psi reduction

### Capacity Control Methods

Ranked by part-load efficiency (best to worst):

1. **Variable speed drive (VFD):**
   - Power ∝ Speed³ (affinity laws for centrifugal)
   - Power ∝ Speed for positive displacement (approximately)
   - 20-50% energy savings at part load

2. **Digital scroll modulation:**
   - 10-100% capacity in 10% steps
   - Maintains high efficiency at part load
   - No hot gas bypass losses

3. **Cylinder unloading (reciprocating):**
   - 25%, 50%, 75%, 100% capacity steps
   - Moderate efficiency degradation
   - Simple, reliable

4. **Slide valve (screw compressor):**
   - 10-100% continuous modulation
   - Efficiency decreases linearly with capacity
   - Good for most applications

5. **Hot gas bypass:**
   - Continuous capacity control
   - Poor part-load efficiency
   - Use only for minimum load protection

## References and Standards

**ASHRAE Handbook - Fundamentals (2021):**
- Chapter 1: Psychrometrics
- Chapter 2: Thermodynamics and Refrigeration Cycles
- Chapter 30: Thermophysical Properties of Refrigerants

**ASHRAE Handbook - Refrigeration (2022):**
- Chapter 1: Halocarbon Refrigeration Systems
- Chapter 2: Ammonia Refrigeration Systems
- Chapter 3: Carbon Dioxide Refrigeration Systems

**Industry Standards:**
- ANSI/ASHRAE Standard 15: Safety Standard for Refrigeration Systems
- ANSI/ASHRAE Standard 34: Designation and Safety Classification of Refrigerants
- ANSI/AHRI Standard 540: Performance Rating of Positive Displacement Refrigerant Compressors
- ISO 917: Testing of Refrigerant Compressors

**Design Tools:**
- NIST REFPROP: Reference Fluid Thermodynamic and Transport Properties Database
- Solkane (Honeywell): Refrigerant property calculator and cycle analysis
- ASHRAE Refrigerant Pressure-Temperature Charts (I-P and SI units)
