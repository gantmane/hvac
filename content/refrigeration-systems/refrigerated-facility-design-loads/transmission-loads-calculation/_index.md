---
title: "Transmission Loads Calculation"
aliases: ["Transmission Loads Calculation"]
description: "Comprehensive methods for calculating heat transmission loads through refrigerated facility envelopes including wall, ceiling, and floor U-values, insulation R-values, thermal bridging effects, ground contact considerations, and adjacent space temperature differences"
weight: 3
---

Transmission loads represent heat transfer through the building envelope of refrigerated spaces due to temperature differences between inside and outside conditions. These loads constitute a major component of the total refrigeration load and require precise calculation for proper equipment sizing and energy analysis.

## Fundamental Heat Transfer Equation

The basic heat transmission through building envelope components follows Fourier's law adapted for one-dimensional steady-state conduction:

**Q = U × A × ΔT**

Where:
- Q = Heat transfer rate (Btu/h or W)
- U = Overall heat transfer coefficient (Btu/h·ft²·°F or W/m²·K)
- A = Surface area (ft² or m²)
- ΔT = Temperature difference between inside and outside (°F or K)

For refrigerated facilities, this equation must account for multiple envelope components with varying thermal properties and temperature gradients.

## Overall Heat Transfer Coefficient (U-Value)

The U-value represents the rate of heat transfer through a building assembly, including all material layers and surface resistances.

### Calculation Methodology

The overall thermal resistance (R-total) includes:

**R-total = R-inside + R-1 + R-2 + ... + R-n + R-outside**

**U = 1 / R-total**

Where:
- R-inside = Inside surface film resistance (h·ft²·°F/Btu or m²·K/W)
- R-1, R-2, ... R-n = Thermal resistance of each material layer (h·ft²·°F/Btu or m²·K/W)
- R-outside = Outside surface film resistance (h·ft²·°F/Btu or m²·K/W)

### Surface Film Resistances

Surface film coefficients depend on air velocity, surface orientation, and emissivity.

**Standard Surface Film Resistances (IP Units):**

| Surface Position | Air Movement | Resistance (h·ft²·°F/Btu) | Coefficient (Btu/h·ft²·°F) |
|------------------|--------------|---------------------------|---------------------------|
| Inside vertical wall | Still air | 0.68 | 1.47 |
| Inside horizontal ceiling | Heat flow up | 0.61 | 1.63 |
| Inside horizontal floor | Heat flow down | 0.92 | 1.09 |
| Outside vertical wall | 7.5 mph wind | 0.17 | 5.88 |
| Outside vertical wall | 15 mph wind | 0.11 | 9.09 |
| Outside horizontal surface | 7.5 mph wind | 0.17 | 5.88 |

**Standard Surface Film Resistances (SI Units):**

| Surface Position | Air Movement | Resistance (m²·K/W) | Coefficient (W/m²·K) |
|------------------|--------------|---------------------|----------------------|
| Inside vertical wall | Still air | 0.12 | 8.3 |
| Inside horizontal ceiling | Heat flow up | 0.11 | 9.3 |
| Inside horizontal floor | Heat flow down | 0.16 | 6.2 |
| Outside vertical wall | 3.4 m/s wind | 0.030 | 33.3 |
| Outside vertical wall | 6.7 m/s wind | 0.019 | 52.6 |
| Outside horizontal surface | 3.4 m/s wind | 0.030 | 33.3 |

Reference: ASHRAE Fundamentals Handbook, Chapter 27 - Heat, Air, and Moisture Control in Insulated Assemblies

## Insulation R-Values

Thermal resistance of insulation materials is the primary barrier to heat transmission in refrigerated facilities.

### Common Insulation Materials

**Thermal Properties of Insulation Materials at 75°F Mean Temperature:**

| Material | Density (lb/ft³) | k-value (Btu·in/h·ft²·°F) | R-value per inch (h·ft²·°F/Btu·in) |
|----------|------------------|---------------------------|-------------------------------------|
| Polyurethane foam (closed cell) | 2.0-2.5 | 0.14-0.16 | 6.25-7.14 |
| Polyisocyanurate foam | 2.0 | 0.13-0.14 | 7.14-7.69 |
| Extruded polystyrene (XPS) | 1.8-2.5 | 0.18-0.20 | 5.00-5.56 |
| Expanded polystyrene (EPS) | 1.0-1.5 | 0.23-0.26 | 3.85-4.35 |
| Mineral fiber board | 8.0-12.0 | 0.29-0.33 | 3.03-3.45 |
| Fiberglass batt | 0.6-1.0 | 0.25-0.30 | 3.33-4.00 |
| Cellular glass | 8.5 | 0.33-0.38 | 2.63-3.03 |
| Cork board | 7.0-8.5 | 0.30-0.33 | 3.03-3.33 |

**Note:** Thermal conductivity (k-value) increases with increasing temperature and moisture content. For refrigerated applications, use k-values at mean operating temperature.

### Temperature Effect on Insulation Performance

The thermal conductivity of insulation varies with temperature. For accurate calculations:

**k(T) = k₀ + a·T + b·T²**

Where:
- k(T) = Thermal conductivity at temperature T
- k₀ = Reference thermal conductivity
- a, b = Material-specific coefficients
- T = Mean temperature (°F or °C)

For polyurethane foam:
- k increases approximately 0.5-1.0% per 10°F temperature increase above 75°F

### Recommended Insulation Thickness

**Minimum Insulation R-Values for Refrigerated Spaces:**

| Space Temperature Range | Wall R-Value (h·ft²·°F/Btu) | Ceiling R-Value (h·ft²·°F/Btu) | Floor R-Value (h·ft²·°F/Btu) |
|------------------------|------------------------------|----------------------------------|-------------------------------|
| +50°F to +60°F | R-15 to R-19 | R-19 to R-25 | R-10 to R-15 |
| +35°F to +50°F | R-19 to R-25 | R-25 to R-30 | R-15 to R-20 |
| +20°F to +35°F | R-25 to R-30 | R-30 to R-38 | R-20 to R-25 |
| 0°F to +20°F | R-30 to R-38 | R-38 to R-49 | R-25 to R-30 |
| -10°F to 0°F | R-38 to R-49 | R-49 to R-60 | R-30 to R-38 |
| Below -10°F | R-49+ | R-60+ | R-38+ |

Reference: ASHRAE Refrigeration Handbook, Chapter 24 - Refrigerated-Facility Design

## Thermal Bridging

Thermal bridges are localized areas of higher heat transfer that bypass insulation, creating paths of least resistance for heat flow.

### Common Thermal Bridge Locations

1. **Structural Penetrations:**
   - Steel columns through insulated walls
   - Concrete or steel beams
   - Wall ties and fasteners
   - Suspended ceiling hangers

2. **Envelope Discontinuities:**
   - Wall-to-floor junctions
   - Wall-to-ceiling junctions
   - Corner assemblies
   - Door frames and jambs

3. **Service Penetrations:**
   - Electrical conduit
   - Piping penetrations
   - Ductwork penetrations
   - Cable trays

### Thermal Bridge Calculation Methods

**Method 1: Linear Thermal Transmittance**

For edge and junction effects:

**Q = Ψ × L × ΔT**

Where:
- Ψ = Linear thermal transmittance (Btu/h·ft·°F or W/m·K)
- L = Length of thermal bridge (ft or m)
- ΔT = Temperature difference (°F or K)

**Method 2: Point Thermal Transmittance**

For isolated penetrations:

**Q = χ × n × ΔT**

Where:
- χ = Point thermal transmittance (Btu/h·°F or W/K)
- n = Number of identical penetrations
- ΔT = Temperature difference (°F or K)

**Method 3: Effective U-Value Adjustment**

For assemblies with distributed thermal bridges:

**U-effective = U-clear × f-clear + U-bridge × f-bridge**

Where:
- U-clear = U-value of clear wall section
- f-clear = Fraction of area with clear wall
- U-bridge = U-value at thermal bridge
- f-bridge = Fraction of area with thermal bridge

### Thermal Bridge Impact

**Typical Thermal Bridge Heat Gain Increases:**

| Thermal Bridge Type | Heat Gain Increase | U-effective Factor |
|---------------------|-------------------|-------------------|
| Metal stud framing (16" o.c.) | 30-50% | 1.3-1.5 |
| Metal stud framing (24" o.c.) | 20-35% | 1.2-1.35 |
| Steel structural penetrations | 40-100% | 1.4-2.0 |
| Suspended ceiling system | 15-25% | 1.15-1.25 |
| Wall panel joints (poor sealing) | 10-20% | 1.1-1.2 |

### Mitigation Strategies

1. **Thermal Breaks:**
   - Use non-metallic spacers between metal components
   - Install thermal break materials at structural connections
   - Select insulated panel systems with thermal breaks at joints

2. **Structural Design:**
   - Place structural members outside insulated envelope
   - Use insulated concrete forms (ICF)
   - Minimize penetrations through insulation

3. **Installation Details:**
   - Continuous insulation layers
   - Staggered stud walls for deep insulation
   - Proper sealing of all penetrations

## Ground Contact Floors

Heat transfer through ground contact floors requires special consideration due to soil thermal properties and depth effects.

### Heat Transfer Mechanisms

Heat flow from refrigerated spaces to ground occurs through:
1. Conduction through floor slab and underlying soil
2. Heat storage in soil mass (transient effects)
3. Moisture migration and phase change

### Calculation Methods

**Method 1: Simplified Steady-State**

For preliminary calculations:

**Q = A × ΔT / (R-floor + R-soil)**

Where:
- R-floor = Thermal resistance of floor assembly and insulation
- R-soil = Effective soil resistance (typically 2-4 h·ft²·°F/Btu)

**Method 2: ASHRAE Ground Heat Transfer Model**

The ground heat transfer coefficient depends on floor dimensions and perimeter characteristics:

**U-ground = (P/A) × F + k-soil/d**

Where:
- P = Floor perimeter (ft or m)
- A = Floor area (ft² or m²)
- F = Perimeter heat loss factor (Btu/h·ft·°F or W/m·K)
- k-soil = Soil thermal conductivity (Btu/h·ft·°F or W/m·K)
- d = Depth below grade (ft or m)

**Soil Thermal Properties:**

| Soil Type | Conductivity (Btu·in/h·ft²·°F) | Conductivity (W/m·K) | Density (lb/ft³) |
|-----------|--------------------------------|----------------------|------------------|
| Clay or silt (dry) | 8-10 | 1.15-1.44 | 70-100 |
| Clay or silt (moist) | 11-14 | 1.58-2.02 | 100-120 |
| Sand and gravel (dry) | 10-14 | 1.44-2.02 | 90-110 |
| Sand and gravel (moist) | 15-20 | 2.16-2.88 | 110-130 |
| Rock (solid) | 18-28 | 2.59-4.03 | 140-180 |
| Frozen ground | 20-24 | 2.88-3.46 | Variable |

Reference: ASHRAE Fundamentals Handbook, Chapter 18 - Nonresidential Cooling and Heating Load Calculations

### Floor Insulation Configuration

**Recommended Floor Insulation:**

| Space Temperature | Full-Coverage R-Value | Perimeter R-Value | Perimeter Width |
|-------------------|----------------------|-------------------|-----------------|
| +35°F to +50°F | R-10 to R-15 | R-15 to R-20 | 4-6 ft |
| +20°F to +35°F | R-15 to R-20 | R-20 to R-25 | 6-8 ft |
| 0°F to +20°F | R-20 to R-30 | R-25 to R-30 | 8-10 ft |
| Below 0°F | R-30+ | R-30+ | 10-15 ft |

### Under-Floor Heating

For spaces below 35°F, under-floor heating prevents:
- Soil freezing and heaving
- Moisture migration and ice lens formation
- Structural damage to floor slab

**Under-Floor Heating Load:**

**Q-heater = Q-refrigerated + Q-downward-loss + Safety-factor**

Typical under-floor heating density: 1.5-3.0 W/ft² (16-32 W/m²)

Control strategy: Maintain sub-slab temperature between 40-50°F (4-10°C)

## Sun-Exposed Surfaces

Solar radiation significantly increases heat gain through exposed surfaces, particularly roofs.

### Solar Heat Gain Components

Total heat gain through sun-exposed surfaces:

**Q-total = Q-conduction + Q-solar**

**Q-solar = U × A × (TETD) × CLF**

Where:
- TETD = Total equivalent temperature difference (°F or K)
- CLF = Cooling load factor (accounts for thermal mass)

### Sol-Air Temperature

Sol-air temperature combines outdoor air temperature with solar radiation effects:

**T-sol-air = T-outdoor + (α × I-total / h-o) - ε × ΔR / h-o**

Where:
- α = Solar absorptance of surface (0.3-0.9)
- I-total = Total solar radiation intensity (Btu/h·ft² or W/m²)
- h-o = Outside surface heat transfer coefficient (Btu/h·ft²·°F or W/m²·K)
- ε = Surface emissivity (0.8-0.95)
- ΔR = Difference between long-wave radiation from surface and surroundings (typically 20 Btu/h·ft² or 63 W/m²)

**Solar Absorptance by Surface Color:**

| Surface Color/Material | Solar Absorptance (α) |
|------------------------|----------------------|
| White paint or coating | 0.20-0.35 |
| Light cream or ivory | 0.35-0.50 |
| Medium colors (tan, buff) | 0.50-0.70 |
| Dark colors (brown, red) | 0.70-0.85 |
| Black surface | 0.85-0.95 |
| Bright metal (aluminum) | 0.10-0.40 |
| Weathered metal | 0.50-0.70 |

### Peak Sol-Air Temperatures

**Representative Peak Sol-Air Temperatures (95°F Design Day):**

| Surface Orientation | Dark Roof | Light Roof | Dark Wall | Light Wall |
|--------------------|-----------|------------|-----------|------------|
| Horizontal (roof) | 170-180°F | 120-130°F | - | - |
| South facing | - | - | 115-125°F | 105-110°F |
| East/West facing | - | - | 120-130°F | 110-115°F |
| North facing | - | - | 100-105°F | 95-100°F |

### Mitigation Strategies

1. **Cool Roofing:**
   - High solar reflectance (SR > 0.65)
   - High thermal emittance (ε > 0.85)
   - Reduces peak sol-air temperature by 30-50°F

2. **Additional Insulation:**
   - Increase roof insulation to R-40 minimum
   - Use insulation with low thermal diffusivity

3. **Ventilated Roof Systems:**
   - Air gap between roof membrane and insulation
   - Reduces heat gain by 15-25%

## Adjacent Space Temperature Differences

Heat transmission from adjacent unconditioned or conditioned spaces requires separate calculation.

### Temperature Differential Categories

**Typical Adjacent Space Conditions:**

| Adjacent Space Type | Temperature Range | Calculation Factor |
|---------------------|-------------------|-------------------|
| Outdoor ambient | Design outdoor temperature | Use full U-value |
| Conditioned office/break room | 70-75°F | Use full U-value × 0.8-1.0 |
| Mechanical/electrical room | 80-90°F | Use full U-value × 0.7-0.9 |
| Unconditioned warehouse | 80-95°F | Use full U-value × 0.6-0.8 |
| Loading dock (enclosed) | 70-85°F | Use full U-value × 0.6-0.8 |
| Freezer to cooler | Varies | Calculate precise ΔT |
| Below-grade space | Ground temperature | Use ground contact method |

### Multi-Temperature Zone Calculations

For refrigerated facilities with multiple temperature zones:

**Q-1to2 = U × A × (T-2 - T-1)**

Where zones are numbered from coldest (1) to warmest (2).

**Design Considerations:**

1. **Zone Arrangement:**
   - Place coldest zones in building core
   - Minimize surface area between zones with large ΔT
   - Use buffer zones to reduce temperature steps

2. **Insulation Strategy:**
   - Lower R-values acceptable between similar temperature zones
   - Higher R-values required between extreme temperature differences

**Recommended R-Values Between Temperature Zones:**

| Temperature Difference (ΔT) | Minimum Wall R-Value | Minimum Ceiling/Floor R-Value |
|-----------------------------|---------------------|------------------------------|
| 0-10°F | R-7 to R-10 | R-10 to R-13 |
| 10-20°F | R-10 to R-15 | R-13 to R-19 |
| 20-35°F | R-15 to R-19 | R-19 to R-25 |
| 35-50°F | R-19 to R-25 | R-25 to R-30 |
| Above 50°F | R-25+ | R-30+ |

## Transmission Load Calculation Procedures

### Step-by-Step Calculation Process

**Step 1: Define Envelope Components**

Identify and quantify all envelope surfaces:
- Exterior walls (by orientation)
- Roof or ceiling
- Floor (ground contact or elevated)
- Walls adjacent to other spaces
- Doors and openings (calculate separately)

**Step 2: Determine Design Temperatures**

Establish temperature differentials:
- Interior design temperature (refrigerated space)
- Exterior design temperature (ASHRAE design conditions)
- Adjacent space temperatures
- Sol-air temperatures for exposed surfaces

**Step 3: Calculate Component U-Values**

For each envelope component:

a) List all material layers with thickness and k-values
b) Calculate R-value for each layer: R = thickness / k
c) Add surface film resistances
d) Sum total R-value: R-total = R-inside + ΣR-layers + R-outside
e) Calculate U-value: U = 1 / R-total
f) Adjust for thermal bridging if significant

**Step 4: Calculate Surface Areas**

Measure or calculate area for each component:
- Use net areas (subtract openings)
- Account for building geometry
- Verify area calculations

**Step 5: Apply Heat Transfer Equation**

For each component:

**Q = U × A × ΔT**

Sum all components for total transmission load:

**Q-transmission-total = ΣQ-components**

**Step 6: Apply Safety Factors**

Add appropriate safety factors:
- Insulation aging/settling: 5-10%
- Installation imperfections: 5-10%
- Thermal bridging (if not explicitly calculated): 10-20%
- Overall uncertainty: 10-15%

### Example Calculation

**Given:**
- Cooler space: 35°F
- Exterior design temperature: 95°F
- Wall construction: 4" polyurethane insulation between metal skins
- Wall dimensions: 40 ft × 12 ft high

**Calculation:**

1. Temperature difference:
   - ΔT = 95°F - 35°F = 60°F

2. Calculate U-value:
   - Outside film resistance: R = 0.17
   - Outside metal skin (0.05"): R = 0.05 / 300 = 0.0002 (negligible)
   - Polyurethane insulation (4"): R = 4 × 6.7 = 26.8
   - Inside metal skin (0.05"): R = 0.0002 (negligible)
   - Inside film resistance: R = 0.68
   - R-total = 0.17 + 26.8 + 0.68 = 27.65
   - U = 1 / 27.65 = 0.0362 Btu/h·ft²·°F

3. Calculate area:
   - A = 40 ft × 12 ft = 480 ft²

4. Calculate heat gain:
   - Q = 0.0362 × 480 × 60 = 1,043 Btu/h

5. Apply thermal bridging factor (panel joints, 15%):
   - Q-adjusted = 1,043 × 1.15 = 1,199 Btu/h

## Advanced Considerations

### Transient Heat Transfer

For facilities with variable operation or cycling:

**Q(t) = U × A × Σ[ΔT-i × CTF-i]**

Where:
- CTF-i = Conduction transfer function coefficients
- ΔT-i = Temperature difference at previous time intervals

Reference: ASHRAE Fundamentals Handbook, Chapter 18 - Nonresidential Cooling and Heating Load Calculations

### Moisture Effects

Moisture accumulation in insulation degrades thermal performance:

**k-wet = k-dry × (1 + m × MC)**

Where:
- k-wet = Thermal conductivity with moisture
- k-dry = Dry thermal conductivity
- m = Material-specific moisture coefficient
- MC = Moisture content (% by volume)

Typical degradation: 3-5% increase in k-value per 1% moisture content by volume

### Three-Dimensional Heat Transfer

At corners and complex geometries, two-dimensional or three-dimensional finite element analysis provides accurate results where simplified methods underestimate heat transfer by 10-30%.

## Quality Assurance

### Verification Checklist

- [ ] All envelope components identified and measured
- [ ] Thermal properties verified for actual installed materials
- [ ] Temperature differentials confirmed for design conditions
- [ ] Surface film resistances appropriate for orientation and exposure
- [ ] Thermal bridges identified and quantified
- [ ] Ground contact calculations include soil properties
- [ ] Solar effects included for exposed surfaces
- [ ] Adjacent space temperatures verified or estimated conservatively
- [ ] Safety factors applied appropriately
- [ ] Calculations peer-reviewed

### Common Errors

1. **Using nominal vs. actual insulation thickness**
   - Impact: 10-20% underestimation of heat gain

2. **Neglecting thermal bridging**
   - Impact: 15-50% underestimation depending on construction

3. **Incorrect sol-air temperatures**
   - Impact: 20-40% underestimation for roof loads

4. **Assuming uniform ground temperature**
   - Impact: 15-25% error in floor loads

5. **Not accounting for insulation aging**
   - Impact: 5-15% underestimation over equipment life

## Summary

Accurate transmission load calculations require:

1. Detailed envelope component analysis with actual material properties
2. Proper accounting for thermal bridges and envelope discontinuities
3. Recognition of ground contact and solar exposure effects
4. Consideration of adjacent space temperature impacts
5. Application of appropriate safety factors for uncertainty

These calculations form the foundation for refrigeration system sizing and must be performed with rigor to ensure adequate capacity, energy efficiency, and space temperature control.

Reference: ASHRAE Refrigeration Handbook, Chapter 24 - Refrigerated-Facility Design; ASHRAE Fundamentals Handbook, Chapter 27 - Heat, Air, and Moisture Control in Insulated Assemblies
