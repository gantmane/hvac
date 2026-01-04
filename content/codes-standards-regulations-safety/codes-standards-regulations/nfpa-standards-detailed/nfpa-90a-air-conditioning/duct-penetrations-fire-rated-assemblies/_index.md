---
title: "Duct Penetrations Through Fire-Rated Assemblies"
linkTitle: "Duct Penetrations & Firestop"
weight: 3
date: 2026-01-04
description: "Comprehensive requirements for duct penetrations through fire-rated assemblies, including firestop systems per ASTM E814 and UL 1479, F-rating and T-rating requirements, annular space protection, and installation details for maintaining fire-resistance ratings."
keywords: ["firestop systems", "fire-rated penetrations", "ASTM E814", "UL 1479", "F-rating", "T-rating", "annular space", "through-penetration firestop", "fire barrier protection", "duct sleeve installation"]
---

## Overview of Penetration Fire Protection

Every opening through a fire-rated assembly represents a potential breach in the building's fire compartmentation strategy. When HVAC ductwork penetrates fire walls, fire barriers, fire partitions, or fire-rated floor/ceiling assemblies, special protection measures must restore and maintain the assembly's fire-resistance rating. Firestop systems, combined with fire dampers where required, prevent fire, smoke, and hot gases from passing through these penetrations.

### Fire-Resistance Rating Fundamentals

Fire-rated assemblies receive hourly ratings based on testing per ASTM E119, Standard Test Methods for Fire Tests of Building Construction and Materials:

**Common ratings for HVAC applications:**
- **1-hour:** Corridor walls, tenant separations, some floor assemblies
- **2-hour:** Fire barriers in high-rise buildings, vertical shafts, some exit enclosures
- **3-hour:** Fire walls separating buildings or major occupancy divisions
- **4-hour:** High-rise standpipe/fire pump enclosures, some fire walls

**Rating preservation requirement:**

$$R_{penetration} \geq R_{assembly}$$

Where:
- $R_{penetration}$ = Fire-resistance rating of penetration protection system (hours)
- $R_{assembly}$ = Fire-resistance rating of penetrated barrier (hours)

Any penetration through a rated assembly must be protected by a system that maintains the assembly's rating.

### Types of Penetration Protection

HVAC duct penetrations employ two primary protection strategies:

**Fire dampers:**
- UL 555 listed devices
- Close automatically to block fire passage
- Rated for specific fire exposure times
- Required at most fire-rated barriers

**Through-penetration firestop systems:**
- Listed assemblies per ASTM E814 or UL 1479
- Seal annular space around duct
- Maintain rating without mechanical closure
- Used with or without fire dampers depending on application

**Combination approaches:**
- Fire damper + firestop system (most common)
- Firestop system alone (limited applications where dampers not required)
- Combination fire/smoke damper + firestop

## ASTM E814 and UL 1479 Testing Standards

### ASTM E814: Standard Test Method for Fire Tests of Penetration Firestop Systems

ASTM E814 (identical to UL 1479) establishes the test protocol for evaluating through-penetration firestop systems. This test subjects penetration assemblies to standardized fire exposure and measures their ability to prevent fire passage.

**Test specimen configuration:**
- Full-scale wall or floor assembly built per rated design
- Penetrating item (duct, pipe, cable, etc.) installed per system specifications
- Firestop materials applied exactly as intended in field
- Specimen exposed to standard time-temperature curve

**Standard time-temperature curve equation:**

$$T = T_0 + 750(1 - e^{-3.79553\sqrt{t}}) + 170.41\sqrt{t}$$

Where:
- $T$ = Furnace temperature (°F)
- $T_0$ = Initial temperature (typically 68°F)
- $t$ = Time (hours)

This produces approximately:
- 1,000°F at 5 minutes
- 1,300°F at 10 minutes
- 1,550°F at 30 minutes
- 1,700°F at 1 hour
- 1,850°F at 2 hours

**Performance criteria:**

1. **Flame passage:** No sustained flaming on unexposed side
2. **Hot gas passage:** Cotton waste pad must not ignite from hot gases
3. **Temperature limits:** See T-rating requirements below
4. **Hose stream test:** System must remain in place after water impact (walls only)

### F-Rating: Fire Resistance Time

The F-rating represents the time (in hours or minutes) the through-penetration firestop system prevents flame passage through the opening.

**F-rating determination:**

System receives F-rating equal to test duration until:
- Sustained flaming on unexposed side (>10 seconds)
- Cotton waste ignition from hot gases
- Opening development allowing flame passage
- Test termination at specified time

**Minimum F-rating requirement:**

$$F_{rating} \geq R_{assembly}$$

Example: 2-hour rated wall requires minimum 2-hour F-rated firestop system.

**Available F-ratings:**
- 1/2 hour, 1 hour, 1-1/2 hours, 2 hours, 3 hours, 4 hours

Some firestop systems achieve F-ratings exceeding the assembly rating, providing additional safety margin.

### T-Rating: Temperature Rise Limitation

The T-rating measures temperature rise on the unexposed side of floor penetrations, ensuring heat transfer does not ignite combustibles in contact with the penetration.

**T-rating criteria:**

Temperature on unexposed surface must not exceed:
$$\Delta T_{max} = 325°F \text{ above ambient}$$

T-rating equals time until this temperature rise occurs.

**T-rating requirements by assembly type:**

| Assembly Type | T-Rating Required? |
|---------------|-------------------|
| Vertical (walls) | No |
| Horizontal (floors) with combustibles above | Yes |
| Horizontal (floors) with membrane ceiling below | Optional* |

*Some jurisdictions require T-rating for all floor penetrations.

**Temperature rise calculation:**

$$\Delta T = T_{unexposed} - T_{ambient}$$

Where:
- $\Delta T$ = Temperature rise (°F)
- $T_{unexposed}$ = Temperature at unexposed surface (°F)
- $T_{ambient}$ = Ambient temperature before test (typically 68-72°F)

When $\Delta T$ reaches 325°F, the T-rating time is established.

### L-Rating: Air Leakage (Optional)

Some firestop systems receive L-ratings for air leakage, though this is less common for HVAC applications:

**L-rating classes:**
- **Class A:** <1 cfm per sq ft at 0.30" w.g.
- **Class B:** <1 cfm per sq ft at 0.05" w.g.

L-ratings primarily apply to smoke barrier penetrations or where air infiltration control is critical.

## Firestop System Components and Materials

### Mineral Wool Products

Mineral wool (rock wool or ceramic fiber) is the most common firestop material for duct penetrations.

**Properties:**
- Non-combustible, melting point >2,000°F
- Compressible for filling irregular spaces
- Maintains integrity during fire exposure
- Available as batts, blankets, or loose fill

**Installation requirements:**
- Fill annular space completely
- Compress to specified density (typically 4-8 pcf)
- Minimum thickness per listing (typically 1" to 4")
- Support with temporary retention while installing

**Mineral wool density calculation:**

$$\rho = \frac{W}{V}$$

Where:
- $\rho$ = Installed density (pcf)
- $W$ = Weight of mineral wool (pounds)
- $V$ = Volume of annular space (cubic feet)

Ensure installed density meets listing requirements.

### Intumescent Materials

Intumescent products expand when exposed to heat, filling voids and insulating penetrating items.

**Types:**

**Intumescent sealants:**
- Gun-grade or trowel-grade consistency
- Applied to annular space surface
- Expand 3:1 to 10:1 at fire temperatures
- Typical thickness: 1/2" to 2"

**Intumescent wraps/collars:**
- Pre-formed bands or sheets
- Wrapped around penetrating duct
- Expand inward to crush and seal combustible penetrants
- Common for PVC and other plastic pipes

**Intumescent pads/pillows:**
- Pre-fabricated modules
- Placed in annular space
- Expand to fill opening
- Easy to install and remove for service access

**Expansion ratio:**

$$ER = \frac{V_{expanded}}{V_{original}}$$

Where:
- $ER$ = Expansion ratio
- $V_{expanded}$ = Volume after expansion at rated temperature
- $V_{original}$ = Original installed volume

Typical intumescent materials: 3:1 to 10:1 expansion.

### Cementitious and Mortar Products

Fire-resistive mortars and sprays provide rigid firestop barriers.

**Cementitious firestop mortar:**
- Gypsum or cement-based powder mixed with water
- Troweled into annular space
- Cures to hard, rigid mass
- Typical compressive strength: 300-500 psi
- Thickness: 1" to 4" depending on rating

**Spray-applied cementitious:**
- Applied pneumatically
- Builds up in layers
- Suitable for complex geometries
- May require wire mesh reinforcement

**Setting time and cure:**
- Initial set: 30 minutes to 2 hours
- Full cure: 24-72 hours
- Temperature-dependent
- Protect from freezing during cure

### Ablative Coatings

Specialized coatings form insulating char layers under fire exposure.

**Applications:**
- Cable tray penetrations
- Large duct penetrations
- Spray-applied directly to duct exterior
- Minimum dry film thickness (DFT) per listing

**Char formation:**
During fire, coating decomposes exothermically, producing:
- Expanded carbon char (insulation layer)
- Non-combustible gases (cooling effect)
- Char thickness 10-50 times original coating thickness

## Installation Requirements and Details

### Annular Space Definition and Sizing

The annular space is the gap between the penetrating item (duct) and the edge of the opening in the fire-rated assembly.

**Annular space calculation:**

For round ducts through round openings:
$$A_{annular} = \frac{\pi}{4}(D_{opening}^2 - D_{duct}^2)$$

For rectangular ducts:
$$A_{annular} = A_{opening} - A_{duct}$$

Where:
- $A_{annular}$ = Annular space area (sq in)
- $D_{opening}$ = Diameter of opening (inches)
- $D_{duct}$ = Duct diameter (inches)
- $A_{opening}$ = Opening area (sq in)
- $A_{duct}$ = Duct cross-sectional area (sq in)

**Annular space width:**

$$W_{annular} = \frac{D_{opening} - D_{duct}}{2}$$

**Listing limits:**
- **Minimum annular space:** Typically 1/2" to 1"
- **Maximum annular space:** Typically 2" to 4" (varies by system)

Annular space outside listed range requires different firestop system or opening modification.

### Sleeve Requirements

Metallic sleeves provide structure for firestop installation and protect penetration edges.

**Sleeve material:**
- Minimum 22-gauge galvanized steel (some systems allow 26-gauge)
- Stainless steel for corrosive environments
- Thickness must match firestop listing

**Sleeve length calculation:**

$$L_{sleeve} = T_{wall} + 2 \times P_{projection}$$

Where:
- $L_{sleeve}$ = Total sleeve length (inches)
- $T_{wall}$ = Wall or floor thickness (inches)
- $P_{projection}$ = Projection beyond assembly face (typically 1/2" to 1" minimum)

**Sleeve securement:**
- Anchor to assembly structure (not just gypsum board or plaster)
- Minimum 4 anchors per sleeve
- Expansion anchors, powder-actuated fasteners, or through-bolts
- Support sleeve weight independently

### Firestop Installation Steps

**Standard installation procedure:**

1. **Preparation:**
   - Verify opening size within firestop system listing
   - Install sleeve if required
   - Clean surfaces of dust, oil, loose debris
   - Verify duct material and gauge match listing

2. **Support installation:**
   - For mineral wool: Install temporary dam/backing material
   - Support from unexposed side when possible
   - Use non-combustible support (mineral wool backer, metal mesh)

3. **Firestop application:**
   - **Mineral wool:** Pack tightly to specified density, ensure complete fill
   - **Intumescent sealant:** Apply per manufacturer depth/width requirements
   - **Cementitious:** Mix per instructions, pack or trowel to required thickness
   - Work from unexposed side (fire side) when possible

4. **Finishing:**
   - Smooth exposed surface
   - Remove excess material
   - Verify complete fill with no voids

5. **Curing/setting:**
   - Protect wet materials from damage
   - Maintain temperature conditions for proper cure
   - Do not load or disturb until fully cured

6. **Labeling:**
   - Install permanent label identifying firestop system
   - Include UL system number, installer, date
   - Label visible from both sides when possible

### Through-Penetration Details

**Duct conditions within assembly:**

NFPA 90A and firestop listings require:
- No joints in duct within barrier thickness + 12" on both sides
- Duct must be continuous, rigid construction
- Support duct independently (not from sleeve or assembly)

**Prohibited within protected zone:**
- Spiral seam connections
- Pittsburgh lock seams
- Slip joints
- Flex duct connections
- Branch takeoffs

**Support spacing near penetrations:**

$$S_{support} \leq 10 \text{ ft} \text{ and } \leq 5 \text{ ft from penetration}$$

Supports must be on both sides of penetration.

### Fire Damper Integration

When fire dampers installed at penetrations:

**Damper-to-sleeve connection:**
- Damper frame secured to sleeve or directly to assembly
- Minimum 4 attachment points
- Sheet metal screws (#10 minimum) or bolts
- Verify attachment method per damper manufacturer

**Firestop around damper:**
- Fill annular space between sleeve and wall per firestop system
- Damper frame does not eliminate need for firestop
- Ensure firestop compatible with damper installation
- Maintain damper accessibility for inspection

**Combined ratings:**
Penetration assembly must satisfy:
- Damper rating ≥ assembly rating (max 3 hours)
- Firestop F-rating ≥ assembly rating
- T-rating if required for floor penetrations

## Special Conditions and Applications

### Flexible Duct Connections

Flexible duct presents challenges for firestop protection:

**Prohibition:**
Flexible duct NOT permitted through fire-rated assemblies in most jurisdictions.

**If allowed by AHJ:**
- Terminate flex duct minimum 5 feet from barrier
- Transition to rigid duct for penetration zone
- Use listed firestop system for rigid duct
- Protect transition point per NFPA 90A

### Insulated Duct Penetrations

External duct insulation complicates penetration protection:

**Option 1: Strip insulation at penetration**
- Remove insulation for minimum 12" both sides of barrier
- Install firestop around bare duct
- Resume insulation beyond protected zone
- Seal insulation vapor barrier to prevent condensation

**Option 2: Listed system for insulated ducts**
- Some firestop systems listed for insulated ducts
- Insulation thickness and type must match listing
- Often requires wider annular space
- May require special retention hardware

**Condensation control:**
For cold ducts, prevent condensation in uninsulated zone:
- Vapor seal at insulation terminations
- Consider insulated sleeve or enclosure
- Monitor for moisture accumulation

### Grease Ducts Through Fire-Rated Assemblies

Commercial kitchen grease exhaust requires special protection:

**NFPA 96 requirements:**
- 16-gauge welded steel grease duct minimum
- Clearance to combustibles: 18" minimum
- Penetration protection per NFPA 96 Section 8.4
- Firestop systems tested with grease duct if available

**Special considerations:**
- High-temperature firestop materials required
- Access for cleaning at penetrations
- Coordinate with automatic fire suppression
- Increased inspection frequency (semi-annual or quarterly)

### Seismic Applications

In seismic regions, accommodate building movement:

**Movement joints:**
Where penetrations cross seismic separation joints:
- Use listed dynamic firestop systems rated for movement
- Specify movement rating (±1/2", ±1", ±2", etc.)
- Test per UL 2079 for dynamic conditions

**Seismic movement calculation:**

$$\Delta_{seismic} = S_D \times L$$

Where:
- $\Delta_{seismic}$ = Expected seismic displacement (inches)
- $S_D$ = Design story drift ratio
- $L$ = Distance from penetration to building expansion joint (feet)

Select dynamic firestop system rated for $\Delta_{seismic}$ or greater.

## Field Testing and Quality Assurance

### Inspection Requirements

**During installation:**
- Verify firestop system matches approved submittal
- Check annular space dimensions
- Confirm material quantities and mixing ratios
- Observe installation technique
- Document with photographs before concealment

**After installation:**
- Verify complete fill of annular space (probe or visual)
- Check for voids or gaps
- Confirm proper curing/setting
- Verify labels installed
- Review documentation

### Third-Party Special Inspection

Building codes often require special inspection for firestop systems:

**IBC Section 1705.16:**
- Continuous special inspection for firestop installation
- Inspector qualified per AHJ requirements
- Certifications: ICC Fire Stop Inspector, FM or UL certifications
- Reports submitted to building official

**Inspection reports include:**
- Firestop system identification (UL number)
- Penetration location
- Penetrating item type and size
- Assembly type and rating
- Installation date and contractor
- Conformance statement

### Common Installation Deficiencies

**Incomplete fill:**
- Voids in annular space
- Insufficient material depth
- Gaps at edges

**Correction:** Remove and reinstall with complete fill.

**Wrong materials:**
- Materials not matching UL listing
- Substitution of "equivalent" products

**Correction:** Remove and reinstall with listed materials.

**Out-of-tolerance annular space:**
- Opening too large or too small for specified system

**Correction:** Core new opening to correct size or specify different firestop system.

**Improper duct conditions:**
- Joints within protected zone
- Duct material/thickness not per listing

**Correction:** Replace duct section with continuous, listed configuration.

## Documentation and Record Keeping

### Submittal Requirements

Design-phase submittals:

1. **Firestop schedule:**
   - Penetration location and ID number
   - Assembly type and rating
   - Penetrating item description
   - UL firestop system number
   - Installer qualifications

2. **Product data:**
   - Manufacturer technical data sheets
   - UL listing information with system details
   - Installation instructions
   - Material safety data sheets (SDS)

3. **Installation details:**
   - Typical penetration details on drawings
   - Special condition details
   - Coordination with other trades

### As-Built Documentation

Upon completion:

**Photographic record:**
- Each penetration before firestop installation (showing annular space)
- During installation (materials placement)
- After completion (finished condition)
- Labels showing UL system number

**Firestop system database:**
Maintain electronic or paper records:

| Field | Information |
|-------|-------------|
| Penetration ID | Unique identifier |
| Location | Building, floor, grid reference |
| Assembly type | Wall/floor, rating |
| UL system number | Specific firestop system |
| Penetrating item | Duct size, material |
| Installation date | When installed |
| Installer | Company and technician |
| Inspector | Who verified installation |
| Photos | Reference to photo documentation |

### Long-Term Maintenance

**Periodic inspection:**
- Annual visual inspection of accessible penetrations
- Check for damage, deterioration, modifications
- Verify labels remain in place and legible

**Modification control:**
- Prohibit unauthorized penetration modifications
- Require permit for new penetrations or duct changes
- Inspect and restore firestop after any work

**Record updates:**
- Document all repairs or modifications
- Update database with new penetrations
- Maintain records for life of building

## Code Requirements and Enforcement

### IBC Requirements

International Building Code Chapter 7 establishes penetration protection requirements:

**IBC Section 714.3:**
- Penetrations must be protected by approved methods
- Fire-resistance rating of assembly must be maintained
- Through-penetration firestop systems per ASTM E814 or UL 1479

**IBC Section 714.4:**
- Membrane penetrations (through one side only) have separate requirements
- Generally less restrictive than through-penetrations

**IBC Section 714.5:**
- Ducts and air transfer openings require fire dampers at specific locations
- Damper ratings per Section 717

### NFPA 90A Requirements

NFPA 90A Section 5.3 addresses penetrations:

**Key requirements:**
- Ducts penetrating fire-rated assemblies protected per IBC or NFPA 101
- Firestop systems installed per manufacturer instructions
- Maintain duct integrity within barrier thickness + 12"
- Fire dampers per Section 5.3.3

### Authority Having Jurisdiction (AHJ)

Local enforcement may exceed model codes:

**Typical AHJ requirements:**
- Special inspection mandatory for all firestop
- Specific approved product lists
- Enhanced documentation
- Stricter annular space limits

**Contractor responsibilities:**
- Understand local amendments to model codes
- Obtain required permits and inspections
- Maintain installer certifications
- Provide specified documentation

## Conclusion

Proper protection of duct penetrations through fire-rated assemblies is essential for maintaining building compartmentation and life safety. Firestop systems tested per ASTM E814 and UL 1479, when installed exactly as listed, preserve fire-resistance ratings and prevent fire spread through HVAC openings. Success requires careful coordination among designers who specify appropriate systems, contractors who install materials precisely per listings, and inspectors who verify code compliance. Understanding F-ratings, T-ratings, annular space requirements, and material properties enables proper system selection. Following manufacturer installation instructions, maintaining thorough documentation, and conducting quality assurance inspections ensures penetration fire protection performs as intended during fire events. The investment in proper firestop installation protects building occupants, limits property damage, and satisfies code requirements for fire-resistive construction.
