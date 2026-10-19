"""Command-line entry point: parses arguments and prints results, nothing else."""

import typer

app = typer.Typer(no_args_is_help=True)


@app.callback()
def main() -> None:
    """Convert temperatures between Celsius, Fahrenheit and Kelvin."""
