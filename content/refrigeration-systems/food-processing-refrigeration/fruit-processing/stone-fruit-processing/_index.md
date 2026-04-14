---
title: "Stone Fruit Processing"
aliases: ["Stone Fruit Processing"]
weight: 5
---

Stone fruit processing refrigeration systems manage thermal conditions for peaches, plums, apricots, cherries, and nectarines throughout harvest, processing, storage, and distribution. These fruits exhibit high respiration rates, ethylene production, and susceptibility to chilling injury, requiring precise temperature and humidity control to maintain quality while preventing physiological disorders.

## Stone Fruit Characteristics

Stone fruits demonstrate distinct refrigeration requirements based on species-specific physiology:

| Fruit Type | Respiration Rate at 20°C (mg CO₂/kg·h) | Ethylene Production | Chilling Sensitivity | Optimal Storage Duration |
|------------|----------------------------------------|---------------------|---------------------|--------------------------|
| Peaches | 40-80 | High (100-200 μL/kg·h) | High | 2-4 weeks |
| Nectarines | 50-90 | High (150-250 μL/kg·h) | Very High | 2-4 weeks |
| Plums | 20-40 | Moderate (10-30 μL/kg·h) | Moderate | 2-5 weeks |
| Apricots | 30-60 | Moderate (20-40 μL/kg·h) | High | 1-3 weeks |
| Sweet Cherries | 25-50 | Low (5-15 μL/kg·h) | Low | 2-3 weeks |
| Sour Cherries | 30-60 | Low (3-10 μL/kg·h) | Low | 1-2 weeks |

Heat of respiration varies significantly with temperature, following Q₁₀ values of 2.5-4.0 for stone fruits, necessitating rapid cooling to reduce metabolic heat generation.

## Field Heat Removal

Stone fruits arrive at processing facilities with substantial field heat that must be removed quickly to minimize quality deterioration:

**Field Heat Load Calculation:**

Q_field = m × c_p × (T_harvest - T_target)

Where:
- Q_field = field heat load (kJ)
- m = fruit mass (kg)
- c_p = specific heat (3.6-3.9 kJ/kg·K for stone fruits)
- T_harvest = harvest temperature (typically 25-35°C)
- T_target = target storage temperature (°C)

**Total Cooling Load:**

Q_total = Q_field + Q_respiration + Q_container + Q_infiltration

For a 1000 kg/h stone fruit processing line operating with fruit at 30°C cooled to 2°C:

Q_field = 1000 kg/h × 3.7 kJ/kg·K × (30 - 2)K = 103,600 kJ/h = 28.8 kW

## Precooling Systems

### Forced-Air Cooling

Forced-air cooling provides rapid heat removal for stone fruits in shipping containers:

**Design Parameters:**

| Parameter | Value | Basis |
|-----------|-------|-------|
| Air velocity through fruit | 1.5-2.5 m/s | Heat transfer optimization |
| Air temperature | -1 to 0°C | Maximum temperature differential |
| Relative humidity | 90-95% | Moisture loss prevention |
| Cooling time (7/8 cooling) | 2-4 hours | Product-dependent |
| Air exchange rate | 60-100 ACH | Heat removal requirement |

**Heat Transfer Coefficient:**

For forced-air cooling through packed stone fruits:

h = 5.7 + 3.8v^0.8

Where:
- h = convective heat transfer coefficient (W/m²·K)
- v = air velocity (m/s)

This relationship yields h values of 15-25 W/m²·K for typical stone fruit precooling operations.

**Cooling Rate:**

The cooling rate follows Newton's law of cooling:

(T - T_a)/(T_i - T_a) = exp(-hA·t/mc_p)

Where:
- T = fruit temperature at time t (°C)
- T_a = air temperature (°C)
- T_i = initial fruit temperature (°C)
- A = surface area (m²)
- t = time (s)

### Hydrocooling

Hydrocooling achieves faster heat removal than air cooling due to water's superior thermal properties:

**Performance Characteristics:**

| Parameter | Value | Notes |
|-----------|-------|-------|
| Water temperature | 0-2°C | Approaching freezing point |
| Water velocity | 0.3-0.6 m/s | Adequate convection |
| Chlorine concentration | 50-150 ppm | Sanitation requirement |
| Contact time | 3-10 minutes | Species-dependent |
| Heat transfer coefficient | 200-500 W/m²·K | 10-20× air cooling |
| Cooling time (7/8 cooling) | 10-30 minutes | Rapid response |

**Water Requirements:**

Q_water = Q_fruit / (ρ_water × c_p,water × ΔT_water)

For continuous operation, water flow rates of 15-25 L/min per ton of fruit capacity maintain effective heat transfer while limiting temperature rise to 2-3°C.

### Room Cooling

Conventional room cooling provides gradual temperature reduction for less perishable stone fruits:

- Air velocity: 0.1-0.3 m/s (gentle circulation)
- Room temperature: 0-2°C (depending on species)
- Cooling time: 12-24 hours (slower but gentler)
- Relative humidity: 90-95%

Room cooling minimizes mechanical damage but extends the period of elevated respiration and quality loss.

## Storage Conditions

### Optimal Storage Parameters

Stone fruit storage requirements vary by species and cultivar:

| Fruit | Temperature (°C) | RH (%) | Storage Life | Freezing Point (°C) |
|-------|-----------------|--------|--------------|---------------------|
| Peaches (melting flesh) | -0.5 to 0 | 90-95 | 2-4 weeks | -0.9 to -1.1 |
| Peaches (non-melting) | 0 to 5 | 90-95 | 3-5 weeks | -0.9 to -1.1 |
| Nectarines | -0.5 to 0 | 90-95 | 2-4 weeks | -0.9 to -1.2 |
| Plums (Japanese) | -0.5 to 0 | 90-95 | 3-5 weeks | -0.8 to -1.5 |
| Plums (European) | -0.5 to 0 | 90-95 | 2-8 weeks | -0.8 to -1.5 |
| Apricots | -0.5 to 0 | 90-95 | 1-3 weeks | -1.0 to -1.4 |
| Sweet Cherries | -1 to 0 | 90-95 | 2-3 weeks | -1.8 to -2.2 |
| Sour Cherries | -1 to 0 | 90-95 | 1-2 weeks | -2.0 to -2.5 |

### Chilling Injury

Many stone fruit cultivars exhibit chilling injury when stored below critical temperatures:

**Chilling Injury Thresholds:**

| Fruit Type | Critical Temperature (°C) | Symptoms | Development Time |
|------------|---------------------------|----------|------------------|
| Peaches | Below 2°C | Mealiness, browning, red pigment loss | 1-4 weeks |
| Nectarines | Below 2°C | Flesh browning, failure to ripen | 1-3 weeks |
| Plums | Below -1°C | Gel breakdown, off-flavor | 2-4 weeks |
| Apricots | Below -0.5°C | Flesh browning, loss of flavor | 1-2 weeks |

**Temperature Conditioning:**

Intermittent warming reduces chilling injury in susceptible cultivars:

- Storage at 0°C for 5-7 days
- Warming to 20°C for 1-2 days
- Return to 0°C storage
- Cycle repeated every 7-10 days

This approach extends storage life by 30-50% for chilling-sensitive peach and nectarine cultivars while increasing energy consumption by 15-25%.

## Controlled Atmosphere Storage

CA storage extends stone fruit storage life by modifying atmospheric composition:

### CA Parameters

| Fruit | O₂ (%) | CO₂ (%) | Temperature (°C) | Life Extension |
|-------|--------|---------|------------------|----------------|
| Peaches | 1-2 | 3-5 | 0 | 1-2 weeks |
| Nectarines | 1-2 | 3-5 | 0 | 1-2 weeks |
| Sweet Cherries | 3-10 | 10-15 | -1 to 0 | 2-3 weeks |
| Plums | 1-2 | 0-5 | -0.5 to 0 | 2-4 weeks |

**CA Equipment Requirements:**

- O₂ scrubbers: Nitrogen generators or membrane systems
- CO₂ scrubbers: Activated carbon or hydrated lime systems
- Gas monitoring: ±0.1% accuracy for O₂ and CO₂
- Room sealing: <2% gas exchange per day

## Freezing Operations

### Blast Freezing

Individual Quick Freezing (IQF) maintains fruit quality for long-term storage:

**Freezing Parameters:**

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Air temperature | -35 to -40°C | Rapid freezing rate |
| Air velocity | 3-6 m/s | Maximum heat transfer |
| Freezing time | 15-45 minutes | Product size-dependent |
| Final center temperature | -18°C minimum | Microbial stability |
| Belt speed | 0.1-0.3 m/min | Residence time control |

**Freezing Time Calculation:**

Plank's equation for freezing time of stone fruits (approximated as spheres):

t_f = (ρL/ΔT) × (PR/h + R²/4k)

Where:
- t_f = freezing time (s)
- ρ = density (950-1050 kg/m³)
- L = latent heat of fusion (280-310 kJ/kg for stone fruits)
- ΔT = T_freezing - T_air (K)
- P = shape factor (1/6 for spheres)
- R = fruit radius (m)
- h = surface heat transfer coefficient (40-80 W/m²·K for blast freezing)
- k = thermal conductivity of frozen fruit (1.8-2.2 W/m·K)

For a 40 mm diameter cherry at -35°C:

t_f ≈ (1000 kg/m³ × 290,000 J/kg / 33 K) × (0.167 × 0.02 m / 60 W/m²·K + (0.02 m)² / (4 × 2.0 W/m·K))

t_f ≈ 8,788 × (5.57 × 10⁻⁵ + 1.0 × 10⁻⁴) = 1,370 seconds ≈ 23 minutes

### Refrigeration System Design

IQF systems for stone fruits require substantial refrigeration capacity:

**Capacity Calculation:**

Q_total = Q_product + Q_air + Q_fan + Q_defrost + Q_infiltration

For 2000 kg/h cherry processing:

- Q_product (sensible + latent): 2000 kg/h × [(3.8 kJ/kg·K × 22 K) + 290 kJ/kg] = 747,200 kJ/h = 208 kW
- Q_air (cooling supply air): 15-20 kW
- Q_fan (mechanical energy): 10-15 kW
- Q_defrost (periodic): 8-12 kW average
- Q_infiltration (door openings): 5-8 kW

Total refrigeration requirement: 250-265 kW (71-75 tons)

### Frozen Storage

Post-freezing storage maintains product quality:

| Parameter | Requirement | Quality Impact |
|-----------|-------------|----------------|
| Storage temperature | -18 to -23°C | Enzyme activity control |
| Temperature stability | ±1°C | Ice crystal growth prevention |
| Relative humidity | 85-90% | Sublimation control |
| Air velocity | <0.5 m/s | Minimize desiccation |
| Storage duration | 12-24 months | Product-dependent |

**Quality Degradation:**

Frozen stone fruit quality follows first-order degradation kinetics:

C/C₀ = exp(-kt)

Where k increases exponentially with temperature according to Arrhenius relationship. Each 5°C temperature increase doubles the degradation rate for most quality factors.

## Processing Line Integration

Refrigeration systems integrate with processing operations:

1. **Receiving and Sorting:** Room cooling at 2-5°C, 60-80% RH
2. **Washing and Grading:** Chilled water systems at 0-2°C
3. **Cutting and Pitting:** Temperature maintenance at 2-5°C to minimize enzymatic browning
4. **Packaging:** Controlled environment at 0-5°C
5. **Cold Storage:** Species-specific optimal conditions
6. **Freezing:** IQF tunnel or plate freezers at -35 to -40°C
7. **Frozen Storage:** -18 to -23°C distribution-ready inventory

Each process stage requires dedicated refrigeration capacity sized for the specific thermal load and residence time.

## Quality Monitoring

Critical control points for stone fruit refrigeration:

- Temperature monitoring: ±0.5°C accuracy, continuous recording
- Humidity control: ±3% RH accuracy
- Air velocity verification: Quarterly anemometer surveys
- Product temperature: Core temperature checks every 2 hours
- Gas composition (CA): Continuous O₂ and CO₂ monitoring
- Defrost cycles: Automated scheduling based on coil pressure drop

Advanced facilities employ wireless sensor networks with 5-10 minute data logging intervals and automated alarm systems for excursions beyond control limits.

