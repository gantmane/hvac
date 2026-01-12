---
title: "Occupancy Loads"
description: "Calculation of sensible and latent heat gains from building occupants for HVAC cooling load analysis and ventilation design."
keywords: ["occupancy loads", "metabolic heat", "sensible heat", "latent heat", "people load", "heat gain", "HVAC design"]
weight: 3
---

Occupancy loads represent significant internal heat gains in many building types, contributing both sensible and latent heat to conditioned spaces. Accurate estimation of occupancy loads is essential for proper HVAC system sizing and ventilation design.

## Metabolic Heat Generation

### Human Metabolism

The human body continuously generates heat through metabolic processes to maintain core temperature. Total metabolic heat production depends on activity level:

$$\dot{Q}_{metabolic} = M \times A_{Du}$$

Where:
- $M$ = metabolic rate (met or W/m²)
- $A_{Du}$ = DuBois body surface area ≈ 1.8 m² (average adult)

**1 met = 58.2 W/m² = 18.4 Btu/h·ft²** (seated, relaxed)

### Activity Levels

| Activity | Met | W/person | Btu/h·person |
|----------|-----|----------|--------------|
| Sleeping | 0.7 | 73 | 250 |
| Seated, relaxed | 1.0 | 105 | 360 |
| Office work | 1.1 | 115 | 400 |
| Standing, light work | 1.6 | 168 | 575 |
| Walking (2 mph) | 2.0 | 210 | 720 |
| Light machine work | 2.4 | 252 | 860 |
| Heavy work | 4.0 | 420 | 1,435 |
| Heavy exercise | 6.0+ | 630+ | 2,150+ |

## Sensible and Latent Components

### Heat Dissipation Mechanisms

Body heat is rejected through:

1. **Convection and radiation** (sensible)
2. **Evaporation** from skin (latent)
3. **Respiration** (sensible and latent)

The split between sensible and latent depends on activity level and environmental conditions.

### Sensible Heat Gain

Sensible heat raises air temperature and depends on:

$$\dot{Q}_{sensible} = h_c \times A_{body} \times (T_{skin} - T_{air}) + h_r \times A_{body} \times (T_{skin} - T_{MRT})$$

### Latent Heat Gain

Latent heat adds moisture to air:

$$\dot{Q}_{latent} = \dot{m}_{evap} \times h_{fg}$$

Where:
- $\dot{m}_{evap}$ = evaporation rate (kg/s)
- $h_{fg}$ = latent heat of vaporization (≈2,450 kJ/kg)

### Typical Sensible/Latent Split

| Activity | Sensible (W) | Latent (W) | Total (W) |
|----------|--------------|------------|-----------|
| Seated, light work | 70 | 45 | 115 |
| Moderate office | 75 | 55 | 130 |
| Standing, light work | 75 | 95 | 170 |
| Walking | 75 | 160 | 235 |
| Heavy work | 170 | 255 | 425 |

Note: Sensible heat relatively constant; latent increases dramatically with activity.

## Occupancy Density

### Design Occupancy Rates

ASHRAE and building codes provide default occupancy densities:

| Space Type | ft²/person | m²/person | people/1000 ft² |
|------------|------------|-----------|-----------------|
| Office, enclosed | 150 | 14 | 7 |
| Office, open plan | 100 | 9 | 10 |
| Conference room | 20 | 2 | 50 |
| Classroom | 20 | 2 | 50 |
| Retail, mall | 40 | 4 | 25 |
| Restaurant dining | 15 | 1.4 | 67 |
| Theater, auditorium | 7 | 0.65 | 150 |
| Gymnasium | 50 | 4.5 | 20 |

### Peak vs. Average Occupancy

Design must consider occupancy patterns:

**Peak Occupancy**: Maximum expected for load calculations
$$Occupancy_{peak} = Density \times Floor\ Area$$

**Average Occupancy**: For energy analysis
$$Occupancy_{average} = Occupancy_{peak} \times Diversity\ Factor$$

Typical diversity factors: 0.6-0.8 for offices, 0.5-0.7 for retail

## Load Calculation Procedures

### Basic Occupancy Heat Gain

$$Q_{people} = N \times q_{sensible} + N \times q_{latent}$$

Where:
- $N$ = number of occupants
- $q_{sensible}$ = sensible heat per person
- $q_{latent}$ = latent heat per person

### Radiant/Convective Split

Sensible heat from occupants is approximately:
- 50% radiant (affects room surfaces)
- 50% convective (directly to air)

For cooling load calculations using RTS:
- Convective portion → immediate load
- Radiant portion → delayed by room thermal mass

### Example Calculation

**Office space**: 10,000 ft² open plan

Given:
- Occupancy: 100 ft²/person = 100 occupants
- Activity: Moderate office work (130 W total, 75W sensible, 55W latent)

Sensible load: 100 × 75W = 7,500 W = 25,600 Btu/h
Latent load: 100 × 55W = 5,500 W = 18,800 Btu/h
**Total**: 13,000 W = 44,400 Btu/h

## Ventilation and Outdoor Air

### Outdoor Air Requirements

ASHRAE 62.1 mandates minimum ventilation based on occupancy:

$$\dot{V}_{oa} = R_p \times P_z + R_a \times A_z$$

Where:
- $R_p$ = per-person outdoor air rate (CFM/person)
- $P_z$ = zone population
- $R_a$ = per-area outdoor air rate (CFM/ft²)

**Typical values**: 5-20 CFM/person depending on space type

### Ventilation Cooling Load

Outdoor air introduces additional cooling load:

$$Q_{vent,sensible} = 1.1 \times CFM_{oa} \times (T_{outdoor} - T_{indoor})$$

$$Q_{vent,latent} = 0.68 \times CFM_{oa} \times (W_{outdoor} - W_{indoor})$$

This can exceed the occupancy heat gain itself in humid climates.

## Schedule Diversity

### Hourly Profiles

Occupancy varies throughout the day:

| Hour | Office | Retail | School |
|------|--------|--------|--------|
| 8 AM | 0.50 | 0.10 | 0.95 |
| 10 AM | 0.95 | 0.50 | 1.00 |
| 12 PM | 0.50 | 0.80 | 0.50 |
| 2 PM | 0.95 | 0.90 | 1.00 |
| 4 PM | 0.90 | 1.00 | 0.50 |
| 6 PM | 0.30 | 0.90 | 0.00 |

### Peak Load Timing

Occupancy peaks may not coincide with:
- Solar load peaks (afternoon)
- Transmission load peaks (delayed by thermal mass)
- Equipment load peaks (continuous processes)

Block load analysis accounts for non-coincident peaks.

## Special Considerations

### High-Activity Spaces

Gymnasiums, kitchens, and manufacturing require elevated heat gain values:
- Use activity-specific metabolic rates
- Account for hot equipment adding to latent load
- Consider heat stress implications

### Transient Occupancy

Lobbies, corridors, and circulation spaces:
- Lower effective occupancy than rated capacity
- Short duration reduces thermal impact
- Design for pass-through rather than sustained occupancy

### Occupant Comfort Feedback

High occupancy density affects:
- Air velocity perception
- Personal space thermal gradients
- CO₂ levels and perceived air quality
- Clothing variations

Accurate occupancy load estimation, combined with appropriate diversity factors and hourly profiles, ensures HVAC systems are properly sized to maintain comfort under all anticipated operating conditions.
