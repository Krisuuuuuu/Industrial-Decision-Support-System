from core.validators.base.baseValidator import BaseValidator
from core.validators.base.models.errorAreaEnum import ErrorArea
from core.validators.base.models.errorTypeEnum import ErrorType


class ExpectedSpeciesIsothermalTransformationValidator(BaseValidator):
    def __init__(self, model, species_model):
        self._species_model = species_model
        super().__init__(ErrorArea.EXPECTED_SPECIES,
                         ErrorType.INVALID_EXPECTED_SPECIES_ISOTHERMAL_TRANSFORMATION_TEMPERATURE,
                         "Expected species - isothermal transformation temperature validator", model)

    def validate(self):
        self._occurs = \
            self._species_model.min_isothermal_transformation_temperature_value <= self._model.manufacturing_process.isothermal_transformation_temperature <= self._species_model.max_isothermal_transformation_temperature_value

