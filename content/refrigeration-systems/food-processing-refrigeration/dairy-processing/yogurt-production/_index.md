---
title: "Yogurt Production"
description: "Yogurt production refrigeration systems including incubation temperature control, rapid cooling requirements, fermentation vessel cooling, storage conditions, and process cooling loads for commercial yogurt manufacturing facilities."
weight: 5
---

Yogurt production requires precise refrigeration control across multiple process stages, from milk pasteurization through fermentation and final product cooling. The thermal management demands differ significantly from fluid milk processing due to the critical temperature control required during bacterial culture incubation and the need for rapid post-fermentation cooling to halt bacterial activity at the desired pH and texture development.

## Yogurt Production Process Temperatures

The refrigeration system must accommodate the following critical temperature zones:

| Process Stage | Temperature Range | Duration | Cooling/Heating Rate | Purpose |
|--------------|-------------------|----------|---------------------|----------|
| Milk Pasteurization | 185-195°F (85-91°C) | 30 min | Heat to spec | Kill pathogens, denature whey |
| Pre-culture cooling | 108-115°F (42-46°C) | 15-30 min | -10°F/min (-5.6°C/min) | Prepare for inoculation |
| Incubation (set style) | 108-115°F (42-46°C) | 4-6 hours | ±1°F (±0.6°C) | Bacterial fermentation |
| Incubation (stirred) | 100-110°F (38-43°C) | 4-8 hours | ±1°F (±0.6°C) | Fermentation before agitation |
| Post-fermentation cooling | 40-45°F (4-7°C) | 30-90 min | -0.5 to -1.5°F/min | Halt fermentation |
| Cold storage | 36-40°F (2-4°C) | Continuous | ±1°F (±0.6°C) | Maintain quality |

## Incubation Temperature Control

Fermentation temperature control represents the most critical refrigeration challenge in yogurt production. The bacterial cultures (Lactobacillus bulgaricus and Streptococcus thermophilus) exhibit narrow optimal growth temperature ranges, and deviations of 2-3°F (1-2°C) significantly affect fermentation kinetics, final product pH, texture, and flavor profile development.

**Temperature control requirements:**

- **Set-style yogurt**: Fermentation occurs in final retail containers within temperature-controlled rooms. The refrigeration system must maintain 108-115°F (42-46°C) with spatial uniformity of ±1°F (±0.6°C) throughout the incubation chamber. Air circulation rates of 15-25 air changes per hour prevent stratification without creating excessive air velocity across containers that could cause surface cooling.

- **Stirred-style yogurt**: Fermentation occurs in jacketed vessels with precise temperature control through the vessel wall. Glycol or water circulation systems maintain 100-110°F (38-43°C) with ±0.5°F (±0.3°C) control. The jacket design must provide uniform heat transfer across the entire vessel surface to prevent localized temperature variations that create non-uniform culture development.

- **Greek-style yogurt**: Similar to stirred-style but often requires extended fermentation at slightly lower temperatures (95-105°F, 35-41°C) to achieve higher acidity before straining. Temperature uniformity becomes even more critical due to the longer fermentation period.

## Rapid Cooling Requirements

Post-fermentation cooling represents the highest instantaneous refrigeration load in yogurt production. When the product reaches the target pH (typically 4.3-4.6), immediate cooling to below 50°F (10°C) within 90 minutes halts bacterial activity and prevents over-acidification that causes excessive sourness and wheying-off.

**Cooling system design criteria:**

The required cooling capacity for a batch system:

Q = m × cp × ΔT / t

Where:
- Q = cooling capacity (Btu/hr or kW)
- m = product mass (lb or kg)
- cp = specific heat of yogurt ≈ 0.93 Btu/lb·°F (3.9 kJ/kg·K)
- ΔT = temperature change, typically 65-70°F (36-39°C)
- t = cooling time (hours)

For a 5,000 lb (2,268 kg) batch cooled from 110°F to 45°F in 60 minutes:

Q = (5,000 lb × 0.93 Btu/lb·°F × 65°F) / 1 hr = 302,250 Btu/hr (88.6 kW)

This represents product cooling only. The total system capacity must account for:

- Vessel heat capacity (typically 15-20% additional load)
- Heat of agitation (for stirred products: 0.5-1.0 hp per 1,000 gallons)
- Heat infiltration through insulation
- Safety factor of 1.15-1.25

## Cooling Methods for Yogurt

| Cooling Method | Application | Cooling Rate | Advantages | Limitations |
|----------------|-------------|--------------|------------|-------------|
| Jacketed vessel cooling | Stirred yogurt | 0.5-1.0°F/min | Gentle, controlled | Requires large jacket surface |
| Plate heat exchanger | Pumped products | 1.0-2.0°F/min | Fast, efficient | Shear stress on texture |
| Scraped surface exchanger | Set-style after breaking | 1.5-3.0°F/min | Handles viscous product | High capital cost |
| Cold room cooling | Set-style containers | 0.3-0.5°F/min | Simple, multi-batch | Slow, requires large space |
| Tunnel cooling | Packaged products | Variable | Continuous process | Limited temperature control |

## Refrigeration System Design Parameters

**Primary refrigerant selection:**

- **Ammonia (R-717)**: Used in larger facilities (>50,000 lb/day production) for process cooling loops. Provides excellent efficiency at the required evaporator temperatures of 25-30°F (-4 to -1°C) for glycol or brine secondary coolants.

- **HFO refrigerants (R-513A, R-1234yf)**: Increasingly specified for new installations due to low GWP. Suitable for medium-capacity systems with evaporator temperatures above 20°F (-7°C).

- **CO₂ (R-744)**: Emerging in cascade systems for large facilities, particularly effective when combined with waste heat recovery for pasteurization pre-heating.

**Secondary coolant systems:**

Most yogurt production facilities use secondary coolant loops to deliver cooling to process equipment:

| Coolant Type | Temperature Range | Concentration | Heat Transfer Coefficient | Application |
|--------------|-------------------|---------------|---------------------------|-------------|
| Propylene glycol | 25-35°F (-4 to 2°C) | 25-30% by weight | 150-180 Btu/hr·ft²·°F | General process cooling |
| Ethylene glycol | 20-30°F (-7 to -1°C) | 30-35% by weight | 175-200 Btu/hr·ft²·°F | Lower temperature requirements |
| Calcium chloride brine | 15-25°F (-9 to -4°C) | 23-25% by weight | 140-165 Btu/hr·ft²·°F | Legacy systems only |
| Ice water | 32-38°F (0 to 3°C) | N/A | 200-225 Btu/hr·ft²·°F | Mild cooling applications |

## Process Cooling Load Calculations

Total refrigeration capacity for a yogurt production facility must account for:

**Fermentation cooling loads:**

During fermentation, bacterial metabolism generates approximately 15-20 Btu/lb (35-47 kJ/kg) of product as heat of fermentation. For a 5,000 lb batch over 5 hours:

Heat generation = (5,000 lb × 18 Btu/lb) / 5 hr = 18,000 Btu/hr (5.3 kW)

The incubation chamber refrigeration system must remove this metabolic heat while maintaining setpoint temperature. In practice, heating is typically required initially, with cooling becoming necessary as fermentation progresses and approaches peak bacterial activity at 3-4 hours.

**Additional cooling loads:**

- **Fruit preparation cooling**: 40-50 Btu/lb (93-116 kJ/kg) when fruit preparations are cooled from ambient to 40°F (4°C) before blending
- **Packaging room cooling**: 35-45°F (2-7°C) at 40-50% RH to prevent condensation on cold containers
- **Cold storage**: Bulk product storage at 36-40°F (2-4°C) requires insulated rooms with 0.25-0.35 W/ft² (2.7-3.8 W/m²) heat gain
- **Cleaning system cooling**: CIP return cooling to maintain bacterial control in recovered rinse water

## Storage Conditions and Requirements

Finished yogurt storage requires precise environmental control to maintain product quality throughout the declared shelf life of 30-45 days:

**Temperature requirements:**

- Maintain 36-40°F (2-4°C) in distribution cold storage
- Temperature uniformity within ±1°F (±0.6°C) throughout storage volume
- Minimize temperature cycling; fluctuations above 45°F (7°C) accelerate wheying-off and texture breakdown
- Air-on temperature differential of 8-12°F (4-7°C) to minimize running time while preventing excessive temperature swings

**Humidity control:**

Relative humidity of 85-90% prevents moisture loss from containers while avoiding condensation formation. Lower humidity causes package label degradation and product weight loss; higher humidity promotes mold growth on exposed surfaces and creates slip hazards on floors.

**Air distribution:**

Design air velocity at product level below 50 fpm (0.25 m/s) to prevent accelerated heat transfer to top layers. Vertical air distribution with floor-level returns provides superior temperature uniformity compared to overhead systems in rooms with pallet stacking heights exceeding 12 feet (3.7 m).

## Glycol System Sizing

Secondary coolant systems for yogurt production typically operate with 10-15°F (5.6-8.3°C) approach between refrigerant evaporating temperature and glycol supply temperature. For a system supplying 30°F (-1°C) glycol with 10°F (5.6°C) return rise:

Required glycol flow rate:

GPM = (Q × 12) / (ΔT × ρ × cp × 60)

Where:
- Q = cooling load (ton refrigeration)
- ΔT = temperature rise, 10°F (5.6°C)
- ρ = glycol density ≈ 8.5 lb/gal for 30% propylene glycol
- cp = specific heat ≈ 0.95 Btu/lb·°F

For 100 tons (352 kW) cooling capacity:

GPM = (100 × 12,000) / (10 × 8.5 × 0.95 × 60) = 248 GPM (56.4 m³/hr)

Pump selection must account for pressure drop through heat exchangers, piping, and control valves. Typical systems experience 20-35 psi (138-241 kPa) total pressure drop, requiring pumps with 50-80 feet (15-24 m) total dynamic head.

## Heat Recovery Opportunities

Yogurt production presents significant heat recovery potential:

- **Condenser heat recovery**: Hot gas desuperheating can provide 140-180°F (60-82°C) water for CIP pre-rinse and pasteurizer pre-heating, recovering 15-25% of total refrigeration energy input
- **Pasteurizer regeneration**: Plate heat exchangers recover heat from hot pasteurized milk to pre-warm incoming cold milk, reducing both heating and cooling loads by 70-85%
- **Compressor jacket cooling**: Water-cooled compressor jackets produce 110-130°F (43-54°C) water suitable for facility hot water needs or additional pasteurizer pre-heating

Integrated heat recovery systems in modern yogurt facilities achieve overall energy efficiency improvements of 30-40% compared to standalone heating and cooling systems, with payback periods of 2-4 years depending on energy costs and production scale.
