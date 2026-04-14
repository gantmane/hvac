---
title: "Infiltration Loads Methods"
aliases: ["Infiltration Loads Methods"]
description: "Advanced calculation methods for infiltration loads in refrigerated facilities including door opening frequency, air curtain effectiveness, strip curtains, vestibule design, Gosney-Olama equation, and infiltration reduction strategies for cold storage and freezer applications"
weight: 6
---

Infiltration through doorways represents one of the most significant and variable cooling loads in refrigerated facilities. Air exchange introduces both sensible and latent heat loads, with moisture deposition on evaporator coils creating additional operational challenges through increased defrost frequency and energy consumption.

## Door Opening Infiltration

### Basic Infiltration Equation

The sensible and latent heat transfer through an open doorway depends on the density difference between inside and outside air:

**Sensible Heat:**
```
Qs = 0.221 × A × h × ρo × Fm × (1 - E) × Δh_sensible
```

**Latent Heat:**
```
Ql = 0.221 × A × h × ρo × Fm × (1 - E) × Δh_latent
```

Where:
- Qs = sensible heat gain, Btu/h
- Ql = latent heat gain, Btu/h
- A = door area, ft²
- h = door height, ft
- ρo = density of outside air, lb/ft³
- Fm = density factor (flow rate multiplier)
- E = effectiveness of protective device (0 to 1.0)
- Δh_sensible = enthalpy difference (sensible), Btu/lb
- Δh_latent = enthalpy difference (latent), Btu/lb

### Density Factor (Fm)

The density factor accounts for the actual air exchange rate based on temperature difference:

**For temperatures above 0°F:**
```
Fm = 0.8 × (1 - ρi/ρo)^0.5
```

**For temperatures below 0°F:**
```
Fm = 1.1 × (1 - ρi/ρo)^0.5
```

Where:
- ρi = density of inside air, lb/ft³
- ρo = density of outside air, lb/ft³

| Temperature Difference (°F) | Density Factor (Fm) |
|----------------------------|---------------------|
| 20 | 0.18 |
| 40 | 0.26 |
| 60 | 0.32 |
| 80 | 0.37 |
| 100 | 0.41 |
| 120 | 0.45 |
| 140 | 0.48 |

### Door Opening Frequency Method

The total daily infiltration load depends on door usage patterns:

```
Q_total = Qs × t_open × n_openings / 24
```

Where:
- Q_total = average hourly load, Btu/h
- Qs = instantaneous infiltration load, Btu/h
- t_open = average door open time per opening, hours
- n_openings = number of door openings per day

**Typical Door Open Times:**

| Facility Type | Average Open Time (seconds) | Openings per Day |
|--------------|----------------------------|------------------|
| Small walk-in cooler | 10-15 | 50-100 |
| Large walk-in cooler | 15-30 | 100-200 |
| Distribution center dock door | 300-600 | 20-40 |
| Warehouse traffic door | 30-60 | 100-300 |
| Processing plant door | 60-180 | 40-80 |

### Traffic Door Usage Factor

For high-traffic doors, apply a usage factor to account for door efficiency:

```
Q_design = Q_infiltration × UF × DF
```

Where:
- UF = usage factor (1.0 to 1.5 for heavy traffic)
- DF = door factor (1.0 for manual, 0.8 for automatic, 0.6 for high-speed)

## Gosney-Olama Equation

The Gosney-Olama equation provides a more accurate prediction of infiltration flow rate through vertical openings based on pressure differential:

```
v = Cd × [2 × g × h × (ρo - ρi) / (ρo + ρi)]^0.5
```

Where:
- v = average air velocity through opening, ft/s
- Cd = discharge coefficient (typically 0.65 to 0.75)
- g = gravitational acceleration, 32.2 ft/s²
- h = height of opening, ft
- ρo, ρi = outside and inside air density, lb/ft³

**Volume Flow Rate:**

```
Q_volume = v × A × 3600 / 2
```

Where:
- Q_volume = volumetric flow rate, ft³/h
- A = opening area, ft²
- Factor of 2 accounts for bidirectional flow

**Mass Flow Rate:**

```
m_dot = Q_volume × ρ_avg / 60
```

Where:
- m_dot = mass flow rate, lb/min
- ρ_avg = (ρo + ρi) / 2

### Discharge Coefficient Values

| Opening Configuration | Discharge Coefficient (Cd) |
|----------------------|---------------------------|
| Unrestricted door opening | 0.70-0.75 |
| Door with threshold | 0.65-0.70 |
| Strip curtain (50% coverage) | 0.35-0.45 |
| Strip curtain (75% coverage) | 0.20-0.30 |
| Air curtain operating | 0.15-0.25 |
| Vestibule configuration | 0.10-0.20 |

## Air Curtain Effectiveness

Air curtains reduce infiltration by creating a high-velocity air stream across the door opening. Effectiveness depends on air velocity, width coverage, and temperature differential.

### Air Curtain Performance

**Effectiveness Factor:**

```
E = 1 - (Q_actual / Q_no_curtain)
```

Where:
- E = effectiveness (0 to 1.0)
- Q_actual = infiltration with air curtain, Btu/h
- Q_no_curtain = infiltration without protection, Btu/h

**Required Air Velocity:**

```
v_jet = K × [g × h × (ρo - ρi) / ρi]^0.5
```

Where:
- v_jet = air curtain discharge velocity, ft/s
- K = velocity factor (1.5 to 2.0 for adequate performance)
- Other terms as previously defined

### Air Curtain Design Parameters

| Application | Discharge Velocity (fpm) | Air Volume (cfm/ft width) | Effectiveness (E) |
|------------|-------------------------|--------------------------|-------------------|
| Cooler (35-40°F) | 800-1000 | 400-500 | 0.60-0.75 |
| Freezer (-10 to 0°F) | 1200-1500 | 600-800 | 0.50-0.65 |
| Cold storage (-20°F) | 1500-1800 | 800-1000 | 0.40-0.55 |
| Vestibule entrance | 600-800 | 300-400 | 0.70-0.85 |

**Recirculated Air Curtains:**

For non-heated air curtains (recirculating cold room air):

| Room Temperature (°F) | Discharge Temperature (°F) | Effectiveness Loss Factor |
|----------------------|---------------------------|--------------------------|
| 35 | 40-45 | 1.10 |
| 0 | 5-10 | 1.15 |
| -10 | -5 to 0 | 1.20 |
| -20 | -15 to -10 | 1.25 |

### Air Curtain Limitations

Air curtain effectiveness decreases with:
- Cross winds >200 fpm (reduce effectiveness by 20-40%)
- Height >10 ft (reduce effectiveness by 5% per additional foot)
- Width >12 ft (use multiple units for wider openings)
- Extended door open periods >5 minutes (effectiveness drops to 40-50%)

## Strip Curtain Systems

Flexible strip curtains provide a physical barrier while allowing personnel and equipment passage.

### Strip Curtain Infiltration Reduction

```
Q_strip = Q_open × (1 - η_strip) × F_overlap
```

Where:
- Q_strip = infiltration with strip curtain, Btu/h
- Q_open = infiltration with open door, Btu/h
- η_strip = strip curtain efficiency
- F_overlap = overlap factor (typically 1.0 to 1.2)

### Strip Curtain Efficiency

| Strip Configuration | Coverage (%) | Efficiency (η) | Effective Cd |
|--------------------|-------------|----------------|--------------|
| Standard 8" strips, 50% overlap | 90 | 0.60-0.70 | 0.35-0.40 |
| Standard 8" strips, 100% overlap | 95 | 0.70-0.80 | 0.25-0.30 |
| Wide 12" strips, 50% overlap | 92 | 0.65-0.75 | 0.30-0.35 |
| Wide 12" strips, 100% overlap | 97 | 0.75-0.85 | 0.20-0.25 |
| Insulated strips | 95 | 0.75-0.85 | 0.20-0.25 |
| Brush strips (edges only) | 30 | 0.20-0.30 | 0.60-0.65 |

### Strip Curtain Design Considerations

**Strip Width Selection:**

| Door Width | Recommended Strip Width | Number of Strips |
|-----------|------------------------|------------------|
| 3-4 ft | 8 in | 6-8 |
| 4-6 ft | 8-10 in | 8-12 |
| 6-10 ft | 10-12 in | 12-18 |
| 10-14 ft | 12 in | 18-24 |

**Overlap Configuration:**
- 50% overlap: strip spacing = 0.5 × strip width
- 100% overlap: strip spacing = 0.33 × strip width
- Edge strips: extend 6-8 inches beyond door frame

**Material Thickness:**

| Application Temperature | Strip Thickness | Material |
|------------------------|----------------|----------|
| Cooler (>32°F) | 0.08-0.12 in | Standard PVC |
| Light freezer (0-32°F) | 0.12-0.16 in | Low-temp PVC |
| Freezer (<0°F) | 0.16-0.20 in | Polar-grade PVC |
| High-traffic any temp | 0.16-0.20 in | Reinforced PVC |

## Vestibule Calculations

Vestibules create a buffer zone that significantly reduces direct infiltration between spaces.

### Two-Door Vestibule

The infiltration through a two-door vestibule system:

```
Q_vestibule = Q_single × F_vestibule
```

Where F_vestibule depends on door operation mode:

| Door Operation Mode | Vestibule Factor (F_vestibule) |
|--------------------|-------------------------------|
| One door always closed | 0.05-0.10 |
| Interlocked doors | 0.10-0.20 |
| Doors occasionally both open | 0.30-0.50 |
| High-speed traffic (no coordination) | 0.50-0.70 |

### Vestibule Volume and Mixing

**Minimum Vestibule Volume:**

```
V_min = Q_volume × t_cycle × SF
```

Where:
- V_min = minimum vestibule volume, ft³
- Q_volume = volumetric flow rate per opening, ft³/min
- t_cycle = door cycle time, min (typically 0.5-2.0 min)
- SF = safety factor (1.5 to 2.0)

**Mixing Factor:**

For partial air mixing in vestibule:

```
Q_actual = Q_theoretical × [1 - (1 - e^(-N))]
```

Where:
- N = number of air changes during door open period
- e = base of natural logarithm (2.718)

### Vestibule Design Requirements

| Facility Type | Minimum Depth (ft) | Width | Height | Volume per Door Width (ft³/ft) |
|--------------|-------------------|-------|--------|-------------------------------|
| Walk-in cooler | 4-6 | Door + 2 ft | 7-8 | 30-50 |
| Warehouse dock | 8-12 | Door + 3 ft | 10-14 | 100-150 |
| Distribution center | 10-15 | Door + 4 ft | 12-16 | 150-200 |
| Freezer entry | 6-10 | Door + 3 ft | 8-10 | 60-100 |

**Vestibule Conditioning:**

| Vestibule Temperature Strategy | Temperature Range | Energy Impact | Infiltration Reduction |
|-------------------------------|------------------|---------------|------------------------|
| Unconditioned | Outdoor temp | Minimal | 80-85% |
| Tempered (heated only) | 50-60°F | Low | 85-90% |
| Semi-conditioned | 60-70°F | Moderate | 90-95% |
| Fully conditioned | 70-75°F | High | 95-98% |

## Doorway Infiltration Combined Methods

Multiple protection methods can be combined for maximum effectiveness:

```
Q_combined = Q_open × (1 - E_air) × (1 - E_strip) × F_vestibule × F_operation
```

Where:
- E_air = air curtain effectiveness
- E_strip = strip curtain effectiveness
- F_vestibule = vestibule factor
- F_operation = operational factor (door management)

### Combined Protection Effectiveness

| Protection Combination | Overall Effectiveness | Typical Application |
|-----------------------|----------------------|---------------------|
| Air curtain only | 60-75% | Coolers, moderate traffic |
| Strip curtain only | 70-85% | Low-speed traffic |
| Air curtain + strip curtain | 85-92% | Freezers, high traffic |
| Vestibule + air curtain | 88-95% | Distribution centers |
| Vestibule + strip curtain | 90-94% | Cold storage |
| Full system (all three) | 95-98% | Critical low-temp storage |

## Infiltration Reduction Strategies

### Operational Controls

**Door Management:**

1. **Automatic door closers:** Reduce average open time by 30-50%
2. **High-speed doors:** Open/close in 3-5 seconds vs. 15-30 seconds
3. **Traffic scheduling:** Batch door openings reduces total open time
4. **Interlocked vestibule doors:** Prevents simultaneous opening

**High-Speed Door Performance:**

| Door Type | Open/Close Cycle (sec) | Infiltration Reduction vs. Standard |
|-----------|----------------------|-------------------------------------|
| Standard manual | 20-40 | Baseline (0%) |
| Standard powered | 15-25 | 20-30% |
| High-speed fabric | 3-6 | 70-85% |
| High-speed rigid | 5-8 | 65-80% |
| Ultra-high-speed | 2-4 | 80-90% |

### Design Strategies

**Pressure Control:**

Maintain slight positive pressure in spaces immediately adjacent to refrigerated areas:

```
ΔP = ρ × g × h × (To - Ti) / (Ti × 144)
```

Where:
- ΔP = pressure differential, in. w.g.
- ρ = air density, lb/ft³
- g = 32.2 ft/s²
- h = height, ft
- To, Ti = absolute temperatures, °R
- 144 converts lb/ft² to lb/in²

**Recommended Pressure Differentials:**

| Adjacent Space Configuration | Pressure Differential (in. w.g.) | Method |
|----------------------------|----------------------------------|--------|
| Cooler to ambient | +0.02 to +0.05 | Exhaust reduction |
| Freezer to cooler | 0 to +0.02 | Balanced or slight + |
| Loading dock to freezer | +0.05 to +0.08 | Supply air to dock |
| Corridor to refrigerated space | +0.03 to +0.05 | Corridor pressurization |

### Physical Barriers

**Threshold and Seals:**

| Seal Type | Infiltration Reduction | Installation Location |
|-----------|------------------------|----------------------|
| Bottom threshold seal | 5-10% | Door base |
| Edge gaskets | 8-12% | Door perimeter |
| Magnetic seals | 10-15% | Door edges (walk-ins) |
| Inflatable seals | 15-25% | Dock doors |
| Full perimeter system | 20-30% | All edges |

**Traffic Flow Management:**

```
n_effective = n_actual / F_batch
```

Where:
- n_effective = effective number of openings
- n_actual = actual number of openings
- F_batch = batching factor (1.0 for random, 0.3-0.7 for scheduled)

### Specialized Applications

**Blast Freezer Infiltration:**

For blast freezers with rapid air movement:

```
Q_blast = Q_standard × (1 + v_internal/500)
```

Where:
- Q_blast = adjusted infiltration load, Btu/h
- v_internal = internal air velocity, fpm
- 500 = normalization factor

**Cold Storage with Racking:**

Obstruction from racking systems near doors affects infiltration:

| Distance from Door (ft) | Rack Density | Flow Reduction Factor |
|------------------------|--------------|----------------------|
| 0-5 | High (>80% full) | 0.70-0.80 |
| 0-5 | Medium (50-80%) | 0.80-0.90 |
| 5-10 | High | 0.85-0.92 |
| 5-10 | Medium | 0.90-0.95 |
| >10 | Any | 0.95-1.00 |

## Load Calculation Example

**Problem:** Calculate the infiltration load for a freezer door at -10°F with outside conditions of 80°F DB, 67°F WB.

**Given:**
- Door: 8 ft wide × 10 ft high
- Average open time: 45 seconds per opening
- Frequency: 100 openings per day
- Protection: Strip curtain (80% efficiency)

**Solution:**

1. **Door area:** A = 8 × 10 = 80 ft²

2. **Air properties:**
   - Outside: ρo = 0.0735 lb/ft³, ho = 31.2 Btu/lb
   - Inside: ρi = 0.0877 lb/ft³, hi = -2.8 Btu/lb (at -10°F, ~90% RH)

3. **Density factor:**
   ```
   Fm = 1.1 × (1 - 0.0877/0.0735)^0.5 = 1.1 × 0.616 = 0.678
   ```

4. **Infiltration without protection:**
   ```
   Q = 0.221 × 80 × 10 × 0.0735 × 0.678 × (31.2 - (-2.8))
   Q = 0.221 × 80 × 10 × 0.0735 × 0.678 × 34.0
   Q = 3,065 Btu per door opening
   ```

5. **With strip curtain:**
   ```
   Q_actual = 3,065 × (1 - 0.80) = 613 Btu per opening
   ```

6. **Average hourly load:**
   ```
   Q_avg = 613 × 100 / 24 = 2,554 Btu/h
   ```

7. **Design load (with 25% safety factor):**
   ```
   Q_design = 2,554 × 1.25 = 3,193 Btu/h
   ```

## ASHRAE Handbook References

Detailed infiltration calculation methods are provided in:

- **ASHRAE Handbook—Refrigeration (2022)**, Chapter 13: Refrigerated-Facility Design
  - Section on Air Exchange and Infiltration
  - Door infiltration calculation procedures
  - Protection device effectiveness factors

- **ASHRAE Handbook—Fundamentals (2021)**, Chapter 16: Airflow Around Buildings
  - Stack effect calculations
  - Pressure differentials across openings

- **ASHRAE Handbook—HVAC Applications (2023)**, Chapter 51: Refrigerated-Facility Design
  - Practical infiltration load estimation
  - Traffic pattern analysis
  - Combined protection systems

## Design Recommendations

1. **Always use protective devices** on refrigerated space doorways—unprotected doors create excessive infiltration loads

2. **Select high-speed doors** for high-traffic applications (>50 openings/day)

3. **Combine protection methods** for freezer applications below 0°F—single methods rarely achieve adequate protection

4. **Install air curtains** with discharge velocity ≥1.5 times the theoretical infiltration velocity

5. **Maintain strip curtains** regularly—damaged or missing strips eliminate most protective benefit

6. **Size vestibules** for actual traffic patterns, not minimum code requirements

7. **Monitor door open time** with data logging to verify design assumptions and identify training opportunities

8. **Apply safety factors** of 1.15-1.30 for critical applications or uncertain usage patterns
