---
title: "University and College HVAC Systems"
description: "Technical guide to campus district heating and cooling, laboratory ventilation, lecture hall HVAC, library climate control, research facilities, and dormitory systems with ASHRAE standards."
keywords: ["university HVAC", "college HVAC systems", "campus district energy", "laboratory ventilation", "lecture hall HVAC", "library climate control", "research facility HVAC", "dormitory heating cooling", "campus chilled water", "campus steam system"]
weight: 2
---

University and college campuses present complex HVAC challenges due to diverse building types, research requirements, occupancy variations, and centralized energy infrastructure. Proper system design balances comfort, energy efficiency, indoor air quality, and specialized environmental controls across multiple facility categories.

## Campus District Energy Systems

Central heating and cooling plants serve multiple buildings through underground distribution networks, providing operational efficiency and fuel flexibility.

### Chilled Water Distribution

Campus chilled water systems typically operate at 42-45°F supply temperature with 12-16°F ΔT. Distribution pipe sizing follows velocity limits of 4-8 ft/s to minimize pumping energy while preventing erosion. Primary-secondary or variable primary flow configurations optimize part-load performance across buildings with different load profiles.

**Critical design parameters:**

| Parameter | Typical Range | Design Consideration |
|-----------|--------------|---------------------|
| Supply temperature | 42-45°F | Lower temps reduce pipe sizes but increase chiller energy |
| ΔT | 12-16°F | Higher ΔT reduces flow rates and pumping energy |
| Pipe insulation | R-6 to R-10 | Minimize heat gain in underground distribution |
| Pressure class | 150-300 psi | Account for elevation changes and pump head |

Decoupling buildings with heat exchangers prevents operational issues when system pressures exceed building equipment ratings. Differential pressure control maintains optimal flow distribution across the campus loop.

### Steam and Hot Water Systems

Many established campuses use medium-pressure steam (50-150 psig) for heating, sterilization, and process loads. Steam distribution requires proper pitch (1 in per 20 ft minimum), steam trap maintenance, and condensate return systems. High-temperature hot water (250-400°F) offers superior heat retention for long distribution runs but demands expansion compensation and pressure safety controls.

Conversion from steam to hot water reduces distribution losses by 30-50% while improving controllability. The transition requires building-level heat exchangers and pump upgrades.

## Laboratory Buildings

Research and teaching laboratories demand 100% outdoor air with no recirculation to prevent cross-contamination and maintain safety. ASHRAE 62.1 specifies minimum ventilation rates, but laboratory-specific standards (ANSI/AIHA Z9.5) govern fume hood and equipment exhaust requirements.

### Ventilation Requirements

Laboratory air change rates range from 6-12 ACH minimum, with higher rates for high-hazard spaces. The total ventilation load combines:

- Fume hood face velocity requirements (80-120 fpm typical)
- General exhaust for odor and vapor dilution
- Make-up air to maintain space pressure relationships
- Equipment cooling and process exhaust

Each fume hood at 100 fpm face velocity exhausts approximately 800-1200 CFM depending on sash opening. A laboratory with 6 hoods operating simultaneously requires 5000-7000 CFM exhaust plus general room ventilation.

### Variable Air Volume Laboratory Systems

VAV laboratory systems reduce energy consumption by modulating supply and exhaust based on actual fume hood usage. As hoods close, both supply and exhaust reduce proportionally while maintaining negative pressure (-0.02 to -0.05 in. w.c. relative to corridors).

Phoenix valve controls or venturi-style airflow monitors maintain constant face velocity across varying sash positions. The supply air system tracks exhaust reductions with a 50-100 CFM offset to preserve negative pressure.

### Energy Recovery Challenges

Laboratory exhaust contains chemical contaminants that prohibit energy recovery wheels or heat pipe heat exchangers that could transfer pollutants. Run-around glycol loop systems provide 40-60% sensible recovery without cross-contamination risk by using separate coils in supply and exhaust streams.

## Lecture Halls and Auditoriums

Large assembly spaces with tiered seating create stratification challenges and high latent loads from occupant density.

Design occupancy of 7-10 ft² per person generates 20-30 CFM outdoor air per person per ASHRAE 62.1. A 300-seat auditorium requires 6000-9000 CFM outdoor air minimum, with total supply airflow of 12,000-18,000 CFM accounting for cooling loads.

**Acoustic requirements** limit NC ratings to 25-30, demanding:

- Low face velocity diffusers (300-450 fpm)
- Duct liner or external lagging
- Fan isolation and vibration control
- Supply registers located away from microphones

Underfloor air distribution (UFAD) systems deliver supply air through floor registers in tiered seating, leveraging natural convection to improve mixing and reduce throw distances. Displacement ventilation achieves similar benefits in flat-floor configurations.

Demand-controlled ventilation using CO₂ sensors (setpoint 800-1000 ppm) reduces outdoor air during unoccupied periods while maintaining code-required rates during events.

## Libraries

Libraries require stable temperature (68-72°F) and humidity control (40-50% RH) to preserve collections while providing occupant comfort in diverse space types.

### Zoning Strategy

Different functional areas demand independent control:

- **Reading rooms**: Standard comfort conditions with low air velocities
- **Stack areas**: Tighter humidity control (±5% RH) to prevent mold growth
- **Computer labs**: Higher cooling capacity for equipment heat gains
- **Special collections**: Precision environmental control (±2°F, ±3% RH)

Constant volume systems with reheat maintain humidity control in critical zones. VAV systems serve general areas with humidity monitoring to prevent excessive drift during low-load conditions.

### Air Distribution

High ceilings in reading rooms create stratification unless properly addressed. Ceiling-mounted diffusers with horizontal throw patterns maintain occupied zone comfort without creating drafts at desk height. Supply air temperatures of 55-58°F provide adequate cooling capacity while limiting condensation risk.

## Research Facilities

Specialized research spaces include vivaria, cleanrooms, imaging suites, and equipment-intensive laboratories that exceed standard ventilation requirements.

Animal research facilities maintain 10-20 ACH with 100% outdoor air and negative pressure (-0.05 in. w.c.). Temperature setpoints of 68-72°F and 30-70% RH meet AAALAC standards while individual holding rooms may require narrower bands.

Cleanroom classifications (ISO 14644) dictate air change rates from 60 ACH (ISO Class 7) to 450 ACH (ISO Class 5) using HEPA-filtered recirculation with 5-20% outdoor air makeup. Pressurization cascades prevent contamination migration from adjacent spaces.

## Dormitories and Residence Halls

Student housing combines characteristics of multi-family residential and hotel applications with high ventilation needs and individual room control expectations.

ASHRAE 62.1 requires 5 CFM per person plus 0.06 CFM/ft² in sleeping spaces. Typical dormitory rooms (150-200 ft²) need 20-25 CFM outdoor air minimum. Continuous ventilation or occupancy-based control through CO₂ sensors maintains air quality while managing energy costs.

**System options:**

- Four-pipe fan coils provide individual temperature control with central ventilation
- DOAS with local heating/cooling separates ventilation from thermal conditioning
- Central VAV with terminal reheat offers precise control but higher first cost
- Through-wall heat pumps deliver lowest installed cost but limited dehumidification

Corridor pressurization (0.02-0.05 in. w.c. positive) relative to rooms reduces odor transfer between units. Bathroom exhaust (50 CFM minimum) operates continuously or on occupancy sensors with sufficient overrun.

## Operational Considerations

Campus HVAC systems operate under diverse schedules requiring flexible control sequences. Academic buildings experience sharp occupancy transitions between class periods, laboratories run 24/7, and dormitories follow residential patterns.

Building automation system (BAS) integration across campus enables demand response, optimal start/stop, and load shedding during peak utility periods. Submetering by building and major system reveals consumption patterns and targets retrofit opportunities.

Maintenance planning must account for summer shutdown periods when many systems undergo major service. Deferred maintenance during the academic year concentrates work into 10-14 week windows, requiring advance planning and contractor coordination.

Commissioning of new construction and major renovations follows ASHRAE Guideline 0 and Guideline 1.1 to verify performance before occupancy. Ongoing commissioning identifies degradation and optimization opportunities in existing facilities.
