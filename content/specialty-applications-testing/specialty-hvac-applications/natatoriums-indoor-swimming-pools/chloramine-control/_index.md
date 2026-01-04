---
title: "Chloramine Control and Air Quality"
weight: 4
description: "Technical analysis of chloramine formation, health effects, and control strategies for natatorium air quality including ventilation dilution, UV treatment, and air filtration methods for indoor swimming pool facilities."
keywords: "chloramines, trichloramine, pool air quality, natatorium ventilation, indoor air quality swimming pools, chlorine byproducts, DBP control"
---

Chloramine control represents one of the most challenging aspects of natatorium indoor air quality management. Unlike conventional buildings where carbon dioxide and odors drive ventilation requirements, indoor pools must address volatile chlorine compounds that cause eye and respiratory irritation, equipment corrosion, and odor complaints even at low concentrations.

## Chemistry of Chloramine Formation

Chloramines are disinfection byproducts (DBPs) formed when free chlorine (hypochlorous acid, HOCl) reacts with nitrogenous compounds introduced by swimmers—primarily urea, ammonia, sweat, and cosmetic residues.

### Primary Reactions

**Monochloramine formation**:
NH₃ + HOCl → NH₂Cl + H₂O

**Dichloramine formation**:
NH₂Cl + HOCl → NHCl₂ + H₂O

**Trichloramine formation**:
NHCl₂ + HOCl → NCl₃ + H₂O

The relative concentrations depend on pH, chlorine-to-nitrogen ratio, temperature, and reaction time. At typical pool pH (7.2-7.8), monochloramine and dichloramine predominate in water, but trichloramine (NCl₃) has low water solubility and readily volatilizes into pool air.

### Volatilization Mechanism

Trichloramine is approximately 100 times more volatile than monochloramine. It partitions from pool water to air across the water-air interface, with transfer rate dependent on:

- **Trichloramine concentration** in pool water (typically 0.1-1.0 mg/L)
- **Temperature** (higher temperatures increase volatilization exponentially)
- **Water agitation** (activity, water features increase mass transfer)
- **Air velocity** across water surface (affects boundary layer resistance)
- **pH** (lower pH favors trichloramine formation)

A heavily-used pool can release 1-5 mg/m³ of trichloramine into indoor air—well above irritation thresholds.

## Health Effects and Exposure Limits

### Acute Effects

Trichloramine exposure causes characteristic symptoms:

**Eye irritation**: Stinging, redness, tearing at concentrations >0.3 mg/m³. Commonly misattributed to "chlorine," but actually caused by chloramines. Properly maintained pools with low chloramine levels rarely cause eye irritation despite adequate free chlorine.

**Respiratory irritation**: Coughing, throat irritation, breathing difficulty at >0.5 mg/m³. Competitive swimmers and pool staff experience chronic exposure effects.

**Odor**: Strong "chlorine smell" indicates excessive chloramines, not excess chlorine. Fresh chlorine has minimal odor. The characteristic pool smell is trichloramine.

### Chronic Exposure

Long-term chloramine exposure among pool workers and competitive swimmers is associated with:

- Occupational asthma ("lifeguard lung")
- Reactive airways dysfunction
- Increased respiratory infection susceptibility
- Potential contribution to childhood asthma development

### Recommended Limits

| Authority | Limit | Parameter |
|-----------|-------|-----------|
| WHO (World Health Organization) | 0.5 mg/m³ | Air concentration limit |
| France (ANSES) | 0.3 mg/m³ | Action level for public pools |
| Germany (DIN 19643) | 0.2 mg/m³ | Design target |
| PWTAG (UK) | 0.5 mg/m³ | Maximum exposure |

**Design Recommendation**: Maintain trichloramine below 0.3 mg/m³ under normal operating conditions, with absolute maximum of 0.5 mg/m³ during peak use.

## Source Control: Water Chemistry Management

The most effective chloramine control strategy is preventing formation through proper pool water chemistry:

### Combined Chlorine Removal

**Superchlorination (breakpoint chlorination)**:
Adding sufficient chlorine to oxidize all chloramines back to nitrogen gas and chloride:

2 NH₂Cl + HOCl → N₂ + 3 HCl + H₂O

Requires chlorine dose of approximately 7.6-10× the combined chlorine concentration. For pool with 0.5 mg/L combined chlorine, add 4-5 mg/L free chlorine beyond normal level.

Frequency: Weekly to monthly depending on bather load. More frequent in heavily-used facilities.

**UV Treatment**:
Medium-pressure UV lamps (200-400 nm wavelength) photolytically destroy chloramines in recirculated pool water:

UV photons break Cl-N bonds, releasing chlorine and oxidizing nitrogen compounds.

Typical dose: 40-60 mJ/cm² for chloramine reduction
Results: 50-90% chloramine reduction depending on dose, flow rate, water quality

UV systems are increasingly standard in commercial pools and dramatically reduce airborne chloramine concentrations.

**Ozone Treatment**:
Ozone (O₃) is a strong oxidizer that destroys chloramines:

NCl₃ + O₃ → products (nitrogen oxides, chloride)

Ozone dose: 0.5-1.0 mg/L applied to side-stream (10-20% of circulation flow)

Advantages: Powerful oxidation, reduces chlorine demand
Disadvantages: Higher cost, requires off-gassing chamber before pool return, complex controls

### pH Management

Maintain pH 7.4-7.6 (lower end of acceptable range) to minimize trichloramine formation. pH >7.8 accelerates trichloramine formation and volatilization.

### Bather Load Management

Reduce nitrogen loading through:
- Mandatory pre-swim showers (removes 75-90% of urea and cosmetics)
- Pool capacity limits
- Enforced swim diaper requirements
- Prohibition of urination in pool (education campaigns)

Well-managed bather hygiene can reduce chloramine formation by 60-80% compared to pools without enforced policies.

## Ventilation Dilution

When source control is insufficient, ventilation dilutes airborne chloramines to acceptable concentrations.

### Dilution Equation

The steady-state chloramine concentration in pool air is:

C_indoor = (G / V) / (ACH / 60)

Where:
- C_indoor = Indoor chloramine concentration (mg/m³)
- G = Generation rate from pool (mg/h)
- V = Pool enclosure volume (m³)
- ACH = Air changes per hour

Rearranging to solve for required ventilation:

ACH = (G × 60) / (V × C_target)

**Example Calculation**:

Pool generating 500 mg/h trichloramine
Pool volume: 85,000 ft³ (2,400 m³)
Target concentration: 0.3 mg/m³

ACH = (500 × 60) / (2,400 × 0.3) = 30,000 / 720 = 41.7 air changes per hour

This extremely high ventilation rate demonstrates why source control is essential. Attempting to control chloramines by ventilation alone is energy-intensive and often impractical.

### Code-Minimum Ventilation

ASHRAE 62.1 specifies minimum ventilation for pools:
- Pool water surface: 0.06 cfm/ft²
- Pool deck area: 0.48 cfm/ft²

For 1,500 ft² pool with 2,500 ft² deck:
- Pool surface: 0.06 × 1,500 = 90 cfm
- Deck: 0.48 × 2,500 = 1,200 cfm
- Total: 1,290 cfm minimum

For 60,000 ft³ enclosure volume:
ACH = (1,290 × 60) / 60,000 = 1.3 air changes per hour

This minimum ventilation is **grossly inadequate** for chloramine control in heavily-used pools. It provides baseline air quality but must be supplemented with source control measures.

### Practical Ventilation Rates

| Pool Type | Typical ACH | Notes |
|-----------|-------------|-------|
| Residential, light use | 3-4 | With good water chemistry |
| Public, moderate use | 4-6 | Requires UV or ozone treatment |
| Competition, heavy use | 6-10 | Mandatory secondary treatment |
| Therapy pools, spas | 8-12 | High temperature increases volatilization |

Higher ventilation rates increase energy consumption dramatically due to outdoor air conditioning loads. Energy recovery is essential when ACH >4.

### Air Distribution

Effective chloramine removal requires proper air distribution:

**Supply air**: Discharge high-velocity air jets along pool perimeter, directed across water surface at ~20° downward angle. Creates "air curtain" that captures chloramines as they volatilize.

**Exhaust air**: Low-level exhaust near water surface (12-36" above deck) removes highest-concentration air before it rises to breathing zone.

**Deck ventilation**: Separate supply/exhaust for spectator and deck areas, maintaining slight negative pressure relative to pool area to prevent migration.

Avoid:
- High-velocity air across pool surface (increases evaporation)
- Ceiling-only exhaust (chloramines stratify near water)
- Supply air directed at swimmers (causes discomfort)

## UV Air Treatment

While UV treatment of pool water reduces chloramine formation, UV irradiation of pool air can directly destroy airborne trichloramine.

### Operating Principle

UV-C radiation (254 nm) photolyzes trichloramine molecules:

NCl₃ + UV photons → Cl· + ·NCl₂ → further breakdown products

Reactions occur in UV lamp chamber with high-intensity exposure.

### System Design

**Configuration**: Return air stream passes through UV lamp chamber before dehumidification/heating and supply.

**UV dose**: 500-2,000 mJ/cm² (much higher than water treatment)

**Residence time**: 0.5-2.0 seconds at typical air velocities

**Lamp type**: Low-pressure or medium-pressure mercury lamps, amalgam lamps for stability

**Effectiveness**: 30-70% single-pass destruction at typical doses

### Design Considerations

- High UV dose requirements increase energy consumption
- Lamp maintenance (annual replacement)
- Ozone generation from UV-C requires catalytic destruction or increased ventilation
- Pre-filtration required to prevent dust accumulation on lamps
- Not a substitute for adequate ventilation, but reduces required ACH

Combined with pool water UV treatment, air UV can achieve trichloramine levels <0.2 mg/m³ in well-managed facilities.

## Activated Carbon Filtration

Activated carbon adsorbs chloramines and other volatile organic compounds.

**Media**: Granular activated carbon (GAC) or carbon-impregnated filters

**Application**: Partial bypass air treatment (10-30% of air circulation) through deep-bed carbon filters

**Contact time**: 0.2-0.5 seconds minimum

**Effectiveness**: 60-90% removal efficiency when fresh, declining to 20-40% as carbon saturates

**Regeneration**: Carbon requires periodic replacement (6-24 months) or off-site thermal regeneration

**Limitations**:
- High pressure drop (1-3 in. w.c.)
- Moderate first cost, ongoing replacement expense
- Chloramines eventually oxidize carbon, reducing capacity
- Not viable as sole control measure

Carbon filtration is occasionally used as polishing step in premium facilities but rarely economically justified as primary control.

## Integrated Control Strategy

Effective chloramine management requires multi-layered approach:

### Primary Level: Water Chemistry
1. UV and/or ozone treatment of pool water
2. Weekly superchlorination
3. pH control (7.4-7.6)
4. Enforced pre-swim showering
5. Regular backwashing and filter maintenance

### Secondary Level: Ventilation
1. 4-8 ACH minimum (more for heavily-used pools)
2. Proper air distribution (perimeter supply, low-level exhaust)
3. Continuous operation during pool hours
4. Energy recovery to minimize operating cost

### Tertiary Level: Air Treatment (if needed)
1. UV air treatment for high-use facilities
2. Activated carbon polishing (rarely)

### Monitoring and Verification
1. Periodic air sampling for trichloramine concentration
2. Water testing: free chlorine, combined chlorine, pH
3. Occupant feedback on eye/respiratory irritation
4. Visual inspection for corrosion indicators

## Troubleshooting High Chloramines

When chloramine levels exceed 0.5 mg/m³ despite controls:

**Water Chemistry Issues**:
- Check combined chlorine in water (should be <0.2 mg/L)
- Verify UV/ozone system operation
- Implement immediate superchlorination
- Inspect for water chemistry controller malfunction

**Ventilation Issues**:
- Verify outdoor air damper position (fully open?)
- Check exhaust fan operation
- Measure actual air change rate (tracer gas test)
- Inspect for air distribution short-circuiting

**Operational Issues**:
- Review bather load (exceeding design capacity?)
- Verify pre-swim shower usage
- Check water temperature (excessive?)
- Inspect for water features increasing volatilization

**Equipment Issues**:
- UV lamp intensity (age, fouling?)
- Ozone generator output
- Ventilation system filters (clogged?)

Chloramine control requires sustained attention to water chemistry, ventilation operation, and facility management. It cannot be solved by HVAC alone but requires integrated approach across all systems and operational practices.
