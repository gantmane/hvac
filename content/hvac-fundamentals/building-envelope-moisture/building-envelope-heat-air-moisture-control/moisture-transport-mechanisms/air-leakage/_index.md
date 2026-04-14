---
title: "Air Leakage"
aliases: ["Air Leakage"]
description: "Pressure-driven moisture transport through building envelope openings, including air leakage mechanisms, driving forces, quantification methods, and control strategies for moisture management"
weight: 2
---

Air leakage represents the dominant moisture transport mechanism through building envelopes, typically transporting 10-100 times more moisture than vapor diffusion. This pressure-driven bulk transport of air and its entrained moisture occurs through unintentional openings, gaps, and cracks in the building envelope, driven by pressure differentials created by stack effect, wind, and mechanical systems.

## Fundamental Principles

### Pressure-Driven Flow Physics

Air leakage follows basic fluid mechanics principles, where volumetric flow rate depends on pressure differential and flow resistance:

**Power Law Equation:**

```
Q = C × (ΔP)^n
```

Where:
- Q = volumetric airflow rate (cfm or L/s)
- C = flow coefficient (depends on opening characteristics)
- ΔP = pressure difference across opening (Pa or in. w.c.)
- n = flow exponent (0.5-1.0, typically 0.65)

**Flow Exponent Interpretation:**

| Flow Regime | Exponent (n) | Characteristics |
|-------------|--------------|-----------------|
| Fully Laminar | 1.0 | Long, narrow cracks; viscous-dominated |
| Transitional | 0.6-0.8 | Most building envelope openings |
| Fully Turbulent | 0.5 | Short, wide openings; inertia-dominated |
| Typical Building | 0.65 | Average value for mixed openings |

### Moisture Transport by Air Leakage

The moisture transport rate through air leakage far exceeds diffusion:

**Mass Transport Equation:**

```
ṁ = ρ × Q × W
```

Where:
- ṁ = moisture transport rate (lb/hr or kg/s)
- ρ = air density (lb/ft³ or kg/m³)
- Q = volumetric airflow rate (cfm or m³/s)
- W = humidity ratio (lb H₂O/lb dry air or kg/kg)

**Example Comparison:**

For a 1 mm² opening in a wall assembly:
- **Diffusion:** ~0.001 g/hr moisture transport
- **Air leakage (10 Pa):** ~0.1 g/hr moisture transport
- **Ratio:** Air leakage transports 100× more moisture

## Driving Forces for Air Leakage

### Stack Effect

Temperature-induced density differences create vertical pressure gradients in buildings:

**Stack Pressure Equation:**

```
ΔP_stack = C_s × H × ΔT/T_avg
```

Where:
- ΔP_stack = stack pressure (Pa)
- C_s = stack coefficient (~0.0342 Pa/(m·K) or ~0.018 in. w.c./(ft·°F))
- H = height above neutral pressure level (m or ft)
- ΔT = indoor-outdoor temperature difference (K or °F)
- T_avg = average absolute temperature (K or °R)

**Simplified US Units:**

```
ΔP_stack = 0.018 × H × (T_in - T_out)/T_avg  [in. w.c.]
```

**Stack Effect Characteristics:**

| Building Height | Winter ΔT (40°F) | Summer ΔT (15°F) | Impact Level |
|-----------------|------------------|------------------|--------------|
| 1 story (10 ft) | ±0.09 in. w.c. | ±0.03 in. w.c. | Low |
| 3 stories (30 ft) | ±0.27 in. w.c. | ±0.10 in. w.c. | Moderate |
| 10 stories (100 ft) | ±0.90 in. w.c. | ±0.34 in. w.c. | High |
| 40 stories (400 ft) | ±3.60 in. w.c. | ±1.35 in. w.c. | Critical |

**Neutral Pressure Level (NPL):**

The NPL location depends on vertical distribution of leakage:
- Equal top/bottom leakage: NPL at mid-height
- Leaky top: NPL shifts upward
- Leaky bottom: NPL shifts downward

### Wind Pressure Effects

Wind creates positive pressure on windward surfaces and negative pressure on leeward surfaces:

**Wind Pressure Equation:**

```
ΔP_wind = C_p × 0.5 × ρ × V²
```

Where:
- ΔP_wind = wind-induced pressure (Pa)
- C_p = pressure coefficient (dimensionless)
- ρ = air density (kg/m³)
- V = wind velocity (m/s)

**Typical Pressure Coefficients:**

| Surface Location | C_p Range | Typical Value |
|------------------|-----------|---------------|
| Windward wall | +0.5 to +0.8 | +0.6 |
| Leeward wall | -0.3 to -0.5 | -0.4 |
| Side walls | -0.5 to -0.7 | -0.6 |
| Flat roof windward | -0.7 to -0.9 | -0.8 |
| Flat roof leeward | -0.3 to -0.5 | -0.4 |

**Simplified Wind Pressure (US Units):**

```
ΔP_wind = 0.00256 × C_p × V²  [lb/ft²]

ΔP_wind = 0.0129 × C_p × (mph)²  [Pa]
```

**Example:** 20 mph wind on windward wall (C_p = +0.6):
```
ΔP = 0.0129 × 0.6 × (20)² = 3.1 Pa (0.012 in. w.c.)
```

### Mechanical System Pressurization

HVAC systems create building pressurization through supply/return air imbalances:

**Building Pressure Equation:**

```
ΔP_mech = (Q_supply - Q_return - Q_exhaust)/C_building
```

Where:
- ΔP_mech = mechanical pressure differential (Pa)
- Q terms = airflow rates (cfm or m³/s)
- C_building = building leakage coefficient

**Typical Building Pressures:**

| Building Type | Target Pressure | Typical Range | Purpose |
|---------------|-----------------|---------------|---------|
| Residential | Neutral | -5 to +5 Pa | Comfort |
| Office | Slightly positive | +2 to +5 Pa | IAQ control |
| Hospital | Positive | +5 to +8 Pa | Infection control |
| Laboratory | Negative | -5 to -15 Pa | Containment |
| Cleanroom | Positive | +10 to +25 Pa | Contamination control |

### Combined Pressure Effects

Total pressure at any envelope location results from superposition:

```
ΔP_total = ΔP_stack + ΔP_wind + ΔP_mech
```

The dominant mechanism varies by:
- **Winter heating:** Stack effect dominates in tall buildings
- **Summer cooling:** Wind and mechanical may dominate
- **Shoulder seasons:** All three factors significant

## Air Leakage Paths

### Common Envelope Discontinuities

Air leakage occurs through numerous envelope penetrations and assembly gaps:

**Wall Assembly Leakage Sites:**

| Location | Typical Leakage | Control Priority |
|----------|-----------------|------------------|
| Window/door perimeters | 25-35% | Critical |
| Wall-to-roof connections | 15-20% | Critical |
| Penetrations (electrical, plumbing) | 15-25% | High |
| Wall-to-foundation joints | 10-15% | High |
| Material joints/seams | 10-15% | Moderate |
| Wall sheathing joints | 5-10% | Moderate |

**Roof/Attic Leakage Sites:**

- Attic access hatches
- Recessed light fixtures
- Plumbing stack penetrations
- HVAC duct penetrations
- Chimney/flue penetrations
- Ridge vents and soffits

**Foundation Leakage Sites:**

- Rim joist assemblies
- Sill plate connections
- Foundation wall penetrations
- Floor drain sumps
- Crawlspace vents

### Leakage Path Characteristics

**Flow Through Cracks:**

Long, narrow cracks exhibit laminar flow characteristics:

```
Q = (w³ × L × ΔP)/(12 × μ × l)
```

Where:
- w = crack width (in or m)
- L = crack length (in or m)
- l = crack depth (wall thickness)
- μ = dynamic viscosity
- ΔP = pressure differential

**Key Insight:** Flow varies with cube of crack width, making crack width control critical.

### Serial vs. Parallel Leakage

**Serial Leakage (through multiple layers):**
- Total resistance = sum of layer resistances
- Controlled by tightest layer
- Example: Air barrier with isolated penetrations

**Parallel Leakage (multiple independent paths):**
- Total leakage = sum of path leakages
- Dominated by largest openings
- Example: Multiple window/door assemblies

## Air Leakage Quantification

### Whole Building Air Leakage

**Blower Door Testing:**

Standardized test method per ASTM E779 and CGSB 149.10:

```
Q = C × (ΔP)^n
```

Test procedure:
1. Depressurize/pressurize building to 50 Pa
2. Measure airflow required to maintain pressure
3. Calculate leakage metrics

**Common Leakage Metrics:**

| Metric | Definition | Units | Application |
|--------|------------|-------|-------------|
| CFM50 | Airflow at 50 Pa | cfm | Absolute leakage |
| ACH50 | Air changes/hour at 50 Pa | ACH | Normalized by volume |
| EqLA | Equivalent leakage area | in² | Opening area equivalent |
| ELA | Effective leakage area | in² or cm² | Area at 4 Pa reference |
| SLA | Specific leakage area | in²/100 ft² | Normalized by surface area |

**Conversion Relationships:**

```
ACH50 = (CFM50 × 60)/Volume

ELA = CFM50/(2610 × √ΔP)  [at 4 Pa reference]

SLA = (ELA/Floor Area) × 100
```

**Typical Building Tightness:**

| Construction Type | ACH50 Range | Characterization |
|-------------------|-------------|------------------|
| Passive House | 0.6 or less | Very tight |
| High-performance | 1-3 | Tight |
| Energy code minimum | 3-5 | Moderate |
| Standard construction | 5-10 | Typical |
| Older/retrofit | 10-20 | Leaky |
| Very old/poor | 20+ | Very leaky |

### Component Air Leakage

**ASTM E283:** Air leakage test for fenestration and curtain walls

**Performance Ratings:**

| Component Type | Maximum Leakage | Test Pressure |
|----------------|-----------------|---------------|
| Windows (fixed) | 0.06 cfm/ft² | 1.57 psf (75 Pa) |
| Windows (operable) | 0.3 cfm/ft² | 1.57 psf (75 Pa) |
| Curtain walls | 0.06 cfm/ft² | 1.57 psf (75 Pa) |
| Storefront systems | 0.06 cfm/ft² | 1.57 psf (75 Pa) |

### Air Barrier Assembly Testing

**ASTM E2357:** Air leakage testing of air barrier assemblies

Maximum allowable leakage rates:

| Assembly Type | Maximum Leakage | Test Conditions |
|---------------|-----------------|-----------------|
| Air barrier material | 0.004 cfm/ft² | 1.57 psf (75 Pa) |
| Air barrier assembly | 0.04 cfm/ft² | 1.57 psf (75 Pa) |
| Composite wall assembly | 0.40 cfm/ft² | 1.57 psf (75 Pa) |

## Dominance Over Vapor Diffusion

### Quantitative Comparison

Air leakage transports moisture at rates orders of magnitude greater than diffusion:

**Example Calculation:**

Consider a 1000 ft² wall assembly:
- Climate: Cold winter (70°F inside, 30°F outside, 40% RH inside)
- Leakage: 2 cfm at 50 Pa (moderate tightness)
- Diffusion: Standard wall assembly (10 perms)

**Moisture Transport by Diffusion:**

```
Vapor pressure difference:
Inside: 0.40 × 0.3630 = 0.145 in. Hg
Outside: 0.80 × 0.1621 = 0.130 in. Hg
Δp = 0.015 in. Hg

Transport rate:
ṁ_diff = (10 perms × 1000 ft² × 0.015 in. Hg)/7000
ṁ_diff = 0.021 lb/hr
```

**Moisture Transport by Air Leakage (10 Pa average):**

```
Airflow at 10 Pa:
Q = 2 cfm × (10/50)^0.65 = 0.47 cfm

Humidity ratio inside (70°F, 40% RH): W = 0.0063 lb/lb
Humidity ratio outside (30°F, 80% RH): W = 0.0033 lb/lb

Transport rate (exfiltration):
ṁ_leak = 0.47 cfm × 60 min/hr × 0.075 lb/ft³ × 0.0063
ṁ_leak = 0.013 lb/hr

Daily comparison (continuous):
Diffusion: 0.021 × 24 = 0.50 lb/day
Air leakage: 0.013 × 24 = 0.31 lb/day
```

**Critical Observation:** Even with this modest leakage rate, air transport approaches diffusion transport. At higher pressure differentials or leakier assemblies, air leakage dominates by factors of 10-100.

### Temperature Effects on Moisture Transport

Air leakage moisture transport capacity varies significantly with temperature:

| Indoor Conditions | W (lb/lb) | Air Capacity | Relative Impact |
|-------------------|-----------|--------------|-----------------|
| 70°F, 40% RH | 0.0063 | Baseline | 1.0× |
| 70°F, 60% RH | 0.0095 | High | 1.5× |
| 75°F, 40% RH | 0.0066 | Moderate | 1.05× |
| 68°F, 30% RH | 0.0040 | Low | 0.63× |

Higher indoor humidity ratios dramatically increase moisture transport through air leakage.

## Air Leakage Control Strategies

### Air Barrier System Design

**Fundamental Requirements:**

Per ASHRAE 90.1 and building codes, air barrier systems must:
1. Be continuous across envelope
2. Withstand design pressures
3. Meet leakage rate requirements
4. Accommodate building movements
5. Be durable over building life

**Air Barrier Location Options:**

| Location | Advantages | Disadvantages | Best Applications |
|----------|------------|---------------|-------------------|
| Exterior | Easy construction access | Exterior durability exposure | Most commercial |
| Interior | Protected from weather | Access issues, penetrations | Retrofit applications |
| Mid-wall | Optimal hygrothermal | Complex detailing | High-performance |
| Split system | Flexible design | Continuity challenges | Complex assemblies |

### Air Barrier Materials

**Material Performance Requirements:**

| Material Category | Air Permeance Limit | Standards | Applications |
|-------------------|---------------------|-----------|--------------|
| Sheet materials | 0.004 cfm/ft² @ 75 Pa | ASTM E2178 | Membranes, boards |
| Fluid-applied | 0.004 cfm/ft² @ 75 Pa | ASTM E2357 | Transitions, details |
| Board materials | 0.004 cfm/ft² @ 75 Pa | ASTM E2178 | Sheathing products |
| Building wraps | 0.004 cfm/ft² @ 75 Pa | ASTM E2178 | Exterior drainage plane |

**Common Air Barrier Systems:**

- Mechanically-attached membranes
- Self-adhered membranes
- Fluid-applied membranes
- Exterior gypsum sheathing (taped/sealed)
- Closed-cell spray foam insulation
- Polyethylene sheet systems
- Concrete/masonry (parged/sealed)

### Critical Transitions and Details

**Air Barrier Continuity Requirements:**

1. **Window/door rough openings:**
   - Sealant at frame perimeter
   - Compatible materials
   - Accommodate thermal movement

2. **Wall-to-roof transitions:**
   - Continuous membrane wrap
   - Compatible flashing systems
   - Structural movement accommodation

3. **Wall-to-foundation:**
   - Below-grade termination
   - Capillary break integration
   - Drainage provision

4. **Penetrations:**
   - Seal at air barrier plane
   - Proper backer materials
   - Accommodate service movement

5. **Material transitions:**
   - Compatible primer systems
   - Overlap/adhesion verification
   - Durability assessment

### Sealant Selection and Design

**Sealant Material Properties:**

| Sealant Type | Movement Capability | Durability | Cost | Applications |
|--------------|---------------------|------------|------|--------------|
| Silicone | ±50% | Excellent | High | Exterior joints, high-movement |
| Polyurethane | ±25% | Very good | Medium | General purpose, flexible |
| Acrylic latex | ±10% | Good | Low | Interior, low-movement |
| Butyl | ±5% | Good | Low | Bedding, low-movement |
| Modified silicone | ±35% | Excellent | High | High-performance applications |

**Joint Design Parameters:**

```
Joint width = (Expected movement/Sealant capability) + 1/4"

Minimum width = 1/4"
Maximum width = 1"
Depth = Width/2 (typical range)
```

### Pressure Management

**Building Pressurization Control:**

1. **Balanced ventilation:**
   - Supply ≈ exhaust + return
   - Minimize pressure differentials
   - Monitor building pressure

2. **Compartmentalization:**
   - Control pressure zones
   - Prevent stack effect transmission
   - Reduce total pressure ranges

3. **Depressurization mitigation:**
   - Makeup air for exhaust systems
   - Combustion air provisions
   - Prevent backdrafting

## Design Considerations

### Climate-Specific Strategies

**Cold Climates:**
- Control exfiltration (interior moisture → cold surfaces)
- Interior air barrier common
- Prevent interior moisture accumulation
- Design for stack effect pressures

**Hot-Humid Climates:**
- Control infiltration (exterior moisture → cold surfaces)
- Exterior air barrier preferred
- Interior vapor retarder caution
- Manage air conditioning condensation

**Mixed Climates:**
- Bidirectional moisture control
- Mid-wall air barrier considerations
- Seasonal performance balance
- Drying pathway provisions

### Integration with Other Systems

**Air Barrier and Vapor Control:**
- Air barriers reduce convective moisture transport
- Vapor retarders control diffusion (lesser concern)
- Systems may be combined (low-perm air barriers)
- Maintain assembly drying capability

**Water Management Integration:**
- Air barriers must not block drainage
- Drainage planes behind cladding
- Flashing integration at transitions
- Capillary break coordination

**Thermal Control:**
- Air barriers reduce convective heat loss
- Coordinate with insulation placement
- Prevent thermal bridging at details
- Address thermal movement

## ASHRAE and Code References

**Primary Standards:**

- **ASHRAE 90.1:** Energy Standard for Buildings Except Low-Rise Residential Buildings
  - Section 5.4: Air leakage requirements
  - Mandatory air barrier provisions
  - Testing requirements

- **ASHRAE 160:** Criteria for Moisture-Control Design Analysis in Buildings
  - Air leakage impact on moisture accumulation
  - Hygrothermal modeling parameters

- **ASHRAE 189.1:** Standard for the Design of High-Performance Green Buildings
  - Enhanced air tightness requirements
  - Testing and verification

**Test Standards:**

- **ASTM E779:** Standard Test Method for Determining Air Leakage Rate by Fan Pressurization
- **ASTM E283:** Standard Test Method for Determining Rate of Air Leakage Through Exterior Windows, Skylights, Curtain Walls, and Doors
- **ASTM E2178:** Standard Test Method for Air Permeance of Building Materials
- **ASTM E2357:** Standard Test Method for Determining Air Leakage of Air Barrier Assemblies

**Building Codes:**

- **International Energy Conservation Code (IECC):** Mandatory air sealing requirements
- **International Building Code (IBC):** Structural and durability requirements
- **International Residential Code (IRC):** Residential air sealing provisions

## Performance Verification

### Construction Quality Assurance

**Testing Protocols:**

1. **Pre-enclosure blower door test:**
   - Verify air barrier continuity
   - Identify major leakage sites
   - Early correction opportunity

2. **Final building test:**
   - Compliance verification
   - Performance documentation
   - Commissioning integration

3. **Infrared thermography:**
   - Air leakage visualization
   - During pressurization testing
   - Identify hidden defects

**Acceptance Criteria:**

Building codes and energy standards establish maximum allowable leakage rates. Testing confirms compliance and validates construction quality.

## Conclusion

Air leakage dominates moisture transport through building envelopes, transporting 10-100 times more moisture than vapor diffusion under typical conditions. Effective moisture control requires comprehensive air leakage control through continuous air barrier systems, proper detailing at transitions and penetrations, and integration with drainage and thermal control strategies. Pressure management through building design and HVAC system operation minimizes driving forces for air leakage. Performance verification through blower door testing ensures construction quality and validates moisture control effectiveness.
