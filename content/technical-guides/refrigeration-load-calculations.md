---
title: "Refrigeration Load Calculations for Cold Storage & Food Processing"
description: "Comprehensive methodology for calculating refrigeration loads including transmission, product cooling, respiration, infiltration, equipment, and safety factors for cold storage design."
keywords: ["refrigeration load", "cold storage design", "product load", "infiltration load", "respiration heat", "cooling load calculation", "freezer design"]
author: "Evgeniy Gantman"
date: 2026-01-04
weight: 37
---

# Refrigeration Load Calculations for Cold Storage & Food Processing

Accurate refrigeration load calculations determine equipment capacity, operating costs, and temperature control performance. This guide covers all heat gain components for cold storage, food processing, and commercial refrigeration applications, with calculation methodology per ASHRAE Refrigeration Handbook.

## Total Refrigeration Load Components

**Total heat gain:**

$$Q_{total} = Q_{trans} + Q_{prod} + Q_{resp} + Q_{inf} + Q_{equip} + Q_{people} + Q_{other}$$

Where:
- $Q_{trans}$ = transmission load through walls, floor, ceiling
- $Q_{prod}$ = product load (cooling from initial to final temperature)
- $Q_{resp}$ = respiration heat from living produce
- $Q_{inf}$ = infiltration load (air exchange, door openings)
- $Q_{equip}$ = equipment heat (fans, lights, forklifts)
- $Q_{people}$ = occupant heat gain
- $Q_{other}$ = miscellaneous loads (defrost, piping heat gain)

## Transmission Load

### Wall, Ceiling, Floor Heat Gain

**Heat transfer through envelope:**

$$Q_{trans} = U \cdot A \cdot \Delta T$$

Where:
- $U$ = overall heat transfer coefficient (Btu/hr·ft²·°F)
- $A$ = surface area (ft²)
- $\Delta T$ = temperature difference, outdoor - indoor (°F)

**U-value calculation:**

$$U = \frac{1}{R_{total}} = \frac{1}{R_{out} + R_{wall} + R_{insulation} + R_{in}}$$

**Typical U-values for insulated cold storage:**

| Application | U-value (Btu/hr·ft²·°F) | R-value (ft²·°F·hr/Btu) |
|-------------|-------------------------|-------------------------|
| Cooler wall (35-50°F) | 0.04-0.06 | R-16 to R-25 |
| Freezer wall (-10 to 0°F) | 0.025-0.04 | R-25 to R-40 |
| Cooler ceiling | 0.03-0.05 | R-20 to R-33 |
| Freezer ceiling | 0.02-0.03 | R-33 to R-50 |
| Floor (insulated slab) | 0.05-0.08 | R-12 to R-20 |

**Design temperature differences:**

| Space Type | Indoor Temp | Outdoor Design Temp | ΔT |
|------------|-------------|---------------------|-----|
| Produce cooler | 35°F | 95°F | 60°F |
| Meat cooler | 32°F | 95°F | 63°F |
| Freezer | -10°F | 95°F | 105°F |
| Ice cream hardening | -20°F | 95°F | 115°F |

### Solar Radiation Load

**Roof solar gain (additional to transmission):**

$$Q_{solar} = A_{roof} \cdot CLTD$$

Where CLTD = Cooling Load Temperature Difference (includes solar effect)

**Typical CLTD for dark roof in summer:** 30-50°F (add to ambient ΔT)

**Mitigation:**
- White reflective roof coating (reduces solar gain 40-60%)
- Insulation above roof deck
- Ventilated air space

## Product Load

### Sensible Cooling Above Freezing

**Heat removal to cool product from initial to final temperature:**

$$Q_{prod,sensible} = \frac{m \cdot c_p \cdot (T_i - T_f)}{t}$$

Where:
- $m$ = product mass (lb)
- $c_p$ = specific heat above freezing (Btu/lb·°F)
- $T_i$ = initial product temperature (°F)
- $T_f$ = final product temperature (°F)
- $t$ = cooling time (hr)

**Typical specific heats (above freezing):**

| Product | Specific Heat (Btu/lb·°F) | Water Content (%) |
|---------|---------------------------|-------------------|
| Beef | 0.77 | 75% |
| Pork | 0.68 | 60% |
| Chicken | 0.80 | 75% |
| Apples | 0.90 | 84% |
| Lettuce | 0.96 | 95% |
| Eggs | 0.76 | 74% |
| Milk | 0.93 | 87% |

**Approximation:** $c_p \approx 0.20 + 0.008 \times \%_{water}$

### Freezing Load

**Heat removal during freezing:**

$$Q_{freezing} = m \cdot h_{latent}$$

Where $h_{latent}$ = latent heat of fusion (Btu/lb)

**Latent heat approximation:**

$$h_{latent} = 144 \times \%_{water}/100$$

**Example:** Beef (75% water): $h_{latent} = 144 \times 0.75 = 108$ Btu/lb

### Sensible Cooling Below Freezing

**Heat removal after freezing:**

$$Q_{prod,frozen} = \frac{m \cdot c_{p,frozen} \cdot (T_f - T_{storage})}{t}$$

Where $c_{p,frozen}$ = specific heat below freezing (typically 0.35-0.50 Btu/lb·°F)

**Total freezing load:**

$$Q_{prod,total} = Q_{above} + Q_{freezing} + Q_{below}$$

<div class="worked-example">
<h3>Worked Example 1: Product Cooling Load</h3>

**Given:**
- Product: 10,000 lb beef (initially 70°F)
- Cooling: 70°F → 28°F (above freezing), then freeze to 0°F
- Cooling time: 24 hours
- Specific heat above freezing: 0.77 Btu/lb·°F
- Latent heat: 108 Btu/lb (75% water content)
- Specific heat below freezing: 0.42 Btu/lb·°F
- Freezing point: 28°F

**Find:** Total product load (Btu/hr)

**Solution:**

Sensible cooling (70°F → 28°F):
$$Q_1 = \frac{10,000 \times 0.77 \times (70 - 28)}{24} = 13,479 \text{ Btu/hr}$$

Latent heat (freezing at 28°F):
$$Q_2 = \frac{10,000 \times 108}{24} = 45,000 \text{ Btu/hr}$$

Sensible cooling below freezing (28°F → 0°F):
$$Q_3 = \frac{10,000 \times 0.42 \times (28 - 0)}{24} = 4,900 \text{ Btu/hr}$$

Total average product load:
$$Q_{prod} = 13,479 + 45,000 + 4,900 = 63,379 \text{ Btu/hr} = 5.3 \text{ tons}$$

**Peak load** occurs during freezing phase: **45,000 Btu/hr**

**Answer:** Average load: 63,379 Btu/hr (5.3 tons) over 24 hours; Peak: 45,000 Btu/hr during freezing

</div>

## Respiration Load

**Fresh fruits and vegetables generate heat through respiration:**

$$Q_{resp} = m \cdot q_{resp}$$

Where:
- $m$ = product mass (lb or ton)
- $q_{resp}$ = specific respiration heat (Btu/day·ton or Btu/day·lb)

**Respiration heat (at storage temperature):**

| Product | Storage Temp | Heat Generation (Btu/day·ton) |
|---------|--------------|-------------------------------|
| Apples | 32°F | 600-1,200 |
| Lettuce | 32°F | 5,000-8,000 |
| Broccoli | 32°F | 10,000-16,000 |
| Tomatoes (ripe) | 50°F | 3,000-4,000 |
| Potatoes | 40°F | 800-1,200 |
| Carrots | 32°F | 2,000-3,000 |

**Important:** Respiration increases exponentially with temperature (Q₁₀ ≈ 2-3)

**Rate at higher temperature:**

$$q_{resp,T2} = q_{resp,T1} \times Q_{10}^{(T_2-T_1)/10}$$

Where $Q_{10}$ = temperature coefficient (typically 2.0-2.5)

## Infiltration Load

### Air Exchange Load

**Heat gain from outdoor air entering space:**

$$Q_{inf} = V \cdot \rho \cdot c_p \cdot (T_{out} - T_{in}) \cdot N_{ACH}$$

Or using simplified form:

$$Q_{inf,sensible} = 1.08 \cdot CFM \cdot \Delta T$$

$$Q_{inf,latent} = 4840 \cdot CFM \cdot \Delta W$$

Where:
- $CFM$ = infiltration airflow rate
- $\Delta T$ = temperature difference (°F)
- $\Delta W$ = humidity ratio difference (lb/lb)

**Infiltration air changes per day:**

| Space | Air Changes per Day |
|-------|---------------------|
| Well-sealed cooler, low traffic | 1-2 |
| Average cooler | 3-5 |
| High-traffic cooler | 8-15 |
| Well-sealed freezer | 0.5-1.5 |
| Average freezer | 2-4 |

**Infiltration through door openings (Gosney-Olama equation):**

$$CFM_{door} = K \cdot A_{door} \cdot \rho_{avg} \cdot \sqrt{H \cdot (1 - \frac{\rho_{in}}{\rho_{out}})} \cdot F_{usage}$$

Where:
- $K$ = flow coefficient (0.6-0.8)
- $A_{door}$ = door opening area (ft²)
- $H$ = door height (ft)
- $\rho_{in}, \rho_{out}$ = air density inside/outside (lb/ft³)
- $F_{usage}$ = usage factor (door open fraction of time)

**Mitigation:**
- Air curtains (reduce infiltration 60-80%)
- Strip curtains (reduce 50-70%)
- Vestibules/airlocks
- High-speed doors (minimize open time)

## Equipment and People Loads

### Internal Equipment

**Typical heat gains:**

| Equipment | Heat Gain |
|-----------|-----------|
| Evaporator fan motors | 2,545 Btu/hr per hp |
| Lighting (LED) | 3.4 Btu/hr per watt |
| Lighting (fluorescent) | 4.1 Btu/hr per watt |
| Electric forklift (during use) | 8,000-12,000 Btu/hr |
| Electric forklift (charging) | All input power (100% heat) |
| Conveyor motors | 2,545 Btu/hr per hp |

**Forklift load calculation:**

$$Q_{forklift} = N \cdot P \cdot U \cdot 2,545$$

Where:
- $N$ = number of forklifts
- $P$ = motor power (hp)
- $U$ = usage factor (0.2-0.4 typical)

### People Load

**Heat gain per person:**

| Space Temperature | Sensible (Btu/hr) | Latent (Btu/hr) | Total (Btu/hr) |
|-------------------|-------------------|-----------------|----------------|
| 50°F | 640 | 140 | 780 |
| 40°F | 730 | 120 | 850 |
| 0°F (freezer) | 920 | 80 | 1,000 |
| -20°F | 1,050 | 50 | 1,100 |

**Occupancy diversity:** Average number, not peak (use time-weighted average)

## Safety Factors and Design Margins

**Refrigeration load safety factors:**

1. **Equipment capacity:** Add 10-20% to calculated load
   - Uncertainty in usage patterns: 10%
   - Future expansion: 10-20%
   - Equipment degradation over time: 5-10%

2. **Pull-down load:** Additional capacity for initial cool-down
   - Empty room: 2-3 × steady-state transmission load
   - With product: Calculate pull-down time requirement

3. **Peak vs. average load:**
   - Design for peak load, not annual average
   - Consider seasonal variations (higher summer transmission)

**Avoid over-sizing:**
- Excessive capacity → short cycling → poor humidity control
- Target: equipment runs 16-20 hr/day at design conditions

## Complete Load Calculation Example

<div class="worked-example">
<h3>Worked Example 2: Walk-In Cooler Load Calculation</h3>

**Given:**
- Cooler size: 20 ft × 30 ft × 12 ft high
- Wall/ceiling U-value: 0.05 Btu/hr·ft²·°F
- Floor (uninsulated): 0.15 Btu/hr·ft²·°F
- Indoor temperature: 35°F
- Outdoor temperature: 95°F (summer design day)
- Product: 5,000 lb apples per day (70°F → 35°F)
- Apple specific heat: 0.90 Btu/lb·°F
- Apple respiration: 1,000 Btu/day·ton (at 35°F)
- Infiltration: 4 air changes per day
- Evaporator fans: 2 × 1/2 hp
- Lighting: 400 watts, 8 hr/day
- People: 2 workers, 4 hr/day average

**Find:** Total refrigeration load

**Solution:**

**1. Transmission load:**

Wall area: $2 \times (20 + 30) \times 12 = 1,200$ ft²
Ceiling area: $20 \times 30 = 600$ ft²
Floor area: $20 \times 30 = 600$ ft²

Walls + ceiling:
$$Q_{walls} = 0.05 \times (1,200 + 600) \times (95 - 35) = 5,400 \text{ Btu/hr}$$

Floor:
$$Q_{floor} = 0.15 \times 600 \times (70 - 35) = 3,150 \text{ Btu/hr}$$

Total transmission: **8,550 Btu/hr**

**2. Product load:**

Daily product: 5,000 lb/day

$$Q_{prod} = \frac{5,000 \times 0.90 \times (70 - 35)}{24} = 6,563 \text{ Btu/hr}$$

**3. Respiration load:**

Product mass: 5,000 lb = 2.5 tons

$$Q_{resp} = \frac{2.5 \times 1,000}{24} = 104 \text{ Btu/hr}$$

**4. Infiltration load:**

Room volume: $20 \times 30 \times 12 = 7,200$ ft³

Infiltration rate: $\frac{7,200 \times 4}{24 \times 60} = 20$ CFM average

Sensible: $Q_{inf,s} = 1.08 \times 20 \times (95 - 35) = 1,296$ Btu/hr

Latent (summer 75°F, 60% RH, W=0.0114 vs 35°F sat, W=0.0037):
$Q_{inf,l} = 4840 \times 20 \times (0.0114 - 0.0037) = 746$ Btu/hr

Total infiltration: **2,042 Btu/hr**

**5. Equipment load:**

Evaporator fans: $2 \times 0.5 \times 2,545 = 2,545$ Btu/hr (continuous)

Lighting: $400 \times 3.4 \times \frac{8}{24} = 453$ Btu/hr (average)

Equipment total: **2,998 Btu/hr**

**6. People load:**

People: $2 \times 850 \times \frac{4}{24} = 283$ Btu/hr (average)

**7. Total load:**

$$Q_{total} = 8,550 + 6,563 + 104 + 2,042 + 2,998 + 283 = 20,540 \text{ Btu/hr}$$

**8. Safety factor (15%):**

$$Q_{design} = 20,540 \times 1.15 = 23,621 \text{ Btu/hr} = 1.97 \text{ tons}$$

**Select equipment:** 2.5 ton condensing unit (next standard size)

**Answer:** Design load: 23,621 Btu/hr (1.97 tons); Select 2.5 ton unit

**Load breakdown:**
- Transmission: 42%
- Product: 32%
- Equipment: 15%
- Infiltration: 10%
- People: 1%

</div>

---

**Related Technical Guides:**
- [Material Thermal Properties](/technical-guides/material-thermal-properties/)
- [Food Storage Requirements](/technical-guides/food-storage-requirements/)
- [Vapor Compression Refrigeration](/technical-guides/vapor-compression-refrigeration/)
- [Compressor Selection & Performance](/technical-guides/compressor-selection-performance/)
- [Cold Storage Facility Design](/technical-guides/cold-storage-facility-design/)

**References:**
- ASHRAE Refrigeration Handbook, Chapter 24: Refrigeration Load Calculations
- ASHRAE Refrigeration Handbook, Chapter 19: Thermal Properties of Foods
- ASHRAE Fundamentals Handbook, Chapter 14: Climatic Design Information
- Stoecker, W.F., "Industrial Refrigeration Handbook"
- USDA: The Commercial Storage of Fruits, Vegetables, and Florist and Nursery Stocks
