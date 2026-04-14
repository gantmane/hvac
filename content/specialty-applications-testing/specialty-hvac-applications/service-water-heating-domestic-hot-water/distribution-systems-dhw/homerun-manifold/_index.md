---
title: "Homerun Manifold DHW Distribution Systems"
aliases: ["Homerun Manifold DHW Distribution Systems"]
weight: 2
description: "Homerun manifold systems deliver hot water through dedicated PEX lines from a central manifold to each fixture, offering faster delivery, individual fixture isolation, and reduced fittings."
keywords: ["homerun manifold", "PEX tubing", "DHW distribution", "manifold plumbing", "domestic hot water", "fixture isolation", "parallel distribution", "residential plumbing"]
tags: ["homerun manifold", "PEX tubing", "DHW distribution", "manifold plumbing", "domestic hot water", "fixture isolation", "parallel distribution", "residential plumbing"]
---

Homerun manifold systems represent a parallel distribution approach where each plumbing fixture receives hot water through a dedicated line running directly from a central manifold. This architecture eliminates the complex branching networks of traditional trunk-and-branch systems, providing superior control, faster delivery, and simplified troubleshooting.

## System Architecture

The homerun manifold configuration consists of a central distribution point—the manifold—located near the water heater. From this manifold, individual supply lines run uninterrupted to each fixture throughout the residence. Each line features its own shutoff valve at the manifold, enabling complete fixture isolation without affecting other outlets.

```mermaid
graph LR
    WH[Water Heater] --> M[Central Manifold]
    M -->|3/8" PEX| F1[Kitchen Sink]
    M -->|1/2" PEX| F2[Master Shower]
    M -->|3/8" PEX| F3[Master Lav]
    M -->|1/2" PEX| F4[Guest Bath]
    M -->|3/8" PEX| F5[Laundry]
    M -->|1/2" PEX| F6[Dishwasher]

    style M fill:#e1f5ff
    style WH fill:#ffe1e1
```

**Manifold Components:**
- Central housing with 6-12 outlet ports (expandable)
- Individual ball valve for each outlet
- Pressure gauges and optional flow meters
- Hot and cold water inlets with isolation valves
- Mounting bracket for wall or floor installation
- Color-coded or labeled outlets for fixture identification

## Pipe Sizing and Friction Loss

Homerun systems typically use smaller diameter PEX tubing than trunk-and-branch configurations because each line serves only one fixture. The Darcy-Weisbach equation governs friction loss in these runs:

$$h_f = f \frac{L}{D} \frac{v^2}{2g}$$

Where:
- $h_f$ = friction head loss (ft)
- $f$ = friction factor (dimensionless, typically 0.007-0.009 for PEX)
- $L$ = pipe length (ft)
- $D$ = inside diameter (ft)
- $v$ = flow velocity (ft/s)
- $g$ = gravitational acceleration (32.2 ft/s²)

For a typical 50-ft run of 3/8" PEX (ID = 0.35") at 2 gpm:

$$v = \frac{Q}{A} = \frac{2 \text{ gpm} \times 0.00223}{π(0.35/24)^2} = 5.8 \text{ ft/s}$$

$$h_f = 0.008 \times \frac{50}{0.35/12} \times \frac{5.8^2}{2 \times 32.2} = 7.6 \text{ ft}$$

This friction loss translates to approximately 3.3 psi, which remains acceptable for most residential applications. The continuous, fitting-free runs minimize pressure drop compared to branched systems with multiple elbows and tees.

**Sizing Guidelines:**

| Fixture Type | Flow Rate | Recommended PEX Size | Maximum Run Length |
|--------------|-----------|----------------------|-------------------|
| Lavatory | 1.5 gpm | 3/8" | 100 ft |
| Kitchen Sink | 2.2 gpm | 1/2" | 80 ft |
| Shower | 2.5 gpm | 1/2" | 75 ft |
| Bathtub | 4.0 gpm | 1/2" | 60 ft |
| Dishwasher | 2.0 gpm | 3/8" | 90 ft |
| Washing Machine | 3.5 gpm | 1/2" | 65 ft |

## Performance Advantages

**Faster Hot Water Delivery:**
The smaller pipe volume in 3/8" or 1/2" homerun lines contains less water to purge before hot water reaches the fixture. A 50-ft run of 3/8" PEX holds only 0.21 gallons compared to 0.61 gallons in 3/4" trunk line, reducing wait time by approximately 65%.

**Individual Fixture Isolation:**
Each manifold outlet valve enables shutoff of specific fixtures for maintenance or repair without disrupting service to other locations. This eliminates the need to locate and operate multiple inline valves scattered throughout walls and ceilings.

**Reduced Fitting Failures:**
Continuous runs from manifold to fixture eliminate intermediate connections—the primary failure points in plumbing systems. A typical homerun installation uses 80-90% fewer fittings than equivalent trunk-and-branch layouts.

**Simplified Balancing:**
Flow to each fixture can be individually throttled at the manifold, enabling precise pressure balancing without accessing remote inline valves. This proves particularly valuable in systems with significant elevation differences or varying run lengths.

## System Comparison

| Characteristic | Homerun Manifold | Trunk-and-Branch |
|----------------|------------------|------------------|
| Pipe diameter | 3/8" - 1/2" PEX | 3/4" - 1" trunk, 1/2" branches |
| Number of fittings | Minimal (manifold connections only) | High (tees, elbows, couplings) |
| Water volume in pipes | 40-60% lower | Baseline |
| Installation labor | Lower (continuous runs) | Higher (multiple fitting joints) |
| Material cost | 15-25% higher (more total pipe length) | Lower |
| Repair accessibility | Excellent (valves at manifold) | Moderate (inline valves required) |
| Pressure balancing | Simple (manifold adjustment) | Complex (multiple valve locations) |
| Thermal efficiency | Better (less volume, faster delivery) | Good |
| Recirculation compatibility | Excellent (dedicated return possible) | Good |

## Installation Considerations

**Manifold Placement:**
Locate the central manifold within 10-15 feet of the water heater to minimize trunk line length. Install in accessible locations—mechanical rooms, basements, or utility closets—to enable future service. Mount at working height (48-60 inches) for comfortable valve operation.

**Routing Strategy:**
Route PEX tubing through floor joists, wall studs, or attic spaces using minimal bends. Maintain 12-inch spacing between hot and cold lines to prevent heat transfer. Secure tubing every 32 inches with plastic clips or hangers, avoiding metal fasteners that promote galvanic corrosion.

**Expansion Provisions:**
PEX tubing expands approximately 1.1 inches per 100 feet per 10°F temperature increase. Allow loops or bends at manifold connections to accommodate thermal movement. Never install PEX in tension.

**Insulation Requirements:**
Insulate all hot water homerun lines to R-3 minimum per IECC requirements. In unconditioned spaces, insulate to R-6 to prevent freezing and reduce standby losses. Use closed-cell foam pipe insulation with vapor barriers in humid climates.

**Water Hammer Protection:**
The small pipe diameters and high flow velocities in homerun systems can amplify water hammer effects. Install water hammer arrestors at fixtures with quick-closing valves (dishwashers, washing machines) or use manifolds with integral shock absorbers.

## Applications and Limitations

Homerun manifold systems excel in new construction where walls are open and routing flexibility maximizes efficiency. Single-story residences with centralized plumbing cores achieve the greatest benefits. Multi-story buildings require careful manifold placement or multiple manifolds per floor to maintain reasonable run lengths.

The system proves less cost-effective in retrofit applications where fishing continuous lines through existing walls generates excessive labor. Structures with widely dispersed fixtures may require prohibitively long runs, increasing both material costs and friction losses beyond practical limits.

For recirculation-equipped systems, homerun manifolds enable dedicated return lines from remote fixtures, creating efficient loops that minimize wait times while controlling energy consumption through precise zone control.
