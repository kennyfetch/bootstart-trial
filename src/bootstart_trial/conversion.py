"""Temperature conversion between Celsius, Fahrenheit and Kelvin. Pure functions, no I/O."""

from enum import StrEnum


class TemperatureUnit(StrEnum):
    """A temperature scale, identified by its usual one-letter symbol."""

    CELSIUS = "C"
    FAHRENHEIT = "F"
    KELVIN = "K"


FAHRENHEIT_DEGREES_PER_CELSIUS_DEGREE = 9 / 5
FAHRENHEIT_AT_ZERO_CELSIUS = 32
KELVIN_AT_ZERO_CELSIUS = 273.15

# Checked in the source unit rather than after converting to Celsius: converting first can land a
# few ulps below -273.15 and reject a valid absolute zero.
ABSOLUTE_ZERO_BY_UNIT = {
    TemperatureUnit.CELSIUS: -273.15,
    TemperatureUnit.FAHRENHEIT: -459.67,
    TemperatureUnit.KELVIN: 0.0,
}


def convert_temperature(
    temperature: float, from_unit: TemperatureUnit, to_unit: TemperatureUnit
) -> float:
    """Return `temperature`, expressed in `from_unit`, converted to `to_unit`.

    Raises:
        ValueError: If `temperature` is below absolute zero in `from_unit`.
    """
    absolute_zero = ABSOLUTE_ZERO_BY_UNIT[from_unit]
    if temperature < absolute_zero:
        raise ValueError(
            f"temperature must be >= {absolute_zero} {from_unit} (absolute zero), got {temperature}"
        )
    if from_unit == to_unit:
        return temperature
    return _celsius_to(_to_celsius(temperature, from_unit), to_unit)


def _to_celsius(temperature: float, unit: TemperatureUnit) -> float:
    match unit:
        case TemperatureUnit.CELSIUS:
            return temperature
        case TemperatureUnit.FAHRENHEIT:
            return (
                temperature - FAHRENHEIT_AT_ZERO_CELSIUS
            ) / FAHRENHEIT_DEGREES_PER_CELSIUS_DEGREE
        case TemperatureUnit.KELVIN:
            return temperature - KELVIN_AT_ZERO_CELSIUS


def _celsius_to(celsius: float, unit: TemperatureUnit) -> float:
    match unit:
        case TemperatureUnit.CELSIUS:
            return celsius
        case TemperatureUnit.FAHRENHEIT:
            return celsius * FAHRENHEIT_DEGREES_PER_CELSIUS_DEGREE + FAHRENHEIT_AT_ZERO_CELSIUS
        case TemperatureUnit.KELVIN:
            return celsius + KELVIN_AT_ZERO_CELSIUS
