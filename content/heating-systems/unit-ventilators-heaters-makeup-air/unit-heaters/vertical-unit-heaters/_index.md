---
title: "Vertical Unit Heaters"
description: "Technical analysis of vertical downflow unit heaters with centrifugal fans including circulation patterns, acoustic performance, and commercial applications."
date: "2026-01-04"
weight: 2
tags: ["vertical unit heater", "centrifugal fan", "downflow heating", "commercial heating", "retail heating", "quiet unit heater"]
categories: ["Heating Systems"]
---

Vertical unit heaters discharge air downward using centrifugal fans to create floor-level circulation patterns. The design delivers quieter operation and more uniform temperature distribution compared to horizontal propeller units. Retail stores, workshops, auto service bays, fitness facilities, and other commercial spaces benefit from reduced noise levels and controlled air patterns that vertical configurations provide.

## Physical Configuration

Vertical units orient the major axis vertically with heights of 36-72 inches and widths of 24-48 inches depending on capacity. The centrifugal fan mounts at either the top or bottom of the cabinet, with corresponding differences in airflow patterns and installation requirements.

### Top Fan Configuration

Top-mounted fans draw return air from the bottom and sides of the cabinet. Air passes upward through the heating coil before entering the fan inlet. The fan discharges air upward into a plenum that redirects flow downward through a discharge cone or grille array.

This arrangement creates an "umbrella" circulation pattern. Warm air spreads radially outward from the unit center after striking the floor, covering a roughly circular area. The pattern suits open floor plans with minimal obstructions where 360° distribution benefits heating uniformity.

### Bottom Fan Configuration

Bottom-mounted fans draw air from the top and sides, passing downward through the heating coil before fan entry. The fan discharges directly downward, concentrating airflow in a columnar pattern with higher velocities than top-discharge units.

Bottom discharge penetrates the occupied zone more effectively in spaces with ceiling heights exceeding 20 feet. The concentrated flow pattern breaks through thermal stratification, delivering heat to floor level before lateral spreading occurs.

## Centrifugal Fan Characteristics

Centrifugal fans in vertical units operate at higher static pressures than propeller fans, typically 0.3-0.8 inches water gauge at rated airflow. This capability enables:

- Finer coil fin spacing (12-14 fins per inch vs 8-10 for propeller units)
- Optional filtration (MERV 8-11) without severe performance degradation
- Acoustic lining in discharge plenums
- Short duct runs for directed heating (up to 15 feet with proper sizing)

The pressure-flow relationship for centrifugal fans follows:

$$\Delta P = K \times Q^2$$

where $K$ depends on fan diameter, blade configuration, and system resistance. Unlike propeller fans where pressure capability remains minimal regardless of speed, centrifugal fans develop substantial pressure through air direction changes within the scroll housing.

## Airflow and Coverage Patterns

Vertical downflow creates different coverage geometry than horizontal discharge. The air column descends vertically, strikes the floor, and spreads radially outward. Coverage radius depends on discharge velocity, mounting height, and temperature rise.

For a unit delivering 3,000 CFM through a 2 ft × 2 ft discharge grille (4 ft² area):

$$V_{discharge} = \frac{3000}{4 \times 60} = 12.5 \text{ ft/s} = 750 \text{ FPM}$$

The air jet descends with minimal lateral spreading until striking the floor. Mounting height affects floor-level velocity and spread pattern. Higher mounting (25-30 feet) reduces floor velocity through entrainment of room air during descent. Lower mounting (15-20 feet) maintains higher floor velocities, creating faster lateral spreading.

Coverage radius approximation:

$$R_{coverage} = K \times h^{0.5} \times V_{discharge}^{0.3}$$

where $h$ is mounting height in feet, $V_{discharge}$ is discharge velocity in FPM, and $K$ is an empirical constant (typically 0.15-0.25). For h=20 ft, V=750 FPM, K=0.20:

$$R_{coverage} = 0.20 \times 20^{0.5} \times 750^{0.3} = 0.20 \times 4.47 \times 5.86 = 5.2 \text{ feet}$$

This seems too small. A more realistic approach uses manufacturer coverage data showing typical radii of 15-25 feet for standard commercial units at 20-foot mounting heights. The spread depends heavily on discharge configuration (cone angle, grille design, louver settings).

## Heating Capacity and Temperature Rise

Vertical units provide heating capacities from 30,000 to 500,000 Btu/hr depending on coil configuration and heat source. The same sensible heating equation applies:

$$Q_h = \text{CFM} \times 1.08 \times \Delta T$$

Temperature rise selection balances capacity requirements against comfort. Vertical downflow units discharge air directly into occupied zones, limiting acceptable temperature rise:

- **Retail/commercial**: 30-50°F maximum to avoid drafts
- **Workshops/service bays**: 50-70°F acceptable with proper mounting height
- **High-bay warehouses**: 70-90°F acceptable (similar to horizontal units)

Lower temperature rises require higher airflow for equivalent capacity. A 100,000 Btu/hr unit with 40°F rise:

$$\text{CFM} = \frac{100,000}{1.08 \times 40} = 2,315 \text{ CFM}$$

The same capacity with 70°F rise requires only 1,323 CFM, reducing fan energy but increasing risk of occupant discomfort from warm air streams.

## Acoustic Performance

Centrifugal fans generate less aerodynamic noise than propeller fans through lower tip speeds and enclosed scroll housings. Forward-curved centrifugal fans in vertical units typically produce 50-65 dB(A) measured at 3 feet from the discharge, suitable for:

- Retail environments (NC-40 to NC-45)
- Office areas (NC-35 to NC-40 with acoustic treatment)
- Fitness facilities (NC-40 to NC-45)
- Restaurants (NC-40 to NC-50 depending on concept)

Backward-inclined centrifugal fans reduce noise by an additional 3-5 dB through improved aerodynamic efficiency and lower tip speeds. The premium cost (15-25% higher) justifies selection in noise-sensitive applications.

Sound attenuation strategies:

- **Internal acoustic liner**: 1-2 inch fiberglass or foam liner on discharge plenum reduces noise by 3-6 dB
- **Vibration isolation**: Spring or rubber isolators prevent structure-borne noise transmission
- **Variable-speed control**: Operating at reduced speeds during low-load periods cuts noise by 6-9 dB
- **Discharge diffusers**: Perforated diffusers reduce turbulence noise compared to louvers or open cones

The sound power level relationship for centrifugal fans:

$$L_w = K_1 + 10 \log_{10}(Q) + 20 \log_{10}(\Delta P)$$

where $Q$ is flow in CFM, $\Delta P$ is static pressure in inches water gauge, and $K_1$ is a constant depending on fan type (typically 35-45 for forward-curved fans).

## Gas-Fired Vertical Units

Gas-fired vertical heaters integrate burners directly into the unit cabinet, eliminating hydronic piping. Three venting categories accommodate different building types and installation requirements.

### Atmospheric (Natural Draft) Venting

Atmospheric burners rely on buoyancy to exhaust combustion products through Type B vents or chimneys. The burner operates at slightly negative pressure relative to ambient, using natural draft for both combustion air intake and flue gas exhaust.

Thermal efficiency: 80-85% (Category I venting)

Venting requirements:
- Vertical rise: Minimum 10-15 feet for adequate draft
- Vent diameter: Sized per manufacturer tables based on capacity and rise
- Combustion air: Room air with adequate ventilation (typically 1 ft² per 100 MBH)
- Installation: Indoor locations with adequate clearances from combustibles

Atmospheric units suit buildings with existing chimneys or adequate height for vertical venting. The simplicity reduces first cost but limits efficiency and installation flexibility.

### Power Venting (Induced Draft)

Induced-draft fans overcome flow resistance in horizontal vent runs and low-rise installations. The fan mounts after the heat exchanger, maintaining combustion chamber at slightly negative pressure while forcing flue gases through the vent.

Thermal efficiency: 80-85% (Category I) or 90-95% (Category IV condensing)

Venting advantages:
- Horizontal venting: Permits sidewall venting without vertical rise requirements
- Longer vent runs: Fans overcome resistance in 50-100 foot runs
- Smaller vent diameters: Positive pressure enables smaller pipe sizes
- PVC venting: Condensing units use PVC or CPVC for low-temperature flue gases

Power venting costs $500-1500 more than atmospheric units but enables installations where natural draft cannot function.

### Separated Combustion (Direct Vent)

Separated combustion draws outdoor air for burner supply through a dedicated intake pipe, eliminating combustion air from conditioned space. A coaxial vent arrangement uses an inner flue pipe surrounded by an annular intake, simplifying wall penetrations.

Thermal efficiency: 90-95% (condensing operation standard)

Benefits:
- No indoor air consumption for combustion
- Sealed combustion chamber improves safety
- Pressure-balanced intake/exhaust prevents backdrafting
- Suitable for tight buildings without make-up air

Separated combustion represents the premium option, costing 40-60% more than atmospheric units while delivering 10-15% higher efficiency and improved safety.

## Mounting and Installation

Vertical units suspend from structural members using threaded rods or chain hangers. The mounting system must support operating weight plus service access loads:

- Equipment weight: 200-600 lbs depending on size and construction
- Live load allowance: 50-100 lbs for service personnel accessing hung units
- Seismic restraint: Lateral bracing per local codes (typically required in seismic zones)

Mounting height selection considers:

- **Floor clearance**: Minimum 7 feet to discharge grille for pedestrian safety
- **Optimal heating**: 15-25 feet for most commercial applications
- **Structural coordination**: Alignment with beam locations and adequate support
- **Service access**: Sufficient clearance for filter changes, coil cleaning, burner service

Gas-fired units require additional clearances from combustibles specified in manufacturer installation manuals, typically 36-72 inches depending on unit capacity and construction.

## Control Strategies

### Space Thermostats

Simple on-off thermostats cycle burners or open/close coil valves based on space temperature. Differential settings (typically 1-2°F) prevent rapid cycling while creating acceptable temperature variations for most applications.

### Modulating Control

Two-position control on hot water or steam coils varies output by modulating valve position. Proportional-integral (PI) controllers maintain stable space temperatures within 0.5-1.0°F of setpoint.

Gas-fired units use modulating burners varying from 20-100% of rated capacity. The turndown ratio affects efficiency (better part-load efficiency with higher turndown) and comfort (reduced cycling and temperature swings).

### Discharge Air Temperature Limiting

High-limit sensors prevent excessive discharge temperatures that cause discomfort or safety concerns. Settings typically range from 110-140°F depending on mounting height and application.

For units discharging at 8 feet above floor (low-mounting applications), limit discharge to 110-120°F to prevent discomfort from warm air contact. Units mounted at 20+ feet tolerate 130-140°F discharge temperatures since air mixes and cools before occupant contact.

## Comparison with Horizontal Units

| Characteristic | Vertical Units | Horizontal Units |
|----------------|----------------|------------------|
| Noise Level | 50-65 dB(A) | 65-75 dB(A) |
| Coverage Pattern | Circular/radial | Directional/elongated |
| First Cost | 30-50% higher | Baseline |
| Static Pressure | 0.3-0.8 in. wg | 0.05-0.15 in. wg |
| Temperature Rise | 30-70°F typical | 50-100°F typical |
| Applications | Commercial/retail | Industrial/warehouse |
| Mounting Height | 15-30 feet | 15-40 feet |

Vertical units cost more but deliver superior comfort and acoustics for occupied commercial spaces. Horizontal units remain more economical for industrial applications tolerating higher noise levels and less uniform temperature distribution.

Vertical unit heaters provide an effective middle ground between basic horizontal propeller units and fully ducted forced-air systems. The combination of centrifugal fan performance, multiple fuel options, and commercial-grade construction makes vertical units suitable for a wide range of heating applications.
