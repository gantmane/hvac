---
title: "Flue Gas Analysis and Efficiency Testing"
weight: 6
description: "Engineering methodology for flue gas analysis including stack temperature measurement, oxygen and CO₂ analysis, CO monitoring, combustion efficiency calculations, stack loss determination, portable combustion analyzers, and continuous emissions monitoring systems (CEMS) for burner optimization."
keywords: "flue gas analysis, combustion efficiency, stack loss, oxygen analyzer, CO analyzer, combustion analyzer, CEMS, emissions testing, burner tuning"
---

# Flue Gas Analysis and Efficiency Testing

Flue gas analysis measures combustion products (O₂, CO₂, CO, NOx) and stack temperature to evaluate combustion efficiency, diagnose burner performance issues, and verify emissions compliance. Comprehensive combustion analysis enables calculating thermal efficiency via stack loss method (typical results 80-92%), optimizing air-fuel ratio for target oxygen levels (2-4% O₂ typical), identifying incomplete combustion through CO measurement (<50 ppm target), and trending performance to detect fouling or misadjustment. Modern portable combustion analyzers provide real-time measurements enabling field adjustment, while permanent continuous emissions monitoring systems (CEMS) track performance and document regulatory compliance for industrial installations.

## Measured Parameters

### Stack Temperature

**Measurement location:**
- Downstream of heat exchanger
- Minimum 8 duct diameters from outlet
- Centerline of stack
- Above condensation temperature (>250°F for gas, >300°F for oil)

**Temperature measurement devices:**

**Type K thermocouple:**
- Range: 0-2000°F
- Accuracy: ±0.75% or 2°F
- Response time: 1-5 seconds
- Most common for combustion testing

**RTD (resistance temperature detector):**
- Range: 0-800°F typically
- Accuracy: ±0.5°F
- Slower response than thermocouple
- Better long-term stability

**Stack temperature significance:**

**Gross stack temperature:** Absolute temperature measured in stack.

**Net stack temperature:** Temperature rise above combustion air:

$$\Delta T_{stack} = T_{stack} - T_{air}$$

This is the temperature relevant to efficiency calculations.

**Typical stack temperatures:**

| System Type | Stack Temp (°F) | Net Temp Rise (°F) |
|-------------|-----------------|---------------------|
| Condensing boiler | 100-160 | 40-100 |
| High-efficiency boiler | 250-350 | 180-280 |
| Standard efficiency boiler | 350-500 | 280-430 |
| Process heater | 450-800 | 380-730 |
| Poor performance | >600 | >500 |

### Oxygen (O₂) Analysis

**Measurement principle:**

**Zirconia sensor:**
- Operating temperature: 600-1500°F
- Electrochemical reaction generates voltage proportional to O₂ partial pressure difference
- Fast response: 5-15 seconds
- Accuracy: ±0.1-0.3% O₂
- Most common for combustion control

**Electrochemical sensor:**
- Operating temperature: 300-600°F
- Galvanic cell generates current proportional to O₂
- Response time: 10-30 seconds
- Accuracy: ±0.2-0.5% O₂
- Used in portable analyzers

**Paramagnetic analyzer:**
- Laboratory/CEMS quality
- Accuracy: ±0.1% O₂
- Expensive, high maintenance
- Rarely used in field

**Oxygen content interpretation:**

**Dry basis vs. wet basis:**
- Dry: Water vapor removed before measurement
- Wet: Water vapor included
- Most analyzers measure dry O₂

**Typical O₂ ranges:**

- 0-1%: Too little excess air, incomplete combustion, CO formation risk
- 1.5-4%: Optimal range for most burners
- 4-7%: Acceptable but lower efficiency
- >7%: Excessive excess air, efficiency loss

**Excess air from O₂:**

$$EA\% = \frac{O_2}{21 - O_2} \times 100$$

**CO₂ measurement (alternative to O₂):**

**Natural gas stoichiometric CO₂:** 11.8% (dry basis)

**Actual CO₂:**

$$CO_2\% = \frac{CO_{2,max}}{1 + EA}$$

For natural gas:

$$CO_2\% = \frac{11.8}{1 + EA}$$

**Relationship between O₂ and CO₂ (natural gas):**

$$O_2 + 0.5 \times CO_2 \approx 10.5\% \text{ (for natural gas)}$$

### Carbon Monoxide (CO) Analysis

**Measurement principle:**

**Electrochemical sensor:**
- CO oxidizes at electrode, generates current
- Linear response 0-2000 ppm typical
- Accuracy: ±5% of reading or ±10 ppm
- Response time: 30-60 seconds

**Non-dispersive infrared (NDIR):**
- IR absorption at 4.6 μm wavelength
- High accuracy: ±1% of reading
- Used in laboratory and CEMS
- Expensive

**CO significance:**

**CO formation mechanisms:**
1. Insufficient oxygen (inadequate combustion air)
2. Poor air-fuel mixing
3. Flame quenching (cold surfaces)
4. Incomplete residence time

**Acceptable CO levels:**

- <50 ppm: Excellent combustion
- 50-100 ppm: Acceptable for most applications
- 100-400 ppm: Needs adjustment
- >400 ppm: Poor combustion, immediate correction required

**Air-free CO:**

Some analyzers report "air-free CO" corrected to 0% O₂:

$$CO_{air-free} = CO_{measured} \times \frac{21}{21 - O_2}$$

This normalizes readings to account for dilution air.

### Nitrogen Oxides (NOx)

**Measurement principle:**

**Chemiluminescence:**
- NO reacts with ozone, produces light
- Light intensity proportional to NO concentration
- NO₂ converted to NO upstream
- High accuracy, used for CEMS and testing
- Expensive, requires calibration gas

**Electrochemical sensor:**
- Portable analyzer option
- Lower accuracy than chemiluminescence
- Adequate for field verification

**NOx reporting:**

**Concentration basis:**
Typically reported in ppm by volume (dry basis).

**Corrected to standard O₂:**

Regulations specify reference O₂ (3% for boilers):

$$NOx_{@3\%O_2} = NOx_{measured} \times \frac{18}{21 - O_{2,measured}}$$

**Example:** 45 ppm NOx measured at 5% O₂

$$NOx_{@3\%O_2} = 45 \times \frac{18}{16} = 50.6 \text{ ppm}$$

**Emission rate (mass basis):**

$$E_{NOx} = NOx_{ppm} \times \frac{Q_{input}}{K}$$

Where $K$ = Conversion factor (depends on fuel, approximately 10⁶ for natural gas in units of ppm·Btu/h per lb/h)

## Combustion Efficiency Calculation

### Stack Loss Method

**Overall efficiency:**

$$\eta = 100\% - L_{stack} - L_{radiation} - L_{incomplete}$$

**Stack loss (dominant term):**

$$L_{stack} = \frac{(T_{stack} - T_{air}) \times C_p \times m_{flue}}{Q_{input}}$$

**Simplified stack loss using flue gas CO₂:**

$$L_{stack} = K \times \frac{T_{stack} - T_{air}}{CO_2\%}$$

Where $K$ = fuel constant:
- Natural gas: $K = 0.65$
- No. 2 oil: $K = 0.54$
- Propane: $K = 0.63$

**Example calculation:**

Natural gas burner:
- Stack temperature: 450°F
- Air temperature: 70°F
- CO₂: 9.0%

$$L_{stack} = 0.65 \times \frac{450 - 70}{9.0} = 27.4\%$$

**Alternative oxygen-based stack loss:**

Siegert formula:

$$L_{stack} = A_1 \times \frac{T_{stack} - T_{air}}{CO_{2,max} - CO_2} + A_2 \times \frac{CO}{CO_2}$$

For natural gas: $A_1 = 0.66$, $CO_{2,max} = 11.8\%$

**Radiation and convection loss:**

Function of boiler/furnace size and surface area:

- Small residential (<350,000 Btu/h): 2-4%
- Commercial (1-10 MMBtu/h): 0.5-2%
- Large industrial (>10 MMBtu/h): 0.2-1%

Measured by:

$$L_{rad} = \frac{Q_{input,on} - Q_{input,off}}{Q_{input,on}}$$

Requires comparing input with burner cycling.

**Incomplete combustion loss:**

$$L_{incomplete} \approx 10.2 \times \frac{CO_{ppm}}{CO_{2\%}}$$

For CO = 100 ppm, CO₂ = 9%:

$$L_{incomplete} = 10.2 \times \frac{100}{9} = 0.11\%$$

Usually negligible if CO <100 ppm.

**Total efficiency example:**

$$\eta_{total} = 100 - 27.4 - 1.0 - 0.1 = 81.5\%$$

### Efficiency Optimization

**Target oxygen level:**

Trade-off between stack loss and incomplete combustion:
- Lower O₂ → less excess air → lower stack loss
- But too low O₂ → CO formation → incomplete combustion loss

**Optimal O₂ determination:**

1. Measure efficiency at several O₂ levels (1%, 2%, 3%, 4%, 5%)
2. Plot efficiency vs. O₂
3. Select O₂ giving maximum efficiency with CO <50 ppm

**Typical optimal O₂:**
- Natural gas: 2.5-3.5%
- No. 2 oil: 3.0-4.0%
- No. 6 oil: 3.5-5.0%

**Efficiency sensitivity:**

Approximately 1% efficiency change per:
- 40°F stack temperature change
- 1% O₂ change (at typical stack temperatures 350-450°F)

## Portable Combustion Analyzers

### Analyzer Components

**Typical portable analyzer includes:**

1. **Sampling probe:**
   - Stainless steel construction
   - Thermocouple integrated
   - Sintered metal filter prevents particulate damage
   - Length: 12-48 inches

2. **Sample conditioning:**
   - Water trap condenses and removes moisture
   - Particulate filter
   - Sample pump draws flue gas

3. **Sensors:**
   - O₂: Electrochemical or zirconia
   - CO: Electrochemical
   - NO/NO₂: Electrochemical (if included)
   - Stack temperature: Thermocouple

4. **Display and processor:**
   - Digital display of measurements
   - Calculates efficiency automatically
   - Data logging capability
   - Printer output (some models)

### Measurement Procedure

**Pre-test preparation:**

1. Verify analyzer calibration (fresh air O₂ should read 20.9%)
2. Check battery charge
3. Prepare sampling location (drill hole if needed)
4. Allow burner to reach steady-state operation (15-30 minutes)

**Sampling procedure:**

1. **Insert probe:** Position in stack centerline, downstream of heat exchanger
2. **Purge analyzer:** Allow 60-120 seconds for readings to stabilize
3. **Record ambient temperature:** For net temperature calculation
4. **Record readings:** O₂, CO, CO₂, stack temperature
5. **Calculate efficiency:** Analyzer performs calculation
6. **Document results:** Record firing rate, fuel type, date, time

**Multiple point sampling:**

For large stacks, traverse multiple points:
- Minimum 3 points: Center, 25% and 75% of diameter
- Average readings for accurate result

### Diagnostic Interpretation

**High O₂ (>5%):**
- Excessive combustion air
- Air leak in furnace (post-combustion air infiltration)
- Fuel valve restricted (low fuel flow)
- **Corrective action:** Reduce air damper opening, check for air leaks

**Low O₂ (<2%):**
- Insufficient combustion air
- Air damper stuck or restricted
- Fuel valve leaking (excessive fuel)
- **Corrective action:** Increase air damper opening, check air supply

**High CO (>100 ppm):**
- Insufficient oxygen
- Poor air-fuel mixing
- Flame impingement on heat exchanger
- Burner needs cleaning
- **Corrective action:** Increase air, inspect burner, clean heat exchanger

**High stack temperature (>500°F gas, >600°F oil):**
- Excessive firing rate
- Heat exchanger fouled (soot, scale)
- Insufficient heat transfer surface
- Bypass damper open
- **Corrective action:** Clean heat exchanger, check dampers, verify proper sizing

**Low stack temperature (<250°F gas, <300°F oil):**
- Excessive excess air (dilution)
- Oversized boiler (cycling)
- Heat exchanger very clean (good condition)
- May indicate condensation risk if <180°F
- **Corrective action:** Reduce excess air if too high

## Continuous Emissions Monitoring Systems (CEMS)

### System Components

**CEMS for combustion sources:**

1. **Sample extraction system:**
   - Heated sample line (prevents condensation)
   - Sample probe with filter
   - Sample pump
   - Pressure and temperature compensation

2. **Gas conditioning:**
   - Refrigerated condenser removes water
   - Particulate filter
   - Sample pressure control
   - Flow meter

3. **Gas analyzers:**
   - O₂: Zirconia or paramagnetic
   - CO: NDIR
   - NOx: Chemiluminescence
   - SO₂: NDIR (if applicable)

4. **Data acquisition system (DAS):**
   - Records all measurements
   - Calculates emission rates
   - Stores data per regulatory requirements (often 5 years)
   - Provides reports

### Regulatory Applications

**EPA regulations requiring CEMS:**

**40 CFR Part 60 (NSPS - New Source Performance Standards):**
- Large boilers >250 MMBtu/h
- Requires continuous monitoring of O₂, NOx, opacity

**40 CFR Part 75 (Acid Rain Program):**
- Electric utility boilers
- NOx, SO₂, CO₂ monitoring required
- Very stringent data quality requirements

**State/local air quality districts:**
- Vary by jurisdiction
- May require CEMS for sources >10-50 MMBtu/h in non-attainment areas

**CEMS data reporting:**

**1-hour average:** Rolling average reported
**Daily calibration:** Automated zero and span gas checks
**Quarterly audits:** Relative accuracy test audit (RATA)
**Annual reports:** Submitted to regulatory agency

### Quality Assurance

**Calibration procedures:**

**Daily calibration drift (CD):**
- Automated zero and upscale gas checks
- Performed every 24 hours
- Acceptance criteria: <5% of span

**Linearity check:**
- Quarterly
- Inject 3-5 calibration gases spanning range
- Verify linear response

**Relative Accuracy Test Audit (RATA):**
- Annual or quarterly (depends on source)
- Reference method testing concurrent with CEMS
- Calculate relative accuracy:

$$RA = \frac{|\text{CEMS}_{avg} - \text{Reference}_{avg}|}{\text{Reference}_{avg}} \times 100\%$$

Acceptance: RA <10% typical (varies by pollutant)

**Data validation:**

- Invalid data flagged (out of range, failed calibration)
- Substitute data methods per regulation
- Downtime tracked and reported

## Field Testing Procedure Summary

### Standard Combustion Test

**Objective:** Measure combustion efficiency and verify proper burner operation.

**Equipment needed:**
- Portable combustion analyzer
- Drill and hole saw (if no test port exists)
- Manometer (verify draft)
- Thermometer (measure ambient air temperature)

**Test procedure:**

1. **Pre-test verification:**
   - Burner operating ≥15 minutes (steady state)
   - Verify normal operating conditions
   - Note firing rate or manifold pressure

2. **Measurements:**
   - Ambient air temperature
   - Stack temperature
   - O₂ or CO₂
   - CO
   - Draft (if applicable)

3. **Calculations:**
   - Net stack temperature
   - Excess air
   - Combustion efficiency
   - CO air-free

4. **Documentation:**
   - Record all readings
   - Calculate efficiency
   - Compare to baseline or specification
   - Recommend adjustments if needed

**Acceptance criteria:**

- Efficiency ≥80% (standard boiler), ≥90% (condensing)
- CO <100 ppm (preferably <50 ppm)
- O₂ in range 2-5% depending on burner type
- Stack temperature appropriate for equipment type

**Frequency:**

- Commissioning: Required
- Annual: Recommended minimum
- Quarterly: Best practice for critical equipment
- After service: Always verify combustion

### Burner Tuning Optimization

**Objective:** Adjust air-fuel ratio for maximum efficiency with safe operation.

**Procedure:**

1. **Measure baseline:**
   - Record O₂, CO, stack temp, efficiency at current settings

2. **Adjust air damper:**
   - Reduce air slightly (close damper 5-10%)
   - Wait 2-3 minutes for stabilization
   - Record new readings

3. **Find optimal point:**
   - Continue adjusting air in small increments
   - Monitor CO: Must stay <100 ppm
   - Find lowest O₂ with acceptable CO
   - This gives maximum efficiency

4. **Verify across firing range:**
   - Check combustion at low, mid, high fire (modulating burners)
   - Adjust cam or control curve if needed
   - Ensure O₂ and CO acceptable across full range

5. **Set oxygen trim (if equipped):**
   - Enable O₂ trim control
   - Set target O₂ setpoint
   - Verify trim maintains setpoint ±0.3%

6. **Final verification:**
   - Record final settings
   - Calculate efficiency improvement
   - Document in maintenance log

**Safety note:** Never adjust to achieve O₂ <1.5% or CO >100 ppm for sake of efficiency. Safety and complete combustion always paramount.
