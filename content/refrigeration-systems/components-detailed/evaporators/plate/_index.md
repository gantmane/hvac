---
title: "Plate Evaporators"
aliases: ["Plate Evaporators"]
description: "Comprehensive technical guide to plate evaporators including brazed and gasketed designs, heat transfer calculations, flow arrangements, pressure drop analysis, and applications in chillers and heat pumps for HVAC systems."
weight: 3
---

## Overview

Plate evaporators are compact heat exchangers using thin metal plates to separate refrigerant and secondary fluid streams. The plates form channels that maximize surface area per unit volume, achieving heat transfer effectiveness exceeding 85% in typical installations.

Two primary designs dominate commercial applications:

- Brazed plate heat exchangers (BPHE): Copper-brazed stainless steel plates in permanent assembly
- Gasketed plate heat exchangers (GPHE): Bolted frame with removable plates and elastomeric gaskets

**Key performance advantages:**

- Heat transfer coefficients: 3000-7000 W/m²·K (water-to-refrigerant)
- Approach temperatures: 1-3°C achievable
- Volume displacement: 1/5 to 1/6 of equivalent shell-and-tube design
- Counterflow arrangement inherent to plate geometry

## Brazed Plate Evaporator Design

### Construction Details

Brazed plate evaporators use copper or nickel brazing to join corrugated stainless steel plates (typically 316L) into a permanent assembly. The brazing process creates a vacuum-tight, high-pressure rated unit without gaskets.

**Plate specifications:**

| Parameter | Typical Range | Notes |
|-----------|---------------|-------|
| Plate thickness | 0.4-0.6 mm | AISI 316L stainless steel |
| Plate width | 76-500 mm | Varies by manufacturer |
| Plate height | 190-1300 mm | Effective heat transfer area |
| Channel gap | 1.5-5.0 mm | Between adjacent plates |
| Brazing material | Copper (99.9%) | Nickel for ammonia systems |
| Brazing temperature | 1100-1150°C | Furnace brazing in vacuum |

**Corrugation patterns:**

The herringbone (chevron) pattern on each plate creates turbulence and provides structural support. The corrugation angle (β) relative to the vertical axis determines flow characteristics:

- Low angle (β = 30°): Lower pressure drop, lower heat transfer coefficient
- Medium angle (β = 45-60°): Balanced performance for most HVAC applications
- High angle (β = 65°): Maximum turbulence, highest heat transfer coefficient

### Pressure and Temperature Ratings

Brazed plate evaporators operate across a wide envelope of conditions:

| Design Parameter | R-134a Systems | R-410A Systems | Water/Glycol Systems |
|------------------|----------------|----------------|----------------------|
| Maximum pressure | 30 bar (435 psig) | 45 bar (653 psig) | 30 bar (435 psig) |
| Minimum temp | -195°C | -60°C | -50°C (with glycol) |
| Maximum temp | +225°C | +150°C | +200°C |
| Test pressure | 45 bar | 67.5 bar | 45 bar |

Thermal stress considerations limit rapid temperature changes to 10-15°C per minute during startup and shutdown sequences.

## Gasketed Plate Evaporators

### Frame and Plate Assembly

Gasketed designs allow field maintenance and capacity adjustment by adding or removing plates. The assembly consists of:

1. **Fixed frame plate**: Permanently mounted to support structure
2. **Movable pressure plate**: Compressed against stack via tightening bolts
3. **Heat transfer plates**: Suspended on upper and lower guide bars
4. **Port gaskets**: Seal refrigerant and secondary fluid passages
5. **Compression bolts**: Maintain gasket compression (typically 4-8 bolts)

**Gasket materials by refrigerant:**

| Refrigerant | Gasket Material | Temperature Range | Notes |
|-------------|-----------------|-------------------|-------|
| R-134a, R-410A | NBR (Nitrile) | -35 to +140°C | Standard for HFC refrigerants |
| R-717 (NH₃) | EPDM | -50 to +150°C | Ammonia compatible |
| R-744 (CO₂) | HNBR | -50 to +150°C | High-pressure transcritical systems |
| Glycol solutions | NBR or EPDM | -35 to +110°C | Avoid glycol concentrations >50% |

### Plate Geometry and Pattern Selection

Plate surface patterns generate turbulence through secondary flow and flow separation. The Reynolds number in plate channels ranges from 50 to 5000, with transition to turbulent flow occurring at Re ≈ 400 (compared to Re ≈ 2300 in smooth tubes).

**Hydraulic diameter calculation:**

d_h = (2 × b) / φ

Where:
- d_h = hydraulic diameter (m)
- b = channel spacing (m)
- φ = surface enlargement factor (1.15-1.25 for typical corrugations)

## Heat Transfer Coefficient Calculations

### Overall Heat Transfer Coefficient

The overall heat transfer coefficient (U) for plate evaporators depends on film coefficients for both fluids and thermal resistance of the plate material:

1/U = 1/h_ref + t/k_plate + 1/h_water + R_fouling

Where:
- U = overall heat transfer coefficient (W/m²·K)
- h_ref = refrigerant-side film coefficient (W/m²·K)
- h_water = water-side film coefficient (W/m²·K)
- t = plate thickness (m)
- k_plate = thermal conductivity of stainless steel (16 W/m·K)
- R_fouling = fouling resistance (m²·K/W)

**Typical coefficient values:**

| Fluid Side | Film Coefficient Range | Dominant Regime |
|------------|------------------------|-----------------|
| Water (turbulent) | 4000-8000 W/m²·K | Forced convection |
| Glycol 30% (turbulent) | 3000-6000 W/m²·K | Higher viscosity reduces h |
| Refrigerant evaporation | 5000-15000 W/m²·K | Nucleate boiling dominant |
| Overall U (clean) | 2500-5500 W/m²·K | Combined resistance |
| Overall U (fouled) | 2000-4500 W/m²·K | After 1 year operation |

### Refrigerant-Side Film Coefficient

During evaporation, the refrigerant-side coefficient depends on heat flux, refrigerant properties, and flow regime. For nucleate boiling in plate evaporators:

h_ref = 207 × (q/A)^0.745 × P_r^0.581 × M^(-0.5)

Where:
- q/A = heat flux (W/m²)
- P_r = reduced pressure (P/P_critical)
- M = molecular weight (kg/kmol)

At low quality (x < 0.3), forced convection dominates. At high quality (x > 0.8), dry-out reduces the heat transfer coefficient significantly.

**Design guidelines for refrigerant distribution:**

- Inlet quality: 0.15-0.25 typical
- Outlet quality: 0.90-0.98 recommended
- Maximum superheat in evaporator: 2-5 K
- Minimum mass flux: 15 kg/m²·s to prevent flow instability

## Flow Arrangement Configurations

### Single-Pass Counterflow

The standard configuration for plate evaporators routes refrigerant and secondary fluid in opposite directions through alternating channels. This arrangement achieves the highest thermal effectiveness and maintains stable evaporating conditions.

**Flow path characteristics:**

- Refrigerant: Enters bottom port, exits top port (vertical upflow preferred)
- Secondary fluid: Enters top port, exits bottom port
- Thermal effectiveness: 0.85-0.92 typical
- Temperature approach: 1.5-3.0 K achievable at design conditions

### Multi-Pass Arrangements

For applications requiring specific pressure drop or velocity constraints, multi-pass configurations redirect fluid flow:

**Two-pass refrigerant side:**

- Divides refrigerant flow into two parallel paths
- Reduces refrigerant-side pressure drop by 60-70%
- Decreases heat transfer coefficient by 15-20%
- Used when distributor pressure drop limits refrigerant feed

**Parallel flow (co-current):**

- Both fluids flow in same direction
- Lower thermal effectiveness (0.50-0.75)
- More uniform plate temperature distribution
- Reduces thermal stress during transient operation

## Pressure Drop Analysis

### Refrigerant-Side Pressure Drop

Two-phase pressure drop in plate evaporators includes acceleration, friction, and elevation components:

ΔP_total = ΔP_friction + ΔP_acceleration + ΔP_elevation

**Friction pressure drop** dominates in typical installations:

ΔP_friction = 2 × f × (L/d_h) × (G²/ρ) × φ²

Where:
- f = friction factor (function of Re and surface roughness)
- L = effective plate length (m)
- d_h = hydraulic diameter (m)
- G = mass flux (kg/m²·s)
- ρ = density (kg/m³)
- φ = two-phase multiplier (1.5-3.5 for evaporation)

**Typical pressure drop values:**

| Operating Condition | Refrigerant ΔP | Water/Glycol ΔP | Total System Impact |
|---------------------|----------------|-----------------|---------------------|
| Design load | 15-40 kPa | 30-60 kPa | Corresponds to 0.5-1.5 K saturation temperature change |
| Part load (50%) | 5-12 kPa | 10-20 kPa | Reduced mass flux decreases ΔP |
| Overload (120%) | 25-60 kPa | 50-90 kPa | May require compressor capacity verification |

High refrigerant pressure drop reduces evaporating temperature and system efficiency. Maximum allowable pressure drop: 50 kPa (0.5 bar) for most applications.

### Water-Side Pressure Drop

Water-side pressure drop follows single-phase correlations with corrections for plate geometry:

ΔP_water = 4 × f × (L/d_h) × (ρ × v²/2) × N_passes

Where:
- v = water velocity (m/s)
- N_passes = number of passes through heat exchanger

**Recommended water velocity ranges:**

- Minimum velocity: 0.3 m/s (prevents sedimentation and fouling)
- Optimal velocity: 0.6-1.2 m/s (balances pressure drop and heat transfer)
- Maximum velocity: 2.5 m/s (erosion and noise concerns above this)

## Applications in Chillers and Heat Pumps

### Water-Cooled Chiller Evaporators

Plate evaporators serve as the primary heat exchanger between refrigerant and chilled water in water-cooled chillers from 20 kW to 2000 kW capacity.

**Design parameters for chiller applications:**

| Parameter | Value | Basis |
|-----------|-------|-------|
| Chilled water supply temp | 5-7°C | Standard comfort cooling |
| Chilled water return temp | 10-12°C | 5 K temperature rise |
| Evaporating temperature | 0-4°C | 3-5 K approach to leaving water |
| Water flow rate | 0.172 L/s per kW | Based on 5 K ΔT |
| Refrigerant charge | 0.3-0.6 kg/kW | 60-80% less than shell-and-tube |

**Advantages in chiller applications:**

- Compact footprint reduces equipment room requirements
- Low refrigerant charge minimizes environmental impact and cost
- High turbulence maintains heat transfer with fouled water
- Brazed construction eliminates gasket maintenance

### Heat Pump Evaporators (Air-to-Water)

In air-source heat pumps, plate evaporators transfer heat from a glycol solution (circulated through an outdoor coil) to the refrigerant. The evaporator operates at temperatures from -15°C to +15°C depending on outdoor conditions.

**Glycol solution considerations:**

- Propylene glycol concentration: 25-35% by volume (freeze protection to -18°C)
- Ethylene glycol concentration: 20-30% by volume (freeze protection to -15°C)
- Viscosity increases 2-3× compared to water
- Heat transfer coefficient reduces 15-25% at same velocity
- Flow rate increase of 10-15% required to maintain equivalent heat transfer

### Ground-Source Heat Pump Applications

Plate evaporators in ground-source heat pumps operate with stable inlet temperatures year-round:

**Vertical loop systems:**

- Supply temperature: 0-10°C (cooling mode), -5 to +5°C (heating mode)
- Temperature change: 3-5 K across evaporator
- Freeze protection: 20-25% propylene glycol
- Fouling factor: 0.000009 m²·K/W (cleaner than surface water)

**Horizontal loop systems:**

- Greater temperature variation than vertical loops
- Summer supply: 15-25°C
- Winter supply: -5 to +5°C
- Design for worst-case (lowest) temperature condition

## Capacity Control and Part-Load Operation

### Variable Water Flow

Reducing chilled water flow rate through the plate evaporator provides capacity control while maintaining refrigerant evaporating temperature. The heat transfer relationship at part load:

Q_partial = Q_design × (m_partial/m_design)^0.8

This approach reduces pump energy but increases approach temperature as water-side heat transfer coefficient decreases.

### Multiple Refrigerant Circuits

Large plate evaporators (>500 kW) may incorporate multiple refrigerant circuits with independent expansion valves. Each circuit feeds a dedicated set of plates, allowing:

- Staged capacity reduction (50%, 75%, 100%)
- Continued operation if one circuit fails
- Improved oil return at part load
- Enhanced refrigerant distribution uniformity

## Fouling and Maintenance

### Fouling Resistance Values

Plate evaporators maintain performance longer than shell-and-tube designs due to high turbulence, but fouling still accumulates over time:

| Water Source | Initial R_fouling | After 1 Year | After 3 Years | Cleaning Frequency |
|--------------|-------------------|--------------|---------------|---------------------|
| Closed loop (treated) | 0.000009 | 0.000018 | 0.000035 | Every 3-5 years |
| Cooling tower water | 0.000018 | 0.000044 | 0.000088 | Every 1-2 years |
| Untreated well water | 0.000035 | 0.000088 | 0.000176 | Every 6-12 months |
| River/lake water | 0.000053 | 0.000123 | 0.000211 | Every 3-6 months |

Values in m²·K/W.

### Chemical Cleaning Procedures

**Brazed plate evaporators** require circulation cleaning since plates cannot be disassembled:

1. Isolate evaporator and drain refrigerant
2. Circulate acid solution (citric or phosphoric, 2-5% concentration) at 50-60°C
3. Circulation time: 2-4 hours depending on fouling severity
4. Flush with clean water until pH neutral
5. Pressure test before returning to service

**Gasketed plate evaporators** allow disassembly for mechanical cleaning:

1. Release compression bolts and remove pressure plate
2. Remove plates from guide bars
3. Inspect gaskets for damage or deterioration
4. Clean plates with soft brush and mild detergent
5. Replace damaged gaskets
6. Reassemble with proper gasket alignment
7. Torque compression bolts to manufacturer specification

## Selection and Sizing

### Heat Transfer Area Calculation

The required heat transfer area derives from the fundamental heat exchanger equation:

Q = U × A × LMTD

Where:
- Q = heat transfer rate (W)
- U = overall heat transfer coefficient (W/m²·K)
- A = effective heat transfer area (m²)
- LMTD = log mean temperature difference (K)

**LMTD for counterflow evaporator:**

LMTD = (ΔT_in - ΔT_out) / ln(ΔT_in / ΔT_out)

Where:
- ΔT_in = T_water_in - T_refrigerant_evap
- ΔT_out = T_water_out - T_refrigerant_evap

**Design margin:** Select plate evaporator with 10-15% excess capacity to account for fouling, degradation, and uncertainty in heat transfer coefficients.

### Performance Curves

Manufacturer-supplied performance curves show capacity as a function of:

- Evaporating temperature (horizontal axis)
- Secondary fluid flow rate (multiple curves)
- Entering fluid temperature (multiple curves or correction factors)

**Example sizing calculation:**

Given:
- Cooling capacity: 350 kW
- Chilled water: 12°C entering, 7°C leaving
- Evaporating temperature: 2°C
- Water flow rate: 60 L/min = 0.001 m³/s

Heat transfer rate matches cooling capacity:
Q = m × c_p × ΔT = (1000 kg/m³)(0.001 m³/s)(4180 J/kg·K)(5 K) = 20.9 kW per K

Calculate LMTD:
- ΔT_in = 12°C - 2°C = 10 K
- ΔT_out = 7°C - 2°C = 5 K
- LMTD = (10 - 5) / ln(10/5) = 7.21 K

Assuming U = 4000 W/m²·K:
A = Q / (U × LMTD) = 350,000 / (4000 × 7.21) = 12.1 m²

Select plate evaporator with 13-14 m² effective area to provide design margin.

## Installation Requirements

### Piping Connections

Proper piping practices ensure reliable operation and serviceable access:

**Refrigerant side:**
- Install liquid line filter-drier upstream of expansion valve
- Provide isolation valves for service access
- Support distributor assembly independently from plate evaporator
- Install liquid line sight glass to verify subcooling
- Pitch horizontal refrigerant lines 1:100 toward compressor for oil return

**Water side:**
- Install balancing valve on outlet for flow adjustment
- Provide thermometer wells at inlet and outlet (verify performance)
- Include isolation valves and drain connections
- Use flexible connectors to isolate vibration
- Install strainer upstream (80-100 mesh minimum)

### Thermal Insulation

Insulate the entire plate evaporator assembly to prevent condensation and heat gain:

- Insulation thickness: 25-50 mm (varies with ambient conditions and humidity)
- Material: Closed-cell elastomeric foam (NBR/PVC)
- Vapor barrier: Essential in humid environments
- Access panels: Provide removable insulation at connection points

Failure to insulate results in capacity loss of 5-10% and condensation dripping onto equipment below.

---

**Related Topics:**
- Shell-and-Tube Evaporators
- Expansion Valves and Refrigerant Distributors
- Chiller System Design
- Heat Pump Fundamentals
- Water Treatment for HVAC Systems
