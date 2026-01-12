---
title: "Freezing Points vs Concentration"
description: "Freezing point depression relationships for glycol and brine secondary coolants, including eutectic points, concentration-property curves, and freeze protection design criteria for HVAC applications"
weight: 2
---

## Overview

The freezing point of secondary coolant solutions varies nonlinearly with solute concentration, exhibiting characteristic depression curves that reach minimum values at eutectic compositions. Understanding these relationships is critical for proper system design, freeze protection, and avoiding equipment damage in chilled water, process cooling, and industrial refrigeration applications.

The addition of antifreeze agents (glycols, salts) disrupts the crystalline structure of water, lowering the temperature at which ice crystals form. This colligative property depends on the mole fraction of dissolved particles rather than their chemical identity, though practical applications must account for solution non-ideality at higher concentrations.

## Freezing Point Depression Fundamentals

### Colligative Property Theory

Freezing point depression follows from Raoult's law and thermodynamic equilibrium between solid and liquid phases. For ideal dilute solutions:

ΔTf = Kf × m × i

Where:
- ΔTf = freezing point depression (°C or °F)
- Kf = cryoscopic constant (1.86 °C·kg/mol for water)
- m = molality of solution (mol solute/kg solvent)
- i = van't Hoff factor (number of particles per formula unit)

For glycol solutions, i ≈ 1 (molecular solutes). For ionic brines, i approaches the number of ions (e.g., i ≈ 2 for NaCl, though less at high concentrations due to ion pairing).

### Non-Ideal Behavior

Real secondary coolant solutions deviate significantly from ideal behavior at concentrations used in HVAC systems (typically 20-60% by mass). Activity coefficients account for:

- Solute-solvent interactions
- Solution viscosity effects
- Hydrogen bonding disruption
- Molecular crowding at high concentrations

Empirical data and correlation equations are required for accurate freezing point prediction at practical concentrations.

## Freezing Point Depression Curves

### Ethylene Glycol Solutions

Ethylene glycol (EG) exhibits the following freezing point characteristics:

| Concentration (% by mass) | Freezing Point (°F) | Freezing Point (°C) | Protection Level |
|---------------------------|---------------------|---------------------|------------------|
| 0 | 32.0 | 0.0 | None |
| 10 | 26.0 | -3.3 | Light |
| 20 | 18.0 | -7.8 | Moderate |
| 25 | 13.5 | -10.3 | Standard |
| 30 | 7.0 | -13.9 | Enhanced |
| 35 | -2.0 | -18.9 | Cold climate |
| 40 | -12.0 | -24.4 | Severe cold |
| 45 | -22.0 | -30.0 | Extreme |
| 50 | -34.0 | -36.7 | Arctic |
| 55 | -44.0 | -42.2 | Near eutectic |
| 60 | -49.0 | -45.0 | Eutectic |
| 65 | -40.0 | -40.0 | Beyond eutectic |
| 70 | -27.0 | -32.8 | Beyond eutectic |

The curve reaches a minimum (eutectic point) at approximately 60% by mass, corresponding to -49°F (-45°C). Beyond this concentration, freezing point increases as the solution behavior transitions toward that of concentrated glycol rather than aqueous solution.

### Propylene Glycol Solutions

Propylene glycol (PG), preferred for food-grade and potable water applications:

| Concentration (% by mass) | Freezing Point (°F) | Freezing Point (°C) | Application |
|---------------------------|---------------------|---------------------|-------------|
| 0 | 32.0 | 0.0 | Pure water |
| 10 | 26.5 | -3.1 | Minimal |
| 20 | 19.0 | -7.2 | Light duty |
| 25 | 14.5 | -9.7 | Standard chiller |
| 30 | 9.0 | -12.8 | Snow melt systems |
| 35 | 1.0 | -17.2 | Cold storage |
| 40 | -8.0 | -22.2 | Freezer coils |
| 45 | -18.0 | -27.8 | Low-temp process |
| 50 | -29.0 | -33.9 | Ultra-low temp |
| 55 | -40.0 | -40.0 | Near eutectic |
| 60 | -51.0 | -46.1 | Eutectic |
| 65 | -45.0 | -42.8 | Beyond eutectic |
| 70 | -34.0 | -36.7 | Beyond eutectic |

Propylene glycol eutectic occurs at approximately 60% by mass at -51°F (-46°C), slightly lower than ethylene glycol due to molecular weight and solution chemistry differences.

### Calcium Chloride Brine

Calcium chloride (CaCl₂) brines provide lower freezing points than glycols at equivalent mass concentrations:

| Concentration (% by mass) | Freezing Point (°F) | Freezing Point (°C) | Density (lb/gal at 60°F) |
|---------------------------|---------------------|---------------------|--------------------------|
| 0 | 32.0 | 0.0 | 8.33 |
| 5 | 26.6 | -3.0 | 8.74 |
| 10 | 20.3 | -6.5 | 9.16 |
| 15 | 12.7 | -10.7 | 9.58 |
| 20 | 3.8 | -15.7 | 10.00 |
| 23 | -4.0 | -20.0 | 10.32 |
| 25 | -9.8 | -23.2 | 10.42 |
| 29.9 | -60.0 | -51.1 | 10.99 |
| 35 | -40.0 | -40.0 | 11.44 |
| 40 | -15.0 | -26.1 | 11.87 |

The eutectic point for CaCl₂ occurs at 29.9% by mass, yielding -60°F (-51°C). This provides excellent freeze protection but introduces corrosion concerns requiring inhibitors.

### Sodium Chloride Brine

Sodium chloride (NaCl) brines, commonly used in ice rinks and industrial applications:

| Concentration (% by mass) | Freezing Point (°F) | Freezing Point (°C) | Specific Gravity |
|---------------------------|---------------------|---------------------|------------------|
| 0 | 32.0 | 0.0 | 1.000 |
| 5 | 27.3 | -2.6 | 1.034 |
| 10 | 20.5 | -6.4 | 1.071 |
| 15 | 11.7 | -11.3 | 1.109 |
| 20 | 1.1 | -17.2 | 1.148 |
| 23.3 | -6.0 | -21.1 | 1.178 |
| 25 | -11.2 | -24.0 | 1.189 |
| 26.4 | -6.0 | -21.1 | 1.201 |

Sodium chloride eutectic occurs at 23.3% by mass at -6°F (-21°C). The relatively high eutectic temperature limits NaCl to moderate low-temperature applications, though it remains cost-effective for ice rink and snow-melt systems.

## Eutectic Points

### Definition and Significance

The eutectic point represents the composition at which a solution exhibits its minimum freezing point. At this concentration, the solution and solid phases (ice plus solute crystals) exist in equilibrium at a single temperature. Key characteristics:

- **Minimum freeze point**: Maximum freeze protection for a given solute
- **Congruent freezing**: Solution solidifies uniformly without phase separation
- **Sharp transition**: Clear liquid-to-solid transformation at eutectic temperature
- **Two solid phases**: Ice and crystalline solute form simultaneously

### Eutectic Composition Data

**Ethylene Glycol:**
- Eutectic concentration: 60.0% by mass
- Eutectic temperature: -49°F (-45°C)
- Below this temperature, ice and ethylene glycol hydrate crystals form

**Propylene Glycol:**
- Eutectic concentration: 60.0% by mass
- Eutectic temperature: -51°F (-46°C)
- Slightly lower than EG due to molecular structure differences

**Calcium Chloride:**
- Eutectic concentration: 29.9% by mass
- Eutectic temperature: -60°F (-51°C)
- Forms CaCl₂·6H₂O hexahydrate crystals below eutectic

**Sodium Chloride:**
- Eutectic concentration: 23.3% by mass
- Eutectic temperature: -6°F (-21°C)
- Forms NaCl·2H₂O dihydrate and ice below eutectic

**Potassium Formate:**
- Eutectic concentration: 53% by mass
- Eutectic temperature: -62°F (-52°C)
- Environmentally preferred alternative to chloride brines

### Engineering Implications

Operating at eutectic concentration is generally avoided in HVAC systems because:

1. **No safety margin**: Any dilution from water ingress raises freezing point
2. **Viscosity penalty**: Eutectic concentrations exhibit maximum viscosity
3. **Pump power**: Higher pressure drops increase operating costs
4. **Heat transfer**: Reduced thermal conductivity and film coefficients
5. **System monitoring**: Difficult to detect concentration drift

Design practice maintains concentrations 10-15 percentage points below eutectic for most applications, providing freeze protection margin with better transport properties.

## Slush Formation and Ice Crystal Formation

### Pre-Eutectic Behavior

When secondary coolant solutions are cooled below their freezing point but above the eutectic temperature, ice crystals nucleate and grow while the remaining liquid becomes progressively concentrated in antifreeze. This two-phase region exhibits:

**Ice Crystal Characteristics:**
- Pure water ice forms initially (no solute incorporation)
- Dendritic growth patterns in flowing systems
- Crystal size: 10-1000 μm depending on cooling rate
- Heterogeneous nucleation on system surfaces

**Solution Behavior:**
- Liquid phase concentration increases as ice forms
- Freezing point of remaining liquid decreases
- Viscosity increases dramatically (3-10× at 20% ice fraction)
- Non-Newtonian rheology in slush regime

### Slush Formation Regimes

The ice fraction as a function of temperature below initial freezing point follows lever rule calculations:

**Mass fraction ice:**

f_ice = (C_initial - C_liquid) / (100 - C_liquid)

Where:
- f_ice = mass fraction of ice in slush
- C_initial = initial coolant concentration (%)
- C_liquid = concentration corresponding to current temperature on freezing curve

**Example Calculation:**

A 30% ethylene glycol solution (freezing point 7°F) is cooled to -10°F. From the freezing curve, -10°F corresponds to approximately 39% EG concentration:

f_ice = (30 - 39) / (100 - 39) = 0.148 or 14.8% ice

This ice fraction significantly impacts flow properties and heat transfer.

### Slush Flow Properties

Ice-laden secondary coolants exhibit complex rheological behavior:

**Viscosity increase:**
- μ_slush ≈ μ_liquid × (1 + 2.5φ + 10.05φ² + ...)

Where φ = volume fraction of ice (Einstein-Roscoe equation for suspensions)

**Pressure drop multiplication:**
- 10% ice by volume: 40-60% pressure drop increase
- 20% ice by volume: 100-200% pressure drop increase
- Flow becomes unstable above 25% ice content

**Heat transfer degradation:**
- Ice crystals block flow channels in heat exchangers
- Film coefficient reduction: 20-40% at 10% ice fraction
- Potential for complete blockage in narrow passages

**Pump damage mechanisms:**
- Cavitation from two-phase flow instabilities
- Mechanical seal damage from abrasive ice particles
- Impeller erosion and efficiency loss
- Pressure fluctuations and vibration

### Ice Crystal Morphology

Crystal structure depends on cooling rate and flow conditions:

**Quiescent freezing:**
- Large dendritic crystals (1-10 mm)
- Slow growth rates (0.1-1 mm/min)
- Preferential growth directions based on water crystal structure
- Interlocking network formation

**Turbulent flow freezing:**
- Smaller fragmented crystals (100-1000 μm)
- Rapid nucleation and breakup
- Spherical to irregular particle shapes
- Free-flowing slush at low ice fractions

**Surface freezing:**
- Ice layer formation on heat exchanger walls
- Insulating effect reduces heat transfer
- Potential for complete blockage in severe cases
- Requires periodic defrost or elevated return temperature

## Freeze Protection Margin

### Design Safety Factor

ASHRAE Standard 90.1 and industry practice require freeze protection margins beyond the expected minimum system temperature:

**Standard safety factors:**

Freeze protection temperature = Minimum ambient - Safety margin

Typical safety margins:
- **10°F (5.6°C)**: Standard commercial HVAC in moderate climates
- **15°F (8.3°C)**: Critical systems or severe climate zones
- **20°F (11.1°C)**: Process systems with high economic consequences
- **25°F (13.9°C)**: Systems with potential for airflow loss or control failure

### Concentration Safety Factor

Converting temperature margin to concentration requires careful analysis of the freezing curve slope:

**Method 1: Direct temperature margin**

Select concentration providing freeze point = T_min - ΔT_safety

Example: Chicago rooftop unit
- Design winter temperature: -10°F (99.6% ASHRAE)
- Safety margin: 15°F
- Required freeze protection: -25°F
- Ethylene glycol concentration: approximately 46%

**Method 2: Concentration addition method**

Some designers add percentage points to the concentration corresponding to minimum temperature:

C_design = C_minimum + ΔC_safety

Where ΔC_safety = 3-5 percentage points

This method is less precise because freezing curves are nonlinear, but provides additional margin for concentration drift.

### Factors Affecting Required Margin

**System vulnerability:**
- Unheated equipment rooms: Higher margin required
- Roof-mounted equipment: Exposed to wind chill effects
- Intermittent operation: Dead-heading allows temperature equalization
- Large thermal mass: Reduces freeze risk but slows warm-up
- Redundant freeze protection: Heat tracing allows lower margin

**Economic considerations:**
- Initial glycol cost increases with concentration
- Pump energy penalties from higher viscosity
- Heat transfer reduction at high concentrations
- Replacement cost of freeze-damaged equipment
- Downtime and lost productivity

**Maintenance and monitoring:**
- Regular concentration testing: Allows lower initial margin
- Automatic makeup systems: Compensate for dilution
- Temperature monitoring: Early warning of freeze conditions
- Preventive maintenance: Ensures control system reliability

### Calculation Example

**Problem:** Determine propylene glycol concentration for a closed-loop snow melt system in Denver, CO.

**Given:**
- Design outdoor temperature: -10°F (ASHRAE 99.6%)
- Safety margin: 20°F (exposed surface, high consequence)
- Required freeze protection: -30°F

**Solution:**

From propylene glycol freezing curve:
- -30°F corresponds to approximately 49% PG by mass
- Add concentration safety factor: 49% + 3% = 52%
- Design concentration: 52% propylene glycol

**Verification:**
- 52% PG freezing point: approximately -32°F
- Margin achieved: -32°F - (-10°F) = 22°F
- Meets 20°F minimum requirement

**System impact assessment:**
- Viscosity at 0°F, 52% PG: approximately 25 cP (vs 2 cP for water)
- Specific heat: 0.89 Btu/(lb·°F) (vs 1.0 for water)
- Flow rate increase: 12% to maintain heat transfer capacity
- Pump power increase: approximately 40% due to viscosity

## Lowest Ambient Temperature Consideration

### Design Temperature Selection

ASHRAE Fundamentals Chapter 14 provides climatic design data based on statistical analysis of weather records. Selection of appropriate design conditions balances freeze protection against economic optimization:

**ASHRAE design temperature bases:**

| Percentile | Temperature Exceeded | Typical Application |
|------------|---------------------|---------------------|
| 99.6% | 35 hours/year (1.5 days) | Critical systems, hospitals, data centers |
| 99.0% | 88 hours/year (3.7 days) | Standard commercial buildings |
| 97.5% | 219 hours/year (9.1 days) | Residential, non-critical loads |

**Example design temperatures (99.6%):**

| Location | Winter Design Temp | Recommended Freeze Point |
|----------|-------------------|-------------------------|
| Miami, FL | 47°F | 32°F (plain water acceptable with controls) |
| Atlanta, GA | 22°F | 5°F (25% EG, 15°F margin) |
| Chicago, IL | -7°F | -25°F (46% EG, 18°F margin) |
| Minneapolis, MN | -16°F | -35°F (51% EG, 19°F margin) |
| Fairbanks, AK | -47°F | -65°F (60% EG at eutectic, 18°F margin) |

### Wind Chill and Equipment Exposure

Wind velocity amplifies convective heat loss from piping and equipment, potentially lowering surface temperatures below ambient air:

**Wind chill equivalent temperature:**

T_wc = 35.74 + 0.6215T - 35.75V^0.16 + 0.4275TV^0.16

Where:
- T_wc = wind chill temperature (°F)
- T = air temperature (°F)
- V = wind velocity (mph)

For insulated piping, wind effects are minimal. For exposed equipment (outdoor coils, piping manifolds, drain pans):

- Moderate exposure (10 mph winds): Add 3-5°F to safety margin
- High exposure (20+ mph winds): Add 8-12°F to safety margin
- Extreme exposure (rooftops, coastal): Add 15°F or provide wind barriers

### Operational Scenarios

**Normal operation:**
- Circulating fluid maintains temperature above freezing
- Heat input from pumps (typically 1-3°F temperature rise)
- System heat gains from ambient (if indoor routing)

**Power failure scenarios:**
- Loss of circulation allows temperature equalization
- Thermal mass provides time buffer (hours to days)
- Exposed piping reaches ambient first
- Emergency heat tracing or glycol concentration critical

**Shutdown conditions:**
- Planned shutdowns require complete drainage or adequate glycol
- Seasonal facilities must be winterized
- Startup in cold weather requires pre-warming procedures

**Dead-heading and stagnation:**
- Isolated piping legs lose heat to surroundings
- No pump heat input or mixing
- Can occur during valve failure or control malfunction
- Requires concentration as if no circulation

## Design Considerations and Best Practices

### Concentration Selection Strategy

**Step 1: Determine minimum system temperature**
- Select ASHRAE design condition (99.6% recommended)
- Assess equipment exposure and wind effects
- Consider operational scenarios (shutdown, power loss)

**Step 2: Apply safety margin**
- Minimum 10°F for standard applications
- 15-20°F for critical systems or high exposure
- 25°F if control reliability is questionable

**Step 3: Select glycol type**
- Ethylene glycol: Closed systems, best cost/performance
- Propylene glycol: Food processing, potable water risk, LEED projects
- Inhibited glycols: Mandatory for corrosion protection

**Step 4: Verify system impacts**
- Calculate viscosity at minimum operating temperature
- Determine flow rate increase for heat transfer equivalence
- Assess pump pressure rise and motor sizing
- Confirm heat exchanger performance at reduced properties

**Step 5: Establish monitoring protocol**
- Initial concentration verification after filling
- Annual concentration testing (minimum)
- Quarterly testing for open systems or if dilution suspected
- pH monitoring to verify inhibitor effectiveness

### Concentration Monitoring and Testing

**Refractometer method:**
- Most common field test
- Measures refractive index (Brix scale)
- Convert to glycol concentration using correlation charts
- Accuracy: ±2 percentage points
- Cannot distinguish glycol types or detect contamination

**Hydrometer method:**
- Measures specific gravity
- Requires temperature correction
- Less accurate than refractometer (±3-5%)
- Suitable for brines

**Titration method:**
- Laboratory analysis
- Most accurate (±0.5%)
- Can identify glycol type and contamination
- Measures reserve alkalinity (inhibitor depletion)

**Freezing point test:**
- Direct measurement in freeze-point apparatus
- Gold standard for accuracy
- Requires specialized equipment
- Used for calibration and dispute resolution

### Dilution and Concentration Drift

**Common causes of dilution:**
- Makeup water addition after leaks
- Condensation in open systems
- Heat exchanger tube leaks
- Improper initial mixing

**Dilution impact:**

ΔC/C_initial = V_water / (V_initial + V_water)

Where V_water = volume of water added

Example: 1000-gallon system at 40% glycol with 100-gallon water addition:
- New concentration: 40% × 1000/(1000+100) = 36.4%
- Freezing point change: -12°F to -2°F (10°F reduction in protection)

**Prevention measures:**
- Closed-loop systems with minimal makeup
- Automatic concentration monitoring in critical systems
- Makeup solution matched to system concentration
- Regular testing and adjustment

### Glycol Degradation and Service Life

Glycol degradation reduces freeze protection and increases corrosion risk:

**Degradation mechanisms:**
- Thermal oxidation at elevated temperatures (>250°F)
- Biological growth in open systems
- Contamination from system corrosion products
- Inhibitor depletion over time

**Monitoring indicators:**
- Color change (clear to yellow/brown indicates oxidation)
- pH reduction (fresh glycol pH 9.5-11, degraded <7)
- Presence of organic acids (formic, oxalic, glycolic)
- Particulate formation

**Service life expectations:**
- Closed systems with inhibited glycol: 5-10 years
- Open systems: 1-3 years
- High-temperature applications (>200°F): 2-5 years
- Systems with biological growth: Annual replacement

**Replacement criteria:**
- pH <7.0 (acidic, inhibitor depleted)
- Reserve alkalinity <50% of original
- Visible contamination or color change
- Concentration cannot be maintained
- Corrosion evidence in system

### System Design Impacts

**Piping sizing:**

For equivalent pressure drop, glycol solutions require larger pipe diameter:

d_glycol / d_water = (μ_glycol / μ_water)^0.2

Example: 40% EG at 40°F (viscosity 4.8 cP vs 1.5 cP for water)
- Diameter ratio: (4.8/1.5)^0.2 = 1.26
- 1-inch water line → 1.25-inch glycol line for same ΔP

**Pump selection:**
- Pressure rise increases with viscosity
- NPSH requirements higher for glycols (lower vapor pressure)
- Mechanical seal materials compatible with glycol
- Motor sizing for worst-case (high viscosity at cold startup)

**Heat exchanger performance:**

Heat transfer coefficient reduction with glycol:

U_glycol / U_water ≈ 0.85 to 0.95 (depending on concentration and temperature)

Requires increased surface area or flow rate to maintain capacity.

**Expansion tank sizing:**

Glycol solutions have different thermal expansion coefficients:

V_expansion = V_system × β × ΔT

Where β = volumetric expansion coefficient
- Water: 0.0002/°F
- 30% EG: 0.00024/°F
- 50% EG: 0.00028/°F

Expansion tanks must be sized 15-20% larger for glycol systems.

### Code and Standard References

**ASHRAE Standards:**
- ASHRAE Standard 15: Safety requirements for refrigerant systems
- ASHRAE Standard 90.1: Energy efficiency requirements
- ASHRAE Handbook—Fundamentals: Chapter 31, Secondary Coolants

**Industry Standards:**
- ASTM D1177: Standard specification for engine coolant (glycol)
- ASTM D3306: Automotive engine coolant specifications
- NSF/ANSI 60: Drinking water treatment chemicals (propylene glycol)

**Plumbing Codes:**
- IPC Section 607: Freeze protection requirements
- UPC Section 607: Similar freeze protection provisions
- Local amendments may have specific glycol requirements

**Best Practice Guidelines:**
- Use only inhibited glycols designed for HVAC systems
- Never use automotive antifreeze (contains silicates harmful to pumps)
- Propylene glycol required for potable water protection
- Maintain concentration records for system life
- Include glycol type and concentration on system labeling

### Environmental and Safety Considerations

**Ethylene glycol:**
- Toxic if ingested (LD50: 4.7 g/kg in rats)
- Sweet taste makes accidental ingestion hazardous
- Metabolizes to toxic glycolic and oxalic acids
- Disposal regulated as hazardous waste in many jurisdictions
- Prohibited in food processing and potable water applications

**Propylene glycol:**
- Generally Recognized As Safe (GRAS) for food contact
- Low toxicity (LD50: 20-30 g/kg in rats)
- Metabolizes to lactic acid (normal metabolite)
- Preferred for LEED projects and green buildings
- Higher cost than ethylene glycol (typically 30-50% premium)

**Brine solutions:**
- Corrosive to system components without inhibitors
- Calcium chloride: Requires additional corrosion control
- Sodium chloride: Less corrosive but limited temperature range
- Environmental concerns for outdoor applications (salt loading)
- Disposal requires neutralization and environmental compliance

**Spill response:**
- Glycol spills create slipping hazard
- Absorb with inert material (sand, clay absorbent)
- Prevent entry to waterways (harmful to aquatic life)
- Dispose according to local hazardous waste regulations
- Glycol-contaminated groundwater requires remediation

## Summary

Freezing point depression in secondary coolants follows predictable but nonlinear relationships with solute concentration. Key engineering considerations:

1. **Eutectic points** represent minimum achievable freezing temperatures but are not optimal operating concentrations due to viscosity penalties and lack of safety margin.

2. **Design concentration** should provide freeze protection to 10-20°F below the expected minimum system temperature, accounting for equipment exposure, operational scenarios, and control reliability.

3. **Glycol selection** balances cost (ethylene glycol), safety (propylene glycol), and application requirements (food-grade, potable water protection).

4. **System performance impacts** from reduced thermal conductivity, increased viscosity, and altered transport properties must be evaluated during design.

5. **Monitoring and maintenance** of glycol concentration is essential to maintain freeze protection throughout system life.

Proper application of freezing point depression principles ensures reliable freeze protection while optimizing system performance and operating costs.
