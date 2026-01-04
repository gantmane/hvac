---
title: "HVAC Cooling and Heating Load Calculations: A Comprehensive Technical Guide"
description: "In-depth analysis of HVAC load calculation methods including ASHRAE Transfer Function Method, Radiant Time Series, Manual J for residential, and CLTD/CLF for commercial applications with worked examples."
keywords: ["HVAC load calculation", "cooling load", "heating load", "ASHRAE TFM", "Radiant Time Series", "Manual J", "CLTD CLF", "heat transfer", "thermal loads", "building energy"]
categories: ["Load Calculations", "Energy Efficiency"]
tags: ["cooling loads", "heating loads", "ASHRAE", "thermal analysis", "heat transfer", "building physics", "energy modeling"]
author: "Evgeniy Gantman"
date: 2026-01-04
draft: false
---

## Introduction

HVAC load calculation represents the fundamental engineering task that determines equipment sizing, energy consumption, and occupant comfort in buildings. The calculation quantifies the rate of heat gain (cooling load) or heat loss (heating load) that HVAC equipment must offset to maintain desired indoor conditions. Accurate load calculations prevent undersized systems that fail to maintain comfort and oversized systems that cycle excessively, waste energy, and increase first costs.

This technical guide analyzes the physics-based methods for calculating thermal loads, examines ASHRAE-approved calculation procedures, and demonstrates practical application through worked examples for both residential and commercial buildings.

## Fundamental Heat Transfer Mechanisms

Heat transfer in buildings occurs through three primary mechanisms that govern thermal load calculations.

### Conduction

Conduction transfers heat through solid materials according to Fourier's law. The heat flux through a building element follows:

{{< formula display="true" >}}
$$q = -k \frac{dT}{dx}$$
{{< /formula >}}

Where:
- $q$ = heat flux (W/m²)
- $k$ = thermal conductivity (W/m·K)
- $dT/dx$ = temperature gradient (K/m)

For steady-state conduction through a wall with multiple layers, the overall heat transfer rate becomes:

{{< formula display="true" >}}
$$Q = U \cdot A \cdot \Delta T$$
{{< /formula >}}

Where:
- $Q$ = heat transfer rate (W)
- $U$ = overall heat transfer coefficient (W/m²·K)
- $A$ = surface area (m²)
- $\Delta T$ = temperature difference (K)

The U-value (thermal transmittance) accounts for all layers including inside and outside air films:

{{< formula display="true" >}}
$$U = \frac{1}{R_{total}} = \frac{1}{R_{i} + \sum R_{layers} + R_{o}}$$
{{< /formula >}}

Where:
- $R_{i}$ = inside surface resistance (m²·K/W)
- $R_{layers}$ = resistance of each material layer (m²·K/W)
- $R_{o}$ = outside surface resistance (m²·K/W)

### Convection

Convection transfers heat between surfaces and fluids (air or water). The convective heat transfer follows Newton's law of cooling:

{{< formula display="true" >}}
$$q = h \cdot (T_{surface} - T_{fluid})$$
{{< /formula >}}

Where:
- $h$ = convective heat transfer coefficient (W/m²·K)
- $T_{surface}$ = surface temperature (K)
- $T_{fluid}$ = bulk fluid temperature (K)

The convection coefficient $h$ depends on flow conditions (natural or forced), fluid properties, and geometry. Typical values range from 5-25 W/m²·K for natural convection in air to 10-100 W/m²·K for forced convection.

### Radiation

Thermal radiation transfers energy through electromagnetic waves without requiring a medium. The net radiative exchange between a surface and its surroundings follows the Stefan-Boltzmann law:

{{< formula display="true" >}}
$$q = \epsilon \sigma (T_{surface}^4 - T_{surrounding}^4)$$
{{< /formula >}}

Where:
- $\epsilon$ = surface emissivity (dimensionless, 0-1)
- $\sigma$ = Stefan-Boltzmann constant (5.67×10⁻⁸ W/m²·K⁴)
- $T$ = absolute temperature (K)

For small temperature differences, linearized radiation heat transfer becomes:

{{< formula display="true" >}}
$$q = h_{r} \cdot (T_{surface} - T_{surrounding})$$
{{< /formula >}}

Where $h_{r}$ represents the linearized radiation coefficient.

### Combined Heat Transfer

Building envelope heat transfer combines conduction through materials with convection and radiation at surfaces. The overall process defines the U-value that appears in load calculations.

{{< diagram >}}
graph LR
    A[Outdoor Air<br/>T_o] -->|Convection + Radiation<br/>h_o| B[Outer Surface]
    B -->|Conduction<br/>k_1/L_1| C[Layer 1]
    C -->|Conduction<br/>k_2/L_2| D[Layer 2]
    D -->|Conduction<br/>k_n/L_n| E[Inner Surface]
    E -->|Convection + Radiation<br/>h_i| F[Indoor Air<br/>T_i]

    style A fill:#ffcccc
    style F fill:#ccccff
    style B fill:#ffe6cc
    style E fill:#e6ccff
{{< /diagram >}}

## Sensible vs Latent Loads

Thermal loads separate into sensible and latent components with distinct physical mechanisms and calculation methods.

### Sensible Loads

Sensible heat changes air temperature without phase change. All conduction through building envelope, solar radiation through windows, heat from lights and equipment (convective portion), and sensible heat from occupants contribute to sensible loads.

{{< formula display="true" >}}
$$Q_{sensible} = \dot{m} \cdot c_{p} \cdot \Delta T = \rho \cdot \dot{V} \cdot c_{p} \cdot \Delta T$$
{{< /formula >}}

Where:
- $\dot{m}$ = mass flow rate (kg/s)
- $c_{p}$ = specific heat capacity of air (≈1006 J/kg·K)
- $\Delta T$ = temperature difference (K)
- $\rho$ = air density (≈1.2 kg/m³)
- $\dot{V}$ = volumetric flow rate (m³/s)

For standard air conditions (101.325 kPa, 20°C), this simplifies to:

{{< formula display="true" >}}
$$Q_{sensible} [W] = 1.23 \cdot \dot{V} [L/s] \cdot \Delta T [K]$$
{{< /formula >}}

Or in IP units:

{{< formula display="true" >}}
$$Q_{sensible} [Btu/h] = 1.08 \cdot \dot{V} [CFM] \cdot \Delta T [°F]$$
{{< /formula >}}

### Latent Loads

Latent heat involves moisture addition or removal without temperature change. Sources include occupant respiration and perspiration, infiltration of humid outdoor air, and evaporation from wet surfaces or processes.

{{< formula display="true" >}}
$$Q_{latent} = \dot{m} \cdot h_{fg} \cdot \Delta \omega = \rho \cdot \dot{V} \cdot h_{fg} \cdot \Delta \omega$$
{{< /formula >}}

Where:
- $h_{fg}$ = latent heat of vaporization of water (≈2501 kJ/kg at 0°C)
- $\Delta \omega$ = humidity ratio difference (kg water/kg dry air)

For standard conditions, this simplifies to:

{{< formula display="true" >}}
$$Q_{latent} [W] = 3010 \cdot \dot{V} [L/s] \cdot \Delta \omega [kg/kg]$$
{{< /formula >}}

Or in IP units:

{{< formula display="true" >}}
$$Q_{latent} [Btu/h] = 4840 \cdot \dot{V} [CFM] \cdot \Delta \omega [lb/lb]$$
{{< /formula >}}

Alternatively, using grains of moisture (1 lb = 7000 grains):

{{< formula display="true" >}}
$$Q_{latent} [Btu/h] = 0.69 \cdot \dot{V} [CFM] \cdot \Delta W [grains/lb]$$
{{< /formula >}}

### Sensible Heat Ratio

The sensible heat ratio (SHR) quantifies the relationship between sensible and total loads:

{{< formula display="true" >}}
$$SHR = \frac{Q_{sensible}}{Q_{sensible} + Q_{latent}} = \frac{Q_{sensible}}{Q_{total}}$$
{{< /formula >}}

SHR values range from 0.6-0.7 for humid climates with high latent loads to 0.85-0.95 for dry climates with predominantly sensible loads. Equipment selection requires matching the equipment's SHR capability to the building's load SHR.

{{< table >}}
| Climate Type | Typical SHR | Latent Load Fraction |
|--------------|-------------|---------------------|
| Hot-Humid (Miami) | 0.65-0.75 | 25-35% |
| Hot-Dry (Phoenix) | 0.90-0.95 | 5-10% |
| Temperate (New York) | 0.75-0.85 | 15-25% |
| Cold-Dry (Minneapolis) | 0.85-0.90 | 10-15% |
{{< /table >}}

## ASHRAE Transfer Function Method (TFM)

The Transfer Function Method represents ASHRAE's rigorous approach to calculating dynamic heat transfer through building envelopes. TFM accounts for thermal mass effects by treating building elements as dynamic systems with time-dependent responses.

### Physical Basis

Building materials store thermal energy during heat transfer, creating a time lag between outdoor temperature variations and indoor heat gain. Massive construction (concrete, brick) exhibits significant thermal lag, while lightweight construction (wood frame) responds quickly to temperature changes.

The heat flux through a wall at time $\theta$ depends on current and past temperature differences and past heat fluxes:

{{< formula display="true" >}}
$$q_{\theta} = \sum_{j=0}^{n_t} b_j (T_{o,\theta-j\delta} - T_{i,\theta-j\delta}) - \sum_{j=1}^{n_q} d_j q_{\theta-j\delta}$$
{{< /formula >}}

Where:
- $q_{\theta}$ = current heat flux (W/m²)
- $b_j$ = conduction transfer function (CTF) coefficients (W/m²·K)
- $d_j$ = flux history coefficients (dimensionless)
- $T_{o,\theta-j\delta}$ = outdoor temperature at time $\theta-j\delta$ (K)
- $T_{i,\theta-j\delta}$ = indoor temperature at time $\theta-j\delta$ (K)
- $\delta$ = time step (typically 1 hour)

### Response Factors

ASHRAE provides tabulated conduction transfer functions for common wall, roof, and floor constructions. The coefficients depend on:

- Material thermal properties (conductivity, density, specific heat)
- Layer sequence and thickness
- Surface conditions (absorptance, emittance)

For a simple homogeneous wall, the CTF coefficients reduce to the steady-state U-value plus dynamic correction terms. For multi-layer assemblies, numerical methods (finite difference, finite element) generate the CTF coefficients.

### Sol-Air Temperature

The sol-air temperature combines outdoor air temperature with solar radiation and long-wave radiation effects into a single equivalent temperature:

{{< formula display="true" >}}
$$T_{sol-air} = T_{outdoor} + \frac{\alpha \cdot I_{solar}}{h_{o}} - \frac{\epsilon \cdot \Delta R}{h_{o}}$$
{{< /formula >}}

Where:
- $\alpha$ = solar absorptance of surface (dimensionless, 0-1)
- $I_{solar}$ = total solar irradiance on surface (W/m²)
- $h_{o}$ = outside combined convection-radiation coefficient (W/m²·K)
- $\epsilon$ = long-wave emittance (dimensionless, 0-1)
- $\Delta R$ = difference between long-wave radiation from surface to sky and surroundings (W/m²)

For horizontal surfaces (roofs) on clear days, $\Delta R/h_{o}$ ≈ 4 K. For vertical surfaces or cloudy conditions, $\Delta R/h_{o}$ ≈ 0.

The sol-air temperature replaces outdoor air temperature in the CTF equations, accounting for solar radiation effects on opaque surfaces.

### TFM Calculation Procedure

1. Determine wall/roof construction and orientation
2. Select appropriate CTF coefficients from ASHRAE tables or calculate
3. Calculate sol-air temperatures for each hour
4. Apply CTF equation to find hourly heat gain through each surface
5. Sum contributions from all surfaces
6. Add internal gains (people, lights, equipment)
7. Calculate infiltration/ventilation loads
8. Identify peak load hour and magnitude

The Transfer Function Method provides accurate results for buildings with significant thermal mass but requires hourly calculations and extensive tabulated data.

## Radiant Time Series (RTS) Method

The Radiant Time Series method simplifies TFM while maintaining accuracy for most building types. ASHRAE currently recommends RTS as the preferred cooling load calculation method.

### Conceptual Framework

RTS recognizes that radiant heat gains (solar through windows, lights, equipment) do not immediately become cooling loads. Instead, radiant energy:

1. Strikes and heats interior surfaces
2. Stores in thermal mass of surfaces
3. Releases to room air through convection over time

This time lag converts instantaneous radiant heat gains into time-delayed cooling loads through radiant time factors.

{{< diagram >}}
graph TD
    A[Solar Radiation<br/>Through Window] -->|100% Radiant| B[Interior Surfaces]
    C[Lighting Heat] -->|60-80% Radiant| B
    D[Equipment Heat] -->|10-50% Radiant| B
    E[People Heat] -->|40-60% Radiant| B

    B -->|Thermal Storage<br/>in Mass| F[Time Delay]
    F -->|Convection| G[Cooling Load<br/>to Space Air]

    C -->|20-40% Convective| G
    D -->|50-90% Convective| G
    E -->|40-60% Convective| G

    style A fill:#ffeb99
    style B fill:#ff9999
    style G fill:#99ccff
{{< /diagram >}}

### Radiant Time Factors

Radiant time factors (RTFs) quantify the fraction of radiant heat gain that becomes cooling load in each subsequent hour. For a radiant gain $Q_{radiant}$ occurring at time $\theta=0$, the cooling load at hour $\theta$ equals:

{{< formula display="true" >}}
$$Q_{cooling,\theta} = Q_{radiant} \cdot RTF_{\theta}$$
{{< /formula >}}

ASHRAE provides RTF values as functions of:
- Building construction type (lightweight, medium, heavyweight)
- Zone type (perimeter, interior)
- Solar distribution pattern

{{< table >}}
| Hour After Gain | Lightweight | Medium | Heavyweight |
|----------------|-------------|---------|-------------|
| 0 | 0.51 | 0.37 | 0.28 |
| 1 | 0.22 | 0.20 | 0.17 |
| 2 | 0.11 | 0.13 | 0.13 |
| 3 | 0.06 | 0.09 | 0.10 |
| 4 | 0.04 | 0.06 | 0.08 |
| 6 | 0.02 | 0.04 | 0.06 |
| 8 | 0.01 | 0.03 | 0.05 |
| 12 | 0.01 | 0.02 | 0.03 |
{{< /table >}}

Note that RTF values sum to 1.0, indicating that all radiant energy eventually becomes cooling load.

### RTS Calculation Steps

#### Step 1: Calculate Hourly Heat Gains

For each hour, calculate all heat gain components:

**Opaque Surfaces (Walls, Roofs):**
{{< formula display="true" >}}
$$Q_{wall} = U \cdot A \cdot (CLTD)$$
{{< /formula >}}

Where CLTD (Cooling Load Temperature Difference) incorporates sol-air temperature effects and thermal mass.

**Windows (Conduction):**
{{< formula display="true" >}}
$$Q_{window,cond} = U \cdot A \cdot (T_{outdoor} - T_{indoor})$$
{{< /formula >}}

**Windows (Solar Radiation):**
{{< formula display="true" >}}
$$Q_{window,solar} = A \cdot SHGC \cdot I_{solar} \cdot CLF_{solar}$$
{{< /formula >}}

Where:
- $SHGC$ = Solar Heat Gain Coefficient (dimensionless)
- $I_{solar}$ = incident solar radiation (W/m²)
- $CLF_{solar}$ = Cooling Load Factor for solar gains

**Internal Gains:**

Lights:
{{< formula display="true" >}}
$$Q_{lights} = W_{lights} \cdot F_{use} \cdot F_{ballast}$$
{{< /formula >}}

Equipment:
{{< formula display="true" >}}
$$Q_{equipment} = W_{equipment} \cdot F_{use} \cdot F_{radiation}$$
{{< /formula >}}

Occupants:
{{< formula display="true" >}}
$$Q_{people,sensible} = N \cdot q_{sensible,person}$$
$$Q_{people,latent} = N \cdot q_{latent,person}$$
{{< /formula >}}

**Infiltration/Ventilation:**
{{< formula display="true" >}}
$$Q_{inf,sensible} = 1.23 \cdot \dot{V} \cdot (T_{outdoor} - T_{indoor})$$
$$Q_{inf,latent} = 3010 \cdot \dot{V} \cdot (\omega_{outdoor} - \omega_{indoor})$$
{{< /formula >}}

#### Step 2: Separate Radiant and Convective Components

For each heat gain, apply radiant/convective split factors:

{{< table >}}
| Heat Gain Source | Radiant Fraction | Convective Fraction |
|------------------|------------------|---------------------|
| Solar through glass | 100% | 0% |
| Lights (recessed) | 50-60% | 40-50% |
| Lights (suspended) | 60-70% | 30-40% |
| Office equipment | 10-30% | 70-90% |
| Occupants (seated) | 40% | 60% |
| Walls, roofs | 60% | 40% |
{{< /table >}}

#### Step 3: Apply Radiant Time Series

For each radiant heat gain component at each hour, distribute the gain to future hours using RTFs:

{{< formula display="true" >}}
$$Q_{cooling,\theta} = \sum_{j=0}^{23} Q_{radiant,\theta-j} \cdot RTF_{j}$$
{{< /formula >}}

Convective gains become cooling load immediately (RTF = 1.0 at hour 0).

#### Step 4: Sum All Components

At each hour, the total cooling load equals:

{{< formula display="true" >}}
$$Q_{total,\theta} = Q_{convective,\theta} + Q_{radiant,delayed,\theta} + Q_{infiltration,\theta}$$
{{< /formula >}}

#### Step 5: Identify Design Cooling Load

The design cooling load equals the maximum hourly load across the design day. This peak typically occurs 2-4 hours after peak solar gain due to thermal mass effects.

## Load Components: Detailed Analysis

### Walls and Roofs

Opaque envelope elements contribute to cooling loads through conduction driven by outdoor-indoor temperature difference and solar radiation absorbed at exterior surfaces.

**Design Parameters:**

U-value (Overall Thermal Transmittance):
- Wood frame wall, R-13 insulation: U = 0.35 W/m²·K (0.062 Btu/h·ft²·°F)
- Masonry wall, R-10 insulation: U = 0.45 W/m²·K (0.079 Btu/h·ft²·°F)
- Built-up roof, R-19 insulation: U = 0.27 W/m²·K (0.048 Btu/h·ft²·°F)
- Concrete roof, R-15 insulation: U = 0.34 W/m²·K (0.060 Btu/h·ft²·°F)

Solar Absorptance:
- Light colors (white, cream): α = 0.3-0.5
- Medium colors (tan, gray): α = 0.5-0.7
- Dark colors (brown, dark gray): α = 0.7-0.9
- Very dark (black, dark blue): α = 0.9-0.95

**Thermal Mass Effects:**

Heavy construction (mass $> 150$ kg/m²) delays and reduces peak heat gain compared to light construction (mass $< 50$ kg/m²):

- Peak reduction: 20-40%
- Time delay: 4-8 hours
- Daily heat gain: Similar total, but distributed over time

### Windows and Glazing

Fenestration represents the dominant cooling load component in most buildings due to direct solar heat gain and higher U-values compared to insulated walls.

**U-value (Thermal Transmittance):**

{{< table >}}
| Glazing Type | U-value (W/m²·K) | U-value (Btu/h·ft²·°F) |
|--------------|------------------|------------------------|
| Single clear | 5.8 | 1.04 |
| Double clear, air fill | 2.7 | 0.48 |
| Double clear, argon fill | 2.4 | 0.42 |
| Double low-e, argon fill | 1.7 | 0.30 |
| Triple low-e, argon fill | 1.0 | 0.18 |
{{< /table >}}

**SHGC (Solar Heat Gain Coefficient):**

SHGC quantifies the fraction of incident solar radiation that enters through the window as heat:

{{< formula display="true" >}}
$$SHGC = \frac{Q_{solar,transmitted} + Q_{solar,absorbed,re-radiated}}{Q_{solar,incident}}$$
{{< /formula >}}

{{< table >}}
| Glazing Type | SHGC | Visible Transmittance |
|--------------|------|----------------------|
| Single clear | 0.86 | 0.90 |
| Double clear | 0.76 | 0.81 |
| Double bronze tint | 0.62 | 0.61 |
| Double low-e, high solar gain | 0.70 | 0.75 |
| Double low-e, low solar gain | 0.40 | 0.70 |
| Triple low-e, low solar gain | 0.27 | 0.65 |
{{< /table >}}

**Solar Heat Gain:**

The instantaneous solar heat gain through glazing follows:

{{< formula display="true" >}}
$$Q_{solar} = A_{glazing} \cdot SHGC \cdot I_{solar} \cdot IAC$$
{{< /formula >}}

Where:
- $A_{glazing}$ = net glazing area (m²)
- $I_{solar}$ = total incident solar radiation (W/m²)
- $IAC$ = Interior Attenuation Coefficient accounting for interior shading

IAC values:
- No interior shading: IAC = 1.0
- Light-colored venetian blinds: IAC = 0.60-0.70
- Medium-colored roller shade: IAC = 0.65-0.75
- Draperies, closed weave: IAC = 0.45-0.60

**Window Orientation Effects:**

Solar heat gain varies dramatically with orientation due to sun position:

{{< table >}}
| Orientation | Peak Solar Gain (W/m²) | Time of Peak |
|-------------|------------------------|--------------|
| South | 150-200 | Noon-1 PM |
| North | 40-80 | 10 AM-2 PM |
| East | 400-500 | 8-9 AM |
| West | 400-500 | 4-5 PM |
| Horizontal (skylight) | 600-800 | Noon-1 PM |
{{< /table >}}

Values shown for 40°N latitude, clear sky, summer design day.

### Infiltration and Ventilation

Air exchange with outdoors brings both sensible (temperature) and latent (humidity) loads.

**Infiltration Rate Estimation:**

Crack method:
{{< formula display="true" >}}
$$\dot{V}_{inf} = \sum (L_{crack} \cdot C_{crack} \cdot \Delta P^{n})$$
{{< /formula >}}

Where:
- $L_{crack}$ = total crack length (m)
- $C_{crack}$ = flow coefficient (m³/s·Pa^n per m)
- $\Delta P$ = pressure difference (Pa)
- $n$ = pressure exponent (≈ 0.65)

Air changes per hour (ACH) method:
{{< formula display="true" >}}
$$\dot{V}_{inf} = \frac{ACH \cdot V_{zone}}{3600}$$
{{< /formula >}}

Where $V_{zone}$ is zone volume (m³).

Typical infiltration rates:
- Tight construction: 0.1-0.3 ACH
- Average construction: 0.3-0.6 ACH
- Loose construction: 0.6-1.5 ACH

**Ventilation Requirements:**

ASHRAE Standard 62.1 specifies minimum outdoor air ventilation rates:

{{< formula display="true" >}}
$$\dot{V}_{OA} = R_{p} \cdot P_{z} + R_{a} \cdot A_{z}$$
{{< /formula >}}

Where:
- $R_{p}$ = outdoor air rate per person (L/s·person or CFM/person)
- $P_{z}$ = zone population
- $R_{a}$ = outdoor air rate per unit area (L/s·m² or CFM/ft²)
- $A_{z}$ = zone floor area

{{< table >}}
| Space Type | R_p (L/s·person) | R_a (L/s·m²) |
|------------|------------------|--------------|
| Office space | 2.5 | 0.3 |
| Conference room | 2.5 | 0.3 |
| Classroom | 3.8 | 0.3 |
| Retail | 3.8 | 0.3 |
| Dining room | 3.8 | 0.9 |
{{< /table >}}

**Load Calculation:**

Sensible load:
{{< formula display="true" >}}
$$Q_{vent,sensible} = 1.23 \cdot \dot{V}_{OA} \cdot (T_{outdoor} - T_{indoor})$$
{{< /formula >}}

Latent load:
{{< formula display="true" >}}
$$Q_{vent,latent} = 3010 \cdot \dot{V}_{OA} \cdot (\omega_{outdoor} - \omega_{indoor})$$
{{< /formula >}}

Where $\dot{V}_{OA}$ is in L/s, temperatures in °C, and humidity ratios in kg/kg.

### Occupants

People generate both sensible and latent heat that varies with activity level.

{{< table >}}
| Activity Level | Total Heat (W) | Sensible (W) | Latent (W) | Sensible Fraction |
|----------------|----------------|--------------|------------|------------------|
| Seated, quiet | 100 | 60 | 40 | 0.60 |
| Seated, light work | 115 | 65 | 50 | 0.57 |
| Standing, light work | 140 | 70 | 70 | 0.50 |
| Walking slowly | 160 | 75 | 85 | 0.47 |
| Light bench work | 235 | 90 | 145 | 0.38 |
| Moderate dancing | 265 | 95 | 170 | 0.36 |
| Heavy work | 440 | 170 | 270 | 0.39 |
{{< /table >}}

The sensible heat splits approximately 60% radiant and 40% convective for most activities.

**Diversity Factor:**

Design occupancy rarely equals maximum possible occupancy. Apply diversity factors based on building type:

- Office buildings: 0.75-0.85 (75-85% of maximum)
- Schools: 1.0 (assume full)
- Retail: 0.5-0.7
- Auditoriums: 1.0
- Restaurants: 0.6-0.8

### Equipment

Office equipment, appliances, and process loads contribute both sensible and sometimes latent heat.

**Nameplate vs Actual Load:**

Equipment rarely operates at full nameplate capacity. Use factors:

{{< formula display="true" >}}
$$Q_{equipment} = W_{nameplate} \cdot F_{use} \cdot F_{load}$$
{{< /formula >}}

Where:
- $F_{use}$ = usage factor (fraction of time in use)
- $F_{load}$ = load factor (fraction of full capacity when in use)

{{< table >}}
| Equipment Type | W/unit | F_use | F_load | Radiant Fraction |
|----------------|--------|-------|--------|------------------|
| Desktop computer | 150 | 0.50 | 0.40 | 0.10 |
| Laptop computer | 50 | 0.50 | 0.40 | 0.10 |
| LCD monitor | 50 | 0.50 | 1.00 | 0.15 |
| Laser printer | 600 | 0.05 | 0.30 | 0.10 |
| Copier | 1500 | 0.10 | 0.30 | 0.20 |
| Coffee maker | 1000 | 0.20 | 0.35 | 0.30 |
| Vending machine | 400 | 1.00 | 1.00 | 0.50 |
{{< /table >}}

### Lighting

Lighting heat gain depends on installed wattage, ballast/driver losses, and radiant/convective split.

{{< formula display="true" >}}
$$Q_{lighting} = W_{lamps} \cdot F_{ballast} \cdot F_{use} \cdot F_{space}$$
{{< /formula >}}

Where:
- $W_{lamps}$ = total lamp wattage
- $F_{ballast}$ = ballast/driver factor
- $F_{use}$ = usage factor
- $F_{space}$ = fraction to conditioned space (vs plenum)

{{< table >}}
| Lighting Type | F_ballast | Radiant Fraction | Convective Fraction |
|---------------|-----------|------------------|---------------------|
| Incandescent | 1.00 | 0.80 | 0.20 |
| Fluorescent T8 | 1.10-1.20 | 0.50-0.60 | 0.40-0.50 |
| LED | 1.00 | 0.50-0.60 | 0.40-0.50 |
| Metal halide | 1.15-1.25 | 0.50 | 0.50 |
{{< /table >}}

For recessed fixtures in lay-in ceiling with return air plenum, a significant fraction of heat (30-60%) enters the plenum rather than the space, reducing cooling load.

## Peak Load vs Block Load

Load calculation methodology distinguishes between peak loads for individual zones and block loads for central equipment.

### Peak Zone Load

The peak cooling load for each zone occurs at the specific hour when that zone experiences maximum heat gain. Different zones peak at different times based on:

- Orientation (east zones peak morning, west zones peak afternoon)
- Internal gain schedules
- Solar exposure
- Thermal mass

Terminal equipment (VAV boxes, fan coils, zone RTUs) sizes to individual zone peak loads.

### Block Load

The block load represents the simultaneous cooling load on central equipment (chillers, central air handlers) when summing all zones at a single point in time. The block peak occurs when the sum of all zone loads reaches maximum.

The block peak load is always less than the sum of individual zone peaks due to non-coincidence:

{{< formula display="true" >}}
$$Q_{block,peak} < \sum_{zones} Q_{zone,peak}$$
{{< /formula >}}

**Diversity Factor:**

{{< formula display="true" >}}
$$DF = \frac{Q_{block,peak}}{\sum_{zones} Q_{zone,peak}}$$
{{< /formula >}}

Typical diversity factors range from 0.75-0.90 depending on building size, configuration, and use.

{{< diagram >}}
graph LR
    A[East Zone<br/>Peak 9 AM<br/>10 tons] --> D[Block Load]
    B[South Zone<br/>Peak 1 PM<br/>12 tons] --> D
    C[West Zone<br/>Peak 4 PM<br/>11 tons] --> D
    D -->|Diversity Factor<br/>0.85| E[Central Chiller<br/>Size: 28 tons<br/>vs 33 tons sum]

    style A fill:#ffcccc
    style B fill:#ffcccc
    style C fill:#ffcccc
    style E fill:#99ccff
{{< /table >}}

## Diversity Factors

Diversity factors account for the statistical improbability that all loads occur simultaneously at maximum.

### Sources of Diversity

**Temporal Diversity:**
- Different orientations peak at different solar times
- Internal gains follow occupancy and usage schedules
- Thermal mass creates time lags between zones

**Operational Diversity:**
- Not all equipment operates simultaneously at full load
- Occupancy varies by zone and time
- Lighting controlled by daylight sensors or occupancy

**Probability Diversity:**
- Peak outdoor temperature rarely coincides with peak solar radiation
- Peak internal gains rarely coincide with peak envelope loads

### Application of Diversity

Apply diversity factors in a hierarchical manner:

1. Equipment-level: Individual equipment actual vs nameplate load
2. Zone-level: Zone peak vs sum of component peaks
3. System-level: System peak vs sum of zone peaks
4. Plant-level: Plant peak vs sum of system peaks

{{< table >}}
| Level | Typical Diversity Factor | Application |
|-------|-------------------------|-------------|
| Individual equipment | 0.30-0.60 | Computers, office equipment |
| Zone components | 0.85-0.95 | Sum of lights, equipment, people |
| Multiple zones to system | 0.75-0.90 | Central air handler sizing |
| Multiple systems to plant | 0.80-0.95 | Chiller plant sizing |
{{< /table >}}

Excessive diversity factors risk undersizing equipment, while insufficient diversity wastes capital and energy. Actual building operating data provides the best calibration for diversity assumptions.

## ASHRAE Methods: Comparison and Selection

### Manual J (Residential)

**Application:** Residential buildings, typically single-family homes and small multi-family.

**Methodology:**
- Simplified steady-state calculation
- Envelope loads use U·A·ΔT with design temperature differences
- Windows use U·A·ΔT plus solar heat gain factor (SHGF)
- Duct losses explicitly calculated
- No hourly simulation; single peak design condition

**Advantages:**
- Simple calculation process
- Standardized forms and worksheets
- Integrated with Manual S (equipment selection) and Manual D (duct design)
- Conservative results suitable for residential application

**Limitations:**
- No thermal mass effects
- Simplified solar calculations
- Single peak condition misses time-varying loads
- Not suitable for commercial buildings

**Design Conditions:**
Use ASHRAE 99.6% winter and 1% summer design conditions for heating and cooling respectively.

### CLTD/CLF Method (Commercial)

**Application:** Commercial buildings with manual calculation approach.

**Methodology:**
- Uses pre-calculated Cooling Load Temperature Differences (CLTD) for walls and roofs
- Uses Cooling Load Factors (CLF) for solar through glass and internal gains
- Accounts for thermal mass through CLTD values
- Accounts for time lag through CLF values

**Wall/Roof Cooling Load:**
{{< formula display="true" >}}
$$Q = U \cdot A \cdot CLTD_{corrected}$$
{{< /formula >}}

Where:
{{< formula display="true" >}}
$$CLTD_{corrected} = CLTD_{table} + (78-T_{indoor}) + (T_{outdoor,mean}-85)$$
{{< /formula >}}

(Equation shown in °F; convert 78°F = 25.6°C, 85°F = 29.4°C for SI units)

**Window Solar Load:**
{{< formula display="true" >}}
$$Q = A \cdot SHGC \cdot SC \cdot SHGF_{max} \cdot CLF$$
{{< /formula >}}

Where:
- $SC$ = Shading Coefficient (deprecated in favor of SHGC)
- $SHGF_{max}$ = maximum Solar Heat Gain Factor
- $CLF$ = Cooling Load Factor from tables

**Advantages:**
- Manual calculation feasible
- Accounts for thermal mass and time lag
- Widely used, well-documented

**Limitations:**
- Tables require interpolation
- Less accurate than hourly methods
- ASHRAE no longer updates CLTD/CLF tables
- Superseded by RTS method

### RTS Method (Commercial)

**Application:** Current ASHRAE-recommended method for commercial buildings.

**Methodology:**
- Hourly heat gain calculation
- Radiant time series for converting radiant gains to cooling loads
- Explicit thermal mass effects through RTS coefficients
- Separate radiant and convective components

**Advantages:**
- More accurate than CLTD/CLF
- Physical basis in heat transfer fundamentals
- Suitable for computer implementation
- Current ASHRAE standard

**Limitations:**
- Requires hourly calculations (software needed)
- More complex than CLTD/CLF
- Requires selection of appropriate RTS coefficients

### Transfer Function Method (TFM)

**Application:** Research, detailed analysis, buildings with complex envelope or high thermal mass.

**Methodology:**
- Most rigorous ASHRAE method
- Conduction transfer functions for dynamic heat transfer
- Hourly simulation required
- Considers complete thermal history

**Advantages:**
- Highest accuracy
- Applicable to any construction type
- Physically rigorous

**Limitations:**
- Complex calculation requiring software
- Requires detailed input data
- CTF coefficient generation non-trivial
- Largely superseded by RTS for practical applications

## Worked Example 1: Residential Cooling Load (Manual J)

**Problem Statement:**

Calculate the design cooling load for a 1600 ft² single-family residence in Phoenix, Arizona with the following characteristics:

**Building Data:**
- Dimensions: 40 ft × 40 ft, single story, 8 ft ceiling height
- Walls: Wood frame, R-13 batt insulation, light color siding
- Roof: Asphalt shingle, vented attic, R-30 insulation, medium color
- Windows: Double clear glass, 200 ft² total (15% of floor area)
  - North: 40 ft²
  - East: 60 ft²
  - South: 40 ft²
  - West: 60 ft²
- Infiltration: 0.35 ACH (average construction)
- Occupants: 4 people
- Internal gains: 1200 W lighting and equipment

**Design Conditions:**
- Outdoor: 108°F dry-bulb, 71°F wet-bulb
- Indoor: 75°F dry-bulb, 50% RH
- Daily range: 25°F

**Solution:**

### Step 1: Wall Load

Gross wall area:
$$A_{wall,gross} = Perimeter \times Height = 160 \text{ ft} \times 8 \text{ ft} = 1280 \text{ ft}^2$$

Net wall area:
$$A_{wall,net} = 1280 - 200 = 1080 \text{ ft}^2$$

For wood frame wall with R-13 insulation:
$$U_{wall} = 0.084 \text{ Btu/h·ft}^2\text{·°F}$$

Design temperature difference with solar effect (Manual J Table):
For light color wall in Phoenix, summer design hour 3 PM:
$$\Delta T_{wall} = 108 - 75 + 15 = 48°\text{F}$$

(The +15°F accounts for solar radiation on walls)

Wall cooling load:
{{< formula display="true" >}}
$$Q_{wall} = U \cdot A \cdot \Delta T = 0.084 \times 1080 \times 48 = 4354 \text{ Btu/h}$$
{{< /formula >}}

### Step 2: Roof/Ceiling Load

Ceiling area:
$$A_{ceiling} = 40 \times 40 = 1600 \text{ ft}^2$$

For vented attic with R-30 ceiling insulation:
$$U_{ceiling} = 0.030 \text{ Btu/h·ft}^2\text{·°F}$$

Design temperature difference (Manual J Table for Phoenix):
$$\Delta T_{ceiling} = 47°\text{F}$$

(This accounts for attic temperature rise above outdoor due to solar heating)

Ceiling cooling load:
{{< formula display="true" >}}
$$Q_{ceiling} = 0.030 \times 1600 \times 47 = 2256 \text{ Btu/h}$$
{{< /formula >}}

### Step 3: Window Conduction Load

For double clear glass:
$$U_{window} = 0.49 \text{ Btu/h·ft}^2\text{·°F}$$

Temperature difference:
$$\Delta T = 108 - 75 = 33°\text{F}$$

Window conduction load:
{{< formula display="true" >}}
$$Q_{window,cond} = 0.49 \times 200 \times 33 = 3234 \text{ Btu/h}$$
{{< /formula >}}

### Step 4: Window Solar Load

Solar heat gain factors (SHGF) for Phoenix, July 3 PM, double clear glass (Manual J Tables):

{{< table >}}
| Orientation | Area (ft²) | SHGF (Btu/h·ft²) | Load (Btu/h) |
|-------------|-----------|------------------|--------------|
| North | 40 | 19 | 760 |
| East | 60 | 32 | 1920 |
| South | 40 | 34 | 1360 |
| West | 60 | 216 | 12960 |
| **Total** | **200** | - | **17000** |
{{< /table >}}

Note the extreme west window load due to afternoon sun in Phoenix.

### Step 5: Infiltration Load

Volume:
$$V = 1600 \times 8 = 12800 \text{ ft}^3$$

Infiltration rate:
$$\dot{V}_{inf} = \frac{0.35 \times 12800}{60} = 74.7 \text{ CFM}$$

Sensible infiltration load:
{{< formula display="true" >}}
$$Q_{inf,sensible} = 1.08 \times 74.7 \times (108-75) = 2663 \text{ Btu/h}$$
{{< /formula >}}

For latent load, determine humidity ratios:
- Outdoor (108°F DB, 71°F WB): $\omega_o = 0.0088$ lb/lb
- Indoor (75°F DB, 50% RH): $\omega_i = 0.0093$ lb/lb

Surprisingly, indoor humidity is higher than outdoor in this Phoenix example, so:
{{< formula display="true" >}}
$$Q_{inf,latent} = 0.68 \times 74.7 \times (88-93) \times 7000 = -1780 \text{ Btu/h}$$
{{< /formula >}}

The negative latent load indicates dehumidification is not required; outdoor air in Phoenix is dry. Set latent infiltration load to zero.

### Step 6: Internal Gains

Occupants (4 people, seated, light activity):
- Sensible: $4 \times 230 = 920$ Btu/h
- Latent: $4 \times 190 = 760$ Btu/h

Lights and equipment:
{{< formula display="true" >}}
$$Q_{internal} = 1200 \text{ W} \times 3.412 = 4094 \text{ Btu/h}$$
{{< /formula >}}

Assume 75% sensible, 25% latent for mixed equipment:
- Sensible: $4094 \times 0.75 = 3071$ Btu/h
- Latent: $4094 \times 0.25 = 1024$ Btu/h

### Step 7: Total Load Summary

{{< table >}}
| Component | Sensible (Btu/h) | Latent (Btu/h) |
|-----------|------------------|----------------|
| Walls | 4354 | - |
| Ceiling | 2256 | - |
| Windows (conduction) | 3234 | - |
| Windows (solar) | 17000 | - |
| Infiltration | 2663 | 0 |
| Occupants | 920 | 760 |
| Equipment | 3071 | 1024 |
| **Subtotal** | **33498** | **1784** |
| **Total Load** | **35282 Btu/h (2.94 tons)** | |
{{< /table >}}

Sensible Heat Ratio:
{{< formula display="true" >}}
$$SHR = \frac{33498}{35282} = 0.95$$
{{< /formula >}}

**Equipment Selection:**

Select 3-ton (36,000 Btu/h) cooling equipment. The high SHR (0.95) is typical for hot-dry climates like Phoenix. Verify selected equipment SHR matches load SHR.

Add duct losses (typically 10-25% depending on duct location):
- Ducts in unconditioned attic: apply 25% gain
- Total capacity required: $35282 \times 1.25 = 44103$ Btu/h

Select 4-ton system (48,000 Btu/h) when accounting for duct losses.

## Worked Example 2: Commercial Office Space (RTS Method)

**Problem Statement:**

Calculate the design cooling load for a perimeter office zone in Chicago, Illinois using the Radiant Time Series method.

**Building Data:**
- Zone: South-facing perimeter office, 4th floor
- Dimensions: 30 ft × 15 ft × 9 ft ceiling (450 ft², 4050 ft³)
- Exterior wall: 30 ft wide × 9 ft high = 270 ft²
  - Construction: 4" brick + 2" polyiso (R-13) + 8" concrete block
  - U-value: 0.082 Btu/h·ft²·°F
  - Dark brick, absorptance α = 0.85
- Window: 30 ft wide × 4 ft high = 120 ft²
  - Double low-e, argon fill
  - U-value: 0.30 Btu/h·ft²·°F, SHGC: 0.40
  - Interior light-colored blinds (IAC = 0.65)
- Floor and ceiling: interior (adiabatic)
- Lighting: 1.0 W/ft² (450 W total), recessed LED, operates 7 AM - 6 PM
- Equipment: 150 W computer, 50 W monitor per workstation, 4 workstations
  - Operates 8 AM - 5 PM with 0.5 diversity
- Occupants: 4 people, seated office work
  - Occupancy 8 AM - 5 PM
- Outdoor air ventilation: 15 CFM per person = 60 CFM
- Construction type: Medium weight (concrete block)

**Design Conditions:**
- Chicago summer design day, July 21
- Outdoor: 91°F dry-bulb, 74°F wet-bulb (1% design)
- Indoor: 75°F, 50% RH
- Daily temperature range: 15°F

**Solution:**

### Step 1: Hourly Outdoor Conditions

Generate hourly outdoor temperatures using ASHRAE design day profile:

{{< table >}}
| Hour | T_outdoor (°F) | T_sol-air (°F) | I_solar,south (Btu/h·ft²) |
|------|----------------|----------------|---------------------------|
| 6 | 77 | 76 | 12 |
| 7 | 78 | 77 | 64 |
| 8 | 80 | 82 | 136 |
| 9 | 83 | 91 | 188 |
| 10 | 86 | 99 | 219 |
| 11 | 88 | 104 | 234 |
| 12 | 90 | 106 | 238 |
| 13 | 91 | 106 | 230 |
| 14 | 91 | 103 | 211 |
| 15 | 90 | 97 | 181 |
| 16 | 89 | 90 | 141 |
| 17 | 87 | 85 | 90 |
| 18 | 85 | 82 | 31 |
{{< /table >}}

Sol-air temperature for dark brick wall (α = 0.85):
{{< formula display="true" >}}
$$T_{sol-air} = T_{outdoor} + \frac{0.85 \times I_{solar,south}}{4.0} - 7°\text{F}$$
{{< /formula >}}

The -7°F accounts for long-wave radiation to sky (ΔR/h₀).

### Step 2: Wall Conduction Heat Gain

Net wall area (excluding window):
$$A_{wall} = 270 - 120 = 150 \text{ ft}^2$$

Hourly wall heat gain using CLTD approximation for medium-weight wall:
{{< formula display="true" >}}
$$Q_{wall,\theta} = U \cdot A \cdot (T_{sol-air,\theta} - T_{indoor})$$
{{< /formula >}}

Example for hour 12 (noon):
$$Q_{wall,12} = 0.082 \times 150 \times (106 - 75) = 381 \text{ Btu/h}$$

Wall heat gain is approximately 60% radiant, 40% convective.

### Step 3: Window Conduction Heat Gain

{{< formula display="true" >}}
$$Q_{window,cond,\theta} = U \cdot A \cdot (T_{outdoor,\theta} - T_{indoor})$$
{{< /formula >}}

Example for hour 13 (1 PM, peak outdoor temperature):
$$Q_{window,cond,13} = 0.30 \times 120 \times (91 - 75) = 576 \text{ Btu/h}$$

Window conduction is 100% convective (immediate cooling load).

### Step 4: Window Solar Heat Gain

{{< formula display="true" >}}
$$Q_{solar,\theta} = A \cdot SHGC \cdot IAC \cdot I_{solar,\theta}$$
{{< /formula >}}

Example for hour 12:
$$Q_{solar,12} = 120 \times 0.40 \times 0.65 \times 238 = 7430 \text{ Btu/h}$$

Solar heat gain is 100% radiant (applies RTS for time delay).

### Step 5: Lighting Heat Gain

{{< formula display="true" >}}
$$Q_{lights} = 450 \text{ W} \times 3.412 = 1535 \text{ Btu/h}$$
{{< /formula >}}

Hours 7-18 (7 AM - 6 PM): 1535 Btu/h
Other hours: 0 Btu/h

For recessed LED fixtures: 60% radiant, 40% convective.

### Step 6: Equipment Heat Gain

Per workstation: 150 W (computer) + 50 W (monitor) = 200 W
Total: $4 \times 200 = 800$ W = 2730 Btu/h

With 0.5 diversity factor: $2730 \times 0.5 = 1365$ Btu/h

Hours 8-17 (8 AM - 5 PM): 1365 Btu/h
Other hours: 0 Btu/h

Office equipment: 10% radiant, 90% convective.

### Step 7: Occupant Heat Gain

4 people, seated office work:
- Sensible: $4 \times 250 = 1000$ Btu/h (245 Btu/h per person)
- Latent: $4 \times 200 = 800$ Btu/h

Hours 8-17: Full occupancy
Other hours: 0

Occupant sensible: 60% radiant, 40% convective.

### Step 8: Ventilation Load

Outdoor air: 60 CFM

Sensible load at hour 13:
{{< formula display="true" >}}
$$Q_{vent,sensible} = 1.08 \times 60 \times (91-75) = 1037 \text{ Btu/h}$$
{{< /formula >}}

For latent load, determine humidity ratios:
- Outdoor (91°F DB, 74°F WB): ω₀ = 0.0116 lb/lb
- Indoor (75°F, 50% RH): ω_i = 0.0093 lb/lb

Latent load:
{{< formula display="true" >}}
$$Q_{vent,latent} = 0.68 \times 60 \times (116-93) \times 7000 = 6552 \text{ Btu/h}$$
{{< /formula >}}

Ventilation loads are 100% convective (immediate cooling load).

### Step 9: Apply Radiant Time Series

For medium-weight construction, south-facing perimeter zone, use RTS coefficients:

{{< table >}}
| Hour | RTF_0 | RTF_1 | RTF_2 | RTF_3 | RTF_4 |
|------|-------|-------|-------|-------|-------|
| | 0.37 | 0.20 | 0.13 | 0.09 | 0.06 |
{{< /table >}}

(Additional hours with smaller coefficients omitted for brevity)

For each radiant heat gain component at each hour, apply:
{{< formula display="true" >}}
$$Q_{cooling,\theta} = \sum_{j=0}^{n} Q_{radiant,\theta-j} \cdot RTF_{j}$$
{{< /formula >}}

**Example calculation for solar gain at hour 14 (2 PM):**

Solar radiant gains:
- Hour 14: 7146 Btu/h
- Hour 13: 7430 Btu/h
- Hour 12: 7430 Btu/h
- Hour 11: 7314 Btu/h
- Hour 10: 6840 Btu/h

Cooling load from solar at hour 14:
{{< formula display="true" >}}
\begin{align}
Q_{solar,cooling,14} &= 7146 \times 0.37 + 7430 \times 0.20 \\
&\quad + 7430 \times 0.13 + 7314 \times 0.09 + 6840 \times 0.06 + \ldots \\
&= 2644 + 1486 + 966 + 658 + 410 + \ldots \\
&= 6164 \text{ Btu/h}
\end{align}
{{< /formula >}}

Note that the 7146 Btu/h instantaneous solar gain at hour 14 becomes only 6164 Btu/h cooling load due to thermal mass storage effects.

### Step 10: Total Hourly Cooling Loads

Sum all components (convective immediately + radiant delayed) for each hour:

{{< table >}}
| Hour | Wall | Window Cond | Solar | Lights | Equip | People Sens | People Lat | Vent Sens | Vent Lat | Total |
|------|------|-------------|-------|--------|-------|-------------|------------|-----------|----------|-------|
| 8 | 182 | 180 | 3024 | 768 | 1228 | 600 | 800 | 324 | 6552 | 13658 |
| 9 | 244 | 288 | 4140 | 768 | 1228 | 600 | 800 | 540 | 6552 | 15160 |
| 10 | 312 | 396 | 5154 | 768 | 1228 | 600 | 800 | 756 | 6552 | 16566 |
| 11 | 367 | 468 | 5964 | 768 | 1228 | 600 | 800 | 900 | 6552 | 17647 |
| 12 | 405 | 540 | 6438 | 768 | 1228 | 600 | 800 | 1008 | 6552 | 18339 |
| 13 | 418 | 576 | 6594 | 768 | 1228 | 600 | 800 | 1037 | 6552 | **18573** |
| 14 | 411 | 576 | 6457 | 768 | 1228 | 600 | 800 | 1037 | 6552 | 18429 |
| 15 | 384 | 540 | 6052 | 768 | 1228 | 600 | 800 | 1008 | 6552 | 17932 |
| 16 | 344 | 504 | 5461 | 768 | 1228 | 600 | 800 | 972 | 6552 | 17229 |
| 17 | 297 | 432 | 4719 | 768 | 1228 | 600 | 800 | 900 | 6552 | 16296 |
| 18 | 259 | 360 | 3909 | 614 | 0 | 0 | 0 | 828 | 0 | 5970 |
{{< /table >}}

(Values shown in Btu/h; some components combined in table for clarity)

**Peak Cooling Load: 18,573 Btu/h at 1 PM (hour 13)**

Breakdown:
- Sensible: 12,021 Btu/h
- Latent: 6,552 Btu/h
- SHR: 0.65

### Step 11: Equipment Selection

Zone cooling load: 18,573 Btu/h = 1.55 tons

This would be the capacity required for a VAV terminal box, fan coil unit, or zone RTU serving this space.

**Key Observations:**

1. Peak load occurs at 1 PM, one hour after peak solar radiation (noon) due to thermal mass effects captured by RTS method.

2. Ventilation latent load (6,552 Btu/h) dominates during occupied hours, representing 35% of total load. This is characteristic of Chicago's humid summer climate.

3. Solar gain through south windows, even with low-e glazing and interior shading, represents the largest single component (6,594 Btu/h at peak).

4. The medium-weight construction reduces and delays peak loads compared to lightweight construction, which would show peak loads closer to peak solar gain time.

## Heating Load Calculations

Heating loads follow simpler calculation procedures than cooling loads because:
- Solar gains and thermal mass effects work in favor (reduce heating load)
- Design condition represents steady-state (coldest hour, no sun)
- No latent load (humidification handled separately if required)
- Internal gains credited against heat loss

### Basic Heating Load Equation

{{< formula display="true" >}}
$$Q_{heating} = Q_{envelope} + Q_{infiltration} - Q_{internal}$$
{{< /formula >}}

Where:
- $Q_{envelope}$ = transmission losses through envelope
- $Q_{infiltration}$ = heat loss from air leakage
- $Q_{internal}$ = internal heat gains (lights, equipment, people)

### Envelope Heat Loss

For each building element:
{{< formula display="true" >}}
$$Q_{envelope} = U \cdot A \cdot (T_{indoor} - T_{outdoor,design})$$
{{< /formula >}}

Use ASHRAE 99.6% winter design temperature (temperature exceeded 99.6% of hours annually, representing very cold but not extreme conditions).

{{< table >}}
| Location | 99.6% Design Temp (°F) | 99% Design Temp (°F) |
|----------|------------------------|----------------------|
| Minneapolis, MN | -16 | -12 |
| Chicago, IL | -7 | -2 |
| New York, NY | 11 | 15 |
| Denver, CO | -2 | 4 |
| Atlanta, GA | 22 | 26 |
{{< /table >}}

### Infiltration Heat Loss

{{< formula display="true" >}}
$$Q_{infiltration} = 1.08 \cdot \dot{V} \cdot (T_{indoor} - T_{outdoor})$$
{{< /formula >}}

Where $\dot{V}$ is in CFM and temperatures in °F.

Winter infiltration rates typically exceed summer rates due to:
- Larger indoor-outdoor temperature difference (stack effect)
- Wind effects more pronounced
- Building envelope contraction creating additional gaps

Apply winter infiltration multiplier: 1.2-1.5 times summer infiltration rate.

### Internal Heat Gain Credit

During occupied hours, credit internal gains against heating load:

{{< formula display="true" >}}
$$Q_{net,heating} = Q_{envelope} + Q_{infiltration} - (Q_{lights} + Q_{equipment} + Q_{people,sensible})$$
{{< /formula >}}

For unoccupied design condition (night setback), internal gains equal zero.

Most residential and some commercial heating load calculations use unoccupied conditions (no internal gain credit) for conservative sizing.

### Worked Example 3: Residential Heating Load

Using the same Phoenix residence from Example 1, calculate heating load for design condition:
- Outdoor: 34°F (Phoenix 99.6% design temperature)
- Indoor: 70°F
- No sun (night design condition)
- Unoccupied (no internal gain credit)

**Envelope Losses:**

Walls:
$$Q_{wall} = 0.084 \times 1080 \times (70-34) = 3265 \text{ Btu/h}$$

Ceiling:
$$Q_{ceiling} = 0.030 \times 1600 \times (70-34) = 1728 \text{ Btu/h}$$

Windows:
$$Q_{window} = 0.49 \times 200 \times (70-34) = 3528 \text{ Btu/h}$$

Floor (slab-on-grade, perimeter):
For uninsulated slab, perimeter = 160 ft:
$$Q_{floor} = F_{2} \times P \times (T_{indoor} - T_{outdoor,design})$$

Where $F_2$ = 0.68 Btu/h·ft·°F for uninsulated slab (ASHRAE value):
$$Q_{floor} = 0.68 \times 160 \times (70-34) = 3917 \text{ Btu/h}$$

**Infiltration Loss:**

Winter infiltration (apply 1.3 multiplier to summer rate):
$$\dot{V}_{inf,winter} = 74.7 \times 1.3 = 97 \text{ CFM}$$

{{< formula display="true" >}}
$$Q_{infiltration} = 1.08 \times 97 \times (70-34) = 3772 \text{ Btu/h}$$
{{< /formula >}}

**Total Heating Load:**

{{< table >}}
| Component | Heat Loss (Btu/h) |
|-----------|------------------|
| Walls | 3265 |
| Ceiling | 1728 |
| Windows | 3528 |
| Floor | 3917 |
| Infiltration | 3772 |
| **Total** | **16210** |
{{< /table >}}

Heating load: 16,210 Btu/h

Note that heating load (16,210 Btu/h) is much smaller than cooling load (35,282 Btu/h) for this Phoenix residence. This climate characteristic drives equipment selection toward cooling-optimized heat pumps rather than heating-optimized furnaces.

## Conclusion

HVAC load calculations form the foundation of system design, directly impacting equipment selection, energy performance, and occupant comfort. Accurate calculations require:

1. Understanding fundamental heat transfer mechanisms (conduction, convection, radiation)
2. Distinguishing sensible and latent loads
3. Applying appropriate calculation methods (Manual J for residential, RTS for commercial)
4. Accounting for all load components (envelope, solar, internal gains, ventilation)
5. Recognizing thermal mass and time-delay effects
6. Applying diversity factors appropriately
7. Using proper design conditions from ASHRAE climate data

Modern building energy codes increasingly require detailed load calculations to demonstrate compliance with energy efficiency requirements. Software tools implement ASHRAE methods (particularly RTS) for commercial buildings, while standardized worksheets serve residential applications using Manual J.

The transition from simple steady-state methods (early Manual J, CLTD/CLF) to dynamic hourly methods (RTS, TFM) reflects improved understanding of building thermal physics and increased computing capability. These rigorous methods enable right-sizing of equipment, avoiding the energy waste and comfort problems associated with oversizing that characterized past practice.

Proper load calculation represents an engineering fundamental that separates professional HVAC design from rules-of-thumb approximation. The time invested in thorough load analysis returns benefits throughout the building's operational lifetime through improved comfort, reduced energy consumption, and optimal equipment performance.

## References

- ASHRAE Handbook - Fundamentals (2021), Chapter 18: Nonresidential Cooling and Heating Load Calculations
- ASHRAE Handbook - Fundamentals (2021), Chapter 19: Residential Cooling and Heating Load Calculations
- ACCA Manual J: Residential Load Calculation (8th Edition)
- ASHRAE Standard 62.1: Ventilation for Acceptable Indoor Air Quality
- Spitler, J.D. and Fisher, D.E. (1999). On the relationship between the radiant time series and transfer function methods for design cooling load calculations. HVAC&R Research, 5(2), 125-138.
- Pedersen, C.O., Fisher, D.E., and Liesen, R.J. (1997). Development of a heat balance procedure for calculating cooling loads. ASHRAE Transactions, 103(2), 459-468.
