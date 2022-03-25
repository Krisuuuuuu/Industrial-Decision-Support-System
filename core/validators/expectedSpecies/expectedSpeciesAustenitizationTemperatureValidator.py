from core.validators.base.baseValidator import BaseValidator
from core.validators.base.models.errorAreaEnum import ErrorArea
from core.validators.base.models.errorTypeEnum import ErrorType
from core.validators.expectedSpecies.models.species import Species
from data.models.adiDuctileIronModel import AdiDuctileIronModel


class ExpectedSpeciesAustenizationTemperatureValidator(BaseValidator):
    def __init__(self, model: AdiDuctileIronModel, species_model: Species):
        self._species_model: Species = species_model
        super().__init__(ErrorArea.EXPECTED_SPECIES, ErrorType.INVALID_EXPECTED_SPECIES_AUSTENITIZATION_TEMPERATURE,
                         "Expected species - austenitization temperature validator", model)

    def validate(self) -> None:
        self._occurs = \
            self._species_model.min_austenitization_temperature_value <= \
            self._model.manufacturing_process.austenitization_temperature <= \
            self._species_model.max_austenitization_temperature_value
