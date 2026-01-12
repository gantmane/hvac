---
title: "Receiving Raw Milk"
description: "Technical requirements for raw milk receiving systems including tanker unloading, plate cooling, immediate refrigeration, and PMO compliance for dairy processing facilities"
weight: 1
---

Raw milk receiving represents the critical first stage in dairy processing where proper refrigeration system design directly impacts product quality, regulatory compliance, and processing efficiency. The receiving system must rapidly cool incoming milk from farm temperatures while maintaining continuous temperature monitoring and microbiological quality control.

## Receiving Bay Environmental Requirements

The receiving area requires controlled environmental conditions to support equipment operation and prevent contamination.

### Temperature Control

| Parameter | Requirement | Design Basis |
|-----------|-------------|--------------|
| Bay Air Temperature | 10-15°C | Equipment protection |
| Maximum Air Temperature | 21°C | PMO sanitation standards |
| Minimum Air Temperature | 4°C | Personnel comfort |
| Temperature Uniformity | ±2°C | Consistent operation |
| Relative Humidity | 50-70% | Condensation prevention |

The receiving bay HVAC system must provide:

- Ventilation rate: 10-15 air changes per hour minimum
- Positive pressurization: 0.02-0.03 in. w.g. (5-7.5 Pa) relative to exterior
- Filtered air supply: MERV 8 minimum, MERV 13 preferred
- Emergency ventilation capability for refrigerant release scenarios

### Structural Integration

Refrigeration equipment placement requires:

**Loading dock configuration:**
- Multiple tanker positions with independent unloading capability
- Overhead door vestibules with air curtains (3000-4000 fpm discharge velocity)
- Insulated dock seals to minimize infiltration
- Floor drainage pitched to collection points (minimum 1/4 in. per foot slope)

**Equipment zones:**
- Heated areas for pumps and instrumentation (maintain above 10°C)
- Refrigerated equipment rooms maintained at 15-18°C
- Separation between glycol systems and ammonia refrigeration zones

## Tanker Unloading System Design

### Milk Tanker Specifications

Farm milk arrives in insulated tankers designed to maintain temperature during transport:

| Tanker Capacity | Typical Range | Insulation Value |
|-----------------|---------------|------------------|
| Small | 3,000-6,000 gallons (11,400-22,700 L) | R-10 to R-15 |
| Standard | 6,000-7,000 gallons (22,700-26,500 L) | R-12 to R-18 |
| Large | 7,000-8,000 gallons (26,500-30,300 L) | R-15 to R-20 |

**Temperature rise during transport:**

ΔT = (U × A × t × ΔT_ambient) / (m × c_p)

Where:
- U = Overall heat transfer coefficient (0.15-0.25 Btu/hr·ft²·°F)
- A = Tank surface area (ft²)
- t = Transport time (hours)
- ΔT_ambient = Temperature difference between ambient and milk
- m = Milk mass (lb)
- c_p = Specific heat of milk (0.93 Btu/lb·°F)

For a 6,500-gallon tanker in 30°C ambient conditions traveling 2 hours:
- Expected temperature rise: 1-2°C
- Acceptable arrival temperature: ≤10°C (PMO Grade A requirement)
- Critical rejection temperature: >10°C sustained

### Unloading Equipment

**Sanitary pumps:**
- Type: Centrifugal or positive displacement (lobe, flexible impeller)
- Flow rate: 150-300 gpm (570-1,140 L/min) typical
- Discharge pressure: 30-50 psi (207-345 kPa)
- Materials: 316 stainless steel wetted parts
- Sanitary connections: Tri-clamp or DIN 11851
- Motor enclosure: TEFC (Totally Enclosed Fan Cooled), wash-down rated

**Flow measurement:**
- Magnetic flowmeters (preferred): ±0.25% accuracy
- Turbine meters: ±0.5% accuracy
- Coriolis meters (premium): ±0.1% accuracy, simultaneous density measurement
- Calibration frequency: Monthly verification, annual certified calibration

**Temperature monitoring:**
- RTD sensors (Pt100 or Pt1000): ±0.1°C accuracy, 3-wire configuration
- Installation: Sanitary thermowell with heat transfer compound
- Response time: T90 < 10 seconds in flowing milk
- Recording interval: Continuous with 15-second averaging

### Unloading Protocol

**Pre-acceptance verification:**

1. Visual inspection of tanker cleanliness
2. Seal integrity verification
3. Temperature measurement at multiple tank locations
4. Sample collection for rapid testing (smell, appearance, temperature)
5. Antibiotic screening (typically 5-7 minute rapid test)

**Unloading sequence:**

1. Connect sanitary hoses with proper tri-clamp seals
2. Verify CIP (Clean-In-Place) cycle completion on receiving lines
3. Open tanker outlet valve
4. Start receiving pump at controlled flow rate
5. Monitor inlet temperature continuously
6. Sample collection during unloading (composite sample)
7. Complete unloading and flush lines
8. Document volume, temperature, and acceptance data

**Unloading time:**
- Target rate: 200-250 gpm (760-950 L/min)
- 6,500-gallon tanker: 26-33 minutes
- Maximum rate limited by downstream cooling capacity

## Immediate Cooling Requirements

Raw milk must be cooled rapidly to inhibit bacterial growth and maintain quality. The FDA Pasteurized Milk Ordinance (PMO) establishes the regulatory framework.

### PMO Temperature Requirements

**Grade A raw milk for pasteurization:**

| Time from Production | Maximum Temperature | Cooling Requirement |
|----------------------|---------------------|---------------------|
| Within 2 hours of completion | Cool to 10°C (50°F) or less | Immediate cooling at farm |
| Upon arrival at plant | 10°C (50°F) or less | Verify before acceptance |
| Silo storage | 4.4°C (40°F) or less | Continuous refrigeration |
| Before processing | 7.2°C (45°F) or less | Maintained until pasteurization |

**Bacterial growth relationship to temperature:**

Psychrotrophic bacteria doubling time:
- At 7°C: 12-18 hours
- At 4°C: 24-48 hours
- At 2°C: 48-96 hours

Target storage temperature of 2-4°C significantly extends shelf life and maintains quality.

### Cooling System Design Philosophy

Two-stage cooling approach:

1. **Primary cooling (plate heat exchanger):** 10°C → 4°C using well water or chilled glycol
2. **Secondary cooling (silo tank refrigeration):** Maintain 2-4°C during storage

This staged approach optimizes energy efficiency and equipment sizing.

## Plate Cooler Design

Plate heat exchangers (PHE) provide the most efficient method for rapid milk cooling at the receiving stage.

### Plate Heat Exchanger Configuration

**Physical design:**
- Type: Gasketed plate and frame
- Plate material: 316 stainless steel
- Gasket material: EPDM (ethylene propylene diene monomer) or NBR (nitrile) food-grade
- Plate pattern: Herringbone or chevron corrugations
- Plate thickness: 0.5-0.7 mm
- Plate spacing: 2-5 mm typical

**Flow arrangement:**
- Configuration: Counterflow for maximum heat transfer efficiency
- Passes: Multiple pass design (2-4 passes per side typical)
- Pressure drop: 5-15 psi (35-100 kPa) per side
- Velocity: 0.3-0.6 m/s in milk channels

### Heat Transfer Calculations

Overall heat transfer coefficient for milk cooling:

U = 1 / (1/h_milk + t_plate/k_plate + 1/h_coolant + R_fouling)

Typical values:
- h_milk = 3,000-5,000 W/m²·K (convective heat transfer coefficient, milk side)
- h_coolant = 4,000-7,000 W/m²·K (water or glycol side)
- k_plate = 16 W/m·K (316 stainless steel)
- R_fouling = 0.0001-0.0002 m²·K/W (milk side fouling factor)

**Overall U value: 2,500-4,000 W/m²·K (440-705 Btu/hr·ft²·°F)**

### Cooling Duty Calculation

Heat removal required to cool milk from 10°C to 4°C:

Q = ṁ × c_p × ΔT

Where:
- ṁ = Mass flow rate of milk (kg/s)
- c_p = Specific heat of milk = 3.93 kJ/kg·K (0.94 Btu/lb·°F)
- ΔT = Temperature change = 6 K

**Example calculation for 200 gpm (757 L/min) milk flow:**

ṁ = 757 L/min × 1.032 kg/L ÷ 60 s/min = 13.0 kg/s

Q = 13.0 kg/s × 3.93 kJ/kg·K × 6 K = 306 kW (87.5 tons refrigeration)

### Plate Heat Exchanger Sizing

Required heat transfer area:

A = Q / (U × LMTD)

**Log Mean Temperature Difference (LMTD) for counterflow:**

LMTD = (ΔT₁ - ΔT₂) / ln(ΔT₁/ΔT₂)

For milk cooling from 10°C to 4°C using glycol at -1°C entering and 3°C leaving:

- ΔT₁ = 10°C - 3°C = 7°C (hot end)
- ΔT₂ = 4°C - (-1°C) = 5°C (cold end)

LMTD = (7 - 5) / ln(7/5) = 5.94 K

Required area:
A = 306,000 W / (3,000 W/m²·K × 5.94 K) = 17.2 m² (185 ft²)

**Typical plate sizes:**
- Small plates: 0.03-0.1 m² per plate
- Medium plates: 0.1-0.3 m² per plate
- Large plates: 0.3-0.6 m² per plate

For this application: approximately 60-170 plates depending on plate size selection.

### Coolant Flow Requirements

Glycol flow rate for balanced design:

ṁ_glycol = Q / (c_p,glycol × ΔT_glycol)

For 30% propylene glycol solution:
- c_p = 3.75 kJ/kg·K
- ΔT = 4 K (from -1°C to 3°C)

ṁ_glycol = 306 kW / (3.75 kJ/kg·K × 4 K) = 20.4 kg/s = 324 gpm

**Glycol-to-milk flow ratio: 1.6:1 (typical range 1.4:1 to 1.8:1)**

## Glycol System Requirements

Propylene glycol solutions provide non-toxic secondary coolant for food processing applications.

### Glycol Concentration Selection

| Glycol Concentration | Freeze Point | Specific Heat | Viscosity at 0°C | Application |
|---------------------|--------------|---------------|------------------|-------------|
| 20% by weight | -7°C (19°F) | 3.93 kJ/kg·K | 2.8 cP | Mild climate |
| 30% by weight | -13°C (9°F) | 3.75 kJ/kg·K | 4.2 cP | Standard dairy |
| 40% by weight | -21°C (-6°F) | 3.56 kJ/kg·K | 6.8 cP | Cold storage |

**Standard selection: 30% propylene glycol for -2°C to 4°C supply temperature**

### Glycol Chiller System

**Primary refrigeration system:**
- Refrigerant: Ammonia (R-717) in industrial installations, or R-404A/R-507 in smaller facilities
- Evaporator type: Flooded shell-and-tube or brazed plate
- Glycol supply temperature: -2°C to 0°C
- Glycol return temperature: 3°C to 5°C
- Temperature control: ±0.5°C stability required

**Glycol circulation:**
- Pump type: Centrifugal, bronze or stainless steel construction
- Flow rate: 1.2 × design flow (20% excess capacity)
- Pressure: 40-80 psi (275-550 kPa) discharge
- Variable frequency drive (VFD) control for load following

**Buffer tank:**
- Capacity: 15-30 minutes of cooling demand
- Insulation: 3-4 inches polyurethane foam (R-20 to R-25)
- Internal baffles to prevent stratification
- Level, temperature, and concentration monitoring

### Glycol System Heat Load

Total cooling load includes:
1. Milk sensible cooling: 306 kW (calculated above)
2. Pump heat addition: 1-2% of cooling load
3. Heat gain from piping: 3-5% of cooling load
4. Safety factor: 10-15%

**Total glycol chiller capacity: 345-390 kW (98-111 tons)**

### Glycol Distribution Network

**Supply piping:**
- Material: Schedule 40 carbon steel (black iron) or stainless steel
- Size: Based on 2-4 ft/s (0.6-1.2 m/s) velocity
- For 324 gpm: 4-inch nominal pipe size
- Insulation: 2-3 inches closed-cell elastomeric foam
- Vapor barrier: All-service jacket (ASJ) or PVC fitting covers

**Control valves:**
- Type: Modulating control valve at PHE glycol inlet
- Sizing: Cv based on pressure drop and flow requirements
- Actuation: Pneumatic or electric actuator with 4-20 mA control
- Fail position: Fail-open to protect equipment

**Temperature control strategy:**
- Primary: Modulate glycol flow to maintain milk outlet temperature
- Secondary: Stage chiller capacity based on glycol return temperature
- Alarm: High milk temperature at 6°C, critical at 7°C

## Silo Storage Tank Cooling

After plate cooling, milk enters insulated storage silos where it must be maintained at 2-4°C until processing.

### Silo Tank Design

**Construction:**
- Material: 304 or 316 stainless steel, sanitary finish (Ra ≤ 0.8 μm)
- Capacity: 10,000-100,000 gallons (38-380 m³) typical
- Orientation: Vertical cylindrical with dished heads
- Insulation: 3-4 inches polyurethane foam spray-applied
- Cladding: Aluminum or stainless steel weather protection

**Internal components:**
- Cooling coils or dimple jackets for refrigeration
- Agitator to prevent cream separation and maintain temperature uniformity
- CIP spray balls for automated cleaning
- Multiple temperature sensors at different heights

### Cooling Jacket Design

**Dimple jacket configuration (preferred for large tanks):**
- Pattern: Staggered or aligned dimple arrays
- Dimple depth: 0.5-1.0 inch (13-25 mm)
- Spacing: 2-4 inches (50-100 mm) center-to-center
- Coverage: 60-80% of cylindrical surface area
- Glycol channels created by spot-welded outer jacket

**Heat transfer through dimple jacket:**

U_jacket = 1 / (1/h_milk + t_wall/k_steel + 1/h_glycol + R_fouling)

Typical values:
- h_milk = 200-400 W/m²·K (with agitation)
- h_glycol = 1,000-2,000 W/m²·K (turbulent flow in dimples)
- t_wall = 3 mm (jacket and tank wall combined)
- k_steel = 16 W/m·K

**Overall U value: 150-300 W/m²·K (26-53 Btu/hr·ft²·°F)**

### Silo Cooling Load Calculation

**Heat gains to storage tank:**

1. **Incoming warm milk:**
   - Sensible load from 4°C to 2°C storage temperature
   - Intermittent load during receiving hours

2. **Heat of agitation:**
   Q_agitation = P_motor × η_mechanical × duty_cycle

   For 5 HP agitator operating 50% duty cycle:
   Q_agitation = 5 HP × 0.746 kW/HP × 0.50 = 1.87 kW

3. **Heat gain through insulation:**
   Q_insulation = U_overall × A_surface × (T_ambient - T_milk)

   For 50,000-gallon silo (D = 12 ft, H = 24 ft) with R-20 insulation at 20°C ambient:
   - A_surface ≈ 1,200 ft² (111 m²)
   - U_overall = 0.05 Btu/hr·ft²·°F (0.28 W/m²·K)
   - Q_insulation = 0.28 × 111 × (20-2) = 559 W

4. **Ambient heat gain through roof and connections:**
   - Estimate 10-20% additional heat gain
   - Q_ambient ≈ 60-110 W

**Continuous cooling requirement: 2.5-3.0 kW per 50,000-gallon silo**

### Glycol Flow for Silo Cooling

For steady-state cooling with 30% glycol solution:

ṁ_glycol = Q / (c_p × ΔT)

Using -2°C supply and 2°C return (ΔT = 4 K):

ṁ_glycol = 3,000 W / (3,750 J/kg·K × 4 K) = 0.20 kg/s = 3.2 gpm per tank

**Dimple jacket flow velocity:**
- Target: 2-4 ft/s (0.6-1.2 m/s) for good heat transfer
- Turbulent flow regime: Reynolds number > 4,000
- Distribution manifold design to ensure uniform flow across jacket

### Agitation System

**Purpose:**
- Prevent cream separation (fat stratification occurs within 2-4 hours without agitation)
- Maintain temperature uniformity throughout silo
- Ensure representative sampling

**Agitator specifications:**
- Type: Top-entering, close-clearance side-wall scraper or propeller
- Speed: 40-60 rpm typical
- Motor power: 3-10 HP depending on tank size
- Blade tip speed: 1.5-2.5 m/s
- Mixing time: Complete turnover in 15-20 minutes

**Agitation cycle:**
- Intermittent operation: 5-10 minutes per hour during storage
- Continuous operation: 30 minutes before and during tank-out
- Temperature-triggered: Activate if temperature gradient > 1°C detected

## Quality Testing Requirements

Comprehensive testing ensures milk meets safety and quality standards before acceptance and processing.

### Incoming Milk Testing

**Temperature verification:**
- Method: Calibrated digital thermometer or RTD sensor
- Locations: Multiple points in tanker (top, middle, bottom)
- Acceptance criteria: All readings ≤10°C
- Documentation: Record maximum temperature observed

**Organoleptic evaluation:**
- Visual appearance: No discoloration, foreign matter, or separation
- Odor: Fresh, sweet smell; no off-odors
- Preliminary enzyme tests: Phosphatase test for pasteurization verification

### Rapid Screening Tests

**Antibiotic residue testing:**
- Method: Enzyme-linked immunosorbent assay (ELISA) or receptor-based rapid tests
- Time: 5-7 minutes
- Target antibiotics: Beta-lactams, tetracyclines, sulfonamides, aminoglycosides
- Action level: Reject if any detectable residue above FDA tolerance

**Bacteria content (platform testing):**
- Method: Direct microscopic count or rapid ATP bioluminescence
- Standard Plate Count (SPC) requirement: <100,000 CFU/mL for Grade A
- Preliminary Incubation (PI) count: <200,000 CFU/mL
- Result time: 5-10 minutes (preliminary), 48 hours (confirmed plate count)

**Somatic cell count (SCC):**
- Method: Flow cytometry or viscosity-based rapid test
- Regulatory limit: <750,000 cells/mL (Grade A individual producer)
- Quality target: <400,000 cells/mL for premium milk
- Significance: Indicator of udder health and milk quality

### Laboratory Analysis

**Composition analysis:**
- Fat content: 3.0-4.5% typical (Babcock or infrared method)
- Protein content: 2.9-3.5% typical (Kjeldahl or infrared)
- Lactose: 4.5-5.0%
- Solids-not-fat (SNF): 8.5-9.0%
- Total solids: 11.5-13.5%

**Freezing point determination:**
- Normal range: -0.525°C to -0.535°C (Hortvet scale)
- Added water detection: Freezing point > -0.525°C indicates dilution
- Method: Thermistor cryoscope

**Microbiological testing (scheduled):**
- Standard Plate Count (SPC): Aerobic bacteria enumeration
- Coliform count: Sanitation indicator
- Psychrotrophic count: Cold-storage bacteria
- Thermoduric count: Heat-resistant bacteria (post-pasteurization concern)

### Continuous Monitoring

**Automated systems:**
- Inline temperature recording with 15-second intervals
- Flow rate and totalizer for volume verification
- Automatic sample collection during receiving (composite sampler)
- Data logging integrated with plant SCADA system

**Alarm conditions:**
- High temperature: >6°C in receiving line
- Low flow: Equipment malfunction indication
- High pressure differential: Filter or heat exchanger fouling
- Glycol system failure: Low supply temperature or flow

## PMO Temperature Compliance

The FDA Pasteurized Milk Ordinance (PMO) establishes comprehensive temperature control requirements throughout milk handling.

### Regulatory Framework

**PMO temperature standards (Grade A milk):**

| Stage | Temperature Requirement | Recording Requirement |
|-------|-------------------------|------------------------|
| Farm cooling | Cool to ≤10°C within 2 hours | Farm bulk tank chart recorder |
| Farm storage | Maintain ≤10°C | Continuous recording |
| Transport | Maintain ≤10°C | Tanker temperature device |
| Plant receiving | Verify ≤10°C at arrival | Manual reading and record |
| Plant storage | Cool to and maintain ≤7°C | Continuous recording, 15-min intervals |
| Before pasteurization | ≤7°C | Verified by chart recorder |

**Recording requirements:**
- Chart recorder or electronic data logger
- Accuracy: ±1°F (±0.6°C)
- Calibration: Monthly verification against certified thermometer
- Chart retention: Minimum 3 months
- Electronic records: Continuous data capture with backup

### Temperature Monitoring System Design

**Sensor placement:**
- Receiving line: Immediately post-pump
- Plate cooler outlet: Verify cooling performance
- Each silo tank: Minimum 2 sensors (top and bottom third)
- Glycol supply and return: Monitor cooling system performance

**Data acquisition:**
- PLC or SCADA-based system
- Sampling rate: 5-15 seconds
- Recording interval: 15 seconds to 1 minute
- Trending and alarm functions
- Network backup and remote access capability

**Calibration protocol:**
- Frequency: Monthly verification, quarterly certified calibration
- Method: Comparison to NIST-traceable reference thermometer
- Ice point verification: 0°C ± 0.2°C
- Adjustment: Recalibrate or replace sensors outside ±0.5°C tolerance

### Documentation and Record-Keeping

**Required records:**
- Individual tanker receiving logs (source, volume, temperature, test results)
- Continuous temperature charts or electronic records for all storage tanks
- Calibration records for all temperature measuring devices
- Quality test results and acceptance decisions
- Cleaning and sanitizing logs for all milk-contact surfaces

**Retention periods:**
- Temperature records: 3 months minimum (PMO), 6-12 months recommended
- Laboratory test results: 1 year minimum
- Calibration records: 2 years
- Regulatory inspection reports: Permanently

**Traceability:**
- Lot identification from source farm through finished product
- Electronic tracking systems integrate receiving data with production scheduling
- Rapid product recall capability based on receiving records

## Equipment Specifications

### Receiving Pumps

**Sanitary centrifugal pump (typical receiving duty):**

| Specification | Value |
|--------------|-------|
| Type | Centrifugal, single-stage |
| Flow rate | 200 gpm (757 L/min) at design point |
| Total head | 80-120 feet (24-37 m) |
| Motor power | 7.5-10 HP (5.6-7.5 kW) |
| Speed | 1,750 rpm (4-pole) or 3,500 rpm (2-pole) |
| Impeller material | 316 stainless steel, open or enclosed |
| Casing material | 316 stainless steel, sanitary design |
| Shaft seal | Mechanical seal, externally cooled |
| Connections | Tri-clamp, 3-inch inlet/outlet typical |
| Surface finish | 32 Ra or better on product-contact surfaces |
| CIP capability | Full drainability, 360° spray coverage |

**Positive displacement pump (alternative for long distance or high head):**
- Type: Rotary lobe or flexible impeller
- Flow: 150-200 gpm (567-757 L/min)
- Pressure: 50-100 psi (345-690 kPa)
- Advantages: Gentle product handling, self-priming
- Disadvantages: Higher cost, more maintenance

### Plate Heat Exchanger

**Gasketed PHE for milk cooling (200 gpm capacity):**

| Specification | Value |
|--------------|-------|
| Type | Gasketed plate and frame |
| Heat transfer area | 15-20 m² (160-215 ft²) |
| Number of plates | 60-100 depending on size |
| Plate material | 316 stainless steel, 0.6 mm thick |
| Gasket material | EPDM or NBR, food-grade |
| Design pressure | 150 psig (10.3 bar) per side |
| Design temperature | -10°C to 120°C |
| Port size | 3-inch NPT or tri-clamp |
| Milk-side pressure drop | 8-12 psi (55-83 kPa) |
| Glycol-side pressure drop | 10-15 psi (69-103 kPa) |
| Frame material | Carbon steel, painted or stainless |
| Mounting | Floor-mounted on stainless steel frame |
| CIP capability | Forward and reverse flow cleaning |

**Performance verification:**
- Milk outlet temperature: 4°C ± 0.5°C at design flow
- Approach temperature: 1-2°C (milk outlet to glycol inlet)
- Fouling factor: Monitor pressure drop increase over time
- Cleaning frequency: CIP every 4-8 hours of operation typical

### Glycol Chiller

**Ammonia/glycol chiller package (100-ton capacity):**

| Specification | Value |
|--------------|-------|
| Cooling capacity | 100 tons (352 kW) at -2°C glycol supply |
| Refrigerant | Ammonia (R-717) |
| Compressor type | Screw or reciprocating |
| Compressor capacity | 3-step or variable capacity control |
| Evaporator type | Flooded shell-and-tube |
| Evaporator material | Carbon steel shell, stainless tubes |
| Glycol flow rate | 240 gpm (909 L/min) at 10°F rise |
| Glycol concentration | 30% propylene glycol |
| Condenser type | Evaporative or air-cooled |
| Condensing temperature | 95-105°F (35-41°C) design |
| Control system | PLC-based with touch-screen HMI |
| Safety systems | High/low pressure cutouts, ammonia detectors |

**System protection:**
- Low glycol temperature cutout: -5°C to prevent freezing
- Flow switch: Proof of glycol circulation before compressor start
- Differential pressure switch: Tube-side fouling detection
- Emergency ventilation: Activated on ammonia detection

### Silo Storage Tanks

**Vertical silo tank (50,000-gallon capacity):**

| Specification | Value |
|--------------|-------|
| Capacity | 50,000 gallons (189 m³) |
| Diameter | 12 feet (3.7 m) |
| Height | 24 feet (7.3 m) overall |
| Material | 304 or 316 stainless steel |
| Shell thickness | 3/16 inch (4.8 mm) typical |
| Head type | Dished elliptical or hemispherical |
| Insulation | 4 inches polyurethane foam spray |
| Insulation R-value | R-25 to R-30 |
| Outer cladding | Aluminum or stainless steel, 0.032-0.040 inch |
| Cooling method | Dimple jacket with glycol circulation |
| Jacket coverage | 70-80% of cylindrical surface |
| Agitator | Top-entering, 5 HP, variable speed |
| CIP system | Rotating spray ball, 50-100 gpm at 40 psi |
| Instrumentation | 3× RTD sensors, level transmitter, pressure gauge |
| Connections | Multiple tri-clamp ports for inlet, outlet, CIP, sample |
| Vent | Sanitary vent filter with breather valve |

**Installation requirements:**
- Foundation: Reinforced concrete pad with anchor bolts
- Seismic restraint: Per local building code requirements
- Access platforms: For top-mounted equipment maintenance
- Leak containment: Secondary containment or sloped floor to drain

### Instrumentation and Controls

**Temperature measurement:**
- Sensor type: RTD (Pt100 or Pt1000), 3-wire or 4-wire
- Accuracy: Class A (±0.15°C at 0°C) or better
- Installation: Sanitary thermowell, tri-clamp mount
- Transmitter: 4-20 mA output, HART protocol

**Flow measurement:**
- Technology: Magnetic flowmeter (primary choice)
- Accuracy: ±0.25% of rate
- Repeatability: ±0.05% of rate
- Output: 4-20 mA + pulse output for totalizing
- Display: Local digital readout with totalizer

**Level measurement:**
- Technology: Guided wave radar or ultrasonic
- Accuracy: ±2 mm typical
- Range: 0-30 feet (0-9 m) typical for silos
- Output: 4-20 mA, HART protocol
- Safety: High level alarm and emergency shutoff

**Control system architecture:**
- PLC: Allen-Bradley, Siemens, or equivalent industrial PLC
- HMI: Touch-screen operator interface, 12-15 inch minimum
- Network: Ethernet/IP or Profinet communication
- Integration: SCADA system for plant-wide monitoring
- Alarm management: Prioritized alarms with escalation
- Data historian: Long-term storage and trending

## Cleaning and Sanitation

All milk-contact equipment requires rigorous cleaning and sanitizing between uses.

### CIP (Clean-In-Place) System

**CIP cycle for receiving system:**

1. Pre-rinse: Ambient water, 5-10 minutes, flush product residue
2. Caustic wash: 1-2% sodium hydroxide at 75-80°C, 10-15 minutes
3. Intermediate rinse: Ambient water, 5 minutes
4. Acid wash: 1-1.5% nitric acid at 60-70°C, 10 minutes (periodic)
5. Final rinse: Potable water until neutral pH and conductivity
6. Sanitize: Before use, typically peroxyacetic acid or hot water (88-93°C)

**CIP solution flow rates:**
- Minimum velocity: 5 ft/s (1.5 m/s) in piping
- PHE cleaning: Forward and reverse flow at design flow rate
- Tank spray devices: 0.5-1.0 gpm per inch of diameter at 30-50 psi

**Chemical concentration monitoring:**
- Conductivity for caustic concentration
- pH measurement for acid neutralization
- Sanitizer concentration test strips or inline sensors

This comprehensive receiving system design ensures regulatory compliance, product quality protection, and operational efficiency in dairy processing facilities.
