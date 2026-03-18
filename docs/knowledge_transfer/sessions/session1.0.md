# Session 1 - axiUm Integration - Part 1

Date: February 05, 2026
Presenter: Tom Wirtz

---

## 🎥 Watch Recording

[▶️ Launch Browser] 
(Unavailable ...)

---

## 📝 Transcript

- [▶️ View PDF version](../../assets/knowledge_transfer/transcripts/Data%20Extraction%20from%20axiUm-20260205_100244-Meeting%20Recording.pdf)
- [▶️ View/Download Word version](../../assets/knowledge_transfer/transcripts/Data%20Extraction%20from%20axiUm-20260205_100244-Meeting%20Recording.docx)

---

## 🧠 AI Summary

Here is a structured, high-signal summary for this recording:

---

### **Session Summary — axiUm Data Extraction & System Landscape**

This session provided a **deep foundational walkthrough of axiUm’s data ecosystem**, focusing on:

* Where data lives
* How to access it
* Why extraction is difficult
* Key structural inconsistencies in the system

---

### **Core Purpose of the Session**

To establish a **mental model of axiUm as a data system**, including:

* Database architecture (Oracle + staging SQL)
* Available tools (Info Manager, Crystal Reports, SQL)
* Documentation limitations
* Known data integrity issues

---

### **System Architecture Overview**

**Primary Data Sources:**

* **Production DB (Oracle)** → Live clinical system
* **Dev/Stage DB (Oracle)** → Near-copy for testing
* **Training DB (Oracle)** → Old, non-synced environment
* **Staging DB (SQL Server)** → Nightly extracted subset (~30 tables)

Key constraint:

> The staging DB is **not a full or guaranteed-accurate replica** due to selective extraction logic. 

---

### **Data Access Tooling**

**1. Info Manager (axiUm native)**

* Provides canned + custom reports
* High risk of inconsistency:

  * Different users → different results for same query
* Not reliable without deep schema understanding 

**2. Crystal Reports**

* Direct connection to Oracle DB
* Used for:

  * Custom reporting
  * Accessing full dataset beyond staging DB
* Version compatibility constraints (older versions required)

**3. SQL Access**

* SQL Server → staging DB (preferred for performance)
* Oracle (via SQL*Plus or tools) → full access
* Python/Django → programmatic extraction

**4. Internal Artifacts**

* Historical SQL queries and reports stored in shared directories
* Valuable for reuse and pattern discovery

---

### **Documentation Reality**

Available:

* Data dictionary (600+ tables)
* Entity relationship diagrams

Missing:

* Workflow/process documentation
* Table interaction logic (how actions affect data)

➡️ Result:

> Data extraction requires **reverse engineering + experimentation**, not just reading docs. 

---

### **Critical Data Constraints**

**1. Staging DB Limitations**

* ~30 tables only
* Nightly refresh (1-day lag)
* Selective update logic (not full sync)
* Potential data gaps depending on extraction rules 

**2. Performance Consideration**

* Direct queries on production DB are avoided
* Staging DB exists to **protect clinical system performance**

---

### **Patient Data Model (Key Domain Example)**

**Core Identifier Complexity:**

* “Patient ID” (primary key)
* “Patient 2 ID” (used in some tables like notes)

➡️ Requires translation between tables → adds complexity. 

---

### **Major Data Integrity Issues**

**1. Inconsistent Field Usage**

* Example: “Last Visit” does not reliably mean last appointment
* Field semantics are **unclear or loosely defined**

**2. Multi-Location Data Storage**

* Example: race/ethnicity stored in **multiple tables/fields**
* Often incomplete (~60% missing)

**3. Chart Number Mutation**

* Chart numbers modified for:

  * Pediatric (prefix “P”)
  * Ortho
  * Research flags
* Breaks traceability and lookup consistency

**4. Status Field Corruption**

* Intended: Active / Inactive / Recall
* Actual: Dozens of variations (e.g., “Active-Endo”, etc.)
* Inconsistent usage across clinics
* Leads to **invalid reporting results**

➡️ Conclusion:

> Many fields are **not reliable without contextual interpretation**. 

---

### **Conceptual Pitfall — Counting Patients**

Critical distinction:

* **Total visits** (same patient counted multiple times)
* **Unique patients** (deduplicated)

➡️ Must always clarify requirement before querying. 

---

### **Architectural Insight (Your Domain)**

This session exposes the deepest layer of the system:

> axiUm is a **data-rich but structurally opaque system with weak semantic integrity**.

What exists:

* Massive relational dataset
* Partial tooling
* Fragmented documentation

What is missing:

* Canonical data definitions
* Consistent data governance
* Reliable transformation layer

---

### **Closing Position of the Session**

* This was **foundational orientation**, not execution
* Next steps involve:

  * Hands-on querying
  * Comparing results across approaches
* Emphasis on:

  * Learning through **trial + validation**
  * Recognizing system inconsistencies early

---

### **One-Line Takeaway**

> axiUm is not just a database—it is a **legacy data ecosystem requiring interpretation, validation, and disciplined extraction practices to produce trustworthy results**.

---

