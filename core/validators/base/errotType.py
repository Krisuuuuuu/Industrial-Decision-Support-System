from enum import Enum


class ErrorType(Enum):
    INVALID_CARBON_VALUE = 1,
    INVALID_SILICON_VALUE = 2,
    INVALID_MAGNESIUM_VALUE = 3,
    INVALID_SULFUR_VALUE = 4,
    INVALID_AUSTENIZATION_TEMPERATURE_VALUE = 5,
    INVALID_AUSTENIZATION_TIME_VALUE = 6,
    INVALID_ISOTHERMAL_TEMPERATURE_VALUE = 7,
    INVALID_ISOTHERMAL_TIME_VALUE = 8,
    INVALID_WALL_THICKNESS_VALUE = 9,
    INVALID_EXPECTED_SPECIES_VALUE = 10
