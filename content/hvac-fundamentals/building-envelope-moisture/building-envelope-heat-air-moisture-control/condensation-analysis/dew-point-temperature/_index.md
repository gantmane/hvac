---
title: "Dew Point Temperature"
description: "Comprehensive analysis of dew point temperature in building envelope condensation analysis, including psychrometric relationships, calculation methods, saturation physics, and application to moisture control strategies in HVAC systems."
weight: 1
---

## Fundamental Physics

Dew point temperature represents the temperature at which air becomes saturated with water vapor at constant pressure and moisture content. This saturation temperature is the critical threshold below which condensation occurs on surfaces or within building assemblies.

### Thermodynamic Definition

The dew point temperature (T_dp) is defined as the temperature at which the partial pressure of water vapor in the air equals the saturation pressure:

**Equilibrium Condition:**
```
P_v = P_sat(T_dp)
```

Where:
- P_v = Actual water vapor partial pressure (psia or Pa)
- P_sat = Saturation pressure at dew point temperature (psia or Pa)
- T_dp = Dew point temperature (°F or °C)

### Physical Significance

At the dew point temperature, the air-vapor mixture reaches 100% relative humidity. Any further cooling results in condensation of water vapor into liquid phase. This phase change releases latent heat (approximately 1060 BTU/lb at standard conditions), which can influence local temperature profiles in building assemblies.

**Key Principle:** Dew point temperature depends only on moisture content and pressure, not on dry-bulb temperature. Two air samples at different temperatures but identical humidity ratios have the same dew point.

## Psychrometric Relationships

### Humidity Ratio and Dew Point

The relationship between humidity ratio (W) and dew point temperature establishes the fundamental link between moisture content and condensation potential:

**For Standard Atmospheric Pressure (14.696 psia):**
```
W = 0.621945 × P_sat(T_dp) / (P_atm - P_sat(T_dp))
```

Where:
- W = Humidity ratio (lb_water/lb_dry air or kg_water/kg_dry air)
- P_atm = Atmospheric pressure (psia or Pa)
- P_sat(T_dp) = Saturation pressure at dew point (psia or Pa)

### Relative Humidity Correlation

Relative humidity (RH) relates the actual vapor pressure to the saturation pressure at the dry-bulb temperature:

```
RH = P_v / P_sat(T_db) = P_sat(T_dp) / P_sat(T_db)
```

Where:
- RH = Relative humidity (decimal or %)
- T_db = Dry-bulb temperature (°F or °C)
- T_dp = Dew point temperature (°F or °C)

**Critical Observation:** As dry-bulb temperature decreases toward dew point, relative humidity increases toward 100%, even though absolute moisture content (W) remains constant.

## Saturation Pressure Equations

### Magnus-Tetens Approximation

For temperatures between -40°C and 50°C (-40°F to 122°F), the Magnus-Tetens equation provides accurate saturation pressure values:

**Over Water (SI Units):**
```
P_sat = 610.78 × exp[(17.2694 × T) / (T + 238.3)]
```

**Over Water (IP Units):**
```
P_sat = 0.08854 × exp[(17.2694 × T_C) / (T_C + 238.3)]
```

Where:
- P_sat = Saturation pressure (Pa for SI, psia for IP)
- T = Temperature (°C)
- T_C = Temperature converted to °C from °F: (T_F - 32) / 1.8

### ASHRAE Correlation

ASHRAE Fundamentals provides polynomial correlations for saturation pressure over the range -148°F to 392°F (-100°C to 200°C):

**For Temperature Range -148°F to 32°F (-100°C to 0°C) - Over Ice:**
```
ln(P_sat) = C₁/T + C₂ + C₃×T + C₄×T² + C₅×T³ + C₆×T⁴ + C₇×ln(T)
```

**Constants (SI Units, Temperature in Kelvin, Pressure in Pa):**
- C₁ = -5.6745359 × 10³
- C₂ = 6.3925247
- C₃ = -9.6778430 × 10⁻³
- C₄ = 6.2215701 × 10⁻⁷
- C₅ = 2.0747825 × 10⁻⁹
- C₆ = -9.4840240 × 10⁻¹³
- C₇ = 4.1635019

**For Temperature Range 32°F to 392°F (0°C to 200°C) - Over Water:**
```
ln(P_sat) = C₈/T + C₉ + C₁₀×T + C₁₁×T² + C₁₂×T³ + C₁₃×ln(T)
```

**Constants (SI Units):**
- C₈ = -5.8002206 × 10³
- C₉ = 1.3914993
- C₁₀ = -4.8640239 × 10⁻²
- C₁₁ = 4.1764768 × 10⁻⁵
- C₁₂ = -1.4452093 × 10⁻⁸
- C₁₃ = 6.5459673

## Dew Point Calculation Methods

### Direct Calculation from Vapor Pressure

If the partial pressure of water vapor is known, dew point can be calculated by inverting the saturation pressure equation.

**Approximate Method (Magnus-Tetens Inversion):**
```
T_dp = [238.3 × ln(P_v/610.78)] / [17.2694 - ln(P_v/610.78)]
```

Where:
- T_dp = Dew point temperature (°C)
- P_v = Water vapor partial pressure (Pa)

**IP Units Version:**
```
T_dp(°F) = T_dp(°C) × 1.8 + 32
```

### Calculation from Dry-Bulb and Relative Humidity

When dry-bulb temperature and relative humidity are known:

**Step 1:** Calculate saturation pressure at dry-bulb temperature
```
P_sat(T_db) = f(T_db)  [Use Magnus-Tetens or ASHRAE equation]
```

**Step 2:** Calculate actual vapor pressure
```
P_v = RH × P_sat(T_db)
```

**Step 3:** Invert saturation equation to find T_dp
```
T_dp = f⁻¹(P_v)  [Use inverse of saturation equation]
```

### Calculation from Wet-Bulb Temperature

The wet-bulb temperature provides an independent measurement that can be used with dry-bulb to determine dew point:

**Approximate Relation (Valid for Standard Atmospheric Pressure):**
```
T_dp ≈ T_wb - (100 - RH) / 5  [°F]
T_dp ≈ T_wb - (100 - RH) / 9  [°C]
```

More accurate methods require iterative psychrometric calculations using energy balance at the wet-bulb surface.

## Psychrometric Chart Determination

### Graphical Method

The psychrometric chart provides a direct graphical method for dew point determination:

1. Locate the state point using dry-bulb temperature (x-axis) and humidity ratio or RH (curved lines)
2. Move horizontally to the left (constant humidity ratio line) until intersecting the saturation curve (100% RH)
3. Read the temperature at this intersection - this is the dew point temperature

**Advantages:**
- Visual representation of thermodynamic state
- Simultaneous display of multiple properties
- Intuitive understanding of condensation potential

**Limitations:**
- Limited precision (typically ±0.5°F for dew point reading)
- Valid for single barometric pressure
- Requires properly scaled chart

### Digital Psychrometric Tools

Modern psychrometric software and calculators use iterative numerical methods to solve the coupled equations:

1. Input two independent properties (e.g., T_db and RH)
2. Calculate humidity ratio from saturation equations
3. Determine vapor pressure from humidity ratio
4. Solve inverse saturation equation for dew point
5. Verify solution convergence (typically within 0.01°F)

## Altitude and Pressure Effects

### Barometric Pressure Correction

Dew point temperature changes with altitude due to pressure variation. The saturation pressure curve shifts, affecting the temperature at which saturation occurs for a given humidity ratio.

**Humidity Ratio at Altitude:**
```
W = 0.621945 × P_sat(T_dp) / [P_atm(z) - P_sat(T_dp)]
```

Where P_atm(z) is the atmospheric pressure at elevation z.

**Standard Atmospheric Pressure Variation:**
```
P_atm(z) = 14.696 × [1 - 6.8754 × 10⁻⁶ × z]^5.2559  [psia, z in feet]
P_atm(z) = 101325 × [1 - 2.25577 × 10⁻⁵ × z]^5.2559  [Pa, z in meters]
```

### Elevation Impact Table

| Elevation (ft) | Atmospheric Pressure (psia) | Pressure Ratio | Dew Point Shift* (°F) |
|----------------|----------------------------|----------------|----------------------|
| Sea Level      | 14.696                     | 1.000          | 0.0                  |
| 2,500          | 13.658                     | 0.929          | -0.5                 |
| 5,000          | 12.683                     | 0.863          | -1.1                 |
| 7,500          | 11.766                     | 0.801          | -1.7                 |
| 10,000         | 10.903                     | 0.742          | -2.4                 |

*Approximate shift for same humidity ratio, referenced to sea level

**Design Implication:** At high elevations, the same humidity ratio produces a slightly lower dew point temperature, marginally reducing condensation risk. However, this effect is typically less than 3°F for elevations below 10,000 feet and is often neglected in practical analysis.

## Application to Condensation Analysis

### Surface Condensation Prediction

Condensation occurs when a surface temperature falls below the dew point of adjacent air. The critical condition:

```
T_surface < T_dp  →  Condensation occurs
```

**Surface Temperature Calculation:**
```
T_surface = T_indoor - R_i × q"
```

Where:
- R_i = Inside surface film resistance (h·ft²·°F/BTU)
- q" = Heat flux through surface (BTU/h·ft²)

**Heat Flux:**
```
q" = (T_indoor - T_outdoor) / R_total
```

Where R_total is the total thermal resistance of the assembly.

### Condensation Plane Temperature Profile

Within a multi-layer assembly, the temperature at any plane can be calculated:

```
T(x) = T_indoor - [(T_indoor - T_outdoor) / R_total] × R(x)
```

Where:
- T(x) = Temperature at distance x from inside surface
- R(x) = Cumulative thermal resistance from inside surface to point x

**Condensation Risk Assessment:**
1. Calculate temperature profile through assembly
2. Determine dew point of indoor air (or air at specific location)
3. Identify planes where T(plane) < T_dp
4. Evaluate moisture accumulation potential

### Winter Design Conditions

ASHRAE 90.1 and building codes typically specify indoor winter conditions:

**Standard Indoor Conditions:**
- Temperature: 68-72°F (20-22°C)
- Relative Humidity: 30-40% (residential/commercial)
- Resulting Dew Point: 37-45°F (3-7°C)

**Outdoor Design Conditions:**
- Use 99.6% or 99% heating design temperature
- Assume outdoor RH corresponding to typical winter conditions
- Calculate outdoor dew point (typically -10°F to 20°F, -23°C to -7°C)

### Critical Surface Temperatures

For standard indoor conditions, critical surface temperatures below which condensation occurs:

| Indoor RH (%) | Indoor T (°F) | Dew Point (°F) | Maximum U-Factor* (BTU/h·ft²·°F) |
|---------------|---------------|----------------|----------------------------------|
| 20            | 70            | 32.8           | 0.22                             |
| 30            | 70            | 41.0           | 0.14                             |
| 40            | 70            | 47.3           | 0.10                             |
| 50            | 70            | 52.3           | 0.07                             |
| 60            | 70            | 56.4           | 0.05                             |

*For outdoor temperature = 0°F, assuming inside surface film resistance = 0.68 h·ft²·°F/BTU

## Interstitial Condensation Analysis

### Vapor Pressure Gradient

Within building assemblies, water vapor diffuses from high vapor pressure to low vapor pressure. The vapor pressure profile must be compared against the saturation pressure profile.

**Vapor Pressure at Location x:**
```
P_v(x) = P_v,in - [(P_v,in - P_v,out) / Z_total] × Z(x)
```

Where:
- Z(x) = Cumulative vapor permeance resistance from inside to point x
- Z_total = Total vapor permeance resistance through assembly

**Saturation Pressure at Location x:**
```
P_sat(x) = P_sat[T(x)]
```

Where T(x) is the temperature at location x from thermal analysis.

**Condensation Criterion:**
```
If P_v(x) > P_sat(x), then condensation occurs at location x
```

### Glaser Method

The Glaser method (EN ISO 13788) provides a systematic approach to interstitial condensation analysis:

**Step 1:** Establish boundary conditions (T_in, RH_in, T_out, RH_out)

**Step 2:** Calculate temperature profile through assembly using steady-state heat transfer

**Step 3:** Calculate saturation pressure profile using P_sat = f(T)

**Step 4:** Calculate vapor pressure profile using vapor diffusion equations

**Step 5:** Identify condensation planes where vapor pressure line intersects saturation pressure line

**Step 6:** Calculate condensation rate at each plane:
```
g_c = (P_v,approach - P_sat) / Z_segment  [lb/h·ft² or kg/s·m²]
```

### Dew Point Depression

When vapor pressure equals saturation pressure, the local temperature equals the local dew point. The temperature depression below the nominal thermal profile indicates condensation potential:

```
ΔT_dp = T(x) - T_dp,local(x)
```

Where:
- ΔT_dp = Dew point depression (temperature margin)
- T(x) = Actual temperature at location x
- T_dp,local(x) = Dew point of vapor at location x

**Design Target:** Maintain ΔT_dp > 5°F (3°C) throughout assembly to provide safety margin against condensation.

## Measurement and Instrumentation

### Chilled Mirror Hygrometer

Chilled mirror hygrometers provide the most accurate dew point measurements (±0.4°F accuracy):

**Operating Principle:**
1. Thermoelectrically cooled mirror surface
2. Optical detection of condensate formation
3. Proportional control maintains equilibrium (condensation ↔ evaporation)
4. Mirror temperature = dew point temperature

**Applications:**
- Laboratory calibration standards
- Critical humidity control verification
- Building commissioning measurements

### Capacitive Humidity Sensors

Modern thin-film capacitive sensors measure relative humidity, from which dew point is calculated:

**Typical Specifications:**
- RH Accuracy: ±2% RH (10-90% RH range)
- Temperature Accuracy: ±0.5°F
- Dew Point Accuracy: ±2-3°F (derived)

**Calculation Method:**
1. Measure T_db and RH
2. Calculate P_sat(T_db)
3. Calculate P_v = RH × P_sat(T_db)
4. Calculate T_dp from inverse saturation equation

### Measurement Location Considerations

For building envelope analysis:

**Interior Measurements:**
- 3-5 feet from exterior walls
- 4-6 feet above floor level
- Away from direct solar radiation or equipment
- Representative of bulk space conditions

**Cavity Measurements:**
- Within wall/roof cavities at critical condensation planes
- Mid-height of wall cavities
- Multiple depths to establish vapor pressure gradient

**Surface Measurements:**
- Surface temperature via infrared or contact sensors
- Adjacent air dew point for condensation risk assessment
- Account for microclimate effects near surfaces

## Design Strategies for Condensation Control

### Dew Point Management Approaches

**1. Lower Indoor Dew Point**
- Reduce interior moisture generation
- Increase ventilation rate with drier outdoor air (winter)
- Use dehumidification equipment
- Target: T_dp,indoor < T_surface,critical + 5°F margin

**2. Raise Surface Temperatures**
- Increase thermal resistance (lower U-factor)
- Eliminate thermal bridges
- Use interior insulation or thermally broken assemblies
- Target: T_surface > T_dp,indoor + 5°F margin

**3. Control Vapor Diffusion**
- Install vapor retarders on warm side of insulation
- Use variable permeability membranes
- Manage vapor drive direction seasonally
- Limit permeable materials on cold side

### Climate-Specific Considerations

**Cold Climates (Heating-Dominated):**
- Primary concern: Interior moisture condensing on cold surfaces
- Strategy: Vapor retarder on interior, high R-value insulation
- Critical dew point: Indoor air (40-50°F typical)

**Hot-Humid Climates (Cooling-Dominated):**
- Primary concern: Exterior moisture condensing on cooled surfaces
- Strategy: Vapor retarder on exterior, manage indoor humidity
- Critical dew point: Outdoor air (60-75°F typical)

**Mixed Climates:**
- Bi-directional vapor drive potential
- Strategy: "Smart" vapor retarders that adjust permeability with humidity
- Monitor both heating and cooling season risks

### Critical Assembly Details

**Window and Door Frames:**
- Frame temperatures often 10-20°F below wall surface temperatures
- Thermal break requirements based on indoor dew point
- Condensation resistance factor (CRF) correlation with dew point

**Thermal Bridges:**
- Steel studs, concrete columns, structural penetrations
- Local surface temperature can drop 15-25°F below surrounding surfaces
- Isolated dew point analysis at bridge locations required

**Corners and Edges:**
- Multi-dimensional heat flow reduces inside surface temperatures
- Corner temperatures typically 5-10°F below field-of-wall
- Increased insulation or interior corner insulation detailing

## ASHRAE Standards and Design Guidance

### ASHRAE 90.1 - Energy Standard

Section 5.5.3.1 addresses moisture control:
- Vapor retarders required in Climate Zones 5, 6, 7, 8, and Marine 4
- Class I, II, or III vapor retarders based on assembly design
- Exemptions for demonstrated hygrothermal performance

### ASHRAE 160 - Design Criteria

ASHRAE Standard 160 provides criteria for hygrothermal analysis:

**Surface Condensation:**
- 30-day running average RH < 80% on interior surfaces
- Accounts for moisture buffering capacity of materials
- Temperature-RH interaction effects

**Interstitial Condensation:**
- Monthly moisture accumulation must not exceed drying capacity
- 12-month net moisture accumulation ≤ 0
- Materials must maintain structural integrity

### ASHRAE Fundamentals Chapter 25

Provides comprehensive guidance on:
- Moisture transport mechanisms
- Dew point calculation methods
- Condensation prediction procedures
- Material moisture properties
- Climate data for hygrothermal analysis

## Advanced Considerations

### Transient Effects

Steady-state dew point analysis may not capture:
- Diurnal temperature/humidity cycles
- Seasonal lag effects in massive assemblies
- Solar-driven vapor transport
- Moisture storage and release in hygroscopic materials

**Transient Analysis Requirements:**
- Hourly simulation using software (WUFI, DELPHIN, HygIRC)
- Material moisture storage properties
- Coupled heat and moisture transport equations
- Climate data with sufficient temporal resolution

### Surface Effects and Microclimate

Actual surface dew point may differ from bulk air:
- Radiation exchange affects surface temperature
- Boundary layer humidity can differ from room average
- Air movement patterns influence local conditions

**Surface Heat Balance:**
```
q_conv + q_rad + q_latent = q_cond
```

When condensation occurs, latent heat release must be included in thermal analysis.

### Sorption and Capillary Condensation

Below 100% RH, hygroscopic materials can absorb moisture through:
- Adsorption on pore surfaces (monolayer formation)
- Capillary condensation in small pores (Kelvin effect)
- Dissolution of salts (deliquescence)

**Kelvin Equation for Capillary Condensation:**
```
RH = exp(-2γV_m / rRT)
```

This moisture uptake can occur at RH well below 100%, complicating dew point-based analysis for porous materials.

## Calculation Example

**Problem:** Determine if condensation will occur on the interior surface of a wall with U = 0.08 BTU/h·ft²·°F.

**Given:**
- Indoor: T_in = 70°F, RH_in = 40%
- Outdoor: T_out = 5°F
- Inside surface film resistance: R_i = 0.68 h·ft²·°F/BTU

**Solution:**

**Step 1:** Calculate indoor dew point
```
P_sat(70°F) = 0.3631 psia  [from steam tables or Magnus-Tetens]
P_v = 0.40 × 0.3631 = 0.1452 psia
T_dp = 44.6°F  [from inverse saturation equation]
```

**Step 2:** Calculate heat flux
```
R_total = 1/U = 1/0.08 = 12.5 h·ft²·°F/BTU
q" = (70 - 5) / 12.5 = 5.2 BTU/h·ft²
```

**Step 3:** Calculate inside surface temperature
```
T_surface = 70 - 0.68 × 5.2 = 66.5°F
```

**Step 4:** Compare to dew point
```
T_surface = 66.5°F > T_dp = 44.6°F
Margin = 66.5 - 44.6 = 21.9°F
```

**Conclusion:** No condensation. Surface temperature remains 21.9°F above dew point, providing substantial safety margin.

## Summary

Dew point temperature is the fundamental parameter for condensation analysis in building envelopes. Accurate determination requires:

- Understanding of psychrometric relationships between T_db, RH, W, and T_dp
- Proper application of saturation pressure equations (Magnus-Tetens or ASHRAE correlations)
- Calculation or measurement methods appropriate to available input data
- Consideration of altitude/pressure effects in non-standard conditions

For condensation control:
- Calculate temperature profiles through assemblies using thermal resistance networks
- Compare local temperatures to dew point of vapor at each location
- Maintain minimum 5°F margin between surface/plane temperature and dew point
- Apply climate-appropriate vapor control strategies
- Verify designs using ASHRAE 160 criteria or hygrothermal simulation

Proper dew point analysis prevents moisture damage, maintains material durability, ensures occupant comfort, and supports energy-efficient building envelope design.
