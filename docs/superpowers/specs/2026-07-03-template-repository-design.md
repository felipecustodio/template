# Modern Full-Stack Template Repository Design

## Purpose

Provide a minimal repository template for typed browser and Python API projects. Keep placeholder behavior small while proving every selected tool works locally, in git hooks, and in GitHub Actions.

## Repository structure

```text
.
├── .github/workflows/ci.yml
├── backend/
│   ├── src/app/
│   ├── tests/
│   ├── pyproject.toml
│   └── uv.lock
├── frontend/
│   ├── src/
│   ├── package.json
│   ├── tsconfig.json
│   └── vite.config.ts
├── hk.pkl
├── mise.toml
└── README.md
```

Root files coordinate repository-wide operations. `frontend/` and `backend/` remain independently understandable and own their dependencies, sources, and tests.

## Frontend

Vite builds and serves a framework-free TypeScript application. TypeScript enables strict checking with no unchecked indexed access and exact optional properties. Zod defines runtime schemas and derives TypeScript types, preventing duplicated boundary types.

One placeholder page requests the backend health resource, parses the response through Zod, and renders success or failure state. A focused test proves schema acceptance and rejection. Biome owns formatting, linting, and import organization. Aube installs dependencies and runs package scripts; Vite performs compilation and bundling.

## Backend

Robyn serves one `GET /api/health` endpoint. Pydantic models define response and future request boundaries. Handler output comes from model serialization, keeping runtime validation and Python type annotations aligned.

uv owns dependency resolution, virtual-environment synchronization, and `uv.lock`. Karva discovers and runs focused tests covering model validation and health-handler behavior. Python configuration uses strict static checking where supported by selected tooling; mise exposes the check through one repository task.

## Tool orchestration

mise pins runtimes and CLIs, installs them, and defines all developer and CI tasks. Public tasks cover setup, development, formatting, linting, type checking, tests, builds, and aggregate CI validation. Tasks delegate to Aube, Biome, Vite, uv, Karva, and backend type tooling instead of duplicating their behavior.

hk installs and runs git hooks. Pre-commit hooks run fast formatting and lint checks against relevant files. Pre-push hooks run broader type checks and tests. Hook commands call mise tasks so local and CI behavior share command definitions.

## CI

GitHub Actions checks out the repository, installs mise, restores supported caches, installs pinned tools from mise configuration, synchronizes frontend and backend dependencies from committed locks, then invokes the aggregate mise CI task. CI verifies formatting, linting, frontend and backend types, tests, and production frontend build. Concurrency cancels obsolete runs on the same branch.

Dependency and tool lockfiles remain committed. CI uses frozen or locked modes whenever each tool supports them, causing stale lockfiles to fail rather than mutate.

## Error handling

Frontend network, HTTP, and schema failures become a small visible error state without unsafe casts. Backend validation failures use Pydantic errors; the placeholder endpoint only emits validated response data. Developer tasks fail immediately when delegated commands fail. CI preserves command exit status.

## Verification

Repository acceptance requires:

- clean dependency installation through Aube and uv;
- Biome formatting and lint checks pass;
- strict frontend type checking passes;
- backend type checking passes;
- frontend tests pass through an Aube script;
- backend tests pass through Karva;
- Vite production build succeeds through an Aube script;
- hk configuration loads and hooks install;
- aggregate mise CI task passes from a clean checkout;
- GitHub Actions uses mise and runs the same aggregate task;
- README documents prerequisites, setup, task commands, structure, and template-renaming steps.

## Exclusions

Template includes no database, authentication, deployment target, frontend framework, generated domain objects, or production business logic. Future projects add these after repository creation.
