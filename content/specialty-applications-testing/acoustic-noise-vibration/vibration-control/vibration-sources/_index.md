---
title: "Vibration Sources in HVAC Systems"
description: "Comprehensive analysis of vibration sources in HVAC equipment including fans, pumps, compressors, and motors with forcing frequency calculations and characteristics."
date: 2025-01-05
weight: 1
keywords: ["vibration sources", "forcing frequency", "rotating equipment vibration", "fan vibration", "pump vibration", "compressor vibration", "motor vibration", "HVAC vibration analysis"]
---

## Fundamental Vibration Sources

HVAC equipment generates vibration through rotating and reciprocating components. Understanding vibration sources is essential for proper isolation system design and troubleshooting. The primary sources include fans, pumps, compressors, motors, and their associated components.

Vibration originates from mass imbalance, misalignment, bearing defects, aerodynamic forces, and electromagnetic effects. Each source produces characteristic frequencies that can be calculated and measured.

## Forcing Frequency Calculations

### Rotational Frequency

The fundamental frequency of rotating equipment is:

$$f_r = \frac{N}{60}$$

where:
- $f_r$ = rotational frequency (Hz)
- $N$ = rotational speed (rpm)

### Blade/Vane Pass Frequency

For fans and pumps with multiple blades or vanes:

$$f_{bp} = \frac{N \times n_b}{60}$$

where:
- $f_{bp}$ = blade pass frequency (Hz)
- $n_b$ = number of blades or vanes

### Belt Drive Frequencies

Belt-driven equipment generates additional frequencies:

$$f_{belt} = \frac{N_{driver} \times D_{driver}}{D_{driven} \times 60}$$

$$f_{defect} = \frac{v}{L}$$

where:
- $D_{driver}$, $D_{driven}$ = sheave diameters
- $v$ = belt velocity
- $L$ = belt length

### Bearing Frequencies

Rolling element bearings produce specific defect frequencies. For ball pass frequency on outer race:

$$f_{BPFO} = \frac{n_b \times N}{120} \left(1 - \frac{d_b \cos \alpha}{D_p}\right)$$

where:
- $n_b$ = number of balls
- $d_b$ = ball diameter
- $D_p$ = pitch diameter
- $\alpha$ = contact angle

## Equipment Vibration Characteristics

### Centrifugal Fans

| Vibration Source | Frequency | Typical Amplitude | Primary Direction |
|------------------|-----------|-------------------|-------------------|
| Mass imbalance | 1× rpm | 0.1-0.3 in/s | Radial |
| Blade pass | $n_b$ × rpm | 0.05-0.2 in/s | Axial/radial |
| Belt defects | Variable | 0.1-0.5 in/s | Radial |
| Aerodynamic pulsation | $n_b$ × rpm | 0.02-0.15 in/s | Axial |
| Bearing wear | BPFO/BPFI | 0.05-0.3 in/s | Radial |

Centrifugal fans typically exhibit:
- Fundamental frequency at running speed
- Strong blade pass frequency component
- Harmonics at 2× and 3× running speed with imbalance
- Low-frequency vibration (< 10 Hz) from inlet flow disturbances

### Centrifugal Pumps

| Vibration Source | Frequency | Typical Amplitude | Primary Direction |
|------------------|-----------|-------------------|-------------------|
| Impeller imbalance | 1× rpm | 0.08-0.25 in/s | Radial |
| Vane pass | $n_v$ × rpm | 0.1-0.4 in/s | Radial |
| Cavitation | Broadband | 0.2-0.8 in/s | Random |
| Misalignment | 2× rpm | 0.15-0.5 in/s | Axial |
| Looseness | Multiple harmonics | 0.1-0.4 in/s | All directions |

Pumps operating away from best efficiency point (BEP) generate:
- Elevated vane pass frequency amplitudes
- Hydraulic instability at 0.3-0.8× vane pass frequency
- Recirculation vibration at 0.1-0.4× running speed

### Reciprocating Compressors

Reciprocating compressors produce complex vibration spectra:

| Vibration Source | Frequency | Typical Amplitude | Primary Direction |
|------------------|-----------|-------------------|-------------------|
| Piston fundamental | 1× rpm | 0.2-0.6 in/s | Axial/vertical |
| Gas pulsation | $n_c$ × rpm | 0.3-1.0 in/s | Piping direction |
| Unbalanced forces | 2× rpm | 0.15-0.5 in/s | Horizontal |
| Valve impact | High frequency | 0.1-0.3 in/s | Random |

where $n_c$ = number of compression stages per revolution.

### Screw Compressors

| Vibration Source | Frequency | Typical Amplitude | Primary Direction |
|------------------|-----------|-------------------|-------------------|
| Rotor imbalance | 1× rpm | 0.1-0.3 in/s | Radial |
| Lobe mesh | $n_l$ × rpm | 0.15-0.4 in/s | Axial/radial |
| Bearing defects | BPFO/BPFI | 0.05-0.25 in/s | Radial |
| Gas pulsation | Variable | 0.1-0.35 in/s | Discharge piping |

where $n_l$ = number of lobes on male rotor.

### Electric Motors

| Vibration Source | Frequency | Typical Amplitude | Primary Direction |
|------------------|-----------|-------------------|-------------------|
| Rotor imbalance | 1× rpm | 0.05-0.2 in/s | Radial |
| Misalignment | 2× rpm | 0.1-0.4 in/s | Axial |
| Electrical | 2× line frequency | 0.02-0.15 in/s | Radial |
| Broken rotor bars | Slip frequency sidebands | 0.05-0.2 in/s | Radial |
| Eccentricity | Line frequency ± slip | 0.03-0.12 in/s | Radial |

For 60 Hz power, electromagnetic vibration occurs at 120 Hz (7,200 cpm) regardless of motor speed. Slip frequency sidebands appear at:

$$f_{slip} = f_{line} \times \left(\frac{N_{sync} - N_{actual}}{N_{sync}}\right)$$

## Practical Calculation Example

For a 1,750 rpm centrifugal fan with 10 blades:

$$f_r = \frac{1750}{60} = 29.2 \text{ Hz (1750 cpm)}$$

$$f_{bp} = \frac{1750 \times 10}{60} = 292 \text{ Hz (17,500 cpm)}$$

Expected vibration spectrum shows peaks at 29.2 Hz and 292 Hz with harmonics at 58.4 Hz, 87.6 Hz, etc.

## Vibration Severity Guidelines

According to ISO 10816 and ASHRAE Handbook Chapter 49, acceptable vibration levels vary by equipment type and mounting:

- **Rigidly mounted equipment (< 15 kW):** < 0.28 in/s RMS
- **Rigidly mounted equipment (15-75 kW):** < 0.45 in/s RMS
- **Flexibly mounted equipment:** < 0.71 in/s RMS
- **Reciprocating machines:** < 1.1 in/s RMS

These values represent overall RMS velocity measured on bearing housings in the frequency range 10-1,000 Hz.

## Diagnostic Considerations

Vibration analysis requires frequency domain measurements using FFT analyzers. Key diagnostic indicators:

- **1× running speed dominance:** Mass imbalance
- **2× running speed dominance:** Misalignment or looseness
- **High blade/vane pass:** Aerodynamic/hydraulic issues
- **Random broadband:** Cavitation, turbulence, or looseness
- **Harmonics with sidebands:** Gear mesh or bearing defects

Trending vibration amplitude over time identifies developing problems before failure. Establish baseline measurements during commissioning for future comparison.

## References

ASHRAE Handbook—HVAC Applications, Chapter 49: Noise and Vibration Control
ISO 10816: Mechanical Vibration—Evaluation of Machine Vibration by Measurements on Non-Rotating Parts
ISO 20816: Mechanical Vibration—Measurement and Evaluation of Machine Vibration