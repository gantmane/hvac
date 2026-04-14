---
title: "Air Leakage Moisture Transport"
aliases: ["Air Leakage Moisture Transport"]
description: "Technical analysis of air leakage as primary moisture transport mechanism in building envelopes, including stack effect, infiltration rates, air barrier continuity, blower door testing, and moisture load calculations for HVAC system design."
weight: 3
---

Air leakage represents the dominant mechanism for moisture transport through building envelopes, typically moving 100 to 1,000 times more moisture than vapor diffusion alone. Understanding air leakage pathways, driving forces, and control strategies is critical for HVAC system design, humidity control, and prevention of moisture-related building failures.

## Air Leakage vs. Vapor Diffusion

The relative importance of air leakage compared to vapor diffusion as a moisture transport mechanism:

| Transport Mechanism | Moisture Transfer Rate | Driving Force | Control Strategy |
|---------------------|------------------------|---------------|------------------|
| Air leakage | 50-500 g/m²·day (typical) | Pressure differential | Air barrier continuity |
| Vapor diffusion | 0.5-5 g/m²·day (typical) | Vapor pressure gradient | Vapor retarder placement |
| Ratio (leakage/diffusion) | 100:1 to 1000:1 | Varies with conditions | Air barrier priority |

### Quantitative Comparison

For a typical wall assembly with a 1 mm crack per linear meter of wall:

**Air leakage moisture transport:**
- Pressure differential: 4 Pa (0.016 in. w.c.)
- Air velocity through crack: 2.5 m/s (492 fpm)
- Airflow rate: 0.0025 m³/s per meter (5.3 cfm/ft)
- Indoor conditions: 21°C (70°F), 40% RH, 7.4 g/kg moisture content
- Outdoor conditions: -18°C (0°F), 60% RH, 0.6 g/kg moisture content
- Moisture transport rate: **230 g/day per meter of crack**

**Vapor diffusion moisture transport:**
- Same wall assembly without air leakage
- Same temperature and humidity conditions
- Typical wall permeance: 50 ng/(Pa·s·m²)
- Vapor pressure differential: 540 Pa
- Moisture transport rate: **2.3 g/day per square meter**

The air leakage through a 1 mm crack per meter of wall transports as much moisture as vapor diffusion through 100 m² of wall surface.

## Driving Forces for Air Leakage

Three primary mechanisms create pressure differentials that drive air leakage through building envelope discontinuities:

### Stack Effect

Stack effect pressure differential calculation:

ΔP_stack = C_s × h × ΔT

Where:
- ΔP_stack = Stack pressure differential (Pa)
- C_s = Stack coefficient = 0.0342 Pa/(m·K) at sea level
- h = Height above neutral pressure plane (m)
- ΔT = Indoor-outdoor temperature difference (K)

**Example calculation for 20-story building:**
- Building height: 60 m (197 ft)
- Indoor temperature: 21°C (70°F)
- Outdoor temperature: -18°C (0°F)
- ΔT = 39 K
- Neutral pressure plane at mid-height: 30 m

Pressure at top of building:
ΔP_top = 0.0342 × 30 × 39 = **40 Pa (0.16 in. w.c.) outward**

Pressure at bottom of building:
ΔP_bottom = -0.0342 × 30 × 39 = **-40 Pa (0.16 in. w.c.) inward**

### Wind-Driven Infiltration

Wind pressure on building surfaces:

ΔP_wind = 0.5 × ρ × C_p × V²

Where:
- ΔP_wind = Wind-induced pressure (Pa)
- ρ = Air density (kg/m³), typically 1.2 kg/m³
- C_p = Pressure coefficient (dimensionless), varies by surface orientation
- V = Wind velocity (m/s)

**Typical pressure coefficients:**

| Surface Location | C_p Value | Pressure Character |
|------------------|-----------|-------------------|
| Windward wall | +0.6 to +0.8 | Positive (inward) |
| Leeward wall | -0.3 to -0.5 | Negative (outward) |
| Side walls | -0.6 to -0.7 | Negative (outward) |
| Roof center | -0.7 to -0.9 | Negative (outward) |
| Roof corners/edges | -1.2 to -2.0 | Strong negative (outward) |

**Example wind pressure calculation:**
- Wind velocity: 10 m/s (22 mph)
- Windward wall: C_p = +0.7
- ΔP_wind = 0.5 × 1.2 × 0.7 × 10² = **42 Pa (0.17 in. w.c.)**

### Mechanical System Pressurization

HVAC systems create building pressurization through imbalanced supply and exhaust airflows:

ΔP_mech = (Q_supply - Q_exhaust) / C_leak

Where:
- ΔP_mech = Mechanical pressurization (Pa)
- Q_supply = Total supply airflow (m³/s)
- Q_exhaust = Total exhaust airflow (m³/s)
- C_leak = Building leakage coefficient (m³/(s·Pa^n))

Typical intentional building pressurization targets:

| Building Type | Pressurization | Purpose |
|---------------|----------------|---------|
| Hospital patient rooms | -2.5 Pa (-0.01 in. w.c.) | Infection control |
| Hospital operating rooms | +2.5 to +8 Pa (+0.01 to +0.03 in. w.c.) | Contamination prevention |
| Laboratory chemical storage | -12 to -25 Pa (-0.05 to -0.10 in. w.c.) | Containment |
| Clean rooms (ISO 5-7) | +5 to +15 Pa (+0.02 to +0.06 in. w.c.) | Particle control |
| Commercial buildings | +2.5 to +7.5 Pa (+0.01 to +0.03 in. w.c.) | Infiltration control |

## Air Barrier Systems

An effective air barrier system requires continuity across all six surfaces of the building envelope with proper transitions at penetrations and intersections.

### Air Barrier Continuity Requirements

Critical air barrier transition details:

1. **Wall-to-roof transitions**
   - Continuous membrane or sealed joint
   - Accommodate differential movement
   - Typical gap before sealing: 6-25 mm (1/4 to 1 in.)

2. **Wall-to-foundation transitions**
   - Below-grade waterproofing integration
   - Capillary break consideration
   - Thermal bridge mitigation

3. **Window and door perimeters**
   - AAMA 711 sealant installation standards
   - Backer rod sizing: 1.25 × joint width
   - Sealant depth: 0.5 × joint width (minimum 6 mm)

4. **Mechanical, electrical, plumbing penetrations**
   - Sleeve-to-air barrier sealing
   - Service core pressurization control
   - Expansion/contraction accommodation

5. **Building expansion joints**
   - Flexible air barrier materials
   - Movement capacity: ±25% minimum
   - UV resistance for exposed locations

### Air Barrier Material Performance Criteria

**ASHRAE 90.1 air barrier assembly requirements:**

| Performance Metric | Maximum Value | Test Standard |
|-------------------|---------------|---------------|
| Air permeance | 0.02 L/(s·m²) at 75 Pa | ASTM E2178 |
| Air leakage (assemblies) | 0.20 L/(s·m²) at 75 Pa | ASTM E2357, E1677, E283 |
| Air leakage (whole building) | 2.0 L/(s·m²) at 75 Pa | ASTM E779 (pressurization) |

Conversion: 0.02 L/(s·m²) at 75 Pa = 0.004 cfm/ft² at 0.3 in. w.c.

**Common air barrier material assemblies:**

| Assembly Type | Air Permeance | Installation Considerations |
|---------------|---------------|----------------------------|
| Self-adhered membrane | 0.001-0.005 L/(s·m²) | Temperature-dependent adhesion |
| Fluid-applied membrane | 0.002-0.008 L/(s·m²) | Wet mil thickness critical |
| Mechanically fastened membrane | 0.005-0.015 L/(s·m²) | Seam overlap and fastener sealing |
| Spray polyurethane foam (SPF) | 0.001-0.003 L/(s·m²) | Minimum 25 mm (1 in.) thickness |
| Exterior gypsum sheathing + sealed joints | 0.01-0.02 L/(s·m²) | Joint sealant longevity concern |
| CMU fully grouted + parged | 0.015-0.025 L/(s·m²) | Block core verification required |

## Blower Door Testing

Blower door testing quantifies whole-building air leakage by measuring airflow required to maintain specific pressure differentials.

### Test Procedure

Standard test protocol per ASTM E779:

1. **Building preparation:**
   - Close all exterior doors and windows
   - Close all interior doors (single-zone test)
   - Close fireplace dampers
   - Disable HVAC systems or seal supply/return registers
   - Record indoor/outdoor temperature and barometric pressure

2. **Pressure testing sequence:**
   - Establish baseline pressure (HVAC off)
   - Create pressure differentials: 10, 15, 20, 25, 30, 40, 50, 60, 75 Pa
   - Measure airflow at each pressure step
   - Perform both pressurization and depressurization tests
   - Average results to minimize wind effects

3. **Data analysis:**
   - Plot airflow vs. pressure on log-log scale
   - Determine power law relationship: Q = C × ΔP^n
   - Calculate equivalent leakage area (ELA)
   - Normalize results to building envelope area

### Air Changes Per Hour at 50 Pa (ACH50)

ACH50 = (Q_50 × 3600) / V_building

Where:
- ACH50 = Air changes per hour at 50 Pa (h⁻¹)
- Q_50 = Airflow rate at 50 Pa (m³/s)
- V_building = Building volume (m³)
- 3600 = Conversion factor (seconds per hour)

**Typical ACH50 values by construction type:**

| Construction Type | ACH50 Range | Air Leakage Rate | Envelope Quality |
|-------------------|-------------|------------------|------------------|
| Passive House | 0.3-0.6 | 0.05-0.10 cfm/ft² @ 50 Pa | Exceptional |
| High-performance | 0.6-1.5 | 0.10-0.25 cfm/ft² @ 50 Pa | Excellent |
| Code-compliant new (2018+) | 1.5-3.0 | 0.25-0.50 cfm/ft² @ 50 Pa | Good |
| Standard new construction | 3.0-5.0 | 0.50-0.85 cfm/ft² @ 50 Pa | Average |
| Existing buildings (pre-2000) | 5.0-15.0 | 0.85-2.50 cfm/ft² @ 50 Pa | Poor |
| Unrenovated historic | 15.0-30.0+ | 2.50-5.00+ cfm/ft² @ 50 Pa | Very poor |

### Converting ACH50 to Natural Infiltration

Natural infiltration rate estimation from ACH50:

ACH_natural = ACH50 / N

Where N is the "LBL factor" or "N-factor":

| Climate/Shielding | N-Factor | Description |
|-------------------|----------|-------------|
| Tight, well-sealed house | 25-30 | Minimal stack effect, sheltered |
| Average construction | 18-22 | Moderate exposure |
| Leaky construction | 12-16 | High exposure, significant height |
| Very leaky, exposed | 8-12 | Multi-story, windy site |

**Example:**
- ACH50 = 3.0 (code-compliant construction)
- N-factor = 20 (average conditions)
- ACH_natural = 3.0 / 20 = **0.15 ACH** (natural infiltration)

## Moisture Load from Air Leakage

Calculating moisture load on HVAC systems from envelope air leakage:

m_moisture = ρ × Q_leak × Δω × 3600

Where:
- m_moisture = Moisture load (kg/h)
- ρ = Air density (kg/m³), typically 1.2 kg/m³
- Q_leak = Leakage airflow rate (m³/s)
- Δω = Humidity ratio difference (kg_water/kg_air)
- 3600 = Conversion factor (seconds per hour)

**Example moisture load calculation:**

Building parameters:
- Floor area: 5,000 m² (53,820 ft²)
- Envelope area: 6,500 m² (69,965 ft²)
- Volume: 15,000 m³ (529,720 ft³)
- ACH50: 2.5 (good construction)
- Estimated natural infiltration: 2.5 / 20 = 0.125 ACH

Winter conditions:
- Indoor: 21°C, 40% RH, ω = 0.0062 kg/kg
- Outdoor: -10°C, 70% RH, ω = 0.0013 kg/kg
- Δω = 0.0049 kg/kg

Infiltration airflow:
Q_leak = (0.125 × 15,000) / 3600 = 0.521 m³/s (1,103 cfm)

Moisture removal load:
m_moisture = 1.2 × 0.521 × 0.0049 × 3600 = **11.0 kg/h (24.3 lb/h)**

This moisture load must be added to internal moisture generation when sizing dehumidification capacity.

## ASHRAE 90.1 Air Barrier Requirements

ASHRAE Standard 90.1 Energy Standard for Buildings establishes mandatory air barrier requirements for the building thermal envelope.

### Continuous Air Barrier Requirement

**Section 5.4.3.1 - Continuous Air Barrier:**

Buildings in climate zones 4-8 (and marine climate zone 3) require a continuous air barrier for the building thermal envelope. The air barrier must be continuous across:
- Building envelope assemblies (walls, roofs, floors)
- Joints and assemblies
- Penetrations of the building envelope
- Transitions in materials, assemblies, and building elements

### Performance Testing Requirements

**Verification options (choose one):**

1. **Materials approach:** Use materials/assemblies tested per:
   - ASTM E2178 (materials): ≤0.02 L/(s·m²) at 75 Pa
   - ASTM E2357 (assemblies): ≤0.20 L/(s·m²) at 75 Pa

2. **Whole building approach:** Test completed building per:
   - ASTM E779 or E1827: ≤2.0 L/(s·m²) at 75 Pa
   - Based on building envelope surface area

### Climate Zone Requirements

| Climate Zone | Air Barrier Required | Typical Infiltration Target |
|--------------|---------------------|----------------------------|
| 1 (Very Hot) | No (recommended) | Not specified |
| 2 (Hot) | No (recommended) | Not specified |
| 3 (Warm) | Marine only | ≤0.25 cfm/ft² @ 75 Pa |
| 4 (Mixed) | Yes | ≤0.25 cfm/ft² @ 75 Pa |
| 5 (Cool) | Yes | ≤0.20 cfm/ft² @ 75 Pa |
| 6 (Cold) | Yes | ≤0.20 cfm/ft² @ 75 Pa |
| 7 (Very Cold) | Yes | ≤0.15 cfm/ft² @ 75 Pa |
| 8 (Subarctic) | Yes | ≤0.15 cfm/ft² @ 75 Pa |

Note: More stringent local codes may apply (e.g., IECC, California Title 24).

## Common Air Leakage Pathways

Identifying and addressing typical leakage locations:

| Leakage Location | Typical % of Total | Mitigation Strategy |
|------------------|-------------------|---------------------|
| Window/door perimeters | 15-25% | Continuous perimeter sealant, integrated flashing |
| Wall-to-roof intersection | 10-20% | Sealed transition membrane, rigid blocking |
| Wall-to-foundation | 8-15% | Sill gasket, spray foam, sealed membrane |
| Service penetrations (MEP) | 10-18% | Sleeve sealing, penetration boots, fire-rated sealants |
| Electrical outlets/switches | 5-12% | Air barrier gaskets, sealed boxes |
| HVAC duct penetrations | 8-15% | Duct mastic at penetrations, sealed sleeves |
| Attic access hatches | 3-8% | Weatherstripping, insulated covers |
| Recessed lighting | 5-10% | IC-rated, airtight fixtures (ASTM E283) |
| Plumbing chases/soffits | 5-12% | Chase sealing, compartmentalization |
| Building expansion joints | 3-8% | Flexible air barrier assemblies |

### Sequential Air Sealing Priority

For maximum cost-effectiveness, address air leakage in this order:

1. Large, accessible penetrations (duct/pipe penetrations)
2. Wall-to-roof and wall-to-foundation transitions
3. Window and door perimeters
4. Service chases and plumbing penetrations
5. Electrical penetrations
6. Small distributed leaks (switches, outlets)

## Impact on HVAC System Design

Air leakage significantly affects multiple HVAC design parameters:

### Heating and Cooling Load Implications

Infiltration sensible load:
Q_sensible = ρ × Q × c_p × ΔT / 1000

Where:
- Q_sensible = Sensible heating/cooling load (kW)
- ρ = Air density (1.2 kg/m³)
- Q = Infiltration airflow rate (m³/s)
- c_p = Specific heat of air (1.006 kJ/(kg·K))
- ΔT = Temperature difference (K)

Infiltration latent load:
Q_latent = ρ × Q × Δω × h_fg / 1000

Where:
- Q_latent = Latent cooling load (kW)
- Δω = Humidity ratio difference (kg/kg)
- h_fg = Latent heat of vaporization (2,501 kJ/kg at 0°C)

**Example load comparison (5,000 m² building):**

| Envelope Tightness | ACH_natural | Infiltration (m³/s) | Winter Heating (kW) | Summer Sensible (kW) | Summer Latent (kW) |
|-------------------|-------------|---------------------|---------------------|----------------------|-------------------|
| Passive House (0.4 ACH50) | 0.02 | 0.083 | 3.1 | 1.8 | 0.9 |
| Excellent (1.5 ACH50) | 0.075 | 0.313 | 11.6 | 6.9 | 3.4 |
| Code minimum (3.0 ACH50) | 0.15 | 0.625 | 23.1 | 13.8 | 6.8 |
| Average existing (7.0 ACH50) | 0.35 | 1.458 | 53.9 | 32.1 | 15.8 |

Assumptions: Winter ΔT = 35 K, Summer ΔT = 12 K, Summer Δω = 0.008 kg/kg

### Humidity Control Challenges

High infiltration rates create humidity control difficulties:

**Winter humidification requirements:**
- Tight building (0.15 ACH): 8-12 kg/h humidification capacity
- Leaky building (0.35 ACH): 18-28 kg/h humidification capacity
- Increased first cost and operating energy

**Summer dehumidification challenges:**
- Latent load from infiltration can exceed internal gains
- Requires proper equipment selection (low sensible heat ratio)
- May necessitate dedicated dehumidification systems
- Envelope improvement often more cost-effective than mechanical oversizing

### Pressurization Control Strategies

For buildings requiring specific pressurization:

1. **Pressure-independent flow control:** Use airflow measuring stations to maintain supply-exhaust differential regardless of envelope leakage

2. **Building pressure sensors:** Direct pressure measurement with relief damper modulation for precision control (±1 Pa)

3. **Envelope tightening:** Reduce C_leak to minimize airflow required for target pressurization, reducing energy consumption

4. **Vestibule design:** Create pressure buffer zones at building entries to minimize pressure fluctuations during door operation

Reducing building air leakage from 5.0 ACH50 to 1.5 ACH50 can decrease pressurization airflow requirements by 60-70%, resulting in substantial fan energy savings and improved pressure control stability.

