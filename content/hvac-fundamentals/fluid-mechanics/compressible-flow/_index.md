---
title: "Compressible Flow"
description: "Gas dynamics fundamentals for HVAC applications including high-velocity duct systems, refrigerant flow through expansion devices, and pneumatic control systems"
weight: 9
---

## Overview

Compressible flow occurs when gas density changes significantly during flow processes. While most HVAC air systems operate at low Mach numbers where incompressible flow assumptions suffice, compressible flow theory becomes essential for:

- High-velocity duct systems (velocity > 80 ft/s)
- Refrigerant flow through expansion valves and orifices
- Pneumatic control air distribution
- Relief valve sizing for pressure vessels
- Critical flow conditions in refrigeration systems
- Compressed air distribution networks

The compressibility of a fluid becomes significant when the Mach number exceeds approximately 0.3, corresponding to air velocities above 340 ft/s at standard conditions. However, compressible flow principles apply at lower velocities when analyzing:

- Pressure recovery in high-velocity duct transitions
- Refrigerant throttling processes
- Gas flow through small orifices
- Pneumatic actuator response dynamics

## Fundamental Principles

### Density Variation and Compressibility

The key distinction between compressible and incompressible flow lies in density variation. For an ideal gas:

ρ = P / (R × T)

Where:
- ρ = density (lbm/ft³)
- P = absolute pressure (lbf/ft²)
- R = specific gas constant (ft·lbf/lbm·°R)
- T = absolute temperature (°R)

The isothermal compressibility:

β = -1/V × (∂V/∂P)_T = 1/P

For air at standard conditions (14.7 psia, 70°F), β = 6.8 × 10⁻⁵ ft²/lbf.

### Speed of Sound

The speed of sound represents the propagation velocity of small pressure disturbances through a gas:

a = √(k × R × T)

For air (k = 1.4, R = 53.35 ft·lbf/lbm·°R):

a = 49.02 × √T (°R)

At standard conditions (70°F = 530°R):
a = 1,128 ft/s = 769 mph

Temperature sensitivity is critical for HVAC applications. At typical duct temperatures:

| Temperature | Speed of Sound |
|-------------|----------------|
| 32°F (492°R) | 1,087 ft/s |
| 70°F (530°R) | 1,128 ft/s |
| 100°F (560°R) | 1,160 ft/s |
| 140°F (600°R) | 1,201 ft/s |

### Mach Number

The Mach number quantifies flow velocity relative to acoustic velocity:

M = V / a

Where:
- M = Mach number (dimensionless)
- V = flow velocity (ft/s)
- a = local speed of sound (ft/s)

**Flow Regimes:**

| Mach Number Range | Flow Classification | HVAC Applications |
|-------------------|---------------------|-------------------|
| M < 0.3 | Incompressible | Standard duct systems, fans |
| 0.3 < M < 0.8 | Subsonic compressible | High-velocity ducts, large relief valves |
| 0.8 < M < 1.2 | Transonic | Rarely encountered in HVAC |
| M > 1.2 | Supersonic | Not applicable to HVAC systems |

For typical HVAC duct velocities:

| Duct Velocity | Mach Number (70°F) | Compressibility Effect |
|---------------|---------------------|------------------------|
| 2,000 fpm (33 ft/s) | 0.029 | Negligible |
| 4,000 fpm (67 ft/s) | 0.059 | Negligible |
| 6,000 fpm (100 ft/s) | 0.089 | Minor (< 1% error) |
| 10,000 fpm (167 ft/s) | 0.148 | Noticeable (2-3% error) |
| 20,000 fpm (333 ft/s) | 0.295 | Significant (> 5% error) |

## Stagnation Properties

Stagnation (total) properties represent the thermodynamic state achieved when a moving fluid is brought to rest isentropically.

### Stagnation Temperature

T₀ = T + V²/(2 × cp)

For air (cp = 0.24 BTU/lbm·°R = 187 ft·lbf/lbm·°R):

T₀ = T × (1 + (k-1)/2 × M²)

Temperature rise due to velocity:

ΔT = V²/(2 × cp × gc)

Where gc = 32.174 lbm·ft/lbf·s²

**Example:** Air at 70°F flowing at 10,000 fpm (167 ft/s):

ΔT = (167)² / (2 × 187 × 32.174) = 2.3°F

This temperature rise becomes significant in high-velocity systems and must be considered for cooling load calculations.

### Stagnation Pressure

For isentropic flow:

P₀/P = (T₀/T)^(k/(k-1)) = (1 + (k-1)/2 × M²)^(k/(k-1))

For air (k = 1.4):

P₀/P = (1 + 0.2 × M²)^3.5

The stagnation pressure represents the maximum pressure recoverable through isentropic deceleration. In HVAC applications:

- Pitot tube measurements yield stagnation pressure
- Static pressure taps measure local static pressure
- Velocity pressure = stagnation pressure - static pressure

### Stagnation Density

ρ₀/ρ = (T₀/T)^(1/(k-1)) = (1 + (k-1)/2 × M²)^(1/(k-1))

For air:

ρ₀/ρ = (1 + 0.2 × M²)^2.5

## Isentropic Flow Relations

Isentropic (constant entropy) flow occurs when processes are reversible and adiabatic. While real flows experience losses, isentropic relations provide:

- Maximum theoretical performance limits
- Reference conditions for efficiency calculations
- Basis for nozzle and expansion device analysis

### Pressure-Temperature Relations

For isentropic processes in ideal gases:

P₂/P₁ = (T₂/T₁)^(k/(k-1))

T₂/T₁ = (P₂/P₁)^((k-1)/k)

For air (k = 1.4):

P₂/P₁ = (T₂/T₁)^3.5

T₂/T₁ = (P₂/P₁)^0.286

### Density Relations

ρ₂/ρ₁ = (P₂/P₁)^(1/k) = (T₂/T₁)^(1/(k-1))

### Critical Pressure Ratio

The critical pressure ratio determines choked flow conditions:

(P*/P₀) = (2/(k+1))^(k/(k-1))

For air (k = 1.4):

P*/P₀ = 0.528

When the downstream-to-upstream pressure ratio falls below 0.528, flow becomes choked at sonic velocity (M = 1), and further pressure reduction does not increase mass flow rate.

## Area-Mach Number Relation

For isentropic flow in a variable-area duct:

A/A* = (1/M) × [(2/(k+1)) × (1 + (k-1)/2 × M²)]^((k+1)/(2(k-1)))

Where:
- A = local cross-sectional area
- A* = sonic throat area (where M = 1)
- M = local Mach number

This relation shows that for subsonic flow (M < 1), area reduction increases velocity and decreases pressure. However, for supersonic flow (M > 1), area increase is required to further accelerate the flow.

**Subsonic HVAC Applications:**

The area-Mach relation explains pressure recovery in expanding ductwork:

| Area Ratio A₂/A₁ | M₁ = 0.1 | M₁ = 0.2 | M₁ = 0.3 |
|------------------|----------|----------|----------|
| 1.5 | M₂ = 0.067 | M₂ = 0.133 | M₂ = 0.200 |
| 2.0 | M₂ = 0.050 | M₂ = 0.100 | M₂ = 0.150 |
| 3.0 | M₂ = 0.033 | M₂ = 0.067 | M₂ = 0.100 |

## Converging Nozzles

Converging nozzles accelerate subsonic flow by reducing cross-sectional area. Applications include:

- Pneumatic control air distribution
- Venturi sections in air measurement stations
- Refrigerant distributor nozzles

### Mass Flow Rate

For choked flow (P_exit/P₀ ≤ 0.528):

ṁ = Cd × A_throat × P₀ × √(k/(R×T₀)) × (2/(k+1))^((k+1)/(2(k-1)))

For air at standard conditions:

ṁ = 0.686 × Cd × A_throat × P₀ / √T₀

Where:
- ṁ = mass flow rate (lbm/s)
- Cd = discharge coefficient (0.95-0.99 for well-designed nozzles)
- A_throat = throat area (ft²)
- P₀ = upstream stagnation pressure (lbf/ft²)
- T₀ = upstream stagnation temperature (°R)

### Choked Flow Conditions

Once the throat reaches M = 1, further reduction in downstream pressure does not increase mass flow rate. The flow is "choked" at:

ṁ_max = Cd × A* × P₀ × √(k/(R×T₀)) × (2/(k+1))^((k+1)/(2(k-1)))

This principle applies to:
- Refrigerant expansion valves at high pressure drops
- Safety relief valve sizing
- Pneumatic control orifices

## Converging-Diverging Nozzles

Converging-diverging (de Laval) nozzles can accelerate flow to supersonic velocities. While uncommon in building HVAC systems, the principles apply to:

- Steam turbine nozzles in central plants
- High-pressure gas expansion in industrial refrigeration
- Ejector systems for refrigeration

The nozzle operates in several modes depending on back pressure:

1. **Subsonic throughout:** Low pressure drop, flow does not reach M = 1
2. **Choked at throat:** Throat reaches M = 1, but diverging section remains subsonic
3. **Design condition:** Supersonic flow in diverging section with shock-free expansion
4. **Overexpanded:** Exit pressure below ambient, external compression waves form
5. **Underexpanded:** Exit pressure above ambient, external expansion waves form

## Choked Flow in HVAC Systems

Choked flow represents a fundamental mass flow rate limit occurring when fluid velocity reaches sonic conditions.

### Refrigerant Expansion Devices

Thermostatic expansion valves (TXVs) and electronic expansion valves (EEVs) frequently operate under choked conditions when:

P_evap/P_cond < 0.528 (for ideal gas approximation)

For real refrigerants, critical pressure ratios differ:

| Refrigerant | Critical Pressure Ratio | Typical Operating Ratio |
|-------------|-------------------------|-------------------------|
| R-410A | ~0.45 | 0.25 - 0.40 |
| R-134a | ~0.48 | 0.28 - 0.45 |
| R-32 | ~0.46 | 0.26 - 0.42 |
| R-744 (CO₂) | ~0.55 | 0.40 - 0.60 |

When choked, refrigerant capacity becomes:

ṁ_ref = Cd × A_orifice × ρ_upstream × a_upstream

Where a = local speed of sound in the refrigerant.

### Valve Sizing Under Choked Conditions

For gas service, the flow coefficient becomes:

Cv = ṁ × √(T₁/(P₁ × SG)) / 0.471

Where:
- Cv = flow coefficient (gpm water equivalent)
- ṁ = gas flow rate (lbm/hr)
- T₁ = upstream temperature (°R)
- P₁ = upstream pressure (psia)
- SG = specific gravity relative to air

When P₂/P₁ < critical ratio, use P₂ = 0.528 × P₁ for calculations.

## Fanno Flow

Fanno flow represents adiabatic flow with friction in constant-area ducts. This model applies to:

- Long pneumatic control tubing runs
- Compressed air distribution piping
- High-velocity duct systems with significant friction

### Governing Equations

The friction parameter:

f × L / D_h = (1 - M₁²)/(k × M₁²) + (k+1)/(2k) × ln[(k+1) × M₁² / (2 × (1 + (k-1)/2 × M₁²))]

Where:
- f = Darcy friction factor
- L = duct length (ft)
- D_h = hydraulic diameter (ft)
- M₁ = inlet Mach number

Key observations for subsonic Fanno flow:

1. Friction always drives the flow toward M = 1
2. Pressure decreases in the flow direction
3. Temperature decreases initially, then may increase near M = 1
4. For long ducts, flow becomes choked at exit (M = 1)

### Maximum Duct Length

For a given inlet Mach number, maximum duct length before choking:

L_max = (D_h/f) × [(1 - M₁²)/(k × M₁²) + (k+1)/(2k) × ln[(k+1) × M₁² / (2 × (1 + (k-1)/2 × M₁²))]]

**Example:** Compressed air duct, D = 2 in, f = 0.02, M₁ = 0.3:

L_max = (2/12)/0.02 × [calculation] ≈ 85 ft

Beyond this length, either:
- Mass flow rate must decrease
- Inlet pressure must increase
- Duct diameter must increase

## Rayleigh Flow

Rayleigh flow represents frictionless flow with heat transfer in constant-area ducts. Applications include:

- Heating or cooling of pneumatic control air
- Heat exchange in compressed air systems
- Analysis of temperature effects in refrigerant piping

### Stagnation Temperature Changes

Heat addition increases stagnation temperature:

dT₀/T₀ = dq/(cp × T)

Where dq = heat added per unit mass.

For subsonic flow (M < 1):
- Heat addition accelerates flow (increases M)
- Heat removal decelerates flow (decreases M)

For supersonic flow (M > 1):
- Heat addition decelerates flow (decreases M)
- Heat removal accelerates flow (increases M)

## HVAC Applications

### High-Velocity Duct Systems

High-velocity HVAC systems (4,000-6,000 fpm) approach conditions where compressible flow effects become measurable.

**Pressure Recovery in Transitions:**

For subsonic flow decelerating through area expansion, actual pressure recovery:

η_diffuser = (P₂ - P₁)_actual / (P₀₁ - P₁)

Typical diffuser efficiencies:
- Gradual expansion (7-10° included angle): 85-90%
- Moderate expansion (15-20° included angle): 70-80%
- Rapid expansion (> 30° included angle): 40-60%

Compressible flow corrections for pressure recovery:

ΔP_static = ΔP_total × [1 - (k-1)/2 × M²]^(k/(k-1))

### Refrigerant Flow Through Expansion Devices

Expansion valves throttle refrigerant from condenser to evaporator pressure. The process involves:

1. Approach to valve: Liquid or two-phase refrigerant
2. Valve orifice: Rapid pressure drop, often choked
3. Exit: Two-phase mixture with flash gas

Capacity prediction for choked flow:

ṁ = Cd × A × √(2 × ρ_liquid × ΔP_critical)

Where ΔP_critical = P_upstream × (1 - 0.528) = 0.472 × P_upstream

**Expansion Valve Selection:**

Manufacturers rate valves using:
- Tons of refrigeration capacity
- Operating temperatures (evaporator and condenser)
- Refrigerant type
- Superheat setting

Actual capacity varies with pressure ratio:

| P_evap/P_cond | Capacity Factor |
|---------------|-----------------|
| 0.50 | 0.95 |
| 0.40 | 1.00 (reference) |
| 0.30 | 1.03 |
| 0.20 | 1.05 |

### Pneumatic Control Systems

Pneumatic controls typically operate at 15-20 psig supply pressure. Control signals range from 3-15 psig (proportional) or 8-13 psig (typical modulating range).

**Tubing Sizing Considerations:**

Response time depends on:
- Tubing length and diameter
- Volume of controlled device
- Supply pressure and flow restrictions

For rapid response (< 1 second):

L/D_h < 1000 × √(P_supply/14.7)

**Orifice Sizing for Control Air:**

Flow rate through orifice:

Q = Cd × A × P_upstream × √(k/(R×T)) × function(pressure_ratio)

For choked conditions (fast response):

Q = 0.686 × Cd × A × P_upstream / √T

## Design Considerations

### When to Apply Compressible Flow Theory

**Mandatory:**
- Duct velocities > 10,000 fpm (M > 0.15)
- Refrigerant expansion devices
- Pneumatic control orifices
- Safety relief valve sizing
- Compressed air system design

**Recommended:**
- High-velocity return air systems
- Energy recovery ventilators with high pressure drops
- Fan discharge transitions at high static pressures
- Sound attenuator pressure drop calculations

**Optional:**
- Standard comfort HVAC duct systems (velocity < 4,000 fpm)
- Low-pressure air handling units
- Gravity ventilation systems

### Pressure Drop Corrections

For high-velocity systems, apply compressible flow corrections when:

M > 0.3 or ΔP/P > 0.05

Corrected pressure drop:

ΔP_compressible = ΔP_incompressible × [1 + M²/4 + M⁴/40]

### Duct Sizing for Compressible Effects

To minimize compressible flow losses in high-velocity systems:

1. **Gradual transitions:** Maximum 7° included angle for expansions
2. **Avoid sudden enlargements:** Use transition sections minimum 3D long
3. **Minimize friction:** Specify smooth duct interiors, maximize radius elbows
4. **Account for density changes:** Recalculate velocity at each section using local density

### Temperature Rise in High-Velocity Systems

Kinetic energy converted to thermal energy in low-velocity terminal sections:

ΔT = V²/(2 × cp × gc)

**Impact on Cooling Loads:**

| Duct Velocity | Temperature Rise | Additional Load (per 1000 cfm) |
|---------------|------------------|-------------------------------|
| 4,000 fpm | 0.36°F | 22 BTU/hr |
| 6,000 fpm | 0.81°F | 49 BTU/hr |
| 8,000 fpm | 1.44°F | 87 BTU/hr |
| 10,000 fpm | 2.25°F | 136 BTU/hr |

## Code and Standard References

### ASHRAE Standards

**ASHRAE Fundamentals Handbook (2021):**
- Chapter 3: Fluid Flow - Compressible flow relationships
- Chapter 21: Duct Design - High-velocity system considerations
- Chapter 38: Compressors - Gas dynamics in refrigeration systems

**ASHRAE Standard 51/AMCA 210:**
- Fan testing procedures accounting for compressibility
- Correction factors for density effects

### Industry Standards

**SMACNA HVAC Duct Construction Standards:**
- High-velocity duct sealing requirements
- Pressure classifications for compressible flow applications

**API 520 (Adapted for HVAC):**
- Relief valve sizing under choked flow conditions
- Gas and vapor service calculations

**ISO 5167:**
- Orifice plate sizing for compressible fluids
- Discharge coefficient correlations

## Best Practices

### System Design

1. **Velocity Limits:** Restrict duct velocities to M < 0.3 to avoid significant compressibility effects
2. **Pressure Drop Budget:** For high-velocity systems, allocate 15-20% additional pressure drop budget for compressible effects
3. **Expansion Device Sizing:** Always check for choked flow conditions; use manufacturer's software tools
4. **Control System Response:** Size pneumatic tubing for desired response time considering compressible flow delays

### Calculations and Analysis

1. **Iterative Solutions:** Compressible flow calculations often require iteration since density varies with pressure
2. **Property Evaluation:** Always use properties at local conditions, not system average
3. **Verification:** Compare compressible and incompressible results; if difference < 2%, incompressible analysis sufficient
4. **Software Tools:** Use specialized software (e.g., NIST REFPROP) for refrigerant compressible flow analysis

### Performance Verification

1. **Field Measurements:** Use calibrated pitot tubes to measure total and static pressures separately
2. **Temperature Monitoring:** Verify predicted temperature changes in high-velocity transitions
3. **Flow Rates:** Confirm refrigerant mass flow rates match expansion valve ratings
4. **Control Response:** Test pneumatic control system response times during commissioning

### Safety Considerations

1. **Overpressure Protection:** Size relief devices considering choked flow limitations
2. **Material Selection:** High-velocity systems experience greater erosion; specify appropriate materials
3. **Noise Control:** Sonic and near-sonic flow generates significant noise; provide adequate attenuation
4. **Structural Support:** High-velocity systems create greater reaction forces at transitions

## Advanced Topics

### Real Gas Effects

While ideal gas law suffices for air systems, refrigerants exhibit real gas behavior requiring:

- Compressibility factor Z corrections: P × v = Z × R × T
- Departure functions for enthalpy and entropy
- Equation of state models (Martin-Hou, Benedict-Webb-Rubin)

For refrigerants, use NIST REFPROP or manufacturer software rather than ideal gas approximations.

### Multiphase Flow

Expansion devices often involve two-phase refrigerant flow combining:
- Liquid phase dynamics
- Vapor phase compressible flow
- Phase change (flashing)
- Non-equilibrium thermodynamics

Homogeneous equilibrium models (HEM) provide simplified analysis; drift flux models offer higher accuracy.

### Unsteady Compressible Flow

Transient phenomena relevant to HVAC:
- Pressure wave propagation in pneumatic controls
- Hammer effects in compressed air systems
- Surge in high-speed fans
- Relief valve opening dynamics

Characteristic method and method of characteristics solve transient compressible flow problems.

---

**Related Topics:**
- Incompressible Flow
- Refrigeration Cycle Analysis
- High-Velocity Duct Design
- Pneumatic Controls
- Fan Performance
- Fluid Properties
