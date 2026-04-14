---
title: "Beer Brewing"
aliases: ["Beer Brewing"]
weight: 1
---

Brewery refrigeration systems maintain precise temperature control throughout the brewing process, from fermentation to packaging. These systems handle significant thermal loads from exothermic fermentation reactions, require exact temperature stability for flavor development, and must accommodate diverse temperature zones within a single facility.

## Brewing Process Temperature Requirements

Different brewing stages demand specific temperature control regimes that directly affect product quality and consistency.

### Fermentation Temperature Control

Fermentation generates substantial heat that must be removed to maintain yeast viability and prevent off-flavor development. The exothermic reaction produces approximately 250-280 BTU per pound of sugar fermented.

| Fermentation Type | Temperature Range | Cooling Load | Duration |
|-------------------|------------------|--------------|----------|
| Ale (Saccharomyces cerevisiae) | 60-75°F | 12,000-18,000 BTU/bbl/day | 5-10 days |
| Lager (Saccharomyces pastorianus) | 45-55°F | 8,000-12,000 BTU/bbl/day | 10-21 days |
| High-gravity fermentation | 65-72°F | 20,000-30,000 BTU/bbl/day | 7-14 days |
| Belgian styles | 68-78°F | 15,000-22,000 BTU/bbl/day | 5-12 days |

Heat generation peaks 24-48 hours after pitching yeast, requiring refrigeration systems to handle 150-200% of average loads during peak fermentation activity.

### Lagering and Cold Conditioning

Lagering requires extended low-temperature storage for flavor maturation, yeast settling, and protein precipitation. Temperature uniformity within ±0.5°F prevents convection currents that resuspend yeast.

| Conditioning Stage | Temperature | Duration | Purpose |
|-------------------|-------------|----------|---------|
| Primary lagering | 32-35°F | 3-8 weeks | Flavor maturation |
| Secondary lagering | 29-32°F | 1-4 weeks | Final conditioning |
| Cold stabilization | 28-30°F | 3-7 days | Protein precipitation |
| Crash cooling | 28-32°F | 12-48 hours | Yeast settling |

## Glycol Cooling Systems

Centralized glycol systems provide temperature control to multiple fermentation vessels and conditioning tanks through jacketed vessels or internal coils.

### Glycol System Design

Propylene glycol-water solutions (food-grade) circulate at temperatures 5-8°F below the required beer temperature to achieve adequate heat transfer rates.

| Application | Glycol Temperature | Glycol Concentration | Flow Rate |
|-------------|-------------------|---------------------|-----------|
| Ale fermentation | 55-65°F | 25-30% by volume | 3-5 GPM/bbl |
| Lager fermentation | 38-48°F | 30-35% by volume | 3-5 GPM/bbl |
| Lagering tanks | 24-28°F | 35-40% by volume | 2-4 GPM/bbl |
| Bright beer tanks | 30-35°F | 30-35% by volume | 2-3 GPM/bbl |

Higher glycol concentrations prevent freezing during lagering operations but reduce heat transfer efficiency and increase pumping energy.

### Heat Transfer Calculations

Heat transfer through jacketed vessels follows:

Q = U × A × LMTD

Where:
- Q = heat transfer rate (BTU/hr)
- U = overall heat transfer coefficient (40-60 BTU/hr·ft²·°F for jacketed vessels)
- A = heat transfer surface area (ft²)
- LMTD = log mean temperature difference (°F)

Adequate jacket coverage (60-80% of vessel surface area) ensures uniform temperature control. Insufficient coverage creates temperature gradients exceeding 2-3°F within the vessel.

## Refrigeration Plant Configuration

Brewery refrigeration plants typically employ multiple temperature levels to optimize energy efficiency across diverse cooling requirements.

### Multi-Temperature System Design

| Temperature Level | Evaporator Temperature | Applications | Refrigerant |
|------------------|----------------------|--------------|-------------|
| High-stage | 28-32°F | Bright beer, packaging | R-134a, R-513A |
| Medium-stage | 20-25°F | Ale fermentation, cellar | R-134a, R-513A |
| Low-stage | 10-15°F | Lager fermentation | R-404A, R-448A, R-449A |
| Ultra-low stage | -5 to 0°F | Lagering, cold stabilization | R-404A, R-448A |

Cascade refrigeration systems with compound compression improve efficiency when temperature differentials exceed 60-70°F between ambient and process requirements.

## Fermentation Vessel Cooling Methods

Different cooling methods provide varying degrees of temperature control and energy efficiency.

### Jacket Cooling vs Internal Coils

**Jacketed vessels:**
- External dimple jackets or full jackets
- Heat transfer coefficient: 40-60 BTU/hr·ft²·°F
- Uniform temperature distribution
- No product contact
- Higher vessel cost

**Internal cooling coils:**
- Submerged coils within fermenter
- Heat transfer coefficient: 80-120 BTU/hr·ft²·°F
- More efficient heat transfer
- Product contact surfaces require sanitary design
- Lower installation cost
- Difficult cleaning validation

## Cold Storage and Packaging Areas

Environmental control in cold storage maintains product stability and supports packaging operations.

| Area | Temperature | Relative Humidity | Air Changes |
|------|-------------|------------------|-------------|
| Bright beer cellar | 32-36°F | 75-85% | 2-4 ACH |
| Cold storage | 34-38°F | 70-80% | 2-3 ACH |
| Packaging hall | 40-50°F | 60-70% | 4-6 ACH |
| Keg cooler | 34-38°F | 80-90% | 2-3 ACH |

Packaging areas require temperature control to prevent foaming during filling operations. Beer temperature above 40°F during carbonated filling causes excessive CO₂ breakout and product loss.

## Heat Recovery Opportunities

Brewery refrigeration systems offer substantial heat recovery potential from hot gas discharge and oil coolers.

### Heat Recovery Applications

| Heat Source | Temperature Available | Application |
|-------------|---------------------|-------------|
| Hot gas discharge | 140-180°F | Hot liquor tank heating |
| Oil cooling | 110-140°F | Mash water preheating |
| Condensers | 100-120°F | CIP water heating |
| Glycol system | 50-70°F | Space heating (winter) |

Heat recovery from fermentation cooling can provide 30-40% of brewery hot water requirements, with payback periods of 2-4 years depending on energy costs.

## Ammonia Refrigeration in Large Breweries

Large production breweries (>100,000 bbl/year) frequently employ industrial ammonia refrigeration for superior efficiency and lower operating costs.

### Ammonia System Design Considerations

- Mechanical rooms isolated from process areas
- Secondary glycol loops for all process cooling
- Evaporative condensers for heat rejection
- Minimum 6-inch concrete separation walls
- Emergency ventilation: 150 CFM per ft² of machinery room floor area
- Refrigerant detection at 25 ppm threshold
- Personnel training for ammonia safety protocols

Ammonia systems achieve 15-25% lower energy consumption compared to HFC systems but require increased safety infrastructure and operator training.

## Temperature Monitoring and Control

Critical control points require continuous monitoring with alarm notification for temperature deviations exceeding ±1°F from setpoint.

### Control Strategies

**PID control loops:**
- Proportional band: 2-4°F
- Integral time: 3-8 minutes
- Derivative time: 0.5-1.5 minutes
- Prevents temperature overshoot during crash cooling

**Solenoid valve staging:**
Multiple glycol solenoid valves provide staged cooling capacity to match varying heat loads throughout fermentation cycles without hunting.

**Variable-speed glycol pumps:**
Modulate flow rates based on temperature differential, reducing pumping energy by 30-50% compared to constant-flow systems.

## Load Calculations

Peak refrigeration loads occur when multiple batches reach maximum fermentation activity simultaneously.

### Cooling Load Components

Total load (BTU/hr) = Fermentation heat + Conduction + Jacket losses + Safety factor

**Fermentation heat:**
Q_ferm = (°Plato × 0.75) × bbl × 260 BTU/lb-sugar / fermentation hours

**Typical peak loads:**
- 30-bbl fermenter (peak): 45,000-65,000 BTU/hr
- 60-bbl fermenter (peak): 90,000-130,000 BTU/hr
- 120-bbl fermenter (peak): 180,000-260,000 BTU/hr

Design refrigeration capacity at 125-150% of calculated peak load to accommodate future expansion and simultaneous batch cooling events.

## Energy Efficiency Optimization

Brewery refrigeration typically represents 30-40% of total facility energy consumption.

### Efficiency Measures

- Variable-speed compressors reduce part-load energy consumption
- Floating head pressure control lowers compression ratios
- Free cooling using ambient winter conditions (glycol temperature >35°F)
- Subcooling optimization prevents flash gas formation
- Insulation upgrades on glycol distribution piping (minimum 2-inch thickness)
- Night setback on non-critical cooling zones
- Heat recovery from compression cycle

Comprehensive efficiency programs achieve 20-30% energy reductions with payback periods under 3 years.
