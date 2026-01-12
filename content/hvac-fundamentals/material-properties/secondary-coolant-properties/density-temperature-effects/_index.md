---
title: "Density Temperature Effects"
description: "Comprehensive analysis of density-temperature relationships in secondary coolants including thermal expansion coefficients, volumetric effects, system design implications, and engineering calculations for glycol and brine solutions"
weight: 6
---

## Physical Principles

The density of secondary coolants varies with temperature according to fundamental thermodynamic relationships governing molecular spacing and thermal expansion. Understanding these effects is critical for proper system design, expansion tank sizing, pump selection, and fluid charge calculations.

### Fundamental Density-Temperature Relationship

Density decreases with increasing temperature due to thermal expansion of the liquid phase. For most secondary coolants, this relationship follows:

**General Density Equation:**

ρ(T) = ρ₀ / [1 + β(T - T₀)]

Where:
- ρ(T) = density at temperature T (lb/ft³ or kg/m³)
- ρ₀ = reference density at T₀ (lb/ft³ or kg/m³)
- β = volumetric thermal expansion coefficient (1/°F or 1/°C)
- T = operating temperature (°F or °C)
- T₀ = reference temperature (°F or °C)

### Thermal Expansion Coefficient

The volumetric thermal expansion coefficient quantifies the fractional change in volume per degree temperature change:

**Volumetric Expansion:**

β = (1/V)(∂V/∂T)ₚ = -(1/ρ)(∂ρ/∂T)ₚ

Where measurements occur at constant pressure.

**Relationship to Linear Expansion:**

For isotropic materials: β ≈ 3α

Where α is the linear coefficient of thermal expansion.

## Glycol Solution Density Properties

### Ethylene Glycol Density Data

Ethylene glycol solutions exhibit concentration and temperature-dependent density variations critical for system calculations.

**Density at 68°F (20°C) by Concentration:**

| Concentration (% by weight) | Density (lb/ft³) | Density (kg/m³) | Specific Gravity |
|----------------------------|------------------|-----------------|------------------|
| 0 (Pure Water) | 62.30 | 998.2 | 0.998 |
| 10 | 63.15 | 1011.8 | 1.013 |
| 20 | 63.95 | 1024.6 | 1.026 |
| 30 | 64.70 | 1036.6 | 1.038 |
| 40 | 65.40 | 1047.8 | 1.049 |
| 50 | 66.05 | 1058.2 | 1.060 |
| 60 | 66.60 | 1067.0 | 1.069 |
| 70 | 67.10 | 1075.0 | 1.077 |
| 80 | 67.50 | 1081.4 | 1.083 |
| 90 | 67.85 | 1087.0 | 1.089 |
| 100 (Pure EG) | 68.15 | 1091.6 | 1.093 |

**Temperature Correction Factors:**

Density at temperature T: ρ(T) = ρ₂₀°C × f(T)

| Temperature (°F) | Temperature (°C) | Correction Factor f(T) |
|-----------------|------------------|------------------------|
| -40 | -40 | 1.055 |
| -20 | -29 | 1.045 |
| 0 | -18 | 1.035 |
| 20 | -7 | 1.025 |
| 32 | 0 | 1.020 |
| 40 | 4 | 1.015 |
| 60 | 16 | 1.005 |
| 68 | 20 | 1.000 |
| 80 | 27 | 0.995 |
| 100 | 38 | 0.985 |
| 120 | 49 | 0.975 |
| 140 | 60 | 0.965 |
| 160 | 71 | 0.955 |
| 180 | 82 | 0.945 |
| 200 | 93 | 0.935 |

### Propylene Glycol Density Data

Propylene glycol exhibits slightly different density characteristics than ethylene glycol.

**Density at 68°F (20°C) by Concentration:**

| Concentration (% by weight) | Density (lb/ft³) | Density (kg/m³) | Specific Gravity |
|----------------------------|------------------|-----------------|------------------|
| 0 (Pure Water) | 62.30 | 998.2 | 0.998 |
| 10 | 63.10 | 1010.9 | 1.012 |
| 20 | 63.85 | 1023.0 | 1.025 |
| 30 | 64.55 | 1034.2 | 1.036 |
| 40 | 65.20 | 1044.6 | 1.046 |
| 50 | 65.80 | 1054.2 | 1.056 |
| 60 | 66.35 | 1063.0 | 1.065 |
| 70 | 66.85 | 1071.0 | 1.073 |
| 80 | 67.30 | 1078.2 | 1.080 |
| 90 | 67.70 | 1084.6 | 1.086 |
| 100 (Pure PG) | 68.05 | 1090.0 | 1.092 |

**Thermal Expansion Coefficients (Propylene Glycol):**

| Concentration (% by weight) | β at 68°F (10⁻⁴/°F) | β at 20°C (10⁻⁴/°C) |
|----------------------------|---------------------|---------------------|
| 0 (Pure Water) | 1.17 | 2.07 |
| 25 | 3.00 | 5.40 |
| 50 | 3.50 | 6.30 |
| 75 | 4.00 | 7.20 |
| 100 (Pure PG) | 4.40 | 7.92 |

## Brine Solution Density Properties

### Calcium Chloride Brine

Calcium chloride solutions provide freeze protection for low-temperature applications.

**Density at 68°F (20°C):**

| Concentration (% by weight) | Density (lb/ft³) | Density (kg/m³) | Specific Gravity |
|----------------------------|------------------|-----------------|------------------|
| 0 | 62.30 | 998.2 | 0.998 |
| 5 | 63.50 | 1017.4 | 1.019 |
| 10 | 64.75 | 1037.4 | 1.039 |
| 15 | 66.05 | 1058.2 | 1.060 |
| 20 | 67.40 | 1079.8 | 1.082 |
| 25 | 68.80 | 1102.2 | 1.104 |
| 30 | 70.25 | 1125.4 | 1.127 |

**Thermal Expansion Coefficient:**

For CaCl₂ solutions: β ≈ 2.5 × 10⁻⁴ to 3.5 × 10⁻⁴ /°F (4.5 × 10⁻⁴ to 6.3 × 10⁻⁴ /°C)

### Sodium Chloride Brine

Sodium chloride provides economical freeze protection with moderate temperature range.

**Density at 68°F (20°C):**

| Concentration (% by weight) | Density (lb/ft³) | Density (kg/m³) | Specific Gravity |
|----------------------------|------------------|-----------------|------------------|
| 0 | 62.30 | 998.2 | 0.998 |
| 5 | 63.35 | 1015.0 | 1.017 |
| 10 | 64.45 | 1032.6 | 1.034 |
| 15 | 65.55 | 1050.2 | 1.052 |
| 20 | 66.70 | 1068.6 | 1.070 |
| 23.3 (Eutectic) | 67.35 | 1079.0 | 1.081 |

## System Design Calculations

### Volume Change with Temperature

The total volume change in a closed system between temperatures T₁ and T₂:

**Volume Expansion Equation:**

ΔV = V₁ × β × (T₂ - T₁)

Where:
- ΔV = volume change (gal or L)
- V₁ = initial system volume (gal or L)
- β = volumetric expansion coefficient (1/°F or 1/°C)
- T₂ - T₁ = temperature change (°F or °C)

**Percent Volume Change:**

% Volume Change = β × ΔT × 100

### Expansion Tank Sizing

Proper expansion tank sizing accommodates fluid volume changes while maintaining system pressure.

**Minimum Expansion Tank Volume:**

**For Diaphragm Tanks:**

V_t = (V_s × ΔV_f × [(P_m + 14.7)/(P_m - P_f + 14.7)]) / (1 - P_a/P_m)

Where:
- V_t = minimum tank volume (gal)
- V_s = system fluid volume (gal)
- ΔV_f = volumetric expansion factor (dimensionless)
- P_m = maximum system pressure (psig)
- P_f = fill pressure (psig)
- P_a = atmospheric pressure = 14.7 psia

**Simplified Expansion Tank Formula:**

V_t = V_s × [β × ΔT / (1 - (P_f + 14.7)/(P_m + 14.7))]

**Volumetric Expansion Factors (ΔV_f):**

| Fluid | Temp Range (°F) | ΔV_f | Temp Range (°C) | ΔV_f |
|-------|----------------|------|----------------|------|
| Water | 40 to 200 | 0.0359 | 4 to 93 | 0.0359 |
| 30% EG | 0 to 200 | 0.0480 | -18 to 93 | 0.0480 |
| 50% EG | -20 to 200 | 0.0540 | -29 to 93 | 0.0540 |
| 30% PG | 0 to 200 | 0.0495 | -18 to 93 | 0.0495 |
| 50% PG | -20 to 200 | 0.0560 | -29 to 93 | 0.0560 |

### System Fill Volume Calculations

Determining proper system charge requires accounting for density at fill temperature.

**Mass-Based Fill Calculation:**

m = ρ_fill × V_system

Where:
- m = total fluid mass (lb or kg)
- ρ_fill = density at fill temperature (lb/ft³ or kg/m³)
- V_system = total system volume (ft³ or m³)

**Volume Conversion:**

V_gal = V_ft³ × 7.48052

V_L = V_m³ × 1000

### Pumping Head Corrections

Density variations affect static head calculations in vertical systems.

**Static Head Pressure:**

P_static = ρ × g × h / 144

Where:
- P_static = static pressure (psi)
- ρ = fluid density (lb/ft³)
- g = gravitational acceleration = 32.174 ft/s²
- h = vertical height (ft)
- 144 = conversion factor (in²/ft²)

**Static Head per Foot of Elevation:**

For water at 68°F: 0.433 psi/ft
For 30% ethylene glycol at 68°F: 0.446 psi/ft
For 50% ethylene glycol at 68°F: 0.455 psi/ft

**Density Correction Factor:**

P_glycol = P_water × (ρ_glycol / ρ_water)

## ASHRAE References

Design values and calculation methods derived from:

**ASHRAE Handbook - Fundamentals:**
- Chapter 31: Physical Properties of Secondary Coolants (Brines)
- Table 3: Thermophysical Properties of Ethylene Glycol Solutions
- Table 4: Thermophysical Properties of Propylene Glycol Solutions
- Table 7: Properties of Aqueous Solutions of Calcium Chloride
- Table 8: Properties of Aqueous Solutions of Sodium Chloride

**ASHRAE Handbook - HVAC Systems and Equipment:**
- Chapter 13: Hydronic Heating and Cooling System Design
- Section on Secondary Coolants and Freeze Protection

## Engineering Design Considerations

### System Volume Calculations

Accurate total system volume determination is essential for expansion tank sizing and fluid charge calculations.

**System Volume Components:**

1. **Piping Volume:**
   - V_pipe = (π/4) × D² × L × n
   - Account for all supply, return, and branch piping

2. **Equipment Volume:**
   - Heat exchangers: manufacturer data
   - Air handling units: coil manufacturer data
   - Buffer tanks: calculated or manufacturer volume
   - Chiller evaporator: manufacturer data

3. **Fitting and Valve Allowance:**
   - Add 5-10% for fittings, valves, and miscellaneous

**Total System Volume:**

V_total = V_piping + V_equipment + V_fittings

### Temperature Range Considerations

Design for the full temperature swing the system will experience.

**Critical Temperature Points:**

1. **Minimum Fill Temperature:**
   - Typically outdoor ambient during installation
   - May be 40-50°F in cold climates

2. **Maximum Operating Temperature:**
   - Design supply or return temperature
   - Consider upset conditions and safety factors

3. **Design Temperature Differential:**
   - ΔT_design = T_max - T_fill
   - Use for expansion calculations

### Concentration Effects on Density

Glycol concentration must be considered in density calculations.

**Concentration Selection Criteria:**

1. **Freeze Protection:**
   - Determine lowest ambient or process temperature
   - Add 10-15°F safety margin
   - Select minimum concentration from freeze point data

2. **Density Impact:**
   - Higher concentrations increase density
   - Affects pump head and system static pressure
   - Influences expansion tank sizing

3. **Performance Optimization:**
   - Use minimum concentration for required protection
   - Reduces viscosity and improves heat transfer
   - Minimizes pumping energy

### Expansion Accommodation Methods

Systems must accommodate thermal expansion through various means.

**Open Systems:**
- Vented to atmosphere
- Free expansion into open tank
- No pressurization concerns
- Limited to low-temperature applications

**Closed Systems - Compression Tank:**
- Air cushion compresses with expansion
- Requires periodic air charging
- Air absorption over time reduces capacity
- Mostly obsolete for new construction

**Closed Systems - Diaphragm Tank:**
- Membrane separates fluid from air charge
- Prevents air absorption
- Factory-pressurized air side
- Standard for modern hydronic systems
- Requires proper sizing calculation

**Closed Systems - Bladder Tank:**
- Replaceable bladder isolates fluid
- Similar function to diaphragm
- Serviceable bladder element
- Higher initial cost

### Pressure Relief Considerations

Thermal expansion creates pressure rise that must be safely relieved.

**Pressure Relief Valve Sizing:**

Required capacity based on thermal expansion rate and valve response time. Per ASME Section IV:

**Relief Capacity:**

Q = (V_s × β × ΔT × ρ × C_p × ΔT_max) / (t × 3600)

Where:
- Q = relief capacity (Btu/hr)
- t = time to relieve (hours)
- C_p = specific heat (Btu/lb·°F)

**Standard Practice:**
- Provide pressure relief valve on systems >15 psig
- Set relief pressure below maximum equipment rating
- Typical settings: 30-50 psig for standard systems
- Pipe relief discharge to visible location

### Instrumentation Requirements

Monitor density-related parameters for proper system operation.

**Key Monitoring Points:**

1. **System Pressure:**
   - Expansion tank connection point
   - High point in system
   - Pump suction (NPSH verification)

2. **Temperature:**
   - Supply and return temperatures
   - Expansion tank location temperature
   - Fill temperature during charging

3. **Fluid Level/Volume:**
   - Visual level gauge on compression tanks
   - Pressure indication on diaphragm tanks
   - Makeup water metering

4. **Concentration Verification:**
   - Refractometer testing
   - Specific gravity measurement
   - Freeze point testing

### Seasonal Effects

Annual temperature cycles create expansion and contraction patterns.

**Annual Cycle Considerations:**

1. **Summer Expansion:**
   - Warmest fill condition
   - Maximum system pressure
   - Potential relief valve operation

2. **Winter Contraction:**
   - Coldest system condition
   - Minimum system pressure
   - Potential for air ingestion if pressure too low

3. **Fill Pressure Selection:**
   - Must prevent cavitation at pump suction year-round
   - Maintain minimum positive pressure at all points
   - Typical fill: 12-15 psig for systems <50 ft height

### High-Rise Building Applications

Vertical height creates significant static pressure variations.

**Static Pressure Gradient:**

ΔP_static = (ρ × g × h) / 144

**For 100 ft elevation change:**
- Water: 43.3 psi
- 30% EG: 44.6 psi
- 50% EG: 45.5 psi

**Design Implications:**

1. **Pressure Zoning:**
   - Separate systems for pressure zones
   - Typically zone every 300-400 ft
   - Intermediate heat exchangers between zones

2. **Expansion Tank Location:**
   - Place at point of no pressure change
   - Typically on pump suction
   - Account for elevation head to all points

3. **Fill Pressure Calculation:**
   - Must overcome static head to highest point
   - Add NPSH requirement
   - Add safety margin (5-10 psi)

## Practical Application Examples

### Example 1: Expansion Tank Sizing

**Given:**
- System volume: 500 gallons
- Fluid: 30% propylene glycol
- Fill temperature: 50°F
- Maximum temperature: 180°F
- Fill pressure: 15 psig
- Maximum pressure: 50 psig

**Solution:**

1. Temperature change: ΔT = 180 - 50 = 130°F

2. Expansion coefficient for 30% PG: β = 3.0 × 10⁻⁴ /°F

3. Volumetric expansion: ΔV_f = β × ΔT = 3.0 × 10⁻⁴ × 130 = 0.039

4. Tank volume:
   V_t = 500 × [0.039 / (1 - (15+14.7)/(50+14.7))]
   V_t = 500 × [0.039 / (1 - 0.459)]
   V_t = 500 × 0.072 = 36 gallons

**Select:** 40-gallon diaphragm expansion tank (next standard size)

### Example 2: System Fill Calculation

**Given:**
- Total system volume: 300 ft³
- Fluid: 40% ethylene glycol
- Fill temperature: 60°F

**Solution:**

1. Density at 60°F for 40% EG:
   - Base density at 68°F: 65.40 lb/ft³
   - Correction factor at 60°F: ≈ 1.003
   - ρ = 65.40 × 1.003 = 65.60 lb/ft³

2. Total mass required:
   m = 65.60 lb/ft³ × 300 ft³ = 19,680 lb

3. Volume in gallons:
   V = 300 ft³ × 7.48052 gal/ft³ = 2,244 gallons

### Example 3: Pump Head Correction

**Given:**
- Vertical elevation: 80 ft
- Fluid: 50% propylene glycol at 40°F
- Water-based pump curve provided

**Solution:**

1. Density of 50% PG at 40°F:
   - Base density at 68°F: 65.80 lb/ft³
   - Correction factor at 40°F: ≈ 1.015
   - ρ_PG = 65.80 × 1.015 = 66.79 lb/ft³

2. Density of water at 40°F: ρ_water = 62.42 lb/ft³

3. Static head correction:
   - Water equivalent: 80 ft × (62.42/62.42) = 80 ft
   - PG actual: 80 ft × (66.79/62.42) = 85.6 ft

4. Additional head required: 85.6 - 80 = 5.6 ft

**Pump must overcome additional 5.6 ft head due to higher density**

## Maintenance and Operations

### Periodic Testing

Regular verification ensures system maintains design parameters.

**Testing Schedule:**

1. **Annual:**
   - Freeze point testing
   - Specific gravity measurement
   - pH testing
   - Inhibitor concentration

2. **Semi-Annual:**
   - System pressure verification
   - Expansion tank pressure check
   - Visual inspection for leaks

3. **As Needed:**
   - After makeup water addition
   - Following system modifications
   - Post-leak repairs

### Makeup and Recharge Procedures

Maintain proper concentration and volume throughout system life.

**Makeup Requirements:**

1. **Concentration Matching:**
   - Match existing system concentration
   - Pre-mix makeup solution
   - Verify with refractometer

2. **Volume Calculation:**
   - Determine volume loss
   - Account for density at makeup temperature
   - Add through fill connection

3. **Documentation:**
   - Record makeup volume and date
   - Track concentration changes
   - Monitor for excessive makeup (leak indication)

---

**Related Topics:**
- Specific Heat Capacity
- Viscosity Temperature Effects
- Thermal Conductivity Properties
- Freeze Point Depression
- Corrosion Inhibitors
