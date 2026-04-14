---
title: "Propylene Glycol"
aliases: ["Propylene Glycol"]
description: "Comprehensive technical guide to propylene glycol secondary coolant properties, thermophysical data, food-grade applications, and HVAC system design considerations including freeze protection and heat transfer performance"
weight: 2
---

Propylene glycol (1,2-propanediol, C₃H₈O₂) serves as the preferred secondary coolant for HVAC applications requiring low toxicity, particularly in food processing facilities, pharmaceutical manufacturing, and potable water applications. This diol exhibits lower heat transfer efficiency compared to ethylene glycol but provides essential safety advantages in systems where human exposure or product contamination presents concern.

## Chemical and Physical Properties

### Molecular Structure

Propylene glycol consists of a three-carbon chain with two hydroxyl groups at the 1 and 2 positions. The molecular weight of 76.09 g/mol and the presence of hydroxyl groups enable hydrogen bonding with water, creating complete miscibility across all concentration ranges. This molecular architecture produces excellent freeze point depression while maintaining relatively low vapor pressure.

**Key molecular characteristics:**
- Chemical formula: CH₃CH(OH)CH₂OH
- CAS number: 57-55-6
- Molecular weight: 76.09 g/mol
- Boiling point: 188.2°C (370.8°F) at 101.325 kPa
- Melting point: -59°C (-74.2°F)
- Flash point: 107°C (225°F) closed cup
- Autoignition temperature: 371°C (700°F)

### Toxicity and Safety Classification

The U.S. Food and Drug Administration classifies propylene glycol as Generally Recognized as Safe (GRAS) under 21 CFR 184.1666 for direct food contact applications. This classification permits its use in food processing systems, beverage cooling, and pharmaceutical manufacturing where incidental contact with products may occur.

**Safety advantages:**
- LD₅₀ (oral, rat): 20-32 g/kg body weight
- Non-carcinogenic per IARC evaluation
- Metabolized to lactic acid and pyruvic acid in human body
- Acceptable daily intake: 25 mg/kg body weight (WHO)
- USP grade available for pharmaceutical applications
- NSF/ANSI 60 certified for potable water system components

The substantially lower toxicity compared to ethylene glycol (LD₅₀ approximately 4.7 g/kg) makes propylene glycol mandatory in many jurisdictions for systems with potential food or drinking water exposure.

## Freeze Point Depression

### Concentration vs. Freezing Point Relationship

Propylene glycol aqueous solutions exhibit non-linear freeze point depression behavior. The eutectic point occurs at approximately 60% propylene glycol by mass, producing a freeze point of -59°C (-74°F). Beyond this concentration, the freeze point rises as pure propylene glycol concentration increases.

**Freeze point data for propylene glycol solutions:**

| Concentration (% by mass) | Freeze Point °C | Freeze Point °F | Typical Application |
|---------------------------|-----------------|-----------------|---------------------|
| 10 | -3.9 | 25 | Light freeze protection |
| 15 | -6.7 | 20 | Minimal freeze protection |
| 20 | -9.4 | 15 | Limited outdoor exposure |
| 25 | -12.8 | 9 | Standard mild climate |
| 30 | -16.7 | 2 | Moderate freeze protection |
| 35 | -21.1 | -6 | Cold climate standard |
| 40 | -26.1 | -15 | Severe cold climate |
| 45 | -31.7 | -25 | Arctic applications |
| 50 | -37.2 | -35 | Maximum practical concentration |
| 55 | -43.3 | -46 | Near-eutectic mixture |
| 60 | -51.7 | -61 | Eutectic composition |

### Design Concentration Selection

ASHRAE and industry practice recommend sizing glycol concentration to provide freeze protection to at least 5.5°C (10°F) below the lowest anticipated fluid temperature. This safety margin accounts for:

1. Local concentration variations during system operation
2. Fluid degradation over time reducing freeze protection
3. Transient conditions during equipment startup or failure
4. Uncertainties in outdoor design temperatures

**Typical concentration ranges:**
- **25-30%**: Closed-loop systems in conditioned spaces, chilled water with limited exposure
- **30-40%**: Standard HVAC applications in moderate climates, rooftop equipment
- **40-50%**: Outdoor equipment in cold climates, snow melting systems
- **Above 50%**: Specialized low-temperature applications, process cooling

Concentrations exceeding 50-55% provide diminishing returns for freeze protection while substantially increasing viscosity and reducing heat transfer performance. Most HVAC applications employ 30-40% solutions as the practical optimum.

## Thermophysical Property Data

### Density

Propylene glycol solution density increases with concentration and decreases with temperature. Accurate density data enables proper fluid inventory calculations, expansion tank sizing, and pressure drop analysis.

**Density at 20°C (68°F):**

| Concentration (% by mass) | Density (kg/m³) | Density (lb/ft³) | Specific Gravity |
|---------------------------|-----------------|------------------|------------------|
| 0 (water) | 998 | 62.3 | 1.000 |
| 10 | 1008 | 62.9 | 1.010 |
| 20 | 1017 | 63.5 | 1.019 |
| 30 | 1026 | 64.1 | 1.028 |
| 40 | 1034 | 64.6 | 1.036 |
| 50 | 1041 | 65.0 | 1.043 |
| 60 | 1047 | 65.4 | 1.049 |
| 100 | 1036 | 64.7 | 1.038 |

**Temperature correction:**
Density decreases approximately 0.5-0.7 kg/m³ per °C temperature increase for typical HVAC concentrations. For precise calculations, consult manufacturer data sheets or ASHRAE Handbook—Fundamentals, Chapter 31.

### Dynamic Viscosity

Viscosity represents the most significant performance penalty when substituting propylene glycol for water or ethylene glycol. Higher viscosity increases pumping power requirements, reduces heat transfer coefficients, and affects system control characteristics.

**Dynamic viscosity data:**

| Temp °C | 0% PG (Water) | 30% PG | 40% PG | 50% PG |
|---------|---------------|---------|---------|---------|
| -10 | - | 12.5 | 22.0 | 45.0 |
| 0 | 1.79 | 5.8 | 9.5 | 17.5 |
| 10 | 1.31 | 3.5 | 5.4 | 9.2 |
| 20 | 1.00 | 2.4 | 3.5 | 5.6 |
| 30 | 0.80 | 1.7 | 2.5 | 3.8 |
| 40 | 0.65 | 1.3 | 1.8 | 2.7 |
| 50 | 0.55 | 1.0 | 1.4 | 2.0 |
| 60 | 0.47 | 0.8 | 1.1 | 1.6 |

*Units: mPa·s (cP)*

At 20°C, a 40% propylene glycol solution exhibits 3.5 times the viscosity of pure water. This viscosity ratio increases dramatically at lower temperatures, reaching 14-fold at 0°C. The strong temperature dependence requires careful pump selection for systems operating across wide temperature ranges.

### Specific Heat Capacity

Propylene glycol solutions possess higher specific heat than ethylene glycol solutions at equivalent concentrations, partially offsetting the viscosity disadvantage. Higher specific heat reduces required flow rates for a given heat transfer duty.

**Specific heat capacity at 20°C (68°F):**

| Concentration (% by mass) | cp (kJ/kg·K) | cp (Btu/lb·°F) | Relative to Water |
|---------------------------|--------------|----------------|-------------------|
| 0 (water) | 4.182 | 0.999 | 100% |
| 10 | 4.130 | 0.987 | 98.8% |
| 20 | 4.070 | 0.972 | 97.3% |
| 30 | 4.010 | 0.958 | 95.9% |
| 40 | 3.940 | 0.941 | 94.2% |
| 50 | 3.865 | 0.923 | 92.4% |
| 60 | 3.780 | 0.903 | 90.4% |
| 100 | 2.480 | 0.592 | 59.3% |

The specific heat decreases approximately 0.4% per 1% increase in glycol concentration for solutions up to 50%. Temperature effects on specific heat remain modest over typical HVAC operating ranges (±5% variation from -10°C to 60°C).

### Thermal Conductivity

Thermal conductivity decreases significantly with increasing propylene glycol concentration, reducing heat transfer performance in heat exchangers and coils.

**Thermal conductivity at 20°C (68°F):**

| Concentration (% by mass) | k (W/m·K) | k (Btu/h·ft·°F) | Relative to Water |
|---------------------------|-----------|-----------------|-------------------|
| 0 (water) | 0.598 | 0.345 | 100% |
| 10 | 0.555 | 0.321 | 92.8% |
| 20 | 0.512 | 0.296 | 85.6% |
| 30 | 0.470 | 0.272 | 78.6% |
| 40 | 0.430 | 0.248 | 71.9% |
| 50 | 0.391 | 0.226 | 65.4% |
| 60 | 0.355 | 0.205 | 59.4% |

A 40% propylene glycol solution conducts heat at only 72% the rate of pure water. Combined with higher viscosity (lower Reynolds numbers) and reduced mass flow rates, the overall heat transfer coefficient in typical HVAC equipment decreases by 20-35% compared to water.

### Volumetric Heat Transfer Capacity

The product of density, specific heat, and flow velocity determines the volumetric heat transfer capacity—the heat transport per unit volume of fluid. This parameter directly relates to required flow rates and pipe sizing.

**Volumetric heat capacity at 20°C:**

| Concentration (% by mass) | ρcp (MJ/m³·K) | Relative to Water |
|---------------------------|---------------|-------------------|
| 0 (water) | 4.174 | 100% |
| 20 | 4.139 | 99.2% |
| 30 | 4.114 | 98.6% |
| 40 | 4.074 | 97.6% |
| 50 | 4.024 | 96.4% |

Propylene glycol solutions retain 96-99% of water's volumetric heat capacity at practical concentrations, minimizing the flow rate penalty for a given heat transfer duty.

## Heat Transfer Performance Considerations

### Overall Heat Transfer Coefficient Reduction

The combined effects of increased viscosity, reduced thermal conductivity, and modified flow characteristics result in substantial reductions in overall heat transfer coefficient (U-value) for HVAC equipment.

**Approximate U-value multipliers for propylene glycol solutions:**
- 20% concentration: 0.88-0.93
- 30% concentration: 0.82-0.87
- 40% concentration: 0.75-0.82
- 50% concentration: 0.68-0.75

These multipliers apply to turbulent flow conditions in typical HVAC heat exchangers (shell-and-tube, plate-and-frame, coils). Actual values depend on:
- Heat exchanger geometry and surface area
- Flow regime (Reynolds number)
- Operating temperature range
- Cleanliness factor

**Design implications:**
- Increase heat exchanger surface area by 15-25% when converting from water to 30-40% propylene glycol
- Derate manufacturer catalog capacities for standard water-rated equipment
- Verify with manufacturer if equipment data includes glycol correction factors
- Consider oversized coils or increased coil rows for critical applications

### Film Coefficient Impact

The film heat transfer coefficient on the fluid side decreases due to:

1. **Reduced thermal conductivity**: Direct reduction in the Nusselt number per the Dittus-Boelter equation
2. **Increased viscosity**: Lower Reynolds number for given flow velocity, potentially transitioning from turbulent to transitional flow
3. **Modified Prandtl number**: Changes heat transfer correlation relationships

For turbulent flow in tubes:
```
Nu = 0.023 Re^0.8 Pr^0.3
```

The Prandtl number (Pr = μcp/k) increases dramatically with glycol concentration:
- Water at 20°C: Pr ≈ 7
- 30% PG at 20°C: Pr ≈ 17
- 40% PG at 20°C: Pr ≈ 24

While increased Prandtl number provides some compensating effect (Pr^0.3 term), the dominant viscosity impact reduces Reynolds number and overall film coefficient by 15-30% for typical HVAC conditions.

## Pumping Power and Pressure Drop

### Viscosity-Induced Pressure Drop Increase

Propylene glycol solutions require substantially higher pumping power than water for equivalent flow rates. The Darcy-Weisbach equation demonstrates pressure drop proportionality to dynamic viscosity in laminar flow and indirect viscosity effects through the friction factor in turbulent flow.

**Approximate pressure drop multipliers at 20°C:**

| Concentration | Turbulent Flow (Re > 4000) | Transitional Flow |
|---------------|---------------------------|-------------------|
| 20% PG | 1.15-1.25 | 1.5-2.0 |
| 30% PG | 1.25-1.40 | 2.0-3.0 |
| 40% PG | 1.40-1.60 | 3.0-4.5 |
| 50% PG | 1.60-1.90 | 4.5-7.0 |

**Critical design considerations:**

1. **Pipe sizing**: Consider upsizing distribution piping by one nominal size to maintain reasonable pressure drops and preserve turbulent flow conditions
2. **Pump selection**:
   - Select pumps for 1.5-2.0 times the head required for water
   - Verify operating point remains in efficient range of pump curve
   - Account for viscosity effects on pump performance curves
3. **Flow regime**: Higher viscosity reduces Reynolds number, potentially transitioning flow from turbulent (Re > 4000) to transitional (2300 < Re < 4000) or even laminar (Re < 2300), dramatically increasing pressure drop
4. **Temperature variation**: Systems operating across wide temperature ranges experience significant viscosity variation, affecting control valve authority and pump performance

### Pump Performance Correction

Centrifugal pump performance degrades with increased fluid viscosity. The Hydraulic Institute provides correction factors for head, flow, and efficiency:

**Typical corrections for 40% PG at 20°C (viscosity ≈ 3.5 cP):**
- Head correction factor (CH): 0.97-0.98
- Flow correction factor (CQ): 0.98-0.99
- Efficiency correction factor (Cη): 0.90-0.95

For viscosities exceeding 50 cP (cold startup conditions), corrections become severe and may require specialized pump selection or fluid preheating strategies.

## Food-Grade and Potable Water Applications

### Regulatory Requirements

Propylene glycol for HVAC applications must meet specific purity standards when used in systems with potential food or potable water contact:

**NSF/ANSI Standard 60**: Drinking Water System Components
- Covers glycols used in heat exchangers serving potable water systems
- Requires toxicological evaluation and maximum use level determination
- Mandates proper labeling and material safety documentation

**FDA Regulation 21 CFR 184.1666**: GRAS status
- Permits direct and indirect food contact
- Establishes good manufacturing practice limitations
- Requires food-grade quality specifications (USP or FCC grade)

**USDA/FDA Food Safety**: Food processing facilities
- Heat transfer fluids must be food-grade certified
- Requires proper leak detection and monitoring
- System design must prevent contamination pathways

### Quality Specifications

**USP (United States Pharmacopeia) grade requirements:**
- Minimum purity: 99.5% propylene glycol
- Maximum water content: 0.2%
- Heavy metals: < 5 ppm
- Chloride: < 50 ppm
- Sulfate: < 50 ppm
- Acidity/alkalinity limits defined
- Residue on ignition: < 0.005%

**Inhibitor packages for food-grade systems:**
Standard automotive or industrial glycol inhibitors often contain toxic components (nitrites, borates, phosphates, silicates) unsuitable for food contact. Food-grade formulations employ:
- Potassium sorbate or sodium benzoate (biological growth control)
- Food-grade corrosion inhibitors (organic acids, pH buffers)
- Reduced or eliminated heavy metal passivators

### Application Examples

**Beverage industry:**
- Brewery glycol systems (fermentation temperature control)
- Winery tank cooling
- Soft drink carbonation cooling
- Process water chillers with potential cross-contamination

**Food processing:**
- Meat processing facility refrigeration
- Dairy processing cooling systems
- Produce cooling and cold storage
- Prepared food manufacturing

**Pharmaceutical manufacturing:**
- Clean room HVAC systems
- Process cooling for temperature-sensitive reactions
- Equipment jacket cooling
- Freeze drying condenser cooling

**Skating rinks and ice arenas:**
- Secondary coolant for ice rink floor cooling
- Reduced toxicity for public facilities
- Enhanced safety for facility maintenance personnel

## Corrosion and Materials Compatibility

### Inhibitor Chemistry

Uninhibited propylene glycol solutions exhibit corrosive behavior toward common HVAC system metals, particularly ferrous materials and aluminum. The degradation mechanism involves:

1. **Oxidation**: Dissolved oxygen reacts with glycol at elevated temperatures, forming organic acids (formic acid, glycolic acid)
2. **Acid attack**: Organic acids reduce solution pH, accelerating metal corrosion
3. **Autocatalytic degradation**: Corrosion products (metal ions) catalyze further glycol oxidation

**Required inhibitor functions:**
- pH buffering (maintain pH 8.5-10.5)
- Metal passivation (protective oxide layer formation)
- Oxygen scavenging (reduce oxidation reactions)
- Biological growth control (prevent bacterial and algae contamination)

### Materials Selection

**Compatible materials:**
- **Ferrous metals**: Carbon steel, cast iron (with proper inhibitors)
- **Stainless steel**: 304, 316 (excellent compatibility)
- **Copper and copper alloys**: Brass, bronze (widely used in HVAC)
- **Elastomers**: EPDM, nitrile (Buna-N), neoprene
- **Plastics**: PVC, CPVC, polypropylene, polyethylene

**Materials requiring caution:**
- **Zinc**: Galvanized steel not recommended (zinc dissolution, white rust formation)
- **Aluminum**: Requires specialized inhibitors; aluminum heat exchangers need manufacturer confirmation
- **Natural rubber**: May soften or swell; use synthetic elastomers
- **Polyacetal (Delrin)**: Potential stress cracking in concentrated solutions

### System Cleanliness Requirements

New or renovated systems require thorough cleaning before glycol introduction:

1. **Mechanical cleaning**: Remove mill scale, welding slag, installation debris
2. **Chemical cleaning**: Alkaline cleaners or specialized detergents to remove oils and organic contaminants
3. **Flushing**: Multiple volume changes with clean water until clear
4. **Passivation**: For critical applications, chemical passivation of steel surfaces
5. **Drying**: Remove excess water to achieve target glycol concentration

Contamination introduction during system startup causes accelerated glycol degradation and inhibitor depletion.

## Fluid Maintenance and Service Life

### Monitoring Requirements

ASHRAE Guideline 3-2012 and manufacturers recommend annual testing of glycol solutions for:

**Critical parameters:**
- **pH**: Target range 8.5-10.5; values below 7.5 indicate significant degradation
- **Reserve alkalinity**: Measures remaining inhibitor capacity
- **Freeze point**: Confirms glycol concentration; detects dilution from makeup water
- **Specific gravity**: Secondary confirmation of concentration
- **Appearance**: Clear to slightly yellow acceptable; brown coloration indicates severe oxidation

**Optional advanced testing:**
- Organic acid content (glycolic acid, formic acid)
- Metal ion concentration (iron, copper, aluminum)
- Biological contamination assessment
- Viscosity verification

### Service Life Expectations

Properly maintained propylene glycol systems achieve service lives of:
- **Closed systems with quality inhibitors**: 5-10 years
- **Systems with poor maintenance**: 2-3 years before significant degradation
- **Systems with chronic air ingress**: 1-2 years
- **Open or vented systems**: Annual replacement typically required

**Service life limiting factors:**
- Dissolved oxygen exposure (system design, makeup water introduction)
- Operating temperature (degradation accelerates exponentially above 65°C/150°F)
- Metal surface area to fluid volume ratio
- Inhibitor package quality and concentration
- Contamination introduction

### Fluid Replacement Criteria

Replace propylene glycol solutions when:
1. pH drops below 7.5 and cannot be restored by inhibitor addition
2. Reserve alkalinity depletes below manufacturer's specified minimum
3. Visual appearance becomes dark brown or cloudy
4. Organic acid content exceeds acceptable limits
5. Corrosion evidence appears in system components

Partial fluid replacement with inhibitor recharge extends service life in moderately degraded systems. Complete replacement proves necessary for severely degraded fluids to remove accumulated organic acids and corrosion products.

## System Design Best Practices

### Concentration Selection Strategy

**Decision framework:**

1. **Determine minimum fluid temperature**:
   - Design outdoor temperature for exposed piping and equipment
   - Chiller supply temperature plus 5.5°C (10°F) margin
   - Process requirements for specialized applications

2. **Select freeze protection level**:
   - Add 5.5°C (10°F) safety margin to minimum fluid temperature
   - Consider burst protection (slush formation) versus complete freeze prevention
   - Account for transient conditions and control failures

3. **Evaluate performance impact**:
   - Calculate heat transfer coefficient reduction
   - Determine pressure drop and pumping power increase
   - Assess economic impact of oversized equipment versus higher glycol concentration

4. **Optimize for application**:
   - Use minimum concentration providing adequate protection
   - Consider split concentration strategy (higher concentration in exposed sections)
   - Evaluate economics of improved insulation versus higher glycol concentration

### Equipment Sizing Modifications

**Heat exchangers:**
- Increase surface area by (1/U-multiplier - 1) to maintain capacity
- Example: 30% PG with U-multiplier of 0.85 requires 18% additional surface area
- Specify glycol service and concentration on equipment submittals
- Request manufacturer performance data for actual fluid properties

**Coils:**
- Add coil rows or increase face area for air-side equipment
- Reduce published capacities by 15-25% for standard water-rated coils
- Verify pressure drop remains within acceptable limits
- Consider enhanced fin geometries for glycol service

**Piping:**
- Upsize by one nominal diameter for long runs (>30 m / 100 ft)
- Maintain minimum velocity of 1 m/s (3 ft/s) to preserve turbulent flow
- Limit velocity to 2.5 m/s (8 ft/s) to control erosion and noise
- Calculate pressure drop using actual glycol properties, not water values

**Pumps:**
- Select for 1.5-2.0 times water system head
- Verify efficiency at operating point with viscous fluid
- Consider variable speed capability for systems with wide temperature ranges
- Confirm mechanical seal and bearing compatibility with glycol

### Air Elimination and Expansion Control

**Air separation:**
Propylene glycol solutions absorb less dissolved air than water, but air elimination remains critical:
- Install air separators at points of lowest solubility (high temperature, low pressure)
- Use tangential or centrifugal separators sized for glycol viscosity
- Locate automatic air vents at high points throughout system
- Consider vacuum deaeration for critical applications

**Expansion accommodation:**
Propylene glycol solutions exhibit higher thermal expansion coefficients than water:

| Concentration | Expansion Coefficient | Relative to Water |
|---------------|----------------------|-------------------|
| 0% (water) | 0.0002 per °C | 1.0 |
| 30% PG | 0.00065 per °C | 3.25 |
| 40% PG | 0.00075 per °C | 3.75 |

**Expansion tank sizing implications:**
- Calculate expansion volume using glycol coefficient, not water
- Typical expansion tanks require 1.5-2.0 times the volume for equivalent water system
- Account for higher system fill volume due to glycol density
- Verify acceptance volume accommodates full temperature range

### Freeze Protection System Design

**Double-wall heat exchangers:**
Required by many codes for potable water applications, double-wall designs provide:
- Physical separation preventing glycol contamination of potable water
- Visible leak detection in intermediate space
- Atmospheric vent to prevent pressure crossover
- ANSI/AHRI Standard 400 compliance for refrigerant-to-water applications

**Leak detection:**
Implement monitoring strategies:
- Conductivity sensors in potable water systems (glycol increases conductivity)
- Regular sampling and analysis of protected system
- Visual inspection of intermediate spaces in double-wall exchangers
- Pressure monitoring for differential pressure loss

**Emergency procedures:**
Establish protocols for glycol leak incidents:
- Immediate system isolation and drainage
- Potable water system flushing procedures
- Contamination assessment and remediation
- Notification requirements for regulatory authorities

## Economic Considerations

### Initial Cost Factors

**Fluid cost comparison (typical installed cost per gallon):**
- Water: $0 (negligible)
- Industrial propylene glycol: $4-7 per gallon
- Inhibited propylene glycol: $6-10 per gallon
- Food-grade/USP propylene glycol: $12-20 per gallon

For a 1000-gallon system at 30% concentration, fluid cost ranges from $1,800 to $6,000 depending on quality grade.

**Equipment cost impacts:**
- Oversized heat exchangers: +15-25% first cost
- Larger pumps and motors: +10-20% first cost
- Upsized piping: +5-10% first cost
- Total system cost increase: typically 10-20% for glycol versus water

### Operating Cost Analysis

**Energy penalties:**
- Increased pumping power: 30-60% higher electrical consumption
- Reduced chiller efficiency: 5-10% increase in compressor energy (lower evaporator temperature to achieve same capacity)
- Additional fan power: if coils upsized and air pressure drop increases

**Maintenance costs:**
- Annual fluid testing: $100-300 per sample
- Fluid replacement cycle: $2,000-10,000+ per replacement (material plus labor)
- Increased pump maintenance: higher bearing loads from increased viscosity

**Life cycle cost calculation:**
Evaluate total cost of ownership:
```
LCC = Initial + Σ(Energy × Years) + Σ(Maintenance × Years) + Replacement
```

For many applications, the safety and regulatory compliance benefits justify the 15-30% life cycle cost premium versus water-based systems.

## Code and Standards References

### ASHRAE Guidelines

**ASHRAE Handbook—Fundamentals (2021), Chapter 31: Secondary Coolants (Brines)**
- Comprehensive property data for propylene glycol solutions
- Heat transfer correction factors
- System design recommendations

**ASHRAE Handbook—HVAC Systems and Equipment (2020), Chapter 13: Hydronic Heating and Cooling**
- Glycol system design practices
- Equipment selection and sizing

**ASHRAE Guideline 3-2012: Reducing Emission of Halogenated Refrigerants from Refrigerant System Startup, Service and Disposal**
- Applies to secondary coolant loop quality and maintenance

### Industry Standards

**NSF/ANSI 60**: Drinking Water Treatment Chemicals—Health Effects
- Certification requirement for glycols in potable water systems
- Maximum concentration limits
- Toxicological evaluation requirements

**ASTM D1384**: Standard Test Method for Corrosion Test for Engine Coolants in Glassware
- Laboratory corrosion testing protocol
- Acceptance criteria for inhibitor packages

**ASTM D3321**: Standard Test Method for Simulated Service Corrosion Testing of Engine Coolants
- Dynamic corrosion testing procedure
- More representative of actual system conditions than D1384

**ASTM E1177**: Standard Specification for Engine Coolant Solutions Containing Propylene Glycol
- Material specifications
- Performance requirements
- Quality control testing

### Building Codes

**International Mechanical Code (IMC)**
- Section 1106.2: Protection of potable water
- Requirements for double-wall heat exchangers
- Backflow prevention mandates

**International Plumbing Code (IPC)**
- Cross-connection control requirements
- Heat exchanger construction standards

**Local amendments**: Many jurisdictions mandate propylene glycol (versus ethylene glycol) for specific applications based on local safety concerns and environmental regulations.

## Comparison with Ethylene Glycol

### Performance Differences

**Ethylene glycol advantages:**
- 20-30% lower viscosity at equivalent concentration and temperature
- 5-10% better thermal conductivity
- Lower cost ($3-5 per gallon typical)
- Better heat transfer performance (10-15% higher U-values)
- More mature inhibitor technology

**Propylene glycol advantages:**
- Substantially lower toxicity (LD₅₀ 4-7 times higher)
- GRAS status for food contact applications
- Reduced environmental impact
- NSF/ANSI 60 certification available
- Meets safety requirements for schools, hospitals, food facilities

### Application Selection Criteria

**Use propylene glycol when:**
- Food processing or beverage production facilities
- Potable water system heat exchangers
- Schools, hospitals, public facilities (enhanced safety)
- Local codes mandate low-toxicity coolants
- Pharmaceutical or clean room applications

**Consider ethylene glycol when:**
- Industrial applications without food contact
- Performance optimization critical (minimizing equipment size)
- Operating cost minimization priority
- Severe cold climate (>50% concentration required)
- Closed systems with minimal human exposure

The 20-30% cost premium and 15-25% performance penalty for propylene glycol prove acceptable in applications where safety and regulatory compliance outweigh economic optimization.

## Troubleshooting Common Issues

### High Viscosity Problems

**Symptoms:**
- Insufficient flow rates
- Pump cavitation or dead-heading
- Poor heat transfer performance
- High pressure drops

**Causes:**
- Concentration too high for application
- Fluid temperature too low
- Degraded fluid with increased viscosity
- Undersized piping or components

**Solutions:**
- Reduce glycol concentration to minimum required
- Improve system insulation to maintain fluid temperature
- Install heat tracing for extreme cold exposure
- Test and replace degraded fluid
- Upsize piping and components

### Corrosion and Fluid Degradation

**Symptoms:**
- Darkening fluid color (yellow to brown)
- pH below 7.5
- Metal debris in strainer screens
- Heat exchanger or coil leaks
- Reduced system capacity

**Causes:**
- Depleted inhibitor package
- Chronic air ingress
- Excessive operating temperatures
- Contaminated system
- Incorrect inhibitor type

**Solutions:**
- Test fluid annually and maintain inhibitor levels
- Repair air leaks and improve air elimination
- Install make-up water treatment (deaeration)
- Replace severely degraded fluid
- Clean system and passivate metal surfaces

### Freeze Protection Inadequacy

**Symptoms:**
- Ice formation in exposed piping
- Burst pipes or heat exchangers
- Slush formation restricting flow

**Causes:**
- Dilution from makeup water addition
- Concentration stratification in low-flow areas
- Design temperature exceeded
- Control system failure allowing overcooling

**Solutions:**
- Test freeze point and restore concentration
- Improve fluid mixing (eliminate dead legs, install circulation pumps)
- Re-evaluate design conditions and increase protection
- Add temperature alarms and low-temperature cutouts

---

## Summary

Propylene glycol serves as the preferred secondary coolant for HVAC applications requiring low toxicity and food-grade compatibility. While exhibiting lower heat transfer performance and higher cost compared to ethylene glycol and water, its GRAS status and substantially reduced toxicity make it mandatory for food processing, potable water, and public facility applications.

**Key design considerations:**
- Select minimum concentration providing 5.5°C (10°F) margin below minimum fluid temperature
- Increase heat exchanger surface area by 15-25% to compensate for reduced heat transfer
- Upsize pumps for 1.5-2.0 times water system head requirements
- Specify food-grade USP or NSF-60 certified products for food contact applications
- Implement annual fluid testing and maintenance program
- Design for 3-4 times water expansion coefficient

Proper system design, quality inhibitor packages, and regular maintenance enable propylene glycol systems to achieve reliable service lives of 5-10 years while meeting stringent safety and regulatory requirements.
