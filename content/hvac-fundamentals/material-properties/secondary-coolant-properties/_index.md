---
title: "Secondary Coolant Properties"
aliases: ["Secondary Coolant Properties"]
description: "Thermophysical properties of secondary coolants, brines, and heat transfer fluids including glycol solutions, calcium chloride, and sodium chloride brines for indirect refrigeration system design."
weight: 2
---

Secondary coolants (brines and heat transfer fluids) transport thermal energy in indirect refrigeration and cooling systems where primary refrigerant circulation is impractical or undesirable. These fluids enable freeze protection, reduce refrigerant charge, improve safety, and facilitate distribution to multiple zones.

## Secondary Coolant Applications

Indirect systems using secondary coolants offer advantages over direct expansion in specific applications:

**Industrial refrigeration:** Large-scale cold storage, process cooling, ice rinks where ammonia (R717) safety concerns drive indirect systems.

**Building HVAC:** Chilled water systems, ice storage, snow melting where freeze protection prevents catastrophic pipe ruptures during winter shutdown.

**Food processing:** Sanitary requirements and equipment flexibility favor brine systems with centralized refrigeration plants.

## Fundamental Property Requirements

Effective secondary coolants must satisfy multiple criteria:

**Freeze protection:** Adequate freeze point depression below minimum operating temperature with safety margin (typically 10°F below lowest expected temperature).

**Heat transfer capability:** High specific heat and thermal conductivity maximize energy transport per unit flow rate and minimize temperature differences.

**Fluid mechanics:** Low viscosity reduces pumping power while maintaining turbulent flow for effective heat transfer.

**Material compatibility:** Non-corrosive to system materials (steel, copper, aluminum, elastomers) or compatible with inhibitor packages.

**Stability:** Chemical and thermal stability throughout operating temperature range without degradation or precipitation.

## Glycol Solutions

Propylene glycol and ethylene glycol represent the most common secondary coolants for HVAC applications. Water-glycol mixtures provide freeze protection while maintaining acceptable heat transfer and pumping characteristics.

**Propylene glycol:** Non-toxic formulation suitable for food processing, potable water proximity, and applications requiring food-grade safety. Slightly inferior heat transfer compared to ethylene glycol at equivalent concentrations.

**Ethylene glycol:** Superior thermal performance but toxic, requiring isolation from potable water systems. Automotive antifreeze formulations unsuitable due to additives that foul heat exchangers.

**Inhibitor packages:** Corrosion inhibitors (nitrites, molybdates, silicates) protect system metallurgy but require periodic testing and replenishment as inhibitors deplete through oxidation and precipitation.

## Inorganic Salt Brines

Calcium chloride and sodium chloride brines offer lower cost for industrial applications accepting higher corrosivity and specific gravity.

**Calcium chloride:** Eutectic at 30% by weight (-55°C) provides exceptional freeze protection for very low temperature applications. High density (1.3 relative to water at eutectic) increases pumping power.

**Sodium chloride:** Eutectic at 23% by weight (-21°C) suitable for ice rink applications and moderate-temperature industrial cooling. Lower freeze protection than calcium chloride.

**Corrosion control:** Chromate inhibitors (now restricted) traditionally provided corrosion protection. Modern alternatives including nitrite-borax combinations require careful pH control and monitoring.

## Concentration Effects

Secondary coolant properties vary strongly with concentration. Freeze point depression increases with concentration, but thermal performance degrades due to reduced specific heat, increased viscosity, and decreased thermal conductivity.

**Optimum concentration:**
- Provides adequate freeze protection (minimum temperature + 10°F margin)
- Minimizes adverse thermal effects (viscosity, reduced cp)
- Balances capital cost (heat exchanger size) against operating cost (pumping power)

Over-concentration beyond freeze protection requirements imposes performance penalties without benefits. Under-concentration risks freeze damage during abnormal conditions or shutdown.

## Property Temperature Dependence

All secondary coolant properties exhibit temperature dependence requiring consideration across the full operating range:

**Density:** Decreases with temperature following approximately linear trends. Affects system charge calculations and thermal expansion.

**Specific heat:** Generally increases slightly with temperature. Determines sensible heat transport capacity via Q = ṁcp∆T.

**Viscosity:** Decreases exponentially with temperature per Arrhenius relationship. Cold-temperature viscosity drives pump sizing while operating viscosity determines Reynolds number.

**Thermal conductivity:** Increases slightly with temperature. Combined with viscosity in Prandtl number (Pr = cpμ/k) governing convective heat transfer.

## Heat Transfer Considerations

Secondary coolant properties directly impact heat exchanger performance through dimensionless groups:

**Reynolds number:** Re = ρVD/μ determines flow regime. Higher viscosity reduces Re, potentially compromising turbulent heat transfer.

**Prandtl number:** Pr = cpμ/k relates momentum diffusivity to thermal diffusivity. Glycol solutions exhibit Pr ≈ 20-100 compared to Pr ≈ 7 for water, reducing heat transfer coefficients.

**Heat transfer coefficient:** h ∝ kRe^0.8Pr^0.4 for turbulent flow. Reduced thermal conductivity and higher Prandtl number decrease h, requiring larger heat exchanger surface area.

## System Design Implications

Secondary coolant selection and concentration affect multiple system aspects:

**Temperature difference:** Lower heat transfer coefficients require larger ∆T between primary refrigerant and secondary coolant, reducing system efficiency.

**Flow rates:** Lower specific heat requires higher flow rates for equivalent capacity, increasing pipe sizes and pumping power.

**Pump power:** Increased viscosity and flow rate combine to increase pressure drop per Darcy-Weisbach equation, raising parasitic energy consumption.

**Heat exchanger sizing:** Reduced overall heat transfer coefficient (U-value) demands greater surface area for specified capacity and approach temperatures.

## Maintenance and Monitoring

Secondary coolants require periodic testing and maintenance:

**Concentration testing:** Refractometer or hydrometer measurements verify adequate freeze protection. Glycol concentrations drift due to water loss through leaks or evaporation.

**pH monitoring:** Glycol systems maintain pH 8-9 for corrosion control. Oxidation produces organic acids reducing pH and accelerating corrosion.

**Inhibitor levels:** Deplete through precipitation and chemical reactions. Annual testing with replenishment extends fluid service life.

**Contamination:** Particulate filtration removes corrosion products. Bacterial growth in glycol systems requires biocides.

## Alternative Heat Transfer Fluids

Specialty applications may employ alternative secondary coolants:

**Potassium formate/acetate:** Low environmental impact, non-toxic, good thermal performance but higher cost than glycols.

**Synthetic oils:** Very low temperature applications (-70°C) where aqueous solutions freeze. Poor heat transfer requires larger equipment.

**Potassium carbonate:** Historical use declining due to corrosivity and handling difficulties.
