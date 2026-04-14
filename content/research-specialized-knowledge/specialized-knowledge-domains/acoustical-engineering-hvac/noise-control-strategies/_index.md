---
title: "Noise Control Strategies"
aliases: ["Noise Control Strategies"]
description: "Source-path-receiver noise control principles, vibration isolation, acoustic enclosures, sound absorption, and reverberation time control for HVAC applications"
weight: 2
---

## Overview

Noise control strategies for HVAC systems apply engineering principles to reduce sound transmission from source to receiver through three fundamental approaches: source modification, path attenuation, and receiver protection. Effective noise control requires systematic analysis identifying dominant sources, transmission paths, and receiver sensitivity before implementing targeted treatments. The source-path-receiver model provides framework for selecting appropriate control measures.

## Source-Path-Receiver Control Framework

The source-path-receiver model recognizes three essential elements in any noise problem. Sources generate sound through mechanical vibration, aerodynamic turbulence, or electromagnetic forces. Paths transmit sound through air, structure, or ductwork. Receivers experience sound at occupied locations. Control measures target any or all three elements.

Source control provides most cost-effective noise reduction by preventing sound generation. Select inherently quiet equipment, reduce operating speeds, balance rotating components, and eliminate flow-induced turbulence. Source control implemented during design costs far less than retrofit path treatment or receiver protection.

Path control interrupts sound transmission using barriers, absorption, distance, and vibration isolation. Increase transmission loss through walls and floors, install duct silencers, apply vibration isolation mounts, and route ductwork away from sound-sensitive areas. Path control effectiveness depends on understanding all transmission routes including flanking paths.

Receiver protection employs barriers, sound-absorbing enclosures, or hearing protection when source and path control prove insufficient or impractical. Administrative controls limit exposure duration. Receiver protection represents last resort after exhausting source and path control options.

## Equipment Selection and Source Control

HVAC equipment selection significantly affects system acoustical performance. Manufacturers provide sound power level data per AHRI standards, permitting comparison between alternative equipment. Select equipment with sound power 5-10 dB below required room sound pressure level to account for installation effects and multiple sources.

Fan selection optimizes for acoustical performance operating at peak efficiency. Sound power increases dramatically at flow conditions away from peak efficiency due to turbulence and flow separation. Centrifugal fans operate quieter than axial fans at equal capacity. Backward-curved centrifugal fans produce less noise than forward-curved designs.

Variable frequency drives (VFDs) enable variable volume operation at reduced speed, decreasing both sound power and energy consumption. Sound power reduces approximately 15 dB per halving of fan speed. VFD tonal noise from switching frequencies requires consideration; use high carrier frequencies (>10 kHz) to shift tones above audible range.

Compressor selection affects chiller and packaged equipment acoustics. Screw compressors generate strong tonal components at compressor operating frequency. Centrifugal compressors produce broadband noise with less tonal content. Scroll compressors operate quietly in smaller capacity ranges. Sound-insulated compressor enclosures reduce radiated noise by 10-20 dB.

## Vibration Isolation Design

Vibration isolation prevents structure-borne sound transmission by inserting compliant mounts between vibrating equipment and building structure. Effective isolation requires isolator natural frequency substantially below lowest excitation frequency. The isolation efficiency equation governs performance:

TE = 20 log|(fn/f)^2 / (1 - (fn/f)^2)|

Where TE is transmissibility in dB, fn is isolator natural frequency, and f is excitation frequency. Transmissibility decreases 12 dB per octave above √2 × fn.

Spring isolators provide low natural frequency (2-8 Hz) suitable for equipment with low-frequency vibration. Open springs, housed springs, and restrained spring mounts accommodate different loading conditions. Seismic restraints limit motion during earthquakes while permitting vibration isolation during normal operation.

Elastomeric isolators using natural rubber, neoprene, or cork provide simple, economical isolation with natural frequencies 8-20 Hz. Elastomeric pads suffice for small equipment with smooth operation. Molded elastomeric mounts with metal housings handle moderate loads and provide all-direction isolation.

Pneumatic isolators achieve very low natural frequencies (1-3 Hz) using air springs, providing superior low-frequency isolation for sensitive equipment. Self-leveling designs maintain constant height despite load variations. However, pneumatic isolators require air supply and pressure regulation.

Inertia bases increase equipment mass, lowering center of gravity and system natural frequency. Concrete inertia bases typically weigh 1.5 to 3 times equipment weight. The combined equipment-base system mounts on vibration isolators. Inertia bases prove essential for equipment with significant unbalanced forces including reciprocating compressors.

## Acoustic Enclosures

Acoustic enclosures surround noise sources with barrier and absorptive materials, reducing radiated sound to surrounding space. Enclosure effectiveness depends on barrier transmission loss, absorption coefficient of interior surfaces, enclosure volume, and opening area for ventilation and access.

Enclosure insertion loss approximates:
IL = TL - 10 log(S/A) - 6 dB

Where IL is insertion loss, TL is barrier transmission loss, S is interior surface area, and A is total interior absorption (S × average absorption coefficient). Achieving 20-30 dB insertion loss requires TL > 30 dB and highly absorptive interior surfaces.

Prefabricated acoustical panels combine mass-loaded vinyl or steel facing with fibrous glass absorption and perforated inner facing. Modular panels assemble into complete enclosures with access doors, windows, and ventilation openings. Sealing panel joints with gaskets prevents flanking transmission degrading performance.

Ventilation openings necessary for heat removal compromise enclosure effectiveness. Acoustically-lined ventilation paths using duct silencers or baffle arrangements maintain adequate insertion loss while providing airflow. Size ventilation openings for low velocity (<500 fpm) to minimize turbulence noise generation.

## Sound-Absorbing Materials

Sound-absorbing materials convert acoustic energy to heat through viscous and thermal losses in porous structures. Fibrous glass, mineral wool, open-cell foam, and acoustical ceiling tile provide sound absorption. Absorption coefficient α ranges from 0 (perfect reflection) to 1 (perfect absorption), varying with frequency and installation method.

Porous absorbers perform best at mid-high frequencies where material thickness exceeds quarter wavelength. One-inch fibrous glass provides α = 0.4-0.6 at 500 Hz, increasing to α = 0.8-0.9 at 2000 Hz. Low-frequency absorption requires thick materials (6+ inches) or air space behind thinner materials.

Absorption placement affects effectiveness. Materials mounted directly on hard surfaces perform poorly at low frequencies due to near-zero particle velocity at boundary. Spacing absorptive materials 2-4 inches from surfaces improves low-frequency performance. Suspended baffles and clouds provide absorption with all surfaces exposed to sound field.

Perforated metal facing protects fibrous materials from air stream erosion in ducts while maintaining acoustic performance. Perforation percentage should exceed 20% with hole diameter 1/8 to 1/4 inch. Fibrous material must contact perforated facing; air gaps reduce effectiveness.

## Acoustic Treatment of Rooms

Room acoustic treatment controls reverberation time, reduces reflected noise, and improves speech intelligibility. Reverberation time T60 represents time for sound to decay 60 dB after source cessation. The Sabine equation relates reverberation time to room characteristics:

T60 = 0.049 V / A

Where V is room volume in cubic feet and A is total room absorption in sabins. Shorter reverberation times reduce overall noise levels and improve subjective acoustic quality in mechanical rooms and occupied spaces.

Mechanical equipment rooms benefit from acoustic treatment reducing reflected sound and worker exposure. Apply 2-4 inch fibrous glass panels to walls and ceiling, achieving α = 0.7-0.9 at mid-high frequencies. Treatment reduces reverberant noise by 3-8 dB depending on room geometry and treatment coverage.

Open-plan offices require careful acoustic design balancing sound absorption and privacy. Excessive absorption creates "dead" acoustic preventing speech privacy through increased speech effort. Moderate absorption (NRC 0.7-0.8) combined with sound masking provides optimal balance.

## Anechoic and Reverberation Chambers

Anechoic chambers provide free-field conditions for acoustical testing, eliminating reflected sound through highly absorptive wedges on all surfaces. Wedge length determines low-frequency cutoff; 36-inch wedges provide anechoic conditions to 100 Hz. Sound power measurements in anechoic chambers eliminate room effects complicating data interpretation.

Reverberation chambers provide diffuse sound fields for sound power determination and absorption coefficient measurement. Hard, non-parallel surfaces with minimal absorption create long reverberation time (5-10 seconds). Spatial averaging eliminates standing wave effects. Rotating diffusers ensure uniform sound distribution.

Semi-anechoic chambers combine absorptive walls/ceiling with reflective floor, simulating equipment installation on floor surface. Free-field conditions exist above reflecting plane. Semi-anechoic rooms accommodate large equipment while maintaining controlled acoustic environment.

## Reverberation Time Control

Reverberation time optimization depends on room function. Mechanical rooms benefit from short reverberation (T60 < 1 second) reducing worker noise exposure. Office spaces target 0.4-0.6 seconds for speech communication. Conference rooms require 0.5-0.8 seconds balancing speech intelligibility and natural acoustic quality.

Adding absorption reduces reverberation time. Calculate required absorption to achieve target reverberation using Sabine equation solved for A. Distribute absorption throughout room rather than concentrating on single surface. Ceiling treatment provides most practical location in most applications.

Live-end dead-end (LEDE) designs place absorptive treatment at room end near loudspeakers with reflective surfaces at opposite end. This arrangement reduces early reflections degrading intelligibility while maintaining adequate reverberation for natural acoustic quality. LEDE designs apply to recording studios and critical listening rooms.

## Outdoor Noise Control

HVAC equipment located outdoors requires consideration of community noise impact. Building codes and municipal ordinances often limit property-line noise levels. Elevated rooftop equipment radiates sound over greater distances than grade-level installations.

Outdoor barriers attenuate sound through diffraction over barrier top and transmission through barrier mass. Barrier insertion loss depends on path length difference between direct and diffracted paths:

IL = 20 log(√(2πN) + 5) - 3 dB

Where N is Fresnel number relating wavelength to path difference. Barriers provide 5 dB insertion loss at low frequencies, increasing to 20-24 dB at high frequencies when line of sight is completely blocked.

Equipment screens combine barrier mass with absorptive inner facing, providing diffraction attenuation plus absorption of reflected sound. Three-sided or four-sided screens surrounding equipment provide greater insertion loss than single barriers. However, screens may restrict airflow to equipment requiring ventilation or heat rejection.
