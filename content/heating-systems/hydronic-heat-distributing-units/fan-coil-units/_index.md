---
title: "Fan Coil Units (Heating Mode)"
weight: 4
description: "Technical analysis of hydronic fan coil units in heating mode including horizontal and vertical cabinet configurations, heating coil design, multi-speed fan control, two-pipe and four-pipe system applications, capacity ratings, condensate management, and filter maintenance for perimeter and interior zone heating."
keywords: "fan coil units, FCU, hydronic heating, hot water coils, fan coil heating, two-pipe systems, four-pipe systems, vertical fan coils, horizontal fan coils, multi-speed fans"
---

# Fan Coil Units (Heating Mode)

Fan coil units provide forced convection hydronic heating through hot water coils with motorized fan circulation, delivering heat outputs of 200-800 Btu/h per square foot of floor area served with fast response times (5-15 minutes to full output) suitable for intermittent occupancy and variable load applications. Unlike natural convection terminals (baseboard, radiators, convectors), fan coils actively circulate room air across finned-tube heat exchangers, achieving 3-5× higher heat transfer coefficients and enabling compact terminal dimensions while operating effectively at lower water temperatures (140-180°F) compatible with condensing boilers and heat pump systems.

## Fan Coil Unit Configurations

### Horizontal Fan Coil Units

**Cabinet arrangement:**
- Horizontal coil orientation (airflow perpendicular to coil face)
- Centrifugal blower (forward-curved or backward-curved)
- Cabinet dimensions: 8-14 in high, 18-30 in deep, 24-72 in long
- Locations: Above ceiling, beneath floor, horizontal closet

**Airflow path:**
- Return air inlet: Bottom, end, or rear
- Fan draws air through filter
- Air passes through coil (heating or cooling)
- Discharge: Top, end, or front through grille/diffuser

**Typical capacities:**
- Residential: 400-1,200 CFM, 9,000-36,000 Btu/h heating
- Commercial: 800-2,000 CFM, 24,000-60,000 Btu/h heating

### Vertical Fan Coil Units

**Cabinet arrangement:**
- Vertical coil orientation (airflow horizontal through coil)
- Tangential (cross-flow) or centrifugal blower
- Cabinet dimensions: 24-48 in high, 6-12 in deep, 18-36 in long
- Locations: Wall-mounted, floor-mounted, recessed in wall

**Airflow path:**
- Return air inlet: Bottom or lower grille
- Fan circulation through filter (optional)
- Air passes horizontally through vertical coil
- Discharge: Upper grille directed into room

**Typical capacities:**
- Small: 200-400 CFM, 6,000-12,000 Btu/h heating
- Medium: 400-800 CFM, 12,000-24,000 Btu/h heating
- Large: 800-1,200 CFM, 24,000-36,000 Btu/h heating

### Ceiling-Concealed vs. Cabinet Units

**Ceiling-concealed (horizontal):**
- Installed in plenum space above ceiling
- Ducted or non-ducted discharge
- Supply and return grilles in ceiling
- Minimal visual impact
- Service access through ceiling panels

**Cabinet units (vertical):**
- Exposed in conditioned space
- Decorative enclosure finish
- Integral supply/return grilles
- Direct service access
- Aesthetic considerations important

## Heating Coil Design and Performance

### Fin-Tube Coil Construction

**Standard heating coil:**
- Copper tubes: 1/2 in or 5/8 in OD
- Aluminum fins: 0.006-0.010 in thickness
- Fin density: 8-14 fins per inch
- Rows deep: 1-4 rows (2-3 typical for heating)
- Tube circuits: Multiple parallel paths for flow distribution

**Heat transfer:**

$$Q = UA \times LMTD$$

Where:
- $U$ = Overall heat transfer coefficient (40-80 Btu/h·ft²·°F for heating coils with forced airflow)
- $A$ = Coil face area × rows deep (effective surface area)
- $LMTD$ = Log mean temperature difference

**LMTD calculation:**

$$LMTD = \frac{(T_{w,in} - T_{a,out}) - (T_{w,out} - T_{a,in})}{\ln\left(\frac{T_{w,in} - T_{a,out}}{T_{w,out} - T_{a,in}}\right)}$$

Where:
- $T_{w,in}$, $T_{w,out}$ = Entering and leaving water temperatures
- $T_{a,in}$, $T_{a,out}$ = Entering and leaving air temperatures

### Heating Capacity Ratings

**Standard rating conditions (ARI 440):**
- Entering water temperature: 180°F
- Water flow rate: 3 GPM per nominal ton (for cooling rating)
- Entering air temperature: 70°F
- Airflow: Per manufacturer specification (CFM per nominal capacity)

**Typical heating output:**

| FCU Size | Airflow (CFM) | Coil Rows | Output @ 180°F EWT, 70°F EA | Output @ 160°F EWT |
|----------|---------------|-----------|------------------------------|-------------------|
| 200 | 200 | 2 | 6,000-8,000 Btu/h | 4,000-5,500 Btu/h |
| 400 | 400 | 2 | 12,000-16,000 Btu/h | 8,000-11,000 Btu/h |
| 600 | 600 | 3 | 20,000-26,000 Btu/h | 14,000-18,000 Btu/h |
| 800 | 800 | 3 | 26,000-34,000 Btu/h | 18,000-24,000 Btu/h |
| 1200 | 1,200 | 3 | 40,000-52,000 Btu/h | 28,000-36,000 Btu/h |

**Temperature correction:**

For water temperatures other than rated:

$$Q_{actual} = Q_{rated} \times \frac{LMTD_{actual}}{LMTD_{rated}}$$

Approximately linear relationship for moderate temperature variations (±20°F).

### Low-Temperature Operation

Fan coils well-suited to low-temperature hot water systems:

**Performance at reduced temperature:**
- 180°F entering water: 100% of rated capacity
- 160°F entering water: ~70% of capacity
- 140°F entering water: ~45% of capacity
- 120°F entering water: ~25% of capacity (marginal for heating)

**Compensating for reduced capacity:**
- Increase coil size (more rows, larger face area)
- Increase airflow (higher fan speed)
- Oversize unit selection
- Combine with other heating sources

**Condensing boiler compatibility:**
- Return water temperature <130°F enables condensation
- Requires lower supply temperature (140-160°F typical)
- Oversizing by 40-60% compared to high-temperature rating
- Fast response compensates for lower output density

## Multi-Speed Fan Control

### Fan Motor Types

**Permanent split capacitor (PSC):**
- Multiple speed taps on motor winding
- Typical: Low, Medium, High (3-speed)
- Simple, reliable, low cost
- Manual or automatic speed selection via thermostat or controller

**Electronically commutated motor (ECM):**
- Variable speed operation
- Energy efficient (50-70% less power than PSC)
- Precise airflow control
- Higher initial cost

**Shaded pole (small units):**
- Single or two-speed
- Lower efficiency
- Quiet operation
- Common in residential vertical units

### Speed vs. Output and Noise

**Airflow and capacity:**

$$Q \propto CFM \times \Delta T_{air}$$

Higher fan speed increases airflow and capacity (up to coil's heat transfer limit).

**Fan speed performance:**

| Fan Speed | Airflow (% of high) | Heating Output (% of high) | Sound Level (NC) | Power (% of high) |
|-----------|---------------------|---------------------------|------------------|-------------------|
| High | 100% | 100% | 35-45 | 100% |
| Medium | 75-80% | 80-88% | 28-35 | 55-65% |
| Low | 50-60% | 60-72% | 22-28 | 30-40% |

**Control strategies:**
- Manual: User selects speed via wall switch or unit control
- Automatic: Thermostat cycles fan speed based on temperature error
- Staged: Low speed for maintaining, high speed for recovery
- Continuous: Low speed for air circulation, higher speeds for heating demand

### Thermostat Integration

**Two-stage heat:**
- Stage 1: Open valve, low fan speed
- Stage 2: Open valve, high fan speed
- Provides proportional response to load

**Modulating control:**
- Proportional valve position
- Variable fan speed (ECM motor)
- Optimizes comfort and efficiency

**Fan cycling:**
- Auto mode: Fan runs only when heating (valve open)
- Continuous mode: Fan runs continuously, valve modulates
- Continuous improves air mixing and filtration but increases energy use

## Two-Pipe and Four-Pipe Systems

### Two-Pipe System Operation

**Seasonal changeover:**
- Summer: Chilled water circulated
- Winter: Hot water circulated
- Building-wide or zone changeover
- Cannot heat and cool simultaneously

**Piping configuration:**
- Single supply main
- Single return main
- Each FCU has supply and return connections
- Zone control via FCU valve or zone valve

**Applications:**
- Suitable for climates with distinct heating/cooling seasons
- Buildings with uniform thermal loads (all zones require same mode)
- Lower piping cost than four-pipe
- Acceptable for perimeter zones with similar solar exposure

### Four-Pipe System Operation

**Simultaneous heating and cooling:**
- Separate hot water supply and return
- Separate chilled water supply and return
- Each FCU has 4 pipe connections
- Independent heating and cooling coils or single coil with dual supply

**Control:**
- Dead band between heating and cooling setpoints
- Automatic mode selection based on room temperature
- Can serve zones with opposite needs simultaneously

**Applications:**
- Interior zones (cooling year-round) and perimeter zones (heating in winter)
- Buildings with high internal loads and envelope losses
- Hospitals, laboratories (precise temperature control)
- Higher installation cost justified by operational flexibility

**Piping and energy:**
- Four pipe mains throughout building
- Both heating and cooling plant operate year-round (increased energy)
- Superior comfort and zone control

## Sizing and Selection

### Load Calculation

**Room heating load:**

$$Q_{heat} = Q_{envelope} + Q_{infiltration} + Q_{ventilation}$$

**Envelope load:**

$$Q_{envelope} = \sum UA(T_{inside} - T_{outside})$$

**Ventilation load (if supplied by FCU):**

$$Q_{vent} = 1.08 \times CFM_{OA} \times (T_{inside} - T_{outside})$$

### Selection Procedure

**Step 1: Determine required capacity**

From load calculation, add pickup allowance (10-20%).

**Step 2: Determine water temperature**

Based on system design:
- High-temp: 180-200°F
- Medium-temp: 160-180°F
- Low-temp: 140-160°F

**Step 3: Select unit size**

From manufacturer catalog, choose FCU meeting capacity at specified water temperature and entering air conditions.

**Step 4: Verify airflow and sound**

- CFM adequate for ventilation if required
- Sound level acceptable for application (NC 25-35 residential, NC 35-45 commercial)

**Step 5: Check clearances and dimensions**

- Unit fits available space (ceiling plenum, wall cavity, floor)
- Service clearances adequate

### Sizing Example

**Perimeter office:**
- Heating load: 18,000 Btu/h
- Water available: 160°F supply, 140°F return (150°F average)
- Entering air: 70°F
- Sound limit: NC 35

**Selection:**
1. At 180°F EWT, need unit rated ~18,000 Btu/h
2. Correction for 160°F: Capacity reduces to ~70%
3. Must select unit rated 18,000 / 0.70 = 25,700 Btu/h @ 180°F
4. Select 800 CFM unit: Rated 26,000-34,000 Btu/h @ 180°F
5. At 160°F: 26,000 × 0.70 = 18,200 Btu/h ✓
6. Check sound: Medium speed = NC 32 ✓
7. Unit selection: 800 CFM vertical FCU, 3-row coil, medium speed

## Installation and Maintenance

### Installation Practices

**Piping connections:**
- Isolation valves on supply and return
- Control valve (two-way modulating or on-off)
- Air vents at high points
- Unions or flanges for unit removal
- Pitch piping for drainage

**Condensate drainage (if cooling):**
- Drain pan beneath coil
- Trap on drain line (overcome negative plenum pressure)
- Pitch to drain
- Not required for heating-only operation

**Electrical:**
- Power to fan motor (24V, 120V, or 208-277V)
- Control wiring to thermostat
- Interlock with valve actuator

**Ductwork (if applicable):**
- Supply duct from unit discharge
- Return duct to unit inlet
- Proper sealing (prevent air leakage)

### Filter Maintenance

**Filter types:**
- Disposable fiberglass: MERV 1-4, replace monthly-quarterly
- Pleated media: MERV 6-8, replace quarterly-annually
- Washable: Clean monthly-quarterly

**Maintenance schedule:**
- Inspect monthly during heavy use
- Replace/clean per manufacturer schedule
- Dirty filters reduce airflow 20-50%, capacity 15-35%

**Access:**
- Return grille removal (most vertical units)
- Access panel or ceiling panel (horizontal units)
- Ensure accessible location

### Routine Maintenance Tasks

**Monthly (during operation):**
- Check filter condition
- Verify fan operation
- Listen for unusual noise

**Quarterly:**
- Replace or clean filter
- Clean return grille
- Check condensate drain (if cooling)

**Annual:**
- Clean coil (vacuum fins, chemical cleaning if heavily fouled)
- Lubricate fan motor bearings (if required)
- Check valve operation and calibration
- Verify control sequence
- Inspect electrical connections

**Coil cleaning:**
- Vacuum fins to remove dust
- Chemical coil cleaner for grease, heavy soil
- Rinse thoroughly
- Allow to dry before operation

## Common Issues and Troubleshooting

**Inadequate heating:**
- Dirty filter (replace/clean)
- Low water temperature (check boiler, valve)
- Air in coil (bleed air vents)
- Valve not opening (check control signal, actuator)
- Fan not running (check power, thermostat, motor)

**Excessive noise:**
- Dirty filter (increased air velocity)
- Fan speed too high (reduce speed if load permits)
- Loose components (secure panels, grilles)
- Failing motor bearings (lubricate or replace motor)

**Uneven room temperature:**
- Short-cycling (check thermostat location, differential)
- Airflow maldistribution (verify duct balance, grille selection)
- Inadequate capacity (verify load, unit selection)

**Water leaks:**
- Coil connections (tighten, replace gaskets)
- Condensate overflow (clean drain, verify trap)
- Corrosion (inspect coil, replace if through-wall corrosion)

---

*Fan coil units provide compact, responsive hydronic heating through forced convection over finned-tube coils, with horizontal and vertical configurations suited to diverse architectural constraints and applications. Multi-speed fan control enables proportional output modulation, while compatibility with low-temperature water sources makes fan coils well-suited to modern condensing boiler and heat pump systems in both two-pipe and four-pipe distributions.*
