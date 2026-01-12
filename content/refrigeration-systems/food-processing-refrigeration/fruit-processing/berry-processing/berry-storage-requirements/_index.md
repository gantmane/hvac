---
title: "Berry Storage Requirements"
description: "Comprehensive HVAC design parameters for berry storage facilities including temperature control, high humidity maintenance, respiration heat loads, and air circulation requirements for strawberries, blueberries, raspberries, and other berries."
weight: 5
---

## Technical Overview

Berry storage presents unique HVAC challenges due to the high respiration rates, delicate nature, and critical moisture requirements of these perishable fruits. Proper environmental control directly impacts shelf life, quality retention, and marketability. Berry storage systems must maintain precise temperature control within ±0.5°C, relative humidity between 90-95%, and carefully managed air velocities to prevent desiccation while providing adequate heat removal.

The high surface-area-to-volume ratio of berries results in rapid moisture loss when vapor pressure deficits exceed 0.1 kPa. Simultaneously, berries generate significant metabolic heat that must be removed efficiently to prevent tissue breakdown and microbial growth. Storage facility design must balance these competing requirements through integrated refrigeration, humidification, and air distribution systems.

## Temperature Requirements by Berry Type

Temperature control is the primary factor determining berry storage life. Each berry variety has specific optimal storage temperatures based on chilling sensitivity, respiration rate, and tissue composition.

### Cold-Hardy Berries

**Strawberries (Fragaria × ananassa)**
- Optimal storage temperature: 0 to 0.5°C
- Maximum storage duration: 7-10 days at 0°C
- Freezing point: -0.8°C
- Temperature uniformity requirement: ±0.5°C
- Critical control point: maintain above freezing to prevent ice crystal formation

**Blueberries (Vaccinium corymbosum)**
- Optimal storage temperature: -0.5 to 0°C
- Maximum storage duration: 14-21 days
- Freezing point: -1.1°C
- Chilling tolerance: excellent, can withstand temperatures to -1°C
- Respiration rate at 0°C: 4-8 mg CO₂/kg·h

**Raspberries (Rubus idaeus)**
- Optimal storage temperature: 0 to 0.5°C
- Maximum storage duration: 2-3 days (highly perishable)
- Freezing point: -0.9°C
- Critical requirement: immediate cooling post-harvest
- Gray mold susceptibility: high at temperatures above 2°C

**Blackberries (Rubus fruticosus)**
- Optimal storage temperature: -0.5 to 0°C
- Maximum storage duration: 3-5 days
- Freezing point: -0.8°C
- Firmness retention: critical parameter for handling

**Cranberries (Vaccinium macrocarpon)**
- Optimal storage temperature: 2 to 4°C
- Maximum storage duration: 2-4 months (extended compared to other berries)
- Freezing point: -1.0°C
- Natural antimicrobial compounds: extend storage life
- Lower temperature tolerance: cranberries tolerate near-freezing better than most berries

**Currants and Gooseberries (Ribes spp.)**
- Optimal storage temperature: -0.5 to 0°C
- Maximum storage duration: 10-14 days
- Freezing point: -0.9°C
- Firm skin structure: provides better storage characteristics than soft berries

### Temperature Control System Design

Refrigeration systems for berry storage must provide:
- Rapid pulldown capacity: reduce product temperature from 20°C to 2°C within 2-4 hours
- Precise temperature control: electronic expansion valves with ±0.3°C control accuracy
- Minimal temperature stratification: not exceeding 1°C between floor and ceiling
- Evaporator coil design: large face area to minimize air-side temperature differential

## High Humidity Requirements and Control

Berry storage requires relative humidity (RH) maintenance between 90-95% to minimize transpiration losses while avoiding free surface moisture that promotes fungal growth.

### Moisture Loss Mechanisms

Transpiration rate equation for berries:
```
W = (Pₛ - Pₐ) × A / Rₜ
```

Where:
- W = water loss rate (kg/h)
- Pₛ = vapor pressure at berry surface (kPa)
- Pₐ = vapor pressure of surrounding air (kPa)
- A = surface area (m²)
- Rₜ = total resistance to moisture transfer (kPa·h/kg)

For strawberries at 0°C:
- Pₛ at berry surface (assumed at 100% RH) = 0.611 kPa
- Pₐ at 90% RH = 0.550 kPa
- Vapor pressure deficit (VPD) = 0.061 kPa

Weight loss exceeding 5% causes visible shriveling and market rejection.

### Humidification System Design

**Ultrasonic Humidifiers**
- Droplet size: 1-5 μm
- Evaporation efficiency: >95% before settling
- Energy consumption: 0.05-0.08 kW per kg/h output
- Advantage: no heat addition to space
- Maintenance requirement: weekly demineralization

**High-Pressure Fog Systems**
- Operating pressure: 5-7 MPa (50-70 bar)
- Droplet size: 10-15 μm
- Complete evaporation distance: 2-3 m
- Distribution uniformity: critical for large storage rooms
- Water quality requirement: <50 ppm total dissolved solids

**Evaporative Pad Systems**
- Medium: cellulose or synthetic fiber
- Pressure drop: 25-50 Pa at 2.5 m/s face velocity
- Humidification efficiency: 80-90%
- Limitation: adds minimal sensible cooling load

### Humidity Control Strategies

Maintain humidity through:
1. Oversized evaporator coils with minimal TD (temperature differential)
2. Hot gas bypass or electronic expansion valve modulation
3. Continuous humidification during refrigeration operation
4. Humidity sensor placement: multiple locations at product level

## Respiration Heat Load Calculations

Respiration generates metabolic heat that represents a significant component of the refrigeration load in berry storage facilities.

### Heat of Respiration Values

| Berry Type | Temperature (°C) | Respiration Rate (mg CO₂/kg·h) | Heat Generation (W/tonne) |
|------------|------------------|--------------------------------|---------------------------|
| Strawberries | 0 | 8-12 | 5.8-8.7 |
| Strawberries | 5 | 18-25 | 13.1-18.2 |
| Strawberries | 10 | 35-45 | 25.5-32.8 |
| Blueberries | 0 | 4-8 | 2.9-5.8 |
| Blueberries | 5 | 10-15 | 7.3-10.9 |
| Blueberries | 10 | 20-30 | 14.6-21.8 |
| Raspberries | 0 | 12-20 | 8.7-14.6 |
| Raspberries | 5 | 30-45 | 21.8-32.8 |
| Raspberries | 10 | 70-100 | 51.0-72.8 |
| Blackberries | 0 | 10-18 | 7.3-13.1 |
| Blackberries | 5 | 25-35 | 18.2-25.5 |
| Cranberries | 2 | 3-5 | 2.2-3.6 |
| Cranberries | 10 | 8-12 | 5.8-8.7 |

Conversion factor: 1 mg CO₂/kg·h = 0.728 W/tonne

### Total Refrigeration Load Calculation

For a berry storage facility, the total refrigeration load consists of:

**Q_total = Q_product + Q_respiration + Q_transmission + Q_infiltration + Q_equipment + Q_people**

**Product Cooling Load:**
```
Q_product = m × cₚ × ΔT / t_cooldown
```

Example for 10,000 kg strawberries:
- m = 10,000 kg
- cₚ = 3.9 kJ/(kg·K) (strawberries at 85% moisture)
- ΔT = 20°C - 0°C = 20 K
- t_cooldown = 4 hours = 14,400 seconds

Q_product = 10,000 × 3.9 × 20 / 14,400 = 54.2 kW (peak)

**Respiration Load:**
For strawberries at 0°C with respiration rate of 10 mg CO₂/kg·h:
```
Q_respiration = 10,000 kg × 7.28 W/tonne = 72.8 W = 0.073 kW
```

**Transmission Load:**
Through insulated walls (assuming 500 m² surface area, U=0.20 W/m²·K, ΔT=35 K):
```
Q_transmission = U × A × ΔT = 0.20 × 500 × 35 = 3.5 kW
```

**Infiltration Load:**
Air changes per 24 hours varies with room volume and door traffic:
- Small rooms (<100 m³): 2-3 air changes per hour
- Medium rooms (100-500 m³): 1-2 air changes per hour
- Large rooms (>500 m³): 0.5-1 air changes per hour

For 300 m³ storage at 1.5 ACH:
```
Q_infiltration = V × ACH × ρ × Δh / 3600
```
Where Δh = enthalpy difference between outside and inside air

Assuming outside conditions: 30°C, 60% RH (h = 76 kJ/kg)
Inside conditions: 0°C, 95% RH (h = 4 kJ/kg)

Q_infiltration = 300 × 1.5 × 1.2 × (76-4) / 3600 = 10.8 kW

## Air Circulation and Velocity

Proper air circulation removes respiration heat and maintains temperature uniformity without causing excessive moisture loss or physical damage to berries.

### Air Velocity Requirements

**Maximum Air Velocities Over Product:**
- Strawberries: 0.25-0.5 m/s
- Blueberries: 0.3-0.6 m/s (firmer skin tolerates higher velocity)
- Raspberries: 0.15-0.25 m/s (extremely delicate)
- Blackberries: 0.2-0.4 m/s
- Cranberries: 0.5-1.0 m/s (firmest berries)

Velocities exceeding these values cause:
1. Accelerated moisture loss through increased convective mass transfer
2. Potential physical damage to delicate fruit
3. Package disruption and product displacement

### Air Change Rates

Storage room air circulation requirements:
- Minimum: 30-40 air changes per hour
- Typical: 40-60 air changes per hour
- High-density loading: 60-80 air changes per hour

For a 300 m³ storage room requiring 50 ACH:
```
Airflow = 300 m³ × 50 h⁻¹ / 3600 s/h = 4.17 m³/s = 8,830 CFM
```

### Evaporator Coil Selection

**Temperature Differential (TD):**
The difference between air-off temperature and refrigerant evaporating temperature must be minimized:
- Standard practice: 8-10 K TD
- Berry storage: 4-6 K TD (to maintain humidity)
- Premium systems: 2-3 K TD (with increased coil surface area)

**Coil Face Velocity:**
Lower face velocities improve dehumidification efficiency but reduce capacity:
- Recommended range: 2.0-2.5 m/s
- Maximum: 3.0 m/s
- Calculate required face area:

For 8,830 CFM (4.17 m³/s) at 2.5 m/s face velocity:
```
Face Area = 4.17 m³/s / 2.5 m/s = 1.67 m²
```

**Fin Spacing:**
Wider fin spacing reduces frost accumulation:
- Standard refrigeration: 4-6 fins per inch (FPI)
- High humidity applications: 3-4 FPI
- Berry storage recommendation: 3 FPI with regular defrost cycles

## Rapid Cooling Necessity

Berries must be cooled immediately after harvest to slow respiration and extend shelf life. Each hour of delay at ambient temperature reduces storage life by 1-2 days.

### Cooling Methods

**Forced Air Cooling (Recommended Primary Method):**
- Principle: Pull cold air through palletized product
- Cooling rate: 0.5-0.75°C per hour (7/8 cooling time: 2-4 hours)
- System components: dedicated cooling plenum, high-capacity fans, oversized evaporator
- Airflow rate: 1-2 L/s per kg of product

**Room Cooling (Supplementary):**
- Slower cooling rate: 0.15-0.25°C per hour
- Acceptable only for small quantities
- Inefficient use of storage space during cooldown

**Hydrocooling (Limited Application):**
- Rapid cooling: achieve target temperature in 15-30 minutes
- Water temperature: 0-1°C
- Limitation: excessive moisture can promote fungal growth on some berries
- Best suited for: strawberries in water-resistant packaging

### Seven-Eighths Cooling Time Calculation

The time required to cool product to within 1/8 of the initial temperature differential:

```
t₇/₈ = -ln(1/8) / h × (ρ × cₚ × V) / (h × A)
```

Simplified for forced air cooling of berries in ventilated containers:
```
t₇/₈ ≈ 1.5 to 3.0 hours (depending on packaging and airflow)
```

## Storage Duration and Quality Parameters

| Berry Type | Storage Temp (°C) | RH (%) | Max Storage (days) | Critical Quality Loss Factor |
|------------|-------------------|--------|-------------------|----------------------------|
| Strawberries | 0 to 0.5 | 90-95 | 7-10 | Botrytis growth, softening |
| Blueberries | -0.5 to 0 | 90-95 | 14-21 | Shriveling, stem end browning |
| Raspberries | 0 to 0.5 | 90-95 | 2-3 | Leakage, mold, collapse |
| Blackberries | -0.5 to 0 | 90-95 | 3-5 | Red cell reversion, leakage |
| Cranberries | 2 to 4 | 90-95 | 60-120 | Rot, softening |
| Currants | -0.5 to 0 | 90-95 | 10-14 | Stem drying, shriveling |
| Gooseberries | -0.5 to 0 | 90-95 | 10-14 | Shriveling, softening |

## Ethylene Management

While berries have low ethylene production rates (0.01-0.1 μL/kg·h), they exhibit moderate to high ethylene sensitivity:
- Effect: accelerated softening and color change
- Control strategy: maintain <0.5 ppm ethylene in storage atmosphere
- Ventilation requirement: 1-2 air changes per day with outside air
- Alternative: activated carbon or potassium permanganate ethylene scrubbers

## Controlled Atmosphere Storage (Advanced Application)

Limited commercial application for berries due to short storage duration, but research shows benefits:

**Optimal CA Conditions for Extended Storage:**
- Oxygen: 5-10% (reduced from ambient 21%)
- Carbon dioxide: 10-20% (elevated from ambient 0.04%)
- Temperature: maintained at optimal for variety
- Extension of storage life: 50-100% increase over air storage

**System Requirements:**
- Gas-tight storage room construction
- Nitrogen generation or supply system
- CO₂ scrubbing capability (lime or molecular sieve)
- O₂ and CO₂ monitoring and control systems

## Packaging Considerations for HVAC Design

Berry packaging directly affects heat and mass transfer:
- Ventilated clamshells: allow 5-8% vent area for air circulation
- Forced air cooling: requires aligned vent holes for horizontal airflow
- Pallet stacking: maintain 5-10 cm air gaps between pallets
- Load density: do not exceed 250-300 kg/m² to prevent crushing

## Post-Harvest Treatments

**Fungicide Application:**
- Timing: within 2 hours of harvest
- HVAC consideration: adequate ventilation during application and drying
- Air changes: minimum 10 ACH during treatment

**Sulfur Dioxide Fumigation (Grapes/Some Berries):**
- Concentration: 50-100 ppm for 20-30 minutes
- Requirement: sealed fumigation chamber separate from main storage
- Exhaust system: scrubber for SO₂ removal before atmospheric discharge

**Ozone Treatment:**
- Concentration: 0.1-0.3 ppm continuous or 1-5 ppm pulsed
- Ozone generation: corona discharge or UV systems
- Material compatibility: ozone degrades many elastomers and plastics
- Destruction: catalytic converter before air discharge

**UVC Light Surface Disinfection:**
- Wavelength: 254 nm
- Dosage: 1000-2000 μJ/cm² for surface treatment
- Integration: tunnel system during packaging or robotic systems
- HVAC isolation: prevent UV exposure to personnel

## System Design Checklist

1. Refrigeration capacity: include 20-30% safety factor for respiration and infiltration
2. Temperature control: precision electronic controls with ±0.5°C accuracy
3. Humidity maintenance: dedicated humidification system targeting 90-95% RH
4. Air distribution: uniform velocities not exceeding 0.5 m/s at product level
5. Rapid cooling: forced air cooling capability for immediate post-harvest treatment
6. Defrost system: hot gas or electric defrost with minimal temperature rise
7. Monitoring: continuous temperature and humidity recording at multiple locations
8. Backup systems: redundant refrigeration or emergency cooling capability
9. Sanitation: cleanable surfaces and drainage for regular washdown
10. Alarm systems: temperature deviation, humidity deviation, power failure alerts