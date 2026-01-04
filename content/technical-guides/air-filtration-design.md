---
title: "Air Filtration Design for HVAC Engineers"
description: "MERV ratings, pressure drop calculations, filter sizing, and service life estimation for particle and gaseous contaminant control."
keywords: ["air filtration", "MERV rating", "filter pressure drop", "filter sizing", "HEPA filter", "carbon filter"]
author: "Evgeniy Gantman"
date: 2026-01-04
weight: 23
---

# Air Filtration Design for HVAC Engineers

Filtration protects occupants from particulates, extends equipment life, and maintains indoor air quality. Proper filter selection balances capture efficiency, pressure drop, and cost.

## MERV Ratings

**Minimum Efficiency Reporting Value (ASHRAE 52.2):**

| MERV | Particle Size | Typical Application |
|------|--------------|---------------------|
| 1-4 | > 10 μm | Residential panel filters (poor) |
| 5-8 | 3-10 μm | Standard commercial (pollen, dust) |
| 9-12 | 1-3 μm | Better commercial (mold spores, vehicle emissions) |
| 13-16 | 0.3-1 μm | Hospital, labs (bacteria, tobacco smoke) |
| 17-20 | < 0.3 μm | HEPA (viruses, surgical suites, cleanrooms) |

**Common selections:**
- Office: MERV 8-11
- School: MERV 11-13
- Hospital: MERV 14-15 + HEPA in critical areas
- Cleanroom: HEPA (MERV 17-20)

## Filter Pressure Drop

**Clean filter:**

$$\Delta P_{clean} = 0.1 - 0.8 \text{ "w.g.}$$

(Higher MERV = higher pressure drop)

**Dirty filter (replace when):**

$$\Delta P_{dirty} = 2 \times \Delta P_{clean}$$ (typically 1.0-1.5 "w.g.)

**Pressure drop increases exponentially as dust loads**

**Energy cost of pressure drop:**

$$Cost = \frac{CFM \times \Delta P \times hours \times \$/kWh}{6,356 \times \eta_{fan}}$$

## Filter Sizing

**Face velocity:**

$$v_f = \frac{CFM}{A_{filter}}$$

**Typical face velocities:**
- Pleated filters (MERV 8-13): 300-500 FPM
- HEPA filters: 250-300 FPM
- Bag filters: 400-600 FPM

**Lower face velocity:**
- Reduces pressure drop
- Increases filter life
- Requires larger filter bank (higher first cost)

## Filter Service Life

**Dust holding capacity:** Grams of synthetic dust per filter area

**Service life estimation:**

$$t_{service} = \frac{Capacity_{grams}}{Dust_{loading,g/h}}$$

**Typical service life:**
- MERV 8 pleated: 3-6 months
- MERV 13 pleated: 6-12 months
- HEPA: 1-3 years

**Replacement triggers:**
- Pressure drop exceeds limit
- Time-based schedule
- Visual inspection (if accessible)

## Gaseous Filtration

**Activated carbon:**
- Removes odors, VOCs
- Does NOT remove particles
- Pressure drop: 0.2-0.5 "w.g.
- Service life: 6-24 months (depends on contaminant concentration)

**Potassium permanganate:**
- Removes odors, ethylene (food storage)

## Filtration System Design

**Two-stage filtration (common):**
1. **Pre-filter (MERV 8):** Captures large particles, protects final filter
2. **Final filter (MERV 13-16):** Fine particle removal

**Benefits of two-stage:**
- Extends final filter life
- Lower overall pressure drop
- Better protection

**HEPA filter bank design:**
- Scan test ports (verify no bypass)
- Gel-sealed frames
- Bag-in-bag-out for hazardous materials

## Practical Applications

1. **ASHRAE 62.1 compliance:** MERV 6 minimum (13 recommended)
2. **Energy code (90.1):** Consider pressure drop in fan power budget
3. **Wildfire smoke:** Upgrade to MERV 13+ during events

---

**Related Technical Guides:**
- [Ventilation Rate Calculations](/technical-guides/ventilation-rate-calculations/)
- [Indoor Air Quality Management](/technical-guides/indoor-air-quality-management/)
- [Fan Selection & Performance](/technical-guides/fan-selection-performance/)

**References:**
- ASHRAE Standard 52.2: Method of Testing General Ventilation Air-Cleaning Devices for Removal Efficiency by Particle Size
- ASHRAE Handbook of HVAC Systems and Equipment, Chapter 29: Air Cleaners for Particulate Contaminants
- NAFA Guide to Air Filtration, 5th Edition
