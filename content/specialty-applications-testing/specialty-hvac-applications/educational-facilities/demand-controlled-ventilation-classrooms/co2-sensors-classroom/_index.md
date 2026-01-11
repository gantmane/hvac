---
title: "CO2 Sensors for Classroom Ventilation Control"
description: "Technical guidance on NDIR CO2 sensor technology, placement strategies, calibration protocols, and control algorithms for demand-controlled ventilation in educational spaces."
date: 2025-01-05
draft: false
keywords:
  - CO2 sensors classroom
  - NDIR sensor technology
  - demand controlled ventilation
  - classroom air quality monitoring
  - CO2 sensor calibration
  - ASHRAE 62.1 sensors
  - ventilation control algorithms
  - indoor air quality sensors
weight: 1
---

## NDIR Sensor Technology

Non-dispersive infrared (NDIR) CO2 sensors represent the industry standard for classroom demand-controlled ventilation (DCV) applications due to their accuracy, stability, and long-term reliability. NDIR sensors operate on the principle that CO2 molecules absorb infrared radiation at a wavelength of 4.26 micrometers.

### Operating Principle

The sensor contains an infrared source, a sample chamber through which room air passes, and a detector filtered to the CO2 absorption wavelength. The reduction in transmitted infrared energy correlates directly to CO2 concentration through the Beer-Lambert Law:

$$A = \epsilon \cdot c \cdot l$$

where:
- $A$ = absorbance (dimensionless)
- $\epsilon$ = molar absorptivity (L·mol⁻¹·cm⁻¹)
- $c$ = CO2 concentration (mol·L⁻¹)
- $l$ = path length through sample chamber (cm)

The transmitted intensity relates to incident intensity through:

$$I = I_0 \cdot e^{-A}$$

Modern NDIR sensors incorporate dual-wavelength measurement, comparing the CO2-absorbing wavelength to a reference wavelength unaffected by CO2, which compensates for optical component aging and contamination.

## Sensor Specifications for Classroom Applications

Critical specifications for classroom CO2 sensors include:

| Parameter | Recommended Value | Rationale |
|-----------|------------------|-----------|
| Measurement range | 0-2000 ppm | Covers normal to high occupancy conditions |
| Accuracy | ±50 ppm or ±3% of reading | Maintains control precision |
| Response time (T90) | <120 seconds | Tracks occupancy changes |
| Drift | <50 ppm over 5 years | Minimizes calibration frequency |
| Operating temperature | 0-50°C | Accommodates all seasons |
| Operating humidity | 0-95% RH non-condensing | Prevents condensation damage |

## Sensor Placement Requirements

Proper sensor placement critically affects measurement accuracy and control system performance.

### Horizontal Positioning

Install sensors in the occupied zone, typically 3-6 feet above finished floor, representing breathing zone concentrations. Position sensors:

- Away from supply air diffusers (minimum 6 feet)
- Away from exhaust grilles (minimum 6 feet)
- Away from doors and operable windows (minimum 3 feet)
- In locations representative of average room conditions

### Vertical Stratification Considerations

CO2 density (1.98 kg/m³ at standard conditions) exceeds air density (1.20 kg/m³), creating potential for stratification in poorly mixed spaces. The concentration gradient under stratified conditions follows:

$$\frac{dc}{dz} = \frac{(c_{floor} - c_{ceiling})}{H}$$

where:
- $c$ = CO2 concentration (ppm)
- $z$ = height above floor (m)
- $H$ = room height (m)

Well-designed ventilation systems with adequate air mixing minimize stratification effects. Verify mixing effectiveness through tracer gas testing or measurement at multiple heights during commissioning.

## Control Algorithms

DCV systems modulate outdoor air supply based on CO2 concentration using proportional control:

$$\dot{V}_{oa} = \dot{V}_{oa,min} + K_p(c_{measured} - c_{setpoint})$$

where:
- $\dot{V}_{oa}$ = outdoor airflow rate (CFM)
- $\dot{V}_{oa,min}$ = minimum outdoor air per ASHRAE 62.1 (CFM)
- $K_p$ = proportional gain (CFM/ppm)
- $c_{measured}$ = measured CO2 concentration (ppm)
- $c_{setpoint}$ = target CO2 concentration (typically 1000-1100 ppm)

The proportional gain derives from occupant generation rate and target concentration differential:

$$K_p = \frac{N_{design} \cdot \dot{G}_{CO2}}{(c_{design} - c_{outdoor})}$$

where:
- $N_{design}$ = design occupancy (persons)
- $\dot{G}_{CO2}$ = CO2 generation rate per person (typically 0.31 L/min for sedentary adults, 0.19 L/min for children)
- $c_{design}$ = design indoor CO2 concentration (ppm)
- $c_{outdoor}$ = outdoor CO2 concentration (typically 400-450 ppm)

## ASHRAE 62.1 Requirements

ASHRAE Standard 62.1 permits DCV in spaces with variable occupancy exceeding 25 people per 1000 ft² and requires:

- CO2 sensors with accuracy of ±75 ppm
- Sensor location in the breathing zone
- Minimum outdoor air delivery regardless of CO2 level
- Outdoor air CO2 measurement or assumed value with 15% safety factor
- Sensor calibration per manufacturer recommendations

The standard recognizes that CO2 serves as an occupancy indicator, not a direct air quality metric, assuming occupants are the primary contaminant source.

## Calibration Protocols

### Automatic Background Calibration (ABC)

Many classroom sensors employ ABC logic, which assumes the sensor periodically experiences outdoor CO2 concentrations (typically 400 ppm). The algorithm identifies the minimum concentration measured over 7-14 days and adjusts calibration accordingly. ABC functions effectively in spaces unoccupied overnight and during weekends.

### Manual Calibration

Perform manual calibration:

- During initial installation
- Annually or per manufacturer recommendation
- When ABC is disabled or inappropriate
- After sensor replacement

Apply calibration gas (typically 1000 ppm CO2 in nitrogen) directly to sensor inlet following manufacturer procedures. Document calibration dates and adjustment values.

### Field Verification

Verify sensor accuracy quarterly using portable reference instruments traceable to NIST standards. Replace sensors exhibiting drift exceeding ±100 ppm.

## Maintenance Requirements

Establish maintenance protocols including:

- Visual inspection quarterly for physical damage and contamination
- Accuracy verification quarterly against reference instrument
- Sensor cleaning per manufacturer guidance (typically every 6-12 months)
- Firmware updates as released
- Replacement at manufacturer-specified interval (typically 10-15 years for quality NDIR sensors)

Document all maintenance activities in the building automation system or separate log.

## Common Implementation Issues

### Inadequate Air Mixing

Poor mixing causes spatial concentration gradients unrepresentative of average conditions. Verify air distribution patterns through testing or CFD analysis.

### Proximity to Contaminant Sources

Sensors near high-density seating or located where students congregate read artificially high concentrations. Select representative locations during design.

### Outdoor Air Reference Errors

Systems without outdoor air CO2 measurement that assume 400 ppm may overventilate in urban environments where outdoor concentrations reach 500-600 ppm, or underventilate in rural areas with lower baseline concentrations.

### Control System Integration

Ensure proper BACnet, Modbus, or analog signal integration between sensors and air handling unit controls. Verify control sequences through functional performance testing during commissioning.

## Performance Verification

Measure DCV system performance by:

1. Logging CO2 concentrations throughout occupied periods
2. Verifying outdoor air modulation correlates with measured CO2
3. Confirming minimum outdoor air delivery at all times
4. Validating energy savings compared to constant-volume operation

Properly implemented CO2-based DCV in classrooms typically reduces outdoor air heating and cooling loads by 20-40% while maintaining ASHRAE 62.1 compliance and occupant comfort.
