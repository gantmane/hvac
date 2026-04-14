---
title: "IBC ASCE 7 Requirements"
aliases: ["IBC ASCE 7 Requirements"]
weight: 4
---

## Seismic Design Categories (SDC)

### SDC Classification

Buildings are assigned a Seismic Design Category (A through F) based on:

- Occupancy category (I, II, III, or IV)
- Mapped spectral response accelerations (Ss and S1)
- Site class (A through F)

**SDC Levels:**

| SDC | Seismic Risk | HVAC Requirements |
|-----|--------------|-------------------|
| A | Minimal | No seismic restraints required |
| B | Low | Limited restraint requirements |
| C | Moderate | Restraints required for equipment > 400 lb |
| D | High | Restraints required for equipment > 400 lb, enhanced detailing |
| E | Very High | Restraints required for equipment > 20 lb, stringent requirements |
| F | Near-fault | Restraints required for equipment > 20 lb, most stringent |

### Determination Process

1. Establish occupancy category from IBC Table 1604.5
2. Obtain mapped spectral accelerations Ss and S1 from ASCE 7 maps
3. Determine site class from geotechnical investigation
4. Calculate design spectral response accelerations SDS and SD1
5. Assign SDC from ASCE 7 Tables 11.6-1 and 11.6-2

## Component Importance Factor (Ip)

### Ip Values

The component importance factor reflects the hazard to human life and need for continued operation:

**Ip = 1.5:**
- Life safety components (fire suppression systems, emergency ventilation)
- Systems required for post-earthquake operation (hospital HVAC, emergency power cooling)
- Components containing hazardous materials
- High occupancy assembly spaces
- Essential facilities

**Ip = 1.0:**
- Standard commercial and residential HVAC equipment
- Non-essential components
- Standard occupancy buildings

### Application

The importance factor directly multiplies the seismic force:
- Higher Ip = larger design force
- More robust anchorage required
- Enhanced quality assurance during installation

## Seismic Design Force (Fp) Calculation

### Primary Equation

The horizontal seismic design force for nonstructural components:

**Fp = (0.4 × ap × SDS × Wp / Rp) × (1 + 2z/h) × Ip**

Where:
- Fp = component seismic design force
- ap = component amplification factor
- SDS = design spectral response acceleration (short period)
- Wp = component operating weight
- Rp = component response modification factor
- z = height of attachment point above grade
- h = building height (roof above grade)
- Ip = component importance factor

### Upper and Lower Limits

**Maximum Fp:**
Fp ≤ 1.6 × SDS × Ip × Wp

**Minimum Fp:**
Fp ≥ 0.3 × SDS × Ip × Wp

These limits prevent unreasonably high or low design forces regardless of calculated values.

### Component Amplification Factor (ap)

Typical values for HVAC equipment per ASCE 7 Table 13.5-1:

| Component Type | ap |
|----------------|-----|
| HVAC equipment on vibration isolators | 2.5 |
| HVAC equipment rigidly attached | 1.0 |
| Boilers and furnaces | 1.0 |
| Chillers | 1.0 |
| Air handlers | 2.5 |
| Fans | 2.5 |
| Suspended equipment (not on isolators) | 1.0 |

**Key Consideration:** Equipment on flexible supports (vibration isolators) experiences amplified motion, requiring larger seismic forces.

### Component Response Modification Factor (Rp)

Typical values for HVAC equipment per ASCE 7 Table 13.6-1:

| Component Type | Rp |
|----------------|-----|
| Mechanical equipment rigidly attached | 2.5 |
| Mechanical equipment on vibration isolators | 2.5 |
| Tanks and vessels | 2.5 |
| Piping systems (high deformability) | 3.5 |
| Piping systems (limited deformability) | 2.5 |
| Ductwork | 6.0 |

**Key Consideration:** Lower Rp = larger design force. Rp accounts for ductility and energy dissipation capacity.

## Height Factor (1 + 2z/h)

### Calculation

- z = elevation of component attachment above grade
- h = roof elevation above grade
- Ratio z/h ranges from 0 (ground level) to 1.0 (roof level)

**Examples:**

| Location | z/h | Factor (1 + 2z/h) |
|----------|-----|-------------------|
| Ground floor | 0 | 1.0 |
| Mid-height | 0.5 | 2.0 |
| Roof | 1.0 | 3.0 |

**Result:** Rooftop equipment experiences 3× the base seismic force due to building amplification effects.

## Anchorage Design Requirements

### Strength Design

Anchorage must resist:

**Horizontal Force:** Fp (calculated above)

**Vertical Force:** Typically 0.2 × SDS × Wp, applied concurrently

### Allowable Stress Design Conversion

If using allowable stress design (ASD) for anchors:

**Fp(ASD) = Fp / 1.4**

This converts load combinations from LRFD to ASD basis.

### Anchor Bolt Design

**Tensile Capacity:**
- Calculated per ACI 318 Chapter 17 (concrete) or AISC 360 (steel)
- Must account for concrete breakout, pullout, and steel yielding
- Apply appropriate reduction factors (φ)

**Shear Capacity:**
- Concrete pryout
- Steel strength
- Concrete edge distance effects

**Combined Loading:**
- Interaction equation: (T/φTn)^2 + (V/φVn)^2 ≤ 1.0
- Where T = applied tension, V = applied shear

### Concrete Anchor Requirements

**Minimum Edge Distance:**
- Typically 4× anchor diameter or per manufacturer
- Increased for anchors near slab edges

**Embedment Depth:**
- Minimum per ACI 318: typically 4× anchor diameter
- Cast-in-place anchors preferred over post-installed

**Reinforcement:**
- Supplementary reinforcement may be required for shallow embedments
- Anchor reinforcement detailed per ACI 318 Appendix D

### Base Plate Design

**Minimum Thickness:**
Calculate to prevent bending between anchor bolts:

t ≥ √(3 × M × L² / (Fy × W))

Where:
- M = moment between anchors
- L = span between anchors
- Fy = steel yield strength
- W = effective width

**Weld Requirements:**
- Full penetration welds for equipment legs to base plates
- Fillet welds sized for calculated forces
- AWS D1.1 requirements apply

## Drift Accommodation

### Relative Displacement

**Dp = (0.5 × SDS / Rp) × (z / h) × h**

This represents the differential displacement components must accommodate.

### Seismic Separation

Clearance required for:
- Piping penetrations through walls and floors
- Ductwork through seismic joints
- Equipment mounted across building joints

**Minimum Clearance:** 2 × Dp (both sides of joint)

### Flexible Connections

Required for:
- Utility lines crossing seismic joints
- Connections to equipment on vibration isolators
- Piping attached to equipment subject to differential movement

## Vertical Seismic Force

### Calculation

**Fv = 0.2 × SDS × Wp**

Applied concurrently with horizontal force for:
- Equipment on vibration isolators
- Suspended components
- Cantilever supports

### Load Combinations

**LRFD:** 1.2D ± Eh ± Ev
- D = dead load
- Eh = horizontal seismic effect (Fp)
- Ev = vertical seismic effect (Fv)

The ± indicates both upward and downward vertical forces must be considered.

## Component Period and Dynamic Analysis

### Qualifying Dynamic Equipment

Equipment requires dynamic analysis when:

| Condition | Requirement |
|-----------|-------------|
| SDC D, E, or F | Equipment weighs > 25% of building seismic weight |
| Flexible support | Natural frequency < 1.2× building frequency |
| Resonance risk | Equipment on upper floors of flexible structures |

### Simplified Period Calculation

For rigid equipment:

**T = 0.32 × √(W/k)**

Where:
- T = period (seconds)
- W = weight (lb)
- k = stiffness (lb/in)

### Testing Alternative

In lieu of calculation, equipment can be shake table tested per ICC-ES AC156 protocol.

## Certification and Documentation

### Design Professional Requirements

**SDC D, E, F:** Seismic restraint design must be performed by licensed engineer.

**SDC A, B, C:** Engineering may be required by authority having jurisdiction.

### Submittal Requirements

**Design Calculations:**
- Seismic force calculations (Fp)
- Anchorage design
- Base plate design
- Material specifications

**Installation Drawings:**
- Anchor layout
- Connection details
- Required torque values
- Special inspection requirements

### Special Inspection

**Required for SDC C and higher:**
- Anchor bolt installation verification
- Torque verification
- Visual inspection of welds
- Vibration isolator restraint installation

**Documentation:**
- Installation inspection reports
- Material certifications
- Anchor test reports (if post-installed)
- Final approval from engineer of record

## Acceptance Criteria

### Load Path Verification

Complete load path must exist from:
1. Equipment center of gravity
2. Through supports and base plates
3. Through anchors
4. Into structural elements

### Installation Tolerances

**Anchor Location:** ±0.5 inches from specified
**Bolt Torque:** Per manufacturer (typically 75% proof load)
**Base Plate Contact:** Minimum 80% full bearing
**Weld Quality:** Per AWS D1.1 acceptance criteria

## Exemptions

### Equipment Not Requiring Restraints

**SDC A:** No restraint requirements

**SDC B and C:**
- Equipment weighing ≤ 400 lb
- Attachments to light-frame construction

**All SDC:**
- HVAC equipment rigidly attached to structure that moves uniformly with equipment (e.g., small roof units with integral curbs adequately anchored)
