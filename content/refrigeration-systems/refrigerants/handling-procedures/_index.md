---
title: "Refrigerant Handling Procedures"
description: "Comprehensive procedures for refrigerant recovery, recycling, reclamation, charging, leak detection, and EPA Section 608 compliance requirements"
weight: 7
---

## Overview

Proper refrigerant handling procedures are mandated by EPA Section 608 regulations and essential for environmental protection, system performance, and technician safety. All technicians working with refrigeration systems containing more than 0.5 lb of refrigerant must be EPA certified.

**Critical Requirements:**
- Recovery before system opening (with limited exemptions)
- Certified recovery equipment meeting EPA standards
- Proper cylinder handling and storage
- Accurate charging and leak detection procedures
- Personal protective equipment usage
- Documentation and recordkeeping

## EPA Section 608 Requirements

### Certification Levels

| Type | Scope | Equipment Coverage |
|------|-------|-------------------|
| Type I | Small appliances | Systems containing < 5 lb refrigerant |
| Type II | High-pressure systems | HCFC-22, R-410A, R-404A systems |
| Type III | Low-pressure systems | Centrifugal chillers (R-123, R-11) |
| Universal | All equipment | Complete authorization for all refrigerants |

### Required Recovery Levels

**High-Pressure Appliances (≥135 psig at 104°F):**

| System Type | Recovery Requirement |
|-------------|---------------------|
| Systems < 200 lb | 0 psig (before disposal) |
| Systems < 200 lb | 10% of system charge or 4 in Hg vacuum (before major repair) |
| Systems ≥ 200 lb | 15% of system charge or 4 in Hg vacuum |
| Systems with non-functioning compressor | 0 psig or 4 in Hg vacuum |

**Low-Pressure Appliances (<135 psig at 104°F):**

| System Type | Recovery Requirement |
|-------------|---------------------|
| Before disposal | 25 mm Hg absolute |
| Before major repair | 25 mm Hg absolute |
| With leak rate > 35% annually | 25 mm Hg absolute |

### Recordkeeping Requirements

Maintain records for at least 3 years:
- Quantity of refrigerant added to systems
- Quantity of refrigerant recovered for disposal
- Name and certification number of technician
- Date of service
- Identity of cylinders used for recovery

## Recovery Procedures

### Recovery Equipment Standards

Recovery equipment must be certified to meet ARI 740 or AHRI 740 standards.

**Equipment Categories:**

| Category | Application | Recovery Rate |
|----------|-------------|---------------|
| Self-contained | Single recovery unit | 4 lb/min liquid or 1 lb/min vapor (for R-22) |
| System-dependent | Uses system compressor | 4 lb/min liquid or 1 lb/min vapor |

### Vapor Recovery Method

Used when system contains only vapor refrigerant or liquid charging is not practical.

**Procedure:**
1. Connect recovery unit to system service ports
2. Connect recovery cylinder to recovery unit outlet
3. Open cylinder valve (ensure cylinder not filled >80% capacity)
4. Start recovery unit
5. Monitor system pressure gauges
6. Recovery complete when pressures stabilize at required levels
7. Close all valves
8. Allow system to sit 5-10 minutes and verify pressure does not rise

**Vapor Recovery Rate Equation:**

$$\dot{m}_v = \frac{(P_s - P_r) \cdot V_d \cdot \eta_v}{R \cdot T}$$

Where:
- $\dot{m}_v$ = vapor mass flow rate (lb/min)
- $P_s$ = system pressure (psia)
- $P_r$ = recovery cylinder pressure (psia)
- $V_d$ = displacement volume (ft³/min)
- $\eta_v$ = volumetric efficiency
- $R$ = gas constant for refrigerant (ft·lbf/lbm·°R)
- $T$ = absolute temperature (°R)

### Liquid Recovery Method

Fastest method for recovering refrigerant charge. Removes liquid phase directly from system.

**Push-Pull Recovery:**

Equipment setup:
- Nitrogen or compressed air supply regulated to 0-2 psig
- Pressure applied to high side liquid line or receiver
- Liquid pushed to recovery unit or cylinder
- Recovery unit pulls vapor from low side

**Procedure:**
1. Connect recovery cylinder to system liquid line
2. Attach pressure source to high side (receiver top)
3. Apply gentle pressure (0-2 psig maximum)
4. Monitor liquid level if receiver has sight glass
5. When liquid recovery complete, switch to vapor recovery
6. Recover remaining vapor charge per standard procedure

**Safety Warning:** Never apply excessive pressure during push-pull recovery. Overpressure can damage compressor seals, system components, or cause refrigerant release.

### Liquid Recovery Rate

$$\dot{m}_l = A \cdot v \cdot \rho_l$$

Where:
- $\dot{m}_l$ = liquid mass flow rate (lb/min)
- $A$ = line cross-sectional area (ft²)
- $v$ = liquid velocity (ft/min)
- $\rho_l$ = liquid density (lb/ft³)

Typical liquid recovery rates: 10-30 lb/min depending on line size and pressure differential.

## Recycling Requirements

Recycling is cleaning refrigerant for reuse using oil separation and single or multiple passes through filter-driers. Recycling can be performed on-site.

**Recycling Equipment Standards:**
- Must meet ARI 740 or AHRI 740 certification
- Oil separation to < 4000 ppm for single refrigerants
- Moisture removal to meet ARI 700 standards
- Particulate filtration to 10 microns

**Recycled Refrigerant Purity Standards (ARI 700):**

| Refrigerant | Max Water (ppm) | Max Acidity (ppm) | High-Boiling Residue |
|-------------|-----------------|-------------------|---------------------|
| R-22 | 10 | 1 (as HCl) | 0.01% by volume |
| R-134a | 10 | 1 (as HCl) | 0.01% by volume |
| R-410A | 10 | 1 (as HCl) | 0.01% by volume |
| R-404A | 10 | 1 (as HCl) | 0.01% by volume |

**Recycling Process:**
1. Recover refrigerant into recovery cylinder
2. Pass through oil separator (coalescing or distillation)
3. Filter through replaceable core filter-drier
4. May include multiple passes for improved purity
5. Test for moisture and acidity if critical application
6. Store in labeled dedicated cylinder

## Reclamation Standards

Reclamation is refrigerant reprocessing to ARI 700 virgin refrigerant specifications. Reclamation requires certified off-site facility.

**Reclamation Process:**
- Distillation to separate refrigerants and contaminants
- Chemical treatment to remove acids
- Filtration and drying to virgin specifications
- Chemical analysis to verify purity
- Must meet AHRI 700 specifications for all parameters

**Reclamation Required When:**
- Refrigerant contaminated with other refrigerants
- Oil contamination exceeds recycling equipment capability
- Acid contamination from compressor burnout
- Non-condensables exceed acceptable limits
- Hermetic compressor burnout (Class 1 contamination)

**Reclaimed Refrigerant Standards (AHRI 700):**

| Parameter | R-22 | R-134a | R-410A |
|-----------|------|--------|--------|
| Purity (wt%) | 99.9% min | 99.5% min | 99.5% min |
| Water (ppm) | 10 max | 10 max | 10 max |
| Acidity (ppm) | 0.1 max | 1 max | 1 max |
| Non-condensables | 1.5% max | 1.5% max | 1.5% max |

## Charging Procedures

### Pre-Charging System Preparation

**Required Steps:**
1. Complete all leak testing and repair
2. Evacuate system to required vacuum level
3. Perform standing vacuum test (pressure rise test)
4. Verify system cleanliness and dryness
5. Calculate or verify required refrigerant charge
6. Select appropriate charging method
7. Prepare manifold gauge set and charging equipment

### Liquid Charging Methods

**When to Use Liquid Charging:**
- Initial system charge
- Adding significant refrigerant quantity
- Manufacturer specifies liquid charging
- System designed for liquid charging (TXV metering)

**Subcooling Method (Most Common):**

Procedure:
1. Connect charging cylinder to manifold high side (liquid port)
2. Invert cylinder or use cylinder with dip tube
3. Open cylinder valve and high-side manifold valve
4. Crack service valve briefly to purge air from hose
5. Add liquid refrigerant slowly (compressor OFF initially)
6. Start system when adequate charge for compressor protection
7. Monitor subcooling at condenser outlet
8. Add refrigerant until subcooling reaches design value

**Target Subcooling Values:**

| System Type | Typical Subcooling | Acceptable Range |
|-------------|-------------------|------------------|
| Fixed orifice | 8-12°F | 6-15°F |
| TXV systems | 10-15°F | 8-20°F |
| Long line set | 15-20°F | 12-25°F |

**Subcooling Calculation:**

$$SC = T_{sat} - T_{liquid}$$

Where:
- $SC$ = subcooling (°F)
- $T_{sat}$ = saturation temperature at measured pressure (°F)
- $T_{liquid}$ = measured liquid line temperature (°F)

### Vapor Charging Methods

**When to Use Vapor Charging:**
- Adding small refrigerant quantities
- Topping off charge
- Near-azeotropic or zeotropic blends requiring special handling
- System operating during charge

**Superheat Method:**

Procedure:
1. System must be operating
2. Connect charging cylinder upright (vapor withdrawal)
3. Add vapor through suction service port (low side)
4. Measure suction line temperature at compressor
5. Read suction pressure and convert to saturation temperature
6. Calculate superheat
7. Add refrigerant slowly until proper superheat achieved

**Target Superheat Values:**

| System Type | Typical Superheat | Acceptable Range |
|-------------|------------------|------------------|
| Fixed orifice | 10-15°F | 8-20°F |
| TXV systems | 8-12°F | 6-15°F |
| Commercial refrigeration | 8-12°F | 5-15°F |

**Superheat Calculation:**

$$SH = T_{suction} - T_{sat}$$

Where:
- $SH$ = superheat (°F)
- $T_{suction}$ = measured suction line temperature (°F)
- $T_{sat}$ = saturation temperature at suction pressure (°F)

### Weighing Method

Most accurate charging method. Essential for critical charge systems.

**Equipment Required:**
- Calibrated electronic scale (0.1 oz resolution minimum)
- Refrigerant cylinder on scale
- Manifold gauge set
- Temperature and pressure monitoring equipment

**Procedure:**
1. Place cylinder on scale and record initial weight
2. Calculate target final weight (initial weight - charge amount)
3. Connect cylinder to system
4. Open valves and begin charging
5. Monitor scale continuously
6. Close valves when target weight reached
7. Verify system operation parameters

**Critical Charge Systems:**
- Residential heat pumps with critical charge curves
- Systems with capillary tube metering
- Small refrigeration systems
- Systems where ±10% charge affects performance >5%

## Leak Detection Methods

### Bubble Test (Soap Solution)

**Application:** Gross leak detection, verification of suspected leak locations.

**Solution Preparation:**
- Commercial leak detector solution (preferred)
- Alternative: 25% liquid dish soap, 75% water
- Do not use detergents with lanolin or oils

**Procedure:**
1. Pressurize system to operating pressure or test pressure
2. Apply solution liberally to suspected areas
3. Observe for bubble formation (2-3 minutes)
4. Bubbles indicate refrigerant leak
5. Mark location for repair

**Detection Threshold:** Approximately 0.5 oz/year leak rate.

### Electronic Leak Detection

Most sensitive and reliable method for refrigerant leak detection.

**Detector Types:**

| Type | Technology | Sensitivity | Refrigerants |
|------|-----------|-------------|--------------|
| Heated diode | Heated element | 0.1 oz/yr | CFCs, HCFCs, HFCs |
| Infrared | IR absorption | 0.01 oz/yr | HFCs, HCFCs |
| Ultrasonic | Sound detection | Varies | All (detects escaping gas) |
| Corona suppression | Ion detection | 0.05 oz/yr | Halogenated refrigerants |

**Heated Diode Operation:**
1. Warm up detector per manufacturer specifications (typically 3-5 minutes)
2. Calibrate using reference sample if required
3. Position probe tip 0.25-0.5 inches from test surface
4. Move probe slowly (1-2 inches per second)
5. Test all connections, joints, and potential leak points
6. Allow settling time when alarm activates
7. Confirm leak location with repeated passes

**Sensitivity Adjustment:**
- Start with highest sensitivity
- Reduce sensitivity in contaminated areas
- Increase sensitivity for difficult-to-access locations

**False Positive Sources:**
- Moisture from recently cleaned surfaces
- Residual refrigerant on clothing or hands
- Hydrocarbon contamination (oils, greases)
- Electrical interference

### Ultrasonic Leak Detection

Detects high-frequency sound produced by turbulent gas flow through leak orifice.

**Operating Principle:**
- Refrigerant escaping through leak creates ultrasonic sound (40 kHz range)
- Detector converts ultrasonic frequency to audible range
- Amplitude indicates proximity to leak

**Advantages:**
- Detects any gas leak (not refrigerant-specific)
- Works in noisy environments (mechanical noise filtered)
- No warm-up time required
- Not affected by refrigerant contamination

**Limitations:**
- Requires adequate pressure differential (>10 psig)
- Less effective for very small leaks
- Background ultrasonic noise can interfere

**Procedure:**
1. Pressurize system to operating pressure
2. Turn on detector and adjust sensitivity
3. Use probe or directional sensor
4. Scan suspected areas
5. Listen for amplitude increase indicating leak
6. Verify with electronic detector or bubble test

### Fluorescent Dye Method

Long-term leak detection for difficult-to-locate leaks.

**Dye Types:**
- Universal fluorescent dye (compatible with all refrigerants and oils)
- Refrigerant-specific dyes
- Oil-soluble dyes

**Procedure:**
1. Inject measured quantity of dye into system (per manufacturer specifications)
2. Operate system minimum 20 minutes to circulate dye
3. Inspect system with UV lamp (365-395 nm wavelength)
4. Dye appears bright yellow-green at leak location
5. Clean area and verify leak with other methods
6. Document leak location

**Dye Injection Rates:**

| System Size | Dye Quantity |
|-------------|--------------|
| < 1 ton | 0.25 oz |
| 1-5 tons | 0.5 oz |
| 5-15 tons | 1 oz |
| > 15 tons | 1-2 oz |

**Advantages:**
- Locates intermittent leaks
- Finds multiple leaks simultaneously
- Permanent marker (dye remains at leak site)
- Effective for difficult-to-access locations

**Limitations:**
- Requires system operation time
- UV lamp required for inspection
- Environmental contamination possible
- Must remove dye for major repairs

### Nitrogen Pressure Testing

**Purpose:** Verify system leak tightness before refrigerant charging.

**Pressure Test Levels:**

| System Type | Test Pressure | Hold Time |
|-------------|---------------|-----------|
| Low-pressure systems | 150 psig | 24 hours |
| High-pressure systems | 400-450 psig | 24 hours |
| High-side only | 400-450 psig | 24 hours |
| Low-side only | 150 psig | 24 hours |

**Procedure:**
1. Connect dry nitrogen cylinder with pressure regulator
2. Pressurize system to test pressure slowly
3. Monitor pressure with calibrated gauge
4. Record initial pressure and temperature
5. Wait specified hold time (typically 24 hours)
6. Measure final pressure and temperature
7. Calculate pressure drop accounting for temperature change

**Pressure-Temperature Correction:**

$$P_2 = P_1 \cdot \frac{T_2}{T_1}$$

Where:
- $P_1$ = initial absolute pressure (psia)
- $P_2$ = expected final pressure at different temperature (psia)
- $T_1$ = initial absolute temperature (°R)
- $T_2$ = final absolute temperature (°R)

**Acceptable Pressure Drop:**
- Zero pressure drop (after temperature correction) = leak-tight
- Any measurable drop indicates leak requiring location and repair

**Safety Requirements:**
- Never exceed system design pressure
- Never use oxygen for pressure testing (explosive with oil)
- Always use dry nitrogen (prevents moisture introduction)
- Use pressure relief valve set at safe pressure
- Stand clear during initial pressurization

## Evacuation Procedures

### Purpose of Evacuation

Removes non-condensable gases and moisture from refrigeration systems before charging.

**Non-Condensables:**
- Air (nitrogen, oxygen)
- Gaseous contaminants
- Water vapor

**Effects of Non-Condensables:**
- Elevated discharge pressure
- Reduced system capacity (10-30%)
- Increased power consumption
- Reduced compressor life
- Formation of acids with moisture

### Vacuum Levels and Requirements

| Vacuum Level | Description | Application |
|--------------|-------------|-------------|
| 29 in Hg | Low vacuum | Inadequate for most systems |
| 500 microns | Standard evacuation | Minimum for most residential/commercial |
| 250 microns | Deep vacuum | Critical systems, chillers |
| 100 microns | Ultra-deep vacuum | Laboratory, special applications |

**Micron to In Hg Conversion:**

| Microns | In Hg | mm Hg |
|---------|-------|-------|
| 500 | 29.92 | 0.5 |
| 250 | 29.96 | 0.25 |
| 100 | 29.99 | 0.1 |

### Single Evacuation Method

**Equipment Required:**
- Two-stage vacuum pump (3 CFM minimum for residential systems)
- Electronic vacuum gauge (micron gauge)
- Manifold gauge set with low-loss fittings
- Large diameter hoses (3/8" or 1/2")

**Procedure:**
1. Connect vacuum pump to system with shortest possible hose path
2. Connect micron gauge directly to system (not gauge manifold)
3. Start vacuum pump
4. Open both manifold valves (high and low side)
5. Evacuate until micron gauge reads target vacuum
6. Typical time: 30-60 minutes for residential system
7. Perform standing vacuum test

**Standing Vacuum Test:**
1. Close manifold valves isolating system
2. Stop vacuum pump
3. Monitor micron gauge for 10-15 minutes
4. Acceptable: pressure rise < 100 microns
5. Excessive rise indicates leak or trapped moisture

### Triple Evacuation Method

Used for systems with heavy contamination, moisture, or after compressor burnout.

**Procedure:**
1. **First Evacuation:**
   - Pull vacuum to 1000-2000 microns
   - Break vacuum with dry nitrogen to 5-10 psig
   - Purge nitrogen briefly to atmosphere

2. **Second Evacuation:**
   - Evacuate to 500-1000 microns
   - Break vacuum with dry nitrogen to 5-10 psig
   - Purge nitrogen briefly

3. **Third Evacuation:**
   - Evacuate to final target vacuum (500 microns or lower)
   - Perform standing vacuum test
   - If test passes, break vacuum with refrigerant charge

**Nitrogen Break Advantages:**
- Helps evaporate remaining moisture
- Purges atmospheric air
- Dilutes contaminants for removal

### Deep Vacuum Method

Achieves lowest vacuum levels for critical applications.

**Enhanced Procedures:**
- Use large diameter hoses (1/2" minimum)
- Minimize hose length
- Connect pump to multiple access points simultaneously
- Use core removal tools (Schrader valve cores removed)
- Evacuate through liquid and suction lines
- Consider system heat application (not exceeding 130°F)

**Heat Application for Moisture Removal:**

Heating system components during evacuation accelerates moisture evaporation:
- Recommended temperature: 100-130°F
- Methods: Heat lamps, blankets, or building heat
- Monitor temperature to prevent damage
- Particularly effective for flooded systems

**Vacuum Pump Sizing:**

Required CFM rating depends on system volume:

$$CFM = \frac{V_{system}}{t_{desired}} \cdot 0.5$$

Where:
- $CFM$ = pump displacement (ft³/min)
- $V_{system}$ = system internal volume (ft³)
- $t_{desired}$ = evacuation time target (minutes)
- 0.5 = efficiency factor

### Vacuum Pump Operation and Maintenance

**Oil Maintenance:**
- Change oil after contaminated system evacuation
- Check oil level before each use
- Oil should be clear (amber color)
- Cloudy oil indicates moisture contamination

**Pump Performance Issues:**

| Symptom | Cause | Solution |
|---------|-------|----------|
| Slow evacuation | Contaminated oil | Change oil |
| Cannot reach target vacuum | System leak | Perform leak test |
| Pump runs hot | Inadequate oil | Add oil to proper level |
| Oil foaming | Excessive moisture | Change oil, continue evacuation |

**Ballast Valve:**
- Open during initial evacuation (high moisture)
- Close for final deep vacuum
- Prevents oil contamination from moisture

## Cylinder Storage and Handling

### Cylinder Color Codes

| Color | Contents | Application |
|-------|----------|-------------|
| White (top) | Refrigerant (various) | Virgin refrigerant |
| Yellow (top) | Recovery | Recovered refrigerant |
| Gray | Recovery (all refrigerants) | Universal recovery |
| Green | Recovery (R-22 only) | Dedicated R-22 |

### Storage Requirements

**Temperature Limits:**
- Storage temperature: 40-125°F
- Never expose to temperatures >130°F
- Store in cool, dry, well-ventilated location
- Protect from direct sunlight

**Physical Storage:**
- Store cylinders upright when possible
- Secure cylinders to prevent falling
- Separate full and empty cylinders
- Label partially filled cylinders with contents and date
- Never store near heat sources or ignition sources
- Indoor storage preferred

**Cylinder Filling Limits:**
- Maximum fill: 80% of cylinder volume
- Accounts for liquid thermal expansion
- DOT regulations strictly enforced
- Overfilled cylinders create safety hazard

### Transportation Requirements

**DOT Regulations:**
- Cylinders must be DOT approved
- Valve protection cap required during transport
- Secure cylinders in vehicle to prevent movement
- Adequate ventilation in transport vehicle
- No smoking in vehicle transporting refrigerants

**Vehicle Transport:**
- Secure cylinders in upright position
- Use cylinder restraints or cages
- Separate from driver compartment if possible
- Keep windows open for ventilation
- Never leave cylinders in hot vehicles

## Personal Protective Equipment

### Required PPE for Refrigerant Handling

| Equipment | Purpose | Specification |
|-----------|---------|---------------|
| Safety glasses | Eye protection from liquid refrigerant | ANSI Z87.1 approved |
| Face shield | Full face protection during cylinder changes | Polycarbonate, ANSI Z87.1 |
| Gloves | Hand protection from frostbite | Neoprene or nitrile, cryogenic rated |
| Long sleeves | Arm protection | Tightly woven, natural fiber preferred |
| Steel-toed boots | Foot protection | ASTM approved safety footwear |

### Safety Protocols

**Liquid Refrigerant Contact:**
- Causes frostbite on contact
- Immediately flush affected area with lukewarm water (not hot)
- Do not rub affected area
- Seek medical attention for severe exposure
- Remove contaminated clothing

**Refrigerant Inhalation:**
- Use adequate ventilation
- Avoid breathing vapors in confined spaces
- Refrigerant displaces oxygen (asphyxiation hazard)
- Some refrigerants decompose at high temperatures forming toxic compounds
- Evacuate area if refrigerant release occurs

**Refrigerant Exposure Limits (ACGIH TLV-TWA):**

| Refrigerant | 8-Hour TWA | STEL (15 min) |
|-------------|------------|---------------|
| R-22 | 1000 ppm | N/A |
| R-134a | 1000 ppm | N/A |
| R-410A | 1000 ppm | N/A |
| R-123 | 50 ppm | N/A |
| Ammonia (R-717) | 25 ppm | 35 ppm |

**Confined Space Precautions:**
- Test oxygen level before entry (19.5% minimum)
- Use supplied air respirator if refrigerant concentration high
- Position exhaust fan to remove refrigerant vapors
- Post warning signs
- Maintain constant ventilation during work

**Fire Safety:**
- Most refrigerants non-flammable under normal conditions
- Decomposition products toxic (hydrogen fluoride, hydrogen chloride)
- Keep away from open flames and hot surfaces
- Halogen torch leak detection creates toxic decomposition
- Use proper ventilation when brazing or welding

## Equipment Specifications

### Recovery Equipment

**Recovery Unit Components:**
- Compressor (hermetic or semi-hermetic)
- Oil separator
- Moisture indicator
- Filter-drier
- High-pressure safety switch
- Low-pressure safety switch

**Performance Specifications (AHRI 740):**

| Refrigerant | Liquid Recovery Rate | Vapor Recovery Rate |
|-------------|---------------------|-------------------|
| R-22 | 4 lb/min minimum | 1 lb/min minimum |
| R-134a | 4 lb/min minimum | 1 lb/min minimum |
| R-410A | 4 lb/min minimum | 1 lb/min minimum |

### Recovery Cylinders

**Cylinder Types:**

| Type | Service Pressure | Application |
|------|------------------|-------------|
| DOT-4BA | 400 psig | Low-pressure refrigerants |
| DOT-4BW | 500 psig | High-pressure refrigerants |
| DOT-39 | Varies | Reusable recovery cylinders |

**Cylinder Testing:**
- Requalification required every 5 years
- Hydrostatic test to 5/3 service pressure
- Visual inspection for damage, corrosion
- Verify test date stamp on cylinder

### Manifold Gauge Sets

**Pressure Ranges:**
- Low-pressure gauge: 30 in Hg vacuum to 250 psig (compound)
- High-pressure gauge: 0-500 psig typical

**Hose Specifications:**
- Minimum diameter: 1/4" (3/8" preferred for faster evacuation)
- Low-loss fittings minimize refrigerant release
- Color coding: Blue (low), Red (high), Yellow (center/charging)

**Digital Manifold Features:**
- Direct temperature measurement
- Automatic superheat/subcooling calculation
- Pressure-temperature correlation
- Data logging capability
- Higher accuracy than analog gauges

### Charging Equipment

**Electronic Scales:**
- Resolution: 0.1 oz minimum
- Capacity: 220 lb typical
- NIST traceable calibration
- Temperature compensation

**Charging Cylinders:**
- Graduated sight glass for volume measurement
- Heating element for vapor pressure boost
- Pressure gauge
- Liquid and vapor valves

## Documentation and Compliance

### Service Records

Required documentation for EPA compliance:
- Date of service
- Technician name and certification number
- Equipment identification
- Refrigerant type and quantity added
- Refrigerant quantity recovered
- System leak test results
- Repairs performed
- Recovery cylinder identification

### Leak Repair Requirements

**Commercial Refrigeration and Industrial Process:**
- Trigger threshold: 10-20% annual leak rate (depends on system type)
- Repair deadline: 30 days after discovery
- Follow-up verification required

**Comfort Cooling:**
- Trigger threshold: 10% annual leak rate
- Repair deadline: 30 days after discovery

**Annual Leak Rate Calculation:**

$$L = \frac{R_{added}}{C_{system}} \times 100\%$$

Where:
- $L$ = annual leak rate (%)
- $R_{added}$ = refrigerant added in 12-month period (lb)
- $C_{system}$ = full system charge (lb)

### Refrigerant Sales Restrictions

**Purchase Requirements:**
- EPA Section 608 certification required
- Certification number provided to supplier
- Applies to containers > 2 lb refrigerant
- Self-sealing containers < 2 lb may have different requirements

**Banned Refrigerants:**
- CFCs (R-12, R-11, R-502) banned for new equipment
- Production ceased (limited reclaimed supply available)
- HCFC phasedown schedule in effect
- HFC phasedown beginning under AIM Act

## Safety Incidents and Emergency Response

### Refrigerant Release Response

**Small Release (<5 lb):**
1. Ventilate area immediately
2. Evacuate non-essential personnel
3. Identify and isolate source
4. Allow vapors to dissipate
5. Re-enter when safe (adequate oxygen level)

**Large Release (>5 lb):**
1. Evacuate area immediately
2. Alert emergency responders if necessary
3. Post warning signs
4. Ventilate area with mechanical exhaust
5. Monitor oxygen levels before re-entry
6. Use supplied air respirator if required

**Medical Emergency:**
- Frostbite: Warm affected area gradually with lukewarm water
- Inhalation: Move to fresh air, monitor breathing
- Seek professional medical attention
- Provide refrigerant SDS to medical personnel

### Cylinder Failures

**Overpressure Events:**
- Pressure relief valve activation
- Clear area immediately
- Allow cylinder to depressurize
- Do not approach until pressure relieved
- Identify cause (overfilling, excessive heat)

**Cylinder Damage:**
- Leaking valve or body
- Isolate cylinder in well-ventilated area
- Contact refrigerant supplier or hazmat team
- Do not attempt to transfer contents without proper equipment
- Follow local hazmat procedures

## Best Practices Summary

1. **Always recover refrigerant** before opening systems (EPA requirement)
2. **Use proper PPE** for all refrigerant handling operations
3. **Maintain EPA certification** and keep records accessible
4. **Calibrate and maintain equipment** per manufacturer specifications
5. **Follow proper charging procedures** to avoid overcharge/undercharge
6. **Perform thorough leak testing** before and after refrigerant charging
7. **Document all service** with required information
8. **Store cylinders properly** in cool, secure locations
9. **Never mix refrigerants** in recovery cylinders or systems
10. **Evacuate systems thoroughly** before refrigerant charging

## Reference Standards

- EPA Section 608 (40 CFR Part 82, Subpart F)
- AHRI 740 (Performance of Refrigerant Recovery, Recycling, and Reclamation Equipment)
- AHRI 700 (Specifications for Refrigerants)
- SAE J2788 (Refrigerant Purity and Container Requirements)
- ASHRAE Standard 15 (Safety Standard for Refrigeration Systems)
- DOT 49 CFR (Hazardous Materials Transportation)
- OSHA 29 CFR 1910 (Occupational Safety Standards)
