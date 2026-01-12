---
title: "VAV Terminal Units"
description: "Technical analysis of variable air volume terminal units including pressure-dependent and pressure-independent control, flow measurement, damper operation, reheat configurations, and selection criteria for VAV systems."
weight: 9
---

Variable air volume (VAV) terminal units modulate airflow to zones in response to thermal load variations while maintaining supply air temperature relatively constant at the central air handling unit. These devices represent the critical interface between the primary distribution system and the conditioned space, directly controlling thermal delivery through volumetric flow adjustment.

## Terminal Unit Classification

VAV terminals are categorized by control method, duct configuration, and auxiliary heating capability.

**Single-Duct VAV Terminals**

Single-duct units receive air from one supply duct and modulate flow through damper position. Cooling-only units provide no supplemental heating. VAV reheat units incorporate heating coils downstream of the damper to satisfy heating loads or maintain minimum ventilation requirements during low-load conditions.

**Dual-Duct VAV Terminals**

Dual-duct terminals receive air from both cold and hot supply ducts, mixing the streams to achieve the required discharge temperature. The unit modulates dampers in each duct to control the ratio of hot to cold air. This configuration eliminates the need for terminal reheat but requires two complete duct distribution systems, resulting in higher first cost and spatial requirements.

**Fan-Powered Terminals**

Fan-powered units incorporate an integral fan that induces return or plenum air, mixing it with primary air from the central system. Series fan-powered units operate the fan continuously, providing constant discharge volume with variable primary air. Parallel fan-powered units energize the fan only when primary airflow falls below a setpoint, typically during heating mode.

## Control Methods

The fundamental distinction in VAV terminal control lies in the response to upstream pressure variations.

**Pressure-Dependent Control**

Pressure-dependent terminals modulate damper position based solely on zone temperature demand without compensating for supply duct pressure fluctuations. The relationship between damper position and airflow varies with upstream static pressure:

**Q** = **C<sub>d</sub>A**√(2**ΔP**/**ρ**)

where **C<sub>d</sub>** is the discharge coefficient, **A** is the effective damper opening area, **ΔP** is the pressure differential across the damper, and **ρ** is air density.

This configuration provides acceptable performance when duct static pressure remains stable, typically in smaller systems with minimal load diversity. Installed cost is lower due to the absence of flow measurement devices.

**Pressure-Independent Control**

Pressure-independent terminals incorporate airflow measurement and control logic to maintain setpoint flow rates regardless of upstream pressure variations. The controller continuously compares measured flow against setpoint and modulates the damper to achieve the target, effectively decoupling flow rate from system pressure fluctuations.

This control method is essential for systems serving multiple zones with diverse load patterns, ensuring each terminal receives design airflow independent of other zone demands. The additional cost of flow sensors and more sophisticated controls is justified by improved zone control and system stability.

## Flow Measurement Technologies

Accurate airflow measurement is fundamental to pressure-independent control.

**Flow Rings and Stations**

Flow measurement rings create a defined pressure drop across multiple sensing points around the duct circumference. The ring typically contains several total pressure and static pressure taps connected to manifolds. The differential pressure between manifolds relates to velocity pressure:

**V** = 4005√(**ΔP**/**ρ**)

where **V** is velocity in fpm and **ΔP** is in inches of water column at standard conditions. Volumetric flow is calculated as **Q** = **VA**, where **A** is the duct cross-sectional area.

**Thermal Dispersion Sensors**

Thermal mass flow sensors measure air velocity by detecting heat transfer from an electrically heated element. These devices provide direct velocity measurement without introducing significant pressure loss, though they require periodic calibration to maintain accuracy across the operating range.

## Airflow Limits and Turndown

Terminal units operate between defined minimum and maximum flow limits to satisfy ventilation requirements and control authority.

**Maximum Airflow**

Maximum flow is established by zone cooling load calculations and typically occurs at design conditions. The terminal damper is fully open, and flow is limited only by upstream pressure and unit pressure drop characteristics. Manufacturers publish maximum certified flow ratings based on inlet static pressure and allowable total pressure drop.

**Minimum Airflow**

Minimum flow setpoints serve multiple functions: maintaining minimum ventilation rates per ASHRAE Standard 62.1, ensuring adequate air motion for comfort and mixing, and providing sufficient flow for stable control. Typical minimum flow ratios range from 20% to 50% of maximum design flow.

The minimum ventilation requirement from Standard 62.1 is:

**V<sub>oz</sub>** = **R<sub>p</sub>P<sub>z</sub>** + **R<sub>a</sub>A<sub>z</sub>**

where **V<sub>oz</sub>** is the required outdoor airflow, **R<sub>p</sub>** is the per-person outdoor air rate, **P<sub>z</sub>** is the zone population, **R<sub>a</sub>** is the per-area outdoor air rate, and **A<sub>z</sub>** is the zone floor area.

Minimum flow must be adjusted for system ventilation efficiency per the standard's ventilation rate procedure, particularly in systems with significant load diversity.

**Turndown Ratio**

Turndown ratio, defined as maximum flow divided by minimum flow, affects control stability and energy performance. Higher turndown ratios (lower minimums) reduce fan energy and reheat penalties but may compromise ventilation delivery and control stability. Ratios of 3:1 to 5:1 are common, though some applications achieve 10:1 with proper sensor selection and commissioning.

## Reheat Configurations

Reheat coils in single-duct VAV terminals address heating loads and temperature control during low-flow conditions.

**Hot Water Reheat**

Hot water coils use hydronic heating water, typically 120°F to 180°F supply temperature. Two-way control valves modulate water flow to maintain discharge air temperature setpoint. The heating capacity is:

**q** = **m<sub>air</sub>c<sub>p</sub>**(**T<sub>discharge</sub>** - **T<sub>supply</sub>**)

where **m<sub>air</sub>** is the air mass flow rate, **c<sub>p</sub>** is the specific heat of air, **T<sub>discharge</sub>** is the desired discharge temperature, and **T<sub>supply</sub>** is the primary air temperature.

Hot water reheat provides superior energy performance compared to electric reheat when the heating plant operates efficiently. The centralized heating source allows heat recovery, condensing boiler operation, or renewable thermal energy integration.

**Electric Reheat**

Electric resistance coils provide heating through direct energy conversion. Staged or SCR-controlled elements modulate capacity from 0% to 100%. Electric reheat simplifies installation by eliminating piping and condensate drainage but operates at source energy conversion efficiencies near 33% when accounting for power generation losses.

Electric reheat is typically specified when: hot water distribution is impractical, the number of reheat zones is small, heating load is minimal, or utility rate structures favor electric resistance heating.

## Damper Operation and Control Sequences

VAV terminal dampers modulate between minimum and maximum positions following defined control sequences.

**Cooling Mode Sequence**

During cooling, the zone thermostat signal modulates the damper from minimum to maximum position as zone temperature rises above setpoint. In pressure-independent units, the controller maintains airflow at the damper position setpoint while compensating for supply pressure variations.

When airflow reaches maximum and zone temperature continues to rise, the space is in cooling saturation. The terminal can deliver no additional capacity without reducing supply air temperature at the central unit or accepting elevated space temperature.

**Heating Mode Sequence**

Heating sequences vary by terminal configuration. In VAV reheat units, as zone temperature falls below setpoint, the damper typically maintains minimum position while the reheat coil modulates to increase discharge temperature. Some sequences drive the damper toward maximum position during heating to increase air circulation before or concurrent with reheat activation.

In series fan-powered terminals, the fan operates continuously. During heating, primary airflow reduces to minimum while the fan induces plenum air across the heating coil. The mixing of cool primary air with heated induced air satisfies the heating load.

In parallel fan-powered terminals, the fan energizes when primary flow falls to minimum and heating is required. The fan draws plenum air across the heating coil while primary airflow is minimized, reducing central system fan energy during heating operation.

## Selection and Sizing Criteria

Proper terminal unit selection ensures adequate capacity, acceptable acoustics, and stable control performance.

**Capacity Verification**

Manufacturers provide performance data correlating airflow to inlet static pressure and total pressure drop. The specified terminal must deliver maximum design airflow at the available inlet pressure while maintaining total pressure drop within acceptable limits (typically 0.25 to 0.5 in. w.c. at maximum flow).

The inlet static pressure available at the terminal is:

**P<sub>inlet</sub>** = **P<sub>fan</sub>** - **ΔP<sub>duct</sub>** - **ΔP<sub>fittings</sub>**

where **P<sub>fan</sub>** is the system static pressure at the air handling unit, **ΔP<sub>duct</sub>** is pressure loss in the supply duct to the terminal, and **ΔP<sub>fittings</sub>** is the loss through fittings and transitions.

**Acoustic Considerations**

Terminal units generate noise through turbulent airflow across the damper and through the unit casing. Manufacturers publish sound power levels in octave bands for various flow rates and inlet pressures. The designer must verify that terminal-generated noise, when attenuated by duct lining and terminal distance from the occupied space, meets the design noise criterion (NC) level.

Critical noise-sensitive spaces may require sound traps, acoustically lined ductwork downstream of the terminal, or selection of oversized units operating at reduced velocities and pressure drops.

**Physical and Installation Constraints**

Terminal unit selection must consider available ceiling space, required clearances for service access, duct connection orientation, and structural support. Reheat coils require condensate drainage for hot water applications (installed with piping sloped against airflow direction). Electric reheat units require appropriate voltage and circuit protection.

Manufacturers specify minimum upstream and downstream straight duct lengths to ensure proper flow measurement accuracy. Installations violating these requirements may experience control instability and inability to achieve calibrated airflow rates.

**Control Integration**

The terminal controller must communicate with the building automation system through compatible protocols (BACnet, LonWorks, Modbus). The system architecture determines whether zone temperature sensors integrate with the terminal controller or connect directly to the building system with airflow setpoints commanded to the terminal.

According to ASHRAE Guideline 36, high-performance sequences for VAV systems include trim and respond logic to reset minimum airflows based on actual ventilation requirements, static pressure reset to minimize fan energy, and coordinated control between cooling and heating modes to prevent simultaneous operation.
