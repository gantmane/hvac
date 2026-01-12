---
title: "Water Treatment"
weight: 5
description: "Comprehensive guide to boiler water treatment including scale prevention, oxygen scavenging, pH control, blowdown calculations, deaeration, and chemical treatment programs."
keywords: ["boiler water treatment", "scale prevention", "oxygen scavenger", "sulfite treatment", "hydrazine", "pH control", "blowdown calculation", "water softening", "deaeration", "condensate treatment"]
---

Proper water treatment prevents scale formation, corrosion, and carryover in boiler systems. Untreated water contains dissolved minerals, gases, and impurities that cause tube failures, efficiency losses, and equipment damage. Treatment programs maintain water chemistry within acceptable limits based on operating pressure and system configuration.

## Scale Prevention

Scale deposits form when dissolved minerals precipitate onto heat transfer surfaces, reducing thermal efficiency and causing localized overheating.

**Primary scale-forming compounds:**
- Calcium carbonate (CaCO₃)
- Calcium sulfate (CaSO₄)
- Magnesium silicate (Mg₂SiO₄)
- Calcium phosphate (Ca₃(PO₄)₂)

**Prevention methods:**

1. **External softening** - Ion exchange removes hardness minerals before feedwater enters the boiler
2. **Internal chemical treatment** - Phosphates, polymers, or chelants prevent precipitation
3. **Blowdown** - Continuous or intermittent removal maintains dissolved solids concentration below saturation limits

ASHRAE Handbook recommends feedwater hardness below 0.3 ppm for pressures above 300 psig. Higher pressure systems require near-zero hardness to prevent scale formation in high heat flux areas.

## Oxygen Scavenging

Dissolved oxygen causes pitting corrosion in feedwater lines, economizers, and boiler tubes. Oxygen solubility decreases with temperature but remains problematic until complete removal.

### Mechanical Deaeration

Deaerators remove oxygen to 0.005-0.04 ppm by heating feedwater to saturation temperature. The deaerator operates at 5-15 psig, releasing non-condensable gases that are vented to atmosphere.

**Deaerator performance factors:**
- Spray valve operation and distribution
- Steam supply pressure and temperature
- Vent rate (typically 2-5 lb steam/1000 lb feedwater)
- Water residence time in storage section

### Chemical Oxygen Scavengers

Chemical treatment removes residual oxygen after mechanical deaeration.

**Sodium Sulfite (Na₂SO₃):**

Reaction: 2Na₂SO₃ + O₂ → 2Na₂SO₄

- Stoichiometric requirement: 7.88 lb sulfite per lb oxygen
- Practical dosage: 10-20 lb per lb oxygen (excess ensures complete reaction)
- Maximum operating pressure: 600 psig
- Temperature limit: 450°F (decomposes to H₂S above this temperature)
- Catalyzed formulations accelerate reaction rates at lower temperatures

**Hydrazine (N₂H₄):**

Reaction: N₂H₄ + O₂ → N₂ + 2H₂O

- Stoichiometric requirement: 1.0 lb hydrazine per lb oxygen
- Practical dosage: 2-3 lb per lb oxygen
- No dissolved solids addition (decomposes to nitrogen and water)
- Required for high-pressure systems (>900 psig)
- Health hazard: carcinogenic, requires careful handling
- Residual maintained at 0.02-0.05 ppm in boiler water

**Organic oxygen scavengers** (carbohydrazide, erythorbate, hydroquinone) provide non-toxic alternatives for specific applications.

## pH Control

Boiler water pH affects corrosion rates, scale formation, and chemical treatment effectiveness.

**Target pH ranges (ASHRAE guidelines):**

| Pressure Range | Boiler Water pH | Condensate pH |
|----------------|-----------------|---------------|
| 0-300 psig | 10.5-12.0 | 7.5-9.0 |
| 301-600 psig | 10.0-11.5 | 8.0-9.0 |
| 601-1000 psig | 9.5-10.5 | 8.5-9.2 |
| >1000 psig | 9.0-9.8 | 8.8-9.2 |

**pH adjustment chemicals:**
- Caustic soda (NaOH) - Raises pH, provides alkalinity reserve
- Sodium carbonate (Na₂CO₃) - Alkalinity control in lower pressure systems
- Filming amines - Condensate pH elevation and corrosion protection
- Neutralizing amines - Volatile alkalinity for steam and condensate systems

Low pH (<7.0) causes acidic corrosion of ferrous metals. High pH (>12.5) promotes caustic corrosion and stress corrosion cracking in certain alloys.

## Blowdown Calculations

Blowdown removes dissolved solids, preventing concentration beyond acceptable limits.

**Blowdown rate calculation:**

BD = (F × S_f) / (S_b - S_f)

Where:
- BD = Blowdown rate (lb/hr or gpm)
- F = Feedwater flow rate
- S_f = Feedwater dissolved solids (ppm)
- S_b = Maximum allowable boiler water dissolved solids (ppm)

**Percent blowdown:**

%BD = (BD / (F + BD)) × 100

**Example calculation:**

Given:
- Feedwater flow: 10,000 lb/hr
- Feedwater TDS: 150 ppm
- Maximum boiler water TDS: 3,000 ppm (300 psig operation)

BD = (10,000 × 150) / (3,000 - 150) = 526 lb/hr

%BD = (526 / 10,526) × 100 = 5.0%

**Cycles of concentration:**

COC = S_b / S_f = 3,000 / 150 = 20 cycles

Higher cycles of concentration reduce blowdown losses but increase risk of scale formation and carryover.

## Water Softening

Ion exchange softening removes calcium and magnesium ions, replacing them with sodium.

**Softener capacity calculation:**

Capacity (grains) = Resin volume (ft³) × Exchange capacity (grains/ft³)

Standard exchange capacity: 20,000-30,000 grains/ft³ depending on regeneration level.

**Regeneration salt requirement:**

Salt (lb) = Resin volume (ft³) × Salt dose (lb/ft³)

Typical salt doses: 6-15 lb NaCl per ft³ resin.

**Hardness leakage:**

Properly operated softeners achieve <1 ppm hardness. End-of-run leakage increases as exchange sites become exhausted.

## Condensate Treatment

Condensate return systems experience corrosion from dissolved CO₂ and low pH.

**Carbonic acid formation:**

CO₂ + H₂O ⇌ H₂CO₃

**Treatment methods:**

1. **Filming amines** - Form protective hydrocarbon film on metal surfaces (18-carbon chain length optimal)
2. **Neutralizing amines** - Volatile alkalinity raises condensate pH
   - Morpholine (boiling point 128°C, distribution ratio 1.5)
   - Cyclohexylamine (boiling point 134°C, distribution ratio 3.0)
   - Methoxypropylamine (boiling point 118°C, distribution ratio 0.5)

Distribution ratio indicates amine partitioning between steam and water phases. Select amines based on system configuration and condensate return temperatures.

## Chemical Treatment Programs

**Phosphate treatment:**
- Precipitates hardness as calcium phosphate sludge
- Trisodium phosphate (Na₃PO₄) provides alkalinity
- Disodium phosphate (Na₂HPO₄) avoids caustic hideout
- Maintains 20-60 ppm PO₄ residual in boiler water

**Chelant treatment:**
- Organic compounds (EDTA, NTA) complex with hardness minerals
- Maintains soluble complexes, preventing precipitation
- Limited to 150 psig maximum pressure
- Strict feedwater quality requirements (<0.01 ppm hardness)

**Polymer treatment:**
- Synthetic dispersants prevent crystal growth and agglomeration
- Compatible with higher pressures than chelants
- Low molecular weight polymers (1,000-5,000 MW) for dispersion
- Typical dosage: 5-20 ppm active polymer

## Monitoring and Control

**Essential water quality tests:**

| Parameter | Frequency | Method |
|-----------|-----------|--------|
| pH | Daily | Electrode |
| Conductivity | Continuous | Inline probe |
| Hardness | Daily | Titration (EDTA) |
| Alkalinity | 2-3 times/week | Titration (H₂SO₄) |
| Chloride | Weekly | Titration (AgNO₃) |
| Silica | Weekly | Colorimetric |
| Phosphate | Daily | Colorimetric |
| Sulfite/hydrazine | Daily | Titration/colorimetric |

Automated blowdown controls maintain conductivity within setpoint limits. Conductivity probes measure total dissolved solids, triggering blowdown valves when concentration exceeds programmed values.

ASHRAE Handbook Chapter 51 (HVAC Applications) provides detailed water quality limits for various operating pressures. Consult manufacturer specifications and ABMA (American Boiler Manufacturers Association) guidelines for specific equipment requirements.
