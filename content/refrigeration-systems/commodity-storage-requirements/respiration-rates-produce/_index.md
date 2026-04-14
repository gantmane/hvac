---
title: "Respiration Rates in Produce Storage"
aliases: ["Respiration Rates in Produce Storage"]
weight: 10
description: "Quantifying produce respiration rates, temperature effects using Q10 factor, respiration heat generation, and impact on refrigeration load calculations for cold storage facilities."
keywords: ["produce respiration", "respiration heat", "Q10 factor", "refrigeration load", "climacteric fruit", "cold storage design", "respiration rate measurement"]
tags: ["produce respiration", "respiration heat", "Q10 factor", "refrigeration load", "climacteric fruit", "cold storage design", "respiration rate measurement"]
---

Respiration rate quantification is fundamental to refrigeration system design for produce storage. Fresh fruits and vegetables continue metabolic respiration after harvest, consuming oxygen and producing carbon dioxide, water vapor, and metabolic heat. This respiration heat constitutes a significant portion of the refrigeration load in cold storage facilities and must be accurately calculated for proper equipment sizing.

## Respiration Fundamentals

Respiration in harvested produce is an oxidative catabolic process that breaks down stored carbohydrates, proteins, and fats to provide energy for cellular maintenance. The general aerobic respiration equation is:

C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O + Heat

This exothermic reaction generates heat proportional to the respiration rate, which varies by commodity type, maturity stage, and storage temperature. Respiration depletes stored energy reserves, reduces product quality, and accelerates senescence. Refrigeration slows but does not stop this process.

The respiratory quotient (RQ) expresses the ratio of CO₂ produced to O₂ consumed:

RQ = moles CO₂ produced / moles O₂ consumed

For carbohydrate respiration, RQ equals 1.0. For fats and proteins, RQ ranges from 0.7 to 0.9. Measuring CO₂ production provides a practical method for determining respiration rates in storage facilities.

## Temperature Effects and Q10 Factor

Temperature exerts the strongest influence on produce respiration rates. The Q10 temperature coefficient quantifies this relationship, expressing the rate change for each 10°C temperature increase:

Q10 = (R₂/R₁)^[10/(T₂-T₁)]

Where:
- R₁, R₂ = respiration rates at temperatures T₁, T₂
- T₁, T₂ = storage temperatures in °C

For most produce, Q10 ranges from 2.0 to 2.5 between 0°C and 20°C, meaning respiration rate doubles to triples for each 10°C rise. At higher temperatures (20-30°C), Q10 may reach 3.0 or higher. This exponential relationship makes temperature control critical for extending storage life.

Example calculation: If lettuce respires at 40 mW/kg at 5°C and Q10 = 2.5, the rate at 15°C becomes:

R₁₅ = R₅ × Q10^[(T₂-T₁)/10] = 40 × 2.5^[(15-5)/10] = 40 × 2.5 = 100 mW/kg

A 10°C increase multiplies respiration heat by 2.5, demonstrating why maintaining design storage temperature is essential.

## Commodity Classification by Respiration Rate

Produce is classified into respiration rate categories at standard reference temperatures (0°C or 5°C), guiding storage system design requirements:

| Classification | Heat Generation at 5°C | Examples |
|----------------|------------------------|----------|
| Very Low | <5 mW/kg | Apples, grapes, citrus fruits, onions |
| Low | 5-15 mW/kg | Potatoes, carrots, cabbage, pears |
| Moderate | 15-25 mW/kg | Tomatoes, peppers, peaches, celery |
| High | 25-40 mW/kg | Strawberries, lettuce, spinach, broccoli |
| Very High | >40 mW/kg | Asparagus, sweet corn, mushrooms |

High respiration commodities require larger refrigeration capacity per unit mass and generally have shorter storage life. Design refrigeration loads must account for peak respiration rates occurring immediately after harvest before produce cools to storage temperature.

## Climacteric vs. Non-Climacteric Behavior

Fruits are classified by their respiration pattern during ripening:

Climacteric fruits exhibit a respiration peak during ripening accompanied by ethylene production. Examples include apples, bananas, tomatoes, avocados, and stone fruits. Respiration may increase 2-5 times peak levels during climacteric rise. Refrigeration delays but does not prevent this peak.

Non-climacteric fruits show steadily declining respiration after harvest without a distinct peak. Examples include citrus, grapes, strawberries, and cherries. These fruits must be harvested at proper maturity since they do not improve after harvest.

For climacteric fruits in long-term storage, controlled atmosphere (reduced O₂, elevated CO₂) suppresses respiration and delays the climacteric peak, extending storage life from weeks to months.

## Respiration Heat Generation

Respiration heat is typically expressed in milliwatts per kilogram (mW/kg) or BTU/(ton·day). The heat release equals the enthalpy change of the respiration reaction, approximately 2800 kJ per mole of glucose oxidized, equivalent to 16.7 kJ per gram of O₂ consumed.

Conversion between CO₂ production and heat generation:

Heat (W/kg) = CO₂ rate (mg CO₂/kg·h) × (16.7 kJ/g O₂) × (32 g O₂/44 g CO₂) × (1/3600 h/s)

For practical refrigeration load calculations, measured respiration values at specific temperatures are used directly from published tables (ASHRAE Handbook - Refrigeration Chapter 37).

## Measurement Methods

Respiration rate measurement employs several techniques:

Static Method: Produce sealed in container, CO₂ accumulation or O₂ depletion measured over time using gas analyzers. Simple but less accurate for rapid respiring commodities.

Flow-Through Method: Continuous airflow through sealed chamber containing produce, CO₂ concentration difference between inlet and outlet measured. More accurate for commercial quantities.

Manometric Method: Oxygen consumption measured by pressure change in sealed container with CO₂ absorbed by KOH solution. Classical research technique.

Infrared CO₂ Analyzer: Non-dispersive infrared (NDIR) sensors provide rapid, continuous CO₂ measurement with 0.01% resolution, suitable for automated storage monitoring.

All methods require temperature control to ±0.5°C during measurement since respiration is highly temperature-dependent.

## Impact on Refrigeration Load Calculations

Respiration heat contributes to the total refrigeration load alongside transmission, infiltration, product cooling, and equipment heat gains. For high-respiration commodities at warm pre-cooling temperatures, respiration may constitute 20-40% of total load.

Total respiration load (W) = Mass (kg) × Specific respiration rate (W/kg)

Load calculation must account for:

1. Temperature variation: Use actual product temperature, not air temperature, especially during cooling
2. Product mass: Full storage capacity determines peak respiration load
3. Time-weighted average: Respiration decreases as product cools from field temperature to storage temperature
4. Product turnover: Fast-moving cold storage has continuously elevated respiration from warm incoming product

For a 20,000 kg strawberry cold storage at 2°C with respiration rate of 45 mW/kg:

Respiration load = 20,000 kg × 0.045 W/kg = 900 W (3,070 BTU/h)

This represents substantial continuous heat input requiring equivalent refrigeration capacity. Design practice includes 10-20% safety factor above calculated respiration loads to accommodate commodity variation and measurement uncertainty.

## Respiration Control Strategies

Minimizing respiration extends storage life and reduces refrigeration requirements:

- Rapid pre-cooling: Reduce product temperature within hours of harvest
- Maintain design temperature: ±0.5°C control prevents respiration increases
- Controlled atmosphere: Reduced O₂ (1-3%) and elevated CO₂ (2-5%) can reduce respiration 50-80%
- Modified atmosphere packaging: Reduces respiration in consumer packages
- Ethylene removal: Prevents premature ripening in climacteric fruits

The combination of proper temperature control, appropriate atmosphere modification, and rapid cooling provides optimal respiration management, maximizing product quality retention while minimizing refrigeration energy consumption.
