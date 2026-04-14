---
title: "Ice Cooling"
aliases: ["Ice Cooling"]
description: "Direct contact ice cooling methods for rapid vegetable precooling, including top icing, liquid ice, and slurry ice systems with heat transfer calculations and equipment specifications"
weight: 5
---

## Overview

Ice cooling represents the most direct form of contact cooling for vegetable precooling, utilizing the latent heat of fusion of ice (334 kJ/kg or 144 BTU/lb) in addition to sensible cooling from cold meltwater. This method provides rapid heat removal rates due to intimate contact between ice and product, maintaining high humidity (near 100% RH) throughout the cooling process. Ice cooling is particularly effective for leafy vegetables, broccoli, and products transported in open containers where moisture loss prevention is critical.

The thermodynamic advantage of ice cooling stems from the phase change process, where ice absorbs substantial energy during melting at constant temperature (0°C or 32°F), providing consistent cooling performance independent of ambient conditions during transportation.

## Ice Cooling Methods

### Top Icing

Top icing involves placing crushed or flake ice directly on top of packed vegetables in shipping containers. Ice is distributed uniformly across the product surface, allowing meltwater to trickle down through the container while absorbing heat.

**Cooling Mechanism:**
- Initial cooling from direct ice contact with upper product layers
- Continuous cooling as cold meltwater (0-2°C) percolates through product mass
- Evaporative cooling from high humidity environment
- Extended cooling duration during transportation (24-72 hours)

**Ice Distribution Requirements:**

| Container Type | Ice Mass Ratio | Distribution Pattern | Cooling Depth |
|----------------|----------------|----------------------|---------------|
| Waxed fiberboard carton | 0.3-0.5 kg ice/kg product | Uniform top layer 5-8 cm | 15-25 cm effective |
| Plastic crate (vented) | 0.4-0.6 kg ice/kg product | Top and intermediate layers | Full container depth |
| Wooden crate | 0.5-0.7 kg ice/kg product | Top layer with sidewall vents | Variable penetration |
| Bulk bin | 0.6-0.8 kg ice/kg product | Multiple layers at 30 cm intervals | >60 cm depth |

**Operational Characteristics:**
- Ice application rate: 200-400 kg/hour per application station
- Ice particle size: 1-3 cm crushed ice or flake ice
- Container fill factor: 0.85-0.90 to allow ice volume without overflow
- Drainage requirement: 5-10 L/min per packing line

### Liquid Ice (Ice Slurry)

Liquid ice consists of fine ice crystals (0.1-1.0 mm diameter) suspended in chilled water at concentrations of 20-50% ice by mass. This pumpable mixture provides rapid cooling through complete surface contact with irregular-shaped vegetables.

**Physical Properties:**

| Ice Concentration | Density (kg/m³) | Viscosity (mPa·s) | Heat Capacity (kJ/kg·K) | Latent Heat Available (kJ/kg) |
|-------------------|-----------------|-------------------|-------------------------|-------------------------------|
| 20% ice | 970 | 3-5 | 3.5 | 67 |
| 30% ice | 950 | 5-8 | 3.2 | 100 |
| 40% ice | 930 | 8-15 | 2.9 | 134 |
| 50% ice | 910 | 15-30 | 2.6 | 167 |

**Application Methods:**
1. **Immersion tanks:** Vegetables submerged in liquid ice for 2-10 minutes
2. **Spray application:** Liquid ice sprayed over moving conveyor belts
3. **Tumble cooling:** Product agitated in liquid ice bath
4. **Recirculation systems:** Continuous liquid ice flow through packed containers

**Heat Transfer Performance:**

The convective heat transfer coefficient for liquid ice contact ranges from 200-600 W/m²·K, compared to 50-150 W/m²·K for forced air cooling.

Cooling time calculation:

```
t = (ρ × V × c_p × ln[(T_i - T_f)/(T_p - T_f)]) / (h × A)

Where:
t = cooling time (s)
ρ = product density (kg/m³)
V = product volume (m³)
c_p = specific heat of product (kJ/kg·K)
T_i = initial product temperature (°C)
T_f = final product temperature (°C)
T_p = liquid ice temperature (°C, typically 0°C)
h = heat transfer coefficient (W/m²·K)
A = product surface area (m²)
```

**System Components:**
- Ice generator: Scraped surface heat exchanger or flake ice maker
- Slurry tank: 500-5000 L capacity with agitation
- Recirculation pump: 50-200 L/min, 2-5 bar pressure
- Ice concentration control: Automatic ice addition based on temperature sensors
- Filtration: 1-5 mm screen to remove product debris

### Slurry Ice Systems

Slurry ice (also termed fluid ice or FluidiceTM) represents advanced ice cooling technology producing microscopic ice crystals (0.01-0.3 mm) in a highly fluid mixture with 30-60% ice content. Unlike liquid ice, slurry ice remains pumpable at higher ice concentrations due to smaller crystal size.

**Generation Technologies:**

1. **Vacuum method:** Water freezing under reduced pressure (610 Pa at 0°C)
   - Ice production rate: 500-2000 kg/hour
   - Power consumption: 85-95 kW per ton of ice
   - Crystal size: 0.1-0.5 mm

2. **Scraped surface method:** Mechanical scraping of ice from refrigerated cylinder walls
   - Ice production rate: 200-1500 kg/hour
   - Power consumption: 90-110 kW per ton of ice
   - Crystal size: 0.05-0.3 mm

3. **Direct contact method:** Refrigerant injection into water
   - Ice production rate: 1000-5000 kg/hour
   - Power consumption: 75-90 kW per ton of ice
   - Crystal size: 0.01-0.1 mm (finest crystals)

**Advantages Over Conventional Ice:**
- Higher heat transfer rates: 30-50% faster cooling
- Better product coverage: Penetrates into crevices and flower heads
- Reduced mechanical damage: Soft, spherical crystals
- Pumpability: Flows through standard piping (50-150 mm diameter)
- Storage stability: Remains fluid for 24-48 hours with minimal agitation

## Heat Transfer Principles

### Conductive Heat Transfer

Direct ice-to-product contact provides conductive heat transfer:

```
q = k × A × (T_product - T_ice) / δ

Where:
q = heat transfer rate (W)
k = thermal conductivity at interface (W/m·K)
   Ice-water interface: 0.5-0.8 W/m·K
   Ice-vegetable interface: 0.3-0.6 W/m·K
A = contact area (m²)
T_product = product surface temperature (°C)
T_ice = ice temperature (0°C)
δ = thermal boundary layer thickness (m, typically 0.5-2 mm)
```

### Convective Cooling from Meltwater

As ice melts, cold water (0-1°C) flows over product surfaces:

```
q = h_c × A × (T_surface - T_water)

Where:
h_c = convective heat transfer coefficient (W/m²·K)
      Laminar flow (meltwater trickle): 50-150 W/m²·K
      Turbulent flow (sprayed liquid ice): 200-600 W/m²·K
      Forced circulation: 400-1000 W/m²·K
```

### Latent Heat Contribution

Ice melting absorbs substantial energy:

```
Q_latent = m_ice × h_fg

Where:
Q_latent = total cooling capacity from ice melting (kJ)
m_ice = mass of ice (kg)
h_fg = latent heat of fusion = 334 kJ/kg
```

### Combined Cooling Equation

Total heat removal from vegetables:

```
Q_total = m_product × c_p × (T_initial - T_final) = m_ice × [h_fg + c_p,water × (T_ambient - 0)]

Where:
Q_total = total heat to be removed (kJ)
m_product = mass of vegetables (kg)
c_p = specific heat of vegetables (kJ/kg·K), typically 3.6-4.0 kJ/kg·K
T_initial = harvest temperature (°C), typically 25-35°C
T_final = target storage temperature (°C), typically 0-4°C
m_ice = ice mass required (kg)
c_p,water = specific heat of water = 4.18 kJ/kg·K
T_ambient = ambient temperature during transportation (°C)
```

### Ice Requirement Calculation Example

Calculate ice needed to cool 1000 kg of broccoli from 28°C to 2°C with 10°C ambient temperature during 24-hour transport:

**Product cooling requirement:**
```
Q_product = 1000 kg × 3.9 kJ/kg·K × (28 - 2)°C = 101,400 kJ
```

**Cooling available from 1 kg of ice:**
```
Q_ice = 1 kg × [334 kJ/kg + 4.18 kJ/kg·K × (10 - 0)°C] = 334 + 41.8 = 375.8 kJ/kg
```

**Ice mass required:**
```
m_ice = 101,400 kJ / 375.8 kJ/kg = 270 kg
```

**Ice-to-product ratio:**
```
Ratio = 270 kg / 1000 kg = 0.27 kg ice per kg product
```

Add 20-30% safety factor for container heat gain and inefficiencies:
```
m_ice,actual = 270 × 1.25 = 338 kg (0.34 kg ice/kg product)
```

## Ice Production Requirements

### Ice Generation Capacity

**Sizing Calculation:**

```
Ice capacity (kg/hour) = (Peak harvest rate × Ice ratio × Safety factor) / Operating hours

For 10,000 kg/hour harvest rate with 0.4 kg ice/kg product:
Ice capacity = (10,000 × 0.4 × 1.2) / 1.0 = 4,800 kg/hour
```

### Ice Maker Types for Vegetable Precooling

| Ice Type | Production Rate | Ice Temperature | Crystal Size | Best Application | Power (kW/ton ice) |
|----------|----------------|-----------------|--------------|------------------|-------------------|
| Flake ice | 500-10,000 kg/hr | -5 to 0°C | 2-5 mm thin flakes | Top icing, general purpose | 90-110 |
| Crushed ice | 1,000-5,000 kg/hr | -2 to 0°C | 10-30 mm pieces | Container icing | 95-115 |
| Tube ice (crushed) | 500-3,000 kg/hr | -3 to -1°C | 15-40 mm pieces | Heavy-duty icing | 100-120 |
| Liquid ice | 200-2,000 kg/hr | 0°C | 0.1-1 mm suspended | Immersion, spray cooling | 85-100 |
| Slurry ice | 500-5,000 kg/hr | 0 to -0.5°C | 0.01-0.3 mm fluid | Rapid cooling, pumping | 75-95 |

### Refrigeration Load Calculation

Total refrigeration capacity required:

```
Q_refrigeration = Q_ice + Q_water + Q_ambient + Q_equipment

Q_ice = m_ice × h_fg / t_production
Q_water = m_ice × c_p,water × (T_water,in - 0°C) / t_production
Q_ambient = U × A_tank × (T_ambient - T_ice)
Q_equipment = Motor heat + Friction losses (typically 5-10% of total)

Where:
t_production = ice production time (hours)
U = overall heat transfer coefficient of ice storage tank (W/m²·K)
A_tank = surface area of tank (m²)
```

**Example:** 2000 kg/hour ice production from 15°C water:

```
Q_ice = (2000 kg/hr × 334 kJ/kg) / 3600 s/hr = 186 kW
Q_water = (2000 kg/hr × 4.18 kJ/kg·K × 15°C) / 3600 s/hr = 35 kW
Q_ambient = 0.3 W/m²·K × 50 m² × 20°C = 0.3 kW
Q_equipment = (186 + 35) × 0.08 = 18 kW

Q_total = 186 + 35 + 0.3 + 18 = 239 kW (68 tons refrigeration)
```

Compressor power (assuming COP = 3.0):
```
Power = 239 kW / 3.0 = 80 kW
```

## Water Quality Requirements

### Chemical Parameters

| Parameter | Specification | Reason | Test Frequency |
|-----------|---------------|---------|----------------|
| Total dissolved solids (TDS) | <500 mg/L | Prevents scaling in ice maker | Weekly |
| Hardness (CaCO₃) | <100 mg/L | Reduces mineral deposits | Weekly |
| pH | 6.5-8.5 | Prevents corrosion and scaling | Daily |
| Chlorides | <250 mg/L | Prevents stainless steel corrosion | Monthly |
| Iron | <0.3 mg/L | Prevents discoloration | Monthly |
| Manganese | <0.05 mg/L | Prevents staining | Monthly |
| Silica (SiO₂) | <50 mg/L | Prevents hard scale formation | Monthly |

### Microbiological Quality

**Food Safety Standards:**
- Total coliform: <1 CFU/100 mL
- E. coli: Not detectable in 100 mL
- Total plate count: <500 CFU/mL
- Listeria monocytogenes: Not detectable in 100 mL
- Salmonella: Not detectable in 100 mL

**Treatment Methods:**
1. **Filtration:** 1-5 μm cartridge filters or sand filtration
2. **UV disinfection:** 30-40 mJ/cm² dosage at end of season
3. **Chlorination:** 0.5-1.0 mg/L free chlorine residual
4. **Ozonation:** 0.1-0.5 mg/L ozone for continuous disinfection

### Water Recycling Systems

Meltwater recovery reduces freshwater consumption:

**System Components:**
1. Collection sump: 1000-5000 L capacity
2. Coarse filtration: 5-10 mm screen to remove plant debris
3. Fine filtration: 1-5 μm cartridge or multimedia filters
4. Disinfection: UV or ozone treatment
5. Chilled storage: 2-4°C holding tank before ice maker

**Recovery Efficiency:**
- Typical recovery: 70-85% of meltwater
- Water savings: 0.3-0.5 L per kg of product cooled
- Payback period: 2-4 years for large operations (>5000 kg/hour)

## Equipment Specifications

### Top Icing Systems

**Automatic Icing Machines:**

| Specification | Small Scale | Medium Scale | Large Scale |
|---------------|-------------|--------------|-------------|
| Ice application rate | 100-500 kg/hr | 500-2,000 kg/hr | 2,000-8,000 kg/hr |
| Container throughput | 10-30 boxes/min | 30-80 boxes/min | 80-200 boxes/min |
| Ice storage capacity | 500-1,500 kg | 1,500-5,000 kg | 5,000-20,000 kg |
| Power requirement | 5-15 kW | 15-40 kW | 40-120 kW |
| Floor space | 3-6 m² | 6-15 m² | 15-40 m² |
| Control system | Manual/timer | PLC with HMI | Fully automated with vision |

**Key Features:**
- Variable speed conveyor: 5-30 m/min adjustable
- Adjustable ice gate: Controls ice volume per container
- Weight-based dispensing: ±5% accuracy
- Ice level sensors: Automatic refill control
- Photoelectric sensors: Container detection and positioning

### Liquid Ice Systems

**Immersion Tank Configuration:**

```
Tank volume calculation:
V_tank = (m_product / ρ_product) × (1 / fill_factor) + V_liquid_ice

Where:
V_tank = tank volume (m³)
m_product = batch mass (kg)
ρ_product = product density in water (kg/m³), typically 900-1050 kg/m³
fill_factor = 0.6-0.8 (allows product movement)
V_liquid_ice = liquid ice volume (m³), typically 1.5-2.5 × product volume
```

**Example Tank Sizing:**

For 500 kg broccoli batch (ρ = 950 kg/m³):
```
V_product = 500 kg / 950 kg/m³ = 0.53 m³
V_tank = 0.53 m³ / 0.7 + (0.53 × 2.0) = 0.76 + 1.06 = 1.82 m³

Use 2.0 m³ tank (dimensions: 1.2 m × 1.2 m × 1.4 m deep)
```

**Circulation System:**
- Pump flow rate: 3-6 tank volumes per hour
- Pump head: 1-3 m (10-30 kPa)
- Pipe velocity: 1.0-2.5 m/s
- Nozzle configuration: Multiple bottom inlet nozzles for upward flow

### Slurry Ice Spray Systems

**Conveyor Cooling Line:**

| Component | Specification | Function |
|-----------|---------------|----------|
| Belt conveyor | 0.6-1.2 m wide × 3-10 m long | Product transport at 5-15 m/min |
| Spray manifold | 6-12 nozzles per meter width | Uniform slurry ice distribution |
| Slurry pump | 50-200 L/min at 2-4 bar | Slurry ice delivery |
| Collection pan | Full conveyor length, 150 mm deep | Meltwater and slurry recovery |
| Return tank | 500-2000 L with agitation | Slurry ice storage and mixing |

**Nozzle Selection:**
- Nozzle type: Full cone or flat fan spray
- Flow rate: 5-15 L/min per nozzle
- Spray angle: 60-90 degrees
- Material: Stainless steel 316L for corrosion resistance
- Spacing: 150-250 mm centers for uniform coverage

## Applications by Vegetable Type

### Leafy Vegetables

**Optimal for ice cooling due to:**
- High surface area to volume ratio
- High respiration rate requiring rapid cooling
- Tolerance to direct ice contact
- Moisture loss sensitivity (99-100% RH required)

| Vegetable | Ice Method | Ice Ratio | Cooling Time | Target Temp | Shelf Life Extension |
|-----------|------------|-----------|--------------|-------------|---------------------|
| Lettuce (iceberg) | Top icing | 0.3-0.4 | 1-2 hours | 0-1°C | 2-3 weeks |
| Lettuce (leaf) | Liquid ice immersion | 0.4-0.5 | 15-30 min | 0-1°C | 10-14 days |
| Spinach | Top icing or liquid ice | 0.4-0.6 | 20-40 min | 0-1°C | 10-14 days |
| Kale | Top icing | 0.3-0.5 | 30-60 min | 0-2°C | 14-21 days |
| Cabbage | Top icing (transit) | 0.2-0.3 | 2-4 hours | 0-1°C | 3-6 months |
| Swiss chard | Liquid ice | 0.4-0.5 | 20-30 min | 0-1°C | 10-14 days |

**Special Considerations:**
- Remove excess surface water before packaging to prevent ice adhesion
- Use perforated liners to allow meltwater drainage
- Avoid heavy ice loads that crush delicate leaves (maximum 5 cm ice depth)

### Cruciferous Vegetables

**Broccoli (Primary Application):**

Broccoli represents the ideal candidate for ice cooling:

- Complex floret structure benefits from ice penetration
- High respiration rate (75-150 mg CO₂/kg·hr at 5°C)
- Rapid yellowing without proper cooling (6-12 hours at 20°C)
- 4-6 hour cooling window after harvest for quality retention

**Ice Cooling Protocol:**
1. Harvest in early morning (product temperature <25°C)
2. Field packing into waxed cartons with crushed ice layer
3. Transport to cooling facility within 2 hours
4. Top icing application: 0.5-0.7 kg ice per kg broccoli
5. Target pulp temperature: 1-2°C within 1 hour
6. Reapply ice as needed during transportation

**Other Cruciferous Vegetables:**

| Vegetable | Ice Applicability | Ice Ratio | Notes |
|-----------|-------------------|-----------|-------|
| Cauliflower | Excellent | 0.4-0.6 | Similar to broccoli, benefits from ice in florets |
| Brussels sprouts | Good | 0.3-0.4 | Small size allows rapid cooling |
| Bok choy | Excellent | 0.4-0.5 | Leafy structure, high moisture content |

### Root Vegetables (Limited Application)

Root vegetables generally unsuitable for ice cooling:

**Limitations:**
- Low surface area to volume ratio reduces cooling rate
- Skin damage from ice contact promotes decay
- Lower respiration rates allow slower cooling methods
- Extended storage life reduces urgency of rapid cooling

**Exceptions:**
- Radishes (bunched): Top icing acceptable with 0.2-0.3 ice ratio for leaf protection
- Carrots (topped): Brief liquid ice immersion (2-5 minutes) for washing and cooling combined

### Specialty Applications

**Fresh-cut Vegetables:**

Slurry ice immersion provides simultaneous washing and cooling:

- Contact time: 1-3 minutes
- Temperature reduction: 15-20°C in single pass
- Microbial reduction: 1-2 log reduction when combined with chlorinated water (50-100 ppm)
- Applications: Cut lettuce, spinach, coleslaw mixes

**Herbs:**

Highly sensitive to moisture and mechanical damage:

- Use liquid ice spray (not immersion) to prevent bruising
- Ice ratio: 0.3-0.4 kg/kg
- Cooling time: 10-20 minutes
- Package immediately after surface water evaporation

## Cooling Rate Calculations

### Half-Cooling Time Method

Half-cooling time (t₁/₂) represents the time required to reduce the temperature difference between product and cooling medium by 50%:

```
t₁/₂ = (ρ × V × c_p × ln(2)) / (h × A)

For spherical products:
t₁/₂ = (ρ × r × c_p × ln(2)) / (3 × h)

Where:
r = product radius (m)
```

**Ice Cooling Half-Cooling Times:**

| Product | Dimension | Air Cooling | Ice Cooling | Time Reduction |
|---------|-----------|-------------|-------------|----------------|
| Broccoli head | 12 cm diameter | 45-60 min | 15-20 min | 65-70% |
| Lettuce head | 15 cm diameter | 60-90 min | 20-30 min | 65-70% |
| Spinach leaves | 0.3 mm thick | 10-15 min | 3-5 min | 70-75% |
| Cabbage head | 18 cm diameter | 120-180 min | 40-60 min | 65-70% |

### Temperature Prediction Model

Temperature at time t:

```
T(t) = T_ice + (T_initial - T_ice) × exp(-t / τ)

Where:
τ = thermal time constant = (ρ × V × c_p) / (h × A)

For ice cooling with meltwater flow:
h = 300-800 W/m²·K (significantly higher than air cooling at 10-50 W/m²·K)
```

**Example:** Broccoli cooling from 28°C to 2°C with ice

```
Given:
T_initial = 28°C
T_ice = 0°C
T_final = 2°C
h = 500 W/m²·K (liquid ice spray)
ρ = 920 kg/m³
c_p = 3900 J/kg·K
V = 0.0008 m³ (12 cm diameter head)
A = 0.0113 m² (surface area)

τ = (920 × 0.0008 × 3900) / (500 × 0.0113) = 509 seconds = 8.5 minutes

Solve for time to reach 2°C:
2 = 0 + (28 - 0) × exp(-t / 509)
t = -509 × ln(2/28) = -509 × ln(0.071) = -509 × (-2.64) = 1344 seconds = 22.4 minutes
```

## Energy Efficiency

### Coefficient of Performance (COP)

Ice-making systems typically operate at lower COP than conventional refrigeration due to the requirement for sub-zero evaporator temperatures:

```
COP = Q_cooling / W_input

Typical values:
Flake ice maker: COP = 2.5-3.2
Liquid ice system: COP = 2.8-3.5
Slurry ice system: COP = 3.0-3.8
Direct expansion air cooling: COP = 3.5-4.5
```

However, ice cooling provides advantages that offset lower instantaneous COP:

1. **Thermal storage capability:** Ice production during off-peak hours at lower ambient temperatures
2. **Transportation cooling:** Eliminates need for refrigerated trucks
3. **Load shifting:** Production during low electricity cost periods
4. **Humidity control:** Eliminates need for separate humidification

### Energy Consumption Comparison

**Example:** Cool 10,000 kg broccoli from 28°C to 2°C

**Ice Cooling Method:**
```
Ice required: 10,000 kg × 0.5 = 5,000 kg ice
Refrigeration load: 5,000 kg × 334 kJ/kg = 1,670,000 kJ
Compressor energy (COP = 3.0): 1,670,000 / 3.0 = 557,000 kJ = 155 kWh
Ice application: 2 kWh
Total: 157 kWh
```

**Forced Air Cooling Method:**
```
Product cooling: 10,000 kg × 3.9 kJ/kg·K × 26°C = 1,014,000 kJ
Container cooling: 500 kg × 1.5 kJ/kg·K × 26°C = 19,500 kJ
Respiration heat (2 hours): 10,000 kg × 0.08 kJ/kg·hr × 2 hr = 1,600 kJ
Total cooling: 1,035,100 kJ
Compressor energy (COP = 3.5): 1,035,100 / 3.5 = 296,000 kJ = 82 kWh
Fan energy: 15 kW × 2 hours = 30 kWh
Total: 112 kWh
```

**Refrigerated Transport (24 hours):**
```
Product respiration: 10,000 kg × 0.04 kJ/kg·hr × 24 hr = 9,600 kJ
Container heat gain: 100 W/m² × 20 m² × 24 hr × 3.6 = 172,800 kJ
Total cooling: 182,400 kJ
Truck refrigeration (COP = 2.0): 182,400 / 2.0 = 91,200 kJ = 25 kWh
```

**Total Energy Comparison:**

- Ice cooling + unrefrigerated transport: 157 kWh
- Forced air + refrigerated transport: 112 + 25 = 137 kWh

Ice cooling uses 15% more energy but eliminates refrigerated transport requirement, reducing capital cost and providing operational flexibility.

### Optimization Strategies

1. **Ice production scheduling:** Generate ice during nighttime hours (lower ambient temperature, lower electricity rates)
2. **Ice storage:** Insulated bins hold ice for 24-48 hours with <10% melting loss
3. **Meltwater recovery:** Recycling reduces water heating load by 60-75%
4. **Variable ice application:** Adjust ice ratio based on product temperature and ambient conditions
5. **Hybrid systems:** Combine ice cooling with forced air for optimal efficiency

## ASHRAE Guidelines

### Design Standards

**ASHRAE Handbook - Refrigeration (Chapter 28: Methods of Precooling)** provides recommendations for ice cooling systems:

**Ice Application Rates:**
- Leafy vegetables: 0.25-0.50 kg ice per kg product
- Broccoli and cauliflower: 0.40-0.70 kg ice per kg product
- General vegetables: 0.20-0.40 kg ice per kg product

**Cooling Time Targets:**
- 7/8 cooling (87.5% temperature reduction): 15-45 minutes
- Storage temperature achieved: Within 1 hour of icing
- Maximum field-to-cooled interval: 2-4 hours depending on commodity

### Refrigeration System Design

**Evaporator Temperature Selection:**

For ice production, evaporator temperature must be significantly below 0°C:

| Ice Type | Evaporator Temp | Compressor Discharge Temp | Expansion Valve Type |
|----------|----------------|---------------------------|---------------------|
| Flake ice | -15 to -10°C | 50-70°C | Thermostatic (TXV) |
| Crushed ice | -12 to -8°C | 45-65°C | Thermostatic (TXV) |
| Liquid ice | -8 to -5°C | 40-60°C | Electronic (EEV) |
| Slurry ice | -5 to -2°C | 35-55°C | Electronic (EEV) |

**Refrigerant Selection:**

Based on ASHRAE Standard 34-2019 safety classifications and environmental considerations:

| Refrigerant | Application | GWP | ODP | Safety Class | Notes |
|-------------|-------------|-----|-----|--------------|-------|
| R-404A (phasing out) | Existing systems | 3922 | 0 | A1 | High GWP, being replaced |
| R-448A | Retrofit replacement | 1387 | 0 | A1 | Drop-in for R-404A |
| R-449A | New installations | 1397 | 0 | A1 | Optimized for ice making |
| R-744 (CO₂) | Transcritical systems | 1 | 0 | A1 | Low GWP, high pressure |
| Ammonia (R-717) | Industrial scale | 0 | 0 | B2L | Efficient, requires safety measures |

### Water Quality Standards

ASHRAE aligns with FDA Food Code requirements:

- Ice must be made from potable water meeting EPA National Primary Drinking Water Regulations
- Ice contact surfaces: Food-grade stainless steel (304 or 316L)
- Regular sanitization: Weekly cleaning with approved food-safe sanitizers
- Microbial testing: Monthly testing during harvest season

### Safety Requirements

**Personal Protective Equipment (PPE):**
- Insulated gloves for ice handling
- Slip-resistant footwear for wet surfaces
- Eye protection when working with ice spray systems

**Machinery Safeguarding:**
- Emergency stops on all conveyors and ice application equipment
- Guarding on rotating ice augers and conveyors
- Lockout/tagout procedures for maintenance

**Food Safety:**
- HACCP plan integration for ice cooling operations
- Critical control point: Ice temperature and microbial quality
- Monitoring frequency: Continuous temperature, daily microbial testing during peak season

---

**References:**
- ASHRAE Handbook - Refrigeration, Chapter 28: Methods of Precooling
- ASHRAE Standard 15-2019: Safety Standard for Refrigeration Systems
- USDA Agricultural Handbook 66: The Commercial Storage of Fruits, Vegetables, and Florist and Nursery Stocks
- Brosnan, T., & Sun, D. W. (2001). Precooling techniques and applications for horticultural products. International Journal of Refrigeration, 24(2), 154-170.
