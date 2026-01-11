---
title: "Equipment Anchorage for Hurricane Resistance"
description: "Engineering principles for anchoring HVAC equipment against hurricane forces, covering ACI 318 anchor design, combined wind-seismic loads, and structural attachment methods."
date: 2025-01-05
keywords:
  - equipment anchorage
  - hurricane resistant HVAC
  - concrete anchor design
  - ACI 318
  - wind load anchorage
  - seismic anchorage
  - structural attachments
  - anchor force calculations
weight: 2
---

Proper equipment anchorage is critical for maintaining HVAC system integrity during hurricane events. Anchorage systems must resist combined wind uplift, overturning moments, and lateral forces while maintaining structural integrity under extreme loading conditions.

## Anchorage Force Calculations

### Design Wind Forces

Equipment anchorage forces derive from ASCE 7 wind pressure calculations applied to exposed surfaces. The total design force considers both horizontal and vertical components:

$$F_h = q_h G C_f A_f$$

where:
- $F_h$ = horizontal wind force (lb)
- $q_h$ = velocity pressure at equipment height (psf)
- $G$ = gust effect factor (typically 0.85 for rigid equipment)
- $C_f$ = net force coefficient (1.4-2.0 for rectangular equipment)
- $A_f$ = projected area normal to wind (ft²)

Vertical uplift forces result from negative pressure coefficients on horizontal surfaces:

$$F_v = q_h G C_p A_p$$

where $C_p$ represents the external pressure coefficient (typically -1.8 to -2.2 for roof-mounted equipment).

### Overturning Analysis

Overturning moments about the anchorage points require evaluation of the force distribution. For equipment with height $h$ and width $b$:

$$M_{ot} = F_h \cdot \frac{h}{2} + F_v \cdot \frac{b}{2}$$

The required anchor tension force per anchor (assuming $n$ anchors):

$$T_{anchor} = \frac{M_{ot}}{b \cdot \frac{n}{2}} - \frac{W_{eq}}{n}$$

where $W_{eq}$ is the equipment dead load providing resisting moment.

### Combined Wind and Seismic Loading

ASCE 7 Section 12.4.3 addresses combined loading. For equipment, the controlling load combination typically follows:

$$(0.9 - 0.2S_{DS})D + \rho Q_E$$

or

$$1.2D + f_1L + 0.5W + \rho Q_E$$

where $S_{DS}$ is the design spectral response acceleration, $\rho$ is the component redundancy factor (1.3 or 1.5), and $Q_E$ represents seismic forces.

In hurricane-prone regions with moderate seismic hazard, evaluate both combinations. The wind load combination frequently governs for rooftop equipment due to high exposure.

## Concrete Anchor Design

### ACI 318 Chapter 17 Requirements

Concrete anchors must satisfy strength requirements for steel failure, concrete breakout, pullout, and side-face blowout. The basic design equation:

$$\phi N_n \geq N_u$$

where $\phi$ = 0.65 (tension) or 0.70 (shear) and $N_u$ represents the factored load.

### Steel Strength in Tension

For cast-in-place headed studs or post-installed mechanical anchors:

$$N_{sa} = n A_{se} f_{uta}$$

where:
- $n$ = number of anchors
- $A_{se}$ = effective cross-sectional area
- $f_{uta}$ = specified tensile strength

### Concrete Breakout Strength

The concrete breakout capacity depends on embedment depth $h_{ef}$:

$$N_{cb} = \frac{A_{Nc}}{A_{Nco}} \psi_{ec,N} \psi_{ed,N} \psi_{c,N} \psi_{cp,N} N_b$$

where the basic concrete breakout strength:

$$N_b = k_c \lambda \sqrt{f'_c} h_{ef}^{1.5}$$

with $k_c = 24$ for cast-in anchors, $k_c = 17$ for post-installed, $\lambda = 1.0$ for normal-weight concrete, and $f'_c$ in psi.

Edge distance and spacing reduction factors ($\psi$ terms) significantly impact capacity. Minimum edge distance should exceed $4h_{ef}$ where practical.

## Structural Attachment Methods

### Welded Connections

Welded equipment support frames provide robust anchorage when designed per AISC 360 and AWS D1.1. Base plates distribute concentrated loads to embedded plates or structural steel supports.

Fillet weld strength for equipment frame attachment:

$$R_n = F_w A_{we}$$

where $F_w = 0.60F_{EXX}$ (LRFD with $\phi = 0.75$), $F_{EXX}$ is electrode strength, and $A_{we}$ is effective throat area.

Full-penetration groove welds develop the base metal strength and are preferred for critical anchorages subject to tension and reversal.

### Bolted Base Plates

Steel base plates transfer equipment loads to concrete anchors. Plate thickness must resist bending between anchors:

$$t_{req} = \sqrt{\frac{6M_u}{F_y b \phi}}$$

where $M_u$ is the applied moment per unit width and $b$ is the effective width of the yield line pattern.

Grout pads beneath base plates ensure uniform bearing. Non-shrink grout provides 4000-6000 psi compressive strength and accommodates minor leveling adjustments.

### Spring Isolators with Seismic Restraints

Vibration-isolated equipment requires supplemental anchorage beyond the isolators. Housing-mounted restraints limit displacement while maintaining isolation performance.

Restraint spacing around the equipment perimeter should distribute forces uniformly. All-directional snubbers with 0.25-0.5 inch clearance accommodate thermal expansion while engaging under seismic or wind loads.

## Installation Considerations

Anchor installation quality directly impacts performance. Post-installed anchors require:

- Proper hole diameter and depth tolerance (±1/16 inch diameter, +1/4 inch depth)
- Clean, dry holes free of concrete dust
- Torque verification per manufacturer specifications
- Proof testing at 1.5 times design load for critical applications

Concrete condition assessment ensures adequate compressive strength before anchor installation. Minimum $f'_c = 2500$ psi required for most mechanical anchors; higher strength needed for high-load applications.

## Quality Assurance

Special inspection per IBC Chapter 17 verifies proper installation. Continuous special inspection applies to:

- High-load post-installed anchors ($N_u > 0.75\phi N_n$)
- Welded connections for equipment over 10 tons
- Anchorage in high-seismic or wind exposure categories

Pull tests on representative samples validate installation procedures. Testing typically involves 5% of anchors with minimum of two per floor or roof level.

Proper anchorage design integrating ACI 318 concrete capacity principles with ASCE 7 load requirements ensures HVAC equipment remains secured during extreme wind events, protecting both the equipment investment and building occupants.
