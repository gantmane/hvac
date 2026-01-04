---
title: "Dehumidification System Design"
weight: 3
description: "Comprehensive analysis of natatorium dehumidification systems including mechanical refrigeration, desiccant, and heat recovery approaches with equipment sizing, psychrometric processes, and energy performance optimization."
keywords: "pool dehumidification, natatorium HVAC equipment, heat recovery dehumidifier, mechanical dehumidification, desiccant systems, pool HVAC sizing"
---

Dehumidification system design represents the core technical challenge in natatorium HVAC engineering. The system must continuously remove massive quantities of moisture (often 50-150 lb/h for typical pools) while maintaining precise humidity control, providing thermal comfort, and operating efficiently across varying loads and outdoor conditions.

## System Selection Criteria

Selection of dehumidification approach depends on multiple factors:

**Climate**: Cold climates favor heat recovery systems that can utilize recovered heat year-round. Hot-humid climates may benefit from mechanical systems with separate heat rejection. Dry climates can sometimes use outdoor air economizers seasonally.

**Pool Size and Type**: Large competitive pools (>2,000 ft²) typically justify sophisticated heat recovery systems. Smaller residential or therapy pools may use simpler mechanical dehumidification. High-use facilities with heavy evaporation loads require robust commercial-grade equipment.

**Energy Costs**: High energy costs favor maximum heat recovery integration. Low energy costs may allow simpler systems with less capital investment.

**Building Integration**: Retrofit applications may face space constraints favoring compact packaged equipment. New construction allows optimization of equipment locations and ductwork distribution.

**Operating Schedule**: Continuous-use facilities (hotels, fitness centers) benefit from steady-state heat recovery. Intermittent-use facilities (schools, community centers) may need rapid capacity modulation.

## Mechanical Refrigeration Dehumidification

Conventional mechanical dehumidification uses direct-expansion or chilled water cooling coils to reduce air temperature below its dewpoint, condensing moisture. The cooled, dehumidified air typically requires reheat before discharge to maintain space temperature.

### Psychrometric Process

The mechanical dehumidification process follows a standard cooling and dehumidification path on the psychrometric chart:

1. **Pool air intake** at design conditions (82°F, 60% RH, humidity ratio ≈ 0.0113 lb_w/lb_da)
2. **Cooling/dehumidification** to apparatus dewpoint (typically 55-60°F, near saturation)
3. **Reheat** to supply air temperature (typically 80-85°F for pool deck discharge)

The apparatus dewpoint must be sufficiently low to achieve the required moisture removal rate. For a pool evaporating 100 lb/h of water with 10,000 cfm air circulation:

Required humidity ratio reduction:
Δω = 100 lb/h / (10,000 cfm × 60 min/h × 0.075 lb/ft³) = 0.0022 lb_w/lb_da

If return air is at ω = 0.0113 lb_w/lb_da, supply air must be at ω = 0.0091 lb_w/lb_da.

At 82°F supply temperature, this corresponds to approximately 45% RH—requiring an apparatus dewpoint of approximately 58-60°F when accounting for coil bypass factor.

### Equipment Configuration

**Direct Expansion Systems**:
- Packaged DX dehumidifiers with integral refrigeration circuit
- Air-cooled condensers reject heat outdoors
- Electric or hot water reheat coils
- Simple controls, moderate first cost
- Limited heat recovery opportunity (only condensate sensible heat)

**Chilled Water Systems**:
- Central chiller plant produces chilled water (42-48°F typical)
- Cooling coils in air handlers or dehumidification units
- Separate reheat system (boiler, heat pump, electric)
- Allows centralized efficiency optimization
- Higher first cost, more complex controls
- Feasible for large facilities or multiple pools

### Sizing Procedure

**Step 1: Calculate Design Latent Load**

From evaporation calculation: W = evaporation rate (lb/h)

Latent load: Q_latent = W × 1,040 Btu/lb

**Step 2: Determine Air Circulation Rate**

Minimum air circulation is often governed by:
- Code-required ventilation rates (typically 0.5-1.0 air changes per hour minimum)
- Air distribution requirements for comfort
- Dehumidification effectiveness

Typical range: 6-12 air changes per hour for pool area
For 60,000 ft³ pool enclosure: 6,000-12,000 cfm

**Step 3: Calculate Required Moisture Removal**

Δω = W / (cfm × 60 × 0.075) lb_w/lb_da

**Step 4: Determine Apparatus Dewpoint**

Based on required Δω and supply air conditions, select apparatus dewpoint (ADP). Account for coil bypass factor (typically 0.05-0.15 for well-designed coils).

**Step 5: Calculate Cooling Capacity**

Total cooling = sensible cooling + latent cooling

Sensible: Q_s = 1.08 × cfm × ΔT

Latent: Q_l = 0.68 × cfm × Δω (where Δω in grains/lb)

Or: Q_l = 4,840 × cfm × Δω (where Δω in lb_w/lb_da)

Total: Q_total = Q_s + Q_l

**Step 6: Calculate Reheat Requirement**

If supply air after cooling is too cold for comfort:

Q_reheat = 1.08 × cfm × (T_supply - T_coil_leaving)

### Energy Penalty

Simple mechanical dehumidification without heat recovery suffers severe energy penalty:

- Cooling energy to condense moisture: ~15,000 Btu/lb_water (includes sensible + latent)
- Reheat energy to restore comfort temperature: ~5,000-10,000 Btu/lb_water
- Total energy: 20,000-25,000 Btu per lb of water removed

For 100 lb/h evaporation: 2,000,000-2,500,000 Btu/h = 167-208 MBH

This energy consumption is rarely economically acceptable, driving adoption of heat recovery systems.

## Heat Recovery Dehumidification

Heat recovery dehumidifiers integrate the refrigeration cycle to simultaneously cool/dehumidify and heat pool water or reheat air. This approach recovers 50-70% of energy compared to simple mechanical systems.

### Operating Principle

The refrigeration cycle condenser heat (normally rejected to outdoor air or cooling tower) is instead used productively:

1. **Evaporator** cools and dehumidifies pool air (removes moisture + sensible heat)
2. **Compressor** elevates refrigerant temperature and pressure
3. **Condenser** rejects heat to pool water, domestic hot water, or air reheat coil
4. **Expansion device** reduces refrigerant pressure, completing cycle

Energy balance: Heat rejected at condenser ≈ Heat absorbed at evaporator + Compressor work

Typical COP (coefficient of performance) for dehumidification: 3.0-4.5

This means 3-4.5 units of useful heating for each unit of electrical input.

### Heat Recovery Applications

**Pool Water Heating**:
- Refrigerant-to-water heat exchanger (brazed plate or tube-in-tube)
- Condenser water circulates through pool heat exchanger
- Provides 60-100% of pool heating load in well-designed systems
- Water temperature typically limited to 85-95°F to maintain adequate condensing temperature difference

**Domestic Hot Water Preheating**:
- Desuperheater or full condenser heat to DHW tank
- Preheat from 50-60°F to 90-110°F
- Auxiliary heater (gas, electric, boiler) provides final heating to 120-140°F
- Excellent application for facilities with simultaneous pool and shower demand

**Air Reheat**:
- Hot gas or refrigerant-to-air heat exchanger
- Provides reheat for supply air stream
- Essential for maintaining comfort during dehumidification
- Most systems combine air reheat with pool water heating for maximum flexibility

### Typical Performance

| Parameter | Value |
|-----------|-------|
| Dehumidification capacity | 50-200 lb/h (standard units) |
| Air circulation | 5,000-20,000 cfm |
| Pool water heating | 200-800 MBH |
| Electrical input | 40-150 kW |
| Overall COP | 3.5-5.0 |
| Heat recovery efficiency | 60-75% |

**Example Calculation**:

Pool with 100 lb/h evaporation at 1,040 Btu/lb = 104,000 Btu/h latent load

Heat recovery dehumidifier:
- Evaporator load (cooling): 120,000 Btu/h (latent + sensible)
- Compressor input: 35,000 Btu/h (equivalent of 10.3 kW electrical)
- Condenser heat available: 155,000 Btu/h
- Pool water heating recovery: 130,000 Btu/h (80% to pool)
- Air reheat: 25,000 Btu/h (20% to air)

Net energy consumption: 35,000 Btu/h electrical input

Compare to mechanical dehumidification without heat recovery:
- Cooling: 120,000 Btu/h
- Reheat: 60,000 Btu/h
- Total: 180,000 Btu/h

Energy savings: (180,000 - 35,000) / 180,000 = 80.6%

## Desiccant Dehumidification

Desiccant systems use hygroscopic materials to absorb moisture chemically rather than condensing it through cooling. Solid desiccant wheels or liquid desiccant spray systems can achieve very low humidity levels and work effectively at low temperatures where mechanical systems struggle.

### Solid Desiccant Systems

Rotating desiccant wheel continuously cycles between adsorption and regeneration:

**Process Stream**:
1. Humid pool air passes through desiccant wheel
2. Moisture adsorbs onto desiccant (silica gel, molecular sieve)
3. Temperature rises due to heat of adsorption (typically 10-15°F)
4. Dry, warm air requires cooling before discharge

**Regeneration Stream**:
1. Heated regeneration air (140-200°F) passes through opposite sector of wheel
2. Heat drives moisture out of desiccant
3. Hot, humid regeneration air exhausted outdoors
4. Desiccant returns to process stream, ready to adsorb

### Liquid Desiccant Systems

Lithium chloride (LiCl) or lithium bromide (LiBr) solution sprayed through process air stream:

1. Strong (concentrated) desiccant solution absorbs moisture from air
2. Weak (diluted) solution is regenerated by heating
3. Heat drives water out of solution
4. Concentrated solution returns to absorber

### Desiccant System Advantages

- Deep dehumidification (can achieve <30°F dewpoint)
- Effective at low temperatures (mechanical systems lose capacity below 50°F)
- Separate control of temperature and humidity
- Potential for heat-activated regeneration (gas, waste heat, solar)

### Desiccant System Disadvantages

- High regeneration energy requirement (1,500-2,000 Btu/lb_water removed)
- Requires cooling to offset heat of adsorption
- Higher maintenance (desiccant wheel replacement, solution management)
- Generally higher first cost than mechanical systems

### Natatorium Applications

Desiccant systems are rarely used as primary dehumidification for standard pools due to high regeneration energy. Specific applications include:

- Cold climate indoor pools where mechanical systems struggle in winter
- Extremely low humidity requirements (competitive diving, gymnastics)
- Integration with available waste heat source
- Hybrid systems combining mechanical and desiccant stages

## Hybrid Systems

Many modern natatorium installations use hybrid approaches:

**Heat Recovery + Outdoor Air Economizer**:
- Heat recovery dehumidifier for baseload
- Outdoor air intake during favorable conditions (cool, dry weather)
- Automatic changeover based on enthalpy comparison
- Maximizes free cooling when available

**Mechanical + Desiccant**:
- Mechanical system for bulk moisture removal
- Desiccant polishing stage for precise low-humidity control
- Used in competition facilities requiring <40% RH

**Multiple Units**:
- Several smaller units rather than single large unit
- Provides redundancy, maintenance flexibility
- Better part-load efficiency through staging
- Improved humidity control during low occupancy

## Controls and Sequencing

Dehumidification system controls must coordinate:

**Humidity Control**:
- Primary setpoint: 50-60% RH
- Deadband: ±5% to prevent cycling
- Discharge air high-limit dewpoint to prevent overcooling
- Demand-based capacity modulation (compressor staging, VFD, hot gas bypass)

**Temperature Control**:
- Space temperature setpoint based on pool water temperature + 2-4°F
- Reheat modulation to maintain supply air temperature
- Integration with auxiliary heating (if provided)

**Pool Water Heating**:
- Three-way valve modulates flow through pool water heat exchanger
- Maintains pool water setpoint (typically 78-84°F)
- Diverts excess heat to auxiliary applications (DHW, space heating) when pool is satisfied
- Protection against excessive pool water temperature

**Ventilation**:
- Minimum outdoor air damper position based on code requirements
- Economizer operation when outdoor conditions favorable
- CO₂ or occupancy-based demand control ventilation (where permitted)

**Safety**:
- High humidity alarm (>70% RH)
- Low temperature protection (freeze prevention)
- Refrigerant leak detection
- Equipment status monitoring

## Sizing Considerations

Conservative dehumidification sizing is critical to prevent humidity control problems:

- Size for peak evaporation with 20% safety factor
- Verify capacity at part-load conditions (ability to turndown)
- Ensure adequate capacity during high outdoor humidity (reduced condensing capacity)
- Consider simultaneous demands (special events, swim meets)
- Account for envelope infiltration during windy conditions

Undersized dehumidification equipment cannot be easily corrected after installation and leads to chronic humidity problems, condensation damage, and occupant complaints. Oversizing, while less problematic, results in short-cycling, poor humidity control, and reduced equipment life unless proper capacity modulation is provided.

## Performance Verification

Commission dehumidification systems thoroughly:

- Verify airflow rates (total and outdoor air)
- Confirm refrigerant charge and superheat/subcooling
- Test capacity control operation (staging, modulation)
- Verify heat recovery operation and setpoints
- Measure actual moisture removal under various loads
- Trend humidity, temperature, and equipment performance over weeks/months

Proper dehumidification system design, installation, and commissioning creates a comfortable, durable natatorium environment while minimizing operating costs.
