---
title: "Heat Rejection"
description: "Comprehensive analysis of heat rejection in refrigeration condensers including fundamentals, load calculations, COP relationships, condenser type comparisons, ambient effects, and optimization strategies for HVAC professionals"
weight: 4
---

## Heat Rejection Fundamentals

Heat rejection in refrigeration systems encompasses the total thermal energy discharged from the condenser to the ambient environment. This thermal load exceeds the evaporator capacity by the amount of compressor work input converted to heat.

### Energy Balance

The condenser must reject the sum of:
- Heat absorbed in the evaporator (Q_evap)
- Heat of compression (W_comp)
- Heat from auxiliary equipment (pumps, fans)
- Superheat removed in the desuperheating zone
- Latent heat removed during condensation
- Subcooling heat removed below saturation temperature

**Total heat rejection equation:**

```
Q_cond = Q_evap + W_comp
```

Or expressed in terms of refrigerant mass flow:

```
Q_cond = ṁ × (h_2 - h_4)
```

Where:
- Q_cond = condenser heat rejection rate (Btu/hr or kW)
- Q_evap = evaporator capacity (Btu/hr or kW)
- W_comp = compressor power input (Btu/hr or kW)
- ṁ = refrigerant mass flow rate (lbm/hr or kg/s)
- h_2 = enthalpy at compressor discharge (Btu/lbm or kJ/kg)
- h_4 = enthalpy at condenser exit (Btu/lbm or kJ/kg)

### Heat Rejection Ratio

The ratio of condenser heat rejection to evaporator capacity:

```
HRR = Q_cond / Q_evap = 1 + (W_comp / Q_evap) = 1 + (1 / COP)
```

Typical heat rejection ratios by application:

| Application | Evaporating Temp | Condensing Temp | Typical HRR |
|-------------|------------------|-----------------|-------------|
| Air Conditioning | 40°F to 50°F | 95°F to 115°F | 1.15 to 1.25 |
| Medium Temp Refrigeration | 0°F to 20°F | 90°F to 105°F | 1.25 to 1.35 |
| Low Temp Refrigeration | -20°F to -10°F | 90°F to 100°F | 1.40 to 1.60 |
| Ultra-Low Temp | -40°F to -30°F | 85°F to 95°F | 1.70 to 2.00 |

## Condenser Heat Load Calculations

### Design Heat Load

Calculate condenser capacity based on compressor performance and operating conditions.

**Step 1: Determine refrigerant state points**

Using refrigerant properties at design conditions:
- State 1: Evaporator outlet (superheated vapor)
- State 2: Compressor discharge (superheated vapor)
- State 3: Condenser mid-point (saturated vapor/liquid)
- State 4: Condenser outlet (subcooled liquid)

**Step 2: Calculate enthalpy changes**

For R-410A at typical air conditioning conditions:
- Evaporating: 45°F (h_1 = 162.5 Btu/lbm)
- Condensing: 105°F (h_3 = 50.2 Btu/lbm)
- Compressor discharge: 140°F (h_2 = 175.3 Btu/lbm)
- Subcooling: 10°F (h_4 = 46.8 Btu/lbm)

**Step 3: Apply energy balance**

```
Q_cond = ṁ × (h_2 - h_4)
       = ṁ × (175.3 - 46.8)
       = ṁ × 128.5 Btu/lbm
```

**Step 4: Determine mass flow rate**

From evaporator capacity:

```
ṁ = Q_evap / (h_1 - h_4)
```

For 36,000 Btu/hr (3 ton) evaporator capacity:

```
ṁ = 36,000 / (162.5 - 46.8)
  = 311 lbm/hr
```

**Step 5: Calculate condenser heat rejection**

```
Q_cond = 311 × 128.5
       = 39,964 Btu/hr
       ≈ 40,000 Btu/hr (3.33 tons)
```

Heat rejection ratio: 40,000 / 36,000 = 1.11

### Condenser Zone Heat Transfer

The condenser operates in three distinct zones with different heat transfer characteristics:

| Zone | Temperature Range | Heat Transfer | % of Total |
|------|-------------------|---------------|------------|
| Desuperheating | T_discharge to T_sat | Single-phase vapor cooling | 10-20% |
| Condensing | T_sat (constant) | Phase change (latent heat) | 70-85% |
| Subcooling | T_sat to T_outlet | Single-phase liquid cooling | 5-15% |

**Desuperheating heat removal:**

```
Q_desup = ṁ × c_p,vapor × (T_2 - T_sat)
```

**Condensing heat removal:**

```
Q_cond_latent = ṁ × h_fg
```

**Subcooling heat removal:**

```
Q_subcool = ṁ × c_p,liquid × (T_sat - T_4)
```

Where:
- c_p,vapor = specific heat of superheated vapor (Btu/lbm·°F)
- c_p,liquid = specific heat of subcooled liquid (Btu/lbm·°F)
- h_fg = latent heat of vaporization (Btu/lbm)
- T_sat = saturation temperature at condensing pressure (°F)

## COP Relationship to Condensing Temperature

System coefficient of performance directly correlates with condensing temperature. Lower condensing temperatures improve efficiency by reducing compression ratio.

### Carnot COP Relationship

Theoretical maximum efficiency:

```
COP_Carnot = T_evap / (T_cond - T_evap)
```

Where temperatures are absolute (°R or K).

**Example:** Refrigeration system
- T_evap = 20°F = 479.67°R
- T_cond = 100°F = 559.67°R

```
COP_Carnot = 479.67 / (559.67 - 479.67)
          = 479.67 / 80
          = 6.0
```

Actual COP typically 40-60% of Carnot COP due to real-world inefficiencies.

### Condensing Temperature Impact

**Effect of condensing temperature on actual COP:**

For R-404A refrigeration system at 0°F evaporating temperature:

| Condensing Temp (°F) | Compression Ratio | Discharge Temp (°F) | COP | % Change |
|----------------------|-------------------|---------------------|-----|----------|
| 80 | 3.2 | 110 | 2.85 | baseline |
| 90 | 3.7 | 125 | 2.55 | -10.5% |
| 100 | 4.3 | 140 | 2.28 | -20.0% |
| 110 | 4.9 | 155 | 2.05 | -28.1% |
| 120 | 5.6 | 170 | 1.85 | -35.1% |

**Key observation:** Each 10°F increase in condensing temperature reduces COP by approximately 8-10%.

### Energy Consumption Impact

Power consumption increases exponentially with condensing temperature:

```
W_comp ∝ (P_cond / P_evap)^((k-1)/k)
```

Where:
- k = ratio of specific heats (≈1.13 for refrigerants)
- P_cond = condensing pressure (absolute)
- P_evap = evaporating pressure (absolute)

**Practical impact on operating cost:**

For 100 ton refrigeration system operating 6,000 hours annually:
- Baseline: 95°F condensing, 150 kW
- High condensing: 105°F condensing, 172 kW

Annual energy increase:
```
ΔE = (172 - 150) kW × 6,000 hr = 132,000 kWh
```

At $0.12/kWh: $15,840 additional annual cost

### Optimization Strategy

Maintain lowest practical condensing temperature by:
- Maximizing condenser airflow (fan speed control)
- Ensuring adequate condenser surface area
- Regular coil cleaning
- Utilizing free cooling when available
- Implementing head pressure control in cold weather

## Air-Cooled vs Water-Cooled Comparison

Selection between air-cooled and water-cooled condensers involves trade-offs in performance, efficiency, cost, and site requirements.

### Performance Characteristics

| Parameter | Air-Cooled | Water-Cooled | Evaporative |
|-----------|------------|--------------|-------------|
| Condensing Temp (design) | Ambient +20-25°F | Water temp +10°F | Ambient WB +15-20°F |
| Typical summer condensing | 115-125°F | 95-105°F | 85-95°F |
| Approach to ambient | 20-25°F DB | 10-15°F to water | 15-20°F WB |
| COP (relative) | 1.0 (baseline) | 1.15-1.25 | 1.20-1.35 |
| Part-load efficiency | Good | Excellent | Very good |

### Air-Cooled Condensers

**Advantages:**
- No water consumption
- Lower installation cost
- Minimal maintenance
- No freeze protection in water systems
- No water treatment required
- Suitable for water-scarce regions
- No cooling tower or water-cooled equipment

**Disadvantages:**
- Higher condensing temperatures
- Lower efficiency (higher energy cost)
- Large footprint and weight
- Noise generation
- Performance degradation in high ambient
- Limited capacity in extreme heat
- Reduced equipment life due to higher pressures

**Heat transfer equation:**

```
Q = U × A × LMTD
```

Where:
- U = overall heat transfer coefficient: 8-15 Btu/hr·ft²·°F
- A = heat transfer surface area (ft²)
- LMTD = log mean temperature difference (°F)

**Typical design parameters:**
- Face velocity: 400-600 fpm
- Fin spacing: 10-16 fins per inch
- Tube arrangement: Staggered or in-line
- Refrigerant circuits: Multiple parallel paths
- Material: Copper tubes with aluminum fins

### Water-Cooled Condensers

**Advantages:**
- Lower condensing temperatures
- Higher COP (15-25% improvement)
- Smaller physical size
- Quieter operation
- Better capacity control
- Consistent performance
- Extended equipment life

**Disadvantages:**
- Water consumption (evaporation + blowdown)
- Cooling tower required
- Higher installation complexity
- Water treatment necessary
- Fouling potential
- Freeze protection needed
- Higher maintenance requirements
- Susceptible to water quality issues

**Shell-and-tube heat transfer:**

```
Q = U × A × LMTD

LMTD = (ΔT₁ - ΔT₂) / ln(ΔT₁/ΔT₂)
```

Where:
- U = 150-300 Btu/hr·ft²·°F (clean tubes)
- ΔT₁ = T_cond - T_water,in
- ΔT₂ = T_cond - T_water,out

**Typical design parameters:**
- Water velocity: 3-10 fps (optimal: 6-8 fps)
- Fouling factor: 0.00025-0.0005 hr·ft²·°F/Btu
- Temperature rise: 10-20°F
- Approach: 5-10°F
- Flow rate: 2.5-3.0 gpm per ton

**Water flow calculation:**

```
GPM = (Q_cond × 12) / (500 × ΔT_water)
```

For 100 ton system (Q_cond = 1,500,000 Btu/hr, ΔT = 10°F):

```
GPM = (1,500,000 × 12) / (500 × 10)
    = 300 gpm
```

### Evaporative Condensers

**Operating principle:** Combines water evaporation and air cooling for enhanced heat transfer.

**Advantages:**
- Lowest condensing temperatures
- Highest efficiency (20-35% better than air-cooled)
- Smaller footprint than air-cooled
- Less water use than cooling tower
- Compact design
- Good part-load performance

**Disadvantages:**
- Water consumption (though less than tower)
- Water treatment required
- Freeze protection necessary
- Plume potential
- Higher maintenance than air-cooled
- Legionella risk (requires protocols)
- Local codes may restrict use

**Heat transfer mechanisms:**

1. Evaporative cooling (dominant):
```
Q_evap = ṁ_water × h_fg,water
```

2. Sensible cooling:
```
Q_sens = ṁ_air × c_p,air × ΔT
```

**Typical performance:**
- Approach to wet bulb: 10-15°F
- Water flow: 1.5-2.0 gpm per ton
- Air velocity through media: 400-600 fpm
- Evaporation rate: 3-5% of circulation rate

### Economic Comparison

**Life-cycle cost analysis (100 ton system, 20 years, 4,000 hr/yr):**

| Cost Category | Air-Cooled | Water-Cooled | Evaporative |
|---------------|------------|--------------|-------------|
| Equipment cost | $45,000 | $65,000 | $55,000 |
| Installation cost | $8,000 | $25,000 | $12,000 |
| Annual energy cost | $28,800 | $24,000 | $22,500 |
| Annual water cost | $0 | $4,200 | $2,400 |
| Annual maintenance | $1,200 | $3,500 | $2,200 |
| 20-year LCC | $653,000 | $721,000 | $565,000 |

Assumptions: $0.12/kWh, $8/1000 gal water, 3% discount rate

## Ambient Temperature Effects

Ambient conditions significantly impact condenser performance, capacity, and efficiency across all condenser types.

### Air-Cooled Condenser Response

**Condensing temperature relationship:**

```
T_cond = T_ambient,DB + ΔT_approach
```

Where ΔT_approach typically ranges 20-30°F depending on:
- Condenser size (larger = smaller approach)
- Airflow rate (higher = smaller approach)
- Coil condition (fouling increases approach)

**Capacity variation with ambient temperature:**

For R-410A air conditioning system:

| Ambient Temp (°F) | Condensing Temp (°F) | System Capacity | Compressor Power | EER |
|-------------------|----------------------|-----------------|------------------|-----|
| 75 | 100 | 107% | 93% | 11.5 |
| 85 | 110 | 103% | 97% | 10.6 |
| 95 | 120 | 100% | 100% | 10.0 |
| 105 | 130 | 96% | 106% | 9.1 |
| 115 | 140 | 91% | 113% | 8.1 |

**Performance degradation in extreme heat:**
- Reduced cooling capacity when needed most
- Increased energy consumption
- Higher discharge temperatures
- Potential high-pressure cutout
- Accelerated oil breakdown
- Shortened equipment life

### Water-Cooled Condenser Response

Performance tied to cooling tower wet bulb temperature:

```
T_cond = T_WB + ΔT_tower_approach + ΔT_range + ΔT_condenser_approach
```

Typical values:
- Tower approach: 7-10°F
- Tower range: 10-15°F
- Condenser approach: 5-8°F

**Example at 78°F wet bulb:**

```
T_cond = 78 + 8 + 12 + 6 = 104°F
```

**Seasonal performance variation:**

| Season | Wet Bulb (°F) | Tower Water (°F) | Condensing (°F) | COP Multiplier |
|--------|---------------|------------------|-----------------|----------------|
| Winter | 35 | 45 | 55 | 1.35 |
| Spring | 55 | 65 | 75 | 1.20 |
| Summer | 75 | 85 | 95 | 1.00 |
| Fall | 60 | 70 | 80 | 1.15 |

### Evaporative Condenser Response

Governed by wet bulb temperature with superior performance:

```
T_cond = T_WB + 10 to 20°F
```

**Performance across ambient conditions:**

| Dry Bulb (°F) | Wet Bulb (°F) | Condensing (°F) | Advantage vs Air-Cooled |
|---------------|---------------|-----------------|-------------------------|
| 95 | 70 | 85 | 30°F lower |
| 100 | 75 | 90 | 30°F lower |
| 105 | 78 | 93 | 32°F lower |
| 110 | 80 | 95 | 35°F lower |

### High Ambient Operation Strategies

**Design considerations for hot climates:**

1. **Oversized condensers**
   - 115-125% of standard capacity
   - Reduces approach temperature
   - Improves efficiency
   - Provides capacity margin

2. **Variable speed condenser fans**
   - Modulate airflow to maintain target condensing pressure
   - Reduce energy at part load
   - Extend fan motor life
   - Reduce noise during cooler periods

3. **Precooling systems**
   - Evaporative precoolers for air-cooled units
   - 10-20°F reduction in entering air temperature
   - Water consumption: 2-4 gpm per 100 tons
   - Effectiveness: 70-85%

4. **Adiabatic cooling**
   - Intermittent water spray on coils
   - Lower water use than evaporative
   - Prevents scale buildup
   - 5-15°F temperature reduction

**Precooler effectiveness:**

```
Effectiveness = (T_DB,entering - T_DB,leaving) / (T_DB,entering - T_WB)
```

For 80% effectiveness at 105°F DB, 75°F WB:

```
T_leaving = 105 - 0.80 × (105 - 75) = 81°F
```

Condensing temperature reduction: 20-25°F

### Low Ambient Operation

Cold weather presents challenges maintaining adequate head pressure.

**Minimum condensing pressure requirements:**
- Ensure proper expansion valve operation
- Maintain adequate subcooling
- Prevent liquid flashing
- Support oil return

**Head pressure control methods:**

1. **Fan cycling**
   - Simple on/off control
   - Limited modulation
   - Pressure cycling

2. **Variable speed fans**
   - Continuous modulation
   - Stable pressure control
   - Energy savings

3. **Dampers**
   - Airflow restriction
   - Lower cost
   - Less efficient

4. **Flooded condenser**
   - Reduces active surface area
   - Maintains pressure
   - Requires receiver capacity

5. **Hot gas bypass**
   - Artificial loading
   - Energy penalty
   - Immediate response

## Equipment Sizing

Proper condenser sizing ensures adequate heat rejection under all operating conditions while balancing first cost and operating efficiency.

### Sizing Methodology

**Step 1: Determine design heat rejection**

```
Q_design = Q_evap × HRR × SF
```

Where:
- Q_evap = design evaporator capacity
- HRR = heat rejection ratio (1.15-1.50)
- SF = safety factor (1.05-1.15)

**Step 2: Establish design conditions**

Air-cooled:
- Ambient dry bulb: 95°F to 115°F (location-dependent)
- Target condensing: Ambient +20-25°F

Water-cooled:
- Entering water temp: 85°F (typical)
- Water temperature rise: 10°F
- Target condensing: 95-105°F

Evaporative:
- Ambient wet bulb: 75-78°F
- Target condensing: WB +15-20°F

**Step 3: Calculate required heat transfer area**

```
A = Q / (U × LMTD)
```

**Step 4: Select equipment from manufacturer data**

Match calculated capacity to available models considering:
- Available space
- Weight limitations
- Sound requirements
- Maintenance access
- Future expansion

### Air-Cooled Condenser Sizing

**Example: 50 ton refrigeration system**

Design parameters:
- Evaporator capacity: 50 tons = 600,000 Btu/hr
- HRR: 1.30 (medium temp application)
- Safety factor: 1.10
- Ambient design: 95°F
- Target condensing: 105°F

**Heat rejection calculation:**

```
Q_cond = 600,000 × 1.30 × 1.10 = 858,000 Btu/hr
```

**Surface area estimation:**

Assuming:
- U = 12 Btu/hr·ft²·°F
- Refrigerant temp: 105°F
- Air entering: 95°F
- Air leaving: 102°F (estimate)
- LMTD ≈ 6°F

```
A = 858,000 / (12 × 6) = 11,900 ft²
```

This is gross face area × rows deep.

**Fan power:**

Typical: 0.10-0.15 HP per ton of rejection
```
HP = 858,000 / 12,000 × 0.12 = 8.6 HP
```

Select (2) condenser units with 5 HP fans each.

### Water-Cooled Condenser Sizing

**Example: 100 ton chiller**

Design parameters:
- Chiller capacity: 100 tons = 1,200,000 Btu/hr
- HRR: 1.20
- Condensing temp: 105°F
- Entering water: 85°F
- Leaving water: 95°F

**Heat rejection:**

```
Q_cond = 1,200,000 × 1.20 = 1,440,000 Btu/hr
```

**Water flow rate:**

```
GPM = Q / (500 × ΔT) = 1,440,000 / (500 × 10) = 288 gpm
```

Use 300 gpm for safety margin.

**Heat transfer area:**

Shell-and-tube condenser:
- U = 200 Btu/hr·ft²·°F (clean, includes fouling factor)
- ΔT₁ = 105 - 85 = 20°F
- ΔT₂ = 105 - 95 = 10°F
- LMTD = (20 - 10) / ln(20/10) = 14.4°F

```
A = 1,440,000 / (200 × 14.4) = 500 ft²
```

**Condenser pressure drop:**

Target: 10-15 psi water side
- Affects pump selection
- Impacts operating cost
- Consider fouling allowance

### Oversizing Considerations

**Benefits of larger condensers:**
- Lower condensing temperatures
- Improved efficiency
- Greater capacity in high ambient
- Reduced compressor stress
- Extended equipment life
- Better part-load performance
- Fouling tolerance

**Economic analysis:**

Incremental cost vs. energy savings:

| Condenser Size | First Cost | Condensing Temp | Annual Energy | NPV (20 yr) |
|----------------|------------|-----------------|---------------|-------------|
| 100% (baseline) | $15,000 | 105°F | $24,000 | $15,000 |
| 115% | $17,250 | 100°F | $22,560 | $7,365 |
| 130% | $19,500 | 95°F | $21,360 | $2,880 |
| 150% | $22,500 | 90°F | $20,400 | -$3,960 |

**Optimal sizing:** 115-130% provides best life-cycle value

**Practical limits:**
- Minimum head pressure control required when oversized
- Diminishing returns beyond 130%
- Space constraints
- Weight considerations
- Installation complexity

## Energy Efficiency

Condenser optimization directly impacts system energy consumption and operating costs throughout equipment life.

### Efficiency Metrics

**Energy Efficiency Ratio (EER):**

```
EER = Q_evap / W_total (Btu/W·hr)
```

**Seasonal Energy Efficiency Ratio (SEER):**

Weighted average accounting for varying conditions:

```
SEER = Total cooling (Btu) / Total energy (W·hr)
```

**Coefficient of Performance (COP):**

```
COP = Q_evap / W_comp
```

**Integrated Energy Efficiency Ratio (IEER):**

For commercial equipment:

```
IEER = 0.02A + 0.617B + 0.238C + 0.125D
```

Where A, B, C, D are EER values at 100%, 75%, 50%, 25% load.

### Condenser Efficiency Factors

**Heat transfer effectiveness:**

```
ε = (T_ref,in - T_ref,out) / (T_ref,in - T_amb)
```

Higher effectiveness indicates better heat transfer.

**Approach temperature:**

Lower approach = higher efficiency

Air-cooled target: 15-20°F
Water-cooled target: 5-10°F
Evaporative target: 10-15°F to WB

**Fouling impact:**

Heat transfer degradation:

```
U_fouled = 1 / (1/U_clean + R_fouling)
```

Where R_fouling typical values:
- Air-cooled: 0.0005-0.001 hr·ft²·°F/Btu
- Water-cooled: 0.00025-0.0005 hr·ft²·°F/Btu

**Fouling energy penalty:**

20% reduction in U-value → 8-12% efficiency loss

### Optimization Strategies

**1. Condenser Temperature Reset**

Reduce condensing temperature when ambient permits:

**Reset schedule example:**

| Outdoor Temp (°F) | Condensing Setpoint (°F) | Energy Savings |
|-------------------|--------------------------|----------------|
| 95+ | 105 | baseline |
| 85-94 | 95 | 6-8% |
| 75-84 | 85 | 12-15% |
| 65-74 | 75 | 18-22% |
| <65 | 65 | 25-30% |

**2. Variable Speed Condenser Fans**

Fan power varies with cube of speed:

```
P₂ = P₁ × (N₂/N₁)³
```

At 75% speed: P₂ = 0.75³ × P₁ = 0.42 × P₁ (58% savings)

**Part-load fan energy reduction:**

| Load (%) | Fixed Speed | Variable Speed | Savings |
|----------|-------------|----------------|---------|
| 100 | 100% | 100% | 0% |
| 75 | 100% | 56% | 44% |
| 50 | 100% | 25% | 75% |
| 25 | 100% | 8% | 92% |

**3. Free Cooling / Economizer**

Utilize low ambient temperatures for direct heat rejection.

**Water-side economizer:**

When T_WB < 50-55°F, bypass chiller:
- Cooling tower provides chilled water directly
- Chiller remains off
- 90-95% energy reduction
- Requires plate-and-frame heat exchanger

**Air-side economizer:**

When T_DB < 55-60°F:
- Outside air provides cooling directly
- DX system remains off
- 80-90% energy reduction
- Common in data centers

**4. Condenser Maintenance**

**Cleaning frequency and impact:**

| Maintenance Level | Fouling Factor | Efficiency | Annual Cost Impact |
|-------------------|----------------|------------|--------------------|
| Poor (yearly) | 0.002 | 80% | +25% |
| Fair (semi-annual) | 0.001 | 90% | +10% |
| Good (quarterly) | 0.0005 | 95% | +5% |
| Excellent (monthly) | 0.0002 | 98% | baseline |

**Cleaning methods:**
- High-pressure water
- Chemical cleaning (water-cooled)
- Brush cleaning (tube-side)
- Fin combing (air-cooled)
- Coil coatings (corrosion protection)

**5. Subcooling Optimization**

Increase subcooling for improved efficiency:

**Subcooling benefits:**

| Subcooling (°F) | Refrigerating Effect | Net Capacity | COP Impact |
|-----------------|----------------------|--------------|------------|
| 0 | 100% | 100% | baseline |
| 5 | 103% | 102% | +2% |
| 10 | 106% | 104% | +4% |
| 15 | 109% | 106% | +6% |
| 20 | 112% | 107% | +7% |

Diminishing returns beyond 15-20°F subcooling.

**Mechanical subcooling methods:**
- Dedicated subcooler circuit
- Subcooling heat exchanger
- Suction-liquid heat exchanger

## ASHRAE Guidelines

ASHRAE provides comprehensive standards for condenser design, installation, and operation.

### Relevant Standards

**ASHRAE Standard 15-2019:** Safety Standard for Refrigeration Systems
- Machinery room requirements
- Ventilation for refrigerant leaks
- Pressure relief sizing
- Emergency procedures

**ASHRAE Standard 34-2019:** Designation and Safety Classification of Refrigerants
- Refrigerant properties
- Safety classifications (A1, A2L, etc.)
- Exposure limits
- Compatibility requirements

**ASHRAE Standard 90.1-2019:** Energy Standard for Buildings
- Minimum efficiency requirements
- Equipment performance tables
- Economizer requirements
- Control sequences

**ASHRAE Handbook - Refrigeration (2022):**
- Chapter 3: Refrigerant and heat transfer
- Chapter 4: Refrigeration system design
- Chapter 13: Condensers

### Design Conditions

**ASHRAE cooling design conditions (Chapter 14, Climatic Design Information):**

Selection criteria:
- 0.4% design conditions: Extreme design
- 1.0% design conditions: Standard design
- 2.0% design conditions: Economical design

**Example cities (1.0% cooling design):**

| Location | Dry Bulb (°F) | Wet Bulb (°F) | Recommended Condensing |
|----------|---------------|---------------|------------------------|
| Phoenix, AZ | 109 | 71 | 130°F (air) / 85°F (evap) |
| Houston, TX | 95 | 78 | 115°F (air) / 95°F (evap) |
| Chicago, IL | 91 | 75 | 110°F (air) / 90°F (evap) |
| Miami, FL | 91 | 79 | 110°F (air) / 95°F (evap) |
| Denver, CO | 93 | 63 | 110°F (air) / 78°F (evap) |

### Efficiency Requirements

**ASHRAE 90.1-2019 minimum efficiency (air-cooled condensing units):**

| Equipment Type | Size Category | Minimum EER |
|----------------|---------------|-------------|
| Air conditioners | <65,000 Btu/h | 11.0 |
| Air conditioners | ≥65,000 and <135,000 Btu/h | 10.8 |
| Air conditioners | ≥135,000 and <240,000 Btu/h | 10.0 |
| Air conditioners | ≥240,000 and <760,000 Btu/h | 9.5 |

**Water-cooled positive displacement chillers:**

| Size Category | Minimum COP (Path A) | Minimum IPLV |
|---------------|----------------------|--------------|
| <75 tons | 4.20 | 5.05 |
| ≥75 and <150 tons | 4.45 | 5.20 |
| ≥150 and <300 tons | 4.90 | 5.60 |
| ≥300 tons | 5.50 | 6.15 |

### Installation Requirements

**Clearances (ASHRAE Standard 15):**

Air-cooled condensers:
- Service side: 36 inches minimum
- Air inlet: 12 inches minimum
- Air discharge: 60 inches minimum (no obstructions)
- Between units: 12-24 inches

Water-cooled condensers:
- Tube removal: 1 × tube length
- Access for cleaning: 30 inches minimum
- Pressure relief discharge: Per Section 9

**Mounting:**
- Vibration isolation per ASHRAE Applications
- Structural support for weight and seismic
- Drainage for condensate (evaporative/air-cooled)
- Electrical disconnects within sight

### Maintenance Recommendations

**ASHRAE Handbook - Refrigeration, Chapter 3:**

**Monthly:**
- Visual inspection
- Check operating pressures
- Verify fan operation
- Monitor approach temperatures

**Quarterly:**
- Clean coils (air-cooled)
- Check water quality (water-cooled)
- Inspect for leaks
- Verify control sequences

**Semi-annually:**
- Detailed coil cleaning
- Water treatment analysis
- Performance testing
- Calibrate controls

**Annually:**
- Tube cleaning (water-cooled)
- Eddy current testing (tube integrity)
- Fan motor service
- Complete system analysis
- Efficiency verification

### Water Quality Standards

**ASHRAE Guideline 12-2020:** Minimizing the Risk of Legionellosis

**Cooling tower water chemistry targets:**

| Parameter | Acceptable Range | Target |
|-----------|------------------|--------|
| pH | 7.0-9.0 | 7.5-8.5 |
| Conductivity | <5,000 μS/cm | 1,000-3,000 μS/cm |
| Total Hardness | <800 ppm as CaCO₃ | 200-500 ppm |
| Alkalinity | 100-500 ppm | 150-300 ppm |
| Chlorides | <500 ppm | <250 ppm |
| Total Dissolved Solids | <3,500 ppm | 1,500-2,500 ppm |
| Cycles of Concentration | 2-6 | 3-4 |

**Condenser fouling factors (ASHRAE Handbook):**

Water-cooled condensers:
- City water: 0.00025 hr·ft²·°F/Btu
- Cooling tower: 0.0005 hr·ft²·°F/Btu
- Treated water: 0.0003 hr·ft²·°F/Btu
- River water: 0.001-0.002 hr·ft²·°F/Btu

## Conclusion

Heat rejection optimization represents one of the most effective strategies for improving refrigeration system efficiency and reducing operating costs. Understanding the fundamental relationships between condenser design, operating conditions, and system performance enables informed decisions regarding equipment selection, installation configuration, and operational control strategies.

Key principles:
- Lower condensing temperature directly improves COP and reduces energy consumption
- Each 10°F reduction in condensing temperature typically improves efficiency by 8-10%
- Proper condenser sizing (115-130% of minimum) provides optimal life-cycle value
- Regular maintenance preserves heat transfer effectiveness and prevents efficiency degradation
- Ambient conditions dictate maximum achievable performance; design for local climate
- Water-cooled and evaporative systems offer superior efficiency but require water management
- Variable speed fan control and condensing temperature reset provide significant energy savings
- ASHRAE standards establish minimum performance requirements and best practices

Comprehensive heat rejection analysis during design, combined with ongoing optimization during operation, maximizes system efficiency, reduces environmental impact, and minimizes life-cycle costs.
