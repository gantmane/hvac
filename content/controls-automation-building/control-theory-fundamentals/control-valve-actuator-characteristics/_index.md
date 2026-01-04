---
title: "Control Valve and Damper Characteristics"
description: "Analysis of control valve and damper flow characteristics including linear, equal percentage, and quick-opening types, valve authority, installed characteristics, and actuator selection for HVAC applications."
date: 2026-01-04
weight: 7
---

Control valves and dampers translate controller output signals into flow variations that regulate HVAC processes. The relationship between actuator position and resulting flow fundamentally affects control quality, stability, and energy efficiency. Understanding inherent and installed characteristics, valve authority, and proper actuator selection enables engineers to design control systems that maintain consistent performance across their operating range.

## Inherent Valve Characteristics

Inherent valve characteristics describe the relationship between valve stem position and flow coefficient under constant pressure drop conditions. Manufacturers test valves with fixed differential pressure, producing idealized curves that define the valve's fundamental behavior.

**Linear characteristic:** Flow varies proportionally with stem position. Equal increments of valve travel produce equal increments of flow:

$$\frac{Q}{Q_{max}} = \frac{x}{x_{max}}$$

Where $Q$ represents flow, $Q_{max}$ is maximum flow at full open position, $x$ is stem position, and $x_{max}$ is full travel. A linear valve at 50% open position passes 50% of maximum flow. This characteristic suits applications requiring consistent control sensitivity across the operating range.

**Equal percentage characteristic:** Each equal increment of valve travel produces a percentage change in flow proportional to the flow at the start of that increment. The flow relationship follows:

$$\frac{Q}{Q_{max}} = R^{(x/x_{max} - 1)}$$

Where $R$ represents the rangeability, typically 25 to 50 for control valves. At 50% travel, an equal percentage valve with rangeability 50 passes only 14% of maximum flow ($50^{-0.5} = 0.14$). This characteristic provides fine control at low flows and coarse control at high flows, compensating for the nonlinear relationship between flow and heat transfer in many HVAC applications.

**Quick-opening characteristic:** Maximum flow change occurs near the closed position. The valve provides most of its capacity within the first 25-30% of travel:

$$\frac{Q}{Q_{max}} \approx \sqrt{\frac{x}{x_{max}}}$$

Quick-opening valves suit on-off service or applications requiring rapid initial response. They provide poor modulating control due to excessive sensitivity near the closed position and minimal control at high flows.

**Modified characteristics:** Some valves blend linear and equal percentage behavior, providing approximately equal percentage at low flows and transitioning toward linear at high flows. These modified characteristics optimize control for specific applications.

## Installed Valve Characteristics

Installed characteristics describe actual flow behavior when the valve operates in a real system where pressure drop varies with flow. System resistance consumes a portion of available pressure, making installed characteristics differ significantly from inherent characteristics.

As flow increases, pressure drop across system components (pipes, coils, fittings) increases proportionally to flow squared. The pressure available to the valve decreases, reducing the valve's effectiveness at high flows. A linear valve exhibits equal percentage behavior when installed in a high-resistance system. An equal percentage valve becomes more linear.

Valve authority quantifies this deviation:

$$N = \frac{\Delta P_{valve,rated}}{\Delta P_{valve,rated} + \Delta P_{system,rated}}$$

Where $\Delta P_{valve,rated}$ represents the valve pressure drop at design flow with the valve wide open, and $\Delta P_{system,rated}$ represents the pressure drop through all other system components at design flow.

Valve authority ranges from 0 to 1. High authority (N > 0.5) indicates the installed characteristic closely matches the inherent characteristic. Low authority (N < 0.25) produces severe distortion, with marginal control at high flows and excessive sensitivity at low flows.

## Valve Authority and Control Quality

Proper valve authority ensures consistent control loop gain across the operating range. Low authority creates nonlinear gain, destabilizing control or producing sluggish response depending on operating conditions.

For a linear valve with authority N, the installed characteristic approximates:

$$\frac{Q}{Q_{max}} \approx \frac{x/x_{max}}{N + (1-N)(x/x_{max})}$$

At 50% valve position with authority N = 0.5, installed flow is 67% of maximum rather than the inherent 50%. At authority N = 0.25, installed flow increases to 80%, demonstrating the severe compression of control range.

Equal percentage valves require less authority than linear valves to maintain acceptable installed characteristics. Authority of 0.25-0.35 typically suffices for equal percentage valves, while linear valves demand 0.5 or higher. This explains why equal percentage valves predominate in HVAC applications where achieving high authority proves difficult due to coil pressure drops.

Achieving adequate authority requires:

- Selecting valves with lower $C_v$ (higher pressure drop at design flow)
- Using pressure-independent control valves with integral differential pressure regulators
- Designing systems with lower component pressure drops
- Accepting the energy penalty from higher pumping power to maintain valve pressure drop

The economic tradeoff balances first cost (larger pipes, lower pressure drop components) against operating cost (higher pumping power) and control quality requirements.

## Damper Characteristics

Damper flow characteristics differ fundamentally from valve characteristics due to the compressible nature of air and the wide variation in pressure drop with flow. The relationship between damper position and airflow depends on blade configuration, duct geometry, and system resistance.

**Opposed blade dampers:** Adjacent blades rotate in opposite directions, creating a more linear flow characteristic. At intermediate positions, the flow passage maintains relatively uniform restriction across the damper height. Opposed blade dampers provide better control than parallel blade configurations:

$$\frac{Q}{Q_{max}} \approx \left(\frac{x}{x_{max}}\right)^{0.8}$$

This approximate relationship holds for typical duct velocities and damper designs, though actual characteristics vary with blade count, seal quality, and Reynolds number.

**Parallel blade dampers:** All blades rotate in the same direction, creating preferential flow channels at intermediate positions. Flow increases rapidly in the first 30-40% of travel, then approaches maximum asymptotically:

$$\frac{Q}{Q_{max}} \approx 1 - \exp\left(-3\frac{x}{x_{max}}\right)$$

Parallel blade dampers suit isolation service where tight shutoff matters more than modulating control. Their poor control characteristics at intermediate positions make them unsuitable for applications requiring accurate flow modulation.

**Damper authority:** Similar to valves, damper authority compares damper pressure drop to total system pressure drop. Low authority dampers provide minimal control, particularly at high flows where most of the available pressure dissipates in ductwork and equipment.

Outdoor air dampers in economizer systems often exhibit poor authority because the duct and louver resistance exceeds the pressure available for control. Opposed blade construction and oversized dampers mitigate this limitation but cannot eliminate it entirely.

## Actuator Types and Characteristics

**Electric modulating actuators:** Drive valve or damper position based on analog control signals (0-10 VDC, 4-20 mA, or 0-135 ohm). Internal servo mechanisms compare commanded position to actual position measured by a potentiometer or encoder, adjusting motor drive to eliminate position error.

Stroke times range from 30 seconds to several minutes depending on actuator size and torque rating. Faster actuators respond more quickly to control signals but cost more and may produce mechanical stress on the valve or damper. Proper stroke time balances control requirements against mechanical considerations.

Electric actuators provide accurate, repeatable positioning with typical accuracy of ±1-2% of full span. They require electrical power at all times and may lack fail-safe capability unless equipped with battery backup or spring return mechanisms.

**Pneumatic modulating actuators:** Use compressed air (typically 3-15 psi signal range) to position a diaphragm or piston against a spring. Spring-return actuators fail to a predetermined position on air failure, providing inherent fail-safe operation critical for safety and equipment protection.

Pneumatic actuators respond more slowly than electric actuators due to air compressibility and controller output device limitations. Response times of 1-3 minutes are typical. This slower response suits many HVAC applications where thermal or flow processes exhibit long time constants.

Direct-acting pneumatic actuators extend with increasing air pressure. Reverse-acting actuators retract with increasing pressure. Proper selection ensures fail-safe position matches safety requirements—heating valves often fail closed while cooling valves may fail open or modulate to a mid-position.

**Two-position actuators:** Provide only fully open or fully closed positions with no intermediate modulation. These actuators suit on-off control where intermediate positions serve no purpose. Two-position electric actuators typically complete full travel in 15-60 seconds. Pneumatic two-position actuators stroke in 30-90 seconds depending on air capacity and valve size.

## Actuator Sizing and Selection

Actuator torque or thrust must exceed the maximum force required to move the valve or damper under worst-case conditions. For valves, the shutoff pressure differential creates the maximum force. For dampers, high velocity air imposes aerodynamic forces on the blades.

**Valve actuators:** Calculate required thrust from:

$$F = \frac{\pi d^2 \Delta P_{max}}{4}$$

Where $d$ is the valve plug diameter and $\Delta P_{max}$ is the maximum expected pressure differential. Include a safety factor of 1.25-1.5 to account for packing friction and aging effects. Select an actuator with rated thrust exceeding this value.

**Damper actuators:** Manufacturers specify required torque based on damper size, blade count, and maximum air velocity. Typical specifications provide torque in inch-pounds per square foot of damper area at design velocity. Multiply this value by damper area and apply a 1.25 safety factor.

Oversized actuators provide margin for unexpected conditions but cost more and may produce excessive wear from higher closing forces. Undersized actuators fail to fully stroke the valve or damper, degrading control quality and potentially creating safety hazards.

## Fail-Safe Position Selection

Fail-safe position determines valve or damper position when power or control signals are lost. Proper selection prevents equipment damage, maintains safety, and limits discomfort during failures.

**Heating valves:** Typically fail closed to prevent overheating, freeze damage from burst heating coils, or energy waste. Spring-return actuators with springs sized to close the valve on air or power loss provide reliable fail-closed operation.

**Cooling valves:** May fail open, closed, or mid-position depending on the application. In critical cooling applications (data centers, process cooling), fail-open maintains some cooling during control failures. In comfort cooling, fail-closed prevents energy waste. Some systems fail to mid-position, providing partial capacity.

**Outdoor air dampers:** Usually fail closed to prevent infiltration during power failures and to minimize heating or cooling load during economizer control failure. However, life safety codes may require fail-open for smoke evacuation or to ensure minimum ventilation.

**Return air dampers:** Coordinate with outdoor air dampers to maintain total airflow. If outdoor air fails closed, return air should fail open (if they're not on the same shaft).

The fail-safe logic must consider the entire system including pumps, fans, and other control valves. A comprehensive failure mode analysis identifies potential hazards and establishes appropriate fail-safe positions for all controlled devices.

## Rangeability and Turndown

Rangeability defines the ratio of maximum to minimum controllable flow. A valve with 50:1 rangeability can modulate flow from 2% to 100% of maximum capacity with acceptable accuracy. Below the minimum controllable flow, the valve exhibits excessive sensitivity or poor repeatability.

Equal percentage valves provide superior rangeability compared to linear valves. The exponential characteristic maintains reasonable control sensitivity even at very low flows. Linear valves lose sensitivity at low flows as small position changes produce minimal flow variation.

Applications requiring wide turndown (100:1 or greater) may need oversized equal percentage valves or special characterized valves. VAV systems, for example, must modulate from design airflow down to minimum ventilation requirements, often demanding 10:1 or greater turndown.

Improper valve sizing that produces excessive rangeability (valve much larger than necessary) creates low authority and poor installed characteristics. The optimal valve size balances adequate rangeability against maintaining reasonable authority and installed characteristics.

Understanding valve and damper characteristics enables proper selection, sizing, and installation to ensure stable, accurate control across the full operating range. This knowledge transforms control system design from trial-and-error to systematic engineering based on fundamental principles.
