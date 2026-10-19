# Handoff

Snapshot of where the work stands, so anyone — human or AI — can pick it up without the chat history.
Overwritten (not appended) at the end of each session by the `handoff` workflow. Git is the log.
Keep it under ~60 lines.

**Last updated:** 2026-10-19 · **Branch:** `main` · **Commit:** initial project commit

## Current state

- Project initialized from Bootstart: Python 3.14 + Typer on the `python` stack pack
  ([ADR 0001](decisions/0001-stack-choice.md)).
- `just dev` runs the CLI (`src/bootstart_trial/cli.py`), which only prints its help so far.
- `just check` passes; CI runs the same command on every pull request.
- `src/bootstart_trial/pricing.py` and its tests are the template's example module, kept as a
  reference for the conventions.

## In progress

- _Nothing._

## Next steps

1. First feature: a `convert` command that converts a temperature between Celsius, Fahrenheit and
   Kelvin (`/feature`).
2. Once real code is tested, delete the `pricing` example module and `tests/test_pricing.py`.

## Pitfalls

- _None yet._

## Open questions

- _None._
