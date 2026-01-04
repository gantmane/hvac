---
title: "Energy Recovery Applications"
weight: 7
description: "Technical analysis of energy recovery systems for natatoriums including heat recovery from dehumidification, exhaust air heat recovery, pool water heat reclaim, and integrated energy management strategies for indoor pool facilities."
keywords: "energy recovery natatorium, pool heat recovery, dehumidifier heat reclaim, exhaust air recovery, pool energy efficiency, natatorium COP"
---

Energy recovery represents the single most effective strategy for reducing operating costs in natatorium facilities. The massive energy consumption required for dehumidification, pool water heating, space heating, and ventilation air conditioning creates numerous opportunities to capture and reuse waste heat that would otherwise be rejected. Well-designed energy recovery systems can reduce overall energy consumption by 50-70% compared to conventional approaches.

## Energy Flows in Natatoriums

Understanding energy recovery opportunities requires analysis of all energy streams:

**Major Energy Consumers**:
1. Pool water heating (evaporation, conduction, fresh water makeup): 40-60% of total
2. Space dehumidification (moisture removal): 20-35% of total
3. Ventilation air conditioning (heating/cooling outdoor air): 15-30% of total
4. Domestic hot water (showers, cleaning): 5-15% of total
5. Space heating (envelope losses): Variable by climate

**Available Heat Sources**:
1. Dehumidification condensing heat (refrigeration condenser)
2. Dehumidification sensible heat (condensate cooling)
3. Exhaust air (humid, warm pool air)
4. Pool filter backwash water (warm water discharge)
5. Equipment waste heat (pumps, lighting, auxiliary systems)

Energy recovery systems strategically match heat sources to heating demands, minimizing external energy input.

## Dehumidification Heat Recovery

Heat recovery dehumidifiers represent the foundation of natatorium energy recovery, capturing refrigeration cycle heat for productive use.

### Integrated Refrigeration Cycle

The dehumidification refrigeration cycle removes heat from pool air (evaporator) and rejects it at higher temperature (condenser). Rather than wasting condenser heat to atmosphere or cooling tower, it is recovered for heating applications.

**Energy balance for refrigeration cycle**:

Q_condenser = Q_evaporator + W_compressor

Where:
- Q_condenser = Heat available at condenser (Btu/h)
- Q_evaporator = Heat removed from pool air (Btu/h)
- W_compressor = Compressor work input (Btu/h)

Typical values for pool dehumidifier removing 100 lb/h moisture:
- Q_evaporator = 130,000 Btu/h (latent + sensible cooling)
- W_compressor = 35,000 Btu/h (10.3 kW electrical)
- Q_condenser = 165,000 Btu/h available for recovery

### Pool Water Heating Recovery

The most direct and efficient recovery application uses condenser heat to maintain pool water temperature.

**System configuration**:
- Refrigerant-to-water heat exchanger (brazed plate, shell-and-tube, or tube-in-tube)
- Condenser water circuit integrated with pool heating system
- Modulating three-way valve controls heat delivery to pool
- Auxiliary heater (gas, electric, boiler) supplements when needed

**Design approach**:

Pool heating load calculation:
- Evaporative heat loss: 60-80% of total (from evaporation rate calculation)
- Convective heat loss: 5-15% (when air is cooler than water)
- Conductive heat loss: 5-10% (through pool walls/floor)
- Fresh water makeup: 5-10% (heating replacement water)
- Radiation to cold surfaces: 1-5%

For typical 1,500 ft² competitive pool at 80°F water temperature:
- Evaporation: 612 lb/h at activity factor 0.8
- Evaporative heat loss: 612 × 1,040 = 636,000 Btu/h
- Total pool heating load: approximately 700,000-800,000 Btu/h

Dehumidifier capacity to match:
- Size for 100-120 lb/h removal (with safety factor)
- Multiple units for redundancy and part-load efficiency
- Total condenser heat available: 200,000-250,000 Btu/h per unit

With 2-3 dehumidifier units, heat recovery can provide 400,000-750,000 Btu/h—sufficient for 50-100% of pool heating load depending on sizing and outdoor conditions.

### Heat Rejection Modulation

During periods when pool heating demand is low (summer, or when pool temperature is satisfied), excess condenser heat must be rejected:

**Partial heat recovery with air-cooled condenser**:
- Refrigerant flows first through pool water heat exchanger
- Remaining heat rejected through air-cooled condenser
- Three-way valve or multi-circuit condenser controls split

**Water-cooled condenser with cooling tower**:
- Condenser water flows through pool heat exchanger
- Three-way valve diverts excess flow to cooling tower
- Cooling tower provides heat rejection during low-demand periods

**Hot gas bypass to auxiliary applications**:
- Desuperheater for domestic hot water preheating
- Space heating coils for deck area or adjacent spaces
- Storage tank for load shifting

### Domestic Hot Water Integration

Pool facilities have significant DHW demand for showers, which aligns well with pool operating hours.

**Desuperheater configuration**:
- Heat exchanger on hot gas discharge before main condenser
- Pre-heats DHW from 50-60°F to 90-110°F
- Auxiliary heater brings to final 120-140°F setpoint
- Typical recovery: 20,000-40,000 Btu/h per dehumidifier unit

**Series heat recovery**:
1. Hot gas to DHW desuperheater (highest temperature)
2. Remaining superheat to pool water heat exchanger
3. Condensing heat to pool water
4. Any excess to air-cooled condenser or cooling tower

This cascaded approach maximizes energy recovery by matching temperature levels to applications.

### Performance Metrics

**Coefficient of Performance (COP)**:

COP_heating = Q_recovered / W_electrical

For heat recovery dehumidifier recovering 165,000 Btu/h with 10.3 kW input:

COP = 165,000 / (10.3 × 3,413) = 165,000 / 35,154 = 4.7

This means 4.7 units of heat recovered for each unit of electrical energy consumed—far superior to resistance electric heating (COP = 1.0) or even efficient boilers (efficiency 80-95%).

**Energy recovery effectiveness**:

Effectiveness = Q_recovered / Q_maximum_possible

For pool heating application where all condenser heat can be used:

Effectiveness = Q_to_pool / Q_condenser = 160,000 / 165,000 = 97%

In practice, effectiveness varies from 60-95% depending on load matching and controls.

## Exhaust Air Heat Recovery

Ventilation outdoor air represents a major load, especially in cold climates. Exhaust air heat recovery pre-conditions incoming outdoor air, reducing heating/cooling energy.

### Heat Recovery Ventilator (HRV) Systems

**Sensible-only heat recovery**:
- Plate heat exchangers or rotary wheels transfer sensible heat only
- Outdoor air pre-heated in winter, pre-cooled in summer
- No moisture transfer (undesirable for natatoriums—want to exhaust moisture)
- Effectiveness: 60-80% sensible recovery

**Not recommended for natatoriums** due to lack of moisture removal from exhaust stream.

### Energy Recovery Ventilator (ERV) Systems

**Sensible + latent heat recovery**:
- Enthalpy wheels or membrane heat exchangers transfer both heat and moisture
- Outdoor air pre-conditioned in temperature AND humidity
- Winter: recovers heat and adds moisture to dry outdoor air
- Summer: pre-cools and dehumidifies hot, humid outdoor air

**Challenge for natatoriums**: ERV transfers some moisture FROM humid exhaust TO incoming outdoor air—partially defeating dehumidification objective. Moisture transfer reduces humidity differential that drives dehumidification system.

**When viable**:
- Dry climates where outdoor air is consistently lower dewpoint than exhaust
- Winter operation when outdoor air is cold and dry
- Interlock controls prevent ERV operation when outdoor dewpoint exceeds threshold

### Run-Around Coil Systems

Most practical heat recovery approach for natatorium exhaust air:

**Configuration**:
1. **Exhaust coil**: Mounted in exhaust air stream near dehumidifier
2. **Supply coil**: Mounted in outdoor air intake stream
3. **Pumped glycol loop**: Circulates between coils, transferring heat
4. **Controls**: Modulating valve or variable-speed pump regulates heat transfer

**Advantages**:
- Sensible-only heat recovery (no moisture transfer to supply air)
- Coils can be separated by distance (no cross-contamination)
- Modulation allows optimization for varying conditions
- No moving parts in air streams (compared to rotary wheels)

**Performance**:
- Effectiveness: 45-65% sensible recovery
- Lower than plate/wheel exchangers but acceptable given other constraints

**Example calculation**:

Exhaust air: 10,000 cfm at 82°F
Outdoor air: 10,000 cfm at 10°F (winter design)
Heat recovery effectiveness: 55%

Temperature rise of outdoor air:
ΔT = 0.55 × (82 - 10) = 0.55 × 72 = 39.6°F

Outdoor air entering building after heat recovery:
T_supply = 10 + 39.6 = 49.6°F (instead of 10°F)

Heating energy saved:
Q = 1.08 × cfm × ΔT = 1.08 × 10,000 × 39.6 = 428,000 Btu/h

Annual savings (5,000 heating hours at $0.06/kWh electric):
428,000 Btu/h × 5,000 h / 3,413 Btu/kWh × $0.06/kWh = $37,600 per year

Typical payback: 3-7 years depending on climate and energy costs.

### Dedicated Outdoor Air System (DOAS) Integration

Modern natatorium designs often use separate DOAS for ventilation air:

**System architecture**:
1. **DOAS unit**: Conditions 100% outdoor air with heat recovery
2. **Pool dehumidifier**: Recirculates and dehumidifies pool air
3. **Separate systems** allow optimization of each function

**Benefits**:
- Heat recovery optimized for ventilation load
- Dehumidification optimized for latent load
- Better part-load performance
- Easier control and commissioning

**DOAS features for natatoriums**:
- Run-around coil or plate heat exchanger (sensible recovery)
- Optional energy recovery wheel with bypass for mild weather
- Heating coil to bring OA to neutral temperature (~70-75°F)
- DX cooling/dehumidification coil for summer conditions
- Integration with pool dehumidifier controls

## Pool Water Heat Recovery

Beyond dehumidifier heat recovery, other pool water heat sources can be captured.

### Filter Backwash Heat Recovery

Pool filtration systems require periodic backwashing, discharging 500-2,000 gallons of 78-82°F water to drain.

**Recovery approach**:
- Plate heat exchanger between backwash drain and pool makeup water
- Pre-heats incoming makeup water (typically 50-60°F municipal supply)
- Captures 70-90% of sensible heat from backwash water

**Example calculation**:

Daily backwash: 1,000 gallons at 80°F to drain
Makeup water: 55°F
Heat exchanger effectiveness: 80%

Heat recovery per backwash:
Q = m × c × ΔT × effectiveness
Q = 1,000 gal × 8.33 lb/gal × 1 Btu/lb·°F × (80 - 55) × 0.80
Q = 166,600 Btu per backwash event

For daily backwashing:
Annual energy recovery = 166,600 × 365 = 60.8 MMBtu/year

At $15/MMBtu natural gas: $912 annual savings

### Shower Drain Heat Recovery

Large pool facilities with multiple showers can recover heat from shower drain water.

**Drain water heat recovery (DWHR)**:
- Passive heat exchangers wrap around drain pipe
- Incoming cold water pre-heated by falling drain water
- Effectiveness: 30-60% depending on flow rates and design
- No pumps or controls required

Particularly effective in facilities with simultaneous shower use (swim team facilities, aquatic centers).

## Integrated Energy Management

Comprehensive energy recovery requires system-level optimization.

### Hierarchical Heat Recovery

Prioritize heat recovery applications by temperature level:

**Highest Temperature** (140-180°F):
1. Domestic hot water (requires 120-140°F delivery)
2. Space heating reheat coils (100-140°F)

**Medium Temperature** (90-110°F):
1. Pool water heating (78-84°F required)
2. Radiant floor heating (85-95°F typical)

**Low Temperature** (70-90°F):
1. Outdoor air pre-heating (winter)
2. Perimeter heating (prevents condensation)

Match heat sources to loads:
- Hot gas/desuperheater → DHW
- Condenser → Pool water heating
- Exhaust air recovery → Outdoor air pre-heating

### Thermal Storage

Thermal storage allows load shifting when heat production and demand don't coincide:

**Hot water storage tank**:
- 500-2,000 gallon insulated tank
- Charged by dehumidifier waste heat during pool operation
- Discharged for DHW, space heating, or pool heating during off-hours
- Allows smaller peak equipment capacity

**Pool thermal mass**:
- Pool water itself provides massive storage (1,500 ft² pool = ~85,000 gallons = ~700,000 lb)
- Heat capacity: 700,000 lb × 1 Btu/lb·°F = 700,000 Btu/°F
- Allowing 2°F temperature swing: 1.4 MMBtu storage
- Can absorb excess heat recovery during day, radiate at night

### Controls Integration

Optimized energy recovery requires sophisticated controls:

**Monitoring points**:
- Pool water temperature
- DHW tank temperature
- Space temperature and humidity
- Outdoor air temperature and humidity
- Dehumidifier operating status
- Heat recovery effectiveness

**Control strategies**:
- Modulating valves direct heat to highest-priority loads
- Enable/disable heat recovery based on availability and demand
- Optimize compressor staging for heat recovery + dehumidification
- Seasonal changeover between heating and cooling modes
- Demand limiting during peak utility rate periods

**Trending and optimization**:
- Log energy consumption by end use
- Calculate actual COP and effectiveness
- Identify opportunities for further improvement
- Verify savings against design predictions

## Economic Analysis

Energy recovery systems require capital investment justified by operating cost savings.

### Typical Component Costs

| System | Cost Range | Notes |
|--------|-----------|-------|
| Heat recovery dehumidifier (vs. standard) | +$15,000-$40,000 | Incremental cost for pool water heating integration |
| Run-around coil system (10,000 cfm) | $25,000-$45,000 | Includes coils, piping, controls |
| Plate heat exchanger (backwash recovery) | $3,000-$8,000 | Simple installation |
| Thermal storage tank (1,000 gallon) | $5,000-$12,000 | Installed with controls |
| Control system enhancements | $10,000-$25,000 | BAS integration, sensors, valves |

### Payback Analysis

**Example Project**:
- 1,500 ft² competitive pool
- Climate zone 5 (cold winter, warm summer)
- Operating hours: 4,000 hours/year (11 hours/day)

**Energy Recovery Systems**:
1. Heat recovery dehumidifier for pool heating: +$30,000
2. Run-around coil for ventilation air: +$35,000
3. DHW desuperheater: +$8,000
4. Controls integration: +$12,000
Total incremental cost: $85,000

**Annual Energy Savings**:
1. Pool water heating (75% from heat recovery): 250 MMBtu × $15/MMBtu = $3,750
2. Reduced ventilation heating: 150 MMBtu × $15/MMBtu = $2,250
3. DHW savings: 40 MMBtu × $15/MMBtu = $600
4. Reduced dehumidification energy: 15,000 kWh × $0.12/kWh = $1,800
Total annual savings: $8,400

Simple payback: $85,000 / $8,400 = 10.1 years

With utility incentives (common for energy efficiency projects): 5-7 year payback typical.

Over 20-year equipment life, net savings: $168,000 - $85,000 = $83,000 (present value higher with discount rate).

### Operating Cost Comparison

Annual energy costs for natatorium without vs. with energy recovery:

| System | No Energy Recovery | With Energy Recovery | Savings |
|--------|-------------------|---------------------|---------|
| Pool heating | $12,000 | $3,000 | 75% |
| Dehumidification | $8,500 | $7,200 | 15% |
| Ventilation heating | $6,000 | $2,500 | 58% |
| DHW | $2,500 | $1,500 | 40% |
| **Total** | **$29,000** | **$14,200** | **51%** |

Energy recovery provides over 50% reduction in annual operating costs—a compelling economic case even before considering comfort, reliability, and environmental benefits.

## Commissioning and Verification

Ensure energy recovery systems perform as designed:

1. **Verify heat recovery flow rates and temperatures** at all heat exchangers
2. **Measure actual COP** of dehumidification system under various loads
3. **Trend energy consumption** by end use for baseline and post-installation comparison
4. **Calculate effectiveness** of each recovery component
5. **Optimize control sequences** based on actual operating patterns
6. **Document savings** for utility incentive programs and ownership reporting

Energy recovery transforms natatoriums from energy-intensive liabilities into reasonably efficient facilities. Proper design, integration, and commissioning of heat recovery systems represents best practice in modern indoor pool engineering.
