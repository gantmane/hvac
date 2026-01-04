---
title: "Combustion Air Requirements"
weight: 5
description: "Engineering analysis of combustion air requirements including stoichiometric air calculations, excess air determination, combustion air fan sizing, air temperature effects on combustion, infiltration air vs. ducted air, and makeup air system design for commercial and industrial burners."
keywords: "combustion air, stoichiometric air, excess air, combustion air fan, air temperature effects, makeup air, ventilation air, NFPA 54, combustion air openings"
---

# Combustion Air Requirements

Combustion air supply must provide sufficient oxygen for complete fuel oxidation while preventing dangerous oxygen-deficient conditions, maintaining burner performance, and meeting code requirements. Proper combustion air design requires calculating stoichiometric air requirements (9.52 ft³/ft³ for natural gas, 1368 ft³/gal for No. 2 oil), determining excess air based on burner type and efficiency targets, sizing air supply fans or openings, accounting for air temperature effects on combustion and density, and integrating combustion air with building ventilation per NFPA 31, 54, and 86. Inadequate combustion air causes incomplete combustion (high CO), sooting, reduced efficiency, and potential safety hazards including flame rollout and appliance spillage.

## Stoichiometric Air Requirements

### Theoretical Air for Complete Combustion

**Natural gas (methane):**

$$\text{CH}_4 + 2\text{O}_2 + 7.52\text{N}_2 \rightarrow \text{CO}_2 + 2\text{H}_2\text{O} + 7.52\text{N}_2$$

**Molar basis:**

$$\frac{n_{air}}{n_{CH_4}} = \frac{2}{0.21} = 9.52 \text{ mol air/mol CH}_4$$

**Volumetric basis (at standard conditions):**

$$A_s = 9.52 \text{ scf air/scf CH}_4$$

**Mass basis:**

$$A_s = \frac{2 \times 32 \text{ lb O}_2}{16 \text{ lb CH}_4} \times \frac{1}{0.2315} = 17.2 \text{ lb air/lb CH}_4$$

**For 1000 Btu/ft³ natural gas:**

$$A_s = 9.52 \text{ scf air/scf gas} = 0.00952 \text{ scf air/Btu}$$

**No. 2 fuel oil (typical composition C₁₂H₂₃):**

$$\text{C}_{12}\text{H}_{23} + 17.375\text{O}_2 \rightarrow 12\text{CO}_2 + 11.5\text{H}_2\text{O}$$

**Volumetric basis:**

For No. 2 oil at 7.0 lb/gal:

$$A_s = 1368 \text{ scf air/gal oil} \approx 195 \text{ scf air/lb oil}$$

**Mass basis:**

$$A_s = 13.8 \text{ lb air/lb oil}$$

**For 140,000 Btu/gal No. 2 oil:**

$$A_s = 1368 \text{ scf air/gal} = 0.00977 \text{ scf air/Btu}$$

**Propane:**

$$\text{C}_3\text{H}_8 + 5\text{O}_2 \rightarrow 3\text{CO}_2 + 4\text{H}_2\text{O}$$

$$A_s = 23.8 \text{ scf air/scf propane} = 15.7 \text{ lb air/lb propane}$$

**For 2500 Btu/ft³ propane:**

$$A_s = 0.00952 \text{ scf air/Btu}$$

### Excess Air Requirements

Actual combustion requires air beyond stoichiometric:

$$A_{actual} = A_s \times (1 + EA)$$

Where $EA$ = Excess air fraction

**Excess air percentage:**

$$EA\% = \frac{A_{actual} - A_s}{A_s} \times 100$$

**Reasons for excess air:**

1. **Non-ideal mixing:** Fuel and air don't mix perfectly; extra air ensures all fuel finds oxygen
2. **Flame stability:** Some excess air needed for stable combustion across firing range
3. **Safety margin:** Prevents fuel-rich conditions that cause CO and smoke
4. **Burner design limitations:** Different burner types achieve different mixing quality

**Typical excess air by burner type:**

| Burner Type | Excess Air | O₂ (%) | Application |
|-------------|-----------|--------|-------------|
| Atmospheric gas | 40-50% | 6-8% | Residential furnaces |
| Power gas | 10-20% | 1.5-3.5% | Commercial boilers |
| Premix gas | 5-15% | 0.8-2.5% | High-efficiency boilers |
| Gun-type oil | 20-30% | 3.5-5% | Residential/light commercial |
| Rotary oil | 15-25% | 2.5-4.5% | Commercial/industrial |
| Steam atomizing oil | 10-20% | 1.5-3.5% | Industrial boilers |

**Relationship to oxygen content:**

$$O_2\% = \frac{21 \times EA}{1 + EA}$$

**Example:** 15% excess air

$$O_2\% = \frac{21 \times 0.15}{1.15} = 2.74\%$$

**Reverse calculation:**

$$EA = \frac{O_2}{21 - O_2}$$

**Example:** 3% O₂ measured

$$EA = \frac{3}{21-3} = 0.167 = 16.7\%$$

## Combustion Air Quantity Calculations

### Total Air Requirement

**For natural gas firing:**

$$\dot{V}_{air} = \frac{Q_{input}}{HHV_{gas}} \times A_s \times (1 + EA)$$

Where:
- $Q_{input}$ = Burner heat input (Btu/h)
- $HHV_{gas}$ = Higher heating value (Btu/scf), typically 1000 Btu/scf
- $A_s$ = Stoichiometric air (scf/scf)
- $EA$ = Excess air fraction

**Simplified form for natural gas:**

$$\dot{V}_{air} = Q_{Btu/h} \times 0.00952 \times (1 + EA)$$

For 15% excess air:

$$\dot{V}_{air} = Q_{Btu/h} \times 0.01095 \text{ scfh}$$

**Example:** 10 MMBtu/h natural gas burner, 15% excess air

$$\dot{V}_{air} = 10,000,000 \times 0.01095 = 109,500 \text{ scfh} = 1825 \text{ scfm}$$

**For fuel oil firing:**

$$\dot{V}_{air} = GPH \times 1368 \times (1 + EA)$$

For 20% excess air:

$$\dot{V}_{air} = GPH \times 1642 \text{ scfh}$$

**Example:** 10 MMBtu/h No. 2 oil burner (71.4 gph), 20% excess air

$$\dot{V}_{air} = 71.4 \times 1642 = 117,200 \text{ scfh} = 1953 \text{ scfm}$$

### Air Density Corrections

Standard conditions: 60°F, 14.7 psia, dry air

**Actual air density:**

$$\rho_{air} = \rho_{std} \times \frac{P_{actual}}{P_{std}} \times \frac{T_{std}}{T_{actual}}$$

Where:
- $\rho_{std} = 0.0764$ lb/ft³ at 60°F, 14.7 psia
- $P$ = Absolute pressure (psia)
- $T$ = Absolute temperature (°R = °F + 460)

**Actual volume flow rate:**

$$\dot{V}_{actual} = \dot{V}_{standard} \times \frac{T_{actual}}{T_{std}} \times \frac{P_{std}}{P_{actual}}$$

**Example:** Standard air flow 1825 scfm at 60°F, actual air temperature 100°F

$$\dot{V}_{actual} = 1825 \times \frac{560}{520} = 1965 \text{ acfm}$$

**Density impact on fan sizing:** Fan must deliver actual cfm at operating temperature, not standard cfm.

### Altitude Corrections

Air density decreases with altitude:

$$\rho_{alt} = \rho_{SL} \times e^{-\frac{h}{29,000}}$$

Where $h$ = Altitude (ft)

**Approximate correction:**

| Altitude (ft) | Pressure Ratio | Density Ratio | Air Volume Increase |
|---------------|----------------|---------------|---------------------|
| 0 (sea level) | 1.00 | 1.00 | 0% |
| 1,000 | 0.964 | 0.964 | 3.7% |
| 2,500 | 0.917 | 0.917 | 9.1% |
| 5,000 | 0.832 | 0.832 | 20.2% |
| 7,500 | 0.753 | 0.753 | 32.8% |
| 10,000 | 0.681 | 0.681 | 46.8% |

**Burner derating at altitude:**

Atmospheric burners aspirate less air at altitude (lower density). Burner capacity must be derated or air supply adjusted.

**Power burners:** Fan can maintain mass flow by increasing volume flow. Control system must compensate for density change.

## Combustion Air Supply Methods

### Infiltration Air (Atmospheric Burners)

**NFPA 54 (National Fuel Gas Code) requirements:**

**Standard method (indoor combustion air):**

All air from inside building space:

$$A_{opening} = \frac{Q_{input}}{1000} \times 50 \text{ in}^2\text{/opening}$$

Two openings required:
- One within 12 in of ceiling
- One within 12 in of floor
- Each opening minimum 50 in² per 1000 Btu/h input

**Example:** 100,000 Btu/h furnace

$$A_{opening} = \frac{100,000}{1000} \times 50 = 5000 \text{ in}^2 = 34.7 \text{ ft}^2 \text{ per opening}$$

Two 35 ft² openings required (e.g., two 6 ft × 6 ft openings).

**Known air infiltration method:**

If space has adequate infiltration (≥0.40 ACH):

$$A_{opening} = \frac{Q_{input}}{1000} \times 21 \text{ in}^2\text{/opening}$$

**Outdoor air via vertical ducts:**

Ducts connected to outdoors:

$$A_{duct} = \frac{Q_{input}}{4000} \text{ ft}^2\text{/duct}$$

Two ducts required (high and low).

**Outdoor air via horizontal ducts:**

$$A_{duct} = \frac{Q_{input}}{2000} \text{ ft}^2\text{/duct}$$

Two ducts required.

**Direct outdoor connection (single opening):**

$$A_{opening} = \frac{Q_{input}}{4000} \text{ ft}^2$$

### Forced Air Supply (Power Burners)

**Combustion air fan sizing:**

**Required air mass flow:**

$$\dot{m}_{air} = \frac{Q_{input}}{HHV} \times A_s \times (1 + EA) \times \rho_{air}$$

**Required fan volume:**

$$\dot{V}_{fan} = \frac{\dot{m}_{air}}{\rho_{air,actual}} = \dot{V}_{standard} \times \frac{T_{air}}{520} \times \frac{14.7}{P_{air}}$$

**Fan static pressure:**

1. **Burner pressure drop:** 1-10 in w.c. (varies by burner type)
   - Atmospheric inspirators: 0 (negative pressure)
   - Power burners: 2-6 in w.c.
   - Industrial burners: 4-10 in w.c.

2. **Ductwork losses:**

$$\Delta P_{duct} = f \times \frac{L}{D} \times \frac{\rho V^2}{2 g_c}$$

   Typical: 0.5-3.0 in w.c. depending on duct length/complexity

3. **Inlet/outlet losses:** 0.2-1.0 in w.c.

4. **Filter (if used):** 0.2-1.0 in w.c. (clean), up to 2.0 in w.c. (dirty)

**Total static pressure:**

$$P_{fan} = P_{burner} + P_{duct} + P_{inlet/outlet} + P_{filter} + \text{margin}$$

Margin: 10-25% for safety and system variations

**Example fan sizing:**

10 MMBtu/h burner:
- Air required: 1825 scfm @ 60°F
- Air temperature: 80°F
- Burner drop: 4.0 in w.c.
- Duct losses: 1.5 in w.c.
- Inlet: 0.5 in w.c.
- Margin: 20%

$$\dot{V}_{actual} = 1825 \times \frac{540}{520} = 1895 \text{ acfm}$$

$$P_{total} = (4.0 + 1.5 + 0.5) \times 1.20 = 7.2 \text{ in w.c.}$$

**Fan selection:** 1900 cfm @ 7.5 in w.c.

### Dedicated Combustion Air vs. Building Air

**Dedicated outdoor air (recommended for commercial/industrial):**

**Advantages:**
- Consistent air temperature
- No interaction with building HVAC
- No depressurization concerns
- Code-compliant
- Predictable performance

**Components:**
- Outdoor air intake with screen/louver
- Ductwork to burner (insulated if needed)
- Combustion air fan (integral to burner)
- Backdraft damper (prevent reverse flow when off)

**Building air (common for smaller systems):**

**Advantages:**
- Lower installation cost
- Warmer air (better efficiency in cold climates)
- Simpler installation

**Disadvantages:**
- Competes with building exhaust systems
- May depressurize building
- Variable air temperature
- Makeup air required

## Air Temperature Effects

### Impact on Combustion Efficiency

**Sensible heat in combustion air:**

Preheated air reduces fuel required to reach flame temperature:

$$\Delta Q = \dot{m}_{air} \times C_p \times (T_{air} - T_{reference})$$

**Effect on efficiency:**

$$\eta_{increased} = \eta_{base} + \frac{\dot{m}_{air} C_p (T_{air} - T_{ref})}{Q_{input}}$$

**Example:** 10 MMBtu/h burner, increase air from 60°F to 200°F

$$\dot{m}_{air} = \frac{109,500 \times 0.0764}{60} = 139.4 \text{ lb/min}$$

$$\Delta Q = 139.4 \times 0.24 \times (200-60) = 4683 \text{ Btu/min} = 281,000 \text{ Btu/h}$$

$$\eta_{increase} = \frac{281,000}{10,000,000} = 2.81\%$$

**Preheated air benefit:** Approximately 1% efficiency improvement per 50°F air preheat.

**Practical combustion air preheat:**

**Small systems (<5 MMBtu/h):**
- Use building air (typically 60-75°F)
- Minimal preheat benefit
- Not economical to preheat

**Large systems (>20 MMBtu/h):**
- Air-to-air heat recovery economical
- Preheat to 200-400°F via stack heat recovery
- Payback: 2-5 years
- Efficiency improvement: 3-8%

### Cold Air Challenges

**Problems with very cold combustion air (<20°F):**

1. **Reduced adiabatic flame temperature:**
   - Lower flame temperature reduces heat transfer
   - May affect burner stability

2. **Condensation in fuel supply:**
   - Cold air chills gas piping
   - Moisture in gas may condense
   - Freeze damage risk

3. **Increased draft requirements:**
   - Cold dense air increases pressure drop
   - Fan may require higher capacity

4. **Thermal stress:**
   - Cold air on hot refractory
   - Rapid temperature changes cause cracking

**Solutions:**

- Insulate combustion air duct
- Heat trace gas piping in cold climates
- Mix outdoor air with building air
- Provide air preheat for very cold climates (<0°F)

## Makeup Air Integration

### Building Depressurization

**Depressurization mechanism:**

Combustion air + flue gases exit building → building pressure drops below atmospheric.

**Depressurization calculation:**

$$Q_{exhaust} = Q_{combustion,air} + Q_{fuel,volume}$$

For gas: $Q_{exhaust} \approx 1.1 \times Q_{combustion,air}$

**Example:** 10 MMBtu/h burner

Combustion air: 1825 cfm
Fuel: $10,000 / 1000 = 10$ cfm
Flue products: $\approx 1825 + 1.1 \times 10 = 1836$ cfm

If building exhaust fans total 2000 cfm, and combustion air from building:

**Net building exhaust:** $1836 + 2000 = 3836$ cfm

**Makeup air required:** 3836 cfm to maintain neutral pressure.

**Consequences of depressurization:**

1. **Backdrafting of naturally-vented appliances:**
   - Water heaters, furnaces may spill combustion products
   - CO hazard

2. **Difficulty opening doors:** Pressure differential resists opening

3. **Increased infiltration:** Cold air pulled through all cracks

4. **Reduced combustion air:** Air hunger affects burner performance

### Makeup Air System Design

**Makeup air requirement:**

$$\dot{V}_{MUA} = \dot{V}_{exhaust,total} - \dot{V}_{infiltration}$$

Conservative design: Assume infiltration = 0, provide 100% makeup air.

**Makeup air unit components:**

1. **Intake hood:** Outdoor air with screen, damper
2. **Heating coil:** Direct-fired or indirect (only if needed)
3. **Fan:** Constant volume or variable
4. **Controls:** Interlocked with exhaust systems

**Makeup air heating:**

**Unheated makeup air (tempering only):**
- Mixed with building air to avoid cold drafts
- Discharge temperature: 55-65°F typical
- Heating penalty on building HVAC system

**Heated makeup air:**
- Directly-fired gas makeup air unit: 80-90% efficiency
- Discharge temperature: 65-110°F
- Offsets building heating load

**Heating capacity required:**

$$Q_{MUA} = \dot{V}_{MUA} \times \rho_{air} \times C_p \times (T_{discharge} - T_{outdoor})$$

**Example:** 4000 cfm makeup air, heat from 0°F to 70°F

$$Q_{MUA} = 4000 \times 60 \times 0.075 \times 0.24 \times 70 = 756,000 \text{ Btu/h}$$

**Control strategies:**

1. **Constant volume:** Makeup air runs continuously when burner/exhaust on
2. **Variable volume:** Makeup air modulates to maintain building pressure
3. **Demand-based:** Makeup air matches actual exhaust flow

**Building pressure control:**

- Pressure sensor in building space
- Setpoint: -0.02 to -0.05 in w.c. (slight negative acceptable)
- Modulating damper or VFD fan adjusts makeup air
- Maintains comfortable conditions, prevents backdrafting

## Code Requirements Summary

**NFPA 31 (Oil-Burning Equipment):**
- Combustion air openings per standard method or engineered calculation
- Louvers sized for free area accounting for blockage
- Connection to unconfined space or outdoors

**NFPA 54 (Gas Equipment):**
- Standard method, known air method, or engineered calculation
- Dedicated outdoor air preferred
- Makeup air for commercial kitchens, exhaust hoods

**NFPA 86 (Industrial Ovens and Furnaces):**
- Forced combustion air supply required
- Positive combustion air proving (pressure switch)
- Interlock combustion air fan with fuel supply

**IMC (International Mechanical Code):**
- Follows NFPA 54 for gas, NFPA 31 for oil
- Additional requirements for commercial cooking equipment
- Makeup air required when exhaust >400 cfm (some jurisdictions)

**Compliance verification:**

1. Calculate combustion air requirement
2. Determine supply method (infiltration, ducted outdoor, forced)
3. Size openings/ducts per applicable code
4. Verify makeup air provided if needed
5. Commission and verify adequate air via combustion analysis
