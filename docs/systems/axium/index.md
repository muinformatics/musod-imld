
# axiUm — Overview
_(This page is intentionally non-procedural and exists only to orient and link.)_

## Purpose
axiUm (Exan) is MUSoD’s primary clinical system of record for patient, scheduling, treatment, and related clinic workflows.

In the context of “Arms Around” documentation, this section focuses on **how teams discover, interpret, and extract axiUm data** for reporting, dashboards, and research-support.

## Who This System Serves
- Clinic operations and leadership
- Faculty and students (clinical workflows)
- Informatics / analytics / reporting
- ITS / application support

## What This System Does
- Clinical workflow and EHR-style documentation
- Scheduling and operational tracking
- Reporting via built-in and external tools
- Data source for downstream dashboards/ETL (where applicable)

## What This System Touches
- **Oracle databases** (production, training, development)
- **BI staging database** (Microsoft SQL Server) with a **subset of tables** refreshed overnight
- **Reporting/extraction tooling** (Info Manager, Crystal Reports, SSMS, SQL*Plus, Python-based extracts)
- **Documentation and access portals** (Exan portal; internal shares)

## Where the Real Docs Live
- Internal file share (technical docs and source files): `S:\Informatics\Administration\aXium\Technical Documentation`
- Exan portal: https://exan.force.com/axium/s/
- ConsortiumEDR: https://www.consortiumedr.org/
- Credential storage (institutional): https://passwordstate.marquette.edu

## Common Entry Points
- **I need a quick report** → Info Manager (canned/custom reports)
- **I need to modify/author a report** → Crystal Reports (compatibility constraints apply)
- **I need dashboard/analytics data** → BI staging database via SQL Server tooling
- **I need full-fidelity source data** → Oracle (coordinate access and avoid unnecessary load)
- **I need schema context** → Data dictionary + ERDs (see Links)
- **I need orientation for data work** → Guide

