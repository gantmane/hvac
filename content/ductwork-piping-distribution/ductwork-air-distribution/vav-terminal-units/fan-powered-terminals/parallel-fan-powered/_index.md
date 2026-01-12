---
title: "Parallel Fan-Powered VAV Terminals"
description: "Comprehensive technical guide to parallel fan-powered VAV terminal units including operating sequences, fan sizing methodology, heating capacity calculations, energy performance analysis, and design parameters for HVAC professionals"
weight: 2
---

## Operating Principle

Parallel fan-powered VAV terminals incorporate a secondary fan that operates in parallel with primary air delivery, drawing plenum air and mixing it with conditioned primary air. The fan operates intermittently based on thermal demand rather than continuously, distinguishing this configuration from series fan-powered units.

During cooling mode, the terminal operates as a standard VAV box with the fan de-energized. Primary air alone satisfies the cooling load through variable volume delivery. When heating is required, the fan energizes to induce plenum air through the heating coil, mixing this heated air with reduced primary airflow.

## Component Configuration

**Primary Air Inlet**
- Pressure-independent or dependent damper assembly
- Factory-calibrated airflow measurement
- Modulating control for variable volume delivery
- Typically sized for peak cooling airflow

**Induced Air Inlet**
- Backdraft damper preventing reverse flow when fan off
- Plenum air intake during heating operation
- No measurement required (calculated difference)
- Filter optional based on plenum cleanliness

**Secondary Fan Assembly**
- Forward-curved centrifugal fan (typical)
- Intermittent duty operation
- Sized for heating airflow minus minimum primary air
- Static pressure requirement: 0.5-1.0 in. w.g.

**Heating Coil**
- Hot water or electric resistance
- Located downstream of mixed air plenum
- Sized for total heating airflow (primary + induced)
- Control valve or staged electric elements

## Operating Modes and Sequences

### Cooling Mode

Primary air damper modulates from maximum to minimum position based on space temperature. Secondary fan remains de-energized. Heating coil valve closed or electric stages off.

Airflow varies from design maximum to minimum setpoint, typically 30-50% of peak. Space sensible cooling provided entirely by primary air from central air handler.

### Deadband Mode

Primary air damper at minimum position. Secondary fan off. Heating coil inactive. Zone receives minimum ventilation airflow only, relying on thermal mass and internal gains for temperature stability.

This mode minimizes energy consumption during mild conditions when neither active cooling nor heating is required.

### Heating Mode

Primary air damper remains at minimum position to maintain required ventilation. Secondary fan energizes, inducing plenum air through the heating coil. Heating output modulates via valve position or electric staging.

**Total zone airflow** = Minimum primary air + Induced air

The heating coil heats only the induced airflow, which then mixes with minimum primary air before discharge to space.

## Fan Sizing Methodology

### Airflow Calculation

Determine peak heating airflow requirement based on:

Q_heat = (Zone heating load, Btu/hr) / [1.08 × (Supply temp - Space temp)]

Typical supply temperature differential: 20-30°F above space setpoint.

**Fan airflow** = Q_heat - Q_primary,min

Where Q_primary,min is the minimum primary airflow for ventilation.

### Static Pressure Requirements

The secondary fan must overcome:

- Backdraft damper resistance: 0.1-0.2 in. w.g.
- Heating coil pressure drop: 0.2-0.5 in. w.g. (depends on type)
- Downstream ductwork and diffuser losses: 0.1-0.3 in. w.g.
- Safety factor: 10-20%

**Total fan static pressure** typically ranges 0.5-1.0 in. w.g.

### Fan Performance Table

| Zone Airflow (CFM) | Fan Airflow (CFM) | Motor Size (HP) | Power Draw (W) |
|--------------------|-------------------|-----------------|----------------|
| 400 | 250-300 | 1/20 | 75-100 |
| 800 | 500-600 | 1/12 | 125-175 |
| 1200 | 750-900 | 1/8 | 200-275 |
| 2000 | 1250-1500 | 1/6 | 325-425 |

*Values assume minimum primary air ratio of 30-40% and induced air providing balance to heating requirement.*

## Heating Capacity Calculations

### Hot Water Coil Sizing

Q_coil = 500 × GPM × (T_entering - T_leaving)

Or alternatively:

Q_coil = 1.08 × CFM_induced × ΔT_air

Where CFM_induced is the secondary fan airflow through the coil.

**Design parameters:**
- Entering water temperature: 140-180°F (typical 160°F)
- Water temperature drop: 20-40°F
- Air temperature rise: 40-60°F across coil
- Coil face velocity: 400-600 FPM

### Electric Coil Staging

For electric resistance heating:

kW_total = (CFM_induced × ΔT_air × 1.08) / 3413

Staging recommended for capacity control:
- 2-stage: 50/50% or 67/33% splits
- 3-stage: 33/33/33% or 50/25/25% splits
- SCR control: Infinitely variable (higher cost)

## Energy Performance Analysis

### Fan Energy Consumption

Annual fan energy depends critically on heating hours and climate.

**Heating season operation:**

Fan kWh = (Motor input, kW) × (Heating hours per year)

Parallel configuration shows significant energy advantage over series units because the fan operates only during heating, not continuously.

### Comparative Operating Costs

| Configuration | Fan Operating Hours | Annual Fan Energy (kWh)* | Energy Cost** |
|---------------|---------------------|-------------------------|---------------|
| Parallel FPB | 1500-3000 (heating only) | 190-600 | $19-60 |
| Series FPB | 8760 (continuous) | 1100-1800 | $110-180 |
| Standard VAV | 0 | 0 | $0 |

*Based on 0.2 HP fan at 200W average draw
**Assuming $0.10/kWh electricity rate

### Plenum Heat Recovery

Parallel terminals can recover heat from the ceiling plenum, reducing overall building heating energy when:

- Return air routed through plenum
- Lights and equipment reject heat to plenum space
- Plenum temperature exceeds space temperature during heating

This "free" heat offsets heating coil energy but requires proper accounting in building energy models.

## Design Parameters and Guidelines

### Application Criteria

**Best suited for:**
- Perimeter zones requiring significant heating
- Buildings with substantial plenum heat gain
- Applications where fan noise during heating is acceptable
- Retrofit projects with adequate plenum access

**Not recommended for:**
- Zones requiring continuous minimum airflow above 50% of peak
- Critical areas requiring constant air circulation
- Applications with contaminated or unconditioned plenums
- Spaces with strict acoustic requirements

### Control Integration

**Required control points:**
- Primary air damper position (0-100% modulation)
- Secondary fan status (on/off or variable speed)
- Heating valve/stages (0-100% modulation)
- Zone temperature sensor
- Discharge air temperature sensor (optional, for diagnostics)

**Typical control sequence:**

1. Zone temperature > Cooling setpoint: Modulate primary air from minimum to maximum, fan off
2. Cooling setpoint > Zone temp > Heating setpoint: Primary air at minimum, fan off (deadband)
3. Zone temperature < Heating setpoint: Primary air at minimum, fan on, modulate heating

### Sizing Rules of Thumb

| Parameter | Typical Value | Range |
|-----------|---------------|-------|
| Primary air ratio (heating) | 35% | 30-50% |
| Heating supply temp rise | 25°F | 20-30°F |
| Fan static pressure | 0.75 in. w.g. | 0.5-1.0 in. w.g. |
| Hot water coil ΔT_water | 30°F | 20-40°F |
| Coil face velocity | 500 FPM | 400-600 FPM |
| Sound level (fan on) | NC 35-40 | NC 30-45 |

## Advantages and Limitations

### Advantages

**Energy efficiency:** Fan operates intermittently, reducing annual energy consumption by 50-70% compared to series units in typical applications.

**Plenum heat utilization:** Captures ceiling plenum heat that would otherwise be wasted, particularly valuable in buildings with significant lighting loads.

**Lower first cost:** Smaller fan and motor compared to series configuration (no requirement to handle full zone airflow).

**Ventilation compliance:** Maintains minimum primary air during all modes, ensuring continuous outdoor air delivery.

### Limitations

**Variable zone airflow:** Total airflow drops to minimum during cooling, which may cause air distribution issues in some spaces or increased temperature stratification.

**Noise during heating:** Fan activation produces audible transition, potentially disruptive in quiet spaces like private offices or conference rooms.

**Plenum dependence:** Performance degraded if plenum air is cold (top floor zones) or contaminated. Requires clean, accessible plenum space.

**Complexity:** More components than standard VAV boxes increase maintenance requirements and potential failure points.

## Commissioning and Testing

### Factory Testing

Verify prior to shipment:
- Primary air damper stroke and closure
- Fan rotation and airflow direction
- Heating coil pressure test (hydronic)
- Control signal response
- Electrical staging (if electric heat)

### Field Verification

**Airflow measurement:**
1. Set primary damper to maximum, fan off: Measure primary air CFM
2. Set to minimum primary, fan on: Measure total discharge CFM
3. Calculate induced air: Total CFM - Primary minimum CFM
4. Verify against design values (±10% tolerance)

**Heating capacity:**
1. Energize fan and heating to maximum
2. Measure discharge temperature
3. Calculate capacity: Q = 1.08 × CFM × ΔT
4. Compare to design heating load

**Control sequence:**
- Verify smooth transitions between modes
- Check deadband operation
- Confirm heating modulation response
- Test override and emergency sequences

## Maintenance Requirements

**Quarterly:**
- Inspect backdraft damper operation
- Check fan belt tension and condition (if belt-driven)
- Verify damper linkage and actuator function
- Clean or replace filters if provided

**Annual:**
- Lubricate fan bearings
- Inspect heating coil for leaks (hydronic)
- Test control valve operation and calibration
- Verify airflow measurements
- Check electrical connections and contactors

**5-Year:**
- Consider fan motor replacement (depending on operating hours)
- Inspect ductwork connections for air leakage
- Recalibrate airflow sensors if drift detected

Parallel fan-powered terminals offer an energy-efficient solution for zones with significant heating requirements and available plenum heat, balancing performance, cost, and operational flexibility in modern HVAC system design.
