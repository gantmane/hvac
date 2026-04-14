---
title: "Demand Response"
aliases: ["Demand Response"]
description: "HVAC demand response fundamentals including load shedding and load shifting strategies, pre-cooling thermal mass utilization, grid integration programs, control strategies for DR events, and economic incentive structures for commercial building applications."
weight: 3
---

Demand response represents a strategic approach to managing electric grid loads by modifying HVAC system operation during periods of high electricity demand or grid stress. HVAC systems account for 40-60% of commercial building electric demand, making them primary targets for demand response programs that reduce peak loads while maintaining acceptable indoor environmental quality.

## Demand Response Fundamentals

Demand response in HVAC applications involves temporary modifications to system operation in response to utility signals, price changes, or grid conditions. The fundamental objective is reducing electrical demand during critical peak periods, typically 2-6 hours duration, when wholesale electricity prices spike or grid reliability becomes compromised.

HVAC systems offer significant demand response potential due to their high energy consumption, controllability, and inherent thermal storage capacity in building mass. The building envelope and interior mass function as passive thermal storage, allowing temporary reductions in cooling or heating without immediate impacts on occupant comfort.

Peak demand reduction potential ranges from 15-40% of HVAC load depending on building thermal mass, insulation quality, system design, and control strategy sophistication. This translates to 10-25% of total building electrical demand in typical commercial applications.

## Load Shedding Strategies

Load shedding involves direct reduction of HVAC system power consumption during demand response events through equipment cycling, capacity limitation, or complete shutdown of non-critical systems.

**Compressor Cycling:**
Reciprocating and scroll compressors can be cycled on/off during DR events, reducing runtime to 50-75% of normal operation. Cycling periods of 15-30 minutes on, 10-20 minutes off maintain partial cooling while reducing demand by 20-35%. Excessive cycling reduces compressor life and requires minimum on-time protection.

**Capacity Limitation:**
Variable capacity systems reduce cooling output to 60-80% of full capacity rather than complete shutdown. Screw compressor slide valves, scroll compressor unloaders, and VFD-controlled compressors provide continuous modulation. This approach maintains some cooling while reducing peak demand 20-40% with less thermal drift than full cycling.

**Fan Speed Reduction:**
Supply and condenser fan VFDs reduce airflow to minimum ventilation requirements during DR events. Fan power follows cube law relationship, so reducing speed to 70% yields 34% power reduction (0.7³ = 0.343). Combined with capacity reduction, fan speed modulation provides 30-50% total system demand reduction.

**Chilled Water Reset:**
Raising chilled water temperature setpoint from 44°F to 50-52°F during DR events reduces chiller power 10-20% while maintaining partial cooling. This strategy works best with systems having excess coil capacity and moderate latent loads.

## Load Shifting Strategies

Load shifting relocates energy consumption from peak to off-peak periods through pre-cooling, thermal storage charging, or delayed operation. This approach reduces peak demand without necessarily reducing total energy consumption.

### Pre-Cooling Operations

Pre-cooling leverages building thermal mass as passive storage by over-cooling the building 2-4 hours before anticipated DR events. The building structure absorbs sensible cooling during off-peak periods, then releases this stored cooling during the event as indoor temperatures drift upward.

Pre-cooling effectiveness depends on thermal mass quantity and accessibility:

| Building Type | Thermal Mass | Pre-Cool Duration | Temperature Drift | DR Duration |
|---------------|--------------|-------------------|-------------------|-------------|
| Heavy concrete | High | 3-4 hours | 2-3°F | 4-6 hours |
| Steel frame, drywall | Medium | 2-3 hours | 3-5°F | 2-4 hours |
| Light construction | Low | 1-2 hours | 4-6°F | 1-2 hours |

Pre-cooling setpoint depression ranges from 3-5°F below normal, reducing space temperature to 70-72°F before the DR event. Excessive pre-cooling wastes energy and creates occupant discomfort. The pre-cooling energy penalty typically equals 10-25% additional consumption but shifts this load to off-peak periods with lower electricity costs.

Optimal pre-cooling requires accurate forecasting of DR event timing, outdoor conditions, and building thermal response. Model predictive control algorithms calculate pre-cooling start time and setpoint based on building thermal model, weather forecast, and DR event schedule.

### Thermal Mass Utilization

Building thermal mass stores sensible heat, providing 15-40 Btu/ft²·°F of effective storage capacity depending on construction:

- Concrete structure: 30-40 Btu/ft²·°F
- Masonry walls: 25-35 Btu/ft²·°F
- Gypsum board: 8-12 Btu/ft²·°F
- Furnishings and contents: 5-10 Btu/ft²·°F

Total building thermal capacitance ranges from 50-100 Btu/ft²·°F for light construction to 150-250 Btu/ft²·°F for heavy concrete buildings. A 50,000 ft² building with 150 Btu/ft²·°F thermal mass stores 7.5 million Btu per degree F temperature change.

Thermal mass effectiveness requires good thermal coupling between conditioned air and mass surfaces. Exposed concrete ceilings, masonry walls, and concrete floors provide direct thermal contact. Suspended ceilings and carpeting insulate mass from conditioned space, reducing effectiveness by 40-60%.

Night ventilation purges stored heat from thermal mass in cooling-dominated climates, improving next-day pre-cooling effectiveness. Drawing outdoor air through the building during cool nighttime hours (60-70°F) removes heat absorbed during the day, resetting mass temperature for the following cycle.

## Grid Integration and Utility Programs

Demand response programs connect building HVAC systems to utility grid management through various participation structures and compensation mechanisms.

**Direct Load Control (DLC):**
Utilities remotely control customer HVAC equipment during peak events through installed controllers or building automation system integration. Customers receive upfront incentives ($50-200 per kW of controllable load) plus annual participation payments. Control events typically limited to 15-20 per year, 2-4 hours each.

**Automated Demand Response (AutoDR):**
Building automation systems respond automatically to utility price or event signals via OpenADR protocol communication. Systems execute pre-programmed DR strategies without manual intervention. AutoDR enables faster response and eliminates human error or inaction during events.

**Time-of-Use (TOU) Pricing:**
Electricity rates vary by time period, creating economic incentive for load shifting. Peak period rates (2-6 PM) range from $0.15-0.45/kWh while off-peak rates (10 PM-6 AM) drop to $0.04-0.10/kWh. Rate differential of 3:1 to 5:1 justifies pre-cooling and thermal storage strategies.

**Critical Peak Pricing (CPP):**
Extreme price surcharges ($0.50-1.50/kWh) apply during 10-15 critical peak events per year, typically 2-6 hours duration on hottest summer afternoons. Annual notification with day-ahead or day-of notice. Aggressive DR strategies justified by high pricing differential.

**Capacity Bidding Programs:**
Large commercial customers bid committed demand reduction capacity into utility or ISO markets, receiving capacity payments ($50-150/kW-year) regardless of event frequency. Performance penalties apply for non-delivery during called events. Requires reliable DR capability and baseline verification.

## Control Strategies for DR Events

Effective demand response requires sophisticated control sequences that balance demand reduction against comfort, equipment protection, and operational constraints.

### Staged Response Strategy

Multi-stage DR strategies provide graduated response levels based on event severity and duration:

**Level 1 - Moderate (10-20% demand reduction):**
- Reset zone temperature setpoints +2°F cooling, -2°F heating
- Reduce outdoor air to code minimum ventilation
- Reduce condenser fan speed 10-15%
- Disable auxiliary equipment (reheat, humidification)

**Level 2 - Aggressive (20-35% demand reduction):**
- Reset zone temperature setpoints +3-4°F cooling, -3-4°F heating
- Reduce supply fan speed 15-25% if ventilation permits
- Cycle compressors 50-70% duty cycle
- Reduce chilled water temperature reset 4-6°F
- Shut down non-critical zones

**Level 3 - Emergency (35-50% demand reduction):**
- Reset zone temperature setpoints +5°F cooling, -4°F heating
- Reduce to minimum equipment operation
- Compressor cycling 30-50% duty cycle or complete shutdown
- Critical loads only (server rooms, laboratories)
- Occupant notification of degraded conditions

### Recovery Strategy

Post-event recovery prevents demand rebound that creates new peak when all systems restart simultaneously. Staggered restart over 30-60 minutes distributes recovery load:

1. Restore outdoor air ventilation rates
2. Resume supply fan normal operation
3. Return zone setpoints to normal over 15-30 minutes
4. Restart chillers and compressors sequentially with 5-10 minute delays
5. Re-enable auxiliary equipment last

Gradual setpoint recovery prevents aggressive cooling that overshoots setpoint and wastes rebound energy. Temperature recovery rate of 1°F per 15-20 minutes balances comfort restoration with demand management.

## Economic Benefits and Incentive Structures

Demand response participation generates multiple revenue streams and cost reductions that improve building operating economics.

### Utility Incentive Payments

| Program Type | Incentive Structure | Typical Value | Payment Frequency |
|--------------|---------------------|---------------|-------------------|
| Direct Load Control | Per-kW enrolled capacity | $75-150/kW-year | Monthly/Annual |
| Auto-DR Enablement | Installation incentive | $0.20-0.50/ft² | One-time |
| CPP Participation | Avoided energy charges | $5-25/kW-event | Per event |
| Capacity Bidding | Committed capacity payment | $100-200/kW-year | Monthly |
| Performance Incentive | Verified load reduction | $0.30-0.75/kWh reduced | Per event |

### Energy Cost Reduction

Peak demand reduction directly reduces electricity costs through multiple mechanisms:

**Demand Charge Reduction:**
Commercial electricity rates include demand charges based on peak 15-minute kW consumption, ranging from $10-30/kW-month. Reducing peak demand 100 kW saves $1,200-3,600 monthly ($14,400-43,200 annually).

**Energy Charge Savings:**
Avoiding consumption during peak price periods saves energy charges. Peak rates of $0.20-0.40/kWh versus off-peak $0.06-0.12/kWh create $0.14-0.28/kWh differential. Shifting 500 kWh daily saves $70-140 per day ($25,000-50,000 annually).

**Capacity Tag Reduction:**
ISO markets allocate capacity costs based on customer contribution to system peak (capacity tag). Reducing consumption during top 5-10 system peak hours reduces annual capacity tag allocation, saving $50-120/kW-year.

### Typical DR Performance Metrics

| Building Type | Load Shed Potential | Annual Events | Event Duration | Annual Value |
|---------------|---------------------|---------------|----------------|--------------|
| Office (200,000 ft²) | 150-300 kW | 12-15 | 3-4 hours | $18,000-35,000 |
| Retail (100,000 ft²) | 100-200 kW | 15-20 | 2-4 hours | $12,000-25,000 |
| School (150,000 ft²) | 120-240 kW | 8-12 | 2-3 hours | $10,000-20,000 |
| Hospital (300,000 ft²) | 200-400 kW | 10-15 | 3-5 hours | $25,000-50,000 |

Return on investment for DR system implementation typically ranges from 1-3 years considering incentive payments, demand charge reduction, and energy cost savings. Advanced control systems with AutoDR capability cost $15,000-75,000 depending on building size and system complexity.

## Technical Considerations

Successful demand response implementation requires attention to equipment limitations, safety considerations, and performance verification.

Minimum compressor off-time requirements (5-10 minutes) prevent short-cycling damage during DR cycling strategies. Crankcase heater operation requirements for reciprocating compressors necessitate advance planning for extended shutdowns exceeding 4-6 hours.

Indoor air quality maintenance during DR events requires careful ventilation management. ASHRAE 62.1 minimum ventilation rates must be maintained unless event severity justifies temporary occupant notification and IAQ degradation acceptance.

Humidity control becomes critical during DR events in humid climates. Reduced cooling operation allows space humidity to drift upward. Limiting DR events to 2-4 hours and monitoring space humidity prevents excessive moisture accumulation that damages materials or enables mold growth.

Baseline establishment determines credited demand reduction by comparing actual consumption during DR events to estimated baseline consumption without DR participation. Accurate baseline calculation requires regression analysis of consumption versus outdoor temperature, occupancy, and other relevant variables.

Measurement and verification protocols confirm actual DR performance and ensure incentive payment accuracy. Interval meter data (15-minute or hourly) tracks consumption before, during, and after DR events. Statistical analysis compares event-day performance to baseline projection with weather normalization.

