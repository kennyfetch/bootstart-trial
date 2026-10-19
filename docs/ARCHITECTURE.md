# Architecture

One page, kept current. Describe the shape of the system; details belong in code, and the reasons
behind choices belong in `docs/decisions/`.

## Purpose

A command-line tool that converts temperatures between Celsius, Fahrenheit and Kelvin, for anyone
who needs a quick, exact conversion in a terminal.

## Context

A single user runs it locally in a terminal. It talks to no external system: input comes from
command-line arguments, output goes to standard output and errors to standard error.

## Module map

| Path | Responsibility |
|---|---|
| `src/bootstart_trial/cli.py` | Typer entry point: parses arguments, prints results and errors |
| `src/bootstart_trial/conversion.py` | Pure temperature conversion and absolute-zero validation |
| `src/bootstart_trial/pricing.py` | Template example module, to delete (see `docs/HANDOFF.md`) |

## Main flows

1. **A temperature is converted:** `bootstart-trial convert -40 --from C --to F` → `cli.convert`
   parses the value and units → `conversion.convert_temperature` checks that it is finite and not
   below absolute zero, then converts through Celsius → the CLI prints the result with two
   decimals. An invalid value becomes a usage error (exit code 2) naming the value.

## Constraints

- Runs on Windows, macOS and Linux with Python 3.14; fully offline.
- No hard performance, security or privacy constraint: no data is stored or sent anywhere.

## Key decisions

_Links to the ADRs that explain the structure above._

- [0001 — Stack choice](decisions/0001-stack-choice.md)
