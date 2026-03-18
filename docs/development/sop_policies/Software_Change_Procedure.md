# SOP — Software Change Procedure

## Purpose

This document defines the standard procedure for introducing software additions and modifications within MUSoD systems.

The purpose of this procedure is to ensure that system changes are implemented in a consistent, controlled, and testable manner that minimizes operational risk and preserves system stability.

---

## Scope

This procedure applies to all MUSoD software systems maintained within the MUSoD GitHub organization, including:

* application feature additions
* bug fixes
* reporting updates
* API changes
* database modifications
* ETL process updates

All software changes must follow this procedure unless explicitly approved otherwise.

---

## Policy

All software modifications must follow a structured development and testing process before being deployed to production environments.

The level of process rigor may vary depending on the type of modification.

Examples:

**Low Impact Changes**

Changes that do not modify stored data or system behavior beyond reporting or display.

Examples include:

* report formatting updates
* user interface adjustments
* minor content updates

These changes may follow a simplified testing process.

**Standard Changes**

Changes that affect application behavior but do not alter database structure.

Examples include:

* feature additions
* bug fixes
* API logic changes
* workflow improvements

These changes must follow the standard development workflow.

**High Impact Changes**

Changes that modify database structure, core system behavior, or critical integrations.

Examples include:

* database schema changes
* data processing logic changes
* major system integrations
* security-sensitive functionality

These changes require full testing and additional review.

---

## Procedure

### Step 1 — Identify and Define the Change

The developer identifies the required change and determines the type of modification:

* low impact
* standard
* high impact

Relevant systems, data, and components affected by the change should be identified.

---

### Step 2 — Create Development Branch

A development branch should be created from the repository’s main branch.

Example branch names:

```
feature/<description>
bugfix/<description>
update/<description>
```

All development work should occur within the branch.

---

### Step 3 — Implement the Change

Developers implement the required code or configuration changes.

Where appropriate, developers should:

* maintain code clarity
* preserve architectural structure
* update configuration files
* maintain dependency definitions

---

### Step 4 — Perform Testing

Testing must be performed in a **development or testing environment** before changes are merged or deployed.

Testing should confirm:

* expected system behavior
* absence of unintended side effects
* compatibility with existing system functionality

For database changes, testing should include validation of:

* data integrity
* migration behavior
* application compatibility

---

### Step 5 — Update Documentation

Where applicable, documentation should be updated to reflect the modification.

Examples include:

* README updates
* documentation in the `docs` directory
* architecture or design notes
* configuration instructions

---

### Step 6 — Review and Merge

Once testing is complete, the development branch may be merged into the main branch.

When appropriate, changes may be reviewed by another developer or project lead prior to merging.

---

### Step 7 — Deploy or Release

After merging into the main branch, the change may be deployed to the appropriate environment according to the project’s deployment process.

Deployment should confirm:

* system stability
* successful execution of updated functionality
* absence of production errors

---

## Responsibilities

**Developers**

Developers are responsible for implementing software changes in accordance with this procedure and ensuring adequate testing prior to deployment.

**Project Leads / Supervisors**

Project leads may review significant system changes, particularly those involving database modifications or major system functionality.

---

## Documentation Requirements

Repositories should maintain documentation related to significant software changes, including:

* change descriptions
* configuration updates
* dependency updates
* architectural adjustments where applicable

---

## Review Cycle

This procedure should be reviewed periodically to ensure alignment with MUSoD development practices and evolving system architecture.

Recommended review frequency: **annually or as systems evolve**.

---

## Related Documentation

* Software Repository Policy
* Dependency and Software Version Management
* MUSoD Development Hub (Arms Around)

---
