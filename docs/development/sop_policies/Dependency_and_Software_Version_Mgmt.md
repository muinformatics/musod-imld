# SOP — Dependency and Software Version Management

## Purpose

This document defines the policy and procedures for managing software dependencies and third-party libraries used in MUSoD software systems.

The goal is to ensure that external dependencies remain secure, supported, and compatible with MUSoD applications while minimizing operational risk.

---

## Scope

This policy applies to all MUSoD software systems that utilize external libraries, packages, frameworks, or runtime dependencies, including:

* Python libraries and packages
* Django framework components
* third-party APIs and SDKs
* system runtime environments
* database drivers and integration libraries

All MUSoD development projects must manage dependencies according to this procedure.

---

## Policy

The following requirements apply to dependency management within MUSoD systems.

### Dependency Definition

All software dependencies must be explicitly defined within the repository.

For Python-based projects, this typically includes files such as:

```
requirements.txt
environment.yml
pyproject.toml
```

Dependency definitions must be maintained within the repository to ensure reproducible environments.

---

### Dependency Review Frequency

All software dependencies must be reviewed periodically to identify:

* outdated libraries
* security vulnerabilities
* deprecated packages
* compatibility concerns

The recommended review frequency is:

```
Quarterly
```

Reviews may also be performed when:

* upgrading a system runtime environment
* introducing new functionality
* resolving security alerts
* addressing dependency conflicts

---

### Security and Vulnerability Monitoring

Developers should periodically review dependency security status using available tools, which may include:

* GitHub security alerts
* `pip-audit`
* `pip list --outdated`
* other dependency scanning tools

Any dependency with a known security vulnerability should be evaluated and updated where feasible.

---

### Introducing New Dependencies

Before introducing a new third-party library into a MUSoD project, the following considerations should be reviewed:

* project maintenance activity
* license compatibility
* security posture
* compatibility with existing system architecture
* stability and maturity of the library

Where appropriate, significant dependency additions should be discussed with the project supervisor or technical lead.

---

### Dependency Version Control

Projects should avoid unbounded dependency specifications.

Where possible, dependency versions should be pinned or constrained to ensure predictable builds and deployments.

Example:

```
numpy==1.26.2
matplotlib>=3.7,<3.9
```

This helps prevent unexpected behavior caused by automatic dependency upgrades.

---

## Procedure

### Dependency Review Process

1. Identify dependency definition files within the repository.
2. Review installed packages for outdated versions.
3. Review security advisories or vulnerability alerts.
4. Determine whether updates are required.
5. Update dependency definitions if necessary.
6. Test application functionality after dependency updates.

---

### Adding a New Dependency

1. Evaluate the proposed library for suitability and maintenance status.
2. Confirm compatibility with the project architecture.
3. Add the dependency to the project dependency definition file.
4. Update project documentation if necessary.
5. Test application functionality after integration.

---

### Updating Dependencies

1. Identify outdated dependencies.
2. Review release notes for breaking changes.
3. Update dependency definitions.
4. Rebuild the application environment.
5. Test application functionality to confirm compatibility.

---

## Responsibilities

**Developers**

Developers are responsible for maintaining dependency definitions, reviewing dependency updates, and ensuring that new dependencies are appropriate for the project.

**Project Leads / Supervisors**

Project leads may review and approve significant dependency additions when necessary.

---

## Documentation Requirements

Repositories should maintain documentation related to dependency usage when relevant, including:

* dependency configuration files
* environment setup instructions
* notes regarding major dependency changes

---

## Review Cycle

This procedure should be reviewed periodically to ensure alignment with MUSoD development practices and evolving technology environments.

Recommended review frequency: **annually or as systems evolve**.

---

## Related Documentation

* MUSoD Software Repository Policy
* MUSoD Development Hub (Arms Around)
* Project-specific technical documentation

---
