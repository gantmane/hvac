---
title: "Water-Cooled Condensers"
weight: 2
description: "Technical overview of water-cooled condenser design, shell-and-tube construction, tube materials, fouling factors, approach temperatures, and efficiency advantages in refrigeration systems."
keywords: ["water-cooled condenser", "shell-and-tube condenser", "condenser tubes", "fouling factor", "approach temperature", "water treatment", "marine condenser", "refrigeration efficiency"]
---

Water-cooled condensers reject heat from refrigerant vapor to cooling water, offering superior efficiency compared to air-cooled designs through enhanced heat transfer coefficients and lower condensing temperatures.

## Shell-and-Tube Construction

Shell-and-tube condensers represent the dominant design for water-cooled applications in medium to large refrigeration systems. The refrigerant flows on the shell side while cooling water passes through the tubes, allowing for effective heat transfer and ease of maintenance.

**Basic Configuration:**
- Refrigerant enters at the top, condenses on tube surfaces, and drains from the bottom
- Water flows through tubes in counterflow or parallel flow arrangement
- Shell diameters range from 8 to 60 inches depending on capacity
- Tube lengths typically 8 to 20 feet for commercial applications

**Tube Arrangements:**
- Fixed tube sheet design: tubes welded to stationary tube sheets at both ends
- Removable bundle design: tube bundle can be extracted for cleaning and inspection
- Straight tube configuration: standard for most applications, allows mechanical cleaning
- U-tube design: eliminates one tube sheet, accommodates thermal expansion

**Pass Configuration:**
- Single-pass: water flows through condenser once, lowest water pressure drop
- Multi-pass: water makes multiple passes through tube bundle, higher heat transfer coefficient
- Two-pass and four-pass configurations most common for balanced performance
- Pass selection based on available water flow rate and required approach temperature

## Tube Materials and Selection Criteria

Tube material selection balances thermal conductivity, corrosion resistance, cost, and water quality considerations.

**Copper Tubes:**
- Standard material for most commercial refrigeration condensers
- Thermal conductivity: 385 W/m·K at 20°C
- Excellent heat transfer performance and moderate cost
- Wall thickness typically 0.028 to 0.049 inches for standard pressure applications
- Susceptible to erosion-corrosion at water velocities exceeding 8 ft/s
- Limited use with seawater or aggressive water chemistry

**Cupronickel Alloys:**
- 90/10 cupronickel (90% copper, 10% nickel): moderate corrosion resistance
- 70/30 cupronickel: superior resistance to seawater and brackish water
- Thermal conductivity: 50 W/m·K (90/10) to 29 W/m·K (70/30)
- Standard material for marine and coastal applications
- Maximum water velocity: 10 ft/s for 90/10, 12 ft/s for 70/30
- Cost approximately 3 to 5 times copper depending on nickel content

**Titanium Tubes:**
- Exceptional corrosion resistance in seawater, brackish water, and chlorinated water
- Thermal conductivity: 16 W/m·K, requires thin walls (0.020 to 0.028 inches) to compensate
- Immune to chloride-induced stress corrosion cracking
- Allows water velocities up to 15 ft/s without erosion concerns
- Premium cost, typically 8 to 12 times copper
- Preferred for critical applications and aggressive water conditions

**Stainless Steel:**
- Type 316L stainless most common for condenser tubes
- Thermal conductivity: 16 W/m·K, similar to titanium
- Good corrosion resistance but susceptible to pitting in stagnant chloride-containing water
- Intermediate cost between cupronickel and titanium
- Requires minimum water velocity to prevent stagnation

## Enhanced Tube Technology

Tube enhancement increases inside or outside heat transfer coefficients through surface modifications, reducing required condenser size and improving efficiency.

**Microfin Tubes:**
- Internal helical fins or grooves increase refrigerant-side heat transfer
- Fin height typically 0.008 to 0.012 inches with 50 to 70 fins per circumference
- Refrigerant-side coefficient improvement: 100% to 200% compared to smooth tubes
- Particularly effective with zeotropic refrigerant mixtures
- Increases refrigerant pressure drop 20% to 40%

**External Enhancement:**
- Integral low-fin tubing: fins formed directly on tube exterior
- Fin density: 19, 26, or 40 fins per inch depending on application
- Water-side coefficient improvement: 50% to 100%
- More susceptible to fouling than smooth tubes, requires good water quality

**Selection Considerations:**
- Enhanced tubes reduce condenser size by 30% to 50% for same capacity
- Cost premium: 15% to 30% compared to smooth tubes
- Fouling characteristics must be evaluated for specific water quality
- Cleaning difficulty increases with enhancement complexity

## Fouling Factors and Heat Transfer

Fouling resistance accounts for thermal resistance from scale, biological growth, and sediment accumulation on tube surfaces, degrading performance over time.

**Fouling Factor Selection:**

| Water Source | Fouling Factor (hr·ft²·°F/BTU) |
|--------------|--------------------------------|
| Cooling tower water (treated) | 0.0005 - 0.001 |
| Once-through river water | 0.001 - 0.003 |
| Seawater | 0.0005 - 0.001 |
| Brackish water | 0.002 - 0.003 |
| Untreated cooling tower | 0.003 - 0.005 |

**Overall Heat Transfer Coefficient:**

The overall coefficient (U) accounts for refrigerant-side, tube wall, and water-side resistances:

1/U = 1/h_r + R_f,r + t/(k·A_m/A_o) + R_f,w + 1/h_w

Where:
- h_r: refrigerant-side coefficient (typically 800-1200 BTU/hr·ft²·°F)
- h_w: water-side coefficient (typically 500-1500 BTU/hr·ft²·°F)
- R_f: fouling factors for refrigerant and water sides
- t: tube wall thickness
- k: tube thermal conductivity

Clean overall coefficients range from 250 to 400 BTU/hr·ft²·°F depending on configuration and materials.

## Approach Temperature Design

Approach temperature, defined as the difference between condensing temperature and leaving water temperature, directly impacts system efficiency and condenser size.

**Design Considerations:**
- Typical approach temperatures: 5°F to 15°F for commercial applications
- Tighter approach (lower value) reduces condensing temperature and compressor power
- Requires larger condenser surface area and higher initial cost
- Economic optimum balances first cost against operating cost savings

**Temperature Relationships:**

For counterflow arrangement:
- Condensing temperature = Leaving water temperature + Approach temperature
- Log mean temperature difference (LMTD) accounts for temperature change through condenser
- LMTD = (ΔT_1 - ΔT_2) / ln(ΔT_1/ΔT_2)
- ΔT_1: temperature difference at refrigerant inlet
- ΔT_2: temperature difference at refrigerant outlet

**Water Temperature Rise:**
- Typical range: 8°F to 15°F across condenser
- Determined by: ΔT_water = Q / (m_water × c_p)
- Higher rise reduces required water flow rate
- Limited by approach temperature and available water supply temperature

## Water Treatment Requirements

Proper water treatment prevents scale formation, corrosion, and biological fouling that degrade condenser performance and shorten equipment life.

**Scale Control:**
- Calcium carbonate scale forms when water exceeds saturation limits
- Langelier Saturation Index (LSI) predicts scaling tendency
- Target LSI: -0.5 to +0.5 for stable water chemistry
- Chemical treatment: phosphonates, polymers inhibit scale formation
- Acid feed reduces alkalinity and calcium carbonate precipitation

**Corrosion Control:**
- Maintain pH between 7.5 and 9.0 for most tube materials
- Chromate-based inhibitors (legacy systems, environmental concerns)
- Molybdate and phosphate-based non-chromate inhibitors
- Corrosion rates: target <2 mils per year for copper alloys
- Cathodic protection for critical installations

**Biological Control:**
- Biocides prevent algae, bacteria, and biofilm formation
- Oxidizing biocides: chlorine, bromine (0.5-1.0 ppm residual)
- Non-oxidizing biocides: quaternary ammonium compounds, isothiazolones
- Dosing frequency: continuous or slug feed depending on system
- Legionella control critical in cooling tower systems

**Monitoring Parameters:**
- pH: daily measurement and automatic control
- Conductivity: indicates dissolved solids concentration
- Cycles of concentration: ratio of cooling tower water to makeup water
- Corrosion coupons: periodic analysis of corrosion rates
- Biological dip slides: monitor biological activity

## Marine and Coastal Applications

Marine condensers handle seawater or brackish water cooling, requiring specialized materials and design considerations for corrosive environments.

**Design Requirements:**
- Tube material: cupronickel or titanium for corrosion resistance
- Water velocity: 6 to 10 ft/s to prevent marine growth attachment
- Sacrificial anodes: aluminum or zinc protect against galvanic corrosion
- Impressed current cathodic protection for large installations
- Tube inlet screens and strainers remove debris and marine organisms

**Seawater Chemistry:**
- Salinity: 3.0% to 3.5% for open ocean, variable for coastal/brackish
- High chloride content: 19,000 ppm aggressive to most metals
- Dissolved oxygen: 5-8 ppm accelerates corrosion
- Temperature: varies seasonally, affects condensing efficiency
- pH: typically 8.0 to 8.3, relatively stable

**Operational Considerations:**
- Seasonal water temperature variation impacts capacity and efficiency
- Marine growth prevention through velocity, chlorination, or mechanical cleaning
- Once-through cooling eliminates cooling tower but requires larger water volumes
- Regulatory compliance: thermal discharge and chlorination limits
- Backup systems critical for continuous operation

## Efficiency Advantages Over Air-Cooled

Water-cooled condensers deliver superior efficiency compared to air-cooled designs through fundamental heat transfer and thermodynamic advantages.

**Heat Transfer Comparison:**

| Parameter | Water-Cooled | Air-Cooled |
|-----------|--------------|------------|
| Overall U-value | 250-400 BTU/hr·ft²·°F | 15-25 BTU/hr·ft²·°F |
| Condensing temp (95°F ambient) | 95-105°F | 115-130°F |
| Approach to cooling medium | 5-15°F | 15-25°F |
| Fan/pump power | 2-4% of cooling | 5-8% of cooling |

**Efficiency Impact:**
- Lower condensing temperature reduces compressor power consumption
- Energy savings: 20% to 35% compared to air-cooled at design conditions
- Savings increase at higher ambient temperatures
- Part-load efficiency maintained with cooling tower or water supply temperature reduction

**Application Selection:**
- Water-cooled preferred where water availability and cost permit
- Air-cooled selected where water is scarce, expensive, or regulated
- Hybrid systems combine water-cooled base capacity with air-cooled supplemental
- Life-cycle cost analysis must include water treatment, makeup water, and maintenance costs
