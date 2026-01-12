---
title: "Flat Roof Systems"
description: "Comprehensive analysis of flat and low-slope roof assemblies including membrane types, insulation strategies, vapor control, and moisture management to prevent interstitial condensation and ensure long-term performance."
weight: 4
---

Flat and low-slope roof systems (slopes less than 2:12 or 9.5 degrees) present unique moisture control challenges due to limited drainage capability, potential for standing water, and vulnerability to interstitial condensation. Proper assembly design requires careful consideration of vapor drive direction, thermal performance, and material compatibility.

## Roof System Classifications

Flat roof assemblies are categorized by the position of the waterproofing membrane relative to insulation and structural deck.

### Conventional Roof Assembly (CRA)

The traditional assembly places insulation above the structural deck with the waterproofing membrane on top of the insulation.

**Layer sequence (bottom to top):**
- Structural deck (concrete, steel, wood)
- Vapor retarder (if required)
- Insulation board(s)
- Cover board or thermal barrier
- Waterproofing membrane
- Surfacing (gravel, pavers, coating)

**Advantages:**
- Membrane protected from UV degradation and mechanical damage
- Insulation remains dry under normal conditions
- Established design with proven performance history
- Wide range of insulation types compatible

**Disadvantages:**
- Membrane exposed to full thermal cycling
- Risk of membrane splitting at insulation joints
- Vapor retarder position critical in cold climates
- Difficult to locate leaks due to water migration

### Protected Membrane Roof (PMR) / Inverted Roof Membrane Assembly (IRMA)

The inverted assembly places insulation above the waterproofing membrane, protecting the membrane from thermal stress and UV exposure.

**Layer sequence (bottom to top):**
- Structural deck
- Waterproofing membrane (applied directly to deck)
- Insulation (extruded polystyrene required)
- Drainage mat or separation layer
- Ballast (gravel, pavers, or vegetated system)

**Advantages:**
- Membrane protected from thermal cycling (extends service life)
- Membrane operates at moderate temperatures year-round
- No vapor retarder typically required
- Easy leak detection (membrane at accessible level)
- Excellent for retrofit applications

**Disadvantages:**
- Insulation exposed to moisture (requires closed-cell XPS)
- Higher insulation R-value needed to compensate for thermal bypasses
- Ballast adds significant dead load (12-25 psf)
- Wind uplift resistance depends on ballast weight
- Limited insulation type options

**Thermal performance correction:**

The effective R-value of insulation in PMR assemblies is reduced due to:
1. Rainwater cooling insulation surface
2. Air circulation under ballast
3. Water absorption in insulation board edges

Correction factor for effective R-value:

```
R_effective = R_nominal × (0.85 to 0.90)
```

ASHRAE 90.1 requires using effective R-values when demonstrating code compliance for PMR assemblies.

### Hybrid or Compact Roof Assembly

Combines elements of both conventional and protected membrane systems, with insulation both above and below the membrane.

**Layer sequence:**
- Structural deck
- Vapor retarder (if required)
- Insulation layer 1 (below membrane)
- Waterproofing membrane
- Insulation layer 2 (above membrane, XPS only)
- Ballast or pavers

**Design rationale:**
- Splits insulation R-value between layers
- Reduces membrane temperature extremes
- Allows vapor retarder when needed (below membrane)
- Provides redundant thermal protection

## Vapor Retarder Requirements and Placement

Vapor retarder necessity and placement depends on climate, interior humidity, and assembly configuration.

### Vapor Drive Analysis

Vapor drive direction varies seasonally:

**Winter (heating climate):**
- Interior vapor pressure > Exterior vapor pressure
- Drive direction: Upward (interior to exterior)
- Risk: Condensation at underside of cold membrane or within insulation

**Summer (with air conditioning):**
- Exterior vapor pressure > Interior vapor pressure
- Drive direction: Downward (exterior to interior)
- Risk: Condensation at underside of deck if impermeable membrane prevents drying

### Vapor Retarder Selection Criteria

Per ASHRAE 90.1 and International Energy Conservation Code (IECC), vapor retarders are classified by permeance:

| Class | Permeance (perms) | Material Examples |
|-------|-------------------|-------------------|
| I - Vapor Impermeable | ≤ 0.1 | Sheet polyethylene, rubberized asphalt membrane, built-up roofing |
| II - Vapor Semi-Impermeable | > 0.1 and ≤ 1.0 | Kraft-faced insulation, asphalt-coated paper |
| III - Vapor Semi-Permeable | > 1.0 and ≤ 10 | Latex paint, some coating membranes |

**Climate-based requirements (IECC):**

Climate zones 1-4 (heating dominated):
- Vapor retarder required when interior design RH > 45% at 68°F
- Class I or II vapor retarder placed below insulation

Climate zones 5-8 (cold climates):
- Vapor retarder typically required for all assemblies
- Class I vapor retarder recommended for high-humidity occupancies

**Exceptions for PMR assemblies:**
- No vapor retarder required regardless of climate
- Membrane at deck level functions as air barrier and limits upward vapor drive
- Insulation above membrane prevents membrane from reaching dew point

### Dewpoint Calculation for Vapor Retarder Placement

The critical interface temperature must remain above the dewpoint of interior air to prevent condensation.

**Given:**
- T_interior = Interior design temperature (°F)
- T_exterior = Exterior design temperature (°F)
- RH_interior = Interior relative humidity (%)
- R_below = R-value below interface (deck + vapor retarder + insulation below)
- R_above = R-value above interface (insulation above + membrane + surfacing)
- R_total = R_below + R_above

**Interface temperature:**

```
T_interface = T_exterior + [(T_interior - T_exterior) × (R_above / R_total)]
```

**Interior dewpoint temperature (approximate):**

For RH = 50% at 70°F: T_dp ≈ 50°F
For RH = 60% at 70°F: T_dp ≈ 55°F
For RH = 70% at 70°F: T_dp ≈ 60°F

**Design criterion:**

```
T_interface > T_dewpoint + 5°F (safety margin)
```

If criterion not met, options include:
1. Increase R_below (add insulation below vapor retarder)
2. Decrease interior humidity through ventilation or dehumidification
3. Use PMR assembly eliminating need for vapor retarder

## Waterproofing Membrane Systems

### Built-Up Roofing (BUR)

Multi-ply system consisting of alternating layers of bitumen (asphalt or coal tar) and reinforcing felts.

**Typical configuration:**
- 3 to 5 plies of organic or fiberglass felt
- Hot-mopped asphalt (Type I, II, III, or IV based on slope and application)
- Flood coat and aggregate surfacing (20 lb/sq gravel)

**Bitumen types and properties:**

| Type | Softening Point (°F) | Application | Slope Limit |
|------|---------------------|-------------|-------------|
| Type I (Dead Level) | 135-151 | Flat roofs | 0.5:12 max |
| Type II (Flat) | 158-176 | Low slope | 1:12 max |
| Type III (Steep) | 185-205 | Steeper slopes | 3:12 max |
| Type IV (Special Steep) | 210-225 | Vertical surfaces | > 3:12 |

**Performance characteristics:**
- Service life: 15-30 years depending on maintenance
- Self-healing capability at laps and penetrations
- Redundant waterproofing layers
- Resistance to standing water
- Heavy mass provides hail resistance

**Limitations:**
- Installation requires hot asphalt (safety concerns)
- Odor and fumes during installation
- Limited cold-weather installation window
- Relatively heavy (5-7 psf)

### Modified Bitumen Membranes

Factory-fabricated sheets of asphalt modified with polymers for improved performance.

**Polymer types:**

1. **APP (Atactic Polypropylene):**
   - Thermoplastic modifier
   - Higher temperature resistance
   - Applied via torch welding or hot asphalt
   - Better performance in hot climates

2. **SBS (Styrene-Butadiene-Styrene):**
   - Elastomeric modifier (rubber-like)
   - Flexible at low temperatures
   - Applied via torch, hot asphalt, or cold adhesive
   - Better performance in cold climates

**Reinforcement options:**
- Polyester mat (higher strength and elongation)
- Fiberglass mat (higher dimensional stability)
- Composite (polyester/fiberglass)

**Installation methods:**

| Method | Description | Advantages | Limitations |
|--------|-------------|------------|-------------|
| Torch-applied | Propane torch melts underside | Fast, strong bond | Fire risk, skilled labor required |
| Hot-mopped | Applied in hot asphalt | Similar to BUR, proven | Fumes, hot kettle required |
| Cold-applied | Solvent or water-based adhesive | Safer, cooler weather | Slower cure, temperature-sensitive |
| Self-adhered | Peel-and-stick backing | Clean, safe, fast | Premium cost, deck prep critical |

**System configurations:**
- Single-ply: Base sheet (mechanically attached) + modified cap sheet
- Two-ply: Two modified bitumen plies fully adhered
- Hybrid BUR: 2-3 BUR plies + modified cap sheet

### Single-Ply Membranes

Factory-fabricated sheets of synthetic polymer or rubber applied in a single layer.

#### Thermoset Membranes (EPDM, CSPE)

**EPDM (Ethylene Propylene Diene Monomer):**
- Synthetic rubber membrane
- Thickness: 45, 60, or 90 mils
- Width: Up to 50 feet (reduces seams)
- Black color (absorbs solar heat)
- Seam types: Tape-applied or liquid adhesive

**Performance:**
- Service life: 20-30+ years
- Excellent UV and ozone resistance
- Flexible at low temperatures (-40°F)
- Resistant to standing water
- Low thermal expansion/contraction

**Attachment methods:**
1. Fully adhered (bonding adhesive)
2. Mechanically attached (plates and fasteners)
3. Ballasted (loose-laid with gravel or pavers)

#### Thermoplastic Membranes (PVC, TPO, KEE)

**PVC (Polyvinyl Chloride):**
- Thermoplastic polymer with plasticizers
- Thickness: 45, 60, or 80 mils
- Heat-welded seams (hot air welding)
- White or light colors (high solar reflectance)
- Excellent chemical resistance

**TPO (Thermoplastic Polyolefin):**
- Blend of polypropylene and ethylene-propylene rubber
- Thickness: 45, 60, or 80 mils
- Heat-welded seams
- White or tan colors
- Lower cost than PVC

**Seam welding:**
- Hot air welding (most common): 900-1100°F air temperature
- Seam strength exceeds membrane tensile strength
- Testable with probe or destructive peel test
- Minimum weld width: 1.5 inches

**Performance comparison:**

| Property | EPDM | PVC | TPO |
|----------|------|-----|-----|
| Seam method | Adhesive/tape | Heat weld | Heat weld |
| Cold flexibility | Excellent | Good | Good |
| Heat aging | Excellent | Very good | Good |
| Plasticizer migration | None | Potential issue | None |
| Chemical resistance | Good | Excellent | Very good |
| Cost (relative) | Low | High | Medium |

## Insulation Materials and Placement

### Insulation Types for Flat Roofs

**Polyisocyanurate (polyiso):**
- R-value: 5.6-6.5 per inch (at 75°F mean temperature)
- Temperature-dependent performance (decreases in cold weather)
- Faced with glass fiber mat or foil
- Most common for conventional assemblies
- Not suitable for above-membrane applications (PMR)

**Extruded Polystyrene (XPS):**
- R-value: 5.0 per inch
- Closed-cell structure (water-resistant)
- Performance stable across temperatures
- Required for PMR/IRMA applications
- Higher compressive strength than EPS

**Expanded Polystyrene (EPS):**
- R-value: 3.8-4.4 per inch (by type)
- Lower cost than XPS
- More permeable than XPS (can dry if wetted)
- Used in tapered systems and specialty applications
- Requires cover board for most membranes

**Spray Polyurethane Foam (SPF):**
- R-value: 6.0-7.0 per inch
- Applied as liquid, expands and cures
- Monolithic (seamless) insulation and air barrier
- Self-adhered to substrate
- Requires protective coating

### Tapered Insulation Systems

Tapered insulation creates positive drainage to roof drains, eliminating standing water.

**Design parameters:**
- Minimum slope: 1/4 inch per foot (2%)
- Recommended slope: 1/2 inch per foot (4%) for critical areas
- Slope to drains, scuppers, or roof edges
- Crickets at penetrations and direction changes

**Slope calculation for drainage time:**

Time for water to drain from roof surface:

```
t = (L × n) / (60 × S^0.5)
```

Where:
- t = Time (minutes)
- L = Drainage path length (feet)
- n = Manning's roughness coefficient (0.016 for smooth membrane)
- S = Slope (ft/ft)

**Example:** 100-foot drainage path at 1/4:12 slope (0.021 ft/ft)
```
t = (100 × 0.016) / (60 × 0.021^0.5) = 1.8 minutes
```

### Insulation Attachment

**Mechanical attachment:**
- Plates and fasteners through insulation to deck
- Spacing per wind uplift calculations
- FM Global or UL 580 ratings for wind resistance

**Adhesive attachment:**
- Low-rise foam adhesive (beads or ribbons)
- Full-spread cold adhesive
- Hot asphalt (for polyiso with appropriate facer)

**Attachment density calculation:**

Required fasteners per square (100 sq ft):

```
N = (F_uplift × A) / (F_fastener × SF)
```

Where:
- N = Number of fasteners per square
- F_uplift = Design wind uplift pressure (psf)
- A = Area per square (100 sq ft)
- F_fastener = Fastener pullout strength (lbf)
- SF = Safety factor (typically 2.0)

## Interstitial Condensation Analysis

### Condensation Potential Assessment

Interstitial condensation occurs when water vapor diffuses through the assembly and reaches a surface below the dewpoint temperature.

**Glaser Method (simplified steady-state analysis):**

1. Calculate temperature profile through assembly
2. Determine dewpoint at each interface
3. Compare actual temperature to dewpoint
4. Identify condensation plane(s)

**Temperature at interface i:**

```
T_i = T_exterior + [(T_interior - T_exterior) × (R_i / R_total)]
```

Where:
- R_i = Total R-value from exterior to interface i
- R_total = Total assembly R-value

**Vapor pressure at interface i:**

```
P_i = P_interior × (R_v,i / R_v,total)
```

Where:
- R_v,i = Vapor resistance from interior to interface i (perm-inches)
- R_v,total = Total vapor resistance of assembly

**Condensation criterion:**

Condensation occurs if: P_i > P_sat(T_i)

Where P_sat(T_i) is the saturation vapor pressure at temperature T_i.

### Design Strategies to Prevent Condensation

**1. Control interior humidity:**
- Mechanical ventilation to maintain RH < 40% in winter
- Dehumidification for indoor pools, kitchens, laundries
- Source control (exhaust at moisture generation points)

**2. Use adequate insulation:**
- Increase total R-value to raise interface temperatures
- Maintain first condensing surface above dewpoint

**3. Position vapor retarder correctly:**
- Place on warm (interior) side of insulation
- Calculate required R-value above vapor retarder

**4. Use PMR assembly:**
- Eliminates vapor retarder requirement
- Membrane remains warm year-round

**5. Provide drying capacity:**
- Avoid multiple vapor retarders (vapor traps)
- Allow outward drying in summer months
- Use "smart" vapor retarders (variable permeance)

### Critical Ratio Method (ASHRAE)

The ratio of R-value above the condensing surface to total R-value must exceed a critical value.

**Required ratio:**

```
(R_above / R_total) > (T_interior - T_dewpoint) / (T_interior - T_exterior)
```

**Example calculation:**

Interior: 70°F, 50% RH (dewpoint = 50°F)
Exterior: 0°F (99% winter design condition)
Total R-value: R-30

```
Required ratio > (70 - 50) / (70 - 0) = 20/70 = 0.286
Minimum R_above = 0.286 × 30 = R-8.6
```

Therefore, place vapor retarder with at least R-9 above it (between vapor retarder and exterior).

## Drainage and Water Management

### Primary Drainage System

**Roof drain sizing:**

Required drain flow capacity per ASRAE/IPC:

```
Q = (A × i) / 96.3
```

Where:
- Q = Flow rate (gpm)
- A = Drainage area (sq ft)
- i = Rainfall intensity (inches/hour) for 100-year, 1-hour storm

**Drain spacing:**
- Maximum area per drain: 10,000 sq ft (typical)
- Maximum distance to drain: 150 feet (typical)
- Minimum 2 drains per roof area (redundancy)

**Sump depth:**
- Minimum 1/2 inch below field of roof
- Recommended 1 inch depth for positive drainage
- Gradual taper over 2-3 feet radius

### Secondary (Emergency) Drainage

Required by IBC for all roofs where interior drainage is used.

**Options:**
1. Secondary roof drains (independent piping to daylight)
2. Scuppers through parapet wall
3. Overflow edge at minimum point

**Capacity requirement:**
- Equal to or greater than primary system capacity
- Activates when primary system blocked or overwhelmed
- Overflow at elevation 2 inches above primary drain inlet

**Scupper sizing:**

Per IPC, scupper width (inches):

```
W = Q / (2.5 × H^0.5)
```

Where:
- W = Width (inches)
- Q = Required flow (gpm)
- H = Head (inches) - typically 4 inches

## Design Best Practices

### Assembly Selection Matrix

| Climate | Interior RH | Assembly Type | Vapor Retarder | Insulation Location |
|---------|-------------|---------------|----------------|---------------------|
| Cold (5-8) | < 45% | Conventional | Class II-III | Above deck |
| Cold (5-8) | > 45% | Conventional | Class I | Above deck |
| Cold | Any | PMR | None | Above membrane |
| Hot-humid (1-3) | With AC | Conventional | None or Class III | Above deck |
| Mixed (4) | < 45% | Conventional | None or Class III | Above deck |
| Mixed (4) | > 45% | Conventional or Hybrid | Class II | Split above/below membrane |

### Penetration Flashing Details

All roof penetrations require properly designed and installed flashing:

**Pipe penetrations:**
- Base flashing: 8 inches onto roof surface minimum
- Counter flashing or storm collar on pipe
- Pitch pan as last resort only (not preferred)

**HVAC equipment curbs:**
- Factory-fabricated curb recommended
- Minimum 8-inch curb height above roof surface
- Fully integrated base flashing
- Cant strip or tapered edge at curb base
- Drainage away from curb on all sides

**Mechanical equipment considerations:**
- Prefabricated equipment supports elevate above roof surface
- Prevents standing water under equipment
- Allows membrane inspection and maintenance
- Maintains drainage patterns

### Service Life Considerations

Expected service life by membrane type (with proper maintenance):

| Membrane Type | Expected Life (years) | Maintenance Frequency |
|---------------|----------------------|----------------------|
| Built-up roof (BUR) | 15-30 | Bi-annual inspections |
| Modified bitumen | 20-30 | Annual inspections |
| EPDM (ballasted) | 25-35 | Annual inspections |
| EPDM (adhered/mechanical) | 20-30 | Annual inspections |
| PVC | 20-30 | Annual inspections |
| TPO | 15-25 | Annual inspections |
| SPF (with coating) | 20-30 | 5-year recoating |

**Factors reducing service life:**
- Ponding water (> 48 hours after rain)
- Inadequate drainage
- Foot traffic without walkway pads
- Hail damage (depends on membrane thickness)
- UV exposure (non-ballasted systems)
- Thermal cycling (conventional > PMR)
- Chemical exposure (kitchen exhaust, pollution)

### Code and Standards References

**ASHRAE Standards:**
- ASHRAE 90.1: Energy Standard for Buildings (insulation requirements)
- ASHRAE 160: Criteria for Moisture-Control Design Analysis

**Building Codes:**
- International Building Code (IBC): Structural and fire requirements
- International Energy Conservation Code (IECC): Thermal performance
- International Plumbing Code (IPC): Roof drainage requirements

**Industry Standards:**
- ASTM D6162: Standard Specification for Styrene Butadiene Styrene (SBS) Modified Bituminous Sheet Materials
- ASTM D6163: Standard Specification for Atactic Polypropylene (APP) Modified Bituminous Sheet Materials
- ASTM D4434: Standard Specification for Poly(Vinyl Chloride) Sheet Roofing
- ASTM D6878: Standard Specification for Thermoplastic Polyolefin Based Sheet Roofing

**Industry Organizations:**
- National Roofing Contractors Association (NRCA): Roofing Manual
- RCI, Inc. (Roof Consultants Institute): Design guidelines
- FM Global: Property Loss Prevention Data Sheets
- UL (Underwriters Laboratories): Fire and wind ratings

### Quality Control During Installation

**Pre-installation requirements:**
- Verify deck is dry, clean, and structurally sound
- Confirm positive drainage (water test if necessary)
- Install temporary drains during construction
- Protect interior from water damage during installation

**Installation monitoring:**
- Weather limitations (temperature, precipitation, wind)
- Proper material storage and handling
- Seam inspection (especially for single-ply)
- Adhesive coverage verification
- Fastener pull tests for mechanical attachment

**Post-installation testing:**
- Electronic leak detection (ELD) for critical applications
- Flood testing at drains and penetrations
- Infrared thermography to identify wet insulation
- Core samples to verify assembly as designed

## Special Considerations

### Green Roof Integration

Vegetated roof assemblies require modified waterproofing approach:

**Assembly components (bottom to top):**
- Structural deck
- Waterproofing membrane (root-resistant)
- Root barrier (if membrane not root-resistant)
- Drainage layer
- Filter fabric
- Growing medium
- Vegetation

**Moisture implications:**
- Membrane remains saturated (no drying potential)
- Requires root-resistant membrane or barrier
- Higher humidity at membrane level
- Cooling effect reduces membrane temperature extremes

### Photovoltaic (PV) System Integration

Roof-mounted PV systems affect moisture performance:

**Ballasted PV:**
- Compatible with PMR assemblies
- Minimal membrane penetrations
- PV shading reduces membrane temperature cycling

**Mechanically attached PV:**
- Penetrations must be properly flashed
- Structural attachments through membrane require special details
- Wind uplift analysis critical

**Moisture considerations:**
- Shaded areas under panels stay cooler and wetter
- Reduced drying potential under arrays
- Condensation potential on underside of panels

### Re-roofing Strategies

Options for existing flat roof replacement:

**1. Complete tear-off and replacement:**
- Remove all existing roofing to deck
- Inspect and repair deck
- Install new assembly per current codes
- Most expensive, most comprehensive

**2. Recover (overlay new over existing):**
- New membrane over existing (if structurally adequate)
- Limited to one recover per most codes
- Must verify no moisture in existing insulation
- Cost-effective but increases dead load

**3. Retrofit to PMR:**
- Install new membrane over existing roof
- Add XPS insulation over new membrane
- Ballast or paver surfacing
- Protects both old and new membranes

**Moisture assessment before re-roofing:**
- Infrared thermography scan
- Nuclear moisture meter survey
- Roof core samples
- Remove and replace wet insulation
