
# axiUm — Technical Reference (Links)
_(This page/template is intentionally non-procedural and exists only to orient and link.)_

## Intended Audience
Informatics/analytics staff, report authors, developers, and ITS support roles who need **technical artifacts** related to axiUm.

## Scope
This page links to technical references such as:
- Data dictionaries / table dictionaries
- ER diagrams
- Environment overview (production vs training vs dev vs staging)
- Reporting and extraction tool references
- Institutional access points (portals, credential systems)

## Non-Scope
This page does not provide step-by-step instructions for:
- Writing SQL queries
- Building reports/dashboards
- Provisioning accounts
- Performing upgrades

## System Map
- Overview: ../axium/index.md
- Guide (orientation): guide.md
- Related systems: ETL (if/when data pipelines exist): ../etl/index.md

## Source of Truth
- Vendor artifacts and cases: Exan portal
- Institutional operational ownership: ITS application support + data management
- Institutional “known issues” and conventions: MUSoD informatics/reporting practice

## Key References
- Exan portal: https://exan.force.com/axium/s/
- ConsortiumEDR: https://www.consortiumedr.org/
- Credential storage (institutional): https://passwordstate.marquette.edu
- Internal technical documentation: `S:\Informatics\Administration\aXium\Technical Documentation`

## Commonly Used Artifacts (as referenced in internal discussions)
- Database table dictionary (multiple versions may exist; newer versions may require a case request)
- ERDs (vendor-provided)
- Report/source file locations (Crystal reports, SQL scripts) on internal shares

## Data Caveats to Keep in Mind
- BI staging is a **subset** of axiUm tables and is refreshed overnight; refresh behavior may vary by table.
- Differences between staging and production can exist; validate assumptions when answering data questions.
- Some data elements may be inconsistently populated (e.g., demographic fields) and require careful interpretation.

