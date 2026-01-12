---
title: "Geothermal HVAC Systems"
description: "Ground source heat pumps, geothermal loop design, ground thermal properties, sizing calculations, COP performance analysis, vertical and horizontal ground heat exchangers for energy-efficient HVAC applications"
weight: 3
---

## Ground Source Heat Pump Fundamentals

Ground source heat pumps (GSHPs) exploit the relatively constant temperature of the earth below the frost line to provide highly efficient heating and cooling. The ground serves as a heat source during winter and a heat sink during summer, offering superior performance compared to air-source equipment.

### Thermodynamic Principles

The earth maintains relatively stable temperatures at depths below 10-15 ft, typically ranging from 45°F to 75°F depending on geographic location. This temperature stability provides:

- Consistent heat source temperature during heating mode
- Lower condensing temperature during cooling mode
- Reduced compressor lift compared to air-source systems
- More efficient operation across seasonal variations

**Heat Transfer Mechanism:**

The refrigeration cycle in a GSHP operates between the ground loop fluid temperature and the building load temperature. During heating:

Q_heating = ṁ_fluid × c_p × (T_return - T_supply)

Where:
- Q_heating = Heat extracted from ground (Btu/hr)
- ṁ_fluid = Mass flow rate of loop fluid (lb/hr)
- c_p = Specific heat of loop fluid (Btu/lb·°F)
- T_return, T_supply = Loop fluid temperatures (°F)

### System Components

**Heat Pump Unit:**
- Water-to-air or water-to-water heat pump
- Reversing valve for heating/cooling operation
- Internal circulation pump or external pump package
- Desuperheater for domestic hot water recovery

**Ground Loop:**
- High-density polyethylene (HDPE) pipe
- Heat transfer fluid (water or antifreeze solution)
- Manifold and header assemblies
- Flow control and balancing valves

**Distribution System:**
- Forced air ductwork or hydronic distribution
- Supplemental heating equipment (if required)
- Buffer tanks for water-to-water systems

## Ground Loop Configuration Types

### Vertical Closed-Loop Systems

Vertical boreholes represent the most common commercial GSHP installation due to minimal land area requirements and consistent thermal performance.

**Design Parameters:**

| Parameter | Typical Range | Notes |
|-----------|---------------|-------|
| Borehole depth | 150-500 ft | Deeper in limited space |
| Borehole diameter | 4-6 inches | Standard rotary drilling |
| Pipe configuration | U-tube or coaxial | U-tube most common |
| Pipe diameter | 3/4" to 1-1/4" | Based on flow requirements |
| Borehole spacing | 15-20 ft minimum | Prevents thermal interference |

**U-Tube Configuration:**

The standard U-tube consists of two pipes connected at the bottom with a U-bend. Heat transfer fluid flows down one leg and returns through the other. Key considerations:

- Pipe separation within borehole affects thermal performance
- Grout thermal conductivity critical for heat transfer
- Thermally enhanced grout (k = 1.2-1.4 Btu/hr·ft·°F) improves performance
- Standard bentonite grout (k = 0.4-0.6 Btu/hr·ft·°F) reduces capacity

**Grout Requirements:**

Proper grouting ensures:
- Thermal contact between pipe and formation
- Prevention of groundwater contamination
- Borehole structural stability
- Regulatory compliance

**Installation Considerations:**

Vertical loop installation requires:
- Geological survey to identify subsurface conditions
- Drilling permits and regulatory approvals
- Thermal response testing for large projects (>50 tons)
- Quality control during grouting operations

### Horizontal Closed-Loop Systems

Horizontal loops install in trenches at depths below the frost line, typically 6-10 ft deep. This configuration suits residential applications with adequate land area.

**Layout Options:**

**Single Pipe Configuration:**
- One pipe per trench
- 6-8 ft trench depth
- Pipe spacing 6-10 ft on center
- Requires 400-600 ft per ton of capacity

**Double Pipe Configuration:**
- Two pipes per trench at different depths
- Reduces land area by 30-40%
- Upper pipe at 6 ft, lower at 8-10 ft
- Improved thermal performance

**Slinky Configuration:**
- Coiled pipe layout in trench
- Reduces trench length by 50-60%
- 3-4 ft diameter coils with 6-12" pitch
- Overlapped or spaced coil arrangements
- Requires 150-250 ft per ton

**Design Calculations:**

Required trench length:

L_trench = Q_design / (q_ground × F_run)

Where:
- L_trench = Total trench length (ft)
- Q_design = Design heating or cooling load (Btu/hr)
- q_ground = Ground heat transfer rate (Btu/hr·ft)
- F_run = Run fraction adjustment factor

### Pond/Lake Loop Systems

Submerged loops in ponds or lakes offer cost-effective installation when suitable water bodies exist.

**Requirements:**

- Minimum water depth: 8-10 ft
- Adequate water volume: 0.5-1 acre per 50 tons
- Water quality considerations for long-term durability
- Regulatory permits for submerged installations

**Installation Details:**

Coiled pipe assemblies attach to weighted frames on the lake bottom. Multiple coils connect in parallel to achieve required capacity:

- Coil diameter: 3-4 ft
- Coil spacing: 10-15 ft minimum
- Pipe burial in sediment for thermal contact
- Anchoring system to prevent flotation

### Open-Loop Systems

Open-loop systems pump groundwater directly through the heat pump heat exchanger, then discharge to a drainage field, surface water, or reinjection well.

**Advantages:**
- Lower installation cost (no ground loop)
- Excellent thermal performance
- Reduced pump energy

**Limitations:**
- Water quality requirements
- Availability of suitable aquifer
- Regulatory restrictions on discharge
- Potential fouling or scaling
- Mineral content affects heat exchanger

**Water Quality Parameters:**

| Parameter | Acceptable Range | Impact |
|-----------|------------------|--------|
| pH | 6.5-8.5 | Corrosion/scaling |
| Hardness | <10 grains/gal | Scaling potential |
| Iron | <0.3 ppm | Fouling |
| Manganese | <0.05 ppm | Fouling |
| Hydrogen sulfide | <0.5 ppm | Corrosion |
| Total dissolved solids | <500 ppm | Scaling |

## Ground Thermal Properties

Ground thermal conductivity and diffusivity determine heat transfer capability and long-term system performance.

### Thermal Conductivity

Thermal conductivity (k) quantifies heat transfer through soil or rock:

| Material | Thermal Conductivity (Btu/hr·ft·°F) | Notes |
|----------|-------------------------------------|-------|
| Dry sand | 0.2-0.4 | Poor performance |
| Moist sand | 0.6-1.2 | Moisture critical |
| Clay (saturated) | 0.6-0.9 | Varies with moisture |
| Rock (granite) | 1.5-2.5 | Excellent performance |
| Rock (sandstone) | 1.0-1.8 | Good performance |
| Rock (limestone) | 1.3-2.2 | Good performance |

**Moisture Content Impact:**

Water dramatically increases thermal conductivity. Saturated soil transfers heat 3-5 times more effectively than dry soil. Groundwater movement further enhances performance through advective heat transfer.

### Thermal Diffusivity

Thermal diffusivity (α) indicates how quickly temperature changes propagate through ground:

α = k / (ρ × c_p)

Where:
- k = Thermal conductivity (Btu/hr·ft·°F)
- ρ = Density (lb/ft³)
- c_p = Specific heat (Btu/lb·°F)

High diffusivity allows ground to recover heat faster between heating/cooling cycles.

### Undisturbed Ground Temperature

Ground temperature below the frost line approximates mean annual air temperature plus 2-4°F. Regional variation affects GSHP performance:

- Northern climates: 45-50°F ground temperature
- Mid-latitude climates: 50-60°F ground temperature
- Southern climates: 60-75°F ground temperature

### Thermal Response Testing

Large commercial projects require thermal response testing to determine actual ground thermal properties. The test involves:

1. Install test borehole with instrumented U-tube
2. Apply constant heat input for 48-72 hours
3. Monitor fluid temperature response
4. Analyze temperature data to determine:
   - Effective ground thermal conductivity
   - Borehole thermal resistance
   - Undisturbed ground temperature

Test results guide final system design and prevent undersizing.

## Ground Loop Sizing Calculations

Proper sizing ensures adequate heat transfer capacity without excessive installation cost.

### Heating Mode Sizing

The ground loop must reject heat from the building plus compressor heat during heating operation:

Q_loop,heating = Q_building,heating × (1 + 1/COP_heating)

For a 100,000 Btu/hr heating load with COP = 3.5:

Q_loop,heating = 100,000 × (1 + 1/3.5) = 128,600 Btu/hr

### Cooling Mode Sizing

During cooling, the loop absorbs heat from the building plus compressor heat:

Q_loop,cooling = Q_building,cooling × (1 + 1/EER)

For a 120,000 Btu/hr cooling load with EER = 18:

Q_loop,cooling = 120,000 × (1 + 1/18) = 126,700 Btu/hr

### Loop Length Calculation

**Vertical Loop:**

L_vertical = Q_loop / q_vertical

Where q_vertical depends on:
- Ground thermal conductivity
- Run hours and load profile
- Ground temperature
- Loop fluid temperature limits

Typical values: q_vertical = 15-25 Btu/hr·ft in heating, 20-35 Btu/hr·ft in cooling

**Example Calculation:**

For 128,600 Btu/hr loop requirement with q_vertical = 20 Btu/hr·ft:

L_vertical = 128,600 / 20 = 6,430 ft

This requires approximately 32 boreholes at 200 ft depth.

### Detailed Design Methods

**Cylindrical Heat Source Method:**

Accounts for transient heat transfer from borehole:

T_loop = T_ground + (q × R_ground) + (q × R_borehole)

Where:
- T_loop = Loop fluid temperature (°F)
- T_ground = Undisturbed ground temperature (°F)
- q = Heat flux per unit length (Btu/hr·ft)
- R_ground = Ground thermal resistance (hr·ft·°F/Btu)
- R_borehole = Borehole thermal resistance (hr·ft·°F/Btu)

### Ground Loop Design Software

Professional design software accounts for:
- Hourly building loads
- Ground thermal properties
- Short-term and long-term ground temperature changes
- Minimum/maximum entering water temperature limits
- Multi-year ground thermal balance
- Hybrid system optimization

Common software tools include GLHEPRO, GLD, and EED.

## Coefficient of Performance Analysis

GSHP systems achieve superior COP compared to air-source equipment due to favorable source/sink temperatures.

### Heating Mode COP

COP_heating = Q_delivered / W_compressor

Typical GSHP heating COP ranges from 3.0 to 5.0, meaning 3-5 units of heat delivered per unit of electrical energy consumed.

**Temperature Impact:**

COP increases as entering water temperature (EWT) increases:

| EWT (°F) | COP_heating | Notes |
|----------|-------------|-------|
| 30 | 2.8-3.2 | Minimum design |
| 40 | 3.3-3.8 | Standard design |
| 50 | 3.8-4.5 | Favorable conditions |
| 60 | 4.3-5.2 | Optimal performance |

### Cooling Mode EER

Energy efficiency ratio (EER) in cooling mode:

EER = Q_removed / W_compressor (Btu/hr per Watt)

Typical GSHP cooling EER ranges from 15 to 25 Btu/hr·W.

**Temperature Impact:**

EER decreases as entering water temperature increases:

| EWT (°F) | EER | Notes |
|----------|-----|-------|
| 60 | 22-26 | Optimal performance |
| 70 | 18-22 | Standard design |
| 80 | 15-18 | Maximum design |
| 90 | 12-15 | Degraded performance |

### Seasonal Performance

Seasonal COP accounts for varying loads and temperatures throughout the year:

COP_seasonal = Σ(Q_delivered,i) / Σ(W_input,i)

Well-designed GSHP systems achieve seasonal heating COP of 3.5-4.2 and cooling EER of 16-20.

### Performance Comparison

**Ground Source vs Air Source (Heating at 17°F outdoor):**

| Parameter | GSHP (50°F EWT) | ASHP (17°F outdoor) |
|-----------|-----------------|---------------------|
| COP | 3.8 | 2.2 |
| Capacity degradation | Minimal | 30-40% reduction |
| Defrost cycles | None | Every 45-90 min |
| Supplemental heat | Rarely needed | Often required |

### Part-Load Performance

GSHP systems maintain high efficiency at part load due to:
- Variable-speed compressor technology
- Favorable source temperature throughout operation
- Minimal cycling losses
- No defrost penalties

Part-load integrated energy efficiency ratio (IEER) often exceeds full-load EER by 10-20%.

## System Design Considerations

### Loop Fluid Selection

**Water:**
- Used where loop temperature remains above 32°F
- Best heat transfer properties
- Lowest pumping energy
- Lowest cost

**Antifreeze Solutions:**

Required when loop temperature may drop below 32°F:

| Solution | Freeze Protection | Heat Transfer | Notes |
|----------|-------------------|---------------|-------|
| Ethanol | -20°F at 22% | Reduced 5-8% | Renewable |
| Propylene glycol | -20°F at 25% | Reduced 8-12% | Safe, non-toxic |
| Methanol | -20°F at 20% | Reduced 4-6% | Toxic, avoid |

### Flow Rate Requirements

Loop flow rate affects heat transfer and pumping energy:

ṁ = Q_loop / (c_p × ΔT_design)

Typical design temperature difference: 8-12°F

For 128,600 Btu/hr with 10°F ΔT and water (c_p = 1.0 Btu/lb·°F):

ṁ = 128,600 / (1.0 × 10) = 12,860 lb/hr = 25.7 gpm

Target flow rate: 2.5-3.0 gpm per ton of capacity

### Pump Selection

Circulation pump must overcome:
- Ground loop piping friction loss
- Heat pump heat exchanger pressure drop
- Manifold and header losses
- Fittings and valve losses

Total head typically ranges from 30-60 ft for residential systems and 60-150 ft for commercial systems.

**Pump Energy:**

W_pump = (GPM × H_total × ρ) / (3960 × η_pump)

Where:
- GPM = Flow rate (gallons per minute)
- H_total = Total dynamic head (ft)
- ρ = Fluid density (lb/gal)
- η_pump = Pump efficiency (0.6-0.8)

### Piping Design

**Sizing:**

Pipe velocity should remain between 2-5 ft/sec to balance pressure drop and heat transfer:

- Low velocity (<2 ft/sec): Poor heat transfer, air separation issues
- High velocity (>5 ft/sec): Excessive pressure drop, erosion, noise

**Pressure Drop:**

Calculate using Darcy-Weisbach equation:

ΔP = f × (L/D) × (ρ × V²/2)

Or use friction loss charts for HDPE pipe with water/glycol mixtures.

## Economic Analysis

### Installation Costs

**Vertical Loop System:**

| Component | Cost Range | Notes |
|-----------|------------|-------|
| Drilling | $10-$30/ft | Varies with geology |
| Loop piping | $2-$4/ft | HDPE material and fusion |
| Grouting | $3-$6/ft | Thermally enhanced grout |
| Header piping | $8-$15/ton | Distribution to heat pump |
| Total loop installed | $2,000-$4,000/ton | Complete ground loop |

**Heat Pump Equipment:**

- Water-to-air heat pump: $1,200-$2,500/ton
- Water-to-water heat pump: $1,500-$3,000/ton
- Installation and controls: $800-$1,500/ton

**Total System Cost:**

Complete GSHP system: $4,000-$8,000/ton installed

### Operating Cost Comparison

**Annual Energy Cost Example (3-ton residential system):**

System assumptions:
- Heating load: 30 MMBtu/year
- Cooling load: 18 MMBtu/year
- Electric rate: $0.12/kWh
- Natural gas: $1.20/therm

| System Type | Heating Cost | Cooling Cost | Total Annual |
|-------------|--------------|--------------|--------------|
| GSHP (COP 3.8, EER 18) | $280 | $210 | $490 |
| ASHP (COP 2.5, EER 12) | $430 | $315 | $745 |
| Gas furnace/AC (80% AFUE, SEER 13) | $380 | $295 | $675 |

Annual savings: $185-$255 compared to conventional systems

### Payback Period

Simple payback = (GSHP cost - Conventional cost) / Annual savings

For 3-ton system:
- GSHP cost: $21,000
- Conventional cost: $12,000
- Additional investment: $9,000
- Annual savings: $220
- Simple payback: 41 years

However, considering:
- 30% federal tax credit (if applicable): $6,300 credit
- Net additional cost: $2,700
- Payback: 12 years

### Life Cycle Cost Analysis

GSHP systems offer favorable life cycle economics:

- Ground loop life: 50+ years
- Heat pump life: 20-25 years (vs 15 years for conventional)
- Lower maintenance costs
- Reduced HVAC energy consumption
- Potential utility incentives

20-year net present value analysis typically shows GSHP advantage of $5,000-$15,000 for residential applications.

## Maintenance Requirements

GSHP systems require minimal maintenance due to protected indoor location and no outdoor coil exposure.

**Annual Maintenance:**

- Air filter replacement (monthly to quarterly)
- Coil cleaning if needed
- Refrigerant charge verification
- Electrical connection inspection
- Condensate drain maintenance

**Every 3-5 Years:**

- Loop fluid analysis (pH, concentration, inhibitor level)
- Circulation pump inspection
- Control calibration
- System performance verification

**Ground Loop:**

The buried ground loop requires virtually no maintenance. HDPE pipe carries 50-year warranty and has demonstrated service life exceeding 100 years in water distribution applications.

## Performance Verification

### Commissioning Procedures

**Loop Pressure Testing:**
- Pressurize loop to 100 psi for 24 hours
- Verify no pressure loss
- Check for air pockets

**Flow Verification:**
- Measure flow rate at design conditions
- Verify proper flow distribution in multiple loops
- Balance flow if needed

**Performance Testing:**
- Measure entering/leaving water temperatures
- Verify proper temperature drop/rise
- Confirm power draw and capacity
- Calculate actual COP or EER

### Monitoring

Continuous monitoring should track:
- Loop supply and return temperatures
- Heat pump power consumption
- Delivered heating/cooling energy
- Flow rates
- System runtime hours

Data analysis identifies performance degradation or operational issues.

## Environmental Benefits

GSHP systems provide significant environmental advantages:

**Reduced Greenhouse Gas Emissions:**

Compared to natural gas furnace/electric AC:
- 30-40% reduction in CO₂ emissions
- 40-50% reduction when powered by renewable electricity

**Refrigerant:**

Modern GSHPs use R-410A or other low-GWP refrigerants in factory-sealed systems with minimal charge and low leakage rates.

**Renewable Energy:**

Ground-coupled systems harvest solar energy stored in the earth, representing a renewable thermal resource that regenerates annually.

**No Combustion:**

Electric GSHP operation eliminates:
- Carbon monoxide risk
- NOx emissions
- Combustion air requirements
- Flue gas disposal

This comprehensive overview addresses ground source heat pump technology, loop configurations, thermal properties, design calculations, and performance analysis required for successful GSHP system implementation.
