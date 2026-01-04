---
title: "Airflow Measurement & Balancing for HVAC Engineers"
description: "Pitot traverse methodology, flow hood techniques, duct traverse procedures, and TAB documentation requirements for HVAC system commissioning."
keywords: ["TAB", "pitot traverse", "airflow measurement", "duct traverse", "flow hood", "system balancing"]
author: "Evgeniy Gantman"
date: 2026-01-04
weight: 20
---

# Airflow Measurement & Balancing for HVAC Engineers

Testing, Adjusting, and Balancing (TAB) verifies HVAC system delivers design airflows to all spaces. Proper measurement techniques and documentation ensure comfort, energy efficiency, and code compliance.

## Duct Traverse Methods

### Pitot Tube Traverse

**Velocity pressure measurement:**

$$v = 4005 \times \sqrt{\frac{P_v}{\rho}}$$

For standard air ($\rho = 0.075$ lb/ft³):

$$v = 4005 \times \sqrt{P_v}$$

Where:
- $v$ = velocity (FPM)
- $P_v$ = velocity pressure ("w.g.)

**Traverse procedure:**
1. Drill test holes per ASHRAE/SMACNA (equal area method)
2. Measure velocity pressure at each point
3. Calculate average velocity
4. Multiply by duct area for CFM

**Number of measurement points:**
- Round duct: 20+ points (5 × 4 grid minimum)
- Rectangular duct: Based on aspect ratio (6-64 points)

**Accuracy:** ±5% with proper technique

### Flow Hoods (Capture Hoods)

**Principle:** Captures all air from diffuser/grille

**Advantages:**
- Fast (30 seconds per measurement)
- No duct access required
- Easy for existing buildings

**Disadvantages:**
- ±15% accuracy (lower than pitot)
- Sensitive to mounting position
- Expensive ($2,000-$5,000)

**Applications:** VAV terminal verification, diffuser balancing

## Balancing Procedure

1. **Preliminary checks:**
   - Verify all dampers open
   - Check belt tensions, sheave settings
   - Measure motor amps (should be < nameplate)

2. **Proportional balancing:**
   - Measure all terminal flows
   - Calculate ratios to design
   - Adjust furthest/highest pressure drop branch first
   - Re-measure and iterate

3. **Final measurements:**
   - Document actual CFM, static pressure
   - Record damper positions
   - Photograph balancing damper settings

## Hydronic Balancing

**Flow measurement methods:**
- **Calibrated balancing valves:** Read flow directly
- **Pressure drop method:** $\Delta P$ across coil/valve correlates to flow
- **Temperature method:** $\Delta T$ and heat transfer rate infer flow

**Balance tolerance:** ±10% of design flow

## Documentation Requirements

**TAB report must include:**
- Design vs. actual CFM for all terminals
- Fan motor amps, voltage, speed
- System static pressures
- Outdoor air measurements
- Damper positions
- Deficiency list

**Standards:**
- ASHRAE Standard 111: Practices for Measurement, Testing, Adjusting, and Balancing
- AABC National Standards
- NEBB Procedural Standards

## Common TAB Issues

- **Low airflow:** Dirty filters, closed dampers, incorrect sheaves
- **Noisy terminals:** Excessive velocity (>2,000 FPM)
- **Unbalanced zones:** Duct leakage, undersized branch dampers
- **Low system airflow:** Undersized ductwork, excessive fittings

## Practical Applications

1. **New construction:** Full TAB per contract documents
2. **Renovation:** Verify affected zones only
3. **Troubleshooting:** Selective measurements to diagnose complaints
4. **Commissioning:** TAB is critical component of Cx process

---

**Related Technical Guides:**
- [Duct Static Pressure Calculations](/technical-guides/duct-static-pressure-calculations/)
- [Fan Selection & Performance](/technical-guides/fan-selection-performance/)
- [Commissioning Procedures](/technical-guides/commissioning-procedures/)

**References:**
- ASHRAE Standard 111: Practices for Measurement, Testing, Adjusting, and Balancing of Building HVAC Systems
- SMACNA HVAC Systems Testing, Adjusting and Balancing, 3rd Edition
