---
title: "Solar Radiation"
weight: 5
---

Solar radiation is the primary external heat gain source for buildings. Accurate prediction of solar heat gains requires understanding extraterrestrial radiation, atmospheric attenuation, geometric relationships, and fenestration properties.

## Solar Constant and Extraterrestrial Radiation

The solar constant represents the intensity of solar radiation at the mean Earth-Sun distance outside the atmosphere.

**Solar Constant:**
- Gsc = 1367 W/m² (433.4 Btu/h·ft²)
- ASHRAE standard value
- Measured perpendicular to solar beam

**Extraterrestrial Radiation:**

Radiation incident on a horizontal surface outside the atmosphere:

Gon = Gsc × (1 + 0.033 × cos(360n/365))

Where:
- n = day of year (1 to 365)
- Factor accounts for Earth's elliptical orbit
- Variation: ±3.3% throughout year

| Date | Day (n) | Gon (W/m²) |
|------|---------|------------|
| Jan 1 | 1 | 1412 |
| Apr 1 | 91 | 1362 |
| Jul 1 | 182 | 1322 |
| Oct 1 | 274 | 1365 |

## Beam and Diffuse Radiation Components

Solar radiation reaching building surfaces consists of direct (beam) and diffuse components.

**Direct Beam Radiation (Edn):**
- Travels directly from sun to surface
- Casts shadows
- Predictable geometry
- Dominant on clear days

**Diffuse Radiation (Ed):**
- Scattered by atmosphere
- No directionality
- Arrives from entire sky dome
- Significant on cloudy days

**Global Radiation (Et):**

Et = Edn × cos(θ) + Ed + Er

Where:
- θ = angle of incidence on surface
- Er = ground-reflected radiation
- Ground reflectance (ρg) typically 0.2

**Ratio Relationships:**

| Sky Condition | Beam/Total | Diffuse/Total |
|---------------|------------|---------------|
| Clear | 0.80-0.90 | 0.10-0.20 |
| Partly cloudy | 0.50-0.70 | 0.30-0.50 |
| Overcast | 0.00-0.10 | 0.90-1.00 |

## Solar Angles

Geometric relationships determine solar position and radiation incidence angles.

**Solar Declination (δ):**

Angle between sun's rays and equatorial plane:

δ = 23.45 × sin[360(284 + n)/365]

| Date | Declination (°) |
|------|-----------------|
| Mar 21 (equinox) | 0 |
| Jun 21 (solstice) | +23.45 |
| Sep 21 (equinox) | 0 |
| Dec 21 (solstice) | -23.45 |

**Hour Angle (H):**

H = 15 × (solar time - 12)

- 15° per hour
- Negative morning, positive afternoon
- Zero at solar noon

**Solar Altitude Angle (β):**

sin(β) = cos(L) × cos(δ) × cos(H) + sin(L) × sin(δ)

Where L = latitude

**Solar Azimuth Angle (φ):**

sin(φ) = cos(δ) × sin(H) / cos(β)

**Zenith Angle (Z):**

Z = 90° - β

**Angle of Incidence (θ):**

For vertical surface:

cos(θ) = cos(β) × cos(φ - ψ)

Where ψ = wall azimuth angle

For tilted surface:

cos(θ) = sin(β) × cos(Σ) + cos(β) × sin(Σ) × cos(φ - ψ)

Where Σ = surface tilt from horizontal

## Clear Sky Models

ASHRAE clear sky models predict maximum solar radiation for design purposes.

**ASHRAE Tau Model:**

Direct normal irradiance:

Eb = Eo × exp[-τb × m]

Diffuse horizontal irradiance:

Ed = Eo × exp[-τd × m]

Where:
- Eo = extraterrestrial irradiance
- m = air mass
- τb, τd = beam and diffuse optical depths

**Air Mass (m):**

m = 1 / [sin(β) + 0.50572 × (6.07995 + β)^(-1.6364)]

- m = 1.0 at β = 90° (overhead sun)
- m = 2.0 at β = 30°
- m approaches infinity at horizon

**Optical Depth Values:**

| Climate | τb | τd | Application |
|---------|----|----|-------------|
| Mid-latitude summer | 0.32 | 2.5 | Cooling load |
| Mid-latitude winter | 0.37 | 2.2 | Solar heating |
| Tropical | 0.27 | 2.8 | High moisture |
| Subarctic summer | 0.28 | 3.0 | Clean, dry air |

## Solar Heat Gain Coefficient (SHGC)

SHGC quantifies fenestration solar heat transmission.

**Definition:**

SHGC = (Transmitted solar + Inward flowing fraction) / Incident solar

**Range:**
- 0.0 (no transmission) to 1.0 (complete transmission)
- Single clear glass: 0.82
- Double clear: 0.70
- Low-e double: 0.30-0.60
- Triple low-e: 0.25-0.45
- Reflective coatings: 0.15-0.30

**Angular Dependence:**

SHGC varies with incidence angle:

| Incidence Angle | SHGC Multiplier |
|-----------------|-----------------|
| 0° (normal) | 1.00 |
| 40° | 0.98 |
| 50° | 0.94 |
| 60° | 0.84 |
| 70° | 0.64 |
| 80° | 0.31 |

## Solar Heat Gain Calculations

**Fenestration Solar Gain:**

q = A × SHGC × Et × IAC

Where:
- A = window area (ft² or m²)
- Et = total incident solar radiation (Btu/h·ft² or W/m²)
- IAC = interior attenuation coefficient (shading devices)

**ASHRAE Solar Heat Gain Factor (SHGF) Method:**

q = A × SHGF × SC

Where:
- SHGF = solar heat gain factor from tables (Btu/h·ft²)
- SC = shading coefficient (reference single glass)

**Peak Solar Heat Gain Factors (Btu/h·ft²):**

| Surface | N | NE/NW | E/W | SE/SW | S | Horiz |
|---------|---|-------|-----|-------|---|-------|
| 40°N July | 47 | 145 | 216 | 180 | 76 | 269 |
| 40°N Jan | 130 | 102 | 105 | 182 | 218 | 134 |

## ASHRAE Calculation Methods

**Radiant Time Series (RTS) Method:**

Current standard for cooling load calculations.

1. Calculate incident solar radiation (clear sky model)
2. Determine transmitted radiation (SHGC)
3. Apply radiant time factors for thermal mass effects
4. Account for room surface absorption

**Solar Air Temperature:**

For opaque surfaces, combine solar and conductive gains:

qsolar = α × A × Et

Where α = solar absorptance

**Equivalent Temperature Difference:**

Used in simplified methods:

TETD = CLTD + (α × Et) / (ho)

Where:
- CLTD = cooling load temperature difference
- ho = outside surface heat transfer coefficient

## Advanced Sky Models

**Isotropic Sky Model:**

Assumes uniform diffuse radiation from sky dome.

**Perez Anisotropic Model:**

Accounts for circumsolar and horizon brightening:

Ed,tilt = Ed,h × [(1 - F1) × (1 + cos(Σ))/2 + F1 × (a/b) + F2 × sin(Σ)]

Where F1, F2 = empirical brightness coefficients

**Ground Reflection:**

Er = (Eb × sin(β) + Ed) × ρg × (1 - cos(Σ))/2

Typical ground reflectances:
- Asphalt, dark soil: 0.10-0.15
- Grass, vegetation: 0.20-0.25
- Concrete, light soil: 0.30-0.40
- Fresh snow: 0.60-0.80

## Design Considerations

**Peak Load Orientations:**

- West-facing: Highest afternoon gains with elevated indoor temperatures
- East-facing: Morning gains, lower impact due to thermal mass lag
- South-facing: Predictable, can be controlled with overhangs
- North-facing: Minimal direct gain (northern hemisphere)

**Calculation Accuracy Factors:**

1. Geographic location (latitude, elevation)
2. Time of year and day
3. Sky conditions (clearness number)
4. Fenestration properties (SHGC, U-factor)
5. Exterior shading (overhangs, fins, trees)
6. Interior shading (blinds, curtains)
7. Building orientation
8. Surface characteristics (absorptance, reflectance)
