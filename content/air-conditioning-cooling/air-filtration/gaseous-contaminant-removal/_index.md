---
title: "Gaseous Contaminant Removal"
aliases: ["Gaseous Contaminant Removal"]
description: "Technologies and methods for removing gaseous pollutants including VOCs, odors, and harmful gases from HVAC airstreams."
keywords: ["gaseous contaminant removal", "VOC removal", "activated carbon", "air cleaning", "gas-phase filtration", "adsorption"]
tags: ["gaseous contaminant removal", "VOC removal", "activated carbon", "air cleaning", "gas-phase filtration", "adsorption"]
weight: 5
---

Gaseous contaminant removal addresses air pollutants that pass through particulate filters, including volatile organic compounds (VOCs), odors, and harmful gases. These technologies are essential for indoor air quality in applications ranging from commercial buildings to specialized industrial environments.

## Gaseous Contaminant Categories

### Volatile Organic Compounds (VOCs)

VOCs originate from numerous indoor and outdoor sources:

**Indoor Sources**:
- Building materials (formaldehyde, solvents)
- Furnishings (off-gassing from adhesives)
- Cleaning products (terpenes, alcohols)
- Office equipment (ozone, VOCs from toners)
- Occupant activities (perfumes, personal care)

**Outdoor Sources**:
- Vehicle exhaust (benzene, toluene)
- Industrial emissions
- Photochemical smog

**Health Concerns**:
VOC exposure effects range from sensory irritation to chronic health impacts:
- Irritation of eyes, nose, throat
- Headaches, fatigue, difficulty concentrating
- Long-term: liver, kidney, CNS damage
- Some VOCs classified as carcinogens

### Inorganic Gases

| Gas | Sources | Health Effects | Typical Concentrations |
|-----|---------|----------------|----------------------|
| Ozone (O₃) | Outdoor air, copiers, ESPs | Respiratory irritation | 20-100 ppb outdoor |
| Nitrogen dioxide (NO₂) | Combustion, traffic | Respiratory inflammation | 10-50 ppb indoor |
| Carbon monoxide (CO) | Combustion appliances | Oxygen displacement | <9 ppm (standard) |
| Sulfur dioxide (SO₂) | Industrial, combustion | Respiratory irritation | <75 ppb (standard) |
| Hydrogen sulfide (H₂S) | Sewage, industrial | Toxic, odor | <10 ppb (odor threshold) |

### Odorous Compounds

Odors may or may not indicate health hazards but significantly impact occupant satisfaction:

- Detection thresholds often in ppb range
- Individual sensitivity varies widely
- Adaptation effects reduce perception over time
- Mixtures may produce synergistic effects

## Adsorption Technologies

### Activated Carbon

Activated carbon remains the dominant gas-phase filtration media due to versatility and effectiveness.

**Production and Structure**:
- Source materials: coconut shell, coal, wood
- Activation: thermal or chemical treatment
- Surface area: 800-1500 m²/g
- Pore structure: micropores (<2 nm), mesopores (2-50 nm)

**Adsorption Mechanism**:
Physical adsorption (physisorption) through van der Waals forces:

$$q_e = K_F C_e^{1/n}$$ (Freundlich isotherm)

$$q_e = \frac{q_m K_L C_e}{1 + K_L C_e}$$ (Langmuir isotherm)

Where:
- $q_e$ = equilibrium adsorption capacity
- $C_e$ = equilibrium concentration
- $K_F$, $K_L$ = isotherm constants

**Removal Capabilities**:

| Compound Class | Removal Efficiency | Carbon Type |
|---------------|-------------------|-------------|
| Aromatics (benzene, toluene) | 85-99% | Virgin carbon |
| Aldehydes (formaldehyde) | 40-60% | Impregnated |
| Chlorinated compounds | 90-99% | Virgin carbon |
| Ammonia | 60-90% | Impregnated |
| Ozone | 95-99% | Virgin carbon |

### Impregnated Carbons

Chemical impregnation enhances removal of specific compounds through chemisorption:

| Impregnant | Target Compounds |
|------------|-----------------|
| Potassium hydroxide (KOH) | Acid gases (H₂S, SO₂) |
| Phosphoric acid | Ammonia, amines |
| Potassium permanganate | Aldehydes, H₂S |
| Metal oxides | Mercury vapor |
| Iodine | Radioactive iodine |

### Activated Alumina

Porous aluminum oxide for specific applications:

- High affinity for polar compounds
- Fluoride removal
- Regenerable at 200-400°C
- Lower capacity than carbon for most VOCs

### Zeolites and Molecular Sieves

Crystalline aluminosilicates with defined pore structures:

**Advantages**:
- Selective adsorption by molecular size
- Hydrophobic varieties resist moisture
- Regenerable
- Thermally stable

**Applications**:
- Polar compound removal
- Moisture control
- Selective VOC capture

## Oxidation Technologies

### Photocatalytic Oxidation (PCO)

UV light activates semiconductor catalyst (typically TiO₂) to oxidize organic compounds.

**Reaction Mechanism**:
1. UV photons excite electrons in TiO₂
2. Electron-hole pairs generate hydroxyl radicals (•OH)
3. Radicals oxidize organic compounds
4. Ideally: VOC → CO₂ + H₂O

**Design Parameters**:
- UV wavelength: 254 nm or 365 nm
- Catalyst surface area and contact time
- Humidity effects on radical generation
- Temperature influence on reaction rates

**Limitations**:
- Incomplete oxidation may produce harmful byproducts (formaldehyde, acetaldehyde)
- Catalyst deactivation from contamination
- Energy consumption for UV lamps
- Limited effectiveness for high concentrations

### Plasma Air Purification

Non-thermal plasma generates reactive species for contaminant destruction.

**Technologies**:
- Dielectric barrier discharge (DBD)
- Corona discharge
- Packed-bed plasma reactors

**Considerations**:
- Ozone generation must be controlled
- Byproduct formation possible
- Energy requirements
- Effectiveness varies by compound

### Thermal Oxidation

High-temperature destruction for industrial applications:

- Catalytic oxidation: 200-400°C with catalyst
- Thermal oxidation: 700-1000°C
- Regenerative thermal oxidizers (RTO): 95%+ heat recovery

## System Design Considerations

### Contaminant Assessment

Design begins with characterizing the gaseous contaminant load:

1. **Source Inventory**: Identify all emission sources
2. **Emission Rates**: Quantify release rates (mg/h)
3. **Concentration Targets**: Establish acceptable levels
4. **Temporal Patterns**: Continuous vs. intermittent sources

### Media Selection

Match media to target compounds:

$$Breakthrough\ Time = \frac{W_s \cdot \rho_b}{Q \cdot C_{in}}$$

Where:
- $W_s$ = saturation capacity (g/g)
- $\rho_b$ = bed bulk density (g/L)
- $Q$ = volumetric flow rate (L/min)
- $C_{in}$ = inlet concentration (g/L)

### Bed Depth and Contact Time

**Empty Bed Contact Time (EBCT)**:
$$EBCT = \frac{V_{bed}}{Q}$$

Recommended EBCT values:

| Application | EBCT (seconds) |
|------------|----------------|
| Odor control | 0.05-0.1 |
| Light VOC | 0.1-0.2 |
| Heavy VOC | 0.2-0.5 |
| High efficiency | 0.5-1.0 |

### Humidity Effects

Relative humidity significantly impacts adsorption:

- RH <50%: Minimal impact
- RH 50-80%: Moderate capacity reduction
- RH >80%: Significant competitive adsorption of water

Hydrophobic media or air drying may be required for humid environments.

## Performance Monitoring

### Breakthrough Detection

Monitor downstream concentrations to detect media exhaustion:

- Continuous monitors for critical applications
- Periodic sampling programs
- Indicator compounds as proxies

### Service Life Estimation

$$Service\ Life = \frac{Media\ Capacity \times Media\ Mass}{Inlet\ Loading}$$

Conservative estimates account for:
- Humidity effects
- Temperature variations
- Contaminant mixture interactions
- Safety factors

Effective gaseous contaminant control requires understanding source characteristics, appropriate technology selection, and ongoing monitoring to ensure continued protection of indoor air quality and occupant health.