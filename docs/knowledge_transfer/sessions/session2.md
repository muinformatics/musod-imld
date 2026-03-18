# Session 2 - Endodontic Competency (Tablet Grading Workflow)

Date: March 03, 2026
Presenter: Tom Wirtz

---

## 🎥 Watch Recording

[▶️ Launch Browser](../../assets/knowledge_transfer/videos/Data%20Extraction-20260303_095725-Meeting%20Recording.mp4)

---

## 📝 Transcript

- [▶️ View PDF version](../../assets/knowledge_transfer/transcripts/Data%20Extraction-20260303_095725-Meeting%20Recording.pdf)
- [▶️ View/Download Word version](../../assets/knowledge_transfer/transcripts/Data%20Extraction-20260303_095725-Meeting%20Recording.docx)

---

## 🧠 AI Summary

Here is a concise, high-signal summary of this recording:

---

### **Session Summary — Endodontic Competency (Tablet Grading Workflow)**

This session focused on the **endo competency exam process**, specifically how it is **executed, graded, and supported technically (X-ray + tablet grading system)**.

---

### **Core Purpose of the Session**

To walk through:

* How the **endo competency exams are structured**
* How grading is performed via the **tablet/X-ray system**
* What **technical and operational checks** are required before execution

---

### **Assessment Structure**

**Nature of the Competency:**

* Students perform a **simulated procedure on a tooth (mannequin-based)**.
* Work is completed within a **2–3 hour window**.
* Output includes:

  * Physical tooth (submitted anonymously)
  * Associated X-rays (digitally captured)

**Grading Model:**

* Grading is **post-execution**, not live.
* Typically performed by a **single evaluator (Dr. Ibram)**.
* Uses a **web-based grading interface tied to student IDs**. 

---

### **Key Workflow Elements**

**1. Anonymized Submission**

* Students submit work using **ID-based tracking (last 4 digits)**.
* Prevents grader bias.

**2. X-Ray Integration**

* Multiple X-rays captured per student.
* System supports **selection of relevant X-rays per grading category**.
* Exact requirements (e.g., 3 vs 5 X-rays) must be confirmed each year. 

**3. Tablet Grading System**

* Grader enters student ID → pulls up grading interface.
* Scores entered across defined categories.
* Backed by a **URL-driven system tied to exam instance IDs**. 

---

### **Grading Model (Important Nuance)**

Although the syllabus defines multiple components:

* Pre-op radiograph
* Rubber dam
* Access opening
* Cleaning & shaping
* Obturation

**Actual practice (recent years):**

* Only **core procedural elements are graded**
* Some components are effectively **auto-scored (full credit)**

➡️ This creates a **disconnect between documented rubric and applied grading logic**. 

---

### **Key Risks & Constraints**

**1. ID Collision Risk**

* System depends on **last 4 digits of student IDs being unique**.
* Must be validated ahead of time (critical pre-check). 

**2. Process Variability**

* Execution details change year-to-year:

  * Whether steps are validated live vs post-process
  * Which X-rays are required
* Requires **direct confirmation with faculty each cycle**. 

**3. Operational Fragility**

* High-stress exam environment:

  * Any technical issue (X-ray system, login delays, etc.) → immediate student impact
* System must be **fully validated prior to exam day**. 

---

### **Architectural Insight (Your Domain)**

This system reveals a different—but related—pattern from the OSCI session:

> The workflow is **operationally functional but loosely coupled and highly person-dependent**.

What exists:

* Tablet grading system (functional but implicit)
* D2L (reference only, not integrated)
* Django-backed student data
* Manual coordination with faculty

What is missing:

* A **formalized, versioned assessment contract**

  * (rubric, X-ray requirements, grading rules)
* A **pre-flight validation pipeline**
* A **clear system boundary between configuration vs execution**

---

### **Closing Position of the Session**

* No major issues currently blocking execution.
* Emphasis is on:

  * **Preparation and validation**
  * **Confirming assumptions with faculty**
* You indicated:

  * This area is **under control**
  * Priority should shift toward **OSCI (higher complexity/problem space)**

---

### **One-Line Takeaway**

> The endo competency system works, but it is **procedurally brittle and dependent on implicit knowledge**, requiring disciplined pre-validation rather than architectural overhaul.

---
