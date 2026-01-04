---
title: "Psychrometric Processes in HVAC Systems"
description: "Detailed analysis of HVAC psychrometric processes including sensible heating, sensible cooling, humidification, dehumidification, and air mixing with formulas and worked examples."
keywords: ["psychrometric processes", "sensible heating", "sensible cooling", "humidification", "dehumidification", "air mixing", "cooling coil", "heating coil", "HVAC processes"]
author: "Evgeniy Gantman"
date: 2026-01-04
weight: 2
---

# Psychrometric Processes in HVAC Systems

Every HVAC system performs psychrometric processes to condition air for thermal comfort and process requirements. Understanding these processes enables equipment selection, energy analysis, and system troubleshooting. This guide examines the six fundamental processes: sensible heating, sensible cooling, cooling with dehumidification, humidification, chemical dehumidification, and air mixing.

## Process Representation on Psychrometric Chart

Psychrometric processes appear as paths on the psychrometric chart connecting initial and final state points. The path geometry indicates the type of process:

- **Horizontal line** (constant W): Sensible heating or cooling
- **Vertical line** (constant T): Pure humidification or dehumidification
- **Diagonal line toward saturation**: Cooling with dehumidification
- **Diagonal line away from saturation**: Heating with humidification
- **Straight line between points**: Air mixing
- **Constant WBT line**: Adiabatic saturation (evaporative cooling)

## Sensible Heating Process

Sensible heating adds heat without changing moisture content. Humidity ratio remains constant while dry bulb temperature increases.

### Process Characteristics

**On Psychrometric Chart:**
- Horizontal line moving right
- Constant humidity ratio (W₁ = W₂)
- Decreasing relative humidity
- Increasing dry bulb temperature
- Increasing enthalpy

**Physical Explanation:** Heat transfer to air increases molecular kinetic energy, raising temperature. No phase change occurs; water vapor mass remains constant. As temperature rises, saturation pressure increases, reducing relative humidity even though absolute moisture stays constant.

### Governing Equations

Energy balance for sensible heating:

$$Q_s = \dot{m}_a c_p (T_2 - T_1)$$

Where:
- $Q_s$ = sensible heat transfer rate (Btu/hr)
- $\dot{m}_a$ = mass flow rate of dry air (lb<sub>da</sub>/hr)
- $c_p$ = specific heat of air = 0.24 Btu/(lb·°F)
- $T_2$ = final temperature (°F)
- $T_1$ = initial temperature (°F)

**Volumetric Form:**

$$Q_s = 1.08 \times CFM \times \Delta T$$

Where:
- CFM = volumetric flow rate (cubic feet per minute)
- ΔT = temperature rise (°F)
- 1.08 = 60 min/hr × 0.075 lb/ft³ × 0.24 Btu/(lb·°F)

**Derivation of 1.08 Constant:**

$$Q = \frac{CFM \times 60 \text{ min/hr} \times 0.075 \text{ lb/ft}^3 \times 0.24 \text{ Btu/(lb·°F)} \times \Delta T}{1}$$

$$Q = 1.08 \times CFM \times \Delta T$$

This assumes standard air density (0.075 lb/ft³). For other densities:

$$Q_s = 60 \times CFM \times \rho \times c_p \times \Delta T$$

<div class="worked-example">

### Worked Example 1: Heating Coil Design

**Given:**
- Airflow: 5,000 CFM
- Inlet conditions: 55°F, 40% RH
- Outlet temperature: 95°F
- Sea level (standard density)

**Find:**
1. Heating load (Btu/hr and kW)
2. Outlet relative humidity
3. All outlet properties

**Solution:**

**Step 1: Calculate heating load**

$$Q_s = 1.08 \times CFM \times \Delta T$$

$$Q_s = 1.08 \times 5000 \times (95 - 55)$$

$$Q_s = 1.08 \times 5000 \times 40 = 216,000 \text{ Btu/hr}$$

Convert to kW: $216,000 / 3412 = 63.3$ kW

**Step 2: Determine outlet relative humidity**

At 55°F inlet: $p_{ws}(55°F) = 0.2141$ psia

Inlet vapor pressure:
$$p_v = 0.40 \times 0.2141 = 0.0856 \text{ psia}$$

Humidity ratio (constant during sensible heating):
$$W = 0.622 \times \frac{0.0856}{14.696 - 0.0856} = 0.00364 \text{ lb}_w/\text{lb}_{da}$$

At 95°F outlet: $p_{ws}(95°F) = 0.8153$ psia

Outlet RH:
$$RH_2 = \frac{p_v}{p_{ws}(95°F)} = \frac{0.0856}{0.8153} = 0.105 = 10.5\%$$

**Step 3: Calculate outlet enthalpy**

$$h_2 = 0.24(95) + 0.00364(1061 + 0.444 \times 95)$$

$$h_2 = 22.8 + 0.00364(1103) = 22.8 + 4.0 = 26.8 \text{ Btu/lb}_{da}$$

**Answer:**
- Heating load: 216,000 Btu/hr (63.3 kW)
- Outlet RH: 10.5%
- Outlet state: 95°F DB, 10.5% RH, W = 0.00364 lb/lb, h = 26.8 Btu/lb

**Note:** Low outlet humidity (10.5%) indicates need for humidification in winter heating applications.

</div>

### Applications

**Preheat Coils:** Protect downstream coils from freezing by warming outdoor air above 35-40°F before mixing or further cooling.

**Reheat Coils:** Raise supply air temperature after cooling/dehumidification to prevent overcooling spaces or achieve specific supply temperatures for VAV systems.

**Furnaces and Unit Heaters:** Provide space heating through direct sensible heat addition.

## Sensible Cooling Process

Sensible cooling removes heat without moisture condensation. Like sensible heating, humidity ratio remains constant.

### Process Characteristics

**On Psychrometric Chart:**
- Horizontal line moving left
- Constant humidity ratio
- Increasing relative humidity
- Decreasing dry bulb temperature
- Decreasing enthalpy

**Cooling Limit:** Process continues until saturation (100% RH). Further cooling causes condensation.

### Governing Equations

$$Q_s = 1.08 \times CFM \times (T_1 - T_2)$$

Where $T_1 > T_2$ for cooling.

**Temperature drop from heat removal:**

$$\Delta T = \frac{Q_s}{1.08 \times CFM}$$

<div class="worked-example">

### Worked Example 2: Sensible Cooling Without Condensation

**Given:**
- Airflow: 3,000 CFM
- Inlet: 85°F, 30% RH
- Desired outlet temperature: 65°F

**Find:** Cooling load and verify no condensation occurs

**Solution:**

**Step 1: Calculate cooling load**

$$Q_s = 1.08 \times 3000 \times (85 - 65) = 64,800 \text{ Btu/hr}$$

**Step 2: Check for condensation**

At 85°F inlet: $p_{ws} = 0.5959$ psia

Inlet vapor pressure: $p_v = 0.30 \times 0.5959 = 0.1788$ psia

Inlet humidity ratio:
$$W = 0.622 \times \frac{0.1788}{14.517} = 0.00766 \text{ lb}/\text{lb}$$

At 65°F: $p_{ws}(65°F) = 0.3056$ psia

Outlet RH if no condensation:
$$RH = \frac{0.1788}{0.3056} = 0.585 = 58.5\%$$

Since 58.5% < 100%, no condensation occurs. Process is pure sensible cooling.

**Answer:**
- Cooling load: 64,800 Btu/hr (19.0 kW)
- Outlet: 65°F, 58.5% RH
- No dehumidification

</div>

## Cooling with Dehumidification

Most cooling coils simultaneously reduce temperature and remove moisture. The process line crosses the saturation curve, causing condensation.

### Apparatus Dew Point (ADP)

The apparatus dew point represents the effective coil surface temperature for heat and mass transfer. Air leaving a perfect coil would be saturated at the ADP temperature.

**Bypass Factor (BF):** Real coils don't achieve perfect contact. Some air "bypasses" the coil:

$$BF = \frac{T_{leaving} - T_{ADP}}{T_{entering} - T_{ADP}}$$

Where:
- BF = bypass factor (0 to 1.0)
- Typical values: 0.05 to 0.30
- Lower BF = better coil performance

**Contact Factor:**

$$CF = 1 - BF$$

### Sensible Heat Ratio (SHR)

SHR indicates the proportion of sensible versus total cooling:

$$SHR = \frac{Q_{sensible}}{Q_{total}} = \frac{1.08 \times CFM \times \Delta T}{4.5 \times CFM \times \Delta h}$$

Simplified:

$$SHR = \frac{0.24 \Delta T}{\Delta h}$$

**Typical SHR Values:**
- Office spaces: 0.70 to 0.85
- Retail: 0.75 to 0.80
- Laboratories: 0.50 to 0.70
- Indoor pools: 0.30 to 0.50

### Governing Equations

**Total Cooling:**

$$Q_t = 4.5 \times CFM \times \Delta h$$

Where:
- 4.5 = 60 min/hr × 0.075 lb/ft³
- Δh = enthalpy difference (Btu/lb<sub>da</sub>)

**Sensible Cooling:**

$$Q_s = 1.08 \times CFM \times \Delta T$$

**Latent Cooling:**

$$Q_l = Q_t - Q_s$$

Or directly:

$$Q_l = 4840 \times CFM \times \Delta W$$

Where:
- 4840 = 60 min/hr × 0.075 lb/ft³ × 1076 Btu/lb (approximate $h_{fg}$)
- ΔW = humidity ratio reduction (lb<sub>w</sub>/lb<sub>da</sub>)

**Condensate Removal Rate:**

$$\dot{m}_{condensate} = 4.5 \times CFM \times (W_1 - W_2) \text{ lb/hr}$$

Convert to gallons per hour: divide by 8.33 lb/gal

<div class="worked-example">

### Worked Example 3: Cooling Coil Performance Analysis

**Given:**
- Airflow: 8,000 CFM
- Inlet conditions: 80°F DB, 67°F WB (60% RH)
- Outlet conditions: 55°F DB, 90% RH

**Find:**
1. Total, sensible, and latent cooling loads
2. Sensible heat ratio (SHR)
3. Apparatus dew point and bypass factor
4. Condensate removal rate

**Solution:**

**Step 1: Determine inlet properties**

From psychrometric chart or calculations:
- $T_1 = 80°F$
- $W_1 = 0.0116$ lb/lb
- $h_1 = 31.4$ Btu/lb

**Step 2: Determine outlet properties**

At 55°F, $p_{ws} = 0.2141$ psia

$$p_v = 0.90 \times 0.2141 = 0.1927 \text{ psia}$$

$$W_2 = 0.622 \times \frac{0.1927}{14.503} = 0.00827 \text{ lb/lb}$$

$$h_2 = 0.24(55) + 0.00827(1061 + 0.444 \times 55)$$

$$h_2 = 13.2 + 0.00827(1085.4) = 13.2 + 9.0 = 22.2 \text{ Btu/lb}$$

**Step 3: Calculate cooling loads**

Total cooling:
$$Q_t = 4.5 \times 8000 \times (31.4 - 22.2) = 4.5 \times 8000 \times 9.2 = 331,200 \text{ Btu/hr}$$

Convert: $331,200 / 12,000 = 27.6$ tons

Sensible cooling:
$$Q_s = 1.08 \times 8000 \times (80 - 55) = 1.08 \times 8000 \times 25 = 216,000 \text{ Btu/hr}$$

Latent cooling:
$$Q_l = 331,200 - 216,000 = 115,200 \text{ Btu/hr}$$

**Step 4: Calculate SHR**

$$SHR = \frac{Q_s}{Q_t} = \frac{216,000}{331,200} = 0.652$$

**Step 5: Determine ADP and bypass factor**

The process line from inlet (80°F, 60% RH) to outlet (55°F, 90% RH) crosses saturation curve at ADP.

Draw line on chart from state 1 to state 2. Extend to saturation curve.

ADP ≈ 50°F (from chart intersection)

Bypass factor:
$$BF = \frac{55 - 50}{80 - 50} = \frac{5}{30} = 0.167$$

Contact factor: $CF = 1 - 0.167 = 0.833$ or 83.3%

**Step 6: Condensate removal**

$$\dot{m}_{cond} = 4.5 \times 8000 \times (0.0116 - 0.00827)$$

$$\dot{m}_{cond} = 36,000 \times 0.00333 = 120 \text{ lb/hr}$$

Gallons per hour: $120 / 8.33 = 14.4$ gal/hr

**Answers:**
- Total cooling: 331,200 Btu/hr (27.6 tons)
- Sensible cooling: 216,000 Btu/hr
- Latent cooling: 115,200 Btu/hr
- SHR: 0.652
- ADP: 50°F
- Bypass factor: 0.167
- Condensate: 120 lb/hr (14.4 gal/hr)

</div>

## Humidification Processes

Humidification adds moisture to air. Two methods exist: steam injection and water evaporation.

### Steam Humidification

Steam injection adds both moisture and heat. The process line moves nearly vertically upward and slightly to the right.

**Mass Balance:**

$$\dot{m}_{steam} = \dot{m}_a (W_2 - W_1)$$

In terms of CFM:

$$\dot{m}_{steam} = 4.5 \times CFM \times (W_2 - W_1) \text{ lb/hr}$$

**Energy Balance:**

Temperature rise from steam heat:

$$\Delta T = \frac{(W_2 - W_1) \times h_{steam}}{c_p + W_{avg} c_{pw}}$$

For low-pressure steam ($h_{steam} \approx 1150$ Btu/lb):

$$\Delta T \approx \frac{(W_2 - W_1) \times 1150}{0.24}$$

Typically 2-5°F temperature rise per 0.001 lb/lb humidity increase.

### Evaporative Humidification

Water spray or wetted media humidification follows an adiabatic process (constant enthalpy). The process line follows a constant wet bulb temperature line.

**Process Characteristics:**
- Enthalpy constant: $h_1 = h_2$
- Temperature decreases
- Humidity ratio increases
- Follows constant WBT line

**Evaporative Cooling Effectiveness:**

$$\epsilon = \frac{T_1 - T_2}{T_1 - T_{wb,1}}$$

Where ε ranges from 0.60 to 0.95 depending on design.

<div class="worked-example">

### Worked Example 4: Spray Humidifier Design

**Given:**
- Airflow: 2,000 CFM
- Inlet: 70°F, 20% RH
- Desired outlet: 70°F, 50% RH

**Find:** Steam requirement (lb/hr)

**Solution:**

**Step 1: Find inlet humidity ratio**

At 70°F: $p_{ws} = 0.3631$ psia

$$W_1 = 0.622 \times \frac{0.20 \times 0.3631}{14.696 - 0.20 \times 0.3631}$$

$$W_1 = 0.622 \times \frac{0.0726}{14.623} = 0.00309 \text{ lb/lb}$$

**Step 2: Find outlet humidity ratio**

$$W_2 = 0.622 \times \frac{0.50 \times 0.3631}{14.696 - 0.50 \times 0.3631}$$

$$W_2 = 0.622 \times \frac{0.1816}{14.515} = 0.00778 \text{ lb/lb}$$

**Step 3: Calculate steam requirement**

$$\dot{m}_{steam} = 4.5 \times 2000 \times (0.00778 - 0.00309)$$

$$\dot{m}_{steam} = 9000 \times 0.00469 = 42.2 \text{ lb/hr}$$

**Step 4: Estimate temperature rise**

$$\Delta T \approx \frac{0.00469 \times 1150}{0.24} = 22.5°F$$

Actual outlet temperature ≈ 70 + 22.5 = 92.5°F

**Note:** To maintain 70°F, cooling must be applied after humidification, or use adiabatic humidification.

**Answer:** 42.2 lb/hr steam required; results in temperature rise to ~92.5°F

</div>

## Air Mixing Process

Mixing two airstreams creates a final state point lying on a straight line between the two initial state points.

### Governing Equations

**Mass Balance:**

$$\dot{m}_3 = \dot{m}_1 + \dot{m}_2$$

**Energy Balance:**

$$\dot{m}_3 h_3 = \dot{m}_1 h_1 + \dot{m}_2 h_2$$

**Moisture Balance:**

$$\dot{m}_3 W_3 = \dot{m}_1 W_1 + \dot{m}_2 W_2$$

**Final State Properties:**

$$h_3 = \frac{\dot{m}_1 h_1 + \dot{m}_2 h_2}{\dot{m}_1 + \dot{m}_2}$$

$$W_3 = \frac{\dot{m}_1 W_1 + \dot{m}_2 W_2}{\dot{m}_1 + \dot{m}_2}$$

**Volumetric Basis (approximation):**

For small temperature differences (< 30°F), mass flow ratios approximately equal volume ratios:

$$\frac{\dot{m}_1}{\dot{m}_2} \approx \frac{CFM_1}{CFM_2}$$

**Graphical Method:**

Mixed state point divides the line between state 1 and state 2 proportionally to mass flow rates:

$$\frac{distance(1-3)}{distance(1-2)} = \frac{\dot{m}_2}{\dot{m}_1 + \dot{m}_2}$$

<div class="worked-example">

### Worked Example 5: Return Air and Outside Air Mixing

**Given:**
- Return air: 8,000 CFM, 75°F DB, 50% RH
- Outside air: 2,000 CFM, 95°F DB, 70% RH
- Atmospheric pressure: 14.696 psia

**Find:** Mixed air temperature, humidity ratio, and enthalpy

**Solution:**

**Step 1: Determine return air properties**

At 75°F: $p_{ws} = 0.4298$ psia

$$W_{RA} = 0.622 \times \frac{0.50 \times 0.4298}{14.696 - 0.50 \times 0.4298}$$

$$W_{RA} = 0.622 \times \frac{0.2149}{14.481} = 0.00923 \text{ lb/lb}$$

$$h_{RA} = 0.24(75) + 0.00923(1061 + 0.444 \times 75)$$

$$h_{RA} = 18.0 + 0.00923(1094) = 18.0 + 10.1 = 28.1 \text{ Btu/lb}$$

**Step 2: Determine outside air properties**

At 95°F: $p_{ws} = 0.8153$ psia

$$W_{OA} = 0.622 \times \frac{0.70 \times 0.8153}{14.696 - 0.70 \times 0.8153}$$

$$W_{OA} = 0.622 \times \frac{0.5707}{14.125} = 0.02513 \text{ lb/lb}$$

$$h_{OA} = 0.24(95) + 0.02513(1061 + 0.444 \times 95)$$

$$h_{OA} = 22.8 + 0.02513(1103) = 22.8 + 27.7 = 50.5 \text{ Btu/lb}$$

**Step 3: Calculate mass flow rates**

Assume standard density for approximation:

$$\dot{m}_{RA} = 8000 \times 60 \times 0.075 = 36,000 \text{ lb/hr}$$

$$\dot{m}_{OA} = 2000 \times 60 \times 0.075 = 9,000 \text{ lb/hr}$$

Total: $\dot{m}_{MA} = 45,000$ lb/hr

**Step 4: Calculate mixed air properties**

Temperature (direct mixing):

$$T_{MA} = \frac{8000 \times 75 + 2000 \times 95}{10,000} = \frac{600,000 + 190,000}{10,000} = 79°F$$

Humidity ratio:

$$W_{MA} = \frac{36,000 \times 0.00923 + 9,000 \times 0.02513}{45,000}$$

$$W_{MA} = \frac{332.3 + 226.2}{45,000} = 0.01241 \text{ lb/lb}$$

Enthalpy:

$$h_{MA} = \frac{36,000 \times 28.1 + 9,000 \times 50.5}{45,000}$$

$$h_{MA} = \frac{1,011,600 + 454,500}{45,000} = 32.6 \text{ Btu/lb}$$

**Verification:**

Calculate enthalpy from T and W:

$$h = 0.24(79) + 0.01241(1061 + 0.444 \times 79)$$

$$h = 19.0 + 0.01241(1096) = 19.0 + 13.6 = 32.6 \text{ Btu/lb}$$ ✓

**Answers:**
- Mixed air: 79°F DB, W = 0.01241 lb/lb (87 grains/lb)
- Mixed air enthalpy: 32.6 Btu/lb
- From chart: RH ≈ 56%

</div>

## Combined Processes: Air Handler Analysis

Real HVAC systems perform multiple processes in sequence.

**Typical Air Handler Sequence:**
1. Mixing (return + outdoor air)
2. Filtering (minimal psychrometric change)
3. Cooling/dehumidification
4. Reheat (if required)
5. Supply fan (small temperature rise from fan heat)

**Fan Heat Addition:**

$$\Delta T_{fan} = \frac{BHP \times 2545}{1.08 \times CFM \times \eta_{motor}}$$

Where:
- BHP = brake horsepower
- η = motor efficiency
- Typical ΔT = 1-3°F

## Summary Table of Process Characteristics

| Process | ΔT | ΔW | Δh | Chart Path | Application |
|---------|----|----|----|-----------| ------------|
| Sensible Heating | + | 0 | + | Horizontal right | Heating coils |
| Sensible Cooling | - | 0 | - | Horizontal left | Precooling |
| Cooling + Dehumid | - | - | - | Toward saturation | Cooling coils |
| Steam Humidification | + | + | + | Nearly vertical up | Winter humidification |
| Evaporative Cooling | - | + | 0 | Constant WBT | Desert cooling |
| Mixing | varies | varies | varies | Straight line | Economizers |

## Conclusion

Mastery of psychrometric processes enables proper equipment selection and system design. Each process follows thermodynamic principles visible on the psychrometric chart. Combined processes require sequential analysis, with outlet conditions from one process becoming inlet conditions for the next.

Engineers must understand sensible heat ratios, bypass factors, and apparatus dew points for accurate cooling coil selection. Mixing processes determine economizer operation and outdoor air introduction strategies.

---

**Related Technical Guides:**
- [Psychrometric Fundamentals](/technical-guides/psychrometric-fundamentals/)
- [Cooling Load Calculations](/technical-guides/cooling-load-calculations/)
- [Heating Load Calculations](/technical-guides/heating-load-calculations/)

**References:**
- ASHRAE Handbook of Fundamentals, Chapter 1: Psychrometrics
- ASHRAE HVAC Systems and Equipment Handbook, Chapter 4: Air Handling and Distribution
- Stoecker, W.F. and Jones, J.W. Refrigeration and Air Conditioning
