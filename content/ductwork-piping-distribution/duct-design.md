---
title: "Ductwork Design and Sizing for HVAC Systems"
description: "Comprehensive technical analysis of duct sizing methods, pressure loss calculations, fitting coefficients, and design standards for HVAC distribution systems with practical examples and formulas."
keywords: ["duct design", "duct sizing", "equal friction method", "static regain", "pressure loss", "fitting loss coefficients", "HVAC ductwork", "duct velocity", "aspect ratio", "branch takeoff design"]
categories: ["HVAC Design", "Ductwork and Piping", "Air Distribution"]
tags: ["duct sizing", "pressure loss", "equal friction", "static regain", "duct design", "ASHRAE", "SMACNA"]
author: "Evgeniy Gantman"
date: 2026-01-04
draft: false
---

## Introduction

Duct design represents the systematic application of fluid mechanics principles to air distribution systems. The objective is to deliver specified airflow rates to each terminal device while minimizing energy consumption, construction cost, and acoustic emissions. This requires balancing competing constraints: smaller ducts reduce material cost but increase pressure loss and fan energy; larger ducts reduce friction but consume building space and increase initial cost.

The design process involves three fundamental steps: selecting a sizing method, calculating pressure losses through all system components, and verifying that velocities remain within acceptable limits for noise control. Modern duct design integrates thermodynamics (heat transfer through duct walls), fluid mechanics (pressure loss and flow distribution), and acoustics (noise generation and attenuation).

## Fundamental Flow Equations

Air distribution systems operate in the turbulent flow regime (Reynolds number > 4000) under standard conditions. The governing equations derive from conservation principles and empirical correlations for friction factors.

### Continuity Equation

Mass conservation requires:

{{< formula display="true" >}}
$$\dot{m} = \rho A V = \text{constant}$$
{{< /formula >}}

For constant density (incompressible flow assumption valid for duct systems):

{{< formula display="true" >}}
$$Q = A_1 V_1 = A_2 V_2$$
{{< /formula >}}

where:
- $Q$ = volumetric flow rate (cfm or m³/s)
- $A$ = cross-sectional area (ft² or m²)
- $V$ = average velocity (fpm or m/s)
- $\rho$ = air density (lb/ft³ or kg/m³)
- $\dot{m}$ = mass flow rate (lb/s or kg/s)

### Bernoulli Equation with Losses

Energy conservation along a streamline, accounting for friction and minor losses:

{{< formula display="true" >}}
$$\frac{P_1}{\rho} + \frac{V_1^2}{2} + gz_1 = \frac{P_2}{\rho} + \frac{V_2^2}{2} + gz_2 + h_L$$
{{< /formula >}}

For horizontal ducts with negligible elevation change, expressed in pressure units:

{{< formula display="true" >}}
$$P_{s1} + P_{v1} = P_{s2} + P_{v2} + \Delta P_L$$
{{< /formula >}}

where:
- $P_s$ = static pressure (in. wg or Pa)
- $P_v = \rho V^2/2$ = velocity pressure (in. wg or Pa)
- $\Delta P_L$ = total pressure loss (in. wg or Pa)

### Velocity Pressure

The dynamic pressure component resulting from fluid motion:

{{< formula display="true" >}}
$$P_v = \frac{\rho V^2}{2} = \frac{V^2}{4005^2} \text{ (in. wg, standard air)}$$
{{< /formula >}}

For standard air at 70°F and sea level ($\rho$ = 0.075 lb/ft³):

{{< formula display="true" >}}
$$P_v = \left(\frac{V}{4005}\right)^2 \text{ in. wg}$$
{{< /formula >}}

where $V$ is in fpm.

In SI units (air at 20°C, 101.325 kPa, $\rho$ = 1.204 kg/m³):

{{< formula display="true" >}}
$$P_v = \frac{V^2}{2} \times 1.204 = 0.602 V^2 \text{ Pa}$$
{{< /formula >}}

where $V$ is in m/s.

## Duct Sizing Methods

Three primary methods exist for sizing duct systems, each with distinct advantages and applications.

### Equal Friction Method

The equal friction method maintains constant pressure loss per unit length throughout the system. This approach provides balanced design with predictable pressure losses and simplifies manual calculations.

**Design Procedure:**

1. Select friction rate based on system type and noise constraints
2. Size main trunk at selected friction rate
3. Size all branches at the same friction rate
4. Calculate dynamic losses for all fittings
5. Balance system using dampers or resize sections

**Friction Rate Selection:**

Typical friction rates for different applications:

- Low velocity systems: 0.08-0.10 in. wg/100 ft
- Medium velocity residential: 0.10-0.15 in. wg/100 ft
- Commercial systems: 0.15-0.25 in. wg/100 ft
- Industrial systems: 0.25-0.40 in. wg/100 ft

Lower friction rates reduce fan energy but increase duct size and cost. The optimal friction rate minimizes total lifecycle cost (first cost + present value of operating cost).

**Sizing from Friction Chart:**

Given airflow $Q$ (cfm) and friction rate $\Delta P_f$ (in. wg/100 ft):

1. Locate intersection of $Q$ and $\Delta P_f$ on friction chart
2. Read duct diameter or rectangular dimensions
3. Read velocity $V$ (fpm) from chart

**Advantages:**
- Simple to apply manually
- Balanced pressure distribution
- Minimal calculation required
- Good for preliminary sizing

**Disadvantages:**
- Does not minimize first cost or operating cost
- Requires dampers for final balancing
- Static pressure varies through system
- Not optimal for complex systems

### Velocity Method

The velocity method selects duct sizes based on maximum allowable velocities for noise control and energy conservation. This approach directly addresses acoustic constraints.

**Maximum Velocity Recommendations:**

{{< table >}}
| Application | Main Ducts | Branch Ducts | Final Runouts |
|-------------|------------|--------------|---------------|
| Residences | 700-900 fpm | 600-700 fpm | 500-600 fpm |
| Apartments | 1000-1300 fpm | 700-1000 fpm | 600-800 fpm |
| Private offices | 1200-1500 fpm | 800-1200 fpm | 600-800 fpm |
| General offices | 1500-2000 fpm | 1000-1500 fpm | 800-1200 fpm |
| Retail stores | 1500-2200 fpm | 1200-1800 fpm | 1000-1500 fpm |
| Industrial | 2000-3000 fpm | 1500-2200 fpm | 1200-1800 fpm |
{{< /table >}}

**Design Procedure:**

1. Select maximum velocities based on application and location
2. Calculate required area: $A = Q/V$
3. Select standard duct size meeting area requirement
4. Reduce velocity progressively downstream
5. Calculate actual pressure losses
6. Size fan for total system resistance

**Velocity Reduction:**

Progressive velocity reduction through the system maintains acceptable noise levels while optimizing duct size. A typical reduction strategy:

- Main trunk at maximum velocity
- Reduce 100-200 fpm at each major branch
- Terminal branches at minimum recommended velocity

**Advantages:**
- Direct noise control
- Simple conceptual approach
- Suitable for noise-sensitive applications
- No complex calculations required

**Disadvantages:**
- Does not optimize energy or cost
- May result in oversized ducts
- Ignores static pressure recovery
- Conservative approach increases first cost

### Static Regain Method

The static regain method exploits velocity pressure conversion to static pressure as velocity decreases. This approach maintains approximately constant static pressure at each branch takeoff, achieving self-balancing without dampers.

**Physical Principle:**

As air velocity decreases in a reducing trunk, kinetic energy converts to static pressure. The duct section is sized such that the static pressure increase from velocity reduction equals the friction loss in that section:

{{< formula display="true" >}}
$$\Delta P_{v,\text{regain}} = \Delta P_{f,\text{section}} + \Delta P_{\text{fittings}}$$
{{< /formula >}}

**Static Regain Calculation:**

The change in velocity pressure between sections:

{{< formula display="true" >}}
$$\Delta P_v = P_{v1} - P_{v2} = \frac{\rho}{2}(V_1^2 - V_2^2)$$
{{< /formula >}}

For standard air:

{{< formula display="true" >}}
$$\Delta P_v = \left(\frac{V_1}{4005}\right)^2 - \left(\frac{V_2}{4005}\right)^2 \text{ in. wg}$$
{{< /formula >}}

**Regain Factor:**

Not all velocity pressure converts to static pressure due to turbulence and losses. The regain factor $R$ accounts for this inefficiency:

{{< formula display="true" >}}
$$\Delta P_{s,\text{regain}} = R \times \Delta P_v$$
{{< /formula >}}

Typical regain factors:
- Straight duct, gradual reduction: $R$ = 0.75-0.90
- Duct with elbow: $R$ = 0.60-0.75
- Abrupt reduction: $R$ = 0.50-0.60

**Design Procedure:**

1. Calculate airflow at each section (cumulative from terminals)
2. Select velocity at fan discharge (typically 1500-2500 fpm)
3. Size first section for selected velocity
4. Calculate friction loss in first section
5. Determine velocity reduction to achieve static regain equal to friction loss
6. Size next section for reduced velocity
7. Repeat for all sections
8. Calculate dynamic losses and verify static pressure at branches

**Section Sizing Algorithm:**

For section $i$ with length $L_i$:

1. Known: $Q_i$, $V_{i-1}$, $P_{s,i-1}$
2. Estimate $V_i$ (typically 0.8-0.9 × $V_{i-1}$)
3. Calculate $P_{v,i}$ and regain: $\Delta P_{v,\text{regain}} = R(P_{v,i-1} - P_{v,i})$
4. Size duct such that $\Delta P_f \times L_i/100 = \Delta P_{v,\text{regain}}$
5. Verify: $P_{s,i} = P_{s,i-1} + \Delta P_{v,\text{regain}} - \Delta P_f - \Delta P_{\text{fittings}}$

**Advantages:**
- Balanced static pressure at branches
- Minimal damper requirements
- Optimized for low operating cost
- Self-balancing design

**Disadvantages:**
- Complex manual calculations
- Requires iterative sizing
- Sensitive to regain factor accuracy
- Difficult to apply without software

### Method Comparison

{{< table >}}
| Criterion | Equal Friction | Velocity | Static Regain |
|-----------|----------------|----------|---------------|
| First cost | Medium | High | Low-Medium |
| Operating cost | Medium | Medium-High | Low |
| Design complexity | Low | Very Low | High |
| Balancing required | Yes | Yes | Minimal |
| Noise control | Indirect | Direct | Indirect |
| Optimization | None | Noise | Energy |
| Best application | Simple systems | Noise-sensitive | Complex, efficiency-critical |
{{< /table >}}

## Pressure Loss Calculations

Total pressure loss consists of friction losses in straight duct sections and dynamic losses in fittings, transitions, and equipment.

### Friction Loss in Straight Ducts

Friction loss results from viscous shear stress at the duct wall and turbulent momentum exchange. The Darcy-Weisbach equation governs friction loss:

{{< formula display="true" >}}
$$\Delta P_f = f \frac{L}{D_h} \frac{\rho V^2}{2} = f \frac{L}{D_h} P_v$$
{{< /formula >}}

where:
- $f$ = Darcy friction factor (dimensionless)
- $L$ = duct length (ft or m)
- $D_h$ = hydraulic diameter (ft or m)
- $P_v$ = velocity pressure (in. wg or Pa)

**Hydraulic Diameter:**

For non-circular ducts, the hydraulic diameter represents the equivalent circular diameter for friction calculations:

{{< formula display="true" >}}
$$D_h = \frac{4A}{P_w}$$
{{< /formula >}}

where:
- $A$ = cross-sectional area
- $P_w$ = wetted perimeter

For rectangular ducts:

{{< formula display="true" >}}
$$D_h = \frac{4ab}{2(a+b)} = \frac{2ab}{a+b}$$
{{< /formula >}}

where $a$ and $b$ are duct dimensions.

**Friction Factor:**

The Colebrook equation relates friction factor to Reynolds number and relative roughness:

{{< formula display="true" >}}
$$\frac{1}{\sqrt{f}} = -2 \log_{10}\left(\frac{\epsilon/D_h}{3.7} + \frac{2.51}{Re\sqrt{f}}\right)$$
{{< /formula >}}

where:
- $\epsilon$ = absolute roughness (ft or m)
- $Re = \rho V D_h / \mu$ = Reynolds number
- $\mu$ = dynamic viscosity

This implicit equation requires iterative solution. For practical duct design, the Altshul-Tsal equation provides explicit approximation:

{{< formula display="true" >}}
$$f = 0.11\left(\frac{\epsilon}{D_h} + \frac{68}{Re}\right)^{0.25}$$
{{< /formula >}}

**Surface Roughness:**

Absolute roughness values for common duct materials:

{{< table >}}
| Material | Roughness $\epsilon$ (ft) | Roughness $\epsilon$ (mm) |
|----------|---------------------------|---------------------------|
| Smooth plastic, drawn tubing | 0.000005 | 0.0015 |
| Galvanized steel, spiral wound | 0.0005 | 0.15 |
| Galvanized steel, longitudinal seams | 0.0005 | 0.15 |
| Fiberglass duct board | 0.003 | 0.9 |
| Flexible duct, fully extended | 0.003-0.01 | 0.9-3.0 |
| Flexible duct, compressed | 0.01-0.05 | 3.0-15.0 |
{{< /table >}}

**Friction Chart Method:**

ASHRAE friction charts incorporate the Darcy-Weisbach equation with standard air properties and assumed roughness ($\epsilon$ = 0.0005 ft for galvanized steel). The charts plot:
- Airflow rate $Q$ (cfm or L/s)
- Duct diameter or dimensions (in. or mm)
- Friction loss (in. wg/100 ft or Pa/m)
- Velocity $V$ (fpm or m/s)

Usage:
1. Connect known airflow and duct size
2. Read friction loss and velocity
3. Scale for actual duct length

**Correction for Altitude and Temperature:**

Friction loss varies with air density. For non-standard conditions:

{{< formula display="true" >}}
$$\Delta P_{f,\text{actual}} = \Delta P_{f,\text{std}} \times \frac{\rho_{\text{actual}}}{\rho_{\text{std}}}$$
{{< /formula >}}

Density ratio:

{{< formula display="true" >}}
$$\frac{\rho_{\text{actual}}}{\rho_{\text{std}}} = \frac{P_{\text{actual}}}{P_{\text{std}}} \times \frac{T_{\text{std}}}{T_{\text{actual}}}$$
{{< /formula >}}

where pressures are absolute and temperatures are absolute (Rankine or Kelvin).

### Dynamic Losses in Fittings

Fittings, transitions, and equipment create turbulence and flow separation, resulting in dynamic pressure losses. These losses are quantified by loss coefficients.

**Loss Coefficient Method:**

{{< formula display="true" >}}
$$\Delta P_{\text{fitting}} = C \times P_v$$
{{< /formula >}}

where:
- $C$ = loss coefficient (dimensionless)
- $P_v$ = velocity pressure at reference location

The reference velocity depends on fitting type:
- Elbows, entries: velocity in duct section
- Transitions: velocity at smaller cross-section
- Branch takeoffs: velocity in branch or main (specified with $C$ value)

**Elbow Loss Coefficients:**

Round elbows:

{{< table >}}
| R/D Ratio | 90° Elbow | 45° Elbow | Notes |
|-----------|-----------|-----------|-------|
| 0.5 | 0.71 | 0.35 | Sharp, not recommended |
| 0.75 | 0.33 | 0.16 | Standard short radius |
| 1.0 | 0.22 | 0.11 | Standard long radius |
| 1.5 | 0.15 | 0.08 | Minimum loss |
| 2.0 | 0.13 | 0.07 | Diminishing returns |
{{< /table >}}

where $R$ = centerline radius, $D$ = duct diameter.

Rectangular elbows without vanes:

{{< table >}}
| H/W Ratio | 90° Elbow $C$ | Notes |
|-----------|---------------|-------|
| 0.25 | 1.20 | Flat elbow, high loss |
| 0.5 | 0.85 | |
| 1.0 | 0.60 | Square cross-section |
| 2.0 | 0.75 | |
| 4.0 | 1.00 | Tall elbow, increased loss |
{{< /table >}}

where $H$ = height, $W$ = width.

Rectangular elbows with turning vanes reduce losses significantly:

{{< table >}}
| Vane Type | $C$ Value | Reduction vs. No Vanes |
|-----------|-----------|------------------------|
| Single thickness vanes | 0.15-0.25 | 60-75% |
| Double thickness vanes | 0.10-0.15 | 75-85% |
| Airfoil vanes | 0.08-0.12 | 80-90% |
{{< /table >}}

**Transition Loss Coefficients:**

Gradual transitions (expansion or contraction):

For expansions (increasing area):

{{< formula display="true" >}}
$$C = 2.6 \sin\left(\frac{\theta}{2}\right) \left[1 - \left(\frac{A_1}{A_2}\right)\right]^2$$
{{< /formula >}}

based on upstream velocity $V_1$.

For contractions (decreasing area):

{{< formula display="true" >}}
$$C = 0.5 \sin\left(\frac{\theta}{2}\right) \left[1 - \left(\frac{A_2}{A_1}\right)^2\right]$$
{{< /formula >}}

based on downstream velocity $V_2$.

where $\theta$ = included angle of transition.

Recommended transition angles:
- Expansions: $\theta$ ≤ 20° (preferred ≤ 15°)
- Contractions: $\theta$ ≤ 30° (preferred ≤ 20°)

Abrupt transitions (no transition section):

{{< table >}}
| Configuration | $C$ Value | Reference Velocity |
|---------------|-----------|-------------------|
| Abrupt expansion | $(1 - A_1/A_2)^2$ | Upstream $V_1$ |
| Abrupt contraction | $0.5(1 - A_2/A_1)$ | Downstream $V_2$ |
{{< /table >}}

**Entry and Exit Losses:**

Inlet conditions:

{{< table >}}
| Inlet Type | $C$ Value |
|------------|-----------|
| Sharp-edged entry | 0.50 |
| Rounded entry, r/D = 0.05 | 0.25 |
| Rounded entry, r/D = 0.10 | 0.15 |
| Rounded entry, r/D ≥ 0.20 | 0.05 |
| Bell mouth entry | 0.03 |
{{< /table >}}

Exit losses:

All duct exits discharge to static pressure environment:

{{< formula display="true" >}}
$$\Delta P_{\text{exit}} = 1.0 \times P_v$$
{{< /formula >}}

Complete velocity pressure is lost (100% loss coefficient). This applies to supply grilles, diffusers, and exhaust hoods.

**Damper Losses:**

Volume dampers:

{{< table >}}
| Damper Position | $C$ Value |
|-----------------|-----------|
| Fully open | 0.19 |
| 15° closed | 0.52 |
| 30° closed | 1.54 |
| 45° closed | 4.52 |
| 60° closed | 17.3 |
{{< /table >}}

Fire/smoke dampers (fully open):

{{< table >}}
| Damper Type | $C$ Value |
|-------------|-----------|
| Standard fire damper | 0.15-0.35 |
| Combination fire/smoke damper | 0.25-0.50 |
| Ceiling radiation damper | 0.10-0.20 |
{{< /table >}}

### Comprehensive Fitting Loss Table

{{< table >}}
| Fitting Type | Configuration | $C$ Value | Notes |
|--------------|---------------|-----------|-------|
| **Entries** | | | |
| | Sharp-edged | 0.50 | Standard duct entry |
| | Bell mouth | 0.03 | Minimum loss entry |
| **Exits** | | | |
| | Any configuration | 1.00 | Complete velocity loss |
| **Elbows (Round)** | | | |
| | 90°, R/D = 0.75 | 0.33 | Standard short radius |
| | 90°, R/D = 1.0 | 0.22 | Standard long radius |
| | 90°, R/D = 1.5 | 0.15 | Preferred for low loss |
| | 45°, R/D = 1.0 | 0.11 | Half angle, half loss |
| **Elbows (Rectangular)** | | | |
| | 90°, no vanes, square | 0.60 | Basic rectangular |
| | 90°, single-thickness vanes | 0.20 | Vanes recommended |
| | 90°, airfoil vanes | 0.10 | Minimum loss |
| **Transitions** | | | |
| | Gradual expansion, θ=15° | 0.15-0.25 | Depends on area ratio |
| | Gradual contraction, θ=20° | 0.05-0.10 | Low loss |
| | Abrupt expansion, 2:1 area | 0.25 | Based on upstream $P_v$ |
| | Abrupt contraction, 1:2 area | 0.19 | Based on downstream $P_v$ |
| **Branch Takeoffs** | | | |
| | 45° wye, branch | 0.30-0.50 | Depends on velocity ratio |
| | 90° tee, branch | 0.90-1.50 | High loss, avoid if possible |
| | Conical tee, branch | 0.15-0.30 | Preferred for branches |
| **Dampers** | | | |
| | Volume, fully open | 0.19 | Balancing damper |
| | Fire damper, open | 0.25 | Code-required |
| | Smoke damper, open | 0.35 | Code-required |
{{< /table >}}

### Total System Pressure Loss

The total pressure loss from fan discharge to terminal equals the sum of all friction and dynamic losses:

{{< formula display="true" >}}
$$\Delta P_{\text{total}} = \sum_{i} \Delta P_{f,i} + \sum_{j} \Delta P_{\text{fitting},j}$$
{{< /formula >}}

For design, calculate the critical path (longest run with highest resistance):

1. Identify path from fan to most remote terminal
2. Calculate friction loss in each duct section
3. Sum all fitting losses along path
4. Add terminal device pressure drop
5. Include filter and coil pressure drops
6. Add safety factor (10-15%) for uncertainty

Fan total pressure requirement:

{{< formula display="true" >}}
$$P_{t,\text{fan}} = \Delta P_{\text{critical path}} + P_{v,\text{discharge}}$$
{{< /formula >}}

## Aspect Ratio Effects

Rectangular ducts deviate from circular cross-sections, affecting pressure loss and construction cost. The aspect ratio $AR = a/b$ (longer side / shorter side) quantifies this deviation.

### Hydraulic Diameter vs. Equivalent Diameter

Two diameter definitions exist for rectangular ducts:

**Hydraulic Diameter** (for friction calculations):

{{< formula display="true" >}}
$$D_h = \frac{2ab}{a+b}$$
{{< /formula >}}

**Equivalent Diameter** (circular duct with same friction and flow):

{{< formula display="true" >}}
$$D_e = 1.30 \frac{(ab)^{0.625}}{(a+b)^{0.25}}$$
{{< /formula >}}

For aspect ratios 1-4, $D_e$ provides accurate friction loss when used with circular duct friction charts.

### Pressure Loss vs. Aspect Ratio

For constant cross-sectional area, increasing aspect ratio increases pressure loss:

{{< diagram >}}
graph LR
    A[12" x 12" Square<br/>AR = 1.0<br/>Baseline Loss] --> B[8" x 18" Rectangle<br/>AR = 2.25<br/>Loss = 1.10x]
    B --> C[6" x 24" Rectangle<br/>AR = 4.0<br/>Loss = 1.25x]
    C --> D[4" x 36" Rectangle<br/>AR = 9.0<br/>Loss = 1.50x]

    style A fill:#90EE90
    style B fill:#FFD700
    style C fill:#FFA500
    style D fill:#FF6347
{{< /diagram >}}

Aspect ratio correction factor for pressure loss:

{{< table >}}
| Aspect Ratio | Correction Factor | % Increase |
|--------------|-------------------|------------|
| 1.0 | 1.00 | Baseline (square) |
| 1.5 | 1.03 | +3% |
| 2.0 | 1.06 | +6% |
| 3.0 | 1.13 | +13% |
| 4.0 | 1.20 | +20% |
| 6.0 | 1.32 | +32% |
| 8.0 | 1.42 | +42% |
{{< /table >}}

### Optimal Aspect Ratio

Balancing construction cost, pressure loss, and space constraints:

**Construction Cost:**
- Square ducts minimize material (lowest perimeter for given area)
- Moderate aspect ratios (2-3) balance material and fabrication costs
- High aspect ratios increase fabrication complexity

**Pressure Loss:**
- Square ducts minimize friction loss
- Each doubling of aspect ratio increases loss 10-15%

**Space Utilization:**
- Flat ducts (high AR) fit above ceilings or in wall cavities
- Architectural constraints often drive aspect ratio selection

**Recommended Practice:**

{{< table >}}
| Application | Recommended AR | Rationale |
|-------------|----------------|-----------|
| Exposed ductwork | 1.0-2.0 | Minimize material and loss |
| Ceiling plenum | 2.0-4.0 | Balance height and loss |
| Wall cavity | 4.0-8.0 | Fit available space |
| Maximum for any application | 8.0 | Excessive loss penalty |
{{< /table >}}

### Structural Considerations

Rectangular ducts require structural reinforcement based on aspect ratio, pressure class, and dimensions. Per SMACNA standards:

**Reinforcement Spacing:**

For ducts operating at pressure class 2 in. wg:

{{< table >}}
| Duct Dimension (in.) | AR = 1-2 | AR = 2-4 | AR = 4-6 |
|---------------------|----------|----------|----------|
| 12-30 | No reinforcement | Intermediate ties | Tie rods + angles |
| 30-54 | Intermediate ties | Tie rods + angles | External angles |
| 54-84 | Tie rods + angles | External angles | Not recommended |
| >84 | External angles | Not recommended | Not recommended |
{{< /table >}}

## Velocity Limits for Noise Control

Air velocity generates noise through turbulence and vibration. Excessive velocity produces objectionable acoustic emissions.

### Noise Generation Mechanisms

**Turbulence Noise:**

Velocity fluctuations in turbulent flow create pressure waves:

{{< formula display="true" >}}
$$L_W \propto 60 \log_{10}(V) + 10 \log_{10}(A)$$
{{< /formula >}}

where:
- $L_W$ = sound power level (dB)
- $V$ = air velocity (fpm)
- $A$ = duct area (ft²)

Doubling velocity increases noise approximately 18 dB.

**Fitting Noise:**

Elbows, dampers, and branches create vortex shedding and flow separation, generating discrete frequency noise (typically 500-2000 Hz).

**Terminal Device Noise:**

Grilles and diffusers generate noise as air expands into occupied space. Noise correlates with discharge velocity and pressure drop.

### Velocity Recommendations by Application

Maximum velocities to achieve NC (Noise Criteria) levels:

**Residential (NC 25-35):**

{{< table >}}
| Location | Main Duct | Branch | Terminal Runout |
|----------|-----------|--------|-----------------|
| Living areas | 700 fpm | 600 fpm | 500 fpm |
| Bedrooms | 600 fpm | 500 fpm | 400 fpm |
| Return air | 800 fpm | 700 fpm | 600 fpm |
{{< /table >}}

**Commercial Office (NC 30-40):**

{{< table >}}
| Location | Main Duct | Branch | Terminal Runout |
|----------|-----------|--------|-----------------|
| Private offices | 1500 fpm | 1000 fpm | 700 fpm |
| Open offices | 1800 fpm | 1200 fpm | 900 fpm |
| Conference rooms | 1200 fpm | 800 fpm | 600 fpm |
| Return air | 2000 fpm | 1500 fpm | 1000 fpm |
{{< /table >}}

**Public Spaces (NC 35-45):**

{{< table >}}
| Location | Main Duct | Branch | Terminal Runout |
|----------|-----------|--------|-----------------|
| Lobbies | 2000 fpm | 1500 fpm | 1000 fpm |
| Retail | 2200 fpm | 1700 fpm | 1200 fpm |
| Corridors | 2500 fpm | 2000 fpm | 1500 fpm |
| Return air | 2500 fpm | 2000 fpm | 1500 fpm |
{{< /table >}}

**Special Applications:**

{{< table >}}
| Application | Maximum Velocity | NC Target |
|-------------|------------------|-----------|
| Recording studios | 300-500 fpm | NC 15-20 |
| Theaters | 500-800 fpm | NC 20-25 |
| Libraries | 800-1200 fpm | NC 30-35 |
| Gymnasiums | 2000-2500 fpm | NC 40-50 |
| Industrial | 2500-4000 fpm | NC 50-60 |
{{< /table >}}

### Grille and Diffuser Selection

Terminal device noise depends on discharge velocity (neck velocity):

{{< formula display="true" >}}
$$V_{\text{neck}} = \frac{Q}{A_{\text{neck}}}$$
{{< /formula >}}

Recommended maximum neck velocities:

{{< table >}}
| Device Type | NC 25 | NC 30 | NC 35 | NC 40 |
|-------------|-------|-------|-------|-------|
| Ceiling diffusers | 400 fpm | 500 fpm | 700 fpm | 900 fpm |
| Slot diffusers | 500 fpm | 600 fpm | 800 fpm | 1000 fpm |
| Grilles (supply) | 500 fpm | 700 fpm | 900 fpm | 1200 fpm |
| Return grilles | 600 fpm | 800 fpm | 1000 fpm | 1400 fpm |
| Linear slot (high induction) | 800 fpm | 1000 fpm | 1400 fpm | 1800 fpm |
{{< /table >}}

Actual noise rating depends on manufacturer data. Consult product catalogs for specific NC values at operating conditions.

## Duct Materials and Construction Standards

Material selection affects cost, pressure loss (surface roughness), and system longevity.

### Galvanized Steel Duct

**Material Specifications:**

ASTM A653 galvanized steel, coating designation G60 (0.60 oz/ft² per side) minimum.

**Gauge Selection (SMACNA):**

Round duct:

{{< table >}}
| Diameter | Pressure Class 2" wg | Pressure Class 4" wg | Pressure Class 6" wg |
|----------|---------------------|---------------------|---------------------|
| 4-12" | 26 ga | 24 ga | 22 ga |
| 13-18" | 24 ga | 22 ga | 20 ga |
| 19-30" | 22 ga | 20 ga | 18 ga |
| 31-54" | 20 ga | 18 ga | 16 ga |
| 55-84" | 18 ga | 16 ga | 14 ga |
{{< /table >}}

Rectangular duct (longest side):

{{< table >}}
| Dimension | Pressure Class 2" wg | Pressure Class 4" wg |
|-----------|---------------------|---------------------|
| Up to 12" | 26 ga | 24 ga |
| 13-30" | 24 ga | 22 ga |
| 31-54" | 22 ga | 20 ga |
| 55-84" | 20 ga | 18 ga |
| 85-96" | 18 ga | 16 ga |
{{< /table >}}

**Construction Types:**

- **Spiral wound:** Helical seam, efficient fabrication, limited sizes
- **Longitudinal seam:** Straight seam, any length, standard construction
- **Snap-lock:** Low-pressure applications (≤ 2 in. wg), residential
- **Standing seam:** Exposed architectural ductwork

**Joint Types:**

{{< table >}}
| Joint Type | Pressure Rating | Application |
|------------|-----------------|-------------|
| Snap-lock (S-slip) | 2 in. wg | Low-pressure, residential |
| TDC (Transverse duct connection) | 2 in. wg | Commercial, quick assembly |
| Flanged connection | 10+ in. wg | Medium/high pressure |
| Welded | 20+ in. wg | High pressure, special |
{{< /table >}}

**Sealing Requirements:**

SMACNA Seal Class:

- **Class A:** Sealed transverse joints only (≤ 2 in. wg)
- **Class B:** Sealed transverse joints and longitudinal seams (2-4 in. wg)
- **Class C:** All joints sealed, gasketed flanges (> 4 in. wg)

### Fiberglass Duct Board

Rigid fiberglass board fabricated into rectangular ducts.

**Material Properties:**

- Thermal resistance: R-4 to R-8 per inch thickness
- Density: 3-6 lb/ft³
- Fire rating: ASTM E84 Class 1 (flame spread ≤ 25)

**Advantages:**
- Integrated thermal insulation
- Acoustic attenuation (1-2 dB/ft typical)
- Lower installed cost for certain applications
- No external insulation required

**Disadvantages:**
- Lower pressure rating (2-4 in. wg maximum)
- Higher surface roughness (increased friction)
- Potential fiber shedding (requires sealed liner in critical applications)
- Moisture sensitivity

**Sizing Considerations:**

Friction loss 30-50% higher than galvanized steel due to roughness:

{{< formula display="true" >}}
$$\Delta P_{f,\text{fiberglass}} \approx 1.3-1.5 \times \Delta P_{f,\text{galvanized}}$$
{{< /formula >}}

Use fiberglass-specific friction charts or apply correction factor.

### Flexible Duct

Flexible duct consists of wire helix supporting polymer film with external insulation.

**Material Construction:**
- Inner core: Polymer film (polyester, metallized polyester)
- Support: Spring steel wire helix
- Insulation: Fiberglass batting (R-4.2 to R-8)
- Vapor barrier: Polymer film jacket

**Pressure Loss:**

Flexible duct exhibits significantly higher friction than rigid duct:

{{< table >}}
| Condition | Friction Multiplier vs. Rigid |
|-----------|------------------------------|
| Fully extended | 1.5-2.0x |
| 10% compressed | 2.0-3.0x |
| 20% compressed | 3.0-5.0x |
{{< /table >}}

**Installation Requirements:**

ASHRAE/SMACNA standards for flexible duct:

- Maximum length: 5 ft per run (minimize use)
- Full extension: No compression allowed
- Support spacing: 4 ft maximum
- Turns: Minimize bends, radius ≥ 1.5 × diameter
- Connections: Secured with draw bands over beads

**Applications:**

Flexible duct serves as terminal connections between rigid duct and diffusers:

- VAV box to diffuser connections
- Duct system adjustments during installation
- Temporary installations
- Vibration isolation connections

Do not use flexible duct as primary distribution due to high friction loss.

### Insulation Requirements

**External Insulation Applications:**

Supply air ducts require insulation to:
- Prevent condensation (cooling applications)
- Reduce heat gain/loss (energy efficiency)
- Reduce noise transmission (acoustic barrier)

**Thickness Selection:**

{{< table >}}
| Location | Minimum R-Value | Typical Thickness |
|----------|-----------------|-------------------|
| Inside conditioned space | R-3 to R-4 | 0.5-1.0 in. |
| Unconditioned space (attic, plenum) | R-6 to R-8 | 1.5-2.0 in. |
| Outdoor | R-8 to R-11 | 2.0-3.0 in. |
| Below grade | R-11 to R-15 | 3.0-4.0 in. |
{{< /table >}}

**Vapor Barrier:**

Cooling applications require vapor barrier on outer surface to prevent moisture infiltration. Vapor retarder permeability ≤ 0.02 perms.

**Return Air Ducts:**

Return ducts typically do not require insulation when located in conditioned space. Insulate return ducts in unconditioned spaces to prevent condensation and heat gain.

## Branch Takeoff Design

Branch takeoffs significantly affect pressure distribution and system balance.

### Takeoff Configurations

{{< diagram >}}
graph TD
    A[Main Duct Flow] --> B{Takeoff Type}
    B --> C[45° Wye<br/>C = 0.30-0.50]
    B --> D[90° Conical Tee<br/>C = 0.15-0.30]
    B --> E[90° Tee<br/>C = 0.90-1.50]
    B --> F[Bullhead Tee<br/>C = 1.50-3.00]

    style C fill:#90EE90
    style D fill:#90EE90
    style E fill:#FFD700
    style F fill:#FF6347
{{< /diagram >}}

**45° Wye (Preferred):**

Low loss coefficient, smooth flow division:

{{< formula display="true" >}}
$$C_{\text{branch}} = 0.30 + 0.20 \left(\frac{V_b}{V_m}\right)^2$$
{{< /formula >}}

where:
- $V_b$ = branch velocity
- $V_m$ = main duct velocity upstream

**Conical Tee (Preferred for 90°):**

Tapered entry reduces separation:

{{< formula display="true" >}}
$$C_{\text{branch}} = 0.15 + 0.15 \left(\frac{V_b}{V_m}\right)^2$$
{{< /formula >}}

**90° Tee (Avoid):**

Abrupt flow direction change creates high loss:

{{< formula display="true" >}}
$$C_{\text{branch}} = 0.90 + 0.60 \left(\frac{V_b}{V_m}\right)^2$$
{{< /formula >}}

**Bullhead Tee (Avoid):**

Flow splits into two opposing branches, maximum loss:

{{< formula display="true" >}}
$$C_{\text{branch}} = 1.50 + 1.50 \left(\frac{V_b}{V_m}\right)^2$$
{{< /formula >}}

### Main Duct Loss at Takeoffs

The main duct experiences loss as flow divides at branches:

**Straight-Through Loss:**

{{< formula display="true" >}}
$$C_{\text{main}} = C_0 \left[1 - \left(\frac{Q_b}{Q_m}\right)^2\right]$$
{{< /formula >}}

where:
- $Q_b$ = branch flow
- $Q_m$ = main duct flow upstream
- $C_0$ = base coefficient (0.10-0.30 depending on configuration)

### Takeoff Sizing Strategy

**Equal Velocity Method:**

Maintain approximately equal velocities in main and branch:

{{< formula display="true" >}}
$$V_b \approx 0.8-1.0 \times V_m$$
{{< /formula >}}

This minimizes loss coefficient and balances static pressure.

**Progressive Reduction:**

Reduce main duct velocity downstream of each takeoff:
1. Calculate airflow remaining after branch
2. Resize main duct for 80-90% of upstream velocity
3. Takeoff sees balanced static pressure

**Damper Placement:**

Locate balancing dampers 3-5 duct diameters downstream of takeoff to allow flow reattachment. Dampers immediately at takeoff increase turbulence and noise.

## Return Air and Exhaust Duct Sizing

Return air systems operate at lower pressure and velocity than supply systems.

### Return Air Velocity Limits

Lower velocities permitted due to:
- Less critical noise propagation (grilles in low-sensitivity areas)
- Lower static pressure availability
- Larger duct cross-sections economically feasible

Recommended maximum velocities:

{{< table >}}
| Location | Main Return | Branch Return | Grille Inlet |
|----------|-------------|---------------|--------------|
| Residential | 800 fpm | 700 fpm | 600 fpm |
| Commercial office | 2000 fpm | 1500 fpm | 800 fpm |
| Retail | 2200 fpm | 1800 fpm | 1000 fpm |
| Industrial | 2500 fpm | 2000 fpm | 1200 fpm |
{{< /table >}}

### Return Air Pathways

**Ducted Return:**

Fully ducted return systems provide:
- Controlled airflow paths
- Minimal leakage
- Acoustic isolation between spaces
- Higher first cost

Size using equal friction method at 0.05-0.08 in. wg/100 ft (lower than supply).

**Plenum Return:**

Use of ceiling plenum, wall cavities, or raised floors as return air path:

**Advantages:**
- Lower first cost (no duct material)
- Easier installation
- Flexible for future modifications

**Disadvantages:**
- Potential odor and contaminant transfer
- Code restrictions in rated construction
- Leakage to outdoors (increased load)
- Sound transmission between spaces

**Code Requirements:**

Plenum spaces must:
- Use plenum-rated cables (CMP, FEP)
- Maintain fire rating with proper penetrations
- Provide access for cleaning
- Meet IMC Section 602 requirements

**Sizing:**

Plenum velocity should not exceed 1.5× ducted return velocity limits to prevent excessive noise from grilles and registers.

### Exhaust System Sizing

Kitchen, bathroom, and laboratory exhaust systems:

**Velocity Recommendations:**

{{< table >}}
| Exhaust Type | Main Duct | Branch | Hood Connection |
|--------------|-----------|--------|-----------------|
| Toilet exhaust | 1800 fpm | 1500 fpm | 1200 fpm |
| Kitchen (grease) | 1500 fpm | 1200 fpm | 1000 fpm |
| General | 2000 fpm | 1500 fpm | 1200 fpm |
| Fume hood | 2000 fpm | 1500 fpm | 1500 fpm |
| Dust collection | 3500-4500 fpm | 3000-4000 fpm | Per material |
{{< /table >}}

**Grease Exhaust:**

Kitchen exhaust ducts require special considerations:
- Minimum velocity 1500 fpm (prevent grease deposition)
- Carbon steel (not galvanized, coating degrades)
- Welded construction, grease-tight
- Slope 2% toward hood for drainage
- Access panels for cleaning

**Dust and Fume:**

Material transport velocity depends on particle size and density. Consult ACGIH Industrial Ventilation Manual for specific materials.

## Practical Design Examples

### Example 1: Residential Forced Air System

**System Description:**

Single-story residence, 2400 ft², cooling load 36,000 Btu/h (3 tons).

**Design Parameters:**

- Supply airflow: $Q = 400$ cfm/ton × 3 ton = 1200 cfm
- Supply air temperature: 55°F
- Return air temperature: 75°F
- Duct location: Unconditioned attic
- Design method: Equal friction

**Step 1: Select Friction Rate**

For residential system in attic: 0.10 in. wg/100 ft

**Step 2: Main Trunk Sizing**

At furnace discharge: $Q$ = 1200 cfm

From friction chart at 0.10 in. wg/100 ft and 1200 cfm:
- Round duct diameter: 14 in.
- Velocity: 940 fpm
- Actual friction: 0.10 in. wg/100 ft

Alternatively, rectangular duct:
- Using $D_e = 1.30(ab)^{0.625}/(a+b)^{0.25} = 14$ in.
- Try 10 × 20 in.: $D_e = 1.30(200)^{0.625}/30^{0.25} = 14.0$ in. ✓
- Aspect ratio: 2.0 (acceptable)

**Step 3: Branch Sizing**

{{< table >}}
| Branch | Flow (cfm) | Diameter (in.) | Velocity (fpm) | Duct Size (rect.) |
|--------|-----------|----------------|----------------|-------------------|
| Master bedroom | 350 | 9 | 750 | 8 × 12 |
| Bedroom 2 | 250 | 8 | 715 | 6 × 10 |
| Bedroom 3 | 250 | 8 | 715 | 6 × 10 |
| Living area | 350 | 9 | 750 | 8 × 12 |
{{< /table >}}

All sized at 0.10 in. wg/100 ft friction rate.

**Step 4: Pressure Loss Calculation (Critical Path)**

Longest run: Furnace → Master bedroom (80 ft total)

Friction losses:

{{< table >}}
| Section | Length (ft) | Diameter (in.) | Loss (in. wg) |
|---------|------------|----------------|---------------|
| Main trunk | 35 | 14 | 0.035 |
| Reduced trunk | 20 | 10 | 0.020 |
| Branch to master | 25 | 9 | 0.025 |
| **Total friction** | | | **0.080** |
{{< /table >}}

Fitting losses:

{{< table >}}
| Fitting | Quantity | $C$ Value | $P_v$ (in. wg) | Loss (in. wg) |
|---------|----------|-----------|----------------|---------------|
| Furnace exit | 1 | 0.50 | 0.055 | 0.028 |
| 90° elbow, R/D=1.0 | 3 | 0.22 | 0.055 | 0.036 |
| 45° wye takeoff | 1 | 0.35 | 0.035 | 0.012 |
| Diffuser | 1 | 1.00 | 0.035 | 0.035 |
| **Total fittings** | | | | **0.111** |
{{< /table >}}

**Step 5: Total System Resistance**

{{< formula display="true" >}}
$$\Delta P_{\text{total}} = 0.080 + 0.111 = 0.191 \text{ in. wg}$$
{{< /formula >}}

Add safety factor (15%):

{{< formula display="true" >}}
$$\Delta P_{\text{design}} = 0.191 \times 1.15 = 0.22 \text{ in. wg}$$
{{< /formula >}}

**Step 6: Return System**

Return airflow: 1200 cfm (same as supply)

Size at lower friction rate (0.08 in. wg/100 ft):
- Return trunk: 16 in. diameter (or 12 × 20 rectangular)
- Branch returns: Typically use ceiling grilles with short plenum connection

Return system pressure drop: ~0.10 in. wg (including filter)

**Step 7: Fan Selection**

External static pressure requirement:

{{< formula display="true" >}}
$$ESP = \Delta P_{\text{supply}} + \Delta P_{\text{return}} = 0.22 + 0.10 = 0.32 \text{ in. wg}$$
{{< /formula >}}

Select furnace/air handler with fan rated for 1200 cfm at 0.35 in. wg ESP minimum.

### Example 2: Commercial VAV System

**System Description:**

Office building floor, 12,000 ft², 120 tons cooling capacity.

**Design Parameters:**

- Peak supply airflow: 48,000 cfm (400 cfm/ton)
- Supply air temperature: 55°F
- Distribution: 24 VAV boxes, 2000 cfm each
- Duct location: Ceiling plenum
- Design method: Static regain

**Step 1: Main Duct Initial Sizing**

Select discharge velocity: 2000 fpm

Required area:

{{< formula display="true" >}}
$$A = \frac{Q}{V} = \frac{48000}{2000} = 24 \text{ ft}^2 = 3456 \text{ in}^2$$
{{< /formula >}}

Circular diameter:

{{< formula display="true" >}}
$$D = \sqrt{\frac{4A}{\pi}} = \sqrt{\frac{4 \times 3456}{\pi}} = 66 \text{ in.}$$
{{< /formula >}}

Use 66 in. diameter round or 36 × 60 in. rectangular duct ($D_e$ = 66 in., AR = 1.67).

**Step 2: Section-by-Section Sizing (Static Regain)**

First section (fan to first VAV box):
- Length: 40 ft
- Flow: 48,000 cfm
- Velocity: 2000 fpm
- $P_v = (2000/4005)^2 = 0.25$ in. wg

Friction loss at 66 in. diameter:
- From friction chart: 0.14 in. wg/100 ft
- Section loss: 0.14 × 40/100 = 0.056 in. wg

After first takeoff (2000 cfm removed):
- Remaining flow: 46,000 cfm
- Target velocity for static regain: Solve for velocity where friction equals regain

Regain available:

{{< formula display="true" >}}
$$\Delta P_v = P_{v1} - P_{v2} = \left(\frac{2000}{4005}\right)^2 - \left(\frac{V_2}{4005}\right)^2$$
{{< /formula >}}

With regain factor $R$ = 0.75:

{{< formula display="true" >}}
$$0.75 \Delta P_v = \Delta P_f$$
{{< /formula >}}

Target friction for next section: 0.056 in. wg / 35 ft × 100 = 0.16 in. wg/100 ft

From friction chart at 46,000 cfm and 0.16 in. wg/100 ft:
- Diameter: 62 in.
- Velocity: 1900 fpm
- Verify regain: $\Delta P_v = 0.25 - (1900/4005)^2 = 0.25 - 0.23 = 0.02$ in. wg
- Regained: 0.75 × 0.02 = 0.015 in. wg ≈ 0.016 in. wg (close enough)

Continue this process for each section, progressively reducing diameter and velocity.

**Step 3: Fitting Losses**

Major fittings in critical path:

{{< table >}}
| Fitting | $C$ Value | $P_v$ (in. wg) | Loss (in. wg) |
|---------|-----------|----------------|---------------|
| Fan discharge transition | 0.15 | 0.25 | 0.038 |
| 90° elbow, vaned | 0.12 | 0.25 | 0.030 |
| 90° elbow, vaned | 0.12 | 0.23 | 0.028 |
| Conical branch takeoffs (×6) | 0.20 | 0.20 avg | 0.240 |
| VAV box | 0.15 | 0.18 | 0.027 |
| Diffuser | 1.00 | 0.04 | 0.040 |
| **Total fittings** | | | **0.403** |
{{< /table >}}

**Step 4: Total Pressure**

With proper static regain design, friction losses approximately balance velocity pressure recovery. Total system pressure dominated by:
- Fitting losses: 0.40 in. wg
- Residual friction (imperfect regain): 0.10 in. wg
- Safety factor: 0.10 in. wg

Total system pressure: ~0.60 in. wg

Add filter (0.50 in. wg) and coil (0.80 in. wg):

{{< formula display="true" >}}
$$P_{t,\text{fan}} = 0.60 + 0.50 + 0.80 = 1.90 \text{ in. wg}$$
{{< /formula >}}

At discharge velocity 2000 fpm:

{{< formula display="true" >}}
$$P_{v,\text{discharge}} = 0.25 \text{ in. wg}$$
{{< /formula >}}

Fan total pressure:

{{< formula display="true" >}}
$$FTP = 1.90 + 0.25 = 2.15 \text{ in. wg}$$
{{< /formula >}}

**Step 5: VAV System Considerations**

At minimum flow (30% of design):
- Main duct flow: 14,400 cfm
- Velocity: 600 fpm (1/3 of design)
- Pressure loss: $(600/2000)^2 = 0.09×$ design ≈ 0.05 in. wg
- Fan rides back on curve, pressure increases
- VAV boxes throttle to maintain setpoint
- Fan control (VFD) reduces speed to maintain duct static pressure

Design static pressure sensor location: 2/3 distance into duct system to maintain adequate pressure at all terminals.

### Example 3: Flex Duct Runout Analysis

**Configuration:**

VAV box to ceiling diffuser connection using flexible duct.

**Parameters:**

- Airflow: 500 cfm
- Flex duct diameter: 10 in.
- Length: 6 ft (exceeds 5 ft recommendation, but common in practice)
- Diffuser pressure drop: 0.04 in. wg

**Rigid Duct Alternative:**

10 in. rigid round duct:
- Velocity: $V = 500/(π × (10/12)^2 / 4) = 917$ fpm
- Friction: 0.08 in. wg/100 ft (from chart)
- Loss: 0.08 × 6/100 = 0.0048 in. wg

**Flex Duct (Fully Extended):**

Friction multiplier: 2.0× rigid duct
- Friction: 0.16 in. wg/100 ft
- Loss: 0.16 × 6/100 = 0.0096 in. wg

**Flex Duct (10% Compressed to 5.4 ft):**

Friction multiplier: 3.0× rigid duct
- Effective friction: 0.24 in. wg/100 ft
- Loss: 0.24 × 5.4/100 = 0.013 in. wg

**Impact Analysis:**

For 24 diffusers in building:

{{< table >}}
| Configuration | Loss per Runout | Total Loss (24×) | Annual Energy Cost* |
|---------------|-----------------|------------------|---------------------|
| Rigid duct | 0.005 in. wg | 0.12 in. wg | Baseline |
| Flex (extended) | 0.010 in. wg | 0.24 in. wg | +$180/year |
| Flex (compressed) | 0.013 in. wg | 0.31 in. wg | +$285/year |
{{< /table >}}

*Assumes 3000 operating hours/year, $0.12/kWh, fan efficiency 60%, motor efficiency 92%.

**Energy Cost Calculation:**

Pressure increase from flex duct: $\Delta P$ = 0.24 - 0.12 = 0.12 in. wg

Fan power increase:

{{< formula display="true" >}}
$$\Delta W = \frac{Q \times \Delta P}{6356 \times \eta_{\text{fan}} \times \eta_{\text{motor}}}$$
{{< /formula >}}

{{< formula display="true" >}}
$$\Delta W = \frac{12000 \times 0.12}{6356 \times 0.60 \times 0.92} = 0.41 \text{ hp} = 0.31 \text{ kW}$$
{{< /formula >}}

Annual cost:

{{< formula display="true" >}}
$$\text{Cost} = 0.31 \text{ kW} \times 3000 \text{ hr} \times \$0.12/\text{kWh} = \$112/\text{year}$$
{{< /formula >}}

**Conclusion:**

Minimize flex duct use. Each 6 ft flex connection costs $110-285/year additional energy compared to rigid duct. Over 20-year lifecycle, this represents $2200-5700 per connection at 3% discount rate.

## Advanced Design Considerations

### Duct Heat Gain and Loss

Air temperature changes as heat transfers through duct walls. This affects delivered capacity and humidity control.

**Heat Transfer Rate:**

{{< formula display="true" >}}
$$\dot{Q} = U \times A_s \times (T_{\text{ambient}} - T_{\text{air}})$$
{{< /formula >}}

where:
- $U$ = overall heat transfer coefficient (Btu/h·ft²·°F)
- $A_s$ = duct surface area (ft²)
- $T_{\text{ambient}}$ = surrounding air temperature (°F)
- $T_{\text{air}}$ = duct air temperature (°F)

**Overall Heat Transfer Coefficient:**

{{< formula display="true" >}}
$$U = \frac{1}{\frac{1}{h_i} + \frac{t_{\text{ins}}}{k_{\text{ins}}} + \frac{1}{h_o}}$$
{{< /formula >}}

For typical insulated duct in attic:
- Interior film coefficient $h_i$ = 1.5 Btu/h·ft²·°F
- Insulation conductivity $k_{\text{ins}}$ = 0.25 Btu/h·ft·°F (fiberglass)
- Insulation thickness $t_{\text{ins}}$ = 2 in. = 0.167 ft
- Exterior film coefficient $h_o$ = 2.0 Btu/h·ft²·°F

{{< formula display="true" >}}
$$U = \frac{1}{\frac{1}{1.5} + \frac{0.167}{0.25} + \frac{1}{2.0}} = \frac{1}{0.67 + 0.67 + 0.50} = 0.54 \text{ Btu/h·ft}^2\text{·°F}$$
{{< /formula >}}

**Temperature Change:**

{{< formula display="true" >}}
$$\Delta T = \frac{\dot{Q}}{1.08 \times Q}$$
{{< /formula >}}

where:
- $Q$ = airflow (cfm)
- 1.08 = specific heat factor for air (Btu/h per cfm·°F)

**Example:**

20 in. diameter duct, 50 ft length in 130°F attic, 55°F supply air, 1200 cfm flow:

Surface area: $A_s = π × (20/12) × 50 = 261$ ft²

Heat gain:

{{< formula display="true" >}}
$$\dot{Q} = 0.54 \times 261 \times (130 - 55) = 10,570 \text{ Btu/h}$$
{{< /formula >}}

Temperature rise:

{{< formula display="true" >}}
$$\Delta T = \frac{10,570}{1.08 \times 1200} = 8.2°F$$
{{< /formula >}}

Delivered air temperature: 55 + 8.2 = 63.2°F (significantly degraded cooling capacity).

**Mitigation:**

- Locate ducts in conditioned space
- Increase insulation thickness (R-8 minimum in unconditioned spaces)
- Minimize duct length in extreme environments
- Consider buried duct in attic insulation

### Duct Leakage

Real duct systems leak air through joints, penetrations, and damaged sections. Leakage reduces delivered airflow and increases energy consumption.

**Leakage Classes:**

ASHRAE 90.1 and IECC define duct leakage classes:

{{< table >}}
| Seal Class | Maximum Leakage | Application |
|------------|-----------------|-------------|
| Seal Class 48 | 48 cfm/100 ft² @ 1 in. wg | Unsealed, legacy systems |
| Seal Class 24 | 24 cfm/100 ft² @ 1 in. wg | Standard sealed, code minimum |
| Seal Class 12 | 12 cfm/100 ft² @ 1 in. wg | Well-sealed systems |
| Seal Class 6 | 6 cfm/100 ft² @ 1 in. wg | Tightly sealed, best practice |
{{< /table >}}

**Leakage Rate:**

{{< formula display="true" >}}
$$Q_{\text{leak}} = C_L \times A_s \times \left(\frac{\Delta P}{1 \text{ in. wg}}\right)^{0.65}$$
{{< /formula >}}

where:
- $C_L$ = leakage class (cfm/100 ft² @ 1 in. wg)
- $A_s$ = duct surface area (ft²)
- $\Delta P$ = duct pressure (in. wg)

**Example:**

1000 ft² duct surface area, Seal Class 12, operating at 2 in. wg:

{{< formula display="true" >}}
$$Q_{\text{leak}} = 12 \times \frac{1000}{100} \times (2)^{0.65} = 12 \times 10 \times 1.57 = 188 \text{ cfm}$$
{{< /formula >}}

For 10,000 cfm system, this represents 1.88% leakage.

**Impact:**

- Reduced delivered airflow to terminals
- Increased fan energy (higher flow at fan)
- Increased heating/cooling energy (conditioned air lost to unconditioned space)
- Pressure imbalance (negative pressure sucks in unconditioned air)

**Testing:**

Duct leakage testing per ANSI/RESNET/ICC 380:
- Pressurize system to 25 Pa (0.1 in. wg)
- Measure airflow required to maintain pressure
- Calculate leakage as cfm per 100 ft² of duct surface area

Target: ≤ 6 cfm/100 ft² @ 25 Pa for tight construction.

## Summary and Design Process

### Comprehensive Design Workflow

1. **Load Calculation and Airflow Requirements**
   - Calculate heating and cooling loads per ACCA Manual J or ASHRAE methods
   - Determine supply airflow: $Q = \text{Load} / (1.08 \times \Delta T)$
   - Establish terminal airflow requirements

2. **Preliminary Layout**
   - Sketch duct routing on building plans
   - Identify available space for duct installation
   - Locate supply and return terminals
   - Determine critical path (longest, highest resistance run)

3. **Sizing Method Selection**
   - Equal friction: Simple systems, manual design
   - Velocity method: Noise-critical applications
   - Static regain: Large systems, energy efficiency priority

4. **Main Duct Sizing**
   - Select initial velocity or friction rate
   - Size main trunk duct
   - Verify aspect ratio ≤ 4:1 preferred, ≤ 8:1 maximum

5. **Branch and Runout Sizing**
   - Size branches using selected method
   - Progressively reduce velocity downstream
   - Maintain velocity limits for noise control

6. **Pressure Loss Calculation**
   - Calculate friction loss for all sections
   - Determine fitting loss coefficients
   - Sum losses along critical path
   - Add equipment pressure drops (filter, coil, terminal devices)

7. **Return System Design**
   - Size return ducts at lower friction rate
   - Consider plenum return where applicable
   - Calculate return system pressure loss

8. **Fan Selection**
   - Sum supply and return pressure losses
   - Add safety factor (10-15%)
   - Select fan for required CFM at total ESP
   - Verify fan operating point on performance curve

9. **Detail Design**
   - Specify duct materials and gauges
   - Detail transitions and fittings
   - Locate balancing dampers
   - Specify insulation and sealing requirements

10. **Verification**
    - Check all velocities against limits
    - Verify aspect ratios
    - Confirm available static pressure at all terminals
    - Review for constructability and access

### Key Design Principles

**Minimize Pressure Loss:**
- Use gradual transitions (15-20° expansion, 20-30° contraction)
- Prefer 45° wye takeoffs over 90° tees
- Specify turning vanes in rectangular elbows
- Minimize flex duct use (≤ 5 ft, fully extended)

**Maintain Velocity Limits:**
- Select velocities based on application noise criteria
- Reduce velocity progressively downstream
- Keep terminal runout velocities low (500-800 fpm)
- Consider acoustic lining for high-velocity ducts

**Optimize Aspect Ratio:**
- Prefer square or near-square cross-sections (AR ≤ 2)
- Use flat ducts only where space requires (AR ≤ 8 maximum)
- Remember: each doubling of AR increases loss 10-15%

**Ensure Proper Sealing:**
- Specify seal class per ASHRAE 90.1
- Seal all transverse joints and longitudinal seams
- Use mastic or approved tapes (no cloth-backed duct tape)
- Test duct leakage on critical projects

**Account for Real-World Conditions:**
- Include safety factors (10-15%) for uncertainty
- Consider duct heat gain/loss in unconditioned spaces
- Specify adequate insulation (R-6 to R-8 minimum)
- Design for future modifications and access

This comprehensive approach to duct design integrates fluid mechanics fundamentals with practical construction constraints, delivering efficient, quiet, and reliable air distribution systems. The physics-based methods presented enable engineers to understand system behavior, optimize designs, and troubleshoot performance issues throughout the system lifecycle.

## References and Standards

- ASHRAE Handbook—Fundamentals, Chapter 21: Duct Design
- ASHRAE Standard 90.1: Energy Standard for Buildings Except Low-Rise Residential Buildings
- SMACNA HVAC Duct Construction Standards—Metal and Flexible
- ACCA Manual D: Residential Duct Systems
- ASHRAE Duct Fitting Database (DFDB)
- ANSI/RESNET/ICC 380: Standard for Testing Airtightness of Building Enclosures, Airtightness of Heating and Cooling Air Distribution Systems
- International Mechanical Code (IMC)
- TABB Procedural Standards for Testing, Adjusting, Balancing of Environmental Systems
