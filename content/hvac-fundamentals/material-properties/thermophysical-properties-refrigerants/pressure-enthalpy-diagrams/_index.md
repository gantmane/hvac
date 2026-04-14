---
title: "Pressure-Enthalpy Diagrams"
aliases: ["Pressure-Enthalpy Diagrams"]
description: "Pressure-enthalpy P-h diagrams for refrigeration cycle analysis including saturation dome, isentropic lines, constant quality lines, subcooling superheat regions, and refrigerant property determination for HVAC system design and troubleshooting"
weight: 3
---

Pressure-enthalpy (P-h) diagrams provide the fundamental graphical tool for analyzing vapor compression refrigeration cycles. These diagrams plot absolute pressure on the vertical axis (typically logarithmic scale) against specific enthalpy on the horizontal axis, enabling direct visualization of thermodynamic processes and rapid determination of refrigerant properties throughout the cycle.

## Diagram Structure and Coordinate System

The P-h diagram uses a logarithmic pressure scale on the vertical axis, spanning from deep vacuum conditions (0.01 bar or lower) to supercritical pressures exceeding the critical point. The horizontal axis represents specific enthalpy in kJ/kg, ranging from compressed liquid states to superheated vapor conditions.

The logarithmic pressure scale compresses the high-pressure region while expanding the low-pressure region, providing better resolution for evaporator conditions where most refrigeration systems operate. This scaling makes the diagram practical for analyzing systems with large pressure ratios, typical in HVAC applications.

## Saturation Dome and Phase Regions

The saturation curve forms the characteristic bell-shaped dome that defines phase boundaries on the P-h diagram. The left boundary represents saturated liquid conditions (bubble line), while the right boundary represents saturated vapor conditions (dew line). These curves meet at the critical point, above which distinct liquid and vapor phases cease to exist.

Inside the saturation dome, the two-phase region contains a mixture of liquid and vapor refrigerant. The quality (dryness fraction) indicates the mass fraction of vapor, with x = 0 at the saturated liquid line and x = 1.0 at the saturated vapor line. Constant quality lines run approximately diagonally through the dome, with x = 0.1, 0.2, 0.3, etc.

To the left of the saturated liquid line lies the subcooled liquid region, where refrigerant temperature falls below the saturation temperature at the corresponding pressure. To the right of the saturated vapor line extends the superheated vapor region, where refrigerant temperature exceeds saturation temperature. The degree of subcooling or superheat equals the temperature difference from saturation conditions.

## Constant Property Lines

**Isotherms** (constant temperature lines) appear as vertical lines in the subcooled liquid region due to liquid incompressibility. Within the two-phase region, isotherms follow constant pressure lines horizontally, since saturation temperature depends only on pressure. In the superheated region, isotherms curve downward to the right with decreasing slope as temperature increases.

**Isobars** (constant pressure lines) plot as horizontal lines across the entire diagram, making P-h diagrams particularly useful since pressure remains constant in heat exchangers. This horizontal representation simplifies visualization of evaporator and condenser processes.

**Isentropes** (constant entropy lines) run nearly vertically in the two-phase and superheated regions. These lines slope slightly to the right with a steeper angle in the two-phase dome. Isentropic compression follows these lines, representing ideal (reversible adiabatic) compressor operation. The deviation between actual compression and isentropic compression quantifies compressor inefficiency.

**Constant volume** (isochores) lines appear in the superheated region, useful for analyzing reciprocating compressor clearance volumes and re-expansion processes. These lines have a steeper slope than isentropes.

**Constant quality lines** within the saturation dome indicate the vapor mass fraction at any point in the two-phase region. These lines radiate from the critical point toward the saturated liquid line, with quality values from 0.1 to 0.9 typically marked.

## Refrigeration Cycle Representation

The basic vapor compression cycle plots as a quadrilateral on the P-h diagram:

**Process 1-2 (Compression):** Starts at evaporator outlet (superheated vapor) and rises to condenser pressure. Ideal isentropic compression follows a constant entropy line vertically upward. Real compression deviates to the right due to irreversibilities, following a path of increasing entropy. The horizontal distance between isentropic and actual endpoints represents compression inefficiency.

**Process 2-3 (Condensing):** Moves horizontally left at constant condenser pressure. The process begins with desuperheating (cooling superheated vapor to saturation), continues through the two-phase condensing region (at constant temperature), and may include subcooling below saturation temperature. The enthalpy change represents heat rejection per unit mass.

**Process 3-4 (Expansion):** Ideally occurs at constant enthalpy (isenthalpic throttling) through an expansion valve. This plots as a vertical line downward from high to low pressure. The process enters the two-phase region, producing a mixture of liquid and vapor at evaporator conditions. Isenthalpic expansion increases entropy, representing an irreversible process.

**Process 4-1 (Evaporation):** Moves horizontally right at constant evaporator pressure. The two-phase refrigerant absorbs heat, increasing vapor fraction from the inlet quality to saturated vapor at the evaporator outlet. Additional superheat may occur if the evaporator includes a superheat section. The enthalpy change represents refrigeration capacity per unit mass.

## Reading Thermodynamic Properties

P-h diagrams enable direct graphical determination of refrigerant properties at any state point:

**Pressure and enthalpy** read directly from the coordinate axes for any point on the diagram.

**Temperature** is determined by locating the isotherm passing through the point. In the two-phase region, temperature equals saturation temperature corresponding to the pressure.

**Entropy** is found by following the isentrope through the point and reading the entropy value marked on that line, typically along the saturated vapor curve.

**Quality** in the two-phase region is interpolated between constant quality lines, indicating the vapor mass fraction.

**Specific volume** is determined from constant volume lines in the superheated region. In the two-phase region, specific volume is calculated from quality and saturated liquid/vapor volumes.

**Degree of superheat** equals the horizontal temperature difference between the state point and the saturated vapor line at the same pressure.

**Degree of subcooling** equals the temperature difference between the saturated liquid line and the state point at the same pressure.

## Cycle Performance Analysis

The P-h diagram provides direct graphical analysis of cycle performance parameters:

**Refrigeration effect** (q_e) equals the horizontal distance (enthalpy change) along the evaporator process line from expansion valve outlet to compressor inlet. This represents cooling capacity per unit mass flow.

**Compression work** (w_c) equals the enthalpy rise from compressor inlet to outlet, read as the horizontal distance of the compression process. Larger work input reduces efficiency.

**Heat rejection** (q_c) equals the enthalpy decrease during condensing from compressor discharge to expansion valve inlet. This exceeds refrigeration effect by the amount of compression work.

**Coefficient of Performance** (COP) equals refrigeration effect divided by compression work: COP = q_e / w_c. Higher COP indicates more efficient operation.

**Isentropic efficiency** (η_is) compares actual compression work to ideal isentropic work at the same pressure ratio: η_is = (h_2s - h_1) / (h_2 - h_1), where h_2s represents isentropic discharge enthalpy.

## Refrigerant-Specific Characteristics

Different refrigerants exhibit distinct P-h diagram characteristics affecting system design:

**Critical point location** varies significantly among refrigerants. High critical temperature refrigerants (R-134a, R-1234yf) allow subcritical operation in most HVAC applications. Low critical temperature refrigerants (R-744/CO2) operate transcritically in warm climates, fundamentally changing cycle characteristics.

**Saturation dome shape** influences cycle efficiency and compressor discharge temperature. Refrigerants with "wet" compression characteristics (dome leaning left) risk liquid carryover to compressors. "Dry" refrigerants (dome leaning right) produce high discharge temperatures requiring careful management.

**Slope of isentropes** in the superheated region affects discharge temperature during compression. Steeper isentropes produce lower discharge temperatures for the same pressure ratio.

**Latent heat magnitude** determines the horizontal extent of the two-phase region. High latent heat refrigerants achieve greater refrigeration effect per unit mass flow, potentially reducing compressor displacement requirements.

## Troubleshooting Applications

P-h diagrams enable systematic diagnosis of refrigeration system problems:

**Insufficient subcooling** at the condenser outlet indicates inadequate condenser capacity, high ambient temperature, or insufficient refrigerant charge. The state point shifts toward the saturated liquid line, risking flash gas formation.

**Excessive superheat** at the compressor inlet suggests underfeeding by the expansion device, low refrigerant charge, or loss of evaporator capacity. The inlet state point shifts far right, reducing capacity and increasing compression ratio effects.

**High discharge temperature** appears as the compression endpoint shifting to higher temperature isotherms. Causes include excessive compression ratio, insufficient inlet superheat, or compressor inefficiency increasing actual work input.

**Subcritical versus transcritical operation** for CO2 systems is immediately apparent from the discharge pressure relationship to the critical point. Transcritical cycles require gas cooler analysis rather than condensing analysis, with significantly different optimization strategies.

**Flooded evaporator** operation shows as reduced superheat or two-phase conditions at the compressor inlet, risking liquid slugging. The state point approaches or crosses into the saturation dome.

## Practical Diagram Usage

Engineers use P-h diagrams throughout system design, analysis, and commissioning. During design, the diagram verifies operating conditions fall within acceptable ranges for all components. For existing systems, measured pressures and temperatures plot as state points, with deviations from expected locations indicating specific problems.

Modern refrigeration analysis increasingly relies on computerized property databases and calculation software, but P-h diagrams remain essential for conceptual understanding, rapid estimation, and effective communication of thermodynamic processes. The visual representation clarifies relationships between properties that equations alone obscure, making P-h diagrams indispensable tools for HVAC professionals analyzing vapor compression systems.
