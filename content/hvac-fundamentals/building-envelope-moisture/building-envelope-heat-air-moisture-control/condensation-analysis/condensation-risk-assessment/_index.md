---
title: "Condensation Risk Assessment"
aliases: ["Condensation Risk Assessment"]
description: "Comprehensive methodology for evaluating condensation risk in building envelopes using temperature factor analysis, thermal resistance ratios, moisture accumulation calculations, and ASHRAE 160 criteria for mold growth prevention."
weight: 4
---

## Technical Overview

Condensation risk assessment evaluates the potential for moisture accumulation on surfaces or within building envelope assemblies when air reaches its dew point temperature. This analysis combines psychrometric principles, heat transfer calculations, and moisture transport modeling to predict condensation occurrence under various environmental conditions.

The assessment process identifies critical surfaces, calculates temperature factors, evaluates thermal resistance ratios, and applies moisture accumulation criteria to determine acceptability. Proper risk assessment prevents structural damage, mold growth, thermal performance degradation, and indoor air quality issues.

## Fundamental Condensation Criteria

### Dew Point Temperature Relationship

Condensation occurs when surface temperature drops below the dew point temperature of adjacent air:

```
T_surface ≤ T_dewpoint → Condensation occurs
```

Where:
- T_surface = Surface temperature (°F or °C)
- T_dewpoint = Dew point temperature of adjacent air (°F or °C)

The dew point temperature is determined from:

```
T_dp = T - [(100 - RH)/5]  (Approximation in °C)
```

Or using psychrometric equations:

```
T_dp = 243.04 × [ln(RH/100) + (17.625×T)/(243.04+T)] / [17.625 - ln(RH/100) - (17.625×T)/(243.04+T)]
```

Where:
- T = Dry-bulb temperature (°C)
- RH = Relative humidity (%)

### Critical Surface Temperature

The minimum surface temperature that prevents condensation:

```
T_critical = T_dewpoint + ΔT_safety
```

Where:
- ΔT_safety = Safety margin (typically 2-5°F or 1-3°C)

## Temperature Factor (f-factor)

### Definition and Calculation

The temperature factor quantifies how close a surface temperature approaches the indoor air temperature relative to the indoor-outdoor temperature difference:

```
f = (T_si - T_o) / (T_i - T_o)
```

Where:
- f = Temperature factor (dimensionless, 0 to 1)
- T_si = Interior surface temperature (°F or °C)
- T_i = Indoor air temperature (°F or °C)
- T_o = Outdoor air temperature (°F or °C)

### Minimum Temperature Factor

The minimum temperature factor to prevent condensation:

```
f_min = (T_dp - T_o) / (T_i - T_o)
```

For acceptable performance:

```
f_actual ≥ f_min
```

### Temperature Factor Requirements

Typical minimum temperature factors by climate zone:

| Climate Zone | Winter Design Temp | Indoor RH | Minimum f-factor |
|--------------|-------------------|-----------|------------------|
| 1 (Warm) | 40°F | 40% | 0.30 |
| 2 | 30°F | 40% | 0.40 |
| 3 | 20°F | 35% | 0.45 |
| 4 | 10°F | 35% | 0.50 |
| 5 | 0°F | 30% | 0.55 |
| 6 | -10°F | 30% | 0.60 |
| 7 (Cold) | -20°F | 25% | 0.65 |
| 8 (Subarctic) | -30°F | 25% | 0.70 |

## Thermal Resistance Ratio Method

### Surface Temperature Calculation

Interior surface temperature from thermal resistance ratios:

```
T_si = T_i - [(T_i - T_o) × R_si] / R_total
```

Where:
- R_si = Interior surface film resistance (h·ft²·°F/Btu)
- R_total = Total assembly R-value (h·ft²·°F/Btu)

### Total Assembly Resistance

```
R_total = R_si + R_1 + R_2 + ... + R_n + R_so
```

Where:
- R_1, R_2, R_n = Layer resistances
- R_so = Exterior surface film resistance

### Critical Resistance Ratio

The ratio of interior thermal resistance to total resistance:

```
R_ratio = R_si / R_total
```

Lower ratios indicate warmer interior surfaces and reduced condensation risk.

## Condensation Resistance Factor (CRF)

### Definition

The Condensation Resistance Factor quantifies the assembly's resistance to condensation formation:

```
CRF = (T_si - T_o) / (T_dp - T_o)
```

Performance criteria:
- CRF ≥ 1.0: No condensation expected
- CRF = 0.8-1.0: Marginal, monitor conditions
- CRF < 0.8: Condensation likely, redesign required

### Modified CRF for Safety Margin

```
CRF_modified = (T_si - T_o) / (T_dp + ΔT_safety - T_o)
```

Design target: CRF_modified ≥ 1.1

## ASHRAE Standard 160 Criteria

### Scope and Application

ASHRAE Standard 160 "Criteria for Moisture-Control Design Analysis in Buildings" provides criteria for preventing mold growth, material degradation, and moisture-related problems.

### Surface Moisture Index (SMI)

The 30-day running average surface relative humidity:

```
SMI = (1/30) × Σ(RH_surface,i)  for i = 1 to 30 days
```

Acceptance criteria:
- SMI < 80%: Acceptable for most materials
- SMI ≥ 80%: Mold growth potential exists

### Surface Relative Humidity Calculation

```
RH_surface = (P_sat(T_si) / P_sat(T_i)) × RH_i × 100%
```

Where:
- P_sat(T) = Saturation vapor pressure at temperature T
- RH_i = Indoor relative humidity (%)

### Saturation Vapor Pressure

Using the Magnus-Tetens equation:

```
P_sat(T) = 610.78 × exp[(17.27 × T) / (T + 237.3)]  (Pa, T in °C)
```

Or in English units:

```
P_sat(T) = 0.1171 × exp[(18.678 - T/234.5) × T / (257.14 + T)]  (psi, T in °F)
```

### Mold Growth Index

ASHRAE 160 references the VTT mold growth model:

```
M(t+Δt) = M(t) + max(0, (1/7) × k_1 × k_2 × Δt)
```

Where:
- M = Mold index (0-6 scale)
- k_1 = Intensity factor (function of RH and T)
- k_2 = Material susceptibility factor
- Δt = Time increment (weeks)

Acceptance: M < 3 (no visible growth)

### Design Criteria Summary

| Parameter | Limit | Duration |
|-----------|-------|----------|
| Surface RH | < 80% | 30-day average |
| Surface RH | < 100% | Instantaneous |
| Mold Index | < 3 | Annual analysis |
| MC (wood) | < 16% | Monthly average |

## Monthly Analysis Method

### Overview

Monthly analysis evaluates condensation risk throughout the annual cycle using representative monthly conditions rather than worst-case hourly data.

### Monthly Design Conditions

For each month, establish:

1. Mean outdoor temperature (T_o,monthly)
2. Mean indoor temperature (T_i,monthly)
3. Mean outdoor relative humidity (RH_o,monthly)
4. Design indoor relative humidity (RH_i,monthly)
5. Indoor moisture generation rate (G)

### Indoor Humidity Ratio Calculation

```
W_i = W_o + (G × 7000) / (ρ × Q)
```

Where:
- W_i = Indoor humidity ratio (lb_w/lb_da)
- W_o = Outdoor humidity ratio (lb_w/lb_da)
- G = Moisture generation rate (lb/h)
- ρ = Air density (lb/ft³)
- Q = Ventilation rate (cfm)

### Monthly Surface Temperature

```
T_si,monthly = T_i,monthly - [(T_i,monthly - T_o,monthly) × R_si] / R_total
```

### Monthly Condensation Hours

Estimate hours per month when T_si < T_dp:

```
H_condensation = N_hours × P(T_si < T_dp)
```

Where:
- N_hours = Hours in month (720, 744, etc.)
- P(T_si < T_dp) = Probability of condensation

### Cumulative Moisture Accumulation

```
M_accumulated = Σ[h_fg × ρ_air × (W_dp - W_si) × v_air × H_condensation]
```

Where:
- h_fg = Latent heat of vaporization (1060 Btu/lb)
- ρ_air = Air density (0.075 lb/ft³)
- W_dp, W_si = Humidity ratios at dew point and surface
- v_air = Air velocity near surface (fpm)

### Acceptance Criteria

Monthly analysis acceptance:
- No month exceeds 100 hours of condensation
- Total annual condensation < 500 hours
- Condensation periods allow complete drying
- No trapped moisture accumulation

## Interstitial Condensation Analysis

### Layer-by-Layer Temperature Distribution

Temperature at interface between layers m and m+1:

```
T_m = T_i - [(T_i - T_o) × Σ(R_1 to R_m)] / R_total
```

### Vapor Pressure at Each Layer

```
P_v,m = P_v,i - [(P_v,i - P_v,o) × Σ(M_1 to M_m)] / M_total
```

Where:
- P_v = Vapor pressure (in. Hg or Pa)
- M = Vapor permeance (perm)
- M_total = Total assembly vapor permeance

### Saturation Vapor Pressure Comparison

At each interface:

```
If P_v,m > P_sat(T_m): Condensation occurs at interface m
```

### Condensation Rate Calculation

```
q_condensation = (P_v,m - P_sat(T_m)) / M_m  (lb/h·ft² or g/h·m²)
```

## Risk Classification System

### Low Risk Conditions

- f-factor ≥ 0.70
- CRF ≥ 1.2
- Surface RH < 70% monthly average
- No interstitial condensation
- All months meet criteria

### Moderate Risk Conditions

- f-factor = 0.60-0.70
- CRF = 1.0-1.2
- Surface RH = 70-80% monthly average
- Minor condensation (< 50 hours/month)
- Adequate drying potential

### High Risk Conditions

- f-factor < 0.60
- CRF < 1.0
- Surface RH > 80% monthly average
- Frequent condensation (> 100 hours/month)
- Limited drying potential
- Interstitial condensation present

### Unacceptable Risk

- f-factor < 0.50
- CRF < 0.8
- Surface RH > 90%
- Continuous condensation conditions
- No drying periods
- Structural damage potential

## Design Considerations

### Thermal Bridge Evaluation

Linear thermal bridging reduces local surface temperature:

```
ψ = Q / (ΔT × L)
```

Where:
- ψ = Linear thermal transmittance (Btu/h·°F·ft)
- Q = Additional heat loss through bridge (Btu/h)
- L = Length of bridge (ft)

Adjusted surface temperature:

```
T_si,bridge = T_i - [(T_i - T_o) × (R_si + ψ×L/A)] / R_total
```

### Air Leakage Impact

Air leakage through envelope increases local condensation risk:

```
q_infiltration = ρ × c_p × Q_leak × (T_i - T_o)
```

Exfiltration deposits moisture within wall assembly.

### Moisture Storage Capacity

Materials with high moisture storage capacity buffer condensation:

```
C_moisture = ∂M/∂RH × ∂RH/∂P_v
```

Where:
- C_moisture = Moisture capacitance (lb/psi)
- M = Moisture content (lb_w/lb_material)

### Drying Potential Assessment

The drying time constant:

```
τ_dry = (M_stored × h_fg) / (ΔP_v / M_total)
```

Shorter time constants indicate better drying potential.

## Best Practices and Recommendations

### Assessment Protocol

1. Identify critical surfaces and assemblies
2. Establish design conditions (outdoor/indoor)
3. Calculate thermal resistance distributions
4. Determine surface temperatures at critical locations
5. Evaluate dew point temperatures
6. Calculate temperature factors and CRF values
7. Perform monthly analysis over annual cycle
8. Check interstitial condensation potential
9. Evaluate thermal bridges and penetrations
10. Assess drying potential between condensation periods
11. Apply ASHRAE 160 mold growth criteria
12. Classify risk level and recommend mitigation

### Mitigation Strategies by Risk Level

**Moderate Risk:**
- Increase thermal resistance
- Relocate insulation outboard
- Improve air sealing
- Control indoor humidity
- Add vapor retarders if appropriate

**High Risk:**
- Redesign assembly thermal performance
- Add continuous exterior insulation
- Install ventilation or drainage cavities
- Implement active humidity control
- Consider alternative materials

**Unacceptable Risk:**
- Complete assembly redesign mandatory
- Increase R-value significantly
- Add thermal breaks at bridges
- Active dehumidification required
- Regular monitoring and maintenance protocol

### Climate-Specific Considerations

**Cold Climates:**
- Focus on interior surface condensation
- Evaluate thermal bridges rigorously
- Control indoor humidity levels (< 35% RH in winter)
- Ensure adequate insulation R-values
- Use interior vapor retarders appropriately

**Hot-Humid Climates:**
- Assess exterior surface condensation in summer
- Evaluate reverse vapor drive potential
- Control air conditioning overcooling
- Consider vapor-permeable exterior layers
- Ensure adequate drainage and ventilation

**Mixed Climates:**
- Evaluate both heating and cooling seasons
- Use vapor semi-permeable assemblies
- Assess bi-directional drying potential
- Consider variable permeance membranes
- Monitor actual performance post-occupancy

### Documentation Requirements

Complete assessment documentation includes:
- Design climate data sources
- Indoor condition assumptions and basis
- Thermal resistance calculations with layer details
- Surface temperature calculations at critical locations
- Temperature factor and CRF calculations
- Monthly analysis results table
- Interstitial condensation analysis
- ASHRAE 160 compliance demonstration
- Risk classification determination
- Mitigation measures if required

## Code and Standard References

- ASHRAE Standard 160: Criteria for Moisture-Control Design Analysis in Buildings
- ASHRAE Handbook—Fundamentals, Chapter 25: Heat, Air, and Moisture Control in Building Assemblies
- ASHRAE Handbook—Fundamentals, Chapter 1: Psychrometrics
- ISO 13788: Hygrothermal Performance of Building Components and Building Elements
- NFRC 500: Procedure for Determining Fenestration Product Condensation Resistance Values
- WUFI and similar hygrothermal simulation tools
- International Energy Conservation Code (IECC)
- Local building codes and amendments
