# Git & GitHub Cheat Sheet for MUSOD Informatics

**Purpose:**  
A quick guide for the standard workflow: creating a feature branch, developing, and submitting a Pull Request for review.

> **A Note on Branch Naming:**  
> Historically, the primary branch in Git repositories was often named `master`.  
> The community has transitioned to using **`main`** as the default branch name.  
> Some older repositories may still reference `master`, but new work should use **main**.

---

# 1. Start a New Feature/Bugfix (Branch Creation & Checkout)

Always start your work on a new branch based on the latest **main** branch.

### Switch to main (if not already there)

```bash
git checkout main
```

### Get the latest changes from GitHub

```bash
git pull origin main
```

### Create and switch to your new dev branch

```bash
git checkout -b your-feature-name
```

**Naming Convention**

Use a clear branch name such as:

```
user-login
bugfix/admin-dashboard
feature/report-export
```

`-b` means **create the branch and switch to it immediately**.

*(You are now on your new feature branch and ready to code.)*

---

# 2. Develop & Commit Your Changes

Work on your feature and **commit changes frequently and logically**.

### Make code changes

Edit your code using your IDE (PyCharm, VS Code, etc.).

---

### Stage your changes

Stage **all modified files**

```bash
git add .
```

Stage **specific files**

```bash
git add filename.py
```

---

### Commit your changes

```bash
git commit -m "Describe the change you made"
```

Example:

```bash
git commit -m "Add validation for login form"
```

---

# 3. Push Your Branch to GitHub

Push your new branch to the remote repository.

```bash
git push -u origin your-feature-name
```

The `-u` flag links your local branch to the remote branch so future pushes can be done with:

```bash
git push
```

---

# 4. Create a Pull Request (PR)

1. Go to the repository on **GitHub**
2. You will usually see a prompt to **Create Pull Request**
3. Click **Compare & Pull Request**

Provide:

- A clear **title**
- A brief **description of the change**
- Any **testing notes**

Then submit the PR for review.

---

# 5. Update Your Branch (If main Changes)

If other developers push updates to `main`, update your branch.

### Switch to main

```bash
git checkout main
```

### Pull latest changes

```bash
git pull origin main
```

### Return to your branch

```bash
git checkout your-feature-name
```

### Merge updates from main

```bash
git merge main
```

Resolve any conflicts if they appear, then commit the merge.

---

# 6. After Your PR is Merged

Once your Pull Request is merged:

### Switch to main

```bash
git checkout main
```

### Pull latest updates

```bash
git pull origin main
```

### Delete your local branch

```bash
git branch -d your-feature-name
```

### Delete the remote branch

```bash
git push origin --delete your-feature-name
```

---

# Summary Workflow

Typical development cycle:

```
git checkout main
git pull origin main
git checkout -b feature-name

# work and commit
git add .
git commit -m "message"

git push -u origin feature-name
```

Then create a **Pull Request** on GitHub.
