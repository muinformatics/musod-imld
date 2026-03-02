# axiUm Data Access — Guide Overview
_(This page/template is intentionally non-procedural and exists only to orient and link.)_

## Who This Is For
- Informatics/analytics staff pulling axiUm data for dashboards, reporting, or research-support
- Report authors working in Info Manager / Crystal Reports
- ITS support roles coordinating access and data movement

## What You’ll Find Here
- How to think about axiUm environments (Oracle vs staging)
- What tools are commonly used for extraction/reporting
- Common data-shape pitfalls to watch for (counts, identifiers, “status”, demographics)
- Where to find authoritative technical references

## What You Won’t Find Here
- Step-by-step query tutorials or report-building procedures
- A comprehensive data model explanation
- Policy guidance (HIPAA/FERPA, data governance); defer to institutional policy sources

## Systems You’ll Interact With
- axiUm application (clinical system)
- Oracle databases (production/training/dev)
- BI staging database (Microsoft SQL Server; subset of tables)
- Tools: Info Manager, Crystal Reports, SSMS, SQL*Plus, Python-based extracts
- Exan portal + internal technical documentation shares

## Common Tasks
- Locate the right reference artifact (data dictionary / ERDs) before querying
- Decide where to pull data from (staging vs Oracle) based on fidelity, refresh, and impact
- Validate whether “unique vs total” counts are intended for a request
- Identify and mitigate known data consistency issues (field usage conventions vary)

## Where to Go Next
- System overview: index.md
- Technical reference links: links.md
- Related system: ETL (if this work feeds pipelines/dashboards): ../etl/index.md
