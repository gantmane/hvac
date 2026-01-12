---
title: "Plug Load Management"
weight: 4
---

Plug loads represent 20-40% of total building electricity consumption in commercial buildings. These loads include all devices that plug into standard electrical outlets: computers, monitors, printers, task lighting, coffee makers, microwaves, and miscellaneous equipment. Unlike regulated loads such as HVAC and lighting, plug loads are growing rapidly and lack comprehensive code requirements.

## Plug Load Assessment

Comprehensive assessment quantifies energy consumption and identifies reduction opportunities.

### Inventory Development

Create detailed equipment inventory:
- Equipment type and model
- Quantity per zone or floor
- Rated power (nameplate watts)
- Operating hours per day
- Occupancy correlation
- Energy Star status

### Power Monitoring

Direct measurement provides actual consumption data:

**Temporary Metering**
- Plug-level power meters (0.5-2% accuracy)
- Data logging interval: 15 minutes minimum
- Measurement duration: 1-2 weeks typical
- Capture operational modes: active, idle, sleep, off

**Permanent Monitoring**
- Branch circuit meters for plug loads
- Integration with building management system
- Continuous tracking and trending
- Automated anomaly detection

### Consumption Calculations

Estimate annual energy use:

| Equipment | Power (W) | Hours/Day | Days/Year | Annual kWh |
|-----------|-----------|-----------|-----------|------------|
| Desktop PC | 80 | 10 | 250 | 200 |
| Monitor (24") | 25 | 10 | 250 | 63 |
| Laser Printer | 400 | 2 | 250 | 200 |
| Task Light | 10 | 8 | 250 | 20 |
| Coffee Maker | 1000 | 1 | 250 | 250 |

Total daily plug load density: 5-15 W/ft² in office buildings.

### Load Profiles

Analyze temporal consumption patterns:
- Peak demand periods (8 AM - 5 PM typical)
- After-hours baseload (should be <10% of peak)
- Weekend consumption (indicates control issues)
- Seasonal variations

## Advanced Power Strips

Smart power strips reduce standby power consumption and provide automatic control.

### Tier 1 Power Strips

Basic surge protection with manual switching:
- Individual outlet switches
- Master on/off switch
- 15A capacity typical
- Minimal energy savings (<5%)

### Tier 2 Power Strips

Load-sensing technology:
- Master outlet controls peripheral outlets
- Senses master device power state
- Threshold: 10-30W typical
- Auto-shutoff peripheral devices when master is off
- Energy savings: 20-35%

**Applications:**
- Computer workstations (PC as master, monitor/speakers as peripherals)
- Entertainment systems (TV as master, cable box/speakers as peripherals)
- Printer stations (primary printer as master)

### Advanced Power Strips (APS)

Occupancy and schedule-based control:
- Integrated occupancy sensors (PIR or ultrasonic)
- Programmable time schedules
- Individual outlet control
- Network connectivity for remote management
- Energy savings: 35-60%

**Control Strategies:**
- Vacancy mode: Outlets shut off after occupancy timeout (15-30 minutes)
- Schedule override: Manual button for after-hours use
- Always-on outlets for critical equipment
- Countdown timers for equipment warmup/shutdown

### Network-Controlled Power Distribution

Enterprise-level management:
- Centralized monitoring and control
- Remote on/off switching
- Real-time power metering per outlet
- Integration with building automation
- User authentication and access control
- Cost: $500-2000 per 20-outlet unit

## Occupancy-Based Control

Automated control based on space occupancy reduces unnecessary runtime.

### Detection Technologies

**Passive Infrared (PIR)**
- Detects thermal motion
- Range: 20-30 feet
- Best for small offices and workstations
- False-off rate: <5% when properly located
- Cost: $20-50 per sensor

**Ultrasonic Sensors**
- Detects physical motion via sound reflection
- Coverage: 400-600 ft²
- Better for partitioned spaces
- Potential for false-on from HVAC airflow
- Cost: $30-80 per sensor

**Dual-Technology Sensors**
- Combines PIR and ultrasonic
- Requires both technologies to confirm occupancy
- Lowest false-on/false-off rates
- Cost: $50-150 per sensor

### Control Zones

Define zones based on occupancy patterns:

**Individual Workstations**
- Personal control for each workspace
- Quick response time (1-2 minute timeout)
- User override capability
- Appropriate for: task lighting, monitors, docking stations

**Shared Spaces**
- Conference rooms, break rooms, copy rooms
- Longer timeout (10-20 minutes)
- Multiple sensor coverage for reliability
- Appropriate for: projectors, monitors, printers, coffee makers

**24/7 Equipment**
- Server rooms, telecom closets
- Exclude from occupancy control
- Continuous operation required
- Focus on equipment efficiency instead

### Timeout Settings

Balance energy savings with occupant convenience:

| Space Type | Recommended Timeout |
|------------|---------------------|
| Private office | 15 minutes |
| Open office workstation | 10 minutes |
| Conference room | 20 minutes |
| Break room | 30 minutes |
| Copy/print room | 20 minutes |

## Equipment Procurement Standards

Establish procurement policies to reduce plug load energy consumption.

### Energy Star Requirements

Mandate Energy Star certification for eligible equipment:

**Computers**
- 25-40% more efficient than standard
- TEC (Typical Energy Consumption) metric
- Advanced power management
- Sleep mode <2W for desktops

**Monitors**
- 25% more efficient than standard
- On-mode efficiency requirements
- Sleep mode <0.5W
- Auto-brightness control

**Imaging Equipment**
- Printers, copiers, multifunction devices
- TEC requirements based on speed and capability
- Sleep mode <5W
- Auto-off after inactivity

**Appliances**
- Refrigerators, dishwashers, water coolers
- 10-50% more efficient depending on category
- Focus on break room equipment

### Total Cost of Ownership

Evaluate lifecycle costs, not just purchase price:

TCO = Purchase Price + (Annual kWh × kWh Rate × Years) + Maintenance

**Example: Desktop Computer**
- Standard desktop: $600 purchase, 200 kWh/year
- Energy Star desktop: $650 purchase, 120 kWh/year
- Electricity rate: $0.12/kWh
- 5-year lifecycle

Standard TCO: $600 + (200 × $0.12 × 5) + $100 = $820
Energy Star TCO: $650 + (120 × $0.12 × 5) + $80 = $802

Energy Star saves $18 over lifecycle despite higher purchase price.

### Thin Client Computing

Replace desktop PCs with thin clients:
- Power consumption: 5-15W vs. 60-100W for desktop
- Centralized processing in data center
- Energy savings: 80-90% at workstation
- Shifts load to data center (requires efficient servers)
- Capital cost: $200-400 per thin client
- Appropriate for: task-oriented work, secure environments

### Right-Sizing Equipment

Specify appropriate capacity:
- Match monitor size to task requirements (21-24" sufficient for most office work)
- Avoid oversized imaging equipment in low-volume areas
- Select appropriate refrigerator size for actual need
- Eliminate redundant devices (consolidate printers)

## Cooling Impact Reduction

Plug loads generate internal heat that increases cooling requirements.

### Heat Gain Calculations

Internal heat gain from plug equipment:

Q = 3.41 × W × Fd × Fr

Where:
- Q = heat gain (Btu/hr)
- W = equipment watts
- Fd = diversity factor (0.5-0.9 depending on simultaneous use)
- Fr = radiant fraction (0.6-0.8 typical)
- 3.41 = conversion factor (W to Btu/hr)

**Example:**
Open office: 100 workstations, 150W average each
Q = 3.41 × (100 × 150) × 0.7 × 0.7 = 25,100 Btu/hr = 2.1 tons cooling

### Cooling Load Multiplier

Account for cooling energy to remove plug load heat:

Total Impact = Plug Load Energy × (1 + COP⁻¹)

For COP = 3.5:
Total Impact = Plug Load Energy × 1.29

Every 1 kWh of plug load energy requires 0.29 kWh of cooling energy.

**Annual Savings Example:**
Reduce plug loads by 10,000 kWh/year
Direct savings: 10,000 kWh
Cooling savings: 10,000 × 0.29 = 2,900 kWh
Total savings: 12,900 kWh

At $0.12/kWh: $1,548 annual savings

### Heat Distribution

Consider thermal impacts:

**Direct Equipment Heat**
- 40-60% convective (immediate cooling load)
- 40-60% radiant (absorbed by surfaces first)
- Radiant heat becomes cooling load with delay (30-90 minutes)

**Location Impact**
- Perimeter zones: Heat may offset heating needs in winter
- Interior zones: Always increases cooling requirement
- Density matters: High plug load density creates hot spots

### Ventilation Requirements

Plug load heat affects air distribution:
- Higher heat gains require increased airflow
- Typical office: 1 CFM per 1-2 ft²
- High plug load areas: 1 CFM per 0.8-1.5 ft²
- Under-ventilated spaces develop temperature stratification

## Implementation Strategies

Successful plug load management requires comprehensive approach.

### Baseline Establishment

Quantify current consumption:
- Conduct plug load audit
- Measure representative sample (10-20% of equipment)
- Extrapolate to whole building
- Document baseline kWh and cost

### Phased Rollout

Implement in stages:

**Phase 1: Low-Cost Measures**
- Equipment shutdown policy
- Power management settings
- Occupant education
- Cost: <$1 per ft²
- Savings: 5-15%

**Phase 2: Moderate Investment**
- Advanced power strips
- Occupancy controls
- Timer controls
- Cost: $1-3 per ft²
- Savings: 15-30%

**Phase 3: Equipment Replacement**
- Energy Star procurement
- Thin client deployment
- Equipment consolidation
- Cost: $5-15 per ft²
- Savings: 30-50%

### Occupant Engagement

User behavior significantly impacts savings:
- Training on power management features
- Visual feedback on consumption
- Recognition programs for low consumers
- Policy enforcement for non-compliance
- Monthly energy reports by department

### Performance Tracking

Monitor results:
- Monthly plug load energy consumption
- Comparison to baseline and goals
- Identify areas of non-compliance
- Adjust controls based on actual use patterns
- Document savings for continued funding support

### Maintenance Requirements

Sustain performance:
- Quarterly checks of control settings
- Annual verification of occupancy sensor operation
- Replace failed power strips promptly
- Update equipment inventory as changes occur
- Review and update procurement standards annually

## Savings Potential

Typical energy and cost reductions:

| Strategy | Energy Savings | Simple Payback |
|----------|----------------|----------------|
| Power management settings | 10-20% | <1 year |
| Advanced power strips | 15-25% | 1-2 years |
| Occupancy controls | 20-35% | 2-3 years |
| Energy Star equipment | 25-40% | 3-5 years |
| Comprehensive program | 40-60% | 3-5 years |

Plug load management delivers measurable energy savings, reduced cooling costs, and improved power quality. The combination of efficient equipment procurement, automated controls, and occupant engagement provides the greatest return on investment.
