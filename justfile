# Python stack: uv + Ruff + Pyright + pytest. Recipe contract: docs/STACKS.md.

set windows-shell := ["powershell.exe", "-NoLogo", "-NoProfile", "-Command"]

# List recipes
default:
    @{{ just_executable() }} --list

# Install dependencies into .venv (CI sets UV_LOCKED=1, so a stale lockfile fails there)
setup:
    uv sync

# Run the CLI locally; extra arguments go to the app (e.g. just dev --help)
dev *args:
    uv run bootstart-trial {{ args }}

# Format code in place (also run by the Claude Code edit hook)
format:
    uv run ruff format .

# Format and apply safe lint fixes
fix: format
    uv run ruff check --fix .

# Check lockfile, formatting and lint rules without changing files
lint:
    uv lock --check
    uv run ruff format --check .
    uv run ruff check .

# Static type checking
typecheck:
    uv run pyright

# Run tests with coverage; extra arguments go to pytest
test *args:
    uv run pytest {{ args }}

# Everything CI runs
check: lint typecheck test
