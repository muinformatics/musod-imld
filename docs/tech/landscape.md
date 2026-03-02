# Technology Landscape

This page provides a **cross-system view** of the major technologies used across MUSoD systems, showing:

- Where each technology is used
- What role it plays
- Why it matters operationally

This is **not a dependency inventory** and **not a skills matrix**.  
It exists to support shared understanding and supportability.

---

## Application Frameworks & Runtimes

| Technology | Used By | Purpose | Notes |
|-----------|--------|---------|------|
| Python | MusodDjango, ETL, Phone API | Core application and scripting language | Version differences exist across systems |
| Django | MusodDjango | Primary web application framework | Hosts multiple internal apps/modules |
| Delphi (Legacy) | X-Ray Interface | Desktop application for X-ray capture | Legacy, limited maintainability |
| MSSQL, SQLAlchemy | ETL | Data extraction and transformation | Primary source for clinical data |
| MSSQL | MusodDjango | Application database | Stores operational and reporting data |

---

## Data & Reporting Technologies

| Technology | Used By | Purpose | Notes |
|-----------|--------|---------|------|
| SQLAlchemy | ETL | Extract clinical, attendance, grading data | Performance sensitive |
| Python ETL Scripts | ETL | Batch processing and aggregation | Long-running jobs (4.5–5 hrs) |
| PDF Generation | ETL | Static reporting for faculty/students | Outputs consumed manually |
| CSV Files | ETL | Intermediate data exchange | Used heavily across stages |

---

## External & Third-Party Systems

| System | Used By | Role | Notes |
|------|--------|------|------|
| axiUm | MusodDjango, ETL, Phone API | Clinic operations system | Vendor-managed, constrained integration |
| BI / Data Warehouse | ETL | Historical clinical data | Used for multi-year lookbacks |
| D2L / DataMarq | ETL | Academic assessment data | Limited scope integrations |

---

## Integration & Interfaces

| Interface | Used By | Direction | Notes |
|----------|--------|-----------|------|
| Phone API | MusodDjango ↔ axiUm | Bi-directional (planned) | Still evolving |
| File-based Integration | ETL ↔ Consumers | One-way (output) | PDF and CSV distribution |
| Database Access | ETL ↔ Oracle/Postgres | Read-heavy | High impact on runtime |

---

## Documentation Systems

> These systems define how institutional knowledge and technical detail are captured, maintained, and shared.
> They are intentionally separated by audience and stability.


| Documentation System | Used For                                           | Audience                      | Notes                                                    |
| -------------------- | -------------------------------------------------- | ----------------------------- | -------------------------------------------------------- |
| Sphinx               | MusodDjango technical documentation                | Developers, Engineers         | Source-code aligned; detailed, version-sensitive         |
| MkDocs (Material)    | IMLD (Institutional Memory & Living Documentation) | Faculty, Admin, IT, New Staff | Human-oriented; system and workflow focused              |
| MkDocs (Material)    | ETL Technical Documentation (future)               | Engineers, Analysts           | Execution- and pipeline-oriented; CLI and data contracts |

---

## Infrastructure & Environments

| Area | Description |
|----|-------------|
| Hosting | Multiple environments (Prod / Sand / Test) depending on system |
| Scheduling | ETL jobs run on scheduled execution |
| File Storage | Shared directories for report distribution |
| Authentication | SSO and credentials depending on system |

---

## Cross-Cutting Concerns

### Performance Sensitivity
- ETL runtime is heavily affected by:
  - Oracle query performance
  - Data volume (multi-year lookbacks)
  - PDF generation fan-out

### Stability vs Change
- MusodDjango: moderate to high change velocity
- ETL: relatively stable logic, heavy execution cost
- Phone API: high uncertainty, active development
- Legacy systems: stable but fragile

### Risk Concentration
- Vendor systems (axiUm) impose hard constraints
- Long-running ETL jobs concentrate operational risk
- Legacy desktop tooling has low bus-factor resilience

---

## How This Landscape Is Used

- **System pages** link back here to show dependencies
- **Ops pages** reference this when diagnosing failures
- **Future architecture work** uses this as a baseline

If a technology materially impacts operations or decision-making, it belongs here.

---

## Known Gaps (v0.1)

- Full environment mapping (hostnames, tiers)
- Monitoring/alerting visibility by system
- Precise ownership boundaries for legacy components

These will be filled incrementally as systems are documented.

---

## Navigation

- ⬅️ Back to: [Technology Overview](index.md)
- ➡️ Next: [Systems Index](../systems/index.md)
