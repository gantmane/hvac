---
title: "Mix Preparation"
description: "Ice cream mix preparation thermal processes including pasteurization, homogenization, cooling systems, aging requirements, equipment heat loads, and process room HVAC design for commercial ice cream manufacturing"
weight: 1
---

## Process Overview

Ice cream mix preparation encompasses ingredient blending, thermal processing, homogenization, and aging. The process requires precise temperature control at multiple stages, generates substantial heat loads requiring refrigeration, and operates in controlled environmental conditions to maintain product quality and food safety compliance.

**Sequential Process Steps:**

1. Ingredient batching and blending (15-40°C)
2. Pasteurization (69-80°C)
3. Homogenization (65-77°C)
4. Cooling (40°C to 4°C)
5. Aging/maturation (2-4°C for 4-24 hours)

## Mix Composition

The ice cream mix formulation determines thermal properties affecting heat transfer calculations and refrigeration load requirements.

### Standard Formulation Ranges

| Component | Percentage Range | Function | Thermal Impact |
|-----------|------------------|----------|----------------|
| Milk Solids Non-Fat (MSNF) | 10-11% | Body, texture | Increases specific heat |
| Milk Fat | 10-16% (premium 14-18%) | Richness, mouthfeel | Reduces specific heat |
| Sucrose/Sweeteners | 12-16% | Sweetness, freezing point depression | Lowers freezing point |
| Corn Syrup Solids | 0-5% | Texture, sweetness | Affects viscosity |
| Stabilizers | 0.1-0.5% | Prevents ice crystal growth | Minimal thermal effect |
| Emulsifiers | 0.1-0.2% | Fat dispersion, whipping | Minimal thermal effect |
| Total Solids | 36-42% | Overall composition | Determines thermal properties |

### Mix Thermal Properties

The thermal properties of ice cream mix vary with composition and temperature.

**Specific Heat Capacity:**

For ice cream mix above freezing:

$$c_p = 4.187 - 2.093 \times X_s$$

Where:
- $c_p$ = specific heat (kJ/kg·°C)
- $X_s$ = mass fraction of total solids (decimal)

For typical mix (40% total solids):
$$c_p = 4.187 - 2.093 \times 0.40 = 3.35 \text{ kJ/kg·°C}$$

**Density:**

Mix density typically ranges 1,080-1,100 kg/m³ at 4°C, varying with fat content and temperature.

## Ingredient Blending

### Blending Temperature Control

Initial ingredient blending occurs at controlled temperatures to facilitate dissolution and prevent premature reactions.

| Blending Stage | Temperature | Purpose | HVAC Consideration |
|----------------|-------------|---------|-------------------|
| Dry ingredient mixing | 15-20°C | Uniform distribution | Ambient control |
| Liquid addition | 35-40°C | Dissolve sugar, hydrate proteins | Hot water demand |
| Final blending | 40-50°C | Complete dissolution | Maintain temperature |

### Blending Equipment Heat Generation

**Mixer Power Requirements:**

High-shear mixers generate heat through mechanical energy dissipation:

$$Q_{mixer} = P_{motor} \times \eta_{mechanical} \times t$$

Where:
- $Q_{mixer}$ = heat generated (kJ)
- $P_{motor}$ = motor power (kW)
- $\eta_{mechanical}$ = mechanical efficiency (0.85-0.95)
- $t$ = mixing time (s)

For a 500 L batch mixer with 15 kW motor operating 20 minutes:
$$Q_{mixer} = 15 \times 0.90 \times 1,200 = 16,200 \text{ kJ}$$

This raises mix temperature approximately:
$$\Delta T = \frac{Q}{m \times c_p} = \frac{16,200}{540 \times 3.35} = 9.0°C$$

## Pasteurization Systems

Pasteurization eliminates pathogenic microorganisms and ensures food safety compliance. Two primary methods are employed.

### High-Temperature Short-Time (HTST) Pasteurization

**Process Parameters:**

| Parameter | Value | Tolerance | Regulatory Requirement |
|-----------|-------|-----------|------------------------|
| Temperature | 79-80°C | ±0.5°C | PMO minimum 79.4°C (175°F) |
| Holding time | 25 seconds | ±2 seconds | Minimum 25 seconds |
| Flow rate | Controlled | ±5% | Maintains residence time |
| Recording | Continuous | 1-second intervals | PMO requirement |

**Heat Load Calculation:**

For continuous HTST pasteurization:

$$Q_{pasteurization} = \dot{m} \times c_p \times (T_{pasteurization} - T_{blending})$$

For 5,000 L/hr (1,500 kg/hr) throughput:
$$Q_{pasteurization} = 1,500 \times 3.35 \times (80 - 45) = 176,138 \text{ kJ/hr} = 48.9 \text{ kW}$$

**Steam Requirements:**

Using steam at 150 kPa (127°C), with condensate return:

$$\dot{m}_{steam} = \frac{Q_{pasteurization}}{h_{fg} \times \eta_{HX}}$$

With $h_{fg}$ = 2,216 kJ/kg (at 150 kPa) and heat exchanger efficiency 85%:

$$\dot{m}_{steam} = \frac{176,138}{2,216 \times 0.85} = 93.5 \text{ kg/hr}$$

### Batch Pasteurization (VAT Method)

**Process Parameters:**

| Parameter | Value | Application | Energy Consideration |
|-----------|-------|-------------|---------------------|
| Temperature | 68-69°C | Small operations | Longer heating time |
| Holding time | 30 minutes | At temperature | Heat loss compensation |
| Heating rate | 1-2°C/min | Controlled | Prevents scorching |
| Cooling rate | Variable | To homogenization temp | Energy recovery opportunity |

**Batch Heat Load:**

For 1,000 L batch:

$$Q_{batch} = m \times c_p \times \Delta T + Q_{losses}$$

Where $Q_{losses}$ accounts for tank heat loss during heating and holding:

$$Q_{batch} = 1,080 \times 3.35 \times (69 - 20) + (U \times A \times \Delta T_{avg} \times t)$$

Assuming insulated tank (U = 0.5 W/m²·°C, A = 8 m², holding 30 min):
$$Q_{losses} = 0.5 \times 8 \times 25 \times 1,800 = 180,000 \text{ J} = 180 \text{ kJ}$$

$$Q_{batch} = 177,282 + 180 = 177,462 \text{ kJ}$$

### Pasteurization Heat Exchanger Types

**Plate Heat Exchanger (PHE) Configuration:**

HTST systems typically use PHE with multiple sections:

1. Regeneration section: Preheats incoming mix using hot pasteurized mix (efficiency 75-85%)
2. Heating section: Steam or hot water brings mix to pasteurization temperature
3. Holding tube: Maintains temperature for required time
4. Cooling section: Chilled water or glycol reduces temperature

**Regeneration Energy Savings:**

With 80% regeneration efficiency:

$$Q_{heating,net} = Q_{total} \times (1 - \eta_{regen})$$

$$Q_{heating,net} = 176,138 \times (1 - 0.80) = 35,228 \text{ kJ/hr} = 9.8 \text{ kW}$$

Energy savings: 80% reduction in heating and cooling loads.

## Homogenization

Homogenization reduces fat globule size (0.2-2.0 μm) to create stable emulsion, improve texture, and prevent creaming.

### Homogenization Parameters

| Parameter | Single-Stage | Two-Stage | Purpose |
|-----------|--------------|-----------|---------|
| First stage pressure | 2,000-2,500 psi (13.8-17.2 MPa) | 2,000-2,500 psi | Fat globule reduction |
| Second stage pressure | N/A | 500-1,000 psi (3.4-6.9 MPa) | Prevent clustering |
| Temperature | 65-77°C | 65-77°C | Maintain fluidity |
| Fat content correlation | Higher fat = lower pressure | Higher fat = lower pressure | Prevent over-processing |

### Temperature Requirements

Homogenization must occur at elevated temperature to ensure:

- Fat remains liquid (milk fat melting point ~40°C)
- Reduced viscosity for efficient processing
- Prevention of fat crystallization in homogenizer

**Temperature Control Strategy:**

If pasteurization at 80°C and homogenization at 70°C:

$$Q_{cooling,pre-homog} = \dot{m} \times c_p \times (T_{past} - T_{homog})$$

$$Q_{cooling,pre-homog} = 1,500 \times 3.35 \times (80 - 70) = 50,250 \text{ kJ/hr} = 14.0 \text{ kW}$$

### Homogenizer Heat Generation

High-pressure homogenization adds significant heat to the product.

**Temperature Rise Calculation:**

$$\Delta T_{homog} = \frac{P_{homog}}{\rho \times c_p \times \eta_{pump}}$$

For single-stage at 2,500 psi (17.2 MPa):

$$\Delta T_{homog} = \frac{17,200}{1,080 \times 3.35 \times 0.90} = 5.3°C$$

For two-stage (2,500 + 500 psi):

$$\Delta T_{total} = \frac{20,700}{1,080 \times 3.35 \times 0.90} = 6.4°C$$

**Impact on Process:**

If mix enters homogenizer at 70°C, it exits at approximately 76°C, requiring additional cooling before aging.

### Homogenizer Power Requirements

**Hydraulic Power:**

$$P_{hydraulic} = \frac{\dot{Q} \times \Delta P}{\eta_{pump}}$$

Where:
- $\dot{Q}$ = volumetric flow rate (m³/s)
- $\Delta P$ = pressure increase (Pa)
- $\eta_{pump}$ = pump efficiency (0.85-0.92)

For 5,000 L/hr at 20.7 MPa total pressure:

$$P_{hydraulic} = \frac{0.00139 \times 20,700,000}{0.90} = 31.9 \text{ kW}$$

Motor power (accounting for mechanical losses): 35-40 kW.

## Cooling Systems

Post-homogenization cooling reduces mix temperature from 70-76°C to aging temperature (2-4°C).

### Cooling Load Calculation

**Total Cooling Requirement:**

$$Q_{cooling} = \dot{m} \times c_p \times (T_{homog} - T_{aging}) + Q_{homog,heat}$$

For 1,500 kg/hr throughput:

$$Q_{cooling} = 1,500 \times 3.35 \times (76 - 3) = 367,088 \text{ kJ/hr} = 102.0 \text{ kW}$$

**Staged Cooling Approach:**

| Cooling Stage | Temperature Range | Cooling Medium | Heat Removal |
|---------------|-------------------|----------------|--------------|
| Pre-cooling | 76°C → 40°C | Chilled water (10-15°C) | 181 kJ/kg |
| Primary cooling | 40°C → 15°C | Glycol (5-8°C) | 84 kJ/kg |
| Final cooling | 15°C → 3°C | Glycol (-2 to 2°C) | 40 kJ/kg |

### Cooling Equipment

**Plate Heat Exchanger Sizing:**

$$Q = U \times A \times LMTD$$

Where LMTD (Log Mean Temperature Difference):

$$LMTD = \frac{(T_{h,in} - T_{c,out}) - (T_{h,out} - T_{c,in})}{\ln\left(\frac{T_{h,in} - T_{c,out}}{T_{h,out} - T_{c,in}}\right)}$$

For final cooling (15°C → 3°C with glycol at -1°C → 5°C):

$$LMTD = \frac{(15 - 5) - (3 - (-1))}{\ln\left(\frac{15 - 5}{3 - (-1)}\right)} = \frac{10 - 4}{\ln(2.5)} = 6.6°C$$

With overall heat transfer coefficient U = 2,500 W/m²·°C:

$$A = \frac{Q}{U \times LMTD} = \frac{16,667}{2,500 \times 6.6} = 1.01 \text{ m}^2$$

### Refrigeration System Requirements

**Compressor Capacity:**

Total refrigeration load includes:

- Mix cooling: 102 kW
- Heat infiltration: 5-10% of cooling load
- Safety factor: 10-15%

$$Q_{refrigeration} = 102 \times 1.10 \times 1.15 = 129 \text{ kW (36.7 tons)}$$

**Glycol System Specifications:**

| Parameter | Value | Notes |
|-----------|-------|-------|
| Glycol concentration | 30-40% propylene glycol | Food-grade |
| Supply temperature | -2 to 2°C | Prevents freezing |
| Return temperature | 5-8°C | Temperature rise |
| Flow rate | 80-100 L/min | Based on ΔT = 5°C |
| Pump pressure | 200-350 kPa | Overcomes PHE resistance |

## Aging and Maturation

Aging at 2-4°C for 4-24 hours allows:

- Fat crystallization (forms membrane around air cells)
- Protein hydration (improves body and texture)
- Stabilizer hydration (increases viscosity)
- Flavor development (ingredient equilibration)

### Aging Tank Requirements

**Tank Capacity Calculation:**

For continuous operation with 12-hour aging:

$$V_{tank} = \dot{Q} \times t_{aging}$$

For 5,000 L/hr production:

$$V_{tank} = 5,000 \times 12 = 60,000 \text{ L minimum}$$

Typical design: Three 25,000 L tanks for operational flexibility.

### Aging Refrigeration Load

**Heat Removal Requirements:**

1. Initial cooling (if entering above aging temperature)
2. Metabolic heat from minor microbial activity (minimal after pasteurization)
3. Heat infiltration through tank walls
4. Agitation heat (gentle stirring 1-2 RPM)

**Tank Heat Infiltration:**

$$Q_{infiltration} = U \times A \times (T_{ambient} - T_{product})$$

For 25,000 L tank (2.9 m diameter × 3.8 m height), insulated with 100 mm polyurethane (U = 0.25 W/m²·°C):

$$A = \pi D H + 2 \times \frac{\pi D^2}{4} = \pi \times 2.9 \times 3.8 + 2 \times \frac{\pi \times 2.9^2}{4} = 47.9 \text{ m}^2$$

$$Q_{infiltration} = 0.25 \times 47.9 \times (20 - 3) = 204 \text{ W} = 0.204 \text{ kW}$$

**Agitation Heat:**

Low-speed agitation (1 kW motor):

$$Q_{agitation} = P_{motor} \times \eta = 1.0 \times 0.85 = 0.85 \text{ kW}$$

**Total per tank:**

$$Q_{total} = 0.204 + 0.85 = 1.05 \text{ kW}$$

For three tanks: 3.15 kW continuous refrigeration load.

### Aging Tank Jacketed Cooling

**Jacket Design:**

| Parameter | Specification | Purpose |
|-----------|---------------|---------|
| Jacket coverage | Full sidewall, partial bottom | Uniform temperature |
| Glycol supply | -2°C | Below product temperature |
| Glycol flow | Turbulent (Re > 10,000) | High heat transfer coefficient |
| Jacket thickness | 50-75 mm | Flow distribution |

**Heat Transfer Coefficient:**

Overall U-value for jacketed tank: 200-400 W/m²·°C depending on agitation and glycol velocity.

## Clean-In-Place (CIP) Systems

Automated cleaning maintains sanitary conditions without equipment disassembly.

### CIP Temperature Requirements

| CIP Stage | Temperature | Duration | Purpose |
|-----------|-------------|----------|---------|
| Pre-rinse | Ambient (15-25°C) | 3-5 minutes | Remove gross soil |
| Caustic wash | 75-85°C | 10-20 minutes | Fat and protein removal |
| Intermediate rinse | Ambient | 3-5 minutes | Remove caustic |
| Acid wash | 65-75°C | 10-15 minutes | Mineral deposit removal |
| Final rinse | Ambient | 3-5 minutes | Remove acid residue |
| Sanitizer | 25-35°C | 5-10 minutes | Microbial reduction |

### CIP Heat Load

**Hot Water/Chemical Heating:**

For 500 L CIP solution heated from 20°C to 80°C:

$$Q_{CIP} = m \times c_p \times \Delta T = 500 \times 4.18 \times (80 - 20) = 125,400 \text{ kJ}$$

Heating time 10 minutes:

$$P_{CIP,heater} = \frac{125,400}{600} = 209 \text{ kW}$$

**Daily CIP Energy:**

Two CIP cycles per day:

$$E_{CIP,daily} = 2 \times 125,400 = 250,800 \text{ kJ/day} = 69.7 \text{ kWh/day}$$

### CIP Steam Demand

Using direct steam injection:

$$\dot{m}_{steam,CIP} = \frac{Q_{CIP}}{h_{fg}} = \frac{125,400}{2,216} = 56.6 \text{ kg per cycle}$$

## Process Room HVAC Design

Mix preparation areas require controlled environmental conditions for product quality, food safety, and worker comfort.

### Design Conditions

| Parameter | Requirement | Rationale | Standard Reference |
|-----------|-------------|-----------|-------------------|
| Temperature | 15-20°C | Prevent equipment overheating, product stability | ASHRAE, PMO |
| Relative humidity | 50-60% | Condensation prevention, microbial control | ASHRAE |
| Air changes | 15-20 ACH | Humidity and heat removal | ASHRAE |
| Pressurization | Positive (+5 to +15 Pa) | Prevent contamination ingress | FDA, PMO |
| Filtration | MERV 13 minimum | Particulate control | ASHRAE 62.1 |

### Process Room Heat Load

**Equipment Heat Gains:**

| Equipment | Quantity | Power (kW) | Duty Cycle | Heat Gain (kW) |
|-----------|----------|------------|------------|----------------|
| Mixers | 2 | 15 | 70% | 21.0 |
| Pumps | 4 | 5 | 80% | 16.0 |
| Homogenizers | 1 | 40 | 90% | 36.0 |
| Conveyors | 2 | 3 | 60% | 3.6 |
| Controls/instrumentation | - | - | 100% | 5.0 |
| Lighting (LED) | - | - | 100% | 8.0 |

**Total equipment gain:** 89.6 kW

**Personnel Heat Gain:**

8 workers, light activity (150 W sensible + 200 W latent each):

$$Q_{personnel} = 8 \times (150 + 200) = 2,800 \text{ W} = 2.8 \text{ kW}$$

**Building Envelope Gains:**

For 500 m² process room with moderate insulation (U = 0.35 W/m²·°C), outdoor temperature 30°C:

$$Q_{envelope} = U \times A \times \Delta T = 0.35 \times 500 \times (30 - 18) = 2,100 \text{ W} = 2.1 \text{ kW}$$

**Total Sensible Heat Load:**

$$Q_{sensible,total} = 89.6 + 2.8 + 2.1 = 94.5 \text{ kW}$$

**Latent Heat Load:**

- Personnel: 8 × 200 W = 1.6 kW
- Process equipment evaporation: minimal when covered
- Outside air ventilation: 15 cfm/person × 8 = 120 cfm

Ventilation latent load (humid climate, outdoor 30°C/80% RH to 18°C/55% RH):

$$Q_{latent,vent} = \dot{V} \times \rho \times \Delta \omega \times h_{fg}$$

Where $\Delta \omega$ = humidity ratio difference ≈ 0.0085 kg/kg:

$$Q_{latent,vent} = 0.057 \times 1.2 \times 0.0085 \times 2,500 = 1.5 \text{ kW}$$

**Total latent:** 3.1 kW

### HVAC System Sizing

**Total Cooling Capacity:**

$$Q_{HVAC} = Q_{sensible} + Q_{latent} = 94.5 + 3.1 = 97.6 \text{ kW (27.8 tons)}$$

With safety factor (15%):

$$Q_{design} = 97.6 \times 1.15 = 112.2 \text{ kW (31.9 tons)}$$

**Ventilation Requirements:**

Minimum outdoor air: 15 cfm/person × 8 = 120 cfm = 204 m³/hr

Supply air for 20 ACH (500 m² × 4 m ceiling = 2,000 m³):

$$\dot{V}_{supply} = 2,000 \times 20 = 40,000 \text{ m}^3\text{/hr} = 23,530 \text{ cfm}$$

**Supply Air Temperature:**

$$T_{supply} = T_{room} - \frac{Q_{sensible}}{\dot{m} \times c_p}$$

$$T_{supply} = 18 - \frac{94,500}{(40,000/3,600) \times 1.2 \times 1.005} = 18 - 7.8 = 10.2°C$$

### Dehumidification Requirements

Process rooms generating moisture require active dehumidification.

**Moisture Removal Rate:**

$$\dot{m}_{moisture} = \frac{Q_{latent}}{h_{fg}} = \frac{3,100}{2,500} = 1.24 \text{ kg/hr}$$

**Chilled Water System:**

Supply temperature: 4-7°C (below dew point for effective moisture removal)

Return temperature: 12-14°C

Flow rate based on sensible cooling:

$$\dot{V}_{CHW} = \frac{Q_{sensible}}{c_p \times \rho \times \Delta T} = \frac{94,500}{4.18 \times 1,000 \times (12-6)} = 3.77 \text{ L/s} = 13.6 \text{ m}^3\text{/hr}$$

## Equipment Specifications

### Batch Mixing System

| Component | Specification | Notes |
|-----------|---------------|-------|
| Tank capacity | 1,000-2,000 L | Batch size dependent |
| Material | 316L stainless steel | Food-grade, corrosion resistant |
| Insulation | 100 mm polyurethane | U ≤ 0.35 W/m²·°C |
| Jacket | Full sidewall | Heating/cooling capability |
| Agitator | Variable speed, 10-100 RPM | High shear or anchor blade |
| Motor | 7.5-15 kW | Torque requirements |
| Temperature control | ±1°C | PID control with PT100 sensors |

### HTST Pasteurizer

| Component | Specification | Capacity |
|-----------|---------------|----------|
| Plate heat exchanger | 316 stainless, FDA approved | 5,000-10,000 L/hr |
| Regeneration efficiency | 75-85% | Energy recovery |
| Holding tube | Time/temperature validated | 25-second minimum |
| Recording devices | Chart recorder or SCADA | PMO compliance |
| Flow diversion valve | Automatic fail-safe | Returns unpasteurized product |
| Booster pump | 3-5 bar discharge | Maintains positive pressure |

### Homogenizer

| Component | Specification | Performance |
|-----------|---------------|-------------|
| Type | Two-stage, positive displacement | 2,000-10,000 L/hr |
| First stage pressure | 2,000-2,500 psi (13.8-17.2 MPa) | Adjustable |
| Second stage pressure | 500-1,000 psi (3.4-6.9 MPa) | Adjustable |
| Motor power | 30-50 kW | Flow rate dependent |
| Material | 316 stainless steel | Sanitary design |
| Temperature control | Jacket cooling optional | Compensate for heat rise |

### Aging Tanks

| Component | Specification | Purpose |
|-----------|---------------|---------|
| Capacity | 10,000-30,000 L each | Production volume |
| Material | 316L stainless steel | Food contact |
| Insulation | 100-150 mm polyurethane | Minimize heat gain |
| Jacket | Full sidewall coverage | Glycol cooling |
| Agitator | 1-2 RPM | Gentle mixing |
| Temperature monitoring | Multiple PT100 sensors | Uniform verification |
| Level indication | Ultrasonic or radar | Inventory tracking |

## Energy Optimization Strategies

### Heat Recovery

**Regeneration Section:**

Plate heat exchangers recover 75-85% of pasteurization heat, reducing heating and cooling loads proportionally.

Annual energy savings (5,000 L/hr, 16 hr/day, 300 days/year):

$$E_{saved} = Q_{regenerated} \times t_{annual}$$

$$E_{saved} = (176,138 \times 0.80) \times 16 \times 300 = 676 \text{ million kJ/year} = 187,778 \text{ kWh/year}$$

At $0.08/kWh: Annual savings = $15,022

### Variable Frequency Drives (VFDs)

Pumps and agitators with VFDs reduce energy consumption during partial load conditions.

Typical savings: 20-40% of motor energy depending on load profile.

### Optimized Batch Scheduling

Coordinate batch cycles to minimize refrigeration system cycling and maintain steady loads on chillers and cooling towers.

## Instrumentation and Control

### Critical Measurement Points

| Parameter | Sensor Type | Location | Accuracy | Purpose |
|-----------|-------------|----------|----------|---------|
| Temperature | PT100 RTD | All process stages | ±0.2°C | Process control, validation |
| Pressure | Strain gauge | Homogenizer, pumps | ±1% FS | Safety, performance |
| Flow rate | Magnetic flowmeter | Pasteurizer inlet/outlet | ±0.5% | Residence time |
| Level | Ultrasonic/radar | All tanks | ±5 mm | Inventory, overfill prevention |
| pH | Glass electrode | Mix tank | ±0.1 pH | Quality control |
| Density | Coriolis meter | Blending outlet | ±0.1 kg/m³ | Composition verification |

### Control Philosophy

Modern mix preparation systems employ distributed control systems (DCS) or programmable logic controllers (PLC) with:

- Automated recipe management
- Real-time monitoring and alarming
- Historical data trending
- Regulatory compliance reporting
- Integration with plant MES/ERP systems

## Safety Considerations

### High-Temperature Hazards

Pasteurization systems operate at 80°C, creating burn risks. Requirements include:

- Insulation on all hot surfaces
- Warning labels
- Personnel training
- Emergency shutdown systems

### High-Pressure Hazards

Homogenizers operate at 2,500+ psi. Safety measures:

- Pressure relief valves
- Interlocked guards
- Regular maintenance inspection
- Operator training

### Food Safety

Critical control points (HACCP):

- Pasteurization time/temperature (CCP)
- Cooling rate (prevent microbial growth)
- Cleaning validation (ATP testing)
- Cross-contamination prevention

## Regulatory Compliance

### Pasteurized Milk Ordinance (PMO)

U.S. ice cream mix must comply with PMO requirements:

- Minimum pasteurization: 79.4°C (175°F) for 25 seconds
- Recording thermometer required
- Flow diversion valve mandatory
- Sanitary construction standards

### FDA Food Safety Modernization Act (FSMA)

Requires:

- Hazard analysis and preventive controls
- Environmental monitoring
- Supplier verification
- Corrective action procedures

### ASHRAE Standards

HVAC systems designed per:

- ASHRAE 62.1: Ventilation for acceptable indoor air quality
- ASHRAE 90.1: Energy standard for buildings
- ASHRAE Handbook: Refrigeration applications chapter

---

**References:**

- ASHRAE Handbook - Refrigeration, Chapter 39: Dairy Product Processing and Storage
- Code of Federal Regulations (CFR) Title 21, Part 135: Ice Cream and Frozen Desserts
- Pasteurized Milk Ordinance (PMO), FDA Publication
- Marshall, R.T., Goff, H.D., & Hartel, R.W. (2003). Ice Cream (6th ed.). Springer.
