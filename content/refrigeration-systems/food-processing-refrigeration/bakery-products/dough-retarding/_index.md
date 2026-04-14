---
title: "Dough Retarding"
aliases: ["Dough Retarding"]
weight: 1
---

Dough retarding refrigeration systems control fermentation kinetics by reducing yeast metabolism through precise temperature management. These systems enable production flexibility by allowing formed dough products to be held for extended periods before baking while maintaining optimal gluten structure and gas retention characteristics.

## Fermentation Control Principles

The retarding process manipulates biochemical reaction rates through temperature depression. Yeast fermentation rate approximately doubles for each 10°C (18°F) temperature increase within the optimal range, following modified Arrhenius kinetics. Retarding temperatures of 2-4°C (36-39°F) reduce fermentation rates by approximately 80-90% compared to proof box conditions at 38°C (100°F).

The temperature reduction must occur gradually to prevent thermal shock to the dough structure. Rapid cooling creates temperature gradients that cause differential fermentation rates within the dough mass, leading to irregular cell structure and compromised final product quality.

## Temperature Profiles and Control Strategies

Dough retarding follows specific cooling and holding profiles based on dough type and intended holding duration.

### Standard Retarding Profile

The conventional retarding sequence:

1. **Initial cooling phase**: Reduce dough temperature from 24-27°C (75-81°F) to 10-12°C (50-54°F) over 60-90 minutes
2. **Secondary cooling**: Continue cooling to 2-4°C (36-39°F) over next 2-3 hours
3. **Holding phase**: Maintain 2-4°C (36-39°F) for duration of retarding period
4. **Controlled warming**: Gradual temperature increase to 15-18°C (59-64°F) before final proofing

The gradual cooling prevents skin formation, maintains even moisture distribution, and allows controlled fermentation throughout the cooling cycle.

### Extended Retarding Systems

For holding periods exceeding 48 hours, modified temperature profiles maintain dough viability:

- Hours 0-4: Cooling phase to 4°C (39°F)
- Hours 4-24: Hold at 2-3°C (36-37°F)
- Hours 24-72: Maintain 1-2°C (34-36°F) to minimize residual fermentation
- Beyond 72 hours: Temperatures approaching 0°C (32°F) with enhanced humidity control

## Psychrometric Requirements

Dough retarding demands precise humidity control to prevent surface drying while avoiding condensation formation.

| Retarding Phase | Temperature | Relative Humidity | Dew Point |
|-----------------|-------------|-------------------|-----------|
| Initial cooling | 10-12°C (50-54°F) | 85-90% | 8-11°C (46-52°F) |
| Secondary cooling | 4-8°C (39-46°F) | 80-85% | 2-6°C (36-43°F) |
| Holding | 2-4°C (36-39°F) | 75-80% | 0-2°C (32-36°F) |
| Pre-proof warming | 15-18°C (59-64°F) | 70-75% | 10-13°C (50-55°F) |

The relative humidity decreases during the holding phase because the dough surface gradually equilibrates with the chamber conditions. Excessive humidity (>85% during holding) promotes surface stickiness and bacterial growth, while insufficient humidity (<70%) causes skin formation that restricts oven spring.

## Refrigeration System Design Parameters

Dough retarding refrigeration systems require specific design considerations distinct from conventional cold storage applications.

### Cooling Load Components

| Load Component | Typical Value | Design Considerations |
|----------------|---------------|----------------------|
| Product sensible heat | 40-50% of total | Based on dough specific heat 3.35 kJ/kg·K (0.80 BTU/lb·°F) |
| Fermentation heat | 15-25% of total | Active yeast metabolism: 420 kJ/kg dry yeast/hr (180 BTU/lb/hr) |
| Infiltration load | 10-15% of total | Door openings during loading/unloading operations |
| Equipment heat | 5-10% of total | Rack motors, conveyor drives, lighting |
| Structural transmission | 10-15% of total | Wall/floor/ceiling heat gain |

The fermentation heat load decreases exponentially as dough temperature declines. Initial cooling phase experiences the highest metabolic heat generation, requiring 60-70% of installed refrigeration capacity.

### Evaporator Design Requirements

Dough retarding evaporators must satisfy conflicting requirements:

- **Low air velocity**: 1.0-2.5 m/s (200-500 fpm) across dough surfaces to prevent drying
- **High heat transfer coefficient**: Requires increased coil surface area (30-40% greater than conventional cold storage)
- **Minimal temperature differential**: Evaporator TD of 3-5°C (5-9°F) to maintain humidity and prevent freezing
- **Defrost frequency**: Every 6-8 hours due to high latent load from dough moisture

The combination of high humidity and low temperature differential demands evaporators with 1.5-2.0 times the surface area of conventional cold storage applications at equivalent capacity.

## Air Distribution Systems

Proper air circulation maintains uniform temperatures throughout the retarding space without creating excessive air movement across dough surfaces.

### Circulation Patterns

Horizontal laminar flow provides optimal conditions:

- Supply air introduced at one end of retarder at 0.5-1.0 m/s (100-200 fpm)
- Air flows parallel to rack levels
- Return air collected at opposite end
- Mixing dampers blend return air with discharge to moderate temperature swings

Vertical air distribution systems create temperature stratification and uneven cooling rates across different rack levels, resulting in inconsistent product quality.

### Air Change Rates

| Retarding Phase | Air Changes per Hour | Velocity at Product Surface |
|-----------------|---------------------|----------------------------|
| Initial cooling | 15-20 | 1.5-2.5 m/s (300-500 fpm) |
| Secondary cooling | 8-12 | 1.0-1.5 m/s (200-300 fpm) |
| Holding | 4-6 | 0.5-1.0 m/s (100-200 fpm) |

Higher air change rates during initial cooling accelerate temperature reduction, while reduced circulation during holding minimizes product dehydration.

## Dough Type-Specific Parameters

Different dough formulations require adjusted retarding conditions based on hydration level, fat content, and fermentation characteristics.

| Dough Type | Temperature Range | Hold Time | RH Range | Critical Control |
|------------|-------------------|-----------|----------|------------------|
| Lean dough (baguettes) | 2-4°C (36-39°F) | 8-24 hours | 75-80% | Prevent skinning |
| Enriched dough (brioche) | 4-6°C (39-43°F) | 12-36 hours | 70-75% | Fat crystallization |
| Laminated dough (croissant) | 2-4°C (36-39°F) | 12-48 hours | 70-75% | Butter layer integrity |
| High-hydration dough | 2-3°C (36-37°F) | 8-16 hours | 80-85% | Structural collapse prevention |
| Pizza dough | 4-6°C (39-43°F) | 24-72 hours | 75-80% | Extensibility development |

Laminated doughs present unique challenges because the butter layers must remain solid (below 15°C/59°F) while the dough remains pliable. Temperature uniformity within ±0.5°C (±1°F) throughout the retarding period prevents butter migration or separation.

## Control Systems and Instrumentation

Precise control systems maintain the narrow temperature and humidity ranges required for optimal dough retarding.

### Temperature Control

- **Sensor placement**: Multiple RTD sensors (±0.1°C accuracy) distributed throughout the space
- **Control algorithm**: PID with adaptive gain scheduling based on load conditions
- **Compressor staging**: Variable capacity or multiple compressors for load matching
- **Set point adjustment**: Programmable profiles for different dough types and holding durations

Step changes in cooling capacity must be limited to prevent temperature overshoot, which can cause localized freezing and permanent dough damage.

### Humidity Control

Humidity maintenance relies on system balance rather than active humidification:

- **Evaporator TD management**: Maintaining minimum practical TD preserves humidity
- **Defrost strategy**: Hot gas defrost with rapid termination minimizes moisture introduction
- **Vapor barriers**: Comprehensive sealing of insulated envelope prevents moisture loss
- **Infiltration control**: Vestibules or rapid-acting doors limit dry air ingress

Active steam injection systems typically prove unnecessary and create condensation problems when dew point exceeds surface temperatures of refrigeration components.

## Defrost Strategies

The high humidity environment and minimal temperature differential create continuous frost accumulation on evaporator coils.

### Hot Gas Defrost System

Hot gas defrost provides the most effective approach:

- Initiation criteria: Evaporator TD increase of 2°C (3.6°F) above baseline
- Duration: 8-12 minutes per cycle
- Frequency: Every 6-8 hours during active retarding
- Termination: Coil temperature reaches 10-12°C (50-54°F)

Defrost cycle timing must coordinate with production schedules to avoid temperature fluctuations during critical cooling phases.

## Energy Recovery Opportunities

Dough retarding operations present heat recovery potential from the refrigeration system's condenser heat rejection.

Heat recovery applications:

- **Proof box heating**: Recovered heat supplies 30-40°C (86-104°F) process heat
- **Domestic hot water**: Pre-heating to 45-50°C (113-122°F) before final heating
- **Space heating**: Winter heating for production areas
- **Floor heating**: Maintaining bakery floor temperatures above dew point

A coefficient of performance (COP) of 2.5-3.0 for the refrigeration system means 1.5-2.0 kW of recoverable heat for each kW of cooling capacity, representing significant energy savings potential.

## Common Operational Challenges

Several failure modes affect dough retarding system performance:

**Surface drying**: Results from excessive air velocity, low humidity, or extended holding beyond designed duration. Manifests as skin formation preventing proper oven spring.

**Uneven cooling**: Caused by insufficient air circulation, improper loading patterns, or temperature stratification. Produces variable fermentation rates within the same batch.

**Over-retarding**: Occurs when holding temperature too low or duration too long, depleting yeast viability and resulting in dense, poor-volume products.

**Condensation**: Forms when warm, moist air contacts cold surfaces during door openings or inadequate insulation. Creates sticky dough surfaces and bacterial growth risk.

## System Sizing Example

For a retarding system handling 500 kg (1,100 lb) dough per batch:

Product cooling load: Q₁ = m × c_p × ΔT = 500 kg × 3.35 kJ/kg·K × (25-3)K = 36,850 kJ/batch

Over 4-hour cooling cycle: Q₁ = 36,850 kJ / (4 × 3,600 s) = 2.56 kW sensible cooling

Fermentation heat (first 2 hours): Q₂ ≈ 1.5-2.0 kW

Total installed capacity with safety factor: 2.56 + 2.0 = 4.56 kW × 1.3 = 5.9 kW (2.0 tons)

This calculation provides the minimum refrigeration capacity; actual systems typically include 40-50% additional capacity for multiple batch loading and accelerated cooling requirements.
