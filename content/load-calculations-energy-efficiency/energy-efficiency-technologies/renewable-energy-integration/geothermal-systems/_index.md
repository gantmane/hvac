---
title: "Geothermal Heat Pump Systems"
aliases: ["Geothermal Heat Pump Systems"]
description: "Ground source heat pump technology, ground loop design methods, vertical and horizontal heat exchanger configurations, ground thermal properties, loop sizing calculations, antifreeze selection, system performance metrics, and ASHRAE design standards for geothermal HVAC systems."
weight: 10
---

Geothermal heat pump systems (also termed ground source heat pumps or GSHP) exploit the stable temperature of the earth to provide efficient heating and cooling. The ground below the frost line maintains relatively constant temperatures year-round, typically 45-75°F depending on geographic location, providing a favorable heat source in winter and heat sink in summer compared to ambient air temperatures.

## Ground Source Heat Pump Fundamentals

### Operating Principles

Ground source heat pumps transfer thermal energy between a building and the ground using a closed-loop piping system filled with heat transfer fluid. The system operates on the vapor compression refrigeration cycle, with the ground loop serving as the heat source/sink instead of outdoor air.

**Energy Transfer Mechanisms:**

The ground loop heat exchanger transfers thermal energy through:
- Conduction through pipe walls
- Conduction through soil surrounding the pipes
- Natural groundwater movement (advection) in permeable soils
- Moisture migration in unsaturated zones

**Coefficient of Performance:**

GSHP systems achieve higher efficiency than air-source equipment due to more favorable operating conditions:

| Season | Ground Temp (°F) | Typical COP | Air-Source COP |
|--------|------------------|-------------|----------------|
| Winter heating | 45-55 | 3.5-4.5 | 2.0-3.0 |
| Summer cooling | 50-60 | 4.0-5.5 | 2.5-3.5 |

The heating COP for a GSHP is calculated as:

COP_h = Q_heating / W_compressor

Where:
- Q_heating = heating capacity delivered (Btu/hr)
- W_compressor = compressor power input (Btu/hr)

Typical water-to-air heat pumps achieve:
- Heating COP: 3.6 to 4.2 at 32°F entering water temperature (EWT)
- Cooling EER: 13 to 20 at 77°F EWT

### Ground Temperature Characteristics

Undisturbed ground temperature varies with depth and geographic location:

T(z,t) = T_mean + A_s × exp(-z√(π/(365α))) × cos[2π/365(t - t_0 - z/(2√(365α/π)))]

Where:
- T(z,t) = temperature at depth z and time t
- T_mean = mean annual earth surface temperature (°F)
- A_s = surface temperature amplitude (°F)
- z = depth below surface (ft)
- α = thermal diffusivity of soil (ft²/day)
- t = time (days)
- t_0 = phase constant (days)

**Typical thermal diffusivity values:**

| Soil Type | Thermal Diffusivity (ft²/day) | Thermal Conductivity (Btu/hr·ft·°F) |
|-----------|-------------------------------|--------------------------------------|
| Dry sand | 0.8-1.2 | 0.15-0.25 |
| Moist sand | 1.2-1.8 | 0.60-1.00 |
| Dry clay | 0.6-0.9 | 0.20-0.30 |
| Saturated clay | 0.9-1.4 | 0.60-0.90 |
| Saturated silt | 1.0-1.5 | 0.70-1.00 |
| Heavy saturated soil | 1.1-1.6 | 0.75-1.20 |
| Light saturated soil | 0.9-1.3 | 0.60-0.95 |
| Rock (granite) | 2.0-3.0 | 1.40-2.20 |
| Rock (limestone) | 1.5-2.5 | 1.00-1.80 |

Below approximately 20-30 ft depth, ground temperature remains relatively constant and equals the mean annual air temperature plus 2-5°F.

## Ground Loop Heat Exchanger Types

### Vertical Closed-Loop Systems

Vertical ground loop heat exchangers consist of U-bend pipe configurations installed in drilled boreholes, typically 150-500 ft deep with 4-6 inch diameter.

**Borehole Configurations:**

| Configuration | Description | Thermal Performance |
|---------------|-------------|---------------------|
| Single U-bend | One U-tube per borehole | Standard, 15-22 Btu/hr·ft |
| Double U-bend | Two U-tubes per borehole | Enhanced, 18-28 Btu/hr·ft |
| Concentric | Pipe within pipe | Highest performance, 25-35 Btu/hr·ft |

**Design Parameters:**

Borehole spacing: Minimum 15-20 ft between boreholes to prevent thermal interference
Loop pipe: 3/4 inch or 1 inch HDPE (SDR-11 or SDR-13.5)
Grout: Thermally enhanced bentonite with thermal conductivity 0.75-1.20 Btu/hr·ft·°F

**Vertical Loop Sizing:**

The required total borehole length is determined from:

L_total = (Q_c × R_ga + (Q_c/COP - W_c) × R_gm) / (EWT_max - T_g)

For heating design:

L_total = (Q_h × R_ga + (W_h - Q_h/COP) × R_gm) / (T_g - EWT_min)

Where:
- L_total = total borehole length required (ft)
- Q_c = peak cooling load (Btu/hr)
- Q_h = peak heating load (Btu/hr)
- R_ga = effective annual ground thermal resistance (hr·ft·°F/Btu)
- R_gm = effective monthly ground thermal resistance (hr·ft·°F/Btu)
- W_c = heat pump power consumption in cooling (Btu/hr)
- W_h = heat pump power consumption in heating (Btu/hr)
- COP = coefficient of performance
- EWT_max = maximum entering water temperature (°F)
- EWT_min = minimum entering water temperature (°F)
- T_g = undisturbed ground temperature (°F)

Typical vertical loop performance:

| Application | Heat Extraction (Btu/hr·ft) | Heat Rejection (Btu/hr·ft) |
|-------------|----------------------------|---------------------------|
| Heating dominated | 18-28 | 15-22 |
| Balanced | 20-30 | 18-26 |
| Cooling dominated | 22-32 | 20-28 |

Values depend on soil thermal conductivity, borehole spacing, and run time fraction.

### Horizontal Closed-Loop Systems

Horizontal loops install pipe in trenches 4-6 ft deep, below the frost line. These systems require significant land area but have lower installation costs in suitable terrain.

**Configuration Types:**

**Single-pipe horizontal:**
- One pipe loop per trench
- 200-300 ft of pipe per ton of capacity
- Trench spacing: 10-15 ft minimum
- Heat transfer: 25-40 Btu/hr·ft² of trench surface area

**Multiple-pipe horizontal:**
- 2-6 pipes per trench in horizontal or vertical orientation
- 150-250 ft of pipe per ton of capacity
- Higher thermal performance in given land area

**Slinky configuration:**
- Coiled pipe overlapping in trench
- Vertical slinky: 70-120 ft of trench per ton
- Horizontal slinky: 80-150 ft of trench per ton
- Pitch spacing: 12-24 inches between coil centers

**Horizontal Loop Design Criteria:**

Trench depth calculation:

d_min = d_frost + 2 ft

Where:
- d_min = minimum trench depth
- d_frost = local frost depth

Heat transfer per unit length varies with soil conditions:

| Soil Condition | Heat Transfer (Btu/hr·ft pipe) |
|----------------|--------------------------------|
| Dry soil (low moisture) | 12-18 |
| Average soil (moderate moisture) | 18-26 |
| Wet soil (high moisture) | 24-35 |
| Saturated soil or groundwater contact | 28-40 |

### Pond/Lake Closed-Loop Systems

Submerged loops in ponds or lakes provide excellent heat transfer due to water's thermal capacity and natural mixing. Minimum water body requirements:

**Pond Sizing Criteria:**

Volume requirement: 500-1000 gallons per ton of capacity
Surface area: Minimum 0.5 acre recommended
Depth: Minimum 8-10 ft year-round water depth

**Coil Placement:**

Depth: 10-20 ft below surface (below ice formation zone)
Spacing: 10-15 ft between coils minimum
Anchoring: Concrete or weighted supports to prevent floating
Heat transfer: 40-60 Btu/hr·ft² of coil surface area

**Performance Advantages:**

- Lowest installation cost when suitable water body exists
- Excellent thermal performance (water thermal conductivity = 0.35 Btu/hr·ft·°F)
- Natural convection enhances heat transfer
- Minimal land disturbance

**Design Limitations:**

- Water body must not freeze solid
- Minimum water quality requirements to prevent fouling
- Local regulations may restrict thermal discharge
- Potential for coil damage from debris or recreation activities

### Open-Loop (Groundwater) Systems

Open-loop systems pump groundwater directly through the heat pump heat exchanger, then discharge to drain, return well, or surface water. These systems achieve highest efficiency but require suitable aquifer conditions.

**Groundwater Requirements:**

Flow rate requirement: 1.5-3.0 gpm per ton of capacity

Water quality limits:

| Parameter | Maximum Recommended |
|-----------|---------------------|
| Total hardness | 350 ppm as CaCO₃ |
| Iron (Fe) | 0.3 ppm |
| Manganese (Mn) | 0.05 ppm |
| Hydrogen sulfide (H₂S) | 0.5 ppm |
| pH | 6.5-8.5 |
| Total dissolved solids | 1000 ppm |

**Well Design:**

Production well:
- Diameter: 4-6 inches minimum
- Depth: Adequate to reach aquifer with sufficient yield
- Screen: Sized for required flow with velocity less than 0.1 ft/sec
- Pump: Submersible, sized for total dynamic head plus heat exchanger pressure drop

Return well (standing column or reinjection):
- Located minimum 50-100 ft from production well
- Downgradient of production well in groundwater flow
- Adequate capacity to accept full discharge flow

**Standing Column Wells:**

Single deep well (300-1500 ft) with submersible pump drawing from bottom and discharging at top. Water circulates within well bore, exchanging heat with formation:

Required well depth (approximate):

L_well = (12,000 Btu/ton × Tons) / (40-80 Btu/hr·ft)

L_well = 150-300 ft per ton of capacity

Performance enhanced by "bleed" during peak loads, discharging 10-15% of flow to prevent temperature stacking.

## Ground Thermal Properties

### Thermal Conductivity Determination

Accurate ground thermal conductivity is critical for loop sizing. Determination methods include:

**In-Situ Thermal Response Test:**

Most accurate method involves installing test borehole, applying constant heat input, and measuring fluid temperature response over 48-72 hours.

Analysis uses line source equation:

T(r,t) = T_initial + (q / 4πk) × ln(4αt/r²C)

Where:
- T(r,t) = temperature at radius r and time t
- q = heat input per unit length (Btu/hr·ft)
- k = thermal conductivity (Btu/hr·ft·°F)
- α = thermal diffusivity (ft²/hr)
- r = radial distance from source (ft)
- C = Euler's constant (1.781)

Thermal conductivity is determined from slope of temperature vs. ln(time) plot.

**Laboratory Testing:**

Core samples analyzed with thermal needle probe or divided bar apparatus per ASTM D5334 or ASTM C177.

**Estimated Values:**

When testing is not feasible, use conservative estimates based on soil classification and moisture content:

| Formation Type | Thermal Conductivity Range (Btu/hr·ft·°F) | Design Value (Conservative) |
|----------------|-------------------------------------------|----------------------------|
| Gravel, dry | 0.15-0.30 | 0.18 |
| Gravel, saturated | 0.55-0.95 | 0.60 |
| Sand, dry | 0.15-0.25 | 0.18 |
| Sand, moist | 0.40-0.70 | 0.45 |
| Sand, saturated | 0.60-1.00 | 0.65 |
| Silt, moist | 0.50-0.85 | 0.55 |
| Silt, saturated | 0.70-1.00 | 0.75 |
| Clay, moist | 0.45-0.75 | 0.50 |
| Clay, saturated | 0.60-0.90 | 0.65 |
| Granite | 1.30-2.20 | 1.40 |
| Limestone | 0.85-1.80 | 1.00 |
| Sandstone | 0.90-1.70 | 1.00 |
| Shale | 0.70-1.30 | 0.80 |

Moisture content dramatically affects thermal conductivity. Saturated soils conduct 2-4 times better than dry soils due to water-filled pore spaces.

### Ground Thermal Resistance Components

Total effective ground thermal resistance comprises:

R_total = R_pipe + R_grout + R_soil

**Pipe thermal resistance:**

R_pipe = ln(d_outer/d_inner) / (2πk_pipe)

For 3/4-inch HDPE pipe (SDR-11):
- Inside diameter = 0.860 inch
- Outside diameter = 1.050 inch
- k_pipe = 0.23 Btu/hr·ft·°F
- R_pipe = 0.04 hr·ft·°F/Btu

**Grout thermal resistance:**

R_grout = ln(d_bore/d_pipe) / (2πk_grout × F_shape)

Where F_shape accounts for pipe configuration (U-tube geometry)

For 4-inch borehole, standard bentonite grout (k = 0.43 Btu/hr·ft·°F):
R_grout = 0.15-0.25 hr·ft·°F/Btu (depends on pipe spacing)

Thermally enhanced grout (k = 0.85-1.20 Btu/hr·ft·°F) reduces this resistance significantly:
R_grout = 0.08-0.14 hr·ft·°F/Btu

**Soil thermal resistance:**

Calculated using analytical solutions or numerical modeling accounting for:
- Borehole spacing and configuration
- Long-term ground temperature penalty from annual heat imbalance
- Short-term peak load effects

ASHRAE Handbook and IGSHPA design software provide resistance values based on these factors.

## Heat Transfer Fluid Selection

### Antifreeze Solutions

Ground loop systems require antifreeze to prevent freezing and provide corrosion protection. Common fluids include:

**Propylene Glycol:**

Most common choice for closed-loop systems due to low toxicity.

Freeze protection vs. concentration:

| Concentration (% by volume) | Freeze Point (°F) | Burst Point (°F) |
|-----------------------------|-------------------|------------------|
| 15% | 26 | 18 |
| 20% | 22 | 13 |
| 25% | 18 | 6 |
| 30% | 13 | -2 |
| 35% | 7 | -11 |
| 40% | 0 | -21 |
| 50% | -15 | -45 |

Design freeze protection: Select concentration providing freeze point 10-15°F below minimum expected loop temperature.

**Fluid Property Effects:**

Glycol solutions have lower thermal performance than water:

| Property (40% Propylene Glycol at 50°F) | Value vs. Water |
|-----------------------------------------|-----------------|
| Specific heat | 0.93 Btu/lb·°F (93% of water) |
| Thermal conductivity | 0.21 Btu/hr·ft·°F (60% of water) |
| Viscosity | 3.5 cP (350% of water) |
| Density | 64.3 lb/ft³ (103% of water) |

**Pressure Drop Correction:**

Reynolds number decreases due to higher viscosity:

Re = (ρ × V × D) / μ

Friction factor increases by factor of 1.3-1.6 for typical concentrations, requiring larger pipe sizes or increased pump power.

Flow rate must increase to compensate for reduced specific heat:

GPM_glycol = GPM_water / (c_p,glycol / c_p,water)

For 30% propylene glycol: multiply water flow rate by 1.05
For 40% propylene glycol: multiply water flow rate by 1.08

**Ethanol and Methanol:**

Less common due to higher toxicity, flammability concerns, and degradation over time. May be used in industrial applications with appropriate safety measures.

**Corrosion Inhibitors:**

All antifreeze solutions must contain corrosion inhibitors for metals in system:
- Copper and brass
- Steel (if used in manifolds)
- Aluminum (heat exchangers)

Check inhibitor concentration annually and maintain per manufacturer specifications.

## Loop Piping Design

### Pipe Materials

**High-Density Polyethylene (HDPE):**

Standard material for ground loop heat exchangers.

Material properties:
- ASTM D3035 or D2737
- PE 3408 or PE 4710 cell classification
- SDR-11 (pressure rating 160 psi at 73°F) or SDR-13.5 (130 psi)
- Thermal conductivity: 0.22-0.24 Btu/hr·ft·°F

Fusion welding methods:
- Butt fusion for straight joints
- Socket fusion for fittings
- Electrofusion for repairs

**Pipe Sizing:**

Vertical loops: Typically 3/4-inch or 1-inch
Horizontal loops: 3/4-inch to 1-1/4-inch
Headers: 1-1/4-inch to 4-inch depending on total flow

Velocity limits:
- Maximum: 5-6 ft/sec (noise and erosion control)
- Minimum: 2 ft/sec (air purging and suspension of particles)
- Design target: 3-4 ft/sec

Flow rate per loop circuit:

For 3/4-inch pipe at 3.5 ft/sec: approximately 4.5 gpm
For 1-inch pipe at 3.5 ft/sec: approximately 8 gpm

### Pressure Drop Calculations

Total system pressure drop determines required pump head:

ΔP_total = ΔP_loop + ΔP_header + ΔP_heatpump + ΔP_fittings

**Loop friction loss:**

Use Darcy-Weisbach equation:

ΔP = f × (L/D) × (ρV²/2)

For turbulent flow in smooth pipe:

f = 0.316 × Re^(-0.25)  (Blasius equation, 3,000 < Re < 100,000)

Practical calculation using flow coefficient:

ΔP (psi) = 0.002 × L × (GPM/100)^1.85 × (C/100)^-1.85 / D^4.86

Where:
- L = pipe length (ft)
- GPM = flow rate
- C = Hazen-Williams coefficient (150 for HDPE)
- D = pipe inside diameter (inches)

**Typical pressure drops:**

| Component | Pressure Drop Range |
|-----------|---------------------|
| Vertical borehole (200 ft, 3 gpm) | 2-4 psi |
| Horizontal trench (200 ft, 3 gpm) | 3-5 psi |
| Headers and distribution | 3-8 psi |
| Heat pump heat exchanger | 5-15 psi |
| Flow center and fittings | 2-5 psi |
| **Total system** | **15-35 psi** |

Design pump for total head plus 20% safety factor.

### Flow Balancing

Multiple loop circuits require balancing to ensure equal flow distribution.

**Reverse-Return Piping:**

Preferred method where each loop has equal pipe length for automatic balancing:
- Supply header runs parallel to return header
- Last loop supplied is first to return
- Equalizes pressure drop through all circuits

**Balance Valves:**

Direct-return systems require manual balancing valves:
- Install on return side of each loop
- Adjust to achieve equal temperature rise across all circuits
- Temperature difference between loops should be within 2-3°F

**Flow Measurement:**

Use inline flow meters or ultrasonic meters to verify:
- Total system flow matches design
- Individual circuits within 10% of target flow

Flow per circuit should be:

GPM_circuit = (Capacity_total × 12,000 Btu/ton) / (500 × ΔT_design × N_circuits)

Where:
- Capacity_total = total system capacity (tons)
- ΔT_design = design temperature difference (typically 8-12°F)
- N_circuits = number of parallel circuits

## Heat Pump Equipment Selection

### Water-to-Air Heat Pumps

Most common configuration for residential and light commercial applications.

**Performance Ratings:**

ASHRAE/ISO/AHRI Standard 13256-1 specifies rating conditions:

| Mode | Entering Water Temp | Entering Air Temp (DB/WB) |
|------|---------------------|---------------------------|
| Heating | 32°F | 70°F / - |
| Cooling | 77°F | 80°F / 67°F |

Manufacturer performance data typically includes:

**Heating Performance (32°F EWT, 70°F EAT):**

| Capacity (tons) | Heating Cap (Btu/hr) | Power Input (kW) | COP | CFM |
|-----------------|----------------------|------------------|-----|-----|
| 2 | 23,000 | 1.8 | 3.7 | 800 |
| 3 | 34,000 | 2.6 | 3.8 | 1200 |
| 4 | 46,000 | 3.5 | 3.8 | 1600 |
| 5 | 57,000 | 4.3 | 3.9 | 2000 |

**Cooling Performance (77°F EWT, 80/67°F EAT):**

| Capacity (tons) | Cooling Cap (Btu/hr) | Power Input (kW) | EER | CFM |
|-----------------|----------------------|------------------|-----|-----|
| 2 | 23,500 | 1.5 | 15.7 | 800 |
| 3 | 35,000 | 2.2 | 15.9 | 1200 |
| 4 | 47,000 | 2.9 | 16.2 | 1600 |
| 5 | 58,500 | 3.6 | 16.3 | 2000 |

**Performance Correction Factors:**

Capacity and power vary with entering water temperature:

Heating correction (from 32°F base):
- 20°F EWT: 85% capacity, 108% power
- 40°F EWT: 107% capacity, 95% power
- 50°F EWT: 114% capacity, 89% power

Cooling correction (from 77°F base):
- 60°F EWT: 109% capacity, 90% power
- 70°F EWT: 104% capacity, 95% power
- 90°F EWT: 93% capacity, 108% power

### Water-to-Water Heat Pumps

Used for hydronic heating/cooling systems with radiant panels, fan coils, or air handlers.

**Rating Conditions (ASHRAE/ISO/AHRI Standard 13256-2):**

| Mode | Entering Source Water | Entering Load Water |
|------|----------------------|---------------------|
| Heating | 32°F | 68°F |
| Cooling | 77°F | 54°F |

**Typical Performance:**

| Capacity (tons) | Heating Cap (Btu/hr) | Heating COP | Cooling Cap (Btu/hr) | Cooling EER |
|-----------------|----------------------|-------------|----------------------|-------------|
| 3 | 32,000 | 3.4 | 33,000 | 13.5 |
| 6 | 64,000 | 3.5 | 66,000 | 13.8 |
| 10 | 107,000 | 3.6 | 110,000 | 14.2 |
| 15 | 160,000 | 3.7 | 165,000 | 14.5 |

### Desuperheater Hot Water Generation

Heat pumps can be equipped with desuperheaters to recover superheat for domestic hot water production:

Typical recovery rate:
- Heating mode: 15-25% of total heating capacity
- Cooling mode: 20-30% of total cooling capacity

For 3-ton heat pump in cooling mode:
- Total cooling rejection = 36,000 + 10,260 = 46,260 Btu/hr
- Desuperheater recovery = 9,000-13,800 Btu/hr
- Hot water production = 15-23 gallons/hr (50°F rise to 140°F)

Installation requires:
- Storage tank with dual heat source capability (80-120 gallons typical)
- Tempering valve for scalding prevention
- Recirculation pump for desuperheater circuit

## System Performance Analysis

### Seasonal Performance

The seasonal coefficient of performance (SCOP) accounts for varying operating conditions throughout the year:

SCOP = Total_annual_output / Total_annual_input

For ground source heat pumps:

SCOP_heating = 3.0 - 4.2 (depending on climate and system design)
SCOP_cooling = 3.5 - 5.0

Compare to air-source heat pumps:
SCOP_heating = 2.0 - 3.2
SCOP_cooling = 2.8 - 4.0

**Factors Affecting Seasonal Performance:**

Ground loop sizing adequacy:
- Undersized loops experience temperature degradation over time
- Temperature penalty reduces efficiency by 2-5% per °F deviation from design

Annual heat balance:
- Heating-dominated climates extract net heat from ground
- Cooling-dominated climates reject net heat to ground
- Imbalanced loads cause ground temperature drift over multiple years

Part-load operation:
- Heat pumps cycle at part load, reducing efficiency 5-15%
- Variable-speed compressors improve part-load performance

Pump energy:
- Circulation pump energy typically 3-8% of heat pump energy
- Poor loop design with high pressure drop increases pumping penalty

### Energy Use Calculations

Annual energy consumption for GSHP system:

**Heating Energy:**

E_heating = (Heating_load × Hours) / (SCOP × 3,412 Btu/kWh)

For 60,000 Btu/hr peak load, 2,000 heating hours, SCOP = 3.8:

E_heating = (60,000 × 2,000) / (3.8 × 3,412) = 9,260 kWh

**Cooling Energy:**

E_cooling = (Cooling_load × Hours) / (SCOP × 3,412 Btu/kWh)

For 48,000 Btu/hr peak load, 1,200 cooling hours, SCOP = 4.5:

E_cooling = (48,000 × 1,200) / (4.5 × 3,412) = 3,750 kWh

**Circulation Pump Energy:**

E_pump = (Horsepower × 0.746 kW/HP × Operating_hours) / η_motor

For 1/2 HP pump, 90% motor efficiency, 3,200 hours:

E_pump = (0.5 × 0.746 × 3,200) / 0.90 = 1,325 kWh

**Total Annual Energy:**

E_total = E_heating + E_cooling + E_pump = 14,335 kWh

Compare to conventional equipment:
- Air-source heat pump: 18,000-22,000 kWh
- Natural gas furnace + AC: 1,200 therms + 5,500 kWh

### Economic Analysis

Life-cycle cost analysis for GSHP systems:

**Initial Costs:**

| Component | Cost Range |
|-----------|------------|
| Heat pump equipment | $3,000-$6,500 per ton |
| Vertical loop installation | $12-$25 per foot of bore |
| Horizontal loop installation | $6-$12 per foot of trench |
| Distribution system | $2,000-$8,000 |
| Labor and controls | $3,000-$8,000 |
| **Total system** | **$20,000-$35,000 for 3-ton residential** |

Vertical loops dominate installed cost:
- 3-ton system requiring 900 ft total bore depth
- Installation cost: 900 × $18 = $16,200 for loops alone

**Operating Cost Savings:**

Annual savings vs. conventional system:
- Electric resistance heat: $1,500-$2,500 per year
- Air-source heat pump: $400-$900 per year
- Natural gas furnace/AC: $300-$700 per year (varies with gas prices)

**Simple Payback:**

Payback = (GSHP_cost - Conventional_cost) / Annual_savings

For 3-ton residential replacing air-source HP:
- Incremental cost: $8,000-$12,000
- Annual savings: $500-$800
- Simple payback: 10-20 years

**Life-Cycle Cost:**

Present value analysis over 25-year equipment life:

PV = Initial_cost + Σ(Operating_cost / (1+discount_rate)^year)

GSHP systems typically show positive net present value when:
- System properly sized and installed
- Electricity rates exceed $0.10/kWh
- Building has significant heating and cooling loads
- Equipment operates for full design life (20-25 years)

Federal tax credits, state incentives, and utility rebates can reduce payback to 5-12 years in many markets.

## Design Standards and References

**ASHRAE Standards:**

- ASHRAE Handbook - HVAC Applications, Chapter 34: Geothermal Energy
- ASHRAE Standard 13256-1: Water-to-Air Heat Pumps
- ASHRAE Standard 13256-2: Water-to-Water Heat Pumps

**IGSHPA Standards:**

- Design and Installation Standards for Closed-Loop Ground Source Heat Pump Systems
- Grouting Procedures for Ground Source Heat Pump Systems
- Loop Installation Standards

**Industry Organizations:**

- International Ground Source Heat Pump Association (IGSHPA)
- Geothermal Exchange Organization (GEO)
- ASHRAE Technical Committee 6.8 (Geothermal Heat Pumps and Energy Recovery)

**Software Tools:**

- GLD (Ground Loop Design) - for vertical loop sizing using g-functions
- GLHEPRO - comprehensive ground loop heat exchanger design
- EnergyPlus - whole-building energy simulation with ground loop models

Proper system design requires detailed analysis using professional design software, validated with thermal response testing when project scale justifies the expense. Conservative estimates and adequate safety factors prevent undersizing, which leads to long-term performance degradation and system failure.
