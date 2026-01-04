---
title: "Unit Heaters (Hydronic)"
weight: 5
description: "Engineering analysis of hydronic unit heaters including propeller fan and centrifugal fan configurations, steam and hot water coil design, horizontal and vertical mounting, high-bay applications, capacity ratings, throw patterns, control strategies, and industrial/commercial space heating."
keywords: "unit heaters, hydronic unit heaters, propeller fan heaters, cabinet unit heaters, steam unit heaters, hot water unit heaters, warehouse heating, industrial heating, high-bay heating"
---

# Unit Heaters (Hydronic)

Hydronic unit heaters deliver concentrated forced-convection heating through steam or hot water coils with high-capacity fans, providing output densities of 30,000-300,000 Btu/h per unit suitable for large open spaces including warehouses, manufacturing facilities, aircraft hangars, and loading docks where ceiling heights of 12-40 feet preclude effective use of perimeter terminals. The combination of finned-tube heat exchangers and propeller or centrifugal fans creates downward air throw patterns that project heated air 20-60 feet, counteracting stratification and delivering heat to occupied zones despite high mounting positions.

## Unit Heater Configurations

### Horizontal Propeller Fan Unit Heaters

**Construction:**
- Cylindrical or rectangular cabinet
- Hot water or steam coil mounted behind propeller fan
- Direct-drive or belt-drive fan motor
- Propeller diameter: 12-36 in typical
- Horizontal discharge (parallel to mounting surface)

**Airflow characteristics:**
- High volume, low static pressure
- Free delivery (no ductwork)
- Throw distance: 20-50 ft depending on size and fan speed
- Spread pattern: Cone-shaped, 30-60° divergence

**Mounting:**
- Suspended from ceiling or roof structure
- Swivel bracket allows directional adjustment
- Typical mounting heights: 12-30 ft
- Downward angle: 0-45° adjustable

**Capacities:**
- Small: 30,000-75,000 Btu/h (12-18 in fan)
- Medium: 75,000-150,000 Btu/h (18-24 in fan)
- Large: 150,000-300,000 Btu/h (24-36 in fan)

### Vertical Downblow Unit Heaters

**Construction:**
- Vertical cabinet with top-mounted heat coil
- Centrifugal blower discharging downward
- Compact footprint (12-24 in square)
- Height: 24-48 in typical

**Airflow characteristics:**
- Medium volume, medium static pressure
- Concentrated downward discharge
- Throw distance: 15-40 ft
- Narrow spread pattern (12-24 in diameter at floor)

**Mounting:**
- Suspended from ceiling
- Fixed downward discharge (typically not adjustable)
- Mounting heights: 10-25 ft typical
- Applications: Spot heating, loading docks, entrance vestibules

**Capacities:**
- Small: 20,000-50,000 Btu/h
- Medium: 50,000-100,000 Btu/h
- Large: 100,000-200,000 Btu/h

### Cabinet Unit Heaters (Centrifugal Fan)

**Construction:**
- Enclosed sheet metal cabinet
- Centrifugal blower and coil in single enclosure
- Optional duct collar for discharge
- Floor-mounted or wall-mounted

**Airflow characteristics:**
- Low to medium volume, high static pressure
- Capable of short duct runs (up to 25 ft equivalent length)
- Throw distance: 10-30 ft
- Directional grilles for throw control

**Applications:**
- Smaller spaces (shops, garages, utility rooms)
- Where ducting is beneficial
- Lower mounting heights (8-15 ft)
- Noise-sensitive applications (quieter than propeller)

**Capacities:**
- Residential/light commercial: 10,000-60,000 Btu/h
- Commercial: 60,000-150,000 Btu/h

## Coil Design and Heat Transfer

### Steam Coil Construction

**Coil configuration:**
- Copper or steel tubes with aluminum or steel fins
- Fin density: 6-10 fins per inch
- Rows deep: 1-2 rows typical
- Full condensing design (vapor in, liquid out)

**Steam supply:**
- Low-pressure steam: 2-15 psig (219-250°F)
- High-pressure steam: 15-50 psig (250-298°F) - industrial applications
- Steam pressure reducing valve if required

**Condensate removal:**
- Steam trap at coil outlet
- Pitch coil toward trap (1/4 in per foot minimum)
- Trap sizing: Adequate for condensate load plus safety factor
- Condensate return: Gravity or pumped

**Heat transfer:**

Steam provides constant temperature across coil:

$$Q = UA(T_{steam} - T_{air,avg})$$

Where:
- $U$ = 60-90 Btu/h·ft²·°F (steam to air, forced convection)
- $A$ = Coil surface area
- $T_{steam}$ = Saturation temperature at steam pressure
- $T_{air,avg}$ = (Entering air + leaving air) / 2

**Advantages of steam:**
- High heat transfer (latent heat of condensation)
- Uniform coil temperature
- Freeze protection (rapid drainage when off)
- Lower fluid volume (reduced weight)

### Hot Water Coil Construction

**Coil configuration:**
- Copper tubes with aluminum fins
- Fin density: 8-12 fins per inch
- Rows deep: 2-4 rows (more rows compensate for lower water temperature vs. steam)
- Multi-pass circuiting for velocity and heat transfer

**Water temperature:**
- High temperature: 180-200°F supply
- Medium temperature: 160-180°F supply
- Low temperature: 140-160°F supply (condensing boiler compatible)
- Design temperature drop: 20-40°F typical

**Heat transfer:**

Water temperature varies through coil:

$$Q = 500 \times GPM \times \Delta T_{water}$$

Also:

$$Q = UA \times LMTD$$

Where LMTD accounts for temperature change of both air and water streams.

**Advantages of hot water:**
- Modulating capacity control (via valve position)
- No steam trap maintenance
- Better suited to outdoor reset control
- Quieter operation (no steam flash or condensate issues)

**Freeze protection:**
- Must drain coil when off in freezing conditions
- Glycol solution alternative (reduces capacity ~10%)
- Face and bypass dampers for temperature control in mild weather

### Coil Performance and Sizing

**Coil face velocity:**

$$V_{face} = \frac{CFM}{A_{face} \times 60}$$

Typical: 400-800 FPM for unit heaters.

Higher velocity increases heat transfer coefficient but increases pressure drop and noise.

**Coil capacity:**

Approximately proportional to airflow and temperature difference:

$$Q = 1.08 \times CFM \times (T_{leaving air} - T_{entering air})$$

**Typical performance:**

| Water Temp | Entering Air | Airflow | Leaving Air | Capacity |
|------------|--------------|---------|-------------|----------|
| 180°F | 50°F | 2,000 CFM | 95°F | 97,000 Btu/h |
| 180°F | 60°F | 2,000 CFM | 100°F | 86,400 Btu/h |
| 160°F | 50°F | 2,000 CFM | 82°F | 69,000 Btu/h |

Leaving air temperature limited to avoid discomfort (typically 95-110°F maximum).

## Fan Performance and Air Distribution

### Propeller Fan Characteristics

**Fan curve:**
- High flow at zero static pressure
- Flow drops rapidly with static pressure increase
- Not suitable for ducted applications
- Efficiency: 40-60%

**Throw distance:**

Empirical relationship:

$$D_{throw} = C \times \sqrt{CFM}$$

Where $C$ = 0.8-1.2 depending on unit design.

**Example:** 2,000 CFM unit
- Throw = 1.0 × √2000 = 45 ft

**Spread pattern:**

Heated air jet expands with distance:
- At discharge: Diameter = fan diameter
- At 20 ft: Diameter ≈ 2× fan diameter
- At 40 ft: Diameter ≈ 3-4× fan diameter

**Directional control:**
- Adjust unit mounting angle (0-45° downward typical)
- Horizontal: Maximum throw, minimal downward penetration
- 45° down: Reduced throw, better occupied zone heating

### Centrifugal Fan Characteristics

**Fan curve:**
- Lower flow than propeller at zero static
- Flow more stable with static pressure
- Can overcome duct resistance
- Efficiency: 50-70%

**Air distribution:**
- More concentrated discharge
- Smaller spread angle
- Better penetration of stratified layers
- Suitable for long, narrow spaces

## Sizing and Selection Methodology

### Heat Load Calculation

**Space heating load:**

$$Q = Q_{envelope} + Q_{infiltration} + Q_{ventilation} + Q_{process}$$

**High-bay considerations:**
- Increased infiltration at loading docks, overhead doors
- Stratification losses (heat rise to ceiling)
- Process loads (equipment, product cooling)
- Pickup load for morning warm-up

**Effective heat loss:**

Account for stratification:

$$Q_{effective} = Q_{calculated} \times F_{stratification}$$

Where $F_{stratification}$ = 1.1-1.3 for ceiling heights 20-40 ft.

### Unit Selection Procedure

**Step 1: Determine space heat loss**

Include stratification factor and pickup load (20-40% for high thermal mass).

**Step 2: Determine heating medium**

Steam or hot water based on availability, control requirements, freeze protection needs.

**Step 3: Calculate number and location of units**

$$N_{units} = \frac{Q_{total}}{Q_{unit}} \times F_{safety}$$

Where $F_{safety}$ = 1.1-1.15.

Distribute units to provide uniform coverage, considering:
- Throw distance (units spaced ≤ 2× throw distance)
- Major heat loss areas (near doors, exterior walls)
- Obstruction avoidance

**Step 4: Verify throw and coverage**

Check each unit's throw reaches intended area without excessive leaving air temperature.

**Step 5: Select fan speed and control**

- Single-speed: Simple, lowest cost, on-off control only
- Two-speed: Better part-load efficiency, reduced noise during mild weather
- Variable-speed (VFD): Best efficiency, modulating capacity, quiet operation

### Sizing Example

**Warehouse:**
- Dimensions: 100 ft × 200 ft × 24 ft high
- Heat loss: 480,000 Btu/h (calculated)
- Stratification factor: 1.15
- Pickup load: 25%
- Heating: 180°F hot water available

**Calculation:**
1. Effective load = 480,000 × 1.15 × 1.25 = 690,000 Btu/h
2. Select unit size: 100,000 Btu/h capacity @ 180°F water, 50°F air
3. Number of units = 690,000 / 100,000 = 6.9 → 7 units
4. Verify coverage:
   - Unit throw ≈ 35 ft
   - Space long dimension: 200 ft
   - Maximum spacing: 2 × 35 = 70 ft
   - Minimum units along length: 200 / 70 = 2.86 → 3 rows
   - Units across width: 7 / 3 ≈ 2-3 per row
5. Layout: 3 rows of 2-3 units = 7 units total ✓

## Installation and Control

### Mounting and Suspension

**Structural support:**
- Unit weight: 50-300 lb depending on size
- Water-filled coil adds weight (0.5-2.0 gal water per unit)
- Vibration isolation: Required for centrifugal units, recommended for propeller

**Suspension hardware:**
- Steel rod or cable suspension (1/4 in to 1/2 in diameter)
- Swivel bracket for propeller units (directional adjustment)
- Fixed bracket for vertical units
- Safety cable or chain (redundant support)

**Clearances:**
- Discharge clearance: 4-8 ft minimum (prevent direct impingement on people/objects)
- Service clearance: 3-4 ft minimum for coil access
- Ceiling/roof: 1-3 ft (thermal clearance, avoid overheating)

### Piping Connections

**Steam systems:**
- Supply: Reduced pressure and temperature if high-pressure source
- Steam trap: At coil condensate outlet, sized for load plus safety factor
- Drip leg: Ahead of coil supply (remove condensate from steam main)
- Vacuum breaker: If condensate returns to vacuum system

**Hot water systems:**
- Supply and return: 3/4 in to 2 in depending on capacity
- Control valve: Two-way modulating or on-off
- Air vents: At coil high point (automatic vents)
- Isolation valves: Service and balancing
- Freeze protection: Drain valves, glycol, or heat trace if freezing risk

**Piping pitch:**
- Steam coils: Pitch toward trap (1/4 in per foot)
- Hot water: Pitch for air removal (toward vents)

### Control Strategies

**On-off control:**
- Thermostat energizes fan and opens valve
- Simple, low cost
- Temperature swing: ±3-5°F typical
- Suitable for unoccupied or tolerant applications

**Two-stage control:**
- Stage 1: Low fan speed, valve open
- Stage 2: High fan speed, valve wide open
- Reduced swing, better comfort
- Lower noise during mild weather

**Modulating control:**
- Proportional valve position based on temperature
- Fan runs continuously or cycles with valve
- Best comfort (±1-2°F)
- Higher cost, complexity

**Freeze protection:**
- Low-limit sensor in discharge air (55-65°F)
- Shuts valve if air temp drops (prevents coil freeze)
- Critical for hot water systems in cold climates

## Applications and Best Practices

### Warehouse and Distribution Centers

**Design approach:**
- Perimeter units beneath skylights/roof (address major heat loss)
- Interior units for supplemental heating
- Door units for infiltration load
- Mounting height: 20-30 ft typical

**Control:**
- Zone by use pattern (high-activity areas vs. storage)
- Setback during unoccupied periods (55-60°F)
- Morning warm-up staging (prevent overcurrent)

### Manufacturing Facilities

**Considerations:**
- Process heat gains reduce heating load
- Local exhaust may create negative pressure (increase infiltration)
- Equipment clearances (cranes, conveyors)
- Noise tolerance (production areas less sensitive)

**Unit selection:**
- Higher capacity units (reduce quantity, installation cost)
- Two-speed or VFD for part-load efficiency
- Industrial-grade construction (heavy-duty motors, corrosion-resistant finish)

### Loading Docks and Vestibules

**Challenge:**
- High infiltration during door open cycles
- Spot heating requirement
- Avoid direct blow on personnel

**Solution:**
- Vertical downblow units above door
- Horizontal units angled to create air curtain effect
- High leaving air temperature acceptable (short exposure)
- Rapid response (two-speed or modulating)

### Aircraft Hangars and High-Bay Spaces

**Unique requirements:**
- Ceiling heights 40-80 ft
- Massive volume, high stratification
- Equipment clearance critical

**Design:**
- Combine unit heaters with radiant heating (infrared)
- Unit heaters for occupied zone, radiant for floor/equipment
- High-capacity units (200,000-300,000 Btu/h)
- Confirm throw distance adequate (may require 60+ ft)

## Maintenance and Troubleshooting

### Routine Maintenance

**Monthly (during operation):**
- Inspect for unusual noise or vibration
- Verify fan operation
- Check for steam/water leaks

**Seasonal:**
- Clean coil fins (vacuum or compressed air)
- Lubricate fan bearings if required
- Inspect belt tension and condition (belt-drive units)
- Test controls and safeties

**Annual:**
- Steam trap inspection and testing
- Coil pressure test (hot water systems)
- Motor inspection and testing
- Vibration isolation check

### Common Problems

**Inadequate heating:**
- Insufficient airflow (dirty coil, failed fan, belt slippage)
- Low steam pressure or water temperature
- Control valve not opening (check actuator, control signal)
- Air trapped in hot water coil (bleed air)

**Short throw/poor coverage:**
- Fan running backwards (check motor rotation)
- Low fan speed (check voltage, motor condition)
- Coil air bypass (leaking cabinet seams)

**Noise:**
- Loose fan mounting or blades
- Failed bearings
- Vibration transmission to structure (check isolation)
- Steam trap malfunction (condensate backup, water hammer)

**Freeze damage:**
- Coil freeze due to low airflow or water temperature
- Prevention: Drain coil when off, use glycol, maintain airflow and water flow

---

*Hydronic unit heaters provide high-capacity forced-convection heating for large open spaces through suspended propeller or centrifugal fan units with steam or hot water coils. Proper selection integrates space heat load with throw distance requirements and mounting constraints, while effective control strategies optimize comfort, efficiency, and equipment protection in warehouse, industrial, and high-bay applications.*
