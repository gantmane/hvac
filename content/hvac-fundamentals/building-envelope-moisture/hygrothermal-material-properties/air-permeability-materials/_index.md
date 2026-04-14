---
title: "Air Permeability of Materials"
aliases: ["Air Permeability of Materials"]
description: "Air permeability coefficients, testing standards, and air barrier material requirements for HVAC building envelope moisture control and infiltration prevention."
weight: 2
---

Air permeability quantifies the rate at which air flows through porous building materials under pressure differential. This property directly affects convective moisture transport, energy losses, and the effectiveness of air barrier systems in the building envelope.

## Air Permeability Fundamentals

Air permeability (ka) represents the volumetric airflow rate through a unit area of material under a unit pressure gradient:

**ka = (Q × L) / (A × ΔP)**

Where:
- ka = air permeability coefficient (m³·m/m²·s·Pa or m²/(Pa·s))
- Q = volumetric airflow rate (m³/s)
- L = material thickness (m)
- A = cross-sectional area (m²)
- ΔP = pressure differential across material (Pa)

Air permeability differs fundamentally from air permeance. Permeability is a material property independent of thickness, while permeance accounts for specific thickness and expresses airflow resistance of a particular assembly.

## Air Permeance vs. Air Permeability

Air permeance (La) relates to permeability through material thickness:

**La = ka / L**

Where:
- La = air permeance (m³/m²·s·Pa)
- ka = air permeability (m²/(Pa·s))
- L = thickness (m)

Air barrier materials are typically specified by maximum allowable air permeance rather than permeability, as the installed thickness determines actual performance.

## Air Barrier Material Requirements

ASHRAE 90.1 defines air barrier assemblies with maximum air leakage rates:

| Component | Maximum Air Leakage | Test Standard |
|-----------|---------------------|---------------|
| Air barrier material | 0.004 cfm/ft² @ 75 Pa (0.02 L/s·m²) | ASTM E2178 |
| Air barrier assembly | 0.04 cfm/ft² @ 75 Pa (0.2 L/s·m²) | ASTM E2357 |
| Building envelope | 0.40 cfm/ft² @ 75 Pa (2.0 L/s·m²) | ASTM E779 |

The three-tier specification approach ensures that individual materials, assembled systems, and completed buildings all meet progressively realistic performance thresholds.

## Material Air Permeability Values

Typical air permeability coefficients for common building materials:

| Material | Air Permeability (m²/(Pa·s)) | Classification |
|----------|------------------------------|----------------|
| Polyethylene sheet (6 mil) | < 1 × 10⁻¹⁵ | Air barrier |
| Fluid-applied membrane | < 1 × 10⁻¹⁵ | Air barrier |
| Self-adhered membrane | < 1 × 10⁻¹⁵ | Air barrier |
| Gypsum board (painted) | 1 × 10⁻¹² to 1 × 10⁻¹¹ | Air retarder |
| Concrete (cast-in-place) | 1 × 10⁻¹³ to 1 × 10⁻¹² | Air barrier |
| CMU (unpainted) | 1 × 10⁻⁹ to 1 × 10⁻⁸ | Air permeable |
| Plywood (unsealed) | 1 × 10⁻¹¹ to 1 × 10⁻¹⁰ | Air retarder |
| OSB (unsealed) | 1 × 10⁻¹¹ to 1 × 10⁻¹⁰ | Air retarder |
| Fiberglass insulation | 1 × 10⁻⁷ to 1 × 10⁻⁶ | Air permeable |
| Cellulose insulation | 1 × 10⁻⁸ to 1 × 10⁻⁷ | Air permeable |

Materials with air permeability below 1 × 10⁻¹² m²/(Pa·s) generally qualify as air barriers when properly installed with sealed joints and penetrations.

## ASTM Testing Standards

### ASTM E2178: Air Permeance of Building Materials

Standard test method measuring air permeance of sheet materials at 75 Pa pressure differential. Specimens are mounted in a test chamber, and airflow is measured across the pressure drop.

Test conditions:
- Pressure differential: 75 Pa (0.3 in. w.c.)
- Temperature: 21°C ± 3°C (70°F ± 5°F)
- Relative humidity: 50% ± 10%
- Specimen size: minimum 305 mm × 305 mm (12 in. × 12 in.)

Materials meeting the 0.004 cfm/ft² threshold qualify as air barrier materials.

### ASTM E283: Air Leakage Through Exterior Windows, Doors, and Curtain Walls

Measures air leakage rate of fenestration assemblies under specified pressure differentials. Critical for determining whole-assembly performance including frame interfaces and operating hardware.

### ASTM E779: Whole Building Air Leakage (Blower Door Test)

Pressurizes or depressurizes entire building envelope to quantify total air leakage. Results expressed as air changes per hour at 50 Pa (ACH50) or airflow at specific pressures.

### ASTM E1677: Air Leakage of Exterior Metal Roof Panel Systems

Specific protocol for metal roofing assemblies, addressing panel joints, fastener penetrations, and laps.

## Convective Moisture Transport

Air permeability enables convective moisture transport, which typically exceeds diffusive vapor transport by orders of magnitude. Air leakage at 1 cfm carries approximately:

**Moisture transport = 0.68 × Q × Δω × ρₐᵢᵣ**

Where:
- Q = airflow rate (cfm)
- Δω = humidity ratio difference (lb water/lb dry air)
- ρₐᵢᵣ = air density (approximately 0.075 lb/ft³)

For example, 1 cfm of air leakage with a 0.005 humidity ratio difference transports:

**Moisture = 0.68 × 1 × 0.005 × 0.075 = 0.000255 lb/min = 0.37 lb/day**

This convective moisture transport far exceeds typical diffusion rates through vapor-permeable materials, making air barrier continuity critical for moisture control.

## Effect of Pressure Differential

Airflow through porous materials follows power-law relationships:

**Q = C × ΔPⁿ**

Where:
- Q = airflow rate
- C = flow coefficient (related to permeability)
- ΔP = pressure differential
- n = flow exponent (0.5 for laminar flow, 1.0 for turbulent flow)

Most building materials exhibit flow exponents between 0.5 and 0.75, indicating transitional flow regimes. Air barrier testing at 75 Pa provides standardized comparison, though actual pressure differentials vary widely:

| Condition | Typical Pressure (Pa) |
|-----------|----------------------|
| Stack effect (10-story building, winter) | 20-50 |
| Wind pressure (20 mph) | 25-75 |
| HVAC system pressurization | 5-25 |
| Test condition (ASTM E2178) | 75 |

Higher test pressures (75 Pa) ensure conservative performance estimates for actual operating conditions.

## Temperature Effects on Air Permeability

Air permeability of most building materials exhibits minimal temperature dependence, as the material structure remains unchanged. However, air viscosity varies with temperature, affecting flow rates:

**μ(T) = μ₀ × (T/T₀)^0.7**

Where:
- μ(T) = dynamic viscosity at temperature T
- μ₀ = reference viscosity at T₀
- T = absolute temperature (K)

This relationship causes approximately 10% variation in measured air permeability across typical temperature ranges (0°C to 40°C), generally within measurement uncertainty.

## Air Barrier System Design

Effective air barrier systems require:

1. **Material selection**: Materials meeting ASTM E2178 criteria (< 0.004 cfm/ft² @ 75 Pa)
2. **Continuity**: Unbroken air barrier plane across all envelope transitions
3. **Sealed penetrations**: All electrical, mechanical, and structural penetrations sealed
4. **Structural support**: Air barrier materials supported to resist design pressures without tearing or displacement
5. **Durability**: Materials maintaining performance throughout building service life

The air barrier location within the wall assembly affects hygrothermal performance but not its fundamental requirement for continuity and low permeability.

## Joints and Penetrations

Air leakage concentrates at joints, seams, and penetrations rather than through material bodies. Typical air leakage paths:

- Window and door perimeters
- Foundation-to-wall transitions
- Wall-to-roof junctions
- Electrical and plumbing penetrations
- HVAC duct penetrations
- Control joint and expansion joint interfaces

Sealant materials and transition membranes at these locations must maintain airtightness while accommodating differential movement. ASTM C920 classifies sealants by movement capability (±12.5%, ±25%, ±50%), critical for maintaining air barrier integrity through thermal expansion and structural deflection.

## Relationship to Vapor Permeability

Air permeability and vapor permeability represent independent material properties. Materials may be:

- **Air impermeable, vapor impermeable**: Polyethylene sheet, aluminum foil
- **Air impermeable, vapor permeable**: Spun-bonded polyolefin membranes, fluid-applied vapor-permeable barriers
- **Air permeable, vapor impermeable**: Perforated vapor barriers (not recommended)
- **Air permeable, vapor permeable**: Fiberglass insulation, mineral wool

Optimal hygrothermal design often requires air-impermeable, vapor-permeable materials, allowing moisture diffusion drying while preventing convective moisture accumulation.

## Quality Assurance Testing

Field verification of air barrier performance:

1. **Visual inspection**: Verify continuity and sealed transitions before concealment
2. **Chamber testing**: ASTM E1186 or E2357 for representative wall sections
3. **Whole-building testing**: ASTM E779 blower door test after substantial completion
4. **Infrared thermography**: Identifies air leakage paths during pressurization testing

USACE and NIBS guidelines recommend testing at least two representative wall sections plus whole-building testing for projects exceeding 50,000 ft² conditioned area.

