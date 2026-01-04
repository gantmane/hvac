---
title: "Ventilation Rates and Indoor Air Quality Standards: ASHRAE 62.1 & 62.2 Design Guide"
description: "Comprehensive technical analysis of ventilation rate calculations, ASHRAE 62.1 commercial and 62.2 residential standards, outdoor airflow procedures, CO2-based demand control ventilation, breathing zone analysis, and contaminant dilution equations with practical examples."
keywords: "ventilation rates, ASHRAE 62.1, ASHRAE 62.2, indoor air quality, outdoor air ventilation, breathing zone outdoor airflow, ventilation effectiveness, CO2 demand control ventilation, air change effectiveness, contaminant dilution, energy recovery ventilator, IAQ procedure"
categories: ["Ventilation", "Indoor Air Quality", "HVAC Design"]
tags: ["ASHRAE 62.1", "ASHRAE 62.2", "Ventilation Design", "Outdoor Air", "IAQ", "DCV", "Breathing Zone", "Contaminant Control"]
author: "Evgeniy Gantman"
date: 2026-01-04
draft: false
---

## Introduction to Ventilation Rate Standards

Ventilation rate design represents the fundamental interface between building occupancy, contaminant generation, and outdoor air delivery. ASHRAE Standards 62.1 and 62.2 establish quantitative requirements for commercial and residential buildings, converting physiological oxygen demand and contaminant dilution needs into engineered airflow specifications. The physics involves mass balance equations, concentration gradients, and air distribution effectiveness factors that determine the minimum outdoor air supply necessary for acceptable indoor air quality.

The design process requires understanding two distinct calculation procedures: the Ventilation Rate Procedure (prescriptive airflow rates based on space type and occupancy) and the Indoor Air Quality Procedure (performance-based approach using contaminant concentration limits). Each method produces different system requirements with specific applications and limitations.

This analysis covers the complete mathematical framework for ventilation design: ASHRAE 62.1 commercial building requirements, ASHRAE 62.2 residential standards, breathing zone calculations, multiple space equations, ventilation effectiveness, CO2-based demand control ventilation, air change effectiveness, energy recovery integration, and contaminant dilution physics. The objective is precise outdoor air system sizing based on first-principles mass transfer analysis.

## ASHRAE 62.1 Commercial Building Ventilation Requirements

### Ventilation Rate Procedure Foundation

ASHRAE 62.1 establishes minimum ventilation rates for commercial buildings through the Ventilation Rate Procedure. The standard recognizes two distinct contaminant sources: people-related emissions (bioeffluents, respiratory products, body odors) and building-related emissions (materials, furnishings, cleaning products, processes). This dual-source recognition leads to the fundamental outdoor air equation.

The breathing zone outdoor airflow for a single zone is calculated as:

{{< formula display="true" >}}
$$V_{bz} = R_p \cdot P_z + R_a \cdot A_z$$
{{< /formula >}}

Where:
- $V_{bz}$ = breathing zone outdoor airflow (CFM)
- $R_p$ = outdoor airflow rate required per person (CFM/person)
- $P_z$ = zone population (occupant design value)
- $R_a$ = outdoor airflow rate required per unit area (CFM/ft²)
- $A_z$ = zone floor area (ft²)

The separation into people and area components reflects different contaminant generation mechanisms. People-based rates address metabolic CO2 production (approximately 0.3 L/min per person at sedentary activity), moisture generation (50-200 g/hr per person depending on activity), and bioeffluent release. Area-based rates dilute emissions from building materials, which follow surface area relationships rather than occupancy density.

### Standard Ventilation Rates by Space Type

ASHRAE 62.1 Table 6.2.2.1 specifies outdoor air requirements for different occupancy categories. The values derive from empirical studies correlating subjective air quality acceptability with ventilation rates under typical contaminant loading conditions.

{{< table >}}
| Space Type | People Outdoor Air ($R_p$) | Area Outdoor Air ($R_a$) | Default Occupant Density | Air Class |
|------------|---------------------------|-------------------------|-------------------------|-----------|
| Office Space | 5 CFM/person | 0.06 CFM/ft² | 5 people/1000 ft² | 1 |
| Conference Room | 5 CFM/person | 0.06 CFM/ft² | 50 people/1000 ft² | 1 |
| Classroom (ages 9+) | 10 CFM/person | 0.12 CFM/ft² | 35 people/1000 ft² | 1 |
| Retail Sales | 7.5 CFM/person | 0.12 CFM/ft² | 15 people/1000 ft² | 1 |
| Gym/Exercise Room | 20 CFM/person | 0.06 CFM/ft² | 40 people/1000 ft² | 1 |
| Restaurant Dining | 7.5 CFM/person | 0.18 CFM/ft² | 70 people/1000 ft² | 2 |
| Hospital Patient Room | 25 CFM/person | 0.06 CFM/ft² | 10 people/1000 ft² | 1 |
| Pharmacy | 5 CFM/person | 0.18 CFM/ft² | 20 people/1000 ft² | 1 |
| Laboratory | 10 CFM/person | 0.18 CFM/ft² | 25 people/1000 ft² | 1 |
| Corridor | 0 CFM/person | 0.06 CFM/ft² | 0 people/1000 ft² | 1 |
{{< /table >}}

The Air Class designation indicates outdoor air quality requirements. Class 1 assumes low outdoor contaminant levels, while Class 2-4 require increasingly higher ventilation effectiveness due to outdoor pollution. Most urban applications use Class 1 or 2 assumptions.

Higher $R_p$ values for gymnasiums (20 CFM/person) and patient rooms (25 CFM/person) reflect elevated metabolic rates and associated CO2/bioeffluent generation. The gymnasium value corresponds to moderate exercise intensity where metabolic CO2 production increases by factor of 3-4 compared to sedentary conditions. Hospital patient rooms require higher rates due to potential infectious disease transmission and medication off-gassing.

### Multiple Zone System Calculations

Most commercial HVAC systems serve multiple zones with varying occupancy densities and ventilation requirements. The system outdoor air intake must account for simultaneous diversity and ensure each zone receives adequate outdoor air despite different supply air fractions.

The uncorrected outdoor air intake is:

{{< formula display="true" >}}
$$V_{ou} = \sum_{all\ zones} R_p \cdot P_z + \sum_{all\ zones} R_a \cdot A_z$$
{{< /formula >}}

This represents simple summation of all zone requirements. However, zones with high ventilation needs may have lower supply air fractions (outdoor air percentage in supply air), while zones with low requirements have higher fractions. The system diversity factor accounts for this distribution challenge.

The zone air distribution effectiveness $E_z$ modifies the breathing zone requirement to account for imperfect mixing. For most ceiling supply/ceiling return systems: $E_z = 1.0$. For displacement ventilation or underfloor air distribution: $E_z = 1.2$ (credit for better delivery efficiency). For heated air supplied near floor: $E_z = 0.8$ (penalty for thermal stratification reducing effectiveness).

The zone outdoor air flow becomes:

{{< formula display="true" >}}
$$V_{oz} = \frac{V_{bz}}{E_z}$$
{{< /formula >}}

The primary outdoor air fraction for each zone is:

{{< formula display="true" >}}
$$Z_p = \frac{V_{oz}}{V_{dz}}$$
{{< /formula >}}

Where $V_{dz}$ is the zone primary (discharge) airflow from the air handler. This fraction indicates what percentage of the supply air must be outdoor air to meet the zone requirement.

The system ventilation efficiency $E_v$ accounts for the worst-case zone:

{{< formula display="true" >}}
$$E_v = \frac{1 + X_s - Z_d}{1 + X_s - Z_{d,max}}$$
{{< /formula >}}

Where:
- $X_s$ = uncorrected system outdoor air fraction = $V_{ou}/V_{ps}$
- $V_{ps}$ = system primary air (sum of all zone discharge airflows)
- $Z_d$ = outdoor air fraction at the ventilation zone (varies by system type)
- $Z_{d,max}$ = maximum zone outdoor air fraction

For single-zone systems: $E_v = 1.0$. For multiple zone systems with recirculation: $E_v < 1.0$, requiring higher outdoor air intake to compensate for zones receiving diluted outdoor air.

The final system outdoor air intake is:

{{< formula display="true" >}}
$$V_{ot} = \frac{V_{ou}}{E_v}$$
{{< /formula >}}

This value determines the outdoor air damper position and minimum outdoor air flow control setpoint. The multiple zone equations ensure that even the worst-served zone receives adequate outdoor air despite system mixing and distribution losses.

### System Ventilation Efficiency by Configuration

Different HVAC system types exhibit different ventilation distribution characteristics:

**Single-Zone Systems:** $E_v = 1.0$ (all supply air has same outdoor air fraction)

**Multiple-Zone VAV with Central Return:** $E_v$ calculated from maximum zone $Z_p$ ratio. Typical range: 0.6-0.8 for systems with diverse zone loads.

**Multiple-Zone VAV with Transfer Air:** More complex calculation accounting for air transferred between zones before returning to air handler. Transfer air from high-ventilation zones can serve downstream zones, improving efficiency.

**Multiple-Zone Constant Volume with Central Return:** Similar to VAV but with less variability in zone airflows. Typical $E_v$: 0.7-0.9.

The physical interpretation: $E_v = 0.7$ means the system must supply 43% more outdoor air than the simple sum of zone requirements to ensure the worst-served zone receives adequate outdoor air. This occurs because the worst-case zone receives the lowest outdoor air fraction (highest recirculated air percentage), requiring the overall system outdoor air intake to increase until that critical zone meets its requirement.

## ASHRAE 62.2 Residential Ventilation Standards

### Residential Ventilation Requirements

ASHRAE 62.2 addresses residential buildings (single-family homes, multifamily units, manufactured housing) where occupancy patterns, contaminant sources, and ventilation strategies differ fundamentally from commercial applications. The standard recognizes continuous low-level ventilation requirements plus intermittent mechanical exhaust for point-source contaminant control.

The whole-house ventilation rate is:

{{< formula display="true" >}}
$$Q_{tot} = 0.03 \cdot A_{floor} + 7.5 \cdot (N_{br} + 1)$$
{{< /formula >}}

Where:
- $Q_{tot}$ = total required ventilation rate (CFM)
- $A_{floor}$ = conditioned floor area (ft²)
- $N_{br}$ = number of bedrooms

The equation structure reflects area-based emissions (0.03 CFM/ft² accounts for building materials, furnishings, cleaning products) and occupancy-based emissions (7.5 CFM per presumed occupant, with bedroom count plus one as occupancy estimator).

For a 2,000 ft² home with 3 bedrooms:

{{< formula display="true" >}}
$$Q_{tot} = 0.03 \cdot 2000 + 7.5 \cdot (3 + 1) = 60 + 30 = 90\ \text{CFM}$$
{{< /formula >}}

This represents continuous equivalent ventilation. The system can operate continuously at 90 CFM or intermittently at higher flow rates with adjusted runtime to deliver equivalent air change.

### Infiltration Credit and Effective Ventilation

Natural infiltration through building envelope leakage provides outdoor air exchange, reducing mechanical ventilation requirements. The standard allows infiltration credit based on blower door testing results.

The effective annual average infiltration rate is:

{{< formula display="true" >}}
$$Q_{inf} = \frac{NL \cdot ACH_{50} \cdot V}{60}$$
{{< /formula >}}

Where:
- $Q_{inf}$ = effective infiltration rate (CFM)
- $NL$ = normalized leakage (weather/shielding factor)
- $ACH_{50}$ = air changes per hour at 50 Pa from blower door test
- $V$ = conditioned volume (ft³)

The normalized leakage factor ranges from 0.5 (very tight construction in mild climate) to 1.5 (leaky construction in severe climate). Typical value: NL = 1.0 for moderate construction in typical climate.

For ACH50 = 5.0 (moderately tight home), volume = 16,000 ft³, NL = 1.0:

{{< formula display="true" >}}
$$Q_{inf} = \frac{1.0 \cdot 5.0 \cdot 16000}{60} = 133\ \text{CFM}$$
{{< /formula >}}

The infiltration credit means mechanical ventilation may not be required if infiltration exceeds the total requirement. However, infiltration is uncontrolled, unfiltered, and climate-dependent, making dedicated mechanical ventilation preferable for consistent indoor air quality.

The adjusted mechanical ventilation requirement is:

{{< formula display="true" >}}
$$Q_{fan} = Q_{tot} - Q_{inf} \cdot \phi$$
{{< /formula >}}

Where $\phi$ is the infiltration credit factor, typically 1.0 for balanced systems, reduced for unbalanced systems due to interaction between mechanical ventilation and infiltration patterns.

### Local Exhaust Requirements

ASHRAE 62.2 mandates local exhaust for kitchens and bathrooms to address high-intensity point-source contaminants (cooking emissions, moisture, odors) that whole-house ventilation cannot adequately dilute.

**Kitchen Exhaust:**
- 100 CFM intermittent exhaust, vented outdoors
- Or 5 ACH continuous exhaust rate based on kitchen volume

**Bathroom Exhaust:**
- 50 CFM intermittent exhaust for full bath
- 20 CFM intermittent for half bath (toilet only)
- Or continuous exhaust at 20 CFM (full bath) / 10 CFM (half bath)

Recirculating range hoods without outdoor discharge do not satisfy the requirement. The physics: cooking generates particulates (PM2.5, PM10), volatile organic compounds, aldehydes, nitrogen dioxide (gas combustion), and moisture at rates far exceeding whole-house dilution capacity. Spot exhaust captures concentrated plumes at the source before distribution throughout the home.

Bathroom exhaust addresses moisture control (shower generates 0.5-2 lbs water vapor per 10-minute shower), odor control, and potential chemical off-gassing from personal care products. Continuous low-flow exhaust (20 CFM) provides equivalent dilution to intermittent high-flow (50 CFM) operation with better moisture control between occupancy events.

### Ventilation System Types

**Exhaust-Only Systems:** Continuous exhaust fan (typically bathroom location) creates negative pressure, inducing infiltration throughout envelope. Simple, low cost, but uncontrolled outdoor air entry points and no filtration. Suitable for mild climates with low outdoor pollution.

**Supply-Only Systems:** Continuous supply fan delivers filtered outdoor air, creating positive pressure and forcing exfiltration through envelope. Better filtration control, reduced outdoor pollutant entry, but moisture can accumulate in wall cavities in cold climates.

**Balanced Systems (HRV/ERV):** Equal supply and exhaust flows maintain neutral building pressure. Heat Recovery Ventilator (HRV) transfers sensible heat between airstreams. Energy Recovery Ventilator (ERV) transfers both sensible and latent heat (moisture). Higher cost, superior energy performance and air quality control.

The balanced system outdoor air effectiveness is 1.0 (full credit for rated flow). Exhaust-only and supply-only systems have effectiveness < 1.0 due to interaction with infiltration, requiring higher mechanical flow rates to achieve equivalent ventilation.

## Indoor Air Quality Procedure

### Performance-Based IAQ Design

The Indoor Air Quality Procedure represents an alternative to the prescriptive Ventilation Rate Procedure. Rather than specifying airflow rates by occupancy category, the IAQ Procedure sets performance targets: maintain specific contaminant concentrations below acceptable limits while allowing any ventilation rate that achieves this objective.

The approach requires:
1. Identify all significant contaminants and generation rates
2. Establish acceptable concentration limits for each contaminant
3. Calculate ventilation rates necessary to maintain limits
4. Implement continuous monitoring to verify performance

The governing equation is the steady-state mass balance for each contaminant:

{{< formula display="true" >}}
$$Q \cdot (C_{out} - C_{in}) + G - R \cdot V \cdot C_{in} = 0$$
{{< /formula >}}

Where:
- $Q$ = outdoor air ventilation rate (CFM)
- $C_{out}$ = outdoor contaminant concentration
- $C_{in}$ = indoor contaminant concentration (must stay below limit)
- $G$ = contaminant generation rate (mass/time)
- $R$ = contaminant removal rate by filtration or reactions (1/time)
- $V$ = space volume

Solving for ventilation rate:

{{< formula display="true" >}}
$$Q = \frac{G - R \cdot V \cdot C_{in}}{C_{in} - C_{out}}$$
{{< /formula >}}

For contaminants with negligible outdoor concentration and no removal mechanism:

{{< formula display="true" >}}
$$Q = \frac{G}{C_{in,limit}}$$
{{< /formula >}}

This represents pure dilution ventilation: the generation rate divided by acceptable concentration determines required outdoor air flow.

### Contaminant-Specific Analysis

**Carbon Dioxide (CO2):** Human respiration generates approximately 0.3 L/min CO2 per person at sedentary activity (increases to 1-2 L/min during exercise). Outdoor CO2 concentration is approximately 420 ppm (rising due to atmospheric accumulation). Acceptable indoor limit: 1000-1200 ppm above outdoor (1420-1620 ppm absolute).

For 50 occupants in a conference room:

{{< formula display="true" >}}
$$G_{CO_2} = 50 \times 0.3\ \text{L/min} = 15\ \text{L/min} = 0.53\ \text{CFM}$$
{{< /formula >}}

Converting to mass rate (CO2 density ≈ 1.98 g/L):

{{< formula display="true" >}}
$$G_{CO_2} = 15\ \text{L/min} \times 1.98\ \text{g/L} = 29.7\ \text{g/min}$$
{{< /formula >}}

For concentration limit 1000 ppm above outdoor (approximately 1800 mg/m³ difference):

{{< formula display="true" >}}
$$Q = \frac{29.7\ \text{g/min} \times 1000\ \text{mg/g}}{1800\ \text{mg/m}^3} \times 35.3\ \text{ft}^3/\text{m}^3 = 581\ \text{CFM}$$
{{< /formula >}}

This aligns with ASHRAE 62.1 prescriptive rate: 50 people × 5 CFM/person + area component ≈ 250-300 CFM base rate. The prescriptive rates derive from IAQ Procedure calculations using typical contaminant generation assumptions.

**Volatile Organic Compounds (VOCs):** Building materials, furnishings, cleaning products, and office equipment emit hundreds of individual VOC species. Total Volatile Organic Compound (TVOC) concentration provides aggregate measure. Emission rates decrease exponentially after installation (off-gassing follows first-order decay):

{{< formula display="true" >}}
$$G(t) = G_0 \cdot e^{-kt}$$
{{< /formula >}}

Where $k$ is decay constant (typically 0.1-0.5 day⁻¹ for building materials). New construction requires higher ventilation rates during initial weeks, decreasing as off-gassing diminishes.

**Particulate Matter:** PM2.5 and PM10 concentrations depend on outdoor infiltration, indoor generation (cooking, combustion, resuspension), and filtration efficiency. The mass balance includes removal term:

{{< formula display="true" >}}
$$Q = \frac{G + Q_{inf} \cdot C_{out} - \eta \cdot Q_{recirc} \cdot C_{in}}{C_{in} - C_{out}}$$
{{< /formula >}}

Where $\eta$ is filter efficiency (MERV 13 filter: η ≈ 0.85 for PM2.5). High-efficiency filtration reduces ventilation requirements by providing removal mechanism complementary to dilution.

### IAQ Procedure Limitations

The IAQ Procedure offers flexibility for specialized applications (cleanrooms, laboratories, industrial spaces with known contaminant profiles) but faces practical challenges:

1. **Unknown Contaminants:** Typical buildings contain thousands of chemical species with unknown generation rates and health effects. Prescriptive ventilation rates provide safety margin against unidentified contaminants.

2. **Variable Generation:** Occupancy, activities, materials, and processes change over building lifetime. IAQ Procedure requires continuous monitoring and adaptive control.

3. **Measurement Challenges:** Real-time sensors exist for CO2, PM2.5, humidity, but comprehensive VOC speciation requires expensive analytical instrumentation.

4. **Acceptance Criteria:** Concentration limits for many contaminants lack consensus. WHO, EPA, OSHA, and other agencies publish different guidelines.

The IAQ Procedure applies best to specialized facilities with controlled contaminant sources, continuous monitoring capability, and expert oversight. Commercial office buildings typically use the simpler Ventilation Rate Procedure.

## Ventilation Effectiveness and Air Distribution

### Ventilation Effectiveness Fundamentals

Ventilation effectiveness quantifies how efficiently delivered outdoor air reaches occupants and dilutes contaminants in the breathing zone. Perfect mixing (outdoor air instantaneously and uniformly distributed throughout space) yields effectiveness = 1.0. Real systems exhibit spatial concentration gradients, short-circuiting between supply and return, and stratification, producing effectiveness ≠ 1.0.

ASHRAE defines multiple effectiveness metrics:

**Air Change Effectiveness ($\epsilon_a$):** Measures overall room air replacement efficiency:

{{< formula display="true" >}}
$$\epsilon_a = \frac{\tau_n}{\tau} = \frac{\tau_n}{2 \cdot \bar{\tau}}$$
{{< /formula >}}

Where:
- $\tau_n$ = nominal time constant = $V/Q$ (space volume / ventilation rate)
- $\tau$ = room mean age of air (average time air molecules have resided in space)
- $\bar{\tau}$ = average age of air at exhaust

For perfect piston flow (plug flow): $\epsilon_a = 2.0$. For perfect mixing: $\epsilon_a = 1.0$. For short-circuiting (supply air directly to exhaust): $\epsilon_a < 1.0$.

**Ventilation Effectiveness ($\epsilon_v$):** Relates contaminant concentration at exhaust to concentration at breathing zone:

{{< formula display="true" >}}
$$\epsilon_v = \frac{C_e - C_s}{C_b - C_s}$$
{{< /formula >}}

Where:
- $C_e$ = contaminant concentration at exhaust
- $C_s$ = contaminant concentration in supply air
- $C_b$ = contaminant concentration in breathing zone

For uniform generation throughout space and perfect mixing: $\epsilon_v = 1.0$. For displacement ventilation with floor-level contaminant sources: $\epsilon_v > 1.0$ (breathing zone receives cleaner air than exhaust). For ceiling supply with ceiling-level contaminant sources: $\epsilon_v < 1.0$ (breathing zone receives contaminated air before dilution).

**Air Distribution Effectiveness ($E_z$):** Used in ASHRAE 62.1 calculations, represents inverse of ventilation effectiveness normalized to mixing ventilation:

{{< formula display="true" >}}
$$E_z = \frac{\epsilon_v}{\epsilon_{v,mixing}} = \epsilon_v\ \text{(for typical cases)}$$
{{< /formula >}}

Values by system type:

{{< table >}}
| Distribution System | Air Distribution Effectiveness ($E_z$) | Application Notes |
|---------------------|---------------------------------------|-------------------|
| Ceiling Supply, Ceiling Return | 1.0 | Standard mixing ventilation baseline |
| Ceiling Supply, Floor Return | 1.0 | Negligible difference from ceiling return |
| Floor Supply, Ceiling Return (cooling) | 1.2 | Displacement ventilation, credit for efficiency |
| Floor Supply, Ceiling Return (heating) | 0.8 | Thermal stratification reduces breathing zone delivery |
| Underfloor Air Distribution (UFAD) | 1.2 | Low-velocity floor supply, thermal plumes enhance mixing |
| Displacement Ventilation | 1.2 | Cool air floor supply, contaminated air rises to ceiling |
| Personal Ventilation Systems | 1.0-1.5 | Individual desk/seat supply, highly variable |
{{< /table >}}

The physical mechanism for displacement ventilation: cool supply air (typically 63-68°F) delivered near floor at low velocity (< 50 FPM) spreads across floor. Human thermal plumes (occupants generate 250-400 BTU/hr sensible heat) create upward convection currents carrying occupant-generated contaminants toward ceiling. Supply air rising through thermal plumes reaches breathing zone (3-6 ft elevation) fresher than in mixed systems where return air recirculates throughout space. The result: same contaminant dilution with 15-20% less outdoor air ($E_z = 1.2$ means 1/1.2 = 0.83 outdoor air fraction).

### Age of Air Distribution

The age of air $\tau(x,y,z)$ represents the time elapsed since air molecules at location (x,y,z) entered the space. Young air (low age) indicates recent outdoor air delivery. Old air (high age) indicates recirculated or stagnant air.

For tracer gas decay measurement:

{{< formula display="true" >}}
$$\tau = \int_0^{\infty} \left(1 - \frac{C(t)}{C_0}\right) dt$$
{{< /formula >}}

Where $C(t)$ is tracer concentration decay from initial $C_0$ after ventilation begins.

For perfect mixing, age of air follows exponential distribution with mean age:

{{< formula display="true" >}}
$$\bar{\tau} = \frac{V}{Q}$$
{{< /formula >}}

This equals the nominal time constant. For displacement ventilation, breathing zone age is lower than average, while exhaust air age is higher, producing $\epsilon_a > 1.0$.

The practical implication: age of air measurements identify stagnant zones, short-circuiting paths, and stratification patterns. Design modifications (relocate supplies/returns, adjust throw patterns, change air change rates) target high-age zones to improve ventilation uniformity.

### Computational Fluid Dynamics Validation

CFD modeling enables prediction of air distribution effectiveness during design phase. The governing equations are Navier-Stokes (momentum conservation) and species transport (contaminant advection-diffusion):

**Continuity:**
{{< formula display="true" >}}
$$\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \vec{v}) = 0$$
{{< /formula >}}

**Momentum:**
{{< formula display="true" >}}
$$\frac{\partial (\rho \vec{v})}{\partial t} + \nabla \cdot (\rho \vec{v} \vec{v}) = -\nabla p + \nabla \cdot \tau + \rho \vec{g}$$
{{< /formula >}}

**Species Transport:**
{{< formula display="true" >}}
$$\frac{\partial (\rho C)}{\partial t} + \nabla \cdot (\rho \vec{v} C) = \nabla \cdot (D \nabla C) + S$$
{{< /formula >}}

Where $D$ is diffusion coefficient and $S$ is source term (contaminant generation rate per volume).

Turbulence modeling (k-ε, k-ω, or Large Eddy Simulation) captures mixing mechanisms at sub-grid scales. Boundary conditions include supply air temperature/velocity, return locations, heat sources (occupants, equipment, solar), and contaminant generation locations.

CFD results provide spatial maps of velocity, temperature, and contaminant concentration, enabling calculation of local air ages and ventilation effectiveness. Validation against tracer gas measurements in representative spaces confirms model accuracy before applying to full building design.

## CO2-Based Demand Control Ventilation

### DCV Fundamentals and Energy Savings

Demand Control Ventilation (DCV) modulates outdoor air intake based on real-time occupancy measurements rather than design maximum occupancy. The strategy exploits the time-varying nature of building occupancy: conference rooms cycle between empty and full, classrooms vacate between periods, restaurants vary with meal times. Operating at maximum outdoor air during low occupancy periods wastes conditioning energy.

CO2 concentration serves as occupancy proxy. Each person generates approximately 0.3 L/min CO2 (0.0106 CFM) at sedentary metabolism. Indoor CO2 rises above outdoor baseline in proportion to occupancy density and inversely to ventilation rate. Measuring indoor CO2 enables inference of current occupancy, allowing outdoor air modulation to match actual rather than design occupancy.

The steady-state CO2 balance:

{{< formula display="true" >}}
$$N \cdot G_{CO_2} = Q \cdot (C_{in} - C_{out})$$
{{< /formula >}}

Where:
- $N$ = number of occupants
- $G_{CO_2}$ = CO2 generation per person (CFM)
- $Q$ = outdoor air ventilation rate (CFM)
- $C_{in}$ = indoor CO2 concentration (ppm)
- $C_{out}$ = outdoor CO2 concentration (≈ 420 ppm currently)

Solving for required outdoor air:

{{< formula display="true" >}}
$$Q = \frac{N \cdot G_{CO_2}}{C_{in} - C_{out}}$$
{{< /formula >}}

For control implementation, invert to calculate target CO2 setpoint based on design ventilation rate:

{{< formula display="true" >}}
$$C_{setpoint} = C_{out} + \frac{N_{design} \cdot G_{CO_2}}{Q_{design}}$$
{{< /formula >}}

The controller maintains $C_{in} \leq C_{setpoint}$ by modulating outdoor air damper. When occupancy drops below design, less CO2 generation occurs, indoor CO2 decreases below setpoint, and the controller reduces outdoor air intake while maintaining the target concentration.

### DCV Control Strategies

**Proportional Control:** Outdoor air damper position modulates proportionally to CO2 error:

{{< formula display="true" >}}
$$OA_{damper} = OA_{min} + K_p \cdot (C_{measured} - C_{setpoint})$$
{{< /formula >}}

Where $K_p$ is proportional gain (damper %/ppm), $OA_{min}$ is minimum outdoor air fraction for area-based ventilation component.

**PI Control:** Adds integral term to eliminate steady-state offset:

{{< formula display="true" >}}
$$OA_{damper} = OA_{min} + K_p \cdot e + K_i \int e \, dt$$
{{< /formula >}}

Where $e = C_{measured} - C_{setpoint}$ is control error.

**Reset Control:** Adjusts CO2 setpoint based on outdoor air damper position to prevent hunting:

{{< formula display="true" >}}
$$C_{setpoint,adjusted} = C_{setpoint,base} + K_{reset} \cdot (OA_{damper} - OA_{design})$$
{{< /formula >}}

The physical interpretation: if outdoor air damper operates continuously at maximum position with CO2 still below setpoint, the setpoint is unnecessarily low and can be raised. If damper operates continuously at minimum position, setpoint can be lowered.

### DCV Energy Savings Calculation

The energy saved by DCV equals the reduction in conditioning load for eliminated outdoor air:

{{< formula display="true" >}}
$$Q_{saved} = Q_{design} - Q_{actual} = Q_{design} \cdot \left(1 - \frac{N_{actual}}{N_{design}}\right)$$
{{< /formula >}}

The conditioning energy savings:

**Cooling Season:**
{{< formula display="true" >}}
$$E_{saved,cooling} = Q_{saved} \times \rho \times c_p \times (T_{OA} - T_{SA}) \times \frac{hours}{12000 \times SEER}$$
{{< /formula >}}

**Heating Season:**
{{< formula display="true" >}}
$$E_{saved,heating} = Q_{saved} \times \rho \times c_p \times (T_{SA} - T_{OA}) \times \frac{hours}{\eta_{furnace}}$$
{{< /formula >}}

Where:
- $\rho$ = air density (0.075 lbm/ft³)
- $c_p$ = specific heat (0.24 BTU/lbm·°F)
- SEER = cooling system efficiency (BTU/Wh)
- $\eta_{furnace}$ = heating system efficiency

Example: Conference room with 50 person design occupancy, average actual occupancy 20 people (40% utilization), 2000 operating hours/year, $Q_{design}$ = 500 CFM, cooling season 1000 hours at average OA temp 85°F, supply air 55°F, SEER 12:

{{< formula display="true" >}}
$$Q_{saved} = 500 \times \left(1 - \frac{20}{50}\right) = 300\ \text{CFM}$$
{{< /formula >}}

{{< formula display="true" >}}
$$E_{saved} = 300 \times 0.075 \times 0.24 \times (85-55) \times \frac{1000}{12000 \times 12} = 1125\ \text{kWh/year}$$
{{< /formula >}}

At $0.12/kWh: $135/year savings. With CO2 sensor cost approximately $200-400 and installation $100-200, simple payback is 2-4 years.

The savings scale with design-to-actual occupancy ratio and outdoor-to-indoor temperature difference. Highest savings occur in spaces with highly variable occupancy (conference rooms, auditoriums, gymnasiums) in climates with extreme outdoor conditions. Minimal savings occur in continuously-occupied spaces (offices with stable staffing) or mild climates where outdoor air provides free cooling (economizer operation).

### DCV Sensor Requirements and Accuracy

ASHRAE 62.1 allows DCV for spaces larger than 500 ft² with variable occupancy and design occupancy > 25 people/1000 ft². CO2 sensors must maintain ±75 ppm accuracy over 0-2000 ppm range.

Sensor accuracy affects control stability. A 100 ppm sensor error at 1000 ppm indoor concentration represents approximately 20% error in calculated occupancy:

{{< formula display="true" >}}
$$N_{error} = \frac{C_{error}}{C_{in} - C_{out}} = \frac{100}{1000 - 420} = 17\%$$
{{< /formula >}}

Non-Dispersive Infrared (NDIR) CO2 sensors provide required accuracy with minimal drift. Electrochemical sensors exhibit higher drift and require frequent calibration. Sensor location matters: place in breathing zone (4-6 ft elevation), away from direct supply air jets, and near return air for representative sampling. Multiple sensors in large spaces prevent spatial bias from local pockets.

Sensor calibration: most NDIR sensors use two-point calibration (outdoor air ≈ 420 ppm, span gas at 1000-2000 ppm). Automatic Background Calibration (ABC) algorithms assume periodic exposure to outdoor air levels, correcting drift over weekly timescales. Spaces with 24/7 occupancy or consistently elevated CO2 require manual calibration.

## Air Change Effectiveness and Ventilation Efficiency

### Air Change Effectiveness Metrics

Air change effectiveness $\epsilon_a$ quantifies how many nominal air changes ($Q/V$) achieve equivalent contaminant removal as one actual air change with real mixing patterns. The metric depends on supply/exhaust locations, supply momentum (throw velocity), thermal stratification, and obstacle distribution.

For step-down tracer decay from initial concentration $C_0$:

{{< formula display="true" >}}
$$C(t) = C_0 \cdot e^{-\epsilon_a \cdot n \cdot t}$$
{{< /formula >}}

Where $n = Q/V$ is nominal air change rate (ACH). Measuring decay time constant reveals $\epsilon_a$.

For step-up tracer injection at constant rate $G$:

{{< formula display="true" >}}
$$C(t) = \frac{G}{Q} \left(1 - e^{-\epsilon_a \cdot n \cdot t}\right)$$
{{< /formula >}}

Steady-state concentration $C_{ss} = G/Q$ is independent of effectiveness, but time to reach 90% of steady-state depends on $\epsilon_a$:

{{< formula display="true" >}}
$$t_{90} = \frac{-\ln(0.1)}{\epsilon_a \cdot n} = \frac{2.3}{\epsilon_a \cdot n}$$
{{< /formula >}}

For $n = 6$ ACH (10 minute nominal time constant), $\epsilon_a = 1.0$: $t_{90}$ = 23 minutes. For $\epsilon_a = 0.5$ (poor mixing): $t_{90}$ = 46 minutes. The practical implication: low effectiveness spaces require longer purge times after high-contaminant events.

### Measuring Ventilation Effectiveness

Tracer gas testing quantifies actual ventilation effectiveness in occupied spaces. The protocol:

1. **Tracer Selection:** SF6 (sulfur hexafluoride) is most common due to negligible background concentration, non-toxicity, chemical stability, and detectability at ppb levels. CO2 works for unoccupied testing but elevated backgrounds in occupied spaces reduce sensitivity.

2. **Injection Method:** Constant concentration method maintains uniform tracer concentration at supply, measuring concentration rise in space until steady-state. Constant injection rate releases known tracer mass flow, measuring resulting steady-state concentration. Decay method establishes uniform initial concentration, measures exponential decay after tracer shutoff.

3. **Sampling Locations:** Minimum 3 locations per zone: breathing zone (5 ft elevation), near return air, and intermediate. Large zones require grid sampling to capture spatial variation.

4. **Calculation:** For constant concentration method:

{{< formula display="true" >}}
$$Q = \frac{G_{tracer}}{C_{exhaust} - C_{supply}}$$
{{< /formula >}}

For decay method:

{{< formula display="true" >}}
$$n \cdot \epsilon_a = -\frac{1}{\Delta t} \ln\left(\frac{C(t_2) - C_{background}}{C(t_1) - C_{background}}\right)$$
{{< /formula >}}

Where $\Delta t = t_2 - t_1$ is measurement interval.

Measured effectiveness lower than design indicates short-circuiting, stratification, or stagnant zones. Corrections include: relocate diffusers to improve throw patterns, add destratification fans, increase air change rate, switch to displacement ventilation, or add personal ventilation for critical breathing zones.

### System-Specific Effectiveness Values

Empirical data from tracer gas studies:

**Overhead Mixing Systems:** $\epsilon_a = 0.9$ to 1.1 depending on diffuser type and room geometry. Linear slot diffusers with high induction: 1.0-1.1. Low-induction perforated diffusers: 0.9-1.0.

**Underfloor Air Distribution (UFAD):** $\epsilon_a = 1.0$ to 1.3 in cooling mode. Floor swirl diffusers create horizontal spread followed by thermal plume entrainment. Effectiveness increases with higher cooling loads (stronger thermal stratification).

**Displacement Ventilation:** $\epsilon_a = 1.1$ to 1.3 for contaminants generated at floor/occupant level. Decreases to 0.8-0.9 for ceiling-level contaminant sources (defeats displacement mechanism).

**Personalized Ventilation:** $\epsilon_a = 1.2$ to 1.8 at breathing zone, but whole-room effectiveness remains 1.0. Local delivery of high outdoor air fraction creates microenvironment with superior air quality without increasing total outdoor air.

**Industrial High-Bay Spaces:** $\epsilon_a = 0.5$ to 0.8 due to thermal stratification. Hot industrial processes create strong upward convection with cool stagnant layer at floor level. Destratification fans, low-velocity high-volume (HVLS) fans, or fabric duct distribution improve effectiveness to 0.8-1.0.

The design implication: specifying displacement ventilation with $E_z = 1.2$ reduces required outdoor air by 17% compared to conventional mixing, yielding proportional energy savings on outdoor air conditioning.

## Breathing Zone Outdoor Airflow Calculations

### Single-Zone Breathing Zone Analysis

The breathing zone represents the region within an occupied space where occupants breathe, typically 3-72 inches above floor and more than 2 feet from walls. ASHRAE 62.1 requires adequate outdoor air delivery specifically to this zone, not merely to the space in general.

For single-zone systems, the breathing zone outdoor airflow $V_{bz}$ directly determines outdoor air intake after adjusting for air distribution effectiveness:

{{< formula display="true" >}}
$$V_{oz} = \frac{V_{bz}}{E_z}$$
{{< /formula >}}

For conventional ceiling supply/return with $E_z = 1.0$, the outdoor air intake equals breathing zone requirement. For underfloor air distribution with $E_z = 1.2$, the outdoor air intake is 83% of breathing zone requirement (credit for superior delivery efficiency).

The critical parameter is ensuring the assumed air distribution effectiveness matches actual installation. Displacement ventilation achieves $E_z = 1.2$ only when:
- Supply air temperature is below space temperature (cooling mode)
- Supply velocity is low (< 50 FPM at diffuser face)
- Ceiling height is adequate (> 9 ft) for stratification development
- Contaminants generate at floor/occupant level, not ceiling level

Violating these conditions (e.g., heating mode with warm supply air, or ceiling-mounted contaminant sources like recessed lighting) reduces effectiveness below 1.0, requiring higher outdoor air delivery to compensate.

### Multiple-Zone Breathing Zone Requirements

Complex air handling systems serving multiple zones with different occupancy densities face the challenge of delivering adequate outdoor air to each zone despite varying supply air outdoor air fractions.

The zone with highest ventilation requirement relative to its supply airflow (highest $Z_p = V_{oz}/V_{dz}$ ratio) becomes the critical zone. This zone receives outdoor air fraction equal to the system outdoor air fraction. All other zones receive higher outdoor air fractions because they have lower ventilation requirements relative to supply airflow.

Consider a 2-zone system:

**Zone 1 (Conference Room):**
- Area: 1000 ft², 50 occupants
- $V_{bz,1} = 5 \times 50 + 0.06 \times 1000 = 310$ CFM
- $V_{oz,1} = 310/1.0 = 310$ CFM (assuming $E_z = 1.0$)
- $V_{dz,1} = 2000$ CFM (cooling load drives supply air)
- $Z_{p,1} = 310/2000 = 0.155$

**Zone 2 (Office):**
- Area: 5000 ft², 25 occupants
- $V_{bz,2} = 5 \times 25 + 0.06 \times 5000 = 425$ CFM
- $V_{oz,2} = 425/1.0 = 425$ CFM
- $V_{dz,2} = 8000$ CFM
- $Z_{p,2} = 425/8000 = 0.053$

Zone 1 has higher $Z_p$, making it the critical zone. The system outdoor air fraction must be at least 0.155 to satisfy Zone 1. This means the total system outdoor air intake is:

{{< formula display="true" >}}
$$V_{ot} = Z_{p,max} \times V_{ps} = 0.155 \times 10000 = 1550\ \text{CFM}$$
{{< /formula >}}

This exceeds the simple sum $V_{oz,1} + V_{oz,2} = 735$ CFM by 111%. The excess is necessary because Zone 2 receives supply air with 15.5% outdoor air fraction when it only needs 5.3%, while Zone 1 receives exactly its required 15.5% fraction. The system cannot provide different outdoor air fractions to each zone without dedicated outdoor air to each zone (DOAS configuration).

### Ventilation Efficiency Reduction Factors

The system ventilation efficiency $E_v$ quantifies this inefficiency. For the example above, the uncorrected outdoor air is 735 CFM, but corrected requirement is 1550 CFM, yielding:

{{< formula display="true" >}}
$$E_v = \frac{V_{ou}}{V_{ot}} = \frac{735}{1550} = 0.47$$
{{< /formula >}}

This extremely low efficiency occurs when zones have vastly different ventilation requirements relative to supply airflow. Conference rooms (high occupancy density, moderate cooling loads) combined with open offices (low occupancy density, moderate cooling loads) produce worst-case scenarios.

Strategies to improve $E_v$:

1. **Dedicated Outdoor Air Systems (DOAS):** Separate outdoor air delivery to each zone at required rate, with local recirculation systems handling sensible/latent loads. Eliminates central system mixing inefficiency.

2. **Zone Transfer Air:** Allow high-ventilation zones to transfer air to adjacent low-ventilation zones before returning to air handler. Counted as outdoor air for receiving zone.

3. **Occupancy-Based Controls:** DCV in high-occupancy zones reduces peak outdoor air requirement, reducing divergence between zones.

4. **System Segmentation:** Serve similar occupancy types on common systems. Conference rooms and classrooms on one system, offices on another, reducing within-system diversity.

Typical $E_v$ values:
- Single zone: 1.0
- Multiple zones, similar occupancy: 0.7-0.9
- Multiple zones, diverse occupancy: 0.4-0.7
- DOAS configuration: 1.0 (each zone independently controlled)

## Multiple Space Ventilation Calculations

### System-Level Outdoor Air Determination

The complete ASHRAE 62.1 multiple zone calculation procedure:

**Step 1:** Calculate breathing zone outdoor airflow for each zone:
{{< formula display="true" >}}
$$V_{bz} = R_p \cdot P_z + R_a \cdot A_z$$
{{< /formula >}}

**Step 2:** Determine zone air distribution effectiveness $E_z$ based on distribution type (1.0 for ceiling, 1.2 for displacement/UFAD).

**Step 3:** Calculate zone outdoor airflow:
{{< formula display="true" >}}
$$V_{oz} = \frac{V_{bz}}{E_z}$$
{{< /formula >}}

**Step 4:** Determine zone primary airflow $V_{dz}$ from cooling/heating load calculations.

**Step 5:** Calculate zone primary outdoor air fraction:
{{< formula display="true" >}}
$$Z_p = \frac{V_{oz}}{V_{dz}}$$
{{< /formula >}}

**Step 6:** Calculate uncorrected outdoor air intake:
{{< formula display="true" >}}
$$V_{ou} = \sum V_{oz}$$
{{< /formula >}}

**Step 7:** Calculate system primary airflow:
{{< formula display="true" >}}
$$V_{ps} = \sum V_{dz}$$
{{< /formula >}}

**Step 8:** Calculate uncorrected outdoor air fraction:
{{< formula display="true" >}}
$$X_s = \frac{V_{ou}}{V_{ps}}$$
{{< /formula >}}

**Step 9:** Determine occupancy category (ASHRAE 62.1 Table 6.2.2.1) and corresponding diversity factor $D$.

**Step 10:** For single-path systems (most VAV), calculate system ventilation efficiency:
{{< formula display="true" >}}
$$E_v = \frac{1 + X_s - Z_{p,max}}{1 + X_s - D \cdot Z_{p,max}}$$
{{< /formula >}}

Where $D$ ranges from 0.25 (high diversity, like retail/multi-purpose) to 1.0 (low diversity, like single occupancy category).

**Step 11:** Calculate required outdoor air intake:
{{< formula display="true" >}}
$$V_{ot} = \frac{V_{ou}}{E_v}$$
{{< /formula >}}

### Worked Example: Office Building VAV System

Consider a VAV system serving 4 zones:

{{< table >}}
| Zone | Type | Area (ft²) | People | $R_p$ | $R_a$ | $V_{bz}$ | $E_z$ | $V_{oz}$ | $V_{dz}$ | $Z_p$ |
|------|------|-----------|--------|-------|-------|----------|-------|----------|----------|-------|
| 1 | Conference | 800 | 40 | 5 | 0.06 | 248 | 1.0 | 248 | 1600 | 0.155 |
| 2 | Office | 3200 | 16 | 5 | 0.06 | 272 | 1.0 | 272 | 5200 | 0.052 |
| 3 | Office | 2400 | 12 | 5 | 0.06 | 204 | 1.0 | 204 | 3900 | 0.052 |
| 4 | Reception | 600 | 4 | 5 | 0.06 | 56 | 1.0 | 56 | 1000 | 0.056 |
| **Total** | | **7000** | **72** | | | **780** | | **780** | **11700** | |
{{< /table >}}

$V_{ou} = 780$ CFM

$V_{ps} = 11700$ CFM

$X_s = 780/11700 = 0.0667$

$Z_{p,max} = 0.155$ (Zone 1 conference room)

For office building with mixed occupancy, use diversity $D = 0.6$:

{{< formula display="true" >}}
$$E_v = \frac{1 + 0.0667 - 0.155}{1 + 0.0667 - 0.6 \times 0.155} = \frac{0.912}{0.974} = 0.936$$
{{< /formula >}}

{{< formula display="true" >}}
$$V_{ot} = \frac{780}{0.936} = 833\ \text{CFM}$$
{{< /formula >}}

The system must provide 833 CFM outdoor air, 6.8% more than the simple sum of zone requirements, to ensure Zone 1 receives adequate outdoor air despite its high $Z_p$ ratio.

System outdoor air percentage:
{{< formula display="true" >}}
$$\%OA = \frac{833}{11700} \times 100\% = 7.1\%$$
{{< /formula >}}

At minimum airflow conditions (assume VAV boxes at 40% minimum):
{{< formula display="true" >}}
$$V_{ps,min} = 11700 \times 0.4 = 4680\ \text{CFM}$$
{{< /formula >}}

{{< formula display="true" >}}
$$\%OA_{min} = \frac{833}{4680} \times 100\% = 17.8\%$$
{{< /formula >}}

The outdoor air damper must modulate from 17.8% (minimum airflow) to 7.1% (design airflow) to maintain constant 833 CFM outdoor air intake across VAV system load variation.

### Critical Zone Identification

The critical zone (maximum $Z_p$) shifts as loads change. During cooling season, perimeter zones with high solar/envelope loads operate at maximum airflow while interior zones throttle down. During heating season, interior zones with high internal gains operate at maximum while perimeter zones reduce. The control system must track $Z_p$ for all zones continuously and adjust system outdoor air to satisfy the instantaneous critical zone.

Advanced implementations calculate required outdoor air intake at each timestep:

{{< formula display="true" >}}
$$V_{ot}(t) = Z_{p,max}(t) \times V_{ps}(t)$$
{{< /formula >}}

This dynamic calculation provides minimum outdoor air necessary to satisfy current critical zone, reducing outdoor air during part-load conditions compared to fixed outdoor air based on design conditions.

## Energy Recovery Ventilator Sizing

### ERV/HRV Fundamentals

Energy Recovery Ventilators (ERV) and Heat Recovery Ventilators (HRV) transfer energy between outdoor air supply and exhaust air streams, reducing conditioning load from ventilation outdoor air. HRV transfers sensible heat only (temperature). ERV transfers both sensible and latent heat (temperature and humidity).

The heat exchanger configurations:

**Plate Heat Exchangers:** Alternating supply and exhaust air channels separated by thin conductive plates. Sensible effectiveness 50-80%, latent effectiveness 40-60% (for ERV with vapor-permeable plates). No cross-contamination. Fixed flow ratio between supply and exhaust.

**Rotary Enthalpy Wheels:** Rotating desiccant-coated wheel alternately exposed to supply and exhaust airstreams. Sensible effectiveness 70-85%, latent effectiveness 60-75%. Requires small purge section to minimize cross-contamination (1-3% exhaust air carryover to supply).

**Heat Pipe Exchangers:** Sealed refrigerant-filled tubes with evaporator in exhaust stream, condenser in supply stream. Sensible-only (HRV). Effectiveness 45-65%. Passive operation (no moving parts or energy input).

**Run-Around Coils:** Separate coils in exhaust and supply ducts connected by pumped glycol loop. Allows non-adjacent exhaust and supply duct locations. Sensible effectiveness 45-60%. Active pumping required.

### ERV Effectiveness and Capacity

Sensible effectiveness quantifies temperature transfer efficiency:

{{< formula display="true" >}}
$$\epsilon_{sensible} = \frac{T_{SA} - T_{OA}}{T_{EA} - T_{OA}}$$
{{< /formula >}}

Where:
- $T_{SA}$ = supply air temperature leaving ERV
- $T_{OA}$ = outdoor air temperature entering ERV
- $T_{EA}$ = exhaust air temperature entering ERV

Total effectiveness (for ERV) includes latent transfer:

{{< formula display="true" >}}
$$\epsilon_{total} = \frac{h_{SA} - h_{OA}}{h_{EA} - h_{OA}}$$
{{< /formula >}}

Where $h$ represents enthalpy (BTU/lbm).

The sensible heat recovery rate:

{{< formula display="true" >}}
$$Q_{sensible} = \dot{m} \cdot c_p \cdot \epsilon_{sensible} \cdot (T_{EA} - T_{OA})$$
{{< /formula >}}

Where $\dot{m} = \rho \cdot Q$ is mass flow rate (lbm/min).

For airflow rate in CFM:

{{< formula display="true" >}}
$$Q_{sensible} = 1.08 \cdot CFM \cdot \epsilon_{sensible} \cdot \Delta T\ [\text{BTU/hr}]$$
{{< /formula >}}

The total recovery (sensible + latent):

{{< formula display="true" >}}
$$Q_{total} = 4.5 \cdot CFM \cdot \epsilon_{total} \cdot \Delta h\ [\text{BTU/hr}]$$
{{< /formula >}}

Where $\Delta h$ is enthalpy difference between exhaust and outdoor air (BTU/lbm).

### ERV Sizing Example

Office building requiring 800 CFM outdoor air ventilation. Location: Chicago (Design cooling: 91°F DB, 75°F WB; Design heating: -7°F). Indoor conditions: 75°F, 50% RH.

**Summer Cooling Design:**
- $T_{OA} = 91°F$, $h_{OA} = 38.2$ BTU/lbm
- $T_{EA} = 75°F$, $h_{EA} = 28.1$ BTU/lbm
- ERV with $\epsilon_{sensible} = 0.75$, $\epsilon_{total} = 0.70$

Supply air temperature leaving ERV:
{{< formula display="true" >}}
$$T_{SA} = T_{OA} - \epsilon_{sensible} \cdot (T_{OA} - T_{EA}) = 91 - 0.75 \times (91-75) = 79°F$$
{{< /formula >}}

Sensible recovery:
{{< formula display="true" >}}
$$Q_{sensible} = 1.08 \times 800 \times 0.75 \times 16 = 10,368\ \text{BTU/hr}$$
{{< /formula >}}

Total recovery:
{{< formula display="true" >}}
$$Q_{total} = 4.5 \times 800 \times 0.70 \times (38.2 - 28.1) = 25,452\ \text{BTU/hr}\ (2.1\ \text{tons})$$
{{< /formula >}}

**Winter Heating Design:**
- $T_{OA} = -7°F$, $h_{OA} = 2.6$ BTU/lbm
- $T_{EA} = 75°F$, $h_{EA} = 28.1$ BTU/lbm

Supply air temperature leaving ERV:
{{< formula display="true" >}}
$$T_{SA} = -7 + 0.75 \times (75 - (-7)) = 54.5°F$$
{{< /formula >}}

Sensible recovery:
{{< formula display="true" >}}
$$Q_{sensible} = 1.08 \times 800 \times 0.75 \times 82 = 53,136\ \text{BTU/hr}$$
{{< /formula >}}

The ERV reduces outdoor air heating load from 70,848 BTU/hr (untempered -7°F outdoor air to 75°F) to 17,712 BTU/hr (tempered 54.5°F air to 75°F), saving 75% of ventilation heating energy.

### ERV Annual Energy Savings

Annual savings depend on climate-specific temperature and humidity distributions. The analysis requires bin analysis integrating recovery over all operating hours:

{{< formula display="true" >}}
$$E_{saved} = \sum_{bins} hours_{bin} \times CFM \times 1.08 \times \epsilon_{sensible} \times \Delta T_{bin} \times \frac{1}{\eta_{HVAC}}$$
{{< /formula >}}

For Chicago climate with 5000 degree-days heating, 1000 degree-days cooling, 3000 operating hours/year, $\eta_{cooling} = 12$ SEER, $\eta_{heating} = 0.9$ furnace efficiency:

Heating season savings: approximately 45,000 kWh thermal equivalent = 50,000 kWh gas / 0.9 efficiency

Cooling season savings: approximately 12,000 kWh thermal / 3.5 COP = 3,400 kWh electric

Total utility cost savings (gas $1.20/therm, electric $0.12/kWh):
- Heating: 50,000 kWh × 3412 BTU/kWh / 100,000 BTU/therm × $1.20 = $2,050
- Cooling: 3,400 kWh × $0.12 = $410
- **Annual savings: $2,460**

ERV equipment cost for 800 CFM: approximately $4,000-6,000. Installation: $2,000-4,000. Total installed cost: $6,000-10,000. Simple payback: 2.4-4.1 years.

### Frost Prevention and Bypass Controls

In heating season with cold outdoor air, moisture transferred from exhaust to supply side can freeze on heat exchanger surfaces when supply air temperature drops below 32°F. Frost accumulation blocks airflow and damages exchanger.

The frost formation threshold occurs when:

{{< formula display="true" >}}
$$T_{OA} < 32 - \epsilon_{sensible} \times (T_{EA} - 32)$$
{{< /formula >}}

For $\epsilon_{sensible} = 0.75$, $T_{EA} = 75°F$:
{{< formula display="true" >}}
$$T_{OA,frost} < 32 - 0.75 \times 43 = -0.25°F$$
{{< /formula >}}

Below approximately 0°F outdoor temperature, frost risk requires prevention strategies:

1. **Exhaust Air Recirculation:** Bypass portion of exhaust air back through exhaust side, raising average exhaust temperature and reducing frost.

2. **Preheat Coil:** Electric or hot water coil in outdoor air upstream of ERV raises inlet temperature above freezing threshold.

3. **Wheel Speed Reduction:** For rotary wheels, reduce rotation speed to decrease effectiveness and frost formation rate.

4. **Defrost Cycle:** Periodically bypass outdoor air around ERV, allowing exhaust air to warm and melt accumulated frost.

The energy penalty from frost prevention reduces net annual savings. Preheat energy consumption:

{{< formula display="true" >}}
$$Q_{preheat} = 1.08 \times CFM \times (32 - T_{OA}) \times hours_{below\ freezing}$$
{{< /formula >}}

For Chicago with approximately 500 hours below 0°F, average temperature -5°F during those hours:

{{< formula display="true" >}}
$$Q_{preheat} = 1.08 \times 800 \times (32 - (-5)) \times 500 = 16\ \text{million BTU} = 4,685\ \text{kWh thermal}$$
{{< /formula >}}

This represents approximately 9% reduction in annual heating savings. Frost prevention remains cost-effective given remaining 91% savings capture.

## Contaminant Dilution Equations

### Steady-State Dilution Ventilation

Dilution ventilation controls contaminant concentration through continuous outdoor air supply that dilutes generation sources. The fundamental mass balance for a well-mixed space:

{{< formula display="true" >}}
$$V \frac{dC}{dt} = G - Q \cdot (C - C_{out}) - k \cdot V \cdot C$$
{{< /formula >}}

Where:
- $V$ = space volume (ft³)
- $C$ = contaminant concentration in space
- $t$ = time
- $G$ = contaminant generation rate (mass/time or volume/time)
- $Q$ = ventilation rate (CFM)
- $C_{out}$ = outdoor contaminant concentration
- $k$ = first-order decay/removal rate constant (1/time)

At steady-state ($dC/dt = 0$):

{{< formula display="true" >}}
$$C_{ss} = \frac{G}{Q + k \cdot V} + C_{out}$$
{{< /formula >}}

For contaminants with negligible outdoor concentration and no removal mechanisms:

{{< formula display="true" >}}
$$C_{ss} = \frac{G}{Q}$$
{{< /formula >}}

This defines the fundamental dilution relationship: steady-state indoor concentration equals generation rate divided by ventilation rate. Doubling ventilation rate halves concentration. Doubling generation rate doubles concentration.

### Transient Contaminant Response

For step-change in generation rate from $G_1$ to $G_2$ at time $t=0$:

{{< formula display="true" >}}
$$C(t) = C_{ss,2} + (C_{ss,1} - C_{ss,2}) \cdot e^{-\frac{Q+kV}{V}t}$$
{{< /formula >}}

Where $C_{ss,1}$ and $C_{ss,2}$ are steady-state concentrations before and after the step change.

The time constant for concentration response:

{{< formula display="true" >}}
$$\tau = \frac{V}{Q + kV} = \frac{1}{n + k}$$
{{< /formula >}}

Where $n = Q/V$ is air change rate (ACH).

For ventilation-dominated removal ($k \approx 0$):
{{< formula display="true" >}}
$$\tau = \frac{V}{Q} = \frac{1}{n}$$
{{< /formula >}}

The time to reach 90% of new steady-state:
{{< formula display="true" >}}
$$t_{90} = -\tau \ln(0.1) = 2.3 \tau = \frac{2.3}{n}$$
{{< /formula >}}

For $n = 2$ ACH (30-minute time constant): $t_{90} = 69$ minutes. Increasing to 6 ACH reduces $t_{90}$ to 23 minutes, providing faster contaminant purge.

### Practical Dilution Ventilation Examples

**Example 1: Solvent Usage in Laboratory**

Paint thinner (mineral spirits) usage in fume hood with partial capture. Evaporation rate: 50 g/hr. Occupational Exposure Limit (OEL): 100 ppm. Laboratory volume: 12,000 ft³. Assume 80% capture efficiency by hood (exhausted directly), 20% escapes to room. Outdoor concentration negligible.

Generation rate to room:
{{< formula display="true" >}}
$$G = 50\ \text{g/hr} \times 0.20 = 10\ \text{g/hr}$$
{{< /formula >}}

Mineral spirits molecular weight ≈ 140 g/mol, density at room temp ≈ 0.78 g/L. Convert OEL to mass concentration:

At standard conditions, 100 ppm = 100 × 140/24.45 = 573 mg/m³ = 16.2 mg/ft³

Required ventilation to maintain below OEL:
{{< formula display="true" >}}
$$Q = \frac{G}{C_{limit}} = \frac{10,000\ \text{mg/hr}}{16.2\ \text{mg/ft}^3} = 617\ \text{CFM}$$
{{< /formula >}}

Air change rate:
{{< formula display="true" >}}
$$n = \frac{617}{12,000} \times 60 = 3.1\ \text{ACH}$$
{{< /formula >}}

This exceeds typical laboratory ventilation (6-12 ACH), indicating the fume hood capture efficiency must be verified and improved, or solvent usage must be reduced.

**Example 2: CO2 Generation in Classroom**

Classroom: 1,200 ft², 9 ft ceiling, 30 students. Metabolic CO2 generation: 0.3 L/min per person. Target indoor CO2: 1000 ppm above outdoor (1420 ppm absolute, outdoor 420 ppm).

Volume: $V = 1200 \times 9 = 10,800$ ft³

Total CO2 generation:
{{< formula display="true" >}}
$$G = 30 \times 0.3\ \text{L/min} = 9\ \text{L/min} = 0.318\ \text{CFM}$$
{{< /formula >}}

At 1000 ppm difference, mass concentration ≈ 1800 mg/m³ = 51 mg/ft³

Required ventilation:
{{< formula display="true" >}}
$$Q = \frac{G}{C_{limit}} = \frac{9\ \text{L/min} \times 1.98\ \text{g/L} \times 1000\ \text{mg/g}}{51\ \text{mg/ft}^3} = 349\ \text{CFM}$$
{{< /formula >}}

ASHRAE 62.1 requirement for classroom: $V_{bz} = 10 \times 30 + 0.12 \times 1200 = 444$ CFM. The ASHRAE rate exceeds CO2-based calculation, providing margin for other bioeffluents and contaminants beyond CO2.

**Example 3: Formaldehyde Off-Gassing from Furnishings**

New office installation with pressed-wood furnishings. Formaldehyde emission rate: 0.1 mg/m²·hr from 500 m² of surface area (desks, cabinets, shelving). Office volume: 50,000 ft³. Target formaldehyde concentration: < 0.1 ppm (123 μg/m³).

Total generation:
{{< formula display="true" >}}
$$G = 0.1\ \text{mg/m}^2\text{·hr} \times 500\ \text{m}^2 = 50\ \text{mg/hr}$$
{{< /formula >}}

Concentration limit: 123 μg/m³ = 3.48 μg/ft³ = 0.00348 mg/ft³

Required ventilation:
{{< formula display="true" >}}
$$Q = \frac{50\ \text{mg/hr}}{0.00348\ \text{mg/ft}^3} = 14,368\ \text{CFM}$$
{{< /formula >}}

This extremely high rate (17.2 ACH) is impractical. Alternative strategies:

1. **Source Control:** Select low-formaldehyde materials (formaldehyde-free MDF, solid wood). Reduces $G$ by factor of 10-100.

2. **Bake-Out:** Elevate temperature (80-90°F) with high ventilation for 1-2 weeks before occupancy. Accelerates off-gassing during unoccupied period.

3. **Air Cleaning:** Activated carbon or potassium permanganate filters provide formaldehyde removal. Adds $k$ term to dilution equation, reducing required ventilation.

4. **Time:** Formaldehyde emission follows first-order decay with half-life of weeks to months. Emission rate drops to 10-20% of initial within 6 months.

The calculation demonstrates that dilution ventilation alone cannot address high-emission sources. Source control remains the primary strategy, with ventilation as supplementary measure.

### Multi-Contaminant Analysis

Real spaces contain multiple contaminants with different generation rates, concentration limits, and removal mechanisms. The required ventilation rate is the maximum among all individual contaminant requirements:

{{< formula display="true" >}}
$$Q_{required} = \max\left(\frac{G_1}{C_{1,limit}}, \frac{G_2}{C_{2,limit}}, \ldots, \frac{G_n}{C_{n,limit}}\right)$$
{{< /formula >}}

Each contaminant may dominate under different conditions:
- **CO2 dominates** in high-occupancy, low-emission spaces (offices, classrooms)
- **VOCs dominate** in new construction or spaces with significant material off-gassing
- **Particulates dominate** in spaces with combustion, industrial processes, or high outdoor PM2.5
- **Moisture dominates** in humid climates or spaces with water-intensive processes

Continuous monitoring of multiple species enables identification of limiting contaminant and optimization of ventilation/filtration strategies for cost-effective air quality maintenance.

## Practical Calculation Examples

### Example 1: Multi-Zone Office Building VAV System

**Building Description:**
- 3-story office building, 45,000 ft² total
- Single VAV air handler per floor (3 total systems)
- Floor 2 analysis: 15,000 ft² served by AHU-2

**Zone Breakdown:**

{{< table >}}
| Zone | Type | Area (ft²) | Occupants | Cooling Load (tons) | Airflow (CFM) |
|------|------|-----------|----------|-------------------|--------------|
| 2-1 | Open Office | 6,000 | 30 | 18 | 7,200 |
| 2-2 | Private Offices | 3,200 | 16 | 10 | 4,000 |
| 2-3 | Conference Room | 1,200 | 60 | 8 | 3,600 |
| 2-4 | Break Room | 800 | 8 | 4 | 1,600 |
| 2-5 | Corridor | 2,400 | 0 | 3 | 1,200 |
| 2-6 | IT Room | 1,400 | 2 | 12 | 4,800 |
{{< /table >}}

**Outdoor Air Calculation:**

Zone 2-1 (Open Office):
{{< formula display="true" >}}
$$V_{bz} = 5 \times 30 + 0.06 \times 6000 = 150 + 360 = 510\ \text{CFM}$$
{{< /formula >}}
$$V_{oz} = 510/1.0 = 510\ \text{CFM}$$
$$Z_p = 510/7200 = 0.0708$$

Zone 2-2 (Private Offices):
$$V_{bz} = 5 \times 16 + 0.06 \times 3200 = 80 + 192 = 272\ \text{CFM}$$
$$V_{oz} = 272/1.0 = 272\ \text{CFM}$$
$$Z_p = 272/4000 = 0.0680$$

Zone 2-3 (Conference):
$$V_{bz} = 5 \times 60 + 0.06 \times 1200 = 300 + 72 = 372\ \text{CFM}$$
$$V_{oz} = 372/1.0 = 372\ \text{CFM}$$
$$Z_p = 372/3600 = 0.1033$$

Zone 2-4 (Break Room):
$$V_{bz} = 7.5 \times 8 + 0.18 \times 800 = 60 + 144 = 204\ \text{CFM}$$
$$V_{oz} = 204/1.0 = 204\ \text{CFM}$$
$$Z_p = 204/1600 = 0.1275$$

Zone 2-5 (Corridor):
$$V_{bz} = 0 \times 0 + 0.06 \times 2400 = 144\ \text{CFM}$$
$$V_{oz} = 144/1.0 = 144\ \text{CFM}$$
$$Z_p = 144/1200 = 0.1200$$

Zone 2-6 (IT Room):
$$V_{bz} = 5 \times 2 + 0.06 \times 1400 = 10 + 84 = 94\ \text{CFM}$$
$$V_{oz} = 94/1.0 = 94\ \text{CFM}$$
$$Z_p = 94/4800 = 0.0196$$

**System Totals:**
{{< formula display="true" >}}
$$V_{ou} = 510 + 272 + 372 + 204 + 144 + 94 = 1,596\ \text{CFM}$$
{{< /formula >}}
$$V_{ps} = 7200 + 4000 + 3600 + 1600 + 1200 + 4800 = 22,400\ \text{CFM}$$
$$X_s = 1596/22400 = 0.0713$$
$$Z_{p,max} = 0.1275\ \text{(Zone 2-4, Break Room)}$$

Diversity factor for office building with break room: $D = 0.75$

{{< formula display="true" >}}
$$E_v = \frac{1 + 0.0713 - 0.1275}{1 + 0.0713 - 0.75 \times 0.1275} = \frac{0.944}{1.015} = 0.930$$
{{< /formula >}}

{{< formula display="true" >}}
$$V_{ot} = \frac{1596}{0.930} = 1,716\ \text{CFM}$$
{{< /formula >}}

**System Design Parameters:**
- Outdoor air intake: 1,716 CFM
- Outdoor air percentage at design: 7.7%
- Outdoor air percentage at 40% minimum flow: 1,716/8,960 = 19.1%

**Energy Recovery Analysis:**

Climate: Minneapolis (7,400 HDD, 800 CDD). ERV with 75% sensible effectiveness.

Winter design: -12°F outdoor, 72°F indoor
Summer design: 91°F outdoor, 75°F indoor

Winter heat recovery:
{{< formula display="true" >}}
$$Q_{winter} = 1.08 \times 1716 \times 0.75 \times (72-(-12)) = 116,748\ \text{BTU/hr}$$
{{< /formula >}}

Annual heating savings (simplified bin analysis):
$$E_{heat} \approx 7400 \times 24 \times 1716 \times 1.08 \times 0.75 / 100,000 = 2,947\ \text{therms/year}$$

At $1.20/therm: **$3,536/year heating savings**

Summer cooling recovery:
$$Q_{summer} = 1.08 \times 1716 \times 0.75 \times (91-75) = 22,252\ \text{BTU/hr}$$

Annual cooling savings:
$$E_{cool} \approx 800 \times 24 \times 22,252 / 12,000 / 3.5 = 1,016\ \text{kWh/year electric}$$

At $0.12/kWh: **$122/year cooling savings**

**Total annual ERV savings: $3,658**

ERV equipment cost (1,700 CFM): $7,000. Installation: $3,500. **Payback: 2.9 years**

### Example 2: Residential House with Balanced Ventilation

**House Specifications:**
- 2,800 ft² conditioned area
- 4 bedrooms
- 22,400 ft³ volume (8 ft average ceiling)
- Blower door test: ACH50 = 3.5
- Climate: Portland, OR (mild, marine)

**ASHRAE 62.2 Whole-House Ventilation:**

{{< formula display="true" >}}
$$Q_{tot} = 0.03 \times 2800 + 7.5 \times (4+1) = 84 + 37.5 = 121.5\ \text{CFM}$$
{{< /formula >}}

**Infiltration Credit:**

Normalized leakage for mild climate: $NL = 0.6$

{{< formula display="true" >}}
$$Q_{inf} = \frac{0.6 \times 3.5 \times 22400}{60} = 784\ \text{CFM}$$
{{< /formula >}}

This exceeds whole-house requirement, but infiltration is uncontrolled and climate-dependent. Recommend mechanical ventilation for consistent air quality with infiltration credit factor $\phi = 0.5$ (partial credit):

{{< formula display="true" >}}
$$Q_{fan} = 121.5 - 784 \times 0.5 \times \frac{121.5}{121.5 + 784 \times 0.5} = 68\ \text{CFM}$$
{{< /formula >}}

Use conservative approach: install 120 CFM ERV for full continuous ventilation without infiltration credit dependency.

**Local Exhaust:**
- Kitchen: 100 CFM range hood, vented outdoors
- Master bath: 50 CFM continuous
- Bath 2: 50 CFM continuous
- Bath 3: 50 CFM intermittent (occupancy sensor)

**ERV Selection:**

120 CFM ERV with 70% sensible effectiveness, 60% latent effectiveness.

Portland climate: 4,200 HDD, 200 CDD (mild climate, minimal savings)

Annual heating savings (natural gas heat, 92% AFUE):
$$E = 4200 \times 24 \times 120 \times 1.08 \times 0.70 / (100,000 \times 0.92) = 991\ \text{therms}$$

At $1.10/therm: **$1,090/year**

Annual cooling savings (minimal in Portland):
**$25/year**

Total annual utility savings: **$1,115**

ERV equipment (120 CFM residential): $1,200
Installation with ductwork: $1,800
**Total cost: $3,000**
**Payback: 2.7 years**

### Example 3: Laboratory with High Outdoor Air Requirements

**Laboratory Specifications:**
- Research laboratory with 8 fume hoods
- Area: 2,400 ft²
- Ceiling height: 10 ft, volume: 24,000 ft³
- Design occupancy: 12 researchers
- Fume hoods: 6 ft wide, 100 FPM face velocity at 18" sash opening

**Fume Hood Exhaust:**

Per hood: $Q_{hood} = 6\ \text{ft} \times 1.5\ \text{ft} \times 100\ \text{FPM} = 900\ \text{CFM}$

Total hood exhaust: $8 \times 900 = 7,200$ CFM

**ASHRAE 62.1 Ventilation:**

Laboratory occupancy category: $R_p = 10$ CFM/person, $R_a = 0.18$ CFM/ft²

{{< formula display="true" >}}
$$V_{bz} = 10 \times 12 + 0.18 \times 2400 = 120 + 432 = 552\ \text{CFM}$$
{{< /formula >}}

**Total Outdoor Air Requirement:**

Fume hood exhaust dominates: 7,200 CFM must be replaced with outdoor air makeup.

ASHRAE 62.1 requirement (552 CFM) is subsumed within hood makeup air.

**Air Change Rate:**

{{< formula display="true" >}}
$$ACH = \frac{7200 \times 60}{24000} = 18\ \text{ACH}$$
{{< /formula >}}

This meets typical laboratory requirement of 6-12 ACH minimum (high hazard labs require up to 20 ACH).

**Heating/Cooling Load:**

Winter design (Chicago): -7°F outdoor, 70°F indoor

Heating load from outdoor air:
{{< formula display="true" >}}
$$Q_{heat} = 1.08 \times 7200 \times (70 - (-7)) = 598,752\ \text{BTU/hr} = 50\ \text{kW}$$
{{< /formula >}}

Annual heating energy (5,000 operating hours at average 35°F outdoor):
$$E_{heat} = 1.08 \times 7200 \times (70-35) \times 5000 / 100,000 = 13,608\ \text{therms}$$

At $1.20/therm: **$16,330/year ventilation heating cost**

**Energy Recovery Opportunity:**

Laboratory exhaust contains hazardous chemicals, prohibiting recirculation or run-around coils. Option: Runaround coil with glycol loop (no cross-contamination).

Runaround effectiveness: 50%

Heating savings:
$$E_{saved} = 13,608 \times 0.50 = 6,804\ \text{therms/year}$$

Annual savings: **$8,165**

Runaround coil system (7,200 CFM, hazardous exhaust rating): $35,000
Installation: $15,000
**Total: $50,000**
**Payback: 6.1 years**

The moderate payback is acceptable for laboratory applications given high energy costs and long equipment lifetime (20+ years).

## Conclusion

Ventilation rate design integrates physiological requirements (oxygen supply, CO2 removal, bioeffluent dilution), building emission characteristics (material off-gassing, process contaminants), and thermodynamic energy management (conditioning load minimization, energy recovery). ASHRAE Standards 62.1 and 62.2 provide prescriptive frameworks translating these multifaceted requirements into engineered airflow specifications.

The mathematical foundation rests on mass balance equations: contaminant generation balanced by dilution ventilation and removal mechanisms. The Ventilation Rate Procedure offers conservative, prescriptive rates validated through empirical acceptability studies. The Indoor Air Quality Procedure enables performance-based optimization for specialized applications with defined contaminant profiles.

Critical design parameters include breathing zone outdoor airflow calculations accounting for both people-based and area-based emission sources, multiple zone system ventilation efficiency corrections addressing distribution losses and mixing challenges, air distribution effectiveness quantifying spatial delivery performance, and energy recovery integration reducing the thermodynamic penalty of outdoor air ventilation.

CO2-based demand control ventilation exploits occupancy variability to reduce energy consumption while maintaining air quality during partial occupancy. The strategy requires accurate sensing, proper control algorithms, and recognition that CO2 serves as occupancy proxy rather than complete air quality metric.

Contaminant dilution equations govern transient response, steady-state concentrations, and required ventilation rates for specific pollutants. Multi-contaminant environments require identification of limiting species and integration of source control, filtration, and ventilation strategies.

The practical examples demonstrate complete calculation procedures for commercial multi-zone systems, residential balanced ventilation with energy recovery, and high-ventilation laboratory applications. Each scenario exhibits distinct controlling parameters: commercial systems balance multiple zone diversity against energy efficiency, residential design emphasizes continuous low-level ventilation with point-source exhaust, and laboratories prioritize safety and hazardous contaminant control over energy optimization.

Energy recovery ventilators provide 2-6 year simple paybacks in most climate zones, with greatest savings in heating-dominated climates where large indoor-outdoor temperature differences maximize recoverable energy. Frost prevention requirements in extreme cold climates impose modest energy penalties but preserve net savings.

The ventilation design process proceeds from first-principles physics (mass/energy conservation) through standardized calculation procedures (ASHRAE 62.1/62.2) to system-specific implementation (equipment selection, control strategies, commissioning verification). The objective is quantifiable: deliver specified outdoor airflow to breathing zones while minimizing energy consumption and capital cost. Proper execution produces indoor environments supporting occupant health, productivity, and comfort within engineered constraints.
