---
title: "Unit Ventilators"
description: "Detailed coverage of unit ventilator design, control sequences, face-bypass dampers, and classroom ventilation applications with psychrometric analysis."
date: "2026-01-04"
weight: 1
tags: ["unit ventilator", "classroom ventilation", "face bypass damper", "economizer cycle", "outdoor air control", "cycle II control"]
categories: ["Heating Systems"]
---

Unit ventilators serve perimeter spaces requiring dedicated outdoor air ventilation combined with heating and optional cooling. The equipment integrates an outdoor air damper, recirculation damper, heating coil, optional cooling coil, fan, and controls in a single factory-assembled cabinet. Educational facilities represent the primary application, where individual classroom control and code-mandated ventilation rates drive equipment selection.

## Physical Configuration

Unit ventilators mount below windows on exterior walls, utilizing short outdoor air intake ducts. Horizontal configurations measure 24-48 inches high, 48-120 inches wide, and 24-36 inches deep depending on capacity. Vertical configurations stack components vertically to reduce floor space requirements in retrofit applications.

The cabinet contains layered components in the airflow path:

1. **Outdoor air intake** with motorized damper and bird screen
2. **Return air inlet** with motorized damper
3. **Filter section** (MERV 8-13, typically 2-inch pleated)
4. **Face-and-bypass dampers** for capacity modulation
5. **Heating coil** (hot water, steam, or electric)
6. **Optional cooling coil** (chilled water or DX)
7. **Centrifugal fan** (forward-curved or backward-inclined)
8. **Discharge grille** with adjustable vanes

This arrangement minimizes mixing of outdoor and return air before the coils, improving freeze protection and control accuracy compared to central air handlers with long mixed air plenums.

## Capacity Ratings

Manufacturers rate unit ventilators by airflow (CFM), heating capacity (MBH), and optional cooling capacity (tons or MBH). Standard classroom units range from 400-1200 CFM with heating capacities of 20-80 MBH.

Heating capacity depends on entering air temperature, water temperature, and airflow:

$$Q_h = \dot{m}_{air} c_p (T_{out} - T_{in}) = \dot{m}_{water} c_p (T_{in,w} - T_{out,w})$$

For a 600 CFM unit with 180°F entering water temperature, 160°F leaving water temperature, and 40°F entering air temperature at design outdoor conditions:

$$Q_h = 600 \times 1.08 \times (110 - 40) = 45,360 \text{ Btu/hr}$$

The water-side calculation confirms:

$$\dot{m}_w = \frac{45,360}{500 \times (180-160)} = 4.5 \text{ GPM}$$

This assumes the standard approximation that $c_p \times \rho = 500$ Btu/(hr·GPM·°F) for water.

## Face-and-Bypass Damper Operation

Face-and-bypass dampers enable capacity modulation without varying airflow. The dampers direct air either through the heating coil (face position) or around it (bypass position). This maintains constant fan operation and room air circulation while varying heat output.

The capacity ratio equals the fraction of air passing through the coil:

$$Q_{actual} = Q_{max} \times \frac{\text{CFM}_{face}}{\text{CFM}_{total}}$$

Full bypass (0% through coil) provides ventilation air circulation without heating. Full face (100% through coil) delivers maximum capacity. Intermediate positions modulate output between these extremes.

Face-and-bypass control offers superior performance compared to cycling for several reasons:

- Maintains acoustic comfort by eliminating fan cycling noise
- Prevents temperature swings from on-off operation
- Enables economizer operation by varying outdoor air without capacity fluctuations
- Protects coils from freezing by maintaining airflow across coils during all operating modes

The damper linkage mechanically couples face and bypass dampers to ensure one closes as the other opens. Spring-return actuators default to bypass position on power failure, preventing coil freezing.

## Control Sequences

Unit ventilator control sequences progress through heating, economizer, and mechanical cooling modes based on outdoor temperature and space requirements. The standard three-cycle sequence defined in educational facility guidelines:

### Cycle I: Heating Mode

Operates when outdoor temperature falls below economizer lockout (typically 55-65°F). The sequence maintains space temperature through modulated heating while providing minimum outdoor air for ventilation.

**Damper Positions:**
- Outdoor air damper: Minimum position (typically 10-30% to meet ventilation codes)
- Recirculation damper: Open proportionally to maintain total airflow
- Face-bypass damper: Modulates based on space temperature

**Control Logic:**
The space thermostat positions the face-bypass damper. When space temperature falls below setpoint, the damper moves toward full face position, increasing capacity. As temperature rises, the damper moves toward bypass, reducing heat output.

### Cycle II: Economizer Mode

Engages when outdoor temperature rises above economizer lockout and space requires cooling. Free cooling through increased outdoor air percentage eliminates mechanical cooling energy.

**Damper Positions:**
- Outdoor air damper: Modulates from minimum to 100% based on cooling demand
- Recirculation damper: Closes as outdoor damper opens
- Face-bypass damper: Full bypass (no heating)

**Control Logic:**
As space temperature rises above setpoint, outdoor air damper opens to increase free cooling. If temperature continues rising with outdoor damper at 100%, the sequence transitions to Cycle III.

### Cycle III: Mechanical Cooling Mode

Activates when outdoor air cannot satisfy cooling load. The cooling coil provides additional capacity beyond economizer capability.

**Damper Positions:**
- Outdoor air damper: Minimum position to reduce cooling load
- Recirculation damper: Maximum open (economizer savings exhausted at this outdoor temperature)
- Face-bypass damper: Full bypass
- Cooling coil valve: Modulates based on space temperature

Some sequences maintain economizer operation during mechanical cooling if outdoor enthalpy remains below return air enthalpy. This requires enthalpy sensors rather than simple outdoor air temperature sensors.

## Psychrometric Analysis

The unit ventilator process appears on the psychrometric chart as a series of mixing and conditioning steps. For a classroom with:

- Outdoor air: 35°F, 80% RH
- Return air: 72°F, 40% RH
- Supply air target: 95-105°F
- Minimum outdoor air: 15 CFM per occupant × 25 occupants = 375 CFM
- Total airflow: 600 CFM
- Outdoor air fraction: 375/600 = 62.5%

The mixed air temperature before the heating coil:

$$T_{mixed} = T_{oa} \times f_{oa} + T_{ra} \times (1 - f_{oa})$$
$$T_{mixed} = 35 \times 0.625 + 72 \times 0.375 = 48.9°F$$

Required temperature rise across heating coil:

$$\Delta T = T_{supply} - T_{mixed} = 100 - 48.9 = 51.1°F$$

Heating capacity required:

$$Q_h = 600 \times 1.08 \times 51.1 = 33,113 \text{ Btu/hr}$$

This load varies throughout the day as outdoor conditions and occupancy change. Morning warm-up requires maximum capacity with minimum outdoor air (unoccupied mode). Occupied periods demand full ventilation air at potentially lower space temperatures.

## Minimum Outdoor Air Control

Modern unit ventilators incorporate demand-based ventilation using occupancy sensors or CO₂ monitors. The control logic adjusts minimum outdoor air damper position based on actual occupancy rather than maintaining design ventilation rates continuously.

Unoccupied mode reduces outdoor air to 0-10% to minimize heating energy while preventing stagnation. Occupied mode provides design ventilation rates (15-20 CFM per person for classrooms per ASHRAE 62.1). CO₂-based control modulates between these extremes, targeting 1000-1200 ppm CO₂ concentration.

The outdoor air damper requires minimum position limits to prevent closure during economizer operation. A 10% minimum prevents damper binding and maintains some outdoor air for pressurization even when ventilation is not required.

## Horizontal vs Vertical Units

**Horizontal units** orient components side-by-side along the exterior wall. Advantages include easier service access, lower discharge velocities, and more uniform air distribution. The low profile suits new construction where floor-to-ceiling heights accommodate the equipment without blocking windows.

**Vertical units** stack components vertically to reduce wall length requirements. This configuration suits retrofit projects in older buildings with limited wall space or architectural constraints. Vertical units discharge air upward or horizontally depending on fan placement, requiring careful selection to avoid drafts or short-circuiting.

Both configurations deliver equivalent performance when properly selected. The choice depends on available mounting space, architectural integration, and service access requirements.

## Acoustic Considerations

Classroom applications demand low noise levels for speech intelligibility. Unit ventilators generate noise from fan operation, damper movement, and airflow turbulence. Design strategies include:

- **Fan selection**: Forward-curved centrifugal fans operate at lower tip speeds than propeller fans, reducing noise by 5-10 dB
- **Discharge velocity**: Maintain velocities below 500 FPM at grilles to minimize turbulence noise
- **Damper seals**: Use low-leakage dampers with edge seals to prevent whistling from air bypass
- **Vibration isolation**: Internal isolation pads prevent cabinet vibration transmission to walls
- **Sound liner**: Acoustic liner on discharge plenums absorbs fan noise before room entry

Properly designed units operate at 35-45 dB(A) at the rated airflow, suitable for classroom environments requiring NC-30 to NC-35 sound levels.

Unit ventilators provide an effective solution for perimeter spaces requiring individual control, dedicated ventilation, and simple installation. The integration of heating, cooling, and ventilation functions with sophisticated control sequences enables energy-efficient operation across diverse climate conditions while maintaining indoor air quality and thermal comfort.
