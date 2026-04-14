---
title: "Fan Powered Terminals"
aliases: ["Fan Powered Terminals"]
description: "Fan-powered VAV terminal units with integrated fans for constant air volume delivery, series and parallel fan configurations, heating coil integration, control sequences, and energy performance analysis for commercial HVAC systems."
weight: 3
---

Fan-powered VAV terminal units integrate a small blower within the terminal box to maintain constant air volume delivery to the conditioned space while varying the primary air flow rate from the central air handler. These units address the limitations of standard VAV terminals by providing continuous air circulation, improved air distribution, and enhanced heating capability during low-load conditions.

## Operating Principle

Fan-powered terminals receive variable primary air from the central system and mix it with plenum or recirculated air drawn by the integral fan. The combined airflow maintains a constant volumetric flow rate to the diffusers, ensuring consistent air distribution and room air motion regardless of cooling load variations. This approach prevents the stagnant air conditions and thermal stratification that can occur with standard VAV terminals at low flow rates.

The terminal fan operates continuously or intermittently depending on configuration and control strategy. Primary air volume modulates from maximum cooling flow down to minimum ventilation requirements, with the terminal fan making up the difference to maintain constant discharge volume.

## Series Fan Configuration

Series fan-powered terminals position the fan downstream of the mixing section, forcing all primary and plenum air through the fan before delivery to the space. The primary air damper modulates to control cooling capacity while the fan runs continuously during occupancy.

**Operating characteristics:**

- Primary air passes through the fan during all operating modes
- Fan operates continuously when space is occupied
- Mixing occurs upstream of fan, ensuring thorough blending
- Discharge air temperature varies based on primary/plenum air ratio
- Heating coil (if present) located in discharge airstream

Series configuration provides superior air mixing and more uniform discharge temperatures. The continuous fan operation creates steady air motion in the space, improving occupant comfort and eliminating the cycling air currents associated with intermittent fan operation. However, continuous fan operation increases energy consumption compared to parallel configurations.

During heating mode, the primary air damper closes to minimum position (typically 30-50% of maximum cooling flow to maintain code-required ventilation), and the fan draws predominantly plenum air across the heating coil. The constant fan operation ensures consistent heat distribution even when heating loads are low.

## Parallel Fan Configuration

Parallel fan-powered terminals arrange the fan in a bypass configuration where primary air can flow directly to the discharge or mix with fan-induced plenum air. The fan operates only when the primary air volume falls below the desired discharge volume, typically during heating mode or low cooling loads.

**Operating characteristics:**

- Primary air bypasses fan during high cooling loads
- Fan cycles on when primary flow drops below setpoint
- Lower fan energy consumption than series configuration
- Discharge air velocity varies with operating mode
- Less thorough mixing of primary and plenum air streams

The parallel arrangement reduces fan operating hours by 40-60% compared to series units, significantly lowering energy consumption. During maximum cooling, all airflow comes from primary air flowing directly through the unit. As cooling load decreases and primary air volume reduces, the fan energizes to maintain constant discharge volume by inducing plenum air.

This configuration presents higher first cost due to the more complex damper arrangement and controls required to coordinate primary air modulation with fan operation. The intermittent fan operation can create noticeable changes in room air motion as the fan cycles, potentially affecting occupant comfort in sound-sensitive spaces.

## Heating Coil Integration

Fan-powered terminals commonly incorporate hot water or electric resistance heating coils to provide space heating without relying solely on heat recovery from the plenum or primary air reheat. The coil location differs between configurations:

**Series units:** Heating coil positioned in discharge airstream downstream of fan, experiencing constant airflow equal to room supply volume. This location ensures consistent heat transfer coefficients and predictable heating capacity.

**Parallel units:** Heating coil typically located in induced air path, experiencing variable airflow depending on fan operation. Some designs place coils in discharge airstream for more consistent performance.

Hot water coils connect to the building's heating water system (typically 140-180°F supply temperature) through a two-way modulating control valve. Electric coils use staged or SCR control for capacity modulation. Coil selection must account for the lower airflow rates in fan-powered terminals compared to central air handlers, requiring higher water temperature differentials or more coil rows to achieve desired capacity.

## Control Sequences

Fan-powered terminal control integrates space temperature control, primary air volume regulation, fan operation, and heating coil modulation into coordinated sequences.

**Cooling sequence:**

1. Space temperature rises above setpoint
2. Primary air damper opens from minimum toward maximum position
3. Discharge air temperature decreases as more cold primary air enters
4. Series fan continues running; parallel fan may shut off at high flow
5. Primary air volume reaches maximum at peak cooling load

**Heating sequence:**

1. Space temperature falls below setpoint
2. Primary air damper modulates to minimum ventilation position
3. Terminal fan energizes (parallel) or continues operation (series)
4. Plenum air volume increases to maintain constant discharge
5. Heating coil valve opens to raise discharge temperature
6. Coil output modulates to maintain space temperature setpoint

Modern DDC systems implement sophisticated control algorithms including discharge air temperature reset, fan speed modulation (for ECM-equipped units), and optimized changeover between cooling and heating modes. Proper minimum primary air settings ensure adequate ventilation air delivery while preventing overcooling during heating mode.

## Energy Performance Comparison

The selection between series and parallel configurations involves balancing first cost, energy consumption, comfort performance, and application requirements.

| Parameter | Series Configuration | Parallel Configuration |
|-----------|---------------------|------------------------|
| Fan operating hours | Continuous during occupancy | Intermittent, 40-60% reduction |
| Annual fan energy | 3,500-5,000 kWh per unit | 1,400-2,000 kWh per unit |
| Air mixing effectiveness | Excellent, uniform discharge | Good, some stratification possible |
| Discharge air motion | Constant, steady | Variable with fan cycling |
| Heating mode performance | Consistent, predictable | Good, slightly variable |
| Acoustic performance | Steady background sound | Cycling noise as fan starts/stops |
| First cost | Lower | Higher (complex damper arrangement) |
| Maintenance | Standard | More components to maintain |

Series units consume approximately 2,500-3,000 additional kWh annually per terminal compared to parallel units due to continuous fan operation. For a building with 100 fan-powered terminals, this represents 250,000-300,000 kWh per year, equivalent to $25,000-$45,000 in annual operating costs depending on electricity rates.

However, series units provide superior comfort in perimeter zones with high heating loads, applications requiring constant air motion for process reasons, and sound-sensitive spaces where fan cycling noise is objectionable. Parallel units excel in interior zones with moderate heating loads, energy-conscious designs, and applications where cycling air motion is acceptable.

## Application Considerations

**Perimeter zones:** Series units preferred for consistent heating performance and elimination of cold drafts during low-load conditions. Continuous air circulation prevents temperature stratification near exterior walls and windows.

**Interior zones:** Parallel units appropriate where heating loads are minimal and energy efficiency is prioritized. Reduced fan operation lowers cooling load on central system by minimizing heat added to airstream.

**Ceiling plenum temperature:** Both configurations rely on adequate plenum air temperature during heating mode. Plenum temperatures below 70°F may require larger heating coils or supplemental heat sources. Heat recovery from lighting (where T-bar fluorescent fixtures discharge heat to plenum) improves heating mode efficiency.

**Ventilation air delivery:** Minimum primary air settings must ensure required outdoor air reaches each zone under all operating conditions. Series units with low minimum settings may compromise ventilation during extended heating operation.

**Sound considerations:** Specify acoustically lined casings and low-sone fans for occupied spaces with NC 30-35 design criteria. Parallel units require careful fan cycling control to minimize start/stop noise transmission.

**Fan motor technology:** ECM motors reduce energy consumption by 30-50% compared to PSC motors and enable continuous fan speed modulation for optimal comfort and efficiency. The higher first cost is typically justified by energy savings within 2-3 years.

## Maintenance Requirements

Fan-powered terminals require periodic maintenance to ensure proper performance and energy efficiency:

- Fan and motor inspection every 6 months, lubrication if required
- Filter replacement quarterly or per pressure drop monitoring
- Damper actuator calibration and linkage inspection annually
- Heating coil inspection for air leakage and water flow annually
- Control valve operation verification and strainer cleaning annually
- Airflow measurement and balancing verification every 2-3 years

Accessible installation locations simplify maintenance and reduce service costs. Ceiling-mounted units should include adequate access panels and clearances for filter changes and component replacement without extensive disassembly.
