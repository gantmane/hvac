---
title: "Fan Selection"
description: "Systematic approach to HVAC fan selection including system analysis, fan sizing, performance matching, and specification considerations."
keywords: ["fan selection", "fan sizing", "HVAC design", "air handling", "system pressure", "fan specification"]
weight: 4
---

Proper fan selection ensures HVAC systems deliver required airflow efficiently and reliably. This systematic approach covers system analysis, fan sizing, performance matching, and specification development.

## System Analysis

### Airflow Requirements

Determine total system airflow based on:

**Cooling Load Method**:
$$CFM = \frac{Q_{sensible}}{1.08 \times \Delta T}$$

**Ventilation Requirements**:
$$CFM_{OA} = R_p \times P_z + R_a \times A_z$$ (ASHRAE 62.1)

**Air Changes Method**:
$$CFM = \frac{Volume \times ACH}{60}$$

### System Pressure Loss

Calculate total system resistance:

$$\Delta P_{total} = \Delta P_{duct} + \Delta P_{fittings} + \Delta P_{components}$$

**Component Losses**:
| Component | Typical Range |
|-----------|---------------|
| Filters (clean) | 0.25-0.50" w.g. |
| Filters (dirty) | 0.50-1.00" w.g. |
| Cooling coil | 0.40-1.00" w.g. |
| Heating coil | 0.20-0.40" w.g. |
| Dampers | 0.05-0.20" w.g. |
| Sound attenuator | 0.25-0.75" w.g. |

### System Effect Factor

Account for non-ideal fan connections:

$$\Delta P_{actual} = \Delta P_{calculated} + \Delta P_{system\ effect}$$

**System Effect Sources**:
- Sharp inlet elbow
- No inlet duct (plenum inlet)
- Short discharge duct
- Elbow at discharge
- Obstructions near fan

Use AMCA 201 for system effect factors.

## Fan Type Selection

### Application Matching

| Application | Recommended Type | Reason |
|-------------|------------------|--------|
| Central AHU | BC Centrifugal | Efficiency, reliability |
| Packaged RTU | FC Centrifugal | Compact, economical |
| Exhaust systems | Tube/Vane-Axial | High CFM, moderate pressure |
| Material handling | Radial Centrifugal | Particle tolerance |
| Condenser fans | Propeller | High CFM, very low pressure |
| Space-constrained | Mixed-flow | Compact, good pressure |

### Efficiency Priority

For energy-critical applications, prioritize:

1. **Backward-curved airfoil** (80-88% efficiency)
2. **Backward-inclined** (75-82%)
3. **Vane-axial** (70-82%)
4. **Mixed-flow** (70-80%)

### Special Requirements

**High Temperature**:
- Welded steel construction
- High-temperature bearings
- Shaft cooling provisions

**Corrosive Environment**:
- FRP construction
- Coated steel
- Stainless steel

**Explosive Atmosphere**:
- Spark-resistant construction (AMCA A, B, or C)
- Non-sparking materials

## Performance Matching

### Fan Curve Analysis

Steps for proper selection:

1. Calculate required CFM and SP
2. Add safety factor (typically 10% CFM, 20% SP)
3. Plot operating point on candidate fan curves
4. Verify operating point is in stable region
5. Check efficiency at operating point
6. Confirm power requirements

### Selection Criteria

**Optimal Operating Point**:
- 70-80% of peak CFM (typical sweet spot)
- Near peak efficiency
- Right of surge/stall region
- Adequate pressure margin

### Multiple Operating Points

For VAV or variable systems:
- Verify performance at minimum flow
- Check for surge/stall at turndown
- Consider VFD speed range
- Evaluate efficiency across range

## Sizing Calculations

### Fan Static Pressure

$$FSP = TP_{outlet} - TP_{inlet} - VP_{outlet}$$

For draw-through configuration:
$$FSP = \Delta P_{system}$$

For blow-through:
$$FSP = \Delta P_{downstream} + VP_{outlet}$$

### Power Calculation

$$BHP = \frac{CFM \times SP}{6356 \times \eta_{static}}$$

Include drive losses:
- Belt drive: 95-97% efficiency
- Direct drive: 100% (fan shaft = motor shaft)

Motor sizing:
$$HP_{motor} = BHP \times Service\ Factor$$ (SF typically 1.10-1.15)

### Speed Selection

For belt-driven fans:

$$RPM_{fan} = RPM_{motor} \times \frac{D_{motor\ sheave}}{D_{fan\ sheave}}$$

Standard motor speeds: 1,750, 1,450, 1,150, 870 RPM (60 Hz)

## Selection Documentation

### Fan Schedule Information

| Item | Required Data |
|------|---------------|
| Tag | Unique identifier |
| Type | Centrifugal, axial, etc. |
| CFM | Design airflow |
| SP | Static pressure |
| BHP | Calculated brake horsepower |
| Motor HP | Specified motor size |
| RPM | Fan speed |
| Efficiency | At operating point |
| Sound | Sound power levels |
| Arrangement | AMCA arrangement number |
| Class | Construction class |

### AMCA Ratings

Specify AMCA certifications:
- **AMCA 210**: Air performance
- **AMCA 300**: Sound rating
- **AMCA 500**: Damper/louver ratings

### Construction Details

**Arrangement** (AMCA 99-0098):
- Arr. 1: SWSI, bearing on sub-base
- Arr. 3: SWSI, bearing on housing
- Arr. 4: DWDI, bearing on sub-base
- Arr. 8: Direct-drive

**Class** (construction strength):
- Class I: Low speed, low pressure
- Class II: Medium duty
- Class III: High speed, high pressure
- Class IV: Heavy duty

## Selection Example

### Given Requirements

- Airflow: 15,000 CFM
- System SP: 4.0" w.g.
- Application: Central AHU, VAV system
- Priority: Energy efficiency

### Selection Process

1. **Add Safety Factor**:
   - CFM: 15,000 × 1.10 = 16,500 CFM
   - SP: 4.0 × 1.20 = 4.8" w.g.

2. **Select Fan Type**: BC Airfoil for efficiency

3. **Evaluate Options**:
   | Model | RPM | BHP | Efficiency |
   |-------|-----|-----|------------|
   | Fan A | 1,340 | 16.2 | 81% |
   | Fan B | 1,450 | 17.0 | 78% |
   | Fan C | 1,180 | 15.8 | 83% |

4. **Select**: Fan C - highest efficiency, adequate speed margin

5. **Motor Selection**: 20 HP (next standard size above 15.8 × 1.15 = 18.2)

### Verification

- Confirm operating point on curve
- Verify stability at minimum VAV flow (40-50%)
- Check sound power levels
- Confirm motor service factor adequate

Systematic fan selection ensures proper matching between system requirements and fan capabilities, delivering efficient, reliable air distribution throughout the system's operating range.
