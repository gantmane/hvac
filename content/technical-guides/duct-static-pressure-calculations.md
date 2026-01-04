---
title: "Duct Static Pressure Calculations for HVAC Engineers"
description: "Friction loss calculations, fitting equivalent lengths, total pressure drop analysis, and fan static pressure determination for duct system design."
keywords: ["static pressure", "duct pressure drop", "friction loss", "fitting losses", "fan static pressure", "total pressure"]
author: "Evgeniy Gantman"
date: 2026-01-04
weight: 21
---

# Duct Static Pressure Calculations for HVAC Engineers

Accurate pressure drop calculations enable proper fan selection and energy-efficient duct sizing. Underprediction causes inadequate airflow; overprediction wastes fan energy and first cost.

## Total Pressure Components

$$P_{total} = P_{static} + P_{velocity}$$

**Velocity pressure:**

$$P_v = \left(\frac{v}{4005}\right)^2 \text{ "w.g.}$$

**Fan static pressure:**

$$FSP = P_{s,discharge} - P_{s,suction}$$

## Friction Pressure Loss

**Darcy-Weisbach equation:**

$$\Delta P_f = f \frac{L}{D} \frac{v^2}{(4005)^2 \times 12.96}$$

Where:
- $f$ = friction factor (from Moody chart or Colebrook equation)
- $L$ = duct length (ft)
- $D$ = hydraulic diameter (ft)
- $v$ = velocity (FPM)

**For rectangular ducts, hydraulic diameter:**

$$D_h = \frac{4ab}{2(a+b)} = \frac{2ab}{a+b}$$

**Alternative:** Use duct friction chart (equal friction method)
- Select friction rate: 0.08-0.15 "w.g./100 ft
- Find duct size for given CFM at selected friction rate

## Fitting Losses

**Local loss coefficient method:**

$$\Delta P_{fitting} = C \times P_v$$

Where $C$ = loss coefficient from ASHRAE Duct Fitting Database

**Common fittings:**

| Fitting | Loss Coefficient C |
|---------|-------------------|
| 90° elbow, R/D = 1.5 | 0.15-0.25 |
| 90° elbow, mitered | 0.8-1.3 |
| Branch tee, straight | 0.10-0.15 |
| Branch tee, 90° branch | 0.9-1.8 |
| Damper, fully open | 0.2-0.5 |
| Filter (clean MERV 8) | 0.3-0.5 |

**Total system pressure drop:**

$$\Delta P_{total} = \Delta P_{straight} + \sum \Delta P_{fittings} + \Delta P_{equipment}$$

## System Effect Factors

**Common causes of system effect:**
1. Inlet/outlet obstructions near fan
2. Elbows within 3 duct diameters of fan
3. Inadequate fan inlet duct length
4. Non-uniform velocity profile at fan inlet

**Impact:** Can increase required fan pressure by 0.25-1.0 "w.g.

**Prevention:**
- Straight duct runs: 2.5D upstream, 5D downstream of fan
- Turning vanes in elbows near fan
- Inlet/outlet bell mouths

## Design Pressure Drops

**Target static pressure:**
- Low-velocity systems: 0.5-1.5 "w.g.
- Medium-velocity systems: 1.5-3.0 "w.g.
- High-velocity systems: 3.0-6.0 "w.g.

**Component breakdown:**
- Straight duct (40-50%)
- Fittings (25-35%)
- Coil/filter (15-25%)
- Terminals/diffusers (5-15%)

## Practical Applications

1. **Equal friction design:** Select 0.10 "w.g./100 ft, size all ducts at this rate
2. **Available static method:** Work backwards from fan capacity
3. **System curve:** Plot $\Delta P$ vs. CFM to find operating point

---

**Related Technical Guides:**
- [Fluid Mechanics for HVAC](/technical-guides/fluid-mechanics-hvac/)
- [Duct Design Fundamentals](/technical-guides/duct-design-fundamentals/)
- [Fan Selection & Performance](/technical-guides/fan-selection-performance/)

**References:**
- ASHRAE Handbook of Fundamentals, Chapter 21: Duct Design
- ASHRAE Duct Fitting Database
- SMACNA HVAC Systems Duct Design, 4th Edition
