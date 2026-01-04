---
title: "Ventilation Indoor Air Quality"
weight: 17
---

Ventilation systems maintain acceptable indoor air quality through controlled outdoor air introduction, contaminant dilution, and air distribution. Building occupants generate carbon dioxide, moisture, and bioeffluents while building materials, furnishings, and activities release volatile organic compounds, particulates, and other contaminants. Effective ventilation dilutes these pollutants to concentrations that protect occupant health, comfort, and productivity while managing energy consumption.

## Outdoor Air Requirements and Ventilation Rate Determination

ASHRAE Standard 62.1 establishes minimum ventilation rates based on occupancy and floor area using the ventilation rate procedure:

$$V_{bz} = R_p \times P_z + R_a \times A_z$$

Where:
- $V_{bz}$ = breathing zone outdoor airflow rate (CFM)
- $R_p$ = outdoor air rate per person (CFM/person)
- $P_z$ = zone population (people)
- $R_a$ = outdoor air rate per unit area (CFM/ft²)
- $A_z$ = zone floor area (ft²)

Typical occupancy requirements range from 5 CFM/person for storage areas to 20 CFM/person for conference rooms. The area component addresses emissions from building materials and furnishings, typically 0.06 to 0.18 CFM/ft² depending on space type.

### Ventilation Effectiveness and Distribution

Air distribution patterns affect contaminant removal efficiency. Ventilation effectiveness relates supply air to exhaust air contaminant concentration:

$$\varepsilon = \frac{C_e - C_s}{C_b - C_s}$$

Where:
- $\varepsilon$ = ventilation effectiveness (dimensionless)
- $C_e$ = exhaust air contaminant concentration
- $C_s$ = supply air contaminant concentration
- $C_b$ = breathing zone contaminant concentration

Well-mixed conditions produce effectiveness near 1.0, while displacement ventilation achieves values of 1.2 to 1.5 by delivering air at floor level and extracting warm, contaminated air at ceiling height. Poor distribution with short-circuiting reduces effectiveness below 0.8, requiring increased ventilation rates.

## Contaminant Dilution and Mass Balance Analysis

Steady-state contaminant concentration in a space follows mass balance principles:

$$G = Q \times (C_i - C_o)$$

Solving for indoor concentration:

$$C_i = C_o + \frac{G}{Q}$$

Where:
- $G$ = contaminant generation rate (mass/time)
- $Q$ = ventilation rate (volume/time)
- $C_i$ = indoor concentration
- $C_o$ = outdoor concentration

For transient conditions, the time-dependent concentration equation applies:

$$C_i(t) = C_{ss} + (C_0 - C_{ss}) \times e^{-\frac{Q}{V} \times t}$$

Where $C_{ss}$ is steady-state concentration, $C_0$ is initial concentration, and $V$ is space volume. The air change rate $Q/V$ determines how rapidly indoor conditions approach steady state.

### Carbon Dioxide as a Ventilation Indicator

Occupants generate CO₂ at rates depending on metabolic activity. Office work produces approximately 0.3 CFH (cubic feet per hour) per person, while moderate exercise generates 0.6 CFH per person. Indoor CO₂ concentration indicates ventilation adequacy:

$$CO_{2,indoor} = CO_{2,outdoor} + \frac{N \times G_{CO_2}}{Q}$$

Where $N$ is occupancy and $G_{CO_2}$ is per-person generation rate. Outdoor CO₂ typically measures 400-450 ppm. ASHRAE Standard 62.1 uses 700 ppm above outdoor levels (approximately 1100-1150 ppm absolute) as a design target, though CO₂ alone does not indicate acceptability for all contaminants.

## Indoor Air Quality Parameters and Limits

Multiple parameters characterize indoor air quality:

| Parameter | Acceptable Range | Measurement | Health Impact |
|-----------|------------------|-------------|---------------|
| CO₂ | < 1000 ppm | NDIR sensor | Cognitive performance indicator |
| PM2.5 | < 12 μg/m³ annual | Optical counter | Respiratory, cardiovascular |
| PM10 | < 50 μg/m³ 24-hr | Optical counter | Respiratory irritation |
| TVOC | < 500 μg/m³ | PID sensor | Varies by compound |
| Formaldehyde | < 27 ppb | Electrochemical | Respiratory irritant, carcinogen |
| Relative Humidity | 30-60% | Capacitive sensor | Mold growth, comfort |
| Radon | < 4 pCi/L | Alpha detector | Lung cancer risk |

Particulate matter poses significant health risks. PM2.5 (particles under 2.5 micrometers) penetrates deep into lungs and enters the bloodstream. Sources include outdoor infiltration, combustion, cooking, and cleaning activities.

## Ventilation System Strategies

Different ventilation approaches offer distinct advantages:

| Strategy | Application | Energy Impact | Control Complexity | Effectiveness |
|----------|-------------|---------------|-------------------|---------------|
| Constant volume | Small buildings, stable occupancy | Moderate | Low | Adequate |
| Variable air volume | Large commercial, variable loads | Lower | Moderate | Good with proper control |
| Demand controlled | High-occupancy spaces | Lowest | High | Excellent with sensors |
| Natural ventilation | Mild climates, low buildings | Minimal | Weather dependent | Variable |
| Mixed-mode | Temperate climates | Low | High | Good seasonal performance |
| Displacement | High ceilings, heat sources | Moderate | Moderate | Superior (ε > 1.2) |

### Demand Controlled Ventilation

Demand controlled ventilation (DCV) modulates outdoor air based on actual occupancy using CO₂ or occupancy sensors. Energy savings reach 20-40% in spaces with variable occupancy like auditoriums, conference rooms, and gymnasiums.

DCV control logic maintains CO₂ setpoint through proportional outdoor air damper modulation:

$$V_{ot} = V_{min} + K \times (CO_{2,measured} - CO_{2,setpoint})$$

Where $V_{ot}$ is outdoor air flow, $V_{min}$ is minimum ventilation, and $K$ is control gain. Proper sensor placement at breathing zone height and adequate control response prevent setpoint overshoot.

## Contaminant Sources and Control Strategies

Indoor contaminants originate from multiple sources requiring layered control approaches:

**Occupant-Generated Contaminants:**
- CO₂, water vapor, bioeffluents: controlled through dilution ventilation
- Body odors, perfumes: 15-20 CFM/person minimum ventilation
- Airborne pathogens: MERV 13+ filtration plus UV germicidal irradiation

**Building-Related Sources:**
- VOCs from materials: source control through low-emission specifications
- Formaldehyde from composite wood: air cleaning or increased ventilation
- Radon from soil: sub-slab depressurization systems
- Moisture and mold: humidity control below 60% RH

**Activity-Related Pollutants:**
- Cooking emissions: local exhaust 100+ CFM per linear foot of cooking surface
- Cleaning products: scheduling during unoccupied hours plus purge ventilation
- Office equipment: isolated with dedicated exhaust in copy rooms

### Air Cleaning Technologies Comparison

| Technology | Particle Removal | Gas Removal | Ozone Generation | Energy Use | Maintenance |
|------------|------------------|-------------|------------------|------------|-------------|
| Mechanical filtration (MERV 13-16) | Excellent (> 85% PM2.5) | None | No | Moderate | 3-6 months |
| HEPA filtration | Superior (> 99.97% ≥ 0.3 μm) | None | No | High | 6-12 months |
| Activated carbon | None | Good for VOCs | No | Low | 3-12 months |
| Electronic air cleaners | Good (varies) | None | Possible | Low | Monthly cleaning |
| UV germicidal | Microorganisms only | None | Possible | Low | Annual lamp |
| Photocatalytic oxidation | Limited | Limited | Yes | Low | Variable |

Mechanical filtration provides the most reliable and maintenance-friendly approach for particulate control. Higher MERV ratings increase particle removal but also increase pressure drop, requiring fan energy evaluation.

## Energy Recovery Ventilation

Energy recovery systems transfer heat and sometimes moisture between exhaust and outdoor airstreams, reducing conditioning loads:

**Sensible effectiveness:**

$$\varepsilon_s = \frac{T_{supply} - T_{outdoor}}{T_{exhaust} - T_{outdoor}}$$

**Latent effectiveness:**

$$\varepsilon_L = \frac{W_{supply} - W_{outdoor}}{W_{exhaust} - W_{outdoor}}$$

Where $T$ represents temperature and $W$ represents humidity ratio. Sensible effectiveness ranges from 60-85% for quality units. Total energy recovery wheels achieve 70-80% total effectiveness by transferring both heat and moisture.

Energy recovery payback depends on climate, operating hours, and utility costs. Cold climates with significant heating loads and hot-humid climates with large cooling loads benefit most. Applications with 3000+ operating hours annually and outdoor air fractions above 30% achieve typical paybacks of 3-7 years.

## Air Changes Per Hour and Ventilation Rates

Air changes per hour (ACH) relates volumetric airflow to space volume:

$$ACH = \frac{Q \times 60}{V}$$

Where $Q$ is airflow in CFM and $V$ is volume in cubic feet. Typical values:
- Residences: 0.35 ACH minimum (ASHRAE 62.2)
- Offices: 4-6 ACH
- Classrooms: 6-8 ACH
- Healthcare patient rooms: 6 ACH minimum, 12+ for isolation
- Laboratories: 6-12 ACH depending on hazards

Higher air change rates provide faster contaminant dilution but increase energy consumption. Ventilation effectiveness allows achieving acceptable IAQ with lower air change rates through improved distribution.

