---
title: "Unit Ventilators, Heaters, and Makeup Air Equipment"
description: "Comprehensive guide to unit ventilators, unit heaters, makeup air units, and destratification systems for commercial and industrial HVAC applications."
date: "2026-01-04"
weight: 10
tags: ["unit ventilator", "unit heater", "makeup air unit", "destratification", "space heating", "ventilation equipment"]
categories: ["Heating Systems"]
---

Unit equipment represents a category of HVAC devices that combine heating, cooling, and ventilation functions in factory-assembled packages designed for specific space conditioning applications. These systems differ from central air handling systems by serving localized zones with self-contained controls and minimal field assembly.

## Unit Equipment Categories

**Unit Ventilators** integrate outdoor air ventilation with heating and optional cooling in a single cabinet. Classroom applications dominate this market segment, where variable outdoor air dampers enable economizer operation while maintaining minimum ventilation rates. The face-and-bypass damper arrangement allows capacity modulation without airflow variation, critical for maintaining acoustic comfort in educational spaces.

**Unit Heaters** provide space heating through forced convection without mechanical cooling capability. Horizontal propeller fan units deliver high throw distances for industrial and warehouse applications. Vertical downflow units with centrifugal fans suit retail and commercial spaces requiring quieter operation and more uniform distribution patterns.

**Makeup Air Units** replace air exhausted from buildings by kitchen hoods, laboratory fume hoods, paint booths, and industrial processes. These systems handle 100% outdoor air and may incorporate tempering (minimal heating), full conditioning (heating and cooling), or direct-fired burners that add combustion products to the supply airstream for maximum efficiency.

**Destratification Fans** reduce thermal stratification in high-bay spaces by circulating warm ceiling air downward to occupied zones. Slow-speed operation minimizes drafts while capturing otherwise wasted heat, reducing heating energy consumption by 20-30% in facilities with ceiling heights exceeding 20 feet.

## Operating Principles

Unit equipment operates on the principle of localized conditioning rather than centralized distribution. Each unit serves a defined zone with independent controls responding to local conditions. This architecture offers several thermodynamic and practical advantages.

The equipment eliminates long duct runs and associated pressure losses. Distribution losses for unit equipment typically range from 5-10% compared to 15-25% for central systems with extensive ductwork. Shorter air paths also reduce fan energy requirements, though multiple smaller fans may consume more total power than a single large fan depending on static efficiency.

Zone-level control enables temperature and ventilation setpoints tailored to occupancy patterns and heat gain characteristics of each space. A classroom unit ventilator responds to occupancy sensors and CO₂ levels independent of adjacent rooms, optimizing ventilation air delivery rather than maintaining building-wide minimum outdoor air fractions.

## Capacity and Sizing

Unit equipment sizing follows load calculation procedures similar to central systems but emphasizes peak zone loads rather than diversified building loads. The absence of load diversity means equipment operates closer to full capacity during design conditions.

Heating capacity for steam and hot water units follows the fundamental heat transfer equation:

$$Q_h = \dot{m} c_p \Delta T = \text{CFM} \times 1.08 \times \Delta T$$

where the 1.08 factor converts CFM to mass flow rate and includes specific heat for standard air. Gas-fired unit heaters use combustion efficiency and fuel heating value:

$$Q_{out} = \dot{m}_{gas} \times \text{HHV} \times \eta_c$$

Direct-fired makeup air units achieve 90-95% efficiency by adding combustion products to the airstream, while indirect-fired units lose 10-15% through flue gas exhaust.

## Application Selection Criteria

Equipment selection balances first cost, operating cost, space constraints, and functional requirements. The decision matrix includes:

**Unit Ventilators**: Perimeter spaces requiring continuous ventilation with occupancy-based control. Schools, offices, and healthcare patient rooms benefit from dedicated outdoor air delivery and individual room temperature control.

**Unit Heaters**: High-bay warehouses, manufacturing facilities, loading docks, and spaces with minimal cooling requirements. Applications tolerate moderate noise levels and non-uniform temperature distribution in exchange for low first cost and simple installation.

**Makeup Air Units**: Any facility with significant exhaust requirements. Kitchen exhaust demands immediate replacement to prevent negative building pressure. Laboratory and industrial exhaust often contains contaminants requiring dedicated outdoor air rather than recirculated building air.

**Destratification Fans**: Spaces with ceiling heights above 20 feet and significant heating loads. ROI improves with higher heating costs, greater ceiling heights, and longer heating seasons.

## Control Integration

Modern unit equipment incorporates DDC controls communicating via BACnet or Modbus protocols. Integration with building automation systems enables:

- Coordinated startup and shutdown sequences
- Demand-based ventilation using occupancy and CO₂ sensors
- Economizer optimization across multiple units
- Alarm monitoring for filter pressure, freeze protection, and equipment status
- Trending of operating parameters for commissioning and diagnostics

The distributed nature of unit equipment creates redundancy. A single central air handler failure affects an entire building, while unit equipment failures impact only the served zone. This characteristic makes unit equipment attractive for critical facilities requiring operational continuity.

## Energy Considerations

Unit equipment energy performance depends on component efficiency and control strategy rather than equipment type. High-efficiency motors (IE3 or better), low-pressure-drop coils, and modulating controls reduce fan energy. Multiple units cycling on and off waste more energy than fewer units with capacity modulation.

Economizer capability in unit ventilators and makeup air units provides free cooling when outdoor conditions permit. Properly tuned economizer controls deliver 500-1500 hours of free cooling annually in temperate climates, reducing mechanical cooling energy by 20-40%.

Direct-fired makeup air represents the most efficient heating method for 100% outdoor air applications, converting 90-95% of fuel energy to useful heating compared to 80-85% for indirect-fired units after accounting for distribution losses. However, direct-fired units add combustion products (CO₂ and water vapor) to supply air, limiting applications to spaces tolerating elevated CO₂ levels.

Unit equipment continues evolving with variable-speed drives, advanced controls, and integration with heat recovery systems. The fundamental advantages of localized conditioning, simple installation, and zone-level control ensure ongoing relevance across commercial and industrial applications.
