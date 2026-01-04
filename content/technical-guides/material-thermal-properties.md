---
title: "Material Thermal Properties for HVAC Engineers"
description: "Comprehensive reference tables of thermal conductivity, specific heat, density, and thermal diffusivity for building materials, insulation, and HVAC components."
keywords: ["thermal conductivity", "specific heat", "thermal properties", "insulation R-value", "material properties", "building envelope"]
author: "Evgeniy Gantman"
date: 2026-01-04
weight: 31
---

# Material Thermal Properties for HVAC Engineers

Accurate thermal property data drives heat transfer calculations, insulation sizing, and energy analysis. This reference consolidates thermal conductivity, specific heat, density, and derived properties for common HVAC and building materials.

## Fundamental Thermal Properties

**Thermal Conductivity (k):** Heat flux through unit thickness per unit temperature difference

$$k = \frac{q \cdot L}{A \cdot \Delta T}$$

Units: Btu·in/(hr·ft²·°F) or W/(m·K)

**Specific Heat (c):** Energy to raise unit mass by one degree

Units: Btu/(lb·°F) or kJ/(kg·K)

**Density (ρ):** Mass per unit volume

Units: lb/ft³ or kg/m³

**Thermal Diffusivity (α):** Rate of temperature propagation

$$\alpha = \frac{k}{\rho c}$$

Units: ft²/hr or m²/s

## Building Envelope Materials

### Masonry and Concrete

| Material | k (Btu·in/hr·ft²·°F) | ρ (lb/ft³) | c (Btu/lb·°F) | R-value per inch |
|----------|----------------------|-----------|---------------|------------------|
| Concrete (normal weight) | 12.0 | 144 | 0.20 | 0.08 |
| Concrete (lightweight) | 3.2 | 70 | 0.20 | 0.31 |
| Brick (common) | 5.0 | 120 | 0.22 | 0.20 |
| Brick (face) | 9.0 | 130 | 0.22 | 0.11 |
| Concrete block (8\") | 1.11 (effective) | - | - | 0.90 (whole unit) |
| Concrete block (hollow) | 0.90 (effective) | - | - | 1.11 (whole unit) |
| Stone | 12.5 | 140 | 0.22 | 0.08 |
| Mortar | 5.0 | 100 | 0.20 | 0.20 |

### Wood and Wood Products

| Material | k (Btu·in/hr·ft²·°F) | ρ (lb/ft³) | c (Btu/lb·°F) | R-value per inch |
|----------|----------------------|-----------|---------------|------------------|
| Softwood lumber | 0.80 | 32 | 0.33 | 1.25 |
| Hardwood lumber | 1.10 | 45 | 0.30 | 0.91 |
| Plywood | 0.80 | 34 | 0.33 | 1.25 |
| Oriented strand board (OSB) | 0.82 | 37 | 0.33 | 1.22 |
| Particleboard | 0.94 | 50 | 0.31 | 1.06 |
| Hardboard | 1.00 | 63 | 0.31 | 1.00 |

### Insulation Materials

| Material | k (Btu·in/hr·ft²·°F) | ρ (lb/ft³) | R-value per inch |
|----------|----------------------|-----------|------------------|
| Fiberglass batt | 0.27 | 0.6 | 3.70 |
| Mineral wool batt | 0.29 | 1.5 | 3.45 |
| Cellulose (loose-fill) | 0.27 | 2.3 | 3.70 |
| Expanded polystyrene (EPS) | 0.26 | 1.0 | 3.85 |
| Extruded polystyrene (XPS) | 0.20 | 1.8 | 5.00 |
| Polyisocyanurate (foil-faced) | 0.16 | 2.0 | 6.25 |
| Spray polyurethane foam (closed-cell) | 0.16 | 2.0 | 6.25 |
| Spray polyurethane foam (open-cell) | 0.25 | 0.5 | 4.00 |

### Gypsum and Plaster

| Material | k (Btu·in/hr·ft²·°F) | ρ (lb/ft³) | c (Btu/lb·°F) | R-value per inch |
|----------|----------------------|-----------|---------------|------------------|
| Gypsum board (drywall) | 1.11 | 50 | 0.26 | 0.90 |
| Gypsum plaster | 3.12 | 105 | 0.20 | 0.32 |
| Cement plaster (stucco) | 5.00 | 116 | 0.20 | 0.20 |

## Glazing and Fenestration

| Material | k (Btu·in/hr·ft²·°F) | ρ (lb/ft³) | U-value (Btu/hr·ft²·°F) | SHGC |
|----------|----------------------|-----------|-------------------------|------|
| Single glazing (1/4\") | 60.0 | 158 | 1.04 | 0.86 |
| Double glazing (1/4\" air gap) | - | - | 0.48 | 0.76 |
| Double glazing (1/2\" air gap) | - | - | 0.49 | 0.70 |
| Double glazing (low-e, argon) | - | - | 0.26-0.30 | 0.27-0.40 |
| Triple glazing (low-e, argon) | - | - | 0.15-0.20 | 0.23-0.35 |

SHGC = Solar Heat Gain Coefficient

## Roofing and Siding Materials

| Material | k (Btu·in/hr·ft²·°F) | ρ (lb/ft³) | R-value per inch |
|----------|----------------------|-----------|------------------|
| Asphalt shingles | 6.5 | 70 | 0.15 |
| Clay tile | 5.0 | 120 | 0.20 |
| Metal roofing | 1200 | 480 | negligible |
| Built-up roofing (BUR) | 1.0 | 70 | 1.00 |
| EPDM membrane | 1.15 | 70 | 0.87 |
| Vinyl siding | 0.60 | 85 | 1.67 |
| Aluminum siding | 1400 | 170 | negligible |
| Fiber cement siding | 2.0 | 88 | 0.50 |

## HVAC Component Materials

### Duct Materials

| Material | k (Btu·in/hr·ft²·°F) | Application |
|----------|----------------------|-------------|
| Galvanized steel | 310 | Sheet metal duct |
| Aluminum | 1400 | Flexible duct core |
| Fiberglass duct board | 0.25 | Insulated ductwork |
| Phenolic foam duct | 0.16 | Pre-insulated duct |

### Pipe Insulation

| Material | k (Btu·in/hr·ft²·°F) | Max Temp (°F) | R-value per inch |
|----------|----------------------|---------------|------------------|
| Fiberglass pipe insulation | 0.25-0.27 | 450 | 3.70-4.00 |
| Elastomeric foam | 0.28 | 220 | 3.57 |
| Polyisocyanurate | 0.16 | 300 | 6.25 |
| Calcium silicate | 0.40 | 1200 | 2.50 |
| Mineral wool | 0.29 | 1200 | 3.45 |

## Refrigerants and Heat Transfer Fluids

### Common Refrigerants (at 40°F)

| Refrigerant | k (Btu·in/hr·ft²·°F) | ρ (lb/ft³) | c (Btu/lb·°F) |
|-------------|----------------------|-----------|---------------|
| R-410A (liquid) | 0.59 | 71.4 | 0.38 |
| R-134a (liquid) | 0.54 | 75.3 | 0.34 |
| R-22 (liquid) | 0.50 | 76.0 | 0.30 |
| Ammonia (liquid) | 2.92 | 38.0 | 1.08 |

### Heat Transfer Fluids

| Fluid | k (Btu·in/hr·ft²·°F) | ρ (lb/ft³) | c (Btu/lb·°F) | Freeze Point (°F) |
|-------|----------------------|-----------|---------------|-------------------|
| Water (60°F) | 4.1 | 62.4 | 1.00 | 32 |
| Ethylene glycol (30%) | 3.3 | 65.0 | 0.90 | 0 |
| Propylene glycol (30%) | 3.1 | 64.5 | 0.92 | 4 |
| Ethylene glycol (50%) | 2.7 | 67.0 | 0.82 | -34 |

## Soil and Groun

d Properties

| Material | k (Btu·in/hr·ft²·°F) | ρ (lb/ft³) | c (Btu/lb·°F) | Application |
|----------|----------------------|-----------|---------------|-------------|
| Clay (dry) | 1.1 | 100 | 0.21 | Ground-source heat pumps |
| Clay (wet) | 7.0 | 110 | 0.35 | GSHP |
| Sand (dry) | 2.0 | 95 | 0.19 | GSHP |
| Sand (wet) | 12.0 | 120 | 0.33 | GSHP |
| Rock | 18.0 | 165 | 0.20 | GSHP, thermal storage |

Moisture content dramatically increases thermal conductivity.

## Temperature Dependence

Thermal conductivity varies with temperature:

$$k(T) = k_0 [1 + \alpha(T - T_0)]$$

Where:
- $k_0$ = conductivity at reference temperature $T_0$
- $\alpha$ = temperature coefficient (typically 0.001-0.005 per °F)

**Example:** Fiberglass insulation increases conductivity ~5% from 0°F to 100°F.

## Practical Applications

**Insulation R-value:**

$$R = \frac{L}{k}$$

Where L = thickness (inches)

**Composite wall U-value:**

$$U = \frac{1}{R_{total}} = \frac{1}{R_1 + R_2 + ... + R_n + R_{air films}}$$

**Heat storage capacity:**

$$Q = m \cdot c \cdot \Delta T = \rho \cdot V \cdot c \cdot \Delta T$$

---

**Related Technical Guides:**
- [Heat Transfer Fundamentals](/technical-guides/heat-transfer-fundamentals/)
- [Building Envelope Heat Transfer](/technical-guides/building-envelope-heat-transfer/)
- [Heating Load Calculations](/technical-guides/heating-load-calculations/)

**References:**
- ASHRAE Handbook of Fundamentals, Chapter 26: Heat, Air, and Moisture Control in Building Assemblies
- ASHRAE Handbook of Fundamentals, Chapter 33: Physical Properties of Materials
- 2021 ASHRAE Handbook—Fundamentals, Chapter 26
