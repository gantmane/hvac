---
title: "Potato Storage Refrigeration Systems"
aliases: ["Potato Storage Refrigeration Systems"]
description: "Engineering design for long-term potato storage facilities including curing processes, temperature and humidity control, sprouting prevention, and refrigeration load calculations for various potato end uses"
weight: 1
---

## Storage Temperature Requirements by End Use

Potato storage temperature is determined by the intended market destination. Temperature directly affects sugar accumulation through enzymatic conversion of starch.

| End Use | Temperature Range | Critical Parameters |
|---------|------------------|-------------------|
| Seed potatoes | 3-4°C (37-39°F) | Maintain dormancy, prevent sprouting |
| Table stock (fresh market) | 7-10°C (45-50°F) | Minimize sugar accumulation, maintain quality |
| Chipping potatoes | 7-10°C (45-50°F) | Prevent reducing sugars, avoid dark chips |
| French fry processing | 7-10°C (45-50°F) | Control sugar content for color |
| Dehydration processing | 10-13°C (50-55°F) | Higher temperature acceptable |

**Temperature Uniformity:** Maintain ±0.5°C throughout storage volume to prevent localized sugar accumulation or sprouting.

## Curing Process Requirements

Curing heals mechanical injuries from harvest and develops skin set to reduce moisture loss and disease susceptibility.

### Curing Parameters

| Parameter | Value | Duration |
|-----------|-------|----------|
| Temperature | 15-20°C (59-68°F) | 10-14 days |
| Relative humidity | 95-99% | Throughout curing |
| Air velocity | 0.15-0.25 m/s | Over potato surface |
| Oxygen concentration | >19% | Prevent anaerobic conditions |

### Wound Healing Process

Curing temperature initiates suberization and periderm formation:

**Suberization rate** = f(T, RH, O₂)

Where healing rate increases exponentially with temperature up to 20°C. Above 20°C, respiration increases faster than healing.

**Heat generation during curing:**
- Fresh potatoes: 0.12-0.18 W/kg at 15-20°C
- Peak respiration occurs days 3-5 of curing

### Curing Load Calculations

Total refrigeration load during curing:

Q_total = Q_resp + Q_infiltration + Q_ventilation + Q_fans

**Respiratory heat:**
Q_resp = m × q_resp × (1 + α(T - T_ref))

Where:
- m = potato mass (kg)
- q_resp = specific heat of respiration at reference temperature (W/kg)
- α = temperature coefficient (0.08-0.12/°C)
- T = curing temperature (°C)
- T_ref = reference temperature (typically 0°C)

## Storage Humidity Control

Target relative humidity: 95% ± 2%

### Moisture Balance

Potatoes contain 78-82% moisture. Weight loss exceeds 5-6% results in visible shriveling and market loss.

**Vapor pressure deficit (VPD):**

VPD = P_sat(T_potato) - P_air

Where:
- P_sat(T_potato) = saturation pressure at potato surface temperature
- P_air = partial pressure of water vapor in air

**Maintaining VPD < 0.2 kPa** minimizes moisture loss while preventing condensation.

### Humidity Generation Systems

**Evaporative pad humidifiers:**
- Efficiency: 80-90%
- Water consumption: 15-25 L/tonne/month
- Air velocity through pad: 1.5-2.5 m/s

**High-pressure fog systems:**
- Droplet size: 5-15 μm
- Coverage: 50-100 m² per nozzle
- Pressure: 4000-7000 kPa (580-1015 psi)
- Evaporation efficiency: >95%

**Ultrasonic humidifiers:**
- Frequency: 1.65-2.4 MHz
- Capacity: 0.5-2.0 kg/h per head
- Power consumption: 50-150 W per head

### Dehumidification Requirements

During warm outdoor conditions or initial storage fill, dehumidification prevents condensation on building surfaces.

**Latent load from potato moisture release:**

Q_latent = (m_potato × E_rate × h_fg) / 3600

Where:
- E_rate = evaporation rate (kg/kg/h) = 0.0001-0.0003
- h_fg = latent heat of vaporization (2450 kJ/kg at 10°C)

## Sprouting Prevention

Sprouting reduces market value and increases respiration heat load. Control methods include temperature management, sprout inhibitors, and ethylene application.

### Physiological Dormancy

Natural dormancy duration: 60-150 days depending on cultivar.

**Dormancy period** influenced by:
- Growing season temperature
- Maturity at harvest
- Post-harvest handling
- Storage temperature

### Temperature Effect on Sprouting

Sprouting occurs at temperatures above 4°C after dormancy break:

| Temperature | Sprout Growth Rate |
|-------------|-------------------|
| 3-4°C | Minimal (<0.5 mm/week) |
| 5-7°C | Slow (1-2 mm/week) |
| 8-10°C | Moderate (3-5 mm/week) |
| >12°C | Rapid (>8 mm/week) |

### Chemical Sprout Inhibitors

**CIPC (Chlorpropham):**
- Application rate: 15-30 g/tonne
- Application timing: Before sprout emergence
- Effective duration: 3-5 months
- Temperature requirement: >10°C for vaporization
- Ventilation: Stop airflow during application

**1,4-Dimethylnaphthalene (DMN):**
- Vapor-release formulation
- Duration: 6-9 months
- Application: Place sachets in storage

### Ethylene Sprout Control

Low-concentration ethylene (10-20 ppm) prevents sprouting:
- Application: Continuous or pulse dosing
- Pulse: 100-150 ppm for 24-48 hours every 2-4 weeks
- Scrubbing required to prevent accumulation

## Sugar Accumulation and Sweetening

Low-temperature sweetening results from enzymatic conversion of starch to reducing sugars (glucose and fructose).

### Biochemical Process

Starch → Maltose → Glucose (by amylase)

**Temperature effect on sugar content:**

Reducing sugars increase exponentially below 7°C:

S(t) = S₀ + k × exp(-E_a/RT) × t

Where:
- S(t) = reducing sugar content at time t (% fresh weight)
- S₀ = initial sugar content
- k = rate constant
- E_a = activation energy (varies by cultivar)
- R = universal gas constant
- T = absolute temperature (K)

### Processing Quality Criteria

| Product | Max Reducing Sugars | Max Sucrose |
|---------|-------------------|-------------|
| Chipping | 0.20-0.35% | 1.5-2.5% |
| French fry | 0.25-0.40% | 2.0-3.0% |
| Fresh market | <1.0% | <3.0% |

### Reconditioning

Warming potatoes before processing reduces sugar content through respiratory consumption:

**Reconditioning protocol:**
- Temperature: 15-20°C
- Duration: 7-14 days
- Sugar reduction: 30-50% of accumulated sugars
- RH: Maintain 90-95%

**Respiration during reconditioning:**
- 0.15-0.25 W/kg at 15°C
- 0.20-0.35 W/kg at 20°C

## Carbon Dioxide Management

CO₂ accumulation from potato respiration requires ventilation management.

### Respiratory CO₂ Production

CO₂ production rate correlates with respiration heat:

**Respiratory quotient (RQ):**
RQ = CO₂ produced / O₂ consumed = 0.95-1.05 for potatoes

**CO₂ generation:**

V_CO₂ = m_potato × R_CO₂ × f(T)

Where:
- R_CO₂ = CO₂ production rate at reference temperature (mL/kg/h)
- f(T) = temperature factor = Q₁₀^((T-T_ref)/10)
- Q₁₀ = 2.0-2.5 for potatoes

### CO₂ Concentration Limits

| Condition | CO₂ Level | Impact |
|-----------|-----------|---------|
| Normal storage | <0.5% | Optimal conditions |
| Warning level | 0.5-1.0% | Monitor closely |
| Blackheart risk | >1.5% | Anaerobic respiration begins |
| Critical level | >3.0% | Severe internal damage |

**Blackheart disorder:**
- Anaerobic respiration causes internal black discoloration
- Results from inadequate O₂ (<2%) or excess CO₂ (>3%)
- Occurs in pile centers with poor air circulation

### Ventilation Requirements

**Minimum air exchange rate:**

Q_vent = (V_CO₂ × 10⁶) / ((C_CO₂,in - C_CO₂,out) × 3600)

Where:
- Q_vent = ventilation rate (m³/h)
- V_CO₂ = CO₂ production (mL/h)
- C_CO₂,in = inlet CO₂ concentration (ppm)
- C_CO₂,out = target storage CO₂ concentration (ppm)

**Typical ventilation rates:**
- Curing: 50-100 m³/tonne/day
- Early storage (0-30 days): 20-40 m³/tonne/day
- Mid storage (30-120 days): 10-20 m³/tonne/day
- Late storage (>120 days): 5-10 m³/tonne/day

## Large-Scale Storage Design

### Storage Configuration Types

**Bulk pile storage:**
- Pile height: 3-5 m (10-16 ft)
- Floor area: 500-3000 m²
- Capacity: 500-5000 tonnes per building
- Air distribution: Pressurized plenum under slatted floor

**Pallet box storage:**
- Stack height: 4-6 boxes (4-6 m)
- Box capacity: 500-1000 kg
- Aisle spacing: 0.3-0.6 m
- Air circulation: Horizontal or vertical

**Bin storage:**
- Bin depth: 2-3 m
- Width: 3-6 m
- Air ducts: Integrated floor or wall systems

### Pressure Bruising Prevention

Excessive pile depth causes compression damage to lower layers.

**Maximum pile depth:**

h_max = (σ_allow × A) / (ρ_bulk × g)

Where:
- σ_allow = allowable stress (2.5-3.5 kPa for potatoes)
- A = contact area fraction
- ρ_bulk = bulk density (650-750 kg/m³)
- g = gravitational acceleration (9.81 m/s²)

**Practical limits:**
- Table stock: 4.5-5.0 m maximum
- Processing potatoes: 4.0-4.5 m maximum
- Seed potatoes: 3.0-3.5 m maximum

### Air Distribution System Design

**Plenum pressure requirements:**

ΔP = f × (L/D) × (ρv²/2) + K × (ρv²/2)

Where:
- f = friction factor (0.02-0.04 for rough surfaces)
- L = airflow path length through pile (m)
- D = hydraulic diameter (m)
- ρ = air density (kg/m³)
- v = air velocity (m/s)
- K = minor loss coefficient

**Target air velocity through pile:**
- 0.02-0.04 m/s during storage
- 0.10-0.20 m/s during curing and cooling

**Plenum static pressure:**
- Bulk pile: 150-400 Pa (0.6-1.6 in. w.g.)
- Pallet boxes: 100-200 Pa (0.4-0.8 in. w.g.)

**Duct sizing for uniform distribution:**
- Velocity reduction method: End velocity ≤ 25% of inlet velocity
- Cross-sectional area increase along duct length
- Dampers every 3-6 m for balancing

## Refrigeration Load Calculations

### Total Refrigeration Load Components

Q_total = Q_resp + Q_field + Q_infiltration + Q_walls + Q_floor + Q_ceiling + Q_lights + Q_fans + Q_defrost

### Respiratory Heat Load

**Peak respiratory load:**

Q_resp = m_potato × q_resp × F_peak

Where:
- m_potato = total potato mass (kg)
- q_resp = specific heat of respiration at storage temperature (W/kg)
- F_peak = peak factor (1.2-1.5 during initial cooldown)

**Respiration rates at storage temperature:**

| Temperature | Heat Output | CO₂ Production |
|-------------|-------------|----------------|
| 3°C | 0.025-0.035 W/kg | 8-12 mL/kg/h |
| 5°C | 0.035-0.050 W/kg | 12-16 mL/kg/h |
| 7°C | 0.050-0.070 W/kg | 16-22 mL/kg/h |
| 10°C | 0.080-0.110 W/kg | 25-35 mL/kg/h |
| 15°C | 0.150-0.200 W/kg | 45-60 mL/kg/h |

### Field Heat Removal Load

Potatoes enter storage at 15-25°C and must be cooled to storage temperature.

**Field heat load:**

Q_field = m_potato × c_p × (T_harvest - T_storage) / t_cooldown

Where:
- c_p = specific heat of potatoes (3.6 kJ/kg·K)
- t_cooldown = cooling period (typically 14-21 days)

**Example:** 1000 tonne storage, harvest at 20°C, cool to 7°C in 14 days:

Q_field = (1,000,000 kg × 3.6 kJ/kg·K × 13 K) / (14 d × 86,400 s/d)
Q_field = 38.7 kW

### Transmission Loads

**Wall, floor, and ceiling heat gain:**

Q_transmission = Σ(U × A × ΔT)

Typical U-values for potato storage:
- Walls: 0.15-0.25 W/m²·K (R-23 to R-38)
- Roof: 0.12-0.20 W/m²·K (R-28 to R-48)
- Floor: 0.30-0.50 W/m²·K (R-11 to R-19)

### Infiltration Load

**Sensible infiltration:**

Q_inf,sens = ρ × c_p × V_inf × (T_out - T_in)

**Latent infiltration:**

Q_inf,lat = ρ × h_fg × V_inf × (ω_out - ω_in)

Where:
- V_inf = infiltration rate (m³/s)
- ω = humidity ratio (kg water/kg dry air)

**Infiltration reduction methods:**
- Vestibule doors: Reduce infiltration 70-80%
- Air curtains: 50-60% reduction
- High-speed doors: 80-90% reduction
- Pressure staging: Maintain 5-10 Pa positive pressure

### Fan Heat Load

**Fan motor heat:**

Q_fan = (P_motor × η_motor) / η_fan

Where:
- P_motor = motor input power (W)
- η_motor = motor efficiency (0.85-0.92)
- η_fan = fan efficiency (0.65-0.80)

Approximately 80-90% of fan power becomes heat in conditioned space.

### Equipment Selection Summary

**Total design capacity:**

Q_design = Q_resp + 0.3 × Q_field + Q_transmission + Q_infiltration + Q_fans + 1.15 × (safety factor)

**Typical capacity requirements:**
- 60-100 W/tonne for storage maintenance
- 150-250 W/tonne for initial cooldown
- Size equipment for 1.15-1.25 × steady-state load

## Equipment Specifications

### Refrigeration System Types

**Direct expansion (DX) systems:**
- Capacity range: 50-500 kW per circuit
- Evaporator temperature: -2 to 2°C
- Refrigerant: R-404A, R-448A, R-449A, R-407F
- Applications: Small to medium storage (<2000 tonnes)

**Flooded ammonia systems:**
- Capacity: 200-2000 kW per system
- Evaporator temperature: -4 to 2°C
- Liquid recirculation ratio: 3:1 to 5:1
- Applications: Large facilities (>2000 tonnes)

**Glycol secondary loop systems:**
- Glycol temperature: -2 to 4°C
- Glycol concentration: 25-35% propylene glycol
- Flow rate: 0.05-0.08 L/s per kW
- Applications: Distributed loads, multiple buildings

### Evaporator Selection

**Unit cooler specifications:**

| Parameter | Value | Notes |
|-----------|-------|-------|
| Face velocity | 2.0-3.0 m/s | Balance capacity and throw |
| Fin spacing | 6-8 mm (0.24-0.31 in) | Wide spacing for low fouling |
| TD (temperature difference) | 4-6 K | Minimize dehydration |
| Defrost method | Off-cycle, hot gas, or electric | Minimize temperature swing |
| Air throw | 20-35 m | Ensure circulation to pile center |

**Capacity derating:**
- Frost accumulation: 10-15% capacity reduction
- Air blockage: 5-10% reduction
- Refrigerant charge variations: 5-8% reduction

### Defrost Strategies

**Off-cycle defrost:**
- Duration: 2-4 hours
- Frequency: Every 6-12 hours
- Application: Storage temperature >6°C, RH <92%

**Hot gas defrost:**
- Duration: 20-40 minutes
- Frequency: Every 4-8 hours
- Temperature spike: <2°C in storage
- Application: Lower temperatures, higher humidity

**Electric defrost:**
- Power: 250-400 W/m² of coil face area
- Duration: 30-60 minutes
- Efficiency: Lower than hot gas
- Application: Small units, DX systems

### Fan Specifications

**Circulation fans:**
- Type: Axial or mixed-flow
- Capacity: 20-40 m³/tonne/h (curing), 5-15 m³/tonne/h (storage)
- Static pressure: 200-500 Pa
- Power: 0.8-1.5 W per m³/h
- Control: VFD for load matching

**Variable frequency drives (VFD):**
- Energy savings: 40-60% compared to constant speed
- Control strategy: CO₂-based or temperature-based modulation
- Minimum speed: 30-40% of rated

## Temperature Monitoring and Control

### Sensor Placement

**Critical monitoring points:**
- Plenum inlet and outlet
- Multiple depths in pile (surface, 1 m, 2 m, pile center)
- Return air to evaporator
- Outdoor ambient
- Product temperature (wireless probes)

**Sensor density:**
- 1 sensor per 100-200 tonnes of potatoes
- Minimum 4 sensors per storage room
- Wireless sensors: Battery life 2-5 years

### Control Strategies

**Proportional-integral (PI) control:**

u(t) = K_p × e(t) + K_i × ∫e(τ)dτ

Where:
- u(t) = control output
- e(t) = error (setpoint - measured)
- K_p = proportional gain (0.5-2.0)
- K_i = integral gain (0.01-0.1)

**Adaptive control:**
- Adjust setpoint based on storage duration
- Gradual temperature reduction: 0.5-1.0°C per week after curing
- Anticipatory control for load changes

**Outdoor air economizer:**
- Engage when T_outdoor < T_storage and ΔT > 1°C
- Free cooling potential: 30-50% of annual load
- Mixed air dampers with minimum ventilation interlock

## USDA Storage Guidelines Summary

USDA Agricultural Handbook 66 and related publications provide baseline storage recommendations:

**Temperature recommendations:**
- Immediate storage after harvest: Begin cooling within 24 hours
- Cooling rate: Not to exceed 0.5°C per day to prevent condensation
- Storage temperature stability: ±0.5°C

**Humidity recommendations:**
- Target RH: 95%
- Acceptable range: 90-98%
- Measure with chilled mirror hygrometers for accuracy

**Storage life by temperature:**
- 3-4°C: 8-10 months
- 7-10°C: 5-7 months
- 12-15°C: 3-4 months

**Quality loss rates:**
- Weight loss: 0.5-1.0% per month at 95% RH
- Sprouting loss: 2-5% per month after dormancy (no inhibitor)
- Disease loss: 1-3% per month (proper storage)

**Air exchange requirements:**
- Curing phase: 60-100 m³/tonne/day
- Storage phase: 10-30 m³/tonne/day
- Base on CO₂ concentration: Maintain <0.5%

**Recommended practices:**
- Grade and sort before storage
- Remove diseased or damaged tubers
- Maintain separate storage for different cultivars
- Monitor for diseases weekly during first month
- Temperature uniformity checks biweekly
- Calibrate sensors quarterly

## Storage Duration and Quality Management

| Storage Duration | Key Management Activities |
|-----------------|---------------------------|
| 0-14 days (Curing) | Maintain 15-20°C, 95-99% RH, monitor wound healing |
| 14-30 days (Cooling) | Gradual cooling 0.5°C/day, monitor condensation |
| 30-90 days (Early storage) | Stabilize at target temperature, initiate sprout control |
| 90-180 days (Mid storage) | Monitor sugar accumulation, adjust ventilation |
| 180-270 days (Late storage) | Increase monitoring frequency, prepare for market |

Potato storage facility design requires integration of refrigeration capacity, air distribution, humidity control, and monitoring systems to maintain product quality throughout the storage season while managing respiratory heat loads and preventing physiological disorders.
