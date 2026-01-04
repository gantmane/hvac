---
title: "Transfer Functions"
description: "Mathematical analysis of HVAC control system dynamics using transfer functions, Laplace transforms, poles and zeros, and frequency domain representation for stability and performance evaluation."
date: 2026-01-04
weight: 3
---

Transfer functions provide a powerful mathematical framework for analyzing and designing control systems without solving differential equations in the time domain. By transforming system equations into the frequency domain using Laplace transforms, engineers can manipulate complex dynamic systems using algebraic operations. This approach enables systematic stability analysis, frequency response characterization, and controller design for HVAC applications.

## Laplace Transform Foundation

The Laplace transform converts time-domain functions into the complex frequency domain, simplifying the mathematics of differential equations. For a time-domain function $f(t)$, the Laplace transform is:

$$F(s) = \mathcal{L}\{f(t)\} = \int_0^\infty f(t) e^{-st} dt$$

Where $s = \sigma + j\omega$ represents the complex frequency variable with real part $\sigma$ and imaginary part $\omega$. Common Laplace transform pairs used in control analysis include:

- Unit step: $\mathcal{L}\{1\} = 1/s$
- Exponential decay: $\mathcal{L}\{e^{-at}\} = 1/(s+a)$
- Derivative: $\mathcal{L}\{df/dt\} = sF(s) - f(0)$
- Integral: $\mathcal{L}\{\int f dt\} = F(s)/s$

The derivative and integral properties transform differential equations into algebraic equations, greatly simplifying analysis. For HVAC systems with zero initial conditions, derivatives become simple multiplications by $s$.

## Transfer Function Definition

A transfer function represents the ratio of the Laplace transform of the output to the Laplace transform of the input, assuming zero initial conditions:

$$G(s) = \frac{Y(s)}{U(s)}$$

Where $Y(s)$ is the transformed output and $U(s)$ is the transformed input. This ratio characterizes the system's input-output behavior completely in the frequency domain.

For a first-order thermal process like a heating coil, the differential equation relating inlet temperature $T_{in}$ to outlet temperature $T_{out}$ is:

$$\tau \frac{dT_{out}}{dt} + T_{out} = K T_{in}$$

Taking Laplace transforms with zero initial conditions:

$$\tau s T_{out}(s) + T_{out}(s) = K T_{in}(s)$$

Solving for the transfer function:

$$G(s) = \frac{T_{out}(s)}{T_{in}(s)} = \frac{K}{\tau s + 1}$$

This transfer function completely describes the coil's dynamic temperature response without repeatedly solving the differential equation for different inputs.

## Poles and Zeros

Transfer functions can be expressed as ratios of polynomials in $s$:

$$G(s) = K \frac{(s - z_1)(s - z_2)...(s - z_m)}{(s - p_1)(s - p_2)...(s - p_n)}$$

The zeros $z_i$ are values of $s$ that make the numerator zero. The poles $p_i$ are values that make the denominator zero. The locations of poles and zeros in the complex plane determine the system's stability and dynamic characteristics.

Poles determine the modes of the system's natural response. For a first-order system $G(s) = K/(\tau s + 1)$, the single pole occurs at $s = -1/\tau$. A negative real pole produces exponential decay with time constant $\tau$. Poles with positive real parts produce exponentially growing responses, indicating instability.

Second-order systems have two poles that may be real or complex conjugates. Complex poles produce oscillatory responses with frequency determined by the imaginary part and decay rate determined by the real part. The damping ratio $\zeta$ and natural frequency $\omega_n$ relate directly to pole locations:

$$s_{1,2} = -\zeta \omega_n \pm j\omega_n\sqrt{1-\zeta^2}$$

Zeros affect the shape and magnitude of the response but not fundamental stability. A zero in the right half-plane produces inverse response or undershoot, where the output initially moves opposite to its final direction.

## System Response Characteristics

The transfer function completely determines the system's response to any input through the convolution theorem. For a step input of magnitude $A$, the output is:

$$Y(s) = G(s) \cdot \frac{A}{s}$$

Inverse Laplace transformation yields the time-domain step response. For the first-order system:

$$y(t) = AK(1 - e^{-t/\tau})$$

The steady-state gain equals $K$, obtained by evaluating $G(s)$ at $s = 0$. The time constant $\tau$ determines how quickly the response reaches steady state. After time $t = 3\tau$, the response reaches 95% of its final value.

Second-order systems exhibit ringing and overshoot depending on the damping ratio. Underdamped systems ($\zeta < 1$) oscillate before settling. Critically damped systems ($\zeta = 1$) reach steady state without oscillation in minimum time. Overdamped systems ($\zeta > 1$) approach steady state slowly without oscillation.

## Dead Time Representation

Dead time or transport delay represents the time between a control action and its observable effect. In HVAC systems, dead time arises from fluid transport in long pipes, sensor response delays, and actuator movement time. Dead time fundamentally limits control performance.

The transfer function for pure dead time $\theta$ is:

$$G_d(s) = e^{-\theta s}$$

This exponential term cannot be expressed as a ratio of polynomials, complicating analytical stability analysis. Approximations using Padé approximants convert the exponential to rational functions:

$$e^{-\theta s} \approx \frac{1 - \theta s/2}{1 + \theta s/2}$$ (first-order Padé)

This approximation enables standard analysis techniques while maintaining reasonable accuracy for $\omega \theta < 1$.

## Block Diagram Algebra

Block diagrams represent control systems as interconnections of transfer functions. Standard configurations include series (cascade), parallel (summing), and feedback arrangements. Block diagram algebra provides rules for simplifying complex systems into equivalent single transfer functions.

For systems in series, the overall transfer function equals the product of individual transfer functions:

$$G_{total}(s) = G_1(s) \cdot G_2(s) \cdot G_3(s)$$

For parallel paths with summing, the total transfer function equals the sum:

$$G_{total}(s) = G_1(s) + G_2(s)$$

For a negative feedback loop with forward path $G(s)$ and feedback path $H(s)$, the closed-loop transfer function is:

$$\frac{Y(s)}{R(s)} = \frac{G(s)}{1 + G(s)H(s)}$$

The denominator $1 + G(s)H(s)$ is called the characteristic equation. Its roots determine closed-loop stability.

## Frequency Response

Substituting $s = j\omega$ into the transfer function yields the frequency response, describing how the system responds to sinusoidal inputs at different frequencies. The magnitude $|G(j\omega)|$ indicates gain at each frequency, while the phase $\angle G(j\omega)$ indicates time shift.

For a first-order system $G(s) = K/(\tau s + 1)$:

$$|G(j\omega)| = \frac{K}{\sqrt{1 + (\omega\tau)^2}}$$

$$\angle G(j\omega) = -\arctan(\omega\tau)$$

At low frequencies ($\omega \ll 1/\tau$), the gain approaches $K$ and phase approaches 0°. At high frequencies ($\omega \gg 1/\tau$), the gain decreases as $1/\omega$ and phase approaches -90°. The break frequency $\omega = 1/\tau$ produces gain of $K/\sqrt{2}$ and phase of -45°.

Bode plots display magnitude (in decibels) and phase versus frequency (on logarithmic scale). These plots enable quick assessment of bandwidth, resonant peaks, and phase margins without detailed calculations.

## HVAC System Examples

A VAV box damper actuator typically behaves as a first-order system. If the actuator has a 30-second stroke time, the time constant is approximately $\tau = 10$ seconds. The transfer function relating command voltage to damper position is:

$$G(s) = \frac{K_{damper}}{10s + 1}$$

Where $K_{damper}$ converts voltage to position. The break frequency is $1/10 = 0.1$ rad/s or 0.016 Hz, indicating the actuator cannot respond to control signals faster than about one cycle per minute.

A room's thermal response to heating input can be modeled as first-order with time constant of 15-30 minutes depending on construction. This slow response allows conservative temperature control tuning:

$$G_{room}(s) = \frac{K_{thermal}}{1800s + 1}$$

Where the time constant of 1800 seconds (30 minutes) produces a break frequency of 0.00056 rad/s or 0.00009 Hz.

A chilled water coil with significant water volume and airflow creates a second-order response with potential for oscillation if the control valve modulates too aggressively. The transfer function might be:

$$G_{coil}(s) = \frac{K}{\tau^2 s^2 + 2\zeta\tau s + 1}$$

Proper valve authority and control tuning ensure adequate damping ($\zeta > 0.7$) to prevent temperature hunting.

## Controller Transfer Functions

PID controllers also have transfer functions. The ideal PID controller in the s-domain is:

$$G_c(s) = K_p + \frac{K_i}{s} + K_d s$$

The integral term $K_i/s$ has a pole at the origin, providing infinite gain at zero frequency to eliminate steady-state error. The derivative term $K_d s$ increases gain linearly with frequency, providing phase lead that improves stability.

Practical PID implementations include a filter on the derivative term to limit high-frequency gain:

$$G_c(s) = K_p + \frac{K_i}{s} + \frac{K_d s}{\tau_f s + 1}$$

Where $\tau_f$ is typically one-tenth the derivative time constant, rolling off derivative gain at high frequencies to reduce noise amplification.
