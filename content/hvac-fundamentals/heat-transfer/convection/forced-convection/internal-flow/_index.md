---
title: "Internal Flow"
weight: 2
---

Internal forced convection governs heat transfer in pipes, ducts, and tubes where fluid flows through enclosed channels. This regime is fundamental to HVAC applications including hydronic piping, refrigerant lines, air distribution systems, and heat exchangers.

## Flow Development Regions

### Hydrodynamic Entry Length

The distance required for the velocity profile to fully develop from a uniform inlet condition to the characteristic parabolic (laminar) or logarithmic (turbulent) profile.

**Laminar flow:**
```
Lh,lam / D = 0.05 Re
```

**Turbulent flow:**
```
Lh,turb / D = 10 to 60
```

Where:
- Lh = hydrodynamic entry length (ft or m)
- D = pipe diameter (ft or m)
- Re = Reynolds number (dimensionless)

### Thermal Entry Length

The distance required for the temperature profile to become fully developed after thermal conditions are imposed.

**Laminar flow:**
```
Lt,lam / D = 0.05 Re Pr
```

**Turbulent flow:**
```
Lt,turb / D = 10 to 60
```

Where:
- Lt = thermal entry length (ft or m)
- Pr = Prandtl number (dimensionless)

### Flow Region Characteristics

| Region | Velocity Profile | Temperature Profile | Heat Transfer Coefficient |
|--------|------------------|---------------------|---------------------------|
| Entrance region | Developing | Developing | Higher than fully developed |
| Fully developed | Constant shape | Constant shape | Uniform along length |
| Transition | Variable | Variable | Position-dependent |

## Laminar Internal Flow

### Fully Developed Laminar Flow

For constant surface temperature (Re < 2300):

```
Nu_D = 3.66  (circular tube, constant Ts)
```

For constant heat flux:

```
Nu_D = 4.36  (circular tube, constant q")
```

### Laminar Entry Region

The Sieder-Tate correlation accounts for developing flow:

```
Nu_D = 1.86 (Re Pr D/L)^(1/3) (μ/μs)^0.14
```

Valid for:
- 0.48 < Pr < 16,700
- 0.0044 < (μ/μs) < 9.75
- Re Pr D/L > 10

Where:
- μ = dynamic viscosity at bulk temperature (lbm/(ft·h) or Pa·s)
- μs = dynamic viscosity at surface temperature (lbm/(ft·h) or Pa·s)
- L = tube length (ft or m)

## Turbulent Internal Flow

### Dittus-Boelter Equation

The most widely used correlation for turbulent flow in smooth tubes:

```
Nu_D = 0.023 Re^0.8 Pr^n
```

Where:
- n = 0.4 for heating (Ts > Tb)
- n = 0.3 for cooling (Ts < Tb)

**Validity range:**
- Re > 10,000
- 0.7 ≤ Pr ≤ 160
- L/D ≥ 10 (fully developed flow)
- Smooth tubes

**Application example:**

For water at 60°F flowing through a 2-inch pipe at 6 ft/s:
- Re = 125,000 (turbulent)
- Pr = 7.0
- For heating: Nu = 0.023 (125,000)^0.8 (7.0)^0.4 = 520
- h = Nu k / D = 520 × 0.34 / (2/12) = 1060 Btu/(h·ft²·°F)

### Gnielinski Correlation

More accurate than Dittus-Boelter, valid for a wider range of conditions:

```
Nu_D = [(f/8)(Re - 1000)Pr] / [1 + 12.7(f/8)^0.5 (Pr^(2/3) - 1)]
```

Where f is the Darcy friction factor:

```
f = (0.790 ln Re - 1.64)^-2  (smooth tubes)
```

**Validity range:**
- 3000 ≤ Re ≤ 5 × 10^6
- 0.5 ≤ Pr ≤ 2000
- Accounts for transition regime

**Advantages over Dittus-Boelter:**
- Valid in transition regime (2300 < Re < 10,000)
- Better accuracy for wide Pr range
- Accounts for friction factor explicitly
- Better for moderate Reynolds numbers

### Comparison of Turbulent Correlations

| Correlation | Re Range | Pr Range | Typical Error | Application |
|-------------|----------|----------|---------------|-------------|
| Dittus-Boelter | >10,000 | 0.7-160 | ±25% | Quick estimates, water/air |
| Gnielinski | 3,000-5×10^6 | 0.5-2000 | ±10% | General purpose, wide range |
| Sieder-Tate | >10,000 | 0.7-16,700 | ±20% | Variable viscosity fluids |
| Petukhov | 10^4-5×10^6 | 0.5-2000 | ±6% | High accuracy required |

## Property Evaluation

All fluid properties should be evaluated at the bulk mean temperature unless otherwise specified:

```
Tb = (Ti + To) / 2
```

Where:
- Tb = bulk mean temperature (°F or °C)
- Ti = inlet temperature (°F or °C)
- To = outlet temperature (°F or °C)

For variable property effects, use the Sieder-Tate viscosity ratio correction:

```
Nu_corrected = Nu × (μb/μs)^0.14
```

## Heat Transfer Calculations

### Heat Transfer Rate

```
Q = h A ΔTlm
```

Where:
- Q = heat transfer rate (Btu/h or W)
- h = convection coefficient (Btu/(h·ft²·°F) or W/(m²·K))
- A = surface area = π D L (ft² or m²)
- ΔTlm = log mean temperature difference (°F or K)

### Log Mean Temperature Difference

```
ΔTlm = (ΔTi - ΔTo) / ln(ΔTi / ΔTo)
```

Where:
- ΔTi = Ts - Ti (temperature difference at inlet)
- ΔTo = Ts - To (temperature difference at outlet)

### Outlet Temperature Calculation

For constant surface temperature:

```
To = Ts - (Ts - Ti) exp(-hA / ṁcp)
```

Where:
- ṁ = mass flow rate (lbm/h or kg/s)
- cp = specific heat (Btu/(lbm·°F) or J/(kg·K))

## Noncircular Ducts

For rectangular and other noncircular cross-sections, use hydraulic diameter:

```
Dh = 4Ac / P
```

Where:
- Dh = hydraulic diameter (ft or m)
- Ac = cross-sectional area (ft² or m²)
- P = wetted perimeter (ft or m)

### Hydraulic Diameter Examples

| Duct Shape | Dimensions | Hydraulic Diameter |
|------------|------------|-------------------|
| Circular | Diameter D | Dh = D |
| Rectangular | Width a, Height b | Dh = 2ab / (a + b) |
| Square | Side a | Dh = a |
| Annulus | Di, Do | Dh = Do - Di |

**Rectangular duct example:**

For a 12" × 8" duct:
```
Dh = 2(12)(8) / (12 + 8) = 9.6 inches
```

### Noncircular Duct Corrections

For laminar flow in rectangular ducts, Nusselt numbers depend on aspect ratio:

| Aspect Ratio (a/b) | Nu (constant Ts) | Nu (constant q") |
|-------------------|------------------|------------------|
| 1.0 (square) | 2.98 | 3.61 |
| 1.43 | 3.08 | 3.73 |
| 2.0 | 3.39 | 4.12 |
| 4.0 | 4.44 | 5.33 |
| 8.0 | 5.60 | 6.49 |
| ∞ (parallel plates) | 7.54 | 8.23 |

For turbulent flow, use standard correlations with Dh, but apply a correction factor:

```
Nu_rect = Nu_circular × 0.95  (typical)
```

## Concentric Tube Annulus

For flow in the annular space between concentric tubes, use hydraulic diameter based on inner (Di) and outer (Do) diameters:

```
Dh = Do - Di
```

### Annular Flow Nusselt Numbers

**Laminar flow with constant heat flux:**

Inner tube heated, outer insulated: Nu = 4.86
Outer tube heated, inner insulated: Nu = 4.86
Both surfaces heated equally: Nu = 5.65

**Turbulent flow:**

Use Dittus-Boelter or Gnielinski with Dh, but verify L/Dh > 60 for fully developed flow.

## Entrance Region Effects

Heat transfer coefficients are higher in the entrance region due to thinner boundary layers.

### Average Nusselt Number for Entrance Region

```
Nu_avg = Nu_fd [1 + (C / (L/D))]
```

Where:
- Nu_fd = fully developed Nusselt number
- C = constant (≈ 0.1 for turbulent flow)
- L/D = length-to-diameter ratio

For short tubes (L/D < 10), entrance effects dominate and specific entrance correlations must be used.

## HVAC Applications

### Chilled Water Piping

Typical conditions:
- Velocity: 4-8 ft/s
- Temperature: 40-55°F
- Re: 50,000-200,000 (turbulent)
- Use Dittus-Boelter or Gnielinski

### Air Ducts

Typical conditions:
- Velocity: 800-2000 fpm
- Temperature: 55-75°F
- Re: 10,000-100,000 (turbulent)
- Use hydraulic diameter for rectangular ducts

### Refrigerant Lines

Considerations:
- Two-phase flow requires different correlations
- Superheated vapor: use single-phase correlations
- Subcooled liquid: use single-phase correlations
- Property variation significant: use Sieder-Tate correction

## Design Considerations

1. **Verify flow regime**: Calculate Re to determine laminar or turbulent
2. **Check entry length**: Determine if flow is developing or fully developed
3. **Select appropriate correlation**: Match to Re, Pr, and geometry
4. **Evaluate properties**: Use bulk temperature unless correction required
5. **Account for fouling**: Apply fouling resistance in series with convection resistance
6. **Consider pressure drop**: Higher velocities increase h but also increase pumping power
