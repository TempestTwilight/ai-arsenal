<!-- omh:agent-instructions:begin -->
# AI Arsenal

Open ecosystem directory and knowledge hub for AI engineering. Tracks models, MCP servers, agent skills/plugins, frameworks, datasets, blueprints, and engineering guides with evidence-based verification and provenance.

Source of truth for roadmap and domain requirements: `docs/scope.md` and `docs/roadmap.md`.

## Dev Environment

- **Python**: 3.14 (`.python-version: 3.14`, `requires-python = ">=3.14"`)
- **Package & env manager**: `uv` (workspace root `pyproject.toml`, lockfile `uv.lock`)
- **Virtualenv**: `.venv/`

## Build & Test

Exact invocations (run from repository root):

- `uv sync`: Install project and dependencies (verified exit 0, 2026-11-10)
- `uv run ruff check`: Run linter across codebase (verified exit 0, 2026-11-10)
- `uv run ruff format --check`: Check formatting without modifying files (verified exit 0, 2026-11-10)
- `uv run ruff format`: Auto-format code (verified exit 0, 2026-11-10)
- `uv run ty check`: Static type check via ty (verified exit 0, 2026-11-10)
- `uv run pytest`: Run test suite (verified exits with code 5 when 0 tests exist, 2026-11-10)
- `uv run ai-arsenal`: Run entrypoint script `ai_arsenal:main` (verified exit 0, 2026-11-10)

## Code & Architecture Conventions

- **Architecture style**: Modular monolith (`apps/`, `packages/`, `registry/`, `knowledge/`). Introduce components incrementally; do not create empty packages in advance.
- **Dependency direction**: `schemas` -> `core` -> (`database`, `ingestion`, `evaluator`, `search`) -> `API` -> (`CLI`, `Web`, `TUI`). The domain layer never imports API, DB, or UI frameworks.
- **Typing**: Strict type annotations required. Avoid `Any`, untyped dicts for core domain entities, and broad exception swallowing (`except Exception: pass`).
- **Data contracts**: Use Pydantic v2 schemas for runtime data validation; maintain versioned schemas.
- **External claims**: Every external tool/metadata claim must record source provenance and retrieval timestamp. Never guess or fabricate metadata.

## Gates

Before marking any task complete, all gates must pass:
1. `uv run ruff check`
2. `uv run ruff format --check`
3. `uv run ty check`
4. `uv run pytest` (once tests are authored)

## Pitfalls

- **uv.lock vs pyproject.toml**: `uv.lock` is tracked; run `uv sync` after editing dependencies in `pyproject.toml`. Do not edit `uv.lock` by hand.
- **pytest exit code 5**: `pytest` exits with code 5 when no tests are collected. This is normal until the first test file in `tests/` is added.
- **Python 3.14 compatibility**: Python 3.14 has no standalone `pip` module here; use `uv` exclusively. If a third-party dependency fails under 3.14, report the incompatibility before altering global project constraints.
- **No speculative LLM / cloud dependencies in MVP**: MVP core and registry must run standalone with PostgreSQL and full-text search. Avoid adding paid LLM or vector DB dependencies without approval.
<!-- omh:agent-instructions:end -->
