---
title: "Metals"
description: "Thermal and physical properties of metals used in HVAC systems including thermal conductivity, specific heat, thermal expansion, and design considerations for thermal bridging and condensation control"
weight: 3
---

Metals constitute the primary structural and heat transfer materials in HVAC systems. Their high thermal conductivity, mechanical strength, and durability make them essential for ductwork, piping, heat exchangers, and equipment construction. Understanding the thermal properties of metals is critical for heat transfer calculations, thermal bridging analysis, condensation prevention, and thermal expansion accommodation.

## Thermal Conductivity of Common HVAC Metals

Thermal conductivity (k) quantifies the rate of heat transfer through a material and is the most critical thermal property for HVAC applications. Values are typically reported at 20°C (68°F) unless otherwise specified.

### High Conductivity Metals

**Copper** (pure, annealed)
- Thermal conductivity: 385-401 W/m·K (223-232 Btu·in/hr·ft²·°F)
- Primary applications: refrigerant tubing, hot water piping, heat exchanger tubes, coils
- Temperature dependence: k decreases approximately 0.6% per °C temperature increase
- At 100°C: k ≈ 379 W/m·K
- At 200°C: k ≈ 374 W/m·K

**Copper Alloys**
- Brass (70% Cu, 30% Zn): k = 109-125 W/m·K (63-72 Btu·in/hr·ft²·°F)
- Bronze (90% Cu, 10% Sn): k = 42-50 W/m·K (24-29 Btu·in/hr·ft²·°F)
- Cupronickel (90/10): k = 50 W/m·K (29 Btu·in/hr·ft²·°F)
- Admiralty brass: k = 111 W/m·K (64 Btu·in/hr·ft²·°F)

Applications: valve bodies, fittings, specialized heat exchanger applications

**Aluminum** (commercially pure)
- Thermal conductivity: 205-237 W/m·K (118-137 Btu·in/hr·ft²·°F)
- Primary applications: finned coils, air-side heat exchangers, ducts in specialized applications
- Alloy 1100 (99% Al): k = 222 W/m·K
- Alloy 3003 (Al-Mn): k = 162 W/m·K
- Alloy 6061-T6 (Al-Mg-Si): k = 167 W/m·K
- Alloy 6063-T5 (extrusions): k = 201 W/m·K

### Moderate Conductivity Metals

**Carbon Steel**
- Thermal conductivity: 45-60 W/m·K (26-35 Btu·in/hr·ft²·°F)
- Variation with carbon content and processing
- Low carbon (ASTM A36): k = 51.9 W/m·K at 20°C
- Medium carbon (0.5% C): k = 48.0 W/m·K
- At 100°C: k ≈ 50.2 W/m·K
- At 200°C: k ≈ 48.0 W/m·K
- At 500°C: k ≈ 39.2 W/m·K

Applications: ductwork, piping (steam, chilled water, heating water), boilers, structural supports

**Galvanized Steel**
- Base steel: k = 45-60 W/m·K (conductivity of steel substrate)
- Zinc coating: k = 113 W/m·K (65 Btu·in/hr·ft²·°F)
- Composite conductivity dominated by steel due to thin coating (typically 0.001-0.004 in)
- Effective conductivity: k ≈ 52 W/m·K for calculations

Applications: sheet metal ductwork, galvanized pipe, outdoor enclosures

### Low Conductivity Metals

**Stainless Steel**
- Type 304 (18-8): k = 16.2 W/m·K (9.4 Btu·in/hr·ft²·°F) at 20°C
- Type 316 (with Mo): k = 16.3 W/m·K at 20°C
- Type 409 (ferritic): k = 25.0 W/m·K
- Type 430 (ferritic): k = 26.0 W/m·K
- Austenitic grades have lowest conductivity
- At 100°C (Type 304): k ≈ 17.3 W/m·K
- At 500°C (Type 304): k ≈ 21.4 W/m·K

Applications: corrosion-resistant piping, exhaust systems, coastal/chemical environments, food service

## Thermal Diffusivity and Heat Capacity

Thermal diffusivity (α = k/ρcp) governs the rate of temperature change in transient conditions, critical for startup, shutdown, and cycling operations.

### Specific Heat Capacity (cp)

**At 20°C (68°F):**

| Metal | cp (J/kg·K) | cp (Btu/lbm·°F) | Notes |
|-------|-------------|-----------------|-------|
| Copper | 385 | 0.092 | Relatively constant to 200°C |
| Aluminum | 903 | 0.216 | Increases slightly with temperature |
| Carbon Steel | 434 | 0.104 | Increases to 0.12 at 400°C |
| Stainless 304 | 500 | 0.120 | Increases to 0.13 at 500°C |
| Brass | 380 | 0.091 | Composition dependent |
| Bronze | 377 | 0.090 | Composition dependent |

The low specific heat of copper explains its rapid temperature response in heat exchangers and refrigerant coils. Aluminum's higher specific heat provides greater thermal mass per unit weight.

### Density (ρ)

| Metal | Density (kg/m³) | Density (lbm/ft³) |
|-------|-----------------|-------------------|
| Copper | 8,933 | 557.6 |
| Aluminum | 2,702 | 168.7 |
| Carbon Steel | 7,850 | 490.1 |
| Stainless 304 | 8,000 | 499.4 |
| Galvanized Steel | 7,850 | 490.1 |
| Brass (70/30) | 8,520 | 532.0 |

### Thermal Diffusivity Values

Calculated from α = k/(ρ·cp):

| Metal | α (m²/s × 10⁻⁶) | α (ft²/hr) |
|-------|-----------------|------------|
| Copper | 112 | 4.34 |
| Aluminum | 84.2 | 3.27 |
| Carbon Steel | 13.6 | 0.528 |
| Stainless 304 | 4.05 | 0.157 |
| Aluminum 6061 | 64.0 | 2.48 |

Copper's high diffusivity enables rapid thermal equilibrium in refrigerant circuits. Stainless steel's low diffusivity (1/28 that of copper) causes significant thermal lag in transient operations.

## Thermal Expansion Properties

Linear thermal expansion coefficient (α) governs dimensional changes with temperature. Inadequate expansion accommodation causes pipe stress, joint failure, buckling, and equipment damage.

### Coefficient of Linear Thermal Expansion

**At 20-100°C (68-212°F):**

| Metal | α (μm/m·K or 10⁻⁶/K) | α (in/in·°F × 10⁻⁶) |
|-------|----------------------|---------------------|
| Copper | 16.5 | 9.2 |
| Aluminum | 23.1 | 12.8 |
| Carbon Steel | 11.7 | 6.5 |
| Stainless 304 | 17.3 | 9.6 |
| Stainless 316 | 16.0 | 8.9 |
| Brass | 18.7 | 10.4 |
| Galvanized Steel | 11.7 | 6.5 |

### Expansion Calculation

Linear expansion: ΔL = α · L₀ · ΔT

Where:
- ΔL = change in length
- α = coefficient of linear expansion
- L₀ = original length
- ΔT = temperature change

**Example: 100-ft (30.5 m) copper hot water supply line**

Temperature change: 70°F to 180°F (ΔT = 110°F or 61°C)

ΔL = 16.5 × 10⁻⁶ m/m·K × 30.5 m × 61 K = 0.0307 m = 30.7 mm (1.21 in)

This significant expansion requires expansion loops, expansion joints, or flexible connections.

### Design Implications

**Piping Systems:**
- Expansion loops required for runs exceeding 30-50 ft (9-15 m) depending on ΔT
- Loop size calculation: W = 0.707√(D·L·ΔL) where W = loop width, D = pipe diameter, L = pipe length, ΔL = expansion
- Expansion joints: bellows type for large movements, slip joints for moderate expansion
- Anchor and guide spacing per ASME B31.9 or manufacturer specifications

**Ductwork:**
- Thermal movement typically accommodated by flexible connections at equipment
- Expansion joints required for runs > 100 ft or high-temperature applications (>250°F)
- Sheet metal ductwork naturally accommodates moderate expansion through seams

**Aluminum-to-Steel Connections:**
- Differential expansion: Δα = 23.1 - 11.7 = 11.4 μm/m·K
- Over 50°C temperature change and 1 m length: differential movement = 0.57 mm
- Requires flexible connections or sliding joints to prevent stress concentration

## Temperature Effects on Properties

Thermal properties vary with temperature. For precision calculations, particularly at elevated or cryogenic temperatures, temperature-dependent values are essential.

### Copper Thermal Conductivity vs Temperature

| Temperature (°C) | k (W/m·K) | Temperature (°F) |
|------------------|-----------|------------------|
| -100 | 413 | -148 |
| 0 | 401 | 32 |
| 20 | 398 | 68 |
| 100 | 379 | 212 |
| 200 | 374 | 392 |
| 300 | 369 | 572 |

Correlation: k(T) ≈ 401 - 0.06(T-20) for T in °C, k in W/m·K

### Steel Thermal Conductivity vs Temperature

| Temperature (°C) | k (W/m·K) | Notes |
|------------------|-----------|-------|
| 0 | 54.0 | Low carbon steel |
| 100 | 50.2 | 7% decrease |
| 200 | 48.0 | Continued decline |
| 400 | 42.3 | Significant reduction |
| 500 | 39.2 | High-temp applications |

Phase transformations in steel above 700°C cause dramatic property changes; not relevant for standard HVAC applications.

### Stainless Steel Temperature Dependence

Type 304 exhibits increasing conductivity with temperature (opposite trend from copper/aluminum):

| Temperature (°C) | k (W/m·K) | Temperature (°F) |
|------------------|-----------|------------------|
| 0 | 14.9 | 32 |
| 100 | 17.3 | 212 |
| 300 | 20.0 | 572 |
| 500 | 21.4 | 932 |

This behavior results from the austenitic crystal structure and magnetic properties.

## Thermal Bridging and Heat Loss Analysis

Metals create thermal bridges through insulated assemblies, causing localized heat loss, condensation, and reduced overall R-value.

### Thermal Bridge Impact

Heat flow through a thermal bridge follows parallel path analysis. Total heat transfer:

Q_total = Q_through_insulation + Q_through_bridge

For a steel stud (k = 45 W/m·K) penetrating fiberglass insulation (k = 0.04 W/m·K), the conductivity ratio is 1125:1. Even a small percentage of area occupied by steel dramatically increases heat transfer.

### Effective R-Value Reduction

**Example: Metal stud wall with insulation**

- Wall section: 400 mm (16 in) wide
- Steel studs: 90 mm (3.5 in) deep, 1.5 mm (0.059 in) thick
- Stud spacing: 400 mm (16 in) on center
- Cavity insulation: R-13 (RSI-2.3)

**Parallel path calculation:**

Area fraction:
- Steel: 1.5/400 = 0.00375 (0.375%)
- Insulation: 398.5/400 = 0.99625 (99.625%)

U-value (ignoring air films):
U_eff = (A_steel × U_steel) + (A_insul × U_insul)

U_steel ≈ k/L = 45/0.09 = 500 W/m²·K (extreme simplification; actual path is complex)
U_insul = 1/2.3 = 0.435 W/m²·K

The steel path, despite occupying <0.4% of area, can account for 15-25% of total heat transfer due to 2D/3D conduction effects around the stud.

**Mitigation strategies:**
- Continuous exterior insulation (ci) breaks thermal bridge
- Thermal breaks at metal connections
- Insulated fasteners and clips
- Wood or composite shims at metal connections

### Condensation Risk at Thermal Bridges

Surface temperature at thermal bridge:

T_surface = T_indoor - U × (T_indoor - T_outdoor)

Where U is the local U-factor including bridge effect.

**Example:**
- Indoor: 21°C (70°F), 50% RH, dew point = 10.5°C (51°F)
- Outdoor: -10°C (14°F)
- Wall R-value: RSI-3.5 (R-20)
- Steel bracket thermal bridge: local R-value reduced to RSI-0.9 (R-5)

At bridge: T_surface = 21 - (1/0.9) × (21-(-10)) = 21 - 34.4 = -13.4°C

This calculation shows condensation (and possible ice formation) will occur. In practice, interior surface resistance moderates this, but condensation risk remains high.

**Design solutions:**
- Thermal break materials (polyamide, phenolic) at penetrations
- Interior vapor retarder to limit moisture access
- Increase insulation thickness at bridge locations
- Use low-conductivity fasteners (stainless vs. carbon steel where possible)

## ASHRAE and Code References

### ASHRAE Handbook - Fundamentals (2021)

**Chapter 26: Heat, Air, and Moisture Control in Building Assemblies**
- Table 1: Thermal conductivity of metals and alloys
- Thermal bridging calculation methods
- Surface condensation prediction

**Chapter 33: Physical Properties of Materials**
- Comprehensive property tables for construction metals
- Temperature-dependent properties
- Density, specific heat, thermal conductivity data

**Chapter 4: Heat Transfer**
- Conduction through composite assemblies
- Parallel path method for thermal bridges
- Multi-dimensional heat flow analysis

### Building Codes

**International Energy Conservation Code (IECC)**
- Section C402.1.4: Air barriers (continuity at metal penetrations)
- Section C402.2: Specific insulation requirements (ci for metal buildings)
- Thermal bridging addressed through mandatory continuous insulation provisions

**ASHRAE Standard 90.1-2019: Energy Standard for Buildings**
- Table A3.1: Thermal property data
- Section 5.5.3: Thermal bridges and thermal mass
- Metal building roof and wall assembly requirements

**ASHRAE Standard 62.1: Ventilation for Acceptable Indoor Air Quality**
- Metal ductwork construction standards
- Sealing requirements to prevent condensation in cavities

### SMACNA Standards

**HVAC Duct Construction Standards - Metal and Flexible (2005)**
- Material specifications for galvanized steel, aluminum, stainless
- Thermal expansion joint details and spacing requirements
- Double-wall duct construction for thermal performance

**Architectural Sheet Metal Manual (2012)**
- Expansion joint design and installation
- Thermal movement calculations for long metal runs
- Material compatibility at dissimilar metal joints

## Material Selection Criteria

### Corrosion Resistance vs. Thermal Performance Trade-offs

**Copper:**
- Advantages: excellent thermal conductivity, corrosion resistance, biostatic
- Disadvantages: cost, thermal bridging, potential galvanic corrosion with steel
- Applications: refrigerant lines, hot water, chilled water (treated systems)

**Aluminum:**
- Advantages: lightweight, good conductivity, corrosion resistance
- Disadvantages: galvanic corrosion risk, lower strength, chemical incompatibility
- Applications: finned coils, air handlers, specialty ductwork

**Carbon Steel:**
- Advantages: cost-effective, high strength, weldable, moderate thermal conductivity
- Disadvantages: corrosion susceptibility, thermal bridging
- Applications: ductwork, hydronic piping, structural, boilers
- Requires corrosion protection: galvanizing, painting, or water treatment

**Stainless Steel:**
- Advantages: corrosion resistance, cleanability, durability
- Disadvantages: cost (3-5× carbon steel), low thermal conductivity, difficult fabrication
- Applications: corrosive environments, food service, coastal installations, exhaust systems
- Lower thermal bridging than carbon steel (k = 16 vs. 45 W/m·K) but higher than insulation

**Galvanized Steel:**
- Advantages: corrosion protection, cost-effective, industry standard for ductwork
- Disadvantages: limited temperature range (<392°F), coating damage during fabrication
- Applications: sheet metal ductwork, light-duty piping, outdoor enclosures

### Dissimilar Metal Connections

Galvanic corrosion occurs when dissimilar metals contact in the presence of an electrolyte (water, condensation). The galvanic series in seawater (similar to condensate):

**Anodic (corrodes):**
- Magnesium alloys
- Zinc (galvanizing)
- Aluminum alloys
- Carbon steel
- Stainless steel (active)
- Copper alloys
- Stainless steel (passive)

**Cathodic (protected)**

**Design rules:**
1. Avoid direct contact between metals >0.25V apart in galvanic series
2. Use dielectric unions, gaskets, or isolation fittings
3. Insulate dissimilar metal joints to prevent condensation bridging
4. Apply protective coatings at joints
5. Design for anode (less noble metal) to have larger surface area than cathode

**Common problem connections:**
- Copper to steel: steel corrodes (use dielectric union)
- Aluminum to steel: aluminum corrodes (isolate or use stainless fasteners)
- Stainless to carbon steel: carbon steel corrodes (generally acceptable with isolation)

## Design Considerations Summary

### Heat Transfer Equipment

**Heat Exchangers:**
- Select high-conductivity metals (copper, aluminum) for heat transfer surfaces
- Account for fouling factors reducing effective conductivity
- Finned surfaces: optimize fin efficiency based on material conductivity
- Temperature limits: copper <250°F, aluminum <350°F, stainless >1000°F

**Coils:**
- Copper tubes with aluminum fins: industry standard for air-side heat transfer
- Fin bond quality critical to thermal performance
- Coil face velocity limits prevent fin damage and ensure drainage

### Piping Systems

**Thermal Expansion:**
- Calculate expansion for maximum temperature differential
- Install expansion devices per ASME B31.9
- Anchor at equipment, guides along runs, expansion accommodation between
- Document expansion loop/joint locations on drawings

**Insulation Attachment:**
- Minimize compression of insulation at metal bands
- Use corrosion-resistant fasteners matching pipe material environment
- Vapor retarder continuity at metal penetrations prevents condensation at bridges

### Ductwork

**Low-Pressure Systems (<2 in w.g.):**
- Galvanized steel: 24-16 gauge based on pressure class and dimension
- Thermal expansion rarely governs for indoor applications
- Flexible connections at equipment accommodate movement

**High-Pressure Systems (>2 in w.g.):**
- Heavier gauge or reinforced construction
- Welded vs. slip-and-drive connections
- Thermal considerations for high-velocity systems with significant temperature differences

**Special Applications:**
- Stainless steel: corrosive exhaust, high temperature (>400°F), coastal environments
- Aluminum: low-pressure, corrosive environments incompatible with galvanized
- PVC/FRP: when thermal conductivity must be minimized (double-wall applications)

## Conclusion

Metal thermal properties govern heat transfer, expansion behavior, and condensation control in HVAC systems. Copper and aluminum provide superior heat transfer for coils and heat exchangers. Steel offers structural strength and economy for ductwork and piping despite moderate conductivity. Stainless steel serves corrosive environments while creating minimal thermal bridging compared to carbon steel.

Design requires balancing thermal performance, structural requirements, corrosion resistance, and cost. Thermal bridging analysis prevents condensation and energy loss. Thermal expansion accommodation prevents stress and failure. Material compatibility prevents galvanic corrosion. Proper application of these principles, supported by ASHRAE data and code requirements, ensures reliable and efficient HVAC system performance.
