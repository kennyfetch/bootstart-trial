from typer.testing import CliRunner

from bootstart_trial.cli import app

runner = CliRunner()


def test_cli_prints_usage_with_help_option() -> None:
    result = runner.invoke(app, ["--help"])

    assert result.exit_code == 0
    assert "Usage" in result.output


def test_convert_prints_converted_temperature_with_two_decimals() -> None:
    result = runner.invoke(app, ["convert", "100", "--from", "C", "--to", "F"])

    assert result.exit_code == 0
    assert result.stdout == "212.00\n"


def test_convert_accepts_lowercase_units() -> None:
    result = runner.invoke(app, ["convert", "0", "--from", "c", "--to", "k"])

    assert result.exit_code == 0
    assert result.stdout == "273.15\n"


def test_convert_accepts_negative_temperature() -> None:
    result = runner.invoke(app, ["convert", "-40", "--from", "C", "--to", "F"])

    assert result.exit_code == 0
    assert result.stdout == "-40.00\n"


def test_convert_fails_below_absolute_zero() -> None:
    result = runner.invoke(app, ["convert", "-500", "--from", "C", "--to", "K"])

    assert result.exit_code != 0
    assert "-500" in result.stderr


def test_convert_rejects_unknown_unit() -> None:
    result = runner.invoke(app, ["convert", "10", "--from", "X", "--to", "C"])

    assert result.exit_code == 2
