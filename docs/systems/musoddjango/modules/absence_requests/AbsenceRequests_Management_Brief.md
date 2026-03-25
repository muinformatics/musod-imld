# AbsenceRequests Module: Management Brief

## Executive Summary

The AbsenceRequests module is MUSOD's workflow engine for student absence governance. It standardizes how absence requests are created, validated, reviewed, approved/denied, archived, and reported. The module supports two primary operating modes:

1. Student self-service submission with guided workflow and policy checks.
2. Staff oversight with direct review, approvals management, and administrative controls.

From a management perspective, the module delivers three core outcomes:

- Compliance and consistency: Rule-driven submissions, required acknowledgments, and explicit status transitions reduce policy drift.
- Operational visibility: Role-based home views, filtering, approvals lists, and date-specific reporting support day-to-day supervision.
- Auditability: Time-stamped actions, status history states, admin comments, and acknowledgment records preserve decision traceability.

This module is already structured as a mature process control system rather than a simple form intake feature.

## Business Scope and Users

### Primary Users

- Students (request owners): create draft requests, select dates/time periods, review schedule conflicts, submit, withdraw pending requests, and reverse approved requests with rationale.
- Staff/Administrators: review and process pending requests, add decision comments, override/verify acknowledgments when appropriate, archive completed items, run approvals views/reports, and maintain policy configuration data.

### Module Boundaries

- In-scope:
- Absence reasons and approval rules.
- Religious holiday catalog management.
- Weekly review cadence configuration.
- Academic year date management for annual-day limit checks.
- End-to-end request lifecycle management.
- Axium conflict visibility integration.
- Approvals-focused reporting and archival utilities.

- Out-of-scope:
- Deep clinical scheduling resolution (the module checks/confirms conflicts, but does not resolve schedules itself).
- External communications strategy beyond configured email/permission integration in surrounding systems.

## End-to-End Workflow

### 1) Request Creation (Draft)

Students begin in a draft state by entering:

- Reason
- Optional religious holiday (required only when reason is Religious Holiday)
- Number of requested dates
- Optional student comment

The system captures the student level (D1-D4) from profile data for downstream filtering/reporting.

### 2) Date and Time Selection

Students provide exact absence dates and time periods (AM, PM, AM-PM). The module enforces:

- Fixed count of date rows based on requested days
- Duplicate-date prevention
- Deactivation of old draft date rows and replacement with current entries

### 3) Conflict Review

Before submission, the module performs Axium-based checks for:

- Rotation conflicts
- Patient appointment conflicts

This does not auto-block submission in every case, but it creates explicit user awareness and acknowledgment pathways.

### 4) Submission Decision Logic

On submission, the module validates that:

- At least one active absence date exists
- Required acknowledgments are present

Then policy logic determines final status:

- Pending (P): default for manual-review scenarios
- Approved (A): auto-approved or admin-approved
- Denied (D): policy denial (for example, annual max-day violation)

Additional status states include:

- Withdrawn (W): student withdraws pending request
- Reversed (R): student reverses approved request with mandatory reason

## Governance and Control Framework

### Policy Configuration Objects

The module uses configurable master data to keep policy adaptable:

- Absence reasons: active/inactive, auto-approval eligibility, same-day-only option, max-allowed-days option.
- Academic year windows: required for annual max-day checks.
- Weekly review day: controls review cadence logic for non-auto-approval reasons.
- Religious holidays: managed list used for reason-specific validation.

This design allows policy updates without code changes for most common operational adjustments.

### Auto-Approval Controls

Auto-approval is not unconditional. Even for eligible reasons, optional guardrails are enforced:

- Same-day-only constraint (if enabled)
- Maximum annual day limits, including half-day accounting (AM/PM counted as 0.5)
- If academic-year configuration is missing/ambiguous, requests fall back to pending review rather than silent failure

### Acknowledgment Controls

Acknowledgments are tracked as discrete records by category:

- Rotation conflicts
- Patient appointments
- Academic conflicts

Each record includes who acknowledged, timestamp, and action type:

- Student acknowledgment
- Admin override/verification

This creates a durable audit trail and supports mixed student/admin completion patterns.

### Role-Based Access and Actions

The module enforces strong separation of student and staff activities:

- Students can create/edit drafts, submit, withdraw pending, reverse approved.
- Staff can approve/deny pending requests, add comments, archive completed requests, and run approvals/reporting workflows.
- Student self-archiving is intentionally disabled; archive authority is centralized to staff.

## Operational Visibility and Reporting

### Home Views

- Student home: personal request list with reason/status/archive filters.
- Admin home: operational queue with filters for student name, pending-only, archive state, and schedule-conflict indicators.

The admin queue intentionally excludes withdrawn records and can prioritize pending review workload.

### Approvals Workspace

A dedicated approvals view supports:

- Approved-only request management
- Student/date/archive filtering
- Quick comment maintenance
- Page-scoped conflict indicators to reduce performance overhead

### Date-Specific Approved Report

The module can generate approved-request reports for a selected date, grouped by student level and sorted by last name. This is operationally useful for daily staffing coordination.

## Data Model and Audit Considerations

Core entities:

- AbsenceRequests: parent request, status, comments, dates, archival, auto-approval flag, approval timestamps.
- AbsenceRequestsDates: one-to-many date/time rows.
- AbsenceRequestAcknowledgment: many events per request and type, enabling longitudinal traceability.
- Policy/config entities: reasons, academic years, religious holidays, weekly review day, guide pages.

Audit strengths:

- Timestamped submission and finalization fields
- Explicit admin comment logging for approve/deny paths
- Structured acknowledgment events with actor attribution
- Retention via archive toggles instead of immediate deletion for most completed records

## Risks and Management Watchpoints

### Current Strengths

- Clear status model and transitions
- Strong configurability of policy controls
- Meaningful data capture for audits and downstream reporting
- Integrated conflict visibility from scheduling systems

### Watchpoints

- Any logged-in user access to general request view should continue to be monitored for least-privilege alignment.
- Reliance on correct academic-year configuration can affect max-day auto-approval outcomes.
- Staff designation via is_staff is broad; group-based governance may be preferable for fine-grained controls in future phases.

## Recommended KPIs

Management can measure module performance with:

- Submission volume by week/month and student level
- Pending queue aging (median and 95th percentile time-to-decision)
- Auto-approval rate vs manual-review rate
- Denial rate by reason category
- Withdrawal and reversal rates
- Archived backlog trend and cleanup cycle adherence
- Frequency of admin overrides/verification in acknowledgment workflow

## Conclusion

The AbsenceRequests module is operationally robust and governance-oriented. It combines student usability with policy enforcement, staff decision controls, and strong traceability. The current implementation supports both daily workload management and policy compliance objectives. With continued attention to role granularity and reporting maturity, it can serve as a durable institutional system of record for absence management.