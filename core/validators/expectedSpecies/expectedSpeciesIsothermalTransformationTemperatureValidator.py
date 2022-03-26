from core.validators.base.models.errorTypeEnum import ErrorType
from core.validators.expectedSpecies.models.baseExpectedSpeciesValidator import BaseExpectedSpeciesValidator
from core.validators.expectedSpecies.models.species import Species
from data.models.adiDuctileIronModel import AdiDuctileIronModel


class ExpectedSpeciesIsothermalTransformationValidator(BaseExpectedSpeciesValidator):
    def __init__(self, model: AdiDuctileIronModel, species_model: Species):
        super().__init__(ErrorType.INVALID_EXPECTED_SPECIES_ISOTHERMAL_TRANSFORMATION_TEMPERATURE,
                         "Expected species - isothermal transformation temperature validator", model, species_model)

    def validate(self) -> None:
        self._occurs = \
            not (self._species_model.min_isothermal_transformation_temperature_value <= \
                 self._model.manufacturing_process.isothermal_transformation_temperature <= \
                 self._species_model.max_isothermal_transformation_temperature_value)
