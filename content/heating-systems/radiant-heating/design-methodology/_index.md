---
title: "Design Methodology"
weight: 3
description: "Comprehensive radiant heating design methodology including panel sizing, mean radiant temperature calculations, comfort criteria, and system integration strategies for floor, ceiling, and wall panels."
keywords: ["radiant panel sizing", "mean radiant temperature", "thermal comfort criteria", "radiant heating design", "panel placement", "MRT calculation", "comfort equation", "radiant system integration"]
---

## Radiant Panel Sizing

Radiant panel sizing requires accurate determination of heating capacity based on panel surface temperature, panel type, and space thermal requirements. The fundamental heat transfer from radiant panels consists of both radiant and convective components.

**Heat Output Calculation:**

The total heat output from radiant panels follows:

Q = Qr + Qc

Where:
- Q = Total heat output (W/m²)
- Qr = Radiant heat transfer (W/m²)
- Qc = Convective heat transfer (W/m²)

**Radiant Heat Transfer:**

Qr = ε × σ × (Tp⁴ - Ts⁴)

Where:
- ε = Emissivity of panel surface (typically 0.9 for most building materials)
- σ = Stefan-Boltzmann constant (5.67 × 10⁻⁸ W/m²·K⁴)
- Tp = Absolute panel surface temperature (K)
- Ts = Absolute surrounding surface temperature (K)

For practical design, simplified equations based on temperature difference are used. Floor panel output typically ranges from 50-100 W/m² at surface temperatures of 25-29°C. Ceiling panels operate at higher temperatures (30-40°C) and deliver 80-150 W/m². Wall panels fall between these ranges at 60-120 W/m².

Panel area required equals space heat loss divided by panel output per unit area. Account for furniture coverage on floors (typically reduce effective area by 10-20% for residential applications) and ensure adequate coverage for uniform temperature distribution.

## Mean Radiant Temperature

Mean radiant temperature (MRT) represents the uniform temperature of an imaginary enclosure where radiant heat exchange equals that of the actual environment. MRT critically affects occupant thermal comfort and must be calculated accurately for radiant system design.

**MRT Calculation:**

For simple geometries with uniform surface temperatures:

MRT = (T₁·Fp₁ + T₂·Fp₂ + T₃·Fp₃ + ... + Tⁿ·Fpⁿ)

Where:
- Tⁿ = Temperature of surface n (°C)
- Fpⁿ = Angle factor between occupant and surface n

**Angle Factor Determination:**

Angle factors represent the fraction of radiation leaving a point that strikes a particular surface. For a seated person in a typical room, approximate angle factors are:
- Floor: 0.15-0.20
- Ceiling: 0.10-0.15
- Walls: 0.15-0.20 each (varies with room geometry)
- Windows: 0.05-0.15 (depends on glazing area)

For more accurate calculations, use the two-dimensional projection method or computational tools that account for occupant position and orientation.

**Simplified MRT Approximation:**

When surface temperatures are relatively uniform (within 5°C), approximate MRT as the area-weighted average:

MRT ≈ Σ(Aⁿ·Tⁿ) / Σ(Aⁿ)

This method provides acceptable accuracy for preliminary design but underestimates actual MRT impact from nearby warm or cold surfaces.

## Thermal Comfort Criteria

Radiant heating design must satisfy thermal comfort requirements defined by ASHRAE Standard 55. The predicted mean vote (PMV) and predicted percentage dissatisfied (PPD) models guide comfort assessment.

**Operative Temperature:**

Operative temperature (To) combines air temperature and MRT effects:

To = (Ta × hc + MRT × hr) / (hc + hr)

For typical indoor conditions with air velocity below 0.2 m/s:

To ≈ (Ta + MRT) / 2

Target operative temperature ranges for winter heating:
- Sedentary office work: 20-24°C
- Light activity: 18-22°C
- Residential living spaces: 21-23°C

**Surface Temperature Limits:**

ASHRAE Standard 55 and ISO 7730 establish maximum radiant panel surface temperatures to prevent local discomfort:

| Panel Type | Maximum Surface Temperature | Application Notes |
|------------|---------------------------|-------------------|
| Floor - Occupied Zones | 29°C | Continuous occupancy areas |
| Floor - Perimeter Zones | 35°C | Along exterior walls, bathrooms |
| Ceiling Panels | 40°C | Standard occupied spaces |
| Ceiling Panels - Industrial | 50°C | High-bay applications |
| Wall Panels | 40°C | Typical installations |

**Vertical Temperature Gradient:**

Limit vertical air temperature difference between head (1.7 m) and ankle (0.1 m) height to 3°C maximum. Floor heating naturally produces favorable gradients, while ceiling heating requires careful design to avoid excessive stratification.

**Radiant Temperature Asymmetry:**

Limit radiant temperature asymmetry to prevent discomfort:
- Warm ceiling: <5°C difference between ceiling and floor MRT contribution
- Cool wall: <10°C difference (windows, exterior walls)
- Warm wall: <23°C difference
- Cool ceiling: <14°C difference

## Panel Placement Strategy

Panel placement determines thermal distribution uniformity, comfort, and system efficiency. Consider occupancy patterns, furniture layouts, and building envelope characteristics.

**Floor Panel Placement:**

Position floor panels to offset heat losses and create uniform floor temperatures. Concentrate tubing density at exterior walls (150-200 mm spacing) and reduce spacing toward interior zones (250-300 mm). Maintain minimum 150 mm distance from walls and partitions.

Avoid placing tubing under permanent fixtures (kitchen cabinets, bathtubs) where heat output provides no benefit. Account for floor coverings that increase thermal resistance—carpet with padding can reduce output by 30-40% compared to tile or wood.

**Ceiling Panel Placement:**

Install ceiling panels in central occupied areas to maximize radiant exchange with occupants. Avoid placement directly above occupant heads in sedentary workspaces (can cause discomfort). Maintain minimum 1.5 m distance between high-temperature panels and occupant head height.

Ceiling panels work exceptionally well for high-ceilinged spaces where floor heating proves impractical. Position panels to compensate for cold exterior walls and large glazing areas.

**Wall Panel Placement:**

Wall panels suit retrofit applications and spaces where floor/ceiling options are constrained. Install panels on interior walls at occupant height (0.5-2.0 m above floor) for maximum radiant exchange.

Exterior wall placement increases heat loss through the building envelope—only use when necessary for architectural reasons. Ensure furniture placement allows unobstructed radiation to occupied zones.

## Floor vs Ceiling vs Wall Panels

Each panel type offers distinct characteristics affecting design approach, thermal performance, and application suitability.

**Floor Radiant Panels:**

Floor panels provide the most thermally comfortable condition due to warm feet, cool head gradient. Thermal response time ranges from 2-4 hours depending on slab thickness and construction. Maximum output limits (surface temperature constraint) restrict floor heating to well-insulated buildings or supplementary heat applications.

Advantages:
- Superior thermal comfort for occupied spaces
- No visible equipment or noise
- Even heat distribution at occupant level
- Minimal vertical stratification

Limitations:
- Slow thermal response
- Surface temperature limits capacity
- Floor covering impact on performance
- Difficult to modify after installation

**Ceiling Radiant Panels:**

Ceiling panels offer faster response (15-30 minutes for suspended panels) and higher output capacity due to elevated surface temperatures. Ideal for spaces with floor obstructions, high ceilings, or where rapid temperature control is required.

Advantages:
- Rapid thermal response
- Higher heat output per unit area
- No floor space constraints
- Easier access for maintenance

Limitations:
- Head-to-feet temperature gradient reversed
- Potential discomfort if oversized
- Thermal stratification in high spaces
- Visible installation in some configurations

**Wall Radiant Panels:**

Wall panels balance installation flexibility with reasonable thermal performance. Response time falls between floor and ceiling systems (1-2 hours). Output capacity suits moderate heating requirements in retrofit applications.

Advantages:
- Retrofit compatibility
- Moderate response time
- Flexibility in placement
- Acceptable comfort characteristics

Limitations:
- Furniture/obstruction conflicts
- Reduced effective area compared to floor/ceiling
- Aesthetic considerations
- Higher surface temperatures on exterior walls

## Integration with Ventilation Systems

Radiant heating provides sensible heating but no ventilation, humidity control, or cooling. Integration with ventilation systems ensures complete environmental control.

**Design Coordination:**

Coordinate radiant system capacity with ventilation system load contributions. Ventilation air introduces both sensible and latent loads that impact radiant panel requirements. Size radiant panels for envelope losses and infiltration only—ventilation system handles outdoor air loads.

**Temperature Control Integration:**

Implement separate temperature sensors for radiant and ventilation systems. Radiant system responds to operative temperature or floor/ceiling surface temperature. Ventilation system controls air temperature based on space requirements. Coordinate setpoints to prevent system conflict.

**Heating Load Distribution:**

| Load Component | Radiant System | Ventilation System |
|----------------|----------------|-------------------|
| Envelope transmission | Primary | Minimal |
| Infiltration | 50-70% | 30-50% |
| Outdoor air ventilation | 0% | 100% |
| Internal gains | Offset capacity | Active removal |

**Ventilation Air Distribution:**

Design ventilation air distribution to complement radiant panel patterns. Low-velocity displacement ventilation pairs excellently with floor heating. Overhead distribution suits ceiling panel applications. Avoid high-velocity air jets that disrupt radiant temperature distribution or create drafts.

Maintain ventilation air temperature within 2-3°C of space air temperature when radiant panels provide primary heating. This prevents ventilation system from dominating space temperature control.

**Control Sequence Coordination:**

Establish control priority between systems. Radiant system typically provides base load with slow outdoor reset response. Ventilation system offers faster response for transient loads and occupancy variations. Implement deadband between heating and ventilation modes to prevent simultaneous operation.

**Humidity Management:**

Radiant panels cannot control humidity. Ventilation system must provide dehumidification when required. Monitor dew point temperature to prevent condensation on radiant cooling panels (when applicable). Maintain surface temperature at least 1°C above space dew point with appropriate safety factor.

**Energy Recovery Integration:**

Incorporate energy recovery ventilators (ERV) to reduce ventilation heating load. This maximizes radiant system effectiveness by minimizing rapid air temperature swings. Heat recovery efficiency of 60-80% significantly reduces combined system energy consumption.

**Zoning Considerations:**

Align radiant heating zones with ventilation zones where practical. Mismatched zoning creates control conflicts and comfort issues. Radiant zones can be larger than ventilation zones due to slower response time. Minimum radiant zone size depends on building heat loss distribution and control valve authority.

**System Balance:**

Commission both systems together to verify coordinated operation. Measure space temperatures, surface temperatures, and air velocities under various load conditions. Adjust radiant flow rates and ventilation air volumes to achieve design comfort criteria across all operating modes.
