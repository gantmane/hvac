---
title: "HVAC Equipment Noise"
aliases: ["HVAC Equipment Noise"]
weight: 3
---

HVAC equipment represents the primary source of environmental noise in occupied spaces. Understanding noise generation mechanisms, quantifying sound power levels, and implementing effective mitigation strategies are fundamental to achieving acceptable acoustic environments.

## Noise Generation Fundamentals

### Sound Power vs. Sound Pressure

Sound power (Lw) represents the total acoustic energy radiated by equipment, measured in decibels referenced to 10^-12 watts. Sound power is an inherent property of the equipment, independent of the acoustic environment.

Sound pressure (Lp) represents the acoustic pressure at a specific location, measured in decibels referenced to 20 μPa. Sound pressure depends on sound power, distance from source, and room acoustics according to:

Lp = Lw - 20log(r) - 11 + 10log(Q/(4π) + 4/R)

Where:
- r = distance from source (ft)
- Q = directivity factor (1 to 8)
- R = room constant (Sα/(1-α))

### Frequency Characteristics

HVAC equipment noise is analyzed in octave bands with center frequencies of 63, 125, 250, 500, 1000, 2000, 4000, and 8000 Hz. Equipment exhibits characteristic spectral shapes based on noise generation mechanisms.

**Low-frequency dominance (63-250 Hz):**
- Compressor operation
- Fan blade passage
- Motor magnetic forces
- Structure-borne vibration

**Mid-frequency content (500-2000 Hz):**
- Turbulent airflow
- Duct-generated noise
- Mechanical friction

**High-frequency components (4000-8000 Hz):**
- Air jets and diffusers
- Throttling and pressure reduction
- Cavitation in valves

## Acoustic Rating Criteria

### NC (Noise Criteria) Curves

NC curves define maximum acceptable sound pressure levels across octave bands. Each NC curve represents a balanced spectrum where low frequencies are permitted at higher levels than high frequencies, reflecting human hearing sensitivity.

**Typical NC targets by space type:**

| Space Type | NC Rating | Application |
|------------|-----------|-------------|
| Recording studio | NC-15 to NC-20 | Critical listening environments |
| Private offices | NC-25 to NC-30 | Executive areas, conference rooms |
| General offices | NC-30 to NC-35 | Open plan, cubicles |
| Retail spaces | NC-35 to NC-40 | Shopping areas |
| Restaurants | NC-40 to NC-45 | Dining areas |
| Lobbies | NC-40 to NC-50 | Public circulation |

### RC (Room Criteria) Curves

RC criteria improve upon NC by addressing spectral balance and incorporating quality assessment descriptors. RC Mark II evaluates both sound level and spectrum shape to identify rumble, hiss, or neutral characteristics.

**RC quality assessment regions:**
- Region A: Excessive rumble (low-frequency energy)
- Region B: Acceptable neutral spectrum
- Region C: Excessive hiss (high-frequency energy)

Design targets should maintain RC values with neutral spectral balance (Region B) to avoid subjective complaints about equipment character.

### dBA Ratings

A-weighted sound levels apply frequency weighting approximating human hearing sensitivity. While dBA provides single-number ratings convenient for specifications, it obscures spectral information critical for identifying noise character and mitigation strategies.

Relationship between NC and dBA (approximate):
dBA ≈ NC + 7 to 10 (varies with spectrum)

## Fan Noise Characteristics

### Fan Sound Power Levels

Fan sound power correlates with airflow, pressure, and fan type according to empirical relationships. Total fan sound power (octave band sum) follows:

Lw ≈ Kw + 10log(Q) + 20log(Ps) + ΔLw

Where:
- Kw = specific sound power constant (fan type dependent)
- Q = airflow (CFM)
- Ps = static pressure (in. wg)
- ΔLw = installation effects

**Specific sound power constants (Kw) by fan type:**

| Fan Type | Kw Range | Noise Character |
|----------|----------|-----------------|
| Centrifugal backward-curved | 35-45 | Broadband, moderate levels |
| Centrifugal forward-curved | 45-55 | Broadband, higher levels |
| Centrifugal airfoil | 30-40 | Low broadband noise |
| Plenum | 50-65 | High broadband noise |
| Vaneaxial | 40-50 | Tonal at blade passage frequency |
| Tubeaxial | 45-60 | Strong tonal components |

### Fan Sound Spectra

Fan noise consists of broadband aerodynamic noise and discrete tonal components at blade passage frequency (BPF) and harmonics.

BPF = (RPM × Number of blades) / 60

Backward-curved and airfoil centrifugal fans exhibit relatively flat broadband spectra with minimal tonal content. Forward-curved fans generate higher broadband levels with peak energy at 250-1000 Hz. Axial fans produce strong tonal peaks at BPF, often requiring specific attenuation.

**Spectral correction factors from total sound power:**
Apply manufacturer-provided octave band distribution factors, typically ranging from -15 dB (low frequencies) to -5 dB (peak frequency band) relative to total Lw.

### Installation Effects

Fan installation significantly impacts radiated noise beyond catalog ratings:

**Inlet conditions:**
- Elbows or obstructions within 2.5 duct diameters: +5 to +10 dB
- Non-uniform inlet flow: +3 to +8 dB
- Inlet spin or swirl: +4 to +12 dB

**Outlet conditions:**
- Discharge elbows within 5 duct diameters: +3 to +7 dB
- Abrupt area changes: +4 to +10 dB

**System effect factors:**
Always account for system effect losses and associated noise increases when fans operate with non-ideal inlet/outlet configurations.

## Compressor Noise

### Reciprocating Compressors

Reciprocating compressors generate pulsating discharge flow at frequencies corresponding to cylinder firing rates. Dominant tones occur at fundamental firing frequency and harmonics, producing characteristic "chugging" sound.

Firing frequency = (RPM × number of cylinders) / (60 × revolution per cycle)

Noise levels: Lw = 90-105 dB total, with strong discrete tones 10-20 dB above broadband floor.

**Mitigation approaches:**
- Discharge mufflers tuned to firing frequencies
- Flexible connections to isolate structure-borne transmission
- Enclosures with absorptive lining
- Base isolation with minimum 95% isolation efficiency at operating frequency

### Scroll Compressors

Scroll compressors produce lower noise levels than reciprocating units with reduced tonal content. Broadband noise dominates with gentle peaks at orbiting frequency (50-60 Hz) and higher harmonics.

Noise levels: Lw = 75-85 dB total, smoother spectrum.

### Screw Compressors

Helical screw compressors exhibit strong tonal components at meshing frequency and multiples. High rotational speeds (3600+ RPM) shift dominant frequencies to 1000-4000 Hz range.

Meshing frequency = RPM × number of lobes / 60

Noise levels: Lw = 95-110 dB total for large units.

**Control measures:**
- Factory-installed enclosures (10-20 dB reduction)
- Intake and discharge silencers
- Vibration isolation mounting

### Centrifugal Compressors

Centrifugal compressors in large chillers generate broadband aerodynamic noise with potential tonal components at impeller blade passage frequency. Noise levels correlate with pressure ratio and impeller tip speed.

Noise levels: Lw = 90-100 dB for typical chillers.

## Pump Noise

Pump noise stems from multiple mechanisms operating simultaneously:

**Hydraulic noise:**
- Impeller blade passage frequency tones
- Cavitation (broad high-frequency noise)
- Flow turbulence and separation

**Mechanical noise:**
- Bearing noise (broadband)
- Coupling misalignment
- Motor magnetic forces (120 Hz and harmonics)

**Dominant frequencies:**
Blade passage: BPF = RPM × impeller vanes / 60
Motor magnetic: 2× line frequency = 120 Hz (60 Hz power)

### Noise Levels by Pump Type

| Pump Type | Sound Power Range | Frequency Character |
|-----------|-------------------|---------------------|
| End suction centrifugal | 70-85 dB | Broadband with BPF tone |
| Split-case centrifugal | 85-95 dB | Broadband, stronger BPF |
| In-line centrifugal | 75-90 dB | Motor noise dominant |
| Vertical turbine | 80-95 dB | High broadband levels |

### Cavitation Noise

Cavitation occurs when local pressure drops below vapor pressure, forming and collapsing vapor bubbles. The collapse process generates intense broadband noise extending to high frequencies (>4000 Hz) with characteristic "gravel" or "frying" sound.

**Prevention:**
- Maintain adequate net positive suction head (NPSH)
- Avoid oversized impellers
- Install suction pressure gauges for monitoring
- Provide proper inlet piping configuration

## Chiller Noise

Chiller noise combines compressor, motor, and refrigerant flow contributions with significant variation by chiller type.

### Air-Cooled Chillers

Air-cooled units generate noise from compressors, condenser fans, and refrigerant flow. Outdoor installation permits higher noise levels but requires evaluation of property line impacts and neighbor complaints.

**Typical sound power levels:**
- 10-ton unit: Lw = 85-92 dB
- 50-ton unit: Lw = 95-100 dB
- 100-ton unit: Lw = 100-105 dB

**Dominant noise sources ranked:**
1. Condenser fans (usually highest)
2. Compressors (scroll or screw)
3. Refrigerant flow noise

### Water-Cooled Chillers

Water-cooled chillers exhibit lower noise levels with compressor as primary source. Enclosed mechanical rooms provide architectural barriers but require proper room acoustic treatment.

**Typical sound power levels:**
- 100-ton centrifugal: Lw = 90-95 dB
- 100-ton screw: Lw = 95-100 dB
- 100-ton scroll: Lw = 85-92 dB

**Evaporator/condenser noise:**
Refrigerant flow through heat exchanger tubes generates broadband flow noise, particularly at high refrigerant velocities (>5 fps). Maintain design velocities and avoid oversizing to minimize flow noise.

## Cooling Tower Noise

Cooling towers represent significant outdoor noise sources affecting neighbors and site boundaries. Noise emanates from fans, water splash, and motor operation.

### Noise Components

**Fan noise (dominant):**
- Airflow through fill and louvers
- Fan blade passage tones
- Tip vortex generation
Accounts for 70-90% of total radiated noise.

**Water splash noise:**
- Droplet impact on basin water surface
- Broadband character, peaks at 1000-2000 Hz
- Increases with fall height and flow rate

**Motor/gearbox noise:**
- Magnetic forces at 120 Hz
- Gear meshing tones (if gearbox equipped)
- Generally 10-15 dB below fan noise

### Sound Power Levels

Cooling tower sound power scales with fan power and airflow:

Lw ≈ 70 + 10log(fan HP)

**Typical values:**
- 100-ton tower, single cell: Lw = 85-90 dB
- 500-ton tower, multi-cell: Lw = 95-100 dB
- 1000-ton tower installation: Lw = 100-105 dB

### Directional Characteristics

Cooling towers exhibit directional sound radiation:
- Maximum levels at fan discharge (top)
- Lower levels at air inlet sides (6-10 dB reduction)
- Minimum levels at ends (8-12 dB reduction)

Position towers considering prevailing directivity relative to noise-sensitive receptors.

## Boiler Noise

Boiler noise originates from combustion, burner fans, and induced/forced draft fans.

**Natural gas firing:**
Combustion roar at flame produces broadband noise peaking at 125-500 Hz. Turbulent mixing of fuel and air creates intense low-frequency energy.

Burner Lw = 85-100 dB (dependent on firing rate)

**Combustion air fans:**
Forced draft fans supplying combustion air and induced draft fans removing flue gas generate significant noise. Centrifugal fan characteristics apply.

**Fuel oil firing:**
Oil burners produce higher noise levels (3-8 dB above gas) due to atomization processes and higher combustion intensities.

### Boiler System Noise

**Flue noise:**
Flue gas discharge velocities exceeding 3000 fpm generate jet noise radiating from stack terminus. High-velocity discharge aims noise upward, reducing grade-level impact.

**Safety relief valves:**
Pressure relief discharge events produce extremely high noise levels (>120 dBA) for short durations. Position discharge locations away from occupied areas and consider silencers for frequent operation.

## Terminal Unit Noise

### VAV Box Noise

VAV terminal unit noise stems from damper throttling and airflow turbulence. Discharge sound power increases dramatically at low damper positions due to high-velocity flow through restricted openings.

**Radiated noise:**
VAV boxes radiate noise through casing to ceiling plenum:
Lw (radiated) = Lw (discharge) - 15 to -25 dB

Casing attenuation depends on gauge thickness and acoustic lining.

**Discharge noise:**
Maximum discharge sound power occurs at 30-50% damper position where flow velocity and turbulence peak. Fully open positions exhibit lower noise despite higher flow rates.

Specify VAV boxes with:
- Lined inlet and discharge plenums
- Acoustic lining on all interior surfaces
- Low-noise damper assemblies

### Fan-Powered Boxes

Fan-powered VAV boxes add fan noise to throttling noise. Series units run fans continuously; parallel units activate fans during heating. Select low-noise plenum fans (Lw 10-15 dB below airflow noise at design condition).

## Diffuser and Grille Noise

### Diffuser-Generated Noise

Diffusers generate noise as supply air expands from duct velocity to low room velocity. Noise increases with diffuser pressure drop and discharge velocity.

Lw (diffuser) ≈ 10log(Q) + 50log(V) - 25

Where:
- Q = airflow (CFM)
- V = discharge velocity (fpm)

**Design guidelines:**
- Limit neck velocities to 500-700 fpm for NC-30 to NC-35 spaces
- Reduce to 400-500 fpm for NC-25 or quieter
- Use larger diffusers to maintain low velocities

### Grille Noise

Return and exhaust grilles generate noise from turbulence at grille face and sudden area changes. Free area percentage significantly impacts noise generation.

**Free area effects:**
- High free area (>70%): Lower noise generation
- Low free area (<50%): Increased noise, avoid for quiet spaces

Limit return grille face velocities to 300-500 fpm for occupied spaces.

## Duct-Related Noise

### Duct Breakout Noise

Breakout noise occurs when sound energy inside ducts radiates through duct walls into occupied spaces. Sheet metal ducts provide 10-30 dB attenuation depending on gauge, frequency, and duct size.

Breakout transmission loss increases with:
- Heavier gauge metal
- Smaller duct dimensions
- Higher frequencies
- External duct lagging or acoustic barriers

**Critical locations:**
- Ducts in ceiling plenums above noise-sensitive spaces
- Exposed ducts in mechanical rooms adjacent to quiet areas
- Main supply ducts near air handling units

### Duct Break-in Noise

Break-in noise transmits from exterior sources through duct walls into ductwork, then distributing to connected spaces. Mechanical room noise breaking into supply ducts creates paths to remote locations.

**Prevention:**
- Acoustically line first 20-30 ft of ductwork leaving mechanical rooms
- Specify 20-gauge minimum for ducts in noisy environments
- Install duct silencers at mechanical room penetrations

### Plenum Radiated Noise

Supply and return plenums radiate equipment and duct noise into adjacent spaces through plenum walls, ceiling tiles, and light fixtures. Plenum sound pressure levels determine transmission magnitude.

**Mitigation:**
- Acoustical ceiling tiles (NRC 0.70-0.90)
- Seal light fixtures and penetrations
- Install duct silencers before plenums
- Add sound absorption in plenum cavity

## Equipment Sound Ratings

### Manufacturer Ratings

Equipment manufacturers provide sound power data according to standardized test procedures:

**AHRI Standards:**
- AHRI 260: Sound rating of ducted air-moving and conditioning equipment
- AHRI 270: Sound rating of outdoor unitary equipment
- AHRI 370: Sound rating of large outdoor refrigerating and air-conditioning equipment
- AHRI 575: Sound rating of non-ducted indoor air-conditioning equipment

Ratings specify octave band sound power levels (Lw) under defined operating conditions. Verify rating conditions match actual installation parameters (airflow, pressure, speed).

**Rating conditions impact:**
- Fan sound power varies as 50log(RPM)
- Doubling airflow increases Lw by approximately 8 dB
- Doubling pressure increases Lw by approximately 12 dB

### Sound Certification Programs

AHRI administers certification programs verifying published ratings through independent testing. Certified ratings provide greater reliability than uncertified catalog data.

Check certification at AHRI Directory (ahridirectory.org) for:
- Air handling units
- Rooftop units
- Chillers
- Condensing units

## Equipment Selection for Noise Control

### Acoustic Selection Criteria

Establish acoustic design criteria early in equipment selection:

1. Determine space NC or RC targets based on occupancy
2. Calculate allowable equipment sound power for planned locations
3. Select equipment meeting sound power limits
4. Verify octave band spectrum compatibility, not just total dBA
5. Account for installation effects and corrections

### Low-Noise Equipment Features

**Fans:**
- Backward-curved or airfoil centrifugal types
- Low tip speeds (<4000 fpm)
- Direct-drive motors eliminating belts
- Inlet and outlet silencers
- Vibration isolation

**Compressors:**
- Scroll over reciprocating for small capacities
- Sound enclosures (factory or field-installed)
- Discharge mufflers for reciprocating units
- Base vibration isolation

**Pumps:**
- Proper sizing avoiding oversized impellers
- Adequate NPSH margin preventing cavitation
- Flexible connections at suction and discharge
- Spring or rubber isolation mounting

**Chillers:**
- Water-cooled over air-cooled for indoor applications
- Scroll or centrifugal over screw for lower noise
- Factory sound enclosures where available
- Acoustic barriers for outdoor installations

## Noise Mitigation Strategies

### Source Treatment

Address noise at generation point before propagation:

**Equipment enclosures:**
Partial or complete enclosures with absorptive lining provide 10-25 dB reduction. Maintain ventilation openings with acoustically-lined louvers. Ensure service access for maintenance.

**Silencers and mufflers:**
Duct silencers attenuate airborne noise in supply and return systems. Select length and pressure drop based on required attenuation spectrum.

**Vibration isolation:**
Prevent structure-borne transmission through proper isolation:
- Spring isolators: 90-95% efficiency at frequencies >2× natural frequency
- Rubber isolators: 70-85% efficiency, simpler installation
- Inertia bases: Increase mass, reduce transmitted force

### Path Treatment

Interrupt transmission paths between source and receiver:

**Acoustic barriers:**
Barriers block direct sound paths but allow diffracted sound over edges. Effectiveness depends on barrier height, distance geometry, and frequency:

Barrier insertion loss ≈ 10log(3 + 20N)

Where N = Fresnel number accounting for path length difference.

**Duct lining:**
Internally-lined ducts absorb sound propagating through ductwork. Attenuation increases with:
- Lining thickness (1-2 in. typical)
- Lined perimeter (4-sided superior to 2-sided)
- Duct length (diminishing returns beyond 15-20 ft)

**Room absorption:**
Acoustical treatment in mechanical rooms reduces reverberant buildup, lowering room sound pressure levels by 3-10 dB. Apply absorption to ceiling and walls using:
- Acoustic panels (NRC 0.80-1.00)
- Spray-applied materials
- Acoustic baffles or clouds

### Receiver Protection

When source and path treatments prove insufficient:

**Space isolation:**
Construct sound-rated partitions and floor/ceiling assemblies (STC 50-60) isolating noise-sensitive areas from mechanical spaces.

**Active noise control:**
Electronic systems generating anti-phase sound waves cancel low-frequency noise in ducts. Effective for tonal components below 500 Hz, particularly variable-frequency drive fan noise.

**Administrative controls:**
Schedule noisy operations during unoccupied periods. Implement maintenance procedures preventing degraded acoustic performance over time.

## Noise Measurement and Verification

### Field Testing

Verify installed system performance through field sound measurements:

**Equipment sound power:**
Measure sound pressure at multiple locations, apply room corrections to determine equipment sound power. Compare to specified values.

**Room sound pressure:**
Measure octave band levels at representative occupied locations with systems operating. Compare to design NC/RC criteria.

**Testing standards:**
- ASTM E336: Sound transmission testing
- ASTM E1130: Objective measurement of speech privacy
- ANSI S12.51: Room sound pressure testing

### Troubleshooting Acoustic Problems

**Systematic approach:**
1. Identify complaint nature (too loud, rumble, hiss, tones)
2. Measure existing conditions documenting levels and spectra
3. Compare measurements to criteria identifying exceedances
4. Trace noise paths from equipment to occupied space
5. Evaluate source, path, and receiver treatment options
6. Implement corrections verifying improvement through re-measurement

**Common issues and solutions:**

| Problem | Likely Cause | Solution |
|---------|--------------|----------|
| Low-frequency rumble | Compressor, fan, vibration transmission | Vibration isolation, enclosure, low-frequency absorption |
| High-frequency hiss | Diffusers, throttling valves, air leaks | Reduce velocities, seal leaks, upsize diffusers |
| Tonal whine | Fan BPF, motor magnetic, pump cavitation | Silencers tuned to frequency, fix cavitation, isolate motor |
| Intermittent noise | Cycling equipment, damper movement | Soft start/stop, damper actuator isolation |
| Excessive overall level | Undersized equipment, inadequate treatment | Reduce loads, add silencers, install barriers |
