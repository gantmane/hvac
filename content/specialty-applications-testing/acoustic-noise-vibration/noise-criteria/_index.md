---
title: "HVAC Noise Criteria and Sound Level Standards"
aliases: ["HVAC Noise Criteria and Sound Level Standards"]
description: "Technical analysis of NC curves, RC Mark II methodology, recommended noise criteria by space type, background noise measurement procedures, and speech interference levels for HVAC systems."
keywords: ["NC curves", "RC Mark II", "noise criteria", "HVAC acoustics", "background noise", "speech interference", "sound pressure level", "octave band analysis", "ASHRAE noise standards"]
tags: ["NC curves", "RC Mark II", "noise criteria", "HVAC acoustics", "background noise", "speech interference", "sound pressure level", "octave band analysis", "ASHRAE noise standards"]
date: 2026-01-05
weight: 2
draft: false
---

## Overview

HVAC noise criteria provide standardized methods for evaluating and specifying acceptable sound levels in occupied spaces. These criteria account for both sound pressure level magnitude and spectral balance across octave frequency bands, ensuring acoustic comfort and functional performance in buildings.

## Noise Criteria (NC) Curves

NC curves, developed by Leo Beranek in 1957, establish maximum acceptable sound pressure levels across octave bands from 63 Hz to 8000 Hz. Each NC curve represents a family of octave band sound pressure levels that define a specific noise rating.

**NC Curve Mathematical Relationship:**

The NC curves follow an approximate relationship where sound pressure level decreases with increasing frequency. For a given NC rating N:

SPL(f) = N + A(f)

Where:
- SPL(f) = Sound pressure level at frequency f (dB)
- N = NC rating number
- A(f) = Frequency-dependent adjustment factor

**NC Rating Determination:**

1. Measure sound pressure levels in octave bands (63, 125, 250, 500, 1000, 2000, 4000, 8000 Hz)
2. Plot measured levels on NC curve chart
3. Identify the highest NC curve touched or exceeded by any octave band
4. The NC rating equals the highest curve intersected

**Limitations of NC Curves:**

- No assessment of spectral balance quality
- Does not differentiate between rumble, hiss, or neutral spectra
- Provides only maximum level limits without guidance on optimal spectral shape

## Room Criteria (RC) Mark II

RC Mark II, published by ASHRAE in the 1995 HVAC Applications Handbook, addresses NC curve limitations by evaluating both sound level and spectral quality. This method provides superior acoustic assessment for modern HVAC systems.

**RC Mark II Methodology:**

The RC rating represents the average sound pressure level in the 500, 1000, 2000, and 4000 Hz octave bands, mathematically expressed as:

RC = (SPL₅₀₀ + SPL₁₀₀₀ + SPL₂₀₀₀ + SPL₄₀₀₀) / 4

**Spectral Quality Descriptors:**

RC Mark II assigns quality descriptors based on deviations from the reference curve:

- **(N) Neutral:** Spectrum follows RC reference curve within acceptable tolerance
- **(LF) Low-Frequency Rumble:** Excess energy below 500 Hz, typically from large fans, ducts, or structure-borne vibration
- **(MF) Mid-Frequency Roar:** Excess energy at 500-1000 Hz, often from diffusers or high-velocity airflow
- **(HF) High-Frequency Hiss:** Excess energy above 2000 Hz, characteristic of turbulent flow or small dampers

**Region of Acceptability:**

RC Mark II defines acceptable deviations from the reference curve:
- Low-frequency region (16-63 Hz): +5 dB maximum above reference
- Mid-frequency region (125-500 Hz): ±5 dB tolerance
- High-frequency region (1000-4000 Hz): ±3 dB tolerance

Sound levels creating noticeable rumble or hiss fall outside the region of acceptability and require corrective action.

## Recommended Noise Criteria by Space Type

Proper specification of noise criteria depends on space function, occupancy expectations, and acoustic sensitivity.

| Space Type | NC Rating | RC Rating | Notes |
|------------|-----------|-----------|-------|
| Private offices | NC 30-35 | RC 30-35(N) | Executive offices at lower end |
| Open office areas | NC 35-40 | RC 35-40(N) | Modern offices trend toward NC 35 |
| Conference rooms | NC 25-30 | RC 25-30(N) | Critical for speech intelligibility |
| Classrooms | NC 25-30 | RC 25-30(N) | Per ANSI S12.60 standard |
| Libraries | NC 30-35 | RC 30-35(N) | Reading areas at lower end |
| Hospital patient rooms | NC 30-35 | RC 30-35(N) | Sleep environment consideration |
| Operating rooms | NC 35-40 | RC 35-40(N) | Higher due to equipment noise |
| Laboratories | NC 40-50 | RC 40-50(N) | Varies by lab type and equipment |
| Retail spaces | NC 40-45 | RC 40-45(N) | Customer areas |
| Restaurants | NC 40-50 | RC 40-50(N) | Depends on dining style |
| Theaters/auditoriums | NC 20-25 | RC 20-25(N) | Most stringent requirement |
| Gymnasiums | NC 45-50 | RC 45-50(N) | High activity level |
| Mechanical equipment rooms | NC 55-65 | — | Not occupied continuously |

## Background Noise Measurement

Accurate background noise measurement requires proper instrumentation and methodology to establish baseline conditions or verify compliance.

**Required Equipment:**

- Type 1 or Type 2 sound level meter per ANSI S1.4
- Octave band filter set (minimum one-octave bands)
- Acoustic calibrator (Class 1 per IEC 60942)

**Measurement Procedure:**

1. **Calibration:** Verify sound level meter calibration before and after measurements
2. **Microphone Position:** Place at 4-5 feet above floor, minimum 3 feet from walls, representative of occupied zone
3. **HVAC Operation:** Operate all systems in normal steady-state mode
4. **Integration Time:** Measure for minimum 30 seconds per location, average fluctuating levels
5. **Multiple Locations:** Take readings at 3-5 positions per space for rooms exceeding 1000 square feet
6. **Data Recording:** Record octave band sound pressure levels (63-8000 Hz minimum)

**Environmental Considerations:**

- Conduct measurements when building is unoccupied or with minimal occupant-generated noise
- Close windows and doors to isolate HVAC contribution
- Turn off non-HVAC equipment (computers, lighting ballasts, appliances)
- Avoid measurements during precipitation or high wind conditions affecting exterior noise intrusion

## Speech Interference and Articulation Index

HVAC background noise directly impacts speech communication effectiveness through masking of speech frequencies.

**Speech Interference Level (SIL):**

SIL represents the arithmetic average of sound pressure levels in octave bands centered at 500, 1000, 2000, and 4000 Hz:

SIL = (SPL₅₀₀ + SPL₁₀₀₀ + SPL₂₀₀₀ + SPL₄₀₀₀) / 4

This parameter correlates directly with communication distance limitations.

**Maximum Communication Distance:**

| Voice Level | SIL 45 dB | SIL 55 dB | SIL 65 dB |
|-------------|-----------|-----------|-----------|
| Normal | 12 ft | 4 ft | 1.5 ft |
| Raised | 24 ft | 8 ft | 3 ft |
| Very loud | 48 ft | 16 ft | 6 ft |
| Shouting | 96 ft | 32 ft | 12 ft |

For conference rooms and classrooms requiring normal voice communication across 15-20 feet, SIL must remain below 45 dB, corresponding approximately to RC 35-40(N).

**Preferred Speech Interference Level (PSIL):**

PSIL uses only the 500, 1000, and 2000 Hz bands, offering slightly different weighting for speech frequency emphasis in certain applications.

## ASHRAE Standards and References

ASHRAE provides authoritative guidance on HVAC acoustics in multiple publications:

- **ASHRAE Handbook—HVAC Applications, Chapter 49:** Comprehensive treatment of sound and vibration control, including RC Mark II methodology
- **ASHRAE Standard 189.1:** Acoustic requirements for high-performance green buildings
- **ASHRAE Design Guide:** Includes recommended design criteria and measurement protocols

The RC Mark II method represents current best practice for HVAC noise specification, superseding NC curves for new design while maintaining compatibility with existing NC-based specifications through approximate equivalence (RC ≈ NC - 5 for neutral spectra).

## Design Implementation

Achieving specified noise criteria requires integrated acoustic design:

1. **Source Control:** Select low-noise HVAC equipment based on manufacturer sound power data
2. **Path Treatment:** Size ductwork for velocities below 2000 fpm in occupied spaces, incorporate sound attenuators where needed
3. **Receiver Protection:** Locate noise-sensitive spaces away from mechanical equipment
4. **Vibration Isolation:** Isolate rotating equipment to prevent structure-borne sound transmission
5. **Commissioning Verification:** Measure final installed performance to confirm compliance with specified criteria

Proper application of noise criteria ensures HVAC systems provide thermal comfort without acoustic disruption, supporting occupant productivity and well-being.
