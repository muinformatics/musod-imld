------------------------------------------------------------------------

# Git and GitHub Usage Guidelines for MUSOD Informatics

------------------------------------------------------------------------

## 1. Branching Strategy: Feature-Based Development

This strategy ensures stable code in main and isolated development for new features and fixes.

- **1.1 The main (formerly master) Branch (Production-Ready Code):** This branch always represents the stable, deployable version of the application.

- > \***A Note on Branch Naming:** Historically, the primary branch in Git repositories was often named \'master\'. In an effort to adopt more inclusive language, the community widely transitioned to using \'main\' as the default branch name. Our existing repositories might still refer to \'master\' in their history or older configurations, but for all new work and naming convention practices in this document, we will use **main**.

**Never commit directly to main.** All changes must come from merged Pull Requests.

- **1.2 Development Branches (dev/\[feature-name\] or feature/\[feature-name\]):**

  - **Purpose:** To isolate new features, bug fixes, or experimental work.

  - **Creation:** Always branch off the latest main branch.

    - git checkout main

    - git pull origin main

    - git checkout -b dev/my-new-feature

  - **Naming Conventions:** Use clear, descriptive names (e.g., dev/user-auth-module, bugfix/login-error, feature/payment-gateway).

  - **Scope:** Each branch should ideally address a single feature or bug.

  - **Regular Syncing:** Periodically pull changes from main into your dev branch to minimize merge conflicts later.

    - git checkout dev/my-new-feature

    - git pull origin main (resolve any conflicts locally)

- **1.3 Hotfix Branches (for urgent production issues):**

  - **Purpose:** To quickly address critical bugs in the main branch when immediate deployment is required.

  - **Creation:** Branch directly from main.

    - git checkout main

    - git pull origin main

    - git checkout -b hotfix/critical-bug-123

  - **Process:** After fixing, create a PR to main. Once merged, ensure the fix is also integrated into your active dev branches or merge it back to dev to prevent reintroduction of the bug.

------------------------------------------------------------------------

## 2. The Power of Pull Requests (PRs)

Pull Requests are essential for code review, quality assurance, and collaborative development before integrating changes into main.

- **2.1 What is a Pull Request?** A mechanism to propose changes from one branch (e.g., dev/my-feature) into another (e.g., main). It\'s not just a merge request; it\'s a **discussion and review platform**.

- **2.2 Benefits of PRs (Dev to Main):**

  - **Code Review:** All changes entering main **must** be reviewed. This allows peers to scrutinize code for:

    - Bugs and errors

    - Code quality and style

    - Adherence to best practices

    - Performance considerations

    - Security vulnerabilities

  - **Improved Code Quality:** Multiple sets of eyes lead to fewer defects and more robust solutions.

  - **Knowledge Sharing:** Developers learn from each other\'s code and approaches.

  - **Collaboration:** Facilitates discussion and feedback before integration.

  - **Historical Record:** PRs provide a clear audit trail of why and how changes were introduced.

  - **Controlled Deployment:** Ensures only approved and tested code makes it to the production branch.

- **2.3 Pull Request Workflow:**

  - **Step 1: Create a dev branch** (as per Section 1.2) and develop your changes.

  - **Step 2: Commit your changes** to your dev branch frequently and with descriptive messages.

  - **Step 3: Push** your dev branch to GitHub: git push origin dev/my-new-feature.

  - **Step 4: Create a Pull Request** on GitHub:

    - **Source:** Your dev branch.

    - **Target:** main branch.

    - **Title:** Make it clear and concise (e.g., \"feat: Implement user authentication,\" \"fix: Resolve login bug\").

    - **Description:** Provide context: What problem does this PR solve? What changes were made? How can the changes be tested (if applicable)? Link to any related issues or tickets.

    - **Reviewers:** Assign appropriate team members for review.

  - **Step 5: Address Feedback:** Respond to comments, make necessary changes, and push new commits to your dev branch (the PR will automatically update).

  - **Step 6: Approval and Merge:** Once approved by at least **\[Number\] reviewer(s)**, the PR can be merged into main. **Prefer \"Squash and Merge\"** for a cleaner main history if individual commits are granular, or \"Create a merge commit\" for preserving all individual commits within the feature branch\'s history.

------------------------------------------------------------------------

## 3. Simple CI/CD Process (Continuous Integration/Continuous Delivery)

Implementing a simple CI/CD process can significantly reduce manual effort and accelerate your development cycle.

- **3.1 What is CI/CD?**

  - **CI (Continuous Integration):** Automating the process of building and testing code every time changes are pushed.

  - **CD (Continuous Delivery):** Automating the release of validated code to various environments (e.g., staging, production).

- **3.2 How a Simple CI/CD Alleviates Time-Consuming Processes:**

  - **Automated Testing:**

    - **Benefit:** Catches bugs early, reduces manual testing effort, and provides immediate feedback on code quality.

    - **Process:** When a PR is opened or a commit is pushed to a dev branch, automatically run unit tests, integration tests, and/or linting.

  - **Automated Builds/Bundling:**

    - **Benefit:** Ensures the application can be built successfully in a consistent environment, saving developers from manual build steps.

    - **Process:** For web applications, automatically compile, transpile, and bundle assets. For backend services, compile binaries or container images.

  - **Automated Deployments (to Staging/Testing Environments):**

    - **Benefit:** Enables quick verification of new features in an environment replicating production, reducing manual deployment errors.

    - **Process:** Upon successful merge to main, automatically deploy the application to a staging or User Acceptance Testing (UAT) environment.

  - **Faster Feedback Loop:** Developers receive immediate notification if their changes break anything, allowing for quick fixes.

  - **Reduced Manual Effort:** Eliminates repetitive, error-prone manual tasks, freeing up developer time for more critical coding.

  - **Increased Confidence:** Knowing that code has passed automated checks builds confidence in releases.

- **3.3 Recommended Tools (for MUSOD Informatics):**

  - **GitHub Actions:** Native to GitHub, easy to configure, and excellent for simple CI/CD workflows.

  - *(A typical workflow: Push code -\> CI pipeline runs tests/builds -\> If successful, option for manual or automated deploy to staging/production.)*

------------------------------------------------------------------------

## 4. Git Best Practices and Etiquette

Adhering to these practices ensures a clean, understandable, and collaborative codebase.

- **4.1 Commit Messages:**

  - Make them clear, concise, and descriptive.

  - Start with a verb in the imperative mood (e.g., \"Fix: Login bug,\" \"Feat: Add user profile page\").

  - Keep the subject line under 50 characters. Use the body for more details if needed.

- **4.2 Frequent Commits:** Commit small, logical chunks of work.

- **4.3 Pull Frequently:** Keep your local branches up-to-date with main (or your base branch) to minimize conflicts.

- **4.4 Resolve Conflicts Locally:** It\'s each developer\'s responsibility to resolve merge conflicts when they arise.

- **4.5 Don\'t Force Push (Unless Absolutely Necessary):** Force pushing (git push \--force) rewrites history and can cause significant issues for collaborators. Only do this if you fully understand the implications and have coordinated with your team.

- **4.6 Clean Up Branches:** Delete dev branches after they have been merged and are no longer needed.

## 5. Troubleshooting Common Issues

- **5.1 Merge Conflicts:** How to identify and effectively resolve them using your chosen IDE\'s integrated tools or command line.

- **5.2 Reverting Changes:** Understanding when to use git revert (to create a new commit that undoes previous changes, preserving history) versus git reset (to move the branch pointer, potentially discarding history).

- **5.3 Accidental Commits/Pushes:** Strategies for recovering from unintended actions.

------------------------------------------------------------------------

## 6. Conclusion

Adherence to these guidelines is crucial for successful team collaboration, consistent code quality, and efficient project delivery within MUSOD Informatics. We encourage feedback and will evolve these guidelines as our needs change.
