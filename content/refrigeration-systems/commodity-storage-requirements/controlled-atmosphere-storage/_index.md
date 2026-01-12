---
title: "Controlled Atmosphere Storage"
description: "Engineering principles of controlled atmosphere storage systems including oxygen and CO2 control, nitrogen generation, gas monitoring, room sealing, and respiration management for extended commodity storage life."
weight: 7
---

Controlled atmosphere (CA) storage extends commodity storage life by modifying atmospheric composition in addition to temperature and humidity control. CA storage reduces oxygen concentration from atmospheric 21% to 1-5% and elevates carbon dioxide from 0.04% to 1-5%, creating conditions that suppress respiration, reduce ethylene production, and slow senescence. This technology is critical for long-term storage of apples, pears, and other climacteric fruits where conventional refrigeration alone provides inadequate storage duration.

## Physiological Basis of CA Storage

Aerobic respiration consumes oxygen and produces carbon dioxide according to:

C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O + Energy

Reducing oxygen availability decreases respiration rate by limiting this reaction. However, excessively low O₂ levels (<1% for most commodities) induce anaerobic respiration, producing ethanol and acetaldehyde that cause off-flavors and tissue damage.

The respiratory quotient (RQ = CO₂ produced / O₂ consumed) typically equals 1.0 for carbohydrate metabolism. Deviations from this ratio indicate stress conditions. RQ >1.0 suggests anaerobic metabolism; RQ <1.0 indicates fat or protein metabolism.

CA storage exploits this physiology by reducing O₂ to the minimum level tolerated by the commodity—the lower compensation point—while maintaining sufficient oxygen for aerobic metabolism. This balance varies by commodity, cultivar, and maturity stage.

## Typical CA Conditions by Commodity

ASHRAE Refrigeration Handbook Chapter 25 provides detailed CA specifications. Representative conditions:

| Commodity | Temperature | O₂ (%) | CO₂ (%) | Storage Duration |
|-----------|-------------|--------|---------|------------------|
| Apples (Gala) | 0-1°C (32-34°F) | 2.5-3.0 | 2.5-3.0 | 6-8 months |
| Apples (Granny Smith) | -1-0°C (30-32°F) | 1.0-1.5 | 1.0-2.0 | 8-10 months |
| Apples (Honeycrisp) | 1-2°C (34-36°F) | 3.0 | 2.0-3.0 | 4-6 months |
| Pears (Bartlett) | -1-0°C (30-32°F) | 2.0-3.0 | 0-1.0 | 2-3 months |
| Pears (Anjou) | -1-0°C (30-32°F) | 1.0-2.0 | <1.0 | 6-8 months |
| Kiwifruit | -0.5-0°C (31-32°F) | 1.0-2.0 | 3.0-5.0 | 5-6 months |
| Avocados | 5-13°C (41-55°F) | 2.0-5.0 | 3.0-10.0 | 2-4 weeks |

These values represent starting points; optimal conditions require adjustment based on specific cultivar characteristics, harvest maturity, and desired market window.

## Room Sealing and Gas-Tightness

CA storage effectiveness depends on maintaining target gas concentrations, requiring gas-tight construction. Room leakage is quantified as pressure decay rate or equivalent leakage area.

Target specification: <0.1% of room volume per day at 250 Pa test pressure. For a 1000 m³ room, this allows <1 m³/day leakage.

**Sealing Methods**:

- **Walls and Ceiling**: Multiple coats of epoxy or urethane sealers applied to interior surfaces after insulation panel installation
- **Penetrations**: All pipe, duct, and electrical penetrations sealed with expanding foam and coated with liquid sealant
- **Doors**: Double-gasket systems with inflatable seals creating positive seal under pressure
- **Floor**: Vapor barrier beneath insulated floor or sealed concrete floor depending on design

Pressure testing verifies room integrity. The room is pressurized to 250 Pa (1.0 in. w.g.) and pressure decay monitored over 15-30 minutes. Acceptable decay rates depend on room volume and target atmosphere composition.

## Nitrogen Generation Systems

Nitrogen generation provides the primary method for reducing oxygen concentration. Two technologies dominate commercial applications:

### Pressure Swing Adsorption (PSA)

PSA systems use molecular sieves (zeolite) that preferentially adsorb oxygen under pressure. The process cycles between two beds:
- **Adsorption phase**: Compressed air (6-8 bar) flows through bed, oxygen adsorbs, nitrogen passes through
- **Regeneration phase**: Pressure reduced to atmospheric, releasing captured oxygen

PSA systems deliver 95-99% nitrogen purity at flow rates from 10-5000 m³/hr. Power consumption: 0.3-0.4 kWh per m³ of nitrogen at 99% purity.

### Membrane Separation

Hollow fiber membranes exploit different permeation rates between oxygen and nitrogen. Compressed air (7-10 bar) flows through membrane bundles. Oxygen permeates faster, creating nitrogen-enriched stream.

Membrane systems produce 95-99% nitrogen with lower capital cost but higher operating pressure requirements. Typical energy consumption: 0.4-0.5 kWh/m³ nitrogen.

**System Sizing**: Calculate nitrogen requirement from room volume, target O₂ reduction rate, and allowable fill time. For rapid pulldown (24-48 hours), generator capacity must handle both volume displacement and respiration O₂ production:

N₂ Flow = (V × ΔO₂) / (t × (1 - O₂_target)) + Respiration O₂ Rate

where V = room volume, ΔO₂ = oxygen reduction (%), t = pulldown time

## Carbon Dioxide Management

CO₂ concentration increases from respiration and must be controlled within target range. Excessive CO₂ causes tissue damage, browning, and off-flavors.

**CO₂ Scrubbing Systems**:

### Activated Carbon Scrubbers
Activated carbon adsorbs CO₂ at low temperatures (<5°C). System cycles between adsorption (cold) and regeneration (warm). Limited to applications where periodic regeneration is acceptable.

### Hydrated Lime Scrubbers
Calcium hydroxide (Ca(OH)₂) reacts with CO₂ forming calcium carbonate:

Ca(OH)₂ + CO₂ → CaCO₃ + H₂O

This irreversible reaction requires continuous lime replacement. Typical consumption: 1 kg lime removes 0.56 kg CO₂. Water vapor released humidifies room air.

### Molecular Sieve Scrubbers
Similar to PSA nitrogen generators but optimized for CO₂ removal. Higher selectivity than activated carbon with regeneration via pressure swing or temperature swing.

**Scrubber Sizing**: Based on respiration rate and target CO₂ concentration:

CO₂ Removal Rate = Mass × Respiration Rate × RQ

For 100,000 kg apples producing 2.5 mg CO₂/kg·h: removal rate = 250 g CO₂/hr = 6 kg/day

## Gas Monitoring and Control Systems

Accurate gas analysis enables closed-loop atmosphere control. Multiple analyzer technologies serve different accuracy and response time requirements:

**Oxygen Analyzers**:
- **Paramagnetic**: 0-25% range, ±0.1% accuracy, reference standard
- **Electrochemical cell**: 0-25% range, ±0.5% accuracy, lower cost
- **Zirconia**: High temperature applications, ±0.1% accuracy

**Carbon Dioxide Analyzers**:
- **Infrared (NDIR)**: 0-10% range, ±0.1% accuracy, industry standard
- **Thermal conductivity**: 0-20% range, ±0.5% accuracy
- **Electrochemical**: Limited life, requires frequent calibration

**Ethylene Analyzers**:
- **Electrochemical**: 0-100 ppm, ±5% accuracy
- **Gas chromatography**: 0-10 ppm, ±0.1 ppm accuracy, laboratory standard

Control systems integrate gas analysis with nitrogen generation and CO₂ scrubbing. PID loops maintain target setpoints with dead bands typically ±0.2% for O₂ and ±0.5% for CO₂.

Sample gas extraction requires moisture removal (condensate traps or desiccant) to prevent analyzer fouling. Sample flow rates: 0.5-2 L/min depending on analyzer technology.

## Establishment Protocol

CA conditions are established gradually to prevent physiological stress:

1. **Precooling**: Reduce commodity temperature to storage setpoint before sealing room (typically 24-48 hours)
2. **Oxygen Pulldown**: Reduce O₂ at 1-2% per day until reaching target
3. **CO₂ Buildup**: Allow natural increase from respiration or inject CO₂ to accelerate establishment
4. **Monitoring Period**: Verify stability, adjust scrubbing rate, confirm commodity tolerance

Rapid pulldown risks low-oxygen injury. Conservative protocols extend establishment over 5-10 days.

## Respiration Heat Load

Respiration generates metabolic heat that must be removed by refrigeration system. Heat production correlates with O₂ consumption:

Heat = O₂ Consumed (mL/kg·h) × 21.1 kJ/L O₂

CA storage reduces respiration heat by 50-70% compared to conventional storage. For apples:
- **Conventional storage** (0°C, air): 3-5 mg CO₂/kg·h ≈ 0.8-1.3 W/kg
- **CA storage** (0°C, 2% O₂, 2% CO₂): 1-2 mg CO₂/kg·h ≈ 0.3-0.5 W/kg

This reduction decreases refrigeration load but requires careful system design to maintain temperature uniformity at lower heat generation rates.

## Safety Considerations

Low-oxygen atmospheres present asphyxiation hazard. OSHA requires confined space protocols for CA rooms:

- **Atmosphere testing** before entry using portable O₂ analyzers
- **Forced ventilation** to restore breathable air (>19.5% O₂)
- **Entry permit system** documenting pre-entry checks
- **Continuous monitoring** during occupancy
- **Emergency procedures** including rescue equipment

Warning signs, alarm systems, and personnel training are mandatory for CA facilities.

## ASHRAE References

ASHRAE Refrigeration Handbook provides comprehensive CA storage guidance:
- **Chapter 25**: Detailed commodity-specific CA recommendations
- **Chapter 19**: Respiration rates and heat generation data
- **Chapter 47**: Terminology and measurement standards

These references inform system design, operation protocols, and troubleshooting procedures for controlled atmosphere storage applications.
