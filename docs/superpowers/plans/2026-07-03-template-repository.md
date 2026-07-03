# Modern Full-Stack Template Repository Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a verified placeholder repository combining a strict Vite/TypeScript/Zod frontend, Robyn/Pydantic backend, Aube and uv dependency workflows, Karva tests, hk hooks, mise tasks, and GitHub Actions CI.

**Architecture:** Root configuration owns tool versions, repository tasks, hooks, CI, and documentation. `frontend/` and `backend/` own isolated application code, dependency manifests, locks, and focused tests; one health contract demonstrates typed runtime boundaries.

**Tech Stack:** Vite, TypeScript, Zod, Biome, Vitest, Aube, Python, uv, Robyn, Pydantic, Karva, ty, hk, mise, GitHub Actions

---

### Task 1: Repository contract checks

**Files:**
- Create: `tests/test_template.py`
- Create: `.gitignore`
- Test: `tests/test_template.py`

- [ ] **Step 1: Write failing structural tests**

Use Python standard-library tests that assert required manifests, locks, source files, task names, hook configuration, and CI workflow exist and contain each mandated tool name.

- [ ] **Step 2: Run tests and verify failure**

Run: `python -m unittest tests/test_template.py -v`
Expected: FAIL because implementation files do not exist.

- [ ] **Step 3: Add ignore rules**

Ignore `.mise/`, `.venv/`, `node_modules/`, `dist/`, caches, coverage, and local environment files while retaining lockfiles.

- [ ] **Step 4: Commit contract test**

```bash
git add tests/test_template.py .gitignore
git commit -m "test: define template contract"
```

### Task 2: Backend health boundary

**Files:**
- Create: `backend/pyproject.toml`
- Create: `backend/src/app/__init__.py`
- Create: `backend/src/app/models.py`
- Create: `backend/src/app/main.py`
- Create: `backend/tests/test_health.py`
- Create: `backend/uv.lock`

- [ ] **Step 1: Add failing Karva tests**

Test that `HealthResponse(status="ok")` serializes to `{"status": "ok"}`, rejects invalid literals, and `health()` returns serialized validated data.

- [ ] **Step 2: Define backend package**

Configure Python 3.13, runtime dependencies `robyn` and `pydantic`, development dependencies `karva` and `ty`, a `src` package, and strict ty settings supported by current release.

- [ ] **Step 3: Lock and sync dependencies**

Run: `cd backend && uv lock && uv sync --all-groups`
Expected: `uv.lock` created and environment synchronized.

- [ ] **Step 4: Verify tests fail**

Run: `cd backend && uv run karva test tests/`
Expected: FAIL because health implementation is absent.

- [ ] **Step 5: Implement Pydantic model and Robyn route**

Create a literal-status `HealthResponse`, pure `health()` serializer, Robyn application, `/api/health` route, and guarded `app.start()` entry point.

- [ ] **Step 6: Verify backend**

Run: `cd backend && uv run karva test tests/ && uv run ty check`
Expected: tests and type checks PASS.

- [ ] **Step 7: Commit backend**

```bash
git add backend
git commit -m "feat(api): add typed health endpoint"
```

### Task 3: Frontend health client

**Files:**
- Create: `frontend/index.html`
- Create: `frontend/package.json`
- Create: `frontend/tsconfig.json`
- Create: `frontend/vite.config.ts`
- Create: `frontend/src/health.ts`
- Create: `frontend/src/health.test.ts`
- Create: `frontend/src/main.ts`
- Create: `frontend/src/style.css`
- Create: `frontend/aube-lock.yaml`

- [ ] **Step 1: Define package and strict compiler settings**

Add Vite, TypeScript, Zod, Biome, and Vitest dependencies. Add `dev`, `format`, `format:check`, `lint`, `typecheck`, `test`, and `build` scripts. Enable `strict`, `noUncheckedIndexedAccess`, `exactOptionalPropertyTypes`, and bundler module resolution.

- [ ] **Step 2: Install through Aube**

Run: `cd frontend && aube install`
Expected: dependencies installed and `aube-lock.yaml` created.

- [ ] **Step 3: Write failing schema tests**

Test accepted `{status: "ok"}` payload and rejected unknown status through exported Zod schema.

- [ ] **Step 4: Verify tests fail**

Run: `cd frontend && aube run test`
Expected: FAIL because schema implementation is absent.

- [ ] **Step 5: Implement browser placeholder**

Define Zod health schema and inferred type, fetch with HTTP error handling, parse unknown JSON, and render loading, healthy, or error state without casts. Add minimal accessible HTML and CSS.

- [ ] **Step 6: Verify frontend**

Run: `cd frontend && aube run format:check && aube run lint && aube run typecheck && aube run test && aube run build`
Expected: every command PASS and `frontend/dist/` exists.

- [ ] **Step 7: Commit frontend**

```bash
git add frontend
git commit -m "feat(web): add typed health client"
```

### Task 4: mise orchestration and hk hooks

**Files:**
- Create: `mise.toml`
- Create: `mise.lock`
- Create: `hk.pkl`
- Modify: `tests/test_template.py`

- [ ] **Step 1: Extend failing contract tests**

Assert mise pins Node, Python, Aube, uv, and hk; public tasks cover install, dev, format, lint, typecheck, test, build, and CI; hk contains pre-commit and pre-push hooks delegated through mise.

- [ ] **Step 2: Verify contract failure**

Run: `python -m unittest tests/test_template.py -v`
Expected: FAIL because root tooling files are absent.

- [ ] **Step 3: Add pinned tools and tasks**

Configure current stable versions resolvable by mise. Make `install` run `aube install` and `uv sync --locked --all-groups`; make aggregate tasks depend on focused frontend/backend tasks; make `ci` depend on install, format check, lint, typecheck, test, and build.

- [ ] **Step 4: Add hk hooks**

Configure pre-commit Biome checks for frontend files and repository contract checks. Configure pre-push aggregate type and test tasks. Use mise execution so hooks resolve pinned tools.

- [ ] **Step 5: Lock and verify tools**

Run: `mise install && mise lock && mise run install && hk validate && hk install`
Expected: tools resolve, lock is written, dependencies synchronize, configuration validates, hooks install.

- [ ] **Step 6: Verify task graph**

Run: `mise tasks && mise run ci`
Expected: required public tasks listed and aggregate CI PASS.

- [ ] **Step 7: Commit orchestration**

```bash
git add mise.toml mise.lock hk.pkl tests/test_template.py
git commit -m "build: orchestrate repository tooling"
```

### Task 5: GitHub Actions CI

**Files:**
- Create: `.github/workflows/ci.yml`
- Modify: `tests/test_template.py`

- [ ] **Step 1: Extend failing workflow tests**

Assert workflow triggers pushes and pull requests, sets concurrency, installs mise with official action, installs locked tools, and calls `mise run ci`.

- [ ] **Step 2: Verify contract failure**

Run: `python -m unittest tests/test_template.py -v`
Expected: FAIL because workflow is absent.

- [ ] **Step 3: Implement workflow**

Use `actions/checkout`, `jdx/mise-action`, locked mise installation, dependency caches where supported, least-privilege permissions, timeout, concurrency cancellation, and one `mise run ci` validation command.

- [ ] **Step 4: Validate workflow and aggregate CI**

Run: `python -m unittest tests/test_template.py -v && mise run ci`
Expected: contract and full repository checks PASS.

- [ ] **Step 5: Commit CI**

```bash
git add .github/workflows/ci.yml tests/test_template.py
git commit -m "ci: validate template through mise"
```

### Task 6: Template documentation and clean-checkout audit

**Files:**
- Modify: `README.md`
- Modify: `tests/test_template.py`

- [ ] **Step 1: Write README contract test**

Assert README covers prerequisites, setup, development, checks, structure, CI, hooks, and rename steps.

- [ ] **Step 2: Rewrite README**

Document mise bootstrap, `mise install`, `mise run install`, hook installation, task table, service URLs, repository structure, lockfile policy, and post-template rename checklist.

- [ ] **Step 3: Run full verification**

Run: `git diff --check && python -m unittest tests/test_template.py -v && mise run ci && git status --short`
Expected: no whitespace errors; all checks PASS; status shows only intended README/test/plan changes.

- [ ] **Step 4: Audit objective requirement by requirement**

Confirm direct evidence for Vite, strict TypeScript, Zod, Biome, Aube, uv lock/sync, Karva, Robyn, Pydantic, hk, mise tasks/tool installation, and complete GitHub CI.

- [ ] **Step 5: Commit documentation**

```bash
git add README.md tests/test_template.py docs/superpowers/plans/2026-07-03-template-repository.md
git commit -m "docs: document template workflow"
```
