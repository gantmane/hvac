---
title: "Processes"
weight: 4
---

Thermodynamic processes describe the path a system follows as it changes from one equilibrium state to another. Understanding these processes is essential for analyzing HVAC equipment cycles, compression, expansion, heating, and cooling operations.

## Fundamental Process Types

### Isothermal Process (Constant Temperature)

**Definition:** Temperature remains constant throughout the process (T = constant, dT = 0).

**Governing Relations:**
- For ideal gas: PV = constant
- Temperature: T₁ = T₂
- Internal energy change: ΔU = 0 (for ideal gas)
- Heat equals work: Q = W

**Work Calculation:**
```
W = ∫PdV = mRT ln(V₂/V₁) = mRT ln(P₁/P₂)
W = P₁V₁ ln(V₂/V₁)
```

**Heat Transfer:**
```
Q = W = mRT ln(V₂/V₁)
```

**HVAC Applications:**
- Ideal vapor compression at constant condenser/evaporator temperatures
- Long-term heat exchanger processes with large thermal mass
- Ground-source heat pump ground loop approximation (seasonal average)
- Storage tank thermal processes with sufficient time constant

**Practical Considerations:**
- Requires perfect heat transfer or extremely slow process
- Real HVAC processes approximate isothermal behavior in large thermal mass systems
- Useful idealization for phase change processes (evaporation, condensation)

---

### Isobaric Process (Constant Pressure)

**Definition:** Pressure remains constant throughout the process (P = constant, dP = 0).

**Governing Relations:**
- For ideal gas: V/T = constant
- Volume ratio: V₂/V₁ = T₂/T₁
- Enthalpy change: ΔH = Q (at constant pressure)

**Work Calculation:**
```
W = P(V₂ - V₁) = PΔV = mR(T₂ - T₁)
```

**Heat Transfer:**
```
Q = mCₚ(T₂ - T₁) = ΔH
```

**First Law Application:**
```
ΔU = Q - W = mCᵥ(T₂ - T₁)
Q = ΔU + W = mCₚ(T₂ - T₁)
```

**HVAC Applications:**
- Heating coils (air heated at atmospheric pressure)
- Cooling coils (air cooled at constant pressure)
- Boiler water heating (liquid phase at constant system pressure)
- Open spray chambers and humidifiers
- Atmospheric air handling processes
- Combustion in open furnaces

**Practical Considerations:**
- Most air-side HVAC processes are approximately isobaric
- Pressure drop in ducts/coils creates slight deviation from ideal
- Enthalpy calculations directly applicable (psychrometric charts)

---

### Isochoric Process (Constant Volume)

**Definition:** Volume remains constant throughout the process (V = constant, dV = 0).

**Governing Relations:**
- For ideal gas: P/T = constant
- Pressure ratio: P₂/P₁ = T₂/T₁
- No boundary work: W = 0

**Work Calculation:**
```
W = ∫PdV = 0 (since dV = 0)
```

**Heat Transfer:**
```
Q = ΔU = mCᵥ(T₂ - T₁)
```

**First Law Application:**
```
Q = ΔU (since W = 0)
ΔU = mCᵥ(T₂ - T₁)
```

**HVAC Applications:**
- Refrigerant in rigid closed vessel during heating/cooling
- Receiver tank pressure/temperature relationships
- Closed vessel safety relief valve sizing calculations
- Autoclave and sterilizer initial heating phases
- Refrigerant cylinder storage temperature-pressure relationships

**Practical Considerations:**
- Common in analysis of closed storage vessels
- Pressure rises directly with temperature increase
- Critical for safety relief valve design
- Used in refrigerant property table relationships

---

### Isentropic Process (Constant Entropy)

**Definition:** Entropy remains constant throughout the process (s = constant, ds = 0). Represents an ideal reversible adiabatic process.

**Governing Relations:**
- For ideal gas: PVᵏ = constant, TVᵏ⁻¹ = constant, TPᵏ/(¹⁻ᵏ) = constant
- Specific heat ratio: k = Cₚ/Cᵥ
- No heat transfer: Q = 0
- Reversible: No entropy generation

**Pressure-Volume Relations:**
```
P₂/P₁ = (V₁/V₂)ᵏ
```

**Temperature Relations:**
```
T₂/T₁ = (V₁/V₂)ᵏ⁻¹ = (P₂/P₁)⁽ᵏ⁻¹⁾/ᵏ
```

**Work Calculation:**
```
W = ΔU = mCᵥ(T₂ - T₁) = [P₂V₂ - P₁V₁]/(1 - k)

For ideal gas:
W = [mR(T₁ - T₂)]/(k - 1) = [P₁V₁/(k-1)][1 - (P₂/P₁)⁽ᵏ⁻¹⁾/ᵏ]
```

**Isentropic Efficiency:**
```
Compression: ηc = Ws/Wa = (h₂s - h₁)/(h₂a - h₁)
Expansion: ηt = Wa/Ws = (h₁ - h₂a)/(h₁ - h₂s)
```
Where subscript 's' indicates isentropic and 'a' indicates actual process.

**HVAC Applications:**
- Ideal compressor compression process (baseline for efficiency)
- Ideal turbine/expander expansion process
- Nozzle flow (short residence time, minimal heat transfer)
- Benchmark for actual compression/expansion processes
- Centrifugal and screw compressor efficiency calculations
- Chiller compressor performance analysis

**Practical Considerations:**
- Real compressors: 70-85% isentropic efficiency (reciprocating, scroll)
- Real compressors: 75-85% isentropic efficiency (screw, centrifugal)
- Deviations due to friction, heat transfer, irreversibilities
- Used to calculate actual work from ideal work and efficiency

---

### Polytropic Process (General Process)

**Definition:** A general process following the relation PVⁿ = constant, where n is the polytropic exponent.

**Governing Relation:**
```
PVⁿ = constant
P₁V₁ⁿ = P₂V₂ⁿ
```

**Polytropic Exponent Values:**
- n = 0: Isobaric (constant pressure)
- n = 1: Isothermal (constant temperature)
- n = k: Isentropic (reversible adiabatic)
- n = ∞: Isochoric (constant volume)
- 1 < n < k: Real compression/expansion with heat transfer

**Temperature Relations:**
```
T₂/T₁ = (V₁/V₂)ⁿ⁻¹ = (P₂/P₁)⁽ⁿ⁻¹⁾/ⁿ
```

**Work Calculation:**
```
W = [P₂V₂ - P₁V₁]/(1 - n) = [mR(T₂ - T₁)]/(1 - n)

For n ≠ 1:
W = [P₁V₁/(n-1)][1 - (P₂/P₁)⁽ⁿ⁻¹⁾/ⁿ]
```

**Heat Transfer:**
```
Q = W + ΔU = W + mCᵥ(T₂ - T₁)
Q = mCₙ(T₂ - T₁)

Where Cₙ = Cᵥ[(k - n)/(1 - n)]
```

**HVAC Applications:**
- Real compressor processes (n = 1.2 to 1.3 for reciprocating with cooling)
- Actual expansion processes in turbines
- Compressor performance mapping
- Real gas compression with jacket cooling/heating
- Multi-stage compression analysis

**Determining Polytropic Exponent:**
```
n = ln(P₂/P₁)/ln(V₁/V₂) = log(P₂/P₁)/log(V₁/V₂)
```

**Practical Considerations:**
- More accurate model for real compression than isentropic
- Accounts for heat transfer during compression/expansion
- Polytropic efficiency often used instead of isentropic for long processes
- Typical reciprocating compressor: n = 1.25-1.30
- Typical centrifugal compressor: n = 1.30-1.35

---

### Adiabatic Process (No Heat Transfer)

**Definition:** No heat transfer occurs between system and surroundings (Q = 0, δQ = 0).

**First Law Application:**
```
Q = ΔU + W
0 = ΔU + W
W = -ΔU = -mCᵥ(T₂ - T₁)
```

**Types:**
1. Reversible adiabatic = Isentropic (s = constant)
2. Irreversible adiabatic (s increases due to friction/irreversibilities)

**HVAC Applications:**
- Rapid compression/expansion processes
- Insulated compressor analysis
- Throttling valves (also isenthalpic)
- Short-duration transient processes
- Nozzles and diffusers (high velocity, short time)

---

### Throttling Process (Isenthalpic)

**Definition:** Enthalpy remains constant (h = constant). Irreversible adiabatic process through a restriction with no work output.

**Governing Relations:**
- Enthalpy: h₁ = h₂
- No heat transfer: Q = 0
- No work: W = 0
- Entropy increases: s₂ > s₁ (irreversible)

**Pressure and Temperature:**
- Pressure drops: P₂ < P₁
- Temperature change depends on fluid properties
- For ideal gas: T₁ = T₂ (Joule-Thomson coefficient = 0)
- For real fluids: Temperature changes (Joule-Thomson effect)

**Joule-Thomson Coefficient:**
```
μJ = (∂T/∂P)h = (1/Cₚ)[T(∂V/∂T)P - V]
```

**HVAC Applications:**
- Thermostatic expansion valves (TXV)
- Electronic expansion valves (EEV)
- Capillary tubes
- Pressure reducing valves
- Orifice plates and flow restrictors
- Critical component in refrigeration cycles

**Practical Considerations:**
- Causes pressure drop and typically temperature drop in refrigerants
- No work recovery (irreversible process)
- Enthalpy remains constant but temperature and quality change
- Creates mixture of liquid and vapor in refrigeration systems

---

## Work and Heat Calculations Summary

### Boundary Work (Closed System)
```
W = ∫P dV

Isobaric: W = P(V₂ - V₁)
Isothermal: W = mRT ln(V₂/V₁)
Isochoric: W = 0
Isentropic: W = [P₁V₁/(k-1)][1 - (P₂/P₁)⁽ᵏ⁻¹⁾/ᵏ]
Polytropic: W = [P₁V₁/(n-1)][1 - (P₂/P₁)⁽ⁿ⁻¹⁾/ⁿ]
```

### Heat Transfer
```
General: Q = ΔU + W (First Law)

Isobaric: Q = mCₚ(T₂ - T₁)
Isothermal: Q = W = mRT ln(V₂/V₁)
Isochoric: Q = mCᵥ(T₂ - T₁)
Isentropic: Q = 0
Adiabatic: Q = 0
```

### Steady Flow Work (Open System)
```
W = -∫V dP (neglecting kinetic/potential energy)

Isentropic compression:
W = [kP₁V₁/(k-1)][(P₂/P₁)⁽ᵏ⁻¹⁾/ᵏ - 1]

Polytropic compression:
W = [nP₁V₁/(n-1)][(P₂/P₁)⁽ⁿ⁻¹⁾/ⁿ - 1]
```

---

## HVAC Process Applications Table

| Process Type | HVAC Application | Key Equations | Typical Conditions |
|--------------|------------------|---------------|-------------------|
| **Isothermal** | Evaporator, Condenser (phase change) | PV = C, Q = W | Saturation conditions |
| **Isobaric** | Heating coil, Cooling coil | Q = mCₚΔT | Atmospheric pressure |
| **Isochoric** | Storage tanks, Receivers | P/T = C, W = 0 | Rigid vessels |
| **Isentropic** | Ideal compressor | PVᵏ = C, Q = 0 | Efficiency baseline |
| **Polytropic** | Real compressor | PVⁿ = C | n = 1.2-1.35 |
| **Throttling** | Expansion valve | h₁ = h₂ | Pressure reduction |

---

## Process Path Representation

Thermodynamic processes are visualized on property diagrams:

**P-V Diagram (Pressure-Volume):**
- Shows boundary work as area under curve
- Isothermal: Hyperbolic curve (PV = constant)
- Isobaric: Horizontal line
- Isochoric: Vertical line
- Isentropic: Steep curve (PVᵏ = constant)

**T-s Diagram (Temperature-Entropy):**
- Shows heat transfer as area under curve
- Isothermal: Horizontal line
- Isentropic: Vertical line
- Area under curve = heat transfer for reversible process

**P-h Diagram (Pressure-Enthalpy):**
- Primary diagram for refrigeration cycle analysis
- Throttling: Vertical line (constant enthalpy)
- Isentropic compression: Steep curve
- Isobaric heat transfer: Horizontal line

---

## Combined Process Analysis

Real HVAC cycles combine multiple processes:

**Vapor Compression Cycle:**
1. Isentropic compression (ideal) or Polytropic (real): Compressor
2. Isobaric heat rejection: Condenser
3. Isenthalpic throttling: Expansion valve
4. Isobaric heat absorption: Evaporator

**Air Handling Process:**
1. Isobaric cooling: Cooling coil
2. Isobaric heating: Heating coil
3. Isobaric humidification: Spray chamber
4. Isobaric mixing: Return and outdoor air

**Compression with Intercooling:**
1. Polytropic compression: First stage
2. Isobaric cooling: Intercooler
3. Polytropic compression: Second stage
4. Improves efficiency over single-stage compression

---

## Reversible vs. Irreversible Processes

**Reversible Process:**
- Ideal, frictionless, quasi-static process
- No entropy generation (Δs_gen = 0)
- System and surroundings can return to initial state
- Maximum work output or minimum work input
- Serves as theoretical upper limit for real processes

**Irreversible Process:**
- All real processes are irreversible
- Entropy generation (Δs_gen > 0)
- Due to friction, heat transfer across finite ΔT, mixing, throttling
- Actual work greater than reversible work (compression)
- Actual work less than reversible work (expansion)

**Isentropic Efficiency Accounts for Irreversibilities:**
```
Compressor: ηc = W_isentropic/W_actual = 0.70-0.85
Turbine: ηt = W_actual/W_isentropic = 0.75-0.90
```

---

## Components

- Isobaric Constant Pressure
- Isochoric Constant Volume
- Isothermal Constant Temperature
- Isentropic Reversible Adiabatic
- Polytropic Pvn Constant
- Throttling Isenthalpic
- Adiabatic No Heat Transfer
- Reversible Processes
- Irreversible Processes
