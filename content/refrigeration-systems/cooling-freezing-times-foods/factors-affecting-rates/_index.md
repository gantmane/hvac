---
title: "Factors Affecting Cooling and Freezing Rates"
description: "Comprehensive analysis of factors controlling food cooling and freezing rates including heat transfer coefficients, product geometry and Biot number, initial and final temperatures, thermal properties, air velocity effects, and packaging resistance for HVAC refrigeration system design"
weight: 5
---

The rate at which foods cool or freeze depends on multiple interrelated factors involving heat transfer mechanisms, product characteristics, and environmental conditions. Understanding these factors enables proper sizing of refrigeration equipment, optimization of process times, and maintenance of product quality.

## Heat Transfer Coefficient Effects

The surface heat transfer coefficient (h) governs the rate of heat removal from the product surface to the cooling medium. This coefficient represents the combined effects of convection and, in some cases, evaporation.

### Convective Heat Transfer Coefficients

For forced air cooling and freezing, typical heat transfer coefficients range as follows:

| Air Velocity (m/s) | h (W/m²·K) | Application |
|-------------------|------------|-------------|
| 0.5-1.0 | 5-10 | Natural convection, still air rooms |
| 1.0-2.5 | 10-25 | Low-velocity forced air |
| 2.5-5.0 | 25-50 | Standard blast freezing |
| 5.0-10.0 | 50-100 | High-velocity blast freezing |
| 10.0-20.0 | 100-200 | Fluidized bed, impingement freezing |

The heat transfer coefficient in forced convection follows empirical correlations of the form:

**Nu = C·Re^m·Pr^n**

where:
- Nu = Nusselt number = h·L/k
- Re = Reynolds number = ρ·v·L/μ
- Pr = Prandtl number = c_p·μ/k
- L = characteristic dimension (m)
- k = thermal conductivity of air (W/m·K)
- ρ = air density (kg/m³)
- v = air velocity (m/s)
- μ = dynamic viscosity (Pa·s)
- c_p = specific heat of air (J/kg·K)

For flow over flat surfaces, typical correlations:
- **Laminar flow (Re < 5×10⁵):** Nu = 0.664·Re^0.5·Pr^0.33
- **Turbulent flow (Re > 5×10⁵):** Nu = 0.037·Re^0.8·Pr^0.33

### Effect of Heat Transfer Coefficient on Process Time

The cooling or freezing time is inversely proportional to the heat transfer coefficient when surface resistance dominates. Doubling the heat transfer coefficient approximately halves the process time in convection-controlled systems.

For small products (Bi < 0.1), where internal resistance is negligible:

**t = (ρ·V·c_p)/(h·A) · ln[(T_i - T_∞)/(T_f - T_∞)]**

where:
- t = cooling time (s)
- ρ = product density (kg/m³)
- V = product volume (m³)
- c_p = specific heat (J/kg·K)
- A = surface area (m²)
- T_i = initial temperature (°C)
- T_f = final temperature (°C)
- T_∞ = cooling medium temperature (°C)

## Product Geometry and Size

The shape and dimensions of food products critically affect cooling and freezing rates through the surface area to volume ratio and internal heat transfer resistance.

### Characteristic Dimension

The characteristic dimension for heat transfer analysis depends on geometry:

| Geometry | Characteristic Dimension | Surface Area to Volume |
|----------|-------------------------|------------------------|
| Infinite slab | Half-thickness (a) | 2/a |
| Infinite cylinder | Radius (r) | 2/r |
| Sphere | Radius (r) | 3/r |
| Cube (side L) | L/6 | 6/L |
| Brick (dimensions a×b×c) | abc/(ab+bc+ca) | 2(ab+bc+ca)/abc |

### Size Effects on Cooling Time

For products where internal resistance dominates, cooling or freezing time is approximately proportional to the square of the characteristic dimension:

**t ∝ d²**

where d is the smallest dimension through which heat must be conducted.

This relationship explains why:
- Cutting products in half reduces freezing time by approximately 75%
- Doubling product thickness quadruples freezing time
- Small products (peas, berries) freeze in minutes, large products (whole turkeys) require hours

### Plank's Equation for Freezing Time

For regular-shaped products undergoing freezing, Plank's equation provides an estimate:

**t_f = (ρ·λ)/(T_f - T_a) · (P·a/h + R·a²/k)**

where:
- t_f = freezing time (s)
- ρ = density (kg/m³)
- λ = latent heat of fusion (J/kg)
- T_f = freezing point (°C)
- T_a = cooling medium temperature (°C)
- a = smallest dimension/characteristic dimension (m)
- h = surface heat transfer coefficient (W/m²·K)
- k = thermal conductivity of frozen product (W/m·K)
- P, R = shape factors

**Shape factors for Plank's equation:**

| Geometry | P | R |
|----------|---|---|
| Infinite slab | 1/2 | 1/8 |
| Infinite cylinder | 1/4 | 1/16 |
| Sphere | 1/6 | 1/24 |

The first term (P·a/h) represents surface resistance; the second term (R·a²/k) represents internal resistance.

## Initial and Final Temperatures

Temperature difference drives heat transfer and directly affects process time and refrigeration load.

### Temperature Differential Impact

The total heat to be removed:

**Q = m·c_p·(T_i - T_f)**

For products undergoing phase change (freezing):

**Q = m·[c_p,u·(T_i - T_f) + λ + c_p,f·(T_f - T_final)]**

where:
- c_p,u = specific heat above freezing (J/kg·K)
- c_p,f = specific heat below freezing (J/kg·K)
- λ = latent heat of fusion (J/kg)
- T_f = freezing point (°C)

### Typical Temperature Ranges

| Process | Initial Temp (°C) | Final Temp (°C) | Temperature Drop |
|---------|------------------|-----------------|------------------|
| Hydrocooling vegetables | 25-35 | 1-4 | 21-34 K |
| Forced air cooling produce | 20-30 | 0-5 | 15-30 K |
| Blast freezing | 5-15 | -18 to -30 | 23-45 K |
| Cryogenic freezing | 5-15 | -40 to -60 | 45-75 K |
| Deep freezing | -18 | -40 to -60 | 22-42 K |

### Precooling Impact on Freezing

Precooling products to near 0°C before freezing reduces freezing time by 15-30% compared to freezing from ambient temperature, because:
1. Less sensible heat removal required above freezing point
2. Reduced time at temperatures favorable for microbial growth
3. Smaller ice crystal formation when freezing point is reached rapidly

## Thermal Properties of Foods

Thermal properties determine how heat conducts through the product and how much energy must be removed.

### Thermal Conductivity

Thermal conductivity (k) varies significantly with temperature, moisture content, and state (frozen vs. unfrozen):

| Product | Unfrozen k (W/m·K) | Frozen k (W/m·K) | Water Content (%) |
|---------|-------------------|-----------------|-------------------|
| Lean beef | 0.45-0.48 | 1.2-1.4 | 70-75 |
| Fish (lean) | 0.50-0.54 | 1.6-1.8 | 75-80 |
| Poultry | 0.44-0.47 | 1.3-1.5 | 70-75 |
| Pork | 0.43-0.46 | 1.1-1.3 | 65-70 |
| Fruits (high moisture) | 0.55-0.60 | 1.8-2.2 | 85-90 |
| Vegetables (leafy) | 0.50-0.58 | 1.5-2.0 | 85-95 |
| Bread | 0.20-0.25 | 0.50-0.70 | 35-40 |
| Cheese | 0.35-0.40 | 0.90-1.10 | 40-50 |

**Frozen products conduct heat 2-4 times faster than unfrozen products** due to the higher thermal conductivity of ice (k_ice ≈ 2.2 W/m·K) compared to water (k_water ≈ 0.6 W/m·K).

### Specific Heat

Specific heat varies with temperature, particularly near the freezing point:

| Product | c_p Unfrozen (kJ/kg·K) | c_p Frozen (kJ/kg·K) |
|---------|------------------------|----------------------|
| Lean meat | 3.4-3.6 | 1.8-2.0 |
| Fish | 3.6-3.8 | 1.9-2.1 |
| Fruits (high moisture) | 3.8-4.0 | 2.0-2.2 |
| Vegetables | 3.8-4.1 | 2.0-2.2 |
| Dairy products | 3.0-3.5 | 1.6-1.9 |

### Apparent Specific Heat

During freezing, ice formation releases latent heat over a temperature range (not at a single freezing point for most foods). The apparent specific heat accounts for this:

**c_p,app = c_p + λ·(df/dT)**

where df/dT represents the rate of ice formation with temperature change.

Peak apparent specific heat occurs at the initial freezing point and can reach values of 50-200 kJ/kg·K for high-moisture foods.

### Latent Heat of Fusion

The latent heat depends on water content:

**λ = 334 × (moisture fraction)**

| Product | Moisture (%) | Latent Heat (kJ/kg) |
|---------|-------------|---------------------|
| Lean beef | 73 | 244 |
| Pork | 68 | 227 |
| Fish (cod) | 81 | 270 |
| Chicken | 74 | 247 |
| Strawberries | 90 | 300 |
| Lettuce | 95 | 317 |
| Ice cream | 60 | 200 |

### Density Changes

Density increases during freezing due to moisture loss and ice formation:

| Product | Unfrozen ρ (kg/m³) | Frozen ρ (kg/m³) |
|---------|-------------------|-----------------|
| Lean meat | 1050-1080 | 950-980 |
| Fish | 1040-1060 | 930-960 |
| Fruits | 980-1050 | 900-970 |
| Vegetables | 950-1020 | 880-950 |

Volume increases by approximately 8-10% upon freezing due to ice crystal expansion, despite weight loss from evaporation.

## Air Velocity and Flow Patterns

Air velocity affects both the heat transfer coefficient and the uniformity of cooling/freezing.

### Velocity Effects on Heat Transfer

The relationship between air velocity and heat transfer coefficient is approximately:

**h ∝ v^(0.5 to 0.8)**

For practical applications:

| Air Velocity (m/s) | Relative h | Relative Process Time | Energy Cost Factor |
|-------------------|-----------|----------------------|-------------------|
| 1 | 1.0 | 1.00 | 1.0 |
| 2 | 1.5 | 0.67 | 1.6 |
| 4 | 2.3 | 0.43 | 3.2 |
| 6 | 2.9 | 0.34 | 5.4 |
| 10 | 3.8 | 0.26 | 10.0 |

**Diminishing returns:** Increasing velocity from 1 to 2 m/s provides greater benefit than increasing from 6 to 10 m/s, while fan power increases with the cube of velocity.

### Optimal Air Velocity Selection

Selection criteria:

1. **Product sensitivity:** Delicate products (berries, leafy vegetables) limited to 2-4 m/s to prevent physical damage and excessive moisture loss
2. **Economic optimization:** Balance reduced freezing time against increased fan power consumption
3. **Surface dehydration:** High velocities increase moisture loss, requiring humidity control
4. **Typical ranges:**
   - Hydrocooling rooms: 0.5-1.5 m/s
   - Cold storage: 0.3-0.8 m/s
   - Blast freezers: 3-6 m/s
   - Spiral freezers: 4-8 m/s
   - Fluidized bed freezers: 8-15 m/s
   - Impingement freezers: 15-30 m/s

### Flow Pattern Effects

Uniform air distribution ensures consistent cooling/freezing rates:

- **Parallel flow:** Air flows in same direction as product movement, suitable for tunnel systems
- **Perpendicular flow:** Air flows through stacked products, common in batch systems
- **Transverse flow:** Cross-flow through product bed in belt freezers
- **Impingement:** High-velocity jets directly impact product surface

**Dead zones** with low air velocity create slow-cooling areas. Proper air distribution design maintains velocity variation within ±20% across the product load.

## Packaging Effects

Packaging materials add thermal resistance between the product and cooling medium, increasing process time.

### Packaging Thermal Resistance

The additional resistance from packaging:

**R_pkg = t_pkg/k_pkg**

where:
- t_pkg = packaging thickness (m)
- k_pkg = thermal conductivity of packaging material (W/m·K)

| Packaging Material | k (W/m·K) | Typical Thickness (mm) | R_pkg (m²·K/W) |
|-------------------|-----------|----------------------|----------------|
| Polyethylene film | 0.33-0.38 | 0.025-0.050 | 0.0007-0.0015 |
| Polystyrene foam | 0.033-0.038 | 3-10 | 0.08-0.30 |
| Corrugated cardboard | 0.060-0.070 | 3-6 | 0.043-0.100 |
| Waxed carton | 0.055-0.065 | 1-3 | 0.015-0.055 |
| Aluminum foil | 200-235 | 0.010-0.020 | 0.00004-0.0001 |
| Paper wrap | 0.050-0.060 | 0.05-0.10 | 0.0008-0.0020 |

### Impact on Cooling Time

The percent increase in cooling/freezing time due to packaging:

**Time increase (%) ≈ (R_pkg·h)/(1 + R_pkg·h) × 100**

**Example calculation:**
For h = 50 W/m²·K and polystyrene foam packaging (R_pkg = 0.15 m²·K/W):

Time increase = (0.15 × 50)/(1 + 0.15 × 50) × 100 = 7.5/(8.5) × 100 = 88%

This packaging nearly doubles the freezing time.

### Packaging Design Considerations

1. **Perforated packaging:** Holes improve air circulation and reduce thermal resistance by 30-60%
2. **Minimal packaging for rapid processes:** Use only film wraps for blast freezing, apply rigid packaging after freezing
3. **Contact freezing:** Packaging must allow good thermal contact with plates
4. **Moisture barrier post-freezing:** Apply moisture-resistant packaging after freezing to prevent dehydration during storage

### Air Gaps

Air trapped between packaging and product adds significant resistance:

**k_air ≈ 0.024 W/m·K at 0°C**

A 2 mm air gap provides equivalent resistance to 10-20 mm of typical packaging material. Vacuum packaging eliminates air gaps and reduces freezing time by 15-25% compared to conventional packaging with air spaces.

## Biot Number Analysis

The Biot number (Bi) characterizes the relative importance of internal vs. external heat transfer resistance.

### Biot Number Definition

**Bi = (h·L_c)/k**

where:
- h = surface heat transfer coefficient (W/m²·K)
- L_c = characteristic length = V/A (m)
- k = thermal conductivity of product (W/m·K)

For simple geometries:
- **Slab (thickness 2a):** L_c = a
- **Cylinder (radius r):** L_c = r/2
- **Sphere (radius r):** L_c = r/3

### Interpretation of Biot Number

| Biot Number | Controlling Resistance | Implication |
|-------------|----------------------|-------------|
| Bi < 0.1 | External (surface) | Lumped capacitance valid; uniform internal temperature |
| 0.1 < Bi < 40 | Both internal and external | Full transient conduction analysis required |
| Bi > 40 | Internal (conduction) | Surface temperature ≈ medium temperature |

### Examples of Biot Number

**Small berry in blast freezer:**
- L_c = 0.005 m (5 mm radius)
- h = 60 W/m²·K
- k = 0.50 W/m·K (unfrozen)
- Bi = (60 × 0.005)/0.50 = 0.60

Both resistances matter; transient analysis needed.

**Large beef roast in still air:**
- L_c = 0.05 m (50 mm half-thickness)
- h = 8 W/m²·K
- k = 0.45 W/m·K (unfrozen)
- Bi = (8 × 0.05)/0.45 = 0.89

Both resistances significant.

**Whole turkey in blast freezer:**
- L_c = 0.08 m (estimated)
- h = 50 W/m²·K
- k = 1.3 W/m·K (frozen)
- Bi = (50 × 0.08)/1.3 = 3.08

Internal resistance dominates.

### Design Implications

**For Bi < 0.1 (surface resistance controls):**
- Increase heat transfer coefficient (higher velocity, better air distribution)
- Reduce packaging resistance
- Cooling time: t ∝ 1/h

**For Bi > 40 (internal resistance controls):**
- Reduce product size/thickness
- Improve product thermal conductivity (if possible)
- Increasing h beyond certain point provides minimal benefit
- Cooling time: t ∝ L²/k

**For intermediate Bi values:**
- Optimize both surface conditions and product geometry
- Use Heisler charts or numerical methods for accurate time prediction

### Biot Number During Freezing

Biot number changes during freezing because thermal conductivity increases:

**Initial Bi (unfrozen):** Bi_u = h·L_c/k_u
**Final Bi (frozen):** Bi_f = h·L_c/k_f

Since k_f ≈ 2-4 × k_u, the final Biot number is 2-4 times smaller than initial. This means:
- Surface resistance becomes more important as freezing progresses
- Early stage freezing may be conduction-limited, later stages surface-limited

## Combined Effects and Optimization

All factors interact to determine overall cooling/freezing rate. Optimization requires considering:

### System Design Hierarchy

1. **Product geometry:** Most powerful effect (t ∝ L²); minimize thickness
2. **Temperature differential:** Increase ΔT where product quality allows
3. **Heat transfer coefficient:** Optimize air velocity for economic benefit
4. **Packaging:** Minimize resistance; use perforated designs
5. **Thermal properties:** Select or condition products for favorable properties where possible

### Economic Optimization

The optimal design balances:
- **Capital cost:** Equipment size, refrigeration capacity
- **Operating cost:** Energy consumption, labor
- **Product quality:** Moisture loss, texture, appearance
- **Throughput:** Production rate requirements

**Typical optimization targets:**
- Maximize heat transfer per unit of energy consumed: h/P_fan
- Minimize total cost per unit mass frozen: (Capital + Operating)/throughput
- Maintain product temperature uniformity: σ_T < 2-3°C across load

### ASHRAE Handbook References

Detailed data, correlations, and design procedures are found in:

- **ASHRAE Handbook—Refrigeration, Chapter 19:** Thermal Properties of Foods
- **ASHRAE Handbook—Refrigeration, Chapter 29:** Methods of Precooling Fruits, Vegetables, and Cut Flowers
- **ASHRAE Handbook—Refrigeration, Chapter 30:** Refrigerated Facility Design
- **ASHRAE Handbook—Fundamentals, Chapter 1:** Psychrometrics
- **ASHRAE Handbook—Fundamentals, Chapter 4:** Heat Transfer
- **ASHRAE Handbook—Fundamentals, Chapter 19:** Thermal Properties of Foods

These chapters provide:
- Comprehensive thermal property data for hundreds of food products
- Empirical correlations for heat transfer coefficients
- Time-temperature prediction methods including Plank's equation modifications
- Process design guidelines and examples
- Quality considerations for various cooling and freezing methods

### Process Control Considerations

Monitor and control:
1. **Air temperature:** ±0.5-1°C for consistent heat transfer driving force
2. **Air velocity:** ±10% for uniform processing
3. **Product temperature:** Multiple points to detect slow-cooling zones
4. **Relative humidity:** 85-95% for refrigeration, 90-98% for freezing to minimize dehydration
5. **Process time:** Adjust for product size variations, initial temperature differences

Understanding these factors and their interactions enables design of efficient refrigeration systems that meet product quality requirements while minimizing energy consumption and capital investment.
