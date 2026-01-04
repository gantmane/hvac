---
title: "NOx Reduction Techniques"
weight: 7
description: "Engineering analysis of nitrogen oxide (NOx) reduction techniques including flue gas recirculation (FGR), selective catalytic reduction (SCR), selective non-catalytic reduction (SNCR), staged combustion, water injection, ultra-low NOx burner design, and combined NOx control strategies for meeting stringent air quality regulations."
keywords: "NOx reduction, nitrogen oxides, flue gas recirculation, FGR, SCR, selective catalytic reduction, SNCR, staged combustion, ultra-low NOx burners, low-NOx burner, thermal NOx, fuel NOx"
---

# NOx Reduction Techniques

Nitrogen oxide (NOx) emissions from combustion equipment must be minimized to meet increasingly stringent air quality regulations (9-60 ppm depending on jurisdiction and source size). NOx reduction strategies include combustion modification techniques achieving 40-80% reduction through flue gas recirculation (FGR), staged combustion, and ultra-low NOx burner designs, and post-combustion treatment via selective catalytic reduction (SCR) achieving 80-95% removal for ultra-low emission requirements (<9 ppm). Selection among NOx control methods requires balancing capital cost ($100-500/kW for combustion controls, $200-1000/kW for SCR), operating cost (auxiliary power, catalyst replacement, chemical consumption), emission reduction effectiveness, and equipment retrofit feasibility.

## NOx Formation Mechanisms

### Thermal NOx (Zeldovich Mechanism)

**Primary NOx formation route in most combustion:**

Occurs at high temperatures (>2800°F) via atmospheric nitrogen oxidation:

$$\text{O} + \text{N}_2 \leftrightarrow \text{NO} + \text{N}$$
$$\text{N} + \text{O}_2 \leftrightarrow \text{NO} + \text{O}$$
$$\text{N} + \text{OH} \leftrightarrow \text{NO} + \text{H}$$

**Rate equation:**

$$\frac{d[NO]}{dt} = k_0 e^{-E_a/RT} \times [O_2]^{0.5} \times [N_2]$$

Where:
- $k_0$ = Pre-exponential factor
- $E_a$ = Activation energy ≈ 70,000 cal/mol
- $R$ = Universal gas constant
- $T$ = Absolute temperature (°R)

**Temperature sensitivity:**

NOx formation rate approximately doubles every 90°F above 2800°F.

**Exponential temperature dependence:**

At 3000°F vs. 2800°F (200°F increase):

$$\frac{Rate_{3000}}{Rate_{2800}} \approx e^{-70000/1.987 \times (1/3460 - 1/3260)} \approx 5.7 \times$$

**Primary control strategy:** Reduce peak flame temperature.

### Fuel NOx

**Formation from nitrogen compounds in fuel:**

Organic nitrogen in fuel (primarily residual oils, coal) oxidized during combustion:

$$\text{Fuel-N} + \text{O}_2 \rightarrow \text{NO}$$

**Fuel nitrogen content:**
- Natural gas: <1 ppm (negligible fuel NOx)
- No. 2 oil: 50-500 ppm (10-30% of total NOx)
- No. 6 oil: 0.2-0.5% by weight (50-80% of total NOx)
- Coal: 0.5-2.0% (60-90% of total NOx)

**Control strategy:** Fuel staging (create fuel-rich primary zone to reduce fuel-N to N₂)

### Prompt NOx

**Formation in fuel-rich flame zones:**

Hydrocarbon radicals react with atmospheric nitrogen:

$$\text{CH} + \text{N}_2 \rightarrow \text{HCN} + \text{N}$$
$$\text{HCN} + \text{O}_2 \rightarrow \text{NO} + \ldots$$

**Significance:**
- Minor contributor for natural gas (<10% of total)
- Occurs in fuel-rich zones regardless of temperature
- Difficult to control by temperature reduction alone

## Combustion Modification Techniques

### Flue Gas Recirculation (FGR)

**Operating principle:**

Recirculate portion of flue gas (10-30%) back to combustion air or fuel stream.

**FGR ratio:**

$$FGR\% = \frac{\dot{m}_{flue,recirculated}}{\dot{m}_{air}} \times 100$$

**Effects on combustion:**

1. **Reduces oxygen concentration:**
   - Dilutes combustion air with inert gases (CO₂, H₂O, N₂)
   - Lowers O₂ from 21% to 16-18% in mixture
   - Reduces oxidizer availability

2. **Increases heat capacity of mixture:**
   - Flue gas has higher $C_p$ than air
   - More energy required to heat mixture to flame temperature
   - Reduces peak temperature

3. **Reduces peak flame temperature:**

$$\Delta T_{reduction} = \frac{FGR \times C_{p,flue} \times (T_{flue} - T_{air})}{C_{p,mix} \times (1 + FGR)}$$

**Example:** 20% FGR, flue gas 450°F, combustion air 70°F

$$\Delta T \approx \frac{0.20 \times 0.26 \times 380}{0.25 \times 1.20} \approx 66°F$$

Adiabatic flame temperature reduced approximately 200-400°F with 20-30% FGR.

**NOx reduction effectiveness:**

$$\text{NOx}_{FGR} = \text{NOx}_{base} \times e^{-k \times FGR}$$

Where $k \approx 0.04-0.06$ depending on burner design.

For 20% FGR, $k = 0.05$:

$$\text{NOx}_{FGR} = \text{NOx}_{base} \times e^{-0.05 \times 20} = 0.368 \times \text{NOx}_{base}$$

**NOx reduction: 63%**

**FGR system configurations:**

**External FGR:**

**Components:**
- FGR fan (induced draft)
- Flue gas ductwork from stack to burner
- FGR damper (modulating control)
- Temperature control (cool flue gas if needed)

**FGR fan sizing:**

$$\dot{V}_{FGR} = \dot{V}_{air} \times FGR\%$$

For 10 MMBtu/h burner, 20% FGR:
- Combustion air: 1825 scfm
- FGR required: $1825 \times 0.20 = 365$ scfm (at flue gas temperature)

At 450°F flue gas:

$$\dot{V}_{FGR,actual} = 365 \times \frac{910}{520} = 639 \text{ acfm}$$

Fan static pressure: 4-10 in w.c. typical (ductwork + burner back pressure)

**FGR control:**
- Modulate FGR damper to maintain target FGR ratio
- Interlock with burner firing rate (proportional FGR)
- Temperature limit to prevent overheating burner

**Internal FGR (induced FGR):**

**Operating principle:**
- High-velocity combustion air creates low-pressure zone
- Induces furnace flue gases into burner without external fan
- Burner design feature (no external ductwork)

**Advantages:**
- No external FGR fan or ductwork
- Lower capital cost
- Simpler installation
- Lower maintenance

**Limitations:**
- FGR ratio lower (15-25% vs. up to 30% for external)
- Dependent on furnace pressure (requires slightly negative furnace)
- NOx reduction limited to 40-60% vs. up to 70% for external FGR

### Staged Combustion

**Air staging:**

**Primary combustion zone:**
- Sub-stoichiometric combustion (fuel-rich)
- Equivalence ratio $\phi = 1.3-1.8$
- Insufficient oxygen limits NOx formation
- Temperature moderate due to incomplete combustion

**Secondary combustion zone:**
- Downstream air injection (20-40% of total air)
- Completes combustion
- Lower temperature (already partially cooled products)
- Minimal NOx formation in secondary zone

**Overall equivalence ratio:**

$$\phi_{overall} = \frac{(\text{F/A})_{actual}}{(\text{F/A})_{stoichiometric}}$$

For lean overall combustion: $\phi_{overall} = 0.9-0.95$ (5-10% excess air)

**NOx reduction mechanism:**
- Primary zone: Low O₂ limits thermal NOx despite moderate temperature
- Secondary zone: Lower temperature limits thermal NOx despite O₂ available

**Reduction effectiveness:** 50-75% vs. conventional single-stage burner

**Fuel staging:**

**Primary combustion zone:**
- Majority of fuel (70-80%) burned with excess air
- Lean combustion ($\phi = 0.7-0.9$)
- Lower flame temperature

**Secondary combustion zone:**
- Remaining fuel (20-30%) injected downstream
- Reburning zone
- Reduces NOx formed in primary zone

**Reburning chemistry:**
Hydrocarbon radicals from secondary fuel reduce NO to N₂:

$$\text{NO} + \text{CH}_i \rightarrow \text{HCN} \rightarrow \text{N}_2$$

**Tertiary air:**
- Final air injection completes combustion
- Oxidizes CO and unburned hydrocarbons

**Reduction effectiveness:** 50-70%

### Ultra-Low NOx Burner Design

**Design features for ultra-low NOx (<30 ppm, <9 ppm for ultra-low):**

1. **Lean premix combustion:**
   - Fuel and air thoroughly premixed upstream
   - Operate lean ($\phi = 0.6-0.9$)
   - Uniform stoichiometry prevents local hot spots
   - Peak temperature reduced 200-400°F

2. **Surface stabilized combustion:**
   - Flame stabilized on porous ceramic or metal fiber matrix
   - Heat loss to surface further reduces gas temperature
   - Radiant emission from surface increases efficiency

3. **Delayed mixing:**
   - Fuel and air streams segregated initially
   - Gradual mixing along flame length
   - Avoids stoichiometric combustion at peak temperature
   - Creates distributed reaction zone

4. **Multiple flame zones:**
   - Burner divided into multiple small flames
   - Each zone operates lean
   - Distributed combustion reduces peak temperatures

5. **Internal flue gas recirculation:**
   - Burner induces FGR without external system
   - 15-25% effective FGR
   - Reduces O₂ concentration and temperature

**Control requirements:**

Ultra-low NOx burners require:
- Precise air-fuel ratio control (±2% accuracy)
- Oxygen trim mandatory
- Electronic control system
- High-quality fuel pressure regulation
- Wobbe index variation <±3%

**Performance:**

| Burner Design | NOx (ppm @ 3% O₂) | CO (ppm) | Turndown | Efficiency |
|---------------|-------------------|----------|----------|------------|
| Conventional | 80-150 | <50 | 5:1 | 82-85% |
| Low-NOx | 30-60 | <50 | 5:1-8:1 | 82-88% |
| Ultra-low NOx | 9-20 | <50 | 8:1-15:1 | 85-92% |
| Ultra-low (<9 ppm) | <9 | <50 | 10:1-20:1 | 85-92% |

### Water or Steam Injection

**Operating principle:**

Inject water or steam into combustion zone:
- Water evaporates, absorbing heat
- Steam increases heat capacity of mixture
- Peak flame temperature reduced

**Injection rate:**

$$\frac{\dot{m}_{water}}{\dot{m}_{fuel}} = 0.5 - 2.0 \text{ (mass ratio)}$$

Higher ratios achieve greater NOx reduction but increase efficiency penalty.

**Temperature reduction:**

Heat of vaporization of water:

$$Q_{evap} = \dot{m}_{water} \times h_{fg}$$

For water at 60°F injected into 3500°F flame:

$$Q = \dot{m}_{water} \times [h_{fg} + C_p(T_{flame} - T_{water})]$$

Approximately 1000 Btu/lb water:

$$\Delta T \approx \frac{\dot{m}_{water} \times 1000}{\dot{m}_{products} \times C_p}$$

**NOx reduction:**

Approximately 10-20% NOx reduction per water/fuel mass ratio of 1.0.

**Efficiency penalty:**

Water/steam carries away sensible heat in flue gas:

$$\eta_{loss} = \frac{\dot{m}_{water} \times C_p \times (T_{stack} - T_{ambient})}{Q_{input}}$$

Typical penalty: 1-3% efficiency loss

**Applications:**
- Emergency NOx control (temporary measure)
- Gas turbines (common)
- Boilers (less common due to efficiency penalty)
- Deprecated for modern installations (better methods available)

## Post-Combustion Treatment

### Selective Catalytic Reduction (SCR)

**Operating principle:**

Inject ammonia (NH₃) or urea upstream of catalyst bed. Catalyst promotes selective reaction of NH₃ with NOx to form N₂ and H₂O:

$$4\text{NH}_3 + 4\text{NO} + \text{O}_2 \rightarrow 4\text{N}_2 + 6\text{H}_2\text{O}$$
$$8\text{NH}_3 + 6\text{NO}_2 \rightarrow 7\text{N}_2 + 12\text{H}_2\text{O}$$

**Catalyst types:**

**Vanadium-titanium (V₂O₅/TiO₂):**
- Operating temperature: 450-850°F
- Most common for boilers and furnaces
- Tolerates some SO₂ and particulate
- Deactivation by ammonium bisulfate below 450°F

**Zeolite:**
- Operating temperature: 500-900°F
- Higher temperature capability
- Less SO₂ tolerance
- Used for gas turbines and engines

**Precious metal:**
- Operating temperature: 350-600°F
- Very active but expensive
- Low dust tolerance
- Specialty applications

**System components:**

1. **Ammonia/urea injection:**
   - Ammonia storage tank (anhydrous or aqueous)
   - Injection grid (uniform distribution critical)
   - Dilution air system
   - Flow control (proportional to NOx load)

2. **Static mixer:**
   - Ensures uniform NH₃ distribution
   - Located upstream of catalyst
   - Duct length: 10-20 duct diameters for complete mixing

3. **Catalyst reactor:**
   - Honeycomb or plate-type catalyst elements
   - Parallel flow channels minimize pressure drop
   - Multiple layers (2-4 typical) for high removal efficiency
   - Face velocity: 5-15 ft/s

4. **Catalyst support structure:**
   - Pressure vessel housing
   - Access doors for inspection/replacement
   - Insulation (maintain operating temperature)

**Ammonia-to-NOx molar ratio (NSR):**

$$NSR = \frac{\text{NH}_3 \text{ injected (mol)}}{\text{NOx} \text{ inlet (mol)}}$$

**Typical operating range:** NSR = 0.9-1.1

**NOx removal efficiency:**

$$\eta_{NOx} = \frac{NOx_{inlet} - NOx_{outlet}}{NOx_{inlet}} \times 100\%$$

**Typical performance:** 80-95% removal efficiency

**Example:**
- Inlet NOx: 100 ppm
- Target outlet: 9 ppm
- Required efficiency: $(100-9)/100 = 91\%$
- NSR required: Approximately 1.0

**Ammonia slip:**

Excess NH₃ not consumed ("slip") causes:
- Visible plume (white NH₃ vapor)
- Ammonium salt formation (fouling downstream equipment)
- Odor (detectable at 5-10 ppm)

**Typical slip target:** <5 ppm NH₃

**Trade-off:** Higher NSR → better NOx removal but higher slip

**Operating temperature control:**

**Temperature too low (<450°F typical):**
- Low catalyst activity
- Ammonium bisulfate formation: $\text{NH}_3 + \text{SO}_3 + \text{H}_2\text{O} \rightarrow \text{NH}_4\text{HSO}_4$
- Catalyst fouling and corrosion

**Temperature too high (>850°F typical):**
- Catalyst sintering (deactivation)
- NH₃ oxidation to NOx (counterproductive)

**Solution:**
- Locate SCR at proper point in flue gas path
- Or use auxiliary heating/cooling

**Pressure drop:**

Catalyst adds static pressure drop:

$$\Delta P_{catalyst} = 1-6 \text{ in w.c.}$$

Affects ID fan sizing and auxiliary power.

**Catalyst life and replacement:**

**Deactivation mechanisms:**
1. Thermal aging (sintering at high temperature)
2. Chemical poisoning (alkaline metals, phosphorus, arsenic)
3. Physical fouling (particulate blockage)
4. Ammonium salt formation (acid dew point operation)

**Typical catalyst life:** 3-5 years (boilers), 5-10 years (gas turbines with clean fuel)

**Replacement cost:** $100-300 per ft² of catalyst

**Performance monitoring:**
- NOx inlet/outlet (continuous)
- NH₃ slip (continuous or periodic)
- Pressure drop across catalyst (indicates fouling)
- Catalyst activity testing (annually)

### Selective Non-Catalytic Reduction (SNCR)

**Operating principle:**

Inject ammonia or urea into furnace at 1600-2100°F. Thermal reactions (no catalyst) reduce NOx:

$$4\text{NH}_3 + 4\text{NO} + \text{O}_2 \rightarrow 4\text{N}_2 + 6\text{H}_2\text{O}$$
$$4\text{NO} + 2\text{(NH}_2)_2\text{CO} + \text{O}_2 \rightarrow 4\text{N}_2 + 4\text{H}_2\text{O} + 2\text{CO}_2$$

(Urea reaction shown in second equation)

**Critical temperature window:**

**Optimal range: 1600-2100°F**

- Below 1600°F: Insufficient thermal energy for reactions, high NH₃ slip
- Above 2100°F: NH₃ oxidizes to NOx (counterproductive)

**Temperature sensitivity:** ±100°F significantly affects performance.

**System components:**

1. **Reagent storage and preparation:**
   - Aqueous ammonia (19-29%) or urea solution (20-50%)
   - Storage tank with level monitoring
   - Pump and flow control

2. **Injection system:**
   - Multiple injection lances at different elevations
   - Atomizing nozzles (compressed air or steam atomization)
   - Temperature-based injection control

3. **Control system:**
   - Flue gas temperature measurement (multiple points)
   - Select active injection level based on temperature
   - Modulate reagent flow proportional to NOx load

**NOx removal efficiency:**

**Typical: 30-70%** (lower than SCR)

**Example:**
- Inlet NOx: 150 ppm
- SNCR efficiency: 50%
- Outlet NOx: 75 ppm

**Normalized stoichiometric ratio (NSR):**

$$NSR = 1.5-2.5 \text{ (higher than SCR due to incomplete mixing)}$$

**Ammonia slip:** Typically 5-20 ppm (higher than SCR)

**Advantages vs. SCR:**
- Lower capital cost ($50-150/kW vs. $200-1000/kW for SCR)
- Retrofit easier (inject into existing furnace)
- No catalyst replacement
- Lower pressure drop (no catalyst pressure drop)

**Disadvantages vs. SCR:**
- Lower NOx removal efficiency
- Higher NH₃ slip
- Temperature window critical (difficult in cycling boilers)
- Not suitable for <50 ppm NOx targets

**Applications:**
- Utility boilers (coal, oil, gas)
- Industrial boilers where 40-60% reduction adequate
- Combined with combustion controls for overall compliance
- Sources without space for SCR catalyst

### Hybrid Systems (SNCR + SCR)

**Configuration:**
- SNCR injection in furnace (1600-2100°F zone)
- SCR catalyst in convection pass (450-850°F)

**Benefits:**
- SNCR provides 40-60% reduction
- SCR polishes to final target (<20 ppm)
- Smaller SCR catalyst than standalone
- Lower ammonia consumption than standalone SCR

**Economics:**
- Capital cost between SNCR-only and SCR-only
- Operating cost lower than standalone SCR (less catalyst replacement)

**Applications:**
- Utility boilers with stringent NOx limits
- Retrofit situations with space constraints
- Optimize capital vs. operating cost

## NOx Control Strategy Selection

### Regulatory Compliance Requirements

**U.S. EPA NSPS (New Source Performance Standards):**
- Subpart Dc (utility boilers >250 MMBtu/h): NOx limits 0.10-0.20 lb/MMBtu
- Subpart Db (industrial boilers): 0.10-0.30 lb/MMBtu depending on fuel
- RACT/BACT requirements vary by state

**California SCAQMD (South Coast Air Quality Management District):**
- Rule 1146.2 (boilers >2 MMBtu/h): 20 ppm @ 3% O₂ (after 2025: 9 ppm)
- Rule 1147 (process heaters): 20-40 ppm depending on category

**Bay Area AQMD:**
- Regulation 9-7: 30 ppm @ 3% O₂ for most sources

**Northeast states (RACT requirements):**
- Varies 30-60 ppm depending on size and fuel

### Selection Matrix

| NOx Limit | Control Technology | Removal Efficiency | Capital Cost | Operating Cost |
|-----------|-------------------|-------------------|--------------|----------------|
| >60 ppm | Conventional burner | Baseline | Baseline | Baseline |
| 40-60 ppm | Low-NOx burner | 30-50% | Low (+10-30%) | Minimal |
| 30-40 ppm | Low-NOx + FGR | 50-70% | Medium (+40-80%) | Moderate (fan power) |
| 20-30 ppm | ULN burner or FGR + Low-NOx | 60-80% | Medium-High (+60-120%) | Moderate |
| 9-20 ppm | ULN burner + O₂ trim | 70-85% | High (+80-150%) | Moderate |
| <9 ppm | ULN burner + SCR | 85-95% | Very High (+200-400%) | High (catalyst, NH₃) |

### Economic Analysis

**Capital cost estimates:**

**Burner replacement:**
- Low-NOx burner: $20,000-100,000 depending on size
- Ultra-low NOx burner: $50,000-200,000

**FGR system:**
- External FGR: $50,000-200,000 (fan, ductwork, controls)
- Internal FGR (burner feature): Included in burner cost

**SCR system:**
- Small boiler (5 MMBtu/h): $200,000-500,000
- Medium boiler (50 MMBtu/h): $1,000,000-3,000,000
- Large boiler (500 MMBtu/h): $5,000,000-20,000,000

**Operating costs:**

**FGR:**
- Fan power: 5-20 kW depending on size
- Annual cost: $2,000-10,000 at $0.10/kWh
- Maintenance: Minimal

**SCR:**
- Catalyst replacement: $50,000-500,000 every 3-5 years
- Ammonia consumption: $5,000-50,000/year depending on size
- Auxiliary power: $10,000-50,000/year
- Maintenance: $20,000-100,000/year

**Efficiency impact:**
- Low-NOx burner: Neutral to +1% (better mixing)
- FGR: -0.5 to -2% (higher stack losses)
- ULN burner: +1 to +3% (lean premix, high efficiency)
- SCR: -0.2 to -1% (pressure drop, heat loss to catalyst)

### Decision Flowchart

**Step 1: Determine required NOx limit (ppm @ 3% O₂)**

**Step 2: Evaluate combustion controls:**
- If limit >60 ppm: Standard burner may suffice
- If limit 30-60 ppm: Low-NOx burner or FGR
- If limit 9-30 ppm: Ultra-low NOx burner required
- If limit <9 ppm: SCR likely required

**Step 3: Assess retrofit constraints:**
- Space available for SCR catalyst reactor?
- Flue gas temperature in SCR range (450-850°F)?
- Budget for SCR capital and operating costs?

**Step 4: Consider fuel characteristics:**
- Natural gas: Thermal NOx dominant, combustion controls very effective
- Residual oil: Fuel NOx significant, staged combustion or SCR needed

**Step 5: Evaluate lifecycle cost:**
- Calculate total cost of ownership (capital + operating over 20 years)
- Consider emission reduction cost-effectiveness ($/ton NOx removed)

**Step 6: Select optimal strategy**

**Common outcomes:**
- <30 ppm, natural gas: Ultra-low NOx burner
- <20 ppm, natural gas: ULN burner + O₂ trim
- <9 ppm, natural gas: ULN burner + small SCR
- <30 ppm, residual oil: Low-NOx burner + FGR + fuel switching
- <20 ppm, residual oil: SCR required

**Best practice:** Maximize combustion controls effectiveness before adding post-combustion treatment. SCR should be final polishing step, not sole control method.
