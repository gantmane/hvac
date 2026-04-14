---
title: "Fluid Statics"
aliases: ["Fluid Statics"]
description: "Fundamental principles of fluids at rest including hydrostatic pressure, manometry, buoyancy, and pressure measurement applied to HVAC system design, tank sizing, and piping analysis."
weight: 2
---

Fluid statics addresses the behavior of fluids at rest and the forces exerted by stationary fluids on surfaces and boundaries. These principles govern pressure distribution in HVAC systems, expansion tank design, static pressure measurement, refrigerant charge calculations, and hydraulic head analysis in hydronic systems.

## Fundamental Pressure Concepts

### Pressure Definition

Pressure is the normal force per unit area exerted by a fluid on any surface in contact with it:

$$P = \frac{F}{A}$$

Where:
- P = pressure (Pa, psi, or lbf/ft²)
- F = normal force (N or lbf)
- A = area (m² or ft²)

**SI Units**: 1 Pa = 1 N/m²
**Imperial Units**: 1 psi = 144 lbf/ft²

At any point in a static fluid, pressure acts equally in all directions (isotropic property). This characteristic enables pressure measurement using taps oriented in any direction without affecting the reading.

### Absolute vs. Gauge Pressure

HVAC applications require clear distinction between pressure references:

| Pressure Type | Reference | Typical Range | HVAC Applications |
|---------------|-----------|---------------|-------------------|
| Absolute (P_abs) | Perfect vacuum | 0 to 115 psia | Refrigeration cycles, psychrometrics, steam tables |
| Gauge (P_g) | Atmospheric pressure | -14.7 to 100+ psig | Hydronic systems, duct pressure, pipe testing |
| Vacuum | Below atmospheric | 0 to 29.92 in Hg | Chiller evaporators, refrigerant evacuation |
| Differential (ΔP) | Between two points | Varies | Filter pressure drop, flow measurement, pump head |

**Relationship**:
$$P_{abs} = P_g + P_{atm}$$

At sea level: P_atm = 14.696 psia = 101.325 kPa = 29.92 in Hg = 760 mm Hg

## Pascal's Law

Pascal's law states that pressure applied to a confined fluid is transmitted undiminished to every portion of the fluid and to the walls of the containing vessel:

$$P_1 = P_2 = P_3 = ... = P_n$$

### HVAC Applications

**Hydraulic Systems**: Expansion tanks, hydraulic actuators, and pressure-relief devices rely on Pascal's law for uniform pressure distribution.

**Pressure Testing**: When pressurizing a piping system for leak testing, the applied pressure reaches all points equally, enabling comprehensive system verification.

**Closed-Loop Hydronic Systems**: Fill pressure established at the expansion tank connection point creates uniform static pressure throughout the system (modified by elevation differences).

## Hydrostatic Pressure Distribution

In a static fluid under gravitational influence, pressure increases linearly with depth:

$$P = P_0 + \rho g h$$

Where:
- P = pressure at depth h (Pa or lbf/ft²)
- P_0 = pressure at reference surface (Pa or lbf/ft²)
- ρ = fluid density (kg/m³ or lbm/ft³)
- g = gravitational acceleration (9.81 m/s² or 32.2 ft/s²)
- h = vertical depth below reference (m or ft)

**For incompressible fluids** (liquids in HVAC systems):
$$\frac{dP}{dh} = \rho g = \gamma$$

Where γ is the specific weight of the fluid.

### Pressure Head Representation

Pressure is often expressed as equivalent fluid column height:

$$h = \frac{P}{\rho g} = \frac{P}{\gamma}$$

**Common Conversions for Water (62.4 lbm/ft³)**:
- 1 psi = 2.31 ft H₂O = 27.7 in H₂O
- 1 ft H₂O = 0.433 psi
- 1 in H₂O = 0.0361 psi = 249 Pa

**For Air Systems**:
- 1 in w.c. (water column) = 0.0361 psi = 249 Pa
- Used for duct static pressure, fan performance, draft measurement

### Tall Building Hydronic Systems

In multi-story buildings, elevation significantly affects system pressure:

$$P_{bottom} = P_{top} + \rho_{water} g h_{building}$$

**Example**: 40-story building (500 ft tall) with water system:
$$\Delta P = 0.433 \text{ psi/ft} \times 500 \text{ ft} = 216.5 \text{ psi}$$

**Design Considerations**:
- Piping pressure ratings must accommodate combined fill pressure and static head
- Pump suction pressure prevents cavitation at upper floors
- Zone separation required above 150-200 ft to limit component pressure ratings
- Expansion tank location affects system pressurization strategy

## Manometry and Pressure Measurement

Manometers measure pressure differential using vertical fluid columns. The fundamental relationship derives from hydrostatic equilibrium:

$$P_A - P_B = \gamma h$$

Where h is the vertical height difference in the manometer fluid.

### U-Tube Manometer

For a U-tube manometer connecting two points:

$$P_1 - P_2 = \rho_{manometer} g h$$

**Selecting Manometer Fluid**:

| Fluid | Density (lbm/ft³) | Application | Sensitivity |
|-------|-------------------|-------------|-------------|
| Water | 62.4 | General HVAC, 0-10 in w.c. | Moderate |
| Mercury | 847 | High pressure, compact height | Low |
| Light oils | 50-55 | Low pressure, enhanced sensitivity | High |
| Colored water/alcohol | 50-60 | Visual clarity, freezing prevention | High |

### Inclined Manometer

Increases sensitivity for low-pressure measurements:

$$\Delta P = \rho g L \sin(\theta)$$

Where:
- L = length of fluid column along inclined tube
- θ = angle of inclination from horizontal

**Magnification Factor**: M = 1/sin(θ)

At 10° inclination: M = 5.76 (5.76 times more sensitive than vertical)

### Differential Pressure Applications

**Filter Pressure Drop Monitoring**:
- Clean filter: 0.10-0.20 in w.c.
- Replace at: 0.50-1.00 in w.c.
- Indicates loading and airflow restriction

**Duct Static Pressure Measurement**:
- Fan discharge static: 1-4 in w.c. (low pressure systems)
- Building pressure relative to outdoors: 0.02-0.10 in w.c.
- Stairwell pressurization: 0.05-0.10 in w.c. minimum

**Coil Pressure Drop Verification**:
- Cooling coil clean: 0.15-0.40 in w.c.
- Heating coil clean: 0.10-0.30 in w.c.
- Excessive drop indicates fouling or incorrect selection

## Barometric Pressure

Atmospheric pressure varies with elevation and weather conditions:

$$P_{atm} = P_{sea level} \left(1 - \frac{L h}{T_0}\right)^{\frac{g M}{R L}}$$

Simplified for standard atmosphere:
$$P_{atm} = 14.696 \left(1 - 6.8756 \times 10^{-6} h\right)^{5.2559}$$

Where h is elevation in feet above sea level.

### Altitude Effects on HVAC Equipment

| Elevation (ft) | Pressure (psia) | Derating Factor | Design Impacts |
|----------------|-----------------|-----------------|----------------|
| 0 (sea level) | 14.696 | 1.00 | Baseline performance |
| 2,500 | 13.21 | 0.96 | 4% capacity reduction |
| 5,000 | 12.23 | 0.92 | 8% capacity reduction, increased combustion air |
| 7,500 | 11.34 | 0.88 | 12% reduction, burner orifice changes required |
| 10,000 | 10.11 | 0.83 | 17% reduction, significant deration |

**ASHRAE 62.1 Outdoor Air Correction**:
At altitude, volumetric flow rates must increase to deliver required mass of outdoor air:

$$CFM_{altitude} = CFM_{sea level} \times \frac{P_{sea level}}{P_{altitude}}$$

## Forces on Submerged Surfaces

Hydrostatic force on a submerged surface results from pressure distribution over the surface area.

### Horizontal Flat Surface

Force magnitude:
$$F = P \cdot A = \rho g h_{centroid} \cdot A$$

Where h_centroid is the depth to the surface centroid.

**Application**: Force on horizontal tank bottom, vessel heads, floor-mounted equipment.

### Vertical Flat Surface

Total force on vertical surface extends from depth h₁ to h₂:

$$F = \frac{1}{2} \rho g (h_2^2 - h_1^2) \cdot w$$

Where w is the width of the surface.

**Center of Pressure**: Located at depth h_cp below the surface:

$$h_{cp} = \frac{2}{3} \frac{h_2^3 - h_1^3}{h_2^2 - h_1^2}$$

For a rectangular surface submerged from surface (h₁ = 0) to depth h:
$$F = \frac{1}{2} \rho g h^2 w$$
$$h_{cp} = \frac{2h}{3}$$

### HVAC Equipment Applications

**Expansion Tank Sizing**: Hydrostatic forces on tank walls determine material thickness and structural support requirements.

**Underground Storage Tanks**: Buoyancy forces when empty must be countered by anchoring or ballast weight.

**Heat Exchanger Tube Sheets**: Pressure forces on tube sheets require adequate thickness to prevent deflection and gasket leakage.

## Buoyancy and Archimedes' Principle

Any object wholly or partially immersed in a fluid experiences an upward buoyant force equal to the weight of the displaced fluid:

$$F_{buoyancy} = \rho_{fluid} g V_{displaced}$$

### Net Force on Submerged Objects

$$F_{net} = F_{buoyancy} - W_{object} = \rho_{fluid} g V - \rho_{object} g V$$

$$F_{net} = (\rho_{fluid} - \rho_{object}) g V$$

**Conditions**:
- ρ_fluid > ρ_object: Object floats
- ρ_fluid = ρ_object: Neutral buoyancy
- ρ_fluid < ρ_object: Object sinks

### Underground Tank Buoyancy

Empty tanks in saturated soil or high groundwater experience significant uplift:

**Example**: 1000-gallon underground fuel tank (42 in diameter × 120 in long)
- Volume displaced: 96.8 ft³
- Buoyant force in water: 96.8 ft³ × 62.4 lbm/ft³ = 6,040 lbf
- Tank weight (empty): ~800 lbf
- Net uplift: 5,240 lbf

**Mitigation**:
- Concrete anchoring straps
- Increased burial depth
- Deadman anchors
- Concrete encasement

### Refrigerant Liquid Level

Buoyancy principles apply to float-operated controls:
- Evaporator float valves
- Receiver liquid level controls
- Low-pressure float refrigerant feed systems

Differential density between liquid refrigerant and vapor creates buoyant force on float mechanism.

## Stability of Floating Bodies

### Metacentric Height

Metacentric height (GM) determines stability of floating equipment platforms or vessels:

$$GM = \frac{I}{V_{submerged}} - BG$$

Where:
- I = second moment of area of waterline plane
- V_submerged = volume of displaced fluid
- BG = vertical distance from center of buoyancy to center of gravity

**Stability Criteria**:
- GM > 0: Stable (restoring moment)
- GM = 0: Neutral (no restoring moment)
- GM < 0: Unstable (capsizing moment)

### HVAC Applications

**Floating Roof Tanks**: Petroleum storage, thermal storage tanks with floating covers require stability analysis.

**Rooftop Equipment Platforms**: Floating foundations on ballasted roofs must maintain stability under equipment weight distribution.

**Cooling Tower Basins**: Float-operated makeup valves rely on stable floating mechanisms.

## Pressure Measurement Devices

### Bourdon Tube Gauge

Curved tube straightens under internal pressure, driving mechanical linkage to dial indicator.

**Range**: 0-15 psi to 0-10,000 psi
**Accuracy**: ±0.5% to ±2% full scale
**Applications**: Refrigerant gauges, boiler pressure, compressed air systems

**Calibration**: ASHRAE Guideline 2 recommends annual calibration with deadweight tester or certified standard.

### Pressure Transducers

Electronic devices convert pressure to electrical signal (4-20 mA, 0-10 VDC).

**Types**:
- Strain gauge (piezoresistive)
- Capacitive diaphragm
- Piezoelectric (dynamic pressure)

**Selection Criteria**:

| Parameter | Typical Range | Design Consideration |
|-----------|---------------|----------------------|
| Accuracy | ±0.25% to ±1% FS | Critical for control, energy monitoring |
| Range | 150% of maximum expected | Prevent over-ranging damage |
| Temperature compensation | -40°F to 185°F | Maintain accuracy across ambient conditions |
| Wetted materials | 316 SS, Hastelloy | Refrigerant/fluid compatibility |

### Digital Pressure Indicators

Microprocessor-based devices provide:
- Direct digital readout (0.01 resolution)
- Multiple unit display (psi, kPa, bar, in Hg)
- Data logging capability
- ±0.05% accuracy (calibration standards)

## Design Considerations for Static Systems

### Expansion Tank Sizing

Closed hydronic systems require expansion volume accommodation:

$$V_{tank} = \frac{V_{system} \times \Delta V}{1 - \frac{P_{fill}}{P_{max}}}$$

Where:
- V_system = total system water volume
- ΔV = volumetric expansion coefficient (typically 0.04 for 40°F to 220°F)
- P_fill = fill pressure (absolute)
- P_max = maximum operating pressure (absolute)

**Acceptance Volume**: Tank must accept expanded volume without exceeding pressure relief setpoint.

**Pre-charge Pressure**: Set to fill pressure to prevent waterlogging.

### Static Pressure in Duct Systems

Proper static pressure measurement locations:

**Fan Inlet**: 2.5 duct diameters upstream, straight section
**Fan Outlet**: 5 duct diameters downstream, after flow stabilization
**Terminal Points**: Remote diffusers, critical zones

**Pitot Tube Orientation**: Face upstream for total pressure, perpendicular for static pressure tap.

### Refrigerant Charge Verification

Sight glass observation relies on static pressure-temperature relationship:

**Subcooling Method**:
$$Subcooling = T_{saturation}(P_{measured}) - T_{liquid line}$$

Target subcooling: 8-15°F for fixed orifice, 5-10°F for TXV systems.

**Superheat Method** (evaporator):
$$Superheat = T_{suction line} - T_{saturation}(P_{measured})$$

Target superheat: 8-12°F for fixed orifice, 5-8°F for TXV systems.

## Code and Standard References

**ASHRAE Handbook - Fundamentals**: Chapter 2 (Fluid Mechanics), Chapter 3 (Thermodynamics)

**ASME B40.100**: Pressure gauges and gauge attachments - specifies accuracy classes, dial sizes, connection threads.

**NFPA 54 (National Fuel Gas Code)**: Section 3.4 - Pressure testing of gas piping using static pressure decay.

**ASME BPVC Section VIII**: Pressure vessel design - governs expansion tanks, pressure vessels, heat exchanger shells.

**IMC Section 312**: Hydronic piping - requires pressure testing at 1.5 times working pressure, minimum 15 psig.

**ASHRAE Guideline 2**: Engineering Analysis of Experimental Data - pressure measurement uncertainty and calibration protocols.

## Best Practices

**Pressure Gauge Installation**:
- Install at eye level for accurate reading
- Vertical orientation with dial facing operator
- Isolation valve and snubber for pulsating service
- Pigtail siphon for steam service (protects Bourdon tube)

**Manometer Use**:
- Verify fluid level zero before measurement
- Allow stabilization time (30-60 seconds)
- Read at eye level to minimize parallax error
- Account for fluid density at measurement temperature

**System Pressurization**:
- Fill hydronic systems from lowest point
- Vent air at high points during filling
- Verify expansion tank pre-charge before system fill
- Document static pressure at reference point for future comparison

**Pressure Testing Safety**:
- Use nitrogen or air for leak testing (never oxygen or refrigerants)
- Stand clear of flanged joints during pressurization
- Limit test pressure to code requirements (typically 1.5× working pressure)
- Hold test pressure minimum 15 minutes for piping, 4 hours for vessels
- Monitor for pressure decay indicating leakage

**Altitude Corrections**:
- Adjust outdoor air quantities per ASHRAE 62.1 requirements
- Specify altitude-compensated gas valves above 2,000 ft
- Confirm equipment ratings at installation elevation
- Recalibrate draft gauges for local atmospheric pressure
