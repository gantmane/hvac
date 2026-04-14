---
title: "Contact Freezing Principles"
aliases: ["Contact Freezing Principles"]
description: "Comprehensive analysis of conduction-based heat transfer in plate freezers, including contact resistance, pressure application effects, heat transfer coefficients, and freezing time calculations for flat food products"
weight: 1
---

## Fundamental Heat Transfer Mechanism

Contact freezing in plate freezers represents the most efficient commercial freezing method for flat or uniformly shaped food products. The process relies on direct conduction heat transfer between refrigerated metal plates and the product surface, eliminating the thermal resistance of convective boundary layers inherent in air blast freezing.

### Conduction Heat Transfer Dominance

The heat transfer mechanism in plate freezers is fundamentally different from air blast or immersion freezing systems. Conduction through direct metal-to-product contact provides heat transfer coefficients 10 to 50 times higher than forced air convection.

**Heat transfer modes comparison:**

| Freezing Method | Heat Transfer Coefficient | Primary Mechanism |
|----------------|--------------------------|-------------------|
| Plate Contact (good) | 200-400 W/m²·K | Conduction through contact |
| Plate Contact (poor) | 50-150 W/m²·K | Conduction with air gaps |
| Air Blast Freezing | 15-50 W/m²·K | Forced convection |
| Immersion Freezing | 100-300 W/m²·K | Convection in liquid |
| Cryogenic Freezing | 200-500 W/m²·K | Boiling heat transfer |

The fundamental heat transfer equation for conduction through the product is:

```
q = k·A·(T₁ - T₂)/L
```

Where:
- q = heat transfer rate (W)
- k = thermal conductivity of product (W/m·K)
- A = contact surface area (m²)
- T₁ = surface temperature (°C)
- T₂ = center temperature (°C)
- L = product thickness (m)

### Overall Heat Transfer in Plate Freezers

The overall heat transfer process involves multiple thermal resistances in series:

```
1/U = 1/h_plate + L_product/k_product + 1/h_contact + R_package
```

Where:
- U = overall heat transfer coefficient (W/m²·K)
- h_plate = plate-side heat transfer coefficient (W/m²·K)
- L_product = product thickness (m)
- k_product = product thermal conductivity (W/m·K)
- h_contact = contact heat transfer coefficient (W/m²·K)
- R_package = package thermal resistance (m²·K/W)

## Contact Resistance Factors

Contact resistance between the refrigerated plate and product surface represents the most critical factor affecting plate freezer performance. Perfect contact is impossible to achieve in practice due to surface irregularities, air entrapment, and product geometry variations.

### Interface Thermal Resistance

The contact interface creates a thermal resistance that can dominate the overall heat transfer process. This resistance depends on:

**Surface roughness effects:**
- Microscopic air gaps between plate and product
- Effective contact area typically 20-60% of apparent area
- Surface finish of plates (smoother plates provide better contact)
- Product surface irregularities and texture

**Thermal contact conductance:**

```
h_contact = k_fluid/(δ + ε·(Ra_plate + Ra_product))
```

Where:
- h_contact = contact conductance (W/m²·K)
- k_fluid = thermal conductivity of interstitial fluid (air or liquid) (W/m·K)
- δ = average gap thickness (m)
- ε = gap enhancement factor (dimensionless)
- Ra_plate = plate surface roughness (m)
- Ra_product = product surface roughness (m)

### Contact Resistance Magnitude

Typical contact resistance values for various conditions:

| Contact Condition | Contact Conductance | Contact Resistance |
|------------------|--------------------|--------------------|
| Excellent (with pressure, moisture) | 800-2000 W/m²·K | 0.0005-0.00125 m²·K/W |
| Good (pressure, dry surface) | 400-800 W/m²·K | 0.00125-0.0025 m²·K/W |
| Fair (light pressure, dry) | 200-400 W/m²·K | 0.0025-0.005 m²·K/W |
| Poor (no pressure) | 50-150 W/m²·K | 0.0067-0.02 m²·K/W |

The contact resistance can represent 40-70% of total thermal resistance in poorly designed systems, but only 10-20% in well-designed systems with proper pressure application.

### Air Gap Effects

Air trapped between plate and product creates significant thermal resistance due to air's low thermal conductivity (0.024 W/m·K at 0°C). Even microscopic air gaps dramatically reduce heat transfer:

**Air gap thermal resistance:**

```
R_gap = L_gap/k_air
```

For a 0.1 mm air gap:
```
R_gap = 0.0001 m / 0.024 W/m·K = 0.00417 m²·K/W
```

This single 0.1 mm air gap creates more thermal resistance than 25 mm of frozen fish (k ≈ 1.5 W/m·K).

## Pressure Application Effects

Hydraulic pressure application is essential for minimizing contact resistance and maximizing heat transfer rates in plate freezers. Pressure serves multiple functions in the freezing process.

### Pressure Requirements

Typical pressure applications for plate freezers:

| Product Type | Applied Pressure | Purpose |
|-------------|-----------------|---------|
| Fish blocks | 140-200 kPa | Consolidate pieces, eliminate voids |
| Fish fillets (packaged) | 70-140 kPa | Improve contact, avoid damage |
| Meat patties | 50-100 kPa | Maintain shape, good contact |
| Prepared meals | 35-70 kPa | Prevent crushing, adequate contact |
| Bakery products | 20-50 kPa | Minimize deformation |

### Pressure Effects on Contact Conductance

Pressure application improves contact conductance by:

1. **Reducing air gaps** - Forces product surface closer to plate
2. **Increasing effective contact area** - Deforms surface asperities
3. **Eliminating package voids** - Compresses packaging against product
4. **Maintaining contact during freezing** - Compensates for product shrinkage

**Pressure-conductance relationship (empirical):**

```
h_contact = h_0 + α·P^β
```

Where:
- h_contact = contact conductance at pressure P (W/m²·K)
- h_0 = zero-pressure conductance (W/m²·K)
- P = applied pressure (kPa)
- α, β = empirical constants (product-specific)

Typical values: α = 2-5, β = 0.3-0.5

### Hydraulic System Requirements

The hydraulic system must provide:

**Pressure generation:**
- Hydraulic pump capacity: 5-15 L/min per freezer station
- System pressure: 3-10 MPa (30-100 bar)
- Pressure reduction valves to control plate pressure
- Accumulator for pressure stability

**Force distribution:**
- Uniform pressure across entire plate surface
- Compensation for plate deflection under load
- Plate stiffness to prevent excessive bending
- Multiple pressure zones for varying product thickness

**Calculation of hydraulic force:**

```
F_hydraulic = P_plate × A_plate
```

For a 1.0 m × 0.8 m plate at 100 kPa:
```
F = 100,000 Pa × 0.8 m² = 80,000 N = 8,000 kgf
```

### Pressure Application Control

Proper pressure control requires:

- Initial high pressure (2-5 minutes) to establish contact
- Reduced holding pressure during freezing to prevent damage
- Pressure release timing synchronized with freezing completion
- Pressure sensors to verify adequate force application
- Safety interlocks to prevent excessive pressure

## Plate Surface Temperature Requirements

The refrigerated plate surface temperature determines the temperature driving force for heat transfer and directly affects freezing rate and product quality.

### Temperature Range Selection

Typical plate surface temperatures for various applications:

| Product Type | Plate Temperature | Considerations |
|-------------|------------------|----------------|
| Fish blocks | -35 to -40°C | Fast freezing, minimize drip loss |
| Shrimp | -30 to -35°C | Prevent surface dehydration |
| Meat products | -30 to -35°C | Balance speed and quality |
| Prepared meals | -25 to -30°C | Prevent texture damage |
| Ice cream products | -35 to -42°C | Maintain structure |

### Temperature Distribution

Plate surface temperature uniformity is critical for consistent product quality:

**Temperature variation limits:**
- Within single plate: ±2°C maximum
- Between plates in stack: ±3°C maximum
- Across refrigeration system: ±4°C maximum

**Factors affecting temperature uniformity:**

1. **Refrigerant distribution** - Proper header design, adequate refrigerant velocity
2. **Plate design** - Internal channel configuration, thermal mass
3. **Refrigeration load** - Balanced product loading across all plates
4. **Defrost cycles** - Timing to minimize temperature cycling
5. **Ambient conditions** - Insulation, room temperature control

### Temperature Driving Force

The temperature difference between plate surface and product determines heat transfer rate:

```
q = U·A·LMTD
```

Where LMTD (Log Mean Temperature Difference) for freezing:

```
LMTD = (ΔT_initial - ΔT_final) / ln(ΔT_initial/ΔT_final)
```

For typical freezing operation:
- T_plate = -35°C
- T_initial = +5°C (unfrozen product surface)
- T_final = -18°C (frozen product center)
- Initial ΔT = 5 - (-35) = 40°C
- Final ΔT = -18 - (-35) = 17°C

```
LMTD = (40 - 17) / ln(40/17) = 23 / 0.857 = 26.8°C
```

### Refrigeration System Requirements

To maintain plate surface temperature:

**Evaporator design:**
- Direct expansion (DX) or liquid overfeed configuration
- Refrigerant: Ammonia (R-717) or R-404A typical
- Evaporating temperature: 5-8°C below plate temperature
- Heat flux through plates: 5-15 kW/m²

**System capacity calculation:**

```
Q_refrigeration = n_plates × A_plate × q_flux × load_factor
```

For 20 plates, 0.8 m² each, 10 kW/m² flux, 0.7 load factor:
```
Q = 20 × 0.8 × 10 × 0.7 = 112 kW refrigeration capacity
```

## Product Thickness Considerations

Product thickness represents the most significant factor determining freezing time in plate freezers. The relationship is approximately quadratic due to the nature of heat conduction.

### Thickness Limitations

Practical thickness ranges for plate freezing:

| Product Form | Minimum Thickness | Maximum Thickness | Optimal Range |
|-------------|------------------|-------------------|---------------|
| Fish blocks | 50 mm | 100 mm | 60-75 mm |
| Fish fillets | 15 mm | 40 mm | 20-30 mm |
| Meat patties | 10 mm | 25 mm | 12-20 mm |
| Vegetable blocks | 30 mm | 75 mm | 40-60 mm |
| Prepared meals | 20 mm | 50 mm | 25-40 mm |

### Thickness Effect on Freezing Time

Plank's equation demonstrates the quadratic relationship between thickness and freezing time:

```
t_f = (ρ·ΔH_f)/(T_f - T_plate) × (P·a/(h) + R·a²/(k))
```

Where:
- t_f = freezing time (s)
- ρ = product density (kg/m³)
- ΔH_f = latent heat of fusion (J/kg)
- T_f = freezing point (°C)
- T_plate = plate temperature (°C)
- P, R = shape factors (1/2, 1/8 for infinite slab)
- a = thickness (m)
- h = surface heat transfer coefficient (W/m²·K)
- k = thermal conductivity of frozen product (W/m·K)

**Simplified form for plate freezing (bilateral contact):**

```
t_f = (ρ·ΔH_f·a²)/(8·k·(T_f - T_plate)) + (ρ·ΔH_f·a)/(2·h·(T_f - T_plate))
```

### Thickness Uniformity Requirements

Non-uniform product thickness creates several problems:

**Issues with thickness variation:**
- Thinner sections over-freeze while thick sections remain warm
- Ice crystal size variation affects texture quality
- Potential for thermal stress cracking
- Inefficient use of freezer capacity
- Difficult to optimize cycle time

**Acceptable thickness variation:**
- ±10% maximum for quality products
- ±15% acceptable for commodity products
- ±5% required for premium applications

### Thickness Optimization

Optimal thickness balances multiple factors:

1. **Freezing time** - Thinner products freeze faster
2. **Product yield** - Thicker blocks maximize weight per package
3. **Heat transfer efficiency** - Moderate thickness optimizes contact
4. **Handling characteristics** - Sufficient thickness for structural integrity
5. **Storage efficiency** - Standard dimensions for palletization

## Heat Transfer Calculations

Detailed heat transfer analysis requires consideration of transient conduction through the product with phase change.

### Thermal Properties of Food Products

Critical thermal properties for heat transfer calculations:

| Product | ρ (kg/m³) | k_unfrozen (W/m·K) | k_frozen (W/m·K) | c_p unfrozen (kJ/kg·K) | c_p frozen (kJ/kg·K) | Water Content (%) |
|---------|-----------|-------------------|-----------------|----------------------|-------------------|------------------|
| Lean fish | 1050 | 0.50 | 1.60 | 3.85 | 1.90 | 80 |
| Fatty fish | 1020 | 0.45 | 1.40 | 3.40 | 1.85 | 68 |
| Beef | 1070 | 0.48 | 1.50 | 3.50 | 1.85 | 75 |
| Pork | 1050 | 0.46 | 1.45 | 3.30 | 1.80 | 72 |
| Vegetables | 1040 | 0.55 | 1.80 | 3.95 | 1.95 | 88 |
| Bread | 420 | 0.25 | 0.60 | 2.60 | 1.40 | 35 |

### Effective Heat Removed

Total heat that must be removed during freezing:

```
Q_total = Q_sensible_1 + Q_latent + Q_sensible_2
```

**Component calculations:**

```
Q_sensible_1 = m·c_p,unfrozen·(T_initial - T_freezing)
Q_latent = m·ΔH_f
Q_sensible_2 = m·c_p,frozen·(T_freezing - T_final)
```

Where:
- m = product mass (kg)
- ΔH_f = latent heat (typically 0.8 × water fraction × 334 kJ/kg)

**Example calculation for 50 kg fish block:**
- Initial temperature: +5°C
- Freezing point: -2°C
- Final temperature: -18°C
- Water content: 80%

```
Q_sensible_1 = 50 × 3.85 × (5 - (-2)) = 1,348 kJ
Q_latent = 50 × 0.8 × 334 = 13,360 kJ
Q_sensible_2 = 50 × 1.90 × (-2 - (-18)) = 1,520 kJ
Q_total = 1,348 + 13,360 + 1,520 = 16,228 kJ = 16.2 MJ
```

### Heat Transfer Rate

The instantaneous heat transfer rate varies throughout the freezing process:

```
q(t) = U(t)·A·(T_plate - T_avg(t))
```

Where U(t) and T_avg(t) vary as freezing progresses.

**Average heat transfer rate:**

```
q_avg = Q_total / t_f
```

Using example above with 2.5 hour freezing time:
```
q_avg = 16,228 kJ / (2.5 × 3600 s) = 1.80 kW
```

For contact area of 0.8 m² (both sides):
```
q_flux = 1.80 kW / 0.8 m² = 2.25 kW/m²
```

### Finite Difference Numerical Solution

For precise freezing time prediction, numerical methods are required:

**Discretization of product thickness:**
- Divide thickness into n nodes (typically 20-50)
- Apply energy balance at each node
- Account for phase change with enthalpy method
- Solve time-stepping algorithm until center reaches target temperature

**Energy balance at internal node i:**

```
ρ·Δx·(H_i^(t+Δt) - H_i^t)/Δt = k·((T_(i+1) - T_i)/Δx - (T_i - T_(i-1))/Δx)
```

Where:
- H = enthalpy (J/kg)
- Δx = node spacing (m)
- Δt = time step (s)
- Superscripts indicate time level

## Freezing Time Equations

Several analytical and empirical equations exist for estimating freezing time in plate freezers.

### Plank's Equation (Classical)

The fundamental equation for freezing time prediction:

```
t_f = (ρ·λ)/(T_f - T_m) × (P·a/h + R·a²/k)
```

Shape factors for common geometries:

| Geometry | P | R |
|----------|---|---|
| Infinite slab (plate freezing) | 1/2 | 1/8 |
| Infinite cylinder | 1/4 | 1/16 |
| Sphere | 1/6 | 1/24 |

**Limitations of Plank's equation:**
- Assumes constant thermal properties
- Neglects precooling above freezing point
- Neglects subcooling below freezing point
- Assumes single freezing point (no freezing range)
- Most accurate when precooling and subcooling are small relative to latent heat

### Modified Plank's Equation

Accounting for sensible heat removal:

```
t_f = (ΔH_eff)/(T_f - T_plate) × (P·a/h + R·a²/k)
```

Where effective enthalpy change:

```
ΔH_eff = c_p,unfrozen·(T_initial - T_f) + λ + c_p,frozen·(T_f - T_final)
```

### Pham's Method

More accurate method accounting for temperature range:

```
t_f = ΔH·ΔT₁/(T_f - T_plate)² × (P·a/h + R·a²/k)
```

Where:
```
ΔH = c_p,unfrozen·(T_initial - T_f) + λ + c_p,frozen·(T_f - T_final)
ΔT₁ = T_initial - T_plate
```

This method provides 10-15% better accuracy than classical Plank's equation.

### Practical Freezing Time Examples

**Example 1: Fish block in plate freezer**

Given:
- Thickness: 60 mm (0.06 m)
- Initial temperature: +5°C
- Final center temperature: -18°C
- Plate temperature: -35°C
- Freezing point: -2°C
- Density: 1050 kg/m³
- Thermal conductivity (frozen): 1.6 W/m·K
- Contact heat transfer coefficient: 300 W/m²·K
- Latent heat: 267 kJ/kg (80% water content)

Using modified Plank's equation:
```
ΔH_eff = 3.85×7 + 267 + 1.90×16 = 27 + 267 + 30 = 324 kJ/kg

t_f = (1050 × 324,000)/(−2 − (−35)) × ((1/2)×0.06/300 + (1/8)×0.06²/1.6)

t_f = (340,200,000)/33 × (0.0001 + 0.00028)

t_f = 10,309,091 × 0.00038 = 3,917 seconds = 1.09 hours
```

**Example 2: Meat patty**

Given:
- Thickness: 15 mm
- Initial: +8°C, Final: -18°C, Plate: -32°C
- h = 250 W/m²·K, k = 1.5 W/m·K
- ΔH_eff = 280 kJ/kg, ρ = 1070 kg/m³

```
t_f = (1070 × 280,000)/30 × (0.5×0.015/250 + 0.125×0.015²/1.5)
t_f = 9,986,667 × (0.00003 + 0.000019) = 489 seconds = 8.2 minutes
```

### Factors Affecting Actual Freezing Time

Actual freezing time in production differs from calculated values due to:

| Factor | Effect on Freezing Time | Typical Magnitude |
|--------|------------------------|-------------------|
| Loading/unloading time | Increases cycle time | +5-15 minutes |
| Poor contact | Increases freezing time | +15-40% |
| Thickness variation | Requires extended time | +10-25% |
| Inadequate pressure | Increases time significantly | +30-60% |
| Plate temperature variation | Variable freezing times | ±10-20% |
| Package thermal resistance | Increases time moderately | +10-30% |

## Equipment Specifications

Plate freezer equipment must meet specific design criteria to achieve proper contact freezing performance.

### Plate Design Requirements

**Material specifications:**
- Material: Aluminum alloy (5000 or 6000 series) or stainless steel
- Plate thickness: 15-25 mm typical
- Internal channel depth: 8-15 mm
- Channel spacing: 40-80 mm
- Surface finish: Ra < 3.2 μm for good contact

**Structural requirements:**
- Maximum deflection under pressure: 2-3 mm across span
- Flatness tolerance: ±1 mm over plate area
- Weld integrity for pressure containment
- Thermal expansion compensation

### Refrigerant Distribution

**Channel configurations:**

| Configuration | Flow Pattern | Advantages | Disadvantages |
|--------------|--------------|------------|---------------|
| Parallel channels | Side-to-side | Even distribution | Requires precise feeding |
| Serpentine | Multiple passes | Simple feed | Pressure drop, temperature gradient |
| Header-lateral | Central distribution | Uniform temperature | Complex fabrication |

**Design parameters:**
- Refrigerant velocity: 3-8 m/s for ammonia, 8-15 m/s for HFCs
- Pressure drop: < 50 kPa through plate
- Liquid overfeed ratio: 2-4:1 for recirculation systems
- Direct expansion superheat: 3-8°C at plate outlet

### Station Configuration

**Vertical plate freezers:**
- 10-40 plates per station typical
- Plate spacing: 50-150 mm depending on product
- Hydraulic closure: top-down or bottom-up
- Footprint: 2-4 m² per station
- Height: 2-5 m for standard units

**Horizontal plate freezers:**
- 3-10 plates per station
- Suitable for larger, heavier products
- Easier loading/unloading
- Greater floor space requirement
- Better accessibility for maintenance

### Automation and Control

**Required control systems:**

1. **Temperature control**
   - Plate temperature monitoring (each plate or zone)
   - Refrigerant temperature and pressure control
   - Alarm limits: ±3°C from setpoint

2. **Pressure control**
   - Hydraulic pressure regulation
   - Individual plate pressure monitoring
   - Pressure application sequences

3. **Cycle timing**
   - Programmable cycle times by product type
   - Automatic loading/unloading sequences
   - Integration with conveyor systems

4. **Safety interlocks**
   - Emergency stop circuits
   - Pressure relief systems
   - Refrigerant leak detection
   - Access door interlocks

### Performance Specifications

Typical plate freezer performance parameters:

| Parameter | Value Range | Units |
|-----------|------------|-------|
| Freezing capacity | 500-5000 | kg/hour per station |
| Energy consumption | 150-250 | kWh/tonne product |
| Specific refrigeration load | 4-8 | kW per m² plate area |
| Water consumption (defrost) | 2-5 | L per cycle |
| Compressed air requirement | 50-150 | L/min at 6 bar |
| Hydraulic fluid volume | 100-500 | L per station |

## Quality Implications

Contact freezing in plate freezers produces superior product quality when properly executed.

### Ice Crystal Formation

Freezing rate directly affects ice crystal size and distribution:

**Ice crystal size vs. freezing rate:**
- Slow freezing (>4 hours): Large crystals (100-150 μm), significant cell damage
- Moderate freezing (1-4 hours): Medium crystals (50-100 μm), acceptable quality
- Fast freezing (<1 hour): Small crystals (20-50 μm), minimal cell damage
- Ultra-fast (<15 minutes): Very small crystals (<20 μm), optimal quality

Plate freezing typically achieves moderate to fast freezing rates, producing acceptable to excellent quality.

### Drip Loss Reduction

Proper contact freezing minimizes thaw drip loss:

**Factors affecting drip loss:**
- Freezing rate: Faster freezing reduces cellular damage (1-3% drip loss vs. 5-8% for slow freezing)
- Ice crystal location: Intracellular vs. extracellular ice formation
- Temperature cycling: Minimize temperature fluctuations during storage
- Thawing method: Controlled thawing maintains quality

### Product Appearance

Contact freezing affects visual quality:

**Surface characteristics:**
- Uniform frozen appearance without surface dehydration
- Minimal surface discoloration due to rapid freezing
- Potential for plate marks if pressure excessive
- Possible surface moisture if condensation occurs before contact

### Texture and Structure Preservation

High heat transfer rates preserve texture:

- Protein structure maintained with minimal denaturation
- Cell wall integrity preserved with small ice crystals
- Fat crystallization controlled for proper mouthfeel
- Starch retrogradation minimized in bakery products

### Microbial and Enzymatic Activity

Rapid freezing improves food safety and shelf life:

- Fast passage through critical temperature zone (0 to -5°C)
- Reduced time for microbial growth during freezing
- Enzymatic reactions halted quickly
- Extended shelf life: 6-24 months depending on product

### Quality Control Requirements

To maintain product quality in plate freezing operations:

1. **Temperature monitoring** - Verify plate temperatures every shift
2. **Freezing time validation** - Test center temperature of products
3. **Pressure verification** - Check hydraulic pressure application
4. **Thickness control** - Measure and control product uniformity
5. **Loading consistency** - Standard operating procedures for product placement
6. **Maintenance schedules** - Regular cleaning and calibration

### Comparison to Other Freezing Methods

Quality characteristics comparison:

| Quality Factor | Plate Freezing | Air Blast | Immersion | Cryogenic |
|----------------|---------------|-----------|-----------|-----------|
| Ice crystal size | Small-Medium | Medium-Large | Small | Very Small |
| Drip loss | 1-3% | 3-6% | 2-4% | 1-2% |
| Surface dehydration | Minimal | Moderate-High | None | Low |
| Uniformity | Excellent | Good | Excellent | Good |
| Color retention | Excellent | Good | Excellent | Very Good |
| Texture preservation | Excellent | Good | Very Good | Excellent |
| Energy efficiency | High | Low | Medium | Very Low |

Contact freezing in plate freezers provides an optimal balance of freezing speed, product quality, and energy efficiency for flat products, making it the preferred method for fish blocks, meat patties, and similar geometries.
