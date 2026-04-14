---
title: "Onion Storage HVAC Systems"
aliases: ["Onion Storage HVAC Systems"]
description: "Comprehensive technical guide to environmental control systems for long-term onion storage including curing processes, dormancy management, humidity control, and air circulation design for bulb onion preservation."
weight: 3
---

## Overview

Onion storage presents unique HVAC challenges due to the requirement for low humidity environments combined with precise temperature control to maintain dormancy while preventing sprouting, rooting, and decay. Unlike most vegetable storage operations that require high humidity, successful onion storage demands relative humidity between 65-75% to prevent moisture-related diseases while avoiding excessive desiccation.

The critical distinction between storage-grade onions and fresh-market onions significantly impacts facility design. Storage onions must undergo proper curing before entering cold storage, requiring separate curing chambers with elevated temperatures and high airflow rates.

## Storage Temperature Requirements

### Optimal Storage Conditions

Dry bulb onions are stored at temperatures approaching 0°C with narrow tolerances to maximize dormancy period and storage life.

| Storage Parameter | Value | Tolerance | Purpose |
|-------------------|-------|-----------|---------|
| Temperature | 0-1°C | ±0.5°C | Dormancy maintenance |
| Relative Humidity | 65-70% | ±5% | Disease prevention |
| Air Velocity | 0.025-0.05 m/s | Variable | Uniform conditions |
| Storage Duration | 1-8 months | Variety dependent | Market distribution |

### Temperature-Storage Life Relationship

Storage life decreases exponentially with increasing temperature above optimal range:

**Storage Duration at Various Temperatures:**

| Temperature | Expected Storage Life | Sprouting Risk | Decay Risk |
|-------------|----------------------|----------------|------------|
| 0-1°C | 6-8 months | Minimal | Low |
| 2-4°C | 4-6 months | Low | Low |
| 5-10°C | 2-3 months | Moderate | Moderate |
| 10-15°C | 1-2 months | High | High |
| >15°C | <1 month | Very High | Very High |

### Heat Load Calculations

Total refrigeration load for onion storage facilities:

**Q_total = Q_transmission + Q_product + Q_respiration + Q_ventilation + Q_infiltration + Q_equipment + Q_personnel**

Where:

- **Q_transmission**: Envelope heat gain through walls, ceiling, floor
- **Q_product**: Heat removal from incoming onions (field heat)
- **Q_respiration**: Heat of respiration from stored onions
- **Q_ventilation**: Outdoor air for periodic ventilation
- **Q_infiltration**: Air leakage through openings
- **Q_equipment**: Heat from fans, lighting, material handling
- **Q_personnel**: Heat gain from workers

**Onion Respiration Heat Production:**

At 0°C: 4-6 W/tonne
At 5°C: 8-12 W/tonne
At 10°C: 15-25 W/tonne

The low respiration rate at proper storage temperature significantly reduces refrigeration requirements compared to living-tissue commodities.

## Curing Process Requirements

### Curing Chamber Design

Curing is essential for preparing onions for long-term storage. Inadequate curing results in neck rot, bacterial soft rot, and reduced storage life.

**Curing Process Parameters:**

| Parameter | Value | Duration | Airflow |
|-----------|-------|----------|---------|
| Temperature | 28-35°C | 2-4 weeks | High |
| Relative Humidity | 60-70% | Initial phase | Continuous |
| Air Changes | 20-40 ACH | Entire period | Forced |
| Air Velocity | 0.5-1.0 m/s | Through product | Critical |

### Curing Objectives

**Primary Goals:**

- **Neck drying**: Complete desiccation of stem tissue prevents fungal entry
- **Scale tightening**: Outer skin layers become protective barrier
- **Wound healing**: Cut surfaces seal through suberization
- **Moisture reduction**: Outer scales lose moisture, toughen
- **Pathogen inhibition**: Dry surface prevents bacterial/fungal colonization

### Curing HVAC System Design

Curing chambers require heating capacity and high-volume air circulation rather than refrigeration:

**Heating capacity** = 50-100 W/m³ of chamber volume

**Air circulation rate** = 0.1-0.2 m³/s per tonne of onions

**Fan motor sizing** for curing:
- Static pressure: 250-500 Pa
- Airflow: Based on 20-40 air changes per hour
- Motor efficiency: Select premium efficiency for extended operation

**Typical curing system configuration:**
- Indirect-fired heaters or electric resistance heating
- Centrifugal or axial fans sized for high volume, moderate pressure
- Damper controls for outdoor air introduction (dehumidification)
- Temperature sensors: Multiple zones, ±0.5°C accuracy
- Control system: PLC-based with ramp-up/ramp-down capability

### Curing Process Stages

**Stage 1: Initial Drying (Days 1-7)**
- Temperature: Gradually increase to 28-30°C
- RH: Allow to float (typically 70-80% initially)
- Airflow: Maximum continuous circulation
- Objective: Surface moisture removal

**Stage 2: Active Curing (Days 8-21)**
- Temperature: Maintain 30-35°C
- RH: Reduce to 60-70% through ventilation
- Airflow: Continuous at full design rate
- Objective: Neck drying, scale tightening

**Stage 3: Conditioning (Days 22-28)**
- Temperature: Gradually reduce to 15-20°C
- RH: Maintain 65-70%
- Airflow: Reduce to 50% of maximum
- Objective: Prepare for transition to cold storage

## Low Humidity Requirements

### Humidity Control Strategy

Unlike high-humidity vegetable storage, onion storage demands low humidity to prevent disease:

**Moisture-Related Disease Pathogens:**

| Disease | Pathogen | Minimum RH for Growth | Control RH |
|---------|----------|----------------------|------------|
| Bacterial soft rot | *Erwinia* spp. | >85% | <75% |
| Botrytis neck rot | *Botrytis allii* | >80% | <75% |
| Black mold | *Aspergillus niger* | >75% | <70% |
| Fusarium basal rot | *Fusarium* spp. | >80% | <75% |

### Humidity Control Methods

**Approach 1: Ventilation with Cold Outdoor Air**

During winter months in temperate climates, cold outdoor air introduced into the storage space provides dehumidification:

**Ventilation rate** = (W_evaporation) / (ρ × (ω_storage - ω_outdoor))

Where:
- W_evaporation = Moisture loss from stored onions (kg/s)
- ρ = Air density (kg/m³)
- ω_storage = Humidity ratio at storage conditions (kg moisture/kg dry air)
- ω_outdoor = Humidity ratio of outdoor air (kg moisture/kg dry air)

**Typical moisture loss from stored onions**: 0.2-0.4% of total mass per month

**Approach 2: Refrigeration-Based Dehumidification**

In humid climates or during warm seasons, refrigeration system operates with low evaporator temperature to condense moisture:

- **Evaporator TD**: 8-12°C (larger than typical vegetable storage)
- **Coil face velocity**: 1.5-2.5 m/s (lower to enhance dehumidification)
- **Coil configuration**: Deep coils (6-8 rows) for moisture removal
- **Defrost cycles**: Less frequent due to low moisture load

**Approach 3: Desiccant Dehumidification**

For critical applications or warm-climate operations:

- Lithium chloride or silica gel desiccant systems
- Regeneration temperature: 100-150°C
- Provides independent humidity control from cooling
- Higher operating cost, used for specialty applications

## Dormancy Management

### Physiological Dormancy

Onion bulbs naturally enter dormancy after harvest. Maintaining dormancy is critical for preventing sprouting and rooting.

**Dormancy Period Factors:**

| Factor | Effect on Dormancy | Management Strategy |
|--------|-------------------|---------------------|
| Variety | 2-8 month range | Select long-dormancy varieties |
| Maturity at harvest | Immature = shorter | Harvest at full maturity |
| Storage temperature | Lower = longer | Maintain 0-1°C |
| Humidity | High = stimulates growth | Keep 65-70% RH |
| Ethylene exposure | Minimal effect | No special control needed |

### Temperature-Dormancy Relationship

Dormancy period (days) = 60 + (180 × e^(-0.15T))

Where T = storage temperature (°C)

This empirical relationship demonstrates exponential reduction in dormancy with increasing temperature.

**Calculated Dormancy Periods:**

- At 0°C: 240 days (8 months)
- At 5°C: 150 days (5 months)
- At 10°C: 90 days (3 months)
- At 15°C: 60 days (2 months)

### Breaking Dormancy Indicators

Monitor stored onions for dormancy breakdown:

**Physical indicators:**
- Basal plate swelling
- Root initiation (white points at base)
- Translucent appearance at neck
- Internal sprouting (detected through neck feel)
- Softening of outer scales

**Management response:**
- Increase air circulation
- Verify temperature uniformity
- Consider market release timing
- Evaluate sprouting inhibitor application (if permitted)

## Sprouting Prevention

### Environmental Control

Sprouting occurs when dormancy ends and environmental conditions permit growth.

**Sprouting Prevention Hierarchy:**

1. **Temperature control** (primary method)
   - Maintain 0-1°C throughout storage
   - Eliminate warm spots (>3°C)
   - Rapid pulldown after loading

2. **Humidity management** (secondary method)
   - Keep RH below 70%
   - Prevent condensation events
   - Maintain dry basal plates

3. **Air circulation** (supporting method)
   - Eliminate stagnant zones
   - Uniform temperature distribution
   - Prevent moisture accumulation

### Chemical Sprouting Inhibitors

Where permitted by regulations, maleic hydrazide (MH) applied pre-harvest provides sprouting suppression:

- Applied 2-4 weeks before harvest
- Extends storage life 2-4 months
- Does not replace proper environmental control
- Regulatory approval varies by region

**HVAC implications:**
- Slightly reduces respiration rate
- May permit marginally higher storage temperature (1-2°C)
- Does not eliminate need for humidity control

### Sprouting Risk Assessment

Calculate sprouting risk index:

**SRI = (T × H × D) / 1000**

Where:
- T = Average storage temperature (°C)
- H = Average relative humidity (%)
- D = Days in storage

**Risk levels:**
- SRI < 50: Low risk
- SRI 50-100: Moderate risk
- SRI 100-150: High risk
- SRI > 150: Severe risk, immediate action required

## Rooting Prevention

### Root Growth Conditions

Rooting differs from sprouting but occurs under similar conditions:

**Factors promoting root growth:**
- High humidity (>75% RH) at basal plate
- Moisture condensation on bulb base
- Temperature fluctuations creating condensation
- Contact with wet surfaces (floor moisture, wet bins)

### Design Strategies

**Floor drainage and moisture control:**
- Sloped floor: 1-2% grade to drains
- Perimeter drainage system
- Vapor barrier under slab
- Heated floor slab (optional, premium installations)

**Air distribution for basal plate drying:**
- Underfloor air distribution systems
- Perforated flooring for upward airflow
- Bottom air introduction in bin storage
- Airflow rate: 0.01-0.02 m³/s per tonne at floor level

**Condensation prevention:**
- Eliminate thermal bridges in floor construction
- Insulated foundation walls
- Continuous vapor barrier envelope
- Dewpoint monitoring at floor level

## Air Circulation Patterns

### Bulk Storage Air Distribution

**Approach 1: Horizontal Airflow**

Air introduced at one end, flows through bulk storage, exhausts at opposite end:

- **Design airflow**: 0.025-0.05 m³/s per tonne
- **Static pressure**: 50-150 Pa depending on pile depth
- **Distribution uniformity**: ±10% velocity variation
- **Typical application**: Long, narrow storage rooms

**Pressure drop through onion bulk:**

ΔP = K × L × v²

Where:
- K = Resistance coefficient (2.5-4.0 Pa·s²/m² for onions)
- L = Airflow path length (m)
- v = Superficial air velocity (m/s)

**Approach 2: Vertical Airflow (Underfloor Distribution)**

Air supplied through perforated floor, rises through product, collected at ceiling:

- **Floor perforation**: 10-20% open area
- **Plenum pressure**: 100-250 Pa
- **Airflow uniformity**: Superior to horizontal systems
- **Advantages**: Better basal plate drying, uniform conditions
- **Disadvantages**: Higher construction cost

**Approach 3: Combination Systems**

Horizontal primary circulation with localized vertical airflow in problem areas:

- Main circulation: Horizontal at 0.03 m³/s per tonne
- Floor supply: Selective zones with moisture risk
- Control: Variable speed drives on both systems
- Optimization: Adjust based on monitoring data

### Bin Storage Air Distribution

Wooden or plastic bins stacked in storage room require different approach:

**Aisle spacing for airflow:**
- Cross-aisle width: 0.6-1.0 m minimum
- Main aisle width: 2.0-3.0 m for equipment
- Vertical spacing: 0.05-0.10 m between bins
- Air pathway maintenance: Critical for circulation

**Supply air delivery:**
- Overhead duct distribution: Supply at ceiling level
- Side wall jets: High-velocity jets along walls
- Underfloor supply: Requires bin elevation on racks
- Design velocity at bin face: 0.5-1.0 m/s

**Air circulation rate for bin storage:**
- Minimum: 0.02 m³/s per tonne
- Design: 0.03-0.05 m³/s per tonne
- Maximum: 0.08 m³/s per tonne (during pulldown)

### Fan System Design

**Centrifugal fans:**
- Backward-inclined or airfoil blade designs
- Efficiency: 75-85%
- Pressure capability: Up to 2000 Pa
- Application: Underfloor systems, long horizontal runs

**Axial fans:**
- Vaneaxial or tubeaxial configurations
- Efficiency: 65-75%
- Pressure capability: Up to 500 Pa
- Application: Low-resistance horizontal systems

**Variable speed control:**
- Variable frequency drives (VFD) standard
- Speed range: 30-100% of design
- Energy savings: Proportional to cube of speed reduction
- Control input: Temperature differential, time schedule

**Fan energy calculation:**

P_fan = (Q × ΔP) / (η_fan × η_motor × η_VFD)

Where:
- P_fan = Fan power input (W)
- Q = Airflow rate (m³/s)
- ΔP = Total pressure rise (Pa)
- η_fan = Fan efficiency (decimal)
- η_motor = Motor efficiency (decimal)
- η_VFD = VFD efficiency (decimal, typically 0.96-0.98)

## Long-Term Storage Design

### Facility Configuration

**Storage room geometry:**

| Configuration | Width | Length | Height | Capacity |
|--------------|-------|--------|--------|----------|
| Small room | 10-15 m | 20-40 m | 4-6 m | 200-600 tonnes |
| Medium room | 15-25 m | 40-80 m | 5-7 m | 600-2000 tonnes |
| Large room | 20-40 m | 60-120 m | 6-9 m | 2000-8000 tonnes |

**Aspect ratio considerations:**
- Length/width ratio: 2:1 to 4:1 for horizontal airflow
- Height limited by: Structural loading, airflow resistance, handling equipment
- Bulk depth: 3-6 m typical, up to 9 m with engineered airflow

### Insulation Requirements

Onion storage operates at relatively high temperature (0°C) compared to frozen storage, but still requires substantial insulation:

**Recommended R-values (RSI):**

| Surface | Climate Zone 1-3 | Climate Zone 4-6 | Climate Zone 7-8 |
|---------|-----------------|-----------------|------------------|
| Walls | R-5.3 (RSI-30) | R-4.4 (RSI-25) | R-3.5 (RSI-20) |
| Roof | R-7.0 (RSI-40) | R-6.2 (RSI-35) | R-5.3 (RSI-30) |
| Floor | R-1.8 (RSI-10) | R-1.4 (RSI-8) | R-0.9 (RSI-5) |

**Insulation materials:**
- Polyurethane spray foam: Highest R-value per inch, vapor barrier properties
- Extruded polystyrene (XPS): Good moisture resistance, moderate R-value
- Expanded polystyrene (EPS): Economical, requires separate vapor barrier
- Polyisocyanurate panels: High R-value, foil facing provides vapor barrier

**Vapor barrier requirements:**
- Permeance: <0.06 perms (low-perm classification)
- Location: Warm side of insulation assembly
- Continuity: Critical at penetrations, joints, transitions
- Testing: Pressure test to 75 Pa minimum

### Loading and Unloading Considerations

**Harvest season influx:**
- Peak loading rate: 50-200 tonnes per day
- Duration: 2-6 weeks depending on growing region
- Field heat removal: Onions arrive at 15-30°C
- Pulldown time: 7-14 days to reach 0-1°C storage temperature

**Refrigeration system staging:**
- Multiple compressors: 3-6 units for capacity control
- Unloading capability: 50-100% shutdown for maintenance
- Peak capacity: 150-200% of steady-state load
- Part-load efficiency: Critical for annual energy cost

**Heat removal during pulldown:**

Q_pulldown = m × c_p × ΔT / t

Where:
- m = Mass of onions loaded (kg)
- c_p = Specific heat of onions (3.6 kJ/kg·K)
- ΔT = Temperature reduction (K)
- t = Pulldown time (seconds)

**Example:** 500 tonnes loaded at 25°C, pulldown to 1°C over 10 days:

Q_pulldown = 500,000 kg × 3.6 kJ/kg·K × 24 K / (10 days × 86,400 s/day)
Q_pulldown = 50 kW average heat removal rate

Add 50-100% to account for respiration, envelope loads, and equipment heat.

### Multi-Room Facilities

Large operations employ multiple storage rooms for operational flexibility:

**Advantages of multi-room design:**
- Segregation by variety, quality, or customer
- Independent temperature control
- Phased loading and unloading
- Maintenance capability without full shutdown
- Energy optimization through selective operation

**Shared infrastructure:**
- Central refrigeration plant serving multiple rooms
- Common loading/unloading areas with air curtains
- Centralized monitoring and control system
- Shared curing chambers (time-sequenced use)

**Refrigeration distribution:**
- Secondary refrigerant loops (glycol) for multiple rooms
- Direct expansion with solenoid control per room
- Dedicated evaporators per room, shared condensing units
- Load balancing controls for energy optimization

## Equipment Specifications

### Refrigeration Equipment

**Compressor Selection:**

| Type | Capacity Range | Efficiency | Application |
|------|---------------|-----------|-------------|
| Reciprocating | 10-150 kW | Moderate | Small facilities |
| Scroll | 5-50 kW | Good | Small to medium |
| Screw | 50-500 kW | Very good | Medium to large |
| Centrifugal | 200-2000 kW | Excellent | Large facilities |

**Refrigerant considerations:**
- R-717 (Ammonia): High efficiency, industrial standard, requires safety measures
- R-404A: Being phased out due to high GWP
- R-448A, R-449A: Lower-GWP replacements for R-404A
- R-744 (CO2): Emerging technology, low GWP, requires high pressure systems

**Evaporator specifications:**

| Parameter | Low-TD Design | Standard Design | High-TD Design |
|-----------|--------------|-----------------|----------------|
| TD (Evap - Room) | 4-6°C | 6-8°C | 8-12°C |
| Fin spacing | 4-6 mm | 6-8 mm | 8-10 mm |
| Face velocity | 1.5-2.0 m/s | 2.0-2.5 m/s | 2.5-3.0 m/s |
| Dehumidification | Excellent | Good | Moderate |
| Energy efficiency | Lower | Moderate | Higher |

**Condenser sizing:**
- Air-cooled: 15-20°C approach to ambient design temperature
- Evaporative: 8-12°C approach to ambient wet bulb temperature
- Water-cooled: 5-8°C approach to entering water temperature

### Air Circulation Equipment

**Evaporator fan motors:**
- Premium efficiency: IE3 or IE4 classification
- Single-speed or multi-speed pole configuration
- Continuous-duty rating for 24/7 operation
- Temperature rating: -15°C to +40°C ambient

**Circulation fans (non-refrigerated):**
- Energy-efficient centrifugal or axial designs
- VFD-controlled for capacity modulation
- Power: 0.5-5.0 kW per fan, multiple units per room
- Material: Epoxy-coated or stainless steel in humid environment

**Fan energy monitoring:**

Annual fan energy (kWh) = P_fan × t_annual × f_avg

Where:
- P_fan = Fan rated power (kW)
- t_annual = 8760 hours per year
- f_avg = Average operating fraction (0.6-0.9 typical)

### Control and Monitoring Equipment

**Temperature sensors:**
- Resistance temperature detectors (RTD): Pt100 or Pt1000
- Accuracy: ±0.1°C at 0°C
- Quantity: Minimum 4-6 per room (distributed 3D grid)
- Wireless options: Battery-powered for bulk storage monitoring

**Humidity sensors:**
- Capacitive or resistive sensing elements
- Accuracy: ±2-3% RH at 65-75% range
- Calibration: Annual verification required
- Quantity: 2-4 per room minimum

**Control system architecture:**
- Programmable logic controller (PLC) or building automation system (BAS)
- Touchscreen HMI for local control
- Remote monitoring via internet connectivity
- Data logging: Minimum 1-year historical storage
- Alarming: Temperature, humidity, equipment failure alerts

**Monitoring points per room:**
- Temperature: 4-10 locations depending on room size
- Relative humidity: 2-4 locations
- Equipment status: All fans, compressors, valves
- Electrical power: Energy monitoring for major loads
- Door status: Open/closed sensors on access doors

### Material Handling Equipment

**Storage loading:**
- Pallet jacks: Manual or electric, 2000-3000 kg capacity
- Forklifts: Electric preferred (no combustion emissions), 2000-5000 kg capacity
- Conveyor systems: Belt or roller for high-volume facilities
- Bulk loading equipment: Front-end loaders for direct bulk storage

**Bin handling:**
- Bin dumpers: Hydraulic tilt for mechanized unloading
- Bin stackers: Automated stacking up to 6-8 bins high
- Bin storage racks: Steel construction, powder-coated finish

**Forklift HVAC considerations:**
- Combustion emissions: Prohibited in sealed storage rooms
- Heat dissipation: Electric forklift generates 5-10 kW heat load
- Traffic frequency: Include in infiltration load calculations
- Door opening duration: Minimize through material handling efficiency

## Quality Parameters

### Storage Quality Assessment

Regular quality monitoring ensures marketability throughout storage period:

**Physical quality parameters:**

| Parameter | Acceptable Range | Measurement Frequency | Action Threshold |
|-----------|-----------------|---------------------|------------------|
| Firmness | Firm, no soft spots | Weekly | >5% soft bulbs |
| Sprouting | No visible sprouts | Weekly | >1% sprouted |
| Rooting | No root growth | Weekly | >2% rooted |
| Decay | <2% affected | Weekly | >5% decay |
| Weight loss | <5% total | Monthly | >8% loss |
| Scale tightness | Dry, papery | Monthly | Loose, deteriorating |

### Quality Deterioration Factors

**Temperature abuse:**
- Each 5°C above optimal reduces storage life by 50%
- Temperature cycling accelerates decay and sprouting
- Warm spots (>3°C) become decay initiation points

**Humidity-related defects:**
- High RH (>75%): Bacterial soft rot, mold growth, rooting
- Low RH (<60%): Excessive weight loss, scale separation, desiccation
- Condensation events: Immediate decay risk at moisture contact points

**Air circulation deficiency:**
- Stagnant zones: Local temperature rise, humidity accumulation
- Inadequate turnover: Incomplete moisture removal, disease progression
- Excessive velocity: Mechanical damage, accelerated desiccation

### Weight Loss Management

Weight loss occurs through moisture evaporation from outer scales:

**Typical weight loss rates:**
- 0.2-0.3% per month at optimal conditions (0°C, 65-70% RH)
- 0.4-0.6% per month at marginal conditions (2-4°C, 70-75% RH)
- 0.8-1.2% per month at poor conditions (5-10°C, variable RH)

**Economic impact:**
- 5% weight loss typically acceptable for processing market
- 8% weight loss approaches economic threshold
- >10% weight loss may result in rejection or price reduction

**Weight loss equation:**

WL = k × (P_v,surface - P_v,air) × A × t

Where:
- WL = Weight loss (kg)
- k = Mass transfer coefficient (kg/Pa·m²·s)
- P_v,surface = Vapor pressure at onion surface (Pa)
- P_v,air = Vapor pressure of storage air (Pa)
- A = Surface area (m²)
- t = Time (s)

**Minimizing weight loss:**
- Maintain RH at upper end of acceptable range (70%)
- Reduce air velocity to minimum required for temperature uniformity
- Minimize temperature fluctuations that drive vapor pressure gradients
- Proper curing to seal outer scales

### Disease Development Monitoring

**Common storage diseases:**

**1. Bacterial soft rot (*Erwinia carotovora*):**
- Symptoms: Soft, watery breakdown starting at neck
- Conditions favoring: RH >80%, temperature >5°C, mechanical injury
- Control: Low humidity, temperature, careful handling

**2. Botrytis neck rot (*Botrytis allii*):**
- Symptoms: Gray mold growth at neck, internal decay
- Conditions favoring: Incomplete neck drying, RH >75%
- Control: Thorough curing, low humidity storage

**3. Black mold (*Aspergillus niger*):**
- Symptoms: Black powdery spores between outer scales
- Conditions favoring: Scale damage, high humidity, temperature >10°C
- Control: Gentle handling, low temperature and humidity

**4. Fusarium basal rot (*Fusarium* spp.):**
- Symptoms: Brown decay starting at base plate
- Conditions favoring: High temperature, humidity >75%, harvest injury
- Control: Optimal storage conditions, avoid basal plate damage

**Disease progression inspection:**
- Visual inspection: Weekly walk-through of storage areas
- Sampling: Random sampling of 100-200 bulbs per room
- Documentation: Record disease incidence, type, location
- Action triggers: Increase air circulation, verify temperature/humidity, consider market release timing

## Operational Strategies

### Seasonal Operation Optimization

**Fall loading period (September-November, Northern Hemisphere):**
- Maximum refrigeration capacity operation
- Continuous air circulation
- Frequent monitoring (daily temperature checks)
- Gradual temperature pulldown over 7-14 days

**Winter storage period (December-March):**
- Reduced refrigeration load (cold outdoor air available)
- Periodic ventilation with outdoor air for dehumidification
- Energy optimization through free cooling
- Maintenance scheduling during stable period

**Spring market release (April-June):**
- Maintain storage conditions until shipment
- Increase monitoring frequency (sprout/root pressure increases)
- Flexible room operation as inventory depletes
- Clean-out and sanitation for next season

### Energy Optimization

**Free cooling with outdoor air:**

During cold weather, outdoor air provides cooling and dehumidification without compressor operation:

- Outdoor air temperature <0°C: Direct cooling opportunity
- Outdoor dewpoint <-5°C: Excellent dehumidification potential
- Control strategy: Economizer mode with temperature/humidity limits
- Energy savings: 30-60% reduction during winter months

**Part-load optimization:**

As storage season progresses and inventory depletes:

- Reduce air circulation in empty areas
- Stage compressor operation for part-load efficiency
- Consolidate inventory into fewer rooms
- Shut down unused rooms completely

**Variable speed drive benefits:**

Fan energy reduction through VFD control:

P_actual = P_rated × (N_actual / N_rated)³

Where:
- P_actual = Actual power consumption
- P_rated = Rated power at full speed
- N_actual = Actual fan speed (rpm)
- N_rated = Rated fan speed (rpm)

**Example:** Operating fans at 70% speed reduces power consumption to 34% of full-speed power.

### Maintenance Scheduling

**Pre-season preparation (before harvest):**
- Refrigeration system service: Leak check, refrigerant charge verification
- Evaporator coil cleaning: Remove dust, debris from previous season
- Fan inspection: Bearing lubrication, belt tension, motor megger test
- Control system verification: Calibrate sensors, test alarms, verify sequences
- Facility cleaning: Remove debris, sanitize surfaces, repair structural defects

**In-season maintenance (during storage):**
- Weekly: Visual inspection, data log review, alarm response
- Monthly: Filter replacement, lubrication, defrost cycle verification
- Quarterly: Vibration analysis on critical rotating equipment
- As-needed: Response to equipment failures, abnormal conditions

**Post-season maintenance (after clean-out):**
- Deep cleaning: High-pressure wash, sanitizer application
- Equipment overhaul: Major repairs scheduled during off-season
- Facility repairs: Structural, insulation, door seal replacement
- System upgrades: Control improvements, efficiency retrofits

## Conclusion

Successful onion storage HVAC design requires integration of precise temperature control, low-humidity management, effective air distribution, and thorough curing processes. The fundamental difference from high-humidity vegetable storage—maintaining 65-70% RH rather than 90-95%—drives system design toward dehumidification capability and careful moisture management.

Key design principles:
- Temperature stability at 0-1°C throughout storage season
- Humidity control at 65-70% RH through ventilation or mechanical dehumidification
- Adequate air circulation (0.025-0.05 m³/s per tonne) for uniform conditions
- Proper curing (28-35°C, 2-4 weeks) before cold storage entry
- Prevention of condensation on bulb surfaces, especially basal plates
- Multi-zone monitoring and control for early problem detection

Economic viability depends on minimizing weight loss, preventing sprouting and decay, and maintaining market quality throughout the extended storage period. HVAC system design directly impacts these outcomes through environmental parameter control.
