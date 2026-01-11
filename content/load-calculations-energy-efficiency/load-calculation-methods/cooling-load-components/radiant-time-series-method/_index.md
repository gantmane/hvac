---
title: "Radiant Time Series Method"
description: "Advanced cooling load calculation using radiant time series (RTS) method with time-dependent response factors for accurate modeling of thermal mass effects and radiant heat transfer."
weight: 3
---

## Method Overview

The Radiant Time Series (RTS) method represents a simplified implementation of the heat balance approach for cooling load calculations, providing higher accuracy than traditional transfer function methods while maintaining computational efficiency suitable for hourly simulations. RTS accounts for the time-dependent conversion of radiant heat gains into cooling loads through the use of pre-calculated response factors that characterize how building thermal mass absorbs and releases radiant energy over multiple hours.

The fundamental principle recognizes that radiant heat gains from solar radiation, lighting, and equipment do not immediately become cooling loads. These radiant gains first strike and are absorbed by room surfaces (walls, floor, ceiling, furnishings), then are released to the room air through convection over subsequent hours. The time lag and magnitude of the delayed cooling load depend on the thermal properties, surface area, and arrangement of room surfaces.

## Theoretical Foundation

RTS methodology separates heat gains into convective and radiant fractions. Convective gains immediately become cooling loads since they directly warm the room air. Radiant gains undergo time-dependent conversion characterized by response factors. The cooling load at any hour equals the sum of current-hour convective gains plus radiant gains from the current and previous 23 hours, each multiplied by appropriate response factors.

Mathematically, the cooling load from a radiant heat source is expressed as:

q(θ) = r₀·q_rad(θ) + r₁·q_rad(θ-1) + r₂·q_rad(θ-2) + ... + r₂₃·q_rad(θ-23)

where q(θ) is cooling load at hour θ, q_rad represents radiant heat gain at various hours, and r₀ through r₂₃ are radiant time factors. The radiant time factors sum to unity, ensuring all radiant energy eventually becomes cooling load.

## Radiant Time Factors

Radiant time factors (RTFs) quantify the fraction of radiant heat gain occurring at hour zero that converts to cooling load at the current hour and each of the subsequent 23 hours. ASHRAE provides tabulated RTF values for different zone construction types ranging from lightweight (minimal thermal mass) to heavyweight (significant concrete or masonry mass).

Lightweight construction exhibits high r₀ values (0.4-0.6), meaning 40-60% of radiant gains immediately become cooling load with rapid decay of subsequent time factors. Heavyweight construction shows lower r₀ values (0.2-0.3) with more uniform distribution across multiple hours, indicating strong thermal storage effects that delay and distribute the cooling load. Medium-weight construction falls between these extremes.

Zone thermal mass classification depends on exposed mass per unit floor area. Lightweight zones have less than 30 lb/ft² exposed mass, medium zones range from 30-70 lb/ft², and heavyweight zones exceed 70 lb/ft². Carpet and ceiling tiles reduce effective thermal mass by insulating floor and ceiling slabs from radiant exchange with the space.

## Solar Radiant Time Factors

Solar radiation transmitted through glazing follows different time-dependent behavior than non-solar heat gains due to complex directional characteristics and varying incidence points on room surfaces. The method employs separate solar radiant time factors (SRTF) that account for the absorption-release process specific to transmitted solar radiation.

Solar RTFs typically show slightly slower response than non-solar factors since beam solar radiation may strike and be absorbed by specific surfaces with thermal properties differing from the average zone construction. The angular dependence of beam radiation and surface solar absorptance creates varying thermal response depending on sun position and room geometry.

## Conduction Time Series

Opaque surface heat gains from conduction through walls and roofs use conduction time series (CTS) factors to account for thermal mass effects in the envelope assembly itself. CTS factors represent the hourly heat flux at the interior surface resulting from a triangular pulse of sol-air temperature 24 hours earlier. These factors are assembly-specific, depending on layer properties, thickness, and arrangement.

The conduction cooling load calculation requires 24-hour history of sol-air temperature for each surface orientation and construction type. The current-hour cooling load equals the sum of current and previous 23-hour sol-air temperatures, each multiplied by the appropriate CTS factor. Heavyweight constructions exhibit CTS factors distributed over many hours with significant damping, while lightweight assemblies show concentrated factors with minimal damping.

## Non-Solar Radiant Time Factors

Internal radiant gains from lighting, people (radiant portion), and equipment apply non-solar RTFs. These factors assume radiant energy distributes uniformly throughout the space rather than focusing on specific surfaces. The uniform distribution assumption simplifies calculations while providing reasonable accuracy for typical commercial spaces with distributed heat sources.

Different room constructions use distinct non-solar RTF values accounting for varying thermal storage capacity. Lightweight construction provides minimal storage, resulting in rapid conversion to cooling load. Massive construction stores radiant gains longer, creating substantial time lags between heat generation and cooling load peaks. This storage effect enables precooling strategies and thermal energy storage applications.

## Split Calculations for Zone Response

The RTS method calculates cooling loads separately for each heat gain component (walls, roof, windows, lights, occupants, equipment, infiltration), applies appropriate response factors, then sums the time-dependent results to determine total zone cooling load at each hour. This component-wise approach enables detailed analysis of load composition and timing.

Convective heat gains including infiltration sensible and latent loads, convective portions of internal gains, and ventilation loads sum directly without applying time factors since they immediately impact zone air temperature and humidity. The total sensible cooling load at any hour equals the sum of all current-hour convective gains plus the time-series summation of all radiant gain components.

## Accuracy and Limitations

RTS method accuracy significantly exceeds traditional CLTD/CLF approaches by properly modeling thermal storage in buildings with significant mass. Validation studies show agreement within 5-10% of detailed heat balance methods for typical commercial construction. The simplified response factor approach executes rapidly compared to full heat balance calculations while capturing essential physics of radiant heat transfer and thermal storage.

Limitations include the assumption of uniform room temperature and surface temperatures, which may not hold in large spaces or with strongly directional heat sources. The method assumes 24-hour periodicity, limiting accuracy for spaces with varying schedules or operating modes across multiple days. Furnishings and interior partitions are approximated through adjustment of effective zone thermal mass rather than explicit modeling.

## Implementation in Load Calculation Software

Major commercial load calculation programs including Carrier HAP, Trane TRACE, and ASHRAE's RTS toolkit implement the radiant time series method. Software automates the time-series calculations, storage of 24-hour gain histories, and application of appropriate response factors based on user-specified construction assemblies and zone characteristics.

Users specify zone construction type (lightweight, medium, heavyweight) either through direct selection or automatic classification based on entered surface materials and areas. The software accesses libraries of pre-calculated RTS, CTS, and SRTF values for standard construction assemblies. Custom assemblies may require calculation of new response factors using specialized tools or reversion to simpler calculation methods.

## Design vs. Annual Energy Analysis

RTS methodology applies equally to peak design load calculations and annual energy analysis. For design applications, the method determines peak cooling load magnitude and timing to support equipment sizing. For energy analysis, hour-by-hour loads throughout the year enable calculation of annual energy consumption, part-load operation, and integration with plant simulation tools.

The ability to accurately predict hour-by-hour load profiles supports optimization of thermal storage systems, demand response programs, and equipment scheduling. Coincident load analysis for multi-zone systems correctly accounts for time-dependent load distributions across different exposures and occupancy patterns, preventing the oversizing that results from simple peak summation methods.
