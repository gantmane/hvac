---
title: "Combustion Analysis"
aliases: ["Combustion Analysis"]
description: "Comprehensive guide to boiler combustion analysis including flue gas measurement, efficiency calculations, excess air optimization, and tuning procedures for peak performance."
keywords: ["combustion analysis", "flue gas analysis", "combustion efficiency", "excess air", "stack temperature", "draft measurement", "O2 analysis", "CO2 measurement", "boiler tuning"]
tags: ["combustion analysis", "flue gas analysis", "combustion efficiency", "excess air", "stack temperature", "draft measurement", "O2 analysis", "CO2 measurement", "boiler tuning"]
weight: 6
---

Combustion analysis is the systematic evaluation of boiler performance through measurement and interpretation of flue gas composition, temperature, and pressure. This diagnostic process identifies efficiency losses, verifies safe operation, and provides data for optimizing fuel-air ratios to achieve maximum thermal efficiency while maintaining emissions compliance.

## Flue Gas Analysis

Flue gas composition directly reflects combustion quality and reveals the completeness of fuel oxidation. Modern combustion analyzers measure multiple gas species simultaneously using electrochemical sensors or infrared detection technology.

### Oxygen Measurement

Oxygen concentration in flue gas indicates excess air quantity. Typical O2 ranges for complete combustion:

| Fuel Type | Target O2 Range | Typical Value |
|-----------|-----------------|---------------|
| Natural Gas | 2-4% | 3% |
| No. 2 Oil | 2-5% | 3.5% |
| No. 6 Oil | 3-6% | 4% |
| Coal | 3-7% | 5% |

Excess oxygen readings above target ranges indicate heat losses from unnecessary flue gas mass flow. Insufficient oxygen creates incomplete combustion and carbon monoxide formation.

### Carbon Dioxide Measurement

CO2 concentration represents the theoretical maximum achievable with perfect combustion efficiency. Maximum CO2 values by fuel:

- Natural Gas: 11.7-12.1%
- No. 2 Oil: 15.0-15.5%
- No. 6 Oil: 16.0-16.5%

Lower CO2 readings correspond to higher excess air and reduced efficiency.

### Carbon Monoxide Monitoring

Carbon monoxide presence signals incomplete combustion due to insufficient oxygen, poor mixing, or flame impingement. Safe operation requires CO levels below 400 ppm air-free. Elevated CO indicates:

- Inadequate combustion air supply
- Burner wear or misalignment
- Insufficient furnace residence time
- Flame quenching on heat transfer surfaces

### Nitrogen Oxides (NOx)

NOx formation increases exponentially with flame temperature. Thermal NOx becomes significant above 2800°F peak flame temperature. Low-NOx burners maintain compliance through:

- Staged combustion reducing peak temperatures
- Flue gas recirculation diluting oxygen concentration
- Air preheat temperature control

## Combustion Efficiency Calculation

Combustion efficiency represents the percentage of fuel energy transferred to the working fluid. The calculation incorporates stack losses as the primary efficiency detriment:

**Efficiency (%) = 100 - Stack Loss - Radiation Loss**

Stack loss depends on flue gas temperature above ambient and excess air quantity. The standard stack loss equation:

**Stack Loss = K × (T_stack - T_ambient) × (% CO2_max / % CO2_measured)**

Where K is a fuel-specific constant ranging from 0.39 for natural gas to 0.54 for heavy oil.

Typical combustion efficiency ranges:

| Boiler Type | Efficiency Range |
|-------------|------------------|
| Condensing | 90-98% |
| Non-condensing | 80-85% |
| Fire-tube | 75-82% |
| Cast Iron | 75-80% |

## Excess Air Optimization

Excess air represents the quantity of combustion air supplied beyond stoichiometric requirements. The relationship:

**% Excess Air = (O2_measured / (20.9 - O2_measured)) × 100**

Optimum excess air balances two competing effects:

1. Insufficient air creates incomplete combustion, elevated CO, smoke, and potential safety hazards
2. Excessive air increases flue gas mass flow and stack temperature, reducing efficiency

Target excess air percentages:

- Natural gas: 10-15% (2-3% O2)
- Light oil: 15-20% (3-4% O2)
- Heavy oil: 20-30% (4-6% O2)

Each 1% reduction in excess oxygen improves efficiency by approximately 0.6% for natural gas and 1.0% for fuel oil.

## Stack Temperature Measurement

Stack temperature directly affects efficiency through sensible heat loss in flue gases. For every 40-50°F reduction in stack temperature, efficiency improves approximately 1%.

Typical stack temperatures:

| Application | Temperature Range |
|-------------|-------------------|
| Condensing Mode | 100-140°F |
| High-Efficiency Non-condensing | 250-350°F |
| Standard Efficiency | 350-500°F |
| Scotch Marine | 400-600°F |

Stack temperature elevation above design indicates:

- Fouled heat transfer surfaces (fire-side or water-side)
- Excessive excess air
- Burner degradation or misfire
- Heat exchanger scaling or corrosion

## Draft Measurement

Draft is the pressure difference driving combustion air into the furnace and flue gas through the boiler passages. Proper draft ensures stable combustion without pressurizing the boiler casing.

### Furnace Draft

Measured immediately downstream of the burner, furnace draft should maintain slight negative pressure:

- Natural draft boilers: -0.02 to -0.04 in. w.c.
- Forced draft boilers: -0.01 to -0.03 in. w.c.
- Balanced draft boilers: -0.05 to -0.10 in. w.c.

Excessive negative pressure indicates restricted flue passages or over-firing the induced draft fan. Positive pressure forces combustion products into the boiler room.

### Breech Draft

Breech draft, measured at the boiler outlet before any draft control device, indicates total pressure loss through the boiler:

- Fire-tube boilers: -0.10 to -0.25 in. w.c.
- Water-tube boilers: -0.20 to -0.50 in. w.c.

Rising breech draft over time signals heat exchanger fouling requiring cleaning.

## Combustion Tuning Procedures

Systematic combustion tuning optimizes efficiency while maintaining safe operation and emissions compliance.

### Initial Setup

1. Verify proper combustion air temperature and humidity
2. Confirm fuel supply pressure and temperature at design values
3. Inspect burner components for wear, alignment, and cleanliness
4. Check all draft gauge locations for accuracy

### Tuning Sequence

**Low Fire Adjustment:**
1. Set fuel valve to minimum position
2. Adjust combustion air damper for target O2 (typically 3-5%)
3. Verify CO below 200 ppm air-free
4. Record all parameters

**High Fire Adjustment:**
1. Set fuel valve to maximum firing rate
2. Adjust combustion air damper for target O2
3. Verify CO below 400 ppm air-free
4. Confirm stack temperature within acceptable range
5. Measure efficiency and compare to baseline

**Mid-Point Verification:**
1. Test combustion at 50% firing rate
2. Verify linear cam adjustment between low and high fire
3. Confirm O2 and CO remain within specifications
4. Adjust linkage if mid-point deviates from target

### Performance Documentation

Record complete combustion data for trending and future comparison:

- Flue gas O2, CO2, CO, NOx concentrations
- Stack temperature (air-free basis)
- Furnace and breech draft pressures
- Combustion efficiency percentage
- Fuel input rate and firing position
- Ambient air temperature

Repeat combustion analysis quarterly for critical boilers, annually for standard installations, and after any burner maintenance or fuel switching. Trending these parameters identifies degradation before efficiency losses become significant.

## Safety Considerations

Combustion analysis requires working near high-temperature surfaces and exposure to combustion gases. Critical safety protocols:

- Never sample flue gas without confirming draft gauge operation
- Maintain proper probe insertion depth to obtain representative samples
- Calibrate analyzers according to manufacturer specifications
- Verify CO alarm functionality before testing
- Monitor for combustible gas accumulation in furnace before ignition attempts

Properly executed combustion analysis optimizes boiler performance, reduces fuel consumption, extends equipment life, and ensures safe operation across all firing rates.
