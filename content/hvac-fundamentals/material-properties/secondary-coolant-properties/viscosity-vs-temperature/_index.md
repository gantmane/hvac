---
title: "Viscosity vs Temperature"
aliases: ["Viscosity vs Temperature"]
description: "Temperature dependence of dynamic and kinematic viscosity in secondary coolants including glycol solutions and brines, with engineering correlations, property tables, and pumping system design implications"
weight: 3
---

## Overview

Viscosity represents the internal resistance of a fluid to flow and is one of the most temperature-sensitive properties of secondary coolants. Unlike water, glycol solutions and brines exhibit dramatic viscosity increases at low temperatures, fundamentally affecting pump selection, pressure drop calculations, heat transfer performance, and system operating costs. The viscosity-temperature relationship governs Reynolds number, flow regime transitions, and power requirements throughout the operating range.

The exponential nature of viscosity's temperature dependence requires careful analysis during system design, particularly for applications operating at temperatures below 0°F (-18°C) where viscosity can increase by factors of 10 to 50 compared to ambient conditions.

## Newtonian Behavior

Secondary coolants used in HVAC applications exhibit Newtonian fluid behavior under normal operating conditions. For Newtonian fluids, the relationship between shear stress and shear rate is linear:

τ = μ(du/dy)

Where:
- τ = shear stress (Pa or lbf/ft²)
- μ = dynamic viscosity (Pa·s or lbf·s/ft²)
- du/dy = velocity gradient perpendicular to flow direction (s⁻¹)

**Newtonian Characteristics:**
- Viscosity is independent of shear rate
- Linear stress-strain rate relationship
- Time-independent behavior
- Valid for aqueous glycol solutions (10-70% by mass)
- Valid for calcium chloride and sodium chloride brines
- Applicable across typical HVAC flow velocities (2-10 ft/s)

**Non-Newtonian Exceptions:**
- Extremely high concentrations (>80% glycol) may show slight shear-thinning
- Slurries and phase-change materials exhibit non-Newtonian behavior
- Contaminated fluids with particulates or biological growth
- Polymer-based heat transfer fluids

For standard HVAC secondary coolant calculations, Newtonian assumptions are valid, simplifying pipe flow and heat transfer analysis.

## Dynamic Viscosity Temperature Dependence

Dynamic viscosity (absolute viscosity) decreases exponentially with increasing temperature. This relationship is fundamental to understanding secondary coolant behavior across seasonal and operational temperature ranges.

### Arrhenius Equation

The most widely used correlation for viscosity-temperature dependence:

μ(T) = A × exp(B/T)

Where:
- μ(T) = dynamic viscosity at temperature T (Pa·s or cP)
- A = pre-exponential constant (Pa·s)
- B = activation energy parameter (K)
- T = absolute temperature (K)

**Alternative Form:**

ln(μ) = ln(A) + B/T

This linear form is useful for fitting experimental data and determining constants A and B from measured viscosity values.

### Vogel Equation (Fulcher-Tammann-Vogel)

Provides improved accuracy over wider temperature ranges:

μ(T) = A × exp[B/(T - T₀)]

Where:
- T₀ = Vogel temperature, typically 100-150 K below freezing point (K)
- Other parameters as defined above

The Vogel equation accounts for the temperature at which viscosity theoretically approaches infinity, providing better fit for low-temperature data.

### Temperature Coefficient of Viscosity

The fractional change in viscosity per degree temperature change:

β = -(1/μ)(dμ/dT)

For glycol solutions:
- β typically ranges from 0.02 to 0.05 K⁻¹
- Higher values at lower temperatures
- 25% propylene glycol: β ≈ 0.025 K⁻¹ at 20°F
- 50% propylene glycol: β ≈ 0.035 K⁻¹ at 0°F

A 10°F temperature drop can increase viscosity by 25-40% depending on concentration and base temperature.

## Dynamic Viscosity Property Tables

### Ethylene Glycol Solutions

| Temperature (°F) | 0% (Water) | 10% | 20% | 30% | 40% | 50% | 60% |
|------------------|------------|-----|-----|-----|-----|-----|-----|
| 60 | 1.12 | 1.31 | 1.55 | 1.93 | 2.51 | 3.48 | 5.13 |
| 40 | 1.55 | 1.85 | 2.26 | 2.91 | 3.95 | 5.70 | 8.90 |
| 20 | 2.09 | 2.56 | 3.23 | 4.31 | 6.10 | 9.35 | 15.5 |
| 0 | 2.73 | 3.46 | 4.57 | 6.40 | 9.60 | 15.6 | 27.3 |
| -20 | 3.49 | 4.60 | 6.40 | 9.50 | 15.0 | 26.0 | 48.5 |
| -40 | - | 6.10 | 8.90 | 14.0 | 23.5 | 44.0 | 88.0 |
| -60 | - | - | - | 20.5 | 37.0 | 75.0 | 165 |

*Values in centipoise (cP). 1 cP = 0.001 Pa·s = 0.000672 lbm/(ft·s)*

### Propylene Glycol Solutions

| Temperature (°F) | 0% (Water) | 10% | 20% | 30% | 40% | 50% | 60% |
|------------------|------------|-----|-----|-----|-----|-----|-----|
| 60 | 1.12 | 1.38 | 1.74 | 2.30 | 3.20 | 4.75 | 7.50 |
| 40 | 1.55 | 1.98 | 2.62 | 3.62 | 5.25 | 8.15 | 13.5 |
| 20 | 2.09 | 2.78 | 3.85 | 5.60 | 8.60 | 14.0 | 24.5 |
| 0 | 2.73 | 3.80 | 5.50 | 8.50 | 13.8 | 23.5 | 43.0 |
| -20 | 3.49 | 5.15 | 7.90 | 12.9 | 22.0 | 39.5 | 76.5 |
| -40 | - | 7.00 | 11.2 | 19.5 | 35.0 | 67.0 | 140 |
| -60 | - | - | - | 29.5 | 56.0 | 115 | 260 |

*Values in centipoise (cP)*

**Key Observations:**
- Propylene glycol exhibits 15-25% higher viscosity than ethylene glycol at equal concentrations
- Viscosity increases exponentially with concentration and decreases with temperature
- At -20°F with 50% ethylene glycol: μ = 26.0 cP (23× water at 60°F)
- At -40°F with 50% propylene glycol: μ = 67.0 cP (60× water at 60°F)

### Calcium Chloride Brine Solutions

| Temperature (°F) | 15% by mass | 20% by mass | 25% by mass | 29.9% by mass (eutectic) |
|------------------|-------------|-------------|-------------|--------------------------|
| 60 | 1.42 | 1.68 | 2.08 | 2.60 |
| 40 | 1.88 | 2.28 | 2.90 | 3.75 |
| 20 | 2.48 | 3.08 | 4.08 | 5.40 |
| 0 | 3.28 | 4.18 | 5.80 | 7.90 |
| -20 | 4.35 | 5.70 | 8.20 | 11.5 |
| -40 | 5.85 | 7.85 | 11.8 | 17.0 |
| -60 | - | - | 17.0 | 25.5 |

*Values in centipoise (cP). Eutectic concentration: 29.9% by mass, freezing point -60°F*

### Sodium Chloride Brine Solutions

| Temperature (°F) | 10% by mass | 15% by mass | 20% by mass | 23.3% by mass (eutectic) |
|------------------|-------------|-------------|-------------|--------------------------|
| 60 | 1.23 | 1.38 | 1.61 | 1.78 |
| 40 | 1.62 | 1.85 | 2.20 | 2.45 |
| 20 | 2.15 | 2.50 | 3.05 | 3.45 |
| 0 | 2.85 | 3.38 | 4.25 | 4.85 |
| -20 | - | - | 5.95 | 6.90 |

*Values in centipoise (cP). Eutectic concentration: 23.3% by mass, freezing point -6°F*

**Brine Characteristics:**
- Lower viscosity than glycol solutions at equivalent freezing points
- More corrosive, requiring inhibitor packages
- Eutectic concentrations provide lowest practical freezing point
- Sodium chloride limited to applications above -6°F

## Kinematic Viscosity

Kinematic viscosity represents the ratio of dynamic viscosity to fluid density:

ν = μ/ρ

Where:
- ν = kinematic viscosity (m²/s, ft²/s, or centistokes)
- μ = dynamic viscosity (Pa·s or lbf·s/ft²)
- ρ = fluid density (kg/m³ or lbm/ft³)

**Unit Conversions:**
- 1 centistoke (cSt) = 1 mm²/s = 10⁻⁶ m²/s
- 1 cSt = 1.076 × 10⁻⁵ ft²/s
- ν(cSt) = μ(cP) / ρ(g/cm³)

Kinematic viscosity is used directly in:
- Reynolds number calculations for pipe flow
- Nusselt number correlations for heat transfer
- Pump performance corrections
- Prandtl number determination

### Kinematic Viscosity Temperature Relationship

Since both dynamic viscosity and density vary with temperature:

ν(T) = μ(T)/ρ(T)

For most secondary coolants:
- μ decreases strongly with increasing temperature (exponential)
- ρ decreases slightly with increasing temperature (linear)
- ν therefore decreases with temperature, but less dramatically than μ

**Example: 40% Propylene Glycol**

| Temperature (°F) | μ (cP) | ρ (g/cm³) | ν (cSt) |
|------------------|--------|-----------|---------|
| 60 | 3.20 | 1.033 | 3.10 |
| 40 | 5.25 | 1.039 | 5.05 |
| 20 | 8.60 | 1.044 | 8.24 |
| 0 | 13.8 | 1.049 | 13.2 |
| -20 | 22.0 | 1.053 | 20.9 |

Kinematic viscosity increases by a factor of 6.7 from 60°F to -20°F.

## Viscosity Concentration Relationship

For glycol-water mixtures, viscosity is not a linear function of concentration. The relationship exhibits strong positive deviation from ideal mixing:

μ_mixture > x_glycol × μ_glycol + x_water × μ_water

Where x represents mass or volume fraction.

### Peak Viscosity Phenomenon

Maximum viscosity occurs at concentrations between 50-70% by mass, not at 100% glycol:

**Ethylene Glycol at 40°F:**
- Pure water: μ = 1.55 cP
- 50% solution: μ = 5.70 cP (3.7× water)
- 100% glycol: μ = 19.2 cP (12.4× water)

**Peak occurs around 70-75% concentration:**
- Due to molecular interactions disrupting water structure
- Hydrogen bonding between glycol and water molecules
- Reduced molecular mobility in mixed state

### Practical Design Implications

**Concentration Selection Criteria:**
1. Use minimum concentration for freeze protection requirements
2. Add 5-10°F safety margin below expected minimum temperature
3. Consider viscosity penalty when exceeding 50% concentration
4. Balance freeze protection against pumping power

**Recommended Maximum Concentrations:**
- Ethylene glycol: 60% by volume (55% by mass)
- Propylene glycol: 55% by volume (50% by mass)
- Higher concentrations acceptable only with enhanced pump selection

## Viscosity Increase at Low Temperature

The viscosity increase at low temperatures is the single most important consideration for secondary coolant system design.

### Quantifying Viscosity Increase

**Viscosity Ratio Method:**

VR = μ_design / μ_reference

Where:
- μ_design = viscosity at minimum design temperature
- μ_reference = viscosity at reference temperature (typically 40°F or 60°F)

**Example: 40% Propylene Glycol**
- Reference: 40°F, μ = 5.25 cP
- Design: -10°F, μ = 17.5 cP
- VR = 17.5/5.25 = 3.33

This 333% increase affects:
- Pump head requirements (proportional to VR)
- Pump power (potentially proportional to VR²)
- Pressure drop (proportional to VR in laminar flow)
- Heat transfer coefficient (decreases with increasing viscosity)

### Critical Temperature Ranges

**Mild Viscosity Impact (Minimal Design Adjustment):**
- Above 32°F for glycols up to 30% concentration
- VR < 1.5
- Standard pump curves applicable with minor correction

**Moderate Viscosity Impact (Significant Design Consideration):**
- 0°F to 32°F for 30-40% glycol solutions
- VR = 1.5 to 3.0
- Pump performance correction factors required
- Pressure drop increases 50-200%

**Severe Viscosity Impact (Major Design Challenge):**
- Below 0°F for concentrations above 40%
- VR > 3.0
- Custom pump selection essential
- Risk of laminar flow in distribution piping
- Heat transfer degradation significant

### Temperature-Viscosity Design Curves

ASHRAE Handbook - Fundamentals provides temperature-viscosity charts for:
- Ethylene glycol solutions (10-60% by volume)
- Propylene glycol solutions (10-60% by volume)
- Calcium chloride brines (15-30% by mass)
- Sodium chloride brines (10-23% by mass)

These charts allow graphical determination of viscosity at any temperature and concentration within the operating range.

## Pumping Considerations

Elevated viscosity fundamentally changes pump selection and system hydraulic design.

### Pump Performance Correction

Centrifugal pump performance curves published by manufacturers are based on water at 60-85°F. For viscous fluids, corrections are required for:

**1. Flow Rate:**
- Minimal correction typically required
- Q_glycol ≈ Q_water for Newtonian fluids

**2. Head:**
- Head capacity decreases with increasing viscosity
- H_glycol = C_H × H_water
- C_H = correction factor (0.6 to 0.95 depending on viscosity)

**3. Efficiency:**
- Efficiency decreases significantly with viscosity
- η_glycol = C_η × η_water
- C_η = correction factor (0.5 to 0.95)

**4. Power:**
- Power increases due to reduced efficiency and increased head
- P_glycol = (Q × H × ρ)/(3960 × η_glycol)

### Hydraulic Institute Correction Method

The Hydraulic Institute Standard ANSI/HI 9.6.7 provides correction factors based on:
- Flow rate (Q in gpm)
- Head (H in feet)
- Viscosity (ν in centistokes)

**Correction Factor Charts:**
- Valid for kinematic viscosities from 1 to 4000 cSt
- Accounts for Reynolds number effects in impeller
- Separate curves for head, flow, and efficiency
- Most accurate for conventional centrifugal pumps

**Application Procedure:**
1. Select pump based on water performance
2. Determine kinematic viscosity at minimum temperature
3. Apply correction factors from HI charts
4. Verify corrected performance meets system requirements
5. Calculate corrected power requirements

### Viscosity Effects on Pump Types

**Centrifugal Pumps:**
- Performance degrades gradually with viscosity
- Suitable for viscosities up to 200-300 cSt with proper correction
- End-suction and inline designs most affected
- Split-case designs more tolerant of viscosity

**Positive Displacement Pumps:**
- Performance less affected by viscosity
- Efficiency may actually improve slightly with moderate viscosity
- Preferred for viscosities above 300 cSt
- Higher initial cost but better efficiency at high viscosity

**NPSH Considerations:**
- Net Positive Suction Head Required increases with viscosity
- NPSH_R_glycol = NPSH_R_water × C_NPSH
- Critical for systems with limited suction head
- May require larger suction piping or relocation of pumps

## Pump Power Requirements

Power requirements increase dramatically for viscous secondary coolants compared to water systems.

### Theoretical Pump Power

P = (Q × ΔP) / η

Or in HVAC units:

P(hp) = [Q(gpm) × H(ft) × SG] / (3960 × η)

Where:
- P = pump power (hp or kW)
- Q = flow rate (gpm or m³/s)
- H = total head (ft or m)
- SG = specific gravity relative to water
- η = pump efficiency (decimal)

### Viscosity Impact on Power

**Direct Effects:**
1. Increased head requirement (higher pressure drop)
2. Reduced pump efficiency
3. Slightly higher specific gravity

**Power Ratio:**

PR = P_glycol / P_water = (H_glycol × SG_glycol × η_water) / (H_water × SG_water × η_glycol)

**Example Calculation:**
- System: 100 gpm, 50 ft head (water basis)
- Fluid: 40% propylene glycol at 0°F
- Viscosity: 13.8 cP (13.2 cSt)
- SG: 1.049

**Water System (60°F):**
- H = 50 ft
- η = 0.70
- P = (100 × 50 × 1.0)/(3960 × 0.70) = 1.80 hp

**Glycol System (0°F):**
- H_corrected = 50 × 1.15 = 57.5 ft (pressure drop increase)
- η_corrected = 0.70 × 0.85 = 0.595 (efficiency penalty)
- P = (100 × 57.5 × 1.049)/(3960 × 0.595) = 2.56 hp

**Power Ratio:**
- PR = 2.56/1.80 = 1.42 (42% increase)

### Life Cycle Cost Impact

**Annual Energy Cost:**
- Assumes pump runs continuously during cold weather
- Operating hours: 2000-4000 hr/year depending on climate
- Energy cost: $0.10-0.15/kWh typical

**For Example Above (3000 hr/year operation):**
- Water: 1.80 hp × 0.746 kW/hp × 3000 hr × $0.12/kWh = $485/year
- Glycol: 2.56 hp × 0.746 kW/hp × 3000 hr × $0.12/kWh = $690/year
- Additional annual cost: $205 (42% increase)

**20-Year Life Cycle:**
- Additional energy cost: $4100 (present value)
- Justifies investment in:
  - Premium efficiency motors
  - Variable speed drives for temperature-based flow control
  - Optimal concentration selection (not over-concentrated)

## Pressure Drop Calculation

Viscosity directly affects friction factor and therefore pressure drop in piping systems.

### Darcy-Weisbach Equation

ΔP = f × (L/D) × (ρV²/2)

Where:
- ΔP = pressure drop (Pa or lbf/ft²)
- f = Darcy friction factor (dimensionless)
- L = pipe length (m or ft)
- D = pipe inside diameter (m or ft)
- ρ = fluid density (kg/m³ or lbm/ft³)
- V = average velocity (m/s or ft/s)

### Friction Factor Determination

The friction factor depends on Reynolds number and pipe roughness.

**Laminar Flow (Re < 2300):**

f = 64/Re

Pressure drop inversely proportional to Reynolds number, therefore directly proportional to viscosity:

ΔP_laminar ∝ μ

**Turbulent Flow (Re > 4000):**

Colebrook-White equation (implicit):

1/√f = -2.0 log₁₀[(ε/D)/3.7 + 2.51/(Re√f)]

Or Haaland approximation (explicit):

1/√f ≈ -1.8 log₁₀[(ε/D/3.7)^1.11 + 6.9/Re]

Where:
- ε = absolute pipe roughness (m or ft)
- ε/D = relative roughness

**Simplified Turbulent Flow (Smooth Pipes):**

f ≈ 0.316/Re^0.25  (Blasius, valid for Re < 100,000)

In turbulent flow, pressure drop increases less dramatically with viscosity than in laminar flow:

ΔP_turbulent ∝ μ^0.25

### Pressure Drop Comparison

**Example: 2-inch Schedule 40 Steel Pipe, 100 ft length, 6 gpm flow**

**Water at 60°F:**
- ν = 1.12 cSt
- V = 1.84 ft/s
- Re = 1.84 × (2.067/12) / (1.12 × 1.076 × 10⁻⁵) = 28,500 (turbulent)
- f = 0.0235 (from Moody chart, ε = 0.00015 ft)
- ΔP = 0.85 psi

**40% Propylene Glycol at 0°F:**
- ν = 13.2 cSt
- V = 1.84 ft/s (same flow rate)
- Re = 1.84 × (2.067/12) / (13.2 × 1.076 × 10⁻⁵) = 2,420 (transitional)
- f = 0.0310 (higher due to lower Re)
- ρ = 1.049 × 62.4 = 65.5 lbm/ft³
- ΔP = 1.14 psi (34% increase)

**40% Propylene Glycol at -20°F:**
- ν = 20.9 cSt
- Re = 1.84 × (2.067/12) / (20.9 × 1.076 × 10⁻⁵) = 1,530 (laminar!)
- f = 64/1530 = 0.0418
- ΔP = 1.55 psi (82% increase over water)

The transition to laminar flow causes accelerated pressure drop increase.

### Piping Design Guidelines

**Velocity Limits for Viscous Fluids:**
- Design velocity: 2-4 ft/s (glycol solutions, turbulent flow)
- Maximum velocity: 6 ft/s (erosion and noise prevention)
- Minimum velocity: 1.5 ft/s (air elimination, avoid stratification)

**Sizing Considerations:**
1. Calculate pressure drop at minimum design temperature (maximum viscosity)
2. Verify Reynolds number to confirm flow regime
3. If Re < 4000, consider upsizing pipe to restore turbulent flow
4. Balance larger pipe cost against reduced pumping power

**Equivalent Length Method:**
- Total pressure drop includes fittings and valves
- Express fittings as equivalent length: L_eq = K × D / f
- For viscous fluids, K values from water tables remain valid
- However, f increases, so equivalent length effectively increases

## Reynolds Number Effects

Reynolds number governs flow regime and is directly affected by viscosity.

### Reynolds Number Definition

Re = (ρVD)/μ = VD/ν

Where:
- Re = Reynolds number (dimensionless)
- ρ = density (kg/m³ or lbm/ft³)
- V = velocity (m/s or ft/s)
- D = characteristic dimension, pipe inside diameter (m or ft)
- μ = dynamic viscosity (Pa·s or lbf·s/ft²)
- ν = kinematic viscosity (m²/s or ft²/s)

### Flow Regime Criteria

**Laminar Flow:**
- Re < 2300
- Parabolic velocity profile
- Friction factor: f = 64/Re
- Pressure drop proportional to velocity (ΔP ∝ V)
- Reduced heat transfer coefficient

**Transitional Flow:**
- 2300 < Re < 4000
- Unstable, intermittent turbulence
- Difficult to predict pressure drop accurately
- Design should avoid this region if possible

**Turbulent Flow:**
- Re > 4000
- Flat velocity profile with boundary layer
- Friction factor depends on Re and roughness
- Pressure drop proportional to V^1.75 to V^2
- Enhanced heat transfer

### Viscosity Impact on Reynolds Number

At constant flow rate (constant velocity for fixed pipe size):

Re₂/Re₁ = ν₁/ν₂

**Example:**
- 3-inch pipe, 30 gpm flow, V = 2.72 ft/s

**Water at 60°F (ν = 1.12 cSt):**
- Re = 2.72 × (3.068/12) / (1.12 × 1.076 × 10⁻⁵) = 57,900 (turbulent)

**50% Propylene Glycol at 0°F (ν = 23.5 cSt):**
- Re = 57,900 × (1.12/23.5) = 2,760 (transitional/laminar)

Flow regime changes from fully turbulent to transitional simply due to temperature drop.

### Design Strategies to Maintain Turbulent Flow

**1. Minimum Velocity Specification:**
- Specify V_min = 2.0-2.5 ft/s at design conditions
- Ensures Re > 4000 for typical glycol solutions
- May require upsized piping compared to water systems

**2. Verify Reynolds Number:**

Re_min = V_min × D / ν_max

Where ν_max is kinematic viscosity at minimum temperature.

Target: Re_min > 4000 (preferably > 5000 for safety margin)

**3. Pipe Sizing Adjustments:**

If Re < 4000 with standard pipe size, upsize:
- Increase D to increase Re (at constant Q, V decreases but D/ν ratio increases)
- Calculate required diameter:

D_required = 4Q/(πV_target) where V_target maintains Re > 4000

**Example:**
- Q = 20 gpm, ν = 20 cSt, target Re = 5000
- Required V×D product: 5000 × 20 × 1.076 × 10⁻⁵ = 1.076 ft²/s
- For V = 2.5 ft/s: D = 1.076/2.5 = 0.430 ft = 5.16 inches
- Select 6-inch pipe (next standard size)

## Laminar Flow Risk at High Viscosity

Laminar flow presents several operational challenges in secondary coolant systems.

### Operational Problems

**1. Increased Pressure Drop:**
- Laminar friction factor (f = 64/Re) higher than turbulent
- Pressure drop increases linearly with flow rate
- System curve becomes steeper
- Pump may not achieve design flow

**2. Reduced Heat Transfer:**
- Laminar Nusselt number much lower than turbulent
- Nu_laminar ≈ 3.66 (constant for developed flow)
- Nu_turbulent = 0.023 Re^0.8 Pr^0.4 (Dittus-Boelter)
- Heat transfer coefficient may drop 50-70%

**3. Stratification:**
- Lack of turbulent mixing allows temperature stratification
- Hot or cold spots in coils
- Reduced heat exchanger effectiveness
- Air separation problems (air rises in low-velocity zones)

**4. Start-Up Issues:**
- High viscosity at cold start-up
- May require circulation before heat transfer equipment operates
- Potential for freeze damage if flow not established

### Critical System Components

**Small Diameter Piping:**
- Branch piping to individual terminals
- ½-inch to 1-inch connections most susceptible
- Lower Reynolds number due to small D

**Long Piping Runs:**
- Remote equipment locations
- Distribution to multiple buildings
- High pressure drop may limit flow

**Heat Exchangers:**
- Tube-side flow in shell-and-tube exchangers
- Plate heat exchangers with narrow channels
- Manufacturer correction factors essential

### Mitigation Strategies

**1. Design Phase:**
- Calculate Reynolds number for all critical piping
- Upsize piping where Re < 4000 predicted
- Specify minimum flow velocities in design documents
- Select plate heat exchangers with appropriate channel dimensions

**2. Fluid Selection:**
- Use minimum glycol concentration for freeze protection
- Consider brines for applications below -10°F (lower viscosity than glycol)
- Evaluate premium heat transfer fluids with improved low-temperature viscosity

**3. Temperature Management:**
- Insulate piping to prevent excessive cooling during operation
- Heat trace critical sections in extreme climates
- Design for higher return temperatures where possible

**4. Flow Assurance:**
- Specify positive displacement pumps for critical high-viscosity applications
- Include circulation pumps for pre-warming during cold starts
- Install flow switches to verify adequate circulation

**5. System Monitoring:**
- Monitor pressure drop across circuits
- Trending increased ΔP indicates viscosity problems or fouling
- Temperature sensors to verify adequate heat transfer

## Viscosity Charts for Glycol Solutions

Graphical representations provide quick reference for design and troubleshooting.

### Chart Types

**1. Temperature-Viscosity Charts:**
- X-axis: Temperature (°F or °C)
- Y-axis: Dynamic or kinematic viscosity (logarithmic scale)
- Multiple curves for different concentrations
- Available in ASHRAE Handbook - Fundamentals, Chapter 31

**2. Concentration-Viscosity Charts:**
- X-axis: Glycol concentration (% by mass or volume)
- Y-axis: Viscosity (logarithmic scale)
- Multiple curves for different temperatures
- Shows peak viscosity at high concentrations

**3. Temperature-Concentration-Viscosity Nomographs:**
- Three-scale alignment charts
- Connect temperature and concentration to read viscosity
- Useful for field calculations without computer

### Using Viscosity Charts

**Design Application:**
1. Determine minimum design temperature
2. Select glycol concentration (freeze point - 10°F safety margin)
3. Enter chart at intersection of temperature and concentration
4. Read dynamic viscosity (cP) and kinematic viscosity (cSt)
5. Use values for pump selection and pressure drop calculations

**Verification Application:**
1. Measure glycol concentration (refractometer)
2. Measure fluid temperature
3. Read expected viscosity from chart
4. Compare to measured system performance (pressure drop, flow rate)
5. Diagnose problems: viscosity mismatch indicates contamination or degradation

### Interpolation and Extrapolation

For conditions between chart curves:
- Linear interpolation acceptable for small intervals (5-10°F)
- Logarithmic interpolation better for large intervals
- Avoid extrapolation beyond chart limits (unreliable)

## ASHRAE References

**ASHRAE Handbook - Fundamentals (2021):**
- Chapter 31: Physical Properties of Secondary Coolants (Brines)
  - Table 2: Ethylene glycol solutions (physical properties vs temperature)
  - Table 3: Propylene glycol solutions (physical properties vs temperature)
  - Table 4: Calcium chloride solutions
  - Table 5: Sodium chloride solutions
  - Figure 1: Viscosity-temperature chart for glycols
  - Figure 2: Specific heat vs temperature for glycols

- Chapter 3: Fluid Flow
  - Friction factor correlations
  - Reynolds number criteria
  - Pressure drop calculation methods

- Chapter 4: Heat Transfer
  - Convective heat transfer correlations
  - Viscosity correction factors for heat transfer

**ASHRAE Standard 15-2019:**
- Safety Standard for Refrigeration Systems
- Toxicity classifications relevant to glycol selection

**ASHRAE Guideline 3-2018:**
- Reducing Emissions of Halogenated Refrigerants
- Secondary loop applications to reduce refrigerant charge

## Design Considerations

### Concentration Optimization

**Freeze Protection:**
- Minimum requirement: Freeze point 10°F below lowest expected temperature
- Consider 99.6% winter design temperature from ASHRAE climatic data
- Add 5-10°F safety margin for:
  - Stagnant conditions (pump failure)
  - Extreme weather events
  - Concentration drift over time

**Viscosity Penalty:**

Compare scenarios:
- 30% propylene glycol: freeze point = 10°F, μ at 0°F = 8.5 cP
- 40% propylene glycol: freeze point = -10°F, μ at 0°F = 13.8 cP
- 50% propylene glycol: freeze point = -28°F, μ at 0°F = 23.5 cP

For location with design temperature of 5°F:
- 30% concentration adequate with 5°F margin
- 40% or 50% over-designed, wastes pumping energy

**Cost-Benefit Analysis:**
- Glycol cost (propylene glycol ≈ $8-12/gallon)
- Pumping energy over system life
- Maintenance (higher viscosity → more frequent filter changes)
- System complexity (larger pumps, piping)

### Pressure Drop Impact

**Allowable Pressure Drop:**
- Limit total system pressure drop: 15-25 psi typical for glycol systems
- Distribution: 40% piping, 30% heat exchanger, 20% control valves, 10% fittings
- Higher than water systems (10-15 psi typical)

**Iterative Design Process:**
1. Assume initial pipe sizes based on velocity (2-4 ft/s)
2. Calculate pressure drop at design temperature (worst case viscosity)
3. If total ΔP exceeds allowable, upsize critical sections
4. Recalculate until acceptable
5. Verify Reynolds number > 4000 in all sections

### Pump Selection

**Selection Criteria:**
1. Determine required flow and head at design conditions
2. Apply Hydraulic Institute correction factors for viscosity
3. Select pump with corrected performance meeting requirements
4. Verify NPSH available > NPSH required (corrected)
5. Calculate power requirement with corrected efficiency
6. Specify motor sized for maximum power condition

**Pump Type Selection:**
- Centrifugal: suitable for ν < 150 cSt
- Positive displacement: required for ν > 300 cSt
- Special centrifugal (open impeller, large passages): ν = 150-300 cSt

**Variable Speed Drives:**
- Essential for systems with wide temperature range
- Reduce pumping power during warmer operation
- Maintain minimum flow velocity at all operating points
- Set minimum speed to maintain Re > 4000

### Heat Transfer Equipment

**Correction Factors:**
- Tube-side heat transfer coefficient: h_glycol ≈ 0.6-0.8 × h_water (depending on viscosity)
- Overall U-value reduced by 10-30%
- Compensate with:
  - Increased surface area (larger heat exchanger)
  - Higher flow velocities (higher Re, better h)
  - Turbulence promoters in tubes

**Fouling Factors:**
- Glycol solutions: f_d = 0.001 hr·ft²·°F/Btu (clean systems)
- Glycol solutions: f_d = 0.002 hr·ft²·°F/Btu (normal service)
- Higher than water due to glycol degradation products over time

**Velocity Requirements:**
- Maintain minimum 3 ft/s in shell-and-tube exchangers
- Plate heat exchangers: manufacturer recommendation for minimum flow
- Test and verify heat transfer performance after startup

### System Operating Strategies

**Cold Weather Operation:**
1. Pre-circulation before equipment startup (warm fluid)
2. Monitor return temperature to verify heat transfer
3. Adjust flow based on temperature (VFD control)
4. Prevent stratification in storage tanks (continuous mixing)

**Seasonal Transition:**
1. Increase glycol concentration before winter (if system allows makeup)
2. Test concentration monthly during cold season
3. Flush and recharge if concentration drifts significantly

**Maintenance Indicators:**
1. Rising pressure drop at constant flow → increased viscosity or fouling
2. Reduced heat transfer → degraded fluid or laminar flow
3. Pump power increase → efficiency loss due to viscosity

### Energy Analysis

**Total Pumping Energy:**

E_annual = (P_pump × hours × load_factor) / η_motor

Where:
- P_pump = pump power (kW)
- hours = operating hours per year
- load_factor = average load as fraction of design (0.4-0.6 typical)
- η_motor = motor efficiency (0.90-0.95)

**Optimization:**
- Balance glycol concentration (viscosity) against freeze protection needs
- Variable speed pumping reduces energy in proportion to flow³
- Temperature reset strategies reduce viscosity by maintaining warmer return
- Monitor and trend energy consumption annually

**Case Study Example:**
- 500 gpm system, 40 ft head (water), 6000 hr/year operation
- Water system: 8 hp average, 35,000 kWh/year, $4,200 annual cost
- 40% propylene glycol at average 10°F: 14 hp, 61,000 kWh/year, $7,300 annual cost
- Additional cost: $3,100/year or $62,000 over 20-year life (discounted)

This energy penalty justifies careful concentration selection and consideration of alternatives (brines, advanced glycols) for very low temperature applications.

## Summary

Viscosity's temperature dependence is the dominant challenge in secondary coolant system design. Key takeaways:

1. **Exponential relationship**: Viscosity increases exponentially as temperature decreases, following Arrhenius or Vogel correlations.

2. **Concentration effects**: Higher glycol concentrations dramatically increase viscosity, with peak occurring at 70-75% concentration.

3. **Pumping penalties**: Power requirements increase 40-100% compared to water systems due to higher pressure drop and reduced pump efficiency.

4. **Flow regime transitions**: High viscosity can cause transition from turbulent to laminar flow, severely impacting pressure drop and heat transfer.

5. **Design approach**:
   - Use minimum concentration for required freeze protection
   - Calculate Reynolds number for all piping sections
   - Apply pump correction factors from Hydraulic Institute standards
   - Size heat exchangers for reduced heat transfer coefficients
   - Consider life cycle costs of elevated pumping energy

6. **Alternatives**: For applications below -10°F, consider calcium chloride brines (lower viscosity than glycol at equivalent freeze point) despite corrosion concerns.

Understanding and accounting for viscosity-temperature behavior ensures reliable, efficient secondary coolant system operation across all seasonal conditions.
