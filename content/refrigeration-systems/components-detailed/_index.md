---
title: "Components Detailed"
weight: 7
description: "Comprehensive technical analysis of refrigeration cycle components including compressors, condensers, evaporators, and expansion devices with performance characteristics and selection criteria"
keywords: ["compressor types", "condenser design", "evaporator selection", "expansion valves", "refrigeration components"]
---

Refrigeration systems consist of four primary components that facilitate the vapor compression cycle: compressor, condenser, evaporator, and expansion device. Each component performs a specific thermodynamic function essential to heat transfer from low-temperature spaces to higher-temperature sinks.

## Component Categories and Functions

| Component | Primary Function | Thermodynamic Process | Pressure Level | Temperature Range |
|-----------|------------------|----------------------|----------------|-------------------|
| Compressor | Vapor compression and circulation | Isentropic compression | Low to high | -40°F to 200°F discharge |
| Condenser | Heat rejection to ambient | Desuperheating, condensation, subcooling | High pressure | 80°F to 130°F saturated |
| Expansion Device | Pressure reduction and flow control | Isenthalpic throttling | High to low | Variable ΔT 20-60°F |
| Evaporator | Heat absorption from refrigerated space | Evaporation and superheating | Low pressure | -40°F to 50°F saturated |

## Compressors

Compressors provide the mechanical energy required to circulate refrigerant through the system and create the pressure differential necessary for heat transfer. The compression process increases both pressure and temperature of the refrigerant vapor.

### Compressor Performance Parameters

| Parameter | Symbol | Typical Range | Impact |
|-----------|--------|---------------|---------|
| Volumetric Efficiency | ηv | 60-95% | Capacity at given displacement |
| Isentropic Efficiency | ηs | 65-85% | Power consumption |
| Compression Ratio | CR | 2:1 to 12:1 | Temperature rise and efficiency |
| Clearance Volume | Vc | 2-8% | Re-expansion losses |
| Displacement | D | 0.5-500 CFM | Nominal capacity |

### Positive Displacement Compressors

Positive displacement compressors trap a fixed volume of vapor and mechanically reduce the volume to achieve compression.

**Reciprocating Compressors:**
- Piston-cylinder arrangement with intake and discharge valves
- Capacity control via cylinder unloading or variable speed drive
- Volumetric efficiency: ηv = 1 + C - C(CR)^(1/n)
  - C = clearance volume ratio
  - CR = compression ratio
  - n = polytropic exponent (1.1-1.3 for refrigerants)
- Applications: 0.5 to 150 tons, medium to high compression ratios
- Suitable for R-22, R-404A, R-410A, ammonia

**Rotary Compressors:**
- Rolling piston or rotating vane creates compression chambers
- Continuous intake and discharge process
- Lower vibration than reciprocating types
- Applications: 0.5 to 10 tons, residential and light commercial
- Common refrigerants: R-410A, R-32

**Scroll Compressors:**
- Two spiral-shaped scrolls create multiple compression pockets
- One fixed scroll, one orbiting scroll
- Near-continuous compression process
- Volumetric efficiency 90-95%
- Applications: 1.5 to 60 tons, HVAC and refrigeration
- Advantages: quiet operation, high efficiency, fewer parts
- Limited turndown capability without modulation

**Screw Compressors:**
- Twin helical rotors mesh to compress vapor
- Continuous flow with minimal pulsation
- Capacity control via slide valve (10-100% capacity)
- Oil injection for cooling, sealing, and lubrication
- Applications: 20 to 1000+ tons, industrial refrigeration
- High efficiency at partial load conditions
- Suitable for ammonia, R-134a, R-404A, R-717

### Dynamic Compressors

Dynamic compressors impart velocity to refrigerant vapor and convert kinetic energy to pressure.

**Centrifugal Compressors:**
- Impeller accelerates vapor radially outward
- Diffuser converts velocity to pressure
- Multiple stages for higher compression ratios
- Capacity control via inlet guide vanes or variable speed
- Applications: 100 to 10,000+ tons, central plants
- High efficiency at design point (isentropic efficiency 75-85%)
- Surge and choke limits define operating envelope
- Common refrigerants: R-134a, R-1233zd(E), R-513A

## Condensers

Condensers reject heat absorbed in the evaporator plus compressor work to a heat sink (air, water, or evaporative process). The condensing process occurs at constant pressure with three distinct zones.

### Condenser Heat Transfer Zones

| Zone | Process | Heat Transfer | Refrigerant State | % Total Heat |
|------|---------|---------------|-------------------|--------------|
| Desuperheating | Vapor cooling | Q = ṁ × cp × ΔT | Superheated vapor | 10-20% |
| Condensing | Phase change | Q = ṁ × hfg | Two-phase | 70-85% |
| Subcooling | Liquid cooling | Q = ṁ × cp × ΔT | Subcooled liquid | 5-15% |

### Air-Cooled Condensers

- Finned-tube heat exchangers with forced air circulation
- Ambient air temperature determines condensing pressure
- Design approach: 15-25°F above ambient dry bulb
- Face velocity: 300-600 FPM
- Fin spacing: 10-20 fins per inch (lower for dirty environments)
- Heat rejection: Q = UA × LMTD × F
  - U = 15-30 Btu/hr-ft²-°F (air-cooled)
  - F = correction factor for cross-flow arrangement

**Advantages:**
- Simple installation, no water required
- Lower maintenance than water-cooled
- Suitable for all climates

**Disadvantages:**
- Higher condensing temperature and pressure
- Higher energy consumption
- Reduced capacity at high ambient temperature

### Water-Cooled Condensers

- Shell-and-tube or plate-and-frame configurations
- Condensing water from cooling tower or city water
- Design approach: 5-10°F above entering water temperature
- Water velocity: 3-10 ft/sec (fouling prevention)
- Overall heat transfer coefficient: U = 150-300 Btu/hr-ft²-°F

**Shell-and-Tube:**
- Refrigerant in shell, water in tubes
- Horizontal configuration most common
- Multiple passes (2, 4, or 6 passes) for higher effectiveness
- Removable tube bundle for cleaning

**Plate-and-Frame:**
- Alternating plates create refrigerant and water channels
- Counter-flow arrangement maximizes heat transfer
- Compact design (high surface area per volume)
- Easy to expand or clean by adding/removing plates

### Evaporative Condensers

- Refrigerant tubes sprayed with water in air stream
- Combined sensible and latent heat transfer
- Approach: 10-15°F above ambient wet bulb temperature
- Lower condensing temperature than air-cooled
- Water consumption: 2-4 GPM per 100 tons (evaporation + bleed)
- Freeze protection required in cold climates

## Evaporators

Evaporators absorb heat from the refrigerated space or medium, causing liquid refrigerant to vaporize. Evaporator design depends on the application (air cooling, liquid chilling, or product freezing).

### Evaporator Classification

| Type | Application | Temperature Range | Heat Transfer Mode |
|------|-------------|-------------------|-------------------|
| Direct Expansion (DX) | Air cooling | 20°F to 50°F SST | Forced convection |
| Flooded | Liquid chilling | 25°F to 45°F SST | Nucleate boiling |
| Recirculation | Process cooling | -40°F to 40°F SST | Enhanced boiling |
| Plate Freezer | Contact freezing | -40°F to -20°F | Conduction |

SST = Saturated Suction Temperature

### Air-Cooling Evaporators

**Finned-Tube Coils:**
- Copper tubes with aluminum fins
- Face velocity: 300-600 FPM (comfort cooling)
- Face velocity: 200-400 FPM (refrigeration, lower moisture carryover)
- Rows: 3-8 deep (more rows = lower TD, higher capacity)
- Fin spacing: 8-14 FPI (comfort cooling), 4-8 FPI (low temperature)
- Temperature difference (TD): air inlet minus SST
  - High temperature: 15-25°F TD
  - Medium temperature: 10-15°F TD
  - Low temperature: 8-12°F TD

**Performance Calculation:**
- Sensible capacity: Qs = 1.08 × CFM × ΔT
- Total capacity: Qt = 4.5 × CFM × Δh
- Sensible Heat Ratio: SHR = Qs / Qt

**Defrost Methods:**
- Off-cycle (above 35°F applications)
- Electric resistance (precise control, higher energy)
- Hot gas (efficient, uses system refrigerant)
- Reverse cycle (heat pump applications)

### Liquid Chilling Evaporators

**Shell-and-Tube Chillers:**
- Refrigerant in shell (DX or flooded), liquid in tubes
- Approach: 2-5°F (refrigerant SST to leaving liquid temperature)
- Liquid velocity: 3-12 ft/sec (turbulence for heat transfer)
- Enhanced tubes (rifled, micro-fin) increase U by 20-40%

**Plate Heat Exchangers:**
- Compact design for smaller capacities (5-200 tons)
- High turbulence yields U = 200-400 Btu/hr-ft²-°F
- Counter-flow arrangement maximizes effectiveness
- Pressure drop: 5-15 psi typical

## Expansion Devices

Expansion devices reduce refrigerant pressure from condensing to evaporating pressure and regulate refrigerant flow to match evaporator load. The expansion process is isenthalpic (constant enthalpy), resulting in flash gas formation.

### Expansion Device Comparison

| Device Type | Control Method | Superheat Control | Applications | Load Range |
|-------------|----------------|-------------------|--------------|------------|
| Fixed Orifice | Fixed opening | None (relies on charge) | Packaged units, heat pumps | Narrow |
| Capillary Tube | Fixed resistance | None | Small appliances, residential | Fixed |
| TXV (Thermal) | Superheat sensing | 6-12°F superheat | Universal, all capacities | 10-100% |
| EXV (Electronic) | Temperature sensors | 2-8°F superheat | Precision, VFD systems | 10-100% |
| Float Valve | Liquid level | N/A (maintains level) | Flooded evaporators | Variable |

### Thermostatic Expansion Valve (TXV)

The TXV modulates refrigerant flow to maintain constant superheat at the evaporator outlet.

**Force Balance:**
- Opening force: Bulb pressure (Pb) acting on diaphragm
- Closing forces: Evaporator pressure (Pe) + Spring pressure (Ps)
- Equilibrium: Pb = Pe + Ps

**Superheat Setting:**
- Static superheat: Spring pressure equivalent (typically 2-4°F)
- Operating superheat: 6-12°F at design conditions
- Total superheat = Static + Operating

**Bulb Placement:**
- Location: Suction line exit from evaporator
- Position: 4 or 8 o'clock on horizontal line (liquid contact)
- Insulation: Bulb must sense line temperature, not ambient

**Capacity Modulation:**
- Pressure drop across valve: ΔP = 50-150 psi typical
- Capacity proportional to √ΔP
- Reduced lift reduces ΔP and valve capacity

### Electronic Expansion Valve (EXV)

Stepper motor or pulse-width modulated valve provides precise refrigerant flow control.

**Advantages over TXV:**
- Lower superheat (2-8°F) increases evaporator capacity
- Active control adapts to changing conditions
- Remote sensing eliminates bulb lag
- Integrated with system controller

**Control Algorithm:**
- PID control based on measured superheat
- Superheat = Tsuction - Tsat(Psuction)
- Faster response than TXV (1-5 second update rate)

### Capillary Tube

Fixed-length small-diameter tube creates pressure drop through friction.

**Sizing Considerations:**
- Length: 3-20 feet typical
- Inside diameter: 0.026-0.082 inches
- Refrigerant charge critical (no superheat control)
- Selected for specific operating condition
- Poor performance at off-design conditions

**Applications:**
- Residential refrigerators and freezers
- Window air conditioners
- Small packaged units (<5 tons)
- Systems with minimal load variation

## Component Selection Criteria

### Compressor Selection

1. **Capacity Requirements:**
   - Calculate evaporator load at design conditions
   - Account for system losses and safety factor (10-15%)
   - Select compressor with adequate capacity at operating temperatures

2. **Operating Envelope:**
   - Verify condensing and evaporating temperatures within manufacturer limits
   - Check compression ratio: CR < 12:1 for single-stage reciprocating
   - Higher ratios require two-stage compression or screw compressor

3. **Efficiency:**
   - Compare EER or COP at ARI rating conditions
   - Evaluate part-load performance for variable loads
   - Consider variable speed or capacity modulation

### Condenser Selection

1. **Heat Rejection:**
   - Total heat rejection = Evaporator load + Compressor power
   - Heat rejection factor: 1.15-1.30 × evaporator capacity

2. **Available Heat Sink:**
   - Air-cooled: ambient dry bulb temperature
   - Water-cooled: cooling water temperature and availability
   - Evaporative: ambient wet bulb temperature

3. **Approach Temperature:**
   - Lower approach = larger condenser, higher cost, lower operating pressure
   - Economic optimization balances first cost and operating cost

### Evaporator Selection

1. **Load Calculation:**
   - Product load, infiltration, transmission, equipment heat
   - Dehumidification requirements (latent load)

2. **Temperature Difference:**
   - Lower TD = larger coil, higher cost, better humidity control
   - Higher TD = smaller coil, lower first cost, reduced efficiency

3. **Defrost Frequency:**
   - Low temperature applications require regular defrost
   - Defrost method impacts energy consumption and downtime

### Expansion Device Selection

1. **Load Variability:**
   - Fixed load: capillary tube or fixed orifice acceptable
   - Variable load: TXV or EXV required

2. **Precision Requirements:**
   - Standard comfort cooling: TXV adequate
   - Process applications, tight control: EXV preferred

3. **System Compatibility:**
   - Matching valve capacity to compressor and evaporator
   - Proper superheat setting for compressor protection
   - Consideration of refrigerant type and operating pressures

Proper component selection, sizing, and matching ensure refrigeration system reliability, efficiency, and performance across the full range of operating conditions. Each component must be evaluated not in isolation but as part of the integrated vapor compression cycle.
