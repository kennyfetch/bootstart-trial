import math
import re

import pytest

from bootstart_trial.conversion import TemperatureUnit, convert_temperature

CELSIUS = TemperatureUnit.CELSIUS
FAHRENHEIT = TemperatureUnit.FAHRENHEIT
KELVIN = TemperatureUnit.KELVIN


@pytest.mark.parametrize(
    ("temperature", "from_unit", "to_unit", "expected"),
    [
        (100, CELSIUS, FAHRENHEIT, 212),
        (32, FAHRENHEIT, CELSIUS, 0),
        (0, CELSIUS, KELVIN, 273.15),
        (300, KELVIN, CELSIUS, 26.85),
        (212, FAHRENHEIT, KELVIN, 373.15),
        (0, KELVIN, FAHRENHEIT, -459.67),
        (-40, CELSIUS, FAHRENHEIT, -40),
    ],
)
def test_convert_temperature_returns_value_in_target_unit(
    temperature: float, from_unit: TemperatureUnit, to_unit: TemperatureUnit, expected: float
) -> None:
    result = convert_temperature(temperature, from_unit, to_unit)

    assert result == pytest.approx(expected)


@pytest.mark.parametrize("unit", list(TemperatureUnit))
def test_convert_temperature_returns_same_value_for_same_unit(unit: TemperatureUnit) -> None:
    result = convert_temperature(21.5, unit, unit)

    assert result == 21.5


@pytest.mark.parametrize(
    ("temperature", "unit"),
    [(-273.15, CELSIUS), (-459.67, FAHRENHEIT), (0, KELVIN)],
)
def test_convert_temperature_accepts_absolute_zero(
    temperature: float, unit: TemperatureUnit
) -> None:
    result = convert_temperature(temperature, unit, KELVIN)

    assert result == pytest.approx(0)


@pytest.mark.parametrize(
    ("temperature", "unit"),
    [(-273.16, CELSIUS), (-459.68, FAHRENHEIT), (-0.01, KELVIN)],
)
def test_convert_temperature_rejects_value_below_absolute_zero(
    temperature: float, unit: TemperatureUnit
) -> None:
    with pytest.raises(ValueError, match=re.escape(str(temperature))):
        convert_temperature(temperature, unit, CELSIUS)


@pytest.mark.parametrize("temperature", [math.nan, math.inf, -math.inf])
def test_convert_temperature_rejects_non_finite_value(temperature: float) -> None:
    with pytest.raises(ValueError, match="finite"):
        convert_temperature(temperature, CELSIUS, FAHRENHEIT)
