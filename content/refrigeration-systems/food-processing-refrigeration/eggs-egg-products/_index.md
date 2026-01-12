---
title: "Eggs and Egg Products Refrigeration"
description: "Technical design specifications for egg and egg products refrigeration systems including shell egg storage conditions, processed egg product requirements, temperature and humidity control, quality preservation parameters, and psychrometric considerations for HVAC engineers."
weight: 8
---

Egg and egg products refrigeration requires precise environmental control to maintain quality, prevent microbial growth, and extend shelf life. Shell eggs and processed egg products have distinct storage requirements that demand specialized refrigeration system design.

## Shell Egg Storage Requirements

### Temperature and Humidity Control

Shell egg storage depends on maintaining specific temperature and humidity conditions to preserve internal quality while preventing moisture loss and microbial penetration through the porous shell.

**Critical storage parameters:**

- **Temperature:** 45°F (7°C) maximum for commercial storage
- **Optimal temperature:** 40-42°F (4.4-5.6°C)
- **Humidity:** 70-80% relative humidity
- **Air velocity:** 50-100 fpm to maintain uniformity without excessive moisture loss

Temperature uniformity throughout the storage space is critical. Temperature variations exceeding ±2°F (±1.1°C) lead to condensation cycling on egg surfaces, promoting bacterial penetration through shell pores.

### Psychrometric Considerations

The psychrometric conditions in shell egg coolers must balance competing requirements:

| Parameter | Value | Engineering Basis |
|-----------|-------|-------------------|
| Dry-bulb temperature | 40-42°F | Minimizes microbial growth without freezing |
| Relative humidity | 70-80% | Prevents excessive moisture loss (weight loss) |
| Dew point | 35-38°F | Prevents surface condensation during temperature cycling |
| Vapor pressure deficit | 0.08-0.12 in Hg | Controls transpiration rate through shell |

Shell eggs lose approximately 0.01% of their weight per day at 70% RH and 0.02% per day at 60% RH at 45°F. This moisture loss degrades internal quality by increasing air cell size and reducing albumen viscosity.

## Processed Egg Products Storage

### Liquid Egg Products

Liquid whole eggs, egg whites, and egg yolks require refrigeration immediately after breaking and processing to prevent rapid microbial growth.

**Storage conditions for liquid eggs:**

| Product Type | Temperature | Maximum Storage | Notes |
|--------------|-------------|-----------------|-------|
| Liquid whole eggs | 33-35°F (0.6-1.7°C) | 7 days | Highly perishable |
| Liquid egg whites | 33-35°F (0.6-1.7°C) | 7-10 days | Lower microbial risk |
| Liquid egg yolks | 33-35°F (0.6-1.7°C) | 5 days | Highest microbial risk |
| Pasteurized liquid eggs | 33-38°F (0.6-3.3°C) | 21-28 days | Extended shelf life |

Liquid egg products freeze at approximately 28-30°F (-2.2 to -1.1°C), requiring precise temperature control to maintain product just above freezing point without ice crystal formation.

### Frozen Egg Products

Frozen egg products provide extended storage capability for industrial food processing applications.

**Frozen storage parameters:**

- **Blast freezing temperature:** -20 to -40°F (-29 to -40°C)
- **Long-term storage:** 0 to -10°F (-18 to -23°C)
- **Freezing time:** 2-4 hours to reach -10°F core temperature
- **Storage duration:** 12 months at 0°F, 24 months at -10°F

Rapid freezing is essential to minimize ice crystal size and maintain product functionality upon thawing. Slow freezing creates large ice crystals that damage protein structure, reducing foaming and emulsification properties.

### Dried Egg Products

Dried egg powders require controlled cold storage to maintain functional properties and prevent lipid oxidation.

| Product | Temperature | Relative Humidity | Storage Life |
|---------|-------------|-------------------|--------------|
| Whole egg powder | 40-50°F (4-10°C) | <50% | 12 months |
| Egg white powder | 40-60°F (4-16°C) | <60% | 24 months |
| Egg yolk powder | 35-45°F (2-7°C) | <40% | 6-9 months |

Egg yolk powder is most susceptible to oxidative rancidity due to high lipid content, requiring lower storage temperatures and controlled humidity to prevent moisture absorption.

## Refrigeration System Design Considerations

### Load Calculations

Refrigeration loads for egg storage facilities include:

**Shell egg cooler loads:**

1. **Product cooling load:** Q = m × cp × ΔT
   - Mass flow rate of eggs entering storage
   - Specific heat of eggs: 0.76 BTU/(lb·°F)
   - Temperature reduction from ambient to storage temperature

2. **Respiration heat:** 0.15-0.20 BTU/(lb·day) at 45°F
   - Shell eggs continue metabolic activity during storage
   - Heat generation decreases with lower temperature

3. **Transmission load:** Through walls, floor, ceiling
   - Insulation R-value typically R-25 to R-30 for walls
   - R-40 for ceiling due to warm air stratification above

4. **Infiltration load:** From door openings and air leakage
   - Critical during egg loading/unloading operations
   - Air curtains and rapid-acting doors minimize impact

### Evaporator Selection

Shell egg coolers require specific evaporator characteristics:

- **Temperature difference:** 8-12°F (4.4-6.7°C) between refrigerant and air
- **Fin spacing:** 4-6 fins per inch to prevent frost accumulation
- **Defrost method:** Electric or hot gas defrost on time/temperature initiation
- **Defrost frequency:** Every 8-12 hours depending on humidity load

Larger temperature differences (>12°F) create excessive dehumidification, reducing storage humidity below the 70-80% target range. This increases egg weight loss and quality degradation.

## Quality Preservation Parameters

### Microbial Control

Temperature is the primary factor controlling microbial growth on and in eggs:

| Temperature | Bacterial Growth Rate | Storage Impact |
|-------------|----------------------|----------------|
| 68°F (20°C) | Normal growth | 3-5 weeks shelf life |
| 45°F (7°C) | 50% reduction | 10-12 weeks shelf life |
| 40°F (4°C) | 70% reduction | 14-16 weeks shelf life |
| 35°F (2°C) | 85% reduction | 20+ weeks shelf life |

Salmonella enteritidis growth is inhibited below 45°F, making temperature control critical for food safety.

### Chemical Quality Changes

Temperature affects the rate of chemical quality degradation in eggs:

**Albumen thinning rate constants:**

- At 68°F: k = 0.015 Haugh units/day
- At 45°F: k = 0.004 Haugh units/day
- At 35°F: k = 0.002 Haugh units/day

The Haugh unit measures albumen quality, with values >72 indicating AA grade eggs. Temperature reduction by 10°F approximately doubles egg shelf life relative to quality retention.

### Carbon Dioxide Loss

Fresh eggs contain 3-4% CO₂ dissolved in the albumen, which maintains pH and viscosity. CO₂ diffuses through the shell pores during storage:

- **Loss rate at 68°F:** 25% CO₂ loss per week
- **Loss rate at 45°F:** 8% CO₂ loss per week
- **Loss rate at 35°F:** 4% CO₂ loss per week

Lower storage temperatures reduce CO₂ diffusion rate, maintaining internal egg quality for extended periods.

## Air Distribution Design

### Shell Egg Coolers

Proper air distribution prevents temperature stratification and maintains uniform conditions throughout the storage space.

**Design parameters:**

- **Air changes:** 40-60 air changes per hour
- **Supply air temperature:** 38-40°F (3.3-4.4°C)
- **Supply/return differential:** 2-4°F (1.1-2.2°C)
- **Duct velocity:** 1200-1500 fpm in mains, 600-800 fpm in branches

Overhead air distribution with perforated ducts or linear diffusers provides uniform air delivery across egg pallets. Return air should be collected from multiple points to prevent dead zones.

### Processed Egg Product Coolers

Liquid egg processing rooms require higher air velocities to rapidly cool product post-pasteurization:

- **Room temperature:** 45-50°F (7-10°C)
- **Air velocity:** 100-150 fpm over product tanks
- **Air changes:** 30-40 per hour
- **Temperature uniformity:** ±1°F throughout space

## Defrost and Humidity Management

### Defrost System Design

Evaporator coils in egg coolers operate below dew point, requiring regular defrost cycles:

**Electric defrost specifications:**

- Power density: 25-35 watts per square foot of coil face area
- Defrost duration: 20-30 minutes
- Defrost termination: 55-65°F coil surface temperature
- Drain pan heating: Prevent refreezing of condensate

**Hot gas defrost specifications:**

- Refrigerant temperature: 90-110°F at coil inlet
- Defrost duration: 15-25 minutes
- Pressure control: Maintain 150-200 psig in coil during defrost

### Humidity Control Systems

Maintaining 70-80% RH in shell egg coolers requires humidity addition in low-humidity climates or during winter operation:

- **Ultrasonic humidifiers:** 2-5 micron droplet size prevents surface wetting
- **Evaporative pad humidifiers:** Simple, energy-efficient for large spaces
- **Atomizing nozzles:** High-pressure water spray (800-1000 psi)

Humidification capacity requirement: 0.5-1.0 lb water/(1000 ft³·hour) to compensate for dehumidification by refrigeration coils.

## Energy Efficiency Considerations

### Temperature Management Strategies

Graduated cooling protocols reduce energy consumption while maintaining product quality:

1. **Staging:** Cool incoming eggs gradually from ambient to storage temperature over 24-48 hours
2. **Night setback:** Reduce temperature by 2-4°F during low-rate periods (not applicable for continuous operations)
3. **Load shifting:** Schedule intensive cooling during off-peak electrical rate periods

### Refrigeration System Optimization

- **Floating head pressure control:** Reduce condensing temperature during cool ambient conditions
- **Variable speed compressors:** Match capacity to actual load rather than cycling on/off
- **Evaporator pressure regulation:** Maintain optimal suction pressure for efficiency
- **Heat recovery:** Capture condenser heat for facility heating or hot water

Properly optimized systems achieve energy efficiency ratios (EER) of 12-15 BTU/W·h for shell egg coolers operating at 40°F storage temperature.

