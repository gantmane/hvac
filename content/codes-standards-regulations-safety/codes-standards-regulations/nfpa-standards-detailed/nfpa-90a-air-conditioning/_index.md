---
title: "NFPA 90A: Air-Conditioning and Ventilating Systems"
linkTitle: "NFPA 90A Standard"
weight: 1
date: 2026-01-04
description: "Comprehensive requirements for NFPA 90A Standard for Installation of Air-Conditioning and Ventilating Systems, covering duct construction, fire dampers, smoke dampers, penetrations, and fire protection for commercial HVAC systems."
keywords: ["NFPA 90A", "air conditioning fire safety", "duct construction standards", "fire damper requirements", "smoke damper installation", "fire-rated penetrations", "plenum fire protection", "HVAC code compliance"]
---

## Overview of NFPA 90A

NFPA 90A, Standard for the Installation of Air-Conditioning and Ventilating Systems, establishes minimum fire safety requirements for HVAC systems in all occupancies except one- and two-family dwellings (covered by NFPA 90B). Published by the National Fire Protection Association and updated on a regular cycle, this standard is referenced by building codes worldwide and forms the basis for mechanical code provisions related to fire safety.

The standard's primary objective is to prevent HVAC systems from contributing to fire spread throughout buildings. Ductwork, if not properly protected, can act as chimneys that rapidly distribute flames, hot gases, and smoke to areas far from the fire origin. NFPA 90A addresses this hazard through comprehensive requirements for materials, construction methods, dampers, and penetration protection.

## Scope and Application

### Covered Systems

NFPA 90A applies to:

- All air-conditioning systems for comfort or process cooling
- Ventilation systems including general, process, and specialty exhaust
- Air-handling equipment and associated ductwork
- Smoke control and smoke management systems
- Ceiling plenums used for air distribution or return
- Air filtration and cleaning equipment

### Excluded Systems

The following are specifically excluded from NFPA 90A scope:

- Residential systems in one- and two-family dwellings (see NFPA 90B)
- Commercial cooking exhaust (covered by NFPA 96)
- Dust collection systems with combustible particulates
- Systems conveying flammable vapors or fumes (see NFPA 91)
- Industrial process exhaust containing corrosive materials

## Duct Materials and Construction

### Material Requirements by Location

NFPA 90A classifies duct locations and specifies acceptable materials for each:

**Class 0 Ducts (Noncombustible):**
- Required in vertical shafts passing through two or more floors
- Required in air plenums above acoustical tile ceilings
- Materials: Steel, stainless steel, aluminum, or other approved noncombustible materials
- Wall thickness per SMACNA standards based on static pressure and dimensions

**Class 1 Ducts (Limited Combustible):**
- Permitted within single floor areas with flame spread ≤25
- Includes certain rigid fiberglass ducts meeting UL 181
- Factory-made ducts with fire-resistant coatings

### Duct Thickness and Gauge Requirements

Minimum metal thickness prevents duct collapse during fire:

| Duct Dimension | Galvanized Steel | Aluminum | Stainless Steel |
|----------------|------------------|----------|-----------------|
| Up to 12 inches | 28 gauge (0.0149") | 0.019" | 30 gauge |
| 13-30 inches | 26 gauge (0.0187") | 0.024" | 28 gauge |
| 31-54 inches | 24 gauge (0.0239") | 0.032" | 26 gauge |
| 55-84 inches | 22 gauge (0.0299") | 0.040" | 24 gauge |
| Over 84 inches | 20 gauge (0.0359") | 0.050" | 22 gauge |

### Duct Insulation and Liners

Internal duct liners and external insulation must meet flame spread and smoke development limits:

**Flame spread index:** ≤25 when tested per ASTM E84
**Smoke developed index:** ≤50 when tested per ASTM E84

Insulation in plenums and concealed spaces requires particular attention to fire performance. Vapor barriers and adhesives must also meet these criteria.

## Fire Dampers

### Installation Requirements

Fire dampers must be installed at every point where a duct penetrates:

1. **Fire walls** (3- or 4-hour rated assemblies)
2. **Fire barriers** (1-, 2-, or 3-hour rated assemblies)
3. **Fire partitions** (1-hour rated assemblies)
4. **Horizontal assemblies** (floor/ceiling assemblies with fire-resistance ratings)

**Fire damper rating equation:**

$$\text{Damper Rating (hours)} = \min(T_{assembly}, 3.0)$$

Where:
- $T_{assembly}$ = Fire-resistance rating of penetrated assembly (hours)
- Maximum required damper rating is 3 hours per UL 555

### Types and Operation

**Static Fire Dampers:**
- Curtain-type blades that close by gravity or spring force
- Activated by fusible link melting at specific temperature (typically 165°F, 212°F, or 286°F)
- Used where airflow stops during fire conditions

**Dynamic Fire Dampers:**
- Rated to close against airflow under system operation
- Required where HVAC systems continue operation during fire (smoke control systems)
- Must meet closure and leakage requirements with air flowing

**Combination Fire/Smoke Dampers:**
- Provide both fire barrier protection and smoke control
- Close on smoke detection signal or fusible link actuation
- Must meet both UL 555 (fire) and UL 555S (smoke) standards

### Fusible Link Temperature Selection

Fusible link temperature rating must be carefully selected:

$$T_{link} = T_{ambient} + 50°F \text{ to } T_{ambient} + 75°F$$

Where:
- $T_{link}$ = Fusible link rating temperature
- $T_{ambient}$ = Maximum expected ambient temperature at damper location

Common ratings:
- **165°F:** Standard for normal HVAC applications
- **212°F:** High-temperature areas (near boilers, roofs in hot climates)
- **286°F:** Commercial kitchen makeup air, high-temperature process areas

## Smoke Dampers

### Purpose and Application

Smoke dampers restrict smoke passage through HVAC systems during fire events. Unlike fire dampers that respond to heat, smoke dampers operate on control signals from smoke detectors or fire alarm systems.

**Required locations per NFPA 90A and IBC:**

- Penetrations of smoke barriers in healthcare facilities
- Air transfer openings in smoke partitions
- Corridors in Group I-2 (hospitals and nursing homes)
- Air-handling system serving multiple smoke compartments

### Performance Requirements

Smoke dampers must meet UL 555S certification:

- **Leakage Class:** Class I (10 cfm/sq ft at 4" w.g.), Class II (40 cfm/sq ft), or Class III (80 cfm/sq ft)
- **Temperature Rating:** Ambient (≤250°F) or elevated (≥250°F continuous, 350°F intermittent)
- **Velocity Rating:** Maximum air velocity damper can withstand while closing

**Leakage calculation:**

$$Q_{leak} = L_{class} \times A_{damper}$$

Where:
- $Q_{leak}$ = Allowable leakage (cfm)
- $L_{class}$ = Leakage class rating (cfm/sq ft)
- $A_{damper}$ = Damper face area (sq ft)

### Control Integration

Smoke dampers require electrical or pneumatic actuation:

- Connected to building fire alarm system
- Activated by duct-mounted smoke detectors or area smoke detectors per NFPA 72
- Fail-safe operation (close on power loss)
- Status monitoring at fire alarm panel

## Penetrations of Fire-Rated Assemblies

### Firestop System Requirements

Every duct penetration through fire-rated construction must incorporate approved firestop systems tested per ASTM E814 or UL 1479. The firestop system must achieve:

**F-Rating:** Time (in hours) the through-penetration firestop system limits flame passage
**T-Rating:** Time until temperature on non-fire side exceeds 325°F above ambient (required for floor penetrations)

**Minimum rating requirement:**

$$R_{firestop} \geq R_{assembly}$$

Where:
- $R_{firestop}$ = F-rating of firestop system (hours)
- $R_{assembly}$ = Fire-resistance rating of penetrated assembly (hours)

### Annular Space Protection

The annular space between duct and opening must be protected with listed materials:

- **Mineral wool** board or blanket
- **Intumescent** materials that expand with heat
- **Cementitious** coatings or wraps
- **Mechanical** fire sleeves for flexible connections

Installation must exactly match tested configuration:

- Same duct material and thickness
- Same firestop product and thickness
- Same wall or floor construction type
- Proper support to prevent sagging

### Sleeve and Through-Penetration Details

**Steel sleeve installation:**

For ducts penetrating fire-rated assemblies without fire dampers:

1. Install steel sleeve minimum 24-gauge, extending minimum 1/2" both sides
2. Sleeve diameter: Duct diameter + 2 × annular space
3. Fill annular space with approved firestop material
4. Install continuous duct without joints within assembly thickness + 12"

## Ceiling Plenums and Concealed Spaces

### Plenum Construction Requirements

Ceiling plenums used for supply or return air distribution must meet specific criteria:

**Materials in plenum:**
- Exposed surfaces: Noncombustible or limited-combustible (flame spread ≤25)
- Electrical wiring: Plenum-rated cable (CMP) per NEC Article 300
- Piping insulation: Maximum flame spread 25, smoke developed 50
- No storage of combustible materials permitted

**Plenum return air velocity:**

$$V_{plenum} \leq 2,000 \text{ fpm}$$

Higher velocities can create noise and reduce firestop effectiveness.

### Fire Protection in Concealed Spaces

Concealed spaces in HVAC systems require protection when:

- Space exceeds 100 sq ft in area
- Space is not separated by draft stops
- Space contains combustible materials

**Draft stopping requirement:**

Install draft stops at maximum intervals:

- **3,000 sq ft** for combustible construction
- **1,000 sq ft** above acoustical tile ceilings used as return air plenums

## Air-Handling Equipment

### Equipment Room Fire Separation

Mechanical equipment rooms containing air-handling units must be separated from other building areas:

- **1-hour fire barrier** for equipment rooms in most occupancies
- **2-hour fire barrier** for central air-handling equipment rooms >2,000 cfm in high-rise buildings

Doors must be fire-rated assemblies with self-closing or automatic-closing devices.

### Equipment Fire Protection Features

Air-handling units must include:

**Remote shutdown capability:** Manual cutoff switches located outside equipment rooms
**Smoke detection:** Duct-mounted detectors in supply and return ducts per NFPA 72
**Filter protection:** Automatic shutdown on high-temperature detection in filter sections
**Electrical disconnects:** Within sight of equipment per NEC

## Inspection, Testing, and Maintenance

### Fire Damper Inspection Frequency

NFPA 90A mandates periodic inspection and testing:

**Initial acceptance test:** Verify proper operation before occupancy

**Periodic inspection:**
- **1 year** after initial occupancy
- **Every 4 years** for dampers in hospitals
- **Every 6 years** for dampers in other occupancies
- **Annually** for dampers in commercial cooking exhaust systems (NFPA 96)

### Testing Procedures

**Visual inspection verifies:**
- Freedom of movement (no obstructions)
- Proper fusible link installation and rating
- No visible damage to damper frame or blades
- Access door seals intact

**Functional testing requires:**
- Remove fusible link or activate control signal
- Verify complete closure
- Check blade alignment and seal contact
- Reinstall fusible link of correct temperature rating

### Documentation Requirements

Maintain permanent records including:

- Damper locations on floor plans
- Inspection dates and findings
- Repairs or replacements performed
- Names of qualified inspectors
- AHJ acceptance documentation

## Conclusion

NFPA 90A provides comprehensive fire safety requirements that protect building occupants by preventing HVAC systems from contributing to fire spread. Compliance demands attention to detail in material selection, installation practices, and ongoing maintenance. Engineers and contractors must thoroughly understand these requirements and coordinate with fire protection specialists to achieve safe, code-compliant installations. Regular inspections and testing ensure fire protection features remain functional throughout the building's service life.
