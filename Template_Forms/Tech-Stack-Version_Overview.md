# Technology Stack & Version Overview

This section provides a consolidated view of the
technology stack in use across MUSoD systems,
including operating versions and current deployed versions.

This page is descriptive only and does not define
upgrade procedures or change policy.

## Version Matrix

| Technology               | Context / System | Baseline / Operating | Current      | Notes                        |
| ------------------------ | ---------------- | -------------------- | ------------ | ---------------------------- |
| Crystal Reports (SAP)    | Reporting        | 2008                 | 2013 (2025*)⚠️ | *Not compatible with axiUm* |
| Delphi                   | Desktop Dev      | XE8                  | 13           | Legacy project lineage       |
| draw.io                  | Documentation    | 29.3 ✅             | 29.3         | —                            |
| FileZilla                | File Transfer    | 3.69.5 ✅           | 3.69.5       | —                            |
| Git                      | Version Control  | 2.45.1 ✅           | 2.52.0       | —                            |
| GitHub Desktop           | Version Control  | 3.5.4                | 3.5.4        | —                            |
| Linux (Red Hat)          | Server OS        | 9.7                  | 10           | —                            |
| MS SQL ODBC Driver       | Database         | 17                   | 18.6.1.1     | —                            |
| MySQL Server Mgmt Studio | Database         | 18                   | 22           | —                            |
| NGINX                    | Musod            | 1.14.1-9             | 1.28.0       | —                            |
| NGINX                    | Phone API        | 1.20.1-22            | 1.28.0       | —                            |
| Gunicorn                 | Musod            | 20.04                | 25.0.1       | —                            |
| Gunicorn                 | Phone API        | 23.0.0               | 25.0.1       | —                            |
| Postman                  | API Tooling      | 11.82.1 ✅          | 11.82.1      | —                            |
| PuTTY                    | SSH Client       | 0.83                 | 0.83         | —                            |
| Python                   | Musod            | 3.6 – 3.7.9          | 3.15         | Version divergence           |
| Python                   | ETL              | 3.7.9                | 3.15         | —                            |
| Python                   | Phone API        | 3.9.13               | 3.15         | —                            |
| Python                   | Dental-External  | ?                    | 3.15         | Baseline unknown             |
| PHP Server               | Web Runtime      | ?                    | 8.5          | Baseline unknown             |
| FoxPro                   | Legacy App       | ?                    | 9.0 (SP2)    | Legacy                       |
| Windows 11 Education     | Desktop OS       | 24H2 ✅             | 24H2         | —                            |
| axiUm (Exan)             | Application      | 2024                 | 2025         | —                            |
| Intellepeer              | External Service | ?                    | ?            | Pending                      |
| D2L                      | LMS              | ?                    | ?            | Pending                      |
| Microsoft Teams          | Collaboration    | ?                    | ?            | Pending                      |
| Microsoft 365            | Productivity     | ?                    | ?            | Pending                      |
| Remexis                  | Application      | ?                    | ?            | Pending                      |


## Compatibility Notes

- Crystal Reports (2013) is not compatible with axilum
- PHP Server version pending confirmation
- Remexis version requires validation

## Maintenance Notes

- This table is reviewed opportunistically during system changes
- Values reflect deployed reality, not target state
- Ownership is shared between IT Operations and System Owners

## Later Refinements/Key
- ⚠️ for known incompatibility
- 🕒 for “planned upgrade”
- a “Last Verified” date footer