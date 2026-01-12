---
title: "Refrigerated Seawater (RSW) Systems"
description: "Comprehensive technical analysis of refrigerated seawater systems for marine fishery applications including system design, heat transfer calculations, refrigeration system sizing, and vessel integration for HVAC professionals."
weight: 3
---

## System Overview

Refrigerated seawater (RSW) systems provide the most effective method for rapidly chilling freshly caught fish aboard commercial fishing vessels. The system circulates chilled seawater at temperatures between 0°C and 2°C through insulated holds, maintaining fish quality by preventing bacterial growth and enzymatic deterioration. RSW systems offer superior temperature uniformity compared to ice storage and eliminate mechanical damage from handling.

The fundamental principle involves extracting heat from seawater using mechanical refrigeration, then circulating the chilled brine through fish storage holds. The seawater acts as both the cooling medium and the storage environment, providing complete thermal contact with all fish surfaces.

## Thermodynamic Principles

### Heat Load Components

The total refrigeration load for an RSW system consists of multiple heat sources that must be continuously removed:

**Product cooling load:** The sensible heat removed from fish tissue as temperature drops from catch temperature to storage temperature. Fish specific heat averages 3.6 kJ/kg·K above freezing point.

**Respiration heat:** Living fish continue metabolic processes post-catch, generating heat at rates of 0.15 to 0.25 W/kg depending on species and time after catch.

**Transmission load:** Heat infiltration through insulated hold walls, deck, and bottom from ambient seawater and air. This represents the largest continuous load component.

**Seawater pulldown load:** Initial cooling of the seawater mass from ambient (typically 10°C to 20°C) to operating temperature (0°C to 2°C). Seawater specific heat is approximately 3.93 kJ/kg·K.

**Solar radiation:** Direct solar heating of deck surfaces above fish holds adds significant load in tropical fishing operations.

**Equipment heat gains:** Pumps, agitators, and other mechanical equipment operating within or near the refrigerated space contribute sensible heat.

### Heat Transfer Calculations

The rate of fish cooling in RSW systems follows Newton's law of cooling with forced convection enhancement:

**Q = h × A × (T_fish - T_water)**

Where:
- Q = heat transfer rate (W)
- h = convective heat transfer coefficient (W/m²·K)
- A = fish surface area (m²)
- T_fish = fish tissue temperature (°C)
- T_water = seawater temperature (°C)

The convective heat transfer coefficient for fish in agitated seawater ranges from 200 to 400 W/m²·K, depending on circulation velocity and fish packing density. Higher circulation rates increase h but also increase pump power consumption.

The time required to cool fish from initial temperature T_i to final temperature T_f:

**t = (m × c_p / (h × A)) × ln((T_i - T_water)/(T_f - T_water))**

Where:
- t = cooling time (seconds)
- m = fish mass (kg)
- c_p = specific heat of fish (J/kg·K)

Typical cooling times to achieve core temperatures within 2°C of seawater temperature range from 4 to 8 hours depending on fish size and species.

## Refrigeration System Design

### System Configuration

RSW refrigeration systems employ direct expansion or liquid overfeed configurations. Direct expansion systems use thermostatic expansion valves feeding refrigerant directly into cooling coils immersed in seawater. Liquid overfeed systems maintain flooded evaporator conditions with improved heat transfer but require larger refrigerant charges.

**Compressor selection:** Reciprocating or screw compressors rated for marine service with corrosion-resistant materials. Typical capacity range 50 to 500 kW refrigeration effect. Twin compressor installations provide redundancy for extended fishing operations.

**Evaporator coils:** Stainless steel or titanium tube bundles designed for seawater immersion. Coil surface area calculated based on overall heat transfer coefficient U = 800 to 1200 W/m²·K for clean coils. Fouling factor of 0.0002 m²·K/W minimum must be applied.

**Condensers:** Seawater-cooled shell and tube heat exchangers with cupro-nickel tubes. Condensing temperature typically 35°C to 45°C depending on ambient seawater temperature. Design for approach temperature of 5°C to 8°C.

**Refrigerants:** R-404A and R-507A historically common, transitioning to R-448A, R-449A, or R-513A for lower GWP. Ammonia (R-717) used in larger vessels with segregated machinery spaces.

### Capacity Sizing Methodology

Total refrigeration capacity required:

**Q_total = Q_product + Q_respiration + Q_transmission + Q_pulldown + Q_solar + Q_equipment**

**Product load:**
Q_product = (m_fish × c_p × ΔT) / t_cool

Where:
- m_fish = total fish catch mass (kg)
- ΔT = temperature reduction required (K)
- t_cool = allowable cooling time (seconds)

**Transmission load:**
Q_transmission = (U_wall × A_wall + U_bottom × A_bottom + U_deck × A_deck) × ΔT_ambient

Typical U-values:
- Insulated hold walls: 0.20 to 0.35 W/m²·K
- Hold bottom (seawater contact): 0.25 to 0.40 W/m²·K
- Deck surface: 0.30 to 0.45 W/m²·K

**Seawater pulldown:**
Q_pulldown = (m_seawater × c_p_seawater × ΔT_seawater) / t_pulldown

Standard practice sizes systems for 2 to 4 hour seawater pulldown from 15°C to 2°C.

**Design safety factors:** Apply 15% to 25% safety margin to calculated loads accounting for:
- Compressor capacity degradation between maintenance intervals
- Higher than design ambient temperatures
- Faster catch processing rates
- Partial load inefficiency

## RSW System Components

### Seawater Storage Tanks

Insulated holds constructed with:

**Structural materials:** Aluminum alloy, fiberglass reinforced plastic, or steel with corrosion-resistant coatings. Tank design pressure minimum 0.3 bar gauge to withstand sloshing loads in rough seas.

**Insulation systems:** Polyurethane foam 100 to 150 mm thickness for hold walls and bottom. Deck insulation 150 to 200 mm thickness due to solar load. Vapor barrier required on warm side to prevent moisture infiltration.

**Tank geometry:** Length-to-width ratio typically 2:1 to 3:1 matching vessel hull form. Depth limited to 3 to 4 meters to prevent pressure damage to fish at bottom layers.

**Volume calculations:** Seawater-to-fish ratio maintained at 1:1 to 1.5:1 by volume. This provides adequate circulation space while maximizing hold capacity utilization.

### Circulation System

**Pumps:** Centrifugal pumps with bronze or stainless steel construction. Flow rate 5 to 10 complete tank volume changes per hour. Head requirement typically 3 to 5 meters including distribution piping and nozzle losses.

**Distribution manifolds:** Perforated pipes or nozzle arrays positioned to create uniform flow patterns. Inlet velocities 1 to 2 m/s prevent stagnant zones while avoiding fish damage.

**Flow pattern:** Bottom inlet with top suction creates upward circulation preventing stratification. Alternative: side inlet with diagonal flow pattern.

### Temperature Control Systems

**Temperature sensors:** RTD (Pt100) sensors positioned at multiple tank locations. Averaging control algorithm prevents compressor cycling from local temperature variations.

**Control strategy:** PID control maintains seawater temperature setpoint ±0.5°C. Compressor capacity modulation via slide valves or variable speed drives provides precise control.

**Safety interlocks:**
- High pressure cutout: 1.8 to 2.0 MPa for R-404A systems
- Low pressure cutout: prevents evaporator freeze-up
- High seawater temperature alarm: >4°C indicates system fault
- Low seawater level cutout: prevents pump cavitation

## Seawater Treatment Requirements

### Filtration Systems

**Pre-filtration:** Strainers with 3 to 5 mm mesh remove large debris, fish scales, and biological material before seawater enters refrigeration circuit.

**Fine filtration:** 100 to 200 micron filters protect evaporator coils from fouling. Duplex filter arrangement allows cleaning without system shutdown.

**Automatic backwash:** Timer or differential pressure controlled backwash cycles maintain filter efficiency. Backwash water discharged overboard through check valves.

### Chemical Treatment

**Chlorination:** Sodium hypochlorite injection 1 to 2 ppm maintains bacteriological control without affecting fish quality. Higher concentrations cause tissue bleaching.

**pH control:** Seawater pH 7.8 to 8.2 optimal. CO2 absorption from fish respiration gradually lowers pH requiring periodic monitoring.

**Ozone treatment:** Advanced systems inject ozone 0.1 to 0.3 ppm for superior disinfection. Ozone decomposes rapidly leaving no residual.

### Fouling Prevention

**Evaporator coil fouling:** Biological growth and scale formation reduce heat transfer coefficient by 20% to 40% over 7 to 14 day fishing trips.

**Cleaning protocols:** Between-trip cleaning with acid wash (phosphoric or citric acid 2% solution) followed by alkaline detergent removes scale and organic deposits.

**Antifouling additives:** Polyphosphates 5 to 10 ppm inhibit calcium carbonate scale formation in warm seawater regions.

## Vessel Installation Considerations

### Structural Integration

**Hold location:** Positioned low in vessel hull for stability. Center of gravity considerations critical for vessel trim and stability.

**Access provisions:** Removable hatch covers 1.2 to 1.5 meters diameter for fish loading and hold cleaning. Gas-tight seals prevent refrigeration loss.

**Drainage systems:** Gravity drain with seacock allows rapid dewatering for hold cleaning. Self-priming pumps provide drainage while underway.

### Refrigeration Machinery Space

**Compressor room ventilation:** Minimum 30 air changes per hour removes compressor heat and maintains safe operating temperatures <35°C.

**Refrigerant detection:** Mandatory leak detection systems with audio-visual alarms meeting SOLAS requirements.

**Vibration isolation:** Compressors mounted on spring isolators prevent structure-borne noise transmission to crew quarters.

**Service access:** Minimum 1 meter clearance around compressors and heat exchangers for maintenance operations.

## Performance Optimization

### Energy Efficiency Measures

**Variable speed compressors:** Reduce energy consumption 20% to 30% compared to on-off cycling during partial load conditions.

**Heat recovery:** Compressor discharge heat recovers to provide domestic hot water or cabin heating reducing auxiliary boiler fuel consumption.

**Subcooling circuits:** Mechanical subcooling of liquid refrigerant increases system capacity 5% to 10% and improves efficiency.

**Optimized setpoints:** Operating at 1°C to 2°C rather than 0°C reduces compressor power 8% to 12% while maintaining adequate fish preservation.

### Operational Strategies

**Pre-cooling protocol:** Cool seawater to operating temperature before fish loading reduces total pulldown time and energy consumption.

**Staged loading:** Adding fish in batches prevents excessive temperature rise that overloads refrigeration capacity.

**Circulation management:** Reduce pump speed after initial pulldown period to 60% of design flow maintains temperature uniformity while reducing power consumption.

## RSW System Specifications

| Parameter | Small Vessel | Medium Vessel | Large Vessel |
|-----------|--------------|---------------|--------------|
| Hold Capacity | 20-50 m³ | 50-150 m³ | 150-500 m³ |
| Refrigeration Capacity | 50-100 kW | 100-300 kW | 300-800 kW |
| Fish Storage Capacity | 15-30 tonnes | 30-100 tonnes | 100-300 tonnes |
| Seawater Volume | 20-50 m³ | 50-150 m³ | 150-500 m³ |
| Circulation Rate | 100-500 m³/h | 500-1500 m³/h | 1500-5000 m³/h |
| Pump Power | 5-15 kW | 15-45 kW | 45-120 kW |
| Insulation Thickness | 100 mm | 125 mm | 150 mm |
| Pulldown Time | 2-3 hours | 3-4 hours | 4-6 hours |

## Design Temperature Parameters

| Component | Temperature | Notes |
|-----------|-------------|-------|
| Seawater Operating Temperature | 0°C to 2°C | Target: 1°C optimal |
| Fish Initial Temperature | 10°C to 25°C | Species and location dependent |
| Ambient Seawater | 5°C to 30°C | Varies by fishing grounds |
| Evaporator Temperature | -5°C to -8°C | Direct expansion systems |
| Condensing Temperature | 35°C to 45°C | Function of ambient seawater |
| Approach Temperature | 5°C to 8°C | Evaporator and condenser |

## Heat Transfer Coefficients

| Interface | U-Value (W/m²·K) | Application |
|-----------|------------------|-------------|
| Clean Evaporator Coil | 1000-1200 | New installation |
| Fouled Evaporator Coil | 600-800 | After 7-14 days operation |
| Hold Wall Insulation | 0.20-0.35 | 100-150 mm polyurethane |
| Hold Bottom | 0.25-0.40 | Seawater contact surface |
| Deck Surface | 0.30-0.45 | Solar radiation exposure |
| Fish Convection | 200-400 | Depends on circulation velocity |

## Refrigerant Performance Comparison

| Refrigerant | Evap Pressure (bar) | Cond Pressure (bar) | COP | GWP | Status |
|-------------|---------------------|---------------------|-----|-----|--------|
| R-404A | 2.9 | 16.8 | 2.4 | 3922 | Phase-out |
| R-507A | 2.9 | 17.0 | 2.4 | 3985 | Phase-out |
| R-448A | 3.1 | 17.2 | 2.5 | 1387 | Acceptable replacement |
| R-449A | 3.0 | 17.0 | 2.5 | 1397 | Acceptable replacement |
| R-513A | 3.2 | 17.5 | 2.6 | 631 | Low-GWP option |
| R-717 (Ammonia) | 2.9 | 15.5 | 3.2 | 0 | Large vessels only |

Note: Pressures at -6°C evaporating, 40°C condensing temperatures.

## Maintenance Requirements

**Daily operations:**
- Monitor seawater temperature multiple times per watch
- Check compressor operating pressures and temperatures
- Inspect pump operation and circulation flow
- Record system performance parameters

**Weekly maintenance:**
- Clean pre-filters and strainers
- Inspect evaporator coils for fouling
- Check refrigerant charge and oil levels
- Test safety controls and alarms

**Trip-end procedures:**
- Pump out seawater completely
- Fresh water rinse all surfaces
- Acid wash evaporator coils if fouled
- Alkaline wash and sanitize hold interior
- Inspect insulation for damage
- Test system operation before next departure

## Safety Considerations

**Confined space hazards:** RSW holds classified as permit-required confined spaces. CO2 accumulation from fish respiration creates asphyxiation risk. Forced ventilation and atmospheric testing mandatory before entry.

**Refrigerant exposure:** Marine-grade refrigerant detectors with 25% LEL alarm setpoints required in machinery spaces. Emergency ventilation activated automatically on alarm.

**Pressure vessel compliance:** Systems operating above atmospheric pressure must meet classification society rules (ABS, DNV-GL, Lloyd's Register) for pressure vessel construction and testing.

**Electrical safety:** All equipment rated IP67 minimum for saltwater spray exposure. Ground fault protection on all circuits.

## Troubleshooting Common Issues

**Inadequate cooling capacity:**
- Verify actual fish load versus design capacity
- Check evaporator coil fouling reducing heat transfer
- Confirm compressor delivering rated capacity
- Measure seawater circulation flow rate

**Temperature stratification:**
- Increase circulation pump speed
- Modify distribution manifold for better flow pattern
- Reduce fish packing density in hold

**Excessive energy consumption:**
- Clean fouled evaporator and condenser coils
- Check for refrigerant leaks reducing charge
- Verify condenser seawater flow adequate
- Inspect insulation integrity for thermal bridges

**Compressor short cycling:**
- Adjust thermostat differential wider
- Increase receiver tank volume
- Check for refrigerant overcharge
- Verify expansion valve superheat setting
