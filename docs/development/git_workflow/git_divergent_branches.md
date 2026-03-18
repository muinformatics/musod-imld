# GitHub - Divergent Branches 

## Synchronizing Divergent Branches When `main/master` Cannot Receive Changes

**Document ID:** ENG-GIT-BR-001
**Version:** 1.0
**Owner:** Engineering
**Last Updated:** Mar 2, 2026

---

## 1. Purpose

This procedure defines the standard process for synchronizing a feature or development branch (e.g., `dev`) with hotfixes or updates from the protected production branch (`main` or `master`) when:

* The development branch has diverged
* The production branch cannot yet accept the development changes
* Conflict resolution must occur in the development branch

This procedure ensures:

* Production stability is preserved
* Development remains aligned with production fixes
* Conflicts are resolved in a controlled manner
* History integrity is maintained

---

## 2. Scope

This process applies when:

* `main` (or `master`) contains hotfixes or production changes
* `dev` contains new features or in-progress work
* `main` is locked or protected from receiving feature changes
* Synchronization must occur from `main` → `dev`

This procedure assumes use of Git and Visual Studio Code.

---

## 3. Definitions

* **Production Branch**: `main` or `master`
* **Development Branch**: `dev`
* **Divergence**: When both branches contain commits not present in the other
* **Protected Branch**: A branch that does not allow direct pushes without review

---

## 4. Guiding Principle

When branches diverge and production cannot receive development changes:

> Always merge production into development — never force development into production.

Conflict resolution occurs inside the development branch.

---

## 5. Preconditions

Before beginning:

* All local work must be committed or stashed
* The working directory must be clean
* The developer must have pull/push access to `dev`

> Tooling Policy: This procedure is Git-first and IDE-neutral. All required actions are expressed as Git CLI commands IDE-specific instructions (VS Code, PyCharm) are provided only as optional guidance. When UI and CLI appear to differ, the CLI is authoritative.

Verify:

```bash
git status
```

If necessary:

```bash
git add .
git commit -m "WIP before branch sync"
```

---

## 6. Standard Procedure (Merge-Based Synchronization)

### Step 1 — Fetch Latest Remote State

```bash
git fetch origin
```

This updates local knowledge of remote branches without modifying local branches.

---

### Step 2 — Switch to Development Branch

```bash
git checkout dev
```

---

### Step 3 — Ensure Local `dev` Is Current

```bash
git pull origin dev
```

---

### Step 4 — Merge Production Into Development

```bash
git merge origin/master
```

(Replace `master` with `main` if applicable.)

This action:

* Brings all hotfixes from production into development
* Preserves branch history
* Creates a merge commit if required

---

### Step 5 — Resolve Conflicts (If Present)

If Git reports conflicts:

1. Open your perferred IDE (See appendix for specific instructions)
2. Navigate to the Source Control panel
3. Open each conflicted file
4. Use the built-in conflict resolution tools:

   * Accept Current Change
   * Accept Incoming Change
   * Accept Both
   * Compare Changes
5. After resolving each file:

```bash
git add <filename>
```

When all conflicts are resolved:

```bash
git commit
```

---

### Step 6 — Validate Application Integrity

Before pushing:

* Run unit tests
* Build the application
* Manually verify critical workflows
* Confirm that hotfix behavior remains intact

Examples:

```bash
npm test
npm run build
pytest
```

Validation is mandatory.

---

### Step 7 — Push Updated Development Branch

```bash
git push origin dev
```

At this point:

* `dev` contains all production hotfixes
* Conflicts have been resolved
* `main/master` remains untouched

---

## 7. What This Procedure Explicitly Avoids

This procedure does NOT:

* Merge `dev` into `main`
* Rebase shared development history
* Force push to protected branches
* Alter production history

Rebasing shared branches is prohibited unless explicitly approved by the Engineering Lead.

---

## 8. When This Procedure Should NOT Be Used

Do not use this process if:

* `dev` is intended to be discarded
* Production is being rebuilt from development
* A release branch strategy is being used instead
* Emergency production restoration is underway

In those cases, escalate to Engineering Leadership.

---

## 9. Conflict Resolution Guidance

When resolving conflicts:

* Prefer production logic for hotfix correctness
* Carefully integrate new feature logic
* Avoid blindly accepting “both” changes
* Validate behavior after resolution
* Document complex conflict decisions in commit messages

---

## 10. Audit and Traceability

The merge commit created during this process serves as:

* Documentation of synchronization timing
* Traceability point for hotfix inclusion
* Audit marker for future debugging

Developers should not squash this merge commit.

---

## 11. Summary

When branches diverge and production cannot receive development changes:

1. Fetch
2. Checkout `dev`
3. Pull `dev`
4. Merge `origin/master`
5. Resolve conflicts
6. Validate
7. Push `dev`

Production remains protected.
Development absorbs production stability.
Conflicts are resolved in a controlled environment.

## Appendix A — VS Code UI Assist (Optional)

- Fetch: Source Control (…) → Fetch
- Checkout branch: bottom-left branch name → select `dev`
- Merge: Command Palette → “Git: Merge Branch…” → select `master/main`
- Resolve conflicts: Source Control → open conflicted files → use conflict actions → stage → commit → push

## Appendix B — PyCharm UI Assist (Optional)

- Fetch: VCS → Git → Fetch
- Checkout `dev`: Git Branches menu (bottom-right) → `dev`
- Pull `dev`: VCS → Update Project… (or Git → Pull)
- Merge: VCS → Git → Merge Changes… → select `master/main`
- Resolve conflicts: use PyCharm 3-way merge tool; after saving, ensure conflicts are marked resolved
- Push `dev`: VCS → Git → Push…

**Validation requirement (all IDEs):** After resolving conflicts, run `git status` and confirm there are no unmerged paths before committing.
