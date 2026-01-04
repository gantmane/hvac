---
title: "Moisture Transport Mechanisms"
weight: 1
description: "Analysis of vapor diffusion, air leakage, capillary action, and gravity drainage mechanisms governing moisture movement through building envelopes, with quantitative transport equations and relative contribution assessment."
---

# Moisture Transport Mechanisms

Moisture moves through building assemblies via four distinct physical mechanisms, each governed by different driving forces and transport laws. Understanding the relative magnitude and control strategies for each mechanism enables effective moisture management in building envelope design.

## Vapor Diffusion

Vapor diffusion represents molecular-scale water vapor transport driven by vapor pressure gradients. While widely discussed in building science, vapor diffusion typically contributes the smallest moisture quantity among transport mechanisms.

### Fick's Law

Steady-state vapor diffusion flux follows Fick's first law:

```
ṁ = -μ × A × (Δpv/Δx)

where:
ṁ = mass flow rate of water vapor (lb/hr or g/s)
μ = vapor permeance (perm or ng/(Pa·s·m²))
A = area (ft² or m²)
Δpv = vapor pressure difference (in. Hg or Pa)
Δx = material thickness (in. or m)
```

For multilayer assemblies, the total vapor resistance equals the sum of individual layer resistances:

```
Rtotal = R1 + R2 + R3 + ... + Rn

where R = 1/μ (vapor resistance)
```

The effective permeance of the complete assembly:

```
μeffective = 1/(R1 + R2 + ... + Rn)
```

### Vapor Pressure Gradient

Vapor pressure pv relates to temperature and relative humidity:

```
pv = φ × psat(T)

where:
φ = relative humidity (decimal)
psat = saturation vapor pressure at temperature T
```

Saturation vapor pressure follows the Antoine equation:

```
psat = exp(C1 - C2/(T + C3))

where:
T = temperature (°F or °C)
C1, C2, C3 = empirical constants
```

For water vapor in typical HVAC temperature ranges:
- **Imperial units**: psat (in. Hg) with T in °F
- **SI units**: psat (Pa) with T in °C

### Typical Diffusion Rates

Consider a 2×6 wall assembly (winter conditions):
- Interior: 70°F, 30% RH → pv = 0.093 in. Hg
- Exterior: 20°F, 70% RH → pv = 0.030 in. Hg
- Wall area: 100 ft²
- Assembly permeance: 5 perms

```
ṁdiffusion = 5 perm × 100 ft² × (0.093 - 0.030) in. Hg
ṁdiffusion = 31.5 grain/hr = 0.051 lb/day
```

This modest diffusion rate (0.051 lb/day) contrasts sharply with air leakage potential.

## Air Leakage

Air leakage transports moisture via bulk air movement through envelope discontinuities. Each cubic foot of air carries moisture proportional to its humidity ratio, making air leakage the dominant moisture transport mechanism in most buildings.

### Moisture Transport by Air

Air leakage moisture flow:

```
ṁair = Q × ρair × W

where:
Q = air flow rate (CFM or m³/s)
ρair = air density (0.075 lb/ft³ at standard conditions)
W = humidity ratio (lb water/lb dry air)
```

Converting to moisture mass flow:

```
ṁair (lb/hr) = Q (CFM) × 60 × 0.075 × W
ṁair (lb/hr) = 4.5 × Q × W
```

### Comparison: Diffusion vs. Air Leakage

For the same 100 ft² wall section with 0.1 CFM/ft² air leakage (moderate leakage):

```
Q = 0.1 CFM/ft² × 100 ft² = 10 CFM
W at 70°F, 30% RH = 0.0024 lb/lb
ṁair = 4.5 × 10 × 0.0024 = 0.108 lb/hr = 2.59 lb/day
```

**Air leakage delivers 51 times more moisture than vapor diffusion** (2.59 vs. 0.051 lb/day).

This ratio increases at higher indoor humidity levels and with greater air leakage rates. Well-sealed assemblies (< 0.02 CFM/ft²) reduce this factor, while leaky assemblies (> 0.5 CFM/ft²) may exceed 500:1 ratios.

### Air Leakage Driving Forces

Air movement through envelope openings follows the orifice equation:

```
Q = C × A × √(ΔP)

where:
C = flow coefficient (CFM/ft²/√in. w.g.)
A = opening area (ft²)
ΔP = pressure difference (in. w.g. or Pa)
```

Pressure differences arise from:

**Stack Effect**:
```
ΔPstack = C × h × (1/Tout - 1/Tin)

where:
C = 7.64 (imperial units)
h = height (ft)
T = absolute temperature (°R = °F + 460)
```

**Wind Pressure**:
```
ΔPwind = Cp × ρair × v²/2

where:
Cp = pressure coefficient (0.2-0.8)
v = wind velocity (ft/s)
```

**Mechanical System Pressure**:
- Supply/exhaust fan imbalance
- Duct leakage
- Combustion appliance depressurization

## Capillary Action

Capillary action transports liquid water through porous materials via surface tension forces. Capillary suction draws water upward against gravity, with transport rates proportional to pore size distribution and material moisture content.

### Capillary Rise

Maximum capillary rise in cylindrical pores:

```
hmax = (2 × σ × cosθ)/(ρw × g × r)

where:
σ = surface tension (0.0050 lb/ft at 68°F)
θ = contact angle (typically 0° for wetting)
ρw = water density (62.4 lb/ft³)
g = gravitational acceleration (32.2 ft/s²)
r = pore radius (ft)
```

For small pores (r = 0.0001 ft = 0.0012 in):
```
hmax = (2 × 0.0050 × 1)/(62.4 × 32.2 × 0.0001)
hmax = 5.0 ft
```

Fine-pore materials (brick, concrete, wood) exhibit substantial capillary rise, necessitating capillary breaks at foundation interfaces.

### Darcy's Law for Liquid Transport

Unsaturated liquid water flow follows Darcy's law:

```
q = -K(θ) × A × (dψ/dx)

where:
q = liquid water flux (ft³/hr or m³/s)
K(θ) = hydraulic conductivity as function of moisture content
A = cross-sectional area
ψ = water potential (capillary + gravity)
```

Hydraulic conductivity decreases exponentially as materials dry. Saturated materials transport water rapidly; partially saturated materials exhibit orders-of-magnitude slower transport.

### Capillary Moisture Transport Rates

Capillary absorption rate for porous materials:

```
i = A × √t

where:
i = cumulative water absorption (lb/ft² or kg/m²)
A = material absorption coefficient
t = time (hr or s)
```

Typical absorption coefficients:
- **Brick**: 0.5-2.0 lb/(ft²·√hr)
- **Concrete**: 0.2-0.8 lb/(ft²·√hr)
- **Wood (grain)**: 1.0-3.0 lb/(ft²·√hr)

### Capillary Break Design

Capillary breaks interrupt liquid water transport by introducing:

1. **Air gap** - Completely breaks capillary continuity
2. **Drainage mat** - Provides drainage plane with minimal capillary conductivity
3. **Hydrophobic layer** - Non-wetting material prevents capillary suction
4. **Coarse material** - Large pores limit capillary rise height

Standard capillary break: 1/4 in. minimum gap or hydrophobic membrane.

## Gravity Drainage

Gravity drives liquid water downward through assemblies. Proper drainage design requires understanding flow paths, drainage rates, and drainage plane capacity.

### Drainage Plane Flow

Laminar film flow down vertical surfaces:

```
q = (ρw × g × δ³)/(3 × ν) × W

where:
q = volumetric flow rate (ft³/s or m³/s)
δ = film thickness (ft or m)
ν = kinematic viscosity (water = 1.0 × 10⁻⁵ ft²/s)
W = wall width (ft or m)
```

For thin films (δ = 0.01 in = 0.00083 ft):
```
q = (62.4 × 32.2 × 0.00083³)/(3 × 1.0 × 10⁻⁵) × W
q = 0.00046 × W ft³/s per foot width
```

Drainage planes handle typical wind-driven rain loads (1-5 gal/ft²/hr during severe storms) when properly sloped and drained.

### Weep Hole Sizing

Weep hole drainage capacity (orifice flow):

```
Q = Cd × A × √(2 × g × h)

where:
Cd = discharge coefficient (0.6-0.65)
A = hole area (ft²)
h = head height (ft)
```

Standard 3/8 in. diameter weep at 6 in. head:
```
A = π × (0.0156 ft)²/4 = 0.00019 ft²
Q = 0.6 × 0.00019 × √(2 × 32.2 × 0.5)
Q = 0.00065 ft³/s = 0.29 gal/min
```

Weep spacing of 24-32 in. on center provides adequate drainage for brick veneer walls.

## Relative Magnitude Comparison

Under typical conditions, moisture transport mechanisms contribute in relative magnitudes:

| Mechanism | Relative Magnitude | Primary Control Strategy |
|-----------|-------------------|-------------------------|
| Air Leakage | 100-1000× | Continuous air barrier |
| Capillary Action | 10-100× (when wetted) | Drainage planes, capillary breaks |
| Gravity Drainage | 10-100× (during rain) | Flashing, weeps, slope |
| Vapor Diffusion | 1× (baseline) | Vapor retarders (climate-specific) |

**Critical Design Principle**: Air barrier continuity provides the greatest moisture control benefit. Vapor diffusion control, while important in specific climates, represents secondary moisture management.

## Integrated Moisture Control Strategy

Effective moisture management requires addressing all mechanisms through layered control:

1. **Drainage Plane** - Manages gravity drainage and diverts bulk water
2. **Air Barrier** - Controls dominant air leakage moisture transport
3. **Capillary Break** - Prevents wicking from foundations and interfaces
4. **Vapor Retarder** - Controls diffusion in climate-appropriate location

These control layers may be provided by separate components or integrated materials serving multiple functions.

## Measurement and Verification

Moisture transport mechanism verification:

- **Vapor Diffusion**: ASTM E96 wet cup/dry cup testing
- **Air Leakage**: ASTM E2357 blower door testing, E783 air barrier testing
- **Capillary Action**: ASTM C1585 water absorption testing
- **Drainage**: Visual observation, drainage capacity testing

Understanding transport mechanisms enables physics-based design rather than prescriptive approaches, optimizing performance for specific climate and assembly combinations.

## Related Topics

- [Vapor Diffusion Fundamentals](../vapor-diffusion-fundamentals/) - Fick's law, permeance calculations
- [Air Leakage Moisture Transport](../air-leakage-moisture-transport/) - Air barrier systems and sealing strategies
- [Condensation Analysis](../condensation-analysis/) - Moisture accumulation from all transport mechanisms
- [Hygrothermal Material Properties](../../hygrothermal-material-properties/) - Material-specific transport properties

---

*Air leakage dominates moisture transport in most building assemblies, requiring continuous air barriers as the primary moisture control strategy.*
