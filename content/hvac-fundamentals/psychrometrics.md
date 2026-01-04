---
title: "Psychrometrics: Properties and Processes of Moist Air"
description: "Comprehensive psychrometric analysis including property calculations, chart interpretation, HVAC processes, and practical applications"
date: 2026-01-04
lastmod: 2026-01-04
author: "Evgeniy Gantman"
keywords:
  - psychrometrics
  - psychrometric chart
  - moist air
  - humidity calculations
  - enthalpy
  - dew point
categories:
  - HVAC Fundamentals
  - Air Properties
tags:
  - psychrometrics
  - thermodynamics
  - air conditioning
---

## Fundamentals

Psychrometrics quantifies thermodynamic and transport properties of moist air—a mixture of dry air and water vapor. These properties govern HVAC system design and analysis.

## Atmospheric Air Composition

Standard dry air at sea level:
- Nitrogen: 78.08%
- Oxygen: 20.95%
- Argon: 0.93%
- CO₂ and trace gases: 0.04%

Water vapor content varies: 0-4% by volume

## Dalton's Law

Total pressure equals sum of partial pressures:

{{< formula display="true" >}}
P_{total} = P_{da} + P_w
{{< /formula >}}

Where:
- $P_{da}$ = partial pressure of dry air (Pa)
- $P_w$ = partial pressure of water vapor (Pa)

Standard atmospheric: $P_{total} = 101,325$ Pa

## Fundamental Properties

### Humidity Ratio

Mass of water vapor per mass of dry air:

{{< formula display="true" >}}
W = 0.622 \frac{P_w}{P_{total} - P_w}
{{< /formula >}}

Units: kg water/kg dry air (or lb/lb)

Alternative form using relative humidity:

{{< formula display="true" >}}
W = 0.622 \frac{\phi \cdot P_{ws}}{P_{total} - \phi \cdot P_{ws}}
{{< /formula >}}

Where:
- $\phi$ = relative humidity (decimal)
- $P_{ws}$ = saturation pressure at dry-bulb temperature

### Saturation Pressure

Antoine equation (0-100°C):

{{< formula display="true" >}}
\ln P_{ws} = C_1 / T + C_2 + C_3 T + C_4 T^2 + C_5 T^3 + C_6 \ln T
{{< /formula >}}

Where $T$ = absolute temperature (K)

Simplified form (valid 0-50°C):

{{< formula display="true" >}}
P_{ws} = \exp\left(16.7 - \frac{4060}{T + 235}\right)
{{< /formula >}}

Result in kPa, $T$ in °C

### Relative Humidity

Ratio of actual to saturation vapor pressure:

{{< formula display="true" >}}
\phi = \frac{P_w}{P_{ws}} \times 100\%
{{< /formula >}}

At saturation: $\phi = 100\%$, $P_w = P_{ws}$

### Dew Point Temperature

Temperature at which condensation begins when air is cooled at constant pressure and humidity ratio:

{{< formula display="true" >}}
t_{dp} : P_w = P_{ws}(t_{dp})
{{< /formula >}}

Inverse of saturation pressure function

**Physical meaning:**
- $t_{dp} < t_{db}$ for unsaturated air
- $t_{dp} = t_{db}$ at saturation
- Cannot cool below $t_{dp}$ without condensation

### Wet-Bulb Temperature

Thermodynamic wet-bulb temperature represents adiabatic saturation:

{{< formula display="true" >}}
h = h_s(t_{wb}) + (W - W_s(t_{wb})) \cdot h_{fg}(t_{wb})
{{< /formula >}}

Where:
- $h$ = enthalpy of moist air (kJ/kg)
- $h_s$ = enthalpy at saturation
- $W_s$ = humidity ratio at saturation
- $h_{fg}$ = latent heat of vaporization

**Property:**
- $t_{dp} \le t_{wb} \le t_{db}$
- At saturation: $t_{dp} = t_{wb} = t_{db}$

### Specific Enthalpy

Total energy per unit mass of dry air:

{{< formula display="true" >}}
h = c_p t_{db} + W(h_{fg,0} + c_{pw} t_{db})
{{< /formula >}}

Where:
- $c_p$ = specific heat of dry air = 1.006 kJ/kg·K
- $c_{pw}$ = specific heat of water vapor = 1.86 kJ/kg·K
- $h_{fg,0}$ = latent heat at 0°C = 2501 kJ/kg

Simplified form:

{{< formula display="true" >}}
h \approx 1.006 t_{db} + W(2501 + 1.86 t_{db})
{{< /formula >}}

Units: kJ/kg dry air

### Specific Volume

Volume per unit mass of dry air:

{{< formula display="true" >}}
v = \frac{R_a T}{P_{total} - P_w} = \frac{287.05 (t_{db} + 273.15)}{P_{total} - P_w}
{{< /formula >}}

Units: m³/kg dry air

Where $R_a$ = gas constant for dry air = 287.05 J/kg·K

### Density

{{< formula display="true" >}}
\rho = \frac{1}{v}(1 + W)
{{< /formula >}}

Units: kg/m³ of moist air

## Psychrometric Chart

{{< diagram title="Psychrometric Chart Structure" >}}
graph TD
    A[Dry-Bulb Temp<br/>Horizontal Axis] --> C[Chart Properties]
    B[Humidity Ratio<br/>Vertical Axis] --> C
    C --> D[Constant RH Lines<br/>Curved]
    C --> E[Constant Enthalpy<br/>Diagonal]
    C --> F[Constant Wet-Bulb<br/>Diagonal]
    C --> G[Saturation Curve<br/>RH=100%]
    style C fill:#f96,stroke:#333
    style G fill:#69f,stroke:#333
{{< /diagram >}}

### Chart Elements

1. **Dry-bulb temperature:** Horizontal scale (°C or °F)
2. **Humidity ratio:** Vertical scale (kg/kg or gr/lb)
3. **Relative humidity:** Curved lines from lower-left to upper-right
4. **Wet-bulb temperature:** Diagonal lines sloping down-right
5. **Specific enthalpy:** Diagonal lines (parallel to wet-bulb)
6. **Specific volume:** Diagonal lines sloping up-right
7. **Saturation curve:** Upper boundary (RH = 100%)

## HVAC Processes

### Sensible Heating

Add heat without moisture change:

{{< formula display="true" >}}
\begin{aligned}
W_2 &= W_1 \text{ (horizontal line)} \\
q_s &= \dot{m}_{da} c_p (t_2 - t_1)
\end{aligned}
{{< /formula >}}

**Example:**
- Initial: 15°C, 50% RH
- Final: 25°C, ~25% RH
- Heat load: $\dot{m}_{da} \times 1.006 \times 10$ kW

### Sensible Cooling

Remove heat without dehumidification:

{{< formula display="true" >}}
\begin{aligned}
W_2 &= W_1 \\
q_s &= \dot{m}_{da} c_p (t_1 - t_2)
\end{aligned}
{{< /formula >}}

**Limit:** Cannot cool below dew point (condensation begins)

### Cooling and Dehumidification

Cooling coil below dew point:

{{< formula display="true" >}}
\begin{aligned}
q_{total} &= \dot{m}_{da}(h_1 - h_2) \\
q_{sensible} &= \dot{m}_{da} c_p (t_1 - t_2) \\
q_{latent} &= \dot{m}_{da} h_{fg} (W_1 - W_2)
\end{aligned}
{{< /formula >}}

**Sensible Heat Ratio (SHR):**

{{< formula display="true" >}}
SHR = \frac{q_{sensible}}{q_{total}} = \frac{q_s}{q_s + q_l}
{{< /formula >}}

{{< diagram title="Cooling and Dehumidification Process" >}}
graph LR
    A[Entering Air<br/>27°C, 60% RH] --> B[Cooling Coil<br/>ADP = 10°C]
    B --> C[Leaving Air<br/>13°C, 95% RH]
    C --> D[Supply Air<br/>After Reheat]
    style B fill:#9cf,stroke:#333
{{< /diagram >}}

**Apparatus Dew Point (ADP):**
Effective surface temperature of coil

**Bypass Factor:**

{{< formula display="true" >}}
BF = \frac{t_2 - t_{ADP}}{t_1 - t_{ADP}}
{{< /formula >}}

Typical values: 0.05-0.30 (lower is better contact)

### Heating and Humidification

Winter air conditioning:

{{< formula display="true" >}}
\begin{aligned}
q_{total} &= \dot{m}_{da}(h_2 - h_1) \\
\dot{m}_w &= \dot{m}_{da}(W_2 - W_1)
\end{aligned}
{{< /formula >}}

Where $\dot{m}_w$ = water addition rate (kg/s)

### Adiabatic Mixing

Two airstreams combine:

{{< formula display="true" >}}
\begin{aligned}
\dot{m}_3 &= \dot{m}_1 + \dot{m}_2 \\
h_3 &= \frac{\dot{m}_1 h_1 + \dot{m}_2 h_2}{\dot{m}_1 + \dot{m}_2} \\
W_3 &= \frac{\dot{m}_1 W_1 + \dot{m}_2 W_2}{\dot{m}_1 + \dot{m}_2}
\end{aligned}
{{< /formula >}}

**Graphical:** State 3 lies on straight line between states 1 and 2

**Lever rule:**

{{< formula display="true" >}}
\frac{\dot{m}_1}{\dot{m}_2} = \frac{|2-3|}{|1-3|}
{{< /formula >}}

## Practical Calculations

### Example 1: Property Determination

**Given:**
- Dry-bulb: $t_{db} = 25°C$
- Relative humidity: $\phi = 60\%$
- Pressure: $P = 101,325$ Pa

**Find:** $W$, $h$, $t_{wb}$, $t_{dp}$

**Solution:**

Saturation pressure at 25°C:

{{< formula display="true" >}}
P_{ws} = \exp\left(16.7 - \frac{4060}{25 + 235}\right) = 3.169 \text{ kPa}
{{< /formula >}}

Vapor pressure:

{{< formula display="true" >}}
P_w = 0.60 \times 3.169 = 1.901 \text{ kPa}
{{< /formula >}}

Humidity ratio:

{{< formula display="true" >}}
W = 0.622 \times \frac{1.901}{101.325 - 1.901} = 0.0119 \text{ kg/kg}
{{< /formula >}}

Enthalpy:

{{< formula display="true" >}}
h = 1.006 \times 25 + 0.0119 \times (2501 + 1.86 \times 25) = 55.3 \text{ kJ/kg}
{{< /formula >}}

Dew point (solve $P_w = P_{ws}(t_{dp})$):

{{< formula display="true" >}}
t_{dp} \approx 16.7°C
{{< /formula >}}

Wet-bulb (iterative or chart):

{{< formula display="true" >}}
t_{wb} \approx 18.9°C
{{< /formula >}}

### Example 2: Cooling Load

**Given:**
- Airflow: 5000 m³/h
- Entering: 28°C DB, 20°C WB
- Leaving: 13°C DB, 95% RH

**Find:** Cooling capacity (sensible, latent, total)

**Solution:**

From chart or calculations:
- State 1: $h_1 = 57.2$ kJ/kg, $W_1 = 0.0109$ kg/kg, $v_1 = 0.865$ m³/kg
- State 2: $h_2 = 34.5$ kJ/kg, $W_2 = 0.0092$ kg/kg

Mass flow rate:

{{< formula display="true" >}}
\dot{m}_{da} = \frac{5000}{0.865 \times 3600} = 1.604 \text{ kg/s}
{{< /formula >}}

Total cooling:

{{< formula display="true" >}}
q_{total} = 1.604 \times (57.2 - 34.5) = 36.4 \text{ kW}
{{< /formula >}}

Sensible cooling:

{{< formula display="true" >}}
q_s = 1.604 \times 1.006 \times (28 - 13) = 24.2 \text{ kW}
{{< /formula >}}

Latent cooling:

{{< formula display="true" >}}
q_l = 1.604 \times 2501 \times (0.0109 - 0.0092) = 6.8 \text{ kW}
{{< /formula>}}

Verification: $q_s + q_l = 24.2 + 6.8 = 31.0$ kW (discrepancy due to approximations)

SHR:

{{< formula display="true" >}}
SHR = \frac{24.2}{36.4} = 0.66
{{< /formula >}}

## Altitude Corrections

Standard pressure at elevation $z$ (m):

{{< formula display="true" >}}
P = 101.325 \left(1 - 2.25577 \times 10^{-5} z\right)^{5.2559}
{{< /formula >}}

**Example:** Denver (1609 m elevation)

{{< formula display="true" >}}
P = 101.325 \left(1 - 2.25577 \times 10^{-5} \times 1609\right)^{5.2559} = 83.4 \text{ kPa}
{{< /formula >}}

**Impact:** Higher humidity ratios for same RH; different enthalpy values

## Comfort Applications

### Summer Design

Typical supply conditions:
- 13-16°C DB
- 90-95% RH
- Delivered to space at 22-26°C, 50% RH

### Winter Design

Typical supply conditions:
- 35-50°C DB
- 20-30% RH
- Delivered to space at 20-23°C, 30-50% RH

## Advanced Topics

### Compressibility Factor

For precise calculations at high pressures:

{{< formula display="true" >}}
Pv = ZRT
{{< /formula >}}

Where $Z$ = compressibility factor (≈1 for atmospheric conditions)

### Virial Equation

Second virial coefficient accounts for non-ideal behavior:

{{< formula display="true" >}}
Z = 1 + \frac{B(T)P}{RT}
{{< /formula>}}

### Transport Properties

**Dynamic viscosity:**

{{< formula display="true" >}}
\mu = 1.715 \times 10^{-5} \left(\frac{T}{273.15}\right)^{0.7}
{{< /formula >}}

Units: Pa·s

**Thermal conductivity:**

{{< formula display="true" >}}
k = 0.0241 \left(\frac{T}{273.15}\right)^{0.9}
{{< /formula >}}

Units: W/m·K

## Measurement Techniques

{{< table title="Psychrometric Measurement Methods" >}}
| Property | Instrument | Accuracy | Response Time |
|----------|-----------|----------|---------------|
| **Dry-bulb** | RTD / Thermistor | ±0.2°C | 30-60 s |
| **Wet-bulb** | Sling psychrometer | ±0.5°C | 3-5 min |
| **RH** | Capacitive sensor | ±2% | 30-120 s |
| **Dew point** | Chilled mirror | ±0.2°C | 1-5 min |
| **Enthalpy** | Calculated | ±2% | N/A |
{{< /table >}}

## Software Tools

Modern psychrometric calculations use:
- ASHRAE Psychrometric Chart software
- EES (Engineering Equation Solver)
- CoolProp library (open-source)
- Excel add-ins with REFPROP

**Advantage:** Handle full range of conditions, altitude, and precision requirements

## Conclusion

Psychrometrics provides the analytical foundation for HVAC system design. The relationships between dry-bulb temperature, humidity ratio, enthalpy, and other properties enable quantitative analysis of air conditioning processes.

The psychrometric chart graphically represents these properties, allowing rapid visualization of heating, cooling, humidification, and mixing processes. Fundamental equations enable precise calculations for load determination and equipment sizing.

Mastery of psychrometric principles is essential for:
- Accurate load calculations
- Equipment selection and sizing
- Energy analysis and optimization
- Troubleshooting comfort and indoor air quality issues

Modern HVAC practice combines classical psychrometric analysis with computational tools for complex systems and operating conditions.

---

*Technical content by Evgeniy Gantman, HVAC Research Engineer*
