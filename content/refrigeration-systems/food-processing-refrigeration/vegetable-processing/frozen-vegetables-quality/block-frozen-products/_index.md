---
title: "Block Frozen Products"
aliases: ["Block Frozen Products"]
description: "Technical analysis of block freezing systems including plate freezer design, heat transfer calculations, freezing time prediction, and applications for institutional food service products"
weight: 2
---

Block freezing represents a high-efficiency method for freezing vegetables in compressed rectangular forms using contact plate freezers. This process provides superior heat transfer rates compared to air blast freezing through direct conduction, making it economically advantageous for institutional and food service applications where individual particle integrity is not critical.

## Plate Freezer Fundamentals

Plate freezers consist of hollow metal plates through which refrigerant flows, creating large heat transfer surfaces that contact product packages on both sides. The plates are constructed from aluminum or stainless steel, typically 12-25 mm thick, with internal refrigerant passages.

### Operating Principles

Heat transfer occurs primarily through conduction from the product through the package material into the refrigerated plates. The overall heat transfer coefficient ranges from 40-120 W/m²·K, significantly higher than air blast systems at 15-35 W/m²·K.

The refrigerant temperature typically operates at -35°C to -40°C, with evaporating pressures of 50-100 kPa (absolute) for ammonia systems or 100-180 kPa for R-404A systems. This temperature differential drives rapid heat extraction from product blocks.

## Plate Freezer Design Parameters

| Parameter | Specification | Notes |
|-----------|---------------|-------|
| Plate spacing | 50-150 mm | Adjustable for different block heights |
| Plate temperature | -35°C to -40°C | Refrigerant evaporating temperature |
| Hydraulic pressure | 20-60 kPa | Applied to ensure plate contact |
| Contact area | 0.25-2.0 m² per station | Per product block |
| Plate material | Aluminum or stainless steel | Aluminum preferred for conductivity |
| Plate thickness | 12-25 mm | Balance between strength and weight |

### Hydraulic System Design

Plate freezers employ hydraulic systems to apply pressure ensuring intimate contact between plates and product packages. Hydraulic pressure of 20-60 kPa (3-9 psi) eliminates air gaps that would create thermal resistance. The pressure must be sufficient to compress the product slightly without damaging packaging.

Horizontal plate freezers typically use hydraulic rams to close vertical stacks of plates. Vertical plate freezers use individual hydraulic cylinders for each plate pair, allowing independent operation of freezing stations.

## Freezing Time Calculations

Freezing time for block products depends on product thickness, initial and final temperatures, thermal properties, and heat transfer coefficients. The Plank equation provides the theoretical basis:

**Plank Equation for Freezing Time:**

t = (ρL/ΔT) × (Pa/h + Ra²/k)

Where:
- t = freezing time (s)
- ρ = product density (kg/m³)
- L = latent heat of fusion (kJ/kg)
- ΔT = temperature difference between refrigerant and initial freezing point (K)
- P = dimensionless parameter (1/2 for infinite slab)
- R = dimensionless parameter (1/8 for infinite slab)
- a = half-thickness of slab (m)
- h = surface heat transfer coefficient (W/m²·K)
- k = thermal conductivity of frozen product (W/m·K)

### Practical Freezing Time Estimates

| Product Type | Block Thickness | Typical Freezing Time | Heat Flux |
|--------------|-----------------|----------------------|-----------|
| Spinach blocks | 50 mm | 1.5-2.0 hours | 8-12 kW/m² |
| Mixed vegetables | 75 mm | 2.5-3.5 hours | 6-10 kW/m² |
| Leafy greens | 60 mm | 1.8-2.5 hours | 7-11 kW/m² |
| Chopped collards | 50 mm | 1.5-2.2 hours | 8-11 kW/m² |

### Modified Plank Equation

For better accuracy with finite cooling times, the modified Plank equation accounts for sensible heat removal above and below the freezing point:

t_total = t_precool + t_freezing + t_tempering

Where precooling time brings product from initial temperature to initial freezing point, freezing time represents the phase change period, and tempering time reduces temperature from initial freezing point to final storage temperature.

## Heat Transfer Through Product Mass

Heat transfer in block frozen products involves three distinct zones as the freezing front propagates from surfaces toward the geometric center.

### Thermal Resistance Network

The total thermal resistance consists of:

1. **Surface boundary layer**: Refrigerant to plate inner surface
2. **Plate material**: Conduction through metal
3. **Plate-package interface**: Contact resistance minimized by hydraulic pressure
4. **Package material**: Paperboard or plastic film
5. **Frozen product layer**: Increasing thickness as freezing progresses
6. **Unfrozen product core**: Decreasing thickness during freezing

The controlling resistance shifts during freezing. Initially, unfrozen product thermal conductivity (0.4-0.6 W/m·K) dominates. As the frozen layer grows with higher conductivity (1.2-2.0 W/m·K), the unfrozen core becomes the limiting factor.

### Temperature Profiles

Temperature distribution through a freezing block shows:

- **Frozen zone**: Nearly linear gradient from surface (-30°C to -35°C) toward freezing front
- **Freezing front**: Sharp temperature change across phase transition zone (-1°C to -3°C)
- **Unfrozen center**: Gradual cooling toward initial freezing point

The freezing front velocity decreases with time as heat must conduct through increasing frozen layer thickness. Initial freezing rates of 2-4 mm/min decrease to 0.5-1.0 mm/min as the frozen layer approaches the center.

## Product Thermal Properties

| Property | Unfrozen | Frozen | Units |
|----------|----------|--------|-------|
| Thermal conductivity (k) | 0.45-0.60 | 1.4-2.0 | W/m·K |
| Specific heat (cp) | 3.5-4.0 | 1.8-2.1 | kJ/kg·K |
| Density (ρ) | 950-1050 | 900-1000 | kg/m³ |
| Latent heat (L) | 250-310 | - | kJ/kg |
| Initial freezing point | -0.5 to -2.0 | - | °C |

Vegetable products with high water content (85-95%) exhibit latent heat values of 280-310 kJ/kg, representing the dominant energy removal requirement. Sensible heat removal typically accounts for 15-25% of total refrigeration load.

## Plate Freezer Configurations

### Horizontal Plate Freezers

Horizontal configurations feature vertical stacks of horizontal plates, with products loaded from one end and discharged from the opposite end. Typical capacities range from 1000-3000 kg per load, with 8-24 freezing stations per unit.

**Advantages:**
- Simple loading and unloading mechanisms
- Uniform pressure distribution across product surface
- Efficient use of floor space
- Lower capital cost per unit capacity

**Disadvantages:**
- Sequential loading and unloading limits throughput
- Product must be self-supporting during loading
- Limited flexibility in block dimensions

### Vertical Plate Freezers

Vertical plate freezers position plates vertically with product blocks inserted horizontally between adjacent plates. Each station operates independently, allowing continuous loading and unloading.

**Advantages:**
- Continuous operation increases throughput
- Individual station control provides flexibility
- Easier automation integration
- Better accommodation of odd-sized products

**Disadvantages:**
- Higher capital cost
- More complex hydraulic systems
- Larger footprint per unit capacity
- Requires more sophisticated controls

## Applications and Product Types

Block freezing suits products where individual piece identity is not required and high packing density provides economic advantages.

### Primary Applications

| Product Category | Typical Block Size | Target Market | Advantages |
|------------------|-------------------|---------------|------------|
| Spinach | 20 kg blocks (400×300×50 mm) | Institutional kitchens | Minimal oxidation, compact storage |
| Collard greens | 15 kg blocks (350×250×60 mm) | Food service | Reduced handling, consistent portions |
| Kale | 12 kg blocks (300×250×50 mm) | Processing ingredient | Pre-blanched, ready-to-use |
| Mixed vegetables | 10 kg blocks (300×200×75 mm) | Institutional | Cost-effective, stable quality |
| Vegetable purees | 25 kg blocks (400×300×75 mm) | Food manufacturing | Homogeneous product, easy thawing |

### Leafy Greens Processing

Leafy vegetables represent the ideal candidates for block freezing due to their natural compressibility and the preference for compressed forms in institutional cooking. Spinach, collards, kale, and similar products are blanched, cooled, dewatered to 88-92% moisture, and compressed into blocks before freezing.

The compression during packaging removes interstitial air, improving both heat transfer during freezing and storage density. Blocks can achieve densities of 400-600 kg/m³ compared to 150-250 kg/m³ for loosely packed IQF leafy greens.

## Quality Considerations vs IQF

Block freezing and individually quick frozen (IQF) methods serve different market segments with distinct quality attributes and cost structures.

### Quality Comparison Matrix

| Quality Factor | Block Frozen | IQF | Notes |
|----------------|--------------|-----|-------|
| Individual piece integrity | Poor | Excellent | Blocks lose piece identity |
| Color retention | Good | Excellent | Minimal air exposure in blocks |
| Texture after thawing | Acceptable | Superior | Compression affects texture |
| Freezing rate | Moderate | Fast | Contact vs. air blast |
| Drip loss on thawing | Moderate (3-5%) | Low (1-3%) | Cell damage from compression |
| Storage density | Excellent | Fair | 2.5-3× higher for blocks |
| Production cost | Low | High | Energy and capital costs |

### Freezing Rate Impact

Block frozen products experience moderate freezing rates of 2-5 cm/hour from surface to center, compared to IQF rates of 5-15 cm/hour for individual pieces. The slower freezing in block centers can result in larger ice crystal formation, potentially affecting texture.

However, for products destined for cooking applications where texture is less critical, this quality difference is acceptable given the substantial cost advantages of block freezing.

## Packaging Requirements

Block frozen products require rigid or semi-rigid packaging that can withstand hydraulic pressure without deformation while providing adequate moisture barrier properties.

### Common Package Types

**Wax-coated paperboard cartons:**
- Thickness: 0.75-1.5 mm
- Moisture barrier: Wax coating or polyethylene liner
- Thermal conductivity: 0.15-0.25 W/m·K
- Cost: Low to moderate
- Recyclability: Limited

**Corrugated containers with plastic liners:**
- Outer: Corrugated board for structure
- Inner: 50-100 μm polyethylene film
- Better moisture protection than wax coating
- Improved stacking strength
- Moderate cost

### Package Thermal Impact

Package thermal resistance typically contributes 5-15% of total thermal resistance in plate freezing operations. Thinner packages with higher thermal conductivity reduce freezing times but must maintain adequate strength under hydraulic pressure.

The package-plate interface represents a critical contact resistance. Hydraulic pressure of 30-50 kPa compresses packaging surfaces against plates, reducing air gaps and minimizing interfacial thermal resistance to 0.0001-0.0005 m²·K/W.

## Refrigeration System Design

Plate freezer refrigeration systems must provide consistent low temperatures with adequate capacity to handle peak heat loads during initial product loading.

### Refrigeration Load Calculation

Total refrigeration load consists of:

**Product load:**
Q_product = m × [cp,u × ΔT_precool + L + cp,f × ΔT_subcool]

**Transmission load:**
Q_trans = U × A × LMTD

**Infiltration load:**
Q_inf = n × V × ρ_air × cp,air × ΔT

Where typical values for a 2000 kg/hour plate freezer system:
- Product load: 150-180 kW (peak)
- Transmission losses: 8-15 kW
- Infiltration: 5-10 kW
- Total design capacity: 175-220 kW

### Compressor Selection

Ammonia screw compressors or reciprocating compressors sized for -40°C evaporating temperature and +35°C condensing temperature typically serve plate freezer systems. The temperature lift of 75 K results in compression ratios of 8-10 for ammonia, requiring single-stage economized or two-stage compression.

## Process Control and Optimization

Modern plate freezer systems employ programmable logic controllers (PLCs) to optimize freezing cycles and minimize energy consumption while maintaining product quality.

### Control Parameters

**Temperature control:**
- Refrigerant evaporating temperature: ±1°C
- Plate surface temperature: ±2°C
- Product core temperature monitoring

**Pressure control:**
- Hydraulic pressure setpoint
- Pressure uniformity across stations
- Automatic pressure relief

**Time control:**
- Programmable freezing cycles
- Variable time based on product type
- Automatic cycle completion sensing

### Energy Optimization

Freezing time optimization balances throughput requirements against energy consumption. Excessively long freezing cycles waste energy cooling products below required temperatures. Insufficient time results in warm centers and quality issues.

Temperature sensors embedded in representative product blocks provide real-time feedback for cycle completion. When the geometric center reaches -18°C, the freezing cycle terminates, and plates separate for product removal.

## Throughput and Capacity

Plate freezer capacity depends on the number of freezing stations, block size, and cycle time.

**Capacity equation:**
Throughput = (Number of stations × Block mass) / Cycle time

Example calculation for a 20-station horizontal plate freezer:
- Block mass: 20 kg
- Cycle time: 2.5 hours (including loading/unloading)
- Throughput: (20 × 20) / 2.5 = 160 kg/hour

For continuous 24-hour operation:
Daily capacity = 160 × 24 = 3840 kg/day

## Installation and Maintenance Considerations

Plate freezers require careful installation to ensure proper leveling, hydraulic system integrity, and refrigerant distribution.

### Installation Requirements

**Structural:**
- Level floor within ±3 mm per meter
- Floor load capacity: 1500-2500 kg/m²
- Vibration isolation pads for compressor equipment

**Refrigerant distribution:**
- Proper oil return design for horizontal plates
- Adequate refrigerant charge for flood-type systems
- Pressure drop limitations: <20 kPa through plates

### Maintenance Protocol

**Daily tasks:**
- Visual inspection of hydraulic pressure
- Refrigerant temperature logging
- Product quality spot checks

**Weekly tasks:**
- Hydraulic fluid level verification
- Refrigerant leak detection
- Plate surface cleaning (if required)

**Monthly tasks:**
- Hydraulic system inspection
- Refrigerant charge verification
- Pressure transducer calibration

**Annually:**
- Complete hydraulic system service
- Refrigerant system inspection
- Plate flatness verification
- Thermal performance testing

Block freezing technology provides a cost-effective method for freezing vegetable products destined for institutional food service and ingredient applications. The superior heat transfer of contact plate freezers combined with high packing density and simplified handling makes this process economically attractive despite quality trade-offs compared to IQF methods. Proper design, operation, and maintenance of plate freezer systems ensures consistent product quality while maximizing energy efficiency and throughput.
