---
title: "Duct Losses in Industrial Exhaust Systems"
aliases: ["Duct Losses in Industrial Exhaust Systems"]
seo_title: "Duct Pressure Loss Calculation Methods & Coefficients"
description: "Calculate duct friction and fitting losses in industrial local exhaust systems using ASHRAE and ACGIH methods. Includes loss coefficients, formulas, and design tables."
keywords: ["duct friction loss", "fitting loss coefficient", "pressure drop calculation", "Darcy-Weisbach equation", "industrial exhaust design", "duct velocity pressure", "ASHRAE duct design", "ACGIH ventilation"]
tags: ["duct friction loss", "fitting loss coefficient", "pressure drop calculation", "Darcy-Weisbach equation", "industrial exhaust design", "duct velocity pressure", "ASHRAE duct design", "ACGIH ventilation"]
weight: 3
---

Pressure losses in industrial exhaust ductwork consume fan energy and determine the required static pressure capability of the ventilation system. These losses arise from two distinct mechanisms: friction between the air stream and duct walls, and turbulent dissipation in fittings such as elbows, transitions, and branch entries.

## Physical Principles of Duct Losses

Air flowing through a duct experiences resistance due to viscous shear at the boundary layer and form drag from flow separation. The total pressure loss represents irreversible conversion of mechanical energy to thermal energy through turbulent dissipation.

For fully developed turbulent flow in circular ducts, the Darcy-Weisbach equation governs friction losses:

$$\Delta P_f = f \cdot \frac{L}{D} \cdot \frac{\rho V^2}{2} = f \cdot \frac{L}{D} \cdot VP$$

Where:
- $\Delta P_f$ = friction pressure loss (Pa or in. w.g.)
- $f$ = Darcy friction factor (dimensionless)
- $L$ = duct length (m or ft)
- $D$ = duct diameter (m or ft)
- $\rho$ = air density (kg/m³ or lb/ft³)
- $V$ = air velocity (m/s or ft/min)
- $VP$ = velocity pressure = $\frac{\rho V^2}{2}$ (Pa or in. w.g.)

The friction factor depends on Reynolds number and relative roughness. For typical industrial exhaust ductwork (galvanized steel, $\epsilon/D \approx 0.0005$), the friction factor ranges from 0.015 to 0.025 for Reynolds numbers between 10,000 and 100,000.

```mermaid
graph LR
    A[Fan Discharge] -->|Straight Duct| B[Friction Loss ΔPf]
    B -->|Elbow| C[Fitting Loss ΔPfit]
    C -->|Transition| D[Fitting Loss ΔPfit]
    D -->|Branch Entry| E[Fitting Loss ΔPfit]
    E -->|Straight Duct| F[Friction Loss ΔPf]
    F -->|Hood Entry| G[Total Pressure Loss]

    style B fill:#e1f5ff
    style C fill:#fff4e1
    style D fill:#fff4e1
    style E fill:#fff4e1
    style F fill:#e1f5ff

    subgraph "Pressure Loss Components"
    B
    C
    D
    E
    F
    end
```

## Fitting Losses

Fittings generate localized turbulence and flow separation, resulting in pressure losses expressed as multiples of velocity pressure:

$$\Delta P_{fit} = C_L \cdot VP$$

Where $C_L$ is the loss coefficient (dimensionless), determined experimentally for each fitting geometry.

### Loss Coefficients by Fitting Type

| Fitting Type | Configuration | Loss Coefficient (CL) | Notes |
|--------------|--------------|----------------------|-------|
| **Elbows** | 90° smooth radius (r/D = 1.5) | 0.22 | Minimum loss configuration |
| | 90° smooth radius (r/D = 1.0) | 0.35 | Standard industrial elbow |
| | 90° mitered, no vanes | 1.20 | High loss, avoid if possible |
| | 90° mitered, with turning vanes | 0.40 | Vanes reduce separation |
| | 45° elbow (r/D = 1.5) | 0.15 | Lower angle reduces loss |
| **Transitions** | Gradual expansion (10° included angle) | 0.18 | Optimal expansion rate |
| | Gradual expansion (20° included angle) | 0.40 | Increased separation |
| | Abrupt expansion | 1.00 | Complete velocity head loss |
| | Gradual contraction (any angle) | 0.05 | Minimal loss in contraction |
| **Branch Entries** | 45° entry, tapered | 0.15 | Best practice design |
| | 90° straight entry | 0.50 | Moderate loss |
| | Straight-through tee | 0.90 | Significant separation |
| **Hood Entries** | Bell mouth entry | 0.05 | Smooth acceleration |
| | Plain opening | 0.50 | Standard hood entry |
| | Inward flange | 0.93 | Poor entry geometry |

**Source:** ACGIH Industrial Ventilation Manual, 30th Edition; ASHRAE Fundamentals Handbook

## Calculation Methods

### ASHRAE Method

ASHRAE provides friction loss charts (Duct Friction Chart, Chapter 21) based on the Colebrook equation for commercial duct systems. For round galvanized ducts at standard air density (0.075 lb/ft³), the chart relates friction loss per 100 ft to duct diameter and airflow rate.

For rectangular ducts, convert to equivalent circular diameter:

$$D_e = 1.30 \cdot \frac{(a \cdot b)^{0.625}}{(a + b)^{0.25}}$$

Where $a$ and $b$ are the rectangular duct dimensions.

### ACGIH Method

The ACGIH Industrial Ventilation Manual emphasizes velocity pressure losses for industrial exhaust systems containing particulate. The total system loss calculation proceeds:

1. Calculate velocity pressure at each duct segment: $VP = \frac{V^2}{4005}$ (in. w.g., V in ft/min)
2. Determine friction loss: $\Delta P_f = f \cdot (L/D) \cdot VP$
3. Sum fitting losses: $\Sigma \Delta P_{fit} = \Sigma (C_L \cdot VP)$
4. Total static pressure requirement: $SP_{total} = \Sigma \Delta P_f + \Sigma \Delta P_{fit} + SP_{hood}$

## Design Considerations

**Velocity Selection:** Industrial exhaust systems require minimum transport velocities to prevent particulate settling. Typical ranges:

- Vapor, gases: 1000-2000 ft/min
- Light dust: 2000-3000 ft/min
- Heavy dust, metal chips: 3500-4500 ft/min

Higher velocities increase pressure losses (proportional to $V^2$), creating tension between transport requirements and energy consumption.

**Duct Roughness:** Particulate buildup increases effective roughness and friction factor over time. Design should include cleanout provisions and anticipate 10-20% pressure loss increase during service intervals.

**Balancing:** Branch systems require careful fitting selection to achieve design airflows without damper losses. Blast gate dampers introduce high losses ($C_L$ = 0.5-2.0 depending on position) and should be sized for minimal restriction in the open position.

## Pressure Loss Budget

For efficient system design, allocate the total fan static pressure capability:

- Hood entry loss: 10-15%
- Duct friction losses: 40-50%
- Fitting losses: 25-35%
- Filter or air cleaner: 10-25%
- Reserve for system degradation: 10-15%

This allocation ensures adequate capture velocity at hoods while limiting fan energy consumption to practical levels for continuous industrial operation.
