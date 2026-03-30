# Maintaining This Documentation Hub

This repository is not the documentation for one application. It is a documentation hub for multiple systems, workflows, environments, and knowledge-transfer artifacts.

The maintenance goal is to keep the hub accurate, navigable, and easy for the next developer or maintainer to extend.

## What Is Source And What Is Output

- `docs/` is the source content for the site.
- `mkdocs.yml` is the site configuration and the source of the left-hand sidebar structure.
- `site/` is generated output from MkDocs build steps and should not be treated as the primary source of truth for content edits.
- `.github/workflows/static.yml` is the GitHub Actions workflow that builds and deploys the site to GitHub Pages.
- `site/` should be ignored in Git because the published output is rebuilt by CI/CD.

## The Two Navigation Systems

There are two different navigation patterns in this repository. They serve different purposes and both matter.

### 1. Sidebar Navigation In `mkdocs.yml`

The `nav:` section in `mkdocs.yml` controls the generated sidebar structure.

Use `mkdocs.yml` when you need to:

- add a page to the global site navigation
- change sidebar labels
- change the order of sections or pages
- expose a page that would otherwise only be reachable by direct link
- keep major sections consistent across the whole site

Important distinction:

- If a file exists in `docs/` but is not represented in the `nav:` section, it may still build, but it will not automatically appear in the main sidebar where users expect to browse.
- The sidebar is the hub-level navigation model. Treat it as the table of contents for the whole documentation site.

### 2. Contextual Navigation In `index.md` Files And Inline Links

The various section `index.md` files and relative links inside Markdown pages provide the normal in-content navigation.

Use section indexes and inline links when you need to:

- introduce a section and explain what belongs there
- link related pages within a topic area
- create a local landing page for a system, guide collection, or workflow group
- give readers next steps without forcing them back to the sidebar

Important distinction:

- `index.md` files do not replace the sidebar.
- The sidebar gets a reader into the right area of the hub.
- Section indexes and inline links help the reader move around once they are already inside that area.

### Maintenance Rule

When adding or restructuring documentation, evaluate both layers every time:

1. Does this page need to appear in the hub-wide sidebar in `mkdocs.yml`?
2. Does the relevant local `index.md` also need a link so the page is discoverable inside its section?

If only one of those gets updated, navigation becomes inconsistent.

## Recommended Workflow For Adding Or Updating Docs

1. Decide where the content belongs under `docs/`.
2. Update or create the Markdown page.
3. Update the closest section `index.md` so the page is discoverable in-context.
4. Update `mkdocs.yml` if the page should appear in the sidebar.
5. Run a local MkDocs build or serve command.
6. Verify links, headings, and placement in the generated site.
7. Commit only source changes that should be maintained long-term.

## Setting Up A New Local Repo For The Next Developer

These steps assume Windows and PowerShell, which matches the current development environment.

### Prerequisites

- Git installed
- Python installed
- permission to access the GitHub repository

### Initial Setup

1. Clone the repository.
2. Open the repo folder in VS Code.
3. Create a virtual environment if one does not already exist:

```powershell
python -m venv .venv
```

4. Activate the environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

5. Install dependencies from the repository requirements file:

```powershell
pip install -r requirements.txt
```

Notes:

- The repository currently uses the file name `requirements.txt`.
- If dependency updates are made, refresh that file intentionally rather than assuming it is current.

6. If a developer chooses not to use `requirements.txt`, install the core documentation packages directly:

```powershell
pip install mkdocs
pip install mkdocs-material
```

- The preferred setup path is still `pip install -r requirements.txt` because it reflects the repository's maintained dependency set.
- The direct package installs above are a fallback for getting the site running when a developer only needs the MkDocs tooling.

## Running The Site Locally

To start the local development server:

```powershell
mkdocs serve
```

MkDocs will typically expose the site at:

```text
http://127.0.0.1:8000/
```

Use local serve when you want to:

- preview page formatting
- check sidebar placement
- verify section indexes and internal links
- validate that new files are included where expected

## Testing And Validation

For this repository, the practical validation step is the MkDocs build itself.

Run:

```powershell
mkdocs build --strict
```

Use strict build before opening a pull request or merging to `main` because it helps catch:

- broken links
- missing referenced files in navigation
- configuration issues that would fail CI

Also note:

- MkDocs may report pages that exist under `docs/` but are not included in `nav:`.
- That is not always an error. Some pages may be intentionally reachable only through local indexes or direct links.
- The key maintenance question is whether the omission from sidebar navigation is deliberate.

If you need a clean local output first, you can also use:

```powershell
mkdocs build --clear
```

## Deployment Model

Deployment is currently handled through GitHub Actions CI/CD.

The active workflow is:

- `.github/workflows/static.yml`

Current behavior:

- a push to `main` triggers the workflow
- the workflow can also be started manually with `workflow_dispatch`
- GitHub Actions builds the MkDocs site
- the generated `site/` output is uploaded as the Pages artifact
- GitHub Pages publishes the result

### What The Workflow Currently Does

At a high level, the workflow:

1. checks out the repo
2. sets up Python 3.11
3. installs MkDocs Material
4. runs `mkdocs build --strict`
5. deploys the generated site to GitHub Pages

### Practical Deployment Guidance

- Do not treat deployment as a manual file-copy process.
- Do not edit the published site as if it were the source.
- Make documentation changes in source files, verify locally, then merge to `main`.
- If deployment fails, inspect the GitHub Actions run before assuming the content is wrong.
- Be aware that local builds currently regenerate files under `site/`, so a validation build may create additional working-tree changes even when your real source edits were only in `docs/` or `mkdocs.yml`.

## Operational Guardrails

- Keep source edits in `docs/` and `mkdocs.yml`.
- Avoid making manual maintenance edits directly inside generated site output.
- Keep the sidebar labels stable unless there is a real information architecture reason to change them.
- Prefer small, deliberate navigation updates over large reorganizations without a migration plan.
- When introducing a new major section, add both a local section index and a matching sidebar entry.

## Suggested Checklist For Maintainers

- Is the content in the correct folder under `docs/`?
- Is the page linked from the correct local `index.md`?
- Is the page included in `mkdocs.yml` if it should appear in the sidebar?
- Does `mkdocs serve` show the page in the expected location?
- Does `mkdocs build --strict` pass before merge?
- Is the GitHub Actions deployment behavior still aligned with the documented process?

## Additional Reference Links

- Material for MkDocs reference: https://squidfunk.github.io/mkdocs-material/reference/
- MkDocs documentation: https://www.mkdocs.org/