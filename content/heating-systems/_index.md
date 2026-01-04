---
title: "Heating Systems"
weight: 6
---

# Heating Systems

Comprehensive coverage of heating equipment, distribution systems, and control strategies for residential, commercial, and industrial applications. Heating systems maintain thermal comfort, enable industrial processes, and provide domestic hot water across diverse climates and building types.

## Equipment Technologies

### Boilers

Boilers generate hot water or steam for space heating and process applications. Boiler selection depends on fuel type, capacity, efficiency requirements, and system configuration.

**Boiler types:**
- **Fire-tube:** Compact, 15-800 hp, commercial/industrial
- **Water-tube:** Large capacity, high pressure, industrial/utility
- **Cast iron sectional:** Modular, residential/light commercial
- **Condensing:** 90-98% efficiency, low return water temperature
- **Electric:** Clean, quiet, 100% efficient at point of use

**Performance metrics:**
- **Thermal efficiency:** Output/input energy ratio
- **AFUE (Annual Fuel Utilization Efficiency):** Seasonal performance
- **Turndown ratio:** Minimum to maximum firing rate
- **Emissions:** NOx, CO limits per codes

**Related Technical Guides:**
- [Boiler Selection & Sizing](/technical-guides/boiler-selection-sizing/)
- [Combustion Analysis](/technical-guides/combustion-analysis/)

### Heat Pumps

Heat pumps extract heat from outdoor air, ground, or water sources and deliver it indoors at higher temperature. Reverse cycle operation provides both heating and cooling.

**Types:**
- **Air-source heat pumps (ASHP):** Most common, moderate cost
- **Ground-source heat pumps (GSHP):** High efficiency, high first cost
- **Water-source heat pumps (WSHP):** Building loop systems
- **Mini-split/multi-split:** Ductless zoning

**Performance:**
- **COP (Coefficient of Performance):** Heating output/electrical input
- **HSPF (Heating Seasonal Performance Factor):** Seasonal efficiency
- **Balance point:** Outdoor temperature where heat pump matches building load

**Related Technical Guides:**
- [Heat Pump Technology](/technical-guides/heat-pump-technology/)

### Furnaces

Furnaces heat air directly and distribute it through ductwork. Common in residential and light commercial applications.

**Categories:**
- **Residential gas furnaces:** 60-100 kBtu/h, 80-98% AFUE
- **Commercial gas furnaces:** 100-500 kBtu/h
- **Electric furnaces:** Resistance heating, 100% efficiency
- **Oil furnaces:** Rural areas without natural gas service

**Heat exchangers:**
- Primary heat exchanger (combustion products)
- Secondary heat exchanger (condensing models)
- Stainless steel for corrosion resistance

### Radiant Heating

Radiant systems heat surfaces (floor, ceiling, walls) that then warm occupants and objects through radiation. Radiant heating provides excellent comfort with lower air temperatures.

**Systems:**
- **Hydronic floor heating:** Tubing in concrete or under flooring
- **Electric floor heating:** Resistance cables or mats
- **Radiant ceiling panels:** Hydronic or electric
- **Infrared heaters:** High-temperature spot heating

**Design considerations:**
- Surface temperature limits (floor: 85°F max, ceiling: 120°F max)
- Thermal mass and response time
- Floor covering thermal resistance
- Control strategies (outdoor reset, slab sensors)

**Related Technical Guides:**
- [Radiant Heating Design](/technical-guides/radiant-heating-design/)

### Combined Heat and Power (CHP)

CHP systems generate electricity and capture waste heat for space heating, water heating, or process use. Typical electrical efficiency: 25-40%, total efficiency: 70-90%.

**Prime movers:**
- **Reciprocating engines:** 100 kW to 10 MW
- **Microturbines:** 30-300 kW
- **Fuel cells:** 5 kW to 5 MW, very low emissions
- **Steam turbines:** > 500 kW, industrial applications

**Economics:** Cost-effective when high electrical and thermal loads coincide.

## Combustion Systems

### Combustion Fundamentals

**Stoichiometry:** Theoretical air required for complete combustion

For natural gas (CH₄):
$$\text{CH}_4 + 2\text{O}_2 \rightarrow \text{CO}_2 + 2\text{H}_2\text{O}$$

**Excess air:** Additional air beyond stoichiometric (typically 10-50%)

**Combustion efficiency:**
$$\eta_{combustion} = \frac{Output}{Input} = \frac{Input - Losses}{Input}$$

**Losses:**
- Flue gas sensible heat (largest)
- Incomplete combustion
- Radiation and convection from jacket
- Cycling losses

**Related Technical Guides:**
- [Combustion Analysis](/technical-guides/combustion-analysis/)

### Fuels

**Natural gas:**
- Heating value: ~1,000 Btu/ft³
- Clean burning, low emissions
- Delivered via utility pipelines

**Propane (LPG):**
- Heating value: ~2,500 Btu/ft³
- Stored on-site in tanks
- Areas without natural gas service

**Fuel oil:**
- #2 oil (distillate): Residential, ~140,000 Btu/gal
- #4, #6 oil (residual): Commercial/industrial, require preheating
- Higher emissions than gas, require more maintenance

## Distribution Systems

### Hydronic (Hot Water) Systems

Water circulates through piping to terminal units (radiators, convectors, fan coils). Hydronic systems provide excellent zoning and quiet operation.

**System configurations:**
- **Series loop:** Simple, limited zoning
- **One-pipe:** Main with branch runouts
- **Two-pipe direct return:** Balanced flow
- **Two-pipe reverse return:** Self-balancing
- **Primary-secondary:** Decouples boiler from system flow
- **Variable primary flow:** Single variable-speed pumped loop

**Terminal units:**
- **Baseboard convectors:** Wall-mounted, gravity convection
- **Fan coil units (FCUs):** Forced airflow, cooling capability
- **Radiators:** Cast iron or steel panels
- **Unit heaters:** Overhead, high airflow

**Related Technical Guides:**
- [Hydronic System Fundamentals](/technical-guides/hydronic-system-fundamentals/)

### Steam Systems

Steam heating uses latent heat of condensation. Common in older buildings and industrial applications.

**Advantages:**
- High heat transfer coefficient
- No circulation pumps (gravity return)
- Rapid response

**Disadvantages:**
- Maintenance (traps, vents, condensate return)
- Safety (high temperature, pressure)
- Difficult zoning

**System types:**
- One-pipe steam (gravity return)
- Two-pipe steam (mechanical return)
- Vacuum return systems

### Forced Air Systems

Air heated by furnace or coil distributes through ductwork. Forced air systems integrate with cooling and ventilation.

**Components:**
- Supply ducts and diffusers
- Return ducts and grilles
- Air filters
- Blower/fan

**Zoning:**
- Multiple furnaces
- Zoned ductwork with dampers
- Bypass dampers for pressure control

## Heating Load Calculations

Accurate load calculations prevent undersizing (inadequate heating) and oversizing (short cycling, inefficiency).

**Heat loss components:**
1. **Transmission:** Heat conduction through envelope
2. **Infiltration:** Cold air entering through cracks
3. **Ventilation:** Outdoor air for IAQ

**Calculation methods:**
- **Simplified:** Area × U-value × ΔT
- **ASHRAE Handbook:** Detailed component-by-component
- **Software:** Load calculation programs (Carrier HAP, Trane TRACE, Wrightsoft Right-Suite)

**Related Technical Guides:**
- [Heating Load Calculations](/technical-guides/heating-load-calculations/)

## Control Strategies

**Temperature control:**
- **Thermostat:** On/off or modulating control
- **Outdoor reset:** Supply water temperature varies with outdoor temp
- **Setback:** Reduced temperature during unoccupied periods

**Optimization:**
- Optimal start/stop (minimize operating hours)
- Warm-up/cool-down rates
- Night setback recovery

## Design Considerations

**Sizing:**
- Design heating load (99.6% or 99% design day)
- Safety factor: 10-20% (not 50%!)
- Pickup load for thermostat setback recovery

**Efficiency:**
- Condensing boilers require low return water temperature
- Modulating burners match load, reduce cycling
- Variable-speed pumps save energy in variable-flow systems

**Codes and standards:**
- **ASHRAE 90.1:** Equipment efficiency minimums, economizers
- **IMC (International Mechanical Code):** Venting, combustion air
- **NFPA codes:** Fuel gas, oil burner installation

## Browse Topics

Explore detailed subtopics within heating systems:

- **[Boilers](./boilers/)** - Fire-tube, water-tube, cast iron, condensing, electric
- **[Heat Pumps](./heat-pumps/)** - Air-source, ground-source, water-source, mini-split
- **[Furnaces](./furnaces/)** - Gas, oil, electric, heat exchangers, controls
- **[Combustion](./combustion/)** - Burners, fuels, efficiency, flue gas analysis
- **[Radiant Heating](./radiant-heating/)** - Floor, ceiling, wall systems, panels
- **[CHP/Cogeneration](./chp-cogeneration/)** - Prime movers, heat recovery, economics
- **[Hydronic Distribution](./hydronic-distribution/)** - Piping, pumps, terminal units, controls
- **[Residential Heating](./residential-heating/)** - Systems, equipment, comfort, efficiency

## Reference Standards

- **ASHRAE Handbook of HVAC Systems and Equipment** - Chapters on heating equipment
- **ASHRAE Standard 90.1:** Energy Standard for Buildings
- **ASME Boiler and Pressure Vessel Code:** Boiler design and safety
- **NFPA 54 (National Fuel Gas Code):** Gas piping and appliances
- **NFPA 31:** Oil-burning equipment installation

---

*Efficient heating systems provide comfort, safety, and reliability while minimizing energy consumption and environmental impact.*
