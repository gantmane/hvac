---
title: "Dominance Over Diffusion"
aliases: ["Dominance Over Diffusion"]
description: "Quantitative analysis of air leakage moisture transport dominance over vapor diffusion in building envelopes, including transport mechanisms, comparative calculations, and design implications for moisture control"
weight: 1
---

## Physical Mechanisms of Moisture Transport

Air leakage transports moisture through building envelope assemblies at rates 10 to 100 times greater than vapor diffusion, fundamentally altering moisture management priorities in building design.

### Transport Mode Comparison

Two distinct physical processes move moisture through building envelopes:

**Vapor Diffusion:**
- Molecular-scale movement driven by partial pressure gradients
- Governed by Fick's Law: vapor flux proportional to permeability and pressure difference
- Continuous process occurring in all materials at all times
- Rate limited by material vapor permeance
- Transport occurs even with perfect air barriers

**Air Leakage (Convective Transport):**
- Bulk movement of air carrying entrained water vapor
- Driven by pressure differences across envelope
- Occurs through cracks, gaps, penetrations, and imperfections
- Transport rate proportional to airflow rate and humidity difference
- Can be eliminated with proper air sealing

The fundamental difference lies in the quantity transported per unit driving force.

## Quantitative Magnitude Comparison

### Moisture Transport Rates

The ratio of moisture transport by air leakage versus diffusion depends on:
- Magnitude of air pressure differences
- Air leakage area and flow characteristics
- Vapor pressure gradient
- Material vapor permeance
- Temperature conditions

**Typical Comparative Analysis:**

For a 1 m² section of wall with 10 Pa pressure difference and 1 cm²/m² leakage area:

Air leakage moisture transport:
```
Q_air = ρ_air × V̇ × Δω
```

Where:
- ρ_air = air density (≈ 1.2 kg/m³)
- V̇ = volumetric airflow rate (m³/s)
- Δω = humidity ratio difference (kg_water/kg_air)

Vapor diffusion transport:
```
q_vapor = M × A × Δp_v
```

Where:
- M = vapor permeance (ng/(Pa·s·m²))
- A = area (m²)
- Δp_v = vapor pressure difference (Pa)

### Example Calculation

**Winter conditions:**
- Indoor: 21°C, 40% RH (partial pressure 1,000 Pa)
- Outdoor: -10°C, 70% RH (partial pressure 180 Pa)
- Pressure difference: 10 Pa (stack effect and wind)
- Wall area: 1 m²
- Leakage area: 1 cm²/m² (0.0001 m²)

**Air Leakage Transport:**

Airflow through orifice:
```
V̇ = C_d × A_L × √(2Δp/ρ)
V̇ = 0.65 × 0.0001 m² × √(2 × 10 Pa / 1.2 kg/m³)
V̇ = 0.65 × 0.0001 × 4.08 = 2.65 × 10⁻⁴ m³/s
V̇ = 0.95 m³/h
```

Humidity ratio difference:
```
Δω = ω_in - ω_out
ω_in = 0.622 × p_v,in / (p_atm - p_v,in) = 0.622 × 1000/(101325-1000) = 0.0062 kg/kg
ω_out = 0.622 × 180/(101325-180) = 0.0011 kg/kg
Δω = 0.0051 kg/kg
```

Moisture transport by air leakage:
```
M_air = ρ × V̇ × Δω
M_air = 1.2 kg/m³ × 2.65×10⁻⁴ m³/s × 0.0051 kg/kg
M_air = 1.62 × 10⁻⁶ kg/s = 5.83 g/h per m²
```

**Vapor Diffusion Transport:**

Typical insulated wall permeance with vapor retarder: M = 60 ng/(Pa·s·m²)

Vapor pressure difference:
```
Δp_v = 1000 - 180 = 820 Pa
```

Moisture transport by diffusion:
```
M_diff = M × A × Δp_v
M_diff = 60 × 10⁻⁹ kg/(Pa·s·m²) × 1 m² × 820 Pa
M_diff = 4.92 × 10⁻⁸ kg/s = 0.177 g/h per m²
```

**Transport Ratio:**
```
Ratio = M_air / M_diff = 5.83 / 0.177 = 33:1
```

Air leakage transports 33 times more moisture than diffusion under these conditions.

## Pressure-Dependent Transport Amplification

### Effect of Pressure Magnitude

Air leakage moisture transport increases with the square root of pressure difference, while diffusion remains constant regardless of air pressure.

| Pressure Difference (Pa) | Air Leakage (g/h·m²) | Diffusion (g/h·m²) | Ratio |
|--------------------------|----------------------|--------------------|-------|
| 4 | 3.69 | 0.177 | 21:1 |
| 10 | 5.83 | 0.177 | 33:1 |
| 20 | 8.24 | 0.177 | 47:1 |
| 50 | 13.04 | 0.177 | 74:1 |
| 75 | 15.97 | 0.177 | 90:1 |

As building height increases or wind exposure intensifies, air leakage becomes progressively more dominant.

### Stack Effect Amplification

In tall buildings, stack effect creates substantial pressure differences:

```
Δp_stack = ρ_o × g × h × (T_in - T_out) / T_in
```

Where:
- ρ_o = outdoor air density (kg/m³)
- g = gravitational acceleration (9.81 m/s²)
- h = height difference (m)
- T = absolute temperature (K)

**Example for 20-story building (60 m):**

Winter conditions: T_in = 294 K (21°C), T_out = 263 K (-10°C)

```
Δp_stack = 1.3 × 9.81 × 60 × (294 - 263) / 294
Δp_stack = 80.7 Pa
```

At 80 Pa, the air leakage to diffusion ratio exceeds 100:1.

## Air Change Rate Impact

### Building Leakage Classification

Air leakage is characterized by air changes per hour at 50 Pa (ACH50):

| Building Tightness | ACH50 | Description |
|-------------------|-------|-------------|
| Very leaky | >10 | Older construction, no air sealing |
| Leaky | 7-10 | Typical existing buildings |
| Average | 4-7 | Standard new construction |
| Tight | 2-4 | Good air sealing practices |
| Very tight | 1-2 | Advanced air sealing, blower door tested |
| Passive House | <0.6 | Superior air barrier, certified testing |

### Infiltration Moisture Load

Annual infiltration moisture load for heating climates:

```
M_annual = ρ × V × ACH_natural × HDD × 24 × Δω_avg
```

Where:
- V = building volume (m³)
- ACH_natural = natural air change rate (typically ACH50/20)
- HDD = heating degree days
- Δω_avg = average humidity ratio difference

**Comparison for 200 m² house (3 m ceiling height = 600 m³):**

Climate: 5,000 HDD, average Δω = 0.004 kg/kg

| ACH50 | ACH_natural | Annual Infiltration Moisture (kg) |
|-------|-------------|-----------------------------------|
| 10 | 0.50 | 1,440 |
| 7 | 0.35 | 1,008 |
| 4 | 0.20 | 576 |
| 2 | 0.10 | 288 |
| 0.6 | 0.03 | 86 |

Vapor diffusion through the entire envelope: approximately 30-60 kg/year.

Even in relatively tight construction (ACH50 = 2), air leakage transports 5-10 times more moisture than diffusion through all surfaces combined.

## Exfiltration and Condensation Risk

### Critical Temperature Plane

During heating season exfiltration, moisture-laden indoor air travels through the envelope and reaches dewpoint temperature at a critical plane within the assembly.

**Condensation mass per exfiltration volume:**

```
m_condensed = ρ × V̇ × (ω_in - ω_sat,dewpoint)
```

For indoor air at 21°C, 40% RH (dewpoint 7°C) exfiltrating through cold sheathing:

If sheathing temperature = -5°C (below dewpoint):
```
ω_in = 0.0062 kg/kg
ω_sat,-5°C = 0.0016 kg/kg
Δω_condensable = 0.0046 kg/kg
```

For 1 m³/h exfiltration:
```
m_condensed = 1.2 kg/m³ × 1 m³/h × 0.0046 kg/kg = 0.0055 kg/h = 5.5 g/h
```

Over a 6-month heating season (4,380 hours):
```
Total condensation = 5.5 g/h × 4,380 h = 24.1 kg
```

This moisture accumulation can saturate sheathing, cause mold growth, and deteriorate structural components.

### Comparison with Diffusion-Only Scenario

Same wall section, diffusion-only transport (no air leakage):

Seasonal diffusion through 30 m² wall area with M = 60 ng/(Pa·s·m²):
```
M_seasonal = M × A × Δp_v,avg × t
M_seasonal = 60×10⁻⁹ × 30 × 700 Pa × 4,380 h × 3600 s/h
M_seasonal = 19.8 kg
```

However, this moisture typically does not condense because it reaches the cold side gradually and can often escape to the exterior before accumulating.

The critical difference is location and concentration:
- Air leakage deposits moisture at specific leak points
- Creates localized saturation and damage
- Condensation occurs rapidly at concentrated locations
- Diffusion distributes moisture across entire assembly
- Lower concentrations allow drying and redistribution

## Design Implications

### Priority Hierarchy for Moisture Control

Based on transport magnitude analysis:

1. **Air sealing (Primary Control):** Reduces moisture transport by factor of 10-100
2. **Proper ventilation:** Controls indoor humidity source
3. **Drainage planes:** Manages liquid water from exterior
4. **Vapor control layers:** Fine-tunes diffusion (secondary effect)

### Critical Air Barrier Requirements

**Performance criteria:**
- Material air permeability: <0.02 L/(s·m²) at 75 Pa
- Assembly tested air leakage: <0.20 L/(s·m²) at 75 Pa
- Continuity across all envelope penetrations
- Durability over building lifetime

**Common failure points where air leakage dominates:**
- Rim joist connections
- Window and door rough openings
- Electrical and plumbing penetrations
- Partition wall to exterior wall intersections
- Attic access hatches
- Recessed lighting in insulated ceilings

### ASHRAE Standard 160 Moisture Control

ASHRAE Standard 160 acknowledges air leakage dominance:

Air leakage rate assumptions for moisture analysis:
- Class I (tight): 0.1 L/(s·m²) at 75 Pa
- Class II (average): 0.3 L/(s·m²) at 75 Pa
- Class III (leaky): 1.0 L/(s·m²) at 75 Pa

Hygrothermal modeling protocols require air leakage input because diffusion-only models fail to predict real-world moisture problems.

## Measurement and Verification

### Blower Door Testing

Standard test protocol (ASTM E779, ISO 9972):

1. Pressurize building to 50 Pa
2. Measure airflow required to maintain pressure
3. Calculate equivalent leakage area (ELA) and ACH50
4. Depressurize test for bidirectional verification

**Target performance:**

| Climate Zone | Maximum ACH50 | Basis |
|--------------|---------------|-------|
| All zones | 5.0 | 2018 IECC prescriptive |
| All zones | 3.0 | 2021 IECC prescriptive |
| All zones | 0.6 | Passive House standard |

### Infrared Thermography

Identifies air leakage paths during blower door testing:

- Depressurize building (exfiltration mode)
- Scan interior surfaces with IR camera
- Cold spots indicate air leakage in heating season
- Quantify with temperature differential

Temperature depression at leak site:
```
ΔT_surface ≈ ΔT_air × (V̇_local / V̇_total) × f_convection
```

Visible temperature drops >2°C indicate significant air leakage.

## Seasonal Variation

### Heating Season (Winter)

Exfiltration dominates at upper floors:
- Stack effect creates positive interior pressure
- Warm, humid air escapes through upper envelope
- Condensation risk at cold sheathing

Infiltration dominates at lower floors:
- Negative interior pressure at base
- Cold, dry air enters
- Increases heating load but reduces condensation risk

### Cooling Season (Summer)

Infiltration at upper floors:
- Reverse stack effect in air-conditioned buildings
- Hot, humid air enters through upper envelope
- Condensation risk on cold interior surfaces

Exfiltration at lower floors:
- Cool, dry air escapes
- Reduced cooling efficiency

### Shoulder Seasons

Minimal stack effect:
- Wind-driven pressure differentials dominate
- Localized infiltration and exfiltration
- Moisture transport highly dependent on wind direction and speed

## Code Requirements and Standards

### International Energy Conservation Code (IECC)

Air leakage testing mandatory for residential buildings:
- 2018 IECC: 5 ACH50 maximum (climate zones 3-8)
- 2021 IECC: 3 ACH50 maximum (all climate zones)

### ASHRAE Standards

**Standard 62.1 (Ventilation):**
- Acknowledges infiltration credit based on envelope tightness
- Requires reduced credit for tight buildings
- Air leakage affects required mechanical ventilation rate

**Standard 90.1 (Energy):**
- Air barrier required for all climate zones
- Continuous air barrier assembly
- Materials must meet air permeance requirements

**Standard 160 (Moisture):**
- Hygrothermal analysis must include air leakage
- Provides air leakage rates for different construction classes
- Validates that air sealing is primary moisture control

## Advanced Considerations

### Interstitial Air Barriers

In some assemblies, air leakage dominates even with exterior air barriers:

Vented rainscreen with permeable sheathing:
- Air can circulate within cavity
- Interior air barrier becomes critical
- Exterior vapor permeability allows drying

### Mechanical Pressurization Effects

HVAC systems alter envelope pressure:

**Supply-dominant systems:**
- Positive building pressure
- Increased exfiltration
- Higher moisture removal in summer (beneficial)
- Higher moisture export in winter (condensation risk)

**Return-dominant systems:**
- Negative building pressure
- Increased infiltration
- Higher heating/cooling loads
- Reduced exfiltration condensation risk

### Air Leakage Distribution

Non-uniform leakage distribution affects moisture risk:

Concentrated leaks at specific locations:
- Higher moisture flux per unit area
- Localized saturation and damage
- More difficult to dry between wetting events

Distributed leakage across envelope:
- Lower flux per unit area
- Reduced condensation risk
- Easier moisture redistribution

## Practical Design Guidance

### Priority Actions for Moisture Control

**Most effective (address air leakage):**
1. Continuous air barrier system
2. Seal all penetrations and transitions
3. Blower door test and remediate leaks
4. Detail air barrier at construction drawings

**Less effective (address diffusion only):**
1. Vapor retarder selection
2. Vapor barrier positioning
3. Material permeance specifications

### Cost-Benefit Analysis

Air sealing costs: $1,000-3,000 per dwelling unit for quality installation

Moisture damage costs: $10,000-50,000+ per incident for:
- Mold remediation
- Sheathing replacement
- Insulation replacement
- Interior finish repair
- Health impacts

Prevention cost ratio: 1:10 to 1:50 compared to repair costs.

### Construction Quality Control

Critical inspection points:
- Rough framing: verify continuous air barrier path
- Rough mechanical/electrical: inspect penetration sealing
- Insulation: verify no compression of air barrier materials
- Pre-drywall: blower door test for early detection
- Final: verify performance meets targets

## Summary of Transport Dominance

Air leakage transports 10-100 times more moisture than vapor diffusion under typical building pressure differences. This fundamental relationship establishes air sealing as the primary moisture control strategy in building envelope design. Vapor diffusion control remains important but secondary to elimination of air leakage paths. Modern building codes increasingly recognize this hierarchy through mandatory air barrier requirements and air leakage testing protocols.

Effective moisture management requires addressing the dominant transport mechanism first—air leakage—followed by appropriate vapor diffusion control based on climate and assembly design.
