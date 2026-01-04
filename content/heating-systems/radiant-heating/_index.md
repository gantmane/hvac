---
title: "Radiant Heating"
weight: 5
description: "Comprehensive coverage of radiant heating systems including hydronic radiant floor heating, electric radiant systems, radiant ceiling panels, and wall heating. Technical analysis of heat transfer fundamentals, surface temperature calculations, thermal mass effects, and control strategies."
keywords: ["radiant floor heating", "hydronic radiant", "electric radiant", "radiant panels", "underfloor heating", "radiant ceiling", "radiant wall heating", "thermal mass", "surface temperature limits"]
---

# Radiant Heating

Radiant heating systems transfer thermal energy directly to building occupants and surfaces through electromagnetic radiation, fundamentally different from convective heating systems that warm air. This direct energy transfer produces superior thermal comfort at lower operative temperatures, reducing heating energy consumption while eliminating air movement and associated dust circulation.

## Heat Transfer Fundamentals

### Radiative Heat Exchange

Radiant heat transfer between two surfaces follows the Stefan-Boltzmann law modified for real surfaces:

$$q = \sigma \varepsilon_1 \varepsilon_2 A F_{1-2} (T_1^4 - T_2^4)$$

Where:
- $q$ = heat transfer rate (W)
- $\sigma$ = Stefan-Boltzmann constant (5.67 × 10⁻⁸ W/m²·K⁴)
- $\varepsilon_1, \varepsilon_2$ = surface emissivities (dimensionless)
- $A$ = surface area (m²)
- $F_{1-2}$ = view factor between surfaces
- $T_1, T_2$ = absolute surface temperatures (K)

For small temperature differences typical in radiant heating (10-30°C above ambient), linearized approximation provides adequate accuracy:

$$q = h_r A (T_s - T_a)$$

Where $h_r$ = radiative heat transfer coefficient (W/m²·K), typically 5-6 W/m²·K for building surfaces.

### Combined Heat Flux

Radiant surfaces transfer heat through both radiation and convection. Total heat flux from a heated surface:

$$q'' = h_c (T_s - T_a) + h_r (T_s - T_{mrt})$$

Where:
- $q''$ = heat flux per unit area (W/m²)
- $h_c$ = convective heat transfer coefficient (W/m²·K)
- $T_s$ = surface temperature (°C)
- $T_a$ = air temperature (°C)
- $T_{mrt}$ = mean radiant temperature of surrounding surfaces (°C)

**Convective coefficients by surface orientation:**
- Floor (upward heat flow): $h_c$ = 4.3 W/m²·K
- Ceiling (downward heat flow): $h_c$ = 0.7 W/m²·K
- Vertical walls: $h_c$ = 2.5 W/m²·K

Floor systems exhibit higher convective heat transfer, requiring lower surface temperatures to deliver equivalent heat output compared to ceiling systems.

## Surface Temperature Calculations

### Required Surface Temperature

For a given heating load, required surface temperature:

$$T_s = T_a + \frac{q''}{h_c + h_r}$$

**Example calculation:** Floor system delivering 80 W/m² with $T_a$ = 20°C:

$$T_s = 20 + \frac{80}{4.3 + 5.5} = 20 + 8.2 = 28.2°C$$

This surface temperature provides comfortable radiant heating without excessive warmth underfoot.

### Temperature Limits by Surface Type

| Surface Location | Maximum Temperature | Comfort Criterion | Typical Operating Range |
|-----------------|---------------------|-------------------|------------------------|
| Occupied floor zones | 29°C (84°F) | ASHRAE 55 limit | 23-27°C (73-81°F) |
| Perimeter floor zones | 35°C (95°F) | Near exterior walls | 27-32°C (81-90°F) |
| Ceiling panels | 40°C (104°F) | Head comfort | 30-38°C (86-100°F) |
| Wall panels | 40°C (104°F) | Touch temperature | 30-38°C (86-100°F) |
| Bathroom floors | 33°C (91°F) | Enhanced comfort | 28-32°C (82-90°F) |

Temperature limits prevent thermal discomfort (warm feet, cool head) and ensure safe touch temperatures for building occupants.

## System Types Comparison

### Performance Characteristics

| Parameter | Floor Radiant | Ceiling Radiant | Wall Radiant |
|-----------|--------------|-----------------|--------------|
| Heat output capacity | 80-120 W/m² | 60-100 W/m² | 80-100 W/m² |
| Response time | Slow (2-6 hours) | Fast (15-30 min) | Medium (1-2 hours) |
| Thermal mass benefit | High | Low | Medium |
| Convective component | 50% | 20% | 35% |
| Radiative component | 50% | 80% | 65% |
| Surface temperature | 23-29°C | 30-40°C | 30-38°C |
| Furniture interference | Minimal | None | Moderate |
| Occupied zone comfort | Excellent | Good | Very good |
| Installation complexity | High | Low | Medium |

### Hydronic vs Electric Radiant

| Characteristic | Hydronic Systems | Electric Systems |
|----------------|------------------|------------------|
| Heat distribution medium | Hot water (35-55°C) | Resistance cables/mats |
| Installation cost | High | Medium to low |
| Operating cost | Low (with efficient boiler) | High (electric resistance) |
| Response time | Slower (fluid thermal mass) | Faster (direct heating) |
| Zoning capability | Good (manifold controls) | Excellent (individual circuits) |
| Retrofit suitability | Difficult | Good (low profile) |
| Heat source options | Boiler, heat pump, solar | Electric only |
| Typical applications | Whole-building heating | Supplemental, bathrooms |
| Floor buildup thickness | 75-150 mm | 3-25 mm |
| Maintenance requirements | Moderate (pumps, valves) | Minimal |

## Thermal Resistance and Floor Coverings

### Resistance Network Analysis

Heat flow from hydronic tubing to floor surface encounters series thermal resistances:

$$R_{total} = R_{tube} + R_{concrete} + R_{underlayment} + R_{flooring}$$

Total resistance determines temperature drop between supply water and surface:

$$\Delta T = q'' \cdot R_{total}$$

### Floor Covering Impact

| Floor Covering | R-value (m²·K/W) | Temperature Drop at 80 W/m² | Suitability |
|----------------|------------------|----------------------------|-------------|
| Tile/stone (10mm) | 0.01 | 0.8°C | Excellent |
| Engineered wood (12mm) | 0.08 | 6.4°C | Good |
| Solid hardwood (19mm) | 0.12 | 9.6°C | Fair (requires higher ΔT) |
| Carpet + pad | 0.15-0.25 | 12-20°C | Poor (limits output) |
| Laminate (8mm) | 0.05 | 4.0°C | Good |
| Vinyl/LVT (5mm) | 0.03 | 2.4°C | Very good |

High-resistance floor coverings (carpet, thick hardwood) require significantly higher supply water temperature to maintain surface temperature, reducing system efficiency and potentially exceeding temperature limits.

## Thermal Mass Effects

### Heat Storage Capacity

Concrete slabs provide thermal energy storage that decouples heat input from heat output:

$$Q = \rho V c_p \Delta T$$

Where:
- $Q$ = stored thermal energy (J)
- $\rho$ = concrete density (2300 kg/m³)
- $V$ = slab volume (m³)
- $c_p$ = specific heat (880 J/kg·K)
- $\Delta T$ = temperature change (K)

**Example:** 100 m² × 100 mm slab warming 5°C stores:

$$Q = 2300 \times 10 \times 0.88 \times 5 = 101,200 \text{ kJ}$$

This thermal mass provides load shifting capability for time-of-use electricity rates.

### Response Time Characteristics

Time constant for radiant slab systems:

$$\tau = \frac{\rho c_p L^2}{k}$$

Where:
- $L$ = slab half-thickness (m)
- $k$ = thermal conductivity (1.4 W/m·K for concrete)

For 100 mm slab: $\tau$ ≈ 3.6 hours

Thermal mass creates time lag between heat input and surface temperature response, requiring anticipatory control strategies.

## Control Strategies

### Outdoor Reset Control

Supply water temperature adjusts based on outdoor temperature following reset curve:

$$T_{supply} = T_{design} - \frac{T_{design} - T_{min}}{T_{outdoor,design} - T_{balance}} (T_{outdoor} - T_{outdoor,design})$$

Where:
- $T_{design}$ = design supply temperature at design outdoor conditions
- $T_{min}$ = minimum supply temperature at balance point
- $T_{outdoor,design}$ = outdoor design temperature
- $T_{balance}$ = balance point temperature (no heating required)

Outdoor reset compensates for thermal mass lag and reduces overheating during mild weather.

### Slab Temperature Limiting

Embedded sensors monitor slab temperature directly, preventing surface temperature violations:

$$T_{slab,max} = T_{comfort} + \Delta T_{safety}$$

Control logic:
1. Primary control: Outdoor reset determines supply temperature
2. Override: Slab sensor limits maximum temperature
3. Safety: High-limit cutoff prevents damage

### Zoning Approaches

**Manifold zoning (hydronic):**
- Individual zone actuators on manifold
- Thermostatic or mixing valve control
- Room-by-room temperature regulation

**Circuit zoning (electric):**
- Separate thermostats per heated area
- Line voltage or low-voltage control
- Programmable setback capability

## Comfort and Energy Efficiency

### Thermal Comfort Analysis

Operative temperature experienced by occupants:

$$T_o = \frac{h_c T_a + h_r T_{mrt}}{h_c + h_r}$$

Radiant systems elevate mean radiant temperature ($T_{mrt}$), allowing lower air temperature while maintaining thermal comfort. For sedentary occupants, each 1°C increase in $T_{mrt}$ permits 1°C reduction in air temperature.

**Comfort advantages:**
- Reduced air temperature minimizes stratification
- Elimination of forced air movement
- Even temperature distribution
- Enhanced perimeter comfort near cold surfaces

### Energy Savings Mechanisms

**1. Lower operative temperature requirement:**
- Air temperature reduction: 2-3°C below convective systems
- Heating energy savings: 10-15% per °C reduction

**2. Reduced distribution losses:**
- Lower water temperature (35-45°C vs 60-80°C for radiators)
- Reduced piping heat loss
- Condensing boiler operation range

**3. Thermal mass load shifting:**
- Nighttime charging with off-peak electricity
- Solar thermal integration
- Demand response capability

**4. Elimination of duct losses:**
- No leakage to unconditioned spaces
- No thermal losses in distribution
- No fan energy (for hydronic systems)

## Design Methodology

Radiant system design follows systematic procedure:

1. **Load calculation:** Determine room-by-room heating requirements
2. **Surface area allocation:** Identify available heated surface area
3. **Heat flux determination:** Calculate required output per unit area
4. **Temperature verification:** Confirm surface temperatures within limits
5. **Tubing layout (hydronic):** Spacing, pattern, circuit length
6. **Heat source selection:** Boiler, heat pump capacity
7. **Control system design:** Reset curves, zone valves, sensors

Refer to [Design Methodology](./design-methodology/) for detailed calculation procedures.

## System Selection Criteria

### Hydronic Radiant Applications

Best suited for:
- New construction with slab-on-grade
- Whole-building primary heating
- Large heated floor areas
- Access to low-temperature heat sources
- Integration with renewable energy
- Commercial/institutional buildings

### Electric Radiant Applications

Best suited for:
- Retrofit installations
- Supplemental heating zones
- Bathrooms, kitchens, entryways
- Small heated areas (<20 m²)
- Fast response requirement
- No access to central heating plant

## Related Topics

Explore detailed implementation approaches:

- **[Hydronic Radiant Systems](./hydronic-radiant/)** - Water-based distribution, tubing types, manifolds
  - [Floor Heating](./hydronic-radiant/floor-heating/) - Slab, thin-slab, and below-floor installations
  - [Ceiling Heating](./hydronic-radiant/ceiling-heating/) - Panel systems, thermal comfort considerations
  - [Wall Heating](./hydronic-radiant/wall-heating/) - Embedded tubing, surface-mounted panels

- **[Electric Radiant Systems](./electric-radiant/)** - Resistance cables, heating mats, control systems

- **[Design Methodology](./design-methodology/)** - Load calculations, tubing layout, system sizing

## Performance Standards

- **ASHRAE Standard 55:** Thermal comfort limits, surface temperatures
- **ASHRAE Standard 62.1:** Ventilation requirements (radiant systems require separate ventilation)
- **ISO 7730:** Thermal environment evaluation, PMV/PPD indices
- **EN 1264:** Radiant heating systems design and installation (European)
- **ASTM F2336:** Installation of engineered wood flooring over radiant heat

---

*Radiant heating systems provide superior thermal comfort through direct energy transfer to occupants and surfaces. Proper design requires analysis of heat transfer mechanisms, thermal mass effects, and control strategies to achieve comfort while minimizing energy consumption.*
