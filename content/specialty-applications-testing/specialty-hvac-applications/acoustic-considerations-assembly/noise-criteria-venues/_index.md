---
title: "Noise Criteria for Performance Venues"
description: "Technical guidance on HVAC noise criteria (NC) curves for performance venues including concert halls (NC-20), theaters (NC-25), lecture halls (NC-30), and arenas (NC-35) with SPL calculations and design strategies."
keywords: ["noise criteria", "NC curves", "concert hall acoustics", "theater HVAC", "sound pressure level", "ASHRAE acoustics", "performance venue HVAC", "NC-20", "NC-25", "NC-30", "background noise"]
tags: ["acoustics", "noise control", "performance venues", "sound design", "ASHRAE standards"]
weight: 1
---

Performance venues demand stringent HVAC noise control to preserve acoustic quality and audience experience. The Noise Criteria (NC) rating system, developed by Leo Beranek and standardized in ASHRAE applications, provides frequency-weighted limits for background sound that correlate with human perception in critical listening environments.

## NC Curve Fundamentals

NC curves define maximum permissible sound pressure levels (SPL) across octave bands from 63 Hz to 8000 Hz. Each NC rating represents a family of frequency-specific limits, with lower frequencies allowed higher SPL due to reduced human sensitivity at low frequencies and the masking characteristics of HVAC systems.

The NC value corresponds approximately to the SPL at 1000 Hz. An NC-25 space permits 25 dB at 1000 Hz, but allows 47 dB at 63 Hz and restricts 22 dB at 4000 Hz. This frequency weighting addresses the fact that low-frequency rumble and high-frequency hiss are the primary complaints in under-designed systems.

## Performance Venue NC Targets

| Venue Type | NC Rating | Design Intent | Critical Considerations |
|------------|-----------|---------------|------------------------|
| Concert Halls | NC-20 | Preserve full dynamic range for unamplified music | Extreme low-frequency control required |
| Theaters | NC-25 | Support clear dialogue and dramatic performance | Balance speech intelligibility with comfort |
| Lecture Halls | NC-30 | Enable effective communication without distraction | Cost-effective while maintaining quality |
| Arenas | NC-35 | Provide acceptable background for amplified events | Focus on duct breakout and equipment isolation |

### NC-20 Concert Halls

Concert halls require NC-20 to preserve the dynamic range of orchestral and chamber music, where pianissimo passages reach 40-50 dBA. HVAC noise above NC-20 intrudes on musical content and reduces perceived hall quality. Achieving NC-20 demands:

- Air velocities below 500 fpm in occupied zones
- Duct velocities limited to 1200-1500 fpm maximum
- Minimum 6-inch duct lining with 1.5 lb/ft³ density
- Equipment rooms separated by minimum 50 STC partitions
- Vibration isolation achieving 95% efficiency at operating frequencies

### NC-25 Theaters

Theatrical venues balance acoustic quality with economic constraints. NC-25 permits adequate speech intelligibility while controlling costs compared to NC-20 designs. The 5 dB relaxation allows modestly higher air velocities and reduced silencer requirements, but still demands attention to:

- Supply air velocities of 600-700 fpm maximum
- High-performance diffusers with low induction ratios
- Duct silencers at AHU discharge and zone entries
- Isolation of rooftop equipment with spring mounts

### NC-30 Lecture Halls

Educational spaces targeting NC-30 support effective communication without the extreme measures required for music venues. The 10 dB margin above NC-20 significantly reduces first cost while maintaining acceptable acoustic conditions. Design focuses on:

- Conventional VAV or displacement ventilation systems
- Standard duct lining and attenuators
- Roof-mounted equipment with basic vibration isolation
- Terminal unit selection emphasizing low-noise damper operation

### NC-35 Arenas

Large arenas and multi-purpose venues typically target NC-35, recognizing that most events employ sound reinforcement. The relaxed criteria acknowledge that acoustical perfection conflicts with the large air quantities, extensive ductwork, and cost constraints of high-occupancy spaces.

## SPL Calculation Methodology

Predicting HVAC-generated sound levels requires accounting for multiple sources and paths:

**Equipment Sound Power:**
Sound power level (Lw) from manufacturer data provides the starting point. A centrifugal fan generating Lw = 85 dB at 500 Hz transmits sound through ductwork to occupied spaces.

**Duct Attenuation:**
Unlined sheet metal duct provides minimal attenuation (0.1-0.3 dB/ft). Lined duct yields 1-3 dB/ft depending on frequency, lining thickness, and duct size. For a 100-foot duct run with 1-inch lining in a 24"x12" duct:

Attenuation = 1.5 dB/ft × 100 ft = 150 dB (unrealistic—actual systems require segmented analysis)

Realistic attenuation considers: straight duct runs, elbows (3-5 dB each), transitions (2-4 dB), splits (3 dB per division), and terminal devices (5-15 dB).

**End Reflection Loss:**
Open duct terminations reflect sound back into the duct system. End reflection loss (ERL) depends on duct area and frequency:

ERL = 10 log(1 + (λ/4πA)²)

Where λ = wavelength and A = duct cross-sectional area. At 125 Hz (λ = 9 ft), a 2 ft² diffuser provides approximately 12 dB end reflection loss.

**Room Effect:**
Sound pressure level in the occupied space depends on room absorption:

SPL = Lw - 10 log(A/4) + 10.5 dB

Where A = room absorption in sabins. A concert hall with 5000 sabins yields:

SPL = Lw - 10 log(5000/4) + 10.5 = Lw - 20.5 dB

## Achieving Design Targets

Meeting stringent NC criteria requires integrated design:

**Source Control:**
Select low-speed fans (TSP < 4 in. wg), oversized coils reducing air velocity, and VFDs to avoid discrete-frequency tones. Centrifugal fans with backward-curved blades generate 5-10 dB less sound than forward-curved alternatives.

**Path Treatment:**
Install silencers where calculated levels exceed targets by >5 dB. Size silencers for insertion loss at problem frequencies—typically 125-500 Hz for rumble, 2000-4000 Hz for hiss. Avoid silencer air velocities above 1500 fpm to prevent self-generated noise.

**Receiver Protection:**
Use sound-rated ceiling plenums (CAC > 35), lined ductwork in occupied spaces, and low-velocity diffusers. Locate returns away from critical listening areas or use ducted returns with similar treatment as supply systems.

**Commissioning Verification:**
Conduct octave-band sound level measurements at design airflow with all systems operating. Compare measured values against NC curves using spectrum analysis. Address exceedances through airflow adjustment, additional silencers, or diffuser replacement before occupancy.

## References

ASHRAE Handbook—HVAC Applications, Chapter 49: Noise and Vibration Control provides comprehensive NC curve data, calculation methods, and application guidance. ANSI/ASA S12.60 establishes performance criteria for classroom acoustics applicable to lecture halls. Acoustic consultants should participate in design for venues requiring NC-25 or lower.
