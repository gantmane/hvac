---
title: "Humidity Control in Cheese Manufacturing and Aging"
aliases: ["Humidity Control in Cheese Manufacturing and Aging"]
description: "Comprehensive analysis of humidity control requirements, psychrometric design, humidification systems, evaporator coil specifications, and control strategies for cheese manufacturing and aging facilities"
weight: 3
---

## Overview

Humidity control represents the most critical environmental parameter in cheese manufacturing and aging facilities. Precise relative humidity (RH) management prevents excessive moisture loss while controlling surface microbiology, rind development, and preventing condensation-related contamination. The challenge lies in maintaining high humidity levels (75-98% RH) at refrigeration temperatures while managing latent loads and preventing free water formation on surfaces.

The economic impact of improper humidity control includes weight shrinkage losses of 0.5-3% monthly, development of undesirable surface microorganisms, cracking or irregular rind formation, and accelerated equipment corrosion.

## Humidity Requirements by Cheese Type

Cheese varieties exhibit widely varying humidity requirements based on target moisture content, rind characteristics, and aging protocols.

### Natural Rind Cheeses

| Cheese Type | Temperature Range | Relative Humidity | Air Velocity | Aging Duration |
|-------------|-------------------|-------------------|--------------|----------------|
| Cheddar | 50-55°F (10-13°C) | 80-85% | 25-50 fpm | 3-24 months |
| Swiss/Emmental | 50-55°F (10-13°C) | 82-88% | 30-60 fpm | 4-12 months |
| Gouda | 50-55°F (10-13°C) | 80-85% | 25-40 fpm | 1-36 months |
| Gruyere | 52-56°F (11-13°C) | 92-95% | 15-30 fpm | 5-12 months |
| Parmesan | 55-60°F (13-16°C) | 75-80% | 40-70 fpm | 12-36 months |
| Manchego | 50-55°F (10-13°C) | 80-85% | 30-50 fpm | 3-12 months |

### Surface Ripened Cheeses

| Cheese Type | Temperature Range | Relative Humidity | Air Velocity | Aging Duration |
|-------------|-------------------|-------------------|--------------|----------------|
| Brie | 50-54°F (10-12°C) | 90-95% | 10-25 fpm | 3-5 weeks |
| Camembert | 50-54°F (10-12°C) | 90-95% | 10-25 fpm | 3-5 weeks |
| Taleggio | 50-55°F (10-13°C) | 90-95% | 15-30 fpm | 6-10 weeks |
| Epoisses | 52-57°F (11-14°C) | 95-98% | 10-20 fpm | 4-8 weeks |
| Munster | 50-55°F (10-13°C) | 92-96% | 15-25 fpm | 3-12 weeks |

### Blue Veined Cheeses

| Cheese Type | Temperature Range | Relative Humidity | Air Velocity | Aging Duration |
|-------------|-------------------|-------------------|--------------|----------------|
| Roquefort | 46-50°F (8-10°C) | 95-98% | 20-40 fpm | 3-9 months |
| Gorgonzola | 36-40°F (2-4°C) | 90-95% | 25-50 fpm | 2-4 months |
| Stilton | 50-55°F (10-13°C) | 90-95% | 30-50 fpm | 9-12 weeks |
| Danish Blue | 45-50°F (7-10°C) | 90-95% | 25-45 fpm | 8-12 weeks |

### Fresh and Soft Cheeses

| Cheese Type | Storage Temperature | Relative Humidity | Air Velocity | Shelf Life |
|-------------|---------------------|-------------------|--------------|------------|
| Mozzarella | 36-40°F (2-4°C) | 80-85% | 50-100 fpm | 7-21 days |
| Ricotta | 36-40°F (2-4°C) | 80-85% | 40-80 fpm | 7-14 days |
| Cottage Cheese | 36-40°F (2-4°C) | 80-85% | 40-80 fpm | 10-21 days |
| Cream Cheese | 36-40°F (2-4°C) | 75-80% | 50-100 fpm | 21-60 days |

## Psychrometric Analysis

### Moisture Loss Mechanisms

Weight loss from cheese surfaces occurs through vapor pressure gradient-driven diffusion:

**Weight Loss Rate:**

```
dm/dt = (k × A × Δpv) / L
```

Where:
- dm/dt = mass transfer rate (lb/hr)
- k = mass transfer coefficient (lb/hr·ft²·psi)
- A = surface area (ft²)
- Δpv = vapor pressure difference (psi)
- L = characteristic length (ft)

**Vapor Pressure Gradient:**

```
Δpv = pvs,cheese - pv,air
```

Where:
- pvs,cheese = saturated vapor pressure at cheese surface temperature
- pv,air = partial vapor pressure in surrounding air

### Relative Humidity and Weight Loss

The relationship between RH and weight loss rate is approximately linear within the typical cheese aging range:

| Relative Humidity | Daily Weight Loss (% per day) |
|-------------------|-------------------------------|
| 70% | 0.08-0.12% |
| 75% | 0.06-0.09% |
| 80% | 0.04-0.07% |
| 85% | 0.03-0.05% |
| 90% | 0.02-0.03% |
| 95% | 0.01-0.015% |
| 98% | 0.005-0.01% |

### Psychrometric State Points

**Example: Cheddar Aging Room (Design Conditions)**

```
Space Conditions:
- Dry bulb temperature: 52°F
- Relative humidity: 82%
- Wet bulb temperature: 50.2°F
- Dew point: 47.8°F
- Humidity ratio: 0.00615 lb moisture/lb dry air
- Specific enthalpy: 18.6 Btu/lb dry air
- Specific volume: 13.05 ft³/lb dry air
```

**Outdoor Air (Summer Design):**

```
- Dry bulb temperature: 95°F
- Relative humidity: 55%
- Wet bulb temperature: 78°F
- Dew point: 75.5°F
- Humidity ratio: 0.01825 lb/lb
- Specific enthalpy: 42.1 Btu/lb
```

**Dehumidification Load Calculation:**

```
Latent load = ṁa × hfg × (ωo - ωi)

Where:
- ṁa = mass flow rate of dry air (lb/hr)
- hfg = latent heat of vaporization = 1061 Btu/lb at 52°F
- ωo = outdoor humidity ratio = 0.01825 lb/lb
- ωi = indoor humidity ratio = 0.00615 lb/lb

Latent load = ṁa × 1061 × (0.01825 - 0.00615)
Latent load = 12.84 × ṁa Btu/hr
```

### Moisture Balance

Total moisture generation in aging room:

```
Qmoisture = (Qinfiltration + Qproduct + Qpeople) - Qhumidification

Where:
Qinfiltration = infiltration moisture gain (lb/hr)
Qproduct = moisture loss from cheese surfaces (lb/hr)
Qpeople = occupant moisture generation (lb/hr)
Qhumidification = humidifier output required (lb/hr)
```

**Product Moisture Loss:**

```
Qproduct = (Total cheese weight × Daily loss rate) / 24

Example:
50,000 lb cheese × 0.05% per day / 24 hr = 1.04 lb/hr loss
```

## Humidification Systems

### Steam Injection Humidifiers

Steam injection provides the most hygienic humidification method for cheese facilities.

**Clean Steam Generation:**

- Culinary steam quality (potable water source)
- Total dissolved solids < 10 ppm
- Silica content < 0.1 ppm
- Endotoxin levels < 0.5 EU/mL
- No treatment chemicals (for food contact applications)

**Steam Humidifier Sizing:**

```
Steam required (lb/hr) = (CFM × 4.5 × ΔW) / 60

Where:
- CFM = airflow rate
- 4.5 = air density factor at standard conditions (0.075 lb/ft³ × 60)
- ΔW = humidity ratio increase (grains/lb)
- 60 = conversion factor
```

**Steam Distribution Manifold Design:**

| Parameter | Specification |
|-----------|---------------|
| Manifold material | 316 stainless steel |
| Dispersion tube diameter | 1-2 inches |
| Orifice spacing | 6-12 inches on center |
| Orifice diameter | 0.125-0.25 inches |
| Steam velocity | < 100 ft/s |
| Condensate trap spacing | Every 20-30 ft horizontal run |
| Absorption distance | Minimum 4 ft downstream |

**Control Response:**

- Modulating steam valve with 0-10 VDC or 4-20 mA control
- Response time: 10-30 seconds
- Turndown ratio: 10:1 to 20:1
- Accuracy: ±2% RH at setpoint

### Ultrasonic Atomizing Humidifiers

Ultrasonic systems produce sub-micron water droplets through high-frequency vibration.

**Operating Characteristics:**

| Parameter | Typical Value |
|-----------|---------------|
| Droplet size | 1-5 microns |
| Frequency | 1.65-2.4 MHz |
| Water consumption | 1-10 lb/hr per module |
| Power consumption | 50-150 watts per lb/hr |
| Water quality requirement | < 50 ppm TDS, filtered to 5 microns |
| Turndown ratio | 10:1 modulating |

**Mineral Content Limits:**

Reverse osmosis (RO) water strongly recommended to prevent white dust and mineral buildup:

- Total dissolved solids: < 10 ppm
- Calcium hardness: < 5 ppm as CaCO₃
- Silica: < 0.5 ppm
- Iron: < 0.1 ppm

### Evaporative Pad Humidifiers

Wetted media systems provide adiabatic cooling and humidification.

**Media Specifications:**

| Media Type | Efficiency | Pressure Drop | Water Flow Rate |
|------------|------------|---------------|-----------------|
| Rigid cellulose (6") | 85-92% | 0.15-0.25 in. w.g. | 0.5-1.0 gpm/ft² |
| Rigid cellulose (12") | 90-95% | 0.25-0.40 in. w.g. | 0.5-1.0 gpm/ft² |
| Plastic media | 70-80% | 0.10-0.20 in. w.g. | 0.3-0.7 gpm/ft² |

**Face Velocity Limits:**

- Maximum: 500-600 fpm (for 85% efficiency)
- Typical design: 400-500 fpm
- Minimum: 200 fpm (below this, efficiency drops significantly)

**Water Quality Requirements:**

- pH: 6.5-8.5
- Total hardness: < 200 ppm as CaCO₃
- Chloride: < 100 ppm
- Sulfate: < 100 ppm
- Biological treatment: UV sterilization or chlorine dosing (0.5-1.0 ppm free chlorine)

## Evaporator Coil Design for High RH

### Coil Configuration Strategies

Maintaining high RH while providing refrigeration requires careful coil design to minimize dehumidification.

**Approach Temperature Difference:**

```
ΔTapproach = Tair,in - Tcoil,sat

For high RH applications:
- Traditional: ΔT = 15-25°F (excessive dehumidification)
- High RH design: ΔT = 5-10°F (minimal dehumidification)
```

**Coil Selection Parameters:**

| Application | Rows Deep | Fins per Inch | Face Velocity | TD Approach |
|-------------|-----------|---------------|---------------|-------------|
| Standard (70% RH) | 4-6 | 8-10 | 400-500 fpm | 15-20°F |
| Medium RH (80-85%) | 6-8 | 6-8 | 300-400 fpm | 10-15°F |
| High RH (85-92%) | 8-10 | 4-6 | 250-350 fpm | 8-12°F |
| Very High RH (92-98%) | 10-12 | 3-5 | 200-300 fpm | 5-8°F |

### Dual Coil Systems

Separate sensible and latent coils provide independent temperature and humidity control.

**System Configuration:**

1. **Sensible Coil (First Stage):**
   - Refrigerant: R-404A, R-507A, R-448A
   - Saturation temperature: 45-48°F (above dew point)
   - Function: Temperature control only, no dehumidification
   - Control: Modulating refrigerant valve based on space temperature

2. **Latent Coil (Second Stage):**
   - Refrigerant: Same as sensible coil
   - Saturation temperature: 35-40°F (below dew point)
   - Function: Dehumidification only when RH exceeds setpoint
   - Control: On/off or staged control based on space RH

**Capacity Ratio:**

```
Sensible coil capacity = 70-85% of total load
Latent coil capacity = 15-30% of total load
```

### Face and Bypass Arrangement

Controlling air bypass around coil provides humidity control without deep coil sections.

**Bypass Damper Control:**

```
Bypass percentage = [(RHactual - RHsetpoint) / (100% - RHsetpoint)] × 100%

Where dampers modulate to achieve:
- 0% bypass at RH below setpoint (full dehumidification)
- 50-100% bypass at or above RH setpoint (minimal dehumidification)
```

**System Benefits:**

- Simpler than dual coil systems
- Lower first cost
- Single refrigeration circuit
- Standard coil construction

**Limitations:**

- Less precise RH control (±3-5% vs. ±2-3% for dual coil)
- Higher face velocity through active coil area
- Bypass damper requires regular maintenance

### Glycol Spray Coils

Direct glycol spray onto coil faces increases wet surface area and heat transfer while minimizing dehumidification.

**Glycol Solution Specifications:**

| Parameter | Specification |
|-----------|---------------|
| Glycol type | Propylene glycol (food-grade) |
| Concentration | 30-40% by weight |
| Freeze protection | To -10°F |
| Spray nozzle pressure | 5-15 psi |
| Flow rate | 1-3 gpm per 10,000 Btu/hr |
| Solution temperature | 45-50°F |

**Heat Transfer Enhancement:**

```
Enhanced UA = Standard UA × (1 + 0.3 to 0.6)

Where enhancement factor depends on:
- Spray coverage uniformity
- Glycol film thickness
- Solution temperature
```

## Moisture Loss Prevention Strategies

### Air Velocity Control

Air movement accelerates evaporation through boundary layer disruption. The relationship follows:

```
Evaporation rate ∝ v^0.8

Where v = air velocity across cheese surface
```

**Maximum Air Velocities by Cheese Type:**

| Cheese Category | Maximum Velocity | Typical Design |
|-----------------|------------------|----------------|
| Hard aged cheeses (Parmesan) | 70 fpm | 40-50 fpm |
| Semi-hard (Cheddar, Gouda) | 50 fpm | 25-40 fpm |
| Semi-soft (Havarti, Fontina) | 40 fpm | 20-30 fpm |
| Soft ripened (Brie, Camembert) | 25 fpm | 10-20 fpm |
| Blue cheeses (Roquefort) | 40 fpm | 20-30 fpm |

### Surface Treatments

**Natural Rind Development:**

- Controlled surface drying during first 3-7 days
- Progressive RH increase from 75% to 85-90%
- Salt brine application (20-24% NaCl) before aging
- Periodic washing/brushing schedules

**Applied Coatings:**

| Coating Type | Application Method | Moisture Retention | Aging Duration |
|--------------|-------------------|-------------------|----------------|
| Wax (paraffin blend) | Dip or brush | 90-95% | 3-24 months |
| Plastic coating | Spray or dip | 95-98% | 2-18 months |
| Breathable membrane | Vacuum applied | 85-92% | 3-12 months |
| Cheese cloth | Wrap and lard | 80-88% | 6-24 months |
| Vacuum packaging | Machine sealed | 98-99% | Extended storage |

### Racking and Spacing

**Shelf Configuration:**

- Minimum 2-inch spacing between cheeses
- Minimum 4-inch spacing from walls
- 12-18 inch vertical tier spacing
- Regular turning schedule (weekly to monthly depending on type)

**Air Distribution Strategy:**

Horizontal airflow parallel to shelving prevents direct impingement:

```
Supply air diffusers: Located at room ends
Return air grilles: Located at opposite ends
Air pattern: Horizontal sweep across shelves
Average velocity: 15-30 fpm in storage zone
```

## Condensation Management

### Dew Point Control

Condensation forms on any surface below the space dew point temperature. Critical surfaces include:

**Surface Temperature Analysis:**

```
For condensation prevention:
Tsurface > Tdew point + 2°F safety margin

At 52°F, 85% RH:
- Dew point = 48.3°F
- Minimum surface temperature = 50.3°F
```

**High-Risk Surfaces:**

| Surface | Risk Level | Mitigation Strategy |
|---------|------------|---------------------|
| Exterior walls (winter) | High | Insulation R-20 minimum, vapor retarder |
| Ceiling (under warm roof) | High | Insulation R-30 minimum, ventilated cavity |
| Windows/doors | Very high | Eliminate or use heated glass |
| Refrigerant piping | High | Insulation R-4 minimum, vapor seal |
| Structural steel | Medium | Insulation wrap or spray foam |
| Concrete floor | Medium | Underslab insulation and vapor barrier |

### Building Envelope Design

**Wall Construction for High RH Spaces:**

```
Interior to Exterior:
1. Stainless steel or FRP panels
2. Vapor retarder (≤ 0.01 perm rating)
3. Rigid insulation (polyisocyanurate), R-20 to R-30
4. Air/weather barrier
5. Exterior cladding
```

**Vapor Retarder Placement:**

Located on warm (exterior) side of insulation in refrigerated spaces to prevent moisture migration into insulation cavity.

**Permeance Requirements:**

```
Vapor retarder permeance ≤ 0.01 perms
(1 perm = 1 grain/hr·ft²·in.Hg)

Common materials:
- Polyethylene sheet (6 mil): 0.06 perms
- Aluminum foil: 0.0 perms (vapor barrier)
- Asphalt-coated kraft paper: 0.3 perms
- Liquid-applied membranes: 0.01-0.05 perms
```

### Dehumidification During Warm Weather

Infiltration and ventilation air introduce high moisture loads during warm, humid weather.

**Moisture Load from Infiltration:**

```
Qlatent = CFM × 4.5 × ΔW × 1061 / 60

Where:
- CFM = infiltration air volume flow rate
- 4.5 = density factor (0.075 lb/ft³ × 60 min/hr)
- ΔW = humidity ratio difference (lb/lb)
- 1061 = latent heat at typical conditions (Btu/lb)
- 60 = conversion factor

Example:
500 CFM infiltration
95°F, 55% RH outdoor (ω = 0.01825 lb/lb)
52°F, 85% RH indoor (ω = 0.00615 lb/lb)

Qlatent = 500 × 4.5 × (0.01825 - 0.00615) × 1061 / 60
Qlatent = 4,838 Btu/hr (0.4 tons latent)
```

**Dedicated Outdoor Air System (DOAS):**

Pre-condition ventilation air with separate dehumidification unit:

1. Cooling coil: Reduce to 40-45°F, removing majority of moisture
2. Reheat coil: Increase to 50-52°F to match space temperature
3. Delivery: Tempered air at space temperature, low humidity ratio

**Desiccant Dehumidification:**

Lithium chloride or silica gel wheels remove moisture without excessive cooling:

- Process air: Space air passed through desiccant wheel
- Regeneration air: Heated outdoor air (180-240°F) regenerates desiccant
- Energy input: 2,500-4,000 Btu per lb water removed
- Typical moisture removal: 20-40 grains per lb of process air

## Control System Design

### Humidity Measurement

**Sensor Technology Selection:**

| Sensor Type | Accuracy | Response Time | Cost | Application |
|-------------|----------|---------------|------|-------------|
| Capacitive thin film | ±2-3% RH | 30-60 sec | Medium | General aging rooms |
| Chilled mirror | ±0.5% RH | 60-120 sec | High | Critical applications |
| Resistive | ±3-5% RH | 30-60 sec | Low | Non-critical areas |
| Psychrometric (wet bulb) | ±2% RH | 90-180 sec | Medium | Verification/calibration |

**Sensor Placement Guidelines:**

- Height: 4-6 ft above floor (representative of cheese level)
- Location: Representative of average space conditions, avoid direct airflow
- Quantity: One sensor per 2,000-3,000 ft² floor area
- Spacing: Minimum 15 ft from humidifiers, 10 ft from evaporator coils
- Protection: Perforated shield to protect from physical damage

**Calibration Schedule:**

- Monthly verification against reference psychrometer
- Annual factory calibration or replacement
- Immediate recalibration after any reading anomalies

### Control Strategies

**Split-Range Control (Single Zone):**

Modulating control sequence for integrated humidity control:

```
RH < 80%: Dehumidification mode
- Refrigeration coil: 100% capacity
- Humidifier: Off

RH = 80-82%: Deadband
- Refrigeration coil: Minimum capacity for sensible load
- Humidifier: Off

RH = 82-85%: Proportional band
- Refrigeration coil: Modulating based on temperature
- Humidifier: Modulating based on RH

RH > 85%: Full humidification
- Refrigeration coil: Sensible load only (high coil temperature)
- Humidifier: 100% capacity
```

**PID Control Algorithm:**

```
Output = Kp × e(t) + Ki × ∫e(t)dt + Kd × de(t)/dt

Where:
- e(t) = setpoint - measured value
- Kp = proportional gain (typical: 2-5% output per % RH error)
- Ki = integral gain (typical: 0.1-0.5 repeats per minute)
- Kd = derivative gain (typical: 0-0.2 minutes)
```

**Tuning Parameters for Humidity Control:**

| Parameter | Conservative | Moderate | Aggressive |
|-----------|--------------|----------|------------|
| Proportional band | ±5% RH | ±3% RH | ±2% RH |
| Integral time | 10 minutes | 5 minutes | 2 minutes |
| Derivative time | 0 minutes | 0.5 minutes | 1 minute |
| Update rate | 1 minute | 30 seconds | 15 seconds |

### Multi-Zone Control

Cheese aging facilities often contain multiple rooms with different environmental requirements.

**Zone Configuration:**

1. **Fresh Cheese Cold Storage:** 36-40°F, 80-85% RH
2. **Initial Aging:** 50-55°F, 85-90% RH
3. **Long-term Aging:** 52-58°F, 75-85% RH
4. **Surface-Ripened Aging:** 50-54°F, 90-95% RH
5. **Packaging/Finishing:** 45-50°F, 70-80% RH

**Central Monitoring:**

- Building automation system (BAS) integration
- Trending and alarming for all zones
- Automated reporting of temperature and RH compliance
- Remote access and control capabilities

**Alarm Setpoints:**

| Parameter | Warning Level | Critical Level | Response Time |
|-----------|---------------|----------------|---------------|
| Temperature deviation | ±3°F | ±5°F | Immediate |
| RH deviation | ±5% | ±8% | 15 minutes |
| Sensor failure | N/A | Signal loss | Immediate |
| Equipment failure | Any component | Critical equipment | Immediate |

## Energy Efficiency Considerations

### Refrigeration System Optimization

**High Suction Temperature Benefits:**

Operating evaporator coils at higher saturation temperatures (closer to space temperature) significantly improves efficiency:

```
COP improvement = (Tevap,high - Tevap,low) / (Tcond - Tevap,low) × 100%

Example:
Standard: Tevap = 35°F, Tcond = 95°F
COP = (95 - 35) / (95 + 460 - 35 + 460) = 0.060 = 6.0% improvement per °F

High RH design: Tevap = 45°F vs. 35°F
Improvement = 10°F × 6.0% = 60% better efficiency
(Actual improvement ~30-40% due to other factors)
```

**Variable Capacity Compressors:**

- Digital scroll compressors: 10-100% capacity in 10% steps
- Variable frequency drives: Continuous modulation, 30-100% capacity
- Multiple compressors: Staged operation based on load

**Floating Head Pressure:**

Allow condensing pressure to decrease during cool weather:

```
Minimum head pressure = Pevap + ΔPexpansion device + safety margin

Typical minimum: 100-125 psig (R-404A)
Standard setting: 200-250 psig
Floating range: 125-250 psig based on ambient temperature
```

### Heat Recovery

**Refrigeration Heat Recovery:**

Capture condenser heat for beneficial use:

1. **Hot Water Generation:**
   - Desuperheater captures 15-25% of heat of rejection
   - Water heating from 50°F to 140°F
   - Applications: CIP systems, wash-down stations

2. **Space Heating:**
   - Condenser heat for adjacent offices or processing areas
   - Typical capacity: 25-50% of refrigeration load
   - Hydronic heating coils or forced air

**Energy Recovery Calculation:**

```
Available heat = Qrefrig × (1 + 1/COP)

Where:
- Qrefrig = refrigeration capacity (Btu/hr)
- COP = coefficient of performance

Example:
100 tons refrigeration (1,200,000 Btu/hr)
COP = 2.5

Available heat = 1,200,000 × (1 + 1/2.5) = 1,680,000 Btu/hr
```

### Insulation and Infiltration Control

**Insulation Requirements:**

| Surface | Minimum R-Value | Recommended R-Value |
|---------|-----------------|---------------------|
| Walls | R-20 | R-25 to R-30 |
| Ceiling/roof | R-30 | R-40 to R-50 |
| Floor (above unconditioned space) | R-15 | R-20 to R-25 |
| Floor (slab on grade) | R-10 perimeter | R-15 full slab |

**Infiltration Reduction:**

- Vestibules or airlocks at all personnel doors
- Strip curtains or high-speed doors at loading docks
- Positive pressure in adjacent anterooms (0.02-0.05 in. w.g.)
- Infiltration target: < 0.1 air changes per hour

**Infiltration Load Calculation:**

```
Qinfiltration,sensible = CFM × 1.08 × ΔT
Qinfiltration,latent = CFM × 0.68 × Δω × (grains/lb)

Total infiltration = Qsensible + Qlatent
```

## Equipment Specifications

### Evaporator Coil Specifications

**High RH Coil Construction:**

| Component | Standard Design | High RH Design |
|-----------|-----------------|----------------|
| Tube material | Copper | Copper or stainless steel |
| Fin material | Aluminum | Aluminum with e-coat or stainless |
| Fin spacing | 6-8 fpi | 4-6 fpi |
| Rows deep | 4-6 | 8-12 |
| Circuiting | Standard | Interlaced for uniform temperature |
| Drain pan | 18 ga galvanized | 16 ga stainless steel |
| Casing | Galvanized steel | Stainless steel or coated aluminum |

**Coil Face Area Calculation:**

```
Coil face area (ft²) = CFM / Face velocity (fpm)

For high RH application:
CFM = 10,000 (typical aging room)
Face velocity = 300 fpm (maximum for minimal dehumidification)

Coil face area = 10,000 / 300 = 33.3 ft²
```

### Fan and Air Distribution

**Fan Type Selection:**

| Fan Type | Efficiency | Noise Level | Application |
|----------|------------|-------------|-------------|
| Forward curved centrifugal | 50-65% | Medium | Low to medium static |
| Backward inclined centrifugal | 70-80% | Low | Medium to high static |
| Airfoil centrifugal | 80-85% | Very low | High static, large CFM |
| Plenum (plug) | 30-50% | High | Unit coolers only |
| EC plug fan | 55-65% | Medium | Energy-efficient unit coolers |

**Motor and Drive:**

- Variable frequency drive (VFD) for all fans > 5 HP
- EC (electronically commutated) motors for smaller applications
- Premium efficiency motors (IE3 or higher)
- Inverter duty rated for VFD applications

**Air Distribution Parameters:**

```
System static pressure = ΔPcoil + ΔPduct + ΔPfittings + ΔPdiffusers

Typical values:
- Evaporator coil: 0.25-0.50 in. w.g.
- Ductwork: 0.05-0.10 in. w.g. per 100 ft
- Fittings: 0.10-0.30 in. w.g. total
- Supply diffusers: 0.05-0.15 in. w.g.

Total system: 0.50-1.25 in. w.g.
```

### Humidifier Specifications

**Steam Humidifier:**

```
Capacity: 25-500 lb/hr per unit
Steam pressure required: 5-15 psig
Electrical connection: 120V or 208-240V control circuit
Control signal: 4-20 mA, 0-10 VDC, or modulating steam valve
Dispersion tube length: Based on duct width minus 4 inches each side
Materials: 316 stainless steel wetted parts
```

**Ultrasonic Humidifier:**

```
Capacity: 5-50 lb/hr per module
Power consumption: 70-120 watts per lb/hr output
Water supply: ½" connection, 20-40 psi, RO treated
Electrical: 115VAC or 230VAC
Control: 4-20 mA or 0-10 VDC modulating
Absorption distance: Minimum 3-4 ft
```

**Installation Requirements:**

- Steam humidifiers: 10-15 ft upstream of coil, 4+ ft absorption distance
- Ultrasonic: 8-12 ft upstream of coil, 3-4 ft absorption distance
- Water supply: Filtered, treated per manufacturer requirements
- Drainage: Trapped condensate drain for steam units
- Maintenance access: 36-inch clearance minimum

### Control Valves and Actuators

**Refrigerant Control Valves:**

| Application | Valve Type | Sizing Criterion |
|-------------|-----------|------------------|
| Liquid line | Electronic expansion valve (EEV) | Pressure drop 50-100 psi |
| Suction modulation | Suction pressure regulator | ΔP < 3 psi at design flow |
| Hot gas bypass | Modulating solenoid | Capacity for 25-40% minimum load |
| Liquid injection | Electronic injection valve | Superheat control response |

**Actuator Specifications:**

- Modulating control: 0-10 VDC or 4-20 mA proportional
- Actuator force: 150-300 lb-in based on valve size
- Spring return for fail-safe position (typically closed)
- Position feedback signal for verification
- Environmental rating: NEMA 4 minimum for wet locations

## System Integration

### Monitoring and Alarms

**Critical Monitoring Points:**

1. Space temperature (multiple locations)
2. Space relative humidity (multiple locations)
3. Coil entering air temperature and RH
4. Coil leaving air temperature and RH
5. Coil saturation temperature (or suction pressure)
6. Humidifier output signal and water flow
7. Fan status and VFD feedback
8. Door position switches (alarm on open > 5 minutes)

**Data Trending:**

- 1-minute interval recording for temperature and RH
- 15-minute average trending for analysis
- Minimum 1-year data retention
- Automated report generation (daily, weekly, monthly)

### Maintenance Requirements

**Preventive Maintenance Schedule:**

| Component | Frequency | Tasks |
|-----------|-----------|-------|
| Evaporator coils | Monthly | Visual inspection, clean if needed |
| Coil cleaning | Quarterly | Alkaline cleaner, sanitize, rinse |
| Humidifier | Monthly | Inspect nozzles/dispersion tube, clean mineral deposits |
| RH sensors | Monthly | Verify reading, clean sensor element |
| Sensor calibration | Annually | Factory calibration or replacement |
| Refrigerant charge | Quarterly | Check superheat/subcooling, add if needed |
| Fan bearings | Semi-annually | Lubricate, check alignment |
| Drain pans | Monthly | Clean, verify drainage, sanitize |
| Air filters | Monthly | Replace or clean (depends on type) |

**Coil Cleaning Procedure:**

1. Shut down refrigeration system
2. Apply alkaline coil cleaner (pH 11-12) per manufacturer instructions
3. Allow 10-15 minute dwell time
4. Rinse thoroughly with low-pressure water (< 300 psi)
5. Apply EPA-registered sanitizer
6. Final rinse with potable water
7. Verify complete drainage before restart

## Design Example

**Project: Cheddar Cheese Aging Facility**

**Design Parameters:**

```
Room dimensions: 40 ft × 60 ft × 12 ft high
Floor area: 2,400 ft²
Volume: 28,800 ft³

Design conditions:
- Temperature: 52°F ±2°F
- Relative humidity: 82% ±3%
- Cheese inventory: 60,000 lb
- Turnover rate: Monthly additions/removals
```

**Load Calculations:**

```
Transmission load:
- Walls (1,440 ft², R-25): 1,440 × 2 × (95-52) / 25 = 4,940 Btu/hr
- Ceiling (2,400 ft², R-40): 2,400 × 1.5 × (95-52) / 40 = 3,870 Btu/hr
- Floor (slab on grade, R-15): 2,400 × 1 × (70-52) / 15 = 2,880 Btu/hr

Subtotal transmission: 11,690 Btu/hr

Infiltration load (0.1 ACH):
- CFM = 28,800 × 0.1 / 60 = 48 CFM
- Sensible: 48 × 1.08 × (95-52) = 2,230 Btu/hr
- Latent: 48 × 4.5 × (0.01825 - 0.00615) × 1061 / 60 = 465 Btu/hr

Subtotal infiltration: 2,695 Btu/hr

Product load:
- Initial cooling: Minimal (pre-cooled before aging)
- Respiration: 60,000 lb × 0.02 Btu/lb/day / 24 hr = 50 Btu/hr

Lighting load:
- 0.5 W/ft² × 2,400 ft² × 3.41 Btu/W × 0.5 usage factor = 2,050 Btu/hr

Occupancy load:
- 2 persons × 4 hours/day × (250 sensible + 200 latent) / 24 hr = 150 Btu/hr

Safety factor: 10%

Total cooling load = (11,690 + 2,695 + 50 + 2,050 + 150) × 1.10 = 18,300 Btu/hr
Total capacity required = 1.5 tons
```

**Equipment Selection:**

```
Evaporator unit:
- Nominal capacity: 2 tons (oversized for high RH operation)
- Coil configuration: 10 rows, 4 fpi, 400 fpm face velocity
- Fan: 3,000 CFM, 0.75 HP with VFD
- Refrigerant: R-404A
- Coil TD: 8-10°F (45°F coil, 52°F air)

Humidifier:
- Type: Modulating steam injector
- Capacity: 15 lb/hr (to overcome infiltration and dehumidification)
- Steam pressure: 5-10 psig
- Control: 4-20 mA modulating valve

Control system:
- BAS integration with modulating PID control
- Dual RH sensors for redundancy
- Temperature sensor averaging (3 locations)
```

This comprehensive design ensures precise environmental control for optimal cheese aging while maintaining energy efficiency and minimizing product weight loss.

## Conclusion

Humidity control in cheese manufacturing and aging facilities demands specialized HVAC system design integrating refrigeration, humidification, air distribution, and control systems. Success requires understanding psychrometric principles, cheese-specific requirements, and system integration strategies. Proper design delivers consistent product quality, minimizes weight loss, prevents contamination, and optimizes energy consumption. The investment in sophisticated humidity control systems returns dividends through reduced shrinkage, improved product quality, and extended shelf life.
