---
title: "Capillary Action"
description: "Physics of capillary moisture transport in porous building materials including wicking mechanisms, capillary pressure calculations, and transport coefficients for HVAC envelope design"
weight: 3
---

Capillary action represents the movement of liquid water through the interconnected pore structure of building materials driven by surface tension forces at the liquid-solid-air interface. This transport mechanism operates independently of gravity and can move moisture both horizontally and vertically through porous materials such as masonry, concrete, wood, and insulation. Understanding capillary transport is essential for preventing moisture accumulation, freeze-thaw damage, and thermal performance degradation in building envelopes.

## Physical Principles

### Surface Tension Fundamentals

The driving force for capillary action originates from the surface tension of water and its interaction with solid surfaces.

**Surface Tension:**

γ = F/L

Where:
- γ = surface tension (N/m)
- F = force acting tangent to the surface (N)
- L = length over which force acts (m)

For water at 20°C: γ = 0.0728 N/m

**Interfacial Energy Balance:**

At the solid-liquid-air interface, three surface tensions interact:
- γ_SL = solid-liquid interfacial tension
- γ_SA = solid-air interfacial tension
- γ_LA = liquid-air surface tension

The equilibrium contact angle θ satisfies Young's equation:

γ_SA = γ_SL + γ_LA × cos(θ)

**Contact Angle Significance:**

| Material Type | Contact Angle (θ) | Wetting Behavior |
|--------------|-------------------|------------------|
| Hydrophilic | 0° - 90° | Water wets surface |
| Hydrophobic | 90° - 180° | Water beads on surface |
| Concrete | 30° - 60° | Moderate wetting |
| Brick | 40° - 70° | Moderate wetting |
| Wood (radial) | 60° - 80° | Limited wetting |
| Glass | 0° - 10° | Complete wetting |
| Silicone coating | 110° - 130° | Water repellent |

### Capillary Pressure

The pressure difference across a curved liquid-air interface drives capillary flow.

**Young-Laplace Equation (Cylindrical Pore):**

P_cap = (2 × γ × cos(θ)) / r

Where:
- P_cap = capillary pressure (Pa)
- γ = surface tension (N/m)
- θ = contact angle (degrees)
- r = pore radius (m)

**Capillary Rise in Vertical Tube:**

h = (2 × γ × cos(θ)) / (ρ × g × r)

Where:
- h = height of capillary rise (m)
- ρ = liquid density (kg/m³)
- g = gravitational acceleration (9.81 m/s²)
- r = tube radius (m)

**Example Calculation:**

For water in a concrete pore with r = 10 μm (10 × 10⁻⁶ m):

P_cap = (2 × 0.0728 × cos(45°)) / (10 × 10⁻⁶)
P_cap = (2 × 0.0728 × 0.707) / (10 × 10⁻⁶)
P_cap = 10,290 Pa ≈ 10.3 kPa

h = (2 × 0.0728 × 0.707) / (1000 × 9.81 × 10 × 10⁻⁶)
h = 1.05 m

This demonstrates that small pores generate substantial capillary pressures and significant rise heights.

### Pore Size Distribution

Real building materials contain a distribution of pore sizes that determines capillary transport characteristics.

**Effective Pore Radius:**

Most materials have complex pore structures characterized by:
- Micropores: r < 0.1 μm (strong capillary forces)
- Mesopores: 0.1 μm < r < 10 μm (moderate capillary forces)
- Macropores: r > 10 μm (weak capillary forces)

**Critical Pore Size:**

The largest pore diameter that remains filled at a given capillary pressure:

r_crit = (2 × γ × cos(θ)) / P_cap

Smaller pores fill first and retain water more strongly during drying.

## Capillary Transport Coefficients

### Liquid Water Permeability

The ability of a material to transport liquid water under a capillary pressure gradient.

**Darcy's Law for Liquid Flow:**

q = -(k_l / μ) × ∇P_cap

Where:
- q = liquid flux (kg/m²·s)
- k_l = liquid permeability (m²)
- μ = dynamic viscosity (Pa·s)
- ∇P_cap = capillary pressure gradient (Pa/m)

**Hydraulic Conductivity:**

K = (k_l × ρ × g) / μ

Where:
- K = hydraulic conductivity (m/s)
- Typical values: 10⁻¹² to 10⁻⁶ m/s for building materials

### Capillary Absorption Coefficient

Characterizes the rate of water uptake by a dry material in contact with liquid water.

**Absorption Rate:**

i = A_cap × √t

Where:
- i = cumulative water absorption (kg/m²)
- A_cap = capillary absorption coefficient (kg/m²·s^0.5)
- t = time (s)

**Material-Specific Coefficients:**

| Material | A_cap (kg/m²·s^0.5) | Notes |
|----------|---------------------|-------|
| Dense concrete | 0.001 - 0.01 | Low permeability |
| Normal concrete | 0.01 - 0.10 | Typical construction |
| Porous concrete | 0.10 - 0.50 | High absorption |
| Clay brick | 0.05 - 0.20 | Variable by firing |
| Calcium silicate brick | 0.10 - 0.30 | High capillarity |
| Sandstone | 0.05 - 0.15 | Sedimentary rock |
| Limestone | 0.01 - 0.10 | Varies with porosity |
| Autoclaved aerated concrete | 0.20 - 0.50 | Very porous |
| Wood (tangential) | 0.02 - 0.10 | Anisotropic |
| Mortar (cement) | 0.05 - 0.20 | Joint material |

### Moisture Diffusivity

Relates moisture flux to moisture content gradient under capillary transport.

**Moisture Transport Equation:**

g = -D_w × ∇w

Where:
- g = moisture flux (kg/m²·s)
- D_w = moisture diffusivity (m²/s)
- ∇w = moisture content gradient (kg/m³·m)

**Moisture-Dependent Diffusivity:**

D_w = D_w(w) = f(moisture content)

Moisture diffusivity increases dramatically with moisture content due to:
- Increased liquid phase connectivity
- Reduced vapor path tortuosity
- Enhanced surface diffusion

Typical range: 10⁻¹² to 10⁻⁷ m²/s

## Wicking and Suction Mechanisms

### Capillary Suction

The spontaneous uptake of water by a dry porous material.

**Suction Pressure:**

During absorption, the material develops a suction pressure that draws water into the pore structure:

S = P_atm - P_liquid

Where:
- S = suction pressure (Pa)
- P_atm = atmospheric pressure (Pa)
- P_liquid = pressure in liquid phase (Pa)

**Moisture Retention Curve:**

The relationship between moisture content and capillary suction:

S = f(w) or S = f(RH)

Critical parameters:
- **Capillary saturation moisture content (w_cap)**: Maximum moisture held by capillary forces
- **Hygroscopic moisture content (w_hyg)**: Moisture at 100% RH without capillary contact
- **Residual moisture content**: Minimum drainage level

### Wicking Transport

Horizontal and vertical moisture movement through connected pore networks.

**Vertical Wicking Against Gravity:**

The equilibrium height where capillary pressure balances gravitational force:

h_eq = P_cap / (ρ × g)

**Time to Reach Height h:**

t = (h² × ε × μ) / (2 × k_l × ρ × g)

Where:
- ε = porosity (m³/m³)
- k_l = liquid permeability (m²)

**Horizontal Wicking:**

Without gravity effects, penetration follows:

x = √(2 × D_w × t)

Where:
- x = penetration depth (m)
- D_w = effective moisture diffusivity (m²/s)

### Ground Contact Moisture Rise

A critical design concern for foundation walls and floor slabs.

**Rising Damp Height:**

In masonry walls without damp-proof course:

h_rise = (A_cap² × ρ_w) / (2 × ρ_b × E)

Where:
- h_rise = equilibrium rise height (m)
- ρ_w = water density (kg/m³)
- ρ_b = bulk material density (kg/m³)
- E = evaporation rate from surface (kg/m²·s)

**Typical Rise Heights:**

| Material | Rise Height (m) | Conditions |
|----------|----------------|------------|
| Concrete block | 0.2 - 0.5 | Standard conditions |
| Clay brick | 0.5 - 1.5 | High capillarity |
| Dense concrete | 0.1 - 0.3 | Low permeability |
| Calcium silicate brick | 1.0 - 2.0 | Very high rise |
| Stone (granite) | 0.1 - 0.3 | Low porosity |
| Stone (sandstone) | 0.3 - 0.8 | Higher porosity |

## Material Properties and Behavior

### Porosity and Pore Structure

**Total Porosity:**

ε = V_pores / V_total

Typical values:
- Dense concrete: 0.08 - 0.12
- Normal concrete: 0.12 - 0.18
- Lightweight concrete: 0.25 - 0.50
- Clay brick: 0.20 - 0.35
- Wood: 0.40 - 0.70

**Effective Porosity:**

Only interconnected pores contribute to transport:

ε_eff < ε_total

**Pore Connectivity:**

Characterized by tortuosity factor (τ):

τ = (actual flow path length) / (straight-line distance)

Typical values: 1.5 - 5.0

### Anisotropic Transport

Many building materials exhibit directional dependence.

**Wood Grain Direction:**

| Direction | Relative Permeability | A_cap Ratio |
|-----------|----------------------|-------------|
| Longitudinal (parallel to grain) | 10 - 100 | 3 - 10 |
| Radial (across growth rings) | 1 | 1 |
| Tangential (tangent to rings) | 0.5 - 2 | 0.8 - 1.5 |

**Concrete Casting Direction:**

Water migration channels preferentially along casting direction:
- Perpendicular to casting: k_l × 1.0
- Parallel to casting: k_l × 2.0 - 5.0

### Temperature Dependence

Capillary properties vary with temperature through:

**Viscosity Variation:**

μ(T) = μ₀ × exp(B / (T - C))

Where:
- T = temperature (K)
- B, C = empirical constants

**Surface Tension Variation:**

γ(T) = γ₀ × (1 - α × (T - T₀))

Where:
- α ≈ 1.5 × 10⁻⁴ K⁻¹ for water

**Temperature Effect on Transport:**

At 0°C vs 20°C:
- Viscosity increases by ~75%
- Capillary absorption rate decreases by ~40%
- Surface tension increases by ~5%

## Capillary Breaks and Barriers

### Damp-Proof Course (DPC)

Physical barriers to interrupt capillary pathways.

**Material Requirements:**

| Material | Water Absorption | Thickness (mm) |
|----------|-----------------|----------------|
| Bituminous felt | < 0.01 kg/m² | 3 - 5 |
| Polyethylene sheet | Impermeable | 0.15 - 0.30 |
| Slate | < 0.005 kg/m² | 6 - 10 |
| EPDM membrane | Impermeable | 1.0 - 2.0 |
| Copper sheet | Impermeable | 0.3 - 0.5 |
| Stainless steel | Impermeable | 0.2 - 0.4 |

**Installation Locations:**

1. **Foundation wall base**: 150-200 mm above finished grade
2. **Under slab edge**: Continuous with underslab vapor retarder
3. **Window sills**: Prevent entry at penetrations
4. **Chimney base**: Isolate from ground moisture

### Capillary Break Design

Creating intentional discontinuities in pore structure.

**Gravel Capillary Break:**

Minimum particle size to prevent capillary bridging:

d_min = (4 × γ × cos(θ)) / (ρ × g × h)

For h = 0.1 m rise limitation:
d_min ≈ 6 mm

Recommended practice: 10-20 mm crushed stone, minimum 100 mm thickness

**Air Gap Capillary Break:**

Minimum gap width to prevent droplet bridging:

w_gap > 10 mm (general practice)
w_gap > 15 mm (high exposure)

### Water-Repellent Treatments

Chemical modification of surface properties.

**Silane/Siloxane Treatments:**

- Reduce contact angle to θ > 90°
- Decrease A_cap by 70-95%
- Maintain vapor permeability
- Penetration depth: 3-10 mm
- Service life: 5-15 years

**Effectiveness Criteria:**

Water absorption reduction > 85% per ASTM C67 or EN 13097-2

## Design Considerations

### Moisture Source Control

**Ground Contact:**

1. **Underslab vapor retarder**:
   - Minimum 0.15 mm polyethylene (ASTM E1745 Class A)
   - Permeance < 0.01 perm (0.057 ng/Pa·s·m²)
   - Seal all seams and penetrations

2. **Foundation drainage**:
   - Perimeter drain at footing level
   - Free-draining backfill or drainage board
   - Daylight or sump discharge

3. **Capillary break layer**:
   - 100-150 mm crushed stone, 10-20 mm size
   - Clean, uniform gradation

**Above-Grade Walls:**

1. **Rain penetration prevention**:
   - Cavity wall design with air gap > 25 mm
   - Weep holes at 800 mm spacing maximum
   - Flashing at all horizontal breaks

2. **Material selection**:
   - Low A_cap materials for exterior wythe
   - Water-repellent coatings for porous substrates

### Thermal Performance Impact

**Moisture Content Effect on Thermal Conductivity:**

λ(w) = λ_dry × (1 + b × w)

Where:
- λ = thermal conductivity (W/m·K)
- w = moisture content (kg/m³)
- b = material-specific coefficient (m³/kg)

**Example Impact:**

Concrete at 5% moisture content by volume:
- λ_dry = 1.4 W/m·K
- λ_wet = 1.8 W/m·K
- Increase: ~30%

**Freeze-Thaw Considerations:**

Critical saturation level (S_crit):

S_crit = 0.91 × (1 - ρ_ice / ρ_water)
S_crit ≈ 0.83

Above this threshold, freezing water cannot expand into available pore space, causing damage.

### Evaporation and Drying

**Surface Evaporation Rate:**

E = h_m × (p_v,sat - p_v,air)

Where:
- E = evaporation rate (kg/m²·s)
- h_m = mass transfer coefficient (s/m)
- p_v,sat = saturation vapor pressure at surface (Pa)
- p_v,air = vapor pressure in air (Pa)

**Drying Time Estimation:**

For simple geometry with one-sided drying:

t_dry = (w_initial × L²) / (π² × D_w,avg)

Where:
- t_dry = drying time to equilibrium (s)
- w_initial = initial moisture content (kg/m³)
- L = thickness (m)

**Factors Affecting Drying:**

| Factor | Effect | Magnitude |
|--------|--------|-----------|
| Air velocity increase (0.5 to 2.0 m/s) | Faster drying | 2-3× |
| Temperature increase (20 to 30°C) | Faster drying | 2-3× |
| RH decrease (80 to 40%) | Faster drying | 3-5× |
| Material thickness doubled | Slower drying | 4× |

## ASHRAE and Code Requirements

### ASHRAE References

**ASHRAE Handbook - Fundamentals (Chapter 26):**
- Moisture transport mechanisms and calculations
- Material property data for common building materials
- Capillary transport coefficients

**ASHRAE Standard 160:**
- Design criteria for moisture control
- Condensation analysis requirements
- Material moisture properties

**ASHRAE Standard 55:**
- Acceptable moisture levels for thermal comfort
- Surface condensation prevention

### Building Code Provisions

**International Building Code (IBC):**
- Section 1805.2: Damp-proofing requirements for foundation walls
- Section 1805.3: Waterproofing for walls retaining earth
- Section 1907: Concrete moisture protection

**International Residential Code (IRC):**
- Section R406: Foundation waterproofing and damp-proofing
- R506.2.3: Vapor retarder under slab-on-grade
- Minimum 6 mil polyethylene or equivalent

**ASTM Standards:**

| Standard | Title | Application |
|----------|-------|-------------|
| ASTM C67 | Sampling and Testing Brick | Absorption testing |
| ASTM C140 | Sampling and Testing Concrete Masonry | Absorption and moisture content |
| ASTM C1585 | Water Absorption Rate | Capillary absorption coefficient |
| ASTM E96 | Water Vapor Transmission | Material permeance |
| ASTM E1745 | Plastic Water Vapor Retarders | Underslab barrier performance |
| ASTM D4829 | Qualitative Analysis of Mortar | Moisture damage assessment |

## Testing and Measurement

### Laboratory Testing Methods

**Capillary Absorption Test (ASTM C1585):**

1. Seal all surfaces except test face
2. Expose test face to 1-3 mm water depth
3. Measure mass gain at specified intervals
4. Calculate absorption coefficient from:

i(t) = A_cap × √t

**Initial rate**: 0-360 seconds (early-time behavior)
**Secondary rate**: After 1 day (long-term transport)

**Water Penetration Under Pressure (EN 12390-8):**

- Apply hydrostatic pressure (500 kPa typical)
- Duration: 72 hours
- Measure penetration depth
- Assess concrete quality and waterproofing

### Field Assessment Methods

**Surface Moisture Meter:**

- Capacitance or resistance-based
- Non-destructive measurement
- Depth: 10-40 mm depending on technology
- Calibration required for each material

**Carbide Moisture Test:**

- Destructive sampling
- Chemical reaction: CaC₂ + 2H₂O → Ca(OH)₂ + C₂H₂
- Pressure measurement indicates moisture content
- Accurate for concrete and masonry

**Infrared Thermography:**

- Detects thermal signatures of wet materials
- Non-contact survey method
- Requires temperature differential
- Qualitative unless calibrated

## Mitigation and Remediation

### Retrofitting Existing Structures

**Rising Damp Treatment:**

1. **Physical DPC insertion**:
   - Horizontal slot cutting
   - DPC membrane insertion
   - Mortar/resin injection to seal

2. **Chemical injection DPC**:
   - Silane/siloxane injection at 100-150 mm spacing
   - Pressure or gravity feed
   - Forms hydrophobic barrier in pore structure

3. **Electro-osmotic systems**:
   - Low-voltage electrical field (12-24V)
   - Reverses capillary flow direction
   - Requires continuous power

**Surface Treatments:**

- Water-repellent impregnation
- Render/coating systems with low capillarity
- External drainage improvements

### Preventive Design Strategies

**Material Selection Hierarchy:**

1. **Minimize capillary potential**: Low A_cap materials in critical locations
2. **Provide drainage**: Remove water before absorption
3. **Install barriers**: DPC and capillary breaks
4. **Enable drying**: Ventilation and evaporation surfaces

**Redundant Protection:**

Apply multiple strategies:
- Primary: Keep water away (drainage, flashing)
- Secondary: Block capillary paths (DPC, air gaps)
- Tertiary: Enable drying (ventilation, permeable finishes)

**Detail Design:**

- Avoid thermal bridges that create condensation
- Ensure continuous moisture barriers
- Provide weeps and drainage paths
- Slope horizontal surfaces for drainage

## References

1. ASHRAE Handbook - Fundamentals, Chapter 26: Heat, Air, and Moisture Control in Building Assemblies - Material Properties
2. ASHRAE Standard 160: Criteria for Moisture-Control Design Analysis in Buildings
3. Straube, J. and Burnett, E. (2005). Building Science for Building Enclosures. Building Science Press.
4. Kumaran, M.K. (1996). "IEA ANNEX 24: Heat, Air and Moisture Transfer in Insulated Envelope Parts." Final Report, Volume 3.
5. Hall, C. and Hoff, W.D. (2002). Water Transport in Brick, Stone and Concrete. Taylor & Francis.
6. Krus, M. (1996). "Moisture Transport and Storage Coefficients of Porous Mineral Building Materials." Fraunhofer IRB Verlag.
7. Carmeliet, J. and Roels, S. (2002). "Determination of the Moisture Capacity of Porous Building Materials." Journal of Thermal Envelope and Building Science.

