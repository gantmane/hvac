---
title: "Psychrometric Calculations"
description: "Step-by-step practical psychrometric calculation examples for HVAC system design including load analysis, equipment sizing, and process optimization."
date: "2026-01-04"
weight: 4
tags: ["HVAC-calculations", "load-analysis", "equipment-sizing", "psychrometric-examples"]
categories: ["air-conditioning-cooling"]
---

Practical psychrometric calculations translate theoretical understanding into equipment sizing and system design. This page provides detailed calculation examples for common HVAC applications.

## Example 1: Summer Air Conditioning Load

**Problem**: An office space requires 3000 m³/h of supply air at 15°C, 90% RH. Outdoor conditions are 33°C, 55% RH. Return air from space is 25°C, 50% RH. Minimum outdoor air is 20% of supply. Calculate cooling coil load.

**Solution**:

**Step 1**: Determine properties from psychrometric chart or calculations:

Outdoor Air (OA):
- $T_{oa} = 33°C$, $\phi = 55\%$
- $W_{oa} = 0.0165$ kg/kg
- $h_{oa} = 75.7$ kJ/kg
- $v_{oa} = 0.893$ m³/kg

Return Air (RA):
- $T_{ra} = 25°C$, $\phi = 50\%$
- $W_{ra} = 0.0099$ kg/kg
- $h_{ra} = 50.4$ kJ/kg
- $v_{ra} = 0.860$ m³/kg

Supply Air (SA):
- $T_{sa} = 15°C$, $\phi = 90\%$
- $W_{sa} = 0.0095$ kg/kg
- $h_{sa} = 39.1$ kJ/kg
- $v_{sa} = 0.826$ m³/kg

**Step 2**: Calculate mass flow rate:

$$\dot{m}_{sa} = \frac{\dot{V}_{sa}}{v_{sa}} = \frac{3000/3600}{0.826} = 1.01 \text{ kg/s}$$

**Step 3**: Calculate outdoor and return air flows:

$$\dot{m}_{oa} = 0.20 \times 1.01 = 0.202 \text{ kg/s}$$

$$\dot{m}_{ra} = 0.80 \times 1.01 = 0.808 \text{ kg/s}$$

**Step 4**: Calculate mixed air conditions:

$$T_{ma} = \frac{0.202 \times 33 + 0.808 \times 25}{1.01} = 26.6°C$$

$$W_{ma} = \frac{0.202 \times 0.0165 + 0.808 \times 0.0099}{1.01} = 0.0113 \text{ kg/kg}$$

$$h_{ma} = \frac{0.202 \times 75.7 + 0.808 \times 50.4}{1.01} = 55.4 \text{ kJ/kg}$$

**Step 5**: Calculate cooling coil load:

Total cooling:

$$q_t = \dot{m}_{sa}(h_{ma} - h_{sa}) = 1.01 \times (55.4 - 39.1) = 16.5 \text{ kW}$$

Sensible cooling:

$$q_s = \dot{m}_{sa} c_p (T_{ma} - T_{sa}) = 1.01 \times 1.02 \times (26.6 - 15) = 11.9 \text{ kW}$$

Latent cooling:

$$q_l = q_t - q_s = 16.5 - 11.9 = 4.6 \text{ kW}$$

Sensible Heat Ratio:

$$SHR = \frac{11.9}{16.5} = 0.72$$

**Step 6**: Calculate condensate removal:

$$\dot{m}_{condensate} = \dot{m}_{sa}(W_{ma} - W_{sa}) = 1.01 \times (0.0113 - 0.0095)$$

$$= 0.00182 \text{ kg/s} = 6.5 \text{ kg/h} = 6.5 \text{ L/h}$$

## Example 2: Winter Heating and Humidification

**Problem**: Size heating coil and humidifier for 2500 m³/h outdoor air system. Outdoor conditions: -5°C, 70% RH. Supply air required: 20°C, 35% RH.

**Solution**:

**Step 1**: Determine properties:

Outdoor Air:
- $T = -5°C$, $\phi = 70\%$
- $W = 0.0015$ kg/kg
- $h = 1.5$ kJ/kg
- $v = 0.770$ m³/kg

Supply Air:
- $T = 20°C$, $\phi = 35\%$
- $W = 0.0052$ kg/kg
- $h = 33.5$ kJ/kg

**Step 2**: Calculate mass flow:

$$\dot{m} = \frac{2500/3600}{0.770} = 0.901 \text{ kg/s}$$

**Step 3**: Sequential process - Preheat then humidify:

Preheat to 20°C (horizontal process):
- $T_1 = -5°C \rightarrow T_2 = 20°C$
- $W$ remains 0.0015 kg/kg
- $\phi$ drops to approximately 12%

$$q_{preheat} = \dot{m} c_p \Delta T = 0.901 \times 1.02 \times 25 = 23.0 \text{ kW}$$

**Step 4**: Humidification (vertical process):

Steam required:

$$\dot{m}_{steam} = \dot{m}_{air}(W_{final} - W_{initial})$$

$$= 0.901 \times (0.0052 - 0.0015) = 0.00333 \text{ kg/s} = 12.0 \text{ kg/h}$$

If using steam at 100°C, 2676 kJ/kg:

$$q_{humidifier} = 0.00333 \times 2676 = 8.9 \text{ kW}$$

**Total Energy**:

$$q_{total} = 23.0 + 8.9 = 31.9 \text{ kW}$$

## Example 3: Economizer Analysis

**Problem**: Air handling unit serves space with 75 kW total cooling load. Return air: 24°C, 50% RH at 10,000 m³/h. Minimum outdoor air: 2000 m³/h. Outdoor air: 20°C, 60% RH. Determine if 100% outdoor air economizer mode is beneficial.

**Solution**:

**Step 1**: Determine properties:

Return Air:
- $h_{ra} = 48.0$ kJ/kg
- $v_{ra} = 0.855$ m³/kg
- $\dot{m}_{ra} = (10000/3600)/0.855 = 3.25$ kg/s

Outdoor Air:
- $h_{oa} = 42.3$ kJ/kg (lower enthalpy!)
- $v_{oa} = 0.842$ m³/kg

**Step 2**: Compare cooling load with minimum OA vs. 100% OA:

**Minimum OA Mode**:

Mixed air enthalpy:

$$h_{ma} = \frac{0.2 \times 42.3 + 0.8 \times 48.0}{1.0} = 46.9 \text{ kJ/kg}$$

**100% OA Mode**:

$$h_{ma} = 42.3 \text{ kJ/kg}$$

**Step 3**: Calculate enthalpy difference:

$$\Delta h = 46.9 - 42.3 = 4.6 \text{ kJ/kg}$$

**Step 4**: Calculate free cooling benefit:

$$q_{free} = \dot{m} \Delta h = 3.25 \times 4.6 = 15.0 \text{ kW}$$

**Conclusion**: Using 100% outdoor air provides 15 kW of free cooling, reducing mechanical cooling load by 20% (15/75). Economizer mode is beneficial.

**Note**: This assumes fan power increase is negligible. Full analysis should include additional fan energy for increased outdoor air damper pressure drop.

## Example 4: Evaporative Cooling Feasibility

**Problem**: Evaluate direct evaporative cooling for warehouse in Phoenix, AZ. Design outdoor: 43°C, 15% RH. Required supply: ≤27°C. Evaporative cooler effectiveness: 85%.

**Solution**:

**Step 1**: Determine outdoor air properties:

At 43°C, 15% RH:
- Dewpoint: $T_d = 11.7°C$
- Wet-bulb: $T_{wb} = 21.3°C$

**Step 2**: Calculate achievable supply temperature:

$$T_{supply} = T_{db} - \varepsilon(T_{db} - T_{wb})$$

$$= 43 - 0.85(43 - 21.3) = 24.6°C$$

**Step 3**: Evaluate performance:

Supply temperature of 24.6°C meets requirement of ≤27°C.

Temperature reduction: $43 - 24.6 = 18.4°C$

**Step 4**: Calculate cooling effect per kg of air:

$$q = c_p \Delta T = 1.02 \times 18.4 = 18.8 \text{ kJ/kg}$$

For 10,000 m³/h airflow:

$$\dot{m} = (10000/3600)/0.92 = 3.02 \text{ kg/s}$$

$$q_{total} = 3.02 \times 18.8 = 56.8 \text{ kW}$$

**Conclusion**: Direct evaporative cooling is feasible and provides substantial cooling at very low energy cost (primarily fan power).

## Example 5: Cooling Coil Bypass Factor

**Problem**: Cooling coil manufacturer specifies apparatus dewpoint (ADP) of 8°C. Entering air: 28°C, 60% RH. Leaving air: 14°C, 90% RH. Calculate bypass factor and verify against typical values.

**Solution**:

**Step 1**: Properties:

Entering:
- $T_1 = 28°C$

Leaving:
- $T_2 = 14°C$

ADP:
- $T_{ADP} = 8°C$

**Step 2**: Calculate bypass factor:

$$BF = \frac{T_2 - T_{ADP}}{T_1 - T_{ADP}} = \frac{14 - 8}{28 - 8} = \frac{6}{20} = 0.30$$

**Step 3**: Evaluate result:

BF = 0.30 is higher than typical values (0.05-0.15 for 4-8 row coils).

**Possible causes**:
- Low number of coil rows (likely 2-3 rows)
- High air velocity reducing contact time
- Poor fin spacing reducing heat transfer surface

**Recommendation**: Consider coil with more rows or lower face velocity to achieve BF ≈ 0.10-0.15 for better dehumidification performance.

## Example 6: Multi-Zone Mixing

**Problem**: VAV system serves three zones mixing at return air plenum:

- Zone A: 500 m³/h at 24°C, 45% RH
- Zone B: 750 m³/h at 26°C, 50% RH
- Zone C: 1000 m³/h at 23°C, 55% RH

Calculate return air conditions entering AHU.

**Solution**:

**Step 1**: Calculate mass flows (assume $v \approx 0.85$ m³/kg):

$$\dot{m}_A = 500/(3600 \times 0.85) = 0.163 \text{ kg/s}$$

$$\dot{m}_B = 750/(3600 \times 0.85) = 0.245 \text{ kg/s}$$

$$\dot{m}_C = 1000/(3600 \times 0.85) = 0.327 \text{ kg/s}$$

$$\dot{m}_{total} = 0.735 \text{ kg/s}$$

**Step 2**: Determine individual properties:

Zone A: $W_A = 0.0084$ kg/kg, $h_A = 45.1$ kJ/kg
Zone B: $W_B = 0.0104$ kg/kg, $h_B = 52.6$ kJ/kg
Zone C: $W_C = 0.0098$ kg/kg, $h_C = 48.0$ kJ/kg

**Step 3**: Calculate mixed conditions:

$$T_{mix} = \frac{0.163 \times 24 + 0.245 \times 26 + 0.327 \times 23}{0.735} = 24.3°C$$

$$W_{mix} = \frac{0.163 \times 0.0084 + 0.245 \times 0.0104 + 0.327 \times 0.0098}{0.735} = 0.0095 \text{ kg/kg}$$

$$h_{mix} = \frac{0.163 \times 45.1 + 0.245 \times 52.6 + 0.327 \times 48.0}{0.735} = 48.9 \text{ kJ/kg}$$

**Step 4**: Calculate RH from $T$ and $W$:

At 24.3°C: $W_{sat} = 0.0191$ kg/kg

$$\phi = \frac{W_{mix}}{W_{sat}} = \frac{0.0095}{0.0191} = 49.7\% \approx 50\%$$

**Result**: Mixed return air is 24.3°C, 50% RH

## Calculation Best Practices

**Accuracy Considerations**:

1. **Property determination**: Use psychrometric charts for visualization, software for precision
2. **Significant figures**: Maintain 3-4 significant figures in intermediate calculations
3. **Rounding**: Round final answers to appropriate precision (±0.5°C, ±5% RH)
4. **Unit consistency**: Always verify units throughout calculations

**Common Errors to Avoid**:

- Using volume flows directly in mixing calculations (must convert to mass)
- Forgetting to account for altitude in property determination
- Assuming constant specific volume across wide temperature ranges
- Neglecting moisture in sensible heat calculations
- Using outdoor air temperature for mixed air in economizer mode

**Validation Checks**:

- Mixed air properties must lie between inlet streams
- Energy out cannot exceed energy in (conservation)
- Humidity ratio cannot be negative
- State points cannot exist left of saturation curve
- Results should align with psychrometric chart visualization

These practical calculation examples demonstrate the application of psychrometric principles to real HVAC design challenges, providing the foundation for equipment sizing and system optimization.
