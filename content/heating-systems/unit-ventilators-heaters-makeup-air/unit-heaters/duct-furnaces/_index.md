---
title: "Duct Furnaces"
description: "Engineering guide to duct furnaces for in-duct heating including gas-fired and electric configurations, draw-through vs blow-through arrangements, and control strategies."
date: "2026-01-04"
weight: 3
tags: ["duct furnace", "in-duct heating", "draw through", "blow through", "electric duct heater", "gas duct furnace"]
categories: ["Heating Systems"]
---

Duct furnaces install within ductwork to heat air supplied by separate fans, contrasting with unit heaters that integrate fans and heating elements in single cabinets. The configuration suits makeup air systems, rooftop unit add-on heating, process air heating, and applications requiring heating capacity beyond what packaged equipment provides. Duct furnaces range from small electric resistance heaters (5-50 kW) to large gas-fired units (500-5000 MBH).

## Configuration Types

### Draw-Through Arrangement

Draw-through duct furnaces mount downstream of the fan, heating air after fan discharge. The fan pushes air through the heating section, creating positive pressure throughout the duct furnace.

Advantages:

- **Uniform air distribution** across heating elements from fan discharge turbulence
- **No fan overheating** since fan operates in cool air upstream
- **Better temperature stratification** prevention through pre-mixing
- **Simpler installation** with standard duct connections

Disadvantages:

- **Higher static pressure** from heating element resistance affects fan performance
- **Limited turndown** on electric heaters if poor air distribution causes hotspots
- **Longer ductwork** runs since furnace adds length after fan

Draw-through represents the standard configuration for most applications where fan selection accounts for heating section pressure drop.

### Blow-Through Arrangement

Blow-through furnaces mount upstream of the fan, with the fan pulling air through the heating section. The heating elements operate under negative pressure relative to the fan suction.

Advantages:

- **Fan selection independence** from heating pressure drop
- **Compact installation** placing furnace directly at air intake
- **Improved mixing** as heated air passes through fan impeller
- **Easier maintenance access** with heating elements before fan housing

Disadvantages:

- **Fan temperature limits** requiring heat-resistant motors and bearings
- **Air distribution sensitivity** demanding uniform air entry to heating section
- **Control complexity** coordinating heating and fan operation
- **Safety concerns** if fan failure leaves energized heating elements in stagnant air

Blow-through configurations suit specialized applications requiring specific airflow patterns or installation constraints.

## Electric Duct Furnaces

Electric duct furnaces use resistance heating elements (tubular, open coil, or finned) to heat passing air. Power ranges from 5 kW (17,000 Btu/hr) for small units to 500 kW (1,700 MBH) for large commercial systems.

### Heating Element Types

**Tubular elements** encase resistance wire in metal sheaths filled with magnesium oxide insulation. The robust construction withstands vibration and thermal cycling. Power density ranges from 15-40 watts per square inch of element surface area.

**Open coil elements** expose resistance wire directly to airstream, maximizing heat transfer. Lower first cost and faster response suit applications with rapid load changes. Service life decreases compared to tubular elements due to oxidation and mechanical stress.

**Finned tubular elements** add aluminum or steel fins to tubular elements, increasing surface area for equivalent capacity with lower element temperatures. The lower surface temperatures (500-700°F vs 800-1100°F for bare tubular) improve element life and reduce downstream temperature stratification.

### Capacity and Staging

Total capacity equals:

$$Q_{electric} = \text{kW} \times 3412 \text{ Btu/hr per kW}$$

A 150 kW duct furnace provides:

$$Q = 150 \times 3412 = 511,800 \text{ Btu/hr}$$

Staging divides capacity into multiple circuits controlled independently. Common configurations:

- **Two-stage**: 50%/50% split enables 0%, 50%, 100% capacity
- **Three-stage**: 33%/33%/33% enables 0%, 33%, 67%, 100% capacity
- **Proportional staging**: Unequal stages (25%/25%/50%) provide finer modulation

The temperature rise relates to capacity and airflow:

$$\Delta T = \frac{\text{kW} \times 3412}{\text{CFM} \times 1.08}$$

For 150 kW heating 5,000 CFM:

$$\Delta T = \frac{150 \times 3412}{5000 \times 1.08} = 95°F$$

This substantial temperature rise requires proper downstream mixing to prevent stratification and occupant discomfort.

### Electrical Requirements

Electric duct furnaces require substantial electrical service:

- **Voltage**: 208V, 240V, 480V, or 600V three-phase (large units)
- **Current**: 150 kW at 480V draws 180A (I = 150,000W / (480V × 1.732 × 0.95 pf))
- **Wire sizing**: #3/0 copper or #250 kcmil aluminum for 200A service
- **Circuit breakers**: HACR-rated breakers sized at 125% of full-load current

The electrical demand makes electric duct furnaces expensive to operate in regions with high electricity costs ($0.12-0.30 per kWh). Operating cost for the 150 kW unit:

$$\text{Cost/hr} = 150 \text{ kW} \times \$0.15/\text{kWh} = \$22.50/\text{hr}$$

Natural gas at $1.00 per therm provides equivalent heating for approximately $6.00 per hour, explaining why gas-fired units dominate large commercial applications despite higher first cost.

## Gas-Fired Duct Furnaces

Gas-fired duct furnaces burn natural gas or propane in tubular or heat exchanger assemblies integrated into duct sections. Capacities range from 100 MBH for small commercial units to 5000 MBH for industrial process heating.

### Heat Exchanger Design

**Tubular heat exchangers** route flue gases through stainless steel or aluminized steel tubes while air passes across tube exteriors. The counterflow or crossflow arrangement maximizes heat transfer. Tube counts range from 6-60 depending on capacity.

Heat transfer effectiveness:

$$\epsilon = \frac{T_{air,out} - T_{air,in}}{T_{flue,in} - T_{air,in}}$$

For well-designed heat exchangers, effectiveness reaches 70-85%, converting 80-90% of fuel energy to useful air heating after accounting for combustion losses and flue gas discharge.

**Direct-fired heat exchangers** burn fuel directly in the airstream without separating combustion products from supply air. This configuration achieves 90-100% thermal efficiency by eliminating flue gas losses. Applications limited to:

- Makeup air systems diluting combustion products with large outdoor air quantities
- Industrial processes tolerating CO₂ and water vapor in supply air
- Temporary heating where efficiency outweighs air quality concerns

Direct-fired units require special permitting and code approval for occupied space applications.

### Burner Types and Controls

**Atmospheric burners** use natural draft for combustion air, operating at near-ambient pressure. Thermal efficiency reaches 80-85%. Simple construction and low first cost make atmospheric burners standard for light commercial applications.

**Power burners** use fans to supply combustion air, enabling higher firing rates and better turndown. Efficiency improves to 85-92% through optimized air-fuel ratios across the operating range.

**Modulating burners** vary fuel input from 20-100% of rated capacity using motorized gas valves and variable-speed combustion air fans. The 5:1 turndown enables precise capacity matching without cycling, improving comfort and efficiency.

### Venting Requirements

Gas-fired duct furnaces require flue gas venting sized for capacity and configuration:

- **Category I (80-85% efficiency)**: Type B vent or chimney with natural draft
- **Category IV (90-95% efficiency)**: PVC or stainless steel with induced-draft fan

Vent sizing follows manufacturer tables accounting for:
- Heat input (MBH)
- Vent height and configuration (vertical vs horizontal)
- Number of elbows and fittings
- Altitude correction factors

A 500 MBH Category I unit requires a 12-inch diameter Type B vent with minimum 15 feet of vertical rise for adequate draft. Category IV condensing units use 8-inch PVC with induced-draft fans overcoming resistance in 100+ foot horizontal runs.

## Safety Controls and Interlocks

Duct furnaces incorporate multiple safety controls preventing equipment damage and fire hazards:

### Airflow Proving

**Differential pressure switches** monitor static pressure across the fan or heating section. The switch prevents burner or heater energization unless adequate airflow exists. Settings typically require 0.1-0.3 inches water gauge differential for proof of airflow.

**Sail switches** use a lightweight vane extending into the airstream. Airflow deflects the vane, closing a switch contact. Lower accuracy than pressure switches but simpler installation and lower cost.

### High Limit Temperature Control

**Limit thermostats** mount downstream of heating elements, de-energizing heat sources if discharge temperature exceeds setpoint. Settings range from 110-180°F depending on application:

- **Occupied space heating**: 110-140°F prevents discomfort
- **Process heating**: 150-200°F for industrial applications
- **Freeze protection**: 35-50°F for minimum heat output

Manual reset limits provide backup protection, requiring physical reset after high-temperature events to prevent automatic restart of failed equipment.

### Flame Safeguard Controls

Gas-fired units use flame safeguard controls monitoring burner operation:

- **Direct spark ignition**: Electronic igniter lights burner while flame sensor proves ignition
- **Flame rod**: Current rectification between flame and ground proves combustion
- **Ultraviolet scanner**: Optical sensor detects UV radiation from flame

Failed ignition or flame loss triggers burner lockout, requiring manual reset after fault correction.

## Application Comparison: Duct Furnace vs Unit Heater

| Characteristic | Duct Furnace | Unit Heater |
|----------------|--------------|-------------|
| Fan Integration | Separate fan required | Integral fan |
| Installation | In-duct, hidden | Exposed, ceiling/wall mounted |
| Air Distribution | Ducted throughout space | Direct discharge from unit |
| Temperature Uniformity | Excellent with proper duct design | Moderate, dependent on throw |
| First Cost | Higher (includes ductwork) | Lower (standalone unit) |
| Energy Efficiency | Better (controlled distribution) | Lower (mixing losses) |
| Noise Level | Lower (remote from occupied space) | Higher (unit in space) |
| Maintenance Access | Requires duct access | Direct access from floor |

Duct furnaces suit applications requiring uniform temperature distribution, low noise levels, and architectural concealment. Unit heaters provide economical heating for spaces tolerating visible equipment and moderate noise.

## Sizing and Selection

Duct furnace capacity selection follows load calculations for the served space. Unlike standalone furnaces that may include built-in oversizing, duct furnaces should match calculated loads closely since staging controls provide capacity modulation.

Airflow sizing considers temperature rise limits:

$$\text{CFM}_{min} = \frac{Q_{heating}}{1.08 \times \Delta T_{max}}$$

For a 400 MBH gas-fired unit with 100°F maximum temperature rise:

$$\text{CFM}_{min} = \frac{400,000}{1.08 \times 100} = 3,704 \text{ CFM}$$

Select fans delivering at least this airflow accounting for heating section pressure drop (typically 0.3-0.8 inches water gauge for gas-fired units, 0.1-0.4 for electric units).

Cabinet sizing accommodates duct dimensions while meeting clearance requirements. Duct furnaces require:

- **Upstream straight duct**: 3-5 duct diameters for uniform air distribution
- **Downstream straight duct**: 2-3 duct diameters for temperature stabilization
- **Clearances to combustibles**: 6-36 inches depending on unit capacity and insulation

Duct furnaces provide flexible heating solutions for applications requiring in-duct air tempering. The variety of fuel sources, capacity ranges, and configurations enables heating system designs matching diverse architectural and functional requirements.
