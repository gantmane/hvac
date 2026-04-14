---
title: "Liquid Overfeed Systems"
aliases: ["Liquid Overfeed Systems"]
weight: 4
---

Liquid overfeed refrigeration systems circulate refrigerant at rates exceeding the evaporation rate, ensuring complete wetting of heat transfer surfaces and maximizing evaporator efficiency. These systems use a low-pressure receiver to separate vapor from liquid, with a pump recirculating liquid refrigerant to multiple evaporators.

## System Architecture

The liquid overfeed system consists of a low-pressure receiver (accumulator), refrigerant pump, liquid distribution piping, evaporators, and vapor return lines. Liquid refrigerant from the high-pressure side feeds into the low-pressure receiver through an expansion valve or float control. The pump draws liquid from the receiver bottom and delivers it to evaporators at a rate 2 to 6 times the evaporation rate.

Vapor generated in the evaporators returns to the low-pressure receiver along with unevaporated liquid. The receiver separates liquid and vapor, with vapor flowing to the compressor suction and liquid remaining available for recirculation. This arrangement maintains consistent liquid feed to all evaporators regardless of load variations.

## Recirculation Ratios

The recirculation ratio defines the mass flow rate of liquid pumped to evaporators divided by the mass flow rate of vapor generated. This parameter fundamentally affects system performance, pump sizing, and piping design.

| Recirculation Ratio | Typical Applications | Advantages | Considerations |
|---------------------|---------------------|------------|----------------|
| 2:1 to 3:1 | Direct expansion retrofit, simple systems | Lower pump power, smaller piping | May have liquid distribution issues |
| 3:1 to 4:1 | Cold storage, process cooling | Good surface wetting, stable operation | Balanced performance and cost |
| 4:1 to 6:1 | Ice rinks, industrial freezers | Excellent heat transfer, uniform temperatures | Higher pump power, larger piping |
| 6:1 to 8:1 | Specialized low-temperature applications | Maximum efficiency, superior distribution | Significant energy penalty, complex control |

Higher recirculation ratios improve heat transfer coefficients by maintaining turbulent flow and complete tube wetting. The relationship between recirculation ratio and evaporator capacity follows:

Q_evap = ṁ_circulated × h_fg × (1 / n)

Where n represents the recirculation ratio. A 4:1 ratio means 25% of circulated liquid evaporates per pass, with 75% returning as liquid to the receiver.

## Low-Pressure Receiver Design

The low-pressure receiver serves as the system's liquid reservoir and vapor-liquid separator. Proper sizing ensures adequate liquid inventory during load fluctuations and effective vapor separation to prevent liquid carryover to the compressor.

### Receiver Sizing Criteria

| Parameter | Typical Value | Basis |
|-----------|---------------|-------|
| Minimum liquid volume | 3-5 minutes pump flow | Prevents pump cavitation during transients |
| Vapor space | 50-60% of total volume | Allows vapor-liquid separation |
| Surge capacity | 1-2 minutes system charge | Accommodates defrost cycles, load changes |
| Length-to-diameter ratio | 3:1 to 5:1 | Optimizes separation efficiency |
| Inlet velocity | < 3 m/s (10 ft/s) | Reduces liquid entrainment |

The receiver must maintain liquid level between high and low limits. Level control typically uses float switches, differential pressure transmitters, or capacitance probes. A low-level alarm prevents pump dry running, while high-level control modulates expansion valve or liquid feed rate.

### Vapor-Liquid Separation

Effective separation requires proper internals design. Inlet nozzles direct return flow tangentially or downward to reduce velocity and promote liquid dropout. Mesh pads or vane-type demisters in the vapor space remove entrained liquid droplets before vapor exits to the compressor.

Return line velocities entering the receiver should remain below 10 m/s (33 ft/s) for ammonia and 15 m/s (50 ft/s) for halocarbon refrigerants. Higher velocities increase liquid entrainment, reducing separation efficiency and potentially causing compressor damage.

## Refrigerant Pump Selection

Liquid overfeed systems require pumps capable of delivering design flow rate against system pressure differential while handling saturated liquid near its boiling point. The Net Positive Suction Head Available (NPSHA) must exceed the Net Positive Suction Head Required (NPSHR) to prevent cavitation.

### Pump Types and Applications

| Pump Type | Operating Range | Advantages | Limitations |
|-----------|-----------------|------------|-------------|
| Centrifugal, single-stage | Flow: 10-200 m³/h<br>Head: 15-60 m | Simple, reliable, low maintenance | Poor performance at low flows |
| Centrifugal, multi-stage | Flow: 5-150 m³/h<br>Head: 60-200 m | Higher pressure capability | More complex, higher cost |
| Regenerative turbine | Flow: 1-50 m³/h<br>Head: 50-150 m | High head at low flows | Limited capacity, lower efficiency |
| Hermetic centrifugal | Flow: 5-100 m³/h<br>Head: 20-80 m | No seal leakage, motor cooling | Motor exposure to refrigerant |

### Pump Sizing Calculations

Total pump flow rate equals the sum of individual evaporator capacities multiplied by the recirculation ratio:

ṁ_pump = Σ(Q_evap,i / h_fg) × n

Where Q_evap,i represents each evaporator's cooling capacity and n is the recirculation ratio.

Required pump head accounts for:
- Elevation difference between receiver and highest evaporator
- Friction losses in liquid supply and return piping
- Pressure drop through evaporators and distribution components
- Control valve pressure drop (if applicable)

Typical total head requirements range from 20 to 100 meters of liquid column (70 to 350 kPa or 10 to 50 psi differential).

### NPSH Considerations

NPSHA equals the receiver pressure head above vapor pressure plus static head minus friction losses in pump suction line. For saturated liquid in the receiver at temperature T_sat:

NPSHA = (P_receiver - P_vapor(T_sat))/ρg + h_static - h_friction

Maintain NPSHA at least 1.5 to 2.0 meters (5 to 7 feet) above pump manufacturer's NPSHR curve at operating flow rate. Subcooling liquid in the receiver by 1-3°C (2-5°F) below saturation temperature significantly improves NPSHA margin.

## System Pressure Differential

The operating pressure differential between high and low sides determines refrigerant distribution and affects overall system efficiency. Low-pressure receiver pressure typically operates 0.5 to 2°C (1 to 4°F) above desired evaporator temperature to account for pressure drops.

| System Temperature | Typical Receiver Pressure | Corresponding Saturation Temperature (Ammonia) |
|--------------------|---------------------------|-----------------------------------------------|
| -40°C (-40°F) | 70-80 kPa abs (10-12 psia) | -38 to -36°C (-36 to -33°F) |
| -30°C (-22°F) | 120-140 kPa abs (17-20 psia) | -28 to -26°C (-18 to -15°F) |
| -20°C (-4°F) | 190-220 kPa abs (28-32 psia) | -18 to -16°C (0 to 3°F) |
| -10°C (14°F) | 280-310 kPa abs (41-45 psia) | -8 to -6°C (18 to 21°F) |
| 0°C (32°F) | 420-450 kPa abs (61-65 psia) | 2 to 4°C (36 to 39°F) |

## Liquid Distribution Systems

Proper liquid distribution to multiple evaporators requires balancing flow through parallel circuits. Distribution methods include:

**Direct feed with individual control valves**: Each evaporator has a dedicated solenoid valve and manual balancing valve. This method provides independent control but requires careful commissioning to balance flows according to design recirculation ratios.

**Central distribution header**: A large header feeds multiple evaporators through branch connections. Header sizing follows velocity criteria: 0.5-1.5 m/s (1.6-5 ft/s) to minimize pressure variations. Branch takeoffs should face upward from the header top to prevent vapor preferential flow.

**Liquid level control**: Float-operated valves at each evaporator maintain constant liquid level, automatically adjusting feed rate to match evaporation. This method provides excellent load following but adds complexity and cost.

## Control Strategies

Level control in the low-pressure receiver regulates high-pressure liquid feed through an expansion valve or float-operated valve. A proportional level control modulates the expansion valve to maintain receiver level between 40% and 60% full during normal operation.

Pump operation typically runs continuously, with backup pumps for redundancy in critical applications. Variable speed drives adjust pump flow in response to system load, reducing energy consumption during low-load conditions.

Evaporator temperature control uses solenoid valves to start/stop liquid feed to individual evaporators, or variable frequency drives on dedicated pumps for zones requiring different temperatures.

## Advantages Over Direct Expansion

Liquid overfeed systems offer several performance benefits compared to direct expansion (DX) systems:

- **Enhanced heat transfer**: Complete tube wetting increases evaporator heat transfer coefficients by 15-30%
- **Uniform distribution**: Equal liquid supply to all circuits eliminates refrigerant maldistribution
- **Higher evaporator efficiency**: Saturated evaporation throughout maintains maximum temperature differential
- **Multiple evaporator capability**: Single refrigeration system serves many evaporators at similar temperatures
- **Reduced compressor superheat**: Eliminates superheat zone in evaporators, maximizing effective heat transfer area
- **Better oil management**: Oil returns to receiver where it can be removed, rather than accumulating in evaporators

## System Design Considerations

Pipe sizing follows different criteria than DX systems. Liquid supply lines size for 0.5-1.5 m/s velocity, balancing pressure drop against line cost. Suction return lines must accommodate both vapor and entrained liquid at 10-20 m/s velocity.

All evaporators in a liquid overfeed system should operate within 3-5°C (5-9°F) of each other. Wider temperature ranges require separate pumped circuits or pressure-controlled intermediate vessels.

Receiver location should be at or below the lowest evaporator elevation to ensure gravity return of liquid-vapor mixture. When evaporators are at multiple elevations, return line sizing must prevent excessive pressure drop that would compromise higher evaporators.

System refrigerant charge typically exceeds DX systems by 50-150% due to liquid inventory in the receiver and distribution piping. This increases initial cost but provides operating advantages in system stability and efficiency.
