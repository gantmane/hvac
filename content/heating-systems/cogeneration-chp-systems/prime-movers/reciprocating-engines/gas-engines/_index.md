---
title: "Natural Gas and Biogas Engines"
description: "Detailed analysis of spark-ignition gas engines for CHP applications including combustion strategies, fuel flexibility, emissions control, heat recovery integration, and performance optimization for natural gas, biogas, and alternative gaseous fuels."
date: 2026-01-04
weight: 1
---

Natural gas engines dominate CHP applications due to fuel availability, favorable economics, and clean combustion characteristics. These spark-ignition engines convert gaseous fuels to electricity with efficiencies of 35-42% while producing recoverable thermal energy from exhaust, jacket water, and auxiliary cooling circuits. The ability to utilize pipeline natural gas, biogas from waste treatment, or landfill gas provides fuel flexibility that diesel engines cannot match.

## Combustion Strategies and Engine Types

Gas engines employ two primary combustion approaches: lean-burn and stoichiometric. The selection fundamentally affects efficiency, emissions, and control complexity.

Lean-burn engines operate with substantial excess air, typically 150-200% of stoichiometric requirements (equivalence ratio φ = 0.5-0.65). The dilute mixture reduces peak combustion temperature from approximately 2800K to 2200K, dramatically suppressing thermal NOx formation. The lean combustion requires high-energy ignition systems (prechamber or plasma igniters) to reliably ignite the weak mixture.

The lean-burn approach achieves higher electrical efficiency (38-42% for large engines) due to increased specific heat ratio of the lean mixture and reduced heat transfer from lower peak temperatures. However, lean-burn engines cannot utilize three-way catalytic converters since excess oxygen prevents simultaneous reduction of NOx and oxidation of CO and hydrocarbons.

Stoichiometric engines maintain the chemically correct air-fuel ratio (φ = 1.0, or Lambda = 1.0). This precise ratio enables three-way catalyst operation where platinum-group metals simultaneously reduce NOx to N₂ and oxidize CO and hydrocarbons to CO₂ and H₂O. The control system maintains Lambda within ±2% of stoichiometric through closed-loop oxygen sensing.

Stoichiometric combustion sacrifices 3-5 percentage points of electrical efficiency compared to lean-burn due to higher heat transfer and lower specific heat ratio. However, the superior emissions control makes this approach necessary in regions with stringent NOx limits (sub-0.07 lb/MWh).

## Fuel Flexibility and Quality Requirements

Natural gas engines tolerate significant variation in fuel composition compared to diesel engines' strict fuel specifications. However, fuel characteristics affect performance, knock tendency, and maintenance requirements.

Pipeline natural gas typically contains 90-98% methane with ethane, propane, and inert diluents. The methane number quantifies knock resistance, with pure methane defining 100. Typical pipeline gas exhibits methane numbers of 70-95. Higher hydrocarbons and hydrogen increase knock tendency, requiring ignition timing retard that reduces efficiency.

The Wobbe Index characterizes fuel interchangeability:

$$WI = \frac{LHV}{\sqrt{SG}}$$

Where LHV represents lower heating value and SG represents specific gravity relative to air. Fuels with similar Wobbe Index produce similar heating rates at constant pressure, enabling fuel substitution without major adjustments. North American pipeline gas ranges from 1300-1400 Btu/scf Wobbe Index.

Biogas from anaerobic digestion contains 55-65% methane with 35-45% CO₂ and trace contaminants. The lower heating value (600-700 Btu/scf versus 1000 Btu/scf for natural gas) requires larger fuel system components and reduces power output by 20-30% at constant displacement. The high CO₂ content increases specific heat, slightly improving efficiency but also increasing exhaust flow.

Biogas contaminants require removal to prevent engine damage and excessive wear:

- Hydrogen sulfide (H₂S) must be reduced below 100-200 ppm to prevent corrosion of exhaust valves and catalysts
- Siloxanes from wastewater treatment must be reduced below 5-10 mg/m³ to prevent silicon deposits on valves and combustion chambers
- Moisture must be removed to prevent water accumulation in fuel systems and intake manifolds
- Particulates require filtration to 5 microns to protect injectors and carburetors

Landfill gas presents similar challenges with additional variability as waste composition changes. The nitrogen content from air infiltration reduces heating value and power output.

## Ignition Systems and Control

Conventional spark ignition systems struggle with lean mixtures due to reduced flame propagation speed and wider ignition energy requirements. Advanced ignition technologies extend lean operation limits.

Prechamber ignition creates a rich mixture in a small prechamber while the main chamber operates lean. The prechamber spark ignites the rich mixture, ejecting burning jets into the main chamber to initiate combustion. This approach enables equivalence ratios as low as 0.5 with reliable ignition.

Plasma ignition generates high-energy electrical discharges that create radical species and accelerate combustion initiation. The broader ignition volume compared to conventional spark plugs improves lean-burn reliability.

Ignition timing optimization balances efficiency and emissions. Advanced timing increases efficiency by allowing more complete expansion, but excessive advance causes knock that damages engines. The control system monitors knock sensors and retards timing when knock occurs.

The air-fuel ratio control maintains combustion within target ranges despite variations in fuel composition, ambient conditions, and engine wear. Mass airflow measurement, fuel flow measurement, and exhaust oxygen sensing enable closed-loop control with ±1-2% accuracy.

## Turbocharging and Air Handling

Turbocharging increases power density and efficiency by recovering exhaust energy to compress intake air. The radial flow turbine drives a centrifugal compressor that pressurizes intake air to 1.5-3.0 bar absolute (7-30 psig boost).

The compressor work increases air temperature according to:

$$T_2 = T_1 \left(\frac{P_2}{P_1}\right)^{(\gamma-1)/\gamma}$$

For compression from 14.7 to 30 psia with inlet temperature of 80°F (540°R), discharge temperature reaches:

$$T_2 = 540 \left(\frac{30}{14.7}\right)^{0.286} = 690°R = 230°F$$

This elevated temperature reduces charge density and increases knock tendency. Intercoolers (air-to-air or air-to-water heat exchangers) cool compressed air to 100-140°F, increasing density by 15-25% and improving knock margin.

The intercooler effectiveness quantifies cooling performance:

$$\varepsilon = \frac{T_{in} - T_{out}}{T_{in} - T_{coolant}}$$

With effectiveness of 0.70-0.85 for typical designs. The heat rejected to intercooler coolant (3-8% of fuel input) represents additional low-grade thermal recovery potential.

## Heat Recovery Integration

Gas engines produce thermal energy in multiple streams requiring integrated heat recovery design.

Exhaust gas at 750-950°F contains 30-35% of fuel input energy. An exhaust heat exchanger (economizer or heat recovery steam generator) cools exhaust to 280-320°F, recovering 25-30% of fuel input as useful thermal energy. Lower exhaust temperatures risk sulfuric acid condensation that corrodes exhaust piping.

The exhaust heat recovery calculation determines recovered thermal energy:

$$Q_{exh} = \dot{m}_{exh} \cdot c_p \cdot (T_{in} - T_{out})$$

For a 1000 kW engine with 18,000 lb/hr exhaust flow, cooling from 850°F to 300°F at $c_p = 0.26$ Btu/lb-°F yields:

$$Q_{exh} = 18000 \cdot 0.26 \cdot (850 - 300) = 2.57 \text{ MMBtu/hr}$$

Jacket water cooling at 190-210°F provides 20-25% of fuel input. A plate-and-frame heat exchanger transfers this energy to facility hot water while maintaining engine coolant within specifications (typically 180-200°F supply, 195-210°F return).

Combined heat recovery from exhaust and jacket water captures 50-55% of fuel input energy, achieving total CHP efficiencies of 85-90%.

## Emissions Control Technologies

NOx formation in gas engines follows thermal and prompt mechanisms. Thermal NOx dominates, forming at high temperatures through Zeldovich reactions:

$$\text{Rate}_{NOx} \propto e^{-E_a/RT} \cdot [O_2] \cdot [N_2]$$

The exponential temperature dependence drives emissions control strategies toward combustion temperature reduction.

Lean-burn combustion reduces NOx by lowering peak temperature. Emissions of 0.15-0.25 g/hp-hr (0.10-0.17 lb/MWh) are achievable without exhaust treatment. Further reduction requires selective catalytic reduction (SCR).

SCR systems inject ammonia or urea into exhaust upstream of a catalyst. The catalyst promotes reduction reactions:

$$4\text{NO} + 4\text{NH}_3 + \text{O}_2 \rightarrow 4\text{N}_2 + 6\text{H}_2\text{O}$$

$$2\text{NO}_2 + 4\text{NH}_3 + \text{O}_2 \rightarrow 3\text{N}_2 + 6\text{H}_2\text{O}$$

NOx reduction of 80-95% enables emissions below 0.07 lb/MWh. The SCR catalyst requires exhaust temperatures above 500°F for proper operation, potentially conflicting with heat recovery objectives.

Stoichiometric engines with three-way catalysts achieve simultaneous control:

$$2\text{CO} + 2\text{NO} \rightarrow 2\text{CO}_2 + \text{N}_2$$

$$\text{C}_x\text{H}_y + \text{NO} \rightarrow \text{CO}_2 + \text{H}_2\text{O} + \text{N}_2$$

Conversion efficiencies exceed 98% within the narrow operating window near stoichiometric. Oxygen storage materials (ceria-zirconia) expand this window to ±2% Lambda variation.

Carbon monoxide and unburned hydrocarbon emissions result from incomplete combustion. Catalytic oxidation converts these species to CO₂ and H₂O with conversion efficiencies of 90-98% when catalyst temperature exceeds 450-500°F.
