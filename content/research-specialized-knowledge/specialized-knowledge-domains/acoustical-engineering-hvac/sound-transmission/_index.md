---
title: "Sound Transmission"
description: "Airborne and structure-borne sound transmission paths, flanking transmission, duct-borne noise propagation, and regenerated noise in HVAC systems"
weight: 1
---

## Overview

Sound transmission in HVAC systems follows multiple paths from source to receiver, including airborne propagation through air spaces, structure-borne transmission through solid materials, and duct-borne propagation through ventilation systems. Understanding transmission mechanisms enables effective noise control through path interruption, barrier enhancement, and vibration isolation.

Sound energy decreases with distance from the source according to geometric spreading and atmospheric absorption. In free field conditions, sound pressure level decreases 6 dB per doubling of distance from point sources, 3 dB per doubling from line sources. Room acoustics, barriers, and absorption modify these idealized relationships.

## Airborne Sound Transmission

Airborne sound transmission occurs when acoustic pressure waves in air excite building surfaces, which vibrate and radiate sound into adjacent spaces. Transmission loss (TL) quantifies a barrier's ability to block airborne sound, expressing the ratio of incident to transmitted sound power in decibels. Mass law predicts transmission loss for homogeneous barriers: TL increases 6 dB per doubling of surface mass or frequency.

Sound Transmission Class (STC) provides single-number rating of barrier performance, derived from transmission loss measurements at 16 standard frequencies from 125-4000 Hz. STC calculation follows ASTM E413 contour method, fitting measured data to standard reference curve. Common STC ratings:

- STC 30-35: Loud speech clearly understood
- STC 40-45: Loud speech heard but not intelligible
- STC 50-55: Loud speech faintly heard
- STC 60+: Excellent isolation, loud sounds barely audible

Wall construction affects transmission loss. Single-layer gypsum board on wood studs achieves STC 35-40. Adding mass (multiple gypsum layers), absorptive cavity fill (fiberglass insulation), and mechanical decoupling (resilient channels, staggered studs) increases STC to 50-60. Double-stud walls with independent framing and separate ceiling/floor connections achieve STC 65-75.

## Structure-Borne Sound

Structure-borne sound transmission results from equipment vibration coupling into building structure, propagating through solid materials as elastic waves. Structure-borne sound travels much farther than airborne sound due to minimal absorption in solid materials. Compressional, shear, and bending waves propagate at different velocities and exhibit different attenuation characteristics.

Vibration isolation breaks the structure-borne transmission path using compliant mounts between equipment and structure. Spring isolators, elastomeric pads, and pneumatic mounts reduce transmitted force proportional to isolation efficiency:

Isolation efficiency = [1 - (f/fn)^2]^-1

Where f is excitation frequency and fn is isolator natural frequency. Isolation begins above √2 times natural frequency, increasing with frequency ratio. Select isolators with natural frequency below 0.3 times lowest excitation frequency for effective isolation.

Equipment vibration characteristics determine isolation requirements. Rotating equipment generates vibration at shaft rotational frequency and harmonics. Reciprocating compressors produce vibration at compressor speed and integer multiples. Unbalanced forces from fans and motors create synchronous vibration. Adequate isolation requires understanding excitation frequencies and force magnitudes.

## Flanking Transmission Paths

Flanking transmission circumvents direct barrier paths through indirect routes including structural connections, plenum spaces, ductwork penetrations, and back-to-back electrical outlets. Flanking reduces effective barrier performance below direct transmission loss. Laboratory STC ratings typically exceed field performance (FSTC) by 5-10 points due to flanking paths.

Common flanking paths include:

- Continuous structure connecting spaces (concrete floor slab, structural beams)
- Shared plenum above suspended ceiling or below raised floor
- Duct and pipe penetrations through barriers
- Gaps at partition perimeter, around doors, at electrical boxes
- Corridor doors serving as two-stage transmission path

Flanking path control requires attention to all transmission routes. Structurally decouple partitions using isolation joints. Extend partitions to structural deck, sealing perimeter with acoustical sealant. Wrap ductwork penetrating barriers with lead-loaded vinyl or seal with acoustical caulk. Stagger electrical outlets, avoiding back-to-back installation.

## Duct-Borne Noise

Ductwork transmits sound from fans, air handling units, and terminal devices to occupied spaces. Sound propagates through duct interior as plane waves (low frequencies) and higher-order modes (high frequencies). Duct attenuation from internal losses and wall absorption is minimal in sheet metal ducts, typically 0.1-0.3 dB per meter.

Lined ductwork provides substantial attenuation using fibrous glass or foam lining bonded to duct interior. Lining effectiveness depends on frequency, duct dimensions, and lining thickness. Typical attenuation ranges from 1-3 dB/ft at 125 Hz to 3-8 dB/ft at 2000 Hz for 1-inch lining in rectangular duct. Round duct provides less attenuation than rectangular duct of similar area due to lower perimeter-to-area ratio.

Duct silencers achieve high attenuation in compact length using parallel baffles or acoustic media filling duct cross-section. Dissipative silencers absorb sound energy using fibrous or foam materials. Reactive silencers reflect sound using impedance discontinuities, effective for low-frequency attenuation in limited space.

Duct breakout transmission occurs when sound inside ductwork radiates through duct walls into surrounding space. Thin-wall sheet metal ductwork provides minimal breakout attenuation, especially at low frequencies. Breakout increases in locations with high internal sound pressure: near fans, at duct elbows, at flow restrictions. Duct lagging with mass-loaded vinyl or lead sheet reduces breakout transmission.

## Regenerated Noise in Terminals

Air terminals, dampers, and flow control devices generate noise through turbulence and pressure reduction. Terminal sound power increases with airflow velocity and pressure drop. Diffusers and grilles create turbulent mixing noise at frequencies determined by face velocity and perforation size. High-velocity terminals concentrate noise generation in ductwork, with final attenuation occurring at discharge to room.

Regenerated noise is sound generated within ductwork by airflow, distinct from equipment sound transmitted through ducts. Sources include:

- Turbulence at elbows, dampers, and transitions
- Flow separation at abrupt area changes
- Vortex shedding from turning vanes and splitters
- Pressure reduction at terminal devices

Regenerated noise control requires aerodynamically smooth transitions, turning vanes in elbows, gradual area changes, and sufficient straight duct length for flow development. Avoid locating flow restrictions near sound-sensitive outlets.

## Duct End Reflection

Sound propagating through ductwork reflects at open terminations, with reflection coefficient depending on duct cross-sectional area and termination geometry. Small openings reflect sound efficiently, preventing sound propagation into occupied space but also preventing effective silencer performance downstream. Large openings permit sound transmission but reduce reflection, allowing silencer effectiveness.

Reflection affects low frequencies more than high frequencies. Small duct terminations may reflect frequencies below 500 Hz almost completely. This phenomenon explains why small diffuser throw distances correlate with high discharge sound levels: sound cannot escape through small neck area.

Duct branch insertion loss represents sound attenuation from main duct to branch due to impedance change at junction. Typical insertion loss ranges from 3-10 dB depending on area ratio and frequency. Branch paths provide natural attenuation reducing cross-talk between spaces served by common duct system.

## Cross-Talk Prevention

Cross-talk is sound transmission between spaces through shared ductwork. Supply and return ductwork connecting adjacent rooms can compromise privacy despite adequate partition STC. Duct cross-talk attenuation depends on duct path length, duct lining, silencers, and terminal device insertion loss.

Minimum cross-talk attenuation recommendations:

- Private offices: 45-50 dB
- Conference rooms: 50-55 dB
- Exam rooms: 55-60 dB
- Sound studios: 65+ dB

Achieve adequate attenuation using lined ductwork (3-5 dB/ft at mid-frequencies), duct length (increased path loss), and in-duct silencers where necessary. Avoid short parallel duct runs serving adjacent critical spaces. Consider separate air handling systems for acoustically critical areas.

## Plenum Return Systems

Plenum return systems use ceiling or floor cavity as return air path, eliminating return ductwork and reducing installation cost. However, plenum returns create acoustic coupling between all spaces sharing the plenum. Sound transmission through plenum depends on:

- Ceiling transmission loss (limited by weakest element)
- Sound absorption in plenum cavity
- Plenum path length between spaces
- Barriers and baffles within plenum

Fiberglass batt laid on suspended ceiling back increases plenum absorption, improving crosstalk attenuation by 5-10 dB. Extending partitions above ceiling into plenum increases path length and provides barrier. Achieving adequate attenuation in plenum returns requires careful design and may necessitate ducted returns for critical spaces.
