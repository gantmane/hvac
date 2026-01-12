---
title: "Demand Response Programs"
weight: 1
---

Demand response programs provide financial incentives for building owners to reduce electrical demand during utility system peak periods or grid emergencies. These programs represent contractual agreements between utilities or grid operators and customers to temporarily modify electricity consumption patterns.

## Program Types

### Incentive-Based Programs

**Direct Load Control (DLC)**

Utility operators remotely control customer equipment during peak events:

- HVAC cycling: 15-30 minute duty cycle reductions
- Water heater cycling: 2-4 hour control periods
- Pool pump control: load shift to off-peak hours
- Customer compensation: $10-50/kW per season
- No performance penalty for equipment availability

**Interruptible/Curtailable Programs**

Customers agree to reduce load upon notification:

- Advance notice: 30 minutes to 2 hours
- Event duration: 2-6 hours typical
- Annual events: 10-100 hours maximum
- Incentive rates: $100-400/kW-year
- Non-compliance penalties: $5-15/kWh missed reduction

**Emergency Demand Response**

Grid operators call events during system emergencies:

- Notification time: 10-30 minutes
- Event frequency: 10-20 per year maximum
- Duration limits: 4 hours typical
- Payment structure: $400-600/MWh
- Voluntary participation in most programs

**Capacity Market Programs**

Annual commitment to provide demand reduction:

- Forward capacity auctions: 1-3 years advance
- Clearing prices: $2-10/kW-month
- Performance requirements: 80-100% of committed load
- Testing protocols: seasonal capability verification
- Penalties for non-performance: replacement energy costs

### Price-Based Programs

**Time-of-Use (TOU) Rates**

Fixed pricing based on time periods:

| Period | Summer Rate | Winter Rate | Typical Hours |
|--------|-------------|-------------|---------------|
| On-Peak | $0.25-0.40/kWh | $0.18-0.28/kWh | 12pm-8pm |
| Mid-Peak | $0.15-0.22/kWh | $0.12-0.18/kWh | 8am-12pm, 8pm-10pm |
| Off-Peak | $0.08-0.12/kWh | $0.08-0.12/kWh | 10pm-8am |

**Critical Peak Pricing (CPP)**

Higher rates during declared critical events:

- Event rates: $0.75-2.00/kWh
- Annual events: 12-15 days maximum
- Notification: Day-ahead or day-of
- Event duration: 3-6 hours
- Baseline rate reduction to offset high event prices

**Real-Time Pricing (RTP)**

Hourly or sub-hourly electricity pricing:

- Price updates: hourly or 15-minute intervals
- Notification: Day-ahead or hour-ahead
- Price range: $0.03-1.50/kWh
- Risk exposure: customers bear market volatility
- Suitable for automated response systems

## Utility Incentives

### Performance Payment Structures

**Energy Payment**

Compensation for actual energy reduction:

- Measurement: metered load reduction vs. baseline
- Rate structure: $/kWh reduced
- Typical range: $0.50-2.00/kWh
- Payment frequency: monthly or event-based
- Baseline calculation: 10-of-10 or regression methods

**Capacity Payment**

Annual payment for load reduction availability:

- Subscription basis: committed kW reduction
- Monthly payments: $3-12/kW-month
- Performance requirements: minimum 4-hour response
- Verification testing: quarterly or seasonal
- Availability guarantee: 95-100% of events

**Reservation Payment**

Fixed payment for program enrollment:

- Participation incentive: $50-200/year
- Minimum load threshold: 100-500 kW
- No performance requirement for reservation
- Additional performance payments during events
- Equipment installation cost-sharing

### Financial Benefits

**Direct Cost Savings**

Peak demand reduction impacts:

- Demand charge reduction: $10-40/kW-month
- Energy cost avoidance: $0.15-0.50/kWh during events
- Annual savings potential: 10-30% of electricity costs
- ROI period: 1-4 years for automation investment
- Ongoing revenue from capacity payments

**Indirect Benefits**

- Reduced equipment runtime hours extends life
- Lower peak loading reduces maintenance frequency
- Improved power factor during load reduction
- Enhanced grid reliability reduces outage risk
- Corporate sustainability goal achievement

## Load Shedding Strategies

### HVAC Load Reduction

**Chiller Cycling**

Temporary shutdown of chilled water production:

- Strategy: 15-30 minute off periods during 1-2 hour events
- Load reduction: 300-800 W/ton of chiller capacity
- Temperature drift: 2-4°F during cycling
- Pre-cooling: lower setpoint 2-4°F for 1-2 hours before event
- Recovery time: 30-60 minutes post-event

**Fan System Modulation**

Variable speed drive reduction strategies:

- VFD setback: 20-40% speed reduction
- Airflow reduction: 50-75% of full flow (cubic relationship)
- Power savings: 85-93% at reduced speed
- Zone impact: temperature drift varies by location
- Duration limits: 1-2 hours before comfort complaints

**Zone Temperature Setpoint Adjustment**

Temporary setpoint modification:

| Season | Normal Setpoint | DR Setpoint | Load Reduction |
|--------|-----------------|-------------|----------------|
| Cooling | 72°F | 76-78°F | 15-25% HVAC load |
| Heating | 70°F | 66-68°F | 10-20% HVAC load |

- Ramp rate: 1°F per 15 minutes maximum
- Pre-conditioning: 2-3°F offset 2 hours before event
- Thermal mass utilization: building envelope stores energy

### Non-HVAC Load Shedding

**Lighting Reduction**

- Dimming: 30-50% output reduction saves 20-40% power
- Zone shutdown: non-critical areas 100% reduction
- Outdoor lighting: parking lot and facade lighting off
- Emergency egress: maintain code-required lighting levels

**Plug Load Management**

- IT equipment: server virtualization and load balancing
- Kitchen equipment: delay cooking operations
- Elevator systems: reduce cars in service
- Water heating: tank systems with stored capacity

**Process Load Curtailment**

- Production line shutdown: schedule maintenance during DR
- Compressed air: use receiver tank storage
- Process cooling: thermal storage discharge
- Material handling: reduce conveyor speeds

## Automated Demand Response

### Control System Integration

**Building Management System (BMS) Integration**

Direct control through existing automation:

- BACnet, Modbus, or proprietary protocol interface
- Pre-programmed DR strategies by event level
- Automated baseline measurement and verification
- Override capability for critical operations
- Post-event automated recovery sequences

**Discrete Control Points**

Typical automated control actions:

- AHU discharge temperature reset: +3-5°F
- Chiller staging: reduce operating units by 1
- Cooling tower fan cycling: intermittent operation
- Zone damper position limits: reduce airflow 20-30%
- Lighting zone dimming: 30-50% reduction

### Response Modes

**Moderate Mode (Level 1)**

Conservative load reduction:

- Load reduction target: 10-15% of connected load
- Temperature setpoint adjustment: 2°F
- Lighting reduction: 20-30% in non-critical zones
- Equipment cycling: minimal or none
- Occupant impact: minimal to none

**High Mode (Level 2)**

Aggressive demand reduction:

- Load reduction target: 20-30% of connected load
- Temperature setpoint adjustment: 4-6°F
- Lighting reduction: 40-60% facility-wide
- Equipment cycling: 15-30 minute periods
- Occupant impact: noticeable but tolerable

**Emergency Mode (Level 3)**

Maximum load curtailment:

- Load reduction target: 30-50% of connected load
- Non-essential HVAC shutdown
- Lighting: emergency and safety only
- Process equipment: critical loads only
- Duration: 1-2 hours maximum
- Occupant impact: significant discomfort expected

## OpenADR Protocol

### Protocol Architecture

**OpenADR 2.0b Standard**

Communication framework for automated DR:

- Transport protocol: HTTPS/TLS for security
- Message format: XML-based payload
- Services: event notification, registration, reporting
- Certification levels: A (basic) through B (full profile)
- Interoperability: vendor-neutral standard

**System Components**

Virtual Top Node (VTN):

- Utility or aggregator DR server
- Event creation and distribution
- Report collection and storage
- Client registration management

Virtual End Node (VEN):

- Customer facility automation gateway
- Event reception and parsing
- Control strategy execution
- Opt-out capability management
- Performance report generation

### Event Signals

**Event Notification Elements**

DR event structure:

- Event ID: unique identifier for tracking
- Start time: ISO 8601 format timestamp
- Duration: event length in minutes
- Ramp up period: preparation time before event
- Recovery period: restoration time after event
- Modification number: tracks event changes

**Signal Types**

Load reduction targets:

| Signal Name | Description | Units | Typical Range |
|-------------|-------------|-------|---------------|
| simple | Simple load level indicator | 0-3 | 0=normal, 3=emergency |
| electricity_price | Real-time pricing | $/kWh | 0.01-2.00 |
| load_control | Absolute demand limit | kW | Facility specific |
| load_dispatch | Reduction from baseline | kW | 0-500+ |

### Implementation Benefits

**Operational Advantages**

- Response time: 2-5 minutes vs. 15-30 minutes manual
- Consistency: programmed response eliminates human error
- Verification: automated M&V reduces administrative burden
- Optimization: real-time adjustment based on conditions
- Scalability: single VTN manages thousands of sites

**Performance Metrics**

- Event participation rate: 95-99% with automation
- Load reduction accuracy: ±5% of target
- Response latency: <5 minutes from event signal
- Availability: 99.5% uptime for communication
- ROI improvement: 20-40% better than manual DR

## Baseline Calculation Methods

### Common Baseline Approaches

**10-of-10 Method**

Average of previous 10 similar days:

- Day selection: same day-type (weekday/weekend)
- Exclusion criteria: DR events, holidays, anomalies
- Calculation: arithmetic mean of hourly consumption
- Adjustment: morning-of same-day correction
- Accuracy: ±10-15% of actual

**Regression-Based Baseline**

Statistical model incorporating variables:

- Temperature correlation: cooling/heating degree days
- Occupancy factors: day-of-week, holidays
- Production levels: industrial facility activity
- Weather normalization: accounts for load variation
- Accuracy: ±5-10% with sufficient data

**High 4-of-5 Method**

Average of highest 4 of preceding 5 days:

- Reduces baseline inflation concerns
- Excludes lowest day automatically
- Simple calculation without statistics
- Used in PJM capacity markets
- Accuracy: ±12-18% of actual

## Program Selection Criteria

### Facility Characteristics

Ideal candidates for DR participation:

- Peak demand: >200 kW minimum
- Load flexibility: 15-30% curtailable
- Thermal mass: building can coast 2-4 hours
- Operating hours: occupied during utility peak
- Automation: existing BMS with remote access

### Economic Analysis

Financial viability assessment:

- Annual incentive potential: capacity + performance
- Load reduction capability: kW and duration
- Automation investment: $5,000-50,000 typical
- Simple payback: <3 years preferred
- Risk assessment: penalties vs. revenue

**Example Calculation**

For 500 kW facility with 100 kW reduction capability:

| Revenue Source | Rate | Annual Value |
|----------------|------|--------------|
| Capacity payment | $8/kW-month | $9,600 |
| Performance payment | $1.50/kWh × 50 hours | $7,500 |
| Demand charge savings | $15/kW-month | $18,000 |
| **Total Annual Benefit** | | **$35,100** |

Automation investment: $25,000
Simple payback: 0.71 years

---

**File Path**: `/Users/evgenygantman/Documents/github/gantmane/hvac/content/hvac-fundamentals/energy-resources/energy-efficiency-potential/demand-response/demand-response-programs/_index.md`
