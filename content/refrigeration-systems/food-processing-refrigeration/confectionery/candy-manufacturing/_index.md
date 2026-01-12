---
title: "Candy Manufacturing"
description: "Technical design requirements for candy manufacturing refrigeration systems including cooling tunnels, temperature control, humidity management, and process-specific cooling for hard candy, chocolate, and gummy products with condensation prevention strategies."
weight: 2
---

Candy manufacturing refrigeration systems provide precise temperature and humidity control for multiple processing stages including cooking, cooling, tempering, and storage. Process cooling requirements vary significantly based on candy composition, with hard candies requiring rapid cooling to achieve glass transition, chocolate products demanding controlled crystallization, and gummy candies needing gradual temperature reduction to prevent surface defects.

## Cooling Tunnel Design

Cooling tunnels remove heat from candy products following cooking or forming operations. Tunnel length, air velocity, and temperature profiles determine production throughput and product quality.

### Tunnel Configuration

**Continuous belt systems** transport products through multiple cooling zones with independent temperature control. Belt speed ranges from 0.5 to 3.0 m/min depending on product mass and required cooling rate.

**Multi-zone design** allows progressive temperature reduction:
- Entry zone: Initial cooling with minimal temperature differential to prevent thermal shock
- Primary cooling: Maximum heat removal at controlled rates
- Tempering zone: Final temperature equilibration
- Exit conditioning: Surface temperature stabilization before packaging

Air distribution employs overhead supply with perforated ducts or nozzle arrays positioned 150-300 mm above product surface. Supply air velocity at product level ranges from 3-8 m/s for forced convection cooling.

### Heat Transfer Analysis

Cooling rate calculation requires convective heat transfer coefficient determination:

h = Nu × k / L

Where:
- h = convective heat transfer coefficient, W/(m²·K)
- Nu = Nusselt number (dimensionless)
- k = air thermal conductivity, W/(m·K)
- L = characteristic length, m

For turbulent flow over flat candy surfaces:

Nu = 0.037 × Re^0.8 × Pr^0.33

Cooling load per meter of tunnel:

Q = ṁ × cp × ΔT

Where:
- Q = cooling load, W
- ṁ = product mass flow rate, kg/s
- cp = specific heat capacity, J/(kg·K)
- ΔT = temperature reduction, K

## Temperature Control Requirements

Different candy types require specific cooling profiles to achieve desired texture, appearance, and shelf stability.

### Hard Candy Cooling

Hard candies require rapid cooling from cooking temperature (150-165°C) to below glass transition temperature (Tg ≈ 30-50°C depending on moisture content and composition).

**Cooling rate targets:**
- Initial cooling: 20-40°C/min from cooking temperature to 80°C
- Secondary cooling: 10-20°C/min from 80°C to 40°C
- Final conditioning: 2-5°C/min from 40°C to packaging temperature

Supply air temperature progression:
- Zone 1: 10-15°C
- Zone 2: 5-10°C
- Zone 3: 15-20°C (tempering)

Excessive cooling rates cause surface stress cracking. Insufficient cooling results in product deformation and sticking.

### Chocolate Tempering Integration

Chocolate enrobing lines require cooling tunnels following tempering units. Proper cocoa butter crystallization demands precise temperature control.

Target cooling profile for dark chocolate:
- Enrobing temperature: 31-32°C
- Initial cooling zone: 12-15°C supply air, 2-3 minutes
- Primary cooling: 8-12°C supply air, 3-5 minutes
- Final conditioning: 15-18°C supply air, 1-2 minutes
- Exit temperature: 18-20°C

Milk chocolate requires gentler cooling due to milk solids:
- Higher initial zone temperatures (15-18°C)
- Extended cooling time
- Exit temperature: 16-18°C

### Gummy Candy Processing

Gummy candies contain 15-22% moisture and require controlled cooling to prevent surface condensation and uneven moisture distribution.

Cooling sequence:
- Demolding temperature: 55-70°C
- Initial air temperature: 20-25°C (small temperature differential prevents surface hardening)
- Primary cooling: 15-20°C, 50-60% RH
- Final temperature: 20-22°C before starch application or packaging

Relative humidity control prevents moisture loss from product surface while avoiding condensation on equipment surfaces.

## Humidity Management

Humidity control prevents surface defects including sugar bloom on chocolate, moisture migration in hard candies, and surface tackiness in gummy products.

### Dew Point Control

Equipment surfaces must remain above dew point temperature of process air to prevent condensation. Temperature differential between supply air and cooling coil surface determines moisture removal capacity.

For supply air at 10°C and 60% RH:
- Dew point temperature: 2.2°C
- Cooling coil surface temperature: -2 to 0°C
- Condensate removal rate depends on air circulation volume

Reheat capacity required:

Q_reheat = ṁ_air × cp,air × (T_supply - T_coil)

Where reheat raises discharge temperature from coil temperature to desired supply temperature while maintaining reduced absolute humidity.

### Process Air Conditions

| Candy Type | Supply Air Temp (°C) | Relative Humidity (%) | Air Velocity (m/s) | Dew Point (°C) |
|------------|---------------------|----------------------|-------------------|----------------|
| Hard candy | 5-15 | 40-50 | 5-8 | -5 to 2 |
| Chocolate | 8-15 | 50-60 | 3-5 | 2 to 8 |
| Gummy candy | 15-22 | 50-60 | 2-4 | 8 to 14 |
| Caramel | 10-18 | 45-55 | 4-6 | 0 to 8 |
| Fondant | 12-20 | 55-65 | 3-5 | 5 to 12 |

## Product-Specific Requirements

### Hard Candy Systems

**Cooling load calculation example:**

Production rate: 500 kg/hr
Inlet temperature: 160°C
Exit temperature: 25°C
Specific heat: 1.8 kJ/(kg·K)

Q = (500 kg/hr) × (1.8 kJ/kg·K) × (160-25 K) / 3600 s/hr
Q = 33.75 kW sensible cooling load

Add safety factor of 1.15-1.25 for equipment heat gain and transient conditions:
Design capacity: 39-42 kW

### Chocolate Cooling Tunnels

Chocolate crystallization releases latent heat of fusion (approximately 120-150 kJ/kg). Total cooling load includes:

Q_total = Q_sensible + Q_latent

Q_sensible = ṁ × cp × ΔT
Q_latent = ṁ × L_f × X

Where:
- L_f = latent heat of cocoa butter crystallization, kJ/kg
- X = cocoa butter mass fraction (0.30-0.35 for dark chocolate)

For 1000 kg/hr production:
- Sensible load: ṁ × 2.2 kJ/(kg·K) × (32-20 K) = 7.3 kW
- Latent load: ṁ × 0.33 × 135 kJ/kg = 12.4 kW
- Total: 19.7 kW, design capacity: 24 kW with safety factor

### Aerated Candy Products

Marshmallow, nougat, and whipped confections contain entrained air (40-60% by volume) requiring gentle handling. Air distribution must avoid product surface disruption while providing adequate cooling.

Design parameters:
- Maximum air velocity: 2-3 m/s at product surface
- Supply air temperature: 15-20°C
- Cooling tunnel residence time: 8-15 minutes
- Final product temperature: 22-25°C

## Condensation Prevention

Condensation on product surfaces causes sugar dissolution, surface defects, and microbial growth. Prevention requires maintaining all contact surfaces above dew point temperature.

### Surface Temperature Control

Belt surface temperature monitoring prevents condensation accumulation:
- Continuous temperature monitoring with IR sensors
- Belt material selection (stainless steel mesh with minimal thermal mass)
- Insulated return path to maintain temperature above dew point

Minimum belt surface temperature:

T_belt,min = T_dp + 3°C safety margin

Where T_dp is dew point temperature of process air.

### Equipment Design Features

**Insulated tunnel enclosures** prevent external moisture infiltration and maintain internal surface temperatures above condensation point. Insulation thickness calculated from:

Q = U × A × ΔT

Where U-value includes insulation resistance and surface resistances. Typical construction: 75-100 mm polyurethane or polyisocyanurate insulation achieving U ≤ 0.25 W/(m²·K).

**Air curtains at tunnel openings** minimize ambient air infiltration:
- Vertical laminar flow curtains
- Air velocity: 8-12 m/s
- Temperature matching adjacent zone ±2°C

**Vapor barriers** on cold surfaces prevent moisture transmission through insulation to cold surfaces where condensation would occur.

## Refrigeration System Design

### Capacity Requirements

Total refrigeration load includes:

1. **Product cooling load** (sensible and latent heat removal)
2. **Air circulation load** (fan motor heat)
3. **Infiltration load** (ambient air entry)
4. **Transmission load** (heat gain through enclosure)
5. **Lighting and equipment loads**

Typical load distribution:
- Product cooling: 60-70%
- Infiltration: 15-20%
- Transmission: 8-12%
- Fan motors: 5-8%
- Other: 2-5%

### System Configuration

**Direct expansion (DX) systems** provide temperature control for small to medium production lines (up to 100 kW cooling capacity). Evaporator coils installed in air handling units with precise temperature control through refrigerant flow modulation.

**Chilled water systems** serve multiple cooling tunnels from central plant. Supply water temperature: 2-6°C. Secondary refrigerant (glycol solutions) used when temperatures below 0°C required.

**Cascade refrigeration** for ultra-low temperature applications (below -40°C for specialized products like ice cream coatings).

## Control Strategies

### Multi-Zone Temperature Control

Independent zone control maintains optimal temperature profile:
- PID control loops for each zone
- Supply air temperature sensors (0.1°C accuracy)
- Product temperature monitoring via non-contact IR sensors
- Refrigerant valve modulation or variable speed fans for capacity control

### Humidity Control Integration

Coupled temperature-humidity control:
- Cooling coil with reheat for dehumidification
- Desiccant systems for precise dew point control (critical for chocolate applications)
- Steam injection humidification for gummy candy conditioning

Control sequence:
1. Measure supply air temperature and humidity
2. Modulate cooling coil capacity to achieve temperature setpoint
3. Adjust reheat to maintain humidity setpoint
4. Monitor product and equipment surface temperatures
5. Alarm conditions if surfaces approach dew point temperature

### Production Integration

Cooling system coordination with upstream processes:
- Cooking temperature feedback adjusts cooling requirements
- Production rate changes modify air circulation and refrigeration capacity
- Product changeover sequences adjust all zone temperatures and humidity levels
- Sanitation mode raises all temperatures for cleaning operations

## Energy Efficiency Considerations

Heat recovery from refrigeration condensers provides process heat:
- Warm water generation for cleaning operations
- Building heating during cold weather
- Tempering water for chocolate processing

Variable speed drives on circulation fans reduce energy consumption during reduced production or partial cooling requirements. Fan power varies with cube of speed, providing substantial savings at reduced airflow.

Night setback schedules for packaging areas while maintaining critical storage zones.

## Sanitation Requirements

Cooling tunnel design must facilitate cleaning:
- Sloped floors with drains (minimum 1% slope)
- Removable belt sections
- Accessible coil surfaces
- Stainless steel construction in product contact zones
- CIP (clean-in-place) capability for coils and air distribution components

Sanitation cycle heating requirements:
- Raise air temperature to 60-80°C
- Maintain for sufficient time to achieve surface sanitization
- Control condensation during cooldown
- Return to production conditions without product quality impact

