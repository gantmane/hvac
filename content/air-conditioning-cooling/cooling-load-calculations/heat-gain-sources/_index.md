---
title: "Heat Gain Sources"
description: "Detailed analysis of HVAC cooling load heat gain sources including solar radiation, transmission, infiltration, and internal gains from occupants and equipment."
date: "2026-01-04"
weight: 1
tags: ["solar-gain", "transmission", "infiltration", "internal-loads", "heat-sources"]
categories: ["air-conditioning-cooling"]
---

Heat gain sources represent all pathways through which thermal energy enters conditioned spaces. Understanding each source enables accurate load calculations and identification of energy efficiency opportunities.

## Solar Radiation Heat Gain

Solar radiation represents the dominant external load for buildings with significant glazing. Solar heat gain depends on geographic location, time of year, time of day, orientation, and shading.

### Solar Geometry

**Solar Altitude Angle** ($\beta$): Angle between sun and horizontal plane:

$$\sin \beta = \cos L \cos \delta \cos H + \sin L \sin \delta$$

where:
- $L$ = latitude
- $\delta$ = solar declination
- $H$ = hour angle

**Solar Azimuth Angle** ($\psi$): Horizontal angle from south to sun position.

### Solar Radiation Components

**Direct Radiation**: Beam radiation from sun traveling straight path to surface.

**Diffuse Radiation**: Scattered radiation from sky and clouds.

**Reflected Radiation**: Radiation reflected from ground and surroundings.

**Total Incident** on surface:

$$I_{total} = I_{direct} + I_{diffuse} + I_{reflected}$$

### Window Solar Gain

**Solar Heat Gain Coefficient (SHGC)**: Fraction of incident solar radiation transmitted as heat:

$$q_{solar} = A_{window} \times SHGC \times I_{incident}$$

SHGC values:
- Single clear: 0.80-0.85
- Double clear: 0.65-0.75
- Double low-E: 0.25-0.60
- Triple low-E: 0.15-0.40

**Shading Coefficient (SC)**: Ratio of SHGC to reference single clear glass:

$$SC = \frac{SHGC}{0.87}$$

### External Shading Effects

**Overhangs**: Reduce solar gain on south-facing windows in summer:

$$Shadow\,Depth = Overhang \times \tan(\beta)$$

**Fins**: Reduce gain on east/west facades:

$$Shadow\,Width = Fin \times \frac{\sin(\psi)}{\cos(\beta)}$$

**Interior Shading**: Blinds, shades, curtains with Interior Attenuation Coefficients (IAC):
- Fully open: IAC = 1.0
- Light blinds closed: IAC = 0.55-0.75
- Dark blinds closed: IAC = 0.45-0.65
- Blackout shades: IAC = 0.15-0.25

**Effective SHGC**:

$$SHGC_{eff} = SHGC_{glass} \times IAC$$

## Transmission Heat Gain

Conductive heat transfer through building envelope depends on temperature difference, material thermal resistance, and surface area.

### Walls and Roofs

**Heat Gain Through Opaque Surfaces**:

$$q = U \times A \times \Delta T$$

where:
- $U$ = overall heat transfer coefficient (W/m²·K)
- $A$ = surface area (m²)
- $\Delta T$ = temperature difference (K)

**U-Factor Calculation**:

$$U = \frac{1}{R_{total}} = \frac{1}{R_{out} + R_{wall} + R_{insulation} + R_{in}}$$

Typical U-factors (W/m²·K):
- Uninsulated wall: 2.0-3.0
- Wall with R-3.5 insulation: 0.4-0.6
- Wall with R-7 insulation: 0.2-0.3
- Roof with R-7 insulation: 0.2-0.3

### Sol-Air Temperature

Accounts for combined effects of outdoor air temperature and solar radiation on exterior surface:

$$T_{sol-air} = T_{outdoor} + \frac{\alpha I_{solar}}{h_o} - \frac{\epsilon \Delta R}{h_o}$$

where:
- $\alpha$ = solar absorptance (0.3-0.9 depending on color)
- $I_{solar}$ = incident solar radiation (W/m²)
- $h_o$ = outside surface heat transfer coefficient
- $\epsilon$ = surface emissivity
- $\Delta R$ = longwave radiation correction

For dark surfaces in full sun, sol-air temperature can exceed outdoor air by 20-30°C (36-54°F).

### Windows - Conduction

Window conduction independent of solar gain:

$$q_{cond} = U_{window} \times A \times (T_{outdoor} - T_{indoor})$$

Typical window U-factors (W/m²·K):
- Single glazing: 5.0-6.0
- Double glazing: 2.5-3.0
- Double low-E: 1.5-2.0
- Triple low-E: 0.8-1.2

### Thermal Mass Effects

Heavy construction (concrete, masonry) delays and dampens heat gain peaks:

**Decrement Factor**: Ratio of interior to exterior temperature swing:

$$f = \frac{\Delta T_{interior}}{\Delta T_{exterior}} < 1.0$$

**Time Lag**: Delay between exterior and interior peak temperatures:

$$\phi = f(mass, thermal\,diffusivity, thickness)$$

Typical values:
- Lightweight (wood frame): 1-2 hours
- Medium weight (brick veneer): 3-5 hours
- Heavyweight (concrete): 6-12 hours

## Infiltration and Ventilation

### Infiltration

Uncontrolled air leakage through cracks and openings in building envelope.

**Crack Method**: Based on measured leakage areas:

$$\dot{Q}_{inf} = \frac{AL}{1000} \times \sqrt{\Delta P}$$

where:
- $AL$ = effective leakage area (cm²)
- $\Delta P$ = pressure difference (Pa)

**Air Changes Method**: Simplified residential approach:

$$\dot{V}_{inf} = \frac{ACH \times Volume}{60}$$

Typical ACH values (air changes per hour):
- Tight construction: 0.1-0.3
- Average: 0.3-0.6
- Loose: 0.6-1.0

**Heat Gain from Infiltration**:

Sensible:
$$q_s = \dot{m}_{inf} \times c_p \times (T_{outdoor} - T_{indoor})$$

Latent:
$$q_l = \dot{m}_{inf} \times h_{fg} \times (W_{outdoor} - W_{indoor})$$

### Ventilation

Controlled outdoor air for IAQ per ASHRAE 62.1:

$$\dot{V}_{vent} = R_p \times P + R_a \times A$$

where:
- $R_p$ = outdoor air per person (L/s per person)
- $P$ = number of people
- $R_a$ = outdoor air per floor area (L/s per m²)
- $A$ = floor area (m²)

Typical office: 2.5 L/s per person + 0.3 L/s per m²

**Ventilation Load** often represents 20-40% of total cooling load.

## Internal Heat Gains

### Occupants

People generate both sensible and latent heat.

**Sensible Heat per Person**:

$$q_s = f(activity, clothing, temperature)$$

ASHRAE values at 24°C (75°F):

| Activity | Sensible (W) | Latent (W) | Total (W) |
|----------|--------------|------------|-----------|
| Seated, quiet | 65 | 55 | 120 |
| Seated, light work | 70 | 80 | 150 |
| Standing, light work | 75 | 90 | 165 |
| Walking slowly | 75 | 115 | 190 |
| Office work | 70 | 80 | 150 |
| Heavy work | 90 | 255 | 345 |

**Diversity**: All occupants rarely present simultaneously:

$$q_{actual} = q_{per\,person} \times Occupancy \times Diversity$$

Typical diversity factors:
- Office: 0.7-0.9
- Classroom: 0.8-1.0
- Restaurant: 0.5-0.8

### Lighting

**Heat Gain from Lighting**:

$$q_{lights} = Watts_{installed} \times F_{use} \times F_{ballast}$$

where:
- $F_{use}$ = usage factor (0-1.0)
- $F_{ballast}$ = ballast factor

Fluorescent/LED ballast factors: 1.10-1.20

**Lighting Power Density (LPD)**: ASHRAE 90.1 limits:

| Space Type | Max LPD (W/m²) |
|------------|----------------|
| Office | 9.7 |
| Classroom | 12.9 |
| Retail | 14.0 |
| Warehouse | 7.5 |

**Radiant/Convective Split**:
- Incandescent: 80% radiant, 20% convective
- Fluorescent: 50% radiant, 50% convective
- LED: 40% radiant, 60% convective

Radiant portion experiences thermal lag; convective portion becomes immediate cooling load.

### Equipment

**Office Equipment**:

| Equipment | Peak Load (W) | Diversity | Usage Factor |
|-----------|---------------|-----------|--------------|
| Desktop PC | 100-150 | 0.5-0.7 | 0.4-0.6 |
| Laptop | 20-50 | 0.6-0.8 | 0.5-0.7 |
| Monitor 24" | 30-50 | 0.8 | 0.6-0.8 |
| Laser printer | 400-600 | 0.3 | 0.2-0.4 |
| Copier | 800-1500 | 0.2 | 0.1-0.3 |

**Equipment Power Density (EPD)**:

- Open office: 8-12 W/m²
- Private office: 6-10 W/m²
- Server room: 100-500 W/m²

**Nameplate vs. Actual**: Equipment rarely operates at nameplate rating:

$$q_{actual} = q_{nameplate} \times Load\,Factor \times Diversity$$

**Latent Gains**: Some equipment produces moisture:
- Cooking equipment: 30-50% latent
- Commercial dishwashers: 50-70% latent
- Indoor plants: evapotranspiration

### Motors

**Heat Gain from Motors**:

If motor and driven equipment both in space:

$$q = \frac{P_{motor}}{\eta_{motor}}$$

If motor in space, driven equipment outside:

$$q = P_{motor}(1 - \eta_{motor})$$

where $\eta_{motor}$ is motor efficiency (0.80-0.95).

## Domestic Hot Water

In buildings with hot water systems, pipe losses and fixture usage contribute:

**Standby Losses** from tanks and piping:

$$q_{standby} = UA(T_{water} - T_{ambient})$$

**Usage Gains**: Brief peaks during fixture use, typically neglected in load calculations unless continuous (commercial kitchen).

## Heat Gain Summary Table

Typical office building (warm climate):

| Source | Peak Gain (W/m²) | % of Total |
|--------|------------------|------------|
| Solar (windows) | 35-50 | 25-30% |
| Transmission | 15-25 | 10-15% |
| Infiltration | 5-10 | 5% |
| Ventilation | 20-30 | 15-20% |
| Lighting | 10-15 | 10% |
| Equipment | 10-15 | 10% |
| Occupants | 10-15 | 10% |
| **Total** | **105-160** | **100%** |

Variations depend on:
- Climate zone
- Building orientation and glazing area
- Occupancy density
- Equipment density
- Operating schedule
- Envelope performance

Understanding heat gain sources enables targeted energy efficiency improvements: reducing solar gain through shading and low-SHGC glazing, improving envelope insulation, minimizing infiltration, using efficient lighting and equipment, and optimizing ventilation rates all reduce cooling loads and energy consumption.
