---
title: "Precooked Foods"
aliases: ["Precooked Foods"]
weight: 1
---

Precooked foods refrigeration systems must address the critical transition from cooking temperatures (typically 165-212°F) to safe storage temperatures (≤40°F) while preventing microbial growth in the temperature danger zone (40-140°F). The refrigeration design must achieve rapid cooling rates to minimize time-temperature exposure and maintain product quality through controlled moisture loss and texture preservation.

## Rapid Cooling Requirements

The fundamental cooling requirement for precooked foods follows FDA Food Code guidelines: food must be cooled from 135°F to 70°F within 2 hours and from 70°F to 41°F or below within an additional 4 hours, for a total cooling time of 6 hours maximum.

### Cooling Rate Physics

The cooling rate is governed by Newton's Law of Cooling:

Q = h × A × ΔT<sub>lm</sub>

Where:
- Q = heat transfer rate (Btu/hr)
- h = convective heat transfer coefficient (Btu/hr·ft²·°F)
- A = surface area exposed to cooling medium (ft²)
- ΔT<sub>lm</sub> = logarithmic mean temperature difference (°F)

The convective heat transfer coefficient increases significantly with air velocity:
- Natural convection: h = 1-2 Btu/hr·ft²·°F
- Forced convection at 200 fpm: h = 3-5 Btu/hr·ft²·°F
- Forced convection at 500 fpm: h = 6-10 Btu/hr·ft²·°F
- Blast chilling at 1000+ fpm: h = 12-20 Btu/hr·ft²·°F

### Blast Chilling Systems

Blast chillers provide high-velocity airflow (800-1500 fpm) at temperatures of 28-34°F to achieve rapid cooling. The refrigeration load includes:

1. **Sensible heat removal from food**: Q<sub>sensible</sub> = m × c<sub>p</sub> × ΔT
2. **Latent heat from moisture evaporation**: Q<sub>latent</sub> = m<sub>water</sub> × h<sub>fg</sub> (typically 2-5% weight loss)
3. **Container thermal mass**: Q<sub>container</sub> = m<sub>c</sub> × c<sub>p,c</sub> × ΔT
4. **Infiltration and equipment heat gain**

Blast chiller evaporator design requires:
- Coil face velocity: 600-800 fpm
- Fin spacing: 4-6 fins per inch (wider than standard to minimize frost buildup)
- Evaporator TD: 8-12°F (tighter than storage systems)
- Refrigerant: R-404A, R-407C, or R-448A for low-temperature duty

## Precooked Food Storage Parameters

Storage conditions vary by product type, moisture content, and intended shelf life.

| Food Product | Storage Temp (°F) | Relative Humidity (%) | Max Storage (Days) | Critical Control Points |
|--------------|-------------------|----------------------|-------------------|------------------------|
| Roasted meats (sliced) | 32-36 | 85-90 | 3-5 | Surface moisture control, oxygen barrier |
| Fried chicken | 34-38 | 70-75 | 2-3 | Coating crispness, moisture migration |
| Pasta dishes (with sauce) | 33-38 | 80-85 | 5-7 | pH control (≥4.6), sauce separation |
| Casseroles | 33-38 | 80-85 | 3-5 | Multi-component stability, moisture balance |
| Precooked seafood | 30-34 | 90-95 | 2-3 | Oxidation control, fishy odor development |
| Rice dishes | 34-38 | 75-80 | 3-5 | Starch retrogradation, texture firmness |
| Precooked vegetables | 32-36 | 85-90 | 5-7 | Color retention, vitamin degradation |
| Breaded/battered items | 34-38 | 65-70 | 2-4 | Coating integrity, sogginess prevention |

## Thermal Load Calculations

The total refrigeration load for precooked foods processing includes multiple simultaneous components.

### Product Load Components

**Initial cooling from cooking temperature:**

For a batch of 500 lb roasted chicken pieces cooled from 165°F to 38°F in a blast chiller:

Q<sub>product</sub> = m × c<sub>p</sub> × ΔT = 500 lb × 0.82 Btu/lb·°F × (165-38)°F = 52,070 Btu

**Moisture evaporation (assuming 3% weight loss):**

Q<sub>evap</sub> = 500 lb × 0.03 × 1060 Btu/lb = 15,900 Btu

**Total heat removal:** 52,070 + 15,900 = 67,970 Btu

**Required refrigeration capacity** (for 2-hour cooling cycle):
67,970 Btu ÷ 2 hr = 33,985 Btu/hr = 2.8 tons

Add safety factor (1.3-1.5×) for equipment losses: 3.7-4.2 tons per 500 lb batch.

## Packaging Considerations for Refrigeration

Packaging directly impacts refrigeration requirements and cooling efficiency.

### Heat Transfer Through Packaging

The thermal resistance of packaging materials affects cooling time:

R = thickness ÷ k

Common packaging thermal conductivities:
- Aluminum foil pans: k = 120 Btu·in/hr·ft²·°F (minimal resistance)
- Polypropylene containers: k = 1.0 Btu·in/hr·ft²·°F
- Expanded polystyrene: k = 0.25 Btu·in/hr·ft²·°F (high resistance)
- Cardboard: k = 0.5-0.7 Btu·in/hr·ft²·°F

**Container depth effects:**
Maximum recommended product depth for rapid cooling:
- Blast chilling: 2-3 inches
- Tumble chilling: 4-6 inches (with agitation)
- Static air cooling: 1-2 inches

Deeper products create internal thermal resistance and extended cooling times due to the low thermal conductivity of food (k = 0.3-0.5 Btu·in/hr·ft²·°F).

## Reheating Considerations

The refrigeration system design must account for the complete thermal cycle including reheating requirements.

### Temperature Cycling Effects

**Thermal stress on product structure:**
- Ice crystal formation during cooling: 28-32°F zone creates maximum crystals
- Reheating induces moisture redistribution
- Multiple freeze-thaw cycles degrade texture exponentially

**Reheating targets:**
- FDA minimum internal temperature: 165°F for 15 seconds
- Holding temperature after reheating: 135-140°F minimum

### Modified Atmosphere Packaging (MAP)

MAP systems interact with refrigeration requirements:

**Gas composition effects on shelf life:**
| Product Type | O₂ (%) | CO₂ (%) | N₂ (%) | Shelf Life Extension | Temperature Sensitivity |
|--------------|---------|---------|---------|---------------------|------------------------|
| Roasted meats | 0-1 | 20-30 | 70-80 | 2-3× baseline | ±2°F critical |
| Pasta dishes | 0 | 30-40 | 60-70 | 1.5-2× baseline | ±3°F acceptable |
| Fried items | 21 (air) | 0 | 79 | 1× (breathable) | ±4°F acceptable |
| Seafood items | 0 | 40-60 | 40-60 | 3-4× baseline | ±1°F critical |

MAP packages require precise temperature control because gas solubility increases at lower temperatures, potentially creating package collapse at 30-32°F.

## Cold Chain Distribution

Precooked foods require unbroken refrigeration from production through retail or foodservice.

**Distribution temperature tolerances:**
- Transport: 36-40°F (allows for door openings, thermal mass)
- Retail display: 34-38°F (higher turnover, shorter exposure)
- Foodservice holding: 33-38°F (immediate use within days)

**Temperature excursion limits:**
Maximum allowable temperature excursion without product rejection:
- Duration ≤30 minutes: up to 50°F acceptable
- Duration 30-60 minutes: up to 45°F acceptable
- Duration >60 minutes: product must not exceed 41°F

These limits assume product started at ≤38°F with adequate thermal mass.

## System Design Specifications

### Walk-in Cooler Design for Precooked Foods

**Envelope specifications:**
- Insulation: 4-inch polyurethane panels (R-28 to R-32)
- Floor insulation: 6-inch (R-42) with heated slab perimeter
- Vapor retarder: 10-mil polyethylene or equivalent (0.02 perm rating)

**Refrigeration unit sizing:**
- Design ambient: 75-80°F
- Box temperature: 35-38°F
- Design TD (evaporator): 10-12°F
- Coil defrost: electric or hot gas, 4-6 cycles per day
- Evaporator airflow: 100-150 CFM per ton

**Air distribution:**
- Air changes per hour: 20-30 ACH
- Maximum air velocity over product: 200-300 fpm (prevent surface drying)
- Supply air directed along ceiling, return at floor level

### Blast Chiller Specifications

**Performance requirements:**
- Cooling capacity: 90-135°F temperature pull-down
- Airflow: 500-800 CFM per cart or rack position
- Evaporator temperature: 15-25°F
- Cycle control: Time-based or core-probe temperature-based
- Defrost: Automatic hot gas or reverse cycle every 2-4 hours

**Typical unit capacities:**
- Roll-in blast chiller: 150-300 lb product per cycle
- Reach-in blast chiller: 50-100 lb product per cycle
- Continuous tunnel chiller: 500-2000 lb/hr throughput

These systems typically operate on R-404A or R-448A refrigerants with multiple compressor staging (2-4 stages) to handle varying loads from pull-down to holding.

## Quality Indicators and Monitoring

Temperature monitoring must capture both time and temperature to validate cooling compliance.

**Critical monitoring points:**
1. Product core temperature (thickest part, geometric center)
2. Blast chiller discharge air temperature
3. Storage cooler ambient temperature
4. Product surface temperature (indicates moisture loss rate)

**Data logging requirements:**
- Recording interval: 5-15 minutes during cooling
- Recording interval: 30-60 minutes during storage
- Alarm setpoints: >40°F for >30 minutes cumulative
- HACCP documentation: full cooling curve for validation
