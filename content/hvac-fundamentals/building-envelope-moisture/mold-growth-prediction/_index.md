---
title: "Mold Growth Prediction"
weight: 4
description: "Quantitative mold growth prediction methods including critical moisture content analysis, isopleth systems, VTT mold growth model, ASHRAE 160 criteria, and biohygrothermal modeling for building envelope design verification."
---

# Mold Growth Prediction

Mold growth represents a critical building envelope failure mode affecting both building durability and occupant health. Quantitative mold growth prediction employs empirical models correlating temperature, relative humidity, substrate material, and exposure duration to predict germination and growth rates. These models enable physics-based design verification beyond simple condensation avoidance.

## Mold Growth Requirements

Mold germination and growth require the simultaneous presence of four conditions:

### 1. Substrate

**Nutrient Source**: Organic materials provide carbon-based nutrition

**Mold-Susceptible Materials**:
- Wood and wood products (framing, sheathing, trim)
- Paper-faced gypsum board
- Cellulose insulation
- Fabric, carpet, upholstery
- Dust accumulation on inorganic surfaces

**Mold-Resistant Materials**:
- Unfaced gypsum board (lower nutrient availability)
- Mineral wool insulation
- Concrete, masonry (when clean)
- Metal, glass (when clean)
- Closed-cell spray foam

**Substrate Classification** (VTT model):

| Class | Sensitivity | Examples |
|-------|-------------|----------|
| Very Sensitive | Highest risk | Pine sapwood, paper-faced gypsum |
| Sensitive | High risk | Untreated wood, plywood, OSB |
| Medium Resistant | Moderate risk | Concrete, aerated concrete |
| Resistant | Low risk | Treated wood, mineral fiber |

### 2. Temperature

**Optimal Range**: 77-86°F (25-30°C)

**Growth Range**: 40-100°F (4-38°C)

**Temperature Effects**:
- Below 40°F (4°C): Growth ceases (spores remain viable)
- 40-60°F (4-15°C): Slow growth rate
- 60-86°F (15-30°C): Rapid growth, increasing with temperature
- Above 100°F (38°C): Growth inhibited, some species die

**Critical Threshold**: ASHRAE 160 uses 41°F (5°C) as minimum temperature for mold risk assessment

### 3. Relative Humidity

**Critical Surface RH**: ≥ 80% for porous materials, ≥ 90% for smooth materials

**RH-Growth Rate Relationship**:

```
Growth rate increases exponentially with RH above threshold:
RH 80-85%: Slow germination, minimal growth
RH 85-90%: Moderate growth rate
RH 90-100%: Rapid growth, multiple species
```

**Surface RH vs. Ambient RH**:

Surface relative humidity differs from ambient based on temperature gradient:

```
RH_surface = (pv_ambient / psat(T_surface)) × 100%

where:
pv_ambient = partial vapor pressure in ambient air
psat(T_surface) = saturation pressure at surface temperature
```

**Example**:
Ambient: 70°F, 50% RH → pv = 0.18 in. Hg
Surface: 55°F → psat = 0.21 in. Hg

RH_surface = (0.18 / 0.21) × 100% = 85.7%

Cold surface elevates local RH despite moderate ambient conditions.

### 4. Time Duration

**Germination Time**: 24-48 hours at optimal conditions (T = 77°F, RH ≥ 80%)

**Visible Growth**: 7-14 days sustained conditions

**Extensive Colonization**: 3-4 weeks

**Time-RH Trade-off**:
- RH 80-85%: Germination requires days to weeks
- RH 90-95%: Germination within 24-48 hours
- RH > 95%: Germination within hours

## Critical Moisture Content

Equilibrium moisture content (EMC) of hygroscopic materials relates to ambient relative humidity via sorption isotherms.

### Wood EMC-RH Relationship

Simplified EMC equation for wood (Hailwood-Horrobin model):

```
EMC ≈ 1800/W × (KH/(1 - KH)) + K1KH/(1 + K1KH)

where:
W = 349 + 1.29T + 0.0135T²
K = 0.805 + 0.000736T - 0.00000273T²
K1 = 6.27 - 0.00938T - 0.000303T²
H = RH (decimal)
T = temperature (°F)
```

**Simplified approximation** for typical HVAC conditions (60-80°F):

```
EMC (%) ≈ 0.22 × RH (%)

For RH = 80%: EMC ≈ 17.6%
For RH = 70%: EMC ≈ 15.4%
For RH = 60%: EMC ≈ 13.2%
```

**Critical Moisture Content for Mold Growth**:

| Material | Critical EMC (% by weight) | Corresponding RH |
|----------|---------------------------|------------------|
| Wood (untreated) | > 16% | > 75% |
| Plywood, OSB | > 18% | > 80% |
| Paper (gypsum facing) | > 12% | > 70% |
| Cellulose insulation | > 18% | > 80% |

**80% RH Threshold**: Widely used critical threshold based on empirical observation that most building materials support mold growth when in equilibrium with ≥ 80% RH environment.

## Water Activity

Water activity (aw) represents equilibrium RH in decimal form:

```
aw = RH / 100

Example: 80% RH → aw = 0.80
```

**Minimum Water Activity for Mold Species**:

| Mold Type | Minimum aw | Corresponding RH |
|-----------|-----------|------------------|
| Xerophilic molds | 0.65-0.70 | 65-70% |
| Most common indoor molds | 0.80-0.85 | 80-85% |
| Hydrophilic molds | 0.90+ | 90%+ |

**Building Material Applications**:
- aw < 0.70: Mold-safe for all species
- aw 0.70-0.80: Risk for xerophilic species (prolonged exposure)
- aw ≥ 0.80: **Critical threshold**, risk for common indoor molds
- aw ≥ 0.90: High risk, rapid growth

## Mold Growth Models

### Isopleth Systems

**Concept**: Graphical representation of mold growth boundaries on temperature-RH coordinates

**Lowest Isopleth Limit (LIM)**: Minimum conditions for mold germination

**Critical Isopleth**: Boundary for specific growth rates (e.g., 1 mm/week)

**Example Isopleth Values** (generic indoor molds):

Temperature (°F) | Minimum RH for Germination | Minimum RH for Growth (1 mm/week)
-----------------|-----------------------------|----------------------------------
50 | 85% | 92%
60 | 82% | 88%
70 | 80% | 85%
80 | 78% | 83%

**Limitations**:
- Steady-state conditions assumed
- No accounting for fluctuating RH
- Species-specific variations
- Substrate effects not quantified

### VTT Mold Growth Model

Developed by VTT Technical Research Centre of Finland, this model predicts mold index as function of temperature, RH, material sensitivity, and time.

**Mold Index Scale**:

| Index | Description | Visible Observation |
|-------|-------------|---------------------|
| 0 | No growth | Spores dormant |
| 1 | Small amounts, microscopic | Not visible |
| 2 | Moderate, <10% coverage | Detection by microscopy |
| 3 | Visual, 10-30% coverage | Visual detection beginning |
| 4 | Visual, 30-70% coverage | Clearly visible |
| 5 | Abundant, 70-100% coverage | Extensive colonization |
| 6 | Very heavy, > 100% original | Dense growth layers |

**Growth Equation** (simplified):

```
dM/dt = 1 / (7 × exp(-0.68 × ln(RH - A) - 13.9 × ln(RH - A) / T))

where:
M = mold index (0-6)
t = time (days)
RH = relative humidity (%)
T = temperature (°C)
A = critical RH threshold for material (sensitivity class)
```

**Material Sensitivity Factor A**:
- Very sensitive (pine sapwood): A = 80%
- Sensitive (plywood, OSB): A = 80%
- Medium resistant (concrete): A = 85%
- Resistant (treated wood): A = 90%

**Model Application**:
1. Input hourly temperature and RH at surface
2. Calculate growth rate dM/dt for each hour
3. Integrate over time to obtain cumulative mold index
4. **Failure criterion**: M > 3 indicates unacceptable growth

**Decline Modeling**:

When RH drops below threshold, mold index declines:

```
dM/dt = -0.032 (M = 1-2)
dM/dt = -0.016 (M = 3-6)
```

Prolonged dry periods can reduce mold index, but do not eliminate spores.

### Biohygrothermal (BHT) Models

Advanced models couple hygrothermal simulation with biological growth kinetics.

**Coupled Physics**:
1. Heat transfer (temperature distribution)
2. Moisture transfer (RH, moisture content distribution)
3. Biological kinetics (spore germination, hyphal growth, sporulation)

**Governing Equation** (biological component):

```
∂B/∂t = μ(T,RH,S) × B - d(T) × B

where:
B = biomass concentration
μ = specific growth rate (function of T, RH, substrate S)
d = decay rate (function of T)
```

**Growth Rate Function**:

```
μ(T,RH,S) = μmax × fT(T) × fRH(RH) × fS(S)

where:
μmax = maximum specific growth rate
fT = temperature factor (0-1)
fRH = humidity factor (0-1)
fS = substrate quality factor (0-1)
```

**Software Tools**:
- WUFI Bio: Integrates VTT model with WUFI hygrothermal simulation
- MOISTURE-EXPERT: Biohygrothermal modeling capability
- DELPHIN: Coupled simulation with mold growth module

## ASHRAE Standard 160

**Title**: Criteria for Moisture-Control Design Analysis in Buildings

**Purpose**: Establish quantitative acceptance criteria for hygrothermal analysis

### Failure Criteria

**Primary Criterion** (Section 5.1):

```
30-day running average surface RH ≤ 80%
when surface temperature > 41°F (5°C)
```

**Calculation**:

```
RH_avg,30day = (ΣRH_i) / 720 hours

where RH_i includes only hours when T > 41°F
```

**Rationale**: 80% RH sustained for 30 days provides sufficient time for mold germination on most building materials at typical indoor temperatures.

### Application Methodology

**Step 1**: Hygrothermal Simulation
- 3-year minimum simulation period
- Hourly climate data (TMY3 or equivalent)
- Detailed assembly construction
- Material hygrothermal properties

**Step 2**: Post-Processing
- Extract surface temperature and RH at critical interfaces
- Calculate 30-day running average RH
- Identify hours where T > 41°F

**Step 3**: Criteria Evaluation

```
For each hour i:
  If T_i > 41°F:
    Calculate RH_avg,30day,i = average of RH from hours (i-719) to i
    If RH_avg,30day,i > 80%:
      FAILURE at hour i
```

**Step 4**: Risk Assessment
- Occasional brief exceedances (< 10 hours/year): Low risk
- Seasonal exceedances (> 100 hours/year): Moderate risk, review design
- Sustained exceedances (> 500 hours/year): High risk, redesign required

### Design Acceptance

**Climate Loads**:
- Outdoor: Standard 160 reference year (severe moisture year)
- Indoor: Standard 160 interior moisture generation schedule

**Pass Criteria**: Zero hours exceeding 80% RH 30-day running average

**Practical Application**: Standard 160 provides conservative design verification, suitable for code compliance and liability minimization.

## Practical Mold Prevention Strategies

### Surface Temperature Control

Maintain interior surface temperatures above dewpoint:

```
T_surface,min > T_dewpoint + 5°F (safety margin)
```

**Design Measures**:
- Adequate insulation: Increase R-value to warm interior surfaces
- Thermal bridge elimination: Continuous insulation, thermal breaks
- Interior surface insulation: Warm cold spots locally

### Relative Humidity Control

**Target Interior RH**:
- Winter (heating): 30-40% RH
- Summer (cooling): 45-55% RH

**Control Methods**:
- Dehumidification: Standalone or integrated with HVAC
- Ventilation: Exhaust moisture sources (bathrooms, kitchens)
- Source control: Limit interior moisture generation
- Air sealing: Prevent humid outdoor air infiltration

### Moisture Accumulation Limits

**Design Verification**:

For materials potentially accumulating moisture, verify drying rate exceeds accumulation rate:

```
M_dry,annual > M_accumulate,annual

where:
M_dry = Σ(moisture removed during drying periods)
M_accumulate = Σ(moisture added during wetting periods)
```

Hygrothermal modeling provides quantitative annual moisture balance.

### Material Selection

**Mold-Resistant Materials** for high-risk locations:

Location | Standard Material | Mold-Resistant Alternative
---------|-------------------|---------------------------
Basement walls | Paper-faced gypsum | Paperless gypsum, cement board
Bathroom walls | Standard gypsum | Mold-resistant gypsum, tile backer
Crawlspace | Fiberglass insulation | Closed-cell spray foam
Roof sheathing | OSB | Plywood, ZIP sheathing with treatment

## Measurement and Monitoring

**Surface Temperature**: IR thermography, thermocouples at critical locations

**Surface RH**: Hygrothermal sensors mounted at assembly interfaces (sheathing, interior surface)

**Moisture Content**: Pin or capacitance meters in wood-based materials

**Continuous Monitoring** (high-risk assemblies):
- Install RH/T sensors during construction
- Data logging at 15-60 minute intervals
- Alert thresholds: RH > 80% for > 48 hours

**Interpretation**:
- RH < 75%: Safe, no mold risk
- RH 75-80%: Caution zone, monitor trends
- RH > 80% sustained: High risk, investigate immediately

## Related Topics

- [Mold Growth Conditions](./mold-growth-conditions/) - Detailed environmental requirements for germination and growth
- [Critical Moisture Content](./critical-moisture-content/) - EMC relationships and material-specific thresholds
- [Mold Growth Models](./mold-growth-models/) - VTT model, isopleth systems, biohygrothermal approaches
- [ASHRAE 160 Standard](./mold-growth-models/ashrae-160-standard/) - Design analysis criteria and acceptance methods

## Reference Standards

- **ASHRAE Standard 160** - Criteria for Moisture-Control Design Analysis in Buildings
- **ASTM D3273** - Test Method for Resistance to Growth of Mold on the Surface of Interior Coatings in an Environmental Chamber
- **ASTM G21** - Standard Practice for Determining Resistance of Synthetic Polymeric Materials to Fungi
- **ISO 846** - Plastics - Evaluation of the action of microorganisms
- **VTT Research Reports** - Mold growth modeling methodology

---

*Mold growth prediction requires integrated analysis of surface temperature, relative humidity, material properties, and exposure duration using validated empirical models such as VTT or ASHRAE 160 criteria.*
