---
title: "Wind Energy Integration"
description: "Advanced wind energy systems for HVAC applications including turbine fundamentals, power calculations, building-integrated wind turbines, small wind systems, site assessment methodology, grid integration strategies, and load matching for commercial and industrial buildings"
weight: 3
---

Wind energy represents a viable renewable power source for HVAC systems in appropriate locations with sufficient wind resources. While less universally applicable than solar photovoltaics, wind turbines can provide significant energy offsets for buildings with favorable wind exposure, particularly in coastal, elevated, or open terrain sites.

## Wind Power Fundamentals

### Power in Wind

The kinetic power available in moving air is described by:

P_wind = (1/2) × ρ × A × v³

Where:
- P_wind = Power in wind stream (W)
- ρ = Air density (kg/m³)
- A = Swept area of turbine (m²)
- v = Wind velocity (m/s)

Standard air density at sea level and 15°C is 1.225 kg/m³. This decreases with altitude and increases with lower temperature according to:

ρ = (P × M) / (R × T)

Where:
- P = Atmospheric pressure (Pa)
- M = Molar mass of air (0.02897 kg/mol)
- R = Universal gas constant (8.314 J/(mol·K))
- T = Absolute temperature (K)

The cubic relationship between power and velocity is critical: doubling wind speed increases available power by a factor of eight.

### Betz Limit

No wind turbine can extract all kinetic energy from the wind stream. The theoretical maximum efficiency (Betz limit) is:

η_Betz = 16/27 ≈ 0.593

This represents 59.3% of the available wind power. Practical turbines achieve:
- Large utility-scale turbines: 45-50% peak efficiency
- Small building-scale turbines: 25-40% peak efficiency
- Building-integrated turbines: 15-30% peak efficiency

### Turbine Power Output

Actual turbine power output is:

P_turbine = (1/2) × ρ × A × v³ × C_p × η_mech × η_elec

Where:
- C_p = Power coefficient (dimensionless, ≤ 0.593)
- η_mech = Mechanical drivetrain efficiency (0.90-0.98)
- η_elec = Electrical generator efficiency (0.85-0.95)

For a horizontal-axis wind turbine, the swept area is:

A = π × R²

Where R is the blade radius (m).

### Wind Speed Distribution

Wind speeds follow a Weibull probability distribution:

f(v) = (k/c) × (v/c)^(k-1) × e^(-(v/c)^k)

Where:
- k = Shape parameter (typically 1.5-3.0)
- c = Scale parameter (m/s)
- v = Wind speed (m/s)

The Rayleigh distribution is a special case with k = 2:

f(v) = (π/2) × (v/v̄²) × e^(-(π/4)(v/v̄)²)

Where v̄ is the mean wind speed.

## Building-Integrated Wind Turbines

### Architectural Integration

Building-integrated wind energy (BIWE) systems mount turbines on or within building structures. Common configurations include:

| Location | Advantages | Disadvantages | Typical Application |
|----------|------------|---------------|---------------------|
| Rooftop corners | Accelerated wind flow | Turbulence, structural loads | Commercial buildings |
| Building gaps | Venturi effect amplification | Limited placement, noise | High-rise complexes |
| Parapet mounting | Architectural integration | Lower wind speeds | Low/mid-rise buildings |
| Facade integration | Distributed generation | Very low efficiency | Experimental applications |

### Wind Flow Acceleration

Buildings can accelerate wind flow through several mechanisms:

**Corner Effect**: Wind velocity at building corners increases by 20-40% due to flow acceleration around edges.

**Augmentation Factor** (AF):

AF = v_accelerated / v_freestream

Typical values:
- Flat rooftop center: 1.0-1.1
- Rooftop edge: 1.2-1.4
- Building corners: 1.3-1.6
- Venturi gaps: 1.5-2.5

Since power varies with v³, a 50% velocity increase (AF = 1.5) yields 3.375 times the power output.

### Structural Considerations

Wind turbine mounting requires structural analysis for:

**Static Loads**:
- Turbine dead load: 50-500 kg depending on size
- Foundation/mounting system: 100-1000 kg

**Dynamic Loads**:
- Thrust force: F_thrust = (1/2) × ρ × A × v² × C_T
- Gyroscopic loads from rotor rotation
- Vibration transmission (5-20 Hz typical)

**Wind Load Combinations**: IBC requires load combinations including turbine-specific wind loads added to building wind loads.

Vibration isolation using spring mounts or elastomeric pads is essential:

f_n = (1/2π) × √(k/m)

Where:
- f_n = Natural frequency (Hz)
- k = Spring stiffness (N/m)
- m = Turbine mass (kg)

Isolation frequency should be less than 0.5 times the minimum turbine operating frequency.

## Small Wind Turbines for Buildings

### Size Classifications

| Class | Rotor Diameter | Rated Power | Swept Area | Application |
|-------|----------------|-------------|------------|-------------|
| Micro | 0.5-1.5 m | 50-500 W | 0.2-1.8 m² | Signage, monitoring |
| Mini | 1.5-3.5 m | 500-3 kW | 1.8-9.6 m² | Small commercial |
| Small | 3.5-7.0 m | 3-20 kW | 9.6-38.5 m² | Medium commercial |
| Medium | 7.0-15 m | 20-100 kW | 38.5-177 m² | Large commercial |

### Horizontal vs. Vertical Axis

**Horizontal Axis Wind Turbines (HAWT)**:

Advantages:
- Higher efficiency (30-45% vs. 15-35%)
- Mature technology with established performance
- Better high-wind performance

Disadvantages:
- Directional sensitivity (requires yaw mechanism)
- Higher tip speeds (noise generation)
- Greater gyroscopic loads

**Vertical Axis Wind Turbines (VAWT)**:

Advantages:
- Omnidirectional (no yaw required)
- Lower acoustic signature
- Generator at ground level (easier maintenance)
- Better performance in turbulent flow

Disadvantages:
- Lower peak efficiency
- Higher starting wind speed requirements
- More complex structural dynamics

Common VAWT types:
- Savonius: Drag-based, C_p = 0.15-0.25, excellent starting torque
- Darrieus: Lift-based, C_p = 0.30-0.40, requires starting assistance
- Helical Darrieus: Reduced vibration, C_p = 0.25-0.38

### Power Curves

Turbine performance is characterized by the power curve, which relates output power to wind speed:

| Wind Speed (m/s) | Power Output (% rated) | Operating State |
|------------------|------------------------|-----------------|
| < 2.5 | 0% | Below cut-in |
| 2.5-3.5 | 5-15% | Starting region |
| 3.5-8.0 | 15-85% | Linear region |
| 8.0-12.0 | 85-100% | Rated power region |
| 12.0-25.0 | 100% | Constant power (pitch/stall control) |
| > 25.0 | 0% | Cut-out (safety shutdown) |

**Cut-in speed**: Minimum wind speed for power generation (typically 2.5-4.0 m/s)

**Rated speed**: Wind speed at which rated power is reached (typically 10-14 m/s)

**Cut-out speed**: Maximum safe operating wind speed (typically 20-30 m/s)

### Annual Energy Production

Annual energy production (AEP) integrates the power curve with the wind speed distribution:

AEP = Σ [P(v_i) × f(v_i) × Δv × 8760]

Where:
- P(v_i) = Power output at wind speed bin i (kW)
- f(v_i) = Probability of wind speed bin i
- Δv = Wind speed bin width (typically 0.5 or 1.0 m/s)
- 8760 = Hours per year

Capacity factor (CF) expresses turbine utilization:

CF = AEP / (P_rated × 8760)

Typical capacity factors:
- Excellent sites (coastal, elevated): 25-35%
- Good sites (rural, open terrain): 15-25%
- Moderate sites (suburban): 8-15%
- Poor sites (urban, sheltered): < 8%

## Site Assessment Methodology

### Wind Resource Evaluation

**Wind Shear and Height Correction**:

Wind speed increases with height above ground according to the power law:

v_2 = v_1 × (h_2/h_1)^α

Where:
- v_1, v_2 = Wind speeds at heights h_1, h_2 (m/s)
- h_1, h_2 = Heights above ground (m)
- α = Wind shear exponent (dimensionless)

Typical wind shear exponents:

| Surface Roughness | α Value | Description |
|-------------------|---------|-------------|
| Water, ice | 0.10 | Very smooth |
| Short grass, airport | 0.14 | Open terrain |
| High grass, crops | 0.16 | Agricultural |
| Scattered trees | 0.20 | Rural |
| Suburban residential | 0.25 | Moderate obstacles |
| Urban areas | 0.30-0.40 | Dense obstacles |

Alternative logarithmic profile:

v_2 = v_1 × [ln(h_2/z_0) / ln(h_1/z_0)]

Where z_0 is the surface roughness length (m).

### Measurement Requirements

Wind resource assessment requires:

**Minimum Measurement Period**: 1 year to capture seasonal variations

**Optimal Duration**: 2-3 years to reduce uncertainty

**Measurement Height**: Should match or exceed planned turbine hub height

**Data Collection Frequency**: 10-minute averages (standard for wind energy)

**Parameters to Record**:
- Wind speed (m/s) - primary parameter
- Wind direction (degrees) - for siting and turbine orientation
- Temperature (°C) - for air density correction
- Barometric pressure (kPa) - for air density correction
- Standard deviation of wind speed - turbulence indicator

### Turbulence Assessment

Turbulence intensity (TI) affects turbine performance and longevity:

TI = σ_v / v̄

Where:
- σ_v = Standard deviation of wind speed (m/s)
- v̄ = Mean wind speed (m/s)

IEC 61400-2 turbulence categories for small wind turbines:

| Category | TI at 15 m/s | Site Description |
|----------|--------------|------------------|
| A | 0.18 | High turbulence (urban) |
| B | 0.16 | Medium turbulence (rural) |
| C | 0.14 | Low turbulence (offshore) |

Building-mounted turbines typically experience Category A conditions (TI = 0.20-0.30).

High turbulence:
- Reduces power output by 10-30%
- Increases mechanical wear
- Raises maintenance requirements
- May require turbine derating

### Obstacle Assessment

Obstacles affect wind flow at distances up to:

Distance = 20 × H_obstacle

Where H_obstacle is obstacle height.

**Minimum Clearances**:
- Horizontal: 2-3 times obstacle height
- Vertical: 10 m above obstacles within 100 m radius
- Recommended: 15-20 m above obstacles for optimal performance

**Computational Fluid Dynamics (CFD)** modeling is recommended for complex urban sites to predict:
- Wind speed distribution
- Turbulence patterns
- Flow acceleration zones
- Wake effects from adjacent buildings

## Power Output Calculations

### Example: Small Commercial Building

**Site Parameters**:
- Location: Coastal commercial building, Boston, MA
- Mean wind speed at 10 m: 6.5 m/s (measured)
- Hub height: 15 m
- Surface roughness: Suburban (α = 0.25)

**Step 1: Height Correction**

v_15m = 6.5 × (15/10)^0.25 = 6.5 × 1.107 = 7.2 m/s

**Step 2: Turbine Selection**

Selected turbine:
- Rated power: 10 kW
- Rotor diameter: 5.5 m (swept area = 23.8 m²)
- Cut-in: 3.0 m/s
- Rated speed: 12.0 m/s
- Cut-out: 25.0 m/s

**Step 3: Air Density Correction**

At site conditions (elevation 5 m, mean temp 11°C):
- P = 101,300 Pa
- T = 284 K

ρ = (101,300 × 0.02897) / (8.314 × 284) = 1.243 kg/m³

Density ratio: 1.243 / 1.225 = 1.015 (1.5% increase from standard)

**Step 4: Annual Energy Production**

Using Rayleigh distribution with mean 7.2 m/s and integrating with turbine power curve:

AEP = 28,500 kWh/year

Capacity factor: 28,500 / (10 × 8760) = 32.5% (excellent for small turbine)

**Step 5: HVAC Load Matching**

Building HVAC annual consumption: 125,000 kWh/year

Wind energy offset: 28,500 / 125,000 = 22.8%

Monthly production varies significantly:

| Month | Mean Wind Speed | Production (kWh) | HVAC Load (kWh) | Match Factor |
|-------|-----------------|------------------|-----------------|--------------|
| Jan | 8.5 m/s | 3,200 | 12,500 | 0.26 |
| Feb | 8.2 m/s | 2,650 | 11,000 | 0.24 |
| Mar | 7.8 m/s | 2,850 | 10,200 | 0.28 |
| Apr | 7.2 m/s | 2,400 | 8,500 | 0.28 |
| May | 6.5 m/s | 2,100 | 7,200 | 0.29 |
| Jun | 5.8 m/s | 1,650 | 9,800 | 0.17 |
| Jul | 5.5 m/s | 1,550 | 11,200 | 0.14 |
| Aug | 5.6 m/s | 1,600 | 10,800 | 0.15 |
| Sep | 6.2 m/s | 1,850 | 8,900 | 0.21 |
| Oct | 6.8 m/s | 2,250 | 8,200 | 0.27 |
| Nov | 7.5 m/s | 2,500 | 9,500 | 0.26 |
| Dec | 8.1 m/s | 2,900 | 11,800 | 0.25 |

Note: Wind production peaks in winter when HVAC heating loads are highest, providing favorable load matching in heating-dominated climates.

## Grid Integration

### Electrical Configuration

**Grid-Connected Systems**:

Components:
- Wind turbine with integrated or external generator
- Rectifier (for AC generators): Converts variable frequency AC to DC
- Inverter: Converts DC to grid-synchronized AC
- Disconnect switches: Manual and automatic isolation
- Protection relays: Over/under voltage, frequency, islanding
- Metering: Production and consumption monitoring

Inverter requirements per IEEE 1547:
- Voltage regulation: ±5% of nominal
- Power factor: 0.95 leading to 0.95 lagging
- Harmonic distortion: < 5% THD
- Frequency tolerance: ±0.5 Hz
- Anti-islanding: Disconnect within 2 seconds

**Battery-Hybrid Systems**:

Adding battery storage improves:
- Load matching from 15-25% to 40-65%
- Power quality and stability
- Backup power capability
- Peak demand reduction

Battery sizing for 50% wind energy utilization:

E_battery = (P_turbine_avg × t_storage) / DOD

Where:
- E_battery = Battery capacity (kWh)
- P_turbine_avg = Average turbine output (kW)
- t_storage = Storage duration (hours)
- DOD = Depth of discharge limit (0.80 for Li-ion, 0.50 for lead-acid)

Example: 10 kW turbine, 3-hour storage, Li-ion:

E_battery = (3.5 × 3) / 0.80 = 13.1 kWh

### Net Metering and Grid Export

Net metering policies affect economic viability:

**Full Retail Rate Net Metering**:
- Exported kWh credited at retail rate
- Most favorable for wind systems
- Annual or monthly reconciliation

**Avoided Cost Net Metering**:
- Export compensated at utility's wholesale cost
- Typically 30-50% of retail rate
- Reduces wind system economics significantly

**Time-of-Use (TOU) Net Metering**:
- Export value varies by time
- Wind generation often occurs during off-peak periods
- May reduce effective value by 15-30%

### Power Quality Considerations

Wind turbines introduce grid interactions:

**Voltage Fluctuations**: Rapid wind speed changes cause output variations

Flicker severity factor: P_st = K × (N_10min)^0.31 × ψ_k

Where:
- N_10min = Number of voltage changes in 10 minutes
- ψ_k = Voltage change factor
- K = System constant

Mitigation:
- Power factor correction (capacitor banks or STATCOM)
- Voltage regulators at service entrance
- Battery storage for output smoothing

**Harmonic Distortion**: Inverter switching generates harmonics

Total harmonic distortion (THD):

THD = √(Σ V_h²) / V_fundamental

Modern inverters maintain THD < 3% through:
- High switching frequencies (20-50 kHz)
- Advanced filtering (LC or LCL filters)
- Digital control algorithms

## HVAC Load Matching

### Temporal Correlation

Wind-HVAC load correlation varies by climate:

**Heating-Dominated Climates** (Northern US, Canada):
- Strong positive correlation
- Winter wind production aligns with heating demand
- Correlation coefficient: 0.45-0.65
- Load matching factor: 35-55%

**Cooling-Dominated Climates** (Southern US):
- Weak or negative correlation
- Peak cooling demand in calm summer conditions
- Correlation coefficient: 0.10-0.25
- Load matching factor: 15-25%

**Mixed Climates**:
- Moderate correlation
- Seasonal variability
- Correlation coefficient: 0.25-0.45
- Load matching factor: 25-40%

Load matching factor (LMF):

LMF = Σ min(P_wind(t), P_HVAC(t)) / Σ P_wind(t)

Where:
- P_wind(t) = Wind production at time t
- P_HVAC(t) = HVAC consumption at time t

### Demand Response Integration

Wind-integrated HVAC systems benefit from demand response strategies:

**Thermal Storage Charging**:
- Ice storage charging during high wind periods
- Chilled water storage for cooling systems
- Hot water storage for heating systems
- Increases wind utilization by 20-40%

**Temperature Setpoint Modulation**:
- Widen deadband during low wind production
- Pre-cool or pre-heat during high wind production
- Typical adjustment: ±2°C from setpoint

**Load Shifting Control Logic**:

```
IF (P_wind > P_HVAC_base) THEN
    Enable thermal storage charging
    Activate non-critical loads
    Reduce setpoint tolerance (tighter comfort)
ELSE IF (P_wind < P_HVAC_base × 0.5) THEN
    Disable thermal storage charging
    Shed non-critical loads
    Increase setpoint tolerance (wider comfort range)
END IF
```

### Economic Analysis

**Levelized Cost of Energy (LCOE)**:

LCOE = (C_capital × CRF + C_O&M_annual) / AEP

Where:
- C_capital = Initial capital cost ($)
- CRF = Capital recovery factor
- C_O&M_annual = Annual operations and maintenance cost ($/year)
- AEP = Annual energy production (kWh/year)

Capital recovery factor:

CRF = [r × (1+r)^n] / [(1+r)^n - 1]

Where:
- r = Discount rate (typically 0.06-0.10)
- n = System lifetime (years)

**Small Wind System Costs** (2025):

| Component | Cost per kW | Installation | Total |
|-----------|-------------|--------------|-------|
| Turbine (< 20 kW) | $3,500-5,500 | $1,500-2,500 | $5,000-8,000 |
| Turbine (20-100 kW) | $2,800-4,200 | $1,200-2,000 | $4,000-6,200 |
| Inverter/Controls | $800-1,200 | $400-600 | $1,200-1,800 |
| Structural/Tower | $1,000-2,500 | $800-1,500 | $1,800-4,000 |
| Electrical | $400-800 | $600-1,200 | $1,000-2,000 |

Total installed cost: $8,000-18,000 per kW (small systems < 20 kW)

**Operations and Maintenance**:
- Annual O&M: 2-4% of capital cost
- Major overhaul: Years 10-15, approximately 15-25% of capital
- Expected lifetime: 20-25 years

**Example Economic Analysis**:

10 kW system:
- Installed cost: $95,000
- Annual O&M: $2,850 (3% of capital)
- AEP: 28,500 kWh/year
- Discount rate: 8%
- Lifetime: 20 years

CRF = [0.08 × 1.08^20] / [1.08^20 - 1] = 0.1019

LCOE = (95,000 × 0.1019 + 2,850) / 28,500 = $0.439/kWh

Compare to retail electricity rate ($0.18-0.35/kWh) and consider:
- Incentives: Federal ITC (30% through 2032)
- State rebates: $0.50-2.00 per watt in some states
- Accelerated depreciation: MACRS 5-year for commercial
- REC sales: $0.01-0.05/kWh in some markets

After 30% ITC:

LCOE = (66,500 × 0.1019 + 2,850) / 28,500 = $0.338/kWh

Simple payback (with incentives, $0.22/kWh electricity rate):

Payback = 66,500 / [(28,500 × 0.22) - 2,850] = 17.8 years

## System Design Considerations

### Turbine Placement Optimization

**Setback Requirements**:
- Property line: 1.1-1.5 × (hub height + rotor radius)
- Buildings: 1.5-2.0 × turbine height
- Power lines: 1.5 × (turbine height + rotor radius)

**Multiple Turbine Spacing**:
- Perpendicular to prevailing wind: 3-5 rotor diameters
- Parallel to prevailing wind: 8-12 rotor diameters

Wake losses from upstream turbines:

P_loss = 0.15 to 0.30 × P_rated

for spacing of 5-8 diameters downwind.

### Safety and Code Compliance

**Standards and Codes**:
- IEC 61400-2: Small wind turbine design requirements
- AWEA 9.1: Small wind turbine performance and safety standard
- ASCE 7: Wind load calculations
- NEC Article 694: Small wind electric systems
- IEEE 1547: Interconnection requirements

**Safety Systems**:
- Overspeed protection: Mechanical brake and/or aerodynamic control
- Lightning protection: Grounding system per NFPA 780
- Tower climbing safety: Fall protection for towers > 4 m
- Aviation marking: FAA notification for systems > 61 m AGL

### Acoustic Considerations

Sound pressure level at distance d:

SPL_d = SPL_source - 20 × log₁₀(d/d_ref) - α × (d - d_ref)

Where:
- SPL_d = Sound level at distance d (dB(A))
- SPL_source = Source sound level (dB(A))
- d_ref = Reference distance (typically 10 m)
- α = Atmospheric absorption (0.005 dB/m at 1000 Hz)

Small turbine sound levels:
- Source level (10 m): 45-55 dB(A)
- Level at 50 m: 35-45 dB(A)
- Level at 100 m: 30-38 dB(A)

Typical noise ordinances require:
- Residential zones: 45-55 dB(A) at property line
- Commercial zones: 55-65 dB(A) at property line

## Emerging Technologies

### Building-Scale Innovations

**Ducted Turbines**:
- Diffuser-augmented wind turbines (DAWT)
- Power augmentation: 30-80% over bare turbine
- Reduced acoustic signature
- Higher cost per kW

**Micro-Turbine Arrays**:
- Multiple small units (< 1 kW each)
- Distributed mounting on building facade
- Total capacity: 5-20 kW for commercial building
- Challenges: Complexity, maintenance access

**Adaptive Geometry**:
- Variable pitch blades for optimal C_p
- Morphing airfoils for turbulence adaptation
- Active flow control using plasma actuators

### Smart Integration

**Predictive Control**:
- Wind forecasting (1-24 hour ahead)
- Optimal storage charge/discharge scheduling
- Preemptive load shifting
- Energy market participation

**Machine Learning Applications**:
- Turbine performance optimization
- Predictive maintenance
- Fault detection and diagnosis
- Adaptive control parameter tuning

**Virtual Power Plant (VPP) Participation**:
- Aggregate multiple small wind systems
- Grid services provision
- Enhanced revenue streams
- Requires sophisticated control and communication

## Practical Implementation Guidelines

### Project Development Sequence

1. **Preliminary Assessment** (1-2 weeks):
   - Review available wind data
   - Evaluate site obstacles and constraints
   - Estimate rough energy production
   - Determine regulatory requirements

2. **Detailed Resource Assessment** (12-24 months):
   - Install meteorological tower
   - Collect site-specific wind data
   - Analyze seasonal patterns
   - Calculate expected AEP

3. **Feasibility Analysis** (1-2 months):
   - Turbine selection
   - Economic modeling
   - Incentive qualification
   - Preliminary design

4. **Permitting** (2-6 months):
   - Zoning approval
   - Building permit
   - Electrical permit
   - Utility interconnection agreement

5. **Design and Engineering** (2-3 months):
   - Structural analysis
   - Electrical design
   - Control system specification
   - Construction documents

6. **Installation** (1-3 weeks):
   - Foundation construction
   - Tower erection
   - Turbine installation
   - Electrical connection

7. **Commissioning** (1-2 weeks):
   - System testing
   - Performance verification
   - Safety checks
   - Operations training

### Risk Mitigation

**Technical Risks**:
- Underperforming wind resource: Minimize through thorough assessment
- Turbulence damage: Select appropriate turbine class
- Structural issues: Comprehensive engineering analysis
- Grid interconnection delays: Early utility coordination

**Financial Risks**:
- Cost overruns: Detailed design and contingency (15-20%)
- Incentive changes: Lock in rates before construction
- Performance shortfall: Conservative energy estimates
- O&M higher than expected: Service contracts and warranties

**Regulatory Risks**:
- Zoning denial: Early neighborhood consultation
- Permit delays: Parallel processing where possible
- Noise complaints: Acoustic analysis and setbacks
- Interconnection rejection: Pre-application utility meeting

Wind energy integration with HVAC systems offers significant potential in appropriate locations but requires careful technical analysis, realistic performance expectations, and thorough risk evaluation. The cubic relationship between wind speed and power output makes site selection critical, with even modest improvements in wind resource yielding substantial energy gains. Building-integrated applications face additional challenges from turbulence and structural constraints but can leverage architectural wind acceleration effects. Economic viability depends heavily on incentives, electricity rates, and the correlation between wind availability and HVAC load patterns, with heating-dominated climates generally showing superior load matching compared to cooling-dominated regions.
