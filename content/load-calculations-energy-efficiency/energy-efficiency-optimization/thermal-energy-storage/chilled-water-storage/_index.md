---
title: "Chilled Water Storage"
aliases: ["Chilled Water Storage"]
description: "Stratified chilled water thermal storage systems design including tank sizing, diffuser selection, temperature stratification maintenance, and system integration for load management."
weight: 2
---

## Chilled Water Storage Fundamentals

Chilled water storage systems store cooling capacity as sensible heat in water, maintaining temperature differential between warm return water at top of tank and cold supply water at bottom. The storage capacity equals Q = m × cp × ΔT, where m is water mass, cp is specific heat (1 BTU/lb-°F), and ΔT is temperature difference. A typical system with 20°F differential (44°F supply, 64°F return) provides 10 BTU storage per pound of water, or approximately 83 BTU per gallon accounting for water density.

The reliance on sensible heat rather than latent heat of phase change requires 6-8 times greater volume than equivalent ice storage capacity. This volume requirement limits chilled water storage to applications with available space for large tanks, typically 100,000-1,000,000 gallon capacity for commercial buildings. The benefit over ice storage is elimination of ice-making energy penalty, enabling chillers to operate at standard efficiency of 0.50-0.65 kW/ton compared to 0.70-0.85 kW/ton for ice making.

## Temperature Stratification Principles

Successful chilled water storage depends on maintaining sharp temperature stratification with minimal mixing between warm upper layer and cold lower layer. The thermocline region of temperature transition occupies 1-3 feet of tank height when properly designed, enabling simultaneous charging (cold water entering bottom) and discharging (cold water leaving bottom, warm water entering top) without degrading stored capacity through mixing.

Stratification stability derives from density difference between warm and cold water, with warmer water remaining buoyant above colder water. The density difference of water between 44°F and 64°F (typical storage range) is approximately 0.3%, creating minimal driving force for stratification. Proper inlet diffuser design distributing flow horizontally at appropriate density level without jet mixing is critical to maintaining separation.

Common causes of stratification degradation include excessive inlet velocities creating turbulent jets that entrain and mix adjacent layers, improper diffuser elevation relative to entering water density, internal obstructions disrupting flow patterns, and thermal conduction through tank walls or internal components. Field measurements show well-designed systems achieve thermocline thickness of 1-2 feet, while poor designs experience 6-10 feet or complete mixing eliminating storage effectiveness.

## Tank Configuration and Sizing

Stratified storage tanks require height-to-diameter ratio of 1:1 or greater to establish stable vertical stratification. Shorter wider tanks are prone to mixing from internal circulations and have insufficient height for adequate separation. Tall narrow tanks maintain better stratification but increase structural costs and may face site restrictions. Typical commercial tanks are cylindrical steel construction with height-to-diameter ratios of 1.0-1.5, ranging from 40-80 feet diameter and similar height.

Tank volume sizing depends on load profile and storage strategy. Full storage requires capacity equal to daytime cooling load integrated over peak period. Partial storage capacity equals the difference between peak instantaneous load and average load. A building with 1000 ton peak, 700 ton average load over 10 hours requires 3000 ton-hours storage for load leveling strategy (300 ton difference × 10 hours). At 20°F ΔT, this equals approximately 360,000 gallons.

Multiple smaller tanks rather than single large tank provide operational flexibility, maintenance redundancy, and phased capacity expansion. However, multiple tanks increase piping complexity and pumping energy. Economic analysis comparing tank quantity versus size identifies optimal configuration for specific applications.

## Inlet Diffuser Design

Diffuser systems introduce charging or discharging flow horizontally across tank cross-section at elevation determined by water density, preventing vertical jets that would entrain and mix stratified layers. Common diffuser types include octagonal ring diffusers, radial arm diffusers with multiple discharge ports, and slotted pipe manifolds spanning tank diameter.

Design criteria limit diffuser discharge velocity below 1-2 feet per second to prevent jet formation while providing adequate flow distribution across tank area. The Froude number Fr = V / √(g × D × ΔT/T) characterizes flow stability, with values below 1.0 ensuring buoyant forces dominate inertial forces preventing mixing. Typical design Froude numbers are 0.3-0.7.

Floating diffusers track thermocline elevation, always introducing flow at appropriate density level as thermocline moves during charge/discharge cycles. Fixed diffusers at multiple elevations provide less precise density matching but simpler mechanical design. The optimal approach depends on tank size, flow rates, and budget constraints.

## Charging and Discharging Modes

During charging mode, chillers produce cold water entering tank bottom through lower diffusers while displacing warm water from tank top returning to chillers. The cold water density (higher than warm water) causes it to settle below thermocline, displacing thermocline upward as tank charges. Complete charge fills entire tank with cold water, pushing thermocline to top.

Discharging draws cold water from tank bottom supplying building loads while warm return water enters tank top, reversing the process. The warm water floats above thermocline, progressively moving thermocline downward as discharge proceeds. Complete discharge fills tank with warm water, moving thermocline to bottom.

Optimal control sequences maintain chillers at peak efficiency by operating during off-peak hours at full capacity charging storage. Variable-speed chiller operation during charging reduces energy efficiency compared to full-load operation. During discharge, chiller operation supplements storage when loads exceed storage discharge capacity or storage becomes depleted before end of peak period.

## Series vs. Parallel Connection

Series connection places storage in main distribution loop with all return water flowing through tank before returning to chillers. This configuration maximizes storage utilization since all return flow has opportunity to stratify and recharge storage. The series arrangement limits system flow rate to tank design flow, potentially restricting building distribution flow or requiring larger tanks to accommodate higher flows.

Parallel connection enables independent control of storage flow separate from main building distribution loop. Variable-speed pumps modulate storage charging and discharging flows independently of building loads. This arrangement provides operational flexibility and unlimited building distribution flow but requires additional piping, pumps, and controls while potentially under-utilizing storage capacity during partial load conditions.

Combined configurations connect storage in series with distribution during charging to maximize storage utilization, then parallel during discharge to independently control discharge rates. Three-way valve arrangements enable mode switching, optimizing both charging efficiency and discharge flexibility.

## Performance Monitoring

Key performance indicators for stratified storage include thermocline thickness (measured by vertical temperature sensors at multiple elevations), storage efficiency (energy recovered during discharge divided by energy input during charging), and capacity utilization (actual ton-hours delivered compared to design capacity). Well-designed systems achieve 90-95% storage efficiency accounting for standby losses and thermocline degradation.

Temperature sensors at 5-10 foot vertical spacing throughout tank height enable real-time thermocline tracking and capacity monitoring. The sensor data reveals mixing problems, improper diffuser operation, or excessive standby losses requiring corrective action. Integration of sensor data with building automation system enables predictive control adjusting charging schedules based on remaining storage capacity and forecasted loads.

Regular inspection and maintenance includes checking diffuser integrity, cleaning any sediment or biofilm accumulation affecting heat transfer or flow distribution, verifying insulation effectiveness, and validating control sequences. Annual performance testing comparing measured versus expected capacity identifies degradation requiring intervention before significant economic impact accumulates.
