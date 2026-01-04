---
title: "Horizontal Unit Heaters"
description: "Engineering analysis of horizontal propeller fan unit heaters including throw calculations, coverage patterns, and mounting strategies for industrial applications."
date: "2026-01-04"
weight: 1
tags: ["horizontal unit heater", "propeller fan", "throw distance", "warehouse heating", "industrial heating", "unit heater mounting"]
categories: ["Heating Systems"]
---

Horizontal unit heaters use propeller fans to generate high-velocity air jets that distribute heated air across large open spaces. The configuration maximizes throw distance while minimizing equipment cost and installation complexity. Warehouses, manufacturing facilities, aircraft hangars, and agricultural buildings rely on horizontal units for economical space heating where noise levels and temperature uniformity requirements permit this approach.

## Fan and Airflow Characteristics

Propeller fans generate thrust by accelerating air axially through rotating blades. Unlike centrifugal fans that change air direction and build static pressure, propeller fans produce minimal pressure rise while delivering high volumetric flow at low power consumption.

The fan operates as a momentum device. Blade rotation imparts velocity to air molecules, creating a high-velocity jet discharged from the unit. The jet velocity depends on fan diameter, rotational speed, and blade pitch:

$$V_{discharge} = \frac{\text{CFM}}{A_{fan}} \times 1.1$$

where the 1.1 factor accounts for flow contraction at the fan outlet. For a 24-inch diameter fan (area = 3.14 ft²) delivering 4,000 CFM:

$$V_{discharge} = \frac{4000}{3.14} \times 1.1 = 1401 \text{ FPM}$$

This discharge velocity decays with distance as the jet entrains surrounding air and loses momentum. The velocity profile follows:

$$\frac{V_x}{V_0} = \frac{K}{\frac{x}{D} + K}$$

where $V_x$ is velocity at distance $x$, $V_0$ is initial discharge velocity, $D$ is fan diameter, and $K$ is an empirical constant (typically 5-7 for propeller fans).

## Throw Distance Engineering

Throw distance defines the horizontal length where discharge velocity decays to 50 FPM, the threshold for perceptible air motion. Beyond this point, air has mixed sufficiently with room air that buoyancy dominates and heated air rises toward the ceiling.

The empirical throw equation commonly used for horizontal propeller units:

$$L_{throw} = K \times \sqrt{\frac{\text{CFM}}{\Delta T}}$$

where $K$ ranges from 15-25 depending on fan design, discharge configuration, and mounting details. For K=20, CFM=4000, ΔT=60°F:

$$L_{throw} = 20 \times \sqrt{\frac{4000}{60}} = 20 \times 8.16 = 163 \text{ feet}$$

This equation captures the inverse relationship between temperature rise and throw. Higher temperature rise creates greater buoyancy, reducing horizontal throw distance. The square root relationship shows that doubling airflow increases throw by only 41%, while halving temperature rise increases throw by 41%.

## Coverage Area Calculations

Each unit covers a defined floor area based on throw pattern, mounting location, and discharge orientation. The coverage geometry depends on mounting configuration.

### Wall-Mounted Units

Wall mounting orients the fan perpendicular to the wall surface, discharging air horizontally into the space. The coverage pattern forms an elongated rectangle with:

- Length = throw distance (L)
- Width = 0.4 × throw distance (0.4L)
- Area = 0.4L²

For the 163-foot throw example:

$$A_{coverage} = 0.4 \times 163^2 = 10,620 \text{ sq ft}$$

Wall mounting suits perimeter heating and loading dock applications. The horizontal discharge counteracts cold air infiltration through doors and creates an air curtain effect when positioned above openings.

### Ceiling-Suspended Units

Ceiling suspension permits 360° discharge patterns or directed discharge depending on mounting hardware. Directed discharge units with louvers create an approximately circular coverage pattern. A conservative coverage factor:

- Radius = 0.5 × throw distance
- Area = π × (0.5L)²

For the 163-foot throw:

$$A_{coverage} = 3.14159 \times (0.5 \times 163)^2 = 20,876 \text{ sq ft}$$

Suspended units require adequate ceiling height for air to drop into the occupied zone after initial horizontal travel. Minimum ceiling height = 18 feet; optimal height = 24-35 feet.

## Multiple Unit Layout

Spaces exceeding single-unit coverage require multiple units with overlapping throw patterns. The layout strategy prevents cold zones while avoiding excessive overlap that wastes energy and creates drafts.

Recommended overlap = 15-25% at floor level. For units with 150-foot throw, spacing between units:

$$S = L \times (1.75 - 1.85)$$

Using the conservative factor:

$$S = 150 \times 1.75 = 262.5 \text{ feet}$$

This spacing assumes units alternate discharge directions to promote circulation. Parallel discharge (all units blowing the same direction) requires greater overlap to prevent cold zones:

$$S = 150 \times (1.4 - 1.6) = 210-240 \text{ feet}$$

Grid layouts for ceiling-suspended units use square or triangular spacing patterns:

- **Square grid**: Spacing = 1.4 × throw distance
- **Triangular grid**: Spacing = 1.6 × throw distance (provides 15% better coverage per unit)

## Mounting Height Selection

Mounting height balances throw distance maintenance, occupied zone heating, and architectural constraints. The heated air jet trajectory follows a parabolic path influenced by initial velocity, temperature rise, and mounting height.

The vertical drop distance depends on buoyancy forces and horizontal travel. As a rough approximation, air traveling 100 feet horizontally with 60°F temperature rise drops approximately 2-4 feet from the initial discharge height. High temperature rises cause greater drop; higher discharge velocities maintain horizontal trajectory longer.

A unit mounted at 20 feet discharging horizontally reaches throw distance at approximately 16-18 feet above floor. This places the terminal velocity point well above the occupied zone (typically 6 feet), allowing warmed air to mix downward gradually.

Excessive mounting height (above 35 feet) causes the heated air to rise before reaching throw distance, creating ceiling stratification. Insufficient height (below 15 feet) subjects occupants to high-velocity air causing discomfort.

## Fan Motor and Drive Selection

Propeller fans couple directly to motor shafts without belt drives. This direct-drive configuration:

- Eliminates belt maintenance and replacement
- Improves energy efficiency by 3-5% (no belt losses)
- Reduces acoustic noise from belt slap and vibration
- Limits fan speed to motor synchronous speed (1800, 1200, 900, or 720 RPM for 60 Hz power)

Motor horsepower depends on airflow and fan efficiency:

$$\text{HP} = \frac{\text{CFM} \times SP}{6356 \times \eta_{fan}}$$

For CFM = 4000, static pressure = 0.15 in. wg, fan efficiency = 45%:

$$\text{HP} = \frac{4000 \times 0.15}{6356 \times 0.45} = 0.21 \text{ HP}$$

Manufacturers standardize on 1/4, 1/3, 1/2, 3/4, or 1 HP motors. This calculation requires a 1/3 HP motor with adequate service factor (typically 1.15) for continuous operation.

Multi-speed motors enable capacity adjustment without variable-frequency drives. Three-speed motors provide high, medium, and low airflow settings, varying both CFM and throw distance. This allows seasonal adjustment: high speed for winter heating, low speed for summer circulation.

## Temperature Rise Limitations

Excessive temperature rise creates several problems:

1. **Reduced throw distance** from buoyancy effects
2. **Occupant discomfort** from high discharge temperatures
3. **Coil stress** from high leaving air temperatures (steam coils especially)
4. **Energy waste** from excessive cycling in low-load conditions

Recommended maximum temperature rise:

- **General comfort heating**: 50-70°F
- **High-bay industrial**: 70-90°F
- **Loading docks/vestibules**: 90-120°F

Temperature rise depends on heating capacity and airflow:

$$\Delta T = \frac{Q_h}{\text{CFM} \times 1.08}$$

For fixed heating capacity, increasing airflow (larger fan, higher speed) reduces temperature rise and improves throw distance at the cost of fan energy.

## Discharge Louvers and Air Pattern Control

Adjustable louvers at the discharge direct airflow horizontally, downward, or at intermediate angles. Louver adjustment enables:

- **Seasonal optimization**: Horizontal discharge for winter, downward for summer circulation
- **Architectural accommodation**: Directing air around obstructions or avoiding sensitive areas
- **Perimeter heating**: Angling discharge along exterior walls to counteract infiltration

Louvers introduce static pressure loss (0.05-0.15 in. wg) reducing airflow by 5-15% compared to free discharge. Fixed louvers minimize pressure loss; adjustable louvers provide flexibility at the cost of higher pressure drop.

## Heating Source Selection

### Steam Coils

Steam coils provide the highest capacity per unit volume. Operating at 2-15 psig steam pressure delivers saturated steam at 219-250°F, creating large temperature differentials with entering air. A compact 2-row steam coil delivers equivalent capacity to a 4-6 row hot water coil.

The high heat transfer coefficient of condensing steam (500-1000 Btu/hr-ft²-°F) enables small coil face areas. However, steam requires:

- Condensate traps and return piping
- Vacuum breakers for modulating control
- Regular trap maintenance
- Freeze protection through continuous drainage

### Hot Water Coils

Hot water coils use 140-200°F supply water with 3-6 rows and 8-12 fins per inch. The lower water temperature compared to steam requires larger face areas but simplifies control and piping.

Two-way control valves modulate flow to vary capacity while maintaining supply water temperature. Three-way valves blend supply and return water, maintaining constant flow through primary piping loops.

Freeze protection options:
- Glycol antifreeze (15-50% propylene glycol)
- Continuous low-speed circulation
- Automatic drainage valves with temperature sensors

### Gas-Fired Burners

Direct-fired gas burners eliminate hydronic piping and central boilers. Natural gas or propane combustion occurs in a tubular heat exchanger with flue gas venting to atmosphere.

Atmospheric burners achieve 80-85% thermal efficiency with Category I venting (Type B vent or chimney). Sealed combustion units with induced-draft fans reach 90-95% efficiency through condensing operation but require PVC or stainless steel venting and outdoor combustion air intake piping.

Gas piping sizing follows maximum simultaneous demand:

$$Q_{gas} = \frac{Q_{heating}}{\eta_{burner} \times \text{HHV}}$$

For 300,000 Btu/hr unit with 82% efficiency and natural gas HHV of 1020 Btu/ft³:

$$\dot{V}_{gas} = \frac{300,000}{0.82 \times 1020} = 358 \text{ ft}^3\text{/hr}$$

Gas line sizing tables determine pipe diameter based on length, pressure drop, and flow rate.

## Acoustic Considerations

Propeller fans generate 60-75 dB(A) at rated airflow depending on fan size, speed, and blade design. The noise consists primarily of:

- **Broadband aerodynamic noise** from blade turbulence
- **Tonal noise** at blade passage frequency (RPM × number of blades / 60)
- **Motor noise** from magnetic forces and bearing friction

Industrial applications typically tolerate these noise levels. Retail, office, or hospitality applications require vertical centrifugal units for reduced acoustic impact.

Sound power level approximation:

$$L_w = 10 \log_{10}(\text{CFM}) + 20 \log_{10}(\text{RPM}) - 35$$

For 4000 CFM at 1200 RPM:

$$L_w = 10 \log_{10}(4000) + 20 \log_{10}(1200) - 35 = 36 + 62 - 35 = 63 \text{ dB}$$

Distance attenuation reduces sound pressure level at occupied locations below discharge noise levels.

Horizontal unit heaters represent the most economical solution for large open spaces requiring basic heating without stringent comfort or acoustic requirements. Proper selection of capacity, fan size, mounting height, and spacing creates effective heating systems for industrial and commercial applications.
