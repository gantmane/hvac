---
title: "Water Activity"
aliases: ["Water Activity"]
weight: 3
---

Water activity (aw) represents the thermodynamic availability of water in a material for biological and chemical reactions. This parameter directly determines whether mold can grow on building materials.

## Water Activity Definition

Water activity is the ratio of the vapor pressure of water in a material to the vapor pressure of pure water at the same temperature:

$$a_w = \frac{p}{p_0}$$

Where:
- aw = water activity (dimensionless, 0 to 1)
- p = partial vapor pressure of water in the material (Pa)
- p0 = saturation vapor pressure of pure water at the same temperature (Pa)

**Physical Significance:**

- aw = 1.0: Pure water, maximum water availability
- aw = 0.0: Completely dry material, no available water
- aw = 0.85: Threshold where most mold species can initiate growth

Water activity differs from moisture content because it measures the energy state of water rather than total water quantity. Two materials with identical moisture content by mass can have vastly different water activities depending on how strongly the water is bound.

## Equilibrium Relative Humidity Relationship

At equilibrium, water activity equals the relative humidity of the surrounding air divided by 100:

$$a_w = \frac{RH}{100}$$

This relationship means a material exposed to 80% RH will equilibrate to aw = 0.80.

**Equilibrium Conditions:**

| Relative Humidity (%) | Water Activity | Material State |
|-----------------------|----------------|----------------|
| 0-30 | 0.00-0.30 | Extremely dry, hygroscopic materials only |
| 30-60 | 0.30-0.60 | Dry, no mold growth risk |
| 60-80 | 0.60-0.80 | Elevated moisture, xerophilic mold risk |
| 80-95 | 0.80-0.95 | High moisture, most molds can grow |
| 95-100 | 0.95-1.00 | Near saturation, bacterial growth possible |

**Time to Equilibrium:**

The time required for a material to reach equilibrium with ambient RH depends on material thickness, permeability, and diffusivity:

$$t_{eq} \approx \frac{L^2}{4D}$$

Where:
- teq = time to reach 95% of equilibrium (s)
- L = material thickness (m)
- D = moisture diffusivity (m²/s)

Typical equilibration times:
- Thin paper: 1-4 hours
- Gypsum board (12.7 mm): 2-7 days
- Wood framing (38 mm): 2-4 weeks
- Concrete (150 mm): 2-6 months

## Material Sorption Isotherms

Sorption isotherms describe the relationship between water activity and equilibrium moisture content (EMC) at constant temperature.

**General Isotherm Equation (GAB Model):**

$$EMC = \frac{M_m \cdot C \cdot K \cdot a_w}{(1-K \cdot a_w)(1-K \cdot a_w + C \cdot K \cdot a_w)}$$

Where:
- EMC = equilibrium moisture content (kg/kg dry basis)
- Mm = monolayer moisture content (kg/kg)
- C = Guggenheim constant (related to sorption heat)
- K = constant related to multilayer sorption
- aw = water activity

**Typical Building Material Isotherms (20°C):**

| Material | aw = 0.50 | aw = 0.65 | aw = 0.80 | aw = 0.95 |
|----------|-----------|-----------|-----------|-----------|
| Gypsum board | 0.5% | 1.2% | 3.5% | 8.0% |
| Oriented strand board (OSB) | 8% | 11% | 16% | 25% |
| Softwood lumber | 9% | 12% | 16% | 24% |
| Cellulose insulation | 2% | 5% | 12% | 28% |
| Concrete | 3% | 4.5% | 6% | 8.5% |
| Brick (clay) | 0.3% | 0.8% | 2.0% | 5.0% |

Note: Moisture content percentages are on a dry mass basis.

**Hysteresis Effect:**

Materials exhibit different isotherms for adsorption (wetting) versus desorption (drying):

- Desorption EMC typically 10-40% higher than adsorption EMC at same aw
- Hysteresis most pronounced at aw = 0.40-0.80
- Important for materials experiencing cyclic moisture conditions

**Temperature Dependence:**

Water activity at constant moisture content decreases with increasing temperature:

$$\frac{d(a_w)}{dT} \approx -0.002 \text{ to } -0.005 \text{ per °C}$$

Example: Wood at 15% moisture content
- At 10°C: aw ≈ 0.80
- At 25°C: aw ≈ 0.75

## Critical Water Activity for Mold Species

Mold species have minimum water activity requirements for germination and growth. These thresholds represent critical design limits.

**Mold Classification by Water Requirement:**

### Xerophilic Molds (0.60-0.80)

Species capable of growth at relatively low water activities:

| Species | Minimum aw | Optimal aw | Common Substrates |
|---------|-----------|-----------|-------------------|
| *Aspergillus restrictus* | 0.70 | 0.90-0.95 | Dust on surfaces |
| *Aspergillus versicolor* | 0.78 | 0.95-0.98 | Gypsum, wood |
| *Penicillium chrysogenum* | 0.79 | 0.90-0.95 | All porous materials |
| *Eurotium* species | 0.71-0.77 | 0.85-0.90 | Stored materials |
| *Wallemia sebi* | 0.75 | 0.90-0.95 | Wood products |

These species pose the greatest risk in buildings because they can initiate growth at RH levels frequently encountered (75-80%).

### Hydrophilic Molds (Above 0.80)

Species requiring higher water activities:

| Species | Minimum aw | Optimal aw | Common Substrates |
|---------|-----------|-----------|-------------------|
| *Stachybotrys chartarum* | 0.90 | 0.98-1.00 | Cellulose (gypsum paper) |
| *Chaetomium* species | 0.88 | 0.95-1.00 | Wood, paper |
| *Fusarium* species | 0.90 | 0.95-1.00 | Wet building materials |
| *Trichoderma* species | 0.90 | 0.95-1.00 | Wood, wet gypsum |
| *Ulocladium* species | 0.88 | 0.95-1.00 | Wet cellulose |

These species indicate severe moisture problems or water damage events.

**Critical Design Thresholds:**

| Water Activity | Risk Level | Design Implication |
|----------------|------------|-------------------|
| < 0.70 | No risk | Safe operating range |
| 0.70-0.75 | Very low risk | Acceptable for short periods |
| 0.75-0.80 | Moderate risk | Limit exposure to < 3 months |
| 0.80-0.85 | High risk | Limit exposure to < 1 month |
| 0.85-0.90 | Very high risk | Limit exposure to < 1 week |
| > 0.90 | Extreme risk | Immediate intervention required |

**Temperature Interaction:**

Minimum aw for growth decreases with increasing temperature within the viable range:

$$a_{w,min}(T) = a_{w,min}(T_{ref}) - \alpha(T - T_{ref})$$

Where:
- α ≈ 0.001-0.003 per °C for most species
- Tref = reference temperature (typically 20-25°C)

Example for *Aspergillus versicolor*:
- At 15°C: aw,min ≈ 0.80
- At 25°C: aw,min ≈ 0.78
- At 35°C: aw,min ≈ 0.76

**Germination vs. Growth:**

Mold spores require higher water activity for germination than for continued hyphal growth:

- Germination: Typically requires aw 0.02-0.05 higher than minimum growth aw
- Growth: Can continue at lower aw once established
- Sporulation: Often requires aw near optimal range

**Practical Application:**

To prevent mold growth, maintain material surfaces below critical thresholds:

1. **Identify vulnerable materials** using sorption isotherms
2. **Determine critical RH** from species-specific aw requirements
3. **Calculate surface RH** from temperature and dewpoint
4. **Design for safety margin** of at least 5% RH below critical threshold

**Example Calculation:**

Given:
- Gypsum board surface
- Target: Prevent *Aspergillus versicolor* (aw,min = 0.78)
- Safety factor: 5% RH

Maximum allowable surface RH = (0.78 × 100) - 5 = 73% RH

If surface temperature = 15°C (dewpoint control required):
- Maximum dewpoint = 9.4°C (from psychrometric chart at 15°C, 73% RH)
- Indoor air must be maintained below this dewpoint year-round

**Substrate Influence:**

Critical aw varies with nutrient availability in substrate:

- **High nutrients** (wood, gypsum paper): Minimum aw as listed above
- **Low nutrients** (concrete, glass): Minimum aw increases by 0.05-0.10
- **Dust-contaminated surfaces**: Minimum aw may decrease by 0.02-0.05

**Duration Factor:**

The time to visible growth after exceeding critical aw:

| Water Activity | Typical Time to Visible Growth |
|----------------|--------------------------------|
| 0.80-0.85 | 3-6 months |
| 0.85-0.90 | 1-3 months |
| 0.90-0.95 | 2-6 weeks |
| 0.95-1.00 | 1-2 weeks |

These durations assume optimal temperature (20-25°C) and nutrient availability.

## Measurement Techniques

**Direct Methods:**

1. **Chilled-mirror hygrometer**: Measures equilibrium RH in sealed chamber
   - Accuracy: ±0.01 aw
   - Time: 1-4 hours for equilibrium

2. **Capacitive humidity sensor**: Measures equilibrium RH
   - Accuracy: ±0.02 aw
   - Lower cost than chilled-mirror

**Indirect Methods:**

1. **Moisture content + isotherm**: Measure MC, reference isotherm data
   - Accuracy depends on isotherm accuracy

2. **In-situ RH sensors**: Embedded in material during construction
   - Provides continuous monitoring
   - Used in concrete slabs and assemblies

## Design Applications

**Controlling Surface Water Activity:**

1. **Thermal insulation**: Prevents cold surfaces that elevate local aw
2. **Vapor control layers**: Limits moisture accumulation in assemblies
3. **Air sealing**: Prevents condensation from air leakage
4. **Ventilation**: Maintains bulk air RH below critical thresholds
5. **Drainage**: Removes liquid water before materials reach high aw

**Material Selection:**

Choose materials with sorption isotherms that maintain aw < 0.75 under design conditions:

- Prefer inorganic materials in high-humidity zones
- Use treated wood products in vulnerable locations
- Specify mold-resistant gypsum board where appropriate

**Monitoring Protocols:**

For critical applications, establish water activity monitoring:

- Install RH sensors in vulnerable assemblies
- Set alarm thresholds at aw = 0.75 (equivalent to 75% RH)
- Log data continuously to detect transient excursions
- Calibrate sensors annually against reference standards
