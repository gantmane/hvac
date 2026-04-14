---
title: "Inorganic Natural Refrigerants"
aliases: ["Inorganic Natural Refrigerants"]
description: "Comprehensive technical analysis of inorganic natural refrigerants including ammonia (R-717), carbon dioxide (R-744), water (R-718), and air (R-729). Covers thermodynamic properties, safety requirements, equipment specifications, and industrial applications for zero-ODP, zero-GWP refrigerants."
weight: 2
---

Inorganic natural refrigerants represent the oldest class of refrigerants in commercial use. These substances—ammonia, carbon dioxide, water, and air—occur naturally in the environment and possess zero ozone depletion potential (ODP) and zero direct global warming potential (GWP). Despite their environmental advantages, inorganic refrigerants present unique engineering challenges related to operating pressures, material compatibility, and safety requirements that distinguish them from synthetic alternatives.

## Fundamental Properties Comparison

The thermophysical properties of inorganic refrigerants differ significantly from synthetic refrigerants, requiring specialized design approaches.

| Property | R-717 (NH₃) | R-744 (CO₂) | R-718 (H₂O) | R-729 (Air) |
|----------|-------------|-------------|-------------|-------------|
| Molecular weight | 17.03 | 44.01 | 18.02 | 28.97 |
| Boiling point at 1 atm (°C) | -33.3 | -78.4 (sublimes) | 100.0 | -194.4 |
| Critical temperature (°C) | 132.3 | 31.0 | 374.1 | -140.7 |
| Critical pressure (bar) | 113.3 | 73.8 | 220.6 | 37.7 |
| ODP | 0 | 0 | 0 | 0 |
| GWP (100-yr) | 0 | 1 | 0 | 0 |
| ASHRAE 34 safety group | B2L | A1 | A1 | A1 |
| Latent heat at NBP (kJ/kg) | 1371 | 574 (at triple point) | 2257 | 199 |

## Ammonia (R-717)

### Thermodynamic Properties

Ammonia exhibits exceptional thermodynamic characteristics that make it the most efficient refrigerant for industrial applications. The latent heat of vaporization at normal boiling point reaches 1371 kJ/kg, approximately 5-7 times higher than synthetic refrigerants. This property results in significantly lower refrigerant mass flow rates for equivalent cooling capacity.

**Pressure-temperature relationship (Antoine equation):**

```
log₁₀(P) = A - B/(C + T)
```

Where:
- P = saturation pressure (bar)
- T = temperature (°C)
- A = 7.3605
- B = 1617.9
- C = 240.17

**Typical saturation conditions:**

| Temperature (°C) | Pressure (bar abs) | Liquid Density (kg/m³) | Vapor Density (kg/m³) | hfg (kJ/kg) |
|------------------|-------------------|------------------------|----------------------|-------------|
| -40 | 0.717 | 681.3 | 0.589 | 1436 |
| -30 | 1.195 | 671.5 | 0.954 | 1416 |
| -20 | 1.901 | 661.5 | 1.490 | 1396 |
| -10 | 2.908 | 651.2 | 2.264 | 1375 |
| 0 | 4.294 | 640.6 | 3.364 | 1354 |
| +10 | 6.153 | 629.6 | 4.906 | 1332 |
| +20 | 8.576 | 618.2 | 6.997 | 1308 |
| +30 | 11.67 | 606.2 | 9.797 | 1283 |
| +40 | 15.55 | 593.5 | 13.49 | 1256 |

### Coefficient of Performance

The volumetric refrigeration capacity of ammonia significantly exceeds that of synthetic refrigerants. For a single-stage system operating between -30°C evaporating and +30°C condensing:

```
COP = Qe / W = (h₁ - h₄) / (h₂ - h₁)
```

Typical single-stage COPs for ammonia systems:
- Low temperature (-40°C/-30°C evap, +30°C cond): 2.8-3.2
- Medium temperature (-10°C evap, +30°C cond): 4.5-5.2
- High temperature (+5°C evap, +30°C cond): 6.5-7.8

### Material Compatibility

Ammonia's chemical reactivity imposes strict material selection requirements. The refrigerant forms explosive compounds with mercury and attacks copper, brass, bronze, and other copper-bearing alloys through corrosive action.

**Acceptable materials:**
- Carbon steel (most common, cost-effective)
- Stainless steel (types 304, 316 for corrosive environments)
- Aluminum (limited applications, careful alloy selection)
- Ductile iron (centrifugal compressor casings)
- Malleable iron (valves, fittings)

**Prohibited materials:**
- Copper and copper alloys (>2% copper content)
- Mercury-containing devices
- Zinc-coated (galvanized) components in direct ammonia contact
- Most elastomers (Buna-N compatible, neoprene limited)

### Safety Classification and Hazards

ASHRAE Standard 34 classifies ammonia as Group B2L:
- **B**: Higher toxicity (IDLH = 300 ppm)
- **2L**: Lower flammability (LFL = 15%, UFL = 28% by volume in air)

**Toxicity thresholds:**
- Odor threshold: 5-50 ppm (detectable by smell)
- OSHA PEL (8-hr TWA): 25 ppm
- OSHA STEL (15-min): 35 ppm
- IDLH (Immediately Dangerous to Life or Health): 300 ppm
- LC₅₀ (rat, 4-hr inhalation): 2000 ppm

**Flammability characteristics:**
- Lower flammability limit: 15% by volume (150,000 ppm)
- Upper flammability limit: 28% by volume
- Autoignition temperature: 651°C (1204°F)
- Minimum ignition energy: 680 mJ

The concentration required for flammability (150,000 ppm) exceeds the lethal concentration by a factor of 75, making ammonia "self-alarming" at concentrations far below flammable levels. Practical refrigeration system leaks create toxic hazards before flammable mixtures develop.

### Detection and Monitoring

Ammonia detection systems employ multiple technologies for comprehensive coverage:

**Detection methods:**
1. **Electrochemical sensors**: 0-100 ppm range, 1 ppm resolution
2. **Infrared (IR) sensors**: 0-1000 ppm, immune to poisoning
3. **Photo-ionization detectors (PID)**: High sensitivity, fast response
4. **Colorimetric tubes**: Single-use verification

**Monitoring strategy per IIAR 2:**
- Machinery rooms: Continuous monitoring with alarm at 25 ppm
- Occupied spaces: Dual-level alarms (25 ppm alert, 150 ppm evacuate)
- Refrigerated spaces: Monitoring where personnel access occurs
- Alarm activation: Local audible/visual, HVAC system response, emergency notification

### Equipment Design Requirements

#### Compressors

Ammonia compressor selection depends on capacity range, efficiency requirements, and application constraints.

**Reciprocating compressors:**
- Capacity range: 10-1000 TR per unit
- Typical displacement: 50-5000 CFM
- Efficiency: 70-80% isentropic at design conditions
- Applications: Low and medium temperature, modular systems
- Configuration: Open-drive preferred for serviceability
- Materials: Ductile iron frame, forged steel crankshaft, aluminum pistons

**Screw compressors:**
- Capacity range: 100-5000 TR per unit
- Volume ratio: 2.0-5.0 (selected for pressure ratio)
- Efficiency: 75-85% isentropic with economizer
- Applications: Large industrial facilities, cold storage
- Oil management: High-efficiency coalescers required (>99.9% separation)
- Capacity control: Slide valve modulation, Vi adjustment

**Centrifugal compressors:**
- Capacity range: 1000-15,000 TR per unit
- Head coefficient: 0.45-0.60
- Efficiency: 78-82% polytropic
- Applications: Very large facilities, process cooling
- Materials: Ductile iron casing, 17-4PH stainless steel impellers
- Limitations: Surge control required, narrow operating range

#### Condensers and Evaporators

**Shell-and-tube heat exchangers:**
- Refrigerant in shell (ammonia corrosivity concern)
- Steel tubes (carbon or stainless)
- Tube-side velocity: 4-8 ft/s for water, 2-4 ft/s for glycol
- Shell-side design pressure: 250-300 psig typical
- Refrigerant charge: 0.15-0.30 lb per ton of refrigeration
- U-values: 150-300 Btu/(hr·ft²·°F) for evaporators, 200-400 for condensers

**Plate heat exchangers:**
- Compact design, 25-50% less refrigerant charge
- High heat transfer coefficients: 400-800 Btu/(hr·ft²·°F)
- Material: 316 stainless steel plates, Buna-N gaskets
- Pressure drop: 5-15 psi typical
- Applications: Liquid overfeed systems, cascade systems, sub-cooling

**Evaporative condensers:**
- Combined heat and mass transfer
- Design approach: 10-15°F above ambient wet bulb
- Water consumption: 3-5 GPM per 100 TR (evaporation + blowdown)
- Coil material: Steel tubes, aluminum or galvanized steel fins
- Capacity control: Fan cycling, two-speed fans, variable frequency drives

### Piping Design

Ammonia piping systems require careful sizing to balance refrigerant velocity, pressure drop, and oil return considerations.

**Velocity criteria:**

| Line Type | Minimum (ft/s) | Maximum (ft/s) | Purpose |
|-----------|----------------|----------------|---------|
| Suction (horizontal) | 800 FPM | 4000 FPM | Oil entrainment |
| Suction (vertical riser) | 1500 FPM | 4000 FPM | Oil return |
| Hot gas (horizontal) | 800 FPM | 5000 FPM | Oil entrainment |
| Hot gas (vertical riser) | 1500 FPM | 5000 FPM | Oil return |
| Liquid | 100 FPM | 300 FPM | Flash gas prevention |

**Pressure drop guidelines:**
- Suction lines: <2°F saturation temperature equivalent
- Discharge lines: <2 psi
- Liquid lines: <1°F saturation temperature equivalent

**Oil return provisions:**
- P-traps at base of all vertical risers
- Trap height: 12-18 inches
- Double risers for capacity modulation systems (switchover at 30-40% load)
- Suction line accumulator sizing: 50% of compressor oil charge minimum

### Industrial Applications

#### Cold Storage and Distribution Centers

Ammonia dominates large-scale refrigerated warehouse applications:

- Temperature ranges: -30°F to +35°F (multiple zones)
- Typical capacity: 1000-20,000 TR
- System configuration: Central engine room, distributed evaporators
- Refrigerant charge: 0.5-2.0 lb per TR (liquid overfeed systems)
- Operating cost advantage: 15-25% over HFC systems

**Design features:**
- Liquid overfeed evaporators (recirculation rates 2:1 to 4:1)
- Thermosiphon or pumped liquid recirculation
- Engine room segregation per IIAR 2 requirements
- Emergency ventilation: 30 air changes per hour machinery room minimum

#### Food Processing

Process applications leverage ammonia's high efficiency and food-grade compatibility:

**Blast freezing:**
- Temperature: -40°F to -60°F
- Air velocity: 1000-3000 FPM across product
- Freezing time: 4-12 hours to product center temperature
- Evaporator TD: 10-15°F

**Spiral freezers:**
- Continuous operation, product on conveyor belt
- Residence time: 20-90 minutes
- Ammonia charge: Limited by indirect systems (CO₂ cascade common)

**Ice production:**
- Plate ice: -20°F to -30°F brine, harvest cycle
- Tube ice: 15-20 minutes freeze, hot gas harvest
- Flake ice: Continuous harvest, rotating auger

#### Petrochemical and Gas Processing

Low-temperature ammonia systems serve hydrocarbon processing:

- Natural gas liquefaction: -40°F to -60°F
- NGL recovery: Cascade systems to -150°F (ammonia as first stage)
- Propylene refrigeration: Two-stage ammonia systems
- Capacity: 5,000-50,000 TR typical

### Regulatory Compliance

#### IIAR Standards

The International Institute of Ammonia Refrigeration publishes industry standards:

**IIAR 2 - Equipment, Design, and Installation:**
- Machinery room requirements (ventilation, egress, separation)
- Refrigerant charge limits for occupied spaces
- Relief valve sizing and discharge termination
- Purging and testing procedures

**IIAR 3 - Ammonia Refrigeration Valves:**
- Valve body material and pressure rating requirements
- Seat leakage classifications
- Marking and identification

**IIAR 4 - Installation of Closed-Circuit Ammonia Refrigeration Systems:**
- Brazing procedures and filler metals
- Pressure testing protocols (pneumatic, hydrostatic)
- System evacuation requirements

**IIAR 6 - Inspection, Testing, and Maintenance:**
- Inspection frequency and scope
- Pressure relief valve testing
- Documentation requirements

#### EPA and OSHA Requirements

**Process Safety Management (PSM):**
- Triggered at 10,000 lb ammonia threshold
- Process Hazard Analysis (PHA) required
- Management of Change (MOC) procedures
- Pre-startup safety reviews
- Mechanical integrity programs

**Risk Management Plan (RMP):**
- Triggered at 10,000 lb ammonia threshold (worst-case release scenarios)
- Off-site consequence analysis
- Prevention program documentation
- Emergency response coordination

## Carbon Dioxide (R-744)

### Thermodynamic Properties and Operating Regimes

Carbon dioxide presents unique thermodynamic characteristics due to its low critical temperature (31.0°C). Above this temperature, CO₂ cannot be condensed regardless of pressure, requiring transcritical operation in many climates.

**Critical point parameters:**
- Critical temperature: 31.0°C (87.8°F)
- Critical pressure: 73.8 bar (1070 psia)
- Critical density: 467.6 kg/m³

**Triple point:**
- Temperature: -56.6°C (-69.8°F)
- Pressure: 5.18 bar (75.1 psia)
- Note: CO₂ sublimes at atmospheric pressure

### Subcritical vs. Transcritical Operation

**Subcritical cycle** (ambient temperature < 31°C):
- Operates like conventional vapor-compression cycle
- Condensing pressure: 35-70 bar dependent on ambient
- Standard condenser design applicable
- COP: 2.5-4.0 depending on temperatures

**Transcritical cycle** (ambient temperature > 31°C or heat rejection > 31°C):
- High-side operates above critical pressure (>73.8 bar)
- Gas cooler replaces condenser (no phase change)
- Gas cooler outlet pressure and temperature independently controllable
- Optimum high-side pressure maximizes COP (typically 90-120 bar)
- Internal heat exchanger (suction line heat exchanger) essential for performance
- COP: 2.0-3.5 depending on temperatures

**Optimum discharge pressure (transcritical):**

```
P_opt ≈ 2.6 × T_gc - 0.0131 × T_gc² + 1.285 × T_evap
```

Where:
- P_opt = optimal gas cooler pressure (bar)
- T_gc = gas cooler outlet temperature (°C)
- T_evap = evaporation temperature (°C)

### Pressure-Enthalpy Characteristics

CO₂ exhibits steep isentropic curves and high volumetric refrigeration capacity.

**Comparison at typical conditions** (-10°C evap, 35°C condensing/gas cooling):

| Parameter | R-744 Subcritical | R-744 Transcritical | R-404A | R-717 |
|-----------|-------------------|---------------------|--------|-------|
| Evaporator pressure (bar) | 26.5 | 26.5 | 2.9 | 2.9 |
| Condenser/GC pressure (bar) | 68.0 | 100.0 | 15.8 | 11.7 |
| Compression ratio | 2.57 | 3.77 | 5.45 | 4.03 |
| Discharge temperature (°C) | 95 | 110 | 68 | 145 |
| Volumetric capacity (kJ/m³) | 22,500 | 18,000 | 2,950 | 1,750 |
| COP | 3.8 | 3.0 | 2.8 | 4.5 |

The volumetric capacity of CO₂ exceeds synthetic refrigerants by 6-10 times, enabling compact compressor designs but requiring attention to pressure drop in heat exchangers and piping.

### Equipment Requirements

#### Compressors

**Operating pressure considerations:**
- Suction pressure: 15-35 bar typical
- Discharge pressure: 40-130 bar (subcritical to transcritical)
- Design pressure: 140-160 bar for high-side components
- Pressure vessel code (ASME Section VIII) applies

**Reciprocating compressors:**
- Limited commercial availability
- Capacity: <100 TR typical
- Two-stage compression common for transcritical
- High bearing loads due to pressure differentials

**Semi-hermetic compressors:**
- Capacity: 5-150 TR
- Motor cooling via refrigerant vapor
- Applications: Commercial refrigeration, heat pumps
- Efficiency: 60-70% isentropic

**Transcritical scroll compressors:**
- Capacity: 2-15 TR per scroll
- Multiple scrolls paralleled for larger systems
- Motor cooling via vapor injection
- Discharge temperature control via economizer
- Applications: Small commercial, residential heat pump water heaters

**Multi-stage centrifugal:**
- Capacity: >500 TR
- 3-4 stages typical for transcritical operation
- Efficiency: 70-75% overall isentropic
- Applications: Large commercial, industrial process

#### Heat Exchangers

**Gas cooler/condenser design:**
- High-side design pressure: 140-160 bar minimum
- Approach temperature: 2-5°C (closer than HFC systems)
- Heat transfer coefficient: 2-5 times higher than HFCs
- Compact designs: microchannel, plate heat exchangers
- Materials: Stainless steel (pressure rating), copper (lower pressure applications)

**Evaporators:**
- Design pressure: 50-60 bar typical
- High refrigerant-side heat transfer coefficient reduces required area
- Direct expansion or pumped liquid overfeed
- Low refrigerant charge: 0.05-0.15 lb/TR

**Internal heat exchanger (IHX):**
- Essential for transcritical cycle efficiency improvement
- Effectiveness: 60-80% (ε = (T_hot,in - T_hot,out) / (T_hot,in - T_cold,in))
- COP improvement: 10-25% depending on operating conditions
- Configuration: Coaxial tube, plate, or tube-in-tube

#### Expansion Devices and High-Side Pressure Control

**Transcritical systems require controlled expansion:**

**Electronic expansion valve (EEV):**
- Fast response for superheat control
- Multiple valves for capacity modulation
- High pressure drop capability (60-80 bar)

**High-side pressure control valve:**
- Maintains optimum gas cooler pressure
- Modulates based on gas cooler outlet temperature and evaporator load
- Critical for transcritical COP optimization
- Control algorithm: P_opt = f(T_gc, T_evap, ambient conditions)

**Back pressure regulator:**
- Subcritical systems or low-temperature cascade applications
- Maintains minimum evaporator pressure during low load

### Applications

#### Cascade Systems

CO₂ serves as the low-stage refrigerant in cascade systems for temperatures below -40°C:

**Configuration:**
- High stage: NH₃, HFC, or HFO refrigerant
- Low stage: CO₂ (subcritical operation)
- Cascade condenser: CO₂ condenses at -10 to -30°C
- CO₂ evaporating temperature: -45 to -65°C

**Advantages:**
- Lower compression ratio per stage
- High volumetric capacity reduces low-stage compressor size
- Separation of refrigerants (ammonia not in occupied/cold storage spaces)
- Total efficiency improvement: 10-15% vs. single-stage NH₃

**Applications:**
- Blast freezing (food processing)
- Ultra-low temperature storage (-60°F pharmaceutical, biological)
- Freeze-drying
- Cryogenic processing

#### Supermarket Refrigeration

Direct expansion transcritical CO₂ systems increasingly replace HFC distributed systems:

**Booster configuration:**
- Medium temperature (MT) compressors: discharge to gas cooler (90-120 bar)
- Low temperature (LT) compressors: discharge to MT suction (26-30 bar)
- Single high-side heat rejection
- Operating range: -35°C to +2°C

**Parallel compression:**
- Auxiliary compressors for flash gas
- 5-10% capacity increase
- 3-8% COP improvement

**Advantages over HFC systems:**
- Zero direct GWP (regulatory future-proofing)
- High efficiency in cold climates (subcritical operation)
- Reduced refrigerant charge per system capacity
- Food safety (non-toxic, asphyxiation risk only at high concentrations)

**Challenges:**
- Lower COP in hot climates (transcritical operation)
- Higher equipment first cost (high pressure components)
- Requires electronic controls for pressure optimization

#### Heat Pump Water Heaters

Transcritical CO₂ cycle efficiently produces hot water due to gas cooler glide:

**Operating characteristics:**
- Water heating: 10°C inlet to 60-90°C outlet
- Gas cooler pressure: 100-120 bar
- Evaporator source: ambient air, exhaust air, ground loop
- COP: 3.0-5.0 (varies with source and water temperatures)

**Temperature glide advantage:**
- Gas cooler temperature glide matches water temperature rise
- Reduced exergy destruction vs. isothermal condensing
- Efficiency advantage over HFC systems for high-temperature lift

**Applications:**
- Residential hot water (80-500 L tanks)
- Commercial hot water (restaurants, hotels, industrial)
- Combined space heating and hot water
- Industrial process heating (<90°C)

#### Secondary Refrigerant Systems

Liquid CO₂ serves as secondary refrigerant (heat transfer fluid) in indirect systems:

**Properties as secondary fluid:**
- Operating range: -50°C to +10°C (subcritical liquid)
- Density: 925-1150 kg/m³ (temperature dependent)
- Specific heat: 2.0-3.5 kJ/(kg·K) (increases near critical point)
- Viscosity: 0.08-0.15 mPa·s (low pumping energy)
- Thermal conductivity: 0.10-0.16 W/(m·K)

**Advantages over glycol:**
- Higher heat transfer coefficient (lower approach temperatures)
- Lower viscosity (reduced pumping power)
- Non-toxic (food safety applications)
- Lower environmental impact

**System design:**
- Primary refrigerant: NH₃, HFC, HFO (charges isolated to machinery room)
- CO₂ circuit: Pumped liquid to evaporators, return to primary chiller
- Pressure maintenance: 20-30 bar typical (subcritical liquid phase)
- Applications: Food processing, cold storage, ice rinks

### Safety Considerations

**ASHRAE 34 classification:** A1 (non-toxic, non-flammable)

**Asphyxiation risk:**
- CO₂ displaces oxygen in confined spaces
- No odor warning (odorless, colorless)
- OSHA PEL: 5000 ppm (0.5%) TWA 8-hr
- NIOSH STEL: 30,000 ppm (3%) 15-min exposure limit
- Physiological effects: >40,000 ppm (4%) causes distress, >100,000 ppm (10%) unconsciousness

**Detection and monitoring:**
- Infrared CO₂ sensors (0-5000 ppm for occupied spaces, 0-50,000 ppm for machinery rooms)
- Ventilation interlock at alarm threshold (typically 5000 ppm)
- Personal monitors for confined space entry

**Physical hazards:**
- High pressure system (blow-out, pipe whip potential)
- Rapid decompression converts liquid to solid (dry ice) and vapor
- Cold burn hazard from direct contact with liquid or dry ice
- Pressure relief discharge requires controlled termination

**Pressure relief requirements:**
- ASME Section VIII pressure vessel code applies
- Relief valve sizing accounts for fire exposure, tube rupture scenarios
- Discharge to atmosphere (ventilated location, above roof level)
- Vent stack sizing: prevent excessive back-pressure

## Water (R-718)

### Thermodynamic Properties

Water functions as a refrigerant in absorption cycles and vapor-compression systems operating at evaporator pressures below atmospheric (vacuum conditions).

**Saturation properties:**

| Temperature (°C) | Pressure (kPa abs) | Pressure (in. Hg abs) | hfg (kJ/kg) | vg (m³/kg) | ρg (kg/m³) |
|------------------|--------------------|-----------------------|-------------|------------|------------|
| 0 | 0.611 | 0.18 | 2501 | 206.1 | 0.00485 |
| 4 | 0.813 | 0.24 | 2491 | 157.2 | 0.00636 |
| 5 | 0.872 | 0.26 | 2489 | 147.1 | 0.00680 |
| 6 | 0.935 | 0.28 | 2487 | 137.7 | 0.00726 |
| 8 | 1.072 | 0.32 | 2483 | 120.9 | 0.00827 |
| 10 | 1.228 | 0.36 | 2478 | 106.4 | 0.00940 |
| 12 | 1.402 | 0.41 | 2474 | 93.8 | 0.01066 |
| 15 | 1.705 | 0.50 | 2466 | 77.9 | 0.01284 |

The extremely low vapor density necessitates very large compressor displacement for practical refrigeration capacity.

### Vacuum Operation Requirements

Water refrigerant systems operate at subatmospheric evaporator pressures, requiring specialized design approaches:

**Operating pressure range:**
- Evaporator: 0.6-1.7 kPa abs (0.18-0.50 in. Hg abs) for 0-15°C chilled water
- Condenser: 5-10 kPa abs (1.5-3.0 in. Hg abs) for 30-40°C cooling water
- Absolute pressure required (no leaks inward)

**Air leakage challenges:**
- Atmospheric air infiltrates through any leak path
- Non-condensable gases accumulate in condenser
- Performance degradation: 1% air concentration reduces capacity 5-10%
- Continuous purging system required

**Purge systems:**
- Mechanical vacuum pump with condensing trap
- Thermal purge (refrigerant vapor jet)
- Purge rate: 0.1-0.5% of refrigerant circulation rate

### Centrifugal Compressor Design

Water vapor's low density (approximately 1/100 of HFC refrigerants) requires multi-stage centrifugal compression:

**Design characteristics:**
- Stages: 2-3 stages typical
- Impeller diameter: 1.0-2.5 m (large)
- Tip speed: 300-450 m/s
- Volume flow: 500-5000 m³/min at inlet
- Capacity per unit: 500-10,000 TR

**Efficiency considerations:**
- Polytropic efficiency: 75-82%
- Mach number limitations at impeller tip
- Reynolds number effects (low density, high velocity)
- Interstage economizers improve performance

**Materials:**
- Steel or aluminum impellers (corrosion resistance)
- Stainless steel shaft
- Non-oxidizing bearing lubrication (vacuum environment)

### Applications

#### Large Centrifugal Chillers

Water refrigerant (R-718) applies to very large capacity commercial and industrial cooling:

**Capacity range:**
- Minimum practical: 500 TR (compressor size constraints)
- Common range: 1000-5000 TR
- Maximum installations: >10,000 TR

**Operating conditions:**
- Chilled water: 5-15°C supply, 10-20°C return
- Cooling water: 25-35°C inlet, 30-40°C outlet
- COP: 4.5-6.5 depending on lift and compressor efficiency

**Advantages:**
- Zero ODP, zero GWP, zero toxicity
- Lowest cost refrigerant (water)
- No refrigerant regulations or phase-outs
- Minimal environmental consequence from leaks

**Disadvantages:**
- High first cost (large compressor, vacuum system)
- Vacuum operation complexity (air removal, leak prevention)
- Freeze protection required (0°C evaporator limit)
- Limited to large capacities (economies of scale)

#### Turbo-Compressor Chillers

Advanced water vapor compression systems employ high-speed turbomachinery:

**Compressor technology:**
- Direct-drive or high-speed gearless motor (3600-10,000 RPM)
- Variable frequency drive (VFD) for capacity control
- Magnetic bearing systems (oil-free, vacuum compatible)
- Part-load efficiency optimization via speed modulation

**Performance characteristics:**
- Full-load COP: 5.0-6.5
- Part-load IPLV: 7.0-10.0 (integrated part-load value)
- Turndown: 10-100% capacity
- Operating range: 5-18°C chilled water

**Control strategy:**
- Compressor speed varies to maintain chilled water setpoint
- Inlet guide vanes (if equipped) for additional modulation
- Condenser water temperature reset for efficiency optimization
- Anti-surge control (centrifugal compressor limitation)

#### Absorption System Integration

Water serves as refrigerant in lithium bromide absorption systems, paired with centrifugal water chillers for hybrid arrangements:

**Configuration:**
- Electric centrifugal chiller provides base load and peak capacity
- Absorption chiller operates on waste heat, thermal energy, or natural gas
- Both use water as refrigerant (common maintenance procedures, controls)

**Advantages of hybrid system:**
- Electric demand reduction (absorption handles partial load)
- Thermal energy utilization (CHP systems, district heating)
- Redundancy (either system can provide partial cooling)
- Peak shaving (reduce electric utility demand charges)

## Air (R-729)

### Properties and Limitations

Air functions as a refrigerant in specialized cryogenic applications and historical systems (bell-coleman cycle).

**Thermodynamic properties:**
- Critical temperature: -140.7°C (-221°F)
- Critical pressure: 37.7 bar abs
- Specific heat (constant pressure): 1.005 kJ/(kg·K)
- Specific heat ratio: 1.4 (γ = cp/cv)

### Reverse Brayton Cycle

Air refrigeration operates on the reverse Brayton cycle (gas refrigeration cycle):

**Cycle processes:**
1. Isentropic compression (1→2): Compressor raises air pressure and temperature
2. Constant pressure heat rejection (2→3): Air cooler rejects heat to ambient
3. Isentropic expansion (3→4): Expander reduces pressure and temperature
4. Constant pressure heat addition (4→1): Air absorbs refrigeration load

**COP equation:**

```
COP = (T₁ - T₄) / (T₂ - T₁) = 1 / [(P₂/P₁)^((γ-1)/γ) - 1]
```

Where:
- T₁ = evaporator inlet temperature
- T₂ = compressor discharge temperature
- T₄ = expander discharge temperature (cold air)
- P₁, P₂ = low and high pressures
- γ = specific heat ratio (1.4 for air)

**Typical performance:**
- COP: 0.5-1.5 (low compared to vapor compression)
- Temperature range: -50 to -150°C
- Pressure ratio: 3-10

### Applications

**Aircraft cooling:**
- Air cycle machine (ACM) provides cabin conditioning
- Ram air compressed, cooled, expanded through turbine
- Simple cycle or bootstrap cycle configurations
- Advantages: Lightweight, air source available, no refrigerant leakage concerns

**Cryogenic gas separation:**
- Air liquefaction plants
- Multiple-stage compression with intercooling
- Expansion through turbo-expanders
- Produces liquid oxygen, nitrogen, argon

**Industrial gas turbine inlet cooling:**
- Evaporative cooling or mechanical refrigeration pre-cools inlet air
- Power augmentation during high ambient temperatures
- Gas turbine output increases with lower inlet temperature
- Simple cycle or combined cycle power plants

## Environmental and Regulatory Advantages

### Zero Ozone Depletion Potential

All inorganic natural refrigerants possess zero ODP:
- No chlorine or bromine atoms (ozone-catalytic destruction mechanisms absent)
- Montreal Protocol compliance (no phase-out schedules)
- No stratospheric lifetime concerns

### Zero Direct Global Warming Potential

Inorganic refrigerants contribute zero direct GWP:
- CO₂ GWP = 1 by definition (reference substance)
- NH₃, H₂O, air: GWP = 0 (naturally occurring at stable atmospheric concentrations)
- Indirect GWP from energy consumption remains (efficiency critical)

### Regulatory Landscape

**European F-Gas Regulation:**
- HFC phase-down drives adoption of natural refrigerants
- Inorganic refrigerants exempt from quota system
- Incentives for low-GWP alternatives

**EPA SNAP Program (US):**
- Ammonia acceptable for industrial process refrigeration, cold storage
- CO₂ acceptable for all applications (ASHRAE 34 A1 classification)
- Water acceptable for comfort cooling, process applications

**California CARB Regulations:**
- GWP limits for commercial refrigeration (2023-2030)
- Natural refrigerants preferred alternative
- Mandatory leak repair thresholds do not apply to CO₂

**International:**
- Kigali Amendment to Montreal Protocol (HFC reduction)
- 80-85% HFC reduction by 2047 (developed nations)
- Natural refrigerants facilitate compliance

## System Design Considerations

### Refrigerant Selection Matrix

Selection among inorganic refrigerants depends on application requirements:

| Criterion | R-717 (NH₃) | R-744 (CO₂) | R-718 (H₂O) | R-729 (Air) |
|-----------|-------------|-------------|-------------|-------------|
| Best efficiency | Industrial | Cascade low-stage | Large chillers | Limited |
| Temperature range | -50 to +10°C | -60 to +10°C | +4 to +15°C | -150 to -40°C |
| Safety class | B2L (toxic) | A1 (safe) | A1 (safe) | A1 (safe) |
| Pressure level | Moderate | Very high | Vacuum | High |
| Equipment cost | Moderate | High | Very high | Moderate |
| Charge per capacity | Moderate | Low | N/A | N/A |
| Material restrictions | Significant | Minimal | Minimal | None |
| Maintenance | Specialized | Moderate | Complex | Simple |

### Hybrid and Cascade Configurations

Combining inorganic refrigerants optimizes system performance:

**NH₃/CO₂ cascade:**
- High stage: Ammonia (condenses at ambient conditions)
- Low stage: CO₂ (subcritical, high efficiency at low temperatures)
- Intermediate temperature: -20 to -40°C
- Applications: Supermarket LT, blast freezing, ice rinks
- Advantages: Ammonia confined to machinery room, CO₂ in occupied spaces (A1 classification)

**CO₂/water indirect systems:**
- Primary: Any refrigerant in machinery room
- Secondary fluid: Liquid CO₂ or water/ice slurry
- Advantages: Reduced primary refrigerant charge, leak isolation, redundancy

### Energy Recovery and Efficiency Enhancement

**Ammonia systems:**
- Desuperheating for hot water/process heating (discharge gas 140-180°F)
- Sub-cooling via mechanical subcoolers or ambient cooling
- Variable-speed compressors and condensing fans
- Floating head pressure control (condenser pressure tracks ambient)

**CO₂ transcritical systems:**
- Internal heat exchanger (IHX) mandatory for efficiency
- Parallel compression captures flash gas for 5-10% improvement
- Ejectors recover expansion work (experimental, 5-8% COP improvement)
- Heat recovery from gas cooler for space heating, water heating (60-95°C)

**Water vapor systems:**
- Free cooling via waterside economizer when ambient permits
- Variable-speed compressor optimization at part load
- Condenser water temperature reset based on ambient wet bulb
- Heat recovery chillers (simultaneous heating and cooling)

## Conclusion

Inorganic natural refrigerants represent mature, proven technologies with inherent environmental advantages. Ammonia dominates industrial refrigeration due to exceptional efficiency and thermodynamic properties despite toxicity and flammability concerns. Carbon dioxide enables distributed refrigeration in commercial applications and provides unique advantages in cascade systems and heat pumping to high temperatures. Water serves niche applications in very large chillers where vacuum operation complexity is justified. Air refrigeration remains limited to specialized cryogenic and aircraft applications.

Selection among inorganic refrigerants requires balancing efficiency, safety, system complexity, first cost, and regulatory compliance. Ongoing technology development focuses on advanced system configurations (ejectors, parallel compression, hybrid systems) and control strategies that maximize the performance potential of these zero-ODP, zero-GWP refrigerants. As regulatory pressure accelerates the phase-down of high-GWP synthetic refrigerants, inorganic natural refrigerants will continue expanding into new applications beyond their traditional domains.
