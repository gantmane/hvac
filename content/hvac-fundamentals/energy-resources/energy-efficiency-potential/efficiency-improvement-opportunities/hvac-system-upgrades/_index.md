---
title: "HVAC System Upgrades"
weight: 1
---

## Overview

HVAC system upgrades represent capital investments that modernize existing equipment and systems to improve energy efficiency, operational performance, and occupant comfort. Strategic upgrades target the greatest energy consumers and inefficiencies in building systems, delivering measurable returns through reduced operating costs.

Upgrade decisions require analysis of existing equipment age, efficiency, operating costs, and remaining service life balanced against capital investment requirements and projected savings. Well-selected upgrades typically achieve simple paybacks of 2-7 years while improving system reliability and reducing maintenance requirements.

## High Efficiency Equipment Replacement

### Chiller Replacement

Modern high-efficiency chillers deliver substantial improvements over equipment manufactured prior to 2000:

| Equipment Age | Typical Efficiency | Modern Efficiency | Improvement |
|---------------|-------------------|-------------------|-------------|
| Pre-1990 chillers | 0.8-1.2 kW/ton | 0.45-0.55 kW/ton | 40-60% |
| 1990-2000 chillers | 0.6-0.8 kW/ton | 0.45-0.55 kW/ton | 25-40% |
| 2000-2010 chillers | 0.55-0.65 kW/ton | 0.45-0.55 kW/ton | 15-25% |

Replacement considerations:
- Centrifugal chillers with magnetic bearing compressors eliminate oil lubrication systems and improve part-load efficiency
- Variable-speed drives on compressors enable efficient modulation across load ranges
- Advanced refrigerants (R-1233zd, R-514A, R-515B) provide lower GWP alternatives with comparable efficiency
- Water-cooled chillers typically justify replacement at 20-25 years, air-cooled at 15-20 years

### Boiler Upgrades

Condensing boilers extract latent heat from flue gases, achieving thermal efficiencies of 90-96% compared to 80-85% for conventional non-condensing boilers.

Key performance factors:
- Return water temperature must remain below 130-140°F to enable condensing operation
- Corrosion-resistant heat exchangers (stainless steel, aluminum) withstand acidic condensate
- Modulating burners maintain high efficiency across 20-100% firing rates
- Integrated controls optimize staging and rotation of multiple boiler modules

Applications favoring condensing boilers:
- Radiant heating systems with design water temperatures of 100-120°F
- Low-temperature hydronic systems with outdoor reset controls
- Domestic water heating with continuous loads
- Retrofit projects where return water temperatures can be reduced

### Packaged Rooftop Unit Replacement

Modern rooftop units incorporate multiple efficiency technologies:

**Cooling efficiency improvements:**
- Variable-speed compressors with scroll or screw technology
- Microchannel heat exchangers reduce refrigerant charge 40-60%
- Variable-speed condenser fans modulate to optimize head pressure
- Improved insulation and seal design minimize cabinet losses

**Heating efficiency improvements:**
- Condensing gas heating sections achieve 90-95% thermal efficiency
- Hot gas reheat eliminates electric resistance heating for humidity control
- Integrated economizers reduce mechanical cooling requirements

Typical efficiency progression:

| Technology Generation | EER | IEER | Heating Efficiency |
|----------------------|-----|------|-------------------|
| Pre-2006 standard | 8-10 | 9-11 | 78-80% AFUE |
| 2006-2018 standard | 11-12 | 13-15 | 80-83% AFUE |
| Current high-efficiency | 13-15 | 16-20 | 90-95% thermal |

## Variable Frequency Drives

VFDs control motor speed by varying frequency and voltage supplied to three-phase motors, reducing energy consumption through affinity laws.

### Affinity Law Relationships

Motor speed changes directly impact power consumption:

**For centrifugal fans and pumps:**
- Flow rate ∝ Speed (Q₂/Q₁ = N₂/N₁)
- Pressure ∝ Speed² (P₂/P₁ = (N₂/N₁)²)
- Power ∝ Speed³ (kW₂/kW₁ = (N₂/N₁)³)

Operating a fan or pump at 80% speed reduces power consumption to 51% of full speed power. At 50% speed, power drops to 12.5% of full speed operation.

### Priority Applications

**Chilled water pumps:**
- Variable flow systems eliminate constant flow requirements
- Primary-secondary configurations convert to variable primary flow
- Energy savings of 30-60% compared to constant volume operation
- Minimum flow requirements prevent chiller evaporator freezing

**Condenser water pumps:**
- Pump speed modulates with chiller loading
- Energy savings of 25-50% at part-load conditions
- Coordinate with cooling tower fan control for optimal system performance

**Cooling tower fans:**
- VFDs replace two-speed motors or damper controls
- Maintain approach temperature while minimizing fan power
- Energy savings of 40-70% compared to on-off control
- Reduced mechanical stress extends fan and drive service life

**Air handling unit supply fans:**
- Enable true variable air volume operation
- Maintain duct static pressure setpoints
- Energy savings of 30-50% compared to inlet vane damper control
- Coordinate with VAV box damper positions for optimal setpoint

**Exhaust and return fans:**
- Track supply fan operation maintaining building pressure control
- Laboratory and healthcare applications with critical pressure relationships
- Energy savings of 25-45% compared to constant volume operation

### VFD Selection Considerations

Critical parameters:
- Motor horsepower and full-load amperage determine VFD sizing
- Harmonic mitigation requirements (IEEE 519-2014 compliance)
- Bypass capability for critical applications requiring backup operation
- Environmental conditions (temperature, humidity, contamination) affect enclosure selection

Installation requirements:
- Line reactors or isolation transformers reduce harmonic distortion
- Proper conductor sizing accounts for harmonic heating effects
- Separation of VFD output cables from control wiring prevents interference
- Ventilation requirements maintain VFD component temperatures within operating limits

## Economizer Systems

Economizers use outdoor air to provide "free cooling" when outdoor conditions permit, reducing mechanical cooling energy.

### Economizer Types

**Dry-bulb economizer:**
- Compares outdoor dry-bulb temperature to return air temperature
- Simple control logic with single temperature sensor
- Appropriate for dry climates where enthalpy control provides minimal additional benefit
- Typically enables economizer operation when T_outdoor < 55-65°F

**Enthalpy economizer:**
- Compares outdoor air enthalpy to return air enthalpy
- Accounts for both temperature and humidity content
- Maximizes economizer hours in humid climates
- Requires accurate enthalpy sensors or paired temperature/humidity sensors

### Integration Strategies

**Airside economizer with DX cooling:**
- Minimum outdoor air damper modulates to 100% when conditions permit
- Compressor stages off during economizer operation
- Return air damper closes to maximize outdoor air intake
- Mixed air temperature control prevents coil freeze-up

**Waterside economizer with chilled water systems:**
- Plate-and-frame heat exchanger transfers heat from chilled water loop to condenser water
- Enables "free cooling" when cooling tower provides sufficiently cold water
- Integrated economizer/chiller control optimizes transition between modes
- Typical operation when T_wetbulb < 45-50°F

Energy savings potential:
- Airside economizers reduce cooling energy 15-40% depending on climate
- Waterside economizers save 20-50% of annual chiller energy in favorable climates
- Greatest benefit in climates with significant temperature variation and moderate humidity

## Heat Recovery Systems

Heat recovery captures thermal energy from exhaust airstreams or condenser heat rejection for productive use.

### Run-Around Loops

Two coils connected by piping loop transfer heat between airstreams:
- Exhaust air coil captures heat before discharge
- Outdoor air coil preheats incoming ventilation air
- Glycol solution circulates between coils
- Pump moves fluid from warm coil to cold coil

Performance characteristics:
- Effectiveness: 45-65% depending on coil size and flow rates
- No cross-contamination between airstreams
- Coils can be separated by significant distances
- Requires pumping energy (typically 0.5-1.5 HP per 10,000 CFM)

### Energy Recovery Wheels

Rotating wheel transfers both sensible and latent heat:
- Desiccant-coated wheel absorbs moisture from exhaust air
- Wheel rotates into supply airstream releasing captured heat and moisture
- Total effectiveness: 70-85% (sensible plus latent)
- Sensible effectiveness: 65-80%

Application considerations:
- Cross-contamination potential requires evaluation for laboratory, healthcare applications
- Purge section reduces carryover to less than 1%
- Requires minimal pressure drop (0.5-1.0 in. w.c. each airstream)
- Motor power approximately 0.1-0.2 HP per 10,000 CFM

### Condenser Heat Recovery

Captures rejected heat from refrigeration cycle for water heating:
- Desuperheater recovers superheat from compressor discharge gas
- Full condenser heat recovery captures total heat of rejection
- Efficiency: COP of 3-5 for water heating (3-5 units heat per unit electricity)

Typical applications:
- Domestic water heating in facilities with year-round cooling loads
- Pool and spa heating at recreation facilities
- Process water heating in industrial facilities
- Space heating in buildings with simultaneous heating and cooling needs

## Controls Upgrades

Advanced control systems optimize equipment operation and enable sophisticated energy management strategies.

### Building Automation System Integration

Modern BAS platforms provide:
- Web-based interfaces accessible from any network device
- Trend logging and analysis identifying operational inefficiencies
- Scheduling optimization preventing unnecessary equipment operation
- Alarm management directing attention to critical issues

Integration capabilities:
- BACnet, Modbus, LonWorks protocol support enables multi-vendor integration
- Equipment-level controllers retain standalone capability during network failures
- Cloud-based analytics platforms identify optimization opportunities
- Mobile applications enable remote monitoring and adjustment

### Demand-Based Ventilation Control

CO₂ sensors modulate outdoor air based on actual occupancy:
- Sensors measure return air CO₂ concentration
- Controls increase outdoor air when CO₂ exceeds setpoint (typically 1000 ppm)
- Reduces outdoor air during unoccupied or lightly occupied periods
- Energy savings of 20-40% on ventilation heating and cooling loads

### Optimal Start-Stop Control

Algorithms minimize unoccupied equipment operation:
- System learns thermal mass and equipment capacity characteristics
- Calculates latest start time to achieve occupancy temperature
- Adjusts start time based on outdoor temperature
- Typical energy savings 5-15% of heating and cooling energy

### Supply Air Temperature Reset

Increases supply air temperature when cooling loads permit:
- Monitors VAV box damper positions throughout building
- Increases supply air temperature when dampers are not fully open
- Reduces mechanical cooling and simultaneous reheat energy
- Typical savings 10-25% of cooling energy in VAV systems

### Chilled Water Temperature Reset

Raises chilled water supply temperature based on cooling load:
- Monitors valve positions at critical cooling coils
- Increases CHW supply temperature when valves not fully open
- Improves chiller efficiency at elevated temperatures
- Reduces pumping energy through increased temperature differential
- Energy savings 5-15% of chiller plant energy

## Return on Investment Analysis

### Energy Savings Calculation

Annual energy cost savings:
- ΔEnergy = (Energy_baseline - Energy_upgraded) × Operating_hours
- Cost_savings = ΔEnergy × Energy_rate

Consider time-of-use rates and demand charges:
- Peak demand reduction (kW) × Demand_charge ($/kW-month) × 12
- Time-differentiated energy rates require hour-by-hour analysis

### Simple Payback Period

Simple payback = Initial_cost / Annual_savings

Typical payback ranges by upgrade type:

| Upgrade Type | Typical Payback | Notes |
|--------------|----------------|-------|
| VFD on constant-volume fans | 2-4 years | Fastest return in VAV conversions |
| Lighting controls integration | 2-5 years | Shared infrastructure costs |
| Economizer retrofit | 3-6 years | Climate-dependent savings |
| Heat recovery systems | 4-8 years | Requires simultaneous heating/cooling |
| Chiller replacement | 8-15 years | Long equipment life extends analysis |
| BAS upgrades | 5-10 years | Benefits extend beyond energy savings |

### Life-Cycle Cost Analysis

Comprehensive analysis includes:
- Initial capital investment
- Annual energy cost savings
- Maintenance cost changes (positive or negative)
- Equipment replacement cycles
- Discount rate for present value calculations

Net present value calculation:
NPV = Σ(Savings_year / (1 + discount_rate)^year) - Initial_cost

Positive NPV indicates economically justified investment.

### Incentive Programs

Utility and government programs reduce effective first cost:
- Prescriptive rebates for qualifying high-efficiency equipment
- Custom incentives for projects demonstrating significant energy savings
- Low-interest financing programs extending available capital
- Accelerated depreciation (Section 179D) for energy-efficient building systems

Typical incentive levels:
- Chiller upgrades: $30-80 per ton
- Lighting controls: $0.10-0.25 per square foot
- VFD installations: $50-150 per horsepower
- Custom projects: $0.05-0.15 per kWh saved annually

### Non-Energy Benefits

Quantifiable benefits beyond energy savings:
- Reduced maintenance costs from more reliable modern equipment
- Extended equipment life from VFD soft-start operation
- Improved comfort reducing occupant complaints
- Enhanced controllability enabling flexible space utilization
- Utility rebates and tax incentives reducing net capital cost

Including non-energy benefits typically reduces payback periods by 15-30%.

## Implementation Strategies

### Phased Upgrade Approach

Prioritize projects by:
1. Shortest payback periods first
2. Equipment approaching end of service life
3. Systems with highest energy consumption
4. Projects with available incentive funding

Sequential implementation:
- Controls and operational improvements first (low capital cost, quick savings)
- VFD and economizer additions second (moderate cost, good returns)
- Major equipment replacement last (high capital, longer payback)

### Maintenance vs. Upgrade Decision

Replace rather than repair when:
- Equipment has exceeded 75% of expected service life
- Repair costs exceed 50% of replacement cost
- Modern equipment efficiency exceeds existing by 25% or greater
- Replacement parts availability becomes limited

### Commissioning Requirements

New equipment requires proper commissioning:
- Functional performance testing verifies design intent achievement
- Controls sequence verification ensures proper integration
- Training for operations staff on new equipment and controls
- Documentation including as-built drawings and O&M manuals

Proper commissioning ensures projected energy savings materialize in actual operation.
