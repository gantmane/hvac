---
title: "Surface Condensation"
description: "Comprehensive analysis of surface condensation in building envelopes, including thermal bridge effects, surface temperature calculations, condensation risk assessment, and prevention strategies for HVAC professionals"
weight: 2
---

## Fundamentals of Surface Condensation

Surface condensation occurs when the temperature of a building surface falls below the dew point temperature of the adjacent air. This phenomenon represents a critical failure mode in building envelope design, leading to moisture accumulation, mold growth, material deterioration, and occupant health concerns.

The physical principle governing surface condensation:

**Surface condensation occurs when:** T<sub>surface</sub> ≤ T<sub>dewpoint</sub>

Where:
- T<sub>surface</sub> = actual surface temperature (°F or °C)
- T<sub>dewpoint</sub> = dew point temperature of adjacent air (°F or °C)

The dew point temperature represents the saturation temperature at which water vapor in air begins to condense. This temperature depends solely on the moisture content of the air and can be calculated from dry-bulb temperature and relative humidity.

### Psychrometric Relationships

The dew point temperature is determined from psychrometric relationships:

**Approximate dew point calculation (IP units):**

T<sub>dp</sub> = T - ((100 - RH) / 5)

**More accurate Magnus-Tetens formula (SI units):**

T<sub>dp</sub> = (b × α(T, RH)) / (a - α(T, RH))

Where:
- α(T, RH) = (a × T) / (b + T) + ln(RH/100)
- a = 17.27 (dimensionless)
- b = 237.7°C
- T = dry-bulb temperature (°C)
- RH = relative humidity (%)

## Surface Temperature Calculation

The surface temperature of building envelope components is calculated using heat transfer principles and thermal resistance values.

### Interior Surface Temperature

For a wall or envelope assembly exposed to interior and exterior conditions:

**T<sub>si</sub> = T<sub>i</sub> - q × R<sub>si</sub>**

Where:
- T<sub>si</sub> = interior surface temperature (°F or °C)
- T<sub>i</sub> = interior air temperature (°F or °C)
- q = heat flux through assembly (Btu/h·ft² or W/m²)
- R<sub>si</sub> = interior surface film resistance (h·ft²·°F/Btu or m²·K/W)

The heat flux through the assembly:

**q = (T<sub>i</sub> - T<sub>o</sub>) / R<sub>total</sub>**

Where:
- T<sub>o</sub> = outdoor air temperature (°F or °C)
- R<sub>total</sub> = total thermal resistance of assembly (h·ft²·°F/Btu or m²·K/W)

**Substituting and rearranging:**

**T<sub>si</sub> = T<sub>i</sub> - [(T<sub>i</sub> - T<sub>o</sub>) / R<sub>total</sub>] × R<sub>si</sub>**

**Alternative form:**

**T<sub>si</sub> = T<sub>i</sub> - (T<sub>i</sub> - T<sub>o</sub>) × (R<sub>si</sub> / R<sub>total</sub>)**

This demonstrates that interior surface temperature depends on the ratio of interior surface resistance to total assembly resistance.

### Temperature Index Method

The Temperature Index (TI) provides a normalized measure of surface temperature:

**TI = (T<sub>si</sub> - T<sub>o</sub>) / (T<sub>i</sub> - T<sub>o</sub>)**

Temperature Index ranges from 0 to 1:
- TI = 1.0: surface at interior air temperature (no heat loss)
- TI = 0.0: surface at exterior air temperature (no insulation)
- TI > 0.7: generally acceptable for condensation resistance

**Relationship to thermal resistance:**

**TI = (R<sub>total</sub> - R<sub>si</sub>) / R<sub>total</sub> = 1 - (R<sub>si</sub> / R<sub>total</sub>)**

This equation shows that higher total R-values produce higher temperature indices and warmer interior surfaces.

## Thermal Bridging Effects

Thermal bridges are localized areas of higher heat flow that create cold spots on interior surfaces, significantly increasing condensation risk.

### Common Thermal Bridge Locations

**Structural elements:**
- Steel studs in exterior walls
- Concrete slab edges
- Structural columns and beams penetrating envelope
- Balcony connections

**Envelope transitions:**
- Wall-to-roof junctions
- Wall-to-floor interfaces
- Foundation wall-to-wall connections
- Window and door frames

**Mechanical penetrations:**
- Pipe and duct penetrations
- Electrical conduit runs
- Recessed lighting fixtures

### Linear Thermal Transmittance

Thermal bridges are characterized by linear thermal transmittance (ψ-value):

**ψ = (L<sub>2D</sub> - ΣU<sub>j</sub> × l<sub>j</sub>)**

Where:
- ψ = linear thermal transmittance (W/m·K or Btu/h·ft·°F)
- L<sub>2D</sub> = thermal coupling coefficient from 2D analysis (W/m·K)
- U<sub>j</sub> = U-factor of 1D element j (W/m²·K)
- l<sub>j</sub> = length of 1D element j (m)

The additional heat loss due to thermal bridging:

**Q<sub>bridge</sub> = ψ × L × ΔT**

Where:
- Q<sub>bridge</sub> = heat loss through thermal bridge (W or Btu/h)
- L = length of thermal bridge (m or ft)
- ΔT = temperature difference (K or °F)

### Steel Stud Thermal Bridging

Steel studs create significant thermal bridging due to their high thermal conductivity (k ≈ 45 W/m·K vs. 0.04 W/m·K for insulation).

**Effective R-value of steel-framed wall:**

**R<sub>eff</sub> = 1 / [(f<sub>s</sub> / R<sub>stud path</sub>) + ((1 - f<sub>s</sub>) / R<sub>cavity</sub>)]**

Where:
- R<sub>eff</sub> = effective R-value of assembly (h·ft²·°F/Btu)
- f<sub>s</sub> = framing fraction (typically 0.15 to 0.25)
- R<sub>stud path</sub> = R-value through stud path (h·ft²·°F/Btu)
- R<sub>cavity</sub> = R-value through cavity path (h·ft²·°F/Btu)

Steel framing can reduce wall assembly R-value by 40-60% compared to clear-wall R-value.

## Surface Film Coefficients

Surface film coefficients significantly impact surface temperature calculations.

### Interior Surface Coefficients

ASHRAE provides standard interior surface film coefficients:

| Surface Position | h<sub>i</sub> (Btu/h·ft²·°F) | h<sub>i</sub> (W/m²·K) | R<sub>si</sub> (h·ft²·°F/Btu) | R<sub>si</sub> (m²·K/W) |
|------------------|------------------------------|------------------------|-------------------------------|------------------------|
| Horizontal, heat flow up | 1.63 | 9.26 | 0.61 | 0.108 |
| Vertical surface | 1.46 | 8.29 | 0.68 | 0.121 |
| Horizontal, heat flow down | 1.08 | 6.13 | 0.92 | 0.163 |
| 45° slope, heat flow up | 1.60 | 9.09 | 0.62 | 0.110 |
| 45° slope, heat flow down | 1.32 | 7.50 | 0.76 | 0.134 |

### Exterior Surface Coefficients

Exterior surface coefficients depend on wind speed and surface orientation:

| Wind Speed | h<sub>o</sub> (Btu/h·ft²·°F) | h<sub>o</sub> (W/m²·K) | R<sub>so</sub> (h·ft²·°F/Btu) | R<sub>so</sub> (m²·K/W) |
|------------|------------------------------|------------------------|-------------------------------|------------------------|
| 7.5 mph (winter) | 6.00 | 34.0 | 0.17 | 0.030 |
| 15 mph | 7.20 | 40.9 | 0.14 | 0.024 |
| Summer (natural) | 4.00 | 22.7 | 0.25 | 0.044 |

### Still Air Conditions

For enclosed air spaces and cavities:

| Application | h (Btu/h·ft²·°F) | h (W/m²·K) | R (h·ft²·°F/Btu) | R (m²·K/W) |
|-------------|------------------|------------|------------------|-----------|
| Non-reflective surface | 1.10 | 6.25 | 0.91 | 0.160 |
| Single reflective surface | 0.59 | 3.35 | 1.70 | 0.299 |
| Double reflective surface | 0.30 | 1.70 | 3.33 | 0.588 |

## Window Condensation

Windows represent the most common location for surface condensation due to their lower thermal resistance compared to opaque walls.

### Window Surface Temperature

For a simple window with single interior surface:

**T<sub>window</sub> = T<sub>i</sub> - (T<sub>i</sub> - T<sub>o</sub>) × (h<sub>i</sub> / (U<sub>window</sub>))**

Or equivalently:

**T<sub>window</sub> = T<sub>i</sub> - (T<sub>i</sub> - T<sub>o</sub>) × (R<sub>si</sub> / (1/U<sub>window</sub>))**

Where U<sub>window</sub> is the center-of-glass U-factor.

### Condensation Resistance Rating

The Condensation Resistance (CR) rating provides a standardized metric for window performance:

**CR = 100 × [1 - (U<sub>window</sub> × R<sub>si</sub>)]**

Condensation Resistance ratings range from 0 to 100:
- CR ≥ 50: Acceptable for most climates
- CR ≥ 60: Good performance for cold climates
- CR ≥ 70: Excellent performance for extreme climates

### Window Performance Comparison

| Glazing Type | U-Factor (Btu/h·ft²·°F) | U-Factor (W/m²·K) | CR Rating | Min. T<sub>o</sub> at 70°F, 40% RH |
|--------------|-------------------------|-------------------|-----------|-------------------------------------|
| Single glazing | 1.04 | 5.91 | 29 | 59°F (15°C) |
| Double, air fill | 0.49 | 2.78 | 67 | 30°F (-1°C) |
| Double, argon fill | 0.42 | 2.39 | 71 | 23°F (-5°C) |
| Triple, argon fill | 0.20 | 1.14 | 86 | -1°F (-18°C) |
| Triple, krypton, low-e | 0.15 | 0.85 | 90 | -14°F (-26°C) |

Minimum outdoor temperature calculated for condensation at interior conditions of 70°F (21°C) and 40% RH (dew point 45°F or 7°C).

### Edge-of-Glass and Frame Effects

The edge-of-glass region (within 2.5 inches of frame) exhibits higher heat loss due to:

- Reduced insulating air space width
- Spacer thermal bridging
- Frame proximity effects

Edge-of-glass U-factors typically 10-30% higher than center-of-glass values.

**Frame condensation risk zones:**

| Frame Material | Thermal Conductivity | Condensation Risk |
|----------------|---------------------|-------------------|
| Aluminum, no break | k = 160 W/m·K | Extremely high |
| Aluminum, thermal break | k<sub>eff</sub> = 5-10 W/m·K | High |
| Vinyl, hollow chamber | k<sub>eff</sub> = 0.15-0.20 W/m·K | Low |
| Wood | k = 0.10-0.15 W/m·K | Very low |
| Fiberglass | k = 0.25-0.35 W/m·K | Low |

## Corner Conditions and Multidimensional Heat Flow

Building corners experience multidimensional heat flow, creating surface temperatures lower than one-dimensional calculations predict.

### Corner Temperature Depression

At inside corners (two exterior walls meeting), heat flows in two directions, creating a localized cold zone.

**Approximate corner temperature:**

**T<sub>corner</sub> ≈ T<sub>wall</sub> - [(T<sub>i</sub> - T<sub>o</sub>) × 0.1 to 0.2]**

The temperature depression factor depends on:
- Wall R-value
- Corner geometry (90° vs. other angles)
- Interior surface coefficient
- Insulation continuity

### Critical Corner Locations

**Exterior corners (inside the building):**
- Wall-to-wall inside corners
- Wall-to-ceiling corners
- Wall-to-floor corners
- Three-way intersections

**Mitigation strategies:**
- Continuous insulation across corners
- Increased insulation thickness at corners
- Air sealing to prevent convective loops
- Interior finish details to improve air circulation

## Cold Surface Condensation Risk Assessment

### Condensation Potential Index

The Condensation Potential Index (CPI) quantifies condensation risk:

**CPI = (T<sub>surface</sub> - T<sub>dewpoint</sub>) / (T<sub>i</sub> - T<sub>dewpoint</sub>)**

**Risk assessment criteria:**

| CPI Value | Risk Level | Design Recommendation |
|-----------|------------|------------------------|
| CPI > 1.0 | No risk | Surface above interior air temp (unusual) |
| 0.2 < CPI < 1.0 | Low risk | Acceptable for most applications |
| 0.0 < CPI < 0.2 | Moderate risk | Enhanced ventilation recommended |
| -0.2 < CPI < 0.0 | High risk | Redesign required |
| CPI < -0.2 | Severe risk | Unacceptable, guaranteed condensation |

### Surface Relative Humidity Prediction

The relative humidity at a surface can be calculated without explicit dew point:

**RH<sub>surface</sub> = RH<sub>interior</sub> × exp[(-L × (T<sub>i</sub> - T<sub>surface</sub>)) / (T<sub>surface</sub> + 273.15)²]**

Where:
- L = 5420 K (latent heat constant)
- T<sub>surface</sub> in Kelvin for SI units
- RH expressed as decimal (e.g., 0.50 for 50%)

**Mold growth threshold:** RH<sub>surface</sub> > 80% for extended periods

## Design Conditions for Condensation Analysis

### ASHRAE Winter Design Conditions

Condensation analysis should use 99% or 99.6% winter design temperatures, not extreme minimums.

**Common design interior conditions:**

| Building Type | Temperature (°F) | Temperature (°C) | Relative Humidity |
|---------------|------------------|------------------|-------------------|
| Residential | 68-72 | 20-22 | 30-40% |
| Office | 70-72 | 21-22 | 30-40% |
| School | 68-72 | 20-22 | 30-50% |
| Hospital | 70-75 | 21-24 | 30-60% |
| Museum | 68-72 | 20-22 | 45-55% |
| Indoor pool | 75-85 | 24-29 | 50-60% |

### Climate-Specific Considerations

**Cold climate (Climate Zones 6-8):**
- Use 99.6% design temperature
- Assume 35% interior RH as upper limit for residential
- Consider vapor retarders on interior side

**Mixed-humid climate (Climate Zones 4A):**
- Analyze both winter and summer condensation
- Consider vapor-open assemblies
- Interior humidity may exceed 50% in summer

**Hot-humid climate (Climate Zones 1-3):**
- Reverse condensation risk (exterior warm/humid, interior cool/dry)
- Never use interior vapor barriers
- Consider vapor retarders on exterior

## Thermal Imaging Analysis

Infrared thermography provides direct measurement of surface temperatures for condensation risk assessment.

### Thermographic Survey Procedures

**Survey requirements:**
- Minimum 20°F (11°C) temperature difference across envelope
- Performed during heating season for cold climate analysis
- Interior surfaces surveyed from inside
- Exterior surfaces surveyed from outside

**Temperature measurement accuracy:**
- Emissivity setting: 0.90-0.95 for painted surfaces
- Reflected temperature compensation required
- Atmospheric correction for exterior surveys

### Identifying Condensation Risk Zones

**Thermal anomalies indicating high condensation risk:**

| Temperature Depression | Risk Level | Likely Cause |
|------------------------|------------|--------------|
| 2-4°F (1-2°C) below adjacent surface | Low | Normal variation |
| 5-8°F (3-4°C) below adjacent surface | Moderate | Minor thermal bridge |
| 9-15°F (5-8°C) below adjacent surface | High | Significant thermal bridge |
| >15°F (>8°C) below adjacent surface | Severe | Missing insulation or major defect |

### Quantitative Analysis

From thermal images, calculate condensation margin:

**Condensation Margin = T<sub>measured</sub> - T<sub>dewpoint</sub>**

**Safety factor:**
- Margin ≥ 5°F (3°C): Acceptable
- Margin = 2-5°F (1-3°C): Monitor during cold weather
- Margin < 2°F (<1°C): High risk, mitigation required

## Prevention Strategies and Best Practices

### Envelope Design Measures

**Increase thermal resistance:**
- Higher R-value insulation
- Continuous insulation over framing
- Thermal break in metal components
- High-performance glazing systems

**Minimize thermal bridging:**
- Advanced framing techniques
- Structural thermal breaks at balconies
- Insulated concrete forms (ICF)
- Thermally broken window frames

**Typical minimum R-values to prevent condensation at 70°F, 40% RH, -10°F outdoor:**

| Climate Zone | Min. Wall R-value | Min. Roof R-value | Min. Window U-factor |
|--------------|-------------------|-------------------|----------------------|
| 6 | R-20 | R-49 | U-0.35 |
| 7 | R-25 | R-60 | U-0.30 |
| 8 | R-30 | R-60 | U-0.25 |

### Humidity Control Strategies

**Source control:**
- Kitchen and bathroom exhaust ventilation
- Clothes dryer vented to exterior
- No unvented combustion appliances
- Dehumidification in high-moisture areas

**Ventilation requirements (ASHRAE 62.2):**
- Continuous mechanical ventilation in tight buildings
- Minimum 7.5 cfm per occupant + 1 cfm per 100 ft² floor area
- Balanced ventilation with heat recovery in cold climates

**Target interior humidity levels:**

| Outdoor Temperature | Maximum Interior RH (%) |
|---------------------|-------------------------|
| 40°F (4°C) | 45% |
| 20°F (-7°C) | 40% |
| 0°F (-18°C) | 35% |
| -10°F (-23°C) | 30% |
| -20°F (-29°C) | 25% |

### Surface Temperature Enhancement

**Interior surface measures:**
- Increase interior surface coefficient through air circulation
- Avoid furniture blocking exterior walls
- Ensure registers direct air across cold surfaces
- Eliminate dead air zones at corners and behind furniture

**Insulation placement:**
- Eliminate compression at corners and edges
- Extend insulation fully into corners
- Seal insulation to framing to eliminate air gaps
- Use spray foam at difficult-to-insulate locations

### Detail Design Considerations

**Critical details requiring special attention:**

1. **Foundation wall-to-frame wall transition**
   - Continuous insulation across transition
   - Air barrier continuity maintained
   - No thermal short-circuit through rim joist

2. **Window rough opening**
   - Sill pan for drainage
   - Continuous air barrier around frame
   - Insulation packed to frame (not compressed)
   - Interior return (if used) detailed to avoid cold surface

3. **Roof-to-wall connection**
   - Raised heel truss or energy truss
   - Full-depth insulation extending over wall top plate
   - Ventilation baffles maintaining air space

4. **Pipe and duct penetrations**
   - Seal penetrations with appropriate materials
   - Insulate penetrating elements
   - Maintain insulation continuity around penetrations

## Performance Verification

### Calculation Verification

**Required analysis for critical projects:**
- 2D or 3D heat transfer modeling at thermal bridges
- Hygrothermal simulation for moisture accumulation risk
- Annual moisture balance calculations

**Software tools:**
- THERM (2D heat transfer)
- WUFI (hygrothermal analysis)
- HEAT3 (3D heat transfer)

### Field Verification Methods

**During construction:**
- Infrared thermography of completed assemblies
- Blower door testing for air leakage
- Tracer gas testing for specific leak locations
- Insulation depth verification

**Post-occupancy:**
- Winter season thermographic survey
- Surface temperature monitoring at critical locations
- Indoor humidity monitoring
- Occupant feedback on condensation occurrence

### Acceptance Criteria

**Performance metrics:**

| Parameter | Target | Acceptable | Marginal | Unacceptable |
|-----------|--------|------------|----------|--------------|
| Window CR rating | ≥70 | ≥60 | 50-59 | <50 |
| Surface temp margin | >5°F | 3-5°F | 1-3°F | <1°F |
| Surface RH | <70% | 70-75% | 75-80% | >80% |
| Thermal bridge ψ-value | <0.1 | 0.1-0.2 | 0.2-0.3 | >0.3 W/m·K |

## Code and Standard References

**ASHRAE Standards:**
- ASHRAE 90.1: Energy Standard for Buildings Except Low-Rise Residential Buildings
- ASHRAE 160: Criteria for Moisture-Control Design Analysis in Buildings
- ASHRAE Handbook - Fundamentals, Chapter 25: Heat, Air, and Moisture Control

**Building Codes:**
- International Energy Conservation Code (IECC)
- International Residential Code (IRC), Chapter 11
- International Building Code (IBC), Chapter 14

**Related Standards:**
- NFRC 500: Procedure for Determining Fenestration Product Condensation Resistance
- ISO 13788: Hygrothermal Performance of Building Components
- ASTM C1363: Standard Test Method for Thermal Performance of Building Materials

## Conclusion

Surface condensation analysis requires understanding of heat transfer, psychrometrics, building envelope construction, and climate conditions. Proper design considers thermal bridging, utilizes accurate surface temperature calculations, and verifies performance through analysis and field testing. Prevention strategies include enhanced thermal resistance, thermal bridge mitigation, humidity control, and careful detailing at critical locations. HVAC professionals must integrate envelope performance with mechanical system design to achieve condensation-free building envelopes throughout the service life.
