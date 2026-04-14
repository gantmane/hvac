---
title: "Filter Efficiency Ratings"
aliases: ["Filter Efficiency Ratings"]
description: "Understanding MERV, HEPA, ULPA, and ISO 16890 filter efficiency ratings for HVAC air filtration system selection and specification."
keywords: ["MERV rating", "HEPA filter", "ULPA filter", "ISO 16890", "filter efficiency", "air filtration", "ASHRAE 52.2"]
tags: ["MERV rating", "HEPA filter", "ULPA filter", "ISO 16890", "filter efficiency", "air filtration", "ASHRAE 52.2"]
weight: 1
---

Filter efficiency ratings provide standardized methods for comparing air filter performance across manufacturers and applications. Understanding these rating systems is essential for proper filter selection in HVAC systems.

## MERV Rating System (ASHRAE 52.2)

The Minimum Efficiency Reporting Value (MERV) rating, established by ASHRAE Standard 52.2, provides a standardized method for rating air filter efficiency based on particle size removal capabilities.

### MERV Rating Categories

| MERV | E1 (0.3-1.0 μm) | E2 (1.0-3.0 μm) | E3 (3.0-10 μm) | Typical Applications |
|------|-----------------|-----------------|----------------|---------------------|
| 1-4  | N/A | N/A | <20% to 80% | Residential, light commercial |
| 5-8  | N/A | <20% to 70% | 80-90% | Commercial buildings |
| 9-12 | N/A | 50-90% | 90-95% | Superior commercial |
| 13-16| 75-95% | 90-99% | >95% | Hospital, cleanroom |

### Test Methodology

ASHRAE 52.2 testing involves:

1. **Particle Size Ranges**: KCl aerosol particles in three size ranges
2. **Loading Test**: Filter loaded with ASHRAE test dust
3. **Minimum Efficiency**: Lowest efficiency during loading cycle determines MERV

The test procedure ensures MERV ratings reflect sustained performance throughout filter service life, not just initial efficiency.

## HEPA and ULPA Classifications

High-Efficiency Particulate Air (HEPA) and Ultra-Low Penetration Air (ULPA) filters represent the highest efficiency categories for particulate filtration.

### HEPA Standards

**US Standard (IEST-RP-CC001)**:
- HEPA: ≥99.97% efficiency at 0.3 μm MPPS
- Tested with DOP or PAO aerosol at rated flow

**European Standard (EN 1822)**:
- H13: ≥99.95% @ MPPS
- H14: ≥99.995% @ MPPS
- U15: ≥99.9995% @ MPPS
- U16: ≥99.99995% @ MPPS

### MPPS Testing

Modern HEPA testing focuses on the Most Penetrating Particle Size (MPPS), typically 0.1-0.2 μm, where combined filtration mechanisms exhibit minimum efficiency:

$$\eta_{total} = 1 - (1-\eta_{diffusion})(1-\eta_{interception})(1-\eta_{impaction})$$

## ISO 16890 Global Standard

ISO 16890 replaced EN 779 and provides globally harmonized filter ratings based on health-relevant particle sizes corresponding to PM standards.

### Classification Groups

| Group | Particle Size | Health Relevance | Minimum Efficiency |
|-------|---------------|------------------|-------------------|
| ePM1 | ≤1 μm | Deep lung penetration | ≥50% required |
| ePM2.5 | ≤2.5 μm | Lower respiratory | ≥50% required |
| ePM10 | ≤10 μm | Upper respiratory | ≥50% required |
| Coarse | >10 μm | Nasal passages | <50% ePM10 |

### Discharge Conditioning

ISO 16890 requires electrostatic discharge conditioning using isopropyl alcohol (IPA) treatment to neutralize electret charges and reveal mechanical efficiency only. This prevents overrating of electrostatically enhanced filters that lose charge over time.

## Efficiency-Pressure Drop Relationship

Filter efficiency must be balanced against system pressure drop and energy consumption:

$$Figure\ of\ Merit = \frac{-\ln(1-\eta)}{\Delta P}$$

Higher FOM values indicate better efficiency per unit pressure drop. Modern filter media development focuses on improving this relationship through:

- Nanofiber coatings
- Gradient density structures
- Optimized fiber diameter distributions
- Enhanced electret treatments

## Application-Specific Requirements

### Commercial Buildings (ASHRAE 62.1)

- Minimum MERV 8 for outdoor air filtration
- MERV 13 recommended for improved IAQ
- Consider MERV 14-16 for high-occupancy spaces

### Healthcare (ASHRAE 170)

- MERV 14 minimum for general areas
- HEPA (MERV 17-20) for protective environments
- Two-stage filtration with prefilters

### Cleanrooms (ISO 14644)

- HEPA or ULPA terminal filtration
- Efficiency verified by in-situ leak testing
- Classification-specific particle count limits

Understanding filter efficiency ratings enables informed selection decisions that balance air quality objectives, energy efficiency, and operational costs across diverse HVAC applications.