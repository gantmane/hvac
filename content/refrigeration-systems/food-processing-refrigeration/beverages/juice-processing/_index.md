---
title: "Juice Processing"
aliases: ["Juice Processing"]
weight: 4
---

Juice processing refrigeration systems provide thermal control for extraction, pasteurization, concentration, and storage operations. Temperature management preserves nutritional quality, prevents enzymatic degradation, and controls microbial growth throughout the production chain.

## Processing Temperature Requirements

Different juice types and processing stages demand specific thermal conditions:

| Juice Type | Extraction Temp | Pasteurization | Flash Cooling Target | Cold Storage | Freeze Point |
|------------|----------------|----------------|---------------------|--------------|-------------|
| Orange | 10-15°C | 90-95°C, 15-30s | 1-4°C | 0-2°C | -0.8 to -1.1°C |
| Apple | 5-10°C | 77-88°C, 15s | 1-4°C | 0-2°C | -1.5 to -2.0°C |
| Grape | 15-20°C | 85-90°C, 15s | 2-5°C | 0-3°C | -2.0 to -2.5°C |
| Pineapple | 10-15°C | 90-95°C, 15-30s | 2-5°C | 1-3°C | -1.0 to -1.5°C |
| Cranberry | 5-10°C | 85-90°C, 15s | 1-4°C | 0-2°C | -1.2 to -1.8°C |
| Tomato | 60-70°C | 93-121°C, 15-30s | 4-7°C | 2-4°C | -0.5 to -0.8°C |
| Carrot | 40-50°C | 88-93°C, 15s | 2-5°C | 1-3°C | -0.8 to -1.2°C |

## Flash Cooling Systems

Flash cooling rapidly reduces juice temperature immediately post-pasteurization to prevent thermal degradation while maintaining aseptic conditions.

**Plate Heat Exchanger Design:**
Flash cooling employs multi-stage plate heat exchangers with glycol or ammonia refrigerant circuits. Thermal shock from 90-95°C to 2-4°C occurs within 10-30 seconds, requiring heat removal rates of 300-500 kW per 10,000 L/h production capacity.

Heat removal calculation:
Q = ṁ × cp × ΔT

For orange juice (cp = 3.85 kJ/kg·K, ρ = 1045 kg/m³):
- Production rate: 10,000 L/h = 2.91 kg/s
- Temperature drop: 92°C to 3°C = 89 K
- Heat load: Q = 2.91 × 3.85 × 89 = 997 kW

**Cooling Medium Selection:**

| Refrigerant | Temperature Range | Heat Transfer Coefficient | Application |
|------------|-------------------|--------------------------|-------------|
| Glycol 30% | -10 to 5°C | 2500-3500 W/m²·K | General flash cooling |
| Glycol 40% | -20 to 0°C | 2200-3200 W/m²·K | Sub-zero concentrate cooling |
| Ammonia DX | -25 to -5°C | 3500-5000 W/m²·K | High-capacity systems |
| CO₂ cascade | -35 to -10°C | 4000-6000 W/m²·K | Ultra-low temperature |

Plate spacing of 3-5 mm maintains turbulent flow (Re > 4000) while preventing pressure drops exceeding 70-100 kPa. Stainless steel 316L construction resists organic acid corrosion from citric and malic acids.

## Pasteurization Heat Recovery

Energy recovery from hot pasteurized juice preheats incoming raw juice, reducing heating and cooling loads by 70-85%.

**Regeneration Section Performance:**

Regeneration efficiency (η) relates to the temperature rise of cold juice:
η = (T_cold,out - T_cold,in) / (T_hot,in - T_cold,in)

Typical performance for 10,000 L/h system:
- Raw juice inlet: 15°C
- After regeneration: 75°C
- Pasteurization: 90°C
- Regeneration efficiency: 82%
- Heating reduction: 75 kW vs. 365 kW (without recovery)
- Cooling reduction: 665 kW vs. 997 kW (without recovery)

## Concentrate Production Refrigeration

Evaporative concentration removes water at reduced pressure and temperature, requiring substantial refrigeration for vapor condensation and product cooling.

**Multi-Effect Evaporator Loads:**

| Effect Stage | Operating Pressure | Boiling Point | Concentration | Vapor Rate | Refrigeration Load |
|--------------|-------------------|---------------|---------------|------------|-------------------|
| First Effect | 50 kPa abs | 82°C | 12-15°Brix | 2500 kg/h | Minimal (steam heated) |
| Second Effect | 25 kPa abs | 65°C | 25-35°Brix | 1800 kg/h | 150 kW (vapor recompression) |
| Third Effect | 12 kPa abs | 50°C | 45-55°Brix | 1200 kg/h | 280 kW (condensing) |
| Fourth Effect | 6 kPa abs | 37°C | 60-68°Brix | 600 kg/h | 320 kW (condensing) |
| Final Cooling | Atmospheric | 25°C to 2°C | 65-70°Brix | N/A | 180 kW |

Total refrigeration for 10,000 L/h single-strength to 65°Brix concentrate: 930 kW.

**Vapor Condensing Systems:**
Surface condensers operate at 2-8°C to condense water vapor from final evaporator effects. Ammonia or R-507A refrigeration provides chilled water at 1-3°C, with approach temperatures of 2-4 K.

For fourth effect at 6 kPa absolute:
- Vapor saturation temperature: 37°C
- Condensing temperature required: 33°C
- Chilled water supply: 3°C
- Return temperature: 10°C
- Heat exchanger area: 45-60 m² per 1000 kg/h vapor

## Aseptic Processing Systems

Aseptic juice processing combines ultra-high temperature (UHT) treatment with sterile cooling and filling, extending shelf life to 6-12 months without refrigeration until opened.

**UHT Flash Cooling Requirements:**

UHT processing heats juice to 135-145°C for 2-4 seconds, then flash cools to 20-25°C for ambient filling or to 2-4°C for cold fill operations.

Heat removal rate:
- UHT exit temperature: 138°C
- Flash cooling target: 22°C
- Temperature drop: 116 K
- For 5000 L/h production: Q = 1.45 × 3.85 × 116 = 647 kW

Multi-stage cooling sequence:
1. Regeneration section: 138°C → 50°C (heat recovery)
2. Chilled water stage: 50°C → 30°C (250 kW)
3. Glycol stage: 30°C → 22°C (120 kW)

## Cold Storage Refrigeration

Bulk juice storage maintains quality between processing and packaging or during market distribution delays.

**Storage Tank Cooling Systems:**

| Storage Type | Capacity Range | Temperature | Refrigeration Method | Specific Load |
|-------------|---------------|-------------|---------------------|--------------|
| Fresh Juice | 10,000-50,000 L | 0-2°C | Glycol jacket | 15-25 W/m² |
| Concentrate | 5,000-25,000 L | -8 to -12°C | DX coils | 35-50 W/m² |
| Puree | 20,000-100,000 L | -18 to -23°C | Ammonia jacket | 55-75 W/m² |
| Aseptic Bulk | 50,000-200,000 L | 2-6°C | Glycol coils | 10-18 W/m² |

Tank cooling load components:
1. Product pulldown: ṁ × cp × ΔT
2. Infiltration losses: U × A × ΔT (insulated tanks)
3. Agitation heat: Motor kW × efficiency factor
4. Ambient transmission: Through walls, roof

For 25,000 L fresh orange juice tank:
- Pulldown: 25,000 kg × 3.85 kJ/kg·K × 18 K / 4 h = 481 kW average
- Transmission (R-25 walls): 0.23 W/m²·K × 50 m² × 23 K = 265 W
- Agitation: 5.5 kW motor × 0.15 heat factor = 825 W
- Total refrigeration: 25-30 kW (peak), 5-8 kW (maintenance)

## Enzymatic Activity Control

Refrigeration slows enzymatic degradation that causes cloud loss, color changes, and off-flavor development.

**Critical Enzyme Systems:**

| Enzyme | Substrate | Optimal Temp | Effect on Quality | Inactivation Strategy |
|--------|-----------|--------------|-------------------|----------------------|
| Pectinase | Pectin | 40-50°C | Cloud loss, clarification | <5°C storage, pasteurization |
| Polyphenol Oxidase | Phenolics | 30-40°C | Browning, color loss | <2°C, ascorbic acid, blanching |
| Lipoxygenase | Lipids | 25-35°C | Off-flavors, rancidity | <0°C, rapid processing |
| Peroxidase | Various | 35-45°C | Flavor/color changes | 85-90°C heat treatment |
| Polygalacturonase | Pectin | 30-40°C | Viscosity loss | <4°C, pH control |

Reaction rate temperature dependence follows Arrhenius relationship:
k = A × e^(-Ea/RT)

Q₁₀ values (reaction rate change per 10°C) for juice enzymes range from 1.8 to 3.5. Refrigeration from 20°C to 2°C reduces enzymatic activity by factor of 8-15, extending quality retention from hours to days.

## Microbial Growth Prevention

Temperature control inhibits pathogenic and spoilage microorganisms throughout processing and storage.

**Microbial Control Temperatures:**

| Organism Category | Growth Range | Refrigeration Target | D-Value at 72°C | Z-Value |
|------------------|--------------|---------------------|----------------|---------|
| E. coli O157:H7 | 7-46°C | <4°C storage | 0.1-0.3 min | 5-6°C |
| Salmonella spp. | 5-47°C | <4°C storage | 0.5-1.5 min | 4-5°C |
| Listeria monocytogenes | -0.4-45°C | <2°C storage | 2-5 min | 5-7°C |
| Yeasts | -5-40°C | <0°C storage | 1-3 min | 4-6°C |
| Molds | -5-35°C | <0°C storage | 2-4 min | 4-7°C |
| Alicyclobacillus | 20-65°C | <10°C storage | 2-8 min | 8-10°C |

Combined pasteurization and refrigeration provides multiple hurdles. Flash cooling to <4°C within 30 minutes post-pasteurization prevents spore germination and outgrowth of surviving heat-resistant organisms.

## System Design Considerations

**Refrigeration Capacity Factors:**

Total installed capacity includes safety factors for:
- Product pulldown: 1.2-1.5× calculated load
- Ambient conditions: 1.1-1.3× for summer peaks
- Fouling degradation: 1.15-1.25× over cleaning cycles
- Future expansion: 1.2-1.4× planned capacity

Typical juice plant refrigeration distribution:
- Flash cooling: 35-45% of total capacity
- Concentrate production: 25-35%
- Cold storage: 15-25%
- Process auxiliaries: 5-10%

**Glycol System Design:**
Central glycol systems serve multiple heat exchangers with 30-40% propylene glycol solution at -8 to -2°C supply temperature. Pumping rates of 0.05-0.08 L/s per kW cooling load maintain 4-6 K temperature differentials.

Glycol circulation pump power:
P = (ΔP × V̇) / (η_pump × η_motor)

For 1000 kW cooling load:
- Flow rate: 60 L/s
- Pressure drop: 150 kPa
- Pump power: (150 × 0.06) / (0.75 × 0.92) = 13 kW

**Ammonia Direct Expansion:**
Large capacity installations (>500 kW) employ ammonia DX systems with plate evaporators or shell-and-tube chillers. Evaporator temperatures of -10 to -6°C produce glycol at -5 to -2°C with approach temperatures of 3-5 K.

Ammonia charge minimization strategies:
- Liquid overfeed with gravity return
- Pumped recirculation at 3-4:1 ratio
- Falling film evaporators
- Plate frame heat exchangers (minimal charge)

## Energy Efficiency Measures

**Heat Recovery Integration:**
1. Pasteurization regeneration: 75-85% energy recovery
2. Evaporator vapor recompression: 40-60% steam reduction
3. Condensate heat recovery: 5-10% auxiliary heating
4. Refrigeration heat reclaim: Pasteurization preheating, CIP water heating

**Variable Capacity Control:**
- Variable frequency drives on refrigeration compressors
- Multiple evaporator stages with sequencing
- Floating head pressure control (ambient tracking)
- Demand-based glycol pumping

Annual energy consumption for 10,000 L/h juice plant:
- Refrigeration: 1,200,000 kWh (60% of total)
- Heating: 600,000 kWh (30%)
- Pumping/mixing: 200,000 kWh (10%)

Heat recovery reduces consumption by 450,000-600,000 kWh annually, with payback periods of 1.5-3.5 years for regeneration systems.

