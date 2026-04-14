---
title: "Filter Ratings and Efficiency Classification Systems"
aliases: ["Filter Ratings and Efficiency Classification Systems"]
description: "Comprehensive guide to MERV, ISO 16890, HEPA, and ULPA filter ratings with efficiency calculations, particle size performance, and selection criteria."
date: 2026-01-05
keywords: ["MERV ratings", "ISO 16890", "HEPA filters", "filter efficiency", "particle filtration", "ASHRAE 52.2", "ULPA filters", "air filter classification"]
tags: ["MERV ratings", "ISO 16890", "HEPA filters", "filter efficiency", "particle filtration", "ASHRAE 52.2", "ULPA filters", "air filter classification"]
weight: 2
---

Air filter ratings provide standardized metrics for comparing particulate removal efficiency across different filter types and manufacturers. Understanding these classification systems is essential for proper filter selection, indoor air quality management, and regulatory compliance.

## ASHRAE Standard 52.2 and MERV Ratings

**Minimum Efficiency Reporting Value (MERV)** is the primary rating system used in North America, defined by ASHRAE Standard 52.2-2017. MERV ratings range from 1 to 16, with higher values indicating greater particle capture efficiency.

### MERV Classification Table

| MERV Rating | Particle Size Range | Typical Applications | Minimum Efficiency |
|-------------|---------------------|----------------------|-------------------|
| MERV 1-4 | >10 μm | Residential furnaces, basic protection | <20% @ 3-10 μm |
| MERV 5-8 | 3-10 μm | Commercial buildings, better residential | 20-70% @ 3-10 μm |
| MERV 9-12 | 1-3 μm | Hospital non-surgical, superior commercial | 40-90% @ 1-3 μm |
| MERV 13-16 | 0.3-1 μm | Hospital surgical, clean rooms, smoke removal | >75% @ 0.3-1 μm |

The MERV test procedure measures efficiency at three particle size ranges using potassium chloride (KCl) aerosol:

- **Range 1:** 0.3-1.0 μm (E1)
- **Range 2:** 1.0-3.0 μm (E2)
- **Range 3:** 3.0-10.0 μm (E3)

Composite minimum efficiency is calculated for each range, and the MERV rating is assigned based on the worst-performing size range.

### MERV Efficiency Formula

The average particle size efficiency for each size range is:

$$E_i = \frac{C_{upstream,i} - C_{downstream,i}}{C_{upstream,i}} \times 100\%$$

Where:
- $E_i$ = Efficiency for particle size range $i$ (%)
- $C_{upstream,i}$ = Upstream particle concentration (particles/ft³)
- $C_{downstream,i}$ = Downstream particle concentration (particles/ft³)

The composite minimum efficiency is the lowest efficiency value recorded during the loading cycle for each particle size range.

## ISO 16890 International Standard

ISO 16890 represents a more recent, globally harmonized filter testing standard that classifies filters based on their ability to remove particulate matter sizes relevant to outdoor air quality and human health.

### ISO 16890 Group Classification

| ISO Group | Particle Size | Minimum Efficiency | Health Relevance |
|-----------|---------------|-------------------|------------------|
| ISO Coarse | >10 μm (PM₁₀) | ≥50% | Pollen, coarse dust |
| ISO ePM₁₀ | PM₁₀ | 50-99% | Respirable particles |
| ISO ePM₂.₅ | PM₂.₅ | 50-99% | Fine combustion particles |
| ISO ePM₁ | PM₁ | 50-99% | Ultrafine particles, smoke |

The ISO standard tests filters using DEHS (diethylhexyl sebacate) aerosol with optical particle counters measuring efficiency at particle sizes from 0.3 to 10 μm. Filters are also subjected to electrostatic discharge conditioning to evaluate performance after static charge dissipation.

### ISO to MERV Approximate Correlation

| MERV | ISO Equivalent | Notes |
|------|----------------|-------|
| MERV 7-8 | ISO Coarse | Limited PM₂.₅ removal |
| MERV 9-11 | ISO ePM₁₀ 50-80% | Moderate fine particle capture |
| MERV 12-13 | ISO ePM₂.₅ 50-70% | Good PM₂.₅ removal |
| MERV 14-16 | ISO ePM₁ 70-95% | Excellent ultrafine particle removal |

Direct correlation between MERV and ISO ratings is approximate due to different test methodologies, particle size emphasis, and conditioning procedures.

## HEPA and ULPA Filtration

**High-Efficiency Particulate Air (HEPA)** and **Ultra-Low Penetration Air (ULPA)** filters provide the highest levels of particulate removal, tested per MIL-STD-282 or EN 1822 standards.

### HEPA/ULPA Classification

| Filter Type | Minimum Efficiency | Test Particle Size | Applications |
|-------------|-------------------|-------------------|--------------|
| HEPA (Type A-E) | 99.97% | 0.3 μm MPPS | Cleanrooms, hospitals, laboratories |
| HEPA (Medical) | 99.99% | 0.3 μm | Isolation rooms, pharmaceutical |
| ULPA (U15) | 99.9995% | 0.12 μm MPPS | Semiconductor manufacturing |
| ULPA (U16-17) | 99.99995%-99.999995% | 0.12 μm MPPS | Critical research applications |

**Most Penetrating Particle Size (MPPS)** is the particle diameter at which filter efficiency is lowest, typically 0.1-0.3 μm depending on filter media characteristics. HEPA efficiency is rated at MPPS to ensure performance across all particle sizes.

### Penetration and Efficiency Relationship

Filter penetration $P$ relates to efficiency $E$ by:

$$P = 1 - E = \frac{C_{downstream}}{C_{upstream}}$$

For HEPA filters with 99.97% efficiency:

$$P = 1 - 0.9997 = 0.0003 = 0.03\%$$

This means only 3 particles per 10,000 penetrate the filter at MPPS.

## Fractional Efficiency Curves

Filter performance varies with particle size. The fractional efficiency curve describes efficiency as a function of particle diameter:

$$E(d_p) = 1 - \exp\left(-\frac{Z \cdot \eta(d_p) \cdot A}{Q}\right)$$

Where:
- $d_p$ = Particle diameter (μm)
- $Z$ = Filter media thickness (m)
- $\eta(d_p)$ = Single-fiber efficiency (dimensionless)
- $A$ = Filter face area (m²)
- $Q$ = Volumetric flow rate (m³/s)

Single-fiber efficiency combines three capture mechanisms:

$$\eta(d_p) = \eta_{diffusion} + \eta_{interception} + \eta_{inertial}$$

For particles <0.1 μm, Brownian diffusion dominates. For particles >1 μm, inertial impaction becomes significant. The minimum efficiency occurs where neither mechanism is dominant (MPPS).

## Filter Selection Guidelines

**Application-Based Selection:**

1. **Residential HVAC:** MERV 8-13 balances particle removal with acceptable pressure drop and energy consumption
2. **Commercial Office:** MERV 13-14 provides superior indoor air quality with manageable operating costs
3. **Healthcare Non-Surgical:** MERV 14 minimum per ASHRAE Standard 170
4. **Operating Rooms:** MERV 17 (HEPA) required for Class I/II spaces
5. **Cleanrooms:** ISO Class specific; Class 5 typically requires ULPA final filtration
6. **Laboratory Exhaust:** HEPA required for biological safety cabinets and fume hoods handling hazardous materials

**Performance Considerations:**

- Higher MERV ratings increase pressure drop (typically 2-4× from MERV 8 to MERV 13)
- Energy consumption rises with increased static pressure
- Dust holding capacity generally decreases with higher MERV ratings
- More frequent filter replacement may be required for MERV 13+

**System Compatibility:**

Verify that existing air handling equipment can accommodate higher efficiency filters by checking:
- Available static pressure budget (system fan curve)
- Filter frame and track depth requirements
- Maximum allowable final pressure drop before filter change
- Bypass and seal integrity to prevent leakage

Proper filter selection requires balancing indoor air quality objectives, energy efficiency, maintenance requirements, and equipment capabilities while meeting applicable codes and standards.

## Regulatory and Code Requirements

ASHRAE Standard 62.1 establishes minimum outdoor air ventilation rates but does not mandate specific MERV ratings. However, ASHRAE Standard 170 (healthcare), IMC (International Mechanical Code), and local jurisdictions may specify minimum filtration levels for particular occupancies.

The choice between MERV and ISO 16890 rating systems depends on geographic location, industry practice, and client requirements. In North America, MERV remains dominant, while ISO 16890 sees increasing adoption in Europe and international projects.
