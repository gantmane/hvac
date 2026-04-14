---
title: "Drying To Interior"
aliases: ["Drying To Interior"]
description: "Design and analysis of building assemblies that allow inward moisture drying in hot-humid climates, including vapor permeance requirements, material selection, and interaction with air conditioning systems"
weight: 2
---

## Overview

Drying-to-interior assemblies represent a fundamental moisture management strategy for hot-humid climates where the predominant vapor drive is from exterior to interior during the cooling season. This approach allows moisture that enters the wall assembly from the exterior (through solar-driven vapor diffusion or bulk water intrusion) to migrate inward and be removed by the air conditioning system, preventing moisture accumulation within the assembly.

The effectiveness of inward drying depends on maintaining adequate vapor permeance on the interior side while controlling outward vapor flow through exterior vapor control layers. This strategy contrasts with cold-climate assemblies that prioritize outward drying and require vapor barriers on the interior.

## Physics of Inward Vapor Drive

### Vapor Pressure Differential

In hot-humid climates during the cooling season, the vapor pressure gradient drives moisture inward. The driving force follows Fick's first law of diffusion:

$$J = -D \frac{dc}{dx}$$

Where:
- J = diffusive flux (kg/m²·s)
- D = diffusion coefficient (m²/s)
- dc/dx = concentration gradient (kg/m⁴)

For building materials, this relationship is more commonly expressed using permeance:

$$g = \frac{M}{A \cdot t \cdot \Delta p}$$

Where:
- g = permeance (ng/Pa·s·m² or perms)
- M = mass of water vapor transmitted (ng or grains)
- A = area (m² or ft²)
- t = time (s or hr)
- Δp = vapor pressure difference (Pa or in. Hg)

### Typical Vapor Pressure Conditions

Hot-humid climate conditions during cooling season:

| Condition | Temperature (°F) | RH (%) | Vapor Pressure (in. Hg) |
|-----------|------------------|--------|-------------------------|
| Exterior (summer) | 95 | 70 | 0.93 |
| Wall cavity | 85 | 75 | 0.78 |
| Interior (conditioned) | 75 | 50 | 0.44 |

Vapor pressure differential (exterior to interior): 0.93 - 0.44 = 0.49 in. Hg

This substantial inward drive necessitates permeable interior finishes to allow moisture removal.

## Material Permeance Requirements

### Vapor Retarder Classifications

Per ASHRAE Standard 160 and IRC Section R702.7, vapor retarders are classified by permeance:

| Class | Permeance Range | Permeance (ng/Pa·s·m²) | Common Materials |
|-------|-----------------|------------------------|------------------|
| Class I (Impermeable) | ≤ 0.1 perm | ≤ 57 | Polyethylene sheet, aluminum foil, rubber membrane |
| Class II (Semi-impermeable) | > 0.1 to ≤ 1.0 perm | 57 to 570 | Kraft-faced insulation, plywood, OSB |
| Class III (Semi-permeable) | > 1.0 to ≤ 10 perms | 570 to 5,700 | Latex paint, unfaced insulation, gypsum board |
| Permeable | > 10 perms | > 5,700 | Unpainted drywall, fiberglass insulation (unfaced) |

### Interior Finish Requirements

For effective inward drying in hot-humid climates, interior finishes must maintain Class III or higher permeance:

**Gypsum Board with Paint:**
- Unpainted gypsum board: 40-50 perms
- One coat latex primer: 15-20 perms
- Two coats latex paint: 8-12 perms
- Oil-based paint: 0.2-0.5 perms (NOT suitable)
- Vinyl wallpaper: 0.05-0.3 perms (NOT suitable)

**Maximum Allowable Interior Permeance:**

For assemblies with exterior insulation permeance < 1 perm, interior surface permeance should be ≥ 5 perms to maintain adequate drying ratio. The drying ratio is calculated as:

$$DR = \frac{P_{interior}}{P_{exterior}}$$

Where:
- DR = drying ratio (dimensionless)
- P_interior = interior surface permeance (perms)
- P_exterior = exterior surface permeance (perms)

Recommended minimum drying ratio: DR ≥ 5:1 for hot-humid climates.

## Assembly Layer Configuration

### Typical Inward-Drying Assembly (Exterior to Interior)

1. **Cladding System**
   - Fiber cement, brick veneer, or vinyl siding
   - Must include drainage plane and ventilation gap
   - Minimum 3/8 inch air space for drying

2. **Weather-Resistive Barrier (WRB)**
   - Permeable WRB: > 10 perms
   - Examples: spunbonded polyolefin, building paper
   - Liquid-applied WRBs: verify permeance > 10 perms

3. **Exterior Sheathing**
   - Options depend on insulation strategy:
     - Plywood/OSB: 0.5-1.5 perms (semi-impermeable)
     - Gypsum sheathing: 15-20 perms (semi-permeable)
     - Structural fiberboard: 20-40 perms (permeable)

4. **Exterior Insulation (if present)**
   - Vapor-permeable rigid insulation
   - Mineral wool board: 25-35 perms (1.5 inch)
   - Unfaced polyisocyanurate: 2-3 perms
   - Avoid foil-faced products (< 0.05 perms)

5. **Structural Framing**
   - Wood or steel studs
   - Provides cavity for cavity insulation

6. **Cavity Insulation**
   - Unfaced fiberglass batts: > 100 perms
   - Unfaced mineral wool: > 100 perms
   - Blown cellulose: 40-60 perms
   - Avoid kraft-faced insulation (0.4-1.0 perms)

7. **Interior Finish**
   - Unpainted gypsum board: 40-50 perms
   - Latex-painted gypsum board: 8-15 perms
   - **Critical: No polyethylene vapor barrier**

### Permeance Calculations Through Assembly

Total assembly vapor resistance in series:

$$R_{total} = R_1 + R_2 + R_3 + ... + R_n$$

Where R = 1/permeance (perm⁻¹)

**Example Calculation:**

Assembly layers (exterior to interior):
- Vinyl siding: negligible resistance
- Permeable WRB: 0.033 perm⁻¹ (30 perms)
- OSB sheathing: 1.0 perm⁻¹ (1.0 perm)
- Unfaced fiberglass cavity insulation: 0.01 perm⁻¹ (100 perms)
- Gypsum board + 2 coats latex: 0.1 perm⁻¹ (10 perms)

Total resistance: R_total = 0.033 + 1.0 + 0.01 + 0.1 = 1.143 perm⁻¹

Assembly effective permeance: P_eff = 1/1.143 = 0.87 perms

The OSB sheathing dominates the vapor resistance in this assembly.

## Interaction with Air Conditioning Systems

### Moisture Removal Mechanisms

Air conditioning systems remove moisture that dries inward through three mechanisms:

1. **Surface Condensation on Cooling Coils**

   Moisture removal rate:

   $$\dot{m}_{condensate} = \rho_{air} \cdot \dot{V} \cdot (W_{in} - W_{out})$$

   Where:
   - ṁ_condensate = condensate production rate (lb/hr)
   - ρ_air = air density (lb/ft³)
   - V̇ = volumetric airflow rate (CFM)
   - W_in = inlet air humidity ratio (lb_w/lb_da)
   - W_out = outlet air humidity ratio (lb_w/lb_da)

2. **Air Movement Across Interior Surfaces**

   Surface mass transfer coefficient:

   $$h_m = \frac{h_c}{c_p \cdot Le^{2/3}}$$

   Where:
   - h_m = mass transfer coefficient (ft/hr)
   - h_c = convective heat transfer coefficient (Btu/hr·ft²·°F)
   - c_p = specific heat of air (Btu/lb·°F)
   - Le = Lewis number ≈ 1.0 for air-water vapor

3. **Dilution Through Ventilation**

   Less significant in hot-humid climates due to high outdoor humidity.

### Interior Surface Temperature Control

To prevent condensation on interior surfaces during inward drying, interior surface temperature must remain above the dew point of interior air.

**Minimum Interior Surface Temperature:**

$$T_{surface,min} = T_{dewpoint} + \Delta T_{safety}$$

Where:
- T_dewpoint = dew point of interior air (°F)
- ΔT_safety = safety margin, typically 3-5°F

For 75°F interior at 50% RH (dew point = 55°F):
T_surface,min = 55 + 5 = 60°F minimum

This requirement influences insulation R-value selection to prevent condensation during peak inward vapor drive conditions.

### Air Conditioning Equipment Considerations

**Sensible Heat Ratio (SHR) Requirements:**

Hot-humid climates require lower SHR to handle latent loads from inward drying:

$$SHR = \frac{Q_{sensible}}{Q_{total}} = \frac{Q_{sensible}}{Q_{sensible} + Q_{latent}}$$

Typical SHR values:
- Dry climates: 0.80-0.95
- Hot-humid climates: 0.65-0.75
- Hot-humid with inward drying assemblies: 0.60-0.70

**Equipment Sizing Implications:**

Total cooling load with inward drying contribution:

$$Q_{total} = Q_{transmission} + Q_{infiltration} + Q_{ventilation} + Q_{internal} + Q_{inward-drying}$$

Where:

$$Q_{inward-drying} = A_{wall} \cdot P_{eff} \cdot \Delta p \cdot h_{fg}$$

Where:
- A_wall = wall area (ft²)
- P_eff = effective assembly permeance (grains/hr·ft²·in.Hg)
- Δp = vapor pressure differential (in. Hg)
- h_fg = latent heat of vaporization = 1,060 Btu/lb at 75°F

**Example Calculation:**

Building with 2,000 ft² wall area, effective permeance = 0.87 perms, vapor pressure differential = 0.49 in. Hg:

Q_inward-drying = 2,000 × 0.87 × 0.49 × 1,060 / 7,000 (conversion)
Q_inward-drying = 130 Btu/hr latent load

While not enormous, this represents additional latent load requiring dehumidification capacity.

## Design Considerations and Best Practices

### Climate Zone Applicability

Inward drying assemblies are appropriate for IECC Climate Zones where inward vapor drive dominates:

| Climate Zone | Applicability | Primary Season | Vapor Drive Direction |
|--------------|---------------|----------------|----------------------|
| 1A (Miami) | Excellent | Year-round cooling | Inward |
| 2A (Houston) | Excellent | Cooling dominant | Inward |
| 3A (Atlanta) | Good | Mixed with cooling emphasis | Primarily inward |
| 4A (Baltimore) | Conditional | Mixed | Seasonal reversal |
| 5A+ (Chicago) | Not recommended | Heating dominant | Outward |

### Prohibited Interior Finishes

The following interior finishes create excessive vapor resistance and prevent inward drying:

**Class I Vapor Barriers (≤ 0.1 perm):**
- Polyethylene sheeting (0.02-0.06 perms)
- Aluminum foil (0.001 perms)
- Rubber-based vapor barrier paints
- Foil-faced insulation on interior

**Class II Materials (0.1-1.0 perm):**
- Oil-based paints (0.3-0.5 perms)
- Vinyl wallcoverings (0.05-0.5 perms)
- Kraft-faced batt insulation (0.4-1.0 perms)
- Certain low-perm primers

### Exterior Cladding Ventilation

Effective inward drying requires that moisture entering through the cladding can migrate through the assembly. Cladding details must include:

**Ventilation Requirements:**
- Minimum 3/8 inch (10 mm) air gap behind cladding
- Minimum 1/16 inch² (64 mm²) net free vent area per ft² (m²) of wall
- Bottom and top venting for continuous airflow path
- Drainage plane with weep provisions

**Drainage Plane Function:**

Bulk water that penetrates cladding must drain by gravity without entering sheathing. The drainage plane prevents capillary suction while allowing vapor transmission.

### Sheathing Selection Strategy

Sheathing selection significantly impacts assembly performance:

**Option 1: Vapor-Open Sheathing**
- Gypsum sheathing: 15-20 perms
- Structural fiberboard: 20-40 perms
- Advantages: Maximum inward drying potential
- Disadvantages: Lower structural capacity, requires alternative bracing

**Option 2: Semi-Permeable Sheathing**
- OSB: 0.5-1.5 perms
- Plywood: 0.5-1.0 perms
- Advantages: Structural rigidity, familiar construction
- Disadvantages: Limits drying rate, creates condensation risk

**Option 3: Hybrid Approach**
- Structural panels at corners/bracing locations
- Non-structural permeable sheathing at field areas
- Balances structural requirements with moisture management

### Condensation Risk Assessment

During periods of inward vapor drive, condensation risk occurs at the first cool surface encountered by moisture moving inward. This is typically:

1. **Air conditioning supply ducts in walls** (if poorly insulated)
2. **Interior surface of exterior sheathing** (during aggressive AC operation)
3. **Interior gypsum board surface** (if interior air dew point too high)

**Temperature Analysis for Condensation Prevention:**

At steady-state, temperature at any point in the assembly:

$$T_x = T_i - \frac{x}{L} (T_i - T_o)$$

For multi-layer assemblies with different R-values:

$$T_{interface} = T_i - \frac{R_{interior}}{R_{total}} (T_i - T_o)$$

Where:
- T_interface = temperature at material interface (°F)
- T_i = interior air temperature (°F)
- T_o = exterior air temperature (°F)
- R_interior = R-value from interior to interface (hr·ft²·°F/Btu)
- R_total = total assembly R-value (hr·ft²·°F/Btu)

**Critical Interface: Interior of OSB Sheathing**

Example conditions:
- Exterior: 95°F, 70% RH (dew point = 84°F)
- Interior: 75°F, 50% RH (dew point = 55°F)
- Wall assembly: R-13 cavity, R-1 sheathing/exterior, R-0.5 interior finish

Temperature at interior of sheathing:
T_sheathing = 75 - [0.5/(0.5+13+1)] × (75-95) = 75.7°F

Since 75.7°F < 84°F (exterior dew point), condensation risk exists if exterior moisture reaches this interface. This underscores the importance of exterior water management.

## ASHRAE and Code References

### ASHRAE Standards

**ASHRAE Standard 160 - Criteria for Moisture-Control Design Analysis in Buildings**
- Section 5.3: Vapor retarder requirements based on climate zone
- Section 6: Moisture analysis procedures
- Appendix C: Climate classification for moisture design

**ASHRAE Standard 62.2 - Ventilation for Acceptable Indoor Air Quality in Residential Buildings**
- Section 4.4: Dehumidification requirements
- Interaction between ventilation and moisture control

**ASHRAE Handbook - Fundamentals (Chapter 26: Heat, Air, and Moisture Control)**
- Section 26.8: Moisture control strategies
- Figure 4: Vapor retarder placement recommendations by climate

### Building Code Requirements

**International Residential Code (IRC)**

Section R702.7: Vapor retarders
- Class I or II vapor retarders required on warm-in-winter side in Climate Zones 5, 6, 7, 8, and Marine 4
- Class III vapor retarders permitted in Climate Zones 1, 2, 3, 4 (except Marine)
- Exception for assemblies with specific exterior insulation ratios

**International Energy Conservation Code (IECC)**

Section C402.5 / R402.5: Air barriers
- While addressing air leakage, affects moisture transport via air movement
- Must coordinate with vapor permeance strategy

### Material Standards

**ASTM E96 - Standard Test Methods for Water Vapor Transmission of Materials**
- Dry cup method (Procedure A): simulates higher humidity on one side
- Wet cup method (Procedure B): simulates lower humidity on one side
- Results reported in perms or metric perms

**ASTM E1677 - Standard Specification for Driven Fasteners Used with Thin-Coat Exterior Insulation and Finish Systems**
- Relevant for continuous insulation applications affecting vapor flow

## Monitoring and Performance Verification

### Installation Quality Control

Critical installation checkpoints for inward-drying assemblies:

1. **Verify absence of interior vapor barriers**
   - Inspect all insulation for facing
   - Check paint specifications (latex only)
   - Confirm no poly sheeting installed

2. **Confirm exterior drainage plane continuity**
   - WRB lapped shingle-fashion
   - Penetrations properly flashed
   - Bottom of wall weep provisions

3. **Check cavity insulation installation**
   - Complete fill without voids
   - No compression reducing effectiveness
   - Proper support without gaps

4. **Validate cladding ventilation**
   - Air gap dimensions maintained
   - Bottom and top vents unobstructed
   - Furring strips properly installed

### Long-Term Performance Monitoring

For critical applications, install moisture monitoring systems:

**Wood Moisture Content Sensors:**
- Embedded at vulnerable locations (exterior sheathing interior surface)
- Alert threshold: 20% moisture content (risk of mold/decay)
- Continuous or periodic monitoring

**Temperature/Humidity Sensors:**
- Within wall cavities at representative locations
- Monitor for condensation conditions
- Data logging for seasonal analysis

**Mold Index Calculations:**

Using monitored temperature and humidity data, calculate mold growth risk per ASHRAE 160:

$$M = \max\left(M_{old} + \frac{\Delta t}{7} \left(\frac{M_{max}}{t_{max}} - M_{old} \cdot k_2\right), 0\right)$$

Where:
- M = mold index (0-6 scale)
- M_max = maximum mold index for conditions
- t_max = time to reach M_max (days)
- k_2 = decay coefficient
- Δt = time step (days)

Mold index > 3 indicates visible mold growth; design target: M < 1.

## Common Design Errors and Solutions

### Error 1: Interior Vapor Barrier Installation

**Problem:** Polyethylene vapor barrier installed on interior despite hot-humid climate location.

**Consequence:** Prevents inward drying, traps moisture in assembly, leads to sheathing decay and mold growth.

**Solution:** Remove interior vapor barrier, repaint with latex paint only (verify Class III permeance).

### Error 2: Vinyl Wallcovering Over Large Areas

**Problem:** Low-permeance vinyl wallcovering installed on interior walls.

**Consequence:** Creates Class I or II vapor barrier preventing moisture removal.

**Solution:** Limit vinyl wallcovering to small areas (< 10% of wall area), use breathable wallcoverings, or apply only to interior partitions.

### Error 3: Insufficient Air Conditioning Dehumidification

**Problem:** Oversized AC equipment with insufficient runtime or high SHR.

**Consequence:** Inadequate moisture removal from interior air, elevated interior humidity, potential condensation on interior surfaces.

**Solution:** Right-size equipment for actual load, select equipment with SHR ≤ 0.75, consider dedicated dehumidification equipment.

### Error 4: Foil-Faced Exterior Insulation

**Problem:** Foil-faced polyisocyanurate used as exterior continuous insulation.

**Consequence:** Creates vapor barrier on exterior preventing inward drying.

**Solution:** Use unfaced or permeable-faced insulation, ensure exterior layer permeance > 1 perm (preferably > 5 perms).

### Error 5: Lack of Cladding Ventilation

**Problem:** Stucco or other mass cladding applied directly to sheathing without drainage plane or air gap.

**Consequence:** Bulk water absorption by cladding drives moisture into assembly with no escape path.

**Solution:** Install drainage plane, provide minimum 3/8 inch air gap using furring or manufactured rainscreen system, detail weeps and vents.

## Advanced Considerations

### Hybrid Climate Conditions

In Climate Zones 4A and portions of 3A, seasonal vapor drive reverses:
- Summer: inward vapor drive (cooling season)
- Winter: outward vapor drive (heating season)

**Bi-directional Drying Strategy:**

Assembly must allow drying in both directions:

$$P_{interior} \approx P_{exterior}$$

Both interior and exterior should maintain Class III permeance (1-10 perms) to accommodate seasonal reversal.

### Embedded Mechanical Systems

HVAC components within exterior walls create condensation risks:

**Supply Ducts:**
- Insulate to minimum R-8 in humid climates
- Use closed-cell insulation (prevents condensation within insulation)
- Vapor barrier on exterior of duct insulation

**Refrigerant Lines:**
- Minimum R-4 insulation on suction lines
- Sealed vapor barrier covering
- Avoid placement in exterior walls when possible

### Future Climate Projections

Climate change projections indicate increasing cooling loads and humidity in many regions:

**Design Implications:**
- Consider inward-drying strategies in transitional climate zones (4A, 4C)
- Increase safety factors for moisture accumulation calculations
- Design for higher peak vapor pressure differentials
- Anticipate longer cooling seasons

## Conclusion

Drying-to-interior assemblies represent a physics-based approach to moisture management in hot-humid climates. Success requires careful material selection to maintain adequate interior permeance (Class III or higher), exterior water management through drainage planes and ventilation, and properly sized air conditioning equipment with sufficient dehumidification capacity.

The fundamental principle remains: moisture driven inward by solar heating and high exterior humidity must find a permeable path to reach the conditioned interior space where mechanical systems can remove it. Any interior vapor barrier—whether poly sheeting, vinyl wallcovering, or oil-based paint—defeats this strategy and creates risk of moisture accumulation and subsequent material degradation.

Design professionals must analyze specific assemblies using permeance calculations, temperature profiles, and condensation risk assessment to verify adequate performance across the range of expected operating conditions. When properly designed and constructed, inward-drying assemblies provide durable, moisture-safe building envelopes for hot-humid climate applications.
