---
title: "Saturation Properties"
description: "Comprehensive analysis of refrigerant saturation properties including temperature-pressure relationships, saturated liquid and vapor states, latent heat of vaporization, quality calculations, and property interpolation methods for HVAC system design and analysis."
weight: 5
---

Saturation properties define the thermodynamic state of a refrigerant existing simultaneously as liquid and vapor in equilibrium. Understanding these properties is fundamental to refrigeration cycle analysis, equipment sizing, and system performance evaluation.

## Saturation State Definition

The saturation state represents the boundary between single-phase liquid and single-phase vapor regions on a thermodynamic property diagram. At saturation conditions:

- Liquid and vapor phases coexist in equilibrium
- Temperature and pressure are interdependent (not independent variables)
- Any heat addition at constant pressure causes phase change without temperature increase
- Properties change dramatically between saturated liquid and saturated vapor states

The saturation condition is uniquely defined by specifying either temperature or pressure—once one is known, the other is fixed by the refrigerant's thermodynamic properties.

## Temperature-Pressure Relationship

The Clausius-Clapeyron equation describes the fundamental relationship between saturation temperature and pressure:

$$\frac{dP}{dT} = \frac{h_{fg}}{T \cdot v_{fg}}$$

Where:
- dP/dT = slope of saturation curve
- h_fg = enthalpy of vaporization (latent heat)
- T = absolute temperature (K or R)
- v_fg = specific volume change during vaporization (v_g - v_f)

This relationship explains why saturation pressure increases exponentially with temperature. The practical implications include:

- Higher condensing temperatures require higher condensing pressures
- Lower evaporating temperatures correspond to lower suction pressures
- Pressure-temperature charts provide quick reference for system diagnosis

### Practical Saturation Relationships

For common refrigerants at typical HVAC operating conditions:

| Refrigerant | Evaporator (40°F) | Condenser (100°F) | Pressure Ratio |
|-------------|-------------------|-------------------|----------------|
| R-410A | 118 psig | 370 psig | 3.14 |
| R-134a | 37 psig | 124 psig | 3.35 |
| R-32 | 96 psig | 300 psig | 3.13 |
| R-290 (Propane) | 78 psig | 230 psig | 2.95 |
| R-744 (CO₂) | 470 psig | 1070 psig | 2.28 |

The pressure ratio (P_cond/P_evap) affects compressor power consumption and system efficiency. Lower ratios generally indicate better system performance.

## Saturated Liquid Properties

Saturated liquid (designated with subscript "f") represents the state immediately before vaporization begins. Key properties include:

**Specific Volume (v_f)**
- Typically very small (0.01-0.02 ft³/lbm for most refrigerants)
- Relatively insensitive to temperature compared to vapor
- Used for liquid line sizing and subcooling calculations

**Enthalpy (h_f)**
- Reference point often set at -40°F or 0°F (varies by refrigerant)
- Increases with temperature
- Represents energy content of liquid entering evaporator

**Entropy (s_f)**
- Used in theoretical cycle analysis
- Determines ideal compression process endpoint
- Lower values at lower temperatures

**Density (ρ_f)**
- Reciprocal of specific volume
- Important for liquid line pressure drop calculations
- Decreases as temperature increases

### Subcooled Liquid Region

When liquid exists below its saturation temperature at a given pressure, it is subcooled. The degree of subcooling is:

$$\Delta T_{sub} = T_{sat} - T_{actual}$$

Subcooling ensures liquid reaches the metering device without flash gas formation, maintaining system capacity and efficiency.

## Saturated Vapor Properties

Saturated vapor (subscript "g") exists at the completion of evaporation, immediately before superheating. Critical properties include:

**Specific Volume (v_g)**
- Much larger than liquid (100-500 times v_f)
- Strongly temperature-dependent
- Determines compressor displacement requirements
- Affects suction line sizing

**Enthalpy (h_g)**
- Sum of liquid enthalpy and latent heat (h_g = h_f + h_fg)
- Represents total energy of saturated vapor
- Starting point for compression process

**Entropy (s_g)**
- Higher than saturated liquid entropy
- Used to establish isentropic compression path
- Temperature-dependent

**Density (ρ_g)**
- Low compared to liquid phase
- Affects compressor volumetric efficiency
- Critical for suction line velocity calculations

### Target Saturated Vapor Conditions

| Application | Typical Evaporator | Saturated Vapor Temp | Purpose |
|-------------|-------------------|---------------------|---------|
| Air Conditioning | 40-45°F | 40-45°F | Comfort cooling |
| Medium Temp Refrigeration | 20-30°F | 20-30°F | Food storage |
| Low Temp Refrigeration | -20 to 0°F | -20 to 0°F | Frozen foods |
| Ice Making | -10 to 10°F | -10 to 10°F | Ice production |

## Latent Heat of Vaporization

The enthalpy of vaporization (h_fg or h_latent) represents the energy required to convert saturated liquid to saturated vapor at constant temperature and pressure:

$$h_{fg} = h_g - h_f$$

Latent heat characteristics:

- Decreases as temperature increases
- Becomes zero at the critical point
- Represents the refrigeration effect in the evaporator
- Larger values indicate higher cooling capacity per unit mass

### Latent Heat Values

Typical latent heat values for common refrigerants at 40°F evaporating temperature:

| Refrigerant | h_fg (Btu/lbm) | h_f (Btu/lbm) | h_g (Btu/lbm) |
|-------------|----------------|---------------|---------------|
| R-410A | 91.7 | 40.6 | 132.3 |
| R-134a | 93.2 | 24.6 | 117.8 |
| R-32 | 141.5 | 50.2 | 191.7 |
| R-404A | 83.5 | 32.1 | 115.6 |
| R-407C | 89.3 | 37.8 | 127.1 |

Higher latent heat values translate to lower refrigerant mass flow rates for the same cooling capacity, potentially reducing compressor displacement requirements.

## Quality and Two-Phase Properties

Quality (x) quantifies the vapor fraction in a two-phase mixture:

$$x = \frac{m_{vapor}}{m_{total}} = \frac{m_g}{m_g + m_f}$$

Quality ranges from 0 (saturated liquid) to 1 (saturated vapor). For any property in the two-phase region:

$$Property_{mixture} = Property_f + x \cdot (Property_g - Property_f)$$

Or equivalently:

$$Property_{mixture} = (1-x) \cdot Property_f + x \cdot Property_g$$

### Quality Applications

**Enthalpy Calculation:**

$$h = h_f + x \cdot h_{fg}$$

This relationship is critical for:
- Determining refrigeration effect
- Analyzing evaporator performance
- Calculating compressor suction conditions with liquid entrainment

**Specific Volume Calculation:**

$$v = v_f + x \cdot (v_g - v_f)$$

Used to:
- Determine two-phase flow characteristics
- Calculate pressure drop in evaporator circuits
- Analyze flash gas formation at metering device

**Example Quality Calculation:**

Given: R-410A at 40°F, h = 90 Btu/lbm

From saturation tables: h_f = 40.6 Btu/lbm, h_fg = 91.7 Btu/lbm

$$x = \frac{h - h_f}{h_{fg}} = \frac{90 - 40.6}{91.7} = 0.539$$

The mixture is 53.9% vapor, 46.1% liquid by mass.

## Property Interpolation Methods

Saturation tables provide discrete data points. Interpolation determines properties between tabulated values.

### Linear Interpolation

For properties between two tabulated points:

$$Property = Property_1 + \frac{(T - T_1)}{(T_2 - T_1)} \cdot (Property_2 - Property_1)$$

Where:
- T = desired temperature (between T_1 and T_2)
- Property_1, Property_2 = tabulated values

Accuracy: ±1-2% for small temperature intervals (5-10°F)

### Logarithmic Interpolation for Pressure

Since pressure-temperature relationship is exponential, logarithmic interpolation improves accuracy:

$$\ln(P) = \ln(P_1) + \frac{(T - T_1)}{(T_2 - T_1)} \cdot [\ln(P_2) - \ln(P_1)]$$

Then: P = e^[ln(P)]

Accuracy: ±0.5% across wider temperature ranges

### Double Interpolation

When interpolating properties at off-table pressure and temperature:

1. Interpolate at constant pressure for two temperatures bracketing the desired value
2. Interpolate between these results at the desired temperature
3. Alternatively, use enthalpy-pressure or entropy-temperature coordinates

## Saturation Property Tables

### R-410A Saturation Properties (Temperature Basis)

| Temp (°F) | Pressure (psia) | v_f (ft³/lbm) | v_g (ft³/lbm) | h_f (Btu/lbm) | h_fg (Btu/lbm) | h_g (Btu/lbm) | s_f (Btu/lbm·R) | s_g (Btu/lbm·R) |
|-----------|----------------|---------------|---------------|---------------|----------------|---------------|-----------------|-----------------|
| -40 | 40.7 | 0.0112 | 1.365 | 12.5 | 102.8 | 115.3 | 0.0325 | 0.2445 |
| -20 | 60.5 | 0.0115 | 0.970 | 21.8 | 99.3 | 121.1 | 0.0538 | 0.2410 |
| 0 | 87.5 | 0.0119 | 0.699 | 31.2 | 95.6 | 126.8 | 0.0742 | 0.2381 |
| 20 | 122.9 | 0.0123 | 0.517 | 40.9 | 91.6 | 132.5 | 0.0937 | 0.2357 |
| 40 | 168.6 | 0.0127 | 0.390 | 50.8 | 87.3 | 138.1 | 0.1126 | 0.2336 |
| 60 | 226.8 | 0.0132 | 0.299 | 61.0 | 82.6 | 143.6 | 0.1309 | 0.2318 |
| 80 | 299.6 | 0.0137 | 0.232 | 71.6 | 77.4 | 149.0 | 0.1488 | 0.2302 |
| 100 | 389.3 | 0.0143 | 0.182 | 82.7 | 71.7 | 154.4 | 0.1664 | 0.2286 |
| 120 | 498.5 | 0.0150 | 0.144 | 94.3 | 65.2 | 159.5 | 0.1839 | 0.2270 |

### R-134a Saturation Properties (Temperature Basis)

| Temp (°F) | Pressure (psia) | v_f (ft³/lbm) | v_g (ft³/lbm) | h_f (Btu/lbm) | h_fg (Btu/lbm) | h_g (Btu/lbm) | s_f (Btu/lbm·R) | s_g (Btu/lbm·R) |
|-----------|----------------|---------------|---------------|---------------|----------------|---------------|-----------------|-----------------|
| -40 | 7.5 | 0.0111 | 6.220 | 0.0 | 102.3 | 102.3 | 0.0000 | 0.2338 |
| -20 | 12.6 | 0.0114 | 3.870 | 5.7 | 100.0 | 105.7 | 0.0135 | 0.2313 |
| 0 | 20.3 | 0.0117 | 2.530 | 11.5 | 97.6 | 109.1 | 0.0267 | 0.2293 |
| 20 | 31.1 | 0.0120 | 1.710 | 17.4 | 95.0 | 112.4 | 0.0395 | 0.2277 |
| 40 | 46.7 | 0.0123 | 1.190 | 23.4 | 92.3 | 115.7 | 0.0521 | 0.2265 |
| 60 | 68.0 | 0.0127 | 0.847 | 29.6 | 89.4 | 119.0 | 0.0644 | 0.2255 |
| 80 | 96.4 | 0.0131 | 0.615 | 35.9 | 86.3 | 122.2 | 0.0765 | 0.2248 |
| 100 | 133.4 | 0.0135 | 0.455 | 42.4 | 83.0 | 125.4 | 0.0884 | 0.2242 |
| 120 | 180.5 | 0.0140 | 0.341 | 49.0 | 79.4 | 128.4 | 0.1001 | 0.2236 |

### R-32 Saturation Properties (Temperature Basis)

| Temp (°F) | Pressure (psia) | v_f (ft³/lbm) | v_g (ft³/lbm) | h_f (Btu/lbm) | h_fg (Btu/lbm) | h_g (Btu/lbm) | s_f (Btu/lbm·R) | s_g (Btu/lbm·R) |
|-----------|----------------|---------------|---------------|---------------|----------------|---------------|-----------------|-----------------|
| -40 | 30.2 | 0.0139 | 1.785 | 22.8 | 152.0 | 174.8 | 0.0545 | 0.4125 |
| -20 | 46.1 | 0.0143 | 1.240 | 33.5 | 148.2 | 181.7 | 0.0771 | 0.4085 |
| 0 | 68.1 | 0.0148 | 0.885 | 44.4 | 144.2 | 188.6 | 0.0989 | 0.4053 |
| 20 | 97.4 | 0.0153 | 0.645 | 55.5 | 139.9 | 195.4 | 0.1199 | 0.4026 |
| 40 | 136.0 | 0.0158 | 0.480 | 66.9 | 135.3 | 202.2 | 0.1403 | 0.4004 |
| 60 | 186.0 | 0.0164 | 0.363 | 78.6 | 130.4 | 209.0 | 0.1602 | 0.3985 |
| 80 | 249.6 | 0.0171 | 0.278 | 90.6 | 125.0 | 215.6 | 0.1797 | 0.3968 |
| 100 | 329.3 | 0.0179 | 0.216 | 103.1 | 119.1 | 222.2 | 0.1989 | 0.3952 |
| 120 | 428.0 | 0.0188 | 0.169 | 116.2 | 112.5 | 228.7 | 0.2180 | 0.3936 |

## Application Considerations

### System Design

Saturation properties directly affect:

- **Compressor Selection**: Suction density determines volumetric flow requirements
- **Heat Exchanger Sizing**: Latent heat and density affect required surface area
- **Refrigerant Charge**: Liquid density determines system charge quantity
- **Pressure Vessel Design**: Saturation pressure establishes minimum wall thickness

### Operating Diagnostics

Measured pressure-temperature relationships reveal:

- **Superheat Verification**: Compare measured temperature to saturation temperature at measured pressure
- **Subcooling Assessment**: Liquid line temperature versus saturation temperature
- **Non-Condensable Detection**: Actual pressure higher than saturation pressure indicates air contamination
- **Refrigerant Identification**: Pressure-temperature pairs identify refrigerant type

### Performance Analysis

Saturation data enables:

- **Theoretical Capacity**: Refrigeration effect equals h_fg at evaporator conditions
- **Compressor Work**: Calculated from enthalpy rise during compression
- **COP Determination**: Ratio of refrigeration effect to compression work
- **Approach Temperature**: Difference between secondary fluid and refrigerant saturation temperature

Understanding saturation properties provides the foundation for all refrigeration cycle analysis, system troubleshooting, and equipment selection decisions in HVAC applications.
