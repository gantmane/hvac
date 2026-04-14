---
title: "Temperature & Humidity Control for Web Press Operations"
aliases: ["Temperature & Humidity Control for Web Press Operations"]
description: "Engineering analysis of integrated temperature and relative humidity control systems for web offset printing to prevent web breaks through dimensional stability."
keywords:
  - web press temperature control
  - humidity control printing
  - web tension control
  - dimensional stability paper
  - web break prevention
  - printing press climate control
  - paper moisture equilibrium
  - hygroscopic expansion
weight: 3
---

Precise temperature and relative humidity control in web press operations directly governs paper dimensional stability, web tension uniformity, and production continuity. Paper's hygroscopic nature causes dimensional changes of 0.012-0.022% per percentage point RH change in the cross-grain direction, translating to tension variations that can exceed web break thresholds during humidity swings. Temperature affects both paper moisture equilibrium and ink rheology, with combined environmental deviations creating multiplicative effects on registration accuracy and web handling. High-speed web presses running at 2,000-3,000 fpm require environmental control within ±2°F and ±2% RH to maintain tension within acceptable limits and prevent catastrophic web breaks.

## Hygroscopic Expansion Physics

Paper is a cellulosic material with hydroxyl groups that form hydrogen bonds with water molecules. The sorption isotherm relationship describes moisture content versus ambient conditions.

### Equilibrium Moisture Content

Paper moisture content equilibrates with surrounding air according to:

$$EMC = \frac{1800}{W} \times \frac{K \times h}{(1-K \times h) \times (1 + (C-1) \times K \times h)}$$

Where:
- $EMC$ = Equilibrium moisture content (%)
- $W$ = Fiber saturation point constant (1800 for cellulose)
- $K$ = Sorption constant (0.04-0.08 for paper)
- $C$ = BET constant (5-15 for paper)
- $h$ = Relative humidity (decimal)

**Simplified linear approximation** for operating range 40-60% RH:

$$EMC(\%) \approx 4 + 0.10 \times RH(\%)$$

At 50% RH, paper moisture content is approximately 9%.

### Dimensional Change Relationship

Paper dimensions vary with moisture content through hygroscopic expansion:

$$\frac{\Delta L}{L_0} = \alpha_{EMC} \times \Delta EMC$$

Where:
- $\Delta L/L_0$ = Fractional length change
- $\alpha_{EMC}$ = Hygroscopic expansion coefficient (0.6-1.0% per %MC)
- $\Delta EMC$ = Moisture content change (%)

**Combined relationship** linking dimension directly to relative humidity:

$$\frac{\Delta L}{L_0} = \alpha_{RH} \times \Delta RH$$

Where effective coefficient:

$$\alpha_{RH} = \alpha_{EMC} \times \frac{dEMC}{dRH} \approx 0.012-0.022\% \text{ per }\%RH$$

**Critical observation:** Cross-grain expansion is 3-4 times greater than grain-direction expansion due to fiber orientation. A 40-inch wide web experiencing 5% RH change expands:

$$\Delta L = 40 \text{ in} \times 0.018\%/\%RH \times 5\%RH = 0.036 \text{ in}$$

This 0.036-inch dimensional change produces measurable tension variation in a running web.

## Web Tension Mechanics

Web tension must remain within narrow limits to prevent breaks (excessive tension) or wrinkles (insufficient tension). Environmental changes alter tension through dimensional effects.

### Tension-Strain Relationship

Paper web behaves as an elastic material under tension:

$$\sigma = E \times \epsilon$$

Where:
- $\sigma$ = Tensile stress (psi)
- $E$ = Elastic modulus (200,000-400,000 psi for paper cross-grain)
- $\epsilon$ = Strain (dimensionless)

For a web under constant length constraint:

$$T = \sigma \times A = E \times \epsilon \times w \times t$$

Where:
- $T$ = Web tension (lbf)
- $w$ = Web width (in)
- $t$ = Paper thickness (in)
- $A$ = Cross-sectional area (in²)

### Humidity-Induced Tension Change

When humidity changes while web length remains fixed (between press units), dimensional change creates strain:

$$\epsilon_{hygro} = \alpha_{RH} \times \Delta RH$$

This hygroscopic strain produces tension change:

$$\Delta T = E \times \alpha_{RH} \times \Delta RH \times w \times t$$

**Example calculation:**

Publication grade paper, 40-inch wide web:
- $E$ = 300,000 psi (cross-grain)
- $\alpha_{RH}$ = 0.018% per %RH = 0.00018 per %RH
- $w$ = 40 in
- $t$ = 0.003 in (typical newsprint)
- $\Delta RH$ = 5% (uncontrolled fluctuation)

$$\Delta T = 300,000 \times 0.00018 \times 5 \times 40 \times 0.003 = 32.4 \text{ lbf}$$

**Operating context:** Typical web tension is 3-5 plf (pounds per linear foot of width), or 10-16.7 lbf for a 40-inch web. A 32.4 lbf change represents 200-300% variation—far exceeding acceptable limits and causing immediate web break.

### Temperature Effects on Tension

Temperature influences tension through two mechanisms:

**1. Thermal expansion of paper:**

$$\alpha_{T} = 5-8 \times 10^{-6} \text{ per }°F$$

**2. Moisture content shift (paper EMC decreases with temperature at constant RH):**

$$\frac{dEMC}{dT} \approx -0.03\% \text{ per }°F$$

Combined effect per °F temperature rise:

$$\frac{\Delta L}{L_0} = \alpha_{T} \times \Delta T - \alpha_{EMC} \times \frac{dEMC}{dT} \times \Delta T$$

Second term (moisture effect) dominates: 10°F increase at constant 50% RH reduces moisture content by 0.3%, shrinking paper by 0.18-0.30% (600-1000 times greater than thermal expansion).

### Combined Temperature-Humidity Model

Total dimensional change from simultaneous temperature and humidity variation:

$$\frac{\Delta L}{L_0} = \alpha_{RH} \times \Delta RH + \alpha_{T,eff} \times \Delta T$$

Where effective temperature coefficient:

$$\alpha_{T,eff} = \alpha_{T} - \alpha_{EMC} \times \frac{dEMC}{dT} \approx -12 \times 10^{-6} \text{ per }°F$$

Negative sign indicates paper shrinks with temperature increase at constant RH.

**Resulting tension change:**

$$\Delta T_{web} = E \times w \times t \times \left(\alpha_{RH} \times \Delta RH + \alpha_{T,eff} \times \Delta T\right)$$

**Design implication:** Humidity effects dominate (18:1 ratio), but temperature control remains critical due to ink rheology and dryer operation requirements.

## Control Tolerances for Web Break Prevention

### Failure Criteria

Paper fails in tension when stress exceeds ultimate tensile strength:

$$\sigma_{break} = \frac{T_{break}}{w \times t}$$

Typical values:
- Newsprint: 3,000-5,000 psi (cross-grain)
- Coated offset: 4,000-7,000 psi
- Label stock: 5,000-8,000 psi

**Operating tension** is typically 20-30% of break strength for safety margin.

### Environmental Tolerance Derivation

Maximum allowable tension variation without exceeding break threshold:

$$\Delta T_{max} = (SF - 1) \times T_{operating}$$

Where $SF$ = safety factor (1.5-2.0 typical).

For $T_{operating}$ = 25% of break strength and $SF$ = 1.5:

$$\Delta T_{max} = 0.5 \times 0.25 \times T_{break} = 0.125 \times T_{break}$$

**Converting to humidity tolerance:**

$$\Delta RH_{max} = \frac{\Delta T_{max}}{E \times \alpha_{RH} \times w \times t}$$

**Example (40-in newsprint web):**

- $T_{break}$ = 3,500 psi × 40 in × 0.003 in = 420 lbf
- $\Delta T_{max}$ = 0.125 × 420 = 52.5 lbf
- From previous equation: $\Delta T/\Delta RH$ = 6.5 lbf per %RH

$$\Delta RH_{max} = \frac{52.5}{6.5} = 8\%RH$$

**Conservative design standard:** Maintain ±2-3% RH control for 2.5-4.0 safety margin.

### Temperature Tolerance

Applying same methodology to temperature:

$$\Delta T_{max} = \frac{\Delta T_{web,max}}{E \times |\alpha_{T,eff}| \times w \times t}$$

For the 40-inch newsprint example:

$$\Delta T_{max} = \frac{52.5}{300,000 \times 12 \times 10^{-6} \times 40 \times 0.003} = 121°F$$

**Conclusion:** Direct thermal expansion effects are minimal. Temperature control requirement of ±2°F is driven by:
1. Ink viscosity/tack consistency
2. Maintaining stable moisture equilibrium
3. Preventing thermal gradients across web width

## HVAC System Design Requirements

### Control Parameters

**Space conditions:**

| Parameter | Setpoint | Tolerance | Consequence of Deviation |
|-----------|----------|-----------|-------------------------|
| Dry-bulb temperature | 72-75°F | ±2°F | Ink consistency, moisture equilibrium |
| Relative humidity | 45-50% | ±2% RH | Dimensional stability, web tension |
| Dewpoint temperature | 50-54°F | ±2°F | Moisture content control |
| Air velocity (at web) | 30-50 fpm | ±10 fpm | Minimal web flutter, heat removal |

### Psychrometric Control Strategy

**Dewpoint control** provides superior performance to relative humidity control:

$$RH = \frac{p_{vapor}}{p_{sat}(T_{db})}$$

At constant dewpoint, RH varies inversely with dry-bulb temperature. A ±2°F temperature swing at 50°F dewpoint causes ±7% RH variation at 70°F dry-bulb.

**Preferred approach:** Control dewpoint to ±1-1.5°F through:
1. Dewpoint sensor in return air
2. Chilled water coil modulating to dewpoint setpoint
3. Separate sensible cooling/heating for temperature control
4. Decoupled latent and sensible control loops

### Capacity Requirements

**Sensible heat loads:**

| Source | Typical Magnitude | Notes |
|--------|------------------|-------|
| Dryer radiant heat | 150,000-300,000 Btu/hr | Per press unit, varies with speed |
| Press drive motors | 200,000-400,000 Btu/hr | Based on 50-100 HP total |
| Lighting | 30,000-60,000 Btu/hr | High illumination required |
| Personnel | 50,000-100,000 Btu/hr | 20-40 operators/support staff |
| External gains | Variable | Depends on building envelope |

**Total sensible cooling:** 500,000-900,000 Btu/hr typical for 4-6 unit press installation (40-75 tons).

**Latent loads:**

Winter humidification dominates in cold climates:

$$Q_{latent,winter} = \frac{CFM \times \rho \times \Delta W \times h_{fg}}{60}$$

For 50,000 CFM makeup air, 0°F outdoor to 72°F/50% RH:
- $\Delta W$ = 0.0078 - 0.0001 = 0.0077 lb/lb
- Latent load = 50,000 × 0.075 × 0.0077 × 1050 / 60 = 506 MBH

Requires approximately 500 lb/hr steam capacity.

Summer dehumidification in humid climates:

For 50,000 CFM, 90°F/70% RH outdoor to 72°F/50% RH:
- $\Delta W$ = 0.0164 - 0.0078 = 0.0086 lb/lb
- Latent load = 50,000 × 0.075 × 0.0086 × 1050 / 60 = 565 MBH (47 tons)

### Air Distribution Design

**Low-velocity displacement strategy:**

Supply conditioned air at floor level, 50-65°F, 200-400 fpm initial velocity:
- Supply diffusers: Perforated duct or floor-mounted displacement outlets
- Spacing: 20-30 feet along press line
- Air pattern: Upward displacement, capturing heat at ceiling
- Return location: High sidewall or ceiling (stratification benefit)

**Advantages:**
1. Minimal web disturbance (< 50 fpm in web path)
2. Excellent temperature uniformity (stratification removes heat)
3. Reduced drafts on operators
4. Energy efficient (supply temperature 8-12°F below space setpoint)

**Design airflow:**

$$CFM_{supply} = \frac{Q_{sensible}}{1.08 \times (T_{space} - T_{supply})}$$

For 600,000 Btu/hr sensible load, 72°F space, 58°F supply:

$$CFM = \frac{600,000}{1.08 \times 14} = 39,700 \text{ CFM}$$

Use 40,000-45,000 CFM to provide margin.

## Integrated Control Systems

### Multi-Zone Control Architecture

Large web press facilities require zone-based control:

**Zone 1: Paper storage/acclimation**
- Setpoint: 72°F, 50% RH
- Tolerance: ±3°F, ±3% RH (less critical than press area)
- System: Separate AHU with humidification

**Zone 2: Press room**
- Setpoint: 73°F, 48% RH
- Tolerance: ±2°F, ±2% RH (critical control)
- System: Dedicated AHU with dewpoint control, DDC integration

**Zone 3: Dryer exhaust/makeup air**
- Makeup air volume: Matches exhaust (12,000-15,000 CFM per press)
- Heating: Direct-fired makeup air unit (80-85% efficiency)
- Cooling: Evaporative or DX cooling
- Integration: Volume tracking with exhaust fans

### Control Sequence

```
PRESS ROOM HVAC CONTROL LOGIC

1. PRIMARY LOOP - Dewpoint Control
   - Measure: Return air dewpoint (DP_ra)
   - Setpoint: 51°F dewpoint
   - Control: Modulate CHW valve position (0-100%)

   IF DP_ra > DP_setpoint + 1°F THEN
      Increase CHW valve position (more cooling/dehumidification)
   ELSE IF DP_ra < DP_setpoint - 1°F THEN
      Decrease CHW valve position
      IF CHW valve < 10% AND DP_ra < DP_setpoint - 2°F THEN
         Enable humidifier (steam injection)
      END IF
   END IF

2. SECONDARY LOOP - Temperature Control
   - Measure: Space dry-bulb temperature (T_db)
   - Setpoint: 73°F
   - Control: Modulate reheat coil or economizer position

   IF T_db > T_setpoint + 1°F THEN
      Increase economizer dampers (if OA temp < 60°F)
      OR increase CHW valve (if dewpoint control allows)
   ELSE IF T_db < T_setpoint - 1°F THEN
      Increase reheat coil output
   END IF

3. TERTIARY LOOP - Pressurization
   - Measure: Space static pressure (P_space)
   - Setpoint: +0.05" w.c. relative to adjacent areas
   - Control: Modulate return/exhaust damper position

   Maintain supply CFM = exhaust CFM + pressurization CFM

4. SAFETY INTERLOCKS
   - IF dewpoint > 60°F (condensation risk) THEN
      Alarm + maximum cooling
   - IF temperature > 80°F OR < 65°F THEN
      Alarm + notify operators
   - IF humidity > 60% OR < 35% THEN
      Alarm + web break warning
```

### Sensor Placement

**Critical sensor locations:**

1. **Return air:** Dewpoint transmitter (±1°F accuracy), temperature sensor (±0.5°F accuracy)
2. **Supply air:** Dewpoint, temperature, flow station
3. **Space reference:** Multiple temperature/RH sensors at web path height (4-6 feet above floor)
4. **Outdoor air:** Temperature, humidity for economizer control and enthalpy calculation

**Sensor spacing:** One temperature/humidity monitoring point per 2,000-3,000 ft² press area to detect spatial variations.

## Control Strategies for Different Web Materials

Environmental requirements vary significantly based on substrate properties.

### Material-Specific Requirements

| Web Material | Temperature | RH Control | Primary Concern | Special Considerations |
|--------------|-------------|------------|----------------|----------------------|
| Newsprint | 72-75°F, ±2°F | 45-50% RH, ±2% | Static control, brittleness | High recycled content increases hygroscopic response |
| Coated gloss paper | 70-73°F, ±1.5°F | 48-52% RH, ±1.5% | Registration accuracy | Low hygroscopic coefficient, tighter tolerance possible |
| Uncoated offset | 72-75°F, ±2°F | 45-50% RH, ±3% | Dimensional stability | Moderate hygroscopic expansion, standard control |
| Label stock | 73-76°F, ±2°F | 40-45% RH, ±2% | Curl control, adhesive performance | Lower RH prevents curl, adhesive optimization |
| Film substrates (polyester, polypropylene) | 70-75°F, ±3°F | Not critical | Static control, heat dissipation | Non-hygroscopic, static elimination primary concern |
| Tissue paper | 72-75°F, ±1.5°F | 35-40% RH, ±2% | Strength retention | Very hygroscopic, excessive moisture reduces strength |

### Control Strategy Selection

**Strategy A: Constant setpoint (tight tolerance)**
- Application: High-quality commercial, packaging
- Setpoint: 73°F, 48% RH year-round
- Tolerance: ±1.5°F, ±1.5% RH
- Equipment: Dewpoint control, DDC, high-efficiency humidification/dehumidification
- Energy penalty: 15-25% higher than Strategy B
- Benefit: Maximum registration accuracy, minimal web breaks

**Strategy B: Seasonal setpoint adjustment**
- Application: Publication printing, newspapers
- Winter: 72°F, 45% RH (±2°F, ±2% RH)
- Summer: 75°F, 50% RH (±2°F, ±2% RH)
- Equipment: Standard AHU with humidification and cooling-based dehumidification
- Energy savings: Reduced humidification (winter) and dehumidification (summer) loads
- Tradeoff: Transition period adjustment (1-2 days for paper acclimation)

**Strategy C: Process-driven modulation**
- Application: Flexible facilities running multiple substrates
- Control: Adjust setpoints based on material being printed (database lookup)
- Implementation: Automated setpoint changes synchronized with job changeover
- Requirement: 2-4 hour acclimation time before critical registration jobs
- Benefit: Optimized conditions for each substrate type

**Strategy D: Film substrate (non-hygroscopic)**
- Temperature: 70-75°F, ±3°F (less critical)
- Humidity: 40-50% RH, ±5% RH (for static control only)
- Primary controls: Active static elimination (ionizing bars), web tension control via dancer rolls
- Reduced HVAC precision requirements, lower capital and operating costs

## Monitoring and Verification

### Real-Time Performance Metrics

**Key performance indicators:**

1. **Environmental stability index:**

$$ESI = \sqrt{(\frac{\Delta T}{\Delta T_{max}})^2 + (\frac{\Delta RH}{\Delta RH_{max}})^2}$$

Where $\Delta T$, $\Delta RH$ are measured deviations from setpoint. Target ESI < 0.5 for stable operation.

2. **Web break frequency:**
- Target: < 1 break per 1,000,000 linear feet
- Monitor correlation with environmental excursions
- Trend analysis: Breaks vs. time of day, season, weather events

3. **Tension variation coefficient:**

$$CV_{tension} = \frac{\sigma_{tension}}{\bar{T}_{tension}} \times 100\%$$

Target CV < 5% for quality production. Continuous tension monitoring at multiple web spans correlates with environmental control effectiveness.

### Diagnostic Tools

**Psychrometric tracking:**

Plot space conditions on psychrometric chart over 24-hour period. Ideal operation shows tight clustering around setpoint. Deviations indicate:
- Horizontal drift: Sensible heat imbalance (temperature control issue)
- Vertical drift: Latent heat imbalance (humidity control issue)
- Diagonal drift: Combined sensible/latent imbalance or outdoor air variation

**Spatial mapping:**

Periodic temperature/humidity surveys across press area using portable dataloggers:
- Grid pattern: 10-15 foot spacing
- Duration: 24-48 hours
- Analysis: Identify hot spots, humidity gradients, air distribution deficiencies

## Integrated Temperature and RH Control System

```mermaid
graph TD
    A[Outdoor Air<br/>Variable T & RH] --> B[Makeup Air Unit<br/>Heating/Cooling]
    B --> C[Supply Air<br/>Conditioned]
    C --> D[Floor-Level Distribution<br/>Low Velocity Discharge]
    D --> E[Press Room Space<br/>73°F, 48% RH Setpoint]

    E --> F[Web Path<br/>Critical Zone]
    F --> G[Dimensional Stability<br/>±0.015% tolerance]

    E --> H[Return Air<br/>Ceiling Level]
    H --> I[Return Air Sensors<br/>Dewpoint & Temperature]

    I --> J{Dewpoint Control<br/>Primary Loop}
    J -->|DP > Setpoint| K[Increase Cooling<br/>CHW Valve Opens]
    J -->|DP < Setpoint| L[Decrease Cooling<br/>Enable Humidifier]

    K --> M[Chilled Water Coil<br/>42-45°F Supply]
    L --> N[Steam Humidifier<br/>Duct Injection]

    M --> C
    N --> C

    I --> O{Temperature Control<br/>Secondary Loop}
    O -->|T > Setpoint| P[Increase Cooling<br/>or Economizer]
    O -->|T < Setpoint| Q[Reheat Coil<br/>Hot Water/Steam]

    P --> C
    Q --> C

    E --> R[Dryer Exhaust<br/>12,000-15,000 CFM]
    R --> S[Thermal Oxidizer<br/>VOC Destruction]
    S --> T[Stack Discharge]

    R -.->|Volume Tracking| B

    U[Building Automation<br/>DDC System] -.->|Control Signals| J
    U -.->|Control Signals| O
    U -.->|Monitor| F

    V[Space Pressure<br/>+0.05" w.c.] -.->|Tertiary Loop| U

    style F fill:#ffcccc
    style G fill:#ffcccc
    style J fill:#cce5ff
    style O fill:#cce5ff
    style E fill:#ffffcc
```

---

Temperature and humidity control systems for web press operations require integrated management of dewpoint, dry-bulb temperature, and pressurization to maintain paper dimensional stability within tolerances that prevent web breaks. The hygroscopic expansion coefficient of 0.012-0.022% per %RH change necessitates ±2% RH control to limit tension variations below break thresholds, while temperature control of ±2°F ensures ink rheology consistency and stable moisture equilibrium. Dewpoint-based control architectures decouple latent and sensible loads, providing superior performance compared to traditional RH control, with proper sensor placement and multi-loop control sequences enabling the environmental stability required for high-speed production exceeding 2,000 fpm web speeds.
