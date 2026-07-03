# Full-Stack Project Template

Minimal project base with typed browser and API boundaries. Vite builds strict TypeScript; Zod validates browser data; Robyn serves Pydantic models. mise pins tools and runs every local or CI workflow.

## Prerequisite

Install [mise](https://mise.jdx.dev/). mise installs Node, Python, Aube, uv, and hk at versions locked by this repository.

## Setup

```sh
mise trust
mise install --locked
mise run install
mise exec -- hk install --mise
```

`mise run install` uses `aube ci` for frontend dependencies and `uv sync --locked --all-groups` for backend dependencies. Commit both `frontend/aube-lock.yaml` and `backend/uv.lock` after dependency changes.

## Development

Run both services:

```sh
mise run dev
```

Frontend runs at <http://localhost:5173>. Robyn API runs at <http://localhost:8080>; Vite proxies `/api` requests to it.

Run services separately with `mise run dev:frontend` and `mise run dev:backend`.

## Tasks

| Command | Purpose |
| --- | --- |
| `mise run install` | Synchronize locked dependencies |
| `mise run dev` | Run frontend and backend |
| `mise run format` | Format supported sources |
| `mise run format:check` | Check formatting without changes |
| `mise run lint` | Run Biome lint rules |
| `mise run typecheck` | Run TypeScript and ty checks |
| `mise run test` | Run contract, Vitest, and Karva tests |
| `mise run build` | Build production frontend assets |
| `mise run ci` | Run complete CI validation |

Use `mise tasks` for focused task names.

## Repository structure

```text
.
├── .github/workflows/ci.yml  # GitHub Actions validation
├── backend/                  # Robyn, Pydantic, uv, Karva, ty
├── frontend/                 # Vite, TypeScript, Zod, Biome, Aube
├── tests/                    # Repository contract tests
├── hk.pkl                    # Git hook checks
├── mise.lock                 # Cross-platform tool lock
└── mise.toml                 # Tool versions and tasks
```

## Git hooks

hk runs frontend checks and repository contract tests before commits. Pre-push hooks run all type checks and tests. `--mise` makes generated hooks resolve hk and project tools without shell activation.

Reinstall hooks after changing hook configuration:

```sh
mise exec -- hk install --mise
```

## Continuous integration

GitHub Actions installs the locked toolchain through `jdx/mise-action`, restores its cache, installs locked project dependencies, and runs `mise run ci`. Local and CI commands therefore share one task graph.

## Using this template

After creating a repository from this template:

1. Replace `template-frontend` and `template-backend` package names.
2. Replace placeholder README title and descriptions.
3. Replace health page and endpoint while retaining Zod and Pydantic boundaries.
4. Update runtime or tool versions with `mise use`, then run `mise lock`.
5. Update dependencies through Aube or uv and commit both dependency lockfiles.
6. Run `mise run ci` before first push.
