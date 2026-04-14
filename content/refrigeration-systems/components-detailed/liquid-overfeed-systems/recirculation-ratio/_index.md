---
title: "Recirculation Ratio"
aliases: ["Recirculation Ratio"]
description: "Comprehensive analysis of recirculation ratio in liquid overfeed refrigeration systems including optimal ratio selection, heat transfer relationships, energy optimization, and application-specific design criteria for industrial refrigeration systems."
weight: 2
---

## Definition and Fundamental Concept

Recirculation ratio represents the mass flow rate of liquid refrigerant supplied to the evaporator divided by the mass flow rate of refrigerant evaporated. This parameter fundamentally determines liquid overfeed system performance, heat transfer effectiveness, and energy consumption characteristics.

**Mathematical definition:**

n = ṁ_circulated / ṁ_evaporated

Where:
- n = recirculation ratio (dimensionless)
- ṁ_circulated = total liquid mass flow rate to evaporator (kg/s)
- ṁ_evaporated = mass flow rate of refrigerant evaporated (kg/s)

The recirculation ratio directly correlates to the vapor quality at the evaporator outlet. A recirculation ratio of 4:1 indicates that for every 4 kg of liquid refrigerant entering the evaporator, 1 kg evaporates and 3 kg return as liquid to the separator vessel.

## Physical Significance

The recirculation ratio governs evaporator tube wetting characteristics. Higher ratios maintain continuous liquid film coverage on heat transfer surfaces, preventing dry patches that drastically reduce local heat transfer coefficients. Insufficient liquid circulation creates vapor blanketing, reducing overall system capacity by 20-40%.

Refrigerant quality at evaporator outlet relates to recirculation ratio:

x_outlet = 1 - (1/n)

Where x_outlet represents vapor quality (mass fraction). A 4:1 ratio produces 0.75 quality (75% vapor, 25% liquid by mass), ensuring adequate tube wetting while minimizing pumping penalties.

## Typical Ratio Ranges

| Application | Recirculation Ratio | Justification |
|-------------|---------------------|---------------|
| Cold storage warehouses | 2:1 to 3:1 | Low heat flux, gravity recirculation |
| Process cooling | 3:1 to 4:1 | Moderate heat flux, reliable wetting |
| Ice rinks | 3:1 to 5:1 | Variable loads, surge capacity |
| Blast freezers | 4:1 to 6:1 | High heat flux, critical wetting |
| Cascade low stage | 4:1 to 6:1 | Low temperature, viscosity effects |
| Ammonia systems | 2:1 to 4:1 | Excellent wetting, lower ratios acceptable |
| Halocarbon systems | 3:1 to 5:1 | Poor wetting, higher ratios required |

## Optimal Ratio Selection Criteria

### Heat Transfer Considerations

Heat transfer coefficient increases logarithmically with recirculation ratio until approximately 4:1, beyond which diminishing returns occur. The relationship follows:

h ≈ h_max [1 - exp(-0.5n)]

Where h represents the average heat transfer coefficient. The improvement from 2:1 to 4:1 ratio yields 35-50% capacity increase, while increasing from 4:1 to 6:1 produces only 10-15% additional gain.

**Critical wetting velocity** determines minimum acceptable ratio. For horizontal tubes:

V_min = 0.25 √[(ρ_liquid - ρ_vapor) g D / ρ_liquid]

Where:
- V_min = minimum liquid velocity to maintain film (m/s)
- D = tube inside diameter (m)
- g = gravitational acceleration (9.81 m/s²)
- ρ = density (kg/m³)

### Energy Optimization

Pumping power increases linearly with recirculation ratio while capacity gains diminish. The optimal ratio balances these competing factors:

COP_effective = Q_evaporator / (W_compressor + W_pump)

For mechanical pump systems, pumping power typically represents 1-3% of compressor power at 3:1 ratio, increasing to 3-7% at 6:1 ratio. Energy analysis should evaluate:

1. Compressor efficiency improvement from reduced superheat
2. Liquid subcooling in separator vessel
3. Pump power consumption
4. Piping pressure drop penalties
5. Heat exchanger approach temperatures

### Refrigerant Charge Requirements

System refrigerant charge increases proportionally with recirculation ratio due to increased liquid inventory in distribution piping and evaporators:

Charge_ratio = Charge_base × [1 + 0.4(n - 1)]

A system with 4:1 ratio requires approximately 2.2 times the refrigerant charge of an equivalent direct expansion system. This consideration significantly impacts:

- Initial refrigerant cost
- Leak impact severity
- Safety classification for high-charge systems
- Refrigerant containment requirements
- Pressure vessel code applicability

## Application-Specific Ratio Selection

### Low Temperature Applications (-40°F to -10°F)

Low saturation temperatures increase refrigerant viscosity and reduce density differential between liquid and vapor phases. These conditions necessitate higher recirculation ratios (4:1 to 6:1) to maintain adequate liquid velocities for continuous tube wetting.

Temperature effects on ammonia properties:

| Temperature (°F) | Liquid Density (lb/ft³) | Vapor Density (lb/ft³) | Viscosity Ratio |
|------------------|-------------------------|------------------------|-----------------|
| 20 | 39.8 | 0.091 | 1.0 |
| 0 | 40.6 | 0.064 | 1.3 |
| -20 | 41.4 | 0.044 | 1.7 |
| -40 | 42.1 | 0.030 | 2.3 |

### High Heat Flux Applications

Blast freezing and quick-chilling applications with heat flux exceeding 4,000 BTU/hr·ft² require minimum 4:1 ratios to prevent nucleate boiling transition to film boiling. Film boiling dramatically reduces heat transfer coefficients from typical values of 400-600 BTU/hr·ft²·°F to 50-100 BTU/hr·ft²·°F.

Critical heat flux relationship:

q"_critical = h_fg × ρ_vapor^0.5 × [σ g (ρ_liquid - ρ_vapor)]^0.25 × 0.18

Where:
- q"_critical = critical heat flux (W/m²)
- h_fg = latent heat of vaporization (J/kg)
- σ = surface tension (N/m)

### Gravity Recirculation Systems

Thermosiphon and gravity-driven systems typically operate at 2:1 to 3:1 ratios due to limited driving head available from liquid column height. The driving pressure differential:

ΔP_available = (ρ_liquid - ρ_vapor) g H

Where H represents vertical separation between separator vessel liquid level and evaporator centerline. Typical installations provide 10-25 feet elevation difference, generating 4-10 psi driving force.

## Recirculation Rate Calculations

Total mass flow rate through evaporators:

ṁ_total = Q_evaporator × n / h_fg

Where:
- Q_evaporator = evaporator cooling capacity (W)
- h_fg = latent heat at evaporating temperature (J/kg)

**Example calculation:**

For 100 TR ammonia system at 20°F evaporating temperature with 4:1 ratio:

- Capacity: 100 TR = 352 kW
- Latent heat: 1,165 kJ/kg at 20°F
- Evaporation rate: 352 / 1,165 = 0.302 kg/s
- Total circulation: 0.302 × 4 = 1.21 kg/s
- Return liquid: 1.21 - 0.302 = 0.908 kg/s

## Pump Selection for Recirculation

Mechanical pump systems must overcome:

1. Static lift from separator to highest evaporator: 5-30 psi
2. Liquid line friction loss: 2-8 psi per 100 ft equivalent length
3. Evaporator pressure drop: 1-5 psi depending on configuration
4. Control valve pressure drop: 5-15 psi
5. Safety factor: 10-20%

Total developed head:

TDH = ΔP_static + ΔP_friction + ΔP_evaporator + ΔP_control + ΔP_safety

Pump power requirement:

W_pump = (ṁ_total × TDH) / (ρ_liquid × η_pump)

Typical centrifugal pump efficiencies range from 60-80% for refrigeration duty pumps in 5-50 HP range.

## Quality at Evaporator Outlet

Vapor quality profoundly affects separator vessel design and downstream piping sizing. Higher recirculation ratios produce lower outlet quality, reducing required vapor-liquid separation area and minimizing liquid carryover risk.

| Recirculation Ratio | Outlet Quality | Liquid Mass Fraction | Separator Design Impact |
|---------------------|----------------|----------------------|-------------------------|
| 2:1 | 0.50 | 50% | Large separator, high carryover risk |
| 3:1 | 0.67 | 33% | Moderate separator, standard design |
| 4:1 | 0.75 | 25% | Compact separator, low carryover risk |
| 5:1 | 0.80 | 20% | Minimal separator, negligible carryover |
| 6:1 | 0.83 | 17% | Oversized circulation, diminishing benefit |

## Distribution System Design

Recirculation ratio selection impacts distribution header sizing. Higher ratios require proportionally larger liquid distribution piping to maintain acceptable velocities (4-8 ft/s for ammonia, 3-6 ft/s for halocarbons) and pressure drop limits (0.5-1.0 psi per 100 ft equivalent length).

Liquid line sizing correlation:

D = 0.408 [(ṁ × L_eq) / (ΔP_allow × ρ)]^0.5 / V^0.5

Where:
- D = inside diameter (inches)
- L_eq = equivalent length including fittings (ft)
- ΔP_allow = allowable pressure drop (psi)
- V = liquid velocity (ft/s)

## Performance Monitoring

Field verification of actual recirculation ratio:

n_actual = [Q_evaporator / (ṁ_return × h_fg)] + 1

Measured return liquid flow rate combined with known evaporator capacity confirms actual operating ratio. Deviations indicate:

- Pump performance degradation
- Distribution system fouling
- Evaporator tube blockage
- Refrigerant charge deficiency
- Separator level control malfunction

## Optimization Strategies

1. **Variable speed pumping**: Modulate recirculation ratio based on actual load, reducing ratio during partial load operation to minimize pumping power
2. **Sectional isolation**: Independently control recirculation to evaporator groups with differing load profiles
3. **Temperature compensation**: Increase ratio at lower evaporating temperatures to compensate for property changes
4. **Superheat monitoring**: Maintain minimum superheat (2-5°F) at separator inlet to verify adequate wetting without excess circulation
5. **Differential pressure tracking**: Monitor evaporator pressure drop as indicator of two-phase flow regime and potential maldistribution

## Economic Considerations

Initial cost increases with recirculation ratio due to:
- Larger pump and motor
- Increased piping diameter
- Higher refrigerant charge
- Larger separator vessel

Operating cost optimization requires lifecycle analysis:

LCC = C_initial + (C_energy × PW) + (C_maintenance × PW)

Where PW represents present worth factor over system design life (typically 20-25 years for industrial refrigeration). Optimal ratio typically falls at 3:1 to 4:1 for most applications when both first cost and operating cost factors are weighted equally.

## Advanced Design Considerations

**Subcooling effects**: Liquid subcooling at evaporator inlet reduces required recirculation ratio by approximately 0.5:1 for each 5°F subcooling. This allows lower ratios while maintaining equivalent heat transfer performance.

**Oil return**: Higher recirculation ratios improve oil return from evaporators to compressor through increased liquid velocities. Ammonia systems require minimum 500 fpm vapor velocity or adequate liquid velocity (>4 ft/s) for oil entrainment.

**Transient response**: Systems with higher recirculation ratios exhibit better stability during load transients due to thermal capacitance of increased liquid inventory, damping rapid pressure and temperature fluctuations.

