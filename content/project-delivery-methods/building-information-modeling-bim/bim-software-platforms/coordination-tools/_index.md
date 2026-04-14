---
title: "BIM Coordination Tools"
aliases: ["BIM Coordination Tools"]
description: "BIM coordination software including Navisworks Manage, Solibri Model Checker, BIM 360 Glue, Synchro 4D, and coordination platforms for clash detection, model federation, and multi-discipline integration."
weight: 3
---

BIM coordination tools aggregate models from multiple disciplines enabling clash detection, constructability review, 4D schedule simulation, and collaborative coordination workflows. These platforms form the technical backbone of multi-discipline BIM coordination identifying conflicts before construction and facilitating resolution among design teams.

## Navisworks Manage

Autodesk Navisworks Manage represents the industry standard for BIM coordination in North American construction. The platform aggregates models from Revit, AutoCAD, MicroStation, and other sources creating federated models preserving discipline separation while enabling holistic coordination analysis. Clash detection automatically identifies physical conflicts between building elements categorizing by severity and affected disciplines.

Navisworks coordination workflow includes importing discipline models, establishing clash detection rules and tolerances, running automated clash tests, generating clash reports, conducting coordination meetings reviewing conflicts, and tracking clash resolution status. The platform supports viewpoint markup enabling coordinators to capture specific conflict views with annotations communicating required changes. 4D simulation links models to construction schedules visualizing building sequences and identifying temporal conflicts.

## Solibri Model Checker

Solibri provides rule-based model checking verifying compliance with modeling standards, code requirements, design criteria, and project specifications. The platform analyzes models against customizable rule sets checking for modeling errors, code violations, incomplete information, and design inconsistencies. Rule-based checking extends beyond geometric clash detection to semantic validation ensuring models contain required information at appropriate quality.

Solibri's strength lies in systematic quality verification. Pre-configured rule sets address common standards including IFC compliance, accessibility requirements, egress analysis, and space program validation. Custom rules can verify project-specific requirements including naming conventions, parameter completeness, or design standard compliance. Batch checking enables consistent validation across multiple models or project phases documenting quality metrics over time.

## BIM 360 Glue

Autodesk BIM 360 Glue (now integrated into BIM 360 Design) provides cloud-based coordination accessible from any internet-connected device including tablets enabling field review. Cloud coordination democratizes model access beyond design team to contractors, owners, and field personnel. Mobile access enables on-site coordination review validating buildability during construction.

BIM 360 collaboration features include issue tracking, model viewing, markup tools, and coordination meeting documentation integrated within single platform. Issues identified in coordination link directly to model locations with photographic documentation, assigned responsibility, and status tracking. Integration with Autodesk Construction Cloud connects design coordination seamlessly to construction management workflows.

## Synchro 4D

Synchro specializes in 4D construction simulation linking 3D models to construction schedules visualizing building sequence over time. The platform imports schedules from Primavera P6, Microsoft Project, or other scheduling tools linking activities to model elements. Time-based simulation identifies temporal conflicts where construction sequence creates physical impossibilities, access problems, or logistical challenges.

4D simulation supports construction planning, sequence optimization, site logistics planning, and stakeholder communication. Visualizing construction sequence helps identify crane positioning requirements, temporary support needs, and material staging logistics. Owner presentations using 4D simulations communicate construction impacts on operations more effectively than Gantt charts enabling informed decisions about phasing and occupancy timing.

## Vico Office

Vico Office integrates 5D cost estimation with 4D scheduling creating construction planning platform linking geometry, schedule, and cost. The tool enables quantity takeoffs from models, cost database integration, schedule development, and resource optimization. Integration among geometric, temporal, and financial dimensions supports construction planning, bid validation, and project control.

Vico workflow involves model import, quantity extraction, cost database application, activity definition, productivity rate assignment, and resource optimization. Results quantify project costs, identify schedule drivers, optimize resource allocation, and support what-if scenario analysis. Owners and construction managers use Vico for bid validation, budget development, and construction feasibility assessment before committing to designs.

## Federated Model Management

Federated models maintain discipline model separation while enabling coordinated viewing and analysis. This approach preserves each discipline's authoring control while creating composite views for coordination. Model federation requires establishing protocols for model submission frequency, coordinate system alignment, model origin consistency, and version tracking.

Federation platforms aggregate models using relative or absolute coordinate systems ensuring spatial alignment. Misaligned models create false clashes and coordination confusion requiring careful setup and validation. Reference point establishment at project initiation prevents alignment problems. Discipline coordinators manage model updates ensuring latest versions load into federated environments.

## Clash Detection Protocols

Effective clash detection requires establishing tolerance settings, classification rules, and resolution workflows. Hard clashes where elements physically occupy same space demand resolution. Soft clashes violating clearance requirements may permit field coordination within defined tolerances. Duplicate clashes representing same conflict identified multiple ways need consolidation preventing redundant resolution efforts.

Clash reports organize conflicts by location, severity, and responsible disciplines. Priority assignment focuses resolution on critical path conflicts affecting major distribution or equipment. Minor conflicts involving small branches or trim may delegate to field coordination. Clash status tracking documents which conflicts are resolved, assigned, under review, or disputed ensuring systematic resolution before construction.

## Coordination Meeting Facilitation

Coordination platforms support structured meetings displaying federated models, reviewing clash reports, capturing resolution decisions, and assigning action items. Screen sharing enables distributed team participation. Viewpoint markup captures agreed resolutions with annotations explaining required changes. Meeting minutes document decisions, responsibility assignments, and follow-up requirements.

Post-meeting workflows include implementing agreed changes in discipline models, updating clash status, verifying clash resolution, and preparing for subsequent coordination cycles. Iterative coordination continues until critical clashes resolve and remaining conflicts have documented field coordination strategies. Final coordination models represent agreed design before construction document issuance.

## Performance Considerations

Large federated models strain computer performance and network bandwidth. Aggregating multiple disciplines' detailed models creates datasets exceeding typical hardware capabilities. Performance optimization includes simplifying models for coordination removing excessive detail, caching models locally reducing network dependency, and using workstation-class hardware with adequate RAM and graphics capabilities.

Cloud-based coordination shifts computational requirements to server infrastructure but introduces network bandwidth dependencies and latency. Reliable high-speed internet becomes critical for cloud coordination workflows. Offline capabilities enable review without internet connection with synchronization when connectivity restores.
