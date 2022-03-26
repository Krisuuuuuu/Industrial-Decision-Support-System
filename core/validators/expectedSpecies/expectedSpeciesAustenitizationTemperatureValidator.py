from core.validators.base.models.errorTypeEnum import ErrorType
from core.validators.expectedSpecies.models.baseExpectedSpeciesValidator import BaseExpectedSpeciesValidator
from core.validators.expectedSpecies.models.species import Species
from data.models.adiDuctileIronModel import AdiDuctileIronModel


class ExpectedSpeciesAustenizationTemperatureValidator(BaseExpectedSpeciesValidator):
    def __init__(self, model: AdiDuctileIronModel, species_model: Species):
        super().__init__(ErrorType.INVALID_EXPECTED_SPECIES_AUSTENITIZATION_TEMPERATURE,
                         "Expected species - austenitization temperature validator", model, species_model)

    def validate(self) -> None:
        self._occurs = \
            not (self._species_model.min_austenitization_temperature_value <= \
                 self._model.manufacturing_process.austenitization_temperature <= \
                 self._species_model.max_austenitization_temperature_value)
