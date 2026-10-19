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
| `src/…` | _…_ |

## Main flows

_The two or three most important flows, step by step (e.g. "an order is placed")._

## Constraints

- Runs on Windows, macOS and Linux with Python 3.14; fully offline.
- No hard performance, security or privacy constraint: no data is stored or sent anywhere.

## Key decisions

_Links to the ADRs that explain the structure above._

- [0001 — Stack choice](decisions/0001-stack-choice.md)
