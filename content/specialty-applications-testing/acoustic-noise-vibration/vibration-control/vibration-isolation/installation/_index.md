---
title: "Installation"
aliases: ["Installation"]
weight: 3
---

Proper installation of vibration isolation systems is critical for achieving design performance. Installation errors can completely negate the benefits of even the best-designed isolation systems.

## Isolator Selection and Specification

### Load Distribution

Isolators must be selected to carry the actual static load with appropriate safety factors:

| Load Condition | Safety Factor | Typical Application |
|----------------|---------------|---------------------|
| Static dead load | 1.25 minimum | Equipment weight only |
| Combined load | 1.5 minimum | Equipment + piping + access loads |
| Unbalanced load | 2.0 minimum | Fans with eccentric drives |

### Deflection Requirements

Static deflection determines natural frequency and isolation efficiency:

**Deflection-Frequency Relationship:**
```
fn = 3.13 / √δ

Where:
fn = natural frequency (Hz)
δ = static deflection (inches)
```

| Deflection | Natural Frequency | Isolation Efficiency at 600 RPM |
|------------|-------------------|----------------------------------|
| 0.1 in | 9.9 Hz | Poor (< 60%) |
| 0.5 in | 4.4 Hz | Moderate (75%) |
| 1.0 in | 3.1 Hz | Good (85%) |
| 2.0 in | 2.2 Hz | Excellent (> 90%) |

### Load Verification

Before installation, verify actual equipment weight:

1. Obtain certified weight from manufacturer
2. Account for motor, drives, and accessories
3. Calculate operating fluid weight (pumps, chillers)
4. Add estimated piping connection loads
5. Distribute total load equally among isolators

**Maximum load variation between isolators: 10%**

## Inertia Bases

Inertia bases provide mass and stiffness to maintain stability and distribute loads evenly across isolators.

### When Inertia Bases Are Required

- Equipment operating speed < 600 RPM
- High center of gravity (h/L > 0.5)
- Unbalanced loads (fans with belt drives)
- Multiple components on single platform
- Rocking mode concerns
- Soft isolation (> 1.5 inch deflection)

### Base Design Criteria

**Mass Requirements:**

Minimum base mass = 1.5 × equipment mass for speeds < 600 RPM
Minimum base mass = 1.0 × equipment mass for speeds > 1200 RPM

**Stiffness Requirements:**

Base deflection under load < isolator deflection / 10

Typical reinforced concrete: 150 lb/ft³ density

### Base Construction

**Concrete Inertia Bases:**

- Minimum thickness: 6 inches
- Reinforcement: #4 rebar at 12 inches on center both ways
- Concrete strength: 3000 psi minimum
- Cure time: 28 days before equipment installation
- Anchor bolt sleeves cast in place
- Leveling plates embedded flush with top surface

**Structural Steel Bases:**

- Welded construction, stress-relieved after fabrication
- Minimum thickness: 1/4 inch plate
- Internal cross-bracing for rigidity
- Filled with concrete or sand for mass
- Drilled and tapped holes for equipment mounting
- Lifting lugs for handling

### Housekeeping Pads

Provide clearance for isolators and prevent water accumulation:

- Height: 4-6 inches above finished floor
- Extend 3 inches beyond equipment base perimeter
- Non-shrink grout between pad and base
- Slope top surface for drainage if outdoors
- Do NOT bond rigidly to building structure

## Structural Considerations

### Floor Capacity Verification

Calculate total imposed load including impact factors:

Total Load = (Equipment + Base + Isolators) × 1.25

Verify floor capacity with structural engineer for:
- Point loads at isolator locations
- Distributed loads over equipment footprint
- Dynamic amplification at resonance (if applicable)

### Clearance Requirements

| Component | Clearance | Purpose |
|-----------|-----------|---------|
| Isolator height | Full deflection + 1 in | Allow movement |
| Lateral clearance | ± 0.5 in minimum | Thermal expansion |
| Overhead clearance | 2 in minimum | Piping flexibility |
| Seismic clearance | Per code | Earthquake displacement |

### Floor Stiffness

Isolators work effectively only when mounted to structures at least 10× stiffer than the isolator:

**Floor Deflection Limit:** δfloor < δisolator / 10

For long-span flexible floors, consider:
- Additional structural reinforcement
- Reduced isolator deflection
- Load distribution over larger area
- Coupled isolation (multiple points)

## Installation Procedures

### Pre-Installation Checklist

- Verify floor capacity and levelness (± 1/8 in per 10 ft)
- Confirm isolator model, quantity, and load rating
- Inspect isolators for shipping damage
- Check anchor bolt locations and embedment
- Ensure housekeeping pad is cured and level
- Verify clearances for piping and electrical

### Mounting Sequence

**For Spring Isolators:**

1. Position housekeeping pad and level to ± 1/16 inch
2. Place isolators at designated locations
3. Lower equipment/base onto isolators
4. Adjust leveling bolts to distribute load evenly
5. Measure isolator compression (should be equal ± 10%)
6. Tighten all mounting hardware
7. Remove shipping restraints and spacers
8. Verify free movement (no binding)

**For Elastomeric Isolators:**

1. Install anchor bolts in housekeeping pad
2. Position and level base or equipment
3. Insert isolators between base and pad
4. Torque mounting bolts to specification
5. Check level and adjust as needed
6. Verify uniform compression visually

### Load Balancing

After installation, verify load distribution:

**Spring Isolators:**
- Measure deflection at each isolator
- Calculate load: Load = k × δ (k = spring rate)
- Adjust leveling screws to equalize loads
- Repeat until all deflections within ± 10%

**Elastomeric Isolators:**
- Visual inspection for uniform compression
- Use feeler gauges to check gaps
- Shim as necessary to eliminate voids

### Anchor Bolt Torque

Apply manufacturer-specified torque to prevent loosening:

| Bolt Size | Torque (ft-lb) | Application |
|-----------|----------------|-------------|
| 1/4 in | 8-10 | Light equipment |
| 3/8 in | 20-25 | Medium equipment |
| 1/2 in | 45-55 | Heavy equipment |
| 5/8 in | 85-95 | Large equipment |
| 3/4 in | 130-150 | Chillers, large fans |

Use calibrated torque wrench and thread lubricant.

## Piping Connections

Rigid piping connections short-circuit vibration isolation. Flexible connections are mandatory.

### Flexible Connector Selection

**Rubber Expansion Joints:**
- Molded or hand-wrapped construction
- Single or multiple convolutions
- Working pressure: 150-300 psi typical
- Temperature limit: 250°F standard, 400°F high-temp
- Install within 1 pipe diameter of equipment
- Control rods limit movement to axial only

**Braided Flexible Hoses:**
- Stainless steel braid over corrugated core
- Working pressure: up to 3000 psi
- Excellent for vibration isolation
- Limited length (typically < 24 inches)
- Use on pump suction and discharge
- Orient to avoid sharp bends

**Metal Expansion Joints:**
- Single or multi-ply bellows
- High pressure and temperature capability
- Requires external restraints for pressure thrust
- Limited flexibility compared to rubber
- Use tie rods to prevent over-extension

### Installation Requirements

**Minimum Flexibility Length:**
- Pumps: 6 pipe diameters minimum
- Fans: 4 pipe diameters minimum
- Chillers: 8 pipe diameters minimum

**Piping Support:**

First rigid support must be located beyond flexible connector:
- Distance from equipment > 4 × pipe diameter
- Support from structure, NOT from equipment
- Allow piping to move freely with equipment
- Use spring hangers if piping is isolated

**Thrust Restraints:**

Flexible connectors transmit pressure thrust. Install restraints to prevent movement:
- Limit rods attached to equipment and piping
- Sized for pressure × area force
- Allow vibration transmission but prevent gross displacement
- Adjust clearance to 1/8 inch gap

### Duct Connections

Flexible duct connectors prevent structure-borne vibration transmission:

**Canvas Connectors:**
- Neoprene-coated fabric
- Temperature limit: 250°F
- Pressure: ±10 in w.g.
- Length: 4-6 inches minimum
- Install without wrinkles or folds

**Metal Flex Connectors:**
- Stainless steel construction
- High temperature (up to 1000°F)
- Length: 3-5 inches
- Avoid compression during installation

**Installation Details:**
- Support ductwork independently
- No metal-to-metal contact across connector
- Seal perimeter with mastic
- First rigid support > 3 duct diameters from equipment

## Seismic and Restraint Systems

### Snubbers

Snubbers allow normal vibration isolation but engage during seismic events:

- Gap: 1/4 to 1/2 inch typical
- Engagement force: > seismic lateral force
- Install in horizontal plane (N-S and E-W directions)
- Anchor to structure, not housekeeping pad
- Do NOT tighten against equipment during normal operation

### Seismic Restraints

Required by code in seismic zones:

**Restraint Load Calculation:**
```
Fp = 0.4 × ap × SDS × Wp × (1 + 2z/h)

Where:
Fp = lateral seismic force
ap = component amplification factor (2.5 for mechanical)
SDS = design spectral acceleration
Wp = component weight
z/h = elevation factor
```

**Installation:**
- Four-way restraint (two horizontal directions)
- Bolt to structure, not architectural elements
- Use ductile connections (avoid brittle failure)
- Clearance for normal vibration (1/4 in typical)
- Designed by licensed engineer in high seismic zones

### Floating Floors

For critical vibration control, isolate entire floor:

- Concrete slab on isolators
- Isolated from building structure
- All equipment mounted to floating floor
- Moat around perimeter (no contact with structure)
- Utilities enter through flexible penetrations

## Common Installation Errors

### Critical Mistakes to Avoid

**Short-Circuiting Isolation:**
- Rigid piping connections within 4 pipe diameters
- Metal-to-metal contact at flexible connectors
- Equipment base touching housekeeping pad sides
- Conduit or cable tray rigidly attached
- Drain lines solidly connected

**Load Problems:**
- Uneven load distribution (> 10% variation)
- Exceeding isolator capacity
- Insufficient safety factor
- Wrong isolator deflection for frequency

**Installation Issues:**
- Shipping restraints not removed
- Anchor bolts not torqued
- Isolators bound up or misaligned
- Base not level (> 1/8 in per 10 ft)
- Inadequate floor capacity

## Post-Installation Verification

### Commissioning Checks

1. **Visual Inspection:**
   - No rigid connections short-circuiting isolation
   - All shipping restraints removed
   - Clearances maintained around equipment
   - Flexible connectors properly installed

2. **Load Verification:**
   - Measure deflection at each isolator
   - Confirm ± 10% uniformity
   - Check anchor bolt torque

3. **Operational Testing:**
   - Start equipment and verify smooth operation
   - Check for unusual noise or vibration
   - Monitor for resonance at critical speeds
   - Confirm no contact during normal movement

4. **Vibration Measurements:**
   - Measure on isolated equipment
   - Measure on building structure nearby
   - Calculate isolation efficiency
   - Compare to design predictions

### Acceptance Criteria

| Parameter | Limit | Action if Exceeded |
|-----------|-------|-------------------|
| Load variation | ± 10% | Adjust leveling |
| Floor vibration | < 0.1 in/sec | Investigate short-circuit |
| Isolation efficiency | > design - 5% | Check installation |
| Resonance peak | < 2× design | Verify natural frequency |

## Maintenance Access

Design installation to permit routine maintenance:

- Isolators visible for inspection
- Deflection measurable without disassembly
- Flexible connectors accessible for replacement
- Anchor bolts reachable for re-torquing
- Equipment removable without isolator replacement
- Clearance for lifting equipment off isolators

Proper installation ensures vibration isolation system performance throughout the equipment lifecycle. Follow manufacturer instructions, industry standards, and these guidelines for optimal results.
