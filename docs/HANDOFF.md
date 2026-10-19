# Handoff

Snapshot of where the work stands, so anyone — human or AI — can pick it up without the chat history.
Overwritten (not appended) at the end of each session by the `handoff` workflow. Git is the log.
Keep it under ~60 lines.

**Last updated:** 2026-10-19 · **Branch:** `feat/convert-command` · **Commit:** `58f0c56` (base; this
note ships in the commit on top of it)

## Current state

- `bootstart-trial convert <temperature> --from C|F|K --to C|F|K` converts a temperature and prints
  it with two decimals (`just dev convert -40 --from C --to F`). Units are case-insensitive.
- A non-finite value (`nan`, `inf`) or a value below absolute zero in its source unit is a usage
  error (exit code 2) naming the value. Tiny negative results print as `0.00`, not `-0.00`.
- Conversion logic lives in `src/bootstart_trial/conversion.py` and does not import Typer; the CLI
  is in `src/bootstart_trial/cli.py`. See `docs/ARCHITECTURE.md`.
- `just check` passes (34 tests, 97 % coverage).

## In progress

- [PR #1](https://github.com/kennyfetch/bootstart-trial/pull/1) (`feat/convert-command`): the
  `convert` command, open and waiting for green CI and a squash merge.

## Next steps

1. Reject results that overflow to infinity: `convert 1e308 --from C --to F` prints `inf` with exit
   code 0. Check `math.isfinite` on the converted value too, with tests in both test files.
2. Raise a specific `InvalidTemperatureError(ValueError)` in `conversion.py` and catch only that in
   the CLI, so an unrelated `ValueError` is not reported as bad input (CONVENTIONS §5).
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
