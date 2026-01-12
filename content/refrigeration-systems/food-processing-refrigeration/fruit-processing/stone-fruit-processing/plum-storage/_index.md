---
title: "Plum Storage"
description: "Refrigeration system design and environmental control for plum storage including temperature stratification, chilling injury prevention, internal breakdown mitigation, and humidity management for Japanese and European plum varieties."
weight: 2
---

Plum storage requires precise environmental control to prevent physiological disorders while maintaining fruit quality throughout the storage period. The refrigeration system must accommodate variety-specific temperature requirements, maintain high relative humidity, and provide uniform air distribution to prevent both chilling injury and desiccation.

## Storage Temperature Requirements by Variety

Temperature management represents the critical control parameter for plum storage. Variety-specific requirements determine refrigeration system setpoints and control strategies.

### Japanese Plums (Prunus salicina)

Japanese plums require the lowest storage temperatures among plum varieties but exhibit variable chilling injury susceptibility.

| Variety | Temperature (°C) | Temperature (°F) | Max Storage Duration | CI Susceptibility |
|---------|------------------|------------------|----------------------|-------------------|
| Santa Rosa | -0.5 to 0 | 31 to 32 | 3-4 weeks | High |
| Black Amber | 0 to 0.5 | 32 to 33 | 4-5 weeks | Moderate |
| Friar | -0.5 to 0 | 31 to 32 | 5-6 weeks | Low |
| Angeleno | -0.5 to 0 | 31 to 32 | 8-12 weeks | Very Low |
| Red Beaut | 0 to 0.5 | 32 to 33 | 3-4 weeks | High |
| Casselman | -0.5 to 0 | 31 to 32 | 4-5 weeks | Moderate |
| Larry Ann | 0 to 1 | 32 to 34 | 2-3 weeks | Very High |

**Control Strategy**: Maintain setpoint at variety-specific optimum with ±0.3°C (±0.5°F) tolerance. Install RTD sensors with 0.1°C resolution for precise control.

### European Plums (Prunus domestica)

European plums tolerate slightly higher storage temperatures and generally exhibit lower chilling injury susceptibility.

| Variety | Temperature (°C) | Temperature (°F) | Max Storage Duration | CI Susceptibility |
|---------|------------------|------------------|----------------------|-------------------|
| Italian Prune | 0 to 2 | 32 to 36 | 4-6 weeks | Low |
| Stanley | 0 to 2 | 32 to 36 | 4-6 weeks | Low |
| President | -0.5 to 1 | 31 to 34 | 5-7 weeks | Very Low |
| Empress | 0 to 2 | 32 to 36 | 3-5 weeks | Moderate |
| Valor | 0 to 2 | 32 to 36 | 4-6 weeks | Low |

**Control Strategy**: European plums permit wider temperature tolerance (±0.5°C) compared to Japanese varieties, reducing refrigeration system cycling frequency.

## Humidity Control Requirements

Plums require high relative humidity to prevent moisture loss while avoiding surface condensation that promotes fungal growth.

### Target Humidity Parameters

**Optimal Range**: 90-95% RH
**Absolute Minimum**: 88% RH
**Vapor Pressure Deficit**: 0.06-0.15 kPa

### Psychrometric Relationships

The saturation vapor pressure at typical plum storage temperatures:

For temperature T in °C:
$$e_s = 0.6108 \exp\left(\frac{17.27T}{T + 237.3}\right) \text{ kPa}$$

At 0°C storage temperature:
$$e_s(0°C) = 0.6108 \text{ kPa}$$

For 90% RH: $e_a = 0.90 \times 0.6108 = 0.550$ kPa
For 95% RH: $e_a = 0.95 \times 0.6108 = 0.580$ kPa

Vapor pressure deficit (VPD):
$$VPD = e_s - e_a$$

At 90% RH: $VPD = 0.6108 - 0.550 = 0.061$ kPa
At 95% RH: $VPD = 0.6108 - 0.580 = 0.031$ kPa

### Moisture Loss Rate

Weight loss rate depends on vapor pressure deficit and fruit surface characteristics:

$$\frac{dm}{dt} = k \cdot A \cdot VPD$$

Where:
- dm/dt = moisture loss rate (kg/h)
- k = mass transfer coefficient (0.8-1.2 × 10⁻⁶ kg/(m²·h·kPa) for plums)
- A = total fruit surface area (m²)
- VPD = vapor pressure deficit (kPa)

**Example Calculation**:
For 10,000 kg plums (average diameter 55 mm, surface area 95 cm²/fruit, 133 fruits/kg):

Total surface area: $A = 10,000 \times 133 \times 0.0095 = 12,635$ m²

At 90% RH (VPD = 0.061 kPa):
$$\frac{dm}{dt} = 1.0 \times 10^{-6} \times 12,635 \times 0.061 = 0.77 \text{ kg/h}$$

Daily moisture loss: $0.77 \times 24 = 18.5$ kg/day (0.185% per day)

At 85% RH (VPD = 0.092 kPa):
$$\frac{dm}{dt} = 1.0 \times 10^{-6} \times 12,635 \times 0.092 = 1.16 \text{ kg/h}$$

Daily moisture loss: $1.16 \times 24 = 27.8$ kg/day (0.278% per day)

**Conclusion**: Reducing RH from 90% to 85% increases moisture loss by 50%, demonstrating the critical importance of humidity control.

### Humidification System Design

**Ultrasonic Humidifiers**: Preferred for plum storage due to minimal heat input and fine droplet size (1-5 μm) that evaporates before settling on fruit surfaces.

Humidification capacity requirement:
$$Q_h = \frac{dm}{dt} + L_{inf}$$

Where:
- Q_h = required humidification capacity (kg/h)
- dm/dt = calculated moisture loss from fruit
- L_inf = moisture loss through infiltration

Infiltration moisture loss:
$$L_{inf} = \frac{V \cdot n \cdot \rho_{air} \cdot (W_{out} - W_{in})}{3600}$$

Where:
- V = storage room volume (m³)
- n = air change rate (0.5-1.0 ACH for sealed cold storage)
- ρ_air = air density (1.29 kg/m³ at 0°C)
- W_out, W_in = humidity ratio outside and inside storage (kg water/kg dry air)

## Chilling Injury Prevention

Chilling injury represents a complex physiological response to low-temperature storage that varies significantly among plum varieties.

### Chilling Injury Mechanisms

**Primary Symptoms**:
- Internal flesh browning (oxidation of phenolic compounds)
- Gel breakdown (pectin depolymerization)
- Mealiness (loss of cell-to-cell adhesion)
- Surface pitting (localized tissue collapse)
- Failure to ripen (ethylene perception impairment)
- Off-flavor development (fermentative metabolism)

**Temperature-Time Relationship**:

Chilling injury accumulates according to temperature-time exposure:

$$CI_{index} = \sum_{i=1}^{n} t_i \cdot f(T_i)$$

Where:
- CI_index = cumulative chilling injury index
- t_i = time period at temperature T_i (days)
- f(T_i) = temperature sensitivity function

For susceptible Japanese plums:
$$f(T) = \begin{cases}
0 & T \geq 5°C \\
0.5(T-5)^2 & 0 < T < 5°C \\
12.5 + 0.2T & T \leq 0°C
\end{cases}$$

**Example**: Santa Rosa plums stored at 0°C for 21 days:
$$CI_{index} = 21 \times 12.5 = 262.5$$

Critical threshold for visible symptoms: CI_index > 200

### Conditioning Treatments

**Pre-storage Conditioning**: Exposure to 15-20°C for 1-2 days before cold storage reduces subsequent chilling injury by 30-50%.

**Intermittent Warming**: Periodic warming cycles interrupt chilling injury development.

Recommended protocol:
- Store at optimal temperature for 7-10 days
- Warm to 10-15°C for 1-2 days
- Return to storage temperature
- Repeat cycle as needed

**Temperature Cycling Refrigeration Load**:

Warming load from 0°C to 15°C:
$$Q_{warm} = m \cdot c_p \cdot \Delta T$$

For 10,000 kg plums (c_p = 3.8 kJ/kg·K):
$$Q_{warm} = 10,000 \times 3.8 \times 15 = 570,000 \text{ kJ} = 158 \text{ kWh}$$

Warming at 1°C/hour requires: 158 kWh / 15 hours = 10.5 kW heating capacity

## Internal Breakdown Considerations

Internal breakdown manifests as translucent flesh, gel formation, and loss of structural integrity without external symptoms.

### Breakdown Mechanisms

**Gel Formation**: Pectin degradation enzymes (polygalacturonase, pectin methylesterase) remain active at low temperatures, progressively degrading cell wall structure.

Enzyme activity temperature relationship (Arrhenius):
$$k = A \cdot e^{-E_a/(RT)}$$

Where:
- k = enzyme reaction rate
- A = pre-exponential factor
- E_a = activation energy (typically 50-70 kJ/mol for pectinases)
- R = gas constant (8.314 J/mol·K)
- T = absolute temperature (K)

At 0°C (273 K): Enzyme activity reduced to approximately 10-15% of activity at 20°C, but not completely inhibited.

### Monitoring and Detection

**Non-Destructive Methods**:

1. **Near-Infrared Spectroscopy (NIRS)**
   - Wavelength range: 700-2500 nm
   - Penetration depth: 5-10 mm
   - Detects changes in soluble solids and moisture distribution

2. **Acoustic Firmness Testing**
   - Frequency response: 100-1000 Hz
   - Correlates with tissue integrity
   - Non-contact measurement

3. **X-ray CT Imaging**
   - Resolution: 0.5-1.0 mm
   - Identifies internal cavities and gel pockets
   - Batch sampling protocol

### Controlled Atmosphere Benefits

Modified atmosphere storage reduces internal breakdown incidence by 40-60%.

**Target Gas Composition**:
- O₂: 1-3%
- CO₂: 3-5%
- N₂: Balance

**Respiratory Gas Exchange**:

Oxygen consumption rate at 0°C:
$$R_{O_2} = 2-5 \text{ mg CO}_2/\text{kg·h}$$

For 10,000 kg plums:
$$R_{O_2} = 10,000 \times 3.5 \times 10^{-3} = 35 \text{ g CO}_2/\text{h}$$

At 0°C, 1 atm: 1 mole CO₂ = 44 g occupies 22.4 L

Volume flow rate: $\frac{35}{44} \times 22.4 = 17.8$ L/h = 0.30 L/min

**CA System Sizing**:

Nitrogen generator capacity:
$$Q_{N_2} = \frac{V_{room} \cdot (0.21 - x_{O_2})}{t_{pulldown}}$$

For 500 m³ room, target 2% O₂, 24-hour pulldown:
$$Q_{N_2} = \frac{500 \times (0.21 - 0.02)}{24} = 3.96 \text{ m}^3/\text{h}$$

Add 20% safety factor: Required capacity = 4.75 m³/h N₂ at 95-99% purity

## Storage Duration by Variety

Maximum storage duration depends on cultivar, harvest maturity, and pre-storage handling.

### Expected Storage Life

| Variety Type | Temperature (°C) | 90% Marketable Quality | 75% Marketable Quality | Limiting Factor |
|-------------|------------------|------------------------|------------------------|-----------------|
| Japanese - Low CI Resistance | 0 | 2-3 weeks | 4-5 weeks | Chilling injury |
| Japanese - Moderate CI Resistance | 0 | 4-5 weeks | 6-7 weeks | Softening, CI |
| Japanese - High CI Resistance | 0 | 6-8 weeks | 10-12 weeks | Softening |
| European - Fresh Market | 0-2 | 4-6 weeks | 7-8 weeks | Softening |
| European - Processing | 0-2 | 6-8 weeks | 10-12 weeks | Surface defects |

### Quality Degradation Kinetics

Firmness loss follows first-order kinetics:

$$F(t) = F_0 \cdot e^{-kt}$$

Where:
- F(t) = firmness at time t (N)
- F_0 = initial firmness (N)
- k = rate constant (day⁻¹)
- t = storage time (days)

At 0°C: k = 0.015-0.025 day⁻¹ for Japanese plums
At 2°C: k = 0.025-0.040 day⁻¹ for Japanese plums

Temperature coefficient (Q₁₀): 1.8-2.2

Rate constant temperature relationship:
$$k(T_2) = k(T_1) \cdot Q_{10}^{(T_2-T_1)/10}$$

**Example**: Plums with initial firmness 60 N stored at 0°C (k = 0.020 day⁻¹):

After 28 days:
$$F(28) = 60 \cdot e^{-0.020 \times 28} = 60 \cdot e^{-0.56} = 60 \times 0.571 = 34.3 \text{ N}$$

Minimum acceptable firmness for most markets: 25-30 N

## Refrigeration System Design

Plum storage refrigeration systems must provide precise temperature control, high evaporator efficiency to maintain humidity, and uniform air distribution.

### Cooling Load Components

**Product Load**:

Field heat removal from 20°C to 0°C:
$$Q_{product} = \frac{m \cdot c_p \cdot \Delta T}{t_{cool}}$$

For 10,000 kg plums, 24-hour cooling period:
$$Q_{product} = \frac{10,000 \times 3.8 \times 20}{24 \times 3600} = 8.80 \text{ kW}$$

**Respiration Heat**:
$$Q_{resp} = m \cdot r$$

Where r = specific heat of respiration at 0°C = 0.010-0.015 W/kg

$$Q_{resp} = 10,000 \times 0.012 = 120 \text{ W} = 0.12 \text{ kW}$$

**Transmission Load** (well-insulated room, U = 0.20 W/m²·K, 300 m² surface area, 20°C ambient):
$$Q_{trans} = U \cdot A \cdot \Delta T = 0.20 \times 300 \times 20 = 1,200 \text{ W} = 1.20 \text{ kW}$$

**Infiltration Load** (0.5 ACH, 500 m³ room volume):

Volumetric flow: $V = 500 \times 0.5 / 3600 = 0.0694$ m³/s

Sensible load:
$$Q_{sens} = \rho \cdot c_p \cdot V \cdot \Delta T = 1.29 \times 1.005 \times 0.0694 \times 20 = 1.79 \text{ kW}$$

Latent load (outdoor air at 20°C, 60% RH, W = 0.0088 kg/kg; storage air W = 0.0038 kg/kg):
$$Q_{lat} = \rho \cdot h_{fg} \cdot V \cdot \Delta W = 1.29 \times 2500 \times 0.0694 \times (0.0088 - 0.0038) = 1.12 \text{ kW}$$

**Lighting, Motors, Personnel**: 0.50 kW (minimal during storage period)

**Total Design Load**:
$$Q_{total} = 8.80 + 0.12 + 1.20 + 1.79 + 1.12 + 0.50 = 13.53 \text{ kW}$$

Add 15% safety factor: **Design capacity = 15.6 kW (4.4 tons)**

### Evaporator Selection

**Coil Temperature Differential (TD)**:

Standard practice: TD = 4-6°C for standard humidity storage
Plum storage requirement: TD = 2-3°C to maintain 90-95% RH

Evaporator temperature: $T_{evap} = T_{room} - TD = 0 - 2.5 = -2.5°C$

**Surface Area Calculation**:

$$Q = U_{coil} \cdot A_{coil} \cdot LMTD$$

For U_coil = 25 W/m²·K (finned coil, forced convection):

LMTD with refrigerant at constant -2.5°C, air entering 0.5°C, leaving -0.5°C:
$$LMTD = \frac{(0.5-(-2.5)) - (-0.5-(-2.5))}{\ln\frac{0.5-(-2.5)}{-0.5-(-2.5)}} = \frac{3.0 - 2.0}{\ln(1.5)} = 2.46°C$$

Required coil area:
$$A_{coil} = \frac{15,600}{25 \times 2.46} = 254 \text{ m}^2$$

**Coil Configuration**: 6-8 rows deep, 2.5-3.0 mm fin spacing, aluminum fins on copper tubes

**Defrost Strategy**:

Low coil temperature (-2.5°C) combined with high humidity promotes frost accumulation.

Expected frost accumulation rate:
$$\dot{m}_{frost} = \frac{Q_{latent}}{h_{fg,ice}} = \frac{1,120}{334} = 3.35 \text{ kg/h} = 80 \text{ kg/day}$$

**Defrost Frequency**: Every 8-12 hours
**Defrost Method**: Hot gas defrost (minimize temperature disruption)
**Defrost Duration**: 20-30 minutes
**Drain Pan Heating**: Required to prevent ice buildup

### Refrigerant Selection

**Recommended Refrigerants**:

| Refrigerant | Evap Pressure (kPa) at -2.5°C | Cond Pressure (kPa) at 35°C | GWP | ODP | Comments |
|-------------|-------------------------------|----------------------------|-----|-----|----------|
| R-404A | 355 | 1835 | 3922 | 0 | Traditional, high GWP |
| R-448A | 361 | 1798 | 1387 | 0 | Lower GWP replacement |
| R-449A | 367 | 1820 | 1397 | 0 | Lower GWP replacement |
| R-744 (CO₂) | 3485 | Transcritical | 1 | 0 | Natural, complex system |
| R-717 (NH₃) | 256 | 1352 | 0 | 0 | Natural, toxic, industrial |

**System Selection Criteria**:
- Small facilities (<50 kW): R-448A or R-449A with DX expansion
- Medium facilities (50-200 kW): R-448A/R-449A with liquid overfeed or NH₃
- Large facilities (>200 kW): NH₃ or CO₂ cascade systems

### Compressor Sizing

For R-448A at evaporating temperature -2.5°C, condensing temperature 35°C:

From refrigerant tables:
- h₁ (evaporator outlet, saturated vapor) = 405 kJ/kg
- h₂ (compressor discharge, isentropic) = 435 kJ/kg
- h₃ (condenser outlet, saturated liquid) = 249 kJ/kg
- h₄ (evaporator inlet, after expansion) = 249 kJ/kg

Refrigeration effect: $q_e = h_1 - h_4 = 405 - 249 = 156$ kJ/kg

Compressor work: $w_c = h_2 - h_1 = 435 - 405 = 30$ kJ/kg

COP: $\frac{q_e}{w_c} = \frac{156}{30} = 5.2$

Mass flow rate: $\dot{m} = \frac{Q_{evap}}{q_e} = \frac{15.6}{156} = 0.100$ kg/s = 360 kg/h

Compressor power (isentropic): $P_{comp} = \dot{m} \cdot w_c = 0.100 \times 30 = 3.0$ kW

Actual power (assuming 70% isentropic efficiency, 90% mechanical efficiency):
$$P_{actual} = \frac{3.0}{0.70 \times 0.90} = 4.76 \text{ kW}$$

Select scroll or screw compressor with 5.5 kW motor for adequate reserve capacity.

## Air Circulation Patterns

Proper air distribution prevents temperature stratification and ensures uniform cooling across the entire storage volume.

### Air Velocity Requirements

**Over Fruit**: 0.25-0.50 m/s (50-100 fpm)
**Between Bins**: 0.50-1.0 m/s (100-200 fpm)
**At Evaporator Face**: 2.0-2.5 m/s (400-500 fpm)

**Rationale**: Higher velocities increase heat transfer but also accelerate moisture loss. Optimum balances cooling rate with humidity maintenance.

### Temperature Uniformity

**Target Variation**: ±0.5°C throughout storage volume

**Air Change Rate**:
$$ACR = \frac{Q_{air}}{V_{room}}$$

Required air flow for 15.6 kW cooling load, 1°C temperature rise:
$$Q_{air} = \frac{Q_{cooling}}{\rho \cdot c_p \cdot \Delta T} = \frac{15,600}{1.29 \times 1.005 \times 1} = 12.0 \text{ m}^3/\text{s}$$

For 500 m³ room:
$$ACR = \frac{12.0 \times 3600}{500} = 86.4 \text{ changes/hour}$$

**Fan Power Requirement**:

Assuming 150 Pa static pressure (typical for low-velocity distribution):
$$P_{fan} = \frac{Q \cdot \Delta P}{\eta_{fan}} = \frac{12.0 \times 150}{0.65} = 2,769 \text{ W} = 2.77 \text{ kW}$$

### Distribution System Design

**Top Air Delivery Configuration**:

Evaporator mounted at ceiling level, discharge air directed along ceiling, returns through floor-level intakes or through product mass.

Advantages:
- Natural temperature stratification assists air circulation
- Condensate drainage simplified
- Accessibility for maintenance

Disadvantages:
- Potential for short-circuiting if not baffled properly
- Upper storage layers receive coldest air

**Bottom Air Delivery Configuration**:

Evaporator at floor level or in plenum beneath slatted floor, upward air flow through product mass.

Advantages:
- More uniform temperature distribution
- Efficient use of floor space
- Reduced short-circuiting

Disadvantages:
- Condensate management challenges
- Higher static pressure requirements

**Recommended**: Top air delivery with vertical baffles to direct air down along walls, return through central aisle.

### Bin Stacking Patterns

**Pallet Configuration**:
- Bin dimensions: 1.2 m × 1.0 m × 0.6 m (typical wooden bin)
- Fruit depth: 0.4-0.5 m (limit to reduce compression damage)
- Void space: 15-25% for air circulation
- Stack height: 3-4 bins maximum (without refrigerated air circulation through bins)

**Air Flow Path**:

Horizontal air flow requires minimum 100 mm gaps between bin stacks and walls.

Vertical air flow (if using perforated bins): Size perforations for 0.5 m/s upward velocity.

Perforation area: 10-15% of bin floor area

Pressure drop through 0.4 m depth of plums at 0.5 m/s superficial velocity:
$$\Delta P = 150 \times d = 150 \times 0.4 = 60 \text{ Pa}$$

(Coefficient 150 Pa/m empirically determined for spherical fruit, moderate packing)

## Pre-Cooling Requirements

Rapid removal of field heat before storage entry prevents condensation on fruit surfaces and reduces total refrigeration load.

### Cooling Methods

**Forced-Air Cooling**:

Air drawn through stacked bins by pressure differential.

Cooling time estimation (half-cooling time):
$$t_{1/2} = \frac{c_p \cdot \rho_{fruit} \cdot D}{2 \cdot h}$$

Where:
- c_p = specific heat of plums = 3.8 kJ/kg·K
- ρ_fruit = bulk density = 550 kg/m³
- D = characteristic dimension (fruit diameter) = 0.055 m
- h = surface heat transfer coefficient = 40-60 W/m²·K at 2 m/s air velocity

$$t_{1/2} = \frac{3,800 \times 550 \times 0.055}{2 \times 50} = 1,149 \text{ s} = 19.1 \text{ minutes}$$

Seven-eighths cooling time (99.2% of temperature difference removed):
$$t_{7/8} = 3 \times t_{1/2} = 57 \text{ minutes}$$

**Hydrocooling**:

Immersion or spray cooling with near-freezing water (0.5-1°C).

Advantages:
- Very rapid cooling (10-15 minutes to near water temperature)
- Minimal weight loss
- Removes field dirt and debris

Disadvantages:
- Water disposal requirements
- Fruit wetting may promote decay if not properly dried
- Requires chlorination (50-100 ppm) to prevent cross-contamination

Heat transfer coefficient in water: 500-800 W/m²·K

Half-cooling time in water (h = 650 W/m²·K):
$$t_{1/2} = \frac{3,800 \times 550 \times 0.055}{2 \times 650} = 88 \text{ s} = 1.5 \text{ minutes}$$

**Room Cooling**:

Slowest method, acceptable only for small volumes or non-perishable varieties.

Natural convection heat transfer coefficient: 5-10 W/m²·K

Half-cooling time:
$$t_{1/2} = \frac{3,800 \times 550 \times 0.055}{2 \times 7.5} = 9,393 \text{ s} = 2.6 \text{ hours}$$

Seven-eighths cooling time: **7.8 hours** (unacceptably slow)

### Pre-Cooling System Capacity

For 10,000 kg daily throughput, cooling from 20°C to 2°C in 1 hour:

$$Q_{precool} = \frac{m \cdot c_p \cdot \Delta T}{t} = \frac{10,000 \times 3.8 \times 18}{3600} = 190 \text{ kW}$$

Add respiration heat during cooling (average 0.030 W/kg at 10°C):
$$Q_{resp} = 10,000 \times 0.030 = 300 \text{ W} = 0.3 \text{ kW}$$

**Total pre-cooling load**: 190.3 kW

With 20% safety margin: **Design capacity = 228 kW (65 tons)**

Pre-cooling systems typically operate intermittently, sized for peak harvest periods.

## Quality Monitoring Protocols

Systematic quality assessment ensures timely intervention before unmarketable deterioration occurs.

### Temperature Monitoring

**Sensor Placement**:
- Warmest location (typically near door, upper level): Critical control point
- Product center: Representative of average conditions
- Evaporator return air: System performance indicator
- Multiple depths within bins: Thermal lag assessment

**Sensor Specifications**:
- Type: Platinum RTD (Pt100 or Pt1000)
- Accuracy: ±0.1°C
- Resolution: 0.01°C
- Response time: <30 seconds in air
- Calibration frequency: Annually against NIST-traceable standard

**Data Logging**:
- Sampling interval: 5-15 minutes
- Alarm setpoints: ±1°C from setpoint
- Historical trending: Identify patterns and system degradation

### Humidity Monitoring

**Sensor Type**: Capacitive RH sensor with Pt1000 temperature sensor

**Specifications**:
- Range: 0-100% RH
- Accuracy: ±2% RH (10-90% range)
- Temperature compensation: Integrated
- Drift: <1% per year

**Placement**: Return air stream, away from direct evaporator discharge

### Firmness Assessment

**Penetrometer Testing**:
- Probe diameter: 8 mm (5/16 inch)
- Penetration depth: 8 mm
- Measurement location: Equatorial region, two opposite sides
- Sample size: Minimum 20 fruits per lot
- Frequency: Weekly during storage

**Acceptance Criteria**:
- Initial firmness: 55-70 N
- Minimum marketable: 25-30 N
- Reject threshold: <20 N

### Visual Inspection

**Inspection Protocol**:
- Frequency: Weekly for first month, bi-weekly thereafter
- Sample size: 1% of lot, minimum 50 fruits
- Assessment parameters:
  - Surface defects (scuffs, bruises, decay)
  - Chilling injury symptoms (pitting, browning)
  - Shriveling (moisture loss >5%)
  - Decay incidence

**Documentation**: Photographic records of representative samples, defect incidence rates, trend analysis.

### Respiration Rate Measurement

Respiration monitoring indicates physiological status and predicts remaining storage life.

**Measurement Method**: Sealed chamber CO₂ accumulation

Sample 5-10 kg fruit in sealed container, measure CO₂ concentration change over 2-4 hours.

$$RR = \frac{\Delta CO_2 \cdot V_{chamber}}{m_{fruit} \cdot t}$$

Where:
- RR = respiration rate (mg CO₂/kg·h)
- ΔCO₂ = CO₂ concentration change (mg/L)
- V_chamber = chamber volume (L)
- m_fruit = fruit mass (kg)
- t = measurement duration (h)

**Normal Values at 0°C**: 2-5 mg CO₂/kg·h

**Elevated Respiration** (>8 mg CO₂/kg·h): Indicates:
- Chilling injury progression
- Pathogen infection
- Over-maturity at harvest
- Excessive mechanical damage

**Action**: Prioritize affected lots for immediate marketing or processing.

## System Integration and Control

Automated control systems optimize energy consumption while maintaining critical environmental parameters.

### Control Strategy

**Temperature Control**:
- Primary: Modulating refrigerant flow via electronic expansion valve (EEV)
- Secondary: Variable-speed compressor or hot gas bypass for capacity modulation
- Tertiary: Evaporator fan cycling (use cautiously to avoid stratification)

**Humidity Control**:
- Ultrasonic humidifier with on/off or modulating control
- Setpoint: 92% RH (midpoint of 90-95% range)
- Deadband: ±1% RH to prevent excessive cycling

**Defrost Control**:
- Time-initiated, temperature-terminated
- Initiation: Every 8-12 hours based on frost accumulation monitoring
- Termination: Coil temperature reaches +8 to +10°C
- Post-defrost fan delay: 2-5 minutes (allow condensate drainage, prevent warm air discharge)

### Energy Optimization

**Night Setback**: Not recommended for plum storage due to narrow acceptable temperature range and chilling injury risk.

**Variable Capacity Operation**:

Compressor energy at partial load (variable speed drive, 60% capacity):
$$P_{60\%} = 0.60^{0.7} \times P_{100\%} = 0.68 \times P_{100\%}$$

Energy savings compared to on/off cycling: 15-25%

**Evaporator Fan Control**:

Continuous operation preferred for humidity maintenance and temperature uniformity.

If cycling is necessary (during very light load periods):
- Minimum on-time: 10 minutes per hour
- Maximum off-time: 20 minutes
- Monitor temperature deviation; resume continuous operation if exceeds ±0.3°C

**Heat Recovery**:

Desuperheater or hot gas condenser can provide:
- Domestic hot water
- Floor heating (loading dock, processing areas)
- Pre-heating ventilation air

Available heat from desuperheater (15-20% of total heat rejection):
$$Q_{desup} = 0.18 \times (Q_{evap} + P_{comp}) = 0.18 \times (15.6 + 4.8) = 3.67 \text{ kW}$$

## Troubleshooting Common Issues

| Symptom | Probable Cause | Diagnostic Steps | Corrective Action |
|---------|----------------|------------------|-------------------|
| Temperature >1°C above setpoint | Insufficient capacity | Check evaporator airflow, coil frost, refrigerant charge | Clean coil, defrost, add refrigerant as needed |
| Temperature fluctuation >±0.5°C | Oversized compressor, poor control | Monitor cycling frequency, check EEV operation | Install capacity modulation, tune EEV parameters |
| RH <88% | Excessive coil TD, infiltration | Measure coil temperature, inspect door seals | Raise evaporator temperature, repair seals, increase humidification |
| RH >96%, condensation on fruit | Insufficient air circulation | Check fan operation, air velocity at bins | Increase fan speed, improve air distribution |
| Rapid firmness loss | Temperature too high, over-mature fruit | Verify temperature accuracy, check harvest maturity records | Lower temperature if variety permits, market fruit promptly |
| Internal browning (no external symptoms) | Chilling injury | Review storage duration and temperature history | Implement intermittent warming, adjust storage temperature upward |
| Surface pitting | Chilling injury, low RH | Check CI susceptibility, verify RH sensor accuracy | Raise temperature, increase RH, apply intermittent warming |
| Excessive weight loss (>3%) | Low RH, high air velocity | Measure RH at multiple locations, check air speeds | Increase humidification, reduce air velocity over fruit |
| Mold growth on fruit surface | Condensation, poor sanitation | Inspect for water accumulation, review sanitation practices | Improve air distribution, sanitize storage room, reduce RH slightly |

## References and Standards

**ASHRAE Standards**:
- ASHRAE Handbook - Refrigeration, Chapter 37: Deciduous Tree and Vine Fruit
- ASHRAE Standard 15: Safety Standard for Refrigeration Systems

**Industry Guidelines**:
- USDA Agricultural Handbook 66: The Commercial Storage of Fruits, Vegetables, and Florist and Nursery Stocks
- University of California Postharvest Technology Center: Stone Fruit Recommendations

**Psychrometric Calculations**:
- ASHRAE Fundamentals, Chapter 1: Psychrometrics

**System Design**:
- ASHRAE Handbook - Refrigeration, Chapter 13: Refrigerant System Chemistry
- ASHRAE Handbook - Refrigeration, Chapter 2: Refrigeration Load Calculations
