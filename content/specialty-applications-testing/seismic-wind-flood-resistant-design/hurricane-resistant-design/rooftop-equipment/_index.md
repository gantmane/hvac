---
title: "Hurricane-Resistant Rooftop Equipment Design"
aliases: ["Hurricane-Resistant Rooftop Equipment Design"]
description: "Engineering specifications for rooftop HVAC equipment hurricane resistance including wind uplift calculations, anchorage design, curb attachments, and FM Global testing."
date: 2025-01-05
weight: 4
draft: false
keywords:
  - rooftop unit anchorage
  - hurricane wind uplift
  - FM Global 4470
  - ASCE 7 wind loads
  - equipment curb design
  - hurricane straps
  - rooftop equipment protection
  - wind screen design
---

## Wind Load Calculation for Rooftop Equipment

Rooftop HVAC equipment in hurricane-prone regions experiences severe wind forces that require rigorous engineering analysis. The design wind pressure on rooftop units combines uplift, horizontal, and overturning forces that must be resisted through proper anchorage systems.

### Design Wind Pressure

The net design wind pressure on rooftop equipment per ASCE 7 is calculated as:

$$p = q_h \cdot G \cdot C_p$$

Where:
- $p$ = design wind pressure (lb/ft²)
- $q_h$ = velocity pressure at mean roof height (lb/ft²)
- $G$ = gust effect factor (typically 0.85 for rigid equipment)
- $C_p$ = external pressure coefficient

The velocity pressure is determined by:

$$q_h = 0.00256 \cdot K_z \cdot K_{zt} \cdot K_d \cdot V^2$$

Where:
- $K_z$ = velocity pressure exposure coefficient
- $K_{zt}$ = topographic factor (1.0 for flat terrain)
- $K_d$ = wind directionality factor (0.85 for buildings)
- $V$ = basic wind speed (mph) from ASCE 7 wind maps

### Uplift Force on Equipment

The total uplift force acting on a rooftop unit is:

$$F_{uplift} = p_{net} \cdot A_{projected}$$

Where:
- $F_{uplift}$ = total uplift force (lb)
- $p_{net}$ = net upward pressure (lb/ft²)
- $A_{projected}$ = horizontal projected area of equipment (ft²)

For equipment mounted on curbs, the effective area includes both the unit and curb:

$$A_{effective} = (L + 2h)(W + 2h)$$

Where $L$ and $W$ are unit length and width, and $h$ is the curb height.

## Anchorage System Design

### Anchor Bolt Requirements

The number of anchor bolts required is determined by:

$$N_{bolts} = \frac{F_{uplift}}{T_{allow} \cdot SF}$$

Where:
- $N_{bolts}$ = number of anchor bolts required
- $T_{allow}$ = allowable tension capacity per bolt (lb)
- $SF$ = safety factor (typically 2.0 to 4.0)

Minimum anchor specifications for hurricane-prone regions:
- **Bolt diameter:** 5/8 inch minimum for units up to 10 tons
- **Embedment depth:** 4.5 inches minimum in concrete
- **Edge distance:** 4 bolt diameters minimum from slab edge
- **Spacing:** 6 bolt diameters minimum between bolts
- **Material:** Hot-dip galvanized or stainless steel Grade 316

### Hurricane Strap Systems

Hurricane straps provide additional resistance to uplift and overturning. Strap systems must be designed to resist:

$$T_{strap} = \frac{F_{uplift} + M_{overturn}/d}{N_{straps}}$$

Where:
- $T_{strap}$ = tension per strap (lb)
- $M_{overturn}$ = overturning moment (lb-ft)
- $d$ = distance between strap attachment points (ft)
- $N_{straps}$ = number of straps

Hurricane straps shall be:
- Constructed from 14-gauge minimum galvanized steel
- Factory-installed with minimum four fasteners per connection
- Attached to structural members, not sheet metal panels
- Provided with manufacturer's load rating documentation

## Equipment Curb Design

### Structural Requirements

Rooftop equipment curbs must transfer wind loads from the unit to the roof structure. The curb must resist:

1. **Uplift forces** transmitted through mounting rails
2. **Lateral shear** from horizontal wind pressure
3. **Overturning moments** at curb-to-roof interface

Curb construction specifications:
- **Material:** Minimum 14-gauge galvanized steel or equivalent aluminum
- **Height:** 8-14 inches depending on roof membrane thickness
- **Insulation:** Rigid insulation with minimum R-6 value
- **Flashing:** Factory-applied cant strip and counter-flashing
- **Corner reinforcement:** Welded or riveted corners with gusset plates

### Curb-to-Roof Attachment

The curb-to-roof connection must be engineered for the combined effects of wind uplift and shear:

$$V_{shear} = q_h \cdot G \cdot C_p \cdot A_{vertical}$$

Where $A_{vertical}$ is the vertical projected area of the equipment.

Attachment specifications:
- Anchor spacing: Maximum 12 inches on center
- Anchors through wood nailers: 3/8-inch lag screws minimum, 3-inch embedment
- Anchors through concrete: 1/2-inch expansion anchors or cast-in-place inserts
- Continuous perimeter attachment required (no gaps)

## Wind Screen Design

Wind screens reduce wind pressure on equipment and improve performance but must be designed as structural elements:

### Screen Loading

Wind pressure on screens:

$$p_{screen} = q_h \cdot G \cdot C_{p,screen}$$

Where $C_{p,screen}$ typically ranges from 1.8 to 2.0 for solid screens.

Screen design requirements:
- **Material:** Aluminum or galvanized steel, minimum 16-gauge
- **Support structure:** Steel angle or channel frame
- **Anchorage:** Designed for screen area wind load plus equipment wind load
- **Openings:** Minimum 50% free area for airflow if perforated
- **Height:** Extend 12 inches above equipment top

## FM Global 4470 Testing Requirements

FM Global Property Loss Prevention Data Sheet 4470 establishes requirements for rooftop equipment subjected to wind uplift:

### Test Classifications

Equipment must be tested and rated for:
- **Class 1-60:** Resists 60 psf uplift pressure
- **Class 1-75:** Resists 75 psf uplift pressure
- **Class 1-90:** Resists 90 psf uplift pressure (minimum for high-velocity hurricane zones)
- **Class 1-105:** Resists 105 psf uplift pressure
- **Class 1-120:** Resists 120 psf uplift pressure

### Installation Requirements

FM Approved installations require:
- Manufacturer's installation instructions followed exactly
- Anchor bolts meeting specified grade and embedment
- Field verification of concrete strength (minimum 2,500 psi)
- Documentation of anchor pull-test results (10% of anchors tested)
- Third-party inspection for insurance compliance

### Maintenance and Inspection

Annual hurricane season preparation:
- Verify all anchor bolts tight (torque verification)
- Inspect hurricane straps for corrosion or damage
- Check curb-to-roof seal integrity
- Ensure no loose panels or access doors
- Document equipment nameplate wind rating vs. site design wind speed

## ASCE 7 Design Considerations

ASCE 7 Chapter 30 specifies wind loads on components and cladding, including rooftop equipment:

### Roof Zone Classifications

Equipment location affects pressure coefficients:
- **Zone 1 (interior):** $C_p = -0.9$ (uplift)
- **Zone 2 (edge):** $C_p = -1.8$ (uplift)
- **Zone 3 (corner):** $C_p = -2.7$ (uplift)

Corner zones extend from building corner by 10% of least building width. Equipment in corner zones requires increased anchorage capacity.

### Special Considerations

Additional factors for rooftop equipment in hurricane regions:
- **Parapets:** Equipment behind parapets may experience reduced wind loads if parapet height exceeds equipment height
- **Building height:** Taller buildings require increased wind pressure calculations
- **Terrain exposure:** Coastal exposure (Exposure D) increases wind loads by 30-50% compared to suburban exposure (Exposure B)
- **Importance factor:** Essential facilities (hospitals, emergency services) require importance factor $I_e = 1.15$

Equipment must be designed for the most critical combination of uplift, horizontal force, and overturning moment to ensure hurricane-resistant performance throughout the equipment service life
