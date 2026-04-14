---
title: "Pumps and Fans"
aliases: ["Pumps and Fans"]
description: "Performance curves, affinity laws, system operating points, NPSH requirements, efficiency optimization, and VFD applications for HVAC pumps and fans"
weight: 10
---

Pumps and fans are the prime movers in HVAC systems, consuming 30-50% of building energy. Understanding their performance characteristics, selection criteria, and control strategies is fundamental to efficient system design and operation.

## Performance Curves

Equipment manufacturers provide performance curves that define the relationship between flow rate and the pressure developed by the machine. For pumps, this is head (feet of water or meters) versus flow (gpm or L/s). For fans, it is static pressure (inches w.g. or Pa) versus airflow (cfm or L/s).

The pump or fan curve represents the energy added to the fluid at various flow rates for a given impeller diameter and rotational speed. These curves typically slope downward from left to right—as flow increases, the pressure developed decreases. The shape depends on impeller design: centrifugal pumps and backward-curved fans have continuously drooping curves, while forward-curved fans may exhibit a saddle shape.

Key points on the performance curve:

- **Shutoff head/pressure**: Maximum pressure at zero flow
- **Peak efficiency point**: Where the machine operates most efficiently (BEP for pumps)
- **Free delivery**: Maximum flow at zero pressure rise
- **Stable operating region**: Portion of curve without flow instabilities

## System Curves

The system curve represents the resistance to flow in the distribution network. It follows the relationship:

ΔP = ΔP₀ + K × Q²

where ΔP₀ is static pressure (elevation head for pumps, fixed resistances), K is the system resistance coefficient, and Q is flow rate. This parabolic relationship reflects the fact that friction losses increase with the square of velocity.

The system curve shifts based on:

- **Valve positions**: Throttling increases K
- **Filter loading**: Dirty filters increase resistance
- **Coil fouling**: Scaling or dirt accumulation
- **Control dampers**: Modulation changes system resistance

## Operating Point

The intersection of the equipment curve and system curve defines the operating point—the actual flow and pressure at which the system operates. This point represents equilibrium: the pressure developed by the pump or fan exactly matches the pressure required to overcome system resistance at that flow rate.

Proper selection ensures the operating point occurs near the equipment's peak efficiency. Operating far from this point results in energy waste, increased noise, and potential mechanical issues. For pumps, operation too far left on the curve can cause recirculation and cavitation; too far right results in overloading and excessive flow velocity.

## Affinity Laws

The affinity laws govern how pump and fan performance changes with impeller speed (N), diameter (D), or fluid density (ρ). These relationships are essential for VFD applications and impeller trimming:

**Flow**: Q₂/Q₁ = (N₂/N₁) × (D₂/D₁)

**Pressure**: ΔP₂/ΔP₁ = (N₂/N₁)² × (D₂/D₁)² × (ρ₂/ρ₁)

**Power**: P₂/P₁ = (N₂/N₁)³ × (D₂/D₁)³ × (ρ₂/ρ₁)

The cubic relationship between speed and power is the foundation of VFD energy savings. Reducing speed by 20% cuts power consumption by approximately 50%. Since system curves are parabolic and equipment curves shift with speed, the new operating point at reduced speed follows a cubic power reduction even though flow decreases only linearly with speed.

## Net Positive Suction Head (NPSH)

NPSH prevents cavitation in pumps by ensuring adequate pressure at the impeller inlet. Two values define the requirement:

**NPSH Required (NPSHR)**: Minimum pressure needed at pump inlet to prevent vapor bubble formation, provided by manufacturer and increases with flow rate.

**NPSH Available (NPSHA)**: Actual pressure at pump inlet, calculated from system conditions:

NPSHA = P_atm + P_static - P_friction - P_vapor

where P_atm is atmospheric pressure, P_static is elevation head, P_friction is suction line losses, and P_vapor is fluid vapor pressure at operating temperature.

Safe operation requires NPSHA > NPSHR with a margin of 3-5 feet. Insufficient NPSH causes cavitation: violent collapse of vapor bubbles that damages impellers, creates noise, and reduces performance. Hot water and high-altitude installations are particularly vulnerable due to reduced NPSHA.

## Efficiency and Power

Equipment efficiency is the ratio of hydraulic power output to electrical power input:

η = (Q × ΔP) / (3960 × P_input) for pumps (Q in gpm, ΔP in ft, P in HP)

η = (Q × ΔP) / (6356 × P_input) for fans (Q in cfm, ΔP in in. w.g., P in HP)

Efficiency varies across the performance curve, peaking at the best efficiency point (BEP). Operating away from BEP wastes energy and accelerates wear. Wire-to-fluid efficiency accounts for motor and VFD losses:

η_system = η_pump/fan × η_motor × η_VFD

Modern premium-efficiency motors achieve 94-96% efficiency, while VFDs add 2-4% losses. Total system efficiency typically ranges from 50-70% for well-designed systems.

Power calculations follow:

**Brake horsepower**: BHP = (Q × ΔP) / (3960 × η) for pumps

**Fan power**: BHP = (Q × ΔP) / (6356 × η) for fans

Motor selection must account for service factors (typically 1.15) and ensure the motor can handle maximum load conditions without overheating.

## VFD Effects on Performance

Variable frequency drives modulate equipment speed to match varying loads, providing substantial energy savings compared to throttling or inlet vane control. As frequency decreases from 60 Hz, the entire performance curve shifts downward according to affinity laws.

Critical VFD considerations:

**Minimum speed limits**: Most equipment should not operate below 30-40% of design speed due to inadequate bearing lubrication, motor cooling, and acoustic resonances.

**Multiple pump/fan staging**: Combining VFD control with sequencing on/off equipment optimizes efficiency across the full load range.

**Pressure setpoint reset**: Reducing the system pressure setpoint as load decreases (trimming the system curve downward) compounds VFD savings.

**Harmonic distortion**: VFDs generate electrical harmonics that may require line reactors or filters to protect upstream equipment.

## Selection Methodology

ASHRAE Fundamentals Chapter 24 (Fans) and Chapter 44 (Pumps) provide detailed selection procedures:

1. Calculate required flow rate from load analysis
2. Determine system pressure requirement from pipe/duct sizing
3. Plot system curve including all resistances
4. Select equipment with operating point near BEP (within 80-110% of BEP flow)
5. Verify adequate NPSH margin (pumps) and motor capacity
6. Evaluate part-load efficiency for variable-flow applications
7. Consider redundancy and future expansion

Oversizing equipment is a common error that results in operation far left on the curve with poor efficiency, excessive noise, and control instabilities. Accurate load calculations and conservative safety factors (10-15% maximum) prevent oversizing while ensuring adequate capacity.

Proper pump and fan selection, combined with VFD control and setpoint optimization, represents one of the highest-return efficiency opportunities in HVAC systems. Understanding the physics of fluid machinery performance enables designers to specify equipment that delivers required performance while minimizing energy consumption and maintenance costs.

