---
title: "Soft Drink Production"
aliases: ["Soft Drink Production"]
weight: 3
---

Soft drink production requires precise refrigeration control for carbonation, syrup preparation, and product quality maintenance. The refrigeration system must deliver consistent cooling across multiple process stages while maintaining strict temperature tolerances that directly affect CO2 solubility, flavor stability, and production efficiency.

## Process Cooling Requirements

Soft drink manufacturing involves three primary refrigeration loads:

**Syrup Preparation**
- Initial cooling of hot syrup from pasteurization (85-95°C) to storage temperature (4-10°C)
- Continuous cooling to maintain syrup at dispensing temperature
- Heat load from sugar dissolution and mixing operations

**Carbonation Water Chilling**
- Primary cooling requirement for maximizing CO2 absorption
- Target water temperature: 0.5-4°C for optimal carbonation
- Continuous process cooling under varying production rates

**Product Cooling**
- Final beverage temperature reduction post-mixing
- Packaging line temperature maintenance
- Quality assurance cooling for laboratory samples

## CO2 Solubility and Temperature Relationship

Carbon dioxide solubility in water follows Henry's Law, with temperature exerting dominant control over gas absorption capacity. The relationship is inversely proportional - lower temperatures dramatically increase CO2 solubility.

| Water Temperature (°C) | CO2 Solubility (g/L at 4 bar) | Relative Absorption | Carbonation Time |
|------------------------|--------------------------------|---------------------|------------------|
| 0 | 7.2 | 100% | Baseline |
| 2 | 6.8 | 94% | +8% |
| 4 | 6.4 | 89% | +15% |
| 6 | 6.0 | 83% | +24% |
| 8 | 5.6 | 78% | +35% |
| 10 | 5.3 | 74% | +48% |
| 12 | 5.0 | 69% | +63% |

**Temperature Control Criticality**
Each 1°C increase above optimal chilling temperature reduces CO2 absorption capacity by approximately 3%. For high-volume production lines operating at 1,000 bottles per minute, temperature variations of ±0.5°C can affect carbonation consistency across thousands of units per hour.

## Carbonation Water Chilling Systems

### Plate Heat Exchanger Configuration

The dominant cooling method for carbonation water uses brazed or gasketed plate heat exchangers operating with glycol or ammonia refrigerant.

**Design Parameters**
- Approach temperature: 1-2°C
- Water inlet temperature: 10-20°C (seasonal variation)
- Water outlet temperature: 0.5-4°C
- Glycol supply temperature: -3 to 0°C
- Heat exchanger effectiveness: 0.85-0.92

**Cooling Load Calculation**

Q = ṁ × cp × ΔT

Where:
- Q = cooling load (kW)
- ṁ = water mass flow rate (kg/s)
- cp = specific heat of water (4.18 kJ/kg·K)
- ΔT = temperature difference (K)

For a production line processing 10,000 L/h of carbonated water:
- Mass flow rate: 2.78 kg/s
- Temperature reduction: 15°C to 2°C (ΔT = 13 K)
- Cooling load: 2.78 × 4.18 × 13 = 151 kW

### Shell-and-Tube Chiller Systems

Large production facilities often employ shell-and-tube chillers for carbonation water, particularly when integrating with central ammonia refrigeration plants.

| System Capacity | Tube Configuration | Refrigerant | Water Flow Rate | Cooling Capacity |
|----------------|-------------------|-------------|-----------------|------------------|
| Small batch | Single pass | R-134a | 2,000 L/h | 30 kW |
| Medium line | Two pass | Ammonia | 10,000 L/h | 150 kW |
| Large production | Four pass | Ammonia | 50,000 L/h | 750 kW |
| Mega facility | Multi-shell | Ammonia | 200,000 L/h | 3,000 kW |

## Syrup Cooling Systems

Syrup cooling presents unique challenges due to high viscosity and sugar content affecting heat transfer characteristics.

**Syrup Physical Properties at 65°Brix**
- Density: 1,320 kg/m³
- Viscosity: 50-150 cP (temperature dependent)
- Specific heat: 2.8 kJ/kg·K
- Heat transfer coefficient: 60-75% of water

### Scraped Surface Heat Exchangers

High-viscosity syrups require mechanical enhancement of heat transfer through scraped surface exchangers.

**Operating Characteristics**
- Rotor speed: 100-400 rpm
- Product residence time: 30-120 seconds
- Heat transfer coefficient: 500-1,200 W/m²·K
- Temperature reduction: 85°C to 10°C in single pass

**Heat Load Components**
1. Sensible cooling from pasteurization temperature
2. Sugar dissolution heat (for in-line mixing systems)
3. Agitation heat input from mixing equipment
4. Ambient heat gain from piping and vessels

### Syrup Storage Tank Cooling

Post-process syrup storage requires continuous cooling to prevent microbial growth and maintain viscosity for accurate dispensing.

| Storage Volume | Cooling Method | Target Temperature | Insulation | Hold Time |
|----------------|----------------|-------------------|------------|-----------|
| 500 L | Jacket cooling | 4-8°C | 75 mm PU foam | 48 hours |
| 2,000 L | Internal coil | 6-10°C | 100 mm PU foam | 72 hours |
| 10,000 L | External PHE | 6-10°C | 150 mm PU foam | 7 days |
| 50,000 L | Recirculation loop | 8-12°C | 200 mm PU foam | 14 days |

## Carbonation Process Parameters

### Pressure-Temperature-Volume Relationships

Carbonation level is specified in volumes of CO2, where one volume equals the amount of CO2 gas (at 0°C and 1 atm) dissolved per unit volume of liquid.

**Typical Carbonation Levels by Product Type**

| Beverage Type | CO2 Volumes | Required Pressure (bar) | Water Temperature (°C) | Contact Time (min) |
|---------------|-------------|-------------------------|------------------------|-------------------|
| Still drinks | 0-0.5 | 1-2 | Not critical | N/A |
| Lightly carbonated | 1.5-2.5 | 2.5-3.5 | 4-6 | 3-5 |
| Standard cola | 3.5-4.0 | 4.0-4.5 | 2-4 | 4-6 |
| Sparkling water | 4.0-5.0 | 4.5-5.5 | 0.5-2 | 5-8 |
| High carbonation | 5.0-6.0 | 5.5-6.5 | 0.5-1.5 | 8-12 |

**Henry's Law Application**

C = kH × P

Where:
- C = CO2 concentration in liquid (mol/L)
- kH = Henry's constant (temperature dependent)
- P = partial pressure of CO2 (bar)

At 2°C, kH = 0.066 mol/(L·bar)
At 10°C, kH = 0.044 mol/(L·bar)

This 33% reduction in kH between 2°C and 10°C directly translates to reduced CO2 absorption capacity, requiring either higher pressures or longer contact times to achieve target carbonation levels.

## Refrigeration System Design

### Glycol Loop Configuration

Most modern soft drink facilities use secondary glycol loops for process cooling, providing temperature stability and eliminating direct ammonia contact with product.

**Glycol System Specifications**
- Glycol concentration: 30-35% propylene glycol
- Supply temperature: -3 to 0°C
- Return temperature: 3 to 8°C
- Temperature differential: 5-8 K
- Freezing protection: -15°C minimum
- System pressure: 3-5 bar

**Distribution Design**
- Main supply header: 150-300 mm diameter
- Branch circuits: 50-100 mm diameter
- Flow velocity: 1.0-2.0 m/s
- Pressure drop limit: 100 kPa total system
- Isolation valves at each process connection

### Chiller Plant Sizing

Total refrigeration capacity must account for all simultaneous cooling loads plus safety factors.

**Load Components**
1. Carbonation water chilling: 150-800 kW (primary load)
2. Syrup cooling: 50-200 kW
3. Product cooling: 30-150 kW
4. Cold storage rooms: 20-100 kW
5. Laboratory and QC: 5-20 kW
6. Distribution system losses: 10-15% of total

**Design Example for 20,000 L/h Production Facility**

| Load Category | Peak Load (kW) | Diversity Factor | Design Load (kW) |
|---------------|----------------|------------------|------------------|
| Carbonation water | 300 | 1.0 | 300 |
| Syrup cooling | 120 | 0.8 | 96 |
| Product cooling | 80 | 0.7 | 56 |
| Cold storage | 60 | 1.0 | 60 |
| Miscellaneous | 30 | 0.6 | 18 |
| **Subtotal** | **590** | - | **530** |
| Piping losses (12%) | - | - | 64 |
| **Total Design Capacity** | - | - | **594 kW** |
| Selected chiller | - | - | **650 kW** |

## Temperature Control and Monitoring

### Critical Control Points

Regulatory compliance and quality assurance require continuous monitoring of specific temperature points throughout production.

**Mandatory Monitoring Locations**
1. Carbonation water supply (±0.5°C tolerance)
2. Syrup storage tanks (±1.0°C tolerance)
3. Final product temperature (±1.0°C tolerance)
4. Glycol supply and return (±0.5°C tolerance)
5. CO2 storage area ambient (±2.0°C tolerance)

**Control System Architecture**
- PLC-based central control
- RTD sensors (Pt100, Class A accuracy)
- Analog output: 4-20 mA signals
- Data logging: 1-minute intervals
- Alarm thresholds: ±0.3°C from setpoint
- Response time: < 30 seconds to full correction

### Carbonation Quality Control

**CO2 Volume Measurement**
Direct measurement uses pressure-temperature relationships and corrects for water vapor pressure:

V = (P - Pw) / (Patm × kH(T))

Where:
- V = volumes of CO2
- P = total pressure in beverage (absolute)
- Pw = water vapor pressure at temperature T
- Patm = atmospheric pressure
- kH(T) = Henry's constant at temperature T

**Inline Monitoring Parameters**
- CO2 content: ±0.1 volumes accuracy
- Temperature: ±0.2°C accuracy
- Pressure: ±0.05 bar accuracy
- Flow rate: ±2% accuracy
- Sampling frequency: Continuous or per batch

## Energy Efficiency Optimization

### Heat Recovery Opportunities

Soft drink production generates significant waste heat that can offset refrigeration loads through heat recovery.

| Heat Source | Temperature | Recovery Potential | Application |
|-------------|-------------|-------------------|-------------|
| Syrup pasteurization | 85-95°C | 40-60 kW/1,000 L | Hot water preheat |
| Compressor heat rejection | 70-85°C | 30-45% of cooling load | CIP water heating |
| Bottle washer discharge | 60-75°C | 20-35 kW/1,000 L | Makeup water preheat |
| Air compressor cooling | 50-65°C | 15-25 kW/100 kW input | Space heating |

**Integrated Heat Recovery System**
A 20,000 L/h production facility can recover 150-250 kW of waste heat, reducing overall energy consumption by 15-25% compared to conventional systems without heat recovery.

### Variable Speed Drive Implementation

Carbonation water flow varies with production rate, making variable speed pumps and refrigeration compressors highly effective for energy savings.

**VFD Applications**
- Glycol circulation pumps: 30-50% energy reduction
- Chiller compressors: 20-40% energy reduction at partial load
- Cooling tower fans: 40-60% energy reduction
- Carbonation pumps: 25-35% energy reduction

Operating at 70% production capacity with VFD control typically reduces refrigeration energy consumption by 25-30% compared to constant-speed operation with capacity control.

## System Maintenance Requirements

**Weekly Tasks**
- Verify carbonation water temperature and CO2 levels
- Check glycol concentration and pH
- Inspect heat exchanger approach temperatures
- Monitor refrigerant charge indicators

**Monthly Tasks**
- Clean carbonation system filters
- Inspect syrup cooling coils for fouling
- Calibrate temperature sensors
- Test emergency shutdown systems

**Quarterly Tasks**
- Heat exchanger cleaning (CIP or disassembly)
- Glycol system water analysis
- Refrigerant leak detection survey
- Compressor oil analysis

**Annual Tasks**
- Complete refrigeration system inspection
- Heat exchanger pressure testing
- Control system calibration verification
- Thermal insulation condition assessment

Proper maintenance ensures carbonation consistency, prevents product quality issues, and maintains energy efficiency throughout the facility lifecycle.
