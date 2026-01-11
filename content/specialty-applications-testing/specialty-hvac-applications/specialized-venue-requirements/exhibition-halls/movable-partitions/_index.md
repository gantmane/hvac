---
title: "HVAC Coordination with Movable Partitions"
description: "Engineering principles for HVAC system design in spaces with movable partitions. Zone boundary management, air distribution flexibility, and acoustical separation strategies."
keywords: ["movable partitions HVAC", "operable walls air distribution", "zone boundary control", "airwall integration", "flexible space conditioning", "partition acoustics", "reconfigurable zones", "exhibition hall flexibility"]
weight: 2
---

Movable partitions in exhibition halls create dynamic boundary conditions that challenge traditional HVAC design assumptions. The system must maintain thermal comfort, acoustical separation, and air quality regardless of partition configuration while avoiding cross-contamination between zones.

## Physical Principles of Partition-HVAC Interaction

Movable partitions introduce variable boundary conditions that affect three coupled transport phenomena:

**Heat Transfer Across Partition Boundaries**

Thermal resistance through partitions depends on construction and airgap configuration. For typical airwall partitions:

$$R_{partition} = \frac{1}{h_i} + \sum \frac{L_i}{k_i} + \frac{1}{h_o}$$

where $h_i$ and $h_o$ are interior and exterior convection coefficients (typically 8-10 W/m²·K for still air), $L_i$ are material thicknesses, and $k_i$ are thermal conductivities.

The U-factor for quality airwall systems ranges from 0.3-0.6 W/m²·K, requiring consideration of inter-zone heat transfer in load calculations.

**Pressure Boundary Integrity**

Maintaining pressure differentials across partitions prevents acoustical crosstalk through the plenum. The pressure difference required to overcome partition leakage:

$$\Delta P = C \cdot Q^n$$

where $C$ is the flow coefficient (dependent on partition seal quality), $Q$ is volumetric airflow through leaks, and $n$ is the flow exponent (0.5 for turbulent flow, 0.65-1.0 for laminar flow through tight seals).

**Acoustical Transmission Paths**

Sound transmission occurs through three mechanisms:
1. Direct transmission through partition mass (governed by mass law)
2. Flanking transmission via ceiling plenum
3. Duct-borne transmission between zones

## Air Distribution Strategies for Flexible Spaces

### Supply Air Placement Relative to Partitions

The grid spacing of supply outlets must accommodate all partition configurations. Critical design parameter:

$$S_{max} = \frac{X}{throw}$$

where $S_{max}$ is maximum outlet spacing, $X$ is partition grid spacing, and throw is measured to terminal velocity (50 fpm for occupied zones per ASHRAE Standard 55).

| Partition Grid | Recommended Outlet Spacing | Diffuser Type | Throw Requirement |
|----------------|---------------------------|---------------|-------------------|
| 3.05 m (10 ft) | 2.4-2.7 m (8-9 ft) | 4-way | 3.7 m (12 ft) at 50 fpm |
| 6.1 m (20 ft) | 4.6-5.5 m (15-18 ft) | Perforated | 6.1 m (20 ft) at 50 fpm |
| 9.15 m (30 ft) | 6.1-7.6 m (20-25 ft) | Linear slot | 9.1 m (30 ft) at 50 fpm |

**Diffuser Selection Criteria:**

- Use wide-angle diffusers (4-way or perforated) to minimize throw distance requirements
- Avoid high-velocity induction diffusers that create noise and drafts near partitions
- Specify low NC ratings (NC 30-35) for acoustically sensitive configurations

### Return Air Configuration Options

Three fundamental approaches address return air flexibility:

```mermaid
graph TD
    A[Return Air Strategy] --> B[Ducted Return Per Zone]
    A --> C[Common Plenum Return]
    A --> D[Hybrid Transfer/Ducted]

    B --> B1[Highest Acoustical Separation]
    B --> B2[STC Loss: 0-3 dB]
    B --> B3[Complexity: High]

    C --> C1[Lowest Cost]
    C --> C2[STC Loss: 15-25 dB]
    C --> C3[Requires Baffles]

    D --> D1[Balanced Performance]
    D --> D2[STC Loss: 5-10 dB]
    D --> D3[Transfer Grilles + Dedicated Returns]
</graph>
```

**Ducted Return Per Zone**

Individual return ducts for each partition configuration eliminate plenum crosstalk. Return grille placement:

- Locate returns opposite supply outlets for proper air circulation
- Minimum 1.5 m (5 ft) from partition tracks to avoid "dead zones"
- Size for 300-400 fpm face velocity to minimize noise generation

**Common Plenum Return with Baffles**

Acoustical baffles in the plenum space reduce flanking transmission. Required baffle insertion loss:

$$IL_{required} = STC_{partition} - STC_{system} + 5$$

where $IL_{required}$ is insertion loss in dB, $STC_{partition}$ is partition rating, and $STC_{system}$ is target system performance. The 5 dB factor accounts for uncertainty.

## Zone Boundary Management

### Pressure Control Strategies

Maintaining neutral or slight positive pressure in each zone prevents inter-zone contamination:

$$Q_{supply} - Q_{return} = Q_{exfiltration}$$

For adjacent zones with partition closed:

$$\Delta P_{zone} = \frac{\rho}{2} \left( \frac{Q_{net}}{C_d A_{leak}} \right)^2$$

where $\rho$ is air density, $C_d$ is discharge coefficient (0.6-0.65 for partition seals), and $A_{leak}$ is effective leakage area.

Target pressure differentials:
- Adjacent zones (partition closed): 0-2.5 Pa (0-0.01 in. w.g.)
- Combined space: < 1 Pa to minimize door forces per ASHRAE 62.1

### Sensor Placement for Reconfigurable Zones

Temperature and air quality sensors must provide accurate control for all configurations:

**Placement Strategy:**

1. Install sensors on permanent walls, not near partition tracks
2. Use averaging algorithms when multiple sensors serve one zone
3. Locate sensors 1.2-1.8 m (4-6 ft) above floor, away from supply air streams
4. Minimum one sensor per potential zone configuration

**Control Logic for Variable Zones:**

```mermaid
flowchart LR
    A[Partition Position Sensors] --> B{Configuration Detection}
    B --> C[Zone 1 Only]
    B --> D[Zone 2 Only]
    B --> E[Combined Space]

    C --> F[VAV-1 Active, VAV-2 Minimum]
    D --> G[VAV-2 Active, VAV-1 Minimum]
    E --> H[Both VAVs Active, Averaging Control]

    F --> I[Zone Temp Control]
    G --> I
    H --> I
</flowchart>
```

## Acoustical Separation Requirements

ASHRAE Standard 189.1 recommends minimum STC 50 for partition assemblies in conference spaces. The HVAC system must not degrade this rating by more than 5 dB.

**Critical Design Elements:**

| Component | STC Impact | Mitigation Strategy |
|-----------|-----------|---------------------|
| Plenum leakage | -15 to -25 dB | Lined baffles, separate returns |
| Duct transmission | -10 to -15 dB | Duct silencers between zones |
| Terminal unit noise | -5 to -10 dB | Locate VAVs away from partition lines |
| Diffuser noise | -3 to -8 dB | Low-velocity diffusers (NC 30-35) |

### Duct Silencer Sizing

For critical acoustical applications, silencer insertion loss requirement:

$$IL = NC_{source} - NC_{target} + 10 \log_{10}\left(\frac{A_{room}}{\alpha \cdot S}\right)$$

where $A_{room}$ is room absorption, $\alpha$ is average absorption coefficient, and $S$ is room surface area. The logarithmic term accounts for room effect (typically 5-10 dB).

## Airflow Balance and Commissioning

Verify system performance for all partition configurations:

1. **Baseline Test:** Measure airflows with partitions fully open
2. **Individual Zone Test:** Close each partition and verify:
   - Supply airflow meets design (±10%)
   - Return airflow maintains pressure balance
   - Temperature control responds within 15 minutes
3. **Acoustical Verification:** Generate pink noise at 85 dBA in one zone, measure NIC (Noise Isolation Class) in adjacent zone
4. **Pressure Mapping:** Confirm pressure differentials < 2.5 Pa between closed zones

## Design Recommendations

**Critical Success Factors:**

- Coordinate diffuser grid with partition track layout during design development
- Specify partition position sensors integrated with BAS for automatic zone reconfiguration
- Provide separate return paths or properly baffled plenum returns for STC > 45 requirements
- Calculate inter-zone heat transfer using actual partition U-factors, not adiabatic assumptions
- Commission all partition configurations, not just fully open and fully closed states

**Common Failure Modes to Avoid:**

- Supply outlets located on partition track lines create "dead zones" in some configurations
- Insufficient return air capacity when spaces combine creates negative pressure and door operation problems
- Thermostats mounted on movable partition tracks lose power connection
- Undersized duct silencers provide inadequate insertion loss at low frequencies (125-250 Hz)

These principles ensure flexible HVAC performance that maintains comfort, acoustical privacy, and energy efficiency across all spatial configurations.
