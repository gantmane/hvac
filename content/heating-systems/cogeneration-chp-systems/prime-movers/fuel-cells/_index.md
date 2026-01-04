---
title: "Fuel Cell Systems for CHP"
description: "Detailed analysis of fuel cell prime movers including electrochemical principles, fuel cell types (PAFC, MCFC, SOFC, PEMFC), thermodynamic efficiency limits, heat recovery characteristics, and integration strategies for high-efficiency distributed generation."
date: 2026-01-04
weight: 5
---

Fuel cells electrochemically convert fuel chemical energy directly to electricity without combustion, achieving electrical efficiencies of 40-60% while producing high-quality thermal energy for CHP applications. The absence of Carnot cycle limitations, minimal moving parts, and ultra-low emissions make fuel cells attractive for applications prioritizing efficiency, power quality, and environmental performance despite higher capital costs.

## Electrochemical Principles and Thermodynamic Efficiency

Fuel cells operate through electrochemical oxidation of hydrogen at the anode and reduction of oxygen at the cathode, producing electricity, water, and heat. The fundamental reaction:

$$\text{H}_2 + \frac{1}{2}\text{O}_2 \rightarrow \text{H}_2\text{O} + \text{electrical energy} + \text{heat}$$

The maximum theoretical efficiency derives from Gibbs free energy rather than Carnot efficiency:

$$\eta_{max} = \frac{\Delta G}{\Delta H} = \frac{-237 \text{ kJ/mol}}{-286 \text{ kJ/mol}} = 0.83$$

This 83% theoretical limit exceeds Carnot efficiency for low-temperature heat engines, explaining fuel cells' superior electrical efficiency. However, practical losses from electrode overpotentials, ionic resistance, and mass transport limit actual efficiency to 40-60%.

The cell voltage under load follows:

$$V_{cell} = E_{rev} - \eta_{act} - \eta_{ohmic} - \eta_{conc}$$

Where $E_{rev}$ represents reversible cell potential (1.23V at 25°C), $\eta_{act}$ represents activation overpotential from electrode kinetics, $\eta_{ohmic}$ represents resistive losses, and $\eta_{conc}$ represents concentration losses from reactant depletion. These overpotentials increase with current density, trading voltage (efficiency) for power density.

## Fuel Cell Types and Operating Characteristics

Phosphoric acid fuel cells (PAFC) operate at 150-220°C using liquid phosphoric acid electrolyte. These represent the most commercially mature fuel cell technology for distributed generation. PAFC systems achieve 40-42% electrical efficiency with thermal output at 140-180°F suitable for hot water or low-pressure steam.

The PAFC requires hydrogen fuel, typically produced through natural gas steam reforming in an integrated fuel processor:

$$\text{CH}_4 + \text{H}_2\text{O} \rightarrow 3\text{H}_2 + \text{CO}$$

$$\text{CO} + \text{H}_2\text{O} \rightarrow \text{H}_2 + \text{CO}_2$$

The fuel processor operates at 750-850°C, providing additional thermal energy for recovery. Total CHP efficiency reaches 80-85%.

Molten carbonate fuel cells (MCFC) operate at 600-650°C using a molten carbonate salt electrolyte. The high operating temperature eliminates the need for precious metal catalysts and enables internal reforming of natural gas directly at the anode:

$$\text{CH}_4 + \text{H}_2\text{O} \rightarrow 4\text{H}_2 + \text{CO}_2$$

MCFC systems achieve 47-50% electrical efficiency with thermal output at 400-650°C suitable for high-pressure steam or absorption cooling. The high-quality thermal output makes MCFC particularly attractive for industrial CHP applications.

Solid oxide fuel cells (SOFC) operate at 600-1000°C using a solid ceramic electrolyte (typically yttria-stabilized zirconia). The very high operating temperature enables internal reforming, fuel flexibility, and superior electrical efficiency of 50-60%.

The high-temperature SOFC exhaust (600-800°C) can drive a gas turbine bottoming cycle in hybrid configurations, achieving combined electrical efficiencies approaching 70%. SOFC-GT hybrids represent the highest efficiency distributed generation technology.

Proton exchange membrane fuel cells (PEMFC) operate at 60-100°C using a polymer membrane electrolyte. The low temperature enables rapid startup and good dynamic response, suiting automotive and portable applications. However, the low-grade thermal output (60-80°C) limits CHP applications. PEMFC electrical efficiency reaches 40-50%.

## Power-to-Heat Ratios and Thermal Integration

Fuel cells exhibit characteristic power-to-heat ratios determined by electrical efficiency and operating temperature:

| Fuel Cell Type | Electrical Efficiency | Thermal Output | Power-to-Heat Ratio |
|----------------|----------------------|----------------|-------------------|
| PEMFC | 40-50% | 40-50% at 60-80°C | 0.9-1.1 |
| PAFC | 40-42% | 42-45% at 140-180°F | 0.90-0.95 |
| MCFC | 47-50% | 30-35% at 400-650°C | 1.4-1.6 |
| SOFC | 50-60% | 25-30% at 600-800°C | 1.8-2.2 |

The high electrical efficiency of MCFC and SOFC results in less waste heat and higher power-to-heat ratios. These technologies suit facilities with substantial electrical loads and high-temperature thermal requirements.

PAFC thermal output at 140-180°F integrates well with hot water heating systems. A 400 kW PAFC system produces approximately 1.6 MMBtu/hr (470 kW thermal) suitable for space heating and domestic hot water in commercial buildings.

MCFC and SOFC high-temperature exhaust can generate 150-400 psig steam for industrial processes or drive absorption chillers. The thermal output quality enables tri-generation (power, heating, and cooling).

## Fuel Processing and Fuel Flexibility

Fuel cells operating directly on hydrogen achieve highest efficiency and zero carbon emissions. However, hydrogen infrastructure limitations necessitate on-site fuel processing for natural gas or other hydrocarbon fuels.

Steam reforming converts natural gas to hydrogen through endothermic reaction at 700-850°C:

$$\text{CH}_4 + \text{H}_2\text{O} \leftrightarrow 3\text{H}_2 + \text{CO}$$

The reforming reaction requires heat input, typically provided by combusting a portion of the fuel or cathode exhaust. The CO byproduct undergoes water-gas shift to produce additional hydrogen:

$$\text{CO} + \text{H}_2\text{O} \leftrightarrow \text{H}_2 + \text{CO}_2$$

Low-temperature fuel cells (PAFC, PEMFC) require CO cleanup to below 10-50 ppm to prevent catalyst poisoning. Preferential oxidation or methanation removes residual CO. High-temperature fuel cells (MCFC, SOFC) tolerate CO and can even oxidize it directly at the anode.

Internal reforming in MCFC and SOFC simplifies the fuel processor by performing reforming within the fuel cell stack. The endothermic reforming reaction absorbs heat, helping to control stack temperature. This integration improves efficiency and reduces system complexity.

Biogas and renewable fuels can power fuel cells with appropriate cleanup. Sulfur compounds must be removed to below 1-10 ppm to prevent catalyst poisoning and electrolyte degradation. Activated carbon, zinc oxide beds, or biological desulfurization achieves required cleanup levels.

## Emissions and Environmental Performance

Fuel cells produce minimal criteria pollutant emissions since oxidation occurs electrochemically rather than through high-temperature combustion. NOx formation requires temperatures above 1400°C, well above fuel cell operating temperatures.

Fuel cell system emissions primarily derive from fuel processing rather than the fuel cell stack. Natural gas reforming in PAFC systems produces NOx of 0.01-0.03 lb/MWh, more than an order of magnitude below gas engines. CO emissions remain below 0.01 lb/MWh. These ultra-low emissions enable siting in environmentally sensitive areas and eliminate most permitting complications.

Carbon dioxide emissions scale with fuel consumption. A PAFC system with 40% electrical efficiency produces:

$$\text{CO}_2 = \frac{3412 \text{ Btu/kWh}}{0.40} \times 117 \frac{\text{lb CO}_2}{\text{MMBtu}} = 997 \frac{\text{lb CO}_2}{\text{MWh}}$$

This compares to approximately 1200 lb CO₂/MWh for less efficient gas engines. When CHP thermal recovery displaces boiler fuel consumption, the net CO₂ reduction reaches 30-50% compared to separate generation.

## Operational Characteristics and Maintenance

Fuel cells operate continuously at baseload due to thermal cycling limitations and startup energy requirements. PAFC systems require 4-8 hours to reach operating temperature from cold start. MCFC and SOFC systems may need 24-48 hours. Once online, fuel cells can operate continuously for 6000-12000 hours between shutdowns.

Part-load performance varies by fuel cell type. PAFC and PEMFC maintain nearly constant efficiency from 100% to 30% load due to cell voltage characteristics. MCFC and SOFC show modest efficiency degradation (2-4 percentage points) at 50% load.

Maintenance requirements are significantly lower than combustion-based prime movers due to minimal moving parts. No oil changes, spark plugs, or valve adjustments are necessary. Primary maintenance involves:

- Air filter replacement (quarterly to annually)
- Fuel desulfurization bed replacement (annually)
- Coolant system maintenance (semi-annually)
- Reformer catalyst replacement (every 3-5 years)
- Stack replacement or refurbishment (every 7-15 years depending on technology)

Maintenance costs typically range from 0.005-0.015 per kWh, lower than reciprocating engines but higher than gas turbines on a per-kWh basis due to lower capacity factors.
