---
title: "PID Control Detailed"
description: "In-depth analysis of proportional-integral-derivative control algorithms for HVAC applications including mathematical formulation, control modes, tuning methods, and implementation considerations."
date: 2026-01-04
weight: 2
---

Proportional-Integral-Derivative control represents the most prevalent algorithm in HVAC control systems, providing a versatile framework that balances responsiveness, accuracy, and stability. The PID controller combines three complementary control actions, each addressing different aspects of dynamic system behavior. Understanding the individual contributions and interactions of these terms enables effective tuning and troubleshooting of HVAC control loops.

## Mathematical Formulation

The continuous-time PID control algorithm computes the controller output as:

$$u(t) = K_p e(t) + K_i \int_0^t e(\tau) d\tau + K_d \frac{de(t)}{dt}$$

Where $u(t)$ represents the controller output, $e(t)$ is the control error, $K_p$ is the proportional gain, $K_i$ is the integral gain, and $K_d$ is the derivative gain. Each term contributes a distinct component to the total control action.

Alternative formulations express the same algorithm using different parameter sets. The time-constant form writes:

$$u(t) = K_p \left[ e(t) + \frac{1}{T_i} \int_0^t e(\tau) d\tau + T_d \frac{de(t)}{dt} \right]$$

Where $T_i$ represents the integral time constant (or reset time) and $T_d$ represents the derivative time constant (or rate time). The relationship between forms follows: $K_i = K_p / T_i$ and $K_d = K_p T_d$.

Digital controllers implement discrete-time versions using sampled error values:

$$u_n = K_p e_n + K_i \Delta t \sum_{k=0}^n e_k + K_d \frac{e_n - e_{n-1}}{\Delta t}$$

Where subscript $n$ denotes the current sample, $\Delta t$ represents the sampling interval, and the integral approximates as a sum while the derivative becomes a difference quotient.

## Proportional Control Action

The proportional term produces an output directly proportional to the current error magnitude. When error increases, proportional action increases proportionally. When error decreases, the output decreases proportionally. This immediate response to error changes provides the primary control action.

The proportional gain $K_p$ determines the strength of proportional action. Higher gains produce larger output changes for the same error, resulting in more aggressive control. Lower gains produce gentler responses that may be more stable but slower.

The throttling range or proportional band quantifies the error range that drives the controller output from minimum to maximum. For a controller with 0-100% output range and proportional gain $K_p = 5$ %/°F, the throttling range equals $100\% / 5 = 20°F$. An error of ±10°F drives the output across its full range.

Proportional-only control exhibits a fundamental limitation: steady-state offset. The controller requires a non-zero error to maintain a non-zero output. If the process requires 60% valve opening to maintain setpoint, the proportional controller must operate with a permanent error of $60\% / K_p$. This offset explains why pure proportional control rarely appears in HVAC temperature control, though it finds application in processes where small offsets are acceptable.

## Integral Control Action

The integral term accumulates error over time, continuously increasing or decreasing based on the sign of the error. Even small persistent errors eventually produce large integral contributions, driving the controlled variable toward the setpoint. This error accumulation eliminates steady-state offset, the primary limitation of proportional-only control.

The integral gain $K_i$ determines how quickly the integral term accumulates. Higher integral gains cause faster accumulation, eliminating offset more quickly but risking overshoot and oscillation. Lower integral gains accumulate slowly, ensuring stability but allowing prolonged deviations.

Integral windup occurs when the integral term accumulates to large values during periods when the actuator saturates at its limits. When conditions change and the actuator can again respond, the large accumulated integral causes excessive overshoot. Anti-windup mechanisms prevent or limit integral accumulation when the output saturates, improving performance during startup, shutdown, and large disturbances.

The integral time constant $T_i$ (reset time) represents the time required for the integral action to duplicate the proportional action's contribution. Smaller time constants produce faster integration, while larger time constants slow integration. Typical HVAC applications use integral time constants ranging from 1 to 20 minutes depending on process dynamics.

## Derivative Control Action

The derivative term responds to the rate of error change rather than error magnitude. When error increases rapidly, derivative action provides additional output to counteract the change. When error approaches setpoint, the derivative term reduces output to prevent overshoot. This anticipatory action improves stability and allows more aggressive proportional and integral gains.

The derivative gain $K_d$ determines the strength of derivative action. Higher derivative gains provide stronger damping of oscillations and faster settling. Excessive derivative gain amplifies measurement noise, potentially causing erratic controller behavior.

Derivative action operates on the rate of error change, making it sensitive to sudden setpoint changes that create instantaneous infinite derivatives. To prevent derivative kick, many implementations compute the derivative of the measured variable rather than the error:

$$u(t) = K_p e(t) + K_i \int_0^t e(\tau) d\tau - K_d \frac{dy(t)}{dt}$$

This modification eliminates derivative kick during setpoint changes while preserving derivative response to disturbances affecting the measured variable.

Derivative filtering reduces noise sensitivity by applying a first-order filter to the derivative term. The filtered derivative smooths rapid fluctuations while preserving response to genuine trend changes. The filter time constant typically ranges from one-tenth to one-fifth of the derivative time constant.

## Control Mode Combinations

PI control combines proportional and integral actions, providing the most common configuration in HVAC applications. The proportional term ensures immediate response, while the integral term eliminates offset. This combination suits most temperature, pressure, and flow control loops with moderate dynamics and acceptable noise levels.

PD control combines proportional and derivative actions without integral terms. This configuration provides fast response with good damping but accepts steady-state offset. PD control suits level control or position control applications where offset is acceptable or where external integration inherently exists.

PID control combines all three terms, offering maximum flexibility. The derivative term allows more aggressive proportional and integral gains than PI control alone, improving response speed and disturbance rejection. However, derivative action's noise sensitivity requires careful implementation and may be inappropriate for noisy measurements.

P-only control applies only proportional action, accepting steady-state offset. This simple approach suits applications with inherent integration or where small offsets are acceptable. Positioning control and some flow control applications use P-only control successfully.

## Practical Implementation Considerations

Controller output limits constrain the manipulated variable within physical actuator ranges. A control valve operates between fully closed (0%) and fully open (100%). Controller output must clip to these limits, preventing impossible command values. When output saturates at limits, the control loop operates open-loop until conditions change to bring the output back into range.

Bumpless transfer ensures smooth transitions when switching between automatic and manual control modes. Without bumpless transfer, switching from manual to automatic can cause sudden output changes if the manual output differs from the automatic calculation. Proper implementation initializes the integral term to match the current output, preventing discontinuous jumps.

Output rate limiting restricts how quickly the controller output can change, protecting actuators and processes from excessive slew rates. While rate limiting improves mechanical reliability, it degrades control performance by limiting the controller's ability to respond quickly. Rate limits should be set as loose as mechanical constraints allow.

Dead bands define regions around the setpoint where the controller produces no output change. Small dead bands reduce actuator wear from continuous hunting without significantly degrading control quality. However, excessive dead bands create larger deviations and slower disturbance rejection.

## Tuning Parameter Interactions

The three PID gains interact in complex ways that affect overall system performance. Increasing proportional gain speeds response but reduces stability margins and increases steady-state offset for P-only control. Adding integral action eliminates offset but can destabilize the loop if the integral gain is too high. Derivative action stabilizes the loop and permits higher proportional and integral gains.

Typical tuning sequences adjust parameters iteratively. Starting with integral and derivative gains at zero, increase proportional gain until the response exhibits slight oscillation. Reduce proportional gain by 30-50% for margin. Add integral action gradually until offset disappears without excessive overshoot. If oscillations persist, reduce integral gain or increase proportional band. Finally, add derivative action if needed to improve damping and enable more aggressive tuning.

The optimal balance depends on application priorities. Temperature control emphasizes stability and comfort over rapid response. Pressure control in supply ducts requires fast response to prevent excessive pressure variations. Flow control balances response speed against valve wear.

## HVAC Application Examples

Discharge air temperature control typically uses PI control with moderate gains. The thermal mass of the coil and ductwork provides some inherent damping. Integral time constants of 5-10 minutes suit typical air handling unit dynamics. Derivative action is rarely necessary due to slow thermal response and potential noise from air turbulence.

Static pressure control in VAV systems employs PI control with faster response than temperature control. Pressure dynamics respond more quickly than thermal processes, requiring faster integral action. Integral time constants of 1-3 minutes prevent excessive pressure fluctuations while avoiding oscillations.

Chilled water valve control on cooling coils uses PI or PID control. The derivative term can improve response to rapid load changes while dampening hunting. However, derivative gain must remain moderate to avoid amplifying noise from turbulent water flow and temperature sensor fluctuations.

Zone temperature control in terminal units operates with PI control tuned conservatively. Occupant comfort prioritizes stability over rapid setpoint tracking. Integral time constants of 10-20 minutes provide gradual adjustment without oscillation. The slow tuning also accommodates the long thermal time constants of building spaces.
