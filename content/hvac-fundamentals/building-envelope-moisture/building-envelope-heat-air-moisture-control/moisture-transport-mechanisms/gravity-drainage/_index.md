---
title: "Gravity Drainage"
aliases: ["Gravity Drainage"]
description: "Physics-based analysis of gravity-driven moisture transport in building envelopes including drainage plane design, weep system hydraulics, flow path geometry, and water management strategies for wall assemblies and roofing systems"
weight: 4
---

## Overview

Gravity drainage represents the primary mechanism for removing bulk water that penetrates the exterior cladding of building assemblies. This moisture transport mechanism relies on gravitational force to move liquid water downward through designed drainage cavities, planes, and exit pathways. Proper gravity drainage design prevents water accumulation within wall and roof assemblies, mitigating moisture-related damage including rot, corrosion, mold growth, and structural deterioration.

The effectiveness of gravity drainage systems depends on three fundamental requirements:

1. **Drainage cavity or plane** - continuous air space or material interface allowing water movement
2. **Downward flow path** - unobstructed vertical or sloped pathway for water to descend
3. **Exit pathway** - weeps, scuppers, or other openings for water to discharge from the assembly

Understanding the physics of gravity-driven flow, including laminar film flow on vertical surfaces and channel flow in cavities, enables proper design of drainage systems that function reliably throughout the building service life.

## Fundamental Physics

### Gravitational Driving Force

Gravity drainage occurs when the gravitational force component acting on a water mass exceeds the resistive forces (adhesion, cohesion, surface tension, friction). For water on a vertical or inclined surface:

**Gravitational force per unit volume:**
```
F_g = ρ_w × g × sin(θ)
```

Where:
- F_g = gravitational force per unit volume (N/m³)
- ρ_w = water density (1000 kg/m³ at 20°C)
- g = gravitational acceleration (9.81 m/s²)
- θ = angle from horizontal (90° for vertical surfaces)

**Critical water film thickness for drainage initiation:**

On vertical surfaces, water begins to drain when the film thickness exceeds a critical value determined by surface tension and wettability:

```
t_crit = √(2σ × cos(α) / (ρ_w × g))
```

Where:
- t_crit = critical film thickness (m)
- σ = surface tension of water (0.072 N/m at 20°C)
- α = contact angle (material dependent)
- ρ_w = water density (1000 kg/m³)
- g = gravitational acceleration (9.81 m/s²)

For most building materials (contact angle 40-80°), critical film thickness ranges from 0.5 to 2.0 mm.

### Laminar Film Flow on Vertical Surfaces

Water flowing down vertical surfaces within drainage cavities typically exhibits laminar film flow, described by the Nusselt solution for falling films:

**Velocity profile:**
```
v(y) = (ρ_w × g / μ) × (δ × y - y²/2)
```

Where:
- v(y) = velocity at distance y from wall (m/s)
- y = distance from wall surface (m)
- δ = film thickness (m)
- μ = dynamic viscosity of water (0.001 Pa·s at 20°C)

**Maximum velocity (at film surface):**
```
v_max = ρ_w × g × δ² / (2μ)
```

**Average velocity:**
```
v_avg = ρ_w × g × δ² / (3μ)
```

**Volumetric flow rate per unit width:**
```
Q' = ρ_w × g × δ³ / (3μ)
```

**Reynolds number for film flow:**
```
Re = 4 × ρ_w × v_avg × δ / μ = 4Q' × ρ_w / μ
```

Film flow remains laminar for Re < 1000, turbulent for Re > 2000.

## Drainage Plane Design

### Types of Drainage Planes

Building envelope assemblies incorporate drainage planes through various configurations:

#### Physical Air Gap Drainage

Creates a continuous open cavity between cladding and sheathing:

| Cavity Width | Flow Capacity | Applications | Limitations |
|--------------|---------------|--------------|-------------|
| 6-10 mm | Low | Residential veneer | Capillary bridging risk |
| 13-19 mm | Medium | Commercial masonry | Standard design |
| 25-38 mm | High | Rainscreen systems | Maximum reliability |
| 50-100 mm | Very High | Pressure-equalized rainscreen | Premium applications |

**Minimum cavity width determination:**

The cavity must be wide enough to prevent capillary water bridging from cladding to sheathing:

```
w_min = 2 × h_cap
```

Where h_cap is the capillary rise height in the cavity gap:

```
h_cap = 2σ × cos(α) / (ρ_w × g × w)
```

For contact angle α = 60° and cavity width w = 13 mm:
- h_cap = 0.46 mm (minimal capillary bridging risk)

#### Applied Membrane Drainage Plane

Water-resistive barriers (WRB) applied to sheathing create a drainage plane at the membrane surface:

- **Building paper** - asphalt-saturated felt (ASTM D226, D4869)
- **Synthetic WRB** - spun-bonded polyolefin, woven polyethylene (ASTM E2556)
- **Self-adhered membranes** - rubberized asphalt, butyl (ASTM D1970)
- **Fluid-applied membranes** - elastomeric coatings (ASTM C836)

**Critical drainage plane properties:**

| Property | Requirement | Test Method | Significance |
|----------|-------------|-------------|--------------|
| Water resistance | >140 Pa (20 psf) | ASTM E2357 | Prevents penetration under wind |
| Water vapor permeance | >57 ng/(Pa·s·m²) (10 perms) | ASTM E96 | Allows drying |
| Drainage efficiency | Low surface energy | Contact angle | Promotes water runoff |
| Continuity | Lapped, sealed | Visual | Prevents water intrusion paths |

#### Drainage Mat Systems

Three-dimensional drainage mats create separation and drainage channels:

- **Entangled net** - tangled polymer filaments (3-6 mm thick)
- **Dimpled sheet** - thermoformed cups (6-8 mm height)
- **Composite** - geotextile bonded to drainage core (6-10 mm)

**Drainage capacity:** Ranges from 5 to 50 L/(min·m) depending on mat thickness and structure.

### Drainage Plane Continuity

Continuous drainage planes require proper detailing at penetrations, transitions, and terminations:

**Vertical continuity:**
- Minimum 150 mm (6") overlap at horizontal joints
- Upper layer overlaps lower layer (shingle principle)
- Sealed joints for self-adhered membranes

**Horizontal continuity:**
- Minimum 150 mm overlap at vertical joints
- Located at solid backing (studs)
- Sealed or taped joints

**Termination points:**
- Base of wall: drainage plane directs to through-wall flashing
- Top of wall: drainage plane integrates with window head flashing
- Penetrations: membrane lapped over flanges or continuous with flashings

### Through-Wall Flashing

Through-wall flashing collects water from the drainage cavity and directs it to weep holes:

**Material selection:**

| Material | Thickness | Flexibility | Durability | Cost |
|----------|-----------|-------------|------------|------|
| Copper | 0.4-0.5 mm | Moderate | Excellent (50+ years) | High |
| Stainless steel | 0.3-0.4 mm | Low | Excellent (50+ years) | High |
| PVC | 0.5-1.0 mm | Good | Good (30+ years) | Low |
| Rubberized asphalt | 1.0-1.5 mm | Excellent | Good (20-30 years) | Moderate |
| EPDM | 1.1-1.5 mm | Excellent | Excellent (40+ years) | Moderate |

**Slope requirements:**

Through-wall flashings must slope toward exterior to promote drainage:

- **Minimum slope:** 1:50 (2%, 1/8" per foot)
- **Recommended slope:** 1:25 (4%, 1/4" per foot)
- **Maximum slope:** Limited by flashing material flexibility

**End dam design:**

End dams at terminations prevent water from exiting cavity laterally:

- **Height:** Minimum 50 mm above flashing
- **Sealed connection:** Bonded to sheathing/substrate
- **Continuous:** No gaps or openings

## Weep System Design

### Weep Hole Hydraulics

Weep holes provide controlled discharge points for gravity drainage. Flow through weeps depends on hole geometry, head pressure, and outlet conditions.

**Orifice flow equation (free discharge):**

```
Q = C_d × A × √(2gh)
```

Where:
- Q = flow rate (m³/s)
- C_d = discharge coefficient (0.6-0.65 for sharp-edged orifice)
- A = weep hole area (m²)
- g = gravitational acceleration (9.81 m/s²)
- h = head above weep centerline (m)

**Flow capacity per weep hole:**

For circular weep holes with 10 mm head above centerline:

| Diameter | Area | Flow Rate | Comments |
|----------|------|-----------|----------|
| 6 mm (1/4") | 28 mm² | 0.024 L/min | Minimum size |
| 10 mm (3/8") | 79 mm² | 0.069 L/min | Standard masonry |
| 13 mm (1/2") | 133 mm² | 0.115 L/min | Heavy drainage |
| 19 mm (3/4") | 283 mm² | 0.245 L/min | Maximum capacity |

**Weep hole sizing methodology:**

1. Estimate maximum water entry rate from wind-driven rain
2. Calculate required total weep area for drainage cavity section
3. Determine number and spacing of individual weep holes

**Example calculation:**

Wall section: 3 m height × 6 m width
Wind-driven rain penetration: 1% of facade exposure = 0.18 L/min (assuming 30 L/(m²·h) rain intensity)
Safety factor: 2.0

Required weep capacity: 0.18 × 2.0 = 0.36 L/min

Number of 10 mm diameter weeps: 0.36 / 0.069 = 5.2 → use 6 weeps

Weep spacing: 6000 mm / 6 = 1000 mm on center

### Weep Hole Spacing

Standard weep spacing recommendations:

**Masonry veneer (prescriptive codes):**
- **Maximum horizontal spacing:** 800 mm (32") o.c.
- **Maximum vertical spacing:** Every floor level
- **Additional locations:** Base of wall, above/below openings, shelf angles

**Rainscreen systems (performance-based):**
- **Based on drainage capacity analysis**
- Typical spacing: 400-600 mm (16-24") o.c.
- Closer spacing at high water load locations

**Panel systems:**
- Minimum two weeps per panel
- Located at low points of drainage cavity

### Weep Types and Components

#### Open Weeps

Direct openings through cladding with no inserts:

- **Advantages:** Maximum flow capacity, no blockage
- **Disadvantages:** Insect entry, visible, wind-driven rain entry
- **Applications:** Industrial, utilitarian construction

#### Screened Weeps

Weep holes with insect screen:

- **Screen material:** Stainless steel, bronze mesh (16-20 mesh)
- **Reduces capacity:** 20-30% due to screen resistance
- **Maintenance:** Requires periodic cleaning

#### Tube/Rope Weeps

Plastic tubes or woven rope inserts:

- **Tube diameter:** 6-10 mm
- **Rope material:** Cotton, synthetic fiber
- **Installation:** Continuous contact with flashing
- **Capacity:** Moderate, prone to clogging

#### Weep Vents

Engineered devices combining drainage and cavity ventilation:

- **Configuration:** Angled louvers or baffles
- **Functions:** Water discharge + air flow for drying
- **Performance:** Best balance of drainage, ventilation, insect resistance
- **Applications:** Premium residential, commercial

### Weep Hole Detailing

**Vertical alignment:**
- Bottom of weep: maximum 25 mm above through-wall flashing
- Ensures water contacts flashing before reaching weep
- Prevents water bypass below flashing

**Clearance from obstacles:**
- Maintain 20 mm clearance above sill plates, shelf angles
- Prevents water accumulation behind obstruction
- Allows visual inspection of drainage

**Flashing integration:**
- Weep at flashing low point
- End dams force water toward weeps
- Positive connection between flashing and weep

## Drainage Cavity Flow Dynamics

### Cavity Ventilation and Drying

Air movement through drainage cavities enhances drying of wetted surfaces:

**Driving mechanisms:**
1. **Stack effect:** Temperature-induced buoyancy (winter, sunny conditions)
2. **Wind pressure:** Differential pressure across cavity openings
3. **Combined effects:** Variable depending on weather conditions

**Natural ventilation flow rate (stack effect):**

```
Q_vent = C_d × A_eff × √(2ΔP/ρ_air)
```

Where pressure difference from stack effect:

```
ΔP = ρ_air × g × H × (T_cav - T_out) / T_avg
```

Where:
- Q_vent = ventilation flow rate (m³/s)
- C_d = discharge coefficient (0.6-0.65)
- A_eff = effective area of openings (m²)
- ΔP = pressure difference (Pa)
- ρ_air = air density (1.2 kg/m³)
- H = cavity height (m)
- T_cav = cavity temperature (K)
- T_out = outdoor temperature (K)

**Ventilation drying rate:**

```
m_dry = Q_vent × ρ_air × (W_sat - W_out)
```

Where:
- m_dry = moisture removal rate (kg/s)
- W_sat = humidity ratio at saturated cavity conditions (kg/kg)
- W_out = outdoor air humidity ratio (kg/kg)

### Cavity Obstructions and Blockages

Obstructions within drainage cavities impede water flow and create accumulation zones:

**Common obstruction types:**
- **Mortar bridging:** Mortar droppings on cavity ties
- **Insulation intrusion:** Poorly installed cavity insulation
- **Construction debris:** Dropped materials during construction
- **Shelf angles:** Horizontal structural supports
- **Fire blocking:** Code-required cavity subdivisions

**Obstruction mitigation strategies:**

| Obstruction | Prevention Method | Drainage Solution |
|-------------|-------------------|-------------------|
| Mortar droppings | Mortar collection devices, clean ties | Repeating flashings above ties |
| Debris | Clean cavity during construction | Cleanout openings at base |
| Shelf angles | Through-wall flashings at each level | Weeps at each flashing |
| Fire blocking | Maintain drainage path through blocking | Notched blocking + flashing |

**Repeating flashing system:**

At unavoidable horizontal obstructions (shelf angles, floor lines):

1. Install through-wall flashing above obstruction
2. Provide weeps at each flashing level
3. Create continuous drainage path in segmented cavities
4. Ensure each cavity section can drain independently

## Material Surface Properties

### Surface Energy and Wettability

Drainage efficiency depends on the wettability of drainage plane surfaces, quantified by contact angle:

**Contact angle ranges:**

| Material | Contact Angle | Wettability | Drainage Characteristics |
|----------|---------------|-------------|-------------------------|
| Glass, clean metal | 0-30° | Hydrophilic | Water spreads, forms thin films |
| Concrete, masonry | 30-60° | Moderate | Intermediate behavior |
| Polyethylene, polypropylene | 90-100° | Hydrophobic | Water beads, drains readily |
| PTFE, silicone | 110-120° | Highly hydrophobic | Excellent drainage |

**Effect on drainage velocity:**

Higher contact angle (more hydrophobic) increases drainage velocity by:
- Reducing adhesion between water and surface
- Promoting thicker, faster-moving water films
- Minimizing water retention on surface

**Surface treatment for enhanced drainage:**

- **Silane/siloxane coatings:** Increase contact angle 20-40°
- **Fluoropolymer treatments:** Increase contact angle 40-60°
- **Textured surfaces:** Can increase or decrease drainage depending on scale

### Surface Roughness Effects

Surface roughness influences drainage through competing mechanisms:

**Microscale roughness (< 0.1 mm):**
- Increases contact angle (Wenzel or Cassie-Baxter effect)
- Can enhance drainage on hydrophobic surfaces
- Can impede drainage on hydrophilic surfaces

**Macroscale roughness (> 1 mm):**
- Creates preferential flow paths
- May cause water retention in depressions
- Increases surface area for evaporation

**Optimal surface for gravity drainage:**
- Smooth to moderately textured (Ra < 5 μm)
- Hydrophobic surface energy (contact angle > 90°)
- Continuous without abrupt transitions

## Design Considerations and Best Practices

### Drainage System Hierarchy

Effective moisture management follows a hierarchical approach:

**Primary defense (shedding):**
- Roof overhangs
- Sloped surfaces
- Water-shedding cladding profiles

**Secondary defense (drainage):**
- Drainage planes and cavities
- Through-wall flashings
- Weep systems

**Tertiary defense (material resistance):**
- Water-resistive barriers
- Moisture-tolerant materials
- Drying capacity

Gravity drainage systems serve as the critical secondary defense, managing water that penetrates the primary cladding layer.

### Climate-Specific Design

Drainage system design requirements vary with climate:

**High rainfall climates (> 1000 mm annual):**
- Larger cavity widths (19-25 mm minimum)
- Increased weep capacity (closer spacing)
- Enhanced flashing systems
- Multiple drainage planes for critical applications

**Moderate rainfall climates (500-1000 mm annual):**
- Standard cavity widths (13-19 mm)
- Code-minimum weep spacing
- Single drainage plane

**Arid climates (< 500 mm annual):**
- Minimum cavity and weep provisions still required
- Focus on occasional intense rainfall events
- Prevent water entry rather than managing large volumes

**Cold climates:**
- Address freeze-thaw cycling effects
- Prevent ice blockage of weeps
- Consider drainage plane continuity with insulation

### Construction Quality Assurance

Gravity drainage systems fail most commonly due to construction defects rather than design flaws:

**Critical inspection points:**

1. **Drainage plane installation**
   - Proper overlap and continuity
   - Correct orientation (shingle principle)
   - Integration with adjacent components

2. **Through-wall flashing**
   - Positive slope to exterior
   - Sealed end dams
   - Extension beyond face of cladding

3. **Weep holes**
   - Correct spacing and location
   - Clear and unobstructed
   - Proper alignment with flashings

4. **Cavity cleanliness**
   - Remove mortar droppings and debris
   - Clean ties and anchors
   - Verify clear drainage path

**Mock-up testing:**

For critical projects, construct full-scale mock-ups and perform water testing:
- **ASTM E1105:** Standard test method for field water penetration testing
- **AAMA 501.2:** Water penetration testing of windows, curtain walls, and doors
- Spray rate: 3.4 L/(min·m²) (5 gal/(ft²·h))
- Test pressure: 137-720 Pa (20-105 psf) depending on exposure
- Test duration: 15 minutes minimum

### Maintenance and Long-Term Performance

Gravity drainage systems require periodic inspection and maintenance:

**Annual inspection:**
- Visual examination of weep holes (clear and functional)
- Check for water staining indicating drainage problems
- Verify no damage to flashings or drainage planes

**5-year inspection:**
- Water testing at representative locations
- Thermographic survey to identify moisture accumulation
- Invasive inspection at high-risk details

**Maintenance actions:**
- Clean clogged weep holes
- Clear obstructions from drainage cavities
- Repair damaged flashings or membranes

**Expected service life:**

| Component | Service Life | Replacement Trigger |
|-----------|--------------|---------------------|
| Through-wall flashing | 30-50+ years | Visible deterioration, leakage |
| Drainage plane membrane | 20-50 years | Loss of water resistance |
| Weep components | 20-30 years | Corrosion, clogging |
| Drainage cavity | Indefinite | Blockage, mortar bridging |

## Code Requirements and Standards

### Prescriptive Code Provisions

**International Building Code (IBC):**

*Section 1405.4 - Flashing*
- Flashings required at wall/roof intersections, above/below openings, built-in gutters, chimney intersections
- Flashing must be corrosion-resistant and impervious to moisture

*Section 1405.5 - Exterior wall coverings*
- Weather-resistant exterior wall envelope required
- Water-resistive barrier behind exterior veneer

**International Residential Code (IRC):**

*Section R703.1 - General*
- Weather-resistant exterior wall envelope with drainage plane

*Section R703.7 - Water-resistive barrier*
- Minimum one layer of No. 15 asphalt felt or approved equivalent
- Applied horizontally with upper layers lapped over lower layers

**Masonry veneer requirements:**

*IBC Section 1405.10 / IRC Section R703.8*
- Weep holes required at maximum 33 inches (838 mm) on center
- Weeps required above all flashing locations
- Minimum 1-inch (25 mm) clear air space behind veneer

### Performance-Based Standards

**ASTM Standards:**

- **ASTM E2112** - Standard practice for installation of exterior windows, doors, and skylights
  - Addresses flashing and drainage plane integration

- **ASTM E2266** - Standard guide for design and construction of low-rise frame building wall systems to resist water intrusion
  - Comprehensive drainage plane design guidance

- **ASTM E2556** - Standard specification for vapor permeable flexible sheet water resistive barriers
  - Performance requirements for WRB drainage planes

**ASHRAE Standards:**

- **ASHRAE 160** - Criteria for moisture-control design analysis in buildings
  - Hygrothermal analysis including drainage plane modeling

- **ASHRAE Handbook - Fundamentals, Chapter 26** - Heat, air, and moisture control in building assemblies
  - Theoretical basis for drainage plane design

### Manufacturer Requirements

Drainage system components must meet manufacturer specifications for:

- Material properties (strength, flexibility, durability)
- Installation methods (fastening, overlap, sealing)
- Compatibility with adjacent materials
- Warranty requirements

Follow manufacturer instructions to maintain product warranties and ensure proper system performance.

## Integration with Other Moisture Control Strategies

Gravity drainage functions as one component of comprehensive moisture control:

**Relationship to air barriers:**
- Air barrier prevents wind-driven rain penetration pressure
- Reduces water load on drainage system
- Separate but integrated layers

**Relationship to vapor control:**
- Drainage plane must not block drying potential
- Vapor-permeable drainage planes allow inward/outward drying
- Consider vapor profile in assembly design

**Relationship to capillary breaks:**
- Drainage cavity width exceeds capillary bridging distance
- Prevents water transfer from cladding to sheathing
- Capillary break materials at base of cavity

**Relationship to material selection:**
- Drainage provides moisture management for moisture-sensitive materials
- Allows use of higher-performance (sometimes less moisture-tolerant) materials
- Reduces moisture exposure of structural components

## Conclusion

Gravity drainage represents a passive, reliable moisture transport mechanism requiring no energy input beyond gravitational force. Proper design ensures bulk water removal from building envelope cavities, preventing moisture accumulation and associated damage. Key design principles include:

- Continuous, unobstructed drainage planes or cavities
- Properly sloped through-wall flashings directing water to exterior
- Adequate weep hole capacity and spacing for expected water loads
- Integration with flashing systems, air barriers, and vapor control layers
- Construction quality assurance to ensure system continuity and function

When designed according to established principles and constructed with attention to critical details, gravity drainage systems provide effective moisture management throughout the building service life with minimal maintenance requirements. This passive approach offers superior reliability compared to active systems requiring mechanical components or energy input.

## References

- ASHRAE Handbook - Fundamentals, Chapter 26: Heat, Air, and Moisture Control in Building Assemblies
- ASTM E2266: Standard Guide for Design and Construction of Low-Rise Frame Building Wall Systems to Resist Water Intrusion
- Lstiburek, J. W. (2006). Builder's Guide to Cold Climates. Building Science Press
- Straube, J. F., & Burnett, E. (2005). Building Science for Building Enclosures. Building Science Press
- International Building Code (IBC), Current Edition
- Brick Industry Association, Technical Notes on Brick Construction
- Canadian Mortgage and Housing Corporation (CMHC), Best Practice Guide: Water Management
