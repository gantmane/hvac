---
title: "Ventilation"
aliases: ["Ventilation"]
description: "Ventilation strategies for mold prevention including dilution ventilation, local exhaust, controlled ventilation rates, and dehumidification to manage indoor moisture and maintain acceptable humidity levels."
weight: 3
---

Ventilation controls indoor humidity by diluting moisture-laden indoor air with outdoor air or through mechanical dehumidification. Effective ventilation strategies balance moisture removal requirements, energy efficiency, and indoor air quality objectives. Modern airtight construction makes mechanical ventilation essential for humidity control and occupant health.

## Dilution Ventilation

Dilution ventilation removes moisture by replacing indoor air with outdoor air at controlled rates. The effectiveness depends on the moisture content difference between indoor and outdoor air. In heating climates during winter, cold outdoor air contains minimal absolute moisture, making dilution ventilation highly effective for humidity control. In cooling climates during summer, outdoor air often contains more moisture than indoor air, making dilution ventilation counterproductive without dehumidification.

Required ventilation rate for moisture removal depends on moisture generation rate and acceptable indoor humidity level. The relationship follows from mass balance:

V = G / (W_in - W_out)

Where V equals ventilation rate (cfm), G equals moisture generation rate (lb/hr), W_in equals indoor humidity ratio (lb/lb), and W_out equals outdoor humidity ratio (lb/lb).

For typical residential occupancy generating 15 lb/day moisture (0.625 lb/hr) with outdoor conditions of 20°F and 50% RH (W_out = 0.0015 lb/lb) and desired indoor conditions of 70°F and 40% RH (W_in = 0.0063 lb/lb), required ventilation equals:

V = 0.625 / (0.0063 - 0.0015) = 130 cfm

This calculation demonstrates why cold weather enables lower ventilation rates for humidity control, while warm humid weather requires mechanical dehumidification rather than increased ventilation.

ASHRAE Standard 62.2 specifies minimum residential ventilation rates based on floor area and bedrooms: Q = 0.03 × Floor Area + 7.5 × (Bedrooms + 1). For a 2000 ft² home with 3 bedrooms, minimum ventilation equals 0.03 × 2000 + 7.5 × 4 = 90 cfm continuous or equivalent intermittent operation.

Commercial ventilation rates per ASHRAE Standard 62.1 vary by occupancy type and density, ranging from 5 cfm per person for storage spaces to 20 cfm per person for meeting rooms. High-moisture-generating spaces including kitchens, locker rooms, and natatoriums require dedicated exhaust ventilation at rates of 0.5-2.0 cfm per square foot.

## Local Exhaust Ventilation

Local exhaust captures moisture at the source before it diffuses throughout the building. Source capture proves far more effective than dilution ventilation, removing moisture at concentrations 10-100 times higher than room air. Common local exhaust locations include bathrooms, kitchens, laundry rooms, and indoor pool enclosures.

### Bathroom Kitchen Exhaust

Bathroom exhaust removes moisture from showering and bathing, which generates 0.5-1.5 kg water per shower event. Code-minimum exhaust rates of 50 cfm intermittent or 20 cfm continuous prove adequate for typical bathrooms when operated during and for 20 minutes after moisture-generating activities. High-use bathrooms benefit from 80-110 cfm exhaust or humidity-sensing controls that operate the fan until space humidity returns to background levels.

Kitchen exhaust removes cooking moisture and combustion products. Range hoods should provide minimum 100 cfm for residential applications, with commercial kitchens requiring dedicated exhaust based on appliance heat generation and cooking methods. Capture efficiency depends critically on hood configuration and airflow pattern. Wall-mounted hoods achieve 80-90% capture efficiency at 100 cfm per linear foot of hood width. Island hoods require 150-200 cfm per linear foot due to cross-currents disrupting capture.

Make-up air becomes necessary when exhaust rates exceed 400 cfm in residential applications or create building depressurization greater than 5 Pa. Depressurization risks include backdrafting of combustion appliances, increased envelope air leakage and moisture transport, and door operability issues. Tempered make-up air systems preheat outdoor air to 60-70°F, reducing thermal discomfort and energy consumption.

## Controlled Ventilation Rate

Continuous controlled ventilation maintains consistent humidity control without the variability of occupant-operated exhaust fans. Controlled ventilation strategies include:

**Supply-only ventilation** distributes outdoor air through forced-air system ductwork, providing good distribution but pressurizing the building. Building pressurization increases exfiltration through envelope assemblies, potentially causing moisture problems in cold climates. Supply-only ventilation suits hot-humid climates where building pressurization prevents humid outdoor air infiltration.

**Exhaust-only ventilation** operates dedicated exhaust fan(s) continuously, depressurizing the building and drawing outdoor air through passive inlets or envelope leakage. Depressurization prevents exfiltration moisture problems in cold climates but introduces humid outdoor air in hot-humid climates. Exhaust-only ventilation costs less than balanced systems and suits cold climate applications.

**Balanced ventilation** supplies and exhausts equal airflow rates, maintaining neutral building pressure. Balanced systems prevent pressurization and depressurization effects on envelope assemblies while providing controlled ventilation. Heat recovery ventilators (HRV) transfer sensible heat between supply and exhaust airstreams, reducing heating and cooling energy consumption. Energy recovery ventilators (ERV) transfer both sensible and latent heat, reducing dehumidification loads in cooling climates.

ERV effectiveness for moisture transfer ranges from 50-80%, significantly reducing indoor humidity in hot-humid climates. For outdoor conditions of 90°F and 70% RH (humidity ratio 0.0156 lb/lb) and indoor conditions of 75°F and 50% RH (humidity ratio 0.0093 lb/lb), 70% ERV effectiveness reduces supply air humidity ratio to:

W_supply = W_outdoor - 0.70 × (W_outdoor - W_indoor) = 0.0156 - 0.70 × (0.0156 - 0.0093) = 0.0112 lb/lb

This reduction decreases latent cooling load by 44%, substantially reducing dehumidification energy consumption.

## Dehumidification

Mechanical dehumidification removes moisture through condensation or desiccant absorption without requiring outdoor air dilution. Dehumidification proves essential in hot-humid climates where outdoor air contains more moisture than acceptable indoor air, and during shoulder seasons when cooling loads remain low but humidity loads remain high.

**Cooling-based dehumidification** condenses moisture on cooling coils maintained below dew point temperature. Sensible heat ratio (SHR) describes the portion of total capacity dedicated to sensible cooling versus latent dehumidification. Standard cooling equipment achieves SHR of 0.75-0.85, removing 1.5-2.5 lb moisture per hour per ton of cooling capacity. Enhanced dehumidification equipment reduces SHR to 0.60-0.70 through lower airflow rates, larger coils, or refrigerant subcooling.

Adequate dehumidification requires equipment operation at part-load conditions where latent capacity exceeds latent load while sensible capacity matches sensible load. Oversized equipment short-cycles, failing to operate long enough for moisture removal. Variable-capacity equipment maintains longer run times at reduced capacity, providing superior humidity control compared to single-stage equipment.

**Dedicated dehumidification systems** provide humidity control independent of space cooling, using separate equipment optimized for moisture removal. Desiccant dehumidifiers achieve supply air dew points of 35-45°F, far lower than cooling-coil-based systems limited to 50-55°F. Desiccant systems suit applications requiring low humidity (museums, hospitals, ice rinks) or providing ventilation dehumidification in dedicated outdoor air systems (DOAS).

Desiccant wheel dehumidifiers pass supply air through rotating wheel impregnated with hygroscopic material (silica gel, molecular sieves). The wheel absorbs moisture from supply air in the process section, then releases moisture to regeneration air in the reactivation section. Regeneration requires heating to 180-250°F, typically using natural gas or electric resistance heating. Coefficient of performance for desiccant dehumidification ranges from 0.5-1.5 depending on regeneration temperature and outdoor conditions.

**Whole-house dehumidifiers** integrate with forced-air systems, operating independently of cooling system to maintain humidity setpoint. These systems provide 70-100 pints per day capacity (approximately 0.7-1.0 tons latent capacity), adequate for typical residential applications in humid climates. Controls operate the dehumidifier when indoor relative humidity exceeds setpoint (typically 50-55%), circulating air through dehumidifier coil using air handler or dedicated fan.

Heat pump water heaters provide incidental dehumidification by cooling and dehumidifying surrounding air while heating water. A typical HPWH removes 1-3 pints per hour during water heating cycles, equivalent to 15-40 pints per day depending on hot water usage. Strategic HPWH location in basements or mechanical rooms provides dehumidification where moisture problems commonly occur.

## Ventilation System Commissioning

Ventilation system performance requires verification through commissioning. Airflow measurements confirm design flow rates, pressure measurements verify adequate static pressure for distribution, and humidity monitoring documents humidity control effectiveness.

Airflow measurement methods include:

- Powered flow hoods for register and grille flows (±10% accuracy)
- Hot-wire anemometers for duct velocities (±5% accuracy)
- Pitot tube traverses for large ducts (±3% accuracy)
- Flow stations for constant monitoring (±5% accuracy)

Acceptable airflow tolerances range from ±10% for non-critical applications to ±5% for high-performance or critical applications. Measured flows exceeding these tolerances require adjustment through fan speed changes, damper adjustment, or duct modifications.

Humidity monitoring during occupied operation verifies ventilation system effectiveness. Target indoor relative humidity depends on season and climate: 30-40% RH during heating season, 40-60% RH during cooling season. Sustained humidity above these ranges indicates insufficient ventilation or dehumidification capacity requiring system adjustment or supplemental dehumidification equipment.
