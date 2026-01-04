---
title: "CHP Fundamentals and Thermodynamic Principles"
description: "Detailed thermodynamic analysis of combined heat and power systems including first and second law efficiencies, power-to-heat ratios, fuel utilization effectiveness, capacity sizing methods, and operational modes for distributed generation applications."
date: 2026-01-04
weight: 1
---

Cogeneration fundamentally changes the thermodynamic proposition of distributed power generation by capturing and utilizing thermal energy that conventional power plants reject to the environment. Understanding the thermodynamic principles governing CHP operation enables accurate performance prediction, appropriate technology selection, and realistic economic evaluation.

## Energy Balance and First Law Efficiency

The first law of thermodynamics requires energy conservation across the CHP system. Fuel chemical energy converts to electrical work, useful thermal energy, and unavoidable losses:

$$Q_{fuel} = W_{elec} + Q_{useful} + Q_{loss}$$

Where $Q_{fuel}$ represents total fuel energy input based on lower heating value, $W_{elec}$ represents net electrical output (generator output minus auxiliary loads), $Q_{useful}$ represents recovered thermal energy delivered to the facility, and $Q_{loss}$ represents unavoidable losses to the environment through radiation, convection, and exhaust.

First law efficiency evaluates the fraction of fuel energy converted to useful outputs:

$$\eta_I = \frac{W_{elec} + Q_{useful}}{Q_{fuel}} = \frac{W_{elec} + Q_{useful}}{Q_{fuel}}$$

This metric can be decomposed into electrical and thermal components:

$$\eta_I = \eta_{elec} + \eta_{thermal}$$

Where electrical efficiency $\eta_{elec} = W_{elec}/Q_{fuel}$ typically ranges from 25-45% depending on prime mover technology and size, while thermal efficiency $\eta_{thermal} = Q_{useful}/Q_{fuel}$ ranges from 30-60%.

The thermal efficiency depends critically on the definition of "useful" thermal energy. Only thermal energy actually utilized by the facility contributes to overall efficiency. Thermal energy generated but rejected because it exceeds demand provides no benefit and reduces effective efficiency. This distinction drives the importance of matching CHP thermal output to facility thermal loads.

## Exergy Analysis and Second Law Efficiency

First law efficiency treats all energy forms equally, failing to recognize that electrical energy has higher thermodynamic value than low-temperature thermal energy. Exergy analysis addresses this limitation by quantifying the maximum theoretical work extractable from each energy stream.

The exergy of electrical work equals the work itself since electricity converts entirely to other energy forms. The exergy of thermal energy depends on delivery temperature:

$$Ex_{thermal} = Q_{useful}\left(1 - \frac{T_0}{T_h}\right)$$

Where $T_0$ represents ambient absolute temperature (typically 298 K) and $T_h$ represents thermal energy delivery absolute temperature. Higher delivery temperatures yield higher exergy and greater thermodynamic value.

Second law efficiency compares actual exergy output to maximum theoretical exergy from the fuel:

$$\eta_{II} = \frac{W_{elec} + Q_{useful}\left(1 - \frac{T_0}{T_h}\right)}{Q_{fuel}\left(1 - \frac{T_0}{T_{flame}}\right)}$$

Where $T_{flame}$ represents adiabatic flame temperature (approximately 2200 K for natural gas combustion). The denominator represents fuel exergy rather than fuel energy, properly accounting for the fundamental irreversibility of combustion.

For typical CHP systems delivering hot water at 200°F (367 K), the exergy factor equals $(1 - 298/367) = 0.188$. High-temperature steam at 400°F (478 K) yields a factor of 0.377, demonstrating the higher thermodynamic value of high-temperature thermal recovery.

Second law efficiency typically ranges from 35-50% for CHP systems, substantially lower than first law efficiency but more representative of thermodynamic quality. Systems delivering low-temperature heat exhibit particularly large differences between first and second law efficiency.

## Power-to-Heat Ratio

The power-to-heat ratio quantifies the relative electrical and thermal outputs:

$$\text{PHR} = \frac{W_{elec}}{Q_{useful}}$$

This ratio represents a fundamental characteristic of each prime mover technology, varying with operating conditions but generally bounded within a characteristic range. The PHR depends on the electrical efficiency and the temperature at which waste heat can be recovered:

$$\text{PHR} = \frac{\eta_{elec}}{\eta_{thermal}} = \frac{\eta_{elec}}{1 - \eta_{elec} - \eta_{loss}}$$

Different technologies exhibit characteristic power-to-heat ratios:

| Prime Mover | Electrical Efficiency | Thermal Efficiency | Typical PHR |
|-------------|---------------------|-------------------|-------------|
| Reciprocating Engine | 32-42% | 40-50% | 0.7-1.0 |
| Gas Turbine (simple) | 25-35% | 45-55% | 0.5-0.8 |
| Gas Turbine (advanced) | 35-42% | 40-50% | 0.8-1.2 |
| Microturbine | 26-33% | 45-55% | 0.5-0.7 |
| Steam Turbine (back-pressure) | 15-25% | 60-70% | 0.2-0.4 |
| Fuel Cell (PAFC) | 40-42% | 40-50% | 0.9-1.1 |
| Fuel Cell (SOFC) | 50-60% | 25-35% | 1.5-2.2 |

Matching the CHP system PHR to the facility's electrical-to-thermal load ratio maximizes utilization. A hospital with electrical load of 2000 kW and thermal load of 10 MMBtu/hr (2930 kW thermal) exhibits a load ratio of 0.68, well-suited to reciprocating engines or simple cycle gas turbines. A data center with minimal thermal loads (PHR > 5) cannot effectively utilize CHP unless absorption cooling provides a thermal sink.

## Fuel Utilization Effectiveness

Fuel utilization effectiveness compares CHP efficiency to the separate production of electricity and heat. The reference case assumes electricity purchased from the grid and heat generated in a conventional boiler:

$$\text{FUE} = \frac{W_{elec} + Q_{useful}}{W_{elec}/\eta_{grid} + Q_{useful}/\eta_{boiler}}$$

Where $\eta_{grid}$ represents the marginal grid efficiency (approximately 0.33-0.40 for fossil generation) and $\eta_{boiler}$ represents conventional boiler efficiency (0.75-0.85 for existing boilers).

For a CHP system with $\eta_I = 0.75$ compared to grid efficiency of 0.35 and boiler efficiency of 0.80, assuming equal electrical and thermal outputs ($W_{elec} = Q_{useful}$):

$$\text{FUE} = \frac{1 + 1}{1/0.35 + 1/0.80} = \frac{2}{2.857 + 1.25} = 0.487$$

This indicates the CHP system requires only 48.7% of the primary energy of separate generation, representing a 51.3% reduction in fuel consumption.

The fuel utilization effectiveness depends critically on the comparison assumptions. If the marginal grid electricity derives from high-efficiency combined cycle plants (55% efficiency), the CHP advantage diminishes. Conversely, comparing to coal-fired generation (33% efficiency) increases CHP benefits.

## Capacity Sizing Methodologies

CHP capacity selection balances capital cost, utilization factor, and displaced energy costs. Three primary sizing strategies exist: thermal-led, electrical-led, and hybrid optimization.

Thermal-led sizing matches CHP thermal output to facility baseload thermal demand. The system operates continuously to meet minimum thermal load, with supplemental heating meeting peak demands. Electrical output follows from the selected prime mover's PHR. This approach maximizes CHP utilization and thermal efficiency but may not optimize electrical economics.

The baseload thermal capacity can be determined from load duration curves:

$$Q_{CHP} = Q_{thermal,min} \cdot f_{operation}$$

Where $Q_{thermal,min}$ represents minimum thermal load and $f_{operation}$ represents the target operating fraction (typically 0.90-0.95 to allow for maintenance).

Electrical-led sizing matches electrical output to facility electrical demand, either baseload or full-load depending on economics. Thermal recovery becomes a beneficial byproduct but may exceed facility thermal requirements, requiring heat rejection and reducing overall efficiency. This approach suits facilities with limited thermal loads or high electrical costs.

Hybrid optimization simultaneously considers electrical and thermal economics:

$$\text{NPV} = \sum_{t=1}^n \frac{E_{elec}(P) \cdot c_{elec} + Q_{useful}(P) \cdot c_{thermal} - C_{fuel}(P) - C_{O\&M}(P)}{(1+r)^t} - C_{capital}(P)$$

Where the system capacity $P$ affects all operational parameters. Numerical optimization identifies the capacity maximizing NPV over the project lifetime.

Capacity factor quantifies utilization relative to maximum potential:

$$CF = \frac{\text{Annual kWh Generated}}{\text{Rated Capacity (kW)} \times 8760 \text{ hr/yr}}$$

CHP systems with capacity factors above 70% generally achieve attractive economics. Lower capacity factors indicate oversizing relative to consistent loads, increasing per-unit energy costs.

## Operating Modes

CHP systems operate in multiple configurations depending on electrical grid interconnection, control strategy, and facility requirements.

Baseload operation runs the CHP system at constant output continuously, meeting minimum facility electrical and thermal loads. Supplemental equipment provides additional capacity during peak periods. This mode maximizes CHP utilization and simplifies controls but requires careful sizing to avoid excess thermal generation.

Load-following operation modulates CHP output to track varying facility electrical or thermal demands. Electrical load-following maintains constant facility grid import/export, while thermal load-following matches heat recovery to thermal demand. Load-following improves energy utilization but requires turndown capability and responsive controls.

Grid-parallel operation maintains electrical connection to the utility, allowing power import when CHP output is insufficient and export when generation exceeds facility demand. This configuration provides maximum reliability through grid backup and potential revenue from exported power. However, utility interconnection requirements, standby charges, and unfavorable export rates can compromise economics.

Grid-independent (island) operation electrically isolates the facility, requiring the CHP system to exactly match electrical load through fast load-following controls. This mode provides energy security during grid outages but requires additional equipment (load bank for minimum loading, start-up power supply, sophisticated controls) and may compromise thermal utilization during electrical load-following.

The electrical-only mode operates the CHP system for power generation while rejecting all thermal energy. This inefficient mode only makes economic sense when electrical spark spread (electricity price minus gas price on equivalent energy basis) exceeds the cost of generation. Facilities should minimize electrical-only operation through appropriate sizing and controls.

## Performance Metrics

Multiple metrics quantify CHP system performance for different stakeholder perspectives.

Heat rate measures fuel consumption per unit electrical generation:

$$\text{HR} = \frac{Q_{fuel}}{W_{elec}}$$

Typically expressed in Btu/kWh, heat rate represents the inverse of electrical efficiency (3412 Btu/kWh ÷ HR = electrical efficiency). Lower heat rates indicate higher electrical efficiency. Combined cycle power plants achieve heat rates of 6200 Btu/kWh (55% efficient), while small reciprocating engines may reach 10,000 Btu/kWh (34% efficient).

Effective electrical efficiency accounts for thermal energy value:

$$\eta_{elec,eff} = \frac{W_{elec} + Q_{useful}/\eta_{boiler,alt}}{Q_{fuel}}$$

This metric credits the CHP system for avoiding boiler fuel consumption, providing a more complete picture than heat rate alone. For a CHP system with 35% electrical efficiency, 45% thermal efficiency, and displacing an 80% efficient boiler:

$$\eta_{elec,eff} = 0.35 + 0.45/0.80 = 0.91$$

The effective electrical efficiency of 91% demonstrates that CHP converts 91% of fuel energy to electricity-equivalent value.

Utilization factor measures the fraction of generated thermal energy actually utilized by the facility:

$$UF = \frac{Q_{utilized}}{Q_{recovered}}$$

High utilization factors (>0.85) indicate good matching between CHP thermal output and facility thermal demand. Low utilization factors suggest oversizing, poor load matching, or inadequate thermal integration.

The combined metric of first law efficiency multiplied by utilization factor represents true system effectiveness:

$$\eta_{eff} = \eta_I \times UF$$

A system with 75% first law efficiency but 60% thermal utilization achieves only 45% effective efficiency, no better than separate generation.
