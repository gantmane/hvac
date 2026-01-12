---
title: "Liquid Overfeed System Piping Design"
description: "Comprehensive technical guide to liquid overfeed refrigeration piping design including liquid supply lines, wet return lines, two-phase flow considerations, velocity limitations, pressure drop calculations, and piping specifications for industrial refrigeration systems."
weight: 8
---

Liquid overfeed piping systems require careful design to manage two-phase refrigerant flow, maintain proper oil return, and ensure reliable operation across varying load conditions. The piping network must accommodate liquid feed to evaporators, vapor return from evaporators, and liquid return to the low-pressure receiver while minimizing pressure drop and maintaining adequate refrigerant velocities.

## System Piping Overview

Liquid overfeed systems consist of three primary piping circuits:

**Liquid Supply Lines** transport high-pressure liquid refrigerant from the receiver to the evaporator distribution points. These lines operate under subcooled conditions and must be sized to prevent flash gas formation.

**Wet Suction Lines** return low-pressure refrigerant vapor from evaporators to the compressor suction. Unlike dry expansion systems, these lines may contain entrained liquid droplets and require higher velocities for proper oil entrainment.

**Liquid Return Lines** convey excess liquid refrigerant from evaporators back to the low-pressure receiver. These lines operate under gravity flow or slight pressure differential and must accommodate two-phase flow conditions.

The interconnection of these circuits creates a complex hydraulic system where pressure drops in one circuit affect refrigerant distribution in others.

## Liquid Supply Line Sizing

Liquid supply lines from the high-pressure receiver to evaporators must maintain subcooled liquid conditions throughout the piping network. Flash gas formation reduces system capacity and creates erratic refrigerant distribution.

### Subcooling Requirements

Minimum subcooling at evaporator inlet:

| Refrigerant | Minimum Subcooling | Recommended Subcooling |
|-------------|-------------------|----------------------|
| R-717 (Ammonia) | 3°F | 5-10°F |
| R-22 | 5°F | 8-12°F |
| R-404A | 5°F | 8-12°F |
| R-507A | 5°F | 8-12°F |

Subcooling must exceed the temperature equivalent of total pressure drop in the liquid line plus a safety margin. For every 1 psi pressure drop, approximately 0.5-1.0°F of additional subcooling is required depending on refrigerant properties.

### Velocity Limitations

Maximum liquid line velocities prevent erosion, noise, and pressure drop:

| Pipe Size | Maximum Velocity | Typical Design Velocity |
|-----------|-----------------|------------------------|
| 1/2" - 1" | 300 ft/min | 150-200 ft/min |
| 1-1/4" - 2" | 300 ft/min | 150-250 ft/min |
| 2-1/2" - 4" | 400 ft/min | 200-300 ft/min |
| 5" and larger | 500 ft/min | 250-400 ft/min |

Lower velocities reduce pressure drop but increase system refrigerant charge. Higher velocities approaching maximum limits should only be used for short runs.

### Pressure Drop Allowances

Total liquid line pressure drop from receiver to evaporator inlet should not exceed:

- **Ammonia systems**: 3-5 psi maximum
- **Halocarbon systems**: 2-4 psi maximum

Pressure drop consists of friction losses in straight pipe, fittings, valves, and accessories. Use the Darcy-Weisbach equation for friction loss:

ΔP = f × (L/D) × (ρV²/2)

Where:
- f = Darcy friction factor
- L = pipe length
- D = pipe diameter
- ρ = refrigerant density
- V = refrigerant velocity

For preliminary sizing, allow 0.5-1.0 psi per 100 ft equivalent length of piping.

## Wet Return Line Design

Wet return lines convey two-phase refrigerant mixture from evaporators back to the low-pressure receiver. These lines operate under more complex hydraulic conditions than single-phase piping.

### Two-Phase Flow Regimes

Refrigerant flow in wet return lines exists in several regimes depending on velocity and liquid fraction:

**Stratified Flow** occurs at low velocities where liquid flows along the pipe bottom and vapor flows above. This condition can trap liquid and impede oil return.

**Slug Flow** develops when liquid waves bridge the pipe cross-section, creating alternating plugs of liquid and vapor. Slug flow causes pressure fluctuations and mechanical stress.

**Annular Flow** forms at higher velocities where liquid forms a film on pipe walls with vapor flowing in the core. This regime provides good oil entrainment.

**Mist Flow** occurs at very high velocities where liquid droplets are suspended in the vapor stream. This condition provides excellent oil return but high pressure drop.

### Minimum Velocity Requirements

Wet return lines must maintain minimum velocities for oil entrainment under all operating conditions:

| Pipe Orientation | Minimum Velocity (ft/min) | Design Velocity (ft/min) |
|-----------------|---------------------------|-------------------------|
| Horizontal lines | 500-700 | 800-1200 |
| Vertical risers (upflow) | 1000-1500 | 1500-2000 |
| Vertical downflow | 300-500 | 500-800 |

Minimum velocities increase with pipe diameter and for refrigerants with lower density. Calculate actual minimum velocity using:

V_min = 3000 / √(ρ_vapor)

Where ρ_vapor is vapor density in lb/ft³ at operating conditions.

### Double Riser Configuration

Vertical wet return risers require special consideration. For systems operating over wide load ranges, double riser configurations prevent liquid trapping during low load operation:

| Load Range | Riser Configuration | Small Riser Size | Large Riser Size |
|------------|-------------------|------------------|------------------|
| 100-50% | Single riser | - | Full capacity |
| 100-25% | Double riser | 25-30% capacity | 70-75% capacity |
| 100-10% | Double riser + trap | 10-15% capacity | 85-90% capacity |

The small riser maintains minimum velocity at low loads while the large riser handles full capacity. Check valves or solenoids direct flow between risers based on load conditions.

## Liquid Return Line Sizing

Liquid return lines drain excess refrigerant from evaporator outlets back to the low-pressure receiver. These lines operate primarily under gravity flow but may contain flashing refrigerant.

### Gravity Flow Design

Size liquid return lines for 50-70% liquid fill at design capacity. Partially filled pipes provide vapor space to accommodate pressure equalization and prevent liquid seal formation.

Line slope toward the receiver should be minimum 1/4 inch per 10 feet (2% grade). Avoid upward loops that can trap liquid. Where upward rises are unavoidable, install drain traps or pump-out provisions.

### Flash Gas Considerations

Liquid draining to the receiver may flash if pressure drop exceeds available subcooling. Flash gas reduces effective line capacity and can cause flow instability.

Estimate flash gas fraction:

X = (h_in - h_f) / (h_fg)

Where:
- h_in = enthalpy of liquid entering return line
- h_f = saturated liquid enthalpy at receiver pressure
- h_fg = enthalpy of vaporization at receiver pressure

For flash gas fractions above 5%, increase line size to accommodate two-phase flow using appropriate multipliers (typically 1.5-2.0× single-phase capacity).

## Pressure Drop Analysis

Total system pressure drop affects evaporator performance and compressor efficiency. Budget pressure drop allocation across system components:

| Component | Pressure Drop Budget |
|-----------|---------------------|
| Liquid line (receiver to evaporator) | 2-4 psi |
| Evaporator distributor/control valve | 20-40 psi |
| Evaporator coil | 2-5 psi |
| Wet suction line (evaporator to compressor) | 1-2 psi |
| Liquid return line | 0.5-1 psi |
| **Total system** | **25-52 psi** |

Each psi of suction line pressure drop reduces system capacity by approximately 1-2% and increases compressor power consumption by 2-3%.

## Piping Material Specifications

### Ammonia Systems

| Pipe Size | Schedule | Wall Thickness | Max Pressure Rating |
|-----------|----------|----------------|-------------------|
| 1/2" - 2" | 40 | Standard | 700 psi @ 100°F |
| 2-1/2" - 8" | 40 | Standard | 500 psi @ 100°F |
| 10" - 12" | 20 | Standard | 300 psi @ 100°F |
| 14" and larger | 10 | Standard | 250 psi @ 100°F |

Steel pipe must be seamless or electric-resistance welded. Avoid copper, brass, or copper alloys in ammonia service due to corrosion.

### Halocarbon Systems

| Pipe Size | Type | Temper | Application |
|-----------|------|--------|-------------|
| 1/8" - 1-5/8" | ACR Copper | Drawn | Liquid and suction lines |
| 2-1/8" - 4-1/8" | ACR Copper | Annealed | Suction lines, large liquid lines |
| 5" and larger | Steel Schedule 40 | - | Main headers and risers |

Type L copper tube is standard for halocarbon refrigerants. Use brazed joints with 15% silver alloy minimum.

## Installation Requirements

### Piping Slope

Maintain continuous slope in all piping to promote drainage and oil flow:

| Line Type | Minimum Slope | Direction |
|-----------|--------------|-----------|
| Liquid supply | 1/4" per 10 ft | Toward evaporators |
| Wet suction | 1/2" per 10 ft | Toward compressor |
| Liquid return | 1/4" per 10 ft | Toward receiver |

Avoid pockets, sags, or reverse slopes that trap liquid or oil. Where unavoidable, install drain connections with valves.

### Support Spacing

Proper pipe support prevents sagging and maintains slope:

| Nominal Pipe Size | Maximum Support Spacing |
|------------------|------------------------|
| 1/2" - 1" | 6-8 ft |
| 1-1/4" - 2" | 8-10 ft |
| 2-1/2" - 4" | 10-12 ft |
| 5" - 8" | 12-14 ft |
| 10" and larger | 14-16 ft |

Support vertical risers independently at each floor level. Use slide supports or expansion loops to accommodate thermal movement.

### Insulation Requirements

Insulate all low-pressure piping to prevent condensation and heat gain:

| Operating Temperature | Insulation Thickness | Vapor Barrier |
|---------------------|---------------------|---------------|
| 20°F to 40°F | 1" - 1-1/2" | Required |
| 0°F to 20°F | 1-1/2" - 2" | Required |
| -20°F to 0°F | 2" - 2-1/2" | Required |
| Below -20°F | 2-1/2" - 3" | Required |

Use closed-cell elastomeric foam or polyisocyanurate insulation with integral or applied vapor barrier. Seal all joints and penetrations to prevent moisture intrusion.

## System Balancing and Commissioning

Verify proper piping performance during commissioning:

1. **Pressure drop verification**: Measure actual pressure drops and compare to design values
2. **Refrigerant distribution**: Confirm equal feed to multiple evaporators
3. **Oil return**: Verify oil return rate at minimum and maximum load
4. **Velocity confirmation**: Check refrigerant velocities using temperature measurements
5. **Receiver level control**: Validate liquid return and level stability

Adjust refrigerant charge, control settings, and operating parameters to achieve design performance across the full load range.

## Common Design Errors

Avoid these frequent piping design mistakes:

- Undersizing wet return risers causing oil trapping at low load
- Excessive liquid line pressure drop causing flash gas formation
- Inadequate slope allowing liquid pockets and oil accumulation
- Single riser design on systems with wide load variation
- Improper support spacing leading to sagging and reverse slope
- Missing expansion provisions causing stress and joint failure
- Inadequate insulation thickness or vapor barrier installation

Proper piping design, installation, and commissioning ensure reliable liquid overfeed system operation with optimal efficiency and longevity.
