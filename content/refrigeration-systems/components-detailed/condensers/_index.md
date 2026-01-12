---
title: "Condensers"
weight: 2
description: "Technical analysis of refrigeration condensers including air-cooled, water-cooled, and evaporative types with heat rejection fundamentals, sizing methods, and performance characteristics."
---

Condensers reject heat from refrigerant vapor discharged by the compressor, condensing it to liquid for circulation through the refrigeration cycle. The condenser heat rejection rate equals the evaporator capacity plus the compressor work input:

Q<sub>c</sub> = Q<sub>e</sub> + W<sub>comp</sub>

where Q<sub>c</sub> is condenser capacity (kW), Q<sub>e</sub> is evaporator load (kW), and W<sub>comp</sub> is compressor power (kW).

## Heat Rejection Fundamentals

The condensing process occurs in three distinct zones:

**Desuperheating zone**: Hot discharge gas cools from superheated vapor to saturation temperature. This sensible heat removal typically accounts for 10-20% of total condenser capacity depending on compression ratio and superheat.

**Condensing zone**: Refrigerant undergoes phase change at constant temperature (saturation). This latent heat rejection represents 75-85% of condenser capacity. The condensing temperature is determined by the balance between refrigerant mass flow and heat transfer effectiveness.

**Subcooling zone**: Condensed liquid cools below saturation temperature. Subcooling typically provides 2-8°C of liquid cooling, ensuring vapor-free liquid enters the expansion device and increasing system capacity and efficiency.

Heat transfer in condensers follows:

Q = UA × LMTD

where U is overall heat transfer coefficient (W/m²·K), A is heat transfer surface area (m²), and LMTD is log mean temperature difference (K).

## Condenser Types

### Air-Cooled Condensers

Air-cooled condensers use ambient air as the cooling medium, circulated by fans across finned tube coil banks. These units dominate commercial refrigeration applications due to simplicity and elimination of water treatment requirements.

**Configuration**: Typical designs employ copper tubes with aluminum plate fins. Fin spacing ranges from 1.8-4.0 mm depending on application. Higher fin densities increase surface area but reduce airflow and increase fouling susceptibility.

**Face velocities**: Design face velocities range from 1.5-3.0 m/s. Higher velocities reduce coil size but increase fan power and noise. Propeller fans provide high airflow at low static pressure (25-75 Pa). Centrifugal fans handle higher static pressure for ducted applications.

**Condensing temperature**: Air-cooled systems typically condense at 10-20°C above ambient dry bulb temperature. This temperature difference (TD) represents the sum of coil approach temperature and air temperature rise through the coil.

**Seasonal performance**: Condensing pressure varies with ambient conditions. A 5°C reduction in condensing temperature improves COP by approximately 10-15% for typical refrigerants. Capacity modulation through fan cycling or variable speed drives optimizes efficiency at part load.

### Water-Cooled Condensers

Water-cooled condensers use water as the heat rejection medium, offering superior performance due to water's high heat capacity and conductivity.

**Shell-and-tube configuration**: Refrigerant condenses on the shell side while cooling water flows through tubes. Tube-side velocities of 1-2.5 m/s provide turbulent flow for effective heat transfer while limiting erosion and pressure drop.

**Tube materials**: Copper tubes dominate due to excellent conductivity (385 W/m·K). Enhanced tubes with internal rifling or external low fins increase U-values from 850-1200 W/m²·K for plain tubes to 1400-2000 W/m²·K.

**Approach temperature**: Water-cooled condensers achieve 2-6°C approach (condensing temperature minus leaving water temperature). This tight approach results from high heat transfer coefficients on both refrigerant and water sides.

**Fouling considerations**: Waterside fouling from scale, biological growth, and suspended solids reduces U-values over time. ASHRAE Refrigeration recommends fouling factors of 0.000044 m²·K/W for clean water to 0.00018 m²·K/W for severely fouling conditions. Regular tube cleaning maintains design performance.

**Water consumption**: Open-loop systems consume 0.03-0.05 L/s per kW of heat rejection (once-through flow). Closed-loop systems with cooling towers recirculate water with makeup for evaporation and blowdown losses.

### Evaporative Condensers

Evaporative condensers combine principles of water-cooled and air-cooled types by spraying water over refrigerant coil while drawing air across the wetted surface.

**Operating principle**: Water evaporation provides latent cooling, allowing heat rejection at wet bulb rather than dry bulb temperature. This 8-15°C advantage over air-cooled systems reduces condensing pressure and improves efficiency.

**Design approach**: Evaporative condensers typically achieve 5-10°C approach to ambient wet bulb temperature. The governing equation combines sensible and latent heat transfer:

Q = h<sub>o</sub> × A × (h<sub>sat,refrig</sub> - h<sub>air</sub>)

where h<sub>o</sub> is overall mass transfer coefficient and h represents specific enthalpy.

**Water requirements**: Evaporative systems use 0.012-0.020 L/s per kW, approximately 40-60% less than cooling tower systems due to direct heat rejection without intermediate water loop.

**Maintenance requirements**: Regular water treatment prevents scale and biological growth. Winterization requires water drainage in freezing climates. Air filtration protects coils from debris accumulation.

## Selection Criteria and Sizing

Condenser selection balances first cost, operating cost, water availability, and space constraints:

**Air-cooled advantages**: No water consumption, minimal maintenance, simple installation. Disadvantages include higher operating cost, reduced efficiency at high ambient, and space requirements for adequate airflow.

**Water-cooled advantages**: Superior efficiency, compact size, consistent performance. Disadvantages include water treatment costs, freeze protection requirements, and cooling tower infrastructure.

**Evaporative advantages**: Efficiency approaching water-cooled with reduced water consumption. Disadvantages include water treatment, winterization complexity, and higher maintenance.

## Sizing Methodology

Condenser capacity must accommodate design conditions with appropriate safety factors:

1. Calculate heat rejection: Q<sub>c</sub> = refrigeration capacity × (1 + 1/COP)
2. Determine condensing temperature based on available cooling medium and approach
3. Select heat transfer surface area: A = Q / (U × LMTD)
4. Apply fouling factors and performance degradation allowances (10-15%)
5. Verify physical constraints (space, weight, connections)

## Subcooling Benefits

Subcooling liquid refrigerant below saturation temperature provides several advantages:

**Capacity increase**: Each degree of subcooling increases refrigeration effect by 0.3-0.7% depending on refrigerant properties. The additional cooling capacity comes from increased enthalpy change in the evaporator.

**Efficiency improvement**: Subcooling prevents flash gas formation in liquid lines, ensuring full liquid feed to expansion devices. This maintains intended expansion device performance and evaporator capacity.

**System stability**: Adequate subcooling (3-5°C minimum) protects against liquid flashing during pressure drops or temperature increases in liquid lines. Insufficient subcooling causes capacity loss and compressor hunting.

**Design targets**: ASHRAE Refrigeration recommends 5-8°C subcooling for most applications. Excessive subcooling (>12°C) indicates overcharged system or restricted airflow requiring investigation.

## Performance Characteristics

Condenser performance varies with operating conditions:

**Temperature effect**: Each 1°C increase in condensing temperature increases compressor power by 2-3% while reducing capacity by 1-2%. This underscores the importance of maintaining design condensing conditions through proper maintenance.

**Fouling impact**: Air-side fouling from dust and debris reduces airflow and increases condensing temperature. A 20% airflow reduction raises condensing temperature approximately 3-5°C. Water-side fouling builds thermal resistance, requiring higher condensing temperatures to reject design heat load.

**Ambient conditions**: Air-cooled condenser capacity varies with ambient temperature. At conditions below design ambient, condensing pressure drops, improving system efficiency but potentially causing low-pressure cutout or expansion device underfeeding.

**Head pressure control**: Systems require minimum condensing pressure for proper expansion device feeding and oil return. Strategies include fan cycling, variable speed drives, condenser flooding, and variable geometry dampers.

## Maintenance Considerations

Regular condenser maintenance preserves design performance:

**Air-cooled systems**: Clean coils quarterly in dusty environments, annually in clean locations. Straighten damaged fins. Verify fan operation and amperage. Check refrigerant charge via subcooling measurements.

**Water-cooled systems**: Brush tube bundles annually or as indicated by approach temperature degradation. Monitor waterside pressure drop indicating fouling. Maintain water treatment program preventing scale and corrosion. Eddy current test tubes for thickness loss.

**Evaporative systems**: Clean water distribution system. Replace worn nozzles. Clean or replace media pads. Verify bleed-off operation. Drain and clean basin monthly during operation. Inspect coil for corrosion.

## Energy Efficiency Comparisons

Condenser type significantly impacts system efficiency. At 35°C ambient conditions:

- Air-cooled: Condensing at 45-50°C, EER 8-10
- Water-cooled: Condensing at 35-40°C, EER 11-14
- Evaporative: Condensing at 32-38°C, EER 10-13

Values vary with specific equipment, refrigerant, and operating conditions. Life cycle cost analysis should evaluate first cost, energy cost, water/sewer charges, and maintenance requirements for complete economic comparison per ASHRAE economic analysis guidelines.
