---
title: "Humidity Control Candy Manufacturing"
aliases: ["Humidity Control Candy Manufacturing"]
description: "Advanced HVAC humidity control systems for candy manufacturing facilities including dehumidification strategies, hygroscopic sugar management, and packaging room environmental requirements for confectionery production."
weight: 3
---

## Technical Overview

Humidity control represents the most critical environmental parameter in candy manufacturing. Sugar-based confections exhibit strong hygroscopic properties, absorbing moisture from ambient air when relative humidity exceeds product-specific thresholds. This moisture absorption causes surface stickiness, crystallization defects, texture degradation, and accelerated microbial growth.

HVAC systems for candy production must maintain precise humidity control throughout manufacturing, cooling, and packaging zones. Typical installations require dedicated dehumidification equipment operating independently from temperature control systems to achieve the low dew points necessary for product stability.

## Hygroscopic Nature of Sugar Confections

### Moisture Equilibrium Relationships

Sugar confections exist in moisture equilibrium with surrounding air. Each candy type possesses a critical relative humidity above which it absorbs moisture and below which it releases moisture.

**Equilibrium Relative Humidity by Product Type:**

| Candy Type | ERH at 20°C | Maximum Safe RH | Moisture Absorption Rate |
|------------|-------------|-----------------|--------------------------|
| Hard candy (anhydrous) | 32-35% | 30% | 0.8 g/100g per hour at 50% RH |
| Fudge | 65-70% | 60% | 0.5 g/100g per hour at 75% RH |
| Caramel | 70-75% | 65% | 0.4 g/100g per hour at 80% RH |
| Marshmallow | 75-80% | 70% | 0.3 g/100g per hour at 85% RH |
| Nougat | 60-65% | 55% | 0.6 g/100g per hour at 70% RH |
| Toffee | 55-60% | 50% | 0.7 g/100g per hour at 65% RH |
| Gummy candy | 50-55% | 45% | 0.9 g/100g per hour at 60% RH |

### Crystallization and Graining

Hard candies and clear confections remain amorphous (non-crystalline) when manufactured properly. Exposure to elevated humidity levels causes surface moisture condensation, dissolving surface sugar and creating conditions favorable for crystallization upon re-drying. This process, termed "graining," produces visible white crystalline patches that destroy product appearance and texture.

Critical humidity thresholds for crystallization initiation occur at 40-45% RH for most hard candies at temperatures between 15-25°C. Maintaining space conditions below 35% RH provides adequate safety margin.

### Surface Stickiness and Agglomeration

Moisture absorption creates a saturated sugar solution layer on candy surfaces. This sticky layer causes individual pieces to adhere together during bulk handling, storage, and packaging operations. Surface stickiness becomes problematic when relative humidity exceeds product ERH by more than 5-10 percentage points.

## Target Humidity Levels

### Production Zone Requirements

**Zone-Specific Humidity Specifications:**

| Manufacturing Zone | Temperature | Relative Humidity | Dew Point | Air Changes per Hour |
|--------------------|-------------|-------------------|-----------|---------------------|
| Cooking area | 24-27°C | 40-50% | 12-16°C | 15-20 ACH |
| Cooling tunnel | 15-20°C | 30-40% | -2 to 4°C | 20-30 ACH |
| Enrobing station | 20-22°C | 35-45% | 4-9°C | 12-18 ACH |
| Molding area | 18-22°C | 30-40% | 0-6°C | 15-20 ACH |
| Wrapping/packaging | 18-20°C | 25-35% | -5 to 1°C | 10-15 ACH |
| Storage (finished goods) | 15-18°C | 30-40% | -2 to 3°C | 2-4 ACH |

### Seasonal Variations and Load Management

Summer cooling loads combine high sensible and latent components, requiring dehumidification equipment to remove 3-8 kg moisture per hour per 1000 m² production area. Winter heating loads present challenges maintaining adequate humidity levels while preventing condensation on cold exterior surfaces and equipment.

Design conditions must account for peak summer outdoor conditions of 35°C and 60% RH (dew point 26°C) requiring moisture removal capacity to achieve indoor dew points of -5 to 5°C depending on production zone.

## Dehumidification System Design

### Equipment Selection Criteria

**Refrigeration-Based Dehumidification:**
- Effective for moderate humidity control (40-50% RH)
- Cooling coil dew point: 2-8°C
- Requires reheat to maintain space temperature
- Energy consumption: 0.8-1.2 kW per kg/hr moisture removal
- Capital cost: Moderate
- Maintenance requirements: Standard refrigeration service

**Desiccant Dehumidification:**
- Required for low humidity applications (20-40% RH)
- Achieves supply dew points: -15 to 5°C
- Silica gel or molecular sieve media
- Regeneration energy: 2500-3500 kJ per kg moisture removed
- Energy consumption: 1.5-2.5 kW per kg/hr moisture removal
- Capital cost: High
- Maintenance requirements: Media replacement every 3-5 years

**Hybrid Systems:**
Combine refrigeration pre-dehumidification with desiccant polishing stage. Refrigeration removes bulk moisture (reducing outdoor air from 60% to 40-45% RH), while desiccant stage achieves final low humidity setpoint. This approach optimizes energy consumption by reducing desiccant regeneration energy requirements.

### System Capacity Calculations

**Total Moisture Load Components:**

1. **Outdoor air ventilation load:** W_oa = ṁ_oa × (w_oa - w_sa)
   - ṁ_oa = outdoor air mass flow rate (kg/s)
   - w_oa = outdoor air humidity ratio (kg_w/kg_da)
   - w_sa = supply air humidity ratio (kg_w/kg_da)

2. **Process moisture generation:** 2-5 kg/hr per 100 kg product throughput from cooking operations

3. **Personnel moisture load:** 0.08-0.12 kg/hr per person

4. **Infiltration moisture load:** 0.5-2.0 kg/hr per 100 m² depending on building envelope quality

**Design Example:**
For 500 m² candy production facility:
- Outdoor air requirement: 1500 m³/hr
- Design outdoor conditions: 35°C, 60% RH (w = 0.021 kg/kg)
- Design indoor conditions: 20°C, 35% RH (w = 0.0051 kg/kg)
- Air density: 1.2 kg/m³

Outdoor air moisture load: (1500 m³/hr × 1.2 kg/m³) × (0.021 - 0.0051) = 28.6 kg/hr

Total facility moisture removal capacity required: 35-45 kg/hr including process loads and safety factor.

### Ductwork and Air Distribution

Supply air distribution requires high velocity systems to prevent moisture stratification and maintain uniform conditions. Typical design parameters:
- Supply air velocity: 8-12 m/s in main ducts
- Throw distance: 10-15 m for overhead diffusers
- Temperature differential: 6-10°C supply air below space temperature
- Return air location: low-level returns to capture moisture-laden air near equipment

Ductwork insulation prevents exterior condensation and minimizes heat gain to dehumidified air streams. Specify R-8 to R-12 insulation values (RSI 1.4 to 2.1) with vapor barriers on all ductwork carrying air below space dew point.

## Condensation Prevention

### Cold Surface Management

Any surface temperature below space dew point becomes a condensation site. Critical surfaces requiring attention:
- Refrigerated equipment exteriors
- Chilled water piping
- Cold product contact surfaces
- Exterior walls during winter
- Glazing systems
- Cooling tunnel exteriors

**Condensation Prevention Strategies:**

| Surface Type | Prevention Method | Design Temperature | Insulation Required |
|--------------|-------------------|-------------------|---------------------|
| Chilled water piping | Closed-cell insulation + vapor barrier | 5-10°C | R-6 minimum (RSI 1.0) |
| Cooling tunnel walls | Insulated panels, controlled warm side | 10-15°C | R-20 (RSI 3.5) |
| Windows | Eliminate or use insulated glazing | Match interior dew point | Triple-pane minimum |
| Exterior walls | Continuous insulation, air barrier | Above interior dew point | R-25 minimum (RSI 4.4) |
| Equipment surfaces | Thermal break, local dehumidification | 2°C above space dew point | Equipment-specific |

### Thermal Bridges and Envelope Details

Thermal bridges through building envelope create localized cold spots. Metal structural members, concrete floor slabs, and penetrations require thermal break details. Specify thermally broken door frames, insulated structural supports, and isolated slab perimeters in packaging rooms.

Continuous air barriers prevent moisture-laden outdoor air infiltration. Seal all envelope penetrations, joints, and transitions. Target envelope airtightness: 0.25 L/s/m² at 75 Pa pressure differential.

## Packaging Room Requirements

### Environmental Specifications

Packaging rooms require the most stringent environmental control. Exposed product surfaces remain vulnerable to moisture absorption during wrapping, boxing, and case packing operations.

**Packaging Room Design Parameters:**

| Parameter | Specification | Tolerance | Monitoring Frequency |
|-----------|---------------|-----------|---------------------|
| Temperature | 18-20°C | ±1°C | Continuous |
| Relative humidity | 25-35% | ±3% RH | Continuous |
| Dew point | -5 to 0°C | ±2°C | Continuous |
| Air velocity | 0.15-0.30 m/s | ±0.05 m/s | Quarterly verification |
| Pressurization | +15 to +25 Pa | ±5 Pa | Continuous |
| Particle count | <100,000 class (ISO 8) | Per ISO 14644-1 | Monthly |

### Vestibules and Air Locks

Product and personnel entry points compromise packaging room environmental control. Implement airlocks with interlocked doors preventing simultaneous opening. Maintain airlock pressurization at intermediate level between packaging room and adjacent spaces.

Airlock air handling:
- Dedicated supply air at 125% of room exhaust volume
- HEPA filtration for particulate control
- Continuous operation maintaining positive pressure
- Rapid air exchange: 30-50 ACH within airlock volume

### Equipment Heat Loads

Packaging machinery generates significant sensible heat requiring removal by HVAC system. Equipment heat loads range from 8-15 kW per packaging line depending on equipment type and production speed.

Wrapping machines with heated sealing elements contribute both sensible heat and minor moisture loads. Exhaust hoods over heated elements prevent thermal plumes from disrupting room air distribution patterns.

## Dehumidification Equipment Selection

### Desiccant Rotor Systems

Rotary desiccant dehumidifiers provide optimal performance for candy manufacturing applications requiring sustained operation at 25-40% RH.

**Operational Characteristics:**
- Rotor speed: 8-20 revolutions per hour
- Process air section: 270° of rotor rotation
- Regeneration section: 90° of rotor rotation
- Regeneration temperature: 120-140°C for silica gel
- Pressure drop: 200-400 Pa across rotor
- Moisture removal: 5-12 grams per kg dry air processed

Regeneration air heating represents primary energy consumption. Natural gas-fired regeneration heaters provide lowest operating cost where gas service exists. Electric resistance heating increases operating costs 2-3× compared to gas regeneration.

### Refrigerant Dehumidification Integration

Pre-conditioning outdoor ventilation air with refrigerant dehumidification reduces desiccant system load. Design approach:
1. Refrigerant coil reduces outdoor air from ambient conditions to 40-50% RH
2. Desiccant system polishes air to final 25-35% RH setpoint
3. Combined system achieves 30-40% energy savings versus desiccant-only design

Refrigerant dehumidification coil design parameters:
- Entering air: 35°C, 60% RH
- Leaving air: 12-14°C, >95% RH (saturated)
- Coil face velocity: 2.0-2.5 m/s
- Fin spacing: 8-10 fins per inch
- Rows deep: 6-8 rows for adequate moisture removal

### Energy Recovery Integration

Heat recovery from desiccant regeneration exhaust preheats regeneration air, reducing supplemental heating requirements by 40-60%. Rotary heat exchangers (sensible wheels) or fixed plate heat exchangers recover thermal energy while preventing cross-contamination between exhaust and incoming air streams.

Energy recovery effectiveness: 65-75% for rotary wheels, 50-60% for plate exchangers.

## Monitoring and Control Systems

### Sensor Placement and Accuracy

Humidity sensors require strategic placement avoiding unrepresentative microclimates near doors, equipment, or supply air discharge points. Mount sensors at product height (1.0-1.5 m above floor) in locations with good air circulation.

**Sensor Specifications:**
- Technology: Thin-film capacitive or chilled mirror for accuracy
- Accuracy: ±2% RH over 20-80% RH range, ±3% below 20% RH
- Calibration frequency: Quarterly for critical packaging rooms
- Response time: <30 seconds for 63% of step change
- Operating temperature range: 0-50°C

### Control Sequences

Desiccant dehumidifier modulation:
- Primary control: Space relative humidity or dew point
- Capacity modulation: Regeneration temperature adjustment (90-140°C range)
- Secondary modulation: Process airflow variation via VFD control
- Setpoint dead band: 3-5% RH to prevent hunting
- Response time: 3-8 minutes for 10% capacity change

Refrigerant system integration:
- Lead with refrigerant dehumidification for loads above 50% RH
- Stage desiccant system when refrigerant alone cannot maintain setpoint
- Optimize refrigerant evaporator temperature (8-12°C) for maximum moisture removal without excessive subcooling

### Alarm and Monitoring Parameters

Critical alarm conditions requiring immediate response:
- Space RH exceeding 45% for >15 minutes
- Space dew point exceeding 8°C
- Desiccant regeneration temperature <100°C (incomplete regeneration)
- Supply air dew point >5°C from setpoint
- System airflow <85% of design

Trending parameters for performance optimization:
- Hourly average RH and dew point
- Daily moisture removal quantity
- Regeneration energy consumption per kg moisture removed
- Outdoor air moisture load contribution
- Equipment runtime hours and cycling frequency

## Operational Considerations

### Seasonal Operation Strategies

**Summer Operation:**
Maximum dehumidification load from outdoor air ventilation. Optimize:
- Minimize outdoor air to code-required ventilation rates
- Maximize use of refrigerant dehumidification for energy efficiency
- Monitor for excessive desiccant wheel cycling indicating undersized capacity

**Winter Operation:**
Reduced moisture loads but increased condensation risk. Strategies:
- Maintain space humidity setpoints to prevent over-drying product
- Increase building envelope inspections for condensation indicators
- Verify proper operation of envelope heating systems preventing cold surface condensation

### Maintenance Requirements

**Desiccant Systems:**
- Monthly: Inspect rotor for damage, verify rotation, check drive belt tension
- Quarterly: Clean or replace pre-filters and post-filters
- Semi-annually: Regeneration burner combustion analysis and tune-up
- Annually: Desiccant media inspection for contamination or degradation
- 3-5 years: Desiccant media replacement if performance degradation occurs

**Refrigerant Systems:**
- Monthly: Verify refrigerant pressures and superheat/subcooling
- Quarterly: Clean condenser coils, inspect drain pans for standing water
- Annually: Refrigerant leak testing, compressor oil analysis
- Per manufacturer schedule: Replace filter-driers, inspect electrical connections

### Troubleshooting Common Issues

**Problem: Space humidity above setpoint**
- Verify dehumidification equipment operation and capacity
- Check for excessive infiltration or unexpected moisture sources
- Confirm accurate humidity sensor calibration
- Evaluate if outdoor air load exceeds design conditions

**Problem: Uneven humidity distribution**
- Adjust air distribution patterns and supply locations
- Verify adequate air mixing and circulation
- Identify dead zones requiring improved airflow
- Consider supplemental circulation fans in problem areas

**Problem: Surface condensation on equipment**
- Verify space dew point below equipment surface temperatures
- Improve local dehumidification near cold surfaces
- Add insulation to cold surfaces
- Implement thermal breaks on equipment supports

## System Commissioning

Functional performance testing verifies installed systems achieve design specifications:

1. **Capacity verification:** Operate at peak load conditions, verify space conditions maintained within specifications
2. **Uniformity testing:** Multi-point space humidity measurements confirming distribution uniformity within ±3% RH
3. **Control sequence verification:** Test all operating modes, setpoint changes, and alarm functions
4. **Energy performance:** Measure power consumption and moisture removal rates, calculate specific energy consumption
5. **Documentation:** Record baseline performance data for ongoing performance comparison

## Economic Analysis

Dehumidification system costs represent significant capital and operating expenses requiring life-cycle cost analysis.

**Comparative System Economics (500 m² facility, 35 kg/hr capacity):**

| System Type | Capital Cost | Annual Energy Cost | Maintenance Cost/Year | 10-Year NPV |
|-------------|--------------|-------------------|----------------------|-------------|
| Refrigerant only | $45,000 | $18,000 | $2,500 | $198,000 |
| Desiccant only (gas regen) | $85,000 | $14,000 | $4,000 | $217,000 |
| Desiccant only (electric regen) | $80,000 | $28,000 | $4,000 | $332,000 |
| Hybrid (refrigerant + desiccant) | $95,000 | $12,000 | $5,000 | $207,000 |

Hybrid systems typically offer lowest life-cycle cost despite higher capital investment due to optimized energy consumption. Natural gas-fired desiccant regeneration provides substantial operating cost advantages in facilities with gas service availability.

Product quality improvements and reduced waste from proper humidity control provide additional economic justification beyond direct HVAC system costs. Typical candy manufacturers report 2-5% reduction in product defects attributable to improved environmental control.

