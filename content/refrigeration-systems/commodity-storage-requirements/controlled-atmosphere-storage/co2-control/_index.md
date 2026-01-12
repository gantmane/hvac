---
title: "CO2 Control in Controlled Atmosphere Storage"
weight: 2
description: "Technical guide to carbon dioxide management in CA storage including scrubbing methods, respiration-generated CO2, commodity-specific target levels, and monitoring systems for optimal produce preservation."
keywords: "CO2 scrubbing, activated carbon CO2 removal, hydrated lime scrubber, controlled atmosphere storage, respiration CO2, produce storage gas control"
---

## CO2 Generation and Management

Carbon dioxide accumulates in controlled atmosphere storage rooms as a metabolic byproduct of fruit and vegetable respiration. CO2 management is critical because excessive levels cause physiological disorders while insufficient removal compromises storage quality.

### Respiration-Generated CO2

Stored commodities continuously produce CO2 through aerobic respiration. The generation rate depends on:

- **Commodity type**: Apples produce 5-15 mg CO2/kg·h at 32-35°F, while broccoli produces 60-90 mg CO2/kg·h
- **Temperature**: Respiration doubles for every 18°F increase above optimal storage temperature
- **O2 concentration**: Lower oxygen levels (1-3%) reduce respiration rates by 30-50%
- **Maturity stage**: Climacteric fruits show peak CO2 production during ripening
- **Storage duration**: Respiration typically decreases 10-20% over extended storage periods

For a 40,000 cubic foot storage room holding 500,000 lb of apples, expect CO2 generation of 10-20 lb per day at optimal storage conditions.

## CO2 Scrubbing Methods

### Activated Carbon Adsorption

Activated carbon scrubbers physically adsorb CO2 molecules onto high surface area carbon beds.

**Operating Parameters**:
- Adsorption capacity: 5-8% CO2 by weight at storage conditions
- Bed depth: 24-36 inches for commercial installations
- Face velocity: 50-100 fpm through carbon bed
- Regeneration cycle: 4-8 hours adsorption, 2-4 hours regeneration
- Purge gas requirement: Outside air at 2-3 times bed volume

**System Design**:
Carbon scrubbers use pressure swing adsorption (PSA) with two or more beds operating alternately. While one bed adsorbs CO2, the other regenerates by depressurization and purging with fresh air. Bed switching occurs automatically based on CO2 breakthrough monitoring.

**Advantages**: No chemical consumption, regenerable system, simultaneous ethylene removal
**Limitations**: High capital cost, requires compressed air for regeneration, moisture sensitivity

### Hydrated Lime Scrubbers

Hydrated lime (calcium hydroxide) chemically reacts with CO2 to form calcium carbonate and water.

**Chemical Reaction**:
Ca(OH)2 + CO2 → CaCO3 + H2O

**Design Specifications**:
- Lime bed depth: 12-18 inches
- Particle size: 4-8 mesh granular lime
- Air velocity: 30-60 fpm through bed
- CO2 removal capacity: 0.7-0.8 lb CO2 per lb lime (theoretical)
- Actual capacity: 0.4-0.5 lb CO2 per lb lime (accounting for channeling and incomplete reaction)
- Replacement interval: When downstream CO2 rises 1-2% above setpoint

**System Configuration**:
Install lime scrubbers in a vertical tower configuration with distribution plenum at bottom and collection plenum at top. Size the bed to provide 7-14 days of capacity before replacement based on expected CO2 generation rates.

**Advantages**: Low initial cost, simple operation, no power requirement for chemical reaction
**Limitations**: Consumable chemical cost, bed replacement labor, disposal requirements, heat release during reaction

### Water Scrubbing Systems

Water absorbs CO2 through physical dissolution, with absorption rate proportional to CO2 partial pressure differential.

**Absorption Principles**:
- Henry's Law governs CO2 solubility: 1.7 volumes CO2 per volume water at 32°F and atmospheric pressure
- Solubility increases with decreasing temperature
- Solubility decreases with increasing pH as CO2 converts to bicarbonate
- Mass transfer enhanced by high surface area contact (spray towers, packed columns)

**System Design**:
- Packed column height: 15-25 feet
- Packing: 1-2 inch random packing (Raschig rings, Pall rings)
- Liquid-to-gas ratio: 10-20 gallons water per 1000 cfm air
- Water temperature: 32-40°F for maximum CO2 absorption
- Desorption tower: Strips CO2 from water by air stripping or heating

**Advantages**: No chemical consumption if water is recirculated with desorption, handles high CO2 loads
**Limitations**: Complex system with pumps and heat exchangers, requires water treatment, potential for microbial growth

## Target CO2 Levels by Commodity

CO2 tolerance varies significantly among stored products. Optimal levels balance respiration suppression benefits against CO2 injury risk.

| Commodity | Target CO2 Range | Maximum Safe Level | Injury Symptoms |
|-----------|-----------------|-------------------|-----------------|
| Apples (most varieties) | 1-3% | 5% | Brown core, flesh browning |
| Apples (Granny Smith) | 0.5-1% | 2% | High CO2 sensitivity |
| Pears (Bartlett) | 0-1% | 2% | Core breakdown |
| Pears (Anjou, Bosc) | 1-3% | 5% | Better CO2 tolerance |
| Kiwifruit | 3-5% | 7% | Relatively CO2 tolerant |
| Cherries (sweet) | 10-15% | 20% | High CO2 beneficial |
| Broccoli | 5-10% | 15% | Yellowing at excess CO2 |
| Lettuce | 0-2% | 3% | Brown stain above 3% |
| Onions | 0-1% | 2% | Scale discoloration |

### CO2 Injury Mechanisms

Excessive CO2 causes several physiological disorders:

- **Fermentation metabolism**: Anaerobic respiration produces ethanol and acetaldehyde, causing off-flavors
- **Membrane damage**: High CO2 disrupts cell membrane integrity and ion transport
- **Enzyme inhibition**: CO2 interferes with key respiratory enzymes
- **Internal browning**: Phenolic compound oxidation accelerated by CO2 stress
- **Texture loss**: Cell wall degradation from metabolic disruption

## CO2 Monitoring and Control

### Monitoring Systems

Accurate CO2 measurement is essential for controlled atmosphere storage management.

**Infrared (IR) Analyzers**:
- Principle: CO2 absorbs infrared radiation at 4.26 μm wavelength
- Range: 0-25% CO2 with ±0.1% accuracy
- Response time: 30-60 seconds
- Calibration: Monthly using span gas (5-10% CO2)
- Sample conditioning: Filter particulates, remove moisture to -40°F dewpoint

**Thermal Conductivity Analyzers**:
- Principle: CO2 has lower thermal conductivity than air
- Range: 0-20% CO2 with ±0.5% accuracy
- Lower accuracy than IR but more economical
- Susceptible to interference from humidity and temperature

### Control Strategies

**Continuous Scrubbing**:
Maintain constant airflow through scrubber with modulating dampers to control CO2 within ±0.5% of setpoint. Typical control loop:
1. IR analyzer measures room CO2 every 2-5 minutes
2. PID controller modulates scrubber airflow based on CO2 deviation from setpoint
3. Proportional band: 2-4% CO2
4. Integral time: 10-20 minutes

**Intermittent Scrubbing**:
Scrubber operates on/off based on CO2 upper and lower limits. Set differential of 0.5-1% to prevent short-cycling. Example: Scrubber activates at 3.5% CO2, deactivates at 2.5% CO2 for 3% target.

### Safety Considerations

- **High CO2 alarm**: Set at 2-3% above maximum safe level for commodity
- **Personnel entry**: Ventilate room to below 0.5% CO2 before entry (OSHA PEL: 0.5%)
- **Confined space**: CA rooms are permit-required confined spaces due to O2 displacement
- **Emergency ventilation**: Provide rapid air exchange capability (12+ air changes per hour)
- **Oxygen monitoring**: Verify O2 above 19.5% before personnel entry

## System Integration

CO2 control integrates with overall CA storage system design:

- **Scrubber location**: Install downstream of cooling coils to remove condensate before scrubber
- **Airflow coordination**: Balance scrubber flow with room circulation to maintain uniform gas distribution
- **Heat load**: Account for 500-1500 BTU/hr heat generation from lime scrubbers
- **Nitrogen generator interaction**: Coordinate N2 addition with CO2 removal to maintain target O2 levels
- **Ethylene scrubbing**: Combined systems remove both CO2 and ethylene (activated carbon, catalytic oxidation)

Proper CO2 management extends storage life by 30-100% compared to conventional refrigerated storage alone, making it economically justified for high-value commodities stored for extended periods.
