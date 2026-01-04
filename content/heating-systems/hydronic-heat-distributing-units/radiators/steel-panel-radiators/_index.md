---
title: "Steel Panel Radiators"
weight: 2
description: "Technical analysis of steel panel radiators including single, double, and triple panel configurations, integral convection fins, compact design characteristics, connection types (side, bottom, TBOE), heat output ratings, thermostatic radiator valve integration, European design standards EN 442, and low-temperature heating system compatibility."
keywords: "steel panel radiators, panel radiators, compact radiators, convector radiators, TRV, thermostatic radiator valve, EN 442, Type 11, Type 21, Type 22, Type 33, panel heating"
---

# Steel Panel Radiators

Steel panel radiators consist of welded steel sheet panels with integrated convection fins, providing compact, lightweight hydronic heating with faster thermal response than cast iron while maintaining significant radiant heat transfer (35-50% of total output). Panel configuration—designated by Type number indicating panel layers and convection fin arrangements—determines heat output per unit face area, with ratings typically 30-110 Btu/h·ft² at standard hot water temperatures. The lower thermal mass (3-14 lb/ft² compared to 40-80 lb/ft² for cast iron) enables rapid warm-up and compatibility with outdoor reset control and intermittent operation strategies.

## Panel Construction and Configurations

### Panel Type Nomenclature

European standard EN 442 defines panel types by construction:

**Type 1X:** Single panel
- **Type 10:** Single panel, no convection fins
- **Type 11:** Single panel, single convection fin layer

**Type 2X:** Double panel (two panels welded together)
- **Type 20:** Double panel, no convection fins (rare)
- **Type 21:** Double panel, single convection fin layer (between panels)
- **Type 22:** Double panel, double convection fin layers

**Type 3X:** Triple panel
- **Type 30:** Triple panel, no convection fins (rare)
- **Type 33:** Triple panel, triple convection fin layers

### Construction Details

**Panel manufacturing:**
- Cold-rolled steel sheet: 1.0-1.5 mm thickness
- Formed with horizontal water channels
- Channels: 6-10 per panel height
- Channel spacing: 4-6 in vertical
- Welded seams: Resistance welding
- Pressure rating: 145 psi (10 bar) typical

**Convection fins:**
- Sheet steel: 0.4-0.6 mm thickness
- Welded or mechanically attached to panel rear
- Fin height: 2-4 in from panel
- Fin spacing: 0.2-0.4 in
- Creates vertical airflow channels (chimney effect)

**Enclosure (optional):**
- Top grille for convective airflow outlet
- Side panels for aesthetics
- Bottom grille for air inlet
- Removable for cleaning access

## Heat Output Ratings

### Standard Rating Conditions (EN 442)

**Hot water:**
- Supply temperature: 75°C (167°F)
- Return temperature: 65°C (149°F)
- Average water temperature: 70°C (158°F)
- Room temperature: 20°C (68°F)
- ΔT = 50°C (90°F)

**Alternative rating (US practice):**
- Average water temperature: 170°F
- Room temperature: 65°F
- ΔT = 105°F

### Output per Unit Area by Type

**Typical heat output (Btu/h·ft² of face area):**

| Panel Type | Panels | Fins | Output @ ΔT=90°F | Output @ ΔT=105°F | Radiation % |
|------------|--------|------|------------------|-------------------|-------------|
| Type 10 | 1 | 0 | 28-32 | 38-43 | 50-55% |
| Type 11 | 1 | 1 | 35-42 | 47-56 | 45-50% |
| Type 21 | 2 | 1 | 50-60 | 67-80 | 42-47% |
| Type 22 | 2 | 2 | 60-75 | 80-100 | 38-43% |
| Type 33 | 3 | 3 | 85-110 | 115-145 | 35-40% |

**Heat output scaling:**

Output varies with temperature difference:

$$Q = Q_{rated} \left(\frac{\Delta T_{actual}}{\Delta T_{rated}}\right)^{1.3}$$

Where:

$$\Delta T = \frac{T_{supply} + T_{return}}{2} - T_{room}$$

**Example:** Type 22 radiator, 4 ft² face area
- Rated output @ ΔT=90°F: 70 Btu/h·ft² → 280 Btu/h total
- Actual: 180°F avg water, 70°F room → ΔT = 110°F
- Actual output = 280 × (110/90)^1.3 = 280 × 1.29 = 361 Btu/h

### Dimensional Standards

**Heights (mm/in):**
- 300 mm (12 in): Low sill applications
- 450 mm (18 in): Compact
- 600 mm (24 in): Standard residential
- 750 mm (30 in): High output
- 900 mm (36 in): Commercial

**Lengths:**
- Standard: 400-3000 mm (16-118 in) in 100 mm increments
- Custom lengths available
- Depth (panel + fins): 50-160 mm (2-6.5 in) depending on type

## Connection Types

### Side Connections (TBSE - Top Bottom Same End)

**Configuration:**
- Supply and return on same end of radiator
- Top connection: Supply (hot water rises)
- Bottom connection: Return
- 15 mm or 1/2 in connections typical

**Advantages:**
- Simple piping
- Concealed piping behind radiator
- Standard for most installations

**Disadvantages:**
- Slight temperature gradient across length
- Less uniform than cross-flow for wide radiators

### Bottom Connections (BOE - Bottom Opposite Ends)

**Configuration:**
- Supply one bottom end
- Return opposite bottom end
- Cross-flow through radiator
- Most uniform temperature distribution

**Advantages:**
- Maximum output for given water temperature
- Best for wide radiators (>6 ft)
- Aesthetic (no visible piping)

**Disadvantages:**
- More complex piping
- Higher installation cost

### Bottom Center Connections (BCC)

**Configuration:**
- Both connections at bottom center
- Integral manifold distributes flow
- Cleanest appearance

**Advantages:**
- Simplest appearance
- Flexible pipe routing
- Factory manifold optimizes flow

**Disadvantages:**
- Slight output penalty (5-10%)
- More expensive than side connections

## Thermostatic Radiator Valve (TRV) Integration

### TRV Function and Benefits

Self-actuating valve modulates flow based on room temperature:

$$\text{Valve Position} = f(T_{room}, T_{setpoint}, P_{differential})$$

**Operating principle:**
- Wax or liquid-filled thermal element
- Element expands with temperature increase
- Expansion closes valve, reducing flow
- Self-powered, no wiring required

**Benefits:**
- Individual room temperature control
- Automatic compensation for solar gains, occupancy
- Energy savings: 15-25% typical
- Prevents overheating from other heat sources

### TRV Installation Practices

**Valve location:**
- Supply connection (not return)
- Horizontal orientation preferred (faster response)
- Minimum 4 in from radiator body (avoid radiator heat influence)
- Free air circulation around sensing element

**Sizing:**
- Match connection size (1/2 in, 3/4 in typical)
- Adequate flow authority: ΔP_valve > 0.5 × ΔP_system
- Prevents control instability

**Settings:**
- Numbered 1-5 (or 0-5) typical
- 1 = ~10°C (50°F)
- 2 = ~15°C (59°F)
- 3 = ~20°C (68°F)
- 4 = ~24°C (75°F)
- 5 = ~28°C (82°F)
- Calibrate to actual room temperature

### System Compatibility

**TRV requirements:**
- Constant circulation (no zone valves that shut all radiators)
- Bypass or pressure relief to prevent overpressure
- Pump with adequate head for partial closure
- Boiler with outdoor reset or modulation (prevent short-cycling)

**Do not install TRV:**
- In room with main thermostat (control conflict)
- On all radiators without bypass (deadhead pump risk)
- In single-radiator systems (use thermostat instead)

## Sizing Methodology

### Design Procedure

**Step 1: Calculate room heat loss**

$$Q_{room} = UA\Delta T + \dot{V}\rho c_p \Delta T + Q_{ventilation}$$

**Step 2: Determine water temperature**

Based on system design:
- High-temp: 180-200°F average
- Medium-temp: 160-180°F
- Low-temp: 140-160°F (condensing boiler, heat pump)

**Step 3: Calculate ΔT**

$$\Delta T = T_{water,avg} - T_{room}$$

**Step 4: Determine output per ft²**

From manufacturer data or table, apply temperature correction:

$$Output = Output_{rated} \times \left(\frac{\Delta T_{actual}}{\Delta T_{rated}}\right)^{1.3}$$

**Step 5: Calculate required face area**

$$A_{required} = \frac{Q_{room}}{Output \text{ per ft²}}$$

**Step 6: Select radiator dimensions**

Choose height and length to achieve required area while fitting available space.

### Sizing Example

**Room data:**
- Heat loss: 4,800 Btu/h
- Available wall space: 6 ft length × 2 ft height max
- Water temperature: 170°F average (180°F supply, 160°F return)
- Room temperature: 70°F

**Calculation:**
1. ΔT = 170 - 70 = 100°F
2. Select Type 22 (double panel, double fin): Rated 70 Btu/h·ft² @ ΔT=90°F
3. Correction: Output = 70 × (100/90)^1.3 = 70 × 1.15 = 80.5 Btu/h·ft²
4. Required area = 4,800 / 80.5 = 59.6 ft²
5. Problem: 6 ft × 2 ft = 12 ft² available (far too small)
6. Solution options:
   - Increase water temperature to 190°F: ΔT = 120°F, Output = 70 × (120/90)^1.3 = 96 Btu/h·ft², Area = 4,800 / 96 = 50 ft² (still too large)
   - Use Type 33: Rated 100 Btu/h·ft² @ ΔT=90°F, Output @ 170°F = 115 Btu/h·ft², Area = 4,800 / 115 = 41.7 ft² (still exceeds)
   - Increase to 190°F with Type 33: Output = 100 × (120/90)^1.3 = 137 Btu/h·ft², Area = 4,800 / 137 = 35 ft² (still exceeds available 12 ft²)
   - Final: Room cannot be adequately heated with available radiator space at these water temperatures
   - Alternatives: Increase water temp to 200°F+, add second radiator location, or use forced convection (fan coil, unit heater)

This example illustrates sizing challenges with low-temperature systems and limited wall space.

## Low-Temperature Heating System Applications

### Condensing Boiler Compatibility

Steel panel radiators well-suited to low-temperature operation:

**Temperature range:**
- Conventional: 180-200°F (82-93°C)
- Condensing optimized: 140-160°F (60-71°C)
- Heat pump: 110-130°F (43-54°C) - requires significant oversizing

**Condensing boiler benefits:**
- Return temperature <130°F enables flue gas condensation
- Efficiency gain: 5-10% over non-condensing mode
- Steel radiators' fast response compatible with modulating controls

**Sizing for low temperature:**

Increased surface area required:

$$\frac{A_{low-temp}}{A_{high-temp}} = \left(\frac{\Delta T_{high}}{\Delta T_{low}}\right)^{1.3}$$

**Example:**
- High-temp: 190°F avg, 70°F room, ΔT = 120°F
- Low-temp: 140°F avg, 70°F room, ΔT = 70°F
- Area multiplier = (120/70)^1.3 = 2.0

Low-temperature system requires approximately 2× radiator surface area.

## Installation and Maintenance

### Mounting

**Wall brackets:**
- Keyhole slots on radiator back
- Brackets screwed to wall studs or masonry
- Check bracket load rating vs. radiator weight + water
- Typical spacing: Every 24-36 in horizontal

**Clearances:**
- Wall: 1-2 in (included in radiator depth)
- Floor: 4-6 in (for cleaning beneath)
- Furniture: 6-12 in front (maintain airflow)
- Curtains/drapes: Avoid contact (fire risk, blocks output)

### Piping Connections

**Valve installation:**
- Isolation valve supply side
- TRV or manual control valve
- Lockshield valve return side (balancing)
- Bleed valve top (air removal)

**Pipe sizing:**
- 1/2 in connections typical residential
- 3/4 in for larger commercial units
- Match valve connection size

### Routine Maintenance

**Annual:**
- Bleed air from system
- Clean surface (damp cloth)
- Check for leaks
- Verify TRV operation

**Multi-year:**
- Water treatment check
- Repaint if surface damage
- Inspect for corrosion

**Corrosion protection:**
- Steel panels susceptible to corrosion if water treatment inadequate
- Maintain pH 8.5-9.5
- Use corrosion inhibitor
- Closed system (no continuous oxygen ingress)

---

*Steel panel radiators provide compact, responsive hydronic heating through welded panel construction with integrated convection fins, offering multiple Type configurations optimized for different output requirements and installation constraints. Lower thermal mass enables compatibility with modern condensing boiler systems and control strategies, while TRV integration facilitates individual room temperature control and energy savings.*
