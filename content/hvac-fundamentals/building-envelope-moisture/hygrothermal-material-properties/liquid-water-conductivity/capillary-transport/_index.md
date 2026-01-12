---
title: "Capillary Transport"
description: "Physics of liquid water movement through porous building materials via capillary action, including capillary suction coefficients, liquid diffusivity, and unsaturated flow mechanics"
weight: 1
---

## Physical Principles

Capillary transport represents liquid water movement through the interconnected pore structure of building materials driven by capillary forces (surface tension). This phenomenon occurs independently of vapor diffusion and becomes the dominant moisture transport mechanism when liquid water is present.

**Capillary Pressure**

The fundamental driving force for capillary transport originates from the curvature of the liquid-gas interface within pores:

**Young-Laplace Equation:**

```
Pc = 2γ cos(θ) / r
```

Where:
- Pc = capillary pressure (Pa)
- γ = surface tension of water (0.0728 N/m at 20°C)
- θ = contact angle between water and solid surface (degrees)
- r = effective pore radius (m)

The capillary pressure creates suction that draws water into and through porous materials. Smaller pores generate higher capillary pressures, enabling water to rise to greater heights and penetrate deeper into materials.

**Key Physics Relationships:**

1. **Capillary Rise Height** - Maximum height water reaches in a capillary tube or pore:
   ```
   h = (2γ cos(θ)) / (ρ g r)
   ```
   Where:
   - h = capillary rise height (m)
   - ρ = water density (1000 kg/m³)
   - g = gravitational acceleration (9.81 m/s²)

2. **Contact Angle** - Determines wetting behavior:
   - θ < 90° → hydrophilic (water wetting)
   - θ > 90° → hydrophobic (water repellent)
   - θ = 0° → complete wetting

## Capillary Suction Coefficient

The capillary suction coefficient (A-value or water absorption coefficient) quantifies the rate of water uptake by a material when one surface contacts liquid water.

**Definition:**

```
A = Δm / (A · √t)
```

Where:
- A = capillary suction coefficient (kg/(m²·s^0.5))
- Δm = mass of absorbed water (kg)
- A = surface area in contact with water (m²)
- t = time (s)

This relationship applies during the initial absorption phase when cumulative uptake is proportional to the square root of time.

### Material A-Values

| Material | A-Value (kg/(m²·s^0.5)) | Classification |
|----------|-------------------------|----------------|
| Dense concrete | 0.01 - 0.05 | Very low |
| Normal concrete | 0.05 - 0.15 | Low |
| Lightweight concrete | 0.15 - 0.30 | Moderate |
| Clay brick (fired) | 0.05 - 0.20 | Low to moderate |
| Calcium silicate brick | 0.15 - 0.40 | Moderate to high |
| Sandstone | 0.10 - 0.50 | Moderate to high |
| Limestone | 0.05 - 0.30 | Low to moderate |
| Gypsum plaster | 0.10 - 0.25 | Moderate |
| Wood (perpendicular to grain) | 0.01 - 0.05 | Very low |
| Wood (parallel to grain) | 0.10 - 0.30 | Moderate |
| Cellular concrete | 0.30 - 0.80 | High |
| Porous ceramic | 0.40 - 1.20 | Very high |

**Measurement Standard:**

ASTM C1794 - Standard Test Method for Determination of the Water Absorption Coefficient by Partial Immersion

Test procedure:
1. Dry specimen to constant mass
2. Seal all surfaces except test surface
3. Place test surface in 5-10 mm water depth
4. Measure mass at prescribed intervals (1, 2, 4, 8, 16, 32 min, 1, 2, 4, 8, 24 hr)
5. Plot cumulative uptake vs. square root of time
6. Calculate A-value from linear regression slope

## Liquid Diffusivity

Liquid diffusivity (Dw) describes the moisture-dependent transport coefficient for liquid water movement driven by moisture content gradients.

**Fick's Law for Liquid Transport:**

```
gw = -Dw(w) · ∂w/∂x
```

Where:
- gw = liquid water flux (kg/(m²·s))
- Dw = liquid diffusivity (m²/s)
- w = volumetric moisture content (kg/m³)
- x = spatial coordinate (m)

**Moisture-Dependent Relationship:**

Liquid diffusivity increases exponentially with moisture content:

```
Dw(w) = D0 · exp(b · w/wmax)
```

Where:
- D0 = diffusivity at low moisture content (m²/s)
- b = empirical coefficient (typically 6-12)
- wmax = maximum moisture content at saturation (kg/m³)

This exponential relationship reflects the fact that liquid transport occurs primarily through larger, water-filled pores, which become available only at higher moisture contents.

### Typical Liquid Diffusivity Ranges

| Material | Dw at 80% RH (m²/s) | Dw near saturation (m²/s) |
|----------|---------------------|---------------------------|
| Dense concrete | 1×10⁻¹² - 1×10⁻¹¹ | 1×10⁻⁹ - 1×10⁻⁸ |
| Brick masonry | 5×10⁻¹² - 5×10⁻¹¹ | 5×10⁻⁹ - 5×10⁻⁸ |
| Lime mortar | 1×10⁻¹¹ - 1×10⁻¹⁰ | 1×10⁻⁸ - 1×10⁻⁷ |
| Cellular concrete | 5×10⁻¹¹ - 5×10⁻¹⁰ | 5×10⁻⁸ - 5×10⁻⁷ |
| Wood | 1×10⁻¹³ - 1×10⁻¹² | 1×10⁻¹⁰ - 1×10⁻⁹ |
| Gypsum | 1×10⁻¹¹ - 1×10⁻¹⁰ | 1×10⁻⁸ - 1×10⁻⁷ |

Note: Liquid diffusivity can vary by 3-5 orders of magnitude between dry and saturated conditions.

## Moisture-Dependent Conductivity

The liquid water conductivity (Kl) relates liquid flux to capillary pressure gradients, analogous to thermal conductivity relating heat flux to temperature gradients.

**Darcy's Law for Porous Media:**

```
gw = -Kl(w) · ∂Pc/∂x
```

Where:
- gw = liquid water flux (kg/(m²·s))
- Kl = liquid water conductivity (s)
- Pc = capillary pressure (Pa)
- x = spatial coordinate (m)

**Relationship to Liquid Diffusivity:**

```
Dw = Kl · (∂Pc/∂w)
```

This relationship connects the two transport coefficients through the slope of the moisture retention curve (capillary pressure vs. moisture content).

**Hydraulic Conductivity:**

For materials containing water as a continuous phase:

```
K(ψ) = Ksat · Kr(ψ)
```

Where:
- K(ψ) = hydraulic conductivity at matric potential ψ (m/s)
- Ksat = saturated hydraulic conductivity (m/s)
- Kr = relative hydraulic conductivity (dimensionless, 0-1)
- ψ = matric (capillary) potential (Pa or m of water)

### Relative Conductivity Models

**Van Genuchten-Mualem Model:**

```
Kr(Se) = Se^0.5 · [1 - (1 - Se^(1/m))^m]²
```

Where:
- Se = effective saturation = (θ - θr)/(θs - θr)
- θ = volumetric water content
- θr = residual water content
- θs = saturated water content
- m = empirical parameter (typically 0.3-0.8)

This model describes the rapid decrease in liquid conductivity as materials dry, reflecting the disconnection of liquid-filled pore networks.

## Unsaturated Flow

Most building materials operate in the unsaturated regime where pores are partially filled with water and partially with air. Unsaturated flow behavior differs fundamentally from saturated flow.

**Richards Equation:**

The governing equation for unsaturated liquid water transport:

```
∂θ/∂t = ∂/∂x[K(θ) · (∂ψ/∂x + ∂z/∂x)]
```

Where:
- θ = volumetric water content (m³/m³)
- t = time (s)
- K(θ) = unsaturated hydraulic conductivity (m/s)
- ψ = matric potential (m)
- z = elevation (m, positive upward)

This nonlinear partial differential equation accounts for:
- Capillary pressure gradients (∂ψ/∂x)
- Gravitational effects (∂z/∂x)
- Moisture-dependent conductivity K(θ)

**Simplified 1D Horizontal Transport:**

For horizontal flow where gravity is negligible:

```
∂θ/∂t = ∂/∂x[D(θ) · ∂θ/∂x]
```

This form uses moisture diffusivity D(θ) instead of hydraulic conductivity.

### Flow Regimes

**1. Capillary-Dominated Flow**
- Occurs in fine-pored materials (r < 100 μm)
- Capillary forces >> gravity
- Water can move upward against gravity
- Typical in: concrete, brick, plaster

**2. Gravity-Dominated Flow**
- Occurs in coarse-pored materials (r > 1000 μm)
- Gravity >> capillary forces
- Water drains readily
- Typical in: gravel drainage layers, coarse aggregates

**3. Mixed Flow**
- Both forces significant
- Most common in building materials
- Complex behavior requiring full Richards equation

### Moisture Retention Curves

The relationship between capillary pressure (or matric potential) and moisture content:

```
θ(ψ) = θr + (θs - θr) / [1 + (α|ψ|)^n]^m
```

Van Genuchten parameters:
- α = inverse of air entry pressure (1/m)
- n = pore size distribution parameter
- m = 1 - 1/n (typically)

| Material | α (1/m) | n | θr (m³/m³) | θs (m³/m³) |
|----------|---------|---|------------|------------|
| Sand | 5-15 | 2.0-3.0 | 0.02-0.04 | 0.35-0.45 |
| Loam | 1-5 | 1.3-1.7 | 0.03-0.06 | 0.40-0.50 |
| Clay | 0.5-2 | 1.1-1.4 | 0.05-0.10 | 0.45-0.55 |
| Concrete | 0.01-0.1 | 1.2-1.8 | 0.02-0.05 | 0.10-0.20 |
| Brick | 0.05-0.5 | 1.3-2.0 | 0.03-0.08 | 0.25-0.40 |

## Darcy's Law Application

Darcy's law, originally developed for saturated groundwater flow, extends to unsaturated flow in porous building materials with moisture-dependent conductivity.

**General Darcy's Law:**

```
q = -K(θ) · (∇ψ + ∇z)
```

Where:
- q = specific discharge vector (m/s)
- K(θ) = hydraulic conductivity as function of moisture content (m/s)
- ∇ψ = matric potential gradient (dimensionless)
- ∇z = elevation gradient (dimensionless, = 1 for vertical flow)

**Mass Flux Form:**

```
gw = -ρw · K(θ) · (∂ψ/∂x + ∂z/∂x)
```

Where:
- gw = mass flux (kg/(m²·s))
- ρw = water density (kg/m³)

### Saturated Hydraulic Conductivity

Reference values for fully saturated conditions:

| Material | Ksat (m/s) | Permeability Classification |
|----------|------------|----------------------------|
| Gravel | 1×10⁻² - 1×10⁻¹ | Very high |
| Coarse sand | 1×10⁻⁴ - 1×10⁻² | High |
| Fine sand | 1×10⁻⁶ - 1×10⁻⁴ | Moderate |
| Silt | 1×10⁻⁸ - 1×10⁻⁶ | Low |
| Clay | 1×10⁻¹¹ - 1×10⁻⁸ | Very low |
| High-strength concrete | 1×10⁻¹² - 1×10⁻¹⁰ | Extremely low |
| Normal concrete | 1×10⁻¹¹ - 1×10⁻⁹ | Very low |
| Fired clay brick | 1×10⁻⁹ - 1×10⁻⁷ | Very low to low |
| Calcium silicate brick | 1×10⁻⁸ - 1×10⁻⁶ | Low to moderate |

**Measurement Standards:**
- ASTM D2434 - Permeability of Granular Soils (Constant Head)
- ASTM D5084 - Hydraulic Conductivity of Saturated Porous Materials (Flexible Wall Permeameter)

### Intrinsic Permeability

The fluid-independent property of the porous medium:

```
k = K · μ / (ρw · g)
```

Where:
- k = intrinsic permeability (m²)
- μ = dynamic viscosity of water (Pa·s)
- K = hydraulic conductivity (m/s)

Intrinsic permeability relates to pore structure geometry independent of fluid properties.

## Design Considerations

### Rain Penetration and Absorption

**Driving Rain Load:**

```
Rdr = U · cos(α) · rh
```

Where:
- Rdr = driving rain intensity (L/(m²·hr))
- U = wind speed (m/s)
- α = angle between wind and wall normal
- rh = horizontal rainfall intensity (mm/hr)

**Critical Penetration Depth:**

For walls exposed to driving rain:

```
xpenetration = A · √(texposure)
```

Provides estimate of water penetration depth during a rain event.

**Protection Strategies:**

1. **Surface Treatments**
   - Hydrophobic coatings (silanes, siloxanes)
   - Reduce A-value by 50-90%
   - Maintain vapor permeability

2. **Drainage Cavities**
   - 25-50 mm air gaps behind cladding
   - Allows capillary break
   - Removes liquid water before deep penetration

3. **Capillary Breaks**
   - Material transitions from fine to coarse pores
   - Interrupts capillary suction
   - Examples: coarse sand layers, drainage mats

### Rising Damp

Capillary rise from ground moisture sources:

**Equilibrium Height:**

```
heq = (2γ cos(θ)) / (ρw · g · reff)
```

For typical masonry materials:
- Clay brick: 1.5-3.0 m
- Concrete block: 0.3-0.6 m
- Lightweight concrete: 3.0-6.0 m

**Mitigation Methods:**

1. **Horizontal Barriers**
   - Damp-proof course (DPC) membranes
   - Stainless steel sheets
   - Chemical injection barriers

2. **Capillary Break Layers**
   - 150-300 mm coarse gravel under slabs
   - Geotextile separation layers
   - Limits rise height

3. **Active Systems**
   - Electro-osmotic systems
   - Ventilated base channels
   - Dehumidification

### Drying Considerations

**Drying Rate:**

Liquid water removal by evaporation and redistribution:

```
∂w/∂t = -∇·gw - E
```

Where:
- E = evaporation rate at surfaces (kg/(m³·s))
- gw = liquid redistribution flux

**Factors Affecting Drying:**

1. **Liquid Conductivity**
   - Higher Dw → faster liquid redistribution to surfaces
   - Enables more efficient drying

2. **Vapor Diffusion Resistance**
   - Low μ-value at surfaces promotes evaporation
   - Vapor-tight finishes trap moisture

3. **Environmental Conditions**
   - Temperature (higher → faster drying)
   - Relative humidity (lower → faster drying)
   - Air velocity (higher → faster drying)

**Design Rules:**

- Allow drying to both sides where possible
- Interior finishes should be more vapor-open than exterior (μ-value ratio)
- Avoid impermeable barriers on potential drying sides

### Moisture Damage Thresholds

Critical moisture contents for damage mechanisms:

| Mechanism | Critical Condition | Typical Materials |
|-----------|-------------------|-------------------|
| Mold growth | RH > 80% for 7+ days | Organic surfaces |
| Corrosion (steel) | RH > 60% sustained | Embedded reinforcement |
| Freeze-thaw damage | Scrit > 0.90, T < 0°C | Brick, concrete |
| Wood rot | MC > 20% sustained | Structural wood |
| Efflorescence | Cycles wet/dry | Masonry, concrete |
| Salt damage | Variable, depends on salt | Porous masonry |

Where Scrit = critical saturation degree for freeze-thaw damage.

## Numerical Simulation

### Discretization Methods

**Finite Difference:**

```
(θᵢⁿ⁺¹ - θᵢⁿ)/Δt = [Dᵢ₊₁/₂ · (θᵢ₊₁ⁿ - θᵢⁿ) - Dᵢ₋₁/₂ · (θᵢⁿ - θᵢ₋₁ⁿ)] / (Δx)²
```

**Implicit Scheme:**

Provides numerical stability for nonlinear moisture transport:
- Time step limited by convergence, not stability
- Requires iterative solution (Newton-Raphson)

### Simulation Tools

1. **WUFI** (Fraunhofer IBP)
   - Coupled heat and moisture transport
   - Extensive material database
   - 1D, 2D capabilities

2. **DELPHIN** (TU Dresden)
   - Multi-dimensional hygrothermal simulation
   - Salt transport modeling
   - Advanced material models

3. **COMSOL Multiphysics**
   - General PDE solver
   - Custom physics implementation
   - Couples with structural, airflow

4. **MOISTURE-EXPERT** (Kunzel)
   - Simplified 1D tool
   - Educational and preliminary design

**Input Requirements:**

- Moisture retention curve θ(ψ)
- Liquid conductivity K(θ) or diffusivity D(θ)
- Capillary suction coefficient A
- Vapor permeability δ(φ)
- Thermal conductivity λ(θ)

## Experimental Characterization

### Laboratory Methods

**1. Capillary Absorption Test (A-value)**

ASTM C1794, EN ISO 15148

Procedure:
- Sample size: minimum 100×100 mm face
- Lateral sealing: epoxy or aluminum tape
- Water depth: 5-10 mm
- Measurements: √t intervals
- Duration: until uptake rate stabilizes

**2. Pressure Plate Method**

Determines moisture retention curve:
- Apply known capillary pressures
- Measure equilibrium moisture content
- Range: 0-1500 kPa typical
- Standard: ASTM D6836, ISO 11274

**3. Hydraulic Conductivity**

Constant or falling head permeameter:
- Saturated conditions
- Measure flow rate under known gradient
- Calculate Ksat from Darcy's law
- Standards: ASTM D2434, D5084

**4. Inverse Analysis**

Determine transport properties from absorption experiments:
- Measure moisture profiles during absorption
- Simulate with numerical model
- Optimize parameters to match experimental data
- Provides Dw(θ) and other nonlinear properties

### Field Assessment

**1. Moisture Mapping**

- Capacitance meters (0-40 mm depth)
- Microwave sensors (50-300 mm depth)
- Infrared thermography (surface conditions)

**2. Core Sampling**

- Extract samples at various depths
- Measure moisture content gravimetrically
- Assess damage state

**3. Tracer Tests**

- Inject fluorescent dyes or salts
- Track transport pathways
- Quantify in-situ transport rates

## ASHRAE and Standards References

**ASHRAE Fundamentals (Chapter 25 - Heat, Air, and Moisture Control in Building Assemblies):**
- Section on moisture transport mechanisms
- Liquid transport coefficients
- Capillary absorption data

**ASTM Standards:**
- C1794: Water Absorption Coefficient by Partial Immersion
- D2434: Permeability of Granular Soils
- D5084: Hydraulic Conductivity of Saturated Porous Materials
- D6836: Water Retention Characteristics

**ISO Standards:**
- ISO 15148: Hygrothermal performance of building materials - Determination of water absorption coefficient
- ISO 11274: Soil quality - Determination of water retention characteristic

**EN Standards:**
- EN 1925: Natural stone test methods - Determination of water absorption coefficient by capillarity
- EN 15026: Hygrothermal performance of building components and building elements

**Other References:**
- WTA Guideline 6-2: Simulation of heat and moisture transfer
- RILEM recommendations for moisture transport property measurement
- NIST Technical Note 1943: Integrated Hygrothermal Models

## Practical Applications

### Material Selection

Choose materials based on capillary transport properties:

**Exterior Walls:**
- Low A-value exterior finish (< 0.1 kg/(m²·s^0.5))
- Capillary-active interior layers for buffering
- Drainage cavity for liquid removal

**Below-Grade Walls:**
- Very low Ksat materials (< 1×10⁻¹⁰ m/s)
- Capillary break at footing
- Drainage board at exterior

**Roofing:**
- Capillary-tight membranes
- Drainage layers above insulation
- Vapor management for condensation control

### Detailing

**Interface Design:**

At material transitions, consider capillary pressure discontinuities:

```
Pc,1 ≠ Pc,2  at same moisture content
```

This can cause moisture accumulation at interfaces. Design solutions:
- Drainage gaps (capillary break)
- Gradual transitions in pore structure
- Bonding bridges for controlled moisture transfer

**Penetration Sealing:**

Around pipes, fasteners, and other penetrations:
- Sealants must maintain capillary break
- Consider differential movement
- Redundant moisture barriers for critical applications

## Summary

Capillary transport represents the primary mechanism for liquid water movement in building materials. Key engineering parameters include:

- **Capillary suction coefficient (A-value)**: Rate of absorption, units kg/(m²·s^0.5)
- **Liquid diffusivity (Dw)**: Moisture-dependent transport coefficient, exponentially increases with moisture content
- **Hydraulic conductivity (K)**: Links liquid flux to capillary pressure gradients
- **Unsaturated flow**: Governed by Richards equation, accounts for partial saturation
- **Darcy's law**: Foundational relationship extended to moisture-dependent transport

Effective hygrothermal design requires understanding these properties and their variation with moisture content to predict water penetration, redistribution, and drying in building assemblies.

Design strategies focus on controlling liquid water ingress through low-absorption materials, providing drainage pathways, establishing capillary breaks at critical interfaces, and ensuring adequate drying potential through vapor-permeable layers.
