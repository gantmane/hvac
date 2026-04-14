---
title: "Syrup Preparation"
aliases: ["Syrup Preparation"]
description: "Refrigeration and temperature control requirements for soft drink syrup preparation, including dissolution, pasteurization, cooling, and storage processes with microbial control considerations."
weight: 1
---

## Process Overview

Syrup preparation represents the critical foundation of soft drink production, requiring precise temperature control across multiple process stages. The HVAC and refrigeration systems must maintain specific environmental conditions in the syrup room while providing process cooling for syrup production and storage.

The complete syrup preparation process encompasses ingredient mixing, thermal treatment for dissolution and pasteurization, rapid cooling, and temperature-controlled storage. Each stage demands specific refrigeration capacity and temperature control accuracy to ensure product quality, microbial safety, and process efficiency.

## Syrup Room Environmental Control

### Temperature Requirements

The syrup preparation room requires maintained environmental conditions independent of external weather and internal process heat loads.

| Space Type | Temperature | Relative Humidity | Air Changes/Hour |
|------------|-------------|-------------------|------------------|
| Mixing room | 18-22°C | 50-60% | 15-20 |
| Storage area | 15-20°C | 50-65% | 10-15 |
| CIP equipment room | 20-25°C | 40-60% | 12-18 |
| Control room | 22-24°C | 45-55% | 20-25 |

### Heat Load Calculations

Process equipment, lighting, personnel, and infiltration contribute to the total cooling load. For a typical 500 m² syrup preparation facility:

**Sensible Heat Gains:**

- Process equipment (mixing, pumps): 35-50 kW
- Lighting (LED, 15 W/m²): 7.5 kW
- Personnel (4 workers, 115 W sensible each): 0.46 kW
- Infiltration and envelope: 15-25 kW
- Motors and electrical equipment: 12-18 kW

**Total Sensible Load:** 70-101 kW

**Latent Heat Gains:**

- Personnel (4 workers, 55 W latent each): 0.22 kW
- Infiltration moisture load: 5-8 kW
- Process evaporation (open tanks): 3-6 kW

**Total Latent Load:** 8-14 kW

**Total Cooling Load:** 78-115 kW (22-33 tons refrigeration)

Safety factor of 1.15-1.25 recommended for equipment selection.

## Sugar Dissolution Process

### Dissolution Temperature Control

Sugar dissolution rate increases exponentially with temperature according to solubility relationships. The process typically operates in batch or continuous modes.

**Dissolution Kinetics:**

The rate of dissolution follows:

dm/dt = kA(Cs - C)

Where:
- dm/dt = dissolution rate (kg/s)
- k = mass transfer coefficient (m/s)
- A = crystal surface area (m²)
- Cs = saturation concentration (kg/m³)
- C = bulk solution concentration (kg/m³)

### Operating Temperature Ranges

| Syrup Type | Dissolution Temp | Time | Final Brix |
|------------|------------------|------|------------|
| Simple syrup | 60-70°C | 20-30 min | 60-65°Bx |
| High-test syrup | 75-85°C | 25-40 min | 70-75°Bx |
| Invert syrup | 85-95°C | 30-45 min | 68-72°Bx |

**Temperature Control Accuracy:** ±1°C for consistent dissolution and product quality.

### Heating System Requirements

Steam or hot water heating systems provide thermal energy for dissolution:

**Steam Heating:**
- Operating pressure: 2-4 bar gauge (135-160°C saturated)
- Heat transfer rate: 15,000-25,000 W/m² in jacketed vessels
- Condensate return system required

**Hot Water Heating:**
- Supply temperature: 90-95°C
- Return temperature: 70-75°C
- Flow rate: Sized for ΔT = 15-20°C
- Circulation rate: 0.5-0.8 L/s per 10 kW load

## Pasteurization Requirements

### Thermal Treatment Parameters

Pasteurization eliminates vegetative microorganisms while preserving flavor compounds and preventing sugar inversion. The process follows time-temperature relationships defined by decimal reduction time (D-value).

**Target Microorganisms:**

| Organism | D-value at 70°C | Z-value |
|----------|-----------------|---------|
| Saccharomyces cerevisiae | 0.5-1.0 min | 5-7°C |
| Lactobacillus species | 2.0-3.5 min | 8-10°C |
| Leuconostoc mesenteroides | 1.5-2.5 min | 6-9°C |

### Pasteurization Methods

**HTST (High Temperature Short Time):**
- Temperature: 85-95°C
- Holding time: 15-30 seconds
- Equipment: Plate heat exchanger
- Energy efficiency: Regeneration 85-90%

**Batch Pasteurization:**
- Temperature: 75-80°C
- Holding time: 15-20 minutes
- Equipment: Jacketed tank with agitation
- Energy efficiency: Lower than HTST

**Lethality Calculation:**

F₀ = ∫(10^((T-Tref)/z))dt

Where:
- F₀ = equivalent time at reference temperature (min)
- T = actual temperature (°C)
- Tref = reference temperature (typically 70°C)
- z = temperature coefficient (°C)
- t = time (min)

For adequate pasteurization: F₀ ≥ 5-10 minutes at 70°C reference.

## Post-Pasteurization Cooling

### Cooling Rate Requirements

Rapid cooling after pasteurization prevents sugar inversion, color development, and thermophilic organism growth. The cooling process must achieve target storage temperature within specific time limits.

**Cooling Performance Targets:**

| Initial Temp | Final Temp | Maximum Time | Cooling Rate |
|--------------|------------|--------------|--------------|
| 90°C | 10°C | 15 minutes | 5.3°C/min |
| 85°C | 8°C | 12 minutes | 6.4°C/min |
| 80°C | 6°C | 10 minutes | 7.4°C/min |

### Cooling System Design

**Plate Heat Exchanger Sizing:**

Heat transfer rate calculation:

Q = UA × LMTD

Where:
- Q = heat transfer rate (W)
- U = overall heat transfer coefficient (2500-3500 W/m²·K for syrup/water)
- A = heat transfer area (m²)
- LMTD = log mean temperature difference (K)

**Example Calculation:**

For cooling 5000 L/hr syrup from 90°C to 10°C:

Q = ṁ × cp × ΔT
Q = (5000 kg/hr × 1.25 kg/L) × 3.6 kJ/kg·K × (90-10)K
Q = 6250 kg/hr × 3.6 kJ/kg·K × 80K = 1,800,000 kJ/hr = 500 kW

With LMTD = 15K and U = 3000 W/m²·K:

A = Q/(U × LMTD) = 500,000/(3000 × 15) = 11.1 m²

Select PHE with 12-15 m² area with 20% margin.

### Chilled Water System

**Primary Cooling Medium:**
- Supply temperature: 2-4°C
- Return temperature: 8-12°C
- Flow rate: Calculated for ΔT = 6-8°C
- Pressure drop: 50-100 kPa across PHE

**Refrigeration Load:**

Peak cooling load = 500 kW = 142 tons refrigeration

Chiller capacity with safety factor: 170-180 tons

## Storage Temperature Requirements

### Temperature Control Parameters

Finished syrup storage maintains product stability, prevents microbial growth, and preserves flavor compounds. Storage temperature directly impacts shelf life and quality retention.

| Syrup Type | Storage Temp | Shelf Life | Quality Parameter |
|------------|--------------|------------|-------------------|
| Simple syrup | 4-8°C | 30-45 days | Color, clarity |
| High fructose | 8-12°C | 60-90 days | HMF formation |
| Flavor syrup | 4-6°C | 21-30 days | Volatile retention |
| Concentrate | 2-4°C | 90-120 days | Microbial stability |

### Storage Tank Cooling

**Jacketed Tank Design:**

Heat ingress through insulated walls and ambient temperature differential:

Q = U × A × ΔT

Where:
- U = overall heat transfer coefficient (0.2-0.3 W/m²·K with 100mm insulation)
- A = tank surface area (m²)
- ΔT = temperature difference between ambient and storage (K)

**Example:** 10,000 L tank (2.5m diameter × 2.0m height):

Surface area ≈ 23 m²

Q = 0.25 W/m²·K × 23 m² × (25-5)K = 115 W = 0.033 tons

**Glycol Cooling System:**
- Jacket supply: -2 to 0°C
- Jacket return: 2-4°C
- Propylene glycol 25-30% concentration
- Flow rate: 15-25 L/min per tank

## Microbial Control Through Refrigeration

### Temperature Control Limits

Refrigeration serves as the primary critical control point (CCP) for microbial safety in syrup storage. Temperature maintenance below 10°C inhibits most spoilage organisms.

**Microbial Growth Temperature Relationships:**

| Organism Category | Minimum Growth Temp | Optimal Temp | Generation Time at 5°C |
|-------------------|---------------------|--------------|------------------------|
| Psychrotrophs | -5 to 5°C | 20-30°C | 24-48 hours |
| Mesophiles | 5-15°C | 30-40°C | No growth |
| Osmophiles | 0-10°C | 25-35°C | 48-96 hours |
| Yeasts (Saccharomyces) | 0-5°C | 25-30°C | 36-72 hours |

### Critical Control Temperature

**Storage CCP Parameters:**
- Critical limit: 10°C maximum
- Operating target: 6-8°C
- Monitoring frequency: Continuous with alarm
- Corrective action: Immediate transfer if >10°C for >2 hours

**Temperature Monitoring:**
- RTD sensors: ±0.1°C accuracy
- Recording interval: 5-15 minutes
- Alarm setpoint: 9°C (warning), 11°C (critical)
- Backup power for refrigeration and monitoring

## Clean-In-Place (CIP) Temperature Requirements

### CIP Process Stages

CIP systems for syrup preparation equipment require specific temperature control at each cleaning stage to ensure sanitation effectiveness and energy efficiency.

| CIP Stage | Temperature | Duration | Purpose |
|-----------|-------------|----------|---------|
| Pre-rinse | 20-30°C | 5-10 min | Soil removal |
| Caustic wash | 75-85°C | 15-30 min | Organic removal |
| Intermediate rinse | 20-30°C | 5-10 min | Caustic removal |
| Acid wash | 60-70°C | 10-20 min | Mineral removal |
| Final rinse | 20-30°C | 5-10 min | Acid removal |
| Sanitizer | 20-30°C | 5-10 min | Microbial kill |

### Heating and Cooling Loads

**CIP Heating Requirements:**

For 2000 L caustic solution heated from 20°C to 80°C:

Q = m × cp × ΔT = 2000 kg × 4.0 kJ/kg·K × 60K = 480,000 kJ = 133 kWh

Heating time target: 20-30 minutes

Required heating capacity: 266-400 kW

**CIP Cooling Requirements:**

Post-caustic rinse cooling from 75°C to 25°C:

Q = 2000 kg × 4.18 kJ/kg·K × 50K = 418,000 kJ = 116 kWh

Cooling time target: 10-15 minutes

Required cooling capacity: 465-698 kW (132-199 tons)

### Water Temperature Control

**Hot Water System:**
- Storage temperature: 85-90°C
- Distribution temperature: 80-85°C
- Capacity: 5000-8000 L for typical facility
- Recovery rate: 1500-2500 L/hr

**Chilled Water System:**
- Supply temperature: 8-12°C for CIP cooling
- Separate from process chilled water (cross-contamination prevention)
- Flow rate: 100-200 L/min during cooling stage

## Refrigeration System Design

### System Architecture

Centralized chilled water plant serves multiple cooling loads with varying temperature and flow requirements. Glycol secondary loops provide sub-zero cooling for storage tanks.

**Primary Refrigeration System:**
- Chiller type: Water-cooled screw or centrifugal
- Refrigerant: R-134a, R-513A, or ammonia (large facilities)
- Capacity: 200-300 tons (multiple units for redundancy)
- Leaving chilled water temperature: 2-4°C
- Chilled water flow: 600-900 L/min

**Secondary Glycol System:**
- Heat exchanger: Plate type, glycol/chilled water
- Glycol concentration: 25-30% propylene glycol
- Supply temperature: -2 to 0°C
- Pump sizing: 150-250 L/min total flow

### Load Profile Analysis

**Typical Daily Load Profile:**

| Time Period | Process Load | CIP Load | Storage Load | Total Load |
|-------------|--------------|----------|--------------|------------|
| 00:00-06:00 | 20 tons | 0 tons | 15 tons | 35 tons |
| 06:00-12:00 | 85 tons | 40 tons | 15 tons | 140 tons |
| 12:00-18:00 | 95 tons | 50 tons | 15 tons | 160 tons |
| 18:00-24:00 | 60 tons | 30 tons | 15 tons | 105 tons |

Peak load: 160 tons (562 kW refrigeration)

Average load: 110 tons (387 kW refrigeration)

Load factor: 0.69

### Equipment Specifications

**Chiller Specifications:**

Two chillers in lead-lag configuration:

| Parameter | Lead Chiller | Lag Chiller |
|-----------|--------------|-------------|
| Capacity | 100 tons | 100 tons |
| Compressor | Screw, variable speed | Screw, fixed speed |
| Evaporator | Shell-and-tube | Shell-and-tube |
| EER | 15.0 BTU/W·h | 13.5 BTU/W·h |
| Power input | 28 kW at full load | 31 kW at full load |

**Cooling Tower:**
- Type: Induced draft, counter-flow
- Capacity: 2900 kW heat rejection at design
- Approach: 4-5°C
- Range: 6-8°C
- Fan power: 7.5 kW per cell (2 cells)

**Pumps:**

Primary chilled water pump:
- Flow: 650 L/min
- Head: 30 m
- Power: 11 kW
- VFD-controlled

Condenser water pump:
- Flow: 900 L/min
- Head: 25 m
- Power: 13 kW
- VFD-controlled

Glycol circulation pump:
- Flow: 200 L/min
- Head: 20 m
- Power: 5.5 kW
- Fixed speed

## Energy Efficiency Optimization

### Variable Load Management

The refrigeration system operates at partial load 65-75% of operating hours. Variable speed drives and staging strategies optimize efficiency across the load range.

**Part-Load Efficiency Strategies:**

- VFD on lead chiller compressor: 15-25% energy reduction at 50-75% load
- Condenser water reset: 8-12% energy reduction
- Chilled water supply temperature reset: 5-10% energy reduction when process allows
- Optimal chiller sequencing: 3-7% energy reduction

**Temperature Reset Control:**

Chilled water supply temperature reset based on load:

Tsupply = Tdesign + K × (1 - Load%)

Where:
- Tdesign = 2°C (design supply temperature)
- K = reset coefficient (0.03-0.05)
- Load% = current load / design load

At 60% load: Tsupply = 2 + 0.04 × (1 - 0.6) = 2 + 1.6 = 3.6°C

### Heat Recovery Opportunities

**Desuperheater Heat Recovery:**

Recovers compressor discharge superheat for CIP hot water heating:

Qrecovery = ṁref × (hdischarge - hsaturated)

For 100-ton chiller with R-134a:
- Discharge temperature: 75-85°C
- Saturated condensing temperature: 40-45°C
- Available superheat: 30-40°C
- Recovery potential: 35-50 kW (10-14% of refrigeration capacity)

Annual energy recovery: 150,000-220,000 kWh

**Hot Gas Heat Recovery:**

Full hot gas diversion for CIP water heating during off-peak refrigeration:

- Heating capacity: 450-500 kW per 100-ton chiller
- COP as heat pump: 4.0-4.5
- Displacement of gas/electric heating: 380,000-450,000 kWh annually

### Free Cooling Integration

Winter operation allows use of cooling tower water for direct cooling when outdoor wet-bulb temperature permits.

**Free Cooling Feasibility:**

Free cooling available when: Twb,outdoor + 5°C < Tchilled water required

For 6°C chilled water requirement: Twb < 1°C

In temperate climates: 1000-2000 hours annually

Energy savings: 25-40 kW × hours = 25,000-80,000 kWh annually

**Waterside Economizer Design:**

- Plate heat exchanger: Cooling tower water/chilled water
- Approach temperature: 3-4°C
- Control: Modulating based on outdoor wet-bulb
- Integration: Series with chiller evaporator

## Instrumentation and Control Integration

### Temperature Monitoring Points

Comprehensive temperature monitoring ensures process control and food safety compliance:

**Critical Monitoring Points:**
- Dissolution tank: 3 points (inlet, mid-level, outlet)
- Pasteurizer: Inlet, outlet, holding tube
- Cooling PHE: Syrup inlet/outlet, water inlet/outlet
- Storage tanks: 2 points per tank (top, bottom)
- Distribution headers: Supply, return
- Ambient room: 4 points per 100 m²

**Sensor Specifications:**
- Type: RTD Pt100 or Pt1000
- Accuracy: ±0.1°C (process), ±0.3°C (ambient)
- Response time: <10 seconds
- Signal: 4-20 mA or digital (Modbus, BACnet)

### Control System Architecture

**Distributed Control:**
- PLC-based process control for syrup preparation
- BMS integration for refrigeration plant and room HVAC
- SCADA for monitoring and data logging
- Recipe management for automated batching

**Control Strategies:**

Process cooling: Cascade control
- Primary: Syrup outlet temperature
- Secondary: Chilled water valve position
- Feedforward: Syrup flow rate

Chiller plant: Demand-based reset
- Chilled water temperature reset based on valve positions
- Chiller staging based on load
- Pump speed modulation for flow optimization

## Reliability and Redundancy

### System Redundancy Requirements

Food safety and production continuity require redundancy for critical refrigeration components:

**N+1 Configuration:**
- Chillers: 2 × 100 tons (200 ton total for 160 ton peak)
- Pumps: Duty + standby for each circuit
- Cooling tower cells: 2 cells minimum
- Controls: Dual network paths

**Backup Power:**
- Emergency generator: 250-300 kW for refrigeration essentials
- UPS: 20-30 kVA for controls and monitoring
- Automatic transfer switch: <10 second transfer time

### Maintenance Accessibility

Equipment layout facilitates preventive maintenance without production shutdown:

- Isolation valves on all major components
- Swing connections for pump maintenance
- Removable bundle chillers preferred
- Access space: 1.5 m minimum around equipment

**Preventive Maintenance Schedule:**

| Component | Frequency | Duration |
|-----------|-----------|----------|
| Chiller maintenance | Annual | 16-24 hours |
| Cooling tower cleaning | Quarterly | 4-6 hours |
| PHE inspection/cleaning | Semi-annual | 8-12 hours |
| Glycol testing/replacement | Annual | 4-6 hours |
| Pump seal replacement | 2-3 years | 4-8 hours |

## Compliance and Documentation

### Food Safety Requirements

HVAC and refrigeration systems supporting syrup preparation must comply with food safety regulations and industry standards.

**Applicable Standards:**
- FDA 21 CFR Part 117: Current Good Manufacturing Practice
- FSMA: Preventive Controls for Human Food
- GFSI standards: SQF, BRC, FSSC 22000
- 3-A Sanitary Standards for equipment

**Documentation Requirements:**
- Temperature monitoring records: Continuous with 3-year retention
- CIP cycle records: Each cycle with validation data
- Preventive maintenance: Logs with completion verification
- Deviation reports: Root cause and corrective action
- Annual system validation: Temperature mapping and verification

### Commissioning and Validation

**Factory Acceptance Testing (FAT):**
- Chiller performance verification at design conditions
- Control system functional testing
- Instrumentation calibration

**Site Acceptance Testing (SAT):**
- Refrigeration capacity verification at actual conditions
- Temperature distribution uniformity testing
- Worst-case challenge testing for CCP verification
- Emergency response testing (power loss, equipment failure)

**Ongoing Validation:**
- Annual temperature mapping: 24-48 hour continuous monitoring
- Quarterly CCP verification: Accuracy and alarm function
- Biannual hygiene inspection: Equipment condition and cleanliness

---

*This technical content provides HVAC design guidance for soft drink syrup preparation facilities. Actual system design must account for site-specific conditions, production capacity, regulatory requirements, and manufacturer specifications. Consult with qualified refrigeration engineers and food safety professionals for project-specific applications.*