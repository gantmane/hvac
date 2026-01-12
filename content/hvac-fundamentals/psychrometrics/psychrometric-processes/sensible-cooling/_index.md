---
title: "Sensible Cooling"
description: "Comprehensive analysis of sensible cooling processes including dry coil operation, heat transfer principles, bypass factors, and apparatus dew point theory for HVAC design."
weight: 2
---

## Overview

Sensible cooling represents a psychrometric process where air temperature decreases without change in moisture content (constant humidity ratio). This occurs when the cooling coil surface temperature remains above the dew point temperature of the entering air stream, preventing condensation. The process follows a horizontal line on the psychrometric chart, moving from right to left at constant specific humidity.

## Fundamental Physics

### Heat Transfer Mechanism

Sensible cooling involves convective heat transfer from the air stream to the coil surface without mass transfer of water vapor. The cooling occurs purely through temperature reduction while maintaining constant absolute humidity.

**Energy Balance:**

```
Q_sensible = ṁ_air × cp_air × (T_entering - T_leaving)
```

Where:
- Q_sensible = sensible cooling capacity (Btu/hr or kW)
- ṁ_air = mass flow rate of air (lb/hr or kg/s)
- cp_air = specific heat of air at constant pressure (0.24 Btu/lb·°F or 1.006 kJ/kg·K)
- T_entering = entering dry-bulb temperature (°F or °C)
- T_leaving = leaving dry-bulb temperature (°F or °C)

**Volumetric Form:**

```
Q_sensible = 1.08 × CFM × ΔT_db  [I-P units]
Q_sensible = 1.23 × L/s × ΔT_db  [SI units]
```

Where:
- CFM = cubic feet per minute of air flow
- L/s = liters per second of air flow
- ΔT_db = dry-bulb temperature difference (°F or °C)

The constant 1.08 derives from: ρ_air × cp_air × 60 min/hr = (0.075 lb/ft³)(0.24 Btu/lb·°F)(60) = 1.08 Btu/min·°F per CFM

### Psychrometric Process Line

On the psychrometric chart, sensible cooling appears as:
- Horizontal line from right to left
- Constant humidity ratio (ω = constant)
- Decreasing dry-bulb temperature
- Decreasing relative humidity (as air cools at constant moisture content)
- Decreasing specific enthalpy

**Enthalpy Change:**

```
Δh = cp_air × ΔT_db
Δh ≈ 0.24 × ΔT_db  [Btu/lb per °F]
```

Since humidity ratio remains constant, the enthalpy change equals the sensible heat change per unit mass.

## Dry Cooling Coil Analysis

### Conditions for Dry Coil Operation

A cooling coil operates in sensible-only mode when:

```
T_coil_surface > T_dewpoint_entering_air
```

The coil surface temperature must exceed the dew point of the entering air to prevent condensation. This condition occurs when:

1. Entering air has low relative humidity
2. Coil operates at elevated water temperatures (economizer mode)
3. Cooling load is predominantly sensible
4. Design intentionally prevents dehumidification

### Apparatus Dew Point (ADP)

The Apparatus Dew Point represents the effective surface temperature of the cooling coil. It is the theoretical saturation temperature at which all air would exit if perfect contact occurred between air and coil surface.

**Definition:**

ADP is the saturation temperature corresponding to the enthalpy and humidity ratio of the leaving air. On the psychrometric chart, ADP lies on the saturation curve.

**For Sensible Cooling:**

When coil operates completely dry:
- ADP > entering air dew point
- No latent cooling occurs
- Process line remains horizontal
- ADP approaches coil surface temperature

**Theoretical ADP Location:**

```
h_ADP = h_leaving_air (at 100% RH)
ω_ADP = ω_entering = ω_leaving (for pure sensible cooling)
```

### Bypass Factor and Contact Factor

#### Bypass Factor (BF)

The Bypass Factor quantifies the fraction of air that passes through the coil without contacting the heat transfer surface, effectively bypassing the cooling process.

**Definition:**

```
BF = (T_leaving - T_ADP) / (T_entering - T_ADP)
```

**Physical Interpretation:**

- BF = 0: Perfect contact, all air reaches ADP temperature
- BF = 1: No contact, no cooling occurs
- Typical range: 0.05 to 0.30 for commercial coils

**Factors Affecting Bypass Factor:**

| Factor | Effect on BF | Explanation |
|--------|--------------|-------------|
| Number of coil rows | Decreases BF | More rows = more contact opportunity |
| Fin spacing | Complex | Optimal spacing balances contact vs. pressure drop |
| Air velocity | Increases BF | Higher velocity = less contact time |
| Coil depth | Decreases BF | Deeper coils provide more surface area |
| Fin configuration | Decreases BF | Enhanced fins improve contact |

**Typical Bypass Factors:**

| Coil Configuration | Bypass Factor | Contact Factor |
|--------------------|---------------|----------------|
| 2-row coil, 10 FPI | 0.30 - 0.40 | 0.60 - 0.70 |
| 4-row coil, 10 FPI | 0.15 - 0.25 | 0.75 - 0.85 |
| 6-row coil, 12 FPI | 0.08 - 0.15 | 0.85 - 0.92 |
| 8-row coil, 14 FPI | 0.05 - 0.10 | 0.90 - 0.95 |

FPI = Fins per inch

#### Contact Factor (CF)

The Contact Factor represents the effectiveness of air-to-coil surface contact:

```
CF = 1 - BF = (T_entering - T_leaving) / (T_entering - T_ADP)
```

Contact factor indicates the fraction of air that effectively contacts the coil surface and undergoes the full cooling process.

### Coil Heat Transfer Analysis

#### Overall Heat Transfer

**Heat Transfer Equation:**

```
Q = U × A × LMTD
```

Where:
- U = overall heat transfer coefficient (Btu/hr·ft²·°F or W/m²·K)
- A = effective heat transfer surface area (ft² or m²)
- LMTD = log mean temperature difference (°F or °C)

**Log Mean Temperature Difference:**

```
LMTD = (ΔT₁ - ΔT₂) / ln(ΔT₁/ΔT₂)
```

Where:
- ΔT₁ = T_air_entering - T_water_leaving (counterflow)
- ΔT₂ = T_air_leaving - T_water_entering

For sensible cooling with dry coil:
- Air-side: T_entering → T_leaving
- Water-side: T_in → T_out
- Configuration typically counterflow for maximum efficiency

#### Overall Heat Transfer Coefficient

**Composite Resistance:**

```
1/U = 1/h_air + t_tube/k_tube + R_fouling + 1/h_water
```

Where:
- h_air = air-side convection coefficient (5-15 Btu/hr·ft²·°F)
- h_water = water-side convection coefficient (200-800 Btu/hr·ft²·°F)
- t_tube = tube wall thickness
- k_tube = tube thermal conductivity
- R_fouling = fouling resistance factor

**Typical U-Values for Dry Coils:**

| Coil Type | U-value (Btu/hr·ft²·°F) | U-value (W/m²·K) |
|-----------|------------------------|------------------|
| Standard finned tube | 20 - 30 | 110 - 170 |
| Enhanced fin | 30 - 40 | 170 - 225 |
| Microchannel | 40 - 50 | 225 - 280 |

The air-side resistance dominates in sensible cooling applications, representing 75-85% of total thermal resistance.

## Design Calculations

### Sensible Cooling Load Determination

**Step 1: Calculate Air Temperature Change**

```
ΔT = Q_sensible / (1.08 × CFM)  [I-P units]
```

**Step 2: Determine Leaving Air Temperature**

```
T_leaving = T_entering - ΔT
```

**Step 3: Verify Dry Coil Operation**

```
Check: T_leaving > T_dewpoint_entering
```

If leaving temperature exceeds entering dew point, coil operates dry with pure sensible cooling.

**Step 4: Calculate Required Coil Capacity**

```
Q_coil = Q_sensible / CF
```

The coil must be sized larger than the required load to account for bypass factor.

### Example Calculation: Sensible Cooling Process

**Given:**
- Air flow rate: 5,000 CFM
- Entering conditions: 85°F DB, 60°F WB (ω = 0.0092 lb_w/lb_da)
- Required sensible cooling: 60,000 Btu/hr
- Coil bypass factor: 0.20 (4-row coil)

**Solution:**

**Temperature drop required:**
```
ΔT = Q / (1.08 × CFM)
ΔT = 60,000 / (1.08 × 5,000) = 11.1°F
```

**Leaving air temperature:**
```
T_leaving = 85 - 11.1 = 73.9°F
```

**Check for dry coil operation:**
- Entering dew point: 60°F (from psychrometric chart at 85°F DB, 60°F WB)
- Leaving temperature: 73.9°F
- Since 73.9°F > 60°F, coil operates dry (sensible cooling only)

**Apparatus Dew Point:**
```
BF = (T_leaving - T_ADP) / (T_entering - T_ADP)
0.20 = (73.9 - T_ADP) / (85 - T_ADP)
0.20 × (85 - T_ADP) = 73.9 - T_ADP
17 - 0.20 × T_ADP = 73.9 - T_ADP
0.80 × T_ADP = 56.9
T_ADP = 71.1°F
```

**Verification:**
- ADP = 71.1°F > entering dew point (60°F)
- Confirms dry coil operation
- Process line horizontal on psychrometric chart

**Leaving air properties:**
- Dry-bulb: 73.9°F
- Humidity ratio: 0.0092 lb_w/lb_da (unchanged)
- Relative humidity: approximately 52% (increased from entering ~41%)

### Coil Selection Procedure

**1. Define Air-Side Parameters:**
- Entering/leaving temperatures
- Air flow rate (CFM or L/s)
- Maximum allowable pressure drop

**2. Calculate Heat Transfer Requirements:**
- Sensible capacity (Btu/hr or kW)
- Required effectiveness
- Temperature approach

**3. Determine Water-Side Conditions:**
- Entering water temperature (EWT)
- Water flow rate (GPM or L/s)
- Allowable water temperature rise

**4. Select Coil Configuration:**
- Number of rows (affects BF)
- Fin spacing (FPI or fins/cm)
- Face area (controls velocity)
- Tube arrangement

**5. Verify Performance:**
- Air-side pressure drop < limit
- Water-side pressure drop < limit
- Leaving air temperature achieved
- Dry coil operation confirmed

## Design Considerations

### Air Velocity and Face Velocity

**Face Velocity:**

```
V_face = CFM / A_face  [ft/min]
```

**Recommended Face Velocities (Sensible Cooling):**

| Application | Face Velocity (FPM) | Face Velocity (m/s) |
|-------------|---------------------|---------------------|
| Low velocity systems | 300 - 400 | 1.5 - 2.0 |
| Standard comfort | 400 - 550 | 2.0 - 2.8 |
| High velocity systems | 550 - 700 | 2.8 - 3.6 |
| Industrial applications | 700 - 900 | 3.6 - 4.6 |

Higher velocities increase heat transfer coefficient but also increase pressure drop and bypass factor.

### Air-Side Pressure Drop

**Pressure Drop Estimation:**

```
ΔP_air = K × ρ × V² / (2 × gc)
```

**Typical Pressure Drops (Dry Coils):**

| Coil Depth | Pressure Drop (in. wg) | Pressure Drop (Pa) |
|------------|------------------------|-------------------|
| 2 rows | 0.15 - 0.25 | 37 - 62 |
| 4 rows | 0.25 - 0.40 | 62 - 100 |
| 6 rows | 0.35 - 0.55 | 87 - 137 |
| 8 rows | 0.45 - 0.70 | 112 - 174 |

Pressure drop for dry coils is significantly lower than wet coils due to absence of condensate film on surfaces.

### Water-Side Design

**Water Flow Rate:**

```
GPM = Q_sensible / (500 × ΔT_water)  [I-P units]
```

Where 500 = ρ_water × cp_water × 60 min/hr = (8.33 lb/gal)(1.0 Btu/lb·°F)(60)

**Typical Water Temperature Rise:**
- Chilled water systems: 10-20°F (5.6-11°C)
- Process cooling: 5-15°F (2.8-8.3°C)

**Water Velocity in Tubes:**

Maintain 2-8 ft/s (0.6-2.4 m/s) to ensure:
- Adequate turbulence (Re > 3,000)
- Prevention of fouling
- Acceptable pressure drop
- Erosion prevention (V < 8 ft/s)

### Freeze Protection

Even for sensible cooling applications, freeze protection remains critical:

**Minimum Coil Surface Temperature:**

Maintain coil surface temperature > 35°F (1.7°C) to prevent:
- Ice formation in tubes
- Tube rupture from expansion
- System damage during off-cycles

**Protection Methods:**
1. Glycol solutions (20-40% ethylene or propylene glycol)
2. Temperature-actuated control valves
3. Pump-through protection during cold weather
4. Low-limit thermostats with safety shutdown

## Operating Characteristics

### Part-Load Performance

At reduced loads, sensible cooling systems exhibit:

**Temperature Control:**
- Linear relationship between load and temperature drop
- Excellent control stability
- Wide turndown capability

**Bypass Factor Variation:**
- BF remains relatively constant across load range
- Minor variation due to air density changes
- Contact factor essentially unchanged

**Energy Efficiency:**
- Sensible cooling more efficient than cooling with dehumidification
- Lower refrigeration lift required
- Reduced compressor power consumption

### Economizer Integration

Sensible cooling coils work effectively with airside economizers:

**Free Cooling Modes:**
1. **Full economizer:** 100% outdoor air when T_outdoor < T_return - 5°F
2. **Partial economizer:** Mixed air provides required leaving temperature
3. **Mechanical cooling:** Coil supplements or replaces economizer

**Economizer Operation:**

When outdoor conditions permit:
```
T_mixed = (CFM_OA × T_OA + CFM_RA × T_RA) / CFM_total
```

If T_mixed achieves required leaving temperature, no mechanical cooling required.

### Humidity Control Implications

Sensible-only cooling increases relative humidity as air temperature decreases:

**Relative Humidity Change:**

For constant humidity ratio:
- As T decreases → RH increases
- Air approaches saturation without adding moisture
- Critical in applications requiring humidity control

**Maximum Sensible Cooling:**

Limited by maximum acceptable RH at leaving conditions:
```
Cool until: RH_leaving = RH_limit (typically 65-70%)
```

Beyond this point, dehumidification becomes necessary even if additional sensible cooling is required.

## ASHRAE Standards and References

### ASHRAE Standard 33

**Standard 33-2016: Methods of Testing Forced Circulation Air Cooling and Air Heating Coils**

Defines standardized test procedures for:
- Entering air conditions
- Water flow rates
- Performance measurements
- Sensible capacity ratings

### ASHRAE Handbook - HVAC Systems and Equipment

**Chapter 23: Air-to-Air Energy Recovery Equipment**
**Chapter 27: Coils for Dehumidifying and Cooling**

Key guidance for sensible cooling:
- Coil selection procedures
- Heat transfer correlations
- Performance prediction methods
- Bypass factor determination

### Design Guidelines

**ASHRAE Handbook - Fundamentals:**

- **Chapter 1:** Psychrometric principles for sensible processes
- **Chapter 26:** Heat transfer fundamentals for coil analysis
- **Chapter 27:** Pressure drop calculations

**Recommended Practices:**

1. Maintain face velocity < 550 FPM for low noise
2. Size coils for 85% contact factor minimum
3. Design water velocity 3-6 ft/s for optimal performance
4. Include 15% safety factor for coil capacity
5. Verify dry operation across expected operating range

## Applications

### Data Centers and IT Facilities

Sensible cooling predominates due to:
- High sensible heat ratio (SHR > 0.95)
- Minimal latent loads
- Equipment heat generation
- Envelope design minimizes infiltration

**Typical Conditions:**
- Entering: 80°F DB, low RH
- Leaving: 65-70°F DB
- Supply air: 55-60°F DB (higher than conventional comfort cooling)

### Industrial Process Cooling

Applications requiring temperature reduction without moisture removal:

**Process Requirements:**
- Electronic assembly (prevent static from low RH)
- Food storage (certain products require specific humidity)
- Textile manufacturing (controlled moisture content)
- Pharmaceutical clean rooms (humidity-sensitive processes)

### Economizer Cooling

High-efficiency cooling using outdoor air:

**Operating Sequence:**
1. Outdoor air < 55°F: direct evaporative or sensible economizer
2. Outdoor air 55-70°F: sensible cooling with economizer assist
3. Outdoor air > 70°F: mechanical cooling with minimum outdoor air

### Laboratory and Vivarium Facilities

100% outdoor air systems with high sensible loads:

**Design Characteristics:**
- No recirculation (code requirement)
- Large air quantities
- Predominantly sensible cooling
- Energy recovery to reduce load

## Best Practices

### Design Phase

1. **Accurate Load Calculation:**
   - Separate sensible and latent components
   - Verify SHR > 0.95 for pure sensible cooling
   - Account for all sensible heat sources

2. **Coil Selection:**
   - Select adequate rows for low bypass factor
   - Verify dry operation at all expected conditions
   - Size for future load growth

3. **Control Strategy:**
   - Use discharge air temperature control
   - Implement water flow modulation or valve control
   - Consider VFD control for optimal part-load efficiency

### Installation

1. **Proper Coil Orientation:**
   - Ensure correct airflow direction
   - Verify counterflow water/air arrangement
   - Check for proper header alignment

2. **Piping Connections:**
   - Install isolation valves for maintenance
   - Provide thermometer wells for verification
   - Include pressure gauges for diagnostics

3. **Instrumentation:**
   - Temperature sensors at entering/leaving positions
   - Differential pressure measurement across coil
   - Water flow indication

### Commissioning

**Verification Tests:**

1. **Air-Side Performance:**
   - Measure entering/leaving dry-bulb temperatures
   - Verify air flow rate (CFM)
   - Check pressure drop across coil
   - Confirm horizontal psychrometric process

2. **Water-Side Performance:**
   - Measure entering/leaving water temperatures
   - Verify water flow rate (GPM)
   - Calculate heat transfer effectiveness
   - Check for proper flow distribution

3. **Control Verification:**
   - Test temperature setpoint control
   - Verify valve operation and authority
   - Confirm freeze protection interlocks
   - Test economizer integration

### Maintenance

**Routine Procedures:**

1. **Quarterly Inspection:**
   - Clean air filters (reduces pressure drop)
   - Inspect fins for damage or blockage
   - Check for signs of water leakage
   - Verify control operation

2. **Annual Maintenance:**
   - Chemical cleaning of water side (if fouled)
   - Straighten damaged fins
   - Verify calibration of sensors
   - Test safety controls

3. **Performance Monitoring:**
   - Track temperature differences
   - Monitor pressure drops (indicate fouling)
   - Trending capacity over time
   - Energy consumption analysis

## Troubleshooting

### Common Issues

**Insufficient Cooling Capacity:**

**Symptoms:**
- Leaving air temperature higher than design
- Unable to meet setpoint

**Causes and Solutions:**

| Cause | Diagnostic | Solution |
|-------|-----------|----------|
| Reduced air flow | Measure ΔP, CFM | Clean/replace filters, check fan |
| Fouled coil | Visual inspection | Clean fins, chemical treatment |
| Low water flow | Check GPM, ΔT_water | Clear strainers, check pump |
| High water temperature | Measure EWT | Verify chiller operation |
| Excessive bypass | Calculate BF from temps | Check for air bypass around coil |

**Excessive Pressure Drop:**

**Symptoms:**
- ΔP > design value
- Reduced air flow
- Increased fan power

**Solutions:**
- Clean coil surfaces
- Straighten collapsed fins
- Remove obstructions
- Verify correct coil installation

**Control Instability:**

**Symptoms:**
- Temperature hunting
- Cycling operation

**Solutions:**
- Tune PID control parameters
- Increase sensor time constant
- Verify valve sizing and authority
- Check for adequate control range

## Performance Optimization

### Energy Efficiency Measures

1. **Increase Leaving Air Temperature:**
   - Raise setpoint to 65-68°F (from 55°F)
   - Reduces refrigeration load
   - Maintains comfort with proper air distribution

2. **Maximize Economizer Hours:**
   - Use sensible cooling with outdoor air when possible
   - Integrate with mechanical cooling
   - Implement demand-based control

3. **Variable Flow Operation:**
   - Vary water flow with load
   - Reduce pump energy
   - Maintain minimum velocity to prevent fouling

4. **Optimize Air Distribution:**
   - Design for higher temperature differentials
   - Reduce air flow rates (lower fan energy)
   - Improve space temperature stratification

### Advanced Control Strategies

**Reset Strategies:**

1. **Supply Air Temperature Reset:**
   ```
   T_supply = T_base + K × (T_outdoor - T_outdoor_base)
   ```
   - Increase leaving air temperature as outdoor temperature decreases
   - Reduces cooling load and mechanical refrigeration

2. **Water Temperature Reset:**
   - Increase CHW supply temperature at part load
   - Improves chiller efficiency
   - Reduces distribution pumping energy

**Predictive Control:**
- Anticipate load changes
- Pre-cool during off-peak periods
- Minimize peak demand charges

## Conclusion

Sensible cooling represents a fundamental psychrometric process in HVAC systems, characterized by temperature reduction at constant humidity ratio. Understanding the physics of heat transfer, bypass factor relationships, and apparatus dew point theory enables proper coil selection and system design.

Key design principles:
- Verify dry coil operation throughout operating range
- Select appropriate bypass factor for application requirements
- Optimize face velocity for pressure drop and heat transfer
- Integrate economizer operation for energy efficiency
- Implement proper control strategies for stable operation

Sensible cooling offers superior energy efficiency compared to cooling with dehumidification, making it ideal for high sensible heat ratio applications such as data centers, industrial processes, and economizer-based systems.

Proper application of sensible cooling principles, combined with accurate load calculations and appropriate coil selection, ensures reliable, efficient, and cost-effective HVAC system operation.
