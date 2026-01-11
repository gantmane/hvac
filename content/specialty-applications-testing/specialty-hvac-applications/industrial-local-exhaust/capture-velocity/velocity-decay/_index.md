---
title: "Velocity Decay in Industrial Exhaust Hood Design"
description: "Principles of velocity decay in industrial local exhaust ventilation, including distance effects, centerline decay rates, and hood placement for effective contaminant capture."
keywords: ["velocity decay", "capture velocity", "hood design", "exhaust ventilation", "industrial ventilation", "velocity profiles", "hood placement", "local exhaust"]
weight: 10
---

Velocity decay describes the rapid reduction in air velocity as distance increases from an exhaust hood face. Understanding velocity decay principles is fundamental to proper hood placement and effective contaminant capture in industrial local exhaust ventilation systems.

## Velocity Decay Principles

Air velocity at any point in front of an exhaust hood decreases proportionally to the square of the distance from the hood opening. This relationship follows the inverse square law, which governs the three-dimensional expansion of air flowing toward a hood.

For a simple unflanged circular or rectangular opening, the centerline velocity at distance $X$ from the hood face is:

$$V_x = \frac{V_{face}}{(10X^2/A + 1)}$$

Where:
- $V_x$ = velocity at distance $X$ from hood face (fpm)
- $V_{face}$ = face velocity at hood opening (fpm)
- $X$ = distance from hood face (ft)
- $A$ = hood face area (ft²)

This equation demonstrates that velocity decreases rapidly with increasing distance, making effective capture possible only within a limited zone in front of the hood.

## Centerline Velocity Decay Rates

The centerline velocity decay follows predictable patterns based on hood geometry and configuration. For practical applications, velocity at one hood diameter distance from an unflanged circular hood face is approximately 10% of face velocity. At two diameters distance, velocity drops to approximately 3% of face velocity.

The decay rate is more pronounced for smaller hoods. A hood with 1 ft² face area exhibits faster velocity decay than a hood with 4 ft² face area at the same volumetric flow rate, even though the smaller hood has higher face velocity.

{{< mermaid >}}
graph LR
    A[Hood Face<br/>V = 100%] -->|1 Diameter| B[V ≈ 10%]
    B -->|1 Diameter| C[V ≈ 3%]
    C -->|1 Diameter| D[V ≈ 1.5%]

    style A fill:#ff6b6b
    style B fill:#ffd93d
    style C fill:#6bcf7f
    style D fill:#4d96ff
{{< /mermaid >}}

## Flanged vs Unflanged Hood Comparison

Flanges significantly improve hood performance by eliminating flow from behind the hood, effectively converting the opening from a sphere of influence to a hemisphere. This modification increases the effective capture velocity at any given distance.

For flanged hoods, the centerline velocity equation becomes:

$$V_x = \frac{V_{face}}{(5X^2/A + 1)}$$

The coefficient changes from 10 to 5, indicating that flanged hoods provide approximately twice the velocity at any given distance compared to unflanged hoods with identical face velocity and area. This represents a substantial improvement in capture efficiency without increasing airflow requirements.

### Velocity Decay Comparison Table

| Hood Type | Distance (Hood Diameters) | Velocity (% of Face Velocity) |
|-----------|---------------------------|-------------------------------|
| Unflanged Round | 0.5 | 29% |
| Unflanged Round | 1.0 | 10% |
| Unflanged Round | 2.0 | 3% |
| Flanged Round | 0.5 | 44% |
| Flanged Round | 1.0 | 17% |
| Flanged Round | 2.0 | 5% |
| Unflanged Rectangular | 0.5 | 27% |
| Unflanged Rectangular | 1.0 | 9% |
| Flanged Rectangular | 0.5 | 42% |
| Flanged Rectangular | 1.0 | 16% |

## Slot Hood Velocity Characteristics

Slot hoods exhibit different velocity decay characteristics due to their elongated geometry. The flow pattern approaches two-dimensional rather than three-dimensional expansion, resulting in slower velocity decay along the slot centerline perpendicular to the slot length.

For slot hoods, velocity decay follows approximately:

$$V_x = \frac{V_{face}}{(3.7X/W + 1)}$$

Where $W$ is the slot width. This linear relationship (rather than inverse square) means slot hoods maintain effective capture velocity over greater distances compared to circular or rectangular hoods of equivalent area. However, this advantage applies only in the direction perpendicular to the slot length. Velocity decay along the slot length follows standard three-dimensional expansion principles.

## Effect of Distance from Hood Face

Distance from the hood face is the single most critical factor affecting capture velocity. Because velocity decreases with the square of distance (or linearly for slot hoods), even small increases in distance dramatically reduce capture effectiveness.

A contaminant source located 6 inches from an unflanged hood experiences approximately four times the capture velocity compared to the same source at 12 inches. This relationship emphasizes the importance of positioning hoods as close as practically possible to contaminant generation points.

Cross-drafts and thermal currents become increasingly dominant as distance from the hood increases. At distances where hood-induced velocity drops below 50-100 fpm, ambient air movements typically overpower the hood's capture capability.

## Implications for Hood Placement

Understanding velocity decay principles leads to specific hood placement guidelines:

**Minimize Distance**: Position hoods within one hood diameter (or width for slots) of the contaminant source whenever possible. Beyond this distance, capture efficiency degrades rapidly.

**Use Flanges**: Install flanges on all hoods unless physical constraints prevent it. The velocity improvement justifies the minimal additional cost and complexity.

**Consider Enclosure**: When contaminant sources cannot be positioned close to hoods, partial or full enclosure reduces the effective distance and shields the capture zone from cross-drafts.

**Account for Process Variability**: If source position varies during operation, size and position the hood based on the worst-case (farthest) position, not the typical or best-case position.

**Evaluate Cross-Draft Effects**: Calculate the ratio of capture velocity to cross-draft velocity at the contaminant source location. Ratios below 2:1 indicate inadequate capture capability.

**Document Assumptions**: Record assumed source-to-hood distances in design documentation, as this parameter critically affects system performance and provides essential information for future modifications or troubleshooting.

Velocity decay represents a fundamental physical limitation in local exhaust ventilation. Successful hood design requires recognition of these limitations and design approaches that minimize their impact through proper positioning, flanging, and when necessary, enclosure strategies.
