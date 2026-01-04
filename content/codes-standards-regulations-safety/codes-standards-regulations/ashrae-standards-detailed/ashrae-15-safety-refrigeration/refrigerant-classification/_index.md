---
title: "Refrigerant Safety Classification System"
description: "ASHRAE Standard 34 refrigerant classification combining toxicity (A/B) and flammability (1/2L/2/3) characteristics with safety group designations A1, A2L, A2, A3, B1, B2L, B2, B3 determining safety requirements."
date: 2026-01-04
weight: 1
---

The refrigerant safety classification system defined in ASHRAE Standard 34 and applied throughout ASHRAE Standard 15 provides a systematic framework for categorizing refrigerants based on toxicity and flammability hazards. This two-dimensional classification matrix enables appropriate safety requirements matching refrigerant characteristics, ensuring adequate protection while allowing practical system applications. The classification system combines letter designations for toxicity (A for lower toxicity, B for higher toxicity) with numerical/alphanumerical designations for flammability (1 for no flame propagation, 2L for lower flammability, 2 for flammable, 3 for higher flammability). Understanding refrigerant classification is fundamental to applying ASHRAE 15 safety requirements correctly and selecting appropriate refrigerants for specific applications.

## Classification System Structure

ASHRAE Standard 34 establishes an alphanumeric classification system creating eight distinct safety groups representing the full spectrum of refrigerant hazard profiles. The first character indicates toxicity class (A or B), and the second character indicates flammability class (1, 2L, 2, or 3). This systematic nomenclature enables immediate recognition of refrigerant hazard characteristics.

The safety group designation directly determines maximum refrigerant quantities in occupied spaces, machinery room requirements, ventilation specifications, detection system needs, and electrical equipment ratings under ASHRAE Standard 15. Lower-hazard refrigerants receive higher quantity limits and fewer restrictions. Higher-hazard refrigerants require more stringent safety provisions including mandatory machinery rooms, enhanced ventilation, and specialized detection.

The classification matrix creates a logical progression from lowest hazard (A1) to highest hazard (B3):

**Class A1:** Lower toxicity, no flame propagation (lowest overall hazard)
**Class A2L:** Lower toxicity, lower flammability
**Class A2:** Lower toxicity, flammable
**Class A3:** Lower toxicity, higher flammability
**Class B1:** Higher toxicity, no flame propagation
**Class B2L:** Higher toxicity, lower flammability
**Class B2:** Higher toxicity, flammable
**Class B3:** Higher toxicity, higher flammability (highest overall hazard)

This systematic structure ensures consistent hazard evaluation across all refrigerants while enabling appropriate differentiation of safety requirements based on actual risk levels.

## Toxicity Classification Criteria

Refrigerant toxicity classification divides refrigerants into Class A (lower toxicity) and Class B (higher toxicity) based on occupational exposure limit (OEL) testing following standardized protocols. The OEL represents the airborne concentration of refrigerant to which workers can be exposed without adverse health effects during normal work periods.

**Class A (Lower Toxicity)** includes refrigerants with OEL ≥400 ppm (parts per million) based on either:
- 8-hour time-weighted average (TWA) exposure, or
- 15-minute short-term exposure limit (STEL)

The 400 ppm threshold reflects toxicological testing showing that exposures below this level present minimal acute or chronic health risks. Class A refrigerants may cause simple asphyxiation at very high concentrations through oxygen displacement but do not produce toxic effects at concentrations below 400 ppm.

Most common refrigerants fall into Class A including:
- R-410A (HFC blend): OEL = 1,000 ppm
- R-134a (HFC): OEL = 1,000 ppm
- R-32 (HFC): OEL = 1,000 ppm
- R-290 (Propane): OEL = 1,000 ppm
- R-744 (CO₂): OEL = 5,000 ppm TWA, 30,000 ppm STEL

**Class B (Higher Toxicity)** includes refrigerants with OEL <400 ppm, indicating potential health effects from relatively low airborne concentrations. These refrigerants require more stringent safety provisions because smaller releases create hazardous atmospheres.

Class B refrigerants include:
- R-717 (Ammonia): OEL = 25 ppm TWA, 35 ppm STEL
- R-764 (Sulfur dioxide): OEL = 2 ppm TWA, 5 ppm STEL
- R-1150 (Ethylene): OEL = 200 ppm

The lower OEL values for Class B refrigerants reflect their irritant properties, potential respiratory effects, or systemic toxicity. Ammonia (R-717), despite its widespread industrial refrigeration use, remains Class B due to its irritant characteristics and relatively low exposure threshold.

Toxicity classification directly affects refrigerant quantity limits in occupied spaces. For Class A refrigerants, quantity limits typically base on 50,000 ppm (5%) concentration preventing oxygen displacement. For Class B refrigerants, quantity limits use the specific refrigerant's OEL, resulting in much lower allowable quantities for the same occupied space volume.

## Flammability Classification Criteria

Flammability classification divides refrigerants into four classes (1, 2L, 2, and 3) based on standardized flame propagation testing. The testing evaluates whether refrigerant-air mixtures propagate flame, flame propagation velocity, heat of combustion, and lower flammability limit (LFL) concentration.

**Class 1 (No Flame Propagation)** includes refrigerants showing no flame propagation when tested according to ASTM E681 or equivalent procedures. These refrigerants do not sustain combustion at any concentration when mixed with air at standard temperature and pressure. Class 1 refrigerants require no special precautions regarding ignition sources, electrical equipment, or ventilation for flammability considerations.

Common Class 1 refrigerants include:
- R-134a (1,1,1,2-tetrafluoroethane)
- R-404A (HFC blend)
- R-410A (R-32/125 blend)
- R-744 (Carbon dioxide)
- R-717 (Ammonia)

Despite containing flammable components in some blends (for example, R-32 in R-410A), the overall mixture composition prevents flame propagation, qualifying the blend as Class 1.

**Class 2L (Lower Flammability)** represents a recently established classification for mildly flammable refrigerants meeting specific criteria:
- Burning velocity ≤10 cm/s when tested per ASTM E681
- Heat of combustion <19 kJ/g
- Lower flammability limit (LFL) >0.10 kg/m³

The "2L" designation indicates these refrigerants are flammable but significantly less hazardous than Class 2 refrigerants. The low burning velocity means flames propagate slowly, allowing more time for detection and response. The heat of combustion limit ensures lower flame temperatures and reduced ignition probability.

Class 2L refrigerants include:
- R-32 (difluoromethane): LFL = 0.307 kg/m³, burning velocity ≈6.7 cm/s
- R-1234yf (HFO): LFL = 0.289 kg/m³, burning velocity ≈1.5 cm/s
- R-1234ze(E) (HFO): LFL = 0.303 kg/m³, burning velocity ≈1.5 cm/s
- R-454B (blend): LFL ≈0.281 kg/m³

The Class 2L category was created specifically to address the new generation of low-GWP refrigerants, particularly HFOs (hydrofluoroolefins), which are mildly flammable but represent significantly lower flammability hazards than traditional Class 2 refrigerants. ASHRAE Standard 15 allows higher refrigerant quantities for Class 2L compared to Class 2, recognizing the reduced hazard level while still requiring appropriate safety provisions.

**Class 2 (Flammable)** includes refrigerants showing flame propagation with:
- Burning velocity ≤10 cm/s, AND
- Heat of combustion ≥19 kJ/g, OR
- LFL ≤0.10 kg/m³

These refrigerants are definitively flammable, requiring significant safety provisions to prevent ignition and manage potential fire hazards.

Class 2 refrigerants include:
- R-1270 (Propylene): LFL = 0.047 kg/m³
- Some refrigerant blends combining flammable and non-flammable components

Class 2 refrigerants require machinery rooms for most applications, electrical equipment rated for flammable atmospheres in some cases, and refrigerant detection with lower alarm thresholds than Class 2L.

**Class 3 (Higher Flammability)** includes refrigerants with:
- Burning velocity >10 cm/s, OR
- LFL ≤0.10 kg/m³

The higher burning velocity indicates rapid flame propagation creating severe fire hazards. The low LFL means relatively small refrigerant releases create flammable atmospheres.

Class 3 refrigerants include:
- R-290 (Propane): LFL = 0.038 kg/m³, burning velocity ≈46 cm/s
- R-600a (Isobutane): LFL = 0.043 kg/m³
- R-1150 (Ethylene): LFL = 0.042 kg/m³

Class 3 refrigerants are highly flammable, requiring the most stringent safety provisions under ASHRAE 15. Applications are typically limited to small charges, specialized equipment with integral safety features, or industrial settings with comprehensive safety programs. Electrical equipment must be rated for flammable atmospheres, ignition sources must be eliminated, and detection systems with very low alarm thresholds are mandatory.

## Combined Safety Group Examples

Understanding how specific refrigerants classify within the safety matrix clarifies the system's practical application:

**R-134a: Class A1**
- Toxicity: OEL = 1,000 ppm (Class A)
- Flammability: No flame propagation (Class 1)
- Applications: Widespread use in commercial air conditioning, chillers, and automotive systems
- Safety provisions: Minimal restrictions, highest refrigerant quantity limits

**R-32: Class A2L**
- Toxicity: OEL = 1,000 ppm (Class A)
- Flammability: LFL = 0.307 kg/m³, burning velocity ≈6.7 cm/s (Class 2L)
- Applications: Residential and light commercial air conditioning, often in blends
- Safety provisions: Moderate restrictions, refrigerant quantity limits based on flammability, detection recommended for larger charges

**R-717 (Ammonia): Class B2L**
- Toxicity: OEL = 25 ppm (Class B)
- Flammability: LFL = 0.15 kg/m³, burning velocity ≈7-8 cm/s (Class 2L)
- Applications: Industrial refrigeration, large cold storage facilities
- Safety provisions: Strict quantity limits in occupied spaces, mandatory machinery rooms, ventilation, detection, and alarm systems

**R-290 (Propane): Class A3**
- Toxicity: OEL = 1,000 ppm (Class A)
- Flammability: LFL = 0.038 kg/m³, burning velocity ≈46 cm/s (Class 3)
- Applications: Limited to small charges in specialized equipment, some European residential applications, commercial refrigeration
- Safety provisions: Very low refrigerant quantity limits, electrical equipment rated for flammable atmospheres, comprehensive ignition source elimination

**R-1234yf: Class A2L**
- Toxicity: OEL = 500 ppm (Class A)
- Flammability: LFL = 0.289 kg/m³, burning velocity ≈1.5 cm/s (Class 2L)
- Applications: Automotive air conditioning replacement for R-134a, some commercial applications
- Safety provisions: Moderate restrictions, significantly higher quantity limits than Class 2 or 3, detection for larger systems

## Classification Testing Procedures

Refrigerant classification relies on standardized testing protocols ensuring consistent, reproducible results across different refrigerants and testing laboratories.

**Toxicity testing** follows protocols established by ASHRAE Standard 34, including:
- Acute inhalation toxicity studies determining short-term exposure effects
- Cardiac sensitization testing evaluating potential for heart rhythm disturbances
- Chronic exposure studies for widely-used refrigerants
- Occupational exposure monitoring and epidemiological studies where available

The OEL determination considers all toxicological data, with the most sensitive endpoint determining classification. For many refrigerants, cardiac sensitization represents the limiting factor. Some refrigerants sensitize the heart to adrenaline at relatively low concentrations, potentially causing arrhythmias. This effect typically determines OEL values for halogenated refrigerants.

**Flammability testing** follows ASTM E681, "Standard Test Method for Concentration Limits of Flammability of Chemicals (Vapors and Gases)." The procedure evaluates:

- Lower flammability limit (LFL): minimum refrigerant concentration supporting flame propagation
- Upper flammability limit (UFL): maximum refrigerant concentration supporting flame propagation
- Burning velocity: speed of flame front propagation through refrigerant-air mixture

Testing occurs at 21°C (70°F) and 101 kPa (1 atmosphere) in standardized apparatus. For refrigerants showing flame propagation, burning velocity measurement uses high-speed photography tracking flame front position over time.

Heat of combustion determination uses bomb calorimetry or calculation from molecular structure and thermodynamic properties:

$$\Delta H_c = \sum(\text{bond energies broken}) - \sum(\text{bond energies formed})$$

For halogenated refrigerants, fluorine and chlorine substitution reduces heat of combustion compared to pure hydrocarbons, often qualifying blends as Class 2L rather than Class 2 despite flame propagation.

## Impact on ASHRAE 15 Requirements

Refrigerant safety classification directly determines ASHRAE Standard 15 requirements for system design, installation, and operation. The classification affects every aspect of refrigeration safety provisions.

**Refrigerant quantity limits** in occupied spaces depend primarily on safety classification. For a commercial occupancy with 10,000 ft² floor area and 10 ft ceiling height:

- Class A1 refrigerant: ≈6,500 lb maximum (based on 5% oxygen displacement)
- Class A2L refrigerant: ≈625 lb maximum (based on LFL for R-32)
- Class A3 refrigerant: ≈75 lb maximum (based on LFL for R-290)
- Class B1 refrigerant: ≈350 lb maximum (based on ammonia OEL)

These dramatically different limits reflect the classification system's effect on practical system design. Class A1 refrigerants enable very large direct systems. Class A2L refrigerants allow moderate-sized systems without machinery rooms. Class A3 and all Class B refrigerants typically require machinery rooms except for very small charges.

**Machinery room requirements** trigger at different thresholds:
- Class A1: Usually not required unless extremely large refrigerant quantities
- Class A2L: Required when quantity exceeds limits typically allowing 600-2,000 lb depending on occupancy
- Class A2/A3: Required at much lower thresholds
- Class B: Nearly always required for any significant refrigerant quantity

**Detection system requirements** vary by class:
- Class A1: Generally not required
- Class A2L: Required in machinery rooms, recommended in occupied spaces for larger charges
- Class A2/A3: Required in machinery rooms and often in occupied spaces
- Class B: Mandatory in machinery rooms with lower alarm thresholds, often required in occupied spaces

**Ventilation rates** scale with hazard level:
- Class A1: Standard machinery room ventilation (0.5 cfm/ft²)
- Class A2L: Enhanced ventilation with emergency mode
- Class B: Higher ventilation rates, sophisticated emergency ventilation with multiple air changes per hour

**Electrical equipment ratings** depend on flammability:
- Class 1: Standard electrical equipment
- Class 2L: Standard equipment in most applications, some restrictions in machinery rooms
- Class 2: Rated equipment required in some locations
- Class 3: Comprehensive use of explosion-proof or intrinsically safe equipment in machinery rooms and high-concentration areas

Understanding refrigerant safety classification enables appropriate refrigerant selection for specific applications, proper application of ASHRAE Standard 15 requirements, and design of safe, code-compliant refrigeration systems. The classification system balances safety considerations with practical system needs, allowing lower-hazard refrigerants in direct systems while requiring appropriate provisions for higher-hazard refrigerants. As the refrigeration industry transitions to lower-GWP refrigerants, many of which are Class A2L, proper understanding of classification criteria and resulting safety requirements becomes increasingly critical for engineers, designers, and code officials.
