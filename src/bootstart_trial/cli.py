"""Command-line entry point: parses arguments and prints results, nothing else."""

from typing import Annotated

import typer

from bootstart_trial.conversion import TemperatureUnit, convert_temperature

app = typer.Typer(no_args_is_help=True)


@app.callback()
def main() -> None:
    """Convert temperatures between Celsius, Fahrenheit and Kelvin."""


# Without ignore_unknown_options, Click reads a negative temperature such as -40 as an option.
@app.command(context_settings={"ignore_unknown_options": True})
def convert(
    temperature: Annotated[float, typer.Argument(help="Temperature to convert.")],
    from_unit: Annotated[
        TemperatureUnit, typer.Option("--from", case_sensitive=False, help="Unit to convert from.")
    ],
    to_unit: Annotated[
        TemperatureUnit, typer.Option("--to", case_sensitive=False, help="Unit to convert to.")
    ],
) -> None:
    """Convert a temperature and print it with two decimals."""
    try:
        converted = convert_temperature(temperature, from_unit, to_unit)
    except ValueError as error:
        raise typer.BadParameter(str(error), param_hint="TEMPERATURE") from error
    # Adding 0.0 turns a rounded -0.0 into 0.0, so tiny negative results do not print as "-0.00".
    typer.echo(f"{round(converted, 2) + 0.0:.2f}")
