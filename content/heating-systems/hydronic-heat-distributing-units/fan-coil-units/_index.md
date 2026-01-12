---
title: "Fan Coil Units (Heating Mode)"
weight: 4
description: "Technical analysis of hydronic fan coil units in heating mode including horizontal and vertical cabinet configurations, heating coil design, multi-speed fan control, two-pipe and four-pipe system applications, capacity ratings, condensate management, and filter maintenance for perimeter and interior zone heating."
keywords: "fan coil units, FCU, hydronic heating, hot water coils, fan coil heating, two-pipe systems, four-pipe systems, vertical fan coils, horizontal fan coils, multi-speed fans"
---

# Fan Coil Units (Heating Mode)

Fan coil units provide forced convection hydronic heating through hot water coils with motorized fan circulation, delivering heat outputs of 200-800 Btu/h per square foot of floor area served with fast response times (5-15 minutes to full output) suitable for intermittent occupancy and variable load applications. Unlike natural convection terminals (baseboard, radiators, convectors), fan coils actively circulate room air across finned-tube heat exchangers, achieving 3-5× higher heat transfer coefficients and enabling compact terminal dimensions while operating effectively at lower water temperatures (140-180°F) compatible with condensing boilers and heat pump systems.

The fundamental advantage of fan coil units lies in their forced convection operation, where mechanical air movement across the coil surface increases the convective heat transfer coefficient from natural convection values of 1-3 Btu/h·ft²·°F to forced convection values of 5-15 Btu/h·ft²·°F. This enhancement enables a 400 CFM fan coil unit with 2-row coil to deliver the same heating capacity as 40-60 linear feet of baseboard radiator, occupying approximately 1/10th the perimeter space. The increased heat transfer rate permits operation at lower water temperatures while maintaining adequate capacity, making fan coils particularly well-suited to condensing boiler systems where return water temperatures below 130°F enable efficiency gains of 10-15% over non-condensing operation.

Fan coil systems dominate multi-family residential and hotel applications due to individual zone control, compact terminal size enabling installation in closets or above ceilings, and compatibility with both two-pipe (seasonal changeover) and four-pipe (simultaneous heating/cooling) distributions. Typical installations serve 300-800 ft² per unit in hotels and apartments, with vertical cabinet units mounted in closets or wall recesses for occupied spaces and horizontal units concealed above bathrooms or corridors where ceiling height permits accessibility.

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

**Coil row configuration impact:**

The number of coil rows directly affects heat transfer capacity and water-side pressure drop. Each additional row increases the effective surface area in contact with airflow and extends the thermal path, improving heat transfer effectiveness at the cost of higher air and water pressure drops.

| Rows Deep | Heat Transfer Effectiveness | Typical Heating Capacity (relative) | Water Δp | Air Δp | Application |
|-----------|---------------------------|-------------------------------------|----------|--------|-------------|
| 1 row | 55-65% | 100% | 0.5-1.5 psi | 0.08-0.12 in wc | Light duty, low-temp systems |
| 2 rows | 75-85% | 160-180% | 1.5-3 psi | 0.12-0.18 in wc | Standard heating |
| 3 rows | 85-92% | 210-240% | 3-5 psi | 0.18-0.25 in wc | High output, four-pipe systems |
| 4 rows | 90-95% | 250-280% | 5-8 psi | 0.25-0.35 in wc | Maximum capacity, limited use |

Two-row coils represent the standard for heating-only applications, providing adequate capacity at 160-180°F entering water temperature with acceptable pressure drop. Three-row coils suit four-pipe systems where the same coil must handle both heating and cooling duties, or where low-temperature water (140-160°F) necessitates increased surface area to maintain capacity. Four-row configurations appear primarily in high-capacity applications or retrofit situations where existing units cannot meet load requirements.

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

Two-pipe systems require a changeover period when transitioning between heating and cooling modes, typically occurring in spring and fall. During changeover, the entire system drains or purges, the central plant switches from boiler to chiller operation (or vice versa), and the distribution system refills with water at the new temperature. This changeover process requires 2-8 hours depending on system size and complexity, during which no conditioning capability exists. The changeover decision point typically occurs when outdoor temperature trends indicate sustained need for the opposite mode, with many systems using outdoor temperature thresholds of 60-65°F for spring changeover to cooling and 55-60°F for fall changeover to heating.

**Applications:**
- Suitable for climates with distinct heating/cooling seasons
- Buildings with uniform thermal loads (all zones require same mode)
- Lower piping cost than four-pipe
- Acceptable for perimeter zones with similar solar exposure
- Hotels and apartments in temperate climates (ASHRAE climate zones 4-5)
- Garden apartments and mid-rise residential where interior zones are minimal

The economic advantage of two-pipe systems stems from reduced piping material (50% compared to four-pipe), simplified plant room layout, and lower pump energy from reduced pipe friction. Installation cost savings reach 25-35% for the distribution system, making two-pipe the default choice for residential applications where simultaneous heating and cooling rarely occurs.

### Four-Pipe System Operation

**Simultaneous heating and cooling:**
- Separate hot water supply and return
- Separate chilled water supply and return
- Each FCU has 4 pipe connections
- Independent heating and cooling coils or single coil with dual supply

Four-pipe fan coil units typically incorporate separate heating and cooling coils within the same cabinet, with the heating coil positioned downstream of the cooling coil in the airflow path. This arrangement ensures cooling coil condensate drains properly and prevents reheating of cooled air during cooling mode. Control sequences energize only one coil at a time based on room temperature relative to heating and cooling setpoints, with a deadband of 2-4°F between modes preventing simultaneous operation and energy waste.

**Control:**
- Dead band between heating and cooling setpoints
- Automatic mode selection based on room temperature
- Can serve zones with opposite needs simultaneously

Typical control logic for four-pipe systems:
- Room temperature < heating setpoint: Open hot water valve, fan operates
- Heating setpoint < room temperature < cooling setpoint: Both valves closed, fan may run for circulation
- Room temperature > cooling setpoint: Open chilled water valve, fan operates
- Changeover occurs automatically at each zone based on local conditions

**Applications:**
- Interior zones (cooling year-round) and perimeter zones (heating in winter)
- Buildings with high internal loads and envelope losses
- Hospitals, laboratories (precise temperature control)
- Higher installation cost justified by operational flexibility
- High-rise hotels and luxury apartments requiring year-round flexibility
- Mixed-use buildings where different tenants have different schedules

**Piping and energy:**
- Four pipe mains throughout building
- Both heating and cooling plant operate year-round (increased energy)
- Superior comfort and zone control

Four-pipe systems excel in hotels where south-facing rooms may require cooling while north-facing rooms need heating on the same spring or fall day. The ability to satisfy diverse thermal loads without compromise justifies the 30-40% premium in installed cost for upscale properties where guest comfort complaints directly impact revenue. Annual operating costs may increase 5-10% due to simultaneous plant operation and higher pumping energy, though superior zone control can offset this through reduced overcooling and overheating.

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

## Condensate Drainage Systems

**Heating-only operation:**

Fan coil units operating exclusively in heating mode produce no condensate and require no drain connections. The coil surface temperature remains above room dew point temperature throughout operation, preventing moisture accumulation. This simplifies installation in heating-only climates or seasonal heating applications where cooling capability is unnecessary.

**Heating/cooling operation:**

Fan coils serving both heating and cooling duties require condensate drainage infrastructure to remove moisture condensed from room air during cooling operation. Coil surface temperatures of 45-55°F in cooling mode fall well below typical room dew points of 55-60°F, causing water vapor to condense at rates of 0.5-2.0 gallons per hour per ton of cooling capacity.

### Condensate Drain Pan Design

**Pan construction:**
- Stainless steel or molded plastic
- Sloped 1/4 in per foot minimum toward drain outlet
- Depth: 1-2 in to contain water during peak condensation
- Sealed joints to prevent leakage into building structure
- Auxiliary drain connection for overflow protection

**Critical considerations:**
- Pan must extend beyond coil footprint to catch all condensate
- Insulation prevents external condensation on cold pan surfaces
- Access for cleaning removes accumulated sediment and biological growth
- Overflow detection (water sensor) alerts to drain blockage

### Drain Line Configuration

**P-trap requirement:**

Condensate drain lines require properly sized P-traps to prevent air flow through the drain while allowing gravity drainage. The trap depth must overcome the negative pressure created when the fan operates:

$$h_{trap} = \frac{\Delta P_{static}}{62.4} \times 12$$

Where:
- $h_{trap}$ = Required trap seal depth in inches water column
- $\Delta P_{static}$ = Static pressure at drain pan in inches water column
- 62.4 = Density of water in lb/ft³
- 12 = Conversion factor

For typical fan coil with -0.3 in wc at drain pan, trap seal depth must exceed 0.3 in water column, translating to 3-4 in actual trap depth providing safety margin.

**Piping practices:**
- Minimum 3/4 in diameter drain line (1 in preferred for units >600 CFM)
- Pitch 1/4 in per foot minimum toward disposal point
- Trap must remain filled; prime with water at commissioning
- Vent trap to atmosphere if negative pressure exceeds trap seal
- Cleanout access at trap and 10 ft intervals maximum

**Drainage methods:**

| Method | Application | Advantages | Disadvantages |
|--------|-------------|------------|---------------|
| Gravity to floor drain | Ground floor units | Simple, reliable | Requires floor drain proximity |
| Gravity to building drain | Multi-story buildings | No pump required | Vertical drain runs increase cost |
- Condensate pump | Remote drain locations | Enables installation anywhere | Requires power, maintenance, noise |
| Indirect waste connection | Health care, food service | Prevents cross-contamination | Code-required air gap increases complexity |

### Hotel and Apartment Installation Considerations

**Vertical cabinet units in closets:**

Hotel guest rooms and apartment units typically install vertical fan coil units in bathroom or entry closets to minimize visual impact and noise transmission to sleeping areas. Critical installation requirements include:

- Sound isolation: Rubber vibration isolators under cabinet, flexible pipe connections
- Access: Removable closet panels or doors for filter service and maintenance
- Clearances: 12-18 in in front of unit for filter removal and service
- Drain routing: Condensate drains run to bathroom floor drain or vertical stack
- Electrical: Dedicated circuit from electrical closet, avoid shared circuits with high-draw appliances

**Horizontal units above bathrooms:**

Ceiling-concealed horizontal fan coils installed above bathroom ceilings serve hotel rooms and apartments where vertical space permits. This configuration centralizes mechanical equipment in non-occupied space but requires:

- Ceiling height: Minimum 8 ft finished ceiling to provide 12-18 in plenum depth
- Structural support: Unit weight (100-250 lb) plus service personnel loads
- Access panels: Minimum 24 × 24 in for unit access and coil cleaning
- Condensate routing: Drains pitch to bathroom plumbing stack
- Supply grilles: Locate to avoid drafts on bed or primary seating
- Return grilles: Position to enable proper air circulation, avoid short-circuiting

**Noise control:**

Guest room fan coil installations demand particular attention to acoustic performance. Vertical cabinet units with closed doors achieve NC 25-30 at low fan speed, acceptable for sleeping spaces. Strategies to minimize noise transmission include:

- Thermostat programming: Low speed operation during nighttime hours
- Resilient mounting: Vibration isolators prevent structure-borne sound
- Grille selection: Adjustable directional grilles enable air distribution without high velocities
- Door undercuts: 1 in minimum clearance enables air circulation without forcing air through unit at high velocity

## Installation and Maintenance

### Installation Practices

**Piping connections:**
- Isolation valves on supply and return
- Control valve (two-way modulating or on-off)
- Air vents at high points
- Unions or flanges for unit removal
- Pitch piping for drainage
- Flexible connectors for vibration isolation (hotel/apartment applications)
- Insulation on supply piping prevents heat loss and condensation

**Condensate drainage (if cooling):**
- Drain pan beneath coil
- Trap on drain line (overcome negative plenum pressure)
- Pitch to drain 1/4 in per foot minimum
- Not required for heating-only operation
- Secondary drain pan or overflow protection in ceiling-concealed applications
- Drain line insulation in unconditioned spaces prevents freezing

**Electrical:**
- Power to fan motor (24V, 120V, or 208-277V)
- Control wiring to thermostat
- Interlock with valve actuator
- Dedicated circuit in hotel/apartment units (avoid shared circuits)
- Emergency power connection for critical applications (hospitals)

**Ductwork (if applicable):**
- Supply duct from unit discharge
- Return duct to unit inlet
- Proper sealing (prevent air leakage)
- Insulation on ducts in unconditioned spaces
- Flexible duct connections for vibration isolation

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

## Control Strategies and Sequences

### Thermostat Control Types

**On-off (two-position) control:**

The simplest control method uses a two-position thermostat to cycle the fan and water valve together. When room temperature falls below setpoint, both fan and valve energize; when temperature rises above setpoint plus differential, both de-energize. This approach suits economy applications but produces temperature swings of 2-4°F due to system thermal mass and lag time.

**Multi-speed fan control:**

Three-speed thermostats or controllers provide staged response to heating demand:

- Stage 1 (small temperature error): Low fan speed, valve open
- Stage 2 (moderate error): Medium fan speed, valve open
- Stage 3 (large error): High fan speed, valve open

This staged approach reduces energy consumption during partial load conditions while maintaining capacity for full load situations. A typical guest room operates at low speed 60-70% of occupied hours, medium speed 20-30%, and high speed only 5-10%, reducing average fan power consumption by 40-50% compared to constant high-speed operation.

**Modulating control:**

Premium installations employ proportional-integral (PI) or proportional-integral-derivative (PID) control with modulating valves and variable-speed ECM fan motors. The controller varies both valve position and fan speed continuously in response to temperature error, maintaining room temperature within ±0.5°F of setpoint.

Control equation for modulating systems:

$$Output = K_p \times Error + K_i \times \int Error \, dt$$

Where proportional gain ($K_p$) provides immediate response to temperature error and integral gain ($K_i$) eliminates long-term offset.

### Valve Control Configurations

**Two-way valves:**

Two-way modulating or on-off valves throttle flow through individual fan coil units while maintaining constant system pressure differential through variable-speed pumping or differential pressure bypass valves. Two-way valves enable system-wide energy savings as diversity reduces total flow:

- Design flow: 100% at peak load (all units calling for maximum capacity)
- Typical average flow: 40-60% due to diversity (many units at partial load or off)
- Pump energy: Varies with flow when using variable-speed pumping

Hotel and apartment applications achieve particularly high diversity factors, with 300-room hotel rarely exceeding 65% simultaneous heating demand even at design conditions.

**Three-way valves:**

Three-way mixing or diverting valves maintain constant flow through the fan coil unit while modulating the ratio of hot water to bypass flow. This approach provides stable airflow and rapid response but eliminates flow reduction benefits:

- Unit flow: Constant regardless of load
- System flow: Constant, no pump energy reduction
- Application: Legacy systems, special temperature control requirements

Three-way valves appear primarily in retrofit applications where existing constant-volume pumping prohibits conversion to variable flow, or in critical applications (laboratories, hospitals) where control stability justifies the energy penalty.

### Hotel and Apartment Control Integration

**Guest room control:**

Modern hotel installations integrate fan coil control with property management systems (PMS) and building automation systems (BAS) to optimize energy consumption while maintaining guest comfort:

**Occupied mode:**
- Guest thermostat control active (65-75°F adjustable range)
- All fan speeds available
- Immediate response to guest adjustments
- Dead band: 2-3°F between heating and cooling (four-pipe systems)

**Unoccupied mode (detected via keycard system or motion sensors):**
- Setback to 62°F heating, 80°F cooling
- Fan speed limited to low (reduced noise, energy savings)
- Reduced ventilation if code permits
- Annual energy savings: 25-35% compared to continuous full operation

**Checkout/makeup mode:**
- Temporary occupancy override for housekeeping
- 2-4 hour timer
- Returns to unoccupied mode automatically

**Master control overrides:**

Building operators can implement system-wide overrides during extreme weather events or demand response periods:

- Heating lockout above outdoor temperature threshold (typically 65-70°F)
- Cooling lockout below outdoor temperature threshold (typically 60-65°F)
- Load shedding: Temporary setpoint adjustment during peak demand periods
- Seasonal changeover scheduling for two-pipe systems

### Apartment Building Control

**Individual tenant control:**

Apartments typically provide full thermostat control to tenants with minimal automation:

- Programmable or smart thermostats enable occupant scheduling
- Heat/cool mode selection (four-pipe systems) or seasonal lockout (two-pipe)
- Fan speed selection: Auto (thermostat-controlled) or manual
- No remote override capability (tenant privacy and autonomy)

**Common area control:**

Corridors, lobbies, and amenity spaces utilize centralized control:

- Scheduled setback during low-occupancy hours
- Outdoor temperature compensation for improved efficiency
- Integration with fire alarm system for smoke control mode
- Central monitoring of equipment failures and maintenance needs

---

*Fan coil units provide compact, responsive hydronic heating through forced convection over finned-tube coils, with horizontal and vertical configurations suited to diverse architectural constraints and applications. Multi-speed fan control enables proportional output modulation, while compatibility with low-temperature water sources makes fan coils well-suited to modern condensing boiler and heat pump systems in both two-pipe and four-pipe distributions. The flexibility to accommodate either seasonal changeover (two-pipe) or simultaneous heating and cooling (four-pipe) makes fan coil systems the dominant choice for hotels and apartments where individual zone control, compact equipment dimensions, and concealed installation drive design decisions. Proper attention to coil row selection, condensate drainage design, and control integration ensures reliable operation and guest comfort while minimizing energy consumption through staged fan operation and occupancy-based setback strategies.*
