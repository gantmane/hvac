---
title: "Antifreeze Solutions for HVAC Systems"
aliases: ["Antifreeze Solutions for HVAC Systems"]
description: "Technical analysis of antifreeze solutions for snow melting and freeze protection systems. Comprehensive coverage of glycol properties, freezing point depression calculations, viscosity effects, and corrosion inhibitor requirements."
keywords:
  - antifreeze solutions
  - propylene glycol
  - ethylene glycol
  - freezing point depression
  - glycol concentration
  - viscosity effects
  - corrosion inhibitors
  - ASHRAE antifreeze
  - hydronic freeze protection
  - glycol properties
  - heat transfer fluids
  - snow melting antifreeze
weight: 4
---

Antifreeze solutions protect hydronic snow melting and freeze protection systems from ice formation during shutdown periods and sub-freezing operation. The selection and proper concentration of antifreeze directly affects system performance, pumping energy, heat transfer efficiency, and equipment longevity.

## Glycol Selection

Two glycol types dominate HVAC applications, each with distinct characteristics that govern selection.

### Propylene Glycol

Propylene glycol (PG) is the standard choice for occupied buildings and potable water applications due to its low toxicity classification. The FDA recognizes propylene glycol as Generally Recognized As Safe (GRAS) for food contact applications.

**Key Properties:**
- Molecular formula: C3H8O2
- Specific gravity: 1.036 at 77°F
- Specific heat: 0.60 Btu/(lb·°F) at 50% concentration
- Viscosity: 3.5 cP at 77°F (pure)
- Requires 5-10% higher concentration than ethylene glycol for equivalent freeze protection

Propylene glycol exhibits higher viscosity at equivalent concentrations compared to ethylene glycol, resulting in increased pumping energy. This viscosity penalty becomes pronounced below 20°F.

### Ethylene Glycol

Ethylene glycol (EG) provides superior thermal performance and lower viscosity but carries toxicity concerns that restrict its application.

**Key Properties:**
- Molecular formula: C2H6O2
- Specific gravity: 1.113 at 77°F
- Specific heat: 0.57 Btu/(lb·°F) at 50% concentration
- Viscosity: 1.5 cP at 77°F (pure)
- Better heat transfer coefficient than propylene glycol
- Toxic - fatal dose approximately 100 mL for adults

Use ethylene glycol only in closed systems with no possibility of cross-connection to potable water. Many jurisdictions prohibit or severely restrict ethylene glycol use in building systems.

## Freezing Point Depression

Pure water freezes at 32°F (0°C). Adding glycol depresses the freezing point through colligative property effects. The relationship between concentration and freezing point is non-linear.

### Concentration Calculation

The ASHRAE Handbook - HVAC Systems and Equipment provides freeze point data for various concentrations. Design concentration must account for the lowest expected ambient temperature plus a safety factor.

**Design Formula:**
```
Design Freeze Point = Lowest Ambient Temperature - Safety Margin
```

Typical safety margins range from 10-20°F depending on application criticality and monitoring capabilities.

### Key Concentration Points

| Propylene Glycol | Ethylene Glycol | Freeze Point | Burst Protection |
|------------------|-----------------|--------------|------------------|
| 30% by volume | 28% by volume | 7°F | 0°F |
| 40% by volume | 37% by volume | -10°F | -20°F |
| 50% by volume | 46% by volume | -28°F | -45°F |
| 60% by volume | 56% by volume | -55°F | -75°F |

Note that solutions continue to provide burst protection below the stated freeze point through slush formation rather than solid ice expansion.

## Viscosity Effects on System Performance

Glycol viscosity increases dramatically as temperature decreases and concentration increases. This affects three critical system parameters.

### Pump Head and Energy

Higher viscosity increases friction losses in piping systems. The relationship follows the Darcy-Weisbach equation where pressure drop increases proportionally with viscosity.

For a 50% propylene glycol solution at 20°F:
- Viscosity increases to approximately 25 cP (vs. 3.5 cP at 77°F)
- Pumping energy increases 40-60% compared to water
- Flow rates decrease if pump curves are not adjusted

### Heat Transfer Coefficient

Film coefficient decreases with increased viscosity, reducing heat exchanger effectiveness. The Sieder-Tate correlation shows heat transfer coefficient varies with (viscosity)^-0.14.

**Practical Impact:**
- 30% propylene glycol reduces heat transfer coefficient by 5-8%
- 50% propylene glycol reduces heat transfer coefficient by 15-20%
- Design heat exchangers for glycol service with 15-25% additional surface area

### Reynolds Number and Flow Regime

Higher viscosity reduces Reynolds number, potentially shifting flow from turbulent to transitional or laminar regime. This affects both pressure drop predictions and heat transfer calculations.

```
Re = ρVD/μ
```

Where turbulent flow (Re > 4000) typically exists with water, glycol solutions may operate at Re = 2000-3000, requiring careful hydraulic analysis.

## Corrosion Inhibitor Package

Pure glycol is mildly corrosive and oxidizes over time, producing acidic degradation products. Inhibitor packages protect system metals and stabilize the glycol solution.

### Inhibitor Types

Modern inhibitor packages typically contain:
- **Azole compounds**: Protect copper and brass (benzotriazole, tolyltriazole)
- **Molybdate or nitrite**: Protect ferrous metals and aluminum
- **pH buffers**: Maintain pH between 8.5-10.5 to prevent acidic corrosion
- **Anti-foam agents**: Reduce entrained air issues

### Inhibitor Depletion

Inhibitors degrade through several mechanisms:
1. **Oxidation**: Exposure to air depletes inhibitor reserves
2. **Thermal decomposition**: High temperatures (>250°F) accelerate breakdown
3. **Dilution**: System leaks and makeup water addition
4. **Precipitation**: Reaction with contaminants or incompatible materials

### Monitoring Requirements

ASHRAE Standard 147 recommends annual glycol testing for:
- **Concentration**: Verify freeze protection level (refractometer or hydrometer)
- **pH**: Should remain 8.0-10.5; values below 7.5 indicate degradation
- **Reserve alkalinity**: Measures remaining inhibitor capacity
- **Metals content**: Elevated copper or iron indicates corrosion

Replace glycol when pH drops below 8.0, reserve alkalinity falls to 50% of original, or when contamination exceeds acceptable limits.

## Concentration Verification

Field verification ensures designed freeze protection exists throughout system life.

**Refractometer Method:**
- Most accurate field measurement
- Temperature-compensated units read directly in freeze point
- Separate scales required for propylene vs. ethylene glycol
- Accuracy: ±2°F freeze point

**Hydrometer Method:**
- Measures specific gravity
- Requires temperature correction
- Less accurate than refractometer (±5°F)
- Suitable for approximate verification

## Design Recommendations

1. **Limit concentration to 60% by volume maximum.** Higher concentrations provide minimal freeze point benefit while substantially increasing viscosity and reducing heat capacity.

2. **Select propylene glycol unless specific conditions justify ethylene glycol.** Regulatory compliance and safety considerations outweigh the performance advantage in most applications.

3. **Design pumps and heat exchangers for glycol properties.** Never assume water-based sizing will accommodate glycol solutions.

4. **Specify inhibited glycol formulated for HVAC applications.** Automotive antifreezes contain silicates incompatible with HVAC equipment.

5. **Establish glycol testing and maintenance protocols.** Annual testing and five-year replacement intervals represent minimum acceptable practice.

6. **Account for reduced specific heat in load calculations.** A 50% glycol solution has approximately 75-80% of water's heat capacity, requiring increased flow rates or temperature differentials.

The ASHRAE Handbook - HVAC Systems and Equipment Chapter 21 provides comprehensive property tables and application guidance for antifreeze solutions in hydronic systems.
