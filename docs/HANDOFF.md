# Handoff

Snapshot of where the work stands, so anyone — human or AI — can pick it up without the chat history.
Overwritten (not appended) at the end of each session by the `handoff` workflow. Git is the log.
Keep it under ~60 lines.

**Last updated:** 2026-10-19 · **Branch:** `feat/convert-command` · **Commit:** `a849712` (base; this
note ships in the commit on top of it)

## Current state

- `bootstart-trial convert <temperature> --from C|F|K --to C|F|K` converts a temperature and prints
  it with two decimals (`just dev convert -40 --from C --to F`). Units are case-insensitive.
- A value below absolute zero in its source unit is a usage error (exit code 2) naming the value.
- Conversion logic lives in `src/bootstart_trial/conversion.py` and does not import Typer; the CLI
  is in `src/bootstart_trial/cli.py`. See `docs/ARCHITECTURE.md`.
- `just check` passes (29 tests, 97 % coverage).

## In progress

- `feat/convert-command`: the `convert` command, being shipped as a pull request.

## Next steps

1. Reject non-finite input in `convert_temperature` (`nan`, `inf`): today `convert nan --from C
   --to F` prints `nan` with exit code 0. Add tests in `tests/test_conversion.py` and through the CLI.
2. Avoid printing `-0.00` for tiny negative results (e.g. `convert -0.001 --from C --to C`).
3. Delete the template's `pricing` example (`src/bootstart_trial/pricing.py`,
   `tests/test_pricing.py`) and its row in `docs/ARCHITECTURE.md`.

## Pitfalls

- Click reads a negative number such as `-40` as an option: the `convert` command sets
  `ignore_unknown_options` so negative temperatures work.
- On Windows, `just` runs recipes through `powershell -Command`, which reports any failure as exit
  code 1: check exit codes with `uv run bootstart-trial …` directly.
- On Windows, run `scripts/setup-github.sh` from Git Bash: in PowerShell, `bash` starts WSL.

## Open questions

- _None._
