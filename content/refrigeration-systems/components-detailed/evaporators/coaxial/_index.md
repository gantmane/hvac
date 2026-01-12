---
title: "Coaxial Evaporators"
weight: 4
description: "Tube-in-tube coaxial evaporators for refrigeration systems: construction, heat transfer characteristics, design parameters, and application considerations"
---

Coaxial evaporators employ a tube-in-tube (concentric tube) configuration where refrigerant and secondary fluid flow in separate passages with counterflow arrangement. This design provides compact heat exchange with high efficiency for liquid cooling applications, particularly in water chillers, heat pumps, and process cooling systems.

## Construction and Geometry

### Tube-in-Tube Configuration

The fundamental geometry consists of:

**Inner Tube:** Contains one fluid (typically refrigerant during evaporation)
- Standard copper tube: 3/8", 1/2", 5/8" OD
- Smooth or internally enhanced surface
- Wall thickness per ASTM B88 Type L or K

**Outer Tube:** Contains the counterflowing fluid (typically water or glycol solution)
- Larger diameter copper tube: 5/8", 7/8", 1-1/8" OD
- Creates annular passage for secondary fluid flow
- Maintains structural integrity and pressure containment

**Annular Space Dimensions:**
- Hydraulic diameter of annulus: D_h = D_outer - D_inner
- Typical annular gap: 1/8" to 3/8" radial clearance
- Flow area affects velocity and heat transfer coefficient

### Enhanced Surface Technologies

**Internal Rifling (Inner Tube):**
- Helical grooves with spiral angles 18-30°
- Groove depth: 0.008" to 0.015"
- Increases internal surface area by 30-60%
- Enhances refrigerant-side boiling coefficient

**Microfin Tubes:**
- Fine helical fins with heights 0.008" to 0.012"
- Fin density: 60-80 fins per circumference
- Provides 80-100% surface area increase
- Improves nucleate boiling and convective heat transfer

**Corrugated Inner Surface:**
- Cross-corrugated or herringbone patterns
- Creates turbulence and disrupts boundary layer
- Effective for single-phase and two-phase flow

### Assembly Methods

**Brazed Construction:**
- Permanent joint using copper-phosphorus or silver alloy
- High thermal conductivity at joint
- Operating pressures to 600 psig
- Temperature limit: 250°F continuous

**Mechanical Swaging:**
- Expansion of inner tube into outer tube
- Creates intimate contact for heat transfer
- Allows field repair and tube replacement
- Requires precise dimensional control

**Triple-Wall Designs:**
- Intermediate barrier tube for double containment
- Leak detection passage between primary barriers
- Required for ammonia/water systems per codes
- Safety consideration for toxic refrigerants

## Heat Transfer Analysis

### Overall Heat Transfer Coefficient

The thermal resistance network for coaxial geometry:

| Resistance Component | Expression | Typical Value |
|---------------------|------------|---------------|
| Refrigerant convection | 1/(h_i × A_i) | h_i = 800-2500 Btu/hr-ft²-°F |
| Inner tube conduction | ln(r_o/r_i)/(2πkL) | Negligible for copper |
| Annulus convection | 1/(h_o × A_o) | h_o = 300-1200 Btu/hr-ft²-°F |
| Fouling (if applicable) | R_f/A | R_f = 0.0005-0.001 hr-ft²-°F/Btu |

**Overall Coefficient:**
U = 1 / [1/(h_i × A_i/A_o) + t_wall/(k_copper × A_log/A_o) + 1/h_o + R_f]

Typical overall U-values: 200-500 Btu/hr-ft²-°F for water cooling applications

### Refrigerant-Side Heat Transfer

**Nucleate Boiling Regime:**
- Dominant at low vapor qualities (x < 0.3)
- Heat flux dependent: q" = C × ΔT_sat^n
- Enhanced by surface roughness and nucleation sites
- Correlations: Cooper, Gorenflo for pool boiling modified for flow

**Convective Boiling Regime:**
- Increases importance at higher qualities (x > 0.4)
- Flow pattern transitions: bubbly → slug → annular
- Two-phase multiplier approach: h_tp = h_lo × F(x, properties)
- Velocity effects become dominant

**Enhancement Factor:**
- Rifled tubes: 1.5-2.5× smooth tube performance
- Microfin tubes: 1.8-3.0× smooth tube performance
- Quality dependent: maximum enhancement at x = 0.3-0.6
- Pressure drop penalty: 1.3-1.8× smooth tube

### Annulus-Side Heat Transfer

**Turbulent Flow (Re > 4000):**
- Dittus-Boelter correlation: Nu = 0.023 Re^0.8 Pr^0.4
- Hydraulic diameter: D_h = 4A_flow/P_wetted = D_outer - D_inner
- Fully developed flow assumption after L/D_h > 10

**Laminar Flow (Re < 2300):**
- Nusselt number depends on thermal boundary conditions
- Constant heat flux: Nu = 4.36 (fully developed)
- Constant wall temperature: Nu = 3.66 (fully developed)
- Entrance effects significant for short coils

**Velocity Optimization:**
- Higher velocity → higher h_o → better heat transfer
- Pressure drop increases as ΔP ∝ V^2
- Economic velocity range: 3-8 ft/s for water
- Erosion concerns above 10 ft/s for copper

## Counterflow Performance Advantages

### Temperature Profiles

**Effectiveness:**
ε = Q_actual / Q_max = (T_out - T_in)_water / (T_evap - T_in)_water

Counterflow provides:
- Maximum temperature differential maintained throughout length
- Higher LMTD compared to parallel flow: LMTD_counter > LMTD_parallel
- Enables closer approach temperatures
- Better thermodynamic efficiency

**Log Mean Temperature Difference:**
LMTD = (ΔT_1 - ΔT_2) / ln(ΔT_1/ΔT_2)

Where:
- ΔT_1 = T_evap - T_water,out (refrigerant inlet end)
- ΔT_2 = T_evap - T_water,in (refrigerant outlet end)

### Approach Temperature

**Typical Values:**
- Water chillers: 3-5°F approach
- Glycol systems: 5-8°F approach
- Direct expansion: 2-4°F approach
- Flooded evaporators: 1-3°F approach

Approach temperature impacts:
- Evaporator size and cost
- System efficiency (lower approach → higher suction pressure → higher COP)
- Control stability
- Part-load performance

## Pressure Drop Considerations

### Refrigerant-Side Pressure Drop

**Components:**
1. **Acceleration:** ΔP_accel due to density change during evaporation
2. **Friction:** ΔP_friction from wall shear stress
3. **Gravitational:** ΔP_grav (orientation dependent)

**Two-Phase Multiplier Method:**
ΔP_tp = ΔP_lo × Φ²_lo

Where:
- ΔP_lo = pressure drop if total mass flowed as liquid
- Φ²_lo = two-phase multiplier (function of quality, fluid properties)
- Lockhart-Martinelli parameter X_tt characterizes flow regime

**Typical Values:**
- Smooth tubes: 2-5 psi total evaporator drop
- Enhanced tubes: 3-8 psi total evaporator drop
- Design limit: < 2°F saturation temperature change

### Water-Side Pressure Drop

**Annular Passage:**
ΔP = (f × L/D_h × ρV²/2) / 144

Friction factor correlations:
- Turbulent: f = 0.079/Re^0.25 (smooth pipe approximation)
- Design range: 5-15 ft water per circuit
- Pump power impact must be considered in efficiency analysis

## Design Specifications

### Performance Parameters

| Parameter | Typical Range | Design Considerations |
|-----------|--------------|----------------------|
| Capacity per circuit | 1-10 tons | Modular assembly for larger loads |
| Tube length | 10-50 ft | Balances pressure drop vs. size |
| Refrigerant velocity | 300-1500 fpm | Quality dependent, exit velocity |
| Water velocity | 2-8 ft/s | Balance heat transfer and ΔP |
| Heat flux | 3,000-12,000 Btu/hr-ft² | Based on inner tube surface area |
| Mass flux (refrigerant) | 50,000-200,000 lb/hr-ft² | Affects flow regime and h_i |
| Refrigerant charge | 0.5-2.0 lb/ton | Low charge characteristic |
| Approach temperature | 2-8°F | Application specific |

### Dimensional Standards

| Inner Tube OD | Outer Tube OD | Annular Gap | Typical Capacity |
|---------------|---------------|-------------|------------------|
| 3/8" | 5/8" | 1/8" | 1-2 tons |
| 1/2" | 7/8" | 3/16" | 2-4 tons |
| 5/8" | 1-1/8" | 1/4" | 4-7 tons |
| 3/4" | 1-3/8" | 5/16" | 7-10 tons |

## Application Domains

### Water Chillers

**Residential and Light Commercial:**
- Heat pump water heaters (integrated or remote)
- Capacity range: 1-5 tons
- Compact footprint advantage
- Low refrigerant charge (environmental benefit)
- Brazed construction typical

**Direct Expansion Systems:**
- Precise superheat control essential
- Thermostatic expansion valve or electronic expansion valve
- Exit superheat: 5-10°F typical
- Liquid return risk mitigation

### Heat Pump Applications

**Water-Source Heat Pumps:**
- Evaporator mode during heating season
- Reversing operation requires oil return considerations
- Ground loop connections
- Antifreeze solutions (glycol) common

**Desuperheater Integration:**
- Upstream water heating before main condenser
- Triple-wall design may be required
- Pressure relief coordination
- Thermal expansion provisions

### Process Cooling

**Advantages:**
- Direct refrigerant-to-process fluid heat exchange
- Eliminates intermediate heat exchanger
- Faster temperature response
- Precise temperature control capability

**Limitations:**
- Single process fluid circuit per refrigerant circuit
- Pressure drop limits on long piping runs
- Flow balancing in multiple parallel circuits
- Not suitable for very high flow rates

### Industrial Refrigeration

**Liquid Overfeed Systems:**
- Coaxial evaporator as liquid cooling element
- Recirculation ratio: 2:1 to 4:1
- Separator vessel after evaporator
- Lower refrigerant-side pressure drop
- More stable operation

**Cascade Systems:**
- Interstage heat exchanger between high and low stage
- Counterflow maximizes efficiency
- Typically larger industrial sizes
- Ammonia low stage / CO₂ or HFC high stage common

## Installation Requirements

### Orientation Considerations

**Horizontal Installation (Preferred):**
- Counterflow: water enters at refrigerant outlet end
- Proper refrigerant distribution throughout length
- Oil return to compressor maintained
- Simplifies piping and support

**Vertical Installation:**
- Upward refrigerant flow recommended (downward water flow)
- Gravity assists oil entrainment and return
- Higher pressure drop on refrigerant side
- May require higher mass flux to ensure annular flow

**Pitch Requirements:**
- Minimum 1/4" per 10 ft toward compressor
- Facilitates oil return during operation
- Prevents liquid trapping during shutdown
- Vapor line pitch critical for reliability

### Piping Connections

**Refrigerant Side:**
- Distributor at inlet for uniform liquid feeding (DX mode)
- Sight glass before evaporator to verify subcooled liquid
- Superheat sensor at outlet (bulb location and insulation)
- Suction accumulator consideration for systems with variable load

**Water Side:**
- Isolation valves for service access
- Pressure relief valve if isolation valves installed
- Flow switch or sensor for freeze protection
- Air vent at high point, drain at low point
- Strainer before evaporator to prevent fouling

### Thermal Expansion and Support

**Linear Expansion:**
α = 9.5 × 10⁻⁶ in/in-°F for copper

For 20 ft coil with 60°F temperature swing:
ΔL = 20 ft × 12 in/ft × 9.5×10⁻⁶ × 60°F = 0.137 inch

**Support Spacing:**
- Horizontal runs: support every 6-10 ft
- Avoid rigid clamping that constrains expansion
- Allow axial movement at one end
- Insulation support separate from tube support

**Vibration Isolation:**
- Flexible connections at compressor discharge and suction
- Avoid resonant frequencies with compressor operation
- Secure mounting to prevent fatigue failure
- Consider water hammer effects in liquid lines

## Performance Monitoring

### Key Indicators

**Operating Temperatures:**
- Entering water temperature (EWT)
- Leaving water temperature (LWT)
- Refrigerant saturation temperature (via pressure measurement)
- Superheat at evaporator outlet
- Subcooling at evaporator inlet (for DX systems)

**Temperature Metrics:**
- Approach: T_evap - T_water,out (expect 3-5°F for water)
- ΔT across evaporator: T_in - T_out water side (capacity indication)
- Superheat: T_suction - T_evap (control parameter, 5-10°F target)

**Pressure Measurements:**
- Evaporator inlet pressure (saturated liquid in flooded/overfeed)
- Evaporator outlet pressure (suction pressure)
- Pressure drop across evaporator (diagnostic for fouling/restrictions)
- Water-side pressure drop (pump performance and fouling indicator)

### Degradation Mechanisms

**Fouling:**
- Water-side scaling from hardness (calcium carbonate)
- Biological fouling in open loop systems
- Reduced U-value and capacity
- Increased pressure drop on affected side
- Maintenance: chemical cleaning or mechanical brushing (requires disassembly for coaxial)

**Refrigerant-Side Issues:**
- Oil accumulation (reduces heat transfer surface)
- Non-condensables (raise pressure, reduce capacity)
- Moisture contamination (ice formation at expansion device)
- Proper system design prevents: oil return velocity, filter-driers, evacuation

**Mechanical Degradation:**
- Erosion at high velocity points (>10 ft/s water)
- Corrosion from water chemistry (pH, chlorides, dissolved oxygen)
- Stress corrosion cracking at brazed joints
- Fatigue from thermal cycling and vibration

## Advantages and Limitations

### Advantages

**Compact Footprint:**
- High heat transfer per unit volume
- Minimal space requirements
- Suitable for tight installations
- Lower material costs for small capacities

**Low Refrigerant Charge:**
- Environmental benefit (reduced GWP impact)
- Safety consideration for flammable refrigerants (A2L, A3 classifications)
- Regulatory compliance advantages
- Lower refrigerant cost

**High Efficiency:**
- Counterflow provides maximum thermodynamic effectiveness
- Enhanced surfaces boost performance further
- Close approach temperatures achievable
- Good part-load performance

**Direct Heat Exchange:**
- No intermediate fluid loops required
- Faster response to load changes
- Simpler system architecture
- Reduced auxiliary energy consumption

### Limitations

**Capacity Constraints:**
- Practical limit ~10 tons per circuit
- Multiple parallel circuits required for larger loads
- Flow distribution challenges with parallel circuits
- Individual circuit control complexity

**Maintenance Access:**
- Brazed construction prevents internal cleaning
- Must replace entire coaxial assembly if fouled
- No access for tube-side inspection
- External water treatment critical

**Pressure Drop:**
- Annular passage limits water flow rate
- Long lengths increase pressure drop
- Pump energy consideration
- May require larger sizes to reduce ΔP

**Application Constraints:**
- Not suitable for very high water flow rates
- Limited to clean water/glycol solutions
- Single-pass design limits temperature change per circuit
- Freeze risk in low-temperature applications requires glycol

## Selection Methodology

### Design Process

1. **Establish Requirements:**
   - Cooling capacity (tons or Btu/hr)
   - Water flow rate and temperature range
   - Refrigerant type and operating conditions
   - Pressure drop limits (water and refrigerant)
   - Space constraints

2. **Initial Sizing:**
   - Calculate heat duty: Q = m_water × cp × ΔT
   - Estimate overall U-value: 250-400 Btu/hr-ft²-°F typical starting point
   - Determine required surface area: A = Q / (U × LMTD)
   - Select tube diameters based on flow rates

3. **Detailed Analysis:**
   - Calculate refrigerant-side heat transfer coefficient (h_i)
   - Calculate water-side heat transfer coefficient (h_o)
   - Compute overall U-value
   - Iterate on length and diameter if needed

4. **Pressure Drop Verification:**
   - Check refrigerant-side pressure drop (< 2°F saturation change)
   - Check water-side pressure drop (< 15 ft head typical)
   - Adjust velocities if needed

5. **Performance Validation:**
   - Verify approach temperature meets application needs
   - Check exit superheat for DX systems
   - Confirm capacity at off-design conditions
   - Ensure oil return velocity maintained

### Selection Criteria

| Factor | Coaxial Preferred | Other Type Preferred |
|--------|------------------|---------------------|
| Capacity | < 10 tons per circuit | > 20 tons total |
| Space | Very limited | Ample |
| Refrigerant charge | Minimize (safety, cost) | Not critical |
| Water quality | Excellent (low fouling) | Poor (needs cleaning access) |
| Application | Residential, light commercial | Industrial, large commercial |
| Control | Precise temperature control | Broad temperature range |
| Maintenance | Replacement acceptable | Regular cleaning required |

## Future Developments

**Enhanced Surfaces:**
- Advanced microstructures for higher boiling coefficients
- Porous metallic coatings for nucleation control
- Gradient structures optimized along tube length
- Additive manufacturing for complex internal geometries

**Alternative Materials:**
- Stainless steel for corrosive applications
- Titanium for seawater and aggressive chemicals
- Polymer-lined copper for water quality protection
- Aluminum for weight reduction and specific refrigerants

**Design Optimization:**
- Variable diameter along length to maintain optimal velocities
- Hybrid smooth/enhanced sections tuned to quality profile
- Integrated circuiting for multiple zones
- CFD-optimized entrance regions

**Low-GWP Refrigerants:**
- Adaptation to A2L refrigerants (R-32, R-454B, R-1234yf)
- Pressure rating increases for high-pressure refrigerants
- Material compatibility with HFO blends
- Natural refrigerants (R-290 propane, R-744 CO₂) considerations
