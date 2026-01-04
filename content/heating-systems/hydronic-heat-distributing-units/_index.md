---
title: "Hydronic Heat Distributing Units"
weight: 11
description: "Comprehensive analysis of hydronic terminal units including baseboard radiation, radiators, convectors, fan coil units, and unit heaters with heat transfer physics, sizing methodologies, output rating calculations, and selection criteria for hot water and steam heating systems."
keywords: "hydronic heating, baseboard radiation, radiators, convectors, fan coil units, unit heaters, heat transfer, terminal units, hot water heating, steam heating, heat output"
---

# Hydronic Heat Distributing Units

Hydronic heat distributing units transfer thermal energy from hot water or steam to conditioned spaces through combinations of radiation, natural convection, and forced convection heat transfer. Terminal unit performance depends fundamentally on heat exchanger surface area, water-to-air temperature difference, flow rate, and the relative contributions of radiative versus convective mechanisms. Proper selection requires matching unit output characteristics to space heating requirements while considering installation constraints, control strategies, and operating water temperatures.

## Heat Transfer Fundamentals

### Combined Heat Transfer Mechanisms

Total heat output from hydronic terminal units combines multiple modes:

$$Q_{total} = Q_{radiation} + Q_{convection}$$

**Radiative component:**

$$Q_{rad} = \epsilon \sigma A F_{1-2} (T_s^4 - T_{surr}^4)$$

Where:
- $\epsilon$ = Surface emissivity (0.85-0.95 for painted surfaces)
- $\sigma$ = Stefan-Boltzmann constant (1.714×10⁻⁹ Btu/h·ft²·°R⁴)
- $A$ = Surface area
- $F_{1-2}$ = View factor (geometry dependent)
- $T_s$ = Surface temperature (°R)
- $T_{surr}$ = Surrounding surface temperature (°R)

**Convective component:**

$$Q_{conv} = h_c A (T_s - T_a)$$

Where:
- $h_c$ = Convection coefficient (Btu/h·ft²·°F)
- $T_a$ = Air temperature (°F)

**Natural convection coefficient correlation:**

$$h_c = C (\Delta T / L)^{0.25}$$

Where:
- $C$ = 0.27-0.29 for vertical surfaces, 0.12-0.15 for horizontal
- $L$ = Characteristic dimension (ft)
- $\Delta T$ = Surface-to-air temperature difference

### Terminal Unit Classification by Mechanism

**Radiation dominant (40-60% radiative):**
- Cast iron radiators
- Steel panel radiators
- Free-standing convectors (partially)

**Convection dominant (10-30% radiative):**
- Baseboard radiation (despite name)
- Cabinet convectors
- Recessed convectors

**Forced convection (5-15% radiative):**
- Fan coil units
- Unit heaters
- Kickspace heaters

## Output Rating Methodology

### Standard Rating Conditions

**Hot water systems (per IBR/AHRI standards):**
- Average water temperature: 215°F (high), 170°F (medium), 150°F (low)
- Entering room air: 65°F
- Water temperature drop: 20°F typical
- Water flow rate: Adequate to maintain rating conditions

**Steam systems:**
- Steam pressure: 2 psig (219°F) typical
- Condensate removal: Adequate trap sizing
- Entering room air: 65°F

### Temperature Correction Factors

Actual output deviates from rated output based on operating conditions:

$$Q_{actual} = Q_{rated} \times CF_{temp} \times CF_{altitude}$$

**Temperature correction factor:**

$$CF_{temp} = \left(\frac{LMTD_{actual}}{LMTD_{rated}}\right)^{1.3}$$

**Log Mean Temperature Difference (LMTD):**

$$LMTD = \frac{(T_{in} - T_a) - (T_{out} - T_a)}{\ln\left(\frac{T_{in} - T_a}{T_{out} - T_a}\right)}$$

Where:
- $T_{in}$ = Entering water temperature
- $T_{out}$ = Leaving water temperature
- $T_a$ = Room air temperature

**Example calculation:**
- Rated: 215°F avg, 20°F ΔT → 225°F entering, 205°F leaving, 65°F air
- LMTD_rated = (225-65) - (205-65) / ln((225-65)/(205-65)) = 20 / ln(1.143) = 149.2°F
- Actual: 180°F avg, 20°F ΔT → 190°F entering, 170°F leaving
- LMTD_actual = (190-65) - (170-65) / ln((190-65)/(170-65)) = 20 / ln(1.190) = 115.4°F
- CF_temp = (115.4/149.2)^1.3 = 0.72

Output reduced to 72% of rated value.

### Altitude Correction

Reduced air density at altitude decreases natural convection:

$$CF_{altitude} = \left(\frac{\rho_{altitude}}{\rho_{sea level}}\right)^{0.5}$$

**Approximate:**
- 1000 ft: CF = 0.98
- 2500 ft: CF = 0.94
- 5000 ft: CF = 0.88
- 7500 ft: CF = 0.82

## Terminal Unit Comparison

| Unit Type | Heat Output Range | Water Temp | Radiation % | Installation | Control Responsiveness |
|-----------|-------------------|------------|-------------|--------------|----------------------|
| Baseboard | 400-800 Btu/h·ft | 180-200°F | 15-25% | Wall-mounted | Slow (30-60 min) |
| Cast iron radiator | 100-200 Btu/h·ft² EDR | 180-215°F | 50-60% | Free-standing/wall | Slow (45-90 min) |
| Steel panel radiator | 30-80 Btu/h·ft² | 160-180°F | 40-50% | Wall-mounted | Medium (20-40 min) |
| Cabinet convector | 1000-3000 Btu/h·ft | 180-200°F | 20-30% | Recessed/surface | Medium (15-30 min) |
| Fan coil unit | 200-800 Btu/h·ft² | 140-180°F | 10-15% | Floor/ceiling | Fast (5-15 min) |
| Unit heater | 30-300 MBH | 140-200°F | 5-10% | Suspended | Fast (5-10 min) |
| Kickspace heater | 3-12 MBH | 140-180°F | 5-10% | Under-cabinet | Fast (3-8 min) |

## Selection Criteria

### Load Matching

**Envelope-dominated loads (perimeter zones):**
- Continuous output devices: baseboard, radiators, convectors
- Distributed along exterior walls
- Match window/wall heat loss distribution

**Ventilation-dominated loads (interior zones):**
- Fan coil units for combined heating/ventilation
- Unit heaters for large open spaces
- Centralized or distributed based on ceiling height

### Space Constraints

**Limited wall space:**
- Recessed convectors (utilize cavity space)
- Trench heaters (perimeter applications)
- Ceiling-mounted fan coils

**Low headroom:**
- Baseboard radiation
- Wall-mounted radiators/convectors
- Low-profile fan coils

**High ceilings (>14 ft):**
- Unit heaters (downward air throw)
- Avoid baseboard/radiators (excessive stratification)

### Water Temperature Availability

**High temperature systems (180-200°F):**
- Compatible with all terminal types
- Required for steam conversion (radiators)
- Optimal for baseboard, convectors

**Medium temperature (140-160°F):**
- Requires larger surfaces: oversized radiators, longer baseboard
- Well-suited to fan coils, unit heaters
- Condensing boiler compatible

**Low temperature (110-130°F):**
- Radiant panels only
- Not suitable for convective terminals
- Requires significantly increased surface area

### Control Requirements

**Zone control:**
- Individual room: TRVs on radiators, line voltage thermostats on baseboard
- Multi-room: Central zone valves, common baseboard loop
- Multiple zones: Fan coils with individual controls

**Response time needs:**
- Fast (intermittent occupancy): Fan coils, unit heaters
- Medium (scheduled occupancy): Convectors, steel radiators
- Slow (continuous occupancy): Cast iron radiators, baseboard

## Browse Terminal Unit Types

- **[Baseboard Radiation](./baseboard-radiation/)** - Fin-tube elements, enclosure design, output ratings per linear foot, series and parallel piping configurations, sizing methodology, and installation practices
- **[Radiators](./radiators/)** - Cast iron column and sectional radiators, steel panel radiators, EDR ratings, steam and hot water applications, and sizing calculations
  - **[Cast Iron Radiators](./radiators/cast-iron-radiators/)** - Column radiators, tube-type radiators, sectional construction, EDR rating methodology, and steam versus hot water operation
  - **[Steel Panel Radiators](./radiators/steel-panel-radiators/)** - Single/double/triple panel configurations, integral convection fins, connection types, TRV integration, and European design standards
- **[Convectors](./convectors/)** - Cabinet convectors, recessed convectors, free-standing units, finned tube elements, enclosure configurations, and damper control
- **[Fan Coil Units](./fan-coil-units/)** - Horizontal and vertical units, heating mode operation, multi-speed controls, two-pipe and four-pipe systems, and capacity ratings
- **[Unit Heaters (Hydronic)](./unit-heaters-hydronic/)** - Propeller fan units, centrifugal fan units, steam and hot water coils, mounting configurations, and high-bay applications
- **[Specialty Terminal Units](./specialty-terminal-units/)** - Kickspace heaters, trench heaters, toe-kick heaters, valance heating units, and architectural applications

## Piping System Integration

### Supply and Return Connections

**Series loop (one-pipe with diverters):**
- Each terminal on main loop
- Diverter fittings direct partial flow through unit
- Temperature decreases progressively through loop
- Limited to small systems (<200 ft loop)

**Two-pipe direct return:**
- Separate supply and return mains
- Each terminal has individual supply/return
- Variable return path lengths (flow imbalance potential)
- Requires careful balancing

**Two-pipe reverse return:**
- Equal total pipe length for all terminals
- Inherently balanced system
- Higher piping cost
- Preferred for uniform loads

**Primary-secondary:**
- Terminal circuits on secondary loops
- Decoupled from primary distribution
- Allows different flow rates, temperatures
- Optimal for diverse terminal types

### Flow Rate Requirements

Terminal unit flow depends on temperature drop and load:

$$\dot{m} = \frac{Q}{c_p \Delta T}$$

For water ($c_p$ = 1.0 Btu/lb·°F, ρ = 8.33 lb/gal):

$$GPM = \frac{Q (Btu/h)}{500 \times \Delta T (°F)}$$

**Typical design temperature drops:**
- High temperature systems: 20°F (standard rating basis)
- Medium temperature: 15-20°F
- Low temperature radiant: 10-15°F
- Fan coils: 15-25°F (higher acceptable with forced convection)

**Example:** 48 ft baseboard @ 600 Btu/h·ft = 28,800 Btu/h
- GPM = 28,800 / (500 × 20) = 2.88 GPM

### Pressure Drop Considerations

Terminal unit pressure drop affects system pump sizing:

$$\Delta P = f \frac{L}{D} \frac{\rho v^2}{2g_c} + K \frac{\rho v^2}{2g_c}$$

**Typical pressure drops:**
- Baseboard (per 100 ft): 0.5-1.5 ft head
- Cabinet convector: 0.5-2.0 ft head
- Fan coil unit: 2-5 ft head
- Unit heater: 3-8 ft head

**System impact:** Sum terminal pressure drops with piping to determine total dynamic head for pump selection.

## Installation and Maintenance

### General Installation Practices

**Location:**
- Beneath windows or along exterior walls (counteract cold surface radiation)
- Maintain clearances to furniture, drapes (air circulation)
- Accessible for maintenance (valve operation, bleeding)

**Piping connections:**
- Pitch horizontal runs for air venting (1/4 in per 10 ft toward vent)
- Install isolation valves for service
- Provide union or flange for unit removal
- Air vents at high points

**Controls integration:**
- Thermostatic radiator valves (TRVs) for individual room control
- Zone valves for multi-room control
- Aquastats or outdoor reset for supply temperature
- Limit controls for freeze protection

### Maintenance Requirements

**Routine (seasonal):**
- Bleed air from units and piping
- Check for leaks at connections
- Clean surfaces (dust reduces output 10-20%)
- Verify control operation

**Periodic (annual):**
- Water treatment analysis and adjustment
- Inspect for corrosion
- Test pressure relief devices
- Balance system flows

**Long-term:**
- Repaint surfaces (maintain emissivity)
- Replace gaskets and seals
- Upgrade controls for efficiency

---

*Hydronic heat distributing units provide flexible, efficient space heating through diverse terminal configurations, each with characteristic heat transfer mechanisms, output ratings, and application suitability. Proper selection integrates thermal performance analysis with installation constraints and control requirements to achieve effective heating system design.*
