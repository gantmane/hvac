---
title: "Makeup Air Units"
description: "Comprehensive coverage of makeup air systems including tempered and heated configurations, direct-fired vs indirect-fired designs, and application requirements."
date: "2026-01-04"
weight: 3
tags: ["makeup air unit", "direct fired makeup air", "tempered makeup air", "kitchen exhaust makeup air", "100% outdoor air", "industrial ventilation"]
categories: ["Heating Systems"]
---

Makeup air units replace air exhausted from buildings by kitchen hoods, laboratory fume hoods, paint booths, welding stations, and industrial processes. Unlike recirculating air handling units that condition primarily return air with minimum outdoor air for ventilation, makeup air units handle 100% outdoor air to maintain building pressure balance and prevent infiltration-driven comfort and energy problems.

## Fundamental Purpose

Exhaust systems remove air from buildings to capture contaminants, control odors, or provide process ventilation. This creates negative pressure unless equal quantities of outdoor air enter the building. Uncontrolled infiltration through cracks, doors, and building envelope penetrations causes:

- **Comfort problems**: Cold drafts near doors and windows during winter
- **Door operation difficulty**: Pressure differentials exceeding 0.05 inches water gauge require excessive force to open doors
- **Combustion appliance backdrafting**: Negative pressure draws flue gases into occupied spaces
- **Energy waste**: Uncontrolled infiltration bypasses heat recovery and conditioning equipment
- **Indoor air quality degradation**: Unconditioned infiltration air carries dust, pollen, and moisture

Makeup air units solve these problems by providing controlled outdoor air introduction at temperatures and velocities compatible with occupied space comfort.

## Capacity Determination

Makeup air unit capacity must equal or slightly exceed exhaust airflow to maintain neutral or slightly positive building pressure. The airflow balance:

$$\text{CFM}_{makeup} \geq \text{CFM}_{exhaust,total} - \text{CFM}_{infiltration}$$

For a restaurant with:
- Kitchen exhaust hood: 5,000 CFM
- Bathroom exhaust: 400 CFM
- Expected infiltration: 300 CFM (approximately 0.2 air changes per hour for 10,000 ft³ space)

Required makeup air:

$$\text{CFM}_{makeup} = 5000 + 400 - 300 = 5,100 \text{ CFM}$$

Designers typically provide 10-20% excess to ensure positive pressure and account for system variations, resulting in a 5,500-6,000 CFM makeup air unit.

## Heating Requirements

Outdoor air at winter design conditions requires substantial heating to prevent occupant discomfort and space temperature depression. The heating load:

$$Q_h = \text{CFM} \times 1.08 \times (T_{discharge} - T_{outdoor})$$

For 5,500 CFM with outdoor temperature of 0°F and discharge temperature of 65°F:

$$Q_h = 5500 \times 1.08 \times (65 - 0) = 385,110 \text{ Btu/hr}$$

This substantial load drives selection between tempering (minimal heating to 50-60°F), full heating (65-75°F discharge), or direct-fired combustion (90-100% efficiency through products-in-airstream combustion).

## Configuration Types

### Tempered Makeup Air

Tempered systems heat outdoor air to 50-65°F, preventing extreme cold air discharge while minimizing heating energy. The reduced discharge temperature suits industrial and commercial spaces where localized heating (unit heaters, radiant heaters) maintains occupied zone comfort.

Heating capacity sized for 50-55°F discharge:

$$Q_{tempered} = 5500 \times 1.08 \times (55 - 0) = 326,700 \text{ Btu/hr}$$

This represents 85% of full heating load, saving 15% in heating capacity and ongoing energy costs.

### Heated Makeup Air

Fully heated systems deliver air at 65-75°F, suitable for occupied spaces without supplemental heating. Restaurants, retail stores, and office areas benefit from heated makeup air that contributes to space conditioning rather than merely preventing excessive cooling.

The discharge temperature limits based on velocity and distribution pattern. High-velocity discharge (1500-2500 FPM) to high-ceiling areas tolerates 70-80°F air. Low-velocity diffusers (300-500 FPM) near occupied zones require 60-70°F maximum to avoid draft complaints.

### Direct-Fired Configuration

Direct-fired makeup air units burn natural gas or propane in the supply airstream, mixing combustion products with outdoor air. This achieves 90-95% thermal efficiency since heat from combustion gases transfers directly to supply air without flue losses.

The stoichiometric combustion of natural gas:

$$\text{CH}_4 + 2\text{O}_2 \rightarrow \text{CO}_2 + 2\text{H}_2\text{O}$$

For every cubic foot of natural gas burned with proper air-fuel ratio, products include approximately 1 ft³ CO₂, 2 ft³ water vapor (as steam), and nitrogen from combustion air. These products mix with supply air, diluting to acceptable concentrations:

For 400 MBH natural gas input (approximately 390 ft³/hr at 1020 Btu/ft³) with 5,500 CFM supply:

$$\text{CO}_2\text{ concentration} = \frac{390 \text{ ft}^3\text{/hr}}{5500 \times 60 \text{ ft}^3\text{/hr}} \times 10^6 = 1,182 \text{ ppm}$$

ASHRAE 62.1 permits CO₂ levels up to 700 ppm above outdoor ambient (typically 400-450 ppm outdoor), allowing 1100-1150 ppm indoor. Direct-fired units operate near this limit, requiring larger airflow rates than combustion heating alone would demand.

### Indirect-Fired Configuration

Indirect-fired units separate combustion products from supply air using heat exchangers. Thermal efficiency drops to 80-85% due to flue gas losses, but supply air remains free of combustion products.

Applications requiring indirect firing:
- Healthcare facilities with strict air quality requirements
- Clean rooms and laboratory spaces
- Food processing facilities (prevent product contamination)
- Installations with inadequate airflow for CO₂ dilution

## Integration with Building Systems

Makeup air systems coordinate with multiple building systems:

### Exhaust System Interlocks

Makeup air fans should energize before or simultaneously with exhaust fans to prevent negative pressure transients. Control sequences typically:

1. Prove makeup air fan operation (airflow switch)
2. Delay 10-30 seconds for supply air to pressurize building
3. Enable exhaust fan operation

Failure of makeup air fans should disable associated exhaust systems to prevent excessive negative pressure.

### Building Pressure Control

Pressure sensors monitor building pressure relative to outdoors (differential pressure = 0.02-0.08 inches water gauge positive). Modulating dampers or variable-speed fans adjust makeup air to maintain setpoint despite varying exhaust flow rates.

For buildings with variable kitchen hood exhaust (demand-based controls), makeup air must track exhaust variations:

$$\text{CFM}_{makeup}(t) = K \times \text{CFM}_{exhaust}(t)$$

where K ranges from 0.85-1.05 depending on building tightness and infiltration rates.

### Heating System Coordination

Makeup air heating loads may exceed primary heating system capacity. Integration strategies:

**Dedicated makeup air heating** using gas-fired burners or electric resistance separate from building heating. This prevents oversizing central heating plants for intermittent makeup air demands.

**Heat recovery** from exhaust airstreams using run-around loops, plate heat exchangers, or energy wheels. Kitchen exhaust temperature of 90-120°F can preheat makeup air, reducing heating loads by 30-60% depending on recovery effectiveness.

**Economizer integration** providing free cooling when outdoor temperatures permit. Makeup air units with economizer capability condition outdoor air for space cooling in addition to pressure balance functions.

## Fan Selection and Performance

Makeup air fans must overcome external static pressure from outdoor louvers, filters, heating coils, and discharge ductwork. Typical system resistance: 1.5-3.0 inches water gauge.

Centrifugal fans with backward-inclined or airfoil blades provide efficiency of 65-75% at operating points. Fan motor horsepower:

$$\text{HP} = \frac{\text{CFM} \times \text{SP}}{6356 \times \eta_{fan} \times \eta_{motor} \times \eta_{drive}}$$

For 5,500 CFM at 2.0 inches water gauge with 70% fan efficiency, 95% motor efficiency, and 97% drive efficiency (VFD):

$$\text{HP} = \frac{5500 \times 2.0}{6356 \times 0.70 \times 0.95 \times 0.97} = 2.65 \text{ HP}$$

Specify a 3 HP motor with service factor of 1.15 for continuous operation.

Variable-frequency drives modulate airflow to match varying exhaust demands, reducing energy consumption by 40-70% compared to constant-volume operation with damper modulation.

## Filtration Requirements

Makeup air handling 100% outdoor air requires effective filtration to prevent coil fouling and maintain indoor air quality. Minimum recommendations:

- **Industrial facilities**: MERV 8 (30-35% ASHRAE dust spot efficiency)
- **Commercial buildings**: MERV 11 (60-65% dust spot efficiency)
- **Healthcare/clean rooms**: MERV 13-14 (85-95% dust spot efficiency)

Higher efficiency filtration increases static pressure by 0.2-0.6 inches water gauge, affecting fan selection and energy consumption. The tradeoff between IAQ improvement and fan energy requires site-specific analysis.

## Discharge Strategies

Makeup air introduction affects comfort and space temperature distribution. Common approaches:

**High-velocity discharge** above occupied zones (12-20 feet ceiling height) at 1500-2500 FPM. The high-velocity jets induce room air mixing 3:1 to 5:1 (induced CFM to supply CFM), moderating temperature impact.

**Low-velocity displacement** through floor-level or low sidewall diffusers at 200-400 FPM. This suits applications where temperature stratification benefits comfort (cool air at floor, warm air at ceiling in summer) or where low noise is critical.

**Perimeter heating integration** discharging makeup air through perimeter diffusers or unit heaters to counteract envelope heat losses. This dual-purpose approach reduces equipment count and installation costs.

Makeup air units represent critical components of building environmental systems wherever significant exhaust airflow creates pressure imbalance. Proper design balances energy efficiency, comfort, code compliance, and system integration to deliver reliable building pressurization and ventilation.
