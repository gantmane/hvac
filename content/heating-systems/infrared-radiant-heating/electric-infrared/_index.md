---
title: "Electric Infrared Heaters"
weight: 2
description: "Engineering analysis of electric infrared heaters including quartz lamp, quartz tube, metal sheath, and ceramic panel technologies, wavelength characteristics, resistance heating fundamentals, reflector design, and applications for process heating, spot comfort, and industrial drying operations."
keywords: "electric infrared heaters, quartz tube heaters, quartz lamp heaters, metal sheath heaters, ceramic infrared, resistance heating, near-infrared, medium-infrared, far-infrared, infrared wavelength"
---

# Electric Infrared Heaters

Electric infrared heaters convert electrical energy directly into infrared radiation through resistance heating elements operating at controlled surface temperatures from 500-2000°F (260-1090°C). Unlike gas-fired systems requiring combustion, venting, and fuel supply infrastructure, electric infrared provides clean, precise, instantly controllable radiant heating suitable for process applications, spot comfort heating, paint curing, plastic forming, and semiconductor manufacturing. Element temperature determines wavelength spectrum from near-infrared (short-wave, 0.7-1.4 μm) through far-infrared (long-wave, 3.0-10 μm), enabling optimization for specific material absorption characteristics.

## Operating Principles

### Resistance Heating Fundamentals

Electrical power converts to heat through resistive dissipation:

$$P = I^2 R = \frac{V^2}{R}$$

Where:
- $P$ = Power (W)
- $I$ = Current (A)
- $V$ = Voltage (V)
- $R$ = Resistance (Ω)

**Heat generation rate per unit volume:**

$$\dot{q}_{gen} = \frac{P}{V_{element}} = \frac{I^2 \rho}{A_{cross}}$$

Where:
- $\rho$ = Resistivity (Ω·m)
- $A_{cross}$ = Element cross-sectional area (m²)

**Temperature-dependent resistivity:**

For most alloys (Ni-Cr, Fe-Cr-Al):

$$\rho(T) = \rho_0 [1 + \alpha(T - T_0)]$$

Where $\alpha$ = temperature coefficient (0.0001-0.0004 per °C)

**Result:** Positive temperature coefficient provides self-limiting behavior (resistance increases with temperature, reducing current and preventing thermal runaway).

### Radiant Energy Emission

Stefan-Boltzmann law governs total radiant emission:

$$E = \varepsilon \sigma T^4$$

Element efficiency (electrical to radiant conversion):

$$\eta_{rad} = \frac{P_{radiant}}{P_{electrical}} = \frac{\varepsilon \sigma A T^4}{P}$$

**Temperature dependence:**

| Element Temp | Radiant Efficiency | Convective Loss | Conductive Loss |
|--------------|-------------------|-----------------|-----------------|
| 500°F (533 K) | 25-35% | 50-60% | 10-15% |
| 1000°F (811 K) | 55-65% | 30-35% | 5-10% |
| 1500°F (1089 K) | 70-80% | 18-25% | 2-5% |
| 2000°F (1366 K) | 80-88% | 10-15% | 2-3% |

**Conclusion:** Higher element temperature dramatically improves radiant efficiency while reducing convective losses.

### Wavelength Distribution

Wien's displacement law determines peak emission wavelength:

$$\lambda_{max} = \frac{2898}{T} \text{ (μm, K)}$$

**Spectral classification:**

| Element Type | Temperature | λ_max | Spectrum | Classification |
|--------------|-------------|-------|----------|----------------|
| Quartz lamp | 2000°F (1366 K) | 2.1 μm | 0.7-2.5 μm | Near-infrared (NIR) |
| Quartz tube (medium) | 1400°F (1033 K) | 2.8 μm | 1.5-4.0 μm | Medium-infrared (MIR) |
| Quartz tube (low) | 1000°F (811 K) | 3.6 μm | 2.0-6.0 μm | Medium-infrared (MIR) |
| Metal sheath | 800°F (700 K) | 4.1 μm | 2.5-8.0 μm | Far-infrared (FIR) |
| Ceramic panel | 600°F (589 K) | 4.9 μm | 3.0-10 μm | Far-infrared (FIR) |

### Material Absorption Characteristics

Absorptivity varies dramatically with wavelength and material:

**Water (and water-containing materials):**
- Peak absorption: 3.0 μm, 6.0 μm
- Food drying, paint curing (water-based): MIR/FIR optimal

**Plastics (PE, PP, PVC):**
- Peak absorption: 3.4 μm
- Thermoforming, heat shrinking: MIR optimal

**Glass:**
- Low absorption: 0.7-2.5 μm (transparent to NIR)
- High absorption: > 2.8 μm
- Glass heating: MIR/FIR required

**Metals:**
- Absorption increases with wavelength
- Polished: α = 0.05-0.15 (NIR), 0.20-0.40 (MIR)
- Oxidized: α = 0.40-0.70 (NIR), 0.60-0.85 (MIR)

**Textiles and paper:**
- Broad absorption: 2-10 μm
- All infrared types effective

## Electric Infrared Technologies

### Quartz Lamp (High-Intensity NIR)

**Construction:**
- Tungsten wire filament (0.5-2.0 mm diameter)
- Quartz glass envelope (fused silica)
- Inert gas fill (argon, nitrogen, or halogen)
- Linear or U-shaped configuration
- Power: 500-5000W per lamp

**Operating characteristics:**
- Filament temperature: 3500-4500°F (2200-2750 K)
- Envelope temperature: 1800-2200°F (1250-1480 K)
- Emission spectrum: 70% in 0.7-2.0 μm (near-infrared)
- Radiant efficiency: 85-92%
- Response time: 1-3 seconds to full output

**Tungsten filament resistance:**

Cold resistance: $R_{cold}$ = 10-30 Ω typical
Hot resistance: $R_{hot}$ = 100-300 Ω typical
Resistance ratio: $R_{hot}/R_{cold}$ = 10-15

**Inrush current:** Initial surge 10-15× operating current due to low cold resistance. Requires slow-start controllers or current-limiting devices.

**Halogen cycle (if halogen-filled):**
Tungsten evaporates from filament → combines with halogen gas → halogen-tungsten compound deposits back on filament → extends life to 5000-10,000 hours vs. 2000-3000 for standard.

**Advantages:**
- Highest radiant efficiency (85-92%)
- Instant on/off (1-3 second response)
- Precise control via dimming
- Compact size, high power density
- Deep penetration (NIR spectrum)

**Disadvantages:**
- High surface temperature (fragile, hot)
- Relatively short life (5000-10,000 h)
- High inrush current (control complexity)
- Visible glow (bright white-yellow light)
- Limited to NIR spectrum only

**Applications:**
- Paint and coating curing (rapid)
- Plastic thermoforming (rapid heating)
- Paper drying (surface drying)
- Semiconductor wafer processing
- Food processing (surface cooking)

### Quartz Tube (Medium-Intensity MIR)

**Construction:**
- Resistance coil (Ni-Cr or Fe-Cr-Al alloy)
- Quartz tube envelope (12-25 mm diameter)
- Air or inert gas atmosphere
- Coil supported by ceramic end caps
- Power: 250-2500W per tube

**Operating characteristics:**
- Coil temperature: 1400-1800°F (1030-1260 K)
- Tube surface temperature: 1200-1600°F (920-1140 K)
- Emission spectrum: Peak 2.5-3.5 μm (medium-infrared)
- Radiant efficiency: 70-80%
- Response time: 30-90 seconds to 90% output

**Heat transfer mechanism:**
1. Resistance coil generates heat (I²R)
2. Radiation from coil to quartz tube inner surface
3. Conduction through quartz wall (minimal, thin wall)
4. Radiation from tube outer surface to target

**Quartz properties:**
- High infrared transmittance in 0.7-3.5 μm range
- Excellent thermal shock resistance
- Maximum continuous: 1800-2000°F
- Emissivity (oxidized surface): ε = 0.85-0.92

**Tube wall temperature control:**

$$T_{tube} = \left[\frac{P_{input}}{\pi D L (\varepsilon \sigma + h_c)}\right]^{1/4}$$

Where:
- $D$ = Tube diameter
- $L$ = Tube length
- $h_c$ = Convective heat transfer coefficient

**Advantages:**
- Moderate temperature (safer than quartz lamp)
- Longer life (8,000-15,000 hours)
- Good radiant efficiency (70-80%)
- Medium-wave spectrum (versatile applications)
- Lower inrush current vs. quartz lamp
- Reasonable cost

**Disadvantages:**
- Slower response vs. quartz lamp (30-90 sec)
- Visible glow (red-orange)
- Fragile quartz tube
- Moderate power density

**Applications:**
- Industrial drying (coatings, inks)
- Plastic heating (sheet forming)
- Powder coating curing
- Textile processing
- Food processing (through-heating)

### Metal Sheath (Low-Intensity FIR)

**Construction:**
- Resistance wire coil (Ni-Cr alloy)
- Magnesium oxide (MgO) insulation
- Metal sheath (stainless steel, Incoloy)
- Compacted construction (wire embedded in MgO)
- Power: 100-2000W per element

**Operating characteristics:**
- Sheath temperature: 700-1100°F (640-870 K)
- Emission spectrum: Peak 3.5-5.0 μm (far-infrared)
- Radiant efficiency: 50-65%
- Response time: 3-8 minutes to 90% output
- Life: 15,000-25,000 hours

**Thermal mass:**

High thermal mass (metal + MgO) provides:
- Slow heating (3-8 min to steady state)
- Slow cooling (maintains heat during short cycling)
- Thermal averaging (smooth output despite voltage fluctuations)
- Durability (resistant to mechanical shock)

**Sheath materials:**

**Stainless steel 304/316:**
- Maximum continuous: 1200°F
- Good corrosion resistance
- Emissivity: ε = 0.70-0.85 (oxidized)
- Most common

**Incoloy 800/825:**
- Maximum continuous: 1400°F
- Excellent oxidation resistance
- Higher cost
- High-temperature applications

**Carbon steel:**
- Maximum continuous: 900°F
- Economy applications
- Limited corrosion resistance
- Requires protective atmosphere

**Advantages:**
- Rugged, durable construction
- Long life (15,000-25,000 hours)
- Can be shaped (bent into custom forms)
- Weatherproof (outdoor capable)
- Safe (lower surface temperature)
- Low inrush current

**Disadvantages:**
- Lower radiant efficiency (50-65%)
- Slow response time (3-8 minutes)
- Lower power density
- Limited to far-infrared only

**Applications:**
- Comfort heating (outdoor patios, warehouses)
- Snow melting (pavement, walkways)
- Process warming (moderate temperature)
- Agricultural (livestock, greenhouses)
- Freeze protection (pipes, tanks)

### Ceramic Panel Heaters

**Construction:**
- Resistance wire embedded in ceramic matrix
- Ceramic composition: alumina-silicate or cordierite
- Flat panel or shaped geometry
- Thickness: 0.5-2.0 in
- Power: 50-500W per panel (lower density)

**Operating characteristics:**
- Surface temperature: 500-900°F (530-760 K)
- Emission spectrum: Peak 4.0-6.0 μm (far-infrared)
- Radiant efficiency: 40-55%
- Response time: 8-15 minutes to 90% output
- Life: 20,000-40,000 hours

**Ceramic properties:**
- High emissivity: ε = 0.90-0.95
- Excellent thermal mass (smooth output)
- Fragile (susceptible to thermal shock if poorly designed)
- Maximum continuous: 1200-1400°F

**Energy distribution:**
- Radiant: 40-55%
- Convective: 40-50% (significant due to large area, low temperature)
- Conductive: 5-10% (through mounting structure)

**Advantages:**
- Highest emissivity (0.90-0.95)
- Very long life (20,000-40,000 hours)
- Uniform surface temperature
- Soft, comfortable radiant heat
- Silent operation

**Disadvantages:**
- Lowest radiant efficiency (40-55%)
- Very slow response (8-15 minutes)
- Low power density
- Fragile ceramic (careful handling required)
- Higher cost per watt

**Applications:**
- Comfort heating (saunas, residential)
- Low-temperature process heating
- Food warming (holding cabinets)
- Reptile/animal enclosures
- Slow drying processes

## Reflector Design

### Reflector Geometry

**Parabolic reflectors:**

For point or linear source, parabolic cross-section focuses radiation:

$$y^2 = 4fx$$

**Depth of focus:**

$$d = \frac{D^2}{16f}$$

Where:
- $D$ = Reflector diameter/width
- $f$ = Focal length
- Element positioned at focal point for collimated beam

**Elliptical reflectors:**

Two focal points: element at one, target at other. Concentrates maximum radiation on target.

**V-groove reflectors:**

For quartz lamps, V-groove with polished surfaces:
- Angle: 90-120°
- Redirects radiation from back and sides
- Simpler than parabolic, lower cost

### Reflector Materials

**Reflectivity in infrared spectrum:**

| Material | NIR (1-2.5 μm) | MIR (2.5-4 μm) | FIR (4-10 μm) |
|----------|----------------|----------------|---------------|
| Polished aluminum | 92-96% | 90-94% | 85-92% |
| Gold plating | 96-98% | 96-98% | 95-98% |
| Polished stainless | 75-85% | 70-80% | 65-75% |
| Aluminum foil | 88-92% | 85-90% | 80-88% |

**Gold reflectors:**
- Highest reflectivity (96-98%)
- Chemically inert
- Expensive (only for premium applications)
- Process heating, semiconductor manufacturing

**Polished aluminum (anodized):**
- Excellent performance (90-94%)
- Moderate cost
- Most common industrial choice
- Periodic cleaning maintains performance

### Reflector Efficiency

**Net radiation reaching target:**

$$q_{target} = q_{direct} + q_{reflected}$$

Where:

$$q_{reflected} = q_{element} \times F_{view} \times \rho \times F_{target}$$

**Example calculation:**

Quartz lamp, 2000W, parabolic aluminum reflector:
- Direct radiation to target: 60% (1200W)
- Backward radiation: 40% (800W)
- View factor (element to reflector): 0.85
- Reflectivity: 0.92
- Reflector to target: 0.95

**Reflected component:**
800W × 0.85 × 0.92 × 0.95 = 594W

**Total to target:** 1200W + 594W = 1794W = **90% efficiency**

**Without reflector:** Only 1200W = **60% efficiency**

**Gain:** 50% increase in delivered radiation through reflector use.

## Control Methods

### Phase-Angle Control

SCR (silicon-controlled rectifier) varies power by delaying firing angle:

$$P = P_{max} \times \frac{1}{\pi} \left[\pi - \alpha + \frac{\sin(2\alpha)}{2}\right]$$

Where:
- $\alpha$ = Firing delay angle (0-180°)
- $P_{max}$ = Full power output

**Characteristics:**
- Smooth power variation: 0-100%
- Fast response (cycle-by-cycle control)
- Generates harmonic distortion
- Suitable for resistive loads

**Harmonic mitigation:** Use at > 50% power to minimize THD (total harmonic distortion).

### Zero-Crossing Control

SCR switches at voltage zero-crossing, varies power by cycle skipping:

$$P = P_{max} \times \frac{N_{on}}{N_{total}}$$

**Characteristics:**
- No harmonic distortion
- Stepwise power control
- Longer thermal time constant (averaging effect)
- Preferred for sensitive electrical environments

### Pulse Width Modulation (PWM)

Cycles element on/off at fixed frequency:

$$P = P_{max} \times \frac{t_{on}}{t_{on} + t_{off}}$$

**Typical frequency:** 0.1-10 Hz (thermal mass provides averaging)

**Characteristics:**
- Digital control (simple microcontroller implementation)
- No power quality concerns (full cycles)
- Requires thermal mass for smooth output
- Suitable for all element types

### Temperature Feedback Control

**PID control:**

$$P(t) = K_p e(t) + K_i \int e(t)dt + K_d \frac{de(t)}{dt}$$

Where $e(t)$ = setpoint - measured temperature

**Tuning parameters:**
- $K_p$ (proportional): 2-10 typical (depends on thermal mass)
- $K_i$ (integral): 0.01-0.1 (eliminates steady-state error)
- $K_d$ (derivative): 0.1-1.0 (anticipates changes)

**Temperature sensing:**
- Thermocouples (process temperature)
- RTDs (precise control, ±0.1°C)
- Infrared sensors (non-contact, fast response)

## Application Engineering

### Power Density Calculation

Required power density depends on application:

$$P_{density} = \frac{q_{load} + q_{loss}}{A_{heated} \times \eta_{system}}$$

Where:
- $q_{load}$ = Heating requirement (W/m²)
- $q_{loss}$ = Environmental loss (convection, conduction)
- $A_{heated}$ = Target area (m²)
- $\eta_{system}$ = System efficiency (0.60-0.90)

**Typical power densities:**

| Application | Power Density | Element Type |
|-------------|---------------|--------------|
| Comfort heating | 5-15 kW/m² | Metal sheath, ceramic |
| Paint curing | 20-50 kW/m² | Quartz tube |
| Plastic forming | 50-150 kW/m² | Quartz lamp |
| Metal preheating | 30-80 kW/m² | Quartz tube |
| Food processing | 15-40 kW/m² | Quartz tube |

### Mounting Distance

Intensity at target surface:

$$I = \frac{P \times \eta_{rad} \times \cos^3(\theta)}{r^2}$$

**Optimization:** Balance intensity (close mounting) with uniformity (distant mounting).

**Rule of thumb:** Mount at distance = 1.5-3.0× heater width for uniform coverage.

**Example:**
- 500mm wide quartz lamp array
- Mounting distance: 750-1500mm
- Provides pattern factor < 1.5

### Array Design

**Spacing for uniform coverage:**

$$S = 2L \times \tan(\theta/2)$$

Where:
- $S$ = Center-to-center spacing
- $L$ = Mounting distance
- $\theta$ = Effective beam angle (typically 90-120°)

**Multi-zone control:**
Divide large areas into independently controlled zones:
- Preheat zone (moderate power)
- Process zone (maximum power)
- Cooldown zone (low power or off)

## Electrical Requirements

### Power Supply Sizing

**Single-phase limitation:** Maximum ~12 kW (50A @ 240V)

**Three-phase for larger loads:**
- Balanced loading across phases
- 208V, 240V, 480V common
- Delta or wye configuration

**Example:** 36 kW infrared system
- Three-phase 240V: 87A per phase
- Requires 100A circuit breaker, #2 AWG wire

### Voltage Drop Considerations

**Acceptable voltage drop:** < 3% for stable operation

$$\Delta V = \frac{2 \times I \times L \times \rho}{A_{wire}}$$

**Impact on power:**

$$P_{actual} = P_{rated} \times \left(\frac{V_{actual}}{V_{rated}}\right)^2$$

5% voltage drop → 10% power reduction

**Mitigation:** Proper wire sizing, minimize run length, use higher voltage where possible.

### Ground Fault Protection

**GFCI required:**
- Wet or damp locations
- Outdoor installations
- Within 6 ft of water source

**Industrial GFCI:** 30 mA trip threshold, meets NEC requirements

## Safety Considerations

### Burn Hazards

**Surface temperatures:**
- Quartz lamp: 2000°F (1090°C) - severe burn on contact
- Quartz tube: 1500°F (815°C) - severe burn on contact
- Metal sheath: 1000°F (540°C) - burn hazard
- Ceramic panel: 700°F (370°C) - burn hazard

**Guards and shields:**
- Wire mesh guards (prevent direct contact)
- Transparent quartz shields (allow radiation transmission)
- Minimum 3-6 in clearance around elements
- Warning labels on equipment

### Electrical Safety

**Grounding:**
- All metal components bonded to ground
- Ground fault protection in wet locations
- Proper conduit and junction box installation

**Overcurrent protection:**
- Circuit breakers sized for 125% of continuous load
- Branch circuit protection per NEC Article 424

**Insulation:**
- Ceramic standoffs for high-temperature sections
- Heat-resistant wire insulation (200°C minimum)
- Periodic insulation resistance testing (> 1 MΩ)

### Fire Hazards

**Clearances to combustibles:**
- Minimum 18-36 in (depends on element temperature)
- Never direct radiation at stored combustible materials
- Automatic shutoff if over-temperature condition

**Ignition temperature concerns:**
- Paper: 450°F
- Wood: 500-700°F
- Textiles: 400-600°F
- Keep element temperature and radiant flux below material ignition

## Maintenance

### Routine Inspection

**Quarterly:**
- Visual inspection of elements (cracking, deformation)
- Reflector cleaning and condition
- Electrical connection tightness
- Control system function test

**Annually:**
- Insulation resistance testing
- Reflector reflectivity measurement
- Power output verification
- Temperature calibration

### Element Replacement

**Failure indicators:**
- Open circuit (complete failure)
- Reduced output (element degradation)
- Hot spots (uneven heating)
- Visible cracks or breaks

**Replacement cost:**
- Quartz lamp: $15-50 per lamp
- Quartz tube: $25-80 per tube
- Metal sheath: $30-100 per element
- Ceramic panel: $50-200 per panel

**Expected life:**
- Quartz lamp: 5,000-10,000 hours
- Quartz tube: 8,000-15,000 hours
- Metal sheath: 15,000-25,000 hours
- Ceramic panel: 20,000-40,000 hours

### Reflector Maintenance

**Cleaning procedure:**
1. De-energize and cool completely
2. Remove loose dust with compressed air
3. Wipe with damp cloth (water or mild detergent)
4. Rinse thoroughly, dry completely
5. Avoid abrasives (damage reflective surface)

**Frequency:**
- Clean environments: Annually
- Moderate dust: Semi-annually
- Heavy dust/contamination: Quarterly

**Performance recovery:** Proper cleaning restores 85-95% of original reflectivity.

## Economic Analysis

### Operating Cost

**Energy consumption:**

$$C_{annual} = P_{rated} \times t_{operation} \times C_{electric}$$

**Example:** 10 kW system, 2000 h/year, $0.12/kWh
- Annual energy: 10 kW × 2000 h = 20,000 kWh
- Annual cost: 20,000 kWh × $0.12 = **$2,400/year**

### Comparison: Electric vs. Gas

**Electric infrared:**
- Efficiency: 85% (quartz lamp to target)
- Operating cost: $0.12/kWh ÷ 0.85 = $0.141/kWh delivered
- Maintenance: Low
- Capital: Moderate

**Gas high-intensity:**
- Efficiency: 65% (combustion to target)
- Operating cost: $1.00/therm ÷ 0.65 = $1.54/therm delivered = $0.045/kWh delivered
- Maintenance: Moderate
- Capital: Moderate
- **Operating cost advantage: Gas = 1/3 of electric**

**When electric makes sense:**
- No gas available
- Clean environment required (semiconductor, food)
- Precise control essential
- Intermittent operation (instant on/off advantage)
- Small capacity (< 10 kW)
- Process heating (specialized wavelength requirements)

**When gas makes sense:**
- Large capacity (> 25 kW)
- Continuous operation
- Space heating (comfort applications)
- Operating cost critical

---

*Electric infrared heaters provide clean, precise, instantly controllable radiant heating through resistance elements spanning near-infrared to far-infrared spectra, enabling optimized performance for process heating, spot comfort, and applications requiring wavelength-specific absorption characteristics unavailable from combustion-based systems.*
