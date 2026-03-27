# ETL Application: Management Brief

## ETL Definition: 
ETL stands for Extract, Transform, and Load. It is a critical data integration process used in IT to pull raw data from various sources (databases, APIs, files), clean and reformat it (transform), and load it into a centralized system like a data warehouse for analytics and business intelligence. 
- ***Extract***: Gathering data from multiple, disparate sources, such as CRM systems, ERPs, or SQL databases.
- ***Transform***: Cleaning, filtering, validating, and standardizing the data so it conforms to a unified format.
- ***Load***: Moving the processed data into a target database, data lake, or warehouse. 

While sometimes considered traditional, ETL remains highly relevant, alongside modern approaches like ELT (Extract, Load, Transform), particularly when complex transformations are needed before data reaches its destination.

## What This Application Is

This repository is a Python-based operational reporting and data automation suite that supports multiple Marquette School of Dentistry workflows. While the codebase is labeled as an ETL project, it functions as a broader reporting platform that:

- extracts data from clinical, imaging, academic, and departmental systems,
- transforms and validates those data for business use,
- loads curated results into internal databases and web-facing dashboards, and
- distributes reports through PDFs, CSV files, and email.

In management terms, this is a business-critical back-office automation asset for student progress tracking, clinical oversight, quality assurance, and referral follow-up.

## Executive Summary

The application portfolio is centered on one large clinical requirements pipeline and several smaller specialty reporting workflows. Together they support oversight of student clinical progression, radiology quality review, internal referrals, and faculty reporting.

The largest workflow, `main_clinical_requirements.py`, orchestrates a multi-stage batch process that pulls from several data sources, updates ETL and Django-backed reporting tables, and generates dashboards and PDF summaries across multiple class years. Additional top-level scripts handle radiology QA, pathology and perio referrals, graduate prosthodontics reporting, and other specialty tasks.

The codebase shows evidence of long-term operational value and institutional knowledge, but it also reflects organic growth. The main management concern is not whether the application is useful; it clearly is. The concern is operational resilience. The system depends on manually created credential and recipient files, hardcoded year-specific logic, local file staging, and external scheduling that is not defined in the repository. These are manageable risks, but they increase support burden and key-person dependency.

## Business Scope And Users

The application appears to serve these primary groups:

- academic leadership monitoring student clinical requirement completion,
- departmental and course leaders reviewing dashboards, case progress, and conference readiness,
- faculty and staff receiving specialty reports by email,
- informatics and IT staff supporting batch execution, credentials, and data troubleshooting.

The practical business outcomes are:

- earlier visibility into students at risk of falling behind,
- reduced manual reporting effort,
- more consistent departmental reporting,
- quality assurance checks across imaging and documentation workflows,
- faster follow-up for internal referrals and incomplete records.

## Major Application Areas

| Area | Primary Purpose | Typical Outputs |
|---|---|---|
| Clinical Requirements | Tracks student progress against clinical requirements and dashboards across class years | Database updates, CSV staging files, dashboards, department PDFs, class summaries, grading matrices |
| Radiology CBCT QA | Compares imaging records with Axium form/documentation records | QA CSVs and email distribution |
| Radiology Notes QA | Identifies note quality/documentation issues for radiology notes | Text summary, CSV exceptions, email distribution |
| Pathology Internal Referrals | Tracks oral pathology referral follow-up and reporting | PDF report and email distribution |
| Perio Internal Referrals | Tracks periodontal internal referral status | PDF report and email distribution |
| Graduate Prosthodontics Reports | Checks treatment plan form completion and reporting status | CSV report, optionally email |
| CBCT Referrals | Historical referral processing workflow using SharePoint inputs | DB updates, PDFs, email; code notes indicate this workflow is no longer actively used in its former form |

## Core Systems And Dependencies

The repository shows direct dependency on several upstream and downstream systems.

### Upstream Data Sources

- Axium clinical systems
- MiPACS imaging records
- Dolphin orthodontic records
- D2L academic data
- SharePoint file intake for at least one referral workflow
- MUSOD Django application database
- BI or staging databases used for reporting extracts

### Downstream Targets

- local ETL project database tables,
- MUSOD Django reporting/dashboard tables,
- local output folders for staged files and generated reports,
- email recipients through Office 365 SMTP.

### Local Runtime Dependencies

The application also depends on a local runtime structure that must exist for successful execution:

- `output/` subfolders for report generation,
- `spreadsheet/` for local file staging,
- `log/` for application logging,
- `db_credentials/credentials.py` for connection details,
- `mail_recipients.py` for report routing.

This means the application is not fully self-contained or environment-neutral in its current form.

## Operating Model

The codebase follows a batch-processing pattern.

### What The Main Pipeline Does

The main clinical requirements process executes in a sequence that roughly looks like this:

1. Extract raw data from source systems.
2. Stage intermediate files locally, including CSV and pickle files.
3. Load or refresh ETL tables.
4. Calculate requirement summaries and dashboard metrics.
5. Update reporting artifacts for multiple class years.
6. Generate PDF outputs and other summary reports.

The workflow naming convention, especially the `daily_XX_*` modules, strongly suggests daily scheduled operation. However, the scheduler itself is not defined in the repository, which means orchestration is likely external to the codebase.

### Logging And Traceability

The application writes log files locally. The clinical requirements logger uses daily rotation with retention, which is a positive operational practice. Other workflows log to static log files without the same rotation model.

### Distribution Model

Several workflows end by emailing reports and attachments to configured distribution lists. This makes the application both a data pipeline and a communications mechanism for business operations.

## Outputs Management Should Care About

From a management perspective, the most important recurring outputs are:

- student and department performance dashboards,
- conference and graduation-readiness reporting,
- PDF summaries for faculty and department review,
- specialty QA exception reports,
- referral follow-up reports,
- audit-style CSV files used for investigation and reconciliation.

These outputs directly support academic operations, clinical oversight, and compliance-like review activity within the school.

## Key Management Risks

### 1. Configuration And Credential Risk

The code depends on local Python files for credentials and email recipients rather than centralized configuration. This creates support friction, inconsistent setup across environments, and elevated operational risk if staff change or environments are rebuilt.

### 2. Hardcoded Year Logic

The clinical requirements workflow contains multiple class-year-specific modules and report generators for years such as 2024 through 2027. This means new cohorts are not simply data changes; they typically require code updates and release effort.

### 3. External Scheduler Dependency

The repository does not define how jobs are scheduled or monitored. If scheduling is handled elsewhere, the runbook, ownership, and alerting path are not visible here. That increases key-person dependency and slows recovery when jobs fail.

### 4. Local File Staging And Recovery Risk

The application stages intermediate artifacts locally using CSV, Excel, PDF, and pickle files. This design is workable, but recovery after partial failure can be harder because job state is spread across database tables, output folders, and serialized local files.

### 5. Mixed Maturity Across Workflows

Some workflows are clearly active and structured, while others appear legacy, partially disabled, or manually versioned. Examples include copy-named scripts and code comments noting workflows that are no longer used. This increases ambiguity about what is production-critical versus historical.

### 6. Monitoring Gap

Logging exists, but there is no visible application-level health dashboard, failure alerting, or centralized monitoring pattern in the repository. A failed run may therefore rely on someone noticing missing output rather than receiving immediate alerting.

## Overall Assessment

This is a high-value operational application portfolio with clear institutional importance. It likely saves substantial manual effort and enables oversight that would otherwise be fragmented across clinical and academic systems.

At the same time, it appears to be a mature but fragile platform: strong business utility, moderate technical debt, and meaningful dependence on local environment setup and accumulated domain knowledge. It should be treated as a supported operational service rather than a collection of ad hoc scripts.

## Recommended Management Priorities

### Near-Term Priorities

- Standardize configuration using environment variables or managed configuration instead of local credential and recipient files.
- Define and document the production scheduler, run order, ownership, and recovery steps.
- Separate active production workflows from legacy or deprecated scripts.
- Establish a simple failure-alerting mechanism for missed or failed daily runs.

### Mid-Term Priorities

- Reduce hardcoded class-year logic by moving to parameter-driven cohort handling.
- Consolidate common reporting, emailing, and database connection patterns.
- Improve restart safety for workflows that rely on intermediate local files.
- Add a lightweight system inventory showing inputs, outputs, owners, and report consumers.

### Strategic View

If this platform will remain central to school operations, it merits treatment as an internal application with explicit lifecycle management, not just script maintenance. The business case for modernization is operational continuity, reduced support burden, and lower dependence on a small number of experts.

## Bottom Line

Management should view this repository as an operational reporting platform that underpins student progress reporting and several specialty oversight processes. It is delivering real value today, but the main opportunity is to harden how it is configured, scheduled, monitored, and maintained so that the institution is less exposed to avoidable operational risk.

