---
title: "Thermal Comfort: PMV/PPD Analysis and ASHRAE Standards"
description: "Comprehensive thermal comfort analysis including PMV/PPD calculations, heat balance equations, adaptive models, and ASHRAE 55 compliance criteria"
date: 2026-01-04
lastmod: 2026-01-04
author: "Evgeniy Gantman"
keywords:
  - thermal comfort
  - PMV
  - PPD
  - ASHRAE 55
  - predicted mean vote
  - thermal sensation
  - metabolic rate
categories:
  - HVAC Fundamentals
  - Indoor Environment
tags:
  - thermal comfort
  - human factors
  - building performance
---

## Overview

Thermal comfort quantifies human thermal sensation under specified environmental and personal conditions. The analytical framework combines heat transfer physics with empirical data from controlled human subject studies.

## Heat Balance Equation

Human thermal comfort requires zero net heat storage:

{{< formula display="true" >}}
M - W = Q_{sk} + Q_{res} + Q_{evap}
{{< /formula >}}

Where:
- $M$ = metabolic rate (W/m²)
- $W$ = external work (typically 0 for sedentary)
- $Q_{sk}$ = skin heat loss (W/m²)
- $Q_{res}$ = respiratory heat loss (W/m²)
- $Q_{evap}$ = evaporative heat loss (W/m²)

### Skin Heat Loss

Convection and radiation from skin surface:

{{< formula display="true" >}}
Q_{sk} = h_c A_{cl}(t_{cl} - t_a) + h_r A_{cl}(t_{cl} - \bar{t}_r)
{{< /formula >}}

Where:
- $h_c$ = convective heat transfer coefficient (W/m²·K)
- $h_r$ = radiative heat transfer coefficient (W/m²·K)
- $A_{cl}$ = clothed body surface area (m²)
- $t_{cl}$ = clothing surface temperature (°C)
- $t_a$ = air temperature (°C)
- $\bar{t}_r$ = mean radiant temperature (°C)

### Respiratory Heat Loss

{{< formula display="true" >}}
Q_{res} = 0.0014 M (34 - t_a) + 0.0173 M (5.87 - p_a)
{{< /formula >}}

Where:
- $p_a$ = water vapor pressure (kPa)
- First term: sensible heat loss
- Second term: latent heat loss

## PMV Model

Predicted Mean Vote (PMV) predicts thermal sensation on a 7-point scale:

{{< table title="ASHRAE Thermal Sensation Scale" >}}
| PMV Value | Thermal Sensation |
|-----------|------------------|
| +3 | Hot |
| +2 | Warm |
| +1 | Slightly warm |
| 0 | Neutral |
| -1 | Slightly cool |
| -2 | Cool |
| -3 | Cold |
{{< /table >}}

### PMV Calculation

The PMV equation (Fanger's model):

{{< formula display="true" >}}
PMV = \left[0.303 \exp(-0.036M) + 0.028\right] L
{{< /formula >}}

Where $L$ = thermal load on body:

{{< formula display="true" >}}
\begin{aligned}
L = &(M - W) - 3.05 \times 10^{-3}[5733 - 6.99(M-W) - p_a] \\
&- 0.42[(M-W) - 58.15] \\
&- 1.7 \times 10^{-5}M(5867 - p_a) \\
&- 0.0014M(34 - t_a) \\
&- 3.96 \times 10^{-8}f_{cl}[(t_{cl} + 273)^4 - (\bar{t}_r + 273)^4] \\
&- f_{cl}h_c(t_{cl} - t_a)
\end{aligned}
{{< /formula >}}

### Clothing Surface Temperature

Iterative solution required:

{{< formula display="true" >}}
t_{cl} = 35.7 - 0.028(M-W) - I_{cl}\left[3.96 \times 10^{-8}f_{cl}[(t_{cl}+273)^4 - (\bar{t}_r+273)^4] + f_{cl}h_c(t_{cl} - t_a)\right]
{{< /formula >}}

Where:
- $I_{cl}$ = clothing insulation (m²·K/W or clo)
- $f_{cl}$ = clothing area factor

{{< formula display="true" >}}
f_{cl} = \begin{cases}
1.00 + 1.290 I_{cl} & \text{if } I_{cl} \le 0.078 \text{ m}^2\text{K/W} \\
1.05 + 0.645 I_{cl} & \text{if } I_{cl} > 0.078 \text{ m}^2\text{K/W}
\end{cases}
{{< /formula >}}

## PPD Model

Predicted Percentage Dissatisfied (PPD) relates to PMV:

{{< formula display="true" >}}
PPD = 100 - 95 \exp(-0.03353 \cdot PMV^4 - 0.2179 \cdot PMV^2)
{{< /formula >}}

{{< diagram title="PMV-PPD Relationship" >}}
graph LR
    A[-3 PMV<br/>100% PPD] --> B[0 PMV<br/>5% PPD]
    B --> C[+3 PMV<br/>100% PPD]
    B -.->|Optimal| B
    style B fill:#4f4,stroke:#333
    style A fill:#f44,stroke:#333
    style C fill:#f44,stroke:#333
{{< /diagram >}}

**Key Finding:** Even at PMV = 0 (neutral), PPD = 5%
- Individual differences in thermal preference
- Minimum achievable dissatisfaction

## Input Parameters

### Metabolic Rate

{{< table title="Typical Metabolic Rates" >}}
| Activity | Met | W/m² |
|----------|-----|------|
| **Sleeping** | 0.7 | 40 |
| **Seated, quiet** | 1.0 | 58 |
| **Standing, relaxed** | 1.2 | 70 |
| **Office work** | 1.2 | 70 |
| **Walking, 3.2 km/h** | 2.0 | 116 |
| **Light exercise** | 3.0 | 175 |
| **Heavy work** | 4.0 | 232 |
{{< /table >}}

Body surface area (DuBois equation):

{{< formula display="true" >}}
A_D = 0.202 m^{0.425} h^{0.725}
{{< /formula >}}

Where:
- $m$ = body mass (kg)
- $h$ = height (m)
- $A_D$ = surface area (m²)

### Clothing Insulation

{{< table title="Clothing Insulation Values" >}}
| Ensemble | Icl (clo) | Icl (m²K/W) |
|----------|-----------|-------------|
| **Nude** | 0 | 0 |
| **Shorts** | 0.1 | 0.016 |
| **Typical summer** | 0.5 | 0.078 |
| **Light business suit** | 1.0 | 0.155 |
| **Typical winter** | 1.5 | 0.233 |
| **Heavy winter** | 2.0 | 0.310 |
{{< /table >}}

Conversion: 1 clo = 0.155 m²·K/W

## ASHRAE 55 Compliance

### Acceptable Thermal Environment

**For PMV/PPD Method:**
- $-0.5 \le PMV \le +0.5$ (PPD < 10%)
- Category II: $-0.7 \le PMV \le +0.7$ (PPD < 15%)

### Graphical Comfort Zone

For typical indoor clothing (0.5-1.0 clo) and activity (1.0-1.3 met):

{{< diagram title="ASHRAE 55 Comfort Zone" >}}
graph TD
    A[Winter: 20-23.5°C] --> C[Comfort Zone]
    B[Summer: 23-26°C] --> C
    C --> D[RH: 30-60%]
    C --> E[Air Velocity < 0.2 m/s]
    style C fill:#4f4,stroke:#333
{{< /diagram >}}

### Operative Temperature

The temperature that combines air and radiant effects:

{{< formula display="true" >}}
t_o = \frac{h_r \bar{t}_r + h_c t_a}{h_r + h_c}
{{< /formula >}}

For low air velocities ($v < 0.2$ m/s):

{{< formula display="true" >}}
t_o \approx \frac{\bar{t}_r + t_a}{2}
{{< /formula >}}

## Local Discomfort

### Draft Rating

Percentage of people bothered by draft:

{{< formula display="true" >}}
DR = (34 - t_a)(v - 0.05)^{0.62}(0.37 v Tu + 3.14)
{{< /formula >}}

Where:
- $v$ = local air velocity (m/s)
- $Tu$ = turbulence intensity (%)

**Limit:** DR < 15% for comfort

### Vertical Air Temperature Difference

Between ankle (0.1 m) and head (1.1 m):

{{< formula display="true" >}}
\Delta t_{vertical} = t_{head} - t_{ankle}
{{< /formula >}}

**Limit:** $\Delta t_{vertical} < 3°C$

### Floor Surface Temperature

Acceptable range for bare feet or light footwear:

**Limit:** 19°C < $t_{floor}$ < 29°C

### Radiant Asymmetry

Warm ceiling / cool wall asymmetry:

**Limit:** $\Delta t_r < 5°C$ (warm ceiling)

## Adaptive Comfort Model

For naturally ventilated buildings, occupants adapt to outdoor conditions:

{{< formula display="true" >}}
t_{comf} = 0.31 t_{rm(out)} + 17.8
{{< /formula >}}

Where:
- $t_{comf}$ = comfort temperature (°C)
- $t_{rm(out)}$ = running mean outdoor temperature (°C)

Running mean calculation:

{{< formula display="true" >}}
t_{rm} = \frac{t_{od-1} + 0.8 t_{od-2} + 0.6 t_{od-3} + 0.5 t_{od-4} + \ldots}{1 + 0.8 + 0.6 + 0.5 + \ldots}
{{< /formula >}}

**80% Acceptability Limits:** $t_{comf} \pm 3.5°C$

{{< diagram title="Adaptive vs Static Comfort" >}}
graph LR
    A[Outdoor Temp<br/>Rising] --> B[Adaptive Model<br/>Higher Setpoint]
    A --> C[PMV Model<br/>Fixed Setpoint]
    B -.->|Energy Savings| D[20-30%]
    style B fill:#4f4,stroke:#333
    style C fill:#f99,stroke:#333
{{< /diagram >}}

## Practical Application

### Design Workflow

1. **Specify Design Conditions:**
   - Activity level (met)
   - Clothing insulation (clo)
   - Acceptable PMV range

2. **Calculate Required Environment:**
   - Solve PMV equation for $t_a$ and $\bar{t}_r$
   - Check local discomfort criteria
   - Verify humidity constraints

3. **System Design:**
   - Size HVAC to maintain calculated conditions
   - Control strategy for operative temperature
   - Prevent drafts and stratification

### Example Calculation

**Given:**
- Activity: Office work (1.2 met = 70 W/m²)
- Clothing: Business suit (1.0 clo = 0.155 m²K/W)
- Target: PMV = 0
- Relative humidity: 50%
- Air velocity: 0.1 m/s

**Find:** Required air temperature if $\bar{t}_r = t_a$

**Solution:**
Using iterative PMV solver:

{{< formula display="true" >}}
t_a = 22.5°C \text{ yields PMV } \approx 0
{{< /formula >}}

At this condition: PPD = 5%

### Seasonal Adjustment

**Winter:**
- Clothing: 1.0 clo
- Comfort range: 20-23.5°C

**Summer:**
- Clothing: 0.5 clo
- Comfort range: 23-26°C

**Energy Saving:** 3°C setpoint difference reduces HVAC energy by 15-25%

## Advanced Considerations

### Individual Control

Personal comfort systems (PCS) improve satisfaction:
- Desk fans
- Task lighting with radiant component
- Localized heating/cooling

**Impact:** Can extend acceptable temperature range by ±2.5°C

### Transient Conditions

Dynamic thermal comfort models account for:
- Thermal history
- Rate of temperature change
- Intermittent occupancy

**Guideline:** Temperature ramp rate < 0.5°C/hour

### Humidity Effects

While not direct PMV input, humidity affects:
- Evaporative heat loss
- Perceived air quality
- Mold/condensation risk

**Recommended Range:** 30% < RH < 60%

## Measurement and Verification

### Required Sensors

- Air temperature: ±0.5°C accuracy
- Globe temperature: For radiant measurement
- Air velocity: ±0.05 m/s (anemometer)
- Humidity: ±5% RH

### Operative Temperature Measurement

Using black globe thermometer:

{{< formula display="true" >}}
t_o = \frac{(t_g + 273)^4 + 2.5 \times 10^8 v^{0.6}(t_g - t_a)}{1 + 2.5 \times 10^8 v^{0.6} / (t_g + 273)^3} - 273
{{< /formula >}}

Where $t_g$ = globe temperature (°C)

## Conclusion

Thermal comfort analysis provides quantitative design targets for HVAC systems. The PMV/PPD model, validated across diverse populations and climates, predicts thermal sensation from measurable environmental and personal parameters.

Key design principles:
- Target PMV between -0.5 and +0.5 for 90% satisfaction
- Control operative temperature, not just air temperature
- Address local discomfort factors (draft, asymmetry, stratification)
- Consider adaptive opportunities in naturally ventilated spaces

Proper application of thermal comfort standards balances occupant satisfaction with energy efficiency, supporting both human productivity and sustainability goals.

---

*Technical content by Evgeniy Gantman, HVAC Research Engineer*
