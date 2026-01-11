---
title: "Psychrometric Analysis for Load Calculations"
description: "Application of psychrometric principles to HVAC load analysis including sensible heat ratio, apparatus dew point, bypass factor, and coil performance determination for cooling system design."
weight: 6
---

## Psychrometric Foundations

Psychrometric analysis provides the graphical and analytical framework for evaluating moist air processes in HVAC systems, directly linking calculated thermal loads to required equipment performance and supply air conditions. The psychrometric chart plots air properties including dry-bulb temperature, wet-bulb temperature, humidity ratio, relative humidity, enthalpy, and specific volume on coordinates that reveal relationships between these interdependent state variables.

Load calculations determine total sensible and latent heat that equipment must remove or add to maintain space conditions. Psychrometric analysis translates these loads into required supply air state points, flow rates, and equipment performance characteristics. The methodology accounts for the coupled nature of temperature and humidity control, ensuring systems provide adequate capacity for both sensible and latent loads at design conditions.

## Sensible Heat Ratio Fundamentals

The sensible heat ratio (SHR) represents the fraction of total cooling load that is sensible rather than latent, mathematically expressed as SHR = q_sensible / q_total. This dimensionless parameter ranges from 0.0 (pure dehumidification) to 1.0 (pure sensible cooling) and determines the required supply air humidity ratio for space humidity control.

Typical commercial building SHR values range from 0.70 to 0.90, with lower values in humid climates or high-occupancy spaces with substantial moisture generation. Residential applications often show SHR values of 0.65-0.80 due to higher ventilation latent loads and occupant moisture generation per unit floor area. Industrial processes with steam or moisture release may exhibit SHR below 0.60, requiring specialized dehumidification equipment.

The room SHR determines the slope of the process line on the psychrometric chart from space conditions to supply air conditions. Lines of constant SHR radiate from the space condition point, with low SHR values requiring colder and drier supply air to remove latent loads while high SHR allows warmer supply air focused on sensible cooling. Equipment selection must provide adequate dehumidification capacity to achieve required supply air humidity ratios.

## Room Sensible Heat Factor

The room sensible heat factor (RSHF) represents the sensible heat ratio of loads directly entering the conditioned space, excluding ventilation and outdoor air loads. RSHF determines the space-to-supply air process line accounting only for internal gains, envelope transmission, and infiltration. This parameter guides supply air temperature selection for terminal units serving individual zones.

RSHF typically exceeds the grand sensible heat factor (GSHF) since ventilation outdoor air loads are handled separately at the air handler rather than within each zone. Spaces with minimal internal moisture generation exhibit high RSHF (0.85-0.95), requiring modest supply air humidity control. High-occupancy spaces or those with moisture sources show lower RSHF (0.60-0.80), demanding drier supply air.

## Grand Sensible Heat Factor

The grand sensible heat factor (GSHF) includes all building loads including ventilation outdoor air sensible and latent components. GSHF determines central air handler coil performance requirements and return air conditions in all-air systems. The GSHF value is always lower than RSHF when outdoor air ventilation introduces latent loads exceeding space latent generation.

In humid climates during peak summer conditions, outdoor air latent loads may dominate total building latent requirements. GSHF values below 0.70 require substantial dehumidification capacity and cold coil leaving air temperatures to achieve required supply air dew points. Energy recovery from exhaust air substantially increases effective GSHF by pre-conditioning outdoor air before entering the cooling coil.

## Effective Sensible Heat Factor

The effective sensible heat factor (ESHF) represents the combined effect of room loads and ventilation air conditioning. The ESHF line on the psychrometric chart extends from space conditions through the mixed air point (mixture of return air and outdoor air) to the coil leaving air conditions. This construction enables determination of required apparatus dew point temperature for cooling coil selection.

The ESHF accounts for bypass factor effects where some supply air passes through the coil without achieving full saturation at the coil surface temperature. Real cooling coils do not bring all air to saturation at the coil surface due to finite contact time and surface area. The bypass factor quantifies this imperfection and determines the required apparatus dew point below the target supply air dew point.

## Apparatus Dew Point

The apparatus dew point (ADP) represents the effective surface temperature of the cooling coil where condensation occurs. The ADP must be sufficiently low to achieve required supply air humidity ratio accounting for bypass factor effects. The psychrometric process line extends from entering air conditions to the ADP, with actual leaving air conditions lying between the ADP and entering conditions based on bypass factor.

Determination of required ADP follows from the bypass factor equation:

BF = (t_leave - t_ADP) / (t_enter - t_ADP)

where temperatures represent dry-bulb values. Rearranging yields:

t_ADP = (t_leave - BF · t_enter) / (1 - BF)

Typical bypass factors range from 0.05-0.15 for commercial cooling coils with 3-6 rows and face velocities of 400-500 fpm. Lower bypass factors (better performance) require more coil rows, lower face velocity, or wet surface treatments that enhance moisture removal.

## Coil Leaving Air Conditions

Supply air temperature selection balances several competing requirements. Lower supply air temperature reduces required airflow rates and duct sizes but increases fan energy, coil capacity, and risk of supply duct condensation. Higher supply temperatures increase airflow and distribution system costs while improving part-load humidity control through reduced bypass of moisture-laden air past the coil.

Typical supply air temperatures range from 52-58°F for commercial systems. Low SHR applications requiring substantial dehumidification may use supply air temperatures of 48-52°F with correspondingly low ADP values requiring chilled water temperatures of 38-42°F or refrigerant evaporator temperatures near 35°F. High SHR sensible-only cooling may use supply temperatures of 58-62°F with reduced dehumidification capacity.

The supply air humidity ratio must equal or be lower than the space humidity ratio by an amount sufficient to offset space latent gains. The mass balance equation relating supply airflow, space latent load, and humidity ratio difference is:

m_dot · (W_space - W_supply) = q_latent / h_fg

where m_dot is mass flow rate, W represents humidity ratios, and h_fg is latent heat of vaporization (approximately 1060 BTU/lb).

## Supply Air Quantity Determination

The required supply air volume flow rate follows from sensible load and temperature difference:

Q = q_sensible / (ρ · cp · ΔT) = q_sensible / (1.08 · ΔT)

where Q is CFM, q_sensible is BTU/hr, and ΔT is temperature difference between space and supply air in °F. The coefficient 1.08 incorporates air density and specific heat at standard conditions.

Larger temperature differences reduce required airflow but may create comfort problems from cold air dumping and high diffuser discharge velocities. Smaller temperature differences increase airflow and distribution system costs. Typical temperature differences of 18-22°F balance these competing factors for conventional overhead supply systems. Underfloor air distribution may use 10-15°F differences due to lower-velocity displacement ventilation principles.

## Part-Load Dehumidification

Systems sized for peak sensible loads may provide inadequate dehumidification during part-load conditions when sensible loads decrease but latent loads remain relatively constant. The part-load SHR decreases below design values, requiring equipment to provide greater dehumidification capacity than available at reduced compressor or chiller output.

Variable-capacity systems including variable-speed compressors, hot gas reheat, and dedicated outdoor air systems maintain better humidity control at part load compared to simple on-off systems. Proper equipment selection requires evaluation of performance across the full range of operating conditions rather than design peak alone. Some applications benefit from separate sensible and latent cooling equipment to independently control temperature and humidity.

## Multiple Zone Systems

Air distribution systems serving multiple zones with different RSHF values face challenges providing appropriate supply air conditions for all zones simultaneously. Single-duct constant-volume systems can satisfy only one zone's humidity requirements at each operating point. Dual-duct, multi-zone, or variable air volume systems with reheat provide better control of both temperature and humidity in diverse zone applications.

Dedicated outdoor air systems (DOAS) precondition ventilation air to neutral or slightly cool-dry conditions, delivering to zones separately from recirculated space air. This separation enables central deep dehumidification of outdoor air while zone terminal units provide only sensible cooling without humidity control responsibility. The DOAS approach suits buildings with high ventilation requirements and varying zone SHR values.
