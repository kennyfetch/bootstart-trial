# 0001 — Stack choice

- **Status:** Accepted
- **Date:** 2026-10-19

## Context

Bootstart Trial is a small command-line tool that converts temperatures between Celsius, Fahrenheit
and Kelvin. It runs locally on Windows, macOS and Linux, has no network, storage or performance
constraint, and is maintained solo. The repository is a throwaway trial of the Bootstart template.

## Options considered

1. **Python + Typer** — the default for a CLI in `docs/STACKS.md`; shipped pack (uv, Ruff, Pyright,
   pytest), typed argument parsing and generated help. Needs a Python runtime to run.
2. **Go or Rust** — single static binary, no runtime to install; no shipped pack, so the stack
   contract would have to be built by hand, which is not worth it for a tool this small.

## Decision

Python 3.14 with Typer for argument parsing, on the `python` stack pack: uv for dependencies,
Ruff for formatting and linting, Pyright in strict mode, pytest with 80 % coverage.

## Consequences

- Users need Python and uv (or an installed wheel) to run the tool.
- Typer is the only runtime dependency; conversion logic stays in plain modules that do not import
  it, so it can be tested without the CLI.
- If distribution as a single binary becomes important, revisit this choice.
