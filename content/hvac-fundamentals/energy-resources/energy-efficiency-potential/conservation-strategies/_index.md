---
title: "Conservation Strategies"
aliases: ["Conservation Strategies"]
description: "HVAC energy conservation strategies including operational improvements, setpoint optimization, equipment efficiency upgrades, system-level optimization, and commissioning approaches for achieving 10-40% energy savings."
weight: 1
---

Energy conservation in HVAC systems represents the most cost-effective approach to reducing operating costs and improving building performance. Unlike efficiency improvements that require equipment replacement, conservation strategies often involve operational changes, controls optimization, and better system management.

## Strategy Classification

Conservation measures divide into distinct categories based on implementation requirements and expected savings.

### No-Cost Operational Changes

Operational improvements require minimal capital investment but demand consistent management attention.

**Setpoint Adjustments**

Temperature setpoints directly control energy consumption. Each degree Fahrenheit of cooling setpoint increase saves approximately 3% of cooling energy. Conversely, each degree of heating setpoint reduction saves approximately 3% of heating energy.

Optimal setpoint ranges:
- Cooling season: 74-76°F occupied, 80-85°F unoccupied
- Heating season: 68-70°F occupied, 60-65°F unoccupied
- Humidity control: 50-60% RH during cooling season

Dead band between heating and cooling modes should maintain minimum 5°F separation to prevent simultaneous heating and cooling.

**Schedule Optimization**

HVAC system runtime directly correlates with energy consumption. Proper scheduling reduces operating hours by 20-40% in typical commercial buildings.

Start/stop optimization adjusts equipment runtime based on:
- Thermal mass effects: Building capacity to store heating or cooling
- Setpoint recovery time: Duration required to achieve occupied setpoints
- Weather conditions: Outdoor temperature impact on recovery time
- Occupancy patterns: Actual building use versus scheduled occupancy

Optimal start algorithms calculate equipment startup time using:

T_start = T_current + (T_setpoint - T_current) / R_recovery

Where R_recovery represents the building's temperature change rate under specific outdoor conditions.

**Supply Air Temperature Reset**

Fixed supply air temperatures waste energy through excessive reheat. Reset strategies adjust supply air temperature based on zone requirements.

Common reset approaches:
- Outdoor air reset: Increase SAT as outdoor temperature decreases
- Zone demand reset: Increase SAT based on coldest zone requiring full cooling
- Trim and respond: Gradual adjustment based on damper positions

Typical savings range from 10-20% of total HVAC energy through reduced reheat and fan energy.

### Low-Cost Control Improvements

Controls optimization requires modest investment in sensors, programming, or minor hardware additions.

**Demand-Based Ventilation**

CO2-based demand control ventilation reduces outdoor air quantities during partial occupancy. Energy savings stem from reduced heating, cooling, and fan energy to condition outdoor air.

Ventilation energy fraction:

E_vent = V_oa × ρ × c_p × (T_oa - T_ra) × h_annual / η_system

Where:
- V_oa = outdoor airflow (CFM)
- ρ = air density (0.075 lb/ft³)
- c_p = specific heat (0.24 BTU/lb-°F)
- T_oa - T_ra = outdoor-indoor temperature difference
- h_annual = annual operating hours
- η_system = system efficiency

CO2 setpoints typically maintain 1000-1200 ppm maximum during occupied periods. Each 100 CFM reduction in outdoor air saves approximately 3-5 kBTU/hr in mixed climates.

**Economizer Optimization**

Properly functioning economizers provide "free cooling" when outdoor conditions permit. Common issues preventing optimal operation:
- Stuck dampers or failed actuators
- Incorrect sensor calibration
- Improper control sequences
- Mixed air temperature control overriding economizer

Economizer savings potential ranges from 10-30% of cooling energy depending on climate zone. Dry climates achieve higher savings through extended economizer hours.

**Chilled Water Temperature Reset**

Raising chilled water supply temperature improves chiller efficiency. Every 1°F increase in CHWS temperature improves chiller efficiency by approximately 1-2%.

Reset strategies balance:
- Chiller efficiency improvement at higher CHWS temperatures
- Increased pumping energy from higher flow rates
- Dehumidification capacity reduction
- Cooling coil performance degradation

Typical reset range: 42-54°F CHWS temperature based on cooling load or outdoor conditions.

### Medium-Cost Equipment Upgrades

Equipment-level improvements require capital investment but deliver measurable savings with reasonable payback periods.

**Variable Frequency Drives**

VFDs on pumps and fans reduce energy consumption through affinity law relationships. Fan power varies with the cube of speed:

P_2 / P_1 = (N_2 / N_1)³

Operating at 80% speed reduces power consumption to 51% of full-speed operation. Operating at 60% speed reduces power to 22% of full-speed operation.

VFD applications by system type:

| System Type | Typical Savings | Payback Period |
|-------------|-----------------|----------------|
| Constant volume AHU conversion | 30-50% | 2-4 years |
| Primary-secondary pumping | 20-40% | 3-5 years |
| Cooling tower fans | 30-60% | 1-3 years |
| Condenser water pumps | 25-45% | 2-4 years |

**High-Efficiency Motors**

Premium efficiency motors (NEMA Premium or IE3) reduce electrical losses by 2-5% compared to standard efficiency motors. Savings increase with:
- Larger motor sizes
- Higher annual operating hours
- Higher load factors

Motor replacement prioritization considers:
- Annual operating hours > 4000 hr/yr
- Motor size > 10 HP
- Load factor > 60%
- Existing motor efficiency < 90%

**LED Lighting Integration**

Lighting heat gains directly impact cooling loads. LED conversion reduces cooling loads by 50-70% compared to incandescent sources and 30-40% compared to fluorescent.

Cooling load reduction:

Q_cooling = Q_lighting × F_space × F_vent × COP_adjustment

Where:
- Q_lighting = reduction in lighting heat gain
- F_space = fraction of lighting load to conditioned space (0.6-0.9)
- F_vent = ventilation air impact factor (1.1-1.3)
- COP_adjustment = chiller efficiency factor

### Capital-Intensive System Optimization

Major system modifications require substantial investment but achieve the highest energy savings.

**System Conversion Projects**

Converting inefficient system types to more efficient configurations:

| Conversion Type | Energy Savings | Typical Cost | Applications |
|-----------------|----------------|--------------|--------------|
| CAV to VAV | 25-40% | $8-15/CFM | Office buildings, schools |
| Constant volume pumping to variable primary | 30-50% | $15-30/ton | Chilled water plants |
| Pneumatic to DDC controls | 15-25% | $2-4/ft² | Older commercial buildings |
| Single-zone RTU to DOAS + radiant | 30-50% | $25-40/ft² | New construction, major renovations |

**Plant Equipment Replacement**

Replacing aging central plant equipment with high-efficiency alternatives:

Chiller replacement considerations:
- New centrifugal chillers: 0.45-0.55 kW/ton
- Magnetic bearing chillers: 0.40-0.50 kW/ton
- Oil-free chillers: 0.35-0.45 kW/ton
- Existing equipment typically: 0.65-0.85 kW/ton

Boiler replacement efficiency gains:
- Existing atmospheric boilers: 75-80% combustion efficiency
- Non-condensing high-efficiency: 82-85% combustion efficiency
- Condensing boilers: 90-96% combustion efficiency

**Building Envelope Improvements**

Envelope upgrades reduce HVAC load requirements:

Load reduction by measure:

| Envelope Measure | Cooling Load Reduction | Heating Load Reduction | Cost Range |
|------------------|------------------------|------------------------|------------|
| Window replacement (U-0.30, SHGC 0.25) | 15-25% | 20-30% | $40-80/ft² |
| Wall insulation upgrade (R-13 to R-19) | 5-10% | 15-25% | $3-6/ft² |
| Roof insulation upgrade (R-19 to R-30) | 8-15% | 12-20% | $2-5/ft² |
| Air sealing (5 ACH to 1 ACH) | 10-15% | 25-35% | $0.50-2/ft² |

## Commissioning Approaches

Commissioning and retro-commissioning identify operational deficiencies and optimization opportunities.

### Existing Building Commissioning

EBCx focuses on optimizing existing system performance without major capital investment. Typical process:
1. Systems documentation review
2. Operational performance testing
3. Deficiency identification and correction
4. Controls optimization and sequence updates
5. Staff training and documentation

Average EBCx findings by system:

| System Category | Deficiencies Found | Energy Penalty | Correction Cost |
|-----------------|-------------------|----------------|-----------------|
| Economizers | 60-80% non-functional | 10-30% cooling energy | Low ($500-2000) |
| Simultaneous heating/cooling | 40-60% of systems | 15-25% total HVAC | Low ($0-1000) |
| Scheduling issues | 50-70% of systems | 20-40% total HVAC | Low ($0-500) |
| Control calibration | 30-50% of sensors | 5-15% total HVAC | Low ($200-1000) |

EBCx typically achieves 10-20% whole-building energy savings with payback periods under 2 years.

### Continuous Commissioning

Ongoing commissioning maintains optimal performance through persistent monitoring and adjustment:

- Fault detection and diagnostics (FDD) systems
- Performance benchmarking against baselines
- Periodic re-tuning of control sequences
- Regular sensor calibration verification
- Staff training reinforcement

Continuous commissioning prevents performance degradation that typically occurs at 2-5% per year without intervention.

## Integrated Strategy Development

Maximum energy savings result from coordinated implementation of multiple strategies.

### Implementation Sequencing

Optimal implementation order:
1. No-cost operational improvements (immediate implementation)
2. Controls optimization and sensor additions (months 1-6)
3. Equipment upgrades during normal replacement cycles (years 1-5)
4. System conversions during major renovations (years 3-10)

### Interaction Effects

Conservation strategies interact, affecting combined savings:

**Positive interactions** (combined savings exceed individual measures):
- Envelope improvements + equipment downsizing = reduced equipment first cost
- Lighting upgrades + cooling load reduction = smaller chiller requirements
- VFD installation + improved scheduling = enhanced part-load efficiency

**Negative interactions** (combined savings less than individual measures):
- Supply air temperature reset + economizer optimization (both address similar loads)
- Demand ventilation + envelope sealing (reduced infiltration decreases ventilation savings)
- Multiple setpoint adjustments (cumulative occupant comfort impacts)

### Measurement and Verification

Quantifying savings requires baseline establishment and ongoing monitoring:

Normalized savings calculation:

Savings = (E_baseline - E_post) × (CDD_actual / CDD_baseline)

Where:
- E_baseline = pre-retrofit energy consumption
- E_post = post-retrofit energy consumption
- CDD = cooling degree days (weather normalization)

Similar approach applies for heating savings using HDD (heating degree days).

Statistical analysis requires minimum 12 months baseline data and 12 months post-implementation data for reliable results.

## Performance Persistence

Conservation savings degrade without ongoing attention:

Typical degradation rates by strategy type:

| Strategy Category | Annual Degradation | Maintenance Requirements |
|-------------------|-------------------|-------------------------|
| Setpoint changes | 15-30% | Monthly verification and enforcement |
| Schedule optimization | 10-20% | Quarterly schedule review |
| VFD operation | 5-10% | Annual calibration and trending review |
| Economizer function | 20-40% | Semi-annual functional testing |
| DCV operation | 10-15% | Annual sensor calibration |

Maintaining conservation savings requires:
- Regular performance monitoring and trending
- Staff training and awareness programs
- Preventive maintenance execution
- Periodic re-commissioning (3-5 year intervals)
- Energy management accountability structures

Energy savings persistence improves dramatically with building automation system integration, automated fault detection, and performance dashboards providing real-time feedback to operations staff.
