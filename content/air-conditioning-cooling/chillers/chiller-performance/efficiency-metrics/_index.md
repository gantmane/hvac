---
title: "Chiller Efficiency Metrics"
aliases: ["Chiller Efficiency Metrics"]
description: "Detailed analysis of chiller efficiency metrics including kW/ton, COP, EER, IPLV, NPLV, AHRI 550/590 standards, and part-load performance evaluation methods for comprehensive energy assessment."
weight: 1
---

## Technical Overview

Chiller efficiency metrics quantify energy consumption relative to cooling output, enabling performance comparison across equipment types, manufacturers, and operating conditions. Multiple metrics exist because chillers operate across varying load conditions, with part-load performance often exceeding full-load ratings. Understanding these metrics enables proper equipment selection, energy modeling accuracy, and operational performance verification. Standardized test conditions ensure consistent comparison while recognizing real-world performance varies with site-specific conditions.

## Kilowatts Per Ton (kW/ton)

Kilowatts per ton represents the most direct efficiency metric, expressing electrical power input per ton of cooling capacity. Lower values indicate superior efficiency. The relationship kW/ton = kW_input / Tons_cooling provides simple calculation from measured parameters. Typical values range from 0.45 to 0.70 kW/ton for centrifugal chillers, 0.60 to 0.90 kW/ton for screw chillers, and 0.70 to 1.20 kW/ton for reciprocating and scroll machines. This metric applies universally across unit systems and requires no conversion factors.

## Coefficient of Performance (COP)

Coefficient of Performance expresses the ratio of cooling output to energy input, both in consistent units. COP = Cooling_Output / Energy_Input, where both quantities use Btuh, watts, or kilowatts. Higher COP values indicate better efficiency. The relationship between COP and kW/ton follows: COP = 3.517 / kW/ton, where 3.517 represents the conversion factor (12,000 Btuh per ton divided by 3,412 Btu per kWh). Typical COP values range from 5.0 to 7.8 for high-efficiency centrifugal chillers, corresponding to 0.45 to 0.70 kW/ton.

## Energy Efficiency Ratio (EER)

Energy Efficiency Ratio measures cooling capacity in Btuh divided by electrical power in watts, yielding units of Btu/Wh. EER = (Tons × 12,000) / (kW × 1,000), where 12,000 Btu/hr equals one ton of cooling. The conversion between EER and kW/ton follows: EER = 12 / kW/ton. Higher EER values indicate superior efficiency. Commercial chillers typically achieve EER values from 10 to 20, with the most efficient centrifugal machines exceeding 24 EER at full load under standard rating conditions.

## Integrated Part Load Value (IPLV)

Integrated Part Load Value represents weighted average efficiency across four specific part-load conditions per AHRI Standard 550/590. The weighting formula IPLV = 0.01A + 0.42B + 0.45C + 0.12D considers performance at 100% load (A), 75% load (B), 50% load (C), and 25% load (D), reflecting typical operating profiles in commercial buildings. IPLV values typically exceed full-load EER by 15-40% due to reduced lift at part-load conditions. This metric provides more representative seasonal performance than full-load ratings alone.

## Non-Standard Part Load Value (NPLV)

Non-Standard Part Load Value applies the same weighting as IPLV but at alternative operating conditions matching specific applications. NPLV accommodates different chilled water temperatures, condenser entering temperatures, or altitude conditions. For example, condenser water-cooled chillers may use 85°F entering condenser water instead of standard 85°F, or chilled water supply temperatures of 42°F rather than 44°F. NPLV enables more accurate predictions for applications with non-standard operating parameters.

## AHRI Standard 550/590 Conditions

AHRI Standard 550/590 establishes uniform test conditions for water-cooled and air-cooled chillers. Water-cooled chiller standard conditions specify 44°F chilled water leaving temperature, 54°F entering temperature (10°F rise), 85°F condenser water entering temperature, and 95°F leaving temperature (10°F rise). Air-cooled chiller conditions use 44°F chilled water leaving, 54°F entering, and 95°F outdoor dry-bulb temperature. These conditions enable direct comparison across manufacturers and equipment types.

## Part-Load Test Points

The four standard part-load points represent typical capacity utilization: 100% load represents design day peak conditions, 75% load reflects moderately high cooling requirements, 50% load indicates average operating conditions, and 25% load represents low-demand periods. Testing at each point establishes performance curves characterizing efficiency across operating ranges. Modern variable-speed centrifugal chillers demonstrate dramatic efficiency improvements at reduced loads, sometimes achieving 0.25 kW/ton or lower at 25% capacity.

## Impact of Operating Conditions

Actual chiller efficiency varies significantly from rated values based on operating conditions. Lower chilled water temperatures increase lift, reducing efficiency. Higher condenser water temperatures similarly elevate lift and power consumption. Each 1°F change in lift affects efficiency approximately 1-2%. Altitude reduces air density, affecting air-cooled chiller performance. Fouling degrades heat transfer, increasing approach temperatures and lift. Equipment age and maintenance quality impact efficiency through mechanical wear and refrigerant charge degradation.

## Efficiency Comparison by Chiller Type

Centrifugal chillers achieve the highest full-load efficiency (0.45-0.70 kW/ton), particularly at large capacities above 500 tons. Screw chillers provide good efficiency (0.60-0.90 kW/ton) with superior part-load performance compared to reciprocating types. Scroll chillers offer moderate efficiency (0.70-1.00 kW/ton) with excellent reliability. Reciprocating chillers typically range from 0.80-1.20 kW/ton but excel in small capacity applications. Absorption chillers use thermal rather than electrical energy, with COPs from 0.7 to 1.7 depending on technology.

## Seasonal Energy Efficiency Ratio (SEER)

Seasonal Energy Efficiency Ratio, while primarily applied to residential equipment, represents annual efficiency accounting for varying outdoor temperatures and part-load operation. SEER calculations integrate performance across temperature bins representing climate-specific frequency distributions. Commercial equivalents include Seasonal Coefficient of Performance (SCOP) used in European standards and Integrated Energy Efficiency Ratio (IEER) as an alternative to IPLV.

## Energy Cost Analysis

Energy cost calculations multiply operating hours by capacity utilization, efficiency, and electricity rates. Annual energy cost equals: Cost = Hours × Average_Load × kW/ton × $/kWh. The "Average_Load" and corresponding efficiency at that load point critically impact total costs. Since chillers rarely operate at full capacity, part-load efficiency metrics more accurately predict operating expenses than full-load ratings. Utility rate structures including demand charges and time-of-use rates complicate simple calculations.

## Impact of Variable Speed Drives

Variable-speed compressor drives dramatically improve part-load efficiency by eliminating capacity unloading losses. Fixed-speed centrifugal chillers unload capacity through inlet guide vane throttling, reducing efficiency at part load. Variable-speed drives maintain high efficiency across broader ranges, achieving 0.20-0.30 kW/ton at 30-50% loads. The additional cost of VFD technology typically provides 2-5 year payback periods in applications with significant part-load operation.

## Measurement and Verification

Chiller efficiency verification requires accurate measurement of electrical power, chilled water flow, chilled water temperatures, condenser water flow, and condenser water temperatures. Power measurement employs true power meters accounting for power factor. Flow measurement uses calibrated flow meters or balancing valve pressure drops with manufacturer curves. Temperature sensors require proper location and RTD or thermistor accuracy. Calculated efficiency compares against manufacturer performance maps, accounting for operating condition differences from rated points.

## Performance Degradation Over Time

Chiller efficiency degrades gradually through fouling accumulation, refrigerant charge loss, mechanical wear, and seal leakage. Annual degradation rates of 1-3% occur without proper maintenance. Regular tube cleaning, refrigerant charge verification, and mechanical inspection maintain design performance. Performance trending identifies degradation patterns, triggering maintenance before severe impacts occur. Properly maintained chillers sustain design efficiency for 20-30 years.

## Code and Standard Requirements

Energy codes increasingly mandate minimum efficiency levels and part-load performance standards. ASHRAE 90.1 specifies minimum full-load efficiency and IPLV requirements varying by chiller type, capacity, and configuration. Title 24 in California establishes stringent requirements exceeding federal minimums. International codes reference similar metrics adapted to local conditions. New construction and major renovations must demonstrate code compliance through specification of qualifying equipment.

## Selection Criteria Beyond Efficiency

While efficiency critically influences life-cycle costs, selection considers first cost, space requirements, maintenance complexity, reliability, noise levels, and operational flexibility. The most efficient chiller may not provide lowest life-cycle cost when considering installation complexity, maintenance expenses, and operational constraints. Economic analysis integrating all factors over expected equipment life determines optimal selection. Energy cost represents 60-80% of chiller life-cycle costs in most applications, justifying efficiency priority.

## Future Efficiency Trends

Advancing chiller technology continues improving efficiency through enhanced heat exchangers, advanced compressor designs, improved refrigerants, variable-speed drives, and sophisticated controls. Magnetic bearing centrifugal compressors eliminate oil systems and associated losses. Low-GWP refrigerants with favorable thermodynamic properties enable continued efficiency gains. Integrated controls optimizing entire chiller plants rather than individual machines promise additional 5-15% energy reductions through intelligent sequencing and load distribution.
