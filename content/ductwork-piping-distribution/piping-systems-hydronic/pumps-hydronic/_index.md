---
title: "Hydronic Pumps"
aliases: ["Hydronic Pumps"]
description: "Hydronic pump types, performance characteristics, affinity laws, pump curves, cavitation prevention, and control strategies for heating and cooling water distribution systems."
weight: 9
---

Hydronic pumps provide the motive force for water circulation through heating and cooling systems, converting mechanical shaft power into fluid pressure and velocity energy. Pump selection critically impacts system performance, energy consumption, reliability, and first cost.

## Pump Function and Performance

Pumps overcome friction losses in piping systems, coil pressure drops, and elevation changes to maintain design flow rates through all system components. The pump head equals the total system pressure drop at the required flow rate, typically expressed in feet of water column.

Pump curves graphically represent the relationship between flow rate and developed head, showing how pump output varies across its operating range. The intersection of the pump curve with the system resistance curve establishes the actual operating point.

Best efficiency point (BEP) represents the flow rate where the pump achieves maximum mechanical-to-hydraulic energy conversion efficiency. Operating significantly away from BEP increases energy consumption, generates noise, and reduces bearing life through radial thrust imbalances.

## Pump Performance Metrics

Pump efficiency varies with operating point, typically peaking at BEP and declining as flow deviates from this optimal condition. Wire-to-water efficiency accounts for motor and pump inefficiencies, typically ranging from 30 to 80 percent depending on pump size and operating conditions.

Net Positive Suction Head (NPSH) represents the absolute pressure at the pump inlet minus the fluid vapor pressure, determining cavitation margin. NPSH available must exceed NPSH required by an adequate margin (typically 3 to 5 feet) to prevent cavitation damage.

## Affinity Laws

Affinity laws predict pump performance changes resulting from speed or impeller diameter modifications. These relationships enable pump performance adjustment without replacing the entire unit.

Speed change effects follow cubic relationships: flow varies directly with speed, head varies with speed squared, and power varies with speed cubed. Reducing pump speed by 20 percent (to 80 percent of initial speed) reduces flow to 80 percent, head to 64 percent, and power to 51 percent of original values.

Impeller trim effects similarly follow predictable patterns, though with slightly different relationships due to volute geometry changes. These adjustments provide economical methods for matching pump output to actual system requirements when the as-installed system differs from original design assumptions.

## Control Strategies

Variable frequency drives (VFDs) provide efficient flow modulation by varying pump speed in response to system demand. VFD control dramatically reduces energy consumption in variable flow systems compared to constant speed operation with throttling valves.

Differential pressure control maintains a setpoint pressure differential at a critical system location, typically two-thirds distance along the most remote circuit. As control valves close in response to reduced load, the sensed differential pressure rises, prompting the VFD to reduce pump speed until the setpoint is restored.

Pressure setpoint reset further enhances energy efficiency by reducing the pressure differential setpoint as system load decreases. This strategy recognizes that lower flow rates require less differential pressure to overcome reduced friction losses in distribution piping.
