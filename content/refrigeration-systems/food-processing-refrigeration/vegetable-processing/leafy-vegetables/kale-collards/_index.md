---
title: "Kale and Collards Refrigeration"
aliases: ["Kale and Collards Refrigeration"]
description: "Comprehensive technical guide to refrigeration systems for kale and collard greens processing and storage, including precooling methods, respiration heat loads, humidity control, and quality preservation strategies for HVAC professionals."
weight: 4
---

## Overview

Kale (Brassica oleracea var. acephala) and collard greens represent high-respiration, perishable leafy vegetables requiring aggressive cooling protocols and precision environmental control. These cruciferous greens exhibit rapid deterioration at ambient conditions, with visible quality loss occurring within hours if proper refrigeration is not implemented immediately post-harvest.

The primary challenge in kale and collard refrigeration lies in removing field heat rapidly while maintaining extremely high relative humidity to prevent wilting and desiccation. These crops generate significant respiration heat, demand near-freezing storage temperatures, and are highly susceptible to yellowing from both ethylene exposure and inadequate cooling.

## Storage Temperature Requirements

### Optimal Storage Conditions

| Parameter | Specification | Critical Tolerance |
|-----------|--------------|-------------------|
| Storage Temperature | 0°C (32°F) | ±0.5°C |
| Freezing Point | -0.9°C (30.4°F) | Product-specific |
| Relative Humidity | 95-100% | -2% maximum deviation |
| Air Velocity | 60-100 fpm at product surface | Varies by packaging |
| Storage Duration | 14-21 days | Quality-dependent |

### Temperature Impact on Shelf Life

Storage temperature directly controls metabolic activity and degradation rate. The relationship follows the Q10 temperature coefficient:

**Shelf Life Temperature Relationship:**

```
Q10 = (R1/R2)^(10/(T1-T2))
```

Where:
- R1, R2 = Respiration rates at temperatures T1 and T2
- T1, T2 = Storage temperatures (°C)
- Q10 = Temperature coefficient (typically 2.0-3.0 for leafy greens)

For kale and collards, Q10 values range from 2.5 to 3.0, meaning every 10°C temperature increase approximately triples the respiration rate and deterioration speed.

**Shelf Life at Various Temperatures:**

| Storage Temperature | Expected Shelf Life | Deterioration Rate |
|--------------------|--------------------|-------------------|
| 0°C (32°F) | 14-21 days | Baseline (1.0×) |
| 5°C (41°F) | 7-10 days | 2.2× faster |
| 10°C (50°F) | 3-5 days | 5.0× faster |
| 20°C (68°F) | 1-2 days | 12× faster |

### Temperature Uniformity Requirements

Maintaining uniform temperature distribution throughout the storage space is critical:

- Maximum temperature variation within storage: ±1°C
- Product core temperature uniformity: ±0.5°C
- Cooling air temperature approach: 0-1°C below target product temperature
- Return air temperature rise: Maximum 1-2°C

## High Humidity Requirements

### Moisture Loss Prevention

Leafy greens consist of 85-92% water by mass. Vapor pressure deficit (VPD) drives moisture loss from product surfaces:

**Vapor Pressure Deficit Calculation:**

```
VPD = es - ea = es(1 - RH/100)
```

Where:
- VPD = Vapor pressure deficit (kPa)
- es = Saturation vapor pressure at product surface temperature (kPa)
- ea = Actual vapor pressure of surrounding air (kPa)
- RH = Relative humidity (%)

**Critical Humidity Parameters:**

| RH Level | VPD at 0°C | Weight Loss Rate | Quality Impact |
|----------|-----------|------------------|----------------|
| 100% | 0 kPa | <0.1%/day | Ideal |
| 98% | 0.012 kPa | 0.2-0.3%/day | Acceptable |
| 95% | 0.031 kPa | 0.5-0.7%/day | Marginal |
| 90% | 0.061 kPa | 1.0-1.5%/day | Unacceptable |

Weight loss exceeding 3-5% of fresh weight causes visible wilting and marketability loss.

### Humidity Control Strategies

**Evaporator Design Considerations:**

- Low temperature differential (TD): 2-4°C maximum between refrigerant and air
- High fin surface area: 8-12 fins per inch for reduced air velocity
- Oversized coil selection: 150-200% of calculated sensible load
- Electric or hot gas defrost: Minimize temperature cycling
- Coil placement: Uniform air distribution without direct impingement

**Humidification Systems:**

When evaporator design alone cannot maintain 95%+ RH:

- Ultrasonic foggers: 5-20 μm droplet size, minimal wetting
- Centrifugal atomizers: Energy-efficient for large facilities
- Compressed air atomizers: Precise control, higher operating cost
- Wetted media evaporative systems: Lower capital cost, less precise

**Humidification Capacity Calculation:**

```
mw = V × ρa × (W2 - W1)
```

Where:
- mw = Water addition rate (kg/h)
- V = Air volume flow rate (m³/h)
- ρa = Air density (kg/m³)
- W2 = Target humidity ratio (kg water/kg dry air)
- W1 = Supply air humidity ratio (kg water/kg dry air)

## Rapid Precooling Necessity

### Field Heat Removal

Kale and collards harvested during warm conditions (20-30°C ambient) contain substantial field heat that drives rapid deterioration. The "half-cooling time" concept quantifies cooling effectiveness:

**Half-Cooling Time:**

Time required to reduce temperature differential by 50%:

```
t1/2 = (T0 - Tc)/(2 × dT/dt)
```

Where:
- t1/2 = Half-cooling time (hours)
- T0 = Initial product temperature (°C)
- Tc = Cooling medium temperature (°C)
- dT/dt = Cooling rate (°C/hour)

**Target half-cooling times for leafy greens:** 0.25-1.0 hours depending on method.

### Precooling Methods Comparison

| Method | Half-Cooling Time | Cooling Rate | Capital Cost | Operating Cost | Suitability |
|--------|------------------|--------------|--------------|----------------|-------------|
| Hydrocooling | 0.25-0.5 hr | Excellent | Medium | Low | Excellent |
| Package Icing | 0.5-1.0 hr | Good | Low | Medium | Very Good |
| Forced Air | 1.0-2.0 hr | Fair | Medium | Medium | Good |
| Room Cooling | 6-12 hr | Poor | Low | Low | Unacceptable |

## Hydrocooling Systems

### System Design Parameters

Hydrocooling provides the most rapid heat removal for kale and collards by directly contacting produce with cold water. Heat transfer coefficient for water is 15-20× greater than air.

**Hydrocooler Specifications:**

| Parameter | Specification | Design Basis |
|-----------|--------------|--------------|
| Water Temperature | 0-2°C | Near-freezing |
| Water Flow Rate | 15-25 L/min per m² product surface | Turbulent flow |
| Contact Time | 5-15 minutes | Product mass-dependent |
| Water Velocity | 0.3-0.6 m/s | Adequate heat transfer |
| Cooling Capacity | 250-350 kW per tonne/hour throughput | Heat load calculation |

**Hydrocooler Heat Load Calculation:**

```
Qhydro = mp × cp × ΔT / ηt
```

Where:
- Qhydro = Cooling capacity required (kW)
- mp = Product mass flow rate (kg/s)
- cp = Specific heat of product (≈3.9 kJ/kg·K for leafy greens)
- ΔT = Temperature reduction (K)
- ηt = Time efficiency factor (0.7-0.9)

**Water System Components:**

1. Refrigeration unit: Sufficient capacity for continuous operation
2. Water chiller: Plate heat exchanger or flooded evaporator
3. Circulation pumps: Variable speed for flow control
4. Spray manifolds: Uniform distribution over product
5. Conveyor system: Adjustable speed for dwell time control
6. Water filtration: 50-100 μm screen filters
7. Sanitization system: Chlorine (50-150 ppm) or alternative sanitizer
8. Water makeup: Temperature-controlled replenishment

### Water Quality Management

| Parameter | Specification | Monitoring Frequency |
|-----------|--------------|---------------------|
| pH | 6.5-7.5 | Hourly |
| Free Chlorine | 50-150 ppm | Every 2 hours |
| Turbidity | <5 NTU | Daily |
| Total Dissolved Solids | <500 ppm | Weekly |
| Bacterial Count | <500 CFU/mL | Daily |

## Package Icing Systems

### Top Icing Applications

Package icing provides both cooling and humidity maintenance during storage and transport. Ice contact cooling achieves half-cooling times of 0.5-1.0 hours while the ice layer maintains near-100% RH.

**Ice Requirements:**

```
mice = (mp × cp × ΔT + Qresp × t) / hfg
```

Where:
- mice = Ice mass required (kg)
- mp = Product mass (kg)
- cp = Product specific heat (3.9 kJ/kg·K)
- ΔT = Temperature reduction (K)
- Qresp = Respiration heat generation (W)
- t = Cooling and storage time (s)
- hfg = Latent heat of fusion for ice (334 kJ/kg)

**Typical Ice-to-Product Ratios:**

| Application | Ice Ratio (kg ice/kg product) | Purpose |
|-------------|------------------------------|---------|
| Initial Cooling | 0.3-0.5 | Field heat removal |
| Short Transport (<12 hr) | 0.2-0.3 | Temperature maintenance |
| Extended Storage/Transport | 0.4-0.6 | Full cooling + maintenance |

### Icing System Design

**Tube Ice Makers:**

- Tube diameter: 28-44 mm (optimal surface area)
- Ice production capacity: 1.5-2.0× peak demand
- Harvest cycle: 15-25 minutes
- Agglomeration prevention: Bin rakes or air circulation
- Storage bin capacity: 8-12 hours of production

**Crushed or Flake Ice:**

- Particle size: 3-10 mm for good contact
- Higher surface area: Faster cooling than tube ice
- Equipment: Flake ice makers or tube ice crushers
- Distribution: Automated or manual top application
- Layer thickness: 25-50 mm over product surface

## Respiration Rates

### Metabolic Heat Generation

Respiration represents the primary source of heat generation in stored kale and collards. This aerobic process converts sugars to CO2, water, and heat while degrading quality.

**Respiration Heat Generation:**

```
Qresp = R × mp × hr
```

Where:
- Qresp = Respiration heat (W)
- R = Respiration rate (mg CO2/kg·h)
- mp = Product mass (kg)
- hr = Heat release per unit CO2 (0.61 W·h/mg CO2)

**Respiration Rates for Kale and Collards:**

| Temperature | Respiration Rate (mg CO2/kg·h) | Heat Generation (W/tonne) | Relative to 0°C |
|-------------|-------------------------------|--------------------------|----------------|
| 0°C (32°F) | 15-25 | 9-15 | 1.0× |
| 5°C (41°F) | 35-50 | 21-31 | 2.3× |
| 10°C (50°F) | 75-110 | 46-67 | 5.0× |
| 15°C (59°F) | 150-200 | 92-122 | 8.3× |
| 20°C (68°F) | 280-350 | 171-214 | 15.6× |

These rates demonstrate why immediate cooling is essential: product held at 20°C generates 15 times more respiration heat than at 0°C.

### Refrigeration Load Calculation

**Total Cooling Load Components:**

```
Qtotal = Qproduct + Qresp + Qinfiltration + Qequipment + Qlights + Qpeople
```

For a cold storage room holding 10,000 kg of kale at 0°C:

| Load Component | Calculation | Heat Load (kW) |
|---------------|-------------|----------------|
| Product Cooling | 10,000 kg × 3.9 kJ/kg·K × (20-0)K / 3600s | 21.7 |
| Respiration Heat | 10,000 kg × 20 mg/kg·h × 0.61 W·h/mg / 1000 | 0.12 |
| Infiltration (5 air changes/day) | Variable by room size | 3.5 |
| Equipment & Lighting | Facility-specific | 2.0 |
| **Total Design Load** | Sum with 20% safety factor | **32.7** |

### Controlled Atmosphere Effects

Elevated CO2 and reduced O2 concentrations suppress respiration:

**Standard Atmosphere:** 0.04% CO2, 21% O2
- Respiration rate: 15-25 mg CO2/kg·h at 0°C

**Controlled Atmosphere (CA):** 5-10% CO2, 1-3% O2
- Respiration rate: 8-15 mg CO2/kg·h at 0°C (40-50% reduction)
- Extended shelf life: 30-50% increase
- Equipment cost: High initial capital investment

## Yellowing Prevention

### Chlorophyll Degradation Mechanisms

Yellowing results from chlorophyll breakdown through enzymatic and oxidative pathways. The visible transition from green to yellow occurs when chlorophyll degrades faster than carotenoid pigments.

**Primary Degradation Factors:**

1. **Temperature:** Enzyme activity increases exponentially with temperature
2. **Ethylene Exposure:** Accelerates senescence and chlorophyll degradation
3. **Moisture Loss:** Cellular dehydration triggers senescence pathways
4. **Physical Damage:** Wound-induced ethylene production
5. **Prolonged Storage:** Natural aging processes

### Temperature Control

Maintaining 0°C storage temperature is the most effective yellowing prevention strategy:

**Chlorophyll Retention vs. Temperature:**

| Storage Temperature | Days to 50% Yellowing | Chlorophyll Retention at 14 Days |
|--------------------|-----------------------|--------------------------------|
| 0°C (32°F) | 18-24 days | 85-90% |
| 5°C (41°F) | 10-14 days | 60-70% |
| 10°C (50°F) | 5-7 days | 30-40% |
| 20°C (68°F) | 2-3 days | 10-15% |

### Ethylene Management

Kale and collards exhibit moderate sensitivity to ethylene (C2H4). Ethylene exposure at concentrations as low as 0.1 ppm accelerates yellowing and senescence.

**Ethylene Removal Strategies:**

1. **Source Elimination:**
   - Separate from ethylene-producing commodities (apples, bananas, tomatoes)
   - Remove damaged or deteriorating product promptly
   - Minimize mechanical damage during handling

2. **Active Removal Systems:**
   - Potassium permanganate (KMnO4) scrubbers: 0.5-1.0 kg per 100 m³ storage volume
   - Catalytic oxidation: Effective at >0.5 ppm inlet concentration
   - Ozone treatment: 0.05-0.3 ppm continuous (with precautions)
   - Activated carbon filters: Lower efficiency, requires frequent replacement

3. **Ventilation:**
   - Fresh air exchange: 1-2 air changes per 24 hours minimum
   - Dilution effectiveness: Reduces ethylene concentration linearly
   - Energy penalty: Increased cooling load from warm outside air

**Ethylene Scrubber Sizing:**

```
Wscr = (Ceth × V × ACH) / Erem
```

Where:
- Wscr = Scrubber capacity required (kg KMnO4)
- Ceth = Target ethylene removal (ppm)
- V = Storage volume (m³)
- ACH = Air changes per hour through scrubber
- Erem = Removal efficiency (≈100 ppm ethylene per kg KMnO4)

## Storage Duration

### Quality Parameters Over Time

Storage duration depends on maintaining critical quality attributes:

| Quality Parameter | Harvest | 7 Days at 0°C | 14 Days at 0°C | 21 Days at 0°C |
|------------------|---------|---------------|----------------|----------------|
| Color (Visual Score 1-5) | 5.0 | 4.8 | 4.5 | 3.8 |
| Texture (Firmness, N) | 8.5 | 8.0 | 7.2 | 6.0 |
| Weight Loss (%) | 0 | 1.5 | 3.0 | 5.0 |
| Chlorophyll (mg/100g) | 160 | 150 | 135 | 115 |
| Vitamin C (mg/100g) | 120 | 115 | 105 | 90 |
| Marketability (%) | 100 | 95 | 85 | 65 |

### Maximum Storage Life

**Optimal Conditions (0°C, 95-100% RH):**
- Commercial storage: 14-21 days
- Maximum technical storage: 28 days with CA
- Recommended turnover: 10-14 days for premium quality

**Factors Reducing Storage Life:**

- Initial field temperature >15°C: -3 to -5 days
- Delayed cooling (>4 hours): -5 to -7 days
- RH below 90%: -3 to -5 days per 5% RH deficit
- Temperature fluctuation >2°C: -2 to -4 days
- Physical damage during harvest: -5 to -10 days
- Ethylene exposure >0.5 ppm: -4 to -7 days

## Equipment Specifications

### Refrigeration System Components

**Compressor Selection:**

| Capacity Range | Compressor Type | Refrigerant | Efficiency (COP) |
|---------------|----------------|-------------|-----------------|
| <20 kW | Scroll | R-448A, R-449A | 2.5-3.0 |
| 20-100 kW | Screw | R-448A, R-449A | 2.8-3.5 |
| >100 kW | Screw or Centrifugal | R-448A, R-449A, R-134a | 3.0-4.0 |

**Evaporator Design:**

- **Type:** Ceiling-mounted unit coolers with low-velocity discharge
- **Fin spacing:** 4-6 mm (8-10 fins per inch)
- **Face velocity:** 1.5-2.5 m/s maximum
- **Temperature difference:** 3-4°C (refrigerant to air)
- **Defrost type:** Electric or hot gas, 2-4 cycles per 24 hours
- **Defrost termination:** Time + temperature (typically 10-15 minutes)
- **Fan motors:** EC (electronically commutated) for efficiency
- **Capacity multiplier:** 1.5-2.0× calculated sensible load for humidity control

**Condensing Unit:**

- **Type:** Air-cooled or evaporative condenser
- **Ambient design:** -10°C to +40°C operation range
- **Head pressure control:** Fan cycling or variable speed for low ambient
- **Condensing temperature:** 10-15°C above ambient (air-cooled)
- **Refrigerant charge:** Optimized for seasonal efficiency

### Control Systems

**Temperature Control:**

- **Controller type:** PLC or DDC with 0.1°C resolution
- **Sensor type:** RTD (Pt100 or Pt1000), Class A accuracy
- **Sensor locations:**
  - Supply air: Downstream of evaporator coil
  - Return air: Representative of space conditions
  - Product simulator: Wireless probe in representative package
- **Control strategy:** PI or PID with anti-windup
- **Setpoint:** 0°C ± 0.5°C
- **Deadband:** 0.5-1.0°C to prevent short cycling

**Humidity Control:**

- **Measurement:** Capacitive RH sensors, ±2% accuracy at 95-100% RH
- **Calibration:** Monthly verification with chilled mirror hygrometer
- **Control output:** Modulating humidifier or on/off with PWM
- **Alarm threshold:** <93% RH
- **Integration:** Coordinated with refrigeration system to prevent condensation cycling

**Data Logging:**

- **Sample interval:** 5-15 minutes for temperature, 15-30 minutes for RH
- **Storage duration:** Minimum 12 months
- **Alarm notification:** SMS/email for out-of-range conditions
- **HACCP compliance:** Automated reporting and trend analysis

### Air Distribution Design

**Airflow Requirements:**

```
Vair = Qsensible / (ρa × cp,a × ΔT)
```

Where:
- Vair = Air volume flow rate (m³/s)
- Qsensible = Sensible cooling load (kW)
- ρa = Air density ≈ 1.3 kg/m³ at 0°C
- cp,a = Specific heat of air ≈ 1.005 kJ/kg·K
- ΔT = Supply-to-return air temperature difference (2-3°C target)

**Air Changes Per Hour:**

- **Minimum:** 30-40 ACH during pulldown
- **Steady-state:** 15-25 ACH for temperature uniformity
- **High-density storage:** 40-60 ACH to maintain uniformity

**Duct Design:**

For large facilities requiring ducted distribution:

- **Supply duct velocity:** 5-8 m/s maximum to minimize pressure drop
- **Diffuser velocity:** 2-3 m/s at discharge
- **Throw distance:** Sized for room geometry without product impingement
- **Return air:** Low-velocity collection, wall-mounted grilles

## Packaging Considerations

### Package Types and Thermal Performance

| Package Type | Ventilation Area | Cooling Rate | Moisture Retention | Cost |
|-------------|------------------|--------------|-------------------|------|
| Waxed cardboard box | 5-8% open area | Good | Fair | Low |
| Plastic crate | 25-40% open area | Excellent | Poor (requires ice) | Medium |
| Perforated poly bag | 0.5-2% open area | Fair | Excellent | Low |
| Modified atmosphere bag | Controlled permeability | Fair | Excellent | High |
| Bulk bin | 15-25% open area | Good | Fair | Low |

**Ventilation Hole Design:**

Total ventilation area affects cooling rate during forced air or hydrocooling:

```
Acool = 0.05 to 0.08 × Abox
```

Where:
- Acool = Minimum ventilation hole area for effective cooling
- Abox = Box surface area
- Typical ratio: 5-8% for acceptable cooling rates

### Stacking and Pallet Configuration

**Airflow Considerations:**

- **Vertical flue spaces:** 50-75 mm between adjacent pallets
- **Horizontal spacing:** 100-150 mm from walls for air circulation
- **Pallet overhang:** Avoid blocking ventilation holes
- **Stack height:** Maximum 2.0-2.5 m to prevent crushing
- **Load stability:** Stretch wrap or strapping without blocking airflow

## Quality Parameters

### Visual Quality Assessment

**Color Evaluation:**

Objective measurement using colorimetry:

- **L* value:** Lightness (40-50 for dark greens, higher indicates yellowing)
- **a* value:** Green (-15 to -10) to red; increasing a* indicates chlorophyll loss
- **b* value:** Blue to yellow (10-15 for fresh greens)
- **Hue angle:** Calculated as arctan(b*/a*), decreases with yellowing

**Acceptable Quality Limits:**

| Parameter | Grade A (Premium) | Grade B (Standard) | Reject |
|-----------|------------------|-------------------|--------|
| Yellowing | <5% leaf area | 5-15% leaf area | >15% |
| Wilting | None visible | Slight, reversible | Severe |
| Decay | None | None | Any visible |
| Damage | <1% area | 1-5% area | >5% |
| Off-odors | None | None | Any detectable |

### Nutritional Quality

**Key Nutrients in Kale and Collards:**

- **Vitamin C:** 120 mg/100g (fresh)
- **Vitamin K:** 817 μg/100g (fresh)
- **Vitamin A (beta-carotene):** 9,226 IU/100g
- **Calcium:** 150 mg/100g
- **Iron:** 1.5 mg/100g

**Nutrient Retention During Storage:**

| Storage Duration (0°C) | Vitamin C Retention | Vitamin A Retention | Overall Quality |
|----------------------|-------------------|-------------------|-----------------|
| Fresh (0 days) | 100% | 100% | Excellent |
| 7 days | 92-96% | 95-98% | Excellent |
| 14 days | 80-88% | 90-95% | Good |
| 21 days | 65-75% | 85-90% | Fair |

Temperature abuse severely impacts nutrient retention:
- Storage at 10°C for 7 days ≈ 50-60% vitamin C loss
- Storage at 20°C for 3 days ≈ 70-80% vitamin C loss

## Safety and Sanitation

### Food Safety Considerations

**Microbial Control:**

- **Wash water sanitation:** 50-150 ppm chlorine or alternative (PAA 40-80 ppm)
- **Cold chain integrity:** Continuous 0-4°C from field to retail
- **Cross-contamination prevention:** Separate raw and processed product flows
- **Personnel hygiene:** Handwashing stations, protective clothing
- **Facility sanitation:** Daily cleaning protocols for all food contact surfaces

**HACCP Critical Control Points:**

1. **Washing/hydrocooling:** Water temperature and sanitizer concentration
2. **Cooling rate:** Time-temperature monitoring during precooling
3. **Cold storage:** Continuous temperature monitoring with alarms
4. **Transportation:** Refrigerated vehicle performance verification

### Occupational Safety

**Cold Storage Environment:**

- **Personal protective equipment:** Insulated clothing for extended exposure below 5°C
- **Acclimatization:** Gradual exposure for workers entering cold spaces
- **Emergency egress:** Interior door releases, illuminated exit signs
- **Slip prevention:** Frost-free flooring, proper footwear

**Refrigerant Safety:**

- **Leak detection:** Fixed monitors for occupied and mechanical spaces
- **Ventilation:** Emergency exhaust for refrigerant release
- **Training:** Annual refrigerant safety training for maintenance personnel
- **Emergency procedures:** Posted evacuation and response protocols

## Conclusion

Successful refrigeration of kale and collard greens requires integrated attention to rapid precooling, precision temperature control at 0°C, maintenance of 95-100% relative humidity, and protection from ethylene exposure. The high respiration rate and extreme perishability of these leafy vegetables demand aggressive cooling protocols—preferably hydrocooling or package icing—immediately following harvest.

HVAC professionals designing refrigeration systems for kale and collards must size equipment for both the substantial initial cooling load and the ongoing respiration heat generation while selecting evaporator components capable of maintaining the critical high humidity environment. Control systems require precision sensors, reliable data logging for HACCP compliance, and alarm notification to prevent costly product losses from temperature excursions.

Proper implementation of these refrigeration strategies extends marketable storage life to 14-21 days while preserving color, texture, nutritional value, and overall quality that consumers demand from fresh leafy greens.
