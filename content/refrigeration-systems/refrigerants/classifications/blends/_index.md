---
title: "Blends"
weight: 6
---

Refrigerant blends consist of mixtures of two or more pure refrigerants formulated to achieve specific thermophysical properties, environmental characteristics, or system performance objectives. These mixtures exhibit unique phase-change behavior that distinguishes them from pure compounds and directly impacts system design, operation, and service procedures.

## Blend Classification Systems

### ASHRAE 400/500-Series Nomenclature

Refrigerant blends receive numeric designations based on composition:

| Series | Composition Type | Example | Components |
|--------|-----------------|---------|------------|
| 400-series | Zeotropic blends | R-407C | HFC-32/125/134a (23/25/52 mass%) |
| 500-series | Azeotropic blends | R-507A | HFC-125/143a (50/50 mass%) |

### Letter Suffixes for Blend Variants

Different compositions of the same component refrigerants receive sequential letter designations:

- R-404A: HFC-125/143a/134a (44/52/4%)
- R-404B: Different composition, same components (alternative formulation)

## Zeotropic Blends

### Phase-Change Characteristics

Zeotropic mixtures exhibit temperature glide during constant-pressure phase transitions. The dew point and bubble point temperatures differ, creating a temperature range over which evaporation or condensation occurs.

**Temperature Glide Definition:**

Glide = T_dewpoint - T_bubblepoint

### Physical Mechanisms

During phase change at constant pressure:

1. **Initial Evaporation** - Liquid composition at bubble point differs from vapor composition at dew point
2. **Progressive Composition Shift** - More volatile components preferentially evaporate first
3. **Final Evaporation** - Remaining liquid becomes enriched in less volatile components

This behavior arises from differences in vapor pressure among blend components at any given temperature.

### Temperature Glide Magnitude

Glide values vary significantly among zeotropic blends:

| Refrigerant | Components | Mass % | Glide (°F) | Glide (K) |
|-------------|-----------|---------|------------|-----------|
| R-407C | HFC-32/125/134a | 23/25/52 | 11.3 | 6.3 |
| R-407A | HFC-32/125/134a | 20/40/40 | 12.6 | 7.0 |
| R-407F | HFC-32/125/134a | 30/30/40 | 10.8 | 6.0 |
| R-410A | HFC-32/125 | 50/50 | 0.3 | 0.17 |
| R-422D | HFC-125/134a/HC-600a | 65.1/31.5/3.4 | 7.9 | 4.4 |
| R-438A | HFC-32/125/134a/290/600a | 8.5/45/44.2/1.6/0.7 | 10.4 | 5.8 |

R-410A exhibits near-azeotropic behavior despite being classified as zeotropic due to minimal glide.

### System Design Implications

**Heat Exchanger Performance:**

Temperature glide affects heat transfer in evaporators and condensers:

- **Counterflow Advantage** - Glide enables closer temperature approach in counterflow heat exchangers
- **LMTD Calculation** - Logarithmic mean temperature difference calculations must account for non-isothermal phase change
- **Capacity Impact** - Effective heat transfer coefficient varies through phase-change region

**Charging Procedures:**

Zeotropic blends require liquid charging to maintain design composition:

- **Vapor Charging Prohibited** - Preferential vaporization alters blend composition in cylinder and system
- **Liquid Phase Required** - Charge as liquid through suction service port with system off or through liquid line

### Fractionation Phenomena

Fractionation occurs when blend composition differs between liquid and vapor phases or between system locations.

**Leakage-Induced Fractionation:**

When zeotropic blends leak from a system:

1. **Vapor-Phase Leak** - More volatile components escape preferentially
2. **Composition Drift** - Remaining charge becomes enriched in less volatile components
3. **Performance Degradation** - System capacity, efficiency, and pressure relationships change
4. **Topping-Off Prohibited** - Adding refrigerant to partially leaked system creates non-homogeneous mixture

**Recovery-Induced Fractionation:**

During refrigerant recovery:

- **Initial Recovery** - Vapor phase removed first contains higher proportion of volatile components
- **Progressive Shift** - Recovery cylinder composition differs from original system charge
- **Complete Recovery Required** - Partial recovery leaves non-representative composition

**Circulating Charge Distribution:**

In operating systems:

- **Evaporator Outlet** - Vapor enriched in volatile components
- **Liquid Line** - Composition matches design specification
- **Accumulator Risk** - Trapped liquid may have altered composition after repeated cycles

### Common Zeotropic Blends

| Refrigerant | Application | Components | Composition (mass %) |
|-------------|-------------|-----------|---------------------|
| R-407C | Medium-temp air conditioning | HFC-32/125/134a | 23/25/52 |
| R-407F | Low-temp refrigeration | HFC-32/125/134a | 30/30/40 |
| R-422D | R-22 retrofit | HFC-125/134a/HC-600a | 65.1/31.5/3.4 |
| R-427A | R-22 retrofit | HFC-32/125/143a/134a | 15/25/10/50 |
| R-438A | R-22 retrofit, low GWP | HFC-32/125/134a/290/600a | 8.5/45/44.2/1.6/0.7 |
| R-448A | HFC/HFO blend, low GWP | HFC-32/125/134a, HFO-1234yf/1234ze | 26/26/21/20/7 |
| R-449A | HFC/HFO blend, R-404A replacement | HFC-32/125/134a, HFO-1234yf | 24.3/24.7/25.3/25.7 |
| R-513A | HFC/HFO blend, R-134a replacement | HFC-134a/HFO-1234yf | 56/44 |

## Azeotropic Blends

### Phase-Change Behavior

Azeotropic mixtures behave as single-component refrigerants during phase transitions. The liquid and vapor phases have identical composition at the azeotropic point, resulting in:

- **Zero Temperature Glide** - Single saturation temperature at given pressure
- **Constant Composition** - No preferential vaporization of components
- **No Fractionation** - Leakage does not alter remaining charge composition

### Thermodynamic Basis

Azeotropy occurs when the mixture's total vapor pressure exhibits an extremum (maximum or minimum) at a specific composition. For refrigerant applications, minimum-boiling azeotropes are typical.

At the azeotropic composition:

(∂P/∂x)_T = 0

where P is total pressure, x is liquid mole fraction, and T is temperature.

### Advantages for Service

Azeotropic blends simplify system service:

- **Vapor Charging Acceptable** - Composition remains constant regardless of phase
- **Partial Leak Tolerance** - Remaining charge maintains original composition
- **Topping-Off Permitted** - Additional refrigerant can be added without composition concerns
- **Simplified Recovery** - Recovery method does not affect composition

### Common Azeotropic Blends

| Refrigerant | Components | Composition (mass %) | Application | Notes |
|-------------|-----------|---------------------|-------------|-------|
| R-500 | CFC-12/HFC-152a | 73.8/26.2 | Low-temp refrigeration | Obsolete, high ODP |
| R-502 | CFC-115/HCFC-22 | 48.8/51.2 | Low-temp refrigeration | Obsolete, high ODP |
| R-507A | HFC-125/143a | 50/50 | Commercial refrigeration | R-502 replacement |
| R-508B | HCFC-23/HFC-116 | 46/54 | Ultra-low temperature | Cascade systems |

## Near-Azeotropic Blends

Some zeotropic blends exhibit temperature glide less than 0.5 K, functionally behaving as azeotropes:

- **R-410A** - Glide of 0.17 K allows vapor charging and simplified service
- **R-508A** - Glide of 0.02 K, used in ultra-low temperature applications

These blends combine the formulation flexibility of zeotropes with the service simplicity of azeotropes.

## Composition Tolerance and Quality Control

ASHRAE Standard 34 specifies composition tolerances for refrigerant blends:

**Typical Tolerance Ranges:**

- Major components (>20%): ±1.0 to ±2.0 mass%
- Minor components (5-20%): ±0.5 to ±1.0 mass%
- Trace components (<5%): ±0.2 to ±0.5 mass%

Manufacturing precision ensures consistent:

- Thermodynamic properties
- System performance
- Safety characteristics (flammability, toxicity)
- Environmental metrics (GWP, ODP)

## Blend Property Prediction

Mixture properties are calculated using:

**Ideal Solution Assumptions:**

For low-pressure vapor: P_total = Σ(y_i × P_i)

where y_i is mole fraction and P_i is partial pressure of component i.

**Non-Ideal Behavior Corrections:**

Real mixtures require equation-of-state models:

- Peng-Robinson equation
- REFPROP database (NIST)
- Activity coefficient models (UNIFAC, Wilson)

These account for molecular interactions affecting:

- Vapor pressure
- Enthalpy of vaporization
- Density
- Specific heat

## Environmental and Safety Considerations

### Global Warming Potential

Blend GWP is mass-weighted average:

GWP_blend = Σ(w_i × GWP_i)

where w_i is mass fraction of component i.

### Flammability Classification

Blend flammability depends on composition and worst-case fractionation:

- **Worst Case of Formulation (WCFF)** - Tests most flammable possible composition within tolerance
- **Worst Case of Fractionation (WCF)** - Tests composition after leak scenarios
- **ASHRAE 34 Classification** - A1, A2L, A2, A3, B1, B2L, B2, B3 based on toxicity and flammability

Many low-GWP blends containing HFO-1234yf or HFO-1234ze(E) are classified A2L (mildly flammable).

## Service and Handling Requirements

### Leak Response

**Zeotropic Blends:**

1. **System Evacuation** - Remove entire charge
2. **Leak Repair** - Fix leak source
3. **System Recharge** - Install fresh refrigerant of correct composition
4. **No Topping-Off** - Never add refrigerant to partially leaked system

**Azeotropic Blends:**

1. **Leak Repair** - Fix leak source
2. **Recharge to Specification** - Add refrigerant as needed
3. **Vapor or Liquid** - Either phase acceptable for charging

### Storage and Cylinder Management

All blends require:

- **Dedicated Cylinders** - Never mix refrigerants
- **Liquid Withdrawal** - Dip tube or cylinder inversion for zeotropes
- **Proper Identification** - ASHRAE number and composition on label
- **Temperature Control** - Store within manufacturer specifications

### Retrofitting Considerations

When replacing existing refrigerants with blends:

1. **Oil Compatibility** - Verify lubricant compatibility with all blend components
2. **Material Compatibility** - Check elastomers, seals, and gaskets
3. **Capacity Matching** - Account for different volumetric capacity
4. **Pressure Relationships** - Verify component pressure ratings
5. **Control Adjustment** - Recalibrate or replace pressure controls
6. **Filter-Drier Replacement** - Install desiccant compatible with new refrigerant
7. **System Flushing** - Remove residual oil and contaminants if required

Proper blend selection and system modification ensure reliable long-term operation while meeting environmental objectives.
