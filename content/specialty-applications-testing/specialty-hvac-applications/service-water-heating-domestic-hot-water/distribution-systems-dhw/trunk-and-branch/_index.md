---
title: "Trunk-and-Branch DHW Distribution Systems"
description: "Engineering analysis of trunk-and-branch domestic hot water distribution systems including pipe sizing methods, friction loss calculations, delivery times, and comparison with manifold systems."
keywords: ["trunk and branch piping", "DHW distribution", "domestic hot water sizing", "plumbing pipe sizing", "hot water delivery time", "graduated pipe sizing", "friction loss calculation", "fixture unit method"]
weight: 1
---

## Overview

Trunk-and-branch distribution represents the traditional method for domestic hot water (DHW) delivery in residential and commercial buildings. This system architecture uses progressively smaller pipe diameters as the main trunk line extends toward the farthest fixtures, with individual branches serving each fixture group. While manifold systems have gained popularity in recent construction, trunk-and-branch remains the dominant installed base and offers specific advantages in retrofit, high-flow applications, and cost-sensitive projects.

## System Architecture

The trunk-and-branch configuration consists of three hierarchical elements:

**Main Trunk Line**: A large-diameter pipe (typically 3/4" to 2" in residential applications) runs from the water heater along the longest path to serve multiple fixtures. The trunk maintains constant diameter until fixture branches reduce the downstream demand sufficiently to justify a pipe size reduction.

**Branch Lines**: Individual pipes tee off the trunk to serve fixture groups or single fixtures. Branch sizing depends on fixture demand and distance from the trunk.

**Graduated Sizing**: As fixtures are served along the trunk route, demand decreases, allowing pipe diameter reduction. This graduated approach minimizes material cost while maintaining adequate flow capacity.

```mermaid
graph LR
    WH[Water Heater<br/>120°F Supply] -->|1" Trunk| T1[Tee 1]
    T1 -->|3/4" Branch| F1[Kitchen Sink<br/>2.5 gpm]
    T1 -->|3/4" Trunk| T2[Tee 2]
    T2 -->|1/2" Branch| F2[Bathroom Lav<br/>1.5 gpm]
    T2 -->|3/4" Trunk| T3[Tee 3]
    T3 -->|1/2" Branch| F3[Shower<br/>2.0 gpm]
    T3 -->|1/2" Trunk| F4[Bathroom Lav<br/>1.5 gpm]

    style WH fill:#ff9999
    style F1 fill:#99ccff
    style F2 fill:#99ccff
    style F3 fill:#99ccff
    style F4 fill:#99ccff
```

## Pipe Sizing Methods

### Fixture Unit Method

The International Plumbing Code (IPC) and Uniform Plumbing Code (UPC) prescribe sizing based on fixture units, which correlate demand to pipe capacity:

$$Q_{design} = \sum_{i=1}^{n} FU_i \times C_{simultaneous}$$

Where:
- $Q_{design}$ = design flow rate (gpm)
- $FU_i$ = fixture unit value for each fixture
- $C_{simultaneous}$ = simultaneity factor (typically 0.6-1.0 for residential)

For copper Type L piping at 5 fps maximum velocity:

| Pipe Size | Maximum Fixture Units | Flow Capacity (gpm) |
|-----------|----------------------|---------------------|
| 1/2"      | 3                    | 4.0                 |
| 3/4"      | 8                    | 8.0                 |
| 1"        | 17                   | 15.0                |
| 1-1/4"    | 27                   | 25.0                |
| 1-1/2"    | 39                   | 35.0                |

### Pressure Drop Calculation

Friction loss in trunk-and-branch systems requires segment-by-segment calculation using the Hazen-Williams equation:

$$\Delta P = \frac{4.52 \times L \times Q^{1.852}}{C^{1.852} \times d^{4.87}}$$

Where:
- $\Delta P$ = pressure drop (psi)
- $L$ = pipe length (ft)
- $Q$ = flow rate (gpm)
- $C$ = roughness coefficient (150 for copper, 140 for PEX)
- $d$ = inside diameter (inches)

Total system pressure drop equals the sum of all segments in the critical path (longest run) plus fittings losses. Residual pressure at the farthest fixture must meet code minimum (typically 15-20 psi dynamic).

## Hot Water Delivery Time

A critical performance limitation of trunk-and-branch systems is extended wait time for hot water arrival at distant fixtures. The volume of water in the piping must be displaced before hot water reaches the fixture.

**Volume calculation:**

$$V_{pipe} = \frac{\pi d^2}{4} \times L \times 7.48 \, \text{gal/ft}^3$$

**Wait time:**

$$t_{wait} = \frac{V_{pipe}}{Q_{fixture}} \times 60 \, \text{sec/min}$$

For a 50-foot run of 3/4" copper (0.785" ID) to a lavatory flowing at 1.5 gpm:

$$V_{pipe} = \frac{\pi (0.785)^2}{4 \times 144} \times 50 \times 7.48 = 0.127 \, \text{gal}$$

$$t_{wait} = \frac{0.127}{1.5} \times 60 = 5.1 \, \text{seconds}$$

This calculation represents best case; actual wait times increase when considering cool-down between uses and heat loss to surroundings.

## Energy Waste Considerations

Water remaining in branch lines after fixture closure cools to ambient temperature, representing wasted energy and water. For a system with 200 feet of total hot water piping:

$$E_{waste} = \rho \times V_{total} \times c_p \times (T_{supply} - T_{ambient})$$

Annual energy waste depends on usage patterns but typically ranges from 5-15% of total water heating energy in residential applications without recirculation.

## Comparison: Trunk-and-Branch vs Manifold Systems

| Characteristic | Trunk-and-Branch | Manifold (PEX) |
|----------------|------------------|----------------|
| **Pipe Diameter** | Graduated (3/4" to 1-1/2") | Uniform (1/2" or 3/8") |
| **Fitting Count** | High (multiple tees) | Low (centralized) |
| **Water Volume** | Higher | Lower |
| **Delivery Time** | 5-20 seconds typical | 3-10 seconds typical |
| **Pressure Loss** | Moderate (fitting losses) | Higher (length, small diameter) |
| **Installation Complexity** | Moderate (accessible routes) | Low (continuous runs) |
| **Material Cost** | Lower (less pipe) | Higher (more total length) |
| **Balancing Difficulty** | Higher (interdependent branches) | Lower (independent runs) |
| **Flow Capacity** | Higher (larger pipes) | Limited (small diameter) |
| **Best Application** | Multi-bath, high flow demand | Single-family, moderate demand |

## Balancing and Flow Considerations

Trunk-and-branch systems exhibit pressure interdependence: when one fixture opens, downstream fixtures experience pressure increase while upstream fixtures see pressure decrease. This creates balancing challenges in multi-fixture simultaneous use scenarios, particularly in shower/tub combinations where temperature stability is critical.

Proper balancing requires:
1. Pressure-balancing or thermostatic mixing valves at shower fixtures
2. Equal friction loss to fixtures requiring simultaneous balanced flow
3. Adequate main trunk sizing to minimize velocity-induced pressure fluctuation

## Code Requirements

IPC Section 604 and UPC Section 610 govern minimum pipe sizing. Key requirements:

- Minimum branch size to fixtures: 3/8" (some codes require 1/2")
- Maximum velocity: 8 fps (5 fps recommended to reduce noise)
- Minimum fixture pressure: 15 psi dynamic (IPC), 8 psi (UPC)
- Support spacing: Maximum 6 feet horizontal for copper, 32 inches for PEX

## Installation Best Practices

1. **Route Planning**: Minimize trunk length by locating the water heater centrally relative to fixture groups
2. **Insulation**: Insulate all hot water piping to reduce standby losses and delivery time
3. **Slope**: Maintain slight slope (1/4" per 10 feet) for drainage during maintenance
4. **Access**: Provide access panels at critical tees for future service
5. **Expansion**: Install expansion compensation for runs exceeding 50 feet in copper or 30 feet in CPVC

## Conclusion

Trunk-and-branch distribution remains the standard DHW delivery method for its material efficiency, high flow capacity, and compatibility with diverse plumbing materials. Understanding graduated sizing principles, friction loss calculation, and delivery time implications enables proper system design. When hot water wait time presents concerns, consider recirculation loops or switching to manifold architecture for specific fixture groups while maintaining trunk-and-branch for high-demand areas.
