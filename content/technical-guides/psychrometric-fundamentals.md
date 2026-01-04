---
title: "Psychrometric Fundamentals for HVAC Engineers"
description: "Comprehensive guide to moist air properties, psychrometric charts, and state point analysis for professional HVAC engineers. Includes formulas, worked examples, and practical applications."
keywords: ["psychrometrics", "moist air properties", "psychrometric chart", "dry bulb temperature", "wet bulb temperature", "relative humidity", "humidity ratio", "enthalpy", "specific volume", "dew point"]
author: "Evgeniy Gantman"
date: 2026-01-04
weight: 1
---

# Psychrometric Fundamentals for HVAC Engineers

Psychrometrics forms the foundation of HVAC engineering practice. Understanding moist air behavior enables accurate equipment selection, system design, and troubleshooting. This guide provides the mathematical framework and practical tools for analyzing air-conditioning processes.

## Introduction to Psychrometrics

Psychrometrics is the study of thermodynamic properties of moist air. The atmosphere consists of dry air mixed with water vapor, and this mixture determines thermal comfort, equipment performance, and energy consumption in HVAC systems. Engineers use psychrometric analysis to:

- Calculate heating and cooling loads
- Design air handling equipment
- Size humidification and dehumidification systems
- Analyze energy recovery systems
- Troubleshoot system performance issues

Accurate psychrometric calculations require understanding seven fundamental properties of moist air. Two independent intensive properties define the thermodynamic state; all other properties can be calculated from these two.

## Fundamental Properties of Moist Air

### Dry Bulb Temperature (DBT)

Dry bulb temperature is the temperature of air measured by a standard thermometer freely exposed to the air but shielded from radiation and moisture. DBT represents the sensible heat content of air and is expressed in degrees Fahrenheit (°F) or Celsius (°C).

**Physical Significance:** DBT indicates the kinetic energy of air molecules. Higher DBT means greater molecular motion and higher sensible heat content.

**Measurement:** Standard mercury-in-glass thermometers, thermocouples, or resistance temperature detectors (RTDs) measure DBT. The sensing element must be shielded from radiant heat sources and positioned in the free airstream.

### Wet Bulb Temperature (WBT)

Wet bulb temperature is the temperature indicated by a thermometer with its bulb wrapped in a water-saturated wick and exposed to moving air. WBT represents the lowest temperature achievable through evaporative cooling at constant pressure.

**Physical Principle:** Water evaporates from the wick, absorbing latent heat from the air and lowering the thermometer reading. The rate of evaporation depends on the vapor pressure difference between the wick and the surrounding air. At equilibrium, the heat transfer from air to wick equals the latent heat of evaporation.

The relationship between DBT and WBT involves the Lewis number, which relates mass and heat transfer:

$$T_{wb} = T_{db} - \frac{(h_s - h)}{c_p \cdot Le^{2/3}}$$

Where:
- $T_{wb}$ = wet bulb temperature (°F)
- $T_{db}$ = dry bulb temperature (°F)
- $h_s$ = enthalpy at saturation (Btu/lb<sub>da</sub>)
- $h$ = actual enthalpy (Btu/lb<sub>da</sub>)
- $c_p$ = specific heat of dry air = 0.24 Btu/(lb·°F)
- $Le$ = Lewis number ≈ 1.0 for air-water vapor

**Measurement:** Sling psychrometers or aspirated psychrometers measure WBT. Air velocity across the wet wick must exceed 900 feet per minute (fpm) to ensure adiabatic saturation conditions.

### Dew Point Temperature

Dew point temperature is the temperature at which water vapor begins to condense when air is cooled at constant pressure and constant humidity ratio. At the dew point, air is saturated (RH = 100%).

**Physical Meaning:** Dew point represents the actual moisture content of air. Higher dew points indicate higher absolute humidity.

The fundamental relationship is:

$$p_v = p_{ws}(T_{dp})$$

Where:
- $p_v$ = partial pressure of water vapor (psi or in. Hg)
- $p_{ws}$ = saturation pressure at dew point (psi or in. Hg)
- $T_{dp}$ = dew point temperature (°F)

**Practical Application:** Dew point indicates condensation risk on cold surfaces. Surfaces below the dew point will experience condensation, leading to moisture damage, mold growth, and heat transfer degradation on chilled water pipes and cooling coils.

### Relative Humidity (RH)

Relative humidity is the ratio of actual water vapor pressure to saturation water vapor pressure at the same dry bulb temperature, expressed as a percentage.

$$\phi = \frac{p_v}{p_{ws}(T_{db})} \times 100\%$$

Where:
- $\phi$ = relative humidity (%)
- $p_v$ = actual vapor pressure (psi)
- $p_{ws}(T_{db})$ = saturation pressure at dry bulb temperature (psi)

**Alternative Definition:** RH can also be expressed as the ratio of humidity ratios:

$$\phi = \frac{W}{W_s} \times \frac{p_{total} - p_{ws}}{p_{total} - p_v} \times 100\%$$

For most HVAC applications, the pressure correction factor is approximately 1.0, simplifying to:

$$\phi \approx \frac{W}{W_s} \times 100\%$$

**Common Misconception:** RH does not directly indicate moisture content. Air at 75°F and 50% RH contains more moisture than air at 40°F and 50% RH because saturation pressure increases with temperature.

### Humidity Ratio (Specific Humidity)

Humidity ratio is the mass of water vapor per unit mass of dry air, expressed in pounds of moisture per pound of dry air (lb<sub>w</sub>/lb<sub>da</sub>) or grains per pound (gr/lb).

$$W = 0.622 \frac{p_v}{p_a}$$

Where:
- $W$ = humidity ratio (lb<sub>w</sub>/lb<sub>da</sub>)
- $0.622$ = ratio of molecular weights (water/air = 18.015/28.965)
- $p_v$ = partial pressure of water vapor (psi)
- $p_a$ = partial pressure of dry air (psi)

Since $p_a = p_{total} - p_v$ and $p_v = \phi \cdot p_{ws}$:

$$W = 0.622 \frac{\phi \cdot p_{ws}}{p_{total} - \phi \cdot p_{ws}}$$

**Units Conversion:**
- 1 lb<sub>w</sub>/lb<sub>da</sub> = 7000 grains/lb<sub>da</sub>
- Typical comfort range: 0.008 to 0.012 lb<sub>w</sub>/lb<sub>da</sub> (56 to 84 grains/lb)

**Engineering Significance:** Humidity ratio remains constant during sensible heating or cooling processes (horizontal lines on psychrometric chart). This property makes W useful for tracking moisture changes.

<div class="worked-example">

### Worked Example 1: Calculating Humidity Ratio

**Given:**
- Dry bulb temperature: 75°F
- Dew point temperature: 60°F
- Atmospheric pressure: 14.696 psia (sea level)

**Find:** Humidity ratio (W)

**Solution:**

Step 1: Find saturation pressure at dew point using ASHRAE correlation.

At 60°F, from steam tables: $p_{ws}(60°F) = 0.2563$ psia

Step 2: At dew point, vapor pressure equals saturation pressure.

$$p_v = p_{ws}(T_{dp}) = 0.2563 \text{ psia}$$

Step 3: Calculate partial pressure of dry air.

$$p_a = p_{total} - p_v = 14.696 - 0.2563 = 14.440 \text{ psia}$$

Step 4: Apply humidity ratio formula.

$$W = 0.622 \times \frac{p_v}{p_a} = 0.622 \times \frac{0.2563}{14.440} = 0.01104 \text{ lb}_w/\text{lb}_{da}$$

Converting to grains: $W = 0.01104 \times 7000 = 77.3$ grains/lb

**Answer:** W = 0.01104 lb<sub>w</sub>/lb<sub>da</sub> = 77.3 grains/lb<sub>da</sub>

</div>

### Specific Enthalpy

Specific enthalpy is the total heat content of moist air per unit mass of dry air, including sensible and latent heat components.

$$h = c_p T_{db} + W(h_{fg} + c_{pw} T_{db})$$

Where:
- $h$ = specific enthalpy (Btu/lb<sub>da</sub>)
- $c_p$ = specific heat of dry air = 0.24 Btu/(lb·°F)
- $T_{db}$ = dry bulb temperature (°F)
- $W$ = humidity ratio (lb<sub>w</sub>/lb<sub>da</sub>)
- $h_{fg}$ = latent heat of vaporization at 0°F = 1061 Btu/lb<sub>w</sub>
- $c_{pw}$ = specific heat of water vapor = 0.444 Btu/(lb·°F)

**Simplified Formula:** For temperature ranges typical in HVAC (32°F to 120°F):

$$h \approx 0.24 T_{db} + W(1061 + 0.444 T_{db})$$

**Practical Use:** Enthalpy determines total cooling or heating loads. The difference in enthalpy between two states multiplied by mass flow rate gives total heat transfer:

$$Q_{total} = \dot{m}_a (h_2 - h_1)$$

In terms of volumetric flow rate (CFM):

$$Q_{total} = 4.5 \times CFM \times \Delta h$$

Where 4.5 is the conversion factor (60 min/hr × 0.075 lb/ft³).

<div class="worked-example">

### Worked Example 2: Calculating Specific Enthalpy

**Given:**
- Dry bulb temperature: 75°F
- Humidity ratio: 0.01104 lb<sub>w</sub>/lb<sub>da</sub> (from previous example)

**Find:** Specific enthalpy

**Solution:**

Apply the enthalpy formula:

$$h = 0.24 T_{db} + W(1061 + 0.444 T_{db})$$

$$h = 0.24(75) + 0.01104[1061 + 0.444(75)]$$

$$h = 18.0 + 0.01104(1061 + 33.3)$$

$$h = 18.0 + 0.01104(1094.3)$$

$$h = 18.0 + 12.08 = 30.08 \text{ Btu/lb}_{da}$$

**Answer:** h = 30.08 Btu/lb<sub>da</sub>

**Components:**
- Sensible heat: 18.0 Btu/lb<sub>da</sub>
- Latent heat: 12.08 Btu/lb<sub>da</sub>

The latent component (40% of total) shows significant moisture contribution to enthalpy.

</div>

### Specific Volume

Specific volume is the volume of moist air per unit mass of dry air.

$$v = \frac{R_a T_{abs}(1 + 1.608W)}{p}$$

Where:
- $v$ = specific volume (ft³/lb<sub>da</sub>)
- $R_a$ = gas constant for dry air = 53.352 ft·lbf/(lb<sub>da</sub>·°R)
- $T_{abs}$ = absolute temperature (°R = °F + 459.67)
- $W$ = humidity ratio (lb<sub>w</sub>/lb<sub>da</sub>)
- $p$ = total pressure (lbf/ft²)
- 1.608 = ratio of gas constants (R<sub>w</sub>/R<sub>a</sub>)

**Simplified Formula at Sea Level (p = 14.696 psia = 2116.2 psf):**

$$v = 0.754 \frac{T_{abs}(1 + 1.608W)}{1}$$

For standard air (70°F, 50% RH at sea level): v ≈ 13.33 ft³/lb<sub>da</sub>

**Density Relationship:**

$$\rho = \frac{1}{v}$$

Standard air density: ρ = 0.075 lb/ft³

**Engineering Application:** Specific volume converts mass flow rate to volumetric flow rate:

$$CFM = \dot{m}_a \times v \times 60$$

Where $\dot{m}_a$ is in lb<sub>da</sub>/min.

## Saturation Pressure Correlations

Accurate psychrometric calculations require precise saturation pressure values. ASHRAE provides polynomial correlations for saturation pressure as a function of temperature.

**ASHRAE Saturation Pressure Formula:**

For temperature range -148°F to 392°F:

$$\ln(p_{ws}) = \frac{C_1}{T} + C_2 + C_3 T + C_4 T^2 + C_5 T^3 + C_6 \ln(T)$$

Where:
- $p_{ws}$ = saturation pressure (psia)
- $T$ = temperature (°R = °F + 459.67)
- $C_1$ through $C_6$ = correlation coefficients

**Coefficients for Ice (Below 32°F):**
- $C_1 = -1.0214165 \times 10^4$
- $C_2 = -4.8932428$
- $C_3 = -5.3765794 \times 10^{-3}$
- $C_4 = 1.9202377 \times 10^{-7}$
- $C_5 = 3.5575832 \times 10^{-10}$
- $C_6 = -9.0344688 \times 10^{-14}$, plus constant

**Coefficients for Water (Above 32°F):**
- $C_1 = -1.0440397 \times 10^4$
- $C_2 = -1.1294650 \times 10^1$
- $C_3 = -2.7022355 \times 10^{-2}$
- $C_4 = 1.2890360 \times 10^{-5}$
- $C_5 = -2.4780681 \times 10^{-9}$
- $C_6 = 6.5459673$

**Simplified Approximation (32°F to 100°F):**

For quick hand calculations:

$$p_{ws} \approx \exp\left(77.345 + 0.0057T - \frac{7235}{T}\right) / 10^9$$

Where T is in °R and $p_{ws}$ is in psia. Accuracy within 0.5% for typical HVAC temperature ranges.

## Psychrometric Chart Construction and Usage

The psychrometric chart graphically represents relationships between moist air properties. Understanding chart construction enables rapid property determination and process analysis.

### Chart Axes and Coordinates

**Horizontal Axis (X-axis):** Dry bulb temperature (°F or °C)
- Range: -20°F to 120°F for ASHRAE normal temperature chart
- Linear scale for easy interpolation

**Vertical Axis (Y-axis):** Humidity ratio (lb<sub>w</sub>/lb<sub>da</sub> or grains/lb<sub>da</sub>)
- Range: 0 to 0.030 lb<sub>w</sub>/lb<sub>da</sub> for normal temperature
- Linear scale on right side
- Enables direct moisture content reading

### Constant Property Lines

**1. Constant Relative Humidity (RH) Lines**
- Curved lines from lower left to upper right
- 100% RH line (saturation curve) bounds the chart
- Typical lines: 10%, 20%, 30%, 40%, 50%, 60%, 70%, 80%, 90%, 100%
- Lines represent constant vapor pressure ratio

**2. Constant Wet Bulb Temperature Lines**
- Diagonal lines sloping downward from left to right
- Nearly parallel to constant enthalpy lines
- Angle approximately 30° from horizontal
- Used for evaporative cooling process lines

**3. Constant Enthalpy Lines**
- Diagonal lines with slope slightly different from WBT lines
- Extend beyond saturation curve (for steam)
- Typical range: 10 to 50 Btu/lb<sub>da</sub>
- Parallel to adiabatic saturation lines

**4. Constant Specific Volume Lines**
- Diagonal lines steeper than enthalpy lines
- Slope approximately 60° from horizontal
- Typical values: 12.5, 13.0, 13.5, 14.0, 14.5 ft³/lb<sub>da</sub>

**5. Constant Dew Point Temperature**
- Horizontal lines (constant humidity ratio)
- Follow any horizontal path until intersection with saturation curve
- Read temperature at intersection = dew point

### Locating State Points

A unique psychrometric state requires two independent intensive properties. Common combinations:

**1. DBT + RH**
- Locate DBT on horizontal axis
- Follow vertical line upward
- Find intersection with RH curve
- This is the state point

**2. DBT + WBT**
- Locate DBT on horizontal axis
- Locate WBT on saturation curve
- Follow WBT line from saturation to DBT vertical line
- Intersection is state point

**3. DBT + Dew Point**
- Dew point determines humidity ratio directly
- Follow horizontal line from dew point on saturation curve
- Find intersection with DBT vertical line

**4. WBT + RH**
- Locate WBT on saturation curve
- Follow WBT line into chart
- Find intersection with RH curve

<div class="worked-example">

### Worked Example 3: Psychrometric Chart State Point Analysis

**Given:**
- Dry bulb temperature: 72°F
- Relative humidity: 60%

**Find:** All psychrometric properties using ASHRAE chart

**Solution:**

Step 1: Locate DBT = 72°F on horizontal axis

Step 2: Draw vertical line upward from 72°F

Step 3: Locate 60% RH curve

Step 4: Find intersection point (this is the state point)

Step 5: Read properties from chart:

**From direct reading:**
- Dry bulb temperature: 72°F (given)
- Humidity ratio: Read from right scale ≈ 0.0098 lb<sub>w</sub>/lb<sub>da</sub> = 68.6 gr/lb
- Specific volume: Follow constant volume line ≈ 13.65 ft³/lb<sub>da</sub>

**From curve intersections:**
- Wet bulb temperature: Follow WBT line to saturation curve ≈ 63.5°F
- Dew point: Follow horizontal line to saturation curve ≈ 59°F
- Enthalpy: Follow enthalpy line ≈ 28.5 Btu/lb<sub>da</sub>
- Relative humidity: 60% (given)

**Verification Calculation:**

Check humidity ratio using formula:

At 72°F: $p_{ws} \approx 0.3887$ psia

$$W = 0.622 \times \frac{0.60 \times 0.3887}{14.696 - 0.60 \times 0.3887} = 0.622 \times \frac{0.2332}{14.463} = 0.01003$$

Chart reading (0.0098) agrees within normal chart accuracy (±2-3%).

</div>

## Altitude Corrections

Standard psychrometric charts assume sea level pressure (14.696 psia or 29.92 in. Hg). Higher elevations have lower atmospheric pressure, affecting all pressure-dependent properties.

### Pressure-Altitude Relationship

$$p_{alt} = p_{sl} \left(1 - 6.875 \times 10^{-6} z\right)^{5.2559}$$

Where:
- $p_{alt}$ = pressure at altitude (psia)
- $p_{sl}$ = sea level pressure = 14.696 psia
- $z$ = elevation above sea level (feet)
- 5.2559 = adiabatic exponent for air

**Simplified Formula:**

$$p_{alt} \approx p_{sl} \exp\left(-\frac{z}{27,000}\right)$$

Accurate within 1% up to 10,000 feet elevation.

### Property Corrections

**Humidity Ratio:** Increases at altitude for same DBT and RH

$$W_{alt} = W_{sl} \times \frac{p_{sl}}{p_{alt}} \times \frac{p_{alt} - p_v}{p_{sl} - p_v}$$

**Specific Volume:** Increases approximately proportional to pressure ratio

$$v_{alt} = v_{sl} \times \frac{p_{sl}}{p_{alt}}$$

**Enthalpy:** Relatively unaffected (less than 1% change)

**Wet Bulb Temperature:** Decreases slightly at altitude

| Elevation (ft) | Pressure (psia) | Pressure Ratio | Volume Correction |
|---------------|-----------------|----------------|-------------------|
| 0 (sea level) | 14.696 | 1.000 | 1.000 |
| 1,000 | 14.175 | 0.965 | 1.037 |
| 2,000 | 13.664 | 0.930 | 1.076 |
| 3,000 | 13.164 | 0.896 | 1.116 |
| 4,000 | 12.676 | 0.863 | 1.159 |
| 5,000 | 12.197 | 0.830 | 1.205 |
| 7,500 | 11.099 | 0.755 | 1.324 |
| 10,000 | 10.102 | 0.687 | 1.455 |

**Engineering Implication:** At Denver (5,000 ft), specific volume is 20.5% higher than sea level. Equipment sized for sea level will move 20.5% more volume but the same mass of air. Fan power and duct sizes require adjustment.

## Standard Air Conditions

### ASHRAE Standard Conditions

Different standards exist for equipment rating, testing, and system design.

**Standard Air (Density basis):**
- Temperature: 70°F
- Density: 0.075 lb/ft³
- Pressure: 14.696 psia (sea level)
- Humidity: 0% (dry air)

**Standard Air (Comfort basis):**
- Temperature: 70°F
- Relative humidity: 50%
- Pressure: 14.696 psia
- Properties:
  - Humidity ratio: 0.00775 lb<sub>w</sub>/lb<sub>da</sub>
  - Enthalpy: 25.0 Btu/lb<sub>da</sub>
  - Specific volume: 13.33 ft³/lb<sub>da</sub>

**AMCA Fan Rating:**
- Temperature: 70°F
- Pressure: 29.92 in. Hg
- Density: 0.075 lb/ft³
- Dry air

**ARI Cooling Equipment Rating:**
- Indoor: 80°F DB / 67°F WB
- Outdoor: 95°F DB / 75°F WB

## Practical Applications

### Comfort Zone Determination

ASHRAE Standard 55 defines thermal comfort zones based on DBT and humidity:

**Summer Comfort Zone:**
- DBT range: 73°F to 79°F
- Humidity ratio: 0.004 to 0.012 lb<sub>w</sub>/lb<sub>da</sub>
- Relative humidity: 30% to 60% (preferred)

**Winter Comfort Zone:**
- DBT range: 68°F to 74°F
- Humidity ratio: 0.002 to 0.012 lb<sub>w</sub>/lb<sub>da</sub>
- Relative humidity: 30% to 60% (preferred)

### Equipment Design Conditions

**Typical Supply Air Conditions:**
- Cooling: 52-58°F, 90-95% RH
- Heating: 90-120°F, 10-30% RH

**Return Air Assumptions:**
- 75°F DB, 50% RH for cooling load calculations
- 70°F DB, 35% RH for heating load calculations

### Moisture Control Requirements

**Condensation Prevention:**
Surface temperatures must remain above dew point.

$$T_{surface} > T_{dp}$$

For 75°F, 50% RH indoor conditions: $T_{dp} \approx 55°F$

All surfaces below 55°F require insulation or vapor barriers.

**Dehumidification Requirement:**
When outdoor humidity ratio exceeds indoor design:

$$\dot{m}_{moisture} = CFM \times \rho \times (W_{outdoor} - W_{indoor})$$

## Summary of Key Formulas

**Humidity Ratio:**

$$W = 0.622 \frac{\phi \cdot p_{ws}}{p - \phi \cdot p_{ws}}$$

**Enthalpy:**

$$h = 0.24 T + W(1061 + 0.444 T)$$

**Specific Volume:**

$$v = \frac{53.352 \times T_{abs} (1 + 1.608W)}{144p}$$

**Relative Humidity:**

$$\phi = \frac{p_v}{p_{ws}(T)}$$

**Degree of Saturation:**

$$\mu = \frac{W}{W_s}$$

## Conclusion

Psychrometric fundamentals enable all HVAC load calculations and system design. Mastery of these seven properties—dry bulb temperature, wet bulb temperature, dew point, relative humidity, humidity ratio, enthalpy, and specific volume—provides the foundation for advanced HVAC engineering.

The psychrometric chart serves as the engineer's primary tool for rapid property determination and process visualization. Modern computer programs perform calculations with higher precision, but chart literacy remains essential for design verification and troubleshooting.

---

**Related Technical Guides:**
- [Psychrometric Processes](/technical-guides/psychrometric-processes/)
- [Cooling Load Calculations](/technical-guides/cooling-load-calculations/)
- [Airflow & Ventilation Calculations](/technical-guides/airflow-ventilation-calculations/)

**References:**
- ASHRAE Handbook of Fundamentals, Chapter 1: Psychrometrics
- ASHRAE Standard 55: Thermal Environmental Conditions for Human Occupancy
- Gatley, D.P. Understanding Psychrometrics, Third Edition
