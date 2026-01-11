---
title: "Specific Heat Brines"
description: "Specific heat capacity of secondary coolants and brines including temperature and concentration dependence, impact on flow rate calculations, and heat transfer capacity for HVAC system design."
weight: 4
---

Specific heat capacity (cp) determines the sensible heat storage capability of secondary coolants and directly governs flow rate requirements for specified cooling or heating capacities. All secondary coolants exhibit lower specific heat than pure water, necessitating higher flow rates and affecting system sizing, pressure drop, and pumping energy.

## Fundamental Heat Transfer Relationship

The sensible heat transferred by a fluid stream follows the fundamental relationship:

Q = ṁ · cp · ∆T

where:
- Q = heat transfer rate (W or Btu/h)
- ṁ = mass flow rate (kg/s or lb/h)
- cp = specific heat capacity [kJ/(kg·K) or Btu/(lb·°F)]
- ∆T = temperature difference (K or °F)

For specified capacity Q and temperature difference ∆T, the required mass flow rate scales inversely with specific heat:

ṁ = Q / (cp · ∆T)

Reduced specific heat demands proportionally higher flow rates. A fluid with 75% of water's specific heat requires 33% higher flow rate for equivalent capacity.

## Water Baseline Properties

Water exhibits exceptionally high specific heat capacity compared to most liquids, making it an ideal heat transfer medium where freeze protection is unnecessary:

**Water specific heat:** cp = 4.18 kJ/(kg·K) = 1.00 Btu/(lb·°F) at 20°C

This high specific heat results from hydrogen bonding in liquid water. The energy required to break and reform hydrogen bonds during molecular motion contributes to thermal energy absorption without temperature increase.

Water's specific heat varies only slightly with temperature in the liquid range (0-100°C), facilitating simplified calculations. Temperature variation approximately 1% over typical HVAC operating range (0-50°C).

## Specific Heat Temperature Dependence

All secondary coolants exhibit specific heat variation with temperature. The temperature coefficient typically increases specific heat with rising temperature, but the effect remains modest over normal operating ranges.

**Propylene glycol solutions:**
- 30% PG at 0°C: cp ≈ 3.75 kJ/(kg·K)
- 30% PG at 20°C: cp ≈ 3.85 kJ/(kg·K)
- 30% PG at 40°C: cp ≈ 3.95 kJ/(kg·K)

The temperature dependence approximates 0.5% per °C for glycol solutions. Over 40°C operating range, specific heat increases approximately 5%, reducing flow rate requirements slightly at higher temperatures.

For most HVAC design calculations, using specific heat at the average fluid temperature provides adequate accuracy. High-precision applications may employ temperature-dependent property correlations.

## Concentration Effects on Specific Heat

Specific heat decreases approximately linearly with increasing solute concentration as the heat capacity of pure glycol or salt is lower than water:

**Propylene glycol specific heat at 20°C:**

| Concentration | cp [kJ/(kg·K)] | cp [Btu/(lb·°F)] | Required Flow Rate Multiplier |
|--------------|----------------|------------------|-------------------------------|
| 0% (water) | 4.18 | 1.00 | 1.00 |
| 10% | 4.06 | 0.97 | 1.03 |
| 20% | 3.98 | 0.95 | 1.05 |
| 30% | 3.85 | 0.92 | 1.09 |
| 40% | 3.72 | 0.89 | 1.12 |
| 50% | 3.52 | 0.84 | 1.19 |

Each 10% increase in glycol concentration reduces specific heat by approximately 3-4%, requiring corresponding flow rate increase.

**Ethylene glycol:** Exhibits similar concentration dependence with slightly higher specific heat than propylene glycol at equivalent concentrations (approximately 2% higher).

**Sodium chloride brines:**

| NaCl Concentration | cp [kJ/(kg·K)] | cp [Btu/(lb·°F)] | Flow Rate Multiplier |
|-------------------|----------------|------------------|----------------------|
| 0% (water) | 4.18 | 1.00 | 1.00 |
| 10% | 3.81 | 0.91 | 1.10 |
| 20% | 3.44 | 0.82 | 1.21 |
| 23% (eutectic) | 3.25 | 0.78 | 1.29 |

Salt brines exhibit more pronounced specific heat reduction than glycol solutions at equivalent freeze protection temperatures. NaCl eutectic brine requires 29% higher flow rate than water.

**Calcium chloride brines:** Show similar patterns with cp ≈ 2.7 kJ/(kg·K) at 30% concentration, requiring 55% higher flow rate than water.

## Impact on System Flow Rates

Reduced specific heat propagates through all system flow rate calculations:

**Temperature change vs flow rate relationship:** For fixed capacity Q:
- ∆T = Q / (ṁ · cp)

Lower specific heat reduces temperature rise/drop for given flow rate, or equivalently, requires higher flow rate for specified temperature difference.

**Design temperature differences:** Water systems typically design for 10-20°F (5-11°C) ∆T across loads. Glycol systems may use 8-15°F (4-8°C) ∆T to maintain reasonable flow rates despite lower specific heat.

**Pipe sizing implications:** Higher volumetric flow rates require larger pipe diameters to maintain equivalent velocities (typically 4-8 ft/s in piping). Alternatively, smaller pipes accept higher velocities with increased pressure drop penalty.

## Gallons per Minute per Ton Calculations

The common HVAC rule of thumb "2.4 gpm/ton for 10°F ∆T" applies specifically to water. Secondary coolants require adjustment:

**Water baseline:**
- gpm/ton = 24 / ∆T(°F)
- For 10°F ∆T: 2.4 gpm/ton
- For 15°F ∆T: 1.6 gpm/ton

**Glycol solution correction:**
- gpm/ton = 24 / [∆T(°F) · SG · (cp/cp_water)]

where SG = specific gravity of glycol solution (1.02-1.05).

**Example: 30% propylene glycol, 10°F ∆T:**
- cp/cp_water = 0.92
- SG = 1.024
- gpm/ton = 24 / (10 · 1.024 · 0.92) = 2.55 gpm/ton

The glycol system requires 6% higher flow rate than water for equivalent capacity and ∆T.

## Heat Capacity and Thermal Storage

Specific heat determines sensible thermal storage capacity in buffer tanks and thermal mass:

**Volumetric heat capacity:** ρ · cp determines energy storage per unit volume:

| Fluid | ρ (kg/m³) | cp [kJ/(kg·K)] | ρcp [kJ/(m³·K)] | Relative Storage |
|-------|-----------|----------------|-----------------|------------------|
| Water (20°C) | 998 | 4.18 | 4172 | 1.00 |
| 30% propylene glycol | 1023 | 3.85 | 3939 | 0.94 |
| 40% propylene glycol | 1032 | 3.72 | 3839 | 0.92 |
| 23% NaCl brine | 1178 | 3.25 | 3829 | 0.92 |

Glycol solutions retain 92-94% of water's volumetric thermal storage capacity. Buffer tank sizing must account for this reduction when substituting glycol for water in existing designs.

## Pumping Power Implications

The combined effect of lower specific heat (requiring higher flow rates) and higher viscosity (increasing pressure drop) significantly increases pumping power:

**Flow rate penalty:** cpwater / cpcoolant factor increases mass and volumetric flow rates.

**Pressure drop penalty:** Higher flow rates increase velocity and pressure drop per ∆P ∝ V². Additionally, higher viscosity further increases pressure drop.

**Combined pumping power effect:**

P_pump ∝ ṁ · ∆P ∝ (1/cp) · (μ · V²) ∝ (1/cp) · (μ/cp²)

For 30% propylene glycol versus water:
- Specific heat factor: 1.09× higher flow rate
- Viscosity factor: 2.8× at 20°C
- Combined effect: 2-3× higher pumping power

This pumping power penalty persists throughout system operation, favoring minimum adequate glycol concentration.

## Design Optimization Strategies

Engineers minimize specific heat penalties through several approaches:

**Concentration optimization:** Use minimum concentration satisfying freeze protection requirements plus safety margin. Each unnecessary 5% concentration costs 1-2% in flow rate and 5-10% in pumping power.

**Temperature difference selection:** Accept larger ∆T (12-15°F instead of 8-10°F) to reduce flow rates. Verify heat exchanger approach temperatures accommodate larger system ∆T.

**Separate systems:** Consider separate water and glycol-protected systems. Use water for primary circulation with glycol only in freeze-exposed coils or loops.

**Variable flow operation:** Implement variable speed pumping. Reduced specific heat affects all load conditions, but variable flow optimization still achieves 30-50% pumping energy savings versus constant volume.

## Measurement and Verification

Field verification of specific heat rarely occurs, but related parameters confirm proper concentration:

**Refractometer:** Measures refractive index to determine glycol concentration. Specific heat correlates directly with concentration per published data.

**Hydrometer:** Measures specific gravity. Combined with temperature measurement, determines concentration and corresponding specific heat.

**Temperature rise measurement:** For known heat input Q and measured flow rate ṁ, temperature rise verifies cp:

cp = Q / (ṁ · ∆T)

Measured specific heat significantly different from expected values indicates concentration error, contamination, or flow measurement problems.

## Application-Specific Considerations

Different HVAC applications emphasize different aspects of specific heat performance:

**Ice storage systems:** Lower specific heat reduces thermal storage capacity per gallon of brine. Storage tank sizing must account for 20-30% capacity reduction versus water-based ice storage.

**Process cooling:** Fixed temperature requirements dictate flow rates. Lower specific heat directly increases required pump size, pipe sizes, and heat exchanger dimensions.

**Snow melting:** Intermittent operation makes pumping energy less critical. Specific heat primarily affects pipe sizing for specified heat output per linear foot.

**District cooling:** Long piping runs magnify pressure drop penalties. Specific heat reduction compounds with viscosity effects, potentially favoring water with local freeze protection over system-wide glycol.
