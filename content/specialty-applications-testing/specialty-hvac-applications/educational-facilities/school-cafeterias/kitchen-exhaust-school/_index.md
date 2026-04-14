---
title: "Kitchen Exhaust Systems for School Cafeterias"
aliases: ["Kitchen Exhaust Systems for School Cafeterias"]
description: "Technical design of Type I and Type II kitchen exhaust hoods for school cafeterias, including hood sizing, makeup air requirements, and energy recovery strategies."
date: 2025-01-05
keywords:
  - kitchen exhaust hood
  - school cafeteria ventilation
  - Type I hood design
  - makeup air systems
  - commercial kitchen exhaust
  - grease exhaust ventilation
  - cafeteria hood sizing
  - kitchen energy recovery
weight: 1
---

## Design Overview

Kitchen exhaust systems in school cafeterias require specialized design to capture grease-laden vapors, heat, moisture, and combustion products while maintaining acceptable indoor air quality and minimizing energy consumption. The design must accommodate variable cooking loads, extended service periods, and strict budget constraints typical of institutional applications.

## Hood Classification and Application

### Type I Hoods (Grease Extraction)

Type I hoods handle appliances producing grease-laden vapors and require UL 710 listed grease filters and fire suppression systems. School cafeteria applications include ranges, ovens, fryers, griddles, and broilers.

**Minimum exhaust flow rate:**

$$Q_{\text{hood}} = A_{\text{hood}} \times v_{\text{capture}}$$

where:
- $Q_{\text{hood}}$ = exhaust volumetric flow rate (cfm)
- $A_{\text{hood}}$ = hood face area or perimeter area (ft²)
- $v_{\text{capture}}$ = capture velocity (fpm)

IMC Section 507 specifies minimum exhaust rates based on hood type and appliance duty:

| Hood Type | Light Duty | Medium Duty | Heavy Duty |
|-----------|------------|-------------|------------|
| Wall-mounted canopy | 200 cfm/ft | 300 cfm/ft | 400 cfm/ft |
| Single island canopy | 300 cfm/ft | 400 cfm/ft | 500 cfm/ft |
| Double island canopy | 400 cfm/ft | 500 cfm/ft | 600 cfm/ft |
| Eyebrow hood | 250 cfm/ft | 350 cfm/ft | Not applicable |

*Note: Rates expressed per linear foot of hood length.*

School cafeterias typically operate with light to medium-duty appliances. A 10-foot wall-mounted canopy hood over medium-duty equipment requires:

$$Q = 10 \text{ ft} \times 300 \frac{\text{cfm}}{\text{ft}} = 3000 \text{ cfm}$$

### Type II Hoods (Heat and Moisture Removal)

Type II hoods serve appliances producing heat and moisture without grease, including steamers, pasta cookers, and dishwashers. These hoods do not require grease filters or fire suppression but must handle substantial latent loads.

**Sensible heat extraction:**

$$Q_{\text{sensible}} = \frac{q_{\text{s}}}{1.08 \times \Delta T}$$

where:
- $Q_{\text{sensible}}$ = airflow for sensible heat removal (cfm)
- $q_{\text{s}}$ = sensible heat load (Btu/hr)
- $\Delta T$ = temperature rise across hood (°F), typically 20-40°F

**Latent heat extraction:**

$$Q_{\text{latent}} = \frac{q_{\text{L}}}{4840 \times \Delta W}$$

where:
- $Q_{\text{latent}}$ = airflow for latent heat removal (cfm)
- $q_{\text{L}}$ = latent heat load (Btu/hr)
- $\Delta W$ = humidity ratio change (lb water/lb dry air)

Dishwasher exhaust typically requires 100-150 cfm per linear foot of hood length for institutional applications.

## Makeup Air Requirements

IMC Section 508 requires makeup air equal to exhaust air volume. For systems exceeding 400 cfm, at least 50% of makeup air must be mechanically supplied to the same room or space.

**Heating load for conditioned makeup air:**

$$q_{\text{heat}} = 1.08 \times Q_{\text{MUA}} \times (T_{\text{supply}} - T_{\text{outdoor}})$$

where:
- $q_{\text{heat}}$ = heating load (Btu/hr)
- $Q_{\text{MUA}}$ = makeup air quantity (cfm)
- $T_{\text{supply}}$ = desired supply temperature (°F)
- $T_{\text{outdoor}}$ = outdoor design temperature (°F)

For a 5000 cfm exhaust system with makeup air supplied at 60°F during 0°F outdoor conditions:

$$q_{\text{heat}} = 1.08 \times 5000 \times (60 - 0) = 324{,}000 \text{ Btu/hr}$$

This represents significant energy consumption, particularly in cold climates with extended heating seasons.

## Energy Recovery Strategies

ASHRAE 90.1 Section 6.5.6.1 requires energy recovery for systems with outdoor air supply exceeding specified thresholds based on climate zone and percent outdoor air. School cafeteria exhaust presents challenges for energy recovery due to grease content.

### Applicable Technologies

**Exhaust-to-makeup air heat recovery:**
- Run-around glycol loop systems: 45-65% effectiveness, suitable for grease-laden exhaust
- Separate heat exchangers prevent cross-contamination
- Preheat makeup air using exhaust energy

**Demand-controlled kitchen ventilation (DCKV):**
- Optical sensors or temperature sensors modulate hood flow based on cooking activity
- ASHRAE 90.1 allows 50% credit toward ventilation energy efficiency
- Reduces both exhaust and makeup air volumes during low-load periods
- Potential energy savings: 30-50% compared to constant-volume operation

**Transfer air from dining areas:**
- Route air from dining space to kitchen before exhaust
- Reduces outdoor makeup air quantity
- Requires careful pressure relationship management
- ASHRAE 62.1 prohibits transfer air from spaces with higher contamination

## Code and Standard Requirements

**Fire protection (IMC Section 507.2):**
- UL 300 compliant wet chemical suppression systems
- Automatic fuel shutoff upon system activation
- Manual pull stations at exit path
- Duct systems must extend to exterior, minimum 18-gauge steel

**Exhaust duct construction:**
- Continuously welded, liquid-tight construction
- Listed grease duct enclosure assemblies where penetrating fire-rated assemblies
- Minimum clearance to combustibles: 18 inches, reducible to 3 inches with specified protection

**Electrical:**
- Exhaust fan interlocked with appliance operation
- Interlocked makeup air supply prevents negative pressures upon exhaust system failure

## Practical Design Considerations

School cafeteria kitchens differ from commercial restaurant applications:

1. **Operating schedules:** Defined meal periods (breakfast, lunch) with extended idle periods
2. **Equipment diversity:** Batch cooking with lower simultaneous usage factors than continuous-service restaurants
3. **Capacity requirements:** Peak loads during 1-2 hour service windows
4. **Maintenance accessibility:** School maintenance staff capabilities vary; robust, simple systems preferred
5. **Budget constraints:** Life-cycle cost analysis favors energy-efficient designs with reasonable first costs

**Recommended hood sizing approach:**
- Apply diversity factors: 0.7-0.85 for multiple appliances under single hood
- Size makeup air systems for peak exhaust demand
- Implement variable-speed exhaust and makeup air fans
- Consider side panels or proximity hoods to reduce exhaust requirements

**Typical school cafeteria layout:**
- Wall-mounted Type I hood: serving line hot holding and limited cooking
- Type II hood: dishwasher area
- Total exhaust: 3000-6000 cfm for facilities serving 500-1000 students

Proper kitchen exhaust design in school cafeterias balances capture effectiveness, energy efficiency, code compliance, and maintainability to serve institutional needs throughout extended service life.

