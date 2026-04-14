---
title: "Orange Storage"
aliases: ["Orange Storage"]
description: "Engineering specifications for orange cold storage facilities including temperature control, humidity management, degreening processes, and controlled atmosphere parameters for extended shelf life and quality preservation"
weight: 2
---

Orange cold storage requires precise environmental control to maintain fruit quality, minimize physiological disorders, and extend marketable life. HVAC system design must account for variety-specific temperature sensitivities, humidity requirements for moisture retention, and optional degreening or controlled atmosphere protocols. Proper refrigeration strategies prevent chilling injury while controlling fungal decay and physiological breakdown.

## Temperature Requirements by Variety

Orange storage temperatures vary by cultivar, with Florida and California fruit requiring different strategies based on climate adaptation and peel characteristics.

### Valencia Oranges

Storage temperature: 3-9°C (37-48°F)

Valencia oranges tolerate temperatures at the lower end of the orange storage range. The optimal temperature depends on storage duration and initial fruit maturity:

- **Short-term storage (2-4 weeks):** 3-5°C (37-41°F)
- **Extended storage (8-12 weeks):** 5-7°C (41-45°F)
- **Maximum safe duration:** 12 weeks at 5°C (41°F)

Temperature uniformity throughout the storage chamber must maintain ±0.5°C to prevent localized chilling injury. Air circulation rates of 30-60 air changes per hour ensure even cooling without causing dehydration at fruit surfaces.

### Navel Oranges

Storage temperature: 5-9°C (41-48°F)

Navel oranges exhibit greater susceptibility to chilling injury than Valencia cultivars. Temperature management focuses on preventing pitting and rind disorders:

- **California navels:** 7-9°C (45-48°F) for 4-8 weeks
- **Arizona navels:** 5-7°C (41-45°F) for 6-10 weeks
- **Early-season fruit:** Higher temperatures (8-9°C) to prevent pitting
- **Late-season fruit:** Lower temperatures (5-6°C) acceptable with reduced chilling sensitivity

The commercial storage strategy often uses 7°C (45°F) as a compromise temperature providing decay control while minimizing chilling injury risk.

### Blood Oranges

Storage temperature: 4-7°C (39-45°F)

Blood orange varieties (Moro, Tarocco, Sanguinello) require specific temperature management to preserve anthocyanin pigments:

- **Optimal storage:** 5-6°C (41-43°F)
- **Color preservation:** Temperatures below 6°C maintain red pigmentation
- **Maximum duration:** 6-8 weeks before color degradation
- **Anthocyanin stability:** Requires darkness in addition to temperature control

Blood oranges tolerate slightly lower temperatures than standard navels but remain susceptible to peel pitting at temperatures below 3°C.

## Storage Temperature Parameters

| Variety | Temperature Range | Optimal Temperature | Maximum Duration | Chilling Threshold |
|---------|-------------------|---------------------|------------------|-------------------|
| Valencia | 3-9°C (37-48°F) | 5-7°C (41-45°F) | 12 weeks | <3°C (37°F) |
| Navel (Early) | 7-9°C (45-48°F) | 8°C (46°F) | 6 weeks | <5°C (41°F) |
| Navel (Late) | 5-9°C (41-48°F) | 6-7°C (43-45°F) | 10 weeks | <4°C (39°F) |
| Blood Orange | 4-7°C (39-45°F) | 5-6°C (41-43°F) | 8 weeks | <3°C (37°F) |
| Mandarin Hybrid | 4-7°C (39-45°F) | 5°C (41°F) | 8 weeks | <2°C (36°F) |

## Humidity Control Specifications

Relative humidity: 85-90%

Orange storage requires high humidity to prevent moisture loss and maintain peel turgidity. Insufficient humidity causes weight loss, peel shriveling, and reduced marketability.

### Humidity Management Systems

Refrigeration systems for orange storage must incorporate humidity control:

**Direct expansion systems:**
- Evaporator coil TD: 2-3°C (4-5°F) maximum to minimize dehumidification
- Coil surface area: 150-200% of standard refrigeration to reduce TD
- Hot gas defrost: Preferred method to minimize humidity fluctuation

**Flooded evaporator systems:**
- Reduced TD capability improves humidity maintenance
- Liquid overfeed ratio: 3:1 to 4:1 for larger wetted surface
- Gravity or pumped recirculation from accumulator vessel

**Humidification equipment:**
- Ultrasonic foggers: 10-20 micron droplet size prevents surface wetting
- Centrifugal atomizers: Install in supply air ductwork upstream of fans
- Evaporative media: Secondary humidity boost with minimal temperature depression
- Control range: ±3% RH around setpoint

### Moisture Loss Prevention

Weight loss calculation:
```
WL = (Vi - Vf) / Vi × 100
```
Where:
- WL = weight loss percentage
- Vi = initial weight
- Vf = final weight

Acceptable weight loss: 3-5% maximum over storage period

Moisture loss rate depends on vapor pressure deficit (VPD) between fruit surface and surrounding air:
```
VPD = es(Tfruit) - ea
```
Where:
- es(Tfruit) = saturation vapor pressure at fruit surface temperature
- ea = actual vapor pressure of air (RH × es at air temperature)

Target VPD: <0.3 kPa for minimal moisture loss

## Degreening Process Parameters

Ethylene degreening converts chlorophyll in orange peel to reveal underlying carotenoid pigments. This process improves visual appeal for fruit with mature internal quality but green external appearance.

### Degreening Room Conditions

**Temperature:** 20-30°C (68-86°F)
- Optimal: 27-29°C (81-84°F) for Florida oranges
- Optimal: 20-24°C (68-75°F) for California oranges
- Higher temperatures accelerate degreening but increase decay risk

**Relative humidity:** 90-95%
- Maintains peel turgidity during treatment
- Reduces moisture loss and weight shrinkage
- Prevents ethylene-induced peel injury

**Ethylene concentration:** 1-10 ppm (parts per million)
- Standard application: 5 ppm continuous flow
- Citrus-specific: 1-5 ppm to minimize peel damage
- Concentration uniformity: ±0.5 ppm throughout chamber

**Treatment duration:** 24-72 hours
- Florida oranges: 24-48 hours typical
- California oranges: 48-96 hours due to thicker peel
- Monitoring: Visual inspection every 12-24 hours

**Ventilation:** 10-20 air changes per hour
- Ensures ethylene distribution uniformity
- Removes CO2 and metabolic heat
- Prevents accumulation of volatile compounds

### Degreening Room HVAC Design

**Heating capacity:**
- Design load: 150-250 W/m² floor area
- Includes metabolic heat from fruit respiration (20-40 W/tonne at 27°C)
- Infiltration load through door openings
- Outside air ventilation load

**Cooling capacity:**
- Required when ambient exceeds setpoint
- Oversized evaporators (TD = 3-4°C) maintain humidity
- Dehumidification minimized through coil design

**Air distribution:**
- Horizontal airflow across stacked fruit containers
- Velocity at fruit surface: 0.2-0.5 m/s
- Perforated duct distribution for uniformity
- Return air plenum below floor or at ceiling

**Ethylene injection system:**
- Flow-through method: Continuous injection with exhaust to atmosphere
- Recirculation method: Catalytic converter removes ethylene for air reuse
- Concentration monitoring: Electrochemical or infrared sensors
- Safety: Exhaust through activated carbon scrubber if required by regulations

## Degreening Parameters by Variety

| Variety | Temperature | Ethylene (ppm) | Duration | RH |
|---------|-------------|----------------|----------|-----|
| Valencia (FL) | 27-29°C | 3-5 | 24-48 hr | 90-95% |
| Valencia (CA) | 21-24°C | 5-10 | 48-72 hr | 90-95% |
| Navel (CA) | 20-23°C | 5-10 | 48-96 hr | 90-95% |
| Hamlin (FL) | 28-30°C | 3-5 | 18-36 hr | 90-95% |
| Temple | 27-29°C | 5-8 | 24-48 hr | 90-95% |

## Controlled Atmosphere Storage Options

Controlled atmosphere (CA) storage extends orange shelf life beyond conventional refrigerated storage through modification of oxygen and carbon dioxide concentrations.

### CA Parameters for Oranges

**Oxygen concentration:** 5-10%
- Standard protocol: 5-7% O2
- Too low (<3%): Anaerobic respiration causes off-flavors
- Too high (>10%): Minimal benefit over air storage

**Carbon dioxide concentration:** 0-5%
- Moderate elevation: 3-5% CO2
- Fungistatic effect: Inhibits mold growth at elevated CO2
- Peel injury threshold: >10% CO2 causes rind damage

**Temperature:** 5-7°C (41-45°F) during CA storage

**Storage life extension:** CA storage extends marketable life by 25-50% compared to conventional cold storage at equivalent temperature.

### CA Storage Facility Requirements

**Gas-tight construction:**
- Infiltration rate: <2% room volume per day
- Door seals: Inflatable gaskets on all access doors
- Pressure relief valves: Set at 250-500 Pa differential
- Structural design: Withstand ±500 Pa pressure differential

**Atmosphere control equipment:**
- Nitrogen generator: PSA or membrane type for O2 reduction
- CO2 scrubber: Activated carbon or hydrated lime for CO2 removal
- CO2 injection: Liquid CO2 vaporization system if elevation required
- Mixing fans: Continuous operation (10-15 air changes/hour)

**Monitoring and safety:**
- O2 analyzer: Paramagnetic or electrochemical, ±0.1% accuracy
- CO2 analyzer: Infrared, ±0.1% accuracy
- Data logging: Continuous recording at 15-minute intervals
- O2 deficiency alarm: Personnel safety for room entry

## Decay Control Through Environmental Management

Fungal decay represents the primary cause of orange storage losses. Environmental control strategies reduce infection and slow disease progression.

### Temperature Effects on Decay

Lower storage temperatures directly suppress fungal growth rates:

- **Penicillium digitatum** (green mold): Growth rate reduced 50% for each 5°C temperature decrease
- **Penicillium italicum** (blue mold): Minimum growth temperature ~5°C
- **Geotrichum candidum** (sour rot): Growth inhibited below 10°C

Decay control requires maintaining fruit temperature uniformly throughout storage. Warm spots in corners or near doors accelerate fungal growth.

### Humidity and Surface Moisture Management

**Free water elimination:**
- Remove surface moisture before storage entry
- Air circulation without direct impingement on wet fruit
- Condensate drainage prevents dripping on fruit
- Evaporator defrost scheduling to prevent moisture release

**Equilibrium relative humidity:**
- 85-90% RH prevents excessive moisture loss
- >95% RH promotes surface condensation and mold germination
- Condensation on fruit surface creates infection sites for fungal spores

### Air Exchange and Sanitation

**Ventilation strategies:**
- Outside air exchange: 1-2 air changes per day minimum
- Removes ethylene produced by fruit respiration
- Dilutes fungal spores and volatile decay metabolites
- Infiltration through door openings often provides adequate exchange

**Ozone application:**
- Concentration: 0.1-0.3 ppm continuous or 1-3 ppm intermittent (1 hour per day)
- Fungistatic effect reduces surface mold growth
- Material compatibility: Ozone degrades certain rubber compounds in gaskets
- Worker exposure: Ensure dissipation before room entry (0.1 ppm PEL)

**UV-C irradiation:**
- Wavelength: 254 nm germicidal effectiveness
- Surface treatment: Conveyors or in-room fixtures for air sterilization
- Dose: 1000-2000 µW·s/cm² for surface treatment
- Shielding: Prevents direct UV exposure to workers

## Chilling Injury Symptoms and Thresholds

Chilling injury occurs when oranges experience temperatures below critical thresholds for extended periods. Symptoms develop during storage or after transfer to ambient conditions.

### Pitting

**Appearance:** Sunken areas on peel surface, 1-5 mm diameter, brown discoloration

**Mechanism:** Membrane damage in peel oil glands causes localized cell collapse

**Temperature threshold:**
- Valencia oranges: <3°C for >4 weeks
- Navel oranges: <5°C for >2 weeks (early season), <4°C for >4 weeks (late season)

**Prevention:**
- Maintain temperature above variety-specific threshold
- Gradual temperature reduction (1°C per day) improves tolerance
- Conditioning treatment: 15-20°C for 3-7 days before storage

### Rind Breakdown

**Appearance:** Large irregular brown areas on peel, tissue collapse, water-soaked appearance

**Development time:** 2-8 weeks at chilling temperatures, symptoms worsen after removal to ambient conditions

**Contributing factors:**
- Excessive moisture loss combined with chilling stress
- Fruit maturity: Overmature fruit more susceptible
- Storage duration: Extended exposure increases severity

### Stem-End Rots

**Causative organisms:** Diplodia natalensis, Phomopsis citri

**Temperature influence:** Chilling stress weakens natural resistance, allowing latent infections to progress

**Prevention strategies:**
- Proper storage temperature prevents stress-related susceptibility
- Fungicide application (thiabendazole, imazalil) at postharvest
- Careful handling to prevent stem injuries

## Storage Life by Condition

| Condition | Temperature | RH | O2 | CO2 | Storage Life |
|-----------|-------------|----|----|-----|--------------|
| Standard Cold Storage | 5-7°C | 85-90% | 21% | 0.04% | 8-12 weeks |
| Optimized Cold Storage | 6-8°C | 88-92% | 21% | 0.04% | 10-14 weeks |
| CA Storage | 5-7°C | 85-90% | 5-7% | 3-5% | 12-18 weeks |
| Modified CA | 6-8°C | 88-92% | 7-10% | 2-4% | 14-20 weeks |
| Ambient (20°C) | 20°C | 60-70% | 21% | 0.04% | 1-2 weeks |

## HVAC System Design Considerations

Orange storage facilities require refrigeration systems designed for narrow temperature control, high humidity maintenance, and optional CA capability.

**Refrigeration load components:**
- Transmission load through insulated envelope
- Product cooling load from field heat removal
- Respiration heat: 30-50 W/tonne at 5-7°C storage temperature
- Infiltration through door openings
- Internal heat gains (lights, fork trucks, workers)

**Evaporator selection:**
- Unit cooler TD: 2-3°C maximum for humidity control
- Fin spacing: 6-8 mm for reduced frosting in high humidity
- Defrost strategy: Hot gas or electric with cycle scheduling to minimize temperature fluctuation
- Air throw: Low-velocity horizontal discharge across fruit pallets

**Control system requirements:**
- Temperature control: ±0.5°C around setpoint
- Humidity monitoring and control capability
- Data logging for temperature, humidity, O2, CO2 (if CA)
- High/low temperature alarms
- Refrigeration system fault detection
- Door-open alarms and refrigeration delay

**Structural envelope:**
- Insulation R-value: RSI 5.3-7.0 (R-30 to R-40)
- Vapor retarder: Continuous on warm side of insulation
- Thermal bridging minimization through structure
- Pressure relief venting for CA rooms
