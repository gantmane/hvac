---
title: "Ethylene Glycol"
description: "Comprehensive technical reference for ethylene glycol secondary coolants in HVAC applications including thermophysical properties, freeze protection, toxicity considerations, and system design requirements"
weight: 1
---

## Overview

Ethylene glycol (EG) is the most widely used secondary coolant in HVAC applications requiring freeze protection. Its superior heat transfer characteristics, lower cost, and effective freeze protection across wide temperature ranges make it the primary choice for closed-loop hydronic systems in commercial and industrial facilities.

### Chemical Properties

Ethylene glycol (1,2-ethanediol, C₂H₆O₂) exhibits the following fundamental characteristics:

**Molecular Structure:**
- Chemical formula: HOCH₂CH₂OH
- Molecular weight: 62.07 g/mol
- CAS number: 107-21-1
- Structure: Two hydroxyl groups on adjacent carbon atoms

**Pure Substance Properties (at 20°C):**
- Density: 1,113 kg/m³
- Viscosity: 16.1 cP (compared to water at 1.0 cP)
- Specific heat: 2.382 kJ/(kg·K)
- Thermal conductivity: 0.252 W/(m·K)
- Boiling point: 197.3°C at 101.3 kPa
- Freezing point: -12.7°C

The addition of ethylene glycol to water creates a eutectic solution with minimum freezing point at approximately 60% concentration by mass (-48.3°C). This non-ideal mixture exhibits thermophysical properties significantly different from either pure component.

## Freeze Protection Characteristics

### Concentration vs Freezing Point

The relationship between ethylene glycol concentration and freeze protection follows a non-linear curve with critical design implications:

| Concentration (% by mass) | Concentration (% by volume) | Freezing Point (°C) | Freezing Point (°F) | Burst Protection (°C) |
|---------------------------|----------------------------|---------------------|---------------------|----------------------|
| 10 | 9 | -3.9 | 25 | -1.7 |
| 15 | 14 | -6.7 | 20 | -2.8 |
| 20 | 18 | -8.9 | 16 | -4.4 |
| 25 | 23 | -12.2 | 10 | -6.7 |
| 30 | 27 | -15.6 | 4 | -9.4 |
| 35 | 32 | -20.6 | -5 | -13.3 |
| 40 | 37 | -25.6 | -14 | -17.8 |
| 45 | 41 | -31.7 | -25 | -23.3 |
| 50 | 46 | -37.8 | -36 | -30.0 |
| 55 | 50 | -43.9 | -47 | -37.2 |
| 60 | 55 | -48.3 | -55 | -43.9 |

**Critical Design Notes:**

1. **Eutectic point:** Maximum freeze protection occurs at 60% by mass. Higher concentrations provide less protection.

2. **Burst protection:** Solutions do not solidify instantaneously. The "burst protection" temperature represents the point where ice crystal formation creates sufficient viscosity to prevent circulation but may not rupture piping.

3. **Safety margin:** ASHRAE recommends designing for 5-10°F (3-6°C) below the lowest anticipated ambient temperature.

4. **Volume vs mass:** Concentration is typically specified by volume in commercial practice but by mass in technical literature. Always verify which basis is being used.

### Typical Concentration Ranges

Standard HVAC applications use the following concentration guidelines:

**25-30% by volume (28-33% by mass):**
- Indoor applications with minimal freeze risk
- Mechanical rooms with supplemental heat
- Protection to approximately 10°F (-12°C)

**35-40% by volume (38-43% by mass):**
- Standard outdoor applications in moderate climates
- Rooftop equipment in temperate zones
- Protection to approximately -10°F (-23°C)

**45-50% by volume (48-53% by mass):**
- Cold climate applications
- Unheated outdoor piping
- Solar thermal collectors
- Protection to approximately -30°F (-34°C)

**Above 50%:** Rarely used in HVAC applications due to significantly degraded heat transfer properties and increased pumping costs with minimal additional freeze protection benefit.

## Thermophysical Properties

### Density

Density decreases with both increasing temperature and increasing ethylene glycol concentration. Accurate density values are essential for pump sizing, expansion tank calculations, and flow measurement.

**Density at 20°C (68°F):**

| Concentration (% by volume) | Density (kg/m³) | Density (lb/ft³) | Specific Gravity |
|----------------------------|-----------------|------------------|------------------|
| 0 (Pure water) | 998 | 62.3 | 1.000 |
| 10 | 1,011 | 63.1 | 1.013 |
| 20 | 1,024 | 63.9 | 1.026 |
| 30 | 1,037 | 64.7 | 1.039 |
| 40 | 1,049 | 65.5 | 1.051 |
| 50 | 1,062 | 66.3 | 1.064 |
| 60 | 1,074 | 67.0 | 1.076 |

**Temperature correction:** Density decreases approximately 0.5-0.7 kg/m³ per °C increase in temperature for concentrations between 30-50%.

### Viscosity

Viscosity increases dramatically with ethylene glycol concentration and decreases with temperature. High viscosity directly impacts pumping power, flow regime (laminar vs turbulent), and heat transfer coefficients.

**Dynamic Viscosity (cP):**

| Temperature | 0% | 20% | 30% | 40% | 50% | 60% |
|-------------|-----|-----|-----|-----|-----|-----|
| -20°C (-4°F) | - | - | 42.5 | 65.0 | 115 | 220 |
| -10°C (14°F) | - | 8.5 | 18.5 | 28.0 | 45.0 | 80.0 |
| 0°C (32°F) | 1.79 | 3.5 | 7.5 | 11.5 | 17.5 | 29.0 |
| 10°C (50°F) | 1.31 | 2.4 | 4.5 | 6.5 | 9.5 | 14.5 |
| 20°C (68°F) | 1.00 | 1.8 | 3.2 | 4.5 | 6.2 | 9.0 |
| 40°C (104°F) | 0.65 | 1.2 | 1.9 | 2.6 | 3.4 | 4.6 |
| 60°C (140°F) | 0.47 | 0.85 | 1.3 | 1.7 | 2.2 | 2.9 |
| 80°C (176°F) | 0.35 | 0.65 | 0.95 | 1.2 | 1.5 | 2.0 |
| 100°C (212°F) | 0.28 | 0.52 | 0.75 | 0.95 | 1.2 | 1.5 |

**Critical Observations:**

1. **Exponential relationship:** Viscosity increases exponentially as temperature decreases, particularly below 0°C.

2. **50% solution impact:** At 0°C, a 50% solution has approximately 10 times the viscosity of water, requiring significantly higher pumping power.

3. **Laminar flow risk:** High viscosity at low temperatures may result in laminar flow (Re < 2,300), drastically reducing heat transfer coefficients.

4. **Start-up considerations:** Cold start-up conditions require careful pump selection to overcome high viscosity during initial circulation.

### Specific Heat

Specific heat capacity decreases with increasing ethylene glycol concentration, reducing the heat-carrying capacity of the solution per unit mass.

**Specific Heat at 20°C (68°F):**

| Concentration (% by volume) | Specific Heat kJ/(kg·K) | Specific Heat Btu/(lb·°F) | Relative to Water |
|----------------------------|-------------------------|---------------------------|-------------------|
| 0 (Pure water) | 4.182 | 0.999 | 1.00 |
| 10 | 4.062 | 0.970 | 0.97 |
| 20 | 3.935 | 0.940 | 0.94 |
| 30 | 3.808 | 0.910 | 0.91 |
| 40 | 3.682 | 0.880 | 0.88 |
| 50 | 3.555 | 0.849 | 0.85 |
| 60 | 3.428 | 0.819 | 0.82 |

**Temperature variation:** Specific heat increases slightly with temperature (approximately 0.5% per 10°C) but this effect is minor compared to concentration effects.

**System capacity impact:** A 50% ethylene glycol solution carries 15% less heat per unit mass than pure water, requiring increased flow rates to maintain equivalent heat transfer capacity.

### Thermal Conductivity

Thermal conductivity decreases with ethylene glycol concentration, reducing the fluid's ability to conduct heat and affecting heat exchanger performance.

**Thermal Conductivity at 20°C (68°F):**

| Concentration (% by volume) | Thermal Conductivity W/(m·K) | Thermal Conductivity Btu/(h·ft·°F) | Relative to Water |
|----------------------------|------------------------------|-------------------------------------|-------------------|
| 0 (Pure water) | 0.598 | 0.345 | 1.00 |
| 10 | 0.563 | 0.325 | 0.94 |
| 20 | 0.528 | 0.305 | 0.88 |
| 30 | 0.493 | 0.285 | 0.82 |
| 40 | 0.458 | 0.265 | 0.77 |
| 50 | 0.423 | 0.244 | 0.71 |
| 60 | 0.388 | 0.224 | 0.65 |

### Combined Heat Transfer Effect

The degradation in heat transfer performance results from the combined effects of reduced specific heat, thermal conductivity, and increased viscosity:

**Approximate Heat Transfer Penalty (compared to water):**

| Concentration | Film Coefficient Reduction | Flow Rate Increase Required | Pumping Power Increase |
|---------------|---------------------------|----------------------------|------------------------|
| 20% | 5-8% | 6-8% | 15-25% |
| 30% | 8-12% | 10-12% | 30-45% |
| 40% | 12-18% | 14-18% | 50-75% |
| 50% | 18-25% | 20-25% | 80-120% |

These penalties apply to typical turbulent flow conditions at normal operating temperatures. At low temperatures or during start-up, penalties may be significantly higher.

## Health and Safety Considerations

### Toxicity Profile

Ethylene glycol presents significant toxicity hazards that distinguish it from propylene glycol:

**Acute Toxicity:**
- Oral LD50 (rats): 4,700 mg/kg (moderately toxic)
- Sweet taste makes accidental ingestion more likely
- Metabolizes to glycolic acid and oxalic acid
- Metabolites cause severe metabolic acidosis and renal failure
- Lethal dose (adult human): approximately 100 mL pure EG

**Chronic Exposure:**
- Dermal absorption: Low but possible with prolonged contact
- Inhalation: Minimal risk at normal temperatures due to low vapor pressure
- Repeated skin contact may cause irritation

### Regulatory Classification

**OSHA:** Not classified as a hazardous substance under 29 CFR 1910.1200

**EPA:** Not regulated under TSCA or CERCLA at typical use concentrations

**NSF/ANSI 60:** Pure ethylene glycol is NOT approved for potable water systems or applications with potential for drinking water contact

**FDA:** Generally recognized as safe (GRAS) for specific food contact applications when inhibited formulations meet FDA requirements, but NOT for use in potable water

### Application Restrictions

**Prohibited Applications:**
- Potable water systems
- Drinking water heat exchangers without double-wall separation
- Food processing facilities (unless specifically NSF-approved formulation)
- Applications where drainage could contaminate drinking water sources
- Open systems with potential human contact
- Locations accessible to children or pets

**Permitted Applications:**
- Closed-loop HVAC systems
- Industrial process cooling
- Solar thermal systems
- Snow melting systems (with proper containment)
- Chilled water systems isolated from potable water

### Required Safety Measures

**Labeling Requirements:**

All systems containing ethylene glycol must be clearly labeled:
- "CAUTION: CONTAINS ETHYLENE GLYCOL"
- "NOT FOR USE IN POTABLE WATER SYSTEMS"
- "HARMFUL IF SWALLOWED"
- Emergency contact information

**Piping Identification:**

- Color coding distinct from potable water (never use green or blue)
- Flow direction arrows
- Concentration markings at key locations
- Warning labels at fill and drain points

**Spill Response:**

1. Evacuate non-essential personnel
2. Contain spill with absorbent materials
3. Prevent entry to drains or water sources
4. Dispose of contaminated materials as hazardous waste per local regulations
5. Flush area with water after cleanup
6. Report spills exceeding reportable quantities (varies by jurisdiction)

**Personal Protective Equipment:**

- Safety glasses or goggles
- Chemical-resistant gloves (nitrile or neoprene)
- Impervious apron for bulk handling
- Adequate ventilation when heating solutions

## Inhibitor Packages and Formulations

Pure ethylene glycol is corrosive to metals and must be used with corrosion inhibitor packages for HVAC applications.

### Inhibitor Chemistry

**Traditional Inhibitors (Inorganic):**
- Sodium nitrite (ferrous metal protection)
- Sodium borate (pH buffer)
- Sodium molybdate (general corrosion inhibition)
- Sodium silicate (aluminum protection)

**Organic Acid Technology (OAT):**
- Organic carboxylates
- Lower conductivity than traditional inhibitors
- Extended service life (5-10 years)
- Better compatibility with non-metallic materials

**Hybrid Inhibitors:**
- Combination of inorganic and organic inhibitors
- Optimized for mixed-metal systems
- Balance of immediate and long-term protection

### Compatibility Requirements

**Metals:**
- Ferrous metals: Excellent with proper inhibitors
- Copper and copper alloys: Excellent with proper inhibitors
- Aluminum: Requires specific inhibitors (silicon-free formulations)
- Galvanized steel: Limited compatibility; avoid if possible

**Non-Metallic Materials:**
- Standard EPDM: Excellent
- Nitrile rubber: Good
- Neoprene: Good
- Natural rubber: Poor (not recommended)
- Polyvinyl chloride (PVC): Generally acceptable
- CPVC: Acceptable below maximum rated temperatures
- Polyethylene (PE): Excellent (PEX tubing applications)

**Gaskets and Seals:**
- Use glycol-compatible materials
- Verify manufacturer compatibility statements
- Replace seals designed for water-only service

## System Design Considerations

### Concentration Selection

Select ethylene glycol concentration based on:

1. **Temperature requirements:** Lowest anticipated temperature with 5-10°F (3-6°C) safety margin

2. **Energy efficiency:** Use minimum concentration providing adequate freeze protection; excess concentration wastes energy

3. **System components:** Consider heat exchanger effectiveness reduction at high concentrations

4. **Pumping costs:** Higher concentrations require larger pumps and more operating energy

**Decision matrix example:**

| Design Condition | Recommended Concentration | Freeze Protection | Typical Application |
|------------------|--------------------------|-------------------|---------------------|
| Indoor, heated space | 20-25% | 15-20°F (-9 to -7°C) | Chilled beams, radiant panels |
| Outdoor, mild climate | 30-35% | 0 to -10°F (-18 to -23°C) | Rooftop equipment, temperate zones |
| Outdoor, cold climate | 40-45% | -15 to -30°F (-26 to -34°C) | Northern climates, solar systems |
| Extreme cold | 50% | -35°F (-37°C) | Arctic applications, special processes |

### Flow Rate Adjustments

When converting a water system to ethylene glycol, adjust design flow rates to maintain heat transfer capacity:

**Flow correction factor:**

F = (ρ_glycol × c_p,glycol) / (ρ_water × c_p,water)

Where the inverse (1/F) gives the required flow rate multiplier.

**Approximate flow rate multipliers:**

| Concentration | Flow Rate Multiplier | Example: 100 GPM water becomes |
|---------------|---------------------|--------------------------------|
| 20% | 1.06 | 106 GPM |
| 30% | 1.09 | 109 GPM |
| 40% | 1.13 | 113 GPM |
| 50% | 1.18 | 118 GPM |

These multipliers maintain equivalent heat capacity; additional increases may be needed to compensate for reduced heat transfer coefficients.

### Pump Sizing Adjustments

Account for increased pressure drop due to higher viscosity:

**Pressure drop correction (turbulent flow):**

ΔP_glycol / ΔP_water ≈ (μ_glycol / μ_water)^0.2

**Pumping power correction:**

P_glycol / P_water = (Flow multiplier) × (ΔP multiplier)

For accurate sizing, calculate Reynolds number to verify turbulent flow:

Re = (ρ × V × D) / μ

Where:
- ρ = density (kg/m³)
- V = velocity (m/s)
- D = diameter (m)
- μ = dynamic viscosity (Pa·s)

If Re < 2,300 (laminar flow), pressure drop increases linearly with viscosity rather than the 0.2 power relationship, requiring significantly larger pumps.

### Expansion Tank Sizing

Glycol solutions have higher thermal expansion coefficients than water, requiring larger expansion tanks.

**Expansion factors (volume change from 4°C to 93°C):**

| Fluid | Expansion (%) |
|-------|---------------|
| Water | 3.5 |
| 20% EG | 4.5 |
| 30% EG | 5.0 |
| 40% EG | 5.5 |
| 50% EG | 6.2 |

**Expansion tank sizing formula:**

V_tank = (V_system × E × (T_max - T_fill)) / ((P_max / P_fill) - (P_max / P_atm))

Where expansion factor E must be adjusted for glycol concentration.

### Heat Exchanger Performance

Glycol solutions reduce heat exchanger effectiveness due to:

1. **Lower heat transfer coefficients:** 5-25% reduction depending on concentration
2. **Reduced specific heat:** Requires higher flow rates
3. **Increased viscosity:** May reduce turbulence

**Correction approaches:**

- Increase heat exchanger surface area by 10-30%
- Increase flow rates to maintain turbulence
- Use enhanced tubes or plate heat exchangers
- Consider temperature penalties in sizing calculations

**Manufacturer consultation:** Always consult heat exchanger manufacturers when converting from water to glycol service, as performance data is often based on water.

## Maintenance and Testing

### Concentration Testing

Regular testing ensures proper freeze protection and prevents concentration drift:

**Testing methods:**

1. **Refractometer:** Most common field method
   - Quick and simple
   - Measures refractive index
   - Provides freeze point reading
   - Accuracy: ±2°F with proper calibration
   - Temperature compensation required

2. **Hydrometer:** Traditional method
   - Measures specific gravity
   - Less accurate than refractometer
   - Requires temperature correction
   - Slower than refractometer

3. **Titration:** Laboratory method
   - Most accurate (±1%)
   - Requires chemical analysis
   - Used for precise concentration determination

**Testing frequency:**

- Initial fill: Test before and after filling
- Seasonal: Before winter season
- Annual: Minimum once per year
- Post-maintenance: After any addition or modification
- Problem diagnosis: When freeze protection questioned

### Inhibitor Testing

Inhibitor depletion allows corrosion and degradation:

**Test parameters:**

1. **pH:** Should remain in range specified by manufacturer (typically 8.0-10.5)
   - Test frequency: Quarterly minimum
   - Method: pH meter or test strips
   - Corrective action: Adjust pH or replace fluid if out of range

2. **Reserve alkalinity:** Indicates inhibitor reserve
   - Test frequency: Annually
   - Method: Titration (laboratory or field test kit)
   - Minimum acceptable: Per manufacturer specification

3. **Metal ion content:** Indicates corrosion activity
   - Test frequency: Annually or when problems suspected
   - Method: Laboratory analysis
   - Elevated iron or copper indicates active corrosion

4. **Visual inspection:** Color and clarity
   - Dark or cloudy solution indicates degradation
   - Sediment or particulates indicate corrosion
   - Immediate action required if significant change

### Fluid Service Life

Properly inhibited ethylene glycol has the following typical service life:

**Traditional inhibitors:**
- Service life: 3-5 years
- Replacement triggers: pH out of range, reserve alkalinity depleted, visible degradation

**OAT inhibitors:**
- Service life: 5-10 years
- Replacement triggers: Contamination, pH shift, visible degradation

**Life extension:**

- Maintain proper concentration (dilution accelerates degradation)
- Prevent air ingress (oxygen accelerates corrosion)
- Use proper fill and venting procedures
- Install strainers to remove particulates
- Maintain system cleanliness

### Addition and Dilution

**Pre-mixed vs concentrate:**

- **Pre-mixed solutions:** Recommended for field use; eliminates mixing errors
- **Concentrate dilution:** Requires accurate measurement; use volume or mass calculations

**Dilution procedure (concentrate):**

1. Calculate required volume and concentration
2. Measure water volume accurately
3. Add concentrate slowly with circulation
4. Mix thoroughly (minimum 1 hour circulation)
5. Test concentration with refractometer
6. Adjust as necessary

**Topping off systems:**

- Never add water only to low systems (dilutes concentration)
- Add pre-mixed solution at system concentration
- Test concentration after addition
- Document all additions

## ASHRAE and Code References

**ASHRAE Handbook - HVAC Systems and Equipment:**
- Chapter 13: Hydronic Heating and Cooling
- Chapter 31: Secondary Coolants (Brines)
- Thermophysical property tables
- System design guidance

**ASHRAE Standard 15-2019:**
- Safety Standard for Refrigeration Systems
- Secondary coolant requirements
- Safety group classifications

**ASHRAE Standard 188-2018:**
- Legionellosis: Risk Management for Building Water Systems
- Glycol system isolation from potable water

**International Mechanical Code (IMC):**
- Section 1202: Hydronic Piping
- Section 305: Piping Support
- Secondary coolant system requirements

**International Plumbing Code (IPC):**
- Section 608: Protection of Potable Water Supply
- Backflow prevention requirements
- Separation from potable water

**NSF/ANSI 60:**
- Chemicals for Use in Potable Water
- Note: Standard ethylene glycol is NOT NSF-60 approved
- Requires propylene glycol for potable water contact risk

**Manufacturer Specifications:**
- Always follow glycol manufacturer's guidelines
- Inhibitor package requirements
- Concentration limits
- Material compatibility

## Best Practices Summary

1. **Concentration:** Use minimum concentration providing adequate freeze protection with safety margin; excess concentration wastes energy without benefit

2. **Inhibitors:** Use only properly inhibited formulations; never use automotive antifreeze in HVAC systems

3. **Compatibility:** Verify material compatibility for all system components including gaskets, seals, and non-metallic materials

4. **Isolation:** Maintain complete isolation from potable water systems; use double-wall heat exchangers where required

5. **Labeling:** Clearly label all glycol-containing systems with warnings and emergency information

6. **Testing:** Establish regular testing program for concentration, pH, and inhibitor reserve

7. **Documentation:** Maintain records of initial concentration, all additions, test results, and maintenance activities

8. **System design:** Account for flow rate increases, pump sizing corrections, expansion tank adjustments, and heat exchanger penalties

9. **Safety:** Provide appropriate spill containment, disposal procedures, and personnel training

10. **Replacement:** Replace fluid on schedule or when testing indicates degradation; do not exceed manufacturer's recommended service life

## Comparison with Propylene Glycol

While both glycols provide freeze protection, key differences inform selection:

| Parameter | Ethylene Glycol | Propylene Glycol |
|-----------|----------------|------------------|
| Toxicity | Toxic (LD50 4,700 mg/kg) | Low toxicity (LD50 20,000 mg/kg) |
| NSF-60 approval | Not approved | Approved formulations available |
| Freeze protection | Excellent (-48°C eutectic) | Good (-51°C eutectic) |
| Viscosity | Lower (better pumping) | Higher (20-40% more viscous) |
| Heat transfer | Better | 5-10% worse |
| Cost | Lower | 1.5-2× higher |
| Food facility use | Prohibited | Permitted |
| Typical HVAC use | Standard for isolated systems | Required for potable water risk |

**Selection guidance:** Use ethylene glycol for all applications with proper isolation from potable water unless regulations, codes, or contamination risk require propylene glycol.
