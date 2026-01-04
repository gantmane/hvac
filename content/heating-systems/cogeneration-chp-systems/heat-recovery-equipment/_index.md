---
title: "Heat Recovery Equipment for CHP Systems"
description: "Engineering analysis of heat recovery technologies including exhaust heat exchangers, heat recovery steam generators, jacket water systems, absorption chiller integration, and thermal storage for maximizing CHP system efficiency and utilization."
date: 2026-01-04
weight: 3
---

Heat recovery equipment captures thermal energy from prime mover waste streams and delivers it at useful temperatures and pressures for facility heating, cooling, and process applications. The effectiveness of heat recovery integration fundamentally determines overall CHP system efficiency, with well-designed systems recovering 50-70% of fuel input energy. Selection and sizing of heat recovery equipment requires careful analysis of available thermal streams, temperature levels, facility thermal loads, and economic trade-offs between recovery depth and capital cost.

## Exhaust Heat Recovery Fundamentals

Exhaust gas from prime movers contains the largest single thermal stream, typically 30-50% of fuel input at temperatures of 350-1000°F depending on prime mover type. The high temperature enables steam generation, hot water production, or direct process heating.

The available thermal energy depends on exhaust mass flow, temperature, and minimum allowable stack temperature:

$$Q_{available} = \dot{m}_{exh} \cdot c_p \cdot (T_{exh,in} - T_{stack,min})$$

Stack temperature must remain above the acid dew point to prevent sulfuric acid condensation that causes rapid corrosion. For natural gas combustion with typical sulfur content, minimum stack temperature ranges from 250-320°F. Higher sulfur fuels require higher stack temperatures.

The acid dew point temperature can be estimated from:

$$T_{dewpoint} = 1000 / (2.276 - 0.0294 \log_{10}(p_{SO_3}) - 0.0858 \log_{10}(p_{H_2O}))$$

Where partial pressures are in mmHg. For natural gas with 0.1 ppm sulfur content, the dew point approximates 280-300°F.

Heat recovery effectiveness quantifies the fraction of available thermal energy actually recovered:

$$\varepsilon_{HR} = \frac{Q_{recovered}}{Q_{available}} = \frac{T_{exh,in} - T_{exh,out}}{T_{exh,in} - T_{stack,min}}$$

Typical exhaust heat recovery systems achieve effectiveness of 0.75-0.90 with proper design. Higher effectiveness requires larger heat exchangers with greater capital cost.

## Heat Recovery Steam Generators

HRSGs extract thermal energy from gas turbine or engine exhaust to generate steam at pressures from 15 psig to 600 psig. The configuration depends on pressure requirements, exhaust characteristics, and integration with facility steam systems.

Single-pressure HRSGs produce steam at one pressure level, typically 50-150 psig for CHP applications. The economizer preheats boiler feedwater, the evaporator generates saturated steam, and the superheater (if included) raises steam temperature above saturation. The pinch point—the minimum temperature difference between exhaust and saturation temperature—typically ranges from 20-40°F.

The steam production rate follows from energy balance:

$$\dot{m}_{steam} = \frac{\dot{m}_{exh} \cdot c_p \cdot (T_{exh,in} - T_{exh,out})}{h_{steam} - h_{feedwater}}$$

For a gas turbine with 50,000 lb/hr exhaust at 950°F, producing 150 psig saturated steam (366°F, h=1196 Btu/lb) from 220°F feedwater (h=188 Btu/lb), cooling exhaust to 350°F:

$$\dot{m}_{steam} = \frac{50000 \cdot 0.26 \cdot (950 - 350)}{1196 - 188} = 7750 \text{ lb/hr}$$

This represents approximately 8.6 MMBtu/hr thermal output.

Multi-pressure HRSGs incorporate two or three pressure levels to improve heat recovery across the full exhaust temperature range. The high-pressure section operates nearest the turbine exit where exhaust temperature is highest. Intermediate and low-pressure sections recover heat from lower-temperature exhaust. This cascaded approach improves overall heat recovery by 5-15% compared to single-pressure designs.

Supplementary firing burns additional fuel in the HRSG to increase steam production or raise steam temperature. The oxygen-rich turbine exhaust (15-17% O₂) supports combustion without additional air. Supplementary firing decreases overall electrical efficiency but provides operational flexibility to meet varying thermal demands.

## Economizers and Hot Water Heat Recovery

Economizers cool exhaust gas to heat water or glycol solutions for space heating, domestic hot water, or low-temperature processes. These simple shell-and-tube or finned-tube heat exchangers suit reciprocating engines and small gas turbines where steam generation is unnecessary.

The UA value (overall heat transfer coefficient times area) determines heat exchanger size for a given duty:

$$Q = UA \cdot \Delta T_{lm}$$

Where the log-mean temperature difference accounts for varying temperature gradients:

$$\Delta T_{lm} = \frac{(T_{h,in} - T_{c,out}) - (T_{h,out} - T_{c,in})}{\ln\left(\frac{T_{h,in} - T_{c,out}}{T_{h,out} - T_{c,in}}\right)}$$

For counter-flow configuration with hot exhaust entering at 800°F and exiting at 350°F, heating water from 140°F to 200°F:

$$\Delta T_{lm} = \frac{(800 - 200) - (350 - 140)}{\ln(600/210)} = 381°F$$

Overall heat transfer coefficients range from 8-15 Btu/hr-ft²-°F for exhaust-to-water economizers depending on gas velocity, fin design, and fouling factors.

Jacket water heat recovery from reciprocating engines transfers thermal energy through plate-and-frame heat exchangers. The engine coolant loop operates at 180-210°F, providing 20-30% of fuel input as recoverable heat. A facility hot water loop receives this energy while maintaining engine coolant within the manufacturer's specified temperature range.

The heat exchanger must accommodate the full engine cooling load under all operating conditions:

$$Q_{jacket} = \dot{m}_{coolant} \cdot c_p \cdot (T_{engine,out} - T_{engine,in})$$

Typical engine coolant flow rates of 200-400 gpm with 15-20°F temperature rise across the engine yield 1.5-3.5 MMBtu/hr thermal output for 1 MW engines.

## Absorption Chiller Integration

Absorption chillers convert recovered thermal energy to cooling capacity, expanding CHP applications to cooling-dominated facilities or enabling tri-generation (power, heating, and cooling). The absorption chiller coefficient of performance relates cooling output to thermal input:

$$\text{COP}_{abs} = \frac{Q_{cooling}}{Q_{thermal,in}}$$

Single-effect absorption chillers operate from low-pressure steam (12-15 psig) or 230-250°F hot water with COP of 0.65-0.75. Double-effect chillers require medium-pressure steam (100-150 psig) or 300-360°F hot water, achieving COP of 1.1-1.4.

The integration affects CHP system economics by providing year-round thermal utilization. A 1 MW reciprocating engine producing 2.5 MMBtu/hr recoverable heat can drive a 500-ton double-effect absorption chiller (2.5 MMBtu/hr ÷ 0.01 MMBtu/hr-ton ÷ 1.2 COP = 500 tons) during cooling season.

Triple-effect absorption chillers operating from 400°F thermal energy achieve COP of 1.6-1.8 but require higher-temperature heat sources such as gas turbine exhaust or high-temperature fuel cells.

## Thermal Energy Storage Integration

Thermal storage buffers mismatches between CHP thermal production and facility thermal demand, improving utilization and allowing CHP operation during periods when instantaneous thermal load is insufficient.

Hot water thermal storage accumulates sensible heat in insulated tanks. The storage capacity depends on volume and temperature swing:

$$Q_{storage} = \rho \cdot V \cdot c_p \cdot \Delta T$$

For water with ρ = 62.4 lb/ft³, $c_p$ = 1 Btu/lb-°F, a 10,000 gallon (1337 ft³) tank with 40°F temperature swing (180°F to 140°F) stores:

$$Q_{storage} = 62.4 \cdot 1337 \cdot 1 \cdot 40 = 3.34 \text{ MMBtu}$$

This provides approximately 1.3 hours of thermal energy for a 1 MW CHP system with 2.5 MMBtu/hr heat recovery.

Steam accumulator tanks store high-pressure saturated water that flashes to steam when pressure is reduced. The storage capacity significantly exceeds sensible hot water storage due to the enthalpy of vaporization. Accumulators enable CHP systems to meet short-duration steam demands exceeding the HRSG capacity.

Ice thermal storage for cooling applications produces ice during off-peak periods (night) when CHP thermal output exceeds heating demands. The ice melts during peak cooling periods, providing cooling capacity without operating chillers. The high latent heat of fusion (144 Btu/lb) enables compact storage compared to chilled water.

## Control and Safety Systems

Heat recovery system controls maintain safe operation and optimize thermal recovery under varying conditions.

Temperature control prevents overheating by bypassing exhaust around heat recovery equipment when downstream thermal demand is insufficient. A modulating bypass damper diverts a fraction of exhaust flow directly to the stack while the remainder passes through the heat recovery equipment.

Pressure control in steam systems maintains safe operating pressure through pressure reducing valves, back-pressure regulators, and safety relief valves. The HRSG must safely accommodate transient conditions during startup, shutdown, and load changes.

Freeze protection prevents water freezing in heat exchangers during shutdown in cold climates. Electric heaters, glycol solutions, or continuous low-flow circulation maintain temperatures above freezing.

Stack temperature monitoring ensures operation above the acid dew point. If stack temperature falls below the safe minimum, the control system increases bypass flow or reduces heat recovery water flow to raise exhaust temperature.

## Heat Recovery Optimization and Economics

The optimal depth of heat recovery balances capital cost against annual energy recovery value. Diminishing returns occur as heat exchanger size increases to approach closer temperature approaches.

The incremental cost-effectiveness can be evaluated by:

$$\frac{\Delta \text{Cost}}{\Delta \text{Energy Recovery}} \leq \frac{1}{\text{Energy Value} \cdot \text{Lifetime} \cdot \text{Discount Factor}}$$

Where energy value reflects displaced fuel cost adjusted for boiler efficiency. For $0.40/therm natural gas displaced by heat recovery (assuming 80% boiler efficiency = $0.50/therm equivalent), 20-year lifetime, and 8% discount rate, the cost-effectiveness limit is approximately $160/MMBtu/hr of additional recovery capacity.

Heat recovery effectiveness above 80% generally requires disproportionate capital investment for diminishing energy recovery. Most economically optimal designs target 70-85% effectiveness.
