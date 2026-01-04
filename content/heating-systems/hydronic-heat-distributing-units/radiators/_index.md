---
title: "Radiators"
weight: 2
description: "Technical analysis of hydronic radiators including cast iron column and sectional radiators, steel panel radiators, EDR rating methodology, radiation and convection heat transfer mechanisms, steam and hot water applications, sizing calculations, and thermostatic radiator valve integration."
keywords: "radiators, cast iron radiators, steel panel radiators, EDR ratings, equivalent direct radiation, radiator sizing, hot water radiators, steam radiators, column radiators, panel radiators"
---

# Radiators

Radiators transfer thermal energy from steam or hot water to conditioned spaces through combined radiation (40-60% of total) and natural convection (40-60%), with heat output rated in terms of Equivalent Direct Radiation (EDR) for steam systems or Btu/h for hot water applications. Unlike predominantly convective terminals like baseboard, radiators emit significant radiant energy that directly warms surfaces and occupants, creating thermal comfort at lower air temperatures. Performance depends on radiator surface area, surface temperature, emissivity, view factors to surrounding surfaces, and the natural convection airflow pattern around the unit.

## Heat Transfer Mechanisms

### Radiation Component

Radiative heat transfer follows Stefan-Boltzmann relationship modified for real surfaces:

$$Q_{rad} = \epsilon \sigma A F_{1-2} (T_s^4 - T_{surr}^4)$$

Where:
- $\epsilon$ = Surface emissivity (0.90-0.95 for painted cast iron/steel)
- $\sigma$ = Stefan-Boltzmann constant (1.714×10⁻⁹ Btu/h·ft²·°R⁴)
- $A$ = External surface area (ft²)
- $F_{1-2}$ = View factor (geometry and location dependent)
- $T_s$ = Surface temperature (°R = °F + 460)
- $T_{surr}$ = Surrounding surface temperature (°R)

**Typical radiative fractions:**
- Free-standing cast iron: 50-60% radiation
- Wall-mounted cast iron: 45-55% radiation (wall blocks rear radiation)
- Steel panel (single): 40-50% radiation
- Steel panel (double/triple): 35-45% radiation (more convection)

### Natural Convection Component

Convection from vertical surfaces:

$$Q_{conv} = h_c A (T_s - T_a)$$

Convection coefficient for natural convection:

$$h_c = C \left(\frac{\Delta T}{L}\right)^{0.25}$$

Where:
- $C$ = 0.27-0.29 for vertical surfaces (Btu/h·ft²·°F)
- $\Delta T$ = Surface-to-air temperature difference (°F)
- $L$ = Characteristic height (ft)

**Multi-column radiators:**

Air flows between columns creating chimney effect:

$$\dot{m}_{air} \propto \sqrt{H \Delta \rho}$$

Narrower column spacing increases velocity but may restrict flow. Optimal spacing: 1.5-2.5 inches between columns.

### Combined Performance

Total output combines both mechanisms operating simultaneously:

$$Q_{total} = Q_{rad} + Q_{conv}$$

For typical cast iron radiator at 215°F surface temperature, 70°F air, 65°F surrounding surfaces:
- Radiation: 55-65 Btu/h·ft² EDR
- Convection: 50-60 Btu/h·ft² EDR
- Total: ~240 Btu/h·ft² EDR (standard rating basis)

## Equivalent Direct Radiation (EDR)

### EDR Definition and Rating Basis

**EDR** = square feet of equivalent direct radiation, defined as surface area that delivers 240 Btu/h under standard steam conditions.

**Standard steam rating conditions:**
- Steam pressure: 1 psig (215°F)
- Surrounding air: 70°F
- No enclosure or restrictions
- Adequate condensate removal

**One square foot EDR = 240 Btu/h**

This allows simple radiator sizing: total building EDR requirement equals heat loss divided by 240.

### Hot Water EDR Conversion

Hot water radiators use same physical units (EDR) but require correction for lower water temperature:

$$EDR_{hot water} = EDR_{steam} \times \left(\frac{T_{w,avg} - T_a}{215 - 70}\right)^{1.3}$$

**Example conversion factors (entering air 70°F):**

| Average Water Temp | EDR Output Factor | Btu/h per ft² EDR |
|-------------------|-------------------|-------------------|
| 215°F | 1.00 | 240 |
| 200°F | 0.82 | 197 |
| 190°F | 0.71 | 170 |
| 180°F | 0.61 | 146 |
| 170°F | 0.52 | 125 |
| 160°F | 0.43 | 103 |

**Example:** 10 ft² EDR radiator on 180°F hot water system
- Output = 10 × 146 = 1,460 Btu/h (compared to 2,400 Btu/h on steam)

## Radiator Types Comparison

| Type | EDR/Section or Unit | Mass (lb/section) | Water Content (gal/section) | Radiation % | Typical Application |
|------|---------------------|-------------------|-----------------------------|-------------|---------------------|
| Cast iron 2-column | 1.5-3.0 ft² | 12-18 | 0.3-0.6 | 55-60% | Steam/hot water, residential |
| Cast iron 3-column | 2.5-4.5 ft² | 18-28 | 0.5-0.9 | 50-55% | Steam/hot water, commercial |
| Cast iron 4-column | 3.5-6.0 ft² | 25-40 | 0.7-1.2 | 50-55% | Large spaces, high output |
| Steel panel single | 30-50 Btu/h·ft² | 3-5 lb/ft² | 0.05-0.10 gal/ft² | 45-50% | Hot water, residential |
| Steel panel double | 50-80 Btu/h·ft² | 5-9 lb/ft² | 0.10-0.18 gal/ft² | 40-45% | Hot water, high output |
| Steel panel triple | 70-110 Btu/h·ft² | 8-14 lb/ft² | 0.15-0.25 gal/ft² | 35-40% | Hot water, very high output |

## Radiator Sizing Methodology

### Steam System Sizing

**Step 1: Calculate room heat loss**

$$Q_{loss} = UA\Delta T + \dot{V} \rho c_p \Delta T$$

Transmission + infiltration/ventilation losses.

**Step 2: Determine required EDR**

$$EDR_{required} = \frac{Q_{loss}}{240 \text{ Btu/h per ft²}}$$

**Step 3: Select radiator**

From manufacturer data, choose radiator with EDR rating ≥ required EDR.

**Example:**
- Room heat loss: 7,200 Btu/h
- Required EDR = 7,200 / 240 = 30 ft²
- Select: Cast iron 3-column, 3.5 ft² per section, 9 sections = 31.5 ft² EDR ✓

### Hot Water System Sizing

**Step 1: Calculate room heat loss** (same as steam)

**Step 2: Determine water temperature**

Based on boiler/system design:
- High temperature: 180-200°F average
- Medium temperature: 160-180°F
- Low temperature: 140-160°F

**Step 3: Calculate radiator output per ft² EDR**

$$Output = 240 \times \left(\frac{T_{w,avg} - T_a}{215 - 70}\right)^{1.3}$$

**Step 4: Determine required EDR**

$$EDR_{required} = \frac{Q_{loss}}{Output \text{ per ft² EDR}}$$

**Step 5: Select radiator**

**Example:**
- Room heat loss: 7,200 Btu/h
- Water temperature: 180°F average (190°F supply, 170°F return)
- Output per ft² EDR = 240 × [(180-70)/(215-70)]^1.3 = 146 Btu/h·ft²
- Required EDR = 7,200 / 146 = 49.3 ft²
- Select: Cast iron 3-column, 3.5 ft² per section, 15 sections = 52.5 ft² EDR ✓

Note: Hot water requires significantly more EDR than steam for same load.

## Installation and Placement

### Location Criteria

**Optimal placement:**
1. **Beneath windows:** Counteract cold downdraft and radiant loss from glazing
2. **Along exterior walls:** Address transmission heat loss at source
3. **Away from furniture:** Maintain clearances for airflow and radiation

**Clearances for effective operation:**
- Front: Minimum 6 in (12 in preferred) to furniture or obstructions
- Rear: 1-2 in to wall (allow air circulation, protect wall from heat)
- Top: 4-6 in to sill or shelf
- Bottom: 2-4 in above floor

**View factor considerations:**

Radiator must "see" room surfaces for effective radiation:
- Central placement: Higher view factor, more effective radiation
- Corner placement: Reduced view factor, more heat to exterior walls
- Enclosure: Significantly reduces radiant component (avoid unless necessary)

### Piping Connections

**Steam radiators:**
- Supply connection: One end or bottom
- Steam trap and drip leg: Opposite end or bottom
- Pitch toward condensate outlet: 1/4 in per 10 ft minimum
- Air vent: Opposite end from steam supply (automatic or manual)

**Hot water radiators:**
- Two-pipe: Supply one end/bottom, return other end/bottom
- Cross-flow preferred (supply and return at opposite ends)
- Air vent at high point (automatic vent valve)
- Isolation valves: Supply and return for service

### Thermostatic Radiator Valves (TRVs)

**Function:**

Self-contained valve modulates flow based on room temperature:

$$\text{Flow} \propto f(T_{room}, T_{setpoint})$$

**Benefits:**
- Individual room temperature control
- Automatic response to solar gains, occupancy
- Energy savings: 10-20% typical in multi-room systems
- No wiring required (self-powered)

**Limitations:**
- Slow response (thermal mass of sensing element)
- Should not be used in room with main thermostat (control conflict)
- Requires minimum differential pressure for closure
- Cannot increase output beyond radiator capacity

**Installation:**
- Horizontal orientation preferred (faster response)
- Away from radiator (avoid false sensing of radiator temperature)
- Away from drapes, furniture (sense room air, not localized)

## Browse Radiator Types

- **[Cast Iron Radiators](./cast-iron-radiators/)** - Column radiators, tube-type radiators, sectional construction, EDR ratings per section, steam and hot water applications, assembly and installation
- **[Steel Panel Radiators](./steel-panel-radiators/)** - Single, double, and triple panel configurations, integral convection fins, compact design, connection types, TRV integration, European design standards

## Performance Factors

### Surface Temperature Effects

Radiator surface temperature depends on heating medium and flow configuration:

**Steam:**
- Surface temperature ≈ steam temperature (excellent thermal contact)
- 215°F at 1 psig (typical residential)
- 219°F at 2 psig (typical commercial)
- Very uniform temperature across entire radiator

**Hot water:**
- Surface temperature < water temperature (thermal resistance)
- Temperature drop from supply to return end
- Average surface temperature used for rating

$$T_{s,avg} = T_{w,avg} - \Delta T_{film}$$

Where $\Delta T_{film}$ = 5-15°F depending on flow rate and radiator mass.

### Thermal Mass and Response

**Cast iron radiators:**
- High thermal mass (12-40 lb per section)
- Slow warm-up: 30-60 minutes to full output
- Slow cool-down: 45-90 minutes after flow stops
- Excellent for maintaining stable temperatures
- Poor for intermittent occupancy or setback

**Steel panel radiators:**
- Lower thermal mass (3-14 lb/ft²)
- Fast warm-up: 15-30 minutes to full output
- Fast cool-down: 20-40 minutes after flow stops
- Better for variable occupancy
- Compatible with outdoor reset and setback strategies

### Altitude and Air Temperature Effects

**Altitude correction:**

Reduced air density decreases natural convection:

$$Q_{altitude} = Q_{sea level} \times \left(\frac{\rho_{altitude}}{\rho_{sea level}}\right)^{0.5}$$

**Approximate factors:**
- Sea level: 1.00
- 2,500 ft: 0.94
- 5,000 ft: 0.88
- 7,500 ft: 0.82

**Entering air temperature:**

Standard rating at 70°F entering air. Actual output:

$$Q_{actual} = Q_{rated} \times \left(\frac{T_s - T_{a,actual}}{T_s - 70}\right)^{1.3}$$

Lower air temperature increases output; higher air temperature decreases output.

## Control Strategies

### On-Off Control

**Zone valve or circulator:**
- Simple, low-cost
- All radiators in zone operate together
- Acceptable for uniform loads

**Limitations:**
- No individual room control
- Potential for overheating rooms with solar gain or internal loads
- Single thermostat location critical

### Modulating Control

**Thermostatic radiator valves (TRVs):**
- Each radiator modulates independently
- Automatic adjustment for load variations
- No central zone control required (constant circulation)

**Supply water temperature reset:**
- Outdoor temperature-based
- Lower water temperature in mild weather
- Reduces distribution losses
- Improves comfort (reduces temperature swings)
- Compatible with condensing boilers

**Curve example:**

| Outdoor Temp | Supply Water Temp |
|--------------|-------------------|
| -10°F | 180°F |
| 0°F | 175°F |
| 10°F | 168°F |
| 20°F | 160°F |
| 30°F | 150°F |
| 40°F | 138°F |
| 50°F | 125°F |
| 60°F | 110°F (min) |

## Maintenance and Troubleshooting

### Routine Maintenance

**Annual tasks:**
- Bleed air from system (radiators and piping)
- Clean external surfaces (dust reduces output 10-15%)
- Check for leaks at connections and valves
- Verify TRV operation
- Test air vents (automatic vents)

**Multi-year:**
- Inspect for corrosion (especially steam systems)
- Water treatment analysis and adjustment (hot water)
- Repaint if surface condition deteriorating (maintain emissivity)

### Common Problems

**Inadequate heating:**
- Air trapped in radiator (bleed air vents)
- Inadequate water flow (balancing, pump capacity)
- Low water temperature (boiler setpoint, mixing valve)
- Undersized radiator (recalculate load, add capacity)

**Uneven heating across radiator:**
- Steam: Condensate not draining (check pitch, steam trap)
- Hot water: Low flow rate (increase pump speed, reduce restrictions)
- Air pockets (bleed thoroughly)

**Noise:**
- Steam: Water hammer (check pitch, condensate drainage, trap operation)
- Hot water: Flow velocity >4 ft/s (reduce pump speed, open balancing valves)
- Expansion: Secure mounting, allow for pipe expansion

**Leaks:**
- Section joints (cast iron): Tighten or re-gasket
- Connections: Tighten or replace gaskets/packing
- Through-corrosion: Replace radiator or section

---

*Radiators provide effective space heating through combined radiation and natural convection, with performance rated in EDR for steam or Btu/h for hot water systems. Proper selection requires matching radiator capacity to room heat loss while accounting for water temperature, altitude, and installation factors, with thermostatic radiator valves enabling individual room control for improved comfort and energy efficiency.*
