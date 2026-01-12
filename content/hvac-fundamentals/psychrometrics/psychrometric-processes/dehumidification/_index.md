---
title: "Dehumidification"
description: "Comprehensive analysis of HVAC dehumidification processes including cooling-based moisture removal, desiccant systems, latent heat calculations, sensible heat ratio optimization, and equipment selection criteria for precise humidity control"
weight: 5
---

## Fundamentals of Dehumidification

Dehumidification removes water vapor from air through two primary mechanisms: cooling the air below its dewpoint temperature (condensing dehumidification) or using hygroscopic materials to absorb moisture (desiccant dehumidification). The process reduces the humidity ratio (W) and can be represented on psychrometric charts as vertical or diagonal paths depending on the method employed.

**Key Parameters:**
- Initial and final humidity ratios (W₁, W₂) in lb_w/lb_da
- Dewpoint temperature (T_dp) in °F
- Latent cooling load (q_latent) in Btu/hr
- Sensible heat ratio (SHR) = q_sensible/(q_sensible + q_latent)
- Moisture removal rate in lb_w/hr or grains/hr

## Cooling-Based Dehumidification

### Process Description

Cooling coil dehumidification occurs when air temperature drops below its dewpoint, causing water vapor to condense on the coil surface. The process follows these stages:

1. **Pre-cooling:** Air cools sensibly until reaching dewpoint
2. **Condensation:** Air cools along saturation curve as moisture condenses
3. **Reheating (optional):** Air warms sensibly to desired supply temperature

The apparatus dewpoint (ADP) represents the effective surface temperature of the cooling coil. Actual air does not reach ADP due to bypass factor (BF), which accounts for air passing through without contacting coil surfaces.

**Bypass Factor Relationship:**
```
BF = (T_leaving - T_ADP)/(T_entering - T_ADP)
```

Typical bypass factors:
- 8-row coil: BF = 0.05-0.10
- 6-row coil: BF = 0.10-0.15
- 4-row coil: BF = 0.15-0.25

### Latent Heat Removal Calculations

The latent cooling load represents energy required to condense moisture:

```
q_latent = ṁ_air × h_fg × ΔW
q_latent = 4.5 × CFM × ΔW (Btu/hr, at standard conditions)
```

Where:
- h_fg = latent heat of vaporization ≈ 1060 Btu/lb_w at typical conditions
- ΔW = W₁ - W₂ (humidity ratio change)
- CFM = volumetric airflow rate

**Alternative formulation:**
```
q_latent = 0.68 × CFM × Δgr
```
Where Δgr = moisture removal in grains/lb_da (1 lb_w = 7000 grains)

### Sensible Heat Ratio

SHR quantifies the proportion of sensible to total cooling:

```
SHR = q_sensible/(q_sensible + q_latent)
SHR = 1.08 × CFM × ΔT/(1.08 × CFM × ΔT + 0.68 × CFM × Δgr)
```

Simplified:
```
SHR ≈ ΔT/(ΔT + 1900 × ΔW)
```

**Typical SHR Values by Application:**

| Application | SHR | Characteristics |
|-------------|-----|-----------------|
| Dry climates (offices) | 0.90-0.95 | High sensible, low latent |
| Standard comfort cooling | 0.70-0.80 | Balanced loads |
| Humid climates (southeast US) | 0.60-0.70 | High latent loads |
| Natatoriums | 0.40-0.60 | Dominant latent loads |
| Laboratory spaces | 0.50-0.70 | High ventilation, moisture sources |
| Supermarkets | 0.60-0.75 | Product moisture release |

### Coil Performance Parameters

**Dewpoint Approach:**
The difference between leaving air dewpoint and ADP indicates coil effectiveness:
- Tight approach (2-3°F): High efficiency, more coil rows
- Loose approach (5-8°F): Lower efficiency, fewer rows

**Coil Bypass Factor:**
Determined by fin spacing, face velocity, and number of rows:

| Coil Configuration | Face Velocity (fpm) | Typical BF |
|-------------------|---------------------|------------|
| 4-row, 8 fins/in | 400-500 | 0.15-0.20 |
| 6-row, 10 fins/in | 400-500 | 0.08-0.12 |
| 8-row, 12 fins/in | 400-500 | 0.04-0.08 |
| 4-row, 8 fins/in | 500-600 | 0.20-0.25 |
| 6-row, 10 fins/in | 500-600 | 0.12-0.16 |

Higher face velocities increase bypass and reduce dehumidification effectiveness.

### Cooling Coil Condensate Removal

Condensate generation rate:
```
ṁ_condensate = ṁ_air × (W₁ - W₂)
ṁ_condensate (lb/hr) = CFM × ρ_air × ΔW
ṁ_condensate (gal/hr) = CFM × 4.5 × ΔW/8.33
```

**Condensate Drain Sizing:**
- Minimum drain diameter: 3/4 inch for coils ≤5 tons
- 1 inch for 5-15 tons
- 1.5 inch for 15-30 tons
- Trap depth = static pressure + 1 inch minimum

## Desiccant Dehumidification

### Solid Desiccant Systems

Solid desiccant dehumidifiers use rotating wheels impregnated with hygroscopic materials (silica gel, molecular sieves, activated alumina). The wheel continuously rotates through process air and reactivation air streams.

**Process Description:**
1. **Adsorption sector (270° of wheel):** Humid process air contacts desiccant, which adsorbs moisture
2. **Reactivation sector (90° of wheel):** Hot regeneration air heats desiccant, releasing moisture to exhaust

**Performance Characteristics:**
- Moisture removal capacity: 20-200 grains/lb_da
- Reactivation temperature: 180-250°F typical, up to 350°F for deep drying
- Wheel rotation speed: 6-20 revolutions per hour
- Pressure drop: 0.5-1.5 in. w.g. per stream

**Moisture Removal vs. Regeneration Temperature:**

| Regeneration Temp (°F) | Moisture Removal (grains/lb_da) | Outlet Dewpoint Depression (°F) |
|------------------------|----------------------------------|----------------------------------|
| 120 | 25-40 | 5-10 |
| 150 | 50-80 | 15-25 |
| 180 | 80-120 | 25-40 |
| 210 | 100-150 | 40-60 |
| 240 | 120-180 | 60-80 |

### Liquid Desiccant Systems

Liquid desiccant dehumidifiers spray hygroscopic salt solutions (lithium chloride, lithium bromide, calcium chloride) through process air, absorbing moisture through direct contact.

**Operating Principles:**
- Solution concentration: 35-45% by weight
- Contact temperature affects capacity and regeneration energy
- Lower solution temperatures increase moisture removal
- Regeneration requires heating solution to release moisture

**Advantages over solid desiccant:**
- Continuous regeneration possible
- Lower regeneration temperatures (120-160°F)
- Can provide some sensible cooling
- Smaller footprint for large capacities

**Typical Performance:**

| Solution Type | Operating Concentration | Regeneration Temp (°F) | Moisture Removal (gr/lb_da) |
|---------------|------------------------|------------------------|------------------------------|
| LiCl | 38-42% | 130-160 | 60-120 |
| LiBr | 45-55% | 140-170 | 50-100 |
| CaCl₂ | 35-40% | 120-150 | 40-90 |

### Desiccant System Applications

**When desiccant systems are preferred:**
- Low dewpoint requirements (<40°F dewpoint)
- High latent loads with low sensible loads (SHR <0.60)
- Independent temperature and humidity control needed
- Regeneration heat available from waste sources
- Simultaneous humidification and dehumidification in different zones

**Energy considerations:**
Total system energy = fan energy + cooling energy + regeneration energy

Regeneration heat required:
```
q_regen = ṁ_air × ΔW × (h_fg + c_p,vapor × ΔT_regen)
q_regen ≈ 3000-4000 Btu/lb_water removed
```

This is significantly higher than cooling-based dehumidification (1060 Btu/lb_water), but advantageous when:
- Waste heat available for regeneration
- Avoiding overcooling and reheating penalties
- Very low dewpoints required

## Combined Dehumidification Systems

### Overcool-Reheat Systems

Traditional approach for high latent load applications:
1. Cool air below required supply temperature to achieve moisture removal
2. Reheat to desired supply temperature

**Energy penalty:**
```
Reheat energy = 1.08 × CFM × (T_supply - T_coil_leaving)
```

Effective when:
- Moderate dehumidification needs (dewpoint >50°F)
- Reheat energy available from hot gas, waste heat, or solar
- Simple control strategy desired

### Hybrid Desiccant-Cooling Systems

Combining cooling coils with desiccant wheels optimizes performance:
1. **Pre-cooling:** Sensible cooling coil reduces temperature
2. **Desiccant wheel:** Removes moisture without condensation
3. **Cooling coil:** Final sensible cooling to supply conditions

**Benefits:**
- Reduced regeneration temperature requirements
- Lower cooling coil temperature (no deep cooling needed)
- Independent temperature and humidity control
- Energy savings of 20-40% compared to overcool-reheat

### Dedicated Outdoor Air Systems (DOAS)

Separating ventilation air treatment from space conditioning allows optimized dehumidification:
- Deep dehumidification of outdoor air only
- Sensible-only cooling of recirculated space air
- Reduced total system airflow and fan energy
- Precise humidity control

**Typical DOAS design conditions:**
- Supply air: 50-55°F, 50-55°F dewpoint (neutral condition)
- Outdoor air: 100% of supply
- Energy recovery effectiveness: 60-80%

## Equipment Selection Criteria

### Cooling Coil Selection

**Key factors for dehumidification performance:**
1. **Number of rows:** More rows = lower bypass factor, better dehumidification
2. **Fin spacing:** 8-10 fins/inch for dehumidification (vs. 12-14 for sensible only)
3. **Face velocity:** 400-500 fpm maximum for effective moisture removal
4. **Coil temperature:** Supply chilled water at 40-45°F for deep dehumidification
5. **Circuiting:** Counterflow provides coldest surface at air inlet

**Dehumidification Capacity by Coil Configuration:**

| Rows | Fins/in | Face Vel (fpm) | ADP (°F) | Moisture Removal* (gr/lb_da) | Energy Required (Btu/lb_water) |
|------|---------|----------------|----------|------------------------------|----------------------------------|
| 4 | 8 | 450 | 52 | 30-40 | 1100-1150 |
| 6 | 10 | 450 | 48 | 50-65 | 1150-1200 |
| 8 | 12 | 450 | 45 | 70-90 | 1200-1250 |
| 6 | 10 | 500 | 50 | 45-58 | 1150-1200 |
| 8 | 12 | 500 | 47 | 65-82 | 1200-1250 |

*From entering air at 75°F DB, 50% RH (65 grains/lb_da)

### Desiccant Wheel Selection

**Selection parameters:**
1. **Wheel diameter:** 24-120 inches (larger = higher capacity)
2. **Desiccant type:**
   - Silica gel: General purpose, 40-140°F regeneration
   - Molecular sieve: Deep drying, 300-600°F regeneration
   - Activated alumina: Medium performance, corrosion resistant
3. **Purge sector:** 5-10% of wheel area prevents carryover
4. **Wheel depth:** 8-16 inches (deeper = more capacity, higher pressure drop)

**Capacity factors:**
- Process airflow (CFM)
- Inlet moisture content (grains/lb_da)
- Regeneration temperature (°F)
- Regeneration airflow ratio (typically 20-30% of process flow)

### System Sizing Methodology

**Step 1: Calculate moisture load**
```
ṁ_moisture = (Outdoor air CFM × W_outdoor + Internal gains) - (Space CFM × W_space)
```

**Step 2: Determine required moisture removal**
```
ΔW_required = ṁ_moisture / (Supply air CFM × ρ_air)
```

**Step 3: Select method based on criteria:**
- If dewpoint >50°F and SHR >0.65: Cooling coil
- If dewpoint 40-50°F or SHR 0.50-0.65: Overcool-reheat or hybrid
- If dewpoint <40°F or SHR <0.50: Desiccant system

**Step 4: Size equipment**
Apply appropriate safety factor:
- Cooling coils: 10-15% capacity margin
- Desiccant wheels: 20-25% capacity margin (degradation over time)

## Control Strategies

### Dewpoint Control

Direct measurement of dewpoint or humidity ratio provides accurate control:
- Dewpoint sensor in supply air duct
- Modulate cooling valve or desiccant regeneration temperature
- Control range: ±2°F dewpoint typical

### Relative Humidity Control

Indirect control using temperature and RH sensors:
- Space RH sensor with temperature compensation
- Setpoint range: 40-60% RH for comfort
- Deadband: ±5% to prevent hunting

### Sequencing Strategies

For systems with multiple dehumidification stages:
1. **Stage 1:** Increase cooling (reduce chilled water temperature)
2. **Stage 2:** Activate reheat or increase desiccant regeneration
3. **Stage 3:** Reduce supply air temperature (increase airflow)

## Performance Metrics

### Dehumidification Effectiveness

```
η_dehumid = (W_entering - W_leaving)/(W_entering - W_ADP)
```

Typical values:
- Well-designed cooling coil: 0.85-0.95
- Standard cooling coil: 0.75-0.85
- Desiccant wheel: 0.60-0.80

### Latent Cooling Efficiency

```
Latent EER = q_latent_removed / Power_input
```

Compare energy efficiency across technologies:
- Cooling coil only: 8-12 Btu/W·hr
- Overcool-reheat: 5-8 Btu/W·hr
- Desiccant with gas regeneration: 10-15 Btu/W·hr (including thermal COP)

### Moisture Removal Rate Verification

Field verification procedure:
1. Measure entering and leaving air conditions (DB, WB)
2. Calculate humidity ratios from psychrometric properties
3. Measure airflow (pitot traverse or flow station)
4. Calculate moisture removal: ṁ_water = CFM × 4.5 × ΔW
5. Collect and measure condensate over test period
6. Compare calculated vs. measured (should agree within ±10%)

## Special Considerations

### Cold Surface Dehumidification Limits

Minimum coil surface temperature limited by:
- Freeze protection: Coil face must remain >36°F with glycol or freeze protection controls
- Chiller operating range: Most chillers limited to 38-42°F supply
- For dewpoints <42°F, consider subcooled refrigerant coils or desiccant systems

### Carryover Prevention

Condensate entrainment occurs at high face velocities:
- Maximum face velocity: 500 fpm for horizontal coils
- 550-600 fpm for vertical coils with drains at both ends
- Install mist eliminators for velocities >500 fpm
- Slope horizontal coils 1/4 inch per foot toward drain

### Air Distribution Impacts

Supply air dewpoint affects space humidity control:
- Supply air dewpoint must be at least 5°F below space dewpoint for stable control
- Lower supply dewpoints improve dehumidification but increase energy use
- Typical supply conditions: 52-58°F, 50-55°F dewpoint for standard comfort

## Components

- Chemical Dehumidification
- Desiccant Dehumidification
- Refrigerant Dehumidification
