---
title: "Cooling Load Calculations for HVAC Engineers"
description: "Heat gain methodology, CLTD/CLF procedures, radiant time series method, and internal load diversity for accurate cooling system sizing and energy analysis."
keywords: ["cooling load", "CLTD", "CLF", "solar heat gain", "radiant time series", "heat gain calculations"]
author: "Evgeniy Gantman"
date: 2026-01-04
weight: 13
---

# Cooling Load Calculations for HVAC Engineers

Cooling loads result from heat gains that must be removed to maintain comfort. Unlike heating (instantaneous heat loss), cooling involves thermal storage effects requiring time-lag analysis.

## Heat Gain vs. Cooling Load

**Heat Gain:** Instantaneous rate of heat transfer into space
**Cooling Load:** Rate at which heat must be removed (accounts for thermal mass storage)

**Radiant heat gains** (solar, lights, equipment): Absorbed by surfaces, released slowly
**Convective heat gains** (infiltration, ventilation): Immediate cooling load

## Solar Heat Gain

**Through windows:**

$$Q_{solar} = A \times SHGC \times SHGF \times CLF$$

Where:
- $A$ = window area (ft²)
- $SHGC$ = solar heat gain coefficient (0-1)
- $SHGF$ = solar heat gain factor from tables (Btu/(h·ft²))
- $CLF$ = cooling load factor (accounts for storage)

**Peak solar gain times:**
- East windows: 8-9 AM
- South windows: 12-1 PM
- West windows: 3-4 PM
- Horizontal (skylight): 12-1 PM

## Envelope Conduction

**Through walls/roofs:**

$$Q_{cond} = U \times A \times CLTD$$

Where CLTD = Cooling Load Temperature Difference

**CLTD accounts for:**
- Sol-air temperature (solar radiation heating surface)
- Thermal mass effect
- Time of day
- Wall/roof orientation

## Internal Heat Gains

**Occupants:**
- Sensible: 250 Btu/h per person (office work)
- Latent: 200 Btu/h per person
- Total: 450 Btu/h per person

**Lighting:**

$$Q = W \times 3.41 \times F_{use} \times F_{ballast} \times F_{SA}$$

Where $F_{SA}$ = return air plenum credit (0.6-0.8 if return air through plenum)

**Equipment:**

$$Q = W \times 3.41 \times F_{load} \times F_{motor} \times F_{use}$$

## Radiant Time Series Method

Modern ASHRAE method replaces CLF/CLTD.

**Process:**
1. Calculate instantaneous heat gains
2. Apply radiative/convective split
3. Convolve radiative gains with radiant time factors
4. Sum convective gains and time-delayed radiative loads

**Benefits:** More accurate for heavyweight construction, varying schedules

## Ventilation Load

$$Q_{vent} = 1.08 \times CFM_{OA} \times (T_{out} - T_{in})$$ (sensible)

$$Q_{vent,latent} = 4,840 \times CFM_{OA} \times (W_{out} - W_{in})$$ (latent)

**CFM from ASHRAE 62.1:**

$$V_{oz} = R_p \times P_z + R_a \times A_z$$

Where:
- $R_p$ = people outdoor air rate (typically 5 CFM/person)
- $R_a$ = area outdoor air rate (typically 0.06 CFM/ft²)

## Cooling Load Example Summary

**Typical office space peak load breakdown:**
- Solar: 25-35%
- Lights: 20-30%
- Equipment: 15-25%
- People: 10-15%
- Envelope conduction: 10-15%
- Ventilation: 15-25%

## Safety Factors

**Do NOT add safety factors** to calculated loads

**Acceptable adjustments:**
- Duct heat gain: 5-10%
- Fan heat: 2,500 Btu/h per ton
- Future expansion: Document separately

## Practical Applications

1. **Room-by-room:** Required for VAV, zone control
2. **Block load:** Acceptable for small residential
3. **Peak diversity:** Not all zones peak simultaneously (building load < sum of room peaks)

---

**Related Technical Guides:**
- [Load Calculation Methodology](/technical-guides/load-calculation-methodology/)
- [Psychrometric Processes](/technical-guides/psychrometric-processes/)
- [Solar heat Gain Calculations](/technical-guides/solar-heat-gain/)

**References:**
- ASHRAE Handbook of Fundamentals, Chapter 18: Nonresidential Cooling and Heating Load Calculations
- ASHRAE Radiant Time Series Method
