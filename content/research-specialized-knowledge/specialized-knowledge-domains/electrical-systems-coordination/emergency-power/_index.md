---
title: "Emergency Power"
aliases: ["Emergency Power"]
description: "Generator sizing for HVAC loads, automatic transfer switches, legally required standby systems, and emergency power distribution strategies"
weight: 3
---

## Overview

Emergency and standby power systems maintain critical HVAC functions during utility outages, protecting building occupants, preserving environmental conditions, and preventing equipment damage. NEC Articles 700, 701, and 702 define three distinct categories of backup power: emergency systems, legally required standby systems, and optional standby systems. Each category has specific code requirements and application criteria.

## Generator Sizing for HVAC Loads

Generator sizing for HVAC applications requires careful analysis of starting inrush currents, continuous operating loads, and load sequencing strategies. The generator must supply sufficient power for the largest motor starting current while maintaining adequate voltage and frequency stability.

Starting kVA for motor loads approximates locked rotor current times rated voltage divided by 1,000. A typical motor with 6 times FLA starting current requires 6 times running kVA during start. Soft starters or variable frequency drives reduce starting current to 2-3 times FLA, permitting smaller generator sizing.

Total generator capacity uses the largest motor starting kVA plus 125% of the next largest motor FLA plus 100% of all remaining connected loads. Alternatively, sequence motor starts with time delays, permitting smaller generator sizing at the cost of extended startup time. Generator capacity should include 20-25% reserve for future loads and transient conditions.

## Load Classification and Prioritization

Emergency systems per NEC Article 700 supply loads essential for safety, including exit lighting, fire alarm systems, fire pumps, and smoke control systems. These loads receive highest priority with automatic connection within 10 seconds of utility failure. Emergency systems require two independent sources: utility plus on-site generator or battery.

Legally required standby systems per NEC Article 701 support loads mandated by code or regulation but not classified as emergency, such as smoke exhaust systems, HVAC for emergency generator rooms, and designated health care facility systems. Transfer time may extend to 60 seconds depending on application.

Optional standby systems per NEC Article 702 protect property and maintain comfort but have no life-safety or code mandate. Commercial HVAC systems typically fall into this category unless specifically required by code. These systems permit flexible transfer timing and load shedding strategies.

## Automatic Transfer Switches

Automatic transfer switches (ATS) monitor utility power quality and transfer loads to generator power when voltage or frequency fall outside acceptable limits. Modern ATS units provide programmable voltage and frequency setpoints, time delays, and bypass modes for maintenance.

Transfer timing depends on system classification: 10 seconds for emergency, 60 seconds typical for legally required standby, and variable for optional standby. Time delays prevent transfer during momentary utility disturbances. Return transfer to utility power incorporates time delay ensuring utility stability before reconnection.

ATS ratings must meet or exceed the load current with appropriate voltage and phase configuration. Three-pole switches transfer all three phases simultaneously, preventing cross-connection between sources. Four-pole switches also transfer the neutral conductor, required for separately derived generator systems per NEC 250.30.

## Load Sequencing and Management

Automatic load sequencing prevents generator overload during startup by connecting loads in predetermined sequence with time delays between steps. Critical loads energize first, followed by secondary loads at intervals permitting generator stabilization between starts.

A typical sequence includes:
1. Emergency lighting and fire alarm (immediate)
2. Smoke control fans and pressurization systems (10-15 seconds)
3. Chiller or cooling tower pump (30 seconds)
4. Second priority HVAC equipment (60 seconds)
5. Additional loads as capacity permits (90+ seconds)

Programmable load controllers automatically implement sequencing based on generator status and capacity utilization. Load shedding disconnects non-essential loads when generator capacity reaches defined limits, protecting critical systems.

## Critical HVAC Equipment Backup

Generator-backed HVAC equipment selection depends on building occupancy, mission criticality, and code requirements. Data centers require continuous cooling with N+1 redundancy on emergency power. Hospitals must maintain environmental conditions in operating rooms, intensive care units, and pharmacy storage areas.

Smoke control systems require emergency power per International Building Code when installed. The emergency power source must supply all smoke control equipment including fans, dampers, and controls. Stairwell pressurization and mechanical smoke exhaust systems depend on emergency power to maintain tenable egress conditions.

Generator room ventilation receives legally required standby power to maintain acceptable operating temperature and prevent combustion air starvation. Without adequate ventilation, generators overheat and fail during extended operation.

## Generator Types and Fuel Considerations

Diesel generators dominate stationary backup power applications due to fuel stability, reliability, and efficient long-duration operation. Diesel fuel stores indefinitely with proper additives and tank maintenance. Generator rating considers altitude derating, temperature effects, and continuous vs. standby duty cycle.

Natural gas generators eliminate on-site fuel storage requirements by connecting to utility gas service. However, earthquakes and other disasters can disrupt gas supply simultaneously with electrical outage. Dual-fuel generators provide diesel backup when gas supply fails.

Battery-based uninterruptible power systems (UPS) provide instant transfer with no interruption, suitable for computers and sensitive electronics. However, battery systems have limited capacity, typically supporting loads for 15-30 minutes. Combining UPS with generators provides both instant transfer and extended runtime.

## Electrical Distribution Architecture

Emergency power distribution employs separate panelboards or designated circuits within normal panelboards, clearly marked per NEC requirements. Wiring for emergency and legally required standby systems must maintain physical separation from normal power wiring, using separate raceways, cables, or 2-hour fire-rated assemblies.

Critical distribution switchgear often uses double-ended unit substations with utility feeds to both ends and generator connected through automatic transfer switch. This configuration provides redundancy against utility and transformer failures. Manual or automatic bus-tie breakers permit feeding entire load from single source during maintenance or outage.

Ring bus or radial distribution topologies balance initial cost against reliability requirements. Ring bus permits isolating faulted sections while maintaining power to unfaulted portions. Radial distribution costs less but creates single points of failure.

## Testing and Maintenance Requirements

NEC requires monthly generator testing under load for emergency and legally required standby systems. Testing verifies automatic transfer switch operation, load block sequencing, and adequate generator capacity. Document voltage, frequency, and load current during testing to establish performance baselines.

Annual load bank testing to rated capacity verifies the generator can support full design load while maintaining voltage and frequency within specified limits. Load bank testing also prevents wet stacking in diesel engines by operating at high load, burning off carbon deposits and unburned fuel.

Fuel quality testing analyzes diesel fuel for water contamination, bacterial growth, and chemical degradation. Fuel polishing removes water and particulates, extending fuel life. Biocide additives prevent bacterial growth. Replace aged fuel every 2-3 years even with treatment.

## Coordination with Utility Systems

Utility interconnection requirements prevent generator backfeed into utility lines during outages, protecting line workers. Transfer switches provide electrical interlocking preventing simultaneous connection to utility and generator. Utility notification of on-site generation may be required depending on capacity and jurisdiction.

Paralleling generators with utility power requires protective relaying preventing reverse power flow, synchronization controls matching frequency and phase angle, and utility approval. Grid-parallel operation permits peak shaving and demand response but adds significant complexity and cost.

Renewable energy systems with battery storage increasingly serve backup power functions. Solar photovoltaic systems with battery banks provide emergency power during daytime while reducing utility consumption during normal operation. Battery capacity determines backup duration when solar production is unavailable.
