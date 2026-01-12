---
title: "Pressure-Dependent VAV Terminal Units"
description: "Comprehensive technical analysis of pressure-dependent VAV terminal units including operating characteristics, control limitations, static pressure effects, and comparison with pressure-independent systems for HVAC professionals"
weight: 2
---

## Operating Principle

Pressure-dependent VAV terminal units represent the simplest form of variable air volume control, utilizing only a modulating damper actuated by a zone thermostat. Airflow through the unit varies as a function of both damper position and upstream static pressure according to the fundamental relationship:

Q = K × √(ΔP)

Where:
- Q = volumetric airflow rate (CFM)
- K = flow coefficient (varies with damper position)
- ΔP = pressure differential across damper (in. w.g.)

The absence of airflow measurement or flow control mechanisms means the terminal cannot maintain constant airflow independent of system pressure fluctuations.

## System Configuration

### Basic Components

**Damper Assembly:**
- Single-blade or multi-blade opposed-blade damper
- 0-10 VDC or 2-10 VDC modulating control signal
- Spring return or fail-safe positioning

**Actuator:**
- Electric modulating actuator (typically 24 VAC)
- Proportional control responding to thermostat signal
- 2-5 minute stroke time for stability

**Sensing and Control:**
- Zone thermostat provides control signal
- No airflow measurement device
- Direct damper modulation based on temperature deviation

### Inlet Configuration

Pressure-dependent terminals are available in standard inlet configurations:
- Round connections: 4" through 24" diameter
- Rectangular connections: up to 2000 CFM capacity
- Standard upstream straight duct requirement: 3-5 diameters minimum

## Performance Characteristics

### Pressure Sensitivity

The fundamental limitation of pressure-dependent terminals is the direct relationship between airflow and static pressure. As duct static pressure varies due to system loading changes, airflow at each terminal changes proportionally.

| Static Pressure Change | Approximate Airflow Change | System Impact |
|------------------------|----------------------------|---------------|
| +25% | +12% | Zone overcooling/overheating |
| +50% | +22% | Significant comfort degradation |
| +100% | +41% | Severe control problems |
| -25% | -13% | Insufficient capacity |
| -50% | -29% | Poor load satisfaction |

### Flow Characteristics

The flow response to damper position is non-linear and pressure-dependent:

**At 0.5 in. w.g. upstream pressure:**

| Damper Position | Approximate Flow (% Max) | Control Authority |
|-----------------|-------------------------|-------------------|
| 100% open | 100% | Maximum flow |
| 75% open | 85-90% | Good control |
| 50% open | 60-70% | Moderate control |
| 25% open | 30-45% | Poor control |
| 10% open | 10-20% | Minimal control |

**At 1.0 in. w.g. upstream pressure:**
All flow rates increase by approximately 40% at equivalent damper positions, demonstrating pressure dependency.

## Control Limitations

### Static Pressure Interaction

When one or more zones reduce demand and their dampers close partially, static pressure at other terminals increases. This creates cascading effects:

1. **Reduced Load Zone:** Damper closes to 30% position
2. **Supply Fan Response:** Duct static pressure increases (if VFD lag exists)
3. **Other Zones:** Airflow increases unintentionally
4. **System Result:** Simultaneous overcooling and undercooling in different zones

### Temperature Control Accuracy

Pressure-dependent terminals exhibit poor temperature control under varying system conditions:

**Typical control accuracy:**
- Best case (stable pressure): ±2°F
- Normal operation: ±3-4°F
- High pressure variation: ±5-7°F
- Worst case: Unable to maintain setpoint

### Turndown Limitations

Effective turndown ratio (maximum flow to minimum controllable flow) is limited by:
- Damper authority at low positions: typically 3:1 to 4:1
- Pressure fluctuation effects: reduces effective turndown
- Practical turndown with pressure variation: 2:1 to 3:1

## Application Considerations

### Appropriate Applications

Pressure-dependent VAV terminals can function acceptably in limited applications:

**Building Types:**
- Small single-zone-per-floor offices with minimal load diversity
- Spaces with consistent occupancy and load patterns
- Retrofit applications where budget severely constrains options
- Non-critical spaces with relaxed comfort requirements

**System Requirements:**
- Total system capacity under 10,000 CFM
- Limited number of terminals (typically under 10 zones)
- Zones with similar load characteristics
- Applications with continuous fan operation

### Design Constraints

**Static Pressure Management:**
- Critical requirement for stable duct static pressure
- Fast-responding static pressure reset recommended
- Multiple static pressure sensors improve stability
- Supply fan VFD with rapid response essential

**Duct Design:**
- Lower design velocities reduce pressure variation
- Oversized ductwork improves pressure stability
- Avoid excessive fitting losses near terminals
- Design static pressure: 0.75-1.0 in. w.g. maximum

**Zone Sizing:**
- Minimize number of zones per system
- Size zones for similar peak loads
- Avoid mixing perimeter and interior zones
- Consider dedicated systems for high-diversity areas

## Comparison with Pressure-Independent Systems

| Characteristic | Pressure-Dependent | Pressure-Independent |
|----------------|-------------------|----------------------|
| Flow control accuracy | Poor (±20-30%) | Excellent (±5-10%) |
| Pressure sensitivity | High sensitivity | Independent of pressure |
| Temperature control | ±3-5°F typical | ±1-2°F typical |
| System complexity | Simple | Moderate to complex |
| First cost | Lowest ($200-400) | Higher ($600-1200) |
| Commissioning requirements | Extensive balancing | Simpler, self-balancing |
| Energy efficiency | Lower (hunting, overcooling) | Higher (precise control) |
| Maintenance | Minimal | Moderate (flow sensors) |
| Application range | Limited | Broad |

## Installation Requirements

### Upstream Conditions

Proper installation requires attention to approach conditions:
- Minimum 3 duct diameters straight upstream duct
- 5 diameters preferred for accurate damper control
- Avoid elbows or transitions immediately upstream
- Remove construction debris before startup

### Damper Orientation

Blade orientation affects control characteristics:
- Parallel blade: higher flow at partial closure (rarely used)
- Opposed blade: better control authority (standard)
- Airfoil blade: lowest pressure drop, best control

### Actuator Mounting

Proper actuator installation ensures reliable operation:
- Mount per manufacturer orientation requirements
- Provide adequate clearance for maintenance
- Protect from water exposure or condensation
- Verify proper damper shaft coupling

## Commissioning and Balancing

### Initial Setup Challenges

Pressure-dependent systems require extensive balancing:

1. **Proportional balancing required:** Adjust all dampers to achieve design flows at one operating condition
2. **Iterative process:** Multiple rounds of adjustment as system settles
3. **Pressure-dependent results:** Balance valid only at specific system loading
4. **Seasonal variation:** May require rebalancing between seasons

### Test and Balance Procedures

**Critical measurements:**
- Inlet static pressure at each terminal
- Actual airflow at design conditions
- Supply air temperature
- Zone temperature at various loads

**Adjustment methodology:**
- Balance at design cooling conditions
- Document inlet static pressures
- Set minimum damper positions
- Verify control response through full range

## Performance Optimization

### Static Pressure Reset

Implementing aggressive static pressure reset partially compensates for pressure-dependent behavior:

**Reset strategies:**
- Trim and respond: Reset based on most open damper position
- Multiple sensor averaging: Reduce localized pressure spikes
- Fast response required: Update setpoint every 30-60 seconds
- Setpoint limits: Maintain 0.5-1.0 in. w.g. range

### Damper Minimum Position

Setting minimum damper positions addresses ventilation and control:
- Typically 20-30% open position minimum
- Ensures minimum ventilation airflow
- Maintains some control authority
- Reduces extreme pressure variations

### Zone Grouping

Strategic zone grouping improves system performance:
- Group zones with similar load patterns
- Separate perimeter and interior zones
- Consider dedicated systems for problem areas
- Limit zones per system to 6-8 maximum

## Economic Analysis

### First Cost Advantage

The primary advantage of pressure-dependent terminals is low first cost:

**Installed cost comparison (per terminal):**
- Pressure-dependent: $400-600 installed
- Pressure-independent: $900-1,400 installed
- Cost differential: $500-800 per terminal
- Typical system savings: $5,000-15,000 for 10-20 zone system

### Operating Cost Penalties

Lower first cost is offset by higher operating costs:

**Energy penalties:**
- Overcooling/overheating: 10-20% increase in energy use
- Damper hunting and cycling: 5-10% fan energy increase
- Poor humidity control: Possible reheat energy waste
- Estimated annual penalty: $0.50-1.50 per square foot

**Comfort and productivity costs:**
- Temperature complaints and adjustments
- Maintenance calls for "system not working"
- Reduced occupant satisfaction
- Difficult to quantify but significant

### Life-Cycle Cost

Over typical 20-year equipment life:
- Higher energy costs typically exceed first cost savings
- Increased service calls add maintenance costs
- Tenant complaints create management costs
- Pressure-independent systems usually more cost-effective

## Troubleshooting Common Issues

### Insufficient Airflow

**Symptoms:** Zone cannot achieve setpoint despite damper fully open

**Causes:**
- System static pressure too low
- Excessive pressure drop in ductwork
- Undersized terminal selection
- Supply air temperature inadequate

**Solutions:**
- Verify design static pressure at terminal inlet
- Check for duct obstructions or damage
- Increase supply fan speed if margin available
- Consider terminal replacement if severely undersized

### Excessive Airflow/Noise

**Symptoms:** Zone overcools, damper nearly closed, noise complaints

**Causes:**
- Excessive static pressure at terminal
- Poor system pressure control
- Oversized terminal for actual load
- Ductwork design velocity too high

**Solutions:**
- Implement or improve static pressure reset
- Add manual volume damper upstream to limit maximum flow
- Verify supply fan VFD operation
- Consider terminal replacement if severe

### Poor Temperature Control

**Symptoms:** Zone temperature varies widely, cannot maintain setpoint

**Causes:**
- Static pressure fluctuation in duct system
- Inadequate damper control authority
- Thermostat calibration or location problems
- Simultaneous heating/cooling from adjacent zones

**Solutions:**
- Improve static pressure control and reset
- Verify minimum damper position settings
- Check thermostat calibration and location
- Consider upgrade to pressure-independent terminals

## Conclusion

Pressure-dependent VAV terminal units represent the most basic form of VAV control, suitable only for small systems with limited zone diversity and relaxed comfort requirements. The fundamental limitation—airflow variation with system pressure—creates control challenges that require careful system design, aggressive pressure control, and extensive commissioning.

For most commercial applications, the modest first cost savings do not justify the performance limitations, higher energy use, and increased maintenance requirements. Pressure-independent terminals provide superior performance and typically better life-cycle costs, making them the preferred choice for systems with more than 6-8 zones or any application requiring precise temperature control.

Modern building requirements for energy efficiency, indoor air quality, and occupant comfort make pressure-dependent systems increasingly obsolete except in the smallest and simplest applications.
