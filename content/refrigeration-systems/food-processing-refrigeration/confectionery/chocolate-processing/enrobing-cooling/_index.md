---
title: "Enrobing Cooling"
aliases: ["Enrobing Cooling"]
description: "Enrobing cooling tunnel design for chocolate solidification including zone temperature control, air velocity profiles, humidity management, and bloom prevention strategies for confectionery production"
weight: 2
---

Enrobing cooling tunnels provide controlled solidification of chocolate coatings applied to confectionery products. The cooling process crystallizes cocoa butter in the desired polymorphic form (Form V beta crystals) while preventing surface defects including bloom, cracking, and inadequate gloss. HVAC system design controls temperature gradients, air velocity profiles, and humidity levels throughout multiple cooling zones.

## Enrobing Process Overview

Chocolate enrobing applies a uniform coating to confectionery centers through a continuous curtain of tempered chocolate. Products pass through the enrober on a wire belt at controlled speeds ranging from 2 to 15 m/min. The coating thickness depends on chocolate viscosity (typically 3000 to 6000 cP at 31-32°C), belt speed, and excess removal by air knives or vibration.

After coating application, products enter the cooling tunnel where controlled refrigeration solidifies the chocolate shell. The cooling rate determines crystal structure formation, surface appearance, and snap characteristics. Excessive cooling rates (>5°C/min) cause thermal shock leading to fat bloom, while insufficient cooling (<0.5°C/min) permits undesirable crystal growth and soft texture.

Temperature differential between chocolate surface temperature (entering at 28-31°C) and cooling air must follow controlled profiles to achieve proper crystallization kinetics. The latent heat of crystallization releases approximately 50 kJ/kg during cocoa butter solidification, requiring heat removal capacity in addition to sensible cooling load.

## Cooling Tunnel Zone Design

Multi-zone cooling tunnels provide staged temperature reduction matching chocolate crystallization requirements. Typical industrial installations incorporate 3 to 6 distinct cooling zones with independent temperature and airflow control.

**Zone 1 - Pre-cooling:**
Temperature: 16-18°C
Purpose: Initial temperature reduction without surface solidification
Duration: 1-2 minutes
Air velocity: 0.5-1.0 m/s

This zone initiates controlled heat removal while maintaining chocolate surface fluidity. Gentle air movement prevents surface disturbance before initial crystallization begins. The temperature remains above chocolate solidification point (approximately 15°C for milk chocolate, 17°C for dark chocolate) to prevent premature skin formation.

**Zone 2 - Primary Cooling:**
Temperature: 12-14°C
Purpose: Surface crystallization initiation
Duration: 2-3 minutes
Air velocity: 1.0-1.5 m/s

Primary cooling establishes Form V beta crystal nucleation sites across the chocolate surface. Temperature control precision within ±0.5°C maintains uniform crystallization throughout the product stream. Increased air velocity accelerates heat transfer while remaining below levels causing surface disruption.

**Zone 3 - Secondary Cooling:**
Temperature: 8-12°C
Purpose: Complete shell solidification
Duration: 3-5 minutes
Air velocity: 1.5-2.5 m/s

Secondary cooling completes chocolate solidification through the entire coating thickness. Temperature gradients between surface and core drive crystallization progression inward. Air velocity increases as surface strength develops, enhancing heat transfer without appearance defects.

**Zone 4 - Final Cooling:**
Temperature: 10-14°C
Purpose: Core temperature equilibration
Duration: 2-4 minutes
Air velocity: 1.0-2.0 m/s

Final cooling equilibrates temperature throughout the product cross-section and prepares for ambient conditions. Controlled temperature increase from Zone 3 prevents condensation formation when products exit the tunnel.

| Zone | Temperature (°C) | Air Velocity (m/s) | Relative Humidity (%) | Duration (min) | Purpose |
|------|------------------|--------------------|-----------------------|----------------|---------|
| Pre-cooling | 16-18 | 0.5-1.0 | 45-50 | 1-2 | Initial heat removal |
| Primary | 12-14 | 1.0-1.5 | 40-45 | 2-3 | Surface crystallization |
| Secondary | 8-12 | 1.5-2.5 | 35-40 | 3-5 | Shell solidification |
| Final | 10-14 | 1.0-2.0 | 40-45 | 2-4 | Temperature equilibration |

## Air Temperature and Velocity Profiles

Cooling air temperature and velocity profiles directly influence chocolate crystallization kinetics and surface quality. Air distribution systems deliver uniform conditions across the tunnel cross-section while accommodating varying product heights and belt loading densities.

**Temperature Profile Requirements:**

Longitudinal temperature variation within each zone must not exceed ±0.5°C to maintain uniform product quality. Temperature stratification across the tunnel height should remain below ±0.3°C at product level. Supply air temperature typically operates 2-4°C below target zone temperature to provide heat transfer driving force while preventing excessive local cooling.

Temperature sensors positioned every 1-2 meters along the tunnel length provide feedback for modulating refrigeration capacity and mixing damper positions. Product surface temperature monitoring via infrared sensors enables real-time process adjustment based on actual chocolate temperature rather than air temperature alone.

**Velocity Profile Design:**

Air velocity profiles balance heat transfer enhancement against surface disruption risk. Excessive velocity causes:
- Surface rippling on liquid chocolate
- Coating thickness variations
- Matte appearance from microscale turbulence
- Fat bloom from rapid surface cooling

Insufficient velocity results in:
- Extended cooling time requirements
- Non-uniform temperature distribution
- Increased tunnel length and cost
- Soft product texture

Optimal velocity ranges depend on product geometry, coating thickness, and chocolate formulation. Flat products tolerate higher velocities (up to 3 m/s) while complex shapes require gentle airflow (0.5-1.5 m/s) to prevent coating disruption in crevices and corners.

Air distribution typically employs overhead plenums with perforated plates or nozzle arrays directing flow downward across the product surface. Return air collection occurs beneath the conveyor belt, creating a vertical airflow pattern. Some designs incorporate horizontal cross-flow for products requiring gentle treatment.

| Product Type | Coating Thickness (mm) | Recommended Velocity (m/s) | Cooling Time (min) |
|--------------|------------------------|----------------------------|---------------------|
| Flat bars | 2-4 | 2.0-3.0 | 6-8 |
| Caramels | 1-2 | 1.5-2.5 | 5-7 |
| Nuts/clusters | 2-5 | 1.0-2.0 | 8-12 |
| Wafers | 1-3 | 1.5-2.5 | 6-9 |
| Filled centers | 2-4 | 1.0-2.0 | 8-10 |

## Humidity Control for Bloom Prevention

Relative humidity control prevents sugar bloom formation caused by moisture condensation dissolving surface sugar crystals. When products exit the cooling tunnel, temperature differential between cold chocolate surface (10-14°C) and ambient air (20-25°C) creates condensation risk if humidity exceeds dew point limits.

**Sugar Bloom Mechanism:**

Moisture condenses on cold chocolate surfaces when surface temperature falls below ambient dew point. Condensed water dissolves sugar from the chocolate matrix, creating a saturated surface solution. As water evaporates, dissolved sugar recrystallizes in large, visible crystals appearing as gray-white surface discoloration.

Prevention requires maintaining tunnel humidity below levels causing condensation at the chocolate surface temperature and ambient humidity combination. The critical relationship follows:

Tunnel RH < 100% × (Psat at Ts)/(Psat at Ta)

Where:
- Ts = chocolate surface temperature at tunnel exit (°C)
- Ta = ambient air temperature (°C)
- Psat = saturation vapor pressure at specified temperature

**Humidity Control Methods:**

1. **Refrigeration Dehumidification:**
   - Cooling coils condense moisture from recirculated tunnel air
   - Typical performance: 50-60% RH at 10-14°C
   - Condensate removal requirement: 0.5-2.0 L/h per meter tunnel length
   - Reheat may be required to maintain temperature setpoint

2. **Desiccant Dehumidification:**
   - Chemical or physical adsorption removes moisture
   - Achieves 30-40% RH at cooling temperatures
   - Higher initial cost, lower operating cost in humid climates
   - Regeneration energy requirement: 2500-3500 kJ/kg water removed

3. **Controlled Exit Conditions:**
   - Final zone temperature elevation reduces condensation risk
   - Gradual transition from 10°C to 14-16°C before exit
   - Buffer zone maintains low humidity while warming product
   - Product surface temperature reaches safe level (>15°C) before ambient exposure

Target humidity levels throughout cooling zones:

| Zone | Target RH (%) | Maximum RH (%) | Dew Point (°C) |
|------|---------------|----------------|----------------|
| Pre-cooling (16-18°C) | 45-50 | 55 | 6-9 |
| Primary (12-14°C) | 40-45 | 50 | 1-5 |
| Secondary (8-12°C) | 35-40 | 45 | -3 to 2 |
| Final (10-14°C) | 40-45 | 50 | 0-5 |

## Radiant Cooling Sections

Radiant cooling panels supplement convective cooling in applications requiring minimal air velocity to protect delicate surface decorations or prevent coating disruption. Cooled surface panels positioned above and below the product stream provide heat transfer through thermal radiation and natural convection.

**Radiant Panel Design:**

Cooling panels consist of aluminum or stainless steel sheets with integral refrigerant passages maintaining surface temperatures of 2-8°C. Panel emissivity affects radiant heat transfer effectiveness - polished aluminum (ε = 0.05) provides minimal radiation while anodized or painted surfaces (ε = 0.8-0.9) enhance radiant contribution.

Heat transfer from chocolate surface to cooling panels combines:
- Radiant exchange: q = σ × ε × A × (Ts⁴ - Tp⁴)
- Natural convection: q = h × A × (Ts - Ta)

Where:
- σ = Stefan-Boltzmann constant (5.67 × 10⁻⁸ W/m²·K⁴)
- ε = effective emissivity between surfaces
- A = panel surface area (m²)
- Ts = chocolate surface temperature (K)
- Tp = panel surface temperature (K)
- Ta = air temperature (K)
- h = natural convection coefficient (3-8 W/m²·K)

**Application Considerations:**

Radiant cooling provides heat removal rates of 50-150 W/m² panel area depending on temperature differentials and surface properties. This represents approximately 20-40% of forced convection heat transfer capacity, requiring longer tunnel lengths for equivalent production rates.

Benefits include:
- Minimal surface disruption for decorated products
- Reduced air movement prevents dust accumulation
- Lower air velocity noise levels
- Suitable for delicate toppings and garnishes

Limitations include:
- Extended cooling time requirements
- Higher capital cost per unit capacity
- Condensation risk on cold panels requires careful humidity control
- Panel cleaning access for hygiene compliance

## Belt Speed and Cooling Time

Conveyor belt speed determines product residence time in each cooling zone and total tunnel throughput capacity. Belt speed selection balances production rate requirements against cooling time needed for complete chocolate crystallization and solidification.

**Cooling Time Calculation:**

Required cooling time depends on coating thickness, chocolate thermal properties, and target exit temperature:

t = (ρ × c × δ × ΔT) / (h × ΔTm)

Where:
- t = cooling time (s)
- ρ = chocolate density (1100-1300 kg/m³)
- c = specific heat (1800-2200 J/kg·K)
- δ = coating thickness (m)
- ΔT = temperature change (K)
- h = heat transfer coefficient (20-50 W/m²·K for forced convection)
- ΔTm = log mean temperature difference (K)

Additional time required for latent heat removal during crystallization:

tL = (ρ × δ × Lf) / (h × ΔTm)

Where Lf = latent heat of cocoa butter crystallization (50,000 J/kg)

**Belt Speed Optimization:**

Tunnel length (L) and belt speed (v) relationship:

v = L / (t + tL)

For a 20-meter tunnel with 10-minute total cooling requirement:
v = 20 m / (10 × 60 s) = 0.033 m/s = 2.0 m/min

Production capacity calculation:

Capacity = v × W × ρs

Where:
- W = belt width (m)
- ρs = product surface density (kg/m²)

| Belt Speed (m/min) | Cooling Time (min) | Tunnel Length (m) | Typical Application |
|--------------------|--------------------|--------------------|---------------------|
| 2-3 | 12-15 | 25-35 | Thick coatings, complex shapes |
| 3-5 | 8-12 | 25-35 | Standard enrobing, medium thickness |
| 5-8 | 6-8 | 25-35 | Thin coatings, simple shapes |
| 8-12 | 4-6 | 25-35 | Very thin coatings, flat products |

## Cooling Tunnel Specifications

Industrial chocolate enrobing cooling tunnels integrate refrigeration systems, air handling, humidity control, and process monitoring to achieve consistent product quality at production scale.

**Refrigeration System Design:**

Cooling capacity requirements combine sensible heat removal, crystallization latent heat, and infiltration loads:

Qsensible = ṁ × c × ΔT
Qlatent = ṁ × Lf × fraction crystallized
Qinfiltration = ρa × Va × ca × ΔTa

Total refrigeration capacity typically ranges from 15 to 50 kW per meter of tunnel length depending on production rate and product characteristics.

Refrigerant selection considerations:
- R-404A: Traditional choice, GWP = 3922, operating temperatures -10 to -30°C
- R-449A: Lower GWP alternative (1397), direct R-404A replacement
- R-744 (CO₂): Low GWP (1), requires cascade system or transcritical operation
- Ammonia (R-717): Industrial applications, secondary coolant distribution to tunnel

**Air Handling System:**

Recirculation ratio typically ranges from 80-95% to minimize refrigeration load while maintaining air quality. Fresh air introduction provides:
- Humidity dilution (5-20% of total airflow)
- Contaminant removal (cocoa dust, volatile compounds)
- Pressurization to prevent ambient air infiltration

Fan power requirements: 0.5-1.5 kW per meter tunnel length
Supply air volume: 2000-5000 m³/h per meter tunnel length
Static pressure: 200-500 Pa across distribution system

**Control System Integration:**

Modern tunnel controls employ PLC-based systems with touchscreen HMI interfaces monitoring and controlling:
- Zone temperatures (±0.2°C precision)
- Air velocities via VFD fan speed control
- Relative humidity with dewpoint protection
- Belt speed and production tracking
- Refrigeration system staging
- Energy consumption monitoring
- Predictive maintenance alerts

| Tunnel Specification | Small Scale | Medium Scale | Large Scale |
|----------------------|-------------|--------------|-------------|
| Length | 10-15 m | 20-30 m | 35-50 m |
| Width | 400-600 mm | 600-1000 mm | 1000-1400 mm |
| Production rate | 50-150 kg/h | 200-500 kg/h | 600-1500 kg/h |
| Refrigeration capacity | 15-25 kW | 30-60 kW | 75-150 kW |
| Connected power | 20-30 kW | 40-75 kW | 100-200 kW |
| Air volume | 8,000-15,000 m³/h | 20,000-40,000 m³/h | 50,000-80,000 m³/h |
| Control zones | 2-3 | 3-4 | 4-6 |

## Energy Efficiency Considerations

Energy consumption in enrobing cooling tunnels represents significant operating cost. Optimization strategies include:

**Heat Recovery:**
Refrigeration system heat rejection (condenser heat) can warm facility spaces during cold weather or provide hot water for sanitation. Heat recovery effectiveness reaches 60-75% of refrigeration capacity with appropriate heat exchanger sizing.

**Variable Speed Control:**
VFD-controlled fans and compressors reduce energy consumption during partial load conditions. Energy savings of 20-35% are achievable compared to constant speed operation when production rates vary throughout shifts.

**Insulation Performance:**
Tunnel wall and ceiling insulation (100-150 mm polyurethane foam, R-value 6.5-9.0 m²·K/W) minimizes heat infiltration. Proper door seals and air curtains at entrance/exit reduce infiltration losses representing 15-25% of total cooling load.

**Night Mode Operation:**
Reduced setpoint temperatures during non-production periods minimize compressor cycling and maintain stable conditions for rapid production startup. Setback to 5-8°C reduces overnight energy consumption by 40-60% compared to maintaining full operating temperatures.
