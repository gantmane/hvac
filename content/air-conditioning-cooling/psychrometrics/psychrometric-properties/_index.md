---
title: "Psychrometric Properties"
description: "Detailed analysis of dry-bulb temperature, wet-bulb temperature, dewpoint, relative humidity, humidity ratio, enthalpy, and specific volume in HVAC systems."
date: "2026-01-04"
weight: 2
tags: ["dry-bulb", "wet-bulb", "dewpoint", "humidity-ratio", "enthalpy", "relative-humidity"]
categories: ["air-conditioning-cooling"]
---

Psychrometric properties define the thermodynamic state of moist air. Understanding these properties and their interrelationships enables accurate analysis of HVAC systems and processes.

## Dry-Bulb Temperature (DBT)

Dry-bulb temperature represents the actual air temperature measured by a standard thermometer shielded from radiation and moisture. It indicates the sensible heat content of air.

**Measurement**: Standard mercury or digital thermometer with dry sensing element, protected from direct solar radiation and precipitation.

**Physical Significance**: DBT directly relates to the kinetic energy of air molecules. Higher temperatures indicate greater molecular motion and higher sensible heat content.

The sensible heat content of dry air:

$$q_s = m c_p (T_2 - T_1)$$

where $c_p = 1.006$ kJ/(kg·K) at 20°C.

**HVAC Applications**:
- Space temperature control setpoints
- Outdoor design temperatures for load calculations
- Energy balance calculations
- Thermal comfort assessment (operative temperature)

**Typical Ranges**:
- Comfort cooling: 22-26°C (72-78°F)
- Comfort heating: 20-22°C (68-72°F)
- Outdoor design: -30°C to +45°C (-22°F to +113°F) depending on climate

## Wet-Bulb Temperature (WBT)

Wet-bulb temperature is the lowest temperature achievable through evaporative cooling at constant pressure. It represents the temperature indicated by a thermometer with wetted wick in moving air.

**Measurement Principle**: As water evaporates from the wick, it absorbs latent heat from the air, cooling the thermometer. Equilibrium is reached when heat transfer to the wick equals evaporative cooling.

**Theoretical Foundation**: Wet-bulb temperature approximates the adiabatic saturation temperature for air-water vapor mixtures:

$$h_1 + (W_{sat} - W_1) h_f = h_{sat}$$

where $h_f$ is enthalpy of liquid water at wet-bulb temperature.

**Relationship to Dry-Bulb**:

$$T_{wb} \leq T_{db}$$

Equality occurs only at saturation (100% RH). The wet-bulb depression $(T_{db} - T_{wb})$ indicates moisture content and evaporative cooling potential.

**Psychrometric Equation**: Relating wet-bulb to other properties:

$$W = W_{sat}(T_{wb}) - \frac{(T_{db} - T_{wb})(c_p + W_{sat} c_{pw})}{h_{fg}}$$

where $h_{fg}$ is latent heat of vaporization.

**HVAC Applications**:
- Cooling tower design and performance
- Evaporative cooling system analysis
- Enthalpy determination on psychrometric charts
- Outdoor air condition characterization

**Practical Measurement**:
- Sling psychrometer: Manual instrument with two thermometers
- Aspirated psychrometer: Motorized air movement over wet bulb
- Digital psychrometers: Electronic sensing with built-in ventilation

## Dewpoint Temperature (Td)

Dewpoint temperature is the temperature at which air becomes saturated (100% RH) when cooled at constant pressure and humidity ratio. At dewpoint, water vapor begins condensing.

**Fundamental Relationship**:

$$p_v = p_{ws}(T_d)$$

The water vapor pressure equals saturation pressure at the dewpoint temperature.

**Calculation from Humidity Ratio**:

$$T_d = T_{sat}\left(\frac{p_{atm} W}{0.622 + W}\right)$$

**Physical Significance**: Dewpoint indicates absolute moisture content independent of temperature. Unlike relative humidity, dewpoint changes only when moisture is added or removed.

**Condensation Analysis**: Condensation occurs on any surface below dewpoint temperature:

$$\dot{m}_{condensate} = \dot{m}_{air}(W_1 - W_2)$$

where $W_2 = W_{sat}(T_{surface})$

**HVAC Applications**:
- Determining when condensation occurs on windows, pipes, ducts
- Mold growth prevention (maintain surfaces above dewpoint)
- Dehumidification requirements
- Absolute humidity measurement

**Typical Values**:
- Dry climates: -10°C to +5°C (14°F to 41°F)
- Moderate climates: +5°C to +15°C (41°F to 59°F)
- Humid climates: +15°C to +25°C (59°F to 77°F)

**Dewpoint Depression**: The difference $(T_{db} - T_d)$ correlates inversely with relative humidity:
- Small depression: High RH
- Large depression: Low RH

## Relative Humidity (φ or RH)

Relative humidity is the ratio of actual water vapor pressure to saturation pressure at the same dry-bulb temperature:

$$\phi = \frac{p_v}{p_{ws}(T_{db})} \times 100\%$$

Alternatively expressed as ratio of humidity ratios:

$$\phi \approx \frac{W}{W_{sat}(T_{db})} \times 100\%$$

**Temperature Dependency**: Unlike humidity ratio and dewpoint, relative humidity varies with temperature even when absolute moisture content remains constant.

**Example**: Air at 20°C, 50% RH heated to 30°C:
- Humidity ratio: Unchanged
- Dewpoint: Unchanged
- Relative humidity: Drops to approximately 25%

**Comfort Implications**: ASHRAE Standard 55 recommends:
- Winter: 30-60% RH (prevents static electricity, dry skin)
- Summer: 40-60% RH (prevents excessive perspiration)

**Material Effects**:
- Wood movement: ±1% dimension change per 5% RH change
- Paper dimensional stability: Critical at 40-60% RH
- Electronics reliability: Optimal 40-50% RH

**Limitations**: RH alone doesn't indicate moisture content. Air at 10°C, 100% RH contains less moisture than air at 30°C, 50% RH.

## Humidity Ratio (W)

Humidity ratio (mixing ratio, moisture content) is the mass of water vapor per unit mass of dry air:

$$W = \frac{m_{vapor}}{m_{dry\,air}} \text{ kg/kg or lb/lb}$$

**Calculation from Vapor Pressure**:

$$W = 0.622 \frac{p_v}{p_{atm} - p_v}$$

The constant 0.622 derives from molecular weight ratio:

$$0.622 = \frac{M_{H_2O}}{M_{air}} = \frac{18.015}{28.965}$$

**Range of Values**:
- Minimum: 0 kg/kg (perfectly dry air, theoretical)
- Cold/dry: 0.001-0.003 kg/kg
- Moderate: 0.005-0.010 kg/kg
- Warm/humid: 0.015-0.025 kg/kg
- Maximum at 35°C: ~0.036 kg/kg at saturation

**Imperial Units**: Often expressed in grains per pound:

$$W_{gr/lb} = W_{kg/kg} \times 7000$$

**Latent Heat Calculations**: Humidity ratio directly determines latent cooling or heating:

$$q_l = \dot{m}_{air} \times (W_1 - W_2) \times h_{fg}$$

where $h_{fg} \approx 2501$ kJ/kg at 0°C.

**Conservation in Processes**:
- Sensible heating/cooling: W constant
- Humidification: W increases
- Dehumidification: W decreases
- Adiabatic mixing: $W_{mix} = \frac{m_1 W_1 + m_2 W_2}{m_1 + m_2}$

## Specific Enthalpy (h)

Specific enthalpy represents total heat content per unit mass of dry air, combining sensible and latent components:

$$h = h_{dry\,air} + W \times h_{water\,vapor}$$

**Expanded Form**:

$$h = c_p T + W(h_{fg,0} + c_{pw} T)$$

where:
- $c_p$ = specific heat of dry air = 1.006 kJ/(kg·K)
- $h_{fg,0}$ = latent heat at 0°C = 2501 kJ/kg
- $c_{pw}$ = specific heat of water vapor = 1.86 kJ/(kg·K)

**Numerical Equation (SI)**:

$$h = 1.006 T + W(2501 + 1.86 T) \text{ kJ/kg}$$

**Numerical Equation (IP)**:

$$h = 0.24 T + W(1061 + 0.444 T) \text{ Btu/lb}$$

**Energy Balance Applications**: Enthalpy enables direct energy calculations:

$$\dot{Q} = \dot{m}_{air}(h_1 - h_2)$$

**Process Analysis**:
- Sensible heating: Enthalpy increases, slope = $c_p + W c_{pw}$
- Humidification with steam: Enthalpy increases, slope = $\Delta h / \Delta W$
- Adiabatic saturation: Nearly constant enthalpy
- Cooling and dehumidification: Enthalpy decreases

**Typical Values**:
- Cold air: 0-20 kJ/kg (0-8 Btu/lb)
- Moderate: 30-50 kJ/kg (13-21 Btu/lb)
- Warm/humid: 60-100 kJ/kg (26-43 Btu/lb)

## Specific Volume (v)

Specific volume is the volume occupied by one unit mass of dry air plus its associated water vapor:

$$v = \frac{V_{total}}{m_{dry\,air}}$$

**Ideal Gas Relationship**:

$$v = \frac{R_a T}{p_a}$$

where $R_a = 287.055$ J/(kg·K) for dry air.

**Accounting for Vapor Pressure**:

$$v = \frac{R_a T}{p_{atm} - p_v}$$

**Numerical Approximation (SI)**:

$$v \approx \frac{287.055 T}{(p_{atm} - p_v) \times 1000} \text{ m}^3\text{/kg}$$

For standard pressure (101.325 kPa) and moderate humidity:

$$v \approx 0.00283 T \text{ m}^3\text{/kg (T in K)}$$

**Volume Flow Conversion**: Essential for relating mass and volumetric flow rates:

$$\dot{V} = \dot{m} \times v$$

$$\dot{m} = \frac{\dot{V}}{v}$$

**Example**: Air at 24°C (297 K), standard pressure:

$$v \approx 0.00283 \times 297 = 0.840 \text{ m}^3\text{/kg}$$

For 1000 m³/h volumetric flow:

$$\dot{m} = \frac{1000}{0.840} = 1190 \text{ kg/h}$$

**Temperature and Pressure Effects**:

$$\frac{v_2}{v_1} = \frac{T_2}{T_1} \times \frac{p_1}{p_2}$$

**Typical Values**:
- 0°C: 0.78 m³/kg (12.5 ft³/lb)
- 20°C: 0.84 m³/kg (13.5 ft³/lb)
- 40°C: 0.90 m³/kg (14.4 ft³/lb)

## Property Interdependencies

Any two independent properties completely define the state of moist air. Common combinations:

**Known: DBT + RH**
1. Calculate $p_{ws}(T_{db})$ from saturation tables
2. Calculate $p_v = \phi \times p_{ws} / 100$
3. Calculate $W = 0.622 p_v / (p_{atm} - p_v)$
4. Calculate $T_d$ from $p_v = p_{ws}(T_d)$
5. Calculate $h$ and $v$ from formulas

**Known: DBT + WBT**
1. Calculate $W_{sat}(T_{wb})$ from saturation conditions
2. Use psychrometric equation to find W
3. Calculate $p_v$ from W
4. Calculate RH, dewpoint, enthalpy, specific volume

**Known: DBT + Dewpoint**
1. Calculate $p_v = p_{ws}(T_d)$
2. Calculate W from vapor pressure
3. Calculate RH, enthalpy, specific volume
4. WBT requires iterative solution

## Measurement Instruments

**Dry-Bulb**:
- Mercury/alcohol thermometers
- Thermocouples, RTDs, thermistors
- Infrared sensors (surface temperature)

**Wet-Bulb**:
- Sling psychrometer (manual)
- Aspirated psychrometer (motorized)
- Electronic wet-bulb sensors

**Dewpoint**:
- Chilled mirror hygrometers (most accurate)
- Capacitive polymer sensors
- Calculated from RH and DBT

**Relative Humidity**:
- Capacitive polymer sensors
- Resistive sensors
- Hair hygrometers (mechanical)

**Humidity Ratio**:
- Calculated from other properties
- Direct measurement rare

## Summary Table

| Property | Symbol | Typical Range | Independent? | Applications |
|----------|--------|---------------|--------------|--------------|
| Dry-bulb | $T_{db}$ | -20 to 40°C | Yes | Temperature control |
| Wet-bulb | $T_{wb}$ | Lower than DBT | Yes | Cooling towers, evaporative systems |
| Dewpoint | $T_d$ | Lower than DBT | Yes | Condensation analysis |
| Relative Humidity | $\phi$ | 0-100% | Yes | Comfort, material stability |
| Humidity Ratio | W | 0-0.030 kg/kg | Yes | Latent load calculations |
| Enthalpy | h | 0-100 kJ/kg | No | Energy balances |
| Specific Volume | v | 0.75-0.95 m³/kg | No | Flow rate conversions |

Understanding these seven fundamental properties enables complete characterization of moist air conditions and accurate analysis of all HVAC processes.
