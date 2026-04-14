---
title: "Psychrometric Chart"
aliases: ["Psychrometric Chart"]
description: "Comprehensive guide to psychrometric chart construction, interpretation, and application for HVAC process analysis and system design"
weight: 2
---

The psychrometric chart represents the graphical solution of psychrometric equations, providing a visual tool for analyzing air conditioning processes. This chart plots the thermodynamic properties of moist air mixtures at constant barometric pressure, enabling rapid determination of air state points and process paths without iterative calculations.

## Chart Construction Fundamentals

The psychrometric chart depicts the relationship between seven independent and dependent properties of moist air. The chart construction follows established thermodynamic principles derived from the ideal gas law and Dalton's law of partial pressures.

### Chart Axes Configuration

**Primary horizontal axis (abscissa):**
- Dry-bulb temperature (°F or °C)
- Represents sensible heat content
- Linear scale from approximately 20°F to 120°F for standard charts
- Extended range charts available for specialized applications

**Primary vertical axis (ordinate):**
- Humidity ratio (lb water/lb dry air or kg/kg)
- Mass of water vapor per unit mass of dry air
- Linear scale from 0 to saturation conditions
- Also termed moisture content or mixing ratio

### Coordinate System Characteristics

The chart employs an oblique-angle coordinate system where the dry-bulb temperature lines intersect the humidity ratio axis at approximately 90°, while the saturation curve creates the upper boundary. This configuration optimizes the usable chart area for typical HVAC processes occurring between 40°F and 100°F dry-bulb temperature.

## Chart Lines and Properties

### Constant Dry-Bulb Temperature Lines

Vertical straight lines parallel to the ordinate represent constant dry-bulb temperature. These lines indicate pure humidification or dehumidification processes where sensible heat remains constant while moisture content changes.

**Process applications:**
- Steam injection humidification (nearly constant dry-bulb)
- Chemical dehumidification with minimal heat addition
- Moisture removal via desiccants

### Saturation Curve

The saturation curve (100% relative humidity line) forms the left boundary of the chart. This curve represents the maximum moisture content air can hold at each temperature before condensation occurs.

**Key characteristics:**
- Exponential relationship between temperature and saturation pressure
- Derived from the Clausius-Clapeyron equation
- Represents dew point temperature for any state point
- Defines the wet-bulb temperature scale along the curve

### Constant Relative Humidity Lines

Curved lines approximately parallel to the saturation curve represent constant relative humidity percentages. These lines typically range from 10% to 90% RH in 10% increments.

**Mathematical basis:**

φ = (Pw / Pws) × 100

Where:
- φ = relative humidity (%)
- Pw = partial pressure of water vapor (psia)
- Pws = saturation pressure at dry-bulb temperature (psia)

### Constant Wet-Bulb Temperature Lines

Diagonal lines sloping from upper left to lower right represent constant wet-bulb temperature. These lines intersect the saturation curve at the corresponding wet-bulb temperature value.

**Physical significance:**
- Represents thermodynamic wet-bulb temperature
- Indicates the temperature approached during adiabatic saturation
- Nearly coincident with constant enthalpy lines at typical HVAC conditions
- Essential for evaporative cooling process analysis

**Slope characteristics:**
The wet-bulb lines slope at approximately 25-30° from horizontal, reflecting the Lewis number relationship (ratio of thermal diffusivity to mass diffusivity) for air-water vapor mixtures.

### Constant Enthalpy Lines

Diagonal lines nearly parallel to constant wet-bulb lines represent constant enthalpy (total heat content). These lines typically deviate less than 1% from wet-bulb lines in the comfort range.

**Enthalpy calculation:**

h = 0.240 × tdb + W × (1061 + 0.444 × tdb)

Where:
- h = enthalpy (Btu/lb dry air)
- tdb = dry-bulb temperature (°F)
- W = humidity ratio (lb/lb)
- 0.240 = specific heat of dry air (Btu/lb·°F)
- 1061 = latent heat of vaporization at 32°F (Btu/lb)
- 0.444 = specific heat of water vapor (Btu/lb·°F)

**Enthalpy scale location:**
The enthalpy scale appears along the saturation curve, typically on the left edge or extending beyond the chart boundary on oblique-angle charts.

### Constant Specific Volume Lines

Diagonal lines sloping from lower left to upper right represent constant specific volume (cubic feet per pound of dry air).

**Calculation basis:**

v = (0.754 × (tdb + 460) × (1 + 1.607 × W)) / Pb

Where:
- v = specific volume (ft³/lb dry air)
- tdb = dry-bulb temperature (°F)
- W = humidity ratio (lb/lb)
- Pb = barometric pressure (psia)
- 0.754 = gas constant for air (ft³·psia/lb·°R)

**Applications:**
- Air quantity calculations (CFM = mass flow × specific volume)
- Duct and equipment sizing
- Fan selection and performance analysis
- Altitude corrections for air handling capacity

### Sensible Heat Ratio (SHR) Line

The sensible heat ratio reference scale appears as a protractor-like semicircle on ASHRAE charts, typically located in the central region.

**Definition:**

SHR = Sensible Heat / Total Heat = ΔhS / ΔhT

**Usage procedure:**
1. Plot the entering air condition state point
2. Align a straightedge from the reference point through the SHR scale at the calculated ratio
3. Extend the line through the entering condition to determine the process path
4. The intersection with supply air temperature vertical line defines the supply air state

**Typical SHR values:**

| Application | SHR Range | Process Characteristics |
|-------------|-----------|-------------------------|
| Dry sensible cooling | 0.95-1.00 | Minimal latent load |
| Office spaces | 0.70-0.85 | Moderate latent loads |
| Restaurants/kitchens | 0.60-0.75 | High ventilation, moisture |
| Natatoriums | 0.40-0.60 | High evaporation rates |
| High-latency process | <0.40 | Dehumidification dominant |

## Reading and Interpreting the Chart

### Determining State Point Properties

To establish a complete air state, two independent properties must be known. Common measurement combinations include:

**Dry-bulb and wet-bulb temperatures:**
1. Locate dry-bulb temperature on horizontal axis
2. Follow constant wet-bulb line from saturation curve
3. Intersection defines the state point
4. Read all other properties from chart lines passing through this point

**Dry-bulb temperature and relative humidity:**
1. Locate dry-bulb temperature on horizontal axis
2. Follow vertical line to intersection with appropriate RH curve
3. State point intersection yields all other properties

**Dew point and dry-bulb temperatures:**
1. Locate dew point on saturation curve
2. Follow horizontal constant humidity ratio line
3. Intersection with dry-bulb vertical line defines state point

### Process Path Analysis

HVAC processes appear as paths connecting initial and final state points. The path shape indicates the nature of the process.

**Sensible heating:**
- Horizontal line moving right (constant humidity ratio)
- Dry-bulb temperature increases
- Relative humidity decreases
- Typical of heating coils with no moisture addition

**Sensible cooling:**
- Horizontal line moving left
- Dry-bulb temperature decreases
- Relative humidity increases
- Occurs when cooling coil surface temperature exceeds dew point

**Cooling and dehumidification:**
- Diagonal line moving down and left
- Both temperature and moisture content decrease
- Path approaches apparatus dew point (ADP)
- Contact factor determines actual path shape
- Representative of chilled water or DX cooling coils

**Humidification processes:**

| Process Type | Path Direction | Slope Characteristics |
|--------------|----------------|----------------------|
| Steam injection | Nearly vertical | Slight right drift, constant enthalpy |
| Evaporative cooling | Down-left along wet-bulb | Constant enthalpy, adiabatic |
| Heated water spray | Up-right | Enthalpy increases |
| Ultrasonic/atomizing | Varies with droplet size | Near-adiabatic to isothermal |

### Apparatus Dew Point (ADP)

The apparatus dew point represents the effective surface temperature of a cooling coil. The actual process path curves from the entering condition toward the ADP, with the degree of approach defined by the contact factor or bypass factor.

**Contact factor calculation:**

CF = (tdb,entering - tdb,leaving) / (tdb,entering - tADP)

**Bypass factor:**

BF = 1 - CF = (tdb,leaving - tADP) / (tdb,entering - tADP)

**Typical contact factors:**

| Coil Configuration | Rows Deep | Fins per Inch | Contact Factor |
|--------------------|-----------|---------------|----------------|
| Low velocity | 4 | 8-10 | 0.70-0.80 |
| Standard | 6 | 10-12 | 0.80-0.90 |
| High performance | 8 | 12-14 | 0.90-0.95 |
| Spray coil | Multiple | N/A | 0.95-0.98 |

## ASHRAE Chart Standards

### Chart Types and Editions

ASHRAE publishes psychrometric charts in various configurations to serve different applications and preferences.

**Standard pressure charts:**
- Chart 1: Normal temperatures (32°F to 120°F), sea level
- Chart 2: Low temperatures (-40°F to 50°F), sea level
- Chart 3: High temperatures (60°F to 250°F), sea level
- Chart 4: Very high temperatures (200°F to 400°F), sea level

**Altitude-specific charts:**
Standard atmospheric pressure decreases with elevation, requiring altitude-corrected charts for accurate analysis.

| Elevation (ft) | Barometric Pressure (psia) | Chart Designation |
|----------------|---------------------------|-------------------|
| 0 (sea level) | 14.696 | Standard |
| 2,500 | 13.65 | Chart 5 |
| 5,000 | 12.23 | Chart 6 |
| 7,500 | 11.10 | Chart 7 |
| 10,000 | 10.11 | Not standard (use equations) |

### Chart Format Variations

**Oblique-angle format:**
- Most common ASHRAE configuration
- Optimizes chart area utilization
- Enthalpy scale extends beyond chart boundary
- Better resolution in comfort zone region

**Rectangular format:**
- Right-angle coordinate system
- Simpler visual interpretation
- Less efficient space utilization
- Preferred for educational purposes

### SI Unit Charts

International versions employ SI units with identical thermodynamic principles:
- Dry-bulb temperature: °C
- Humidity ratio: g/kg or kg/kg
- Enthalpy: kJ/kg
- Specific volume: m³/kg
- Pressure: kPa

## Altitude and Barometric Pressure Corrections

### Pressure Effects on Psychrometric Properties

Barometric pressure significantly affects psychrometric relationships. The humidity ratio at saturation increases with decreasing pressure (higher altitude), while specific volume increases proportionally.

**Humidity ratio correction:**

W = 0.622 × (Pw / (Pb - Pw))

The saturation humidity ratio at 70°F changes with altitude:

| Elevation (ft) | Pressure (psia) | W saturation (lb/lb) | % Increase vs. Sea Level |
|----------------|-----------------|---------------------|-------------------------|
| 0 | 14.696 | 0.0159 | 0% |
| 2,500 | 13.65 | 0.0171 | 7.5% |
| 5,000 | 12.23 | 0.0192 | 20.8% |
| 7,500 | 11.10 | 0.0214 | 34.6% |

**Specific volume correction:**

The specific volume is inversely proportional to barometric pressure. At constant temperature and humidity ratio:

v(altitude) = v(sea level) × (Pb,sea level / Pb,altitude)

### Practical Implications

**Cooling equipment capacity:**
Cooling capacity measured in tons or Btu/hr remains constant with altitude, but airflow in CFM must increase to maintain the same mass flow rate due to increased specific volume.

**Fan power requirements:**
Static pressure requirements remain essentially constant, but volume flow increases, potentially requiring larger fan selections at high altitude.

**Evaporative cooling effectiveness:**
Higher saturation humidity ratios at altitude provide greater potential for evaporative cooling, improving wet-bulb depression.

## Design Applications and Best Practices

### Psychrometric Process Plotting

**Mixed air conditions:**
When outdoor air and return air mix, the resulting state point lies on a straight line connecting the two conditions, proportioned by mass flow ratio:

W(mix) = (m(oa) × W(oa) + m(ra) × W(ra)) / (m(oa) + m(ra))

h(mix) = (m(oa) × h(oa) + m(ra) × h(ra)) / (m(oa) + m(ra))

**Heating coil analysis:**
Plot horizontal line from entering condition to required leaving dry-bulb temperature. Heat addition equals:

q(sensible) = m × Cp × Δt = CFM × 1.08 × Δt (Btu/hr)

Where 1.08 = conversion factor incorporating density and specific heat at standard conditions.

**Cooling coil analysis:**
1. Establish entering air condition
2. Determine required leaving condition from load calculations
3. Draw line connecting points to estimate ADP
4. Verify ADP is achievable with selected chilled water or refrigerant temperature
5. Calculate required coil capacity:

q(total) = CFM × 4.5 × Δh (Btu/hr)

Where 4.5 = conversion factor for standard air density.

### Comfort Zone Representation

ASHRAE Standard 55 defines thermal comfort zones based on operative temperature and humidity. These zones can be plotted on the psychrometric chart to verify space conditions.

**Summer comfort zone (typical clothing, 0.5 clo):**
- Temperature range: 73°F to 79°F operative temperature
- Humidity range: 30% to 65% RH
- Air velocity: <40 fpm

**Winter comfort zone (typical clothing, 1.0 clo):**
- Temperature range: 68°F to 75°F operative temperature
- Humidity range: 30% to 60% RH
- Air velocity: <30 fpm

### Energy Recovery System Analysis

Energy recovery devices (heat wheels, plate heat exchangers, run-around loops) modify the outdoor air condition before mixing. The effectiveness determines the degree of approach toward return air conditions.

**Sensible effectiveness:**

ε(s) = (toa,leaving - toa,entering) / (tra - toa,entering)

**Latent effectiveness:**

ε(L) = (Woa,leaving - Woa,entering) / (Wra - Woa,entering)

Plot the leaving outdoor air condition using calculated temperature and humidity ratio, then proceed with mixing calculations.

### Economizer Cycle Optimization

The psychrometric chart provides visual analysis of economizer suitability:

**Dry-bulb economizer:**
Compare outdoor air dry-bulb temperature to return air temperature. Enable economizer when toa < tra.

**Enthalpy economizer:**
Compare outdoor air enthalpy to return air enthalpy. Enable economizer when hoa <hra. This method accounts for both temperature and humidity, preventing operation when high outdoor moisture content negates temperature benefits.

**Differential enthalpy economizer:**
Most sophisticated control strategy, incorporating both conditions plus supply air enthalpy requirements. Plot all three points to determine optimal mixing ratio.

### Coil Selection Considerations

**Leaving air temperature requirements:**
Cooling coils must achieve supply air temperature cold enough to absorb space sensible load when delivered at design airflow rate. Verify adequate separation between required supply temperature and apparatus dew point.

**Dehumidification requirements:**
When space latent loads are significant, the cooling coil must reduce moisture content sufficiently. Plot supply air condition to verify humidity ratio meets space requirements with design ventilation rates.

**Coil surface temperature:**
Chilled water temperature or refrigerant evaporating temperature must be below the apparatus dew point by sufficient margin (typically 5-8°F) to achieve required contact factor. Lower surface temperatures improve dehumidification but increase energy consumption and condensate removal requirements.

### Validation and Quality Control

**Measurement verification:**
When field-measured conditions appear inconsistent with expectations, plot values on psychrometric chart to identify potential sensor errors. Dry-bulb and wet-bulb measurements should yield consistent relative humidity and dew point values.

**Energy balance checks:**
For systems with known airflow rates and measured entering/leaving conditions, calculate energy transfer rates and compare to design specifications. Significant deviations indicate measurement errors, fouling, or equipment degradation.

**Seasonal performance analysis:**
Plot typical seasonal outdoor conditions along with space conditions and economizer changeover points to evaluate system operation and identify optimization opportunities.

## Advanced Chart Applications

### Chemical Dehumidification Process

Desiccant systems remove moisture while adding heat. The process line moves down and right on the chart, with slope determined by the ratio of moisture removal to heat addition.

**Solid desiccant wheel:**
Moisture transfer occurs with simultaneous temperature increase. Process path depends on:
- Wheel rotational speed (dwell time)
- Desiccant material properties
- Regeneration temperature
- Entering air conditions

Typical temperature rise: 15-25°F while reducing humidity ratio by 0.003-0.008 lb/lb.

### Indirect Evaporative Cooling

Indirect evaporative coolers reduce supply air temperature while maintaining constant humidity ratio through heat exchanger separation.

**Process representation:**
Primary air: Horizontal line moving left (sensible cooling only)
Secondary air: Diagonal line following wet-bulb (evaporative cooling)

**Effectiveness calculation:**

ε(IEC) = (tdb,entering - tdb,leaving) / (tdb,entering - twb,entering)

High-performance indirect evaporative coolers achieve 70-85% effectiveness, providing substantial cooling in dry climates without moisture addition.

### Multi-Stage Processes

Complex HVAC systems involve sequential processes plotted as connected line segments:

1. **Outdoor air + economizer mixing:** Straight line from outdoor to mixed point
2. **Energy recovery:** Modified outdoor air state before mixing
3. **Preheat coil:** Horizontal line right (winter only)
4. **Cooling coil:** Down and left toward ADP
5. **Reheat or fan heat:** Horizontal line right
6. **Space conditioning:** Line to room condition based on SHR

Plot each stage sequentially to verify system performance and identify optimization opportunities.

## Computational Tools and Software

Modern HVAC design increasingly relies on computational psychrometrics, but chart literacy remains essential for concept validation and troubleshooting.

**Software capabilities:**
- Precise property calculations using ASHRAE correlations
- Iterative solutions for complex processes
- Altitude and pressure corrections
- Refrigerant property integration
- Process optimization algorithms

**Chart advantages:**
- Rapid visual process understanding
- Intuitive relationship comprehension
- Communication tool for design teams
- Field troubleshooting without electronics
- Conceptual design and feasibility studies

Experienced practitioners use both methods complementarily: charts for rapid analysis and concept development, software for precise final calculations and documentation.

## References and Standards

**ASHRAE Standards:**
- ASHRAE Handbook—Fundamentals, Chapter 1: Psychrometrics
- ASHRAE Standard 41.6: Standard Method for Measurement of Moist Air Properties
- ASHRAE Psychrometric Chart (various editions and pressures)

**Calculation methods:**
- Hyland-Wexler correlations for saturation pressure
- Herrmann formulations for moist air properties
- ASHRAE-approved equations for engineering calculations

**Chart accuracy:**
Standard ASHRAE psychrometric charts provide accuracy within ±0.5% for enthalpy, ±0.0002 lb/lb for humidity ratio, and ±0.2°F for temperatures when properly interpolated within the comfort zone region.
