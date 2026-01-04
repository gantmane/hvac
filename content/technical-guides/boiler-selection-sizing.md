---
title: "Boiler Selection & Sizing for HVAC Engineers"
description: "Fire-tube, water-tube, and condensing boiler types with efficiency calculations, turndown ratio analysis, and sequencing strategies for optimal performance."
keywords: ["boiler sizing", "boiler efficiency", "condensing boiler", "fire-tube boiler", "boiler turndown", "combustion efficiency"]
author: "Evgeniy Gantman"
date: 2026-01-04
weight: 8
---

# Boiler Selection & Sizing for HVAC Engineers

Boiler selection impacts energy costs, reliability, and system control. Proper sizing and type selection optimize efficiency while meeting load requirements across all operating conditions.

## Boiler Types

### Fire-Tube Boilers

Hot combustion gases flow through tubes surrounded by water.

**Characteristics:**
- Capacity: up to 25,000 lb/h steam or 25 MMBtu/h hot water
- Pressure: typically < 150 psig
- Efficiency: 75-84% (non-condensing)
- Advantages: Simple, low cost, compact
- Disadvantages: Slower response, thermal shock sensitivity

### Water-Tube Boilers

Water flows through tubes surrounded by hot combustion gases.

**Characteristics:**
- Capacity: 10,000 - 500,000+ lb/h steam
- Pressure: up to 1,500+ psig
- Efficiency: 80-85% (non-condensing)
- Advantages: High capacity, high pressure capable, fast response
- Disadvantages: Higher cost, larger footprint

### Condensing Boilers

Recovers latent heat from flue gas condensation.

**Efficiency:** 90-99% (HHV basis)

**Key requirement:** Return water temperature < 130°F for condensing

**Applications:** Low-temperature systems (radiant floor, baseboard), outdoor reset control

## Boiler Sizing

**Heating load:**

$$Q_{boiler} = \frac{Q_{design}}{n_{boilers} - 1} \times SF$$

Where:
- $Q_{design}$ = design heating load (Btu/h)
- $n_{boilers}$ = number of boilers
- $SF$ = safety factor (typically 1.15-1.25)

**Piping loss allowance:** Add 10-15% for distribution losses

**Pickup allowance:** Historical practice (20-30%) no longer recommended for modern systems

## Efficiency Metrics

**Combustion Efficiency:**

$$\eta_{comb} = 100 - \%_{loss,dry} - \%_{loss,moisture}$$

**AFUE** (Annual Fuel Utilization Efficiency):
Seasonal efficiency including cycling losses, jacket losses.

**Thermal Efficiency:**

$$\eta_{thermal} = \frac{Q_{output}}{Q_{input}} \times 100\%$$

## Turndown Ratio

Ratio of maximum to minimum firing rate.

$$Turndown = \frac{Q_{max}}{Q_{min}}$$

**Typical values:**
- Single-stage: 1:1 (on/off only)
- Two-stage: 2:1 or 3:1
- Modulating: 5:1 to 10:1
- Condensing: 10:1 to 20:1

**Benefits of high turndown:**
- Better part-load efficiency
- Reduced cycling
- Improved comfort

## Practical Applications

1. **Multiple boilers:** Size for N+1 redundancy
2. **Lead-lag control:** Sequence boilers based on load
3. **Outdoor reset:** Lower supply temperature when outdoor temperature rises (10-20% energy savings)

---

**Related Technical Guides:**
- [Heating Load Calculations](/technical-guides/heating-load-calculations/)
- [Combustion Analysis](/technical-guides/combustion-analysis/)
- [Hydronic System Fundamentals](/technical-guides/hydronic-system-fundamentals/)

**References:**
- ASHRAE Handbook of HVAC Systems and Equipment, Chapter 32: Boilers
- ASME Boiler and Pressure Vessel Code
