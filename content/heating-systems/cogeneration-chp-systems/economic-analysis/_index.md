---
title: "Economic Analysis and Financial Evaluation"
description: "Comprehensive financial analysis methodologies for CHP systems including spark spread calculations, avoided cost analysis, payback period, net present value, internal rate of return, utility rate structures, incentives, and sensitivity analysis for investment decision-making."
date: 2026-01-04
weight: 6
---

CHP economic viability depends on the difference between avoided energy costs and CHP operating costs plus capital recovery. Facilities with high electricity rates, substantial thermal loads, favorable electricity-to-gas price ratios, and long operating hours provide the most attractive economics. Systematic financial analysis quantifies project economics across multiple metrics to support investment decisions and optimize system sizing.

## Spark Spread and Fuel Cost Differential

The spark spread measures the profitability of converting fuel to electricity, representing the difference between electricity value and fuel cost on an equivalent energy basis:

$$\text{Spark Spread} = P_{elec} - \frac{P_{fuel} \cdot HR}{1{,}000{,}000}$$

Where $P_{elec}$ is electricity price ($/kWh), $P_{fuel}$ is fuel price ($/MMBtu), and HR is heat rate (Btu/kWh). For a CHP system with heat rate of 10,000 Btu/kWh (34% efficient), electricity price of $0.12/kWh, and natural gas price of $6.00/MMBtu:

$$\text{Spark Spread} = 0.12 - \frac{6.00 \times 10{,}000}{1{,}000{,}000} = 0.12 - 0.06 = \$0.06/\text{kWh}$$

Positive spark spreads indicate favorable conditions for CHP, while negative spreads suggest purchasing grid electricity costs less than on-site generation. However, spark spread analysis alone ignores thermal recovery value, underestimating CHP economics.

The effective spark spread accounts for thermal energy value:

$$\text{Effective SS} = P_{elec} + \frac{Q_{thermal} \cdot P_{fuel,avoided}}{W_{elec}} - \frac{P_{fuel} \cdot HR}{1{,}000{,}000}$$

Where $Q_{thermal}$ represents thermal recovery (Btu/hr), $W_{elec}$ represents electrical output (kW), and $P_{fuel,avoided}$ represents displaced fuel cost adjusted for boiler efficiency. The thermal credit significantly improves CHP economics.

## Avoided Cost Calculations

CHP systems offset multiple facility costs beyond simple commodity energy purchases. Comprehensive analysis quantifies all avoided costs.

Avoided electricity costs include both energy charges and demand charges. Time-of-use rates vary by season and time-of-day, requiring hourly analysis of CHP operation:

$$\text{Avoided}_{elec} = \sum_{i=1}^{8760} P_{elec,i} \cdot W_{CHP,i} + \sum_{m=1}^{12} P_{demand,m} \cdot \Delta D_m$$

Where $P_{elec,i}$ represents hourly energy rate, $W_{CHP,i}$ represents CHP electrical output, $P_{demand,m}$ represents monthly demand charge, and $\Delta D_m$ represents peak demand reduction in month $m$.

Demand charge reductions depend on CHP reliability and operating strategy. Firm capacity (CHP plus standby) enables full demand charge credit. Interruptible CHP or single CHP units may not reduce peak demand if outages coincide with facility peak loads.

Avoided thermal fuel costs reflect displaced boiler fuel consumption:

$$\text{Avoided}_{thermal} = \frac{Q_{utilized}}{\eta_{boiler}} \cdot P_{fuel,boiler}$$

Where $Q_{utilized}$ represents thermal energy actually utilized by the facility (not merely recovered), $\eta_{boiler}$ represents displaced boiler efficiency, and $P_{fuel,boiler}$ represents boiler fuel price. Credit applies only to utilized thermal energy—excess thermal production provides no economic benefit.

Avoided capacity costs capture deferred or eliminated equipment purchases. CHP can defer boiler replacement, chiller capacity, transformer upgrades, or electrical service expansions. The present value of deferred capital equals:

$$PV_{deferred} = \frac{C_{avoided}}{(1+r)^n}$$

Where $C_{avoided}$ represents avoided capital cost, $r$ represents discount rate, and $n$ represents years of deferral.

## Operating Cost Components

CHP operating costs include fuel consumption, maintenance, labor, and utility charges.

Fuel costs represent the largest operating expense, typically 70-85% of total operating costs:

$$C_{fuel} = Q_{fuel} \cdot h_{annual} \cdot P_{fuel}$$

Where $Q_{fuel}$ represents fuel consumption rate (MMBtu/hr), $h_{annual}$ represents annual operating hours, and $P_{fuel}$ represents fuel price ($/MMBtu). Fuel costs scale linearly with operating hours and fuel price.

Maintenance costs depend on prime mover technology, size, and operating regime. Reciprocating engines incur 0.010-0.020/kWh, gas turbines 0.005-0.012/kWh, and fuel cells 0.005-0.015/kWh. Maintenance costs include:

- Scheduled maintenance (oil, filters, spark plugs, inspections)
- Major overhauls at 40,000-80,000 hour intervals
- Unscheduled repairs and component replacement
- Emissions system maintenance (catalyst replacement, SCR reagent)

Labor costs for operation and monitoring vary with system complexity and facility staffing. Small packaged CHP systems with remote monitoring may require minimal incremental labor. Large industrial installations with multiple units and complex integration require dedicated operations staff.

Utility standby charges compensate the electric utility for maintaining backup service during CHP outages. Monthly standby charges typically range from $3-10/kW of CHP capacity. Annual standby costs can reach 5-15% of total operating costs.

Exit fees apply when CHP reduces electricity purchases below minimum contract levels. Some industrial rate structures assess penalties for demand reduction or contractual minimum purchases.

## Capital Cost Estimation

CHP installed costs vary widely with prime mover technology, size, site conditions, and integration complexity. The following table summarizes typical installed costs:

| Technology | Capacity Range | Installed Cost ($/kW) |
|------------|---------------|---------------------|
| Reciprocating Engine | 100-500 kW | $3,500-5,500 |
| Reciprocating Engine | 1-5 MW | $2,200-3,800 |
| Gas Turbine | 5-40 MW | $2,000-4,000 |
| Microturbine | 30-250 kW | $4,000-6,500 |
| Fuel Cell (PAFC) | 400 kW | $6,000-8,000 |
| Fuel Cell (MCFC) | 1-3 MW | $5,500-7,500 |
| Fuel Cell (SOFC) | 100-300 kW | $7,000-10,000 |

These costs include prime mover, generator, heat recovery equipment, controls, electrical interconnection, and installation. Costs exclude site-specific civil work, gas service upgrades, or building modifications.

Integration complexity significantly affects installed costs. Simple packaged systems with hot water recovery and minimal integration cost 15-25% less than complex installations with steam generation, absorption cooling, and sophisticated controls.

## Simple Payback Period

Simple payback calculates years required to recover initial investment from annual savings:

$$\text{Payback} = \frac{C_{installed}}{S_{annual} - C_{O\&M,annual}}$$

Where $C_{installed}$ represents total installed cost, $S_{annual}$ represents annual avoided energy costs, and $C_{O\&M,annual}$ represents annual operating and maintenance costs excluding fuel.

For a 1 MW reciprocating engine CHP system with $3,000,000 installed cost, annual electricity savings of $800,000, thermal savings of $400,000, fuel costs of $850,000, and O&M costs of $150,000:

$$\text{Payback} = \frac{3{,}000{,}000}{(800{,}000 + 400{,}000 - 850{,}000) - 150{,}000} = 15.0 \text{ years}$$

This long payback suggests poor economics. However, if thermal savings increase to $700,000 through better utilization:

$$\text{Payback} = \frac{3{,}000{,}000}{(800{,}000 + 700{,}000 - 850{,}000) - 150{,}000} = 6.0 \text{ years}$$

This demonstrates the critical importance of thermal utilization to CHP economics.

Payback periods below 7 years generally indicate favorable projects, though specific thresholds vary by organization and available incentives.

## Net Present Value and Internal Rate of Return

Net present value accounts for the time value of money by discounting future cash flows:

$$\text{NPV} = \sum_{t=1}^n \frac{CF_t}{(1+r)^t} - C_0$$

Where $CF_t$ represents net cash flow in year $t$ (savings minus operating costs), $r$ represents discount rate, $n$ represents project lifetime, and $C_0$ represents initial capital cost. Positive NPV indicates economic attractiveness.

For the previous example with improved thermal utilization, assuming 20-year life and 8% discount rate:

$$\text{NPV} = \frac{500{,}000}{0.08} \cdot \left(1 - \frac{1}{1.08^{20}}\right) - 3{,}000{,}000 = \$1{,}909{,090$$

The positive NPV indicates an economically viable project returning $1.91 million above the required 8% return.

Internal rate of return represents the discount rate yielding NPV of zero:

$$0 = \sum_{t=1}^n \frac{CF_t}{(1+IRR)^t} - C_0$$

IRR calculation requires iterative solution. For the example, IRR equals approximately 13.5%, substantially exceeding the 8% required return.

## Sensitivity Analysis

CHP economic performance varies with multiple uncertain parameters. Sensitivity analysis quantifies impact of parameter variations on project returns.

Critical parameters affecting CHP economics include:

- Natural gas price: ±$1-3/MMBtu variation typical over project life
- Electricity price: ±20-40% variation possible with market conditions
- Capacity factor: Actual operating hours may vary ±10-20% from projections
- Thermal utilization: Actual heat utilization often 70-90% of recovery capacity
- Capital cost: Final installed cost may vary ±15-25% from estimates
- Maintenance costs: Actual maintenance may vary ±25-50% from projections

Tornado diagrams rank parameters by NPV sensitivity. Typically, electricity price and capacity factor exert greatest influence, followed by fuel price and thermal utilization. Projects with small positive NPV under base assumptions risk becoming uneconomic with modest adverse parameter shifts.

Break-even analysis identifies parameter values yielding zero NPV or target payback. For example, minimum thermal utilization for 7-year payback or minimum electricity price for positive NPV.

## Utility Rate Structures and Tariffs

Electricity rate structures significantly affect CHP economics through both energy and demand components.

Real-time pricing (RTP) varies hourly based on wholesale market prices. CHP systems can target operation during high-price periods, improving economics by 15-30% compared to flat rates. However, thermal-led CHP operation may not align with electrical price peaks.

Time-of-use (TOU) rates establish distinct on-peak and off-peak energy prices. Summer afternoon on-peak rates often exceed off-peak rates by 2-4x. CHP operation during on-peak periods captures maximum electricity value.

Demand charges assess fees based on peak 15-minute or 30-minute demand each billing period. Typical commercial and industrial demand charges range from $5-25/kW per month. For facilities with peak demands of 2000 kW, annual demand charges can reach $120,000-600,000.

CHP demand charge savings depend on coincidence between CHP operation and facility peak demand. Baseload CHP operating continuously reduces demand charges proportionally to CHP capacity. Intermittent CHP or single-unit systems may fail to reduce peak demand if outages coincide with peak loads.

## Incentives and Tax Benefits

Federal, state, and utility incentives can improve CHP economics substantially.

Federal Investment Tax Credit (ITC) provides 10% credit for CHP systems meeting efficiency thresholds (60% total CHP efficiency for systems ≤20 MW, 70% for larger systems). The ITC reduces net capital cost by 10%.

Modified Accelerated Cost Recovery (MACRS) depreciation enables accelerated depreciation over 5 or 7 years rather than 20+ year equipment life. The accelerated depreciation increases present value of tax shields.

State incentives vary widely by jurisdiction. Some states offer:
- Capital cost rebates ($500-1500/kW)
- Production incentives ($0.01-0.03/kWh for 5-10 years)
- Property tax exemptions
- Sales tax exemptions on CHP equipment

Utility programs may provide incentives for peak demand reduction, emissions reduction, or grid support services. These programs can contribute 10-30% of project capital costs in favorable jurisdictions.

Carbon pricing or renewable energy credits provide additional revenue in some markets. CHP systems generate cleaner electricity than grid average in most regions, potentially qualifying for carbon credits or renewable energy certificates.
