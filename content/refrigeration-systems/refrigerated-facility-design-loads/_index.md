---
title: "Refrigerated Facility Design Loads"
description: "Comprehensive refrigeration load calculation methodology for cold storage facilities including transmission loads, infiltration, product loads, equipment heat gains, safety factors, and system sizing criteria per ASHRAE standards"
weight: 14
---

Accurate refrigeration load calculations form the foundation for proper refrigerated facility design. The total refrigeration load consists of multiple components that must be systematically evaluated to determine equipment capacity requirements.

## Load Calculation Methodology Overview

Refrigeration load calculations follow a systematic approach that accounts for all heat gains to the refrigerated space. The total design load represents the sum of simultaneous peak loads from all sources.

**Total Refrigeration Load:**

Q_total = Q_trans + Q_inf + Q_prod + Q_int + Q_equip + Q_lights + Q_people + Q_misc

Where:
- Q_trans = Transmission heat gain through envelope (Btu/hr or W)
- Q_inf = Infiltration air load (Btu/hr or W)
- Q_prod = Product cooling load (Btu/hr or W)
- Q_int = Internal equipment heat gain (Btu/hr or W)
- Q_equip = Process equipment loads (Btu/hr or W)
- Q_lights = Lighting heat gain (Btu/hr or W)
- Q_people = Occupancy load (Btu/hr or W)
- Q_misc = Safety factor and miscellaneous loads (Btu/hr or W)

## Component Loads Summary

### Transmission Loads

Transmission loads result from heat transfer through walls, floors, ceilings, and structural elements. This load operates continuously and represents a significant portion of total refrigeration requirements.

**Transmission Load Equation:**

Q_trans = U × A × ΔT

Where:
- U = Overall heat transfer coefficient (Btu/hr·ft²·°F or W/m²·K)
- A = Surface area (ft² or m²)
- ΔT = Temperature difference across envelope (°F or K)

**Typical U-Values for Refrigerated Facilities:**

| Construction Type | Insulation | U-Value (Btu/hr·ft²·°F) | U-Value (W/m²·K) |
|-------------------|------------|------------------------|------------------|
| Walls, 4" polyurethane | R-28 | 0.036 | 0.20 |
| Walls, 6" polyurethane | R-42 | 0.024 | 0.14 |
| Ceiling, 6" polyurethane | R-42 | 0.024 | 0.14 |
| Ceiling, 8" polyurethane | R-56 | 0.018 | 0.10 |
| Floor, unheated slab | R-20 | 0.050 | 0.28 |
| Floor, heated slab | R-15 | 0.067 | 0.38 |

For below-grade surfaces and slabs on grade, use modified calculation methods accounting for ground temperature and heat flow paths per ASHRAE Handbook—Refrigeration Chapter 24.

### Infiltration Loads

Infiltration represents outdoor air entering the refrigerated space through door openings, structural leaks, and pressure differentials. This load includes both sensible and latent heat components.

**Infiltration Load Components:**

Q_inf = Q_sens + Q_lat

**Sensible Load:**

Q_sens = ṁ_air × c_p × (T_out - T_in)

**Latent Load:**

Q_lat = ṁ_air × h_fg × (W_out - W_in)

Where:
- ṁ_air = Mass flow rate of infiltrating air (lb/hr or kg/hr)
- c_p = Specific heat of air (0.24 Btu/lb·°F or 1.006 kJ/kg·K)
- h_fg = Latent heat of water vaporization (~1060 Btu/lb or 2465 kJ/kg)
- W = Humidity ratio (lb_water/lb_air or kg_water/kg_air)

**Door Infiltration—Doorway Flow Factor Method:**

Q_door = D_f × A_door × ρ_m × Δh × F_m

Where:
- D_f = Doorway flow factor (from ASHRAE tables)
- A_door = Door opening area (ft² or m²)
- ρ_m = Density of air mixture (lb/ft³ or kg/m³)
- Δh = Enthalpy difference (Btu/lb or kJ/kg)
- F_m = Door usage factor (0.4-1.0 depending on traffic)

**Typical Door Infiltration Loads:**

| Door Size | Traffic Level | Temp Differential | Infiltration Load |
|-----------|---------------|-------------------|-------------------|
| 4' × 8' (1.2m × 2.4m) | Light (10 openings/hr) | 70°F to 35°F (21°C to 2°C) | 2,500 Btu/hr (730 W) |
| 4' × 8' (1.2m × 2.4m) | Medium (25 openings/hr) | 70°F to 35°F (21°C to 2°C) | 5,000 Btu/hr (1,465 W) |
| 4' × 8' (1.2m × 2.4m) | Heavy (50 openings/hr) | 70°F to 35°F (21°C to 2°C) | 8,500 Btu/hr (2,490 W) |
| 10' × 10' dock door | Medium (15 openings/hr) | 70°F to 0°F (21°C to -18°C) | 35,000 Btu/hr (10,250 W) |

For freezer applications below 0°F (-18°C), vestibules or air curtains significantly reduce infiltration loads.

### Product Cooling Loads

Product loads consist of heat removal required to cool incoming product from receiving temperature to storage temperature, plus heat of respiration for fresh produce.

**Product Cooling Load:**

Q_prod = ṁ_prod × c_p × ΔT / t_cool

Where:
- ṁ_prod = Product mass (lb or kg)
- c_p = Specific heat of product (Btu/lb·°F or kJ/kg·K)
- ΔT = Temperature reduction required (°F or K)
- t_cool = Cooling time period (hr)

**For freezing applications, add latent heat:**

Q_freeze = ṁ_prod × h_f / t_freeze

Where h_f = latent heat of fusion (typically 100-144 Btu/lb or 233-335 kJ/kg for water content)

**Specific Heat Values for Common Products:**

| Product | Temp Range | c_p Above Freezing (Btu/lb·°F) | c_p Below Freezing (Btu/lb·°F) |
|---------|------------|-------------------------------|-------------------------------|
| Beef | 28-40°F | 0.77 | 0.40 |
| Poultry | 28-40°F | 0.80 | 0.40 |
| Fish | 28-40°F | 0.82 | 0.41 |
| Apples | 30-40°F | 0.87 | 0.45 |
| Lettuce | 32-40°F | 0.96 | 0.48 |
| Ice cream | Below 0°F | — | 0.50 |
| Frozen foods | Below 0°F | — | 0.45 |

**Respiration Heat for Fresh Produce:**

Living fruits and vegetables generate metabolic heat that contributes to refrigeration load. Respiration rates vary significantly with temperature and must be included for produce storage.

| Product | Temperature | Respiration Heat (Btu/ton·day) | Respiration Heat (W/1000 kg) |
|---------|-------------|--------------------------------|------------------------------|
| Apples | 32°F (0°C) | 800-1,200 | 380-570 |
| Apples | 40°F (4°C) | 1,600-2,400 | 760-1,140 |
| Lettuce | 32°F (0°C) | 3,500-4,500 | 1,665-2,140 |
| Tomatoes (mature green) | 55°F (13°C) | 2,000-3,000 | 950-1,425 |
| Potatoes | 40°F (4°C) | 1,200-1,800 | 570-855 |

Reference: ASHRAE Handbook—Refrigeration Chapter 19 for comprehensive produce data.

### Internal Equipment Loads

Equipment operating within the refrigerated space generates heat that must be removed by the refrigeration system.

**Electric Motors (Inside Refrigerated Space):**

Q_motor = P_motor × 3.413 / η_motor

Where:
- P_motor = Motor nameplate power (kW)
- η_motor = Motor efficiency (typically 0.85-0.95)
- 3.413 = Conversion factor (Btu/hr per Watt)

**Fork Lifts and Material Handling Equipment:**

| Equipment Type | Operating Load (Btu/hr) | Standby Load (Btu/hr) |
|----------------|------------------------|----------------------|
| Electric forklift, 4,000 lb capacity | 12,000-15,000 | 2,000-3,000 |
| Propane forklift, 4,000 lb capacity | Not recommended (combustion products) | — |
| Electric pallet jack | 3,000-5,000 | 500-1,000 |
| Conveyor systems, per hp | 3,400-4,250 | — |

**Usage Factor:**

Apply a usage factor (F_use) based on actual operating hours:

Q_equip,avg = Q_equip,rated × F_use

Typical usage factors range from 0.3-0.7 depending on facility operations.

### Lighting Loads

Lighting heat gain depends on lamp type, wattage, and operating schedule.

**Lighting Load:**

Q_lights = P_lights × 3.413 × F_use × F_bal

Where:
- P_lights = Total lighting power (W)
- F_use = Usage factor (fraction of time lights operate)
- F_bal = Ballast factor (1.0 for LED, 1.15-1.20 for fluorescent)

**Typical Lighting Power Densities:**

| Space Type | Power Density (W/ft²) | Power Density (W/m²) |
|------------|----------------------|---------------------|
| Cooler storage | 0.5-0.8 | 5-9 |
| Freezer storage | 0.4-0.6 | 4-6 |
| Processing areas | 1.0-1.5 | 11-16 |
| Loading docks | 0.8-1.2 | 9-13 |

LED lighting reduces both energy consumption and heat gain compared to traditional high-intensity discharge (HID) lamps.

### Occupancy Loads

Personnel working in refrigerated spaces generate sensible and latent heat. Load magnitude depends on activity level and protective clothing.

**Heat Gain from People:**

Q_people = N × (q_sens + q_lat)

Where:
- N = Number of occupants
- q_sens = Sensible heat gain per person (Btu/hr or W)
- q_lat = Latent heat gain per person (Btu/hr or W)

**Heat Gain Values:**

| Activity Level | Space Temperature | Sensible (Btu/hr) | Latent (Btu/hr) | Total (Btu/hr) |
|----------------|-------------------|-------------------|-----------------|----------------|
| Light work | 50°F (10°C) | 375 | 175 | 550 |
| Moderate work | 50°F (10°C) | 475 | 525 | 1,000 |
| Heavy work | 50°F (10°C) | 580 | 920 | 1,500 |
| Light work | 0°F (-18°C) | 450 | 50 | 500 |
| Moderate work | 0°F (-18°C) | 550 | 150 | 700 |

At lower temperatures, latent heat gain decreases significantly as water vapor condenses on clothing and protective gear before entering the space.

## Safety Factors

Safety factors account for uncertainties in load calculations, future expansion, and unusual operating conditions. Apply safety factors to the sum of all calculated loads.

**Recommended Safety Factors:**

| Facility Type | Safety Factor Range | Typical Application |
|---------------|---------------------|---------------------|
| Coolers (>32°F) | 10-15% | 1.10-1.15 multiplier |
| Freezers (<32°F) | 10-20% | 1.10-1.20 multiplier |
| Process rooms | 15-25% | 1.15-1.25 multiplier |
| Distribution centers | 10-15% | 1.10-1.15 multiplier |
| Food processing | 20-30% | 1.20-1.30 multiplier |

Higher safety factors apply when:
- Load calculations contain significant uncertainties
- Future expansion is anticipated
- Process equipment loads are not well-defined
- Facility operates near design conditions for extended periods
- Rapid pulldown capability is required

Lower safety factors apply when:
- Detailed load calculations are performed
- Equipment specifications are well-defined
- Conservative assumptions were used in base calculations
- Multiple refrigeration units provide inherent redundancy

## Design Conditions

### Outdoor Design Conditions

Select outdoor design temperatures based on ASHRAE Handbook—Fundamentals Chapter 14 climatic data. Use appropriate percentile values for the application.

**Recommended Design Conditions:**

| Application | Summer Design Condition | Winter Design Condition |
|-------------|------------------------|------------------------|
| Refrigeration equipment | 0.4% dry-bulb and mean coincident wet-bulb | 99.6% dry-bulb |
| Infiltration loads | 1% dry-bulb and dew point | 99% dry-bulb |
| Structural loads | 0.4% dry-bulb | 99.6% dry-bulb |

The 0.4% design condition represents conditions exceeded 35 hours per year, while 1% represents 88 hours per year.

### Indoor Design Conditions

Storage temperatures depend on product requirements and storage duration. Maintain temperature uniformity within ±2°F (±1°C) throughout the space.

**Common Storage Temperatures:**

| Product Category | Temperature Range | Relative Humidity |
|------------------|-------------------|-------------------|
| Fresh meat | 28-32°F (-2 to 0°C) | 88-92% |
| Dairy products | 33-40°F (1-4°C) | 80-85% |
| Fresh produce (most) | 32-36°F (0-2°C) | 90-95% |
| Bananas (ripening) | 58-65°F (14-18°C) | 85-90% |
| Frozen storage | -10 to 0°F (-23 to -18°C) | Not controlled |
| Ice cream hardening | -20 to -30°F (-29 to -34°C) | Not controlled |

### Design Temperature Differentials

The temperature difference between outdoor and indoor conditions drives transmission and infiltration loads. Consider both summer and winter conditions.

**Typical Design ΔT Values:**

| Location | Summer Outdoor DB | Cooler Indoor | Freezer Indoor | Cooler ΔT | Freezer ΔT |
|----------|-------------------|---------------|----------------|-----------|------------|
| Phoenix, AZ | 108°F (42°C) | 35°F (2°C) | 0°F (-18°C) | 73°F (41K) | 108°F (60K) |
| Atlanta, GA | 92°F (33°C) | 35°F (2°C) | 0°F (-18°C) | 57°F (32K) | 92°F (51K) |
| Minneapolis, MN | 90°F (32°C) | 35°F (2°C) | 0°F (-18°C) | 55°F (31K) | 90°F (50K) |
| Seattle, WA | 84°F (29°C) | 35°F (2°C) | 0°F (-18°C) | 49°F (27K) | 84°F (47K) |

## Load Diversity

Not all loads reach peak values simultaneously. Load diversity accounts for the temporal variation in different load components.

### Diversity Factors

**Typical Diversity Applications:**

- **Multiple rooms:** When calculating central plant capacity for multiple rooms at different temperatures, apply diversity to account for non-simultaneous peaks
- **Door openings:** Multiple doors rarely operate at peak traffic simultaneously
- **Product loading:** Receiving operations typically occur during specific hours, not continuously
- **Lighting:** Not all lights operate simultaneously in large facilities
- **Equipment:** Material handling equipment operates on varying schedules

**Diversity Factor Range:**

F_div = 0.75 to 0.95 for total facility load (apply to sum of individual room loads)

Do not apply diversity factors to:
- Transmission loads (continuous)
- Individual room sizing calculations
- Safety-critical applications
- Rapid-pulldown requirements

### Time-Dependent Loads

Some loads vary predictably throughout the day:

**24-Hour Load Profile Considerations:**

- **Product loads:** Peak during receiving hours (typically 6:00 AM - 2:00 PM)
- **Occupancy:** Varies with shift schedules
- **Lighting:** Follows occupancy patterns
- **Equipment:** Material handling equipment operates during active periods
- **Transmission:** Relatively constant, peaks during hottest outdoor conditions
- **Infiltration:** Related to door traffic patterns

**Load Profile Application:**

For central plant sizing, consider both peak instantaneous load and total heat removal over 24 hours. Thermal storage systems may leverage load diversity to reduce peak demand.

## Peak vs Average Loads

### Peak Load Determination

Peak refrigeration load represents the maximum simultaneous heat gain to the space. Size evaporators and compressors based on peak load plus safety factor.

**Peak Load Calculation:**

Q_peak = (Q_trans,max + Q_inf,max + Q_prod,peak + Q_int,peak + Q_lights,peak + Q_people,peak) × SF

Where SF = safety factor (1.10 to 1.30)

Peak loads typically occur when:
- Outdoor temperature is at design maximum
- Maximum product receiving occurs
- Full personnel complement is working
- All lights and equipment operate
- Doors experience high traffic

### Average Load Determination

Average load represents typical operating conditions over a 24-hour period. Use average loads for:
- Energy consumption calculations
- Operating cost estimates
- Annual refrigerant consumption
- Heat recovery system sizing

**Average Load Estimation:**

Q_avg = Q_trans,avg + Q_inf,avg + Q_prod,avg + Q_int,avg + Q_lights,avg + Q_people,avg

Average loads typically range from 40-60% of peak design loads depending on facility operation.

**Load Factor:**

LF = Q_avg / Q_peak

Typical load factors:
- Distribution centers: 0.45-0.55
- Food processing: 0.55-0.70
- Cold storage only: 0.40-0.50

## System Sizing Considerations

### Equipment Capacity Selection

Refrigeration equipment capacity must accommodate peak loads while operating efficiently at part-load conditions.

**Compressor Capacity:**

Select compressor capacity based on:

Q_comp,required = Q_peak / COP_system

Where COP_system accounts for:
- Compressor efficiency
- Condenser performance
- Evaporator performance
- Piping and component losses
- Defrost loads (if applicable)

**Multiple Compressor Staging:**

For improved part-load efficiency and reliability:
- Use 2-4 compressors per system
- Stage capacity in 25-50% increments
- Provide minimum 50% capacity with largest unit off
- Consider variable-speed compressors for modulation

### Evaporator Capacity

Select evaporators with sufficient capacity at design temperature difference (TD) between refrigerant and air.

**Evaporator Sizing:**

Q_evap,rated = Q_peak / (1 - f_defrost)

Where:
- f_defrost = Fraction of time in defrost (0.08-0.12 for low-temp applications)
- TD typically ranges from 8-15°F (4-8K) for coolers, 10-18°F (6-10K) for freezers

**Evaporator Selection Criteria:**

| Application | TD Range | Air Velocity | Defrost Method |
|-------------|----------|--------------|----------------|
| Coolers (high humidity) | 8-10°F (4-6K) | 500-700 fpm (2.5-3.5 m/s) | Off-cycle |
| Coolers (low humidity) | 10-15°F (6-8K) | 600-800 fpm (3-4 m/s) | Off-cycle |
| Freezers (normal) | 10-15°F (6-8K) | 400-600 fpm (2-3 m/s) | Electric/hot gas |
| Freezers (low humidity) | 15-18°F (8-10K) | 500-700 fpm (2.5-3.5 m/s) | Electric/hot gas |

Lower TD values provide:
- Better humidity control
- More uniform temperatures
- Higher equipment cost
- Improved product quality

Higher TD values provide:
- Lower equipment cost
- Reduced refrigerant charge
- Lower humidity (more dehumidification)
- Increased defrost frequency

### Condenser Capacity

Size condensers to reject both refrigeration load and compressor work at design conditions.

**Heat Rejection:**

Q_condenser = Q_evap + W_comp = Q_evap × (1 + 1/COP)

For air-cooled condensers:
- Size at 95°F (35°C) ambient minimum for most locations
- Consider 105-115°F (41-46°C) for hot climates
- Allow 120-125% capacity margin for fouling and degradation

For evaporative condensers:
- Size at design wet-bulb temperature
- Provide 110-115% capacity margin
- Consider water treatment requirements

### System Redundancy

Provide redundant capacity for critical applications:

**Redundancy Strategies:**

- **N+1 Configuration:** Provide one additional compressor beyond minimum required
- **50% Rule:** Size equipment so facility operates with any single largest unit offline
- **Separate Systems:** Divide facility into multiple independent refrigeration circuits
- **Emergency Backup:** Provide portable refrigeration connection points

**Redundancy by Application:**

| Facility Type | Recommended Redundancy | Justification |
|---------------|------------------------|---------------|
| Pharmaceutical | N+1 or 100% backup | Product value, regulatory requirements |
| Research laboratories | N+1 | Specimen preservation |
| Long-term frozen storage | 50% capacity with largest unit off | Product value, recovery time |
| Distribution centers | Multiple independent systems | Operational continuity |
| Short-term coolers | Minimal redundancy | Product can be relocated |

### Capacity Verification

Verify final equipment selection accounts for:

1. **Load calculation accuracy:** Review all assumptions and confirm input data
2. **Safety factor:** Ensure appropriate margin for uncertainties
3. **Future expansion:** Consider planned facility growth
4. **Part-load performance:** Confirm efficient operation at average loads
5. **Extreme conditions:** Evaluate performance during unusual events
6. **Defrost impact:** Account for capacity loss during defrost cycles
7. **Refrigerant charge:** Confirm adequate charge for all operating conditions

**Final Capacity Check:**

Q_installed ≥ Q_peak × SF × F_future

Where:
- Q_installed = Total installed refrigeration capacity
- F_future = Future expansion factor (1.0-1.25)

Document all load calculations, assumptions, and equipment selections for future reference and system troubleshooting.

## Calculation Documentation

Maintain comprehensive documentation including:
- Design basis and assumptions
- Climatic data sources
- Building construction details
- Product specifications and throughput
- Equipment schedules and operating profiles
- Safety factors applied
- Diversity factors used
- Equipment selection rationale
- Alternative scenarios evaluated

Reference ASHRAE Handbook—Refrigeration Chapters 13 (Load Calculations) and 24 (Refrigerated Facility Design) for detailed calculation procedures and additional guidance.
