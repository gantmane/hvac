---
title: "Prepared Foods"
weight: 10
---

Prepared foods refrigeration encompasses systems designed for cook-chill operations, ready-to-eat production, and precooked food manufacturing. These facilities require rapid cooling capabilities to minimize bacterial growth during the critical temperature danger zone (135°F to 41°F), along with precise temperature control throughout processing, packaging, and storage operations.

## Cook-Chill Processing

Cook-chill systems produce fully cooked foods that undergo rapid chilling to extend shelf life while maintaining food safety and quality.

### Rapid Chilling Requirements

FDA Food Code mandates cooling from 135°F to 70°F within 2 hours, then from 70°F to 41°F within an additional 4 hours (6 hours total). European standards (HACCP-based) typically require 90 minutes from 160°F to 50°F, then holding at 37°F or below.

**Cooling rate equation for food products:**

ΔT/Δt = h·A·(T_food - T_air) / (m·c_p)

Where:
- ΔT/Δt = temperature change rate (°F/hr or K/hr)
- h = convective heat transfer coefficient (Btu/hr·ft²·°F)
- A = surface area exposed to cooling air (ft²)
- T_food = food temperature (°F)
- T_air = cooling air temperature (°F)
- m = food mass (lb)
- c_p = specific heat of food (Btu/lb·°F)

### Blast Chiller Design

Blast chillers provide high-velocity air (500-1200 fpm) at 28°F to 34°F to achieve rapid heat removal. System capacity must account for:

- Latent heat removal from product moisture evaporation
- Sensible heat removal from product cooling
- Heat generation from respiration (fresh-cut produce additions)
- Packaging material thermal mass
- Pan or tray thermal capacity

Evaporator coil design requires:
- TD (temperature difference) of 8-12°F between refrigerant and air
- Face velocity 400-600 fpm to prevent product dehydration
- Fin spacing 4-6 FPI for reduced frost accumulation
- Stainless steel construction for sanitation compliance

### Tumble Chilling

Rotary drum chillers tumble product in cold air or water spray, achieving uniform cooling for items like pasta, rice, vegetables, and diced proteins. Water-based tumble chilling (32-34°F water) provides cooling rates 10-15 times faster than air due to water's thermal conductivity (0.35 Btu/hr·ft·°F vs 0.015 for air).

Heat removal rate for immersion chilling:

Q = m·c_p·(T_initial - T_final) / t_chill

Typical tumble chiller specifications:

| Parameter | Value | Notes |
|-----------|-------|-------|
| Drum rotation | 4-12 rpm | Prevents product damage |
| Water flow rate | 3-5 gpm per lb product | Maintains temperature |
| Chill water temperature | 32-34°F | Near freezing point |
| Residence time | 8-20 minutes | Product dependent |
| Product load | 40-60% drum volume | Ensures tumbling action |

## Ready-to-Eat (RTE) Processing

Ready-to-eat facilities process foods consumed without additional cooking, requiring stringent environmental controls to prevent Listeria monocytogenes and other pathogen contamination.

### Temperature Zoning

RTE facilities implement temperature-controlled zones:

**Processing zones:**
- Post-lethality (cooking) area: 50-55°F
- Packaging area: 45-50°F
- Cold assembly: 38-42°F
- Finished product holding: 34-38°F

Air handling systems maintain directional airflow from clean to less-clean areas with minimum 15 Pa pressure differential between zones.

### Refrigeration Load Components

| Load Component | Typical Contribution | Calculation Method |
|----------------|---------------------|-------------------|
| Product cooling | 40-55% | m·c_p·ΔT |
| Equipment heat gain | 15-25% | Nameplate ratings |
| Infiltration/ventilation | 10-20% | Q = 1.08·CFM·ΔT + 0.68·CFM·Δω |
| Lighting | 5-8% | Watts × 3.41 Btu/W |
| Personnel | 8-12% | 450-600 Btu/hr per person |
| Packaging materials | 5-10% | m·c_p·ΔT |

### Environmental Control Requirements

HVAC systems for RTE processing must provide:

- Air changes: 15-25 ACH in processing areas
- Filtration: MERV 14 minimum, HEPA for high-risk areas
- Relative humidity: 40-60% to prevent condensation and control microbial growth
- Air velocity: 30-80 fpm in processing zones (prevents drafts on product)
- Coil face velocity: 300-500 fpm (prevents moisture carryover)

Refrigeration systems require hot gas defrost or reverse-cycle defrost to minimize temperature excursions during defrost cycles.

## Precooked Foods Cooling

Precooked items (rotisserie chicken, roasted meats, cooked grains) require cooling protocols that balance food safety with quality retention.

### Shallow Pan Cooling

Products distributed in shallow pans (2-3 inch depth) cool faster than bulk containers due to increased surface area-to-volume ratio. Walk-in coolers for pan cooling require:

- Air temperature: 36-38°F
- Air circulation: 200-400 fpm across pan surfaces
- Evaporator capacity: 1.5-2.0 times steady-state load
- Pan spacing: 1-2 inches vertical separation for airflow

### Ice Paddles and Agitators

Mechanical agitation during cooling increases convective heat transfer coefficient from 5-10 Btu/hr·ft²·°F (static) to 25-50 Btu/hr·ft²·°F (agitated). Ice paddles reduce liquid product temperatures while adding cooling capacity through ice melting (144 Btu/lb latent heat).

### Refrigeration System Design

Systems for precooked food cooling employ:

**Compressor selection:**
- Screw compressors for loads >50 tons
- Scroll compressors for loads 5-50 tons
- Multiple compressors for capacity staging

**Evaporator design:**
- Unit coolers with stainless steel casings
- Coil face area sized for 400-500 fpm
- Drain pans with electric heat (50-100 W/ft²) to prevent freeze-up
- Sloped drains (1/4 inch per foot minimum) for complete drainage

**Refrigerant piping:**
- Hot gas bypass for capacity control below 25% load
- Liquid subcooling 10-15°F to prevent flash gas
- Suction superheat 10-20°F to protect compressors

## Storage Temperature Requirements

| Product Category | Storage Temperature | Relative Humidity | Maximum Storage Time |
|------------------|---------------------|-------------------|---------------------|
| Cook-chill meals | 34-38°F (1-3°C) | 80-85% | 5-7 days |
| Fresh pasta | 32-36°F (0-2°C) | 75-80% | 7-14 days |
| Prepared salads | 32-34°F (0-1°C) | 90-95% | 3-5 days |
| Sliced deli meats | 28-32°F (-2 to 0°C) | 85-90% | 14-21 days |
| Cooked poultry | 34-38°F (1-3°C) | 80-85% | 3-5 days |
| Precooked grains | 36-40°F (2-4°C) | 75-80% | 5-7 days |
| Prepared soups | 34-38°F (1-3°C) | N/A | 7-10 days |

## Thermal Properties of Prepared Foods

Specific heat and thermal conductivity vary with moisture content, composition, and temperature.

| Product Type | Specific Heat (Btu/lb·°F) | Thermal Conductivity (Btu/hr·ft·°F) | Moisture Content (%) |
|--------------|--------------------------|-------------------------------------|---------------------|
| Cooked pasta | 0.75-0.82 | 0.25-0.30 | 60-70 |
| Cooked rice | 0.70-0.78 | 0.22-0.28 | 65-75 |
| Prepared sauces | 0.85-0.92 | 0.30-0.35 | 75-85 |
| Cooked meats | 0.65-0.75 | 0.20-0.25 | 55-70 |
| Mixed casseroles | 0.72-0.80 | 0.24-0.29 | 60-75 |
| Cooked vegetables | 0.88-0.94 | 0.32-0.38 | 80-92 |

Higher moisture content increases specific heat and thermal conductivity, requiring greater refrigeration capacity but enabling faster cooling rates.

## Packaging Considerations

Modified atmosphere packaging (MAP) and vacuum packaging extend shelf life but impose refrigeration requirements:

- MAP products (CO₂/N₂ blends): 32-36°F storage prevents gas permeation through film
- Vacuum-packed items: 34-38°F storage with consistent temperature (±2°F) prevents purge accumulation
- Rigid container packaging: Accounts for 10-20% additional cooling load due to container thermal mass

Packaging line refrigeration maintains 45-55°F ambient to prevent condensation on cold product surfaces while preserving product temperature during filling operations.

## Quality Control Monitoring

Temperature monitoring systems document HACCP compliance:

- Data loggers: 1-minute intervals during chilling
- Core temperature probes: ±0.5°F accuracy
- Alarm systems: Audible/visual alerts at 41°F threshold
- Wireless monitoring: Real-time tracking of batch cooling profiles

Cooling validation studies establish worst-case scenarios (thickest products, maximum load density) to verify system capability.

## Energy Optimization

Prepared foods refrigeration consumes 30-45% of facility energy. Optimization strategies:

- Variable frequency drives on compressors (15-30% energy savings)
- Floating head pressure control (10-15% savings during cool weather)
- Heat recovery for hot water (COP 3.0-4.5 for hot water generation)
- LED lighting in coolers (60-70% lighting energy reduction)
- Strip curtains or air curtains at cooler doors (20-30% infiltration reduction)
- Demand defrost based on actual coil conditions (5-10% savings)

Proper system sizing prevents excessive cycling while maintaining rapid pull-down capability during peak production periods.
