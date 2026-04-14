---
title: "Thermophysical Properties Refrigerants"
aliases: ["Thermophysical Properties Refrigerants"]
description: "Comprehensive thermophysical and transport properties of refrigerants including saturation data, P-h diagrams, T-s diagrams, equations of state, and property tables for refrigeration cycle analysis and system design."
weight: 1
---

Refrigerant thermophysical properties form the engineering foundation for refrigeration cycle analysis, equipment sizing, and system performance prediction. Accurate property data spanning saturation, superheated, and subcooled regions enables rigorous calculations for compressor work, heat exchanger capacity, expansion device sizing, and coefficient of performance.

## Property Categories

Refrigerant properties fall into distinct categories serving different analytical purposes:

**Thermodynamic properties:** Pressure, temperature, specific volume, enthalpy, entropy, internal energy defining the thermodynamic state. Required for cycle analysis using the first and second laws of thermodynamics.

**Transport properties:** Viscosity, thermal conductivity, diffusivity governing momentum, energy, and mass transfer. Essential for heat exchanger design, pressure drop calculations, and convective heat transfer coefficient prediction.

**Phase equilibrium properties:** Vapor pressure, liquid-vapor density, critical point data describing phase boundaries and two-phase behavior. Fundamental for evaporator and condenser design.

**Surface properties:** Surface tension affecting nucleate boiling, droplet formation, and refrigerant-oil interactions in systems.

## Refrigeration Cycle Analysis Requirements

The vapor-compression refrigeration cycle comprises four fundamental processes requiring specific property data:

**Compression (1→2):** Superheated vapor compression from evaporator pressure to condenser pressure. Requires superheat enthalpy at suction conditions and discharge conditions for work calculation:

W_comp = ṁ(h₂ - h₁)

Property needs: h(P,T) in superheated region, isentropic path for ideal compression h₂s = h(s₁, P₂).

**Condensation (2→3):** Desuperheating, condensation, and subcooling from superheated discharge to subcooled liquid. Heat rejection:

Q_cond = ṁ(h₂ - h₃)

Property needs: Superheat properties, saturation properties at condenser pressure, subcooled liquid enthalpy.

**Expansion (3→4):** Isenthalpic throttling through expansion valve or capillary tube:

h₄ = h₃

Property needs: Quality x = (h₄ - hf₄)/(hg₄ - hf₄) at evaporator pressure to determine two-phase state.

**Evaporation (4→1):** Two-phase evaporation from expanded liquid-vapor mixture to superheated suction vapor. Refrigeration capacity:

Q_evap = ṁ(h₁ - h₄)

Property needs: Saturation properties at evaporator pressure, superheat enthalpy at suction conditions.

**Coefficient of Performance:**

COP = Q_evap / W_comp = (h₁ - h₄) / (h₂ - h₁)

## Saturation Properties

Saturation conditions define the phase boundary between liquid and vapor states. At saturation, liquid and vapor coexist in equilibrium at specific temperature-pressure combinations governed by the Clausius-Clapeyron relation:

dP/dT = hfg / (T · vfg)

**Saturation pressure:** Vapor pressure corresponding to saturation temperature. This P-T relationship is fundamental to refrigerant selection and system operating conditions.

**Liquid properties:** Saturated liquid density (ρf), enthalpy (hf), entropy (sf), specific volume (vf) at the bubble point.

**Vapor properties:** Saturated vapor density (ρg), enthalpy (hg), entropy (sg), specific volume (vg) at the dew point.

**Enthalpy of vaporization:** hfg = hg - hf represents the latent heat required for phase change. High hfg indicates large refrigeration effect per unit mass.

**Specific volume ratio:** vg/vf ranges from 100-1000 depending on pressure, affecting compressor displacement requirements.

Saturation tables present properties as functions of either temperature or pressure, with one implying the other through the vapor pressure curve.

## Superheated Properties

Superheated vapor exists above saturation temperature at given pressure or below saturation pressure at given temperature. Compressor suction and discharge gases occupy the superheated region.

Superheat tables organize properties in a temperature-pressure grid:
- Rows: Temperature (T)
- Columns: Pressure (P)
- Cells: v, h, s, cp, cv, ρ at (T,P) state point

Degrees of superheat: ∆Tsup = T - Tsat(P)

Typical compressor suction superheat: 10-20°F (5-11°C) ensuring vapor-only compression preventing liquid slugging.

Typical compressor discharge superheat: 40-100°F (20-55°C) depending on compression ratio and refrigerant properties.

Superheated properties follow ideal gas behavior at low density (high superheat, low pressure) but require complex equations of state near saturation.

## Subcooled Liquid Properties

Subcooled liquid exists below saturation temperature at given pressure or above saturation pressure at given temperature. Condenser outlet liquid and receiver contents occupy the subcooled region.

Degrees of subcooling: ∆Tsub = Tsat(P) - T

Typical condenser subcooling: 5-15°F (3-8°C) ensuring liquid-only supply to expansion device.

Liquid properties exhibit weak pressure dependence (incompressible approximation often valid). Temperature primarily determines density, enthalpy, and entropy in subcooled region.

## Pressure-Enthalpy Diagrams

The P-h diagram represents the universal tool for refrigeration cycle visualization and analysis. Logarithmic pressure scale (vertical) versus linear enthalpy scale (horizontal) reveals cycle processes as lines on the diagram.

**Saturation dome:** Bell-shaped curve separating subcooled liquid (left), two-phase region (inside dome), and superheated vapor (right). Critical point tops the dome.

**Constant temperature lines (isotherms):**
- Horizontal in two-phase region (T = Tsat at fixed P)
- Steeply sloped in subcooled liquid region (vertical for incompressible liquid)
- Gradually sloped in superheated region, asymptotically approaching ideal gas behavior

**Constant entropy lines (isentropes):**
- Steep in superheated region
- Represent isentropic compression path (ideal compressor)
- Cross isotherms from lower-left to upper-right

**Constant quality lines:** Radiate from critical point through two-phase dome marking percentages of vapor by mass (x = 0, 0.1, 0.2, ... 0.9, 1.0).

**Constant volume lines:** Steeply sloped, nearly vertical in liquid region, horizontal at very low density approaching ideal gas limit.

## Temperature-Entropy Diagrams

The T-s diagram provides alternative thermodynamic cycle representation emphasizing second-law analysis:

**Carnot cycle:** Rectangle on T-s diagram representing theoretical maximum efficiency.

**Actual cycle:** Resembles trapezoid with rounded corners, revealing irreversibilities through entropy generation.

**Area under curve:** Represents heat transfer (Q = ∫T ds). Enclosed area represents net work.

**Compression process:** Curves upward-right. Vertical line represents isentropic (ideal) compression. Actual compression slopes right showing entropy generation.

**Heat rejection/addition:** Primarily horizontal in two-phase regions (constant T at saturation), sloped in superheat/subcool regions.

## Equations of State

Accurate property calculation requires sophisticated equations of state (EOS) relating P, v, T, and derived properties:

**Fundamental equations:** Helmholtz energy formulation a(ρ,T) enables calculating all thermodynamic properties through partial derivatives. NIST REFPROP database employs fundamental equations achieving accuracy ±0.1% in density, ±0.5% in derived properties.

**Cubic equations:** Peng-Robinson and Redlich-Kwong-Soave provide adequate vapor properties with simpler mathematics. Suitable for preliminary design but less accurate than fundamental equations.

**Martin-Hou equation:** Historical multi-parameter equation balancing accuracy and computational complexity. Superseded by modern fundamental equations.

**Benedict-Webb-Rubin (BWR):** Complex multi-parameter equation with good accuracy. Modified BWR (MBWR) versions extend range and precision.

Modern refrigerant property software (REFPROP, CoolProp) implements fundamental equations providing high-accuracy properties across the full operating range.

## Transport Properties

Transport properties enable heat exchanger and pressure drop calculations:

**Viscosity (μ):** Resistance to flow. Dynamic viscosity appears in Reynolds number Re = ρVD/μ determining flow regime. Kinematic viscosity ν = μ/ρ appears in momentum diffusion.

Liquid viscosity: 100-500 μPa·s depending on refrigerant and temperature
Vapor viscosity: 10-20 μPa·s, increasing with temperature

**Thermal conductivity (k):** Heat conduction capability. Appears in Fourier's law q" = -k∇T and convective correlations through Nusselt number Nu = hD/k.

Liquid k: 60-120 mW/(m·K)
Vapor k: 10-20 mW/(m·K)

**Prandtl number:** Pr = μcp/k represents ratio of momentum to thermal diffusivity. Affects convective heat transfer:

Liquid Pr: 3-6 (similar to water)
Vapor Pr: 0.7-0.9 (similar to air)

Transport properties exhibit strong temperature dependence and moderate pressure dependence requiring temperature-specific values in calculations.

## Refrigerant Mixtures

Zeotropic blends (non-azeotropic mixtures) exhibit temperature glide during phase change, complicating property determination:

**Bubble point:** Temperature where first vapor forms at given pressure and composition.

**Dew point:** Temperature where last vapor condenses at given pressure and composition.

**Temperature glide:** ∆Tglide = Tdew - Tbubble ranges from 1°F for near-azeotropes (R410A) to 10°F for high-glide blends (R407C).

**Composition shift:** Preferential evaporation of more volatile components shifts composition between liquid and vapor phases. Leak charging requires liquid phase to maintain composition.

Property tables for blends require specifying liquid or vapor composition. Dew point and bubble point tables replace single saturation tables of pure fluids.

## Critical Point and Limits

The critical point represents the highest temperature and pressure where distinct liquid and vapor phases exist:

**Critical temperature Tc:** Above Tc, fluid cannot be liquefied regardless of pressure. Sets upper limit for condensing temperature.

**Critical pressure Pc:** Pressure at Tc. Above Pc, no phase distinction exists.

**Transcritical cycles:** CO₂ (R744) systems with Tc = 31°C operate transcritically in many climates. Gas cooler replaces condenser, requiring different property evaluation.

**Reduced properties:** Tr = T/Tc and Pr = P/Pc enable corresponding states correlations estimating properties of new refrigerants from similar compounds.

## Modern Refrigerant Property Sources

Authoritative property data sources include:

**NIST REFPROP:** Reference Fluid Properties database from National Institute of Standards and Technology. Implements fundamental Helmholtz equations of state for 100+ refrigerants. Industry standard for accuracy.

**ASHRAE Fundamentals:** Chapter 30 provides saturation and superheat tables for common refrigerants. Sufficient for manual calculations.

**CoolProp:** Open-source property library implementing REFPROP-compatible equations. Freely available for software integration.

**Manufacturer data:** Equipment manufacturers provide refrigerant property data for specific applications, often presented in P-h diagram form.

Accuracy requirements drive source selection. Preliminary design accepts simplified properties; detailed simulation and performance prediction require high-accuracy fundamental equations.
