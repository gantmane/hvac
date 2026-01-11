---
title: "VTT Model"
description: "Finnish VTT mold growth model for predicting mold risk in building assemblies based on time-of-wetness method, mold index calculations, sensitivity classes, and critical thresholds per ASHRAE 160 implementation."
weight: 1
---

The VTT (Technical Research Centre of Finland) mold growth model represents the most widely adopted empirical approach for predicting mold growth risk in building envelope assemblies. Developed through extensive laboratory testing and field validation, the VTT model quantifies mold risk using a dimensionless mold index scale that corresponds to observable growth stages.

## Finnish VTT Model

The VTT model emerged from research conducted by Hannu Viitanen and colleagues at VTT Building Technology in the 1990s. The model derives from controlled growth chamber experiments exposing common building materials (pine sapwood, plywood, concrete, glass wool) to various temperature and relative humidity combinations for extended periods. Researchers documented mold growth progression photographically and developed mathematical relationships between environmental conditions, exposure duration, and growth extent.

The model's empirical foundation provides advantages over theoretical approaches. Laboratory-derived coefficients reflect actual mold growth behavior on building materials under realistic conditions. The model accounts for material-specific susceptibility through sensitivity class parameters, recognizing that gypsum board paper facing supports more rapid growth than painted surfaces or inorganic materials.

Mathematical implementation employs differential equations describing mold index change rate as function of temperature, relative humidity, material properties, and current mold index. The equations capture key biological phenomena including germination delay periods, accelerated growth under favorable conditions, and growth cessation under unfavorable conditions.

## Time Of Wetness Method

The time-of-wetness approach underlies VTT model calculations, accumulating exposure time when surface relative humidity exceeds critical thresholds. Unlike instantaneous evaluation methods that assess conditions at single time points, time-of-wetness integrates conditions over extended periods, capturing the cumulative nature of biological growth processes.

Critical relative humidity thresholds depend on temperature and material sensitivity. For sensitive materials (paper-faced gypsum board) at 20°C, critical RH equals approximately 80%. For less sensitive materials (treated wood, concrete) at the same temperature, critical RH increases to 85-95%. These thresholds represent conditions below which mold growth essentially ceases.

Temperature modifies critical RH thresholds and growth rates. Optimal growth occurs at 25-30°C with critical RH around 80%. At 5°C, critical RH increases to approximately 90%, and growth rates decrease by factor of 10. At 40°C, growth rates similarly decrease despite lower critical RH, as temperatures approach the upper tolerance limit for most mold species.

The model tracks accumulated exposure under growth-favorable conditions, incrementing a time-weighted exposure parameter. When conditions become unfavorable (RH drops below critical threshold or temperature falls outside viable range), growth ceases but accumulated growth remains. Mold does not "reverse" or decrease unless conditions become extremely dry for extended periods (below 60% RH for weeks), representing spore viability loss and growth degradation.

## Mold Index Calculation

The mold index (MI) provides quantitative measure of growth extent on a 0-6 scale corresponding to visually observable growth stages:

- MI = 0: No growth
- MI = 1: Initial stages, microscopic mold growth (not visible)
- MI = 2: Moderate mold growth (spores and hyphae visible under microscope, <10% coverage)
- MI = 3: Some mold growth on surface (visual detection, 10-30% coverage)
- MI = 4: Visual mold coverage >10-30% distributed coverage
- MI = 5: Plenty of mold growth on surface (50-100% coverage)
- MI = 6: Very heavy and tight mold growth, coverage 100%

Mold index increases follow S-curve progression: slow initial increase during germination (MI 0-1), rapid increase during exponential growth (MI 1-4), and asymptotic approach to maximum (MI 5-6). Growth rate depends on environmental conditions, with favorable conditions (high RH, moderate temperature) producing rapid MI increase.

The differential equation describing MI increase takes the form:

dM/dt = k₁ × k₂ × (M_max - M)

Where M equals current mold index, t equals time, k₁ represents temperature-dependent growth rate factor, k₂ represents RH-dependent growth rate factor, and M_max represents maximum achievable mold index for the material.

## MI 0 To 6 Scale

The six-level scale provides correspondence between calculated index values and observable growth:

**MI 0-1 (No visible growth):** Spore germination and initial hyphal development occur at microscopic level. Building materials exhibit no visible changes. This stage represents the critical prevention target, as growth remains reversible through drying.

**MI 1-2 (Microscopic growth):** Hyphal networks develop across material surfaces but remain below visual detection threshold without magnification. Trained observers using microscopy can detect growth. Risk of spore release remains low as fruiting bodies have not developed.

**MI 2-3 (Threshold of visible growth):** Mold becomes visible to trained observers under good lighting conditions. Surface discoloration may appear as small spots or patches. Musty odors may become detectable. This threshold represents the practical detection limit for visual inspection.

**MI 3-4 (Moderate visible growth):** Mold growth becomes obvious to any observer. Surface coverage reaches 10-50% depending on material and conditions. Spore production accelerates, increasing exposure risk for occupants. Material damage begins as hyphae penetrate substrate.

**MI 4-5 (Extensive growth):** Mold covers majority of exposed surface (>50%). Multiple colors may be visible as different species colonize the substrate. Strong musty odors prevail. Structural material properties begin degrading as extensive hyphal penetration occurs.

**MI 5-6 (Maximum growth):** Complete surface coverage with thick, velvet-like mat of growth. Material strength significantly compromised. Massive spore production creates high exposure risk. Remediation requires material removal rather than surface cleaning.

## Sensitivity Classes

Material sensitivity classifications account for varying mold susceptibility across building materials. The VTT model defines four sensitivity classes:

**Very sensitive (Class 1):** Biodegradable materials including untreated wood, paper products, cardboard, and natural fiber insulations. These materials provide ideal nutrients for mold growth with critical RH threshold around 80% at 20°C.

**Sensitive (Class 2):** Planed and surface-treated wood, paper-faced gypsum board, and cellulose-based materials. Treatment provides some resistance but materials remain susceptible under sustained moisture exposure. Critical RH threshold approximately 85% at 20°C.

**Medium resistant (Class 3):** Cement-based materials, mineral wool insulation, glass-faced gypsum board, and treated wood products. These materials resist mold growth better than Classes 1-2 but support growth when contaminated with dust or when moisture levels remain elevated for extended periods. Critical RH threshold approximately 90% at 20°C.

**Resistant (Class 4):** Inorganic materials including glass, metal, ceramic tile, and plastics. These materials provide no nutrients for mold growth. Growth occurs only when organic contamination (dust, oils, residues) accumulates on surfaces. Critical RH threshold approximately 95% at 20°C.

## Critical Mold Index Mi 3

MI = 3 represents the critical threshold used in ASHRAE Standard 160 and building design practice. This threshold corresponds to initial visible mold growth detectable by building occupants, marking the transition from acceptable to unacceptable conditions.

Selecting MI = 3 as the failure criterion provides several advantages. The threshold remains conservative, preventing growth before extensive colonization occurs. Remediation at MI = 3 remains relatively simple, often requiring only cleaning and drying rather than material replacement. The threshold corresponds to observable criteria, enabling validation through visual inspection.

Design targets typically aim to maintain MI below 1.0 under normal conditions, providing safety margin before reaching the MI = 3 threshold. This approach accommodates modeling uncertainties, construction defects, and more severe weather events than design conditions.

Time to reach MI = 3 varies dramatically with environmental conditions and material sensitivity. Under highly favorable conditions (25°C, 95% RH, sensitive material), MI = 3 may be reached in 4-8 weeks. Under marginal conditions (20°C, 85% RH, medium-resistant material), reaching MI = 3 may require 6-12 months or may never occur if conditions fluctuate.

## Exposure Calculations

Calculating mold risk using the VTT model requires hourly or daily environmental data over extended periods (typically one year). Hygrothermal simulation software including WUFI, DELPHIN, and hygIRC generates the required temperature and relative humidity data for critical surfaces within building assemblies.

Analysis workflow proceeds through several steps:

1. **Assembly definition:** Specify material layers, thicknesses, and properties (thermal conductivity, specific heat, vapor permeability, sorption isotherms)

2. **Boundary conditions:** Define interior and exterior climate conditions using weather data, indoor temperature and humidity setpoints, and air change rates

3. **Simulation:** Calculate hourly temperature and RH at critical surfaces (typically exterior sheathing surface and interior surface of exterior walls)

4. **VTT model application:** Apply VTT equations using simulation outputs to calculate mold index progression over time

5. **Evaluation:** Compare maximum mold index achieved during simulation period against acceptance criteria (typically MI < 1.0 target, MI < 3.0 maximum)

## Ashrae 160 Implementation

ASHRAE Standard 160 "Criteria for Moisture-Control Design Analysis in Buildings" implements the VTT model as the recommended method for evaluating mold risk in hygrothermal simulations. The standard specifies:

**Analysis period:** Minimum three years of simulation with last year used for compliance evaluation (first two years allow moisture equilibration from assumed initial conditions)

**Critical surfaces:** Exterior sheathing surface behind cladding and interior surface of exterior walls

**Acceptance criteria:** 30-day running average surface RH must remain below limits specified in tables based on material sensitivity and temperature. For sensitive materials at 20°C, 30-day running average must remain below 80% RH.

**Climate data:** TMY3 (Typical Meteorological Year) or actual weather data for project location

The 30-day running average approach smooths short-term RH fluctuations while capturing sustained elevated moisture conditions that support mold growth. Brief excursions above critical thresholds do not trigger failures if average conditions remain acceptable.

Standard 160 compliance provides objective evidence that building assemblies resist mold growth under typical climate conditions. Compliance does not guarantee mold-free performance, as actual construction quality, occupant behavior, and weather conditions may deviate from simulation assumptions. However, compliance provides reasonable assurance that properly constructed assemblies will perform acceptably.
