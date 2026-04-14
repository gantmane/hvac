---
title: "Extended Surfaces"
aliases: ["Extended Surfaces"]
weight: 3
---

Extended surfaces (fins) enhance heat transfer by increasing the surface area available for convection. Common applications include air-cooled heat exchangers, electronic cooling, HVAC coils, and radiators.

## Fundamental Principles

### Fin Equation

The general differential equation governing fin heat transfer:

$$\frac{d^2T}{dx^2} - m^2(T - T_\infty) = 0$$

Where:
- m² = hP/(kAc) for uniform cross-section fins
- P = fin perimeter (m)
- Ac = cross-sectional area (m²)
- k = thermal conductivity (W/m·K)
- h = convection coefficient (W/m²·K)

### Fin Parameter

The fin parameter m determines fin behavior:

$$m = \sqrt{\frac{hP}{kA_c}}$$

**Physical significance:**
- High m: steep temperature gradient, ineffective fin
- Low m: gradual temperature gradient, effective fin
- Units: m⁻¹

## Fin Efficiency

Fin efficiency compares actual heat transfer to ideal heat transfer if the entire fin were at base temperature.

$$\eta_f = \frac{Q_{actual}}{Q_{ideal}} = \frac{Q_{actual}}{hA_{fin}(T_b - T_\infty)}$$

### Rectangular Fin Efficiency

For a straight rectangular fin (constant cross-section):

$$\eta_f = \frac{\tanh(mL)}{mL}$$

Where L = fin length from base to tip.

**Corrected length** (accounts for tip heat loss):

$$L_c = L + \frac{t}{2}$$

For thin fins where t << L, use:

$$\eta_f = \frac{\tanh(mL_c)}{mL_c}$$

### Circular Fin Efficiency

For annular fins (constant thickness):

$$\eta_f = \frac{2r_1}{r_2^2 - r_1^2} \cdot \frac{K_1(mr_1)I_1(mr_2) - I_1(mr_1)K_1(mr_2)}{I_0(mr_1)K_1(mr_2) + K_0(mr_1)I_1(mr_2)}$$

Where:
- r₁ = tube outer radius (m)
- r₂ = fin outer radius (m)
- I, K = modified Bessel functions

**Simplified approximation** for r₂/r₁ < 2:

$$\eta_f \approx \frac{\tanh(mL_e)}{mL_e}$$

Where equivalent length Le = r₂ - r₁.

### Triangular and Parabolic Fins

**Triangular fin** (thickness varies linearly to zero at tip):

$$\eta_f = \frac{1}{mL} \cdot \frac{I_1(2mL)}{I_0(2mL)}$$

**Parabolic fin** (optimized profile):

$$\eta_f = \frac{2}{1 + \sqrt{1 + (2mL)^2}}$$

## Fin Efficiency Table

| Fin Geometry | Efficiency Equation | Typical η_f Range |
|--------------|---------------------|-------------------|
| Rectangular, insulated tip | tanh(mL)/(mL) | 0.65 - 0.95 |
| Rectangular, convection tip | tanh(mL_c)/(mL_c) | 0.60 - 0.93 |
| Triangular | I₁(2mL)/[mL·I₀(2mL)] | 0.70 - 0.98 |
| Parabolic | 2/[1+√(1+(2mL)²)] | 0.75 - 0.99 |
| Pin fin (cylindrical) | tanh(mL+D/4)/(mL+D/4) | 0.55 - 0.90 |
| Annular (circular) | Complex Bessel function | 0.60 - 0.92 |

## Fin Effectiveness

Fin effectiveness compares heat transfer with fin to heat transfer without fin.

$$\varepsilon_f = \frac{Q_{with\,fin}}{Q_{without\,fin}} = \frac{Q_{fin}}{hA_b(T_b - T_\infty)}$$

For a straight fin with insulated tip:

$$\varepsilon_f = \sqrt{\frac{kP}{hA_c}} \cdot \tanh(mL)$$

### Effectiveness Criteria

| Condition | Recommendation |
|-----------|----------------|
| ε_f < 2 | Fin not justified economically |
| ε_f = 2-5 | Marginal benefit, evaluate cost |
| ε_f = 5-20 | Good fin application |
| ε_f > 20 | Excellent fin application |

**Design guideline:** Use high thermal conductivity materials (aluminum, copper) for maximum effectiveness.

## Rectangular Fin Analysis

### Straight Rectangular Fin

**Geometry:**
- Width: W (m)
- Thickness: t (m)
- Length: L (m)
- Ac = W × t
- P = 2(W + t) ≈ 2W for thin fins

**Heat transfer rate:**

$$Q = \sqrt{hPkA_c} \cdot (T_b - T_\infty) \cdot \tanh(mL)$$

### Design Parameters

| Parameter | Aluminum | Copper | Steel |
|-----------|----------|--------|-------|
| k (W/m·K) | 200-240 | 380-400 | 45-60 |
| Typical t (mm) | 0.3-1.5 | 0.4-1.2 | 0.5-2.0 |
| Typical spacing (mm) | 1.5-4.0 | 2.0-5.0 | 2.5-6.0 |
| Max operating temp (°C) | 200 | 250 | 400 |

## Circular Fin Analysis

### Annular Fin on Tube

**Configuration:**
- Tube outer diameter: D₀
- Fin outer diameter: D_f
- Fin thickness: t
- Fin spacing: s

**Heat dissipation per fin:**

$$Q = 2\pi r_1 kt(T_b - T_\infty) \cdot m \cdot \eta_f \cdot \phi$$

Where φ is a dimensionless parameter from Bessel function solution.

### Circular Fin Optimization

**Optimal fin spacing** (natural convection):

$$s_{opt} = 2.714 \cdot L \cdot \left(\frac{Ra_L}{4}\right)^{-0.25}$$

Where Ra_L is Rayleigh number based on fin height.

## Heat Sink Design

### Overall Surface Efficiency

For a finned surface with N fins:

$$\eta_o = 1 - \frac{N \cdot A_{fin}}{A_{total}}(1 - \eta_f)$$

Where:
- A_total = total heat transfer area (base + fins)
- A_fin = surface area of single fin

**Total heat transfer rate:**

$$Q_{total} = h \cdot A_{total} \cdot \eta_o \cdot (T_b - T_\infty)$$

### Heat Sink Performance Parameters

| Heat Sink Type | Thermal Resistance (°C/W) | Fin Density (fins/inch) |
|----------------|---------------------------|-------------------------|
| Extruded aluminum | 0.05 - 0.5 | 8 - 20 |
| Bonded fin | 0.1 - 0.8 | 6 - 15 |
| Stamped | 0.3 - 1.5 | 5 - 12 |
| Pin fin array | 0.2 - 1.0 | 20 - 40 pins/in² |

### Thermal Resistance

The total thermal resistance from junction to ambient:

$$R_{total} = R_{junction-case} + R_{contact} + R_{sink}$$

Heat sink resistance:

$$R_{sink} = \frac{1}{h \cdot A_{total} \cdot \eta_o}$$

## HVAC Coil Fin Analysis

### Plate Fin Coils

**Typical specifications:**
- Fin spacing: 8-20 fins per inch (FPI)
- Fin thickness: 0.1-0.15 mm aluminum
- Tube diameter: 7-10 mm
- Row depth: 2-8 rows

**Fin efficiency for plate fins on round tubes:**

$$\eta_f = \frac{\tanh(m \cdot r_{eq} \cdot \phi)}{m \cdot r_{eq} \cdot \phi}$$

Where:
- r_eq = equivalent radius = 0.5 × (fin spacing)
- φ = correction factor from charts (typically 0.8-1.0)

### Coil Surface Effectiveness

**Air-side heat transfer:**

$$Q = h_o \cdot A_o \cdot \eta_o \cdot LMTD$$

Where:
- h₀ = outside convection coefficient (W/m²·K)
- A₀ = total outside surface area (m²)
- LMTD = log mean temperature difference

### Fin Spacing Selection

| Application | FPI | Fin Thickness (mm) | η_f |
|-------------|-----|-------------------|-----|
| Clean air | 14-20 | 0.10-0.12 | 0.85-0.92 |
| Standard comfort cooling | 10-14 | 0.12-0.15 | 0.88-0.94 |
| Dirty environments | 6-10 | 0.15-0.20 | 0.90-0.95 |
| Frosting applications | 6-8 | 0.15-0.20 | 0.92-0.96 |

Higher FPI increases surface area but decreases air-side heat transfer coefficient due to increased pressure drop and reduced flow area.

## Fin Parameter Equations

### Dimensionless Groups

**Biot number for fins:**

$$Bi_f = \frac{hL_c}{k}$$

Represents ratio of conduction resistance to convection resistance.

**Fin length parameter:**

$$mL = L\sqrt{\frac{hP}{kA_c}}$$

**Critical fin length** (beyond which additional length adds negligible heat transfer):

$$L_{crit} = \frac{2.3}{m}$$

For mL > 2.3, tanh(mL) ≈ 1.0, and additional length is wasteful.

## Optimization Strategies

### Mass Optimization

For a given heat duty Q and material volume V:

**Rectangular fin optimum thickness:**

$$t_{opt} = \sqrt{\frac{2k}{h}}$$

**Optimum fin spacing** (vertical plate array, natural convection):

$$s_{opt} = 2.714 \cdot \left(\frac{L}{Ra_s^{0.25}}\right)$$

### Cost-Performance Optimization

**Performance index:**

$$PI = \frac{Q}{Cost} = \frac{\eta_f \cdot A_{fin} \cdot h \cdot \Delta T}{\rho \cdot V \cdot C_{material}}$$

Where:
- ρ = material density (kg/m³)
- V = fin volume (m³)
- C_material = material cost ($/kg)

### Material Selection Criteria

| Material | k (W/m·K) | Cost Index | √(k/ρC) | Application |
|----------|-----------|------------|---------|-------------|
| Copper | 400 | 10 | 9.5 | High performance, small size |
| Aluminum 6063 | 200 | 3 | 8.2 | General HVAC, cost-effective |
| Aluminum 1100 | 220 | 2.5 | 8.6 | Best value for performance |
| Steel | 50 | 1 | 2.8 | High temperature only |

The parameter √(k/ρC) represents thermal performance per unit cost.

## Design Procedure

1. **Calculate required heat transfer rate** Q from thermal load
2. **Estimate convection coefficient** h based on fluid, velocity, geometry
3. **Select fin material** based on temperature, corrosion, cost
4. **Calculate fin parameter** m = √(hP/kAc)
5. **Determine fin efficiency** η_f from appropriate equation
6. **Calculate overall surface efficiency** η_o
7. **Size fin array** to achieve Q = hA_total·η_o·ΔT
8. **Check constraints:** spacing, pressure drop, manufacturability
9. **Optimize** if needed for cost, weight, or volume

## Performance Degradation

### Fouling Effects

Fouling reduces effective fin efficiency:

$$\eta_{f,fouled} = \eta_f \cdot \frac{h_{clean}}{h_{fouled}}$$

Typical fouling factors for HVAC coils: 0.85-0.95 after 1 year of operation.

### Contact Resistance

For bonded or press-fit fins, contact resistance R_c reduces performance:

$$\eta_{effective} = \eta_f \cdot \frac{1}{1 + \frac{R_c \cdot k \cdot t}{A_c}}$$

Thermal greases or brazing eliminate contact resistance.
