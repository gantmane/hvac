---
title: "Horizontal Plate Freezers"
aliases: ["Horizontal Plate Freezers"]
description: "Comprehensive technical analysis of horizontal plate freezer design, hydraulic systems, refrigerant distribution, plate spacing, loading mechanisms, and capacity calculations for batch freezing operations"
weight: 2
---

## Horizontal Plate Freezer Configuration

Horizontal plate freezers employ a stacked arrangement of refrigerated platens oriented in horizontal planes to freeze packaged or bulk food products in batch operations. The horizontal configuration allows gravity-assisted loading and efficient stacking of multiple product layers within a single freezing chamber.

### Fundamental Design Principles

The horizontal plate freezer consists of parallel refrigerated plates arranged vertically in a stack, with adjustable spacing to accommodate product thickness. Each plate functions as an evaporator surface, conducting heat from products placed between adjacent plates through conduction heat transfer.

**Conduction Heat Transfer Mechanism:**

The freezing process relies on direct contact between product surfaces and refrigerated plates, maximizing heat transfer rates through conduction rather than convection or radiation. The contact pressure applied by hydraulic systems eliminates air gaps and ensures intimate thermal contact.

### Plate Construction and Materials

| Component | Material | Thickness | Thermal Conductivity |
|-----------|----------|-----------|---------------------|
| Contact Surface | Aluminum Alloy 6061-T6 | 6-10 mm | 167 W/(m·K) |
| Refrigerant Channels | Extruded Aluminum | Internal passages | 167 W/(m·K) |
| Surface Coating | Food-grade anodized | 15-25 μm | Protection layer |
| Insulation Backing | Polyurethane foam | 50-75 mm | 0.022 W/(m·K) |

Aluminum alloy provides optimal thermal conductivity, corrosion resistance, and weight characteristics. The extruded design incorporates internal refrigerant passages with serpentine or parallel flow configurations to ensure uniform temperature distribution across the plate surface.

## Stacked Plate Configuration

### Vertical Stack Arrangement

Horizontal plate freezers typically contain 10 to 30 refrigerated plates arranged vertically within an insulated cabinet. The number of plates determines batch capacity and overall freezer productivity.

**Stack Configuration Parameters:**

- **Plate Dimensions:** 1000-2000 mm length × 500-1200 mm width
- **Stack Height:** 2000-4000 mm total cabinet height
- **Plate Spacing Range:** 25-200 mm adjustable clearance
- **Number of Stations:** 10-30 freezing positions per cabinet

The vertical stack allows efficient floor space utilization, providing large freezing surface area within a compact footprint. Each plate position represents an independent freezing station for product packages.

### Plate Spacing Requirements

Adjustable plate spacing accommodates varying product thicknesses while maintaining the contact pressure required for effective heat transfer.

**Spacing Calculation:**

```
S = t_p + Δ_c + Δ_h
```

Where:
- S = Required plate spacing (mm)
- t_p = Product thickness (mm)
- Δ_c = Clearance allowance (3-5 mm)
- Δ_h = Hydraulic compression allowance (2-4 mm)

**Common Product Thickness Ranges:**

| Product Type | Typical Thickness | Plate Spacing |
|--------------|------------------|---------------|
| Fish fillets | 25-40 mm | 30-50 mm |
| Fish blocks | 50-100 mm | 55-110 mm |
| Burger patties | 15-25 mm | 20-35 mm |
| Formed products | 20-60 mm | 25-70 mm |
| Bulk cartons | 75-150 mm | 80-160 mm |

The hydraulic system adjusts plate positions to accommodate product height while applying controlled compression force during the freezing cycle.

## Hydraulic Pressure Systems

### Hydraulic Circuit Design

The hydraulic system provides vertical plate movement and applies contact pressure to products during freezing. Precision control of hydraulic force ensures adequate thermal contact without product damage.

**Hydraulic System Components:**

1. **Hydraulic Power Unit**
   - Electric motor: 3-7.5 kW
   - Hydraulic pump: Gear or piston type
   - Reservoir capacity: 50-200 liters
   - Operating pressure: 50-150 bar

2. **Plate Actuators**
   - Hydraulic cylinders: Single or double-acting
   - Cylinder diameter: 50-100 mm
   - Stroke length: 200-400 mm
   - Mounting: Frame-integrated

3. **Control Valves**
   - Proportional pressure control valves
   - Position feedback sensors
   - Safety relief valves
   - Manual override capability

### Contact Pressure Application

Applied hydraulic pressure creates contact force between products and refrigerated plates, eliminating air gaps that would impede heat transfer.

**Contact Pressure Calculation:**

```
P_c = F_h / A_p
```

Where:
- P_c = Contact pressure (kPa)
- F_h = Hydraulic force per station (N)
- A_p = Product contact area (m²)

**Recommended Contact Pressures:**

| Product Category | Contact Pressure | Purpose |
|-----------------|-----------------|---------|
| Soft products (fillets) | 5-15 kPa | Avoid crushing |
| Firm products (blocks) | 15-35 kPa | Good contact |
| Rigid packages | 35-70 kPa | Maximum transfer |
| Dense products | 50-100 kPa | Air elimination |

Excessive pressure damages delicate products, while insufficient pressure reduces heat transfer effectiveness and extends freezing time.

### Plate Movement Sequence

**Loading Sequence:**
1. Plates fully retracted to maximum spacing
2. Products manually loaded onto lower plates
3. Hydraulic system extends upper plates downward
4. Contact pressure applied and maintained
5. Freezing cycle initiated

**Unloading Sequence:**
1. Hydraulic system retracts plates upward
2. Products released from contact
3. Frozen products manually removed
4. Plates cleaned if required
5. Next batch loading begins

## Refrigerant Distribution

### Internal Refrigerant Circuits

Each plate contains internal passages through which refrigerant evaporates, absorbing heat from products in contact with plate surfaces. Refrigerant distribution design ensures uniform plate temperature.

**Flow Configuration Options:**

1. **Serpentine Flow**
   - Single continuous passage
   - Zigzag pattern across plate
   - Uniform refrigerant velocity
   - Simple distribution

2. **Parallel Flow**
   - Multiple parallel passages
   - Header distribution and collection
   - Lower pressure drop
   - More uniform temperature

3. **Spiral Flow**
   - Concentric spiral pattern
   - Center-to-edge or edge-to-center
   - Reduced refrigerant charge
   - Compact design

### Refrigerant Feed Systems

**Direct Expansion (DX) Configuration:**

The most common arrangement feeds refrigerant to each plate through thermostatic expansion valves or electronic expansion valves, maintaining optimal superheat control.

```
Q_evap = ṁ_r × (h_outlet - h_inlet)
```

Where:
- Q_evap = Evaporator capacity (kW)
- ṁ_r = Refrigerant mass flow rate (kg/s)
- h_outlet = Outlet specific enthalpy (kJ/kg)
- h_inlet = Inlet specific enthalpy (kJ/kg)

**Flooded Configuration:**

Some designs employ flooded evaporators with liquid refrigerant level control, providing more uniform plate temperatures but requiring larger refrigerant charge.

### Temperature Distribution

Uniform plate surface temperature ensures consistent product freezing across the entire contact area. Temperature variation should not exceed ±2°C across plate surfaces.

**Plate Temperature Monitoring:**

- Surface temperature sensors: RTD or thermocouple
- Measurement points: 4-6 locations per plate
- Control range: -35°C to -45°C typical
- Uniformity tolerance: ±1.5°C

## Loading and Unloading Mechanisms

### Manual Loading Operations

Horizontal plate freezers predominantly utilize manual loading due to batch operation and product variability. Operators load products onto plates when the stack is fully opened with maximum spacing.

**Loading Procedure:**

1. **Plate Opening**
   - Hydraulic system retracts all movable plates
   - Spacing adjusted to loading clearance
   - Fixed plates remain in position
   - Access clearance: 300-500 mm

2. **Product Placement**
   - Products positioned on lower plate surfaces
   - Alignment for uniform coverage
   - Edge clearance maintained
   - Multiple pieces per plate if applicable

3. **Stack Closure**
   - Hydraulic cylinders extend sequentially or simultaneously
   - Upper plates descend to contact products
   - Contact pressure applied
   - Position sensors confirm closure

**Loading Efficiency Factors:**

| Factor | Impact | Optimization |
|--------|--------|--------------|
| Operator access | Loading speed | Wide door openings |
| Plate height | Ergonomics | 500-1800 mm working zone |
| Product handling | Cycle time | Wheeled carts, conveyors |
| Stack configuration | Accessibility | Alternating fixed/movable |

### Semi-Automated Loading

Some installations incorporate mechanical assists to reduce labor requirements and improve consistency.

**Semi-Automation Options:**

- **Powered Conveyors:** Transport products to plate level
- **Pusher Mechanisms:** Slide products onto plates
- **Articulating Arms:** Position heavy products
- **Height-Adjustable Platforms:** Improve ergonomics

Complete automation remains uncommon due to product variability and batch nature of horizontal plate freezers.

### Unloading Mechanisms

**Manual Unloading:**

After freezing cycle completion, hydraulic system opens plates and operators remove frozen products. Frozen products may stick to plate surfaces, requiring release assistance.

**Release Enhancement Methods:**

1. **Brief Warm Refrigerant Pulse**
   - Momentary temperature increase
   - Melts ice interface
   - Product separates from plate
   - 10-30 second duration

2. **Mechanical Vibration**
   - Plate vibrators activated
   - Breaks ice bond
   - Gentle product release
   - Prevents damage

3. **Manual Prying Tools**
   - Food-grade plastic scrapers
   - Avoid metal damage to plates
   - Labor-intensive method
   - Used with difficult products

## Capacity Calculations

### Batch Freezing Time

The primary parameter affecting horizontal plate freezer capacity is the time required to freeze each product batch from initial temperature to final center temperature.

**Plank Freezing Time Equation:**

For flat products frozen from both surfaces (between two plates):

```
t_f = (ρ × L_f × a) / (T_m - T_p) × [P × a / 2 + R × a²]
```

Where:
- t_f = Freezing time (s)
- ρ = Product density (kg/m³)
- L_f = Latent heat of fusion (kJ/kg)
- a = Product thickness (m)
- T_m = Initial freezing point (°C)
- T_p = Plate temperature (°C)
- P = Precooling factor (dimensionless)
- R = Freezing resistance factor (dimensionless)

**Simplified Practical Equation:**

```
t_f = a² / (8 × α × ΔT_eff)
```

Where:
- α = Thermal diffusivity of frozen product (m²/s)
- ΔT_eff = Effective temperature difference (°C)

### Typical Freezing Times

| Product | Thickness | Initial Temp | Plate Temp | Freezing Time |
|---------|-----------|--------------|------------|---------------|
| Fish fillets | 30 mm | 0°C | -40°C | 1.5-2.0 hours |
| Fish blocks | 75 mm | 2°C | -40°C | 2.5-3.5 hours |
| Burger patties | 20 mm | 4°C | -35°C | 1.0-1.5 hours |
| Formed products | 50 mm | 0°C | -38°C | 2.0-2.8 hours |

### Daily Production Capacity

**Capacity Calculation:**

```
Q_daily = (N_plates × A_plate × ρ_load × 24) / (t_f + t_load + t_unload)
```

Where:
- Q_daily = Daily production capacity (kg/day)
- N_plates = Number of freezing stations
- A_plate = Plate area (m²)
- ρ_load = Product loading density (kg/m²)
- t_f = Freezing time (hours)
- t_load = Loading time (hours)
- t_unload = Unloading time (hours)

**Example Calculation:**

For a 20-plate horizontal plate freezer:
- Plate dimensions: 1.5 m × 1.0 m = 1.5 m² per plate
- Number of plates: 20 stations
- Loading density: 15 kg/m² (fish fillets)
- Freezing time: 2.0 hours
- Loading time: 0.3 hours
- Unloading time: 0.3 hours

```
Q_daily = (20 × 1.5 × 15 × 24) / (2.0 + 0.3 + 0.3)
Q_daily = 10,800 / 2.6 = 4,154 kg/day
```

### Refrigeration Load Calculation

**Total Heat Removal:**

```
Q_total = Q_sensible + Q_latent + Q_package + Q_misc
```

**Component Heat Loads:**

```
Q_sensible = ṁ_p × c_p × (T_initial - T_freeze)
Q_latent = ṁ_p × L_f × f_water
Q_package = ṁ_pkg × c_pkg × ΔT_pkg
Q_misc = Q_defrost + Q_cabinet + Q_infiltration
```

Where:
- ṁ_p = Product mass flow rate (kg/s)
- c_p = Specific heat capacity (kJ/kg·K)
- L_f = Latent heat of fusion for water (335 kJ/kg)
- f_water = Water fraction in product
- Q_misc = Miscellaneous heat gains (kW)

**Typical Refrigeration Loads:**

| Freezer Size | Plate Area | Product Load | Refrigeration Capacity |
|--------------|------------|--------------|----------------------|
| Small | 15-20 m² | 300-400 kg/batch | 25-35 kW |
| Medium | 25-35 m² | 500-700 kg/batch | 40-60 kW |
| Large | 40-60 m² | 800-1200 kg/batch | 70-100 kW |

## Product Applications

### Fish and Seafood Processing

Horizontal plate freezers are extensively used in fish processing operations due to their ability to freeze flat products rapidly with minimal quality degradation.

**Common Fish Products:**

1. **Fish Fillets**
   - Thickness: 20-40 mm
   - Individual quick frozen (IQF) or block
   - Excellent quality retention
   - Minimal drip loss

2. **Fish Blocks**
   - Standardized dimensions: 75 × 400 × 200 mm
   - Multiple fillets compressed together
   - Institutional and processing use
   - High-density freezing

3. **Shellfish**
   - Shrimp blocks
   - Scallop trays
   - Formed patties
   - Tray-packed products

### Meat and Poultry Products

**Suitable Applications:**

- Ground beef patties: Uniform thickness, rapid freezing
- Formed meat products: Consistent shape, good contact
- Sliced meats: Flat configuration, quality preservation
- Poultry portions: Breasts, thighs, uniform pieces

### Prepared Foods

**Convenience Food Products:**

| Product Category | Configuration | Freezing Advantage |
|-----------------|---------------|-------------------|
| Pizza (uncooked) | Flat rounds | Uniform freezing |
| Lasagna trays | Rectangular pans | Rapid solidification |
| Filled pastries | Flat pieces | Shape retention |
| Formed entrees | Portioned trays | Consistent quality |

### Packaging Considerations

**Optimal Package Types:**

1. **Flat Cartons**
   - Rigid construction
   - Good heat transfer
   - Standard dimensions
   - Stackable design

2. **Vacuum Bags**
   - Conform to plate surface
   - Excellent contact
   - Moisture barrier
   - Extended shelf life

3. **Aluminum Trays**
   - High thermal conductivity
   - Institutional portions
   - Reheating capability
   - Premium applications

Products with irregular shapes, excessive height variation, or air-filled packages freeze poorly in horizontal plate freezers due to inadequate contact with refrigerated surfaces.

## Equipment Specifications

### Standard Freezer Dimensions

| Parameter | Small Units | Medium Units | Large Units |
|-----------|-------------|--------------|-------------|
| Overall length | 2.0-2.5 m | 2.5-3.0 m | 3.0-4.0 m |
| Overall width | 1.5-2.0 m | 2.0-2.5 m | 2.5-3.0 m |
| Overall height | 2.5-3.0 m | 3.0-3.5 m | 3.5-4.5 m |
| Number of plates | 10-15 | 15-22 | 22-30 |
| Plate dimensions | 1.0×0.8 m | 1.5×1.0 m | 2.0×1.2 m |

### Refrigeration System Requirements

**Compressor Selection:**

- Reciprocating compressors: 10-40 kW units
- Screw compressors: 30-100 kW capacity
- Evaporating temperature: -42°C to -48°C
- Condensing temperature: +30°C to +40°C

**Refrigerant Options:**

| Refrigerant | Application | Advantages | Considerations |
|-------------|-------------|------------|----------------|
| R-404A | Traditional | Established performance | Phase-out concerns |
| R-507A | Alternative | Similar to R-404A | Phase-out concerns |
| R-448A | Low-GWP replacement | Reduced environmental impact | Lower capacity |
| R-449A | Low-GWP replacement | Drop-in characteristics | Pressure differences |
| NH3 (Ammonia) | Industrial systems | High efficiency, natural | Toxicity, regulations |
| CO2 cascade | Modern installations | Ultra-low GWP | Complex systems |

### Electrical Requirements

**Power Consumption Breakdown:**

- Refrigeration compressor: 15-75 kW
- Hydraulic pump motor: 3-7.5 kW
- Control systems: 0.5-1.5 kW
- Lighting and accessories: 0.5-1.0 kW
- Total connected load: 20-85 kW

**Voltage and Phase:**

- 380-480V, 3-phase, 50/60 Hz standard
- Motor starters and overload protection
- Variable frequency drives (VFD) for capacity control
- Power factor correction recommended

### Insulation and Construction

**Cabinet Insulation:**

- Material: Polyurethane foam injection
- Thickness: 100-150 mm walls, 150-200 mm floor/ceiling
- Thermal conductivity: 0.022 W/(m·K)
- Exterior finish: Stainless steel or painted steel

**Door Construction:**

- Insulated door panels: 100-125 mm thickness
- Heated door frames: Prevent ice buildup
- Magnetic or cam-lock seals
- Manual or powered operation

## Energy Efficiency

### Heat Transfer Optimization

Maximum energy efficiency in horizontal plate freezers requires optimizing heat transfer from products to refrigerant while minimizing parasitic heat gains.

**Heat Transfer Enhancement:**

1. **Contact Pressure Optimization**
   - Adequate pressure eliminates air gaps
   - Excessive pressure wastes hydraulic energy
   - Optimal range: 15-50 kPa for most products

2. **Plate Surface Condition**
   - Smooth, clean surfaces maximize contact
   - Regular cleaning removes residue
   - Surface roughness < 3.2 μm Ra

3. **Refrigerant Distribution**
   - Uniform plate temperature reduces freezing time
   - Proper superheat control (4-8°C)
   - Adequate refrigerant flow velocity

### Refrigeration System Efficiency

**Compressor Capacity Control:**

Variable capacity control matches refrigeration output to actual freezing load, reducing energy consumption during partial load operation.

- VFD-controlled screw compressors: 10-100% capacity
- Slide valve control: Step capacity reduction
- Cylinder unloaders: Reciprocating compressors
- Multiple compressor staging: Discrete steps

**Evaporator Temperature Management:**

```
COP_carnot = T_evap / (T_cond - T_evap)
```

Higher evaporator temperatures improve coefficient of performance but extend freezing time. Optimization balances energy cost and productivity.

**Optimal Evaporator Temperature Selection:**

| Product | Evaporator Temp | Freezing Time | Relative COP |
|---------|----------------|---------------|--------------|
| Fish fillets | -45°C | 1.8 hours | 1.00 |
| Fish fillets | -40°C | 2.1 hours | 1.15 |
| Fish fillets | -35°C | 2.6 hours | 1.32 |

The -40°C to -42°C range typically provides optimal balance between freezing time and energy efficiency for most applications.

### Heat Recovery Opportunities

**Desuperheating:**

Compressor discharge gas contains significant superheat that can be recovered for useful heating purposes.

```
Q_desuperheat = ṁ_r × c_p,vapor × (T_discharge - T_saturation)
```

Applications for recovered heat:
- Domestic hot water heating
- Space heating
- Defrost heat source
- Clean-in-place (CIP) water heating

**Condenser Heat Recovery:**

Total condenser heat equals refrigeration capacity plus compressor power, representing substantial energy recovery potential.

```
Q_condenser = Q_evaporator + P_compressor
```

For a 50 kW evaporator capacity with 20 kW compressor power:
- Available condenser heat: 70 kW
- Temperature: 35-45°C
- Applications: Process heating, space heating, water heating

### Defrost Energy Management

Horizontal plate freezers require periodic defrost to remove ice accumulation on plate surfaces from product moisture and infiltration air.

**Defrost Methods:**

1. **Hot Gas Defrost**
   - Compressor discharge gas circulated through plates
   - Rapid melting: 15-30 minutes
   - Energy from refrigeration system
   - Most common method

2. **Electric Defrost**
   - Resistance heaters in plate assemblies
   - Precise control
   - Higher operating cost
   - Backup defrost method

3. **Water Defrost**
   - Warm water circulated through plates
   - Fast defrost
   - Requires water heating and drainage
   - Limited applications

**Defrost Optimization:**

- Demand defrost: Initiate based on pressure drop or temperature
- Time-of-day scheduling: Off-peak electricity rates
- Defrost termination: Temperature-based to avoid excessive heating
- Frequency: 1-3 times per 24 hours typical

### Insulation Performance

Minimizing cabinet heat gain reduces refrigeration load and improves energy efficiency.

**Heat Gain Calculation:**

```
Q_transmission = U × A × (T_ambient - T_cabinet)
```

Where:
- U = Overall heat transfer coefficient (W/m²·K)
- A = Cabinet surface area (m²)
- T_ambient = Ambient temperature (°C)
- T_cabinet = Cabinet temperature (°C)

**Insulation Performance:**

For 150 mm polyurethane insulation:
- U-value: 0.14 W/(m²·K)
- 30 m² cabinet surface area
- 25°C ambient, -35°C cabinet interior
- Heat gain: Q = 0.14 × 30 × 60 = 252 W

Thermal bridging at structural penetrations and door seals can increase actual heat gain by 20-40% above calculated values.

### Loading Efficiency Impact

Maximizing plate utilization per batch reduces energy consumption per kilogram of frozen product.

**Specific Energy Consumption:**

```
SEC = (E_refrigeration + E_hydraulic + E_auxiliary) / m_product
```

Where:
- SEC = Specific energy consumption (kWh/kg)
- E = Energy consumption by component (kWh/batch)
- m_product = Product mass per batch (kg)

**Efficiency Optimization:**

- Full plate loading: Minimize energy per kg
- Proper product sizing: Maximize contact area
- Reduced loading/unloading time: Minimize infiltration
- Batch scheduling: Reduce idle time

Typical specific energy consumption: 0.08-0.15 kWh/kg for fish products at high loading efficiency.

