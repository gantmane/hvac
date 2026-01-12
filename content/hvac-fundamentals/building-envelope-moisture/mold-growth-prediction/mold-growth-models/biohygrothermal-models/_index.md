---
title: "Biohygrothermal Models"
weight: 3
---

Biohygrothermal models couple mold growth predictions with dynamic heat and moisture transport simulations in building assemblies. These models predict mold development under transient boundary conditions by solving simultaneous differential equations for temperature, moisture, and biological activity.

## VTT Mold Growth Model

### Model Structure

The VTT model (Technical Research Centre of Finland) integrates biological growth kinetics with material hygrothermal properties.

**Mold Index Evolution:**

```
dM/dt = (1/7) × k₁ × k₂ × exp(-0.68 ln(RHcrit) - 13.9 ln(RHcrit)/T + 0.14 W - 0.33 ln(t₁))
```

Where:
- M = mold index (0-6 scale)
- t = time (weeks)
- k₁ = intensity factor based on material sensitivity
- k₂ = surface quality factor
- RHcrit = critical relative humidity
- T = temperature (°C)
- W = wood species factor
- t₁ = delay time for growth initiation

### Critical Conditions

**Material Sensitivity Classes:**

| Class | Description | RHcrit at 20°C | Examples |
|-------|-------------|----------------|----------|
| Very Sensitive | Optimal nutrients | 80% | Pine sapwood, gypsum |
| Sensitive | Sufficient nutrients | 85% | Planed wood, concrete |
| Medium Resistant | Limited nutrients | 90% | PUR with biocide |
| Resistant | Poor growth substrate | 95% | Glass fiber, mineral wool |

### Decline Phase

When conditions become unfavorable (RH < RHcrit):

```
dM/dt = -0.032 (for M ≥ 3)
dM/dt = -0.016 (for M ≥ 1 and M < 3)
```

Mold index decreases but never returns to zero, representing permanent colonization.

## ESP-r Mold Model

### Integration Approach

ESP-r (Environmental Systems Performance - research) couples mold prediction with whole-building energy and moisture simulation.

**Simultaneous Solution:**

1. Heat transfer equation:
```
ρc ∂T/∂t = ∇(λ∇T) + Lv ∂u/∂t
```

2. Moisture transport equation:
```
ξ ∂φ/∂t = ∇(Dφ∇φ + δp∇(φpsat))
```

3. Mold growth rate:
```
dM/dt = f(T, φ, substrate, M)
```

Where:
- ρ = material density (kg/m³)
- c = specific heat capacity (J/kg·K)
- λ = thermal conductivity (W/m·K)
- Lv = latent heat of vaporization (2.5×10⁶ J/kg)
- u = moisture content (kg/m³)
- ξ = moisture capacity (kg/m³)
- φ = relative humidity (-)
- Dφ = liquid diffusivity (m²/s)
- δp = vapor permeability (kg/m·s·Pa)
- psat = saturation vapor pressure (Pa)

### Substrate Parameterization

Material-specific growth parameters integrated into building component database:

- Sorption isotherm coefficients
- Critical RH thresholds
- Nutrient availability indices
- Surface pH effects
- Biocide presence factors

## Moisture Transport Coupling

### Capillary-Vapor Transfer

**Combined Moisture Flux:**

```
g = -δp∇(φpsat) - Dw∇u
```

Where:
- g = total moisture flux (kg/m²·s)
- δp = vapor permeability (kg/m·s·Pa)
- Dw = liquid water diffusivity (m²/s)

### Sorption Hysteresis

**Absorption vs Desorption:**

Materials exhibit different moisture storage curves depending on wetting history:

```
u_abs = A₁(1 - exp(-B₁φ^C₁))
u_des = A₂(1 - exp(-B₂φ^C₂))
```

Hysteresis affects mold prediction because spore germination occurs preferentially during absorption phases.

### Surface Exchange

**Boundary Condition:**

```
g_surf = βx(pv,air - φpsat,surf)
```

Where:
- βx = surface moisture transfer coefficient (kg/m²·s·Pa)
- pv,air = air vapor pressure (Pa)
- φpsat,surf = surface vapor pressure (Pa)

Typical βx values: 2×10⁻⁸ to 8×10⁻⁸ kg/m²·s·Pa

## Spore Germination Modeling

### Germination Probability

**Time-Dependent Activation:**

```
P(t) = 1 - exp(-k_germ × t^n)
```

Where:
- P(t) = probability of germination at time t
- k_germ = germination rate constant (1/day)
- n = shape parameter (typically 1.5-2.5)

### Environmental Dependencies

**Temperature Effect:**

```
k_germ(T) = k_ref × exp(-Ea/R × (1/T - 1/Tref))
```

Where:
- Ea = activation energy (50-70 kJ/mol)
- R = gas constant (8.314 J/mol·K)
- T = absolute temperature (K)
- Tref = reference temperature (293 K, 20°C)

**Moisture Effect:**

```
k_germ(φ) = k_max × ((φ - φmin)/(φopt - φmin))^α for φ < φopt
k_germ(φ) = k_max for φ ≥ φopt
```

Where:
- φmin = minimum RH for germination (typically 75-85%)
- φopt = optimal RH (typically 95-100%)
- α = moisture sensitivity exponent (2-4)

### Lag Phase Duration

**Pre-Germination Delay:**

```
t_lag = t₀ × exp(A(φcrit - φ) + B(Topt - T))
```

Where:
- t₀ = baseline lag time at optimal conditions (1-3 days)
- A, B = empirical coefficients
- φcrit = critical RH for the substrate
- Topt = optimal temperature for growth (25-30°C)

## Growth Rate Equations

### Primary Model

**Exponential Growth Phase:**

```
dX/dt = μmax × X × (1 - X/Xmax) × f(T) × f(φ)
```

Where:
- X = biomass density (g/m²)
- μmax = maximum specific growth rate (1/day)
- Xmax = carrying capacity (g/m²)
- f(T), f(φ) = environmental response functions

### Temperature Response

**Cardinal Temperature Model:**

```
f(T) = ((T - Tmin)(T - Tmax))/(((Topt - Tmin)(Topt - Tmax)) - ((Topt - T)²))
```

Where:
- Tmin = minimum growth temperature (0-5°C)
- Topt = optimal growth temperature (25-30°C)
- Tmax = maximum growth temperature (40-45°C)

For T < Tmin or T > Tmax: f(T) = 0

### Water Activity Response

**Davey Model:**

```
f(aw) = exp(-((aw,min - aw)/k)²)
```

Where:
- aw = water activity (≈ RH/100)
- aw,min = minimum water activity for growth
- k = shape parameter (typically 0.1-0.2)

### Secondary Metabolite Production

**Mycotoxin Formation:**

```
dTox/dt = qtox × μ × X × (1 - Tox/Toxmax)
```

Where:
- Tox = toxin concentration (μg/g substrate)
- qtox = specific toxin production rate (μg/g biomass·day)
- Toxmax = maximum toxin accumulation

## Model Parameters

### Material Properties

| Parameter | Symbol | Typical Range | Units |
|-----------|--------|---------------|-------|
| Density | ρ | 400-2400 | kg/m³ |
| Thermal conductivity | λ | 0.05-2.0 | W/m·K |
| Specific heat | c | 800-2000 | J/kg·K |
| Vapor permeability | δp | 10⁻¹²-10⁻⁹ | kg/m·s·Pa |
| Moisture capacity | ξ | 10-200 | kg/m³ |
| Capillary saturation | wsat | 100-800 | kg/m³ |

### Biological Parameters

| Parameter | Description | Typical Range | Notes |
|-----------|-------------|---------------|-------|
| μmax | Maximum growth rate | 0.1-0.5 day⁻¹ | Species-dependent |
| Xmax | Maximum biomass | 5-50 g/m² | Substrate-limited |
| Ea | Activation energy | 50-70 kJ/mol | Germination/growth |
| RHcrit | Critical humidity | 75-95% | Material-specific |
| t_lag | Lag phase duration | 1-14 days | Condition-dependent |

## Computational Implementation

### Time Stepping

**Adaptive Step Control:**

```
Δt_new = Δt_old × (ε_target/ε_actual)^(1/(p+1))
```

Where:
- ε_target = desired error tolerance (0.001-0.01)
- ε_actual = computed error estimate
- p = order of the numerical method

### Spatial Discretization

**Finite Volume Method:**

Node spacing at material interfaces adjusted to capture moisture gradients:
- Geometric progression ratio: 1.2-1.5
- Minimum node spacing: 0.5-2 mm at surfaces
- Maximum node spacing: 10-50 mm in bulk material

### Convergence Criteria

Iterations continue until:

```
||X^(k+1) - X^k|| < ε_abs + ε_rel × ||X^k||
```

Where:
- ε_abs = absolute tolerance (10⁻⁶)
- ε_rel = relative tolerance (10⁻⁴)
- X = solution vector (T, φ, M)

## Validation Requirements

Models validated against:
- Laboratory growth chamber tests with controlled T and RH
- Field monitoring of building envelope assemblies
- Interstitial condensation events
- Seasonal moisture cycling in walls and roofs
- Known mold growth observations in buildings

Typical model accuracy:
- Mold index prediction: ±1 index unit
- Time to growth initiation: ±20%
- Growth rate: factor of 2-3 variation

## Application Context

Biohygrothermal models serve as the foundation for:
- Building envelope design optimization
- Material selection for mold resistance
- Climate-specific construction detailing
- Retrofit analysis for moisture problems
- Long-term durability assessment
- Risk mapping for geographic regions
