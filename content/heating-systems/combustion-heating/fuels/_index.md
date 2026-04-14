---
title: "Fuels"
aliases: ["Fuels"]
description: "Technical analysis of heating fuels including natural gas, propane, and fuel oil properties, heating values, combustion characteristics, and fuel selection criteria for commercial and residential HVAC applications."
weight: 2
---

Heating fuel selection significantly impacts combustion system design, efficiency, operating costs, and environmental performance. The three primary fuels used in HVAC combustion systems are natural gas, propane (liquefied petroleum gas), and fuel oil, each characterized by distinct physical properties, combustion characteristics, and handling requirements.

## Fuel Property Fundamentals

Fuel performance in combustion heating systems depends on chemical composition, energy content, and combustion characteristics. The key properties that influence system design include heating value, specific gravity, stoichiometric air-fuel ratio, and ignition characteristics.

### Heating Values

Heating value represents the energy released during complete combustion and exists in two forms:

**Higher Heating Value (HHV)**: Also called gross heating value, includes the latent heat of vaporization of water vapor formed during combustion. HHV assumes all combustion products cool to the initial fuel temperature and water vapor condenses to liquid state. This value is used for rating conventional heating equipment and appears on most manufacturer specifications.

**Lower Heating Value (LHV)**: Also called net heating value, excludes the latent heat of water vapor. LHV assumes water remains as vapor in combustion products. This value more accurately represents usable heat in conventional systems where flue gases exit above water dew point. European equipment ratings typically use LHV.

The relationship between HHV and LHV depends on fuel hydrogen content, as hydrogen combustion produces water vapor:

LHV = HHV - (m_water × h_fg)

Where m_water represents mass of water formed and h_fg is the latent heat of vaporization at reference conditions.

Condensing equipment can recover a portion of this latent heat, achieving efficiencies above 100% when referenced to LHV or above 90% when referenced to HHV.

## Natural Gas

Natural gas consists primarily of methane (CH₄) with smaller quantities of ethane, propane, butane, and inert gases. Composition varies by source and processing, affecting heating value and combustion characteristics.

### Composition and Properties

Typical natural gas composition in North America:

| Component | Volume % | Range |
|-----------|----------|-------|
| Methane (CH₄) | 95.0 | 87-97 |
| Ethane (C₂H₆) | 2.5 | 1.5-7 |
| Propane (C₃H₈) | 0.2 | 0.1-1.5 |
| Butane (C₄H₁₀) | 0.03 | 0-0.3 |
| Carbon Dioxide (CO₂) | 1.0 | 0.1-2 |
| Nitrogen (N₂) | 1.3 | 0.5-5 |

This variation necessitates proper combustion system adjustment for local gas composition.

### Natural Gas Characteristics

**Physical Properties**:
- Specific gravity: 0.60-0.70 (air = 1.0)
- Density at 60°F, 14.7 psia: 0.042-0.047 lb/ft³
- Heating value (HHV): 1,000-1,050 Btu/ft³
- Heating value (LHV): 900-950 Btu/ft³
- Wobbe Index: 1,310-1,390 Btu/ft³

**Combustion Properties**:
- Stoichiometric air-fuel ratio: 9.7:1 by volume (for pure methane)
- Theoretical air requirement: 9.5-10.5 ft³ air/ft³ gas
- Ignition temperature: 900-1,170°F
- Flammability limits: 5-15% by volume in air
- Flame speed: 0.37 m/s (laminar)

### Advantages of Natural Gas

Natural gas offers several operational advantages:

- Clean combustion with minimal soot or particulate formation
- No on-site storage required (utility supply)
- Lower carbon content produces less CO₂ per Btu than oil
- Gaseous state enables precise control and complete mixing
- Generally lower fuel cost per Btu in most markets
- Minimal maintenance requirements for fuel handling systems

### Limitations

- Requires utility infrastructure or pipeline access
- Subject to utility interruptions and curtailment
- Lower energy density requires larger volume flow
- Potential for gas leaks due to low specific gravity
- Combustion air requirements similar to other hydrocarbon fuels

## Propane (LPG)

Propane, or liquified petroleum gas (LPG), consists primarily of C₃H₈ with varying amounts of propylene, butane, and butylene. Stored as liquid under moderate pressure, it vaporizes when released to atmospheric pressure.

### Physical Properties

**Liquid Phase** (at 60°F):
- Specific gravity: 0.504 (water = 1.0)
- Density: 4.20 lb/gal
- Boiling point at 14.7 psia: -44°F
- Vapor pressure at 70°F: 124 psig
- Vapor pressure at 100°F: 196 psig

**Vapor Phase**:
- Specific gravity: 1.52 (air = 1.0)
- Density at 60°F, 14.7 psia: 0.1162 lb/ft³
- Heating value (HHV): 2,516 Btu/ft³ vapor, 91,500 Btu/gal liquid
- Heating value (LHV): 2,385 Btu/ft³ vapor, 84,300 Btu/gal liquid

### Combustion Characteristics

- Stoichiometric air-fuel ratio: 23.8:1 by volume
- Theoretical air requirement: 24 ft³ air/ft³ gas
- Ignition temperature: 920-1,120°F
- Flammability limits: 2.1-9.5% by volume in air
- Flame speed: 0.46 m/s (laminar)

### Storage and Vaporization

Propane storage requires pressure vessels rated for vapor pressure at maximum ambient temperature. Tank sizing must account for both liquid volume and vaporization capacity.

**Vaporization Rate**: Natural vaporization from tank surface depends on ambient temperature and liquid surface area. Insufficient vaporization capacity causes pressure drop and reduced equipment capacity.

Vaporization rate (Btu/hr) = K × A × ΔT

Where:
- K = overall heat transfer coefficient (Btu/hr·ft²·°F)
- A = wetted surface area (ft²)
- ΔT = temperature difference between ambient and liquid (°F)

External vaporizers may be required for high-capacity systems or cold climates where natural vaporization proves insufficient.

### Propane System Considerations

**Advantages**:
- Higher energy density than natural gas (2.5× per cubic foot)
- Available in areas without natural gas service
- Portability enables temporary or remote installations
- Dual fuel capability with natural gas (requires conversion)
- Cleaner combustion than fuel oil

**Limitations**:
- Vapor heavier than air accumulates in low areas (safety concern)
- On-site storage required with associated costs
- Vaporization capacity limits in cold weather
- Pressure regulation required for consistent supply
- Higher fuel cost per Btu than natural gas in most markets

## Fuel Oil

Fuel oil for heating applications consists of refined petroleum distillates and residual oils, classified by viscosity and processing level. No. 2 fuel oil (heating oil) dominates residential and light commercial applications, while No. 4, 5, and 6 (heavy oils) serve larger industrial and institutional systems.

### No. 2 Fuel Oil Properties

**Physical Characteristics**:
- Specific gravity at 60°F: 0.82-0.95 (water = 1.0)
- Density: 6.8-7.9 lb/gal
- Viscosity at 100°F: 1.9-4.1 centistokes
- Flash point: 100-130°F minimum
- Pour point: 0°F maximum

**Energy Content**:
- Heating value (HHV): 137,000-141,000 Btu/gal
- Heating value (LHV): 129,000-133,000 Btu/gal
- Typical design value: 140,000 Btu/gal

### Fuel Oil Combustion

**Combustion Air Requirements**:
- Stoichiometric air-fuel ratio: 1,500 lb air/gal oil (by mass)
- Theoretical air requirement: 10.8 lb air/lb fuel
- Excess air requirement: 15-30% for complete combustion

**Combustion Products** (per gallon at 15% excess air):
- CO₂: 22 lb
- H₂O: 11 lb
- Flue gas volume: 1,660 ft³ at 60°F

### Atomization and Combustion

Fuel oil requires atomization into fine droplets for efficient combustion. Droplet size distribution affects flame characteristics, combustion efficiency, and emissions:

- Sauter Mean Diameter: 30-80 microns optimal
- Spray angle: 45-90° typical
- Spray pattern: Hollow cone or solid cone

Atomization methods include:

**Pressure Atomization**: High-pressure pump forces oil through nozzle orifice, creating mechanical atomization through turbulence and hydraulic forces.

**Air Atomization**: Compressed air mixes with oil at nozzle, breaking liquid into droplets through momentum transfer.

**Steam Atomization**: Steam provides atomizing energy for heavy oils requiring elevated temperatures.

### Fuel Oil System Requirements

**Storage**:
- Above-ground or underground tanks (steel or fiberglass)
- Vent and fill piping for delivery
- Leak detection for underground installations
- Secondary containment in some jurisdictions

**Fuel Handling**:
- Supply pump maintaining 100-150 psi for pressure nozzles
- Fuel filtration to remove sediment and water
- Heating for heavy oils to reduce viscosity
- Piping materials compatible with petroleum products

### Fuel Oil Considerations

**Advantages**:
- High energy density enables compact storage
- Independent of utility infrastructure
- Fuel availability during electrical outages
- Well-established technology and service network
- Dual fuel capability in some systems

**Limitations**:
- Storage tank requirements and regulations
- Potential for spills and environmental contamination
- Combustion produces more emissions than gaseous fuels
- Requires regular maintenance (nozzles, filters, combustion chamber)
- Soot formation requires periodic cleaning
- Higher particulate matter and sulfur emissions

## Combustion Air Requirements

All hydrocarbon fuels require oxygen for combustion. Theoretical air represents the stoichiometric quantity for complete combustion. Actual systems require excess air to ensure complete combustion and account for imperfect mixing.

### Theoretical Air Calculation

For any hydrocarbon fuel C_x H_y:

C_x H_y + (x + y/4) O₂ → x CO₂ + (y/2) H₂O

Since air contains approximately 21% oxygen by volume (23.15% by mass):

Theoretical air = (x + y/4) × (100/21) moles air/mole fuel

### Excess Air Requirements

Practical combustion systems operate with excess air beyond theoretical requirements:

| Fuel Type | Typical Excess Air | Range |
|-----------|-------------------|-------|
| Natural gas (atmospheric burner) | 40-50% | 30-100% |
| Natural gas (power burner) | 10-20% | 5-30% |
| Propane (atmospheric burner) | 40-50% | 30-100% |
| Propane (power burner) | 10-20% | 5-30% |
| No. 2 oil (pressure atomizing) | 20-30% | 15-40% |
| Heavy oil (steam atomizing) | 25-35% | 20-50% |

Excess air optimization balances complete combustion against heat loss. Insufficient excess air produces carbon monoxide and soot; excessive excess air reduces efficiency by heating unnecessary air mass.

## Fuel Comparison Table

| Property | Natural Gas | Propane | No. 2 Oil |
|----------|-------------|---------|-----------|
| **Energy Content** |
| HHV | 1,025 Btu/ft³ | 2,516 Btu/ft³ | 140,000 Btu/gal |
| LHV | 925 Btu/ft³ | 2,385 Btu/ft³ | 132,000 Btu/gal |
| **Physical State** | Gas | Liquid/Gas | Liquid |
| **Specific Gravity** | 0.65 | 1.52 (vapor) | 0.85 |
| **Storage Pressure** | Line pressure | 100-200 psig | Atmospheric |
| **Ignition Temp** | 1,050°F | 920-1,120°F | 500-650°F |
| **Stoich Air/Fuel** | 9.7:1 (vol) | 23.8:1 (vol) | 1,500 lb/gal |
| **Carbon Content** | Low | Medium | High |
| **Typical Efficiency** | 80-98% | 80-98% | 78-88% |

## Fuel Selection Criteria

### Availability and Infrastructure

Geographic location determines fuel availability. Natural gas requires pipeline infrastructure; propane and oil require delivery access and storage facilities. Urban areas typically offer all options; rural locations may limit choices to propane or oil.

### Operating Cost Analysis

Total fuel cost includes commodity price, delivery charges, storage costs, and efficiency losses. Economic analysis should evaluate:

- Annual fuel consumption based on heating load
- Current and projected fuel prices
- Delivery frequency and minimum order quantities
- Storage tank rental or purchase costs
- Efficiency differences between fuel types

### Equipment Considerations

Burner design, heat exchanger configuration, and venting requirements vary by fuel. Conversion between fuels requires component replacement and combustion system adjustment.

**Natural Gas Systems**: Simple fuel train, atmospheric or power burners, Category I or condensing venting.

**Propane Systems**: Similar to natural gas with modified orifices and pressure regulation, larger gas piping for equivalent capacity.

**Oil Systems**: Fuel pump, atomizing nozzle, larger combustion chamber, draft control requirements.

### Emissions and Environmental Impact

Environmental regulations and sustainability goals influence fuel selection:

**CO₂ Emissions** (per million Btu input):
- Natural gas: 117 lb CO₂
- Propane: 139 lb CO₂
- No. 2 oil: 161 lb CO₂

Natural gas produces the lowest carbon emissions per unit energy. However, methane leakage in production and distribution adds greenhouse gas impact not reflected in combustion emissions alone.

**Local Air Quality**: Oil combustion produces particulate matter and sulfur compounds. Low-sulfur fuel oil (15 ppm maximum) reduces SO₂ emissions but at premium cost. Natural gas and propane combustion produce minimal particulates.

### Reliability and Security

Fuel supply reliability affects system design for critical applications:

- Natural gas: Subject to utility interruptions and pipeline capacity constraints
- Propane: On-site storage provides autonomy limited by tank capacity
- Oil: On-site storage enables multi-month supply with adequate tank sizing

Dual-fuel capability or backup generators address reliability requirements for hospitals, data centers, and life-safety systems.

### Safety Considerations

Each fuel presents distinct safety requirements:

**Natural Gas**: Lighter than air disperses upward; odorant (mercaptan) enables leak detection; automatic shutoff valves and combustible gas detectors in critical locations.

**Propane**: Heavier than air accumulates in low areas; requires gas detection in basements and pits; pressure relief valves on storage vessels mandatory.

**Fuel Oil**: Liquid spills contaminate soil and groundwater; double-wall tanks and leak detection for underground storage; fire safety due to flash point above ambient temperature.

## Regulatory Compliance

Fuel selection, storage, and use must comply with:

- **NFPA 54/ANSI Z223.1**: National Fuel Gas Code (natural gas and propane)
- **NFPA 31**: Installation of Oil-Burning Equipment
- **NFPA 58**: Liquefied Petroleum Gas Code
- **EPA 40 CFR Part 63**: National Emission Standards for Hazardous Air Pollutants
- **State and local fuel storage regulations**
- **Environmental protection regulations for underground storage tanks**

Building codes specify fuel piping materials, venting requirements, combustion air provisions, and equipment clearances. Local amendments often impose additional restrictions.
