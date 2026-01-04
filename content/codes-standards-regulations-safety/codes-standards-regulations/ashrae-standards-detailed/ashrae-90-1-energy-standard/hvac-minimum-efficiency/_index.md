---
title: "HVAC Equipment Minimum Efficiency Requirements"
description: "Comprehensive equipment efficiency tables and performance metrics for HVAC systems including cooling equipment, heating equipment, heat rejection, and specialized applications with capacity-based requirements."
date: 2026-01-04
weight: 3
---

ASHRAE Standard 90.1 Section 6.8 establishes minimum energy efficiency requirements for HVAC equipment through comprehensive tables organized by equipment category, capacity range, and operational characteristics. These prescriptive efficiency minimums represent achievable performance levels based on current technology and manufacturing capabilities. Equipment manufacturers rate products using standardized test procedures allowing direct comparison of efficiency across brands and models. Understanding these efficiency requirements, rating metrics, and application considerations is essential for equipment selection, specification development, and code compliance verification.

## Equipment Efficiency Rating Metrics

Different equipment categories use different efficiency metrics reflecting their operational characteristics and testing procedures. Understanding these metrics enables proper interpretation of equipment ratings and code requirements.

**Energy Efficiency Ratio (EER)** measures cooling efficiency at a single, specified operating condition. EER represents the ratio of cooling capacity in Btu/h to electrical power input in watts at standard rating conditions:

$$EER = \frac{Q_{cooling,Btu/h}}{P_{input,W}}$$

Standard rating conditions for EER include 95°F outdoor dry-bulb temperature, specific indoor conditions (80°F DB/67°F WB for comfort cooling), and full-load operation. EER provides a snapshot of peak-condition performance useful for peak load analysis and capacity verification.

**Integrated Energy Efficiency Ratio (IEER)** evaluates part-load cooling performance by testing at multiple operating points and weighting the results to represent typical annual operation. The calculation includes performance at 100%, 75%, 50%, and 25% load:

$$IEER = 0.02 \times EER_{100\%} + 0.617 \times EER_{75\%} + 0.238 \times EER_{50\%} + 0.125 \times EER_{25\%}$$

The weighting factors reflect the percentage of annual operating hours equipment spends at each load level for typical commercial applications. IEER better represents annual energy consumption than EER because most equipment operates at part-load conditions the majority of the time.

**Seasonal Energy Efficiency Ratio (SEER)** applies to residential and light commercial equipment, measuring cooling performance over an entire cooling season using seasonal temperature bins. Higher SEER values indicate better seasonal performance. SEER accounts for cycling losses, part-load degradation, and variable outdoor conditions throughout the cooling season.

**Coefficient of Performance (COP)** measures heating efficiency as the ratio of heating capacity to power input, both expressed in consistent units (typically Btu/h or watts):

$$COP = \frac{Q_{heating}}{P_{input}}$$

For electric resistance heating, COP = 1.0 because all electrical input converts to heat. Heat pumps achieve COP >1.0 by moving heat rather than generating it, with typical values ranging from 2.0 to 4.5 depending on outdoor temperature and equipment type.

**Heating Seasonal Performance Factor (HSPF)** evaluates heat pump heating performance over an entire heating season, analogous to SEER for cooling. HSPF accounts for defrost operation, cyclic degradation, and variable outdoor temperatures. Minimum HSPF requirements ensure acceptable heating season performance.

**Thermal Efficiency and Combustion Efficiency** apply to fuel-fired heating equipment. Combustion efficiency measures the percentage of fuel energy released during combustion that transfers to the heat exchanger rather than exhausting up the flue. Thermal efficiency includes both combustion efficiency and jacket losses, representing total useful heat output divided by fuel input:

$$\eta_{thermal} = \frac{Q_{useful}}{Q_{fuel,input}} \times 100\%$$

Condensing equipment achieves thermal efficiency >90% by extracting latent heat from flue gas water vapor. Non-condensing equipment typically achieves 80-85% thermal efficiency.

## Air Conditioners and Condensing Units

ASHRAE 90.1 Table 6.8.1-1 establishes minimum efficiency requirements for electrically operated unitary air conditioners and condensing units. Requirements vary based on equipment type, cooling capacity, and whether equipment is air-cooled or evaporatively-cooled.

**Small air conditioners (<65,000 Btu/h):**
- Split systems: SEER ≥14.0, EER ≥11.0
- Single package: SEER ≥14.0, EER ≥11.0
- These values reflect federal minimum efficiency standards for this equipment category

**Medium air conditioners (≥65,000 Btu/h and <135,000 Btu/h):**
- Air-cooled: EER ≥11.2, IEER ≥12.0
- Evaporatively-cooled: EER ≥11.6, IEER ≥12.4
- Both full-load (EER) and part-load (IEER) minimums must be satisfied

**Large air conditioners (≥135,000 Btu/h and <240,000 Btu/h):**
- Air-cooled: EER ≥11.0, IEER ≥12.9
- Evaporatively-cooled: EER ≥11.4, IEER ≥13.3
- Requirements increase for larger capacities reflecting improved economies of scale

**Extra-large air conditioners (≥240,000 Btu/h and <760,000 Btu/h):**
- Air-cooled: EER ≥10.0, IEER ≥13.0
- Evaporatively-cooled: EER ≥10.4, IEER ≥13.4
- These larger systems typically serve multiple zones or whole buildings

**Very large air conditioners (≥760,000 Btu/h):**
- Air-cooled: EER ≥9.7, IEER ≥12.4
- Evaporatively-cooled: EER ≥10.1, IEER ≥12.8
- Frequently applied in central station applications and large commercial buildings

Evaporatively-cooled equipment shows approximately 4% higher efficiency minimums than air-cooled equipment because evaporative precooling of condenser air improves heat rejection effectiveness.

## Air-Source Heat Pumps

Table 6.8.1-2 establishes minimum efficiency for electrically operated unitary and applied heat pumps. Requirements include both cooling mode (EER/IEER/SEER) and heating mode (COP/HSPF) minimums.

**Small heat pumps (<65,000 Btu/h cooling capacity):**
- Cooling: SEER ≥15.0, EER ≥12.0
- Heating: HSPF ≥8.8, COP ≥3.4 at 47°F
- Split systems have slightly higher minimums than single-package systems

**Medium heat pumps (≥65,000 Btu/h and <135,000 Btu/h):**
- Cooling: EER ≥11.0, IEER ≥12.5
- Heating: COP ≥3.3 at 47°F
- Air-cooled and water-source types have different heating minimums

**Large heat pumps (≥135,000 Btu/h):**
- Cooling: EER ≥10.6-11.0, IEER ≥12.0-13.0 (depends on capacity)
- Heating: COP ≥3.2 at 47°F
- Both air-source and water-source configurations are specified

Heating COP is rated at 47°F outdoor temperature, representing moderate heating conditions. Performance degrades at lower outdoor temperatures, particularly for air-source units. Cold climate heat pumps maintain higher COP at reduced outdoor temperatures through enhanced refrigeration cycles and optimized heat exchangers.

## Water-Chilling Packages (Chillers)

Table 6.8.1-3 provides minimum efficiency requirements for water-chilling packages, organized by compressor type, condenser type, capacity range, and refrigerant. Both full-load efficiency (Path A) and part-load efficiency (Path B using IPLV) must be satisfied.

**Air-cooled chillers:**
- <150 tons: EER ≥9.5, IPLV ≥12.5
- ≥150 tons: EER ≥9.7-10.1, IPLV ≥13.0-14.0
- Screw and scroll compressors have slightly different minimums
- Part-load performance (IPLV) receives significant weight because chillers operate at part-load most hours

**Water-cooled centrifugal chillers:**
- <150 tons: COP ≥5.50 (EER ≥18.8), IPLV ≥6.20
- ≥150 tons and <300 tons: COP ≥5.55, IPLV ≥6.28
- ≥300 tons: COP ≥6.10, IPLV ≥6.40-7.00
- Positive displacement types: COP ≥4.45-5.00, IPLV ≥5.05-6.00

Larger capacity chillers achieve higher efficiency through larger heat exchangers, improved aerodynamics, and optimized refrigeration cycles. Water-cooled chillers outperform air-cooled types because water provides more effective heat rejection than air, particularly during warm weather.

Integrated Part-Load Value (IPLV) for chillers uses the weighting:

$$IPLV = 0.01A + 0.42B + 0.45C + 0.12D$$

Where A = COP at 100% load, B = COP at 75% load, C = COP at 50% load, D = COP at 25% load. This weighting emphasizes 50% and 75% load operation where chillers spend most operating hours.

## Packaged Terminal Equipment

Packaged terminal air conditioners (PTACs) and heat pumps (PTHPs) follow unique efficiency requirements accounting for their standardized sizes and wall-sleeve installation. Table 6.8.1-4 establishes minimums using capacity-dependent formulas.

**PTAC minimum efficiency:**

$$EER_{min} = 14.0 - (0.300 \times Cap_{1000\,Btu/h})$$

For example, a 9,000 Btu/h PTAC requires:
$$EER_{min} = 14.0 - (0.300 \times 9.0) = 11.3$$

**PTHP minimum cooling efficiency:**

$$EER_{min} = 14.0 - (0.300 \times Cap_{1000\,Btu/h})$$

Same relationship as PTAC for cooling mode.

**PTHP minimum heating efficiency:**

$$COP_{min} = 1.70 - (0.060 \times Cap_{1000\,Btu/h})$$

For the same 9,000 Btu/h unit in heating:
$$COP_{min} = 1.70 - (0.060 \times 9.0) = 1.16$$

These sliding scales recognize that smaller capacity PTACs and PTHPs achieve higher EER values than larger units within this equipment category due to heat exchanger size constraints and standardized chassis dimensions.

## Warm Air Furnaces and Unit Heaters

Table 6.8.1-6 establishes minimum thermal efficiency or combustion efficiency for fuel-fired warm air furnaces and unit heaters based on fuel type and capacity.

**Gas-fired warm air furnaces:**
- <225,000 Btu/h input: AFUE ≥80% (non-weatherized), ≥81% (weatherized)
- ≥225,000 Btu/h input: Thermal efficiency ≥80% or combustion efficiency ≥80%
- Condensing furnaces typically achieve AFUE ≥92%

**Oil-fired warm air furnaces:**
- <225,000 Btu/h input: AFUE ≥83%
- ≥225,000 Btu/h input: Thermal efficiency ≥81% or combustion efficiency ≥81%

**Gas-fired unit heaters:**
- <225,000 Btu/h input: Thermal efficiency ≥80%
- ≥225,000 Btu/h input: Thermal efficiency ≥80% or combustion efficiency ≥80%

Annual Fuel Utilization Efficiency (AFUE) accounts for seasonal cycling losses and pilot light consumption in addition to steady-state combustion efficiency. Thermal efficiency and combustion efficiency represent steady-state performance at specified test conditions.

## Boilers

Table 6.8.1-7 provides minimum efficiency requirements for boilers organized by fuel type, capacity, and application (hot water versus steam). Combustion efficiency and thermal efficiency serve as alternative compliance metrics.

**Gas-fired hot water boilers:**
- <300,000 Btu/h: AFUE ≥82%
- ≥300,000 Btu/h and <2,500,000 Btu/h: Thermal efficiency ≥80%
- ≥2,500,000 Btu/h: Combustion efficiency ≥80%

**Gas-fired steam boilers:**
- <300,000 Btu/h: AFUE ≥80%
- ≥300,000 Btu/h and <2,500,000 Btu/h: Combustion efficiency ≥79%
- ≥2,500,000 Btu/h: Combustion efficiency ≥79%

**Oil-fired hot water boilers:**
- <300,000 Btu/h: AFUE ≥84%
- ≥300,000 Btu/h and <2,500,000 Btu/h: Thermal efficiency ≥82%
- ≥2,500,000 Btu/h: Combustion efficiency ≥82%

**Oil-fired steam boilers:**
- <300,000 Btu/h: AFUE ≥82%
- ≥300,000 Btu/h: Combustion efficiency ≥81%

Gas-fired condensing boilers commonly achieve thermal efficiency 90-96% by extracting latent heat from flue gas. Non-condensing boilers typically reach 80-85% thermal efficiency, limited by minimum stack temperature requirements for proper draft and condensation prevention.

## Heat Rejection Equipment

Table 6.8.1-8 establishes minimum efficiency for heat rejection equipment including cooling towers, evaporative condensers, and air-cooled condensers. Performance metrics differ from refrigeration equipment.

**Open-circuit cooling towers:**

Performance measured in gpm/hp (gallons per minute per fan horsepower) at specified wet-bulb and approach temperatures:

- Centrifugal fan towers: ≥38.2 gpm/hp
- Axial fan towers: ≥50.9 gpm/hp
- Propeller fan towers: ≥85.0 gpm/hp

Higher gpm/hp ratios indicate better efficiency because the tower moves more water per unit of fan power consumed.

**Closed-circuit cooling towers (fluid coolers):**
- Centrifugal fan: ≥14.0 gpm/hp
- Axial fan: ≥20.0 gpm/hp

**Air-cooled condensers:**

Performance rated in Btu/h·W (heat rejection per watt of fan power):

- ≥5,000 Btu/h·W (rated capacity/rated power input)

Air-cooled condensers reject heat directly to ambient air without evaporative cooling, typically resulting in higher condensing temperatures and lower system efficiency than evaporative heat rejection.

## Variable Refrigerant Flow Systems

Table 6.8.1-10 establishes minimum efficiency for variable refrigerant flow (VRF) multi-split air conditioners and heat pumps. VRF systems connect one outdoor unit to multiple indoor units with individual zone control.

**VRF air conditioners:**
- <65,000 Btu/h: EER ≥11.0, IEER ≥12.0
- ≥65,000 Btu/h and <135,000 Btu/h: EER ≥10.0, IEER ≥11.5
- ≥135,000 Btu/h: EER ≥9.5, IEER ≥11.0

**VRF heat pumps:**
- <65,000 Btu/h: EER ≥11.0, IEER ≥12.0, COP ≥3.3
- ≥65,000 Btu/h and <135,000 Btu/h: EER ≥10.0, IEER ≥11.5, COP ≥3.2
- ≥135,000 Btu/h: EER ≥9.5, IEER ≥11.0, COP ≥3.2

VRF systems often achieve IEER values significantly higher than minimums (14-20 IEER) through sophisticated capacity modulation, multiple compressors, and zone-level control reducing unnecessary conditioning.

## Compliance Verification Process

Equipment efficiency verification requires several steps ensuring specified equipment meets or exceeds minimum requirements:

1. **Identify equipment category:** Determine which table applies based on equipment type, application, and capacity
2. **Determine capacity range:** Identify the correct row within the applicable table based on rated cooling or heating capacity
3. **Verify all applicable metrics:** Check that equipment meets minimums for all required metrics (EER and IEER for most cooling equipment, COP for heating)
4. **Review manufacturer data:** Obtain certified performance data from manufacturer showing rated efficiency for the specific model
5. **Document compliance:** Record equipment make, model, capacity, and rated efficiency in compliance documentation

For equipment with multiple size options or accessory configurations, verify that the specific combination selected meets minimums. Some equipment achieves minimum efficiency only with specific coil sizes, airflow rates, or accessory configurations.

## Capacity-Weighted Efficiency

When multiple pieces of identical equipment type serve a building (for example, multiple chillers or rooftop units), the capacity-weighted average efficiency must meet or exceed minimums:

$$\eta_{weighted} = \frac{\sum_{i=1}^{n} Q_i \cdot \eta_i}{\sum_{i=1}^{n} Q_i}$$

Where $Q_i$ represents capacity of unit $i$ and $\eta_i$ represents efficiency of unit $i$. This allows mixing equipment with different efficiencies provided the aggregate meets requirements.

Understanding ASHRAE 90.1 equipment efficiency requirements enables proper equipment selection balancing code compliance, first cost, operating cost, and performance characteristics. The comprehensive tables cover virtually all HVAC equipment types, providing clear minimum performance targets. As technology advances and manufacturing costs decrease, these minimums periodically increase through the addenda process, continuously improving building energy performance across new construction and major renovations.
