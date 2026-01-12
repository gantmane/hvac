---
title: "Commodity Storage Requirements"
description: "Technical specifications for commodity storage environments including temperature, humidity, air circulation, and ethylene control requirements for optimizing storage life across frozen, refrigerated, and controlled atmosphere applications."
weight: 12
---

Commodity storage requirements establish the environmental parameters necessary to maintain product quality, minimize deterioration, and maximize storage life. These specifications vary significantly by commodity type, physiological characteristics, and desired storage duration. ASHRAE Refrigeration Handbook Chapter 19 provides comprehensive storage condition tables for perishable commodities.

## Storage Environment Classification

Storage environments are classified by temperature range and atmospheric control:

**Frozen Storage**: Maintains product temperatures at -18°C (0°F) or below. This temperature arrests most biological activity and enzymatic reactions. Commercial frozen storage typically operates at -23°C to -29°C (-10°F to -20°F) to ensure product quality throughout distribution cycles. Lower temperatures reduce sublimation rates and extend storage life but increase energy consumption.

**Refrigerated Storage**: Operates above freezing, typically 0°C to 13°C (32°F to 55°F) depending on commodity. This range slows but does not stop metabolic processes. Precise temperature control is critical because temperature fluctuations accelerate respiration rates and moisture loss.

**Controlled Atmosphere (CA) Storage**: Combines refrigerated temperatures with modified oxygen and carbon dioxide concentrations. Typical CA conditions reduce O₂ from atmospheric 21% to 1-5% and elevate CO₂ to 1-5%. This atmosphere modification dramatically slows respiration and ethylene production in climacteric fruits.

**Modified Atmosphere (MA) Storage**: Similar to CA but with less precise control, often achieved through packaging films rather than room-scale atmosphere management.

## Temperature Requirements by Commodity Type

Storage temperature represents the most critical control parameter. The relationship between temperature and respiration rate follows Q₁₀ principles, where respiration rate approximately doubles for each 10°C increase.

| Commodity Category | Temperature Range | Typical Duration |
|-------------------|-------------------|------------------|
| Frozen meat products | -23°C to -18°C (-10°F to 0°F) | 6-12 months |
| Frozen vegetables | -18°C to -12°C (0°F to 10°F) | 8-12 months |
| Fresh meat (beef) | -1.5°C to 2°C (29°F to 36°F) | 1-6 weeks |
| Fresh poultry | -2°C to 0°C (28°F to 32°F) | 5-7 days |
| Dairy products | 1°C to 4°C (34°F to 40°F) | Variable |
| Apples (CA) | -1°C to 4°C (30°F to 39°F) | 2-10 months |
| Citrus fruits | 0°C to 15°C (32°F to 59°F) | 1-6 months |
| Tropical fruits | 10°C to 13°C (50°F to 55°F) | 1-4 weeks |
| Leafy vegetables | 0°C to 2°C (32°F to 36°F) | 10-21 days |
| Root vegetables | 0°C to 4°C (32°F to 40°F) | 1-8 months |

Temperature uniformity throughout the storage space is essential. Spatial variations should not exceed ±0.5°C for sensitive commodities. This requires proper air distribution design and adequate refrigeration capacity to handle both steady-state loads and pulldown requirements.

## Relative Humidity Control

Relative humidity (RH) directly affects moisture transfer between commodities and the surrounding air. The vapor pressure difference drives this transfer, calculated from psychrometric relationships and the commodity's water activity.

**High Humidity Storage (90-95% RH)**: Required for most fresh fruits and vegetables to minimize transpiration and wilting. Leafy greens, berries, and other high-surface-area commodities are particularly susceptible to moisture loss.

**Moderate Humidity Storage (80-90% RH)**: Appropriate for commodities with lower transpiration rates or protective skins, such as citrus fruits and certain root vegetables.

**Low Humidity Storage (65-75% RH)**: Used for cured products like onions, garlic, and winter squash where lower humidity prevents mold growth while product moisture content is already reduced.

Humidity control presents competing requirements with refrigeration coil operation. Evaporator coil temperature depression below space dewpoint causes moisture removal. Maintaining high RH requires:

- Minimal temperature differential between coil and space air (2-4°C)
- Oversized coil surface area to reduce required ΔT
- Frequent defrost cycles to prevent excessive ice buildup
- Humidification systems to replace removed moisture

The moisture removal rate equals the latent cooling load divided by the latent heat of vaporization (2501 kJ/kg at 0°C). For a 1000 kW cooling load with 30% latent fraction, moisture removal approximates 0.12 kg/s or 430 kg/hr.

## Air Circulation Requirements

Air circulation serves multiple functions: heat transfer from commodities, temperature uniformity maintenance, and humidity distribution. However, excessive air velocity causes moisture loss and wind burn.

**Velocity Requirements**:
- Bulk storage areas: 0.25-0.5 m/s around product
- Packaged goods: 0.5-1.0 m/s through rack aisles
- Surface of sensitive produce: <0.25 m/s to minimize transpiration

Air changes per hour vary by application:
- Frozen storage: 2-4 air changes per hour
- Fresh produce storage: 20-40 air changes per hour
- CA rooms: 1-2 air changes per hour (after establishment)

Distribution system design must prevent short-circuiting while ensuring air reaches all product zones. Computational fluid dynamics (CFD) modeling helps optimize layouts for complex geometries.

## Ethylene Sensitivity and Management

Ethylene (C₂H₄) functions as a plant hormone triggering ripening and senescence. Climacteric fruits produce significant ethylene during ripening, while non-climacteric fruits produce minimal amounts.

**Ethylene Production Rates** at optimal storage temperature:

| Commodity | Production Rate | Sensitivity |
|-----------|----------------|-------------|
| Apples | 10-100 μL/kg·h | Medium |
| Bananas (ripe) | 50-200 μL/kg·h | High |
| Tomatoes (mature green) | 0.5-5 μL/kg·h | Medium |
| Lettuce | <0.1 μL/kg·h | High |
| Cucumbers | 0.1-1 μL/kg·h | High |

Ethylene concentrations as low as 0.1 ppm can accelerate ripening in sensitive commodities. Management strategies include:

1. **Separation**: Store ethylene producers separate from sensitive commodities
2. **Ventilation**: Fresh air introduction dilutes ethylene concentration
3. **Scrubbing**: Catalytic converters or potassium permanganate filters oxidize ethylene
4. **CA Storage**: Low O₂ atmospheres reduce ethylene production rates

For mixed storage facilities, continuous ethylene monitoring with action thresholds (typically 1 ppm) enables intervention before quality loss occurs.

## Storage Life Optimization

Storage life depends on initial product quality, temperature management, humidity control, and atmospheric composition. The relationship follows:

Storage Life = f(Temperature, RH, [O₂], [CO₂], [C₂H₄], Initial Quality)

**Temperature Management**: The most influential factor. Each 1°C increase above optimal temperature typically reduces storage life by 10-25%. Rapid cooling immediately after harvest preserves quality by minimizing field heat and respiration.

**Humidity Optimization**: Maintaining RH within ±5% of optimal prevents moisture loss while avoiding condensation. Condensation promotes microbial growth and accelerates decay.

**Atmosphere Modification**: CA storage extends apple storage from 3-4 months to 8-10 months by reducing respiration rate by 50-70%. The specific atmosphere must be tailored to variety; Granny Smith apples tolerate 1% O₂, while Fuji requires 2-3% O₂ to prevent fermentation.

**Load Management**: Proper stacking, packaging orientation, and pallet arrangement ensure adequate air circulation. Blocking >30% of surface area significantly reduces heat transfer coefficient and extends cooling time.

## Respiration Rates and Heat Generation

Respiration represents the primary metabolic process in stored fruits and vegetables, consuming carbohydrates and producing heat, CO₂, and water vapor. The respiration heat load directly impacts refrigeration capacity requirements and must be calculated for proper system sizing.

Respiration rate (RR) follows the temperature-dependent relationship:

RR(T₂) = RR(T₁) × Q₁₀^((T₂-T₁)/10)

where Q₁₀ typically ranges from 2.0 to 3.5 for most commodities. This exponential relationship underscores the critical importance of rapid cooling and precise temperature control.

**Respiration Heat Generation at Optimal Storage Temperature**:

| Commodity | Temperature | Respiration Heat | Classification |
|-----------|-------------|-----------------|----------------|
| Asparagus | 0°C | 180-250 mW/kg | Very high |
| Broccoli | 0°C | 90-120 mW/kg | Very high |
| Sweet corn | 0°C | 120-180 mW/kg | Very high |
| Strawberries | 0°C | 40-60 mW/kg | High |
| Lettuce | 0°C | 30-45 mW/kg | High |
| Apples | 0°C | 5-15 mW/kg | Moderate |
| Potatoes | 4°C | 8-12 mW/kg | Moderate |
| Onions (cured) | 0°C | 3-5 mW/kg | Low |
| Cabbage | 0°C | 8-12 mW/kg | Low |

For a storage room containing 50,000 kg of broccoli at 0°C with average respiration of 100 mW/kg, the respiration load equals:

Q_resp = 50,000 kg × 0.1 W/kg = 5,000 W = 5.0 kW

This represents a continuous sensible load that must be removed to maintain storage temperature. High-respiration commodities can contribute 20-40% of total refrigeration load in fully loaded rooms.

## Comprehensive Commodity Storage Tables

The following tables provide detailed storage specifications based on ASHRAE Refrigeration Handbook Chapter 21 (formerly Chapter 25 in older editions):

### Fruits - Storage Specifications

| Commodity | Temperature | RH | Storage Life | Freezing Point | Notes |
|-----------|-------------|-----|--------------|----------------|-------|
| Apples | -1 to 4°C | 90-95% | 2-10 months | -1.5°C | CA extends to 12 months |
| Apricots | -0.5 to 0°C | 90-95% | 1-3 weeks | -1.0°C | High ethylene production |
| Avocados | 4.5-13°C | 85-90% | 2-8 weeks | -0.4°C | Chilling sensitive |
| Bananas | 13-15°C | 90-95% | 1-4 weeks | -0.8°C | Chilling injury <10°C |
| Blueberries | -0.5 to 0°C | 90-95% | 2-4 weeks | -1.1°C | Rapid cooling critical |
| Cherries | -1 to 0°C | 90-95% | 2-3 weeks | -1.8°C | MA packaging beneficial |
| Grapes | -1 to 0°C | 90-95% | 1-6 months | -2.0°C | SO₂ pads control decay |
| Lemons | 10-14°C | 85-90% | 1-6 months | -1.4°C | Ethylene sensitive |
| Oranges | 3-9°C | 85-90% | 3-12 weeks | -0.8°C | Variety dependent |
| Peaches | -0.5 to 0°C | 90-95% | 2-4 weeks | -0.9°C | High ethylene production |
| Pears | -1.5 to 0°C | 90-95% | 2-7 months | -1.6°C | CA storage recommended |
| Strawberries | 0°C | 90-95% | 5-7 days | -0.8°C | Precooling essential |

### Vegetables - Storage Specifications

| Commodity | Temperature | RH | Storage Life | Freezing Point | Notes |
|-----------|-------------|-----|--------------|----------------|-------|
| Artichokes | 0°C | 95-100% | 2-3 weeks | -1.2°C | Iced storage common |
| Asparagus | 0-2°C | 95-100% | 2-3 weeks | -0.6°C | Vertical storage upright |
| Beans (snap) | 4-7°C | 95% | 7-10 days | -0.7°C | Chilling sensitive |
| Beets | 0°C | 98-100% | 4-6 months | -1.8°C | Top removal essential |
| Broccoli | 0°C | 95-100% | 10-14 days | -0.6°C | Rapid yellowing above 5°C |
| Brussels sprouts | 0°C | 95-100% | 3-5 weeks | -0.8°C | High respiration rate |
| Cabbage | 0°C | 98-100% | 3-6 months | -0.9°C | Long storage capability |
| Carrots | 0°C | 98-100% | 7-9 months | -1.4°C | Topped, hydrocooled |
| Cauliflower | 0°C | 95-98% | 3-4 weeks | -0.8°C | Light causes discoloration |
| Celery | 0°C | 98-100% | 2-3 months | -0.5°C | Wilts easily, high RH critical |
| Corn (sweet) | 0°C | 95-98% | 5-8 days | -0.6°C | Sugar converts to starch rapidly |
| Cucumbers | 10-13°C | 95% | 10-14 days | -0.5°C | Chilling injury <7°C |
| Lettuce | 0°C | 98-100% | 2-3 weeks | -0.2°C | Ethylene sensitive |
| Mushrooms | 0°C | 95% | 3-7 days | -0.9°C | Browning sensitive |
| Onions (dry) | 0°C | 65-70% | 1-8 months | -0.9°C | Cured, sprouting control |
| Peppers (bell) | 7-10°C | 90-95% | 2-3 weeks | -0.7°C | Chilling sensitive |
| Potatoes | 4-10°C | 90-95% | 5-10 months | -0.6°C | <4°C causes sweetening |
| Spinach | 0°C | 95-100% | 10-14 days | -0.3°C | Rapid deterioration |
| Tomatoes (mature green) | 12-15°C | 90-95% | 1-3 weeks | -0.6°C | Ripens at 18-21°C |
| Tomatoes (ripe) | 8-10°C | 90-95% | 4-7 days | -0.6°C | Chilling injury <7°C |

### Protein Products - Storage Specifications

| Commodity | Temperature | RH | Storage Life | Notes |
|-----------|-------------|-----|--------------|-------|
| Beef (fresh) | -1.5 to 2°C | 88-92% | 1-6 weeks | Vacuum packaging extends life |
| Beef (frozen) | -23°C | 90-95% | 6-12 months | Oxidation limits storage |
| Pork (fresh) | -1.5 to 2°C | 85-90% | 3-7 days | Higher fat, shorter life |
| Pork (frozen) | -23°C | 90-95% | 4-8 months | Fat oxidation issue |
| Lamb (fresh) | -1 to 1°C | 85-90% | 5-15 days | Rapid aging beneficial |
| Poultry (fresh) | -2 to 0°C | 90-95% | 5-7 days | Surface bacteria growth critical |
| Poultry (frozen) | -18°C | 90-95% | 6-9 months | Glazing reduces dehydration |
| Fish (fresh) | -1 to 0°C | 95-100% | 5-15 days | Iced storage preferred |
| Fish (frozen) | -23°C | 95-100% | 3-12 months | Fatty fish shorter storage |

## Commodity Compatibility Groupings

Commodity compatibility determines which products can be stored together without quality deterioration. Incompatibilities arise from ethylene sensitivity, odor absorption, temperature requirements, and humidity needs.

### Storage Compatibility Groups

**Group 1 - Low Temperature, High Humidity, Ethylene Producers**:
- Apples (most varieties)
- Pears
- Stone fruits (peaches, plums, apricots)
- Melons (cantaloupe, honeydew)

These commodities should be stored separately from ethylene-sensitive products. CA storage beneficial for extended life.

**Group 2 - Low Temperature, High Humidity, Ethylene Sensitive**:
- Leafy greens (lettuce, spinach, kale)
- Broccoli, cauliflower, Brussels sprouts
- Cabbage
- Celery
- Berries (strawberries, blueberries, raspberries)

Requires ethylene-free environment. Cannot be stored with Group 1 without ethylene scrubbing.

**Group 3 - Low Temperature, Moderate Humidity**:
- Citrus fruits
- Root vegetables (topped)
- Grapes

Compatible with high-humidity commodities if humidity can be maintained above 85%.

**Group 4 - Moderate Temperature, High Humidity, Chilling Sensitive**:
- Tomatoes (mature green and ripe)
- Cucumbers
- Peppers (bell and hot)
- Eggplant
- Beans (snap)
- Squash (summer types)

Incompatible with low-temperature storage. Chilling injury occurs below 7-10°C causing pitting, discoloration, and accelerated decay.

**Group 5 - Moderate Temperature, Low Humidity, Cured Products**:
- Onions (dry)
- Garlic
- Winter squash
- Pumpkins
- Sweet potatoes (cured)

Requires lower humidity (65-75%) to prevent mold growth. Incompatible with high-humidity requirements of most fresh produce.

**Group 6 - Cold Temperature, Odor Sensitive**:
- Dairy products
- Eggs
- Butter

Must be isolated from strong-odor commodities like onions, cabbage, and fish due to odor absorption through packaging.

**Group 7 - Tropical Fruits, High Temperature**:
- Bananas
- Pineapples
- Mangoes
- Papayas

Severe chilling injury below 10-13°C. Incompatible with standard refrigerated storage.

### Incompatibility Matrix

| Primary Commodity | Incompatible With | Reason |
|------------------|-------------------|---------|
| Apples | Lettuce, celery, carrots | Ethylene damage |
| Bananas | All refrigerated products | Temperature requirement |
| Onions | Apples, pears, dairy | Odor transfer |
| Cabbage | Apples, pears, grapes | Odor transfer |
| Potatoes | Apples, onions | Ethylene causes sprouting |
| Tomatoes | Apples, stone fruits | Ethylene accelerates ripening |

## Design Application Guidelines

Applying commodity storage requirements to refrigeration system design requires integration of multiple parameters:

**Load Calculation Protocol**:
1. Determine commodity-specific respiration heat at design temperature
2. Calculate product cooling load from initial temperature to storage temperature
3. Add transmission, infiltration, and equipment loads
4. Apply safety factor (10-20%) for temperature recovery after loading
5. Verify capacity adequate for warmest anticipated outdoor conditions

**Control System Requirements**:
- Temperature control: ±0.5°C accuracy for sensitive commodities
- Humidity control: ±5% RH for high-value products
- Defrost scheduling: Based on coil pressure drop or time interval
- Alarm systems: Temperature excursion, compressor failure, power loss
- Data logging: Continuous recording for quality assurance and FSMA compliance

**Air Distribution Design**:
- Ensure minimum air velocity at product surfaces (0.15-0.25 m/s)
- Prevent dead zones through CFD modeling or empirical layout
- Size ductwork for low pressure drop (typically <25 Pa)
- Configure discharge and return for uniform temperature distribution

## ASHRAE References

ASHRAE Refrigeration Handbook provides detailed storage requirements:

- **Chapter 21**: Fruits, Vegetables, and Other Products - comprehensive storage condition tables, respiration rates, and compatibility information
- **Chapter 19**: Thermal Properties of Foods - specific heat, enthalpy, and heat of respiration data for load calculations
- **Chapter 26**: Meat Products - temperature, humidity, and storage duration specifications
- **Chapter 27**: Poultry Products - handling and storage requirements
- **Chapter 28**: Dairy Products - temperature sensitivity and shelf life data
- **Chapter 29**: Fishery Products - icing requirements and frozen storage conditions

These references include commodity-specific data for calculating refrigeration loads, optimizing storage conditions, and predicting storage life under various environmental conditions. Chapter 21 contains the primary storage condition tables referenced throughout the industry for specification development and facility design.

## Design Considerations

Refrigeration system design for commodity storage must account for:

**Load Components**:
- Transmission load through insulated envelope
- Product load during pulldown
- Respiration heat (0.1-10 W/kg depending on commodity and temperature)
- Infiltration from door openings and air leakage
- Internal loads from lighting and material handling equipment

**Temperature Control**: PID control with ±0.5°C accuracy for sensitive commodities. Dead band should not exceed 1°C to prevent temperature cycling.

**Defrost Strategy**: Time-initiated, temperature-terminated defrost cycles sized to prevent excessive ice accumulation while minimizing product temperature rise. High-humidity applications may require defrost every 4-6 hours.

**Monitoring Systems**: Continuous temperature logging with alarm notification for excursions. Multiple sensor locations verify spatial uniformity. Humidity sensors enable closed-loop RH control.

Proper application of commodity storage requirements ensures product quality preservation, minimizes shrinkage losses, and optimizes economic return throughout the cold chain.
