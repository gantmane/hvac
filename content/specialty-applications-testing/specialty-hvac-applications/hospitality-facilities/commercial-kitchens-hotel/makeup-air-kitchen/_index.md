---
title: "Makeup Air Systems for Hotel Commercial Kitchens"
aliases: ["Makeup Air Systems for Hotel Commercial Kitchens"]
description: "Engineering analysis of makeup air delivery methods, volume calculations, hood integration, temperature conditioning, and pressure balancing for hotel kitchen HVAC systems."
keywords: ["makeup air", "kitchen ventilation", "commercial kitchen HVAC", "exhaust hood", "air balance", "short-circuit hood", "negative pressure", "kitchen air curtain"]
tags: ["makeup air", "kitchen ventilation", "commercial kitchen HVAC", "exhaust hood", "air balance", "short-circuit hood", "negative pressure", "kitchen air curtain"]
date: 2025-01-11
draft: false
weight: 2
---

Makeup air systems provide critical replacement air for hotel commercial kitchens to compensate for exhaust volumes while maintaining proper building pressurization, occupant comfort, and energy efficiency. Proper makeup air design prevents negative pressure issues, reduces infiltration, and ensures exhaust hood performance.

## Makeup Air Volume Requirements

The fundamental principle of makeup air design is mass balance. The volume of air exhausted must be replaced to maintain pressure control.

### Basic Makeup Air Calculation

For a commercial kitchen, the total makeup air requirement is:

$$Q_{MA} = Q_{hood} + Q_{misc} - Q_{transfer}$$

Where:
- $Q_{MA}$ = Required makeup air volume (CFM)
- $Q_{hood}$ = Total exhaust hood airflow (CFM)
- $Q_{misc}$ = Miscellaneous exhaust (restrooms, trash rooms) (CFM)
- $Q_{transfer}$ = Transfer air from adjacent spaces (CFM)

### Direct vs. Transfer Air Strategy

**Direct Makeup Air** is supplied directly to the kitchen space through dedicated makeup air units. The percentage of exhaust that must be replaced by direct makeup air:

$$\%_{direct} = \frac{Q_{hood} - Q_{transfer}}{Q_{hood}} \times 100$$

**Transfer Air** is conditioned air supplied to dining areas that migrates to the kitchen through door undercuts, grilles, or vestibules. Transfer air should not exceed 10% of exhaust volume for pressure control, though 20-30% is common in practice:

$$Q_{transfer,max} = 0.10 \times Q_{hood}$$

### Pressure Relationship

Kitchen negative pressure relative to dining areas should be maintained at -0.02 to -0.05 inches water column (5-12 Pa) to contain odors while avoiding excessive negative pressure:

$$\Delta P = \frac{(Q_{exhaust} - Q_{supply})^2 \times \rho}{2 \times C_d^2 \times A^2}$$

Where:
- $\Delta P$ = Pressure differential (inches w.c.)
- $\rho$ = Air density (lb/ft³)
- $C_d$ = Discharge coefficient (typically 0.6-0.7)
- $A$ = Effective leakage area (ft²)

## Short-Circuit Hood Design Integration

Short-circuit makeup air hoods deliver conditioned makeup air directly at the hood face, improving capture efficiency and reducing the volume of air that must be conditioned.

### Short-Circuit Hood Performance

Short-circuit hoods can reduce total makeup air requirements by 20-40% compared to general area delivery. The effective exhaust reduction:

$$Q_{hood,effective} = Q_{hood} - (0.20 \text{ to } 0.40) \times Q_{hood}$$

**Advantages:**
- Reduced makeup air conditioning load
- Improved capture and containment efficiency
- Lower supply air velocities in kitchen workspace
- Better temperature gradient control

**Design Considerations:**
- Supply air velocity at hood face: 50-100 FPM
- Supply air temperature: 50-70°F maximum below space temperature
- Supply discharge positioned 6-12 inches from hood face
- Avoid cross-drafts that disrupt hood capture

### Discharge Location Effects

| Location | Capture Efficiency | Conditioning Load | Comfort Impact |
|----------|-------------------|-------------------|----------------|
| Within hood canopy | 90-95% | Lowest | Minimal |
| Hood perimeter (short-circuit) | 85-90% | Low | Low |
| General area low sidewall | 75-80% | Moderate | Moderate |
| General area high sidewall | 70-75% | High | High |

## Heating and Cooling Makeup Air

Makeup air must be conditioned to maintain kitchen comfort and prevent thermal shock to equipment and personnel.

### Heating Requirements

In heating season, makeup air must be heated to prevent discomfort and equipment condensation. Minimum supply temperature:

$$T_{supply,min} = T_{space} - 20°F$$

For a 75°F kitchen, minimum supply temperature is 55°F.

Heating capacity required:

$$Q_{heat} = 1.08 \times Q_{MA} \times (T_{supply} - T_{ambient})$$

Where:
- $Q_{heat}$ = Heating capacity (BTU/hr)
- 1.08 = Constant for air (CFM × °F to BTU/hr)
- $T_{ambient}$ = Outdoor air temperature (°F)

### Cooling Requirements

Makeup air cooling reduces kitchen heat gain during hot weather. Cooling load:

$$Q_{cool} = 1.08 \times Q_{MA} \times (T_{ambient} - T_{supply}) + 0.68 \times Q_{MA} \times (W_{ambient} - W_{supply})$$

The second term accounts for latent cooling, where:
- 0.68 = Latent heat constant
- $W$ = Humidity ratio (grains moisture/lb dry air)

### Energy Recovery Integration

Energy recovery systems capture heat from kitchen exhaust to precondition makeup air, reducing operating costs:

- **Run-around coil loops:** 45-55% effectiveness
- **Heat pipe exchangers:** 50-65% effectiveness
- **Indirect evaporative cooling:** 60-75% effectiveness for cooling

Energy savings from recovery:

$$\text{Savings} = \eta \times Q_{MA} \times 1.08 \times (T_{exhaust} - T_{ambient}) \times \text{Hours}$$

Where $\eta$ is heat recovery effectiveness.

## Air Curtain Applications

Air curtains at kitchen doorways minimize air transfer and maintain pressure separation between kitchen and dining areas while allowing traffic flow.

### Air Curtain Sizing

Required air curtain velocity:

$$V_{curtain} = 1.5 \times \sqrt{\frac{2 \times \Delta P}{\rho}}$$

For typical kitchen pressure of -0.03 inches w.c.:

$$V_{curtain} = 1.5 \times \sqrt{\frac{2 \times 0.03}{0.075}} = 1.5 \times 0.89 = 1.34 \text{ ft/s}$$

Converted to FPM: approximately 80 FPM at door center.

**Air Curtain Performance Factors:**
- Discharge velocity: 500-1000 FPM at nozzle
- Air volume: 150-250 CFM per linear foot of door width
- Effectiveness: 60-80% reduction in air transfer
- Heated air curtains required in cold climates

## Kitchen Air Balance Strategy

```mermaid
graph TD
    A[Outdoor Air<br/>100% of Makeup Air] --> B[Makeup Air Unit<br/>Heat/Cool]
    B --> C[Kitchen Space<br/>75°F, -0.03" w.c.]
    D[Dining Room<br/>72°F, Neutral] -->|Transfer Air<br/>10-20%| C
    C --> E[Exhaust Hood<br/>Primary Exhaust]
    C --> F[General Exhaust<br/>Restrooms/Storage]
    E --> G[Grease Removal<br/>Filters/ESP]
    F --> H[Exhaust to Atmosphere]
    G --> H
    B -.->|Short-Circuit<br/>at Hood Face| E
    I[Air Curtain] -->|Door Seal| C
    D ---|Pressure Gradient| C

    style C fill:#ffe6e6
    style B fill:#e6f3ff
    style E fill:#fff4e6
```

## Makeup Air Delivery Strategies Comparison

| Strategy | Conditioning Load | Installation Cost | Operating Cost | Kitchen Comfort | Capture Efficiency |
|----------|------------------|-------------------|----------------|-----------------|-------------------|
| 100% Short-Circuit at Hood | Low | High | Low | Excellent | 90-95% |
| 80% Short-Circuit, 20% General | Low-Moderate | Moderate-High | Low-Moderate | Very Good | 85-90% |
| 50% Perimeter, 50% General | Moderate | Moderate | Moderate | Good | 80-85% |
| 100% General Low Sidewall | High | Low | High | Fair | 75-80% |
| 100% General High Sidewall | Very High | Low | Very High | Poor | 70-75% |

## Energy Efficiency Strategies

### Demand-Controlled Kitchen Ventilation (DCKV)

Modulate exhaust and makeup air based on cooking activity using:
- **Optical sensors** detecting smoke/steam
- **Temperature sensors** at hood face
- **Appliance interlocks** tied to equipment operation

Energy savings potential: 30-50% compared to constant volume operation.

Turndown relationship:

$$Q_{variable} = Q_{design} \times (0.30 \text{ to } 1.0)$$

Minimum ventilation maintains 30% of design exhaust during idle periods.

### Thermal Destratification

Ceiling fans or destratification units recirculate hot air accumulated at ceiling (often 90-110°F) back to occupied zone, reducing makeup air heating load:

$$Q_{saved} = 1.08 \times Q_{destrat} \times (T_{ceiling} - T_{occupied})$$

Savings of 10-20% on heating energy are achievable in high-ceiling kitchens.

### Night Setback and Purge

**Night Setback:** Reduce makeup air temperature to 50-55°F during unoccupied hours.

**Morning Purge:** Operate exhaust at 50-70% to remove overnight buildup before full production, then ramp to full flow.

### Variable Frequency Drives (VFDs)

VFDs on makeup air and exhaust fans provide:
- Fan energy proportional to cube of speed: $P \propto \omega^3$
- 30% airflow reduction yields 66% energy reduction
- Soft starting reduces electrical demand charges

## Pressure Control and Balancing

Maintain proper kitchen pressure through:

1. **Exhaust 10-15% greater than supply** to maintain negative pressure
2. **Airflow monitoring stations** on makeup air and exhaust
3. **Pressure sensors** measuring kitchen-to-dining differential
4. **Building automation control** modulating makeup air dampers

**Commissioning Verification:**
- Measure pressure at multiple kitchen locations
- Verify airflow at all supply and exhaust points
- Perform smoke test at doorways during peak operation
- Validate control sequences under varying loads

Proper makeup air system design balances energy efficiency, occupant comfort, code compliance, and operational performance. Short-circuit delivery, demand control, and energy recovery represent best practices for modern hotel kitchen HVAC systems.
