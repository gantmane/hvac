---
title: "Chiller Operating Parameters"
description: "Critical analysis of chiller operating parameters including chilled water temperatures, flow rates, condenser water conditions, approach temperatures, temperature lift, and their impact on efficiency and capacity."
weight: 2
---

## Technical Overview

Chiller operating parameters define the thermodynamic boundaries within which compression cycles operate. These parameters directly influence capacity, efficiency, and component longevity through their impact on compression ratio, heat transfer effectiveness, and refrigerant state conditions. Understanding parameter relationships enables optimization of chiller plant performance while maintaining equipment within safe operating limits. Proper monitoring and control of operating parameters forms the foundation of efficient chiller operation.

## Chilled Water Supply Temperature

Chilled water supply temperature represents the water temperature leaving the evaporator, typically ranging from 40°F to 48°F (4°C to 9°C) for comfort cooling applications. Lower supply temperatures increase cooling capacity per gallon of water flow but elevate compressor lift and reduce efficiency. Design supply temperature selection balances distribution system requirements, dehumidification needs, and energy efficiency. Process cooling applications may demand temperatures from 35°F to 60°F (2°C to 16°C) depending on process requirements. Each 1°F (0.6°C) supply temperature increase improves chiller efficiency approximately 1-2%.

## Chilled Water Return Temperature

Return water temperature entering the evaporator determines the temperature difference (delta-T) driving heat transfer. Design return temperatures typically range from 54°F to 60°F (12°C to 16°C) for standard comfort cooling. The temperature difference between return and supply water directly affects required water flow rate for given cooling loads. Higher return temperatures (wider delta-T) reduce pump energy through lower flow requirements but may indicate insufficient air-side heat transfer in terminal equipment.

## Chilled Water Delta-T

Chilled water temperature difference (delta-T) equals return temperature minus supply temperature, typically designed for 10-14°F (5.6-7.8°C). This parameter fundamentally determines water flow rates through the relationship Q = 500 × GPM × ΔT for cooling load Q in Btuh, flow rate GPM in gallons per minute, and temperature difference ΔT in °F. Delta-T degradation, where actual operating delta-T falls below design values, indicates flow problems, control issues, or heat transfer deficiencies requiring investigation and correction.

## Chilled Water Flow Rate

Flow rate through the evaporator affects heat transfer coefficients, pressure drop, and velocity-dependent fouling. Design flow rates typically provide 2-4 ft/s (0.6-1.2 m/s) tube velocity, balancing heat transfer against pumping energy. Minimum flow prevents freezing risk and maintains adequate heat transfer. Maximum flow limits avoid excessive pressure drop and tube erosion. Variable flow systems reduce pumping energy during partial load conditions while maintaining minimum flow through operating chillers.

## Condenser Water Supply Temperature

Condenser water entering temperature significantly impacts chiller efficiency through its effect on condensing temperature and compression lift. Cooling tower water supply typically ranges from 65°F to 85°F (18°C to 29°C) depending on ambient wet-bulb temperature and tower approach. Each 1°F (0.6°C) reduction in condenser water temperature improves efficiency approximately 1-2%. Free cooling opportunities arise when condenser water temperatures drop below chilled water return temperatures.

## Condenser Water Return Temperature

Water leaving the condenser carries rejected heat from the refrigeration cycle plus compressor power input. Return temperature typically exceeds supply by 8-12°F (4.4-6.7°C), representing condenser heat rejection. This temperature influences cooling tower selection and performance verification. Higher return temperatures indicate increased heat rejection or reduced flow rates, potentially signaling fouling or operational issues.

## Condenser Water Flow Rate

Condenser water flow affects condensing temperature and pressure through heat transfer coefficient variation. Design flow rates typically achieve 3-5 ft/s (0.9-1.5 m/s) tube velocity, higher than evaporator velocities due to greater fouling susceptibility. Flow reductions elevate condensing pressure, reducing efficiency and potentially triggering high-pressure cutouts. Excess flow wastes pumping energy without proportional efficiency gains due to diminishing heat transfer coefficient improvements.

## Approach Temperature

Approach temperature quantifies heat exchanger effectiveness by measuring the difference between refrigerant temperature and water temperature at heat exchanger outlets. Evaporator approach equals chilled water supply temperature minus evaporating refrigerant temperature, typically 2-4°F (1-2°C). Condenser approach equals condensing refrigerant temperature minus condenser water return temperature, typically 2-5°F (1-3°C). Increasing approach temperatures indicate fouling, inadequate flow, or refrigerant charge issues.

## Evaporator Approach

Evaporator approach temperature measures thermal effectiveness of chilled water heat exchanger. Lower approach values indicate superior heat transfer, enabling lower refrigerant temperatures for given chilled water temperatures. Flooded evaporators typically achieve 1-3°F (0.6-1.7°C) approach, while direct expansion designs range from 3-5°F (1.7-2.8°C). Approach degradation over time signals fouling accumulation, refrigerant charge loss, or non-condensable gas contamination requiring service attention.

## Condenser Approach

Condenser approach quantifies condenser heat transfer effectiveness. Shell-and-tube condensers typically achieve 2-4°F (1-2°C) approach to leaving water temperature. Air-cooled condensers reference ambient dry-bulb temperature with approaches from 10-20°F (5.6-11°C) depending on coil design and airflow. Evaporative condensers achieve 5-10°F (2.8-5.6°C) approach to ambient wet-bulb temperature. Rising approach values indicate fouling, airflow restrictions, or degraded heat transfer surfaces.

## Temperature Lift

Chiller lift represents the temperature difference between condensing and evaporating refrigerant, directly determining compression ratio and power input. Typical lift ranges from 35-55°F (19-31°C) for comfort cooling applications. Lift equals (condensing temperature) minus (evaporating temperature), where condensing temperature approximates condenser leaving water temperature plus condenser approach, and evaporating temperature approximates chilled water supply temperature minus evaporator approach. Each 1°F (0.6°C) lift increase raises compressor power approximately 2-3%.

## Impact on Compression Ratio

Compression ratio relates absolute discharge pressure to absolute suction pressure, governing compressor work input. Higher ratios demand increased work per unit mass of refrigerant, reducing efficiency and increasing discharge temperatures. Reciprocating and scroll compressors tolerate ratios up to 10:1, while centrifugal machines operate efficiently from 2:1 to 5:1. Screw compressors handle intermediate ranges. Excessive compression ratios trigger high discharge temperature cutouts and accelerate component wear.

## Relationship to Efficiency Metrics

Operating parameters directly influence kilowatts per ton (kW/ton) efficiency through their impact on thermodynamic cycle performance. Optimal efficiency occurs at low lift conditions with adequate flow rates and minimal approach temperatures. Part-load operation often improves efficiency through reduced lift when condenser water temperatures decrease with lower ambient conditions. Energy management strategies manipulate operating parameters within equipment constraints to maximize seasonal efficiency.

## Load Calculation Verification

Operating parameter monitoring verifies actual cooling load delivery. Evaporator-side calculation uses Q = 500 × GPM × (TR - TS) where TR represents return temperature and TS denotes supply temperature. Condenser-side verification employs Q = 500 × GPM × (TL - TE) + Power, incorporating leaving temperature TL, entering temperature TE, and electrical power input. Agreement between evaporator and condenser calculations within 5-10% validates sensor accuracy and identifies measurement errors.

## Refrigerant Saturation Temperatures

Refrigerant saturation temperatures at evaporator and condenser pressures define thermodynamic state points. Evaporator refrigerant temperature typically ranges from 32°F to 44°F (0°C to 7°C), maintained above freezing by controls monitoring chilled water temperature and refrigerant pressure. Condenser refrigerant temperature ranges from 70°F to 110°F (21°C to 43°C) depending on condenser water or ambient conditions. These temperatures determine available temperature differences driving heat transfer.

## Control System Response

Modern chiller controls continuously adjust operating parameters to maintain setpoints while optimizing efficiency. Chilled water temperature reset strategies raise supply temperature during reduced load conditions, lowering lift and improving efficiency. Condenser water temperature reset maintains optimal head pressure across varying ambient conditions. Demand-limiting algorithms constrain operating parameters to prevent exceeding electrical demand targets.

## Seasonal Variation Considerations

Operating parameters vary seasonally with ambient conditions affecting condenser temperatures. Summer design conditions establish maximum lift and lowest efficiency operation. Shoulder season and winter conditions enable reduced lift through lower condenser temperatures, significantly improving efficiency. Chiller plant optimization exploits these favorable conditions through appropriate control strategies and equipment sequencing.

## Monitoring and Trending

Continuous monitoring of operating parameters enables performance verification, fault detection, and predictive maintenance. Trending analysis identifies gradual degradation from fouling, refrigerant loss, or mechanical wear. Deviation from established performance baselines triggers investigation before failures occur. Building automation systems collect, store, and analyze parameter data supporting operational optimization and maintenance planning.

## Safety Limit Parameters

Operating parameter limits protect equipment from damage. Minimum chilled water flow prevents freeze-up. Maximum condenser pressure triggers high-pressure cutouts. Minimum evaporator pressure prevents freezing. Maximum discharge temperature protects compressor motors. Low oil pressure differential indicates lubrication loss. These safety parameters require proper calibration and regular verification ensuring equipment protection.
