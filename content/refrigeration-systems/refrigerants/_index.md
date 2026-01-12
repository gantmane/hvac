---
title: "Refrigerants"
weight: 8
---

Refrigerants are working fluids used in vapor compression refrigeration cycles to absorb heat at low temperature and pressure, then reject heat at higher temperature and pressure. The selection of refrigerant fundamentally determines system performance, efficiency, safety characteristics, and environmental impact. Modern refrigerant selection involves balancing thermodynamic properties, environmental considerations, safety requirements, regulatory compliance, and economic factors.

## Fundamental Properties

Refrigerant performance depends on thermophysical properties that govern heat transfer, pressure-volume relationships, and transport characteristics.

### Thermodynamic Properties

**Vapor Pressure Characteristics**
- Evaporator pressure must remain above atmospheric to prevent air infiltration
- Condenser pressure should not exceed equipment pressure ratings
- Pressure ratio affects compressor efficiency and discharge temperature
- Critical temperature must exceed maximum condensing temperature

**Latent Heat of Vaporization**
- Higher latent heat reduces refrigerant mass flow rate for given capacity
- Affects compressor displacement requirements
- Influences heat exchanger sizing
- Varies with saturation temperature

**Specific Heat and Density**
- Liquid specific heat affects subcooling effectiveness
- Vapor specific heat determines superheat temperature rise
- Liquid density impacts pump sizing and pipe friction losses
- Vapor density affects compressor displacement and pressure drop

### Transport Properties

**Thermal Conductivity**
- Affects heat transfer coefficients in evaporators and condensers
- Influences nucleate boiling performance
- Important for low-temperature applications

**Viscosity**
- Liquid viscosity affects pressure drop and film heat transfer
- Vapor viscosity influences compressor efficiency
- Critical for oil return in direct expansion systems

**Surface Tension**
- Influences nucleate boiling heat transfer
- Affects refrigerant-oil miscibility
- Important for flooded evaporator design

## Refrigerant Classification Systems

### ASHRAE Numbering System

The ASHRAE Standard 34 numbering system provides systematic identification:

**Methane-Series Compounds (R-10 through R-50)**
- First digit: (number of carbon atoms - 1)
- Second digit: (number of hydrogen atoms + 1)
- Third digit: number of fluorine atoms
- Example: R-134a has 2 carbons, 2 hydrogens, 4 fluorines

**Ethane-Series Compounds (R-100 through R-200)**
- Follows same pattern with first digit representing carbon atoms
- Example: R-125 has 2 carbons, 1 hydrogen, 5 fluorines

**Isomer Designation**
- Lowercase letters (a, b, c) denote increasingly asymmetric isomers
- Most symmetric structure has no letter designation

**Zeotropic Blends (R-400 series)**
- Temperature glide during phase change
- Composition changes with leakage
- Requires special charging and service procedures

**Azeotropic and Near-Azeotropic Blends (R-500 series)**
- No temperature glide or minimal glide
- Constant composition during phase change
- Can be charged as vapor or liquid

**Organic Compounds (R-600 series)**
- Hydrocarbons and other organic refrigerants
- Example: R-600a (isobutane), R-290 (propane)

## Refrigerant Categories by Chemical Composition

| Category | Chemical Structure | Examples | Characteristics |
|----------|-------------------|----------|-----------------|
| CFCs | Chlorofluorocarbons | R-11, R-12, R-113, R-115 | High ODP, banned under Montreal Protocol |
| HCFCs | Hydrochlorofluorocarbons | R-22, R-123, R-124 | Moderate ODP, phaseout in progress |
| HFCs | Hydrofluorocarbons | R-134a, R-410A, R-407C | Zero ODP, high GWP, regulated under Kigali Amendment |
| HFOs | Hydrofluoroolefins | R-1234yf, R-1234ze(E) | Zero ODP, low GWP, mildly flammable |
| Natural Refrigerants | Hydrocarbons, CO₂, NH₃ | R-290, R-600a, R-744, R-717 | Zero ODP, low GWP, safety considerations |
| Blends | Mixtures of above | R-404A, R-407C, R-448A, R-449A | Properties depend on composition |

## Environmental Properties

### Ozone Depletion Potential (ODP)

ODP quantifies the relative capacity of a refrigerant to destroy stratospheric ozone, referenced to R-11 (ODP = 1.0).

**Mechanism**
- Chlorine and bromine atoms catalytically destroy ozone molecules
- One chlorine atom can destroy thousands of ozone molecules
- Stratospheric lifetime determines total ozone depletion

**Regulatory Impact**
- Montreal Protocol (1987) mandated CFC phaseout
- Copenhagen Amendment accelerated schedule
- HCFCs subject to progressive reduction and elimination

| Refrigerant | Chemical Formula | ODP | Status |
|-------------|------------------|-----|--------|
| R-11 | CCl₃F | 1.0 | Banned (1996) |
| R-12 | CCl₂F₂ | 1.0 | Banned (1996) |
| R-22 | CHClF₂ | 0.055 | Production banned (2020), service allowed until 2030 |
| R-123 | CHCl₂CF₃ | 0.02 | Limited production for specific uses |
| R-134a | CH₂FCF₃ | 0 | Allowed but GWP regulated |
| R-410A | R-32/R-125 | 0 | Allowed but GWP regulated |

### Global Warming Potential (GWP)

GWP measures the heat-trapping capacity of a refrigerant over 100 years relative to CO₂ (GWP = 1).

**Total Equivalent Warming Impact (TEWI)**
TEWI = Direct Emissions + Indirect Emissions

Direct emissions result from refrigerant leakage and end-of-life losses.
Indirect emissions result from energy consumption and associated CO₂ production.

**Life Cycle Climate Performance (LCCP)**
More comprehensive than TEWI, including manufacturing, transport, and disposal impacts.

| Refrigerant | GWP (AR5) | Application Category | Regulatory Trend |
|-------------|-----------|----------------------|------------------|
| R-744 (CO₂) | 1 | Transcritical systems, cascade | Increasing |
| R-290 (Propane) | 3 | Small commercial, domestic | Increasing |
| R-717 (Ammonia) | 0 | Industrial refrigeration | Stable |
| R-1234yf | 4 | Mobile A/C, chillers | Increasing |
| R-1234ze(E) | 6 | Centrifugal chillers | Increasing |
| R-32 | 675 | Split A/C, heat pumps | Transitional |
| R-134a | 1430 | Chillers, mobile A/C | Declining |
| R-410A | 2088 | Unitary equipment | Declining |
| R-404A | 3922 | Commercial refrigeration | Phaseout |
| R-507A | 3985 | Low-temp refrigeration | Phaseout |

## Safety Classifications

ASHRAE Standard 34 and ISO 817 establish refrigerant safety classifications based on toxicity and flammability.

### Classification Matrix

| Class | Toxicity | Flammability | Examples | Applications |
|-------|----------|--------------|----------|--------------|
| A1 | Lower | No flame propagation | R-134a, R-410A, R-744 | General HVAC, most common |
| A2L | Lower | Lower flammability | R-32, R-1234yf, R-1234ze(E) | Modern low-GWP systems |
| A2 | Lower | Flammable | R-152a | Limited applications |
| A3 | Lower | Higher flammability | R-290, R-600a, R-1270 | Requires strict safety measures |
| B1 | Higher | No flame propagation | R-123 | Low-pressure chillers |
| B2L | Higher | Lower flammability | R-717/R-1234yf blends | Specialized industrial |
| B2 | Higher | Flammable | Ammonia/hydrocarbon blends | Rare, specialized |
| B3 | Higher | Higher flammability | R-717 (NH₃) | Industrial refrigeration |

### Toxicity Criteria

**Class A (Lower Toxicity)**
- Occupational Exposure Limit (OEL) ≥ 400 ppm
- Suitable for occupied spaces with proper design
- Standard ventilation requirements

**Class B (Higher Toxicity)**
- OEL < 400 ppm
- Requires refrigerant detection systems
- Machinery room requirements more stringent
- Ammonia (R-717): OEL = 25 ppm

### Flammability Criteria

**Class 1 (No Flame Propagation)**
- Will not propagate flame under ASHRAE 34 test conditions
- No special flammability precautions required

**Class 2L (Lower Flammability)**
- Burning velocity < 10 cm/s
- Heat of combustion < 19 kJ/kg
- Limited charge size regulations
- Requires ignition source risk assessment

**Class 2 (Flammable)**
- Lower flammability limit (LFL) > 0.10 kg/m³
- Heat of combustion ≥ 19 kJ/kg
- Significant safety design requirements

**Class 3 (Higher Flammability)**
- LFL ≤ 0.10 kg/m³ or burning velocity ≥ 10 cm/s
- Stringent safety requirements
- Machinery room isolation mandatory
- Explosion-proof electrical equipment

## Refrigerant Selection Criteria

### Performance Factors

**Thermodynamic Efficiency**
- Coefficient of Performance (COP) in intended operating range
- Pressure ratio across compressor
- Discharge temperature limits
- Volumetric capacity (refrigeration effect per unit volume)

**Compatibility**
- Materials compatibility (metals, elastomers, plastics)
- Lubricant miscibility and solubility
- Moisture tolerance
- Chemical stability at operating temperatures

**Heat Transfer Characteristics**
- Evaporation and condensation coefficients
- Pressure drop characteristics
- Nucleate boiling performance
- Transport properties

### Regulatory Compliance

**International Agreements**
- Montreal Protocol: ODP restrictions
- Kigali Amendment: HFC phasedown schedule
- F-Gas Regulation (EU): Progressive reduction quotas
- AIM Act (USA): HFC production and consumption reduction

**Building Codes and Standards**
- International Mechanical Code (IMC)
- Uniform Mechanical Code (UMC)
- ASHRAE Standard 15: Safety Standard for Refrigeration Systems
- ASHRAE Standard 34: Designation and Safety Classification

**Charge Limits**
- Refrigerant quantity restrictions based on safety class
- Occupied space vs. machinery room requirements
- Probability of exposure calculations
- Ventilation and detection requirements

### Economic Considerations

**Refrigerant Cost**
- Initial charge cost
- Replacement and service costs
- Price volatility and availability
- Reclamation value

**System Cost Impact**
- Pressure ratings and materials
- Safety equipment requirements
- Efficiency-related energy costs
- Maintenance and service complexity

## Common Refrigerant Properties

| Refrigerant | Molecular Weight | Normal BP (°C) | Critical Temp (°C) | Critical Press (kPa) | Safety Class |
|-------------|-----------------|----------------|-------------------|---------------------|--------------|
| R-22 | 86.5 | -40.8 | 96.1 | 4990 | A1 |
| R-32 | 52.0 | -51.7 | 78.1 | 5782 | A2L |
| R-123 | 152.9 | 27.8 | 183.7 | 3662 | B1 |
| R-134a | 102.0 | -26.1 | 101.1 | 4059 | A1 |
| R-290 (Propane) | 44.1 | -42.1 | 96.7 | 4251 | A3 |
| R-404A | 97.6 | -46.5 | 72.1 | 3735 | A1 |
| R-407C | 86.2 | -43.6 | 86.7 | 4631 | A1 |
| R-410A | 72.6 | -51.4 | 71.3 | 4901 | A1 |
| R-600a (Isobutane) | 58.1 | -11.7 | 134.7 | 3629 | A3 |
| R-717 (Ammonia) | 17.0 | -33.3 | 132.3 | 11,333 | B2L |
| R-744 (CO₂) | 44.0 | -78.4* | 31.0 | 7377 | A1 |
| R-1234yf | 114.0 | -29.5 | 94.7 | 3382 | A2L |
| R-1234ze(E) | 114.0 | -19.0 | 109.4 | 3636 | A2L |

*Sublimation temperature at atmospheric pressure

## Pressure-Temperature Relationships

Refrigerant vapor pressure varies exponentially with temperature according to the Clausius-Clapeyron relation. System designers must ensure:

- Evaporator pressure remains sufficiently above atmospheric pressure
- Condenser pressure does not exceed equipment ratings
- Pressure ratio remains within compressor design limits
- Discharge temperature stays below decomposition limits

**Representative Saturation Pressures (kPa absolute)**

| Refrigerant | -40°C | -20°C | 0°C | 20°C | 40°C | 60°C |
|-------------|-------|-------|-----|------|------|------|
| R-22 | 153 | 244 | 498 | 910 | 1533 | 2430 |
| R-134a | 51 | 133 | 293 | 572 | 1017 | 1702 |
| R-404A | 144 | 265 | 527 | 964 | 1622 | 2567 |
| R-410A | 220 | 406 | 755 | 1337 | 2215 | 3431 |
| R-717 (NH₃) | 71 | 190 | 430 | 857 | 1554 | 2614 |

## Refrigerant Transitions and Replacements

### Historical Evolution

**First Generation (Pre-1990s)**
- R-12, R-22, R-502 dominated
- CFCs widely used
- No environmental regulations

**Second Generation (1990s-2010s)**
- HCFCs as transitional refrigerants
- HFCs as long-term replacements
- Montreal Protocol implementation

**Third Generation (2010s-Present)**
- Low-GWP HFOs and HFO blends
- Natural refrigerant resurgence
- Kigali Amendment phasedown

### Drop-In and Retrofit Considerations

**True Drop-In Requirements**
- Same safety classification
- Compatible with existing lubricant
- Similar operating pressures
- No equipment modifications required

**Practical Retrofit**
- May require lubricant change
- Pressure transducer recalibration
- Control algorithm adjustments
- Performance verification

**Common Replacement Paths**

| Original | Common Replacements | Notes |
|----------|-------------------|-------|
| R-12 | R-134a, R-1234yf | Requires POE oil, smaller charge |
| R-22 | R-410A, R-32, R-454B | New equipment preferred, retrofit challenging |
| R-404A | R-407A, R-407F, R-448A, R-449A | Zeotropic blends, charge management critical |
| R-502 | R-404A, R-507A | Now being phased out themselves |

## Charging and Handling Requirements

### Charging Methods

**Vapor Charging**
- Required for zeotropic blends during system operation
- Prevents composition shift
- Slower process
- Used for final topping-up

**Liquid Charging**
- Acceptable for pure refrigerants and azeotropes
- Must charge into liquid line or through restriction
- Faster bulk charging
- Risk of compressor liquid slugging if improper

### Leak Detection

**Detection Methods by Sensitivity**
- Electronic leak detectors: 0.1-0.5 oz/year
- Ultrasonic detectors: larger leaks, non-specific
- Fluorescent dyes: visual identification
- Soap bubbles: qualitative, low-cost

**Regulatory Leak Rate Thresholds**
- Commercial refrigeration: 35% annually (EPA)
- Industrial process: 35% annually
- Comfort cooling: 20% annually
- Trigger mandatory repair requirements

### Recovery and Reclamation

**Recovery**
- Removal from system to external storage
- Required before servicing or disposal
- Equipment must meet EPA/AHRI standards

**Recycling**
- Oil separation and filtration
- Reduces moisture and particulates
- Can be returned to same system

**Reclamation**
- Reprocessing to ARI 700 specifications
- Chemical analysis required
- Returns refrigerant to virgin specification

This overview establishes the foundation for understanding modern refrigerant selection, application, and management in HVAC and refrigeration systems. Subsequent sections detail specific refrigerant types, system applications, and regulatory compliance strategies.
