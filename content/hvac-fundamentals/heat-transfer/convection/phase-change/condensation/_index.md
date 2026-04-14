---
title: "Condensation"
aliases: ["Condensation"]
weight: 2
---

Condensation occurs when vapor contacts a surface below its saturation temperature, releasing latent heat during the phase change from vapor to liquid. This phenomenon drives heat transfer in condensers, dehumidification coils, and numerous HVAC applications.

## Condensation Mechanisms

Two distinct modes characterize condensation heat transfer, differing by orders of magnitude in effectiveness.

### Film Condensation

Film condensation forms a continuous liquid layer on the condensing surface. The condensate film provides thermal resistance between the vapor and the wall, controlling the overall heat transfer rate.

The film thickness increases along the surface as more vapor condenses, progressively reducing the local heat transfer coefficient. Gravity drives the condensate flow, with the film Reynolds number determining whether the flow remains laminar or transitions to turbulent.

**Film Reynolds number:**

$$Re_f = \frac{4\Gamma}{\mu_l}$$

where Γ is the mass flow rate per unit width (kg/s·m) and μ_l is the liquid dynamic viscosity.

Laminar film condensation occurs for Re_f < 30, transitional behavior exists between 30 < Re_f < 1800, and turbulent film condensation develops for Re_f > 1800.

### Dropwise Condensation

Dropwise condensation forms discrete liquid droplets on the surface rather than a continuous film. Droplets nucleate at surface imperfections, grow through direct condensation, and coalesce with adjacent droplets. When droplets reach sufficient size, gravity removes them from the surface.

Heat transfer coefficients in dropwise condensation exceed film condensation by factors of 5 to 10 because the surface remains largely exposed to vapor, with minimal thermal resistance from liquid. The highest heat transfer occurs in regions between droplets where fresh surface continuously becomes available.

Sustaining dropwise condensation requires:
- Surface contamination or coatings (promoter substances)
- Low surface energy materials (hydrophobic surfaces)
- Absence of non-condensable gases
- Continuous droplet removal

Most industrial surfaces revert to film condensation due to surface aging, contamination, or oxide formation. Design calculations conservatively assume film condensation unless proven dropwise operation can be maintained.

## Nusselt Analysis for Film Condensation

Nusselt's classical analysis provides the theoretical foundation for laminar film condensation heat transfer. The analysis assumes:

- Laminar flow in the condensate film
- Negligible vapor shear stress
- Constant property values
- Negligible acceleration and convection terms
- Linear temperature profile through the film

### Vertical Surface Condensation

For laminar film condensation on a vertical surface of height L:

$$h_{avg} = 0.943 \left[\frac{g\rho_l(\rho_l - \rho_v)h_{fg}k_l^3}{\mu_l(T_{sat} - T_w)L}\right]^{1/4}$$

where:
- g = gravitational acceleration (9.81 m/s²)
- ρ_l = liquid density (kg/m³)
- ρ_v = vapor density (kg/m³)
- h_fg = latent heat of vaporization (J/kg)
- k_l = liquid thermal conductivity (W/m·K)
- μ_l = liquid dynamic viscosity (Pa·s)
- T_sat = saturation temperature (°C)
- T_w = wall temperature (°C)
- L = vertical height (m)

The average heat transfer coefficient varies as L^(-1/4), indicating that taller surfaces have lower average coefficients due to film thickening.

**Local heat transfer coefficient:**

$$h_x = 0.707 \left[\frac{g\rho_l(\rho_l - \rho_v)h_{fg}k_l^3}{\mu_l(T_{sat} - T_w)x}\right]^{1/4}$$

where x is the distance from the top of the surface.

### Horizontal Tube Condensation

For laminar film condensation on a horizontal tube of diameter D:

$$h_{avg} = 0.728 \left[\frac{g\rho_l(\rho_l - \rho_v)h_{fg}k_l^3}{\mu_l(T_{sat} - T_w)D}\right]^{1/4}$$

This coefficient applies to single horizontal tubes. For tube banks, condensate from upper tubes drips onto lower tubes, increasing film thickness and reducing heat transfer.

### Tube Bank Condensation

For N horizontal tubes arranged vertically in a bank:

$$h_{avg,N} = \frac{h_{avg,1}}{N^{1/4}}$$

where h_avg,1 is the single tube coefficient. The heat transfer coefficient for the bottom tube is approximately 0.59 times the top tube value for N = 10.

## Modified Latent Heat

The Nusselt analysis uses a modified latent heat that accounts for sensible cooling of the condensate film:

$$h'_{fg} = h_{fg} + 0.68c_{p,l}(T_{sat} - T_w)$$

where c_p,l is the liquid specific heat. This correction typically increases the effective latent heat by 1-5% depending on temperature difference.

## Forced Convection Condensation

When vapor flows with significant velocity, shear forces at the vapor-liquid interface enhance heat transfer beyond gravity-driven predictions.

### Condensation Inside Tubes

Internal condensation occurs in refrigerant condensers and steam condensers. The flow regime depends on vapor velocity and quality:

**Annular flow regime:** Liquid film on tube wall, vapor core in center
**Stratified flow regime:** Liquid accumulates at bottom, vapor flows over top
**Slug/plug flow regime:** Intermittent liquid plugs separate vapor regions
**Mist flow regime:** Liquid droplets entrained in vapor

For annular flow in horizontal tubes, empirical correlations account for both gravity and shear effects:

$$h = h_{film}\left(1 + \frac{h_{shear}}{h_{film}}\right)$$

The Shah correlation provides widely used predictions for in-tube condensation across flow regimes and refrigerants.

## HVAC Applications

### Refrigerant Condensers

Air-cooled condensers:
- Film condensation on tube exterior
- Forced convection inside tubes
- Condensate drainage from fins
- Typical heat transfer coefficients: 300-800 W/m²·K (tube-side)

Water-cooled condensers:
- Shell-and-tube configuration most common
- Film condensation on tube exterior (shell-side)
- Typical overall U-values: 800-1500 W/m²·K

### Dehumidification Coils

Cooling coils operating below the air dew point experience simultaneous sensible and latent heat transfer. Moisture condenses on fin and tube surfaces when the surface temperature drops below the air dew point.

**Condensation requirements:**
- Surface temperature < air dew point temperature
- Adequate surface area for heat and mass transfer
- Proper condensate drainage

The total heat transfer includes:

$$q_{total} = q_{sensible} + q_{latent}$$

$$q_{total} = \dot{m}_{air}(h_{in} - h_{out})$$

where h represents air enthalpy (J/kg).

**Sensible heat ratio:**

$$SHR = \frac{q_{sensible}}{q_{total}} = \frac{c_p(T_{in} - T_{out})}{h_{in} - h_{out}}$$

Typical cooling coil surface temperatures range from 4-10°C (40-50°F) for comfort cooling applications, ensuring condensation when room dew points exceed these values.

## Condensate Drainage

Proper condensate removal prevents water accumulation, microbiological growth, and system performance degradation.

### Drainage System Design

**Drain pan requirements:**
- Minimum slope: 1% (1/8 inch per foot)
- Depth sufficient to contain condensate during peak loads
- Corrosion-resistant materials (stainless steel, polymers)
- Access for cleaning

**Trap sizing:**
- Static pressure drop across coil determines trap depth
- Minimum trap seal depth = 1.5 × static pressure (inches H₂O)
- Prevents air bypass through drain line

**Drain line sizing:**

$$D = 0.00659\sqrt{Q}$$

where D is the drain pipe diameter (inches) and Q is the condensate flow rate (lb/hr).

Minimum drain line size: 3/4 inch (20 mm) regardless of calculation.

### Condensate Pumps

Required when gravity drainage is unavailable:
- Reservoir capacity: 2-5 minutes of peak condensate production
- Redundant pumps for critical applications
- High-level safety shutoff prevents overflow
- Check valves prevent backflow

## Non-Condensable Gases

Non-condensable gases (air, nitrogen) dramatically reduce condensation heat transfer by accumulating at the vapor-liquid interface, creating additional thermal resistance.

Even small concentrations (1-3% by volume) can reduce heat transfer coefficients by 50% or more. Steam condensers incorporate venting systems to continuously remove non-condensables and maintain performance.

## Performance Factors

Parameters affecting condensation heat transfer:

**Surface conditions:**
- Roughness (promotes or hinders dropwise condensation)
- Cleanliness (fouling reduces performance)
- Material properties (thermal conductivity, surface energy)

**Operating conditions:**
- Temperature difference (T_sat - T_w)
- Vapor velocity and quality
- Non-condensable gas concentration

**Geometric factors:**
- Surface orientation (vertical, horizontal, inclined)
- Tube diameter and arrangement
- Enhanced surfaces (fins, grooves, microstructures)

Fouling factors account for performance degradation:
- Water-side fouling: 0.00009 m²·K/W (0.0005 ft²·h·°F/Btu)
- Refrigerant-side fouling: 0.00018 m²·K/W (0.001 ft²·h·°F/Btu)

## Enhanced Condensation Surfaces

Modern condensers employ surface modifications to improve heat transfer:

**External enhancements:**
- Low-fin tubes (increased surface area)
- Three-dimensional pin fins
- Hydrophobic coatings (promote dropwise condensation)

**Internal enhancements:**
- Microfin tubes (spiral grooves increase turbulence)
- Twisted tape inserts
- Surface tension devices (improve drainage)

Enhanced tubes provide 1.5 to 4 times the heat transfer coefficient of smooth tubes, enabling reduced size and refrigerant charge.
