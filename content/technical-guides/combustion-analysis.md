---
title: "Combustion Analysis for HVAC Engineers"
description: "Stoichiometry, combustion efficiency calculations, flue gas analysis, and excess air determination for gas-fired HVAC equipment optimization."
keywords: ["combustion analysis", "combustion efficiency", "stoichiometry", "flue gas analysis", "excess air", "burner tuning"]
author: "Evgeniy Gantman"
date: 2026-01-04
weight: 11
---

# Combustion Analysis for HVAC Engineers

Combustion efficiency directly impacts operating costs and emissions. Flue gas analysis enables burner optimization, efficiency verification, and troubleshooting.

## Stoichiometric Combustion

**Natural gas (CH₄) complete combustion:**

$$\text{CH}_4 + 2\text{O}_2 + 7.52\text{N}_2 \rightarrow \text{CO}_2 + 2\text{H}_2\text{O} + 7.52\text{N}_2$$

**Theoretical air:** 9.52 lb air/lb fuel (2 O₂ + 7.52 N₂ from air)

**Actual air:** Always exceeds theoretical due to excess air requirement

## Excess Air

$$\%EA = \left(\frac{\text{Actual Air} - \text{Theoretical Air}}{\text{Theoretical Air}}\right) \times 100$$

From flue gas O₂:

$$\%EA \approx \frac{\%O_2}{0.264 \times (20.9 - \%O_2)}$$

**Typical excess air:**
- Atmospheric gas burner: 30-50% (4-7% O₂)
- Power burner: 10-20% (2-4% O₂)
- Too low: Incomplete combustion, CO formation
- Too high: Stack heat loss

## Combustion Efficiency

**Stack loss method:**

$$\eta_{comb} = 100 - L_{dry} - L_{moisture}$$

**Dry gas loss:**

$$L_{dry} = K \times \frac{T_{flue} - T_{air}}{%CO_2}$$

Where K ≈ 0.65 for natural gas

**Typical efficiencies:**
- Atmospheric boiler: 75-84%
- Power burner boiler: 80-85%
- Condensing boiler: 90-98%

## Flue Gas Analysis

**Measured parameters:**
- **O₂:** Indicates excess air (target: 2-6%)
- **CO₂:** Indicates completeness (target: 9-11% for natural gas)
- **CO:** Carbon monoxide (must be < 100 ppm)
- **Flue temperature:** Stack loss indicator

**CO formation causes:**
- Insufficient excess air
- Poor air-fuel mixing
- Flame impingement
- Insufficient combustion chamber volume

## Practical Applications

1. **Annual tuning:** Adjust air-fuel ratio for optimal efficiency
2. **Commissioning:** Verify design efficiency achieved
3. **Troubleshooting:** Diagnose sooting, high stack temperature, odors

---

**Related Technical Guides:**
- [Boiler Selection & Sizing](/technical-guides/boiler-selection-sizing/)
- [Thermodynamic Cycles](/technical-guides/thermodynamic-cycles/)

**References:**
- ASHRAE Handbook of HVAC Systems and Equipment, Chapter 31: Combustion and Fuels
- NFPA 54: National Fuel Gas Code
