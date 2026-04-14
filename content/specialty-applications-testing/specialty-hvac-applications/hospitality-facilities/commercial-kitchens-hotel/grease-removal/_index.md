---
title: "Grease Removal Systems for Hotel Kitchen Exhaust"
aliases: ["Grease Removal Systems for Hotel Kitchen Exhaust"]
description: "Engineering analysis of baffle filters, UV and ESP systems, grease duct cleaning protocols, NFPA 96 compliance, rooftop discharge design, and maintenance schedules."
keywords: ["grease removal", "baffle filters", "UV systems", "ESP grease extractors", "NFPA 96", "grease duct cleaning", "kitchen exhaust", "hotel kitchens"]
tags: ["grease removal", "baffle filters", "UV systems", "ESP grease extractors", "NFPA 96", "grease duct cleaning", "kitchen exhaust", "hotel kitchens"]
date: 2026-01-11
draft: false
weight: 3
---

Grease removal systems in hotel commercial kitchens represent a critical safety and operational component that must effectively capture airborne grease particles before they enter exhaust ductwork. The primary function is preventing grease accumulation in ducts, which poses substantial fire hazards and requires robust engineering solutions combining mechanical filtration, electronic precipitation, and ultraviolet oxidation technologies.

## Baffle Filter Design and Efficiency

Baffle filters constitute the first line of defense in grease-laden vapor removal, utilizing a series of vertical or horizontal baffles that force air through directional changes. The inertial separation principle governs their operation—grease particles, having greater mass than air molecules, cannot follow the abrupt changes in airflow direction and impinge on baffle surfaces where they coalesce and drain into collection troughs.

Standard baffle filter efficiency typically ranges from 60-85% for particles larger than 10 micrometers. The capture efficiency can be expressed as:

$$\eta = 1 - e^{-\frac{9\mu L v}{2\rho_p d_p^2 V}}$$

Where $\eta$ is capture efficiency, $\mu$ is air dynamic viscosity, $L$ is baffle length, $v$ is baffle spacing, $\rho_p$ is particle density, $d_p$ is particle diameter, and $V$ is air velocity through the filter.

Multi-stage baffle configurations achieve higher efficiencies by increasing the number of directional changes. Optimal baffle spacing ranges from 12-25 mm (0.5-1.0 inches), with face velocities between 200-400 fpm. Lower velocities reduce pressure drop but decrease separation efficiency, while excessive velocities can cause grease re-entrainment.

Filter material selection significantly impacts performance and longevity. Stainless steel 304 or 316 provides corrosion resistance against acidic condensate, while stamped or formed construction allows drainage without horizontal surfaces where grease can pool.

## UV and ESP Grease Removal Systems

Ultraviolet (UV) grease removal systems employ high-intensity UV-C lamps (typically 254 nm wavelength) to break down grease molecules through photolysis, converting them to carbon dioxide and water vapor. These systems install downstream of baffle filters, treating residual grease particles that escape mechanical separation. UV intensity of 30-50 mW/cm² at the duct centerline provides effective treatment, with residence time requirements of 0.25-0.5 seconds.

Electrostatic precipitator (ESP) systems apply an ionizing voltage (typically 8,000-12,000 VDC) to charge grease particles, which then migrate to grounded collection plates under the influence of the electric field. Collection efficiency follows the Deutsch equation:

$$\eta = 1 - e^{-\frac{w A}{Q}}$$

Where $w$ is particle migration velocity (0.1-0.3 m/s for grease), $A$ is collection plate area, and $Q$ is volumetric airflow rate.

ESP systems achieve 85-95% removal efficiency for submicron particles that pass through baffle filters. Power consumption ranges from 0.15-0.30 kW per 1,000 CFM, with collection plates requiring cleaning every 1-4 weeks depending on cooking volume and grease load.

{{< mermaid >}}
graph TB
    A[Cooking Appliance] -->|Grease-laden vapor| B[Exhaust Hood]
    B --> C[Baffle Filters<br/>60-85% efficiency]
    C --> D{Secondary Treatment}
    D -->|Option 1| E[UV System<br/>30-50 mW/cm²]
    D -->|Option 2| F[ESP System<br/>8-12 kVDC]
    D -->|Option 3| G[Direct to Duct]
    E --> H[Exhaust Duct]
    F --> H
    G --> H
    H --> I[Exhaust Fan]
    I --> J[Rooftop Discharge]
    J --> K[Atmospheric Release]

    C -.-> L[Grease Collection]
    E -.-> M[UV Lamp Maintenance]
    F -.-> N[Plate Cleaning]
    H -.-> O[Duct Cleaning Schedule]

    style C fill:#e1f5ff
    style E fill:#fff4e1
    style F fill:#ffe1f5
    style L fill:#ff9999
    style M fill:#ffcc99
    style N fill:#ffcc99
    style O fill:#ff9999
{{< /mermaid >}}

## Grease Duct Cleaning Requirements

NFPA 96 mandates cleaning frequency based on system inspection revealing grease accumulation. The standard requires cleaning when grease deposits exceed 1.6 mm (1/16 inch) thickness anywhere in the exhaust system. Inspection intervals depend on cooking volume and food type:

| Cooking Type | Inspection Frequency | Typical Cleaning Frequency |
|--------------|---------------------|---------------------------|
| Solid fuel cooking | Monthly | Monthly |
| High-volume operations (24-hour) | Quarterly | Quarterly |
| Moderate-volume operations | Semi-annually | Semi-annually |
| Low-volume operations (churches, seasonal) | Annually | Annually |

Professional cleaning must employ methods that remove grease from all internal duct surfaces, including horizontal runs, vertical rises, and transition sections. Hand scraping, steam cleaning, or chemical treatment provides acceptable cleaning, with post-cleaning certification required documenting the extent of cleaning and residual grease conditions.

Access panels at 6-meter (20-foot) maximum intervals facilitate inspection and cleaning. Welded duct construction eliminates fasteners and gaps where grease can accumulate and create ignition points.

## NFPA 96 Compliance for Grease Ducts

NFPA 96 establishes comprehensive requirements for grease duct design, installation, and maintenance. Critical specifications include:

**Material and Construction**: Ducts must be 16-gauge (1.5 mm) carbon steel or 18-gauge (1.2 mm) stainless steel minimum, with all seams continuously welded on both sides. Spiral-wound or lock-seam ducts are prohibited due to grease trapping in seams.

**Clearances**: Minimum 450 mm (18 inches) clearance from combustible construction, or reduced to 75 mm (3 inches) with listed clearance systems incorporating ventilated airspace or insulation barriers.

**Slope and Drainage**: Horizontal duct runs require minimum 2% slope (1/4 inch per foot) toward the hood or collection point to prevent grease pooling. Drainage provisions at low points prevent liquid accumulation.

**Fire Suppression Integration**: Automatic fire suppression system activation must simultaneously shut down fuel and power to cooking appliances, activate exhaust fan (where code permits), and discharge suppression agent throughout the hood, plenum, and duct system.

## Rooftop Discharge Considerations

Rooftop exhaust termination requires careful design addressing both safety and operational concerns. Discharge velocity must achieve 1,500-2,500 fpm to provide adequate plume rise and prevent grease deposition on roof surfaces. The effective stack height follows:

$$H_e = H_s + \frac{V_s^2 - V_a^2}{2g}$$

Where $H_e$ is effective height, $H_s$ is physical stack height, $V_s$ is stack velocity, $V_a$ is ambient wind velocity, and $g$ is gravitational acceleration (9.81 m/s²).

Minimum 3-meter (10-foot) distance from air intakes, property lines, and operable openings prevents re-entrainment and neighbor complaints. Hinged or removable fan assemblies facilitate duct cleaning access at the discharge point, where grease accumulation concentrates due to temperature drop and velocity reduction.

Weather protection requires upblast or straight discharge configurations rather than horizontal discharge, which allows rain infiltration. Listed grease duct enclosures protect roof penetrations and provide required clearances to combustible roof construction.

## Maintenance and Cleaning Schedules

Comprehensive maintenance programs address all system components with frequency determined by actual operating conditions:

**Baffle Filters**: Daily removal and dishwasher cleaning (minimum 71°C/160°F), or soak tank cleaning with alkaline detergent. Quarterly inspection for damage, warping, or deteriorated drain channels.

**UV Systems**: Monthly lamp cleaning to remove grease film reducing UV transmission, with lamp replacement at manufacturer intervals (typically 10,000-15,000 hours). Quarterly UV intensity measurement verifying minimum 30 mW/cm² output.

**ESP Systems**: Weekly to monthly plate cleaning depending on grease load, using hot water (minimum 71°C/160°F) or automatic wash-in-place systems. Quarterly high-voltage power supply testing and ionizer wire inspection.

**Exhaust Fans**: Monthly belt tension and bearing lubrication, quarterly belt replacement, annual motor testing and vibration analysis. Grease accumulation on fan blades requires cleaning when deposits exceed 3 mm (1/8 inch).

## Technology Comparison

| Technology | Capture Efficiency | Pressure Drop | Maintenance Frequency | Capital Cost | Operating Cost |
|------------|-------------------|---------------|----------------------|--------------|----------------|
| Baffle Filters | 60-85% | 0.4-0.8 in. w.g. | Daily cleaning | Low | Low |
| UV Systems | 90-95% (residual) | 0.1-0.2 in. w.g. | Monthly lamps | Medium | Medium |
| ESP Systems | 85-95% | 0.2-0.4 in. w.g. | Weekly/monthly plates | High | Medium-High |
| Baffle + UV | 95-98% (combined) | 0.5-1.0 in. w.g. | Daily + monthly | Medium | Medium |
| Baffle + ESP | 95-98% (combined) | 0.6-1.2 in. w.g. | Daily + weekly | High | Medium-High |

The selection of grease removal technology depends on cooking volume, menu profile, available maintenance resources, and local code requirements. Hotel kitchens with high-volume frying operations benefit from multi-stage systems combining mechanical filtration with electronic enhancement, while lower-volume operations may achieve adequate performance with properly maintained baffle filters and rigorous duct cleaning schedules.

Proper system design, installation, and maintenance prevents fire hazards, extends equipment life, reduces energy consumption through lower pressure drop accumulation, and ensures compliance with fire and building codes protecting occupants and property.