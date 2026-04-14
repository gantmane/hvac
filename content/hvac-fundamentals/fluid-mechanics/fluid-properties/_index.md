---
title: "Fluid Properties"
aliases: ["Fluid Properties"]
description: "Fundamental physical properties of fluids used in HVAC systems including density, viscosity, compressibility, and thermal expansion characteristics for water, air, refrigerants, and glycol solutions"
weight: 1
---

Fluid properties define the physical and thermodynamic characteristics that govern fluid behavior in HVAC systems. These properties determine flow rates, pressure drops, heat transfer effectiveness, pump and fan performance, and system energy consumption. Accurate knowledge of fluid properties at operating conditions is critical for proper system design, equipment selection, and performance prediction.

## Density

Density (ρ) represents the mass per unit volume of a fluid and directly affects momentum, pressure drop, and buoyancy forces in HVAC systems.

**Definition:**

ρ = m/V

Where:
- ρ = density (lbm/ft³ or kg/m³)
- m = mass (lbm or kg)
- V = volume (ft³ or m³)

### Temperature Effects on Density

All fluids exhibit density variations with temperature. For liquids, density decreases with increasing temperature. For gases, density is inversely proportional to absolute temperature per the ideal gas law.

**Ideal Gas Law:**

ρ = P/(R·T)

Where:
- P = absolute pressure (psia or Pa)
- R = specific gas constant (ft·lbf/(lbm·°R) or J/(kg·K))
- T = absolute temperature (°R or K)

### Density Values for Common HVAC Fluids

| Fluid | Temperature (°F) | Density (lbm/ft³) | Notes |
|-------|------------------|-------------------|-------|
| Water | 32 | 62.42 | Maximum density at 39.2°F |
| Water | 60 | 62.37 | Standard reference |
| Water | 100 | 62.00 | Cooling water systems |
| Water | 180 | 60.57 | Hot water heating |
| Water | 200 | 60.12 | High temperature systems |
| Air (sea level) | 70 | 0.0749 | Standard conditions |
| Air (sea level) | 0 | 0.0862 | Cold outdoor air |
| R-134a liquid | 40 | 79.89 | Saturated liquid |
| R-410A liquid | 40 | 70.76 | Saturated liquid |
| 30% Ethylene Glycol | 40 | 64.89 | Freeze protection to 15°F |
| 50% Propylene Glycol | 40 | 65.26 | Freeze protection to -28°F |

**ASHRAE Reference:** ASHRAE Handbook - Fundamentals, Chapter 33 (Thermophysical Properties of Refrigerants) and Chapter 34 (Psychrometrics)

### Altitude Effects on Air Density

Air density decreases with elevation, affecting fan performance and air-side heat transfer:

ρ_altitude = ρ_std · (1 - 6.87 × 10^-6 · h)^5.26

Where h = elevation above sea level (ft)

## Specific Gravity

Specific gravity (SG) is the dimensionless ratio of fluid density to the density of water at standard conditions (60°F, 62.37 lbm/ft³).

SG = ρ_fluid / ρ_water

Specific gravity is particularly important for:
- Glycol solution concentrations
- Refrigerant charge calculations
- Pump NPSH requirements
- Hydronic system design

### Specific Gravity Values

| Fluid | Temperature (°F) | Specific Gravity | Application |
|-------|------------------|------------------|-------------|
| Water | 60 | 1.000 | Reference standard |
| Ethylene Glycol (100%) | 60 | 1.115 | Antifreeze concentrate |
| Propylene Glycol (100%) | 60 | 1.036 | Antifreeze concentrate |
| 30% Ethylene Glycol | 60 | 1.040 | Typical freeze protection |
| R-134a liquid | 40 | 1.28 | Refrigerant systems |
| Mercury | 60 | 13.55 | Pressure measurement |

## Specific Weight

Specific weight (γ) represents the weight per unit volume:

γ = ρ·g

Where:
- γ = specific weight (lbf/ft³ or N/m³)
- g = gravitational acceleration (32.174 ft/s² or 9.807 m/s²)

Specific weight is used in hydrostatic pressure calculations and pump head determinations. For water at 60°F: γ = 62.37 lbf/ft³.

## Viscosity

Viscosity quantifies a fluid's resistance to flow and internal shearing forces. It directly impacts pressure drop, pumping power, heat transfer coefficients, and flow regime determination.

### Dynamic (Absolute) Viscosity

Dynamic viscosity (μ) represents the ratio of shear stress to shear rate in a fluid:

τ = μ · (du/dy)

Where:
- τ = shear stress (lbf/ft² or Pa)
- μ = dynamic viscosity (lbm/(ft·s), cP, or Pa·s)
- du/dy = velocity gradient perpendicular to flow (s^-1)

**Unit Conversions:**
- 1 centipoise (cP) = 0.000672 lbm/(ft·s)
- 1 Pa·s = 1000 cP
- 1 lbm/(ft·s) = 1488.2 cP

### Kinematic Viscosity

Kinematic viscosity (ν) is the ratio of dynamic viscosity to density:

ν = μ/ρ

Where:
- ν = kinematic viscosity (ft²/s, cSt, or m²/s)
- 1 centistoke (cSt) = 1.076 × 10^-5 ft²/s

Kinematic viscosity is used in Reynolds number calculations and appears in the Navier-Stokes equations.

### Viscosity Values for HVAC Fluids

| Fluid | Temp (°F) | Dynamic Viscosity (cP) | Kinematic Viscosity (cSt) |
|-------|-----------|------------------------|---------------------------|
| Water | 32 | 1.79 | 1.93 |
| Water | 60 | 1.12 | 1.22 |
| Water | 100 | 0.68 | 0.74 |
| Water | 180 | 0.35 | 0.39 |
| Air | 32 | 0.0171 | 13.23 |
| Air | 70 | 0.0181 | 16.15 |
| Air | 212 | 0.0220 | 33.44 |
| 30% Ethylene Glycol | 40 | 3.24 | 3.37 |
| 50% Propylene Glycol | 40 | 6.10 | 6.31 |
| R-134a liquid | 40 | 0.270 | 0.228 |

### Temperature Effects on Viscosity

**Liquids:** Viscosity decreases exponentially with temperature:

μ = A · e^(B/T)

Where A and B are empirical constants specific to each fluid.

**Gases:** Viscosity increases with temperature per Sutherland's law:

μ = μ_0 · (T/T_0)^(3/2) · [(T_0 + S)/(T + S)]

For air: S = 110.4 K (Sutherland constant)

**ASHRAE Reference:** ASHRAE Handbook - Fundamentals, Chapter 1 (Psychrometrics), provides detailed viscosity correlations.

## Newtonian vs. Non-Newtonian Fluids

### Newtonian Fluids

Newtonian fluids exhibit constant viscosity regardless of shear rate. The shear stress is directly proportional to shear rate. Most HVAC fluids are Newtonian:

- Water
- Air
- Refrigerants
- Glycol solutions (at typical concentrations)
- Hydronic oils

Standard pipe friction correlations (Darcy-Weisbach, Colebrook equation) apply directly to Newtonian fluids.

### Non-Newtonian Fluids

Non-Newtonian fluids exhibit viscosity changes with shear rate. Examples in specialized HVAC applications:

- High-concentration polymeric additives
- Some thermal storage phase-change materials
- Certain heat transfer fluids at extreme temperatures

**Types:**
1. Pseudoplastic (shear-thinning): viscosity decreases with shear rate
2. Dilatant (shear-thickening): viscosity increases with shear rate
3. Bingham plastic: requires threshold stress before flow begins

Non-Newtonian behavior requires specialized friction factor correlations and computational fluid dynamics analysis.

## Compressibility

Compressibility quantifies the volume change of a fluid under pressure variations.

### Bulk Modulus of Elasticity

The bulk modulus (K or β) measures resistance to compression:

K = -V · (dP/dV) = ρ · (dP/dρ)

Where:
- K = bulk modulus (psi or Pa)
- V = volume
- P = pressure

**Practical Values:**

| Fluid | Temperature (°F) | Bulk Modulus (psi) | Compressibility |
|-------|------------------|---------------------|-----------------|
| Water | 60 | 320,000 | Nearly incompressible |
| Water | 200 | 270,000 | Decreases with temperature |
| Ethylene Glycol | 60 | 420,000 | Less compressible than water |
| Air | 60 | 14.7 (at 1 atm) | Highly compressible |
| Hydraulic Oil | 60 | 250,000 | Used in controls |

### Compressibility Coefficient

β = 1/K = -(1/V) · (dV/dP)

For liquids in hydronic systems, compressibility is typically negligible in pressure drop calculations but becomes important in:
- Water hammer analysis
- Expansion tank sizing
- Pressure surge protection
- Acoustic wave propagation

**ASHRAE Reference:** ASHRAE Handbook - HVAC Systems and Equipment, Chapter 13 (Hydronic Heating and Cooling Systems)

### Speed of Sound

The speed of sound in a fluid relates directly to compressibility:

c = √(K/ρ)

For water at 60°F: c ≈ 4,900 ft/s
For air at 70°F: c ≈ 1,130 ft/s

## Coefficient of Thermal Expansion

The volumetric coefficient of thermal expansion (β_T) quantifies volume change with temperature:

β_T = (1/V) · (dV/dT)_P

Or for density:

β_T = -(1/ρ) · (dρ/dT)_P

### Thermal Expansion Values

| Fluid | Temperature Range (°F) | β_T (1/°F) | Application Impact |
|-------|------------------------|------------|---------------------|
| Water | 40-200 | 2.1 × 10^-4 | Expansion tank sizing |
| Ethylene Glycol | 40-200 | 3.5 × 10^-4 | Larger expansion tanks |
| Propylene Glycol | 40-200 | 3.8 × 10^-4 | Larger expansion tanks |
| Air (ideal gas) | All | 1/T_abs | Density altitude correction |

### Hydronic System Expansion Volume

The total expansion volume in a closed hydronic system:

V_exp = V_sys · β_T · ΔT

Where:
- V_exp = expansion volume (gal)
- V_sys = total system volume (gal)
- ΔT = temperature change from fill to maximum operating (°F)

This calculation is critical for expansion tank selection per ASHRAE Standard 12 (Minimizing the Risk of Legionellosis).

## Surface Tension

Surface tension (σ) is the force per unit length at the interface between liquid and gas:

σ = F/L

Units: lbf/ft, dyne/cm, or N/m

### Surface Tension Values

| Fluid | Temperature (°F) | Surface Tension (dyne/cm) |
|-------|------------------|---------------------------|
| Water | 60 | 73.0 |
| Water | 212 | 58.9 |
| Ethylene Glycol | 60 | 48.4 |
| R-134a | 40 | 12.3 |

**HVAC Applications:**
- Droplet formation in cooling coils
- Condensate drainage behavior
- Evaporative cooling effectiveness
- Spray nozzle atomization
- Drain pan design

## Capillarity

Capillary action results from the combination of surface tension and adhesive forces between liquid and solid surfaces.

### Capillary Rise

The height of capillary rise in a tube:

h = (2·σ·cos θ)/(ρ·g·r)

Where:
- h = capillary rise height (ft)
- σ = surface tension (lbf/ft)
- θ = contact angle (degrees)
- r = tube radius (ft)

**HVAC Relevance:**
- Condensate drainage in small tubes
- Wicking in insulation materials
- Drain line trap seal maintenance
- Microgroove heat exchanger design

## Vapor Pressure

Vapor pressure is the pressure exerted by a vapor in equilibrium with its liquid phase at a given temperature. It increases exponentially with temperature.

### Antoine Equation

log₁₀(P_vap) = A - B/(C + T)

Where A, B, C are substance-specific constants.

### Vapor Pressure Values for Water

| Temperature (°F) | Vapor Pressure (psia) | Significance |
|------------------|----------------------|--------------|
| 32 | 0.0887 | Freezing point |
| 60 | 0.2563 | Standard conditions |
| 100 | 0.9503 | Cooling tower range |
| 180 | 7.510 | Hot water systems |
| 212 | 14.696 | Atmospheric boiling |

**ASHRAE Reference:** ASHRAE Handbook - Fundamentals, Chapter 1 (Psychrometrics), Steam tables

### HVAC Design Implications

1. **NPSH Requirements:** Net Positive Suction Head must exceed vapor pressure to prevent cavitation:

   NPSH_available = P_atm + P_static - P_friction - P_vapor

2. **Cooling Tower Performance:** Wet bulb temperature approach limited by vapor pressure differential

3. **Dehumidification:** Coil surface temperature must be below dewpoint (vapor pressure determines saturation)

4. **Vacuum Systems:** Steam condensers operate below atmospheric pressure

## Cavitation Phenomenon

Cavitation occurs when local pressure in a liquid drops below vapor pressure, causing vapor bubble formation, subsequent collapse, and potential equipment damage.

### Cavitation Index

The Thoma cavitation parameter (σ):

σ = (NPSH_available)/(H_pump)

Where H_pump = total pump head developed (ft)

Cavitation risk increases when σ < σ_critical (typically 0.1-0.4 for centrifugal pumps)

### Cavitation Prevention Strategies

1. **Increase NPSH_available:**
   - Elevate fluid source above pump
   - Minimize suction line friction
   - Reduce suction line length
   - Increase pipe diameter
   - Lower fluid temperature

2. **System Design:**
   - Position pumps at lowest point
   - Use suction diffusers
   - Avoid elbows near pump inlet
   - Provide adequate submergence in open systems

3. **Pump Selection:**
   - Select pumps with low NPSH_required
   - Use double-suction impellers
   - Consider inducer-equipped pumps

**ASHRAE Reference:** ASHRAE Handbook - HVAC Systems and Equipment, Chapter 44 (Pumps)

### Cavitation Damage Indicators

- High-frequency noise and vibration (sounds like gravel)
- Reduced pump performance
- Eroded impeller surfaces (pitting)
- Mechanical seal failure
- Bearing damage

## Pressure-Temperature-Density Relationships

### Incompressible Flow Assumption

For liquids in hydronic systems, density remains constant:

ρ ≈ constant (for ΔP << 1000 psi)

This assumption simplifies:
- Bernoulli equation application
- Pump head calculations
- Pipe sizing procedures
- Flow measurement

### Compressible Flow Criteria

Air and refrigerant vapor must account for density changes when:

M = V/c > 0.3 (Mach number)

Or pressure drop exceeds:

ΔP/P > 0.1

**Compressible Flow Applications:**
- High-velocity duct systems (>4,000 fpm)
- Refrigerant suction lines (high Mach number)
- Steam systems above 50 psig
- Air compressor discharge lines

## Property Determination Methods

### For Liquids (Water, Glycols)

1. **Reference Tables:** ASHRAE Fundamentals Chapter 34
2. **Polynomial Correlations:** Curve-fit equations for temperature dependency
3. **Manufacturer Data:** Glycol concentration effects (Dow, MEGlobal)
4. **Software:** REFPROP, Engineering Equation Solver (EES)

### For Gases (Air, Refrigerant Vapor)

1. **Ideal Gas Law:** Accurate for air at HVAC conditions
2. **Real Gas Equations:** Benedict-Webb-Rubin for refrigerants
3. **Psychrometric Charts:** Air-water vapor mixtures
4. **REFPROP Database:** NIST-certified properties

### For Refrigerants

1. **ASHRAE Standard 34:** Refrigerant designation and safety classification
2. **REFPROP 10.0:** Reference fluid properties database
3. **Martin-Hou Equation of State:** Industrial refrigerant calculations
4. **Manufacturer Software:** Refrigerant property calculators

## Design Considerations

### Fluid Selection Criteria

| Property | Water | Glycol Solutions | Refrigerants | Air |
|----------|-------|------------------|--------------|-----|
| Heat Capacity | Excellent | Good (20% penalty) | Fair | Poor |
| Density | High | High | Variable | Very Low |
| Viscosity | Low | Moderate-High | Low | Very Low |
| Toxicity | None | Low (propylene) | Varies by class | None |
| Flammability | None | Low | Varies by class | Supports combustion |
| Cost | Lowest | Moderate | High | Free |

### Temperature-Dependent Property Effects

1. **Hot Water Systems (140-200°F):**
   - Reduced density (2-4% lower than 60°F)
   - Significantly lower viscosity (60-70% reduction)
   - Higher vapor pressure (requires system pressurization)
   - Expansion tank sizing critical

2. **Chilled Water Systems (40-55°F):**
   - Increased viscosity (40-60% higher than 60°F)
   - Higher density (slight increase)
   - Condensation risk at pipe surfaces
   - Glycol addition impacts all properties

3. **Glycol Solutions:**
   - All properties degrade compared to water
   - Pumping power increases 30-80% for 30-50% concentrations
   - Heat transfer penalty 5-15%
   - Freeze protection vs. performance tradeoff

### Altitude Corrections

Air density at altitude affects:

**Fan Performance:**
- BHP_altitude = BHP_std · (ρ_altitude/ρ_std)
- Pressure developed remains constant (in inches w.c.)
- Motor may be oversized at altitude

**Heat Transfer:**
- Reduced mass flow for same volumetric flow
- Sensible capacity proportional to density
- Coil face velocity correction required

**Burner Performance:**
- Reduced oxygen availability
- Deration factors for gas-fired equipment
- Combustion air fan sizing critical

### Pressure Drop Implications

Property effects on pressure drop (Darcy-Weisbach):

ΔP = f · (L/D) · (ρ·V²/2)

Where f depends on Reynolds number:

Re = (ρ·V·D)/μ = (V·D)/ν

**Key Relationships:**
1. Pressure drop proportional to density
2. Friction factor inversely related to Reynolds number (in laminar flow)
3. Viscosity increase substantially raises pumping power
4. Temperature changes affect both ρ and μ simultaneously

## Best Practices

1. **Use actual fluid properties at operating conditions** - not handbook values at 60°F
2. **Account for glycol concentration effects** - particularly viscosity and heat capacity
3. **Verify altitude corrections** for fan and burner selections above 1,000 ft
4. **Calculate NPSH margin** - maintain at least 5 ft above pump requirement
5. **Consider temperature cycling** - expansion/contraction in system design
6. **Update properties in energy models** - seasonal variations affect performance
7. **Document fluid specifications** - concentration, additives, inhibitors
8. **Test actual fluid properties** - particularly in critical applications
9. **Account for degradation** - glycol breakdown, refrigerant contamination
10. **Reference current ASHRAE data** - properties updated with research

## Code and Standard References

- **ASHRAE Handbook - Fundamentals:** Chapters 1, 33, 34 (Property data)
- **ASHRAE Standard 34:** Refrigerant designation and safety
- **ASHRAE Standard 12:** Legionellosis risk minimization
- **NIST REFPROP:** Thermophysical property database
- **Hydraulic Institute Standards:** Pump NPSH requirements
- **SMACNA HVAC Systems Duct Design:** Air property applications
- **ASME B31.9:** Building services piping (pressure-temperature ratings)

## Related Topics

- [Density Compressibility](density-compressibility/)
- [Specific Gravity](specific-gravity/)
- [Specific Weight](specific-weight/)
- [Viscosity Dynamic](viscosity-dynamic/)
- [Viscosity Kinematic](viscosity-kinematic/)
- [Newtonian Fluids](newtonian-fluids/)
- [Non Newtonian Fluids](non-newtonian-fluids/)
- [Surface Tension](surface-tension/)
- [Capillarity](capillarity/)
- [Vapor Pressure](vapor-pressure/)
- [Cavitation Phenomenon](cavitation-phenomenon/)
- [Bulk Modulus](bulk-modulus/)
- [Coefficient Thermal Expansion](coefficient-thermal-expansion/)
