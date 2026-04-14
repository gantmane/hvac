---
title: "Burner Controls and Flame Safeguard Systems"
aliases: ["Burner Controls and Flame Safeguard Systems"]
weight: 4
description: "Comprehensive analysis of burner control systems including flame safeguard programming, air-fuel ratio positioning controls, oxygen trim systems, cross-limiting logic, and safety interlocks for commercial and industrial automatic fuel-burning equipment per NFPA 86 requirements."
keywords: "burner controls, flame safeguard, air-fuel ratio control, oxygen trim, cross-limiting, UV scanner, flame detection, burner management system, NFPA 86"
tags: ["burner controls", "flame safeguard", "air-fuel ratio control", "oxygen trim", "cross-limiting", "UV scanner", "flame detection", "burner management system", "NFPA 86"]
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

## Programming Controllers

### Burner Management System Architecture

**Programmable flame safeguard controllers (PFSC):**

Modern burner management systems utilize microprocessor-based programming controllers that integrate flame safeguard sequencing, safety interlocks, modulation control, and diagnostic functions. These controllers replace traditional relay-based logic with software-defined sequences meeting NFPA 86 and CSD-1 requirements.

**Controller classifications:**

**Class A controllers:**
- Self-checking design with continuous internal diagnostics
- Dual microprocessor architecture with cross-checking
- Diagnostic fault detection within 1 second
- Automatic lockout on internal fault
- Required for systems >12.5 MMBtu/h per NFPA 86

**Class B controllers:**
- Single microprocessor with self-checking routines
- Periodic diagnostic testing (every startup cycle)
- Suitable for smaller systems <12.5 MMBtu/h
- Lower cost than Class A
- Manual verification of safety functions during commissioning

**Programming methodology:**

**Timing diagram development:**

Controllers execute preprogrammed timing sequences with discrete outputs for each controlled device:

**Sequence timing table:**

| Event | Start Time | Duration | Outputs Energized | Interlocks Required |
|-------|-----------|----------|-------------------|---------------------|
| Pre-start check | 0 s | 2-5 s | None | All safety devices proven |
| Pre-purge | 5 s | 60 s | Fan, damper 100% | Air pressure proven |
| Pilot trial | 65 s | 10 s | Pilot valve, ignitor | Scanner clear |
| Main trial | 75 s | 10 s | Main valve, ignitor | Pilot flame proven |
| Flame stabilization | 85 s | 10 s | Main valve | Main flame proven |
| Modulation enabled | 95 s | Continuous | Per demand | Continuous flame supervision |

**Custom sequence programming:**

Advanced controllers allow field programming of timing parameters:
- Pre-purge duration: 15-300 seconds (must meet code minimums)
- Trial for ignition: 4-15 seconds (fuel-dependent)
- Flame stabilization hold: 5-60 seconds
- Interlocks bypass conditions: Controlled shutdown only
- Alarm response delays: 1-10 seconds (nuisance prevention)

**Parameter storage:**
- Non-volatile memory retains settings during power loss
- Password protection prevents unauthorized changes
- Audit trail logs all parameter modifications
- Remote programming capability via network interface

### Advanced Control Features

**Adaptive control algorithms:**

Modern programming controllers incorporate adaptive features optimizing performance:

**Load-based purge time:**
- Standard purge: Fixed duration per code requirements
- Adaptive purge: Extended duration after high-fire operation
- Calculation: Purge time proportional to previous firing rate × time

$$t_{purge,adaptive} = t_{purge,min} + K_{adapt} \times \int_{0}^{t_{off}} FiringRate(\tau) d\tau$$

Where $K_{adapt}$ scales accumulated heat input to additional purge time.

**Self-tuning combustion:**
- O₂ trim setpoint optimization based on efficiency calculations
- Automatic fuel characterization (heating value compensation)
- Seasonal adjustment for air density changes
- Efficiency tracking with alarm on degradation >5%

**Predictive diagnostics:**
- Flame signal trending to predict scanner maintenance needs
- Ignition trial statistics identifying marginal ignition
- Interlock nuisance trip logging
- Cycle counting for planned maintenance scheduling

## Fuel Valve Proving Systems

### Valve Proving Methodology

Fuel valve proving systems verify automatic safety shutoff valves (ASSO) achieve complete closure and gas-tight seal before permitting burner startup. NFPA 86 and ASME CSD-1 mandate valve proving for systems >400,000 Btu/h.

**Proving system configuration:**

**Dual valve with vent proving:**

Standard configuration per NFPA 86:
- Two automatic shutoff valves in series
- Vent valve between safety shutoff valves
- Pressure switch monitoring vent section
- Test sequence proves both valves seal

**Component layout:**

```
[Gas supply] → [Manual cock] → [ASSO #1] → [Vent valve + Pressure switch] → [ASSO #2] → [Burner]
```

**Valve proving sequence:**

**Pre-startup proving:**

**Step 1 - Valve closure verification:**
1. Both ASSO valves confirmed closed (de-energized)
2. Vent valve opens to atmosphere
3. Monitor vent section pressure
4. Pressure must decay to <0.5 in. w.c. within proving time (5-60 seconds)
5. Decay confirms at least one valve sealed

**Step 2 - Valve #1 leak test:**
1. Close vent valve
2. Open ASSO #1 (upstream valve)
3. Monitor pressure rise in vent section
4. Pressure must remain <50% of supply pressure for leak test period (5-60 seconds)
5. Pass indicates ASSO #2 sealed gas-tight

**Step 3 - Valve #2 leak test:**
1. Close ASSO #1
2. Open vent valve momentarily to relieve vent section
3. Close vent valve
4. Open ASSO #2 (downstream valve)
5. Monitor pressure decay in vent section
6. Pressure must decay below threshold (proves ASSO #1 sealed)

**Acceptance criteria:**

**Leak rate calculation:**

Maximum allowable leakage through closed valve:

$$Q_{leak,max} = 0.01 \times Q_{burner,max}$$

For 10 MMBtu/h burner: Maximum valve leakage = 100,000 Btu/h

**Pressure-based leak detection:**

Vent section volume and pressure change indicate leak rate:

$$Q_{leak} = \frac{V_{vent} \times \Delta P}{t_{test} \times P_{atm}} \times Q_{supply}$$

Where:
- $V_{vent}$ = Vent section volume (ft³)
- $\Delta P$ = Pressure change during test (in. w.c.)
- $t_{test}$ = Test duration (seconds)
- $P_{atm}$ = Atmospheric pressure (407 in. w.c.)
- $Q_{supply}$ = Available gas flow rate

**Proving system components:**

**Pressure switch specifications:**
- Sensing range: 0-10 in. w.c. typical
- Accuracy: ±0.1 in. w.c.
- Response time: <1 second
- Adjustability: Fixed factory setting (tamper-proof)
- Enclosure: NEMA 4 minimum (outdoor/washdown environments)

**Vent valve sizing:**
- Flow capacity: Sufficient to relieve vent section in <5 seconds
- Seal class: Bubble-tight shutoff
- Actuator: Fail-open (spring return to vent position)

**Proving time parameters:**
- Minimum test duration: 5 seconds (adequate pressure response)
- Maximum test duration: 60 seconds (startup delay limitation)
- Typical setting: 10-15 seconds per valve test

### Proving System Failures

**Lockout conditions:**

**Both valves leaking:**
- Vent section pressure fails to decay (Step 1 failure)
- Indicates both valves passing gas
- Potential furnace flooding hazard
- Replace both valves before operation permitted

**Upstream valve leaking:**
- Step 2 passes, Step 3 fails
- ASSO #1 not sealing
- Gas accumulation in vent section when downstream valve opens
- Replace upstream valve

**Downstream valve leaking:**
- Step 2 fails, vent section pressure rises
- ASSO #2 passing gas with upstream valve open
- Most common failure mode
- Replace downstream valve

**Pressure switch failure:**
- Erratic proving results
- Nuisance lockouts on good valves
- Switch stuck or out of calibration
- Annual calibration verification required

## Air Proving Switches

### Air Pressure Proving

Air proving switches verify combustion air fan operation and adequate airflow before fuel valve opening. These critical safety devices prevent fuel-rich operation causing fires or explosions.

**Pressure switch installation:**

**Sensing location:**
- Install in burner windbox (after combustion air fan)
- Location must sense actual burner air pressure
- Avoid dead-end taps (dirt accumulation, condensation)
- Install sensing line sloped for condensate drainage

**Typical pressure ranges:**

| Burner Type | Normal Pressure | Switch Setpoint | Application |
|-------------|-----------------|------------------|-------------|
| Atmospheric | 0.1-0.5 in. w.c. | 0.05-0.1 in. w.c. | Residential furnaces |
| Low pressure | 1-5 in. w.c. | 0.8-4 in. w.c. | Commercial burners |
| High pressure | 5-20 in. w.c. | 4-18 in. w.c. | Industrial burners |
| Forced draft | 10-50 in. w.c. | 8-45 in. w.c. | Large industrial |

**Setpoint determination:**

Set air proving switch at 80-90% of normal operating pressure:

$$P_{switch} = 0.80 \times P_{operating,normal}$$

This provides margin for:
- Filter loading (pressure drop increase over time)
- Damper position variation
- Atmospheric pressure changes
- Fan performance degradation

**Response time requirements:**

**Startup proving:**
- Fan starts
- Pressure must rise above switch setpoint within 10-30 seconds
- Proving establishes before fuel permitted
- Excessive delay indicates fan, damper, or ductwork problem

**Running supervision:**
- Continuous monitoring during operation
- Pressure loss triggers immediate fuel shutoff
- Typical trip delay: 1-2 seconds (prevents nuisance trips)
- Fan failure, damper closure, or ductwork collapse detected

**Switch selection criteria:**

**Differential vs. gage pressure:**
- Differential: Compares burner pressure to atmosphere
- Gage: Measures absolute pressure (draft applications)
- Burners typically use differential sensing

**SPDT vs. DPDT contacts:**
- SPDT: Single pole, adequate for most applications
- DPDT: Double pole, required for redundant safety circuits
- Contact rating: Minimum 5A at 120VAC (pilot duty)

**Adjustable vs. fixed:**
- Adjustable: Field setting of trip point (commission flexibility)
- Fixed: Factory-set (tamper-proof, certified applications)
- Adjustment range: Typically 2:1 to 10:1 span

### Air Switch Testing and Maintenance

**Functional testing procedure:**

**Startup test:**
1. Initiate burner startup sequence
2. Observe fan start
3. Measure time to air pressure switch closure
4. Verify switch closes before fuel valves open
5. Document proving time

**Running test:**
1. With burner operating at high fire
2. Manually close combustion air damper slightly
3. Observe pressure decrease
4. Switch should trip at setpoint pressure
5. Fuel valves should close immediately
6. Return damper to normal position and restart

**Annual calibration:**
- Remove switch from service
- Connect to calibrated pressure source
- Verify trip point within ±5% of setpoint
- Check contact operation (continuity test)
- Document results, recalibrate if drift >5%

**Common failure modes:**

**Condensate blockage:**
- Sensing line fills with water
- Gives false pressure reading (high or erratic)
- Install moisture trap or slope lines for drainage
- Winterization: Heat trace in freezing environments

**Diaphragm deterioration:**
- Switch becomes sluggish or inoperative
- Age-related rubber/elastomer degradation
- Replace switch every 5-10 years as preventive maintenance

**Contact corrosion:**
- Switch fails to make or break circuit
- Caused by low current (pilot duty) and environmental exposure
- Use gold-plated contacts for low-current applications

## High Limit Controls

### Temperature and Pressure Limiting

High limit controls provide independent overheat protection separate from operating controls. ASME Boiler and Pressure Vessel Code Section IV requires high limits on all automatically fired boilers.

**Limit control types:**

**Steam boiler pressure limit:**

**Installation:**
- Senses steam pressure directly from boiler steam space
- Independent sensing from operating pressure control
- Manual reset required after trip

**Settings:**

| Boiler MAWP | Operating Pressure | Limit Setting | Operating Control |
|-------------|-------------------|---------------|-------------------|
| 15 psig | 5-10 psig | 15 psig | 8 psig |
| 50 psig | 20-40 psig | 50 psig | 35 psig |
| 150 psig | 100-125 psig | 150 psig | 115 psig |

High limit must not exceed boiler MAWP (Maximum Allowable Working Pressure).

**Hot water boiler temperature limit:**

**Installation:**
- Immersion well in boiler outlet header
- Sensor must contact water directly (proper well installation)
- Manual reset typically required

**Settings:**

| Boiler Type | Operating Range | Limit Setting |
|-------------|-----------------|---------------|
| Low temperature | 120-160°F | 180-200°F |
| Standard | 160-200°F | 220-240°F |
| High temperature | 200-240°F | 250-260°F |

Limit setpoint 20-40°F above normal operating temperature provides safety margin without nuisance trips.

**Process heater limits:**

**Multiple limit strategy:**
- Process temperature limit (product protection)
- Heater tube skin temperature limit (equipment protection)
- Stack temperature limit (fire detection)

Each limit independently capable of shutting fuel supply.

### Limit Control Installation Standards

**Sensor placement:**

**Critical requirements:**
- Immersion wells: Minimum 4-inch insertion into fluid
- Well fill: Conductive paste or oil (eliminates air gaps)
- Location: Representative of maximum temperature/pressure
- Avoid stratified zones, dead-end connections

**Capillary tube considerations:**
- Maximum length: 6-12 feet (manufacturer-specified)
- Protection: Metal conduit in traffic areas
- Bending radius: Minimum 3-inch radius (avoid kinking)
- Temperature rating: Ambient temperature along entire length

**Electrical wiring:**

**Safety circuit integration:**

Limit controls wired to interrupt fuel valve circuit directly:

```
[Line] → [High limit] → [Operating control] → [Flame safeguard] → [Fuel valve]
```

Breaking any device in series string stops fuel flow immediately.

**Manual reset requirement:**

ASME code mandates manual reset high limits:
- Prevents automatic restart after overheat condition
- Forces operator investigation of trip cause
- Reset button located at boiler (not remote panel)
- Trip indication: Visible alarm light or flag

**Limit control testing:**

**Functional test procedure:**

**Method 1 - Controlled heat:**
1. With burner firing, disable operating control
2. Allow boiler temperature/pressure to rise slowly
3. Observe limit trip at setpoint
4. Verify fuel valves close immediately
5. Record trip point, compare to setting (±2% tolerance)

**Method 2 - Simulated trip:**
1. Disconnect limit control sensor
2. Apply test signal simulating over-temperature/pressure
3. Verify trip and fuel shutoff
4. Reconnect sensor and verify proper reading

**Test frequency:**
- Operating test: Monthly (observe normal operation)
- Functional trip test: Annually
- Calibration verification: Every 2-5 years

## Modulating Control Systems

### Proportional-Integral-Derivative Control

Modulating burner controls maintain process variables within tight tolerances using PID algorithms adjusting firing rate continuously. Modern systems achieve ±1-2°F control with proper tuning.

**Control loop components:**

**Sensor (measurement):**
- Temperature: RTD (Pt100, Pt1000) or thermocouple
- Pressure: 4-20 mA transmitter
- Accuracy requirement: ±0.25-0.5% of span

**Controller (computation):**
- Microprocessor-based PID algorithm
- Update rate: 0.1-1 second intervals
- Auto-tune capability: Automatic PID parameter determination

**Actuator (final control element):**
- Modulating damper actuator (air control)
- Modulating fuel valve (fuel control)
- Travel time: 15-60 seconds full stroke
- Position feedback: 4-20 mA or 0-10 VDC signal

**PID algorithm implementation:**

**Discrete PID equation:**

For digital controllers with sampling interval $\Delta t$:

$$u_n = K_p e_n + K_i \sum_{k=0}^{n} e_k \Delta t + K_d \frac{e_n - e_{n-1}}{\Delta t}$$

Where:
- $u_n$ = Control output at sample $n$ (firing rate %)
- $e_n$ = Error at sample $n$ (setpoint - measurement)
- $K_p, K_i, K_d$ = PID gains

**Anti-windup protection:**

Integral windup occurs when actuator saturates (0% or 100%) but error continues accumulating:

**Conditional integration:**

$$\int e dt =
\begin{cases}
\text{Accumulate} & \text{if } 0\% < u < 100\% \\
\text{Freeze} & \text{if } u = 0\% \text{ or } u = 100\%
\end{cases}$$

Prevents overshoot on setpoint changes or load disturbances.

**Tuning methodology:**

**Ziegler-Nichols closed-loop method:**

1. Set $K_i = 0$, $K_d = 0$ (proportional only)
2. Increase $K_p$ until sustained oscillation occurs
3. Record ultimate gain $K_u$ and oscillation period $T_u$
4. Calculate PID parameters:

$$K_p = 0.6 K_u$$
$$K_i = \frac{1.2 K_u}{T_u}$$
$$K_d = 0.075 K_u T_u$$

**Lambda tuning (process-specific):**

For first-order plus dead time processes (typical thermal systems):

$$K_p = \frac{\tau}{\lambda K_{process}}$$
$$K_i = \frac{1}{\lambda}$$

Where $\lambda$ = desired closed-loop time constant (1-3× process time constant).

**Practical tuning tips:**

**Start conservative:**
- $K_p$: Set for 20-30°F proportional band initially
- $K_i$: 0.1-0.2 (reset time 5-10 minutes)
- $K_d$: 0 initially (add only if needed for fast processes)

**Observe response:**
- Step setpoint change ±10°F
- Measure overshoot, settling time, oscillations
- Quarter-decay ratio: Peak overshoot = 25% of step

**Adjust iteratively:**
- Reduce overshoot: Decrease $K_p$, increase $K_i$
- Reduce settling time: Increase $K_p$, decrease $K_i$
- Reduce oscillations: Decrease all gains, add $K_d$ carefully

## Lockout Procedures and Reset Protocols

### Safety Lockout Classification

Burner management systems employ multiple lockout categories based on fault severity and required corrective action.

**Hard lockout (manual reset required):**

Conditions requiring operator investigation before restart:

1. **Flame failure during operation**
   - Main flame lost while burner firing
   - Indicates fuel supply, ignition, or combustion problem
   - Potential unburned fuel accumulation
   - Investigation required: Check fuel supply, scanner, air-fuel ratio

2. **Ignition failure**
   - Flame not established within trial-for-ignition period
   - Indicates ignition system, fuel supply, or air-fuel ratio fault
   - Multiple retries create explosion hazard
   - Investigation required: Verify spark, fuel pressure, air damper position

3. **Unsafe flame signal**
   - Flame detected during pre-purge (before fuel commanded)
   - Flame signal with all fuel valves closed
   - Scanner self-check failure
   - Indicates scanner malfunction or flame rectification
   - Investigation required: Verify scanner operation, check for hot refractory false signal

4. **Critical interlock failure**
   - Low combustion air pressure
   - Fuel pressure out of range
   - High temperature/pressure limit trip
   - Low water condition (steam boilers)
   - Investigation required: Resolve interlock condition, verify safe operation

**Soft lockout (automatic retry permitted):**

Transient conditions allowing limited automatic restart attempts:

1. **Momentary power loss**
   - Controller loses power briefly
   - Burner sequence interrupted
   - Automatic restart after power restoration and pre-purge
   - Limit: 3 retries, then hard lockout

2. **Nuisance interlock trip**
   - Brief pressure fluctuations
   - Transient electrical noise
   - Delay timers prevent nuisance lockout
   - Automatic restart if condition clears within 5-10 seconds

### Reset and Restart Procedures

**Manual reset protocol:**

**Required operator actions:**

1. **Identify lockout cause**
   - Read fault code or alarm display
   - Note which interlock or safety device tripped
   - Record operating conditions at time of lockout

2. **Investigate and correct root cause**
   - Verify fuel supply adequate
   - Check air fan operation
   - Inspect flame scanner cleanliness
   - Test interlock devices
   - Correct identified deficiency

3. **Verify safe conditions**
   - Confirm no gas accumulation in furnace
   - Check that all interlocks satisfied
   - Verify manual fuel cock open
   - Ensure proper burner configuration

4. **Execute controlled restart**
   - Press manual reset button (at burner location)
   - Observe pre-purge completion
   - Monitor ignition sequence
   - Verify stable operation at low-fire
   - Allow modulation to operating setpoint

**Lockout persistence:**

**Recycle limit:**

Controllers limit restart attempts preventing repeated ignition failures:

**Standard recycling logic:**
- First lockout: Manual reset, immediate restart permitted
- Second lockout within 1 hour: Manual reset, 5-minute delay before restart
- Third lockout within 1 hour: Manual reset disabled, service required
- Reset condition after 1 hour of successful operation

**Service lockout conditions:**

Faults requiring qualified technician:
- Repeated flame failures (>3 in 24 hours)
- Scanner self-check failures
- Internal controller faults
- Valve proving system failures

Service lockout requires password or physical reset (key switch) accessible only to authorized personnel.

**Documentation requirements:**

**Lockout logging:**

Modern controllers maintain event logs:
- Date/time of lockout
- Fault code and description
- Operating conditions (firing rate, temperatures, pressures)
- Number of occurrences
- Operator actions taken

Review lockout history to identify:
- Recurring problems requiring corrective maintenance
- Seasonal issues (outdoor temperature effects)
- Operator training needs
- Equipment degradation trends
