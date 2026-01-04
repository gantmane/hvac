---
title: "Burner Controls and Flame Safeguard Systems"
weight: 4
description: "Comprehensive analysis of burner control systems including flame safeguard programming, air-fuel ratio positioning controls, oxygen trim systems, cross-limiting logic, and safety interlocks for commercial and industrial automatic fuel-burning equipment per NFPA 86 requirements."
keywords: "burner controls, flame safeguard, air-fuel ratio control, oxygen trim, cross-limiting, UV scanner, flame detection, burner management system, NFPA 86"
---

# Burner Controls and Flame Safeguard Systems

Burner control systems integrate flame safeguard logic, air-fuel ratio positioning, and safety interlocks to ensure safe startup, reliable operation, and controlled shutdown of automatic fuel-burning equipment. Modern burner management systems (BMS) combine programmable flame safeguard controls (PFSC) per NFPA 86, modulating positioning controls achieving ±5-10% air-fuel ratio accuracy, oxygen trim systems maintaining 2-4% O₂, and comprehensive safety interlocks preventing unsafe operating conditions. Proper control system design and programming are critical to achieving combustion efficiency targets while maintaining safety compliance and preventing equipment damage or explosion hazards.

## Flame Safeguard Controls

### Startup Sequence Programming

**Standard burner startup per NFPA 86:**

**1. Pre-start checks (system interlocks):**
- Verify combustion air fan running
- Prove combustion air pressure (pressure switch)
- Verify fuel supply pressure adequate
- Check flame scanner proven clear (no residual flame signal)
- Verify furnace draft acceptable (if required)
- Confirm all safety interlocks satisfied

Failure of any pre-start check prevents startup sequence from initiating.

**2. Pre-purge:**
- Duration: Minimum 15 seconds for small burners (<400,000 Btu/h)
- Duration: Minimum 30 seconds for medium burners (0.4-10 MMBtu/h)
- Duration: Minimum 60 seconds for large burners (>10 MMBtu/h)
- Purpose: Remove any combustible gases from furnace/flue
- Air changes required: Minimum 4 complete air changes
- Fan operation: 100% air flow during purge

**Pre-purge time calculation:**

$$t_{purge} = \frac{4 \times V_{furnace}}{\dot{V}_{air}} \times 3600$$

Where:
- $V_{furnace}$ = Furnace volume (ft³)
- $\dot{V}_{air}$ = Air flow rate (cfm)
- $t_{purge}$ = Purge time (seconds)

**3. Pilot ignition (if used):**
- Pilot gas valve opens
- Spark ignitor energizes
- Trial for ignition period: 4-10 seconds
- Flame scanner must detect pilot flame before main fuel enabled
- Pilot flame must remain stable throughout main flame establishment

**4. Main fuel ignition:**
- Positioning system moves to low-fire position
- Verify low-fire position reached (limit switches)
- Spark ignitor continues (oil burners) or pilot proven (gas burners)
- Main fuel valve opens
- Trial for ignition: 4-10 seconds (gas), 15 seconds (oil)
- Flame scanner must detect main flame within trial period
- Ignitor de-energizes after flame establishment

**5. Flame establishment:**
- Flame signal strength verified adequate (typically >3 μA for UV)
- Hold at low-fire for flame stabilization (5-30 seconds)
- System ready for modulation to firing rate setpoint

**Startup sequence timing example:**

For 5 MMBtu/h burner:
- Pre-start checks: 2-5 seconds
- Pre-purge: 60 seconds minimum
- Pilot trial: 10 seconds
- Main trial: 10 seconds
- Low-fire hold: 10 seconds
- **Total startup time:** 92-95 seconds

### Flame Detection Technologies

**Ultraviolet (UV) scanner:**

**Operating principle:**
- UV-sensitive tube detects radiation 1850-2900 Å wavelength
- Flame emits UV; sunlight filtered by furnace
- Self-checking via shutter or modulated detection
- Response time: 1-4 seconds

**Advantages:**
- Works with gas and oil flames
- Discriminates flame from hot refractory
- Self-checking capability
- Not susceptible to electromagnetic interference

**Typical installation:**
- Sighting distance: 12-48 inches from flame
- Mounting angle: 15-30° from horizontal
- Requires clean sight path (no oil spray fouling)
- Self-check interval: 1-3 seconds

**Flame signal strength:**
- Minimum acceptable: 2-3 μA
- Typical operating range: 5-15 μA
- Weak flame alarm: <3 μA
- Flame failure trip: <1 μA for >2 seconds

**Cadmium sulfide (CdS) flame detector:**

**Operating principle:**
- Photoresistor sensitive to visible light (5500 Å)
- Flame produces visible light, resistance decreases
- Requires complete darkness with burner off
- Response time: 1-3 seconds
- Used primarily residential/light commercial

**Typical resistance:**
- Dark (no flame): >100,000 ohms
- Illuminated (flame present): 300-1000 ohms
- Trip threshold: >10,000 ohms

**Flame rod (ionization):**

**Operating principle:**
- Metal rod inserted in flame
- AC voltage applied (120V typically)
- Flame ionization creates conductive path
- DC microamp signal indicates flame presence
- Gas flames only (oil too conductive)

**Typical signal:**
- Good flame: 3-10 μA DC
- Weak flame: 1-3 μA
- No flame: <0.5 μA

**Installation requirements:**
- Rod position: 1-3 inches into flame envelope
- Insulation: High-temperature ceramic
- Grounding: Burner must be well-grounded
- Gap: Rod must not contact burner parts

**Infrared (IR) scanner:**

**Operating principle:**
- Detects specific IR wavelengths (4.3 μm for CO₂)
- Discriminates flame from background radiation
- Very reliable for large industrial burners
- Response time: 1-4 seconds

**Advantages:**
- Excellent flame/refractory discrimination
- Works in high-temperature environments
- Minimal maintenance
- Very stable signal

### Safety Lockout Conditions

**Flame failure lockout:**
- Flame lost during operation
- Immediate fuel shutoff
- Manual reset required
- Investigate and correct cause before restart

**Ignition failure lockout:**
- Flame not established within trial-for-ignition period
- Fuel valves close
- Manual reset required
- Check spark, fuel supply, air-fuel ratio

**Low airflow lockout:**
- Combustion air pressure below minimum
- Prevents fuel-rich combustion
- Check fan, dampers, ductwork

**Unsafe flame signal lockout:**
- Flame detected during pre-purge (residual flame)
- Flame signal with fuel valves closed (simulated flame)
- Scanner self-check failure
- Indicates scanner fault or flame rectification

**High/low fuel pressure:**
- Gas pressure outside acceptable range
- Oil pressure inadequate for atomization
- Check regulators, pumps, supply system

**Loss of atomizing medium:**
- Steam pressure low (steam atomizing oil burners)
- Air pressure low (air atomizing oil burners)
- Prevents poor combustion and smoke

## Air-Fuel Ratio Control

### Positioning Control Systems

**Jackshaft mechanical linkage:**

**Configuration:**
- Single rotary actuator drives jackshaft
- Mechanical linkages connect to air damper and fuel valve
- Cams shape linkage motion to maintain air-fuel ratio
- Fixed ratio across firing range (determined by cam design)

**Cam design methodology:**

For constant air-fuel ratio:

$$\theta_{fuel}(\theta_{damper}) = f(\theta_{damper})$$

Where function $f$ designed such that:

$$\frac{\dot{m}_{fuel}(\theta_{fuel})}{\dot{m}_{air}(\theta_{damper})} = \text{constant}$$

**Calibration procedure:**
1. Set high-fire position: Optimize air-fuel ratio via combustion analysis
2. Set low-fire position: Optimize air-fuel ratio at minimum fire
3. Adjust intermediate cam positions for smooth ratio across range
4. Verify combustion O₂ consistent (±0.5%) across firing range

**Advantages:**
- Simple, reliable
- Single actuator controls both air and fuel
- Proven technology
- Lower cost than electronic systems

**Limitations:**
- Fixed ratio (no automatic optimization)
- Mechanical wear over time
- Difficult to adjust without disassembly
- Limited to simpler systems

**Parallel positioning (electronic):**

**Configuration:**
- Separate actuators for air damper and fuel valve
- Electronic controller calculates required positions
- Feedback from position sensors
- Air-fuel curve programmed in controller

**Control algorithm:**

For firing rate demand $D$ (0-100%):

$$\theta_{damper} = f_1(D)$$
$$\theta_{fuel} = f_2(D)$$

Where $f_1$ and $f_2$ are characterized curves ensuring proper ratio.

**Characterization methods:**

1. **Point-by-point:**
   - Program specific positions at 10-20 firing rates
   - Controller interpolates between points
   - Allows custom curves for complex burner characteristics

2. **Mathematical model:**
   - Fit polynomial or exponential to air and fuel requirements
   - Calculate positions algorithmically
   - Enables smooth modulation

**Advantages:**
- Precise air-fuel ratio control
- Easy adjustment via software
- Can implement complex curves
- Diagnostic capability (position feedback)

**Limitations:**
- Higher cost than mechanical
- Requires commissioning/programming
- Electronic component reliability critical

### Cross-Limiting Control

**Purpose:** Prevent dangerous fuel-rich conditions during firing rate changes.

**Increasing firing rate logic:**

**Air lead:**
1. Air damper increases to target position
2. When air reaches 90% of target, fuel increase enabled
3. Fuel valve increases to target
4. Ensures air available before adding fuel

**Lead time:**

$$t_{lead} = \frac{\Delta \theta_{damper}}{r_{damper}} - \frac{\Delta \theta_{fuel}}{r_{fuel}}$$

Where:
- $\Delta \theta$ = Position change (degrees or %)
- $r$ = Actuator rate (degrees/second or %/second)

Typical: Air reaches position 2-5 seconds before fuel.

**Decreasing firing rate logic:**

**Fuel lead:**
1. Fuel valve decreases to target position
2. When fuel reaches 110% of target, air decrease enabled
3. Air damper decreases to target
4. Ensures excess air maintained during decrease

**Implementation:**

Modern cross-limiting implemented in PLC or dedicated combustion controller using:
- High-select logic (increasing): $Position_{actual} = \max(Position_{air} - offset, Position_{fuel})$
- Low-select logic (decreasing): $Position_{actual} = \min(Position_{fuel} + offset, Position_{air})$

**Safety benefit:** Prevents explosions and incomplete combustion during transients.

### Oxygen Trim Control

**System components:**

**Oxygen sensor:**
- Zirconia sensor (most common): 600-1500°F operating temperature
- Electrochemical sensor: 300-600°F operating temperature
- Response time: 5-20 seconds
- Accuracy: ±0.1-0.3% O₂

**Controller:**
- PID algorithm
- Setpoint: Typically 2.5-4.0% O₂
- Update frequency: 1-10 seconds
- Output: Air damper trim adjustment

**Trim actuator:**
- Modulates air damper or fan speed
- Authority: Typically ±10-20% from baseline
- Slow response to prevent instability

**Control loop:**

**PID algorithm:**

$$u(t) = K_p e(t) + K_i \int_0^t e(\tau) d\tau + K_d \frac{de(t)}{dt}$$

Where:
- $e(t) = O_{2,setpoint} - O_{2,measured}$
- $u(t)$ = Damper trim position
- $K_p$, $K_i$, $K_d$ = Proportional, integral, derivative gains

**Typical tuning:**
- $K_p = 2-5\%$ damper per % O₂ error
- $K_i = 0.5-2\%$ damper per % O₂·second
- $K_d = 0$ (derivative often disabled to prevent noise amplification)

**Setpoint selection:**

**Natural gas:**
- 2.0-3.0% O₂: High efficiency, requires good control
- 3.0-4.0% O₂: Safe operation, slightly lower efficiency

**No. 2 oil:**
- 2.5-3.5% O₂: Optimized efficiency
- 3.5-4.5% O₂: Conservative setting

**Operating limits:**
- High O₂ alarm: >6% (excessive excess air)
- Low O₂ alarm: <1.5% (insufficient excess air, safety risk)

**Efficiency improvement:**

Reducing O₂ from 5% to 3% at 450°F stack temperature:

**Excess air correlation:**

$$EA = \frac{21 \times O_2}{21 - O_2}$$

At 5% O₂: $EA = 31\%$
At 3% O₂: $EA = 17\%$

**Stack loss reduction:**

$$\Delta L_{stack} \approx 1\% \text{ per 40°F per \% O}_2$$

$$\Delta L_{stack} = \frac{(450-70) \times (5-3)}{40} \approx 1.9\%$$

**Efficiency improvement:** Approximately 2% increase by O₂ trim optimization.

## Modulation Control

### Firing Rate Control

**On-off control:**
- Burner cycles between off and full fire
- No intermediate firing rates
- Controlled by setpoint differential

**Operating characteristics:**
- Cycling rate: 3-10 cycles/hour typical
- Efficiency loss from cycling: 2-5%
- Temperature swing: ±5-15°F

**High-low-off control:**
- Three firing positions: Off, low-fire (30-50%), high-fire (100%)
- Reduces cycling losses vs. on-off
- Two-stage thermostat or controller

**Modulating control:**

**Proportional control:**

$$Fire\% = K_p \times (SP - PV) + Fire_{base}$$

Where:
- $SP$ = Temperature/pressure setpoint
- $PV$ = Process variable (measured temperature/pressure)
- $K_p$ = Proportional gain
- $Fire_{base}$ = Baseline firing rate (typically 0%)

**Proportional band:**

Range over which firing rate modulates from 0-100%:

$$PB = \frac{100\%}{K_p}$$

Example: If $K_p = 5$, then $PB = 20°F$ (firing rate changes 100% over 20°F temperature range)

**PID modulation:**

$$Fire\% = K_p e(t) + K_i \int e(\tau) d\tau + K_d \frac{de}{dt}$$

**Typical tuning for boiler:**
- $K_p = 3-10$ (proportional band 10-33°F)
- $K_i = 0.1-0.5$ (integral time 2-10 minutes)
- $K_d = 0-0.5$ (derivative time 0-5 minutes)

**Firing rate limiting:**
- Minimum firing rate: 10-30% (combustion stability limit)
- Maximum firing rate: 90-100% (safety margin, sensor limit)
- Rate of change limit: 10-30%/second (prevent thermal shock)

### Load Following Strategies

**Boiler pressure control:**

**Steam boiler:**
- Measure steam pressure
- Setpoint: Typically 10-150 psig
- Pressure drops → increase firing rate
- Proportional band: 5-15 psi typical

**Hot water boiler:**
- Measure supply water temperature
- Setpoint: Typically 140-200°F
- Temperature drops → increase firing rate
- Proportional band: 10-30°F typical

**Outdoor reset:**

Adjust setpoint based on outdoor temperature:

$$SP_{water} = SP_{design} - K_{reset} \times (T_{outdoor} - T_{design,outdoor})$$

Where $K_{reset} = 0.5-1.5°F$ water per °F outdoor

**Lead-lag control (multiple burners):**

**Sequence:**
1. Lead burner modulates 0-100%
2. When lead reaches 95-100%, lag burner starts
3. Both burners modulate proportionally
4. When load drops, lag burner unloads first

**Efficiency benefit:** Operate single burner at higher firing rate (better efficiency) when possible.

## Safety Interlocks

### Critical Safety Interlocks

**Combustion air proving:**
- Airflow switch or pressure switch
- Proves adequate air before fuel permitted
- Typical setting: 80-90% of normal air pressure

**Fuel pressure proving:**
- High/low gas pressure switches
- Oil pressure switch (atomization pressure)
- Prevents operation with improper fuel supply

**Flame safeguard supervision:**
- Flame scanner self-check
- Flame supervision during operation
- Lockout on flame failure or scanner fault

**Limit controls:**
- High temperature limit (ASME required for boilers)
- High pressure limit (steam boilers)
- Low water cutoff (steam boilers, absolutely critical)

**Ventilation interlock:**
- Combustion air intake damper proven open
- Exhaust damper proven open
- Room ventilation proven (enclosed burner rooms)

### Interlock Logic Implementation

**Series wiring (traditional):**
All safety devices wired in series with fuel valve circuit. Opening any switch interrupts fuel valve power.

**Advantages:** Simple, fail-safe
**Limitations:** No diagnostics, all interlocks look identical

**PLC-based interlocks:**
Each interlock provides discrete input to PLC. PLC logic determines burner enable.

**Advantages:**
- Detailed diagnostics
- Alarm annunciation
- Data logging
- Remote monitoring

**Alarm priority levels:**

**Level 1 - Immediate lockout:**
- Flame failure
- Low combustion air
- Low fuel pressure (gas)
- High temperature limit

**Level 2 - Pre-alarm:**
- Weak flame signal
- Drift in O₂ reading
- Low fuel pressure (oil, pre-pump)

**Level 3 - Advisory:**
- High number of cycles
- Low efficiency detected
- Service reminder

## Commissioning and Adjustment

### Initial Startup Procedure

**Step 1: Mechanical verification**
- Verify all linkages connected and moving freely
- Check damper and valve travel (0-100%)
- Confirm limit switches positioned correctly
- Verify flame scanner sighting

**Step 2: Control verification**
- Test all safety interlocks (force each to trip)
- Verify lockout on each condition
- Confirm reset function works
- Test flame failure response (shut fuel during operation)

**Step 3: Combustion adjustment**

**Low-fire setting:**
1. Position burner at low-fire (minimum firing rate)
2. Measure O₂, CO, stack temperature
3. Adjust air damper for target O₂ (typically 3-5% for safety)
4. Verify CO <100 ppm, smoke trace 0
5. Lock low-fire position

**High-fire setting:**
1. Position burner at high-fire (maximum firing rate)
2. Measure O₂, CO, stack temperature
3. Adjust air damper for target O₂ (typically 2.5-4%)
4. Verify CO <50 ppm, smoke trace 0
5. Optimize for efficiency (lowest O₂ with safe CO)
6. Lock high-fire position

**Intermediate points:**
- Check combustion at 25%, 50%, 75% firing rates
- Verify O₂ within ±0.5% across range
- Adjust cam or electronic curve if needed

**Step 4: Safety system verification**
- Verify pre-purge timing (measure actual duration)
- Confirm trial-for-ignition timing
- Test flame failure response time (<2 seconds typical)
- Document all settings

### Ongoing Optimization

**Oxygen trim commissioning:**
1. Set baseline air-fuel ratio (manual adjustment)
2. Enable O₂ trim control
3. Set O₂ setpoint (2.5-3.5% typical)
4. Tune PID loop (start with low gains, increase until stable)
5. Verify trim holds setpoint ±0.3% O₂
6. Document trim authority limits (±10-20%)

**Performance monitoring:**
- Log firing cycles per day
- Track average O₂
- Monitor stack temperature trends
- Record efficiency calculations
- Identify drift requiring re-tuning

**Maintenance intervals:**
- Combustion analysis: Monthly to quarterly
- Flame scanner cleaning: Quarterly to annually
- Linkage lubrication: Annually
- Full re-commissioning: Every 2-5 years
