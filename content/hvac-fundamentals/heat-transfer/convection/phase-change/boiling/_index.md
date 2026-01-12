---
title: "Boiling"
weight: 1
---

Boiling is phase-change heat transfer where liquid converts to vapor at a heated surface. This process provides extremely high heat transfer coefficients and is fundamental to refrigeration cycles, evaporators, and thermal management systems.

## Pool Boiling Fundamentals

Pool boiling occurs when a heated surface is submerged in a quiescent liquid pool. The heat transfer characteristics depend strongly on the degree of superheat (ΔT = T_surface - T_sat).

### Pool Boiling Curve

The pool boiling curve relates heat flux to surface superheat and exhibits distinct regimes:

**Free Convection Regime (ΔT < 5°C):**
- Heat transfer by natural convection
- No bubble formation
- q" ∝ ΔT^(5/4) (typical)

**Nucleate Boiling Regime (5°C < ΔT < 30°C):**
- Vapor bubbles form at nucleation sites
- Extremely high heat transfer coefficients
- h = 2,500 to 100,000 W/(m²·K)
- Optimal regime for most HVAC applications

**Transition Boiling Regime (30°C < ΔT < 120°C):**
- Unstable region
- Alternating nucleate and film boiling
- Decreasing heat flux with increasing ΔT

**Film Boiling Regime (ΔT > 120°C):**
- Continuous vapor film blankets surface
- Poor heat transfer
- Surface temperatures can reach dangerous levels

## Nucleate Boiling

Nucleate boiling provides the highest heat transfer coefficients in pool boiling.

### Rohsenow Correlation

The Rohsenow correlation predicts nucleate boiling heat transfer:

**q"/μ_l h_fg = [c_p,l (T_s - T_sat) / (C_sf h_fg Pr_l^n)]^3**

Where:
- q" = heat flux (W/m²)
- μ_l = liquid dynamic viscosity (Pa·s)
- h_fg = latent heat of vaporization (J/kg)
- c_p,l = liquid specific heat (J/(kg·K))
- T_s = surface temperature (K)
- T_sat = saturation temperature (K)
- C_sf = surface-fluid combination constant
- Pr_l = liquid Prandtl number
- n = exponent (typically 1.0 for water, 1.7 for other fluids)

**Typical C_sf Values:**

| Surface-Fluid Combination | C_sf |
|---------------------------|------|
| Water-Copper (scored) | 0.0068 |
| Water-Copper (polished) | 0.0130 |
| Water-Stainless Steel | 0.0130 |
| R-134a-Copper | 0.0030 |
| R-22-Copper | 0.0050 |
| Ammonia-Stainless Steel | 0.0040 |

Surface roughness significantly affects nucleation site density and boiling performance. Rougher surfaces generally provide better nucleate boiling heat transfer.

### Bubble Dynamics

Bubble formation follows a sequence:
1. **Nucleation** - Vapor embryo forms at cavity
2. **Growth** - Bubble expands as liquid evaporates
3. **Departure** - Bubble detaches when buoyancy exceeds surface tension
4. **Condensation** - Bubble may condense in subcooled liquid

Bubble departure diameter (Fritz correlation):

**D_b = 0.0208 β [σ / (g(ρ_l - ρ_v))]^(1/2)**

Where:
- D_b = bubble departure diameter (m)
- β = contact angle (degrees)
- σ = surface tension (N/m)
- g = gravitational acceleration (9.81 m/s²)
- ρ_l, ρ_v = liquid and vapor densities (kg/m³)

## Critical Heat Flux (CHF)

CHF represents the maximum heat flux achievable in nucleate boiling before transition to film boiling. Exceeding CHF causes rapid surface temperature increase and potential equipment damage.

### Zuber Correlation (Pool Boiling)

For pool boiling on large horizontal surfaces:

**q"_CHF = 0.149 h_fg ρ_v [σ g (ρ_l - ρ_v) / ρ_v²]^(1/4)**

Typical CHF values:
- Water at 1 atm: 1.0 to 1.3 MW/m²
- R-134a at 5°C: 200 to 300 kW/m²
- Ammonia at -10°C: 400 to 600 kW/m²

**CHF Design Considerations:**
- Operate at 50-70% of CHF for safety margin
- Higher pressures increase CHF
- Surface orientation affects CHF (horizontal surfaces optimal)
- Subcooling increases CHF

## Flow Boiling

Flow boiling occurs inside tubes and channels where forced convection augments boiling heat transfer.

### Flow Boiling Regimes

As vapor quality increases along evaporator length:

**Subcooled Boiling (x < 0):**
- Liquid temperature below saturation
- Bubbles form at wall, condense in bulk liquid
- High heat transfer coefficients

**Saturated Nucleate Boiling (0 < x < 0.1):**
- Bulk liquid at saturation
- Bubbles form and grow at wall
- Heat transfer dominated by nucleate boiling

**Convective Boiling (0.1 < x < 0.8):**
- Annular flow regime
- Thin liquid film on wall with vapor core
- Heat transfer by convection through liquid film

**Dry-Out Region (x > 0.8):**
- Liquid film breaks down
- Wall contacts vapor
- Sharp decrease in heat transfer coefficient
- Must be avoided in evaporator design

### Flow Boiling Heat Transfer

The Chen correlation combines nucleate and convective contributions:

**h = h_nucleate · S + h_convective · F**

Where:
- S = suppression factor (0 to 1)
- F = Reynolds number enhancement factor

For convective component:

**h_convective = 0.023 (k_l/D) Re_l^0.8 Pr_l^0.4**

Where Re_l is based on liquid-only flow.

## Evaporator Design Applications

### Superheat Requirements

Superheat (vapor temperature above saturation) ensures complete evaporation and prevents liquid carryover to compressor.

**Typical Superheat Values:**

| Application | Superheat (K) |
|-------------|---------------|
| DX air conditioning coils | 5-8 |
| Refrigeration evaporators | 4-7 |
| Flooded shell evaporators | 0-2 |
| Thermostatic expansion valve control | 4-6 |
| Electronic expansion valve control | 2-4 |

### Heat Flux Design Guidelines

**Maximum Design Heat Flux:**

| Evaporator Type | q" (kW/m²) | % of CHF |
|-----------------|-----------|----------|
| Flooded shell-and-tube | 15-25 | 50-60% |
| DX shell-and-tube | 8-15 | 40-50% |
| DX finned coils | 5-12 | 30-40% |
| Plate heat exchangers | 10-20 | 40-50% |
| Microchannel evaporators | 8-18 | 35-45% |

### Design Considerations

**Mass Flux Effects:**
- Low mass flux (G < 100 kg/(m²·s)): Nucleate boiling dominant
- Medium mass flux (100 < G < 500 kg/(m²·s)): Mixed regime
- High mass flux (G > 500 kg/(m²·s)): Convective boiling dominant

**Pressure Drop Concerns:**
- Two-phase pressure drop reduces evaporating temperature
- ΔT_sat = (dT/dP)·ΔP_friction
- Limits evaporator length and refrigerant velocity
- Use larger diameter tubes for low pressure drop

**Oil Return:**
- Minimum vapor velocity required to entrain oil
- V_min ≈ 3-5 m/s for horizontal lines
- V_min ≈ 5-8 m/s for vertical risers
- Critical at low load conditions

## Film Boiling and Leidenfrost Point

Film boiling occurs when surface superheat exceeds CHF condition, forming a stable vapor blanket.

**Leidenfrost Temperature:**
- Minimum surface temperature for stable film boiling
- Typically 200-300°C above saturation for water
- Minimum in pool boiling curve
- Must be avoided in refrigeration equipment

**Film Boiling Heat Transfer:**

**h_film = 0.62 [k_v³ ρ_v (ρ_l - ρ_v) g h'_fg / (μ_v D (T_s - T_sat))]^(1/4)**

Where:
- h'_fg = modified latent heat = h_fg + 0.4 c_p,v (T_s - T_sat)
- k_v, μ_v, ρ_v = vapor properties
- D = characteristic length

Film boiling provides poor heat transfer (h ≈ 100-400 W/(m²·K)) compared to nucleate boiling.

## Practical HVAC Applications

**Refrigeration Evaporators:**
- Operate in nucleate to convective boiling regimes
- Design for complete evaporation plus superheat
- Monitor for dry-out at partial loads

**Chiller Evaporators:**
- Flooded shell design maintains nucleate boiling
- Refrigerant recirculation rates of 2-4× evaporation rate
- High heat transfer coefficients (3,000-8,000 W/(m²·K))

**Heat Pump Evaporators:**
- Outdoor coils experience frost formation
- Defrost cycles critical for maintaining performance
- Refrigerant distribution affects coil utilization

**DX Expansion Devices:**
- Control superheat to optimize evaporator utilization
- Balance between full coil usage and compressor protection
- Electronic valves provide superior control

## Performance Factors

**Enhancement Techniques:**
- Micro-fin tubes increase nucleation sites
- Enhanced surfaces improve h by 100-300%
- Surface treatments modify wettability
- Nanofluid refrigerants under research

**Degradation Factors:**
- Fouling reduces heat transfer
- Oil accumulation blankets surfaces
- Non-condensable gases reduce performance
- Inadequate refrigerant charge
