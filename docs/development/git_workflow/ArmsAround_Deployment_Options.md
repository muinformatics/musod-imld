# GIT Hub Pages

The key is that answer depends on what we mean by “private.”

If you want the MkDocs site to stay on **GitHub Pages** and be accessible only to authorized users, GitHub’s built-in access control for Pages requires an **organization on GitHub Enterprise Cloud**. A privately published Pages site can then be viewed only by people who have **read access to the repository** it is published from. ([GitHub Docs][1])

If you are **not** on GitHub Enterprise Cloud, then simply making the repo private is not enough for a normal GitHub Pages setup. GitHub’s docs state that, unless your enterprise uses Enterprise Managed Users, Pages sites are publicly available by default even when the source repository is private or internal. ([GitHub Docs][2])

### Practical paths

**Path 1 — Keep GitHub Pages and make the site private**
This is the cleanest path if the organization is willing to pay for Enterprise Cloud. The high-level steps are:

1. Move or keep the docs repo inside a **GitHub organization**.
2. Ensure that organization is on **GitHub Enterprise Cloud**.
3. In the repo, go to **Settings → Pages**.
4. Change the Pages visibility from **Public** to **Private**.
5. Grant repo read access only to the people who should see the documentation.
6. Keep the current GitHub Actions / Pages publish workflow, then test access with an authorized and unauthorized account. GitHub documents the visibility toggle in repo Pages settings, and private Pages access is tied to repository read permissions. ([GitHub Docs][1])

### Cost

GitHub’s pricing page currently shows:

* **Team** starting at **$4/user/month**
* **Enterprise** starting at **$21/user/month** ([GitHub][3])

For the use case, the important point is that **private GitHub Pages requires Enterprise Cloud**, not Team. ([GitHub Docs][2])

### Actions / workflow cost impact

Since the site is built through a GitHub workflow, moving the repo from public to private can affect Actions billing. GitHub says Actions on **public repositories** are free for standard GitHub-hosted runners, while **private repositories** get only plan-based included minutes/storage and overages are billed. ([GitHub Docs][4])

GitHub’s pricing page currently shows included Actions minutes of about:

* **Team:** 3,000 CI/CD minutes/month
* **Enterprise:** 50,000 CI/CD minutes/month ([GitHub][3])

GitHub also announced a **$0.002/minute cloud platform charge** for Actions usage beginning **March 1, 2026**, applying to usage subject to that billing model. ([The GitHub Blog][5])

### Path 2 — Keep the repo private, but stop using GitHub Pages for access-controlled hosting

If you do **not** want Enterprise Cloud pricing, the usual alternative is:

* keep the repo private on GitHub,
* build the MkDocs site with GitHub Actions,
* deploy the generated static site somewhere else that supports authentication directly.

Common examples are an internal web server, SharePoint/Teams-adjacent hosting, Azure Static Web Apps behind identity, Netlify with access control, Cloudflare Access, or an S3/CloudFront setup behind SSO. This often ends up cheaper than Enterprise Cloud when the audience is small.

### Recommendation

For a documentation hub like “Arms Around,” the decision is usually this:

If you want **minimal architecture change**, stay with GitHub Pages and upgrade to **GitHub Enterprise Cloud**.

If you want **lowest recurring cost**, keep GitHub for source control and move the published MkDocs site to a host that supports authentication.

For planning purposes, the rough conclusion is:

* **GitHub-native private Pages:** straightforward, but likely **$21/user/month** on Enterprise Cloud. ([GitHub][3])
* **Alternative hosting:** more setup effort, but often cheaper and more flexible for private internal docs.

If you want, I can map this into a concrete decision matrix for the exact situation: small team, number of readers, and whether they already authenticate with Microsoft 365.

[1]: https://docs.github.com/enterprise-cloud%40latest/pages/getting-started-with-github-pages/changing-the-visibility-of-your-github-pages-site "Changing the visibility of your GitHub Pages site - GitHub Enterprise Cloud Docs"
[2]: https://docs.github.com/enterprise-cloud%40latest/pages/getting-started-with-github-pages/creating-a-github-pages-site "Creating a GitHub Pages site - GitHub Enterprise Cloud Docs"
[3]: https://github.com/pricing "Pricing · Plans for every developer · GitHub"
[4]: https://docs.github.com/en/actions/concepts/billing-and-usage "Billing and usage - GitHub Docs"
[5]: https://github.blog/changelog/2025-12-16-coming-soon-simpler-pricing-and-a-better-experience-for-github-actions/ "Update to GitHub Actions pricing - GitHub Changelog"

---
## Questions:

- What constitutes a "user" for Enterprise Cloud ? 
- Can the pages allow for "access" to specific emails without requiring them to be a GitHub user?

This is where the “gotcha” lives with GitHub Pages + Enterprise Cloud. Let’s break it cleanly.

---

# 1. What counts as a “user” in GitHub Enterprise Cloud?

A **billable user** is anyone who is a member of the organization **or** an outside collaborator with access to private repositories.

That includes:

* Org members (developers, admins, etc.)
* Outside collaborators with repo access (even read-only)

It does **NOT** include:

* Anonymous viewers (for public repos)
* People without repo access

👉 **Important implication:**
For a **private GitHub Pages site**, access is tied directly to **repository permissions**.

So:

> If someone can view the private Pages site → they must have access to the repo → they are a billable user.

---

# 2. Can you grant access by email without GitHub accounts?

**Short answer: No.**

GitHub Pages private access works like this:

* Viewer must:

  * Have a **GitHub account**
  * Be **granted access to the repository**
  * Be **logged into GitHub**

There is **no native way** to:

* whitelist arbitrary emails
* allow password-based access
* integrate lightweight access control (like a shared link with auth)
* support non-GitHub users

---

# 3. What this means in practice

Depending upon potential/scalable direction ...

If you have:

* 5 internal devs → fine
* 10 stakeholders → still fine
* 50+ students / faculty / clients → 🚨 cost explodes quickly

Because:

> Every viewer = GitHub user with repo access = billable seat

At ~$21/user/month, this could become **prohibitively expensive** for documentation distribution.

---

# 4. Why GitHub designed it this way

GitHub Pages private mode is essentially:

> “Repository access control = site access control”

It was not designed to be:

* a documentation portal
* a client-facing knowledge base
* a lightweight internal wiki with flexible auth

It’s really meant for:

* internal engineering docs for teams already in GitHub

---

# 5. In our use case: “Arms Around Hub”

Based on what has currently been determined:

* Knowledge transfer artifacts
* Admin assistant uploads 

Future consideration:

* Faculty / stakeholders consuming content
* Potential scale beyond engineers

If we include *Future Considerttions* then ... 👉 This is **not a good fit** for GitHub Enterprise Pages access model.

---

# 6. Better architectural options (aligned to the context)

Now we shift from “can we” → “what else fits the system”

### Option A — Azure Static Web Apps (VERY strong fit)

* Keep repo private in GitHub
* Deploy via GitHub Actions
* Add **Microsoft Entra ID (Azure AD)** auth

**Benefits:**

* Users log in with institutional email (MUSoD / SWTC)
* No GitHub accounts required
* Fine-grained access control
* Likely already aligned with the environment

💰 Cost: Often free or very low for the scale

---

### Option B — Cloudflare Pages + Access

* Deploy MkDocs site
* Protect with **Cloudflare Access (Zero Trust)**

**Benefits:**

* Email-based access control
* One-time login links / SSO
* No GitHub accounts required
* Extremely fast + secure

💰 Cost: Free tier is often sufficient

---

### Option C — S3 + CloudFront + Cognito (AWS)

* More complex
* Fully customizable auth

👉 Probably overkill for the potential trajectory
👉 Can be used if the user base is kept small

---

### Option D — SharePoint / Teams integration (lowest friction)

* Export or embed content
* Leverage existing Microsoft auth

👉 Less elegant technically, but **high adoption**

---

# 7. Strategic recommendation (not just technical)

Given the current trajectory (AI curriculum, knowledge systems, Arms Around Hub):

👉 Treat this as an **internal knowledge platform**, not a “repo artifact.”

Which means:

* GitHub = **source of truth**
* Build pipeline = **artifact generator**
* Hosting = **identity-aware delivery layer**

---

# 8. Bottom line

* A “user” = anyone with repo access (and therefore billed)
* Private GitHub Pages **requires GitHub accounts**
* You **cannot grant access by email alone**

👉 For our use case, GitHub Enterprise is:

* technically valid
* economically inefficient, if we expand the scope of users.

---
