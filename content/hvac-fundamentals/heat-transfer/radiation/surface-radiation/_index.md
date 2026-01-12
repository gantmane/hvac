---
title: "Surface Radiation"
weight: 2
---

Surface radiation heat transfer depends on material properties, surface finish, and geometric relationships between surfaces. Understanding emissivity, absorptivity, and reflectivity is essential for HVAC design, particularly for thermal comfort and energy efficiency.

## Surface Radiation Properties

### Emissivity

Emissivity (ε) represents a surface's ability to emit thermal radiation compared to a blackbody at the same temperature. Values range from 0 to 1.

**Gray Body Assumption:**
- Most HVAC calculations assume gray surfaces (ε independent of wavelength)
- Simplifies analysis while maintaining adequate accuracy
- Real surfaces exhibit wavelength-dependent properties

**Temperature Dependence:**
- Emissivity varies with surface temperature
- Most building materials show minimal variation in HVAC temperature range
- Metallic surfaces more temperature-sensitive than non-metals

### Absorptivity and Reflectivity

Energy balance at opaque surface:
```
α + ρ = 1
```
Where:
- α = absorptivity (fraction of incident radiation absorbed)
- ρ = reflectivity (fraction reflected)

**Kirchhoff's Law:**
For surfaces at thermal equilibrium:
```
ε = α
```
This relationship applies when:
- Surface and radiation source at same temperature
- Surface properties independent of wavelength (gray body)

## Emissivity Values for Common Materials

### Building Materials

| Material | Surface Condition | Emissivity ε | Temperature °F |
|----------|------------------|--------------|----------------|
| Aluminum, polished | New, bright | 0.04-0.06 | 70-200 |
| Aluminum, oxidized | Natural aging | 0.11-0.15 | 70-200 |
| Aluminum, anodized | Commercial finish | 0.77-0.84 | 70 |
| Aluminum paint | Fresh coat | 0.27-0.67 | 70 |
| Brick, common | Red, rough | 0.93 | 70 |
| Brick, glazed | Smooth surface | 0.85 | 70 |
| Concrete, rough | Typical finish | 0.94 | 70 |
| Concrete, smooth | Troweled | 0.88-0.93 | 70 |
| Copper, polished | New | 0.04-0.05 | 70-200 |
| Copper, oxidized | Black oxide | 0.76-0.78 | 70 |
| Glass, window | Clear, smooth | 0.84-0.94 | 70 |
| Gypsum, white | Drywall | 0.90 | 70 |
| Paint, black | Flat, non-metallic | 0.95-0.98 | 70 |
| Paint, white | Flat, non-metallic | 0.91-0.96 | 70 |
| Paint, oil-based | Various colors | 0.92-0.96 | 70 |
| Plaster, rough | White lime | 0.91 | 70 |
| Stainless steel, polished | Mirror finish | 0.07-0.17 | 70-500 |
| Stainless steel, oxidized | Discolored | 0.44-0.62 | 500 |
| Steel, galvanized | New, bright | 0.23-0.28 | 70 |
| Steel, oxidized | Rusted | 0.80-0.85 | 70 |
| Wood, planed | Oak, smooth | 0.90 | 70 |
| Wood, rough | Untreated | 0.90-0.95 | 70 |

### HVAC Equipment Surfaces

| Surface | Condition | Emissivity ε | Notes |
|---------|-----------|--------------|-------|
| Aluminum ductwork | Mill finish | 0.09-0.12 | Increases with oxidation |
| Painted ductwork | White enamel | 0.90-0.95 | Standard HVAC paint |
| Galvanized duct | New, clean | 0.25-0.30 | Increases with age/dirt |
| Insulation facing | Aluminum foil | 0.03-0.05 | Single side, smooth |
| FSK facing | Foil-scrim-kraft | 0.03-0.05 | Duct insulation |
| Black pipe | Oxidized steel | 0.79-0.82 | Standard pipe |
| Copper pipe | Clean, no oxidation | 0.06-0.07 | New installation |

### Effect of Surface Condition

**Surface Roughness:**
- Rougher surfaces → higher emissivity
- Microscopic irregularities trap radiation
- Polishing reduces emissivity significantly

**Oxidation:**
- Metal oxides have much higher emissivity than base metal
- Aluminum: 0.05 (polished) → 0.15 (oxidized) → 0.80 (anodized)
- Copper: 0.04 (polished) → 0.78 (black oxide)

**Contamination:**
- Dust and dirt increase emissivity of low-ε surfaces
- Oil films reduce emissivity
- Regular cleaning maintains low-ε performance

## Selective Surfaces

### Wavelength-Dependent Properties

Selective surfaces exhibit different properties at different wavelengths, violating gray body assumption.

**Solar-Selective Surfaces:**
- High absorptivity in solar spectrum (0.3-2.5 μm)
- Low emissivity in thermal infrared (>2.5 μm)
- Used in solar collectors to maximize energy gain

**Cool Roof Coatings:**
- High reflectivity in solar spectrum
- High emissivity in thermal infrared
- Reduces cooling loads in hot climates

### Solar Absorptance vs. Thermal Emittance

| Surface Type | Solar Absorptance α_sol | Thermal Emittance ε_th | Application |
|--------------|------------------------|------------------------|-------------|
| Black paint | 0.96 | 0.96 | Conventional surface |
| White paint | 0.25 | 0.92 | Cool roofs |
| Polished aluminum | 0.20 | 0.05 | Radiant barriers |
| Selective absorber | 0.95 | 0.10 | Solar collectors |
| Cool white coating | 0.20 | 0.90 | Energy-efficient roofs |
| Black chrome | 0.96 | 0.12 | High-temp collectors |
| Titanium oxide | 0.30 | 0.90 | Cool roof pigment |

**Performance Metrics:**

Solar Reflectance Index (SRI):
```
SRI = 123.97 - 141.35×α_sol + 9.655×ε_th
```
Higher SRI indicates cooler surface under solar exposure.

## Low-Emissivity (Low-E) Coatings

### Coating Technologies

**Pyrolytic (Hard Coat):**
- Applied during glass manufacturing at high temperature
- Tin oxide or fluorine-doped tin oxide
- Durable, can be exposed to weather
- ε ≈ 0.15-0.20

**Sputtered (Soft Coat):**
- Applied post-manufacturing via vacuum deposition
- Silver-based multilayer coatings
- Must be sealed in IGU (insulated glazing unit)
- ε ≈ 0.02-0.10
- Superior thermal performance

### Window Performance

**Single-Pane Performance:**
- Clear glass: ε ≈ 0.84
- Low-e coating reduces radiant heat transfer
- Must be in sealed airspace to prevent oxidation

**Double-Pane IGU:**

| Configuration | U-Factor Btu/(hr·ft²·°F) | SHGC | Application |
|---------------|-------------------------|------|-------------|
| Clear-clear, air | 0.48-0.52 | 0.70 | Basic insulation |
| Low-e #2, air | 0.30-0.35 | 0.62 | Heating climates |
| Low-e #2, argon | 0.26-0.30 | 0.60 | Standard energy code |
| Low-e #3, argon | 0.26-0.30 | 0.42 | Cooling climates |
| Double low-e, argon | 0.24-0.28 | 0.38 | High performance |

**Surface Numbering Convention:**
- Surface #1: Outdoor exterior
- Surface #2: Outdoor interior
- Surface #3: Indoor exterior
- Surface #4: Indoor interior

**Coating Position Effects:**
- Surface #2: Best for heating climates (blocks outgoing radiation)
- Surface #3: Best for cooling climates (blocks incoming solar radiation)
- Surface #4: Minimal benefit (moisture/condensation risk)

### Triple-Pane Performance

| Configuration | U-Factor Btu/(hr·ft²·°F) | SHGC | Notes |
|---------------|-------------------------|------|-------|
| Triple low-e, argon | 0.18-0.22 | 0.35 | Cold climates |
| Triple low-e, krypton | 0.15-0.18 | 0.33 | Ultra-efficient |
| Two low-e coatings | 0.16-0.20 | 0.28 | Maximum insulation |

## Radiant Barriers

### Function and Placement

Radiant barriers are low-emissivity surfaces that reduce radiant heat transfer across airspaces.

**Effectiveness Requirements:**
- Adjacent airspace ≥ 0.75 inches
- Low-emissivity surface (ε ≤ 0.10)
- Must face airspace (not in contact with other materials)
- Clean surface (dust degrades performance)

### Attic Applications

**Installation Methods:**

1. **Draped over rafters:**
   - Installed on top of ceiling joists
   - Creates airspace below roof deck
   - Allows ventilation

2. **Attached to rafters:**
   - Foil facing attic space
   - Between roof deck and insulation
   - Requires ventilation gap

3. **Roof deck application:**
   - Adhered to underside of roof deck
   - Factory-applied or field-installed
   - Must maintain airspace to attic

**Heat Flow Reduction:**

Without radiant barrier:
```
q = h_c × ΔT + h_r × ΔT
q = (h_c + h_r) × ΔT
```

With radiant barrier (ε = 0.05):
```
h_r,reduced = σ × (T_hot + T_cold) × (T_hot² + T_cold²) / (1/ε_1 + 1/ε_2 - 1)
h_r,reduced ≈ 0.05 × h_r,original (for ε_2 = 0.90)
```

**Cooling Load Reduction:**
- Hot climates: 10-25% reduction in ceiling heat gain
- Most effective when roof-attic ΔT is large
- Minimal benefit in heating-dominated climates

### Ductwork Applications

**Radiant Barrier Sheathing:**
- Aluminum foil facing on duct insulation
- Reduces radiant heat transfer in attics
- Most effective when ducts not buried in insulation

**Performance in Attic:**
- Duct surface temperature: 55°F (cooling mode)
- Attic temperature: 130°F
- Roof deck temperature: 160°F

Heat gain comparison (per 100 ft² duct surface):

| Configuration | Heat Gain Btu/hr | Reduction |
|---------------|------------------|-----------|
| R-4.2 insulation, ε = 0.90 | 2,850 | Baseline |
| R-4.2 insulation, ε = 0.05 | 2,100 | 26% |
| R-6.0 insulation, ε = 0.90 | 2,250 | 21% |
| R-6.0 insulation, ε = 0.05 | 1,725 | 39% |

## Building Surface Radiation

### Internal Surface Radiation

**Room Heat Balance:**
All internal surfaces exchange radiation with each other. Net radiation depends on:
- Surface temperatures
- Surface emissivities
- View factors between surfaces

**Simplified Approach (ASHRAE):**
Assume all surfaces at mean radiant temperature (MRT):
```
MRT = (A₁T₁ + A₂T₂ + ... + AₙTₙ) / (A₁ + A₂ + ... + Aₙ)
```

For small temperature differences:
```
q_rad,i = h_r × A × (T_surface - MRT)
```

Where:
```
h_r = 4 × ε × σ × T_mean³
```
Typical value: h_r ≈ 1.0 Btu/(hr·ft²·°F) at room temperature

### Exterior Surface Radiation

**Nighttime Sky Radiation:**
Clear sky acts as low-temperature radiation sink:
```
T_sky = T_air - ΔT_depression
```

Depression values:
- Clear, dry: ΔT = 20-40°F
- Partly cloudy: ΔT = 10-20°F
- Overcast: ΔT = 0-5°F

**Net Longwave Radiation:**
```
q_net = ε × σ × (T_surface⁴ - T_sky⁴)
```

This causes:
- Roof surface temperatures below air temperature at night
- Condensation potential on clear nights
- Enhanced cooling for night sky radiative cooling systems

### Solar Radiation Absorption

**Absorbed Solar Heat Flux:**
```
q_absorbed = α_sol × I_incident
```

Where:
- α_sol = solar absorptance
- I_incident = incident solar radiation (Btu/(hr·ft²))

**Equilibrium Temperature:**
Surface temperature rises until heat gain = heat loss:
```
α_sol × I = h_conv(T_surf - T_air) + ε_th × σ(T_surf⁴ - T_sky⁴)
```

**Sol-Air Temperature Concept:**
Equivalent air temperature accounting for solar absorption and infrared radiation:
```
T_sol-air = T_outdoor + (α_sol × I)/(h_o) - (ε × ΔR)/h_o
```

Where:
- h_o = outside surface film coefficient
- ΔR = difference between longwave radiation and surroundings

## Thermal Comfort and Radiant Effects

### Mean Radiant Temperature (MRT)

MRT represents the uniform temperature of an imaginary enclosure with which occupant exchanges same radiant heat as actual environment.

**Calculation from Surface Temperatures:**
```
MRT = [(F_p-1 × T₁⁴) + (F_p-2 × T₂⁴) + ... + (F_p-n × Tₙ⁴)]^(1/4)
```

Where F_p-i = angle factor from person to surface i

**Simplified Calculation (small temperature differences):**
```
MRT ≈ (F_p-1 × T₁) + (F_p-2 × T₂) + ... + (F_p-n × Tₙ)
```

With ΣF_p-i = 1.0

### Operative Temperature

The temperature of uniform enclosure with which occupant exchanges same total heat (convection + radiation):
```
T_op = (h_c × T_air + h_r × MRT) / (h_c + h_r)
```

For typical indoor conditions (h_c ≈ h_r):
```
T_op ≈ (T_air + MRT) / 2
```

**Comfort Implications:**
- Occupants respond to operative temperature, not air temperature alone
- Cold window (T = 30°F) can make room feel cold even with T_air = 72°F
- Radiant heating panels allow lower air temperatures with equal comfort

### Asymmetric Radiation

**Radiant Temperature Asymmetry:**
Difference in MRT experienced by opposite sides of occupant.

**Comfort Limits (ASHRAE 55):**

| Direction | Maximum Asymmetry °F | Source |
|-----------|---------------------|--------|
| Warm ceiling | 9 | Overhead radiant heating |
| Cool wall | 18 | Cold window/wall |
| Cool ceiling | 25 | Unconditioned space above |
| Warm wall | 41 | Sunlit wall, fireplace |

**Design Strategies:**

Cold windows:
- Use low-e glazing to increase inner surface temperature
- Position heating registers near windows
- Consider radiant floor/baseboard to warm adjacent surfaces

Hot ceilings:
- Limit radiant panel temperature
- Use increased air movement
- Provide local cooling

### Radiant Heating/Cooling Systems

**Surface Temperature Limits:**

Radiant heating (floor):
- Occupied areas: 84°F maximum
- Perimeter zones: 88°F maximum
- Bathrooms: 95°F maximum

Radiant cooling (ceiling):
- 66°F minimum (condensation prevention)
- 62-68°F typical operating range

**Heat Transfer Performance:**
```
q = h_total × A × (T_surface - T_op)
```

Where:
```
h_total = h_conv + h_rad
```

Floor heating: h_total ≈ 2.5-3.0 Btu/(hr·ft²·°F)
Ceiling cooling: h_total ≈ 1.5-2.0 Btu/(hr·ft²·°F)

Radiation typically accounts for 50-60% of total heat transfer.

## Components

- Radiosity Concept
- Irradiation Concept
- Diffuse Surfaces
- Specular Surfaces
- View Factor Algebra
- View Factor Relations
- Crossed Strings Method
- Contour Integration
- Hottel Strings Method
- View Factor Catalogs
