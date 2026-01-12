---
title: "Sensible Heating"
description: "Comprehensive analysis of sensible heating processes in HVAC systems including thermodynamic principles, heating coil design, heat transfer calculations, and psychrometric analysis for air conditioning applications"
weight: 1
---

## Technical Overview

Sensible heating represents a psychrometric process where thermal energy is added to air without changing its moisture content. The process increases dry-bulb temperature while maintaining constant absolute humidity ratio, resulting in a horizontal line movement to the right on the psychrometric chart. This fundamental HVAC process occurs in heating coils, electric resistance heaters, and other air heating equipment.

The term "sensible" refers to heat that causes a temperature change measurable by a thermometer, distinguishing it from latent heat associated with phase changes of water vapor. In practical HVAC systems, sensible heating is the primary winter conditioning process and a component of year-round air handling operations.

## Thermodynamic Principles

### Energy Conservation

The First Law of Thermodynamics governs sensible heating processes. For a steady-flow open system with negligible kinetic and potential energy changes:

**Energy Balance Equation:**
```
Q̇ = ṁ × cp × (T₂ - T₁)
```

Where:
- Q̇ = sensible heating rate, Btu/hr or kW
- ṁ = mass flow rate of air, lbm/hr or kg/s
- cp = specific heat of air at constant pressure, Btu/(lbm·°F) or kJ/(kg·K)
- T₂ = leaving air temperature, °F or °C
- T₁ = entering air temperature, °F or °C

**Volumetric Flow Rate Form:**
```
Q̇ = Q × ρ × cp × ΔT
```

Where:
- Q = volumetric flow rate, CFM or m³/s
- ρ = air density, lbm/ft³ or kg/m³
- ΔT = temperature rise, °F or °C

**Standard Air Approximation (IP Units):**
```
Q̇ = 1.08 × CFM × ΔT
```

Where 1.08 = 60 min/hr × 0.075 lbm/ft³ × 0.24 Btu/(lbm·°F)

**Standard Air Approximation (SI Units):**
```
Q̇ = 1.2 × L/s × ΔT
```

Where 1.2 = 1.2 kg/m³ × 1.0 kJ/(kg·K)

### Psychrometric Properties

During sensible heating, specific psychrometric properties change while others remain constant:

**Constant Properties:**
- Absolute humidity ratio (W)
- Dew point temperature (Tdp)
- Vapor pressure (Pv)

**Changing Properties:**
- Dry-bulb temperature (increases)
- Relative humidity (decreases)
- Specific enthalpy (increases)
- Specific volume (increases slightly)
- Wet-bulb temperature (increases)

**Enthalpy Change:**
```
Δh = cp × ΔT
```

For standard air:
```
Δh ≈ 0.24 × ΔT (Btu/lbm dry air)
Δh ≈ 1.0 × ΔT (kJ/kg dry air)
```

**Relative Humidity Relationship:**

As air is heated at constant humidity ratio, relative humidity decreases according to:

```
RH₂/RH₁ = (Pws₁/Pws₂)
```

Where Pws = saturation vapor pressure at the respective dry-bulb temperature.

## Heating Coil Design and Calculations

### Heat Transfer Fundamentals

Heating coils transfer thermal energy from a heating medium (hot water, steam, electric resistance) to air through convection. The governing equation is:

**Overall Heat Transfer:**
```
Q̇ = U × A × LMTD
```

Where:
- U = overall heat transfer coefficient, Btu/(hr·ft²·°F) or W/(m²·K)
- A = coil face area or heat transfer surface area, ft² or m²
- LMTD = log mean temperature difference, °F or °C

**Log Mean Temperature Difference:**
```
LMTD = (ΔT₁ - ΔT₂) / ln(ΔT₁/ΔT₂)
```

For counterflow arrangement:
- ΔT₁ = entering water temperature - leaving air temperature
- ΔT₂ = leaving water temperature - entering air temperature

### Coil Selection Parameters

| Parameter | Typical Range | Notes |
|-----------|---------------|-------|
| Face velocity | 300-800 fpm | 400-600 fpm optimal for low pressure drop |
| Coil depth | 2-8 rows | More rows increase capacity and pressure drop |
| Fin spacing | 8-14 fins/inch | Closer spacing increases surface area |
| Water velocity | 2-8 fps | 3-5 fps recommended to prevent erosion |
| Entering water temp | 140-200°F | Based on heating medium and application |
| Water temp drop | 10-40°F | 20°F typical design value |
| Air pressure drop | 0.2-1.0 in. w.g. | Function of face velocity and rows |

### Hot Water Heating Coil Calculations

**Water-Side Energy Balance:**
```
Q̇ = ṁw × cpw × (Tw,in - Tw,out)
Q̇ = 500 × GPM × ΔTw (simplified, IP units)
```

Where:
- ṁw = water mass flow rate, lbm/hr
- cpw = specific heat of water ≈ 1.0 Btu/(lbm·°F)
- GPM = water flow rate, gallons per minute
- ΔTw = water temperature drop, °F
- 500 = 60 min/hr × 8.33 lbm/gal

**Required Water Flow Rate:**
```
GPM = Q̇ / (500 × ΔTw)
```

**Coil Heat Transfer Effectiveness:**
```
ε = (Ta,out - Ta,in) / (Tw,in - Ta,in)
```

### Steam Heating Coil Calculations

Steam coils operate on latent heat of condensation, providing high heat transfer rates in compact configurations.

**Steam Consumption:**
```
ṁs = Q̇ / hfg
```

Where:
- ṁs = steam mass flow rate, lbm/hr or kg/hr
- hfg = latent heat of vaporization, Btu/lbm or kJ/kg

For saturated steam at 5 psig: hfg ≈ 960 Btu/lbm

**Condensate Load:**
```
Condensate (lbm/hr) = Q̇ (Btu/hr) / 960 Btu/lbm
```

### Electric Resistance Heating

Electric heating coils convert electrical energy directly to thermal energy with near 100% efficiency at the point of use.

**Electrical Power:**
```
Q̇ (Btu/hr) = 3.412 × kW
Q̇ (kW) = V × I × √3 × PF / 1000 (three-phase)
Q̇ (kW) = V × I / 1000 (single-phase)
```

Where:
- V = voltage, volts
- I = current, amperes
- PF = power factor (≈1.0 for resistance heating)

**Element Sizing:**
```
kW required = CFM × ΔT / 3,412
```

| Heating Element Type | Typical kW Density | Application |
|----------------------|-------------------|-------------|
| Open coil | 10-25 W/in² | Light duty, low temperature |
| Finned tubular | 25-40 W/in² | Standard HVAC applications |
| Serpentine | 15-30 W/in² | Uniform heat distribution |

## Psychrometric Chart Analysis

### Process Line Characteristics

On the psychrometric chart, sensible heating appears as:

- **Direction:** Horizontal line moving right (increasing temperature)
- **Slope:** Zero slope (constant humidity ratio)
- **End Points:** State 1 (entering conditions) to State 2 (leaving conditions)

**Graphical Determination:**

1. Locate entering air state point (T₁, RH₁)
2. Move horizontally to the right to desired leaving temperature T₂
3. Read final relative humidity RH₂ (will be lower than RH₁)
4. Calculate enthalpy change from chart scales

### Sensible Heat Ratio

For processes involving only sensible heating:

```
SHR = Sensible Heat / Total Heat = 1.0
```

This distinguishes pure sensible heating from combined sensible and latent processes.

## Design Considerations

### Coil Freeze Protection

Hot water heating coils require protection from freezing when exposed to cold air:

**Prevention Methods:**

1. **Face and Bypass Dampers:** Blend cold outdoor air with warm return air before coil
2. **Preheat Coils:** Steam or electric preheat upstream of water coils
3. **Glycol Solutions:** Use propylene glycol/water mixtures (reduces heat transfer)
4. **Minimum Flow Interlocks:** Ensure water circulation whenever fans operate
5. **Low Temperature Cutouts:** Shut down fans if discharge air drops below setpoint

**Freeze Protection Temperatures:**

| Coil Type | Minimum Discharge Temp | Action |
|-----------|------------------------|--------|
| Hot water, no glycol | 40°F | Shutdown and alarm |
| 30% propylene glycol | 25°F | Shutdown and alarm |
| Steam or electric | N/A | No freeze risk |

### Control Strategies

**Hot Water Coil Control:**

1. **Two-Way Valve Modulation:** Varies water flow rate, maintains system ΔT
2. **Three-Way Valve Mixing:** Blends supply and return water, constant flow
3. **On/Off Control:** Simple applications, cycling increases wear

**Control Sequences:**

- Preheat coils: Typically controlled to maintain minimum mixed air or discharge temperature
- Reheat coils: Modulate to maintain space temperature or humidity control
- Freeze protection: Override normal control for safety

### Stratification Prevention

Sensible heating can create temperature stratification in supply ducts:

**Causes:**
- Low face velocity through coil
- Inadequate mixing downstream of coil
- Long duct runs with insufficient turbulence

**Solutions:**
- Maintain minimum face velocity 400 fpm
- Install mixing devices downstream of heating coils
- Locate coils close to air distribution points
- Use VAV systems with proper duct design

## Application-Specific Considerations

### Preheat Coils

Located upstream of main air handling equipment to temper cold outdoor air:

**Typical Requirements:**
- Entering air: -20°F to 40°F (design outdoor air temperature)
- Leaving air: 40°F to 50°F (freeze protection for downstream coils)
- Steam preferred over hot water for reliability
- Face velocity: 400-600 fpm
- Often oversized for rapid warm-up

**Capacity Calculation:**
```
Q̇preheat = 1.08 × CFM × (Tleaving - Tdesign OA)
```

### Reheat Coils

Provide zone-level temperature control and humidity management:

**Functions:**
- Terminal reheat in VAV systems
- Dehumidification system reheat
- Perimeter zone heating

**Design Parameters:**
- Smaller capacity than preheat coils
- Located at terminal units or zone level
- Hot water, steam, or electric
- Face velocity: 300-500 fpm

**Energy Considerations:**

Simultaneous cooling and reheat is energy-intensive. ASHRAE Standard 90.1 limits reheat applications:
- Exception for humidity control
- Exception for special processes or health/safety
- DDC VAV systems with specific sequence requirements

## Performance Calculations Examples

### Example 1: Hot Water Heating Coil

**Given:**
- Air flow rate: 10,000 CFM
- Entering air: 55°F
- Leaving air: 95°F
- Entering water temperature: 180°F
- Water temperature drop: 20°F

**Calculate:**
1. Heating capacity
2. Required water flow rate

**Solution:**

```
Q̇ = 1.08 × CFM × ΔT
Q̇ = 1.08 × 10,000 × (95 - 55)
Q̇ = 432,000 Btu/hr

GPM = Q̇ / (500 × ΔTw)
GPM = 432,000 / (500 × 20)
GPM = 43.2 GPM
```

### Example 2: Electric Heating Element

**Given:**
- Air flow rate: 2,000 CFM
- Temperature rise: 30°F

**Calculate:** Required electric heater kW

**Solution:**

```
kW = CFM × ΔT / 3,412
kW = 2,000 × 30 / 3,412
kW = 17.6 kW

Round up to standard size: 18 kW or 20 kW
```

### Example 3: Steam Coil Condensate

**Given:**
- Heating load: 500,000 Btu/hr
- Steam pressure: 5 psig (hfg = 960 Btu/lbm)

**Calculate:** Condensate load

**Solution:**

```
Condensate = Q̇ / hfg
Condensate = 500,000 / 960
Condensate = 521 lbm/hr
Condensate = 1.04 GPM (at 8.33 lbm/gal)
```

## ASHRAE References and Standards

**ASHRAE Handbook - HVAC Systems and Equipment:**
- Chapter on air-to-air energy recovery
- Heating coil selection and performance data

**ASHRAE Handbook - Fundamentals:**
- Chapter 1: Psychrometrics
- Chapter 4: Heat Transfer
- Chapter 33: Physical Properties of Materials (specific heat data)

**ASHRAE Standard 90.1:**
- Section 6.5.2.2: Simultaneous heating and cooling limitation
- Section 6.5.3.3: Zone controls for reheat systems

**ASHRAE Standard 62.1:**
- Ventilation requirements affecting preheat capacity
- Outdoor air intake considerations

**Air-Conditioning, Heating, and Refrigeration Institute (AHRI):**
- AHRI Standard 410: Forced-Circulation Air-Cooling and Air-Heating Coils
- Performance rating procedures
- Testing methods for coil capacity

## Design Best Practices

### Coil Selection

1. **Size for Design Conditions:** Use 99% or 99.6% winter design temperatures per ASHRAE climate data
2. **Include Safety Factor:** 10-15% capacity margin for non-standard conditions
3. **Verify Pressure Drop:** Ensure fan can overcome coil resistance at design flow
4. **Access for Maintenance:** Provide service clearance for cleaning and valve service
5. **Proper Orientation:** Install coils with condensate drain provisions even for heating

### Piping and Connections

**Hot Water Systems:**
- Reverse return piping for multiple coils
- Air elimination at high points
- Isolation valves for maintenance
- Balancing valves for design flow rates
- Pressure/temperature test ports

**Steam Systems:**
- Pitch condensate lines for gravity drainage
- Steam trap selection based on load and pressure
- Vacuum breakers to prevent coil collapse
- Strainers upstream of control valves

### Control Valve Sizing

**Valve Authority:**
```
N = ΔPvalve / (ΔPvalve + ΔPcoil)
```

Target valve authority: 0.3 to 0.5

**Cv Calculation:**
```
Cv = GPM × √(SG / ΔP)
```

Where:
- SG = specific gravity (1.0 for water)
- ΔP = pressure drop across valve at design flow, psi

Select valve with Cv at 70-80% of maximum flow to ensure good control range.

### Energy Efficiency Strategies

1. **Heat Recovery:** Use energy recovery ventilators to reduce preheat loads
2. **Economizer Operation:** Maximize free heating from outdoor air when available
3. **Reset Schedules:** Lower discharge air temperature setpoints based on outdoor conditions
4. **Variable Flow:** Use two-way valves with variable speed pumps
5. **Minimize Reheat:** Design for reduced simultaneous heating and cooling

## Troubleshooting Common Issues

| Problem | Possible Causes | Diagnostic Steps |
|---------|-----------------|------------------|
| Insufficient heating capacity | Fouled coil surfaces | Measure air pressure drop, inspect coil |
|  | Low water temperature | Verify supply temperature at coil |
|  | Inadequate water flow | Check flow rate, valve position |
|  | Air flow rate too high | Measure CFM, verify fan operation |
| Uneven heating | Stratified air distribution | Check face velocity uniformity |
|  | Partial coil blockage | Inspect for debris, collapsed fins |
|  | Air bypass around coil | Verify coil gaskets and seals |
| Coil freeze damage | Control failure during cold weather | Test low limit controls |
|  | Water flow loss | Verify pump operation, check for closed valves |
|  | Inadequate preheat | Review face/bypass damper operation |
| High energy consumption | Excessive outdoor air | Verify damper minimum positions |
|  | Simultaneous heating/cooling | Analyze system operation sequences |
|  | Poor insulation | Inspect ductwork and equipment |

## Related Psychrometric Processes

Sensible heating is often combined with other processes in complete air conditioning systems:

- **Sensible Cooling:** Opposite process, horizontal line moving left on chart
- **Humidification:** Combined with heating for winter comfort conditioning
- **Mixing:** Outdoor and return air mixing before preheat coil
- **Adiabatic Processes:** Follow-on evaporative cooling after heating

Understanding the interaction between sensible heating and other psychrometric processes is essential for proper HVAC system design and operation.

