---
title: "Commercial Laundry Facilities"
description: "Heat and moisture load analysis, exhaust requirements, makeup air for dryers, and heat recovery opportunities for hotel laundries."
date: "2026-01-04"
weight: 5
tags: ["laundry HVAC", "dryer exhaust", "heat recovery", "moisture loads", "makeup air"]
categories: ["Specialty Applications"]
---

## Load Characteristics

Commercial hotel laundries generate extreme heat and moisture loads relative to floor area, often producing 500-800 Btu/hr-ft² sensible heat and requiring 15-30 air changes per hour for moisture control. A typical 1,000 ft² laundry serving a 200-room hotel operates 8-16 hours daily, processing 800-1,200 lb of linens with associated washer heat, dryer heat rejection, and evaporative moisture loads.

### Sensible Heat Sources

Equipment heat release dominates laundry sensible loads. Commercial washers contribute 20-30% of rated motor horsepower as heat to space, while dryers reject 50-70% of burner or heating element input. Calculate total sensible load:

$$Q_{sensible} = (Q_{washers} + Q_{dryers} + Q_{ironers} + Q_{lighting} + Q_{people})$$

For a mid-size hotel laundry:
- Washers (3 × 5 HP motors): $3 \times 5 \times 2545 \times 0.25 = 9,544$ Btu/hr
- Dryers (4 × 150k Btu/hr input): $4 \times 150,000 \times 0.60 = 360,000$ Btu/hr
- Ironers and folders (25 kW): $25 \times 3412 = 85,300$ Btu/hr
- Lighting (1.0 W/ft² × 1,000 ft²): $1,000 \times 3.41 = 3,410$ Btu/hr
- Occupants (4 people × 450 Btu/hr): $1,800$ Btu/hr
- **Total sensible**: $460,054$ Btu/hr or 460 Btu/hr-ft²

This extreme load density requires substantial cooling capacity. Most facilities operate with minimal air conditioning, instead using high ventilation rates to remove heat through outdoor air exhaust.

### Latent Heat Loads

Moisture evaporation from washing and drying processes generates 150-250 lb/hr of water vapor in active laundries. This moisture must be removed through ventilation to prevent condensation on cool surfaces and maintain acceptable working conditions (50-60% RH maximum).

Latent load calculation accounts for moisture evaporation rate and required enthalpy change:

$$Q_{latent} = \dot{m}_{evap} \times h_{fg}$$

where $\dot{m}_{evap}$ is evaporation rate (lb/hr) and $h_{fg}$ = 1,050 Btu/lb heat of vaporization.

For 200 lb/hr evaporation rate:
$$Q_{latent} = 200 \times 1,050 = 210,000 \text{ Btu/hr}$$

This latent load exceeds sensible load in many laundries, driving ventilation requirements based on moisture removal rather than temperature control.

## Exhaust Requirements

### Dryer Exhaust

Commercial dryers require dedicated exhaust ductwork removing 300-600 CFM per machine depending on capacity (20-75 lb load). Gas-fired dryers exhaust combustion products plus moisture, while electric dryers exhaust moisture-laden air without combustion gases. All dryer exhaust must duct directly to exterior, independent of general room ventilation systems.

Dryer exhaust velocity maintains 1,500-2,500 FPM in smooth metal ductwork, preventing lint accumulation that creates fire hazards. Duct materials must be metal (galvanized steel or aluminum) with mechanically fastened joints—flexible ducting prohibited beyond 8 feet from dryer connection point per fire codes.

Calculate dryer exhaust pressure drop using standard duct friction equations accounting for 90° elbows (0.25 in. wc each), dryer transition connection (0.3-0.5 in. wc), and exhaust termination (0.1-0.2 in. wc). Total static pressure typically 1.0-2.5 in. wc depending on duct length and configuration.

Exhaust terminal hoods require screening to prevent bird/rodent entry while minimizing back pressure. Gravity dampers prevent backdrafting during dryer shutdown but add 0.1-0.2 in. wc pressure drop. Power roof ventilators can assist exhaust but must interlock with dryer operation to prevent over-ventilation when machines idle.

### General Room Ventilation

Beyond dryer exhaust, laundry spaces need 15-25 air changes per hour for moisture and heat removal. This ventilation removes heat from washers, ironers, workers, and lighting while controlling humidity below 60% RH. Calculate required airflow:

$$CFM_{exhaust} = \frac{Q_{sensible}}{1.08 \times (T_{indoor} - T_{outdoor})} + \frac{\dot{m}_{moisture}}{0.075 \times (W_{indoor} - W_{outdoor})}$$

Use the greater of sensible or latent ventilation requirement. For many laundries, latent load dominates requiring 10,000-20,000 CFM total exhaust for 1,000 ft² space.

Exhaust fans mount on roof or exterior walls with gravity or motorized backdraft dampers. Centrifugal fans suit high static pressure applications (1.5-3.0 in. wc), while axial fans work for low-resistance installations. All exhaust fans require disconnect switches, vibration isolation, and weather protection.

## Makeup Air Systems

Exhausting 10,000-20,000 CFM creates substantial building depressurization unless compensated by dedicated makeup air. Uncontrolled infiltration through doors, cracks, and elevator shafts occurs if makeup air is inadequate, causing drafts, door-closing difficulty, and infiltration of unconditioned outdoor air.

### Makeup Air Volume

Makeup air should equal 90-95% of exhaust volume, with remaining 5-10% satisfied by transfer air from adjacent conditioned spaces. Complete makeup air balance (100% makeup = 100% exhaust) creates neutral pressure, while slight negative pressure (95% makeup) prevents migration of heat and moisture into adjacent hotel areas.

For laundry exhausting 15,000 CFM total (dryers + general ventilation):
- Makeup air: $15,000 \times 0.92 = 13,800$ CFM
- Infiltration/transfer: $15,000 \times 0.08 = 1,200$ CFM

Makeup air fans interlock with exhaust fans, energizing only when exhaust operates. This prevents over-pressurization during dryer shutdown periods.

### Makeup Air Tempering

Direct introduction of outdoor air without tempering creates occupant discomfort during extreme weather. Cold winter air at 10°F requires heating to 55-60°F minimum before discharge into occupied space, while hot humid summer air benefits from cooling/dehumidification for worker comfort.

**Heating-Only Makeup Air**: Most economical approach heats outdoor air to 55-65°F using gas-fired burners or hot water coils. Discharge high in space (12-15 feet above floor) allows air to mix with room air before reaching workers. Heating capacity:

$$Q_{heating} = CFM \times 1.08 \times (T_{discharge} - T_{outdoor})$$

For 13,800 CFM raised from 10°F to 60°F:
$$Q_{heating} = 13,800 \times 1.08 \times 50 = 745,200 \text{ Btu/hr}$$

This represents significant heating load—a 750 MBH makeup air heater nearly doubles hotel boiler capacity.

**Cooling and Dehumidification**: Humid climates benefit from makeup air cooling to remove moisture before introduction to space. Direct-expansion cooling coils sized for 40-50°F leaving air temperature dehumidify while cooling. Cooling capacity requirements:

$$Q_{cooling} = CFM \times 4.5 \times (h_{outdoor} - h_{supply})$$

where $h$ represents air enthalpy (Btu/lb). For 80°F/70% RH outdoor air (enthalpy 35.5 Btu/lb) cooled to 55°F/90% RH (enthalpy 23.0 Btu/lb):

$$Q_{cooling} = 13,800 \times 4.5 \times (35.5 - 23.0) = 776,700 \text{ Btu/hr (65 tons)}$$

This cooling load often proves economically unjustifiable given laundry heat gains. Most facilities use heating-only makeup air in cold climates and direct untempered outdoor air in warm climates.

### Makeup Air Distribution

Makeup air distributes through low-velocity diffusers (500-800 FPM) positioned to create air mixing without drafts on workers. Wall-mounted diffusers discharge horizontally across ceiling allowing air warming before reaching occupied zone. Floor-level distribution works only when makeup air is tempered to within 10°F of space temperature.

Avoid discharging makeup air directly onto workers, especially in heating mode where 55-60°F supply creates discomfort. Position diffusers above equipment or in circulation aisles, allowing air to mix with room temperature before contact with occupants.

## Heat Recovery Opportunities

Laundry exhaust air contains substantial energy—15,000 CFM at 90°F represents 1.5 million Btu/hr sensible heat at 40°F outdoor temperature differential. Heat recovery systems capture this energy, preheating makeup air and reducing heating costs by 40-70%.

### Air-to-Air Heat Exchangers

Plate heat exchangers or heat wheels transfer energy from exhaust airstream to makeup air without mixing air streams. Effectiveness ranges 50-75% depending on design, calculated as:

$$\epsilon = \frac{T_{MAU,leaving} - T_{outdoor}}{T_{exhaust} - T_{outdoor}}$$

For 70% effectiveness with 90°F exhaust and 20°F outdoor air:
$$T_{MAU} = 20 + 0.70 \times (90-20) = 69°F$$

This preheats makeup air from 20°F to 69°F, reducing supplemental heating from 50°F rise to 19°F rise (62% heating energy savings).

Equipment considerations:
- **Plate exchangers**: No moving parts, 50-65% effectiveness, require lint filtration on exhaust to prevent fouling
- **Heat wheels**: 65-75% effectiveness, rotating components need maintenance, optional enthalpy recovery for moisture transfer
- **Run-around coils**: Flexibility in equipment placement, 45-60% effectiveness, glycol pumps add parasitic energy

### Exhaust Air Heat Pumps

Heat pumps extract energy from exhaust air producing 100-140°F hot water for laundry washing, domestic hot water, or space heating. Systems achieve COP 3.0-4.0 using waste heat that otherwise discharges to atmosphere.

A 15,000 CFM exhaust stream at 90°F contains recoverable heat:
$$Q_{available} = 15,000 \times 1.08 \times (90-32) = 939,600 \text{ Btu/hr}$$

A heat pump recovering 60% of available heat produces:
$$Q_{recovered} = 939,600 \times 0.60 = 563,760 \text{ Btu/hr}$$

At COP 3.5, this requires compressor power:
$$P_{compressor} = \frac{563,760}{3.5 \times 3412} = 47 \text{ kW}$$

Annual energy savings depend on hot water demand coinciding with laundry operation. Properties with all-electric resistance domestic hot water see greatest savings, while facilities with efficient gas boilers see reduced benefit.

### Economic Analysis

Heat recovery equipment costs $15-35/CFM installed depending on complexity. For 15,000 CFM system:
- Equipment cost: $225,000 - $525,000
- Annual heating savings: $8,000 - $20,000 (varies by climate and fuel cost)
- Simple payback: 11-65 years

This wide payback range explains limited heat recovery adoption in hotel laundries. Cold climates with high heating costs justify investment, while mild climates or properties with low energy costs cannot economically support heat recovery equipment.

## Space Conditioning Strategy

Most commercial laundries operate without mechanical cooling, relying on high ventilation rates to remove heat. This creates summer working conditions of 85-95°F and 50-60% RH—tolerable for laundry staff but uncomfortable by typical commercial building standards.

Partial air conditioning using evaporative cooling or small DX units provides spot cooling at folding stations where workers spend concentrated time. This hybrid approach maintains 75-80°F at worker positions while allowing equipment areas to rise to 90-95°F.

Design considerations for laundry air conditioning:
- Size systems for 85°F indoor design temperature versus 72-75°F in office areas
- Accept higher humidity (55-60% RH) to reduce dehumidification load
- Use high-efficiency filtration (MERV 8-11) to capture lint before coils
- Schedule cooling only during occupied hours (8 AM - 6 PM typically)
- Consider refrigerant type—lint poses fire risk with flammable refrigerants

## Code and Safety Requirements

Laundry spaces classification as mechanical equipment spaces requires 1-hour fire-rated separation from occupied hotel areas in many jurisdictions. Dryer exhaust ductwork must be metal with cleanable access panels every 10-15 feet, terminating through fire-rated construction with listed fire dampers.

Gas-fired dryers require combustion air provisions at 50 CFM per 1,000 Btu/hr input (typical 150 MBH dryer needs 7,500 CFM) unless using direct-vent sealed combustion models. This combustion air comes from makeup air system or dedicated outdoor air intakes.

Electrical disconnects mount within sight of each major appliance (washers, dryers, ironers) for maintenance safety. Ground fault circuit interrupter (GFCI) protection required for all 120V receptacles in wet areas per NEC.
