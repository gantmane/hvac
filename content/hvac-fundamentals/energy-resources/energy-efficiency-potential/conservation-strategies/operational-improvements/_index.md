---
title: "Operational Improvements"
weight: 2
---

Operational improvements represent the lowest-cost approach to energy conservation, targeting system performance optimization without capital investment. These strategies focus on extracting maximum efficiency from existing equipment through better control, maintenance, and operating practices.

## Scheduling Optimization

Operating equipment only when needed eliminates unnecessary energy consumption while maintaining comfort and functionality.

### Occupancy-Based Scheduling

Time-based scheduling aligns system operation with building use patterns:

- **Start/Stop Optimization**: Calculate minimum lead time required to reach setpoint by occupancy time
- **Optimal Start Algorithms**: Use outdoor temperature, space temperature, and thermal mass characteristics
- **Night Setback Recovery**: Predict warmup/cooldown time based on ΔT and building thermal response
- **Weekend/Holiday Scheduling**: Reduce or eliminate operation during unoccupied periods
- **Staged Equipment Start**: Prevent demand peaks by sequencing equipment startup

Optimal start time calculation:

**t_start = t_occupancy - (T_setpoint - T_current) / R_thermal**

Where R_thermal represents building heating/cooling rate (°F/hr or °C/hr).

### Zone-Level Scheduling

Independent scheduling for different building areas improves efficiency:

- **Perimeter vs. Core**: Different solar gain patterns require different schedules
- **Multi-Tenant Coordination**: Individual zone control for varied occupancy patterns
- **After-Hours Overrides**: Temporary occupancy accommodation with automatic reversion
- **Cleaning Schedule Integration**: Ventilation during custodial operations only
- **Kitchen/Laboratory Exhaust**: Match exhaust to actual use periods

### Load Shedding Strategies

Strategic equipment cycling reduces peak demand without compromising comfort:

- **Rotating Equipment Shutdown**: Brief cycling of non-critical loads
- **Pre-Cooling**: Lower temperature before peak demand periods
- **Thermal Mass Utilization**: Leverage building thermal storage capacity
- **Demand Response Integration**: Automated response to utility signals
- **Peak Demand Limiting**: Real-time load monitoring with automated shedding

## Setback and Setup Strategies

Temperature setback during unoccupied periods reduces heating and cooling loads significantly.

### Night Setback Heating

Lower heating setpoint during unoccupied hours:

- **Typical Setback**: 55-60°F (13-16°C) for most commercial buildings
- **Freeze Protection**: Minimum 50°F (10°C) for piping protection
- **Equipment Protection**: Higher setpoints for sensitive equipment areas
- **Humidity Considerations**: Prevent condensation during setback periods
- **Recovery Time**: 1-3 hours typical for commercial construction

Energy savings equation:

**Q_saved = UA × (T_normal - T_setback) × t_unoccupied**

### Cooling Setup

Raise cooling setpoint during unoccupied periods:

- **Typical Setup**: 80-85°F (27-29°C) for commercial spaces
- **Humidity Limits**: Maximum 60% RH to prevent moisture damage
- **Computer Room Exceptions**: Maintain tighter control for IT equipment
- **Building Mass Impact**: Heavy construction allows wider temperature swing
- **Peak Load Consideration**: Setup may increase peak cooling demand

### Seasonal Adjustments

Optimize setpoints based on outdoor conditions:

- **Shoulder Season**: Wider acceptable temperature range (70-78°F vs. 72-76°F)
- **Humidity-Based Limits**: Tighter control during high humidity periods
- **Occupant Adaptation**: Gradual seasonal adjustment improves acceptance
- **Clothing Factor**: Consider seasonal dress code in setpoint selection
- **Activity Level**: Adjust for space function and metabolic heat generation

## Economizer Operation

Free cooling using outdoor air when conditions permit reduces mechanical cooling energy substantially.

### Economizer Control Strategies

Selection of appropriate control method affects energy savings:

| Control Type | Changeover Point | Advantages | Limitations |
|--------------|------------------|------------|-------------|
| Dry Bulb | 55-65°F (13-18°C) | Simple, reliable | Ignores humidity |
| Enthalpy | 28 BTU/lb (65 kJ/kg) | Accounts for latent load | Requires humidity sensor |
| Differential Dry Bulb | Return air temperature | No fixed setpoint | May overcool |
| Differential Enthalpy | Return air enthalpy | Optimal savings | Complex control |

### Economizer Optimization Techniques

Maximize free cooling benefit through proper operation:

- **Integrated Control**: Coordinate economizer with mechanical cooling
- **Minimum Damper Position**: Ensure adequate ventilation air at all times
- **Damper Sequencing**: Modulate outdoor air before mechanical cooling
- **Morning Purge**: Pre-cool building with cool outdoor air before occupancy
- **Night Cooling**: Flush building heat during mild evenings
- **High-Limit Shutoff**: Prevent economizer operation during unfavorable conditions

### Common Economizer Problems

Typical failures that eliminate energy savings:

- **Stuck Dampers**: Mechanical failure prevents modulation
- **Failed Sensors**: Incorrect readings cause improper control
- **Control Logic Errors**: Programming mistakes prevent economizer operation
- **Minimum Position Too High**: Excessive outdoor air during mechanical cooling
- **Relief Damper Issues**: Improper building pressure affects economizer capacity
- **Mixed Air Temperature**: Below dewpoint causes coil condensation and freezing

## Maintenance Impact on Energy Performance

Proper maintenance preserves equipment efficiency and prevents energy waste.

### Filter Maintenance

Clean filters reduce fan energy and maintain airflow:

- **Pressure Drop Monitoring**: Replace at 1.0-2.0 in. w.g. (250-500 Pa) depending on filter type
- **Energy Impact**: Each 0.5 in. w.g. increases fan power by approximately 10-15%
- **Filter Selection**: Balance filtration efficiency with pressure drop
- **Prefilters**: Extend life of final filters, reduce overall pressure drop
- **Differential Pressure Sensors**: Automate filter change notifications

Fan power relationship to pressure:

**BHP = (CFM × ΔP) / (6356 × η_fan)**

### Coil Maintenance

Clean heat exchanger surfaces maintain heat transfer efficiency:

- **Fouling Impact**: Dirty coils reduce capacity by 10-30%
- **Airside Cleaning**: Annual cleaning prevents biological growth
- **Waterside Cleaning**: Remove scale and biological deposits
- **Fin Straightening**: Restore airflow through damaged fins
- **Condensate Drain**: Clear blockages to prevent water damage and IAQ issues

### Belt and Drive Maintenance

Proper belt tension and alignment reduce energy loss:

- **Belt Tension**: Loose belts slip, wasting 5-10% of motor power
- **Belt Condition**: Worn belts reduce transmission efficiency
- **Sheave Alignment**: Misalignment increases belt wear and energy loss
- **Direct Drive Benefits**: Eliminate belt losses (3-5% efficiency gain)
- **VFD Integration**: Variable speed operation reduces mechanical stress

### Bearing Lubrication

Proper lubrication reduces friction losses and prevents failure:

- **Lubrication Schedule**: Follow manufacturer recommendations
- **Bearing Temperature**: Monitor for excessive heat indicating problems
- **Vibration Analysis**: Detect bearing wear before failure
- **Motor Efficiency**: Poor bearings increase motor current draw
- **Seal Condition**: Prevent lubricant loss and contamination

## Monitoring-Based Commissioning

Continuous monitoring identifies operational problems and optimization opportunities.

### Key Performance Indicators

Track critical parameters to identify problems:

- **Energy Use Intensity (EUI)**: kBTU/sf/yr or kWh/m²/yr
- **Cooling Efficiency**: kW/ton or COP
- **Heating Efficiency**: Combustion efficiency percentage
- **Fan Efficiency**: CFM/W or pressure rise per unit power
- **Pump Efficiency**: GPM/W or head per unit power
- **Delta-T**: Supply-return temperature difference indicates distribution efficiency

### Fault Detection and Diagnostics

Automated analysis identifies operational faults:

- **Simultaneous Heating and Cooling**: Wasteful operation requiring correction
- **Excessive Outdoor Air**: Above minimum ventilation requirements
- **Temperature Sensor Errors**: Unrealistic or unchanging readings
- **Economizer Faults**: Damper position inconsistent with control logic
- **Equipment Cycling**: Short cycling indicates oversizing or control problems
- **Schedule Adherence**: Equipment operating outside scheduled hours

### Trending and Baselining

Establish normal operation patterns to identify deviations:

- **Load Normalization**: Adjust for weather using degree-days or regression
- **Seasonal Patterns**: Compare current year to previous year same period
- **Day-Type Comparison**: Weekdays vs. weekends, occupied vs. unoccupied
- **Benchmark Comparison**: Compare to similar buildings or industry standards
- **CUSUM Analysis**: Cumulative sum charts reveal performance drift

### Alarm Management

Effective notification ensures timely response to problems:

- **Alarm Prioritization**: Critical vs. informational classifications
- **Setpoint Tolerance**: Dead bands prevent nuisance alarms
- **Alarm Delays**: Time delays filter transient conditions
- **Escalation Procedures**: Automatic notification hierarchy
- **Alarm Analysis**: Review patterns to identify systemic issues

## Reset Strategies

Adjusting supply temperatures based on demand reduces energy consumption.

### Supply Air Temperature Reset

Raise supply air temperature when cooling loads decrease:

- **Outdoor Air Reset**: Increase SAT as OAT decreases
- **Warmest Zone Reset**: SAT based on zone requiring most cooling
- **Return Air Temperature Reset**: Maintain target return air temperature
- **Typical Range**: 55-65°F (13-18°C) depending on load
- **Humidity Constraints**: Minimum SAT to maintain dehumidification

### Chilled Water Temperature Reset

Increase chilled water supply temperature reduces chiller energy:

- **Outdoor Air Reset**: 42-50°F (6-10°C) range based on OAT
- **Load-Based Reset**: Increase temperature during low load periods
- **Valve Position Reset**: Monitor valve positions, reset when all valves <90% open
- **Chiller Efficiency Impact**: Each 1°F increase saves approximately 1-2% compressor energy
- **Dehumidification Limit**: Maintain adequate coil temperature for latent removal

### Hot Water Temperature Reset

Lower hot water temperature reduces heat loss and boiler cycling:

- **Outdoor Air Reset**: 120-180°F (49-82°C) range based on OAT
- **Linear Reset**: ΔT_hw proportional to ΔT_outdoor
- **Design Day Operation**: Maximum temperature at design outdoor temperature
- **Domestic Hot Water Priority**: Separate DHW from space heating for better control
- **Condensing Boiler Optimization**: Lower return temperature maximizes efficiency

Reset schedule example:

| Outdoor Temp | Hot Water Supply |
|--------------|------------------|
| 70°F (21°C) | 120°F (49°C) |
| 50°F (10°C) | 140°F (60°C) |
| 30°F (-1°C) | 160°F (71°C) |
| 0°F (-18°C) | 180°F (82°C) |

## Variable Speed Drive Optimization

VFD operation reduces fan and pump energy through affinity law relationships.

### Fan Speed Optimization

Reduce airflow during low load conditions:

- **VAV System Reset**: Lower static pressure setpoint based on damper positions
- **Trim and Respond**: Incrementally adjust setpoint to maintain minimum damper position
- **Diversity Factor**: Account for zones requiring simultaneous maximum airflow
- **Minimum Speed**: Maintain minimum 30-40% speed for stable operation
- **Duct Pressure Distribution**: Ensure adequate pressure at furthest zones

Energy savings relationship:

**P₂/P₁ = (RPM₂/RPM₁)³**

Reducing fan speed to 80% of design reduces power to 51% of design.

### Pump Speed Optimization

Variable flow reduces pumping energy substantially:

- **Differential Pressure Reset**: Lower setpoint when control valves open
- **Temperature-Based Control**: Modulate flow to maintain ΔT
- **Minimum Flow Requirements**: Maintain chiller/boiler minimum flow
- **Distribution Efficiency**: Ensure adequate flow at furthest loads
- **Decoupling Applications**: Primary-secondary pumping with variable secondary

## Demand Controlled Ventilation

Modulate outdoor air based on actual occupancy reduces conditioning load.

### CO₂-Based Control

Carbon dioxide concentration indicates occupancy level:

- **Setpoint Selection**: 800-1000 ppm typical target above outdoor ambient
- **Sensor Placement**: Return air or representative zone location
- **Minimum Ventilation**: Maintain code-required minimum at all times
- **Transient Response**: Account for sensor lag and space mixing time
- **Sensor Calibration**: Verify accuracy annually, replace as needed

Ventilation rate equation:

**CFM_vent = (G × 10⁶) / [CS(CO₂_space - CO₂_outdoor)]**

Where G = CO₂ generation rate (CFM), CS = steady-state constant.

### Occupancy Sensor Integration

Direct occupancy detection enables faster response:

- **PIR Sensors**: Passive infrared detects motion
- **Dual Technology**: Combines PIR with ultrasonic for better accuracy
- **CO₂ Backup**: Use both methods for redundancy
- **Zone Aggregation**: Combine multiple zones for smoother control
- **Time Delays**: Prevent rapid cycling on occupancy changes

## Components

- Preventive Maintenance Efficiency
- Control System Optimization
- System Balancing Commissioning
- Economizer Optimization
- Supply Air Temperature Reset
- Chilled Water Temperature Reset
- Hot Water Temperature Reset
- Demand Controlled Ventilation
- Variable Speed Drive Optimization
