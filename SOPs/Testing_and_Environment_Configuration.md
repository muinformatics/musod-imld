# SOP — Testing and Environment Configuration

## Purpose

This document defines the procedures for testing software changes and managing development, sandbox, and production environment configurations for MUSoD software systems.

The goal is to ensure that system changes are verified prior to production deployment and that application environments remain reproducible and consistent across development, sandbox, and production systems.

---

## Scope

This procedure applies to all MUSoD software systems maintained within the MUSoD GitHub organization, including:

* Django web applications
* APIs and backend services
* ETL processes and scheduled data workflows
* reporting and analytics tools
* supporting utilities and scripts

All software changes must be tested prior to deployment into production environments.

---

## Policy

All MUSoD software changes must be validated in a **development or sandbox environment** prior to deployment into production.

Testing procedures currently rely primarily on **manual execution and verification of system functionality**. Developers must confirm that application behavior remains correct after modifications.

Testing environments should be configured as similarly to production environments as practical in order to reduce unexpected behavior during deployment.

---

## Django Migration Management

For Django-based applications, all database schema changes must be implemented using **Django migration files**.

The following rules apply:

* Migration files must be generated using Django migration commands.
* Migration files must be **committed to the repository**.
* Direct modification of database schema outside the migration system is not permitted.
* Migration files must be executed and verified in development or sandbox environments prior to production deployment.

This ensures that database structure changes remain version-controlled and reproducible across environments.

---

## Environment Configuration

Application configuration must be **reproducible from repository-managed files**.

Environment-specific settings must not rely on undocumented manual changes between environments.

Configuration differences between environments should be handled using one of the following approaches:

* environment variables
* environment-specific configuration files
* structured settings modules

Example approaches may include:

```
settings/
   base.py
   local.py
   production.py
```

or the use of environment variables loaded from environment configuration files.

Sensitive values such as passwords, tokens, and keys must **not be stored directly in the repository**.

---

## Procedure

### Step 1 — Prepare Testing Environment

Before testing begins, confirm that the development or sandbox environment is properly configured.

This may include:

* installing required dependencies
* configuring environment variables
* verifying database connectivity
* applying database migrations
* preparing test datasets where applicable

---

### Step 2 — Execute Functional Testing

Developers must manually execute application workflows relevant to the modification.

Testing should verify:

* the new or modified functionality behaves as expected
* existing functionality continues to operate correctly
* no unexpected errors appear in application logs

Examples may include:

* running application features through the web interface
* validating generated reports
* executing API requests
* running ETL processes

---

### Step 3 — Verify Database Integrity

When database-related changes are introduced, developers must confirm:

* migrations apply successfully
* existing data remains valid
* queries execute correctly
* reports and downstream systems function properly

---

### Step 4 — Review Application Logs

Application logs should be reviewed to confirm that no new errors or warnings were introduced by the change.

This includes:

* application logs
* ETL execution logs
* API service logs where applicable

---

### Step 5 — Confirm Environment Consistency

Developers should verify that configuration changes required by the modification are properly documented and reproducible across environments.

No environment should rely on undocumented manual configuration changes.

---

## Responsibilities

**Developers**

Developers are responsible for ensuring that software changes are tested in development or sandbox environments prior to production deployment and that configuration changes remain reproducible.

**Project Leads / Supervisors**

Project leads may review testing procedures for significant system changes or database modifications.

---

## Documentation Requirements

Repositories should maintain documentation describing:

* environment setup procedures
* database initialization instructions
* required environment variables
* testing procedures for complex systems

This documentation should enable future developers to reproduce development environments and testing procedures.

---

## Review Cycle

This procedure should be reviewed periodically to ensure alignment with MUSoD development practices and system architecture.

Recommended review frequency: **annually or as systems evolve**.

---

## Related Documentation

* Software Repository Policy
* Dependency and Software Version Management
* Software Change Procedure
* MUSoD Development Hub (Arms Around)

---
