# Session 3 - OSCE Dashbord & Data Handling

Date: March 10, 2026
Presenter: Tom Wirtz

---

## 🎥 Watch Recording

[▶️ Launch Browser](../../assets/knowledge_transfer/videos/Data%20Extraction-20260310_095814-Meeting%20Recording.mp4)

---

## 📝 Transcript

- [▶️ View PDF version](../../assets/knowledge_transfer/transcripts/Data%20Extraction-20260303_095725-Meeting%20Recording.pdf)
- [▶️ View/Download Word version](../../assets/knowledge_transfer/transcripts/Data%20Extraction-20260303_095725-Meeting%20Recording.docx)

---

## 🧠 AI Summary


Here is a concise, high-signal summary of this recording session:

---

### **Session Summary — OSCE Dashboard & Data Handling**

This meeting focused on how **OSCE assessments** (simulated competency exams) are currently **structured, tracked, and inconsistently integrated into the dashboard system**.

**Core Purpose of OSCE:**

* Used to assess student competency in non-clinical (simulated) scenarios.
* Originally introduced to address gaps identified during accreditation reviews. 

---

### **Key Issues Identified**

**1. Lack of Reliable Data Pipeline**

* Initial approach pulled data from **D2L quizzes**, but:

  * Grading inconsistencies (manual grading, delays).
  * Students disputing scores.
* Result: the automated pipeline was **abandoned after limited use**. 

**2. Dashboard Is Not a System of Record**

* The dashboard displays data but is **not a reliable long-term audit source**.
* Accreditation requires **historically accurate, traceable records**, which are currently fragmented. 

**3. Inconsistent Faculty Processes**

* Faculty sometimes:

  * Delay reporting results.
  * Request bulk “mark everyone complete” actions.
* This creates **data integrity risks**, especially for accreditation validation. 

**4. Mixing Clinical and Non-Clinical Measures**

* OSCE (simulated) assessments are sometimes used to **compensate for missing clinical experiences**, but:

  * These are fundamentally different measures.
  * The system does not clearly distinguish or reconcile them. 

---

### **Current / Proposed Approaches**

**Option A — D2L-Based (Original)**

* Pull quiz scores and infer pass/fail.
* ❌ Not reliable due to grading and timing issues.

**Option B — Manual Entry via BSC Master (Preferred Direction)**

* Staff enter:

  * Student ID
  * Assessment type (OSCE)
  * Date
  * Pass/fail
* Data flows into ETL and persists long-term.
* ✅ Provides **audit-ready historical record**. 

---

### **Architectural Insight (Your Domain)**

There is a clear underlying tension:

> The system lacks a **single authoritative source of truth for assessment events**.

What exists today:

* D2L → transient, inconsistent
* Dashboard → presentation layer only
* Spreadsheets / ad hoc entry → fragmented persistence

What is needed:

* A **normalized, durable assessment record system**
* Clear ownership (likely via Dr. Talley / assessment leadership)
* Explicit modeling of:

  * Clinical vs simulated (OSCE)
  * Primary vs compensatory assessments

---

### **Closing Position of the Session**

* No final solution implemented yet.
* Agreement that:

  * The problem is **not just technical**, but **process + ownership driven**.
  * A cleaner, controlled data-entry + persistence model is likely required.
* You (Cash) will review and follow up with questions after rewatching.

---

### **One-Line Takeaway**

> The session exposed that OSCE tracking is currently **process-fragile, technically inconsistent, and not accreditation-safe**, and needs a **formalized system-of-record architecture** to stabilize it.


---