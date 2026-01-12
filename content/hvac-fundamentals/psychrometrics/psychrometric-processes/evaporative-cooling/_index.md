---
title: "Evaporative Cooling"
description: "Comprehensive technical analysis of evaporative cooling processes, including direct and indirect systems, wet bulb effectiveness, psychrometric analysis, and engineering design calculations for HVAC applications."
weight: 7
---

## Overview

Evaporative cooling utilizes the thermodynamic principle of evaporative heat transfer to reduce air temperature through the phase change of water from liquid to vapor. This adiabatic process transfers sensible heat from the air to provide the latent heat required for water evaporation, resulting in decreased dry bulb temperature and increased moisture content in direct systems, or sensible cooling without moisture addition in indirect configurations.

The fundamental physics governing evaporative cooling derives from the First Law of Thermodynamics applied to an open system. The enthalpy change equals zero for adiabatic evaporative cooling processes, meaning total heat content remains constant while sensible heat converts to latent heat.

### Physical Principles

The evaporative cooling process occurs when air passes through or over water surfaces with sufficient contact area and residence time. Water molecules at the liquid-air interface absorb energy from the air stream, increasing their kinetic energy until vapor pressure equals or exceeds ambient partial pressure, allowing phase transition to vapor.

**Key thermodynamic relationships:**

- Energy absorbed per unit mass of water evaporated equals the latent heat of vaporization (approximately 1,055 Btu/lb or 2,454 kJ/kg at standard conditions)
- Maximum achievable cooling corresponds to the difference between entering dry bulb and wet bulb temperatures
- Adiabatic saturation process follows constant enthalpy lines on the psychrometric chart
- Effectiveness determines the fraction of theoretical maximum cooling achieved

## Psychrometric Analysis

On the psychrometric chart, direct evaporative cooling processes follow a path of constant wet bulb temperature (constant enthalpy), moving from the entering air condition toward the saturation curve. The process line slopes downward and to the right, indicating decreasing dry bulb temperature and increasing humidity ratio.

**Process characteristics:**

- Dry bulb temperature decreases
- Wet bulb temperature remains constant (theoretically)
- Humidity ratio increases
- Relative humidity increases
- Specific enthalpy remains constant (ideal adiabatic process)
- Dew point temperature increases

The theoretical limit of direct evaporative cooling is the wet bulb temperature of the entering air. Practical systems achieve 70-95% of this theoretical maximum, depending on media efficiency, air velocity, and contact time.

## Direct Evaporative Cooling

Direct evaporative cooling systems bring air into direct contact with water, either through spray chambers, wetted media pads, or atomizing nozzles. The air stream absorbs moisture while its temperature decreases along a constant wet bulb line.

### Wet Bulb Effectiveness

Wet bulb effectiveness (also called saturation effectiveness or direct evaporative cooler efficiency) quantifies actual performance relative to theoretical maximum:

**Effectiveness equation:**

```
ε_wb = (T_db,in - T_db,out) / (T_db,in - T_wb,in)
```

Where:
- ε_wb = Wet bulb effectiveness (dimensionless, 0 to 1.0)
- T_db,in = Entering dry bulb temperature (°F or °C)
- T_db,out = Leaving dry bulb temperature (°F or °C)
- T_wb,in = Entering wet bulb temperature (°F or °C)

**Typical effectiveness values:**

| Media Type | Effectiveness Range | Face Velocity Limit |
|------------|---------------------|---------------------|
| Rigid cellulose media (6-12 in thick) | 0.80 - 0.95 | 200-400 fpm |
| Aspen wood fiber pads | 0.70 - 0.85 | 200-250 fpm |
| Spray chamber (vertical) | 0.60 - 0.80 | 400-600 fpm |
| Atomizing nozzles (fine mist) | 0.70 - 0.90 | Variable |
| Wetted rotating disc | 0.65 - 0.75 | 300-500 fpm |

### Design Calculations

**Temperature drop calculation:**

```
ΔT = ε_wb × (T_db,in - T_wb,in)
```

**Humidity ratio change:**

The increase in humidity ratio can be calculated from psychrometric relationships or energy balance:

```
Δω = (h_out - h_in) / h_fg
```

Where h_fg is the latent heat of vaporization at the average process temperature.

**Water consumption:**

```
ṁ_water = ṁ_air × Δω
```

Where:
- ṁ_water = Water evaporation rate (lb/hr or kg/hr)
- ṁ_air = Dry air mass flow rate (lb/hr or kg/hr)
- Δω = Change in humidity ratio (lb_water/lb_air or kg_water/kg_air)

For volumetric flow rate:

```
ṁ_air = Q × ρ_air = Q / v
```

Where Q is volumetric flow rate (cfm or m³/hr) and v is specific volume.

### Media Types and Performance

**Rigid cellulose media:**

The most efficient direct evaporative cooling media consists of cross-fluted cellulose sheets bonded together to form a rigid honeycomb structure. Media thickness ranges from 4 to 12 inches, with thicker media providing higher effectiveness but increased pressure drop.

- Pressure drop: 0.15-0.40 in. w.g. at design velocity
- Service life: 5-10 years with proper maintenance
- Requires continuous water distribution system
- Self-cleaning action with adequate water flow rates

**Aspen wood fiber pads:**

Traditional evaporative cooling media consisting of aspen wood shavings compressed into pads, typically 1-4 inches thick.

- Lower cost than rigid media
- Shorter service life (1-3 years)
- Effectiveness decreases as pads age and compress
- Requires periodic replacement

### Application Limitations

Direct evaporative cooling effectiveness depends on climate conditions. The process works optimally in hot, dry climates where significant wet bulb depression exists.

**Climate suitability assessment:**

| Climate Classification | Wet Bulb Depression | Application Suitability |
|------------------------|---------------------|-------------------------|
| Hot-Arid (Desert) | >30°F (>17°C) | Excellent - Primary cooling |
| Hot-Dry (Semi-arid) | 20-30°F (11-17°C) | Good - Primary or supplemental |
| Warm-Moderate | 15-20°F (8-11°C) | Fair - Supplemental only |
| Hot-Humid | <15°F (<8°C) | Poor - Not recommended |

**Design considerations:**

- Maximum acceptable discharge relative humidity (typically 70-80%)
- Occupant comfort requirements and activity levels
- Ventilation air requirements and outdoor air percentages
- Water quality and treatment requirements
- Legionella prevention strategies
- Mineral buildup and scaling potential
- Blowdown requirements for mineral control

## Indirect Evaporative Cooling

Indirect evaporative cooling systems provide sensible cooling without adding moisture to the supply air stream. A heat exchanger separates the primary (supply) air from secondary (scavenger) air that undergoes direct evaporative cooling. Heat transfers from the warm primary air to the cooled secondary air through the heat exchanger surfaces.

### Operating Principles

The indirect evaporative cooling process occurs in two stages:

1. **Primary air side:** Air to be cooled flows through one side of a heat exchanger. Temperature decreases through sensible heat transfer to the heat exchanger surfaces. No moisture is added to this air stream.

2. **Secondary air side:** Outdoor air or exhaust air flows through the opposite side of the heat exchanger while undergoing direct evaporative cooling. The cooled, saturated air absorbs heat from the heat exchanger surfaces and is then exhausted to atmosphere.

### Wet Bulb Approach

For indirect systems, effectiveness is defined relative to the wet bulb approach temperature:

**Indirect evaporative cooler effectiveness:**

```
ε_IEC = (T_db,in - T_db,out) / (T_db,in - T_wb,sec)
```

Where:
- ε_IEC = Indirect evaporative cooler effectiveness (dimensionless)
- T_db,in = Primary air entering dry bulb temperature
- T_db,out = Primary air leaving dry bulb temperature
- T_wb,sec = Secondary air entering wet bulb temperature

Typical indirect evaporative cooler effectiveness ranges from 0.40 to 0.75, depending on heat exchanger configuration, air velocities, and secondary air evaporative effectiveness.

### Heat Exchanger Configurations

**Plate-type heat exchangers:**

Parallel flat plates with alternating primary and secondary air passages. Evaporative cooling occurs on the secondary air side through wetted surfaces or spray systems.

- Effectiveness: 0.50-0.70
- Pressure drop: 0.3-0.8 in. w.g. per side
- Compact footprint
- Suitable for rooftop applications

**Tubular heat exchangers:**

Primary air flows inside tubes while evaporatively cooled secondary air flows across the exterior surfaces.

- Effectiveness: 0.40-0.60
- Higher pressure drop on tube side
- Easy to clean and maintain
- Suitable for high-pressure applications

**Rotating heat wheels (with evaporative section):**

Hybrid systems incorporating both sensible heat recovery and evaporative cooling through sectored wheel designs.

## Two-Stage Evaporative Cooling

Two-stage evaporative cooling systems combine indirect evaporative cooling (first stage) followed by direct evaporative cooling (second stage), achieving lower supply air temperatures than either system alone.

### System Configuration

**Stage 1 - Indirect evaporative cooling:**
- Primary air temperature reduces from T1 to T2
- No moisture addition to primary air
- Primary air dry bulb approaches secondary air wet bulb

**Stage 2 - Direct evaporative cooling:**
- Primary air from Stage 1 undergoes direct evaporative cooling
- Temperature reduces from T2 to T3 along constant wet bulb line
- Moisture added to primary air stream

**Overall effectiveness:**

The combined effectiveness of a two-stage system can be calculated as:

```
ε_total = ε_IEC + ε_DEC × (1 - ε_IEC)
```

Where:
- ε_total = Overall two-stage effectiveness
- ε_IEC = Indirect stage effectiveness
- ε_DEC = Direct stage effectiveness (based on Stage 1 outlet conditions)

**Typical performance:**

| Configuration | Overall Effectiveness | Supply Air Condition |
|---------------|----------------------|----------------------|
| Indirect only | 0.50-0.75 | T_db decreased, ω constant |
| Direct only | 0.70-0.95 | T_db decreased, ω increased |
| Two-stage | 0.90-1.20 | T_db greatly decreased, ω increased |

Note: Two-stage effectiveness can exceed 1.0 when referenced to the original entering wet bulb temperature, as the first stage reduces the dry bulb temperature, establishing a new reference point for the second stage.

### Temperature Calculation Example

**Given conditions:**
- Entering air: 95°F DB, 65°F WB
- Indirect stage effectiveness: 0.60
- Direct stage effectiveness: 0.85

**Stage 1 (Indirect) calculation:**

```
ΔT_1 = 0.60 × (95 - 65) = 18°F
T_2 = 95 - 18 = 77°F DB, 65°F WB (approx.)
```

**Stage 2 (Direct) calculation:**

From psychrometric chart, determine new wet bulb at 77°F DB with constant enthalpy from original condition. For this example, assume T_wb,2 ≈ 64°F.

```
ΔT_2 = 0.85 × (77 - 64) = 11°F
T_3 = 77 - 11 = 66°F DB
```

**Overall performance:**
- Total temperature reduction: 95 - 66 = 29°F
- Overall effectiveness: 29/(95-65) = 0.97

## Saturation Effectiveness

Saturation effectiveness represents the degree to which air approaches saturation conditions after passing through an evaporative cooling device. This metric is particularly relevant for direct evaporative cooling systems and spray chambers.

**Saturation effectiveness equation:**

```
ε_sat = (ω_out - ω_in) / (ω_sat - ω_in)
```

Where:
- ε_sat = Saturation effectiveness (dimensionless)
- ω_out = Leaving air humidity ratio (lb/lb or kg/kg)
- ω_in = Entering air humidity ratio (lb/lb or kg/kg)
- ω_sat = Saturated air humidity ratio at entering wet bulb temperature (lb/lb or kg/kg)

For ideal adiabatic evaporative cooling processes, saturation effectiveness equals wet bulb effectiveness. In practice, saturation effectiveness may differ slightly due to non-adiabatic conditions, heat gain from pumps and fans, and incomplete evaporation of water droplets.

## Engineering Design Considerations

### Water Quality and Treatment

Water quality significantly impacts evaporative cooling system performance, maintenance requirements, and longevity.

**Critical water quality parameters:**

| Parameter | Acceptable Range | Impact if Exceeded |
|-----------|------------------|-------------------|
| Total Dissolved Solids (TDS) | <1,500 ppm | Scaling, white dust formation |
| pH | 6.5-8.5 | Corrosion or scaling |
| Total Hardness (as CaCO₃) | <200 ppm | Mineral deposits on media |
| Chlorides | <200 ppm | Corrosion of metal components |
| Silica | <50 ppm | Hard scale deposits |
| Total Alkalinity | <200 ppm | Carbonate scaling |

**Water treatment strategies:**

- Bleed-off/blowdown to control mineral concentration
- Chemical treatment for scale and biological control
- Water softening for high hardness conditions
- Filtration to remove suspended solids
- UV sterilization for biological control

**Blowdown calculation:**

```
Blowdown Rate = Evaporation Rate / (Cycles of Concentration - 1)
```

Cycles of concentration typically range from 3 to 8, depending on water quality and treatment approach.

### Pressure Drop Analysis

Total system pressure drop includes media pressure drop, distributor/nozzle pressure drop, and eliminator pressure drop (if installed).

**Media pressure drop correlation:**

```
ΔP = K × (V/1000)^n
```

Where:
- ΔP = Pressure drop (in. w.g.)
- K = Media coefficient (manufacturer-specific)
- V = Face velocity (fpm)
- n = Exponent (typically 1.8-2.0 for turbulent flow)

**Design velocity selection:**

Lower velocities improve effectiveness but require larger media areas. Higher velocities reduce equipment size but decrease effectiveness and increase pressure drop.

Optimal design velocities:
- Rigid cellulose media: 250-350 fpm
- Aspen pads: 200-250 fpm
- Spray chambers: 400-500 fpm

### Airflow Distribution

Uniform airflow distribution across media surfaces maximizes effectiveness and prevents channeling, dry spots, and premature media degradation.

**Distribution requirements:**
- Velocity variation across media face: ±15% maximum
- Adequate upstream straight duct length: 3-5 duct diameters minimum
- Turning vanes in upstream elbows to reduce swirl
- Perforated plate or baffle upstream of media for flow straightening

### Water Distribution Systems

Proper water distribution ensures complete media wetting and optimal evaporative efficiency.

**Distribution methods:**

1. **Gravity trough distribution:** Water overflows from perforated or slotted distribution troughs positioned above media. Requires precise leveling.

2. **Pressurized spray systems:** Nozzles spray water onto media surfaces. Allows uneven installation but requires pump pressure (5-15 psi).

3. **Flooded media systems:** Water pumped to top of media, flowing down through media cross-section by gravity.

**Water flow rates:**

Media wetting requires minimum water flow rates to maintain complete surface coverage:

- Rigid cellulose media: 0.3-0.5 gpm per linear foot of distribution
- Aspen pads: 0.2-0.4 gpm per linear foot
- Spray chambers: 1.5-3.0 gpm per cfm of air flow (for effective droplet formation)

## ASHRAE Design Guidance

**ASHRAE Handbook - HVAC Systems and Equipment, Chapter 40** provides comprehensive design information for evaporative cooling systems, including:

- Psychrometric analysis methods
- Equipment selection criteria
- Water treatment recommendations
- Maintenance requirements
- Application guidelines by climate zone

**ASHRAE Standard 90.1 - Energy Standard for Buildings:**

Evaporative cooling systems can contribute to energy code compliance through:
- Reduced mechanical cooling energy consumption
- Economizer operation enhancement
- Integration with indirect/direct evaporative cooling for pre-cooling
- Demand-controlled ventilation with evaporative cooling

**ASHRAE Standard 62.1 - Ventilation for Acceptable Indoor Air Quality:**

Requirements for evaporative cooling systems include:
- Prevention of stagnant water conditions
- Drainage and cleaning provisions
- Drift eliminator installation where carryover could impact occupants
- Water treatment to prevent microbial growth

## Control Strategies

Effective control systems optimize evaporative cooling performance while minimizing water consumption and energy use.

### Staging and Sequencing

**Single-stage direct evaporative cooling:**
- On/off control based on space temperature or discharge temperature
- Water pump interlocked with supply fan
- Freeze protection for outdoor installations

**Two-stage evaporative cooling:**
- Stage 1 (indirect) operates first when cooling required
- Stage 2 (direct) adds cooling capacity as needed
- Humidity limit override to prevent over-humidification
- Temperature-based staging with dead bands

### Optimization Controls

**Wet bulb economizer control:**
- Monitor outdoor wet bulb temperature
- Enable evaporative cooling when outdoor wet bulb < indoor temperature setpoint - offset
- Disable when wet bulb approaches indoor dew point to prevent condensation

**Discharge air temperature control:**
- Modulate water flow rate to control leaving air temperature
- Faster response than on/off control
- Requires modulating valve and variable frequency drive on recirculation pump

**Indoor humidity limiting:**
- Disable direct evaporative cooling when indoor RH exceeds setpoint (typically 60-65%)
- Prevent moisture-related issues in building envelope and contents

## Energy Performance Analysis

Evaporative cooling systems offer significant energy savings compared to vapor compression air conditioning in suitable climates.

**Energy consumption comparison (per ton-hour of cooling):**

| System Type | Electrical Consumption | Approximate kWh/ton-hr |
|-------------|------------------------|------------------------|
| Direct evaporative cooling | Fan + pump only | 0.15-0.35 |
| Indirect evaporative cooling | Fans + pumps (primary + secondary) | 0.30-0.60 |
| Two-stage evaporative | Fans + pumps | 0.40-0.75 |
| Standard DX air conditioning | Compressor + fan | 1.0-1.5 |
| Centrifugal chiller + pumps | Chiller + pumps + cooling tower | 0.6-1.0 |

**Energy savings calculation:**

```
Annual Energy Savings = (kWh_baseline - kWh_evaporative) × Cooling Hours × Utility Rate
```

Account for climate-specific operating hours, part-load performance, and hybrid system operation when comparing alternatives.

### Life Cycle Cost Analysis

Complete economic analysis includes:
- Initial equipment and installation costs
- Annual energy costs (electricity and water)
- Maintenance costs (media replacement, cleaning, water treatment)
- Replacement costs over analysis period
- Present worth calculations at appropriate discount rate

Direct evaporative cooling typically shows 2-5 year simple payback in suitable climates when replacing mechanical cooling, primarily due to energy savings.

## Installation and Commissioning

### Installation Requirements

**Structural considerations:**
- Support for equipment weight plus water in sump (8.34 lb/gal)
- Vibration isolation for rotating equipment
- Access for media replacement and maintenance
- Drainage provisions for blowdown and overflow

**Piping and drainage:**
- Makeup water connection with backflow preventer
- Overflow drain sized for maximum fill valve flow rate
- Blowdown drain connection
- Drip pan or curb beneath equipment for leak containment

**Electrical:**
- Pump and fan motor circuits with appropriate overcurrent protection
- Control power supply
- Interlock with supply fan (pumps off when fan off)
- Freeze protection thermostats for outdoor installations

### Commissioning Procedures

**Pre-functional checklists:**
- Verify proper rotation of pumps and fans
- Confirm water distribution uniformity across all media
- Check for leaks in water distribution system
- Verify control sequences and interlocks

**Functional performance testing:**
- Measure entering and leaving air conditions (DB, WB, RH) at design airflow
- Calculate actual effectiveness and compare to design
- Verify water consumption rates
- Document pressure drops across all components
- Test control sequences under various load conditions

**Performance acceptance criteria:**
- Wet bulb effectiveness within 5% of design value
- Airflow within ±10% of design
- Water distribution uniform (no dry spots visible)
- All control sequences operate correctly

## Maintenance Requirements

### Routine Maintenance Tasks

**Pre-season (annual):**
- Inspect and clean sump and reservoir
- Replace or clean media (per manufacturer recommendations)
- Check water distribution system for clogs or damage
- Lubricate pumps and fan bearings
- Verify proper operation of makeup water valve and controls
- Test blowdown system
- Calibrate sensors and controls

**Monthly (during cooling season):**
- Visual inspection of media for biological growth or mineral buildup
- Check water quality (TDS, pH)
- Adjust blowdown rate if needed
- Verify uniform water distribution
- Inspect eliminator plates (if installed) for carryover

**Weekly:**
- Check sump water level and makeup water operation
- Visual inspection for unusual operation or sounds
- Verify control operation

### Media Replacement

Media replacement frequency depends on water quality, operating hours, and maintenance practices:

- Rigid cellulose media: 5-10 years typical service life
- Aspen pads: 1-3 years typical service life
- Consider replacement when effectiveness decreases >10% or visible degradation occurs

## Hybrid and Advanced Systems

### Evaporative Condenser Pre-cooling

Outdoor air can be evaporatively cooled before entering air-cooled condensers, improving refrigeration cycle efficiency.

**Benefits:**
- Reduced condensing temperature and pressure
- Increased cooling capacity
- Reduced compressor energy consumption
- Extended equipment life

**Condensing temperature reduction:**

```
ΔT_cond = ε_wb × (T_db,ambient - T_wb,ambient) × Effectiveness_factor
```

Where Effectiveness_factor accounts for heat exchanger performance (typically 0.6-0.8).

### Desiccant-Enhanced Evaporative Cooling

Combining desiccant dehumidification with evaporative cooling enables effective cooling in humid climates.

**Process sequence:**
1. Desiccant dehumidification lowers air humidity ratio
2. Dehumidified air undergoes evaporative cooling
3. Lower humidity ratio enables greater evaporative cooling effectiveness

This hybrid approach extends evaporative cooling viability to hot-humid climates where direct evaporative cooling alone proves ineffective.

### Indirect-Direct Evaporative Cooling with Energy Recovery

Advanced systems integrate energy recovery with two-stage evaporative cooling:
- Heat recovery from exhaust air pre-cools outdoor air
- Indirect evaporative cooling provides additional sensible cooling
- Direct evaporative cooling provides final temperature reduction
- Overall system effectiveness >1.5 achievable

## Health and Safety Considerations

### Legionella Prevention

Evaporative cooling systems can support Legionella bacteria growth if not properly designed, operated, and maintained.

**Prevention strategies:**
- Maintain water temperature >140°F or <68°F where possible
- Ensure complete system drainage when not in operation
- Implement regular cleaning and disinfection protocols
- Use biocides or other water treatment
- Eliminate dead legs and stagnant water zones
- Maintain adequate blowdown to prevent nutrient accumulation

**Reference:** ASHRAE Guideline 12-2020, Managing the Risk of Legionellosis Associated with Building Water Systems

### Water Carryover Prevention

Drift eliminators prevent water droplet carryover into supply air streams, reducing moisture damage risk and mineral deposition in ductwork.

**Eliminator specifications:**
- Removal efficiency: >95% for droplets >50 microns
- Pressure drop: 0.05-0.15 in. w.g.
- Face velocity limit: 500-700 fpm

## Climate-Specific Design Recommendations

### Hot-Arid Climates (ASHRAE Climate Zones 2B, 3B)

- Direct evaporative cooling viable as primary cooling system
- Design wet bulb effectiveness: 0.80-0.90
- Consider two-stage systems for commercial applications requiring lower humidity
- Size for peak afternoon conditions (highest DB, lowest RH)

### Hot-Dry Climates (ASHRAE Climate Zones 3B, 4B)

- Direct evaporative cooling suitable for industrial and some commercial applications
- Consider indirect evaporative cooling for spaces with humidity concerns
- Hybrid systems combining evaporative and mechanical cooling optimize energy use
- Design for 2-3% cooling design conditions

### Moderate Climates (ASHRAE Climate Zones 3C, 4C)

- Indirect evaporative cooling effective for pre-cooling outdoor air
- Integrate with economizer systems
- Two-stage systems provide supplemental cooling during peak periods
- Primary mechanical cooling typically required

### Humid Climates (Not Recommended for Primary Cooling)

- Limited to indirect evaporative cooling for condenser pre-cooling
- Possible use during low-humidity periods (winter/spring in some locations)
- Focus on energy recovery and mechanical dehumidification

## Summary

Evaporative cooling represents an energy-efficient cooling technology applicable in climates with adequate wet bulb depression. Direct systems achieve high effectiveness (0.70-0.95) with minimal energy consumption but add moisture to supply air. Indirect systems provide sensible cooling without humidification at moderate effectiveness (0.40-0.75). Two-stage configurations combine both approaches, achieving overall effectiveness approaching or exceeding 1.0 relative to entering wet bulb temperature.

Successful evaporative cooling system design requires:
- Careful climate analysis and psychrometric evaluation
- Proper equipment selection based on performance requirements
- Adequate water treatment and quality management
- Comprehensive maintenance programs
- Appropriate control strategies
- Integration with building HVAC systems

When properly applied, evaporative cooling systems deliver 60-85% energy savings compared to vapor compression cooling while maintaining acceptable thermal comfort conditions.
