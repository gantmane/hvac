---
title: "Air Transport Refrigeration"
aliases: ["Air Transport Refrigeration"]
weight: 5
---

Air transport refrigeration systems enable the shipment of temperature-sensitive cargo including pharmaceuticals, biologics, perishable foods, and electronics via commercial and dedicated cargo aircraft. These systems operate under unique constraints: limited power availability, altitude-induced pressure variations, rapid ground-to-cruise transitions, and strict weight limitations that fundamentally influence system design.

## Operational Environment

Aircraft cargo compartments present challenges distinct from surface transport:

**Pressure Effects**
- Cabin pressure at cruise altitude: 75-85 kPa (10.9-12.3 psia) equivalent to 2400 m (8000 ft) elevation
- Unpressurized cargo holds: ambient pressure at altitude, down to 25 kPa (3.6 psia) at 12,000 m (40,000 ft)
- Reduced air density decreases convective heat transfer coefficient by 20-30% at typical cruise conditions
- Refrigerant saturation temperatures shift with ambient pressure changes in vented systems

**Temperature Variations**
- Ground operations: -30°C to +50°C (-22°F to +122°F) depending on location and season
- Cruise conditions: -55°C to -40°C (-67°F to -40°F) outside fuselage skin
- Cargo hold temperature (passive): typically +5°C to +25°C (41°F to 77°F) with aircraft environmental control system (ECS)
- Ramp exposure times: 15-90 minutes during loading/unloading cycles

| Flight Phase | Duration (typical) | Ambient Temperature Range | Available Power |
|--------------|-------------------|---------------------------|-----------------|
| Ground (hot climate) | 30-60 min | +30°C to +50°C | 400 Hz AC or GPU |
| Ground (cold climate) | 30-60 min | -30°C to +10°C | 400 Hz AC or GPU |
| Climb | 15-25 min | Decreasing | Limited AC |
| Cruise | 1-15 hours | -55°C to -40°C | AC available |
| Descent | 20-30 min | Increasing | AC available |

## Unit Load Device (ULD) Thermal Control

ULDs are standardized containers designed to interface with aircraft cargo handling systems. Thermal control varies from passive insulation to active refrigeration.

### Passive Thermal Containers

**Insulated ULDs**
- Polyurethane foam insulation: 50-100 mm thickness, R-value 3.5-7.0 m²·K/W
- Vacuum insulated panels (VIP): 25-40 mm thickness, effective R-value 15-25 m²·K/W
- Phase change material (PCM) integration: eutectic plates at -20°C, 0°C, +5°C, or +21°C
- Thermal mass provided by PCM: 150-300 kJ/kg latent heat capacity
- Temperature maintenance duration: 24-96 hours depending on external conditions

**Envelope Construction**
- Outer shell: aluminum alloy (2024-T3 or 7075-T6), 1.6-2.0 mm thickness
- Inner liner: food-grade aluminum or composite panel
- Thermal bridge minimization: low-conductivity structural supports, edge seals
- Air infiltration control: compression gaskets achieving <0.1 air changes per hour

### Active Refrigerated ULDs

Electric-powered refrigeration units integrated into ULD structures provide precise temperature control independent of ambient conditions.

**Vapor Compression Systems**
- Compressor types: rotary (scroll or rolling piston), reciprocating for small units
- Refrigerants: R-134a, R-404A (legacy), R-452A, R-513A (low-GWP alternatives)
- Cooling capacity: 500-2000 W at +38°C ambient, +2°C setpoint
- Power input: 400 Hz, 115V AC (aircraft standard) or 230V AC (ground power)
- Power consumption: 0.8-2.5 kW during operation
- Temperature range: -20°C to +25°C controlled to ±2°C

**System Components**
- Hermetic compressor with vibration isolation mounting
- Microchannel or fin-and-tube heat exchangers optimized for weight
- Thermostatic expansion valve or electronic expansion valve (EEV)
- Microprocessor control with data logging capability
- Battery backup for monitoring during power interruptions (4-8 hours)

| ULD Type | Internal Volume | Cooling Capacity | Weight (empty) | Insulation Type |
|----------|----------------|------------------|----------------|-----------------|
| RKN (active) | 4.2 m³ | 1500 W @ +38°C | 95-115 kg | PU foam 75 mm |
| RAP (active) | 6.1 m³ | 2000 W @ +38°C | 140-165 kg | PU foam 75 mm |
| RKN (passive PCM) | 4.2 m³ | N/A (passive) | 75-90 kg | VIP 30 mm + PCM |
| RAP (passive PCM) | 6.1 m³ | N/A (passive) | 110-130 kg | VIP 30 mm + PCM |

### Cryogenic Cooling with Dry Ice

Dry ice (solid CO₂) sublimation provides refrigeration through enthalpy of sublimation (571 kJ/kg at 1 atm) without mechanical systems.

**Thermodynamic Properties**
- Sublimation temperature: -78.5°C (-109.3°F) at 101.325 kPa
- Sublimation pressure relationship: log₁₀(P) = 6.81228 - 1301.679/(T + 273.15) where P is in kPa, T in °C
- Specific heat (solid, -78°C): 1.04 kJ/kg·K
- Density (solid): 1560 kg/m³ at -78.5°C
- Gas expansion ratio: 1 kg solid → 0.51 m³ gas at STP

**Heat Removal Calculations**

Total cooling capacity from dry ice mass m (kg):

Q_total = m × [h_sublimation + c_p,gas × (T_final - T_sublimation)]

For dry ice warming cargo from +20°C to +2°C:
- Heat extraction from product: Q_product = m_product × c_p × ΔT
- Heat infiltration through insulation: Q_infiltration = U × A × ΔTLM × t
- Dry ice required: m_ice = (Q_product + Q_infiltration) / (h_sublimation + sensible cooling of CO₂ gas)

**Practical Application**
- Ice-to-product mass ratio: typically 0.15-0.30 for 24-48 hour shipments
- Placement: distributed throughout container, often in specialized chambers
- Ventilation requirement: 0.5-1.0 L/min per kg of dry ice to prevent CO₂ accumulation
- Aircraft limitations: maximum 200 kg dry ice per ULD (IATA regulations), labeled as UN 1845

**Safety Considerations**
- CO₂ concentration limits: 0.5% (5000 ppm) TWA, 3% (30,000 ppm) STEL
- Pressure relief venting: minimum vent area 25 cm² per 50 kg dry ice
- Personnel exposure during ground handling: confined space protocols required
- Asphyxiation risk in enclosed cargo holds: monitoring and ventilation essential

## Aircraft-Integrated Refrigeration Systems

Large cargo aircraft may incorporate built-in refrigeration serving multiple pallet positions.

### Centralized Refrigeration Units

**System Architecture**
- Vapor compression cycle with capacity 5-20 kW per zone
- Compressor drive: aircraft electrical bus (115V 400 Hz 3-phase) or pneumatic (bleed air)
- Condenser heat rejection: ram air through dedicated heat exchanger or integration with ECS
- Evaporator location: ducted air distribution to cargo zones
- Independent zones: 2-4 temperature zones with individual control

**Bleed Air Expansion Cooling**
- Available on aircraft with pneumatic systems (Boeing 747F, 777F, MD-11F)
- Compressed bleed air (310-370 kPa, 200-260°C) expanded through air cycle machine
- Expansion turbine produces air at -10°C to +5°C
- Flow rate: 0.05-0.15 kg/s per zone
- Coefficient of performance: effective COP 1.5-2.5 (accounting for engine fuel burn)

### Electric Vapor Compression Systems

Modern aircraft increasingly use electric refrigeration eliminating bleed air dependency.

**Technical Specifications**
- Scroll or screw compressor: 3-10 kW input per module
- Refrigerant: R-134a or R-513A (compliant with F-gas regulations)
- Evaporator air temperature: -20°C to +15°C controlled
- Supply air flow: 150-400 m³/h per zone at sea level equivalent
- Distribution: insulated flexible duct to cargo pallet positions
- Control: digital temperature controller with ±1°C accuracy

| Parameter | Conventional Cargo Hold | Refrigerated Cargo Zone | Deep Freeze Zone |
|-----------|------------------------|-------------------------|------------------|
| Temperature Range | +5°C to +25°C | -20°C to +20°C | -40°C to -20°C |
| Control Accuracy | ±5°C | ±2°C | ±3°C |
| Air Changes per Hour | 3-6 | 8-12 | 10-15 |
| Humidity Control | None | Optional (50-75% RH) | None (very low RH) |
| Power Requirement | N/A (ECS only) | 3-6 kW | 8-12 kW |

## Eutectic Plate Systems

Eutectic systems utilize phase change materials charged on the ground and providing cooling during flight without onboard power.

**Operating Principle**
- PCM frozen using ground power (6-12 hours charging at -25°C to -30°C)
- Latent heat release during phase transition maintains setpoint temperature
- Heat transfer: natural convection or forced air over eutectic plates
- Cooling duration: 24-72 hours depending on plate mass and insulation quality

**Eutectic Formulations**

| Eutectic Type | Phase Change Temperature | Latent Heat | Application |
|---------------|-------------------------|-------------|-------------|
| Water/salt (NaCl 23%) | -21°C (-6°F) | 280 kJ/kg | Frozen pharmaceuticals |
| Water (pure) | 0°C (32°F) | 334 kJ/kg | Fresh produce |
| Water/salt (proprietary) | +5°C (41°F) | 290 kJ/kg | Refrigerated biologics |
| Paraffin wax blend | +21°C (70°F) | 190 kJ/kg | Temperature-sensitive chemicals |

**Plate Design**
- Enclosure: HDPE or aluminum, thickness 2-4 mm
- Heat transfer enhancement: internal fins or turbulence promoters
- Plate dimensions: typically 400 × 600 × 25 mm, mass 4-8 kg
- Number per ULD: 8-20 plates depending on cooling requirement
- Positioning: vertical orientation along container walls for optimal convection

## Temperature Monitoring and Data Logging

Regulatory requirements (FDA 21 CFR Part 11, EU GDP) mandate continuous temperature recording for pharmaceutical shipments.

**Monitoring Systems**
- Data loggers: autonomous battery-powered units
- Sampling interval: 1-15 minutes (typically 5 minutes for pharma)
- Accuracy: ±0.5°C over operating range
- Memory: 8,000-32,000 data points
- Communication: USB download, Bluetooth, cellular, or RFID
- Alarm thresholds: programmable high/low limits with visual/audible indication

**Real-Time Tracking**
- Cellular IoT devices with GPS location
- Temperature, humidity, shock, light exposure sensors
- Cloud-based monitoring platforms
- Alert notification: SMS, email when excursions occur
- Battery life: 7-30 days continuous operation

## Design Considerations for Air Transport

**Weight Constraints**
- Every kg of refrigeration equipment reduces revenue payload
- Trade-off: active system weight (60-160 kg) vs. dry ice weight vs. passive insulation weight
- Fuel cost implications: additional 0.03-0.05 L fuel per kg per 1000 km flight

**Power Availability**
- Ground power units (GPU): often limited to 60-90 minutes before departure
- In-flight power: 115V 400 Hz AC available in cargo holds of most widebody aircraft
- Power budget: refrigeration competes with other cargo systems (monitoring, ventilation)
- Battery backup: required for units to survive ground transfer without power

**Altitude Effects on Refrigeration Performance**
- Compressor volumetric efficiency decreases 5-10% due to reduced suction density
- Evaporator capacity affected by air density: approximately 15% reduction at cruise altitude
- Condenser performance improved at cruise due to cold ambient (-40°C to -55°C)
- Net effect: system operates with different pressure ratios than ground testing

**Rapid Thermal Transitions**
- Takeoff from +40°C desert location to -50°C cruise in 20 minutes
- Thermal shock to container structure and products
- Condensation risk during descent into humid climates
- Control algorithm must handle 90°C ambient swing without overshoot

## Pharmaceutical Cold Chain Applications

Temperature-sensitive pharmaceuticals require stringent thermal control throughout air transport.

**Temperature Classifications**
- Deep frozen: -80°C to -60°C (ultra-cold chain for mRNA vaccines)
- Frozen: -25°C to -15°C (conventional vaccines, biologics)
- Refrigerated: +2°C to +8°C (most vaccines, insulin, blood products)
- Controlled room temperature: +15°C to +25°C (certain APIs and finished drugs)

**Qualification Requirements**
- Thermal mapping: demonstrate temperature uniformity within ±2°C throughout container
- Operational qualification (OQ): performance testing at extreme ambient conditions
- Performance qualification (PQ): simulated flight profiles with product simulant
- Stability studies: product viability testing after transport exposure
- Annual recertification of active refrigeration units

**Excursion Management**
- Mean kinetic temperature (MKT) calculation:
  T_MK = (ΔH/R) / [ln(t₁e^(-ΔH/RT₁) + t₂e^(-ΔH/RT₂) + ... + t_ne^(-ΔH/RT_n)) - ln(t₁ + t₂ + ... + t_n)]
  where ΔH/R typically assumed as 83.144 K (activation energy)
- Product-specific stability data determines acceptable MKT
- Deviation reporting protocols when temperature exceeds specified range

This technical foundation enables reliable temperature-controlled air cargo operations, balancing thermal performance requirements against weight, cost, and operational constraints inherent to aviation applications.
