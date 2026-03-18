# SOP — Software Repository Policy

## Purpose

This document defines the standard policy and procedures for managing MUSoD software source code repositories.

The goal is to ensure that all MUSoD software systems are maintained in a consistent, secure, and maintainable manner that supports long-term development and operational continuity.

---

## Scope

This policy applies to all software developed or maintained for MUSoD systems, including:

* internally developed applications
* APIs and services
* ETL processes and data pipelines
* utilities and support tools
* supporting documentation repositories

All MUSoD development work must follow this repository policy unless explicitly approved otherwise.

---

## Policy

The following requirements apply to MUSoD software repositories.

### Repository Location

All MUSoD software source code must reside within the official MUSoD GitHub organization:

```
https://github.com/muinformatics
```

All repositories within this organization are maintained as **private repositories** unless explicitly approved otherwise.

No production software source code may be maintained outside the official MUSoD GitHub organization.

---

### Repository Ownership

All repositories are owned by the organizational account:

```
muinformatics@marquette.edu
```

This ensures continuity of ownership and access regardless of individual personnel changes.

---

### Repository Creation Authority

Only the **[muinformatics@marquette.edu](mailto:muinformatics@marquette.edu) organizational owner** is authorized to create new repositories within the MUSoD GitHub organization.

Developers requiring a new repository should submit a request to the repository owner.

---

### Repository Access Control

Repository access is restricted to **approved collaborators**.

Access is granted by repository administrators or project leads as appropriate for the project.

Access should follow the principle of **least privilege**, granting only the permissions necessary to perform development tasks.

---

### Repository Naming Conventions

New repositories should follow **standard Python project naming conventions** using lowercase characters and hyphen-separated words.

Recommended format:

```
<system>-<purpose>
```

Examples:

```
student-clinic-reporting
absence-request-app
clinical-report-api
etl-xray-import
```

Existing repositories may retain their current names. Renaming existing repositories is not required.

---

### Default Branch

The default branch for all new repositories must be:

```
main
```

Some legacy repositories may still use `master`. These may remain unchanged unless actively migrated.

---

### Repository Description

Each repository must include a **GitHub repository description** that clearly explains the purpose of the project.

Example descriptions:

* Django application for student clinical reporting
* ETL process for X-ray image ingestion
* API service for clinical data lookup

This helps developers quickly understand repository contents when browsing the organization.

---

### Required Repository Files

Each repository must include the following minimum files and directories.

**README.md**

The primary project description, including:

* project overview
* installation instructions
* usage information
* deployment notes if applicable

**docs/**

Published technical documentation intended for developers or maintainers.

**documentation/**

Supplemental materials including:

* architecture notes
* technical decisions
* historical implementation notes
* supporting reference materials

---

### Repository Structure

Repository structure should follow the conventions of the **primary technology framework used by the application**.

Examples include:

* Django project structure for Django applications
* Standard Python project structure for Python utilities
* Framework-specific layouts for other technologies

Additional directories such as `src`, `tests`, or `scripts` may be included where appropriate.

---

## Procedure

### Creating a New Repository

1. Submit a repository request to the repository owner.
2. The repository will be created within the MUSoD GitHub organization.
3. The repository owner assigns initial collaborators.
4. The repository should be initialized with:

   * README.md
   * initial project structure
   * dependency definitions if applicable.

---

### Adding Collaborators

1. Request collaborator access from the repository administrator.
2. Access will be granted based on project involvement.
3. Collaborators should follow MUSoD development practices when modifying repository contents.

---

## Responsibilities

**Developers**

Developers are responsible for ensuring that development work is maintained within the official MUSoD repositories and that repository documentation remains accurate and up to date.

**Repository Administrators**

Repository administrators are responsible for managing repository creation, collaborator access, and ensuring adherence to repository policies.

---

## Review Cycle

This policy should be reviewed periodically to ensure it remains aligned with MUSoD development practices and technology environments.

Recommended review frequency: **annually or as systems evolve**.

---

## Related Documentation

* MUSoD Development Hub (Arms Around)
* MUSoD SDLC Policies
* Application-specific technical documentation

---
