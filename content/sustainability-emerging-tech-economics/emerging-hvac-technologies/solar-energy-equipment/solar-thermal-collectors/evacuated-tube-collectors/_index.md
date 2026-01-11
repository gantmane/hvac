---
title: "Evacuated Tube Collectors"
description: "Technical analysis of evacuated tube solar thermal collectors including heat pipe and direct flow configurations, vacuum insulation physics, efficiency calculations, and cold climate performance characteristics"
keywords: ["evacuated tube collectors", "solar thermal", "heat pipe", "vacuum insulation", "cold climate solar", "selective coating", "stagnation temperature", "thermal efficiency"]
weight: 2
---

## Vacuum Insulation Physics

Evacuated tube collectors achieve superior thermal performance through vacuum insulation between concentric glass tubes. The vacuum pressure is maintained at 10⁻³ to 10⁻⁵ Pa, effectively eliminating conduction and convection losses. Heat transfer in the evacuated space occurs only through radiation, governed by the Stefan-Boltzmann law.

The radiative heat loss per unit area is:

$$q_{rad} = \sigma \epsilon (T_a^4 - T_{amb}^4)$$

Where:
- σ = 5.67 × 10⁻⁸ W/(m²·K⁴) (Stefan-Boltzmann constant)
- ε = absorber emissivity (0.04-0.06 for selective coatings)
- T_a = absorber temperature (K)
- T_amb = ambient temperature (K)

The selective absorber coating maintains high solar absorptance (α > 0.95) while exhibiting low thermal emittance (ε < 0.06), creating a favorable ratio α/ε > 15 that minimizes re-radiation losses.

## Heat Pipe Configuration

Heat pipe evacuated tubes utilize a sealed copper heat pipe containing a small volume of working fluid (water, methanol, or acetone depending on operating temperature range). The heat pipe operates on a closed thermodynamic cycle:

1. **Evaporation**: Solar radiation absorbed at the tube bottom vaporizes the working fluid
2. **Vapor Rise**: Pressure differential drives vapor to the condenser bulb
3. **Condensation**: Vapor releases latent heat to the heat transfer fluid in the manifold
4. **Return**: Condensate returns via gravity and capillary action

The heat pipe provides inherent thermal diode behavior—heat flows only upward. This prevents reverse thermosiphoning during periods without solar gain. The minimum installation angle is typically 20-25° from horizontal to ensure condensate return.

```
Heat Pipe Evacuated Tube (Longitudinal Section)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

                    ╔════════╗  ← Condenser bulb (dry connection)
                    ║ MANIFOLD
                    ╚════════╝
                        ║
    ┌─────────────────║─────────────────┐
    │  Outer glass    ║   Heat pipe     │
    │  ┌──────────────║──────────────┐  │
    │  │ Vacuum gap   ║              │  │
    │  │  ┌───────────║───────────┐  │  │
    │  │  │ Inner     ║ Selective │  │  │
    │  │  │ glass     ║  coating  │  │  │
    │  │  │           ║           │  │  │
    │  │  │    Evaporator section │  │  │
    │  │  │    (liquid pool)      │  │  │
    │  │  └───────────────────────┘  │  │
    │  └───────────────────────────────┘  │
    └─────────────────────────────────────┘

         Vapor ↑          ↓ Condensate
```

## Direct Flow Configuration

Direct flow (U-tube or coaxial) evacuated tubes circulate the heat transfer fluid directly through the absorber tube. The fluid enters at the bottom, flows along the absorber surface, and returns to the manifold.

**U-Tube Design**: Twin-tube configuration where fluid descends through one tube and ascends through the other. The tubes are thermally bonded to a fin within the vacuum envelope.

**Coaxial Design**: Fluid flows down the center tube and returns through the annular space between inner and outer flow tubes, maximizing heat exchange area.

Direct flow tubes offer several advantages:
- No minimum tilt angle requirement (can operate horizontally)
- Higher flow rates possible for large systems
- No working fluid freezing concerns
- Wet connection allows individual tube replacement without draining system

```
Direct Flow U-Tube (Cross Section)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    ┌─────────────────────────────┐
    │   Outer glass tube          │
    │  ┌─────────────────────┐    │
    │  │  Vacuum gap         │    │
    │  │ ┌───────────────┐   │    │
    │  │ │ Inner glass   │   │    │
    │  │ │  ┌─────────┐  │   │    │
    │  │ │  │  Metal   │  │   │    │
    │  │ │  │   fin    │  │   │    │
    │  │ │  │  ╔═╗ ╔═╗│  │   │    │
    │  │ │  │  ║ ║ ║ ║│  │   │    │  ← U-tubes
    │  │ │  │  ╚═╝ ╚═╝│  │   │    │
    │  │ │  │Selective│  │   │    │
    │  │ │  │ coating │  │   │    │
    │  │ │  └─────────┘  │   │    │
    │  │ └───────────────┘   │    │
    │  └─────────────────────┘    │
    └─────────────────────────────┘
```

## Thermal Efficiency Analysis

The instantaneous collector efficiency follows the ASHRAE 93-2010 standard test method:

$$\eta = \eta_0 - a_1 \frac{(T_m - T_{amb})}{G_T} - a_2 \frac{(T_m - T_{amb})^2}{G_T}$$

Where:
- η₀ = optical efficiency (typically 0.60-0.75 for evacuated tubes)
- a₁ = first-order heat loss coefficient (W/m²·K), typically 0.6-1.2
- a₂ = second-order coefficient (W/m²·K²), typically 0.003-0.008
- T_m = mean fluid temperature (°C)
- T_amb = ambient temperature (°C)
- G_T = total solar irradiance on collector plane (W/m²)

The reduced temperature difference is defined as:

$$T^* = \frac{T_m - T_{amb}}{G_T}$$

Evacuated tubes maintain efficiency η > 0.40 even at T* = 0.15 K·m²/W, conditions where flat plate collectors drop below η = 0.20.

## Cold Climate Performance

Evacuated tube collectors excel in cold climates due to three physical mechanisms:

**Minimal Convective Losses**: The vacuum eliminates air-mediated heat transfer. At -20°C ambient temperature, a flat plate collector with U_L = 4.5 W/m²·K experiences convective losses of 180 W/m² at 60°C operating temperature. An evacuated tube with effective U_L = 0.8 W/m²·K loses only 32 W/m² under identical conditions.

**Diffuse Radiation Collection**: The cylindrical tube geometry intercepts radiation from multiple angles without requiring tracking. The effective aperture area varies with sun angle, but collection continues under overcast skies when diffuse radiation dominates. Morning and afternoon collection efficiency remains high even at oblique sun angles.

**Snow Shedding**: Individual tubes accumulate minimal snow due to small top surface area. The tube curvature and residual heat from the absorber prevent snow bonding. Arrays maintain partial output even during snowfall events that completely cover flat plate collectors.

## Stagnation Characteristics

Stagnation temperature (no flow condition under peak solar radiation) reaches 200-250°C for heat pipe tubes and 280-320°C for direct flow configurations. Heat pipe tubes self-limit at lower temperatures because the vapor pressure ceiling prevents further evaporation. Direct flow tubes require overpressure protection and high-temperature glycol formulations rated to 150°C continuous service.

Per ASHRAE 90.1-2019 requirements for solar thermal systems, collectors operating above 180°C must incorporate pressure relief rated for the stagnation temperature, and piping materials must maintain structural integrity at maximum no-flow conditions.

## Selection Criteria

**Heat Pipe Applications**:
- Residential and light commercial (<50 tubes)
- Drain-back or pressurized glycol systems
- Moderate temperature applications (40-90°C)
- Tilt angle >20° available
- Individual tube serviceability priority

**Direct Flow Applications**:
- Large arrays (>50 tubes)
- High flow rate requirements
- Horizontal or low-angle installations
- Process heating (90-150°C)
- Minimizing pressure drop across array

Both configurations deliver annual efficiencies 15-30% higher than flat plate collectors in climates with mean January temperatures below 0°C and significant heating season diffuse radiation fractions above 40%.
