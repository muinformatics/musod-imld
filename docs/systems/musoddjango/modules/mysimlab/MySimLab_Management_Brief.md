# MySimLab Module: Management Brief

## Executive Summary

The MySimLab module is MUSOD's digital practical-assessment platform for simulation and selected imaging workflows. It supports structured rubric-based grading across multiple delivery modes, including bench assessments, Cabinet V2 anonymous grading, and Endodontics X-ray workflows.

At a management level, the module delivers value in three areas:

- Instructional quality: standardized rubrics, repeatable grading processes, and documented feedback.
- Operational control: role-based access, configurable assessment windows, and class-level administration.
- Data visibility: grade exports, student-facing grade views, and totals reporting for course/year-term oversight.

MySimLab operates as both a faculty grading tool and a student academic record touchpoint.

## Business Scope and Users

### Primary User Groups

- Students: view available assessments, present QR codes, upload/select X-ray files, and review published grades.
- Graders (faculty): grade students via QR/manual lookup, provide rubric-based scores, and submit feedback.
- My_Sim_Lab_Admin users: create/manage courses, classes, assessments, questions, rubrics, file types, and assessment status.
- Dental_informatics users: run administrative visibility views for class staffing and assessment totals.

### Assessment Types Supported

- Bench (B): student-visible context with assessment-linked QR workflows.
- Cabinet V2 (C2): anonymous/blind grading workflow driven by scan + assessment context.
- Endodontics X-Ray (EX): file-type-driven imaging workflows with grading integration.
- Legacy Cabinet (C): still represented for backward compatibility but functionally deprecated in creation flows.

## Functional Workflow Overview

### 1) Configuration and Setup

Admins configure the academic structure:

- Course creation
- Student class creation (year, term, student year)
- Assignment of admins and graders to classes
- Optional additional students by class

Then they configure assessment definitions:

- Assessment metadata (name, type, date, visibility)
- Questions and rubric criteria
- Required comments flags on rubric options
- Grading mode controls:
- default rubric preselection
- partial grading enablement

For EX assessments, admins additionally define required file types.

### 2) Assessment Availability and Access Control

Assessment status supports controlled release modes:

- Open for all (OA)
- Open for selected students (OS)
- Closed (CL)

Open-selected mode uses explicit student-level assignment records, enabling targeted assessment access while keeping non-selected students excluded.

### 3) Grading Operations

Grading intake supports multiple entry paths:

- QR scanning (legacy assessment|student payload)
- Cabinet V2 scan payloads using producer code with assessment context
- Manual student lookup by last 4 digits (with duplicate resolution)

Grading submission logic includes:

- Required-rubric validation when partial grading is disabled
- Required-comment validation tied to rubric settings
- Creation of auditable Grade records per question/rubric selection
- Feedback attribution and preservation of previous context
- Re-render with preserved input on validation errors (reduced rework for graders)

### 4) Student Experience

Students receive role-filtered views for:

- available assessments
- QR code generation for bench workflows
- X-ray file management and image manipulation (rotate/flip)
- grades review (legacy and V2 course/year-term navigation)

Grade visibility is governed by assessment settings and access policies.

## Governance, Security, and Controls

### Role and Group Enforcement

The module enforces access through user role relationships and group membership:

- My_Sim_Lab_Admin group and class-admin mappings for configuration privileges
- grader_student_classes mappings for grading privileges
- student profile validation for student-facing functions
- Dental_informatics group for selected administrative reporting views

### Process Controls

- Duplicate student-ID handling in manual lookup to prevent mis-grading.
- Student-in-class integrity checks before grading proceeds.
- Status-based assessment opening/closing and selective assignment.
- Controlled edit/delete/duplicate lifecycle for assessment artifacts.

### Audit and Record Integrity

- Each grading action creates timestamped grade records linked to grader, student, and rubric.
- Latest-grade retrieval patterns support reporting while preserving submission history.
- Feedback fields maintain attributed comments for instructional traceability.

## Reporting and Management Visibility

### Faculty/Admin Views

- Assessment detail view with question/rubric ordering controls.
- Posted grades and detailed grade exports per assessment.
- Student-class totals CSV export (normalized assessment naming for rollup).
- X-ray assessment totals interface with stepped course/year-term selection.

### Student Views

- Course/term-oriented grades browsing (V2) for simpler navigation.
- Detailed assessment/question-level history in course context.

### Operational Benefit

These outputs support both instructional decisions (feedback, remediation, calibration) and administrative monitoring (performance trend snapshots, class-level completion visibility, and grading throughput support).

## Notable Technical and Operational Dependencies

- Student identity and class enrollment depend on StudentProfile and class mappings.
- X-ray ingestion depends on FTP transfer and local media storage flows.
- QR workflows depend on payload format compatibility (legacy and C2 conventions).

These dependencies are managed in code with fallback and validation paths, but remain key operating assumptions.

## Risks and Management Watchpoints

- Legacy/parallel grading endpoints exist (original and extended flows), which can increase maintenance complexity.
- Cabinet legacy type remains present for historical compatibility; governance should continue migration discipline toward C2.
- FTP-based image movement introduces external dependency risk and operational sensitivity.
- Large multifunction views increase regression risk when modifying grading logic.

## Recommended KPIs

- Assessment throughput: number graded per course/term/week.
- Grading latency: time from assessment date to grade submission completion.
- Validation friction rate: frequency of required-comment/required-rubric failures.
- Regrade frequency: count of repeated grading actions per student-question.
- Student access utilization: percentage of eligible assessments opened by students.
- Reporting adoption: frequency of CSV exports and totals-view usage by admins.

## Conclusion

MySimLab is a comprehensive assessment operations platform that combines course administration, faculty grading, student participation, and reporting in one module. It is especially strong in rubric governance, role-based control, and multi-mode grading support (bench, anonymous cabinet, and X-ray). Continued simplification of endpoint variants and sustained focus on dependency resilience will further improve maintainability and operational reliability.