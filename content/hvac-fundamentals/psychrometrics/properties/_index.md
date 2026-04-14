---
title: "Psychrometric Properties"
aliases: ["Psychrometric Properties"]
description: "Comprehensive treatment of psychrometric properties including dry bulb, wet bulb, dew point temperatures, humidity ratio, enthalpy, and vapor pressure with engineering equations and interrelationships"
weight: 1
---

Psychrometric properties define the thermodynamic state of moist air, which is a binary mixture of dry air and water vapor. Understanding these properties and their interrelationships is fundamental to HVAC system design, load calculations, and equipment selection. Each property can be measured or calculated, and knowing any two independent properties allows determination of all others using psychrometric relationships.

## Dry Bulb Temperature

Dry bulb temperature (Tdb or t) is the temperature of air measured by a standard thermometer freely exposed to the air but shielded from radiation and moisture. It represents the true thermodynamic temperature of the air-water vapor mixture.

**Definition and Measurement:**

- Measured with temperature sensors (thermocouples, RTDs, thermistors)
- Unaffected by moisture content in the air
- Primary independent variable in psychrometric analysis
- Typically expressed in °F or °C

**Engineering Significance:**

Dry bulb temperature directly affects:
- Sensible heat transfer calculations: Q = ṁ × cp × ΔT
- Air density and buoyancy effects
- Occupant thermal comfort (operative temperature)
- Equipment capacity and efficiency

**Typical Design Values:**

| Application | Winter Design | Summer Design |
|-------------|---------------|---------------|
| Comfort Cooling | 70-72°F | 75-78°F |
| Comfort Heating | 70-72°F | 68-70°F |
| Data Centers | - | 64.4-80.6°F (ASHRAE A1) |
| Hospitals (Patient Rooms) | 70-75°F | 70-75°F |
| Laboratories | 68-78°F | 68-78°F |

**ASHRAE Reference:** ASHRAE Handbook—Fundamentals, Chapter 1: Psychrometrics

## Wet Bulb Temperature

Wet bulb temperature (Twb or t*) is the temperature indicated by a thermometer whose bulb is covered with a water-saturated wick and exposed to moving air. It represents the lowest temperature achievable through evaporative cooling at constant pressure.

**Physical Principle:**

When air flows over a wetted surface, water evaporates and absorbs latent heat from the air stream, cooling the wetted bulb. At steady state, the heat transferred to the water by convection equals the heat removed by evaporation:

hc × (Tdb - Twb) = hfg × ṁevap

Where:
- hc = convective heat transfer coefficient, Btu/(h·ft²·°F)
- hfg = latent heat of vaporization, Btu/lbm
- ṁevap = evaporation rate, lbm/(h·ft²)

**Measurement Requirements:**

- Air velocity: 900-1000 ft/min (4.5-5 m/s) for sling psychrometer
- Minimum velocity: 300 ft/min to ensure proper evaporation
- Wick must be clean, wetted with distilled water
- Thermometer shield required to prevent radiation effects

**Applications:**

- Cooling tower performance evaluation
- Evaporative cooling system design
- Humidity determination (with dry bulb)
- WBGT (Wet Bulb Globe Temperature) heat stress calculations

**Relationship to Enthalpy:**

At sea level (29.921 in. Hg), a simplified relationship exists:

h ≈ 0.24 × Tdb + W × (1061 + 0.444 × Tdb)

For saturated air (at wet bulb):
h ≈ 1061 + 0.444 × Twb

This approximation allows enthalpy estimation from wet bulb temperature alone.

## Thermodynamic Wet Bulb Temperature

Thermodynamic wet bulb temperature (T*) is the temperature at which water, by evaporating into air, can bring the air to saturation adiabatically at the same temperature while the pressure remains constant. This is a theoretical property distinct from the psychrometric wet bulb.

**Key Distinction:**

The thermodynamic wet bulb differs from psychrometric wet bulb due to:
- Different heat and mass transfer mechanisms
- Psychrometric wet bulb affected by Lewis Number (Le = α/D)
- For air-water vapor at typical HVAC conditions, the difference is negligible (< 0.5°F)

**Adiabatic Saturation Process:**

Starting from state point (T₁, W₁), air is saturated by contact with water at T* in an adiabatic chamber:

h₁ + (Ws* - W₁) × hw* = hs*

Where:
- h₁ = initial enthalpy, Btu/lbm-da
- Ws* = humidity ratio at saturation at T*, lbm/lbm-da
- hw* = enthalpy of water at T*, Btu/lbm
- hs* = enthalpy at saturation at T*, Btu/lbm-da

**Engineering Use:**

- Rigorous psychrometric calculations
- Validation of measured wet bulb values
- Evaporative cooling process analysis
- Lines of constant thermodynamic wet bulb on psychrometric chart approximate constant enthalpy lines

## Dew Point Temperature

Dew point temperature (Tdp or td) is the temperature at which air becomes saturated when cooled at constant pressure and constant humidity ratio. At the dew point, water vapor begins to condense.

**Fundamental Equation:**

At dew point, partial pressure of water vapor equals saturation pressure:

pw = pws(Tdp)

The dew point can be calculated from partial pressure using the inverse of the saturation pressure equation.

**Approximation for Dew Point (ASHRAE):**

For pw in range 0.0005-0.5 psia:

Tdp = C₁₄ + C₁₅ × α + C₁₆ × α² + C₁₇ × α³ + C₁₈ × (pw)^0.1984

Where α = ln(pw) and coefficients C₁₄-C₁₈ are provided in ASHRAE Handbook.

**Engineering Applications:**

1. **Condensation Risk Assessment:**
   - Surface temperature below dew point causes condensation
   - Critical for envelope design, ductwork, and piping

2. **Minimum Supply Air Temperature:**
   - Supply air dew point must be below space dew point for dehumidification
   - ADP (apparatus dew point) determines coil performance

3. **Outdoor Air Economizer Control:**
   - Dew point economizer more effective than dry bulb or enthalpy control
   - Prevents introducing high-moisture outdoor air

4. **Compressed Air Systems:**
   - Pressure dew point specification for air quality
   - Typical: -40°F PDP for instrument air

**Dew Point Depression:**

ΔTdp = Tdb - Tdp

Depression indicates moisture content:
- Small depression (< 5°F): High relative humidity
- Large depression (> 30°F): Low relative humidity, dry conditions

## Relative Humidity

Relative humidity (RH or φ) is the ratio of the actual partial pressure of water vapor in air to the saturation pressure at the same dry bulb temperature, expressed as a percentage.

**Definition:**

φ = (pw / pws) × 100%

Or in terms of humidity ratio:

φ = [W / Ws] × [(p - pws) / (p - pw)] × 100%

For practical purposes at atmospheric pressure:

φ ≈ (W / Ws) × 100%

**Relationship to Mole Fraction:**

φ = (xw / xws) × 100%

Where xw is mole fraction of water vapor in the mixture.

**Comfort and Health Implications:**

| RH Range | Effects | Recommendation |
|----------|---------|----------------|
| < 20% | Dry skin, static electricity, respiratory irritation | Avoid for occupied spaces |
| 20-30% | Acceptable for some applications, preserves materials | Museums, archives |
| 30-50% | Optimal for general comfort and health | ASHRAE Standard 55 comfort zone |
| 50-60% | Upper comfort limit, increased microbial growth risk | Maximum for most occupied spaces |
| > 60% | Mold growth, condensation risk, discomfort | Unacceptable for conditioned spaces |

**Design Considerations:**

1. **Winter Humidification:**
   - Maximum indoor RH limited by condensation on coldest surfaces
   - Interior storm windows allow higher RH without condensation
   - ASHRAE 55: 30% RH minimum recommended for comfort

2. **Summer Dehumidification:**
   - Space RH control typically 50-55% maximum
   - Lower RH (40-50%) preferred for mold prevention
   - Dehumidification requires cooling below space dew point

3. **Precision Control Applications:**
   - Data centers: 20-80% RH (ASHRAE TC 9.9)
   - Hospitals (surgical suites): 20-60% RH
   - Laboratories: application-specific, often 30-60% RH

**Control Limitations:**

Relative humidity is temperature-dependent. A constant moisture content (W) results in varying RH as temperature changes:

dφ/dT < 0 (at constant W)

This complicates control strategies; humidity ratio or dew point control is more stable.

## Humidity Ratio

Humidity ratio (W), also called mixing ratio or specific humidity, is the mass of water vapor per unit mass of dry air in the mixture, expressed in lbm-water/lbm-dry air or grains/lbm (7000 grains = 1 lbm).

**Fundamental Equation:**

W = 0.621945 × (pw / (p - pw))

Where:
- pw = partial pressure of water vapor, psia
- p = total barometric pressure, psia
- 0.621945 = ratio of molecular weights (Mw/Ma = 18.015/28.965)

**At Saturation:**

Ws = 0.621945 × (pws / (p - pws))

Where pws is saturation pressure at the given temperature.

**Relationship to Relative Humidity:**

W = 0.621945 × (φ × pws / (p - φ × pws))

**Typical Values:**

| Condition | Tdb | Tdp | W (lbm/lbm) | W (gr/lbm) |
|-----------|-----|-----|-------------|------------|
| Cold/Dry | 32°F | 10°F | 0.0015 | 10.5 |
| Moderate | 70°F | 50°F | 0.0076 | 53.2 |
| Hot/Humid | 95°F | 75°F | 0.0159 | 111.3 |
| Saturated 75°F | 75°F | 75°F | 0.0193 | 135.1 |

**Engineering Applications:**

1. **Latent Load Calculations:**

Qlatent = ṁa × hfg × ΔW = ṁa × 1076 × ΔW (approx.)

More precisely:
Qlatent = 60 × ρ × CFM × 1076 × ΔW

Where ρ = air density, lbm/ft³

2. **Ventilation and Infiltration:**

Moisture gain from outdoor air:
ṁw = ṁa × (Wo - Wi)

Where Wo = outdoor humidity ratio, Wi = indoor humidity ratio

3. **Space Moisture Balance:**

For steady-state:
ṁsupply × Wsupply + ṁinfiltration × Woutdoor + Ġinternal = ṁreturn × Wspace

4. **Dehumidification Requirement:**

SHR = Qsensible / Qtotal = Qsensible / (Qsensible + Qlatent)

Required apparatus dew point (ADP) is determined by:
WADP = Wspace - (Qlatent / (1076 × ṁa))

## Degree of Saturation

Degree of saturation (μ) is the ratio of the actual humidity ratio to the humidity ratio at saturation at the same temperature and pressure.

**Definition:**

μ = W / Ws

Or in terms of partial pressures:

μ = [(p - pws) / (p - pw)] × (pw / pws)

**Relationship to Relative Humidity:**

μ ≈ φ × [(p - pws) / (p - pw)]

At atmospheric pressure and moderate conditions, μ ≈ φ, but they diverge at high humidity or reduced pressure.

**Engineering Use:**

- Quantifies proximity to saturation
- Useful in fog formation prediction
- Relevant for high-altitude applications where pressure effects are significant
- Less commonly used than RH in practice but more thermodynamically rigorous

**Typical Values:**

For standard atmospheric conditions (14.696 psia):
- μ = 0.90 indicates air is 90% of the way to saturation by mass
- At 50% RH and 70°F, μ ≈ 0.499 (nearly identical to φ)
- Difference becomes significant at high RH: at 95% RH, μ ≈ 0.93

## Specific Enthalpy of Moist Air

Specific enthalpy (h) is the total heat content of moist air per unit mass of dry air, accounting for both sensible and latent components. Expressed in Btu/lbm-da or kJ/kg-da.

**Fundamental Equation:**

h = ha + W × hw

Where:
- ha = specific enthalpy of dry air, Btu/lbm
- hw = specific enthalpy of water vapor, Btu/lbm
- W = humidity ratio, lbm-water/lbm-da

**Practical Calculation (IP Units):**

h = 0.240 × Tdb + W × (1061 + 0.444 × Tdb)

Where:
- 0.240 = specific heat of dry air, Btu/(lbm·°F)
- 1061 = latent heat at 0°F datum, Btu/lbm
- 0.444 = specific heat of water vapor, Btu/(lbm·°F)
- Tdb in °F, resulting h in Btu/lbm-da

**SI Units:**

h = 1.006 × Tdb + W × (2501 + 1.86 × Tdb)

Where:
- 1.006 = specific heat of dry air, kJ/(kg·K)
- 2501 = latent heat at 0°C datum, kJ/kg
- 1.86 = specific heat of water vapor, kJ/(kg·K)
- Tdb in °C, resulting h in kJ/kg-da

**Components:**

1. **Sensible Component:**
   hs = 0.240 × Tdb (dry air sensible heat)

2. **Latent Component:**
   hl = W × 1061 (latent heat at datum)

3. **Vapor Sensible Component:**
   hw,sensible = W × 0.444 × Tdb (water vapor sensible heat)

**Engineering Applications:**

1. **Cooling/Heating Load:**

Q = ṁa × Δh = 60 × ρ × CFM × Δh

For standard air (0.075 lbm/ft³):
Q = 4.5 × CFM × Δh

2. **Psychrometric Processes:**

All HVAC processes follow enthalpy changes:
- Sensible heating: Δh = 0.240 × ΔT
- Sensible cooling: Δh = 0.240 × ΔT
- Humidification (steam): Δh = Δhs + W × hsteam
- Dehumidification: Δh = 0.240 × ΔT + 1061 × ΔW

3. **Economizer Operation:**

Compare outdoor and return air enthalpies:
- If houtdoor < hreturn: economizer mode saves energy
- Enthalpy-based economizer more accurate than temperature-only

4. **Evaporative Cooling:**

Adiabatic process: h₁ ≈ h₂
Temperature decrease offset by moisture increase
Efficiency = (Tdb1 - Tdb2) / (Tdb1 - Twb1) × 100%

**Enthalpy Wheel Performance:**

Effectiveness = (hreturn - hsupply) / (hreturn - houtdoor)

Typical effectiveness: 65-85% depending on wheel design and airflow.

## Specific Volume of Moist Air

Specific volume (v) is the volume of moist air per unit mass of dry air, expressed in ft³/lbm-da or m³/kg-da. Its reciprocal is density (ρ = 1/v).

**Ideal Gas Equation:**

v = (Ra × T) / (p - pw)

Where:
- Ra = specific gas constant for dry air = 53.352 ft·lbf/(lbm·°R) or 287.042 J/(kg·K)
- T = absolute temperature, °R or K
- p = total pressure, lbf/ft² or Pa
- pw = partial pressure of water vapor, lbf/ft² or Pa

**Practical Calculation (IP Units):**

v = (0.754 × T) / (p - pw)

Or more conveniently:

v = 0.754 × (Tdb + 460) × (1 + 1.6078 × W) / p

Where:
- Tdb in °F
- p in psia (standard = 14.696 psia)
- W in lbm/lbm
- Result in ft³/lbm-da

**Standard Conditions:**

At 70°F, 14.696 psia, 50% RH:
- W ≈ 0.0078 lbm/lbm
- v ≈ 13.33 ft³/lbm-da
- ρ ≈ 0.075 lbm/ft³

**Effect of Humidity:**

Moist air is less dense than dry air at the same pressure and temperature because water vapor (MW = 18) is lighter than dry air (MW = 29). Each 0.001 increase in W increases specific volume by approximately 0.02 ft³/lbm-da.

**Engineering Applications:**

1. **Mass Flow Rate from Volumetric Flow:**

ṁa = CFM × 60 × ρ = CFM × 60 / v

At standard conditions:
ṁa ≈ CFM × 60 × 0.075 = 4.5 × CFM lbm/min

2. **Altitude Correction:**

Atmospheric pressure decreases with elevation:
p(z) = 14.696 × exp(-z / 29,000)

Where z = elevation in feet (approximate)

At 5000 ft: p ≈ 12.23 psia
Specific volume increases ~20%, reducing air density and capacity

3. **Duct Sizing:**

A = ṁa × v / (60 × V)

Where:
- A = duct area, ft²
- ṁa = mass flow, lbm/min
- V = velocity, ft/min
- v = specific volume, ft³/lbm-da

4. **Fan Performance:**

Fans move volumetric flow (CFM), but HVAC processes depend on mass flow:

Actual Capacity = Rated Capacity × (ρactual / ρrated)

Temperature and humidity corrections are essential for accurate system performance.

## Partial Pressure of Water Vapor

Partial pressure of water vapor (pw) is the pressure exerted by water vapor in the air-vapor mixture. It represents the independent contribution of water vapor to total atmospheric pressure.

**Dalton's Law:**

p = pa + pw

Where:
- p = total barometric pressure
- pa = partial pressure of dry air
- pw = partial pressure of water vapor

**From Humidity Ratio:**

pw = p × W / (0.621945 + W)

For typical conditions where W << 1:

pw ≈ p × W / 0.621945

**From Relative Humidity:**

pw = φ × pws

Where pws is saturation pressure at dry bulb temperature.

**Typical Values:**

| Condition | Tdb | RH | pws | pw |
|-----------|-----|----|----|-----|
| Cold/Dry | 32°F | 30% | 0.0887 psia | 0.0266 psia |
| Comfort | 70°F | 50% | 0.3631 psia | 0.1816 psia |
| Hot/Humid | 95°F | 70% | 0.8153 psia | 0.5707 psia |

**Engineering Significance:**

1. **Condensation Analysis:**
   - When surface temperature Ts < Tdp, condensation occurs
   - Surface vapor pressure equals saturation pressure at Ts
   - Vapor pressure gradient drives moisture migration

2. **Vapor Pressure Deficit (VPD):**

VPD = pws(Tdb) - pw

VPD indicates evaporation potential:
- High VPD: dry air, high evaporation rate
- Low VPD: humid air, low evaporation rate
- Critical for agricultural applications, greenhouses

3. **Permeance and Vapor Retarders:**

Water vapor transmission:
ṁv = M × A × Δpv

Where:
- M = permeance, perms (grains/(h·ft²·in. Hg))
- A = area, ft²
- Δpv = vapor pressure difference, in. Hg

Vapor retarder requirement: M < 1.0 perm (Class II) or M < 0.1 perm (Class I)

## Saturation Pressure

Saturation pressure (pws or ps) is the pressure at which water vapor and liquid water exist in equilibrium at a given temperature. It defines the maximum partial pressure of water vapor possible at that temperature.

**Hyland-Wexler Equation (ASHRAE Standard):**

ln(pws) = C₁/T + C₂ + C₃×T + C₄×T² + C₅×T³ + C₆×T⁴ + C₇×ln(T)

Where T is absolute temperature in Kelvin, and C₁-C₇ are empirical constants different for ice (-148 to 32°F) and water (32 to 392°F).

**Antoine Equation (Simplified):**

log₁₀(pws) = A - B / (C + T)

Where A, B, C are substance-specific constants.

For water (32-212°F):
- A = 7.96681
- B = 1668.21
- C = 228.0
- T in °C, pws in mm Hg

**Magnus-Tetens Formula (Approximation):**

pws(T) = 6.112 × exp(17.67 × T / (T + 243.5))

Where:
- T in °C
- Result in millibar (mb)
- Valid range: -40 to 50°C
- Accuracy: ±0.5% within range

**Temperature Dependence:**

Saturation pressure increases exponentially with temperature following the Clausius-Clapeyron relation:

dpws/dT = (hfg × pws) / (Rv × T²)

Where:
- hfg = latent heat of vaporization
- Rv = gas constant for water vapor
- T = absolute temperature

**Engineering Data Table:**

| Temperature | pws (psia) | Temperature | pws (psia) |
|-------------|-----------|-------------|-----------|
| 0°F | 0.0185 | 70°F | 0.3631 |
| 10°F | 0.0267 | 75°F | 0.4298 |
| 20°F | 0.0378 | 80°F | 0.5069 |
| 32°F | 0.0887 | 85°F | 0.5959 |
| 40°F | 0.1217 | 90°F | 0.6982 |
| 50°F | 0.1780 | 95°F | 0.8153 |
| 60°F | 0.2563 | 100°F | 0.9487 |

**Applications:**

1. **Humidity Calculations:**
   - All humidity properties derive from saturation pressure
   - Accurate pws calculation essential for precise psychrometrics

2. **Coil Performance:**
   - Apparatus dew point (ADP) determined by pws at coil surface temperature
   - Bypass factor depends on ratio of leaving to saturation conditions

3. **Cooling Tower Design:**
   - Evaporation rate proportional to (pws - pw)
   - Approach = Tcold water - Twb relates to saturation conditions

4. **Frost Formation:**
   - Below 32°F, saturation pressure over ice < saturation pressure over water
   - Supersaturation between ice and water curves enables frost

## Interrelationships Between Properties

Psychrometric properties are interdependent. Two independent properties define the complete state, allowing calculation of all others. Common property pairs used in practice:

**Primary Measurement Pairs:**

1. **Dry Bulb + Wet Bulb (Tdb, Twb):**
   - Traditional psychrometer measurement
   - Calculate humidity ratio from energy balance
   - Determine all other properties

2. **Dry Bulb + Relative Humidity (Tdb, φ):**
   - Common sensor combination
   - Calculate pw = φ × pws(Tdb)
   - Derive W from pw

3. **Dry Bulb + Dew Point (Tdb, Tdp):**
   - Most stable sensor combination
   - Calculate pw = pws(Tdp)
   - Independent of temperature sensor errors

4. **Dry Bulb + Humidity Ratio (Tdb, W):**
   - Direct calculation of enthalpy and other properties
   - Used in load calculation procedures

**Calculation Sequence Example (Tdb, Twb given):**

1. Determine pws(Tdb) and pws(Twb) from saturation equations
2. Approximate: W ≈ [(2830 - 1.44×Twb)×Ws(Twb) - (Tdb - Twb)] / [2830 + 1.44×Tdb]
3. Calculate pw = p × W / (0.621945 + W)
4. Calculate φ = pw / pws(Tdb)
5. Solve for Tdp where pws(Tdp) = pw
6. Calculate h = 0.240×Tdb + W×(1061 + 0.444×Tdb)
7. Calculate v = 0.754×(Tdb+460)×(1 + 1.6078×W) / p

**Graphical Representation:**

The psychrometric chart displays these relationships:
- Horizontal axis: dry bulb temperature
- Vertical axis: humidity ratio
- Curves: constant relative humidity, wet bulb, enthalpy, specific volume
- Any point represents complete state
- Process lines show HVAC operations

**Consistency Checks:**

1. Tdp ≤ Twb ≤ Tdb (always true)
2. W ≤ Ws(Tdb) (air cannot exceed saturation at its temperature)
3. φ ≤ 100% (by definition)
4. At saturation: Tdb = Twb = Tdp, φ = 100%, W = Ws

## ASHRAE Standards and References

**ASHRAE Handbook—Fundamentals (Chapter 1: Psychrometrics):**

- Definitive source for psychrometric equations and properties
- Hyland-Wexler formulations for saturation pressure
- Perfect gas relationships for moist air
- Psychrometric chart construction methodology
- Numerical tables for wide range of conditions

**ASHRAE Standard 55: Thermal Environmental Conditions for Human Occupancy:**

- Comfort zone: 67-82°F operative temperature
- Humidity limits: 30-60% RH recommended (not mandated)
- Elevated air speed can extend comfort zone
- PMV/PPD method for thermal comfort prediction

**ASHRAE Standard 62.1: Ventilation for Acceptable Indoor Air Quality:**

- Ventilation rates affect moisture balance
- Indoor humidity not directly regulated
- Moisture control implicit in ventilation effectiveness

**ASHRAE Standard 169: Climatic Data for Building Design Standards:**

- Design day dry bulb and wet bulb temperatures
- Humidity ratio data for load calculations
- 0.4%, 1.0%, 2.0% occurrence levels
- Basis for equipment sizing decisions

**ASHRAE Guideline 0: The Commissioning Process:**

- Verification of psychrometric controls
- Humidity sensor calibration requirements
- Testing at design conditions

**ASHRAE RP-1485: Thermodynamic Properties of Real Moist Air:**

- Refinements to ideal gas assumptions
- Enhancement factors for saturation pressure
- Improved accuracy at extreme conditions

## Design Considerations

**Sensor Selection and Placement:**

1. **Temperature Sensors:**
   - Accuracy: ±0.5°F for most HVAC applications
   - ±0.2°F for critical environments (laboratories, data centers)
   - Shield from radiation, ensure adequate air movement
   - RTDs preferred over thermocouples for stability

2. **Humidity Sensors:**
   - Capacitive RH sensors: ±2% RH typical, ±3-5% at extremes
   - Chilled mirror dew point sensors: ±0.2°F, most accurate
   - Resistive sensors: lower cost, less stable, require calibration
   - Placement: representative location, away from moisture sources

3. **Calibration Requirements:**
   - Temperature: annually or biannually
   - Humidity: quarterly for critical applications, annually for general
   - Drift over time necessitates regular verification
   - Use certified calibration standards traceable to NIST

**Altitude and Pressure Corrections:**

Standard atmospheric pressure = 14.696 psia (sea level)

At elevation z (feet):
p(z) ≈ 14.696 × exp(-z / 29,000)

Corrections required:
- Humidity ratio calculations (direct pressure dependence)
- Specific volume and density (inversely proportional to pressure)
- Equipment capacity ratings (mass flow affected)
- Boiling point of water (affects humidification)

Example: Denver, CO (5,280 ft)
- p ≈ 12.2 psia (17% reduction)
- Air density reduced ~17%
- Cooling capacity per CFM reduced proportionally
- Adjust equipment selections accordingly

**Control Strategies:**

1. **Relative Humidity Control:**
   - Simple, intuitive for occupants
   - Unstable with temperature swings
   - Seasonal adjustment needed
   - Common in residential, light commercial

2. **Dew Point Control:**
   - Most stable, temperature-independent moisture control
   - Ideal for precision applications
   - Requires dew point sensors or calculation
   - Preferred for data centers, laboratories

3. **Enthalpy-Based Control:**
   - Optimal for economizer operation
   - Accounts for total cooling load
   - More complex, requires both T and RH/W sensors
   - Energy code requirements (ASHRAE 90.1)

**Load Calculation Best Practices:**

1. Use design day data from ASHRAE Handbook or Standard 169
2. Calculate both sensible and latent loads separately
3. Account for ventilation and infiltration moisture gains
4. Size dehumidification capacity for peak latent load
5. Verify ADP can achieve required space humidity
6. Consider part-load conditions and humidity control

**Common Design Errors:**

1. Neglecting latent load in humid climates
2. Oversizing equipment (poor humidity control at part load)
3. Inadequate outdoor air humidity consideration
4. Failure to account for altitude/pressure effects
5. Using relative humidity when dew point is more appropriate
6. Ignoring sensor accuracy and placement effects
7. Not verifying psychrometric consistency of inputs

**Critical Applications:**

High-precision psychrometric control required for:
- Hospitals (surgical suites, isolation rooms)
- Museums and archives (artifact preservation)
- Laboratories (testing repeatability)
- Data centers (equipment reliability)
- Pharmaceutical manufacturing (process control)
- Food processing and storage (quality, safety)

Each requires application-specific design criteria, control strategies, and equipment selection based on rigorous psychrometric analysis.
