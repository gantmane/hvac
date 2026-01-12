---
title: "Enthalpy and Entropy of Water"
description: "Thermodynamic properties of water and steam including enthalpy, entropy, property tables, and applications in HVAC system design and analysis"
weight: 5
---

## Thermodynamic Property Definitions

Enthalpy and entropy are fundamental thermodynamic properties essential for HVAC system analysis, steam system design, refrigeration cycle calculations, and energy balance computations.

### Enthalpy (h)

Enthalpy represents the total heat content of a substance per unit mass, combining internal energy and flow work:

**h = u + Pv**

Where:
- h = specific enthalpy (Btu/lbm or kJ/kg)
- u = specific internal energy (Btu/lbm or kJ/kg)
- P = absolute pressure (lbf/ft² or Pa)
- v = specific volume (ft³/lbm or m³/kg)

#### Physical Significance

Enthalpy quantifies the energy required to create a system and make space for it by displacing its environment. In HVAC applications, enthalpy differences determine heat transfer requirements for heating, cooling, humidification, and phase change processes.

For water/steam systems, enthalpy serves as the primary property for:
- Boiler energy input calculations
- Condensate return energy recovery
- Steam trap sizing and selection
- Heat exchanger thermal analysis
- Turbine work output determination

### Entropy (s)

Entropy measures the thermal energy per unit temperature unavailable for performing useful work, representing the degree of molecular disorder:

**ds = δQ/T** (for reversible processes)

Where:
- s = specific entropy (Btu/lbm·°R or kJ/kg·K)
- δQ = differential heat transfer (Btu or kJ)
- T = absolute temperature (°R or K)

#### Physical Significance

Entropy quantifies:
- Irreversibility of real processes
- Quality degradation of energy during conversion
- Direction of spontaneous processes (second law of thermodynamics)
- Maximum theoretical work obtainable from a heat engine
- Minimum theoretical work required for refrigeration

In HVAC systems, entropy analysis enables:
- Identification of major inefficiency sources
- Optimization of component performance
- Evaluation of thermodynamic perfection (isentropic efficiency)
- Second-law analysis of system performance

## Water Phase Relationships

### Saturation Conditions

At saturation, liquid and vapor phases coexist in thermodynamic equilibrium. Saturation temperature and pressure are dependent properties—specifying one fixes the other.

#### Subcooled (Compressed) Liquid

Liquid water below saturation temperature at a given pressure. Properties approximately equal saturated liquid properties at the same temperature:

**h_f ≈ h_f@T** (pressure effect negligible for most HVAC applications)

Typical applications:
- Condensate in steam systems (below saturation)
- Chilled water systems (35-50°F)
- Hot water heating systems (120-250°F)
- Boiler feedwater (prior to economizer)

#### Saturated Liquid

Liquid water at saturation temperature for a given pressure, ready to vaporize with any additional heat input. Properties denoted with subscript "f":

- h_f = enthalpy of saturated liquid (Btu/lbm or kJ/kg)
- s_f = entropy of saturated liquid (Btu/lbm·°R or kJ/kg·K)

#### Saturated Vapor

Vapor at saturation temperature for a given pressure, ready to condense with any heat removal. Properties denoted with subscript "g":

- h_g = enthalpy of saturated vapor (Btu/lbm or kJ/kg)
- s_g = entropy of saturated vapor (Btu/lbm·°R or kJ/kg·K)

#### Superheated Vapor

Vapor above saturation temperature at a given pressure. Temperature and pressure are independent properties in the superheat region. Degree of superheat:

**Δt_superheat = t_actual - t_sat@P**

Applications:
- Power generation turbine inlet steam (high superheat)
- Steam heating systems (minimal superheat, typically 5-15°F)
- Refrigeration compressor discharge (30-80°F superheat)

### Latent Heat of Vaporization (h_fg)

The energy required to convert saturated liquid to saturated vapor at constant temperature and pressure:

**h_fg = h_g - h_f**

Temperature dependence of latent heat:

| Temperature (°F) | Pressure (psia) | h_fg (Btu/lbm) |
|------------------|-----------------|----------------|
| 32 | 0.0886 | 1075.4 |
| 100 | 0.9503 | 1037.0 |
| 212 | 14.696 | 970.3 |
| 250 | 29.825 | 945.5 |
| 300 | 67.028 | 910.1 |
| 350 | 134.63 | 863.6 |
| 400 | 247.31 | 804.6 |
| 450 | 422.6 | 730.0 |
| 500 | 680.8 | 631.4 |
| 550 | 1045.4 | 493.9 |
| 600 | 1542.9 | 296.6 |
| 705.4 (critical) | 3206.2 | 0 |

Note: Latent heat decreases with increasing temperature, reaching zero at the critical point (705.4°F, 3206.2 psia).

### Quality (Dryness Fraction)

For two-phase mixtures, quality (x) defines the mass fraction of vapor:

**x = m_vapor / (m_liquid + m_vapor)**

Range: 0 ≤ x ≤ 1

- x = 0: saturated liquid
- 0 < x < 1: two-phase mixture
- x = 1: saturated vapor

Properties in the two-phase region:

**h = h_f + x·h_fg**

**s = s_f + x·s_fg**

**v = v_f + x·v_fg**

Steam quality considerations in HVAC:
- Boiler steam quality: x ≥ 0.98 minimum (ASME guidelines)
- Steam heating systems: x ≥ 0.95 recommended
- Steam turbines: x ≥ 0.88 at exhaust (erosion prevention)
- Flash steam recovery: quality calculation determines flash quantity

## Temperature and Pressure Relationships

### Clausius-Clapeyron Equation

Describes the relationship between saturation pressure and temperature:

**dP/dT = h_fg / (T·v_fg)**

Or in integrated approximation form:

**ln(P₂/P₁) = (h_fg/R_v)·(1/T₁ - 1/T₂)**

Where:
- P = saturation pressure (absolute)
- T = saturation temperature (absolute)
- h_fg = latent heat of vaporization
- v_fg = difference in specific volume (v_g - v_f)
- R_v = specific gas constant for water vapor (0.1102 Btu/lbm·°R or 461.5 J/kg·K)

### Pressure-Temperature Correlation

For water/steam, saturation pressure increases exponentially with temperature:

| Pressure (psia) | Temperature (°F) | Application |
|-----------------|------------------|-------------|
| 0.0886 | 32.0 | Triple point reference |
| 0.2563 | 60.0 | Evaporator conditions |
| 0.9503 | 100.0 | Low-pressure steam |
| 2.0 | 126.0 | Vacuum steam heating |
| 5.0 | 162.2 | Low-pressure heating steam |
| 10.0 | 193.2 | District heating steam |
| 14.696 | 212.0 | Atmospheric pressure (standard) |
| 25.0 | 240.1 | Building heating steam |
| 50.0 | 281.0 | Medium-pressure steam |
| 75.0 | 307.6 | Process steam |
| 100.0 | 327.8 | Industrial steam |
| 150.0 | 358.4 | High-pressure heating |
| 200.0 | 381.8 | Power generation |
| 400.0 | 444.6 | High-pressure industrial |
| 600.0 | 486.2 | Supercritical approach |
| 1000.0 | 544.6 | Power plant conditions |
| 3206.2 | 705.4 | Critical point |

### Thermodynamic Region Identification

Given temperature and pressure, determine the phase:

1. Compare actual pressure to saturation pressure at given temperature
2. If P < P_sat@T: superheated vapor
3. If P = P_sat@T: saturation (may be liquid, vapor, or mixture)
4. If P > P_sat@T: compressed liquid

Alternatively, compare temperature to saturation temperature at given pressure:

1. If T > T_sat@P: superheated vapor
2. If T = T_sat@P: saturation
3. If T < T_sat@P: compressed liquid

## Property Tables

### Saturated Water Table (Temperature Basis)

Representative values for HVAC applications:

| Temp (°F) | Press (psia) | v_f (ft³/lbm) | v_g (ft³/lbm) | h_f (Btu/lbm) | h_fg (Btu/lbm) | h_g (Btu/lbm) | s_f (Btu/lbm·°R) | s_g (Btu/lbm·°R) |
|-----------|--------------|---------------|---------------|---------------|----------------|---------------|------------------|------------------|
| 32 | 0.0886 | 0.01602 | 3302.4 | 0.00 | 1075.4 | 1075.4 | 0.0000 | 2.1870 |
| 50 | 0.1780 | 0.01602 | 1703.2 | 18.05 | 1065.2 | 1083.3 | 0.0361 | 2.1382 |
| 60 | 0.2563 | 0.01603 | 1206.7 | 28.06 | 1059.6 | 1087.7 | 0.0555 | 2.1164 |
| 70 | 0.3631 | 0.01605 | 867.7 | 38.05 | 1054.0 | 1092.1 | 0.0745 | 2.0955 |
| 80 | 0.5069 | 0.01607 | 633.3 | 48.04 | 1048.5 | 1096.5 | 0.0932 | 2.0754 |
| 100 | 0.9503 | 0.01613 | 350.4 | 68.00 | 1037.0 | 1105.0 | 0.1295 | 2.0374 |
| 120 | 1.6945 | 0.01620 | 203.0 | 87.97 | 1025.5 | 1113.5 | 0.1646 | 2.0023 |
| 140 | 2.8892 | 0.01629 | 122.9 | 107.95 | 1013.8 | 1121.7 | 0.1985 | 1.9696 |
| 160 | 4.741 | 0.01639 | 77.23 | 127.94 | 1001.8 | 1129.7 | 0.2313 | 1.9390 |
| 180 | 7.510 | 0.01651 | 50.20 | 147.97 | 989.4 | 1137.4 | 0.2630 | 1.9102 |
| 200 | 11.526 | 0.01663 | 33.63 | 168.04 | 976.6 | 1144.6 | 0.2938 | 1.8829 |
| 212 | 14.696 | 0.01672 | 26.80 | 180.10 | 970.3 | 1150.4 | 0.3121 | 1.8684 |
| 250 | 29.825 | 0.01700 | 13.83 | 218.48 | 945.5 | 1164.0 | 0.3682 | 1.8164 |
| 300 | 67.028 | 0.01745 | 6.472 | 269.51 | 910.1 | 1179.6 | 0.4372 | 1.7575 |
| 350 | 134.63 | 0.01799 | 3.346 | 321.73 | 863.6 | 1185.3 | 0.5029 | 1.6993 |
| 400 | 247.31 | 0.01864 | 1.8661 | 375.40 | 804.6 | 1180.0 | 0.5667 | 1.6409 |
| 450 | 422.6 | 0.01944 | 1.0993 | 431.0 | 730.0 | 1161.0 | 0.6296 | 1.5813 |
| 500 | 680.8 | 0.02043 | 0.6761 | 489.3 | 631.4 | 1120.7 | 0.6927 | 1.5194 |

Reference: ASHRAE Handbook—Fundamentals, Chapter 30, Thermophysical Properties of Refrigerants

### Saturated Water Table (Pressure Basis)

Common HVAC steam pressures:

| Press (psig) | Press (psia) | Temp (°F) | v_g (ft³/lbm) | h_f (Btu/lbm) | h_fg (Btu/lbm) | h_g (Btu/lbm) | s_f (Btu/lbm·°R) | s_g (Btu/lbm·°R) |
|--------------|--------------|-----------|---------------|---------------|----------------|---------------|------------------|------------------|
| 0 | 14.696 | 212.0 | 26.80 | 180.1 | 970.3 | 1150.4 | 0.3121 | 1.8684 |
| 2 | 16.696 | 220.0 | 24.06 | 188.2 | 965.7 | 1153.9 | 0.3247 | 1.8574 |
| 5 | 19.696 | 228.0 | 20.79 | 196.2 | 960.1 | 1156.3 | 0.3358 | 1.8453 |
| 10 | 24.696 | 240.1 | 16.32 | 208.4 | 952.2 | 1160.6 | 0.3535 | 1.8273 |
| 15 | 29.696 | 250.3 | 13.83 | 218.8 | 945.4 | 1164.2 | 0.3679 | 1.8132 |
| 25 | 39.696 | 267.2 | 10.50 | 236.0 | 933.8 | 1169.8 | 0.3921 | 1.7900 |
| 40 | 54.696 | 287.1 | 7.815 | 256.3 | 918.4 | 1174.7 | 0.4201 | 1.7625 |
| 50 | 64.696 | 298.0 | 6.583 | 267.5 | 911.9 | 1179.4 | 0.4344 | 1.7485 |
| 75 | 89.696 | 320.3 | 4.900 | 290.5 | 894.9 | 1185.4 | 0.4651 | 1.7193 |
| 100 | 114.696 | 338.0 | 3.788 | 309.9 | 881.0 | 1190.9 | 0.4903 | 1.6962 |
| 125 | 139.696 | 353.0 | 3.093 | 326.3 | 869.2 | 1195.5 | 0.5117 | 1.6775 |
| 150 | 164.696 | 366.0 | 2.594 | 340.5 | 859.2 | 1199.7 | 0.5307 | 1.6614 |

### Superheated Steam Table

Selected values for typical HVAC steam heating applications:

**At 25 psig (39.696 psia):**

| Temp (°F) | v (ft³/lbm) | h (Btu/lbm) | s (Btu/lbm·°R) | Superheat (°F) |
|-----------|-------------|-------------|----------------|----------------|
| 267.2 (sat) | 10.50 | 1169.8 | 1.7900 | 0 |
| 280 | 10.78 | 1177.0 | 1.8030 | 12.8 |
| 300 | 11.31 | 1187.9 | 1.8219 | 32.8 |
| 320 | 11.84 | 1198.7 | 1.8400 | 52.8 |
| 350 | 12.62 | 1214.4 | 1.8640 | 82.8 |
| 400 | 13.89 | 1239.2 | 1.9000 | 132.8 |

**At 100 psig (114.696 psia):**

| Temp (°F) | v (ft³/lbm) | h (Btu/lbm) | s (Btu/lbm·°R) | Superheat (°F) |
|-----------|-------------|-------------|----------------|----------------|
| 338.0 (sat) | 3.788 | 1190.9 | 1.6962 | 0 |
| 350 | 3.890 | 1197.8 | 1.7061 | 12 |
| 400 | 4.218 | 1227.5 | 1.7483 | 62 |
| 450 | 4.531 | 1256.7 | 1.7869 | 112 |
| 500 | 4.838 | 1285.8 | 1.8229 | 162 |
| 600 | 5.438 | 1343.9 | 1.8895 | 262 |

### Compressed Liquid Water

For pressures significantly above saturation pressure at a given temperature, enthalpy and entropy corrections may be necessary:

**h(T,P) ≈ h_f(T) + v_f(T)·(P - P_sat)**

For most HVAC applications (P < 500 psia), the pressure correction is negligible:

- At 200°F and 100 psia: h ≈ 168.04 Btu/lbm (error < 0.5%)
- At 200°F and 500 psia: h ≈ 168.7 Btu/lbm (correction ~0.6 Btu/lbm)

Compressed liquid approximation is acceptable for:
- Boiler feedwater systems
- Hot water heating systems
- Chilled water systems
- Condensate return calculations

## ASHRAE and Code References

### ASHRAE Standards

**ASHRAE Handbook—Fundamentals, Chapter 30: Thermophysical Properties of Refrigerants**
- Comprehensive water/steam property tables
- Saturation and superheat data
- Thermodynamic diagrams
- Property correlations and equations

**ASHRAE Standard 41.6: Standard Method for Measurement of Moist Air Properties**
- Psychrometric calculations involving water vapor
- Enthalpy of moist air mixtures
- Humidity ratio determination

**ASHRAE Guideline 2: Engineering Analysis of Experimental Data**
- Uncertainty analysis for property measurements
- Data correlation methodology

### ASME Standards

**ASME Steam Tables (ASME International Steam Tables—IAPWS-IF97)**
- Industrial standard for water/steam properties
- Temperature range: 0-800°C (32-1472°F)
- Pressure range: 0-100 MPa (0-14,500 psia)
- Accuracy: ±0.03% for most properties

**ASME Power Test Code PTC 19.3: Temperature Measurement**
- Instrumentation requirements for steam systems
- Measurement uncertainty quantification

**ASME Boiler and Pressure Vessel Code (BPVC)**
- Section I: Power Boilers (steam quality requirements)
- Section IV: Heating Boilers (low-pressure systems)

### Industry References

**Spirax Sarco Steam Engineering Tutorials**
- Practical steam system design
- Steam quality and dryness considerations
- Condensate management

**Department of Energy (DOE) Steam System Best Practices**
- Energy efficiency optimization
- Steam trap management
- Condensate recovery economics

## Design Considerations for Steam Systems

### Steam Quality Requirements

Minimum steam quality (dryness fraction) varies by application:

| Application | Minimum Quality | Rationale |
|-------------|-----------------|-----------|
| Power generation turbines | 0.88-0.90 | Blade erosion prevention |
| Process steam users | 0.95-0.97 | Product quality, heat transfer |
| Steam heating systems | 0.95-0.98 | Uniform heating, trap operation |
| Boiler outlet | 0.98-0.999 | ASME requirements, carryover prevention |
| Sterilization/autoclaves | 0.97-1.00 | Process effectiveness |
| Humidification | 0.90-0.95 | Droplet prevention |

Low steam quality consequences:
- Water hammer (safety hazard, equipment damage)
- Erosion of valves, traps, and piping
- Reduced heat transfer efficiency
- Thermal stress from temperature variation
- Process quality degradation

### Enthalpy Drop Calculations

For steam heating applications, the enthalpy change determines heat transfer:

**Q = ṁ·(h₁ - h₂)**

Where:
- Q = heat transfer rate (Btu/hr or kW)
- ṁ = mass flow rate (lbm/hr or kg/s)
- h₁ = inlet steam enthalpy (Btu/lbm or kJ/kg)
- h₂ = outlet condensate enthalpy (Btu/lbm or kJ/kg)

#### Example: Steam Coil Calculation

**Given:**
- Steam supply: 25 psig saturated steam
- Condensate return: saturated liquid at 25 psig
- Heat load: 1,000,000 Btu/hr

**Solution:**

From tables at 25 psig (39.696 psia):
- t_sat = 267.2°F
- h_g = 1169.8 Btu/lbm
- h_f = 236.0 Btu/lbm

Enthalpy drop:
h_fg = 1169.8 - 236.0 = 933.8 Btu/lbm

Steam flow required:
ṁ = Q / h_fg = 1,000,000 / 933.8 = 1071 lbm/hr

If condensate subcools to 200°F:
h₂ = 168.04 Btu/lbm
Δh = 1169.8 - 168.04 = 1001.8 Btu/lbm
ṁ = 1,000,000 / 1001.8 = 998 lbm/hr (6.8% reduction)

### Flash Steam Recovery

When high-pressure condensate is reduced to lower pressure, a portion flashes to steam. The flash steam percentage is determined by enthalpy balance:

**x_flash = (h_f1 - h_f2) / h_fg2**

Where:
- x_flash = mass fraction flashing to steam
- h_f1 = liquid enthalpy at high pressure
- h_f2 = liquid enthalpy at low pressure
- h_fg2 = latent heat at low pressure

#### Example: Flash Steam Calculation

**Given:**
- Condensate at 100 psig (309.9 Btu/lbm)
- Flashes to 15 psig
- Condensate flow: 5000 lbm/hr

**Solution:**

At 100 psig: h_f1 = 309.9 Btu/lbm
At 15 psig: h_f2 = 218.8 Btu/lbm, h_fg2 = 945.4 Btu/lbm

Flash fraction:
x = (309.9 - 218.8) / 945.4 = 0.0964 or 9.64%

Flash steam flow:
ṁ_flash = 5000 × 0.0964 = 482 lbm/hr

Recoverable energy (if flashed steam utilized):
Q = 482 × 945.4 = 455,682 Btu/hr

### Isentropic Efficiency

For expansion devices (turbines, expanders), isentropic efficiency compares actual performance to ideal reversible (constant entropy) expansion:

**η_isentropic = (h₁ - h₂_actual) / (h₁ - h₂_isentropic)**

For compression devices (pumps, compressors):

**η_isentropic = (h₂_isentropic - h₁) / (h₂_actual - h₁)**

Typical isentropic efficiencies:
- Large steam turbines: 85-92%
- Small steam turbines: 65-80%
- Centrifugal pumps: 70-85%
- Boiler feed pumps: 75-88%

### Condensate Return System Design

Condensate enthalpy represents significant recoverable energy:

**Energy Recovery = ṁ_condensate × (h_condensate - h_makeup)**

At 212°F (atmospheric flash tank):
- Condensate enthalpy: 180.1 Btu/lbm
- Makeup water at 60°F: 28.06 Btu/lbm
- Recoverable energy: 152.0 Btu/lbm

For a system condensing 10,000 lbm/hr steam:
- Energy recovery: 10,000 × 152.0 = 1,520,000 Btu/hr
- Annual savings at $8/MMBtu: 1.52 × 8760 × 8 = $106,598/year

Return temperature considerations:
- Maximum recommended: 200-212°F (prevents cavitation)
- Minimum recommended: 130°F (maintains system cleanliness)
- Optimal for deaeration: 180-212°F

### Entropy Analysis for System Optimization

Entropy generation identifies irreversibilities and optimization opportunities:

**ΔS_gen = Σ(ṁ·s)_out - Σ(ṁ·s)_in + Q/T_boundary**

For adiabatic systems (Q = 0):

**ΔS_gen = Σ(ṁ·s)_out - Σ(ṁ·s)_in ≥ 0**

Major sources of entropy generation in steam systems:
1. Throttling losses (pressure reducing valves): 15-30%
2. Heat transfer across finite temperature differences: 25-40%
3. Mixing of streams at different conditions: 5-15%
4. Friction in piping and equipment: 10-20%
5. Unrecovered condensate energy: 15-25%

#### Example: Throttling Loss Analysis

**Given:**
- Steam at 100 psig, saturated (338°F, 1190.9 Btu/lbm)
- Throttled to 15 psig (250.3°F saturation)
- Flow rate: 2000 lbm/hr

**Solution:**

At 100 psig (sat): h₁ = 1190.9 Btu/lbm, s₁ = 1.6962 Btu/lbm·°R

Throttling is isenthalpic: h₂ = h₁ = 1190.9 Btu/lbm

At 15 psig:
- h_f = 218.8 Btu/lbm, h_fg = 945.4 Btu/lbm, h_g = 1164.2 Btu/lbm
- s_f = 0.3679 Btu/lbm·°R, s_fg = 1.4453 Btu/lbm·°R

Since h₂ > h_g at 15 psig, steam is superheated after throttling.

Using superheat table at 15 psig, 290°F (approximate):
s₂ ≈ 1.7850 Btu/lbm·°R

Entropy generation:
ΔS_gen = s₂ - s₁ = 1.7850 - 1.6962 = 0.0888 Btu/lbm·°R

Total rate: 2000 × 0.0888 = 177.6 Btu/hr·°R

Exergy destruction at T₀ = 70°F (529.67°R):
Ẋ_destroyed = T₀ × ΔṠ_gen = 529.67 × 177.6 = 94,069 Btu/hr

Alternative: Replace PRV with back-pressure turbine or mechanical work extraction device.

## Practical Applications

### Psychrometric Calculations

Water vapor enthalpy in air-water vapor mixtures:

**h_a = h_da + W·h_g**

Where:
- h_a = enthalpy of moist air (Btu/lbm dry air)
- h_da = enthalpy of dry air ≈ 0.240·t (Btu/lbm dry air)
- W = humidity ratio (lbm water vapor/lbm dry air)
- h_g = enthalpy of water vapor at dry-bulb temperature (Btu/lbm)

For standard psychrometric calculations, h_g is approximated:

**h_g ≈ 1061 + 0.444·t** (Btu/lbm) at temperatures from 32-100°F

This represents saturated vapor enthalpy plus superheat correction.

### Boiler Efficiency Calculations

Direct method (input-output):

**η_boiler = ṁ_steam·(h_steam - h_feedwater) / (ṁ_fuel × HHV_fuel)**

Heat balance method includes all losses:
- Stack (flue gas) losses: 10-20% (largest single loss)
- Radiation and convection losses: 1-3%
- Blowdown losses: 1-5%
- Unburned fuel losses: 0.5-2%

Target boiler efficiency:
- Fire-tube boilers: 75-82%
- Water-tube boilers: 80-85%
- Condensing boilers: 90-96%

### Deaerator Performance

Deaerators remove dissolved oxygen and CO₂ from feedwater by heating to saturation temperature, releasing non-condensable gases.

Operating pressure selection:

| Deaerator Pressure | Temperature | Application |
|--------------------|-------------|-------------|
| 5 psig | 228°F | Low-pressure heating boilers |
| 10 psig | 240°F | Small industrial boilers |
| 15 psig | 250°F | Medium industrial boilers |
| 30 psig | 268°F | Large industrial/power boilers |

Enthalpy balance for steam consumption:

**ṁ_steam·h_steam + ṁ_makeup·h_makeup + ṁ_condensate·h_condensate = (ṁ_steam + ṁ_makeup + ṁ_condensate)·h_deaerator**

Typical dissolved oxygen targets:
- < 0.005 ppm for boilers > 900 psig
- < 0.04 ppm for boilers 300-900 psig
- < 0.3 ppm for boilers < 300 psig

### Steam Turbine Work Output

For steam turbines, work output is the enthalpy drop:

**W_turbine = ṁ·(h_inlet - h_exhaust)_actual**

With isentropic efficiency:

**h_exhaust,actual = h_inlet - η_s·(h_inlet - h_exhaust,isentropic)**

Where h_exhaust,isentropic is found at exhaust pressure and s = s_inlet.

Back-pressure vs. condensing turbines:
- Back-pressure: exhaust steam used for process (higher pressure, lower work)
- Condensing: maximum work extraction (vacuum exhaust, 1-2 psia)

## Conclusion

Enthalpy and entropy are fundamental properties for HVAC system analysis, design, and optimization. Accurate property evaluation using steam tables, understanding phase relationships, and applying thermodynamic principles enable:

- Precise energy balance calculations
- Efficient steam system design
- Optimization of component performance
- Identification of energy recovery opportunities
- Economic analysis of system improvements

Mastery of water/steam thermodynamic properties is essential for HVAC professionals involved in steam heating systems, boiler plants, power generation, and industrial process applications.
