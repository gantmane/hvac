---
title: "Duct Traverse Procedures for Airflow Measurement"
aliases: ["Duct Traverse Procedures for Airflow Measurement"]
description: "Technical guide to pitot tube and hot-wire anemometer traverse methods including log-Tchebycheff and equal area point selection for accurate duct airflow measurement."
date: 2025-01-05
weight: 2
tags: ["duct traverse", "pitot tube", "airflow measurement", "log-Tchebycheff", "equal area method", "hot-wire anemometer", "ASHRAE fundamentals", "testing and balancing"]
keywords: ["duct traverse procedures", "pitot tube traverse", "log-Tchebycheff method", "equal area traverse", "airflow measurement", "velocity profile", "duct airflow testing", "hot-wire anemometer"]
---

# Duct Traverse Procedures for Airflow Measurement

Duct traverse procedures establish accurate methods for measuring airflow velocity profiles across duct cross-sections. These systematic measurement techniques form the foundation of air system testing and balancing, providing the data necessary to verify system performance and identify flow distribution issues.

## Traverse Location Requirements

Proper traverse location selection critically affects measurement accuracy. Position traverse stations in straight duct sections with fully developed flow:

**Minimum straight duct lengths:**
- **Upstream**: 7.5 equivalent diameters from elbows, transitions, or takeoffs
- **Downstream**: 3 equivalent diameters to next disturbance
- **Preferred**: 10-15 diameters upstream when possible

For rectangular ducts, calculate equivalent diameter:

$$D_e = 1.30 \frac{(ab)^{0.625}}{(a+b)^{0.25}}$$

where:
- $D_e$ = equivalent diameter (ft or m)
- $a$ = duct width (ft or m)
- $b$ = duct height (ft or m)

**Access requirements:**
- Traverse ports on opposite faces for two-plane measurement
- Ports perpendicular to each other
- Minimum 2-inch diameter holes with sealing plugs
- Safe access platform when required

## Log-Tchebycheff Point Selection Method

The log-Tchebycheff method positions traverse points to optimize measurement accuracy by accounting for the logarithmic velocity profile near duct walls. This method provides superior accuracy for turbulent flow conditions typical in HVAC systems.

**Point locations from wall** for N traverse points per diameter:

$$x_i = \frac{D}{2}\left(1 - \cos\left[\frac{(2i-1)\pi}{2N}\right]\right)$$

where:
- $x_i$ = distance from duct wall to measurement point $i$
- $D$ = duct diameter or dimension
- $N$ = number of traverse points
- $i$ = point number (1 to N)

**Standard point quantities:**
- Round ducts: 16-20 points (single plane) or 32-40 points (two planes)
- Rectangular ducts: 25-64 points depending on aspect ratio
- Small ducts (<12 inches): minimum 16 points

**Example calculation** for 10 points in a 24-inch duct:

For point 1: $x_1 = \frac{24}{2}\left(1 - \cos\left[\frac{(2\cdot1-1)\pi}{20}\right]\right) = 12(1 - 0.9877) = 0.148$ inches

Average velocity calculation:

$$V_{avg} = \frac{1}{N}\sum_{i=1}^{N}V_i$$

Volumetric flow rate:

$$Q = V_{avg} \times A$$

## Equal Area Method

The equal area method divides the duct cross-section into equal areas with measurement points at the centroid of each area. This approach provides consistent spatial sampling but may underweight near-wall regions.

**Rectangular duct division:**
- Divide cross-section into rectangular grids
- Minimum 25 equal areas (5×5 grid)
- Larger ducts: 36-64 areas (6×6 to 8×8 grids)

**Point location** for M×N grid:

$$x_i = \frac{(2i-1)a}{2M}, \quad y_j = \frac{(2j-1)b}{2N}$$

where:
- $M$ = number of divisions in width direction
- $N$ = number of divisions in height direction
- $i$, $j$ = grid position indices

**Round duct equal area:**
Divide into concentric annular rings of equal area. For $n$ rings:

$$r_k = R\sqrt{\frac{k}{n}}$$

where $r_k$ is the outer radius of ring $k$, and $R$ is the duct radius.

Measure at the center of each annular area.

## Pitot Tube Traverse

Pitot tubes measure velocity pressure by sensing the difference between total and static pressure. The standard pitot tube remains the most accurate and reliable instrument for duct traverses.

**Velocity calculation:**

$$V = C\sqrt{\frac{2\Delta P}{\rho}}$$

For standard air (0.075 lb/ft³):

$$V = 1096.7\sqrt{\Delta P_{in}}$$

$$V = 4005\sqrt{\Delta P_{Pa}}$$

where:
- $V$ = velocity (ft/min or m/s)
- $C$ = pitot coefficient (0.99-1.00 for standard pitot)
- $\Delta P$ = velocity pressure (in. w.g. or Pa)
- $\rho$ = air density

**Measurement procedure:**
1. Zero manometer with both ports open to ambient
2. Insert pitot tube perpendicular to duct wall
3. Align tip parallel to airflow direction
4. Allow 10-15 seconds for pressure stabilization
5. Record velocity pressure at each traverse point
6. Calculate velocity from pressure at each point
7. Average all point velocities

**Accuracy considerations:**
- Pitot coefficient: verify with manufacturer data
- Alignment: maintain within ±5° of flow direction
- Minimum velocity: 400 ft/min for acceptable accuracy
- Pressure measurement: ±0.01 in. w.g. resolution required

## Hot-Wire Anemometer Traverse

Hot-wire and thermal anemometers measure low velocities where pitot tubes lack sufficient accuracy (<400 ft/min). These instruments require careful calibration and are sensitive to temperature variations.

**Measurement characteristics:**
- Velocity range: 0-2000 ft/min typical
- Response time: <1 second
- Accuracy: ±3% of reading ±10 ft/min
- Temperature compensation required

**Traverse procedure:**
1. Calibrate in similar temperature and humidity conditions
2. Allow 15-minute warm-up period
3. Position sensor at each traverse point
4. Allow 5-10 seconds for stabilization
5. Record time-averaged reading (5-10 seconds)
6. Verify calibration after completing traverse

**Correction for temperature:**

$$V_2 = V_1\sqrt{\frac{T_2}{T_1}}$$

where $T$ is absolute temperature.

## Measurement Accuracy and Uncertainty

Total measurement uncertainty includes instrument accuracy, point selection, flow profile variations, and environmental factors.

**Typical uncertainty sources:**
- Pitot tube coefficient: ±1%
- Pressure measurement: ±2%
- Point positioning: ±1-2%
- Flow profile assumptions: ±3-5%
- Air density calculations: ±1%

Combined uncertainty (root-sum-square):

$$U_{total} = \sqrt{u_1^2 + u_2^2 + ... + u_n^2}$$

Expected accuracy: ±5-7% for well-executed traverses under ideal conditions.

## Quality Assurance

Verify traverse quality through:
- Velocity profile symmetry check
- Comparison of single-plane vs. two-plane results
- Repeat measurements with <5% variation
- Flow rate comparison with system design values
- Temperature and barometric pressure documentation

## References

ASHRAE Handbook—Fundamentals, Chapter 37: Measurement and Instruments provides detailed guidance on traverse procedures, instrument selection, and uncertainty analysis for air system measurements.
