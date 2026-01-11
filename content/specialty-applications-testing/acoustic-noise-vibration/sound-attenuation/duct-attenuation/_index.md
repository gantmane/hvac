---
title: "Duct Attenuation in HVAC Systems"
description: "Comprehensive guide to sound attenuation in HVAC ductwork including octave band calculations, lined vs unlined performance, and attenuation factors for elbows and branches."
weight: 1
date: 2025-01-05
keywords:
  - duct attenuation
  - sound attenuation
  - acoustical duct liner
  - octave band attenuation
  - duct elbow attenuation
  - branch attenuation
  - terminal unit attenuation
  - HVAC noise control
---

# Duct Attenuation in HVAC Systems

Duct attenuation represents the natural sound reduction that occurs as sound propagates through HVAC ductwork. Understanding and quantifying this attenuation is critical for accurate acoustic predictions and achieving target noise criteria in occupied spaces.

## Fundamental Attenuation Mechanisms

Sound attenuation in ducts occurs through three primary mechanisms:

**Viscous losses** occur at the boundary layer where air velocity approaches zero at the duct wall. These losses increase with frequency and are proportional to the duct perimeter-to-area ratio.

**Thermal conduction losses** result from temperature gradients between compressed and rarefied air regions near duct walls. This mechanism becomes significant at mid to high frequencies.

**Wall absorption** depends on duct material properties and construction. Unlined sheet metal provides minimal absorption, while fibrous duct liner dramatically increases attenuation through energy dissipation within the porous material.

## Straight Duct Attenuation

### Unlined Rectangular Ducts

For unlined rectangular ducts, natural attenuation is minimal and calculated using:

$$\alpha = \frac{K \cdot P}{A \cdot f^{0.5}}$$

Where:
- $\alpha$ = attenuation coefficient (dB/ft)
- $K$ = constant (approximately 1.0 for standard conditions)
- $P$ = duct perimeter (ft)
- $A$ = duct cross-sectional area (ft²)
- $f$ = frequency (Hz)

This relationship demonstrates that higher frequencies attenuate more readily, and ducts with large perimeter-to-area ratios (smaller ducts) provide greater natural attenuation.

### Lined Rectangular Ducts

Acoustical duct liner dramatically improves attenuation performance. The attenuation for lined ducts follows:

$$\alpha_L = \frac{1.4 \cdot P_L \cdot \alpha_m}{A}$$

Where:
- $\alpha_L$ = lined duct attenuation (dB/ft)
- $P_L$ = lined perimeter (ft)
- $\alpha_m$ = material absorption coefficient (Sabins/ft²)
- $A$ = duct cross-sectional area (ft²)

The absorption coefficient varies significantly with frequency and liner thickness. One-inch liner typically provides peak performance between 500-2000 Hz, while two-inch liner extends effectiveness to lower frequencies.

## Attenuation Performance Comparison

| Duct Configuration | 125 Hz | 250 Hz | 500 Hz | 1000 Hz | 2000 Hz | 4000 Hz |
|-------------------|--------|--------|--------|---------|---------|---------|
| **24x12 Unlined** | 0.02 | 0.03 | 0.04 | 0.06 | 0.08 | 0.11 |
| **24x12, 1" Liner** | 0.3 | 0.8 | 1.9 | 2.4 | 2.0 | 1.4 |
| **24x12, 2" Liner** | 0.8 | 1.8 | 3.2 | 3.6 | 2.8 | 1.8 |
| **48x24 Unlined** | 0.01 | 0.02 | 0.03 | 0.04 | 0.06 | 0.08 |
| **48x24, 1" Liner** | 0.2 | 0.5 | 1.2 | 1.5 | 1.3 | 0.9 |
| **48x24, 2" Liner** | 0.5 | 1.1 | 2.0 | 2.3 | 1.8 | 1.2 |

*Table values represent attenuation in dB per linear foot. Data derived from ASHRAE Handbook - HVAC Applications, Chapter 49.*

The comparison demonstrates several critical relationships. Liner effectiveness increases dramatically from unlined conditions, with 2-inch liner providing approximately double the attenuation of 1-inch liner at low frequencies. Larger ducts require greater lengths to achieve equivalent total attenuation due to reduced perimeter-to-area ratios.

## Elbow Attenuation

Duct elbows provide significant attenuation through sound reflection and scattering. Attenuation depends on elbow geometry and frequency:

**Unlined Elbows** - Rectangular turning vanes:

| Frequency Band | 125 Hz | 250 Hz | 500 Hz | 1000 Hz | 2000 Hz | 4000 Hz |
|---------------|--------|--------|--------|---------|---------|---------|
| **Attenuation (dB)** | 1 | 1 | 2 | 3 | 5 | 7 |

**Lined Elbows** - With acoustical liner on all surfaces:

| Frequency Band | 125 Hz | 250 Hz | 500 Hz | 1000 Hz | 2000 Hz | 4000 Hz |
|---------------|--------|--------|--------|---------|---------|---------|
| **Attenuation (dB)** | 3 | 5 | 8 | 12 | 15 | 18 |

Mitered elbows without turning vanes provide 1-2 dB additional attenuation across all frequencies compared to vaned elbows due to increased turbulence and reflection, though at the cost of higher pressure drop.

## Branch Attenuation

When sound propagates through branch takeoffs, energy divides between paths. The attenuation in the branch depends on the area ratio:

$$IL_{branch} = 10 \log_{10}\left(1 + \frac{A_{branch}}{A_{main}}\right)$$

Where:
- $IL_{branch}$ = insertion loss at branch (dB)
- $A_{branch}$ = branch duct area (ft²)
- $A_{main}$ = main duct area (ft²)

A typical branch takeoff (144 in² branch from 576 in² main) provides approximately 6 dB attenuation. Sound in the main duct past the branch experiences:

$$IL_{main} = 10 \log_{10}\left(1 + \frac{A_{main}}{A_{branch}}\right)$$

This yields minimal attenuation (typically 1-2 dB) in the main duct continuation.

## Terminal Unit Attenuation

Terminal units provide substantial attenuation through several mechanisms. VAV boxes generate 5-15 dB attenuation depending on damper position and internal geometry. Fan-powered boxes provide 8-20 dB attenuation, with greatest effectiveness at mid frequencies where internal acoustic lining is most effective.

Diffuser attenuation varies with design:

- Linear slot diffusers: 2-5 dB
- Perforated face diffusers: 3-8 dB
- Ceiling diffusers with backdraft damper: 5-10 dB

## Design Application

Accurate acoustic modeling requires summing individual attenuation components:

$$IL_{total} = \alpha_L \cdot L + IL_{elbows} + IL_{branches} + IL_{terminal}$$

Where $L$ represents the total length of straight duct. Conservative design practice applies a maximum attenuation limit of 20-25 dB per straight duct section to account for flanking paths and uncertainty in liner performance.

## Performance Considerations

Duct liner effectiveness degrades over time due to erosion, particularly in high-velocity systems. Velocities should not exceed 2500 fpm in lined ducts to maintain long-term acoustic performance. Liner must be mechanically fastened per SMACNA standards to prevent delamination.

Field measurements frequently show 2-4 dB less attenuation than theoretical predictions due to installation quality, flanking paths through duct walls, and liner discontinuities at joints. Design calculations should incorporate appropriate safety factors based on project acoustic sensitivity.

The ASHRAE Handbook - HVAC Applications, Chapter 49 provides comprehensive tables for various duct configurations, liner thicknesses, and fittings. These empirically derived values represent the industry standard for acoustic predictions and should be referenced for detailed design work.
