---
title: "Energy Storage Research"
aliases: ["Energy Storage Research"]
description: "Advanced research in thermal energy storage systems, ice storage, chilled water storage, phase change materials, and battery integration for HVAC load shifting and demand response applications."
weight: 2
---

Energy storage research addresses peak demand reduction, load shifting, renewable energy integration, and economic optimization of HVAC systems through thermal and electrical storage technologies.

## Thermal Energy Storage Fundamentals

Thermal energy storage (TES) systems store heating or cooling capacity for later use, decoupling energy production from consumption. Storage enables cost reduction through time-of-use rate arbitrage and improves grid stability by shifting electrical loads.

**Storage capacity equation:**

Q = m × c × ΔT (sensible storage)
Q = m × hfg (latent storage)

Where:
- Q = stored energy (Btu or kJ)
- m = mass of storage medium (lb or kg)
- c = specific heat (Btu/lb·°F or kJ/kg·K)
- ΔT = temperature change (°F or K)
- hfg = latent heat of fusion (Btu/lb or kJ/kg)

**Efficiency metrics:**

ηstorage = Qout / Qin × 100%

Practical storage efficiencies range from 85-95% depending on configuration, insulation, and operating conditions.

## Ice Storage Systems

Ice storage produces ice during off-peak hours using chillers operating at low loads and higher efficiency. Ice melts during peak periods to provide cooling without chiller operation.

### Ice-on-Coil Systems

Polyethylene tanks contain coils submerged in water. Glycol solution at 18-22°F circulates through coils, freezing surrounding water.

**Charge characteristics:**
- Ice builds uniformly around coils
- Complete freeze time: 6-10 hours
- Ice thickness: 0.5-1.5 inches
- Glycol supply temperature: 18-20°F
- Glycol return temperature: 22-24°F

**Discharge characteristics:**
- Melt water circulates through external heat exchanger
- Leaving water temperature: 34-36°F
- Discharge rate: variable based on demand
- Complete melt time: 4-8 hours

### Ice Harvesting Systems

Ice forms on evaporator plates, then releases into storage tank as loose ice. Harvesting cycle repeats continuously during charging.

**Operational sequence:**
1. Freeze cycle: 20-30 minutes, ice builds to 0.25-0.375 inch thickness
2. Harvest cycle: 1-3 minutes, warm refrigerant releases ice
3. Ice falls into insulated storage tank
4. Process repeats until tank is full

**Performance parameters:**
- Ice production rate: 15-25 tons per harvester module
- Storage density: 25-35 lb ice/ft³ tank volume
- Harvest efficiency: 92-96%
- Subcooling during harvest: 2-4°F

### External Melt Ice-on-Coil

Warm return water from building flows over external surface of ice-filled tubes, melting ice from outside. Internal glycol circuit remains isolated from building loop.

**Advantages:**
- Direct interface with chilled water system
- No glycol in building loop
- Lower pumping energy
- Simpler controls

**Design considerations:**
- Tank inlet/outlet manifold design critical for uniform flow
- Typical discharge approach: 2-3°F
- Water velocity over coils: 1-2 ft/s
- Stratification control required

## Chilled Water Storage

Stratified chilled water storage tanks maintain temperature separation between warm and cold water layers through density differences and careful inlet/outlet design.

### Stratification Maintenance

**Richardson number criterion:**

Ri = (g × β × ΔT × H) / V²

Where:
- Ri = Richardson number (>10 for stable stratification)
- g = gravitational acceleration (32.2 ft/s²)
- β = thermal expansion coefficient (1/°R)
- ΔT = temperature difference between layers (°F)
- H = thermocline height (ft)
- V = inlet/outlet velocity (ft/s)

**Diffuser design requirements:**
- Radial diffusers with octagonal or circular geometry
- Inlet velocity: 0.1-0.3 ft/s through diffuser openings
- Froude number: Fr < 1.0 for stability
- Multiple inlet levels for variable volume operation

### Tank Configuration

| Configuration | Volume Range | Aspect Ratio | Applications |
|--------------|--------------|--------------|--------------|
| Cylindrical vertical | 50,000-2,000,000 gal | 1:1 to 2:1 (H:D) | New construction, unlimited height |
| Cylindrical horizontal | 10,000-500,000 gal | 3:1 to 5:1 (L:D) | Height restrictions |
| Rectangular | 100,000-5,000,000 gal | Variable | Underground, structural integration |
| Modular field-erected | 500,000+ gal | Variable | Large campus systems |

**Storage capacity sizing:**

Vstorage = (Qpeak × tpeak) / (ρ × c × ΔT × ηstorage)

Where:
- Vstorage = required tank volume (gal or m³)
- Qpeak = peak cooling load (tons or kW)
- tpeak = peak period duration (hours)
- ρ = water density (8.33 lb/gal or 1000 kg/m³)
- c = specific heat (1.0 Btu/lb·°F or 4.186 kJ/kg·K)
- ΔT = temperature differential (°F or K)

### Operating Strategies

**Full storage:** Chiller off during peak hours, all cooling from storage. Requires larger tank, smaller chiller.

**Partial storage:** Chiller operates during peak hours at reduced capacity, supplemented by storage. Optimizes first cost and operating cost balance.

**Load leveling:** Constant chiller operation over 24 hours, storage absorbs load variations. Maximizes chiller efficiency.

## Phase Change Materials (PCM)

PCM research focuses on materials with high latent heat capacity at useful temperature ranges for HVAC applications. Materials store 5-14 times more energy per unit volume than sensible storage.

### Organic PCMs

**Paraffin waxes:**
- Melt temperature range: 32-140°F
- Latent heat: 75-90 Btu/lb
- Chemical stability: excellent
- Subcooling: minimal (1-2°F)
- Thermal conductivity: low (0.1 Btu/hr·ft·°F)
- Cost: moderate ($1.50-3.00/lb)

**Fatty acids:**
- Melt temperature range: 40-120°F
- Latent heat: 80-100 Btu/lb
- Chemical stability: good
- Corrosivity: low with proper containment
- Thermal cycling stability: >10,000 cycles

### Inorganic PCMs

**Salt hydrates:**
- High latent heat: 100-140 Btu/lb
- Lower cost: $0.50-1.50/lb
- Supercooling issues: requires nucleating agents
- Phase separation over cycles: requires thickening agents
- Corrosivity: moderate to high

| PCM Type | Melt Temp (°F) | Latent Heat (Btu/lb) | Density (lb/ft³) | Thermal Conductivity (Btu/hr·ft·°F) |
|----------|----------------|----------------------|------------------|-------------------------------------|
| Paraffin C16-C18 | 45-50 | 85-90 | 52-54 | 0.10-0.12 |
| Calcium chloride hexahydrate | 84 | 75 | 102 | 0.35 |
| Sodium sulfate decahydrate | 90 | 108 | 90 | 0.33 |
| Eutectic salts (custom) | 45-70 | 90-120 | 95-110 | 0.30-0.45 |

### PCM Integration Methods

**Encapsulation:**
- Macro-encapsulation: pouches, tubes, panels (>1 inch dimension)
- Micro-encapsulation: spherical particles (1-1000 μm)
- Encapsulation prevents leakage during phase transition
- Shell material must withstand thermal cycling

**Heat transfer enhancement:**
- Metal foam matrices increase effective conductivity by 10-50×
- Graphite additives improve conductivity to 1-5 Btu/hr·ft·°F
- Finned tubes increase surface area by 5-20×
- Trade-off: reduced PCM volume fraction

## Battery Energy Storage Integration

Battery systems enable electrical load shifting, demand charge reduction, and renewable integration for electrically-driven HVAC equipment.

### Battery Technologies for HVAC Applications

| Technology | Energy Density (Wh/L) | Power Density (W/L) | Cycle Life | Efficiency | Cost ($/kWh) |
|------------|----------------------|---------------------|------------|------------|--------------|
| Lithium-ion (NMC) | 400-600 | 1000-3000 | 3000-5000 | 92-95% | 300-500 |
| Lithium iron phosphate | 300-400 | 800-2000 | 4000-7000 | 90-94% | 250-400 |
| Flow battery (vanadium) | 20-40 | 10-50 | 10,000+ | 70-80% | 400-600 |
| Lead-acid (VRLA) | 80-100 | 150-300 | 500-1000 | 75-85% | 150-250 |

### Control Integration

**Peak shaving algorithm:**

Pbattery(t) = Pload(t) - Pthreshold

Battery discharges when building load exceeds threshold, maintaining flat demand profile below utility demand charge breakpoint.

**Time-of-use optimization:**

Battery charges during low-cost periods (typically nighttime), discharges during high-cost periods (afternoon peak). Optimization considers:
- Time-of-use rate structure
- Demand charges
- Battery degradation cost
- Round-trip efficiency losses

**Renewable integration:**

Battery buffers solar PV output, enabling:
- Peak demand offset from time-shifted solar
- Voltage regulation
- Frequency response
- Reduced grid interaction

### Hybrid TES-Battery Systems

Combining thermal and electrical storage optimizes total system performance:

**Chiller + ice storage + battery:**
- Battery handles short-duration peaks (<1 hour)
- Ice storage handles extended afternoon peak (4-8 hours)
- Chiller sized for average load, not peak
- Battery protects against demand charges from auxiliary loads

**Heat pump + water storage + battery:**
- Battery enables heat pump operation during low-cost hours
- Water storage provides heating/cooling during peak hours
- Combined system coefficient of performance (COP) 3-5
- Payback period: 4-8 years in high time-of-use differential markets

## Advanced Storage Research Directions

**Solid-state thermal storage:**
- Ceramic and concrete storage media for high-temperature (300-1000°F) applications
- Volumetric heat capacity: 30-50 Btu/ft³·°F
- Applications: solar thermal integration, industrial waste heat recovery

**Thermochemical storage:**
- Reversible chemical reactions store energy as chemical potential
- Energy density: 200-300 Btu/lb (2-3× PCM)
- Long-term storage without losses
- Challenges: reaction kinetics, material degradation, cost

**Underground thermal energy storage (UTES):**
- Borehole thermal energy storage (BTES): seasonal storage in soil/rock
- Aquifer thermal energy storage (ATES): warm/cold water storage in aquifers
- Capacity: 1000-100,000 MWh thermal
- Recovery efficiency: 50-90% depending on geology and duration

**Cryogenic energy storage:**
- Liquefied air energy storage (LAES)
- Air liquefaction during off-peak hours (-196°C)
- Expansion through cryogenic turbine generates power
- Integration with HVAC for cold recovery during regasification
- Round-trip efficiency: 50-70%

## Economic Analysis

**Life cycle cost analysis for storage systems:**

LCC = C₀ + Σ[(Cenergy + Cmaint - Csavings) / (1 + d)ⁿ]

Where:
- C₀ = initial capital cost
- Cenergy = annual energy cost
- Cmaint = annual maintenance cost
- Csavings = annual savings from demand reduction and TOU arbitrage
- d = discount rate
- n = year number

**Typical payback periods:**

| System Type | Capital Cost ($/ton-hr) | Simple Payback (years) | NPV Positive Scenarios |
|-------------|-------------------------|------------------------|------------------------|
| Ice storage | 150-300 | 4-8 | TOU differential >$0.15/kWh |
| Chilled water storage | 50-150 | 3-6 | Demand charges >$15/kW |
| PCM integrated | 300-600 | 6-12 | Limited space, high land cost |
| Battery (HVAC only) | 400-800 | 8-15 | Combined solar + storage incentives |

Storage economics improve with:
- Higher utility demand charges (>$15/kW-month)
- Larger time-of-use rate differentials (>$0.12/kWh)
- Longer peak periods (>6 hours/day)
- Available incentives and rebates
- Participation in demand response programs (revenue: $50-200/kW-year)
