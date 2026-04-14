---
title: "Exergy Analysis"
aliases: ["Exergy Analysis"]
weight: 5
---

Exergy analysis provides a rigorous thermodynamic method for evaluating HVAC system performance based on the second law of thermodynamics. Unlike energy analysis, which accounts only for quantity, exergy analysis evaluates the quality and maximum useful work potential of energy streams.

## Fundamental Concepts

### Exergy Definition

Exergy is the maximum theoretical useful work obtainable as a system interacts with a reference environment to reach equilibrium. For a closed system:

Ex = (U - U₀) + P₀(V - V₀) - T₀(S - S₀)

Where:
- Ex = exergy of the system (kJ)
- U = internal energy (kJ)
- P₀ = dead state pressure (kPa)
- V = volume (m³)
- T₀ = dead state temperature (K)
- S = entropy (kJ/K)
- Subscript 0 denotes dead state properties

### Dead State

The dead state (reference environment) represents conditions where the system is in complete equilibrium with its surroundings. Standard dead state conditions for HVAC analysis:

| Parameter | Typical Value |
|-----------|---------------|
| Temperature (T₀) | 25°C (298.15 K) |
| Pressure (P₀) | 101.325 kPa |
| Relative Humidity | 60% |
| Elevation | Sea level |

The choice of dead state significantly affects exergy values but not exergy destruction calculations.

### Specific Flow Exergy

For flowing streams in HVAC systems, specific flow exergy (exergy per unit mass):

ex = (h - h₀) - T₀(s - s₀) + V²/2 + gz

Where:
- ex = specific exergy (kJ/kg)
- h = specific enthalpy (kJ/kg)
- s = specific entropy (kJ/kg·K)
- V = velocity (m/s)
- g = gravitational acceleration (9.81 m/s²)
- z = elevation (m)

For most HVAC applications, kinetic and potential energy terms are negligible:

ex ≈ (h - h₀) - T₀(s - s₀)

## Exergy Balance

### General Exergy Balance Equation

For a control volume at steady state:

ΣĖxᵢₙ - ΣĖxₒᵤₜ - Ẇ - Ėxₕₑₐₜ = Ėxₐₑₛₜᵣₒᵧₑₐ

Where:
- Ėx = exergy flow rate (kW)
- Ẇ = power output (kW)
- Ėxₕₑₐₜ = exergy transfer with heat (kW)
- Ėxₐₑₛₜᵣₒᵧₑₐ = exergy destruction rate (kW)

### Exergy Transfer with Heat

Heat transfer at temperature T carries exergy:

Ėxₕₑₐₜ = Q̇(1 - T₀/T)

Where:
- Q̇ = heat transfer rate (kW)
- T = temperature at which heat crosses boundary (K)

The factor (1 - T₀/T) is the Carnot efficiency, representing the fraction of heat that could theoretically be converted to work.

## Exergy Destruction

### Irreversibility and Entropy Generation

Exergy destruction quantifies irreversibilities in a process:

Ėxₐₑₛₜᵣₒᵧₑₐ = T₀Ṡgₑₙ

Where:
- Ṡgₑₙ = entropy generation rate (kW/K)

This relationship directly links second law violations (entropy generation) to loss of work potential.

### Common Sources in HVAC Systems

**Heat Transfer Across Finite Temperature Differences:**

For a heat exchanger with heat transfer rate Q̇:

Ėxₐ = Q̇T₀(1/Tₒᵤₜ - 1/Tₕₒₜ)

**Throttling Processes:**

For expansion valves and dampers at constant enthalpy:

Ėxₐ = ṁT₀(s₂ - s₁)

**Mixing Processes:**

For two streams mixing adiabatically:

Ėxₐ = T₀[ṁ₃s₃ - (ṁ₁s₁ + ṁ₂s₂)]

**Fluid Friction:**

Pressure drop in ducts and piping:

Ėxₐ = ṁT₀Δs = ṁv̄ΔP

Where v̄ is average specific volume and ΔP is pressure drop.

## Second Law Efficiency

### Exergetic Efficiency

Second law efficiency (ψ) compares actual performance to ideal reversible performance:

ψ = Exergy output / Exergy input = Ėxₒᵤₜ / Ėxᵢₙ

Or equivalently:

ψ = (Ėxᵢₙ - Ėxₐₑₛₜᵣₒᵧₑₐ) / Ėxᵢₙ = 1 - (Ėxₐₑₛₜᵣₒᵧₑₐ / Ėxᵢₙ)

### Comparison with First Law Efficiency

| Aspect | Energy Efficiency | Exergy Efficiency |
|--------|-------------------|-------------------|
| Basis | First law | Second law |
| Focus | Quantity | Quality |
| Maximum value | 100% (often) | Typically 20-50% HVAC |
| Insight | Energy conservation | Thermodynamic perfection |
| Improvement potential | Limited | Reveals opportunities |

### Task-Specific Definitions

**Heat Pump:**

ψₕₚ = Ėxₒᵤₜ,ₕₑₐₜ / Ẇᵢₙ = Q̇ₕ(1 - T₀/Tₕ) / Ẇ

**Chiller:**

ψ꜀ₕ = Ėxᵢₙ,ₕₑₐₜ / Ẇᵢₙ = Q̇ₑ(T₀/T꜀ - 1) / Ẇ

**Heat Exchanger:**

ψₕₓ = Ėxₒᵤₜ,꜀ₒₗₐ / Ėxᵢₙ,ₕₒₜ

## HVAC System Exergy Analysis

### Air Conditioning System Components

**Compressor:**

- Exergy input: Electrical work + refrigerant inlet exergy
- Exergy output: Refrigerant outlet exergy
- Major destruction: Compression irreversibilities
- Typical ψ: 80-90%

**Condenser:**

- Exergy input: Hot refrigerant exergy
- Exergy output: Cooling water/air exergy increase
- Major destruction: Heat transfer across ΔT
- Typical ψ: 5-15%

**Evaporator:**

- Exergy input: Chilled water/air exergy decrease
- Exergy output: Refrigerant exergy increase
- Major destruction: Heat transfer across ΔT
- Typical ψ: 20-40%

**Expansion Valve:**

- Exergy destruction: Throttling irreversibility
- Typical ψ: 10-30%
- Potential: Replace with expander

### Typical Exergy Destruction Distribution

| Component | % of Total Destruction |
|-----------|------------------------|
| Condenser | 35-45% |
| Evaporator | 25-35% |
| Compressor | 15-25% |
| Expansion valve | 10-20% |

### Air Distribution System

**Fans:**

Ėxₐ = Ẇfₐₙ(1 - ηfₐₙ/ηfₐₙ,ᵢₐₑₐₗ) + ṁT₀Δsₐᵤ꜀ₜ

**Duct System:**

Ėxₐ = ṁₐᵢᵣvₐᵥgΔPfᵣᵢ꜀ₜᵢₒₙ

Minimized through proper sizing (duct velocity 4-8 m/s in mains).

## Optimization Using Exergy Analysis

### Identification of Improvement Opportunities

1. Rank components by exergy destruction rate
2. Calculate exergy destruction ratio: yₐ = Ėxₐ,ᵢ / ΣĖxₐ
3. Focus on high-yₐ components
4. Evaluate cost-effectiveness of modifications

### Design Trade-offs

**Heat Exchanger Sizing:**

- Larger area → Lower ΔT → Lower Ėxₐ,ₕₓ
- But: Higher capital cost, more fluid friction
- Optimal size balances exergy destruction costs

**Temperature Lift Minimization:**

For heat pumps, reducing (Tₕ - T꜀) improves ψ:

COPₐₑₐₗ = Tₕ/(Tₕ - T꜀)

Strategies:
- Lower supply water temperature (radiant systems)
- Higher evaporator temperature (raised floor coils)
- Cascade systems for large lifts

### System-Level Optimization

**Matching Source and Load Temperatures:**

Exergy destruction minimized when temperature differences are small throughout the system. This favors:

- Low-temperature heating (30-40°C)
- High-temperature cooling (15-18°C chilled water)
- Multiple temperature levels
- Thermal storage at appropriate temperatures

**Exergoeconomic Analysis:**

Cost per unit exergy destroyed:

cₐ = C̊ / Ėxₐ

Where C̊ is cost rate ($/hr). Optimize total system cost (capital + operating).

## Practical Application Procedure

### Step-by-Step Analysis

1. **Define system boundary and components**
2. **Specify dead state conditions**
3. **Determine thermodynamic properties** (P, T, h, s) at all states
4. **Calculate exergy at each state point:**
   - ex = (h - h₀) - T₀(s - s₀)
5. **Apply exergy balance to each component**
6. **Calculate exergy destruction rates**
7. **Determine exergetic efficiencies**
8. **Rank destruction sources**
9. **Identify improvement strategies**
10. **Evaluate economic feasibility**

### Software Tools

- EES (Engineering Equation Solver)
- REFPROP (thermodynamic properties)
- Custom Python/MATLAB scripts
- Specialized exergy analysis packages

## Advantages for HVAC Design

- Reveals true thermodynamic inefficiencies
- Quantifies quality degradation of energy
- Identifies optimal operating conditions
- Guides equipment selection
- Justifies high-efficiency investments
- Enables fair comparison of different technologies
- Supports sustainability assessments

## Components

- Availability Analysis
- Irreversibility Calculation
- Second Law Efficiency
- Exergy Destruction
- Chemical Exergy
- Physical Exergy
- Exergetic Efficiency
- Exergy Balance
- Grassmann Diagrams
- Exergoeconomic Analysis
- Thermoeconomic Optimization
