# Technology (IMLD)

This section provides a *high-level* view of the technologies MUSoD systems depend on.  
It is intentionally **not exhaustive**. The goal is institutional clarity:

- What we run
- What it connects to
- What tends to break
- Where to find deeper technical documentation

If you are looking for a specific application, start in **[Systems](../systems/index.md)**.

---

## How to use this section

- **Faculty / Administration:** use this to understand what platforms are involved and where data comes from.
- **IT / Support:** use this to locate likely failure points, ownership, and operational constraints.
- **Engineers / Analysts:** use this as a navigation hub into system-specific deep docs.

---

## Technology Landscape (At a Glance)

> The categories below represent the major “layers” of the MUSoD ecosystem.

### Application Platforms
- **MusodDjango** (Primary web application)
- **Legacy desktop utilities** (e.g., X-Ray Interface)

### Data & Reporting
- **ETL / batch processing** (SQL + scripting + PDF outputs)
- **Dashboards / static reporting** (PDF generation and distribution)

### External / Third-Party Systems
- **axiUm** (clinic operations platform; source of clinical scheduling and treatment records)

### Integration Interfaces
- **Phone API** (in development; evolving integrations with axiUm scheduling)

### Infrastructure & Environments
- Hosting environments (Prod / Sand / Test as applicable)
- File shares / distribution paths used for report delivery
- Scheduling/orchestration used to run ETL jobs

---

## What we document here (and what we don’t)

### We DO document
- Major technologies that materially affect operations
- Integration boundaries between systems
- High-value constraints (vendor limitations, environment assumptions)
- Operational touchpoints (where support and monitoring matters)

### We DO NOT document (in IMLD)
- Full dependency lists
- Source-level implementation details
- Developer setup instructions (those belong in technical repos)

---

## Quick Links

### System Overviews
- [MusodDjango](../systems/musoddjango/index.md)
- [ETL Dashboards](../systems/etl/index.md)
- [Phone API](../systems/phone_api/index.md)
- [axiUm](../systems/axium/index.md)
- [X-Ray Interface](../systems/xray_interface/index.md)

### Deeper Technical Documentation
> These will be linked per-system (preferred) so IMLD remains stable.

- MusodDjango Sphinx docs (link from MusodDjango → Links page)
- ETL technical docs (link from ETL → Links page)
- Phone API repo/docs (link from Phone API → Links page)

---

## Current Gaps / Known Unknowns (v0.1)

This section tracks what we *know we don’t know yet*.

- Phone API: full scope and supported endpoints still being clarified.
- X-Ray Interface: legacy behaviors and dependencies still being documented.
- Additional systems likely exist but are not yet inventoried.

If you discover a missing system, add it to the **[Systems Index](../systems/index.md)** first, then link it here.

---

## Next: Technology Landscape Page

For a more detailed breakdown (still high-level), see:  
➡️ **[Technology Landscape](landscape.md)**
