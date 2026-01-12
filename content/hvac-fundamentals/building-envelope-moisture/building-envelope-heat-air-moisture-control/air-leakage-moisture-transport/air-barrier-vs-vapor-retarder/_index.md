---
title: "Air Barrier Vs Vapor Retarder"
description: "Technical comparison of air barriers and vapor retarders including performance criteria, material specifications, permeance ratings, and integration strategies for building envelope moisture control"
weight: 3
---

## Overview

Air barriers and vapor retarders serve distinct functions in building envelope moisture control, yet confusion between these two systems remains common in practice. An air barrier controls moisture transport via air leakage (convection), while a vapor retarder controls moisture transport via diffusion. Understanding the fundamental differences between these systems is critical because air leakage typically transports 10-100 times more moisture than vapor diffusion under equivalent driving forces.

The distinction becomes critical in climate-specific design. In heating climates, uncontrolled air leakage during winter can deposit moisture within wall cavities through exfiltration, leading to condensation on cold surfaces. In cooling climates, infiltration of humid outdoor air can cause similar problems on cooled interior surfaces. Vapor diffusion, while slower, operates continuously and must be managed through appropriate retarder placement.

## Fundamental Differences

### Transport Mechanisms

Air barriers control moisture movement by bulk air transport (convection), while vapor retarders control moisture movement by molecular diffusion. The moisture transport capacity of these mechanisms differs by orders of magnitude:

**Moisture Transport by Air Leakage:**
```
M_air = ρ_air × ω × Q_air
```

Where:
- M_air = Moisture transport rate by air leakage (kg/s)
- ρ_air = Air density (kg/m³)
- ω = Humidity ratio (kg water/kg dry air)
- Q_air = Air leakage rate (m³/s)

**Moisture Transport by Vapor Diffusion:**
```
M_diff = δ × A × Δp_v / d
```

Where:
- M_diff = Moisture transport rate by diffusion (kg/s)
- δ = Vapor permeability of material (kg/(s·m·Pa))
- A = Area (m²)
- Δp_v = Vapor pressure difference (Pa)
- d = Material thickness (m)

### Quantitative Comparison

For a typical 1 m² wall section with indoor conditions at 21°C, 50% RH and outdoor conditions at 0°C, 80% RH:

| Transport Mode | Moisture Flow Rate | Relative Magnitude |
|----------------|-------------------|-------------------|
| Air leakage at 0.1 L/(s·m²) | ~0.08 g/h | 100× |
| Vapor diffusion through gypsum board | ~0.0008 g/h | 1× |

This 100:1 ratio demonstrates why air barrier performance typically dominates moisture control effectiveness.

## Performance Criteria

### Air Barrier Requirements

ASHRAE 90.1 and the International Energy Conservation Code (IECC) define air barrier performance based on maximum air leakage rates:

**Assembly Air Leakage Limits:**

| Assembly Type | Maximum Air Leakage (L/(s·m²) at 75 Pa) |
|---------------|----------------------------------------|
| Walls | 0.20 |
| Roofs | 0.20 |
| Floors | 0.20 |

**Material Air Leakage Limits:**

| Material Category | Maximum Air Leakage (L/(s·m²) at 75 Pa) |
|-------------------|----------------------------------------|
| Rigid materials | 0.02 |
| Flexible membranes | 0.02 |
| Sealed joints | 0.20 |

**Air Barrier Continuity:**

The air barrier system must form a continuous plane around the building thermal envelope. Discontinuities at the following locations require specific detailing:
- Wall-to-roof transitions
- Wall-to-foundation transitions
- Penetrations (windows, doors, mechanical, electrical)
- Material transitions
- Construction joints

### Vapor Retarder Requirements

The International Residential Code (IRC) and International Building Code (IBC) classify vapor retarders based on permeance:

**Vapor Retarder Classes (Per IRC R702.7 and IBC 1405.3):**

| Class | Permeance | Description | Example Materials |
|-------|-----------|-------------|-------------------|
| Class I | ≤0.1 perm | Vapor impermeable | Polyethylene sheet, aluminum foil, sheet metal, rubber membrane |
| Class II | >0.1 to ≤1.0 perm | Vapor semi-impermeable | Kraft-faced insulation, unfaced XPS (>1 inch), certain paints |
| Class III | >1.0 to ≤10 perm | Vapor semi-permeable | Latex paint, unfaced fiberglass batt, plywood, OSB |
| Not a vapor retarder | >10 perm | Vapor permeable | Unpainted gypsum board, unfaced mineral wool, open-cell spray foam |

**Permeance Calculation:**

Permeance (M) is defined as:

```
M = δ / d
```

Where:
- M = Permeance (kg/(Pa·s·m²)) or (perm)
- δ = Vapor permeability (kg/(s·m·Pa))
- d = Material thickness (m)

**Unit Conversion:**
- 1 perm (US) = 57.4 ng/(Pa·s·m²) = 5.74 × 10⁻¹¹ kg/(Pa·s·m²)
- 1 perm-inch = 1.46 × 10⁻¹² kg/(Pa·s·m)

## Material Properties

### Air Barrier Materials

**Rigid Air Barriers:**

| Material | Air Permeability (L/(s·m²) at 75 Pa) | Installation Notes |
|----------|-------------------------------------|-------------------|
| Gypsum board (sealed) | <0.02 | Requires sealed joints, penetrations |
| Exterior gypsum sheathing | <0.02 | Requires sealed joints, face-sealed fasteners |
| Cement board | <0.02 | Joints must be sealed with appropriate mastic |
| Structural sheathing (sealed) | <0.02 | OSB or plywood with sealed joints and penetrations |
| Cast-in-place concrete | <0.02 | Inherently air-tight, seal formwork penetrations |
| Precast concrete panels | <0.02 | Seal panel joints with appropriate sealant |

**Flexible Air Barriers:**

| Material | Air Permeability (L/(s·m²) at 75 Pa) | Installation Requirements |
|----------|-------------------------------------|--------------------------|
| Self-adhered membranes | <0.02 | Continuous substrate, no voids, proper adhesion |
| Mechanically fastened membranes | <0.02 | Overlapped seams, sealed fastener penetrations |
| Fluid-applied membranes | <0.02 | Minimum dry film thickness, proper surface prep |
| House wraps (taped seams) | <0.02 | All seams taped, fastener penetrations sealed |

**Air Barrier Coatings:**

Spray-applied air barriers require proper surface preparation and minimum dry film thickness:

| Product Type | Typical Dry Film Thickness | Substrate Requirements |
|--------------|---------------------------|------------------------|
| Water-based acrylic | 20-40 mils (0.5-1.0 mm) | Clean, dry, free of oils/dust |
| Vapor-permeable coating | 20-30 mils (0.5-0.75 mm) | Can accommodate substrate moisture |
| Vapor-impermeable coating | 30-60 mils (0.75-1.5 mm) | Dry substrate required |

### Vapor Retarder Materials

**Class I Vapor Retarders (≤0.1 perm):**

| Material | Permeance (perm) | Application | Limitations |
|----------|------------------|-------------|-------------|
| Polyethylene sheet (6 mil) | 0.06 | Interior in heating climates | Not recommended in mixed/cooling climates |
| Aluminum foil (1 mil) | 0.05 | Facing on insulation products | Corrosion potential in high humidity |
| Rubberized asphalt membrane | 0.05 | Below-grade waterproofing | High cost, temperature sensitive |
| Sheet metal | 0.00 | Mechanical equipment, ducts | Condensation potential |
| Self-adhered bituminous membrane | 0.05-0.08 | Foundation waterproofing | UV degradation if exposed |

**Class II Vapor Retarders (>0.1 to ≤1.0 perm):**

| Material | Permeance (perm) | Application | Benefits |
|----------|------------------|-------------|----------|
| Kraft facing on insulation | 0.3-0.5 | Interior vapor control, heating climates | Allows some drying |
| XPS foam (1.5 inch) | 0.6-0.8 | Continuous insulation | Provides both thermal and vapor control |
| Foil-faced polyisocyanurate | 0.05-0.1 | Roofing, continuous insulation | High R-value per inch |
| Vapor retarder paint (special) | 0.45-0.90 | Retrofit applications | Easy application |

**Class III Vapor Retarders (>1.0 to ≤10 perm):**

| Material | Permeance (perm) | Application | Benefits |
|----------|------------------|-------------|----------|
| Latex paint (2 coats) | 5-10 | Standard interior finish | Allows significant drying |
| Plywood (3/8 inch) | 0.5-1.5 | Structural sheathing | Structural and vapor control |
| OSB (7/16 inch) | 0.5-2.0 | Structural sheathing | Cost-effective |
| Closed-cell spray foam (2 inch) | 1.0-2.0 | Air and vapor control | Combined functions |

## Performance Testing

### Air Barrier Testing Methods

**ASTM E2357 - Standard Test Method for Determining Air Leakage of Air Barrier Assemblies:**

Test conditions:
- Pressure differential: 75 Pa (1.57 psf)
- Temperature: 24 ± 3°C (75 ± 5°F)
- Test specimen: Representative wall assembly
- Pass criterion: ≤0.20 L/(s·m²) at 75 Pa

**ASTM E283 - Standard Test Method for Determining Rate of Air Leakage:**

Used for testing windows, curtain walls, and other fenestration products:
- Test pressure: 75 Pa or 1.57 psf
- Results reported in L/(s·m²) or cfm/ft²

**Field Testing - Blower Door:**

Whole-building air leakage testing per ASTM E779:

```
ACH₅₀ = (Q₅₀ × 60) / V
```

Where:
- ACH₅₀ = Air changes per hour at 50 Pa
- Q₅₀ = Air flow rate at 50 Pa (m³/s)
- V = Building volume (m³)

**Normalization for Climate:**

```
ELA = Q₅₀ / (2√Δp)
```

Where:
- ELA = Equivalent leakage area (m²)
- Q₅₀ = Air flow rate at 50 Pa (m³/s)
- Δp = Pressure difference (50 Pa)

Target values from ASHRAE Standard 62.2:
- New construction: 3-5 ACH₅₀ (residential)
- Commercial buildings: <0.40 cfm/ft² at 75 Pa

### Vapor Retarder Testing Methods

**ASTM E96 - Standard Test Methods for Water Vapor Transmission:**

**Desiccant Method (Procedure A):**
- Measures water vapor movement from high to low humidity
- Test conditions: 50% RH gradient
- Used for low permeance materials

**Water Method (Procedure B):**
- Measures water vapor movement from liquid water source
- Test conditions: 100% to 50% RH gradient
- Used for high permeance materials

**Permeance Calculation:**

```
M = (G / t) / (A × Δp_v)
```

Where:
- M = Permeance (kg/(Pa·s·m²))
- G = Mass of water vapor transmitted (kg)
- t = Time (s)
- A = Test area (m²)
- Δp_v = Vapor pressure difference (Pa)

**ASTM C1512 - Standard Test Method for Characterizing the Moisture Vapor Permeance of Spray Applied Liquid Air Barriers:**

Specific protocol for spray-applied products:
- Substrate: Concrete masonry unit (CMU) or gypsum board
- Minimum dry film thickness as specified by manufacturer
- Test per ASTM E96 after proper cure time

## Climate-Specific Requirements

### Vapor Retarder Placement by Climate Zone

**IECC Climate Zone Requirements (Per IRC R702.7):**

| Climate Zone | Description | Required Vapor Retarder Class | Placement |
|--------------|-------------|------------------------------|-----------|
| 1, 2, 3 | Hot-humid, Mixed | Not required, or Class III | Interior (if used) |
| 4 Marine | Marine | Not required, or Class III | Interior (if used) |
| 4 (except Marine) | Mixed-humid | Class III | Interior |
| 5 | Cold | Class II or III | Interior |
| 6, 7, 8 | Very cold/Subarctic | Class I, II, or III | Interior |

**Exceptions and Special Cases:**

Class I vapor retarders can be eliminated when one of the following is installed on the exterior side:
- Continuous insulation R-5 or greater (Zones 4C, Marine 4)
- Continuous insulation R-7.5 or greater (Zone 4 except Marine)
- Continuous insulation R-10 or greater (Zones 5, 6)
- Continuous insulation R-15 or greater (Zones 7, 8)

### Air Barrier Requirements by Climate

Air barriers are required in all climate zones per ASHRAE 90.1 and IECC. Location options:

1. **Exterior Air Barrier:**
   - Protects insulation from air washing
   - Must be exterior to insulation or between insulation layers
   - Common with cavity insulation + continuous insulation

2. **Interior Air Barrier:**
   - Common in cold climates (reduces exfiltration)
   - Often combined with vapor retarder function
   - Must be continuous across structural framing

3. **Mid-Wall Air Barrier:**
   - At structural sheathing plane
   - Protected from weather
   - Requires careful window/door integration

## Design Strategies

### Separate vs. Combined Systems

**Separate Systems:**

Advantages:
- Optimized performance for each function
- Allows independent material selection
- Better drying potential (air barrier can be vapor-permeable)
- Easier retrofit and repair

Typical assembly (cold climate):
- Interior: Painted gypsum board (Class III vapor retarder, 5-10 perm)
- Cavity: Fiberglass or mineral wool insulation
- Sheathing: OSB with sealed joints (air barrier, 0.5-2 perm)
- Exterior: Weather-resistive barrier

**Combined Systems:**

Advantages:
- Reduced complexity
- Fewer potential failure points
- Lower installed cost
- Simplified detailing

Materials that function as both air and vapor barrier:
- Self-adhered membranes (Class I vapor retarder + air barrier)
- Closed-cell spray foam (Class II vapor retarder + air barrier)
- Foil-faced rigid insulation (Class I vapor retarder + air barrier)

**Design Considerations:**

When combining air barrier and vapor retarder functions, verify:
1. Material provides required air leakage resistance (<0.02 L/(s·m²) at 75 Pa)
2. Material provides appropriate permeance for climate zone
3. Continuity can be maintained at all transitions
4. Assembly provides adequate drying potential

### Continuity at Transitions

**Foundation to Wall Transition:**

Critical details:
- Sealant between sill plate and foundation
- Membrane transition from foundation waterproofing to wall air barrier
- Rim joist insulation and air sealing
- Penetration sealing (anchor bolts, utilities)

**Wall to Roof Transition:**

Methods:
- Extend wall air barrier to roof deck
- Transition membrane from wall to roof assembly
- Seal top plate penetrations
- Address thermal bridging at structural members

**Window and Door Openings:**

Integration requirements:
- Rough opening air sealing before unit installation
- Window/door unit sealed to air barrier system
- Use of compatible sealants and tapes
- Maintain continuity of air barrier plane
- Consider thermal expansion/contraction

**Mechanical, Electrical, and Plumbing Penetrations:**

Sealing strategies:
- Dedicated penetration sleeves with integrated sealing
- Expandable foam for grouped penetrations (non-shrinking formulation)
- Compression gaskets for through-wall penetrations
- Prefabricated boots for ductwork and piping

## Common Design Errors

### Error 1: Confusing Functions

**Problem:** Specifying polyethylene sheet as "air and vapor barrier" in cooling climates.

**Issue:** Polyethylene is a Class I vapor retarder (0.06 perm), which prevents inward drying during cooling season. If installed on interior of wall in mixed or cooling climate, summer moisture drive can trap moisture in wall assembly.

**Solution:** In cooling or mixed climates, use Class III vapor retarder (>1.0 perm) on interior to allow inward drying. Locate air barrier at sheathing plane with vapor-permeable air barrier material.

### Error 2: Vapor Retarder on Both Sides

**Problem:** Installing vapor-impermeable materials on both interior and exterior of wall assembly.

**Issue:** Creates "vapor sandwich" with no drying potential. Any construction moisture or incidental water intrusion becomes trapped, leading to mold growth and material degradation.

**Solution:** Ensure one side of assembly allows drying. Typical approach: vapor-impermeable or semi-impermeable on climate-appropriate side, vapor-permeable on opposite side.

### Error 3: Air Barrier Discontinuity

**Problem:** Air barrier transitions not detailed or executed at critical junctions.

**Issue:** Even small gaps dramatically reduce air barrier system performance. A 1% gap can reduce effectiveness by 30% or more.

**Solution:** Detail all transitions in construction documents. Common locations requiring attention:
- Window and door rough openings
- Foundation to wall connection
- Wall to roof connection
- Structural penetrations
- Service penetrations

### Error 4: Inappropriate Climate Application

**Problem:** Using Class I vapor retarder in mixed or cooling climate based on heating climate prescriptive requirements.

**Issue:** Prevents inward drying during cooling season, trapping moisture from air conditioning condensation or summer moisture drive.

**Solution:** Reference IECC climate-specific requirements. In mixed climates (Zone 4 except Marine), maximum Class III interior vapor retarder recommended unless continuous exterior insulation is provided.

## Installation Quality Control

### Air Barrier Installation

**Pre-Installation Verification:**
- Substrate is clean, dry, and appropriate for selected material
- Ambient conditions meet manufacturer requirements
- Materials are stored per manufacturer specifications
- Installers are trained and experienced with system

**During Installation:**
- Continuous oversight of critical transitions
- Random adhesion testing of self-adhered membranes
- Wet film thickness measurement of fluid-applied products
- Joint and penetration sealing verification
- Photographic documentation of concealed elements

**Post-Installation Testing:**
- Localized blower door testing of individual floors or zones
- Infrared thermography during pressurization
- Smoke pencil testing at suspected leakage locations
- Whole-building blower door test

**Performance Criteria:**

Residential targets (ASHRAE 62.2):
- New construction: ≤5 ACH₅₀ (climate zones 1-2), ≤3 ACH₅₀ (climate zones 3-8)
- Energy-efficient construction: ≤1.5 ACH₅₀ (with ventilation system)

Commercial targets (ASHRAE 90.1):
- Maximum 0.40 cfm/ft² of envelope area at 75 Pa
- High-performance buildings: 0.25 cfm/ft² or less

### Vapor Retarder Installation

**Installation Requirements:**

Class I vapor retarders:
- Continuous sheet installation
- Minimum 6-inch overlaps at seams
- Sealed penetrations with compatible tape or sealant
- Protection from mechanical damage during construction

Class II and III vapor retarders:
- Application per manufacturer instructions
- Proper surface preparation for coatings
- Sealed joints for kraft-faced products
- Fastener penetrations addressed per system requirements

**Verification Methods:**
- Visual inspection of all seams and penetrations
- Sample removal and laboratory testing of spray-applied products
- Wet film thickness measurement during application
- Documentation of ambient conditions during installation

## Advanced Considerations

### Hygrothermal Modeling

Computer simulation tools (WUFI, THERM, MOISTURE-EXPERT) allow analysis of:
- Coupled heat and moisture transport
- Transient conditions throughout annual cycle
- Material moisture content over time
- Condensation potential at interfaces
- Drying rates and directions

**Key Simulation Parameters:**
- Accurate material properties (permeability, sorption isotherms, thermal conductivity)
- Representative climate data (ASHRAE climate design conditions)
- Realistic interior conditions (temperature, relative humidity generation)
- Construction sequence and initial moisture content

### Smart Vapor Retarders

Variable permeance materials adjust vapor permeability based on ambient relative humidity:

**Performance Characteristics:**

| Relative Humidity | Permeance (perm) | Classification |
|------------------|------------------|----------------|
| Low (<40% RH) | 0.5-1.0 | Class II |
| Medium (40-70% RH) | 3-5 | Class III |
| High (>70% RH) | 10-20 | Vapor open |

**Applications:**
- Mixed climates with seasonal moisture drive reversals
- Retrofit applications with unknown existing conditions
- High-performance enclosures requiring bidirectional drying
- Assemblies with moisture-sensitive materials

**Mechanism:**
Nylon film expands at high humidity, increasing effective permeance by enlarging pore structure.

### Airtight Drywall Approach (ADA)

Gypsum board interior finish serves as air barrier:

**Requirements:**
- Sealed top and bottom plates to framing
- Sealed electrical boxes (airtight-rated boxes or gaskets)
- Sealed drywall joints (compound and tape)
- Sealed penetrations (switches, outlets, fixtures)
- Sealed perimeter (gasket or sealant at base and ceiling)

**Performance:**
Properly executed ADA can achieve:
- 0.6-1.2 ACH₅₀ in residential construction
- Equivalent to 0.02 L/(s·m²) at 75 Pa material requirement

**Advantages:**
- Uses standard construction materials
- Inspectable and testable
- Easy to repair
- Combines with interior vapor retarder function

## Specification Guidance

### Section 07 26 00 - Vapor Retarders

**Part 1 - General:**
- Reference standards: ASTM E96, ASTM C1512, IRC R702.7
- Climate zone designation
- Required vapor retarder class
- Submittals: product data, third-party test reports, installation instructions

**Part 2 - Products:**
- Material type and permeance classification
- Physical properties (thickness, tensile strength, UV resistance)
- Accessories (tapes, sealants, primers)
- Compatibility with adjacent materials

**Part 3 - Execution:**
- Surface preparation requirements
- Application method
- Lap and seam requirements
- Penetration sealing methods
- Protection during construction
- Quality control testing

### Section 07 27 00 - Air Barriers

**Part 1 - General:**
- Reference standards: ASTM E2357, ASTM E283, ASTM E779
- Performance criteria: ≤0.20 L/(s·m²) at 75 Pa for assemblies
- Testing requirements: pre-construction mockup, field testing
- Installer qualifications

**Part 2 - Products:**
- Air barrier material type and air permeability
- Physical properties (tensile strength, elongation, water resistance)
- Accessories (transitions, terminations, primers, reinforcement)
- Compatibility with other envelope components

**Part 3 - Execution:**
- Substrate preparation and inspection
- Application method and coverage rates
- Continuity details at all transitions
- Penetration sealing methods
- Quality control inspections and testing
- Field air leakage testing protocol

## References

**ASHRAE Standards:**
- ASHRAE Standard 90.1: Energy Standard for Buildings Except Low-Rise Residential Buildings
- ASHRAE Standard 62.2: Ventilation and Acceptable Indoor Air Quality in Residential Buildings
- ASHRAE Handbook - Fundamentals, Chapter 25: Heat, Air, and Moisture Control in Building Assemblies

**ASTM Standards:**
- ASTM E96: Standard Test Methods for Water Vapor Transmission of Materials
- ASTM E283: Standard Test Method for Determining Rate of Air Leakage Through Exterior Windows, Skylights, Curtain Walls, and Doors
- ASTM E779: Standard Test Method for Determining Air Leakage Rate by Fan Pressurization
- ASTM E2357: Standard Test Method for Determining Air Leakage of Air Barrier Assemblies
- ASTM C1512: Standard Test Method for Characterizing the Moisture Vapor Permeance of Spray Applied Liquid Air Barriers

**Building Codes:**
- International Energy Conservation Code (IECC)
- International Residential Code (IRC), Section R702.7
- International Building Code (IBC), Section 1405.3

**Industry References:**
- Air Barrier Association of America (ABAA): Air Barrier Specifications and Testing
- Building Science Corporation: Building Science Digests on Air Barriers and Vapor Control
- NIST Technical Note 1496: Review of Test Methods for Air Leakage
