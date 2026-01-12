---
title: "Humidification"
description: "Comprehensive analysis of HVAC humidification processes including steam injection, spray humidification, evaporative methods, psychrometric process representation, energy requirements, and design considerations for commercial and industrial applications."
weight: 4
---

## Overview

Humidification increases the moisture content of air by adding water vapor to the airstream. This process is fundamental to maintaining indoor air quality, occupant comfort, process control, and material preservation in cold weather when outdoor air contains insufficient moisture. Humidification processes modify both the absolute humidity (humidity ratio) and, depending on the method employed, the dry-bulb temperature of the air.

The physics of humidification involves mass transfer of water vapor into the airstream, with simultaneous energy transfer that depends on the humidification method. Understanding the psychrometric process path, energy requirements, and control implications is essential for proper system design and operation.

## Fundamental Principles

### Mass Transfer Process

Humidification increases the humidity ratio (W) of air:

**Humidity Ratio Change:**
```
ΔW = W₂ - W₁
```

Where:
- W₁ = initial humidity ratio (lb H₂O/lb dry air)
- W₂ = final humidity ratio (lb H₂O/lb dry air)
- ΔW = moisture added per pound of dry air

**Mass Flow Rate of Water Vapor Added:**
```
ṁw = ṁa × ΔW
```

Where:
- ṁw = mass flow rate of water vapor added (lb/hr)
- ṁa = mass flow rate of dry air (lb/hr)
- ΔW = change in humidity ratio (lb H₂O/lb dry air)

### Energy Considerations

The energy required for humidification depends on the initial state of the water supplied and the humidification method employed. The total energy includes:

1. **Sensible energy** to heat water to required temperature
2. **Latent energy** to vaporize liquid water to vapor
3. **Sensible energy** change in the air (method-dependent)

## Humidification Methods

### Steam Injection Humidification

Steam injection introduces water vapor directly into the airstream. This is an isothermal humidification process when dry saturated steam is used, meaning the dry-bulb temperature remains constant while humidity ratio increases.

#### Process Characteristics

**Psychrometric Process Path:**
- Horizontal line on psychrometric chart (constant dry-bulb temperature)
- Increases humidity ratio
- Increases enthalpy
- Increases relative humidity
- Dew point temperature increases

**Energy Balance:**

For isothermal humidification with dry saturated steam:

```
h₂ = h₁ + ΔW × hg
```

Where:
- h₁ = initial enthalpy of air (Btu/lb dry air)
- h₂ = final enthalpy of air (Btu/lb dry air)
- ΔW = humidity ratio increase (lb H₂O/lb dry air)
- hg = enthalpy of saturated steam at atmospheric pressure (≈ 1150 Btu/lb)

**Steam Flow Rate:**

```
ṁsteam = ṁa × (W₂ - W₁)
```

Where:
- ṁsteam = steam flow rate (lb/hr)
- ṁa = dry air flow rate (lb/hr)
- W₂ - W₁ = humidity ratio increase (lb H₂O/lb dry air)

**Energy Input:**

```
Q̇steam = ṁa × (h₂ - h₁) = ṁsteam × hg
```

Where:
- Q̇steam = rate of energy addition (Btu/hr)
- hg = enthalpy of steam supplied (Btu/lb)

#### Steam Quality Considerations

| Steam Type | Temperature Impact | Control Characteristics | Application |
|-----------|-------------------|------------------------|-------------|
| Dry saturated steam | Minimal (isothermal) | Precise, rapid response | Clean steam applications, hospitals, food processing |
| Wet steam | Slight decrease | Variable moisture delivery | Not recommended - causes spitting |
| Superheated steam | Temperature increase | Predictable but adds sensible heat | Process applications requiring superheat |

**Clean Steam vs. Boiler Steam:**

- **Clean steam**: Generated from treated water, suitable for occupied spaces and sensitive processes
- **Boiler steam**: May contain chemical additives, volatile compounds; requires evaluation for indoor air quality impact
- ASHRAE Standard 188 requires assessment of steam source for Legionella risk

### Water Spray Humidification

Water spray humidification introduces liquid water droplets into the airstream. The droplets evaporate, absorbing latent heat from the air. This process is fundamentally adiabatic when water is supplied at the entering air wet-bulb temperature.

#### Adiabatic Humidification (Evaporative Cooling)

**Psychrometric Process Path:**
- Follows constant wet-bulb temperature line (constant enthalpy line approximately)
- Dry-bulb temperature decreases
- Humidity ratio increases
- Relative humidity increases
- Enthalpy remains approximately constant

**Process Equation:**

For ideal adiabatic saturation:

```
h₁ = h₂ (constant enthalpy)
```

```
T₁ + W₁ × hg₁ = T₂ + W₂ × hg₂
```

Where:
- T = dry-bulb temperature (°F)
- W = humidity ratio (lb H₂O/lb dry air)
- hg = enthalpy of saturated water vapor at respective temperature (Btu/lb)

**Practical Efficiency:**

Real spray humidifiers do not achieve perfect adiabatic saturation:

```
ε = (W₂ - W₁)/(Wsat,wb₁ - W₁)
```

Where:
- ε = saturation efficiency (typically 0.50 to 0.95)
- Wsat,wb₁ = humidity ratio at saturation at entering wet-bulb temperature
- W₁ = entering humidity ratio
- W₂ = leaving humidity ratio

| Spray System Type | Typical Efficiency | Droplet Size | Pressure |
|------------------|-------------------|--------------|----------|
| Low pressure spray | 50-70% | 100-200 microns | 20-40 psi |
| Medium pressure spray | 70-85% | 50-100 microns | 60-150 psi |
| High pressure atomizing | 85-95% | 10-50 microns | 200-1000 psi |
| Ultrasonic atomizing | 90-98% | 1-10 microns | N/A |

#### Non-Adiabatic Spray Humidification

When water temperature differs from the entering air wet-bulb temperature, the process deviates from the constant wet-bulb line:

**Heated Water Spray:**
- Water temperature > entering wet-bulb temperature
- Process path curves upward (adds both sensible and latent heat)
- Can increase or slightly decrease dry-bulb temperature depending on water temperature
- Increases humidity ratio
- Enthalpy increases

**Chilled Water Spray:**
- Water temperature < entering wet-bulb temperature
- Process path curves downward (removes sensible heat, adds moisture)
- Dry-bulb temperature decreases more than adiabatic process
- Increases humidity ratio
- Enthalpy may increase or decrease depending on conditions

**Energy Balance for Non-Adiabatic Spray:**

```
ṁa × h₂ = ṁa × h₁ + ṁw × hw
```

Where:
- ṁa = dry air mass flow rate (lb/hr)
- h₁, h₂ = air enthalpy entering and leaving (Btu/lb dry air)
- ṁw = water evaporated (lb/hr)
- hw = enthalpy of water supplied (Btu/lb)

For water enthalpy:
```
hw = cp,w × Tw ≈ 1.0 × Tw (Btu/lb)
```

Where:
- cp,w = specific heat of water ≈ 1.0 Btu/lb·°F
- Tw = water temperature (°F)

### Evaporative Media Humidification

Evaporative media (wetted pad) humidifiers pass air through water-saturated porous media. Water evaporates from the media surface into the airstream.

#### Process Characteristics

**Psychrometric Behavior:**
- Similar to adiabatic spray humidification
- Follows approximately constant wet-bulb temperature line
- Dry-bulb temperature decreases
- Humidity ratio increases
- Efficiency depends on media depth, face velocity, water distribution

**Saturation Effectiveness:**

```
εevap = (Tdb₁ - Tdb₂)/(Tdb₁ - Twb₁)
```

Where:
- εevap = evaporative effectiveness (decimal)
- Tdb₁ = entering dry-bulb temperature (°F)
- Tdb₂ = leaving dry-bulb temperature (°F)
- Twb₁ = entering wet-bulb temperature (°F)

| Media Type | Typical Effectiveness | Face Velocity | Pressure Drop |
|-----------|---------------------|---------------|---------------|
| Rigid cellulose pad (6" depth) | 80-90% | 400-600 fpm | 0.15-0.30 in. wg |
| Rigid cellulose pad (12" depth) | 90-95% | 400-600 fpm | 0.25-0.50 in. wg |
| Random fill media | 60-80% | 300-500 fpm | 0.10-0.25 in. wg |
| Structured polymer media | 70-85% | 400-700 fpm | 0.12-0.35 in. wg |

**Advantages:**
- Lower initial cost than steam
- Simultaneous cooling and humidification in heating season
- No chemical additives enter airstream
- Simple maintenance

**Limitations:**
- Requires water treatment to prevent mineral buildup and biological growth
- Not suitable for precise humidity control
- Cooling effect may be undesirable in some applications
- Freeze protection required in cold climates

## Psychrometric Process Analysis

### Humidification Process Lines

On the psychrometric chart, different humidification methods produce distinct process paths:

1. **Steam injection (isothermal)**: Horizontal line to the right
   - Constant Tdb
   - Increasing W, h, RH, Tdp

2. **Adiabatic evaporative**: Along constant Twb line (approximately constant enthalpy)
   - Decreasing Tdb
   - Increasing W, RH, Tdp
   - Approximately constant h

3. **Heated water spray**: Curved line upward
   - Variable Tdb (depends on water temperature)
   - Increasing W, h, RH, Tdp

### Example Calculation: Steam Humidification

**Given:**
- Air flow rate: 10,000 cfm
- Entering conditions: 70°F DB, 20% RH
- Desired leaving conditions: 70°F DB, 40% RH
- Steam supplied: dry saturated at atmospheric pressure

**From psychrometric chart at entering conditions:**
- W₁ = 0.0031 lb H₂O/lb dry air
- h₁ = 17.8 Btu/lb dry air
- v₁ = 13.34 ft³/lb dry air

**From psychrometric chart at leaving conditions:**
- W₂ = 0.0062 lb H₂O/lb dry air
- h₂ = 21.4 Btu/lb dry air

**Calculations:**

Dry air mass flow rate:
```
ṁa = Q/v₁ = 10,000 cfm / 13.34 ft³/lb = 750 lb/min = 45,000 lb/hr
```

Moisture addition:
```
ΔW = W₂ - W₁ = 0.0062 - 0.0031 = 0.0031 lb H₂O/lb dry air
```

Steam flow rate required:
```
ṁsteam = ṁa × ΔW = 45,000 × 0.0031 = 139.5 lb/hr
```

Energy addition rate:
```
Q̇ = ṁa × (h₂ - h₁) = 45,000 × (21.4 - 17.8) = 162,000 Btu/hr
```

Or equivalently:
```
Q̇ = ṁsteam × hg = 139.5 × 1150 = 160,425 Btu/hr ≈ 162,000 Btu/hr
```

### Example Calculation: Evaporative Media Humidification

**Given:**
- Same entering conditions: 70°F DB, 20% RH
- Evaporative media effectiveness: 85%
- Air flow rate: 10,000 cfm

**From psychrometric chart:**
- Entering: Tdb₁ = 70°F, Twb₁ = 46°F, W₁ = 0.0031 lb/lb
- At saturation at Twb₁ = 46°F: Wsat = 0.0066 lb/lb

**Humidity ratio increase:**
```
W₂ = W₁ + ε × (Wsat - W₁)
W₂ = 0.0031 + 0.85 × (0.0066 - 0.0031)
W₂ = 0.0031 + 0.00298 = 0.00608 lb/lb
```

**Temperature change:**
```
Tdb₂ = Tdb₁ - ε × (Tdb₁ - Twb₁)
Tdb₂ = 70 - 0.85 × (70 - 46)
Tdb₂ = 70 - 20.4 = 49.6°F
```

**Result:** Leaving conditions approximately 50°F DB, 0.00608 lb/lb

Note: Significant cooling occurs, which may require downstream reheating.

## Design Considerations

### System Selection Criteria

| Criterion | Steam Injection | Spray Humidification | Evaporative Media |
|----------|----------------|---------------------|-------------------|
| Initial cost | High | Medium | Low to Medium |
| Operating cost | High (energy) | Medium | Low (water, pump) |
| Response time | Fast (seconds) | Medium (minutes) | Slow (minutes) |
| Control accuracy | Excellent (±2-5% RH) | Good (±5-10% RH) | Fair (±10-15% RH) |
| Maintenance | Low | Medium (nozzles, filters) | High (media, water treatment) |
| Space requirement | Minimal | Medium | Large |
| Air temperature impact | Minimal | Significant cooling | Significant cooling |
| Water quality sensitivity | Low | High (mineral buildup) | High (scaling, biological) |
| Suitable for close-coupled | Yes | Limited | No |

### Steam Humidification Design

**Steam Source Selection:**

1. **Direct boiler steam**: Evaluate chemical treatment additives for indoor air quality
2. **Clean steam generator**: Dedicated unit for humidification, uses treated water
3. **Electric resistance steam**: On-demand generation, no boiler required

**Distribution System Design:**

- Manifold design for uniform steam distribution across duct cross-section
- Minimum duct length after injection: 15-20 duct diameters for complete evaporation
- Steam trap installation to remove condensate
- Modulating control valve with fast response actuator
- Separation distance from cooling coils to prevent condensation: minimum 10 ft

**Condensate Considerations:**

If steam condenses in duct:
- Creates moisture load on downstream surfaces
- Potential for microbial growth
- Requires condensate collection and drain
- May cause water hammer in ductwork

### Spray Humidification Design

**Nozzle Arrangement:**

- Multiple nozzles for uniform coverage
- Spacing: 12-24 inches on center
- Spray pattern: full cone or hollow cone
- Orientation: typically perpendicular to airflow

**Droplet Evaporation Distance:**

Required distance for complete evaporation depends on droplet size and air velocity:

```
Levap ≈ V × tevap
```

Where:
- Levap = evaporation distance (ft)
- V = air velocity (ft/s)
- tevap = evaporation time (s)

Typical evaporation distances:
- Low pressure spray: 8-12 ft
- High pressure spray: 4-8 ft
- Ultrasonic atomizing: 2-4 ft

**Eliminator Requirements:**

Install mist eliminators when:
- Complete evaporation cannot be guaranteed
- Downstream components sensitive to moisture
- Required efficiency > actual spray efficiency
- Typical pressure drop: 0.10-0.25 in. wg

### Evaporative Media Design

**Media Selection:**

Consider:
- Required effectiveness
- Available pressure drop budget
- Air velocity constraints
- Water quality and treatment program
- Maintenance access

**Water Distribution:**

- Uniform distribution across media face
- Recirculation pump sizing: 2-5 gpm per ft² of media face area
- Sump capacity: 3-5 minutes of recirculation flow
- Bleed-off rate: 10-20% of evaporation rate to control mineral concentration

**Freeze Protection:**

In cold climates:
- Automatic drain-down when system off
- Heat trace on water lines
- Sump heaters for exposed installations
- Isolation dampers to prevent cold air exposure

### Water Quality and Treatment

**Conductivity Management:**

Maximum cycles of concentration:
```
Cycles = TDS_max / TDS_makeup
```

Where:
- TDS = total dissolved solids (ppm)
- Typical maximum: 1500-2500 ppm before scaling risk

**Bleed-Off Rate:**

```
Bleed = Evap / (Cycles - 1)
```

Where:
- Bleed = bleed-off water flow rate
- Evap = evaporation rate
- Cycles = desired concentration cycles

**Treatment Considerations:**

- Softened water reduces scaling but increases sodium
- Reverse osmosis (RO) water ideal for spray humidification
- Biocide treatment for evaporative media systems
- UV sterilization for biological control
- Filtration: 5-25 micron for spray nozzles

### Controls and Sequencing

**Humidity Sensing:**

- Locate return air or space humidity sensor away from humidifier influence
- Provide averaging sensors for large spaces
- Calibration frequency: annually minimum
- Accuracy requirement: ±3-5% RH typical

**Control Strategies:**

1. **Proportional control**: Modulates humidifier output based on error signal
2. **PI control**: Adds integral action to eliminate offset
3. **High-limit cutout**: Prevents over-humidification (typically 60-70% RH)
4. **Low-limit cutout**: Stops humidification if supply air temperature too low (prevent condensation)

**Condensation Prevention:**

Disable humidification when:
```
Tdp,supply > Tsurface - 5°F
```

Where:
- Tdp,supply = dew point of supply air
- Tsurface = temperature of coldest downstream surface

**Sequencing with Other Equipment:**

- Disable during economizer cooling
- Reduce or disable during mechanical cooling
- Coordinate with preheat to prevent condensation in mixed air plenum
- Interlock with air-side economizer to prevent simultaneous cooling and humidification

## Health and Safety Considerations

### Legionella Prevention

ASHRAE Standard 188 and ASHRAE Guideline 12 provide guidance:

- Maintain water temperature > 140°F for steam generators or < 68°F for spray water storage
- Implement water treatment program
- Regular cleaning and disinfection (monthly to quarterly depending on system)
- Avoid stagnant water conditions
- Design for complete drainage

### Indoor Air Quality

**Volatile Compound Release:**

- Boiler steam may contain volatile treatment chemicals
- Clean steam or electric steam generators eliminate this concern
- Evaluate boiler water treatment chemicals for volatility and toxicity

**Mineral Dust:**

- Spray humidifiers using hard water can aerosolize minerals
- Results in white dust deposition
- Use treated water (RO, DI, or softened)

**Biological Contamination:**

- Evaporative media and spray systems can harbor bacteria, fungi
- Regular maintenance and water treatment essential
- Design for accessibility and cleanability

### Duct and Component Protection

**Condensation Control:**

Prevent condensation on duct surfaces:
- Insulate exterior ductwork
- Maintain supply air dew point below surface temperature
- Avoid humidification in cool supply air (< 55°F typical minimum)

**Material Compatibility:**

- Galvanized steel ductwork suitable for most applications
- Stainless steel in high-moisture areas or with aggressive water chemistry
- Avoid aluminum in contact with humidified air containing alkaline water

## Standards and References

### ASHRAE Standards and Guidelines

- **ASHRAE Standard 55**: Thermal Environmental Conditions for Human Occupancy
  - Recommended humidity range: 30-60% RH for comfort

- **ASHRAE Standard 62.1**: Ventilation for Acceptable Indoor Air Quality
  - No specific humidity requirements, but addresses moisture control

- **ASHRAE Standard 188**: Legionellosis: Risk Management for Building Water Systems
  - Requirements for humidification system water treatment and maintenance

- **ASHRAE Guideline 12**: Managing the Risk of Legionellosis Associated with Building Water Systems
  - Detailed guidance on humidification system design and operation

### Recommended Indoor Humidity Levels

| Application | Recommended RH Range | Notes |
|------------|---------------------|-------|
| Office buildings | 30-50% | ASHRAE 55 comfort range |
| Healthcare (general) | 30-60% | FGI Guidelines |
| Healthcare (surgical suites) | 20-60% | ASHRAE 170, varies by space type |
| Museums, archives | 40-55% | Collection-dependent, tight control |
| Data centers | 40-60% | ASHRAE TC 9.9 recommendations |
| Laboratories | 30-60% | Process-dependent |
| Printing facilities | 40-50% | Paper moisture content control |
| Manufacturing (electronics) | 30-50% | Static control, process requirements |

### Energy Code Compliance

**ASHRAE Standard 90.1 Requirements:**

- Section 6.5.2.4: Humidification systems
- Automatic shutoff when space unoccupied
- Modulating control of humidification capacity
- High-limit humidistat to prevent over-humidification
- Outdoor air damper position monitoring (no humidification during economizer operation)

**International Energy Conservation Code (IECC):**

- Similar requirements to ASHRAE 90.1
- Humidification setpoint limits in some climate zones

## Energy Efficiency Considerations

### Humidification Energy Consumption

Steam humidification energy (electric generation):
```
Energy = ṁsteam × hfg / ηsteam

Approximate: 1000 Btu/lb water = 0.293 kWh/lb water
```

For 100 lb/hr humidification:
- Steam energy: 100,000 Btu/hr = 29.3 kW
- Annual energy (6 month heating season): ~125,000 kWh

### Energy Recovery Opportunities

**Waste Heat Utilization:**

- Use waste heat from compressors, process equipment for steam generation
- Heat recovery from building exhaust for water preheating
- Combined heat and power (CHP) steam for humidification

**Adiabatic Economizing:**

- Use evaporative humidification during economizer operation
- Simultaneous free cooling and humidification
- Reduces or eliminates mechanical cooling load

### Load Reduction Strategies

1. **Envelope tightening**: Reduce infiltration of dry outdoor air
2. **Setpoint optimization**: Maintain minimum acceptable humidity, not excess
3. **Zoned humidification**: Humidify only areas requiring moisture control
4. **Outdoor air reduction**: Minimize ventilation air within code limits
5. **Heat recovery ventilation**: Recover moisture from exhaust air

## Conclusion

Humidification is a critical HVAC process for comfort, health, and process control in cold climates. The selection of humidification method depends on application requirements, energy considerations, installation constraints, and maintenance capabilities. Steam injection provides precise control with minimal space requirements but higher operating costs. Spray and evaporative systems offer lower operating costs but require more maintenance and produce significant cooling that may necessitate reheating.

Proper psychrometric analysis ensures appropriate system design, avoiding over-humidification, condensation, and energy waste. Careful attention to water quality, biological control, and indoor air quality impacts is essential for safe, effective humidification system operation. Compliance with ASHRAE standards and energy codes ensures appropriate performance while minimizing operational costs and health risks.
