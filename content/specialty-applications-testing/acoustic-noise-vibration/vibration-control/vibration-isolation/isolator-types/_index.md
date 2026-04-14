---
title: "Vibration Isolator Types for HVAC Equipment"
aliases: ["Vibration Isolator Types for HVAC Equipment"]
description: "Comprehensive guide to spring, neoprene, rubber, and air isolators for HVAC applications, including deflection characteristics, natural frequencies, and selection criteria."
keywords: ["vibration isolators", "spring isolators", "neoprene mounts", "air springs", "isolator deflection", "natural frequency", "equipment isolation", "vibration control"]
tags: ["vibration isolators", "spring isolators", "neoprene mounts", "air springs", "isolator deflection", "natural frequency", "equipment isolation", "vibration control"]
date: 2025-01-05
draft: false
weight: 1
---

Vibration isolators serve as the primary interface between rotating or reciprocating HVAC equipment and the supporting structure. Proper isolator selection requires understanding the mechanical characteristics, deflection behavior, and frequency response of each isolator type to achieve effective vibration attenuation.

## Fundamental Isolation Principles

The effectiveness of vibration isolation depends on the relationship between the equipment's operating frequency and the isolator's natural frequency. Maximum isolation occurs when:

$$\frac{f_{\text{operating}}}{f_{\text{natural}}} > \sqrt{2}$$

Where isolation efficiency increases as this ratio increases. The natural frequency of an isolated system relates directly to static deflection:

$$f_n = \frac{1}{2\pi}\sqrt{\frac{g}{\delta}} = \frac{3.13}{\sqrt{\delta}}$$

Where:
- $f_n$ = natural frequency (Hz)
- $g$ = gravitational acceleration (386 in/s²)
- $\delta$ = static deflection (inches)

This relationship demonstrates that greater deflection produces lower natural frequency and improved isolation at higher frequency ratios.

## Spring Isolators

Steel spring isolators provide predictable, linear load-deflection characteristics with minimal degradation over time. Springs maintain consistent stiffness across wide temperature ranges and resist chemical attack from oils and refrigerants.

### Deflection and Frequency Characteristics

| Static Deflection | Natural Frequency | Typical Application |
|-------------------|-------------------|---------------------|
| 0.5 inch | 4.4 Hz | Light equipment, minimal isolation |
| 1.0 inch | 3.1 Hz | Standard HVAC equipment |
| 1.5 inch | 2.6 Hz | Enhanced isolation |
| 2.0 inch | 2.2 Hz | Sensitive applications |
| 3.0 inch | 1.8 Hz | Critical isolation requirements |
| 4.0 inch | 1.6 Hz | Maximum commercial isolation |

Spring selection requires calculating required spring constant:

$$k = \frac{W}{\delta}$$

Where:
- $k$ = spring constant (lbf/in)
- $W$ = supported weight per isolator (lbf)
- $\delta$ = design deflection (inches)

### Spring Isolator Types

**Open springs** provide maximum deflection capability but require ancillary damping components. **Housed springs** incorporate internal damping mechanisms and limit hardware to control motion during startup and shutdown transients.

**Restrained spring isolators** include mechanical stops that limit upward movement during equipment shutdown, preventing excessive spring extension. Restraint engagement typically occurs at 50-75% of static deflection.

## Elastomeric Isolators

Elastomeric isolators use rubber compounds (natural or synthetic) or neoprene to provide both isolation and inherent damping in a compact package.

### Material Property Comparison

| Material | Durometer (Shore A) | Temperature Range | Chemical Resistance | Damping Coefficient |
|----------|---------------------|-------------------|---------------------|---------------------|
| Natural Rubber | 30-70 | -40°F to 180°F | Poor | 0.05-0.10 |
| Neoprene | 40-70 | -40°F to 200°F | Good | 0.05-0.12 |
| EPDM | 40-80 | -60°F to 300°F | Excellent | 0.04-0.08 |
| Nitrile | 50-80 | -30°F to 250°F | Excellent (oils) | 0.06-0.12 |
| Silicone | 30-80 | -100°F to 400°F | Good | 0.03-0.06 |

Elastomeric isolators exhibit nonlinear stiffness characteristics, with effective spring constant increasing under higher loads. The manufacturer's load-deflection curves must be consulted for accurate natural frequency calculations.

### Deflection Characteristics

Typical elastomeric isolator deflections range from 0.1 to 0.5 inches at rated load, corresponding to natural frequencies of 10 to 4.4 Hz. These higher natural frequencies provide adequate isolation only when equipment operates above 14-20 Hz (840-1200 rpm).

The effective stiffness of elastomeric materials in shear differs from compression:

$$k_{\text{shear}} = \frac{GA}{t}$$

Where:
- $G$ = shear modulus (typically 25-35% of compression modulus)
- $A$ = loaded area
- $t$ = material thickness

## Air Springs (Pneumatic Isolators)

Air springs provide superior low-frequency isolation through large deflections (2-8 inches) and extremely low natural frequencies (1-2 Hz). These systems maintain constant height through automatic leveling valves that compensate for load changes.

### Performance Characteristics

| Type | Deflection Range | Natural Frequency | Damping | Stability |
|------|------------------|-------------------|---------|-----------|
| Single Convolution | 2-4 inches | 1.5-2.5 Hz | Minimal | Good |
| Double Convolution | 4-8 inches | 1.0-1.8 Hz | Minimal | Fair |
| Triple Convolution | 6-12 inches | 0.8-1.5 Hz | Minimal | Poor |

The natural frequency of an air spring system depends on air volume and effective area:

$$f_n = \frac{1}{2\pi}\sqrt{\frac{A_e^2 \gamma P}{WV}}$$

Where:
- $A_e$ = effective piston area
- $\gamma$ = ratio of specific heats (1.4 for air)
- $P$ = absolute air pressure
- $W$ = supported weight
- $V$ = total air volume (spring + auxiliary tank)

Air springs require auxiliary equipment including air compressor, leveling valves, and pressure regulation, increasing initial cost and maintenance requirements. External damping must be added through viscous dampers or friction mechanisms.

## Isolator Selection Methodology

Selection proceeds through systematic analysis:

1. **Determine operating frequency**: Equipment speed (rpm) divided by 60
2. **Establish required isolation efficiency**: Typically 85-95% for HVAC applications
3. **Calculate maximum natural frequency**: $f_n = \frac{f_{\text{operating}}}{\sqrt{2 + \frac{1}{1-\eta}}}$ where $\eta$ is isolation efficiency
4. **Compute minimum deflection**: $\delta = \left(\frac{3.13}{f_n}\right)^2$
5. **Select isolator type** based on deflection, load, environment, and constraints
6. **Verify transmissibility**: $T = \frac{1}{\sqrt{\left(1-r^2\right)^2 + (2\zeta r)^2}}$ where $r = f_{\text{operating}}/f_n$ and $\zeta$ is damping ratio

## Application-Specific Considerations

**Roof installations** require consideration of wind loads and thermal expansion. Spring isolators with restrained housings prevent excessive motion during high winds.

**Seismic zones** necessitate restraints that allow normal vibration isolation while limiting displacement during seismic events. Snubbers engage only during extreme motion.

**Corrosive environments** favor stainless steel springs or non-metallic elastomeric isolators. Marine applications typically specify 316 stainless steel with protective coatings.

**Low-temperature applications** below 0°F require special elastomeric compounds or metallic springs, as standard rubber becomes brittle.

ASHRAE Handbook—HVAC Applications Chapter 49 provides comprehensive vibration isolation data including recommended deflections for various equipment types, isolation efficiencies at different frequency ratios, and installation details for optimal performance.

## References

- ASHRAE Handbook—HVAC Applications, Chapter 49: Noise and Vibration Control
- ASHRAE Handbook—HVAC Systems and Equipment, Chapter 48: Noise and Vibration
