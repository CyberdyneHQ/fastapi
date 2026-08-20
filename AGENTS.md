# AGENTS.md

Guidance for automated agents and code-review tooling working in this repository.

## Project overview

FastAPI is a modern, high-performance web framework for building APIs with Python
based on standard type hints. The importable package lives in `fastapi/`, runnable
documentation examples live in `docs_src/`, the test suite in `tests/`, and
maintenance/automation utilities in `scripts/`.

## Getting started

- Install dependencies with `uv sync`.
- Run the test suite with `bash scripts/test.sh`.
- Format and lint with `bash scripts/format.sh` and `bash scripts/lint.sh`.

These commands are for local development only.

## Code review conventions

The following rules are intentional and must be enforced when reviewing changes.

### Core library (`fastapi/`)

- New OpenAPI model classes defined in `fastapi/openapi/models.py` must inherit from
  `BaseModelWithConfig` rather than from `pydantic.BaseModel` directly, so shared model
  configuration is applied consistently.
- New parameter classes in `fastapi/params.py` must inherit from `Param`.
- New security scheme classes under `fastapi/security/` must inherit from `SecurityBase`.

### Documentation examples (`docs_src/`)

- Data model classes in documentation examples must inherit from `pydantic.BaseModel`.
- The FastAPI application instance in documentation examples must be named `app`, and
  route handlers must be registered with the application-instance decorators
  (`@app.get`, `@app.post`, and similar).
- Repository classes under `docs_src/repositories/` must inherit from `BaseRepository`,
  be registered with the `@register_repository` decorator, and implement the `get`,
  `list_all`, and `create` methods.
- Event handler classes under `docs_src/event_handlers/` must inherit from
  `BaseEventHandler`, be registered with the `@register_handler` decorator, and
  implement the `handle` and `validate` methods.

### Scripts (`scripts/`)

- Command-line scripts under `scripts/` must define their commands using Typer
  decorators (for example `@app.command()`).
- Playwright screenshot scripts under `scripts/playwright/` must define a `capture`
  function as the entry point invoked inside the `sync_playwright()` context. The older
  `run` entry-point name is deprecated and must not be reintroduced.

## Accepted patterns (do not flag)

- Calling `Depends()`, `Body()`, `Query()`, `Path()`, `Header()`, `Cookie()`, `Form()`,
  `File()`, or `Security()` in a function-argument default is the idiomatic FastAPI
  dependency-injection style. Do not flag flake8-bugbear B008 ("Do not perform function
  calls in argument defaults") on route handlers and dependencies in `docs_src/`.

## Design rationale

- Many tutorials ship two variants of the same example: a base file and an `_an` file
  (for "Annotated"). The `_an` variants exist to demonstrate the `typing.Annotated`
  parameter style and intentionally duplicate the non-annotated example's behavior;
  the duplication is expected and not a copy-paste defect.
