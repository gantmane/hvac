---
title: "Functional Performance Testing"
description: "Comprehensive guide to HVAC functional performance testing including equipment tests, system integration verification, sequence of operations validation, trend data analysis, and deficiency tracking protocols per ASHRAE Guideline 0."
keywords: ["functional performance testing", "equipment testing", "system integration tests", "sequence of operations", "trend data analysis", "commissioning deficiencies", "ASHRAE Guideline 0", "FPT procedures", "HVAC testing protocol", "control sequence verification"]
weight: 4
---

Functional performance testing (FPT) represents the systematic verification that HVAC systems operate according to design intent and sequence of operations under actual load conditions. FPT distinguishes itself from static equipment testing by evaluating dynamic system responses, control interactions, and integrated performance across multiple operating modes.

## Equipment Performance Tests

Equipment-level functional testing validates individual components operate within specified parameters before integration testing. This hierarchical approach isolates equipment deficiencies from system-level issues.

### Chiller Functional Tests

Chiller FPT verifies capacity control, safety interlocks, and energy management sequences. Test the following:

- **Capacity staging**: Command chiller from 0-100% load in 10% increments. Verify guide vanes, compressor speed, or digital scroll modulation responds correctly. Record leaving water temperature, power draw, and response time at each step.
- **Safety shutdowns**: Simulate low evaporator temperature, low refrigerant pressure, high condenser pressure, and flow switch loss. Confirm immediate shutdown and lockout behavior.
- **Lead-lag rotation**: For multiple chiller plants, verify automatic rotation occurs per programmed interval. Test manual override capability.
- **Chilled water reset**: Command various outdoor air temperatures through BAS. Verify leaving water temperature resets according to programmed schedule.

### Boiler Functional Tests

Boiler testing validates firing sequences, modulation, and safety responses:

- **Firing sequence**: Initiate call for heat. Verify pre-purge period, pilot ignition, main burner ignition timing, and flame proving. Record all time delays.
- **Modulation verification**: Command boiler through full firing range. Confirm burner modulates smoothly without hunting. Monitor flue gas temperature and O₂ content at various firing rates.
- **Safety interlocks**: Test low water cutoff, high limit switch, blocked vent switch, and flame failure response. Each must shut down burner immediately.

### Air Handling Unit Tests

AHU functional testing encompasses economizer operation, heating/cooling sequencing, and fan control:

**Economizer sequence test script:**

```
1. Set space to cooling mode, outdoor air temperature to 45°F
2. Verify outdoor air damper opens to 100%, return air damper closes
3. Gradually increase OA temperature to 55°F, 65°F, 75°F
4. Record damper positions at each temperature
5. Verify mechanical cooling stages only when economizer exhausted
6. Confirm minimum outdoor air maintained at all positions
```

Test heating and cooling valve sequencing by commanding various supply air temperature setpoints. Verify valves modulate in proper sequence without simultaneous heating and cooling.

## System Integration Tests

Integration testing verifies coordinated operation across multiple equipment and control zones. These tests reveal communication failures, control conflicts, and unintended interactions.

### Plant-Distribution Integration

Test the relationship between central plants and distribution systems:

- **Differential pressure control**: Vary building load by adjusting terminal setpoints. Verify distribution pumps modulate to maintain setpoint. Confirm chillers or boilers stage appropriately with flow changes.
- **Primary-secondary decoupling**: For decoupled systems, verify primary flow remains constant while secondary flow modulates. Monitor common pipe temperature differential.

### Zone-Level Integration

Multi-zone systems require testing of master-submaster relationships:

- **VAV zone sequencing**: Command individual zones through full heating and cooling range. Verify proper airflow tracking, reheat lockout during economizer, and discharge temperature limits.
- **Simultaneous heating-cooling detection**: Monitor all zones simultaneously under mixed loads. Flag any zones providing heating and cooling concurrently.

## Sequence of Operations Verification

ASHRAE Guideline 0 emphasizes verification of all control sequences documented in design specifications. Create mode-specific test scripts for each unique sequence.

### Occupied Mode Test

```
Preconditions:
- Set schedule to occupied
- Space temperature at setpoint ±1°F
- All safeties normal

Test procedure:
1. Verify minimum outdoor air damper position = design %
2. Command space temperature +5°F above setpoint
3. Record: cooling valve position, airflow CFM, discharge temp
4. Verify cooling stages in correct sequence
5. Return to setpoint, allow 10 min stabilization
6. Command space temperature -5°F below setpoint
7. Record: heating valve position, airflow CFM, discharge temp
8. Verify heating stages in correct sequence
```

### Unoccupied Mode Test

Verify setback and setup sequences reduce energy consumption while maintaining equipment protection:

- Confirm space temperature drifts to unoccupied setpoints
- Verify HVAC equipment enters standby mode
- Test morning warmup or cooldown sequence initiation timing
- Validate optimal start calculations by comparing predicted vs actual time to occupancy temperature

## Trend Data Analysis

Continuous trend logging provides quantitative performance evidence. Configure trends before testing with appropriate sampling intervals.

### Critical Trend Points

| Point Type | Sampling Interval | Duration |
|------------|-------------------|----------|
| Space temperatures | 15 minutes | 7 days minimum |
| Supply air temperature | 5 minutes | 7 days minimum |
| Valve/damper positions | 5 minutes | 7 days minimum |
| Equipment status | Change of value | 7 days minimum |
| Power/energy | 15 minutes | 7 days minimum |

Analyze trends for:

- **Hunting**: Oscillating control signals indicate improper PID tuning
- **Setpoint deviation**: Persistent offset from setpoint reveals capacity or control issues
- **Simultaneous operation**: Heating and cooling active concurrently
- **Excessive cycling**: Equipment short cycling indicates oversizing or poor control

### Trend Analysis Example

A supply air temperature trend showing ±3°F oscillation with 8-minute period indicates excessive proportional gain. The control valve cycles fully open to closed rather than modulating smoothly. Resolution requires reducing proportional gain and potentially increasing integral time.

## Deficiency Tracking

Document all deficiencies discovered during FPT in a formal issues log per ASHRAE Guideline 0 requirements.

### Deficiency Classification

- **Critical**: Prevents system operation or creates safety hazard (immediate correction required)
- **Major**: System operates but fails to meet performance specifications (correction before substantial completion)
- **Minor**: System meets specifications but requires optimization (correction before final acceptance)

### Deficiency Log Format

Each entry must include:

1. Deficiency number and date identified
2. Equipment or system affected
3. Description of observed vs expected behavior
4. Classification level
5. Responsible party for correction
6. Target resolution date
7. Verification test required after correction
8. Resolution date and verification results

Deficiency resolution requires retesting the specific function that failed. Document pass/fail status in the log. Only after all critical and major deficiencies achieve passing retest results can commissioning proceed to acceptance.

Functional performance testing transforms static equipment installations into verified, integrated systems. The systematic application of equipment tests, integration verification, sequence validation, and trend analysis ensures HVAC systems deliver design performance throughout their operational life.
