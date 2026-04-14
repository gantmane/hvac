---
title: "Wine Production"
aliases: ["Wine Production"]
weight: 2
---

Wine production requires precise refrigeration control across multiple process stages, from fermentation temperature management to cold stabilization and long-term barrel storage. Each wine variety demands specific thermal conditions to develop desired flavor profiles, prevent spoilage, and achieve chemical stability.

## Fermentation Temperature Control

Fermentation generates metabolic heat that must be removed to maintain target temperatures. Heat generation rate depends on sugar concentration, yeast activity, and fermentation stage.

**Heat Release During Fermentation:**

Q_fermentation = 25 BTU/lb sugar metabolized (approximately)

For a 1000-gallon fermentation tank with 22°Brix must:
- Sugar content: 1000 gal × 8.34 lb/gal × 1.09 SG × 0.22 = 2,010 lb sugar
- Total heat release: 2,010 lb × 25 BTU/lb = 50,250 BTU
- Peak heat generation rate: 10,000-15,000 BTU/hr during active fermentation

### White Wine Fermentation

White wines require lower fermentation temperatures to preserve delicate aromatic compounds and prevent volatile ester loss.

| Parameter | Cool Fermentation | Standard Fermentation |
|-----------|------------------|----------------------|
| Temperature Range | 50-60°F (10-16°C) | 60-68°F (16-20°C) |
| Duration | 14-30 days | 7-14 days |
| Cooling Load (per 1000 gal) | 8,000-12,000 BTU/hr | 6,000-10,000 BTU/hr |
| Volatile Ester Retention | High | Moderate |
| Fruit Character | Enhanced | Standard |

**Cooling Methods:**
- Jacketed fermentation tanks with glycol circulation
- Internal cooling coils (stainless steel)
- External heat exchangers with must recirculation
- Controlled-temperature room with tank insulation

Glycol systems typically operate at 28-32°F (-2 to 0°C) with 30-35% propylene glycol concentration to provide adequate temperature differential.

### Red Wine Fermentation

Red wines ferment at higher temperatures to extract color, tannins, and phenolic compounds from grape skins.

| Parameter | Standard Red | Cold Soak | Extended Maceration |
|-----------|-------------|-----------|-------------------|
| Initial Soak Temperature | N/A | 45-55°F (7-13°C) | N/A |
| Fermentation Temperature | 75-85°F (24-29°C) | 70-80°F (21-27°C) | 75-90°F (24-32°C) |
| Peak Temperature Control | ±2°F | ±2°F | ±3°F |
| Color Extraction | Standard | Enhanced | Maximum |
| Tannin Extraction | Moderate | Controlled | High |

Red wine fermentation requires both cooling and heating capability:
- Cooling during peak fermentation activity
- Heating during cold soak phase and cool ambient conditions
- Temperature ramp control for extended maceration

## Barrel Storage Climate Control

Barrel aging requires stable temperature and humidity conditions to control evaporation rates, prevent microbial growth, and ensure consistent wine development.

### Temperature Requirements

| Wine Type | Storage Temperature | Tolerance | Annual Temperature Swing |
|-----------|-------------------|-----------|------------------------|
| Red Wine Aging | 55-60°F (13-16°C) | ±3°F (±2°C) | <10°F (<6°C) |
| White Wine Aging | 50-55°F (10-13°C) | ±3°F (±2°C) | <8°F (<5°C) |
| Sparkling Wine (tirage) | 50-55°F (10-13°C) | ±2°F (±1°C) | <5°F (<3°C) |
| Premium/Reserve | 55-58°F (13-14°C) | ±1°F (±0.5°C) | <5°F (<3°C) |

**Cooling Load Calculation for Barrel Rooms:**

Q_total = Q_transmission + Q_barrels + Q_infiltration + Q_lighting + Q_personnel

Where:
- Q_transmission = U × A × ΔT (building envelope heat gain)
- Q_barrels = m_wine × c_p × ΔT + m_evap × h_fg (wine cooling + evaporation)
- Q_infiltration = 1.08 × CFM × ΔT + 0.68 × CFM × Δω (sensible + latent)

Typical barrel room cooling loads: 8-12 BTU/hr per square foot

### Humidity Control

Relative humidity affects evaporation rates through barrel staves, impacting both wine volume loss and flavor concentration.

| Relative Humidity | Water Loss | Alcohol Loss | Net Effect |
|------------------|------------|--------------|------------|
| 50-60% | High | Low | Wine concentrates, alcohol increases |
| 65-75% | Moderate | Moderate | Balanced evaporation |
| 75-85% | Low | High | Wine dilutes, alcohol decreases |
| >85% | Minimal | High | Mold risk, excessive alcohol loss |

Target RH: 70-75% for balanced aging

Evaporation rate (angel's share): 2-4% volume loss per year at 70-75% RH

**Humidity Control Methods:**
- Direct steam injection (requires pure steam generation)
- Ultrasonic humidification (prevents mineral deposits on barrels)
- Evaporative media with filtered water
- Dehumidification during high ambient humidity periods

## Cold Stabilization

Cold stabilization precipitates tartrate crystals before bottling to prevent post-bottling precipitation. This process requires precise low-temperature control.

### Process Parameters

| Wine Type | Stabilization Temperature | Hold Time | Tartrate Reduction |
|-----------|-------------------------|-----------|------------------|
| White Wine | 25-30°F (-4 to -1°C) | 5-10 days | 90-95% |
| Rosé | 28-32°F (-2 to 0°C) | 5-8 days | 85-90% |
| Red Wine | 30-35°F (-1 to 2°C) | 7-14 days | 80-90% |
| Sparkling Wine (base) | 25-28°F (-4 to -2°C) | 8-12 days | 95-98% |

**Cooling Load for Cold Stabilization:**

Q_stabilization = (m_wine × c_p × ΔT) / t_cooldown + Q_losses

Example for 5,000 gallons white wine (70°F to 28°F in 24 hours):
- Wine mass: 5,000 gal × 8.5 lb/gal = 42,500 lb
- Specific heat: 0.95 BTU/lb-°F
- Temperature change: 70°F - 28°F = 42°F
- Heat removal: 42,500 × 0.95 × 42 = 1,695,750 BTU
- Required capacity (24 hr): 1,695,750 / 24 = 70,656 BTU/hr
- With safety factor (1.25): 88,320 BTU/hr (7.4 tons)

### Contact Stabilization

Accelerated process using potassium bitartrate seeding crystals at cold temperatures.

**Process Advantages:**
- Reduced hold time: 1-3 days vs. 5-10 days
- Lower energy consumption
- Improved production throughput
- More predictable results

**Temperature Control Requirements:**
- Rapid cooling to 28-30°F (-2 to -1°C)
- Agitation during crystal addition
- Controlled warming after filtration to prevent thermal shock

## Refrigeration System Design

### Glycol Circulation Systems

Primary method for fermentation tank and cold stabilization cooling.

**System Components:**
- Glycol chiller (typically screw or scroll compressor)
- Insulated glycol storage tank (buffer capacity)
- Variable-speed circulation pumps
- Zone control manifolds for individual tank control
- Temperature sensors with ±0.5°F accuracy

**Glycol Specifications:**

| Application | Glycol Type | Concentration | Supply Temperature | Return ΔT |
|-------------|-------------|---------------|-------------------|-----------|
| Fermentation Control | Propylene Glycol | 30-35% | 28-32°F (-2 to 0°C) | 8-12°F |
| Cold Stabilization | Propylene Glycol | 35-40% | 20-25°F (-7 to -4°C) | 10-15°F |
| Rapid Cooling | Propylene Glycol | 40-45% | 15-20°F (-9 to -7°C) | 12-18°F |

Flow rate calculation:
GPM = (Q_BTU/hr) / (500 × ΔT × SG)

### Direct Expansion Systems

Used for barrel room and warehouse cooling where precise individual tank control is not required.

**System Characteristics:**
- Lower first cost than glycol systems
- Higher energy efficiency for steady-state loads
- Multiple evaporator zones for different storage areas
- Defrost cycles required for low-temperature applications

**Typical Configuration:**
- Air-cooled condensing units (outdoor installation)
- Multiple ceiling-mounted or wall-mounted evaporators
- Electronic expansion valves for precise superheat control
- Microprocessor controls with humidity management

## Heat Recovery Opportunities

Winery refrigeration systems reject substantial heat that can be recovered for process heating.

**Heat Recovery Applications:**

| Heat Source | Temperature Available | Potential Use | Energy Offset |
|-------------|---------------------|---------------|---------------|
| Chiller Condenser | 95-110°F (35-43°C) | Barrel wash water heating | 30-40% of heat rejected |
| Hot Gas Reheat | 140-160°F (60-71°C) | CIP solution heating | 15-25% of heat rejected |
| Desuperheater | 160-200°F (71-93°C) | Domestic hot water | 10-20% of heat rejected |

Heat recovery effectiveness: 40-60% of total refrigeration energy input

## Process Integration Considerations

**Harvest Season Peak Loads:**
- Fermentation cooling capacity must handle simultaneous tank operation
- Diversity factor: 0.6-0.8 (not all tanks at peak simultaneously)
- Backup capacity recommendation: 20-30% above calculated peak

**Energy Efficiency Measures:**
- Variable-speed compressors for part-load operation
- Free cooling with glycol-to-air heat exchangers during cold weather
- Thermal storage (ice bank) for peak shaving
- Heat recovery integration with process loads

**Control Strategy:**
- Individual tank temperature control with ±0.5°F accuracy
- Automated cooling/heating switchover for red fermentation
- Alarm systems for out-of-range conditions
- Remote monitoring and trending

**Safety and Sanitary Design:**
- Food-grade glycol (propylene glycol, never ethylene glycol)
- Stainless steel wetted surfaces in cooling coils
- CIP-compatible connections and fittings
- Leak detection for glycol systems
- Emergency backup cooling capability for critical fermentations
